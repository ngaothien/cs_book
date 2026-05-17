# 14 Các chủ đề tối ưu hóa cụ thể (Specific optimization topics)

## 14.1 Sử dụng bảng tra cứu (Use lookup tables)

Việc đọc một giá trị từ bảng các hằng số sẽ rất nhanh nếu bảng đó được lưu trong bộ nhớ cache. Thông thường chỉ mất vài chu kỳ xung nhịp để đọc từ một bảng trong bộ nhớ cache mức 1 (level-1 cache). Chúng ta có thể tận dụng thực tế này bằng cách thay thế một lời gọi hàm bằng một bảng tra cứu nếu hàm chỉ có một số lượng giới hạn các đầu vào có thể.

Hãy lấy hàm giai thừa số nguyên (n!) làm ví dụ. Các đầu vào duy nhất được phép là các số nguyên từ 0 đến 12. Đầu vào cao hơn sẽ gây ra tràn bộ nhớ (overflow) và đầu vào âm sẽ cho ra vô cực (infinity). Một triển khai điển hình của hàm giai thừa trông như thế này:

```cpp
// Ví dụ 14.1a
int factorial (int n) {          // n!
   int i, f = 1;
   for (i = 2; i <= n; i++) f *= i;
   return f;
}
```

Phép tính này yêu cầu n-1 phép nhân, có thể mất khá nhiều thời gian. Sẽ hiệu quả hơn nếu sử dụng bảng tra cứu:

```cpp
// Ví dụ 14.1b
int factorial (int n) {          // n!
   // Bảng các giai thừa:
   const int FactorialTable[13] = {1, 1, 2, 6, 24, 120, 720,
      5040, 40320, 362880, 3628800, 39916800, 479001600};
   if ((unsigned int)n < 13) {   // Kiểm tra giới hạn (xem trang 137)
      return FactorialTable[n];  // Tra cứu bảng
   }
   else {
      return 0;                  // trả về 0 nếu ngoài phạm vi
   }
}
```

Cách triển khai này sử dụng một bảng tra cứu thay vì tính toán giá trị mỗi khi hàm được gọi. Tôi đã thêm kiểm tra giới hạn trên `n` ở đây bởi vì hậu quả của việc `n` nằm ngoài phạm vi có thể nghiêm trọng hơn khi `n` là một chỉ số mảng (array index) so với khi `n` là một biến đếm vòng lặp. Phương pháp kiểm tra giới hạn được giải thích ở trang 137.

Bảng nên được khai báo là `const` để cho phép lan truyền hằng số (constant propagation) và các tối ưu hóa khác. Bạn có thể khai báo hàm là `inline`.

Việc thay thế một hàm bằng một bảng tra cứu là có lợi trong hầu hết các trường hợp số lượng các đầu vào có thể là giới hạn và không có vấn đề về cache. Không nên sử dụng bảng tra cứu nếu bạn dự đoán bảng sẽ bị đẩy khỏi (evicted from) cache giữa mỗi lần gọi, và thời gian cần thiết để tính toán hàm ít hơn thời gian để tải lại giá trị từ bộ nhớ cộng với chi phí cho các phần khác của chương trình do việc chiếm giữ một dòng cache (cache line).

Tra cứu bảng không thể được vector hóa với tập lệnh hiện tại. Không sử dụng các bảng tra cứu nếu điều này ngăn cản việc viết một mã vector hóa nhanh hơn.

Việc lưu trữ một cái gì đó trong bộ nhớ tĩnh có thể gây ra các vấn đề về cache vì dữ liệu tĩnh có khả năng nằm rải rác ở các địa chỉ bộ nhớ khác nhau. Nếu cache là một vấn đề thì có thể hữu ích khi sao chép bảng từ bộ nhớ tĩnh sang bộ nhớ ngăn xếp (stack memory) ở bên ngoài vòng lặp trong cùng. Việc này được thực hiện bằng cách khai báo bảng bên trong một hàm nhưng bên ngoài vòng lặp trong cùng và không có từ khóa `static`:

```cpp
// Ví dụ 14.1c
void CriticalInnerFunction () {
   // Bảng các giai thừa:
   const int FactorialTable[13] = {1, 1, 2, 6, 24, 120, 720,
      5040, 40320, 362880, 3628800, 39916800, 479001600};
   ...
   int i, a, b;
   // Vòng lặp trong cùng tới hạn (Critical innermost loop):
   for (i = 0; i < 1000; i++) {
      ...
      a = FactorialTable[b];
      ...
   }
}
```

Bảng `FactorialTable` trong ví dụ 14.1c được sao chép từ bộ nhớ tĩnh sang ngăn xếp khi `CriticalInnerFunction` được gọi. Trình biên dịch sẽ lưu trữ bảng trong bộ nhớ tĩnh và chèn một mã để sao chép bảng sang bộ nhớ ngăn xếp ở đầu hàm. Đương nhiên việc sao chép bảng tốn thêm thời gian, nhưng điều này được cho phép khi nó nằm ngoài vòng lặp trong cùng tới hạn. Vòng lặp sẽ sử dụng bản sao của bảng được lưu trong bộ nhớ ngăn xếp, vốn liên kề (contiguous) với các biến cục bộ khác và do đó có khả năng được cache hiệu quả hơn so với bộ nhớ tĩnh.

Nếu bạn không muốn tính toán các giá trị bảng bằng tay và chèn các giá trị vào mã thì bạn có thể tất nhiên là để chương trình thực hiện các tính toán. Thời gian để tính toán bảng là không đáng kể miễn là nó chỉ được thực hiện một lần. Có người có thể tranh luận rằng việc để chương trình tự tính toán bảng sẽ an toàn hơn là gõ các giá trị vào vì lỗi đánh máy trong bảng viết tay có thể không bị phát hiện.

Nguyên lý tra cứu bảng có thể được sử dụng trong bất kỳ tình huống nào mà chương trình chọn giữa hai hoặc nhiều hằng số. Ví dụ, một nhánh chọn giữa hai hằng số có thể được thay thế bằng một bảng có hai mục (entries). Điều này có thể cải thiện hiệu năng nếu nhánh được dự đoán kém (poorly predictable). Ví dụ:

```cpp
// Ví dụ 14.2a
float a;  int b;
a = (b == 0) ? 1.0f : 2.5f;
```

Nếu chúng ta giả định rằng `b` luôn là 0 hoặc 1 và giá trị của nó khó dự đoán, thì sẽ có lợi nếu thay thế nhánh rẽ bằng một việc tra cứu bảng:

```cpp
// Ví dụ 14.2b
float a;  int b;
const float OneOrTwo5[2] = {1.0f, 2.5f};
a = OneOrTwo5[b & 1];
```

Ở đây, tôi đã `AND` `b` với 1 để đảm bảo an toàn. `b & 1` chắc chắn không có giá trị nào khác ngoài 0 hoặc 1 (xem trang 138). Tất nhiên, bước kiểm tra bổ sung này trên `b` có thể được bỏ qua, nếu giá trị của `b` được đảm bảo là 0 hoặc 1. Viết `a = OneOrTwo5[b!=0];` cũng sẽ hoạt động, mặc dù kém hiệu quả hơn một chút. Tuy nhiên, phương pháp này không hiệu quả khi `b` là một số thực kiểu float hoặc double vì tất cả các trình biên dịch mà tôi đã thử nghiệm đều triển khai `OneOrTwo5[b!=0]` dưới dạng `OneOrTwo5[(b!=0) ? 1 : 0]` trong trường hợp này, vì vậy chúng ta không loại bỏ được nhánh rẽ. Có vẻ như thiếu logic khi trình biên dịch sử dụng cách triển khai khác nếu `b` là dấu phẩy động (floating point). Lý do, theo tôi đoán, là các nhà sản xuất trình biên dịch cho rằng phép so sánh dấu phẩy động dễ dự đoán hơn so với so sánh số nguyên. Giải pháp `a = 1.0f + b * 1.5f;` có hiệu quả khi `b` là một kiểu float, nhưng không nếu `b` là số nguyên vì việc chuyển đổi số nguyên sang float mất nhiều thời gian hơn việc tra cứu bảng.

