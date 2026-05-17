# 10 Đa luồng (Multithreading)

| Kích thước ma trận (Matrix size) | Thời gian mỗi phần tử, Ví dụ 9.6a | Thời gian mỗi phần tử, Ví dụ 9.6b |
| --- | --- | --- |
| 64x64 | 14.0 | 80.8 |
| 65x65 | 13.6 | 80.9 |
| 512x512 | 378.7 | 168.5 |
| 513x513 | 58.7 | 168.3 |
*Bảng 9.3 Thời gian để hoán vị và sao chép các ma trận ở nhiều kích cỡ khác nhau, tính theo chu kỳ xung nhịp (clock cycles) trên mỗi phần tử.*

Như bảng 9.3 đã cho thấy, phương pháp lưu trữ dữ liệu mà bỏ qua bộ đệm chỉ mang lại lợi thế khi và chỉ khi có một sự trượt bộ đệm cấp 2 (level-2 cache miss) được đoán trước. Kích thước ma trận 64x64 gây ra những lần trượt ở bộ đệm cấp 1. Sự việc này hầu như không đem tới ảnh hưởng nào đối với tổng thời gian thực thi bởi vì một cú trượt bộ đệm trong quá trình lưu trữ sẽ không làm trì hoãn các lệnh được thực thi tiếp theo. Kích thước ma trận 512x512 gây ra những cú trượt ở bộ đệm cấp 2. Sự kiện này mang tới ảnh hưởng mang tính thảm họa đối với tổng thời gian thực thi do đường truyền bộ nhớ (memory bus) bị bão hòa. Khúc mắc này có thể được xoa dịu thông qua việc xài tới các lệnh viết không tạm thời (nontemporal writes). Nếu các cạnh tranh (contentions) ở bộ đệm có thể được phòng tránh qua các phương thức khác, giống như giải thích ở chương 9.10, thì những lệnh viết không tạm thời sẽ không phải là một giải pháp tối ưu.

Có một vài hạn chế đối với việc sử dụng các chỉ lệnh được liệt kê ở bảng 9.2. Tất cả những chỉ lệnh này đều yêu cầu bộ vi xử lý phải có trong mình tập lệnh SSE hoặc SSE2, như đã được ghi trong bảng. Các lệnh 16-byte như `MOVNTPS`, `MOVNTPD` và `MOVNTDQ` đều yêu cầu hệ điều hành phải hỗ trợ các thanh ghi XMM; hãy xem ở trang 125.

Trình biên dịch của Intel có thể tự động chèn các thao tác viết không tạm thời vào trong đoạn mã đã được vectơ hóa (vectorized code) khi mà lệnh `#pragma vector nontemporal` được xài tới. Dẫu vậy, phương pháp này không có tác dụng đối với ví dụ 9.6b.

Lệnh `MOVNTQ` bắt buộc phải được theo sau bởi một lệnh `EMMS` trước khi tiến hành bất kỳ lệnh dấu phẩy động (floating point instructions) nào. Hành động này được viết bằng đoạn mã `_mm_empty()` giống như đang thể hiện ở ví dụ 9.6b. Lệnh `MOVNTQ` không thể được xài trong các trình điều khiển thiết bị (device drivers) 64-bit thuộc hệ điều hành Windows.


Tần số xung nhịp (clock frequency) của CPU bị giới hạn bởi các yếu tố vật lý. Giải pháp để tăng thông lượng của các chương trình đòi hỏi nhiều CPU khi tần số xung nhịp bị giới hạn là thực hiện nhiều công việc cùng một lúc. Có ba cách để thực thi công việc một cách song song:

* Sử dụng nhiều CPU hoặc các CPU đa lõi (multi-core CPUs), như được mô tả trong chương này.
* Khai thác khả năng thực thi không tuần tự (out-of-order execution) của các CPU hiện đại, như được mô tả trong chương 11.
* Sử dụng các phép toán vectơ (vector operations) của các CPU hiện đại, như được mô tả trong chương 12.

