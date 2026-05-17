# 7 Tính hiệu quả của các cấu trúc C++ khác nhau (The efficiency of different C++ constructs)

*(Tiếp theo)* Vì hầu hết các phương pháp phát triển đều có bản chất tăng dần (incremental) hoặc lặp đi lặp lại (iterative), điều quan trọng là phải có một chiến lược để lưu bản sao lưu (backup) của từng phiên bản trung gian. Đối với các dự án chỉ có một người, việc tạo một tệp zip của từng phiên bản là đủ. Đối với các dự án nhóm, bạn nên sử dụng một công cụ kiểm soát phiên bản (version control tool).

## 7 Tính hiệu quả của các cấu trúc C++ khác nhau (The efficiency of different C++ constructs)

Hầu hết các lập trình viên đều có rất ít hoặc không có ý niệm về việc một đoạn mã chương trình được dịch thành mã máy (machine code) như thế nào và bộ vi xử lý xử lý mã này ra sao. Ví dụ, nhiều lập trình viên không biết rằng các phép tính với độ chính xác kép (double precision) cũng nhanh như độ chính xác đơn (single precision). Và ai có thể biết rằng một lớp khuôn mẫu (template class) lại hiệu quả hơn một lớp đa hình (polymorphous class)?

Chương này nhằm giải thích tính hiệu quả tương đối của các phần tử ngôn ngữ C++ khác nhau nhằm giúp lập trình viên lựa chọn phương án hiệu quả nhất. Nền tảng lý thuyết được giải thích thêm trong các tập khác của bộ tài liệu này.

## 7.1 Các loại lưu trữ biến khác nhau (Different kinds of variable storage)

Các biến (variables) và đối tượng (objects) được lưu trữ trong các phần khác nhau của bộ nhớ, tùy thuộc vào cách chúng được khai báo trong chương trình C++. Điều này có ảnh hưởng đến tính hiệu quả của bộ đệm dữ liệu (data cache) (xem trang 88). Data caching sẽ kém hiệu quả nếu dữ liệu nằm rải rác ngẫu nhiên trong bộ nhớ. Do đó, điều quan trọng là phải hiểu các biến được lưu trữ như thế nào. Các nguyên tắc lưu trữ là giống nhau đối với các biến đơn giản, mảng và đối tượng.

**Lưu trữ trên ngăn xếp (Storage on the stack)**

Các biến và đối tượng được khai báo bên trong một hàm được lưu trữ trên ngăn xếp (stack), ngoại trừ các trường hợp được mô tả trong các phần dưới đây.

Ngăn xếp là một phần của bộ nhớ được tổ chức theo kiểu vào-trước-ra-sau (first-in-last-out). Nó được sử dụng để lưu trữ các địa chỉ trả về của hàm (tức là nơi hàm được gọi), các tham số của hàm, các biến cục bộ và để lưu các thanh ghi (registers) phải được khôi phục trước khi hàm trả về. Mỗi khi một hàm được gọi, nó phân bổ một lượng không gian cần thiết trên ngăn xếp cho tất cả các mục đích này. Không gian bộ nhớ này được giải phóng khi hàm trả về. Lần tiếp theo khi một hàm được gọi, nó có thể sử dụng cùng một không gian đó cho các tham số của hàm mới.

Ngăn xếp là không gian bộ nhớ hiệu quả nhất để lưu trữ dữ liệu vì cùng một dải địa chỉ bộ nhớ được sử dụng đi sử dụng lại. Nếu không có các mảng lớn, thì gần như chắc chắn rằng phần bộ nhớ này được sao chép trong bộ đệm dữ liệu cấp 1 (level-1 data cache), nơi nó được truy cập khá nhanh.

Bài học chúng ta có thể rút ra từ điều này là tất cả các biến và đối tượng tốt nhất nên được khai báo bên trong hàm mà chúng được sử dụng.

Có thể làm cho phạm vi của một biến thậm chí còn nhỏ hơn bằng cách khai báo nó bên trong các dấu ngoặc nhọn `{}`. Tuy nhiên, hầu hết các trình biên dịch không giải phóng bộ nhớ mà một biến sử dụng cho đến khi hàm trả về mặc dù nó có thể giải phóng bộ nhớ khi thoát khỏi các dấu ngoặc nhọn `{}` nơi biến được khai báo. Nếu biến được lưu trữ trong một thanh ghi (xem bên dưới) thì nó có thể được giải phóng trước khi hàm trả về.

**Lưu trữ toàn cục hoặc tĩnh (Global or static storage)**

Các biến được khai báo bên ngoài bất kỳ hàm nào được gọi là các biến toàn cục (global variables). Chúng có thể được truy cập từ bất kỳ hàm nào. Các biến toàn cục được lưu trữ trong một phần tĩnh của bộ nhớ (static memory). Bộ nhớ tĩnh cũng được sử dụng cho các biến được khai báo bằng từ khóa `static`, cho các hằng số dấu phẩy động, hằng số chuỗi, danh sách khởi tạo mảng (array initializer lists), bảng nhảy của câu lệnh `switch` (switch statement jump tables) và bảng hàm ảo (virtual function tables).

Vùng dữ liệu tĩnh thường được chia thành ba phần: một phần dành cho các hằng số không bao giờ bị sửa đổi bởi chương trình, một phần dành cho các biến đã được khởi tạo có thể bị sửa đổi bởi chương trình, và một phần dành cho các biến chưa được khởi tạo có thể bị sửa đổi bởi chương trình.

Ưu điểm của dữ liệu tĩnh là nó có thể được khởi tạo về các giá trị mong muốn trước khi chương trình bắt đầu. Nhược điểm là không gian bộ nhớ bị chiếm dụng trong suốt quá trình thực thi chương trình, ngay cả khi biến chỉ được sử dụng trong một phần nhỏ của chương trình. Điều này làm cho việc caching dữ liệu kém hiệu quả hơn.

Đừng biến các biến thành toàn cục nếu bạn có thể tránh được nó. Biến toàn cục có thể cần thiết để giao tiếp giữa các luồng (threads) khác nhau, nhưng đó gần như là tình huống duy nhất mà chúng không thể tránh khỏi. Có thể hữu ích khi biến một biến thành toàn cục nếu nó được truy cập bởi một vài hàm khác nhau và bạn muốn tránh overhead (chi phí phụ) của việc truyền biến như một tham số hàm. Nhưng một giải pháp tốt hơn có thể là làm cho các hàm truy cập biến đó trở thành thành viên (members) của cùng một lớp (class) và lưu trữ biến dùng chung đó bên trong lớp. Giải pháp nào bạn thích hơn là một vấn đề về phong cách lập trình.

Thường thì tốt hơn là tạo một bảng tra cứu (lookup-table) tĩnh. Ví dụ:

