# Chương 5: Ứng dụng (Applications)

Hiệu năng được tinh chỉnh tốt nhất gần nơi công việc được thực hiện nhất: trong các ứng dụng. Chúng bao gồm máy chủ cơ sở dữ liệu, máy chủ web, máy chủ ứng dụng, bộ cân bằng tải, máy chủ tệp, và nhiều hơn nữa. Các chương tiếp theo tiếp cận ứng dụng từ góc nhìn của các tài nguyên mà chúng tiêu thụ: CPU, bộ nhớ, hệ thống tệp, đĩa, và mạng. Chương này đề cập đến cấp độ ứng dụng.

Bản thân các ứng dụng có thể trở nên cực kỳ phức tạp, đặc biệt trong các môi trường phân tán liên quan đến nhiều thành phần. Nghiên cứu nội bộ ứng dụng thường là lĩnh vực của nhà phát triển ứng dụng và có thể bao gồm việc sử dụng các công cụ của bên thứ ba để nội soi (introspection). Đối với những người nghiên cứu hiệu năng hệ thống, phân tích hiệu năng ứng dụng bao gồm cấu hình ứng dụng để sử dụng tốt nhất tài nguyên hệ thống, đặc trưng hóa cách ứng dụng sử dụng hệ thống, và phân tích các bệnh lý phổ biến.

Các mục tiêu học tập của chương này là:

- Mô tả các mục tiêu tinh chỉnh hiệu năng.
- Làm quen với các kỹ thuật cải thiện hiệu năng, bao gồm lập trình đa luồng (multithreaded programming), bảng băm (hash table), và I/O không chặn (non-blocking I/O).
- Hiểu các nguyên thủy khóa và đồng bộ hóa (locking and synchronization primitives) phổ biến.
- Hiểu các thách thức do các ngôn ngữ lập trình khác nhau đặt ra.
- Tuân theo phương pháp phân tích trạng thái luồng (thread state analysis methodology).
- Thực hiện lập hồ sơ CPU (CPU profiling) và phân tích off-CPU.
- Thực hiện phân tích lời gọi hệ thống (syscall analysis), bao gồm truy vết việc thực thi tiến trình.
- Nhận biết các bẫy của dấu vết ngăn xếp (stack trace gotchas): thiếu ký hiệu (symbol) và ngăn xếp.

Chương này thảo luận về các kiến thức cơ bản về ứng dụng, các nguyên lý cơ bản cho hiệu năng ứng dụng, ngôn ngữ lập trình và trình biên dịch, các chiến lược cho phân tích hiệu năng ứng dụng tổng quát, và các công cụ quan sát ứng dụng dựa trên hệ thống.

## 5.1 Kiến thức Cơ bản về Ứng dụng (Application Basics)

Trước khi đào sâu vào hiệu năng ứng dụng, bạn nên làm quen với vai trò của ứng dụng, các đặc điểm cơ bản của nó, và hệ sinh thái của nó trong ngành. Điều này tạo thành bối cảnh mà trong đó bạn có thể hiểu hoạt động của ứng dụng. Nó cũng mang đến cho bạn cơ hội tìm hiểu về các vấn đề hiệu năng phổ biến và tinh chỉnh, đồng thời cung cấp các hướng nghiên cứu sâu hơn. Để tìm hiểu bối cảnh này, hãy thử trả lời các câu hỏi sau:

- **Chức năng (Function)**: Vai trò của ứng dụng là gì? Nó là máy chủ cơ sở dữ liệu, máy chủ web, bộ cân bằng tải, máy chủ tệp, kho đối tượng (object store)?
- **Hoạt động (Operation)**: Ứng dụng phục vụ những yêu cầu nào, hoặc nó thực hiện những thao tác nào? Cơ sở dữ liệu phục vụ các truy vấn (và lệnh), máy chủ web phục vụ các yêu cầu HTTP, v.v. Điều này có thể được đo dưới dạng tốc độ (rate), để đánh giá tải và cho hoạch định dung lượng.
- **Yêu cầu hiệu năng (Performance requirements)**: Công ty vận hành ứng dụng có mục tiêu cấp dịch vụ (service level objective — SLO) không (ví dụ: 99,9% yêu cầu có độ trễ < 100 ms)?
- **Chế độ CPU (CPU mode)**: Ứng dụng được triển khai dưới dạng phần mềm cấp người dùng (user-level) hay cấp nhân (kernel-level)? Hầu hết các ứng dụng là cấp người dùng, thực thi dưới dạng một hoặc nhiều tiến trình, nhưng một số được triển khai dưới dạng dịch vụ nhân (ví dụ: NFS), và các chương trình BPF cũng là cấp nhân.
- **Cấu hình (Configuration)**: Ứng dụng được cấu hình như thế nào, và tại sao? Thông tin này có thể được tìm thấy trong tệp cấu hình hoặc qua các công cụ quản trị. Kiểm tra xem có bất kỳ tham số có thể tinh chỉnh nào liên quan đến hiệu năng đã được thay đổi không, bao gồm kích thước bộ đệm (buffer sizes), kích thước bộ nhớ đệm (cache sizes), mức song song (processes hoặc threads), và các tùy chọn khác.
- **Máy chủ (Host)**: Cái gì lưu trữ ứng dụng? Một máy chủ hay instance đám mây? CPU, topology bộ nhớ, thiết bị lưu trữ, v.v. là gì? Giới hạn của chúng là bao nhiêu?
- **Chỉ số (Metrics)**: Các chỉ số ứng dụng có được cung cấp không, chẳng hạn như tốc độ thao tác (operation rate)? Chúng có thể được cung cấp bởi các công cụ đi kèm hoặc công cụ bên thứ ba, qua các yêu cầu API, hoặc bằng cách xử lý nhật ký thao tác (operation logs).
- **Nhật ký (Logs)**: Ứng dụng tạo ra những nhật ký thao tác nào? Những nhật ký nào có thể được kích hoạt? Những chỉ số hiệu năng nào, bao gồm độ trễ, có sẵn từ nhật ký? Ví dụ, MySQL hỗ trợ nhật ký truy vấn chậm (slow query log), cung cấp chi tiết hiệu năng có giá trị cho mỗi truy vấn chậm hơn một ngưỡng nhất định.
- **Phiên bản (Version)**: Ứng dụng có phải là phiên bản mới nhất không? Có các bản sửa lỗi hiệu năng hoặc cải tiến được ghi nhận trong ghi chú phát hành (release notes) cho các phiên bản gần đây không?
- **Bug**: Có cơ sở dữ liệu bug cho ứng dụng không? Các bug "hiệu năng" cho phiên bản ứng dụng của bạn là gì? Nếu bạn có một vấn đề hiệu năng hiện tại, hãy tìm kiếm trong cơ sở dữ liệu bug để xem liệu điều gì tương tự đã xảy ra trước đó, cách nó được điều tra, và những gì khác có liên quan.
- **Mã nguồn (Source code)**: Ứng dụng có mã nguồn mở không? Nếu có, các đường dẫn mã được xác định bởi các trình lập hồ sơ (profiler) và trình truy vết (tracer) có thể được nghiên cứu, có thể dẫn đến các cải thiện hiệu năng. Bạn có thể tự sửa đổi mã ứng dụng để cải thiện hiệu năng, và gửi các cải tiến của mình upstream để đưa vào ứng dụng chính thức.
- **Cộng đồng (Community)**: Có cộng đồng cho ứng dụng nơi các phát hiện hiệu năng được chia sẻ không? Cộng đồng có thể bao gồm diễn đàn, blog, kênh Internet Relay Chat (IRC), các kênh chat khác (ví dụ: Slack), meetup, và hội nghị. Meetup và hội nghị thường đăng slide và video trực tuyến, là những tài nguyên hữu ích trong nhiều năm sau đó. Họ cũng có thể có một quản lý cộng đồng chia sẻ cập nhật và tin tức cộng đồng.
- **Sách (Books)**: Có sách về ứng dụng và/hoặc hiệu năng của nó không? Chúng có phải là sách tốt không (ví dụ: được viết bởi chuyên gia, thực tế/có thể hành động, sử dụng tốt thời gian của người đọc, cập nhật, v.v.)?
- **Chuyên gia (Experts)**: Ai là các chuyên gia hiệu năng được công nhận cho ứng dụng? Biết tên họ có thể giúp bạn tìm tài liệu mà họ đã viết.

Bất kể nguồn nào, bạn đang nhắm đến việc hiểu ứng dụng ở mức cao — nó làm gì, nó hoạt động như thế nào, và nó hoạt động hiệu năng ra sao. Một tài nguyên cực kỳ hữu ích, nếu bạn có thể tìm thấy, là một sơ đồ chức năng (functional diagram) minh họa nội bộ ứng dụng.

Các phần tiếp theo đề cập đến các kiến thức cơ bản khác về ứng dụng: đặt mục tiêu, tối ưu hóa trường hợp phổ biến, khả năng quan sát, và ký hiệu big O.

### 5.1.1 Mục tiêu (Objectives)

Một mục tiêu hiệu năng cung cấp hướng đi cho công việc phân tích hiệu năng của bạn và giúp bạn chọn những hoạt động nào cần thực hiện. Nếu không có mục tiêu rõ ràng, phân tích hiệu năng có nguy cơ biến thành chuyến "câu cá" ngẫu nhiên.

Đối với hiệu năng ứng dụng, bạn có thể bắt đầu với những thao tác mà ứng dụng thực hiện (như đã mô tả trước đó) và mục tiêu hiệu năng là gì. Mục tiêu có thể là:

- **Độ trễ (Latency)**: Thời gian phản hồi ứng dụng thấp hoặc nhất quán
- **Thông lượng (Throughput)**: Tốc độ thao tác ứng dụng hoặc tốc độ truyền dữ liệu cao
- **Sử dụng tài nguyên (Resource utilization)**: Hiệu quả cho một khối lượng công việc ứng dụng nhất định
- **Giá cả (Price)**: Cải thiện tỷ lệ hiệu năng/giá, giảm chi phí tính toán

Sẽ tốt hơn nếu những mục tiêu này có thể được định lượng bằng các chỉ số có thể được suy ra từ các yêu cầu kinh doanh hoặc chất lượng dịch vụ. Các ví dụ là:

- Độ trễ yêu cầu ứng dụng trung bình là 5 ms
- 95% yêu cầu hoàn thành với độ trễ 100 ms hoặc ít hơn
- Loại bỏ các giá trị ngoại lai (outlier) về độ trễ: không có yêu cầu nào vượt quá 1.000 ms
- Thông lượng tối đa ít nhất 10.000 yêu cầu ứng dụng mỗi giây trên mỗi máy chủ có kích thước nhất định<sup>1</sup>
- Sử dụng đĩa trung bình dưới 50% cho 10.000 yêu cầu ứng dụng mỗi giây

Khi một mục tiêu đã được chọn, bạn có thể làm việc trên các yếu tố giới hạn (limiter) cho mục tiêu đó. Đối với độ trễ, yếu tố giới hạn có thể là I/O đĩa hoặc mạng; đối với thông lượng, nó có thể là sử dụng CPU. Các chiến lược trong chương này và các chương khác sẽ giúp bạn xác định chúng.

> <sup>1</sup> Nếu kích thước máy chủ thay đổi (như với các instance đám mây). Điều này có thể được biểu thị tốt hơn theo tài nguyên giới hạn: ví dụ, tối đa 1.000 yêu cầu ứng dụng mỗi giây trên mỗi CPU, cho khối lượng công việc bị ràng buộc bởi CPU (CPU-bound workload).

Đối với các mục tiêu dựa trên thông lượng, lưu ý rằng không phải tất cả các thao tác đều bằng nhau về mặt hiệu năng hoặc chi phí. Nếu mục tiêu là một tốc độ thao tác nhất định, có thể quan trọng để cũng xác định loại thao tác đó là gì. Đây có thể là một phân phối dựa trên các khối lượng công việc dự kiến hoặc đo được.

Mục 5.2, Kỹ thuật Hiệu năng Ứng dụng, mô tả các phương pháp phổ biến để cải thiện hiệu năng ứng dụng. Một số phương pháp có thể hợp lý cho một mục tiêu nhưng không cho mục tiêu khác; ví dụ, chọn kích thước I/O lớn hơn có thể cải thiện thông lượng nhưng gây tổn hại cho độ trễ. Hãy nhớ mục tiêu mà bạn đang theo đuổi khi xác định chủ đề nào áp dụng nhất.

**Apdex**

Một số công ty sử dụng chỉ số hiệu năng ứng dụng mục tiêu (Application Performance Index — ApDex hoặc Apdex) như một mục tiêu và như một chỉ số để giám sát. Nó có thể truyền đạt tốt hơn trải nghiệm khách hàng và bao gồm việc đầu tiên phân loại các sự kiện khách hàng theo việc chúng là "thỏa đáng" (satisfactory), "chấp nhận được" (tolerable), hay "gây khó chịu" (frustrating). Apdex sau đó được tính bằng [Apdex 20]:

Apdex = (satisfactory + 0,5 × tolerable + 0 × frustrating) / total events

Kết quả Apdex nằm trong khoảng từ 0 (không có khách hàng hài lòng) đến 1 (tất cả khách hàng đều hài lòng).

### 5.1.2 Tối ưu hóa Trường hợp Phổ biến (Optimize the Common Case)

Nội bộ phần mềm có thể phức tạp, với nhiều đường dẫn mã và hành vi khác nhau. Điều này có thể đặc biệt rõ ràng nếu bạn duyệt mã nguồn: các ứng dụng thường có hàng chục nghìn dòng mã, trong khi nhân hệ điều hành lên đến hàng trăm nghìn dòng. Chọn các khu vực để tối ưu hóa một cách ngẫu nhiên có thể bao gồm rất nhiều công việc mà đạt được ít lợi ích.

Một cách để cải thiện hiệu năng ứng dụng hiệu quả là tìm đường dẫn mã phổ biến nhất cho khối lượng công việc sản xuất và bắt đầu bằng cách cải thiện đường dẫn đó. Nếu ứng dụng bị ràng buộc bởi CPU (CPU-bound), điều đó có thể có nghĩa là các đường dẫn mã thường xuyên trên CPU (on-CPU). Nếu ứng dụng bị ràng buộc bởi I/O (I/O-bound), bạn nên xem xét các đường dẫn mã thường xuyên dẫn đến I/O. Chúng có thể được xác định bằng cách phân tích và lập hồ sơ ứng dụng, bao gồm nghiên cứu dấu vết ngăn xếp (stack trace) và flame graph, như được đề cập trong các chương sau. Một mức ngữ cảnh cao hơn để hiểu trường hợp phổ biến cũng có thể được cung cấp bởi các công cụ quan sát ứng dụng.

### 5.1.3 Khả năng Quan sát (Observability)

Như tôi nhắc lại trong nhiều chương của cuốn sách này, những cải thiện hiệu năng lớn nhất có thể đến từ việc loại bỏ công việc không cần thiết.

Thực tế này đôi khi bị bỏ qua khi một ứng dụng đang được chọn dựa trên hiệu năng. Nếu benchmarking cho thấy ứng dụng A nhanh hơn ứng dụng B 10%, có thể hấp dẫn khi chọn ứng dụng A. Tuy nhiên, nếu ứng dụng A là không minh bạch (opaque) và ứng dụng B cung cấp một bộ công cụ quan sát phong phú, rất có khả năng ứng dụng B sẽ là lựa chọn tốt hơn về lâu dài. Những công cụ quan sát đó giúp có thể nhìn thấy và loại bỏ công việc không cần thiết, đồng thời hiểu và tinh chỉnh công việc đang hoạt động tốt hơn. Những cải thiện hiệu năng đạt được thông qua khả năng quan sát nâng cao có thể vượt xa sự khác biệt hiệu năng 10% ban đầu. Điều tương tự cũng đúng cho việc lựa chọn ngôn ngữ và runtime: chẳng hạn như chọn Java hoặc C, vốn trưởng thành và có nhiều công cụ quan sát, so với việc chọn một ngôn ngữ mới.

### 5.1.4 Ký hiệu Big O (Big O Notation)

