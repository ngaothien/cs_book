Các đối tượng kiểu phức hợp (composite type) chỉ có thể được trả về trong các thanh ghi (registers) ở những trường hợp đơn giản nhất. Xem tài liệu 5: "Calling conventions for different C++ compilers and operating systems" để biết chi tiết về khi nào các đối tượng có thể được trả về trong các thanh ghi.

Ngoại trừ các trường hợp đơn giản nhất, các đối tượng phức hợp được trả về bằng cách sao chép chúng vào một vị trí do bên gọi (caller) chỉ định thông qua một con trỏ ẩn (hidden pointer). Hàm tạo sao chép (copy constructor), nếu có, thường được gọi trong quá trình sao chép, và hàm hủy (destructor) được gọi khi bản gốc bị hủy. Trong những trường hợp đơn giản, trình biên dịch có thể tránh việc gọi copy constructor và destructor bằng cách khởi tạo đối tượng trực tiếp tại đích đến cuối cùng của nó, nhưng đừng quá trông mong vào điều này.

Thay vì trả về một đối tượng phức hợp, bạn có thể xem xét các lựa chọn thay thế sau:

*   Biến hàm đó thành một constructor (hàm tạo) cho đối tượng.
*   Yêu cầu hàm sửa đổi một đối tượng hiện có thay vì tạo ra một đối tượng mới. Đối tượng hiện có có thể được cung cấp cho hàm thông qua một con trỏ hoặc tham chiếu, hoặc hàm có thể là một hàm thành viên (member function) của lớp chứa đối tượng đó.
*   Yêu cầu hàm trả về một con trỏ hoặc tham chiếu đến một đối tượng tĩnh (static object) được định nghĩa bên trong hàm. Cách này rất hiệu quả, nhưng rủi ro. Con trỏ hoặc tham chiếu được trả về chỉ hợp lệ cho đến khi hàm được gọi lần tiếp theo và đối tượng cục bộ bị ghi đè, có thể là trong một luồng (thread) khác. Nếu bạn quên đặt đối tượng cục bộ thành `static` thì nó sẽ trở nên không hợp lệ ngay khi hàm trả về.
*   Yêu cầu hàm tạo một đối tượng với `new` và trả về một con trỏ trỏ tới nó. Cách này không hiệu quả vì chi phí cấp phát bộ nhớ động. Phương pháp này cũng tiềm ẩn rủi ro rò rỉ bộ nhớ (memory leaks) nếu bạn quên xóa (`delete`) đối tượng.

## 7.17 Hàm đệ quy đuôi (Function tail calls)

Gọi đuôi (tail call) là một cách để tối ưu hóa các lệnh gọi hàm. Nếu câu lệnh cuối cùng của một hàm là lệnh gọi tới một hàm khác, thì trình biên dịch có thể thay thế lệnh gọi đó bằng một lệnh nhảy (jump) tới hàm thứ hai. Một trình biên dịch tối ưu hóa sẽ tự động thực hiện điều này. Hàm thứ hai sẽ không trả về hàm thứ nhất, mà trả trực tiếp về nơi hàm thứ nhất được gọi. Việc này hiệu quả hơn vì nó loại bỏ được một bước trả về (return). Ví dụ:

```cpp
// Example 7.35. Tail call 
void function2(int x); 

void function1(int y) { 
  ... 
   function2(y+1); 
} 
```

Ở đây, việc trả về từ `function1` bị loại bỏ bằng cách nhảy trực tiếp đến `function2`. Điều này hoạt động ngay cả khi có giá trị trả về:

```cpp
// Example 7.36. Tail call with return value 
int function2(int x); 

int function1(int y) { 
  ... 
   return function2(y+1); 
} 
```

Tối ưu hóa gọi đuôi chỉ hoạt động nếu hai hàm có cùng kiểu trả về. Nếu các hàm có tham số trên ngăn xếp (điều này thường xảy ra ở chế độ 32-bit) thì hai hàm phải sử dụng cùng một dung lượng không gian ngăn xếp cho các tham số.

## 7.18 Hàm đệ quy (Recursive functions)

Hàm đệ quy là một hàm tự gọi chính nó. Các lệnh gọi hàm đệ quy có thể hữu ích trong việc xử lý các cấu trúc dữ liệu đệ quy. Cái giá phải trả cho các hàm đệ quy là tất cả các tham số và biến cục bộ sẽ có một thể hiện (instance) mới sau mỗi lần đệ quy, và điều này tiêu tốn không gian ngăn xếp (stack space). Đệ quy sâu cũng làm cho việc dự đoán địa chỉ trả về kém hiệu quả hơn. Vấn đề này thường xuất hiện với các mức đệ quy sâu hơn 16 (xem giải thích về return stack buffer trong tài liệu 3: "The microarchitecture of Intel, AMD and VIA CPUs").

Tuy nhiên, lệnh gọi hàm đệ quy vẫn có thể là giải pháp hiệu quả nhất để xử lý cấu trúc dữ liệu dạng cây phân nhánh (branching data tree structure). Đệ quy sẽ hiệu quả hơn nếu cấu trúc cây mở rộng theo chiều ngang (broad) thay vì đi sâu (deep). Đệ quy không phân nhánh (non-branching recursion) luôn có thể được thay thế bằng một vòng lặp, vòng lặp này sẽ hiệu quả hơn. Một ví dụ kinh điển trong sách giáo khoa về hàm đệ quy là hàm tính giai thừa:

```cpp
// Example 7.37. Factorial as recursive function 
unsigned long int factorial(unsigned int n) { 
   if (n < 2) return 1; 
   return n * factorial(n-1); 
} 
```

Cách triển khai này rất kém hiệu quả vì tất cả các thể hiện của `n` và tất cả các địa chỉ trả về đều chiếm dụng không gian lưu trữ trên ngăn xếp. Sẽ hiệu quả hơn nếu sử dụng một vòng lặp:

```cpp
// Example 7.38. Factorial function as loop 
unsigned long int factorial(unsigned int n) { 
   unsigned long int product = 1; 
   while (n > 1) { 
      product *= n; 
      n--; 
   } 
   return product; 
} 
```

Gọi đệ quy đuôi (Recursive tail calls) hiệu quả hơn các lệnh gọi đệ quy khác, nhưng vẫn kém hiệu quả hơn vòng lặp.

Những lập trình viên mới vào nghề đôi khi gọi hàm `main` để khởi động lại chương trình của họ. Đây là một ý tưởng tồi vì ngăn xếp sẽ bị lấp đầy bởi các thể hiện mới của tất cả các biến cục bộ sau mỗi lần gọi đệ quy tới `main`. Cách đúng đắn để khởi động lại một chương trình là tạo một vòng lặp bên trong `main`.

## 7.19 Cấu trúc và lớp (Structures and classes)

Ngày nay, các sách giáo khoa lập trình khuyến nghị lập trình hướng đối tượng (object oriented programming) như một phương pháp để làm cho phần mềm rõ ràng và mang tính mô-đun hơn. Các cái gọi là đối tượng (objects) chính là các thể hiện (instances) của các cấu trúc (structures) và lớp (classes). Phong cách lập trình hướng đối tượng có cả tác động tích cực lẫn tiêu cực đến hiệu suất chương trình. Các tác động tích cực là:

*   Các biến được sử dụng cùng nhau cũng sẽ được lưu trữ cùng nhau nếu chúng là thành viên của cùng một cấu trúc hoặc lớp. Điều này giúp cho việc caching dữ liệu hiệu quả hơn.
*   Các biến là thành viên của một lớp không cần phải được truyền như các tham số cho một hàm thành viên (member function) của lớp đó. Nhờ vậy, ta tránh được chi phí (overhead) truyền tham số cho các biến này.

Các tác động tiêu cực của lập trình hướng đối tượng là:

*   Các hàm thành viên không tĩnh (Non-static member functions) có một con trỏ `this` được truyền vào như một tham số ẩn cho hàm. Chi phí truyền tham số cho con trỏ `this` sẽ phát sinh trên tất cả các hàm thành viên không tĩnh.
*   Con trỏ `this` chiếm một thanh ghi (register). Thanh ghi là tài nguyên khan hiếm trong các hệ thống 32-bit.
*   Các hàm thành viên ảo (Virtual member functions) kém hiệu quả hơn (xem trang 55).