```cpp
// Example 7.1 
float SomeFunction (int x) { 
   static float list[] = {1.1, 0.3, -2.0, 4.4, 2.5}; 
   return list[x]; 
} 
```

Ưu điểm của việc sử dụng `static` ở đây là danh sách không cần phải được khởi tạo khi hàm được gọi. Các giá trị đơn giản là được đặt vào đó khi chương trình được tải vào bộ nhớ. Nếu từ `static` bị xóa khỏi ví dụ trên, thì cả năm giá trị phải được đưa vào danh sách mỗi lần hàm được gọi. Điều này được thực hiện bằng cách sao chép toàn bộ danh sách từ bộ nhớ tĩnh sang bộ nhớ ngăn xếp. Việc sao chép dữ liệu hằng số từ bộ nhớ tĩnh sang ngăn xếp là một sự lãng phí thời gian trong hầu hết các trường hợp, nhưng nó có thể là tối ưu trong những trường hợp đặc biệt khi dữ liệu được sử dụng nhiều lần trong một vòng lặp nơi gần như toàn bộ cache cấp 1 được sử dụng cho một số mảng mà bạn muốn giữ cùng nhau trên ngăn xếp.

Các hằng số chuỗi và hằng số dấu phẩy động được lưu trữ trong bộ nhớ tĩnh trong mã được tối ưu hóa. Ví dụ:

```cpp
// Example 7.2 
a = b * 3.5; 
c = d + 3.5; 
```

Tại đây, hằng số `3.5` sẽ được lưu trữ trong bộ nhớ tĩnh. Hầu hết các trình biên dịch sẽ nhận ra rằng hai hằng số này giống hệt nhau nên chỉ cần lưu trữ một hằng số. Tất cả các hằng số giống hệt nhau trong toàn bộ chương trình sẽ được nối lại với nhau để giảm thiểu lượng không gian cache được sử dụng cho các hằng số.

Hằng số nguyên thường được bao gồm như là một phần của mã lệnh (instruction code). Bạn có thể giả định rằng không có vấn đề caching nào đối với hằng số nguyên.

**Lưu trữ trên thanh ghi (Register storage)**

Một số lượng hạn chế các biến có thể được lưu trữ trong các thanh ghi (registers) thay vì bộ nhớ chính (main memory). Một thanh ghi là một mảnh bộ nhớ nhỏ bên trong CPU được sử dụng để lưu trữ tạm thời. Các biến được lưu trữ trong thanh ghi được truy cập rất nhanh. Tất cả các trình biên dịch tối ưu hóa sẽ tự động chọn các biến được sử dụng thường xuyên nhất trong một hàm để lưu trữ trên thanh ghi. Cùng một thanh ghi có thể được sử dụng cho nhiều biến miễn là phạm vi sống (live ranges) của chúng không trùng lặp.

Số lượng các thanh ghi là rất hạn chế. Có khoảng sáu thanh ghi số nguyên có sẵn cho các mục đích chung (general purposes) trong hệ điều hành 32-bit và mười bốn thanh ghi số nguyên trong hệ thống 64-bit.

Các biến dấu phẩy động sử dụng một loại thanh ghi khác. Có tám thanh ghi dấu phẩy động có sẵn trong hệ điều hành 32-bit và mười sáu trong hệ điều hành 64-bit. Một số trình biên dịch gặp khó khăn trong việc tạo các biến thanh ghi dấu phẩy động trong chế độ 32-bit trừ khi tập lệnh SSE2 (hoặc cao hơn) được kích hoạt.

**Từ khóa Volatile**

Từ khóa `volatile` chỉ định rằng một biến có thể bị thay đổi bởi một luồng (thread) khác. Điều này ngăn trình biên dịch thực hiện các tối ưu hóa dựa trên giả định rằng biến luôn có giá trị mà nó được gán trước đó trong mã. Ví dụ:

```cpp
// Example 7.3. Explain volatile 
volatile int seconds;  // incremented every second by another thread 
 
void DelayFiveSeconds() { 
   seconds = 0; 
   while (seconds < 5) { 
      // do nothing while seconds count to 5 
   } 
} 
```

Trong ví dụ này, hàm `DelayFiveSeconds` sẽ chờ cho đến khi `seconds` được tăng lên 5 bởi một luồng khác. Nếu `seconds` không được khai báo là `volatile` thì một trình biên dịch tối ưu hóa sẽ giả định rằng `seconds` vẫn bằng không trong vòng lặp `while` vì không có gì bên trong vòng lặp có thể thay đổi giá trị đó. Vòng lặp sẽ là `while (0 < 5) {}`, tức là một vòng lặp vô hạn.

Tác dụng của từ khóa `volatile` là nó đảm bảo biến được lưu trữ trong bộ nhớ thay vì trong thanh ghi và ngăn chặn mọi tối ưu hóa trên biến. Điều này có thể hữu ích trong các tình huống thử nghiệm (test situations) để tránh việc một số biểu thức bị trình biên dịch loại bỏ đi.

Lưu ý rằng `volatile` không có nghĩa là nguyên tử (atomic). Nó không ngăn hai luồng cố gắng ghi vào biến tại cùng một thời điểm. Mã trong ví dụ trên có thể bị lỗi trong trường hợp nó cố gắng đặt `seconds` về không cùng lúc với luồng kia tăng giá trị của `seconds`. Một cách triển khai an toàn hơn sẽ chỉ đọc giá trị của `seconds` và chờ cho đến khi giá trị thay đổi năm lần.

**Lưu trữ cục bộ cho luồng (Thread-local storage)**

Hầu hết các trình biên dịch có thể thực hiện lưu trữ cục bộ trên luồng (thread-local storage) đối với các biến tĩnh và toàn cục bằng cách sử dụng từ khóa `__thread` hoặc `__declspec(thread)`. Các biến như vậy có một phiên bản (instance) cho mỗi luồng. Lưu trữ thread-local không hiệu quả vì nó được truy cập thông qua một con trỏ được lưu trữ trong khối môi trường luồng (thread environment block). Nên tránh sử dụng lưu trữ thread-local, nếu có thể, và thay thế bằng lưu trữ trên ngăn xếp (xem bên trên, trang 26). Các biến được lưu trữ trên ngăn xếp luôn thuộc về luồng mà chúng được tạo ra.

**Từ khóa Far**

Các hệ thống có bộ nhớ phân đoạn (segmented memory), chẳng hạn như DOS và Windows 16-bit, cho phép lưu trữ các biến trong một phân đoạn dữ liệu xa (far data segment) bằng cách sử dụng từ khóa `far` (mảng cũng có thể là `huge`). Lưu trữ far, con trỏ far, và thủ tục far không hiệu quả. Nếu một chương trình có quá nhiều dữ liệu cho một phân đoạn thì nên sử dụng hệ điều hành khác cho phép các phân đoạn lớn hơn (hệ thống 32-bit hoặc 64-bit).

