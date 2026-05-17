## 9.11 Kiểm soát bộ đệm một cách tường minh (Explicit cache control)
Các bộ vi xử lý mang trong mình tập lệnh SSE và SSE2 sở hữu các lệnh nhất định cho phép bạn kiểm soát (manipulate) bộ nhớ đệm dữ liệu. Những lệnh này có thể được tiếp cận từ các trình biên dịch có hỗ trợ cho các hàm bản thể (intrinsic functions) (ví dụ như Microsoft, Intel và Gnu). Các trình biên dịch khác sẽ cần sử dụng mã hợp ngữ (assembly code) để truy cập những tập lệnh này.

| Chức năng (Function) | Tên hợp ngữ (Assembly name) | Tên hàm bản thể (Intrinsic function name) | Tập lệnh (Instruction set) |
| --- | --- | --- | --- |
| Lấy dữ liệu trước (Prefetch) | PREFETCH | _mm_prefetch | SSE |
| Lưu 4 byte bỏ qua bộ đệm | MOVNTI | _mm_stream_si32 | SSE2 |
| Lưu 8 byte bỏ qua bộ đệm | MOVNTQ | _mm_stream_pi | SSE |
| Lưu 16 byte bỏ qua bộ đệm | MOVNTPS | _mm_stream_ps | SSE |
| Lưu 16 byte bỏ qua bộ đệm | MOVNTPD | _mm_stream_pd | SSE2 |
| Lưu 16 byte bỏ qua bộ đệm | MOVNTDQ | _mm_stream_si128 | SSE2 |
*Bảng 9.2 Các lệnh kiểm soát bộ đệm.*

Vẫn còn tồn tại các lệnh kiểm soát bộ đệm khác ngoài những cái tên được đề cập trong bảng 9.2, chẳng hạn như các lệnh tuôn xả (flush) và hàng rào cản (fence), nhưng những lệnh này thì hầu như không liên quan đến việc tối ưu hóa.

### Lấy dữ liệu trước (Prefetching data)
Lệnh lấy trước dữ liệu (prefetch) có thể được sử dụng cho việc lấy một dòng bộ đệm mà chúng ta dự tính sẽ sử dụng sau này trong luồng chạy của chương trình. Tuy nhiên, nó không cải thiện được chút tốc độ thực thi nào trong bất kỳ ví dụ nào mà tôi từng thử nghiệm. Lý do là vì các bộ xử lý hiện đại sẽ tự động thực hiện lấy dữ liệu trước nhờ cơ chế thực thi không tuần tự (out-of-order execution) và các cơ chế dự đoán bậc cao. Các bộ vi xử lý hiện đại có khả năng tự động thực hiện nạp dữ liệu trước đối với các mô thức truy cập thông thường (regular access patterns) bao gồm nhiều luồng số liệu (multiple streams) với những khoảng cách trượt dài khác nhau (different strides). Vì thế, bạn không cần phải nạp dữ liệu một cách tường minh (explicitly) miễn là thao tác truy cập dữ liệu đã được bố trí thành những mô thức chung với các khoảng trượt độ dài cố định.

### Thao tác lưu bộ nhớ bỏ qua bộ đệm (Uncached memory store)
Một thao tác viết bỏ qua bộ đệm (uncached write) thì đắt đỏ hơn là một thao tác đọc không đệm bởi lẽ thao tác viết khiến toàn bộ dòng bộ đệm phải được đọc vào và rồi viết trả lại.

Các lệnh viết không tạm thời (nontemporal write instructions - MOVNT) được thiết kế ra để giải quyết vấn đề này. Những lệnh này thực hiện thao tác viết trực tiếp vào bộ nhớ chính mà không cần tải một dòng bộ đệm nào. Điều này mang lại lợi thế cho những trường hợp chúng ta đang thực hiện lệnh viết vào một vùng nhớ không dùng đệm và chúng ta cũng không có mong chờ gì về việc sẽ phải đọc từ cùng một vị trí hoặc một địa chỉ liền kề một lần nữa trước khi dòng bộ nhớ đệm kia kịp bị loại bỏ. Đừng lẫn lộn sử dụng các lệnh viết dạng không tạm thời (nontemporal writes) chung với những thao tác viết hay đọc bình thường nhắm vào một vùng không gian bộ nhớ.

Các lệnh thực hiện thao tác viết dạng không tạm thời sẽ không phù hợp cho trường hợp của ví dụ 9.5 vì chúng ta đang tiến hành đọc và viết trên cùng một địa chỉ nên bất kể như thế nào thì một dòng không gian bộ đệm cũng sẽ được tải lên. Nếu chúng ta sửa đổi ví dụ 9.5 theo cách để nó chỉ việc thực hiện việc viết, thì sức ảnh hưởng từ những lệnh viết không tạm thời mới trở nên đáng chú ý. Ví dụ sau đây dùng để thực hiện việc hoán vị cho ma trận rồi lưu giữ kết quả ở một cấu trúc mảng khác.

```cpp
// Example 9.6a 
const int SIZE = 512; // number of rows and columns in matrix 
 
// function to transpose and copy matrix 
void TransposeCopy(double a[SIZE][SIZE], double b[SIZE][SIZE]) { 
   int r, c;  
   for (r = 0; r < SIZE; r++) { 
      for (c = 0; c < SIZE; c++) { 
         a[c][r] = b[r][c]; 
      } 
   } 
} 
```

Chức năng này thực hiện lệnh viết vào ma trận `a` dựa theo phương pháp tiến dần trên chiều cột (column-wise manner), nơi khoảng cách bước trượt tới hạn (critical stride) gây ra hệ quả là mọi thao tác viết đều tự nạp mới một dòng bộ đệm ngay trên cả hai không gian đệm cấp 1 và cấp 2. Thông qua việc tận dụng lệnh viết mang hình thức không tạm thời (nontemporal write), ta sẽ chặn bộ đệm cấp 2 thực hiện thao tác tải bất kỳ một dòng đệm nào dành riêng cho ma trận `a`:

```cpp
// Example 9.6b. 
#include "xmmintrin.h"  // header for intrinsic functions 
 
// This function stores a double without loading a cache line: 
static inline void StoreNTD(double * dest, double const & source) { 
   _mm_stream_pi((__m64*)dest, *(__m64*)&source);  // MOVNTQ 
   _mm_empty();                                    // EMMS 
} 
 
const int SIZE = 512; // number of rows and columns in matrix 
// function to transpose and copy matrix 
void TransposeCopy(double a[SIZE][SIZE], double b[SIZE][SIZE]) { 
   int r, c;  
   for (r = 0; r < SIZE; r++) { 
      for (c = 0; c < SIZE; c++) { 
         StoreNTD(&a[c][r], b[r][c]); 
      } 
   } 
} 
```

Phần thời gian của quá trình thực thi trên mỗi ô ma trận dành cho những kích cỡ đa dạng của các ma trận đã được ghi đo lại trên một dàn máy tính tính dùng chip Pentium 4. Thông tin cho kết quả đã thu thập có độ trình bày theo như những nội dung bên dưới:
