Các triển khai phổ biến nhất của con trỏ thông minh là `auto_ptr` và `shared_ptr`.

`auto_ptr` có một đặc điểm là luôn luôn có một và chỉ một `auto_ptr` sở hữu đối tượng được cấp phát, và quyền sở hữu (ownership) được chuyển từ `auto_ptr` này sang một `auto_ptr` khác thông qua phép gán (assignment). `shared_ptr` cho phép nhiều con trỏ trỏ đến cùng một đối tượng.

Không có thêm chi phí nào khi truy cập một đối tượng thông qua con trỏ thông minh. Việc truy cập một đối tượng bằng `*p` hoặc `p->member` đều nhanh như nhau bất kể `p` là một con trỏ thông thường hay một con trỏ thông minh. Nhưng sẽ có thêm một khoản chi phí bổ sung mỗi khi một con trỏ thông minh được tạo ra, bị xóa, sao chép hoặc chuyển giao từ hàm này sang hàm khác. Các khoản chi phí này lớn hơn đối với `shared_ptr` so với `auto_ptr`.

Con trỏ thông minh có thể hữu ích trong tình huống cấu trúc logic của một chương trình yêu cầu một đối tượng phải được tạo động bởi một hàm và sau đó bị xóa bởi một hàm khác và hai hàm này không liên quan đến nhau (không phải là thành viên của cùng một lớp). Nếu cùng một hàm hoặc cùng một lớp chịu trách nhiệm cả tạo và xóa đối tượng thì bạn không cần sử dụng con trỏ thông minh.

Nếu một chương trình sử dụng nhiều đối tượng được cấp phát động nhỏ và mỗi đối tượng đều có con trỏ thông minh riêng thì bạn có thể cần xem xét liệu chi phí của giải pháp này có quá cao hay không. Sẽ hiệu quả hơn nếu gộp chung (pool) tất cả các đối tượng lại với nhau vào một container duy nhất, tốt nhất là với vùng nhớ liên tục (contiguous memory). Xem phần thảo luận về các lớp container ở trang 94.

## 7.10 Mảng (Arrays)

Một mảng (array) được triển khai một cách đơn giản bằng cách lưu trữ các phần tử liên tiếp nhau trong bộ nhớ. Không có thông tin nào về các chiều (dimensions) của mảng được lưu trữ. Điều này làm cho việc sử dụng mảng trong C và C++ nhanh hơn so với các ngôn ngữ lập trình khác, nhưng cũng kém an toàn hơn. Vấn đề an toàn này có thể được khắc phục bằng cách định nghĩa một lớp container cư xử giống như một mảng có kiểm tra ranh giới (bounds checking), như minh họa trong ví dụ này:

```cpp
// Example 7.15a. Array with bounds checking 
template <typename T, unsigned int N> class SafeArray { 
protected: 
   T a[N];                      // Array with N elements of type T 
public: 
   SafeArray() {                // Constructor 
      memset(a, 0, sizeof(a));  // Initialize to zero 
   } 
   int Size() {                 // Return the size of the array 
      return N; 
   } 
   T & operator[] (unsigned int i) { // Safe [] array index operator 
      if (i >= N) { 
         // Index out of range. The next line provokes an error. 
         // You may insert any other error reporting here: 
         return *(T*)0;   // Return a null reference to provoke error 
      } 
      // No error 
      return a[i];     // Return reference to a[i] 
   } 
}; 
```

Bạn có thể xem thêm các ví dụ khác về các lớp container tại www.agner.org/optimize/cppexamples.zip.

Một mảng sử dụng lớp khuôn mẫu (template class) ở trên được khai báo bằng cách chỉ định kiểu dữ liệu và kích thước làm các tham số khuôn mẫu (template parameters), như trong ví dụ 7.15b dưới đây. Nó được truy cập bằng chỉ số nằm trong dấu ngoặc vuông (square brackets), giống hệt như một mảng thông thường. Hàm tạo (constructor) thiết lập tất cả các phần tử về 0. Bạn có thể loại bỏ dòng `memset` nếu bạn không muốn khởi tạo này, hoặc nếu kiểu `T` là một lớp có constructor mặc định thực hiện việc khởi tạo cần thiết. Trình biên dịch có thể cảnh báo rằng `memset` không được khuyến nghị sử dụng (deprecated). Điều này là do nó có thể gây ra lỗi nếu tham số kích thước bị sai, nhưng nó vẫn là cách nhanh nhất để đặt một mảng về 0. Toán tử `[]` sẽ phát hiện lỗi nếu chỉ số (index) nằm ngoài ranh giới (xem trang 137 về kiểm tra ranh giới - bounds checking). Một thông báo lỗi được gây ra ở đây theo một cách khá độc đáo bằng cách trả về một tham chiếu null (null reference). Điều này sẽ gây ra thông báo lỗi trong hệ điều hành được bảo vệ nếu một phần tử mảng được truy cập, và lỗi này rất dễ theo dõi bằng trình gỡ lỗi (debugger). Bạn có thể thay thế dòng này bằng bất kỳ hình thức báo lỗi nào khác. Ví dụ, trong Windows, bạn có thể viết `FatalAppExitA(0,"Array index out of range");` hoặc tốt hơn là tạo hàm báo lỗi của riêng bạn.

Ví dụ sau đây minh họa cách sử dụng `SafeArray`:

```cpp
// Example 7.15b 
SafeArray <float, 100> list;            // Make array of 100 floats 
for (int i = 0; i < list.Size(); i++) { // Loop through array 
   cout << list[i] << endl;             // Output array element 
} 
```

Một mảng được khởi tạo bằng danh sách tốt nhất nên là tĩnh (static), như đã được giải thích ở trang 27. Một mảng có thể được khởi tạo về 0 bằng cách sử dụng `memset`:

```cpp
// Example 7.16 
float list[100]; 
memset(list, 0, sizeof(list)); 
```

Một mảng đa chiều (multidimensional array) nên được tổ chức sao cho chỉ số cuối cùng thay đổi nhanh nhất:

```cpp
// Example 7.17 
const int rows = 20, columns = 50; 
float matrix[rows][columns]; 
int i, j;  float x; 
   for (i = 0; i < rows; i++) 
      for (j = 0; j < columns; j++) 
         matrix[i][j] += x; 
```

Điều này đảm bảo rằng các phần tử được truy cập một cách tuần tự. Việc đảo ngược trật tự của hai vòng lặp sẽ khiến việc truy cập trở nên không tuần tự, làm cho quá trình data caching kém hiệu quả hơn.

Kích thước của tất cả các chiều (ngoại trừ chiều đầu tiên) tốt nhất nên là lũy thừa của 2 nếu các hàng được lập chỉ mục theo một thứ tự không tuần tự nhằm giúp cho việc tính toán địa chỉ hiệu quả hơn:

```cpp
// Example 7.18 
int FuncRow(int);  int FuncCol(int); 
const int rows = 20, columns = 32; 
float matrix[rows][columns]; 
int i;  float x; 
for (i = 0; i < 100; i++) 
   matrix[FuncRow(i)][FuncCol(i)] += x; 
```

Ở đây, mã lệnh phải tính toán `(FuncRow(i)*columns + FuncCol(i)) * sizeof(float)` để tìm địa chỉ của phần tử ma trận. Việc nhân với `columns` trong trường hợp này sẽ nhanh hơn khi `columns` là một lũy thừa của 2. Trong ví dụ trước, điều này không phải là vấn đề bởi vì một trình biên dịch tối ưu hóa có thể thấy rằng các hàng được truy cập liên tiếp và có thể tự tính toán địa chỉ của mỗi hàng bằng cách cộng thêm chiều dài của một hàng vào địa chỉ của hàng trước đó.

Lời khuyên tương tự cũng áp dụng cho các mảng chứa các đối tượng struct hoặc class. Kích thước (tính bằng bytes) của các đối tượng tốt nhất nên là lũy thừa của 2 nếu các phần tử được truy cập theo một trật tự không tuần tự.

Lời khuyên biến số lượng cột thành một lũy thừa của 2 không phải lúc nào cũng áp dụng cho các mảng lớn hơn bộ đệm dữ liệu level-1 (level-1 data cache) và bị truy cập không tuần tự vì nó có thể gây ra tranh chấp bộ đệm (cache contentions). Xem trang 88 để biết thảo luận về vấn đề này.

## 7.11 Chuyển đổi kiểu (Type conversions)

Cú pháp C++ có một vài cách khác nhau để thực hiện chuyển đổi kiểu dữ liệu (type conversions):

```cpp
// Example 7.19 
int i;  float f; 
f = i;                      // Implicit type conversion 
f = (float)i;               // C-style type casting 
f = float(i);               // Constructor-style type casting 
f = static_cast<float>(i);  // C++ casting operator 
```

Tất cả các phương pháp này đều có cùng một tác dụng giống hệt nhau. Bạn sử dụng phương pháp nào chỉ đơn giản là vấn đề của phong cách lập trình. Mức độ tiêu thụ thời gian của các loại chuyển đổi kiểu dữ liệu khác nhau được thảo luận dưới đây.

**Chuyển đổi giữa số có dấu / không dấu (Signed / unsigned conversion)**

```cpp
// Example 7.20 
int i; 
if ((unsigned int)i < 10) { ... 
```

Việc chuyển đổi giữa số nguyên có dấu (signed integers) và không dấu (unsigned integers) đơn giản chỉ là việc khiến trình biên dịch diễn giải các bit của số nguyên theo một cách khác. Không có bất kỳ sự kiểm tra tràn số nào, và mã lệnh không tốn thêm bất kỳ thời gian nào. Các chuyển đổi này có thể được sử dụng thoải mái mà không ảnh hưởng gì tới hiệu suất.

**Chuyển đổi kích thước số nguyên (Integer size conversion)**

```cpp
// Example 7.21 
int i;  short int s; 
i = s; 
```

Một số nguyên được chuyển đổi sang kích thước lớn hơn bằng cách mở rộng sign-bit (bit dấu) nếu nó là số nguyên có dấu, hoặc mở rộng bằng các zero-bits (bit không) nếu nó là số không dấu. Quá trình này thường tốn một chu kỳ xung nhịp nếu nguồn là một biểu thức toán học. Trong nhiều trường hợp, việc chuyển đổi kích thước không làm mất thêm bất kỳ thời gian nào nếu nó được thực hiện cùng lúc với việc đọc giá trị từ một biến trong bộ nhớ, giống như ở ví dụ 7.22.

```cpp
// Example 7.22 
short int a[100];  int i, sum = 0; 
for (i=0; i<100; i++) sum += a[i]; 
```

Chuyển đổi một số nguyên xuống kích thước nhỏ hơn đơn giản được thực hiện bằng cách bỏ qua các bit cao hơn. Không có kiểm tra tràn số (overflow). Ví dụ:

```cpp
// Example 7.23 
int i;  short int s; 
s = (short int)i; 
```

Chuyển đổi này không mất thêm thời gian. Nó đơn giản chỉ lưu 16 bit thấp hơn của số nguyên 32-bit.

**Chuyển đổi độ chính xác của dấu phẩy động (Floating point precision conversion)**

Việc chuyển đổi giữa `float`, `double` và `long double` không mất thêm bất kỳ thời gian nào khi sử dụng các thanh ghi ngăn xếp dấu phẩy động (floating point register stack). Nhưng nó sẽ mất từ 2 đến 15 chu kỳ xung nhịp (tùy thuộc vào vi xử lý) khi sử dụng các thanh ghi XMM. Xem trang 32 để biết giải thích về register stack so với các thanh ghi XMM. Ví dụ:

```cpp
// Example 7.24 
float a; double b; 
a += b; 
```

Trong ví dụ này, việc chuyển đổi sẽ khá đắt đỏ nếu sử dụng thanh ghi XMM. `a` và `b` nên có cùng kiểu để tránh điều này. Xem trang 143 để thảo luận thêm.

**Chuyển đổi số nguyên sang dấu phẩy động (Integer to float conversion)**

Chuyển đổi từ số nguyên có dấu sang một biến `float` hoặc `double` sẽ tốn khoảng 4 - 16 chu kỳ xung nhịp, tùy thuộc vào vi xử lý và loại thanh ghi được sử dụng. Chuyển đổi một số nguyên không dấu sẽ mất nhiều thời gian hơn. Vì thế, việc đầu tiên cần làm là chuyển đổi số nguyên không dấu đó sang một số nguyên có dấu nếu không có rủi ro tràn số (overflow):

```cpp
// Example 7.25 
unsigned int u;  double d; 
d = (double)(signed int)u;  // Faster, but risk of overflow 
```

Trong một số trường hợp, chúng ta có thể tránh được việc chuyển đổi số nguyên sang dấu phẩy động bằng cách sử dụng luôn một biến dấu phẩy động thay thế cho biến số nguyên. Ví dụ:

```cpp
// Example 7.26a 
float a[100];  int i; 
for (i = 0;  i < 100;  i++) a[i] = 2 * i; 
```

Việc chuyển đổi `i` sang `float` trong ví dụ này có thể được ngăn chặn bằng cách tạo thêm một biến dấu phẩy động:

```cpp
// Example 7.26b 
float a[100];  int i;  float i2; 
for (i = 0, i2 = 0;  i < 100;  i++, i2 += 2.0f) a[i] = i2; 
```

**Chuyển đổi dấu phẩy động sang số nguyên (Float to integer conversion)**

Chuyển đổi từ số dấu phẩy động sang số nguyên sẽ tốn rất nhiều thời gian nếu tập lệnh SSE2 hoặc mới hơn không được kích hoạt. Thông thường, quá trình chuyển đổi mất từ 50 - 100 chu kỳ xung nhịp. Nguyên nhân là do tiêu chuẩn C/C++ quy định việc cắt bớt phần thập phân (truncation) nên chế độ làm tròn dấu phẩy động (floating point rounding mode) phải được chuyển thành truncation rồi sau đó chuyển trở lại.

Nếu có các phép chuyển đổi từ dấu phẩy động sang số nguyên trong phần trọng yếu (critical part) của mã lệnh thì việc tìm giải pháp xử lý là rất quan trọng. Các giải pháp có thể là:

*   Tránh các chuyển đổi bằng cách sử dụng các kiểu biến khác nhau.
*   Chuyển các chuyển đổi ra ngoài vòng lặp trong cùng (innermost loop) bằng cách lưu trữ các kết quả trung gian dưới dạng dấu phẩy động.
*   Sử dụng chế độ 64-bit hoặc kích hoạt tập lệnh SSE2 (yêu cầu bộ vi xử lý hỗ trợ).
*   Sử dụng chế độ làm tròn thay vì cắt bớt phần thập phân và tạo một hàm làm tròn bằng ngôn ngữ hợp ngữ (assembly language). Xem trang 144 để biết thông tin chi tiết về làm tròn số.

**Chuyển đổi kiểu con trỏ (Pointer type conversion)**

Một con trỏ có thể được chuyển đổi sang một con trỏ có kiểu khác. Tương tự, một con trỏ có thể được chuyển đổi thành một số nguyên, hoặc một số nguyên có thể được chuyển đổi thành con trỏ. Điều quan trọng là số nguyên phải có đủ số bit để giữ con trỏ.

Những chuyển đổi này không tạo ra thêm bất kỳ đoạn mã lệnh nào. Đó chỉ đơn thuần là việc diễn giải lại các bit theo cách khác hoặc bỏ qua các kiểm tra cú pháp (syntax checks).

Tất nhiên, các chuyển đổi này không an toàn. Trách nhiệm của lập trình viên là đảm bảo rằng kết quả hợp lệ.

**Diễn giải lại kiểu của một đối tượng (Re-interpreting the type of an object)**

Chúng ta có thể làm cho trình biên dịch coi một biến hoặc một đối tượng như thể nó có một kiểu dữ liệu khác bằng cách ép kiểu (type-casting) địa chỉ của nó:

```cpp
// Example 7.27 
float x; 
*(int*)&x |= 0x80000000;   // Set sign bit of x 
```

Cú pháp ở đây có vẻ hơi lạ lẫm. Địa chỉ của `x` được ép kiểu thành một con trỏ tới số nguyên, và sau đó con trỏ này được trích xuất (de-referenced) để có thể truy cập `x` như một số nguyên. Trình biên dịch không sinh thêm đoạn mã nào để tạo con trỏ cả. Con trỏ đó đơn giản bị tối ưu hóa đi và kết quả là `x` được xử lý như một số nguyên. Tuy nhiên, toán tử `&` buộc trình biên dịch lưu `x` trong bộ nhớ thay vì trong thanh ghi. Ví dụ trên thiết lập sign bit của `x` bằng cách sử dụng toán tử `|` mà nếu ở trường hợp bình thường, nó chỉ có thể áp dụng cho các số nguyên. Cách làm này nhanh hơn so với viết `x = -abs(x);`.

Có một số mối nguy hiểm cần lưu ý khi ép kiểu cho con trỏ:

*   Thủ thuật này vi phạm nguyên tắc 'strict aliasing rule' của C chuẩn (standard C), một quy tắc cho rằng hai con trỏ thuộc các kiểu khác nhau không thể trỏ tới cùng một đối tượng (ngoại trừ với con trỏ `char`). Một trình biên dịch tối ưu hóa có thể lưu trữ các dạng biểu diễn của dấu phẩy động và số nguyên vào hai thanh ghi khác nhau. Bạn cần kiểm tra xem trình biên dịch có đang làm đúng như những gì bạn muốn hay không. Nó sẽ an toàn hơn nếu sử dụng một union, như ở ví dụ 14.23 trang 146.
*   Thủ thuật sẽ thất bại nếu đối tượng được coi là lớn hơn so với thực tế. Đoạn mã trên sẽ gặp lỗi nếu một biến `int` dùng nhiều bit hơn một biến `float`. (Cả hai đều dùng 32 bit trên các hệ thống x86).
*   Nếu bạn truy cập vào một phần của một biến, chẳng hạn như 32 bit của một biến `double` 64 bit, thì đoạn mã sẽ không có tính di động (portable) tới các nền tảng sử dụng big endian storage (lưu trữ theo định dạng big endian).
*   Nếu bạn truy cập một phần của một biến, ví dụ nếu bạn ghi vào một biến `double` 64 bit với mỗi lần ghi 32 bit, thì đoạn mã đó có thể sẽ thực thi chậm hơn dự định do xuất hiện store forwarding delay (độ trễ khi chuyển tiếp) trong CPU (Xem tài liệu 3: "The microarchitecture of Intel, AMD and VIA CPUs").

**Const cast**

Toán tử `const_cast` được dùng để loại bỏ thuộc tính rào cản `const` của con trỏ. Nó thực hiện một vài kiểm tra cú pháp và do đó nó an toàn hơn phương thức type-casting theo kiểu C (không sinh ra thêm mã lệnh). Ví dụ:

```cpp
// Example 7.28 
class c1 { 
   const int x;       // constant data 
   public: 
   c1() : x(0) {};    // constructor initializes x to 0 
   void xplus2() {    // this function can modify x 
      *const_cast<int*>(&x) += 2;}  // add 2 to x 
}; 
```

Tác dụng của toán tử `const_cast` ở đây là gỡ bỏ rào cản `const` trên `x`. Đây là một cách để giải phóng giới hạn cú pháp, nhưng nó không tạo ra thêm bất kỳ đoạn mã lệnh nào cũng như không tốn thêm thời gian. Đây là một cách hiệu quả để đảm bảo rằng chỉ có một số hàm cụ thể mới được thay đổi `x`, trong khi các hàm khác thì không.

**Static cast**

Toán tử `static_cast` thực hiện công việc tương tự type-casting theo kiểu C. Ví dụ, nó được dùng để đổi `float` thành `int`.

**Reinterpret cast**

Toán tử `reinterpret_cast` được dùng cho việc chuyển đổi con trỏ. Nó hoạt động giống type-casting theo kiểu C với nhiều hơn đôi chút kiểm tra cú pháp. Nó không sinh thêm đoạn mã lệnh nào.

**Dynamic cast**

Toán tử `dynamic_cast` được sử dụng để chuyển đổi một con trỏ tới lớp này thành con trỏ tới một lớp khác. Nó thực hiện kiểm tra tại thời điểm chạy (runtime check) xem phép chuyển đổi đó có hợp lệ hay không. Chẳng hạn, khi chuyển một con trỏ tới một lớp cơ sở (base class) thành con trỏ tới một lớp dẫn xuất (derived class), nó sẽ kiểm tra xem con trỏ gốc có thực sự đang trỏ tới một đối tượng của lớp dẫn xuất hay không. Việc kiểm tra này làm cho `dynamic_cast` mất nhiều thời gian hơn so với một type casting đơn giản, nhưng bù lại thì nó an toàn hơn. Nó có khả năng bắt được những lỗi lập trình mà nếu không thì rất khó bị phát hiện.

**Chuyển đổi đối tượng của lớp (Converting class objects)**

Chuyển đổi giữa các đối tượng của các lớp (không phải là con trỏ tới đối tượng) chỉ có thể thực hiện nếu lập trình viên đã định nghĩa một constructor, một toán tử gán (assignment operator) được nạp chồng (overloaded), hoặc một toán tử ép kiểu (type casting operator) nạp chồng, những thứ chỉ định cụ thể cách thức chuyển đổi. Constructor hay toán tử nạp chồng cũng có tính hiệu quả tương đương như một hàm thành viên (member function).

## 7.12 Rẽ nhánh và câu lệnh Switch (Branches and switch statements)

Tốc độ cao của các bộ vi xử lý hiện đại đạt được là nhờ việc sử dụng pipeline (đường ống) nơi mà các lệnh được tìm nạp (fetched) và giải mã (decoded) trong nhiều chu kỳ trước khi chúng thực sự được thực thi. Tuy nhiên, cấu trúc pipeline có một vấn đề lớn. Bất cứ khi nào mã lệnh có một cấu trúc rẽ nhánh (ví dụ như cấu trúc if-else), vi xử lý không thể biết trước cần nạp nhánh nào trong số hai nhánh đó vào pipeline. Nếu nạp sai nhánh vào pipeline, thì sai lầm này sẽ không bị phát hiện cho tới tận 10 - 20 chu kỳ xung nhịp sau đó và toàn bộ lượng công việc (tìm nạp, giải mã, hoặc có lẽ là thực thi mang tính dự đoán) trong lúc đó bị coi là lãng phí. Hậu quả là vi xử lý bị mất vài chu kỳ xung nhịp mỗi lần nó nạp lệnh cho một nhánh vào pipeline và sau đó phát hiện ra rằng nó đã chọn nhầm nhánh.

Các nhà thiết kế bộ vi xử lý đã dành rất nhiều thời gian để giảm thiểu vấn đề này. Phương pháp quan trọng nhất được sử dụng là dự đoán nhánh (branch prediction). Các bộ vi xử lý hiện đại đang sử dụng những thuật toán tiên tiến nhằm dự đoán hướng rẽ của một nhánh dựa trên lịch sử quá khứ của nhánh đó và các nhánh xung quanh. Thuật toán dự đoán nhánh trên mỗi loại bộ vi xử lý là khác nhau. Các thuật toán này được mô tả chi tiết trong tài liệu 3: "The microarchitecture of Intel, AMD and VIA CPUs".

Một câu lệnh nhánh (branch instruction) thường mất khoảng 0 - 2 chu kỳ xung nhịp trong trường hợp vi xử lý đưa ra được dự đoán đúng. Khoảng thời gian để khôi phục sau một dự đoán sai (misprediction) là xấp xỉ 12 - 25 chu kỳ xung nhịp, tùy thuộc vào bộ xử lý. Nó được gọi là hình phạt cho việc dự đoán sai nhánh (branch misprediction penalty).

Các nhánh tương đối rẻ nếu chúng hầu hết được dự đoán đúng, nhưng lại rất đắt đỏ nếu thường xuyên bị dự đoán sai. Rõ ràng, một nhánh luôn rẽ theo một hướng duy nhất thì chắc chắn được dự đoán rất tốt. Một nhánh hầu hết rẽ một hướng và hiếm khi đi hướng còn lại thì chỉ bị dự đoán sai khi nó đi hướng còn lại đó. Một nhánh rẽ theo hướng A rất nhiều lần, và rẽ hướng B cũng rất nhiều lần thì chỉ bị dự đoán sai khi nó thay đổi (từ A sang B, hoặc B sang A). Một nhánh tuân theo một khuôn mẫu (pattern) tuần hoàn đơn giản cũng có thể được dự đoán khá tốt nếu nó nằm trong một vòng lặp mà có chứa rất ít (hoặc không có) nhánh khác. Một mô hình vòng lặp đơn giản có thể là: đi theo một hướng hai lần, và hướng còn lại ba lần. Sau đó lại đi hướng kia hai lần, rồi hướng kia ba lần, v.v. Trường hợp xấu nhất xảy ra đối với một nhánh mà nó rẽ một hướng này hoặc hướng kia theo tỷ lệ ngẫu nhiên 50-50. Một nhánh như vậy sẽ có tỷ lệ dự đoán sai là 50%.

Một vòng lặp for hoặc vòng lặp while cũng là một kiểu rẽ nhánh. Sau mỗi vòng lặp, nó lại quyết định xem liệu có cần lặp lại (repeat) hoặc thoát vòng lặp hay không. Nhánh kiểm soát vòng lặp thường được dự đoán rất tốt nếu số lần lặp nhỏ và luôn cố định. Số vòng lặp tối đa có thể dự đoán một cách hoàn hảo biến động trong khoảng từ 9 đến 64, tùy thuộc vào vi xử lý. Các vòng lặp lồng nhau (nested loops) chỉ được dự đoán tốt trên một số vi xử lý. Đối với rất nhiều vi xử lý khác, một vòng lặp chứa nhiều rẽ nhánh thì không được dự đoán tốt.

Câu lệnh switch là một kiểu rẽ nhánh mà nó có thể đi theo nhiều hơn hai hướng. Câu lệnh switch đạt hiệu quả cao nhất nếu các nhãn case (case labels) đi theo một chuỗi (sequence) nơi nhãn này nối tiếp nhãn kia, tăng dần một đơn vị, bởi vì khi đó nó có thể được triển khai như một bảng các mục tiêu nhảy (table of jump targets). Câu lệnh switch có nhiều nhãn với các giá trị cách xa nhau thì không hiệu quả vì trình biên dịch phải chuyển đổi nó thành một cây rẽ nhánh (branch tree).

Trên các vi xử lý đời cũ, một lệnh switch với các nhãn tuần tự được mặc định dự đoán đi theo cùng hướng giống với lần nó thực thi gần nhất. Do đó, chắc chắn nó bị dự đoán sai mỗi khi nó rẽ sang một nhánh khác với lần cuối cùng. Các vi xử lý mới hơn đôi khi có thể dự đoán một lệnh switch nếu nó chạy theo một khuôn mẫu tuần hoàn đơn giản hoặc nếu nó có tương quan với các lệnh rẽ nhánh đi trước và số lượng mục tiêu rẽ nhánh là ít.

Số lượng câu lệnh rẽ nhánh và switch tốt nhất nên được giữ ở mức nhỏ nhất có thể bên trong các phần trọng yếu của mã lệnh, đặc biệt là nếu chúng là các nhánh khó dự đoán. Việc trải phẳng vòng lặp (roll out) có thể hữu ích nếu nó giúp loại bỏ các cấu trúc rẽ nhánh, như được thảo luận trong đoạn tiếp theo.

Mục tiêu (đích đến) của các rẽ nhánh và gọi hàm được lưu trong một vùng đệm (cache) đặc biệt gọi là branch target buffer (BTB). Các xung đột (contentions) trong BTB có thể xảy ra nếu một chương trình có quá nhiều thao tác gọi hàm và rẽ nhánh. Kết quả của những sự tranh chấp này là các rẽ nhánh có thể bị dự đoán sai ngay cả khi về cơ bản thì chúng đã được dự đoán rất tốt. Thậm chí các thao tác gọi hàm cũng có thể bị dự đoán sai vì lý do này. Một chương trình với nhiều thao tác rẽ nhánh và gọi hàm trong các phần quan trọng của mã do đó có thể bị ảnh hưởng nặng nề bởi việc dự đoán sai.

Trong một vài trường hợp, hoàn toàn có khả năng thay thế một cấu trúc rẽ nhánh dự đoán kém (poorly predictable branch) bằng một bảng tra cứu (table lookup). Ví dụ:

```cpp
// Example 7.29a 
float a;  bool b; 
a = b ? 1.5f : 2.6f; 
```

Toán tử `?:` ở đây đóng vai trò như một nhánh rẽ. Nếu nó khó được dự đoán thì hãy thay thế nó bằng một thao tác lookup table:

```cpp
// Example 7.29b 
float a;  bool b = 0; 
const float lookup[2] = {2.6f, 1.5f}; 
a = lookup[b]; 
```

Nếu một `bool` được sử dụng làm một chỉ số mảng thì bắt buộc phải khởi tạo hoặc lấy nó từ một nguồn đáng tin cậy để giá trị của nó không thể khác ngoài 0 hoặc 1. Xem trang 34.

Trong một vài trường hợp, trình biên dịch có thể tự động thay thế một nhánh bằng một thao tác gán có điều kiện (conditional move), tùy thuộc vào tập lệnh được chỉ định (specified instruction set).

Các ví dụ trên trang 137 và 138 chỉ ra những cách khác nhau nhằm làm giảm số lượng cấu trúc nhánh.

Tài liệu 3: "The microarchitecture of Intel, AMD and VIA CPUs" có trình bày nhiều thông tin chi tiết hơn về các cơ chế dự đoán nhánh trên những vi xử lý khác nhau.

## 7.13 Vòng lặp (Loops)

Độ hiệu quả của một vòng lặp phụ thuộc vào cách vi xử lý có thể dự đoán nhánh kiểm soát vòng lặp (loop control branch) tốt như thế nào. Vui lòng xem ở đoạn trước và tài liệu 3: "The microarchitecture of Intel, AMD and VIA CPUs" để biết cách thức hoạt động của cơ chế dự đoán nhánh. Một vòng lặp với số lượng lặp nhỏ, cố định, và không có rẽ nhánh nào bên trong thì có thể được dự đoán rất hoàn hảo. Như đã giải thích ở trên, số vòng lặp tối đa có thể được dự đoán phụ thuộc vào vi xử lý. Các vòng lặp lồng nhau (nested loops) chỉ được dự đoán tốt trên những vi xử lý được tích hợp bộ dự đoán vòng lặp chuyên biệt (loop predictor). Trên các vi xử lý khác, chỉ có vòng lặp trong cùng nhất mới được dự đoán chính xác. Một vòng lặp có repeat count cao (tức lặp nhiều lần) chỉ bị dự đoán sai ở thao tác thoát lặp. Lấy ví dụ, nếu một vòng lặp thực thi 1.000 lần thì nhánh kiểm soát lặp chỉ bị dự đoán sai có 1 lần trong số 1.000, khiến cho penalty (hình phạt do dự đoán sai) là hoàn toàn không đáng kể so với toàn bộ thời gian thực thi.

**Trải phẳng vòng lặp (Loop unrolling)**

Trong một số trường hợp, việc trải phẳng một vòng lặp có thể là một lợi thế. Ví dụ:

```cpp
// Example 7.30a 
int i; 
for (i = 0; i < 20; i++) { 
   if (i % 2 == 0) { 
      FuncA(i); 
   } 
   else { 
      FuncB(i); 
   } 
   FuncC(i); 
} 
```

Vòng lặp này lặp lại 20 lần, xen kẽ giữa việc gọi hàm `FuncA` và `FuncB`, tiếp đó gọi `FuncC`. Trải phẳng vòng lặp (Unrolling the loop) theo bội số 2 ta có:

```cpp
// Example 7.30b 
int i; 
for (i = 0; i < 20; i += 2) { 
   FuncA(i); 
   FuncC(i); 
   FuncB(i+1); 
   FuncC(i+1); 
} 
```

Cách làm này có ba ưu điểm:

*   Nhánh điều khiển lặp `i<20` chỉ cần chạy 10 lần thay vì 20.
*   Việc giảm số đếm (repeat count) từ 20 xuống 10 có nghĩa là vòng lặp này có thể được dự đoán cực kỳ chính xác trên bộ xử lý Pentium 4.
*   Các nhánh lệnh `if` đã bị loại bỏ hoàn toàn.

Trải phẳng vòng lặp cũng có những khuyết điểm:

*   Đoạn mã lặp đã được trải phẳng tiêu thụ nhiều không gian bộ nhớ trong bộ đệm mã (code cache) hoặc micro-op cache.
*   Bộ vi xử lý Core2 hoạt động tốt hơn trên các vòng lặp siêu nhỏ (ít hơn 65 byte mã).
*   Nếu repeat count là số lẻ, và bạn dùng unroll by two (trải phẳng bằng hai), lúc đó sẽ có thêm một vòng lặp dôi ra cần được xử lý ở ngoài luồng. Tựu chung lại, bạn sẽ luôn gặp vấn đề này nếu chưa xác định chính xác liệu repeat count có thể chia hết cho hệ số unroll hay không.

Trải phẳng vòng lặp chỉ nên được sử dụng khi nó mang lại một lợi ích thật sự nổi bật. Nếu một vòng lặp chứa các phép tính liên quan đến dấu phẩy động và có một biến đếm kiểu số nguyên, thì bạn hãy mặc định giả định rằng thời gian tính toán hoàn toàn phụ thuộc vào việc thi hành mã lệnh dấu phẩy động thay vì xử lý các cấu trúc điều khiển vòng lặp. Nghĩa là trong trường hợp đó, bạn chẳng nhận được lợi lộc gì nếu trải phẳng vòng lặp.

Nên tránh việc trải phẳng vòng lặp trên các bộ vi xử lý có bộ đệm mã micro-op cache (như Sandy Bridge), vì bạn sẽ muốn dùng cache một cách tiết kiệm.

Trình biên dịch thông thường sẽ tự động trải phẳng các vòng lặp nếu nó thấy có ích (xem trang 71). Lập trình viên không cần thiết phải trải phẳng các vòng lặp một cách thủ công trừ phi muốn lấy được một lợi thế rõ ràng, chẳng hạn như để triệt tiêu đoạn nhánh `if` ở trong ví dụ 7.30b.

**Điều kiện kiểm soát vòng lặp (The loop control condition)**

Câu lệnh điều khiển vòng lặp có hiệu quả cao nhất chính là bộ đếm số nguyên đơn giản. Một vi xử lý có tính năng out-of-order execution (được giải thích ở trang 105) sẽ có khả năng đánh giá mệnh đề điều khiển của một vòng lặp vài lượt trước.

Vòng lặp sẽ trở nên kém hiệu quả hơn nếu điều kiện rẻ nhánh lại phụ thuộc vào những bước tính toán đang làm bên trong nó. Thử xem ví dụ này: đoạn mã sẽ đổi những ký tự (đã null terminated) thành dạng viết thường (lower case):

```cpp
// Example 7.31a 
char string[100], *p = string; 
while (*p != 0) *(p++) |= 0x20; 
```

Nếu trước đó mà ta đã biết chiều dài chuỗi kí tự, tốt nhất ta nên sử dụng một bộ đếm:

```cpp
// Example 7.31b 
char string[100], *p = string;  int i, StringLength; 
for (i = StringLength; i > 0; i--) *(p++) |= 0x20; 
```

Một kịch bản rất hay thấy đó là, điều kiện kiểm soát vòng lặp phải đợi tính toán bên trong vòng lặp có được kết quả, đặc biệt phổ biến với chuỗi Taylor hay thuật toán Newton-Raphson. Ở đó, các phép tính lặp sẽ chạy tới bao giờ sai số dư (residual error) bé hơn một độ dung sai (tolerance) nhất định mới thôi. Bạn có thể tốn khá nhiều thời gian nhằm so sánh độ dung sai để tìm ra độ chính xác. Một phương pháp hiệu quả hơn là tìm hẳn số lần lặp ở trường hợp tồi tệ nhất (worst-case maximum repeat count) và thi hành toàn bộ đoạn mã đó. Ưu thế ở phương án này là: vi xử lý có thể thực thi sẵn (từ khá sớm) các nhánh trong tương lai và kịp thời xử lý xong mọi lỗi dự đoán phân nhánh, trước khi các lệnh dấu phẩy động trong vòng lặp hiện tại kết thúc. Bạn có thể sử dụng phương pháp này khi mà số lần lặp điển hình rất gần mức lặp tối đa và lúc mà phần tính sai số dư đòi hỏi quá nhiều chi phí (cấu thành nên 1 khoảng thời gian đáng kể trong quy trình).

Biến đếm nên thuộc kiểu dữ liệu số nguyên. Khi vòng lặp buộc phải đếm một cách liên tục trên dấu phẩy động, hãy dùng một bộ đếm integer khác làm bổ trợ. Ví dụ:

```cpp
// Example 7.32a 
double x, n, factorial = 1.0; 
for (x = 2.0; x <= n; x++) factorial *= x; 
```

Có thể sửa đoạn mã bằng việc cho thêm 1 bộ đếm biến đổi hệ số:

```cpp
// Example 7.32b 
double x, n, factorial = 1.0;  int i; 
for (i = (int)n - 2, x = 2.0; i >= 0; i--, x++) factorial *= x; 
```

Xin lưu ý điểm khác biệt về dấu chấm phẩy và dấu phẩy trong việc khai báo biến đi kèm. Vòng lặp for chia ra làm 3 điều kiện: (1) thiết lập ban đầu (initialization), (2) kiểm tra lặp, và (3) toán tử thay đổi tham số biến đếm. 3 bước được giới hạn bởi 2 dấu phẩy. Mọi tính toán ở từng vế (mệnh đề) đều phải xài dấu phẩy. Việc so sánh trong phần kiểm tra lặp (phần điều kiện thứ 2) chỉ cho phép khai báo tối đa một bước kiểm tra (1 step) mà thôi.

Thi thoảng dùng phép so sánh `0` (với 1 số integer) sẽ tối ưu hơn so sánh với các con số khác. Cụ thể ở đây, vòng lặp giảm biến đếm lùi dần xuống số không (zero) tốt hơn tăng biến đếm đụng tới mức N. Trừ phi hệ số kia làm chỉ số mảng (array index). Bộ nhớ đệm tối ưu rất mạnh vào khả năng tìm mảng từ dưới đi lên, thay vì truy ngược trở xuống (backwards).

**Sao chép hoặc xóa mảng (Copying or clearing arrays)**

Một vòng lặp sẽ trở thành gánh nặng nếu thao tác sao chép nguyên cả chuỗi/mảng về dạng bit số không. Lấy ví dụ:

```cpp
// Example 7.33a 
const int size = 1000;  int i; 
float a[size], b[size]; 
// set a to zero 
for (i = 0; i < size; i++) a[i] = 0.0; 
// copy a to b 
for (i = 0; i < size; i++) b[i] = a[i]; 
```

Một cách lẹ hơn nhiều là xài cả bộ hàm tiêu chuẩn `memset` và `memcpy`:

```cpp
// Example 7.33b 
const int size = 1000; 
float a[size], b[size]; 
// set a to zero 
memset(a, 0, sizeof(a)); 
// copy a to b 
memcpy(b, a, sizeof(b)); 
```