**Cấp phát bộ nhớ động (Dynamic memory allocation)**

Cấp phát bộ nhớ động được thực hiện với các toán tử `new` và `delete` hoặc với các hàm `malloc` và `free`. Các toán tử và hàm này tiêu thụ một lượng thời gian đáng kể. Một phần bộ nhớ được gọi là heap được dành riêng cho cấp phát động. Heap có thể dễ dàng bị phân mảnh (fragmented) khi các đối tượng có kích thước khác nhau được cấp phát và giải phóng theo thứ tự ngẫu nhiên. Trình quản lý heap (heap manager) có thể dành nhiều thời gian để dọn dẹp các không gian không còn được sử dụng và tìm kiếm các không gian trống. Quá trình này được gọi là thu gom rác (garbage collection). Các đối tượng được phân bổ tuần tự không nhất thiết phải được lưu trữ liên tiếp trong bộ nhớ. Chúng có thể nằm rải rác ở những nơi khác nhau khi heap đã bị phân mảnh. Điều này làm cho việc caching dữ liệu trở nên kém hiệu quả.

Việc cấp phát bộ nhớ động cũng có xu hướng làm cho mã phức tạp hơn và dễ sinh lỗi hơn. Chương trình phải giữ các con trỏ trỏ tới tất cả các đối tượng đã được phân bổ và theo dõi xem khi nào chúng không còn được sử dụng nữa. Điều quan trọng là tất cả các đối tượng đã được cấp phát cũng phải được giải phóng (deallocated) trong tất cả các trường hợp luồng chương trình (program flow) có thể xảy ra. Việc không làm như vậy là một nguồn lỗi phổ biến được gọi là rò rỉ bộ nhớ (memory leak). Một loại lỗi thậm chí tồi tệ hơn là truy cập vào một đối tượng sau khi nó đã bị giải phóng. Logic chương trình có thể cần thêm các overhead để ngăn chặn các lỗi như vậy.

Xem trang 91 để thảo luận thêm về các ưu điểm và hạn chế của việc sử dụng cấp phát bộ nhớ động.

Một số ngôn ngữ lập trình, chẳng hạn như Java, sử dụng cấp phát bộ nhớ động cho tất cả các đối tượng. Điều này tất nhiên là kém hiệu quả.

**Các biến được khai báo bên trong một lớp (Variables declared inside a class)**

Các biến được khai báo bên trong một lớp (class) được lưu trữ theo thứ tự mà chúng xuất hiện trong khai báo lớp. Loại lưu trữ được xác định tại nơi đối tượng của lớp đó được khai báo. Một đối tượng của lớp, cấu trúc (structure) hoặc liên hiệp (union) có thể sử dụng bất kỳ phương pháp lưu trữ nào được đề cập ở trên. Một đối tượng không thể được lưu trữ trong thanh ghi ngoại trừ những trường hợp đơn giản nhất, nhưng các biến thành viên dữ liệu (data members) của nó có thể được sao chép vào các thanh ghi.

Một biến thành viên của lớp với từ khóa sửa đổi `static` sẽ được lưu trữ trong bộ nhớ tĩnh và sẽ chỉ có một và chỉ một phiên bản (instance). Các thành viên không tĩnh (Non-static members) của cùng một lớp sẽ được lưu trữ cùng với mỗi phiên bản của lớp.

Việc lưu trữ các biến trong một lớp hoặc cấu trúc là một cách tốt để đảm bảo rằng các biến được sử dụng trong cùng một phần của chương trình cũng được lưu trữ gần nhau. Xem trang 52 để biết những ưu và nhược điểm của việc sử dụng các lớp.

## 7.2 Các biến và toán tử số nguyên (Integers variables and operators)

**Kích thước số nguyên (Integer sizes)**

Số nguyên có thể có kích thước khác nhau, và chúng có thể là có dấu (signed) hoặc không dấu (unsigned). Bảng sau tóm tắt các kiểu số nguyên có sẵn khác nhau.

| Khai báo | Kích thước, bit | Giá trị tối thiểu | Giá trị tối đa | trong stdint.h |
|---|---|---|---|---|
| char | 8 | -128 | 127 | int8_t |
| short int <br> (trong hệ thống 16-bit: int) | 16 | -32768 | 32767 | int16_t |
| int <br> (trong hệ thống 16-bit: long int) | 32 | -2³¹ | 2³¹-1 | int32_t |
| long long hoặc int64_t <br> Trình biên dịch MS: \_\_int64 <br> Linux 64-bit: long int | 64 | -2⁶³ | 2⁶³-1 | int64_t |
| unsigned char | 8 | 0 | 255 | uint8_t |
| unsigned short int <br> (trong hệ thống 16-bit: unsigned int) | 16 | 0 | 65535 | uint16_t |
| unsigned int <br> (trong hệ thống 16-bit: unsigned long) | 32 | 0 | 2³²-1 | uint32_t |
| unsigned long long hoặc uint64_t <br> Trình biên dịch MS: unsigned \_\_int64 <br> Linux 64-bit: unsigned long int | 64 | 0 | 2⁶⁴-1 | uint64_t |

*Bảng 7.1. Kích thước của các kiểu số nguyên khác nhau*

Đáng tiếc, cách khai báo một số nguyên với một kích thước cụ thể lại khác nhau đối với các nền tảng khác nhau như được hiển thị trong bảng trên. Nếu tệp tiêu đề tiêu chuẩn (standard header file) `stdint.h` hoặc `inttypes.h` có sẵn thì bạn nên sử dụng nó để có một cách định nghĩa các kiểu số nguyên với kích thước cụ thể có tính di động (portable).

Các phép toán trên số nguyên là nhanh trong hầu hết các trường hợp, bất kể kích thước. Tuy nhiên, sử dụng kích thước số nguyên lớn hơn kích thước thanh ghi khả dụng lớn nhất là không hiệu quả. Nói cách khác, sử dụng số nguyên 32-bit trên các hệ thống 16-bit hoặc số nguyên 64-bit trên các hệ thống 32-bit là không hiệu quả, đặc biệt nếu mã chứa các phép tính nhân hoặc chia.

Trình biên dịch sẽ luôn chọn kích thước số nguyên hiệu quả nhất nếu bạn khai báo một `int`, mà không chỉ định kích thước. Số nguyên có kích thước nhỏ hơn (`char`, `short int`) chỉ kém hiệu quả hơn một chút xíu. Trong nhiều trường hợp, trình biên dịch sẽ chuyển đổi các kiểu này thành số nguyên có kích thước mặc định khi thực hiện các phép tính, rồi sau đó chỉ sử dụng 8 hoặc 16 bit thấp hơn của kết quả. Bạn có thể giả định rằng việc chuyển đổi kiểu dữ liệu mất từ không đến một chu kỳ xung nhịp. Trong các hệ thống 64-bit, chỉ có sự khác biệt rất nhỏ về hiệu suất giữa số nguyên 32-bit và số nguyên 64-bit, miễn là bạn không thực hiện các phép chia.

