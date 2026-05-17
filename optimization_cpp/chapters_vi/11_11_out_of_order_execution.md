# 11 Thực thi không tuần tự (Out of order execution)

Tất cả các loại CPU x86 hiện đại đều có thể thực thi các tập lệnh theo kiểu không tuần tự hoặc xử lý nhiều việc cùng một lúc, ngoại trừ một số mẫu CPU cỡ nhỏ tiết kiệm điện năng (Intel Atom). Ví dụ sau đây sẽ cho thấy cách để tận dụng lấy ưu thế từ chức năng này:

```cpp
// Example 11.1a 
float a, b, c, d, y; 
y = a + b + c + d; 
```

Biểu thức này được tính toán dưới dạng `((a+b)+c)+d`. Đây là một chuỗi phụ thuộc (dependency chain) nơi mỗi phép cộng đều phải chờ đợi kết quả từ phép cộng diễn ra ngay trước nó. Bạn có thể cải thiện chuyện này bằng cách viết như sau:

```cpp
// Example 11.1b 
float a, b, c, d, y; 
y = (a + b) + (c + d); 
```

Bây giờ hai dấu ngoặc đơn có thể được đem ra tính toán một cách hoàn toàn độc lập với nhau. CPU sẽ bắt tay vào tính cho `(c+d)` trước cả khi nó kịp dứt điểm bài toán `(a+b)`. Điều này có khả năng tiết kiệm được một lượng số chu kỳ xung nhịp. Bạn không được quyền mặc định rằng trình biên dịch tối ưu hóa sẽ tự động biến đoạn mã ở ví dụ 11.1a thành đoạn mã ở 11.1b, dẫu cho cái cách làm đó nhìn chung hiển nhiên là như vậy. Nguyên do khiến cho các trình biên dịch không thực hiện cái trò tối ưu này đối với các biểu thức dấu phẩy động đó là nó có thể dẫn đến việc đánh mất độ chính xác, như đã được giải thích ở trang 73. Việc thiết đặt các dấu ngoặc đơn phải do bạn tự thân vận động.

Tầm ảnh hưởng của một chuỗi xích phụ thuộc sẽ càng đậm đặc một khi chúng mang chiều dài lớn. Đây là tình trạng hay gặp trong các vòng lặp. Cùng phân tích ví dụ sau, chuyên làm nhiệm vụ tính tổng của 100 con số:

```cpp
// Example 11.2a 
const int size = 100; 
float list[size], sum = 0;  int i; 
for (i = 0; i < size; i++) sum += list[i]; 
```

Đoạn mã này đang cõng một chuỗi phụ thuộc kéo rất dài. Giả sử một phép cộng dấu phẩy động sẽ ngốn hết 5 chu kỳ xung nhịp, vậy thì vòng lặp này sẽ tiêu hao một lượng xấp xỉ khoảng 500 chu kỳ xung nhịp. Bạn có thể cải thiện hiệu năng một cách ngoạn mục thông qua phương thức trải phẳng vòng lặp (unrolling the loop) để từ đó chẻ đôi chuỗi phụ thuộc kia ra làm hai nửa:

```cpp
// Example 11.2b 
const int size = 100; 
float list[size], sum1 = 0, sum2 = 0;  int i; 
for (i = 0; i < size; i += 2) { 
   sum1 += list[i]; 
   sum2 += list[i+1];} 
sum1 += sum2; 
```

Nếu bộ vi xử lý đang làm phép cộng nhồi vào `sum1` trong khoảng từ lúc thời điểm T cho tới T+5, thế thì nó cũng có thể đồng thời đẩy phép cộng nhồi cho `sum2` trong quãng từ T+1 đến T+6, và toàn bộ cái vòng lặp giờ đây sẽ chỉ còn ngốn khoảng 256 chu kỳ xung nhịp.