Không thể khẳng định một cách khái quát rằng những tác động tích cực hay tiêu cực của lập trình hướng đối tượng đang chiếm ưu thế. Ít nhất có thể nói rằng việc sử dụng các lớp và hàm thành viên không hề tốn kém. Bạn có thể sử dụng phong cách lập trình hướng đối tượng nếu nó tốt cho cấu trúc logic và độ trong sáng của chương trình, miễn là bạn tránh sử dụng số lượng lệnh gọi hàm quá lớn ở những phần trọng yếu nhất của chương trình. Việc sử dụng các cấu trúc (không có các hàm thành viên) không gây tác động tiêu cực nào đến hiệu suất.

## 7.20 Thành viên dữ liệu của lớp (Class data members / instance variables)

Các thành viên dữ liệu (data members) của một lớp hoặc cấu trúc được lưu trữ liên tiếp theo thứ tự chúng được khai báo bất cứ khi nào một thể hiện của lớp hoặc cấu trúc đó được tạo ra. Không có hình phạt hiệu suất nào (performance penalty) cho việc tổ chức dữ liệu thành các lớp hoặc cấu trúc. Truy cập vào một thành viên dữ liệu của một đối tượng thuộc lớp hoặc cấu trúc không tốn nhiều thời gian hơn so với truy cập vào một biến đơn giản.

Hầu hết các trình biên dịch sẽ căn lề (align) các thành viên dữ liệu tới các địa chỉ làm tròn để tối ưu hóa truy cập, như cho trong bảng sau:

| Kiểu dữ liệu | Kích thước, byte | Căn lề, byte |
| :--- | :--- | :--- |
| `bool` | 1 | 1 |
| `char`, signed hoặc unsigned | 1 | 1 |
| `short int`, signed hoặc unsigned | 2 | 2 |
| `int`, signed hoặc unsigned | 4 | 4 |
| `64-bit integer`, signed hoặc unsigned | 8 | 8 |
| con trỏ (pointer) hoặc tham chiếu (reference), chế độ 32-bit | 4 | 4 |
| con trỏ (pointer) hoặc tham chiếu (reference), chế độ 64-bit | 8 | 8 |
| `float` | 4 | 4 |
| `double` | 8 | 8 |
| `long double` | 8, 10, 12 hoặc 16 | 8 hoặc 16 |

*Bảng 7.2. Căn lề các thành viên dữ liệu.*

Sự căn lề này có thể tạo ra các "lỗ hổng" chứa các byte không được sử dụng bên trong một cấu trúc hoặc lớp có các thành viên mang kích thước hỗn hợp. Ví dụ:

```cpp
// Example 7.39a 
struct S1 { 
   short int a;  // 2 bytes. byte đầu tại 0, byte cuối tại 1 
                 // 6 bytes không được sử dụng
   double b;     // 8 bytes. byte đầu tại 8, byte cuối tại 15 
   int d;        // 4 bytes. byte đầu tại 16, byte cuối tại 19 
                 // 4 bytes không được sử dụng 
}; 
S1 ArrayOfStructures[100]; 
```

Ở đây, có 6 byte không sử dụng giữa `a` và `b` bởi vì `b` phải bắt đầu ở một địa chỉ chia hết cho 8. Cũng có 4 byte không sử dụng ở phần cuối. Lý do là thể hiện tiếp theo của `S1` trong mảng phải bắt đầu ở một địa chỉ chia hết cho 8 để căn lề thành viên `b` của nó theo bộ bội số của 8. Số byte không sử dụng có thể được giảm xuống còn 2 bằng cách đặt các thành viên nhỏ nhất ở vị trí cuối cùng:

```cpp
// Example 7.39b 
struct S1 { 
   double b;     // 8 bytes. byte đầu tại 0, byte cuối tại 7 
   int d;        // 4 bytes. byte đầu tại 8, byte cuối tại 11 
   short int a;  // 2 bytes. byte đầu tại 12, byte cuối tại 13 
                 // 2 bytes không được sử dụng 
}; 
S1 ArrayOfStructures[100]; 
```

Việc sắp xếp lại này làm cho cấu trúc nhỏ hơn 8 byte và toàn bộ mảng nhỏ hơn 800 byte.

Các đối tượng cấu trúc và lớp thường có thể được làm nhỏ hơn bằng cách sắp xếp lại thứ tự các thành viên dữ liệu. Nếu lớp có ít nhất một hàm thành viên ảo (virtual member functions) thì sẽ có một con trỏ trỏ tới bảng ảo (virtual table) được đặt trước thành viên dữ liệu đầu tiên hoặc sau thành viên dữ liệu cuối cùng. Con trỏ này có kích thước 4 byte trong các hệ thống 32-bit và 8 byte trong các hệ thống 64-bit. Nếu bạn nghi ngờ cấu trúc hoặc mỗi thành viên của nó lớn bao nhiêu thì bạn có thể làm một vài phép thử nghiệm với toán tử `sizeof`. Giá trị trả về bởi toán tử `sizeof` đã bao gồm bất kỳ byte chưa sử dụng nào ở cuối đối tượng.

Mã lệnh dùng để truy cập vào một thành viên dữ liệu sẽ nhỏ gọn (compact) hơn nếu khoảng cách (offset) từ thành viên đó đến phần đầu của cấu trúc hoặc lớp nhỏ hơn 128 byte, vì độ dời này có thể được biểu diễn dưới dạng số có dấu 8-bit. Nếu độ dời so với phần đầu của cấu trúc hoặc lớp từ 128 byte trở lên thì nó phải được biểu thị dưới dạng số 32-bit (tập lệnh không có dạng nào nằm giữa độ dời 8-bit và 32-bit). Ví dụ:

```cpp
// Example 7.40 
class S2 { 
   public: 
   int a[100];  // 400 bytes. byte đầu tại 0, byte cuối tại 399 
   int b;       // 4 bytes. byte đầu tại 400, byte cuối tại 403 
   int ReadB() {return b;} 
}; 
```

Độ dời (offset) của `b` ở đây là 400. Mọi mã lệnh truy cập vào `b` thông qua một con trỏ hoặc một hàm thành viên như `ReadB` đều phải mã hóa offset này thành số 32-bit. Nếu tráo đổi vị trí của `a` và `b` thì cả hai đều có thể được truy cập với offset được mã hóa bằng số có dấu 8-bit, hoặc không cần offset. Điều này làm cho mã lệnh gọn gàng hơn để bộ đệm mã (code cache) được sử dụng hiệu quả hơn. Do đó, có một lời khuyên là các mảng lớn và các đối tượng lớn khác nên được đặt cuối cùng trong một cấu trúc hoặc lớp khai báo, và các thành viên dữ liệu được sử dụng thường xuyên nhất nên được đặt lên đầu. Nếu không thể chứa tất cả các thành viên dữ liệu trong 128 byte đầu tiên thì hãy đưa những thành viên được sử dụng thường xuyên nhất vào khu vực 128 byte đầu tiên này.

## 7.21 Hàm thành viên của lớp (Class member functions / methods)

Mỗi lần một đối tượng mới của một lớp được khai báo hoặc tạo ra, nó sẽ sinh ra một thể hiện mới của các thành viên dữ liệu. Nhưng mỗi hàm thành viên chỉ có đúng một thể hiện duy nhất. Mã của hàm không bị sao chép vì cùng một mã có thể được áp dụng cho mọi thể hiện của lớp.

Gọi một hàm thành viên nhanh ngang với gọi một hàm đơn giản kèm theo con trỏ hoặc tham chiếu trỏ đến một cấu trúc. Ví dụ:

```cpp
// Example 7.41 
class S3 { 
   public: 
   int a; 
   int b; 
   int Sum1() {return a + b;} 
}; 
int Sum2(S3 * p) {return p->a + p->b;} 
int Sum3(S3 & r) {return  r.a +  r.b;} 
```

Ba hàm `Sum1`, `Sum2` và `Sum3` đang làm những việc giống hệt nhau và chúng đều hiệu quả như nhau. Nếu bạn xem mã được trình biên dịch tạo ra, bạn sẽ nhận thấy rằng một số trình biên dịch sẽ tạo ra các đoạn mã y hệt nhau cho cả ba hàm này. `Sum1` có một con trỏ ẩn `this` thực hiện việc tương tự như con trỏ `p` và tham chiếu `r` ở trong `Sum2` và `Sum3`. Việc bạn muốn để hàm đó là một thành viên của lớp hay cung cấp cho nó một con trỏ hoặc tham chiếu tới lớp (hoặc cấu trúc) đơn giản chỉ là vấn đề của phong cách lập trình. Vài trình biên dịch sẽ làm cho `Sum1` hiệu quả hơn một chút so với `Sum2` và `Sum3` trên hệ điều hành Windows 32-bit bằng cách truyền con trỏ `this` trong một thanh ghi thay vì trên ngăn xếp.

