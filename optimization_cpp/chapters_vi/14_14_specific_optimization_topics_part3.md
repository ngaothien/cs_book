Chúng ta có thể kiểm tra xem một số thực dấu phẩy động có bằng 0 hay không bằng cách kiểm tra tất cả các bit ngoại trừ bit dấu:

```cpp
// Ví dụ 14.25
union {
   float f;
   int i;
} u;
if (u.i & 0x7FFFFFFF) { // kiểm tra các bit 0 - 30
   // f khác 0
}
else {
   // f bằng 0
}
```

Chúng ta có thể nhân một số thực dấu phẩy động khác 0 với $2^n$ bằng cách cộng $n$ vào số mũ:

```cpp
// Ví dụ 14.26
union {
   float f;
   int i;
} u;
int n;
if (u.i & 0x7FFFFFFF) { // kiểm tra xem có khác 0 không
   u.i += n << 23;      // cộng n vào số mũ
}
```

Ví dụ 14.26 không kiểm tra lỗi tràn số (overflow) và chỉ hoạt động đối với $n$ dương. Bạn có thể chia cho $2^n$ bằng cách trừ $n$ khỏi số mũ nếu không có nguy cơ xảy ra lỗi tràn dưới (underflow).

Thực tế là việc biểu diễn của số mũ được thêm một giá trị thiên vị (biased) cho phép chúng ta so sánh hai số thực dấu phẩy động dương một cách đơn giản bằng cách so sánh chúng như các số nguyên:

```cpp
// Ví dụ 14.27
union {
   float f;
   int i;
} u, v;
if (u.i > v.i) {
   // u.f > v.f nếu cả hai đều dương
}
```

Ví dụ 14.27 giả định rằng chúng ta biết u.f và v.f đều dương. Nó sẽ thất bại nếu cả hai đều âm hoặc nếu một số là 0 và số kia là -0 (số 0 với bit dấu được thiết lập).

Chúng ta có thể dịch bit dấu ra ngoài (shift out) để so sánh các giá trị tuyệt đối:

```cpp
// Ví dụ 14.28
union {
   float f;
   unsigned int i;
} u, v;
if (u.i * 2 > v.i * 2) {
   // abs(u.f) > abs(v.f)
}
```

Phép nhân với 2 trong ví dụ 14.28 sẽ dịch chuyển bit dấu ra ngoài sao cho các bit còn lại đại diện cho một hàm tăng đơn điệu (monotonically increasing function) của giá trị tuyệt đối của số thực dấu phẩy động.

Chúng ta có thể chuyển đổi một số nguyên trong khoảng $0 \le n < 2^{23}$ thành một số thực dấu phẩy động trong khoảng $[1.0, 2.0)$ bằng cách thiết lập các bit phân số (fraction bits):

```cpp
// Ví dụ 14.29
union {
   float f;
   int i;
} u;
int n;
u.i = (n & 0x7FFFFF) | 0x3F800000; // Bây giờ 1.0 <= u.f < 2.0
```

Phương pháp này hữu ích cho các trình tạo số ngẫu nhiên (random number generators).

Nói chung, việc truy cập một biến dấu phẩy động như một số nguyên sẽ nhanh hơn nếu nó được lưu trữ trong bộ nhớ (memory), nhưng sẽ không nhanh hơn nếu nó là một biến thanh ghi (register variable). Kiểu `union` buộc biến phải được lưu trữ trong bộ nhớ, ít nhất là tạm thời. Do đó, việc sử dụng các phương pháp trong các ví dụ trên sẽ là một bất lợi nếu các phần khác gần đó của mã có thể hưởng lợi từ việc sử dụng các thanh ghi cho cùng các biến đó.

Trong các ví dụ này, chúng ta đang sử dụng `union` thay vì ép kiểu (type casting) các con trỏ bởi vì phương pháp này an toàn hơn. Việc ép kiểu con trỏ có thể không hoạt động trên các trình biên dịch dựa vào quy tắc strict aliasing của chuẩn C, quy tắc này chỉ định rằng các con trỏ có kiểu khác nhau không thể trỏ tới cùng một đối tượng, ngoại trừ các con trỏ `char`.

