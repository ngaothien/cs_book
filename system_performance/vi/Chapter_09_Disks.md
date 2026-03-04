# Chương 9: Các đĩa (Disks)

I/O đĩa có thể gây ra độ trễ ứng dụng đáng kể, và do đó là một mục tiêu quan trọng của phân tích hiệu năng hệ thống. Dưới mức tải cao, các đĩa trở thành một nút thắt cổ chai, để lại các CPU rảnh rỗi trong khi hệ thống chờ đợi I/O đĩa hoàn thành. Việc xác định và loại bỏ các nút thắt cổ chai này có thể cải thiện hiệu năng và thông lượng ứng dụng theo nhiều bậc độ lớn.

Thuật ngữ *disks* (các đĩa) đề cập đến các thiết bị lưu trữ sơ cấp của hệ thống. Chúng bao gồm các đĩa dựa trên bộ nhớ flash (SSDs) và các đĩa quay từ tính. SSDs được giới thiệu chủ yếu để cải thiện hiệu năng I/O đĩa, và chúng đã làm được điều đó. Tuy nhiên, nhu cầu về dung lượng, tốc độ I/O, và thông lượng cũng đang tăng lên, và các thiết bị bộ nhớ flash không miễn nhiễm với các vấn đề hiệu năng.

Các mục tiêu học tập của chương này là:
- Hiểu các mô hình và khái niệm đĩa.
- Hiểu cách thức các mẫu truy cập đĩa ảnh hưởng đến hiệu năng.
- Hiểu những nguy hiểm khi diễn giải mức sử dụng đĩa (disk utilization).
- Trở nên quen thuộc với các đặc tính và thành phần nội bộ của thiết bị đĩa.
- Trở nên quen thuộc với đường dẫn kernel từ các hệ thống tập tin tới các thiết bị.
- Hiểu các cấp độ RAID và hiệu năng của chúng.
- Tuân theo các phương pháp luận khác nhau cho phân tích hiệu năng đĩa.
- Đặc tính hóa I/O đĩa trên toàn hệ thống và theo từng tiến trình.
- Đo lường phân phối độ trễ I/O đĩa và nhận diện các giá trị ngoại lai.
- Nhận diện các ứng dụng và các đường dẫn mã yêu cầu I/O đĩa.
- Điều tra chi tiết I/O đĩa bằng các công cụ truy vết (tracers).
- Nhận biết các tham số tinh chỉnh đĩa.

Chương này bao gồm sáu phần, ba phần đầu cung cấp cơ sở cho việc phân tích I/O đĩa và ba phần cuối trình bày ứng dụng thực tế của nó cho các hệ thống dựa trên Linux. Các phần như sau:
- **Nền tảng (Background)** giới thiệu thuật ngữ liên quan đến lưu trữ, các mô hình cơ bản của thiết bị đĩa, và các khái niệm hiệu năng đĩa then chốt.
- **Kiến trúc (Architecture)** cung cấp các mô tả chung về phần cứng lưu trữ và kiến trúc phần mềm.
- **Phương pháp luận (Methodology)** mô tả các phương pháp luận phân tích hiệu năng, cả quan sát và thực nghiệm.
- **Công cụ Quan trắc (Observability Tools)** trình bày các công cụ quan sát hiệu năng đĩa cho các hệ thống dựa trên Linux, bao gồm truy vết và hình ảnh hóa.
- **Thực nghiệm (Experimentation)** tóm tắt các công cụ benchmark đĩa.
- **Tinh chỉnh (Tuning)** mô tả các tham số tinh chỉnh đĩa ví dụ.

Chương trước đã đề cập đến hiệu năng của các hệ thống tập tin được xây dựng trên các đĩa, và là một mục tiêu tốt hơn để nghiên cứu nhằm hiểu hiệu năng ứng dụng.

## 9.1 Thuật ngữ (Terminology)
Thuật ngữ liên quan đến đĩa được sử dụng trong chương này bao gồm:
- **Đĩa ảo (Virtual disk):** Một sự mô phỏng của một thiết bị lưu trữ. Nó xuất hiện đối với hệ thống như một đĩa vật lý duy nhất, nhưng nó có thể được xây dựng từ nhiều đĩa hoặc một phần của một đĩa.
- **Vận chuyển (Transport):** Bus vật lý được sử dụng cho việc liên lạc, bao gồm truyền tải dữ liệu (I/O) và các lệnh đĩa khác.
- **Cung từ (Sector):** Một khối lưu trữ trên đĩa, theo truyền thống có kích thước 512 byte, nhưng ngày nay thường là 4 Kbyte.
- **I/O:** Nói một cách chính xác, I/O chỉ bao gồm các lệnh đọc và ghi đĩa, và sẽ không bao gồm các lệnh đĩa khác. I/O có thể được mô tả bởi, ít nhất, hướng (đọc hoặc ghi), một địa chỉ đĩa (vị trí), và một kích thước (byte).
- **Các lệnh đĩa (Disk commands):** Các đĩa có thể được ra lệnh để thực hiện các lệnh không truyền tải dữ liệu khác (ví dụ: một lệnh flush bộ đệm ẩn).
- **Thông lượng (Throughput):** Với các đĩa, thông lượng thường đề cập đến tốc độ truyền dữ liệu hiện tại, được đo bằng byte mỗi giây.
- **Băng thông (Bandwidth):** Đây là tốc độ truyền dữ liệu tối đa có thể cho các phương thức vận chuyển hoặc bộ điều khiển lưu trữ; nó bị giới hạn bởi phần cứng.
- **Độ trễ I/O (I/O latency):** Thời gian cho một thao tác I/O từ lúc bắt đầu đến khi kết thúc. Mục 9.3.1, Đo lường thời gian, định nghĩa thuật ngữ thời gian chính xác hơn. Hãy lưu ý rằng lĩnh vực mạng sử dụng thuật ngữ *latency* để đề cập đến thời gian cần thiết để khởi tạo một I/O, sau đó là thời gian truyền dữ liệu.
- **Giá trị ngoại lai độ trễ (Latency outliers):** I/O đĩa với độ trễ cao bất thường.

Các thuật ngữ khác được giới thiệu xuyên suốt chương này. Bảng thuật ngữ (Glossary) bao gồm thuật ngữ cơ bản để tham khảo, bao gồm *disk*, *disk controller*, *storage array*, *local disks*, *remote disks*, và *IOPS*. Đồng thời xem các phần thuật ngữ trong Chương 2 và 3.

## 9.2 Mô hình (Models)
Các mô hình đơn giản sau đây minh họa một số nguyên tắc cơ bản của hiệu năng I/O đĩa.

### 9.2.1 Đĩa đơn giản (Simple Disk)
Các đĩa hiện đại bao gồm một hàng đợi trên đĩa cho các yêu cầu I/O, như được mô tả trong Hình 9.1.

(Hình 9.1 Đĩa đơn giản với hàng đợi)

I/O được chấp nhận bởi đĩa có thể đang chờ trong hàng đợi hoặc đang được phục vụ. Mô hình đơn giản này tương tự như một quầy thanh toán tại cửa hàng tạp hóa, nơi khách hàng xếp hàng để được phục vụ. Nó cũng phù hợp cho việc phân tích sử dụng lý thuyết xếp hàng (queueing theory).

Trong khi điều này có thể ám ý một hàng đợi đến-trước-được-phục-vụ-trước, bộ điều khiển trên đĩa có thể áp dụng các thuật toán khác để tối ưu hóa hiệu năng. Các thuật toán này có thể bao gồm tìm kiếm thang máy (elevator seeking) cho I/O đĩa quay (xem thảo luận trong Mục 9.4.1, Các loại đĩa), hoặc các hàng đợi riêng biệt cho các yêu cầu đọc và ghi (đặc biệt đối với các đĩa dựa trên bộ nhớ flash).

### 9.2.2 Đĩa có bộ đệm ẩn (Caching Disk)
Việc bổ sung một bộ đệm ẩn trên đĩa cho phép một số yêu cầu đọc được đáp ứng từ một loại bộ nhớ nhanh hơn, như được trình bày trong Hình 9.2. Điều này có thể được triển khai dưới dạng một lượng nhỏ bộ nhớ (DRAM) chứa bên trong thiết bị đĩa vật lý.

Trong khi các lần trúng bộ đệm ẩn trả về với độ trễ rất thấp (tốt), các lần trượt bộ đệm ẩn vẫn thường xuyên, trả về với độ trễ đĩa cao.

Bộ đệm ẩn trên đĩa cũng có thể được sử dụng để cải thiện hiệu năng ghi, bằng cách sử dụng nó như một bộ đệm ẩn ghi ngược (write-back cache). Ngược lại là bộ đệm ẩn ghi xuyên qua (write-through cache), thứ chỉ hoàn thành các lệnh ghi sau khi đã truyền hoàn toàn tới tầng tiếp theo.

Trong thực tế, các bộ đệm ẩn ghi ngược lưu trữ thường được kết hợp với pin (batteries), sao cho dữ liệu được đệm vẫn có thể được lưu lại trong trường hợp mất điện. Các loại pin như vậy có thể nằm trên đĩa hoặc bộ điều khiển đĩa.

(Hình 9.2 Đĩa đơn giản với bộ đệm ẩn trên đĩa)

### 9.2.3 Bộ điều khiển (Controller)
Một loại bộ điều khiển đĩa đơn giản được trình bày trong Hình 9.3, làm cầu nối giữa vận chuyển I/O CPU với vận chuyển lưu trữ và các thiết bị đĩa gắn kèm. Những thứ này còn được gọi là *host bus adapters* (HBAs).

(Hình 9.3 Bộ điều khiển đĩa đơn giản và các phương thức vận chuyển được kết nối)

Hiệu năng có thể bị giới hạn bởi một trong hai bus này, bộ điều khiển đĩa, hoặc các đĩa. Xem Mục 9.4, Kiến trúc, để biết thêm về các bộ điều khiển đĩa.

## 9.3 Các khái niệm (Concepts)
Sau đây là các khái niệm quan trọng trong hiệu năng đĩa.

### 9.3.1 Đo lường thời gian (Measuring Time)
Thời gian I/O có thể được đo lường dưới dạng:
- **Thời gian yêu cầu I/O (I/O request time)** (còn được gọi là *thời gian phản hồi I/O - I/O response time*): Toàn bộ thời gian từ lúc phát ra một I/O cho đến khi nó hoàn thành.
- **Thời gian chờ I/O (I/O wait time):** Thời gian dành cho việc chờ đợi trong một hàng đợi.
- **Thời gian dịch vụ I/O (I/O service time):** Thời gian trong đó I/O đang được xử lý (không phải chờ đợi).

Những điều này được hình ảnh hóa trong Hình 9.4.

(Hình 9.4 Thuật ngữ thời gian I/O (chung))

Thuật ngữ thời gian dịch vụ có nguồn gốc từ khi các đĩa là các thiết bị đơn giản hơn được quản lý trực tiếp bởi hệ điều hành, do đó kernel biết được khi nào đĩa đang tích cực phục vụ I/O. Các đĩa ngày nay hiện thực hiện việc xếp hàng nội bộ của riêng chúng, và thời gian dịch vụ của hệ điều hành bao gồm cả thời gian dành cho việc chờ đợi trên các hàng đợi kernel.

Khi có thể, tôi sử dụng các thuật ngữ làm rõ để nêu rõ những gì đang được đo lường, từ sự kiện bắt đầu đến sự kiện kết thúc nào. Các sự kiện bắt đầu và kết thúc có thể dựa trên kernel hoặc dựa trên đĩa, với thời gian được đo lường từ giao diện I/O khối cho các thiết bị đĩa (được trình bày trong Hình 9.7).

Từ kernel:
- **Thời gian chờ I/O khối (Block I/O wait time)** (còn được gọi là *thời gian chờ OS - OS wait time*): là thời gian dành từ khi một I/O khối mới được tạo ra và chèn vào một hàng đợi I/O kernel cho đến khi nó rời khỏi hàng đợi kernel cuối cùng và được phát tới thiết bị đĩa. Điều này có thể trải dài qua nhiều hàng đợi cấp kernel, bao gồm một tầng I/O khối và một hàng đợi thiết bị đĩa.
- **Thời gian dịch vụ I/O khối (Block I/O service time):** là thời gian từ khi phát yêu cầu tới thiết bị cho tới khi nhận được ngắt hoàn thành từ thiết bị.
- **Thời gian yêu cầu I/O khối (Block I/O request time):** là cả thời gian chờ I/O khối và thời gian dịch vụ I/O khối: thời gian đầy đủ từ lúc tạo ra một I/O cho đến khi nó hoàn thành.

Từ đĩa:
- **Thời gian chờ đĩa (Disk wait time):** là thời gian dành cho một hàng đợi trên đĩa.
- **Thời gian dịch vụ đĩa (Disk service time):** là thời gian sau khi yêu cầu trên đĩa cần cho một I/O được xử lý tích cực.
- **Thời gian yêu cầu đĩa (Disk request time)** (còn được gọi là *thời gian phản hồi đĩa - disk response time* và *độ trễ I/O đĩa - disk I/O latency*): là cả thời gian chờ đĩa và thời gian dịch vụ đĩa, và bằng với thời gian dịch vụ I/O khối.

Những điều này được hình ảnh hóa trong Hình 9.5, nơi DWT là thời gian chờ đĩa, và DST là thời gian dịch vụ đĩa. Sơ đồ này cũng trình bày một bộ đệm ẩn trên đĩa, và cách các lần trúng bộ đệm ẩn trên đĩa có thể dẫn đến một thời gian dịch vụ thiết bị (DST) ngắn hơn nhiều.

(Hình 9.5 Thuật ngữ thời gian kernel và đĩa)

Độ trễ I/O là một thuật ngữ thường được sử dụng khác, được giới thiệu trong Chương 1. Như với các thuật ngữ khác, ý nghĩa của nó tùy thuộc vào nơi nó được đo lường. Bản thân độ trễ I/O có thể đề cập đến thời gian yêu cầu I/O khối. Các ứng dụng và các công cụ hiệu năng thường sử dụng thuật ngữ *I/O latency* để đề cập đến thời gian yêu cầu đĩa: toàn bộ thời gian trên thiết bị. Nếu bạn đang nói chuyện với một kỹ sư phần cứng từ quan điểm của thiết bị, họ có thể sử dụng thuật ngữ *disk I/O latency* để đề cập đến thời gian chờ đĩa.

Thời gian dịch vụ I/O khối thường được coi như một thước đo cho hiệu năng đĩa hiện tại (đây là những gì các phiên bản cũ của iostat(1) hiển thị); tuy nhiên, bạn nên nhận thức rằng đây là một sự đơn giản hóa. Trong Hình 9.7, một I/O stack chung được trình bày, thứ cho thấy ba tầng trình điều khiển khả thi bên dưới giao diện thiết bị khối. Bất kỳ tầng nào trong số này cũng có thể triển khai hàng đợi của riêng nó, hoặc có thể bị chặn trên các mutexes, thêm độ trễ cho I/O. Độ trễ này được bao gồm trong thời gian dịch vụ I/O khối.

**Tính toán thời gian (Calculating Time)**
Thời gian dịch vụ đĩa thường không thể quan sát được trực tiếp qua các thống kê kernel, nhưng thời gian dịch vụ đĩa trung bình có thể được suy ra bằng cách sử dụng IOPS và mức sử dụng (utilization):

```
thời gian dịch vụ đĩa = mức sử dụng / IOPS
```

Ví dụ, một mức sử dụng 60% và một IOPS là 300 cho một thời gian dịch vụ trung bình là 2 ms (600 ms / 300 IOPS). Các đĩa có thể xử lý đồng thời nhiều I/O song song, khiến tính toán này không chính xác.

Thay vì sử dụng các thống kê kernel, việc truy vết sự kiện có thể được sử dụng để cung cấp một phép đo thời gian chính xác bằng cách đo lường các dấu thời gian có độ phân giải cao cho việc phát hành và hoàn thành I/O khối. Điều này có thể được thực hiện bằng cách sử dụng các công cụ được mô tả sau này trong chương này (ví dụ: biolatency(8) trong Mục 9.6.6, biolatency).

### 9.3.2 Các thang thời gian (Time Scales)
Thang thời gian cho I/O đĩa có thể thay đổi theo các bậc độ lớn, từ hàng chục micro giây tới hàng nghìn mili giây. Ở đầu nhanh nhất, phản hồi I/O đĩa có thể nhanh đến mức nó bị gây ra bởi một lần trượt bộ đệm ẩn nhỏ; ở đầu chậm nhất, I/O đĩa có thể trở thành một vấn đề chỉ trong một số lượng lớn (tổng của nhiều I/O nhanh bằng một I/O chậm).

Để bối cảnh hóa, Bảng 9.1 cung cấp một ý tưởng chung về phạm vi khả thi của các độ trễ I/O đĩa. Để có các giá trị chính xác và hiện tại, hãy tham khảo tài liệu của nhà cung cấp đĩa, và thực hiện micro-benchmarking của riêng bạn. Đồng thời xem Chương 2, Phương pháp luận, để biết thang thời gian cho các I/O đĩa khác.

Để minh họa rõ hơn các bậc độ lớn liên quan, cột Scaled hiển thị một sự so sánh dựa trên một độ trễ trúng bộ đệm ẩn trên đĩa giả định là một giây.

Bảng 9.1 Thang thời gian ví dụ của các độ trễ I/O đĩa
| Sự kiện | Độ trễ | Được điều chỉnh |
| --- | --- | --- |
| Trúng bộ đệm ẩn trên đĩa | < 100 μs | 1 giây |
| Đọc bộ nhớ Flash | ~100 tới 1,000 μs (I/O nhỏ tới lớn) | 1 tới 10 giây |
| Đọc tuần tự đĩa quay | ~1 ms | 10 giây |
| Đọc ngẫu nhiên đĩa quay (7,200 rpm) | ~8 ms | 1.3 phút |
| Đọc ngẫu nhiên đĩa quay (chậm, đang xếp hàng) | > 10 ms | 1.7 phút |
| Đọc ngẫu nhiên đĩa quay (hàng chục yêu cầu trong hàng đợi) | > 100 ms | 17 phút |
| I/O đĩa ảo trường hợp tệ nhất (bộ điều khiển phần cứng, RAID-5, đang xếp hàng, I/O ngẫu nhiên) | > 1,000 ms | 2.8 giờ |

Những độ trễ này có thể được diễn giải khác nhau dựa trên các yêu cầu của môi trường. Trong khi làm việc trong ngành công nghiệp doanh nghiệp, tôi coi các độ trễ đĩa trên 10 ms là không bình thường chậm và là một nguồn gốc tiềm tàng của các vấn đề hiệu năng. Trong ngành công nghiệp điện toán đám mây, có một sự khoan dung lớn hơn cho các độ trễ cao, đặc biệt là trong các ứng dụng hướng người dùng thứ đã kỳ vọng độ trễ cao giữa mạng và trình duyệt máy khách. Trong những môi trường đó, độ trễ đĩa có thể chỉ trở thành một vấn đề chỉ sau 50 ms (riêng lẻ, hoặc tổng cộng trong một yêu cầu ứng dụng).

Bảng này cũng minh họa rằng một đĩa có thể trả về hai loại độ trễ: một cho các lần trúng bộ đệm ẩn trên đĩa (dưới 100 μs) và một cho các lần trượt (1–8 ms và cao hơn, tùy thuộc vào mẫu truy cập và loại thiết bị). Vì một đĩa sẽ trả về một sự kết hợp của các loại này, việc diễn đạt chúng cùng nhau như một độ trễ *trung bình* (như iostat(1) làm) thực sự là một sự kết hợp với hai chế độ. Xem Hình 2.23 trong Chương 2, Phương pháp luận, cho một ví dụ về phân phối độ trễ I/O đĩa dưới dạng một biểu đồ histogram.

### 9.3.3 Caching (Lưu đệm ẩn)
Bài kiểm tra hiệu năng I/O tốt nhất là không có I/O nào cả. Nhiều tầng của stack phần mềm cố gắng tránh I/O đĩa bằng cách đọc cache và buffer các lệnh ghi, ngay xuống tới chính đĩa. Danh sách đầy đủ của các bộ đệm ẩn này nằm trong Bảng 3.2 của Chương 3, Hệ điều hành, thứ bao gồm page cache mức ứng dụng và hệ thống tập tin. Tại mức thiết bị đĩa và bên dưới, các bộ đệm ẩn bao gồm những loại được liệt kê trong Bảng 9.2.

Bảng 9.2 Các bộ đệm ẩn I/O đĩa
| Bộ đệm ẩn | Ví dụ |
| --- | --- |
| Bộ đệm ẩn thiết bị | ZFS vdev |
| Bộ đệm ẩn khối | Buffer cache |
| Bộ đệm ẩn bộ điều khiển đĩa | RAID card cache |
| Bộ đệm ẩn mảng lưu trữ | Array cache |
| Bộ đệm ẩn trên đĩa | DRAM đi kèm của Disk data controller (DDC) |

Buffer cache dựa trên khối đã được mô tả trong Chương 8, Hệ thống tập tin. Những bộ đệm ẩn I/O đĩa này có tầm quan trọng đặc biệt để cải thiện hiệu năng của các khối lượng công việc I/O ngẫu nhiên.

### 9.3.4 I/O Ngẫu nhiên so với Tuần tự (Random vs. Sequential I/O)
Khối lượng công việc I/O đĩa có thể được mô tả bằng cách sử dụng các thuật ngữ *random* và *sequential*, dựa trên vị trí tương đối của I/O trên đĩa (*disk offset*). Những thuật ngữ này đã được thảo luận trong Chương 8, Hệ thống tập tin, liên quan đến các mẫu truy cập tập tin.

Khối lượng công việc tuần tự cũng được gọi là *streaming workloads*. Thuật ngữ *streaming* thường được sử dụng ở mức ứng dụng, để mô tả các lệnh đọc và ghi truyền phát tới "đĩa" (hệ thống tập tin).

Các mẫu I/O tuần tự so với ngẫu nhiên rất quan trọng để nghiên cứu trong thời đại của các đĩa từ tính quay. Đối với những đĩa này, I/O ngẫu nhiên gây thêm độ trễ khi các đầu đọc đĩa tìm kiếm và mâm đĩa quay giữa các I/O. Điều này được trình bày trong Hình 9.6, nơi cả việc seek và rotation là cần thiết để đầu đĩa di chuyển giữa các cung từ 1 và 2 (đường dẫn thực sự thực hiện sẽ trực tiếp nhất có thể). Tinh chỉnh hiệu năng bao gồm việc xác định I/O ngẫu nhiên và cố gắng loại bỏ nó theo một số cách, bao gồm caching, buffering, cô lập I/O ngẫu nhiên vào các đĩa riêng biệt, và đặt đĩa để giảm khoảng cách seek.

(Hình 9.6 Đĩa quay)

Các loại đĩa khác, bao gồm SSDs dựa trên bộ nhớ flash, thường thực hiện khác nhau trên các mẫu I/O ngẫu nhiên và tuần tự. Tùy thuộc vào ổ đĩa, có thể có một sự khác biệt nhỏ do các yếu tố khác, ví dụ, một cache tra cứu địa chỉ thứ có thể trải dài qua các truy cập tuần tự nhưng không ngẫu nhiên. Các lệnh ghi nhỏ hơn kích thước khối có thể gặp phải một hình phạt hiệu năng do một chu kỳ read-modify-write, đặc biệt đối với các lệnh ghi ngẫu nhiên.

Lưu ý rằng các offset đĩa như được thấy từ hệ điều hành có thể không khớp với các offset trên đĩa vật lý. Ví dụ, một đĩa ảo được cung cấp bởi phần cứng có thể ánh xạ một dải liên tục các offset qua nhiều đĩa. Đôi khi I/O ngẫu nhiên không được nhận diện bằng cách kiểm tra các offset nhưng có thể được suy ra bằng cách đo lường thời gian dịch vụ đĩa tăng lên.

### 9.3.5 Tỷ lệ Đọc/Ghi (Read/Write Ratio)
Bên cạnh việc nhận diện các khối lượng công việc ngẫu nhiên so với tuần tự, một thước đo đặc tính khác là tỷ lệ đọc so với ghi, đề cập đến số lượng IOPS hoặc thông lượng. Điều này có thể được diễn đạt dưới dạng tỷ lệ hoặc dưới dạng phần trăm, ví dụ, "Hệ thống đã chạy ở mức 80% đọc kể từ khi khởi động."

Hiểu tỷ lệ này giúp ích khi thiết kế và cấu hình hệ thống. Một hệ thống với tốc độ ghi cao có thể được hưởng lợi nhiều nhất từ việc thêm cache ghi. Một hệ thống với tốc độ đọc cao có thể được hưởng lợi nhiều nhất từ việc thêm nhiều đĩa hơn để tăng thông lượng và IOPS tối đa khả dụng.

Bản thân các lệnh đọc và ghi có thể cho thấy các mẫu khối lượng công việc khác nhau: các lệnh đọc có thể là ngẫu nhiên trong khi các lệnh ghi có thể là tuần tự (đặc biệt đối với các hệ thống tập tin copy-on-write). Chúng cũng có thể thể hiện các kích thước I/O khác nhau.

### 9.3.6 Kích thước I/O (I/O Size)
Kích thước I/O trung bình (byte), hoặc phân phối các kích thước I/O, là một đặc tính khối lượng công việc khác. Các kích thước I/O lớn hơn thường mang lại thông lượng cao hơn, mặc dù cho độ trễ mỗi I/O dài hơn.

Kích thước I/O có thể bị thay đổi bởi hệ thống con thiết bị đĩa (ví dụ, được định lượng thành các cung từ 512-byte). Các kích thước I/O có thể đã bị thổi phồng và bị giảm bớt kể từ khi I/O ứng dụng được phát ra, bởi các thành phần kernel như các volume managers, và các trình điều khiển thiết bị. Xem các phần Bị thổi phồng và Bị giảm bớt trong Chương 8, Hệ thống tập tin, Mục 8.3.12, I/O Logic so với Vật lý.

Một số thiết bị đĩa, đặc biệt là SSDs, thực hiện rất khác nhau với các kích thước đọc và ghi khác nhau. Ví dụ, một ổ đĩa flash có thể thực hiện tối ưu với các lệnh đọc 4 Kbyte và các lệnh ghi 1 Mbyte. Các kích thước I/O đĩa lý tưởng có thể được tài liệu hóa bởi nhà cung cấp đĩa hoặc được nhận diện bằng cách sử dụng micro-benchmarking. Kích thước I/O đĩa hiện tại đang sử dụng có thể được thấy bằng cách sử dụng các công cụ quan sát (xem Mục 9.6, Các công cụ quan trắc).

### 9.3.7 IOPS không bình đẳng (IOPS Are Not Equal)
Bởi vì ba đặc tính cuối cùng đó, IOPS không được tạo ra bình đẳng và không thể được so sánh trực tiếp giữa các thiết bị và khối lượng công việc khác nhau. Một giá trị IOPS tự thân nó không mang nhiều ý nghĩa.

Ví dụ, với các đĩa quay, một khối lượng công việc 5,000 IOPS tuần tự có thể nhanh hơn nhiều so với một khối lượng công việc 1,000 IOPS ngẫu nhiên. Các IOPS dựa trên bộ nhớ Flash cũng khó so sánh, vì hiệu năng ghi I/O của chúng thường liên quan đến kích thước I/O và hướng (đọc hoặc ghi).

IOPS thậm chí có thể không quan trọng lắm đối với khối lượng công việc ứng dụng. Một khối lượng công việc bao gồm các yêu cầu ngẫu nhiên thường nhạy cảm với độ trễ, trong trường hợp đó IOPS cao là mong muốn. Một khối lượng công việc truyền phát (tuần tự) nhạy cảm với thông lượng, thứ có thể mang lại tốc độ IOPS thấp hơn của các I/O lớn hơn nhưng mong muốn hơn.

Để hiểu ý nghĩa của IOPS, hãy bao gồm các chi tiết khác: ngẫu nhiên hoặc tuần tự, kích thước I/O, đọc/ghi, được đệm/trực tiếp, và số lượng I/O song song. Đồng thời cân nhắc sử dụng các chỉ số dựa trên thời gian, chẳng hạn như mức sử dụng và thời gian dịch vụ, thứ phản ánh hiệu năng kết quả và có thể được so sánh dễ dàng hơn.

### 9.3.8 Các lệnh đĩa không truyền tải dữ liệu (Non-Data-Transfer Disk Commands)
Các lệnh khác có thể được gửi tới các đĩa ngoài các lệnh đọc và ghi I/O. Bộ đệm ẩn trên đĩa (RAM) có thể được ra lệnh để flush bộ đệm ẩn xuống đĩa. Một lệnh như vậy không phải là một lệnh truyền tải dữ liệu; dữ liệu đã được gửi tới đĩa trước đó qua các lệnh ghi.

