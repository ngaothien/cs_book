| Phương pháp tối ưu hóa | Microsoft | Borland | Intel | Gnu | PathScale | PGI | Digital Mars | Watcom | Codeplay |
|---|---|---|---|---|---|---|---|---|---|
| Inlining hàm | x | - | x | x | x | x | - | - | x |
| Gộp hằng số | x | x | x | x | x | x | x | x | x |
| Truyền hằng số | x | - | x | x | x | x | - | - | x |
| Loại bỏ con trỏ | x | x | x | x | x | x | x | x | x |
| Loại bỏ biểu thức con chung, số nguyên | x | (x) | x | x | x | x | x | x | x |
| Loại bỏ biểu thức con chung, số thực | x | - | x | x | x | x | - | x | x |
| Biến thanh ghi, số nguyên | x | x | x | x | x | x | x | x | x |
| Biến thanh ghi, số thực | x | - | x | x | x | x | - | x | x |
| Phân tích khoảng hoạt động | x | x | x | x | x | x | x | x | x |
| Gộp các nhánh giống nhau | x | - | - | x | - | - | - | x | - |
| Loại bỏ lệnh nhảy | x | x | x | x | x | x | - | x | x |
| Loại bỏ các nhánh | x | - | x | x | x | x | - | - | - |
| Loại bỏ nhánh luôn đúng/sai | x | - | x | x | x | x | x | x | x |
| Khai triển vòng lặp | x | - | x | x | x | x | - | - | x |
| Chuyển động đoạn mã bất biến trong vòng lặp | x | - | x | x | x | x | x | x | x |
| Biến quy nạp cho các phần tử mảng | x | x | x | x | x | x | x | x | x |
| Biến quy nạp cho các biểu thức số nguyên khác | x | - | x | x | x | - | x | x | x |
| Biến quy nạp cho biểu thức số thực | - | - | - | - | - | - | - | - | - |
| Tự động vector hóa | - | - | x | x | x | x | - | - | x |
| Loại bỏ hàm ảo (Devirtualization) | - | - | - | x | - | - | - | - | - |
| Tối ưu hóa có hướng dẫn (Profile-guided optimization) | x | - | x | x | x | x | - | - | - |
| Tối ưu hóa toàn chương trình | x | - | x | x | x | - | - | - | - |
| **Rút gọn đại số số nguyên:**<br>a+b = b+a | x | (x) | x | x | x | x | - | x | x |
| a*b = b*a | x | (x) | x | x | x | x | - | x | x |
| (a+b)+c = a+(b+c) | x | - | x | x | - | - | x | x | - |
| a+b+c = c+b+a | x | - | - | x | - | - | - | - | - |
| a+b+c+d = (a+b)+(c+d) | - | - | x | x | - | - | - | - | - |
| a*b+a*c = a*(b+c) | x | - | x | x | x | - | - | - | x |
| a*x*x*x + b*x*x + c*x + d = ((a*x+b)*x+c)*x+d | x | - | x | x | x | - | - | - | x |
| x*x*x*x*x*x*x*x = ((x^2)^2)^2 | - | - | x | - | - | - | - | - | - |
| a+a+a+a = a*4 | x | - | x | x | - | - | - | - | x |
| -(-a) = a | x | - | x | x | x | x | x | x | - |
| a-(-b) = a+b | x | - | x | x | x | x | - | x | - |
| a-a = 0 | x | - | x | x | x | x | x | x | x |
| a+0 = a | x | x | x | x | x | x | x | x | x |
| a*0 = 0 | x | x | x | x | x | x | x | - | x |
| a*1 = a | x | x | x | x | x | x | x | x | x |
| (-a)*(-b) = a*b | x | - | x | x | x | - | - | - | - |
| a/a = 1 | - | - | - | - | x | - | - | - | x |
| a/1 = a | x | x | x | x | x | x | x | x | x |
| 0/a = 0 | - | - | - | x | - | - | - | x | x |
| (-a == -b) = (a == b) | - | - | - | x | x | - | - | - | - |
| (a+c == b+c) = (a == b) | - | - | - | - | x | - | - | - | - |
| !(a < b) = (a >= b) | x | x | x | x | x | x | x | x | x |
| (a<b && b<c && a<c) = (a<b && b<c) | - | - | - | - | - | - | - | - | - |
| Nhân với hằng số = dịch bit và cộng | x | x | x | x | - | x | x | x | - |
| Chia cho hằng số = nhân và dịch bit | x | - | x | x | x | (-) | x | - | - |
| **Rút gọn đại số số thực:**<br>a+b = b+a | x | - | x | x | x | x | - | - | x |
| a*b = b*a | x | - | x | x | x | x | - | - | x |
| a+b+c = a+(b+c) | x | - | x | x | - | - | - | - | - |
| (a+b)+c = a+(b+c) | - | - | x | x | - | - | - | - | - |
| a*b*c = a*(b*c) | x | - | - | x | - | - | - | - | - |
| a+b+c+d = (a+b)+(c+d) | - | - | - | x | - | - | - | - | - |
| a*b+a*c = a*(b+c) | x | - | - | - | x | - | - | - | x |
| a*x*x*x + b*x*x + c*x + d = ((a*x+b)*x+c)*x+d | x | - | x | x | x | - | - | - | - |
| x*x*x*x*x*x*x*x = ((x^2)^2)^2 | - | - | - | x | - | - | - | - | - |
| a+a+a+a = a*4 | x | - | - | x | x | - | - | - | - |
| -(-a) = a | - | - | x | x | x | x | x | x | - |
| a-(-b) = a+b | - | - | - | x | x | x | - | x | - |
| a+0 = a | x | - | x | x | x | x | x | x | - |
| a*0 = 0 | - | - | x | x | x | x | - | x | x |
| a*1 = a | x | - | x | x | x | x | x | - | x |
| (-a)*(-b) = a*b | - | - | - | x | x | x | - | - | - |
| a/a = 1 | - | - | - | - | - | - | - | - | x |
| a/1 = a | x | - | x | x | x | - | x | - | - |
| 0/a = 0 | - | - | - | x | x | - | - | x | x |
| (-a == -b) = (a == b) | - | - | - | x | x | - | - | - | - |
| (-a > -b) = (a < b) | - | - | - | x | x | - | - | - | x |
| Chia cho hằng số = nhân với nghịch đảo | x | x | - | x | x | - | - | x | - |
| **Rút gọn đại số Boolean:**<br>!(!a) = a | x | - | x | x | x | x | x | x | x |
| (a&&b) \|\| (a&&c) = a&&(b\|\|c) | x | - | x | x | x | - | - | - | - |
| !a && !b = !(a \|\| b) | x | x | x | x | x | x | x | x | x |
| a && !a = false, a \|\| !a = true | x | - | x | x | x | x | - | - | - |
| a && true = a, a \|\| false = a | x | x | x | x | x | x | x | x | - |
| a && false = false, a \|\| true = true | x | - | x | x | x | x | x | x | - |
| a && a = a | x | - | x | x | x | x | - | - | - |
| (a&&b) \|\| (a&&!b) = a | x | - | - | x | x | - | - | - | - |
| (a&&b) \|\| (!a&&c) = a ? b : c | x | - | x | x | - | - | - | - | - |
| (a&&b) \|\| (!a&&c) \|\| (b&&c) = a ? b : c | x | - | - | x | - | - | - | - | - |
| (a&&b) \|\| (a&&b&&c) = a&&b | x | - | - | x | x | - | - | - | - |
| (a&&b) \|\| (a&&c) \|\| (a&&b&&c) = a&&(b\|\|c) | x | - | - | x | x | - | - | - | - |
| (a&&!b) \|\| (!a&&b) = a XOR b | - | - | - | - | - | - | - | - | - |
| **Rút gọn đại số vector bit:**<br>~(~a) = a | x | - | x | x | x | x | x | - | - |
| (a&b)\|(a&c) = a&(b\|c) | x | - | x | x | x | x | - | - | x |
| (a\|b)&(a\|c) = a\|(b&c) | x | - | x | x | x | x | - | - | x |
| ~a & ~b = ~(a \| b) | - | - | x | x | x | x | - | - | - |
| a & a = a | x | - | - | x | x | x | - | - | x |
| a & ~a = 0 | - | - | x | x | x | x | - | - | - |
| a & -1 = a,  a \| 0 = a | x | - | x | x | x | x | x | x | x |
| a & 0 = 0,  a \| -1 = -1 | x | - | x | x | x | x | x | x | x |
| (a&b) \| (~a&c) \| (b&c) = (a&b) \| (~a&c) | - | - | - | - | - | - | - | - | - |
| a&b&c&d = (a&b)&(c&d) | - | - | - | x | - | - | - | - | - |
| a ^ 0 = a | x | x | x | x | x | - | x | x | x |
| a ^ -1 = ~a | x | - | x | x | x | - | x | x | - |
| a ^ a = 0 | x | - | x | x | x | x | - | x | x |
| a ^ ~a = -1 | - | - | - | x | x | x | - | - | - |
| (a&~b) \| (~a&b) = a ^ b | - | - | - | - | - | - | - | - | - |
| ~a ^ ~b = a ^ b | - | - | - | x | x | - | - | - | - |
| a<<b<<c = a<<(b+c) | x | - | x | x | x | - | - | x | x |
| **Rút gọn số nguyên XMM (vector):**<br>Loại bỏ biểu thức con chung | x | n.a. | x | x | x | - | n.a. | n.a. | x |
| Gộp hằng số | - | n.a. | - | x | - | - | n.a. | n.a. | - |
| a+b = b+a, a*b = b*a | - | n.a. | - | x | - | - | n.a. | n.a. | x |
| (a+b)+c = a+(b+c) | - | n.a. | - | - | - | - | n.a. | n.a. | - |
| a*b+a*c = a*(b+c) | - | n.a. | - | - | - | - | n.a. | n.a. | - |
| x*x*x*x*x*x*x*x = ((x^2)^2)^2 | - | n.a. | - | - | - | - | n.a. | n.a. | - |
| a+a+a+a = a*4 | - | n.a. | - | - | - | - | n.a. | n.a. | - |
| -(-a) = a | - | n.a. | - | - | - | - | n.a. | n.a. | - |
| a-a = 0 | - | n.a. | x | - | - | - | n.a. | n.a. | - |
| a+0 = a | - | n.a. | - | - | - | - | n.a. | n.a. | - |
| a*0 = 0 | - | n.a. | - | x | - | - | n.a. | n.a. | - |
| a*1 = a | - | n.a. | - | x | - | - | n.a. | n.a. | - |
| (-a)*(-b) = a*b | - | n.a. | - | - | - | - | n.a. | n.a. | - |
| !(a < b) = (a >= b) | - | n.a. | - | - | - | - | n.a. | n.a. | - |
| **Rút gọn số thực XMM (vector):**<br>a+b = b+a,  a*b = b*a | x | n.a. | - | x | - | - | n.a. | n.a. | x |
| a+b+c = a+(b+c) | - | n.a. | - | - | - | - | n.a. | n.a. | - |
| a*b+a*c = a*(b+c) | - | n.a. | - | - | - | - | n.a. | n.a. | - |
| -(-a) = a | - | n.a. | - | - | - | - | n.a. | n.a. | - |
| a-a = 0 | - | n.a. | - | x | - | - | n.a. | n.a. | - |
| a+0 = a | - | n.a. | x | - | - | - | n.a. | n.a. | - |
| a*0 = 0 | - | n.a. | x | - | - | - | n.a. | n.a. | - |
| a*1 = a | - | n.a. | - | x | - | - | n.a. | n.a. | - |
| a/1 = a | - | n.a. | - | x | - | - | n.a. | n.a. | - |
| 0/a = 0 | - | n.a. | x | x | - | - | n.a. | n.a. | - |
| Chia cho hằng số = nhân với nghịch đảo | - | n.a. | - | - | - | - | n.a. | n.a. | - |
| **Rút gọn Boolean XMM (vector):**<br>~(~a) = a | - | n.a. | - | - | - | - | n.a. | n.a. | - |
| (a&b)\|(a&c) = a&(b\|c) | - | n.a. | - | - | - | - | n.a. | n.a. | - |
| a & a = a,  a \| a = a | - | n.a. | x | x | - | - | n.a. | n.a. | - |
| a & ~a = 0 | - | n.a. | - | x | - | - | n.a. | n.a. | - |
| a & -1 = a,  a \| 0 = a | - | n.a. | - | - | - | - | n.a. | n.a. | - |
| a & 0 = 0 | - | n.a. | - | x | - | - | n.a. | n.a. | - |
| a \| -1 = -1 | - | n.a. | - | - | - | - | n.a. | n.a. | - |
| a ^ a = 0 | - | n.a. | x | x | - | - | n.a. | n.a. | - |
| andnot(a,a) = 0 | - | n.a. | - | x | - | - | n.a. | n.a. | - |
| a<<b<<c = a<<(b+c) | - | n.a. | - | - | - | - | n.a. | n.a. | - |

