# Chương 2: Phương Pháp Luận

> *Cho người ta một con cá, bạn nuôi họ một ngày.*
> *Dạy người ta câu cá, bạn nuôi họ cả đời.*
> — Ngạn ngữ Trung Quốc

Tôi bắt đầu sự nghiệp công nghệ với tư cách là một quản trị viên hệ thống cấp dưới, và tôi nghĩ rằng tôi có thể học hiệu năng chỉ bằng cách nghiên cứu các công cụ dòng lệnh và chỉ số. Tôi đã sai. Tôi đọc man page từ đầu đến cuối và học các định nghĩa cho page fault, context switch và các chỉ số hệ thống khác nhau, nhưng tôi không biết phải làm gì với chúng: làm thế nào để đi từ tín hiệu đến giải pháp.

Tôi nhận thấy rằng, bất cứ khi nào có vấn đề hiệu năng, các quản trị viên hệ thống cấp cao có quy trình tư duy riêng để nhanh chóng đi qua các công cụ và chỉ số để tìm nguyên nhân gốc rễ. Họ hiểu chỉ số nào quan trọng và khi nào chúng chỉ ra vấn đề, và cách sử dụng chúng để thu hẹp cuộc điều tra. Chính bí quyết này là thứ thiếu trong man page — nó thường được học bằng cách quan sát qua vai một quản trị viên hoặc kỹ sư cấp cao.

Kể từ đó, tôi đã thu thập, ghi chép, chia sẻ và phát triển các phương pháp luận hiệu năng của riêng mình. Chương này bao gồm các phương pháp luận này và kiến thức nền tảng thiết yếu khác cho hiệu năng hệ thống: khái niệm, thuật ngữ, thống kê và trực quan hóa. Nội dung này bao gồm lý thuyết trước khi các chương sau đi sâu vào triển khai.

Các mục tiêu học tập của chương này bao gồm:

- Hiểu các chỉ số hiệu năng chính: độ trễ (latency), mức sử dụng (utilization) và bão hòa (saturation).
- Phát triển cảm giác về thang đo thời gian đo lường, xuống đến nano giây.
- Tìm hiểu các đánh đổi trong tinh chỉnh, mục tiêu, và khi nào nên dừng phân tích.
- Xác định vấn đề của khối lượng công việc so với kiến trúc.
- Xem xét phân tích tài nguyên so với phân tích khối lượng công việc.
- Tuân theo các phương pháp luận hiệu năng khác nhau, bao gồm: phương pháp USE, đặc trưng hóa khối lượng công việc, phân tích độ trễ, tinh chỉnh hiệu năng tĩnh, và các phương châm hiệu năng.
- Hiểu kiến thức cơ bản về thống kê và lý thuyết hàng đợi.

Trong tất cả các chương của cuốn sách này, chương này là chương ít thay đổi nhất kể từ ấn bản đầu tiên. Phần mềm, phần cứng, công cụ hiệu năng và các tham số tinh chỉnh hiệu năng đều đã thay đổi trong suốt sự nghiệp của tôi. Những gì không thay đổi là lý thuyết và phương pháp luận: các kỹ năng lâu bền được đề cập trong chương này.

Chương này có ba phần:

- **Kiến thức nền tảng** giới thiệu thuật ngữ, mô hình cơ bản, các khái niệm hiệu năng chính và các góc nhìn. Phần lớn nội dung này sẽ được coi là kiến thức cơ sở cho phần còn lại của cuốn sách.
- **Phương pháp luận** thảo luận về các phương pháp luận phân tích hiệu năng, cả quan sát và thực nghiệm; mô hình hóa; và hoạch định dung lượng.
- **Chỉ số** giới thiệu thống kê hiệu năng, giám sát và trực quan hóa.

Nhiều phương pháp luận được giới thiệu ở đây được khám phá chi tiết hơn trong các chương sau, bao gồm các phần phương pháp luận trong Chương 5 đến 10.

## 2.1 Thuật Ngữ (Terminology)

Sau đây là các thuật ngữ chính cho hiệu năng hệ thống. Các chương sau cung cấp thuật ngữ bổ sung và mô tả một số thuật ngữ này trong các ngữ cảnh khác nhau.

- **IOPS**: Input/output operations per second (số thao tác I/O mỗi giây) là thước đo tốc độ của các thao tác truyền dữ liệu. Đối với I/O đĩa, IOPS đề cập đến số lần đọc và ghi mỗi giây.
- **Throughput** (Thông lượng): Tốc độ công việc được thực hiện. Đặc biệt trong truyền thông, thuật ngữ này được sử dụng để chỉ tốc độ dữ liệu (byte trên giây hoặc bit trên giây). Trong một số ngữ cảnh (ví dụ: cơ sở dữ liệu), thông lượng có thể đề cập đến tốc độ thao tác (thao tác trên giây hoặc giao dịch trên giây).
- **Response time** (Thời gian phản hồi): Thời gian để một thao tác hoàn thành. Điều này bao gồm bất kỳ thời gian chờ nào và thời gian được phục vụ (service time), bao gồm cả thời gian để truyền kết quả.
- **Latency** (Độ trễ): Thước đo thời gian một thao tác dành để chờ được phục vụ. Trong một số ngữ cảnh, nó có thể đề cập đến toàn bộ thời gian cho một thao tác, tương đương với thời gian phản hồi. Xem Phần 2.3, Khái niệm, để biết ví dụ.
- **Utilization** (Mức sử dụng): Đối với các tài nguyên phục vụ yêu cầu, mức sử dụng là thước đo mức độ bận rộn của tài nguyên, dựa trên bao nhiêu thời gian trong một khoảng nhất định mà nó đang tích cực thực hiện công việc. Đối với các tài nguyên cung cấp lưu trữ, mức sử dụng có thể đề cập đến dung lượng đã tiêu thụ (ví dụ: mức sử dụng bộ nhớ).
- **Saturation** (Bão hòa): Mức độ mà một tài nguyên có công việc xếp hàng mà nó không thể phục vụ.
- **Bottleneck** (Nút thắt cổ chai): Trong hiệu năng hệ thống, nút thắt cổ chai là tài nguyên giới hạn hiệu năng của hệ thống. Xác định và loại bỏ các nút thắt cổ chai hệ thống là hoạt động chính của hiệu năng hệ thống.
- **Workload** (Khối lượng công việc): Đầu vào cho hệ thống hoặc tải được áp dụng là khối lượng công việc. Đối với cơ sở dữ liệu, khối lượng công việc bao gồm các truy vấn và lệnh cơ sở dữ liệu được gửi bởi client.
- **Cache** (Bộ nhớ đệm): Một vùng lưu trữ nhanh có thể nhân bản hoặc đệm một lượng dữ liệu giới hạn, để tránh giao tiếp trực tiếp với tầng lưu trữ chậm hơn, qua đó cải thiện hiệu năng. Vì lý do kinh tế, cache thường nhỏ hơn tầng chậm hơn.

Bảng thuật ngữ (Glossary) bao gồm thêm thuật ngữ để tham khảo khi cần.

## 2.2 Mô Hình (Models)

Các mô hình đơn giản sau minh họa một số nguyên tắc cơ bản của hiệu năng hệ thống.

### 2.2.1 Hệ Thống Đang Thử Nghiệm (System Under Test)

Hiệu năng của một hệ thống đang thử nghiệm (SUT - System Under Test) được thể hiện trong Hình 2.1.

*Hình 2.1: Sơ đồ khối của hệ thống đang thử nghiệm*

Điều quan trọng là phải nhận biết rằng các nhiễu loạn (perturbation/interference) có thể ảnh hưởng đến kết quả, bao gồm những nhiễu loạn gây ra bởi hoạt động hệ thống được lập lịch, người dùng khác của hệ thống, và các khối lượng công việc khác. Nguồn gốc của các nhiễu loạn có thể không rõ ràng, và có thể cần nghiên cứu cẩn thận về hiệu năng hệ thống để xác định nó. Điều này có thể đặc biệt khó khăn trong một số môi trường đám mây, nơi hoạt động khác (bởi các tenant khách) trên hệ thống host vật lý có thể không quan sát được từ bên trong SUT khách.

Một khó khăn khác với các môi trường hiện đại là chúng có thể bao gồm nhiều thành phần nối mạng phục vụ khối lượng công việc đầu vào, bao gồm load balancer, proxy server, web server, caching server, application server, database server và hệ thống lưu trữ. Hành động đơn thuần là lập bản đồ môi trường có thể giúp tiết lộ các nguồn nhiễu loạn trước đó bị bỏ qua. Môi trường cũng có thể được mô hình hóa như một mạng các hệ thống hàng đợi, cho nghiên cứu phân tích.

### 2.2.2 Hệ Thống Hàng Đợi (Queueing System)

Một số thành phần và tài nguyên có thể được mô hình hóa như một hệ thống hàng đợi để hiệu năng của chúng trong các tình huống khác nhau có thể được dự đoán dựa trên mô hình. Đĩa thường được mô hình hóa như một hệ thống hàng đợi, có thể dự đoán cách thời gian phản hồi suy giảm dưới tải. Hình 2.2 cho thấy một hệ thống hàng đợi đơn giản.

*Hình 2.2: Mô hình hàng đợi đơn giản*

Lĩnh vực lý thuyết hàng đợi, được giới thiệu trong Phần 2.6, Mô Hình Hóa, nghiên cứu các hệ thống hàng đợi và mạng lưới các hệ thống hàng đợi.

## 2.3 Các Khái Niệm (Concepts)

Sau đây là các khái niệm quan trọng của hiệu năng hệ thống và được coi là kiến thức cơ sở cho phần còn lại của chương này và cuốn sách. Các chủ đề được mô tả theo cách tổng quát, trước khi các chi tiết cụ thể về triển khai được giới thiệu trong các phần Kiến trúc của các chương sau.

### 2.3.1 Độ Trễ (Latency)

Đối với một số môi trường, độ trễ là trọng tâm duy nhất của hiệu năng. Đối với các môi trường khác, nó là một hoặc hai chỉ số hàng đầu cho phân tích, cùng với thông lượng.

Như một ví dụ về độ trễ, Hình 2.3 cho thấy một truyền tải mạng, chẳng hạn như yêu cầu HTTP GET, với thời gian được chia thành các thành phần độ trễ và truyền dữ liệu.

*Hình 2.3: Độ trễ kết nối mạng*

Độ trễ là thời gian dành để chờ trước khi một thao tác được thực hiện. Trong ví dụ này, thao tác là yêu cầu dịch vụ mạng để truyền dữ liệu. Trước khi thao tác này có thể diễn ra, hệ thống phải chờ kết nối mạng được thiết lập, đó là độ trễ cho thao tác này. Thời gian phản hồi bao gồm độ trễ này và thời gian thao tác.

Vì độ trễ có thể được đo từ các vị trí khác nhau, nó thường được biểu thị cùng với mục tiêu đo lường. Ví dụ, thời gian tải của một trang web có thể bao gồm ba khoảng thời gian khác nhau được đo từ các vị trí khác nhau: độ trễ DNS, độ trễ kết nối TCP, và sau đó là thời gian truyền dữ liệu TCP. Độ trễ DNS đề cập đến toàn bộ thao tác DNS. Độ trễ kết nối TCP chỉ đề cập đến phần khởi tạo (bắt tay TCP - TCP handshake).

Ở cấp độ cao hơn, tất cả những thứ này, bao gồm thời gian truyền dữ liệu TCP, có thể được coi là độ trễ của thứ gì đó khác. Ví dụ, thời gian từ khi người dùng nhấp vào liên kết trang web đến khi trang kết quả được tải đầy đủ có thể được gọi là độ trễ, bao gồm thời gian để trình duyệt lấy trang web qua mạng và hiển thị nó. Vì từ "latency" đơn lẻ có thể mơ hồ, tốt nhất nên bao gồm các thuật ngữ xác định để giải thích những gì nó đo: request latency, TCP connection latency, v.v.