Một lệnh ví dụ khác được sử dụng để hủy bỏ dữ liệu: lệnh ATA TRIM, hoặc lệnh SCSI UNMAP. Điều này báo cho ổ đĩa biết rằng một dải cung từ không còn cần thiết nữa, và có thể giúp ổ SSD duy trì hiệu năng ghi.

Các lệnh đĩa này có thể ảnh hưởng đến hiệu năng và có thể khiến một đĩa được sử dụng trong khi chờ đợi I/O.

### 9.3.9 Mức sử dụng (Utilization)
Mức sử dụng có thể được tính toán bằng tỷ lệ thời gian một đĩa bận rộn tích cực thực hiện công việc trong một khoảng thời gian.

Một đĩa ở mức sử dụng 0% là "rảnh rỗi", và một đĩa ở mức sử dụng 100% là liên tục bận rộn thực hiện I/O (và các lệnh đĩa khác). Các đĩa ở mức sử dụng 100% có khả năng là một nguồn gây ra các vấn đề hiệu năng, đặc biệt nếu chúng duy trì ở mức 100% trong một thời gian. Tuy nhiên, bất kỳ tốc độ sử dụng đĩa nào cũng có thể đóng góp vào hiệu năng kém, vì I/O đĩa điển hình là một hoạt động chậm.

Cũng có một ranh giới giữa mức sử dụng 0% và 100% (ví dụ, 60%) mà tại đó hiệu năng của đĩa không còn thỏa đáng nữa do việc xếp hàng tăng lên, hoặc trên đĩa hoặc trong hệ thống điều hành. Giá trị mức sử dụng chính xác mà tại đó trở thành một vấn đề phụ thuộc vào đĩa, khối lượng công việc và các yêu cầu về độ trễ. Xem phần M/D/1 và lý thuyết xếp hàng 60% Utilization trong Chương 2, Phương pháp luận, Mục 2.6.5, Lý thuyết xếp hàng.

Để xác nhận liệu mức sử dụng cao có đang gây ra các vấn đề hiệu năng hay không, hãy nghiên cứu thời gian phản hồi của đĩa và liệu ứng dụng có đang bị chặn trên I/O hay không. Ứng dụng hoặc hệ điều hành có thể đang thực hiện I/O một cách bất đồng bộ, sao cho I/O chậm đó không trực tiếp khiến ứng dụng phải chờ đợi.

Lưu ý rằng mức sử dụng là một bản tóm tắt theo khoảng thời gian. I/O đĩa có thể xảy ra theo các đợt bùng phát, đặc biệt do việc flush ghi, thứ có thể bị che giấu khi tóm tắt qua các khoảng thời gian dài hơn. Xem Chương 2, Các Phương pháp luận, Mục 2.3.11, Mức sử dụng, để biết thêm thảo luận về loại chỉ số mức sử dụng.

**Mức sử dụng Đĩa ảo (Virtual Disk Utilization)**
Đối với các đĩa ảo được cung cấp bởi phần cứng (ví dụ: một bộ điều khiển đĩa, hoặc lưu trữ gắn mạng), hệ điều hành có thể biết khi nào đĩa ảo bận, nhưng không biết gì về hiệu năng của các đĩa vật lý cơ sở. Điều này dẫn đến các kịch bản nơi mức sử dụng đĩa ảo, như được báo cáo bởi hệ điều hành, khác biệt đáng kể so với những gì đang xảy ra trên các đĩa vật lý (và là trái ngược với trực giác):
- Một đĩa ảo bận rộn 100%, và được xây dựng trên nhiều đĩa vật lý, có thể chấp nhận thêm nhiều công việc hơn. Trong trường hợp này, 100% có thể có nghĩa là *một số* đĩa đã bận rộn suốt thời gian qua, nhưng không phải tất cả các đĩa đều bận suốt thời gian đó, và do đó một số đĩa vẫn rảnh rỗi.
- Các đĩa ảo bao gồm một bộ đệm ẩn ghi ngược có thể không xuất hiện bận rộn trong các đợt bùng phát tải ghi, vì bộ điều khiển đĩa trả về các lần hoàn thành ngay lập tức, mặc dù các đĩa cơ sở bận rộn trong một thời gian sau đó.
- Các đĩa có thể bận rộn do xây dựng lại phần cứng RAID, mà không có I/O tương ứng được thấy bởi hệ điều hành.

Vì những lý do tương tự, có thể khó diễn giải mức sử dụng của các đĩa ảo được tạo ra bởi phần mềm hệ điều hành (software RAID). Tuy nhiên, hệ điều hành nên để lộ mức sử dụng cho các đĩa vật lý, thứ có thể được kiểm tra.

Khi một đĩa vật lý đạt mức sử dụng 100% và có thêm I/O được yêu cầu, nó trở thành bị bão hòa.

### 9.3.10 Độ bão hòa (Saturation)
Độ bão hòa là một thước đo của công việc được xếp hàng vượt quá những gì tài nguyên có thể đáp ứng. Đối với các thiết bị đĩa, nó có thể được tính toán như độ dài trung bình của hàng đợi thiết bị trong khoảng thời gian điều hành (giả sử nó không xếp hàng).

Điều này cung cấp một thước đo hiệu năng vượt ra ngoài điểm mức sử dụng 100%. Một đĩa ở mức sử dụng 100% có thể không có sự bão hòa (đang xếp hàng), hoặc nó có thể có một hàng đợi lớn, ảnh hưởng đáng kể đến hiệu năng do việc xếp hàng I/O.

Bạn có thể giả định rằng các đĩa ở mức sử dụng dưới 100% thì không có độ bão hòa, nhưng điều này thực sự tùy thuộc vào khoảng thời gian sử dụng: mức sử dụng 50% trong một khoảng thời gian có thể có nghĩa là bận rộn 100% trong một nửa thời gian đó và rảnh rỗi cho phần còn lại. Bất kỳ sự tóm tắt theo khoảng thời gian nào cũng có thể gặp phải các vấn đề tương tự. Khi việc biết chính xác những gì đã xảy ra là quan trọng, các công cụ truy vết có thể được sử dụng để kiểm tra các sự kiện I/O.

### 9.3.11 Đợi I/O (I/O Wait)
Đợi I/O là một chỉ số hiệu năng cho mỗi CPU cho thấy thời gian CPU rảnh rỗi, khi có các luồng trong hàng đợi điều phối CPU (ở trạng thái ngủ) bị chặn trên I/O đĩa. Điều này chia thời gian CPU rảnh rỗi thành thời gian rảnh rỗi khi không có việc gì làm, và thời gian dành cho việc chờ đợi I/O đĩa. Mẫu hình ở đây là một dấu hiệu của một nút thắt cổ chai hệ thống: các CPU rảnh rỗi. Một cách khác để giải thích I/O đợi là các đĩa có thể là một nút thắt cổ chai, để lại CPU rảnh rỗi trong khi nó chờ đợi chúng.

I/O đợi có thể là một chỉ số rất gây nhầm lẫn. Nếu một tiến trình tiêu tốn CPU khác xuất hiện, giá trị I/O đợi có thể giảm xuống: các CPU bây giờ có thứ gì đó để làm, thay vì rảnh rỗi. Tuy nhiên, cùng một khối lượng công việc I/O đĩa vẫn hiện diện và chặn các luồng, bất chấp việc chỉ số I/O đợi giảm xuống. Trường hợp ngược lại đôi khi xảy ra khi các quản trị viên hệ thống đã nâng cấp phần mềm ứng dụng và phiên bản mới hơn hiệu quả hơn và sử dụng ít chu kỳ CPU hơn, *tiết lộ* I/O đợi. Điều này có thể khiến quản trị viên hệ thống nghĩ rằng bản nâng cấp đã gây ra một vấn đề về đĩa và làm giảm hiệu năng, trong khi thực tế hiệu năng đĩa là như nhau, nhưng hiệu năng CPU đã được cải thiện.

Một chỉ số đáng tin cậy hơn là thời gian mà các luồng ứng dụng bị chặn trên I/O đĩa. Điều này bắt được sự ảnh hưởng mà các luồng ứng dụng phải chịu do các đĩa, bất kể các CPU đang làm công việc gì khác. Chỉ số này có thể được đo lường bằng cách sử dụng instrumentation tĩnh hoặc động.

I/O đợi vẫn là một chỉ số phổ biến trên các hệ thống Linux và, bất chấp tính chất gây nhầm lẫn của nó, nó được sử dụng thành công để xác định một loại nút thắt cổ chai đĩa: các CPU rảnh rỗi. Một cách để diễn giải nó là coi bất kỳ I/O đợi nào như một dấu hiệu của một nút thắt cổ chai hệ thống, và sau đó tinh chỉnh hệ thống để giảm thiểu nó—ngay cả khi I/O vẫn đang xảy ra đồng thời với mức sử dụng CPU. I/O đợi đồng thời có nhiều khả năng là I/O không chặn, và ít có khả năng gây ra một vấn đề trực tiếp. I/O không đồng thời, như được nhận diện bởi I/O đợi, có nhiều khả năng là I/O ứng dụng chặn, và một nút thắt cổ chai.

### 9.3.12 Đồng bộ so với Bất đồng bộ (Synchronous vs. Asynchronous)
Có thể quan trọng để hiểu rằng độ trễ I/O đĩa có thể không trực tiếp ảnh hưởng đến hiệu năng ứng dụng, nếu ứng dụng I/O và đĩa I/O hoạt động một cách bất đồng bộ. Điều này thường xuyên xảy ra với write-back caching, nơi ứng dụng I/O hoàn thành sớm, và đĩa I/O được phát ra sau đó.

Các ứng dụng có thể sử dụng read-ahead để thực hiện các lệnh đọc bất đồng bộ, thứ có thể không chặn ứng dụng trong khi đĩa hoàn thành I/O. Hệ thống tập tin có thể tự khởi tạo việc này để làm nóng bộ đệm ẩn (prefetch).

Ngay cả khi một ứng dụng đang chờ đợi I/O một cách đồng bộ, đường dẫn mã ứng dụng đó có thể không phải là nhiệm vụ quan trọng (non-critical) và bất đồng bộ đối với các yêu cầu ứng dụng của khách hàng. Nó có thể là một luồng worker I/O của ứng dụng, được tạo ra để quản lý I/O trong khi các luồng khác tiếp tục xử lý công việc.

Các kernel cũng thường hỗ trợ I/O *asynchronous* hoặc *non-blocking*, nơi một API được cung cấp cho các ứng dụng để yêu cầu I/O và được thông báo về sự hoàn thành của nó vào lúc nào đó sau đó. Xem Chương 8, Hệ thống tập tin, các Mục 8.3.9, Non-Blocking I/O; 8.3.5, Read-Ahead; 8.3.4, Prefetch; và 8.3.7, Các lệnh ghi đồng bộ.

### 9.3.13 Đĩa so với I/O Ứng dụng (Disk vs. Application I/O)
I/O đĩa là kết quả cuối cùng của các thành phần kernel khác nhau, bao gồm các hệ thống tập tin và các trình điều khiển thiết bị. Có nhiều lý do tại sao tốc độ và khối lượng của I/O đĩa này có thể không khớp với I/O được phát ra bởi ứng dụng. Những điều này bao gồm:
- **Sự thổi phồng, giảm bớt, và không liên quan của hệ thống tập tin I/O.** Xem Chương 8, Hệ thống tập tin, Mục 8.3.12, I/O Logic so với Vật lý.
- **Paging do sự thâm hụt bộ nhớ hệ thống.** Xem Chương 7, Bộ nhớ, Mục 7.2.2, Paging.
- **Kích thước I/O trình điều khiển thiết bị:** làm tròn kích thước I/O, hoặc phân mảnh I/O.
- **Gương ghi RAID hoặc dữ liệu kiểm tra tổng (checksum), hoặc dữ liệu đọc xác minh.**

Sự không khớp này có thể gây nhầm lẫn khi không được mong đợi. Nó có thể được hiểu bằng cách tìm hiểu kiến trúc và thực hiện phân tích hiệu năng.

---

## 9.4 Kiến trúc (Architecture)
Phần này mô tả kiến trúc đĩa, thứ thường được nghiên cứu trong quá trình quy hoạch dung lượng để xác định các giới hạn cho các thành phần và các lựa chọn cấu hình khác nhau. Nó cũng nên được kiểm tra trong quá trình điều tra các vấn đề hiệu năng sau này, trong trường hợp vấn đề bắt nguồn từ các lựa chọn kiến trúc hơn là tải và tinh chỉnh hiện tại.

### 9.4.1 Các loại Đĩa (Disk Types)
Hai loại đĩa được sử dụng phổ biến nhất hiện nay là đĩa quay từ tính và đĩa dựa trên bộ nhớ flash (SSDs). Cả hai đều cung cấp khả năng lưu trữ lâu dài; nội dung của chúng vẫn khả dụng sau khi chu kỳ nguồn điện kết thúc.

#### 9.4.1.1 Quay từ tính (Magnetic Rotational)
Còn được gọi là *hard disk drive* (HDD), loại đĩa này bao gồm một hoặc nhiều mâm đĩa, được tẩm bằng các hạt oxit sắt. Một vùng nhỏ của những hạt này có thể được từ hóa theo một trong hai hướng; định hướng này được sử dụng để lưu trữ một bit. Các mâm đĩa quay, trong khi một cánh tay cơ học với các mạch điện để đọc và ghi dữ liệu vươn ra bề mặt. Mạch điện này bao gồm các *disk heads*, và một cánh tay có thể có nhiều đầu đọc, cho phép nó đọc và ghi nhiều bit đồng thời. Dữ liệu được lưu trữ trên mâm đĩa trong các đường tròn (tracks), và mỗi đường tròn được chia thành các cung từ (sectors).

Là các thiết bị cơ học, chúng thực hiện tương đối chậm, đặc biệt đối với I/O ngẫu nhiên. Với những tiến bộ trong công nghệ bộ nhớ flash, SSDs đang thay thế các đĩa quay, và có thể hiểu được rằng một ngày nào đó các đĩa quay sẽ trở nên lỗi thời (cùng với các công nghệ lưu trữ cũ hơn khác như các ổ đĩa băng từ và bộ nhớ lõi). Tuy nhiên, trong thời gian chờ đợi, các đĩa quay vẫn mang tính cạnh tranh trong một số kịch bản, chẳng hạn như lưu trữ mật độ cao giá rẻ (chi phí mỗi megabyte thấp), đặc biệt cho việc lưu trữ dữ liệu (data warehousing).

Các chủ đề sau đây tóm tắt các yếu tố trong hiệu năng đĩa quay.

**Seek và Rotation (Tìm kiếm và Quay)**
I/O chậm cho đĩa quay từ tính thường gây ra bởi thời gian tìm kiếm cho các đầu đĩa và thời gian quay của mâm đĩa đĩa, cả hai đều có thể mất vài mili giây. Trường hợp tốt nhất là khi I/O tiếp theo được yêu cầu nằm ở cuối I/O hiện đang được phục vụ, sao cho các đầu đĩa không cần phải di chuyển hoặc chờ đợi thêm vòng quay. Như đã mô tả trước đó, đây được gọi là *sequential I/O*, trong khi I/O yêu cầu đầu đọc di chuyển hoặc chờ đợi vòng quay được gọi là *random I/O*.

Có nhiều chiến lược để giảm thiểu thời gian chờ seek và rotation, bao gồm:
- **Caching:** loại bỏ hoàn toàn I/O.
- **Vị trí và hành vi hệ thống tập tin:** bao gồm copy-on-write (thứ làm cho các lệnh ghi là tuần tự, nhưng có thể làm cho các lệnh đọc là ngẫu nhiên).
- **Phân tách các khối lượng công việc khác nhau vào các đĩa khác nhau:** để tránh việc seek giữa các I/O của các khối lượng công việc.
- **Di chuyển các khối lượng công việc khác nhau vào các hệ thống khác nhau:** (một số môi trường điện toán đám mây có thể thực hiện việc này để giảm bớt các tác động đa thuê - multi-tenancy).
- **Elevator seeking:** được thực hiện bởi chính đĩa.
- **Đĩa mật độ cao hơn:** để thu hẹp vị trí khối lượng công việc.
- **Cấu hình Phân vùng (hoặc "slice"):** cho seek ngắn, kiểu short-stroking.

Một chiến lược bổ sung để giảm thời gian quay là sử dụng các đĩa nhanh hơn. Các đĩa có sẵn ở các tốc độ quay khác nhau, bao gồm 5400, 7200, 10 K, và 15 K vòng mỗi phút (rpm). Lưu ý rằng tốc độ cao hơn có thể dẫn đến tuổi thọ đĩa thấp hơn, do nhiệt độ và độ mòn tăng lên.

**Thông lượng Tối đa Lý thuyết (Theoretical Maximum Throughput)**
Nếu số cung từ tối đa trên mỗi track của một đĩa là đã biết, thông lượng đĩa có thể được tính toán bằng công thức sau:

```
thông lượng tối đa = các cung từ tối đa trên mỗi track × kích thước cung từ × rpm/60 s
```

Công thức này hữu ích hơn cho các đĩa cũ đã để lộ thông tin này một cách chính xác. Các đĩa hiện đại cung cấp một hình ảnh ảo của đĩa cho hệ điều hành, và chỉ để lộ các giá trị tổng hợp (synthetic) cho những thuộc tính này.

**Short-Stroking**
Short-stroking là nơi chỉ các track bên ngoài của đĩa được sử dụng cho khối lượng công việc; phần còn lại hoặc không được sử dụng, hoặc được sử dụng cho khối lượng công việc ưu tiên thấp (ví dụ: các kho lưu trữ). Điều này làm giảm thời gian seek vì chuyển động của đầu đọc bị giới hạn trong một dải nhỏ hơn, và đầu đọc có thể đưa các đầu đọc về trạng thái nghỉ tại mép ngoài, giảm seek đầu tiên sau khi rảnh rỗi. Các track bên ngoài cũng thường có hiệu năng thông lượng tốt hơn do zoning cung từ (xem phần tiếp theo). Hãy lưu ý rằng các benchmark đĩa đã được công bố, đặc biệt là các benchmark đặc biệt không bao gồm giá trị giá cả, nơi có thể đã sử dụng nhiều đĩa short-stroked.

**Sector Zoning (Phân vùng cung từ)**
Chiều dài của các track đĩa thay đổi, với chiều dài ngắn nhất ở tâm của đĩa và dài nhất ở mép ngoài. Thay vì số lượng cung từ (và bit) trên mỗi track được cố định, phân vùng cung từ (còn được gọi là *multiple-zone recording*) tăng số lượng cung từ cho các track dài hơn, vì có thể ghi được nhiều cung từ hơn về mặt vật lý. Bởi vì tốc độ quay là không đổi, các track ở mép ngoài dài hơn cung cấp thông lượng cao hơn (megabyte mỗi giây) so với các track bên trong.

**Kích thước Cung từ (Sector Size)**
Ngành công nghiệp lưu trữ đã phát triển một tiêu chuẩn mới cho các kích thước cung từ, được gọi là Advanced Format, để hỗ trợ các kích thước cung từ lớn hơn, cụ thể là 4 Kbyte. Điều này làm giảm chi phí metadata, cải thiện thông lượng cũng như giảm các chi phí cho metadata lưu trữ của đĩa trên mỗi cung từ. Các đĩa cung từ 512 byte vẫn có thể được cung cấp bởi firmware của đĩa thông qua một tiêu chuẩn mô phỏng được gọi là Advanced Format 512e. Tùy thuộc vào đĩa, điều này có thể làm tăng các chi phí metadata, kích hoạt một chu trình đọc-sửa-ghi để ánh xạ các cung từ 512 byte sang một cung từ 4 Kbyte. Các vấn đề hiệu năng khác cần lưu ý bao gồm các I/O 4 Kbyte bị sai lệch (misaligned), thứ trải dài qua hai cung từ, làm thổi phồng I/O đĩa lên gấp đôi để phục vụ chúng.

**Bộ đệm ẩn trên đĩa (On-Disk Cache)**
Một thành phần chung của những đĩa này là một lượng nhỏ bộ nhớ (RAM) được sử dụng để đệm kết quả của các lệnh đọc và các lệnh ghi buffer. Bộ nhớ này cũng cho phép I/O (các lệnh) được xếp hàng trên thiết bị và được sắp xếp lại hiệu quả hơn. Với SCSI, điều này được gọi là Tagged Command Queueing (TCQ); với SATA, nó được gọi là Native Command Queueing (NCQ).

**Elevator Seeking**
Thuật toán thang máy (còn được gọi là *elevator seeking*) là một cách mà một hàng đợi lệnh có thể cải thiện hiệu quả. Nó sắp xếp lại I/O dựa trên vị trí trên đĩa của chúng, để giảm thiểu hành trình của các đầu đĩa. Kết quả tương tự như một thang máy trong tòa nhà, thứ không phục vụ các tầng dựa trên thứ tự các nút tầng được bấm, nhưng thực hiện các lượt quét lên và xuống tòa nhà, dừng lại tại các tầng được yêu cầu hiện tại.

Hành vi này trở nên rõ ràng khi kiểm tra các vết truy vết I/O đĩa và nhận thấy rằng việc sắp xếp I/O theo thời gian hoàn thành không khớp với việc sắp xếp theo thời gian bắt đầu: I/O đang được hoàn thành lệch khỏi thứ tự.

Trong khi điều này có vẻ như là một thắng lợi rõ rệt về hiệu năng, hãy suy ngẫm về kịch bản sau: Một đĩa có 1,000 I/O được gửi tới offset 1,000, và một I/O duy nhất ở offset 2,000. Bây giờ hãy xem xét rằng, trong khi I/O ở mức 1,000 đang được phục vụ, thêm 1,000 cái nữa đến ở gần mức 1,000, và hơn thế nữa—đủ để liên tục phục vụ I/O ở mức 1,000 trong 10 giây. Khi nào I/O ở offset 2,000 sẽ được phục vụ, và độ trễ I/O cuối cùng của nó là bao nhiêu?

**Tính toàn vẹn dữ liệu (Data Integrity)**
Các đĩa lưu trữ một mã sửa lỗi (error-correcting code - ECC) ở cuối mỗi cung từ cho tính toàn vẹn dữ liệu, sao cho ổ đĩa có thể xác minh dữ liệu đã được đọc chính xác, hoặc sửa bất kỳ lỗi nào có thể đã xảy ra. Nếu cung từ không được đọc chính xác, các đầu đĩa có thể thử đọc lại ở vòng quay tiếp theo (và có thể thử lại một vài lần, di chuyển vị trí đầu đọc một chút mỗi lần). Đây có thể là lời giải thích cho các I/O đơn lẻ chậm bất thường (ví dụ: 10 ms). Ổ đĩa có thể cung cấp các lỗi mềm cho OS để giải thích những gì đã xảy ra. Có thể có lợi khi giám sát tỷ lệ các lỗi mềm này, vì sự gia tăng có thể chỉ ra rằng ổ đĩa sắp hỏng.

Một lợi ích của việc ngành công nghiệp chuyển từ 512 byte sang các cung từ 4 Kbyte là cần ít bit ECC hơn cho cùng một khối lượng dữ liệu, vì ECC hiệu quả hơn cho kích thước cung từ lớn hơn [Smith 09].

Lưu ý rằng các dữ liệu kiểm tra tổng (checksums) khác cũng có thể được sử dụng để xác minh dữ liệu. Ví dụ, một kiểm tra dự phòng vòng (cyclic redundancy check - CRC) có thể được sử dụng để xác minh việc truyền dữ liệu tới host, và các checksums khác có thể được sử dụng bởi các hệ thống tập tin.

**Rung động (Vibration)**
Trong khi các nhà cung cấp thiết bị đĩa nhận thức rõ về các vấn đề rung động, những vấn đề này không được biết đến một cách phổ biến hoặc được ngành công nghiệp coi trọng. Vào năm 2008, trong khi đang điều tra một vấn đề hiệu năng bí ẩn, tôi đã tiến hành một thực nghiệm kích thích rung động bằng cách hét (shouting) vào một mảng đĩa trong khi nó đang thực hiện một benchmark ghi, thứ gây ra một đợt bùng phát I/O chậm bất thường. Thực nghiệm của tôi đã ngay lập tức được quay video và đăng lên YouTube, nơi nó đã lan truyền nhanh chóng, và từ đó nó đã được mô tả như là sự trình diễn đầu tiên về tác động của rung động đối với hiệu năng đĩa [Turner 10]. Video này đã có hơn 1,700,000 lượt xem, thúc đẩy nhận thức về các vấn đề rung động đĩa [Gregg 08]. Dựa trên các email tôi nhận được, tôi cũng nhận thấy đã vô tình sinh ra một ngành công nghiệp trong việc cách âm các trung tâm dữ liệu: giờ đây bạn có thể thuê các chuyên gia để phân tích mức âm thanh trung tâm dữ liệu và cải thiện hiệu năng đĩa bằng cách giảm thiểu các rung động.

**Sloth Disks**
Một vấn đề hiệu năng hiện tại với một số đĩa quay là sự phát hiện của cái được gọi là *sloth disks*. Những đĩa này đôi khi trả về I/O rất chậm, trên một giây, mà không báo cáo bất kỳ lỗi nào. Điều này dài hơn nhiều so với thời gian mà các lần thử lại dựa trên ECC nên mất. Có lẽ sẽ tốt hơn nếu các đĩa như vậy trả về một lỗi thay vì trì hoãn lâu như vậy, sao cho hệ điều hành hoặc các bộ điều khiển đĩa có thể thực hiện hành động khắc phục, chẳng hạn như đưa đĩa ra khỏi hệ thống (offlining) trong các môi trường dư thừa và báo cáo sự cố. Đĩa Sloth là một sự phiền toái, đặc biệt là khi chúng là một phần của một mảng lưu trữ ảo được trình diễn bởi một mảng lưu trữ mà hệ điều hành không có khả năng quan sát trực tiếp, khiến chúng khó nhận diện hơn. (Nếu hệ thống Linux Distributed Replicated Block Device (DRBD) đang được sử dụng, nó cung cấp một tham số "disk-timeout".)

**SMR**
Shingled Magnetic Recording (SMR) mang lại mật độ cao hơn bằng cách sử dụng các track hẹp hơn. Các track này quá hẹp để đầu ghi có thể ghi lại, nhưng không phải cho đầu đọc (nhỏ hơn) để đọc chúng, vì vậy nó ghi chúng bằng cách xếp chồng một phần các track khác, theo một kiểu tương tự như ngói lợp mái nhà (do đó có tên như vậy). Các ổ đĩa sử dụng SMR tăng mật độ lên khoảng 25%, với chi phí là hiệu năng ghi bị suy giảm, vì dữ liệu chồng lên nhau bị phá hủy và phải được ghi lại. Những ổ đĩa này phù hợp cho các khối lượng công việc lưu trữ được ghi một lần rồi sau đó chủ yếu được đọc, nhưng không phù hợp cho các khối lượng công việc nặng về ghi trong các cấu hình RAID [Mellor 20].

**Disk Data Controller**
Các đĩa cơ học trình diễn một giao diện đơn giản tới hệ thống, ám chỉ một tỷ lệ cung từ-trên-mỗi-track cố định và một dải các offset địa chỉ liên tục. Những gì thực sự xảy ra trên đĩa tùy thuộc vào bộ điều khiển dữ liệu đĩa—một bộ vi xử lý được lập trình bởi firmware. Các đĩa có thể triển khai các thuật toán chẳng hạn như zoning cung từ, ảnh hưởng đến vị trí các offset được bố trí. Điều này gây khó khăn cho việc phân tích—ngay cả đối với hệ điều hành—vì nó không thể thấy bên trong bộ điều khiển dữ liệu đĩa.

#### 9.4.1.2 Các ổ đĩa thể rắn (Solid-State Drives)
Chúng còn được gọi là *solid-state disks* (SSDs). Thuật ngữ solid-state đề cập đến việc sử dụng các linh kiện điện tử thể rắn, thứ cung cấp bộ nhớ không bay hơi (nonvolatile) được lập trình được với hiệu năng thường tốt hơn nhiều so với các đĩa quay. Không có các bộ phận chuyển động, các đĩa này cũng bền về mặt vật lý và không dễ bị các vấn đề hiệu năng gây ra bởi rung động.

Hiệu năng của loại đĩa này thường nhất quán trên các offset khác nhau (không có seek rotation hoặc độ trễ tìm kiếm) và có thể dự đoán được cho các kích thước I/O nhất định. Đặc tính ngẫu nhiên hoặc tuần tự của khối lượng công việc ít quan trọng hơn nhiều so với các đĩa quay. Tất cả những điều này khiến chúng dễ dàng hơn cho việc nghiên cứu và quy hoạch dung lượng. Tuy nhiên, nếu chúng gặp phải các bệnh lý (pathologies) hiệu năng, việc hiểu chúng có thể cũng phức tạp như với các đĩa quay, do cách chúng vận hành bên trong.