Bảng 8.1. So sánh các phương pháp tối ưu hóa trên các trình biên dịch C++ khác nhau
Các bài kiểm tra đã được thực hiện với tất cả các tùy chọn tối ưu hóa có liên quan được bật, bao gồm cả việc giảm độ chính xác của dấu phẩy động. Các phiên bản trình biên dịch sau đây đã được kiểm tra:
* Trình biên dịch C++ của Microsoft v. 14.00 cho 80x86 / x64 (Visual Studio 2005).
* Borland C++ 5.82 (Embarcadero/CodeGear/Borland C++ Builder 5, 2009).
* Trình biên dịch C++ của Intel v. 11.1 cho IA-32/Intel64, 2009.
* Gnu C++ v. 4.1.0, 2006 (Red Hat).
* PathScale C++ v. 3.1, 2007.
* PGI C++ v. 7.1-4, 2008.
* Trình biên dịch Digital Mars v. 8.42n, 2004.
* Open Watcom C/C++ v. 1.4, 2005.
* Codeplay VectorC v. 2.1.7, 2004.
Không có sự khác biệt nào được quan sát thấy giữa các khả năng tối ưu hóa cho mã 32-bit và 64-bit đối với các trình biên dịch Microsoft, Intel, Gnu và PathScale.

## 8.3 Các trở ngại đối với việc tối ưu hóa của trình biên dịch
Có một số yếu tố có thể ngăn cản trình biên dịch thực hiện các tối ưu hóa mà chúng ta mong muốn. Điều quan trọng đối với lập trình viên là phải nhận thức được những trở ngại này và biết cách tránh chúng. Một số trở ngại quan trọng đối với việc tối ưu hóa được thảo luận dưới đây.