Các ví dụ trên đều sử dụng độ chính xác đơn (single precision). Việc sử dụng độ chính xác kép (double precision) trong các hệ thống 32 bit làm phát sinh thêm một số phức tạp. Một biến `double` được biểu diễn bằng 64 bit, nhưng các hệ thống 32 bit không hỗ trợ vốn có (inherent support) cho số nguyên 64 bit. Nhiều hệ thống 32 bit cho phép bạn định nghĩa các số nguyên 64 bit, nhưng thực chất chúng được biểu diễn dưới dạng hai số nguyên 32 bit, điều này kém hiệu quả hơn. Bạn có thể sử dụng 32 bit cao hơn (upper 32 bits) của một số `double` cho phép truy cập vào bit dấu, số mũ và phần quan trọng nhất của phân số. Ví dụ, để kiểm tra dấu của một số `double`:

```cpp
// Ví dụ 14.23b
union {
   double d;
   int i[2];
} u;
if (u.i[1] < 0) {  // kiểm tra bit dấu
   // u.d là số âm hoặc -0
}
```

Không nên thay đổi một biến `double` bằng cách chỉ sửa đổi một nửa của nó, ví dụ nếu bạn muốn đảo bit dấu trong ví dụ trên bằng `u.i[1] ^= 0x80000000;` vì điều này có khả năng tạo ra độ trễ chuyển tiếp lưu trữ (store forwarding delay) trong CPU (Xem tài liệu 3: "Kiến trúc vi mô của CPU Intel, AMD và VIA"). Điều này có thể tránh được trong các hệ thống 64 bit bằng cách sử dụng một số nguyên 64 bit chứ không phải hai số nguyên 32 bit để gán bí danh (alias) lên biến `double`.

Một vấn đề khác đối với việc truy cập 32 bit của một biến `double` 64 bit là nó không thể chuyển đổi (portable) sang các hệ thống sử dụng kiểu lưu trữ big-endian. Các ví dụ 14.23b và 14.30 do đó sẽ cần được sửa đổi nếu được triển khai trên các nền tảng khác có lưu trữ big-endian. Tất cả các nền tảng x86 (Windows, Linux, BSD, Mac OS dựa trên Intel, v.v.) đều có kiểu lưu trữ little-endian, nhưng các hệ thống khác có thể có lưu trữ big-endian (ví dụ PowerPC).

Chúng ta có thể thực hiện so sánh xấp xỉ các biến `double` bằng cách so sánh các bit từ 32-62. Điều này có thể hữu ích để tìm phần tử lớn nhất về mặt số học trong một ma trận để sử dụng làm chốt (pivot) trong phép khử Gauss (Gauss elimination). Phương pháp trong ví dụ 14.28 có thể được triển khai như thế này trong tìm kiếm pivot:

```cpp
// Ví dụ 14.30
const int size = 100;
// Mảng chứa 100 số double:
union {double d; unsigned int u[2];} a[size];
unsigned int absvalue, largest_abs = 0;
int i, largest_index = 0;
for (i = 0; i < size; i++) {
   // Lấy 32 bit cao hơn của a[i] và dịch chuyển bit dấu ra ngoài:
   absvalue = a[i].u[1] * 2;
   // Tìm phần tử lớn nhất về mặt số học (xấp xỉ):
   if (absvalue > largest_abs) {
      largest_abs = absvalue;
      largest_index = i;
   }
}
```

Ví dụ 14.30 tìm phần tử có giá trị số học lớn nhất trong một mảng, hoặc xấp xỉ như vậy. Nó có thể thất bại trong việc phân biệt các phần tử có sự khác biệt tương đối nhỏ hơn $2^{-20}$, nhưng như thế này là đủ chính xác cho mục đích tìm kiếm một phần tử chốt (pivot) phù hợp. Phép so sánh số nguyên có khả năng nhanh hơn phép so sánh dấu phẩy động. Trên các hệ thống big endian, bạn phải thay thế `u[1]` bằng `u[0]`.

## 14.10 Các hàm toán học (Mathematical functions)