Một số SSDs sử dụng DRAM không bay hơi (NV-DRAM). Hầu hết sử dụng bộ nhớ flash.

**Bộ nhớ Flash (Flash Memory)**
Các ổ SSD dựa trên bộ nhớ flash mang lại hiệu năng đọc cao, đặc biệt là hiệu năng đọc ngẫu nhiên có thể vượt qua các đĩa quay tới nhiều bậc độ lớn. Hầu hết được xây dựng bằng bộ nhớ flash NAND, thứ sử dụng các môi trường lưu trữ điện tích bị mắc kẹt bởi electron (electron-based trapped-charge) có thể lưu trữ các electron một cách bền vững trong trạng thái không có điện [Cornwell 12]. Tên gọi "flash" liên quan đến cách dữ liệu được ghi, thứ yêu cầu xóa toàn bộ một khối bộ nhớ tại một thời điểm (bao gồm nhiều trang, thường là 8 hoặc 64 Kbyte mỗi trang) và ghi lại nội dung. Do các chu kỳ ghi này, bộ nhớ flash có các đặc tính hiệu năng đọc/ghi không đối xứng: các lần đọc nhanh và các lần ghi chậm hơn. Các ổ đĩa thường giảm thiểu điều này bằng cách sử dụng các bộ đệm ẩn ghi để cải thiện hiệu năng ghi, và một tụ điện nhỏ để làm bộ lưu điện trong trường hợp mất điện.

Bộ nhớ Flash có nhiều loại khác nhau:
- **Single-level cell (SLC):** Lưu trữ các bit dữ liệu trong các cell riêng lẻ.
- **Multi-level cell (MLC):** Lưu trữ nhiều bit trên mỗi cell (thường là hai, yêu cầu bốn mức điện áp).
- **Enterprise multi-level cell (eMLC):** MLC với firmware nâng cao dành cho việc sử dụng trong doanh nghiệp.
- **Tri-level cell (TLC):** Lưu trữ ba bit (tám mức điện áp).
- **Quad-level cell (QLC):** Lưu trữ bốn bit.
- **3D NAND / Vertical NAND (V-NAND):** Thứ xếp chồng các lớp bộ nhớ (ví dụ: TLC) để tăng mật độ và dung lượng lưu trữ.

Danh sách này sắp xếp theo thứ tự thời gian thô, với các công nghệ mới nhất được liệt kê sau cùng: 3D NAND đã được thương mại hóa từ năm 2013.

SLC có xu hướng có hiệu năng và độ tin cậy cao hơn so với các loại khác và được ưu tiên trong ngành công nghiệp trước đây, mặc dù với chi phí cao hơn. MLC hiện nay thường được sử dụng trong doanh nghiệp do mật độ cao hơn, mặc dù độ tin cậy thấp hơn. Độ tin cậy của Flash thường được đo lường dưới dạng số lượng chu kỳ chặn (program/erase cycles) mà một ổ đĩa được kỳ vọng sẽ hỗ trợ. Đối với SLC, con số này nằm trong khoảng 50,000 đến 100,000 chu kỳ; đối với MLC khoảng 5,000 đến 10,000 chu kỳ; đối với TLC khoảng 3,000 chu kỳ; và đối với QLC khoảng 1,000 chu kỳ [Liu 20].

**Bộ điều khiển (Controller)**
Bộ điều khiển cho một ổ SSD có nhiệm vụ sau [Leventhal 13]:
- **Input:** Đọc và ghi xảy ra theo từng trang (thường là 8 Kbytes); việc ghi chỉ có thể xảy ra đối với các trang đã xóa; các trang được xóa theo từng khối gồm 32 đến 64 trang (256–512 Kbytes).
- **Output:** Mô phỏng một giao diện đĩa cứng: đọc hoặc ghi các cung từ tùy ý (512 byte hoặc 4 Kbytes).

Việc dịch giữa input và output được thực hiện bởi tầng dịch flash (flash translation layer - FTL) của bộ điều khiển, thứ cũng phải theo dõi các khối trống. Về cơ bản nó sử dụng hệ thống tập tin riêng của nó để làm điều này, chẳng hạn như một hệ thống tập tin có cấu trúc log (log-structured file system).

Các đặc tính ghi có thể là một vấn đề đối với các khối lượng công việc ghi, đặc biệt là khi thực hiện I/O có kích thước nhỏ hơn kích thước khối bộ nhớ flash (thứ có thể lên đến 512 Kbyte). Điều này có thể gây ra hiện tượng *khuếch đại ghi* (write amplification), nơi phần còn lại của khối được sao chép đi nơi khác trước khi xóa, và do đó độ trễ cho ít nhất là chu kỳ xóa-ghi. Các ổ đĩa flash hiện đại giảm bớt vấn đề độ trễ này bằng cách cung cấp một bộ đệm ẩn trên đĩa (dựa trên RAM) được hỗ trợ bởi pin, sao cho các lệnh ghi có thể được buffer và ghi sau đó, ngay cả trong trường hợp mất điện.

Ổ đĩa flash cấp doanh nghiệp phổ biến nhất mà tôi từng sử dụng thực hiện tối ưu với các lệnh đọc 4 Kbyte và các lệnh ghi 1 Mbyte, do bố cục bộ nhớ flash. Các giá trị này thay đổi cho các ổ đĩa khác nhau và có thể được tìm thấy thông qua micro-benchmarking các kích thước I/O.

Do sự chênh lệch giữa các hoạt động gốc của flash và giao diện khối được để lộ, đã có chỗ cho sự cải thiện của hệ điều hành và hệ thống tập tin của nó. Lệnh TRIM là một ví dụ: nó báo cho SSD biết rằng một vùng không còn được sử dụng nữa, cho phép SSD dễ dàng tập hợp pool các khối trống của nó hơn, giảm thiểu khuếch đại ghi. (Đối với SCSI, điều này có thể được triển khai bằng cách sử dụng các lệnh UNMAP hoặc WRITE SAME; đối với ATA, lệnh DATA SET MANAGEMENT. Linux hỗ trợ tùy chọn mount `discard`, và lệnh fstrim(8).)

**Tuổi thọ (Lifespan)**
Có nhiều vấn đề khác nhau với bộ nhớ flash NAND dưới dạng môi trường lưu trữ, bao gồm burnout, mòn dữ liệu (data fade), và nhiễu loạn đọc (read disturbance) [Cornwell 12]. Những vấn đề này có thể được giải quyết bởi bộ điều khiển SSD, thứ có thể di chuyển dữ liệu để tránh các vấn đề. Những điều này thường được gọi là *wear leveling*, thứ rải các chu kỳ ghi qua các khối dữ liệu khác nhau để giảm thiểu việc mòn các khối riêng lẻ, và *memory overprovisioning*, thứ giữ lại các khối dư thừa để có thể được ánh xạ vào phục vụ khi cần thiết.

Trong khi các kỹ thuật này cải thiện tuổi thọ, SSD vẫn có một số lượng hữu hạn các chu kỳ ghi trên mỗi khối, tùy thuộc vào loại bộ nhớ flash và các tính năng giảm thiểu được nhà cung cấp sử dụng. Các ổ đĩa cấp doanh nghiệp sử dụng các chiến lược quản lý bộ nhớ để đạt được tốc độ chu kỳ ghi là 1 triệu và cao hơn. Các ổ đĩa cấp tiêu dùng dựa trên MLC có thể chỉ cung cấp 1,000 chu kỳ.

**Các bệnh lý (Pathologies)**
Dưới đây là một số bệnh lý SSD bộ nhớ flash cần lưu ý:
- **Các giá trị ngoại lai độ trễ do lão hóa:** và ổ SSD cố gắng hơn nữa để trích xuất dữ liệu chính xác (được kiểm tra bằng ECC).
- **Độ trễ cao hơn do phân mảnh:** (việc format lại có thể khắc phục điều này bằng cách xóa sạch các ánh xạ FTL).
- **Thông lượng thấp hơn nếu SSD triển khai nén nội bộ.**

Hãy kiểm tra các tài liệu của nhà cung cấp để biết các tính năng hiệu năng SSD và các vấn đề gặp phải.

#### 9.4.1.3 Bộ nhớ bền vững (Persistent Memory)
Bộ nhớ bền vững, dưới dạng DRAM được hỗ trợ bởi pin, được sử dụng cho bộ đệm ẩn ghi của bộ điều khiển lưu trữ. Hiệu năng của loại này có tốc độ nhanh hơn nhiều bậc độ lớn so với flash, nhưng chi phí của nó và tuổi thọ pin giới hạn đã hạn chế nó chỉ dành cho các mục đích sử dụng chuyên biệt.

Một loại bộ nhớ bền vững mới gọi là 3D XPoint, được phát triển bởi Intel và Micron, sẽ cho phép bộ nhớ bền vững được sử dụng cho nhiều ứng dụng hơn với mức giá/hiệu năng hấp dẫn nằm giữa DRAM và bộ nhớ flash. 3D XPoint hoạt động bằng cách lưu trữ các bit trong một mảng chéo có thể xếp chồng lên nhau, và có thể truy cập theo từng byte. Một sự so sánh hiệu năng của Intel đã báo cáo độ trễ truy cập ngẫu nhiên 14 micro giây so với 200 micro giây cho SSD 3D NAND [Hady 18]. 3D XPoint cũng cho thấy độ trễ nhất quán cho bài kiểm tra của họ, trong khi 3D NAND có phân phối độ trễ rộng hơn lên đến 3 mili giây.

3D XPoint đã được thương mại hóa từ năm 2017. Intel sử dụng tên thương hiệu Optane, và phát hành nó dưới dạng bộ nhớ bền vững Intel Optane trong một gói DIMM, và dưới dạng các ổ SSD Intel Optane.

### 9.4.2 Các giao diện (Interfaces)
Giao diện là giao thức được hỗ trợ bởi ổ đĩa để liên lạc với hệ thống, thường là thông qua một bộ điều khiển đĩa. Một bản tóm tắt ngắn gọn về các giao diện SCSI, SAS, SATA, FC, và NVMe như sau. Bạn sẽ cần kiểm tra các giao diện và băng thông được hỗ trợ hiện tại là gì, vì chúng thay đổi theo thời gian khi các thông số kỹ thuật mới được phát triển và áp dụng.

**SCSI**
Small Computer System Interface ban đầu là một bus vận chuyển song song, sử dụng nhiều đầu nối điện để truyền một byte dữ liệu cho mỗi chu kỳ clock. Phiên bản đầu tiên, SCSI-1 vào năm 1986, có chiều rộng bus dữ liệu là 8 bit, cho phép truyền một byte cho mỗi chu kỳ clock, và mang lại băng thông 5 Mbytes/s. Điều này được kết nối bằng cách sử dụng một đầu nối 50-pin Centronics C50. Các phiên bản SCSI sau này đã sử dụng các bus dữ liệu rộng hơn và nhiều chân cắm hơn cho các đầu nối, lên đến 80 chân, và các băng thông lên đến hàng trăm megabytes.

Bởi vì SCSI song song là một bus chia sẻ, nó có thể gặp phải các vấn đề hiệu năng do tranh chấp bus, ví dụ khi một bản sao lưu theo lịch trình làm bão hòa bus với I/O ưu tiên thấp. Các giải pháp khắc phục bao gồm các thiết bị ưu tiên thấp trên các bus hoặc bộ điều khiển SCSI của riêng chúng.

Xung nhịp của các bus song song cũng trở thành một vấn đề ở tốc độ cao hơn, cùng với các vấn đề khác (bao gồm giới hạn khoảng cách và nhu cầu cho các bộ kết thúc SCSI - SCSI terminator packs), thứ đã dẫn đến việc chuyển sang phiên bản nối tiếp: SAS.

**SAS**
Serial Attached SCSI được thiết kế như một vận chuyển điểm-tới-điểm tốc độ cao, tránh các vấn đề tranh chấp bus của SCSI song song. Đặc tả SAS-1 ban đầu là 3 Gbits/s (phát hành năm 2003), tiếp theo là SAS-2 hỗ trợ 6 Gbits/s (2009), SAS-3 hỗ trợ 12 Gbits/s (2012), và SAS-4 hỗ trợ 22.5 Gbit/s (2017). Các liên kết tập hợp (link aggregations) được hỗ trợ, sao cho nhiều cổng có thể kết hợp để mang lại băng thông cao hơn. Tốc độ truyền dữ liệu thực tế là 80% băng thông, do mã hóa 8b/10b.

Các tính năng SAS khác bao gồm cổng kép (dual porting) của các ổ đĩa để sử dụng với các đầu nối dự phòng và kiến trúc, I/O đa đường (I/O multipathing), các miền SAS, thay thế nóng (hot swapping), và hỗ trợ tương thích cho các ổ đĩa SATA. Những tính năng này đã khiến SAS trở nên phổ biến cho việc sử dụng trong doanh nghiệp, đặc biệt với các kiến trúc lưu trữ dự phòng.

**SATA**
Vì những lý do tương tự như SCSI và SAS, bus song song ATA (còn gọi là IDE) đã phát triển để trở thành giao diện Serial ATA. Được tạo ra vào năm 2003, SATA 1.0 hỗ trợ 1.5 Gbits/s; các phiên bản lớn sau này là SATA 2.0 hỗ trợ 3.0 Gbits/s (2004), và SATA 3.0 hỗ trợ 6.0 Gbits/s (2008). Các tính năng bổ sung đã được thêm vào trong các bản phát hành chính và phụ, bao gồm native command queueing (NCQ). SATA đã được sử dụng phổ biến cho các máy tính để bàn và laptop tiêu dùng.

**FC**
Fibre Channel (FC) là một giao diện chuẩn tốc độ cao, ban đầu chỉ dành cho cáp quang (do đó có tên như vậy) và sau đó hỗ trợ cả cáp đồng. FC thường được sử dụng trong các môi trường doanh nghiệp để tạo ra các mạng khu vực lưu trữ (SANs) nơi nhiều thiết bị lưu trữ có thể được kết nối tới nhiều máy chủ qua một Fibre Channel Fabric. Điều này mang lại khả năng mở rộng và khả năng truy cập cao hơn các giao diện khác, và tương tự như kết nối nhiều host qua một mạng. Và, giống như mạng, FC có thể liên quan đến việc sử dụng các *switches* để kết nối với nhau nhiều endpoints (máy chủ và lưu trữ). Việc phát triển một chuẩn Fibre Channel đã bắt đầu từ năm 1988 với các cải tiến tốc độ đầu tiên được phê duyệt bởi ANSI vào năm 1994 [FICA 20]. Đã có nhiều biến thể và tốc độ được cải thiện, với chuẩn Gen 7 256GFC mới nhất đạt tới 51,200 MB/s song công (full duplex) [FICA 18].

**NVMe**
Non-Volatile Memory express (NVMe) là một đặc tả bus PCIe cho các thiết bị lưu trữ. Thay vì kết nối các thiết bị lưu trữ tới một bộ điều khiển đĩa, một thiết bị NVMe tự nó là một card kết nối trực tiếp tới bus PCIe. Được tạo ra vào năm 2011, đặc tả NVMe đầu tiên là 1.0e (phát hành năm 2013), và mới nhất là 1.4 (2019) [NVMe 20]. Các tính năng mới hơn bao gồm nhiều tính năng đa dạng, ví dụ, các tính năng và lệnh quản lý nhiệt để tự kiểm tra, xác minh dữ liệu, và xóa sạch dữ liệu (giúp việc khôi phục dữ liệu là không thể). Băng thông của các card NVMe bị giới hạn bởi bus PCIe; PCIe phiên bản 4.0, được sử dụng phổ biến hiện nay, có băng thông một hướng là 31.5 Gbytes/s cho một liên kết x16 (x16 link width).

Một lợi thế của NVMe so với SAS và SATA truyền thống là sự hỗ trợ của nó cho nhiều hàng đợi phần cứng. Những hàng đợi này có thể được sử dụng từ cùng một CPU để thúc đẩy sự ấm áp của bộ đệm ẩn (cache warmth) (và với trình điều khiển lưu trữ đa hàng đợi của Linux, các khóa kernel cũng được tránh). Những hàng đợi này cũng cho phép đệm (buffering) nhiều hơn, hỗ trợ lên tới 64 nghìn lệnh trong mỗi hàng đợi, trong khi các ổ đĩa SAS và SATA điển hình bị giới hạn ở 256 và 32 lệnh tương ứng.

NVMe cũng hỗ trợ SR-IOV để cải thiện hiệu năng lưu trữ máy ảo (xem Chương 11, Điện toán đám mây, Mục 11.2, Ảo hóa phần cứng).

NVMe được sử dụng cho các thiết bị flash có độ trễ thấp, với độ trễ I/O kỳ vọng dưới 20 micro giây.

### 9.4.3 Các loại Lưu trữ (Storage Types)
Lưu trữ có thể được cung cấp cho một máy chủ theo nhiều cách; các phần sau đây mô tả bốn kiến trúc chung: các thiết bị đĩa, RAID, các mảng lưu trữ, và lưu trữ gắn mạng (NAS).

**Các thiết bị Đĩa (Disk Devices)**
Kiến trúc đơn giản nhất là một máy chủ với các đĩa nội bộ, được điều khiển riêng lẻ bởi hệ điều hành. Các đĩa kết nối tới một bộ điều khiển đĩa, thứ có mạch điện trên bo mạch chủ hoặc một card mở rộng, và cho phép các thiết bị đĩa được nhìn thấy và truy cập. Trong kiến trúc này, bộ điều khiển đĩa chỉ đơn thuần đóng vai trò như một đường dẫn sao cho hệ thống có thể liên lạc với đĩa. Một máy tính cá nhân hoặc laptop điển hình có một đĩa được gắn theo cách này cho lưu trữ sơ cấp.

Kiến trúc này là dễ phân tích nhất bằng cách sử dụng các công cụ hiệu năng, vì mỗi đĩa được hệ điều hành biết đến và có thể được quan sát một cách riêng biệt.

Một số bộ điều khiển đĩa hỗ trợ kiến trúc này, nơi nó được gọi là *just a bunch of disks* (JBOD).

**RAID**
Các bộ điều khiển đĩa nâng cao có thể cung cấp kiến trúc redundant array of independent disks (RAID) cho các thiết bị đĩa (ban đầu là *inexpensive disks* [Patterson 88]). RAID có thể trình diễn nhiều đĩa như là một đĩa ảo duy nhất, nhanh chóng và đáng tin cậy. Những bộ điều khiển này thường bao gồm một bộ nhớ trên bo mạch (RAM) để cải thiện hiệu năng đọc và ghi.

Việc cung cấp RAID bởi một card bộ điều khiển đĩa được gọi là *hardware* RAID. RAID cũng có thể được triển khai bởi phần mềm điều hành, nhưng phần cứng RAID đã được ưu tiên vì các tính toán checksum và parity tốn kém CPU có thể được thực hiện trên phần cứng chuyên dụng, cộng với phần cứng thường có một thiết bị pin dự phòng (BBU) cho khả năng phục hồi được cải thiện. Tuy nhiên, các bộ xử lý hiện đại đã tạo ra các CPU dư thừa theo các chu kỳ, làm giảm nhu cầu dời tải tính toán parity. Một số lượng lớn các giải pháp lưu trữ đã chuyển sang RAID phần mềm (ví dụ, sử dụng ZFS), thứ làm giảm độ phức tạp của phần cứng và cải thiện khả năng quan sát từ hệ điều hành. RAID phần mềm (hãy tưởng tượng một card RAID bị hỏng) cũng có thể dễ dàng hơn để sửa chữa so với RAID phần cứng (hãy tưởng tượng một card RAID bị hỏng và cần được thay thế bằng một bản sao giống hệt).

Các phần sau đây mô tả các đặc tính hiệu năng của RAID. Thuật ngữ *stripe* (sọc) thường được sử dụng: nó đề cập đến việc dữ liệu được nhóm thành các khối được ghi qua nhiều ổ đĩa (giống như vẽ một dải sọc qua tất cả chúng).

**Các loại RAID**
Nhiều loại RAID khác nhau có sẵn để đáp ứng các nhu cầu đa dạng về dung lượng, hiệu năng và độ tin cậy. Bản tóm tắt này tập trung vào các đặc tính hiệu năng được trình bày trong Bảng 9.3.

Bảng 9.3 Các loại RAID
| Cấp độ | Mô tả | Hiệu năng |
| --- | --- | --- |
| 0 (concat.) | Các ổ đĩa được lấp đầy từng cái một tại một thời điểm. | Cuối cùng cải thiện hiệu năng đọc ngẫu nhiên khi nhiều ổ đĩa có thể tham gia. |
| 0 (stripe) | Các ổ đĩa được sử dụng song song, chia nhỏ (striping) I/O qua nhiều ổ đĩa. | Kỳ vọng hiệu năng I/O ngẫu nhiên và tuần tự tốt nhất (tùy thuộc vào kích thước sọc và mẫu khối lượng công việc). |
| 1 (mirror) | Nhiều ổ đĩa (thường là hai) được nhóm lại, lưu trữ nội dung giống hệt nhau để dự phòng. | Hiệu năng đọc ngẫu nhiên và tuần tự tốt (có thể đọc từ tất cả các ổ đĩa đồng thời, tùy thuộc vào việc triển khai). Các lệnh ghi bị giới hạn bởi đĩa chậm nhất trong gương, và các chi phí thông lượng bị gấp đôi (hai lệnh ghi). |
| 10 | Một sự kết hợp của các sọc RAID-0 qua các nhóm ổ đĩa RAID-1, cung cấp dung lượng và sự dự phòng. | Các đặc tính hiệu năng tương tự như RAID-1 nhưng cho phép nhiều nhóm ổ đĩa hơn tham gia, giống như RAID-0, tăng băng thông. |
| 5 | Dữ liệu được lưu trữ dưới dạng các sọc qua nhiều ổ đĩa, cùng với thông tin parity bổ sung để dự phòng. | Hiệu năng ghi kém do chu kỳ đọc-sửa-ghi và các tính toán parity. |
| 6 | RAID-5 với hai cung từ parity cho mỗi sọc. | Tương tự như RAID-5 nhưng tệ hơn. |

Trong khi phân chia RAID-0 mang lại hiệu năng tốt nhất, nó không có sự dự phòng, khiến nó trở nên không thực tế cho hầu hết các trường hợp sử dụng sản xuất. Các ngoại lệ bao gồm các môi trường điện toán đám mây chịu lỗi nơi các thiết bị lưu trữ ảo được thay thế tự động, và các máy chủ lưu trữ cho dữ liệu không quan trọng chỉ dành cho caching.

**Khả năng quan sát (Observability)**
Như đã mô tả trước đó trong phần về mức sử dụng đĩa ảo, việc sử dụng các đĩa ảo được cung cấp bởi phần cứng có thể làm cho các công cụ quan sát trong hệ điều hành bị nhầm lẫn, vì chúng không thể thấy được các đĩa vật lý đang làm gì. Nếu RAID được cung cấp bởi phần mềm, các thiết bị đĩa vật lý riêng lẻ thường có thể được quan sát, và hệ điều hành sẽ quản lý chúng trực tiếp.

**Read-Modify-Write**
Khi dữ liệu được lưu trữ dưới dạng một sọc bao gồm một parity, như với RAID-5, việc ghi I/O có thể phát sinh thêm các lệnh đọc và thời gian tính toán I/O. Điều này là do các lệnh ghi nhỏ hơn kích thước sọc có thể yêu cầu toàn bộ sọc phải được đọc, các byte được sửa đổi, parity được tính toán lại, và sau đó toàn bộ sọc được ghi lại. Một sự tối ưu hóa cho RAID-5 có thể được sử dụng để tránh điều này: thay vì đọc toàn bộ sọc, chỉ các phần của sọc (các cung từ) được ghi lại là được đọc cùng với dữ liệu parity hiện có. Bằng một chuỗi các thao tác XOR, một parity mới có thể được tính toán và ghi lại cùng với các sọc đã sửa đổi.

Các lệnh ghi trải dài toàn bộ sọc có thể ghi đè lên các nội dung trước đó, mà không cần phải đọc chúng trước. Hiệu năng trong môi trường này có thể được cải thiện bằng cách cân bằng kích thước của sọc với kích thước I/O trung bình của các lệnh ghi, để giảm các chi phí I/O bổ sung.

**Caches**
Các bộ điều khiển đĩa triển khai RAID có thể giảm thiểu hiệu năng đọc-sửa-ghi bằng cách sử dụng bộ đệm ẩn ghi ngược. Những bộ đệm ẩn này nên có pin dự phòng, để trong trường hợp mất điện, chúng vẫn có thể hoàn thành các lệnh ghi buffer.

**Các tính năng bổ sung**
Hãy nhận biết rằng các card bộ điều khiển đĩa nâng cao có thể cung cấp các tính năng nâng cao có thể ảnh hưởng đến hiệu năng. Tốt nhất là bạn nên duyệt qua các tài liệu của nhà cung cấp để ít nhất nhận thức được những gì có thể đang diễn ra. Ví dụ, dưới đây là một vài tính năng từ các card Dell PERC 5 [Dell 20]:
- **Patrol read:** Cứ vài ngày một lần, tất cả các khối đĩa được đọc và các checksum của chúng được xác minh. Nếu các đĩa đang bận rộn phục vụ các yêu cầu, tài nguyên cấp cho chức năng patrol read sẽ bị giảm, để tránh tranh chấp với khối lượng công việc hệ thống.
- **Cache flush interval:** Thời gian tính theo giây giữa các lần flush dữ liệu bẩn trong bộ đệm ẩn xuống đĩa. Các khoảng thời gian dài hơn có thể giảm I/O đĩa do việc hủy bỏ ghi và các lệnh ghi kết hợp tốt hơn; tuy nhiên, chúng cũng có thể gây ra độ trễ đọc cao hơn trong các đợt flush lớn.

Cả hai tính năng này đều có thể có ảnh hưởng đáng kể đến hiệu năng.

**Storage Arrays (Mảng lưu trữ)**
Các mảng lưu trữ cho phép nhiều đĩa được kết nối tới hệ thống. Chúng sử dụng các bộ điều khiển đĩa nâng cao sao cho RAID có thể được cấu hình, và cuối cùng trình diễn một ổ đĩa lớn tới hệ điều hành. Các mảng này cũng thường có pin dự phòng, cho phép chúng vận hành trong chế độ ghi ngược. Một chính sách phổ biến là chuyển sang chế độ ghi xuyên qua nếu pin bị lỗi, thứ có thể được chú ý như một sự sụt giảm hiệu năng đột ngột do việc chờ đợi các ổ đĩa thực hiện các chu kỳ ghi-đọc-xác minh.

Một cân nhắc hiệu năng bổ sung là cách mảng lưu trữ được gắn tới hệ thống—thông thường là qua một card bộ điều khiển lưu trữ mở rộng. Card này, và phương thức vận chuyển giữa nó và mảng, sẽ có các giới hạn cho IOPS và thông lượng. Để cải thiện cả hiệu năng và độ tin cậy, các mảng lưu trữ thường có hai đường dẫn (dual-attached), nghĩa là chúng có thể được kết nối bằng hai dây cáp vật lý, tới một hoặc hai bộ điều khiển lưu trữ khác nhau.

**Network-Attached Storage (Lưu trữ gắn mạng)**
NAS được cung cấp tới máy chủ qua mạng hiện có thông qua một giao thức mạng, chẳng hạn như NFS, SMB/CIFS, hoặc iSCSI, thường từ các thiết bị NAS chuyên dụng. Đây là các hệ thống riêng biệt và nên được phân tích như vậy. Một số phân tích hiệu năng có thể được thực hiện trên khách hàng (client), để kiểm tra khối lượng công việc được áp dụng và các độ trễ I/O. Hiệu năng của mạng cũng trở thành một yếu tố, và các vấn đề có thể phát sinh từ tắc nghẽn mạng và độ trễ đa bước (multiple-hop latency).

### 9.4.4 Operating System Disk I/O Stack
Các thành phần và các tầng trong I/O stack đĩa của hệ điều hành tùy thuộc vào hệ điều hành, phiên bản, và các công nghệ phần cứng và phần mềm được sử dụng. Hình 9.7 mô tả một mô hình chung. Xem Chương 3, Hệ điều hành, cho một mô hình tương tự bao gồm cả ứng dụng.

(Hình 9.7 I/O stack đĩa chung)

**Block Device Interface**
Giao diện thiết bị khối được tạo ra trong Unix sơ khai để truy cập các thiết bị lưu trữ theo đơn vị khối 512 byte, và để cung cấp một bộ đệm ẩn thiết bị khối (buffer cache). Vai trò của buffer cache đã giảm bớt khi các bộ đệm ẩn hệ thống tập tin khác đã được đưa vào, mặc dù thuật ngữ này vẫn tồn tại trên Linux và được mô tả trong Chương 8, Hệ thống tập tin.