**Không thể tối ưu hóa xuyên suốt các mô-đun (Cannot optimize across modules)**
Trình biên dịch không có thông tin về các hàm trong các mô-đun khác ngoài mô-đun mà nó đang biên dịch. Điều này ngăn cản nó thực hiện các tối ưu hóa xuyên suốt các lời gọi hàm. Ví dụ:
```cpp
// Example 8.20
module1.cpp
int Func1(int x) {
   return x*x + 1;
}

module2.cpp
int Func2() {
   int a = Func1(2);
   ...
}
```
Nếu `Func1` và `Func2` nằm trong cùng một mô-đun thì trình biên dịch sẽ có khả năng thực hiện inlining hàm và truyền hằng số (constant propagation) và rút gọn `a` thành hằng số 5. Nhưng trình biên dịch không có thông tin cần thiết về `Func1` khi biên dịch `module2.cpp`.

Cách đơn giản nhất để giải quyết vấn đề này là kết hợp nhiều mô-đun `.cpp` thành một thông qua các chỉ thị `#include`. Điều này chắc chắn sẽ hoạt động trên tất cả các trình biên dịch. Một số trình biên dịch có một tính năng gọi là tối ưu hóa toàn bộ chương trình (whole program optimization), tính năng này sẽ cho phép tối ưu hóa xuyên suốt các mô-đun (Xem trang 82).

**Bí danh con trỏ (Pointer aliasing)**
Khi truy cập vào một biến thông qua một con trỏ hoặc tham chiếu, trình biên dịch có thể không hoàn toàn loại trừ khả năng biến được trỏ tới giống hệt với một số biến khác trong mã. Ví dụ:
```cpp
// Example 8.21
void Func1 (int a[], int * p) {
   int i;
   for (i = 0; i < 100; i++) {
      a[i] = *p + 2;
   }
}

void Func2() {
   int list[100];
   Func1(list, &list[8]);
}
```
Ở đây, cần phải tải lại `*p` và tính toán lại `*p+2` một trăm lần vì giá trị được trỏ tới bởi `p` giống hệt với một trong các phần tử trong `a[]` sẽ thay đổi trong suốt vòng lặp. Không được phép giả định rằng `*p+2` là một đoạn mã bất biến trong vòng lặp có thể được chuyển ra ngoài vòng lặp. Ví dụ 8.21 thực sự là một ví dụ rất gượng ép, nhưng điểm mấu chốt là trình biên dịch không thể loại trừ khả năng lý thuyết rằng những ví dụ gượng ép như vậy tồn tại. Do đó, trình biên dịch bị ngăn không cho giả định rằng `*p+2` là một biểu thức bất biến trong vòng lặp mà nó có thể di chuyển ra ngoài vòng lặp.

Hầu hết các trình biên dịch đều có một tùy chọn để giả định không có bí danh con trỏ (`/Oa`). Cách dễ nhất để vượt qua trở ngại của khả năng bí danh con trỏ là bật tùy chọn này. Việc này yêu cầu bạn phải phân tích cẩn thận tất cả các con trỏ và tham chiếu trong đoạn mã để đảm bảo rằng không có biến hay đối tượng nào được truy cập bằng nhiều cách khác nhau trong cùng một phần của mã. Ngoài ra cũng có thể báo cho trình biên dịch biết rằng một con trỏ cụ thể không được gán bí danh với bất cứ thứ gì bằng cách sử dụng từ khóa `__restrict` hoặc `__restrict__`, nếu được trình biên dịch hỗ trợ.

Chúng ta không bao giờ có thể chắc chắn rằng trình biên dịch nhận ra gợi ý về việc không có bí danh con trỏ. Cách duy nhất để chắc chắn rằng mã được tối ưu hóa là thực hiện nó một cách rõ ràng. Trong ví dụ 8.21, bạn có thể tính toán `*p+2` và lưu nó vào một biến tạm thời bên ngoài vòng lặp nếu bạn chắc chắn rằng con trỏ không làm bí danh cho bất kỳ phần tử nào trong mảng. Phương pháp này yêu cầu bạn phải có khả năng dự đoán các trở ngại đối với việc tối ưu hóa nằm ở đâu.

**Cấp phát bộ nhớ động (Dynamic memory allocation)**
Bất kỳ mảng hoặc đối tượng nào được cấp phát động (với `new` hoặc `malloc`) nhất thiết phải được truy cập thông qua một con trỏ. Đối với lập trình viên, có thể rõ ràng rằng các con trỏ trỏ đến các đối tượng được cấp phát động khác nhau sẽ không chồng chéo hoặc gán bí danh, nhưng trình biên dịch thường không thể nhận ra điều này. Điều này cũng ngăn cản trình biên dịch căn chỉnh dữ liệu (align) một cách tối ưu, hoặc ngăn nó biết rằng các đối tượng đã được căn chỉnh. Khuyến nghị khai báo các đối tượng và mảng có kích thước cố định bên trong hàm cần tới chúng.

**Các hàm thuần túy (Pure functions)**
Hàm thuần túy là hàm không có tác dụng phụ (side-effects) và giá trị trả về của nó chỉ phụ thuộc vào giá trị của các đối số của nó. Điều này theo sát khái niệm toán học về một "hàm".

Nhiều lời gọi đến một hàm thuần túy với cùng các đối số chắc chắn sẽ tạo ra cùng một kết quả. Trình biên dịch có thể loại bỏ các biểu thức con chung có chứa các lời gọi hàm thuần túy và nó có thể di chuyển đoạn mã bất biến ra khỏi vòng lặp nếu đoạn mã đó chứa lời gọi hàm thuần túy. Thật không may, trình biên dịch không thể biết một hàm là thuần túy nếu hàm đó được định nghĩa trong một mô-đun khác hoặc trong một thư viện hàm.

Do đó, cần phải thực hiện thủ công các tối ưu hóa như loại bỏ biểu thức con chung, truyền hằng số và chuyển động đoạn mã bất biến trong vòng lặp khi nó liên quan đến các lời gọi hàm thuần túy.

Trình biên dịch Gnu và trình biên dịch Intel cho Linux có một thuộc tính có thể được áp dụng cho mẫu thử hàm (function prototype) để nói cho trình biên dịch biết rằng đây là một hàm thuần túy. Ví dụ:
```cpp
// Example 8.22
#ifdef __GNUC__
#define pure_function  __attribute__((const))
#else
#define pure_function
#endif

double Func1(double) pure_function ;

double Func2(double x) {
   return Func1(x) * Func1(x) + 1.;
}
```
Ở đây, trình biên dịch Gnu sẽ chỉ gọi `Func1` một lần, trong khi các trình biên dịch khác sẽ thực hiện gọi hai lần.

Một số trình biên dịch khác (Microsoft, Intel) biết rằng các hàm thư viện tiêu chuẩn như `sqrt`, `pow` và `log` là các hàm thuần túy, nhưng thật không may là không có cách nào để cho các trình biên dịch này biết rằng một hàm do người dùng định nghĩa là hàm thuần túy.

**Hàm ảo và con trỏ hàm (Virtual functions and function pointers)**
Hiếm khi trình biên dịch có thể dự đoán chắc chắn phiên bản nào của một hàm ảo sẽ được gọi, hoặc một con trỏ hàm sẽ trỏ tới đâu. Do đó, nó không thể inline hàm đó hoặc thực hiện tối ưu hóa xuyên qua lời gọi hàm.