Hàm thành viên tĩnh (static member function) không thể truy cập bất kỳ thành viên dữ liệu không tĩnh hay hàm thành viên không tĩnh nào. Một hàm thành viên tĩnh nhanh hơn một hàm thành viên không tĩnh vì nó không cần con trỏ `this`. Bạn có thể tăng tốc cho các hàm thành viên bằng cách biến chúng thành hàm `static` nếu chúng không cần bất kỳ quyền truy cập không tĩnh nào.

## 7.22 Hàm thành viên ảo (Virtual member functions)

Các hàm ảo (Virtual functions) được sử dụng để hiện thực hóa các lớp đa hình (polymorphic classes). Mỗi thể hiện của một lớp đa hình có một con trỏ trỏ đến một bảng con trỏ tương ứng với các phiên bản khác nhau của các hàm ảo. Bảng này được gọi là bảng ảo (virtual table), dùng để tìm đúng phiên bản của hàm ảo tại thời điểm chạy (runtime). Tính đa hình (Polymorphism) là một trong những nguyên nhân chính khiến các chương trình hướng đối tượng trở nên kém hiệu quả hơn so với các chương trình không hướng đối tượng. Nếu bạn có thể tránh sử dụng các hàm ảo, thì bạn có thể có được hầu hết các lợi thế của lập trình hướng đối tượng mà không phải trả giá bằng chi phí hiệu năng.

Thời gian để gọi một hàm thành viên ảo mất nhiều hơn vài chu kỳ xung nhịp so với gọi một hàm thành viên không ảo, với điều kiện là câu lệnh gọi hàm luôn luôn gọi cùng một phiên bản của hàm ảo. Nếu phiên bản này thay đổi thì bạn có thể phải nhận hình phạt do dự đoán sai (misprediction penalty) từ 10 - 20 chu kỳ xung nhịp. Các quy tắc đối với việc dự đoán đúng và sai của các lệnh gọi hàm ảo cũng tương tự như quy tắc dành cho lệnh `switch`, như đã giải thích ở trang 44.

Cơ chế điều phối (dispatching mechanism) có thể bị bỏ qua khi hàm ảo được gọi trên một đối tượng đã biết rõ kiểu dữ liệu, nhưng bạn không phải lúc nào cũng có thể tin tưởng vào việc trình biên dịch sẽ bỏ qua cơ chế điều phối này ngay cả khi nó là một việc cực kỳ hiển nhiên. Xem trang 74.

Tính đa hình tại thời điểm chạy (Runtime polymorphism) chỉ cần thiết nếu ta không thể biết được phiên bản nào của một hàm thành viên đa hình sẽ được gọi tại thời điểm biên dịch. Nếu các hàm ảo được dùng trong một khu vực quan trọng của chương trình, bạn có thể xem xét xem liệu có khả năng nào đạt được chức năng mong muốn mà không dùng tính đa hình, hoặc có thể dùng tính đa hình lúc biên dịch (compile-time polymorphism) hay không.

Đôi khi ta có thể đạt được hiệu ứng đa hình mong muốn với template (khuôn mẫu) thay vì các hàm ảo. Tham số template nên là một lớp chứa các hàm có nhiều phiên bản. Phương pháp này nhanh hơn bởi vì tham số template luôn được phân giải ở thời điểm biên dịch chứ không phải tại runtime. Ví dụ 7.47 trang 59 minh họa cách làm việc này. Đáng tiếc là cú pháp này có phần rườm rà (kludgy) tới mức nó có thể không bõ công.

## 7.23 Nhận dạng kiểu thời gian chạy (Runtime type identification - RTTI)

Tính năng nhận dạng kiểu tại thời điểm chạy (Runtime type identification) gắn thêm thông tin phụ vào tất cả các đối tượng của lớp và tính năng này thì không hiệu quả. Nếu trình biên dịch có một tùy chọn để dùng RTTI, hãy tắt nó đi và dùng các cách triển khai thay thế khác.

## 7.24 Kế thừa (Inheritance)

Một đối tượng thuộc một lớp dẫn xuất (derived class) được triển khai theo cách tương tự với một đối tượng của một lớp đơn giản chứa tất cả các thành viên từ cả lớp cha và lớp con. Các thành viên của lớp cha và lớp con được truy cập với tốc độ nhanh như nhau. Nhìn chung, bạn có thể mặc định coi rằng gần như không có bất kỳ hình phạt hiệu suất nào cho việc sử dụng tính kế thừa.

Tuy vậy, có thể có một chút suy giảm nhẹ ở quá trình cache mã lệnh do những nguyên nhân sau:

*   Kích thước (tính bằng byte) các thành viên dữ liệu của lớp cha được cộng dồn vào khoảng lệch (offset) của các thành viên lớp con. Các đoạn mã lệnh truy cập tới những thành viên dữ liệu có tổng offset lớn hơn 127 byte sẽ kém gọn nhẹ hơn (less compact). Xem trang 54.
*   Các hàm thành viên của cha và con thường được lưu trữ trong các mô-đun (tệp) khác nhau. Điều này có thể dẫn tới việc nhảy lệnh xung quanh quá nhiều, khiến khả năng cache mã lệnh kém đi. Vấn đề này có thể được xử lý bằng cách đảm bảo rằng các hàm thường được gọi cùng nhau thì cũng phải được lưu ở gần nhau. Xem trang 89 để rõ chi tiết.

Kế thừa từ nhiều lớp cha (đa kế thừa) trong cùng một thế hệ có thể gây ra nhiều sự rắc rối với các con trỏ thành viên, các hàm ảo, hoặc khi truy cập vào một đối tượng thuộc lớp dẫn xuất thông qua một con trỏ trỏ tới một trong các lớp cơ sở. Bạn có thể tránh sử dụng đa kế thừa bằng cách nhúng các đối tượng vào bên trong lớp dẫn xuất:

```cpp
// Example 7.42a. Multiple inheritance 
class B1; class B2; 
class D : public B1, public B2 { 
public: 
   int c; 
}; 
```

Thay thế bằng:

```cpp
// Example 7.42b. Alternative to multiple inheritance 
class B1; class B2; 
class D : public B1 { 
public: 
   B2 b2; 
   int c; 
}; 
```

## 7.25 Hàm tạo và Hàm hủy (Constructors and destructors)

Hàm tạo (constructor) được triển khai nội bộ như một hàm thành viên để trả về tham chiếu đến đối tượng đó. Việc cấp phát bộ nhớ cho một đối tượng mới không nhất thiết phải do bản thân hàm tạo thực hiện. Vì thế các hàm tạo hiệu quả giống như bất kỳ hàm thành viên nào khác. Điều này áp dụng cho hàm tạo mặc định (default constructors), hàm tạo sao chép (copy constructors), và bất kỳ loại hàm tạo nào khác.

Một lớp không bắt buộc phải có một constructor. Không cần tới constructor mặc định nếu như đối tượng đó không cần thiết khởi tạo. Hàm tạo sao chép (copy constructor) là không cần thiết nếu đối tượng có thể được sao chép đơn giản bằng cách copy tất cả các thành viên dữ liệu của nó. Một constructor đơn giản có thể được inlined nhằm tối ưu hóa hiệu suất.

Hàm tạo sao chép có thể bị gọi bất cứ khi nào một đối tượng bị copy bằng phép gán (assignment), thông qua tham số hàm (function parameter), hoặc thông qua giá trị trả về của hàm (function return value). Hàm tạo sao chép có thể là tác nhân ngốn thời gian nếu nó cần phải cấp phát bộ nhớ hoặc các tài nguyên khác. Có rất nhiều cách để phòng tránh việc sao chép lãng phí các khối bộ nhớ (memory blocks), ví dụ như:

*   Dùng tham chiếu (reference) hoặc con trỏ (pointer) tới đối tượng thay vì sao chép toàn bộ đối tượng.
*   Sử dụng "move constructor" để chuyển quyền sở hữu của khối bộ nhớ. Việc này yêu cầu trình biên dịch phải hỗ trợ tiêu chuẩn C++0x (C++11).
*   Tạo một hàm thành viên, hàm bạn (friend function), hoặc toán tử có nhiệm vụ chuyển giao quyền sở hữu khối nhớ từ một đối tượng này sang đối tượng khác. Đối tượng vừa mất đi quyền sở hữu đối với khối nhớ đó nên trỏ con trỏ của nó về `NULL`. Dĩ nhiên, luôn cần phải có một destructor để hủy bất kỳ khối nhớ nào mà đối tượng đang sở hữu.

