# Chương 12: Kiểm thử (Benchmarking)

> *Có những lời nói dối, những lời nói dối chết tiệt và sau đó là các phép đo hiệu năng.*
> —Anon và cộng sự, “A Measure of Transaction Processing Power” [Anon 85]

Kiểm thử (Benchmarking) kiểm tra hiệu năng theo một cách thức được kiểm soát, cho phép các lựa chọn được so sánh, các sự sụt giảm hiệu năng (regressions) được nhận diện, và các giới hạn hiệu năng được thấu hiểu—trước khi chúng gặp phải trong sản xuất. Những giới hạn này có thể là các tài nguyên hệ thống, các giới hạn phần mềm trong một môi trường ảo hóa (điện toán đám mây), hoặc các giới hạn trong ứng dụng mục tiêu. Các chương trước đã khám phá những thành phần này, mô tả các loại giới hạn hiện diện và các công cụ được sử dụng để phân tích chúng.

Các chương trước cũng đã giới thiệu các công cụ cho *micro-benchmarking*, thứ sử dụng các khối lượng công việc nhân tạo đơn giản chẳng hạn như I/O hệ thống tập tin để kiểm tra các thành phần. Cũng có *macro-benchmarking*, thứ mô phỏng các khối lượng công việc máy khách để kiểm tra toàn bộ hệ thống. Macro-benchmarking có thể liên quan đến một sự mô phỏng khối lượng công việc máy khách, hoặc một lần phát lại truy vết (trace replay). Bất kể bạn sử dụng loại nào, điều quan trọng là phải phân tích benchmark sao cho bạn có thể xác nhận những gì đang được đo lường. Benchmarks chỉ cho bạn biết hệ thống có thể chạy benchmark nhanh như thế nào; việc hiểu kết quả và xác định cách nó áp dụng cho môi trường của bạn là tùy thuộc vào bạn.

Các mục tiêu học tập của chương này là:
- Hiểu micro-benchmarking và macro-benchmarking.
- Trở nên nhận thức được vô số các thất bại benchmarking cần tránh.
- Tuân theo một phương pháp luận benchmarking tích cực.
- Sử dụng một benchmarking checklist để kiểm tra các kết quả.
- Phát triển sự chính xác khi thực hiện và diễn giải các benchmarks.

Chương này thảo luận về benchmarking nói chung, cung cấp các lời khuyên và phương pháp luận để giúp bạn tránh các sai lầm phổ biến và kiểm tra các hệ thống của bạn một cách chính xác. Đây cũng là nền tảng hữu ích khi bạn cần diễn giải các kết quả từ những người khác, bao gồm các benchmarks từ nhà cung cấp và từ ngành công nghiệp.

## 12.1 Nền tảng (Background)
Phần này mô tả các hoạt động benchmarking và benchmarking hiệu quả, và tóm tắt các sai lầm phổ biến.

### 12.1.1 Các lý do (Reasons)
Benchmarking có thể được thực hiện vì những lý do sau đây:
- **Thiết kế hệ thống (System design):** So sánh các hệ thống, các thành phần hệ thống, hoặc các ứng dụng khác nhau. Đối với các sản phẩm thương mại, benchmarking có thể cung cấp dữ liệu để hỗ trợ một quyết định mua sắm, cụ thể là tỷ lệ *price/performance* của các lựa chọn có sẵn. Trong một số trường hợp, các kết quả từ các *industry benchmarks* đã được công bố có thể được sử dụng, thứ tránh nhu cầu cho các khách hàng phải tự mình thực thi các benchmarks.
- **Bằng chứng khái niệm (Proofs of concept):** Để kiểm tra hiệu năng của phần mềm hoặc phần cứng dưới tải, trước khi mua hoặc cam kết triển khai sản xuất.
- **Tinh chỉnh (Tuning):** Kiểm tra các tham số tinh chỉnh và các lựa chọn cấu hình, để nhận diện những thứ đáng để điều tra thêm với khối lượng công việc sản xuất.
- **Phát triển (Development):** Cho cả *non-regression testing* (kiểm tra không hồi quy) và *limit investigations* (điều tra giới hạn) trong quá trình phát triển sản phẩm. Non-regression testing có thể là một chuỗi các bài kiểm tra hiệu năng tự động chạy thường xuyên, sao cho bất kỳ sự sụt giảm hiệu năng nào cũng có thể được phát hiện sớm và nhanh chóng khớp với thay đổi sản phẩm. Đối với limit investigations, benchmarking có thể được sử dụng để thúc đẩy các sản phẩm tới giới hạn của chúng trong quá trình phát triển, nhằm nhận diện nơi nỗ lực kỹ thuật được dành ra tốt nhất để cải thiện hiệu năng sản phẩm.
- **Quy hoạch dung lượng (Capacity planning):** Xác định các giới hạn của hệ thống và ứng dụng cho quy hoạch dung lượng, hoặc để cung cấp dữ liệu cho việc mô phỏng hiệu năng, hoặc để tìm kiếm các giới hạn dung lượng một cách trực tiếp.
- **Xử lý sự cố (Troubleshooting):** Để xác minh rằng các thành phần vẫn có thể vận hành tại hiệu năng tối đa. Ví dụ: kiểm tra thông lượng mạng tối đa giữa các hosts để kiểm tra liệu có thể có một vấn đề mạng hay không.
- **Tiếp thị (Marketing):** Xác định hiệu năng sản phẩm tối đa để sử dụng bởi bộ phận tiếp thị (cũng được gọi là *benchmarketing*).

Trong các môi trường tại chỗ của doanh nghiệp, benchmarking phần cứng trong quá trình proofs of concept có thể là một bài tập quan trọng trước khi cam kết một đợt mua sắm phần cứng lớn, và có thể là một quá trình kéo dài nhiều tuần hoặc nhiều tháng. Điều này bao gồm thời gian vận chuyển, lắp giá kệ, và các hệ thống cáp, và sau đó cài đặt các hệ điều hành trước khi kiểm tra. Một quá trình như vậy có thể xảy ra mỗi một hoặc hai năm một lần, khi phần cứng mới được phát hành.

Trong các môi trường điện toán đám mây, tuy nhiên, các tài nguyên có sẵn theo nhu cầu mà không cần sự đầu tư ban đầu tốn kém vào phần cứng, và cũng có thể được sửa đổi nhanh chóng khi cần thiết (tái triển khai trên các loại thực thể khác nhau). Những môi trường này vẫn liên quan đến các khoản đầu tư dài hạn hơn khi lựa chọn ngôn ngữ lập trình ứng dụng nào để sử dụng, và hệ điều hành, cơ sở dữ liệu, máy chủ web, và trình cân bằng tải nào để chạy. Một số trong những lựa chọn này có thể khó để thay đổi về sau. Benchmarking có thể được thực hiện để điều tra xem các lựa chọn khác nhau có thể mở rộng quy mô tốt như thế nào khi cần thiết. Mô hình điện toán đám mây khiến benchmarking trở nên dễ dàng: một môi trường quy mô lớn có thể được tạo ra trong vài phút, được sử dụng cho một lần chạy benchmark, và sau đó bị hủy bỏ, tất cả đều với một mức chi phí rất thấp.

Lưu ý rằng một môi trường đám mây phân tán và có khả năng chịu lỗi cũng khiến cho việc thực nghiệm trở nên dễ dàng: khi các loại thực thể mới được làm sẵn có, môi trường có thể cho phép kiểm tra chúng ngay lập tức với các khối lượng công việc sản xuất, bỏ qua một đợt đánh giá benchmarking truyền thống. Trong kịch bản đó, benchmarking vẫn có thể được sử dụng để giúp giải thích các sự khác biệt hiệu năng chi tiết hơn, bằng cách so sánh hiệu năng thành phần. Ví dụ, nhóm kỹ sư hiệu năng Netflix đã tự động hóa phần mềm cho việc phân tích các loại thực thể mới với một loạt các micro-benchmarks. Điều này bao gồm việc thu thập tự động các thống kê hệ thống và CPU profiles sao cho bất kỳ sự khác biệt nào được tìm thấy đều có thể được phân tích và giải thích.

### 12.1.2 Benchmarking Hiệu quả (Effective Benchmarking)
Benchmarking là cực kỳ khó khăn để thực hiện tốt, với nhiều cơ hội cho các sai lầm và sơ suất. Như đã được tóm tắt bởi bài báo “A Nine Year Study of File System and Storage Benchmarking” [Traeger 08]:

> Trong bài báo này chúng tôi khảo sát 415 benchmarks hệ thống tập tin và lưu trữ từ 106 bài báo gần đây. Chúng tôi thấy rằng hầu hết các benchmarks phổ biến đều có sai sót và nhiều bài báo nghiên cứu đã không cung cấp một chỉ báo rõ ràng về hiệu năng thực sự.

Bài báo cũng đưa ra các khuyến nghị cho những gì nên được thực hiện; cụ thể, các đánh giá benchmark nên giải thích *cái gì* đã được kiểm tra và *tại sao*, và họ nên thực hiện một số phân tích về hành vi dự kiến của hệ thống.

Bản chất của một benchmark tốt cũng đã được tóm tắt bởi [Smaalders 06]:
- **Có thể lặp lại (Repeatable):** Để tạo điều kiện thuận lợi cho các sự so sánh
- **Có thể quan sát (Observable):** Sao cho hiệu năng có thể được phân tích và thấu hiểu
- **Có thể di động (Portable):** Để cho phép benchmarking trên các đối thủ cạnh tranh và qua các đợt phát hành sản phẩm khác nhau
- **Dễ dàng trình bày (Easily presented):** Sao cho mọi người đều có thể hiểu các kết quả
- **Thực tế (Realistic):** Sao cho các phép đo phản ánh các thực tế mà khách hàng trải nghiệm
- **Có thể thực thi (Runnable):** Sao cho các nhà phát triển có thể nhanh chóng kiểm tra các thay đổi

Một đặc tính khác phải được thêm vào khi so sánh các hệ thống khác nhau với ý định mua sắm: tỷ lệ *price/performance*. Giá cả có thể được định lượng như chi phí vốn năm năm của thiết bị [Anon 85].

Benchmarking hiệu quả cũng là về cách bạn áp dụng benchmark: quá trình phân tích và các kết luận được đưa ra.

**Phân tích Benchmark (Benchmark Analysis)**
Khi sử dụng các benchmarks, bạn cần hiểu:
- Cái gì đang được kiểm tra
- Yếu tố hoặc các yếu tố hạn chế là gì
- Bất kỳ sự nhiễu loạn nào có thể ảnh hưởng đến các kết quả
- Những kết luận nào có thể được rút ra từ các kết quả

Những nhu cầu này yêu cầu một sự thấu hiểu sâu sắc về những gì phần mềm benchmark đang thực hiện, cách hệ thống đang phản hồi, và các kết quả liên quan như thế nào tới môi trường đích.

Với một công cụ benchmark và quyền truy cập vào hệ thống chạy nó, những nhu cầu này được phục vụ tốt nhất bởi phân tích hiệu năng của hệ thống trong khi benchmark đang chạy. Một sai lầm phổ biến là để các nhân viên ít kinh nghiệm thực thi các benchmarks, sau đó mang đến các chuyên gia hiệu năng để giải thích các kết quả sau khi benchmark đã hoàn thành. Tốt nhất là thu hút các chuyên gia hiệu năng trong quá trình benchmark sao cho họ có thể phân tích hệ thống trong khi nó vẫn đang chạy. Việc này có thể bao gồm phân tích drill-down để giải thích và định lượng (các) yếu tố hạn chế.

Sau đây là một ví dụ thú vị về phân tích:

> Như một thực nghiệm để điều tra hiệu năng của việc triển khai TCP/IP kết quả, chúng tôi đã truyền tải 4 Megabytes dữ liệu giữa hai tiến trình người dùng trên các máy khác nhau. Việc truyền tải được phân chia thành các bản ghi 1024 byte và được đóng gói trong 1068 byte gói tin Ethernet. Việc gửi dữ liệu từ chiếc 11/750 của chúng tôi tới chiếc 11/780 của chúng tôi qua TCP/IP mất 28 giây. Điều này bao gồm tất cả thời gian cần thiết để thiết lập và phá bỏ các kết nối, cho một thông lượng giữa người dùng-với-người dùng là 1.2 Megabaud. Trong thời gian này chiếc 11/750 là CPU bị bão hòa, nhưng chiếc 11/780 có khoảng 30% thời gian rảnh rỗi. Thời gian dành cho hệ thống để xử lý dữ liệu được trải rộng giữa việc xử lý cho Ethernet (20%), xử lý gói tin IP (10%), xử lý TCP (30%), checksum (25%), và xử lý lệnh gọi hệ thống của người dùng (15%), không có phần đơn lẻ nào của việc xử lý chiếm ưu thế về thời gian trong hệ thống.

Trích dẫn này mô tả việc kiểm tra các yếu tố hạn chế ("chiếc 11/750 là CPU bị bão hòa"), sau đó giải thích các chi tiết của các thành phần kernel gây ra chúng. Như một nội dung bên lề, việc có thể thực hiện phân tích này và tóm tắt nơi thời gian CPU kernel được dành cho ở mức độ cao chỉ mới trở nên dễ dàng gần đây với việc sử dụng flame graphs. Trích dẫn này có trước flame graphs lâu đời: nó là của Bill Joy mô tả nguyên bản chồng BSD TCP/IP vào năm 1981 [Joy 81]!

Thay vì sử dụng một công cụ benchmark có sẵn, bạn có thể thấy hiệu quả hơn khi phát triển công cụ benchmark tùy chỉnh của riêng bạn, hoặc ít nhất là các trình tạo tải (load generators) tùy chỉnh. Những thứ này có thể được giữ ngắn gọn, tập trung vào chỉ những gì cần thiết cho bài kiểm tra của bạn, giúp chúng nhanh chóng để phân tích và gỡ lỗi.

Trong một số trường hợp bạn không có quyền truy cập vào công cụ benchmark hoặc hệ thống, chẳng hạn như khi đọc các kết quả benchmark từ những người khác. Hãy cân nhắc danh sách các điểm trước đó dựa trên các tài liệu có sẵn, và ngoài ra, hãy hỏi, Môi trường hệ thống là gì? Nó được cấu hình như thế nào? Xem Mục 12.4, Các câu hỏi về Benchmark, để biết thêm các câu hỏi.

### 12.1.3 Các thất bại Benchmarking (Benchmarking Failures)
Các phần sau đây cung cấp một checklist về các thất bại benchmarking khác nhau—các sai lầm, các ngụy biện, và các hành vi sai trái—và cách để tránh chúng. Mục 12.3, Phương pháp luận, mô tả cách thực hiện benchmarking.

**1. Benchmarking Tùy tiện (Casual Benchmarking)**
Thực hiện benchmarking tốt không phải là một hoạt động kiểu "fire-and-forget" (khởi động rồi để đó). Các công cụ benchmark cung cấp các con số, nhưng những con số đó có thể không phản ánh những gì bạn nghĩ rằng chúng đang thực hiện, và các kết luận của bạn về chúng do đó có thể là giả mạo. Tôi tóm tắt nó như sau:

> Casual benchmarking: bạn benchmark A, nhưng thực tế đo lường B, và kết luận rằng bạn đã đo lường C.

Benchmarking tốt yêu cầu sự nghiêm ngặt để kiểm tra những gì thực sự được đo lường và một sự hiểu biết về những gì đã được kiểm tra nhằm hình thành các kết luận có giá trị.

Ví dụ, nhiều công cụ tuyên bố hoặc ám chỉ rằng họ đo lường hiệu năng đĩa, nhưng thực tế lại kiểm tra hiệu năng hệ thống tập tin. Sự khác biệt có thể lên tới các bậc độ lớn, vì các hệ thống tập tin sử dụng đệm ẩn và buffering để thay thế đĩa I/O bằng bộ nhớ I/O. Ngay cả khi công cụ benchmark có thể đang hoạt động chính xác và kiểm tra hệ thống tập tin, các kết luận của bạn về các đĩa sẽ là sai một cách điên rồ.

Việc hiểu các benchmarks là đặc biệt khó khăn đối với những người mới bắt đầu, những người không có bản năng để nhận ra liệu các con số có đáng nghi hay không. Nếu bạn mua một chiếc nhiệt kế hiển thị nhiệt độ của căn phòng bạn đang ở là 1,000 độ Fahrenheit (hoặc Celsius), bạn sẽ ngay lập tức biết rằng có điều gì đó không ổn. Điều tương tự không đúng với các benchmarks, thứ tạo ra các con số có lẽ là xa lạ với bạn.

**2. Niềm tin Mù quáng (Blind Faith)**
Có thể là cám dỗ để tin rằng một công cụ benchmark phổ biến là đáng tin cậy, đặc biệt nếu nó là mã nguồn mở và đã tồn tại trong một thời gian dài. Quan niệm sai lầm rằng sự phổ biến tương đương với tính hợp lệ được gọi là *argumentum ad populum* (tiếng Latin cho "appeal to the people").

Phân tích các benchmarks bạn đang sử dụng là tiêu tốn thời gian và yêu cầu chuyên môn để thực hiện một cách đúng đắn. Và, đối với một benchmark phổ biến, nó có vẻ lãng phí khi phân tích những gì *chắc chắn* phải là hợp lệ.

Nếu một benchmark phổ biến được quảng bá bởi một trong những công ty hàng đầu về công nghệ, bạn có tin tưởng nó không? Điều này đã từng xảy ra trong quá khứ khi mà những kỹ sư hiệu năng kỳ cựu đã biết rằng micro-benchmark được quảng bá đó là sai lầm và lẽ ra không bao giờ nên được sử dụng. Không có cách nào dễ dàng để ngăn chặn điều đó xảy ra (tôi đã thử).

Vấn đề thậm chí không nhất thiết nằm ở phần mềm benchmark—mặc dù các lỗi vẫn xảy ra—mà nằm ở sự diễn giải của các kết quả của benchmark.

**3. Các con số mà Không có Phân tích (Numbers Without Analysis)**
Các kết quả benchmark thô, được cung cấp mà không có các chi tiết phân tích, có thể là một dấu hiệu cho thấy tác giả thiếu kinh nghiệm và đã giả định rằng các kết quả benchmark là đáng tin cậy và cuối cùng. Thông thường, đây chỉ là khởi đầu của một cuộc điều tra—một cuộc điều tra cuối cùng tìm thấy các kết quả là sai hoặc gây nhầm lẫn.

Mỗi con số benchmark nên được đi kèm với một mô tả về giới hạn gặp phải và phân tích đã được thực hiện. Tôi đã tóm tắt rủi ro này theo cách này:

> Nếu bạn dành ít hơn một tuần để nghiên cứu một kết quả benchmark, nó có thể là sai.

Phần lớn nội dung của cuốn sách này tập trung vào phân tích hiệu năng, thứ nên được thực hiện trong quá trình benchmarking. Trong các trường hợp bạn không có thời gian cho phân tích cẩn thận, ý tưởng tốt là liệt kê các giả định mà bạn đã không có thời gian để kiểm tra và bao gồm chúng cùng với các kết quả, ví dụ:
- Giả định rằng công cụ benchmark không có lỗi
- Giả định rằng bài kiểm tra đĩa I/O thực sự đo lường đĩa I/O
- Giả định rằng công cụ benchmark đã đẩy đĩa I/O tới giới hạn của nó, như ý định
- Giả định rằng loại đĩa I/O này là phù hợp cho ứng dụng này

Điều này có thể trở thành một danh sách các việc cần làm (to-do list) cho việc xác minh thêm, nếu kết quả benchmark sau đó được coi là đủ quan trọng để dành thêm nỗ lực vào đó.

**4. Các công cụ Benchmark Phức tạp (Complex Benchmark Tools)**
Điều quan trọng là công cụ benchmark không gây cản trở việc phân tích benchmark do chính độ phức tạp của nó. Lý tưởng nhất, chương trình là mã nguồn mở sao cho nó có thể được nghiên cứu, và đủ ngắn gọn để nó có thể được đọc và hiểu nhanh chóng.

Đối với micro-benchmarks, khuyến nghị là chọn những cái được viết bằng ngôn ngữ lập trình C. Cho việc mô phỏng khối lượng công việc máy khách, khuyến nghị là sử dụng cùng ngôn ngữ lập trình của máy khách, để giảm thiểu các sự khác biệt.

Một vấn đề phổ biến là một vấn đề về *benchmarking the benchmark*—nơi hiệu năng được báo cáo bị giới hạn bởi chính bản thân phần mềm benchmark. Một nguyên nhân phổ biến của việc này là phần mềm benchmark đơn luồng (single-threaded). Các bộ benchmark phức tạp có thể làm cho việc phân tích trở nên khó khăn do khối lượng mã cần thấu hiểu và phân tích.

**5. Kiểm tra Sai Thứ (Testing the Wrong Thing)**
Trong khi có vô số công cụ benchmark có sẵn để kiểm tra nhiều loại khối lượng công việc, nhiều cái trong số chúng có thể không liên quan đến ứng dụng mục tiêu.

Ví dụ, một sai lầm phổ biến là kiểm tra hiệu năng đĩa—dựa trên tính sẵn có của các công cụ benchmark đĩa—ngay cả khi khối lượng công việc môi trường mục tiêu được kỳ vọng sẽ chạy hoàn toàn từ file system cache và không bị ảnh hưởng bởi đĩa I/O.

Tương tự, một nhóm kỹ sư phát triển một sản phẩm có thể chuẩn hóa trên một benchmark cụ thể và dành tất cả nỗ lực hiệu năng của họ để cải thiện hiệu năng như được đo lường bởi benchmark đó. Nếu nó không thực sự giống với các khối lượng công việc của khách hàng, tuy nhiên, nỗ lực kỹ thuật sẽ tối ưu hóa cho hành vi sai lầm [Smaalders 06].

Đối với một môi trường sản xuất hiện có, phương pháp luận đặc tính hóa khối lượng công việc (đã bao quát trong các chương trước) có thể đo lường thành phần của khối lượng công việc thực sự từ thiết bị I/O tới các yêu cầu ứng dụng. Những phép đo này có thể hướng dẫn bạn chọn các benchmarks phù hợp nhất. Không có một môi trường sản xuất để phân tích, bạn có thể thiết lập các mô phỏng để phân tích, hoặc mô hình hóa khối lượng công việc dự kiến. Đồng thời kiểm tra với đối tượng mục tiêu của dữ liệu benchmark để xem liệu họ có đồng ý với các bài kiểm tra hay không.

Một benchmark có thể đã kiểm tra một khối lượng công việc phù hợp một lần cách đây rất lâu nhưng hiện nay chưa được cập nhật trong nhiều năm và đang kiểm tra một thứ sai lầm.

**6. Bỏ qua Môi trường (Ignoring the Environment)**
Môi trường sản xuất có khớp với môi trường kiểm tra không? Hãy tưởng tượng bạn được giao nhiệm vụ đánh giá một cơ sở dữ liệu mới. Bạn cấu hình một máy chủ kiểm tra và chạy một benchmark cơ sở dữ liệu, chỉ để sau đó nhận ra rằng bạn đã bỏ lỡ một bước quan trọng: máy chủ kiểm tra của bạn là một thiết lập mặc định với các tham số tinh chỉnh mặc định, hệ thống tập tin mặc định, v.v. Các máy chủ cơ sở dữ liệu sản xuất được tinh chỉnh cho IOPS đĩa cao, vì vậy việc kiểm tra trên một hệ thống không được tinh chỉnh là phi thực tế: bạn đã bỏ lỡ bước đầu tiên là thấu hiểu môi trường sản xuất.

**7. Bỏ qua các Lỗi (Ignoring Errors)**
Chỉ vì một kết quả benchmark được tạo ra không có nghĩa là kết quả đó phản ánh một bài kiểm tra *thành công*. Một số—hoặc thậm chí tất cả—các yêu cầu có thể đã dẫn đến một lỗi. Trong khi vấn đề này được bao quát bởi các sai lầm trước đó, cái này cụ thể là rất phổ biến đến mức nó đáng để được nêu riêng.

Tôi đã được nhắc nhở về điều này trong một đợt kiểm tra hiệu năng máy chủ web. Những người chạy bài kiểm tra đã báo cáo rằng độ trễ trung bình của máy chủ web là quá cao cho các nhu cầu của họ: trên một giây, *trung bình*. Một giây? Một phân tích nhanh đã xác định điều gì không ổn: máy chủ web đã không làm gì cả trong quá trình kiểm tra, vì tất cả các yêu cầu đều bị chặn bởi một tường lửa. *Tất cả* các yêu cầu. Độ trễ hiển thị là thời gian máy khách benchmark cần để hết thời gian chờ (time out) và báo lỗi!

**8. Bỏ qua Biến động (Ignoring Variance)**
Các công cụ benchmark, đặc biệt là micro-benchmarks, thường áp dụng một khối lượng công việc ổn định và nhất quán, dựa trên mức *trung bình* của một chuỗi các phép đo thực tế, chẳng hạn như vào các thời điểm khác nhau trong ngày hoặc trong một khoảng thời gian. Ví dụ, một khối lượng công việc đĩa có thể được tìm thấy là có tốc độ trung bình 500 lần đọc/giây và 50 lần ghi/giây. Một công cụ benchmark sau đó có thể hoặc mô phỏng tốc độ này hoặc mô phỏng tỷ lệ 10:1 đọc/ghi, sao cho tốc độ cao hơn có thể được kiểm tra.

