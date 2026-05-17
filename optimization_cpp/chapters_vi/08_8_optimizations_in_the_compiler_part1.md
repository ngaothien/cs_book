# 8 Tối ưu hóa trong trình biên dịch
## 8.1 Cách trình biên dịch tối ưu hóa
Các trình biên dịch hiện đại có thể thực hiện rất nhiều sửa đổi đối với mã để cải thiện hiệu suất. Rất hữu ích cho lập trình viên khi biết trình biên dịch có thể làm gì và không thể làm gì. Các phần sau đây mô tả một số tối ưu hóa của trình biên dịch mà lập trình viên cần biết.

**Inlining hàm (Function inlining)**
Trình biên dịch có thể thay thế một lời gọi hàm bằng phần thân của hàm được gọi. Ví dụ:
```cpp
// Example 8.1a
float square (float a) {
   return a * a;}

float parabola (float x) {
   return square(x) + 1.0f;}
```
Trình biên dịch có thể thay thế lời gọi `square` bằng đoạn mã bên trong `square`:
```cpp
// Example 8.1b
float parabola (float x) {
   return x * x + 1.0f;}
```
Những lợi thế của inlining hàm là:
* Chi phí của lời gọi hàm, trả về và truyền tham số được loại bỏ.
* Code caching sẽ tốt hơn vì đoạn mã trở nên liền kề nhau.
* Đoạn mã trở nên nhỏ hơn nếu chỉ có một lời gọi đến hàm được inline.
* Inlining hàm có thể mở ra khả năng cho các tối ưu hóa khác, như được giải thích bên dưới.

Nhược điểm của inlining hàm là đoạn mã trở nên lớn hơn nếu có nhiều hơn một lời gọi đến hàm được inline và hàm đó lại lớn. Trình biên dịch có nhiều khả năng inline một hàm hơn nếu nó nhỏ hoặc nếu nó được gọi từ chỉ một hoặc một vài nơi.

**Gộp hằng số (Constant folding) và Truyền hằng số (Constant propagation)**
Một biểu thức hoặc biểu thức con chỉ chứa các hằng số sẽ được thay thế bằng kết quả đã tính toán. Ví dụ:
```cpp
// Example 8.2a
double a, b;
a = b + 2.0 / 3.0;
```
Trình biên dịch sẽ thay thế đoạn này bằng
```cpp
// Example 8.2b
a = b + 0.666666666666666666667;
```
Điều này thực sự khá tiện lợi. Viết `2.0/3.0` sẽ dễ hơn là tự tính giá trị và viết nó ra với nhiều số thập phân. Khuyên bạn nên đặt dấu ngoặc đơn quanh một biểu thức con như vậy để đảm bảo trình biên dịch nhận ra nó là một biểu thức con. Ví dụ, `b*2.0/3.0` sẽ được tính là `(b*2.0)/3.0` thay vì `b*(2.0/3.0)` trừ khi bạn đặt dấu ngoặc đơn quanh biểu thức con hằng số.

Một hằng số có thể được truyền (propagated) qua một chuỗi các phép tính:
```cpp
// Example 8.3a
float parabola (float x) {
   return x * x + 1.0f;}

float a, b;
a = parabola (2.0f);
b = a + 1.0f;
```
Trình biên dịch có thể thay thế bằng:
```cpp
// Example 8.3b
a = 5.0f;
b = 6.0f;
```
Gộp hằng số và truyền hằng số không thể thực hiện được nếu biểu thức chứa một hàm không thể được inline hoặc không thể được tính toán tại thời điểm biên dịch (compile time). Ví dụ:
```cpp
// Example 8.4
double a = sin(0.8);
```
Hàm `sin` được định nghĩa trong một thư viện hàm riêng biệt và bạn không thể mong đợi trình biên dịch có khả năng inline hàm này và tính toán nó tại thời điểm biên dịch. Một số trình biên dịch có khả năng tính toán các hàm toán học phổ biến nhất như `sqrt` và `pow` tại thời điểm biên dịch, nhưng không phải các hàm phức tạp hơn như `sin`.

**Loại bỏ con trỏ (Pointer elimination)**
Một con trỏ hoặc tham chiếu có thể bị loại bỏ nếu mục tiêu được trỏ tới đã được biết trước. Ví dụ:
```cpp
// Example 8.5a
void Plus2 (int * p) {
   *p = *p + 2;}

int a;
Plus2 (&a);
```
Trình biên dịch có thể thay thế bằng:
```cpp
// Example 8.5b
a += 2;
```