Các hàm toán học phổ biến nhất như logarit, hàm mũ, hàm lượng giác, v.v. được triển khai bằng phần cứng trong các CPU x86. Tuy nhiên, việc triển khai bằng phần mềm (software implementation) thường nhanh hơn việc triển khai bằng phần cứng (hardware implementation) trong hầu hết các trường hợp khi tập lệnh SSE2 có sẵn. Các trình biên dịch tốt nhất sử dụng việc triển khai bằng phần mềm nếu tập lệnh SSE2 được bật.

Lợi thế của việc sử dụng một triển khai phần mềm so với triển khai phần cứng của các hàm này cao hơn đối với độ chính xác đơn (single precision) so với độ chính xác kép (double precision). Nhưng việc triển khai phần mềm cũng nhanh hơn triển khai phần cứng trong hầu hết các trường hợp, ngay cả với độ chính xác kép.

Bạn có thể sử dụng thư viện hàm toán học của Intel với một trình biên dịch khác bằng cách bao gồm tệp thư viện `libmmt.lib` và tệp tiêu đề (header) `mathimf.h` đi kèm với trình biên dịch Intel C++. Thư viện này chứa nhiều hàm toán học hữu ích. Rất nhiều hàm toán học nâng cao được cung cấp trong Math Kernel Library của Intel, có sẵn tại www.intel.com. (Xem thêm trang 122). Thư viện lõi toán học của AMD chứa các hàm tương tự, nhưng được tối ưu hóa ít hơn.

Lưu ý rằng các thư viện hàm của Intel không sử dụng tập lệnh tốt nhất có thể khi chạy trên các bộ xử lý không phải của Intel (xem trang 133 để biết cách khắc phục hạn chế này).

## 14.11 Thư viện tĩnh và thư viện liên kết động (Static versus dynamic libraries)

Các thư viện hàm có thể được triển khai dưới dạng thư viện liên kết tĩnh (static link libraries - `*.lib`, `*.a`) hoặc thư viện liên kết động (dynamic link libraries), còn được gọi là shared objects (`*.dll`, `*.so`). Cơ chế của liên kết tĩnh là linker sẽ trích xuất (extract) các hàm được cần thiết từ tệp thư viện và sao chép chúng vào tệp thực thi (executable file). Chỉ có tệp thực thi là cần được phân phối cho người dùng cuối (end user).

Liên kết động hoạt động khác biệt. Liên kết tới một hàm trong một thư viện động được giải quyết (resolved) khi thư viện được tải (loaded) hoặc tại thời điểm chạy (run time). Do đó, cả tệp thực thi và một hoặc nhiều thư viện động đều được nạp vào bộ nhớ khi chương trình chạy. Cả tệp thực thi và tất cả các thư viện động cần phải được phân phối cho người dùng cuối.

Ưu điểm của việc sử dụng liên kết tĩnh thay vì liên kết động là:

*   Liên kết tĩnh chỉ bao gồm phần của thư viện thực sự được ứng dụng cần dùng đến, trong khi liên kết động làm cho toàn bộ thư viện (hoặc ít nhất là một phần lớn của nó) được nạp vào bộ nhớ ngay cả khi chỉ cần dùng một hàm duy nhất từ thư viện.
*   Tất cả mã được gói gọn trong một tệp thực thi duy nhất khi sử dụng liên kết tĩnh. Liên kết động làm cho việc phải nạp nhiều tệp khi chương trình được khởi chạy là cần thiết.
*   Sẽ mất nhiều thời gian hơn để gọi một hàm trong thư viện động so với trong thư viện tĩnh vì nó cần phải nhảy qua một con trỏ trong bảng import (import table) và có thể là cả một lần tra cứu (lookup) trong bảng liên kết thủ tục (procedure linkage table - PLT).
*   Không gian bộ nhớ trở nên phân mảnh (fragmented) hơn khi mã được phân tán giữa nhiều thư viện động. Các thư viện động được nạp tại các địa chỉ bộ nhớ tròn (round memory addresses) chia hết cho kích thước trang bộ nhớ (memory page size - 4096). Điều này sẽ khiến tất cả các thư viện động cạnh tranh (contend) cho cùng các dòng bộ nhớ cache (cache lines). Điều này khiến bộ đệm mã (code caching) và bộ đệm dữ liệu (data caching) kém hiệu quả hơn.
*   Thư viện động kém hiệu quả hơn ở một số hệ thống vì nhu cầu về mã độc lập với vị trí (position-independent code), xem bên dưới.
*   Cài đặt một ứng dụng thứ hai sử dụng phiên bản mới hơn của cùng một thư viện động có thể thay đổi hành vi của ứng dụng đầu tiên nếu liên kết động được sử dụng, nhưng sẽ không xảy ra nếu liên kết tĩnh được sử dụng.