Cách tiếp cận này bỏ qua *variance* (biến động): tốc độ của các thao tác có thể thay đổi. Các loại thao tác cũng có thể thay đổi, và một số loại có thể xảy ra theo hướng vuông góc (orthogonally). Ví dụ, các lệnh ghi có thể được áp dụng theo các đợt bùng phát (bursts) sau mỗi 10 giây (ghi dữ liệu write-back bất đồng bộ), trong khi các lệnh đọc là ổn định. Các đợt bùng phát ghi có thể gây ra các vấn đề thực sự trong sản xuất, chẳng hạn như bằng cách xếp hàng các lệnh đọc, nhưng không được mô phỏng nếu benchmark chỉ áp dụng các tốc độ trung bình ổn định.

Một giải pháp khả thi để mô phỏng biến động là việc sử dụng một mô hình Markov bởi benchmark: điều này có thể phản ánh xác suất rằng một lệnh ghi sẽ được theo sau bởi một lệnh ghi khác.

**9. Bỏ qua các Nhiễu loạn (Ignoring Perturbations)**
Cân nhắc những gì các kết quả bên ngoài có thể đang ảnh hưởng. Liệu có một hoạt động hệ thống theo lịch trình, chẳng hạn như một bản sao lưu hệ thống, thực thi trong quá trình benchmark không? Các tác vụ giám sát có thu thập các thống kê mỗi phút một lần không? Đối với đám mây, một sự nhiễu loạn có thể được gây ra bởi các bên thuê không nhìn thấy được trên cùng một hệ thống host.

Một chiến lược phổ biến để loại bỏ các nhiễu loạn là làm cho benchmark chạy lâu hơn—hàng chục phút thay vì hàng giây. Theo quy tắc, thời lượng của một benchmark không nên ngắn hơn một giây. Các bài kiểm tra ngắn có thể bị ảnh hưởng bất thường bởi các ngắt thiết bị (ghim luồng trong khi thực hiện các thói quen dịch vụ ngắt), các quyết định lập lịch CPU của kernel (chờ đợi trước khi di chuyển các luồng đã xếp hàng để bảo toàn affinity của CPU), và các hiệu ứng làm ấm bộ đệm ẩn CPU. Hãy thử chạy benchmark kiểm tra vài lần và kiểm tra độ lệch tiêu chuẩn (standard deviation)—điều này nên nhỏ nhất có thể.

Đồng thời thu thập dữ liệu sao cho các nhiễu loạn, nếu hiện diện, có thể được nghiên cứu. Điều này có thể bao gồm việc thu thập phân phối của độ trễ thao tác—không chỉ thời gian chạy tổng cộng cho benchmark—sao cho các giá trị ngoại lai có thể được nhìn thấy và các chi tiết của chúng được ghi lại.

**10. Thay đổi Nhiều Yếu tố (Changing Multiple Factors)**
Khi so sánh các kết quả benchmark từ hai bài kiểm tra, hãy cẩn thận để hiểu tất cả các yếu tố khác biệt giữa hai bài.

Ví dụ, nếu hai host được đánh giá qua mạng, liệu mạng giữa chúng có giống hệt nhau không? Nếu một host có nhiều hops hơn, qua một mạng chậm hơn, hoặc qua một mạng bị tắc nghẽn hơn thì sao? Bất kỳ yếu tố bổ sung nào như vậy cũng có thể làm cho kết quả benchmark trở nên giả mạo.

Trong đám mây, các benchmarks đôi khi được thực hiện bằng cách tạo ra các thực thể, kiểm tra chúng, và sau đó hủy bỏ chúng. Điều này tạo ra tiềm năng cho nhiều yếu tố không lường trước được: các thực thể có thể được tạo ra trên các hệ thống nhanh hơn hoặc chậm hơn, hoặc trên các hệ thống có tải và tranh chấp cao hơn hoặc thấp hơn từ các bên thuê khác. Tôi khuyên bạn nên kiểm tra nhiều thực thể và lấy trung bình (hoặc tốt hơn, ghi lại phân phối) để tránh các giá trị ngoại lai gây ra bởi việc kiểm tra một hệ thống nhanh hoặc chậm một cách bất thường.

**11. Nghịch lý Benchmark (Benchmark Paradox)**
Các benchmarks thường được sử dụng bởi các khách hàng tiềm năng để đánh giá sản phẩm của bạn, và chúng thường không chính xác đến mức bạn có thể chỉ cần tung đồng xu. Một nhân viên bán hàng từng nói với tôi rằng anh ta sẽ hạnh phúc với những tỷ lệ cược đó: chiến thắng một nửa số đợt đánh giá sản phẩm của mình sẽ đạt được các mục tiêu doanh số của anh ta. Nhưng việc phớt lờ các benchmarks là một cạm bẫy benchmarking, và tỷ lệ cược trong thực tế còn tệ hơn nhiều. Tôi đã tóm tắt nó như sau:

> “Nếu cơ hội chiến thắng một benchmark của sản phẩm của bạn là 50/50, bạn sẽ thường thất bại.”
> [Gregg 14c]

Nghịch lý dường như này có thể được giải thích bằng một số xác suất đơn giản.

Khi mua một sản phẩm dựa trên hiệu năng, các khách hàng thường muốn thực sự chắc chắn rằng nó mang lại hiệu năng cao. Điều đó có thể có nghĩa là không chỉ chạy một benchmark, mà là vài cái, và muốn sản phẩm chiến thắng *tất cả*. Nếu một benchmark có 50% xác suất chiến thắng, thì:

Xác suất chiến thắng ba benchmarks = 0.5 × 0.5 × 0.5 = 0.125 = 12.5%

Càng nhiều benchmarks—với yêu cầu chiến thắng tất cả chúng—thì cơ hội càng tệ.

**12. Benchmarking Đối thủ cạnh tranh (Benchmarking the Competition)**
Bộ phận tiếp thị của bạn sẽ thích các kết quả benchmark cho thấy sản phẩm của bạn đánh bại đối thủ cạnh tranh. Điều này khó khăn hơn nhiều so với âm hưởng của nó.

Khi khách hàng chọn một sản phẩm, họ không sử dụng nó trong năm phút; họ sử dụng nó trong nhiều tháng. Trong thời gian đó, họ phân tích và tinh chỉnh sản phẩm cho hiệu năng, có lẽ rũ bỏ các kết quả tồi tệ nhất ở giai đoạn đầu.

Bạn không có vài tuần để dành cho việc phân tích và tinh chỉnh *đối thủ cạnh tranh* của mình. Trong thời gian có sẵn, bạn chỉ có thể thu thập các kết quả chưa được tinh chỉnh—và do đó không thực tế. Các khách hàng của đối thủ cạnh tranh—mục tiêu của hoạt động tiếp thị này—có thể thấy rằng bạn đã đăng tải các kết quả chưa được tinh chỉnh, vì vậy công ty của bạn mất đi uy tín với chính những người mà nó đang cố gắng gây ấn tượng.

Nếu bạn phải benchmark đối thủ cạnh tranh, bạn sẽ cần dành thời gian nghiêm túc để tinh chỉnh sản phẩm của họ. Phân tích hiệu năng bằng cách sử dụng các kỹ thuật đã mô tả trong các chương trước. Đồng thời tìm kiếm các thực tiễn tốt nhất, các diễn đàn khách hàng, và các cơ sở dữ liệu lỗi. Bạn thậm chí có thể muốn đưa vào các chuyên gia bên ngoài để tinh chỉnh hệ thống. Sau đó hãy đảm bảo rằng cùng một nỗ lực đó được dành cho công ty của chính bạn trước khi bạn cuối cùng thực hiện các benchmarks đối đầu (head-to-head).

**13. Quân ta đánh quân mình (Friendly Fire)**
Khi benchmarking các sản phẩm của chính bạn, hãy nỗ lực hết sức để đảm bảo rằng hệ thống và cấu hình có hiệu năng cao nhất đã được kiểm tra, và hệ thống đã được đẩy tới giới hạn thực sự của nó. Hãy chia sẻ các kết quả với nhóm kỹ sư trước khi công bố; họ có thể phát hiện ra các mục cấu hình mà bạn đã bỏ lỡ. Và nếu bạn thuộc nhóm kỹ sư, hãy cảnh giác với các nỗ lực benchmark—từ công ty của bạn hoặc từ các bên thứ ba hợp đồng—và giúp đỡ họ.

Trong một trường hợp, tôi thấy một nhóm kỹ sư đã làm việc chăm chỉ để phát triển một sản phẩm hiệu năng cao. Chìa khóa cho hiệu năng của nó là một công nghệ mới chưa được tài liệu hóa. Đối với việc ra mắt sản phẩm, một nhóm benchmark đã được yêu cầu cung cấp các con số. Họ đã không hiểu công nghệ mới (nó đã không được tài liệu hóa), họ đã cấu hình sai, và sau đó họ đã công bố các con số đánh giá thấp sản phẩm.

Đôi khi hệ thống có thể được cấu hình chính xác nhưng đơn giản là chưa được đẩy tới giới hạn của nó. Hãy đặt câu hỏi, Nút thắt cổ chai cho benchmark này là gì? Đây có thể là một tài nguyên vật lý (chẳng hạn như CPUs, đĩa, hoặc một kết nối mạng) thứ đã đạt tới mức sử dụng 100% và có thể được nhận diện bằng phân tích. Xem Mục 12.3.2, Kiểm thử Tích cực (Active Benchmarking).

Một vấn đề quân ta đánh quân mình khác là khi benchmarking các phiên bản cũ hơn của một phần mềm có các vấn đề hiệu năng đã được sửa trong các phiên bản sau này, hoặc trên các thiết bị giới hạn tình cờ có sẵn, tạo ra một kết quả không phải là tốt nhất có thể. Các khách hàng tiềm năng của bạn có thể giả định bất kỳ kết quả benchmark nào được công bố đều cho thấy hiệu năng tốt nhất có thể—chứ không phải cung cấp các con số đánh giá thấp sản phẩm.

**14. Các Benchmarks gây Nhầm lẫn (Misleading Benchmarks)**
Các benchmarks gây nhầm lẫn là phổ biến trong ngành công nghiệp. Chúng có thể là kết quả của việc vô tình giới hạn thông tin về những gì benchmark thực sự đo lường, hoặc các thông tin bị bỏ qua một cách có chủ ý. Thông thường, kết quả benchmark là chính xác về mặt kỹ thuật nhưng sau đó được trình bày sai lệch tới khách hàng.

Hãy cân nhắc tình huống giả định này: Một nhà cung cấp đạt được một kết quả tuyệt vời bằng cách xây dựng một sản phẩm tùy chỉnh cực kỳ tốn kém và sẽ không bao giờ được bán cho một khách hàng thực sự. Giá cả không được tiết lộ với kết quả này, thứ tập trung vào các chỉ số hiệu năng trên-mỗi-giá (non-price/performance metrics). Bộ phận tiếp thị tự do chia sẻ một bản tóm tắt gây nhầm lẫn về kết quả ("Chúng tôi nhanh hơn gấp 2 lần!"), liên kết nó trong tâm trí khách hàng với công ty nói chung hoặc một dòng sản phẩm. Đây là một trường hợp bỏ sót các chi tiết để trình bày các sản phẩm một cách thuận lợi. Mặc dù nó có thể không phải là gian lận—các con số không phải là giả mạo—nhưng nó là *nói dối bằng cách bỏ sót*.

Những benchmarks của nhà cung cấp như vậy vẫn có thể hữu ích cho bạn dưới dạng các giới hạn trên cho hiệu năng. Chúng là các giá trị mà bạn không nên kỳ vọng sẽ vượt qua (ngoại trừ các trường hợp quân ta đánh quân mình).

Hãy cân nhắc một tình huống giả định khác: Một bộ phận tiếp thị có ngân sách để dành cho một chiến dịch và muốn một kết quả benchmark tốt để sử dụng. Họ thuê một vài bên thứ ba để benchmark sản phẩm của họ và chọn kết quả tốt nhất từ nhóm đó. Ba bên này không được chọn vì chuyên môn của họ; họ được trả tiền để mang lại một kết quả nhanh và không tốn kém. Trên thực tế, chuyên môn thấp có thể được coi là có lợi: các kết quả càng sai lệch so với thực tế, thì càng tốt—lý tưởng nhất là một trong số chúng sai lệch rất nhiều theo hướng tích cực!

Khi xem các kết quả của nhà cung cấp, hãy cẩn thận kiểm tra các dòng chữ in nhỏ để xem hệ thống nào đã được kiểm tra, loại đĩa nào đã được sử dụng và bao nhiêu cái, bao nhiêu giao diện mạng đã được sử dụng và trong cấu hình nào, và các yếu tố khác. Để biết các chi tiết cần cảnh giác, xem Mục 12.4, Các câu hỏi về Benchmark.