Bạn nên sử dụng kích thước số nguyên mặc định trong các trường hợp kích thước không quan trọng và không có nguy cơ tràn số (overflow), chẳng hạn như các biến đơn giản, biến đếm vòng lặp, v.v. Trong các mảng lớn, có thể ưu tiên sử dụng kích thước số nguyên nhỏ nhất đủ lớn cho mục đích cụ thể nhằm tận dụng tốt hơn bộ đệm dữ liệu (data cache). Bit-fields (Trường bit) có kích thước khác 8, 16, 32 và 64 bit sẽ kém hiệu quả hơn. Trong các hệ thống 64-bit, bạn có thể sử dụng số nguyên 64-bit nếu ứng dụng có thể tận dụng các bit phụ này.

Kiểu số nguyên không dấu `size_t` có kích thước 32 bit trong các hệ thống 32-bit và 64 bit trong các hệ thống 64-bit. Nó được dùng cho kích thước mảng và chỉ số mảng khi bạn muốn đảm bảo rằng việc tràn số không bao giờ xảy ra, ngay cả đối với các mảng lớn hơn 2 GB.

Khi xem xét liệu một kích thước số nguyên cụ thể có đủ lớn cho một mục đích cụ thể hay không, bạn phải xem xét liệu các tính toán trung gian có thể gây tràn số hay không. Ví dụ, trong biểu thức `a = (b*c)/d`, có thể xảy ra trường hợp `(b*c)` bị tràn, ngay cả khi `a, b, c` và `d` đều ở dưới giá trị tối đa. Không có chức năng kiểm tra tự động đối với lỗi tràn số nguyên.

**Số nguyên có dấu so với số nguyên không dấu (Signed versus unsigned integers)**

Trong hầu hết các trường hợp, không có sự khác biệt về tốc độ giữa việc sử dụng số nguyên có dấu và không dấu. Nhưng có một vài trường hợp điều này có tạo ra sự khác biệt:

* **Chia cho một hằng số:** Không dấu nhanh hơn có dấu khi bạn chia một số nguyên cho một hằng số (xem trang 140). Điều này cũng áp dụng cho toán tử chia lấy dư (modulo) `%`.
* **Chuyển đổi sang số dấu phẩy động** nhanh hơn với số nguyên có dấu so với số nguyên không dấu đối với hầu hết các tập lệnh (xem trang 145).
* **Tràn số (Overflow)** hoạt động khác nhau trên các biến có dấu và không dấu. Một tràn số của một biến không dấu tạo ra một kết quả dương thấp. Một tràn số của một biến có dấu được xác định chính thức là không xác định (undefined). Hành vi thông thường là quay vòng (wrap-around) tràn số dương thành một giá trị âm, nhưng trình biên dịch có thể tối ưu hóa để loại bỏ các nhánh phụ thuộc vào việc tràn số, dựa trên giả định rằng tràn số không xảy ra.

Việc chuyển đổi giữa số nguyên có dấu và không dấu là không tốn kém (costless). Nó đơn giản chỉ là vấn đề diễn giải cùng một dải bit (bits) theo cách khác nhau. Một số nguyên âm sẽ được diễn giải thành một số dương rất lớn khi được chuyển đổi sang dạng không dấu.

```cpp
// Example 7.4. Signed and unsigned integers 
int a, b;  
double c; 
b = (unsigned int)a / 10;    // Convert to unsigned for fast division 
c = a * 2.5;                 // Use signed when converting to double 
```

Trong ví dụ 7.4, chúng ta đang chuyển đổi `a` sang dạng không dấu để thực hiện phép chia nhanh hơn. Tất nhiên, điều này chỉ hoạt động nếu chắc chắn rằng `a` sẽ không bao giờ âm. Dòng cuối cùng ngầm định chuyển đổi `a` sang `double` trước khi nhân với hằng số `2.5` (kiểu `double`). Ở đây chúng ta ưu tiên `a` là kiểu có dấu.

Hãy chắc chắn không kết hợp số nguyên có dấu và không dấu trong các phép so sánh, chẳng hạn như `<`. Kết quả của việc so sánh số nguyên có dấu với số nguyên không dấu không rõ ràng và có thể tạo ra kết quả không mong muốn.

**Các toán tử số nguyên (Integer operators)**

Các phép toán số nguyên nhìn chung là rất nhanh. Các phép toán số nguyên đơn giản như cộng, trừ, so sánh, các phép toán bit (bit operations) và phép dịch chuyển (shift operations) chỉ mất một chu kỳ xung nhịp trên hầu hết các bộ vi xử lý.

Phép nhân và phép chia mất nhiều thời gian hơn. Phép nhân số nguyên mất 11 chu kỳ xung nhịp trên bộ xử lý Pentium 4, và 3 - 4 chu kỳ xung nhịp trên hầu hết các bộ vi xử lý khác. Phép chia số nguyên mất 40 - 80 chu kỳ xung nhịp, tùy thuộc vào bộ vi xử lý. Phép chia số nguyên nhanh hơn khi kích thước số nguyên nhỏ hơn trên các bộ xử lý AMD, nhưng không phải trên các bộ xử lý Intel. Thông tin chi tiết về độ trễ của các lệnh được liệt kê trong tài liệu 4: "Instruction tables". Các mẹo về cách tăng tốc độ phép nhân và phép chia được đưa ra ở trang 139 và 140, tương ứng.

**Toán tử tăng và giảm (Increment and decrement operators)**

Toán tử tăng trước (pre-increment operator) `++i` và toán tử tăng sau (post-increment operator) `i++` đều nhanh như các phép cộng. Khi được sử dụng đơn giản để tăng một biến số nguyên, không có sự khác biệt về việc bạn sử dụng tiền tố tăng hay hậu tố tăng. Hiệu quả đơn giản là hoàn toàn giống nhau. Ví dụ, `for (i=0; i<n; i++)` thì giống như `for (i=0; i<n; ++i)`. Nhưng khi giá trị kết quả của biểu thức được sử dụng, thì có thể có sự khác biệt về hiệu năng. Ví dụ, `x = array[i++]` hiệu quả hơn `x = array[++i]` bởi vì trong trường hợp thứ hai, việc tính toán địa chỉ của phần tử mảng phải đợi giá trị mới của `i`, điều này sẽ làm chậm sự có sẵn của `x` trong khoảng hai chu kỳ xung nhịp. Rõ ràng, giá trị khởi tạo của `i` phải được điều chỉnh nếu bạn chuyển đổi từ tiền tố tăng sang hậu tố tăng.