**Rút gọn đại số (Algebraic reduction)**
Hầu hết các trình biên dịch đều có thể thực hiện các rút gọn đại số đơn giản như `-(-a) = a`, nhưng chúng không có khả năng thực hiện các phép rút gọn phức tạp hơn. Rút gọn đại số là một quá trình phức tạp và rất khó để cài đặt vào trong trình biên dịch.

Nhiều thao tác rút gọn đại số không được phép vì những lý do liên quan đến tính thuần túy của toán học. Trong nhiều trường hợp, có thể xây dựng những ví dụ mơ hồ nơi thao tác rút gọn sẽ gây ra tràn số hoặc mất độ chính xác, đặc biệt là trong các biểu thức dấu phẩy động (xem trang 73). Trình biên dịch không thể loại trừ khả năng rằng một thao tác rút gọn cụ thể sẽ không hợp lệ trong một tình huống cụ thể, nhưng lập trình viên thì có thể. Do đó, trong nhiều trường hợp, cần phải thực hiện các thao tác rút gọn đại số một cách thủ công.

Các biểu thức nguyên ít nhạy cảm với các vấn đề về tràn số và mất độ chính xác hơn vì những lý do được giải thích trên trang 73. Do đó, trình biên dịch có khả năng thực hiện nhiều rút gọn trên các biểu thức nguyên hơn là trên các biểu thức dấu phẩy động. Hầu hết các rút gọn liên quan đến phép cộng, phép trừ và phép nhân số nguyên đều được cho phép trong tất cả các trường hợp, trong khi nhiều thao tác rút gọn liên quan đến phép chia và các toán tử quan hệ (ví dụ `>`) không được phép vì lý do thuần túy toán học. Ví dụ, các trình biên dịch không thể rút gọn biểu thức nguyên `-a > -b` thành `a < b` vì khả năng cực kỳ khó nhận thấy về việc tràn số.

Bảng 8.1 (trang 78) cho thấy các rút gọn nào mà trình biên dịch có thể thực hiện, ít nhất là trong một số tình huống, và các rút gọn nào mà chúng không thể thực hiện. Tất cả các rút gọn mà các trình biên dịch không thể thực hiện phải được lập trình viên thực hiện theo cách thủ công.

**Biến quy nạp dấu phẩy động (Floating point induction variables)**
Các trình biên dịch không thể tạo ra các biến quy nạp dấu phẩy động vì cùng lý do mà chúng không thể thực hiện các thao tác rút gọn đại số trên các biểu thức dấu phẩy động. Do đó, cần phải làm điều này một cách thủ công. Nguyên tắc này rất hữu ích bất cứ khi nào một hàm số dựa trên biến đếm của vòng lặp có thể được tính toán hiệu quả hơn từ giá trị trước đó của nó thay vì từ chính biến đếm vòng lặp. Bất kỳ biểu thức nào là đa thức bậc `n` của biến đếm vòng lặp đều có thể được tính toán thông qua `n` phép cộng và không cần phép nhân. Ví dụ sau đây cho thấy nguyên tắc đối với đa thức bậc 2:
```cpp
// Example 8.23a. Loop to make table of polynomial
const double A = 1.1, B = 2.2, C = 3.3; // Polynomial coefficients
double Table[100];                      // Table
int x;                                  // Loop counter
for (x = 0; x < 100; x++) {
   Table[x] = A*x*x + B*x + C;          // Calculate polynomial
}
```
Phép tính toán của đa thức này có thể được thực hiện chỉ bằng hai phép cộng thông qua việc sử dụng hai biến quy nạp:
```cpp
// Example 8.23b. Calculate polynomial with induction variables
const double A = 1.1, B = 2.2, C = 3.3; // Polynomial coefficients
double Table[100];                      // Table
int x;                                  // Loop counter
const double A2 = A + A;                // = 2*A
double Y = C;                           // = A*x*x + B*x + C
double Z = A + B;                       // = Delta Y
for (x = 0; x < 100; x++) {
   Table[x] = Y;                        // Store result
   Y += Z;                              // Update induction variable Y
   Z += A2;                             // Update induction variable Z
}
```
Vòng lặp trong ví dụ 8.23b có hai chuỗi phụ thuộc kéo theo vòng lặp (loop-carried dependency chains), đó là hai biến quy nạp `Y` và `Z`. Mỗi chuỗi phụ thuộc có độ trễ bằng với độ trễ của một phép cộng dấu phẩy động. Độ trễ này đủ nhỏ để chứng minh phương pháp này là hợp lý. Một chuỗi phụ thuộc kéo theo vòng lặp dài hơn sẽ làm cho phương pháp biến quy nạp không thuận lợi, trừ khi giá trị được tính từ một giá trị nằm lùi về trước hai hoặc nhiều vòng lặp hơn.

Phương pháp biến quy nạp cũng có thể được vector hóa nếu bạn xem xét tới việc mỗi giá trị được tính toán từ một giá trị nằm cách đó `r` vị trí trong chuỗi, trong đó `r` là số phần tử trong một vector hoặc là hệ số khai triển vòng lặp (loop unroll factor). Cần một chút kiến thức toán học để tìm ra công thức phù hợp trong từng trường hợp.

**Các hàm được inline có một bản sao không được inline (Inlined functions have a non-inlined copy)**
Inlining hàm có một điểm phức tạp là hàm đó cũng có thể được gọi từ một mô-đun khác. Trình biên dịch phải tạo một bản sao không được inline (non-inlined copy) của hàm được inline để dự phòng khả năng hàm đó cũng được gọi từ mô-đun khác. Bản sao không được inline này là đoạn mã chết (dead code) nếu không có mô-đun nào khác gọi hàm đó. Sự phân mảnh này của đoạn mã làm cho việc sử dụng bộ nhớ đệm (caching) trở nên kém hiệu quả hơn.

Có nhiều cách để giải quyết vấn đề này. Nếu một hàm không được tham chiếu tới từ bất kỳ mô-đun nào khác, hãy thêm từ khóa `static` vào định nghĩa hàm. Việc này nói cho trình biên dịch biết rằng hàm không thể được gọi từ bất kỳ mô-đun nào khác. Khai báo `static` giúp trình biên dịch dễ dàng đánh giá hơn liệu việc inline hàm có tối ưu hay không, và nó ngăn cản trình biên dịch tạo ra một bản sao không được sử dụng của một hàm được inline. Từ khóa `static` cũng giúp cho nhiều sự tối ưu hóa khác có khả năng thực hiện vì trình biên dịch không phải tuân theo bất kỳ quy ước gọi hàm cụ thể nào đối với các hàm không thể truy cập từ các mô-đun khác. Bạn có thể thêm từ khóa `static` cho tất cả các hàm không phải là hàm thành viên (non-member functions) chỉ mang tính cục bộ.

Thật không may, phương pháp này không hoạt động đối với các hàm thành viên của lớp vì từ khóa `static` có ý nghĩa khác đối với các hàm thành viên. Bạn có thể buộc một hàm thành viên phải được inline bằng cách khai báo phần thân hàm bên trong định nghĩa của lớp. Việc này sẽ ngăn trình biên dịch tạo bản sao không được inline của hàm, nhưng nó có nhược điểm là hàm sẽ luôn được inline ngay cả khi việc đó không hề tối ưu (tức là nếu hàm thành viên đó lớn và được gọi từ nhiều nơi khác nhau).

