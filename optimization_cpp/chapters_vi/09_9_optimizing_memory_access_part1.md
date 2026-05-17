# 9 Tối ưu hóa truy cập bộ nhớ

## 9.1 Caching mã và dữ liệu
Bộ nhớ đệm (cache) là một bộ nhớ đại diện (proxy) cho bộ nhớ chính trong máy tính. Bộ nhớ đại diện này nhỏ hơn và gần CPU hơn so với bộ nhớ chính và do đó việc truy cập vào nó sẽ nhanh hơn rất nhiều. Có thể có hai hoặc ba cấp độ bộ nhớ đệm nhằm mang lại tốc độ truy cập nhanh nhất có thể đối với những dữ liệu được sử dụng nhiều nhất.

Tốc độ của các CPU đang tăng nhanh hơn so với tốc độ của bộ nhớ RAM. Do đó, việc lưu trữ bộ nhớ đệm hiệu quả đang ngày càng trở nên quan trọng hơn.

## 9.2 Tổ chức bộ nhớ đệm
Sẽ rất hữu ích nếu bạn biết cách một bộ nhớ đệm được tổ chức ra sao khi bạn đang viết các chương trình có cấu trúc dữ liệu lớn cùng khả năng truy cập không tuần tự và bạn muốn ngăn chặn sự cạnh tranh bộ nhớ đệm (cache contention). Bạn có thể bỏ qua phần này nếu bạn đã hài lòng với các nguyên tắc mang tính kinh nghiệm (heuristic) hơn.

Hầu hết các bộ nhớ đệm được tổ chức thành các dòng (lines) và các tập hợp (sets). Hãy để tôi giải thích điều này bằng một ví dụ. Ví dụ của tôi là một bộ nhớ đệm có kích thước 8 kb với kích thước dòng là 64 byte. Mỗi dòng bao trùm 64 byte bộ nhớ liên tiếp. Một kilobyte bằng 1024 byte, vì vậy chúng ta có thể tính ra số lượng dòng là 8*1024/64 = 128. Các dòng này được tổ chức thành 32 tập hợp x 4 chiều (ways). Điều này có nghĩa là một địa chỉ bộ nhớ cụ thể không thể được tải vào một dòng bộ nhớ đệm bất kỳ. Chỉ có thể sử dụng một trong 32 tập hợp, nhưng bất kỳ dòng nào trong 4 dòng thuộc tập hợp đó đều có thể được sử dụng. Chúng ta có thể tính toán tập hợp dòng bộ nhớ đệm nào sẽ được sử dụng đối với một địa chỉ bộ nhớ cụ thể theo công thức: (tập hợp) = (địa chỉ bộ nhớ) / (kích thước dòng) % (số lượng tập hợp). Ở đây, / có nghĩa là phép chia nguyên lấy phần nguyên, và % có nghĩa là modulo (chia lấy dư). Ví dụ, nếu chúng ta muốn đọc từ địa chỉ bộ nhớ a = 10000, thì chúng ta có (tập hợp) = (10000 / 64) % 32 = 28. Điều này có nghĩa là a phải được đọc vào một trong bốn dòng bộ nhớ đệm thuộc tập hợp số 28. Phép tính này trở nên dễ dàng hơn nếu chúng ta sử dụng hệ cơ số thập lục phân (hexadecimal) vì tất cả các số đều là lũy thừa của 2. Sử dụng các số hex, chúng ta có a = 0x2710 và (tập hợp) = (0x2710 / 0x40) % 0x20 = 0x1C. Việc đọc hoặc viết vào một biến từ địa chỉ 0x2710 sẽ khiến bộ nhớ đệm phải tải toàn bộ 64 hoặc 0x40 byte từ địa chỉ 0x2700 đến 0x273F vào một trong bốn dòng bộ nhớ đệm thuộc tập hợp 0x1C. Nếu chương trình sau đó thực hiện đọc hoặc viết vào bất kỳ địa chỉ nào khác trong phạm vi này thì giá trị đã có sẵn trong bộ nhớ đệm nên chúng ta không cần phải đợi cho một thao tác truy cập bộ nhớ khác.

Giả sử rằng một chương trình đọc từ địa chỉ 0x2710 và sau đó đọc từ các địa chỉ 0x2F00, 0x3700, 0x3F00 và 0x4700. Tất cả các địa chỉ này đều thuộc về tập hợp số 0x1C. Chỉ có bốn dòng bộ nhớ đệm trong mỗi tập hợp. Nếu bộ nhớ đệm luôn chọn dòng bộ nhớ đệm ít được sử dụng gần đây nhất (least recently used) thì dòng bao trùm phạm vi địa chỉ từ 0x2700 đến 0x273F sẽ bị loại bỏ khi chúng ta đọc từ 0x4700. Việc đọc lại từ địa chỉ 0x2710 sẽ gây ra hiện tượng trượt bộ nhớ đệm (cache miss). Nhưng nếu chương trình đã đọc từ các địa chỉ khác nhau với các giá trị tập hợp khác nhau thì dòng chứa phạm vi địa chỉ từ 0x2700 đến 0x273F vẫn sẽ nằm trong bộ nhớ đệm. Vấn đề chỉ xảy ra bởi vì các địa chỉ được đặt cách nhau một khoảng bằng bội số của 0x800. Tôi sẽ gọi khoảng cách này là khoảng cách tới hạn (critical stride). Các biến có khoảng cách trong bộ nhớ là bội số của khoảng cách tới hạn sẽ cạnh tranh cho cùng các dòng bộ nhớ đệm. Khoảng cách tới hạn có thể được tính bằng (khoảng cách tới hạn) = (số lượng tập hợp) x (kích thước dòng) = (tổng kích thước bộ nhớ đệm) / (số lượng chiều).

Nếu một chương trình chứa nhiều biến và đối tượng nằm rải rác trong bộ nhớ thì sẽ có nguy cơ một vài biến vô tình nằm cách nhau một khoảng bằng bội số của khoảng cách tới hạn và gây ra sự cạnh tranh (contentions) trong bộ nhớ đệm dữ liệu. Điều tương tự cũng có thể xảy ra trong bộ nhớ đệm chứa đoạn mã nếu có nhiều hàm nằm rải rác trong bộ nhớ của chương trình. Nếu một vài hàm được sử dụng trong cùng một phần của chương trình vô tình có khoảng cách bằng bội số của khoảng cách tới hạn thì điều này có thể gây ra sự cạnh tranh trong bộ nhớ đệm chứa đoạn mã. Các phần tiếp theo sẽ mô tả nhiều cách khác nhau để tránh những vấn đề này.

Thông tin chi tiết hơn về cách thức hoạt động của bộ nhớ đệm có thể được tìm thấy trên Wikipedia trong mục CPU cache (en.wikipedia.org/wiki/L2_cache).

Các chi tiết về việc tổ chức bộ nhớ đệm đối với các bộ xử lý khác nhau được đề cập trong hướng dẫn số 3: "The microarchitecture of Intel, AMD and VIA CPUs".

