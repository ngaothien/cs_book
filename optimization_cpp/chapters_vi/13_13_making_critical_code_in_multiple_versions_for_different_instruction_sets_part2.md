## 13.4 Kiểm tra và bảo trì (Test and maintenance)

Có hai điều cần kiểm tra khi phần mềm sử dụng điều phối CPU:

1.  Bạn đạt được bao nhiêu tốc độ bằng cách sử dụng một phiên bản mã cụ thể.
2.  Kiểm tra xem tất cả các phiên bản mã có hoạt động chính xác không.

Bài kiểm tra tốc độ nên ưu tiên được thực hiện trên loại CPU mà mỗi nhánh mã cụ thể nhắm tới. Nói cách khác, bạn cần phải kiểm tra trên một vài CPU khác nhau nếu bạn muốn tối ưu hóa cho một vài CPU khác nhau.

Mặt khác, không nhất thiết phải có nhiều CPU khác nhau để xác minh rằng tất cả các nhánh mã đều hoạt động chính xác. Một nhánh mã dành cho tập lệnh thấp vẫn có thể chạy trên CPU có tập lệnh cao hơn. Do đó, bạn chỉ cần một CPU có tập lệnh cao nhất để kiểm tra tính chính xác của tất cả các nhánh. Vì vậy, nên đưa một tính năng kiểm tra vào mã cho phép bạn ghi đè lên bộ điều phối CPU và chạy bất kỳ nhánh mã nào cho mục đích kiểm tra.

Nếu mã được triển khai dưới dạng thư viện hàm hoặc mô-đun riêng biệt, thì nên tạo một chương trình kiểm tra có thể gọi tất cả các nhánh mã riêng biệt và kiểm tra chức năng của chúng. Điều này sẽ rất hữu ích cho việc bảo trì sau này. Tuy nhiên, đây không phải là một cuốn sách giáo khoa về lý thuyết kiểm thử phần mềm. Lời khuyên về cách kiểm tra một mô-đun phần mềm để đảm bảo tính đúng đắn phải được tìm ở nơi khác.

## 13.5 Triển khai (Implementation)

Cơ chế điều phối CPU có thể được triển khai ở các vị trí khác nhau, đưa ra quyết định điều phối tại các thời điểm khác nhau:

*   **Điều phối ở mỗi lần gọi (Dispatch on every call)**. Một cây phân nhánh hoặc câu lệnh switch dẫn đến phiên bản thích hợp của hàm tới hạn. Việc rẽ nhánh được thực hiện mỗi khi hàm tới hạn được gọi. Nhược điểm của phương pháp này là việc rẽ nhánh gây tốn thời gian.
*   **Điều phối ở lần gọi đầu tiên (Dispatch on first call)**. Hàm được gọi thông qua một con trỏ hàm, ban đầu trỏ đến một bộ điều phối (dispatcher). Bộ điều phối thay đổi con trỏ hàm và làm cho nó trỏ đến phiên bản hàm đúng. Ưu điểm của phương pháp này là nó không dành thời gian quyết định sử dụng phiên bản nào trong trường hợp hàm không bao giờ được gọi. Phương pháp này được minh họa trong ví dụ 13.1 bên dưới.
*   **Tạo con trỏ tại thời điểm khởi tạo (Make pointer at initialization)**. Chương trình hoặc thư viện có một thói quen khởi tạo được gọi trước lần gọi đầu tiên đến hàm tới hạn. Thói quen khởi tạo (initialization routine) sẽ đặt con trỏ hàm trỏ đến phiên bản đúng của hàm. Ưu điểm của phương pháp này là thời gian phản hồi là nhất quán đối với lệnh gọi hàm.
*   **Tải thư viện tại thời điểm khởi tạo (Load library at initialization)**. Mỗi phiên bản mã được triển khai trong một thư viện liên kết động riêng biệt (*.dll hoặc *.so). Chương trình có một thủ tục khởi tạo tải phiên bản thích hợp của thư viện. Phương pháp này hữu ích nếu thư viện rất lớn hoặc nếu các phiên bản khác nhau phải được biên dịch bằng các trình biên dịch khác nhau.
*   **Điều phối tại thời điểm tải (Dispatch at load time)**. Chương trình sử dụng bảng liên kết thủ tục (procedure linkage table - PLT) được khởi tạo khi chương trình được tải. Phương pháp này yêu cầu sự hỗ trợ của HĐH và có sẵn trong các phiên bản mới hơn của Linux và có lẽ cả Mac OS. Xem ví dụ 13.2 bên dưới.
*   **Điều phối tại thời điểm cài đặt (Dispatch at installation time)**. Mỗi phiên bản mã được triển khai trong một thư viện liên kết động riêng biệt (*.dll hoặc *.so). Chương trình cài đặt tạo một liên kết tượng trưng (symbolic link) tới phiên bản phù hợp của thư viện. Chương trình ứng dụng tải thư viện thông qua liên kết tượng trưng này.
*   **Sử dụng các file thực thi khác nhau (Use different executables)**. Phương pháp này có thể được sử dụng nếu các tập lệnh không tương thích với nhau. Bạn có thể tạo các file thực thi riêng biệt cho hệ thống 32-bit và 64-bit. Phiên bản phù hợp của chương trình có thể được chọn trong quá trình cài đặt hoặc bởi một đoạn mã mồi của file thực thi (executable file stub).