Ưu điểm của liên kết động là:

*   Nhiều ứng dụng chạy đồng thời có thể chia sẻ cùng các thư viện động mà không cần nạp nhiều hơn một phiên bản (instance) của thư viện vào bộ nhớ. Điều này hữu ích trên các máy chủ chạy đồng thời nhiều tiến trình. Trên thực tế, chỉ có phân vùng mã (code section) và các phân vùng dữ liệu chỉ đọc (read-only data sections) là có thể được chia sẻ. Bất kỳ phân vùng dữ liệu có thể ghi nào cũng cần một phiên bản (instance) cho mỗi tiến trình (process).
*   Thư viện động có thể được cập nhật lên phiên bản mới mà không cần cập nhật chương trình gọi nó.
*   Một thư viện động có thể được gọi từ các ngôn ngữ lập trình không hỗ trợ liên kết tĩnh.
*   Thư viện động có thể hữu ích để tạo các phần bổ trợ (plug-ins) bổ sung tính năng vào một chương trình hiện có.

Cân nhắc những ưu điểm của từng phương pháp như trên, rõ ràng là liên kết tĩnh nên được ưu tiên hơn cho các hàm đòi hỏi tốc độ khắt khe. Nhiều thư viện hàm có sẵn ở cả hai phiên bản tĩnh và động. Khuyến nghị sử dụng phiên bản tĩnh nếu tốc độ là quan trọng.

Một số hệ thống cho phép liên kết hàm lười (lazy binding). Nguyên tắc của lazy binding là địa chỉ của một hàm được liên kết không được giải quyết (resolved) khi chương trình được nạp, mà chờ đến lần đầu tiên hàm đó được gọi. Lazy binding có thể hữu ích cho các thư viện lớn, nơi chỉ có một số ít các hàm thực sự được gọi trong một phiên bản (session). Nhưng lazy binding chắc chắn làm giảm hiệu suất cho các hàm được gọi. Sự chậm trễ đáng kể xảy ra khi một hàm được gọi lần đầu tiên vì nó cần nạp trình liên kết động (dynamic linker).

Sự chậm trễ trên lazy binding dẫn đến một vấn đề về tính khả dụng (usability) trong các chương trình tương tác vì thời gian phản hồi (chẳng hạn cho một nhấp chuột trên menu) trở nên không nhất quán và đôi khi dài quá mức chấp nhận được. Do đó, lazy binding chỉ nên được sử dụng cho các thư viện rất lớn.

Địa chỉ bộ nhớ mà một thư viện động được nạp không thể xác định trước, vì một địa chỉ cố định có thể xung đột với một thư viện động khác yêu cầu cùng địa chỉ. Có hai phương pháp thường dùng để xử lý vấn đề này:

1.  **Định vị lại (Relocation)**. Tất cả các con trỏ và địa chỉ trong mã được sửa đổi, nếu cần, cho khớp với địa chỉ tải (load address) thực tế. Việc tái định vị được thực hiện bởi trình liên kết (linker) và trình tải (loader).
2.  **Mã độc lập với vị trí (Position-independent code)**. Tất cả các địa chỉ trong mã có tính tương đối với vị trí hiện tại (self-relative).