Một số trình biên dịch có một tùy chọn (Windows: `/Gy`, Linux: `-ffunction-sections`) cho phép bộ liên kết (linker) loại bỏ các hàm không được tham chiếu. Rất khuyến khích bật tùy chọn này.

## 8.4 Các trở ngại đối với việc tối ưu hóa của CPU
Các CPU hiện đại có thể thực hiện nhiều sự tối ưu hóa bằng cách thực thi các câu lệnh không theo thứ tự (out of order). Những chuỗi phụ thuộc dài trong đoạn mã sẽ ngăn cản CPU thực hiện việc thực thi không theo thứ tự, như được giải thích ở trang 22. Tránh các chuỗi phụ thuộc dài, đặc biệt là các chuỗi phụ thuộc kéo theo vòng lặp có độ trễ dài.

## 8.5 Các tùy chọn tối ưu hóa của trình biên dịch
Tất cả các trình biên dịch C++ đều có nhiều tùy chọn tối ưu hóa khác nhau mà bạn có thể bật và tắt. Điều quan trọng là phải nghiên cứu các tùy chọn có sẵn đối với trình biên dịch mà bạn đang sử dụng và bật tất cả các tùy chọn liên quan.

Nhiều tùy chọn tối ưu hóa không tương thích với việc gỡ lỗi (debugging). Một trình gỡ lỗi có thể thực thi đoạn mã từng dòng một và hiển thị giá trị của tất cả các biến. Rõ ràng, điều này là không thể khi các phần của đoạn mã đã bị sắp xếp lại, inlined, hoặc tối ưu hóa cho biến mất. Việc tạo ra hai phiên bản của tệp thực thi chương trình là phổ biến: một phiên bản gỡ lỗi (debug version) được hỗ trợ gỡ lỗi đầy đủ được dùng trong quá trình phát triển chương trình, và một phiên bản phát hành (release version) với tất cả các tùy chọn tối ưu hóa phù hợp đã được bật. Hầu hết các IDE (Môi trường phát triển tích hợp) đều có công cụ để tạo phiên bản gỡ lỗi và phiên bản phát hành cho các tệp đối tượng (object files) và tệp thực thi. Hãy đảm bảo rằng bạn phân biệt được hai phiên bản này và tắt các hỗ trợ gỡ lỗi cũng như tạo hồ sơ (profiling) trong phiên bản tệp thực thi đã được tối ưu hóa.

Hầu hết các trình biên dịch cung cấp lựa chọn giữa việc tối ưu hóa cho kích thước (size) và tối ưu hóa cho tốc độ (speed). Việc tối ưu hóa cho kích thước là phù hợp khi đoạn mã dù sao cũng đã chạy nhanh và bạn muốn tệp thực thi càng nhỏ càng tốt, hoặc khi code caching là vấn đề quan trọng. Việc tối ưu hóa cho tốc độ là phù hợp khi khả năng truy cập CPU và bộ nhớ là những yếu tố tiêu tốn nhiều thời gian. Hãy chọn tùy chọn tối ưu hóa mạnh mẽ nhất có sẵn.

Một số trình biên dịch cung cấp tối ưu hóa có hướng dẫn (profile-guided optimization). Tính năng này hoạt động theo cách sau: Đầu tiên, bạn biên dịch chương trình với khả năng hỗ trợ profiling. Sau đó, bạn thực hiện một lần chạy thử với một trình phân tích dữ liệu (profiler), qua đó xác định được luồng chương trình và số lần mỗi hàm và nhánh được thực thi. Trình biên dịch sau đó có thể sử dụng thông tin này để tối ưu hóa đoạn mã và đưa các hàm khác nhau theo một thứ tự tối ưu.

Một số trình biên dịch có hỗ trợ tối ưu hóa toàn bộ chương trình (whole program optimization). Tính năng này hoạt động thông qua việc biên dịch làm hai bước. Đầu tiên, tất cả các tệp mã nguồn sẽ được biên dịch sang một định dạng tệp trung gian thay vì định dạng tệp đối tượng thông thường. Các tệp trung gian sau đó được liên kết với nhau trong bước thứ hai, đây là nơi việc biên dịch được hoàn tất. Quá trình cấp phát thanh ghi và inlining hàm được thực hiện tại bước thứ hai. Định dạng tệp trung gian không được chuẩn hóa. Nó thậm chí còn không tương thích với các phiên bản khác nhau của cùng một trình biên dịch. Vì vậy, không thể phân phối các thư viện hàm theo định dạng này.

Các trình biên dịch khác cung cấp khả năng biên dịch nhiều tệp `.cpp` vào một tệp đối tượng duy nhất. Điều này cho phép trình biên dịch thực hiện các tối ưu hóa xuyên suốt các mô-đun khi tối ưu hóa liên tục các thủ tục (interprocedural optimization) được bật. Một cách nguyên thủy hơn, nhưng hiệu quả hơn, để thực hiện tối ưu hóa toàn bộ chương trình là ghép tất cả các tệp mã nguồn thành một bằng các chỉ thị `#include` và khai báo tất cả các hàm là `static` hoặc `inline`. Điều này sẽ cho phép trình biên dịch thực hiện các tối ưu hóa interprocedural đối với toàn bộ chương trình.

Xuyên suốt lịch sử phát triển của CPU, mỗi thế hệ CPU mới lại tăng cường thêm tập lệnh (instruction set) có sẵn. Các tập lệnh mới hơn cho phép trình biên dịch tạo ra đoạn mã hiệu quả hơn, nhưng điều này khiến đoạn mã không tương thích với các CPU cũ. Tập lệnh Pentium Pro giúp các phép so sánh dấu phẩy động hoạt động hiệu quả hơn. Tập lệnh này được hỗ trợ bởi tất cả các CPU hiện đại. Tập lệnh SSE2 đặc biệt thú vị vì nó làm cho mã dấu phẩy động hoạt động hiệu quả hơn trong một số trường hợp và nó giúp khả năng sử dụng các lệnh vector (xem trang 107) có thể xảy ra. Tuy nhiên, việc sử dụng tập lệnh SSE2 không phải lúc nào cũng tối ưu. Trong một số trường hợp, tập lệnh SSE2 làm cho mã dấu phẩy động chậm hơn, đặc biệt là khi đoạn mã trộn lẫn giữa `float` và `double` (xem trang 143). Tập lệnh SSE2 được hỗ trợ bởi hầu hết các CPU và hệ điều hành có sẵn hiện nay.

Bạn có thể chọn một tập lệnh mới hơn khi không cần phải duy trì sự tương thích với các CPU cũ. Tốt hơn nữa, bạn có thể tạo nhiều phiên bản của phần mã quan trọng nhất để hỗ trợ các CPU khác nhau. Phương pháp này được giải thích trên trang 125.

Mã sẽ trở nên hiệu quả hơn khi không có xử lý ngoại lệ. Khuyến khích tắt sự hỗ trợ xử lý ngoại lệ, trừ khi đoạn mã dựa vào các thao tác xử lý ngoại lệ có cấu trúc (structured exception handling) và bạn muốn đoạn mã có thể khôi phục lại từ các ngoại lệ. Xem trang 62.

Nên tắt tính năng nhận dạng kiểu thời gian chạy (runtime type identification - RTTI). Xem trang 55.