## 9.3 Các hàm được dùng chung với nhau nên được lưu trữ cùng nhau
Bộ nhớ đệm đoạn mã hoạt động hiệu quả nhất nếu các hàm được sử dụng gần nhau cũng được lưu trữ gần nhau trong bộ nhớ đoạn mã. Các hàm thường được lưu trữ theo thứ tự xuất hiện của chúng trong mã nguồn. Do đó, một ý tưởng tốt là tập hợp các hàm được sử dụng trong phần quan trọng nhất của đoạn mã lại với nhau ở gần nhau trong cùng một tệp mã nguồn. Hãy giữ các hàm thường xuyên được sử dụng tách biệt khỏi các hàm hiếm khi được sử dụng, và đặt các nhánh hiếm khi được sử dụng, chẳng hạn như xử lý lỗi ở cuối hàm hoặc trong một hàm riêng biệt.

Đôi khi, các hàm được giữ trong các tệp mã nguồn khác nhau nhằm mục đích tăng tính mô-đun. Ví dụ, việc giữ các hàm thành viên của lớp cha trong một tệp mã nguồn và các hàm của lớp kế thừa trong một tệp mã nguồn khác có thể sẽ thuận tiện. Nếu các hàm thành viên của lớp cha và lớp kế thừa được gọi từ cùng một phần quan trọng của chương trình thì việc giữ hai mô-đun này liền kề nhau trong bộ nhớ chương trình có thể mang lại lợi ích. Bạn có thể làm điều này bằng cách kiểm soát thứ tự mà các mô-đun được liên kết với nhau. Thứ tự liên kết (link order) thường là thứ tự mà các mô-đun xuất hiện trong cửa sổ dự án (project window) hoặc tệp makefile. Bạn có thể kiểm tra thứ tự của các hàm trong bộ nhớ bằng cách yêu cầu tệp bản đồ (map file) từ bộ liên kết (linker). Tệp bản đồ sẽ cho biết địa chỉ của từng hàm tương đối so với phần đầu của chương trình. Tệp bản đồ bao gồm địa chỉ của các hàm thư viện được liên kết từ các thư viện tĩnh (static libraries - tệp .lib hoặc .a), nhưng không bao gồm các thư viện động (dynamic libraries - tệp .dll hoặc .so). Không có cách dễ dàng nào để kiểm soát địa chỉ của các hàm thư viện được liên kết động.

## 9.4 Các biến được dùng chung với nhau nên được lưu trữ cùng nhau
Hiện tượng trượt bộ nhớ đệm (cache miss) rất đắt đỏ. Một biến có thể được lấy từ bộ nhớ đệm chỉ trong một vài chu kỳ xung nhịp, nhưng có thể mất hơn một trăm chu kỳ xung nhịp để lấy biến từ bộ nhớ RAM nếu nó không có trong bộ nhớ đệm.

Bộ nhớ đệm hoạt động hiệu quả nhất nếu các đoạn dữ liệu được dùng chung với nhau được lưu trữ gần nhau trong bộ nhớ. Tốt nhất là các biến và đối tượng nên được khai báo trong hàm mà chúng được sử dụng. Những biến và đối tượng như vậy sẽ được lưu trữ trên ngăn xếp (stack), nơi rất có thể sẽ nằm trong bộ nhớ đệm cấp 1. Các loại lưu trữ biến khác nhau được giải thích trên trang 26. Tránh sử dụng các biến toàn cục (global) và biến tĩnh (static) nếu có thể, và tránh cấp phát bộ nhớ động (`new` và `delete`).

Lập trình hướng đối tượng có thể là một cách hiệu quả để giữ dữ liệu ở cùng nhau. Các thành viên dữ liệu của một lớp (còn được gọi là thuộc tính) luôn được lưu trữ cùng nhau trong một đối tượng của lớp đó. Các thành viên dữ liệu của lớp cha và lớp kế thừa được lưu trữ cùng nhau trong một đối tượng của lớp kế thừa (xem trang 52).

Thứ tự lưu trữ dữ liệu có thể đóng vai trò quan trọng nếu bạn có cấu trúc dữ liệu lớn. Ví dụ, nếu một chương trình có hai mảng, a và b, và các phần tử được truy cập theo thứ tự a[0], b[0], a[1], b[1], ... thì bạn có thể cải thiện hiệu năng bằng cách tổ chức dữ liệu thành một mảng của các cấu trúc (array of structures):

```cpp
// Example 9.1a 
int Func(int); 
const int size = 1024; 
int a[size], b[size], i; 
... 
for (i = 0; i < size; i++) { 
   b[i] = Func(a[i]); 
} 
```

Dữ liệu trong ví dụ này có thể được truy cập tuần tự trong bộ nhớ nếu được sắp xếp như sau:

```cpp
// Example 9.1b 
int Func(int); 
const int size = 1024; 
struct Sab {int a; int b;}; 
Sab ab[size]; 
int i; 
... 
for (i = 0; i < size; i++) { 
   ab[i].b = Func(ab[i].a); 
} 
```

Sẽ không có chi phí bộ đệm (overhead) phụ thêm trong mã chương trình cho việc tạo cấu trúc trong ví dụ 9.1b. Ngược lại, đoạn mã trở nên đơn giản hơn vì nó chỉ cần tính toán địa chỉ phần tử cho một mảng thay vì hai.

Một số trình biên dịch sẽ sử dụng các không gian bộ nhớ khác nhau cho các mảng khác nhau ngay cả khi chúng không bao giờ được sử dụng cùng một lúc. Ví dụ:

```cpp
// Example 9.2a 
void F1(int   x[]); 
void F2(float x[]); 
 
void F3(bool y) {    
   if (y) { 
      int a[1000]; 
      F1(a); 
   } 
   else { 
      float b[1000]; 
      F2(b); 
   } 
} 
```

Ở đây, hoàn toàn có thể sử dụng cùng một vùng bộ nhớ cho `a` và `b` vì khoảng hoạt động của chúng không hề chồng chéo nhau. Bạn có thể tiết kiệm rất nhiều không gian bộ nhớ đệm bằng cách nối kết `a` và `b` trong một cấu trúc `union`:

```cpp
// Example 9.2b 
void F3(bool y) {    
   union { 
      int   a[1000]; 
      float b[1000]; 
   }; 
   if (y) { 
      F1(a); 
   } 
   else { 
      F2(b); 
   } 
} 
```

Tất nhiên, sử dụng một `union` không phải là một phương pháp lập trình an toàn, bởi vì bạn sẽ không nhận được bất kỳ cảnh báo nào từ trình biên dịch nếu việc sử dụng `a` và `b` bị chồng chéo. Bạn chỉ nên sử dụng phương pháp này đối với các đối tượng lớn chiếm nhiều không gian bộ nhớ đệm. Việc đưa các biến đơn giản vào một `union` là không tối ưu vì nó ngăn cản việc sử dụng các biến thanh ghi.

## 9.5 Căn chỉnh dữ liệu
Một biến được truy cập hiệu quả nhất nếu nó được lưu trữ tại một địa chỉ bộ nhớ chia hết cho kích thước của biến đó. Ví dụ, một số `double` chiếm 8 byte không gian lưu trữ. Do đó, tốt nhất là nó nên được lưu trữ tại một địa chỉ chia hết cho 8. Kích thước phải luôn là lũy thừa của 2. Các đối tượng lớn hơn 16 byte nên được lưu trữ tại một địa chỉ chia hết cho 16. Nhìn chung, bạn có thể cho rằng trình biên dịch sẽ tự động thực hiện việc căn chỉnh này.