Vì độ trễ là chỉ số dựa trên thời gian, nhiều phép tính khác nhau có thể thực hiện được. Các vấn đề hiệu năng có thể được định lượng bằng độ trễ và sau đó xếp hạng vì chúng được biểu thị bằng cùng đơn vị (thời gian). Tốc độ cải thiện dự đoán cũng có thể được tính toán, bằng cách xem xét khi nào độ trễ có thể được giảm hoặc loại bỏ. Không phép tính nào trong số này có thể được thực hiện chính xác khi sử dụng chỉ số IOPS, ví dụ.

Để tham khảo, các bậc độ lớn thời gian và viết tắt của chúng được liệt kê trong Bảng 2.1.

**Bảng 2.1: Đơn vị thời gian**

| Đơn vị | Viết tắt | Phần của 1 Giây |
|--------|----------|-----------------|
| Phút | m | 60 |
| Giây | s | 1 |
| Mili giây | ms | 0.001 hay 1/1.000 hay 1 × 10⁻³ |
| Micro giây | μs | 0.000001 hay 1/1.000.000 hay 1 × 10⁻⁶ |
| Nano giây | ns | 0.000000001 hay 1/1.000.000.000 hay 1 × 10⁻⁹ |
| Pico giây | ps | 0.000000000001 hay 1/1.000.000.000.000 hay 1 × 10⁻¹² |

Khi có thể, việc chuyển đổi các loại chỉ số khác sang độ trễ hoặc thời gian cho phép so sánh chúng. Nếu bạn phải chọn giữa 100 I/O mạng hoặc 50 I/O đĩa, làm sao bạn biết cái nào sẽ hoạt động tốt hơn? Đó là một câu hỏi phức tạp, liên quan đến nhiều yếu tố: số hop mạng, tỷ lệ mất gói mạng và retransmit, kích thước I/O, I/O ngẫu nhiên hay tuần tự, loại đĩa, v.v. Nhưng nếu bạn so sánh 100 ms tổng I/O mạng và 50 ms tổng I/O đĩa, sự khác biệt là rõ ràng.

### 2.3.2 Thang Thời Gian (Time Scales)

Mặc dù thời gian có thể được so sánh bằng số, việc có bản năng về thời gian và kỳ vọng hợp lý về độ trễ từ các nguồn khác nhau cũng rất hữu ích. Các thành phần hệ thống hoạt động trên các thang thời gian rất khác nhau (bậc độ lớn), đến mức có thể khó nắm bắt những khác biệt đó lớn đến mức nào. Trong Bảng 2.2, các ví dụ về độ trễ được cung cấp, bắt đầu với truy cập thanh ghi CPU cho bộ xử lý 3.5 GHz. Để minh họa sự khác biệt trong các thang thời gian, bảng cho thấy thời gian trung bình mà mỗi thao tác có thể mất, được chia tỷ lệ sang một hệ thống tưởng tượng trong đó một chu kỳ CPU — 0.3 ns (khoảng một phần ba của một phần tỷ¹ giây) trong thực tế — mất một giây đầy đủ.

> ¹ Phần tỷ US: 1/1.000.000.000

**Bảng 2.2: Ví dụ về thang thời gian của độ trễ hệ thống**

| Sự kiện | Độ trễ | Tỷ lệ |
|---------|--------|--------|
| 1 chu kỳ CPU | 0.3 ns | 1 giây |
| Truy cập cache Level 1 | 0.9 ns | 3 giây |
| Truy cập cache Level 2 | 3 ns | 10 giây |
| Truy cập cache Level 3 | 10 ns | 33 giây |
| Truy cập bộ nhớ chính (DRAM, từ CPU) | 100 ns | 6 phút |
| I/O đĩa thể rắn (bộ nhớ flash) | 10–100 μs | 9–90 giờ |
| I/O đĩa quay | 1–10 ms | 1–12 tháng |
| Internet: San Francisco đến New York | 40 ms | 4 năm |
| Internet: San Francisco đến Vương quốc Anh | 81 ms | 8 năm |
| Khởi động ảo hóa phần cứng nhẹ | 100 ms | 11 năm |
| Internet: San Francisco đến Úc | 183 ms | 19 năm |
| Khởi động ảo hóa hệ điều hành | <1 s | 105 năm |
| Retransmit TCP dựa trên timer | 1–3 s | 105–317 năm |
| Timeout lệnh SCSI | 30 s | 3 thiên niên kỷ |
| Khởi động ảo hóa phần cứng (HW) | 40 s | 4 thiên niên kỷ |
| Khởi động lại hệ thống vật lý | 5 phút | 32 thiên niên kỷ |

Như bạn có thể thấy, thang thời gian cho các chu kỳ CPU là rất nhỏ. Thời gian ánh sáng di chuyển 0.5 m, có lẽ khoảng cách từ mắt bạn đến trang sách này, là khoảng 1.7 ns. Trong cùng khoảng thời gian đó, một CPU hiện đại có thể đã thực hiện năm chu kỳ CPU và xử lý nhiều lệnh.

Để biết thêm về chu kỳ CPU và độ trễ, xem Chương 6, CPU, và về độ trễ I/O đĩa, Chương 9, Đĩa. Các độ trễ Internet được bao gồm là từ Chương 10, Mạng, có thêm nhiều ví dụ.

### 2.3.3 Đánh Đổi (Trade-Offs)

Bạn nên nhận biết một số đánh đổi hiệu năng phổ biến. Đánh đổi tốt/nhanh/rẻ "chọn hai" được thể hiện trong Hình 2.4, cùng với thuật ngữ được điều chỉnh cho các dự án CNTT.

*Hình 2.4: Đánh đổi: chọn hai*

Nhiều dự án CNTT chọn đúng thời hạn và chi phí thấp, để hiệu năng được sửa chữa sau. Lựa chọn này có thể trở nên vấn đề khi các quyết định trước đó cản trở việc cải thiện hiệu năng, chẳng hạn như chọn và triển khai kiến trúc lưu trữ không tối ưu, sử dụng ngôn ngữ lập trình hoặc hệ điều hành được triển khai không hiệu quả, hoặc chọn một thành phần thiếu công cụ phân tích hiệu năng toàn diện.

Một đánh đổi phổ biến trong tinh chỉnh hiệu năng là giữa CPU và bộ nhớ, vì bộ nhớ có thể được sử dụng để cache kết quả, giảm sử dụng CPU. Trên các hệ thống hiện đại với CPU dồi dào, đánh đổi có thể được đảo ngược: thời gian CPU có thể được dùng để nén dữ liệu nhằm giảm sử dụng bộ nhớ.

Các tham số tinh chỉnh thường đi kèm với đánh đổi. Đây là một vài ví dụ:

- **Kích thước bản ghi hệ thống file** (hoặc kích thước block): Kích thước bản ghi nhỏ, gần với kích thước I/O ứng dụng, sẽ hoạt động tốt hơn cho khối lượng công việc I/O ngẫu nhiên và sử dụng hiệu quả hơn bộ nhớ đệm hệ thống file khi ứng dụng đang chạy. Kích thước bản ghi lớn sẽ cải thiện khối lượng công việc streaming, bao gồm sao lưu hệ thống file.
- **Kích thước bộ đệm mạng**: Kích thước bộ đệm nhỏ sẽ giảm chi phí bộ nhớ cho mỗi kết nối, giúp hệ thống mở rộng. Kích thước lớn sẽ cải thiện thông lượng mạng.

Hãy tìm kiếm những đánh đổi như vậy khi thực hiện thay đổi cho hệ thống.

### 2.3.4 Nỗ Lực Tinh Chỉnh (Tuning Efforts)

Tinh chỉnh hiệu năng hiệu quả nhất khi được thực hiện gần nhất với nơi công việc được thực hiện. Đối với khối lượng công việc được điều khiển bởi ứng dụng, điều này có nghĩa là bên trong chính ứng dụng. Bảng 2.3 cho thấy một ví dụ ngăn xếp phần mềm với khả năng tinh chỉnh.

**Bảng 2.3: Ví dụ về mục tiêu tinh chỉnh**

| Lớp | Ví dụ Mục tiêu Tinh chỉnh |
|-----|---------------------------|
| Ứng dụng | Logic ứng dụng, kích thước hàng đợi yêu cầu, truy vấn cơ sở dữ liệu được thực hiện |
| Cơ sở dữ liệu | Bố cục bảng cơ sở dữ liệu, chỉ mục, đệm |
| System call | Memory-mapped hoặc read/write, cờ I/O đồng bộ hoặc bất đồng bộ |
| Hệ thống file | Kích thước bản ghi, kích thước bộ nhớ đệm, tham số tinh chỉnh hệ thống file, journaling |
| Lưu trữ | Cấp RAID, số lượng và loại đĩa, tham số tinh chỉnh lưu trữ |

Bằng cách tinh chỉnh ở cấp ứng dụng, bạn có thể loại bỏ hoặc giảm các truy vấn cơ sở dữ liệu và cải thiện hiệu năng theo hệ số lớn (ví dụ: 20 lần). Tinh chỉnh xuống cấp thiết bị lưu trữ có thể loại bỏ hoặc cải thiện I/O lưu trữ, nhưng một khoản thuế đã được trả trong việc thực thi mã ngăn xếp OS cấp cao hơn, nên điều này chỉ có thể cải thiện hiệu năng ứng dụng kết quả theo phần trăm (ví dụ: 20%).

Có một lý do khác để tìm cải thiện hiệu năng lớn ở cấp ứng dụng. Nhiều môi trường ngày nay nhắm đến triển khai nhanh cho các tính năng và chức năng, đẩy các thay đổi phần mềm vào sản xuất hàng tuần hoặc hàng ngày.² Phát triển và kiểm thử ứng dụng do đó có xu hướng tập trung vào tính chính xác, để lại ít hoặc không có thời gian cho đo lường hoặc tối ưu hiệu năng trước khi triển khai sản xuất. Các hoạt động này được thực hiện sau, khi hiệu năng trở thành vấn đề.

> ² Ví dụ về các môi trường thay đổi nhanh bao gồm đám mây Netflix và Shopify, đẩy nhiều thay đổi mỗi ngày.

Mặc dù ứng dụng có thể là cấp hiệu quả nhất để tinh chỉnh, nó không nhất thiết là cấp hiệu quả nhất để quan sát. Các truy vấn chậm có thể được hiểu tốt nhất từ thời gian chúng dành trên CPU, hoặc từ I/O hệ thống file và đĩa mà chúng thực hiện. Những điều này có thể quan sát được từ các công cụ hệ điều hành.

Trong nhiều môi trường (đặc biệt là điện toán đám mây) cấp ứng dụng đang được phát triển liên tục, đẩy các thay đổi phần mềm vào sản xuất hàng tuần hoặc hàng ngày. Các cải thiện hiệu năng lớn, bao gồm sửa chữa cho các hồi quy, thường được tìm thấy khi mã ứng dụng thay đổi. Trong các môi trường này, tinh chỉnh cho hệ điều hành và khả năng quan sát từ hệ điều hành có thể dễ bị bỏ qua. Hãy nhớ rằng phân tích hiệu năng hệ điều hành cũng có thể xác định các vấn đề cấp ứng dụng, không chỉ các vấn đề cấp OS, trong một số trường hợp dễ dàng hơn so với chỉ từ ứng dụng.

### 2.3.5 Mức Độ Phù Hợp (Level of Appropriateness)

Các tổ chức và môi trường khác nhau có yêu cầu khác nhau về hiệu năng. Bạn có thể đã tham gia một tổ chức nơi phân tích sâu hơn nhiều so với những gì bạn đã thấy trước đây, hoặc thậm chí không biết là có thể. Hoặc bạn có thể thấy rằng, ở nơi làm việc mới, những gì bạn coi là phân tích cơ bản được coi là nâng cao và chưa bao giờ được thực hiện trước đó (tin tốt: quả chín treo thấp!).