Một hàm hủy (destructor) cũng mang lại hiệu năng cao như một hàm thành viên. Đừng tạo ra destructor nếu điều đó là không cần thiết. Một destructor ảo (virtual destructor) có độ hiệu quả tương tự như một hàm thành viên ảo. Xem trang 55.

## 7.26 Unions

Union là một dạng cấu trúc trong đó các thành viên dữ liệu dùng chung cùng một khoảng không gian bộ nhớ. Ta có thể dùng union để tiết kiệm không gian bộ nhớ bằng cách cho phép hai thành viên dữ liệu (những biến mà chẳng bao giờ được dùng cùng một lúc) sử dụng chung mảnh bộ nhớ. Xem ví dụ trang 91.

Một union cũng có thể dùng để truy cập vào cùng một dữ liệu theo nhiều kiểu cách khác nhau. Ví dụ:

```cpp
// Example 7.43 
union { 
   float f; 
   int i; 
} x; 
x.f = 2.0f; 
x.i |= 0x80000000;  // thiết lập bit dấu của f 
cout << x.f;        // sẽ in ra -2.0 
```

Trong ví dụ này, bit dấu (sign bit) của `f` được bật bằng cách sử dụng toán tử OR bitwise, vốn chỉ có thể áp dụng cho các biến số nguyên.

## 7.27 Trường bit (Bitfields)

Bitfield có thể rất hữu ích trong việc thu gọn dữ liệu. Việc truy xuất một thành viên của bitfield kém hiệu năng hơn so với truy xuất thành viên của một structure. Tuy nhiên, thời gian chênh lệch phụ trội này có thể được biện minh trong trường hợp mảng quá lớn; khi đó, nó có thể giúp tiết kiệm không gian cache hoặc giảm bớt dung lượng tập tin.

Sẽ nhanh hơn nếu cấu thành một bitfield thông qua toán tử dịch bit `<<` và toán tử `|`, thay vì viết từng thành viên một. Ví dụ:

```cpp
// Example 7.44a 
struct Bitfield { 
   int a:4; 
   int b:2; 
   int c:2; 
}; 
Bitfield x; 
int A, B, C; 
x.a = A; 
x.b = B; 
x.c = C; 
```

Giả sử rằng các giá trị của A, B và C là đủ nhỏ để không làm phát sinh sự cố tràn số (overflow), thì mã lệnh này có thể được nâng cấp tối ưu như sau:

```cpp
// Example 7.44b 
union Bitfield { 
   struct { 
      int a:4; 
      int b:2; 
      int c:2; 
   }; 
   char abc; 
}; 
Bitfield x; 
int A, B, C; 
x.abc = A | (B << 4) | (C << 6); 
```

Hoặc, nếu như cần có sự bảo vệ chống tràn (overflow protection):

```cpp
// Example 7.44c 
x.abc = (A & 0x0F) | ((B & 3) << 4) | ((C & 3) <<6 ); 
```

## 7.28 Hàm nạp chồng (Overloaded functions)

Những phiên bản khác nhau của một hàm nạp chồng được trình biên dịch xem xét đơn giản như các hàm độc lập khác nhau. Sử dụng các hàm nạp chồng không tạo ra bất cứ hình phạt nào về mặt hiệu suất.

## 7.29 Toán tử nạp chồng (Overloaded operators)

Một toán tử được nạp chồng thực chất cũng tương đương như một hàm. Sử dụng một toán tử nạp chồng có độ hiệu quả hoàn toàn ngang bằng với một hàm mang cùng một chức năng.

Tuy nhiên, một biểu thức chứa nhiều toán tử nạp chồng sẽ gây ra việc khởi tạo các đối tượng tạm thời (temporary objects) dùng để chứa kết quả trung gian, điều này có thể nằm ngoài ý muốn. Ví dụ:

```cpp
// Example 7.45a 
class vector {                                // 2-dimensional vector 
public: 
   float x, y;                                // x,y coordinates 
   vector() {}                                // default constructor 
   vector(float a, float b) {x = a; y = b;}   // constructor 
   vector operator + (vector const & a) {     // sum operator 
      return vector(x + a.x, y + a.y);}       // add elements 
}; 

vector a, b, c, d; 
a = b + c + d;         // tạo đối tượng tạm thời trung gian cho cụm (b + c) 
```

Việc phải tạo đối tượng trung gian chứa kết quả `(b + c)` có thể được loại bỏ nhờ việc kết nối các phép toán tử thành cụm:

```cpp
// Example 7.45b 
a.x = b.x + c.x + d.x; 
a.y = b.y + c.y + d.y; 
```

Rất may là đa phần mọi trình biên dịch đều có thể tự mình thực hiện quá trình tối ưu hóa này một cách tự động đối với những trường hợp cơ bản.

## 7.30 Khuôn mẫu (Templates)

Khuôn mẫu (template) có tính chất tựa như một macro theo nghĩa các tham số của template (khuôn mẫu) sẽ được thay bằng giá trị tương ứng của chúng trước bước biên dịch. Ví dụ sau đây miêu tả sự khác nhau giữa tham số hàm (function parameter) và tham số khuôn mẫu (template parameter):

```cpp
// Example 7.46 
int Multiply (int x, int m) { 
   return x * m;} 

template <int m> 
int MultiplyBy (int x) { 
   return x * m;} 

int a, b; 
a = Multiply(10,8); 
b = MultiplyBy<8>(10); 
```

Cả `a` và `b` đều cùng trả về kết quả `10 * 8 = 80`. Điểm dị biệt nằm ngay ở cách `m` được đẩy qua hàm xử lí. Ở hàm cơ bản, biến `m` được đưa sang từ luồng gọi lúc runtime (caller to called function). Cơ mà ở hàm thiết kế bằng template, thì tham số `m` bị ghi đè sẵn vào hàm (biên dịch lại với giá trị đó), kết quả là compiler thấy được ngay 1 số hằng (constant) `8` thay vì biến số `m`. Sức mạnh của thủ thuật dùng tham số template hơn tham số thông thường chính là loại bỏ chi phí truyền nhận của bước gán thông số. Tuy vậy khuyết điểm của template là: mỗi lần ứng với 1 thông số parameter thay đổi thì trình biên dịch buộc lòng đẻ ra một bản copy hàm template mới. Cụ thể ở hàm `MultiplyBy` ở trên, khi bạn nhét nhiều hệ số template parameter vô, khối lượng mã sinh ra đâm phình to khổng lồ.

Ở thí dụ trên, lệnh hàm khuôn mẫu `template` có tốc độ xử lý lẹ hơn hàm bình thường, lí do bởi nó nhận biết bản thân đang phải nhân lũy thừa cơ số hai và biến đổi nó bằng toán tử dịch (shift operation). Mã `x*8` nhường chỗ lại cho mã `x<<3` siêu nhanh. Về phía hàm bình thường, compiler không đoán được giá trị của biến `m` là bao nhiêu nên đành ngậm ngùi chạy mà bỏ xó việc tối ưu hóa, trừ trường hợp hàm đó bị inlined (Inlined function). (Trong bài toán vừa rồi, cả 2 function đều được Inline, vì thế compiler nhét thẳng luôn giá trị `80` vào `a` và `b` cho xong. Thế nhưng những ca đụng độ hóc búa, compiler khó mà kham nổi công tác thần kỳ ấy).

Thông số template parameter cũng đóng vai trò kiểu loại Type. Hãy tham khảo ví dụ ở trang số 39 để hình dung cách bạn nhào nặn những mảng dữ liệu Type vô định hình qua cùng bộ khung template như thế nào.

Template hoạt động rất mượt mà vì mọi tham số template đều được sáng tỏ tức khắc (resolved) ngay tại quá trình biên dịch (compile time). Mặc dù template khiến lớp vỏ source code thêm thắt phần rối não, thế nhưng dung lượng cục mã được dịch (compiled code) thì không lớn thêm tẹo nào. Tóm lại, chẳng tồn tại rào cản cản trở tốc độ execution speed nào khi viện tới template.