Việc căn chỉnh các thành viên của cấu trúc và lớp có thể gây lãng phí không gian bộ nhớ đệm, như đã giải thích trong ví dụ 7.39 ở trang 53.

Bạn có thể chọn căn chỉnh các đối tượng và mảng lớn theo kích thước dòng của bộ nhớ đệm, thường là 64 byte. Việc này đảm bảo rằng phần đầu của đối tượng hoặc mảng trùng khớp với phần đầu của dòng bộ nhớ đệm. Một số trình biên dịch sẽ tự động căn chỉnh các mảng tĩnh lớn nhưng bạn cũng có thể chỉ định rõ ràng việc căn chỉnh bằng cách viết:

```cpp
__declspec(align(64)) int BigArray[1024]; // Windows syntax 
```

hoặc

```cpp
int BigArray[1024] __attribute__((aligned(64))); // Linux syntax 
```

Xem trang 96 và 123 để biết các cuộc thảo luận về việc căn chỉnh đối với bộ nhớ được cấp phát động.

## 9.6 Cấp phát bộ nhớ động
Các đối tượng và mảng có thể được cấp phát động với `new` và `delete`, hoặc `malloc` và `free`. Điều này có thể hữu ích khi số lượng bộ nhớ cần thiết không được biết vào thời điểm biên dịch. Có bốn cách sử dụng điển hình của việc cấp phát bộ nhớ động được đề cập tại đây:

* Một mảng lớn có thể được cấp phát động khi kích thước của mảng không được biết ở thời điểm biên dịch.
* Số lượng đối tượng biến thiên có thể được cấp phát động khi tổng số lượng đối tượng không được biết ở thời điểm biên dịch.
* Các chuỗi văn bản và các đối tượng tương tự có kích thước biến thiên có thể được cấp phát động.
* Các mảng quá lớn đối với ngăn xếp (stack) có thể được cấp phát động.

Những ưu điểm của cấp phát bộ nhớ động bao gồm:

* Cung cấp một cấu trúc chương trình rõ ràng hơn trong một số trường hợp.
* Không cấp phát nhiều không gian hơn mức cần thiết. Điều này giúp cho quá trình lưu trữ dữ liệu vào bộ nhớ đệm hiệu quả hơn so với khi sử dụng một mảng có kích thước cố định được làm rất lớn để đảm bảo giải quyết được cả tình huống xấu nhất liên quan đến yêu cầu bộ nhớ cao nhất có thể xảy ra.
* Hữu ích khi không có giới hạn trên hợp lý nào cho lượng bộ nhớ cần thiết có thể được cung cấp trước.

Những nhược điểm của cấp phát bộ nhớ động bao gồm:

* Quá trình cấp phát và thu hồi bộ nhớ động tốn nhiều thời gian hơn nhiều so với các loại lưu trữ khác. Xem trang 26.
* Không gian vùng bộ nhớ heap trở nên bị phân mảnh (fragmented) khi các đối tượng có kích thước khác nhau được cấp phát và thu hồi một cách ngẫu nhiên. Điều này làm cho việc lưu trữ dữ liệu vào bộ nhớ đệm trở nên kém hiệu quả.
* Một mảng đã được cấp phát có thể cần phải thay đổi kích thước trong trường hợp nó bị đầy. Điều này có thể yêu cầu việc phân bổ một khối bộ nhớ mới lớn hơn và sao chép toàn bộ nội dung sang khối bộ nhớ mới. Bất kỳ con trỏ nào trỏ đến phần dữ liệu trong khối cũ sau đó đều sẽ trở nên không hợp lệ.
* Trình quản lý heap sẽ bắt đầu thu gom rác (garbage collection) khi vùng không gian heap trở nên quá phân mảnh. Việc thu gom rác này có thể bắt đầu vào những khoảng thời gian không thể đoán trước và gây ra sự chậm trễ cho luồng chương trình vào những thời điểm bất tiện khi người dùng đang chờ đợi để nhận được phản hồi.
* Trách nhiệm của lập trình viên là đảm bảo rằng mọi thứ đã được cấp phát cũng sẽ được thu hồi. Nếu không làm như vậy, vùng heap sẽ bị lấp đầy. Đây là một lỗi lập trình phổ biến được gọi là rò rỉ bộ nhớ (memory leaks).
* Trách nhiệm của lập trình viên là đảm bảo rằng không có đối tượng nào được truy cập sau khi nó đã bị thu hồi. Việc không làm như vậy cũng là một lỗi lập trình phổ biến.
* Bộ nhớ được cấp phát có thể không được căn chỉnh một cách tối ưu. Xem trang 123 về cách để căn chỉnh bộ nhớ được cấp phát động.
* Trình biên dịch rất khó tối ưu hóa các mã sử dụng con trỏ bởi vì nó không thể loại bỏ hoàn toàn hiện tượng bí danh (aliasing) (xem trang 79).
* Một ma trận hoặc mảng đa chiều sẽ kém hiệu quả hơn nếu chiều dài hàng không được biết trước vào thời điểm biên dịch do phải thực hiện thêm công việc để tính toán phần địa chỉ của hàng tại mỗi một lần truy cập. Trình biên dịch có thể sẽ không thể tối ưu hóa được việc này bằng các biến quy nạp.

Điều quan trọng là phải cân nhắc các ưu điểm so với các nhược điểm khi quyết định xem có nên sử dụng cấp phát bộ nhớ động hay không. Không có lý do gì để sử dụng bộ nhớ động khi kích thước mảng hoặc số lượng các đối tượng đã được biết trước vào thời điểm biên dịch hoặc có thể xác định được một giới hạn trên hợp lý.

Chi phí của việc cấp phát bộ nhớ động là không đáng kể khi số lượng các lần cấp phát bị hạn chế. Do đó, bộ nhớ động có thể mang lại lợi ích khi một chương trình có một hoặc một vài mảng với kích thước có thể thay đổi. Giải pháp thay thế bằng cách làm cho các mảng trở nên rất lớn để bao phủ được tình huống xấu nhất lại làm lãng phí không gian bộ nhớ đệm. Một tình huống khi chương trình sở hữu một số mảng lớn và khi kích thước của mỗi mảng lại là bội số của khoảng cách tới hạn (xem ở trên, trang 88) thì rất có thể sẽ gây ra các cạnh tranh (contentions) trong bộ nhớ đệm dữ liệu.

Nếu số lượng các phần tử trong một mảng tăng dần trong quá trình thực thi chương trình thì tốt hơn hết là cấp phát luôn kích thước mảng cuối cùng ngay từ đầu thay vì phân bổ thêm không gian theo từng bước. Trong hầu hết các hệ thống, bạn không thể tăng kích thước cho một khối bộ nhớ đã được cấp phát. Nếu không thể đoán trước được kích thước cuối cùng hoặc nếu sự dự đoán hóa ra lại quá nhỏ, thì cần phải cấp phát một khối bộ nhớ lớn hơn và sao chép nội dung thuộc về khối bộ nhớ cũ sang vị trí bắt đầu của khối bộ nhớ mới lớn hơn. Điều này tất nhiên là không hiệu quả, và khiến cho vùng không gian heap bị phân mảnh. Một giải pháp thay thế là lưu trữ nhiều khối bộ nhớ, có thể dưới dạng danh sách liên kết (linked list) hoặc có chỉ mục của các khối bộ nhớ. Phương pháp liên quan tới nhiều khối bộ nhớ làm cho việc truy cập vào các phần tử của mảng một cách riêng lẻ trở nên phức tạp hơn và gây tốn nhiều thời gian.