Điều này không nhất thiết có nghĩa là một số tổ chức đang làm đúng và một số sai. Nó phụ thuộc vào lợi tức đầu tư (ROI) cho chuyên môn hiệu năng. Các tổ chức có trung tâm dữ liệu lớn hoặc môi trường đám mây lớn có thể thuê một đội kỹ sư hiệu năng phân tích mọi thứ, bao gồm nội bộ nhân và bộ đếm hiệu năng CPU, và thường xuyên sử dụng nhiều công cụ tracing. Họ cũng có thể mô hình hóa hiệu năng một cách chính thức và phát triển dự đoán chính xác cho tăng trưởng tương lai. Đối với các môi trường chi hàng triệu mỗi năm cho tính toán, việc tuyển dụng đội hiệu năng như vậy có thể dễ dàng được biện minh, vì những chiến thắng họ tìm thấy chính là ROI. Các startup nhỏ với chi tiêu tính toán khiêm tốn có thể chỉ thực hiện kiểm tra bề mặt, tin tưởng các giải pháp giám sát bên thứ ba để kiểm tra hiệu năng và cung cấp cảnh báo.

Tuy nhiên, như đã giới thiệu trong Chương 1, hiệu năng hệ thống không chỉ về chi phí: nó còn về trải nghiệm người dùng cuối. Một startup có thể thấy cần thiết phải đầu tư vào kỹ thuật hiệu năng để cải thiện độ trễ trang web hoặc ứng dụng. ROI ở đây không nhất thiết là giảm chi phí, mà là khách hàng hạnh phúc hơn thay vì cựu khách hàng.

Các môi trường cực đoan nhất bao gồm sàn giao dịch chứng khoán và các nhà giao dịch tần suất cao, nơi hiệu năng và độ trễ là quan trọng và có thể biện minh cho nỗ lực và chi phí lớn. Như một ví dụ, một cáp xuyên Đại Tây Dương giữa sàn giao dịch New York và London đã được lên kế hoạch với chi phí 300 triệu đô la, để giảm độ trễ truyền tải 6 ms [Williams 11].

### 2.3.6 Khi Nào Dừng Phân Tích (When to Stop Analysis)

Một thách thức bất cứ khi nào thực hiện phân tích hiệu năng là biết khi nào nên dừng. Có quá nhiều công cụ, và quá nhiều thứ để kiểm tra!

Khi tôi dạy các lớp hiệu năng (như tôi đã bắt đầu làm lại gần đây), tôi có thể cho sinh viên một vấn đề hiệu năng có ba nguyên nhân góp phần, và thấy rằng một số sinh viên dừng lại sau khi tìm thấy một nguyên nhân, số khác hai, và số khác tìm được cả ba. Một số sinh viên tiếp tục, cố gắng tìm thêm nhiều nguyên nhân cho vấn đề hiệu năng. Ai đang làm đúng? Có thể dễ dàng nói rằng bạn nên dừng lại sau khi tìm thấy cả ba nguyên nhân, nhưng đối với các vấn đề thực tế bạn không biết số lượng nguyên nhân.

Đây là ba kịch bản khi bạn có thể xem xét dừng phân tích, với một số ví dụ cá nhân:

- **Khi bạn đã giải thích phần lớn vấn đề hiệu năng.** Một ứng dụng Java đang tiêu thụ CPU gấp ba lần so với trước đây. Vấn đề đầu tiên tôi tìm thấy là exception stack đang tiêu thụ CPU. Tôi sau đó định lượng thời gian trong các stack đó và thấy rằng chúng chiếm chỉ 12% dấu chân CPU tổng thể. Nếu con số đó gần 66%, tôi có thể đã dừng phân tích — độ chậm 3 lần sẽ được giải thích. Nhưng trong trường hợp này, ở 12%, tôi cần tiếp tục tìm kiếm.
- **Khi ROI tiềm năng ít hơn chi phí phân tích.** Một số vấn đề hiệu năng tôi làm việc có thể mang lại chiến thắng được đo bằng hàng chục triệu đô la mỗi năm. Đối với những vấn đề này, tôi có thể biện minh việc dành hàng tháng thời gian của mình (chi phí kỹ thuật) cho phân tích. Các chiến thắng hiệu năng khác, chẳng hạn cho các microservice nhỏ, có thể được đo bằng hàng trăm đô la: có thể không đáng ngay cả một giờ thời gian kỹ thuật để phân tích chúng.
- **Khi có ROI lớn hơn ở nơi khác.** Ngay cả khi hai kịch bản trước chưa được đáp ứng, có thể có ROI lớn hơn ở nơi khác được ưu tiên.

Nếu bạn đang làm việc toàn thời gian như kỹ sư hiệu năng, việc ưu tiên phân tích các vấn đề khác nhau dựa trên ROI tiềm năng có lẽ là nhiệm vụ hàng ngày.

### 2.3.7 Khuyến Nghị Tại Thời Điểm (Point-in-Time Recommendations)

Đặc tính hiệu năng của các môi trường thay đổi theo thời gian, do thêm nhiều người dùng, phần cứng mới hơn, và phần mềm hoặc firmware được cập nhật. Một môi trường hiện bị giới hạn bởi hạ tầng mạng 10 Gbit/s có thể bắt đầu gặp nút thắt cổ chai ở hiệu năng đĩa hoặc CPU sau khi nâng cấp lên 100 Gbit/s.

Các khuyến nghị hiệu năng, đặc biệt là giá trị của các tham số tinh chỉnh, chỉ hợp lệ tại một thời điểm cụ thể. Lời khuyên tốt nhất từ một chuyên gia hiệu năng một tuần có thể trở nên không hợp lệ một tuần sau khi nâng cấp phần mềm hoặc phần cứng, hoặc sau khi thêm người dùng.

Các giá trị tham số tinh chỉnh tìm được trên Internet có thể mang lại chiến thắng nhanh — trong một số trường hợp. Chúng cũng có thể làm tê liệt hiệu năng nếu chúng không phù hợp cho hệ thống hoặc khối lượng công việc của bạn, từng phù hợp nhưng giờ không còn, hoặc chỉ phù hợp như giải pháp tạm thời cho bug phần mềm được sửa đúng cách trong bản nâng cấp sau. Nó giống như lục tủ thuốc của người khác và uống thuốc có thể không phù hợp cho bạn, có thể đã hết hạn, hoặc chỉ nên uống trong thời gian ngắn.

Khi thay đổi các tham số tinh chỉnh, có thể hữu ích để lưu trữ chúng trong hệ thống quản lý phiên bản với lịch sử chi tiết. (Bạn có thể đã làm điều tương tự khi sử dụng các công cụ quản lý cấu hình như Puppet, Salt, Chef, v.v.) Bằng cách đó, thời điểm và lý do thay đổi tham số tinh chỉnh có thể được kiểm tra sau này.

### 2.3.8 Tải so với Kiến Trúc (Load vs. Architecture)

Một ứng dụng có thể hoạt động kém do vấn đề với cấu hình phần mềm và phần cứng mà nó đang chạy: kiến trúc và triển khai của nó. Tuy nhiên, ứng dụng cũng có thể hoạt động kém chỉ đơn giản do quá nhiều tải được áp dụng, dẫn đến xếp hàng và độ trễ dài. Tải và kiến trúc được minh họa trong Hình 2.5.

*Hình 2.5: Tải so với kiến trúc*

Nếu phân tích kiến trúc cho thấy xếp hàng công việc nhưng không có vấn đề với cách công việc được thực hiện, vấn đề có thể là quá nhiều tải đang được áp dụng. Trong môi trường điện toán đám mây, đây là thời điểm mà thêm instance máy chủ có thể được giới thiệu theo nhu cầu để xử lý công việc.

Ví dụ, vấn đề kiến trúc có thể là ứng dụng đơn luồng (single-threaded) đang bận trên CPU, với các yêu cầu xếp hàng trong khi các CPU khác khả dụng và nhàn rỗi. Trong trường hợp này, hiệu năng bị giới hạn bởi kiến trúc đơn luồng của ứng dụng. Vấn đề kiến trúc khác có thể là chương trình đa luồng tranh chấp một khóa đơn lẻ, sao cho chỉ một luồng có thể tiến triển trong khi các luồng khác chờ đợi.

Vấn đề tải có thể là ứng dụng đa luồng đang bận trên tất cả CPU khả dụng, với các yêu cầu vẫn đang xếp hàng. Trong trường hợp này, hiệu năng bị giới hạn bởi dung lượng CPU khả dụng, hay nói cách khác, bởi có nhiều tải hơn CPU có thể xử lý.

### 2.3.9 Khả Năng Mở Rộng (Scalability)

Hiệu năng của hệ thống dưới tải tăng dần là khả năng mở rộng của nó. Hình 2.6 cho thấy hồ sơ thông lượng điển hình khi tải của hệ thống tăng.

*Hình 2.6: Thông lượng so với tải*

Trong một khoảng thời gian, khả năng mở rộng tuyến tính được quan sát. Sau đó đạt đến một điểm, được đánh dấu bằng đường chấm, nơi tranh chấp cho một tài nguyên bắt đầu làm suy giảm thông lượng. Điểm này có thể được mô tả là **điểm gối** (knee point), vì nó là ranh giới giữa hai hàm. Vượt qua điểm này, hồ sơ thông lượng rời khỏi khả năng mở rộng tuyến tính, khi tranh chấp cho tài nguyên tăng. Cuối cùng, chi phí cho tranh chấp tăng và tính nhất quán (coherency) khiến ít công việc được hoàn thành và thông lượng giảm.

Điểm này có thể xảy ra khi một thành phần đạt 100% sử dụng: **điểm bão hòa**. Nó cũng có thể xảy ra khi một thành phần tiến gần 100% sử dụng và xếp hàng bắt đầu trở nên thường xuyên và đáng kể.

Ví dụ, hệ thống có thể thể hiện hồ sơ này là ứng dụng thực hiện tính toán nặng, với thêm tải được thêm dưới dạng luồng bổ sung. Khi CPU tiến gần 100% sử dụng, thời gian phản hồi bắt đầu suy giảm khi độ trễ bộ lập lịch CPU tăng. Sau hiệu năng đỉnh, ở 100% sử dụng, thông lượng bắt đầu giảm khi thêm luồng được thêm, gây ra nhiều context switch hơn, tiêu thụ tài nguyên CPU và khiến ít công việc thực tế được hoàn thành.

Cùng đường cong có thể được thấy nếu bạn thay thế "tải" trên trục x bằng tài nguyên như lõi CPU. Để biết thêm về chủ đề này, xem Phần 2.6, Mô Hình Hóa.

Sự suy giảm hiệu năng cho khả năng mở rộng phi tuyến, về thời gian phản hồi trung bình hoặc độ trễ, được vẽ biểu đồ trong Hình 2.7 [Cockcroft 95].

*Hình 2.7: Suy giảm hiệu năng*

Thời gian phản hồi cao hơn, tất nhiên, là xấu. Hồ sơ suy giảm "nhanh" có thể xảy ra cho tải bộ nhớ, khi hệ thống bắt đầu di chuyển các trang bộ nhớ ra đĩa để giải phóng bộ nhớ chính. Hồ sơ suy giảm "chậm" có thể xảy ra cho tải CPU.

Một ví dụ hồ sơ "nhanh" khác là I/O đĩa. Khi tải (và mức sử dụng đĩa kết quả) tăng, I/O càng có khả năng xếp hàng sau I/O khác. Một đĩa quay nhàn rỗi (không phải thể rắn) có thể phục vụ I/O với thời gian phản hồi khoảng 1 ms, nhưng khi tải tăng, điều này có thể tiến gần 10 ms. Điều này được mô hình hóa trong Phần 2.6.5, Lý Thuyết Hàng Đợi, dưới M/D/1 và 60% Sử dụng, và hiệu năng đĩa được đề cập trong Chương 9, Đĩa.

Khả năng mở rộng tuyến tính của thời gian phản hồi có thể xảy ra nếu ứng dụng bắt đầu trả về lỗi khi tài nguyên không khả dụng, thay vì xếp hàng công việc. Ví dụ, web server có thể trả về 503 "Service Unavailable" thay vì thêm yêu cầu vào hàng đợi, để những yêu cầu được phục vụ có thể được thực hiện với thời gian phản hồi nhất quán.