Tình huống tính toán bên trong vòng lặp khi mà mỗi một phiên lặp lại cần dùng tới hệ quả sinh ra từ phiên lặp đi liền trước đó thì được gọi là một chuỗi phụ thuộc do vòng lặp sinh ra (loop-carried dependency chain). Những chuỗi xích liên đới loại này có thể trở nên cực kỳ dai nhách và cũng rất tốn thời gian. Chúng ta có thể gặt hái vô vàn lợi ích nếu những chuỗi phụ thuộc như thế này bị bẻ gãy rời ra. Hai loại biến tính tổng là `sum1` cùng `sum2` được gọi là các bộ tích lũy (accumulators). Các loại CPU trên thị trường hiện tại chỉ có duy nhất một đơn vị lo phần cộng phép tính dấu phẩy động, nhưng bộ phận này được thực thi dưới cấu trúc đường ống (pipelined), giống như giải thích ở phần bên trên, qua đó nó có khả năng khởi tạo một thao tác cộng mới tinh ngay trước lúc phần lệnh cộng sinh trước đó kịp hoàn thành trọn vẹn.

Lượng số tối ưu các bộ tích lũy dùng trong phép cộng và phép nhân cho dấu phẩy động có thể nằm trong mức ba hoặc bốn, còn phải tùy theo từng mẫu CPU.

Công đoạn trải phẳng vòng lặp sẽ trở nên phức tạp hơn một chút nếu lượng số vòng lặp không chia hết cho hệ số trải (unroll factor). Đơn cử, giả sử số lượng phần tử thuộc mảng `list` tại ví dụ 11.2b mang một lượng số lẻ thế thì chúng ta sẽ đành phải cộng nhồi cái phần tử đứng cuối đó vào lúc đã thoát khỏi vòng lặp hoặc chèn thêm một phần tử rỗng (dummy) nằm nối gót trong `list` và cho điểm giá trị của phần tử cấy thêm này nằm ở mốc số không.

Việc trải phẳng vòng lặp cùng với quá trình sử dụng một nhóm các bộ tích lũy là không cần thiết nếu như không hề tồn tại bất kỳ chuỗi phụ thuộc sinh ra do vòng lặp nào (loop-carried dependency chain). Một bộ vi xử lý trang bị trong mình khả năng làm việc không tuần tự (out-of-order) thừa sức đắp chồng (overlap) các phiên lặp với nhau để rồi khởi phát quá trình tính toán của một phiên lặp dẫu cho cái phiên lặp đứng ngay đằng trước chưa hoàn thành xong. Ví dụ:

```cpp
// Example 11.3 
const int size = 100;  int i; 
float a[size], b[size], c[size]; 
float register temp; 
for (i = 0; i < size; i++) { 
   temp = a[i] + b[i]; 
   c[i] = temp * temp; 
} 
```

Các bộ vi xử lý mang đặc trưng thực thi không tuần tự thường khá thông minh. Chúng có khả năng dò ra việc cái mốc giá trị của thanh ghi `temp` thuộc một phiên chạy trong vòng lặp tại ví dụ 11.3 không hề có dây mơ rễ má (độc lập) gì với mức giá trị đã sinh ra từ phiên lặp trước. Sự việc đó cấp quyền cho CPU tiến hành tính luôn một kết quả mới dành cho `temp` trước cả lúc nó xài xong điểm giá trị của lượt ngay trước đó. Cỗ máy đó vận hành trò này thông qua thủ thuật gán thêm hẳn một thanh ghi vật lý mới để thay vào chỗ cho biến `temp` bất chấp việc thanh ghi logic (hiển thị trên tập mã máy) là hệt nhau. Cơ chế này được gọi tên là đổi tên thanh ghi (register renaming). Bộ vi xử lý (CPU) có khả năng cưu mang vô vàn các biến thể đổi tên của duy nhất một kiểu thanh ghi logic định sẵn.

Loại ưu thế như thế này xuất hiện hoàn toàn tự động. Chẳng mảy may tồn tại lý do gì để đi trải phẳng vòng lặp rồi lại phải ôm lấy thêm một cái `temp1` đi kèm cùng `temp2`. Khối CPU hiện đại rất có tiềm năng trong khả năng đổi tên thanh ghi và xử lý nhiều thao tác tính toán ở chung một đường chạy song song giả như có vài điều kiện nhất định được đáp ứng. Những hệ quy chiếu để giúp CPU nhúng tay được vào cái trò đắp đè các khâu tính toán của mọi phiên lặp lên với nhau là:

* Không tồn tại chuỗi xích phụ thuộc do vòng lặp sinh ra. Không có một thứ râu ria gì xuất hiện trong công đoạn tính toán tại một phiên lặp lại phải bấu víu vào phần kết quả của phiên lặp đằng trước (loại trừ bộ đếm vòng lặp, thứ vốn được tính tốc độ lẹ làng khi mà nó là một số nguyên).
* Mọi kết quả trung gian đều phải được lưu trữ trong thanh ghi, chứ không phải bên trong bộ nhớ. Cơ cấu hệ đổi tên (renaming mechanism) chỉ có cửa hoạt động được ở trên thanh ghi, chứ không phải ở trên các biến ngự trị trong bộ nhớ hay khoang đệm (cache). Số đông trình biên dịch sẽ nhào nặn biến `temp` thành một biến thanh ghi (register variable) khi xem lại ví dụ 11.3 bất chấp việc không có từ khóa `register`. Trình biên dịch CodeGear không có khiếu nặn ra các dạng biến mang hệ thanh ghi chứa kết quả dấu phẩy động (floating point register variables), thay vào đó nó sẽ quẳng `temp` ngâm vô trong bộ nhớ chính. Hành vi này ngăn cấm CPU tiến hành đắp đè lên các thao tác tính toán.
* Nhánh điều kiện lặp (loop branch) phải được dự đoán trước. Điều này không có gì phiền toái nếu lượng số được khai báo lặp (repeat count) mang vóc dáng to lớn hoặc mang tính hằng số. Nếu mốc lặp vòng lặp mang dáng hình bé tẹo và luôn chuyển biến thì thi thoảng CPU sẽ phán bừa là quá trình lặp đã thoái trào đóng cửa rời đi, nơi thực tế lại trái ngang (kết luận bị sai), dẫn tới hậu quả là cú đúp trượt ngã không nổ máy cho lượt tính toán sau cùng. Tuy thế, bộ chế tác không tuần tự cấp cho CPU môt quyền năng nhồi thông số bộ đếm trước hạn định thời gian qua đó nó dò thấu được điểm phán mù (misprediction) trước thời khắc hối không kịp. Chính vì lẽ vậy bạn không cần phải quá nhọc lòng ưu phiền xoay quanh vấn đề quy chiếu này.

Tựu chung lại, bộ chế tác thực thi không tuần tự tự thân nó sẽ thực hiện công việc. Tuy vậy, lập trình viên vẫn được phép nhúng tay làm vài việc hòng bóc lột lợi ích triệt để nhất từ hệ tính năng thực thi không tuần tự. Chuyện tối quan trọng nhất nằm ở chỗ phải né đòn khỏi đám rễ chuỗi phụ thuộc kéo dài ngoằn ngoèo. Chuyện nữa mà bạn có tay nghề bấu víu vào đó là nhào nặn pha trộn (mix) đủ dạng phép tính hỗn tạp nhằm rải đều mức việc san bằng cho hệ đầu não thực thi vô hình trong khối CPU. Pha trộn lẫn lộn cả chuỗi phép đếm số nguyên cùng kiểu phép tính cho dạng phẩy động có khả năng tạo ưu thế cực mạnh miễn là bạn không vướng phải chuyện quy đổi chuyển hệ giữa số nguyên với đám số thập phân phẩy động. Cũng khá đem lại ưu thế khi pha trộn phép cộng dấu phẩy động nhào vào phép nhân dấu phẩy động, trộn lẫn các phép tính số nguyên cơ bản với phần toán tử hệ số nguyên vectơ (vector integer operations), đồng thời lôi thêm phép đếm tính toán học quăng trộn với lệnh truy cập bộ nhớ (memory access).