**Loại bỏ biểu thức con chung (Common subexpression elimination)**
Nếu cùng một biểu thức con xuất hiện nhiều hơn một lần thì trình biên dịch có thể chỉ tính toán nó một lần. Ví dụ:
```cpp
// Example 8.6a
int a, b, c;
b = (a+1) * (a+1);
c = (a+1) / 4;
```
Trình biên dịch có thể thay thế đoạn này bằng:
```cpp
// Example 8.6b
int a, b, c, temp;
temp = a+1;
b = temp * temp;
c = temp / 4;
```

**Biến thanh ghi (Register variables)**
Các biến được sử dụng phổ biến nhất được lưu trong các thanh ghi (register) (xem trang 27).
Số lượng tối đa của các biến thanh ghi số nguyên xấp xỉ là sáu trong các hệ thống 32-bit và mười bốn trong hệ thống 64-bit.
Số lượng tối đa của các biến thanh ghi dấu phẩy động là tám trong hệ thống 32-bit và mười sáu trong hệ thống 64-bit. Một số trình biên dịch gặp khó khăn trong việc tạo các biến thanh ghi dấu phẩy động trên hệ thống 32-bit trừ khi tập lệnh SSE2 (hoặc mới hơn) được bật.

Trình biên dịch sẽ chọn các biến được sử dụng nhiều nhất để làm biến thanh ghi. Bao gồm cả con trỏ và tham chiếu, những biến này có thể được lưu trong các thanh ghi số nguyên. Các ứng cử viên tiêu biểu cho biến thanh ghi là các biến trung gian tạm thời, biến đếm vòng lặp, tham số hàm, con trỏ, tham chiếu, con trỏ `this`, các biểu thức con chung, và biến quy nạp (induction variables - xem bên dưới).

Một biến không thể được lưu trữ trong thanh ghi nếu địa chỉ của nó được lấy (lấy địa chỉ bằng `&`), tức là nếu có một con trỏ hoặc tham chiếu tới nó. Do đó, bạn nên tránh tạo bất kỳ con trỏ hoặc tham chiếu nào trỏ đến một biến có thể tận dụng không gian lưu trữ thanh ghi.

**Phân tích khoảng hoạt động (Live range analysis)**
Khoảng hoạt động của một biến là phạm vi đoạn mã trong đó biến đó được sử dụng. Một trình biên dịch tối ưu hóa có thể sử dụng cùng một thanh ghi cho nhiều biến nếu khoảng hoạt động của chúng không chồng chéo lên nhau hoặc nếu chúng chắc chắn có cùng một giá trị. Điều này hữu ích khi số lượng thanh ghi có sẵn là hạn chế. Ví dụ:
```cpp
// Example 8.7
int SomeFunction (int a, int x[]) {
   int b, c;
   x[0] = a;
   b = a + 1;
   x[1] = b;
   c = b + 1;
   return c;
}
```
Trong ví dụ này, `a`, `b` và `c` có thể chia sẻ cùng một thanh ghi vì các khoảng hoạt động của chúng không chồng chéo lên nhau. Nếu `c = b + 1` được thay đổi thành `c = a + 2` thì `a` và `b` không thể sử dụng cùng một thanh ghi vì các khoảng hoạt động của chúng bây giờ đã bị chồng chéo.

Các trình biên dịch thường không sử dụng nguyên tắc này cho các đối tượng được lưu trữ trong bộ nhớ. Nó sẽ không sử dụng cùng một vùng bộ nhớ cho các đối tượng khác nhau ngay cả khi khoảng hoạt động của chúng không chồng chéo. Xem trang 90 để biết ví dụ về cách làm cho các đối tượng khác nhau chia sẻ cùng một vùng bộ nhớ.

**Gộp các nhánh giống hệt nhau (Join identical branches)**
Đoạn mã có thể được làm gọn hơn bằng cách gộp các đoạn mã giống hệt nhau. Ví dụ:
```cpp
// Example 8.8a
double x, y, z;  bool b;
if (b) {
   y = sin(x);
   z = y + 1.;
}
else {
   y = cos(x);
   z = y + 1.;
}
```
Trình biên dịch có thể thay thế bằng:
```cpp
// Example 8.8b
double x, y;  bool b;
if (b) {
   y = sin(x);
}
else {
   y = cos(x);
}
z = y + 1.;
```