### 2.3.10 Chỉ Số (Metrics)

Các chỉ số hiệu năng là các thống kê được chọn được tạo ra bởi hệ thống, ứng dụng hoặc các công cụ bổ sung để đo hoạt động quan tâm. Chúng được nghiên cứu cho phân tích và giám sát hiệu năng, hoặc bằng số trên dòng lệnh hoặc đồ họa sử dụng trực quan hóa.

Các loại chỉ số hiệu năng hệ thống phổ biến bao gồm:

- **Throughput** (Thông lượng): Hoặc thao tác hoặc khối lượng dữ liệu mỗi giây
- **IOPS**: Số thao tác I/O mỗi giây
- **Utilization** (Mức sử dụng): Mức độ bận rộn của tài nguyên, tính theo phần trăm
- **Latency** (Độ trễ): Thời gian thao tác, dưới dạng trung bình hoặc phân vị

**Chi phí (Overhead)**

Các chỉ số hiệu năng không miễn phí; tại một thời điểm nào đó, chu kỳ CPU phải được chi tiêu để thu thập và lưu trữ chúng. Điều này gây ra chi phí, có thể tác động tiêu cực đến hiệu năng của mục tiêu đo lường. Đây được gọi là **hiệu ứng quan sát viên** (observer effect). (Nó thường bị nhầm lẫn với Nguyên lý Bất định Heisenberg, mô tả giới hạn độ chính xác mà tại đó các cặp thuộc tính vật lý, như vị trí và động lượng, có thể được biết.)

**Vấn đề (Issues)**

Bạn có thể giả định rằng nhà cung cấp phần mềm đã cung cấp các chỉ số được chọn tốt, không có bug và cung cấp khả năng hiển thị đầy đủ. Trong thực tế, các chỉ số có thể gây nhầm lẫn, phức tạp, không đáng tin cậy, không chính xác và thậm chí sai hoàn toàn (do bug). Đôi khi một chỉ số đúng trong một phiên bản phần mềm nhưng không được cập nhật để phản ánh việc thêm mã và đường dẫn mã mới.

### 2.3.11 Mức Sử Dụng (Utilization)

Thuật ngữ mức sử dụng³ thường được sử dụng cho hệ điều hành để mô tả việc sử dụng thiết bị, chẳng hạn như cho các thiết bị CPU và đĩa. Mức sử dụng có thể dựa trên thời gian hoặc dựa trên dung lượng.

> ³ Viết là utilisation ở một số nơi trên thế giới.

**Dựa trên Thời gian (Time-Based)**

Mức sử dụng dựa trên thời gian được định nghĩa chính thức trong lý thuyết hàng đợi. Ví dụ [Gunther 97]:

> khoảng thời gian trung bình mà máy chủ hoặc tài nguyên bận

cùng với tỷ lệ:

```
U = B/T
```

trong đó U = mức sử dụng, B = tổng thời gian hệ thống bận trong T, khoảng thời gian quan sát.

Đây cũng là "mức sử dụng" dễ dàng nhất từ các công cụ hiệu năng hệ điều hành. Công cụ giám sát đĩa iostat(1) gọi chỉ số này là %b cho phần trăm bận, thuật ngữ truyền tải tốt hơn chỉ số cơ bản: B/T.

Chỉ số mức sử dụng này cho chúng ta biết mức độ bận rộn của một thành phần: khi một thành phần tiến gần 100% sử dụng, hiệu năng có thể suy giảm nghiêm trọng khi có tranh chấp cho tài nguyên. Các chỉ số khác có thể được kiểm tra để xác nhận và xem liệu thành phần đó đã trở thành nút thắt cổ chai hệ thống hay chưa.

Một số thành phần có thể phục vụ nhiều thao tác song song. Đối với chúng, hiệu năng có thể không suy giảm nhiều ở 100% sử dụng vì chúng có thể chấp nhận thêm công việc. Để hiểu điều này, hãy xem xét thang máy tòa nhà. Nó có thể được coi là được sử dụng khi đang di chuyển giữa các tầng, và không được sử dụng khi nhàn rỗi chờ đợi. Tuy nhiên, thang máy có thể chấp nhận thêm hành khách ngay cả khi nó bận 100% thời gian đáp ứng cuộc gọi — nghĩa là, nó ở mức sử dụng 100%.

Một đĩa ở 100% bận cũng có thể chấp nhận và xử lý thêm công việc, ví dụ, bằng cách đệm ghi trong bộ nhớ đệm trên đĩa để hoàn thành sau. Các mảng lưu trữ thường chạy ở 100% sử dụng vì một đĩa nào đó bận 100% thời gian, nhưng mảng có nhiều đĩa nhàn rỗi và có thể chấp nhận thêm công việc.

**Dựa trên Dung lượng (Capacity-Based)**

Định nghĩa khác của mức sử dụng được sử dụng bởi các chuyên gia CNTT trong bối cảnh hoạch định dung lượng [Wong 97]:

> Một hệ thống hoặc thành phần (như ổ đĩa) có khả năng cung cấp một lượng thông lượng nhất định. Ở bất kỳ mức hiệu năng nào, hệ thống hoặc thành phần đang hoạt động ở một tỷ lệ nào đó của dung lượng. Tỷ lệ đó được gọi là mức sử dụng.

Điều này định nghĩa mức sử dụng theo dung lượng thay vì thời gian. Nó ngụ ý rằng một đĩa ở 100% sử dụng không thể chấp nhận thêm công việc. Với định nghĩa dựa trên thời gian, 100% sử dụng chỉ có nghĩa là nó bận 100% thời gian.

> **100% bận không có nghĩa là 100% dung lượng.**

Trong thế giới lý tưởng, chúng ta sẽ có thể đo cả hai loại mức sử dụng cho một thiết bị. Thật không may, điều này thường không khả thi.

Trong cuốn sách này, mức sử dụng thường đề cập đến phiên bản dựa trên thời gian, mà bạn cũng có thể gọi là thời gian không nhàn rỗi (non-idle time). Phiên bản dung lượng được sử dụng cho một số chỉ số dựa trên khối lượng, chẳng hạn như sử dụng bộ nhớ.

### 2.3.12 Bão Hòa (Saturation)

Mức độ mà nhiều công việc hơn được yêu cầu của một tài nguyên so với những gì nó có thể xử lý là bão hòa. Bão hòa bắt đầu xảy ra ở 100% sử dụng (dựa trên dung lượng), vì công việc thêm không thể được xử lý và bắt đầu xếp hàng. Điều này được minh họa trong Hình 2.8.

*Hình 2.8: Mức sử dụng so với bão hòa*

Hình vẽ minh họa bão hòa tăng tuyến tính vượt qua mốc sử dụng 100% dựa trên dung lượng khi tải tiếp tục tăng. Bất kỳ mức bão hòa nào đều là vấn đề hiệu năng, vì thời gian được dành để chờ đợi (độ trễ). Đối với mức sử dụng dựa trên thời gian (phần trăm bận), xếp hàng và do đó bão hòa có thể không bắt đầu ở mốc sử dụng 100%, tùy thuộc vào mức độ mà tài nguyên có thể hoạt động trên công việc song song.

### 2.3.13 Profiling

Profiling xây dựng bức tranh của mục tiêu có thể được nghiên cứu và hiểu. Trong lĩnh vực hiệu năng tính toán, profiling thường được thực hiện bằng cách lấy mẫu trạng thái của hệ thống theo khoảng thời gian định kỳ và sau đó nghiên cứu tập hợp các mẫu.

Không giống như các chỉ số trước đó đã đề cập, bao gồm IOPS và thông lượng, việc sử dụng lấy mẫu cung cấp cái nhìn thô của hoạt động mục tiêu. Mức độ thô phụ thuộc vào tốc độ lấy mẫu.

### 2.3.14 Bộ Nhớ Đệm (Caching)

Bộ nhớ đệm thường được sử dụng để cải thiện hiệu năng. Cache lưu trữ kết quả từ tầng lưu trữ chậm hơn trong tầng lưu trữ nhanh hơn, để tham khảo. Ví dụ là cache các khối đĩa trong bộ nhớ chính (RAM).

Nhiều tầng cache có thể được sử dụng. CPU thường sử dụng nhiều bộ nhớ đệm phần cứng cho bộ nhớ chính (Level 1, 2 và 3), bắt đầu với cache rất nhanh nhưng nhỏ (Level 1) và tăng cả kích thước lưu trữ và độ trễ truy cập. Đây là đánh đổi kinh tế giữa mật độ và độ trễ; các cấp và kích thước được chọn cho hiệu năng tốt nhất cho không gian trên chip có sẵn.

Một chỉ số để hiểu hiệu năng cache là **tỷ lệ trúng cache** (hit ratio) — số lần dữ liệu cần thiết được tìm thấy trong cache (hit) so với tổng số truy cập (hit + miss):

```
hit ratio = hits / (hits + misses)
```

Càng cao càng tốt, vì tỷ lệ cao hơn phản ánh nhiều dữ liệu được truy cập thành công từ phương tiện nhanh hơn. Hình 2.9 cho thấy cải thiện hiệu năng kỳ vọng cho tỷ lệ trúng cache tăng.

*Hình 2.9: Tỷ lệ trúng cache và hiệu năng*

Sự khác biệt hiệu năng giữa 98% và 99% lớn hơn nhiều so với giữa 10% và 11%. Đây là hồ sơ phi tuyến vì sự khác biệt tốc độ giữa cache hit và miss — hai tầng lưu trữ đang hoạt động. Sự khác biệt càng lớn, đường dốc càng lớn.

Một chỉ số khác để hiểu hiệu năng cache là **tỷ lệ miss** (cache miss rate), tính bằng số miss mỗi giây. Điều này tỷ lệ thuận (tuyến tính) với hình phạt hiệu năng của mỗi miss và có thể dễ giải thích hơn.

Ví dụ, khối lượng công việc A và B thực hiện cùng tác vụ sử dụng thuật toán khác nhau và sử dụng cache bộ nhớ chính để tránh đọc từ đĩa. Khối lượng công việc A có tỷ lệ trúng cache 90%, và khối lượng công việc B có tỷ lệ trúng cache 80%. Thông tin này đơn lẻ gợi ý khối lượng công việc A hoạt động tốt hơn. Nhưng nếu khối lượng công việc A có tỷ lệ miss 200/giây và khối lượng công việc B, 20/giây? Dưới góc nhìn đó, khối lượng công việc B thực hiện ít hơn 10 lần số lần đọc đĩa, có thể hoàn thành tác vụ nhanh hơn nhiều. Để chắc chắn, tổng thời gian chạy cho mỗi khối lượng công việc có thể được tính:

```
runtime = (hit rate × hit latency) + (miss rate × miss latency)
```

**Thuật toán**

Các thuật toán và chính sách quản lý cache xác định những gì cần lưu trong không gian giới hạn có sẵn. Most recently used (MRU) đề cập đến chính sách giữ lại cache. Least recently used (LRU) có thể đề cập đến chính sách trục xuất cache tương đương. Cũng có most frequently used (MFU) và least frequently used (LFU).

**Cache Nóng, Lạnh và Ấm**

- **Cold** (Lạnh): Cache trống, hoặc chứa dữ liệu không mong muốn. Tỷ lệ trúng bằng không.
- **Warm** (Ấm): Cache được điền với dữ liệu hữu ích nhưng tỷ lệ trúng chưa đủ cao để được coi là hot.
- **Hot** (Nóng): Cache được điền với dữ liệu thường xuyên được yêu cầu và có tỷ lệ trúng cao, ví dụ trên 99%.
- **Warmth** (Độ ấm): Mô tả mức hot hay cold của cache.

Khi cache được khởi tạo lần đầu, chúng bắt đầu cold và sau đó ấm lên theo thời gian. Khi cache lớn hoặc lưu trữ cấp tiếp theo chậm (hoặc cả hai), cache có thể mất nhiều thời gian để được điền và ấm lên.