Một tập hợp với số lượng đối tượng có thể thay đổi thường được triển khai dưới dạng danh sách liên kết. Mỗi phần tử trong danh sách liên kết có khối bộ nhớ riêng và một con trỏ trỏ đến khối tiếp theo. Một danh sách liên kết hoạt động kém hiệu quả hơn so với mảng tuyến tính vì những lý do sau đây:

* Mỗi đối tượng được cấp phát riêng biệt. Việc cấp phát, thu hồi và quá trình dọn rác bộ nhớ chiếm một khoảng thời gian đáng kể.
* Các đối tượng không được lưu trữ kề nhau trong bộ nhớ. Điều này làm cho việc lưu trữ dữ liệu đệm kém hiệu quả hơn.
* Không gian bộ nhớ phụ thêm sẽ được dùng cho các con trỏ liên kết và cho những thông tin được lưu trữ bởi hệ thống quản lý heap cho từng khối được cấp phát.
* Việc lướt qua một danh sách liên kết sẽ tốn nhiều thời gian hơn là đi vòng quanh một mảng tuyến tính. Sẽ không có con trỏ liên kết nào có thể được tải cho tới khi con trỏ liên kết đứng trước đó đã được tải xong. Điều này tạo ra một chuỗi phụ thuộc có tính chí mạng, gây cản trở lên quá trình thực thi không tuần tự (out-of-order execution).

Thường thì cấp phát một khối bộ nhớ lớn duy nhất cho toàn bộ các đối tượng (nhóm vùng nhớ, memory pooling) sẽ cho thấy được sự hiệu quả lớn hơn là việc cấp phát các khối nhỏ cho mỗi đối tượng riêng biệt.

Một kỹ thuật thay thế ít người biết tới dành cho `new` và `delete` chính là việc thực hiện việc cấp phát mảng với kích thước tùy biến thông qua `alloca`. Đây là một hàm phân bổ không gian bộ nhớ trên ngăn xếp thay vì vùng heap. Phần không gian sẽ tự động bị thu hồi khi có thao tác quay về từ hàm đã chứa lời gọi `alloca`. Việc thu hồi không gian một cách rõ ràng khi xài `alloca` là việc không cần làm. So với `new` và `delete` hoặc `malloc` và `free`, việc sử dụng `alloca` có thể mang lại các lợi thế sau:

* Có rất ít chi phí bộ đệm (overhead) cho quá trình cấp phát bởi vì bộ vi xử lý đã trang bị sự hỗ trợ phần cứng (hardware support) dành riêng cho ngăn xếp.
* Không gian bộ nhớ sẽ không bao giờ xuất hiện tình trạng phân mảnh là nhờ tính chất vào trước-ra sau (first-in-last-out) vốn có của ngăn xếp.
* Việc thu hồi không tốn bất kỳ chi phí nào vì nó diễn ra tự động khi hàm trả về kết quả. Do đó việc thu gom rác (garbage collection) là không cần thiết.
* Bộ nhớ vừa được cấp phát sẽ nằm liền kề với những đối tượng đang nằm trên ngăn xếp, điều này giúp cho quá trình lưu trữ dữ liệu vào bộ nhớ đệm mang lại hiệu suất cực cao.

Đoạn mã trong ví dụ ngay phía sau đây mô phỏng phương pháp tạo một mảng có kích thước biến thiên với sự hỗ trợ của hàm `alloca`:

```cpp
// Example 9.3 
#include <malloc.h> 
 
void SomeFunction (int n) { 
   if (n > 0) { 
      // Make dynamic array of n floats: 
      float * DynamicArray = (float *)alloca(n * sizeof(float)); 
      // (Some compilers use the name _alloca) 
      for (int i = 0; i < n; i++) { 
         DynamicArray[i] = WhateverFunction(i); 
         // ... 
      } 
   } 
}  
```

Rõ ràng, một hàm không bao giờ nên trả về bất kỳ con trỏ hay tham chiếu nào trỏ tới thứ mà nó vừa mới cấp phát bằng `alloca`, bởi vì dung lượng này đã được giải phóng hoàn toàn tại thời điểm hàm trả về kết quả. `alloca` có khả năng không tương thích với việc xử lý ngoại lệ có cấu trúc. Hãy tham khảo phần hướng dẫn của trình biên dịch mà bạn đang sử dụng để biết các quy tắc hạn chế về việc dùng lệnh `alloca`.

## 9.7 Lớp vùng chứa (Container classes)
Bất cứ khi nào cấp phát bộ nhớ động được sử dụng, bạn nên bọc bộ nhớ được cấp phát vào trong một lớp vùng chứa (container class). Lớp vùng chứa này bắt buộc phải có hàm hủy (destructor) để đảm bảo rằng mọi thứ được cấp phát cũng sẽ được giải phóng. Đây là cách tốt nhất để ngăn chặn rò rỉ bộ nhớ (memory leaks) và các lỗi lập trình phổ biến khác liên quan đến cấp phát bộ nhớ động.

Các lớp vùng chứa cũng có thể rất tiện lợi trong việc thêm chức năng kiểm tra giới hạn (bounds-checking) vào một mảng và hỗ trợ cho các cấu trúc dữ liệu nâng cao hơn có sử dụng cơ chế Vào trước-Ra trước (First-In-First-Out) hoặc Vào trước-Ra sau (First-In-Last-Out), các tiện ích sắp xếp (sort) và tìm kiếm (search facilities), cây nhị phân (binary trees), biểu đồ băm (hash maps), v.v.

Thông thường người ta hay tạo ra các lớp vùng chứa dưới dạng các khuôn mẫu (templates) mà ở đó kiểu của các đối tượng chúng chứa được xem như một tham số của khuôn mẫu (template parameter). Sẽ không có chi phí về hiệu suất nào khi sử dụng các khuôn mẫu này.

Các mẫu lớp vùng chứa được làm sẵn luôn có sẵn cho nhiều mục đích khác nhau. Bộ vùng chứa được sử dụng phổ biến nhất là Thư viện Khuôn mẫu Chuẩn (Standard Template Library - STL) đi kèm với hầu hết các trình biên dịch C++ hiện đại. Ưu điểm của việc sử dụng các vùng chứa có sẵn là bạn không cần phải phát minh lại bánh xe. Các vùng chứa trong STL mang tính phổ quát, linh hoạt, đã được kiểm tra kỹ lưỡng và rất hữu ích cho nhiều mục đích khác nhau.