**15. Benchmark Specials**
*Benchmark specials* là khi nhà cung cấp nghiên cứu một benchmark phổ biến hoặc của ngành công nghiệp, và sau đó tinh chỉnh sản phẩm của họ sao cho nó ghi điểm tốt trong benchmark đó, trong khi bỏ qua hiệu năng thực tế của khách hàng. Điều này cũng được gọi là *tối ưu hóa cho benchmark*.

Thuật ngữ benchmark specials bắt đầu được sử dụng vào năm 1993 với benchmark TPC-A, như được mô tả trên trang lịch sử của Hội đồng Hiệu năng Xử lý Giao dịch (TPC) [Shanley 98]:

> The Standish Group, một công ty tư vấn có trụ sở tại Massachusetts, đã cáo buộc rằng Oracle đã thêm một tùy chọn đặc biệt (các giao dịch rời rạc) vào phần mềm cơ sở dữ liệu của mình, với mục đích duy nhất là thổi phồng các kết quả TPC-A của Oracle. The Standish Group tuyên bố rằng Oracle đã "vi phạm tinh thần của TPC" vì tùy chọn giao dịch rời rạc là thứ mà một khách hàng điển hình sẽ không sử dụng và do đó, là một kết quả benchmark đặc biệt. Oracle kịch liệt bác bỏ lời cáo buộc, tuyên bố, với một số biện minh, rằng họ đã tuân thủ đúng câu chữ của pháp luật trong các đặc tả benchmark. Oracle lập luận rằng vì các benchmark specials, ít hơn nhiều tinh thần của TPC, đã không được đề cập trong các đặc tả benchmark TPC, nên thật không công bằng khi buộc tội họ vi phạm bất cứ điều gì.

TPC đã thêm một điều khoản chống-benchmark special:

> Tất cả các triển khai "benchmark special" nhằm cải thiện các kết quả benchmark nhưng không thực tế đối với hiệu năng hoặc giá cả trong thế giới thực, đều bị cấm.

Vì TPC tập trung vào giá cả/hiệu năng, một chiến lược khác để thổi phồng các con số có thể là dựa trên *giá cả đặc biệt*—các mức giảm giá sâu mà không khách hàng nào thực sự nhận được. Giống như những thay đổi của phần mềm, kết quả này không khớp với thực tế khi một khách hàng thực sự mua hệ thống. TPC cũng đã đề cập đến vấn đề này trong các yêu cầu về giá của họ [TPC 19a]:

> Các đặc tả TPC yêu cầu rằng tổng giá phải nằm trong khoảng 2% của mức giá mà một khách hàng sẽ trả cho cấu hình đó.

Trong khi những ví dụ này giúp giải thích khái niệm về các benchmark specials, TPC đã giải quyết chúng trong các đặc tả của mình nhiều năm trước, và bạn không nên nhất thiết kỳ vọng chúng ngày nay.

**16. Gian lận (Cheating)**
Thất bại cuối cùng của benchmarking là gian lận: chia sẻ các kết quả giả mạo. May mắn thay, điều này là hiếm hoặc không tồn tại; tôi chưa thấy một trường hợp nào về những con số hoàn toàn hư cấu được chia sẻ, ngay cả trong những trận chiến benchmarking khốc liệt nhất.

## 12.2 Các loại Benchmarking
Một phổ các loại benchmark được hình ảnh hóa trong Hình 12.1, dựa trên khối lượng công việc mà chúng kiểm tra. Khối lượng công việc sản xuất cũng được bao gồm trong phổ này.

(Hình 12.1 Các loại Benchmark)

Các phần sau đây mô tả ba loại benchmarking: micro-benchmarks, các mô phỏng (simulations), và trace/replay. Các benchmarks tiêu chuẩn ngành công nghiệp cũng được thảo luận.

### 12.2.1 Micro-Benchmarking
Micro-benchmarking sử dụng các khối lượng công việc nhân tạo để kiểm tra một loại thao tác cụ thể, ví dụ, thực hiện một loại đơn lẻ của I/O hệ thống tập tin, truy vấn cơ sở dữ liệu, chỉ lệnh CPU, hoặc lệnh gọi hệ thống. Ưu điểm là sự đơn giản: thu hẹp số lượng các thành phần và các đường dẫn mã liên quan dẫn đến các kết quả trong một mục tiêu dễ dàng hơn để nghiên cứu và cho phép các sự khác biệt hiệu năng được lần ra tận gốc rễ một cách nhanh chóng. Các bài kiểm tra cũng thường có thể lặp lại được, vì sự biến động từ các thành phần khác được tính đến hết mức có thể. Micro-benchmarks cũng thường nhanh chóng để thực hiện trên các hệ thống khác nhau. Và bởi vì chúng là nhân tạo một cách có chủ ý, micro-benchmarks không dễ dàng bị nhầm lẫn với các mô phỏng thực tế.

Đối với các micro-benchmark kết quả cần được tiêu thụ, chúng cần được ánh xạ tới khối lượng công việc đích. Một micro-benchmark có thể kiểm tra vài chiều (dimensions), nhưng chỉ một hoặc hai cái có thể là phù hợp. Phân tích hiệu năng hoặc mô hình hóa hệ thống đích có thể giúp xác định micro-benchmark nào mang lại kết quả phù hợp nhất, và ở mức độ nào.

Các công cụ micro-benchmark ví dụ được đề cập trong các chương trước bao gồm, theo loại tài nguyên:
- **CPU:** SysBench
- **Bộ nhớ I/O:** lmbench (trong Chương 6, CPUs)
- **Hệ thống tập tin:** fio
- **Đĩa:** hdparm, dd hoặc fio với I/O trực tiếp
- **Mạng:** iperf

Có rất nhiều, rất nhiều công cụ benchmark sẵn có. Tuy nhiên, hãy nhớ cảnh báo từ [Traeger 08]: “Hầu hết các benchmarks phổ biến đều có sai sót.”

Bạn cũng có thể phát triển cái của riêng mình. Mục tiêu là giữ cho chúng đơn giản nhất có thể, nhận diện các thuộc tính của khối lượng công việc có thể được kiểm tra riêng lẻ. (Xem Mục 12.3.6, Các Benchmarks tùy chỉnh, để biết thêm về nội dung này.) Sử dụng các externals tools (công cụ bên ngoài) để xác minh rằng chúng thực hiện các thao tác mà chúng tuyên bố thực hiện.

**Ví dụ Thiết kế (Design Example)**
Cân nhắc việc thiết kế một micro-benchmark hệ thống tập tin để kiểm tra các thuộc tính sau: tuần tự hoặc ngẫu nhiên I/O, kích thước I/O, và hướng (đọc hoặc ghi). Bảng 12.1 trình bày năm bài kiểm tra mẫu để điều tra những khía cạnh này, cùng với lý do cho mỗi bài kiểm tra.

Bảng 12.1 Các bài kiểm tra micro-benchmark hệ thống tập tin mẫu
| # | Bài kiểm tra | Ý định |
|---| --- | --- |
| 1 | tuần tự 512-byte reads | Để kiểm tra IOPS tối đa (thực tế) |
| 2 | tuần tự 1-Mbyte reads | Để kiểm tra thông lượng đọc tối đa |
| 3 | tuần tự 1-Mbyte writes | Để kiểm tra thông lượng ghi tối đa |
| 4 | ngẫu nhiên 512-byte reads | Để kiểm tra ảnh hưởng của I/O ngẫu nhiên |
| 5 | ngẫu nhiên 512-byte writes | Để kiểm tra ảnh hưởng của việc ghi lại |

Nhiều bài kiểm tra hơn có thể được thêm vào như mong muốn. Tất cả các bài kiểm tra này được nhân lên bởi hai yếu tố bổ sung:
- **Kích thước tập dữ liệu làm việc (Working set size):** Kích thước dữ liệu được truy cập (ví dụ: tổng kích thước tệp):
  - Nhỏ hơn nhiều so với bộ nhớ chính: Sao cho dữ liệu nằm hoàn toàn trong file system cache, và hiệu năng của phần mềm hệ thống tập tin có thể được nghiên cứu.
  - Lớn hơn nhiều so với bộ nhớ chính: Để giảm thiểu ảnh hưởng của file system cache và thúc đẩy benchmark hướng tới việc kiểm tra đĩa I/O.
- **Số lượng luồng (Thread count):** Giả định một kích thước tập dữ liệu làm việc nhỏ:
  - Đơn luồng (Single-threaded): Để kiểm tra hiệu năng hệ thống tập tin dựa trên tốc độ xung nhịp CPU hiện tại.
  - Đa luồng (Multithreaded): Đủ để làm bão hòa tất cả các CPUs: Để kiểm tra hiệu năng tối đa của hệ thống, hệ thống tập tin, và các CPUs.

Những thứ này có thể nhanh chóng nhân lên để tạo thành một ma trận lớn các bài kiểm tra. Các kỹ thuật phân tích thống kê có thể được sử dụng để giảm bớt tập hợp bài kiểm tra cần thiết.

Tạo ra các benchmarks tập trung vào các tốc độ đỉnh cao đã được gọi là kiểm thử *sunny day* (ngày nắng). Để các vấn đề không bị bỏ qua, bạn cũng muốn cân nhắc kiểm thử hiệu năng *cloudy day* (ngày mây) hoặc *rainy day* (ngày mưa), thứ liên quan đến việc kiểm tra các tình huống không lý tưởng, bao gồm tranh chấp, các nhiễu loạn, và biến động khối lượng công việc.

### 12.2.2 Mô phỏng (Simulation)
Nhiều benchmarks mô phỏng các khối lượng công việc ứng dụng của khách hàng; những thứ này đôi khi được gọi là *macro-benchmarks*. Chúng có thể dựa trên việc đặc tính hóa khối lượng công việc của môi trường sản xuất (xem Chương 2, Các phương pháp luận) để xác định các đặc tính cần mô phỏng. Ví dụ, bạn có thể thấy rằng một khối lượng công việc sản xuất NFS bao gồm các loại thao tác và xác suất sau đây: reads, 40%; writes, 7%; getattr, 19%; readdir, 1%; và cứ tiếp tục như vậy. Các đặc tính khác cũng có thể được đo lường và mô phỏng.

Các mô phỏng có thể tạo ra các kết quả tương tự như cách khách hàng sẽ thực hiện với tải trong thế giới thực, nếu không giống hệt, thì ít nhất là đủ gần để hữu ích. Chúng có thể bao quát nhiều yếu tố có thể tốn thời gian để nghiên cứu sử dụng micro-benchmarking. Các mô phỏng cũng có thể bao gồm các ảnh hưởng của các tương tác hệ thống phức tạp có thể bị bỏ lỡ hoàn toàn khi sử dụng micro-benchmarking.

Các micro-benchmarks CPU Whetstone và Dhrystone, được giới thiệu trong Chương 6, CPUs, là các ví dụ về các mô phỏng. Whetstone được phát triển vào năm 1972 để mô phỏng các khối lượng công việc khoa học của thời bấy giờ. Dhrystone, từ năm 1984, mô phỏng các khối lượng công việc dựa trên số nguyên của thời bấy giờ.

Nhiều công ty mô phỏng tải HTTP máy khách sử dụng phần mềm tạo tải nội bộ hoặc bên ngoài—ví dụ bao gồm wrk [Glozer 19], siege [Fulmer 12], và hey [Dogan 20]. Những thứ này có thể được sử dụng để đánh giá các thay đổi phần mềm hoặc phần cứng, và cũng để mô phỏng tải cao điểm (ví dụ: “flash sales” trên một nền tảng mua sắm trực tuyến) để lộ ra các nút thắt cổ chai có thể được phân tích và giải quyết.

Một sự mô phỏng khối lượng công việc có thể là *không trạng thái* (stateless), nơi mỗi yêu cầu máy chủ là không liên quan đến yêu cầu trước đó. Ví dụ, khối lượng công việc máy chủ NFS được mô tả trước đó có thể được mô phỏng bằng cách yêu cầu một chuỗi các thao tác, với mỗi loại thao tác được chọn ngẫu nhiên dựa trên xác suất đo lường được.

Một mô phỏng cũng có thể là *có trạng thái* (stateful), nơi mỗi yêu cầu phụ thuộc vào trạng thái máy khách, ở mức tối thiểu yêu cầu trước đó. Bạn có thể thấy rằng các lần đọc NFS có xu hướng đến theo nhóm, sao cho xác suất của một lệnh ghi theo sau một lệnh ghi là cao hơn nhiều so với một lệnh ghi theo sau một lệnh đọc. Những hành vi như vậy có thể được mô phỏng tốt hơn bằng cách sử dụng một *mô hình Markov*, bằng việc trình bày các yêu cầu như các trạng thái và đo lường xác suất của các đợt chuyển đổi trạng thái [Jain 91].