Bạn nên kích hoạt các phép tính dấu phẩy động nhanh (fast floating point calculations) hoặc tắt yêu cầu tính toán dấu phẩy động nghiêm ngặt, trừ khi yêu cầu sự nghiêm ngặt này là bắt buộc. Xem thảo luận tại trang 74 và 73.

Bật tùy chọn "liên kết cấp độ hàm" (function level linking) nếu có. Xem trang 82 để được giải thích về tùy chọn này.

Sử dụng tùy chọn "giả định không có bí danh con trỏ" (assume no pointer aliasing) nếu bạn chắc chắn rằng đoạn mã không có bí danh con trỏ. Xem giải thích tại trang 79. (Trình biên dịch của Microsoft chỉ hỗ trợ tùy chọn này trong các phiên bản Professional và Enterprise).

Không bật sửa lỗi "Lỗi FDIV" (FDIV bug). Lỗi FDIV là một lỗi nhỏ trong các CPU Pentium cũ nhất có thể gây ra hiện tượng giảm nhẹ độ chính xác trong một vài trường hợp hiếm gặp đối với phép chia dấu phẩy động. Việc kích hoạt tính năng sửa lỗi FDIV làm cho phép chia dấu phẩy động chậm hơn.

Nhiều trình biên dịch có tùy chọn "khung ngăn xếp tiêu chuẩn" (standard stack frame) hoặc "con trỏ khung" (frame pointer). Khung ngăn xếp tiêu chuẩn được sử dụng để gỡ lỗi và xử lý ngoại lệ. Việc bỏ qua khung ngăn xếp tiêu chuẩn làm cho việc gọi hàm nhanh hơn và giúp cung cấp thêm một thanh ghi cho các mục đích khác. Điều này là có lợi vì thanh ghi là một tài nguyên khan hiếm. Không sử dụng khung ngăn xếp trừ khi chương trình của bạn phụ thuộc vào xử lý ngoại lệ.

## 8.6 Chỉ thị tối ưu hóa
Một số trình biên dịch có nhiều từ khóa và chỉ thị được sử dụng để đưa ra các hướng dẫn tối ưu hóa cụ thể tại các vị trí cụ thể trong đoạn mã. Nhiều chỉ thị trong số này là tùy thuộc vào trình biên dịch cụ thể (compiler-specific). Bạn không thể kỳ vọng một chỉ thị dành cho trình biên dịch trên Windows sẽ hoạt động với trình biên dịch trên Linux, hoặc ngược lại. Tuy nhiên, hầu hết các chỉ thị của Microsoft đều hoạt động trên trình biên dịch Intel cho Windows và trình biên dịch Gnu cho Windows, trong khi hầu hết các chỉ thị Gnu đều hoạt động trên các trình biên dịch PathScale và Intel dành cho Linux.

**Các từ khóa hoạt động trên tất cả các trình biên dịch C++**
Từ khóa `register` có thể được thêm vào khai báo biến để nói cho trình biên dịch biết rằng bạn muốn biến này trở thành một biến thanh ghi. Từ khóa `register` chỉ mang tính chất như một lời gợi ý và trình biên dịch có thể không làm theo lời gợi ý đó, nhưng nó có thể hữu ích trong các tình huống mà trình biên dịch không thể dự đoán được các biến nào sẽ được sử dụng nhiều nhất.

Ngược lại với `register` là `volatile`. Từ khóa `volatile` đảm bảo rằng một biến không bao giờ được lưu trữ trong một thanh ghi, ngay cả khi chỉ mang tính tạm thời. Điều này dành cho các biến được chia sẻ giữa nhiều luồng khác nhau, nhưng nó cũng có thể được sử dụng để tắt tất cả các tối ưu hóa đối với một biến cho các mục đích kiểm tra.

Từ khóa `const` báo rằng một biến sẽ không bao giờ thay đổi. Việc này sẽ cho phép trình biên dịch tối ưu hóa nhằm loại bỏ hoàn toàn biến trong nhiều trường hợp. Ví dụ:
```cpp
// Example 8.24. Integer constant
const int ArraySize = 1000;
int List[ArraySize];
...
for (int i = 0; i < ArraySize; i++) List[i]++;
```
Ở đây, trình biên dịch có thể thay thế tất cả các lần xuất hiện của `ArraySize` bằng giá trị `1000`. Vòng lặp trong ví dụ 8.24 có thể được cài đặt theo một cách hiệu quả hơn nếu giá trị của biến đếm vòng lặp (`ArraySize`) là hằng số và được trình biên dịch nhận biết tại thời điểm biên dịch. Không có bộ nhớ nào được cấp phát cho một hằng số nguyên, trừ khi địa chỉ của nó (`&ArraySize`) được sử dụng.

Một con trỏ `const` hoặc tham chiếu `const` không thể thay đổi giá trị mà nó đang trỏ đến. Một hàm thành viên `const` không thể sửa đổi các thành viên dữ liệu. Bạn được khuyên sử dụng từ khóa `const` ở bất cứ nơi nào thích hợp để cung cấp cho trình biên dịch thêm thông tin về một biến, con trỏ hoặc hàm thành viên vì điều này có thể cải thiện khả năng tối ưu hóa. Ví dụ, trình biên dịch có thể giả định một cách an toàn rằng giá trị của một biến thành viên của lớp sẽ không thay đổi khi gọi đến một hàm `const` thuộc cùng lớp đó.

Từ khóa `static` có một vài ý nghĩa tùy thuộc vào ngữ cảnh. Từ khóa `static`, khi được áp dụng cho một hàm không phải hàm thành viên, nghĩa là hàm đó không được truy cập bởi bất kỳ mô-đun nào khác. Điều này giúp thao tác inlining hiệu quả hơn và cho phép thực hiện các tối ưu hóa interprocedural. Xem trang 81.

Từ khóa `static`, khi áp dụng cho một biến toàn cục, nghĩa là nó không được truy cập bởi bất kỳ mô-đun nào khác. Điều này cho phép thực hiện các tối ưu hóa interprocedural.

Từ khóa `static`, khi áp dụng cho một biến cục bộ bên trong một hàm, nghĩa là biến đó sẽ được bảo tồn khi hàm trả về và giữ nguyên trạng thái trong lần tiếp theo hàm đó được gọi. Điều này có thể không hiệu quả bởi vì một số trình biên dịch sẽ chèn mã bổ sung để bảo vệ biến khỏi sự truy cập từ nhiều luồng cùng một lúc. Điều này có thể được áp dụng ngay cả khi biến là `const`.

Tuy nhiên, vẫn có thể có một lý do để làm cho biến cục bộ trở thành `static` và `const` nhằm đảm bảo rằng nó chỉ được khởi tạo trong lần đầu tiên hàm được gọi. Ví dụ:
```cpp
// Example 8.25
void Func () {
   static const double log2 = log(2.0);
   ...
}
```
Ở đây, `log(2.0)` chỉ được tính toán trong lần đầu tiên `Func` được thực thi. Nếu không có `static`, phép tính logarit sẽ được tính lại mỗi lần `Func` được thực thi. Việc này có nhược điểm là hàm phải kiểm tra xem liệu nó đã được gọi trước đây hay chưa. Việc này nhanh hơn việc tính toán lại logarit, nhưng nó thậm chí sẽ nhanh hơn nữa nếu menjadikan `log2` thành một biến `const` toàn cục hoặc thay thế nó bằng giá trị đã được tính toán.