Các tệp DLL trong Windows sử dụng sự tái định vị (relocation). Các DLL được tái định vị bởi trình liên kết tới một địa chỉ nạp cụ thể. Nếu địa chỉ này không trống (không vacant) thì DLL được tái định vị (rebased) một lần nữa bởi trình tải (loader) tới một địa chỉ khác. Một lệnh gọi từ tệp thực thi chính (main executable) tới một hàm trong một DLL sẽ đi qua một bảng import (import table) hoặc một con trỏ. Một biến trong một DLL có thể được truy cập từ chương trình chính thông qua một con trỏ được import, nhưng tính năng này hiếm khi được dùng. Việc trao đổi dữ liệu hoặc con trỏ tới dữ liệu thông qua các lệnh gọi hàm thì phổ biến hơn. Việc tham chiếu nội bộ (internal references) tới dữ liệu nằm trong DLL sử dụng các tham chiếu tuyệt đối (absolute references) trong chế độ 32 bit và hầu hết là sử dụng các tham chiếu tương đối (relative references) trong chế độ 64 bit. Cách thứ hai có phần hiệu quả hơn vì các tham chiếu tương đối không cần tái định vị vào lúc nạp (load time).

Các đối tượng được chia sẻ (Shared objects) trong các hệ thống giống như Unix mặc định sử dụng mã độc lập với vị trí (position-independent code). Phương pháp này kém hiệu quả hơn so với việc tái định vị, đặc biệt trong chế độ 32 bit. Phần tiếp theo mô tả cách thức hoạt động của phương pháp này và đề xuất các biện pháp để tránh các chi phí (costs) của position-independent code.

## 14.12 Mã độc lập vị trí (Position-independent code)

Các Shared objects trong các hệ thống Linux, BSD và Mac thường sử dụng cái gọi là mã độc lập với vị trí (position-independent code). Tên gọi "position-independent code" (mã độc lập với vị trí) thực chất ngụ ý nhiều hơn những gì nó thể hiện. Một mã được biên dịch như là position-independent (độc lập với vị trí) có các tính năng sau:

*   Phân vùng mã (code section) không chứa các địa chỉ tuyệt đối cần được tái định vị (relocation), mà chỉ chứa các địa chỉ mang tính tương đối (self-relative). Do đó, phân vùng mã có thể được tải (loaded) ở một địa chỉ bộ nhớ tùy ý (arbitrary) và được chia sẻ (shared) giữa nhiều tiến trình (processes) với nhau.
*   Phân vùng dữ liệu (data section) không được chia sẻ giữa nhiều tiến trình vì nó thường chứa dữ liệu có thể ghi (writeable data). Vì vậy, phân vùng dữ liệu có thể chứa các con trỏ hoặc địa chỉ cần được tái định vị.
*   Tất cả các hàm và dữ liệu public có thể bị ghi đè (overridden) trong Linux và BSD. Nếu một hàm trong tệp thực thi chính (main executable) có cùng tên với một hàm trong một shared object, thì phiên bản trong chương trình chính sẽ được ưu tiên (take precedence), không chỉ khi được gọi từ chương trình chính mà còn khi được gọi từ trong shared object. Tương tự như vậy, khi một biến toàn cục (global variable) trong chương trình chính có cùng tên với một biến toàn cục trong shared object, thì phiên bản trong chương trình chính sẽ được sử dụng, ngay cả khi nó được truy cập từ shared object. Tính năng được gọi là chèn biểu tượng (symbol interposition) này nhằm mục đích bắt chước hành vi của các thư viện tĩnh. Một shared object có một bảng các con trỏ trỏ tới các hàm của nó, gọi là bảng liên kết thủ tục (procedure linkage table - PLT) và một bảng các con trỏ trỏ tới các biến của nó gọi là bảng độ lệch toàn cục (global offset table - GOT) nhằm triển khai tính năng "override" này. Tất cả các quyền truy cập vào các hàm và các biến public đều thông qua PLT và GOT.