### 2.3.15 Biết-Không biết (Known-Unknowns)

Được giới thiệu trong Lời nói đầu, khái niệm về known-knowns, known-unknowns, và unknown-unknowns rất quan trọng cho lĩnh vực hiệu năng:

- **Known-knowns** (Biết-biết): Đây là những thứ bạn biết. Bạn biết bạn nên kiểm tra một chỉ số hiệu năng, và bạn biết giá trị hiện tại của nó.
- **Known-unknowns** (Biết-không biết): Đây là những thứ bạn biết rằng bạn không biết. Bạn biết bạn có thể kiểm tra một chỉ số nhưng chưa quan sát nó.
- **Unknown-unknowns** (Không biết-không biết): Đây là những thứ bạn không biết rằng bạn không biết. Ví dụ, bạn có thể không biết rằng device interrupt có thể trở thành nguồn tiêu thụ CPU nặng, nên bạn không kiểm tra chúng.

Hiệu năng là lĩnh vực mà "bạn biết càng nhiều, bạn càng không biết nhiều." Bạn càng học về hệ thống, bạn càng nhận ra nhiều unknown-unknowns, sau đó trở thành known-unknowns mà bạn có thể kiểm tra.

## 2.4 Các Góc Nhìn (Perspectives)

Có hai góc nhìn phổ biến cho phân tích hiệu năng, mỗi góc nhìn có đối tượng, chỉ số và cách tiếp cận khác nhau. Đó là phân tích khối lượng công việc (workload analysis) và phân tích tài nguyên (resource analysis). Chúng có thể được coi là phân tích từ trên xuống hoặc từ dưới lên của ngăn xếp phần mềm hệ điều hành, như thể hiện trong Hình 2.10.

*Hình 2.10: Các góc nhìn phân tích*

Phần 2.5, Phương Pháp Luận, cung cấp các chiến lược cụ thể để áp dụng cho mỗi góc nhìn. Các góc nhìn này được giới thiệu ở đây chi tiết hơn.

### 2.4.1 Phân Tích Tài Nguyên (Resource Analysis)

Phân tích tài nguyên bắt đầu với phân tích các tài nguyên hệ thống: CPU, bộ nhớ, đĩa, giao diện mạng, bus và interconnect. Nó thường được thực hiện bởi quản trị viên hệ thống — những người chịu trách nhiệm về tài nguyên vật lý. Các hoạt động bao gồm:

- **Điều tra vấn đề hiệu năng**: Để xem một loại tài nguyên cụ thể có phải là nguyên nhân không
- **Hoạch định dung lượng**: Cho thông tin để giúp xác định kích thước hệ thống mới, và xem khi nào tài nguyên hệ thống hiện tại có thể cạn kiệt

Góc nhìn này tập trung vào mức sử dụng, để xác định khi nào tài nguyên đang ở hoặc tiến gần giới hạn. Các chỉ số phù hợp nhất cho phân tích tài nguyên bao gồm:

- IOPS
- Thông lượng (Throughput)
- Mức sử dụng (Utilization)
- Bão hòa (Saturation)

Phân tích tài nguyên là cách tiếp cận phổ biến cho phân tích hiệu năng, một phần nhờ tài liệu sẵn có rộng rãi về chủ đề này. Tài liệu như vậy tập trung vào các công cụ "stat" của hệ điều hành: vmstat(8), iostat(1), mpstat(1). Điều quan trọng khi bạn đọc tài liệu như vậy là hiểu rằng đây là một góc nhìn, nhưng không phải góc nhìn duy nhất.

### 2.4.2 Phân Tích Khối Lượng Công Việc (Workload Analysis)

Phân tích khối lượng công việc (xem Hình 2.11) kiểm tra hiệu năng của ứng dụng: khối lượng công việc được áp dụng và cách ứng dụng phản hồi. Nó thường được sử dụng bởi nhà phát triển ứng dụng và nhân viên hỗ trợ — những người chịu trách nhiệm về phần mềm và cấu hình ứng dụng.

*Hình 2.11: Phân tích khối lượng công việc*

Các mục tiêu cho phân tích khối lượng công việc là:

- **Yêu cầu (Requests)**: Khối lượng công việc được áp dụng
- **Độ trễ (Latency)**: Thời gian phản hồi của ứng dụng
- **Hoàn thành (Completion)**: Tìm kiếm lỗi

Nghiên cứu yêu cầu khối lượng công việc thường bao gồm kiểm tra và tóm tắt các thuộc tính của chúng: đây là quá trình đặc trưng hóa khối lượng công việc (workload characterization). Đối với cơ sở dữ liệu, các thuộc tính này có thể bao gồm host client, tên cơ sở dữ liệu, bảng và chuỗi truy vấn. Dữ liệu này có thể giúp xác định công việc không cần thiết, hoặc công việc mất cân bằng. Hãy nhớ rằng truy vấn nhanh nhất là truy vấn mà bạn không thực hiện.

Độ trễ (thời gian phản hồi) là chỉ số quan trọng nhất để biểu thị hiệu năng ứng dụng. Đối với MySQL, đó là độ trễ truy vấn; đối với Apache, đó là độ trễ yêu cầu HTTP; v.v.

Các chỉ số phù hợp nhất cho phân tích khối lượng công việc bao gồm:

- Thông lượng (giao dịch mỗi giây)
- Độ trễ (Latency)

## 2.5 Phương Pháp Luận (Methodology)

Khi đối mặt với một môi trường hệ thống phức tạp và hoạt động kém, thách thức đầu tiên có thể là biết bắt đầu phân tích từ đâu và tiến hành như thế nào. Phương pháp luận có thể giúp bạn tiếp cận các hệ thống phức tạp này bằng cách chỉ ra nơi bắt đầu phân tích và gợi ý quy trình hiệu quả để tuân theo.

Phần này mô tả nhiều phương pháp luận và quy trình hiệu năng cho hiệu năng hệ thống và tinh chỉnh, một số do tôi phát triển. Các phương pháp luận này giúp người mới bắt đầu và phục vụ như lời nhắc nhở cho chuyên gia. Một số phương pháp chống (anti-methodology) cũng được bao gồm.

**Bảng 2.4: Các phương pháp luận hiệu năng hệ thống tổng quát**

| Phần | Phương pháp luận | Loại |
|------|-------------------|------|
| 2.5.1 | Anti-method đèn đường | Phân tích quan sát |
| 2.5.2 | Anti-method thay đổi ngẫu nhiên | Phân tích thực nghiệm |
| 2.5.3 | Anti-method đổ lỗi người khác | Phân tích giả thuyết |
| 2.5.4 | Phương pháp danh sách kiểm tra ad hoc | Phân tích quan sát và thực nghiệm |
| 2.5.5 | Mô tả vấn đề | Thu thập thông tin |
| 2.5.6 | Phương pháp khoa học | Phân tích quan sát |
| 2.5.7 | Chu kỳ chẩn đoán | Vòng đời phân tích |
| 2.5.8 | Phương pháp công cụ | Phân tích quan sát |
| 2.5.9 | Phương pháp USE | Phân tích quan sát |
| 2.5.10 | Phương pháp RED | Phân tích quan sát |
| 2.5.11 | Đặc trưng hóa khối lượng công việc | Phân tích quan sát, hoạch định dung lượng |
| 2.5.12 | Phân tích đào sâu | Phân tích quan sát |
| 2.5.13 | Phân tích độ trễ | Phân tích quan sát |
| 2.5.14 | Method R | Phân tích quan sát |
| 2.5.15 | Tracing sự kiện | Phân tích quan sát |
| 2.5.16 | Thống kê cơ sở | Phân tích quan sát |
| 2.5.17 | Tinh chỉnh hiệu năng tĩnh | Phân tích quan sát, hoạch định dung lượng |
| 2.5.18 | Tinh chỉnh cache | Phân tích quan sát, tinh chỉnh |
| 2.5.19 | Micro-benchmarking | Phân tích thực nghiệm |
| 2.5.20 | Phương châm hiệu năng | Tinh chỉnh |

### 2.5.1 Anti-Method Đèn Đường (Streetlight Anti-Method)

Phương pháp này thực chất là sự vắng mặt của một phương pháp luận có chủ đích. Người dùng phân tích hiệu năng bằng cách chọn các công cụ quan sát quen thuộc, tìm thấy trên Internet, hoặc chỉ ngẫu nhiên để xem có gì rõ ràng xuất hiện không. Cách tiếp cận này được ăn may và có thể bỏ qua nhiều loại vấn đề.

Phương pháp luận này được đặt tên theo thiên kiến quan sát gọi là hiệu ứng đèn đường (streetlight effect), được minh họa bởi câu chuyện ngụ ngôn:

> Một đêm, một cảnh sát thấy người say đang tìm kiếm dưới ánh đèn đường và hỏi anh ta đang tìm gì. Người say nói anh ta đã mất chìa khóa. Cảnh sát cũng không tìm thấy và hỏi: "Anh có chắc mất ở đây, dưới ánh đèn đường không?" Người say trả lời: "Không, nhưng đây là nơi ánh sáng tốt nhất."

### 2.5.2 Anti-Method Thay Đổi Ngẫu Nhiên (Random Change Anti-Method)

Đây là phương pháp chống thực nghiệm. Người dùng đoán ngẫu nhiên vấn đề có thể ở đâu và sau đó thay đổi mọi thứ cho đến khi nó biến mất. Cách tiếp cận như sau:

1. Chọn một mục ngẫu nhiên để thay đổi (ví dụ: tham số tinh chỉnh).
2. Thay đổi nó theo một hướng.
3. Đo hiệu năng.
4. Thay đổi nó theo hướng khác.
5. Đo hiệu năng.
6. Kết quả ở bước 3 hoặc 5 có tốt hơn đường cơ sở không? Nếu có, giữ thay đổi và quay lại bước 1.

Mặc dù quá trình này cuối cùng có thể tìm ra tinh chỉnh hoạt động cho khối lượng công việc được thử nghiệm, nó rất tốn thời gian và cũng có thể dẫn đến tinh chỉnh không có ý nghĩa lâu dài.

### 2.5.3 Anti-Method Đổ Lỗi Người Khác (Blame-Someone-Else Anti-Method)

Anti-methodology này tuân theo các bước:

1. Tìm một thành phần hệ thống hoặc môi trường mà bạn không chịu trách nhiệm.
2. Đặt giả thuyết rằng vấn đề nằm ở thành phần đó.
3. Chuyển hướng vấn đề cho đội chịu trách nhiệm về thành phần đó.
4. Khi được chứng minh là sai, quay lại bước 1.

Để tránh trở thành nạn nhân của đổ-lỗi-người-khác, hãy yêu cầu người buộc tội cung cấp ảnh chụp màn hình cho thấy công cụ nào đã được chạy và đầu ra được giải thích như thế nào.

### 2.5.4 Phương Pháp Danh Sách Kiểm Tra Ad Hoc (Ad Hoc Checklist Method)

Đi qua một danh sách kiểm tra có sẵn là phương pháp luận phổ biến được sử dụng bởi chuyên gia hỗ trợ khi được yêu cầu kiểm tra và tinh chỉnh hệ thống, thường trong khoảng thời gian ngắn. Mặc dù các danh sách kiểm tra này có thể cung cấp giá trị nhiều nhất trong khoảng thời gian ngắn nhất, chúng là khuyến nghị tại thời điểm và cần được làm mới thường xuyên để cập nhật.

### 2.5.5 Mô Tả Vấn Đề (Problem Statement)

Định nghĩa mô tả vấn đề là nhiệm vụ thường xuyên cho nhân viên hỗ trợ khi lần đầu phản hồi các sự cố. Nó được thực hiện bằng cách hỏi khách hàng các câu hỏi sau:

1. Điều gì khiến bạn nghĩ rằng có vấn đề hiệu năng?
2. Hệ thống này đã bao giờ hoạt động tốt chưa?
3. Gần đây có gì thay đổi? Phần mềm? Phần cứng? Tải?
4. Vấn đề có thể được biểu thị dưới dạng độ trễ hoặc thời gian chạy không?
5. Vấn đề có ảnh hưởng đến người hoặc ứng dụng khác không (hay chỉ bạn)?
6. Môi trường là gì? Phần mềm và phần cứng nào được sử dụng? Phiên bản? Cấu hình?

Chỉ việc hỏi và trả lời các câu hỏi này thường chỉ ra nguyên nhân và giải pháp ngay lập tức. Mô tả vấn đề do đó được đưa vào đây như phương pháp luận riêng và nên là cách tiếp cận đầu tiên bạn sử dụng khi xử lý vấn đề mới.

### 2.5.6 Phương Pháp Khoa Học (Scientific Method)

Phương pháp khoa học nghiên cứu cái chưa biết bằng cách đưa ra giả thuyết và sau đó kiểm tra chúng. Tóm tắt bằng các bước:

1. Câu hỏi
2. Giả thuyết
3. Dự đoán
4. Kiểm tra
5. Phân tích

Câu hỏi là mô tả vấn đề hiệu năng. Từ đây bạn có thể đặt giả thuyết về nguyên nhân có thể gây ra hiệu năng kém. Sau đó bạn xây dựng một kiểm tra, có thể quan sát hoặc thực nghiệm, kiểm tra dự đoán dựa trên giả thuyết. Bạn kết thúc với phân tích dữ liệu kiểm tra thu thập được.

**Ví dụ (Quan sát)**:
1. Câu hỏi: Điều gì gây ra truy vấn cơ sở dữ liệu chậm?
2. Giả thuyết: Neighbor ồn ào (tenant đám mây khác) đang thực hiện I/O đĩa, tranh chấp với I/O đĩa cơ sở dữ liệu.
3. Dự đoán: Nếu đo độ trễ I/O hệ thống file trong truy vấn, nó sẽ cho thấy hệ thống file chịu trách nhiệm cho truy vấn chậm.
4. Kiểm tra: Tracing độ trễ hệ thống file cơ sở dữ liệu cho thấy ít hơn 5% thời gian được dành cho hệ thống file.
5. Phân tích: Hệ thống file và đĩa không chịu trách nhiệm cho truy vấn chậm.

**Ví dụ (Thực nghiệm)**:
1. Câu hỏi: Tại sao yêu cầu HTTP từ host A đến host C lâu hơn từ host B đến host C?
2. Giả thuyết: Host A và host B ở các trung tâm dữ liệu khác nhau.
3. Dự đoán: Di chuyển host A đến cùng trung tâm dữ liệu với host B sẽ sửa vấn đề.
4. Kiểm tra: Di chuyển host A và đo hiệu năng.
5. Phân tích: Hiệu năng đã được sửa — nhất quán với giả thuyết.

### 2.5.7 Chu Kỳ Chẩn Đoán (Diagnosis Cycle)

Tương tự phương pháp khoa học là chu kỳ chẩn đoán:

```
giả thuyết → đo lường → dữ liệu → giả thuyết
```

Chu kỳ nhấn mạnh rằng dữ liệu có thể dẫn nhanh đến giả thuyết mới, được kiểm tra và tinh chỉnh, v.v. Tương tự như bác sĩ thực hiện chuỗi kiểm tra nhỏ để chẩn đoán bệnh nhân.

### 2.5.8 Phương Pháp Công Cụ (Tools Method)

Cách tiếp cận hướng công cụ như sau:

1. Liệt kê các công cụ hiệu năng có sẵn (tùy chọn, cài đặt hoặc mua thêm).
2. Cho mỗi công cụ, liệt kê các chỉ số hữu ích mà nó cung cấp.
3. Cho mỗi chỉ số, liệt kê các cách giải thích có thể.

Kết quả là danh sách kiểm tra mô tả công cụ nào cần chạy, chỉ số nào cần đọc, và cách giải thích chúng. Mặc dù khá hiệu quả, nó dựa hoàn toàn vào các công cụ có sẵn (hoặc đã biết), có thể cung cấp cái nhìn không đầy đủ, tương tự anti-method đèn đường.

### 2.5.9 Phương Pháp USE (The USE Method)

Phương pháp sử dụng, bão hòa và lỗi (USE - Utilization, Saturation, and Errors) nên được sử dụng sớm trong cuộc điều tra hiệu năng để xác định các nút thắt cổ chai hệ thống [Gregg 13b]. Đây là phương pháp luận tập trung vào tài nguyên hệ thống và có thể được tóm tắt:

> **Cho mỗi tài nguyên, kiểm tra mức sử dụng, bão hòa và lỗi.**

Các thuật ngữ được định nghĩa:
- **Tài nguyên** (Resources): Tất cả các thành phần chức năng máy chủ vật lý (CPU, bus, ...). Một số tài nguyên phần mềm cũng có thể được kiểm tra.
- **Mức sử dụng** (Utilization): Trong khoảng thời gian nhất định, phần trăm thời gian tài nguyên bận phục vụ công việc.
- **Bão hòa** (Saturation): Mức độ tài nguyên có công việc thêm mà nó không thể phục vụ, thường chờ trong hàng đợi. Thuật ngữ khác là áp lực (pressure).
- **Lỗi** (Errors): Số lượng sự kiện lỗi.

Lỗi nên được điều tra vì chúng có thể làm suy giảm hiệu năng nhưng có thể không được nhận thấy ngay lập tức khi chế độ thất bại có thể phục hồi.

**Quy trình**: Phương pháp USE được minh họa như lưu đồ trong Hình 2.12. Lỗi được kiểm tra trước vì thường nhanh để giải thích. Bão hòa được kiểm tra thứ hai vì nhanh hơn để giải thích so với mức sử dụng: bất kỳ mức bão hòa nào cũng có thể là vấn đề.

*Hình 2.12: Lưu đồ phương pháp USE*

**Biểu thị chỉ số**:
- **Mức sử dụng**: Phần trăm trong khoảng thời gian (ví dụ: "Một CPU đang chạy ở 90% sử dụng")
- **Bão hòa**: Độ dài hàng đợi chờ (ví dụ: "CPU có độ dài hàng đợi chạy trung bình là bốn")
- **Lỗi**: Số lỗi được báo cáo (ví dụ: "Ổ đĩa này đã có 50 lỗi")

**Danh sách tài nguyên**: Bước đầu tiên trong phương pháp USE là tạo danh sách tài nguyên. Hãy cố gắng đầy đủ nhất có thể:
- **CPU**: Socket, lõi, luồng phần cứng (CPU ảo)
- **Bộ nhớ chính**: DRAM
- **Giao diện mạng**: Cổng Ethernet, Infiniband
- **Thiết bị lưu trữ**: Đĩa, bộ điều hợp lưu trữ
- **Bộ tăng tốc**: GPU, TPU, FPGA, v.v.
- **Bộ điều khiển**: Lưu trữ, mạng
- **Interconnect**: CPU, bộ nhớ, I/O

**Bảng 2.6: Ví dụ chỉ số phương pháp USE**

| Tài nguyên | Loại | Chỉ số |
|-----------|------|--------|
| CPU | Mức sử dụng | Mức sử dụng CPU (từng CPU hoặc trung bình toàn hệ thống) |
| CPU | Bão hòa | Độ dài hàng đợi chạy, độ trễ bộ lập lịch, áp lực CPU (Linux PSI) |
| Bộ nhớ | Mức sử dụng | Bộ nhớ trống khả dụng (toàn hệ thống) |
| Bộ nhớ | Bão hòa | Swapping (anonymous paging), quét trang, sự kiện out-of-memory, áp lực bộ nhớ (Linux PSI) |
| Giao diện mạng | Mức sử dụng | Thông lượng nhận/băng thông tối đa, thông lượng gửi/băng thông tối đa |
| I/O thiết bị lưu trữ | Mức sử dụng | Phần trăm bận thiết bị |
| I/O thiết bị lưu trữ | Bão hòa | Độ dài hàng đợi chờ, áp lực I/O (Linux PSI) |
| I/O thiết bị lưu trữ | Lỗi | Lỗi thiết bị ("soft," "hard") |

**Gợi ý giải thích**:
- **Mức sử dụng**: 100% thường là dấu hiệu nút thắt cổ chai. Vượt 60% có thể là vấn đề vì có thể ẩn các đợt ngắn 100%.
- **Bão hòa**: Bất kỳ mức nào (khác không) đều có thể là vấn đề.
- **Lỗi**: Bộ đếm lỗi khác không đáng điều tra, đặc biệt nếu tăng khi hiệu năng kém.

**Tài nguyên phần mềm**: Một số tài nguyên phần mềm có thể được kiểm tra tương tự:
- **Mutex lock**: Mức sử dụng là thời gian khóa được giữ, bão hòa là các luồng xếp hàng chờ.
- **Thread pool**: Mức sử dụng là thời gian luồng bận xử lý công việc, bão hòa là số yêu cầu chờ.
- **Dung lượng tiến trình/luồng**: Hệ thống có thể có số lượng giới hạn tiến trình hoặc luồng.
- **Dung lượng file descriptor**: Tương tự dung lượng tiến trình/luồng.

### 2.5.10 Phương Pháp RED (The RED Method)

Trọng tâm của phương pháp luận này là dịch vụ, điển hình là dịch vụ đám mây trong kiến trúc microservice. Nó xác định ba chỉ số để giám sát sức khỏe từ góc nhìn người dùng [Wilkie 18]:

> **Cho mỗi dịch vụ, kiểm tra tỷ lệ yêu cầu, lỗi và thời lượng.**

Các chỉ số:
- **Request rate** (Tỷ lệ yêu cầu): Số yêu cầu dịch vụ mỗi giây
- **Errors** (Lỗi): Số yêu cầu thất bại
- **Duration** (Thời lượng): Thời gian để yêu cầu hoàn thành

Phương pháp RED được tạo bởi Tom Wilkie. Các phương pháp luận này bổ sung cho nhau: phương pháp USE cho sức khỏe máy, và phương pháp RED cho sức khỏe người dùng.

### 2.5.11 Đặc Trưng Hóa Khối Lượng Công Việc (Workload Characterization)

Đặc trưng hóa khối lượng công việc là phương pháp đơn giản và hiệu quả để xác định một lớp vấn đề: những vấn đề do tải áp dụng. Nó tập trung vào đầu vào cho hệ thống, thay vì hiệu năng kết quả.

Khối lượng công việc có thể được đặc trưng bằng cách trả lời:

- **Ai** đang gây ra tải? PID, user ID, IP từ xa?
- **Tại sao** tải đang được gọi? Đường dẫn mã, stack trace?
- **Đặc điểm tải** là gì? IOPS, thông lượng, hướng (đọc/ghi), loại? Bao gồm phương sai.
- **Tải thay đổi theo thời gian** như thế nào? Có mẫu hàng ngày không?

Các chiến thắng hiệu năng tốt nhất là kết quả của việc loại bỏ công việc không cần thiết.

### 2.5.12 Phân Tích Đào Sâu (Drill-Down Analysis)

Phân tích đào sâu bắt đầu bằng kiểm tra vấn đề ở cấp độ cao, sau đó thu hẹp trọng tâm dựa trên kết quả trước đó, loại bỏ những khu vực không thú vị, và đào sâu hơn vào những khu vực thú vị.

Phương pháp luận phân tích đào sâu ba giai đoạn:

1. **Giám sát (Monitoring)**: Được sử dụng để ghi liên tục thống kê cấp cao theo thời gian, và xác định hoặc cảnh báo nếu vấn đề có thể xuất hiện.
2. **Nhận dạng (Identification)**: Cho một vấn đề nghi ngờ, thu hẹp cuộc điều tra đến tài nguyên hoặc khu vực cụ thể, xác định nút thắt cổ chai có thể.
3. **Phân tích (Analysis)**: Kiểm tra thêm các khu vực hệ thống cụ thể để cố gắng tìm nguyên nhân gốc rễ và định lượng vấn đề.