Nếu các phiên bản khác nhau của đoạn mã tới hạn được biên dịch bằng các trình biên dịch khác nhau thì nên chỉ định liên kết tĩnh (static linking) cho mọi hàm thư viện mà đoạn mã tới hạn gọi đến, như vậy bạn không phải phân phối tất cả các thư viện động (*.dll hoặc *.so) thuộc về từng trình biên dịch kèm theo ứng dụng.

Tính khả dụng của các tập lệnh khác nhau có thể được xác định bằng các lời gọi hệ thống (ví dụ: `IsProcessorFeaturePresent` trong Windows). Ngoài ra, bạn có thể gọi trực tiếp lệnh CPUID, hoặc sử dụng hàm phát hiện CPU mà tôi đã cung cấp trong thư viện www.agner.org/optimize/asmlib.zip. Tên của hàm này là `InstructionSet()`. Ví dụ sau cho thấy cách triển khai phương pháp điều phối ở lần gọi đầu tiên bằng cách sử dụng `InstructionSet()`:

```cpp
// Ví dụ 13.1
// Điều phối CPU ở lần gọi đầu tiên (CPU dispatching on first call)

// File tiêu đề cho InstructionSet()
#include "asmlib.h"

// Định nghĩa kiểu hàm với các tham số mong muốn
typedef int CriticalFunctionType(int parm1, int parm2);

// Khai báo nguyên mẫu hàm (Function prototype)
CriticalFunctionType CriticalFunction_Dispatch;

// Con trỏ hàm đóng vai trò là điểm vào (entry point).
// Sau lần gọi đầu tiên, nó sẽ trỏ đến phiên bản hàm phù hợp
CriticalFunctionType * CriticalFunction = &CriticalFunction_Dispatch;

// Phiên bản thấp nhất
int CriticalFunction_386(int parm1, int parm2) {...}

// Phiên bản SSE2
int CriticalFunction_SSE2(int parm1, int parm2) {...}

// Phiên bản AVX
int CriticalFunction_AVX(int parm1, int parm2) {...}

// Bộ điều phối. Sẽ chỉ được gọi ở lần đầu tiên
int CriticalFunction_Dispatch(int parm1, int parm2)
{
   // Lấy tập lệnh được hỗ trợ, sử dụng thư viện asmlib
   int level = InstructionSet();

   // Đặt con trỏ đến phiên bản phù hợp (Có thể sử dụng một bảng
   // các con trỏ hàm nếu có nhiều nhánh):
   if (level >= 11)
   {  // AVX được hỗ trợ
      CriticalFunction = &CriticalFunction_AVX;
   }
   else if (level >= 4)
   {  // SSE2 được hỗ trợ
      CriticalFunction = &CriticalFunction_SSE2;
   }
   else
   {  // Phiên bản chung (generic)
      CriticalFunction = &CriticalFunction_386;
   }

   // Bây giờ gọi phiên bản đã chọn
   return (*CriticalFunction)(parm1, parm2);
}

int main()
{
   int a, b, c;
   ...

   // Gọi hàm tới hạn thông qua con trỏ hàm
   a = (*CriticalFunction)(b, c);

   ...
   return 0;
}
```