Một vấn đề với các mô phỏng là chúng có thể bỏ qua biến động, như đã được mô tả trong Mục 12.1.3, Thất bại Benchmarking. Các mẫu sử dụng của khách hàng cũng có thể thay đổi theo thời gian, yêu cầu những mô phỏng này phải được cập nhật và điều chỉnh để luôn phù hợp. Có thể có sự kháng cự đối với việc này, tuy nhiên, nếu đã có các kết quả đã được công bố dựa trên phiên bản cũ hơn của benchmark, thứ sẽ không còn có thể sử dụng được cho các sự so sánh với phiên bản mới.

### 12.2.3 Phát lại (Replay)
Một loại benchmarking thứ ba liên quan đến việc cố gắng phát lại (replay) một nhật ký truy vết (trace log) tới mục tiêu, kiểm tra hiệu năng của nó với các thao tác khách đã bắt được thực sự. Điều này nghe có vẻ lý tưởng—tốt như việc kiểm tra trong sản xuất, đúng chứ? Tuy nhiên, nó có vấn đề: khi các đặc tính và độ trễ được phân phối thay đổi trên máy chủ, khối lượng công việc máy khách đã bắt được khó có thể phản ứng tự nhiên với những thay đổi này, thứ có thể chứng minh là không tốt hơn một khối lượng công việc khách được mô phỏng. Khi quá nhiều niềm tin được đặt vào nó, mọi thứ có thể trở nên tồi tệ hơn.

Cân nhắc tình huống giả định này: Một khách hàng đang cân nhắc việc nâng cấp hạ tầng lưu trữ. Khối lượng công việc sản xuất hiện tại được truy vết và phát lại trên phần cứng mới. Thật không may, hiệu năng là tệ hơn, và đợt bán hàng bị mất. Vấn đề là: việc truy vết/phát lại vận hành tại mức đĩa I/O. Hệ thống cũ chứa các đĩa 10 K rpm, và hệ thống mới chứa các đĩa 7,200 rpm chậm hơn. Tuy nhiên, hệ thống mới cung cấp gấp 16 lần lượng file system cache và các bộ xử lý nhanh hơn. Khối lượng công việc sản xuất thực tế đáng lẽ sẽ cho thấy hiệu năng được cải thiện, vì nó sẽ được trả về phần lớn từ bộ đệm ẩn—thứ không được mô phỏng bằng cách phát lại các sự kiện đĩa.

Trong khi đây là một trường hợp kiểm tra sai thứ, những hiệu ứng thời gian tinh vi khác có thể làm rối tung mọi thứ, ngay cả với mức độ truy vết/phát lại chính xác. Giống như với tất cả các benchmarks, điều quan trọng là phải phân tích và hiểu những gì đang diễn ra.

### 12.2.4 Các tiêu chuẩn Ngành công nghiệp (Industry Standards)
Các benchmarks tiêu chuẩn ngành công nghiệp có sẵn từ các tổ chức độc lập, nhằm mục đích tạo ra các benchmarks công bằng và phù hợp. Đây thường là một bộ sưu tập các mô phỏng khối lượng công việc khác nhau được xác định rõ ràng và được tài liệu hóa và phải được thực thi dưới các hướng dẫn nhất định sao cho các kết quả đạt được như mong muốn. Các nhà cung cấp có thể tham gia (thường là trả phí) thứ cung cấp cho nhà cung cấp phần mềm để thực thi benchmark. Kết quả của họ thường yêu cầu sự công bố đầy đủ về môi trường đã cấu hình, thứ có thể cần được kiểm toán (audited).

Đối với khách hàng, các tiêu chuẩn này có thể tiết kiệm rất nhiều thời gian, vì các kết quả benchmark có thể đã sẵn có cho một loạt các nhà cung cấp và sản phẩm. Tác vụ dành cho bạn, sau đó, là tìm ra benchmark mô phỏng chặt chẽ nhất tải khối lượng công việc sản xuất hiện tại hoặc tương lai của bạn. Đối với các khối lượng công việc hiện tại, điều này có thể được xác định bằng đặc tính hóa khối lượng công việc.

Nhu cầu cho các benchmarks tiêu chuẩn ngành công nghiệp đã trở nên rõ ràng trong một bài báo năm 1985 mang tên “A Measure of Transaction Processing Power” bởi Jim Gray và những người khác [Anon 85]. Nó mô tả nhu cầu về hiệu năng đo lường giá trị/hiệu năng, và chi tiết hóa ba benchmarks mà các nhà cung cấp có thể thực thi, được gọi là Sort, Scan, và DebitCredit. Nó cũng gợi ý một thước đo tiêu chuẩn của các giao dịch trên mỗi giây (TPS) dựa trên DebitCredit, thứ có thể được sử dụng tương tự như dặm trên mỗi gallon cho ô tô. Jim Gray và công việc của ông sau đó đã khuyến khích việc tạo ra TPC [DeWitt 08].

Bên cạnh phép đo TPS, những cái khác đã được sử dụng cho cùng vai trò đó bao gồm:
- **MIPS:** Hàng triệu chỉ lệnh trên mỗi giây. Trong khi đây là một thước đo hiệu năng, công việc được thực hiện phụ thuộc vào loại chỉ lệnh, thứ có thể khó so sánh giữa các kiến trúc bộ xử lý khác nhau.
- **FLOPS:** Các thao tác dấu phẩy động (floating-point operations) trên mỗi giây—một vai trò tương tự như MIPS, nhưng cho các khối lượng công việc thực hiện việc sử dụng nặng nề các tính toán dấu phẩy động.

Các benchmarks ngành công nghiệp thường đo lường một chỉ số tùy chỉnh dựa trên benchmark, thứ chỉ phục vụ cho các sự so sánh với chính nó.

**TPC**
Hội đồng Hiệu năng Xử lý Giao dịch (Transaction Processing Performance Council - TPC) tạo ra và quản trị các benchmarks ngành công nghiệp với trọng tâm vào hiệu năng cơ sở dữ liệu. Những thứ này bao gồm:
- **TPC-C:** Một mô phỏng về một môi trường tính toán hoàn chỉnh nơi một lượng người dùng thực thi các giao dịch chống lại một cơ sở dữ liệu.
- **TPC-DS:** Một mô phỏng của một hệ thống hỗ trợ quyết định (decision support system), bao gồm các truy vấn và bảo trì dữ liệu.
- **TPC-E:** Một khối lượng công việc xử lý giao dịch trực tuyến (OLTP), mô hình hóa một công ty môi giới với các khách hàng tạo ra các giao dịch liên quan đến các đợt giao dịch, các truy vấn tài khoản, và nghiên cứu thị trường.
- **TPC-H:** Một benchmark hỗ trợ quyết định, mô phỏng các truy vấn tùy biến (ad hoc queries) và các sửa đổi dữ liệu đồng thời.
- **TPC-VMS:** Hệ thống Đơn Máy ảo TPC (TPC Virtual Measurement Single System) cho phép các benchmarks khác được thu thập cho các cơ sở dữ liệu ảo hóa.
- **TPC-HS:** Một benchmark dữ liệu lớn (big data) sử dụng Hadoop.
- **TPCx-V:** Kiểm tra các khối lượng công việc cơ sở dữ liệu trong các máy ảo.

Các kết quả TPC được chia sẻ trực tuyến [TPC 19b] và bao gồm giá cả/hiệu năng.

**SPEC**
Tập đoàn Đánh giá Hiệu năng Tiêu chuẩn (Standard Performance Evaluation Corporation - SPEC) phát triển và công bố một bộ các benchmarks ngành công nghiệp tiêu chuẩn hóa, bao gồm:
- **SPEC Cloud IaaS 2018:** Thử nghiệm này kiểm tra việc cung cấp, tính toán, lưu trữ, và tài nguyên mạng, sử dụng nhiều khối lượng công việc đa thực thể (multi-instance workloads).
- **SPEC CPU 2017:** Một thước đo của các khối lượng công việc tiêu tốn nhiều tính toán, bao gồm các bài kiểm tra dấu phẩy động và số nguyên, và một chỉ số tùy chọn cho tiêu thụ năng lượng.
- **SPECjEnterprise 2018 Web Profile:** Một thước đo hiệu năng đầy đủ của hệ thống cho các máy chủ ứng dụng Java Enterprise Edition (Java EE) Web Profile phiên bản 7 hoặc sau này, các cơ sở dữ liệu, và hạ tầng hỗ trợ.
- **SPECfs2014:** Một mô phỏng của một khối lượng công việc truy cập tệp máy khách cho các máy chủ NFS, hệ thống tệp internet chung (common internet file system - CIFS), và các hệ thống tệp tương tự.
- **SPECvirt_sc2013:** Cho các môi trường ảo hóa, điều này đo lường hiệu năng đầu-cuối của phần cứng ảo hóa, nền tảng, và hệ điều hành khách cùng phần mềm ứng dụng.

Các kết quả của SPEC được chia sẻ trực tuyến [SPEC 20] và bao gồm các chi tiết về cách các hệ thống được tinh chỉnh và một danh sách các thành phần, nhưng không thường là giá của chúng.

## 12.3 Phương pháp luận (Methodology)
Phần này mô tả các phương pháp luận và các bài tập cho việc thực hiện benchmarking, cho dù đó là micro-benchmarking, các mô phỏng, hay phát lại. Các chủ đề được tóm tắt trong Bảng 12.2.

Bảng 12.2 Các phương pháp luận phân tích benchmark
| Mục | Phương pháp luận | Các loại |
| --- | --- | --- |
| 12.3.1 | Benchmarking thụ động | Phân tích thực nghiệm |
| 12.3.2 | Benchmarking tích cực | Phân tích quan sát |
| 12.3.3 | CPU profiling | Phân tích quan sát |
| 12.3.4 | Phương pháp USE | Phân tích quan sát |
| 12.3.5 | Đặc tính hóa khối lượng công việc | Phân tích quan sát |
| 12.3.6 | Benchmarks tùy chỉnh | Phát triển phần mềm |
| 12.3.7 | Tăng dần tải (Ramping load) | Phân tích thực nghiệm |
| 12.3.8 | Kiểm tra tính hợp lý (Sanity check) | Phân tích quan sát |
| 12.3.9 | Phân tích thống kê | Phân tích thống kê |

### 12.3.1 Benchmarking Thụ động (Passive Benchmarking)
Đây là chiến lược "fire-and-forget" của benchmarking—nơi benchmark được thực thi và sau đó bị phớt lờ cho đến khi nó hoàn thành. Mục tiêu chính là thu thập dữ liệu benchmark. Đây là cách thức các benchmarks thường được thực thi, và được mô tả như là phản-phương pháp luận (anti-methodology) của chính nó để so sánh với benchmarking tích cực.

Dưới đây là một số bước benchmarking thụ động ví dụ:
1. Chọn một công cụ benchmark.
2. Chạy nó với một loạt các tùy chọn.
3. Tạo một bản trình chiếu các kết quả.
4. Gửi các bản trình chiếu cho ban quản lý.

Các vấn đề với cách tiếp cận này đã được thảo luận trước đó. Tóm lại, các kết quả có thể là:
- Không hợp lệ do các lỗi phần mềm benchmark
- Bị giới hạn bởi phần mềm benchmark (ví dụ: đơn luồng)
- Bị giới hạn bởi một thành phần không liên quan đến mục tiêu benchmark (ví dụ: mạng bị tắc nghẽn)
- Bị giới hạn bởi cấu hình (các tính năng hiệu năng không được bật, không phải cấu hình tối đa)
- Chịu các nhiễu loạn (và không thể lặp lại)
- Benchmarking hoàn toàn sai thứ

Benchmarking thụ động là dễ thực hiện nhưng dễ xảy ra lỗi. Khi được thực hiện bởi nhà cung cấp, nó có thể tạo ra các báo động giả lãng phí tài nguyên kỹ thuật hoặc gây mất doanh thu. Khi được thực hiện bởi khách hàng, nó có thể dẫn đến các lựa chọn sản phẩm kém gây ám ảnh cho công ty sau này.

### 12.3.2 Benchmarking Tích cực (Active Benchmarking)
Với benchmarking tích cực, bạn phân tích hiệu năng trong khi benchmark đang chạy—không chỉ sau khi nó đã xong—sử dụng các công cụ quan sát [Gregg 14d]. Bạn có thể xác nhận những gì benchmark kiểm tra và bài kiểm tra nói gì, và rằng bạn hiểu những gì mà nó đang thực hiện. Benchmarking tích cực cũng có thể nhận diện các yếu tố hạn chế thực sự của hệ thống đang được kiểm tra, hoặc của chính benchmark đó. Nó có thể rất hữu ích khi bao gồm các chi tiết cụ thể của giới hạn gặp phải khi chia sẻ các kết quả benchmark.

Như một phần thưởng, đây có thể là một thời điểm tốt để phát triển các kỹ năng của bạn với các công cụ quan sát hiệu năng. Về mặt lý thuyết, bạn đang kiểm tra một *known load* (tải đã biết) và có thể thấy nó xuất hiện như thế nào từ những công cụ này.