Các bảng tra cứu đặc biệt có lợi ích khi được sử dụng làm phương án thay thế cho các câu lệnh `switch` vì các câu lệnh `switch` thường gặp vấn đề về dự đoán nhánh kém. Ví dụ:

```cpp
// Ví dụ 14.3a
int n;
switch (n) {
case 0:
   printf("Alpha");  break;
case 1:
   printf("Beta");   break;
case 2:
   printf("Gamma");  break;
case 3:
   printf("Delta");  break;
}
```

Điều này có thể được cải thiện bằng cách sử dụng một bảng tra cứu:

```cpp
// Ví dụ 14.3b
int n;
char const * const Greek[4] = {
   "Alpha", "Beta", "Gamma", "Delta"
};
if ((unsigned int)n < 4) { // Kiểm tra để đảm bảo chỉ số không nằm ngoài giới hạn
   printf(Greek[n]);
}
```

Phần khai báo của bảng có từ khóa `const` hai lần vì cả con trỏ và các văn bản mà chúng trỏ tới đều là hằng số.

## 14.2 Kiểm tra giới hạn (Bounds checking)

Trong C++, thường cần phải kiểm tra xem một chỉ số mảng có nằm ngoài giới hạn hay không. Cách làm này thường trông như thế này:

```cpp
// Ví dụ 14.4a
const int size = 16; int i;
float list[size];
...
if (i < 0 || i >= size) {
   cout << "Error: Index out of range";
}
else {
   list[i] += 1.0f;
}
```

Hai phép so sánh `i < 0` và `i >= size` có thể được thay thế bằng một phép so sánh duy nhất:

```cpp
// Ví dụ 14.4b
if ((unsigned int)i >= (unsigned int)size) {
   cout << "Error: Index out of range";
}
else {
   list[i] += 1.0f;
}
```

Giá trị âm có thể có của `i` sẽ xuất hiện như một số dương lớn khi `i` được hiểu là một số nguyên không dấu (unsigned integer) và điều này sẽ kích hoạt điều kiện lỗi. Thay thế hai phép so sánh bằng một làm cho mã nhanh hơn vì việc kiểm tra một điều kiện tương đối tốn kém, trong khi chuyển đổi kiểu (type conversion) hoàn toàn không sinh ra thêm mã lệnh.

Phương pháp này có thể được mở rộng cho trường hợp tổng quát mà bạn muốn kiểm tra xem một số nguyên có nằm trong một khoảng nhất định hay không:

```cpp
// Ví dụ 14.5a
const int min = 100, max = 110;  int i;
...
if (i >= min && i <= max) { ...
```

có thể được đổi thành:

```cpp
// Ví dụ 14.5b
if ((unsigned int)(i - min) <= (unsigned int)(max - min)) { ...
```

Có một cách thậm chí còn nhanh hơn để giới hạn phạm vi của một số nguyên nếu độ dài của khoảng mong muốn là một lũy thừa của 2. Ví dụ:

```cpp
// Ví dụ 14.6
float list[16]; int i;
...
list[i & 15] += 1.0f;
```

Điều này cần một chút giải thích. Giá trị của `i&15` được đảm bảo nằm trong khoảng từ 0 đến 15. Nếu `i` nằm ngoài khoảng này, ví dụ `i = 18`, thì toán tử `&` (bitwise and) sẽ cắt bớt giá trị nhị phân của `i` thành bốn bit, và kết quả sẽ là 2. Kết quả tương tự như `i` modulo 16. Phương pháp này hữu ích để ngăn ngừa lỗi chương trình trong trường hợp chỉ số mảng nằm ngoài phạm vi và chúng ta không cần thông báo lỗi nếu có. Điều quan trọng cần lưu ý là phương pháp này chỉ áp dụng đối với các lũy thừa của 2 (nghĩa là 2, 4, 8, 16, 32, 64,...). Chúng ta có thể chắc chắn rằng một giá trị nhỏ hơn $2^n$ và không âm bằng cách `AND` nó với $2^n - 1$. Phép toán bitwise AND cô lập $n$ bit ít quan trọng nhất (least significant bits) của số và đặt tất cả các bit khác thành zero.