Hai hay đa số nhiều template sẽ bị nhồi cục làm chung (một instance) chừng nào thông số (template parameter) giữa chúng hệt nhau như khuôn đúc. Một khi lòi ra dị biệt dù nhỏ nhoi thì sẽ xuất hiện một cá thể template phân lập mới tương ứng một bộ thông số. Khai sinh một mớ cá thể instance template đẩy quy mô file compiled to ra và chiếm cả rổ không gian bộ đệm mã.

Sử dụng tràn lan vô độ template đẩy Source code vào cảnh rối rắm, ngột ngạt. Chừng nào bản thân cái template chỉ mang 1 hình hài (instance) duy nhất thì ta hoàn toàn nên chuyển bớt về `#define`, `const`, `typedef` thay vì gồng gánh bằng template.

Khuôn mẫu có thể được vận dụng như kỹ nghệ siêu lập trình metaprogramming, giải thích tại trang 154.

**Dùng template thế chỗ tính năng Đa hình (polymorphism)**

Khuôn mẫu class thừa sức giải quyết vấn đề đa hình tại quá trình biên dịch (compile-time polymorphism), tỏ rõ thế lực mạnh áp đảo việc sử dụng đa hình thông qua Virtual Member (Hàm ảo) trong khi runtime. Trình bày sau đây cho bạn thấy diện mạo đa hình đa hệ qua Runtime:

```cpp
// Example 7.47a. Runtime polymorphism with virtual functions 
class CHello { 
public: 
   void NotPolymorphic();    // Hàm không đa hình
   virtual void Disp();      // Hàm ảo (Virtual function)
   void Hello() { 
      cout << "Hello "; 
      Disp();                // Call to virtual function 
   } 
}; 

class C1 : public CHello { 
   public: 
   virtual void Disp() { 
      cout << 1; 
   } 
}; 

class C2 : public CHello { 
   public: 
   virtual void Disp() { 
      cout << 2; 
   } 
}; 

void test () { 
   C1 Object1;  C2 Object2; 
   CHello * p; 
   p = &Object1; 
   p->NotPolymorphic();      // Được gọi trực tiếp
   p->Hello();               // Writes "Hello 1" 
   p = &Object2; 
   p->Hello();               // Writes "Hello 2" 
} 
```

Bảng phân công cho cơ cấu điều hướng để nhảy vào hàm `C1::Disp()` hay `C2::Disp()` ở Runtime diễn ra khi compiler tịt ngòi không biết trỏ `p` thực sự trỏ tới loại Class Object nào (đọc phần trang 74). Compiler thời nay vốn kém cỏi trong kĩ nghệ vô hiệu hóa con trỏ `p` hay mang chức năng `Object1.Hello()` vô trào lưu Inlining, dẫu chăng tương lai nó có thể tự làm được.

Chừng nào việc xác thực đối tượng trỏ về `C1` hay `C2` (khi compile time) có thể thấy rõ, lúc đấy bạn sẽ hoàn toàn loại bỏ quá trình phân luồng ảo (virtual function dispatch process) rùa bò đi. Chúng ta sẽ cầu cứu sự trợ lực qua trick mánh khóe đến từ thư viện chuẩn (Active Template Library (ATL) và Windows Template Library (WTL)):

```cpp
// Example 7.47b. Compile-time polymorphism with templates 

// Các hàm phi đa hình sẽ đóng đô tại lớp "Grandparent": 
class CGrandParent { 
public: 
   void NotPolymorphic(); 
}; 

// Hàm nào cần cầu viện tới chức năng đa hình, dời về lớp "Parent".
// Lớp con (Child) tham gia qua ngõ Template Parameter: 
template <typename MyChild> 
class CParent : public CGrandParent { 
public: 
   void Hello() { 
      cout << "Hello "; 
      // Gọi lệnh gọi class hàm đa hình con: 
      (static_cast<MyChild*>(this))->Disp(); 
   } 
}; 

// Các Class lớp Con (Child classes) triển khai đa hệ tính năng: 
class CChild1 : public CParent<CChild1> { 
   public: 
   void Disp() { 
      cout << 1; 
   } 
}; 

class CChild2 : public CParent<CChild2> { 
   public: 
   void Disp() { 
      cout << 2; 
   } 
}; 

void test () { 
   CChild1 Object1;  CChild2 Object2; 
   CChild1 * p1; 
   p1 = &Object1; 
   p1->Hello();              // Ghi "Hello 1" 
   CChild2 * p2; 
   p2 = &Object2; 
   p2->Hello();              // Ghi "Hello 2" 
} 
```

Lớp `CParent` trở thành môt template class gánh vác mọi thông tin xuất xứ từ lớp class Con qua Template parameter. Lớp cha sẽ khéo léo triệu tập nhánh hàm đa hình của nhánh con bằng cách ép kiểu (Type-cast) mảng con trỏ `this` hướng tới Class con cái của mình. Công đoạn đầy gian truân kia chỉ hiệu nghiệm chừng nào đúng lớp Child nằm dưới danh sách template parameter mà thôi. Nhắc nhở cho kĩ:

```cpp
class CChild1 : public CParent<CChild1> { 
```

sở hữu chuẩn mực y xì hệ tham chiếu trùng khớp từ Template Parameter.

Hàng thừa kế cha-con chia chác theo dòng trật tự sau. Thế hệ cụ nội gốc thứ nhất (`CGrandParent`) dung túng nhóm tính năng phi đa hình (non-polymorphic). Dòng máu phụ thân lai lai thứ hai (`CParent<>`) ôm trọn mớ hàm Member function hễ dính dáng gì đến đa hình (polymorphic function). Dòng cháu ngoại chắt hệ ba mới thực mang theo đầy đủ các version (chức năng) đa hình đặc biệt của riêng mỗi nhánh. Thế hệ thứ hai lĩnh hội và hấp thu tri thức lớp thứ ba nhờ tính năng (Template parameter).

Như thế là trọn vẹn dẹp tan cái nạn gián đoạn dispatch virtual, vì xuất thân Object (class nào) đã phơi bày. Bí mật đã bật mí, nằm khỏa lấp trong hai loại type thuộc `p1` và `p2`. Sự mệt mỏi ở đây bỗng xuất hiện: bộ class `CParent::Hello()` đẻ thành bầy đàn vô số phiên bản lấp chiếm toàn không gian Code Cache.

Không thể chối cãi, diện mạo mã của Example 7.47b là cồng kềnh/rối beng (kludgy). Một dúm xung nhịp giật lại nhờ màn dẹp bỏ cơ cấu Virtual chả bao giờ khỏa lấp nổi bãi mìn chằng chịt, hãi hùng khiến cho công cuộc duy trì/bảo trì tốn xương máu. Phải chăng ta phó mặc tất cho Compiler với tính năng "devirtualization" (ảo hóa lại, trang 74) một cách tự động, xem chừng vẫn nhàn nhã hơn là gánh khối tạ qua kĩ thuật template xoắn não bên trên.

## 7.31 Luồng (Threads)

Thread (Luồng) sinh ra nhằm thao tác hai và bạt ngàn nhiều hơn thao tác làm việc chồng lấp / tức thì cùng một lúc (hoặc trông giống như thế). Phía cái lõi (CPU Core) hẩm hiu đơn phương thì việc chạy mọi việc trơn mượt tại một khoảnh khắc là vô phương. Kéo theo đó mỗi Thread bị xắt mỏng từng miếng thời gian (time slices) ngốn độ chừng 30ms cho dạng thức foreground và 10ms dạt qua các ứng dụng background. Công việc vất vả thuyên chuyển (Context switches) nhảy cóc luân phiên làm đau đầu (ngốn giá trị kinh khủng) các cụm Cached, nó cần thì giờ hòa nhịp môi trường tác vụ mới. Ngược lại, người ta giãn cách nới lỏng thêm miếng ăn thời gian Slice sẽ đỡ khổ công thuyên chuyển Switch. Nới lỏng Time Slice đồng nghĩa bóp nghẹt User input, dẫn đến thời gian chờ gõ phím trễ lê thê (tại Window bạn kéo giãn nó bằng Optimize performance for background services dưới thẻ tùy chọn Advanced system performance option, còn với Linux, ai mà biết được).