Cũng có những trường hợp toán tử tăng trước hiệu quả hơn toán tử tăng sau. Ví dụ, trong trường hợp `a = ++b;` trình biên dịch sẽ nhận ra rằng giá trị của `a` và `b` là như nhau sau câu lệnh này do đó nó có thể sử dụng cùng một thanh ghi cho cả hai, trong khi biểu thức `a = b++;` sẽ làm cho giá trị của `a` và `b` khác nhau do đó chúng không thể sử dụng cùng một thanh ghi.

Mọi thứ được nói ở đây về các toán tử tăng cũng áp dụng cho các toán tử giảm trên các biến số nguyên.

## 7.3 Các biến và toán tử dấu phẩy động (Floating point variables and operators)

Các bộ vi xử lý hiện đại trong dòng x86 có hai loại thanh ghi dấu phẩy động khác nhau và tương ứng với đó là hai loại lệnh dấu phẩy động khác nhau. Mỗi loại đều có những ưu điểm và nhược điểm riêng.

Phương pháp nguyên thủy để thực hiện các phép toán dấu phẩy động bao gồm tám thanh ghi dấu phẩy động được tổ chức thành một ngăn xếp thanh ghi (register stack). Các thanh ghi này có độ chính xác kép dài (long double precision, 80 bits). Những lợi thế của việc sử dụng ngăn xếp thanh ghi này là:

* Tất cả các tính toán đều được thực hiện với độ chính xác kép dài.
* Việc chuyển đổi giữa các độ chính xác khác nhau không mất thêm thời gian.
* Có sẵn các tập lệnh nội tại (intrinsic instructions) cho các hàm toán học như logarit và lượng giác.
* Mã lệnh nhỏ gọn và chiếm ít không gian trong bộ nhớ cache mã (code cache).

Tuy nhiên, ngăn xếp thanh ghi cũng có những nhược điểm:

* Rất khó để trình biên dịch tạo các biến thanh ghi do cách thức tổ chức của ngăn xếp thanh ghi.
* So sánh dấu phẩy động chậm trừ khi tập lệnh của Pentium-II hoặc các bộ vi xử lý ra đời sau nó được kích hoạt.
* Việc chuyển đổi giữa số nguyên và số dấu phẩy động là không hiệu quả.
* Phép chia, khai căn bậc hai và các hàm toán học tốn nhiều thời gian tính toán hơn khi sử dụng độ chính xác kép dài.

Một phương pháp mới hơn để thực hiện các phép tính dấu phẩy động bao gồm tám hoặc mười sáu thanh ghi vector (XMM hoặc YMM), có thể được sử dụng cho nhiều mục đích. Các phép toán dấu phẩy động được thực hiện với độ chính xác đơn (single) hoặc kép (double), và các kết quả trung gian luôn được tính toán với độ chính xác tương đương với độ chính xác của các toán hạng (operands). Ưu điểm của việc sử dụng thanh ghi vector là:

* Dễ dàng tạo các biến thanh ghi dấu phẩy động.
* Có sẵn các phép toán vector (Vector operations) để tính toán song song (parallel calculations) trên các vector gồm hai biến độ chính xác kép hoặc bốn biến độ chính xác đơn trong các thanh ghi XMM (xem trang 107). Nếu có tập lệnh AVX thì mỗi vector có thể giữ bốn biến độ chính xác kép hoặc tám biến độ chính xác đơn trong các thanh ghi YMM.

Nhược điểm bao gồm:

* Độ chính xác kép dài (Long double precision) không được hỗ trợ.
* Việc tính toán các biểu thức mà toán hạng có độ chính xác hỗn hợp yêu cầu các lệnh chuyển đổi độ chính xác (precision conversion instructions) vốn có thể khá tốn thời gian (xem trang 143).
* Các hàm toán học phải sử dụng thư viện hàm, nhưng điều này thường nhanh hơn so với các hàm phần cứng nội tại (intrinsic hardware functions).

Các thanh ghi ngăn xếp dấu phẩy động (floating point stack registers) có sẵn trong tất cả các hệ thống có khả năng xử lý dấu phẩy động (ngoại trừ trong các trình điều khiển thiết bị - device drivers - cho Windows 64-bit). Thanh ghi vector XMM có sẵn trong các hệ thống 64-bit và hệ thống 32-bit khi tập lệnh SSE2 hoặc cao hơn được kích hoạt (độ chính xác đơn chỉ cần SSE). Thanh ghi YMM có sẵn nếu tập lệnh AVX được bộ xử lý và hệ điều hành hỗ trợ. Xem trang 125 để biết cách kiểm tra sự khả dụng của các tập lệnh này.

Hầu hết các trình biên dịch sẽ sử dụng thanh ghi XMM cho các tính toán dấu phẩy động bất cứ khi nào chúng có sẵn, tức là trong chế độ 64-bit hoặc khi tập lệnh SSE2 được kích hoạt. Rất ít trình biên dịch có khả năng trộn lẫn (mix) hai loại toán tử dấu phẩy động này và chọn ra loại nào tối ưu cho mỗi phép tính.

Trong hầu hết các trường hợp, phép tính với độ chính xác kép không mất nhiều thời gian hơn độ chính xác đơn. Khi sử dụng các thanh ghi dấu phẩy động, đơn giản là không có sự khác biệt về tốc độ giữa độ chính xác đơn và kép. Độ chính xác kép dài (Long double precision) chỉ mất thời gian nhỉnh hơn một chút. Phép chia độ chính xác đơn, căn bậc hai và các hàm toán học được tính toán nhanh hơn độ chính xác kép khi sử dụng các thanh ghi XMM, trong khi tốc độ của phép cộng, trừ, nhân, v.v., vẫn giống nhau không phụ thuộc vào độ chính xác trên hầu hết các bộ xử lý (khi các phép toán vector không được sử dụng).

Bạn có thể sử dụng độ chính xác kép mà không cần lo lắng quá nhiều về chi phí nếu nó tốt cho ứng dụng. Bạn có thể sử dụng độ chính xác đơn nếu có các mảng lớn và muốn đưa càng nhiều dữ liệu càng tốt vào cache dữ liệu. Độ chính xác đơn tốt nếu bạn có thể tận dụng lợi thế của các phép toán vector, như được giải thích ở trang 107.

Phép cộng dấu phẩy động mất từ 3 - 6 chu kỳ xung nhịp, tùy thuộc vào vi xử lý. Phép nhân mất từ 4 - 8 chu kỳ xung nhịp. Phép chia mất từ 14 - 45 chu kỳ xung nhịp. So sánh dấu phẩy động kém hiệu quả khi sử dụng các thanh ghi ngăn xếp dấu phẩy động. Chuyển đổi từ `float` hoặc `double` sang số nguyên mất một thời gian khá lâu khi sử dụng thanh ghi ngăn xếp dấu phẩy động.