## 14.3 Sử dụng toán tử bitwise để kiểm tra nhiều giá trị cùng lúc

Các toán tử bitwise `&`, `|`, `^`, `~`, `<<`, `>>` có thể kiểm tra hoặc thao tác tất cả các bit của một số nguyên trong một thao tác duy nhất. Ví dụ, nếu mỗi bit của một số nguyên 32 bit có một ý nghĩa cụ thể, thì bạn có thể đặt (set) nhiều bit trong một thao tác duy nhất bằng cách sử dụng toán tử `|`; bạn có thể xóa hoặc làm ẩn (mask out) nhiều bit bằng toán tử `&`; và bạn có thể bật/tắt (toggle) nhiều bit bằng toán tử `^`.

Toán tử `&` cũng hữu ích để kiểm tra nhiều điều kiện trong một phép toán duy nhất. Ví dụ:

```cpp
// Ví dụ 14.7a. Kiểm tra nhiều điều kiện
enum Weekdays {
   Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
};
Weekdays Day;
if (Day == Tuesday || Day == Wednesday || Day == Friday) {
   DoThisThreeTimesAWeek();
}
```

Câu lệnh `if` trong ví dụ này có ba điều kiện được thực hiện thành ba nhánh (branches). Chúng có thể được kết hợp thành một nhánh duy nhất nếu các hằng số Sunday, Monday, v.v. được định nghĩa dưới dạng các lũy thừa của 2:

```cpp
// Ví dụ 14.7b. Kiểm tra nhiều điều kiện bằng toán tử &
enum Weekdays {
   Sunday = 1, Monday = 2, Tuesday = 4, Wednesday = 8,
   Thursday = 0x10, Friday = 0x20, Saturday = 0x40
};
Weekdays Day;
if (Day & (Tuesday | Wednesday | Friday)) {
   DoThisThreeTimesAWeek();
}
```

Bằng cách cung cấp cho mỗi hằng số một giá trị là lũy thừa của 2 trong ví dụ 14.7b, thực tế chúng ta đang sử dụng mỗi bit trong `Day` để biểu thị một trong những ngày trong tuần. Số hằng số lớn nhất mà chúng ta có thể xác định theo cách này bằng với số bit trong một số nguyên, thường là 32. Trong các hệ thống 64 bit, chúng ta có thể sử dụng các số nguyên 64 bit với việc suy giảm hiệu năng là không đáng kể.

Biểu thức `(Tuesday | Wednesday | Friday)` trong ví dụ 14.7b được trình biên dịch chuyển thành giá trị `0x2C` để điều kiện `if` có thể được tính toán bằng một thao tác `&` duy nhất, và như vậy là rất nhanh. Kết quả của phép toán `&` sẽ khác 0 và do đó được tính là `true`, nếu bất kỳ bit nào trong các bit của `Tuesday`, `Wednesday` hoặc `Friday` được bật (set) trong biến `Day`.

Lưu ý sự khác biệt giữa các toán tử logic (Boolean operators) `&&`, `||`, `!` và các toán tử bitwise tương ứng `&`, `|`, `~`. Các toán tử logic tạo ra một kết quả duy nhất là `true` (1) hoặc `false` (0); và toán hạng thứ hai chỉ được ước lượng khi cần thiết. Các toán tử bitwise tạo ra 32 kết quả khi được áp dụng cho các số nguyên 32 bit và chúng luôn ước lượng cả hai toán hạng. Tuy nhiên, các toán tử bitwise được tính toán nhanh hơn nhiều so với các toán tử logic vì chúng không sử dụng nhánh (branches), với điều kiện là các toán hạng là các biểu thức số nguyên chứ không phải biểu thức logic.

Có rất nhiều thứ bạn có thể làm với các toán tử bitwise bằng cách sử dụng số nguyên làm vector logic, và các hoạt động này rất nhanh. Điều này có thể hữu ích trong các chương trình có nhiều biểu thức logic. Việc các hằng số được khai báo bằng `enum`, `const`, hoặc `#define` thì cũng không có gì khác biệt đối với hiệu năng.

## 14.4 Nhân số nguyên (Integer multiplication)