**Loại bỏ các lệnh nhảy (Eliminate jumps)**
Các lệnh nhảy có thể tránh được bằng cách sao chép đoạn mã mà nó sẽ nhảy tới. Ví dụ:
```cpp
// Example 8.9a
int SomeFunction (int a, bool b) {
   if (b) {
      a = a * 2;
   }
   else {
      a = a * 3;
   }
   return a + 1;
}
```
Mã này có một lệnh nhảy từ `a=a*2;` đến `return a+1;`. Trình biên dịch có thể loại bỏ lệnh nhảy này bằng cách sao chép câu lệnh return:
```cpp
// Example 8.9b
int SomeFunction (int a, bool b) {
   if (b) {
      a = a * 2;
      return a + 1;
   }
   else {
      a = a * 3;
      return a + 1;
   }
}
```

Một nhánh có thể bị loại bỏ nếu điều kiện có thể được đơn giản hóa thành luôn luôn đúng hoặc luôn luôn sai:
```cpp
// Example 8.10a
if (true) {
   a = b;
}
else {
   a = c;
}
```
Có thể rút gọn thành:
```cpp
// Example 8.10b
a = b;
```

Một nhánh cũng có thể bị loại bỏ nếu điều kiện đã được biết từ một nhánh trước đó. Ví dụ:
```cpp
// Example 8.11a
int SomeFunction (int a, bool b) {
   if (b) {
      a = a * 2;
   }
   else {
      a = a * 3;
   }
   if (b) {
      return a + 1;
   }
   else {
      return a - 1;
   }
}
```
Trình biên dịch có thể rút gọn đoạn này thành:
```cpp
// Example 8.11b
int SomeFunction (int a, bool b) {
   if (b) {
      a = a * 2;
      return a + 1;
   }
   else {
      a = a * 3;
      return a - 1;
   }
}
```

**Khai triển vòng lặp (Loop unrolling)**
Một số trình biên dịch sẽ khai triển (unroll) các vòng lặp nếu có yêu cầu về mức độ tối ưu hóa cao. Xem trang 45. Điều này có thể có lợi nếu phần thân của vòng lặp rất nhỏ hoặc nếu nó mở ra khả năng cho những tối ưu hóa sâu hơn. Các vòng lặp với số lần lặp lại rất thấp có thể được khai triển hoàn toàn để tránh chi phí vòng lặp (loop overhead). Ví dụ:
```cpp
// Example 8.12a
int i, a[2];
for (i = 0; i < 2; i++) a[i] = i+1;
```
Trình biên dịch có thể rút gọn thành:
```cpp
// Example 8.12b
int a[2];
a[0] = 1; a[1] = 2;
```
Thật không may, một số trình biên dịch lại khai triển quá mức. Khai triển vòng lặp quá mức là không tối ưu vì nó chiếm quá nhiều không gian trong bộ nhớ đệm (code cache) và nó lấp đầy bộ đệm vòng lặp (loop buffer) mà một số vi xử lý có. Trong một số trường hợp, có thể hữu ích khi tắt tùy chọn khai triển vòng lặp trong trình biên dịch.

**Chuyển động đoạn mã bất biến trong vòng lặp (Loop invariant code motion)**
Một phép tính toán có thể được di chuyển ra ngoài vòng lặp nếu nó độc lập với biến đếm của vòng lặp. Ví dụ:
```cpp
// Example 8.13a
int i, a[100], b;
for (i = 0; i < 100; i++) {
   a[i] = b * b + 1;
}
```
Trình biên dịch có thể thay đổi nó thành:
```cpp
// Example 8.13b
int i, a[100], b, temp;
temp = b * b + 1;
for (i = 0; i < 100; i++) {
   a[i] = temp;
}
```

**Biến quy nạp (Induction variables)**
Một biểu thức là hàm tuyến tính của một biến đếm vòng lặp có thể được tính toán bằng cách cộng thêm một hằng số vào giá trị trước đó. Ví dụ:
```cpp
// Example 8.14a
int i, a[100];
for (i = 0; i < 100; i++) {
   a[i] = i * 9 + 3;
}
```
Trình biên dịch có thể tránh phép nhân bằng cách thay đổi thành:
```cpp
// Example 8.14b
int i, a[100], temp;
temp = 3;
for (i = 0; i < 100; i++) {
   a[i] = temp;
   temp += 9;
}
```