Hầu hết các CPU hiện đại đều có hai hoặc nhiều lõi hơn, và có thể dự đoán rằng số lượng lõi sẽ còn tăng lên trong tương lai. Để sử dụng nhiều CPU hoặc lõi CPU, chúng ta cần chia công việc thành nhiều luồng (threads). Có hai nguyên tắc chính ở đây: phân tách chức năng (functional decomposition) và phân tách dữ liệu (data decomposition). Phân tách chức năng ở đây có nghĩa là các luồng khác nhau sẽ thực hiện các loại công việc khác nhau. Ví dụ, một luồng có thể đảm nhận giao diện người dùng, một luồng khác có thể lo việc giao tiếp với cơ sở dữ liệu từ xa, và luồng thứ ba có thể thực hiện các phép tính toán học. Điều quan trọng là giao diện người dùng không được nằm trong cùng một luồng với các tác vụ rất tốn thời gian, bởi vì điều này sẽ gây ra thời gian phản hồi bị kéo dài và bất thường một cách khó chịu. Việc đưa các tác vụ tốn thời gian vào những luồng riêng biệt có độ ưu tiên thấp (low priority) thường mang lại nhiều lợi ích.

Tuy nhiên, trong nhiều trường hợp, chỉ có một tác vụ duy nhất tiêu thụ hầu hết các tài nguyên. Trong trường hợp này, chúng ta cần chia dữ liệu thành nhiều khối để tận dụng được sức mạnh của nhiều lõi vi xử lý. Mỗi luồng khi đó sẽ xử lý khối dữ liệu của riêng nó. Đây gọi là phân tách dữ liệu (data decomposition).

Điều quan trọng là phải phân biệt được giữa tính song song hạt thô (coarse-grained parallelism) và tính song song hạt mịn (fine-grained parallelism) khi quyết định xem liệu làm mọi việc song song có mang lại lợi ích gì không. Tính song song hạt thô đề cập đến tình huống khi một chuỗi các hoạt động dài có thể được tiến hành độc lập với các tác vụ khác đang chạy song song. Tính song song hạt mịn là tình huống khi một tác vụ được chia thành nhiều tác vụ con nhỏ (subtasks), nhưng không thể thực hiện một tác vụ con cụ thể quá lâu trước khi cần có sự phối hợp (coordination) với các tác vụ con khác.

Đa luồng hoạt động hiệu quả với tính song song hạt thô hơn là với tính song song hạt mịn vì việc giao tiếp và đồng bộ hóa (synchronization) giữa các lõi khác nhau diễn ra rất chậm. Nếu độ phân giải hạt (granularity) quá mịn thì việc chia tách các tác vụ thành nhiều luồng sẽ không mang lại lợi thế. Việc thực thi không tuần tự (chương 11) và các phép toán vectơ (chương 12) là các phương pháp hữu ích hơn để khai thác tính song song hạt mịn.

Cách để tận dụng nhiều lõi CPU là phân chia công việc thành nhiều luồng. Việc sử dụng luồng đã được thảo luận trên trang 61. Trong trường hợp phân rã dữ liệu, tốt nhất là chúng ta không nên có số lượng các luồng với cùng mức độ ưu tiên nhiều hơn số lõi hoặc bộ xử lý logic (logical processors) có sẵn trong hệ thống. Số lượng các bộ xử lý logic có sẵn có thể được xác định bằng một lời gọi hệ thống (ví dụ: `GetProcessAffinityMask` trên Windows).

Có một vài cách để chia nhỏ khối lượng công việc cho nhiều lõi CPU:

* Định nghĩa ra nhiều luồng và đặt một lượng công việc bằng nhau vào mỗi luồng. Phương pháp này hoạt động với mọi trình biên dịch.
* Sử dụng tính năng song song tự động (automatic parallelization). Các trình biên dịch của Gnu, Intel và PathScale có khả năng tự động phát hiện các cơ hội để song song hóa bên trong đoạn mã rồi chia nó ra làm nhiều luồng, nhưng trình biên dịch có thể sẽ không tìm ra được cách phân tách dữ liệu tối ưu nhất.
* Sử dụng các chỉ thị OpenMP (OpenMP directives). OpenMP là một chuẩn quy định về quá trình xử lý song song trong C++ và Fortran. Các chỉ thị này được hỗ trợ bởi các trình biên dịch Microsoft, Intel, PathScale và Gnu. Truy cập www.openmp.org và sổ tay của trình biên dịch để biết thêm chi tiết.
* Sử dụng các thư viện hàm có chức năng đa luồng nội bộ (internal multi-threading), ví dụ như thư viện Intel Math Kernel.