Không trộn lẫn độ chính xác đơn và kép khi sử dụng thanh ghi XMM. Xem trang 143.

Tránh việc chuyển đổi qua lại giữa số nguyên và biến dấu phẩy động, nếu có thể. Xem trang 144.

Các ứng dụng tạo ra dưới tràn dấu phẩy động (floating point underflow) trong các thanh ghi XMM có thể hưởng lợi từ việc thiết lập chế độ "flush-to-zero" thay vì sinh ra các số phi chuẩn (subnormal numbers) trong trường hợp bị dưới tràn (underflow):

```cpp
// Example 7.5. Set flush-to-zero mode (SSE): 
#include <xmmintrin.h> 
_MM_SET_FLUSH_ZERO_MODE(_MM_FLUSH_ZERO_ON); 
```

Bạn rất nên thiết lập chế độ flush-to-zero trừ khi bạn có những lý do đặc biệt để sử dụng số phi chuẩn. Ngoài ra, bạn cũng có thể thiết lập chế độ `denormals-are-zero` nếu có hỗ trợ SSE2:

```cpp
// Example 7.6. Set flush-to-zero and denormals-are-zero mode (SSE2): 
#include <xmmintrin.h> 
_mm_setcsr(_mm_getcsr() | 0x8040); 
```

Xem trang 149 và 122 để biết thêm thông tin về các hàm toán học.

## 7.4 Enums (Kiểu liệt kê)

Một enum về cơ bản chỉ là một số nguyên được ngụy trang. Enums có hiệu quả chính xác như số nguyên.

Lưu ý rằng các phần tử liệt kê (enumerators) sẽ xung đột (clash) với bất kỳ biến hoặc hàm nào có cùng tên. Do đó, enums trong các tệp tiêu đề (header files) nên có tên dài và duy nhất hoặc được đặt trong một namespace.

## 7.5 Booleans (Kiểu Boolean)

**Thứ tự của các toán hạng Boolean (The order of Boolean operands)**

Các toán hạng của các toán tử Boolean `&&` và `||` được đánh giá (evaluated) theo cách sau. Nếu toán hạng đầu tiên của `&&` là false, thì toán hạng thứ hai hoàn toàn không được đánh giá vì kết quả chắc chắn được biết là false bất kể giá trị của toán hạng thứ hai. Tương tự, nếu toán hạng đầu tiên của `||` là true, thì toán hạng thứ hai không được đánh giá, vì kiểu gì kết quả cũng chắc chắn là true.

Sẽ rất có lợi nếu bạn đặt toán hạng có xác suất đúng (true) cao nhất vào vị trí cuối cùng trong biểu thức `&&`, hoặc đặt vào vị trí đầu tiên trong biểu thức `||`. Ví dụ, giả sử rằng `a` đúng trong 50% số trường hợp và `b` đúng trong 10% số trường hợp. Biểu thức `a && b` cần phải đánh giá `b` khi `a` đúng, tức là trong 50% trường hợp. Biểu thức tương đương `b && a` chỉ cần đánh giá `a` khi `b` đúng, tức là chỉ trong 10% thời gian. Nó sẽ nhanh hơn nếu `a` và `b` mất cùng lượng thời gian để đánh giá và có cùng xác suất được dự đoán bởi cơ chế dự đoán nhánh (branch prediction). Xem trang 44 để biết giải thích về cơ chế dự đoán nhánh.

Nếu một toán hạng dễ dự đoán hơn toán hạng kia, thì hãy đặt toán hạng dễ dự đoán nhất lên đầu.

Nếu một toán hạng tính toán nhanh hơn toán hạng kia, thì hãy đặt toán hạng được tính toán nhanh nhất lên đầu.

Tuy nhiên, bạn phải cẩn thận khi đảo ngược (swapping) trật tự của các toán hạng Boolean. Bạn không thể đảo các toán hạng nếu việc đánh giá các toán hạng tạo ra tác dụng phụ (side effects) hoặc nếu toán hạng đầu tiên xác định xem toán hạng thứ hai có hợp lệ hay không. Ví dụ:

```cpp
// Example 7.7 
unsigned int i;  const int ARRAYSIZE = 100;  float list[ARRAYSIZE]; 
if (i < ARRAYSIZE && list[i] > 1.0) { ... 
```

Ở đây, bạn không thể hoán đổi thứ tự của các toán hạng vì biểu thức `list[i]` là không hợp lệ khi `i` không nhỏ hơn `ARRAYSIZE`. Một ví dụ khác:

```cpp
// Example 7.8 
if (handle != INVALID_HANDLE_VALUE && WriteFile(handle, ...)) { ... 
```

Ở đây, bạn cũng không thể đổi chỗ các toán hạng vì bạn không nên gọi hàm `WriteFile` nếu handle không hợp lệ.

**Các biến Boolean bị quá ranh giới định hình (Boolean variables are overdetermined)**

Biến Boolean được lưu trữ như những số nguyên 8-bit với giá trị 0 cho `false` và 1 cho `true`.

Biến Boolean có tính quá định (overdetermined) theo nghĩa là tất cả các toán tử sử dụng biến Boolean làm đầu vào đều kiểm tra xem đầu vào có giá trị nào khác ngoài 0 hoặc 1 hay không, nhưng các toán tử tạo ra Boolean ở đầu ra thì không thể sinh ra giá trị nào khác ngoài 0 hoặc 1. Điều này làm cho các phép toán sử dụng biến Boolean làm đầu vào kém hiệu quả hơn mức cần thiết. Lấy ví dụ:

```cpp
// Example 7.9a 
bool a, b, c, d; 
c = a && b; 
d = a || b; 
```

Trình biên dịch thường triển khai mã này theo cách như sau:

```cpp
bool a, b, c, d; 
if (a != 0) { 
   if (b != 0) { 
      c = 1; 
   } 
   else { 
      goto CFALSE; 
   } 
} 
else { 
   CFALSE: 
   c = 0; 
} 
if (a == 0) { 
   if (b == 0) { 
      d = 0; 
   } 
   else { 
      goto DTRUE; 
   } 
} 
else { 
   DTRUE: 
   d = 1; 
} 
```