Unix đã cung cấp một đường dẫn để bỏ qua buffer cache, được gọi là *raw block device I/O* (hoặc chỉ là *raw I/O*), thứ có thể được sử dụng qua các tập tin thiết bị đặc biệt ký tự (xem Chương 3, Hệ điều hành). Những tập tin này không còn được sử dụng phổ biến theo mặc định trong Linux. Direct I/O hệ thống tập tin thì có phần khác biệt so với raw I/O, nhưng theo một số cách tương tự với tính năng hệ thống tập tin "direct I/O" được mô tả trong Chương 8, Hệ thống tập tin.

Giao diện I/O khối thường có thể được quan sát từ các công cụ hiệu năng hệ điều hành (iostat(1)). Nó cũng là một vị trí chung cho instrumentation tĩnh và có thể được khám phá bằng instrumentation động. Linux đã tăng cường khu vực này của kernel với các tính năng bổ sung.

**Linux**
Các thành phần chính của Linux block I/O stack được trình bày trong Hình 9.8.

(Hình 9.8 Linux I/O stack)

Linux đã nâng cường I/O khối với việc bổ sung I/O merging và các trình lập lịch I/O để cải thiện hiệu năng, các volume managers để nhóm các thiết bị, và một device mapper để tạo ra các thiết bị ảo.

**I/O merging**
Khi các yêu cầu I/O được tạo ra, Linux có thể gộp và kết hợp chúng như được trình bày trong Hình 9.9.

(Hình 9.9 Các loại I/O merging)

Việc này nhóm các I/O lại, làm giảm các chi phí CPU cho mỗi I/O trong kernel storage stack và chi phí trên đĩa, cải thiện thông lượng. Các thống kê cho các lần gộp front và back này khả dụng trong iostat(1). Sau khi gộp, I/O sau đó được lập lịch để phân phối tới các đĩa.

**I/O Schedulers (Trình lập lịch I/O)**
I/O được xếp hàng và lập lịch trong block layer hoặc bởi các trình lập lịch cổ điển (chỉ hiện diện trong các phiên bản Linux cũ hơn 5.0) hoặc bởi các trình lập lịch đa hàng đợi (multi-queue) mới hơn. Những trình lập lịch này có thể cải thiện hiệu năng bằng cách cho phép I/O được sắp xếp lại (hoặc lập lịch lại) để phân phối tối ưu. Điều này có thể cải thiện và mang lại hiệu năng cân bằng hơn, đặc biệt đối với các thiết bị có độ trễ I/O cao (các đĩa quay).

Các trình lập lịch cổ điển bao gồm:
- **Noop:** Trình lập lịch này không thực hiện việc lập lịch (noop là viết tắt của "không-thao-tác" - no-operation) và có thể được sử dụng khi chi phí của việc lập lịch được coi là không cần thiết (ví dụ, trong một đĩa RAM).
- **Deadline:** Cố gắng thực thi một thời hạn cuối (deadline) cho độ trễ, ví dụ, các mốc thời gian đọc và ghi tính theo mili giây có thể được chọn. Điều này có thể hữu ích cho các hệ thống thời gian thực, nơi tính xác định (determinism) là mong muốn. Nó cũng có thể giúp tránh hiện tượng *đói tài nguyên* (starvation): nơi một yêu cầu I/O bị chết đói tài nguyên đĩa do các I/O mới phát ra liên tục nhảy vào hàng đợi, dẫn đến một giá trị ngoại lai độ trễ. Sự chết đói có thể xảy ra do các lần đọc tranh chấp với các lần ghi, và vì một thang máy quay và seek từ vùng này của đĩa sang vùng khác. Trình lập lịch deadline giải quyết vấn đề này, một phần, bằng cách sử dụng ba hàng đợi riêng biệt cho I/O: đọc FIFO, ghi FIFO, và đã sắp xếp [Love 10].
- **CFQ:** Trình lập lịch completely fair queueing phân bổ các lát thời gian I/O cho các tiến trình, tương tự như lập lịch CPU, để sử dụng tỷ lệ công bằng các tốc độ I/O. Nó cũng cho phép các mức ưu tiên và các lớp được thiết lập cho các tiến trình người dùng, thông qua lệnh ionice(1).

Một vấn đề với các trình lập lịch cổ điển là việc họ sử dụng một khóa duy nhất, được bảo vệ bởi một khóa đơn, thứ đã trở thành một nút thắt cổ chai ở tốc độ I/O cao. Hàng đợi đa hàng đợi (blk-mq, được thêm vào Linux 3.13) giải quyết vấn đề này bằng cách sử dụng các hàng đợi phục vụ riêng biệt cho mỗi CPU, và nhiều hàng đợi phân phối cho các thiết bị. Điều này mang lại hiệu năng tốt hơn và độ trễ thấp hơn cho I/O so với các trình lập lịch cổ điển, khi các yêu cầu có thể được xử lý song song và trên cùng một CPU nơi I/O được khởi tạo. Điều này là cần thiết để hỗ trợ bộ nhớ flash và các thiết bị lưu trữ khác có khả năng xử lý hàng triệu IOPS [Corbet 13b].

Các trình lập lịch đa hàng đợi bao gồm:
- **None:** Không xếp hàng.
- **BFQ:** Trình lập lịch budget fair queueing, tương tự như CFQ, nhưng phân bổ băng thông cũng như thời gian I/O. Nó tạo ra một hàng đợi cho mỗi tiến trình đang thực hiện I/O, và duy trì một ngân sách cho mỗi hàng đợi được đo lường bằng các cung từ. Có một hệ thống ngân sách toàn hệ thống để ngăn chặn một tiến trình chiếm giữ thiết bị quá lâu. BFQ hỗ trợ cgroups.
- **mq-deadline:** Một phiên bản blk-mq của trình lập lịch deadline (đã mô tả trước đó).
- **Kyber:** Một trình lập lịch điều chỉnh độ dài hàng đợi đọc và ghi dựa trên hiệu năng so với các độ trễ đọc và ghi mục tiêu. Đây là một trình lập lịch đơn giản chỉ có hai tham số có thể tinh chỉnh: độ trễ đọc mục tiêu (read_lat_nsec) và độ trễ ghi mục tiêu (write_lat_nsec). Kyber đã cho thấy các độ trễ I/O được cải thiện trong đám mây Netflix, nơi nó được sử dụng theo mặc định.

Kể từ Linux 5.0, các trình lập lịch đa hàng đợi là mặc định (các trình lập lịch cổ điển không còn được bao gồm).

Các trình lập lịch I/O được tài liệu hóa chi tiết trong mã nguồn Linux dưới Documentation/block. Sau khi lập lịch I/O, yêu cầu được đặt trên hàng đợi thiết bị khối để phát hành cho thiết bị.

---

## 9.5 Phương pháp luận (Methodology)
Phần này mô tả các phương pháp luận và bài tập khác nhau cho phân tích và tinh chỉnh I/O đĩa. Các chủ đề được tóm tắt trong Bảng 9.4.

Bảng 9.4 Các phương pháp luận hiệu năng đĩa
| Mục | Phương pháp luận | Các loại |
| --- | --- | --- |
| 9.5.1 | Phương pháp công cụ | Phân tích quan sát |
| 9.5.2 | Phương pháp USE | Phân tích quan sát |
| 9.5.3 | Giám sát hiệu năng | Phân tích quan sát, quy hoạch dung lượng |
| 9.5.4 | Đặc tính hóa khối lượng công việc | Phân tích quan sát, quy hoạch dung lượng |
| 9.5.5 | Phân tích độ trễ | Phân tích quan sát |
| 9.5.6 | Tinh chỉnh hiệu năng tĩnh | Phân tích quan sát, quy hoạch dung lượng |
| 9.5.7 | Tinh chỉnh bộ đệm ẩn | Phân tích quan sát, tinh chỉnh |
| 9.5.8 | Các kiểm soát tài nguyên | Tinh chỉnh |
| 9.5.9 | Micro-benchmarking | Phân tích thực nghiệm |
| 9.5.10 | Scaling | Quy hoạch dung lượng, tinh chỉnh |

Xem Chương 2, Phương pháp luận, để biết thêm về các phương pháp luận này và phần giới thiệu cho nhiều nội dung trong số đó. Những phương pháp này có thể được tuân theo riêng lẻ hoặc được sử dụng kết hợp. Khi điều tra các vấn đề về đĩa, gợi ý của tôi là sử dụng các chiến lược sau, theo thứ tự này: phương pháp USE, phân tích độ trễ, micro-benchmarking, phân tích hiệu năng tĩnh, và truy vết sự kiện.

Mục 9.6, Các công cụ quan trắc, giới thiệu các công cụ hệ điều hành để áp dụng các phương pháp này.

### 9.5.1 Phương pháp Công cụ (Tools Method)
Phương pháp công cụ là một quá trình lặp đi lặp lại qua các công cụ có sẵn, kiểm tra các chỉ số then chốt mà chúng cung cấp. Mặc dù là một phương pháp đơn giản, nó có thể bỏ sót các vấn đề mà các công cụ của bạn vô tình cung cấp thông tin kém hoặc không có khả năng hiển thị, và nó có thể tiêu tốn nhiều thời gian để thực hiện.

Đối với đĩa, phương pháp công cụ có thể bao gồm việc kiểm tra những điều sau (cho Linux):
- **iostat:** Sử dụng chế độ mở rộng để tìm kiếm các đĩa bận rộn (trên 60% mức sử dụng), thời gian dịch vụ trung bình cao (trên 10 ms), và IOPS cao (tùy thuộc vào thiết bị).
- **iotop/biotop:** Để xác định tiến trình nào đang gây ra I/O đĩa.
- **biolatency:** Để kiểm tra phân phối độ trễ I/O đĩa dưới dạng một biểu đồ histogram, tìm kiếm các phân phối đa chế độ và các giá trị ngoại lai độ trễ (trên 100 ms).
- **biosnoop:** Để kiểm tra các I/O đĩa riêng lẻ.
- **perf(1)/BCC/bpftrace:** Cho phân tích tùy chỉnh bao gồm xem các stack tiến trình người dùng và kernel đã phát ra I/O.
- **Các công cụ đặc thù cho bộ điều khiển đĩa:** (từ nhà cung cấp).

Nếu tìm thấy vấn đề, hãy kiểm tra tất cả các trường từ các công cụ có sẵn để tìm hiểu thêm ngữ cảnh. Xem Mục 9.6, Các công cụ quan trắc, để biết thêm về từng công cụ. Các phương pháp luận khác cũng có thể được sử dụng, thứ có thể giúp xác định thêm các loại vấn đề.

### 9.5.2 Phương pháp USE
Phương pháp USE là để nhận diện các nút thắt cổ chai và các lỗi trên tất cả các thành phần, sớm trong một cuộc điều tra hiệu năng. Các phần sau đây mô tả cách áp dụng phương pháp USE cho các thiết bị đĩa và bộ điều khiển, đồng thời hiển thị các công cụ để đo lường các chỉ số cụ thể.

**Các thiết bị đĩa**
Cho mỗi thiết bị đĩa, kiểm tra:
- **Mức sử dụng (Utilization):** Thời gian thiết bị bận rộn.
- **Độ bão hòa (Saturation):** Mức độ I/O đang chờ trong một hàng đợi.
- **Các lỗi (Errors):** Các lỗi thiết bị.

Các lỗi có thể được kiểm tra trước tiên. Đôi khi chúng bị bỏ qua vì các chức năng hệ thống vẫn hoạt động chính xác—mặc dù chậm hơn—bất chấp các lỗi đĩa: các đĩa thường được cấu hình trong một pool RAID dự phòng được thiết kế để chịu được một số lỗi. Ngoài các số lượng lỗi đĩa tiêu chuẩn, một loạt các bộ đếm lỗi khác có thể được truy xuất qua các công cụ đặc biệt (ví dụ, SMART data).

Nếu các đĩa là các đĩa vật lý, mức sử dụng nên dễ dàng tìm thấy. Nếu chúng là các đĩa ảo, mức sử dụng có thể không phản ánh những gì các đĩa vật lý đang làm. Xem Mục 9.3.9, Mức sử dụng, để biết thêm thảo luận về vấn đề này.

**Các bộ điều khiển Đĩa**
Cho mỗi bộ điều khiển đĩa, kiểm tra:
- **Mức sử dụng:** Thông lượng hiện tại so với tối đa, và cùng một chỉ số cho tốc độ thao tác (thao tác mỗi giây). Các thao tác bao gồm đọc/ghi và các lệnh đĩa khác. Thông lượng hoặc tốc độ thao tác cũng có thể bị giới hạn bởi vận chuyển kết nối bộ điều khiển tới hệ thống, giống như nó có thể bị giới hạn bởi vận chuyển từ bộ điều khiển tới các đĩa riêng lẻ. Mỗi phương thức vận chuyển cũng nên được coi như là một tài nguyên.
- **Độ bão hòa:** Mức độ I/O đang chờ do bão hòa bộ điều khiển.
- **Các lỗi:** Các lỗi bộ điều khiển.

Ở đây chỉ số mức sử dụng không được định nghĩa theo thời gian, mà theo các giới hạn của card bộ điều khiển đĩa: thông lượng (byte mỗi giây) và tốc độ thao tác (thao tác mỗi giây). Các thao tác bao gồm đọc/ghi và các lệnh đĩa khác. Thông lượng hoặc tốc độ thao tác cũng có thể bị giới hạn bởi phương thức vận chuyển kết nối bộ điều khiển đĩa tới hệ thống, giống như nó có thể bị giới hạn bởi vận chuyển từ bộ điều khiển tới các đĩa riêng lẻ. Mỗi phương thức vận chuyển cũng nên được coi là một tài nguyên.

Bạn có thể thấy rằng các công cụ quan sát (ví dụ, iostat(1) của Linux) không cung cấp các chỉ số cho mỗi bộ điều khiển đĩa. Có các cách giải quyết cho vấn đề này: nếu hệ thống chỉ có một bộ điều khiển, bạn có thể xác định IOPS và thông lượng của bộ điều khiển bằng cách cộng tổng các chỉ số đó cho tất cả các đĩa. Nếu hệ thống có nhiều bộ điều khiển, bạn sẽ cần xác định đĩa nào thuộc về bộ điều khiển nào, và cộng tổng các chỉ số tương ứng.

Hiệu năng của các bộ điều khiển đĩa và các phương thức vận chuyển thường bị bỏ qua. May mắn thay, chúng không phải là nguồn gốc phổ biến của các nút thắt cổ chai hệ thống, vì dung lượng của chúng thường vượt xa dung lượng của các đĩa gắn kèm. Nếu tổng thông lượng đĩa hoặc IOPS luôn dừng lại ở một tốc độ nhất định, ngay cả dưới các khối lượng công việc khác nhau, đây có thể là một manh mối cho thấy các bộ điều khiển đĩa hoặc các phương thức vận chuyển thực sự đang gây ra các vấn đề.

### 9.5.3 Giám sát Hiệu năng (Performance Monitoring)
Giám sát hiệu năng có thể xác định các vấn đề đang hoạt động và các mẫu hành vi theo thời gian. Các chỉ số then chốt cho I/O đĩa là:
- Mức sử dụng đĩa.
- Thời gian phản hồi.

Mức sử dụng đĩa ở mức 100% cho nhiều giây là rất có thể là một vấn đề. Tuy nhiên, bất kỳ giá trị sử dụng nào trên 60% cũng có thể gây ra hiệu năng kém do việc tăng hàng đợi. Giá trị cho "bình thường" hay "tệ" phụ thuộc vào khối lượng công việc, môi trường, và các yêu cầu về độ trễ của bạn. Nếu bạn không chắc chắn, micro-benchmarks về các đĩa bận rộn và các đĩa rảnh rỗi đã biết có thể được thực hiện để cho thấy khối lượng công việc có thể bị ảnh hưởng như thế nào bởi mức sử dụng đĩa. Xem Mục 9.8, Thực nghiệm.

Các chỉ số này nên được kiểm tra trên cơ sở từng đĩa, để tìm kiếm các đĩa không cân bằng hoặc một đĩa duy nhất chậm chạp. Chỉ số thời gian phản hồi có thể được giám sát dưới dạng giá trị trung bình cho mỗi giây và có thể bao gồm các giá trị khác chẳng hạn như tối đa và độ lệch chuẩn. Lý tưởng nhất, bạn có thể kiểm tra phân phối đầy đủ của thời gian phản hồi, ví dụ bằng cách sử dụng một biểu đồ histogram hoặc bản đồ nhiệt, để tìm kiếm các giá trị ngoại lai và các mẫu khác.

Nếu hệ thống áp đặt các kiểm soát tài nguyên I/O đĩa, các thống kê có thể được bao gồm để chỉ ra liệu và khi nào những thứ này đang được sử dụng. Độ trễ và thời gian phản hồi cũng có thể được ghi lại cho từng loại thao tác (đọc, ghi, v.v.).

Mức sử dụng và thời gian phản hồi nên hiển thị kết quả của đĩa, bao gồm IOPS và thông lượng, cung cấp dữ liệu quan trọng cho việc sử dụng trong quy hoạch dung lượng (xem Mục tiếp theo và Mục 9.5.10, Scaling).

### 9.5.4 Đặc tính hóa Khối lượng công việc (Workload Characterization)
Đặc tính hóa tải được áp dụng là một bài tập quan trọng trong quy hoạch dung lượng, benchmarking, và mô phỏng khối lượng công việc. Nó cũng có thể dẫn đến một số cải thiện hiệu năng lớn nhất bằng cách xác định các công việc không cần thiết có thể được loại bỏ.

Sau đây là các thuộc tính cơ bản để đặc tính hóa khối lượng công việc I/O đĩa:
- Tốc độ I/O.
- Thông lượng I/O.
- Kích thước I/O.
- Tỷ lệ đọc/ghi.
- Truy cập offset tập tin ngẫu nhiên so với tuần tự.

Ngẫu nhiên so với tuần tự, tỷ lệ đọc/ghi, và kích thước I/O đã được mô tả trong Mục 9.3, Các khái niệm. Tốc độ I/O (IOPS) và thông lượng I/O đã được định nghĩa trong Mục 9.1, Thuật ngữ.

Các đặc tính này có thể thay đổi theo từng giây, đặc biệt đối với các ứng dụng và các hệ thống tập tin buffer và flush các lệnh ghi theo các khoảng thời gian. Để đặc tính hóa khối lượng công việc tốt hơn, hãy thu thập các giá trị tối đa cũng như các giá trị trung bình. Tốt hơn nữa, hãy kiểm tra toàn bộ phân phối các giá trị theo thời gian.

Dưới đây là một mô tả khối lượng công việc ví dụ, để chỉ ra cách các thuộc tính này có thể được diễn đạt cùng nhau:

> Các đĩa hệ thống có một khối lượng công việc đọc ngẫu nhiên nhẹ, trung bình 350 IOPS với thông lượng 3 Mbytes/s, chạy ở mức 96% đọc. Các đợt bùng phát ngắn hạn không liên tục của các lệnh ghi tuần tự, kéo dài từ 2 đến 5 giây, thứ đẩy các đĩa tới mức tối đa 4,800 IOPS và 560 Mbytes/s. Các lệnh đọc có kích thước khoảng 8 Kbytes, và các lệnh ghi khoảng 128 Kbytes.

Ngoài việc mô tả các đặc tính trên toàn hệ thống, chúng cũng có thể được sử dụng để mô tả các khối lượng công việc đĩa theo từng bộ điều khiển I/O.

**Đặc tính hóa Khối lượng công việc Nâng cao / Checklist**
Các chi tiết bổ sung có thể được bao gồm để đặc tính hóa khối lượng công việc. Những điều này đã được liệt kê ở đây dưới dạng các câu hỏi để cân nhắc, thứ cũng có thể phục vụ như một checklist khi nghiên cứu thấu đáo các vấn đề về đĩa:
- IOPS trên toàn hệ thống là bao nhiêu? Cho mỗi đĩa? Cho mỗi bộ điều khiển?
- Thông lượng trên toàn hệ thống là bao nhiêu? Cho mỗi đĩa? Cho mỗi bộ điều khiển?
- Những ứng dụng hoặc người dùng nào đang sử dụng các đĩa?
- Những hệ thống tập tin hoặc các tập tin nào đang được truy cập?
- Có bất kỳ lỗi nào gặp phải không? Chúng có phải do các yêu cầu không hợp lệ, hay các vấn đề trên đĩa không?
- Mức độ cân bằng của I/O qua các đĩa khả dụng như thế nào?
- IOPS cho mỗi vận chuyển bus liên quan là bao nhiêu?
- Thông lượng cho mỗi vận chuyển bus liên quan là bao nhiêu?
- Những lệnh đĩa không truyền tải dữ liệu nào đang được phát ra?
- Tại sao I/O đĩa được phát ra (kernel call path)?
- Mức độ ứng dụng-đồng bộ của I/O đĩa là bao nhiêu?
- Phân phối của các thời gian I/O đến là gì?

Các câu hỏi về IOPS và thông lượng có thể được đặt ra cho các lệnh đọc và lệnh ghi một cách riêng biệt. Bất kỳ câu hỏi nào cũng có thể được kiểm tra theo thời gian, để tìm kiếm các giá trị tối đa, tối thiểu, và các biến đổi dựa trên thời gian. Đồng thời xem Chương 2, Các phương pháp luận, Mục 2.5.11, Đặc tính hóa khối lượng công việc, thứ cung cấp một bản tóm tắt cấp cao hơn về các đặc tính cần đo lường (ai, tại sao, cái gì, như thế nào).

**Đặc tính hóa Hiệu năng (Performance Characterization)**
Danh sách đặc tính hóa khối lượng công việc trước đó kiểm tra tải được áp dụng. Sau đây kiểm tra hiệu năng kết quả:
- Mỗi đĩa bận rộn như thế nào (mức sử dụng)?
- Mỗi đĩa bị bão hòa như thế nào (đợi hàng đợi)?
- Thời gian dịch vụ I/O trung bình là bao nhiêu?
- Thời gian chờ I/O trung bình là bao nhiêu?
- Có bất kỳ đĩa nào có độ trễ cao không?
- Phân phối đầy đủ của độ trễ I/O là gì?
- Các kiểm soát tài nguyên hệ thống, chẳng hạn như I/O throttling, có hiện diện và đang hoạt động không?
- Độ trễ của các lệnh đĩa không truyền tải dữ liệu là bao nhiêu?

**Event Tracing (Truy vết Sự kiện)**
Các công cụ truy vết có thể được sử dụng để ghi lại tất cả các thao tác đĩa và các chi tiết vào một bản nhật ký để phân tích sau này (ví dụ, Mục 9.6.7, biosnoop). Điều này có thể bao gồm ID đĩa, I/O hoặc loại lệnh, offset, kích thước, và các dấu thời gian bắt đầu và hoàn thành, độ trễ I/O có thể được tính toán (hoặc nó có thể đã được bao gồm trực tiếp trong bản nhật ký). Bằng cách nghiên cứu chuỗi các yêu cầu và hoàn thành, I/O được sắp xếp lại bởi thiết bị cũng có thể được nhận diện. Trong khi các công cụ vết I/O có thể là công cụ tối thượng cho việc đặc tính hóa khối lượng công việc, trong thực tế nó có thể gây ra chi phí đáng kể để lưu và xử lý hàng triệu thao tác đĩa. Nếu việc ghi các lệnh ghi vào vết sự kiện được bao gồm trong cùng một vết, nó có thể không chỉ làm ô nhiễm vết mà còn tạo ra một vòng lặp phản hồi và một vấn đề hiệu năng.

### 9.5.5 Phân tích Độ trễ (Latency Analysis)
Phân tích độ trễ liên quan đến việc đào sâu hơn vào hệ thống để tìm ra nguồn gốc của độ trễ. Với các đĩa, việc này thường sẽ kết thúc tại giao diện đĩa: thời gian giữa một yêu cầu I/O và sự hoàn thành. Nếu điều này khớp với độ trễ I/O tại mức ứng dụng, thông thường là an toàn để giả định rằng I/O đĩa bắt nguồn từ các đĩa, cho phép bạn tập trung cuộc điều tra của mình vào chúng. Nếu độ trễ khác nhau, việc đo lường nó tại các tầng khác nhau của stack hệ thống vận hành sẽ xác định nguồn gốc.

Hình 9.10 mô tả một I/O stack chung, với độ trễ được hiển thị tại các tầng khác nhau của hai giá trị ngoại lai I/O, A và B.

Độ trễ của I/O A là tương tự tại mỗi tầng từ ứng dụng xuống tới các trình điều khiển đĩa. Các điểm tương quan này tới các đĩa (hoặc trình điều khiển đĩa) là nguyên nhân gây ra độ trễ. Điều này có thể được suy ra nếu các tầng được đo lường một cách độc lập, dựa trên các giá trị độ trễ tương tự giữa chúng.

Độ trễ của B dường như bắt nguồn tại tầng hệ thống tập tin (khóa hoặc hàng đợi?), với độ trễ I/O tại các tầng thấp hơn đóng góp ít thời gian hơn đáng kể. Hãy nhận biết rằng các tầng khác nhau của stack có thể làm thổi phồng hoặc giảm bớt I/O, nghĩa là kích thước, số lượng và độ trễ sẽ khác nhau từ tầng này sang tầng tiếp theo. Ví dụ B có thể là một trường hợp chỉ quan sát thấy một I/O ở các tầng thấp hơn (10 ms), nhưng không tính được các I/O liên quan khác đã xảy ra để phục vụ cùng một hệ thống tập tin I/O (ví dụ, siêu dữ liệu).

Độ trễ tại mỗi tầng có thể được trình bày dưới dạng:
- **Trung bình I/O theo khoảng thời gian:** Như thường được báo cáo bởi các công cụ hệ điều hành.
- **Phân phối I/O đầy đủ:** Dưới dạng biểu đồ histogram hoặc bản đồ nhiệt; xem Mục 9.7.3, Bản đồ nhiệt độ trễ.
- **Các giá trị độ trễ cho mỗi I/O:** Xem phần Truy vết sự kiện ở trước đó.

Hai cái cuối cùng là hữu ích cho việc theo dõi nguồn gốc của các giá trị ngoại lai và có thể giúp xác định các trường hợp nơi I/O đã bị chia tách hoặc kết hợp.

(Hình 9.10 Phân tích độ trễ stack)

### 9.5.6 Tinh chỉnh Hiệu năng Tĩnh (Static Performance Tuning)
Tinh chỉnh hiệu năng tĩnh tập trung vào các vấn đề của môi trường đã cấu hình. Cho hiệu năng đĩa, hãy kiểm tra các khía cạnh sau của cấu hình tĩnh:
- Có bao nhiêu đĩa hiện diện? Thuộc loại nào (ví dụ: SMR, MLC)? Kích thước?
- Phiên bản của firmware đĩa là gì?
- Có bao nhiêu bộ điều khiển đĩa hiện diện? Thuộc loại giao diện nào?
- Các card bộ điều khiển đĩa có được kết nối tới các khe cắm tốc độ cao không?
- Có bao nhiêu đĩa được kết nối tới mỗi HBA?
- Nếu các pin/tụ điện dự phòng đĩa/bộ điều khiển hiện diện, trạng thái mức điện của chúng là gì?
- Phiên bản của firmware bộ điều khiển đĩa là gì?
- RAID có được cấu hình không? Chính xác như thế nào, bao gồm cả độ rộng sọc?
- Multipathing (đa đường dẫn) có sẵn và được cấu hình không?
- Phiên bản trình điều khiển thiết bị đĩa là gì?
- Kích thước bộ nhớ chính của máy chủ là bao nhiêu? Được sử dụng bởi page cache và buffer cache như thế nào?
- Có bất kỳ lỗi hệ điều hành/bản vá nào cho bất kỳ thiết bị lưu trữ nào không?
- Có các kiểm soát tài nguyên nào đang được sử dụng cho I/O đĩa không?

Hãy nhận thức rằng các lỗi hiệu năng có thể tồn tại trong các trình điều khiển thiết bị và firmware, thứ lý tưởng nhất là được khắc phục bởi các bản cập nhật từ nhà cung cấp.

Việc trả lời những câu hỏi này có thể tiết lộ các lựa chọn cấu hình đã bị bỏ qua. Đôi khi một hệ thống đã được cấu hình cho một khối lượng công việc, và sau đó được chuyển mục đích cho một khối lượng công việc khác. Chiến lược này sẽ nhắc nhở bạn xem xét lại những lựa chọn đó.