Tuy nhiên, STL được thiết kế cho tính tổng quát và tính linh hoạt, trong khi tốc độ thực thi, tính kinh tế của bộ nhớ, hiệu quả của bộ nhớ đệm và kích thước đoạn mã không được ưu tiên cao. Đặc biệt là việc cấp phát bộ nhớ trong STL gây lãng phí không cần thiết. Một số template của STL như `list`, `set` và `map` có xu hướng cấp phát số lượng khối bộ nhớ nhiều hơn so với số lượng đối tượng có trong vùng chứa. `deque` (hàng đợi hai đầu) của STL cấp phát một khối bộ nhớ cho mỗi bốn đối tượng. `vector` của STL lưu trữ tất cả các đối tượng trong cùng một khối bộ nhớ, nhưng khối bộ nhớ này sẽ được cấp phát lại mỗi khi nó bị đầy, điều này xảy ra khá thường xuyên do kích thước khối chỉ tăng trưởng 50% hoặc ít hơn trong mỗi lần cấp phát. Một cuộc thử nghiệm khi chèn 10 phần tử lần lượt từng phần tử một vào một `vector` của STL cho thấy nó đã gây ra bảy lần cấp phát bộ nhớ với kích thước lần lượt là 1, 2, 3, 4, 6, 9 và 13 đối tượng (phiên bản MS Visual Studio 2008). Hành vi gây lãng phí này có thể được ngăn chặn bằng cách gọi `vector::reserve` kèm theo một ước tính về kích thước tối đa cần thiết trước khi thêm đối tượng đầu tiên vào `vector`. Các vùng chứa STL khác không có tính năng đặt trước bộ nhớ (reserving memory in advance) như vậy.

Việc cấp phát và giải phóng bộ nhớ thường xuyên bằng `new` và `delete` (hoặc `malloc` và `free`) làm cho bộ nhớ bị phân mảnh và việc lưu vào bộ nhớ đệm (caching) trở nên kém hiệu quả. Việc quản lý bộ nhớ và thu gom rác (garbage collection) có chi phí (overhead) lớn, như đã đề cập ở trên.

Tính tổng quát của STL cũng phải trả giá bằng kích thước đoạn mã. Trên thực tế, STL đã bị chỉ trích vì sự cồng kềnh và tính phức tạp của mã nguồn (en.wikipedia.org/wiki/Standard_Template_Library). Các đối tượng được lưu trữ trong một vùng chứa STL được phép có các hàm tạo (constructors) và hàm hủy (destructors). Các hàm tạo sao chép (copy constructors) và hàm hủy của mỗi đối tượng được gọi mỗi khi một đối tượng bị di chuyển, điều này có thể xảy ra khá thường xuyên. Điều này là cần thiết nếu bản thân các đối tượng được lưu trữ là các vùng chứa. Nhưng việc cài đặt một ma trận trong STL dưới dạng một `vector` của các `vector`, như thường thấy, chắc chắn là một giải pháp rất kém hiệu quả.

Nhiều vùng chứa sử dụng danh sách liên kết. Danh sách liên kết là một cách thuận tiện để làm cho vùng chứa có thể mở rộng, nhưng nó lại rất kém hiệu quả. Các mảng tuyến tính nhanh hơn danh sách liên kết trong hầu hết các trường hợp.

Các trình lặp (iterators) được sử dụng trong STL để truy cập vào các phần tử của vùng chứa khá cồng kềnh đối với nhiều lập trình viên và chúng không thực sự cần thiết nếu bạn có thể sử dụng một danh sách tuyến tính với chỉ số (index) đơn giản. Một trình biên dịch tốt có thể tối ưu hóa để loại bỏ phần chi phí (overhead) dư thừa của trình lặp trong một số trường hợp, nhưng không phải tất cả.

May mắn thay, có những giải pháp thay thế hiệu quả hơn có thể được sử dụng ở những nơi mà tốc độ thực thi, tính kinh tế của bộ nhớ, hiệu quả của bộ đệm và kích thước đoạn mã được ưu tiên hàng đầu. Biện pháp khắc phục quan trọng nhất là tạo nhóm bộ nhớ (memory pooling). Việc lưu trữ nhiều đối tượng cùng với nhau trong một khối bộ nhớ lớn sẽ hiệu quả hơn nhiều so với việc lưu trữ mỗi đối tượng trong một khối bộ nhớ được cấp phát riêng lẻ. Một khối lớn chứa nhiều đối tượng có thể được sao chép hoặc di chuyển bằng một lời gọi duy nhất tới `memcpy` thay vì phải di chuyển từng đối tượng một cách riêng biệt nếu không có các hàm tạo sao chép và hàm hủy nào cần phải gọi.

Tôi đã viết một tập hợp các lớp vùng chứa mẫu (example container classes) sử dụng các phương pháp này nhằm mục đích cải thiện hiệu suất. Chúng có sẵn trong phần phụ lục của tài liệu này tại trang www.agner.org/optimize/cppexamples.zip với các lớp vùng chứa và template cho nhiều mục đích khác nhau. Tất cả các ví dụ này đều được tối ưu hóa cho tốc độ thực thi và để giảm thiểu sự phân mảnh bộ nhớ. Việc kiểm tra giới hạn (bounds checking) được tích hợp vì lý do an toàn, nhưng nó có thể bị xóa đi sau khi tiến hành gỡ lỗi (debugging) nếu được yêu cầu đối với các nguyên do hiệu năng. Hãy sử dụng những vùng chứa làm mẫu này trong các trường hợp mà hiệu năng của STL không được thỏa đáng.

Những cân nhắc sau đây nên được đưa vào tính toán khi lựa chọn một vùng chứa cho mục đích cụ thể:

* Chứa một hay nhiều phần tử? Nếu vùng chứa chỉ được giữ đúng một phần tử thì hãy dùng một con trỏ thông minh (smart pointer) (xem trang 38).
* Kích thước có được biết vào thời điểm biên dịch không? Nếu số lượng các phần tử đã được biết tại thời điểm biên dịch hoặc nếu bạn có thể đặt một mức giới hạn trên (upper limit) không quá lớn thì giải pháp tối ưu nhất là một mảng có kích thước cố định hoặc vùng chứa không có chức năng cấp phát bộ nhớ động. Tuy nhiên, nếu mảng hoặc vùng chứa quá lớn đối với ngăn xếp thì việc cấp phát bộ nhớ động vẫn sẽ cần thiết.
* Kích thước có được biết trước khi lưu trữ phần tử đầu tiên không? Nếu tổng số phần tử cần được lưu trữ đã được biết trước khi thực hiện lưu trữ phần tử đầu tiên (hoặc nếu có thể đưa ra mức ước tính hợp lý) thì nên ưu tiên việc sử dụng một vùng chứa cho phép đặt trước (reserve) dung lượng nhớ cần thiết thay vì phân bổ từng mảnh một (piecewise) hoặc phải cấp phát lại nếu dung lượng khối bộ nhớ hóa ra lại quá nhỏ.
* Các đối tượng có được đánh số liên tiếp không? Nếu các đối tượng được xác định qua các chỉ số liên tục (consecutive indices) hoặc thông qua các khóa (keys) nằm trong một phạm vi giới hạn thì một mảng đơn giản sẽ là giải pháp hiệu quả nhất.
* Có cần một cấu trúc đa chiều không? Một ma trận hoặc mảng đa chiều nên được lưu trữ trong một khối không gian bộ nhớ liền kề (contiguous). Không nên xài một vùng chứa riêng cho từng hàng hoặc cột. Việc truy cập sẽ diễn ra nhanh hơn nếu số lượng phần tử trên mỗi hàng là một hằng số được biết sẵn tại thời điểm biên dịch.
* Các đối tượng có được truy cập theo cơ chế FIFO không? Nếu các đối tượng được truy cập dựa theo tiêu chuẩn Vào trước-Ra trước (First-In-First-Out) thì hãy dùng một hàng đợi (queue). Sẽ hiệu quả hơn nhiều nếu triển khai hàng đợi này dưới dạng một bộ đệm vòng (circular buffer) thay vì là một danh sách liên kết.
* Các đối tượng có được truy cập theo cơ chế FILO không? Nếu các đối tượng được truy cập theo tiêu chuẩn Vào trước-Ra sau (First-In-Last-Out) thì hãy dùng một mảng tuyến tính kèm theo một chỉ số đỉnh ngăn xếp (top-of-stack index).
* Các đối tượng có được xác định bằng một khóa (key) không? Nếu các giá trị của khóa nằm gọn trong một giới hạn hẹp thì một mảng đơn giản cũng đủ để giải quyết. Nếu số lượng các đối tượng ở mức cao thì giải pháp tốt nhất ở đây có thể là một cây nhị phân (binary tree) hoặc một sơ đồ băm (hash map).
* Các đối tượng có trật tự tự nhiên (natural ordering) không? Nếu bạn cần phải thực hiện các tác vụ tìm kiếm thuộc dạng: "phần tử nào gần với biến x nhất?" hoặc "có bao nhiêu phần tử nằm giữa x và y?" thì bạn có thể sử dụng một danh sách đã được sắp xếp (sorted list) hoặc cây nhị phân.
* Có cần thực hiện tìm kiếm sau khi tất cả các đối tượng đã được thêm vào không? Nếu bắt buộc phải dùng tới các chức năng tìm kiếm nhưng chỉ ở lúc sau cùng khi mọi đối tượng đều đã được lưu trữ trong vùng chứa, thì một mảng tuyến tính sẽ là một giải pháp hiệu quả. Hãy sắp xếp mảng sau khi tất cả các phần tử đã được thêm vào và sau đó sử dụng tìm kiếm nhị phân (binary search) để tìm các phần tử. Một sơ đồ băm (hash map) cũng có thể trở thành phương án có tính hiệu quả.
* Có cần thực hiện tìm kiếm trước khi tất cả các đối tượng đã được thêm vào không? Nếu các chức năng tìm kiếm (search facilities) là thiết yếu, và các đối tượng mới có thể được bổ sung thêm bất cứ lúc nào, thì bài toán giải quyết lúc này lại rắc rối hơn. Nếu số lượng phần tử là nhỏ thì danh sách đã được sắp xếp (sorted list) được xem là giải pháp hiệu quả nhất vì tính đơn giản của nó. Nhưng một danh sách đã được sắp xếp có thể rất kém hiệu quả nếu danh sách này lớn bởi vì thao tác chèn một phần tử mới vào sẽ làm các phần tử kế đằng sau phải bị dời vị trí. Bắt buộc phải cần tới một cây nhị phân hoặc một sơ đồ băm trong tình huống này. Cây nhị phân có thể được sử dụng nếu các phần tử có một thứ tự tự nhiên và có các yêu cầu tìm kiếm cho các phần tử trong một khoảng (interval) cụ thể. Một sơ đồ băm có thể được sử dụng nếu các phần tử không có thứ tự cụ thể nhưng được xác định bởi một khóa duy nhất (unique key).
* Các đối tượng có chứa kiểu loại hoặc kích cỡ hỗn hợp không? Có thể lưu trữ các đối tượng khác kiểu (different types) hoặc các chuỗi có độ dài khác nhau trong cùng một memory pool. Tham khảo www.agner.org/optimize/cppexamples.zip. Nếu số lượng và kiểu của các phần tử đã được biết tại thời điểm biên dịch thì không cần phải sử dụng một vùng chứa hay một memory pool.
* Yêu cầu việc căn chỉnh (Alignment)? Một số ứng dụng yêu cầu dữ liệu phải được căn chỉnh tại các địa chỉ làm tròn (round addresses). Đặc biệt, việc sử dụng các vectơ bản thể (intrinsic vectors) yêu cầu việc căn chỉnh tới các địa chỉ chia hết cho 16. Việc căn chỉnh các cấu trúc dữ liệu tới các địa chỉ chia hết cho kích thước của dòng bộ nhớ đệm (thường là 64) có thể cải thiện hiệu năng trong một vài trường hợp.
* Đa luồng (Multiple threads)? Các lớp của vùng chứa nói chung không an toàn về luồng (thread safe) nếu có nhiều luồng (multiple threads) có thể thêm, xóa hoặc sửa đổi các đối tượng cùng một lúc. Trong các ứng dụng đa luồng (multithreaded), sẽ hiệu quả hơn nhiều nếu có các vùng chứa riêng biệt cho mỗi luồng thay vì phải tạm thời khóa một vùng chứa để cho quyền truy cập độc quyền (exclusive access) bởi mỗi luồng.
* Các con trỏ hướng tới các đối tượng bên trong (contained objects)? Có thể không an toàn nếu tạo một con trỏ trỏ tới đối tượng bên trong bởi vì vùng chứa có thể sẽ di chuyển đối tượng trong trường hợp cần thiết phải cấp phát lại bộ nhớ. Các đối tượng bên trong vùng chứa nên được xác định thông qua chỉ số (index) hoặc khóa (key) của chúng trong vùng chứa đó thay vì dùng các con trỏ hoặc tham chiếu. Dù vậy, vẫn có thể chấp nhận được việc truyền một con trỏ hoặc tham chiếu tới một đối tượng như thế vào một hàm không thực hiện việc thêm hay xóa đối tượng nếu không có luồng (thread) nào khác có quyền truy cập vào vùng chứa.
* Vùng chứa có khả năng tái sử dụng (recycled) hay không? Việc khởi tạo hay triệt bỏ các vùng chứa tốn chi phí khá lớn. Nếu logic của chương trình cho phép, sẽ hiệu quả hơn nhiều nếu tái sử dụng lại một vùng chứa thay vì xóa nó và tạo ra một vùng chứa mới.

Tôi đã cung cấp một vài ví dụ về các khuôn mẫu lớp vùng chứa (containers class templates) phù hợp tại trang www.agner.org/optimize/cppexamples.zip. Những ví dụ này có thể được sử dụng như các lựa chọn thay thế cho thư viện khuôn mẫu chuẩn (STL) nếu tính tổng quát đầy đủ và tính linh hoạt của các vùng chứa STL là không cần thiết. Bạn có thể tự viết các lớp vùng chứa cho riêng mình hoặc sửa đổi những vùng chứa có sẵn để phù hợp với các nhu cầu cụ thể.