Biến quy nạp thường được sử dụng để tính toán địa chỉ của các phần tử trong mảng. Ví dụ:
```cpp
// Example 8.15a
struct S1 {double a; double b;};
S1 list[100];  int i;
for (i = 0; i < 100; i++) {
   list[i].a = 1.0;
   list[i].b = 2.0;
}
```
Để truy cập một phần tử trong `list`, trình biên dịch phải tính toán địa chỉ của nó. Địa chỉ của `list[i]` bằng với địa chỉ của vị trí bắt đầu `list` cộng với `i*sizeof(S1)`. Đây là một hàm tuyến tính của `i` có thể được tính toán bằng một biến quy nạp. Trình biên dịch có thể sử dụng cùng một biến quy nạp để truy cập `list[i].a` và `list[i].b`. Nó cũng có thể loại bỏ `i` và sử dụng biến quy nạp làm biến đếm vòng lặp khi giá trị cuối cùng của biến quy nạp có thể được tính toán trước. Điều này làm giảm mã xuống còn:
```cpp
// Example 8.15b
struct S1 {double a; double b;};
S1 list[100], *temp;
for (temp = &list[0]; temp < &list[100]; temp++) {
   temp->a = 1.0;
   temp->b = 2.0;
}
```
Yếu tố `sizeof(S1) = 16` thực ra bị ẩn giấu đằng sau cú pháp C++ trong ví dụ 8.15b. Biểu diễn số nguyên của `&list[100]` là `(int)(&list[100]) = (int)(&list[0]) + 100*16`, và `temp++` thực ra cộng 16 vào giá trị số nguyên của `temp`.

Trình biên dịch không cần các biến quy nạp để tính toán địa chỉ của các phần tử mảng thuộc các kiểu đơn giản vì CPU có hỗ trợ phần cứng cho việc tính toán địa chỉ của một phần tử mảng nếu địa chỉ có thể được biểu thị bằng một địa chỉ cơ sở cộng với một hằng số cộng với một chỉ số được nhân với một hệ số là 1, 2, 4 hoặc 8, nhưng không phải bất kỳ hệ số nào khác. Nếu `a` và `b` trong ví dụ 8.15a là kiểu `float` thay vì `double`, thì `sizeof(S1)` sẽ là 8 và không cần biến quy nạp nào vì CPU có hỗ trợ phần cứng để nhân chỉ số với 8.

Các trình biên dịch mà tôi đã nghiên cứu không tạo biến quy nạp cho các biểu thức dấu phẩy động hoặc các biểu thức nguyên phức tạp hơn. Xem trang 81 để biết ví dụ về cách sử dụng các biến quy nạp cho việc tính toán một đa thức.

**Lập lịch (Scheduling)**
Trình biên dịch có thể sắp xếp lại các lệnh (reorder instructions) nhằm mục đích thực thi song song. Ví dụ:
```cpp
// Example 8.16
float a, b, c, d, e, f, x, y;
x = a + b + c;
y = d + e + f;
```
Trình biên dịch có thể đan xen hai công thức trong ví dụ này sao cho `a+b` được tính toán trước, sau đó là `d+e`, tiếp theo `c` được cộng vào tổng đầu tiên, sau đó `f` được cộng vào tổng thứ hai, tiếp theo kết quả thứ nhất được lưu vào `x`, và cuối cùng kết quả thứ hai được lưu vào `y`. Mục đích của việc này là để hỗ trợ CPU thực hiện nhiều phép tính song song. Các CPU hiện đại trên thực tế có khả năng sắp xếp lại các câu lệnh mà không cần tới sự trợ giúp của trình biên dịch (xem trang 105), nhưng trình biên dịch có thể làm cho quá trình sắp xếp lại này trở nên dễ dàng hơn cho CPU.

**Rút gọn đại số (Algebraic reductions)**
Hầu hết các trình biên dịch có thể rút gọn các biểu thức đại số đơn giản bằng cách sử dụng các định luật cơ bản của đại số. Ví dụ, một trình biên dịch có thể thay đổi biểu thức `-(-a)` thành `a`.