Tính năng chèn biểu tượng cho phép ghi đè các hàm và dữ liệu public trong Linux và BSD đi kèm với một cái giá cao, và trong hầu hết các thư viện, nó không bao giờ được sử dụng. Mỗi khi một hàm trong shared object được gọi, cần phải tìm kiếm địa chỉ hàm trong bảng PLT (procedure linkage table). Và bất cứ khi nào truy cập vào một biến public trong shared object, trước tiên cần phải tìm địa chỉ biến trong bảng GOT (global offset table). Các hoạt động tra cứu bảng (table lookups) này là cần thiết ngay cả khi truy cập hàm hoặc biến từ trong chính shared object đó. Rõ ràng, tất cả các hoạt động tra cứu bảng này làm chậm đáng kể quá trình thực thi. Một cuộc thảo luận chi tiết hơn có thể được tìm thấy tại http://www.macieira.org/blog/2012/01/sorry-state-of-dynamic-libraries-on-linux/

Một gánh nặng nghiêm trọng khác là việc tính toán các tham chiếu tương đối (self-relative references) trong chế độ 32 bit. Tập lệnh x86 32 bit không có lệnh để lập địa chỉ dữ liệu tương đối (self-relative addressing of data). Mã trải qua các bước sau để truy cập một đối tượng dữ liệu public: (1) nhận địa chỉ của chính nó thông qua một cuộc gọi hàm. (2) tìm bảng GOT thông qua một địa chỉ tương đối. (3) tra cứu địa chỉ của đối tượng dữ liệu trong GOT, và cuối cùng (4) truy cập đối tượng dữ liệu thông qua địa chỉ này. Bước (1) không cần thiết ở chế độ 64 bit vì tập lệnh x86-64 có hỗ trợ truy cập dữ liệu tương đối.

Trong Linux và BSD 32 bit, quá trình tra cứu GOT chậm chạp này được sử dụng cho tất cả các dữ liệu tĩnh, bao gồm cả dữ liệu cục bộ (local data) không cần tính năng "ghi đè" (override feature). Điều này bao gồm các biến tĩnh (static variables), hằng số dấu phẩy động (floating point constants), hằng chuỗi (string constants) và các mảng được khởi tạo (initialized arrays). Tôi không có lời giải thích nào cho lý do vì sao tiến trình làm chậm này lại được sử dụng ngay cả khi nó không cần thiết.

Rõ ràng, cách tốt nhất để tránh position-independent code nặng nề và tra cứu bảng (table lookup) là sử dụng liên kết tĩnh (static linking), như đã được giải thích ở chương trước (trang 149). Trong những trường hợp không thể tránh liên kết động, có nhiều cách khác nhau để tránh các tính năng tốn thời gian của position-independent code. Các phương pháp giải quyết này phụ thuộc vào từng hệ thống, như được giải thích dưới đây.

**Shared objects trong Linux 32 bit**
Shared objects thường được biên dịch với tùy chọn `-fpic` theo sổ tay hướng dẫn của trình biên dịch Gnu. Tùy chọn này làm cho phần phân vùng mã (code section) trở nên độc lập với vị trí, tạo ra một bảng PLT cho tất cả các hàm và một bảng GOT cho tất cả dữ liệu public và tĩnh.

Có thể biên dịch một shared object mà không cần tùy chọn `-fpic`. Khi đó chúng ta thoát khỏi tất cả các vấn đề đề cập ở trên. Bây giờ mã sẽ chạy nhanh hơn bởi vì chúng ta có thể truy cập các biến nội bộ (internal variables) và các hàm nội bộ trong một bước duy nhất thay vì các cơ chế tính toán địa chỉ và tra cứu bảng phức tạp như giải thích ở trên. Một shared object được biên dịch không có `-fpic` sẽ nhanh hơn nhiều, ngoại trừ có lẽ đối với một shared object rất lớn mà ở đó hầu hết các hàm đều không bao giờ được gọi tới. Nhược điểm của việc biên dịch không có `-fpic` trong Linux 32 bit là trình tải (loader) sẽ có nhiều tham chiếu cần tái định vị hơn (relocate), nhưng những phép tính địa chỉ này chỉ được thực hiện một lần, trong khi các tính toán địa chỉ lúc chạy (runtime address calculations) phải được thực hiện ở mọi truy cập.