Lý tưởng nhất, benchmark có thể được cấu hình và để chạy trong trạng thái ổn định (steady state), sao cho việc phân tích có thể được thực hiện qua một khoảng thời gian hàng giờ hoặc hàng ngày.

**Nghiên cứu Điển hình về Phân tích (Analysis Case Study)**
Như một ví dụ, hãy nhìn vào bài kiểm tra đầu tiên của công cụ micro-benchmark bonnie++. Nó được mô tả bởi trang man của nó dưới dạng (tôi nhấn mạnh):

> bonnie++ – chương trình để kiểm tra **hiệu năng ổ cứng (hard drive performance).**

Và trên trang chủ của nó [Coker 01]:

> Bonnie++ là một bộ benchmark nhằm mục đích thực hiện một số bài kiểm tra đơn giản về hiệu năng ổ cứng và hệ thống tập tin.

Chạy bonnie++ trên Ubuntu Linux:
```bash
# bonnie++
[...]
Version  1.97       ------Sequential Output------ --Sequential Input-- --Random-
Concurrency   1     -Per Chr- --Block-- -Rewrite- -Per Chr- --Block-- --Seeks--
Machine        Size K/sec %CP K/sec %CP K/sec %CP K/sec %CP K/sec %CP  /sec %CP
ip-10-1-239-21    4G   739  99 549247  46 308024  37 1845  99 1156838  38 +++++ +++
Latency             18699us     983ms     280ms   11065us    4505us   7762us
[...]
```
Bài kiểm tra đầu tiên là "Sequential Output" và "Per Chr", và ghi được 739 Kbytes/sec theo bonnie++.

Kiểm tra tính hợp lý (Sanity check): nếu điều này thực sự là I/O cho mỗi ký tự, nó sẽ có nghĩa là hệ thống đang đạt được 739,000 I/O mỗi giây. Benchmark được mô tả là kiểm tra hiệu năng ổ cứng, nhưng tôi nghi ngờ hệ thống này có thể đạt được mức IOPS đĩa cao như vậy.

Trong khi chạy bài kiểm tra đầu tiên, tôi đã sử dụng iostat(1) để kiểm tra IOPS đĩa:
```bash
$ iostat -sxz 1
[...]
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          11.44    0.00   38.81    0.00    0.00   49.75

Device             tps      kB/s    rqm/s   await aqu-sz  areq-sz  %util
[...]
```
Không có đĩa I/O nào được báo cáo.

Bây giờ sử dụng bpftrace để đếm các sự kiện I/O khối (xem Chương 9, Đĩa, Mục 9.6.11, bpftrace):
```bash
# bpftrace -e 'tracepoint:block:* { @[probe] = count(); }'
Attaching 18 probes...
^C

@[tracepoint:block:block_dirty_buffer]: 808225
@[tracepoint:block:block_touch_buffer]: 1025678
```
Điều này cũng cho thấy không có đĩa I/O nào được phát hành (không có block:block_rq_issue) hoặc hoàn thành (block:block_rq_complete); tuy nhiên, các bộ đệm đã bị bẩn (dirtied). Sử dụng cachestat(8) (Chương 8, Hệ thống Tập tin, Mục 8.6.12, cachestat) để xem trạng thái của file system cache:
```bash
# cachestat 1
    HITS   MISSES  DIRTIES HITRATIO   BUFFERS_MB  CACHED_MB
       0        0        0    0.00%           49        361
     293        0    54299  100.00%           49        361
     658        0   298748  100.00%           49        361
     250        0   602499  100.00%           49        362
[...]
```
bonnie++ đã bắt đầu thực thi trên dòng kết quả thứ hai, và điều này xác nhận một khối lượng công việc gồm "dirties": ghi vào file system cache.

Kiểm tra I/O cao hơn trong I/O stack, tại mức VFS (xem Chương 8, Hệ thống Tập tin, Mục 8.6.15, bpftrace):
```bash
# bpftrace -e 'kprobe:vfs_* /comm == "bonnie++"/ { @[probe] = count(); }'
Attaching 65 probes...
^C

@[kprobe:vfs_fsync_range]: 2
@[kprobe:vfs_statx_fd]: 6
@[kprobe:vfs_open]: 7
@[kprobe:vfs_read]: 13
@[kprobe:vfs_write]: 1176936
```
Điều này cho thấy thực sự có một khối lượng công việc vfs_write() nặng nề. Việc đào sâu hơn nữa với bpftrace xác minh kích thước:
```bash
# bpftrace -e 'k:vfs_write /comm == "bonnie++"/ { @bytes = hist(arg2); }'
Attaching 1 probe...
^C

@bytes:
[1]               668839 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[2, 4)                 0 |                                                    |
[4, 8)                 0 |                                                    |
[8, 16)                0 |                                                    |
[16, 32)               1 |                                                    |
```
Đối số thứ ba của vfs_write() là số lượng byte, và nó thường là 1 byte (thông điệp đơn lẻ trong phạm vi 16 tới 31 byte có khả năng là một thông điệp bonnie++ về việc bắt đầu benchmark).

Bằng việc phân tích benchmark trong khi nó đang chạy (benchmarking tích cực), chúng ta đã biết được rằng bài kiểm tra bonnie++ đầu tiên là một bài kiểm tra ghi tập tin 1-byte, thứ đệm các tập tin trong file system cache. Nó không kiểm tra đĩa I/O, như được ngụ ý bởi các mô tả của bonnie++.

Theo trang man, bonnie++ có tùy chọn -b cho "no write buffering," gọi fsync(2) sau mỗi lệnh ghi. Tôi sẽ sử dụng strace(1) để phân tích hành vi này, vì strace(1) in ra tất cả các syscalls theo cách mà con người có thể đọc được. strace(1) cũng tiêu tốn chi phí cao, vì vậy các kết quả benchmark trong khi sử dụng strace(1) nên được loại bỏ.
```bash
$ strace bonnie++ -b
[...]
write(3, "6", 1)                        = 1
write(3, "7", 1)                        = 1
write(3, "8", 1)                        = 1
write(3, "9", 1)                        = 1
write(3, ":", 1)                        = 1
[...]
```
Kết quả cho thấy bonnie++ không gọi fsync(2) sau mỗi lệnh ghi. Nó cũng có một tùy chọn -D cho Direct IO, tuy nhiên, điều đó không thành công trên hệ thống của tôi. Không có cách nào để thực sự thực hiện một bài kiểm tra ghi đĩa theo từng ký tự (per-character).

Một số người có thể lập luận rằng bonnie++ không bị hỏng, và nó thực sự thực hiện một "Sequential Output" và "Per Chr" test: cả hai đều chọn những bài kiểm tra đáng nghi nhất của nó để nghiên cứu bởi vì nó nổi tiếng, tôi đã nghiên cứu nó trước đây, và thấy rằng điều này không phải là hiếm gặp. Nhưng nó chỉ là một ví dụ.

Các phiên bản cũ hơn của bonnie++ có thêm một vấn đề với bài kiểm tra này: nó cho phép libc đệm các lần ghi trước khi chúng được gửi tới hệ thống tập tin, vì vậy kích thước ghi VFS là 4 Kbytes hoặc cao hơn, tùy thuộc vào libc và phiên bản OS. Điều này khiến cho việc so sánh bonnie++ giữa các hệ điều hành khác nhau sử dụng các kích thước đệm libc khác nhau trở nên sai lệch. Vấn đề này đã được sửa trong các phiên bản gần đây của bonnie++, nhưng điều đó tạo ra một vấn đề khác: các kết quả mới từ bonnie++ không thể so sánh được với các kết quả cũ.

Để biết thêm về phân tích hiệu năng bonnie++, hãy xem bài báo của Roch Bourbonnais về “Decoding Bonnie++” [Bourbonnais 08].

### 12.3.3 CPU Profiling
Tạo hồ sơ (Profiling) cho cả đối tượng mục tiêu benchmark và phần mềm benchmark là đáng để nêu riêng như một phương pháp luận, vì nó có thể dẫn đến một số khám phá nhanh chóng. Nó thường được thực hiện như một phần của một cuộc điều tra benchmarking tích cực.

Ý định là để nhanh chóng kiểm tra xem tất cả phần mềm đang làm gì, để xem liệu có bất kỳ điều gì thú vị xuất hiện hay không. Điều này cũng có thể thu hẹp nghiên cứu của bạn vào các thành phần phần mềm quan trọng nhất: những thành phần đang hoạt động cho benchmark.

Cả hồ sơ stack cấp người dùng và cấp kernel đều có thể được tạo. CPU profiling cấp người dùng đã được giới thiệu trong Chương 5, Các ứng dụng. Cả hai đều được bao quát trong Chương 6, CPUs, với các ví dụ trong Mục 6.6, Các công cụ Quan trắc, bao gồm flame graphs.

**Ví dụ**
Một micro-benchmark đĩa đã được thực hiện trên một hệ thống mới được đề xuất với một số kết quả thất vọng: thông lượng đĩa tệ hơn so với hệ thống cũ. Tôi đã được yêu cầu tìm ra điều gì không ổn, với kỳ vọng rằng hoặc các đĩa hoặc bộ điều khiển đĩa là kém hơn và nên được nâng cấp.

Tôi đã bắt đầu với phương pháp USE (Chương 2, Các phương pháp luận) và thấy rằng các đĩa không bận rộn lắm. Có một số mức sử dụng CPU, trong system-time (kernel).

Đối với một benchmark đĩa, bạn có lẽ không kỳ vọng các CPUs là một mục tiêu thú vị để phân tích. Với một số mức sử dụng CPU trong kernel, tôi nghĩ nó đáng giá để xem liệu có bất cứ điều gì thú vị xuất hiện hay không, mặc dù tôi không kỳ vọng nó. Tôi đã tạo hồ sơ và tạo ra flame graph được trình bày trong Hình 12.2.

(Hình 12.2 Flame graph profiling thời gian kernel)

Việc duyệt qua các stack frames cho thấy 62.17% các mẫu CPU bao gồm một hàm mang tên zfs_zone_io_throttle(). Tôi đã không cần đọc mã nguồn cho hàm này, vì tên của nó đã đủ mang lại một manh mối: một kiểm soát tài nguyên, ZFS I/O throttling, đang hoạt động và *thực hiện điều tiết một cách nhân tạo* cho benchmark! Đây là một thiết lập mặc định trên hệ thống mới (nhưng không phải hệ thống cũ hơn) đã bị bỏ qua khi benchmark được thực hiện.

### 12.3.4 Phương pháp USE
Phương pháp USE đã được giới thiệu trong Chương 2, Các phương pháp luận, và được mô tả trong các chương cho các tài nguyên mà nó nghiên cứu. Áp dụng phương pháp USE trong quá trình benchmarking có thể đảm bảo rằng một giới hạn được tìm thấy. Hoặc là một số thành phần (phần cứng hoặc phần mềm) đã đạt tới mức sử dụng 100%, hoặc bạn chưa đẩy hệ thống tới giới hạn của nó.

### 12.3.5 Đặc tính hóa Khối lượng công việc
Đặc tính hóa khối lượng công việc cũng đã được giới thiệu trong Chương 2, Các phương pháp luận, và được thảo luận trong các chương sau này. Phương pháp luận này có thể được sử dụng để xác định benchmark đã thực hiện khớp tốt như thế nào so với một môi trường sản xuất hiện tại bằng cách đặc tính hóa khối lượng công việc sản xuất để so sánh.

### 12.3.6 Các Benchmarks tùy chỉnh
Đối với micro-benchmarks đơn giản, có thể là mong muốn để bạn tự viết mã phần mềm. Hãy cố gắng giữ chương trình càng ngắn càng tốt, để tránh độ phức tạp gây cản trở việc phân tích.

Ngôn ngữ lập trình C thường là một lựa chọn tốt cho micro-benchmarks, vì nó ánh xạ chặt chẽ tới những gì được thực thi—mặc dù bạn nên suy nghĩ cẩn thận về cách các tối ưu hóa của trình biên dịch sẽ ảnh hưởng đến mã của bạn: trình biên dịch có thể loại bỏ các thói quen benchmark đơn giản nếu nó nghĩ rằng kết quả không được sử dụng và do đó không cần thiết để tính toán. Luôn kiểm tra bằng các công cụ khác trong khi benchmark đang chạy để xác nhận hoạt động của nó. Có thể cũng đáng giá để tháo rời (disassembling) file nhị phân đã biên dịch để xem những gì sẽ thực sự được thực thi.

Các ngôn ngữ liên quan đến máy ảo, thu gom rác bất đồng bộ (asynchronous garbage collection), và biên dịch động trong thời gian chạy (dynamic run-time compilation) có thể làm cho benchmarking trở nên khó khăn hơn nhiều để thực hiện và kiểm soát với độ chính xác đáng tin cậy. Bạn có thể cần sử dụng những ngôn ngữ như vậy, tuy nhiên, nếu cần thiết để mô phỏng phần mềm máy khách được viết bằng chúng: macro-benchmarks.