Luồng (Thread) đắc dụng khi bạn ban sắc lệnh trọng vọng ưu tiên cho mảng việc (tasks) khác nhau. Tại trình biên tập văn bản, người dùng yêu cầu hệ thống ngay tắp lự tuân lệnh các luồng gõ phím/lướt chuột (Mouse/Keyboard). Mảng task thao tác tương tác phải lẫy lừng uy thế bậc cao (high priority). Ngược lại các nhóm việc khác, như tra cứu lỗi cú pháp, tự dàn hàng trang tự động (repagination) sẽ vứt xó tại luồng Threads ưu tiên bét nhè. Nước cờ đó tạo thế phân chia tách biệt (ưu tiên), kẻo không, cái máy có thể đứng trân mình ì ạch từ tốn vì bộ não phải lo check lỗi trước, gõ chữ sau (vô vọng đắp ứng yêu cầu user keyboard).

Đóng cọc mấy thể loại mảng task làm hao nguyên khí bộ nhớ - cỡ như giải phương trình tính toán vĩ mô - nằm ngoài phạm vi UI bằng mọi giá, tránh xa khu vực luồng User Interface. Tránh cái họa màn hình đơ máy (unresponsive).

Ta có đủ bản lĩnh giả lập quá trình phân bổ các Threads ngay chính ứng dụng Application mà chả màn dòm qua/ thỉnh lệnh (Operating system thread scheduler) của Hệ Điều Hành làm gì. Áp dụng cái trick chia nhỏ công việc background ra bằng các mảnh cắn vụn (small pieces) vào trong cụm mã vòng lặp đồ họa Message (OnIdle ở Windows MFC). Giải pháp mang tới hiệu suất cho nhóm 1 CPU core tốt hơn nhưng bị gò bó yêu cầu bài toán chia làm sao cho đều đoạn việc, trôi đều mượt ở hàm thời lượng thích hợp.

Cách trọn vẹn đẩy sức vóc các công việc (Jobs) cho một cổ máy siêu nhiều nhân (CPU Cores) là tung rải đều nhiều luồng Thread. Mỗi CPU tự cáng đáng lấy mảng Thread cá thể đó.

Tựu chung bốn góc độ ngốn tài nguyên khi đa nhiệm (Multithreading) buộc ta rà soát:

*   Cái giá cho khâu Khởi động/ Ngắt luồng (Starting and stopping threads). Khoan vội phó mặc giao 1 Task vô 1 luồng mỏng manh Thread hễ độ dài Task chưa bù đắp kịp lượng thời gian cho Start/Stop Thread.
*   Cái giá cho việc hoán đổi nhiệm vụ (Task switching). Quá trình này sẽ vô hại hễ mức độ Thread tương đồng ưu tiên không chạm mức quá số đo quy định của lượng tài nguyên lõi CPU cores.
*   Cái giá của sự chờ đợi kết nối đồng thuận luồng qua lại. Việc trùm gánh Semaphores, Mutexes quá nặng. Khi đôi bên cứ thấp thỏm hóng hớt nhau tới đợt giải phóng tài nguyên, một cách tốt nhất thì gộp ngay chúng vô làm 1 luồng (one thread). Việc công khai tham số xài chung ở cả hai (shared variable), biến ấy cần đội thêm tiền tố `volatile`. Ngăn trở Compiler tự tiện mông má/ phá phách biến đó.
*   Nhiều luồng Threads xâu xé chia 5 xẻ 7 vùng Storage: nghiêm cấm Function / Class nằm chung chạ tĩnh - Global / Static variables. (Vui lòng coi trang 28 Thread-local storage). Đống hầm bà lằng riêng lẻ bộ nhớ (Stack) đẩy nhanh mâu thuẫn/va đập tranh chấp ở mặt Cache contentions (một khi đụng độ chung 1 mảng Cache).

Đã lập trình cho ứng dụng đa luồng (Multithreaded) phải trang bị kỹ thuật bọc thép "Thread-safe". Đừng xài cái chi tĩnh (Static) ở trong!

Tham khảo rõ chương 10, trang 102 đào sâu cặn kẽ nghệ thuật Đa luồng (Multithreading).

## 7.32 Ngoại lệ và xử lý lỗi (Exceptions and error handling)

Tính năng quản lý khối Ngoại lệ sinh ra với thiên chức nhặt nhạnh đống xà bần rác lỗi (hiếm khi xảy ra), để chữa cháy chương trình tránh sụp nguồn (graceful way). Chúng ta lầm to đinh ninh quá trình bọc Ngoại lệ (Exception handling) vô hình chẳng chiếm chác tí ti sức mạnh, trong khi lỗi Error chưa thèm gõ cửa! Sự đời đâu hoàn hảo. Phần mềm cần vận nội công lo chuyện chuẩn bị phương án sổ sách (bookkeeping), đề phòng/ lỡ khi bùng phát 1 trận lôi đình (exception), nó có đường rút mà tự hồi phục. Quy mô sự mệt mỏi ở quá trình Bookkeeping dựa vào Compiler nào thao diễn nó. Mảng Compiler theo hướng bảng quy chiếu (table-based) cực lợi (hao tốn gần zero chi phí overhead) khi đặt cạnh những hệ Compiler mã hóa cứng cựa (code-based) hay đèo bòng ôm thêm nhóm RTTI, những nhóm nầy vấy bẩn các bãi mìn lung tung ra toàn hệ code. Hãy xem lại ấn bản ISO/IEC TR18015 Technical Report on C++ Performance để coi giải thích sâu sát.

Mẫu sau bóc mẽ quá trình vất vả sổ sách chuẩn bị (bookkeeping) như thế nào:

```cpp
// Example 7.48 
class C1 { 
   public: 
   ... 
   ~C1(); 
}; 

void F1() { 
   C1 x; 
   ... 
} 

void F0() {    
   try { 
      F1(); 
   } 
   catch (...) { 
   ... 
   } 
} 
```

Đoạn lệnh `F1` mang sứ mệnh cao cả: triệu hồi destructor của mã object `x` khi rời ghế hàm (return). Thế nhưng biến cố (Exception) nổ súng đánh ập giữa đường lúc `F1` còn tại vị? Bỏ của chạy lấy người ra khỏi `F1`! Chẳng thấy Destructor lên tiếng thu dọn bãi chiến trường, vì sự vụ đã bị phá nát (brutally interrupted). Phút lâm nguy, Exception handler choàng gánh vác việc sai phái gọi hộ lệnh hàm Destructor `x` cho `F1`. Cơ chế ảo diệu vận hành, chừng nào `F1` đã bàn giao trọn vẹn bộ nhớ mật mã gọi Destructor hoặc cái sự thu dọn nào khác cần cho cái đám rác Exception handler. Mà này! Hễ `F1` triệu hồi một anh bạn hàm khác, ông nội kia lại gọi đệ gọi đàn dài lòa xòa, lúc đấy nếu chấn động exception đâm ngay trái tim hàm sâu xa nhất, thì tay vác súng (exception handler) phải moi móc ra trọn cỗ dây chuyền gốc rễ, phăng dọc truy tung trở ra ngọn ngành theo từng nấc thang gọi Functions, và kiểm soát hết việc thu gọn rác bãi chiến trường. Kỹ nghệ ảo này vang danh bảng vàng với nghệ danh: Xả cuộn ngăn xếp (Stack unwinding).

Hàng ngàn Function rùng rùng cúi đầu cất lại thông tin cho cơ chế chúa tể Exception, dù cho bói không ra 1 vệt ngoại lệ xuất hiện. Vì thế tính năng này kéo lùi tiến trình làm việc lại với nhóm compiler cổ lổ xỉ. Chừng nào Application chẳng đoái hoài sử dụng, lập tức phế truất đi (vô hiệu hóa) nhằm cứu rỗi sinh linh code chạy siêu lẹ và mi nhon (smaller). Bạn ban phép trừ tà cho cả bộ máy phần mềm bằng lệnh Disable exception handling trong trình cài đặt compiler. Còn với mỗi 1 tệp lệnh (chức năng đơn chiếc), kẹp cái bảng trừ tà (throw()) chặn đầu họng vào cái hàm nguyên mẫu (prototype) của nó:

```cpp
void F1() throw(); 
```

Mệnh lệnh nầy phó thác, để compiler ngộ nhận 100% `F1` chẳng bao giờ đẻ/mửa ra 1 exception nào ráo, thế là compiler tháo xích tha cho `F1` không cần vác cái gánh nặng dọn dẹp (recovery information). Mỉa mai ở chỗ, rủi `F1` kết giao 1 nhóm lệnh `F2` mà hàm `F2` văng miễn/ném đá (throw exception) thì lúc đó `F1` buộc tròng phải thanh tra kiểm soát nhóm exception của ông `F2` bằng phương thức bắt tại trận: gọi hàm chuẩn (`std::unexpected()`). Kết luận: Đừng tùy tiện gắn mác hàm rỗng (empty throw()) cho chức năng `F1` khi mà các bạn không thể làm điều tương tự dán bảng (empty throw()) lên các anh bạn chức năng nó gọi. Empty throw() rất bám việc và ăn rơ dành cho mảng library function.