Hàm `InstructionSet()` có sẵn trong thư viện hàm `asmlib`, được cung cấp với các phiên bản khác nhau cho các trình biên dịch khác nhau. Hàm này độc lập với hệ điều hành và kiểm tra cả CPU lẫn hệ điều hành về việc hỗ trợ các tập lệnh khác nhau. Các phiên bản khác nhau của `CriticalFunction` trong ví dụ 13.1 có thể được đặt trong các mô-đun riêng biệt nếu cần, mỗi phiên bản được biên dịch cho một tập lệnh cụ thể.

## 13.6 Điều phối CPU trong trình biên dịch Gnu

Một tính năng có tên là "Gnu indirect function" (hàm gián tiếp Gnu) đã được giới thiệu trong Linux và được các tiện ích Gnu hỗ trợ vào năm 2010. Tính năng này được dành riêng cho việc điều phối CPU và được sử dụng trong thư viện C của Gnu. Nó yêu cầu sự hỗ trợ từ cả trình biên dịch, trình liên kết (linker) và trình tải (loader) (yêu cầu binutils phiên bản 2.20, glibc phiên bản 2.11 nhánh ifunc).

Tính năng này sử dụng một bảng liên kết thủ tục (PLT) thông thường theo cách sau: Có hai hoặc nhiều phiên bản của cùng một hàm, mỗi phiên bản được tối ưu hóa cho một CPU cụ thể hoặc các điều kiện phần cứng khác. Một hàm điều phối (dispatcher function) sẽ quyết định sử dụng hàm nào và trả về một con trỏ trỏ đến hàm mong muốn. Mục nhập PLT ban đầu trỏ đến hàm điều phối. Khi chương trình được tải, trình tải (loader) gọi hàm điều phối và thay thế mục nhập PLT bằng con trỏ mà nó nhận được từ hàm điều phối. Điều này sẽ làm cho bất kỳ lời gọi nào tới hàm đều đi đến phiên bản mong muốn. Lưu ý rằng hàm điều phối thường được gọi trước khi chương trình bắt đầu chạy và trước khi bất kỳ hàm khởi tạo (constructors) nào được gọi. Do đó, hàm điều phối không thể dựa vào bất kỳ thứ gì khác đã được khởi tạo. Hàm điều phối rất có thể sẽ được gọi, ngay cả khi hàm được điều phối không bao giờ được gọi đến.

Rất tiếc, cú pháp được mô tả trong tài liệu hướng dẫn của Gnu hiện tại không hoạt động (gcc v. 4.5.2, tháng 7 năm 2011). Thay vào đó, bạn có thể sử dụng cách khắc phục tạm thời sau:

```cpp
// Ví dụ 13.2. Điều phối CPU trong trình biên dịch Gnu
// Tương tự ví dụ 13.1, Yêu cầu binutils phiên bản 2.20 trở lên

// File tiêu đề cho InstructionSet()
#include "asmlib.h"

// Phiên bản thấp nhất
int CriticalFunction_386(int parm1, int parm2) {...}

// Phiên bản SSE2
int CriticalFunction_SSE2(int parm1, int parm2) {...}

// Phiên bản AVX
int CriticalFunction_AVX(int parm1, int parm2) {...}

// Nguyên mẫu cho điểm vào chung (common entry point)
extern "C" int CriticalFunction ();
__asm__ (".type CriticalFunction, @gnu_indirect_function");

// Tạo hàm điều phối
typeof(CriticalFunction) * CriticalFunctionDispatch(void)
   __asm__ ("CriticalFunction");
typeof(CriticalFunction) * CriticalFunctionDispatch(void)
{
   // Trả về một con trỏ đến phiên bản hàm mong muốn

   // Lấy tập lệnh được hỗ trợ, sử dụng thư viện asmlib
   int level = InstructionSet();

   // Đặt con trỏ đến phiên bản phù hợp (Có thể sử dụng một bảng
   // các con trỏ hàm nếu có nhiều nhánh):
   if (level >= 11)
   {  // AVX được hỗ trợ
      return &CriticalFunction_AVX;
   }
   if (level >= 4)
   {  // SSE2 được hỗ trợ
      return &CriticalFunction_SSE2;
   }
   // Phiên bản mặc định
   return &CriticalFunction_386;
}

int main()
{
   int a, b, c;
   ...

   // Gọi hàm tới hạn
   a = CriticalFunction(b, c);

   ...
   return 0;
}
```

Tính năng hàm gián tiếp được sử dụng trong thư viện hàm Gnu C cho một số hàm đặc biệt tới hạn.