Tất nhiên, điều này khác xa so với tối ưu. Các cấu trúc rẽ nhánh (branches) có thể mất nhiều thời gian trong trường hợp dự đoán sai (mispredictions - xem trang 44). Các phép toán Boolean có thể được thực hiện hiệu quả hơn nhiều nếu biết chắc chắn rằng các toán hạng không có giá trị nào khác ngoài 0 và 1. Lý do khiến trình biên dịch không đưa ra giả định như vậy là vì các biến có thể có các giá trị khác nếu chúng chưa được khởi tạo (uninitialized) hoặc đến từ các nguồn không xác định. Mã trên có thể được tối ưu hóa nếu `a` và `b` đã được khởi tạo bằng các giá trị hợp lệ hoặc nếu chúng đến từ các toán tử có đầu ra kiểu Boolean. Đoạn mã được tối ưu hóa trông như sau:

```cpp
// Example 7.9b 
char a = 0, b = 0, c, d; 
c = a & b; 
d = a | b; 
```

Ở đây, tôi đã sử dụng `char` (hoặc `int`) thay vì `bool` để có thể sử dụng các toán tử bit (bitwise operators - `&` và `|`) thay vì các toán tử Boolean (`&&` và `||`). Các toán tử bit là các lệnh đơn chỉ mất một chu kỳ xung nhịp. Toán tử OR (`|`) hoạt động ngay cả khi `a` và `b` có các giá trị khác 0 hoặc 1. Toán tử AND (`&`) và toán tử EXCLUSIVE OR (`^`) có thể trả về các kết quả không nhất quán nếu các toán hạng có các giá trị khác ngoài 0 và 1.

Lưu ý rằng có một vài cạm bẫy ở đây. Bạn không thể sử dụng `~` thay cho `NOT`. Thay vào đó, bạn có thể thực hiện `NOT` một biến Boolean (khi đã biết chắc nó là 0 hoặc 1) bằng cách thực hiện phép XOR nó với 1:

```cpp
// Example 7.10a 
bool a, b; 
b = !a; 
```

có thể được tối ưu hóa thành:

```cpp
// Example 7.10b 
char a = 0, b; 
b = a ^ 1; 
```

Bạn không thể thay thế `a && b` bằng `a & b` nếu `b` là một biểu thức không nên được đánh giá khi `a` là `false`. Tương tự, bạn không thể thay thế `a || b` bằng `a | b` nếu `b` là một biểu thức không nên được đánh giá khi `a` là `true`.

Thủ thuật sử dụng các toán tử bitwise sẽ có lợi hơn nếu các toán hạng là biến so với trường hợp các toán hạng là các biểu thức so sánh, v.v. Ví dụ:

```cpp
// Example 7.11 
bool a; float x, y, z; 
a = x > y && z != 0; 
```

Điều này là tối ưu trong hầu hết các trường hợp. Đừng đổi `&&` thành `&` trừ khi bạn hy vọng biểu thức `&&` tạo ra nhiều lỗi dự đoán nhánh (branch mispredictions).

**Phép toán Boolean dạng Vector (Boolean vector operations)**

Một số nguyên có thể được sử dụng như một vector Boolean. Ví dụ, nếu `a` và `b` là các số nguyên 32-bit, thì biểu thức `y = a & b;` sẽ thực hiện 32 phép AND chỉ trong một chu kỳ xung nhịp. Các toán tử `&`, `|`, `^`, `~` rất hữu ích cho các phép toán vector Boolean.

## 7.6 Con trỏ và tham chiếu (Pointers and references)

**Con trỏ so với tham chiếu (Pointers versus references)**

Con trỏ (pointers) và tham chiếu (references) đều hiệu quả như nhau vì trên thực tế chúng đang thực hiện cùng một công việc. Ví dụ:

```cpp
// Example 7.12 
void FuncA (int * p) { 
   *p = *p + 2; 
} 
 
void FuncB (int & r) { 
   r = r + 2; 
} 
```

Hai hàm này làm cùng một việc và nếu bạn xem đoạn mã do trình biên dịch tạo ra, bạn sẽ nhận thấy rằng đoạn mã này hoàn toàn giống nhau cho cả hai hàm. Sự khác biệt chỉ đơn giản là vấn đề về phong cách lập trình. Những ưu điểm của việc sử dụng con trỏ thay vì tham chiếu là:

* Khi bạn nhìn vào phần thân hàm ở trên, rõ ràng `p` là một con trỏ, nhưng không rõ liệu `r` là tham chiếu hay một biến thông thường. Việc sử dụng con trỏ giúp người đọc hiểu rõ hơn về những gì đang xảy ra.
* Có thể thực hiện các thao tác với con trỏ mà không thể thực hiện với tham chiếu. Bạn có thể thay đổi những gì mà con trỏ chỉ tới và bạn có thể thực hiện các phép toán số học (arithmetic operations) với con trỏ.

Những lợi thế của việc sử dụng tham chiếu thay vì con trỏ là:

* Cú pháp đơn giản hơn khi sử dụng tham chiếu.
* Tham chiếu an toàn hơn so với con trỏ vì trong hầu hết các trường hợp, chúng chắc chắn sẽ trỏ đến một địa chỉ hợp lệ. Con trỏ có thể không hợp lệ và gây ra lỗi nghiêm trọng (fatal errors) nếu chúng không được khởi tạo (uninitialized), nếu các tính toán số học trên con trỏ vượt ra ngoài giới hạn của các địa chỉ hợp lệ, hoặc nếu con trỏ bị ép kiểu (type-casted) sai.
* Tham chiếu hữu ích cho các copy constructors (hàm tạo sao chép) và các toán tử nạp chồng (overloaded operators).
* Tham số hàm được khai báo dưới dạng tham chiếu hằng (constant references) chấp nhận biểu thức làm đối số trong khi con trỏ và tham chiếu không hằng yêu cầu một biến (variable).

**Tính hiệu quả (Efficiency)**

Truy cập một biến hoặc đối tượng thông qua một con trỏ hoặc tham chiếu có thể nhanh như truy cập trực tiếp nó. Nguyên nhân cho tính hiệu quả này nằm ở cách cấu tạo của bộ vi xử lý. Tất cả các biến và đối tượng không tĩnh được khai báo trong hàm đều được lưu trữ trên ngăn xếp (stack) và thực tế được đánh địa chỉ (addressed) tương đối so với con trỏ ngăn xếp (stack pointer). Tương tự, tất cả các biến và đối tượng không tĩnh được khai báo trong một lớp đều được truy cập thông qua một con trỏ ngầm định được biết đến trong C++ là `this`. Do đó, chúng ta có thể kết luận rằng hầu hết các biến trong một chương trình C++ được cấu trúc tốt trên thực tế đều được truy cập thông qua con trỏ bằng cách này hay cách khác. Vì vậy, các vi xử lý phải được thiết kế để làm cho con trỏ hoạt động hiệu quả, và đúng là chúng đã được thiết kế như vậy.