Ký hiệu big O, thường được dạy như một chủ đề khoa học máy tính, được sử dụng để phân tích độ phức tạp của các thuật toán và để mô hình hóa cách chúng sẽ hoạt động khi tập dữ liệu đầu vào tăng quy mô. Chữ O đề cập đến bậc (order) của hàm, mô tả tốc độ tăng trưởng của nó. Ký hiệu này giúp các lập trình viên chọn các thuật toán hiệu quả hơn và có hiệu năng cao hơn khi phát triển ứng dụng [Knuth 76][Knuth 97].

Các ký hiệu big O phổ biến và ví dụ thuật toán được liệt kê trong Bảng 5.1.

**Bảng 5.1: Các ký hiệu big O ví dụ**

| Ký hiệu (Notation) | Ví dụ (Examples) |
|---|---|
| O(1) | Phép kiểm tra boolean (Boolean test) |
| O(log n) | Tìm kiếm nhị phân trong mảng đã sắp xếp (Binary search of a sorted array) |
| O(n) | Tìm kiếm tuyến tính trong danh sách liên kết (Linear search of a linked list) |
| O(n log n) | Sắp xếp nhanh — trường hợp trung bình (Quick sort — average case) |
| O(n²) | Sắp xếp nổi bọt — trường hợp trung bình (Bubble sort — average case) |
| O(2ⁿ) | Phân tích thừa số; tăng trưởng hàm mũ (Factoring numbers; exponential growth) |
| O(n!) | Tìm kiếm vét cạn bài toán người bán hàng du lịch (Brute force of traveling salesman problem) |

Ký hiệu này cho phép các lập trình viên ước tính tốc độ cải thiện của các thuật toán khác nhau, xác định những khu vực mã nào sẽ dẫn đến những cải thiện lớn nhất. Ví dụ, để tìm kiếm một mảng đã sắp xếp gồm 100 phần tử, sự khác biệt giữa tìm kiếm tuyến tính và tìm kiếm nhị phân là một hệ số 21 (100/log(100)).

Hiệu năng của các thuật toán này được minh họa trong Hình 5.1, cho thấy xu hướng của chúng khi tăng quy mô.

*Hình 5.1: Thời gian chạy so với kích thước đầu vào cho các thuật toán khác nhau*

Phân loại này giúp nhà phân tích hiệu năng hệ thống hiểu rằng một số thuật toán sẽ hoạt động rất kém ở quy mô lớn. Các vấn đề hiệu năng có thể xuất hiện khi ứng dụng bị đẩy để phục vụ nhiều người dùng hoặc đối tượng dữ liệu hơn bao giờ hết, tại thời điểm đó các thuật toán như O(n²) có thể bắt đầu trở nên bệnh lý (pathological). Cách sửa có thể là cho nhà phát triển sử dụng thuật toán hiệu quả hơn hoặc phân vùng quần thể (population) theo cách khác.

Ký hiệu big O bỏ qua một số chi phí tính toán hằng số phát sinh cho mỗi thuật toán. Đối với các trường hợp trong đó n (kích thước dữ liệu đầu vào) nhỏ, các chi phí này có thể chiếm ưu thế.

## 5.2 Kỹ thuật Hiệu năng Ứng dụng (Application Performance Techniques)

Phần này mô tả một số kỹ thuật phổ biến được sử dụng để cải thiện hiệu năng ứng dụng: chọn kích thước I/O, bộ nhớ đệm, sử dụng bộ đệm, bỏ phiếu, đồng thời và song song, I/O không chặn, và ràng buộc bộ xử lý. Tham khảo tài liệu ứng dụng để xem kỹ thuật nào được sử dụng, và để biết các tính năng bổ sung dành riêng cho ứng dụng.

### 5.2.1 Chọn Kích thước I/O (Selecting an I/O Size)

Các chi phí liên quan đến việc thực hiện I/O có thể bao gồm khởi tạo bộ đệm, thực hiện lời gọi hệ thống, chuyển đổi chế độ hoặc ngữ cảnh (mode or context switching), cấp phát metadata nhân, kiểm tra đặc quyền và giới hạn tiến trình, ánh xạ địa chỉ đến thiết bị, thực thi mã nhân và trình điều khiển để chuyển giao I/O, và cuối cùng, giải phóng metadata và bộ đệm. "Thuế khởi tạo" (initialization tax) được thanh toán cho I/O nhỏ và lớn như nhau. Để đạt hiệu quả, càng nhiều dữ liệu được truyền bởi mỗi I/O, càng tốt.

Tăng kích thước I/O là một chiến lược phổ biến được các ứng dụng sử dụng để cải thiện thông lượng. Thường hiệu quả hơn nhiều khi truyền 128 Kbyte như một I/O đơn lẻ so với 128 × 1 Kbyte I/O, xem xét bất kỳ chi phí cố định nào cho mỗi I/O. I/O đĩa quay (rotational disk I/O), cụ thể, lịch sử đã có chi phí cao cho mỗi I/O do thời gian tìm kiếm (seek time).

Có một nhược điểm khi ứng dụng không cần kích thước I/O lớn hơn. Một cơ sở dữ liệu thực hiện các lần đọc ngẫu nhiên 8 Kbyte có thể chạy chậm hơn với kích thước I/O đĩa 128 Kbyte, vì 120 Kbyte truyền dữ liệu bị lãng phí. Điều này tạo ra độ trễ I/O, có thể được giảm bằng cách chọn kích thước I/O nhỏ hơn phù hợp hơn với những gì ứng dụng đang yêu cầu. Kích thước I/O lớn hơn không cần thiết cũng có thể lãng phí không gian bộ nhớ đệm.

### 5.2.2 Bộ nhớ đệm (Caching)

Hệ điều hành sử dụng bộ nhớ đệm (cache) để cải thiện hiệu năng đọc hệ thống tệp và hiệu năng cấp phát bộ nhớ; các ứng dụng thường sử dụng bộ nhớ đệm vì lý do tương tự. Thay vì luôn thực hiện một thao tác tốn kém, kết quả của các thao tác được thực hiện phổ biến có thể được lưu trữ trong bộ nhớ đệm cục bộ để sử dụng trong tương lai. Một ví dụ là bộ nhớ đệm cơ sở dữ liệu (database buffer cache), lưu trữ dữ liệu từ các truy vấn cơ sở dữ liệu được thực hiện phổ biến.

Một nhiệm vụ phổ biến khi triển khai ứng dụng là xác định những bộ nhớ đệm nào được cung cấp, hoặc có thể được kích hoạt, và sau đó cấu hình kích thước của chúng cho phù hợp với hệ thống.

Trong khi bộ nhớ đệm cải thiện hiệu năng đọc, bộ nhớ lưu trữ của chúng thường được sử dụng làm bộ đệm (buffer) để cải thiện hiệu năng ghi.

### 5.2.3 Sử dụng Bộ đệm (Buffering)

Để cải thiện hiệu năng ghi, dữ liệu có thể được tổng hợp trong một bộ đệm trước khi được gửi đến cấp tiếp theo. Điều này làm tăng kích thước I/O và hiệu quả của thao tác. Tùy thuộc vào loại ghi, nó cũng có thể làm tăng độ trễ ghi, vì lần ghi đầu tiên vào bộ đệm phải chờ các lần ghi tiếp theo trước khi được gửi đi.

Bộ đệm vòng (ring buffer) (hoặc bộ đệm tròn — circular buffer) là một loại bộ đệm có kích thước cố định có thể được sử dụng để truyền liên tục giữa các thành phần, hoạt động trên bộ đệm một cách bất đồng bộ. Nó có thể được triển khai sử dụng các con trỏ bắt đầu và kết thúc, có thể được di chuyển bởi mỗi thành phần khi dữ liệu được thêm vào hoặc loại bỏ.

### 5.2.4 Bỏ phiếu (Polling)

Bỏ phiếu (polling) là một kỹ thuật trong đó hệ thống chờ đợi một sự kiện xảy ra bằng cách kiểm tra trạng thái của sự kiện trong một vòng lặp, với các khoảng dừng giữa các lần kiểm tra. Có một số vấn đề hiệu năng tiềm ẩn với polling khi có ít công việc để làm:

- Chi phí CPU tốn kém của các lần kiểm tra lặp đi lặp lại
- Độ trễ cao giữa thời điểm sự kiện xảy ra và lần kiểm tra polled tiếp theo

Khi đây là vấn đề hiệu năng, ứng dụng có thể thay đổi hành vi của chúng để lắng nghe (listen) sự kiện xảy ra, điều này ngay lập tức thông báo cho ứng dụng và thực thi routine mong muốn.

**Lời gọi Hệ thống poll()**

Có lời gọi hệ thống poll(2) để kiểm tra trạng thái của các bộ mô tả tệp (file descriptor), phục vụ chức năng tương tự như polling, mặc dù nó dựa trên sự kiện nên không chịu chi phí hiệu năng của polling.

Giao diện poll(2) hỗ trợ nhiều bộ mô tả tệp dưới dạng mảng, yêu cầu ứng dụng quét mảng khi sự kiện xảy ra để tìm các bộ mô tả tệp liên quan. Việc quét này là O(n) (xem Mục 5.1.4, Ký hiệu Big O), chi phí của nó có thể trở thành vấn đề hiệu năng ở quy mô lớn. Một lựa chọn thay thế trên Linux là epoll(2), có thể tránh việc quét và do đó là O(1). Trên BSD, tương đương là kqueue(2).

### 5.2.5 Đồng thời và Song song (Concurrency and Parallelism)

Các hệ thống chia sẻ thời gian (time-sharing systems) (bao gồm tất cả các hệ thống bắt nguồn từ Unix) cung cấp khả năng đồng thời chương trình (program concurrency): khả năng tải và bắt đầu thực thi nhiều chương trình có thể chạy (runnable). Trong khi thời gian chạy của chúng có thể chồng chéo, chúng không nhất thiết phải thực thi trên CPU vào cùng một thời điểm chính xác. Mỗi chương trình này có thể là một tiến trình ứng dụng.

Để tận dụng hệ thống đa bộ xử lý (multiprocessor), một ứng dụng phải thực thi trên nhiều CPU cùng lúc. Đây là tính song song (parallelism), mà ứng dụng có thể đạt được bằng cách sử dụng nhiều tiến trình (multiprocess) hoặc nhiều luồng (multithreaded), mỗi cái thực hiện nhiệm vụ riêng. Vì các lý do được giải thích trong Chương 6, CPU, Mục 6.3.13, Đa tiến trình, Đa luồng, nhiều luồng (hoặc các tác vụ tương đương) hiệu quả hơn và do đó là cách tiếp cận được ưa thích.

Ngoài việc tăng thông lượng công việc CPU, nhiều luồng (hoặc tiến trình) là một cách để cho phép I/O được thực hiện đồng thời, vì các luồng khác có thể thực thi trong khi một luồng bị chặn trên I/O đang chờ. (Cách khác là I/O bất đồng bộ — asynchronous I/O.)

Việc sử dụng kiến trúc đa tiến trình hoặc đa luồng có nghĩa là cho phép nhân quyết định ai sẽ chạy, thông qua bộ lập lịch CPU (CPU scheduler), và với chi phí chuyển đổi ngữ cảnh (context-switch overheads). Một cách tiếp cận khác là cho ứng dụng chế độ người dùng (user-mode) triển khai cơ chế lập lịch riêng và mô hình chương trình để nó có thể phục vụ các yêu cầu ứng dụng (hoặc chương trình) khác nhau trong cùng một luồng OS. Các cơ chế bao gồm:

- **Fiber**: Còn gọi là luồng nhẹ (lightweight threads), đây là phiên bản chế độ người dùng của luồng trong đó mỗi fiber đại diện cho một chương trình có thể lập lịch. Ứng dụng có thể sử dụng logic lập lịch riêng để chọn fiber nào sẽ chạy. Ví dụ, chúng có thể được sử dụng để phân bổ một fiber để xử lý mỗi yêu cầu ứng dụng, với chi phí ít hơn so với làm tương tự với luồng OS. Microsoft Windows, ví dụ, hỗ trợ fiber.<sup>2</sup>
- **Co-routine (Coroutine)**: Nhẹ hơn fiber, co-routine là một chương trình con (subroutine) có thể được lập lịch bởi ứng dụng chế độ người dùng, cung cấp một cơ chế cho đồng thời.
- **Đồng thời dựa trên sự kiện (Event-based concurrency)**: Các chương trình được chia nhỏ thành một loạt các bộ xử lý sự kiện (event handler), và các sự kiện có thể chạy được có thể được lên kế hoạch và thực thi từ một hàng đợi. Ví dụ, chúng có thể được sử dụng bằng cách phân bổ metadata cho mỗi yêu cầu ứng dụng, được tham chiếu bởi các bộ xử lý sự kiện. Ví dụ, runtime Node.js sử dụng đồng thời dựa trên sự kiện sử dụng một luồng worker sự kiện đơn lẻ (có thể trở thành nút thắt cổ chai, vì nó chỉ có thể thực thi trên một CPU).

Với tất cả các cơ chế này, I/O vẫn phải được xử lý bởi nhân, vì vậy việc chuyển đổi luồng OS thường là không thể tránh khỏi.<sup>3</sup> Ngoài ra, để đạt tính song song, nhiều luồng OS phải được sử dụng để chúng có thể được lập lịch trên nhiều CPU.

Một số runtime sử dụng cả co-routine cho đồng thời nhẹ và nhiều luồng OS cho tính song song. Một ví dụ là runtime Golang, sử dụng goroutine (co-routine) trên một pool luồng OS. Để cải thiện hiệu năng, khi một goroutine thực hiện lời gọi chặn (blocking call), bộ lập lịch của Golang tự động chuyển các goroutine khác trên luồng bị chặn sang các luồng khác để chạy [Golang 20].

Ba mô hình phổ biến của lập trình đa luồng là:

- **Pool luồng dịch vụ (Service thread pool)**: Một pool luồng phục vụ các yêu cầu mạng, trong đó mỗi luồng phục vụ một kết nối client tại một thời điểm.
- **Pool luồng CPU (CPU thread pool)**: Một luồng được tạo trên mỗi CPU. Điều này thường được sử dụng bởi xử lý hàng loạt dài hạn (long-duration batch processing), chẳng hạn như mã hóa video.
- **Kiến trúc hướng sự kiện phân tầng (Staged event-driven architecture — SEDA)**: Các yêu cầu ứng dụng được phân tách thành các giai đoạn có thể được xử lý bởi các pool gồm một hoặc nhiều luồng.

> <sup>2</sup> Tài liệu chính thức của Microsoft cảnh báo về các vấn đề mà fiber có thể gây ra: ví dụ, lưu trữ cục bộ luồng (thread-local storage) được chia sẻ giữa các fiber, vì vậy lập trình viên phải chuyển sang lưu trữ cục bộ fiber (fiber-local storage), và bất kỳ routine nào thoát khỏi luồng sẽ thoát tất cả fiber trên luồng đó. Tài liệu nêu rõ: "Nói chung, fiber không cung cấp lợi thế so với một ứng dụng đa luồng được thiết kế tốt" [Microsoft 18].

> <sup>3</sup> Với một số ngoại lệ, chẳng hạn như sử dụng sendfile(2) để tránh lời gọi hệ thống I/O, và Linux io_uring, cho phép không gian người dùng lập lịch I/O bằng cách ghi và đọc từ các hàng đợi io_uring (chúng được tóm tắt trong Mục 5.2.6, I/O Không chặn).

**Nguyên thủy Đồng bộ hóa (Synchronization Primitives)**

Vì lập trình đa luồng chia sẻ cùng không gian địa chỉ với tiến trình, các luồng có thể đọc và ghi cùng bộ nhớ trực tiếp, mà không cần các giao diện tốn kém hơn (chẳng hạn như giao tiếp liên tiến trình [IPC] cho lập trình đa tiến trình). Để đảm bảo tính toàn vẹn, các nguyên thủy đồng bộ hóa được sử dụng để dữ liệu không bị hỏng bởi nhiều luồng đọc và ghi đồng thời.

Các nguyên thủy đồng bộ hóa quản lý quyền truy cập vào bộ nhớ để đảm bảo tính toàn vẹn, và có thể hoạt động tương tự như đèn giao thông điều tiết quyền truy cập vào một giao lộ. Và, giống như đèn giao thông, chúng có thể dừng luồng giao thông, gây ra thời gian chờ (độ trễ). Ba loại phổ biến được sử dụng cho ứng dụng là:

- **Khóa Mutex (MUTually EXclusive)**: Chỉ người giữ khóa mới có thể thao tác. Những người khác bị chặn và chờ ngoài CPU (off-CPU).
- **Khóa quay (Spin lock)**: Khóa quay cho phép người giữ thao tác, trong khi những người khác quay trên CPU (on-CPU) trong một vòng lặp chặt, kiểm tra xem khóa đã được giải phóng chưa. Mặc dù chúng có thể cung cấp quyền truy cập độ trễ thấp — luồng bị chặn không bao giờ rời CPU và sẵn sàng chạy trong vài chu kỳ khi khóa có sẵn — chúng cũng lãng phí tài nguyên CPU trong khi các luồng quay, chờ đợi.
- **Khóa RW (RW lock)**: Khóa đọc/ghi (reader/writer lock) đảm bảo tính toàn vẹn bằng cách cho phép hoặc nhiều người đọc hoặc chỉ một người ghi và không có người đọc.
- **Semaphore**: Đây là kiểu biến có thể đếm (counting) để cho phép một số lượng thao tác song song nhất định, hoặc nhị phân (binary) để chỉ cho phép một (hiệu quả là khóa mutex).

Khóa mutex có thể được triển khai bởi thư viện hoặc nhân dưới dạng kết hợp (hybrid) của khóa quay và khóa mutex, quay nếu người giữ đang chạy trên CPU khác và chặn nếu không (hoặc nếu đạt ngưỡng quay). Chúng ban đầu được triển khai cho Linux vào năm 2009 [Zijlstra 09] và giờ có ba đường dẫn tùy thuộc vào trạng thái của khóa (như được mô tả trong Documentation/locking/mutex-design.rst [Molnar 20]):

1. **fastpath**: Cố gắng lấy khóa sử dụng lệnh cmpxchg để đặt chủ sở hữu. Điều này chỉ thành công nếu khóa không được giữ.
2. **midpath**: Còn gọi là quay lạc quan (optimistic spinning), quay trên CPU trong khi người giữ khóa cũng đang chạy, hy vọng rằng nó sẽ sớm được giải phóng và có thể được lấy mà không cần chặn.
3. **slowpath**: Chặn và hủy lịch luồng (deschedule), để được đánh thức sau khi khóa có sẵn.

Cơ chế đọc-sao chép-cập nhật (read-copy-update — RCU) của Linux là một cơ chế đồng bộ hóa khác được sử dụng nhiều cho mã nhân. Nó cho phép các thao tác đọc mà không cần lấy khóa, cải thiện hiệu năng so với các loại khóa khác. Với RCU, các thao tác ghi tạo một bản sao của dữ liệu được bảo vệ và cập nhật bản sao trong khi các thao tác đọc đang diễn ra vẫn có thể truy cập bản gốc. Nó có thể phát hiện khi không còn người đọc nào (dựa trên các điều kiện từng CPU khác nhau) và sau đó thay thế bản gốc bằng bản sao đã cập nhật [Linux 20e].

Việc điều tra các vấn đề hiệu năng liên quan đến khóa có thể tốn thời gian và thường yêu cầu sự quen thuộc với mã nguồn ứng dụng. Đây thường là một hoạt động dành cho nhà phát triển.

**Bảng Băm (Hash Tables)**

Một bảng băm (hash table) của các khóa có thể được sử dụng để sử dụng số lượng khóa tối ưu cho một số lượng lớn cấu trúc dữ liệu. Mặc dù bảng băm được tóm tắt ở đây, đây là một chủ đề nâng cao giả định nền tảng lập trình.

Hãy hình dung hai cách tiếp cận sau:

- Một khóa mutex toàn cục đơn lẻ cho tất cả cấu trúc dữ liệu. Mặc dù giải pháp này đơn giản, quyền truy cập đồng thời sẽ gặp tranh chấp (contention) cho khóa và độ trễ trong khi chờ đợi. Nhiều luồng cần khóa sẽ tuần tự hóa (serialize) — thực thi tuần tự, thay vì đồng thời.
- Một khóa mutex cho mỗi cấu trúc dữ liệu. Mặc dù điều này giảm tranh chấp chỉ xuống những lúc thực sự cần thiết — quyền truy cập đồng thời vào cùng cấu trúc dữ liệu — có chi phí lưu trữ cho khóa, và chi phí CPU cho việc tạo và hủy khóa cho mỗi cấu trúc dữ liệu.

Bảng băm của các khóa là giải pháp trung gian và phù hợp khi tranh chấp khóa được dự kiến là nhẹ. Một số lượng khóa cố định được tạo, và một thuật toán băm (hashing algorithm) được sử dụng để chọn khóa nào được sử dụng cho cấu trúc dữ liệu nào. Điều này tránh chi phí tạo và hủy với cấu trúc dữ liệu và cũng tránh vấn đề chỉ có một khóa duy nhất.

Bảng băm ví dụ được hiển thị trong Hình 5.2 có bốn mục, gọi là bucket, mỗi bucket chứa khóa riêng.

*Hình 5.2: Bảng băm ví dụ*

Ví dụ này cũng cho thấy một cách tiếp cận để giải quyết xung đột băm (hash collision), nơi hai hoặc nhiều cấu trúc dữ liệu đầu vào băm đến cùng bucket. Ở đây, một chuỗi (chain) các cấu trúc dữ liệu được tạo để lưu trữ tất cả dưới cùng bucket, nơi chúng sẽ được tìm thấy lại bởi hàm băm. Các chuỗi băm (hash chain) này có thể là vấn đề hiệu năng nếu chúng trở nên quá dài và được duyệt tuần tự, vì chúng được bảo vệ bởi chỉ một khóa có thể bắt đầu có thời gian giữ dài. Hàm băm và kích thước bảng có thể được chọn với mục tiêu phân bổ đều các cấu trúc dữ liệu trên nhiều bucket, để giữ độ dài chuỗi băm ở mức tối thiểu. Độ dài chuỗi băm nên được kiểm tra cho các khối lượng công việc sản xuất, trong trường hợp thuật toán băm không hoạt động như dự định và thay vào đó tạo ra các chuỗi băm dài hoạt động kém.

Lý tưởng nhất, số lượng bucket bảng băm nên bằng hoặc lớn hơn số CPU, cho tiềm năng tính song song tối đa. Thuật toán băm có thể đơn giản như lấy các bit bậc thấp<sup>4</sup> của địa chỉ cấu trúc dữ liệu và sử dụng đây làm chỉ mục vào một mảng khóa có kích thước lũy thừa của hai. Các thuật toán đơn giản như vậy cũng nhanh, cho phép các cấu trúc dữ liệu được định vị nhanh chóng.

> <sup>4</sup> Hoặc các bit ở giữa. Các bit bậc thấp nhất cho địa chỉ đến một mảng struct có thể có quá nhiều xung đột.

Với một mảng các khóa liền kề trong bộ nhớ, một vấn đề hiệu năng có thể phát sinh khi các khóa rơi vào cùng dòng bộ nhớ đệm (cache line). Hai CPU cập nhật các khóa khác nhau trong cùng dòng bộ nhớ đệm sẽ gặp chi phí nhất quán bộ nhớ đệm (cache coherency overhead), với mỗi CPU vô hiệu hóa dòng bộ nhớ đệm trong bộ nhớ đệm của CPU kia. Tình huống này được gọi là chia sẻ giả (false sharing) và thường được giải quyết bằng cách đệm (padding) các khóa với các byte không sử dụng để chỉ một khóa tồn tại trong mỗi dòng bộ nhớ đệm trong bộ nhớ.

### 5.2.6 I/O Không chặn (Non-Blocking I/O)

Vòng đời tiến trình Unix, được minh họa trong Chương 3, Hệ Điều Hành, cho thấy các tiến trình bị chặn và đi vào trạng thái ngủ (sleep state) trong khi I/O. Có một vài vấn đề hiệu năng với mô hình này:

- Mỗi thao tác I/O tiêu thụ một luồng (hoặc tiến trình) trong khi nó bị chặn. Để hỗ trợ nhiều I/O đồng thời, ứng dụng phải tạo nhiều luồng (thường là một cho mỗi client), chúng có chi phí liên quan đến việc tạo và hủy luồng, cũng như không gian ngăn xếp cần thiết để giữ chúng.
- Đối với I/O ngắn hạn thường xuyên, chi phí chuyển đổi ngữ cảnh thường xuyên có thể tiêu thụ tài nguyên CPU và thêm độ trễ ứng dụng.

Mô hình I/O không chặn (non-blocking I/O) phát I/O một cách bất đồng bộ, mà không chặn luồng hiện tại, sau đó luồng có thể thực hiện công việc khác. Đây là một tính năng chính của Node.js [Node.js 20], một môi trường ứng dụng JavaScript phía máy chủ hướng dẫn mã được phát triển theo cách không chặn.

Có một số cơ chế để thực hiện I/O không chặn hoặc bất đồng bộ, bao gồm:

- **open(2)**: Qua cờ O_ASYNC. Tiến trình được thông báo sử dụng tín hiệu (signal) khi I/O trở nên khả thi trên bộ mô tả tệp.
- **io_submit(2)**: I/O bất đồng bộ Linux (AIO).
- **sendfile(2)**: Sao chép dữ liệu từ một bộ mô tả tệp sang bộ khác, trì hoãn I/O cho nhân thay vì I/O cấp người dùng.<sup>5</sup>
- **io_uring_enter(2)**: Linux io_uring cho phép I/O bất đồng bộ được gửi sử dụng bộ đệm vòng (ring buffer) được chia sẻ giữa không gian người dùng và nhân [Axboe 19].

Kiểm tra tài liệu hệ điều hành của bạn để biết các phương pháp khác.

> <sup>5</sup> CDN của Netflix sử dụng điều này để gửi tài sản video cho khách hàng mà không có chi phí I/O cấp người dùng.

### 5.2.7 Ràng buộc Bộ xử lý (Processor Binding)

Đối với các môi trường NUMA, có thể có lợi khi một tiến trình hoặc luồng tiếp tục chạy trên một CPU đơn lẻ và chạy trên cùng CPU như trước đó sau khi thực hiện I/O. Điều này có thể cải thiện tính cục bộ bộ nhớ (memory locality) của ứng dụng, giảm các chu kỳ cho I/O bộ nhớ và cải thiện hiệu năng ứng dụng tổng thể. Các hệ điều hành nhận thức rõ điều này và được thiết kế để giữ các luồng ứng dụng trên cùng CPU (ái lực CPU — CPU affinity). Các chủ đề này được giới thiệu trong Chương 7, Bộ Nhớ.

Một số ứng dụng ép buộc hành vi này bằng cách tự ràng buộc (bind) vào các CPU. Điều này có thể cải thiện hiệu năng đáng kể cho một số hệ thống. Nó cũng có thể giảm hiệu năng khi các ràng buộc xung đột với các ràng buộc CPU khác, chẳng hạn như ánh xạ ngắt thiết bị (device interrupt mappings) đến CPU.

Hãy đặc biệt cẩn thận về rủi ro của việc ràng buộc CPU khi có các tenant hoặc ứng dụng khác chạy trên cùng hệ thống. Đây là vấn đề tôi đã gặp trong các môi trường ảo hóa OS (container), nơi một ứng dụng có thể thấy tất cả CPU và sau đó ràng buộc vào một số, với giả định rằng nó là ứng dụng duy nhất trên máy chủ. Khi một máy chủ được chia sẻ bởi các ứng dụng tenant khác cũng đang ràng buộc, nhiều tenant có thể vô tình ràng buộc vào cùng CPU, gây ra tranh chấp CPU và độ trễ bộ lập lịch ngay cả khi các CPU khác nhàn rỗi.

Trong suốt vòng đời của một ứng dụng, hệ thống máy chủ cũng có thể thay đổi, và các ràng buộc không được cập nhật có thể gây hại thay vì giúp hiệu năng, ví dụ khi chúng ràng buộc không cần thiết vào các CPU trên nhiều socket.

### 5.2.8 Các Châm ngôn Hiệu năng (Performance Mantras)

Để biết thêm các kỹ thuật cải thiện hiệu năng ứng dụng, xem phương pháp Châm ngôn Hiệu năng từ Chương 2. Tóm tắt:

1. Đừng làm điều đó (Don't do it).
2. Làm đi, nhưng đừng làm lại (Do it, but don't do it again).
3. Làm ít hơn (Do it less).
4. Làm sau (Do it later).
5. Làm khi họ không nhìn (Do it when they're not looking).
6. Làm đồng thời (Do it concurrently).
7. Làm rẻ hơn (Do it cheaper).

Mục đầu tiên, "Đừng làm điều đó," là loại bỏ công việc không cần thiết. Để biết thêm chi tiết về phương pháp luận này, xem Chương 2, Phương pháp luận, Mục 2.5.20, Châm ngôn Hiệu năng.

## 5.3 Ngôn ngữ Lập trình (Programming Languages)

Các ngôn ngữ lập trình có thể được biên dịch hoặc thông dịch và cũng có thể được thực thi qua máy ảo. Nhiều ngôn ngữ liệt kê "tối ưu hóa hiệu năng" như các tính năng, nhưng nói đúng ra, đây thường là các tính năng của phần mềm thực thi ngôn ngữ, không phải bản thân ngôn ngữ. Ví dụ, phần mềm Máy ảo Java HotSpot bao gồm trình biên dịch tức thời (just-in-time — JIT compiler) để cải thiện hiệu năng một cách động.

Các trình thông dịch và máy ảo ngôn ngữ cũng cung cấp các mức hỗ trợ khả năng quan sát hiệu năng khác nhau qua các công cụ cụ thể riêng của chúng. Đối với nhà phân tích hiệu năng hệ thống, lập hồ sơ cơ bản sử dụng các công cụ này có thể dẫn đến một số cải thiện nhanh. Ví dụ, mức sử dụng CPU cao có thể được xác định là kết quả của thu gom rác (garbage collection — GC) và sau đó được sửa qua một số tham số tinh chỉnh phổ biến. Hoặc nó có thể được gây ra bởi một đường dẫn mã có thể được tìm thấy là bug đã biết trong cơ sở dữ liệu bug và được sửa bằng cách nâng cấp phiên bản phần mềm (điều này xảy ra rất nhiều).

Các phần sau mô tả các đặc điểm hiệu năng cơ bản theo loại ngôn ngữ lập trình. Để biết thêm về hiệu năng ngôn ngữ riêng lẻ, hãy tìm các tài liệu về ngôn ngữ đó.

### 5.3.1 Ngôn ngữ Biên dịch (Compiled Languages)

Biên dịch (compilation) lấy một chương trình và tạo các lệnh máy trước thời gian chạy (runtime) được lưu trữ trong các tệp thực thi nhị phân gọi là binary, thường sử dụng Định dạng Liên kết và Thực thi (Executable and Linking Format — ELF) trên Linux và các hệ điều hành Unix phái sinh khác, và định dạng Portable Executable (PE) trên Windows. Chúng có thể được chạy bất kỳ lúc nào mà không cần biên dịch lại. Các ngôn ngữ biên dịch bao gồm C, C++, và assembly. Một số ngôn ngữ có thể có cả trình thông dịch và trình biên dịch.

Mã biên dịch thường có hiệu năng cao vì nó không yêu cầu dịch thêm trước khi CPU thực thi. Một ví dụ phổ biến về mã biên dịch là nhân Linux, được viết chủ yếu bằng C, với một số đường dẫn quan trọng được viết bằng assembly.

Phân tích hiệu năng của các ngôn ngữ biên dịch thường đơn giản, vì mã máy được thực thi thường ánh xạ chặt chẽ đến chương trình gốc (mặc dù điều này phụ thuộc vào các tối ưu hóa biên dịch). Trong quá trình biên dịch, một bảng ký hiệu (symbol table) có thể được tạo ánh xạ các địa chỉ đến các hàm chương trình và tên đối tượng. Việc lập hồ sơ và truy vết thực thi CPU sau đó có thể được ánh xạ trực tiếp đến các tên chương trình này, cho phép nhà phân tích nghiên cứu việc thực thi chương trình. Dấu vết ngăn xếp (stack trace), và các địa chỉ số mà chúng chứa, cũng có thể được ánh xạ và dịch sang tên hàm để cung cấp nguồn gốc đường dẫn mã.

Trình biên dịch có thể cải thiện hiệu năng bằng cách sử dụng tối ưu hóa biên dịch (compiler optimization) — các routine tối ưu hóa lựa chọn và vị trí đặt lệnh CPU.

**Tối ưu hóa Trình biên dịch (Compiler Optimizations)**

Trình biên dịch gcc(1) cung cấp bảy mức tối ưu hóa: 0, 1, 2, 3, s, fast, và g. Các số là một phạm vi trong đó 0 sử dụng ít tối ưu hóa nhất và 3 sử dụng nhiều nhất. Cũng có "s" để tối ưu hóa cho kích thước, "g" cho gỡ lỗi, và "fast" để sử dụng tất cả tối ưu hóa cộng thêm các tối ưu bổ sung bỏ qua tuân thủ tiêu chuẩn. Bạn có thể truy vấn gcc(1) để hiển thị những tối ưu hóa nào nó sử dụng cho các mức khác nhau. Ví dụ:

```
$ gcc -Q -O3 --help=optimizers
The following options control optimizations:
-O<number>
-Ofast
-Og
-Os
-faggressive-loop-optimizations           [enabled]
-falign-functions                         [disabled]
-falign-jumps                             [disabled]
-falign-label                             [enabled]
-falign-loops                             [disabled]
-fassociative-math                        [disabled]
-fasynchronous-unwind-tables              [enabled]
-fauto-inc-dec                            [enabled]
-fbranch-count-reg                        [enabled]
-fbranch-probabilities                    [disabled]
-fbranch-target-load-optimize             [disabled]
[...]
-fomit-frame-pointer                      [enabled]
[...]
```

Danh sách đầy đủ cho gcc phiên bản 7.4.0 bao gồm khoảng 230 tùy chọn, một số trong đó được kích hoạt ngay cả ở –O0. Như một ví dụ về những gì một trong các tùy chọn này làm, tùy chọn -fomit-frame-pointer, thấy trong danh sách này, được mô tả trong trang man gcc(1):

> Không giữ con trỏ khung (frame pointer) trong thanh ghi cho các hàm không cần nó. Điều này tránh các lệnh lưu, thiết lập và khôi phục con trỏ khung; nó cũng tạo thêm một thanh ghi khả dụng trong nhiều hàm. Nó cũng làm cho việc gỡ lỗi trở nên không thể trên một số máy.

Đây là ví dụ về đánh đổi (trade-off): bỏ qua con trỏ khung thường làm hỏng hoạt động của các trình phân tích lập hồ sơ dấu vết ngăn xếp.

Với tính hữu ích của các trình lập hồ sơ ngăn xếp, tùy chọn này có thể hy sinh nhiều về mặt các cải thiện hiệu năng sau này không thể dễ dàng tìm thấy nữa, điều có thể vượt xa các cải thiện hiệu năng mà tùy chọn này ban đầu mang lại. Một giải pháp, trong trường hợp này, có thể là biên dịch với -fno-omit-frame-pointer để tránh tối ưu hóa này.<sup>6</sup> Một tùy chọn được khuyến nghị khác là -g để bao gồm debuginfo, để hỗ trợ gỡ lỗi sau này. Debuginfo có thể được gỡ bỏ hoặc stripped sau nếu cần.<sup>7</sup>

Nếu các vấn đề hiệu năng phát sinh, có thể hấp dẫn khi chỉ đơn giản biên dịch lại ứng dụng với mức tối ưu hóa giảm (từ –O3 xuống –O2, ví dụ) với hy vọng rằng bất kỳ nhu cầu gỡ lỗi nào sau đó đều có thể được đáp ứng. Hóa ra điều này không đơn giản: các thay đổi đối với đầu ra trình biên dịch có thể rất lớn và quan trọng, và có thể ảnh hưởng đến hành vi của vấn đề bạn ban đầu đang cố phân tích.

> <sup>6</sup> Tùy thuộc vào trình lập hồ sơ, có thể có các giải pháp khác cho việc duyệt ngăn xếp (stack walking), chẳng hạn như sử dụng debuginfo, LBR, BTS, và nhiều hơn nữa. Đối với trình lập hồ sơ perf(1), các cách sử dụng các trình duyệt ngăn xếp khác nhau được mô tả trong Chương 13, perf, Mục 13.9, perf record.

> <sup>7</sup> Nếu bạn phân phối binary đã stripped, hãy xem xét tạo các gói debuginfo để thông tin gỡ lỗi có thể được cài đặt khi cần.

### 5.3.2 Ngôn ngữ Thông dịch (Interpreted Languages)

Ngôn ngữ thông dịch thực thi chương trình bằng cách dịch nó thành các hành động trong thời gian chạy, một quá trình thêm chi phí thực thi. Ngôn ngữ thông dịch không được kỳ vọng thể hiện hiệu năng cao và được sử dụng cho các tình huống mà các yếu tố khác quan trọng hơn, chẳng hạn như dễ lập trình và gỡ lỗi. Shell scripting là ví dụ về ngôn ngữ thông dịch.

Trừ khi các công cụ quan sát được cung cấp, phân tích hiệu năng của ngôn ngữ thông dịch có thể khó khăn. Lập hồ sơ CPU có thể cho thấy hoạt động của trình thông dịch — bao gồm phân tích cú pháp (parsing), dịch, và thực hiện hành động — nhưng nó có thể không hiển thị tên hàm chương trình gốc, khiến ngữ cảnh chương trình thiết yếu trở thành một bí ẩn. Phân tích trình thông dịch này có thể không hoàn toàn vô ích, vì có thể có các vấn đề hiệu năng với chính trình thông dịch, ngay cả khi mã mà nó đang thực thi có vẻ được thiết kế tốt.

Tùy thuộc vào trình thông dịch, ngữ cảnh chương trình có thể có sẵn dưới dạng đối số cho các hàm trình thông dịch, có thể được nhìn thấy sử dụng thiết bị đo đạc động (dynamic instrumentation). Một cách tiếp cận khác là kiểm tra bộ nhớ của tiến trình, với kiến thức về bố cục chương trình (ví dụ: sử dụng lời gọi hệ thống Linux process_vm_readv(2)).

Thường thì các chương trình này được nghiên cứu bằng cách đơn giản thêm các câu lệnh print và dấu thời gian. Phân tích hiệu năng nghiêm ngặt hơn là không phổ biến, vì ngôn ngữ thông dịch không thường được chọn cho các ứng dụng hiệu năng cao ngay từ đầu.

### 5.3.3 Máy ảo (Virtual Machines)

Máy ảo ngôn ngữ (language virtual machine) (còn gọi là máy ảo tiến trình — process virtual machine) là phần mềm mô phỏng một máy tính. Một số ngôn ngữ lập trình, bao gồm Java và Erlang, thường được thực thi sử dụng máy ảo (VM) cung cấp cho chúng một môi trường lập trình độc lập nền tảng (platform-independent). Chương trình ứng dụng được biên dịch thành bộ lệnh máy ảo (bytecode) và sau đó được thực thi bởi máy ảo. Điều này cho phép tính di động (portability) của các đối tượng đã biên dịch, miễn là có máy ảo để chạy chúng trên nền tảng mục tiêu.

Bytecode có thể được thực thi bởi máy ảo ngôn ngữ theo nhiều cách khác nhau. Máy ảo Java HotSpot hỗ trợ thực thi qua thông dịch và cũng qua biên dịch JIT, biên dịch bytecode thành mã máy để bộ xử lý thực thi trực tiếp. Điều này cung cấp các lợi thế hiệu năng của mã biên dịch, cùng với tính di động của máy ảo.

Máy ảo thường là loại ngôn ngữ khó quan sát nhất. Vào thời điểm chương trình đang thực thi trên CPU, nhiều giai đoạn biên dịch hoặc thông dịch có thể đã trải qua, và thông tin về chương trình gốc có thể không sẵn có. Phân tích hiệu năng thường tập trung vào bộ công cụ được cung cấp cùng máy ảo ngôn ngữ, nhiều trong số đó cung cấp USDT probe, và vào các công cụ bên thứ ba.

### 5.3.4 Thu gom Rác (Garbage Collection)

Một số ngôn ngữ sử dụng quản lý bộ nhớ tự động (automatic memory management), trong đó bộ nhớ được cấp phát không cần được giải phóng một cách rõ ràng, để lại điều đó cho một quá trình thu gom rác (garbage collection) bất đồng bộ. Mặc dù điều này làm cho các chương trình dễ viết hơn, có thể có các nhược điểm:

- **Tăng trưởng bộ nhớ (Memory growth)**: Có ít kiểm soát hơn đối với việc sử dụng bộ nhớ của ứng dụng, có thể tăng lên khi các đối tượng không được xác định tự động là đủ điều kiện để giải phóng. Nếu ứng dụng tăng quá lớn, nó có thể đạt giới hạn riêng hoặc gặp phân trang hệ thống (Linux swapping), gây hại nghiêm trọng cho hiệu năng.
- **Chi phí CPU (CPU cost)**: GC thường chạy không liên tục và bao gồm việc tìm kiếm hoặc quét các đối tượng trong bộ nhớ. Điều này tiêu thụ tài nguyên CPU, giảm những gì có sẵn cho ứng dụng trong các khoảng thời gian ngắn. Khi bộ nhớ của ứng dụng tăng, tiêu thụ CPU bởi GC cũng có thể tăng. Trong một số trường hợp, điều này có thể đạt đến mức GC liên tục tiêu thụ toàn bộ một CPU.
- **Giá trị ngoại lai độ trễ (Latency outliers)**: Thực thi ứng dụng có thể bị tạm dừng trong khi GC thực thi, gây ra các phản hồi ứng dụng đôi khi có độ trễ cao do bị GC gián đoạn.<sup>8</sup> Điều này phụ thuộc vào loại GC: dừng toàn bộ thế giới (stop-the-world), tăng dần (incremental), hoặc đồng thời (concurrent).

GC là mục tiêu phổ biến để tinh chỉnh hiệu năng nhằm giảm chi phí CPU và sự xuất hiện của các giá trị ngoại lai độ trễ. Ví dụ, Java VM cung cấp nhiều tham số có thể tinh chỉnh để đặt loại GC, số luồng GC, kích thước heap tối đa, tỷ lệ heap trống mục tiêu, và nhiều hơn nữa.

Nếu tinh chỉnh không hiệu quả, vấn đề có thể là ứng dụng tạo quá nhiều rác, hoặc rò rỉ tham chiếu (leaking references). Đây là các vấn đề để nhà phát triển ứng dụng giải quyết. Một cách tiếp cận là cấp phát ít đối tượng hơn, khi có thể, để giảm tải GC. Các công cụ quan sát cho thấy các cấp phát đối tượng và đường dẫn mã của chúng có thể được sử dụng để tìm các mục tiêu tiềm năng để loại bỏ.

> <sup>8</sup> Đã có nhiều nghiên cứu về các kỹ thuật để giảm thời gian GC hoặc gián đoạn ứng dụng từ GC. Một ví dụ sử dụng các chỉ số hệ thống và ứng dụng để xác định thời điểm tốt nhất để gọi GC [Schwartz 18].

## 5.4 Phương pháp luận (Methodology)

Phần này mô tả các phương pháp luận cho phân tích và tinh chỉnh ứng dụng. Các công cụ được sử dụng để phân tích hoặc được giới thiệu ở đây hoặc được tham chiếu từ các chương khác. Các phương pháp luận được tóm tắt trong Bảng 5.2.

**Bảng 5.2: Các phương pháp luận hiệu năng ứng dụng**

| Mục | Phương pháp luận | Loại |
|---|---|---|
| 5.4.1 | Lập hồ sơ CPU (CPU profiling) | Phân tích quan sát |
| 5.4.2 | Lập hồ sơ Off-CPU (Off-CPU profiling) | Phân tích quan sát |
| 5.4.3 | Phân tích syscall (Syscall analysis) | Phân tích quan sát |
| 5.4.4 | Phương pháp USE (USE method) | Phân tích quan sát |
| 5.4.5 | Phân tích trạng thái luồng (Thread state analysis) | Phân tích quan sát |
| 5.4.6 | Phân tích khóa (Lock analysis) | Phân tích quan sát |
| 5.4.7 | Tinh chỉnh hiệu năng tĩnh (Static performance tuning) | Phân tích quan sát, tinh chỉnh |
| 5.4.8 | Truy vết phân tán (Distributed tracing) | Phân tích quan sát |

Xem Chương 2, Phương pháp luận, để giới thiệu một số phương pháp trong đó, và cũng có các phương pháp luận tổng quát bổ sung: đối với ứng dụng, đặc biệt hãy xem xét lập hồ sơ CPU, đặc trưng hóa khối lượng công việc, và phân tích đào sâu (drill-down analysis). Cũng xem các chương tiếp theo cho phân tích tài nguyên hệ thống và ảo hóa.

Các phương pháp luận này có thể được theo dõi riêng lẻ hoặc sử dụng kết hợp. Đề xuất của tôi là thử chúng theo thứ tự được liệt kê trong bảng.

Ngoài những phương pháp này, hãy tìm các kỹ thuật phân tích tùy chỉnh cho ứng dụng cụ thể và ngôn ngữ lập trình mà nó được phát triển. Chúng có thể xem xét hành vi logic của ứng dụng, bao gồm các vấn đề đã biết, và dẫn đến một số cải thiện hiệu năng nhanh chóng.

### 5.4.1 Lập hồ sơ CPU (CPU Profiling)

Lập hồ sơ CPU là một hoạt động thiết yếu cho phân tích hiệu năng ứng dụng và được giải thích trong Chương 6, CPU, bắt đầu từ Mục 6.5.4, Lập hồ sơ. Phần này tóm tắt lập hồ sơ CPU và CPU flame graph, và mô tả cách lập hồ sơ CPU có thể được sử dụng cho một số phân tích off-CPU.

Có nhiều trình lập hồ sơ CPU cho Linux, bao gồm perf(1) và profile(8), được tóm tắt trong Mục 5.5, Công cụ Quan sát, cả hai đều sử dụng lấy mẫu theo thời gian (timed sampling). Các trình lập hồ sơ này chạy trong chế độ nhân và có thể thu cả ngăn xếp nhân và người dùng, tạo ra hồ sơ chế độ hỗn hợp (mixed-mode profile). Điều này cung cấp khả năng hiển thị (gần như) hoàn chỉnh cho việc sử dụng CPU.

Các ứng dụng và runtime đôi khi cung cấp trình lập hồ sơ riêng chạy trong chế độ người dùng, không thể hiển thị việc sử dụng CPU nhân. Các trình lập hồ sơ dựa trên người dùng này có thể có khái niệm lệch về thời gian CPU vì chúng có thể không biết khi nhân đã hủy lịch ứng dụng, và không tính toán điều đó. Tôi luôn bắt đầu với các trình lập hồ sơ dựa trên nhân (perf(1) và profile(8)) và sử dụng trình lập hồ sơ dựa trên người dùng như phương sách cuối cùng.

Các trình lập hồ sơ dựa trên mẫu tạo ra nhiều mẫu: một hồ sơ CPU điển hình tại Netflix thu thập dấu vết ngăn xếp ở 49 Hertz trên (khoảng) 32 CPU trong 30 giây: điều này tạo ra tổng cộng 47.040 mẫu. Để hiểu được chúng, các trình lập hồ sơ thường cung cấp các cách khác nhau để tóm tắt hoặc trực quan hóa chúng. Một trực quan hóa phổ biến cho các dấu vết ngăn xếp được lấy mẫu được gọi là **flame graph**, mà tôi đã phát minh.

**CPU Flame Graph**

Một CPU flame graph đã được hiển thị trong Chương 1, và một trích đoạn ví dụ khác được hiển thị là Hình 2.15. Ví dụ Hình 5.3 bao gồm chú thích ext4 để tham khảo sau. Đây là các flame graph chế độ hỗn hợp, hiển thị cả ngăn xếp người dùng và nhân.

Trong flame graph, mỗi hình chữ nhật là một khung (frame) từ dấu vết ngăn xếp, và trục y hiển thị luồng mã: từ trên xuống hiển thị hàm hiện tại và sau đó là tổ tiên của nó. Chiều rộng khung tỷ lệ thuận với sự hiện diện của nó trong hồ sơ, và thứ tự trục x không có ý nghĩa (đó là sắp xếp theo bảng chữ cái). Bạn tìm kiếm các "cao nguyên" hoặc "tháp" lớn — đó là nơi phần lớn thời gian CPU được dành.

Xem Chương 6, CPU, Mục 6.7.3, Flame Graph, để biết thêm chi tiết về flame graph.

*Hình 5.3: Trích đoạn CPU flame graph*

Trong Hình 5.3, crc32_z() là hàm ở trên CPU nhiều nhất, chiếm khoảng 40% trích đoạn này (cao nguyên ở giữa). Một tháp bên trái cho thấy đường dẫn syscall write(2) vào nhân, chiếm khoảng 30% tổng thời gian CPU. Với một cái nhìn nhanh, chúng ta đã xác định hai mục tiêu cấp thấp có thể để tối ưu hóa. Duyệt nguồn gốc đường dẫn mã (xuống dưới) có thể tiết lộ các mục tiêu cấp cao: trong trường hợp này, tất cả việc sử dụng CPU là từ hàm MYSQL_BIN_LOG::commit().

Tôi không biết crc32_z() hoặc MYSQL_BIN_LOG::commit() làm gì (mặc dù tôi có thể đoán). Hồ sơ CPU phơi bày hoạt động bên trong của ứng dụng, và trừ khi bạn là nhà phát triển ứng dụng, bạn không được kỳ vọng biết bất kỳ hàm nào trong số này là gì. Bạn sẽ cần nghiên cứu chúng để phát triển các cải thiện hiệu năng có thể hành động.

Ví dụ, tôi đã thực hiện tìm kiếm internet cho MYSQL_BIN_LOG::commit() và nhanh chóng tìm thấy các bài viết mô tả nhật ký nhị phân MySQL (MySQL binary logging), được sử dụng cho khôi phục và sao chép cơ sở dữ liệu, và cách nó có thể được tinh chỉnh hoặc tắt hoàn toàn. Tìm kiếm nhanh cho crc32_z() cho thấy nó là hàm tính tổng kiểm tra (checksumming function) từ zlib. Có lẽ có phiên bản zlib mới hơn và nhanh hơn? Bộ xử lý có lệnh CRC tối ưu hóa không, và zlib có sử dụng nó không? MySQL thậm chí có cần tính CRC không, hay nó có thể được tắt? Xem Chương 2, Phương pháp luận, Mục 2.5.20, Châm ngôn Hiệu năng, để biết thêm về phong cách tư duy này.

Mục 5.5.1, perf, tóm tắt hướng dẫn để tạo CPU flame graph sử dụng perf(1).

**Dấu chân Off-CPU (Off-CPU Footprints)**

Hồ sơ CPU có thể cho thấy nhiều hơn chỉ việc sử dụng CPU. Bạn có thể tìm bằng chứng của các loại vấn đề off-CPU khác. I/O đĩa, ví dụ, có thể được nhìn thấy ở một mức độ nào đó qua việc sử dụng CPU cho truy cập hệ thống tệp và khởi tạo I/O khối. Điều này giống như tìm dấu chân của một con gấu: bạn không thấy con gấu, nhưng bạn đã phát hiện ra rằng có một con tồn tại.

Bằng cách duyệt CPU flame graph, bạn có thể tìm thấy bằng chứng về I/O hệ thống tệp, I/O đĩa, I/O mạng, tranh chấp khóa, và nhiều hơn nữa. Hình 5.3 làm nổi bật I/O hệ thống tệp ext4 như một ví dụ. Nếu bạn duyệt đủ flame graph, bạn sẽ trở nên quen thuộc với các tên hàm để tìm kiếm: "tcp_*" cho các hàm TCP nhân, "blk_*" cho các hàm I/O khối nhân, v.v. Đây là một số thuật ngữ tìm kiếm được đề xuất cho hệ thống Linux:

- "ext4" (hoặc "btrfs", "xfs", "zfs"): để tìm hoạt động hệ thống tệp.
- "blk": để tìm I/O khối.
- "tcp": để tìm I/O mạng.
- "utex": để hiển thị tranh chấp khóa ("mutex" hoặc "futex").
- "alloc" hoặc "object": để hiển thị đường dẫn mã thực hiện cấp phát bộ nhớ.

Phương pháp này chỉ xác định sự hiện diện của các hoạt động này, không phải độ lớn của chúng. CPU flame graph hiển thị độ lớn của việc sử dụng CPU, không phải thời gian bị chặn off-CPU. Để đo thời gian off-CPU trực tiếp, bạn có thể sử dụng phân tích off-CPU, được đề cập tiếp theo, mặc dù nó thường tốn chi phí lớn hơn để đo.

### 5.4.2 Phân tích Off-CPU (Off-CPU Analysis)

Phân tích off-CPU là nghiên cứu các luồng hiện không chạy trên CPU: Trạng thái này được gọi là off-CPU. Nó bao gồm tất cả các lý do mà luồng bị chặn: I/O đĩa, I/O mạng, tranh chấp khóa, ngủ rõ ràng (explicit sleep), ưu tiên bộ lập lịch (scheduler preemption), v.v. Phân tích các lý do này và các vấn đề hiệu năng mà chúng gây ra thường bao gồm nhiều công cụ khác nhau. Phân tích off-CPU là một phương pháp để phân tích tất cả, và có thể được hỗ trợ bởi một công cụ lập hồ sơ off-CPU đơn lẻ.

Lập hồ sơ off-CPU có thể được thực hiện theo nhiều cách khác nhau, bao gồm:

- **Lấy mẫu (Sampling)**: Thu thập các mẫu dựa trên bộ hẹn giờ của các luồng off-CPU, hoặc đơn giản là tất cả các luồng (gọi là lấy mẫu wallclock).
- **Truy vết bộ lập lịch (Scheduler tracing)**: Đo đạc bộ lập lịch CPU nhân để đo thời gian mà luồng off-CPU, và ghi lại các thời gian này với dấu vết ngăn xếp off-CPU. Dấu vết ngăn xếp không thay đổi khi luồng off-CPU (vì nó không chạy để thay đổi), nên dấu vết ngăn xếp chỉ cần được đọc một lần cho mỗi sự kiện chặn.
- **Thiết bị đo đạc ứng dụng (Application instrumentation)**: Một số ứng dụng có thiết bị đo đạc tích hợp cho các đường dẫn mã thường chặn, chẳng hạn như I/O đĩa. Thiết bị đo đạc này có thể bao gồm ngữ cảnh cụ thể cho ứng dụng. Mặc dù tiện lợi và hữu ích, cách tiếp cận này thường mù (blind) đối với các sự kiện off-CPU (ưu tiên bộ lập lịch, lỗi trang — page fault, v.v.).

Hai cách tiếp cận đầu tiên được ưa thích vì chúng hoạt động cho tất cả ứng dụng và có thể thấy tất cả sự kiện off-CPU; tuy nhiên, chúng đi kèm với chi phí lớn. Lấy mẫu ở 49 Hertz nên có chi phí không đáng kể trên, giả sử, hệ thống 8-CPU, nhưng lấy mẫu off-CPU phải lấy mẫu pool luồng thay vì pool CPU. Cùng hệ thống có thể có 10.000 luồng, hầu hết nhàn rỗi, nên lấy mẫu chúng tăng chi phí lên 1.000 lần<sup>9</sup> (hãy tưởng tượng lập hồ sơ CPU trên hệ thống 10.000-CPU). Truy vết bộ lập lịch cũng có thể tốn chi phí đáng kể, vì cùng hệ thống có thể có 100.000 sự kiện bộ lập lịch hoặc hơn mỗi giây.

> <sup>9</sup> Có thể cao hơn, vì nó sẽ yêu cầu lấy mẫu dấu vết ngăn xếp cho các luồng off-CPU, và ngăn xếp của chúng không thể nằm trong bộ nhớ đệm CPU (không giống với lập hồ sơ CPU). Hạn chế nó cho một ứng dụng đơn lẻ nên giúp giảm số luồng, mặc dù hồ sơ sẽ không đầy đủ.

Truy vết bộ lập lịch là kỹ thuật hiện thường được sử dụng, dựa trên các công cụ của tôi như offcputime(8) (Mục 5.5.3, offcputime). Một tối ưu hóa tôi sử dụng là chỉ ghi lại các sự kiện off-CPU vượt quá một thời gian nhỏ, giảm số lượng mẫu.<sup>10</sup> Tôi cũng sử dụng BPF để tổng hợp ngăn xếp trong ngữ cảnh nhân, thay vì phát tất cả mẫu ra không gian người dùng, giảm chi phí hơn nữa. Dù các kỹ thuật này giúp ích, bạn nên cẩn thận với lập hồ sơ off-CPU trong sản xuất, và đánh giá chi phí trong môi trường thử nghiệm trước khi sử dụng.

> <sup>10</sup> Trước khi bạn nói "nếu có một trận lũ các thời gian ngủ nhỏ bị loại trừ bởi tối ưu hóa này thì sao?" — bạn nên thấy bằng chứng của nó trong hồ sơ CPU do gọi bộ lập lịch quá thường xuyên, thúc đẩy bạn tắt tối ưu hóa này.

**Flame Graph Thời gian Off-CPU (Off-CPU Time Flame Graphs)**

Hồ sơ off-CPU có thể được trực quan hóa dưới dạng flame graph thời gian off-CPU. Hình 5.4 cho thấy hồ sơ off-CPU toàn hệ thống 30 giây, nơi tôi đã phóng to để hiển thị một luồng máy chủ MySQL xử lý lệnh (truy vấn).

*Hình 5.4: Flame graph thời gian off-CPU, đã phóng to*

Phần lớn thời gian off-CPU nằm trong đường dẫn mã fsync() và hệ thống tệp ext4. Con trỏ chuột ở trên một hàm, Prepared_statement::execute(), để chứng minh rằng dòng thông tin ở dưới cho thấy thời gian off-CPU trong hàm này: tổng cộng 3,97 giây. Cách diễn giải tương tự như đối với CPU flame graph: tìm các tháp rộng nhất và điều tra chúng trước.

Bằng cách sử dụng cả flame graph on- và off-CPU, bạn có cái nhìn đầy đủ về thời gian on- và off-CPU theo đường dẫn mã: một công cụ mạnh mẽ. Tôi thường hiển thị chúng dưới dạng flame graph riêng biệt. Có thể kết hợp chúng thành một flame graph đơn lẻ, mà tôi gọi là **flame graph nóng/lạnh (hot/cold flame graph)**. Nó không hoạt động tốt: thời gian CPU bị ép vào một tháp mỏng vì phần lớn flame graph nóng/lạnh hiển thị thời gian chờ. Điều này vì số luồng off-CPU có thể lớn hơn số luồng đang chạy on-CPU gấp hai bậc lớn, khiến flame graph nóng/lạnh bao gồm 99% thời gian off-CPU, mà (trừ khi được lọc) chủ yếu là thời gian chờ.

**Thời gian Chờ (Wait Time)**

Ngoài chi phí thu thập hồ sơ off-CPU, một vấn đề khác là diễn giải chúng: chúng có thể bị chi phối bởi thời gian chờ (wait time). Đây là thời gian các luồng chờ đợi công việc. Hình 5.5 hiển thị cùng flame graph thời gian off-CPU, nhưng không phóng to vào một luồng thú vị.

*Hình 5.5: Flame graph thời gian off-CPU, đầy đủ*

Hầu hết thời gian trong flame graph này bây giờ nằm trong đường dẫn mã pthread_cond_wait() và futex() tương tự: đây là các luồng chờ đợi công việc. Các hàm luồng có thể được nhìn thấy trong flame graph: từ phải sang trái, có srv_worker_thread(), srv_purge_coordinator_thread(), srv_monitor_thread(), v.v.

Có một vài kỹ thuật để tìm thời gian off-CPU quan trọng:

- Phóng to (hoặc lọc theo) các hàm xử lý yêu cầu ứng dụng, vì chúng ta quan tâm nhất đến thời gian off-CPU trong quá trình xử lý yêu cầu ứng dụng. Đối với máy chủ MySQL, đây là hàm do_command(). Tìm kiếm do_command() và sau đó phóng to tạo ra flame graph tương tự như Hình 5.4. Mặc dù cách tiếp cận này hiệu quả, bạn sẽ cần biết hàm nào để tìm kiếm trong ứng dụng cụ thể của mình.
- Sử dụng bộ lọc nhân (kernel filter) trong quá trình thu thập để loại trừ các trạng thái luồng không thú vị. Hiệu quả phụ thuộc vào nhân; trên Linux, khớp với TASK_UNINTERRUPTIBLE tập trung vào nhiều sự kiện off-CPU thú vị, nhưng cũng loại trừ một số.

Đôi khi bạn sẽ tìm thấy các đường dẫn mã chặn ứng dụng đang chờ thứ gì đó khác, chẳng hạn như khóa. Để đào sâu hơn, bạn cần biết tại sao người giữ khóa mất quá lâu để giải phóng nó. Ngoài phân tích khóa, được mô tả trong Mục 5.4.7, Tinh chỉnh Hiệu năng Tĩnh, một kỹ thuật tổng quát là đo đạc sự kiện đánh thức (waker event). Đây là một hoạt động nâng cao: xem Chương 14 của BPF Performance Tools [Gregg 19], và các công cụ wakeuptime(8) và offwaketime(8) từ BCC.

Mục 5.5.3, offcputime, hiển thị hướng dẫn để tạo flame graph off-CPU sử dụng offcputime(8) từ BCC. Ngoài các sự kiện bộ lập lịch, các sự kiện syscall là một mục tiêu hữu ích khác để nghiên cứu ứng dụng.

### 5.4.3 Phân tích Syscall (Syscall Analysis)

Lời gọi hệ thống (syscall) có thể được đo đạc để nghiên cứu các vấn đề hiệu năng dựa trên tài nguyên. Mục đích là tìm ra thời gian syscall được dành ở đâu, bao gồm loại syscall và lý do nó được gọi.

Các mục tiêu cho phân tích syscall bao gồm:

- **Truy vết tiến trình mới (New process tracing)**: Bằng cách truy vết syscall execve(2), bạn có thể ghi nhật ký việc thực thi tiến trình mới, và phân tích các vấn đề của tiến trình tồn tại ngắn. Xem công cụ execsnoop(8) trong Mục 5.5.5, execsnoop.
- **Lập hồ sơ I/O (I/O profiling)**: Truy vết read(2)/write(2)/send(2)/recv(2) và các biến thể của chúng, và nghiên cứu kích thước I/O, cờ, và đường dẫn mã của chúng, sẽ giúp bạn xác định các vấn đề I/O chưa tối ưu, chẳng hạn như số lượng lớn I/O nhỏ. Xem công cụ bpftrace trong Mục 5.5.7, bpftrace.
- **Phân tích thời gian nhân (Kernel time analysis)**: Khi hệ thống cho thấy lượng lớn thời gian CPU nhân, thường được báo cáo là "%sys", đo đạc syscall có thể xác định nguyên nhân. Xem công cụ syscount(8) trong Mục 5.5.6, syscount. Syscall giải thích hầu hết nhưng không phải tất cả thời gian CPU nhân; các ngoại lệ bao gồm lỗi trang (page fault), luồng nhân bất đồng bộ, và ngắt.

Syscall là API được tài liệu hóa tốt (trang man), khiến chúng trở thành nguồn sự kiện dễ nghiên cứu. Chúng cũng được gọi đồng bộ với ứng dụng, có nghĩa là thu thập dấu vết ngăn xếp từ syscall sẽ hiển thị đường dẫn mã ứng dụng chịu trách nhiệm. Các dấu vết ngăn xếp như vậy có thể được trực quan hóa dưới dạng flame graph.

### 5.4.4 Phương pháp USE (USE Method)

Như được giới thiệu trong Chương 2, Phương pháp luận, và được áp dụng trong các chương sau, phương pháp USE kiểm tra việc sử dụng (utilization), bão hòa (saturation), và lỗi (errors) của tất cả tài nguyên phần cứng. Nhiều vấn đề hiệu năng ứng dụng có thể được giải quyết theo cách này, bằng cách cho thấy một tài nguyên đã trở thành nút thắt cổ chai.

Phương pháp USE cũng có thể được áp dụng cho tài nguyên phần mềm. Nếu bạn có thể tìm thấy sơ đồ chức năng hiển thị các thành phần bên trong của ứng dụng, hãy xem xét các chỉ số sử dụng, bão hòa, và lỗi cho mỗi tài nguyên phần mềm và xem điều gì hợp lý.

Ví dụ, ứng dụng có thể sử dụng pool luồng worker để xử lý yêu cầu, với hàng đợi cho các yêu cầu chờ đến lượt. Xem đây là tài nguyên, ba chỉ số có thể được định nghĩa như sau:

- **Sử dụng (Utilization)**: Số luồng trung bình bận xử lý yêu cầu trong một khoảng thời gian, dưới dạng phần trăm tổng số luồng. Ví dụ, 50% có nghĩa là trung bình, một nửa số luồng bận làm việc trên yêu cầu.
- **Bão hòa (Saturation)**: Độ dài trung bình của hàng đợi yêu cầu trong một khoảng thời gian. Điều này cho thấy bao nhiêu yêu cầu đã tích tụ chờ đợi luồng worker.
- **Lỗi (Errors)**: Các yêu cầu bị từ chối hoặc thất bại vì bất kỳ lý do gì.

Nhiệm vụ của bạn sau đó là tìm cách các chỉ số này có thể được đo. Chúng có thể đã được cung cấp bởi ứng dụng ở đâu đó, hoặc chúng có thể cần được thêm hoặc đo sử dụng công cụ khác, chẳng hạn như truy vết động.

Các hệ thống hàng đợi, như ví dụ này, cũng có thể được nghiên cứu sử dụng lý thuyết hàng đợi (queueing theory) (xem Chương 2, Phương pháp luận).

Đối với ví dụ khác, hãy xem xét bộ mô tả tệp (file descriptor). Hệ thống có thể áp đặt giới hạn, sao cho đây là tài nguyên hữu hạn. Ba chỉ số có thể như sau:

- **Sử dụng (Utilization)**: Số bộ mô tả tệp đang sử dụng, dưới dạng phần trăm giới hạn
- **Bão hòa (Saturation)**: Phụ thuộc vào hành vi OS: nếu luồng bị chặn chờ bộ mô tả tệp, đây có thể là số luồng bị chặn chờ tài nguyên này
- **Lỗi (Errors)**: Lỗi cấp phát, chẳng hạn như EFILE, "Too many open files"

Lặp lại bài tập này cho các thành phần của ứng dụng, và bỏ qua bất kỳ chỉ số nào không hợp lý. Quá trình này có thể giúp bạn phát triển danh sách kiểm tra ngắn để kiểm tra sức khỏe ứng dụng trước khi chuyển sang các phương pháp luận khác.

### 5.4.5 Phân tích Trạng thái Luồng (Thread State Analysis)

Đây là phương pháp luận đầu tiên tôi sử dụng cho mọi vấn đề hiệu năng, nhưng nó cũng là một hoạt động nâng cao trên Linux. Mục tiêu là xác định ở mức độ cao nơi các luồng ứng dụng đang dành thời gian của chúng, điều này giải quyết một số vấn đề ngay lập tức và hướng dẫn điều tra các vấn đề khác. Bạn có thể làm điều này bằng cách chia thời gian luồng của mỗi ứng dụng thành một số trạng thái có ý nghĩa.

Tối thiểu, có hai trạng thái luồng: on-CPU và off-CPU. Bạn có thể xác định xem các luồng có ở trạng thái on-CPU không bằng cách sử dụng các chỉ số và công cụ tiêu chuẩn (ví dụ: top(1)), và tiếp theo với lập hồ sơ CPU hoặc phân tích off-CPU nếu phù hợp (xem Mục 5.4.1, Lập hồ sơ CPU, và Mục 5.4.2, Phân tích Off-CPU). Phương pháp luận này hiệu quả hơn với nhiều trạng thái hơn.

**Chín Trạng thái (Nine States)**

Đây là danh sách chín trạng thái luồng tôi đã chọn để cung cấp các điểm khởi đầu phân tích tốt hơn hai trạng thái trước đó (on-CPU và off-CPU):

- **User**: On-CPU ở chế độ người dùng (user mode)
- **Kernel**: On-CPU ở chế độ nhân (kernel mode)
- **Runnable**: Và off-CPU chờ lượt on-CPU
- **Swapping (anonymous paging)**: Có thể chạy (Runnable), nhưng bị chặn chờ các lần page-in ẩn danh
- **Disk I/O**: Chờ I/O thiết bị khối: đọc/ghi, data/text page-in
- **Net I/O**: Chờ I/O thiết bị mạng: socket đọc/ghi
- **Sleeping**: Ngủ tự nguyện (voluntary sleep)
- **Lock**: Chờ lấy khóa đồng bộ hóa (waiting on someone else)
- **Idle**: Chờ đợi công việc

Mô hình chín trạng thái này được minh họa trong Hình 5.6.

*Hình 5.6: Mô hình luồng chín trạng thái*

Hiệu năng cho một yêu cầu ứng dụng được cải thiện bằng cách giảm thời gian ở mọi trạng thái ngoại trừ idle. Trong điều kiện khác như nhau, điều này có nghĩa là các yêu cầu ứng dụng có độ trễ thấp hơn, và ứng dụng có thể xử lý thêm tải.

Khi bạn đã xác định các luồng đang dành thời gian ở trạng thái nào, bạn có thể điều tra thêm:

- **User hoặc Kernel**: Lập hồ sơ có thể xác định các đường dẫn mã đang tiêu thụ CPU, bao gồm thời gian quay trên các khóa (spin on locks). Xem Mục 5.4.1, Lập hồ sơ CPU.
- **Runnable**: Thời gian ở trạng thái này có nghĩa là ứng dụng muốn thêm tài nguyên CPU. Kiểm tra tải CPU cho toàn bộ hệ thống, và bất kỳ giới hạn CPU nào hiện có cho ứng dụng (ví dụ: kiểm soát tài nguyên — resource controls).
- **Swapping (anonymous paging)**: Thiếu bộ nhớ chính (main memory) có sẵn cho ứng dụng có thể gây ra độ trễ swapping. Kiểm tra mức sử dụng bộ nhớ cho toàn bộ hệ thống và bất kỳ giới hạn bộ nhớ nào hiện có. Xem Chương 7, Bộ nhớ, để biết chi tiết.
- **Disk**: Trạng thái này bao gồm I/O đĩa trực tiếp và page fault. Để phân tích, xem Mục 5.4.3, Phân tích Syscall; Chương 8, Hệ thống Tệp; và Chương 9, Đĩa. Việc đặc trưng hóa khối lượng công việc (workload characterization) có thể giúp giải quyết nhiều vấn đề I/O đĩa; kiểm tra tên tệp, kích thước I/O, và loại I/O.
- **Network**: Trạng thái này dành cho thời gian bị chặn trong khi I/O mạng (send/receive), nhưng không phải lắng nghe các kết nối mới (đó là thời gian idle). Để phân tích, xem Mục 5.4.3, Phân tích Syscall; Mục 5.5.7, bpftrace và tiêu đề Lập hồ sơ I/O; và Chương 10, Mạng. Đặc trưng hóa khối lượng công việc cũng có thể hữu ích cho các vấn đề I/O mạng; kiểm tra tên máy chủ, giao thức, và thông lượng.
- **Sleeping**: Phân tích lý do (đường dẫn mã) và thời gian của các lần ngủ.
- **Lock**: Xác định khóa, luồng giữ nó, và lý do tại sao người giữ giữ nó quá lâu. Lý do có thể là người giữ đang bị chặn bởi một khóa khác, đòi hỏi điều tra thêm. Đây là một hoạt động nâng cao, thường được thực hiện bởi nhà phát triển phần mềm có kiến thức sâu về ứng dụng và hệ thống phân cấp khóa của nó. Tôi đã phát triển một công cụ BCC để hỗ trợ loại phân tích này: offwaketime(8) (có trong BCC), hiển thị dấu vết ngăn xếp chặn cùng với waker.

Vì cách các ứng dụng thường chờ đợi công việc, bạn thường sẽ thấy rằng thời gian ở trạng thái I/O mạng và khóa thực ra là thời gian idle. Một luồng worker ứng dụng có thể triển khai idle bằng cách chờ I/O mạng cho yêu cầu tiếp theo (ví dụ: HTTP keep-alive) hoặc bằng cách chờ một biến điều kiện (trạng thái khóa) được đánh thức để xử lý công việc.

Sau đây tóm tắt cách các trạng thái luồng này có thể được đo trên Linux.

**Linux**

Hình 5.7 cho thấy mô hình trạng thái luồng Linux dựa trên trạng thái luồng nhân.

Trạng thái luồng nhân dựa trên thành viên trạng thái `task_struct` của nhân: Runnable là `TASK_RUNNING`, Disk là `TASK_UNINTERRUPTIBLE`, và Sleep là `TASK_INTERRUPTIBLE`. Các trạng thái này được hiển thị bởi các công cụ bao gồm ps(1) và top(1) sử dụng mã một chữ cái: R, D, và S tương ứng. (Có thêm các trạng thái, chẳng hạn như bị dừng bởi debugger, mà tôi không bao gồm ở đây.)

Mặc dù điều này cung cấp một số gợi ý cho phân tích thêm, nhưng nó còn lâu mới phân chia thời gian thành chín trạng thái được mô tả trước đó. Cần thêm thông tin: ví dụ, Runnable có thể được tách thành thời gian user và kernel sử dụng thống kê /proc hoặc getrusage(2).

*Hình 5.7: Các trạng thái luồng Linux*

Các nhân khác thường cung cấp nhiều trạng thái hơn, làm cho phương pháp luận này dễ áp dụng hơn. Tôi ban đầu phát triển và sử dụng phương pháp luận này trên nhân Solaris, được lấy cảm hứng từ tính năng kế toán vi trạng thái (microstate accounting) của nó, ghi lại thời gian luồng ở tám trạng thái khác nhau: user, system, trap, text fault, data fault, lock, sleep, và run queue (độ trễ bộ lập lịch). Chúng không khớp với các trạng thái lý tưởng của tôi, nhưng là điểm khởi đầu tốt hơn.

Tôi sẽ thảo luận ba cách tiếp cận tôi sử dụng trên Linux: dựa trên manh mối (clue-based), phân tích off-CPU, và đo trực tiếp.

**Dựa trên Manh mối (Clue-Based)**

Bạn có thể bắt đầu bằng cách sử dụng các công cụ OS phổ biến, chẳng hạn như pidstat(1) và vmstat(8), để gợi ý về nơi thời gian trạng thái luồng có thể được dành. Các công cụ và cột quan tâm là:

- **User**: pidstat(1) "%usr" (trạng thái này được đo trực tiếp)
- **Kernel**: pidstat(1) "%system" (trạng thái này được đo trực tiếp)
- **Runnable**: vmstat(8) "r" (toàn hệ thống)
- **Swapping**: vmstat(8) "si" và "so" (toàn hệ thống)
- **Disk I/O**: pidstat(1) -d "iodelay" (bao gồm trạng thái swapping)
- **Network I/O**: sar(1) -n DEV "rxkB/s" và "txkB/s" (toàn hệ thống)
- **Sleeping**: Không dễ dàng có sẵn
- **Lock**: perf(1) top (có thể xác định thời gian spin lock trực tiếp)
- **Idle**: Không dễ dàng có sẵn

Một số thống kê này là toàn hệ thống. Nếu bạn phát hiện qua vmstat(8) rằng có tốc độ swapping toàn hệ thống, bạn có thể điều tra trạng thái đó bằng cách sử dụng các công cụ sâu hơn để xác nhận rằng ứng dụng bị ảnh hưởng. Các công cụ này được đề cập trong các phần và chương sau.

**Phân tích Off-CPU**

Vì nhiều trạng thái là off-CPU (tất cả ngoại trừ User và Kernel), bạn có thể áp dụng phân tích off-CPU để xác định trạng thái luồng. Xem Mục 5.4.2, Phân tích Off-CPU.

**Đo Trực tiếp (Direct Measurement)**

Đo thời gian luồng chính xác theo trạng thái luồng như sau:

- **User**: CPU chế độ người dùng có sẵn từ một số công cụ và trong /proc/PID/stat và getrusage(2). pidstat(1) báo cáo điều này là %usr.
- **Kernel**: CPU chế độ nhân cũng có trong /proc/PID/stat và getrusage(2). pidstat(1) báo cáo điều này là %system.
- **Runnable**: Điều này được theo dõi bởi tính năng schedstats nhân theo nanosecond và được hiển thị qua /proc/PID/schedstat. Nó cũng có thể được đo, với chi phí nhất định, bằng các công cụ truy vết bao gồm lệnh con sched của perf(1) và BCC runqlat(8), cả hai được đề cập trong Chương 6, CPU.
- **Swapping**: Thời gian swapping (anonymous paging) theo nanosecond có thể được đo bởi kế toán độ trễ (delay accounting), được giới thiệu trong Chương 4, Công cụ Quan sát, Mục 4.3.3, Kế toán Độ trễ, bao gồm một công cụ ví dụ: getdelays.c. Các công cụ truy vết cũng có thể được sử dụng để thiết bị đo đạc độ trễ swapping.
- **Disk**: pidstat(1) -d hiển thị "iodelay" là số tick đồng hồ trong đó một tiến trình bị trì hoãn bởi block I/O và swapping; nếu không có swapping toàn hệ thống (được báo cáo bởi vmstat(8)), bạn có thể kết luận rằng bất kỳ iodelay nào là trạng thái I/O. Kế toán độ trễ và các tính năng kế toán khác, nếu được kích hoạt, cũng cung cấp thời gian block I/O, được sử dụng bởi iotop(8). Bạn cũng có thể sử dụng các công cụ truy vết chẳng hạn như biotop(8) từ BCC.
- **Network**: I/O mạng có thể được điều tra bằng các công cụ truy vết chẳng hạn như BCC và bpftrace, bao gồm công cụ tcptop(8) cho I/O mạng TCP. Ứng dụng cũng có thể có thiết bị đo đạc để theo dõi thời gian trong I/O (mạng và đĩa).
- **Sleeping**: Thời gian vào ngủ tự nguyện có thể được kiểm tra bằng các trình truy vết và sự kiện bao gồm tracepoint `syscalls:sys_enter_nanosleep`. Công cụ naptime.bt của tôi truy vết các lần ngủ này và in PID và thời gian [Gregg 19][Gregg 20b].
- **Lock**: Thời gian khóa có thể được điều tra bằng các công cụ truy vết, bao gồm klockstat(8) từ BCC và, từ kho bpf-perf-tools-book, pmlock.bt và pmheld.bt cho khóa pthread mutex, và mlock.bt và mheld.bt cho kernel mutex.
- **Idle**: Các công cụ truy vết có thể được sử dụng để thiết bị đo đạc các đường dẫn mã ứng dụng xử lý việc chờ đợi công việc.

Đôi khi ứng dụng có thể có vẻ như hoàn toàn ngủ: chúng vẫn bị chặn off-CPU mà không có tốc độ I/O hoặc các sự kiện khác. Để xác định trạng thái luồng ứng dụng đang ở, có thể cần sử dụng debugger chẳng hạn như pstack(1) hoặc gdb(1) để kiểm tra dấu vết ngăn xếp luồng, hoặc đọc chúng từ các tệp /proc/PID/stack. Lưu ý rằng debugger như vậy có thể tạm dừng ứng dụng đích và gây ra các vấn đề hiệu năng của chính chúng: hãy hiểu cách sử dụng chúng và rủi ro của chúng trước khi thử chúng trong môi trường sản xuất.


### 5.4.6 Phân tích Khóa (Lock Analysis)

Đối với các ứng dụng đa luồng, các khóa có thể trở thành điểm nghẽn cổ chai, ức chế tính song song và khả năng mở rộng. Các ứng dụng đơn luồng có thể bị ức chế bởi các khóa nhân (ví dụ: khóa hệ thống tệp). Khóa có thể được phân tích bằng cách:

- Kiểm tra tranh chấp (contention)
- Kiểm tra thời gian giữ quá mức (excessive hold times)

Điều đầu tiên xác định xem hiện có vấn đề không. Thời gian giữ quá mức không nhất thiết là vấn đề ngay lập tức, nhưng chúng có thể trở thành vấn đề trong tương lai với tải song song nhiều hơn. Đối với mỗi trường hợp, hãy cố xác định tên của khóa (nếu nó tồn tại) và đường dẫn mã dẫn đến việc sử dụng nó.

Mặc dù có các công cụ chuyên dụng cho phân tích khóa, đôi khi bạn có thể giải quyết vấn đề chỉ từ lập hồ sơ CPU. Đối với spin lock, tranh chấp hiển thị dưới dạng sử dụng CPU và có thể dễ dàng xác định bằng cách lập hồ sơ CPU dấu vết ngăn xếp. Đối với khóa mutex thích nghi (adaptive mutex lock), tranh chấp thường liên quan đến một số quay, cũng có thể được xác định bằng cách lập hồ sơ CPU dấu vết ngăn xếp. Trong trường hợp đó, hãy lưu ý rằng hồ sơ CPU chỉ cho thấy một phần của câu chuyện, vì các luồng có thể đã chặn và ngủ trong khi chờ khóa. Xem Mục 5.4.1, Lập hồ sơ CPU.

Để biết các công cụ phân tích khóa cụ thể trên Linux, xem Mục 5.5.7, bpftrace.

### 5.4.7 Tinh chỉnh Hiệu năng Tĩnh (Static Performance Tuning)

Tinh chỉnh hiệu năng tĩnh tập trung vào các vấn đề của môi trường được cấu hình. Đối với hiệu năng ứng dụng, hãy kiểm tra các khía cạnh sau của cấu hình tĩnh:

- Phiên bản ứng dụng nào đang chạy, và các phần phụ thuộc của nó là gì? Có các phiên bản mới hơn không? Ghi chú phát hành của chúng có đề cập đến các cải tiến hiệu năng không?
- Có các vấn đề hiệu năng đã biết không? Có cơ sở dữ liệu bug nào liệt kê chúng không?
- Ứng dụng được cấu hình như thế nào?
- Nếu nó được cấu hình hoặc tinh chỉnh khác với mặc định, lý do là gì? (Nó dựa trên các phép đo và phân tích, hay đoán mò?)
- Ứng dụng có sử dụng bộ nhớ đệm đối tượng (cache of objects) không? Nó được định kích thước như thế nào?
- Ứng dụng có chạy đồng thời không? Điều đó được cấu hình như thế nào (ví dụ: định kích thước thread pool)?
- Ứng dụng có đang chạy ở chế độ đặc biệt không? (Ví dụ, chế độ debug có thể đã được kích hoạt và đang làm giảm hiệu năng, hoặc ứng dụng có thể là bản debug build thay vì release build.)
- Ứng dụng sử dụng những thư viện hệ thống nào? Phiên bản của chúng là gì?
- Ứng dụng sử dụng trình cấp phát bộ nhớ (memory allocator) nào?
- Ứng dụng có được cấu hình để sử dụng trang lớn (large pages) cho heap của nó không?
- Ứng dụng có được biên dịch không? Phiên bản trình biên dịch nào? Tùy chọn và tối ưu hóa trình biên dịch nào? 64-bit?
- Mã native có bao gồm các lệnh nâng cao không? (Có nên không?) (Ví dụ: lệnh SIMD/vector bao gồm Intel SSE.)
- Ứng dụng có gặp lỗi và hiện đang ở chế độ bị giảm cấp không? Hay nó bị cấu hình sai và luôn chạy ở chế độ bị giảm cấp?
- Có các giới hạn hệ thống hoặc kiểm soát tài nguyên cho CPU, bộ nhớ, hệ thống tệp, đĩa, hoặc sử dụng mạng không? (Chúng phổ biến với điện toán đám mây.)

Trả lời các câu hỏi này có thể tiết lộ các lựa chọn cấu hình đã bị bỏ qua.

### 5.4.8 Truy vết Phân tán (Distributed Tracing)

Trong môi trường phân tán, một ứng dụng có thể được tạo thành từ các dịch vụ chạy trên các hệ thống riêng biệt. Mặc dù mỗi dịch vụ có thể được nghiên cứu như thể nó là ứng dụng mini của riêng mình, cũng cần nghiên cứu ứng dụng phân tán như một tổng thể. Điều này đòi hỏi các phương pháp luận và công cụ mới, và thường được thực hiện bằng cách sử dụng truy vết phân tán (distributed tracing).

Truy vết phân tán liên quan đến việc ghi nhật ký thông tin trên mỗi yêu cầu dịch vụ và sau đó kết hợp thông tin này để nghiên cứu. Mỗi yêu cầu ứng dụng trải rộng trên nhiều dịch vụ sau đó có thể được phân tích thành các yêu cầu phụ thuộc (dependency request) của nó, và dịch vụ chịu trách nhiệm về độ trễ ứng dụng cao hoặc lỗi có thể được xác định.

Thông tin được thu thập có thể bao gồm:

- Mã định danh duy nhất cho yêu cầu ứng dụng (external request ID)
- Thông tin về vị trí của nó trong hệ thống phân cấp phụ thuộc
- Thời gian bắt đầu và kết thúc
- Trạng thái lỗi

Một thách thức với truy vết phân tán là lượng dữ liệu nhật ký được tạo ra: nhiều mục cho mỗi yêu cầu ứng dụng. Một giải pháp là thực hiện lấy mẫu đầu (head-based sampling) nơi ở đầu ("head") của yêu cầu, quyết định được đưa ra về việc có lấy mẫu ("trace") nó không: ví dụ, truy vết một trong mỗi mười nghìn yêu cầu. Điều này đủ để phân tích hiệu năng của phần lớn các yêu cầu, nhưng nó có thể làm cho việc phân tích các lỗi không thường xuyên hoặc các giá trị ngoại lai trở nên khó khăn do dữ liệu hạn chế. Một số trình truy vết phân tán dựa trên đuôi (tail-based), nơi tất cả sự kiện được thu thập đầu tiên và sau đó quyết định được đưa ra về những gì nên giữ lại, có thể dựa trên độ trễ và lỗi.

Khi một dịch vụ có vấn đề đã được xác định, nó có thể được phân tích chi tiết hơn bằng cách sử dụng các phương pháp luận và công cụ khác.


## 5.5 Công cụ Quan sát (Observability Tools)

Phần này giới thiệu các công cụ quan sát hiệu năng ứng dụng cho các hệ điều hành dựa trên Linux. Xem phần trước để biết các chiến lược cần tuân theo khi sử dụng chúng.

Các công cụ trong phần này được liệt kê trong Bảng 5.3 cùng với mô tả cách chúng được sử dụng trong chương này.

**Bảng 5.3: Công cụ quan sát ứng dụng Linux**

| Mục | Công cụ | Mô tả |
|-----|---------|-------|
| 5.5.1 | perf | Lập hồ sơ CPU, CPU flame graph, truy vết syscall |
| 5.5.2 | profile | Lập hồ sơ CPU sử dụng lấy mẫu theo thời gian |
| 5.5.3 | offcputime | Lập hồ sơ off-CPU sử dụng truy vết bộ lập lịch |
| 5.5.4 | strace | Truy vết syscall |
| 5.5.5 | execsnoop | Truy vết tiến trình mới |
| 5.5.6 | syscount | Đếm syscall |
| 5.5.7 | bpftrace | Truy vết tín hiệu, lập hồ sơ I/O, phân tích khóa |

Chúng bắt đầu với các công cụ lập hồ sơ CPU sau đó là các công cụ truy vết. Nhiều công cụ truy vết dựa trên BPF và sử dụng các frontend BCC và bpftrace (Chương 15); chúng là: profile(8), offcputime(8), execsnoop(8), và syscount(8). Xem tài liệu cho mỗi công cụ, bao gồm các trang man của nó, để tham khảo đầy đủ các tính năng của nó.

Cũng hãy tìm kiếm các công cụ hiệu năng dành riêng cho ứng dụng không được liệt kê trong bảng này. Các chương sau đề cập đến các công cụ hướng tài nguyên: CPU, bộ nhớ, đĩa, v.v., cũng hữu ích cho phân tích ứng dụng.

Nhiều công cụ sau đây thu thập dấu vết ngăn xếp ứng dụng. Nếu bạn thấy dấu vết ngăn xếp của mình chứa các khung "[unknown]" hoặc có vẻ ngắn một cách không thể xảy ra, xem Mục 5.6, Bẫy (Gotchas), mô tả các vấn đề phổ biến và tóm tắt các phương pháp để sửa chúng.

### 5.5.1 perf

perf(1) là trình lập hồ sơ Linux chuẩn, một công cụ đa năng với nhiều công dụng. Nó được giải thích trong Chương 13, perf. Vì lập hồ sơ CPU là cực kỳ quan trọng cho phân tích ứng dụng, tóm tắt lập hồ sơ CPU sử dụng perf(1) được bao gồm ở đây. Chương 6, CPU, đề cập đến lập hồ sơ CPU và flame graph chi tiết hơn.

**Lập hồ sơ CPU (CPU Profiling)**

Ví dụ sau sử dụng perf(1) để lấy mẫu dấu vết ngăn xếp (`-g`) trên tất cả CPU (`-a`) ở 49 Hertz (`-F 49`: mẫu mỗi giây) trong 30 giây, sau đó liệt kê các mẫu:

```
# perf record -F 49 -a -g -- sleep 30
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.560 MB perf.data (2940 samples) ]
# perf script
mysqld 10441 [000] 64918.205722:    10101010 cpu-clock:pppH:
    5587b59bf2f0 row_mysql_store_col_in_innobase_format+0x270 (/usr/sbin/mysqld)
    5587b59c3951 [unknown] (/usr/sbin/mysqld)
    5587b58803b3 ha_innobase::write_row+0x1d3 (/usr/sbin/mysqld)
    ...
```

Có 2.940 mẫu ngăn xếp trong hồ sơ này; chỉ một ngăn xếp được bao gồm ở đây. Lệnh con `script` của perf(1) in mỗi mẫu ngăn xếp trong hồ sơ đã được ghi trước đó (tệp perf.data). perf(1) cũng có lệnh con `report` để tóm tắt hồ sơ dưới dạng phân cấp đường dẫn mã. Hồ sơ cũng có thể được trực quan hóa dưới dạng CPU flame graph.

**CPU Flame Graph**

CPU flame graph đã được tự động hóa tại Netflix để các nhà điều hành và nhà phát triển có thể yêu cầu chúng từ giao diện người dùng dựa trên trình duyệt. Chúng có thể được xây dựng hoàn toàn bằng phần mềm mã nguồn mở, bao gồm từ kho GitHub theo các lệnh sau. Đối với CPU flame graph Hình 5.3 được hiển thị trước đó, các lệnh là:

```
# perf record -F 49 -a -g -- sleep 10; perf script --header > out.stacks
# git clone https://github.com/brendangregg/FlameGraph; cd FlameGraph
# ./stackcollapse-perf.pl < ../out.stacks | ./flamegraph.pl --hash > out.svg
```

Tệp out.svg sau đó có thể được tải trong trình duyệt web.

flamegraph.pl cung cấp bảng màu tùy chỉnh cho các ngôn ngữ khác nhau: ví dụ, cho các ứng dụng Java, thử `--color=java`. Chạy `flamegraph.pl -h` cho tất cả các tùy chọn.

**Truy vết Syscall (Syscall Tracing)**

Lệnh con `trace` của perf(1) truy vết các lời gọi hệ thống theo mặc định và là phiên bản perf(1) của strace(1). Ưu điểm của perf(1) là nó sử dụng bộ đệm mỗi CPU để giảm chi phí, làm cho nó an toàn hơn nhiều để sử dụng so với triển khai hiện tại của strace(1). Nó cũng có thể truy vết toàn hệ thống, trong khi strace(1) bị giới hạn đến một tập tiến trình.

**Phân tích Thời gian Nhân (Kernel Time Analysis)**

perf(1) trace tóm tắt các syscall với `-s`:

```
# perf trace -s -p $(pgrep mysqld)
```

Kết quả đầu ra hiển thị số lần gọi syscall và thời gian cho mỗi luồng.

**Lập hồ sơ I/O (I/O Profiling)**

I/O syscall đặc biệt thú vị. Để phân tích tùy chỉnh hơn, bạn có thể chuyển sang bpftrace trong Mục 5.5.7, bpftrace.

### 5.5.2 profile

profile(8) là trình lập hồ sơ CPU dựa trên bộ hẹn giờ từ BCC (Chương 15). Nó sử dụng BPF để giảm chi phí bằng cách tổng hợp dấu vết ngăn xếp trong ngữ cảnh nhân, và chỉ chuyển các ngăn xếp duy nhất và số lần xuất hiện của chúng sang không gian người dùng.

Ví dụ profile(8) sau lấy mẫu ở 49 Hertz trên tất cả CPU, trong 10 giây:

```
# profile -F 49 10
Sampling at 49 Hertz of all threads by user + kernel stack for 10 secs.
[...]
SELECT_LEX::prepare(THD*)
Sql_cmd_select::prepare_inner(THD*)
...
```

Chỉ một dấu vết ngăn xếp được bao gồm trong kết quả đầu ra này, cho thấy rằng `SELECT_LEX::prepare()` được lấy mẫu on-CPU với dòng kế thừa đó 13 lần.

profile(8) được thảo luận thêm trong Chương 6, CPU, Mục 6.6.14, profile, liệt kê các tùy chọn khác nhau của nó và bao gồm hướng dẫn để tạo CPU flame graph từ kết quả đầu ra của nó.

### 5.5.3 offcputime

offcputime(8) là công cụ BCC và bpftrace (Chương 15) để tóm tắt thời gian các luồng bị chặn và off-CPU, hiển thị dấu vết ngăn xếp để giải thích lý do. Nó hỗ trợ phân tích Off-CPU (Mục 5.4.2, Phân tích Off-CPU). offcputime(8) là đối tác của profile(8): giữa chúng, chúng hiển thị toàn bộ thời gian được dành bởi các luồng trên hệ thống.

Ví dụ sau hiển thị offcputime(8) từ BCC, truy vết trong 5 giây:

```
# offcputime 5
Tracing off-CPU time (us) of all threads by user + kernel stack for 5 secs.
[...]
    finish_task_switch
    schedule
    jbd2_log_wait_commit
    ...
    MYSQL_BIN_LOG::commit(THD*, bool)
    ...
```

Kết quả đầu ra hiển thị dấu vết ngăn xếp duy nhất và thời gian off-CPU của chúng theo microsecond.

Để hiệu quả, offcputime(8) tổng hợp các ngăn xếp này trong ngữ cảnh nhân và chỉ phát ra các ngăn xếp duy nhất đến không gian người dùng. Nó cũng chỉ ghi lại dấu vết ngăn xếp cho các khoảng off-CPU vượt quá ngưỡng, một microsecond theo mặc định, có thể được tinh chỉnh bằng tùy chọn `-m`.

**Flame Graph Thời gian Off-CPU**

Để trực quan hóa flame graph thời gian off-CPU:

```
# git clone https://github.com/brendangregg/FlameGraph; cd FlameGraph
# offcputime -f 5 | ./flamegraph.pl --bgcolors=blue \
--title="Off-CPU Time Flame Graph"> out.svg
```

Tôi đã đặt màu nền là xanh dương để nhắc nhở trực quan rằng đây là flame graph off-CPU thay vì CPU flame graph thường được sử dụng.

### 5.5.4 strace

Lệnh strace(1) là trình truy vết lời gọi hệ thống Linux. Nó có thể truy vết các syscall, in tóm tắt một dòng cho mỗi lệnh, và cũng có thể đếm các syscall và in báo cáo.

Ví dụ, truy vết syscall bằng PID 1884:

```
$ strace -ttt -T -p 1884
1356982510.395542 close(3)  = 0 <0.000267>
1356982510.396064 close(4)  = 0 <0.000293>
...
```

Tùy chọn `-c` có thể được sử dụng để tóm tắt hoạt động lời gọi hệ thống.

**Chi phí strace (strace Overhead)**

> **CẢNH BÁO**: Phiên bản hiện tại của strace(1) sử dụng truy vết dựa trên breakpoint qua giao diện ptrace(2) của Linux. Điều này đặt breakpoint cho việc vào và trả về của tất cả syscall (ngay cả khi tùy chọn `-e` được sử dụng để chỉ chọn một số). Điều này xâm lấn, và các ứng dụng với tốc độ syscall cao có thể thấy hiệu năng của chúng bị giảm đến một bậc độ lớn.

Ví dụ, cùng lệnh dd(1) không có strace(1) chạy nhanh hơn 73 lần so với khi có strace(1). Các trình truy vết khác bao gồm perf(1), Ftrace, BCC, và bpftrace giảm đáng kể chi phí truy vết bằng cách sử dụng truy vết được đệm.

### 5.5.5 execsnoop

execsnoop(8) là công cụ BCC và bpftrace truy vết việc thực thi tiến trình mới trên toàn hệ thống. Nó có thể tìm các vấn đề của các tiến trình tồn tại ngắn tiêu thụ tài nguyên CPU và cũng có thể được sử dụng để gỡ lỗi việc thực thi phần mềm, bao gồm các script khởi động ứng dụng.

execsnoop(8) hoạt động bằng cách truy vết lời gọi hệ thống execve(2) và in tóm tắt một dòng cho mỗi lệnh. Công cụ hỗ trợ một số tùy chọn, bao gồm `-t` cho dấu thời gian.

### 5.5.6 syscount

syscount(8) là công cụ BCC và bpftrace để đếm các lời gọi hệ thống trên toàn hệ thống.

Ví dụ kết quả từ phiên bản BCC:

```
# syscount
Tracing syscalls, printing top 10... Ctrl+C to quit.
^C[05:01:28]
SYSCALL                   COUNT
recvfrom                 114746
sendto                    57395
ppoll                     28654
...
```

Điều này cho thấy syscall thường xuyên nhất là recvfrom(2). syscount(8) cũng có thể đếm theo tiến trình bằng `-P`.

### 5.5.7 bpftrace

bpftrace là trình truy vết dựa trên BPF cung cấp ngôn ngữ lập trình cấp cao, cho phép tạo các lệnh một dòng (one-liner) và các script ngắn mạnh mẽ. Nó phù hợp cho phân tích ứng dụng tùy chỉnh dựa trên manh mối từ các công cụ khác.

bpftrace được giải thích trong Chương 15. Phần này hiển thị một số ví dụ cho phân tích ứng dụng.

**Truy vết Tín hiệu (Signal Tracing)**

Lệnh một dòng bpftrace này truy vết tín hiệu tiến trình (qua syscall kill(2)) hiển thị PID và tên tiến trình nguồn, và PID đích và số hiệu tín hiệu:

```
# bpftrace -e 't:syscalls:sys_enter_kill { time("%H:%M:%S ");
printf("%s (PID %d) send a SIG %d to PID %d\n",
comm, pid, args->sig, args->pid); }'
```

**Lập hồ sơ I/O (I/O Profiling)**

bpftrace có thể được sử dụng để phân tích I/O theo nhiều cách: kiểm tra kích thước, độ trễ, giá trị trả về, và dấu vết ngăn xếp.

Hiển thị kích thước bộ đệm recvfrom(2) dưới dạng histogram:

```
# bpftrace -e 't:syscalls:sys_enter_recvfrom { @bytes = hist(args->size); }'
```

Đo độ trễ recvfrom(2):

```
# bpftrace -e 't:syscalls:sys_enter_recvfrom { @ts[tid] = nsecs; }
t:syscalls:sys_exit_recvfrom /@ts[tid]/ {
@usecs = hist((nsecs - @ts[tid]) / 1000); delete(@ts[tid]); }'
```

Các tùy chọn phân tích thêm:
- `@usecs[args->ret]`: Phân tích theo giá trị trả về syscall
- `@usecs[ustack]`: Phân tích theo dấu vết ngăn xếp người dùng

**Truy vết Khóa (Lock Tracing)**

bpftrace có thể được sử dụng để điều tra tranh chấp khóa ứng dụng theo nhiều cách. Đối với khóa pthread mutex điển hình, uprobes có thể được sử dụng để truy vết các hàm thư viện pthread: `pthread_mutex_lock()`, v.v.

Ví dụ sử dụng pmlock.bt để truy vết thời gian hàm pthread_mutex_lock():

```
# pmlock.bt $(pgrep mysqld)
```

Và pmheld.bt hiển thị dấu vết ngăn xếp của người giữ khóa:

```
# pmheld.bt $(pgrep mysqld)
```

**Nội bộ Ứng dụng (Application Internals)**

Nếu cần, bạn có thể phát triển các công cụ tùy chỉnh để tóm tắt nội bộ ứng dụng. Bắt đầu bằng cách kiểm tra xem USDT probe có sẵn không, hoặc có thể được làm sẵn không (thường bằng cách biên dịch lại với một tùy chọn). Nếu không thể làm sẵn hoặc không đủ, hãy xem xét sử dụng uprobes.


## 5.6 Bẫy (Gotchas)

Các phần sau mô tả các vấn đề phổ biến với phân tích hiệu năng ứng dụng, cụ thể là thiếu ký hiệu (symbols) và dấu vết ngăn xếp (stack trace). Bạn có thể gặp những vấn đề này đầu tiên khi kiểm tra hồ sơ CPU, chẳng hạn như flame graph, và thấy rằng nó thiếu tên hàm và dấu vết ngăn xếp.

### 5.6.1 Thiếu Ký hiệu (Missing Symbols)

Khi trình lập hồ sơ hoặc trình truy vết không thể giải quyết địa chỉ lệnh ứng dụng thành tên hàm (symbol) của nó, nó có thể in nó dưới dạng số thập lục phân hoặc chuỗi "[unknown]". Cách sửa phụ thuộc vào trình biên dịch, runtime, và tinh chỉnh của ứng dụng, và chính trình lập hồ sơ.

**Binary ELF (C, C++, ...)**

Các symbol có thể bị thiếu khỏi các binary đã biên dịch, đặc biệt là những binary được đóng gói và phân phối, vì chúng đã được xử lý sử dụng strip(1) để giảm kích thước tệp. Một cách sửa là điều chỉnh quá trình build để tránh stripping symbol; cách khác là sử dụng nguồn thông tin symbol khác, chẳng hạn như debuginfo hoặc BPF Type Format (BTF). Lập hồ sơ Linux qua perf(1), BCC, và bpftrace hỗ trợ symbol debuginfo.

**JIT Runtime (Java, Node.js, ...)**

Thiếu symbol thường xảy ra cho các runtime trình biên dịch tức thời (JIT) như Java và Node.js. Trong những trường hợp đó, trình biên dịch JIT có bảng symbol riêng đang thay đổi trong quá trình thực thi và không phải là một phần của các bảng symbol được biên dịch trước trong binary. Cách sửa phổ biến là sử dụng các bảng symbol bổ sung được tạo bởi runtime, được đặt trong các tệp `/tmp/perf-<PID>.map` được đọc bởi cả perf(1) và BCC.

Ví dụ, Netflix sử dụng perf-map-agent, có thể gắn vào một tiến trình Java đang chạy và dump một tệp symbol bổ sung. Tôi đã tự động hóa việc sử dụng của nó với một công cụ khác gọi là jmaps, nên được chạy ngay sau hồ sơ và trước khi dịch symbol.

### 5.6.2 Thiếu Ngăn xếp (Missing Stacks)

Một vấn đề phổ biến khác là thiếu hoặc dấu vết ngăn xếp không đầy đủ, có thể ngắn chỉ một hoặc hai khung. Ví dụ, từ hồ sơ off-CPU của MySQL server:

```
finish_task_switch
schedule
futex_wait_queue_me
futex_wait
do_futex
__x64_sys_futex
do_syscall_64
entry_SYSCALL_64_after_hwframe
pthread_cond_timedwait@@GLIBC_2.3.2
[unknown]
```

Ngăn xếp này không đầy đủ: sau `pthread_cond_timedwait()` là một khung "[unknown]" đơn lẻ. Nó thiếu các hàm MySQL bên dưới điểm này.

Dấu vết ngăn xếp không đầy đủ thường xảy ra do sự kết hợp của hai yếu tố: 1) công cụ quan sát sử dụng cách tiếp cận dựa trên con trỏ khung (frame pointer-based) để đọc dấu vết ngăn xếp, và 2) binary đích không dành một thanh ghi (RBP trên x86_64) cho con trỏ khung, thay vào đó sử dụng lại nó như một thanh ghi đa năng như một tối ưu hóa hiệu năng trình biên dịch.

Giải pháp dễ nhất thường là sửa thanh ghi con trỏ khung:

- **C/C++ và các ngôn ngữ biên dịch với gcc(1) hoặc LLVM**: Biên dịch lại phần mềm với `-fno-omit-frame-pointer`.
- **Java**: Chạy java(1) với `-XX:+PreserveFramePointer`.

Điều này có thể đi kèm chi phí hiệu năng, nhưng thường được đo ở dưới 1%; lợi ích của việc có thể sử dụng dấu vết ngăn xếp để tìm các cải thiện hiệu năng thường vượt xa chi phí này.

Cách tiếp cận khác là chuyển sang kỹ thuật duyệt ngăn xếp không dựa trên con trỏ khung. perf(1) hỗ trợ duyệt ngăn xếp dựa trên DWARF, ORC, và last branch record (LBR).

## 5.7 Bài tập (Exercises)

1. Trả lời các câu hỏi sau về thuật ngữ:
   - Bộ nhớ đệm (cache) là gì?
   - Bộ đệm vòng (ring buffer) là gì?
   - Khóa quay (spin lock) là gì?
   - Khóa mutex thích nghi (adaptive mutex lock) là gì?
   - Sự khác biệt giữa đồng thời (concurrency) và song song (parallelism) là gì?
   - Ái lực CPU (CPU affinity) là gì?

2. Trả lời các câu hỏi khái niệm sau:
   - Ưu điểm và nhược điểm chung của việc sử dụng kích thước I/O lớn là gì?
   - Bảng băm của các khóa được dùng để làm gì?
   - Mô tả các đặc điểm hiệu năng chung của runtime của các ngôn ngữ biên dịch, ngôn ngữ thông dịch, và các ngôn ngữ sử dụng máy ảo.
   - Giải thích vai trò của thu gom rác (garbage collection) và cách nó có thể ảnh hưởng đến hiệu năng.

3. Chọn một ứng dụng và trả lời các câu hỏi cơ bản sau về nó:
   - Vai trò của ứng dụng là gì?
   - Ứng dụng thực hiện thao tác riêng biệt nào?
   - Ứng dụng có chạy ở chế độ người dùng hay chế độ nhân không?
   - Ứng dụng được cấu hình như thế nào? Các tùy chọn quan trọng nào liên quan đến hiệu năng?
   - Ứng dụng cung cấp các chỉ số hiệu năng nào?
   - Ứng dụng tạo ra những nhật ký nào? Chúng có chứa thông tin hiệu năng không?
   - Phiên bản gần đây nhất của ứng dụng có sửa các vấn đề hiệu năng không?
   - Có các bug hiệu năng đã biết cho ứng dụng không?
   - Ứng dụng có cộng đồng không (ví dụ: IRC, meetup)? Cộng đồng hiệu năng?
   - Có sách về ứng dụng không? Sách về hiệu năng?
   - Có các chuyên gia hiệu năng nổi tiếng cho ứng dụng không? Họ là ai?

4. Chọn một ứng dụng đang chịu tải và thực hiện các tác vụ sau:
   - Trước khi thực hiện bất kỳ phép đo nào, bạn có dự kiến ứng dụng bị ràng buộc bởi CPU hay I/O không? Giải thích lý do của bạn.
   - Xác định bằng cách sử dụng các công cụ quan sát nếu nó bị ràng buộc bởi CPU hay I/O.
   - Tạo CPU flame graph cho ứng dụng. Đường dẫn mã CPU nóng nhất là gì?
   - Tạo off-CPU flame graph cho ứng dụng. Sự kiện chặn dài nhất trong yêu cầu của ứng dụng là gì (bỏ qua ngăn xếp idle)?
   - Đặc trưng hóa kích thước I/O mà nó thực hiện (ví dụ: đọc/ghi hệ thống tệp, gửi/nhận mạng).
   - Ứng dụng có bộ nhớ đệm không? Xác định kích thước và tỷ lệ trúng của chúng.
   - Đo độ trễ (thời gian phản hồi) cho thao tác mà ứng dụng phục vụ. Hiển thị trung bình, tối thiểu, tối đa, và phân phối đầy đủ.
   - Thực hiện phân tích đào sâu của thao tác, điều tra nguồn gốc của phần lớn độ trễ.
   - Đặc trưng hóa khối lượng công việc được áp dụng cho ứng dụng (đặc biệt là ai và cái gì).
   - Thực hiện danh sách kiểm tra tinh chỉnh hiệu năng tĩnh.
   - Ứng dụng có chạy đồng thời không? Điều tra việc sử dụng nguyên thủy đồng bộ hóa của nó.

5. (Tùy chọn, nâng cao) Phát triển công cụ cho Linux gọi là tsastat(8) in các cột cho nhiều trạng thái phân tích trạng thái luồng, với thời gian dành cho mỗi trạng thái. Điều này có thể hoạt động tương tự như pidstat(1) và tạo ra kết quả đầu ra liên tục.

## 5.8 Tài liệu Tham khảo (References)

[Knuth 76] Knuth, D., "Big Omicron and Big Omega and Big Theta," ACM SIGACT News, 1976.

[Knuth 97] Knuth, D., *The Art of Computer Programming, Volume 1: Fundamental Algorithms*, 3rd Edition, Addison-Wesley, 1997.

[Zijlstra 09] Zijlstra, P., "mutex: implement adaptive spinning," http://lwn.net/Articles/314512, 2009.

[Gregg 17a] Gregg, B., "EuroBSDcon: System Performance Analysis Methodologies," EuroBSDcon, http://www.brendangregg.com/blog/2017-10-28/bsd-performance-analysis-methodologies.html, 2017.

[Intel 18] "Tool tracing syscalls in a fast way using eBPF linux kernel feature," https://github.com/pmem/vltrace, last updated 2018.

[Microsoft 18] "Fibers," Windows Dev Center, https://docs.microsoft.com/en-us/windows/win32/procthread/fibers, 2018.

[Rudolph 18] Rudolph, J., "perf-map-agent," https://github.com/jvm-profiling-tools/perf-map-agent, last updated 2018.

[Schwartz 18] Schwartz, E., "Dynamic Optimizations for SBCL Garbage Collection," 11th European Lisp Symposium, 2018.

[Axboe 19] Axboe, J., "Efficient IO with io_uring," https://kernel.dk/io_uring.pdf, 2019.

[Gregg 19] Gregg, B., *BPF Performance Tools: Linux System and Application Observability*, Addison-Wesley, 2019.

[Apdex 20] Apdex Alliance, "Apdex," https://www.apdex.org, accessed 2020.

[Golang 20] "Why goroutines instead of threads?" Golang documentation, https://golang.org/doc/faq#goroutines, accessed 2020.

[Gregg 20b] Gregg, B., "BPF Performance Tools," https://github.com/brendangregg/bpf-perf-tools-book, last updated 2020.

[Gregg 20c] Gregg, B., "jmaps," https://github.com/brendangregg/FlameGraph/blob/master/jmaps, last updated 2020.

[Linux 20e] "RCU Concepts," Linux documentation, https://www.kernel.org/doc/html/latest/RCU/rcu.html, accessed 2020.

[Microsoft 20] "Procmon Is a Linux Reimagining of the Classic Procmon Tool from the Sysinternals Suite of Tools for Windows," https://github.com/microsoft/ProcMon-for-Linux, last updated 2020.

[Molnar 20] Molnar, I., and Bueso, D., "Generic Mutex Subsystem," Linux documentation, https://www.kernel.org/doc/Documentation/locking/mutex-design.rst, accessed 2020.

[Node.js 20] "Node.js," http://nodejs.org, accessed 2020.

[Pangin 20] Pangin, A., "async-profiler," https://github.com/jvm-profiling-tools/async-profiler, last updated 2020.