Gần như các compiler sẽ chuyển thành API `memset` / `memcpy`, đặc biệt ở những trường hợp đơn thuần. Cần chú ý, `memset` / `memcpy` đều bị quy kết là hàm "nguy hiểm", mọi thứ sẽ đổ bể khi tham số của mảng đích dài hơn số liệu ban đầu. Mà thật ra thì, ngay cả khi xài đoạn for loop thủ công, ta vẫn mắc vào cái bẫy này nếu thiết đặt loop count to bành trướng.

## 7.14 Các hàm (Functions)

Những cuộc gọi hàm (Function calls) có thể kéo lùi tiến độ (tốc độ) bằng những nguyên do dưới đây:

*   Lệnh gọi hàm buộc bộ xử lý nhảy cóc qua phần không gian địa chỉ bộ nhớ chứa phần mã lệnh khác (cách xa địa chỉ cũ) rồi quay về điểm ban đầu. Mất khoảng chừng 4 xung nhịp clock cycle. Rất may vi xử lý có thể giải quyết các bước trả - gọi thông qua sự đan xen (overlap).
*   Không gian cache code xử lý cồng kềnh khi phải liên tục phân tách rải rác từng khúc (scattered) ở nhiều vùng trong memory.
*   Chế độ (Mode) 32-bit đem toàn bộ thông số lên trên Stack, làm trì trệ việc trích xuất nếu chúng mắc kẹt vào các tiến trình dây chuyền phụ thuộc chéo (dependency chains).
*   Mỗi khi gọi hàm thì cần tốn chút thì giờ chuẩn bị Stack frame, tải rồi cất thông số các thanh ghi, cũng như chuẩn bị các bộ nắn/sửa code lỗi.
*   Một dòng lệnh gọi hàm nhồi thêm hàng tá gánh nặng và rủi ro gây tranh chấp (contentions) cho BTB. Cứ càng nhiều function/branch ở nơi nhạy cảm, tỉ lệ gánh chịu quả báo dự đoán rẽ nhánh nhầm (mispredictions) càng lớn.

Các kĩ năng ở đây có thể dùng được để rút bớt khoảng thời gian lãng phí ở phần nhạy cảm khi phát lệnh gọi.

**Tránh các hàm không cần thiết (Avoid unnecessary functions)**

Nhiều loại sách dạy cách cắt nhỏ mã lệnh (function) ra làm nhiều đoạn hàm khác nhau nếu hàm quá dài. Nhưng hãy tránh làm như vậy. Chẳng qua bạn muốn mã có một diện mạo đẹp, mà lại tàn phá hoàn toàn mọi chỉ số tốc độ của nó! Sự cắt sẻ ấy, chừng nào chức năng mang một hàm ý rành rọt / một sự định danh rẽ nhánh lớn (distinct tasks), thì chia cắt hàm chỉ vì hàm "quá to" chẳng cho thấy hiệu quả. Bất cứ bộ rẽ nhánh lặp (innermost loops) trọng tâm nào hãy thiết đặt nó ngay giữa không gian hàm đó, không gọi.

**Sử dụng hàm inline (Use inline functions)**

Hàm Inline cũng giống như biến thể của "Macro", nghĩa là toàn bộ nơi gọi hàm được thế chỗ bằng phần thịt (body) của mã đó. Thông thường chức năng trên xuất hiện nếu có thuộc tính `inline` ở bên hay nếu nguyên cả đoạn body lọt vô một Class definition (trong tệp class đó). Rất tuyệt vời khi các loại mã có nội dung ngắn/chỉnh hoặc chỉ có một lượt thực thi/gọi lệnh duy nhất (được Inlined thủ công hoặc trình biên dịch lo tự động Inlined cho). Trình biên dịch có quyền tước đoạt việc Inline (làm lơ yêu cầu của bạn) khi phải cân não với nhiều nguy cơ từ góc nhìn kĩ thuật hoặc do lỗi tính hiệu năng (performance).

**Tránh các cuộc gọi hàm lồng nhau trong vòng lặp trong cùng (Avoid nested function calls in the innermost loop)**

Cấu trúc (Hàm) bao bọc một vài cấu trúc nhỏ, gọi là frame function; ngược lại cấu trúc (hàm) đơn côi chỉ chứa code cơ bản, không đá động thêm một cấu trúc nhỏ nào, gọi là leaf function. Vì những kẽ hở sẽ lộ ra tại trang 63, leaf function tốt hơn hẳn frame function. Một cụm innermost loop quan trọng bị cài nhắm chứa các mã cấu trúc frame functions cần được tối ưu thành: đem inline trực tiếp vô trong luôn, biến phần frame structure thành kiểu leaf functions thuần tủy - đem tất cả thông tin trong thân ruột các lệnh chức năng nội bộ, xả tung (inline) thẳng thừng.

**Sử dụng Macro thay cho các hàm (Use macros instead of functions)**

Các lệnh gọi bằng `#define` luôn luôn Inlined, thế nhưng có nguy hiểm rằng chúng tự động thi hành mọi tham số ngay khi bị viện dẫn đến. Ví dụ:

```cpp
// Example 7.34a. Use macro as inline function 
#define MAX(a,b) (a > b ? a : b) 
y = MAX(f(x), g(x)); 
```

`f(x)` hoặc `g(x)` phải chịu sự thi hành 2 lần vì cấu trúc này tính kết quả trước rồi mới làm lệnh so sánh điều kiện ở bước 2!

Có thể sử dụng một hàm inline thay vì tạo Marco. Khi bạn tìm một loại mã đa dạng với mọi thông số/ kiểu dữ liệu (type of parameters), vui lòng thiết lập các templates thay vì tạo Macros:

```cpp
// Example 7.34b. Replace macro by template 
template <typename T> 
static inline T max(T const & a, T const & b) { 
   return a > b ? a : b; 
} 
```

Vấn nạn tiếp theo của `#define` là chức năng ẩn định/bao hàm sẽ vô vọng: Macro tự dưng nhẩy bổ và vùi giập 1 hàm/biến đang xài có chung danh xưng (cái tên), bất chấp các không gian rào cản namespace/scope. Vậy là hãy sử dụng nhiều chữ, tránh sử dụng kiểu đại trà cho Macros tại phần tệp tiêu đề (Header files).

**Sử dụng hàm fastcall (Use fastcall functions)**

Tính năng của từ khóa `__fastcall` ở môi trường 32-bit buộc hệ điều hành tải (thông số parameter) thông qua bộ Register thay vì gán chúng trên vùng Stack (với 2 parameter thuộc integer đầu, hoặc 3 đối với CodeGear compiler). Hiệu năng đạt tốc độ khá tốt trên các dạng thông số nguyên số (integer parameter).