Tôi không cho rằng các lập trình viên thường viết các biểu thức như `-(-a)`, nhưng những biểu thức như vậy có thể xuất hiện do kết quả của các quá trình tối ưu hóa khác như inlining hàm. Các biểu thức có thể rút gọn cũng xảy ra khá thường xuyên do quá trình khai triển macro (macro expansions).

Tuy nhiên, các lập trình viên thường viết các biểu thức có thể rút gọn được. Điều này có thể là do biểu thức chưa được rút gọn giải thích tốt hơn logic phía sau chương trình, hoặc do lập trình viên chưa nghĩ về khả năng rút gọn đại số. Ví dụ, một lập trình viên có thể muốn viết `if(!a && !b)` thay vì cách viết tương đương `if(!(a || b))` mặc dù cách thứ hai có ít đi một toán tử. Rất may, tất cả các trình biên dịch đều có khả năng thực hiện rút gọn trong trường hợp này.

Bạn không thể mong đợi một trình biên dịch sẽ rút gọn các biểu thức đại số phức tạp. Ví dụ, chỉ một trong số các trình biên dịch mà tôi đã kiểm tra có khả năng rút gọn `(a*b*c)+(c*b*a)` thành `a*b*c*2`. Rất khó để cài đặt nhiều quy tắc đại số vào trong một trình biên dịch. Một số trình biên dịch có thể rút gọn một vài loại biểu thức và một số trình biên dịch khác có thể rút gọn những loại biểu thức khác, nhưng không có trình biên dịch nào tôi từng thấy có thể rút gọn tất cả chúng. Trong trường hợp của đại số Boolean, có thể cài đặt một thuật toán chung (ví dụ: Quine–McCluskey hoặc Espresso) có khả năng rút gọn bất kỳ biểu thức nào, nhưng không có trình biên dịch nào tôi từng kiểm tra dường như làm điều đó.

Các trình biên dịch giỏi hơn trong việc rút gọn các biểu thức nguyên so với biểu thức dấu phẩy động, mặc dù các quy tắc đại số là như nhau trong cả hai trường hợp. Điều này là do các thao tác đại số trên các biểu thức dấu phẩy động có thể có những tác dụng không mong muốn. Tác dụng này có thể được minh họa bằng ví dụ sau:
```cpp
// Example 8.17
char a = -100, b = 100, c = 100, y;
y = a + b + c;
```
Ở đây, `y` sẽ nhận giá trị `-100+100+100 = 100`. Bây giờ, theo các quy tắc của đại số, chúng ta có thể viết:
```cpp
y = c + b + a;
```
Điều này có thể hữu ích nếu biểu thức con `c+b` có thể được sử dụng lại ở nơi khác. Trong ví dụ này, chúng ta đang sử dụng các số nguyên 8-bit, có phạm vi từ -128 đến +127. Tràn số nguyên sẽ làm cho giá trị quấn vòng lại (wrap around). Việc cộng 1 vào 127 sẽ tạo ra -128, và trừ 1 khỏi -128 sẽ tạo ra 127. Tính toán `c+b` sẽ sinh ra tràn số và cho kết quả là -56 thay vì 200. Tiếp theo, chúng ta cộng -100 với -56, điều này sẽ sinh ra underflow và trả về kết quả 100 thay vì -156. Thật đáng ngạc nhiên, chúng ta kết thúc với đúng kết quả vì tràn số (overflow) và dưới tràn (underflow) đã tự vô hiệu hóa nhau. Đây là lý do tại sao an toàn khi sử dụng các thao tác đại số trên các biểu thức nguyên (ngoại trừ các toán tử `<`, `<=`, `>`, và `>=`).