Viết các benchmarks tùy chỉnh cũng có thể tiết lộ các chi tiết tinh tế về mục tiêu thứ có thể chứng minh là hữu ích sau này. Ví dụ, khi phát triển một benchmark cơ sở dữ liệu, bạn có thể khám phá ra rằng các tùy chọn API cho việc cải thiện hiệu năng không hiện diện trong môi trường sản xuất hiện tại, thứ đã được phát triển trước khi các tùy chọn đó tồn tại.

Phần mềm của bạn có thể chỉ đơn giản là tạo ra tải (một trình tạo tải - *load generator*) và để lại việc đo lường cho các công cụ khác. Một cách để thực hiện điều này là *ramp load*.

### 12.3.7 Tăng dần Tải (Ramping Load)
Đây là một phương pháp đơn giản để xác định thông lượng tối đa mà một hệ thống có thể xử lý. Nó liên quan đến việc thêm tải theo các đợt tăng nhỏ và đo lường thông lượng đạt được cho đến khi đạt được giới hạn. Các kết quả có thể được vẽ đồ thị, hiển thị một scalability profile. Kết quả này có thể được nghiên cứu trực quan hoặc bằng cách sử dụng các mô hình khả năng mở rộng (xem Chương 2, Các phương pháp luận).

Như một ví dụ, Hình 12.3 cho thấy một scalability profile của máy chủ tập tin với các luồng. Mỗi luồng thực hiện các lần đọc ngẫu nhiên 8 Kbyte trên một tập tin đã đệm ẩn (cached), và những thứ này đã được thêm vào từng cái một.

Hệ thống này đạt đỉnh tại mức gần nửa triệu lần đọc mỗi giây. Các kết quả đã được kiểm tra bằng cách sử dụng các thống kê cấp VFS, thứ xác nhận rằng kích thước I/O là 8 Kbytes và tại đỉnh điểm hơn 3.5 Gbytes/s đã được truyền tải.

(Hình 12.3 Tăng dần tải hệ thống tập tin)

Trình tạo tải cho bài kiểm tra này được viết bằng Perl và đủ ngắn để bao gồm hoàn toàn như một ví dụ:
```perl
#!/usr/bin/perl -w
#
# randread.pl – đọc ngẫu nhiên trên tệp được chỉ định.

use strict;

my $IOSIZE = 8192;              # kích thước của I/O, byte
my $QUANTA = $IOSIZE;           # độ chi tiết của seek, byte

die "USAGE: randread.pl filename
" if @ARGV != 1 or not -e $ARGV[0];

my $file = $ARGV[0];
my $span = -s $file;            # phạm vi để đọc ngẫu nhiên, byte
my $junk;

open FILE, "$file" or die "ERROR: reading $file: $!
";

while (1) {
          seek(FILE, int(rand($span / $QUANTA)) * $QUANTA, 0);
          sysread(FILE, $junk, $IOSIZE);
}

close FILE;
```
Để tránh buffering, việc này sử dụng sysread() để gọi trực tiếp lệnh gọi hệ thống read(2).

Việc này được viết cho micro-benchmark một máy chủ NFS và được thực thi song song từ một farm gồm các máy khách, mỗi máy khách thực hiện các lệnh đọc ngẫu nhiên trên một file được mount NFS. Các kết quả của micro-benchmark (số lần đọc mỗi giây) được đo lường trên máy chủ NFS, sử dụng nfsstat(8) và các công cụ khác.

Số lượng tập tin được sử dụng và kích thước kết hợp của chúng được kiểm soát (điều này tạo thành *working set size*), sao cho một số bài kiểm tra chạy hoàn toàn từ bộ đệm ẩn trên máy chủ, và những bài kiểm tra khác từ đĩa. (Xem Ví dụ Thiết kế trong Mục 12.2.1, Micro-Benchmarking.)

Số lượng thực thể thực thi trên client farm được tăng dần từng cái một, để ramp load cho đến khi đạt được giới hạn. Điều này đã được phối hợp với phân tích hiệu năng với việc sử dụng tài nguyên (phương pháp USE), xác nhận rằng một tài nguyên đã bị cạn kiệt. Trong trường hợp này nó là các tài nguyên CPU trên máy chủ, thứ thúc đẩy một cuộc điều tra khác để cải thiện hơn nữa hiệu năng.

Tôi đã sử dụng chương trình này và cách tiếp cận này để tìm ra các giới hạn của Sun ZFS Storage Appliance [Gregg 09b]. Những giới hạn này đã được sử dụng như là các kết quả chính thức—theo sự hiểu biết tốt nhất của chúng tôi đã thiết lập các kỷ lục thế giới. Tôi cũng có một bộ phần mềm tương tự được viết bằng C, thứ mà tôi thường sử dụng, nhưng nó không cần thiết trong trường hợp này: Tôi đã có dư thừa các CPUs máy khách, và trong khi việc chuyển sang C đã làm giảm mức sử dụng của họ, nó đã không tạo ra sự khác biệt cho kết quả vì cùng một nút thắt cổ chai đã đạt tới trên mục tiêu. Các benchmarks khác, tinh vi hơn cũng đã được thử nghiệm, cũng như các ngôn ngữ khác, nhưng chúng không thể cải thiện so với những kết quả dựa trên Perl này.

Khi tuân theo cách tiếp cận này, hãy đo lường độ trễ cũng như thông lượng, đặc biệt là độ trễ phân phối. Khi hệ thống tiếp cận giới hạn của nó, độ trễ xếp hàng có thể trở nên đáng kể, khiến cho độ trễ tăng lên. Nếu bạn đẩy tải lên quá cao, độ trễ có thể trở nên cao đến mức nó không còn hợp lý để coi kết quả là hợp lệ. Hãy tự hỏi liệu độ trễ được phân phối có được chấp nhận đối với một khách hàng hay không.

Ví dụ: Bạn sử dụng một dãy lớn các máy khách để thúc đẩy một hệ thống mục tiêu tới 990,000 IOPS, thứ phản hồi với một độ trễ I/O trung bình là 5 ms. Bạn thực sự muốn nó phá vỡ mức 1 triệu IOPS, nhưng hệ thống đã đạt tới mức bão hòa. Bằng cách thêm nhiều máy khách hơn, bạn xoay xở để cày xới vượt qua 1 triệu IOPS; tuy nhiên, tất cả các thao tác bây giờ bị xếp hàng nặng nề, với độ trễ trung bình trên 50 ms, thứ là không thể chấp nhận được! Bạn đưa kết quả nào cho bộ phận tiếp thị? (Trả lời: 990,000 IOPS.)

### 12.3.8 Kiểm tra tính Hợp lý (Sanity Check)
Đây là một bài tập để kiểm tra một kết quả benchmark bằng cách điều tra xem liệu bất kỳ đặc tính nào có điểm vô lý hay không. Nó bao gồm việc kiểm tra xem liệu kết quả có yêu cầu một số thành phần vượt quá các giới hạn đã biết của nó hay không, chẳng hạn như băng thông mạng, băng thông bộ điều khiển, băng thông kết nối, hoặc IOPS đĩa. Nếu bất kỳ giới hạn nào đã bị vượt qua, điều đó đáng giá để điều tra chi tiết hơn. Trong hầu hết các trường hợp, bài tập này cuối cùng khám phá ra rằng kết quả benchmark là giả mạo.

Dưới đây là một ví dụ: Một máy chủ NFS được benchmark với các lần đọc 8 Kbyte và được báo cáo là phân phối 50,000 IOPS. Nó được kết nối tới mạng bằng cách sử dụng một giao diện Ethernet 1 Gbit/s duy nhất. Thông lượng mạng cần thiết để thúc đẩy 50,000 IOPS × 8 Kbytes = 400,000 Kbytes/s, cộng với các headers giao thức. Con số này là trên 3.2 Gbits/s—vượt xa giới hạn của một liên kết 1 Gbit/s. Có điều gì đó không ổn!

Các kết quả như thế này thường có nghĩa là benchmark đã kiểm tra *client caching* và không đẩy toàn bộ khối lượng công việc tới máy chủ NFS.

Tôi đã sử dụng cách tính toán này để nhận diện vô số các benchmarks giả mạo, thứ bao gồm các thông lượng sau đây qua một giao diện 1 Gbit/s duy nhất [Gregg 09c]:
- 120 Mbytes/s (0.96 Gbit/s)
- 200 Mbytes/s (1.6 Gbit/s)
- 350 Mbytes/s (2.8 Gbit/s)
- 800 Mbytes/s (6.4 Gbit/s)
- 1.15 Gbytes/s (9.2 Gbit/s)

Đây là tất cả thông lượng trong một hướng duy nhất. Kết quả 120 Mbytes/s có thể là ổn—một giao diện 1 Gbit/s nên đạt được khoảng 119 Mbyte/s, trong thực tế. Kết quả 200 Mbyte/s là khả thi chỉ nếu có tải lưu lượng lớn theo cả hai hướng và giá trị này được tổng hợp; tuy nhiên, đây là những kết quả theo hướng đơn lẻ. Kết quả 350 Mbyte/s và cao hơn rõ ràng là giả mạo.

Khi bạn được đưa cho một kết quả benchmark để kiểm tra, hãy tìm kiếm bất kỳ phép tính tổng đơn giản nào bạn có thể thực hiện trên các con số được cung cấp để khám phá các giới hạn đó.

Nếu bạn có quyền truy cập vào hệ thống, có thể thực hiện các bài kiểm tra kết quả sâu hơn bằng cách xây dựng các quan sát hoặc thực nghiệm mới. Điều này có thể tuân theo phương pháp luận khoa học: câu hỏi mà bạn đang kiểm tra là liệu kết quả benchmark có hợp lệ hay không. Từ đó, các giả thuyết và các dự đoán có thể được đưa ra và sau đó được kiểm tra để xác minh.

### 12.3.9 Phân tích Thống kê
Phân tích thống kê có thể được sử dụng để nghiên cứu dữ liệu benchmark. Nó tuân theo ba giai đoạn:
1. **Lựa chọn (Selection)** công cụ benchmark, cấu hình của nó, và các chỉ số hiệu năng hệ thống để thu thập.
2. **Thực thi (Execution)** benchmark, thu thập một tập dữ liệu lớn về các kết quả và các chỉ số.
3. **Diễn giải (Interpretation)** dữ liệu với phân tích thống kê, tạo ra một bản báo cáo.

Khác với benchmarking tích cực, thứ tập trung vào phân tích hệ thống trong khi benchmark đang chạy, phân tích thống kê tập trung vào việc phân tích các kết quả. Nó cũng khác biệt với benchmarking thụ động, trong đó không có phân tích nào được thực hiện.

Cách tiếp cận này được sử dụng trong các môi trường nơi quyền truy cập vào một hệ thống quy mô lớn có thể bị giới hạn về thời gian và tốn kém. Ví dụ, có thể chỉ có một "cấu hình tối đa" (max config) hệ thống có sẵn, nhưng nhiều nhóm muốn quyền truy cập để chạy các bài kiểm tra cùng một lúc, bao gồm:
- **Kinh doanh (Sales):** Trong quá trình proofs of concept, để chạy một mô phỏng tải khách hàng nhằm cho thấy cấu hình tối đa có thể mang lại những gì.
- **Tiếp thị (Marketing):** Để có được những con số tốt nhất cho một chiến dịch tiếp thị.
- **Hỗ trợ (Support):** Để điều tra các bệnh lý (pathologies) chỉ phát sinh trên hệ thống cấu hình tối đa, dưới tải nghiêm trọng.
- **Kỹ thuật (Engineering):** Để kiểm tra hiệu năng của các tính năng mới và thay đổi mã.
- **Chất lượng (Quality):** Để thực hiện các bài kiểm tra không hồi quy và các chứng nhận.

Mỗi nhóm có thể chỉ có một thời gian giới hạn để chạy các benchmarks của họ trên hệ thống, nhưng có nhiều thời gian hơn để phân tích các kết quả sau đó.

Vì việc thu thập các chỉ số là tốn kém, hãy nỗ lực thêm để đảm bảo rằng chúng là đáng tin cậy và đáng tin cậy, nhằm tránh việc phải làm lại sau này nếu có vấn đề được tìm thấy. Bên cạnh việc kiểm tra xem chúng được tạo ra như thế nào về mặt kỹ thuật, bạn cũng có thể thu thập thêm các thuộc tính thống kê để những vấn đề đó có thể được tìm thấy sớm hơn. Những thứ này có thể bao gồm các thống kê cho sự biến động, các phân phối đầy đủ, các sai số (error margins), và những thứ khác (xem Chương 2, Các phương pháp luận, Mục 2.8, Thống kê). Khi thực hiện benchmark cho các thay đổi hoặc kiểm tra không hồi quy, việc thấu hiểu biến động và các sai số là cực kỳ quan trọng để hiểu được ý nghĩa của một cặp kết quả.