Nhân số nguyên mất nhiều thời gian hơn phép cộng và phép trừ (3 - 10 chu kỳ xung nhịp, tùy thuộc vào bộ vi xử lý). Các trình biên dịch tối ưu hóa thường sẽ thay thế phép nhân số nguyên với một hằng số bằng sự kết hợp giữa các phép cộng và phép dịch bit (shift operations). Phép nhân với một lũy thừa của 2 nhanh hơn phép nhân với các hằng số khác vì nó có thể được thực hiện bằng một phép dịch. Ví dụ, `a * 16` được tính bằng `a << 4`, và `a * 17` được tính bằng `(a << 4) + a`.

Bạn có thể tận dụng lợi thế này bằng cách ưu tiên sử dụng các lũy thừa của 2 khi nhân với một hằng số. Các trình biên dịch cũng có những cách nhanh chóng để nhân với 3, 5 và 9.

Các phép nhân được thực hiện ẩn ngầm khi tính toán địa chỉ của một phần tử trong mảng. Trong một số trường hợp, phép nhân này sẽ nhanh hơn khi hệ số nhân là lũy thừa của 2. Ví dụ:

```cpp
// Ví dụ 14.8
const int rows = 10, columns = 8;
float matrix[rows][columns];
int i, j;
int order(int x);
...
for (i = 0; i < rows; i++) {
   j = order(i);
   matrix[j][0] = i;
}
```

Ở đây, địa chỉ của `matrix[j][0]` được tính toán ngầm (internally) là:
`(int)&matrix[0][0] + j * (columns * sizeof(float))`.
Lúc này, hệ số để nhân với `j` là `(columns * sizeof(float)) = 8 * 4 = 32`. Đây là một lũy thừa của 2, vì vậy trình biên dịch có thể thay thế `j * 32` bằng `j << 5`. Nếu `columns` không phải là một lũy thừa của 2 thì phép nhân sẽ tốn nhiều thời gian hơn. Vì vậy, việc đặt số lượng cột trong ma trận thành lũy thừa của 2 có thể mang lại lợi ích nếu các hàng được truy xuất theo một thứ tự không tuần tự.

Điều tương tự cũng áp dụng cho một mảng các phần tử của một cấu trúc (structure) hoặc lớp (class). Kích thước của mỗi đối tượng nên là một lũy thừa của 2 nếu các đối tượng được truy xuất theo một thứ tự không tuần tự. Ví dụ:

```cpp
// Ví dụ 14.9
struct S1 {
   int a;
   int b;
   int c;
   int UnusedFiller;
};
int order(int x);
const int size = 100;
S1 list[size];  int i, j;
...
for (i = 0; i < size; i++) {
   j = order(i);
   list[j].a = list[j].b + list[j].c;
}
```

Ở đây, chúng ta đã chèn `UnusedFiller` vào trong structure để đảm bảo kích thước của nó là lũy thừa của 2 nhằm làm cho việc tính toán địa chỉ nhanh hơn.

Ưu điểm của việc sử dụng lũy thừa của 2 chỉ áp dụng khi các phần tử được truy xuất theo thứ tự không tuần tự. Nếu đoạn mã trong ví dụ 14.8 và 14.9 được thay đổi sao cho chỉ số là `i` thay vì `j` thì trình biên dịch có thể thấy rằng các địa chỉ được truy xuất theo thứ tự tuần tự và nó có thể tính toán mỗi địa chỉ bằng cách cộng thêm một hằng số vào địa chỉ trước đó (xem trang 72). Trong trường hợp này thì việc kích thước có phải là lũy thừa của 2 hay không không thành vấn đề.

Lời khuyên về việc sử dụng lũy thừa của 2 không áp dụng cho các cấu trúc dữ liệu rất lớn. Ngược lại, bạn nên bằng mọi cách tránh sử dụng các lũy thừa của 2 nếu một ma trận quá lớn đến mức bộ nhớ cache trở thành một vấn đề. Nếu số lượng cột trong một ma trận là một lũy thừa của 2 và ma trận đó lớn hơn bộ nhớ cache thì bạn có thể gặp phải những cạnh tranh nội dung cache rất tốn kém (expensive cache contentions), như đã giải thích ở trang 98.