Từ khóa `static`, khi được áp dụng cho hàm thành viên của lớp, có nghĩa là nó không thể truy cập vào bất kỳ thành viên dữ liệu hoặc hàm thành viên nào không phải là `static`. Một hàm thành viên `static` được gọi nhanh hơn một hàm thành viên không phải là `static` vì nó không cần con trỏ `this`. Rất khuyến khích biến các hàm thành viên thành `static` tại các vị trí thích hợp.

**Các từ khóa đặc thù cho trình biên dịch (Compiler-specific keywords)**
Gọi hàm nhanh (Fast function calling). `__fastcall` hoặc `__attribute__((fastcall))`. Cờ bổ nghĩa `fastcall` có thể giúp quá trình gọi hàm nhanh hơn ở chế độ 32-bit. Hai tham số nguyên đầu tiên được truyền trong các thanh ghi thay vì trên ngăn xếp (ba tham số đối với trình biên dịch CodeGear). Các hàm mang từ khóa fastcall thì không tương thích giữa các trình biên dịch khác nhau. Fastcall là không cần thiết trong chế độ 64-bit vì các tham số dù sao cũng được truyền trong các thanh ghi.

Hàm thuần túy (Pure function). `__attribute__((const))` (chỉ dành cho Linux). Xác định một hàm là hàm thuần túy. Điều này cho phép loại bỏ các biểu thức con chung và di chuyển các đoạn mã bất biến trong vòng lặp. Xem trang 80.

Giả định không có bí danh con trỏ (Assume no pointer aliasing). `__declspec(noalias)` hoặc `__restrict` hoặc `#pragma optimize("a",on)`. Xác định rằng các bí danh con trỏ không xảy ra. Xem giải thích ở trang 79. Xin lưu ý rằng các chỉ thị này không phải lúc nào cũng hoạt động.

Căn chỉnh dữ liệu (Data alignment). `__declspec(align(16))` hoặc `__attribute__((aligned(16)))`. Chỉ định việc căn chỉnh cho các mảng và cấu trúc. Rất hữu ích đối với các thao tác vector, xem trang 107.

## 8.7 Kiểm tra những gì trình biên dịch đang làm
Có thể rất hữu ích khi nghiên cứu đoạn mã mà trình biên dịch tạo ra để xem mức độ tối ưu hóa đoạn mã của nó tốt đến mức nào. Thỉnh thoảng trình biên dịch sẽ thực hiện những việc rất tài tình để khiến cho đoạn mã trở nên hiệu quả hơn, và đôi khi nó thực hiện những điều vô cùng ngớ ngẩn. Nhìn vào đầu ra của trình biên dịch có thể thường xuyên tiết lộ những thứ có thể được cải thiện thông qua việc sửa đổi mã nguồn, như được hiển thị trong ví dụ bên dưới.

Cách tốt nhất để kiểm tra đoạn mã mà trình biên dịch tạo ra là sử dụng tùy chọn của trình biên dịch đối với đầu ra bằng hợp ngữ (assembly language). Trên hầu hết các trình biên dịch, bạn có thể làm điều này bằng cách kích hoạt trình biên dịch từ dòng lệnh với tất cả các tùy chọn tối ưu hóa có liên quan và tùy chọn `-S` hoặc `/Fa` cho đầu ra dưới dạng hợp ngữ. Tùy chọn đầu ra bằng hợp ngữ cũng khả dụng trên một số IDE. Nếu trình biên dịch không có tùy chọn đầu ra bằng hợp ngữ thì hãy sử dụng trình phân dịch hợp ngữ đối tượng (object file disassembler).

Lưu ý rằng trình biên dịch Intel có một tùy chọn cho việc ghi chú mã nguồn (source annotation) bên trong đầu ra dạng hợp ngữ (`/FAs` hoặc `-fsource-asm`). Tùy chọn này giúp cho đầu ra dạng hợp ngữ trở nên dễ đọc hơn, nhưng đáng tiếc là nó ngăn chặn các sự tối ưu hóa nhất định. Không sử dụng tùy chọn chú giải mã nguồn nếu bạn muốn thấy kết quả của sự tối ưu hóa toàn diện.

Ngoài ra, bạn cũng có thể xem mã do trình biên dịch tạo ra tại cửa sổ phân dịch (disassembly window) của trình gỡ lỗi (debugger). Tuy nhiên, đoạn mã mà bạn thấy trong trình gỡ lỗi không phải là phiên bản đã được tối ưu hóa vì các tùy chọn gỡ lỗi ngăn cản quá trình tối ưu hóa. Trình gỡ lỗi không thể đặt các điểm dừng (breakpoint) trong đoạn mã đã được tối ưu hóa đầy đủ vì nó không có thông tin về số thứ tự của dòng mã. Thường thì có thể chèn một điểm dừng cố định trong mã với một câu lệnh hợp ngữ nội tuyến (inline assembly instruction) thông qua hàm ngắt 3 (interrupt 3). Mã lệnh là `__asm int 3;` hoặc `__asm ("int 3");` hoặc `__debugbreak();`. Nếu bạn chạy mã được tối ưu hóa (phiên bản phát hành) trong trình gỡ lỗi thì nó sẽ tạm dừng tại điểm dừng ngắt 3 và hiển thị phần phân dịch, có thể là không bao gồm thông tin về tên của các hàm và tên biến. Hãy nhớ bỏ điểm ngắt thông qua hàm ngắt 3 đi một lần nữa.