Trong khi làm việc với tư cách là trưởng bộ phận hiệu năng cho sản phẩm lưu trữ ZFS của Sun, khiếu nại về hiệu năng phổ biến nhất mà tôi nhận được là do lỗi cấu hình: sử dụng một pool gồm 12 đĩa JBOD của RAID-Z2 (sọc rộng). Cấu hình này mang lại độ tin cậy tốt nhưng hiệu năng IOPS không ấn tượng, tương tự như hiệu năng của một đĩa đơn. Tôi đã học được cách hỏi các chi tiết cấu hình trước tiên (thường là qua điện thoại) trước khi dành thời gian đăng nhập vào hệ thống và kiểm tra độ trễ I/O.

### 9.5.7 Tinh chỉnh Bộ đệm ẩn (Cache Tuning)
Có thể có nhiều bộ đệm ẩn khác nhau trong hệ thống, bao gồm mức ứng dụng, hệ thống tập tin, bộ điều khiển đĩa, và chính đĩa. Một danh sách các bộ đệm ẩn đã được bao gồm trong Mục 9.3.3, Caching. Tóm lại, hãy kiểm tra xem các bộ đệm ẩn đó có hiện diện không, kiểm tra xem chúng có đang hoạt động không, kiểm tra xem chúng thực hiện tốt như thế nào (tỷ lệ trúng), và sau đó tinh chỉnh khối lượng công việc cho bộ đệm ẩn và tinh chỉnh bộ đệm ẩn cho khối lượng công việc.

### 9.5.8 Các kiểm soát tài nguyên (Resource Controls)
Hệ điều hành có thể cung cấp các kiểm soát cho việc phân bổ tài nguyên I/O đĩa cho các tiến trình hoặc các nhóm tiến trình. Những điều này có thể bao gồm các giới hạn cố định cho IOPS và thông lượng, hoặc các phần của I/O đĩa linh hoạt hơn. Xem Mục 9.9, Tinh chỉnh, cho các ví dụ.

### 9.5.9 Kiểm thử vi mô (Micro-Benchmarking)
Micro-benchmarking I/O đĩa đã được giới thiệu trong Chương 8, Hệ thống tập tin, nơi giải thích sự khác biệt giữa việc kiểm tra hiệu năng hệ thống tập tin I/O và kiểm tra đĩa I/O, thứ thường có nghĩa là kiểm tra qua hệ điều hành bằng cách sử dụng các đường dẫn thiết bị thô, đặc biệt là bypass tất cả các bộ đệm ẩn của hệ thống tập tin (bao gồm caching, buffering, I/O splitting, I/O coalescing, chi phí đường dẫn mã, và các khác biệt ánh xạ offset).

Các yếu tố cho micro-benchmarking bao gồm:
- **Hướng:** Đọc hoặc ghi.
- **Mẫu offset đĩa:** Ngẫu nhiên hoặc tuần tự.
- **Dải offset:** Toàn bộ đĩa hoặc các dải chặt chẽ (ví dụ: chỉ offset 0).
- **Kích thước I/O:** 512 byte (tối thiểu điển hình) lên đến 1 Mbyte.
- **Tính song song:** Số lượng I/O trong hàng đợi, hoặc số lượng luồng thực hiện I/O.
- **Số lượng thiết bị:** Các bài kiểm tra đĩa đơn, hoặc nhiều đĩa (để khám phá bộ điều khiển và các giới hạn bus).

Hai phần tiếp theo chỉ ra cách các yếu tố này có thể được kết hợp để kiểm tra đĩa và hiệu năng bộ điều khiển đĩa. Xem Mục 9.8, Thực nghiệm, để biết chi tiết về các công cụ cụ thể có thể được sử dụng để thực hiện những bài kiểm tra này.

**Các đĩa**
Micro-benchmarking có thể được thực hiện trên cơ sở mỗi đĩa để xác định những điều sau, cùng với các khối lượng công việc được gợi ý:
- **Thông lượng đĩa tối đa (Mbytes mỗi giây):** Các lệnh đọc 128 Kbyte hoặc 1 Mbyte, tuần tự.
- **Tốc độ thao tác đĩa tối đa (IOPS):** các lệnh đọc 512-byte, offset 0 duy nhất.
- **IOPS đọc ngẫu nhiên đĩa tối đa:** các lệnh đọc 512-byte, các offset ngẫu nhiên.
- **Hồ sơ độ trễ đọc (độ trễ trung bình tính theo micro giây):** Các lệnh đọc tuần tự, lặp lại cho 512 byte, 1K, 2K, 4K, và cứ thế tiếp tục.
- **Hồ sơ độ trễ I/O ngẫu nhiên (độ trễ trung bình tính theo micro giây):** Các lệnh đọc 512-byte, lặp lại cho sọc offset đầy đủ, bắt đầu với các offset duy nhất, cho tới toàn bộ sọc.

Các bài kiểm tra này có thể được lặp lại cho các lệnh ghi. Việc sử dụng "offset 0 duy nhất" là nhằm đệm ẩn dữ liệu trong bộ đệm ẩn trên đĩa, sao cho thời gian truy cập bộ đệm ẩn đó có thể được đo lường.

**Các bộ điều khiển đĩa**
Các bộ điều khiển đĩa có thể được micro-benchmark bằng cách áp dụng một khối lượng công việc cho nhiều đĩa, được thiết kế để chạm tới các giới hạn trong bộ điều khiển. Những bài kiểm tra này có thể được thực hiện bằng cách sử dụng các bài kiểm tra sau đây, cùng với các khối lượng công việc được gợi ý cho các đĩa:
- **Thông lượng bộ điều khiển tối đa (Mbytes mỗi giây):** Các lệnh đọc 128 Kbyte, offset 0 duy nhất.
- **Tốc độ thao tác bộ điều khiển tối đa (IOPS):** Các lệnh đọc 512-byte, offset 0 duy nhất.

Áp dụng khối lượng công việc cho các đĩa từng cái một, quan sát các giới hạn. Có thể mất hơn một chục đĩa để tìm thấy giới hạn trong một bộ điều khiển đĩa.

### 9.5.10 Scaling (Mở rộng)
Các đĩa và các bộ điều khiển đĩa có các giới hạn thông lượng và IOPS, thứ có thể được trình diễn qua micro-benchmarking như đã mô tả trước đó. Tinh chỉnh có thể cải thiện hiệu năng chỉ tới những giới hạn này. Nếu cần thêm hiệu năng đĩa, và các chiến lược khác chẳng hạn như caching không hoạt động, các đĩa sẽ cần được mở rộng.

Dưới đây là một phương pháp đơn giản, dựa trên quy hoạch dung lượng của tài nguyên:
1. Xác định khối lượng công việc đĩa mục tiêu, xét theo thông lượng và IOPS. Nếu đây là một hệ thống mới, hãy xem Chương 2, Các phương pháp luận, Mục 2.7, Quy hoạch dung lượng. Nếu hệ thống đã có một khối lượng công việc, hãy diễn đạt dân số người dùng xét theo thông lượng đĩa và IOPS hiện tại, và tỉ lệ các con số đó tới dân số người dùng mục tiêu. (Nếu bộ đệm ẩn không tỉ lệ thuận với dân số người dùng, IOPS đĩa có thể tăng lên, vì tỷ lệ bộ đệm ẩn-trên-mỗi-người dùng trở nên nhỏ hơn.)
2. Tính toán số lượng đĩa cần thiết để hỗ trợ khối lượng công việc này. Tính toán dựa trên cấu hình RAID. Đừng sử dụng các giá trị thông lượng và IOPS tối đa của mỗi đĩa, vì điều này sẽ dẫn đến việc các đĩa hoạt động ở mức sử dụng 100%, dẫn đến các vấn đề hiệu năng tức thời do việc tăng hàng đợi. Chọn một mức sử dụng mục tiêu (ví dụ: 50%) và tỉ lệ các giá trị tương ứng.
3. Tính toán số lượng bộ điều khiển đĩa cần thiết để hỗ trợ khối lượng công việc này.
4. Kiểm tra xem các giới hạn vận chuyển chưa bị vượt quá, và chia tỉ lệ vận chuyển nếu cần.
5. Tính toán các chu kỳ CPU cho mỗi I/O đĩa, và số lượng CPU cần thiết (điều này có thể cần thiết cho hàng triệu IOPS và I/O song song).

Thông lượng và IOPS đĩa tối đa cho mỗi đĩa sẽ tùy thuộc vào loại của chúng và kích thước I/O cụ thể đối với một kích thước I/O và loại I/O nhất định, và đặc tính hóa khối lượng công việc có thể được sử dụng trên các khối lượng công việc hiện có để xem các kích thước và loại đĩa nào được sử dụng.

Để phân phối yêu cầu khối lượng công việc đĩa, không hiếm trường hợp tìm thấy các máy chủ yêu cầu hàng chục đĩa, được kết nối thông qua các mảng lưu trữ. Chúng tôi thường hay nói, "Thêm nhiều trục quay hơn." Ngày nay chúng ta có thể nói, "Thêm nhiều bộ nhớ flash hơn."

---

## 9.6 Các Công cụ Quan trắc (Observability Tools)
Phần này giới thiệu các công cụ quan sát I/O đĩa cho các hệ điều hành dựa trên Linux. Hãy xem phần trước cho các chiến lược cần tuân theo khi sử dụng chúng.

Các công cụ trong phần này được liệt kê trong Bảng 9.5.

Bảng 9.5 Các công cụ quan sát đĩa
| Mục | Công cụ | Mô tả |
| --- | --- | --- |
| 9.6.1 | iostat | Các thống kê đa dạng cho mỗi đĩa |
| 9.6.2 | sar | Các thống kê lịch sử đĩa |
| 9.6.3 | PSI | Thông tin về áp lực đĩa (disk pressure) |
| 9.6.4 | pidstat | Mức sử dụng đĩa theo tiến trình |
| 9.6.5 | perf | Ghi lại các tracepoints I/O khối |
| 9.6.6 | biolatency | Tóm tắt độ trễ I/O đĩa dưới dạng một biểu đồ histogram |
| 9.6.7 | biosnoop | Truy vết I/O đĩa với PID và độ trễ |
| 9.6.8 | iotop, biotop | Top cho các đĩa: tóm tắt I/O đĩa theo tiến trình |
| 9.6.9 | biostacks | Hiển thị I/O đĩa với các stack khởi tạo |
| 9.6.10 | blktrace | Truy vết sự kiện I/O đĩa |
| 9.6.11 | bpftrace | Truy vết đĩa tùy chỉnh |
| 9.6.12 | MegaCli | Các thống kê bộ điều khiển LSI |
| 9.6.13 | smartctl | Các thống kê điều khiển đĩa |

Đây là một sự lựa chọn các công cụ để hỗ trợ Mục 9.5, Phương pháp luận, bắt đầu với các công cụ và thống kê truyền thống, sau đó là các công cụ truy vết, và cuối cùng là các thống kê của bộ điều khiển và ổ đĩa. Một số công cụ truyền thống có khả năng khả dụng trên các hệ điều hành dạng Unix khác nơi chúng bắt nguồn, bao gồm: iostat(8) và sar(1). Nhiều công cụ truy vết dựa trên BPF, và sử dụng các frontend BCC và bpftrace (Chương 15); chúng là: biolatency(8), biosnoop(8), biotop(8), và biostacks(8).

Hãy xem tài liệu cho từng công cụ, bao gồm cả các trang man của chúng, để biết các tham chiếu đầy đủ về các tính năng của nó.

### 9.6.1 iostat
iostat(1) tóm tắt các thống kê I/O cho mỗi đĩa, cung cấp các chỉ số cho việc đặc tính hóa khối lượng công việc, mức sử dụng, và sự bão hòa. Những thống kê này được thực thi bởi kernel. Các thống kê được báo cáo lần đầu tiên bởi iostat(1) khi được thực hiện ở dòng lệnh. Các thống kê nó báo cáo ở chế độ mở rộng là rất đáng để học chi tiết để hiểu sâu hơn về giám sát đĩa. Những thống kê này được kernel bật theo mặc định, vì vậy các chi phí của công cụ này được coi là không đáng kể.

Tên gọi "iostat" là viết tắt của "I/O statistics", mặc dù nó có lẽ nên được gọi là "diskiostat" để phản ánh loại I/O mà nó báo cáo. Tên này đã dẫn đến sự nhầm lẫn thỉnh thoảng khi một người dùng biết rằng một ứng dụng đang thực hiện I/O (tới hệ thống tập tin) nhưng tự hỏi tại sao nó không thể thấy được trong iostat(1) (tới các đĩa).

iostat(1) ban đầu được viết vào đầu những năm 1980 cho Unix, và các phiên bản khác nhau có sẵn cho các hệ điều hành khác nhau. Nó có thể được thêm vào các hệ thống dựa trên Linux qua gói sysstat. Phần sau đây mô tả phiên bản Linux.

**Kết quả mặc định của iostat**
Không có bất kỳ đối số hoặc tùy chọn nào, một bản tóm tắt kể từ khi boot cho CPU và các thống kê đĩa được in. Nó được bao gồm ở đây như một sự giới thiệu cho công cụ này; tuy nhiên, chế độ mở rộng được đề cập sau này sẽ hữu ích hơn.
```bash
$ iostat
Linux 5.3.0-1010-aws (ip-10-1-239-218)    02/12/20    _x86_64_    (2 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.29    0.01    0.18    0.03    0.21   99.28

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
loop0             0.00         0.05         0.00       1232          0
[...]
nvme0n1           3.40        17.11        36.03     409902     863344
```
Dòng kết quả đầu tiên là một bản tóm tắt về hệ thống, bao gồm phiên bản kernel, host name, ngày, kiến trúc, và số lượng CPU. Các dòng tiếp theo hiển thị các thống kê tóm tắt kể từ khi boot cho các CPU (avg-cpu; những thống kê này được bao quát trong Chương 6, CPUs) và các thiết bị đĩa (dưới Device:).

Mỗi thiết bị đĩa được hiển thị như một hàng, với các chi tiết cơ bản trong các cột. Tôi đã bôi đậm các tiêu đề cột; chúng là:
- **tps:** Các giao dịch mỗi giây (IOPS)
- **kB_read/s, kB_wrtn/s:** Kilobyte được đọc mỗi giây, và được ghi mỗi giây
- **kB_read, kB_wrtn:** Tổng số kilobyte được đọc và ghi

Một số thiết bị SCSI, bao gồm CD-ROMs, có thể không được hiển thị bởi iostat(1). Thay vào đó, hãy sử dụng tapestat(1), cũng có trong gói sysstat. Đồng thời lưu ý rằng, trong khi iostat(1) báo cáo các lệnh đọc và ghi đĩa khối, nó có thể loại trừ một số loại lệnh đĩa khác tùy thuộc vào kernel (xem logic trong hàm kernel blk_do_io_stat()). Chế độ mở rộng bao gồm các trường bổ sung cho các lệnh đĩa này.

**Các tùy chọn iostat**
iostat(1) có thể được thực thi với các tùy chọn khác nhau, theo sau bởi một khoảng thời gian và số lượng tùy chọn. Ví dụ:
`# iostat 1 10`
sẽ in các bản tóm tắt một giây trong mười lần. Và:
`# iostat 1`
sẽ in các bản tóm tắt một giây không ngừng (cho đến khi Ctrl-C được nhấn).

Các tùy chọn được sử dụng phổ biến là:
- **-c:** Hiển thị báo cáo CPU
- **-d:** Hiển thị báo cáo đĩa
- **-k:** Sử dụng kilobyte thay vì các khối (512-byte)
- **-m:** Sử dụng megabyte thay vì các khối (512-byte)
- **-p:** Bao gồm các thống kê cho mỗi phân vùng
- **-t:** In dấu thời gian kết quả
- **-x:** Các thống kê mở rộng
- **-s:** Kết quả ngắn (hẹp)
- **-z:** Bỏ qua các bản tóm tắt hoạt động bằng không

Cũng có một biến môi trường, POSIXLY_CORRECT=1, để xuất các khối (mỗi cái 512 byte) thay vì Kbytes. Một số phiên bản cũ hơn bao gồm một tùy chọn cho các thống kê NFS, -n. Tùy chọn này đã được chuyển sang lệnh nfsiostat riêng biệt kể từ phiên bản 9.1.3.

**Kết quả Ngắn Mở rộng iostat**
Kết quả mở rộng (-x) cung cấp thêm các cột hữu ích cho các phương pháp luận đã đề cập trước đó. Những cột bổ sung này bao gồm IOPS và các chỉ số thông lượng cho việc đặc tính hóa khối lượng công việc, mức sử dụng và độ dài hàng đợi cho phương pháp USE, và thời gian phản hồi của đĩa cho việc đặc tính hóa hiệu năng và phân tích độ trễ.

Trong những năm qua, kết quả của iostat đã tăng chiều rộng và phiên bản mới nhất (12.3.1, tháng 12 năm 2019) tạo ra kết quả rộng 197 ký tự. Điều này không còn khớp trong các terminal màn hình rộng điển hình, khiến cho kết quả mặc định trở nên khó đọc do các lần xuống dòng. Một giải pháp đã được thêm vào vào năm 2017, tùy chọn -s, để cung cấp một kết quả "ngắn" hoặc hẹp được thiết kế để khớp trong chiều rộng 80 ký tự.

Dưới đây là một ví dụ về kết quả mở rộng ngắn (-sx), và bỏ qua các thiết bị không có hoạt động (-z):
```bash
$ iostat -sxz 1
[...]
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          15.82    0.00   10.71   31.63    1.53   40.31

Device             tps      kB/s    rqm/s   await aqu-sz  areq-sz  %util
nvme0n1        1642.00   9064.00   664.00    0.44   0.00     5.52 100.00
[...]
```
Các cột đĩa là:
- **tps:** Các giao dịch được phát hành mỗi giây (IOPS)
- **kB/s:** Kilobyte mỗi giây
- **rqm/s:** Các yêu cầu được xếp hàng và kết hợp mỗi giây
- **await:** Thời gian phản hồi I/O trung bình, bao gồm cả thời gian dành cho việc xếp hàng trong hệ điều hành và thời gian phản hồi của thiết bị (ms)
- **aqu-sz:** Số lượng yêu cầu trung bình cả hai đang chờ trong hàng đợi trình điều khiển yêu cầu và đang hoạt động trên thiết bị
- **areq-sz:** Kích thước yêu cầu trung bình tính theo Kbyte
- **%util:** Phần trăm thời gian thiết bị bận rộn xử lý các yêu cầu I/O (mức sử dụng)

Chỉ số quan trọng nhất cho hiệu năng được cung cấp là await, cho thấy thời gian chờ trung bình tổng cộng cho I/O. Những gì cấu thành "tốt" hay "tệ" tùy thuộc vào nhu cầu của bạn. Trong ví dụ trước đó, await là 0.44 ms, thứ là thỏa đáng cho máy chủ cơ sở dữ liệu này. Nó có thể tăng lên vì một số lý do: việc xếp hàng (tải), kích thước I/O lớn, I/O ngẫu nhiên trên các đĩa quay, và các lỗi thiết bị.

Đối với quy hoạch dung lượng và sử dụng tài nguyên, %util là quan trọng, nhưng hãy lưu ý rằng nó chỉ là một thước đo mức độ bận rộn (thời gian không rảnh rỗi) và không có nghĩa là cho các máy chủ lưu trữ ảo được hỗ trợ bởi nhiều đĩa. Những thiết bị đó có thể được hiểu rõ hơn bởi tải được áp dụng: tps (IOPS) và kB/s (thông lượng).

Các số lượng khác không bằng không trong cột rqm/s cho thấy các yêu cầu liên tục đã được gộp lại trước khi phân phối tới thiết bị, để cải thiện hiệu năng. Chỉ số này cũng là một dấu hiệu của một khối lượng công việc tuần tự.

areq-sz là kích thước sau khi gộp, các kích thước nhỏ (8 Kbyte hoặc ít hơn) là một chỉ báo của một khối lượng công việc I/O ngẫu nhiên thứ không thể được gộp lại. Kích thước lớn hơn có thể là I/O tuần tự lớn hoặc một khối lượng công việc tuần tự được gộp lại (được chỉ ra bởi các cột trước đó).

**Kết quả Mở rộng iostat**
Không có tùy chọn -s, -x in nhiều cột hơn nữa. Dưới đây là bản tóm tắt kể từ khi boot (không có khoảng thời gian hoặc số lượng) cho phiên bản sysstat 12.3.2 (từ tháng 4 năm 2020):
```bash
$ iostat -x
[...]
Device            r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz      w/s     wkB/s
wrqm/s  %wrqm w_await wareq-sz      d/s     dkB/s   drqm/s  %drqm d_await dareq-sz
f/s f_await  aqu-sz  %util
nvme0n1          0.23      9.91     0.16  40.70    0.56    43.01     3.10     33.09
0.92  22.91    0.89     10.66     0.00   0.00     0.00    0.00    0.00      0.00
0.00    0.00    0.00      0.12
```
Những thứ này chia nhỏ nhiều chỉ số -sx thành các thành phần đọc và ghi, và cũng bao gồm cả các lệnh discard và flushes.

Các cột bổ sung là:
- **r/s, w/s, d/s, f/s:** Các yêu cầu Read, write, discard, và flush đã hoàn thành từ thiết bị đĩa mỗi giây (sau khi gộp)
- **rkB/s, wkB/s, dkB/s:** Đọc, ghi, và loại bỏ bao nhiêu Kbytes từ đĩa mỗi giây
- **rrqm/s, wrqm/s, drqm/s:** Các yêu cầu Read, write, và discard được xếp hàng và kết hợp mỗi giây
- **%rrqm, %wrqm, %drqm:** Phần trăm của tổng số yêu cầu cho loại đó đã được gộp lại
- **r_await, w_await, d_await, f_await:** Thời gian trung bình cho các lệnh read, write, discard, và flush đã hoàn thành, bao gồm thời gian chờ trong OS và thời gian phản hồi từ thiết bị (ms)
- **rareq-sz, wareq-sz, dareq-sz:** Kích thước yêu cầu đọc, ghi, và loại bỏ trung bình (Kbytes)

Việc kiểm tra các lệnh đọc và ghi một cách riêng biệt là quan trọng. Các ứng dụng và các hệ thống tập tin thường sử dụng các kỹ thuật để giảm thiểu độ trễ ghi (ví dụ, write-back caching), sao cho ứng dụng ít có khả năng bị chặn bởi các lệnh ghi đĩa. Điều này có nghĩa là bất kỳ chỉ số nào nhóm các lệnh đọc và ghi đều bị sai lệch bởi một thành phần có thể không trực tiếp quan trọng đối với ứng dụng. Bằng cách chia chúng ra, bạn có thể thấy được r_await, thứ hiển thị độ trễ đọc trung bình, và có khả năng là chỉ số quan trọng nhất cho hiệu năng ứng dụng.

Các lệnh discard và flush là những sự bổ sung mới cho iostat(1). Các thao tác discard giúp giải phóng các khối trên ổ đĩa (lệnh ATA TRIM), và các thống kê của chúng đã được thêm vào kernel Linux 4.19. Thống kê Flush đã được thêm vào Linux 5.5. Những thứ này có thể giúp thu hẹp lý do gây ra độ trễ đĩa.

Dưới đây là một sự kết hợp hữu ích khác của iostat(1):
`$ iostat -dmstxz -p ALL 1`
Kết quả đầu tiên là một bản tóm tắt kể từ khi boot, theo sau là các khoảng thời gian một giây. Tùy chọn -d tập trung vào các thống kê đĩa (không có CPU), -m cho Mbytes, và -t cho các bản tóm tắt có dấu thời gian, thứ hữu ích hơn khi so sánh kết quả với các nguồn có dấu thời gian khác, và -p ALL bao gồm các thống kê cho mỗi phân vùng. Thật không may, phiên bản hiện tại của iostat(1) không bao gồm các lỗi đĩa; nếu không thì tất cả các chỉ số phương pháp USE có thể được kiểm tra từ một công cụ duy nhất!

### 9.6.2 sar
Trình báo cáo hoạt động hệ thống, sar(1), có thể được sử dụng để quan sát hoạt động hiện tại và có thể được cấu hình để lưu trữ và báo cáo các thống kê lịch sử. Nó được giới thiệu trong Mục 4.4, sar, và đã được đề cập trong các chương khác nhau cho các thống kê khác nhau mà nó cung cấp.

Bản tóm tắt đĩa của sar(1) được in bằng tùy chọn -d, được trình diễn trong ví dụ sau đây với một khoảng thời gian là một giây. Kết quả là rộng, vì vậy nó được bao gồm ở đây dưới dạng hai phần (sysstat 12.3.2):
```bash
$ sar -d 1
Linux 5.3.0-1010-aws (ip-10-0-239-218)    02/13/20    _x86_64_    (2 CPU)

09:10:22          DEV       tps     rkB/s     wkB/s     dkB/s   areq-sz \ ...
09:10:23      dev259-0   1509.00  11100.00  12776.00      0.00     15.82 / ...
[...]
```
Dưới đây là các cột còn lại:
```bash
$ sar -d 1
09:10:22    \ ...   aqu-sz     await     %util
09:10:23    / ...     0.02      0.60     94.00
[...]
```
Các cột này cũng xuất hiện trong kết quả iostat(1) -x, và đã được mô tả trong Mục trước đó. Kết quả này cho thấy một khối lượng công việc đọc/ghi hỗn hợp với một await là 0.6 ms, đẩy đĩa tới mức sử dụng 94%.

Các phiên bản trước của sar(1) bao gồm một cột svctm (service time): thời gian phản hồi trung bình (suy ra). Kể từ khi tính toán đơn giản của nó không còn chính xác cho các đĩa hiện đại thực hiện I/O song song, svctm đã bị loại bỏ trong các phiên bản sau này.

### 9.6.3 PSI
Thông tin về áp lực áp suất Linux (PSI), được thêm vào trong Linux 4.20, bao gồm các thống kê cho độ bão hòa đĩa. Những điều này không chỉ hiển thị liệu có áp lực đĩa hay không, mà còn cho thấy nó đang thay đổi như thế nào trong năm phút qua. Kết quả ví dụ:
```bash
# cat /proc/pressure/io
some avg10=63.11 avg60=32.18 avg300=8.62 total=667212021
full avg10=60.76 avg60=31.13 avg300=8.35 total=622722632
```
Kết quả này cho thấy áp lực I/O đang tăng lên, với mức trung bình 10 giây cao hơn (63.11) so với trung bình 300 giây (8.62). Những giá trị trung bình này là phần trăm thời gian mà một tác vụ bị chặn I/O. Dòng *some* cho thấy khi một số tác vụ (luồng) bị ảnh hưởng, và dòng *full* khi tất cả các tác vụ sẵn sàng chạy bị ảnh hưởng.

Giống như với các mức trung bình tải (load averages), đây có thể là một chỉ số cấp cao được sử dụng cho việc cảnh báo. Một khi bạn nhận thức được một vấn đề hiệu năng đĩa, bạn có thể sử dụng các công cụ khác để tìm ra các nguồn gốc thực sự, bao gồm pidstat(8) cho các thống kê đĩa theo tiến trình.

### 9.6.4 pidstat
Công cụ pidstat(1) của Linux in mức sử dụng CPU theo mặc định và bao gồm một tùy chọn -d cho các thống kê I/O đĩa. Chúng khả dụng trên các kernel 2.6.20 và mới hơn. Ví dụ:
```bash
$ pidstat -d 1
Linux 5.3.0-1010-aws (ip-10-0-239-218)    02/13/20    _x86_64_    (2 CPU)

09:47:41       UID       PID   kB_rd/s   kB_wr/s kB_ccwr/s iodelay  Command
09:47:42         0      2705  32468.00      0.00      0.00       5  tar
09:47:42         0      2706      0.00   8192.00      0.00       0  gzip
[...]
09:47:56       UID       PID   kB_rd/s   kB_wr/s kB_ccwr/s iodelay  Command
09:47:57         0       229      0.00     72.00      0.00       0  systemd-journal
09:47:57         0       380      0.00      0.00      0.00       0  auditd
09:47:57         0      2699      4.00      0.00      0.00      10  kworker/
u4:1-flush-259:0
09:47:57         0      2705  15104.00      0.00      0.00       0  tar
09:47:57         0      2706      0.00   6912.00      0.00       0  gzip
```
Các cột bao gồm:
- **kB_rd/s:** Kilobyte được đọc mỗi giây
- **kB_wr/s:** Kilobyte được phát hành để ghi mỗi giây
- **kB_ccwr/s:** Kilobyte bị hủy bỏ cho việc ghi mỗi giây (ví dụ, ghi đè hoặc xóa trước khi flush)
- **iodelay:** Thời gian tiến trình bị chặn trên I/O đĩa (clock ticks), bao gồm cả swapping