## 9.8 Chuỗi văn bản (Strings)
Các chuỗi văn bản thường mang kích thước thay đổi linh hoạt - thứ không thể biết trước vào thời điểm dịch mã. Thao tác lưu trữ chuỗi văn bản vào bên trong các lớp cấu trúc như `string`, `wstring` hoặc `CString` chuyên dùng `new` và `delete` để phân bổ một khối không gian bộ nhớ mới trong mỗi khoảnh khắc mà một chuỗi được tạo hoặc bị sửa đổi. Điều này có thể khá không hiệu quả nếu một chương trình tạo ra hay hiệu chỉnh nhiều chuỗi.

Trong hầu hết các tình huống, cách nhanh nhất để thao tác với chuỗi là thông qua phong cách hệ C truyền thống với các mảng ký tự (character arrays). Các chuỗi có thể được xử lý bằng các hàm C như `strcpy`, `strcat`, `strlen`, `sprintf`, v.v. Nhưng hãy lưu ý rằng các hàm này không có tính năng kiểm tra tràn mảng (overflow). Một hiện tượng tràn mảng có thể gây ra các lỗi không thể đoán trước ở các vị trí khác trong chương trình mà rất khó để chẩn đoán. Trách nhiệm của lập trình viên là đảm bảo rằng các mảng đủ lớn để xử lý các chuỗi (bao gồm cả ký tự số không kết thúc - terminating zero) và để thực hiện việc kiểm tra tràn mảng ở nơi cần thiết. Các phiên bản đi tắt liên đới tới các chức năng hệ chuỗi căn bản cũng như các hàm hiệu quả phục vụ thao tác tìm kiếm và thông dịch cho chuỗi được cung cấp bên trong thư viện `asmlib` tại www.agner.org/optimize/asmlib.zip.

Nếu bạn muốn cải thiện tốc độ mà không gây nguy hiểm cho sự an toàn, bạn có thể lưu trữ tất cả chuỗi văn bản trong một memory pool, giống như mô tả bên trên. Có thể xem thêm các ví dụ được cung cấp trong phụ lục cho tài liệu hướng dẫn này tại www.agner.org/optimize/cppexamples.zip.

## 9.9 Truy cập dữ liệu theo tuần tự
Bộ nhớ đệm làm việc hiệu quả nhất khi dữ liệu được truy cập một cách tuần tự. Nó hoạt động có phần kém hiệu quả hơn khi dữ liệu được truy cập ngược lại và hoạt động rất kém hiệu quả khi dữ liệu bị truy cập theo một cơ chế ngẫu nhiên. Điều này được áp dụng cho việc đọc cũng như thao tác viết dữ liệu.

Các mảng đa chiều nên được truy cập với sự thay đổi đối với chỉ số cuối cùng (last index) nằm trong vòng lặp sâu nhất (innermost loop). Điểm này phản ánh trật tự mà các phần tử được lưu trữ trong bộ nhớ. Ví dụ:

```cpp
// Example 9.4 
const int NUMROWS = 100, NUMCOLUMNS = 100; 
int matrix[NUMROWS][NUMCOLUMNS]; 
int row, column; 
for (row = 0; row < NUMROWS; row++) 
   for (column = 0; column < NUMCOLUMNS; column++)  
      matrix[row][column] = row + column; 
```

Không được tráo đổi trật tự của hai vòng lặp này (trừ ở ngôn ngữ Fortran nơi thứ tự lưu trữ là ngược lại).

## 9.10 Sự cạnh tranh bộ đệm trên cấu trúc dữ liệu lớn
Không phải lúc nào cũng có thể truy cập tuần tự vào một mảng đa chiều. Một số ứng dụng (ví dụ: trong đại số tuyến tính) yêu cầu các mô thức truy cập khác. Việc này có thể gây ra những độ trễ (delays) nghiêm trọng nếu khoảng cách giữa các hàng trong một ma trận lớn tình cờ bằng với khoảng cách tới hạn (critical stride), như đã được giải thích ở trang 89. Hiện tượng này sẽ xảy ra nếu kích thước của một hàng ma trận (tính bằng byte) là một lũy thừa bậc cao của 2.

Ví dụ sau đây minh họa cho việc này. Ví dụ của tôi là một hàm thực hiện hoán vị một ma trận bậc hai, nghĩa là mỗi phần tử `matrix[r][c]` được hoán đổi với phần tử `matrix[c][r]`.

```cpp
// Example 9.5a 
const int SIZE = 64;          // number of rows/columns in matrix 
 
void transpose(double a[SIZE][SIZE]) { // function to transpose matrix 
   // define a macro to swap two array elements: 
   #define swapd(x,y) {temp=x; x=y; y=temp;} 
 
   int r, c;  double temp; 
   for (r = 1; r < SIZE; r++) {        // loop through rows 
      for (c = 0; c < r; c++) {        // loop columns below diagonal 
         swapd(a[r][c], a[c][r]);      // swap elements 
      } 
   } 
} 
 
void test () { 
   __declspec(__align(64))       // align by cache line size 
   double matrix[SIZE][SIZE];    // define matrix 
   transpose(matrix);            // call transpose function 
} 
```

Hoán vị một ma trận cũng giống như việc phản xạ nó qua đường chéo (diagonal). Mỗi phần tử `matrix[r][c]` bên dưới đường chéo sẽ được hoán đổi với phần tử `matrix[c][r]` tại vị trí phản chiếu của nó ở phía trên đường chéo. Vòng lặp `c` trong ví dụ 9.5a chạy từ cột ngoài cùng bên trái cho tới đường chéo. Các phần tử ở ngay trên đường chéo vẫn sẽ không thay đổi.

Vấn đề với mã nguồn này là nếu các phần tử `matrix[r][c]` bên dưới đường chéo được truy cập theo chiều hàng dọc, thì các phần tử phản chiếu `matrix[c][r]` ở trên đường chéo lại được truy cập theo chiều cột đứng.

Giả sử bây giờ chúng ta đang chạy mã nguồn này với một ma trận 64x64 trên một chiếc máy tính Pentium 4, nơi có bộ đệm dữ liệu cấp 1 (level-1) là 8 kb = 8192 byte, 4 chiều (ways), với kích thước dòng bộ đệm là 64. Mỗi dòng bộ nhớ đệm có thể chứa 8 phần tử dạng `double` (với 8 byte cho mỗi phần tử). Khoảng cách tới hạn (critical stride) là 8192 / 4 = 2048 byte = 4 hàng.