### 2.5.13 Phân Tích Độ Trễ (Latency Analysis)

Phân tích độ trễ kiểm tra thời gian để hoàn thành một thao tác và sau đó chia nó thành các thành phần nhỏ hơn, tiếp tục chia nhỏ các thành phần có độ trễ cao nhất để có thể xác định và định lượng nguyên nhân gốc rễ. Tương tự phân tích đào sâu, phân tích độ trễ có thể đào sâu qua các lớp ngăn xếp phần mềm để tìm nguồn gốc vấn đề độ trễ.

Ví dụ, phân tích độ trễ truy vấn MySQL:

1. Có vấn đề độ trễ truy vấn không? (có)
2. Thời gian truy vấn chủ yếu dành trên CPU hay chờ ngoài CPU (off-CPU)? (off-CPU)
3. Thời gian off-CPU đang chờ gì? (I/O hệ thống file)
4. Thời gian I/O hệ thống file do I/O đĩa hay tranh chấp khóa? (I/O đĩa)
5. Thời gian I/O đĩa chủ yếu là xếp hàng hay đang phục vụ I/O? (đang phục vụ)
6. Thời gian phục vụ đĩa chủ yếu là khởi tạo I/O hay truyền dữ liệu? (truyền dữ liệu)

Mỗi bước đặt ra câu hỏi chia độ trễ thành hai phần và sau đó phân tích phần lớn hơn: tìm kiếm nhị phân của độ trễ.

*Hình 2.14: Quy trình phân tích độ trễ*

### 2.5.14 Method R

Method R là phương pháp luận phân tích hiệu năng được phát triển cho cơ sở dữ liệu Oracle, tập trung vào tìm nguồn gốc độ trễ dựa trên các sự kiện trace Oracle [Millsap 03]. Nó được mô tả là "phương pháp cải thiện hiệu năng dựa trên thời gian phản hồi mang lại giá trị kinh tế tối đa cho doanh nghiệp."

### 2.5.15 Tracing Sự Kiện (Event Tracing)

Hệ thống hoạt động bằng cách xử lý các sự kiện rời rạc. Chúng bao gồm lệnh CPU, I/O đĩa, gói tin mạng, system call, lời gọi thư viện, giao dịch ứng dụng, truy vấn cơ sở dữ liệu, v.v. Phân tích hiệu năng thường nghiên cứu tóm tắt các sự kiện này, nhưng đôi khi chi tiết quan trọng bị mất trong tóm tắt và các sự kiện được hiểu tốt nhất khi kiểm tra riêng lẻ.

Ví dụ tcpdump(8) cho gói tin mạng:

```
# tcpdump -ni eth4 -ttt
00:00:00.000000 IP 10.2.203.2.22 > 10.2.0.2.33986: Flags [P.], seq ...
00:00:00.000392 IP 10.2.0.2.33986 > 10.2.203.2.22: Flags [.], ack 192, ...
[...]
```

Ví dụ biosnoop(8) cho I/O thiết bị lưu trữ:

```
# biosnoop
TIME(s)     COMM          PID    DISK    T SECTOR      BYTES   LAT(ms)
0.000004    supervise     1950   xvda1   W 13092560    4096    0.74
0.000178    supervise     1950   xvda1   W 13092432    4096    0.61
[...]
```

Khi thực hiện tracing sự kiện, tìm kiếm:
- **Đầu vào**: Tất cả thuộc tính yêu cầu sự kiện: loại, hướng, kích thước, v.v.
- **Thời gian**: Thời gian bắt đầu, kết thúc, độ trễ (chênh lệch)
- **Kết quả**: Trạng thái lỗi, kết quả sự kiện

### 2.5.16 Thống Kê Cơ Sở (Baseline Statistics)

Các môi trường thường sử dụng giải pháp giám sát để ghi chỉ số hiệu năng máy chủ và trực quan hóa chúng dưới dạng biểu đồ đường. Tuy nhiên, có nhiều chỉ số và chi tiết hệ thống khả dụng trên dòng lệnh mà có thể không được giám sát.

Giải pháp là thu thập thống kê cơ sở (baseline statistics). Điều này bao gồm thu thập tất cả chỉ số hệ thống khi hệ thống ở tải "bình thường" và ghi lại chúng trong file văn bản hoặc cơ sở dữ liệu để tham khảo sau này. Các baseline có thể được thu thập theo khoảng thời gian đều đặn (hàng ngày), cũng như trước và sau thay đổi hệ thống hoặc ứng dụng.

### 2.5.17 Tinh Chỉnh Hiệu Năng Tĩnh (Static Performance Tuning)

Tinh chỉnh hiệu năng tĩnh tập trung vào vấn đề của kiến trúc được cấu hình. Phân tích hiệu năng tĩnh có thể được thực hiện khi hệ thống nghỉ và không có tải.

Kiểm tra các câu hỏi:
- Thành phần có hợp lý không? (lỗi thời, thiếu năng lực, v.v.)
- Cấu hình có hợp lý cho khối lượng công việc dự kiến không?
- Thành phần có được tự động cấu hình ở trạng thái tốt nhất không?
- Thành phần có gặp lỗi khiến nó ở trạng thái suy giảm không?

Ví dụ vấn đề: đàm phán giao diện mạng chọn 1 Gbit/s thay vì 10 Gbit/s; đĩa hỏng trong pool RAID; phiên bản cũ; hệ thống file gần đầy; chế độ debug vô tình bật.

### 2.5.18 Tinh Chỉnh Cache (Cache Tuning)

Chiến lược chung cho tinh chỉnh từng cấp cache:

1. Nhắm đến cache càng cao trong ngăn xếp càng tốt, gần nơi công việc được thực hiện.
2. Kiểm tra cache đã được bật và hoạt động.
3. Kiểm tra tỷ lệ hit/miss và tốc độ miss.
4. Nếu kích thước cache động, kiểm tra kích thước hiện tại.
5. Tinh chỉnh cache cho khối lượng công việc.
6. Tinh chỉnh khối lượng công việc cho cache.

Cẩn thận với double caching — hai cache khác nhau cùng cache dữ liệu giống nhau.

### 2.5.19 Micro-Benchmarking

Micro-benchmarking kiểm tra hiệu năng của khối lượng công việc đơn giản và nhân tạo. Điều này khác với macro-benchmarking (hoặc benchmarking ngành), thường nhắm đến kiểm tra khối lượng công việc thực tế và tự nhiên.

Ví dụ mục tiêu:
- **Thời gian syscall**: Cho fork(2), execve(2), open(2), read(2), close(2)
- **Đọc hệ thống file**: Từ file đã cache, thay đổi kích thước đọc từ 1 byte đến 1 Mbyte
- **Thông lượng mạng**: Truyền dữ liệu giữa endpoint TCP, với kích thước bộ đệm socket khác nhau

### 2.5.20 Phương Châm Hiệu Năng (Performance Mantras)

Đây là phương pháp luận tinh chỉnh cho thấy cách cải thiện hiệu năng tốt nhất, liệt kê các hành động từ hiệu quả nhất đến ít hiệu quả nhất:

1. **Đừng làm.** Loại bỏ công việc không cần thiết.
2. **Làm, nhưng đừng làm lại.** Caching.
3. **Làm ít hơn.** Tinh chỉnh tần suất refresh, polling hoặc cập nhật.
4. **Làm sau.** Write-back caching.
5. **Làm khi họ không nhìn.** Lập lịch công việc chạy ngoài giờ cao điểm.
6. **Làm đồng thời.** Chuyển từ đơn luồng sang đa luồng.
7. **Làm rẻ hơn.** Mua phần cứng nhanh hơn.

## 2.6 Mô Hình Hóa (Modeling)

Mô hình hóa phân tích của hệ thống có thể được sử dụng cho nhiều mục đích, đặc biệt là phân tích khả năng mở rộng: nghiên cứu cách hiệu năng mở rộng khi tải hoặc tài nguyên tăng.

Mô hình hóa phân tích có thể được coi là loại hoạt động đánh giá hiệu năng thứ ba, cùng với khả năng quan sát hệ thống sản xuất ("đo lường") và kiểm tra thực nghiệm ("mô phỏng") [Jain 91]. Hiệu năng được hiểu tốt nhất khi ít nhất hai trong số các hoạt động này được thực hiện.

### 2.6.1 Doanh Nghiệp so với Đám Mây (Enterprise vs. Cloud)

Với điện toán đám mây, các môi trường ở bất kỳ quy mô nào có thể được thuê trong thời gian ngắn. Thay vì tạo mô hình toán học để dự đoán hiệu năng, khối lượng công việc có thể được đặc trưng hóa, mô phỏng, và sau đó kiểm tra trên đám mây ở các quy mô khác nhau.

### 2.6.2 Nhận Dạng Trực Quan (Visual Identification)

Có nhiều hồ sơ khả năng mở rộng có thể tìm kiếm:
- **Khả năng mở rộng tuyến tính**: Hiệu năng tăng tỷ lệ thuận khi tài nguyên được mở rộng.
- **Tranh chấp** (Contention): Một số thành phần kiến trúc được chia sẻ và chỉ có thể sử dụng tuần tự.
- **Tính nhất quán** (Coherence): Chi phí duy trì tính nhất quán dữ liệu bắt đầu lớn hơn lợi ích mở rộng.
- **Điểm gối** (Knee point): Một yếu tố gặp phải thay đổi hồ sơ khả năng mở rộng.
- **Trần khả năng mở rộng** (Scalability ceiling): Giới hạn cứng đạt được.

### 2.6.3 Định Luật Mở Rộng Amdahl (Amdahl's Law of Scalability)

Định luật này mô hình hóa khả năng mở rộng hệ thống, tính đến các thành phần tuần tự của khối lượng công việc không mở rộng song song:

```
C(N) = N/(1 + α(N – 1))
```

Trong đó C(N) là dung lượng tương đối, N là chiều mở rộng (như số CPU), và α biểu thị mức tuần tự.

### 2.6.4 Định Luật Mở Rộng Phổ Quát (Universal Scalability Law)

USL được phát triển bởi Tiến sĩ Neil Gunther, bao gồm thêm tham số cho độ trễ nhất quán:

```
C(N) = N/(1 + α(N – 1) + βN(N – 1))
```

Khi β == 0, điều này trở thành Định luật Amdahl.

### 2.6.5 Lý Thuyết Hàng Đợi (Queueing Theory)

Lý thuyết hàng đợi là nghiên cứu toán học của các hệ thống có hàng đợi, cung cấp cách phân tích độ dài hàng đợi, thời gian chờ (độ trễ) và mức sử dụng (dựa trên thời gian).

**Định luật Little**: `L = λW`, xác định số yêu cầu trung bình trong hệ thống, L, bằng tốc độ đến trung bình, λ, nhân với thời gian yêu cầu trung bình trong hệ thống, W.

**Ký hiệu Kendall**: Dạng A/S/m — quá trình đến (A), phân phối thời gian phục vụ (S), và số trung tâm phục vụ (m).

Ví dụ: M/M/1, M/M/c, M/G/1, M/D/1.

**M/D/1 và 60% Sử dụng**: Thời gian phản hồi cho M/D/1:

```
r = s(2 - ρ)/2(1 - ρ)
```

Trong đó r = thời gian phản hồi, s = thời gian phục vụ, ρ = mức sử dụng.

Vượt 60% sử dụng, thời gian phản hồi trung bình tăng gấp đôi. Đến 80%, nó tăng gấp ba. Đây là lý do mức sử dụng đĩa có thể trở thành vấn đề rất trước khi đạt 100%.

## 2.7 Hoạch Định Dung Lượng (Capacity Planning)

Hoạch định dung lượng kiểm tra hệ thống xử lý tải tốt như thế nào và cách nó mở rộng khi tải mở rộng.

### 2.7.1 Giới Hạn Tài Nguyên (Resource Limits)

Phương pháp này tìm kiếm tài nguyên sẽ trở thành nút thắt cổ chai dưới tải:

1. Đo tốc độ yêu cầu máy chủ và giám sát theo thời gian.
2. Đo sử dụng tài nguyên phần cứng và phần mềm. Giám sát theo thời gian.
3. Biểu thị yêu cầu máy chủ theo tài nguyên sử dụng.
4. Ngoại suy yêu cầu đến giới hạn đã biết cho mỗi tài nguyên.

Ví dụ: Hệ thống hiện tại 1.000 yêu cầu/giây, 16 CPU ở 40% sử dụng:

```
CPU% mỗi yêu cầu = 16 × 40%/1.000 = 0.64%
Yêu cầu tối đa/giây = 1.600/0.64 = 2.500 yêu cầu/giây
```

### 2.7.2 Phân Tích Yếu Tố (Factor Analysis)

Khi mua và triển khai hệ thống mới, có nhiều yếu tố có thể thay đổi. Cách tiếp cận dựa trên cấu hình tối đa:

1. Kiểm tra hiệu năng với tất cả yếu tố ở mức tối đa.
2. Thay đổi từng yếu tố một, kiểm tra hiệu năng.
3. Gán phần trăm giảm hiệu năng cho mỗi yếu tố cùng với tiết kiệm chi phí.
4. Chọn yếu tố để tiết kiệm chi phí đồng thời duy trì yêu cầu hiệu năng.
5. Kiểm tra lại cấu hình đã tính.

### 2.7.3 Giải Pháp Mở Rộng (Scaling Solutions)

- **Mở rộng dọc** (Vertical scaling): Hệ thống lớn hơn.
- **Mở rộng ngang** (Horizontal scaling): Phân tải qua nhiều hệ thống, thường qua load balancer.
- **Auto Scaling Group (ASG)**: Tự động tăng/giảm số instance dựa trên chỉ số sử dụng.
- **Sharding**: Cho cơ sở dữ liệu, dữ liệu được chia thành các phần logic, mỗi phần quản lý bởi cơ sở dữ liệu riêng.

## 2.8 Thống Kê (Statistics)

### 2.8.1 Định Lượng Cải Thiện Hiệu Năng (Quantifying Performance Gains)

**Dựa trên Quan sát**: Chọn chỉ số đáng tin cậy, ước tính cải thiện hiệu năng từ việc giải quyết vấn đề.

**Dựa trên Thực nghiệm**: Áp dụng bản sửa, định lượng trước so với sau bằng chỉ số đáng tin cậy.

### 2.8.2 Trung Bình (Averages)

- **Trung bình số học** (Arithmetic mean): Tổng chia cho số lượng.
- **Trung bình hình học** (Geometric mean): Căn bậc n của tích các giá trị. Phù hợp cho hiệu ứng "nhân".
- **Trung bình điều hòa** (Harmonic mean): Số lượng chia cho tổng nghịch đảo. Phù hợp cho trung bình tốc độ.
- **Trung bình suy giảm** (Decayed average): Thời gian gần đây được ưu tiên hơn thời gian xa hơn.

**Hạn chế**: Trung bình là thống kê tóm tắt che giấu chi tiết. Tôi đã phân tích nhiều trường hợp I/O đĩa đôi khi vượt 100 ms, trong khi trung bình gần 1 ms.

### 2.8.3 Độ Lệch Chuẩn, Phân Vị, Trung Vị (Standard Deviation, Percentiles, Median)

Độ lệch chuẩn là thước đo phương sai. Phân vị 90th, 95th, 99th, 99.9th được sử dụng trong giám sát hiệu năng để định lượng yêu cầu chậm nhất.

Phân vị 50th, gọi là **trung vị** (median), cho thấy phần lớn dữ liệu ở đâu.

### 2.8.4 Hệ Số Biến Thiên (Coefficient of Variation)

Tỷ lệ của độ lệch chuẩn với trung bình, gọi là hệ số biến thiên (CoV hoặc CV). CV thấp hơn nghĩa là ít biến thiên hơn.

### 2.8.5 Phân Phối Đa Đỉnh (Multimodal Distributions)

Hiệu năng hệ thống thường đa đỉnh (bimodal), trả về độ trễ thấp cho đường dẫn mã nhanh và độ trễ cao cho đường dẫn chậm, hoặc độ trễ thấp cho cache hit và độ trễ cao cho cache miss.

Mỗi khi bạn thấy trung bình được sử dụng làm chỉ số hiệu năng, đặc biệt là trung bình độ trễ, hãy hỏi: Phân phối là gì?

### 2.8.6 Giá Trị Ngoại Lai (Outliers)

Số lượng rất nhỏ các giá trị cực cao hoặc cực thấp không phù hợp với phân phối dự kiến. Ví dụ: I/O đĩa đôi khi vượt 1.000 ms trong khi phần lớn từ 0 đến 10 ms.

Để hiểu tốt hơn phân phối đa đỉnh, giá trị ngoại lai và các hành vi phức tạp khác, hãy kiểm tra toàn bộ phân phối, ví dụ bằng histogram.

## 2.9 Giám Sát (Monitoring)

Giám sát hiệu năng hệ thống ghi thống kê hiệu năng theo thời gian (chuỗi thời gian) để quá khứ có thể so sánh với hiện tại và các mẫu sử dụng dựa trên thời gian có thể được xác định.

### 2.9.1 Mẫu Dựa Trên Thời Gian (Time-Based Patterns)

Các chu kỳ hành vi phổ biến:
- **Hàng giờ**: Giám sát và báo cáo.
- **Hàng ngày**: Mẫu sử dụng trùng với giờ làm việc (9h–17h).
- **Hàng tuần**: Mẫu ngày làm việc và cuối tuần.
- **Hàng quý**: Báo cáo tài chính.
- **Hàng năm**: Mẫu do lịch trường và kỳ nghỉ.

### 2.9.2 Sản Phẩm Giám Sát (Monitoring Products)

Có nhiều sản phẩm bên thứ ba cho giám sát hiệu năng hệ thống. Ví dụ: đám mây Netflix gồm hơn 200.000 instance và được giám sát bằng công cụ Atlas [Harrington 14].

### 2.9.3 Tóm Tắt Từ Khi Khởi Động (Summary-Since-Boot)

Nếu giám sát chưa được thực hiện, kiểm tra xem ít nhất giá trị tóm tắt từ khi khởi động có sẵn từ hệ điều hành không.

## 2.10 Trực Quan Hóa (Visualizations)

Trực quan hóa cho phép kiểm tra nhiều dữ liệu hơn so với dạng văn bản. Chúng cũng hỗ trợ nhận dạng mẫu và so khớp mẫu.

### 2.10.1 Biểu Đồ Đường (Line Chart)

Biểu đồ đường thường dùng để kiểm tra chỉ số hiệu năng theo thời gian, với trục x là thời gian. Nhiều đường có thể được vẽ, bao gồm trung vị, trung bình, độ lệch chuẩn và phân vị.

### 2.10.2 Biểu Đồ Phân Tán (Scatter Plots)

Biểu đồ phân tán cho phép xem tất cả dữ liệu. Mỗi sự kiện được vẽ dưới dạng điểm. Cho phép xác định giá trị ngoại lai một cách trực tiếp.

### 2.10.3 Bản Đồ Nhiệt (Heat Maps)

Bản đồ nhiệt giải quyết vấn đề khả năng mở rộng của biểu đồ phân tán bằng cách lượng tử hóa các phạm vi x và y thành nhóm gọi là bucket. Chúng được hiển thị dưới dạng pixel lớn, tô màu dựa trên số sự kiện trong phạm vi đó.

### 2.10.4 Biểu Đồ Dòng Thời Gian (Timeline Charts)

Biểu đồ dòng thời gian hiển thị tập hợp hoạt động dưới dạng thanh trên dòng thời gian. Thường dùng cho phân tích hiệu năng front-end (trình duyệt web), cũng gọi là waterfall chart.

### 2.10.5 Biểu Đồ Bề Mặt (Surface Plot)

Biểu diễn ba chiều, thường được render dưới dạng wireframe model. Hoạt động tốt nhất khi giá trị chiều thứ ba không thay đổi đáng kể.

### 2.10.6 Công Cụ Trực Quan Hóa (Visualization Tools)

Các công cụ trực quan hóa hiện đại cung cấp xem thời gian thực về hiệu năng hệ thống, truy cập từ trình duyệt và thiết bị di động.

## 2.11 Bài Tập (Exercises)

1. Trả lời các câu hỏi về thuật ngữ hiệu năng chính: IOPS là gì? Mức sử dụng là gì? Bão hòa là gì? Độ trễ là gì? Micro-benchmarking là gì?

2. Chọn năm phương pháp luận để sử dụng cho môi trường của bạn. Chọn thứ tự và giải thích lý do.

3. Tóm tắt các vấn đề khi sử dụng trung bình độ trễ là chỉ số hiệu năng duy nhất. Có thể giải quyết bằng phân vị 99th không?

## 2.12 Tài Liệu Tham Khảo (References)

- [Amdahl 67] Amdahl, G., "Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities," AFIPS, 1967.

- [Jain 91] Jain, R., The Art of Computer Systems Performance Analysis: Techniques for Experimental Design, Measurement, Simulation and Modeling, Wiley, 1991.

- [Cockcroft 95] Cockcroft, A., Sun Performance and Tuning, Prentice Hall, 1995.

- [Gunther 97] Gunther, N., The Practical Performance Analyst, McGraw-Hill, 1997.

- [Wong 97] Wong, B., Configuration and Capacity Planning for Solaris Servers, Prentice Hall, 1997.

- [Elling 00] Elling, R., "Static Performance Tuning," Sun Blueprints, 2000.

- [Millsap 03] Millsap, C., and J. Holt., Optimizing Oracle Performance, O'Reilly, 2003.

- [McDougall 06a] McDougall, R., Mauro, J., and Gregg, B., Solaris Performance and Tools: DTrace and MDB Techniques for Solaris 10 and OpenSolaris, Prentice Hall, 2006.

- [Gunther 07] Gunther, N., Guerrilla Capacity Planning, Springer, 2007.

- [Allspaw 08] Allspaw, J., The Art of Capacity Planning, O'Reilly, 2008.

- [Gregg 10a] Gregg, B., "Visualizing System Latency," Communications of the ACM, July 2010.

- [Gregg 10b] Gregg, B., "Visualizations for Performance Analysis (and More)," USENIX LISA, 2010.

- [Gregg 11b] Gregg, B., "Utilization Heat Maps," http://www.brendangregg.com/HeatMaps/utilization.html, 2011.

- [Williams 11] Williams, C., "The $300m Cable That Will Save Traders Milliseconds," The Telegraph, 2011.

- [Gregg 13b] Gregg, B., "Thinking Methodically about Performance," Communications of the ACM, February 2013.

- [Gregg 14a] Gregg, B., "Performance Scalability Models," https://github.com/brendangregg/PerfModels, 2014.

- [Harrington 14] Harrington, B., and Rapoport, R., "Introducing Atlas: Netflix's Primary Telemetry Platform," Netflix Technology Blog, 2014.

- [Gregg 15b] Gregg, B., "Heatmaps," http://www.brendangregg.com/heatmaps.html, 2015.

- [Wilkie 18] Wilkie, T., "The RED Method: Patterns for Instrumentation & Monitoring," Grafana Labs, 2018.

- [Eclipse 20] Eclipse Foundation, "Trace Compass," https://www.eclipse.org/tracecompass, accessed 2020.

- [Wikipedia 20] Wikipedia, "Five Whys," https://en.wikipedia.org/wiki/Five_whys, accessed 2020.

- [Grafana 20] Grafana Labs, "Heatmap," https://grafana.com/docs/grafana/latest/features/panels/heatmap, accessed 2020.

- [KernelShark 20] "KernelShark," https://www.kernelshark.org, accessed 2020.

- [Kubernetes 20a] Kubernetes, "Horizontal Pod Autoscaler," https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale, accessed 2020.

- [R Project 20] R Project, "The R Project for Statistical Computing," https://www.r-project.org, accessed 2020.