Khối lượng công việc được thấy trong kết quả là một lệnh tar đang đọc hệ thống tập tin vào một pipe, và gzip đang đọc từ pipe và ghi một tập tin nén. Các lần đọc tar đã gây ra I/O đĩa (5 clock ticks), trong khi các lần ghi gzip thì không, do write-back caching trong page cache. Một thời gian sau đó, page cache được flush, như có thể thấy trong khoảng thời gian kết quả thứ hai bởi luồng kernel kworker/u4:1-flush-259:0, thứ gặp phải iodelay.

iodelay là một sự bổ sung mới và cho thấy mức độ nghiêm trọng của các vấn đề hiệu năng: ứng dụng đã phải chờ đợi bao nhiêu. Các cột khác cho thấy khối lượng công việc được áp dụng.

Lưu ý rằng chỉ superusers (root) mới có thể truy cập các thống kê đĩa cho các tiến trình mà họ không sở hữu. Những thống kê này được đọc qua /proc/PID/io.

### 9.6.5 perf
Công cụ perf(1) của Linux (Chương 13) có thể ghi lại các tracepoints khối. Liệt kê chúng:
```bash
# perf list 'block:*'

List of pre-defined events (to be used in -e):

  block:block_bio_backmerge                          [Tracepoint event]
  block:block_bio_bounce                             [Tracepoint event]
  block:block_bio_complete                           [Tracepoint event]
  block:block_bio_frontmerge                         [Tracepoint event]
  block:block_bio_queue                              [Tracepoint event]
  block:block_bio_remap                              [Tracepoint event]
  block:block_dirty_buffer                           [Tracepoint event]
  block:block_getrq                                  [Tracepoint event]
  block:block_plug                                   [Tracepoint event]
  block:block_rq_complete                            [Tracepoint event]
  block:block_rq_insert                              [Tracepoint event]
  block:block_rq_issue                               [Tracepoint event]
  block:block_rq_remap                               [Tracepoint event]
  block:block_rq_requeue                             [Tracepoint event]
  block:block_sleeprq                                [Tracepoint event]
  block:block_split                                  [Tracepoint event]
  block:block_touch_buffer                           [Tracepoint event]
  block:block_unplug                                 [Tracepoint event]
```
Ví dụ, các bản ghi sau đây ghi lại các sự kiện phát hành thiết bị khối với các stack traces. Một lệnh ngủ 10 giây được cung cấp dưới dạng khoảng thời gian truy vết.
```bash
# perf record -e block:block_rq_issue -a -g sleep 10
[ perf record: Woken up 22 times to write data ]
[ perf record: Captured and wrote 5.701 MB perf.data (19267 samples) ]
# perf script --header
[...]
mysqld  1965 [001] 160501.158573: block:block_rq_issue: 259,0 WS 12288 () 10329704 +
24 [mysqld]
        ffffffffb12d5040 blk_mq_start_request+0xa0 ([kernel.kallsyms])
        ffffffffb12d5040 blk_mq_start_request+0xa0 ([kernel.kallsyms])
        ffffffffb1532b4c nvme_queue_rq+0x16c ([kernel.kallsyms])
        ffffffffb12d7b46 __blk_mq_try_issue_directly+0x116 ([kernel.kallsyms])
        ffffffffb12d87bb blk_mq_request_issue_directly+0x4b ([kernel.kallsyms])
        ffffffffb12d8896 blk_mq_try_issue_directly+0x46 ([kernel.kallsyms])
        ffffffffb12dce7e blk_mq_sched_insert_requests+0xae ([kernel.kallsyms])
        ffffffffb12d86c8 blk_mq_flush_plug_list+0x1e8 ([kernel.kallsyms])
        ffffffffb12cd623 blk_flush_plug_list+0xe3 ([kernel.kallsyms])
        ffffffffb12cd676 blk_finish_plug+0x26 ([kernel.kallsyms])
        ffffffffb119771c ext4_writepages+0x77c ([kernel.kallsyms])
        ffffffffb10209c3 do_writepages+0x43 ([kernel.kallsyms])
        ffffffffb1017ed5 __filemap_fdatawrite_range+0xd5 ([kernel.kallsyms])
        ffffffffb10186ca file_write_and_wait_range+0x5a ([kernel.kallsyms])
        ffffffffb118637f ext4_sync_file+0x8f ([kernel.kallsyms])
        ffffffffb1105869 vfs_fsync_range+0x49 ([kernel.kallsyms])
        ffffffffb11058fd do_fsync+0x3d ([kernel.kallsyms])
        ffffffffb1105944 __x64_sys_fsync+0x14 ([kernel.kallsyms])
        ffffffffb1a0008c entry_SYSCALL_64_after_hwframe+0x44 ([kernel.kallsyms])
        7f2285d1988b fsync+0x3b (/usr/lib/x86_64-linux-gnu/libpthread-2.30.so)
        55ac10a05ebe Fil_shard::redo_space_flush+0x44e (/usr/sbin/mysqld)
        55ac10a06179 Fil_shard::flush_file_redo+0x99 (/usr/sbin/mysqld)
        55ac1076ff1c [unknown] (/usr/sbin/mysqld)
        55ac10777030 log_flusher+0x520 (/usr/sbin/mysqld)
        55ac10748d61
std::thread::_State_impl<std::thread::_Invoker<std::tuple<Runnable, void (*)(log_t*),
log_t* > > >::_M_run+0xc1 (/usr/sbin/mysqld)
        7f228559df74 [unknown] (/usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.28)
        7f226c3652c0 [unknown] ([unknown])
        55ac107499f0
std::thread::_State_impl<std::thread::_Invoker<std::tuple<Runnable, void (*)(log_t*),
log_t* > > >::_State_impl+0x0 (/usr/sbin/mysqld)
        5441554156415741 [unknown] ([unknown])
[...]
```
Chỉ có hai stacks được bao gồm ở đây. Cái đầu tiên là từ lệnh gọi ngủ(1) giả mà tôi đã kích hoạt, và cái thứ hai là từ máy chủ MySQL. Khi truy vết trên toàn hệ thống, bạn có thể thấy nhiều stacks từ các tiến trình tồn tại ngắn ngủi nhanh chóng kích hoạt các lỗi trang, kích hoạt I/O, trước khi kết thúc. Bạn có thể sử dụng -p PID thay vì -a để khớp với một tiến trình.

Kết quả đầy đủ là 222,582 dòng; báo cáo perf tóm tắt các đường dẫn mã dưới dạng một hệ thống phân cấp, nhưng kết quả vẫn còn 7,592 dòng. Các bản đồ nhiệt (flame graphs) có thể được sử dụng để hình ảnh hóa toàn bộ hồ sơ hiệu năng một cách hiệu quả hơn.

**Các bản đồ nhiệt lỗi trang (Page Fault Flame Graphs)**
Hình 7.12 trình bày một bản đồ nhiệt lỗi trang được tạo ra từ hồ sơ trước đó.

Hình 7.12 cho thấy hơn một nửa sự tăng trưởng bộ nhớ trong máy chủ MySQL là từ đường dẫn mã JOIN::optimize() (cây lớn bên trái). Việc rê chuột qua JOIN::optimize() cho thấy nó và các lệnh gọi con của nó chịu trách nhiệm cho 3,226 lỗi trang; với các trang 4 Kbyte, điều này tương đương với khoảng 12 Mbyte tăng trưởng bộ nhớ chính.

Các lệnh được sử dụng để tạo bản đồ nhiệt này, bao gồm cả lệnh perf(1) để ghi lại các lỗi trang, là:
```bash
# perf record -e page-faults -a -g -- sleep 60
# perf script --header > out.stacks
$ git clone https://github.com/brendangregg/FlameGraph; cd FlameGraph
$ ./stackcollapse-perf.pl < ../out.stacks | ./flamegraph.pl --hash 
    --bgcolor=green --count=pages --title="Page Fault Flame Graph" > out.svg
```
Tôi đã đặt màu nền thành màu xanh lá cây như một lời nhắc nhở trực quan rằng đây không phải là một bản đồ nhiệt CPU điển hình (nền vàng) mà là một bản đồ nhiệt bộ nhớ (nền xanh lá cây).

### 9.6.6 biolatency
biolatency(8) là một công cụ BCC và bpftrace để hiển thị I/O đĩa dưới dạng một biểu đồ histogram. Thuật ngữ *I/O latency* được sử dụng ở đây đề cập đến thời gian từ khi phát yêu cầu tới thiết bị, tới khi nó hoàn thành (hay còn gọi là thời gian yêu cầu đĩa).

Phần sau đây cho thấy biolatency(8) từ việc truy vết I/O đĩa BCC trong 10 giây:
```bash
# biolatency 10 1
Tracing block device I/O... Hit Ctrl-C to end.

usecs               : count     distribution
    0 -> 1          : 0        |                                        |
    2 -> 3          : 0        |                                        |
    4 -> 7          : 0        |                                        |
    8 -> 15         : 0        |                                        |
   16 -> 31         : 2        |                                        |
   32 -> 63         : 0        |                                        |
   64 -> 127        : 0        |                                        |
  128 -> 255        : 1065     |****************                        |
  256 -> 511        : 2462     |****************************************|
  512 -> 1023       : 1949     |*******************************         |
 1024 -> 2047       : 373      |******                                  |
 2048 -> 4095       : 1815     |*****************************           |
 4096 -> 8191       : 591      |*********                               |
 8192 -> 16383      : 397      |******                                  |
16384 -> 32767      : 50       |                                        |
```
Kết quả này cho thấy một phân phối bi-modal, với một chế độ nằm giữa 128 và 1023 micro giây, và một chế độ khác nằm giữa 2048 và 4095 micro giây (2.0 tới 4.1 mili giây). Bây giờ tôi biết rằng độ trễ thiết bị là bi-modal, tôi hiểu rằng việc chỉ sử dụng mức trung bình (average) cho thiết bị là gây nhầm lẫn. Chế độ nhanh hơn, ví dụ, có thể là các lệnh đọc ngẫu nhiên I/O hoặc kích thước I/O lớn hơn (có thể được xác định bằng các công cụ BPF khác), hoặc các cờ I/O khác nhau (được hiển thị bằng tùy chọn -F). I/O chậm nhất trong kết quả này đã đạt tới phạm vi 16- tới 32-mili giây: điều này nghe có vẻ giống như việc xếp hàng thiết bị đĩa.

Phiên bản BCC của biolatency(8) hỗ trợ các tùy chọn bao gồm:
- **-m:** Kết quả tính theo mili giây
- **-Q:** Bao gồm thời gian chờ xếp hàng của hệ điều hành (thời gian yêu cầu OS)
- **-F:** Hiển thị một biểu đồ histogram cho mỗi bộ cờ I/O
- **-D:** Hiển thị một biểu đồ histogram cho mỗi thiết bị đĩa

Sử dụng -Q khiến biolatency(8) báo cáo toàn bộ thời gian I/O từ lúc tạo và chèn vào một hàng đợi cho tới khi hoàn thành thiết bị, được mô tả trước đó như là thời gian yêu cầu khối I/O.

BCC biolatency(8) cũng chấp nhận khoảng thời gian và số lượng đối số tùy chọn, tính theo giây.

**Theo mỗi cờ (Per-Flag)**
Tùy chọn -F đặc biệt hữu ích, chia nhỏ phân phối cho mỗi cờ I/O. Ví dụ, với -m cho các biểu đồ histogram mili giây:
```bash
# biolatency -Fm 10 1
Tracing block device I/O... Hit Ctrl-C to end.

flags = Sync-Write
     msecs               : count     distribution
         0 -> 1          : 2        |****************************************|

flags = Flush
     msecs               : count     distribution
         0 -> 1          : 1        |****************************************|

flags = Write
     msecs               : count     distribution
         0 -> 1          : 14       |****************************************|
         2 -> 3          : 1        |**                                      |
         4 -> 7          : 10       |****************************            |
         8 -> 15         : 11       |*******************************         |
        16 -> 31         : 11       |*******************************         |

flags = NoMerge-Write
     msecs               : count     distribution
         0 -> 1          : 95       |**********                              |
         2 -> 3          : 152      |****************                        |
         4 -> 7          : 266      |****************************            |
         8 -> 15         : 350      |****************************************|
        16 -> 31         : 298      |*********************************       |

flags = Read
     msecs               : count     distribution
         0 -> 1          : 11       |****************************************|

flags = ReadAhead-Read
     msecs               : count     distribution
         0 -> 1          : 5261     |****************************************|
         2 -> 3          : 1238     |*********                               |
         4 -> 7          : 481      |***                                     |
         8 -> 15         : 5        |                                        |
        16 -> 31         : 2        |                                        |
```
Các cờ này có thể được xử lý khác nhau bởi thiết bị lưu trữ; việc chia nhỏ chúng ra cho phép chúng ta nghiên cứu chúng một cách riêng biệt. Kết quả trước đó cho thấy việc đọc nhanh hơn các lệnh ghi, và có thể giải thích cho phân phối bi-modal.

biolatency(8) tóm tắt độ trễ I/O đĩa. Để kiểm tra nó cho mỗi I/O, hãy sử dụng biosnoop(8).

### 9.6.7 biosnoop
biosnoop(8) là một công cụ BCC và bpftrace in một dòng tóm tắt cho mỗi I/O đĩa. Ví dụ:
```bash
# biosnoop
TIME(s)     COMM           PID    DISK    T SECTOR     BYTES   LAT(ms)
0.009165000 jbd2/nvme0n1p1 174    nvme0n1 W 2116272    8192       0.43
0.009612000 jbd2/nvme0n1p1 174    nvme0n1 W 2116288    4096       0.39
0.011836000 mysqld         1948   nvme0n1 W 2116296    4096       0.45
0.012363000 jbd2/nvme0n1p1 174    nvme0n1 W 2116296    8192       0.49
0.012844000 jbd2/nvme0n1p1 174    nvme0n1 W 2116312    4096       0.43
0.016809000 mysqld         1948   nvme0n1 W 10227712   262144     1.82
0.017184000 mysqld         1948   nvme0n1 W 10228224   262144     2.19
0.017679000 mysqld         1948   nvme0n1 W 10228736   262144     2.68
0.018056000 mysqld         1948   nvme0n1 W 10229248   262144     3.05
0.018264000 mysqld         1948   nvme0n1 W 10230272   262144     3.25
0.018657000 mysqld         1948   nvme0n1 W 10230272   262144     3.64
0.018954000 mysqld         1948   nvme0n1 W 10230784   262144     3.93
0.019053000 mysqld         1948   nvme0n1 W 10231296   131072     4.03
0.019731000 jbd2/nvme0n1p1 174    nvme0n1 W 2116320    8192       0.49
0.020243000 jbd2/nvme0n1p1 174    nvme0n1 W 2116336    4096       0.46
0.020593000 mysqld         1948   nvme0n1 R 4495352    4096       0.26
[...]
```
Kết quả này cho thấy một khối lượng công việc ghi tới đĩa nvme0n1, chủ yếu từ mysqld, PID 174, với các kích thước I/O khác nhau. Các cột là:
- **TIME(s):** Thời gian hoàn thành I/O tính bằng giây
- **COMM:** Tên tiến trình (nếu công cụ này biết)
- **PID:** ID tiến trình (nếu công cụ này biết)
- **DISK:** Tên thiết bị lưu trữ
- **T:** Loại: R == reads, W == writes
- **SECTOR:** Địa chỉ tính theo các đơn vị cung từ 512-byte
- **BYTES:** Kích thước của yêu cầu I/O
- **LAT(ms):** Thời gian từ khi phát yêu cầu tới thiết bị đến khi hoàn thành (thời gian yêu cầu đĩa)

Xung quanh phần giữa của kết quả ví dụ là một chuỗi 262,144 byte ghi, bắt đầu với độ trễ 1.82 ms và tăng dần độ trễ cho từng đợt tiếp theo, kết thúc bằng 4.03 ms. Đây là một mẫu hình tôi thường thấy, và lý do có khả năng nhất có thể được tính toán từ một cột khác trong kết quả: TIME(s). Nếu bạn trừ đi cột LAT(ms) từ cột TIME(s), bạn có thời gian bắt đầu của I/O, và những thứ này đã bắt đầu vào cùng một thời điểm. Điều này dường như là một nhóm I/O lớn đã được phát đồng thời, được xếp hàng trên thiết bị, và sau đó được hoàn thành lần lượt, với độ trễ tăng dần cho từng cái.

Bằng việc kiểm tra kỹ lưỡng các thời điểm bắt đầu và kết thúc, việc sắp xếp lại trên thiết bị cũng có thể được xác định. Vì kết quả có thể chứa hàng nghìn dòng, tôi thường sử dụng phần mềm thống kê R để vẽ biểu đồ kết quả dưới dạng một biểu đồ phân tán (scatter plot), nhằm giúp xác định các mẫu hình này (xem Mục 9.7, Hình ảnh hóa).

**Phân tích Giá trị ngoại lai (Outlier Analysis)**
Dưới đây là một phương pháp để tìm kiếm và phân tích các giá trị ngoại lai độ trễ bằng cách sử dụng biosnoop(8):
1. Ghi kết quả vào một tập tin:
   `# biosnoop > out.biosnoop01.txt`
2. Sắp xếp kết quả theo cột độ trễ, và in năm mục cuối cùng (những cái có độ trễ cao nhất):
   `# sort -n -k 8,8 out.biosnoop01.txt | tail -5`
   ```bash
   31.344175  logger         10994  nvme0n1 W 15218056   262144   30.92
   31.344401  logger         10994  nvme0n1 W 15217544   262144   30.92
   31.344757  logger         10994  nvme0n1 W 15219080   262144   31.49
   31.345260  logger         10994  nvme0n1 W 15218568   262144   32.00
   46.059274  logger         10994  nvme0n1 W 15198896   4096     64.86
   ```
3. Mở kết quả trong một trình soạn thảo văn bản (ví dụ: vi(1) hoặc vim(1)):
   `# vi out.biosnoop01.txt`
4. Duyệt qua các giá trị ngoại lai từ chậm nhất tới nhanh nhất, tìm kiếm thời gian ở cột đầu tiên. Chậm nhất là 64.86 mili giây, với thời gian hoàn thành là 46.059274 (giây). Tìm kiếm cho 46.059274:
   ```bash
   [...]
   45.992419  jbd2/nvme0n1p1 174    nvme0n1 W 2107232    8192       0.45
   45.992988  jbd2/nvme0n1p1 174    nvme0n1 W 2107248    4096       0.50
   46.059274  logger         10994  nvme0n1 W 15198896   4096      64.86
   [...]
   ```
5. Nhìn vào các sự kiện đã xảy ra trước giá trị ngoại lai đó, để xem liệu có độ trễ tương tự và vì thế đây có phải là kết quả của việc xếp hàng hay không (tương tự như độ trễ tăng từ 1.82 lên 4.03 ms thấy trong kết quả biosnoop đầu tiên), hay cho bất kỳ manh mối nào khác. Không có cái nào ở đây: I/O trước đó là khoảng 6 ms sớm hơn, với một độ trễ là 0.5 ms. Thiết bị có thể đã sắp xếp lại các sự kiện và hoàn thành những cái khác trước tiên. Nếu sự kiện hoàn thành trước đó diễn ra khoảng 64 ms trước đó, thì khoảng trống trong các lần hoàn thành từ thiết bị có thể được giải thích bởi các yếu tố khác: ví dụ, hệ thống này là một thực thể VM, và có thể đã bị ngắt lịch trình (de-scheduled) bởi hypervisor trong quá trình I/O, thêm thời gian đó vào thời gian I/O.

**Queued Time (Thời gian xếp hàng)**
Một tùy chọn -Q của BCC biosnoop(8) có thể được sử dụng để hiển thị thời gian dành cho việc chờ đợi giữa lúc tạo I/O và phát hành tới thiết bị (trước đây được gọi là *block I/O wait time* hoặc *OS wait time*). Thời gian này chủ yếu được dành cho các hàng đợi OS, nhưng cũng có thể bao gồm việc cấp phát bộ nhớ và tranh chấp khóa. Ví dụ:
```bash
# biosnoop -Q
TIME(s)     COMM           PID    DISK    T SECTOR     BYTES QUE(ms) LAT(ms)
0.000000    kworker/u4:0   9491   nvme0n1 W 5726504    4096      0.06    0.60
0.000039    kworker/u4:0   9491   nvme0n1 W 8128536    4096      0.05    0.64
0.000084    kworker/u4:0   9491   nvme0n1 W 8128584    4096      0.05    0.68
0.000138    kworker/u4:0   9491   nvme0n1 W 8128632    4096      0.05    0.74
0.000231    kworker/u4:0   9491   nvme0n1 W 8128664    4096      0.05    0.83
[...]
```
Thời gian xếp hàng được hiển thị trong cột QUE(ms).

### 9.6.8 iotop, biotop
Tôi đã viết iotop đầu tiên vào năm 2005 cho các hệ thống dựa trên Solaris [McDougall 06a]. Hiện nay có nhiều phiên bản, bao gồm một công cụ iotop(1) Linux dựa trên các thống kê kế toán kernel (kernel accounting statistics) [Chazagain 13], và công cụ biotop(8) của riêng tôi dựa trên BPF.

**iotop**
iotop thường có thể được cài đặt qua một gói iotop. Khi chạy không có đối số, nó làm mới màn hình mỗi giây, hiển thị các tiến trình I/O đĩa hàng đầu. Chế độ lô (-b) có thể được sử dụng để cung cấp một kết quả dạng cuốn (không xóa màn hình); nó được trình diễn ở đây với I/O chỉ dành cho các tiến trình (-o) và một khoảng thời gian 5 giây (-d5):
```bash
# iotop -bod5
Total DISK READ:       4.78 K/s | Total DISK WRITE:      15.04 M/s
  TID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN      IO    COMMAND
22400 be/4 root        4.78 K/s    0.00 B/s  0.00 % 13.76 % [flush-252:0]
  279 be/3 root        0.00 B/s 1657.27 K/s  0.00 %  9.25 % [jbd2/vda2-8]
22446 be/4 root        0.00 B/s   10.16 M/s  0.00 %  0.00 % beam.smp -K true ...
Total DISK READ:       0.00 B/s | Total DISK WRITE:      10.75 M/s
  TID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN      IO    COMMAND
  279 be/3 root        0.00 B/s    0.00 B/s  0.00 %  0.01 % [jbd2/vda2-8]
22446 be/4 root        0.00 B/s   10.37 M/s  0.00 %  0.00 % beam.smp -K true ...
  646 be/4 root        0.00 B/s  272.71 B/s  0.00 %  0.00 % rsyslogd -n -c 5
[...]
```
Kết quả hiển thị tiến trình beam.smp (Riak) đang thực hiện một khối lượng công việc ghi đĩa khoảng 10 Mbytes/s. Các cột bao gồm:
- **DISK READ:** Đọc Kbytes/s
- **DISK WRITE:** Ghi Kbytes/s
- **SWAPIN:** Phần trăm thời gian luồng chờ đợi việc swap-in I/O
- **IO:** Phần trăm thời gian luồng chờ đợi I/O

iotop(8) hỗ trợ nhiều tùy chọn khác nhau, bao gồm -a cho các thống kê tích lũy (thay vì cho mỗi khoảng thời gian), -p PID để khớp với một tiến trình, và -d SEC để thiết lập khoảng thời gian.

Tôi khuyên bạn nên kiểm tra iotop(8) với một khối lượng công việc đã biết và kiểm tra xem các con số có khớp không. Tôi vừa thử nghiệm iotop (phiên bản 0.6) và thấy rằng nó đánh giá thấp đáng kể các khối lượng công việc ghi. Tôi cũng đã sử dụng biotop(8), thứ sử dụng một sự instrumentation khác và *thực sự* khớp với khối lượng công việc kiểm tra của tôi.

**biotop**
biotop(8) là một công cụ BCC, và là một top(1) khác cho các đĩa. Kết quả ví dụ:
```bash
# biotop
Tracing... Output every 1 secs. Hit Ctrl-C to end

08:04:11 loadavg: 1.48 0.87 0.45 1/287 14547

PID    COMM             D MAJ MIN DISK       I/O  Kbytes  AVGms
14501  cksum            R 202 1   xvda1      361   28832   3.39
6961   dd               R 202 1   xvda1     1628   13024   0.59
13855  dd               R 202 1   xvda1     1627   13016   0.59
326    jbd2/xvda1-8     W 202 1   xvda1        3     168   0.00
1880   supervise        W 202 1   xvda1        2       8   6.71
1873   supervise        W 202 1   xvda1        2       8   2.51
1871   supervise        W 202 1   xvda1        2       8   1.57
1876   supervise        W 202 1   xvda1        2       8   1.22
[...]
```
Điều này cho thấy lệnh cksum(1) và dd(1) đang thực hiện các lệnh đọc, và các tiến trình supervise đang thực hiện một số lệnh ghi. Đây là một cách nhanh chóng để xác định ai đang thực hiện I/O đĩa, và bao nhiêu. Các cột là:
- **PID:** ID tiến trình được đệm ẩn (nỗ lực tốt nhất)
- **COMM:** Tên tiến trình được đệm ẩn (nỗ lực tốt nhất)
- **D:** Hướng (R == read, W == write)
- **MAJ MIN:** Các số major và minor của đĩa (một định danh kernel)
- **DISK:** Tên đĩa
- **I/O:** Số lượng I/O đĩa trong khoảng thời gian
- **Kbytes:** Tổng thông lượng đĩa trong khoảng thời gian (Kbytes)
- **AVGms:** Thời gian trung bình cho I/O (độ trễ) từ lúc phát hành cho tới lúc hoàn thành (mili giây)

Bởi vì I/O đĩa được phát ra bất đồng bộ, tiến trình yêu cầu I/O có thể không còn ở trên CPU, và việc nhận diện nó có thể khó khăn. biotop(8) sử dụng một cách tiếp cận nỗ lực tốt nhất: các cột PID và COMM thường sẽ khớp với tiến trình đúng, nhưng điều này không được đảm bảo.

biotop(8) hỗ trợ các tùy chọn khoảng thời gian và số lượng cột (khoảng thời gian mặc định là một giây), -C để không xóa màn hình, và -r MAXROWS để chỉ định số lượng tiến trình hàng đầu để hiển thị.

### 9.6.9 biostacks
biostacks(8) là một công cụ bpftrace truy vết thời gian yêu cầu I/O khối (từ lúc đưa vào hàng đợi OS cho tới lúc hoàn thành) cùng với I/O initialization stack trace. Ví dụ:
```bash
# biostacks.bt
Attaching 5 probes...
Tracing block I/O with init stacks. Hit Ctrl-C to end.
^C
[...]

@usecs[
    blk_account_io_start+1
    blk_mq_make_request+1069
    generic_make_request+292
    submit_bio+115
    submit_bh_wbc+384
    ll_rw_block+173
    ext4_bread+102
    __ext4_read_dirblock+52
    ext4_dx_find_entry+145
    ext4_find_entry+365
    ext4_lookup+129
    lookup_slow+171
    walk_component+451
    path_lookupat+132
    filename_lookup+182
    user_path_at_empty+54
    sys_access+175
    do_syscall_64+115
    entry_SYSCALL_64_after_hwframe+61
]:
[2K, 4K)                 2 |@@                                                        |
[4K, 8K)                37 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[8K, 16K)               15 |@@@@@@@@@@@@@@@@@@@@@                                     |
[16K, 32K)               9 |@@@@@@@@@@@@                                              |
[32K, 64K)               1 |@                                                         |
```
Kết quả hiển thị một biểu đồ histogram độ trễ (tính theo micro giây) cho I/O đĩa, cùng với I/O stack yêu cầu: thông qua syscall access(2), filename_lookup(), và ext4_lookup(). I/O này được gây ra bởi việc tìm kiếm các tên đường dẫn trong các kiểm tra quyền hạn tập tin. Kết quả chỉ ra rằng những I/O này được gây ra bởi hoạt động khác ngoài các lệnh đọc và ghi.

Tôi đã thấy các trường hợp có I/O đĩa bí ẩn mà không có bất kỳ ứng dụng nào gây ra nó. Lý do hóa ra là do các tác vụ hệ thống tập tin chạy nền. (Trong một trường hợp đó là scrubbing chạy nền của ZFS, thứ định kỳ xác minh các checksum.) biostacks(8) có thể nhận diện lý do thực sự cho I/O đĩa bằng cách hiển thị kernel stack trace.

### 9.6.10 blktrace
blktrace(8) là một cơ sở truy vết tùy chỉnh cho các sự kiện I/O thiết bị khối trên Linux sử dụng kernel blktrace tracer. Đây là một trình truy vết chuyên dụng được kiểm soát thông qua BLKTRACE ioctl(2) tới các tập tin thiết bị đĩa. Các công cụ frontend bao gồm blktrace(8), blkparse(1), và btrace(8).