Phân vùng mã (code section) cần một bản sao (instance) cho từng tiến trình khi được biên dịch không có `-fpic` bởi vì các sự tái định vị trong phân vùng mã sẽ khác nhau đối với mỗi tiến trình. Rõ ràng, chúng sửa mất khả năng ghi đè (override) các biểu tượng công khai (public symbols), nhưng tính năng này hiếm khi cần thiết.

Bạn nên tránh dùng các biến toàn cục (global variables) hoặc ẩn chúng vì lợi ích di chuyển (portability) sang chế độ 64 bit, như được giải thích bên dưới.

**Shared objects trong Linux 64 bit**
Thủ tục tính toán các địa chỉ tương đối (self-relative addresses) đơn giản hơn nhiều ở chế độ 64 bit bởi vì tập lệnh 64 bit có hỗ trợ cho việc định địa chỉ dữ liệu tương đối. Sự cần thiết của position-independent code (mã độc lập với vị trí) đặc biệt nhỏ hơn vì dù sao các địa chỉ tương đối (relative addresses) thường được sử dụng mặc định trong mã 64 bit. Tuy nhiên, chúng ta vẫn muốn loại bỏ việc tra cứu GOT và PLT cho các tham chiếu nội bộ.

Nếu chúng ta biên dịch shared object không có `-fpic` ở chế độ 64 bit, chúng ta sẽ gặp một vấn đề khác. Trình biên dịch đôi khi sử dụng các địa chỉ tuyệt đối 32 bit (32-bit absolute addresses), chủ yếu cho các mảng tĩnh (static arrays). Điều này hoạt động tốt trong tệp thực thi chính bởi vì nó chắc chắn được nạp tại một địa chỉ dưới 2 GB, nhưng không phải trong một shared object, thường được nạp ở một địa chỉ cao hơn không thể đạt được bằng một địa chỉ 32 bit (có dấu). Trình liên kết (linker) sẽ tạo ra một thông báo lỗi trong trường hợp này. Giải pháp tốt nhất là biên dịch với tùy chọn `-fpie` thay vì `-fpic`. Điều này sẽ tạo ra các địa chỉ tương đối trong phân vùng mã, nhưng nó sẽ không sử dụng GOT và PLT cho các tham chiếu nội bộ. Do đó, nó sẽ chạy nhanh hơn khi so với biên dịch bằng `-fpic` và nó sẽ không gặp những nhược điểm như được đề cập ở trên đối với trường hợp 32 bit. Tùy chọn `-fpie` ít hữu ích hơn trong chế độ 32 bit, nơi nó vẫn sử dụng bảng GOT.

Một khả năng khác là biên dịch với `-mcmodel=large`, nhưng tùy chọn này sẽ sử dụng các địa chỉ 64 bit đầy đủ cho mọi thứ, điều này khá là kém hiệu quả, và nó sẽ tạo ra sự tái định vị (relocations) trong phân vùng mã dẫn đến việc phân vùng mã không thể chia sẻ được.

Bạn không thể dùng các biến public trong một shared object 64 bit được tạo bằng tùy chọn `-fpie` bởi vì trình liên kết (linker) tạo ra thông báo lỗi khi nó thấy một tham chiếu tương đối (relative reference) tới một biến public trong khi nó lại mong đợi một mục nhập GOT (GOT entry). Bạn có thể tránh lỗi này bằng cách tránh mọi biến public. Tất cả các biến toàn cục (global variables - tức là các biến được định nghĩa bên ngoài hàm) nên bị ẩn đi bằng cách sử dụng khai báo "static" hoặc `__attribute__((visibility ("hidden")))`.

Trình biên dịch gnu phiên bản 5.1 trở lên có một tùy chọn `-fno-semantic-interposition`, khiến nó tránh việc sử dụng tra cứu PLT và GOT, nhưng chỉ dành cho các tham chiếu (references) trong cùng một tệp. Có thể thu được tác dụng tương tự bằng cách dùng mã hợp ngữ nội tuyến (inline assembly code) để cung cấp cho biến hai tên, một toàn cục (global) và một cục bộ (local), và sử dụng tên cục bộ cho các tham chiếu cục bộ.