## 13.7 Điều phối CPU trong trình biên dịch Intel

Trình biên dịch Intel có tính năng tạo nhiều phiên bản của một hàm cho các CPU Intel khác nhau. Nó sử dụng phương pháp điều phối ở mỗi lần gọi. Khi hàm được gọi, một sự điều phối sẽ được thực hiện để dẫn đến phiên bản mong muốn của hàm. Việc điều phối tự động có thể được thực hiện cho tất cả các hàm phù hợp trong một mô-đun bằng cách biên dịch mô-đun với, ví dụ như tùy chọn `/QaxAVX` hoặc `-axAVX`. Điều này sẽ tạo ra nhiều phiên bản cho cả các hàm không thuộc phần tới hạn. Bạn có thể thực hiện điều phối chỉ đối với các hàm có tốc độ tới hạn (speed-critical functions) bằng cách sử dụng lệnh chỉ thị `__declspec(cpu_dispatch(...))`. Hãy xem tài liệu Hướng dẫn Trình biên dịch Intel C++ (Intel C++ Compiler Documentation) để biết chi tiết. Cần lưu ý rằng cơ chế điều phối CPU trong trình biên dịch Intel chỉ hoạt động đối với các CPU của Intel, chứ không hoạt động đối với các thương hiệu CPU khác như AMD và VIA. Phần tiếp theo sẽ trình bày một cách để lách qua giới hạn này và các lỗ hổng khác trong cơ chế nhận diện CPU.

Cơ chế điều phối CPU trong trình biên dịch Intel kém hiệu quả hơn so với cơ chế của trình biên dịch Gnu bởi vì nó thực hiện điều phối trong mỗi lần gọi hàm tới hạn. Trong một số trường hợp, cơ chế của Intel thực thi một loạt các rẽ nhánh mỗi khi hàm được gọi, trong khi cơ chế của Gnu lưu trữ một con trỏ đến phiên bản mong muốn trong bảng liên kết thủ tục (procedure linkage table). Nếu một hàm được điều phối (dispatched function) gọi một hàm được điều phối khác thì nhánh điều phối của hàm thứ hai vẫn được thực thi mặc dù loại CPU đã được biết ở vị trí này. Điều này có thể tránh được bằng cách nội tuyến (inlining) hàm thứ hai, nhưng có lẽ tốt hơn là nên thực hiện việc điều phối CPU một cách tường minh như trong ví dụ 13.1.

Các trình biên dịch và thư viện hàm của Intel có các tính năng điều phối CPU tự động. Nhiều hàm thư viện của Intel có một số phiên bản cho các bộ xử lý và tập lệnh khác nhau. Tương tự, trình biên dịch có thể tự tự động tạo nhiều phiên bản mã do người dùng viết với tính năng điều phối CPU tự động.

Thật không may, cơ chế nhận diện CPU trong trình biên dịch Intel có một số thiếu sót:

*   Phiên bản tốt nhất có thể của mã chỉ được chọn khi chạy trên bộ xử lý Intel. Bộ điều phối CPU kiểm tra xem bộ xử lý có phải là của Intel hay không trước khi kiểm tra xem nó hỗ trợ tập lệnh nào. Một phiên bản kém hơn của mã sẽ được chọn nếu bộ xử lý không phải của Intel, ngay cả khi bộ xử lý đó tương thích với phiên bản mã tốt hơn. Điều này có thể dẫn đến sự suy giảm hiệu suất đáng kể trên các bộ xử lý AMD và VIA.
*   Điều phối CPU tường minh chỉ hoạt động với bộ xử lý Intel. Bộ xử lý không phải của Intel làm cho bộ điều phối báo lỗi một cách đơn giản bằng cách thực hiện một thao tác bất hợp pháp (illegal operation) làm chương trình gặp sự cố (crash).
*   Bộ điều phối CPU không kiểm tra xem các thanh ghi XMM có được hệ điều hành hỗ trợ hay không. Nó sẽ gây ra lỗi (crash) trên các hệ điều hành cũ không hỗ trợ SSE.

Một số thư viện hàm được phát hành bởi Intel có cơ chế điều phối CPU tương tự, và một số trong số này cũng xử lý CPU không phải của Intel một cách không tối ưu.

Việc bộ điều phối CPU của Intel đối xử với các CPU không phải của Intel theo cách không tối ưu đã trở thành một vấn đề pháp lý nghiêm trọng. Xem blog của tôi để biết thông tin chi tiết.