Ví dụ sau cho thấy những gì xuất hiện tại đầu ra dạng hợp ngữ của một trình biên dịch và làm thế nào bạn có thể dùng nó để cải thiện đoạn mã.
```cpp
// Example 8.26a
void Func(int a[], int & r) {
   int i;
   for (i = 0; i < 100; i++) {
      a[i] = r + i/2;
   }
}
```
Trình biên dịch Intel tạo ra mã hợp ngữ sau đây từ ví dụ 8.26a (chế độ 32-bit):
```assembly
; Example 8.26a compiled to assembly:
ALIGN     4                                ; align by 4
PUBLIC ?Func@@YAXQAHAAH@Z                  ; mangled function name
?Func@@YAXQAHAAH@Z PROC NEAR              ; start of Func
; parameter 1: 8 + esp                     ; a
; parameter 2: 12 + esp                    ; r
$B1$1:                                     ; unused label
        push      ebx                      ; save ebx on stack
        mov       ecx, DWORD PTR [esp+8]   ; ecx = a
        xor       eax, eax                 ; eax = i = 0
        mov       edx, DWORD PTR [esp+12]  ; edx = r
$B1$2:                                     ; top of loop
        mov       ebx, eax                 ; compute i/2 in ebx
        shr       ebx, 31                  ; shift down sign bit of i
        add       ebx, eax                 ; i + sign(i)
        sar       ebx, 1                   ; shift right = divide by 2
        add       ebx, DWORD PTR [edx]     ; add what r points to
        mov       DWORD PTR[ecx+eax*4],ebx ; store result in array
        add       eax, 1                   ; i++
        cmp       eax, 100                 ; check if i < 100
        jl        $B1$2                    ; repeat loop if true
$B1$3:                                     ; unused label
        pop       ebx                      ; restore ebx from stack
        ret                                ; return
        ALIGN     4                        ; align
?Func@@YAXQAHAAH@Z ENDP                    ; mark end of procedure
```
Hầu hết các nhận xét được tạo ra bởi trình biên dịch đều đã được thay thế bằng những bình luận của riêng tôi, có màu xanh lục. Phải cần đến một số kinh nghiệm để làm quen với việc đọc và hiểu các mã hợp ngữ được tạo bởi trình biên dịch. Hãy để tôi giải thích phần mã ở trên một cách chi tiết. Cái tên có vẻ buồn cười `?Func@@YAXQAHAAH@Z` là tên của hàm `Func` cùng với rất nhiều thông tin được thêm vào về loại hàm cũng như các tham số của nó. Đây được gọi là quá trình thay đổi tên (name mangling). Các ký tự `?`, `@` và `$` được phép xuất hiện trong tên của hợp ngữ. Các thông tin chi tiết về việc name mangling được giải thích trong hướng dẫn số 5: "Quy ước gọi cho các trình biên dịch C++ và hệ điều hành khác nhau". Các tham số `a` và `r` được truyền tới ngăn xếp tại địa chỉ `esp+8` và `esp+12` và lần lượt tải vào trong `ecx` và `edx`. (Trong chế độ 64-bit, các tham số này sẽ được truyền thông qua các thanh ghi thay vì ngăn xếp). `ecx` bây giờ chứa địa chỉ về phần tử đầu tiên của mảng `a` và `edx` thì chứa địa chỉ của biến mà `r` trỏ tới. Một biến tham chiếu có bản chất cũng giống như một con trỏ trong mã hợp ngữ. Thanh ghi `ebx` được đẩy lên trên ngăn xếp trước khi nó được sử dụng và lấy ra khỏi ngăn xếp (popped) trước khi hàm kết thúc. Điều này là vì quy ước về việc sử dụng thanh ghi quy định rằng một hàm không được phép làm thay đổi giá trị của `ebx`. Chỉ có các thanh ghi `eax`, `ecx` và `edx` mới có thể thay đổi một cách tự do. Biến đếm vòng lặp `i` được lưu trữ dưới dạng biến thanh ghi bên trong `eax`. Khởi tạo vòng lặp `i=0;` đã được biên dịch thành lệnh `xor eax,eax`. Đây là một cách phổ biến để đặt giá trị của một thanh ghi bằng không hiệu quả hơn so với lệnh `mov eax,0`. Phần thân vòng lặp bắt đầu tại nhãn (label) `$B1$2:`. Đây chỉ là một cái tên tùy ý mà trình biên dịch đã chọn cho nhãn. Nó dùng `ebx` làm một thanh ghi tạm thời cho việc tính toán `i/2+r`. Cặp lệnh `mov ebx,eax` / `shr ebx,31` dùng để sao chép bit dấu (sign bit) của `i` vào trong bit thấp nhất của `ebx`. Hai lệnh tiếp theo `add ebx, eax` / `sar ebx,1` để cộng kết quả đó vào `i` và dịch phải một bit để tính giá trị `i` chia 2. Lệnh `add ebx, DWORD PTR [edx]` cộng biến mà địa chỉ của nó đang nằm trong `edx` vào `ebx`, chứ không phải là cộng trực tiếp `edx`. Dấu ngoặc vuông cho biết việc sử dụng giá trị của `edx` với vai trò là một con trỏ bộ nhớ. Đây là giá trị của biến mà `r` trỏ đến. Bây giờ `ebx` đang chứa `i/2+r`. Lệnh kế tiếp `mov DWORD PTR [ecx+eax*4],ebx` sẽ lưu trữ kết quả này tại biến `a[i]`. Hãy lưu ý về khả năng hiệu quả từ việc tính toán các địa chỉ trong mảng. `ecx` chứa giá trị địa chỉ vùng bắt đầu của mảng. `eax` giữ giá trị chỉ số mảng, tức là `i`. Chỉ số này cần được nhân với kích thước (tính bằng số byte) của từng phần tử mảng để tính được giá trị địa chỉ của phần tử thứ `i`. Kích thước của biến kiểu `int` là 4. Nên địa chỉ phần tử mảng `a[i]` là `ecx+eax*4`. Kết quả `ebx` sau đó sẽ được đưa vào phần địa chỉ `[ecx+eax*4]`. Tất cả đều được tiến hành qua một câu lệnh duy nhất. CPU sẽ hỗ trợ những dạng lệnh thế này dành cho mục đích truy cập siêu nhanh vào các phần tử bên trong mảng. Lệnh `add eax,1` có chức năng để tăng bước lặp thông qua `i++`. Lệnh `cmp eax, 100` / `jl $B1$2` thể hiện điều kiện trong vòng lặp `i < 100`. Nó đem so sánh `eax` với 100 và quay trở lại chỗ nhãn `$B1$2` nếu trường hợp `i < 100` vẫn còn đúng. Hàm `pop ebx` giúp cho giá trị của `ebx` được phục hồi lại như đã lưu ban đầu. Hàm `ret` tạo kết quả trả về cho hàm.

Bảng liệt kê phần hợp ngữ tiết lộ ba điểm có thể tối ưu hóa sâu hơn nữa. Điều đầu tiên ta để ý là trình biên dịch đã làm một số thứ khá lạ lẫm bằng cách thao tác lên phần bit biểu diễn dấu của `i` nhằm mục đích chia `i` cho 2. Trình biên dịch chưa phát hiện ra rằng `i` sẽ không bao giờ nhận giá trị âm, cho nên chúng ta sẽ không cần thiết phải quan tâm đến bit chỉ phần dấu. Chúng ta hoàn toàn có thể cho nó biết việc này bằng cách biến `i` thành một số kiểu `unsigned int` hoặc ép kiểu `i` sang kiểu `unsigned int` trước khi thực hiện bước chia 2 (Xem trang 140).

Điều thứ hai cần để ý là phần giá trị bị r trỏ tới được đọc lại từ bộ nhớ (memory) hàng trăm lần. Nó diễn ra vì chúng ta quên không ra lệnh cho trình biên dịch rằng hãy đưa ra giả định là sẽ không có bí danh con trỏ (assume no pointer aliasing - xem thêm trên trang 79). Việc thêm cái tùy chọn trình biên dịch về "assume no pointer aliasing" (nếu có hiệu lực) thì cũng có khả năng gia tăng thêm chất lượng đoạn mã.

Điểm thứ ba có thể cải thiện, đó là biểu thức `r+i/2` nên được tính bằng biến quy nạp (induction variable) vì nó biểu thị quan hệ hàm cầu thang so với giá trị chỉ số của bước lặp. Tính chất chia nguyên (integer division) cản trở việc tạo ra biến quy nạp của trình biên dịch trừ trường hợp chúng ta khai triển vòng lặp lên gấp 2. (Xem trang 72).

Kết luận đưa ra là chúng ta có thể giúp trình biên dịch tối ưu hóa ví dụ 8.26a bằng cách khai triển vòng lặp (rolling out) lên mức 2 và tạo ra một biến quy nạp rõ ràng. (Như thế nó sẽ loại bỏ nhu cầu cần thiết đối với hai hướng cải thiện đã được đề xuất đầu tiên).
```cpp
// Example 8.26b  
void Func(int a[], int & r) { 
   int i; 
   int Induction = r; 
   for (i = 0; i < 100; i += 2) { 
      a[i] = Induction; 
      a[i+1] = Induction; 
      Induction++; 
   } 
} 
```