Mặc dù có những thủ thuật này, bạn vẫn có thể nhận được thông báo lỗi: "`relocation R_X86_64_PC32 against symbol functionname can not be used when making a shared object; recompile with -fPIC`", khi mà shared object được tạo từ nhiều mô-đun (tệp nguồn) và có lệnh gọi từ mô-đun này sang mô-đun khác. Tôi vẫn chưa tìm được cách giải quyết vấn đề này.

**Shared objects trong BSD**
Shared objects trong BSD hoạt động tương tự như trong Linux.

**Mac OS X 32 bit**
Các trình biên dịch cho Mac OS X 32 bit luôn mặc định tạo ra position-independent code và lazy binding, ngay cả khi shared objects không được sử dụng. Phương pháp hiện đang được sử dụng để tính toán địa chỉ tương đối (self-relative addresses) trong mã Mac 32 bit dùng một cách kém may mắn khiến làm chậm quá trình thực thi do làm cho địa chỉ trả về (return addresses) bị dự đoán sai (mispredicted) (Xem tài liệu 3: "The microarchitecture of Intel, AMD and VIA CPUs" để xem giải thích về return prediction - dự đoán lệnh trả về).

Tất cả mã không thuộc về shared object đều có thể được tăng tốc đáng kể chỉ bằng cách tắt cờ (flag) position-independent code trong trình biên dịch. Do đó, hãy nhớ luôn chỉ định tùy chọn trình biên dịch `-fno-pic` khi biên dịch cho Mac OS X 32 bit, trừ phi bạn đang tạo một shared object.

Bạn có thể tạo các shared objects mà không cần position-independent code khi bạn biên dịch với tùy chọn `-fno-pic` và liên kết (link) với tùy chọn `-read_only_relocs suppress`.

Bảng GOT và PLT không được dùng cho các tham chiếu nội bộ (internal references).

**Mac OS X 64 bit**
Phân vùng mã (code section) luôn là độc lập với vị trí (position-independent) bởi vì đây là giải pháp hiệu quả nhất cho mô hình bộ nhớ (memory model) được dùng ở đây. Tùy chọn trình biên dịch `-fno-pic` rõ ràng là không có tác dụng.

Bảng GOT và PLT không được dùng cho các tham chiếu nội bộ.

Không cần thiết phải thực hiện các biện pháp phòng ngừa (precautions) đặc biệt nào để tăng tốc shared objects 64 bit trong Mac OS X.

## 14.13 Lập trình hệ thống (System programming)

Trình điều khiển thiết bị (Device drivers), quy trình phục vụ ngắt (interrupt service routines), lõi hệ thống (system core) và các luồng có mức ưu tiên cao (high-priority threads) là những lĩnh vực mà tốc độ đặc biệt quan trọng (speed is particularly critical). Một hàm ngốn nhiều thời gian trong mã hệ thống (system code) hoặc trong một luồng mức ưu tiên cao có thể có khả năng chặn (block) việc thực thi của mọi thứ khác.

Mã hệ thống phải tuân theo các quy tắc nhất định về việc dùng thanh ghi (register use), như đã được giải thích trong chương "Việc dùng thanh ghi trong mã nhân" (Register usage in kernel code) của tài liệu 5: "Calling conventions for different C++ compilers and operating systems" (Các quy ước gọi hàm cho các hệ điều hành và trình biên dịch C++ khác nhau). Vì lý do này, bạn chỉ có thể dùng các trình biên dịch và các thư viện hàm nhằm dành cho mã hệ thống (system code). Mã hệ thống nên được viết bằng C, C++ hoặc hợp ngữ (assembly language).

Việc tiết kiệm (economize) dùng tài nguyên trong mã hệ thống là rất quan trọng. Phân bổ bộ nhớ động (Dynamic memory allocation) là đặc biệt nguy hiểm (risky) vì nó kéo theo rủi ro kích hoạt trình thu gom rác (garbage collector) vô cùng tốn thời gian vào những thời điểm bất tiện. Một hàng đợi (queue) nên được triển khai như là một bộ đệm vòng (circular buffer) có kích thước cố định, chứ không phải là một danh sách liên kết (linked list). Đừng dùng các container của STL. Xem trang 91.