Hành vi của trình biên dịch Intel đẩy lập trình viên vào một tình thế khó xử. Bạn có thể thích sử dụng trình biên dịch Intel vì nó có nhiều tính năng tối ưu hóa nâng cao, và bạn có thể muốn sử dụng các thư viện hàm Intel được tối ưu hóa rất tốt, nhưng ai lại muốn dán nhãn lên một chương trình nói rằng nó không hoạt động tốt trên các máy không phải của Intel?

Các giải pháp khả thi cho vấn đề này như sau:

*   Biên dịch cho một tập lệnh cụ thể, ví dụ: `/arch:SSE2`. Trình biên dịch sẽ tạo ra mã tối ưu cho tập lệnh này và chỉ chèn phiên bản SSE2 của hầu hết các hàm thư viện mà không có sự điều phối CPU. Kiểm tra xem chương trình có chạy thỏa đáng trên CPU không phải của Intel hay không. Nếu không, thì có thể cần phải thay thế hàm nhận diện CPU như mô tả bên dưới. Chương trình sẽ không tương thích với các vi xử lý cũ không có tập lệnh đã chọn.
*   Tạo hai hoặc nhiều phiên bản của phần mã quan trọng nhất và biên dịch chúng riêng biệt với tập lệnh thích hợp được chỉ định. Chèn một cơ chế điều phối CPU tường minh vào mã để gọi phiên bản phù hợp với vi xử lý mà nó đang chạy.
*   Thay thế hoặc bỏ qua hàm phát hiện CPU của trình biên dịch Intel. Phương pháp này được mô tả bên dưới.
*   Thực hiện các cuộc gọi trực tiếp đến các phiên bản dành riêng cho CPU của các hàm thư viện. Các hàm dành riêng cho CPU có các hậu tố chẳng hạn như e.g. `.R.` cho AVX. Các hậu tố này được liệt kê trong bảng 19 trong tài liệu 5: các quy ước gọi (calling conventions). Dấu chấm trong tên hàm không được phép trong C++ nên bạn cần phải sử dụng mã hợp ngữ hoặc sử dụng `objconv` hay một tiện ích tương tự để sửa đổi tên trong file đối tượng (object file).
*   Sử dụng một thư viện hàm khác hoạt động tốt trên mọi nhãn hiệu CPU.

Hiệu năng trên các bộ xử lý không phải của Intel có thể được cải thiện bằng cách sử dụng một hoặc nhiều phương pháp trên nếu phần tiêu tốn nhiều thời gian nhất của chương trình chứa tính năng điều phối CPU tự động hoặc các hàm sử dụng nhiều bộ nhớ (như memcpy, memmove, memset) hoặc các hàm toán học (như pow, log, exp, sin, v.v.).

### Ghi đè hàm phát hiện CPU của Intel (Overriding the Intel CPU detection function)

Trong một số trường hợp, có hai phiên bản của hàm phát hiện CPU, một phiên bản phân biệt giữa các thương hiệu CPU, và một phiên bản thì không.

Hàm thư viện không có tài liệu (undocumented) của Intel là `__intel_cpu_features_init()` thiết lập biến `__intel_cpu_feature_indicator` trong đó mỗi bit cho biết một tính năng cụ thể trên CPU Intel. Một hàm khác là `__intel_cpu_features_init_x()` thực hiện điều tương tự mà không phân biệt giữa các thương hiệu CPU và tương tự thiết lập biến `__intel_cpu_feature_indicator_x`. Bạn có thể bỏ qua việc kiểm tra thương hiệu CPU đơn giản bằng cách thiết lập các biến này thành 0 và sau đó gọi hàm `__intel_cpu_features_init_x()`.

Trong các trường hợp khác, có thể thay thế hàm nhận diện CPU trong các thư viện hàm Intel và trong mã do trình biên dịch tạo ra bằng cách tạo một hàm khác có cùng tên. Trong hệ điều hành Windows, điều này yêu cầu liên kết tĩnh (static linking) (ví dụ: tùy chọn `/MT`). Trong hệ thống Linux và Mac, điều này có thể hoạt động với cả liên kết tĩnh và liên kết động.

Tệp tin `http://www.agner.org/optimize/asmlib.zip` chứa các ví dụ mã hoàn chỉnh cho những phương pháp này.