Đồng thời thu thập càng nhiều dữ liệu hiệu năng càng tốt từ hệ thống đang chạy (mà không gây hại cho kết quả do chi phí thu thập) sao cho việc phân tích pháp chứng (forensic analysis) có thể được thực hiện sau đó trên dữ liệu này. Việc thu thập dữ liệu có thể bao gồm việc sử dụng các công cụ chẳng hạn như sar(1), các sản phẩm giám sát, và các công cụ tùy chỉnh trích xuất tất cả các thống kê có sẵn.

Ví dụ, trên Linux, một shell script tùy chỉnh có thể sao chép nội dung của các tệp bộ đếm /proc trước và sau lần chạy. Mọi thứ khả thi đều có thể được bao gồm, để đề phòng trường hợp nó cần thiết. Một script như vậy cũng có thể được thực thi theo các khoảng thời gian. Nhu cầu này, với điều kiện việc cung cấp chi phí hiệu năng là chấp nhận được. Các công cụ thống kê khác cũng có thể được sử dụng để tạo nhật ký.

Phân tích thống kê các kết quả và các chỉ số có thể bao gồm *phân tích khả năng mở rộng* (scalability analysis) và *lý thuyết hàng đợi* (queueing theory) để mô hình hóa hệ thống như một mạng lưới các hàng đợi. Những chủ đề này đã được giới thiệu trong Chương 2, Các phương pháp luận, và là chủ đề của các văn bản riêng biệt [Jain 91][Gunther 97][Gunther 07].

### 12.3.10 Benchmarking Checklist
Lấy cảm hứng từ Performance Mantras checklist (Chương 2, Các phương pháp luận, Mục 2.5.20, Performance Mantras) tôi đã tạo ra một checklist benchmarking gồm các câu hỏi mà bạn có thể tìm kiếm câu trả lời từ một benchmark để xác minh sự chính xác của nó [Gregg 18d]:
- Tại sao không gấp đôi? (Why not double?)
- Nó có phá vỡ các giới hạn không? (Did it break limits?)
- Nó có bị lỗi không? (Did it error?)
- Nó có tái hiện được không? (Does it reproduce?)
- Nó có quan trọng không? (Does it matter?)
- Nó có thực sự xảy ra không? (Did it even happen?)

Chi tiết hơn:
- **Tại sao không gấp đôi? (Why not double?)** Tại sao tốc độ hoạt động đã không gấp đôi kết quả benchmark? Đây thực sự là câu hỏi yếu tố hạn chế (limiter) là gì. Mục đích là để xác định các vấn đề thực sự của benchmarking, khi bạn khám phá ra rằng yếu tố hạn chế không phải là mục tiêu dự định của bài kiểm tra.
- **Nó có phá vỡ các giới hạn không? (Did it break limits?)** Đây là một kiểm tra tính hợp lý (Mục 12.3.8, Sanity Check).
- **Nó có bị lỗi không? (Did it error?)** Các lỗi thực thi khác với các thao tác bình thường, và một tỷ lệ lỗi cao sẽ làm sai lệch các kết quả benchmark.
- **Nó có tái hiện được không? (Does it reproduce?)** Các kết quả nhất quán như thế nào?
- **Nó có quan trọng không? (Does it matter?)** Khối lượng công việc của một bài kiểm tra benchmark cụ thể có thể không phù hợp với các nhu cầu sản xuất của bạn. Một số micro-benchmarks kiểm tra các syscalls và lệnh gọi thư viện riêng lẻ, nhưng ứng dụng của bạn có lẽ thậm chí còn không sử dụng chúng.
- **Nó có thực sự xảy ra không? (Did it even happen?)** Tiêu đề Ignoring Errors trước đó trong Mục 12.1.3, Thất bại Benchmarking, đã mô tả một trường hợp nơi một tường lửa chặn một benchmark đạt tới mục tiêu, và báo cáo độ trễ dựa trên thời gian hết hạn (timeout) là kết quả của nó.

Phần tiếp theo bao gồm một danh sách các câu hỏi dài hơn nhiều, thứ cũng hoạt động cho các kịch bản nơi bạn có thể không có quyền truy cập vào hệ thống mục tiêu để tự mình phân tích.

## 12.4 Các câu hỏi về Benchmark (Benchmark Questions)
Nếu một nhà cung cấp đưa cho bạn một kết quả benchmark, có một số câu hỏi bạn có thể hỏi để hiểu rõ hơn và áp dụng nó cho môi trường của bạn, ngay cả khi bạn không có quyền truy cập vào hệ thống đang chạy để phân tích nó. Mục tiêu là xác định những gì thực sự đang được đo lường và kết quả đó thực tế hoặc có thể lặp lại như thế nào.
- **Nói chung:**
  - Benchmark có liên quan đến khối lượng công việc sản xuất của tôi không?
  - Cấu hình của hệ thống được kiểm tra là gì?
  - Đó là một hệ thống đơn lẻ được kiểm tra, hay đây là kết quả của một cụm các hệ thống?
  - Chi phí của hệ thống đang kiểm tra là bao nhiêu?
  - Cấu hình của các máy khách benchmark là gì?
  - Benchmark có chạy thường xuyên không, vì vậy vấn đề này được bao quát như thế nào?
  - Thời lượng của bài kiểm tra là bao lâu? Các kết quả được thu thập như thế nào?
  - Kết quả là một giá trị trung bình hay một giá trị đỉnh cao? Giá trị trung bình là gì?
  - Các chi tiết phân phối khác là gì (độ lệch tiêu chuẩn, các phân vị (percentiles), hoặc các chi tiết phân phối đầy đủ)?
  - Yếu tố hạn chế của benchmark là gì?
  - Tỷ lệ thành công/thất bại của các thao tác là bao nhiêu?
  - Các thuộc tính thao tác là gì?
  - Các thuộc tính thao tác được chọn để mô phỏng một khối lượng công việc như thế nào? Chúng đã được lựa chọn như thế nào?
  - Benchmark có mô phỏng biến động, hay một mức trung bình ổn định?
  - Kết quả benchmark có được xác nhận bằng các công cụ phân tích khác không? (Cung cấp ảnh chụp màn hình.)
  - Một sai số (error margin) có thể được diễn đạt với kết quả benchmark không?
  - Kết quả benchmark có thể tái hiện được không?
- **Cho các benchmarks liên quan đến CPU/bộ nhớ:**
  - Những bộ xử lý nào đã được sử dụng?
  - Các bộ xử lý có được ép xung (overclocked) không? Có sử dụng tản nhiệt tùy chỉnh không (ví dụ: tản nhiệt nước)?
  - Có bao nhiêu mô-đun bộ nhớ (ví dụ: DIMMs) đã được sử dụng? Chúng được gắn vào các sockets như thế nào?
  - Có bất kỳ CPUs nào bị vô hiệu hóa không?
  - Mức sử dụng CPU trên toàn hệ thống là bao nhiêu? (Các hệ thống tải nhẹ có thể thực hiện nhanh hơn do mức độ turbo boosting cao hơn.)
  - Các CPUs được kiểm tra là các cores hay các hyperthreads?
  - Bao nhiêu bộ nhớ chính đã được cài đặt? Thuộc loại nào?
  - Có bất kỳ thiết lập BIOS tùy chỉnh nào được sử dụng không?
- **Cho các benchmarks liên quan đến lưu trữ:**
  - Cấu hình thiết bị lưu trữ là gì (bao nhiêu thiết bị đã được sử dụng, loại của chúng, giao thức lưu trữ, cấu hình RAID, kích thước bộ đệm ẩn, write-back hoặc write-through, v.v.)?
  - Cấu hình hệ thống tệp là gì (loại gì, bao nhiêu, cấu hình của chúng chẳng hạn như việc sử dụng journaling, và tinh chỉnh của chúng)?
  - Kích thước tập dữ liệu làm việc (working set size) là bao nhiêu?
  - Bộ đệm ẩn tập dữ liệu làm việc ở mức độ nào? Nó đã đệm ẩn ở đâu?
  - Có bao nhiêu tệp được truy cập?
- **Cho các benchmarks liên quan đến mạng:**
  - Cấu hình mạng là gì (bao nhiêu giao diện đã được sử dụng, loại và cấu hình của chúng)?
  - Topo mạng là gì?
  - Những giao thức nào đã được sử dụng? Các tùy chọn Socket?
  - Những thiết lập network stack nào đã được tinh chỉnh? Các tunables TCP/UDP?

Khi nghiên cứu các benchmarks ngành công nghiệp, nhiều câu hỏi trong số này có thể được trả lời từ các chi tiết công bố.

## 12.5 Các bài tập (Exercises)
1. Trả lời các câu hỏi khái niệm sau đây:
   - Một micro-benchmark là gì?
   - Kích thước tập dữ liệu làm việc (working set size) là gì, và nó có thể ảnh hưởng đến các kết quả của các benchmarks lưu trữ như thế nào?
   - Lý do cho việc nghiên cứu tỷ lệ price/performance là gì?

2. Chọn một micro-benchmark và thực hiện các tác vụ sau:
   - Chia tỉ lệ một chiều (số luồng, kích thước I/O...) và đo lường hiệu năng.
   - Vẽ đồ thị các kết quả (khả năng mở rộng).
   - Sử dụng benchmarking tích cực để thúc đẩy mục tiêu tới hiệu năng đỉnh cao, và phân tích yếu tố hạn chế.

## 12.6 Các tài liệu tham khảo (References)
- [Joy 81] Joy, W., “tcp-ip digest contribution,” http://www.rfc-editor.org/rfc/museum/tcp-ip-digest/tcp-ip-digest.v1n6.1, 1981.
- [Anon 85] Anon et al., “A Measure of Transaction Processing Power,” *Datamation*, April 1, 1985.
- [Jain 91] Jain, R., *The Art of Computer Systems Performance Analysis: Techniques for Experimental Design, Measurement, Simulation, and Modeling*, Wiley, 1991.
- [Gunther 97] Gunther, N., *The Practical Performance Analyst*, McGraw-Hill, 1997.
- [Shanley 98] Shanley, K., “History and Overview of the TPC,” http://www.tpc.org/information/about/history.asp, 1998.
- [Coker 01] Coker, R., “bonnie++,” https://www.coker.com.au/bonnie++, 2001.
- [Smaalders 06] Smaalders, B., “Performance Anti-Patterns,” *ACM Queue* 4, no. 1, February 2006.
- [Gunther 07] Gunther, N., *Guerrilla Capacity Planning*, Springer, 2007.
- [Bourbonnais 08] Bourbonnais, R., “Decoding Bonnie++,” https://blogs.oracle.com/roch/entry/decoding_bonnie, 2008.
- [DeWitt 08] DeWitt, D., and Levine, C., “Not Just Correct, but Correct and Fast,” *SIGMOD Record*, 2008.
- [Traeger 08] Traeger, A., Zadok, E., Joukov, N., and Wright, C., “A Nine Year Study of File System and Storage Benchmarking,” *ACM Transactions on Storage*, 2008.
- [Gregg 09b] Gregg, B., “Performance Testing the 7000 series, Part 3 of 3,” http://www.brendangregg.com/blog/2009-05-26/performance-testing-the-7000-series3.html, 2009.
- [Gregg 09c] Gregg, B., and Straughan, D., “Brendan Gregg at FROSUG, Oct 2009,” http://www.beginningwithi.com/2009/11/11/brendan-gregg-at-frosug-oct-2009, 2009.
- [Fulmer 12] Fulmer, J., “Siege Home,” https://www.joedog.org/siege-home, 2012.
- [Gregg 14c] Gregg, B., “The Benchmark Paradox,” http://www.brendangregg.com/blog/2014-05-03/the-benchmark-paradox.html, 2014.
- [Gregg 14d] Gregg, B., “Active Benchmarking,” http://www.brendangregg.com/activebenchmarking.html, 2014.
- [Gregg 18d] Gregg, B., “Evaluating the Evaluation: A Benchmarking Checklist,” http://www.brendangregg.com/blog/2018-06-30/benchmarking-checklist.html, 2018.
- [Glozer 19] Glozer, W., “Modern HTTP Benchmarking Tool,” https://github.com/wg/wrk, 2019.
- [TPC 19a] “Third Party Pricing Guideline,” http://www.tpc.org/information/other/pricing_guidelines.asp, 2019.
- [TPC 19b] “TPC,” http://www.tpc.org, 2019.
- [Dogan 20] Dogan, J., “HTTP load generator, ApacheBench (ab) replacement, formerly known as rakyll/boom,” https://github.com/rakyll/hey, last updated 2020.
- [SPEC 20] “Standard Performance Evaluation Corporation,” https://www.spec.org, accessed 2020.