blktrace(8) cho phép truy vết driver kernel thiết bị khối và trích xuất dữ liệu vết thô, dữ liệu này có thể được xử lý bằng blkparse(1). Để thuận tiện, công cụ btrace(8) chạy cả blktrace(8) và blkparse(1), sao cho các nội dung sau đây là tương đương:
`# blktrace -d /dev/sda -o - | blkparse -i -`
`# btrace /dev/sda`

blktrace(8) là một công cụ cấp thấp hiển thị nhiều sự kiện cho mỗi I/O.

**Kết quả mặc định**
Phần sau đây trình bày kết quả mặc định của btrace(8) và bắt được một sự kiện đọc đĩa duy nhất của lệnh cksum(1):
```bash
# btrace /dev/sdb
  8,16   3        1     0.429604145 20442  A   R 184773879 + 8 <- (8,17) 184773816
  8,16   3        2     0.429604569 20442  Q   R 184773879 + 8 [cksum]
  8,16   3        3     0.429606014 20442  G   R 184773879 + 8 [cksum]
  8,16   3        4     0.429607624 20442  P   N [cksum]
  8,16   3        5     0.429608804 20442  I   R 184773879 + 8 [cksum]
  8,16   3        6     0.429610501 20442  U   N [cksum] 1
  8,16   3        7     0.429611912 20442  D   R 184773879 + 8 [cksum]
  8,16   1        1     0.440227144     0  C   R 184773879 + 8 [0]
```
Tám dòng kết quả đã được báo cáo cho I/O đĩa đơn này, hiển thị từng hành động (sự kiện) liên quan đến hàng đợi thiết bị khối và thiết bị.

Theo mặc định, có bảy cột:
1. Số major, minor của thiết bị
2. CPU ID
3. Số thứ tự (sequence number)
4. Thời gian hành động, tính theo giây
5. Process ID
6. Bộ định danh hành động (action identifier): loại sự kiện (xem tiêu đề Action Identifiers)
7. Mô tả RWBS: các cờ I/O (xem tiêu đề RWBS Description)

Các cột kết quả này có thể được tùy chỉnh bằng tùy chọn -f. Theo sau chúng là dữ liệu tùy chỉnh dựa trên hành động. Dữ liệu cuối cùng tùy thuộc vào hành động. Ví dụ, 184773879 + 8 [cksum] có nghĩa là một I/O tại địa chỉ khối 184773879 với kích thước 8 (cung từ), từ tiến trình có tên cksum.

**Action Identifiers**
Những thứ này được mô tả trong trang man blkparse(1):
- **A:** I/O đã được ánh xạ lại tới một thiết bị khác
- **B:** I/O bounce (đẩy ngược)
- **C:** I/O hoàn thành
- **D:** I/O được phát hành tới driver
- **F:** I/O front được gộp với yêu cầu trên hàng đợi
- **G:** Nhận yêu cầu (get request)
- **I:** I/O được chèn vào hàng đợi yêu cầu
- **M:** I/O back được gộp với yêu cầu trên hàng đợi
- **P:** Plug request (cắm yêu cầu)
- **Q:** I/O được xử lý bởi mã hàng đợi yêu cầu
- **S:** Sleep request (ngủ yêu cầu)
- **T:** Rút phích cắm (unplug) do hết thời gian
- **U:** Unplug request (rút phích cắm yêu cầu)
- **X:** Split (chia nhỏ)

Danh sách này đã được bao gồm vì nó cũng hiển thị các sự kiện mà framework blktrace có thể quan sát.

**Mô tả RWBS**
Để truy vết khả năng quan sát, kernel cung cấp một cách để mô tả loại của mỗi I/O bằng một chuỗi ký tự tên là *rwbs*. rwbs được sử dụng bởi blktrace(8) và các công cụ truy vết khác. Nó được xác định trong hàm kernel `blk_fill_rwbs()` và sử dụng các ký tự:
- **R:** Đọc
- **W:** Ghi
- **M:** Siêu dữ liệu (Metadata)
- **S:** Đồng bộ (Synchronous)
- **A:** Đọc trước (Read-ahead)
- **F:** Flush hoặc ép buộc truy cập đơn vị
- **D:** Discard (hủy bỏ)
- **E:** Erase (xóa)
- **N:** None (không)

Các ký tự có thể được kết hợp. Ví dụ, "WM" là cho các lệnh ghi siêu dữ liệu.

**Lọc hành động (Action Filtering)**
Các lệnh blktrace(8) và btrace(8) có thể lọc các hành động để chỉ hiển thị loại sự kiện quan tâm. Ví dụ, để chỉ truy vết các hành động D (I/O được phát hành), hãy sử dụng bộ lọc `-a issue`:
```bash
# btrace -a issue /dev/sdb
  8,16   1        1     0.000000000   448  D   W 38978223 + 8 [jbd2/sdb]
  8,16   1        2     0.000306181   448  D   W 104685501 + 8 [jbd2/sdb]
  8,16   1        3     0.000496706   448  D   W 104685527 + 24 [jbd2/sdb]
  8,16   1        1     0.010441458 20824  D   R 184944151 + 8 [tar]
[...]
```
Các bộ lọc khác được mô tả trong trang man blktrace(8), bao gồm các tùy chọn chỉ truy vết các lần đọc (-a read), ghi (-a write), hoặc các thao tác đồng bộ (-a sync).

**Phân tích (Analyze)**
Gói blktrace bao gồm btt(1) để phân tích các vết I/O. Dưới đây là một lời gọi ví dụ, bây giờ sử dụng blktrace(8) trên /dev/nvme0n1p1 để ghi các tập tin vết (một thư mục mới được sử dụng vì các lệnh này tạo ra nhiều tập tin):
```bash
# mkdir tracefiles; cd tracefiles
# blktrace -d /dev/nvme0n1p1 -o out -w 10
=== nvme0n1p1 ===
  CPU  0:                20135 events,          944 KiB data
  CPU  1:                38272 events,         1795 KiB data
  Total:                 58407 events (dropped 0),         2738 KiB data
# blkparse -i out.blktrace.* -d out.bin
  259,0    1        1     0.000000000  7113  A  RM 161888 +- (259,1) 159840
  259,0    1        1     0.000000000  7113  A  RM 161888 + 8 <- (259,1) 159840
[...]
# btt -i out.bin
==================== All Devices ====================

            ALL           MIN           AVG           MAX           N
---------------- -----------------------------------------------------------

Q2Q               0.000000001   0.000365336   2.186239507       24625
Q2A               0.000037519   0.000476609   0.001628905        1442
Q2G               0.000000247   0.000007117   0.006140020       15914
G2I               0.000001949   0.000027449   0.000081146         602
Q2M               0.000000139   0.000000198   0.000021066        8720
I2D               0.000022292   0.00008148    0.000030147         602
M2D               0.000001333   0.000188409   0.008407029        8720
D2C               0.000195685   0.000885833   0.006083538       12308
Q2C               0.000198056   0.000964784   0.009578213       12308
[...]
```
Những thống kê này tính theo đơn vị giây, và hiển thị thời gian cho từng giai đoạn của quá trình xử lý I/O. Các thời gian thú vị bao gồm:
- **Q2C:** Tổng thời gian từ yêu cầu I/O cho tới khi hoàn thành (thời gian trong block layer)
- **D2C:** Thời gian từ lúc phát hành thiết bị cho tới khi hoàn thành (độ trễ I/O đĩa)
- **I2D:** Thời gian từ lúc chèn vào hàng đợi thiết bị cho tới khi phát hành thiết bị (thời gian chờ yêu cầu)
- **M2D:** Thời gian từ khi gộp I/O cho tới khi phát hành

Kết quả cho thấy thời gian D2C trung bình là 0.86 ms, và tối đa M2D là 8.4 ms. Các giá trị tối đa như thế này có thể gây ra các giá trị ngoại lai độ trễ I/O.

Để biết thêm thông tin, hãy xem Hướng dẫn sử dụng btt [Brunelle 08].

**Hình ảnh hóa (Visualizations)**
Công cụ blktrace(8) có thể ghi lại các sự kiện vào các tập tin vết có thể được hình ảnh hóa bằng cách sử dụng iowatcher(1), cũng được cung cấp trong gói blktrace, và cũng được hình ảnh hóa bằng cách sử dụng seekwatcher của Chris Mason [Mason 08].

### 9.6.11 bpftrace
bpftrace là một trình truy vết dựa trên BPF cung cấp một ngôn ngữ lập trình cấp cao, cho phép tạo ra các lệnh một dòng mạnh mẽ và các script ngắn. Nó rất phù hợp cho việc phân tích đĩa tùy chỉnh dựa trên các manh mối từ các công cụ khác.

bpftrace được giải thích trong Chương 15, BPF. Phần này hiển thị một số ví dụ cho phân tích đĩa: lệnh một dòng, kích thước I/O đĩa, và độ trễ I/O đĩa.

**Các lệnh Một-Dòng**
Các lệnh một dòng sau đây rất hữu ích và trình diễn các khả năng khác nhau của bpftrace.

Đếm các sự kiện tracepoints I/O khối:
```bash
bpftrace -e 'tracepoint:block:* { @[probe] = count(); }'
```
Tóm tắt kích thước khối I/O dưới dạng một biểu đồ histogram:
```bash
bpftrace -e 't:block:block_rq_issue { @bytes = hist(args->bytes); }'
```
Đếm các vết stack người dùng yêu cầu I/O đĩa:
```bash
bpftrace -e 't:block:block_rq_issue { @[ustack] = count(); }'
bpftrace -e 't:block:block_rq_insert { @[ustack] = count(); }'
```
Đếm các cờ loại I/O khối:
```bash
bpftrace -e 't:block:block_rq_issue { @[args->rwbs] = count(); }'
```
Truy vết các lỗi I/O khối và loại I/O:
```bash
bpftrace -e 't:block:block_rq_complete /args->error/ {
    printf("dev %d type %s error %d
", args->dev, args->rwbs, args->error); }'
```
Đếm các mã vận hành SCSI (SCSI opcodes):
```bash
bpftrace -e 't:scsi:scsi_dispatch_cmd_start { @opcode[args->opcode] =
count(); }'
```
Đếm các mã kết quả SCSI:
```bash
bpftrace -e 't:scsi:scsi_dispatch_cmd_done { @result[args->result] = count(); }'
```
Đếm các chức năng driver SCSI:
```bash
bpftrace -e 'kprobe:scsi* { @[func] = count(); }'
```

**Kích thước I/O Đĩa**
Đôi khi I/O đĩa chậm đơn giản là vì nó lớn, đặc biệt đối với các ổ SSD. Một vấn đề dựa trên kích thước khác là khi một yêu cầu ứng dụng có nhiều I/O nhỏ, thứ có thể được tổng hợp thành các kích thước lớn hơn để giảm bớt các chi phí I/O. Cả hai vấn đề này đều có thể được điều tra bằng cách kiểm tra phân phối kích thước I/O.

Sử dụng bpftrace, phần sau đây cho thấy một phân phối kích thước I/O đĩa được chia nhỏ theo tên tiến trình yêu cầu:
```bash
# bpftrace -e 't:block:block_rq_issue /args->bytes/ { @[comm] = hist(args->bytes); }'
Attaching 1 probe...
^C
[...]
@[kworker/3:1H]:
[4K, 8K)                 1 |@@@@@@@@@@                                              |
[8K, 16K)                0 |                                                        |
[16K, 32K)               0 |                                                        |
[32K, 64K)               0 |                                                        |
[64K, 128K)              0 |                                                        |
[128K, 256K)             0 |                                                        |
[256K, 512K)             0 |                                                        |
[512K, 1M)               5 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[1M, 2M)                 3 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                       |

@[dmcrypt_write]:
[4K, 8K)               103 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[8K, 16K)               46 |***************************************             |
[16K, 32K)              11 |@@@@@                                               |
[32K, 64K)               0 |                                                    |
[64K, 128K)              1 |                                                    |
[128K, 256K)             1 |                                                    |
```
Kết quả cho thấy các tiến trình tên là dmcrypt_write thực hiện các I/O nhỏ, chủ yếu trong phạm vi 4 đến 32 Kbyte.

Tracepoint block:block_rq_issue hiển thị khi I/O được gửi tới driver thiết bị để phân phối cho thiết bị đĩa. Không có đảm bảo rằng tiến trình đang on CPU là tiến trình đã phát ra I/O, đặc biệt đối với I/O được xếp hàng bởi một trình lập lịch, vì vậy tên tiến trình được hiển thị có thể dành cho một luồng kernel chạy muộn hơn thứ đọc I/O từ một hàng đợi để phân phối cho thiết bị. Bạn có thể chuyển đổi tracepoint sang block:block_rq_insert để đo lường từ việc chèn I/O vào một hàng đợi cho phân phối thiết bị. Bạn cũng có thể sử dụng instrumentation I/O khối thứ bỏ qua việc xếp hàng (điều này cũng đã được đề cập trong Mục 9.6.5, perf).

Nếu bạn thêm `args->rwbs` như một histogram key, kết quả sẽ được chia nhỏ hơn nữa theo loại I/O:
```bash
# bpftrace -e 't:block:block_rq_insert /args->bytes/ { @[comm, args->rwbs] =
    hist(args->bytes); }'
Attaching 1 probe...
^C
[...]
@[dmcrypt_write, WS]:
[4K, 8K)                 4 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[8K, 16K)                1 |@@@@@@@@@@@@                                        |
[16K, 32K)               0 |                                                    |
[32K, 64K)               1 |@@@@@@@@@@@@                                        |
[64K, 128K)              1 |@@@@@@@@@@@@                                        |
[128K, 256K)             1 |@@@@@@@@@@@@                                        |

@[dmcrypt_write, W]:
[512K, 1M)               8 |@@@@@@@@@@@                                         |
[1M, 2M)                38 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
```
Kết quả bây giờ bao gồm W cho writes, WS cho synchronous writes, v.v. Xem các mô tả RWBS sớm hơn để có lời giải thích cho các ký tự này.

**Độ trễ I/O Đĩa**
Thời gian phản hồi của đĩa, thường được đề cập đến như độ trễ I/O đĩa, có thể được đo lường bằng cách instrument việc phát hành đĩa tới các sự kiện hoàn thành. Công cụ biolatency.bt thực hiện điều này, hiển thị độ trễ I/O đĩa dưới dạng một biểu đồ histogram. Ví dụ:
```bash
# biolatency.bt
Attaching 4 probes...
Tracing block device I/O... Hit Ctrl-C to end.
^C

@usecs:
[32, 64)                 2 |@                                                   |
[64, 128)                1 |                                                    |
[128, 256)               1 |                                                    |
[256, 512)              27 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      |
[512, 1K)               43 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    |
[1K, 2K)                54 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[2K, 4K)                41 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         |
[4K, 8K)                47 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       |
[8K, 16K)               16 |@@@@@@@@@@@@@@@                                     |
[16K, 32K)               4 |@@@                                                 |
```
Kết quả này cho thấy I/O đĩa thường hoàn thành giữa 256 micro giây và 16 mili giây (16K micro giây).

Mã nguồn là:
```c
#!/usr/local/bin/bpftrace
BEGIN
{
          printf("Tracing block device I/O... Hit Ctrl-C to end.
");
}

tracepoint:block:block_rq_issue
{
          @start[args->dev, args->sector] = nsecs;
}

tracepoint:block:block_rq_complete
/@start[args->dev, args->sector]/
{
          @usecs = hist((nsecs - @start[args->dev, args->sector]) / 1000);
          delete(@start[args->dev, args->sector]);
}

END
{
          clear(@start);
}
```
Việc đo lường độ trễ I/O yêu cầu lưu trữ một dấu thời gian tùy chỉnh cho lúc bắt đầu của mỗi I/O, và sau đó truy xuất nó khi I/O đã hoàn thành để tính toán thời gian đã trôi qua. Khi đo lường VFS hoặc hệ thống tập tin, tôi đã sử dụng một bản đồ BPF được khóa bởi thread ID: việc đó hoạt động vì cùng một luồng VFS đang on CPU cho cả các sự kiện bắt đầu và hoàn thành. Đó không phải là trường hợp với I/O đĩa, vì CPU có thể thực hiện công việc khác trong khi đĩa đang phục vụ một I/O. Thread ID ngẫu nhiên khác cũng có thể đang on CPU cho sự kiện hoàn thành đĩa. Khóa duy nhất là thiết bị và số cung từ: nó giả định rằng chỉ có một I/O đang bay tới một cung từ nhất định tại một thời điểm.

Cũng như với một lệnh một dòng kích thước I/O, bạn có thể thêm `args->rwbs` vào histogram key để chia nhỏ theo loại I/O.

**Các lỗi I/O Đĩa**
Trạng thái lỗi I/O là một đối số cho tracepoint block:block_rq_complete, và chương trình bioerr(8) sau đây (một phiên bản một dòng của chương trình này đã được bao gồm trước đó) sử dụng nó để in các chi tiết cho các thao tác I/O bị lỗi:
```c
#!/usr/local/bin/bpftrace

BEGIN
{
          printf("Tracing block I/O errors. Hit Ctrl-C to end.
");
}

tracepoint:block:block_rq_complete
/args->error != 0/
{
          time("%H:%M:%S ");
          printf("device: %d,%d, sector: %d, bytes: %d, flags: %s, error: %d
",
                 args->dev >> 20, args->dev & ((1 << 20) - 1), args->sector,
                 args->nr_sector * 512, args->rwbs, args->error);
}
```
Tìm kiếm thêm thông tin về một lỗi đĩa có thể yêu cầu các công cụ đĩa cấp thấp hơn, chẳng hạn như ba cái tiếp theo (MegaCli, smartctl, SCSI logging).

### 9.6.12 MegaCli
Các bộ điều khiển đĩa (host bus adapters) bao gồm phần cứng và phần mềm nội bộ bên ngoài hệ thống. Các công cụ phân tích hệ điều hành, ngay cả các tracers động, không thể thấy trực tiếp bên trong các thành phần nội bộ của chúng. Đôi khi hoạt động của chúng có thể được suy luận bằng cách quan sát input và output một cách cẩn thận (bao gồm sử dụng kernel static hoặc dynamic instrumentation), để xem bộ điều khiển đĩa phản hồi như thế nào với một chuỗi I/O.

Có một số công cụ phân tích cho các bộ điều khiển đĩa cụ thể, chẳng hạn như MegaCli của LSI. Phần sau đây hiển thị các sự kiện bộ điều khiển gần đây:
```bash
# MegaCli -AdpEventLog -GetLatest 50 -f lsi.log -aALL
# more lsi.log
seqNum: 0x0000282f
Time: Sat Jun 16 05:55:05 2012
Code: 0x00000023
Class: 0
Locale: 0x20
Event Description: Patrol Read complete
Event Data:
===========
None

seqNum: 0x000027ec
Time: Sat Jun 16 03:00:00 2012
Code: 0x00000027
Class: 0
Locale: 0x20
Event Description: Patrol Read started
[...]
```
Hai sự kiện cuối cùng cho thấy một lệnh patrol read (thứ có thể ảnh hưởng đến hiệu năng) đã xảy ra giữa 3:00 và 5:55 sáng. Các lần đọc patrol đã được đề cập trong Mục 9.4.3, Các loại lưu trữ; chúng đọc các khối đĩa và xác minh các checksum của chúng.

MegaCli có nhiều tùy chọn khác, thứ có thể hiển thị thông tin bộ điều khiển, thông tin thiết bị ảo, thông tin thiết bị vật lý, tình trạng pin, và các lỗi vật lý. Những điều này có thể giúp xác định các vấn đề về cấu hình và các lỗi. Ngay cả với thông tin này, một số loại vấn đề không thể được phân tích dễ dàng, chẳng hạn như lý do tại sao một I/O cụ thể mất hàng trăm mili giây.

Hãy kiểm tra các tài liệu của nhà cung cấp để xem giao diện nào, nếu có, tồn tại cho phân tích bộ điều khiển đĩa.

### 9.6.13 smartctl
Nhiều đĩa hiện đại cung cấp SMART (Self-Monitoring, Analysis and Reporting Technology), thứ cung cấp các thống kê tình trạng đĩa đa dạng. Phần sau đây hiển thị các loại dữ liệu khả dụng (việc này là truy cập vào đĩa đầu tiên trong một thiết bị RAID ảo, sử dụng -d megaraid,0):
```bash
# smartctl --all -d megaraid,0 /dev/sdb
smartctl 5.40 2010-03-16 r3077 [x86_64-unknown-linux-gnu] (local build)
Copyright (C) 2002-10 by Bruce Allen, http://smartmontools.sourceforge.net

Device: SEAGATE  ST3600002SS       Version: ER62
Serial number: 3SS0LM01
Device type: disk
Transport protocol: SAS
Local Time is: Sun Jun 17 10:11:31 2012 UTC
Device supports SMART and is Enabled
Temperature Warning Disabled or Not Supported
SMART Health Status: OK

Current Drive Temperature:     23 C
Drive Trip Temperature:        68 C
Elements in grown defect list: 0
Vendor (Seagate) cache information
  Blocks sent to initiator = 3172800756
  Blocks received from initiator = 2618189622
  Blocks read from cache and sent to initiator = 854615302
  Number of read and write commands whose size <= segment size = 30848143
  Number of read and write commands whose size > segment size = 0
Vendor (Seagate/Hitachi) factory information
  number of hours powered up = 12377.45
  number of minutes until next internal SMART test = 56

Error counter log:
           Errors Corrected by           Total  Correction     Gigabytes    Total
               ECC          rereads/    errors  algorithm      processed  uncorrected
           fast | delayed rewrites  corrected  invocations [10^9 bytes] errors
read:   7416197         0         0   7416197          0      1886.494           0
write:        0         0         0         0          0      1349.999           0
verify: 142475069       0         0 142475069  142475069     22222.134           0

Non-medium error count:      2661

SMART Self-test log
Num  Test              Status                 segment  LifeTime  LBA_first_err [SK ASC ASQ]
     Description                              number   (hours)
# 1  Background long   Completed                  16         3                 - [-    -    -]
# 2  Background short  Completed                  16         0                 - [-    -    -]

Long (extended) Self Test duration: 6400 seconds [106.7 minutes]
```
Trong khi điều này rất hữu ích, nó không có độ phân giải để trả lời các câu hỏi về từng I/O chậm riêng lẻ, vì các kernel tracing frameworks thực hiện điều đó. Thông tin lỗi được sửa chữa nên được sử dụng cho giám sát, để giúp dự đoán lỗi đĩa trước khi nó xảy ra, cũng như để xác nhận rằng một đĩa đã hỏng hoặc đang hỏng.

### 9.6.14 SCSI Logging
Linux có một cơ sở tích hợp cho việc ghi nhật ký sự kiện SCSI. Nó có thể được bật qua sysctl(8) hoặc /proc. Ví dụ, cả hai lệnh sau đây đều thiết lập việc ghi nhật ký ở mức tối đa cho tất cả các loại sự kiện (cảnh báo: tùy thuộc vào khối lượng công việc đĩa của bạn, điều này có thể làm tràn nhật ký hệ thống của bạn):
`# sysctl -w dev.scsi.logging_level=0333333333`
`# echo 0333333333 > /proc/sys/dev/scsi/logging_level`

Định dạng của con số là một trường bit thiết lập mức độ ghi nhật ký từ 1 tới 7 cho 10 loại sự kiện khác nhau (được viết ở đây dưới dạng bát phân; dưới dạng thập lục phân nó là 0x1b6db6db). Trường bit này được định nghĩa trong drivers/scsi/scsi_logging.h. Gói sg3-utils cung cấp một công cụ scsi_logging_level(8) để thiết lập những thứ này. Ví dụ:
`# scsi_logging_level -s --all 3`

Các sự kiện ví dụ:
```bash
# dmesg
[...]
[542136.259412] sd 0:0:0:0: tag#0 Send: scmd 0x0000000001fb89dc
[542136.259422] sd 0:0:0:0: tag#0 CDB: Test Unit Ready 00 00 00 00 00 00
[542136.261103] sd 0:0:0:0: tag#0 Done: SUCCESS Result: hostbyte=DID_OK
driverbyte=DRIVER_OK
[542136.261110] sd 0:0:0:0: tag#0 CDB: Test Unit Ready 00 00 00 00 00 00
[542136.261115] sd 0:0:0:0: tag#0 Sense Key : Not Ready [current]
[542136.261121] sd 0:0:0:0: tag#0 Add. Sense: Medium not present
[542136.261127] sd 0:0:0:0: tag#0 0 sectors total, 0 bytes done.
[...]
```
Điều này có thể được sử dụng để giúp gỡ lỗi các lỗi và hết thời gian (timeouts). Trong khi các dấu thời gian được cung cấp (cột đầu tiên), việc sử dụng chúng để tính toán độ trễ I/O là khó khăn vì thiếu các chi tiết định danh duy nhất.

### 9.6.15 Các công cụ khác (Other Tools)
Các công cụ đĩa có trong các chương khác của cuốn sách này và trong *BPF Performance Tools* [Gregg 19] được liệt kê trong Bảng 9.6.

Bảng 9.6 Các công cụ quan sát đĩa khác
| Mục | Công cụ | Mô tả |
| --- | --- | --- |
| 7.5.1 | vmstat | Các thống kê bộ nhớ ảo bao gồm swapping |
| 7.5.3 | swapon | Sử dụng thiết bị swap |
| [Gregg 19] | seeksize | Hiển thị các khoảng cách seek I/O được yêu cầu |
| [Gregg 19] | biopattern | Nhận diện các mẫu truy cập đĩa ngẫu nhiên/tuần tự |
| [Gregg 19] | bioerr | Truy vết các lỗi đĩa |
| [Gregg 19] | mdflush | Truy vết các yêu cầu flush md |
| [Gregg 19] | iosched | Tóm tắt độ trễ trình lập lịch I/O |
| [Gregg 19] | scsilatency | Hiển thị phân phối độ trễ lệnh SCSI |
| [Gregg 19] | scsiresult | Hiển thị các mã kết quả lệnh SCSI |
| [Gregg 19] | nvmelatency | Tóm tắt độ trễ lệnh trình điều khiển NVMe |

Các công cụ và nguồn quan sát đĩa Linux khác bao gồm:
- **/proc/diskstats:** Các thống kê cho mỗi đĩa cấp cao.
- **seekwatcher:** Hình ảnh hóa các mẫu truy cập đĩa [Mason 08].

Các nhà cung cấp đĩa có thể có các công cụ bổ sung truy cập các thống kê phần sụn, hoặc bằng cách cài đặt một phiên bản gỡ lỗi của firmware.

## 9.7 Hình ảnh hóa (Visualizations)
Có nhiều loại hình ảnh hóa có thể giúp ích trong việc phân tích hiệu năng I/O đĩa. Phần này trình bày các hình ảnh hóa với các ảnh chụp màn hình từ các công cụ khác nhau. Xem Chương 2, Các Phương pháp luận, Mục 2.10, Hình ảnh hóa, để biết thảo luận về các hình ảnh hóa nói chung.

### 9.7.1 Đồ thị đường (Line Graphs)
Các giải pháp giám sát hiệu năng thường vẽ biểu đồ IOPS, thông lượng và mức sử dụng đĩa theo thời gian dưới dạng các đồ thị đường. Điều này giúp minh họa các mẫu dựa trên thời gian, chẳng hạn như các thay đổi trong tải trong ngày, hoặc các sự kiện định kỳ chẳng hạn như các khoảng thời gian flush hệ thống tập tin.

Lưu ý rằng chỉ số được vẽ biểu đồ là mức trung bình. Độ trễ trung bình có thể che giấu các phân phối đa chế độ và các giá trị ngoại lai. Các mức trung bình qua các khoảng thời gian dài cũng có thể che giấu các biến động ngắn hạn hơn.

### 9.7.2 Các biểu đồ phân tán độ trễ (Latency Scatter Plots)
Các biểu đồ phân tán hữu ích cho việc hình ảnh hóa độ trễ I/O cho mỗi sự kiện, thứ có thể bao gồm hàng nghìn sự kiện. Trục x là thời gian hoàn thành, và trục y là thời gian phản hồi I/O. Ví dụ trong Hình 9.11 vẽ 1,400 sự kiện I/O từ một máy chủ cơ sở dữ liệu MySQL sản xuất, được bắt bằng cách sử dụng opensnoop(8) và được vẽ bằng R.

(Hình 9.11 Biểu đồ phân tán về các lệnh đọc và ghi đĩa)

Biểu đồ phân tán hiển thị các lệnh đọc (+) và các lệnh ghi (o) khác nhau. Các chiều khác có thể được vẽ, ví dụ, địa chỉ khối đĩa trên trục y thay vì độ trễ.