Lập luận tương tự không áp dụng cho các biểu thức dấu phẩy động. Các biến dấu phẩy động không quấn vòng lại khi xảy ra tràn số hoặc dưới tràn. Phạm vi của các biến dấu phẩy động lớn đến mức chúng ta không cần phải lo lắng nhiều về tràn số và dưới tràn ngoại trừ trong các ứng dụng toán học đặc biệt. Nhưng chúng ta phải lo lắng về việc mất độ chính xác. Hãy lặp lại ví dụ trên với các số dấu phẩy động:
```cpp
// Example 8.18
float a = -1.0E8, b = 1.0E8, c = 1.23456, y;
y = a + b + c;
```
Phép tính ở đây đưa ra `a+b=0`, và sau đó `0+1.23456 = 1.23456`. Nhưng chúng ta sẽ không nhận được kết quả tương tự nếu chúng ta thay đổi thứ tự của các toán hạng và tính tổng `b` và `c` trước. `b+c = 100000001.23456`. Kiểu `float` có độ chính xác khoảng bảy chữ số có nghĩa, vì vậy giá trị của `b+c` sẽ được làm tròn thành `100000000`. Khi chúng xuất hiện, chúng ta cộng `a` vào số này, chúng ta nhận được `0` thay vì `1.23456`.

Kết luận từ lập luận này là thứ tự của các toán hạng dấu phẩy động không thể bị thay đổi mà không có rủi ro mất đi độ chính xác. Các trình biên dịch sẽ không thực hiện điều đó trừ khi bạn chỉ định một tùy chọn cho phép các phép tính dấu phẩy động kém chính xác hơn. Ngay cả với tất cả các tùy chọn tối ưu hóa liên quan đã được bật, các trình biên dịch sẽ không thực hiện các rút gọn quá rõ ràng như `0/a = 0` vì điều này sẽ không hợp lệ nếu `a` là 0 hoặc vô cực hoặc NAN (not a number). Các trình biên dịch khác nhau có hành vi khác nhau vì có những ý kiến khác nhau về sự thiếu chính xác nào được phép và sự thiếu chính xác nào không.

Bạn không thể dựa vào trình biên dịch để thực hiện bất kỳ rút gọn đại số nào trên mã chứa dấu phẩy động và bạn chỉ có thể dựa vào các rút gọn đơn giản nhất trên mã số nguyên. Sẽ an toàn hơn khi tự bạn thực hiện các phép rút gọn một cách thủ công. Tôi đã kiểm tra khả năng thực hiện rút gọn nhiều biểu thức đại số khác nhau trên bảy trình biên dịch khác nhau. Kết quả được liệt kê trong Bảng 8.1 bên dưới.

**Loại bỏ hàm ảo (Devirtualization)**
Một trình biên dịch tối ưu hóa có thể bỏ qua quá trình tra cứu bảng ảo cho một lệnh gọi hàm ảo nếu biết được phiên bản nào của hàm ảo là cần thiết. Ví dụ:
```cpp
// Example 8.19. Devirtualization
class C0 {
   public:
   virtual void f();
};

class C1 : public C0 {
   public:
   virtual void f();
};

void g() {
   C1 obj1;
   C0 * p = & obj1;
   p->f();               // Virtual call to C1::f
}
```
Nếu không có sự tối ưu hóa, trình biên dịch cần tra cứu trong một bảng ảo để xem lời gọi `p->f()` sẽ trỏ đến `C0::f` hay `C1::f`. Nhưng một trình biên dịch tối ưu hóa sẽ thấy rằng `p` luôn luôn trỏ đến một đối tượng của lớp `C1`, vì vậy nó có thể gọi trực tiếp `C1::f` mà không cần sử dụng bảng ảo. Thật không may, rất ít trình biên dịch có khả năng thực hiện tối ưu hóa này.

## 8.2 So sánh các trình biên dịch khác nhau
Tôi đã thực hiện một loạt các thí nghiệm trên bảy nhãn hiệu trình biên dịch C++ khác nhau để xem liệu chúng có khả năng thực hiện các loại tối ưu hóa khác nhau hay không. Kết quả được tóm tắt trong Bảng 8.1. Bảng cho thấy liệu các trình biên dịch khác nhau có thành công trong việc áp dụng các phương pháp tối ưu hóa và rút gọn đại số khác nhau trong các ví dụ kiểm tra của tôi.

Bảng này có thể đưa ra một số chỉ báo về những quá trình tối ưu hóa nào bạn có thể mong đợi một trình biên dịch cụ thể thực hiện và quá trình tối ưu hóa nào bạn phải tự thực hiện bằng tay.

Cần nhấn mạnh rằng các trình biên dịch có thể hoạt động khác nhau trên các ví dụ kiểm tra khác nhau. Bạn không thể hy vọng một trình biên dịch luôn luôn hoạt động theo như trong bảng.