Nhiều lõi CPU hoặc bộ xử lý logic thường dùng chung một bộ nhớ đệm, chí ít là tại cấp bộ nhớ đệm cuối cùng (last cache level), và trong một vài trường hợp có thể dùng chung cả bộ đệm cấp 1. Ưu điểm của việc chia sẻ cùng bộ nhớ đệm là thao tác giao tiếp giữa các luồng diễn ra nhanh hơn và các luồng có thể chia sẻ cùng một đoạn mã hay dữ liệu chỉ đọc (read-only data). Nhược điểm là bộ nhớ đệm sẽ bị lấp đầy nếu các luồng sử dụng các vùng bộ nhớ khác nhau, và sẽ nảy sinh các tranh chấp trên bộ đệm (cache contentions) nếu các luồng cùng viết vào chung những vùng không gian bộ nhớ.

Dữ liệu mang tính chỉ đọc có thể được chia sẻ giữa nhiều luồng với nhau, trong khi dữ liệu bị sửa đổi nên được giữ cách biệt riêng cho mỗi luồng. Việc có hai hoặc nhiều luồng cùng ghi vào một dòng bộ nhớ đệm là một điều không tốt, bởi vì các luồng này sẽ làm mất tính hợp lệ (invalidate) của bộ nhớ đệm thuộc về nhau, dẫn đến hiện tượng trễ nghiêm trọng. Cách dễ dàng nhất để tạo ra dữ liệu cụ thể cho từng luồng là khai báo nó ở trạng thái cục bộ (locally) ngay trong hàm của luồng để nó có thể được lưu trữ vào trong ngăn xếp (stack). Mỗi luồng đều có một ngăn xếp của riêng mình. Ngoài ra, bạn cũng có thể định nghĩa một cấu trúc hoặc lớp để chứa dữ liệu cụ thể cho từng luồng và tạo ra một cá thể (instance) dành riêng cho mỗi luồng. Lớp hoặc cấu trúc này nên được căn chỉnh với ít nhất là kích thước của dòng bộ đệm nhằm hạn chế việc nhiều luồng viết đè lên cùng một dòng đệm. Kích thước dòng đệm thông thường là 64 byte trên các bộ xử lý đương đại. Kích thước dòng đệm có thể lớn hơn (128 hoặc 256 byte) trên các thế hệ vi xử lý tương lai.

Tồn tại rất nhiều phương pháp cho việc giao tiếp và đồng bộ (synchronization) giữa các luồng, chẳng hạn như cờ hiệu (semaphores), khóa tương hỗ (mutexes) cùng hệ thống truyền thông điệp (message systems). Tất cả những phương pháp này đều làm tiêu tốn thời gian. Do đó, phần dữ liệu và tài nguyên nên được sắp xếp sao cho lượng công việc giao tiếp cần thiết giữa các luồng bị giảm xuống mức tối thiểu. Ví dụ, nếu nhiều luồng đang sử dụng chung hàng đợi, danh sách, cơ sở dữ liệu hoặc các cấu trúc dữ liệu khác thì bạn có thể cân nhắc xem liệu có thể cấp cho mỗi luồng một cấu trúc dữ liệu của riêng nó hay không, và sau đó hợp nhất (merge) các cấu trúc dữ liệu lại với nhau ở công đoạn cuối cùng khi tất cả các luồng đã hoàn tất quá trình xử lý dữ liệu tốn kém thời gian.

Khởi chạy nhiều luồng trên một hệ thống có cấu tạo chỉ chứa một bộ xử lý logic sẽ không mang lại ưu thế nào nếu các luồng phải tham gia cạnh tranh cho cùng những loại tài nguyên. Thế nhưng việc đưa các tác vụ tính toán tốn kém thời gian sang một luồng phân cách có độ ưu tiên thấp hơn giao diện người dùng lại là một ý tưởng hay ho. Sẽ rất hữu ích nếu bạn đưa các thao tác truy cập tập tin hay mạng lưới vào trong những luồng riêng rẽ để một luồng có thể tiến hành phần tính toán trong khi một luồng khác mải mê chờ đợi sự phản hồi từ ổ đĩa cứng hay mạng internet.