Hãy xem điều gì xảy ra bên trong vòng lặp, ví dụ như khi `r = 28`. Chúng ta lấy các phần tử từ hàng 28 bên dưới đường chéo và đổi chỗ các phần tử này cho cột 28 phía trên đường chéo. Tám phần tử đầu tiên trong hàng 28 sẽ dùng chung một dòng bộ nhớ đệm (cache line). Nhưng tám phần tử này sẽ đi vào tám dòng bộ nhớ đệm khác nhau trong cột 28, bởi vì các dòng bộ nhớ đệm đi theo các hàng chứ không phải các cột. Cứ mỗi dòng thứ tư trong các dòng bộ nhớ đệm này lại cùng thuộc chung vào một tập hợp (set) ở trong bộ đệm. Khi chúng ta chạm đến phần tử số 16 trong cột 28, bộ đệm sẽ trục xuất dòng bộ đệm đã được sử dụng bởi phần tử số 0 ở cột này. Phần tử số 17 sẽ trục xuất phần tử 1. Phần tử số 18 sẽ trục xuất phần tử 2, v.v. Điều này có nghĩa là tất cả các dòng bộ đệm chúng ta đã sử dụng phía trên đường chéo đã bị mất đi vào thời điểm mà chúng ta tiến hành hoán đổi cột 29 với hàng 29. Mỗi dòng bộ đệm đều phải nạp lại tám lần vì nó liên tục bị trục xuất trước khi chúng ta cần dùng đến phần tử kế tiếp. Tôi đã xác nhận điều này thông qua việc đo lường thời gian cần thiết để thực hiện hoán vị một ma trận dùng ví dụ 9.5a trên máy Pentium 4 với những kích cỡ ma trận khác nhau. Các kết quả thí nghiệm của tôi được cung cấp ở bên dưới. Đơn vị thời gian là các chu kỳ xung nhịp (clock cycles) trên mỗi phần tử mảng.

| Kích thước ma trận | Tổng kilobyte | Thời gian mỗi phần tử |
| --- | --- | --- |
| 63x63 | 11.6 | 16.4 |
| 64x64 | 16.4 | 11.8 |
| 65x65 | 11.8 | 12.2 |
| 127x127 | 12.2 | 17.4 |
| 128x128 | 17.4 | 14.4 |
| 129x129 | 14.4 | 38.7 |
| 511x511 | 2040 | 230.7 |
| 512x512 | 2048 | 38.1 |
| 513x513 | 2056 | |

*Bảng 9.1 Thời gian thực hiện việc hoán vị cho các ma trận nhiều kích cỡ, tính theo xung chu kỳ đồng hồ (clock cycles) chia cho mỗi phần tử.*

Bảng trên cho thấy rằng cần nhiều hơn 40% thời gian để hoán vị một ma trận khi kích thước của ma trận đó là bội số kích thước của bộ đệm cấp 1. Lý do là vì khoảng cách tới hạn (critical stride) trở thành một bội số cho kích thước dòng ma trận. Độ trễ thấp hơn so với thời gian cần thiết để nạp lại bộ nhớ đệm cấp 1 từ cấp 2 là bởi vì cơ chế thực thi không tuần tự (out-of-order execution) có thể thực hiện lấy dữ liệu trước (prefetch).

Hiệu ứng sẽ trở nên ấn tượng hơn rất nhiều khi các cạnh tranh (contentions) xuất hiện trong không gian bộ đệm cấp 2. Bộ đệm cấp 2 mang 512 kb, 8 chiều (8 ways). Khoảng cách tới hạn (critical stride) của bộ đệm cấp 2 là 512 kb / 8 = 64 kb. Giá trị này tương ứng với 16 dòng trong một bản ma trận 512x512. Các kết quả thí nghiệm của tôi trong bảng 9.1 cho thấy thời gian để hoán đổi một ma trận sẽ gấp sáu lần nếu có các cạnh tranh xảy ra ở bộ đệm cấp 2 so với lúc hiện tượng này vắng mặt. Lý do tại sao hiệu ứng này ảnh hưởng mạnh mẽ hơn rất nhiều đối với các cạnh tranh trên bộ đệm cấp 2 so với bộ đệm cấp 1 là vì bộ đệm cấp 2 không thể nạp trước (prefetch) nhiều hơn một dòng tại một thời điểm.

Một cách đơn giản để giải quyết vấn đề này là làm cho các hàng trong ma trận dài hơn mức cần thiết nhằm tránh trường hợp khoảng cách tới hạn vô tình là một bội số của kích thước dòng ma trận. Tôi đã thử làm cho ma trận thành 512x520 và để lại 8 cột cuối cùng nằm trống không dùng tới. Điều này đã loại bỏ hoàn toàn các tranh chấp cạnh tranh và mức tiêu thụ thời gian đã tụt xuống số 36.

Sẽ có những trường hợp không thể thêm các cột chưa sử dụng vào cho một ma trận. Ví dụ, một thư viện các hàm toán học nên phải hoạt động hiệu quả trên tất cả các kích cỡ ma trận. Một giải pháp hiệu quả trong trường hợp này là chia ma trận thành các hình vuông nhỏ hơn và xử lý lần lượt từng hình vuông một. Kỹ thuật này được gọi là chia khối vuông (square blocking) hoặc lát gạch (tiling). Kỹ thuật trên đã được minh họa rõ ở ví dụ 9.5b.

```cpp
// Example 9.5b 
void transpose(double a[SIZE][SIZE]) { 
   // Define macro to swap two elements: 
   #define swapd(x,y) {temp=x; x=y; y=temp;} 
   // Check if level-2 cache contentions will occur: 
   if (SIZE > 256 && SIZE % 128 == 0) { 
      // Cache contentions expected. Use square blocking: 
      int r1, r2, c1, c2; double temp; 
      // Define size of squares: 
      const int TILESIZE = 8;   // SIZE must be divisible by TILESIZE 
      // Loop r1 and c1 for all squares: 
      for (r1 = 0; r1 < SIZE; r1 += TILESIZE) { 
         for (c1 = 0; c1 < r1; c1 += TILESIZE) { 
            // Loop r2 and c2 for elements inside sqaure: 
            for (r2 = r1; r2 < r1+TILESIZE; r2++) { 
               for (c2 = c1; c2 < c1+TILESIZE; c2++) { 
                  swapd(a[r2][c2],a[c2][r2]); 
               } 
            } 
         } 
         // At the diagonal there is only half a square. 
         // This triangle is handled separately: 
         for (r2 = r1+1; r2 < r1+TILESIZE; r2++) { 
            for (c2 = r1; c2 < r2; c2++) { 
               swapd(a[r2][c2],a[c2][r2]); 
            } 
         } 
      } 
   } 
   else { 
      // No cache contentions. Use simple method. 
      // This is the code from example 9.5a: 
      int r, c;  double temp; 
      for (r = 1; r < SIZE; r++) {    // loop through rows 
         for (c = 0; c < r; c++) {    // loop columns below diagonal 
            swapd(a[r][c], a[c][r]);  // swap elements 
         } 
      } 
  } 
} 
```

Đoạn mã này mất 50 chu kỳ xung nhịp (clock cycles) cho mỗi phần tử đối với một ma trận 512x512 trong các thử nghiệm của tôi.

Các cạnh tranh (contentions) trong bộ đệm cấp 2 là rất đắt đỏ, do đó việc làm một điều gì đó để giải quyết chúng là rất quan trọng. Vì vậy, bạn nên nhận thức được những tình huống mà số lượng các cột trong một ma trận là lũy thừa bậc cao của 2. Các cạnh tranh trong bộ đệm cấp 1 thì ít tốn kém hơn. Việc sử dụng các kỹ thuật phức tạp như square blocking (chia khối vuông) cho bộ đệm cấp 1 có thể không đáng với công sức bỏ ra.

Square blocking và các phương pháp tương tự được mô tả chi tiết hơn trong cuốn sách "Performance Optimization of Numerically Intensive Codes" (Tối ưu hóa Hiệu suất của các Mã Chuyên sâu về Số học), của S. Goedecker và A. Hoisie, SIAM 2001.