Một cặp giá trị ngoại lai độ trễ có thể được thấy ở đây, với các độ trễ trên 150 ms. Lý do cho những giá trị ngoại lai này trước đây không được biết đến. Biểu đồ phân tán này, và những cái khác bao gồm các giá trị ngoại lai tương tự, cho thấy chúng xảy ra sau một đợt bùng phát ghi. Các lệnh ghi được ghi vào thiết bị sau đó trả về từ một bộ điều khiển RAID đệm ẩn ghi ngược, thứ sẽ ghi chúng vào thiết bị sau khi trả về các lần hoàn thành. Tôi nghi ngờ rằng các lệnh đọc đang xếp hàng đằng sau các lệnh ghi thiết bị.

Biểu đồ phân tán này hiển thị một máy chủ duy nhất trong một vài giây. Nhiều máy chủ hoặc các khoảng thời gian dài hơn có thể bắt được nhiều sự kiện hơn nữa, thứ khi được vẽ cùng nhau có thể trở nên khó đọc. Tại thời điểm đó, hãy cân nhắc sử dụng một bản đồ nhiệt độ trễ.

### 9.7.3 Các bản đồ nhiệt độ trễ (Latency Heat Maps)
Một *heat map* có thể được sử dụng để hình ảnh hóa độ trễ, đặt sự trôi qua của thời gian trên trục x, độ trễ I/O trên trục y, và số lượng I/O trong một khoảng thời gian và dải độ trễ nhất định được hiển thị bằng màu sắc (màu càng đậm nghĩa là càng nhiều). Bản đồ nhiệt đã được giới thiệu trong Chương 2, Các Phương pháp luận, Mục 2.10.3, Bản đồ nhiệt. Một ví dụ thú vị về đĩa được trình bày trong Hình 9.12.

Khối lượng công việc được hình ảnh hóa là thực nghiệm: Tôi đã áp dụng các lệnh ghi tuần tự tới nhiều đĩa từng cái một để khám phá các giới hạn bus và bộ điều khiển. Bản đồ nhiệt thu được là bất ngờ (nó đã được mô tả như một loài pterodactyl) và hiển thị thông tin mà lẽ ra đã bị bỏ lỡ khi chỉ xem xét các mức trung bình. Có các lý do kỹ thuật cho từng chi tiết được thấy: ví dụ, "mỏ" kết thúc ở tám đĩa, bằng với số cổng SAS được kết nối (hai cổng x4) và "đầu" bắt đầu ở chín đĩa một khi các cổng đó bắt đầu chịu sự tranh chấp.

Tôi đã phát minh ra các bản đồ nhiệt độ trễ để hình ảnh hóa độ trễ theo thời gian, lấy cảm hứng từ taztool, được mô tả trong Mục tiếp theo. Hình 9.12 là từ Analytics trong thiết bị lưu trữ ZFS của Sun Microsystems [Gregg 10a]: Tôi đã thu thập cái này và các bản đồ nhiệt độ trễ thú vị khác để chia sẻ công khai và thúc đẩy việc sử dụng chúng.

(Hình 9.12 Bản đồ nhiệt độ trễ đĩa)

Trục x và y là giống như một biểu đồ phân tán độ trễ. Ưu điểm chính của các bản đồ nhiệt là chúng có thể mở rộng tới hàng triệu sự kiện, trong khi biểu đồ phân tán trở thành "sơn". Vấn đề này đã được thảo luận trong Chương 2, Mục 2.10.2, Biểu đồ phân tán, và 2.10.3, Bản đồ nhiệt.

### 9.7.4 Các bản đồ nhiệt Offset (Offset Heat Maps)
Vị trí I/O, hay offset, cũng có thể được hình ảnh hóa dưới dạng một bản đồ nhiệt (và có trước các bản đồ nhiệt độ trễ trong điện toán). Hình 9.13 cho thấy một ví dụ.

Offset đĩa (địa chỉ khối) được hiển thị trên trục y, và thời gian trên trục x. Mỗi pixel được tô màu dựa trên số lượng I/O rơi vào khoảng thời gian và dải địa chỉ đó, các màu đậm hơn cho các số lượng lớn hơn. Khối lượng công việc được hình ảnh hóa là một kho lưu trữ hệ thống tập tin, thứ bò qua đĩa từ khối 0. Các đường kẻ đậm hơn chỉ ra I/O tuần tự, và các đám mây màu nhạt hơn chỉ ra I/O ngẫu nhiên.

Sự hình ảnh hóa này đã được giới thiệu vào năm 1995 với taztool của Richard McDougall. Ảnh chụp màn hình này là từ DTraceTazTool, một phiên bản tôi đã viết vào năm 2006. Bản đồ nhiệt offset đĩa có sẵn từ nhiều công cụ, bao gồm seekwatcher (Linux).

(Hình 9.13 Bản đồ nhiệt Offset)

### 9.7.5 Các bản đồ nhiệt Mức sử dụng (Utilization Heat Maps)
Mức sử dụng trên mỗi thiết bị cũng có thể được hiển thị dưới dạng một bản đồ nhiệt, sao cho mức sử dụng đĩa cân bằng và các giá trị ngoại lai riêng lẻ có thể được nhận diện một cách dễ dàng. Trong trường hợp này, mức sử dụng phần trăm là trên trục y, và đĩa (màu sắc càng đậm có nghĩa là càng nhiều đĩa tại mức sử dụng đó). Loại bản đồ nhiệt này có thể được sử dụng cho việc nhận diện các đĩa đơn lẻ chậm chạp, bao gồm cả các sloth disks, như một loại giá trị ngoại lai độ trễ cho mỗi cung từ. Ví dụ, một bản đồ nhiệt mức sử dụng xem Chương 6, CPUs, Mục 6.7.1, Bản đồ nhiệt mức sử dụng.

---

## 9.8 Thực nghiệm (Experimentation)
Phần này mô tả các công cụ cho việc kiểm tra chủ động hiệu năng I/O đĩa. Xem Mục 9.5.9, Micro-Benchmarking, cho một chiến lược được gợi ý để tuân theo.

Khi sử dụng các công cụ này, bạn nên để iostat(1) chạy liên tục sao cho bất kỳ kết quả benchmark nào cũng có thể được kiểm tra chéo ngay lập tức. Một số công cụ micro-benchmark có thể yêu cầu một chế độ thao tác "trực tiếp" để bỏ qua bộ đệm ẩn hệ thống tập tin, và tập trung vào hiệu năng thiết bị đĩa.

### 9.8.1 Ad Hoc (Tùy biến)
Lệnh dd(1) (sao chép thiết bị tới thiết bị) có thể được sử dụng để thực hiện các bài kiểm tra tùy biến về hiệu năng đĩa tuần tự. Các lệnh sau đây viết, và sau đó đọc một tập tin 1 Gbyte có tên file1 với kích thước I/O 1 Mbyte:
- **Ghi:** `dd if=/dev/zero of=file1 bs=1024k count=1k`
- **Đọc:** `dd if=file1 of=/dev/null bs=1024k`

Vì kernel đệm ẩn và buffer dữ liệu, lệnh dd(1) đo lường thông lượng của bộ đệm ẩn và đĩa chứ không chỉ riêng đĩa. Để chỉ kiểm tra hiệu năng của đĩa, bạn có thể sử dụng một ký tự đặc biệt cho đĩa: Trên Linux, lệnh raw(8) (nếu có sẵn) có thể tạo ra các giao diện thô cho đĩa; tuy nhiên, hãy nhận thức rủi ro phá hủy tất cả dữ liệu trên đĩa, bao gồm cả master boot record và bảng phân vùng!

Một cách tiếp cận an toàn hơn là sử dụng cờ I/O trực tiếp (direct I/O) với dd(1) và các tập tin hệ thống tập tin thay vì các thiết bị đĩa. Hãy nhớ rằng bài kiểm tra bây giờ bao gồm cả các chi phí hệ thống tập tin. Ví dụ, thực hiện một bài kiểm tra ghi tới một tập tin mang tên out1:
`# dd if=/dev/zero of=out1 bs=1024k count=1000 oflag=direct`
```bash
1000+0 records in
1000+0 records out
1048576000 bytes (1.0 GB, 1000 MiB) copied, 1.79189 s, 585 MB/s
```
iostat(1) trong một phiên làm việc terminal khác đã xác nhận rằng thông lượng ghi đĩa là khoảng 585 Mbytes/s.

Sử dụng `iflag=direct` cho I/O trực tiếp với các tập tin đầu vào.

### 9.8.2 Các máy phát tải tùy chỉnh (Custom Load Generators)
Để kiểm tra hiệu năng đĩa tùy chỉnh, bạn có thể viết máy phát tải của riêng mình và đo lường hiệu năng kết quả. Một máy phát tải tùy chỉnh có thể là một chương trình C ngắn mở đường dẫn thiết bị và áp dụng các lệnh đọc hoặc ghi. Nếu bạn sử dụng các ngôn ngữ cấp cao hơn, hãy cố gắng sử dụng các giao diện cấp hệ thống để tránh các đợt buffering trong thư viện (ví dụ, sysread() trong Perl) ít nhất là, và lý tưởng nhất là các giao diện buffer kernel cũng như (ví dụ, O_DIRECT).

### 9.8.3 Các công cụ Kiểm thử vi mô (Micro-Benchmark Tools)
Các công cụ benchmark đĩa có sẵn bao gồm, ví dụ, hdparm(8) trên Linux:
```bash
# hdparm -Tt /dev/sdb

/dev/sdb:
 Timing cached reads:   16718 MB in  2.00 seconds = 8367.66 MB/sec
 Timing buffered disk reads:   846 MB in  3.00 seconds = 281.65 MB/sec
```
Tùy chọn -T kiểm tra các lần đọc được đệm ẩn, và -t kiểm tra các lần đọc thiết bị đĩa. Các kết quả cho thấy sự khác biệt đáng kể giữa các lần trúng bộ đệm ẩn trên đĩa và các lần trượt.

Nghiên cứu tài liệu công cụ để hiểu bất kỳ cảnh báo nào, và xem Chương 12, Benchmarking, để biết thêm nền tảng về micro-benchmarking, cho các công cụ có sẵn (trong đó có nhiều công cụ hơn nữa).

### 9.8.4 Ví dụ Đọc Ngẫu nhiên (Random Read Example)
Như một thực nghiệm ví dụ, tôi đã viết một công cụ tùy chỉnh để thực hiện một khối lượng công việc đọc 8 Kbyte ngẫu nhiên của một đường dẫn thiết bị đĩa. Từ một đến năm thực thể của công cụ đã được chạy đồng thời, với iostat(1) đang chạy. Các cột ghi, chứa số không, đã được loại bỏ:
```bash
Device:         rrqm/s       r/s     rkB/s   avgrq-sz  aqu-sz r_await  svctm  %util
sda             878.00    234.00   2224.00      19.01    1.00    4.27   4.27 100.00
[...]
sda            1233.00    311.00   3088.00      19.86    2.00    6.43   3.22 100.00
[...]
sda            1366.00    358.00   3448.00      19.26    3.00    8.44   2.79 100.00
[...]
sda            1775.00    413.00   4376.00      21.19    4.01    9.66   2.42 100.00
[...]
sda            1977.00    423.00   4800.00      22.70    5.04   12.08   2.36 100.00
```
Lưu ý các bước tăng dần trong aqu-sz, và độ trễ r_await tăng lên.

### 9.8.5 ioping
ioping(1) là một công cụ micro-benchmark thú vị giống như tiện ích ping(8) ICMP. Chạy ioping(1) trên thiết bị đĩa nvme0n1:
```bash
# ioping /dev/nvme0n1
4 KiB <<< /dev/nvme0n1 (block device 8 GiB): request=1 time=438.7 us (warmup)
4 KiB <<< /dev/nvme0n1 (block device 8 GiB): request=2 time=421.0 us
4 KiB <<< /dev/nvme0n1 (block device 8 GiB): request=3 time=449.4 us
4 KiB <<< /dev/nvme0n1 (block device 8 GiB): request=4 time=412.6 us
4 KiB <<< /dev/nvme0n1 (block device 8 GiB): request=5 time=468.8 us
^C
--- /dev/nvme0n1 (block device 8 GiB) ioping statistics ---
4 requests completed in 1.75 ms, 16 KiB read, 2.28 k iops, 8.92 MiB/s
generated 5 requests in 4.37 s, 20 KiB, 5 iops, 4.58 KiB/s
min/avg/max/mdev = 412.6 us / 437.9 us / 468.8 us / 22.4 us
```
Theo mặc định, ioping(1) phát ra các lệnh đọc 4 Kbyte mỗi giây và in độ trễ I/O của nó tính bằng micro giây. Khi kết thúc, các thống kê đa dạng được in.

Những gì khiến ioping(1) khác biệt so với các công cụ benchmark khác là khối lượng công việc của nó nhẹ nhàng. Dưới đây là một số kết quả iostat(1) trong khi ioping(1) đang chạy:
```bash
$ iostat -xsz 1
[...]
Device             tps      kB/s    rqm/s   await aqu-sz  areq-sz  %util
nvme0n1           1.00      4.00     0.00    0.44   0.00     4.00   0.40
```
Đĩa đã được đẩy tới mức sử dụng chỉ 0.4%. ioping(1) có khả năng được sử dụng để gỡ lỗi các vấn đề trong các môi trường sản xuất mà các micro-benchmarks khác là không phù hợp, vì chúng thường đẩy các đĩa tới mức sử dụng 100%.

### 9.8.6 fio
Flexible IO Tester (fio) là một công cụ benchmark hệ thống và đĩa có thể làm sáng tỏ hiệu năng đĩa, đặc biệt khi được sử dụng với tùy chọn `--direct=true` để sử dụng non-buffered I/O (khi non-buffered I/O được hỗ trợ bởi hệ thống tập tin). Nó đã được giới thiệu trong Chương 8, Hệ thống tập tin, Mục 8.7.2, Các công cụ Kiểm thử vi mô.

### 9.8.7 blkreplay
Công cụ blkreplay có thể phát lại tải I/O đĩa được bắt bằng blktrace (Mục 9.6.10, blktrace) hoặc Windows DiskMon [Schöbel-Theuer 12]. Điều này có thể hữu ích khi gỡ lỗi các vấn đề đĩa khó tái hiện bằng các công cụ micro-benchmark. Xem Chương 12, Benchmarking, Mục 12.2.3, phát lại, cho một ví dụ về cách phát lại I/O đĩa có thể gây nhầm lẫn nếu mục tiêu đã thay đổi.

---

## 9.9 Tinh chỉnh (Tuning)
Nhiều cách tiếp cận tinh chỉnh đã được bao quát trong Mục 9.5, Phương pháp luận, bao gồm tinh chỉnh bộ đệm ẩn, scaling, và đặc tính hóa khối lượng công việc, thứ có thể giúp bạn xác định và loại bỏ các công việc không cần thiết. Phần cuối cùng của việc tinh chỉnh là cấu hình lưu trữ, thứ có thể được nghiên cứu như một phần của một phương pháp luận tinh chỉnh hiệu năng tĩnh.

Các phần sau đây chỉ ra các khu vực có thể được tinh chỉnh: hệ điều hành, các thiết bị đĩa, và bộ điều khiển đĩa. Các tham số tinh chỉnh có sẵn khác nhau giữa các phiên bản hệ điều hành, các model đĩa, các bộ điều khiển đĩa, và firmware của chúng; hãy xem các tài liệu hướng dẫn tương ứng của chúng. Trong khi thay đổi các tunables có thể dễ dàng thực hiện, các thiết lập mặc định thường là hợp lý và hiếm khi cần tinh chỉnh nhiều.

### 9.9.1 Các Tham số Tinh chỉnh Hệ điều hành
Những thứ này bao gồm ionice(1), các kiểm soát tài nguyên, và các tham số tinh chỉnh kernel.

**ionice**
Trên Linux, lệnh ionice(1) có thể được sử dụng để thiết lập một lớp lập lịch I/O và mức ưu tiên cho một tiến trình. Các lớp lập lịch được xác định bằng số:
- **0, none:** Không có lớp nào được chỉ định, vì vậy kernel sẽ chọn một mặc định—nỗ lực tốt nhất, với một mức ưu tiên dựa trên giá trị nice của tiến trình.
- **1, real-time:** Mức ưu tiên cao nhất tới đĩa. Nếu lạm dụng, điều này có thể làm chết đói các tiến trình khác (giống như lớp lập lịch RT CPU).
- **2, best effort:** Lớp lập lịch mặc định, hỗ trợ các mức ưu tiên 0–7, với 0 là cao nhất.
- **3, idle:** I/O đĩa chỉ được cho phép sau một khoảng thời gian chờ của sự rảnh rỗi đĩa.

Ví dụ sử dụng:
`# ionice -c 3 -p 1623`
Điều này đặt tiến trình PID 1623 vào lớp lập lịch I/O idle. Điều này có thể là mong muốn cho các tác vụ backup dài hạn sao cho chúng ít có khả năng can thiệp vào khối lượng công việc sản xuất.

**Các kiểm soát Tài nguyên (Resource Controls)**
Các hệ điều hành hiện đại cung cấp các kiểm soát tài nguyên để quản lý mức sử dụng đĩa I/O theo các cách tùy chỉnh. Cho Linux, hệ thống con container groups (cgroups) block I/O (blkio) cung cấp các kiểm soát bổ sung đa dạng. Những điều này bao gồm:
- **memory.limit_in_bytes:** Bộ nhớ người dùng tối đa cho phép, bao gồm sử dụng bộ đệm ẩn tập tin, tính theo byte.
- **memory.memsw.limit_in_bytes:** Tổng bộ nhớ và không gian swap tối đa cho phép, tính theo byte (khi swap đang được sử dụng).
- **memory.kmem.limit_in_bytes:** Bộ nhớ kernel tối đa cho phép, tính theo byte.
- **memory.tcp.limit_in_bytes:** Bộ nhớ đệm TCP tối đa cho phép, tính theo byte.
- **memory.swappiness:** Tương tự như vm.swappiness đã được mô tả trước đó nhưng có thể được thiết lập cho một cgroup.
- **memory.oom_control:** Có thể được thiết lập thành 0, để cho phép OOM killer cho cgroup này, hoặc 1, để vô hiệu hóa nó.

Linux cũng cho phép cấu hình trên toàn hệ thống trong /etc/security/limits.conf. Để biết thêm về các kiểm soát tài nguyên, hãy xem Chương 11, Điện toán đám mây.

**Các tham số Tinh chỉnh (Tunable Parameters)**
Các tunables của kernel Linux ví dụ bao gồm:
- **/sys/block/*/queue/scheduler:** Để chọn chính sách lập lịch I/O: những thứ này có thể bao gồm noop, deadline, cfq, v.v. Xem các mô tả trước đó về những thứ này trong Mục 9.4, Kiến trúc.
- **/sys/block/*/queue/nr_requests:** Số lượng yêu cầu đọc hoặc ghi có thể được cấp phát bởi block layer.
- **/sys/block/*/queue/read_ahead_kb:** Số lượng Kbytes tối đa mà hệ thống tập tin sẽ đọc trước (read ahead) cho các yêu cầu.

Cũng như với các tunables kernel khác, hãy kiểm tra tài liệu để biết danh sách đầy đủ, các mô tả, và các cảnh báo. Trong mã nguồn Linux, xem Documentation/block/queue-sysfs.txt.

### 9.9.2 Các Tham số Tinh chỉnh Thiết bị Đĩa
Trên Linux, công cụ hdparm(8) có thể thiết lập các tunables thiết bị đĩa đa dạng, bao gồm quản lý điện năng và các thời hạn hết thời gian spin-down [Archlinux 20]. Hãy cực kỳ cẩn thận khi sử dụng công cụ này và nghiên cứu trang man hdparm(8)—nhiều tùy chọn khác nhau được đánh dấu là "DANGEROUS" (nguy hiểm) vì chúng có thể dẫn đến mất dữ liệu.

### 9.9.3 Các Tham số Tinh chỉnh Bộ điều khiển Đĩa
Các tham số tinh chỉnh bộ điều khiển đĩa khả dụng tùy thuộc vào model bộ điều khiển đĩa và nhà cung cấp. Để cung cấp cho bạn một ý tưởng về những gì những thứ này có thể bao gồm, phần sau đây trình bày một số thiết lập từ một card Dell PERC 6, được xem bằng cách sử dụng lệnh MegaCli:
```bash
# MegaCli -AdpAllInfo -aALL
[...]
Predictive Fail Poll Interval     : 300sec
Interrupt Throttle Active Count   : 16
Interrupt Throttle Completion     : 50us
Rebuild Rate                      : 30%
PR Rate                           : 0%
BGI Rate                          : 1%
Check Consistency Rate            : 1%
Reconstruction Rate               : 30%
Cache Flush Interval              : 30s
Max Drives to Spinup at One Time  : 2
Delay Among Spinup Groups         : 12s
Physical Drive Coercion Mode      : 128MB
Cluster Mode                      : Disabled
Alarm                             : Disabled
Auto Rebuild                      : Enabled
Battery Warning                   : Enabled
Ecc Bucket Size                   : 15
Ecc Bucket Leak Rate              : 1440 Minutes
Load Balance Mode                 : Auto
[...]
```
Mỗi thiết lập có một cái tên khá dễ hiểu và được mô tả chi tiết hơn trong tài liệu của nhà cung cấp.

---

## 9.10 Các bài tập (Exercises)
1. Trả lời các câu hỏi sau về thuật ngữ đĩa:
   - IOPS là gì?
   - Sự khác biệt giữa thời gian dịch vụ và thời gian chờ là gì?
   - Đợi I/O (I/O wait time) là gì?
   - Giá trị ngoại lai độ trễ là gì?
   - Lệnh đĩa không truyền tải dữ liệu là gì?

2. Trả lời các câu hỏi khái niệm sau:
   - Mô tả mức sử dụng đĩa và độ bão hòa.
   - Mô tả sự khác biệt về hiệu năng giữa I/O đĩa ngẫu nhiên và tuần tự.
   - Mô tả vai trò của một bộ đệm ẩn trên đĩa cho việc đọc và ghi I/O.

3. Trả lời các câu hỏi sâu hơn sau:
   - Giải thích tại sao mức sử dụng (phần trăm bận rộn) của các đĩa ảo có thể gây nhầm lẫn.
   - Giải thích tại sao chỉ số "I/O wait" có thể gây nhầm lẫn.
   - Mô tả các đặc tính hiệu năng của RAID-0 (striping) và RAID-1 (mirroring).
   - Mô tả những gì xảy ra khi các đĩa bị quá tải, bao gồm cả ảnh hưởng đến hiệu năng ứng dụng.
   - Mô tả những gì xảy ra khi bộ điều khiển lưu trữ bị quá tải với công việc (hoặc thông lượng hoặc IOPS), bao gồm cả ảnh hưởng đến hiệu năng ứng dụng.

4. Phát triển các quy trình sau cho hệ điều hành của bạn:
   - Một checklist phương pháp USE cho các thiết bị đĩa (và các bộ điều khiển). Bao gồm cách lấy mỗi chỉ số (ví dụ, lệnh nào để thực thi) và cách diễn giải kết quả. Thử sử dụng các công cụ quan sát hệ điều hành hiện có trước tiên khi cài đặt các sản phẩm phần mềm bổ sung.
   - Một checklist đặc tính hóa khối lượng công việc cho các tài nguyên đĩa. Bao gồm cách lấy mỗi chỉ số, và thử sử dụng các công cụ quan sát hệ điều hành hiện có trước tiên.

5. Mô tả hành vi đĩa có thể thấy trong kết quả iostat(1) Linux duy nhất này:
```bash
$ iostat -x 1
[...]
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.23    0.00   45.16   31.18    0.00   20.43

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s  avgrq-sz
avgqu-sz   await r_await w_await  svctm  %util
vda              39.78 13156.99  800.00  151.61 3466.67 41200.00     93.88
11.99    7.49    0.57   44.01   0.49  46.56
vdb               0.00     0.00    0.00    0.00     0.00      0.00      0.00
0.00     0.00    0.00    0.00   0.00   0.00
```

6. (tùy chọn, nâng cao) Phát triển một công cụ để truy vết tất cả các lệnh đĩa *ngoại trừ* các lệnh đọc và ghi. Điều này có thể yêu cầu truy vết ở cấp độ SCSI.

---

## 9.11 Các tài liệu tham khảo (References)
- [Patterson 88] Patterson, D., Gibson, G., and Kats, R., “A Case for Redundant Arrays of Inexpensive Disks,” *ACM SIGMOD*, 1988.
- [McDougall 06a] McDougall, R., Mauro, J., and Gregg, B., *Solaris Performance and Tools: DTrace and MDB Techniques for Solaris 10 and OpenSolaris*, Prentice Hall, 2006.
- [Brunelle 08] Brunelle, A., “btt User Guide,” blktrace package, /usr/share/doc/blktrace/btt.pdf, 2008.
- [Gregg 08] Gregg, B., “Shouting in the Datacenter,” https://www.youtube.com/watch?v=tDacjrSCeq4, 2008.
- [Mason 08] Mason, C., “Seekwatcher,” https://oss.oracle.com/~mason/seekwatcher, 2008.
- [Smith 09] Smith, R., “Western Digital’s Advanced Format: The 4K Sector Transition Begins,” https://www.anandtech.com/show/2888, 2009.
- [Gregg 10a] Gregg, B., “Visualizing System Latency,” *Communications of the ACM*, July 2010.
- [Love 10] Love, R., *Linux Kernel Development*, 3rd Edition, Addison-Wesley, 2010.
- [Turner 10] Turner, J., “Effects of Data Center Vibration on Compute System Performance,” *USENIX SustainIT*, 2010.
- [Gregg 11b] Gregg, B., “Utilization Heat Maps,” http://www.brendangregg.com/HeatMaps/utilization.html, published 2011.
- [Cassidy 12] Cassidy, C., “SLC vs MLC: Which Works Best for High-Reliability Applications?” https://www.eetimes.com/slc-vs-mlc-which-works-best-for-high-reliability-applications/#, 2012.
- [Cornwell 12] Cornwell, M., “Anatomy of a Solid-State Drive,” *Communications of the ACM*, December 2012.
- [Schöbel-Theuer 12] Schöbel-Theuer, T., “blkreplay - a Testing and Benchmarking Toolkit,” http://www.blkreplay.org, 2012.
- [Chazagain 13] Chazagain, G., “Iotop,” http://guichaz.free.fr/iotop, 2013.
- [Corbet 13b] Corbet, J., “The multiqueue block layer,” *LWN.net*, https://lwn.net/Articles/552904, 2013.
- [Leventhal 13] Leventhal, A., “A File System All Its Own,” *ACM Queue*, March 2013.
- [Cai 15] Cai, Y., Luo, Y., Haratsch, E. F., Mai, K., and Mutlu, O., “Data Retention in MLC NAND Flash Memory: Characterization, Optimization, and Recovery,” *IEEE 21st International Symposium on High Performance Computer Architecture (HPCA)*, 2015. https://users.ece.cmu.edu/~omutlu/pub/flash-memory-data-retention_hpca15.pdf
- [FICA 18] “Industry’s Fastest Storage Networking Speed Announced by Fibre Channel Industry Association—64GFC and Gen 7 Fibre Channel,” *Fibre Channel Industry Association*, https://fibrechannel.org/industrys-fastest-storage-networking-speed-announced-by-fibre-channel-industry-association-64gfc-and-gen-7-fibre-channel, 2018.
- [Hady 18] Hady, F., “Achieve Consistent Low Latency for Your Storage-Intensive Workloads,” low-latency-for-storage-intensive-workloads-article-brief.html, 2018.
- [Gregg 19] Gregg, B., *BPF Performance Tools: Linux System and Application Observability*, Addison-Wesley, 2019.
- [Archlinux 20] “hdparm,” https://wiki.archlinux.org/index.php/Hdparm, last updated 2020.
- [Dell 20] “PowerEdge RAID Controller,” https://www.dell.com/support/article/en-us/sln312338/poweredge-raid-controller?lang=en, accessed 2020.
- [FCIA 20] “Features,” *Fibre Channel Industry Association*, https://fibrechannel.org/fibre-channel-features, accessed 2020.
- [Liu 20] Liu, L., “Samsung QVO vs EVO vs PRO: What’s the Difference? [Clone Disk],” https://www.partitionwizard.com/clone-disk/samsung-qvo-vs-evo-vs-pro.html, 2020.
- [Mellor 20] Mellor, C., “Western Digital Shingled Out in Lawsuit for Sneaking RAID-unfriendly Tech into Drives for RAID arrays,” *TheRegister*, https://www.theregister.com/2020/05/29/wd_class_action_lawsuit, 2020.
- [Netflix 20] “Open Connect Appliances,” https://openconnect.netflix.com/en/appliances, accessed 2020.
- [NVMe 20] “NVM Express,” https://nvmexpress.org, accessed 2020.
- [Torvalds 20a] Torvalds, L., “Re: Do not blame anyone. Please give polite, constructive criticism,” https://www.realworldtech.com/forum/?threadid=189711&curpostid=189841, 2020.