Compiler xét nét tường tận giữa hai hàm "Leaf" (hàm lá) và "Frame" (hàm khung). Hàm khung Frame gọi vẫy gọi tới 1 đàn em function. Còn Leaf đi chiếc lẻ loi (không có hàm chắp nối). Rõ rành rành Leaf vinh hiển nhẹ tâng (vượt lên) do chẳng phải chất lên mình thông điệp xả xui ngăn xếp (stack unwinding), bởi ngoại lệ không dính líu chi, hoặc không có cái rác rưởi nào đáng dọn để lại. Việc phẫu thuật nâng cấp 1 con gà "Frame function" lên hàng chúa tể "Leaf" rất trơn tru khi áp dụng đòn phép Nội-hóa Inline (inline all functions it calls) xả hết mọi liên hàm. Tuyệt tác hoàn mỹ nhất lộ diện lúc nào cái vòng lặp tử huyệt (innermost loop) dọn sạch bách cái bóng dáng 1 tay hàm Frame calls.

Cũng có lúc trống vắng throw (empty throw()) đem lại lợi thế tối ưu (optimization). Khuyên là đừng vẽ vời, trát thêm màu (như `throw(A,B,C)`) mô tả cụ thể chi chít đống loại mã Exception nào sắp sổ lồng. Thật lòng mà nói, Compiler sẽ thù dai và quăng thêm rác "check the exceptions type" vào để phạt lỗi, hòng xác minh đám rác lỗi có y nguyên khuôn mẫu specified types đã báo! (Tác giả Sutter: A Pragmatic Look at Exception Specifications, Dr Dobbs Journal, 2002).

Một vài phân khúc tử thần, cơ chế Exception lại mang hiệu quả phi thường (thâm nhập trọng tâm ruột vòng lặp). Áp dụng tại những điểm nút khi cách thức khác gây rườm rà (inefficient) và bạn băn khoăn tìm hướng khôi phục cái mã sau đợt tai nạn lỗi Error. Quan sát ví dụ:

```cpp
// Example 7.49 
// Portability note: Mẫu này đặc trị cho hệ Microsoft compilers. 
// Bộ cánh khác có thể xài lệnh trệch đi tùy compiler. 
#include <excpt.h> 
#include <float.h> 
#include <math.h> 
#define EXCEPTION_FLT_OVERFLOW  0xC0000091L 

void MathLoop() { 
   const int arraysize = 1000;  unsigned int dummy; 
  double  a[arraysize], b[arraysize], c[arraysize]; 

   // Cho phép quăng đá ném ngoại lệ Overflow: 
  _controlfp_s(&dummy, 0, _EM_OVERFLOW);  
   // _controlfp(0, _EM_OVERFLOW); // nếu rủi thay lệnh trên tê liệt 
  
  int i = 0;   // Thiết lập bộ đếm Counter từ tận vòng ngoài cùng
   // Đặt cụm while làm rào phao cứu sinh, đợi khôi phục sau biến loạn exception: 
   while (i < arraysize) { 
      // Săn đón trói exception tại rào chắn nầy: 

      __try { 
         // Khúc ruột siêu tử huyệt, cày cuốc mã: 
        for ( ; i < arraysize; i++) { 

            // Cơn ác mộng bùng nổ văng tràn Overflow khi hàm nhân: 
            a[i] = log (b[i] * c[i]); 
         } 
      } 
      // Vây bắt mỗi nạn Tràn Dấu phẩy động (FLT OVERFLOW), bơ đi mấy mảng kia: 
      __except (GetExceptionCode() == EXCEPTION_FLT_OVERFLOW 
      ? EXCEPTION_EXECUTE_HANDLER : EXCEPTION_CONTINUE_SEARCH) { 
         // Cơn bão Overflow xẹt ngang. 
         // Rà lại thiết đặt Status của Float: 
         _fpreset(); 
         _controlfp_s(&dummy, 0, _EM_OVERFLOW);  
         // _controlfp(0, _EM_OVERFLOW); // lỡ trên fail thì vác vô

         // Mần lại bài toán theo đường hẹp an toàn (cứu tràn): 
         a[i] = log(b[i]) + log(c[i]); 

         // Vỗ về cái bộ đếm biến tăng rồi tiễn về lại chiến trường for-loop: 
         i++; 
      } 
   } 
} 
```

Bạn có ngỡ `b[i]` và `c[i]` bành trướng vĩ mô sinh cảnh Tràn Số Overflow lúc hai ông nội này nhân nhau `b[i]*c[i]`, hiếm khi, cơ mà vẫn có! Đoạn mã vây lưới chực bắt trọn bọn Exception ngay khoảnh khắc tràn, thong dong bắt tay chạy tính tay công thức cũ với sự hao gầy (tốn giờ) bù đắp lại trị tuyệt để nạn tràn số. Mọi người đều biết phương pháp quy đổi trị phép Logarit hai hệ số triệt tiêu nguy cơ Tràn Số Overflow, đổi lại phí phạm giờ giấc công hai thao tác nhân lên (doubled time calculation).

Gần như Zero chi phí dọn đường Exception handling do bộ khu vực tử huyệt Innermost vòng lặp không bóng dáng cấu trúc Check `try` (lẫn hàm chéo nào ngoài mảng chuẩn `log`). `log` nằm chễm chệ trong hệ hàm thư viện, đã được gọt dũa Optimization (tối ưu hóa). Thôi khỏi bàn lùi vì chúng ta dẫu sao cấm cản đụng vô/chỉnh mảng Exception handling của hàm này. Exception chém ngọt cục Thời gian một khi lỡ xảy ra, phước cái là hãn hữu mới lú mặt.

Không rơi hạt bụi hiệu suất khi dò tìm nạn Tràn Số bên trong hàm. Do việc rà soát đã có tay anh hai phần cứng bộ vi xử lý (CPU Hardware hardware) phát xung cảnh cáo! HĐH trói dính (cảnh báo bắt Exception) ném thẳng cổ về tay Xử lí Lỗi Exceptions (ở trong khối mã, nếu khai phá cắm block "try").

Vấp mìn di động (portability issue) khi áp phần cứng phần mềm exception hardware. Hệ lệnh này bám víu mãu nhỏ ngầm không đồng chuẩn quy chiếu (non-standardized), nằm đan xen tùy compiler, hệ điều hành HĐH, và CPU. Trổ tài port ứng dụng (sang môi trường platform khác biệt) dự báo đem tàn phá sửa tanh bành bộ codebase.

Quay mòng mòng điểm lại vài thế chân của exception. Phương trình có quyền thanh trừng số đo khổng lồ quá khổ `b[i]` hay `c[i]` lúc nhân nhau. Điều này trói buộc 2 lượt đánh giá Dấu phẩy động (2 floating comparisons) khiến hao tiền tốn lực, ác đạn là nó mắc ở ngay rún Innermost loop. Phương pháp hạ đẳng tiếp vác nguyên xi thuật toán làm phép: `a[i] = log(b[i]) + log(c[i]);`. Bạn lãnh trọn hai cú tốn lực triệu hồi hàm `log` (mà hàm nầy chậm như rùa). Một cánh cửa sáng bừng nếu rà soát Overflow xảy ra ngoài Vòng Lặp loop hòng tha không soi đủ mọi ngóc mảng mã mảng. Soi Overflow lúc chập choạng vô vòng lặp nếu thông số hệ số nạp giống mẩu parameter. Đợi đến lúc phán ván cờ, dồn công lực dọn kết quả để check overflow! Tràn không cản (uncaught overflow) sùi bọt ra khối vô tận (infinity), hệ giá trị lan tỏa ngấm rỉ qua công đoạn khác gieo lại kết cục INF hoặc rác (NAN - Not A Number), một khi Overflow giáng đòn hỏng bét ở đâu đó hệ thống. Có thể xài mảng hàm kiểm tra lỗi xem INF (vd hàm `_finite()`), lỡ hỏng thì vá, chạy thuật toán tính tay an toàn. Chú ý con dao hai lưỡi, tính tốn ở các mẫu vi xử lý đẻ thêm vài khoảng giật thời gian (take more time) cho bọn rác INF hoặc NAN.