Tuy nhiên, có một số nhược điểm khi sử dụng con trỏ và tham chiếu. Quan trọng nhất là nó yêu cầu thêm một thanh ghi để giữ giá trị của con trỏ hoặc tham chiếu. Thanh ghi là một nguồn tài nguyên khan hiếm, đặc biệt ở chế độ 32-bit. Nếu không có đủ thanh ghi, con trỏ phải được nạp (loaded) từ bộ nhớ mỗi khi nó được sử dụng và điều này sẽ làm chương trình chậm hơn. Một bất lợi khác là giá trị của con trỏ cần phải có sẵn một vài chu kỳ xung nhịp trước thời điểm truy cập biến được trỏ tới.

**Số học con trỏ (Pointer arithmetic)**

Con trỏ trên thực tế là một số nguyên chứa địa chỉ bộ nhớ. Do đó, các phép toán số học với con trỏ cũng nhanh như phép toán số học với số nguyên. Khi một số nguyên được cộng vào một con trỏ, giá trị của số nguyên đó sẽ được nhân với kích thước của đối tượng mà con trỏ đang trỏ tới. Ví dụ:

```cpp
// Example 7.13 
struct abc {int a; int b; int c;}; 
abc * p; int i; 
p = p + i; 
```

Tại đây, giá trị được cộng vào `p` không phải là `i` mà là `i*12`, vì kích thước của `abc` là 12 bytes. Thời gian để thêm `i` vào `p` do đó bằng với thời gian thực hiện một phép nhân và một phép cộng. Nếu kích thước của `abc` là lũy thừa của 2 thì phép nhân có thể được thay thế bằng phép dịch chuyển (shift operation) vốn nhanh hơn nhiều. Trong ví dụ trên, kích thước của `abc` có thể được tăng lên 16 bytes bằng cách thêm một số nguyên nữa vào cấu trúc.

Việc tăng (Incrementing) hoặc giảm (decrementing) một con trỏ không yêu cầu phép nhân mà chỉ cần một phép cộng. So sánh hai con trỏ chỉ yêu cầu so sánh số nguyên, khá nhanh. Tính toán hiệu số (difference) giữa hai con trỏ yêu cầu một phép chia, và phép toán này sẽ bị chậm trừ khi kích thước của kiểu đối tượng được trỏ tới là lũy thừa của 2 (Xem trang 140 về phép chia).

Đối tượng được trỏ tới có thể được truy cập khoảng hai chu kỳ xung nhịp sau khi giá trị của con trỏ được tính toán. Do đó, khuyến nghị tính toán giá trị của con trỏ trước lúc sử dụng con trỏ đó. Ví dụ, `x = *(p++)` hiệu quả hơn `x = *(++p)` bởi vì trong trường hợp sau, việc đọc `x` phải đợi thêm vài chu kỳ xung nhịp sau khi con trỏ `p` đã được tăng lên, trong khi với trường hợp trước, `x` có thể được đọc trước khi `p` tăng lên. Xem trang 31 để biết thêm phần thảo luận về các toán tử tăng và giảm.

## 7.7 Con trỏ hàm (Function pointers)

Gọi một hàm thông qua một con trỏ hàm (function pointer) thường tốn thêm một vài chu kỳ xung nhịp so với gọi hàm trực tiếp nếu địa chỉ đích (target address) có thể được dự đoán. Địa chỉ đích được dự đoán nếu giá trị của con trỏ hàm giống hệt như lần cuối cùng câu lệnh được thực thi. Nếu giá trị của con trỏ hàm đã thay đổi, địa chỉ đích có khả năng bị dự đoán sai, gây ra một độ trễ dài. Xem trang 44 về dự đoán nhánh (branch prediction). Bộ vi xử lý Pentium M có thể dự đoán mục tiêu nếu các thay đổi của con trỏ hàm tuân theo một khuôn mẫu (pattern) thông thường đơn giản, trong khi bộ vi xử lý Pentium 4 và AMD chắc chắn sẽ đưa ra dự đoán sai mỗi khi con trỏ hàm thay đổi.

## 7.8 Con trỏ thành viên (Member pointers)

Trong những trường hợp đơn giản, một con trỏ thành viên dữ liệu (data member pointer) chỉ đơn thuần lưu trữ độ lệch (offset) của một thành viên dữ liệu so với điểm đầu của đối tượng, và một con trỏ hàm thành viên (member function pointer) chỉ là địa chỉ của hàm thành viên. Nhưng có một số trường hợp đặc biệt như đa kế thừa (multiple inheritance) trong đó cần đến một cách triển khai phức tạp hơn nhiều. Bạn hoàn toàn nên tránh những trường hợp phức tạp này.

Trình biên dịch phải sử dụng cách thức triển khai phức tạp nhất của con trỏ thành viên nếu nó không có đầy đủ thông tin về lớp mà con trỏ thành viên tham chiếu tới. Ví dụ:

```cpp
// Example 7.14 
class c1; 
int c1::*MemberPointer; 
```

Tại đây, trình biên dịch không có thông tin nào về lớp `c1` ngoài cái tên của nó tại thời điểm khai báo `MemberPointer`. Do đó, nó phải giả định tình huống tồi tệ nhất có thể xảy ra và thực hiện một quá trình triển khai phức tạp đối với con trỏ thành viên. Điều này có thể tránh được bằng cách khai báo đầy đủ cho lớp `c1` trước khi khai báo `MemberPointer`. Hãy tránh sử dụng đa kế thừa, các hàm ảo (virtual functions) và các yếu tố phức tạp khác khiến các con trỏ thành viên giảm đi tính hiệu quả.

Hầu hết các trình biên dịch C++ đều có các tùy chọn khác nhau để điều khiển cách các con trỏ thành viên được triển khai. Sử dụng tùy chọn mang lại cách triển khai đơn giản nhất nếu có thể, và đảm bảo rằng bạn đang sử dụng cùng một tùy chọn biên dịch cho tất cả các mô-đun (modules) dùng chung một con trỏ thành viên.

## 7.9 Con trỏ thông minh (Smart pointers)

Con trỏ thông minh (smart pointer) là một đối tượng cư xử giống như một con trỏ. Nó có một tính năng đặc biệt là đối tượng mà nó trỏ tới sẽ bị xóa (delete) khi con trỏ bị xóa. Các con trỏ thông minh chỉ được sử dụng cho các đối tượng được lưu trữ trong bộ nhớ cấp phát động, sử dụng `new`. Mục đích của việc sử dụng các con trỏ thông minh là để đảm bảo đối tượng được xóa đúng cách và giải phóng bộ nhớ khi đối tượng không còn được sử dụng. Một con trỏ thông minh có thể được coi là một container (vùng chứa) chỉ chứa một phần tử duy nhất.

Các cách triển khai phổ biến nhất của con trỏ thông minh là `auto_ptr` và `shared_ptr`.