Còn khi đụng chuyện với floating point, các đối số trên sẽ không nhúc nhích dù có bật chức năng `__fastcall`. Lệnh trỏ `this` - implicit 'this' pointer - cho các chức năng ở hàm Member cũng chỉ xài duy nhất 1 khe tải (register). Vì thế, khi nào dùng `__fastcall` thì nên nhớ điều quan trọng là đưa ngay thông số parameter kiểu integer ở mục ưu tiên số một. Mọi chuyện sẽ bay lên trời, khi thiết đặt môi trường 64-bit; chế độ mặc định của bộ thông số đều là Registers (kéo theo `__fastcall` vô hiệu).

**Biến các hàm thành cục bộ (Make functions local)**

Bất cứ mã lệnh chức năng nào ở một tập tin (module) - vd .cpp file - cũng nên được giữ cục bộ, để trình Compiler nắm thóp (Inline the function) tối ưu lệnh tốt hơn thông qua các thủ tục rẽ nhánh. Đây là ba giải pháp cho Local:

1.  Từ khóa (keyword) `static` trước cái tên: Phương pháp này hiệu năng (giản đơn), thế nhưng vô hiệu khi xử lí cấu trúc Class member, (vì lúc bấy giờ `static` mang nội dung khác hẳn).
2.  Lập cho đoạn function hoặc Class một không gian vô danh (anonymous namespace).
3.  GNU Compiler chấp thuận giải pháp: `__attribute__((visibility("hidden")))`.

**Sử dụng tính năng tối ưu hóa toàn cục toàn chương trình (Use whole program optimization)**

Một vài bộ biên dịch Compiler tung ra khả năng "Whole program optimization", đóng nén hàng loạt các nhánh/module .cpp lại chung một cục object file. Tính năng này giải phóng bộ Compiler được quyền cấp số (bơm bộ parameter tải tới register) trên mọi không gian liên kết .cpp đang định hình sản phẩm. Tính năng Whole program optimization không dùng chung cho function library (phát tán ở file objects hay tệp thư viện libraries).

**Sử dụng chế độ 64-bit (Use 64-bit mode)**

Sức tải ở một bộ parameter vận hành mượt mà 64-bit tốt hơn môi trường 32-bit. 64-bit Linux cũng ăn đứt 64-bit Windows. Nhóm thông số parameter của Linux trên nền 64-bit tận dụng không gian: 6 integer (tham số số nguyên), và 8 luồng floating (tám tham số dấu phẩy động) trọn vẹn đưa qua thanh tải Register. Vị chi bằng mười bốn (14) parameter tất thảy. 64-bit của Windows cũng chỉ nhường tối đa không quá 4 chỗ parameter để đẩy bộ load cho các Registers, dù là Integer hay Dấu phẩy động (float numbers). Vậy ta kết luận là Linux nhanh hơn ở phần parameter có quy mô từ 4 tham số.

## 7.15 Tham số hàm (Function parameters)

Trong hầu hết các trường hợp, các tham số hàm được truyền theo giá trị (transferred by value). Có nghĩa là giá trị của thông số sẽ được sao chép tới vùng/biến cục bộ của hàm (local variable). Điều này hiệu quả cho các loại type sơ cấp/nhỏ, như: `int`, `float`, `double`, `bool`, `enum`, hay qua con trỏ và tham chiếu (pointers/references).

Mảng (Array) mặc định qua rào chuyển tải luôn bằng phương thức pointer, nếu nó không bị nhúng / trùm vô cái structure hoặc class.

Thật nhức đầu nếu parameter rơi vô thể loại ghép (composite type): Structure và Class. Sẽ an toàn/ hiệu năng và hoàn hảo nhất cho parameter thuộc dạng composite khi thoả mãn những gạch đầu dòng sau:

*   Độ bành trướng đối tượng thuộc loại "nhí" (kích thước tí hon, nằm lọt trong không gian duy nhất 1 Register).
*   Tuyệt đối vắng bóng cấu trúc (copy constructor/destructor).
*   Đối tượng nói "không" với hàm ảo (Virtual members).
*   Chống dùng RTTI (Runtime type identification) trong ruột đối tượng này.

Sẽ là giải pháp hợp lí/ thông suốt/ lợi về thời gian nếu bạn trỏ con trỏ (pointer/reference) qua parameter, một khi các mục kể trên dở dang - không đạt bất kì 1 yêu cầu nào. Gánh cái vật (object lớn cồng kềnh) đi loanh quanh sẽ chiếm cả núi thời gian, khi copy nguyên khối cái structure đó. Copy Constructor bắt đầu công việc lúc mảng Parameter nhận được bản ngã phó bản, cùng với hàm Destructor thi hành xóa lệnh lúc function chuẩn bị trả bước trở ra.

Lời khuyên tuyệt vời của các phương pháp đẩy tham số qua - với composite object - là dùng tham chiếu hằng (const reference). Từ khóa "const" bảo đảm không có một cú phá hoại bóp nghẹt nguyên bản Object nào xảy ra (bởi ai / hàm khác). Nó dễ thở với compiler (Inline nhanh) so với loại con trỏ hay Non-const references; const references mở đường (tạo lối thoáng cho tham số chức năng lấy "biểu thức" / mảng ẩn danh (anonymous object)). Compiler xử đẹp, dọn gánh dễ hơn với Const.

Cũng rất tiện (và không mất sức) để cho cả đoạn parameter chức năng thuộc sở hữu (Member) của lớp/structure gốc rễ. Tốc độ cao không kém!

Các môi trường 32-bit sẽ đẩy các (Simple function parameter) vô trong Stack (hố). Thế nhưng qua 64-bit, thanh tải (Registers) đã lo liệu cả. Và đương nhiên 64-bit vượt trội hẳn. Hệ thống Windows 64-bit ngậm không quá bốn bộ thông số tải parameter truyền vô Register, trong khi Unix 64-bit chịu một lúc nhai được tận 14 Parameter (8 float hay double, kèm thêm 6 nhóm cho integer, hoặc pointer/reference types). Tham số kiểu "Pointer trỏ This - The this pointer" được tính coi như bằng một thông số (one parameter) thông thường cho hàm member. Khám phá rõ ngọn ngành xem thêm mục 5: "Calling conventions for different C++ compilers and operating systems".

## 7.16 Kiểu trả về của hàm (Function return types)

Return function (Kiểu hàm xuất kết quả/trả giá trị) yêu cầu kiểu Type sơ đẳng nhất, là `void`, tham chiếu hay bộ Pointer, còn loại Composite/Objects thì đứt mạch, khá chậm chạp.