**Tránh cái giá phải trả của quá trình quản lý ngoại lệ (Avoiding the cost of exception handling)**

Việc xử lý ngoại lệ là không cần thiết khi không có ý định phục hồi lỗi. Nếu bạn chỉ muốn chương trình xuất ra một thông báo lỗi và dừng chương trình trong trường hợp có lỗi, thì không có lý do gì để sử dụng `try`, `catch` và `throw`. Sẽ hiệu quả hơn nếu bạn định nghĩa một hàm xử lý lỗi của riêng mình, hàm này đơn giản chỉ in ra một thông báo lỗi thích hợp rồi sau đó gọi `exit`.

Tuy nhiên, gọi `exit` có thể không an toàn nếu có các tài nguyên đã được cấp phát cần phải được dọn dẹp, như được giải thích dưới đây. Có những cách khác để xử lý lỗi mà không cần dùng đến exceptions. Hàm phát hiện ra lỗi có thể trả về một mã lỗi (error code) mà hàm gọi (calling function) có thể dùng để phục hồi hoặc xuất ra một thông báo lỗi.

Chúng tôi khuyến nghị bạn nên sử dụng một cách tiếp cận có hệ thống và được suy tính kỹ lưỡng để xử lý lỗi. Bạn phải phân biệt rõ ràng giữa các lỗi có thể phục hồi (recoverable) và không thể phục hồi (non-recoverable); đảm bảo các tài nguyên đã cấp phát được dọn dẹp gọn gàng trong trường hợp xảy ra lỗi; và tạo các thông báo lỗi phù hợp cho người dùng.

**Làm cho mã lệnh an toàn với ngoại lệ (Making exception-safe code)**

Giả sử một hàm mở một tệp tin (file) ở chế độ độc quyền (exclusive mode), và một tình huống lỗi nào đó chấm dứt chương trình trước khi tệp tin được đóng lại. Tệp tin đó sẽ vẫn bị khóa sau khi chương trình kết thúc và người dùng sẽ không thể truy cập vào nó cho đến khi máy tính được khởi động lại. Để phòng ngừa loại vấn đề này, bạn phải làm cho chương trình của mình an toàn với ngoại lệ (exception safe). Nói cách khác, chương trình phải dọn dẹp sạch sẽ mọi thứ trong trường hợp xảy ra ngoại lệ hoặc các tình trạng lỗi khác. Những thứ có thể cần dọn dẹp bao gồm:

*   Bộ nhớ được cấp phát bằng lệnh `new` hoặc `malloc`.
*   Các Handle trỏ tới các window (cửa sổ), graphic brush (cọ đồ họa), v.v.
*   Các mutex đang bị khóa.
*   Các kết nối cơ sở dữ liệu (database connections) đang mở.
*   Các tệp tin và kết nối mạng đang mở.
*   Các tệp tin tạm (temporary files) cần được xóa bỏ.
*   Các tiến trình công việc của người dùng đang thực hiện cần được lưu lại.
*   Bất kỳ tài nguyên nào khác đã được cấp phát.

Phong cách chuẩn của C++ để xử lý các công việc dọn dẹp là sử dụng hàm hủy (destructor). Một hàm vừa có chức năng đọc hoặc ghi tệp tin có thể được bao bọc (wrapped) vào trong một lớp, và lớp đó có một hàm hủy (destructor) với nhiệm vụ đảm bảo rằng tệp tin đó chắc chắn sẽ được đóng lại. Phương pháp tương tự có thể được sử dụng cho bất kỳ tài nguyên nào khác, chẳng hạn như bộ nhớ cấp phát động, cửa sổ đồ họa, mutex, kết nối cơ sở dữ liệu, v.v.

Hệ thống xử lý ngoại lệ của C++ sẽ đảm bảo rằng tất cả các destructor của các đối tượng cục bộ (local objects) đều sẽ được gọi. Chương trình sẽ an toàn trước ngoại lệ nếu nó có các lớp vỏ bọc (wrapper classes) chứa các destructor để lo liệu toàn bộ việc dọn dẹp các tài nguyên đã cấp phát. Ngược lại, hệ thống có nguy cơ sụp đổ nếu như bản thân một destructor lại gây ra một ngoại lệ khác.

Nếu bạn tạo ra hệ thống xử lý lỗi của riêng mình thay vì sử dụng cơ chế xử lý ngoại lệ tích hợp sẵn (exception handling), thì bạn không thể chắc chắn rằng tất cả các destructor đều sẽ được gọi và tài nguyên sẽ được dọn dẹp sạch. Nếu một trình xử lý lỗi (error handler) gọi `exit()`, `abort()`, `_endthread()`, v.v. thì sẽ không có gì đảm bảo rằng tất cả các destructor được gọi cả. Cách an toàn để xử lý một lỗi không thể phục hồi (unrecoverable error) mà không sử dụng exceptions là trả về (return) từ chính hàm đó. Hàm có thể trả về một mã lỗi (error code) nếu có thể, hoặc mã lỗi có thể được lưu trữ trong một đối tượng toàn cục (global object). Sau đó, hàm gọi (calling function) bắt buộc phải kiểm tra cái mã lỗi đó. Nếu hàm gọi này cũng có thứ gì đó cần dọn dẹp thì nó lại phải tiếp tục thực hiện trả về cho hàm đã gọi nó, và cứ thế tiếp tục (truy ngược lên đầu dây).

## 7.33 Những trường hợp tháo cuộn ngăn xếp khác (Other cases of stack unwinding)

Đoạn trước đã mô tả một cơ chế gọi là tháo cuộn ngăn xếp (stack unwinding), được sử dụng bởi các trình xử lý ngoại lệ (exception handlers) cho mục đích dọn dẹp và gọi tới bất kỳ destructor nào cần thiết, sau khi chương trình nhảy thoát ra khỏi một hàm trong trường hợp có ngoại lệ mà không sử dụng con đường trả về bình thường (return route). Cơ chế này cũng được áp dụng trong hai tình huống khác:

Cơ chế tháo cuộn ngăn xếp có thể được sử dụng khi một luồng (thread) bị kết thúc. Mục đích là để dò xét xem liệu có bất kỳ đối tượng nào được khai báo trong luồng đó sở hữu một hàm hủy (destructor) đang cần được gọi hay không. Lời khuyên là hãy `return` (trả về) từ các hàm yêu cầu dọn dẹp tài nguyên trước khi bạn chủ động kết thúc một thread. Bạn không thể dám chắc rằng một cuộc gọi tới `_endthread()` sẽ dọn dẹp ngăn xếp một cách gọn gàng. Hành vi này hoàn toàn phụ thuộc vào từng nền tảng hoặc trình biên dịch cụ thể (implementation dependent).

Cơ chế tháo cuộn ngăn xếp cũng được sử dụng khi hàm `longjmp` được dùng để nhảy thoát ra khỏi một hàm. Nên tránh sử dụng `longjmp` nếu có thể. Đừng trông cậy vào `longjmp` trong các đoạn mã nhạy cảm về thời gian (time-critical code).

## 7.34 Chỉ thị tiền xử lý (Preprocessing directives)

Các chỉ thị tiền xử lý (Preprocessing directives - mọi thứ bắt đầu bằng dấu `#`) hoàn toàn miễn phí (costless) xét về mặt hiệu suất của chương trình, bởi vì chúng được phân giải xong xuôi từ trước khi chương trình được biên dịch.

Các chỉ thị `#if` rất hữu ích cho việc hỗ trợ đa nền tảng hoặc đa cấu hình (multiple configurations) mà chỉ cần sử dụng cùng một mã nguồn. `#if` hoạt động hiệu quả hơn lệnh `if` thông thường vì `#if` được giải quyết ngay lúc biên dịch (compile time) trong khi `if` được đánh giá tại thời điểm chạy (runtime).

Các chỉ thị `#define` tương đương với các định nghĩa `const` khi được sử dụng cho mục đích định nghĩa các hằng số. Chẳng hạn, `#define ABC 123` và `const int ABC = 123;` là hiệu quả như nhau, bởi vì trong hầu hết các trường hợp, một trình biên dịch tối ưu hóa có thể thay thế thẳng một hằng số nguyên bằng giá trị thực sự của nó. Tuy nhiên, khai báo `const int` trong vài trường hợp có thể chiếm một phần không gian bộ nhớ.