Các công cụ hỗ trợ phát triển các phần mềm đa luồng đều có sẵn từ phía Intel. Hãy tìm hiểu Intel Technology Journal số tập thứ 11, kỳ xuất bản 4, 2007 (www.intel.com/technology/itj/).

## 10.1 Đa luồng đồng thời (Simultaneous multithreading)
Nhiều loại vi xử lý có khả năng khởi chạy hai luồng cho mỗi lõi. Ví dụ, một bộ xử lý sở hữu 4 lõi có thể chạy đồng thời 8 luồng. Bộ xử lý này có 4 bộ xử lý vật lý nhưng mang tới 8 bộ xử lý logic.

"Siêu phân luồng" (Hyperthreading) là định nghĩa từ hãng Intel ám chỉ quá trình đa luồng đồng thời. Hai luồng đang chạy trên cùng một lõi sẽ luôn luôn cạnh tranh để chiếm các tài nguyên dùng chung, chẳng hạn như bộ nhớ đệm hay đơn vị thực thi (execution units). Nếu có bất kỳ tài nguyên dùng chung nào nằm trong nhóm yếu tố làm cản trở phần hiệu năng thì việc sử dụng chức năng đa luồng đồng thời sẽ không mang đến ưu điểm nào. Ngược lại, mỗi luồng có thể chạy với mức tốc độ chưa bằng phân nửa do những sự trục xuất trên bộ nhớ đệm và các xung đột tài nguyên khác. Tuy nhiên nếu một phần lớn quỹ thời gian lại được dành cho hiện tượng trượt bộ nhớ đệm, lỗi dự đoán rẽ nhánh (branch misprediction) hoặc chuỗi xích phụ thuộc (dependency chains) thì từng luồng sẽ chạy với mức quá nửa tốc độ so với luồng độc lập. Có một ưu điểm khi xài đa luồng đồng thời cho tình huống này, thế nhưng không mang lại gấp đôi hiệu năng. Một luồng chia sẻ phần tài nguyên bên trong bộ lõi cho các luồng khác sẽ luôn luôn phải chạy ở tốc độ chậm hơn so với khi luồng đó chạy đơn độc ở trong cái lõi.

Thường cần thực hiện các cuộc thử nghiệm để xác định xem liệu có ưu thế nào khi xài đa luồng đồng thời hay không trên một phần ứng dụng cụ thể.

Nếu tính năng đa luồng đồng thời không mang lại lợi ích gì thì sẽ rất cần thiết để gọi một số chức năng hệ điều hành nhất định (ví dụ: `GetLogicalProcessorInformation` trên Windows) để xác định xem vi xử lý có cấu tạo đa luồng đồng thời hay không. Nếu có, thì bạn có thể bỏ qua tính năng đa luồng đồng thời thông qua việc chỉ xài những bộ xử lý logic được đánh số chẵn (0, 2, 4, v.v.). Các hệ điều hành cũ hơn còn thiếu đi những chức năng tiên quyết dùng phân biệt lượng bộ xử lý vật lý với bộ xử lý logic.

Hoàn toàn không có cách thức nào để yêu cầu vi xử lý cấp chỉ số ưu tiên cao hơn cho luồng này so với những luồng khác. Chính vì thế, thường hay xảy ra chuyện một luồng có mức ưu tiên ở hạng thấp lại tước đoạt các tài nguyên thuộc về một luồng sở hữu độ ưu tiên cao hơn đang cùng chạy trong chung một không gian lõi. Đảm bảo việc tránh vận hành hai luồng mang khoảng cách về chỉ số ưu tiên quá chênh lệch trong cùng một không gian lõi vi xử lý là trách nhiệm đối với hệ điều hành. Thật không may, các loại hệ điều hành hiện tại chưa đủ khả năng giải quyết rốt ráo bài toán này.

Trình biên dịch của nhà Intel có năng lực kiến tạo ra hai luồng xử lý nơi một luồng được dùng vào nhiệm vụ nạp trước dữ liệu (prefetching) cung cấp cho luồng xử lý thứ hai. Thế nhưng, tính năng tự động nạp trước của cơ sở phần cứng lại làm việc hiệu quả hơn việc nạp trước bằng phần mềm (software prefetching) trong đa phần mọi trường hợp.
