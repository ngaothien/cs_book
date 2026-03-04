# Chương 4: Công cụ Quan sát (Observability Tools)

Các hệ điều hành trong lịch sử đã cung cấp nhiều công cụ để quan sát các thành phần phần mềm và phần cứng của hệ thống. Đối với người mới, phạm vi rộng lớn của các công cụ và chỉ số có sẵn gợi ý rằng mọi thứ — hoặc ít nhất là mọi thứ quan trọng — đều có thể được quan sát. Trong thực tế, có nhiều khoảng trống, và các chuyên gia hiệu năng hệ thống đã trở nên thành thạo trong nghệ thuật suy luận và diễn giải: tìm ra hoạt động từ các công cụ và thống kê gián tiếp. Ví dụ, các gói tin mạng có thể được kiểm tra riêng lẻ (sniffing), nhưng I/O đĩa thì không thể (ít nhất là không dễ dàng).

Khả năng quan sát (observability) đã được cải thiện đáng kể trong Linux nhờ sự phát triển của các công cụ truy vết động (dynamic tracing), bao gồm BCC và bpftrace dựa trên BPF. Các góc tối giờ đã được chiếu sáng, bao gồm I/O đĩa riêng lẻ sử dụng biosnoop(8). Tuy nhiên, nhiều công ty và sản phẩm giám sát thương mại vẫn chưa áp dụng truy vết hệ thống, và đang bỏ lỡ những hiểu biết mà nó mang lại. Tôi đã dẫn đầu con đường này bằng cách phát triển, xuất bản, và giải thích các công cụ truy vết mới, những công cụ đã được sử dụng bởi các công ty như Netflix và Facebook.

Các mục tiêu học tập của chương này là:

- Xác định các công cụ hiệu năng tĩnh (static performance tools) và các công cụ khẩn cấp (crisis tools).
- Hiểu các loại công cụ và chi phí của chúng: bộ đếm (counter), lập hồ sơ (profiling), và truy vết (tracing).
- Tìm hiểu về các nguồn khả năng quan sát, bao gồm: /proc, /sys, tracepoint, kprobe, uprobe, USDT, và PMC.
- Tìm hiểu cách cấu hình sar(1) để lưu trữ thống kê.

Trong Chương 1, tôi đã giới thiệu các loại khả năng quan sát khác nhau: bộ đếm, lập hồ sơ, và truy vết, cũng như thiết bị đo đạc tĩnh (static instrumentation) và thiết bị đo đạc động (dynamic instrumentation). Chương này giải thích chi tiết các công cụ quan sát và nguồn dữ liệu của chúng, bao gồm tóm tắt về sar(1), công cụ báo cáo hoạt động hệ thống (system activity reporter), và giới thiệu về các công cụ truy vết. Điều này cung cấp cho bạn những kiến thức thiết yếu để hiểu khả năng quan sát của Linux; các chương sau (6 đến 11) sử dụng các công cụ và nguồn này để giải quyết các vấn đề cụ thể. Các Chương 13 đến 15 đề cập chi tiết về các trình truy vết (tracer).

Chương này sử dụng bản phân phối Ubuntu Linux làm ví dụ; hầu hết các công cụ này đều giống nhau trên các bản phân phối Linux khác, và một số công cụ tương tự tồn tại trên các nhân và hệ điều hành khác nơi các công cụ này bắt nguồn.

## 4.1 Phạm vi Công cụ (Tool Coverage)

Hình 4.1 cho thấy sơ đồ hệ điều hành mà tôi đã chú thích với các công cụ quan sát khối lượng công việc Linux<sup>1</sup> liên quan đến từng thành phần.

*Hình 4.1: Các công cụ quan sát khối lượng công việc Linux*

Hầu hết các công cụ này tập trung vào một tài nguyên cụ thể, chẳng hạn như CPU, bộ nhớ, hoặc đĩa, và được đề cập trong một chương sau dành riêng cho tài nguyên đó. Có một số công cụ đa năng (multi-tool) có thể phân tích nhiều lĩnh vực, và chúng được giới thiệu sau trong chương này: perf, Ftrace, BCC, và bpftrace.

### 4.1.1 Công cụ Hiệu năng Tĩnh (Static Performance Tools)

Có một loại khả năng quan sát khác kiểm tra các thuộc tính của hệ thống ở trạng thái nghỉ thay vì dưới khối lượng công việc hoạt động. Điều này đã được mô tả là phương pháp tinh chỉnh hiệu năng tĩnh (static performance tuning methodology) trong Chương 2, Phương pháp luận, Mục 2.5.17, Tinh chỉnh Hiệu năng Tĩnh, và các công cụ này được hiển thị trong Hình 4.2.

> <sup>1</sup> Khi giảng dạy các lớp hiệu năng vào giữa những năm 2000, tôi thường vẽ sơ đồ nhân riêng trên bảng trắng và chú thích bằng các công cụ hiệu năng khác nhau và những gì chúng quan sát. Tôi thấy đó là cách hiệu quả để giải thích phạm vi công cụ như một dạng bản đồ tư duy. Kể từ đó, tôi đã xuất bản các phiên bản kỹ thuật số, trang trí các vách ngăn văn phòng trên khắp thế giới. Bạn có thể tải chúng trên trang web của tôi [Gregg 20a].

*Hình 4.2: Các công cụ tinh chỉnh hiệu năng tĩnh Linux*

Hãy nhớ sử dụng các công cụ trong Hình 4.2 để kiểm tra các vấn đề về cấu hình và thành phần. Đôi khi các vấn đề hiệu năng chỉ đơn giản là do cấu hình sai (misconfiguration).

### 4.1.2 Công cụ Khẩn cấp (Crisis Tools)

Khi bạn gặp một cuộc khủng hoảng hiệu năng sản xuất đòi hỏi nhiều công cụ hiệu năng khác nhau để gỡ lỗi, bạn có thể thấy rằng không có công cụ nào được cài đặt. Tệ hơn, vì máy chủ đang gặp vấn đề hiệu năng, việc cài đặt các công cụ có thể mất nhiều thời gian hơn bình thường, kéo dài cuộc khủng hoảng.

Đối với Linux, Bảng 4.1 liệt kê các gói cài đặt được khuyến nghị hoặc kho mã nguồn cung cấp các công cụ khẩn cấp này. Tên gói cho Ubuntu/Debian được hiển thị trong bảng này (tên gói này có thể khác nhau giữa các bản phân phối Linux khác nhau).

**Bảng 4.1: Các gói công cụ khẩn cấp Linux**

| Gói (Package) | Cung cấp (Provides) |
|---|---|
| procps | ps(1), vmstat(8), uptime(1), top(1) |
| util-linux | dmesg(1), lsblk(1), lscpu(1) |
| sysstat | iostat(1), mpstat(1), pidstat(1), sar(1) |
| iproute2 | ip(8), ss(8), nstat(8), tc(8) |
| numactl | numastat(8) |
| linux-tools-common linux-tools-$(uname -r) | perf(1), turbostat(8) |
| bcc-tools (hay bpfcc-tools) | opensnoop(8), execsnoop(8), runqlat(8), runqlen(8), softirqs(8), hardirqs(8), ext4slower(8), ext4dist(8), biotop(8), biosnoop(8), biolatency(8), tcptop(8), tcplife(8), trace(8), argdist(8), funccount(8), stackcount(8), profile(8), và nhiều hơn nữa |
| bpftrace | bpftrace, các phiên bản cơ bản của opensnoop(8), execsnoop(8), runqlat(8), runqlen(8), biosnoop(8), biolatency(8), và nhiều hơn nữa |
| perf-tools-unstable | Phiên bản Ftrace của opensnoop(8), execsnoop(8), iolatency(8), iosnoop(8), bitesize(8), funccount(8), kprobe(8) |
| trace-cmd | trace-cmd(1) |
| nicstat | nicstat(1) |
| ethtool | ethtool(8) |
| tiptop | tiptop(1) |
| msr-tools | rdmsr(8), wrmsr(8) |
| github.com/brendangregg/msr-cloud-tools | showboost(8), cpuhot(8), cputemp(8) |
| github.com/brendangregg/pmc-cloud-tools | pmcarch(8), cpucache(8), icache(8), tlbstat(8), resstalls(8) |

Các công ty lớn, chẳng hạn như Netflix, có các đội hệ điều hành và hiệu năng đảm bảo rằng các hệ thống sản xuất đã cài đặt tất cả các gói này. Một bản phân phối Linux mặc định có thể chỉ cài đặt procps và util-linux, vì vậy tất cả các gói khác phải được thêm vào.

Trong môi trường container, có thể mong muốn tạo một container gỡ lỗi đặc quyền (privileged debugging container) có toàn quyền truy cập vào hệ thống<sup>2</sup> và tất cả các công cụ đã được cài đặt. Image cho container này có thể được cài đặt trên các máy chủ container và triển khai khi cần.

Việc thêm các gói công cụ thường chưa đủ: phần mềm nhân và không gian người dùng cũng có thể cần được cấu hình để hỗ trợ các công cụ này. Các công cụ truy vết thường yêu cầu một số tùy chọn CONFIG nhân nhất định phải được kích hoạt, chẳng hạn như CONFIG_FTRACE và CONFIG_BPF. Các công cụ lập hồ sơ thường yêu cầu phần mềm được cấu hình để hỗ trợ duyệt ngăn xếp (stack walking), bằng cách sử dụng các phiên bản biên dịch với con trỏ khung (frame-pointer) của tất cả phần mềm (bao gồm các thư viện hệ thống: libc, libpthread, v.v.) hoặc các gói debuginfo được cài đặt để hỗ trợ duyệt ngăn xếp DWARF. Nếu công ty của bạn chưa thực hiện điều này, bạn nên kiểm tra rằng mỗi công cụ hiệu năng hoạt động và sửa những công cụ không hoạt động trước khi chúng cần thiết gấp trong một cuộc khủng hoảng.

> <sup>2</sup> Nó cũng có thể được cấu hình để chia sẻ namespace với một container mục tiêu cần phân tích.

Các phần sau giải thích chi tiết hơn về các công cụ quan sát hiệu năng.

## 4.2 Các Loại Công cụ (Tool Types)

Một cách phân loại hữu ích cho các công cụ quan sát là liệu chúng cung cấp khả năng quan sát toàn hệ thống (system-wide) hay theo tiến trình (per-process), và liệu chúng dựa trên bộ đếm (counter) hay sự kiện (event). Các thuộc tính này được hiển thị trong Hình 4.3, cùng với các ví dụ công cụ Linux.

*Hình 4.3: Các loại công cụ quan sát*

Một số công cụ nằm trong nhiều hơn một phần tư; ví dụ, top(1) cũng có tóm tắt toàn hệ thống, và các công cụ sự kiện toàn hệ thống thường có thể lọc cho một tiến trình cụ thể (-p PID).

Các công cụ dựa trên sự kiện bao gồm trình lập hồ sơ (profiler) và trình truy vết (tracer). Trình lập hồ sơ quan sát hoạt động bằng cách lấy một loạt các ảnh chụp nhanh (snapshot) về các sự kiện, vẽ nên một bức tranh thô về mục tiêu. Trình truy vết đo đạc mọi sự kiện quan tâm, và có thể thực hiện xử lý trên chúng, ví dụ để tạo các bộ đếm tùy chỉnh. Bộ đếm, truy vết, và lập hồ sơ đã được giới thiệu trong Chương 1.

Các phần sau mô tả các công cụ Linux sử dụng bộ đếm cố định (fixed counter), truy vết, và lập hồ sơ, cũng như các công cụ thực hiện giám sát (monitoring) (chỉ số - metrics).

### 4.2.1 Bộ đếm Cố định (Fixed Counters)

Nhân duy trì nhiều bộ đếm khác nhau để cung cấp thống kê hệ thống. Chúng thường được triển khai dưới dạng số nguyên không dấu (unsigned integer) được tăng khi các sự kiện xảy ra. Ví dụ, có các bộ đếm cho số lượng gói tin mạng nhận được, I/O đĩa được phát hành, và ngắt đã xảy ra. Chúng được phần mềm giám sát phơi bày dưới dạng chỉ số (xem Mục 4.2.4, Giám sát).

Một cách tiếp cận nhân phổ biến là duy trì một cặp bộ đếm tích lũy: một để đếm sự kiện và một để ghi lại tổng thời gian trong sự kiện. Chúng cung cấp trực tiếp số đếm sự kiện và thời gian trung bình (hoặc độ trễ) trong sự kiện, bằng cách chia tổng thời gian cho số đếm. Vì chúng là tích lũy, bằng cách đọc cặp này tại một khoảng thời gian (ví dụ: một giây), delta có thể được tính toán, và từ đó có được số đếm trên giây và độ trễ trung bình. Đây là cách nhiều thống kê hệ thống được tính toán.

Về mặt hiệu năng, các bộ đếm được coi là "miễn phí" để sử dụng vì chúng được kích hoạt mặc định và được nhân duy trì liên tục. Chi phí bổ sung duy nhất khi sử dụng chúng là hành động đọc giá trị từ không gian người dùng (không đáng kể). Các công cụ ví dụ sau đây đọc các bộ đếm toàn hệ thống hoặc theo tiến trình.

**Toàn hệ thống (System-Wide)**

Các công cụ này kiểm tra hoạt động toàn hệ thống trong ngữ cảnh của tài nguyên phần mềm hoặc phần cứng hệ thống, sử dụng các bộ đếm nhân. Các công cụ Linux bao gồm:

- vmstat(8): Thống kê bộ nhớ ảo và vật lý, toàn hệ thống
- mpstat(1): Sử dụng theo CPU
- iostat(1): Sử dụng I/O theo đĩa, được báo cáo từ giao diện thiết bị khối (block device)
- nstat(8): Thống kê ngăn xếp TCP/IP
- sar(1): Nhiều thống kê khác nhau; cũng có thể lưu trữ chúng để báo cáo lịch sử

Các công cụ này thường có thể xem được bởi tất cả người dùng trên hệ thống (không cần root). Thống kê của chúng cũng thường được vẽ đồ thị bởi phần mềm giám sát.

Nhiều công cụ tuân theo quy ước sử dụng nơi chúng chấp nhận một khoảng thời gian (interval) và số đếm (count) tùy chọn, ví dụ, vmstat(8) với khoảng thời gian một giây và số đếm đầu ra là ba:

```
$ vmstat 1 3
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 4  0 1446428 662012 142100 5644676   1    4    28   152   33    1 29  8 63  0  0
 4  0 1446428 665988 142116 5642272   0    0     0   284 4957 4969 51  0 48  0  0
 4  0 1446428 685116 142116 5623676   0    0     0     0 4488 5507 52  0 48  0  0
```

Dòng đầu ra đầu tiên là tóm tắt kể từ khi khởi động (summary-since-boot), hiển thị giá trị trung bình cho toàn bộ thời gian hệ thống đã hoạt động. Các dòng tiếp theo là tóm tắt khoảng thời gian một giây, hiển thị hoạt động hiện tại. Ít nhất, đây là ý định: phiên bản Linux này trộn lẫn giá trị tổng kết và giá trị hiện tại cho dòng đầu tiên (các cột bộ nhớ là giá trị hiện tại; vmstat(8) được giải thích trong Chương 7).

**Theo tiến trình (Per-Process)**

Các công cụ này hướng đến tiến trình và sử dụng các bộ đếm mà nhân duy trì cho mỗi tiến trình. Các công cụ Linux bao gồm:

- ps(1): Hiển thị trạng thái tiến trình, hiển thị nhiều thống kê tiến trình khác nhau, bao gồm sử dụng bộ nhớ và CPU.
- top(1): Hiển thị các tiến trình hàng đầu, sắp xếp theo sử dụng CPU hoặc thống kê khác.
- pmap(1): Liệt kê các phân đoạn bộ nhớ tiến trình với thống kê sử dụng.

Các công cụ này thường đọc thống kê từ hệ thống tệp /proc.

### 4.2.2 Lập hồ sơ (Profiling)

Lập hồ sơ mô tả đặc điểm mục tiêu bằng cách thu thập một tập hợp các mẫu (sample) hoặc ảnh chụp nhanh (snapshot) về hành vi của nó. Sử dụng CPU là mục tiêu phổ biến của lập hồ sơ, nơi các mẫu dựa trên bộ hẹn giờ (timer-based sample) được lấy từ con trỏ lệnh (instruction pointer) hoặc dấu vết ngăn xếp (stack trace) để mô tả đặc điểm các đường dẫn mã tiêu thụ CPU. Các mẫu này thường được thu thập ở tốc độ cố định, chẳng hạn như 100 Hz (chu kỳ mỗi giây) trên tất cả CPU, và trong thời gian ngắn như một phút. Các công cụ lập hồ sơ, hay trình lập hồ sơ (profiler), thường sử dụng 99 Hz thay vì 100 Hz để tránh lấy mẫu đồng bộ với hoạt động mục tiêu, điều có thể dẫn đến đếm thừa hoặc đếm thiếu (over- or undercounting).

Lập hồ sơ cũng có thể dựa trên các sự kiện phần cứng không theo thời gian (untimed hardware event), chẳng hạn như lỗi bộ nhớ đệm phần cứng CPU (CPU hardware cache miss) hoặc hoạt động bus. Nó có thể cho thấy đường dẫn mã nào chịu trách nhiệm, thông tin đặc biệt có thể giúp các nhà phát triển tối ưu hóa mã của họ cho việc sử dụng bộ nhớ.

Không giống như bộ đếm cố định, lập hồ sơ (và truy vết) thường chỉ được kích hoạt khi cần, vì chúng có thể tốn một số chi phí CPU để thu thập, và chi phí lưu trữ để chứa. Độ lớn của chi phí này phụ thuộc vào công cụ và tốc độ sự kiện mà nó đo đạc. Các trình lập hồ sơ dựa trên bộ hẹn giờ thường an toàn hơn: tốc độ sự kiện được biết trước, vì vậy chi phí có thể được dự đoán, và tốc độ sự kiện có thể được chọn sao cho chi phí không đáng kể.

**Toàn hệ thống (System-Wide)**

Các trình lập hồ sơ toàn hệ thống Linux bao gồm:

- perf(1): Trình lập hồ sơ Linux tiêu chuẩn, bao gồm các lệnh con lập hồ sơ.
- profile(8): Trình lập hồ sơ CPU dựa trên BPF từ kho BCC (được đề cập trong Chương 15, BPF) đếm tần suất các dấu vết ngăn xếp trong ngữ cảnh nhân.
- Intel VTune Amplifier XE: Lập hồ sơ Linux và Windows, với giao diện đồ họa bao gồm duyệt mã nguồn.

Chúng cũng có thể được sử dụng để nhắm mục tiêu một tiến trình đơn lẻ.

**Theo tiến trình (Per-Process)**

Các trình lập hồ sơ hướng tiến trình bao gồm:

- gprof(1): Công cụ lập hồ sơ GNU, phân tích thông tin lập hồ sơ được thêm bởi trình biên dịch (ví dụ: gcc -pg).
- cachegrind: Một công cụ từ bộ công cụ valgrind, có thể lập hồ sơ sử dụng bộ nhớ đệm phần cứng (và nhiều hơn nữa) và trực quan hóa hồ sơ bằng kcachegrind.
- Java Flight Recorder (JFR): Các ngôn ngữ lập trình thường có các trình lập hồ sơ mục đích đặc biệt riêng có thể kiểm tra ngữ cảnh ngôn ngữ. Ví dụ, JFR cho Java.

Xem Chương 6, CPU, và Chương 13, perf, để biết thêm về các công cụ lập hồ sơ.

### 4.2.3 Truy vết (Tracing)

Truy vết đo đạc mọi lần xuất hiện của một sự kiện, và có thể lưu trữ chi tiết dựa trên sự kiện để phân tích sau hoặc tạo tóm tắt. Điều này tương tự với lập hồ sơ, nhưng mục đích là thu thập hoặc kiểm tra tất cả sự kiện, không chỉ một mẫu. Truy vết có thể phát sinh chi phí CPU và lưu trữ cao hơn so với lập hồ sơ, điều có thể làm chậm mục tiêu truy vết. Điều này nên được xem xét, vì nó có thể ảnh hưởng tiêu cực đến khối lượng công việc sản xuất, và các dấu thời gian (timestamp) đo được cũng có thể bị lệch bởi trình truy vết. Giống như lập hồ sơ, truy vết thường chỉ được sử dụng khi cần.

Ghi nhật ký (logging), nơi các sự kiện không thường xuyên như lỗi và cảnh báo được ghi vào tệp nhật ký để đọc sau, có thể được coi là truy vết tần suất thấp được kích hoạt mặc định. Nhật ký bao gồm nhật ký hệ thống (system log).

Dưới đây là các ví dụ về công cụ truy vết toàn hệ thống và theo tiến trình.

**Toàn hệ thống (System-Wide)**

Các công cụ truy vết này kiểm tra hoạt động toàn hệ thống trong ngữ cảnh của tài nguyên phần mềm hoặc phần cứng hệ thống, sử dụng các cơ sở truy vết nhân. Các công cụ Linux bao gồm:

- tcpdump(8): Truy vết gói tin mạng (sử dụng libpcap)
- biosnoop(8): Truy vết I/O khối (sử dụng BCC hoặc bpftrace)
- execsnoop(8): Truy vết tiến trình mới (sử dụng BCC hoặc bpftrace)
- perf(1): Trình lập hồ sơ Linux tiêu chuẩn, cũng có thể truy vết sự kiện
- perf trace: Một lệnh con perf đặc biệt truy vết các lời gọi hệ thống toàn hệ thống
- Ftrace: Trình truy vết tích hợp sẵn của Linux
- BCC: Thư viện và bộ công cụ truy vết dựa trên BPF
- bpftrace: Trình truy vết (bpftrace(8)) và bộ công cụ dựa trên BPF

perf(1), Ftrace, BCC, và bpftrace được giới thiệu trong Mục 4.5, Công cụ Truy vết, và được đề cập chi tiết trong các Chương 13 đến 15. Có hơn một trăm công cụ truy vết được xây dựng bằng BCC và bpftrace, bao gồm biosnoop(8) và execsnoop(8) từ danh sách này. Nhiều ví dụ hơn được cung cấp xuyên suốt cuốn sách này.

**Theo tiến trình (Per-Process)**

Các công cụ truy vết này hướng đến tiến trình, cũng như các framework hệ điều hành mà chúng dựa trên. Các công cụ Linux bao gồm:

- strace(1): Truy vết lời gọi hệ thống
- gdb(1): Trình gỡ lỗi cấp mã nguồn

Các trình gỡ lỗi có thể kiểm tra dữ liệu từng sự kiện, nhưng chúng phải làm điều đó bằng cách dừng và khởi động lại việc thực thi mục tiêu. Điều này có thể đi kèm với chi phí rất lớn, khiến chúng không phù hợp cho sử dụng trong sản xuất.

Các công cụ truy vết toàn hệ thống như perf(1) và bpftrace hỗ trợ bộ lọc để kiểm tra một tiến trình đơn lẻ và có thể hoạt động với chi phí thấp hơn nhiều, khiến chúng được ưa chuộng hơn khi có sẵn.

### 4.2.4 Giám sát (Monitoring)

Giám sát đã được giới thiệu trong Chương 2, Phương pháp luận. Không giống như các loại công cụ đã đề cập trước đó, giám sát ghi lại thống kê liên tục trong trường hợp chúng cần thiết sau này.

**sar(1)**

Một công cụ truyền thống để giám sát một máy chủ hệ điều hành đơn lẻ là System Activity Reporter — sar(1), có nguồn gốc từ AT&T Unix. sar(1) dựa trên bộ đếm và có một tác nhân (agent) thực thi theo thời gian được lên lịch (qua cron) để ghi lại trạng thái của các bộ đếm toàn hệ thống. Công cụ sar(1) cho phép xem các giá trị này tại dòng lệnh, ví dụ:

```
# sar
Linux 4.15.0-66-generic (bgregg)        12/21/2019      _x86_64_        (8 CPU)

12:00:01 AM     CPU     %user     %nice   %system   %iowait    %steal     %idle
12:05:01 AM     all      3.34      0.00      0.95      0.04      0.00     95.66
12:10:01 AM     all      2.93      0.00      0.87      0.04      0.00     96.16
12:15:01 AM     all      3.05      0.00      1.38      0.18      0.00     95.40
12:20:01 AM     all      3.02      0.00      0.88      0.03      0.00     96.06
[...]
Average:        all      0.00      0.00      0.00      0.00      0.00      0.00
```

Theo mặc định, sar(1) đọc kho lưu trữ thống kê của nó (nếu được kích hoạt) để in các thống kê lịch sử gần đây. Bạn có thể chỉ định khoảng thời gian và số đếm tùy chọn để nó kiểm tra hoạt động hiện tại theo tốc độ đã chỉ định.

sar(1) có thể ghi lại hàng chục thống kê khác nhau để cung cấp cái nhìn sâu về CPU, bộ nhớ, đĩa, mạng, ngắt, sử dụng năng lượng, và nhiều hơn nữa. Nó được đề cập chi tiết hơn trong Mục 4.4, sar.

Các sản phẩm giám sát của bên thứ ba thường được xây dựng trên sar(1) hoặc cùng thống kê khả năng quan sát mà nó sử dụng, và phơi bày các chỉ số này qua mạng.

**SNMP**

Công nghệ truyền thống cho giám sát mạng là Giao thức Quản lý Mạng Đơn giản (Simple Network Management Protocol — SNMP). Các thiết bị và hệ điều hành có thể hỗ trợ SNMP và trong một số trường hợp cung cấp nó theo mặc định, tránh cần cài đặt các tác nhân hoặc trình xuất (exporter) của bên thứ ba. SNMP bao gồm nhiều chỉ số hệ điều hành cơ bản, mặc dù nó chưa được mở rộng để bao phủ các ứng dụng hiện đại. Hầu hết các môi trường đã chuyển sang giám sát dựa trên tác nhân tùy chỉnh thay thế.

**Các tác nhân (Agents)**

Phần mềm giám sát hiện đại chạy các tác nhân (còn gọi là trình xuất — exporter hoặc plugin) trên mỗi hệ thống để ghi lại các chỉ số nhân và ứng dụng. Chúng có thể bao gồm các tác nhân cho các ứng dụng và mục tiêu cụ thể, ví dụ, máy chủ cơ sở dữ liệu MySQL, Máy chủ Web Apache, và hệ thống bộ nhớ đệm Memcached. Các tác nhân như vậy có thể cung cấp các chỉ số yêu cầu ứng dụng chi tiết không có sẵn chỉ từ các bộ đếm hệ thống.

Phần mềm và tác nhân giám sát cho Linux bao gồm:

- Performance Co-Pilot (PCP): PCP hỗ trợ hàng chục tác nhân khác nhau (gọi là Performance Metric Domain Agent — PMDA), bao gồm cho các chỉ số dựa trên BPF [PCP 20].
- Prometheus: Phần mềm giám sát Prometheus hỗ trợ hàng chục trình xuất khác nhau, cho cơ sở dữ liệu, phần cứng, nhắn tin, lưu trữ, HTTP, API, và ghi nhật ký [Prometheus 20].
- collectd: Hỗ trợ hàng chục plugin khác nhau.

Một kiến trúc giám sát ví dụ được minh họa trong Hình 4.4 bao gồm một máy chủ cơ sở dữ liệu giám sát để lưu trữ chỉ số, và một máy chủ web giám sát để cung cấp giao diện người dùng cho khách hàng. Các chỉ số được gửi (hoặc cung cấp) bởi các tác nhân đến máy chủ cơ sở dữ liệu và sau đó được cung cấp cho giao diện người dùng khách hàng để hiển thị dưới dạng đồ thị đường và trong bảng điều khiển (dashboard). Ví dụ, Graphite Carbon là máy chủ cơ sở dữ liệu giám sát, và Grafana là máy chủ web/bảng điều khiển giám sát.

*Hình 4.4: Kiến trúc giám sát ví dụ*

Có hàng chục sản phẩm giám sát, và hàng trăm tác nhân khác nhau cho các loại mục tiêu khác nhau. Đề cập tất cả nằm ngoài phạm vi của cuốn sách này. Tuy nhiên, có một mẫu số chung được đề cập ở đây: thống kê hệ thống (dựa trên bộ đếm nhân). Các thống kê hệ thống được hiển thị bởi các sản phẩm giám sát thường giống với những thống kê được hiển thị bởi các công cụ hệ thống: vmstat(8), iostat(1), v.v. Học các công cụ này sẽ giúp bạn hiểu các sản phẩm giám sát, ngay cả khi bạn không bao giờ sử dụng các công cụ dòng lệnh. Các công cụ này được đề cập trong các chương sau.

Một số sản phẩm giám sát đọc các chỉ số hệ thống bằng cách chạy các công cụ hệ thống và phân tích đầu ra văn bản, điều này không hiệu quả. Các sản phẩm giám sát tốt hơn sử dụng các giao diện thư viện và nhân để đọc trực tiếp các chỉ số — cùng giao diện được sử dụng bởi các công cụ dòng lệnh. Các nguồn này được đề cập trong phần tiếp theo, tập trung vào mẫu số chung nhất: các giao diện nhân.

## 4.3 Các Nguồn Khả năng Quan sát (Observability Sources)

Các phần tiếp theo mô tả các giao diện khác nhau cung cấp dữ liệu cho các công cụ quan sát trên Linux. Chúng được tóm tắt trong Bảng 4.2.

**Bảng 4.2: Các nguồn khả năng quan sát Linux**

| Loại (Type) | Nguồn (Source) |
|---|---|
| Bộ đếm theo tiến trình (Per-process counters) | /proc |
| Bộ đếm toàn hệ thống (System-wide counters) | /proc, /sys |
| Cấu hình và bộ đếm thiết bị (Device configuration and counters) | /sys |
| Thống kê cgroup (Cgroup statistics) | /sys/fs/cgroup |
| Truy vết theo tiến trình (Per-process tracing) | ptrace |
| Bộ đếm phần cứng (Hardware counters — PMC) | perf_event |
| Thống kê mạng (Network statistics) | netlink |
| Bắt gói tin mạng (Network packet capture) | libpcap |
| Chỉ số độ trễ theo luồng (Per-thread latency metrics) | Delay accounting |
| Truy vết toàn hệ thống (System-wide tracing) | Function profiling (Ftrace), tracepoint, software event, kprobe, uprobe, perf_event |

Các nguồn chính của thống kê hiệu năng hệ thống được đề cập tiếp theo: /proc và /sys. Sau đó, các nguồn Linux khác được đề cập: delay accounting, netlink, tracepoint, kprobe, USDT, uprobe, PMC, và nhiều hơn nữa.

Các trình truy vết được đề cập trong Chương 13 perf, Chương 14 Ftrace, và Chương 15 BPF sử dụng nhiều nguồn này, đặc biệt là truy vết toàn hệ thống. Phạm vi của các nguồn truy vết này được minh họa trong Hình 4.5, cùng với tên sự kiện và nhóm: ví dụ, block: dành cho tất cả các tracepoint I/O khối, bao gồm block:block_rq_issue.

*Hình 4.5: Các nguồn truy vết Linux*

Chỉ một vài nguồn USDT ví dụ được minh họa trong Hình 4.5, cho cơ sở dữ liệu PostgreSQL (postgres:), trình biên dịch JVM hotspot (hotspot:), và libc (libc:). Bạn có thể có nhiều hơn tùy thuộc vào phần mềm cấp người dùng của bạn.

Để biết thêm thông tin về cách tracepoint, kprobe, và uprobe hoạt động, chi tiết bên trong của chúng được tài liệu hóa trong Chương 2 của BPF Performance Tools [Gregg 19].

### 4.3.1 /proc

Đây là giao diện hệ thống tệp cho thống kê nhân. /proc chứa một số thư mục, trong đó mỗi thư mục được đặt tên theo ID tiến trình cho tiến trình mà nó đại diện. Trong mỗi thư mục này có một số tệp chứa thông tin và thống kê về mỗi tiến trình, được ánh xạ từ các cấu trúc dữ liệu nhân. Có thêm các tệp trong /proc cho thống kê toàn hệ thống.

/proc được nhân tạo động và không được hỗ trợ bởi thiết bị lưu trữ (nó chạy trong bộ nhớ). Nó chủ yếu là chỉ đọc, cung cấp thống kê cho các công cụ quan sát. Một số tệp có thể ghi, để kiểm soát hành vi tiến trình và nhân.

Giao diện hệ thống tệp rất tiện lợi: đó là một framework trực quan để phơi bày thống kê nhân cho user-land qua cây thư mục, và có giao diện lập trình nổi tiếng qua các lời gọi hệ thống tệp POSIX: open(), read(), close(). Bạn cũng có thể khám phá nó tại dòng lệnh sử dụng cd, cat(1), grep(1), và awk(1). Hệ thống tệp cũng cung cấp bảo mật cấp người dùng thông qua sử dụng quyền truy cập tệp. Trong các trường hợp hiếm khi các công cụ quan sát tiến trình thông thường (ps(1), top(1), v.v.) không thể thực thi, một số gỡ lỗi tiến trình vẫn có thể được thực hiện bởi các lệnh tích hợp shell từ thư mục /proc.

Chi phí đọc hầu hết các tệp /proc là không đáng kể; ngoại lệ bao gồm một số tệp liên quan đến bản đồ bộ nhớ (memory-map) phải duyệt bảng trang (page table).

**Thống kê theo tiến trình (Per-Process Statistics)**

Nhiều tệp được cung cấp trong /proc cho thống kê theo tiến trình. Đây là ví dụ về những gì có thể có sẵn (Linux 5.4), ở đây xem PID 18733:

```
$ ls -F /proc/18733
arch_status   environ    mountinfo    personality  statm
attr/         exe@       mounts       projid_map   status
autogroup     fd/        mountstats   root@        syscall
auxv          fdinfo/    net/         sched        task/
cgroup        gid_map    ns/          schedstat    timers
clear_refs    io         numa_maps    sessionid    timerslack_ns
cmdline       limits     oom_adj      setgroups    uid_map
comm          loginuid   oom_score    smaps        wchan
coredump_filter map_files/ oom_score_adj smaps_rollup
cpuset        maps       pagemap      stack
cwd@          mem        patch_state  stat
```

Bạn cũng có thể kiểm tra /proc/self cho tiến trình hiện tại (shell) của mình.

Danh sách chính xác các tệp có sẵn phụ thuộc vào phiên bản nhân và các tùy chọn CONFIG. Những tệp liên quan đến khả năng quan sát hiệu năng theo tiến trình bao gồm:

- limits: Giới hạn tài nguyên có hiệu lực
- maps: Các vùng bộ nhớ được ánh xạ
- sched: Nhiều thống kê bộ lập lịch CPU khác nhau
- schedstat: Thời gian chạy CPU, độ trễ, và lát thời gian
- smaps: Các vùng bộ nhớ được ánh xạ với thống kê sử dụng
- stat: Trạng thái và thống kê tiến trình, bao gồm tổng sử dụng CPU và bộ nhớ
- statm: Tóm tắt sử dụng bộ nhớ theo đơn vị trang
- status: Thông tin stat và statm, có nhãn
- fd: Thư mục các liên kết tượng trưng bộ mô tả tệp (cũng xem fdinfo)
- cgroup: Thông tin thành viên cgroup
- task: Thư mục thống kê theo tác vụ (luồng)

Phần sau cho thấy cách thống kê theo tiến trình được top(1) đọc, được truy vết bằng strace(1):

```
stat("/proc/14704", {st_mode=S_IFDIR|0555, st_size=0, ...}) = 0
open("/proc/14704/stat", O_RDONLY)        = 4
read(4, "14704 (sshd) S 1 14704 14704 0 -"..., 1023) = 232
close(4)
```

Điều này đã mở một tệp gọi là "stat" trong thư mục được đặt tên theo ID tiến trình (14704), và sau đó đọc nội dung tệp.

top(1) lặp lại điều này cho tất cả các tiến trình hoạt động trên hệ thống. Trên một số hệ thống, đặc biệt những hệ thống có nhiều tiến trình, chi phí thực hiện các thao tác này có thể trở nên đáng chú ý, đặc biệt với các phiên bản top(1) lặp lại chuỗi này cho mọi tiến trình ở mỗi lần cập nhật màn hình. Điều này có thể dẫn đến tình huống top(1) báo cáo rằng chính top là tiến trình tiêu thụ CPU cao nhất!

**Thống kê toàn hệ thống (System-Wide Statistics)**

Linux cũng đã mở rộng /proc để bao gồm thống kê toàn hệ thống, chứa trong các tệp và thư mục bổ sung sau:

```
$ cd /proc; ls -Fd [a-z]*
acpi/        dma          kallsyms     mdstat        schedstat     thread-self@
buddyinfo    driver/      kcore        meminfo       scsi/         timer_list
bus/         execdomains  keys         misc          self@         tty/
cgroups      fb           key-users    modules       slabinfo      uptime
cmdline      filesystems  kmsg         mounts@       softirqs      version
consoles     fs/          kpagecgroup  mtrr          stat          vmallocinfo
cpuinfo      interrupts   kpagecount   net@          swaps         vmstat
crypto       iomem        kpageflags   pagetypeinfo  sys/
devices      ioports      loadavg      partitions    sysrq-trigger
diskstats    irq/         locks        sched_debug   sysvipc/      zoneinfo
```

Các tệp toàn hệ thống liên quan đến khả năng quan sát hiệu năng bao gồm:

- cpuinfo: Thông tin bộ xử lý vật lý, bao gồm mọi CPU ảo, tên mô hình, tốc độ xung nhịp, và kích thước bộ nhớ đệm.
- diskstats: Thống kê I/O đĩa cho tất cả thiết bị đĩa
- interrupts: Bộ đếm ngắt theo CPU
- loadavg: Tải trung bình (load average)
- meminfo: Phân tích sử dụng bộ nhớ hệ thống
- net/dev: Thống kê giao diện mạng
- net/netstat: Thống kê mạng toàn hệ thống
- net/tcp: Thông tin socket TCP hoạt động
- pressure/: Các tệp thông tin áp lực trì hoãn (Pressure Stall Information — PSI)
- schedstat: Thống kê bộ lập lịch CPU toàn hệ thống
- self: Liên kết tượng trưng đến thư mục ID tiến trình hiện tại, để tiện lợi
- slabinfo: Thống kê bộ nhớ đệm bộ cấp phát slab nhân
- stat: Tóm tắt thống kê nhân và tài nguyên hệ thống: CPU, đĩa, phân trang, hoán đổi, tiến trình
- zoneinfo: Thông tin vùng bộ nhớ (memory zone)

Chúng được đọc bởi các công cụ toàn hệ thống. Ví dụ, đây là vmstat(8) đọc /proc, được truy vết bởi strace(1):

```
open("/proc/meminfo", O_RDONLY)           = 3
lseek(3, 0, SEEK_SET)                     = 0
read(3, "MemTotal:       889484 kB\nMemF"..., 2047) = 1170
open("/proc/stat", O_RDONLY)              = 4
read(4, "cpu  14901 0 18094 102149804 131"..., 65535) = 804
open("/proc/vmstat", O_RDONLY)            = 5
lseek(5, 0, SEEK_SET)                     = 0
read(5, "nr_free_pages 160568\nnr_inactive"..., 2047) = 1998
```

Đầu ra này cho thấy vmstat(8) đang đọc meminfo, stat, và vmstat.

**Độ chính xác Thống kê CPU**

Tệp /proc/stat cung cấp thống kê sử dụng CPU toàn hệ thống và được sử dụng bởi nhiều công cụ (vmstat(8), mpstat(1), sar(1), các tác nhân giám sát). Độ chính xác của các thống kê này phụ thuộc vào cấu hình nhân. Cấu hình mặc định (CONFIG_TICK_CPU_ACCOUNTING) đo sử dụng CPU với độ chi tiết của tick đồng hồ [Weisbecker 13], có thể là bốn mili giây (tùy thuộc vào CONFIG_HZ). Điều này thường đủ. Có các tùy chọn để cải thiện độ chính xác bằng cách sử dụng bộ đếm độ phân giải cao hơn, mặc dù với chi phí hiệu năng nhỏ (VIRT_CPU_ACCOUNTING_NATIVE và VIRT_CPU_ACCOUNTING_GEN), cũng như tùy chọn cho thời gian IRQ chính xác hơn (IRQ_TIME_ACCOUNTING). Một cách tiếp cận khác để có được phép đo sử dụng CPU chính xác là sử dụng MSR hoặc PMC.

**Nội dung Tệp**

Các tệp /proc thường được định dạng văn bản, cho phép chúng được đọc dễ dàng từ dòng lệnh và xử lý bởi các công cụ shell scripting. Ví dụ:

```
$ cat /proc/meminfo
MemTotal:       15923672 kB
MemFree:        10919912 kB
MemAvailable:   15407564 kB
Buffers:           94536 kB
Cached:          2512040 kB
SwapCached:            0 kB
Active:          1671088 kB
[...]
$ grep Mem /proc/meminfo
MemTotal:       15923672 kB
MemFree:        10918292 kB
MemAvailable:   15405968 kB
```

Mặc dù điều này tiện lợi, nó thêm một lượng nhỏ chi phí cho nhân để mã hóa thống kê dưới dạng văn bản, và cho bất kỳ công cụ user-land nào sau đó phân tích văn bản. netlink, được đề cập trong Mục 4.3.4, netlink, là giao diện nhị phân hiệu quả hơn.

Nội dung của /proc được tài liệu hóa trong trang man proc(5) và trong tài liệu nhân Linux: Documentation/filesystems/proc.txt [Bowden 20]. Một số phần có tài liệu mở rộng, chẳng hạn như diskstats trong Documentation/iostats.txt và thống kê bộ lập lịch trong Documentation/scheduler/sched-stats.txt. Ngoài tài liệu, bạn cũng có thể nghiên cứu mã nguồn nhân để hiểu nguồn gốc chính xác của tất cả các mục trong /proc. Cũng có thể hữu ích khi đọc mã nguồn của các công cụ sử dụng chúng.

Một số mục /proc phụ thuộc vào tùy chọn CONFIG: schedstats được kích hoạt với CONFIG_SCHEDSTATS, sched với CONFIG_SCHED_DEBUG, và pressure với CONFIG_PSI.

### 4.3.2 /sys

Linux cung cấp hệ thống tệp sysfs, được gắn trên /sys, được giới thiệu cùng nhân 2.6 để cung cấp cấu trúc dựa trên thư mục cho thống kê nhân. Điều này khác với /proc, đã phát triển theo thời gian và nhiều thống kê hệ thống phần lớn được thêm vào thư mục cấp cao nhất. sysfs ban đầu được thiết kế để cung cấp thống kê trình điều khiển thiết bị nhưng đã được mở rộng để bao gồm bất kỳ loại thống kê nào.

Ví dụ, phần sau liệt kê các tệp /sys cho CPU 0 (được cắt ngắn):

```
$ find /sys/devices/system/cpu/cpu0 -type f
/sys/devices/system/cpu/cpu0/uevent
/sys/devices/system/cpu/cpu0/hotplug/target
/sys/devices/system/cpu/cpu0/hotplug/state
/sys/devices/system/cpu/cpu0/hotplug/fail
/sys/devices/system/cpu/cpu0/crash_notes_size
/sys/devices/system/cpu/cpu0/power/runtime_active_time
/sys/devices/system/cpu/cpu0/power/runtime_active_kids
/sys/devices/system/cpu/cpu0/power/pm_qos_resume_latency_us
/sys/devices/system/cpu/cpu0/power/runtime_usage
[...]
/sys/devices/system/cpu/cpu0/topology/die_id
/sys/devices/system/cpu/cpu0/topology/physical_package_id
/sys/devices/system/cpu/cpu0/topology/core_cpus_list
/sys/devices/system/cpu/cpu0/topology/die_cpus_list
/sys/devices/system/cpu/cpu0/topology/core_siblings
[...]
```

Nhiều tệp được liệt kê cung cấp thông tin về bộ nhớ đệm phần cứng CPU. Đầu ra sau hiển thị nội dung của chúng (sử dụng grep(1) để tên tệp được bao gồm cùng đầu ra):

```
$ grep . /sys/devices/system/cpu/cpu0/cache/index*/level
/sys/devices/system/cpu/cpu0/cache/index0/level:1
/sys/devices/system/cpu/cpu0/cache/index1/level:1
/sys/devices/system/cpu/cpu0/cache/index2/level:2
/sys/devices/system/cpu/cpu0/cache/index3/level:3
$ grep . /sys/devices/system/cpu/cpu0/cache/index*/size
/sys/devices/system/cpu/cpu0/cache/index0/size:32K
/sys/devices/system/cpu/cpu0/cache/index1/size:32K
/sys/devices/system/cpu/cpu0/cache/index2/size:1024K
/sys/devices/system/cpu/cpu0/cache/index3/size:33792K
```

Điều này cho thấy CPU 0 có quyền truy cập vào hai bộ nhớ đệm Cấp 1, mỗi cái 32 Kbyte, một bộ nhớ đệm Cấp 2 là 1 Mbyte, và một bộ nhớ đệm Cấp 3 là 33 Mbyte.

Hệ thống tệp /sys thường có hàng chục nghìn thống kê trong các tệp chỉ đọc, cũng như nhiều tệp có thể ghi để thay đổi trạng thái nhân. Ví dụ, CPU có thể được đặt thành trực tuyến (online) hoặc ngoại tuyến (offline) bằng cách ghi "1" hoặc "0" vào một tệp có tên "online." Cũng như đọc thống kê, một số thiết lập trạng thái có thể được thực hiện bằng cách sử dụng chuỗi văn bản tại dòng lệnh (echo 1 > filename), thay vì giao diện nhị phân.

### 4.3.3 Delay Accounting

Các hệ thống Linux có tùy chọn CONFIG_TASK_DELAY_ACCT theo dõi thời gian cho mỗi tác vụ ở các trạng thái sau:

- Độ trễ bộ lập lịch (Scheduler latency): Chờ đến lượt trên CPU
- I/O khối (Block I/O): Chờ I/O khối hoàn thành
- Hoán đổi (Swapping): Chờ phân trang (áp lực bộ nhớ)
- Thu hồi bộ nhớ (Memory reclaim): Chờ thủ tục thu hồi bộ nhớ

Về mặt kỹ thuật, thống kê độ trễ bộ lập lịch có nguồn từ schedstats (đã đề cập trước đó, trong /proc) nhưng được phơi bày cùng với các trạng thái delay accounting khác. (Nó nằm trong struct sched_info, không phải struct task_delay_info.)

Các thống kê này có thể được đọc bởi các công cụ cấp người dùng sử dụng taskstats, đây là giao diện dựa trên netlink để lấy thống kê theo tác vụ và tiến trình. Trong mã nguồn nhân có:

- Documentation/accounting/delay-accounting.txt: tài liệu
- tools/accounting/getdelays.c: ví dụ về trình tiêu thụ

Sau đây là một số đầu ra từ getdelays.c:

```
$ ./getdelays -dp 17451
print delayacct stats ON
PID     17451
CPU             count     real total  virtual total    delay total
                  386    3452475144    31387115236     1253300657
IO              count    delay total  delay average
                  302    1535758266          5ms
SWAP            count    delay total  delay average
                    0              0          0ms
RECLAIM         count    delay total  delay average
                    0              0          0ms
```

Thời gian được tính bằng nano giây trừ khi có quy định khác. Ví dụ này được lấy từ một hệ thống chịu tải CPU nặng, và tiến trình được kiểm tra đang chịu độ trễ bộ lập lịch.

### 4.3.4 netlink

netlink là một họ địa chỉ socket đặc biệt (AF_NETLINK) để lấy thông tin nhân. Sử dụng netlink bao gồm mở một socket mạng với họ địa chỉ AF_NETLINK và sau đó sử dụng một loạt các lời gọi send(2) và recv(2) để truyền yêu cầu và nhận thông tin trong các cấu trúc nhị phân (binary struct). Mặc dù đây là giao diện phức tạp hơn để sử dụng so với /proc, nhưng nó hiệu quả hơn, và cũng hỗ trợ thông báo (notification). Thư viện libnetlink hỗ trợ việc sử dụng.

Cũng như với các công cụ trước đó, strace(1) có thể được sử dụng để cho thấy thông tin nhân đến từ đâu. Kiểm tra công cụ thống kê socket ss(8):

```
# strace ss
[...]
socket(AF_NETLINK, SOCK_RAW|SOCK_CLOEXEC, NETLINK_SOCK_DIAG) = 3
[...]
```

Đây là mở một socket AF_NETLINK cho nhóm NETLINK_SOCK_DIAG, trả về thông tin về socket. Nó được tài liệu hóa trong trang man sock_diag(7). Các nhóm netlink bao gồm:

- NETLINK_ROUTE: Thông tin định tuyến (cũng có /proc/net/route)
- NETLINK_SOCK_DIAG: Thông tin socket
- NETLINK_SELINUX: Thông báo sự kiện SELinux
- NETLINK_AUDIT: Kiểm toán (bảo mật)
- NETLINK_SCSITRANSPORT: Truyền tải SCSI
- NETLINK_CRYPTO: Thông tin mật mã nhân

Các lệnh sử dụng netlink bao gồm ip(8), ss(8), routel(8), và các lệnh cũ hơn ifconfig(8) và netstat(8).


### 4.3.5 Tracepoint

Tracepoint là một nguồn sự kiện nhân Linux dựa trên thiết bị đo đạc tĩnh (static instrumentation), một thuật ngữ đã được giới thiệu trong Chương 1, Giới thiệu, Mục 1.7.3, Truy vết. Tracepoint là các điểm đo đạc được mã hóa cứng (hard-coded) đặt tại các vị trí logic trong mã nhân. Ví dụ, có các tracepoint tại đầu và cuối các lời gọi hệ thống, sự kiện bộ lập lịch, thao tác hệ thống tệp, và I/O đĩa.<sup>4</sup> Cơ sở hạ tầng tracepoint được phát triển bởi Mathieu Desnoyers và lần đầu có sẵn trong bản phát hành Linux 2.6.32 vào năm 2009. Tracepoint là một API ổn định<sup>5</sup> và bị giới hạn về số lượng.

Tracepoint là một tài nguyên quan trọng cho phân tích hiệu năng vì chúng cung cấp năng lượng cho các công cụ truy vết nâng cao vượt ra ngoài thống kê tóm tắt, cung cấp cái nhìn sâu hơn vào hành vi nhân. Trong khi truy vết dựa trên hàm (function-based tracing) có thể cung cấp sức mạnh tương tự (ví dụ: Mục 4.3.6, kprobe), chỉ tracepoint mới cung cấp giao diện ổn định, cho phép phát triển các công cụ mạnh mẽ.

Phần này giải thích về tracepoint. Chúng có thể được sử dụng bởi các trình truy vết được giới thiệu trong Mục 4.5, Công cụ Truy vết, và được đề cập chi tiết trong các Chương 13 đến 15.

> <sup>4</sup> Một số tracepoint bị kiểm soát bởi các tùy chọn Kconfig và có thể không có sẵn nếu nhân được biên dịch mà không có chúng; ví dụ: tracepoint rcu và CONFIG_RCU_TRACE.

> <sup>5</sup> Tôi gọi nó là "ổn định theo nỗ lực tốt nhất" (best-effort stable). Hiếm khi xảy ra, nhưng tôi đã thấy tracepoint thay đổi.

**Ví dụ Tracepoint**

Các tracepoint có sẵn có thể được liệt kê bằng lệnh perf list (cú pháp cho perf(1) được đề cập trong Chương 14):

```
# perf list tracepoint
List of pre-defined events (to be used in -e):
[...]
block:block_rq_complete                              [Tracepoint event]
block:block_rq_insert                                [Tracepoint event]
block:block_rq_issue                                 [Tracepoint event]
[...]
sched:sched_wakeup                                   [Tracepoint event]
sched:sched_wakeup_new                               [Tracepoint event]
sched:sched_waking                                   [Tracepoint event]
scsi:scsi_dispatch_cmd_done                          [Tracepoint event]
scsi:scsi_dispatch_cmd_error                         [Tracepoint event]
scsi:scsi_dispatch_cmd_start                         [Tracepoint event]
scsi:scsi_dispatch_cmd_timeout                       [Tracepoint event]
[...]
skb:consume_skb                                      [Tracepoint event]
skb:kfree_skb                                        [Tracepoint event]
[...]
```

Tôi đã cắt ngắn đầu ra để hiển thị một tá tracepoint ví dụ từ tầng thiết bị khối (block device layer), bộ lập lịch, và SCSI. Trên hệ thống của tôi có 1808 tracepoint khác nhau, 634 trong số đó để đo đạc lời gọi hệ thống (syscall).

Ngoài việc cho biết khi nào một sự kiện xảy ra, tracepoint cũng có thể cung cấp dữ liệu ngữ cảnh (contextual data) về sự kiện. Ví dụ, lệnh perf(1) sau đây truy vết tracepoint block:block_rq_issue và in các sự kiện trực tiếp:

```
# perf trace -e block:block_rq_issue
[...]
0.000 kworker/u4:1-e/20962 block:block_rq_issue:259,0 W 8192 () 875216 + 16
[kworker/u4:1]
255.945 :22696/22696 block:block_rq_issue:259,0 RA 4096 () 4459152 + 8 [bash]
256.957 :22705/22705 block:block_rq_issue:259,0 RA 16384 () 367936 + 32 [bash]
[...]
```

Ba trường đầu tiên là dấu thời gian (giây), chi tiết tiến trình (tên/ID luồng), và mô tả sự kiện (theo sau là dấu hai chấm thay vì dấu cách). Các trường còn lại là đối số cho tracepoint và được tạo bởi một chuỗi định dạng (format string) được giải thích tiếp theo; đối với chuỗi định dạng block:block_rq_issue cụ thể, xem Chương 9, Đĩa, Mục 9.6.5, perf.

Một lưu ý về thuật ngữ: tracepoint (hay trace point) về mặt kỹ thuật là các hàm truy vết (còn gọi là tracing hook) được đặt trong mã nguồn nhân. Ví dụ, trace_sched_wakeup() là một tracepoint, và bạn sẽ tìm thấy nó được gọi từ kernel/sched/core.c. Tracepoint này có thể được đo đạc qua các trình truy vết sử dụng tên "sched:sched_wakeup"; tuy nhiên, đó về mặt kỹ thuật là một sự kiện truy vết (trace event), được định nghĩa bởi macro TRACE_EVENT. TRACE_EVENT cũng định nghĩa và định dạng các đối số của nó, tự động tạo mã trace_sched_wakeup(), và đặt sự kiện truy vết vào các giao diện tracefs và perf_event_open(2) [Ts'o 20]. Các công cụ truy vết chủ yếu đo đạc các sự kiện truy vết, mặc dù chúng có thể gọi chúng là "tracepoint." perf(1) gọi các sự kiện truy vết là "Tracepoint event," điều này gây nhầm lẫn vì các sự kiện truy vết dựa trên kprobe và uprobe cũng được gắn nhãn "Tracepoint event."

**Đối số và Chuỗi Định dạng Tracepoint**

Mỗi tracepoint có một chuỗi định dạng (format string) chứa các đối số sự kiện: ngữ cảnh bổ sung về sự kiện. Cấu trúc của chuỗi định dạng này có thể được xem trong tệp "format" dưới /sys/kernel/debug/tracing/events. Ví dụ:

```
# cat /sys/kernel/debug/tracing/events/block/block_rq_issue/format
name: block_rq_issue
ID: 1080
format:
    field:unsigned short common_type;      offset:0;    size:2;  signed:0;
    field:unsigned char common_flags;      offset:2;    size:1;  signed:0;
    field:unsigned char common_preempt_count; offset:3;  size:1;  signed:0;
    field:int common_pid;                  offset:4;    size:4;  signed:1;

    field:dev_t dev;                       offset:8;    size:4;  signed:0;
    field:sector_t sector;                 offset:16;   size:8;  signed:0;
    field:unsigned int nr_sector;          offset:24;   size:4;  signed:0;
    field:unsigned int bytes;              offset:28;   size:4;  signed:0;
    field:char rwbs[8];                    offset:32;   size:8;  signed:0;
    field:char comm[16];                   offset:40;   size:16; signed:0;
    field:__data_loc char[] cmd;           offset:56;   size:4;  signed:1;

print fmt: "%d,%d %s %u (%s) %llu + %u [%s]", ((unsigned int) ((REC->dev) >> 20)),
((unsigned int) ((REC->dev) & ((1U << 20) - 1))), REC->rwbs, REC->bytes,
__get_str(cmd), (unsigned long long)REC->sector, REC->nr_sector, REC->comm
```

Dòng cuối cùng cho thấy định dạng chuỗi và các đối số. Phần sau hiển thị định dạng chuỗi từ đầu ra này, theo sau là một ví dụ chuỗi định dạng từ đầu ra perf script trước đó:

```
%d,%d %s %u (%s) %llu + %u [%s]
259,0 W 8192 () 875216 + 16 [kworker/u4:1]
```

Chúng khớp nhau.

Các trình truy vết thường có thể truy cập các đối số từ chuỗi định dạng thông qua tên của chúng. Ví dụ, đoạn sau sử dụng perf(1) để truy vết các sự kiện phát I/O khối chỉ khi kích thước (đối số bytes) lớn hơn 65536<sup>6</sup>:

```
# perf trace -e block:block_rq_issue --filter 'bytes > 65536'
0.000 jbd2/nvme0n1p1/174 block:block_rq_issue:259,0 WS 77824 () 2192856 + 152
[jbd2/nvme0n1p1-]
5.784 jbd2/nvme0n1p1/174 block:block_rq_issue:259,0 WS 94208 () 2193152 + 184
[jbd2/nvme0n1p1-]
[...]
```

Ví dụ về một trình truy vết khác, đoạn sau sử dụng bpftrace để in đối số bytes chỉ cho tracepoint này (cú pháp bpftrace được đề cập trong Chương 15, BPF; tôi sẽ sử dụng bpftrace cho các ví dụ tiếp theo vì nó ngắn gọn, yêu cầu ít lệnh hơn):

```
# bpftrace -e 't:block:block_rq_issue { printf("size: %d bytes\n", args->bytes); }'
Attaching 1 probe...
size: 4096 bytes
size: 49152 bytes
size: 40960 bytes
[...]
```

Đầu ra là một dòng cho mỗi lần phát I/O, hiển thị kích thước của nó.

Tracepoint là một API ổn định bao gồm tên tracepoint, chuỗi định dạng, và các đối số.

> <sup>6</sup> Đối số --filter cho perf trace được thêm vào Linux 5.5. Trên các nhân cũ hơn, bạn có thể thực hiện điều này bằng: perf trace -e block:block_rq_issue --filter 'bytes > 65536' -a; perf script

**Giao diện Tracepoint (Tracepoints Interface)**

Các công cụ truy vết có thể sử dụng tracepoint qua các tệp sự kiện truy vết của chúng trong tracefs (thường được gắn tại /sys/kernel/debug/tracing) hoặc lời gọi hệ thống perf_event_open(2). Ví dụ, công cụ iosnoop(8) dựa trên Ftrace của tôi sử dụng các tệp tracefs:

```
# strace -e openat ~/Git/perf-tools/bin/iosnoop
chdir("/sys/kernel/debug/tracing")                          = 0
[...]
openat(AT_FDCWD, "events/block/block_rq_issue/enable", O_WRONLY|O_CREAT|O_TRUNC,
0666) = 3
openat(AT_FDCWD, "events/block/block_rq_complete/enable", O_WRONLY|O_CREAT|O_TRUNC,
0666) = 3
[...]
```

Đầu ra bao gồm một chdir(2) đến thư mục tracefs và việc mở các tệp "enable" cho các tracepoint khối. Nó cũng bao gồm /var/tmp/.ftrace-lock: đây là một biện pháp phòng ngừa mà tôi đã mã hóa để chặn người dùng công cụ đồng thời, điều mà giao diện tracefs không dễ dàng hỗ trợ. Giao diện perf_event_open(2) hỗ trợ người dùng đồng thời và được ưu tiên khi có thể. Nó được sử dụng bởi phiên bản BCC mới hơn của cùng công cụ:

```
# strace -e perf_event_open /usr/share/bcc/tools/biosnoop
perf_event_open({type=PERF_TYPE_TRACEPOINT, size=0 /* PERF_ATTR_SIZE_??? */,
config=2323, ...}, -1, 0, -1, PERF_FLAG_FD_CLOEXEC) = 8
perf_event_open({type=PERF_TYPE_TRACEPOINT, size=0 /* PERF_ATTR_SIZE_??? */,
config=2324, ...}, -1, 0, -1, PERF_FLAG_FD_CLOEXEC) = 10
[...]
```

perf_event_open(2) là giao diện tới hệ thống con perf_events của nhân, cung cấp nhiều khả năng lập hồ sơ và truy vết. Xem trang man của nó để biết thêm chi tiết, cũng như giao diện perf(1) trong Chương 13.

**Chi phí Tracepoint (Tracepoints Overhead)**

Khi tracepoint được kích hoạt, chúng thêm một lượng nhỏ chi phí CPU cho mỗi sự kiện. Công cụ truy vết cũng có thể thêm chi phí CPU để xử lý hậu kỳ các sự kiện, cộng với chi phí hệ thống tệp để ghi lại chúng. Liệu chi phí có đủ cao để làm xáo trộn các ứng dụng sản xuất hay không phụ thuộc vào tốc độ sự kiện và số lượng CPU, và đó là điều bạn cần xem xét khi sử dụng tracepoint.

Trên các hệ thống điển hình ngày nay (4 đến 128 CPU), tôi thấy rằng tốc độ sự kiện dưới 10.000 mỗi giây có chi phí không đáng kể, và chỉ trên 100.000 chi phí mới bắt đầu có thể đo được. Ví dụ về sự kiện, bạn có thể thấy rằng sự kiện đĩa thường dưới 10.000 mỗi giây, nhưng sự kiện bộ lập lịch có thể vượt quá 100.000 mỗi giây và do đó có thể tốn kém để truy vết.

Trước đây tôi đã phân tích chi phí cho một hệ thống cụ thể và thấy chi phí tracepoint tối thiểu là 96 nano giây thời gian CPU [Gregg 19]. Có một loại tracepoint mới gọi là raw tracepoint, được thêm vào Linux 4.7 năm 2018, tránh chi phí tạo các đối số tracepoint ổn định, giảm chi phí này.

Ngoài chi phí khi được kích hoạt trong khi tracepoint đang sử dụng, còn có chi phí khi bị vô hiệu hóa để chúng sẵn sàng. Một tracepoint bị vô hiệu hóa trở thành một số lượng nhỏ lệnh: đối với x86_64 là một lệnh không-thao-tác (nop) 5 byte. Cũng có một trình xử lý tracepoint được thêm vào cuối hàm, làm tăng kích thước text của nó một chút. Mặc dù các chi phí này rất nhỏ, chúng là thứ bạn nên phân tích và hiểu khi thêm tracepoint vào nhân.

**Tài liệu Tracepoint**

Công nghệ tracepoint được tài liệu hóa trong mã nguồn nhân tại Documentation/trace/tracepoints.rst. Bản thân các tracepoint (đôi khi) được tài liệu hóa trong các tệp header định nghĩa chúng, nằm trong mã nguồn Linux tại include/trace/events. Tôi đã tóm tắt các chủ đề tracepoint nâng cao trong BPF Performance Tools, Chương 2 [Gregg 19]: cách chúng được thêm vào mã nhân, và cách chúng hoạt động ở cấp lệnh.

Đôi khi bạn có thể muốn truy vết việc thực thi phần mềm mà không có tracepoint nào: trong trường hợp đó bạn có thể thử giao diện không ổn định kprobe.

### 4.3.6 kprobe

kprobe (viết tắt của kernel probe — thăm dò nhân) là một nguồn sự kiện nhân Linux cho các trình truy vết dựa trên thiết bị đo đạc động (dynamic instrumentation), một thuật ngữ đã được giới thiệu trong Chương 1, Giới thiệu, Mục 1.7.3, Truy vết. kprobe có thể truy vết bất kỳ hàm hoặc lệnh nhân nào, và đã có sẵn trong Linux 2.6.9, phát hành năm 2004. Chúng được coi là API không ổn định (unstable API) vì chúng phơi bày các hàm và đối số nhân thô có thể thay đổi giữa các phiên bản nhân.

kprobe có thể hoạt động theo nhiều cách khác nhau bên trong. Phương pháp tiêu chuẩn là sửa đổi text lệnh (instruction text) của mã nhân đang chạy để chèn thiết bị đo đạc khi cần. Khi đo đạc điểm vào của hàm, một tối ưu hóa có thể được sử dụng khi kprobe tận dụng truy vết hàm Ftrace có sẵn, vì nó có chi phí thấp hơn.<sup>7</sup>

kprobe quan trọng vì chúng là nguồn phương sách cuối cùng<sup>8</sup> (last-resort) cung cấp thông tin gần như không giới hạn về hành vi nhân trong sản xuất, điều có thể rất quan trọng để quan sát các vấn đề hiệu năng mà các công cụ khác không nhìn thấy. Chúng có thể được sử dụng bởi các trình truy vết được giới thiệu trong Mục 4.5, Công cụ Truy vết, và được đề cập chi tiết trong các Chương 13 đến 15.

kprobe và tracepoint được so sánh trong Bảng 4.3.

**Bảng 4.3: So sánh kprobe với tracepoint**

| Chi tiết | kprobe | Tracepoint |
|---|---|---|
| Loại | Động (Dynamic) | Tĩnh (Static) |
| Số lượng sự kiện ước tính | 50.000+ | 1.000+ |
| Bảo trì nhân | Không | Cần thiết |
| Chi phí khi vô hiệu hóa | Không | Rất nhỏ (NOP + metadata) |
| API ổn định | Không | Có |

kprobe có thể truy vết điểm vào hàm cũng như offset lệnh (instruction offset) bên trong hàm. Việc sử dụng kprobe tạo ra các sự kiện kprobe (sự kiện truy vết dựa trên kprobe). Các sự kiện kprobe này chỉ tồn tại khi một trình truy vết tạo chúng: theo mặc định, mã nhân chạy không bị sửa đổi.

> <sup>7</sup> Nó cũng có thể được bật/tắt thông qua sysctl(8) debug.kprobes-optimization.

> <sup>8</sup> Nếu không có kprobe, lựa chọn phương sách cuối cùng sẽ là sửa đổi mã nhân để thêm thiết bị đo đạc khi cần, biên dịch lại, và triển khai lại.

**Ví dụ kprobe**

Ví dụ về việc sử dụng kprobe, lệnh bpftrace sau đây đo đạc hàm nhân do_nanosleep() và in tiến trình đang chạy trên CPU:

```
# bpftrace -e 'kprobe:do_nanosleep { printf("sleep by: %s\n", comm); }'
Attaching 1 probe...
sleep by: mysqld
sleep by: mysqld
sleep by: sleep
^C
#
```

Đầu ra cho thấy một vài lần sleep bởi tiến trình có tên "mysqld", và một lần bởi "sleep" (có thể là /bin/sleep). Sự kiện kprobe cho do_nanosleep() được tạo khi chương trình bpftrace bắt đầu chạy và bị xóa khi bpftrace kết thúc (Ctrl-C).

**Đối số kprobe**

Vì kprobe có thể truy vết các lời gọi hàm nhân, thường mong muốn kiểm tra các đối số cho hàm để có thêm ngữ cảnh. Mỗi công cụ truy vết phơi bày chúng theo cách riêng và được đề cập trong các phần sau. Ví dụ, sử dụng bpftrace để in đối số thứ hai của do_nanosleep(), là hrtimer_mode:

```
# bpftrace -e 'kprobe:do_nanosleep { printf("mode: %d\n", arg1); }'
Attaching 1 probe...
mode: 1
mode: 1
mode: 1
[...]
```

Đối số hàm có sẵn trong bpftrace sử dụng biến tích hợp arg0..argN.

**kretprobe**

Giá trị trả về và sự trở về từ các hàm nhân có thể được truy vết bằng kretprobe (viết tắt của kernel return probe — thăm dò trả về nhân), tương tự như kprobe. kretprobe được triển khai bằng cách sử dụng kprobe cho điểm vào hàm, chèn một hàm trampoline để đo đạc điểm trả về.

Khi kết hợp với kprobe và một trình truy vết ghi lại dấu thời gian, thời gian thực thi của một hàm nhân có thể được đo. Ví dụ, đo thời gian thực thi do_nanosleep() bằng bpftrace:

```
# bpftrace -e 'kprobe:do_nanosleep { @ts[tid] = nsecs; }
    kretprobe:do_nanosleep /@ts[tid]/ {
        @sleep_ms = hist((nsecs - @ts[tid]) / 1000000); delete(@ts[tid]); }
    END { clear(@ts); }'
Attaching 3 probes...
^C
@sleep_ms:
[0]                 1280 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[1]                    1 |                                                    |
[2, 4)                 1 |                                                    |
[4, 8)                 0 |                                                    |
[8, 16)                0 |                                                    |
[16, 32)               0 |                                                    |
[32, 64)               0 |                                                    |
[64, 128)              0 |                                                    |
[128, 256)             0 |                                                    |
[256, 512)             0 |                                                    |
[512, 1K)              2 |                                                    |
```

Đầu ra cho thấy do_nanosleep() thường là một hàm nhanh, trả về trong không mili giây (làm tròn xuống) 1.280 lần. Hai lần xuất hiện đạt đến phạm vi 512 đến 1024 mili giây. Cú pháp bpftrace được giải thích trong Chương 15, BPF, bao gồm một ví dụ tương tự cho việc đo thời gian vfs_read().

**Giao diện và Chi phí kprobe**

Giao diện kprobe tương tự như tracepoint. Có cách để đo đạc chúng qua các tệp /sys, qua lời gọi hệ thống perf_event_open(2) (được ưu tiên), và cũng qua API nhân register_kprobe(). Chi phí tương tự như tracepoint khi điểm vào hàm được truy vết (phương pháp Ftrace, nếu có), và cao hơn khi offset hàm được truy vết (phương pháp breakpoint) hoặc khi kretprobe được sử dụng (phương pháp trampoline). Cho một hệ thống cụ thể, tôi đo chi phí CPU tối thiểu của kprobe là 76 nano giây, và chi phí CPU tối thiểu của kretprobe là 212 nano giây [Gregg 19].

**Tài liệu kprobe**

kprobe được tài liệu hóa trong mã nguồn Linux tại Documentation/kprobes.txt. Các hàm nhân mà chúng đo đạc thường không được tài liệu hóa bên ngoài mã nguồn nhân (vì hầu hết không phải là API, chúng không cần phải được tài liệu hóa). Tôi đã tóm tắt các chủ đề kprobe nâng cao trong BPF Performance Tools, Chương 2 [Gregg 19]: cách chúng hoạt động ở cấp lệnh.

### 4.3.7 uprobe

uprobe (user-space probe — thăm dò không gian người dùng) tương tự như kprobe, nhưng dành cho không gian người dùng (user-space). Chúng có thể đo đạc động các hàm trong ứng dụng và thư viện, và cung cấp một API không ổn định để đào sâu vào nội bộ phần mềm vượt ra ngoài phạm vi của các công cụ khác. uprobe đã có sẵn trong Linux 3.5, phát hành năm 2012.

uprobe có thể được sử dụng bởi các trình truy vết được giới thiệu trong Mục 4.5, Công cụ Truy vết, và được đề cập chi tiết trong các Chương 13 đến 15.

**Ví dụ uprobe**

Ví dụ về uprobe, lệnh bpftrace sau đây liệt kê các vị trí điểm vào hàm uprobe có thể trong shell bash(1):

```
# bpftrace -l 'uprobe:/bin/bash:*'
uprobe:/bin/bash:rl_old_menu_complete
uprobe:/bin/bash:maybe_make_export_env
uprobe:/bin/bash:initialize_shell_builtins
uprobe:/bin/bash:extglob_pattern_p
uprobe:/bin/bash:dispose_cond_node
uprobe:/bin/bash:decode_prompt_string
[...]
```

Đầu ra đầy đủ cho thấy 1.507 uprobe có thể. uprobe đo đạc mã và tạo sự kiện uprobe (sự kiện truy vết dựa trên uprobe) khi cần: mã không gian người dùng chạy không bị sửa đổi theo mặc định. Điều này tương tự như sử dụng trình gỡ lỗi (debugger) để thêm breakpoint vào hàm: trước khi breakpoint được thêm, hàm đang chạy không bị sửa đổi.

**Đối số uprobe**

Đối số cho các hàm người dùng được uprobe cung cấp. Ví dụ, đoạn sau sử dụng bpftrace để đo đạc hàm decode_prompt_string() của bash và in đối số đầu tiên dưới dạng chuỗi:

```
# bpftrace -e 'uprobe:/bin/bash:decode_prompt_string { printf("%s\n", str(arg0)); }'
Attaching 1 probe...
\[\e[31;1m\]\u@\h:\w>\[\e[0m\]
\[\e[31;1m\]\u@\h:\w>\[\e[0m\]
^C
```

Đầu ra hiển thị chuỗi dấu nhắc (prompt string) của bash(1) trên hệ thống này. uprobe cho decode_prompt_string() được tạo khi chương trình bpftrace bắt đầu chạy, và bị xóa khi bpftrace kết thúc (Ctrl-C).

**uretprobe**

Giá trị trả về và sự trở về từ các hàm người dùng có thể được truy vết bằng uretprobe (viết tắt của user-level return probe — thăm dò trả về cấp người dùng), tương tự như uprobe. Khi kết hợp với uprobe và một trình truy vết ghi lại dấu thời gian, thời gian thực thi của một hàm cấp người dùng có thể được đo. Lưu ý rằng chi phí của uretprobe có thể làm lệch đáng kể phép đo thời gian của các hàm nhanh.

**Giao diện và Chi phí uprobe**

Giao diện uprobe tương tự như kprobe. Có cách để đo đạc chúng qua các tệp /sys và cũng (tốt hơn là) qua lời gọi hệ thống perf_event_open(2).

uprobe hiện tại hoạt động bằng cách bẫy (trapping) vào nhân. Chi phí CPU cao hơn đáng kể so với kprobe hoặc tracepoint. Cho một hệ thống cụ thể mà tôi đo, chi phí tối thiểu của uprobe là 1.287 nano giây, và chi phí tối thiểu của uretprobe là 1.931 nano giây [Gregg 19]. Chi phí uretprobe cao hơn vì nó là uprobe cộng thêm hàm trampoline.

**Tài liệu uprobe**

uprobe được tài liệu hóa trong mã nguồn Linux tại Documentation/trace/uprobetracer.rst. Tôi đã tóm tắt các chủ đề uprobe nâng cao trong BPF Performance Tools, Chương 2 [Gregg 19]: cách chúng hoạt động ở cấp lệnh. Các hàm người dùng mà chúng đo đạc thường không được tài liệu hóa bên ngoài mã nguồn ứng dụng (vì hầu hết khó có thể là API, chúng không cần phải được tài liệu hóa). Để truy vết không gian người dùng có tài liệu, hãy sử dụng USDT.

### 4.3.8 USDT

Truy vết được định nghĩa tĩnh cấp người dùng (User-level Statically-Defined Tracing — USDT) là phiên bản không gian người dùng của tracepoint. USDT đối với uprobe cũng như tracepoint đối với kprobe. Một số ứng dụng và thư viện đã thêm đầu dò USDT (USDT probe) vào mã của chúng, cung cấp API ổn định (và có tài liệu) để truy vết các sự kiện cấp ứng dụng. Ví dụ, có các đầu dò USDT trong Java JDK, trong cơ sở dữ liệu PostgreSQL, và trong libc. Đoạn sau liệt kê các đầu dò USDT của OpenJDK bằng bpftrace:

```
# bpftrace -lv 'usdt:/usr/lib/jvm/openjdk/libjvm.so:*'
usdt:/usr/lib/jvm/openjdk/libjvm.so:hotspot:class__loaded
usdt:/usr/lib/jvm/openjdk/libjvm.so:hotspot:class__unloaded
usdt:/usr/lib/jvm/openjdk/libjvm.so:hotspot:method__compile__begin
usdt:/usr/lib/jvm/openjdk/libjvm.so:hotspot:method__compile__end
usdt:/usr/lib/jvm/openjdk/libjvm.so:hotspot:gc__begin
usdt:/usr/lib/jvm/openjdk/libjvm.so:hotspot:gc__end
[...]
```

Danh sách này liệt kê các đầu dò USDT cho nạp và giải phóng lớp Java (class loading/unloading), biên dịch phương thức (method compilation), và thu gom rác (garbage collection). Nhiều mục khác đã bị cắt ngắn: danh sách đầy đủ cho thấy 524 đầu dò USDT cho phiên bản JDK này.

Nhiều ứng dụng đã có nhật ký sự kiện tùy chỉnh có thể được kích hoạt và cấu hình, và hữu ích cho phân tích hiệu năng. Điều làm cho đầu dò USDT khác biệt là chúng có thể được sử dụng từ nhiều trình truy vết khác nhau có thể kết hợp ngữ cảnh ứng dụng với các sự kiện nhân như I/O đĩa và mạng. Một trình ghi nhật ký cấp ứng dụng có thể cho bạn biết rằng truy vấn cơ sở dữ liệu chậm do I/O hệ thống tệp, nhưng trình truy vết có thể tiết lộ thêm thông tin: ví dụ, truy vấn chậm do tranh chấp khóa (lock contention) trong hệ thống tệp, chứ không phải I/O đĩa như bạn có thể đã giả định.

Một số ứng dụng chứa đầu dò USDT, nhưng chúng hiện không được kích hoạt trong phiên bản đóng gói của ứng dụng (đây là trường hợp với OpenJDK). Sử dụng chúng yêu cầu xây dựng lại ứng dụng từ mã nguồn với tùy chọn cấu hình phù hợp. Tùy chọn đó có thể được gọi là --enable-dtrace-probes theo tên trình truy vết DTrace, đã thúc đẩy việc áp dụng USDT trong các ứng dụng.

Đầu dò USDT phải được biên dịch vào tệp thực thi mà chúng đo đạc. Điều này không thể thực hiện được cho các ngôn ngữ biên dịch JIT (just-in-time) như Java, thường biên dịch ngay trong khi chạy. Giải pháp cho vấn đề này là USDT động (dynamic USDT), tiền biên dịch các đầu dò dưới dạng thư viện chia sẻ (shared library), và cung cấp giao diện để gọi chúng từ ngôn ngữ biên dịch JIT. Thư viện USDT động tồn tại cho Java, Node.js, và các ngôn ngữ khác. Các ngôn ngữ thông dịch (interpreted language) có vấn đề tương tự và cần USDT động.

Đầu dò USDT được triển khai trong Linux sử dụng uprobe: xem phần trước để mô tả uprobe và chi phí của chúng. Ngoài chi phí khi được kích hoạt, đầu dò USDT đặt các lệnh nop vào mã, giống như tracepoint.

Đầu dò USDT có thể được sử dụng bởi các trình truy vết được giới thiệu trong Mục 4.5, Công cụ Truy vết, được đề cập chi tiết trong các Chương 13 đến 15 (mặc dù sử dụng USDT với Ftrace yêu cầu thêm một số công việc).

**Tài liệu USDT**

Nếu một ứng dụng cung cấp đầu dò USDT, chúng nên được tài liệu hóa trong tài liệu của ứng dụng. Tôi đã tóm tắt các chủ đề USDT nâng cao trong BPF Performance Tools, Chương 2 [Gregg 19]: cách đầu dò USDT có thể được thêm vào mã ứng dụng, cách chúng hoạt động bên trong, và USDT động.

### 4.3.9 Bộ đếm Phần cứng (Hardware Counters — PMC)

Bộ xử lý và các thiết bị khác thường hỗ trợ bộ đếm phần cứng (hardware counter) để quan sát hoạt động. Nguồn chính là các bộ xử lý, nơi chúng thường được gọi là bộ đếm giám sát hiệu năng (Performance Monitoring Counters — PMC). Chúng còn được biết đến với các tên khác: bộ đếm hiệu năng CPU (CPU Performance Counters — CPC), bộ đếm đo đạc hiệu năng (Performance Instrumentation Counters — PIC), và sự kiện đơn vị giám sát hiệu năng (Performance Monitoring Unit events — PMU events). Tất cả đều chỉ cùng một thứ: các thanh ghi phần cứng có thể lập trình trên bộ xử lý cung cấp thông tin hiệu năng cấp thấp ở mức chu kỳ CPU.

PMC là tài nguyên quan trọng cho phân tích hiệu năng. Chỉ thông qua PMC bạn mới có thể đo hiệu quả lệnh CPU, tỷ lệ trúng (hit ratio) bộ nhớ đệm CPU, mức sử dụng bus bộ nhớ và thiết bị, mức sử dụng liên kết nối (interconnect), chu kỳ trì hoãn (stall cycle), v.v. Sử dụng chúng để phân tích hiệu năng có thể dẫn đến nhiều tối ưu hóa hiệu năng khác nhau.

**Ví dụ PMC**

Mặc dù có nhiều PMC, Intel đã chọn bảy PMC làm "tập kiến trúc" (architectural set), cung cấp cái nhìn tổng quan cấp cao về một số chức năng lõi [Intel 16]. Sự hiện diện của các PMC tập kiến trúc này có thể được kiểm tra bằng lệnh cpuid. Bảng 4.4 cho thấy tập này, phục vụ như một tập ví dụ về PMC hữu ích.

**Bảng 4.4: PMC kiến trúc Intel**

| Tên Sự kiện | UMask | Event Select | Ví dụ Mnemonic Mặt nạ Sự kiện |
|---|---|---|---|
| UnHalted Core Cycles | 00H | 3CH | CPU_CLK_UNHALTED.THREAD_P |
| Instruction Retired | 00H | C0H | INST_RETIRED.ANY_P |
| UnHalted Reference Cycles | 01H | 3CH | CPU_CLK_THREAD_UNHALTED.REF_XCLK |
| LLC References | 4FH | 2EH | LONGEST_LAT_CACHE.REFERENCE |
| LLC Misses | 41H | 2EH | LONGEST_LAT_CACHE.MISS |
| Branch Instruction Retired | 00H | C4H | BR_INST_RETIRED.ALL_BRANCHES |
| Branch Misses Retired | 00H | C5H | BR_MISP_RETIRED.ALL_BRANCHES |

Ví dụ về PMC, nếu bạn chạy lệnh perf stat mà không chỉ định sự kiện (không có -e), nó mặc định đo đạc các PMC kiến trúc. Ví dụ, đoạn sau chạy perf stat trên lệnh gzip(1):

```
# perf stat gzip words

 Performance counter stats for 'gzip words':

        156.927428      task-clock (msec)         #    0.987 CPUs utilized
                 1      context-switches          #    0.006 K/sec
                 0      cpu-migrations            #    0.000 K/sec
               131      page-faults               #    0.835 K/sec
       209,911,358      cycles                    #    1.338 GHz
       288,321,441      instructions              #    1.37  insn per cycle
        66,240,624      branches                  #  422.110 M/sec
         1,382,627      branch-misses             #    2.09% of all branches

       0.159065542 seconds time elapsed
```

Các số đếm thô là cột đầu tiên; sau dấu thăng là một số thống kê, bao gồm một chỉ số hiệu năng quan trọng: lệnh trên mỗi chu kỳ (instructions per cycle — insn per cycle). Điều này cho thấy CPU đang thực thi lệnh hiệu quả như thế nào — càng cao càng tốt. Chỉ số này được giải thích trong Chương 6, CPU, Mục 6.3.7, IPC, CPI.

**Giao diện PMC**

Trên Linux, PMC được truy cập qua lời gọi hệ thống perf_event_open(2) và được tiêu thụ bởi các công cụ bao gồm perf(1).

Mặc dù có hàng trăm PMC có sẵn, chỉ có một số lượng cố định các thanh ghi trong CPU để đo chúng cùng lúc, có lẽ chỉ sáu. Bạn cần chọn PMC nào muốn đo trên sáu thanh ghi đó, hoặc luân chuyển qua các tập PMC khác nhau như cách lấy mẫu chúng (Linux perf(1) hỗ trợ điều này tự động). Các bộ đếm phần mềm khác không chịu những ràng buộc này.

PMC có thể được sử dụng ở các chế độ khác nhau: đếm (counting), nơi chúng đếm sự kiện với chi phí gần như bằng không; và lấy mẫu tràn (overflow sampling), nơi một ngắt được phát sinh cho mỗi số lượng sự kiện có thể cấu hình, để trạng thái có thể được ghi lại. Đếm có thể được sử dụng để định lượng vấn đề; lấy mẫu tràn có thể được sử dụng để cho thấy đường dẫn mã chịu trách nhiệm.

perf(1) có thể thực hiện đếm bằng lệnh con stat, và lấy mẫu bằng lệnh con record; xem Chương 13, perf.

**Thách thức PMC**

Hai thách thức phổ biến khi sử dụng PMC là độ chính xác cho lấy mẫu tràn và tính khả dụng trong môi trường đám mây.

Lấy mẫu tràn có thể không ghi lại con trỏ lệnh (instruction pointer) chính xác đã kích hoạt sự kiện, do độ trễ ngắt (thường gọi là "trượt" — skid) hoặc thực thi lệnh không theo thứ tự (out-of-order instruction execution). Đối với lập hồ sơ chu kỳ CPU, trượt như vậy có thể không phải là vấn đề, và một số trình lập hồ sơ cố tình giới thiệu dao động (jitter) để tránh lấy mẫu đồng bộ (hoặc sử dụng tốc độ lấy mẫu lệch như 99 Hertz). Nhưng khi đo các sự kiện khác, như lỗi LLC (LLC miss), con trỏ lệnh được lấy mẫu cần phải chính xác.

Giải pháp là hỗ trợ bộ xử lý cho những gì được gọi là sự kiện chính xác (precise event). Trên Intel, sự kiện chính xác sử dụng công nghệ gọi là lấy mẫu dựa trên sự kiện chính xác (Precise Event-Based Sampling — PEBS)<sup>9</sup>, sử dụng bộ đệm phần cứng để ghi lại con trỏ lệnh chính xác hơn ("precise") tại thời điểm sự kiện PMC. Trên AMD, sự kiện chính xác sử dụng lấy mẫu dựa trên lệnh (Instruction-Based Sampling — IBS) [Drongowski 07]. Lệnh Linux perf(1) hỗ trợ sự kiện chính xác (xem Chương 13, perf, Mục 13.9.2, Lập hồ sơ CPU).

Thách thức khác là điện toán đám mây (cloud computing), vì nhiều môi trường đám mây vô hiệu hóa truy cập PMC cho guest. Về mặt kỹ thuật có thể kích hoạt nó: ví dụ, hypervisor Xen có tùy chọn dòng lệnh vpmu, cho phép các tập PMC khác nhau được phơi bày cho guest<sup>10</sup> [Xenbits 20]. Amazon đã kích hoạt nhiều PMC cho guest hypervisor Nitro của họ.<sup>11</sup> Ngoài ra, một số nhà cung cấp đám mây cung cấp "phiên bản bare-metal" (bare-metal instance) nơi guest có toàn quyền truy cập bộ xử lý, và do đó toàn quyền truy cập PMC.

> <sup>9</sup> Một số tài liệu của Intel mở rộng PEBS khác nhau, thành: processor event-based sampling.

> <sup>10</sup> Tôi đã viết mã Xen cho phép các chế độ PMC khác nhau: "ipc" chỉ cho PMC lệnh-trên-mỗi-chu-kỳ, và "arch" cho tập kiến trúc Intel. Mã của tôi chỉ là một tường lửa trên hỗ trợ vpmu hiện có trong Xen.

> <sup>11</sup> Hiện chỉ cho các phiên bản Nitro lớn hơn nơi VM sở hữu toàn bộ socket bộ xử lý (hoặc nhiều hơn).

**Tài liệu PMC**

PMC là đặc trưng cho bộ xử lý và được tài liệu hóa trong hướng dẫn nhà phát triển phần mềm bộ xử lý tương ứng. Ví dụ theo nhà sản xuất bộ xử lý:

- **Intel**: Chương 19, "Performance Monitoring Events," của Intel® 64 and IA-32 Architectures Software Developer's Manual Volume 3 [Intel 16].
- **AMD**: Mục 2.1.1, "Performance Monitor Counters," của Open-Source Register Reference For AMD Family 17h Processors Models 00h-2Fh [AMD 18].
- **ARM**: Mục D7.10, "PMU Events and Event Numbers," của Arm® Architecture Reference Manual Armv8, for Armv8-A architecture profile [ARM 19].

Đã có công việc phát triển một lược đồ đặt tên tiêu chuẩn cho PMC có thể được hỗ trợ trên tất cả bộ xử lý, gọi là giao diện lập trình ứng dụng hiệu năng (Performance Application Programming Interface — PAPI) [UTK 20]. Hỗ trợ hệ điều hành cho PAPI không đồng đều: nó yêu cầu cập nhật thường xuyên để ánh xạ tên PAPI sang mã PMC của nhà cung cấp.

Chương 6, CPU, Mục 6.4.1, Phần cứng, phần con Bộ đếm phần cứng (PMC), mô tả triển khai chi tiết hơn và cung cấp thêm ví dụ PMC.

### 4.3.10 Các Nguồn Khả năng Quan sát Khác (Other Observability Sources)

Các nguồn khả năng quan sát khác bao gồm:

- **MSR**: PMC được triển khai bằng các thanh ghi đặc trưng mô hình (Model-Specific Register — MSR). Có các MSR khác để hiển thị cấu hình và tình trạng của hệ thống, bao gồm tốc độ xung nhịp CPU, mức sử dụng, nhiệt độ, và tiêu thụ năng lượng. Các MSR có sẵn phụ thuộc vào loại bộ xử lý (đặc trưng mô hình), phiên bản và cài đặt BIOS, và cài đặt hypervisor. Một ứng dụng là phép đo chính xác dựa trên chu kỳ về mức sử dụng CPU.

- **ptrace(2)**: Lời gọi hệ thống này điều khiển truy vết tiến trình, được sử dụng bởi gdb(1) cho gỡ lỗi tiến trình và strace(1) cho truy vết lời gọi hệ thống. Nó dựa trên breakpoint và có thể làm chậm mục tiêu hơn một trăm lần. Linux cũng có tracepoint, được giới thiệu trong Mục 4.3.5, Tracepoint, cho truy vết lời gọi hệ thống hiệu quả hơn.

- **Lập hồ sơ hàm (Function profiling)**: Các lời gọi hàm lập hồ sơ (mcount() hoặc __fentry__()) được thêm vào đầu tất cả các hàm nhân không nội tuyến (non-inlined) trên x86 cho truy vết hàm Ftrace hiệu quả. Chúng được chuyển đổi thành lệnh nop cho đến khi cần. Xem Chương 14, Ftrace.

- **Bắt gói tin mạng (Network sniffing — libpcap)**: Các giao diện này cung cấp cách bắt gói tin từ thiết bị mạng để điều tra chi tiết hiệu năng gói tin và giao thức. Trên Linux, bắt gói tin được cung cấp qua thư viện libpcap và /proc/net/dev và được tiêu thụ bởi công cụ tcpdump(8). Có chi phí, cả CPU và lưu trữ, cho việc bắt và kiểm tra tất cả gói tin. Xem Chương 10 để biết thêm về bắt gói tin mạng.

- **netfilter conntrack**: Công nghệ Linux netfilter cho phép các trình xử lý tùy chỉnh được thực thi trên các sự kiện, không chỉ cho tường lửa, mà còn cho theo dõi kết nối (connection tracking — conntrack). Điều này cho phép tạo nhật ký luồng mạng (network flow) [Ayuso 12].

- **Kế toán tiến trình (Process accounting)**: Điều này có từ thời máy tính lớn (mainframe) và nhu cầu tính phí các bộ phận và người dùng cho việc sử dụng máy tính, dựa trên việc thực thi và thời gian chạy của các tiến trình. Nó tồn tại ở một số dạng cho Linux và các hệ thống khác và đôi khi có thể hữu ích cho phân tích hiệu năng ở cấp tiến trình. Ví dụ, công cụ Linux atop(1) sử dụng kế toán tiến trình để bắt và hiển thị thông tin từ các tiến trình có thời gian sống ngắn mà nếu không sẽ bị bỏ lỡ khi chụp ảnh /proc [Atoptool 20].

- **Sự kiện phần mềm (Software events)**: Chúng liên quan đến sự kiện phần cứng nhưng được đo đạc trong phần mềm. Lỗi trang (page fault) là một ví dụ. Sự kiện phần mềm được cung cấp qua giao diện perf_event_open(2) và được sử dụng bởi perf(1) và bpftrace. Chúng được minh họa trong Hình 4.5.

- **Lời gọi hệ thống (System calls)**: Một số lời gọi hệ thống hoặc thư viện có thể có sẵn để cung cấp một số chỉ số hiệu năng. Chúng bao gồm getrusage(2), một lời gọi hệ thống cho tiến trình để lấy thống kê sử dụng tài nguyên của chính chúng, bao gồm thời gian người dùng và hệ thống, lỗi trang, thông báo, và chuyển đổi ngữ cảnh.

Nếu bạn quan tâm đến cách mỗi nguồn này hoạt động, bạn sẽ thấy rằng tài liệu thường có sẵn, dành cho nhà phát triển đang xây dựng công cụ trên các giao diện này.

**Và Nhiều hơn nữa**

Tùy thuộc vào phiên bản nhân và các tùy chọn được kích hoạt, có thể có thêm nhiều nguồn khả năng quan sát. Một số được đề cập trong các chương sau của cuốn sách này. Đối với Linux, chúng bao gồm I/O accounting, blktrace, timer_stats, lockstat, và debugfs.

Một cách để tìm các nguồn như vậy là đọc mã nhân mà bạn quan tâm đến quan sát và xem thống kê hoặc tracepoint nào đã được đặt ở đó.

Trong một số trường hợp có thể không có thống kê nhân cho những gì bạn đang tìm kiếm. Ngoài thiết bị đo đạc động (Linux kprobe và uprobe), bạn có thể thấy rằng các trình gỡ lỗi như gdb(1) và lldb(1) có thể lấy các biến nhân và ứng dụng để làm sáng tỏ một cuộc điều tra.

**Solaris Kstat**

Ví dụ về cách khác để cung cấp thống kê hệ thống, các hệ thống dựa trên Solaris sử dụng framework thống kê nhân (kernel statistics — Kstat) cung cấp cấu trúc phân cấp nhất quán của các thống kê nhân, mỗi cái được đặt tên bằng bốn-tuple sau:

```
module:instance:name:statistic
```

Đó là:

- **module**: Thường chỉ module nhân đã tạo thống kê, chẳng hạn như sd cho trình điều khiển đĩa SCSI, hoặc zfs cho hệ thống tệp ZFS.
- **instance**: Một số module tồn tại dưới dạng nhiều phiên bản, chẳng hạn như module sd cho mỗi đĩa SCSI. Instance là một sự liệt kê.
- **name**: Đây là tên cho nhóm thống kê.
- **statistic**: Đây là tên thống kê riêng lẻ.

Kstat được truy cập bằng giao diện nhị phân nhân, và nhiều thư viện khác nhau tồn tại.

Ví dụ Kstat, đoạn sau đọc thống kê "nproc" bằng kstat(1M) và chỉ định bốn-tuple đầy đủ:

```
$ kstat -p unix:0:system_misc:nproc
unix:0:system_misc:nproc        94
```

Thống kê này hiển thị số lượng tiến trình đang chạy hiện tại.

So sánh, các nguồn kiểu /proc/stat trên Linux có định dạng không nhất quán và thường yêu cầu phân tích văn bản để xử lý, tốn một số chu kỳ CPU.

## 4.4 sar

sar(1) đã được giới thiệu trong Mục 4.2.4, Giám sát, như một cơ sở giám sát quan trọng. Mặc dù gần đây có nhiều hứng thú với siêu năng lực truy vết BPF (và tôi chịu một phần trách nhiệm), bạn không nên bỏ qua tính hữu dụng của sar(1) — đây là công cụ hiệu năng hệ thống thiết yếu có thể tự mình giải quyết nhiều vấn đề hiệu năng. Phiên bản Linux của sar(1) cũng được thiết kế tốt, có tiêu đề cột tự mô tả, nhóm chỉ số mạng, và tài liệu chi tiết (trang man).

sar(1) được cung cấp qua gói sysstat.

### 4.4.1 Phạm vi sar(1)

Hình 4.6 cho thấy phạm vi khả năng quan sát từ các tùy chọn dòng lệnh khác nhau của sar(1).

*Hình 4.6: Khả năng quan sát Linux sar(1)*

Hình này cho thấy sar(1) cung cấp phạm vi rộng cho nhân và thiết bị, và thậm chí có khả năng quan sát cho quạt. Tùy chọn -m (quản lý năng lượng) cũng hỗ trợ các đối số khác không hiển thị trong hình này, bao gồm IN cho đầu vào điện áp, TEMP cho nhiệt độ thiết bị, và USB cho thống kê năng lượng thiết bị USB.

### 4.4.2 Giám sát sar(1)

Bạn có thể thấy rằng việc thu thập dữ liệu (giám sát) sar(1) đã được kích hoạt cho hệ thống Linux của bạn. Nếu chưa, bạn cần kích hoạt nó. Để kiểm tra, chỉ cần chạy sar mà không có tùy chọn. Ví dụ:

```
$ sar
Cannot open /var/log/sysstat/sa19: No such file or directory
Please check if data collecting is enabled
```

Đầu ra cho thấy việc thu thập dữ liệu sar(1) chưa được kích hoạt trên hệ thống này (tệp sa19 chỉ kho lưu trữ hàng ngày cho ngày 19 của tháng). Các bước để kích hoạt có thể khác nhau tùy theo bản phân phối của bạn.

**Cấu hình (Ubuntu)**

Trên hệ thống Ubuntu này, tôi có thể kích hoạt thu thập dữ liệu sar(1) bằng cách chỉnh sửa tệp /etc/default/sysstat và đặt ENABLED thành true:

```
ubuntu# vi /etc/default/sysstat
#
# Default settings for /etc/init.d/sysstat, /etc/cron.d/sysstat
# and /etc/cron.daily/sysstat files
#
# Should sadc collect system activity informations? Valid values
# are "true" and "false". Please do not put other values, they
# will be overwritten by debconf!
ENABLED="true"
```

Và sau đó khởi động lại sysstat bằng:

```
ubuntu# service sysstat restart
```

Lịch trình ghi thống kê có thể được sửa đổi trong tệp crontab cho sysstat:

```
ubuntu# cat /etc/cron.d/sysstat
# The first element of the path is a directory where the debian-sa1
# script is located
PATH=/usr/lib/sysstat:/usr/sbin:/usr/sbin:/usr/bin:/sbin:/bin
# Activity reports every 10 minutes everyday
5-55/10 * * * * root command -v debian-sa1 > /dev/null && debian-sa1 1 1
# Additional run at 23:59 to rotate the statistics file
59 23 * * * root command -v debian-sa1 > /dev/null && debian-sa1 60 2
```

Cú pháp 5-55/10 có nghĩa là nó sẽ ghi mỗi 10 phút trong phạm vi từ phút 5 đến 55 qua giờ. Bạn có thể điều chỉnh để phù hợp với độ phân giải mong muốn: cú pháp được tài liệu hóa trong trang man crontab(5). Thu thập dữ liệu thường xuyên hơn sẽ tăng kích thước các tệp lưu trữ sar(1), có thể tìm thấy trong /var/log/sysstat.

Tôi thường thay đổi thu thập dữ liệu thành:

```
*/5 * * * * root command -v debian-sa1 > /dev/null && debian-sa1 1 1 -S ALL
```

*/5 sẽ ghi mỗi năm phút, và -S ALL sẽ ghi tất cả thống kê. Theo mặc định, sar(1) sẽ ghi hầu hết (nhưng không phải tất cả) nhóm thống kê. Tùy chọn -S ALL được sử dụng để ghi tất cả nhóm thống kê — nó được truyền cho sadc(1), và được tài liệu hóa trong trang man cho sadc(1). Cũng có phiên bản mở rộng, -S XALL, ghi thêm các phân tích chi tiết của thống kê.

**Báo cáo (Reporting)**

sar(1) có thể được thực thi với bất kỳ tùy chọn nào hiển thị trong Hình 4.6 để báo cáo nhóm thống kê đã chọn. Nhiều tùy chọn có thể được chỉ định. Ví dụ, đoạn sau báo cáo thống kê CPU (-u), TCP (-n TCP), và lỗi TCP (-n ETCP):

```
$ sar -u -n TCP,ETCP
Linux 4.15.0-66-generic (bgregg)        01/19/2020      _x86_64_        (8 CPU)

10:40:01 AM     CPU     %user     %nice   %system   %iowait    %steal     %idle
10:45:01 AM     all      6.87      0.00      2.84      0.18      0.00     90.12
10:50:01 AM     all      6.87      0.00      2.49      0.06      0.00     90.58
[...]

10:40:01 AM  active/s passive/s    iseg/s    oseg/s
10:45:01 AM      0.16      0.00     10.98      9.27
10:50:01 AM      0.20      0.00     10.40      8.93
[...]

10:40:01 AM  atmptf/s  estres/s retrans/s isegerr/s   orsts/s
10:45:01 AM      0.04      0.02      0.46      0.00      0.03
10:50:01 AM      0.03      0.02      0.53      0.00      0.03
[...]
```

Dòng đầu ra đầu tiên là tóm tắt hệ thống, hiển thị loại và phiên bản nhân, tên máy chủ, ngày, kiến trúc bộ xử lý, và số CPU.

Chạy sar -A sẽ xuất tất cả thống kê.

**Định dạng Đầu ra**

Gói sysstat đi kèm với lệnh sadf(1) để xem thống kê sar(1) ở các định dạng khác nhau, bao gồm JSON, SVG, và CSV. Các ví dụ sau xuất thống kê TCP (-n TCP) ở các định dạng này.

**JSON (-j):**

JavaScript Object Notation (JSON) có thể dễ dàng được phân tích và nhập bởi nhiều ngôn ngữ lập trình, khiến nó trở thành định dạng đầu ra phù hợp khi xây dựng phần mềm khác dựa trên sar(1).

```
$ sadf -j -- -n TCP
{"sysstat": {
  "hosts": [
    {
      "nodename": "bgregg",
      "sysname": "Linux",
      "release": "4.15.0-66-generic",
      "machine": "x86_64",
      "number-of-cpus": 8,
      "file-date": "2020-01-19",
      "file-utc-time": "18:40:01",
      "statistics": [
        {
          "timestamp": {"date": "2020-01-19", "time": "18:45:01", "utc": 1,
          "interval": 300},
          "network": {
            "net-tcp": {"active": 0.16, "passive": 0.00, "iseg": 10.98, "oseg": 9.27}
          }
        },
[...]
```

Bạn có thể xử lý đầu ra JSON tại dòng lệnh bằng công cụ jq(1).

**SVG (-g):**

sadf(1) có thể xuất tệp Scalable Vector Graphics (SVG) có thể được xem trong trình duyệt web. Hình 4.7 cho thấy một ví dụ. Bạn có thể sử dụng định dạng đầu ra này để xây dựng bảng điều khiển (dashboard) sơ khai.

*Hình 4.7: Đầu ra SVG sar(1) sadf(1)<sup>12</sup>*

> <sup>12</sup> Lưu ý rằng tôi đã chỉnh sửa tệp SVG để hình này dễ đọc hơn, thay đổi màu sắc và tăng kích thước phông chữ.

**CSV (-d):**

Định dạng giá trị phân tách bằng dấu phẩy (Comma-Separated Values — CSV) dành cho nhập vào cơ sở dữ liệu (và sử dụng dấu chấm phẩy):

```
$ sadf -d -- -n TCP
# hostname;interval;timestamp;active/s;passive/s;iseg/s;oseg/s
bgregg;300;2020-01-19 18:45:01 UTC;0.16;0.00;10.98;9.27
bgregg;299;2020-01-19 18:50:01 UTC;0.20;0.00;10.40;8.93
bgregg;300;2020-01-19 18:55:01 UTC;0.12;0.00;9.27;8.07
[...]
```

### 4.4.3 sar(1) Trực tiếp (Live)

Khi được thực thi với khoảng thời gian và số đếm tùy chọn, sar(1) thực hiện báo cáo trực tiếp. Chế độ này có thể được sử dụng ngay cả khi thu thập dữ liệu không được kích hoạt.

Ví dụ, hiển thị thống kê TCP với khoảng thời gian một giây và số đếm năm:

```
$ sar -n TCP 1 5
Linux 4.15.0-66-generic (bgregg)        01/19/2020      _x86_64_        (8 CPU)

03:09:04 PM  active/s passive/s    iseg/s    oseg/s
03:09:05 PM      1.00      0.00     33.00     42.00
03:09:06 PM      0.00      0.00    109.00     86.00
03:09:07 PM      0.00      0.00    107.00     67.00
03:09:08 PM      0.00      0.00    104.00    119.00
03:09:09 PM      0.00      0.00     70.00     70.00
Average:         0.20      0.00     84.60     76.80
```

Thu thập dữ liệu được thiết kế cho các khoảng thời gian dài, chẳng hạn như năm hoặc mười phút, trong khi báo cáo trực tiếp cho phép bạn xem biến thiên mỗi giây.

Các chương sau bao gồm nhiều ví dụ khác nhau về thống kê sar(1) trực tiếp.

### 4.4.4 Tài liệu sar(1)

Trang man sar(1) tài liệu hóa các thống kê riêng lẻ và bao gồm tên SNMP trong ngoặc vuông. Ví dụ:

```
$ man sar
[...]
active/s
    The number of times TCP connections have made a direct
    transition to the SYN-SENT state from the CLOSED state per
    second [tcpActiveOpens].

passive/s
    The number of times TCP connections have made a direct
    transition to the SYN-RCVD state from the LISTEN state per
    second [tcpPassiveOpens].

iseg/s
    The total number of segments received per second, including
    those received in error [tcpInSegs]. This count includes
    segments received on currently established connections.
[...]
```

Các cách sử dụng cụ thể của sar(1) được mô tả sau trong cuốn sách này; xem các Chương 6 đến 10. Phụ lục C là tóm tắt các tùy chọn và chỉ số của sar(1).

## 4.5 Công cụ Truy vết (Tracing Tools)

Các công cụ truy vết Linux sử dụng các giao diện sự kiện đã mô tả trước đó (tracepoint, kprobe, uprobe, USDT) để phân tích hiệu năng nâng cao. Các công cụ truy vết chính là:

- **perf(1)**: Trình lập hồ sơ chính thức của Linux. Nó xuất sắc cho lập hồ sơ CPU (lấy mẫu dấu vết ngăn xếp) và phân tích PMC, và có thể đo đạc các sự kiện khác, thường ghi vào tệp đầu ra để xử lý hậu kỳ.
- **Ftrace**: Trình truy vết chính thức của Linux, nó là một công cụ đa năng gồm nhiều tiện ích truy vết khác nhau. Nó phù hợp cho phân tích đường dẫn mã nhân và các hệ thống bị hạn chế tài nguyên, vì nó có thể được sử dụng mà không cần phụ thuộc.
- **BPF (BCC, bpftrace)**: Extended BPF đã được giới thiệu trong Chương 3, Hệ điều hành, Mục 3.4.4, Extended BPF. Nó cung cấp năng lượng cho các công cụ truy vết nâng cao, chủ yếu là BCC và bpftrace. BCC cung cấp các công cụ mạnh mẽ, và bpftrace cung cấp ngôn ngữ cấp cao cho lệnh một dòng (one-liner) và chương trình ngắn tùy chỉnh.
- **SystemTap**: Ngôn ngữ cấp cao và trình truy vết với nhiều tapset (thư viện) để truy vết các mục tiêu khác nhau [Eigler 05][Sourceware 20]. Gần đây nó đã phát triển backend BPF, mà tôi khuyên dùng (xem trang man stapbpf(8)).
- **LTTng**: Trình truy vết được tối ưu hóa cho ghi hộp đen (black-box recording): ghi tối ưu nhiều sự kiện để phân tích sau [LTTng 20].

Ba trình truy vết đầu tiên được đề cập trong Chương 13, perf; Chương 14, Ftrace; và Chương 15, BPF. Các chương tiếp theo (5 đến 12) bao gồm nhiều cách sử dụng khác nhau của các trình truy vết này, cho thấy các lệnh cần gõ và cách diễn giải đầu ra. Thứ tự này là có chủ đích, tập trung vào cách sử dụng và lợi ích hiệu năng trước, sau đó đề cập chi tiết hơn về các trình truy vết nếu và khi cần.

Tại Netflix, tôi sử dụng perf(1) cho phân tích CPU, Ftrace để đào sâu mã nhân, và BCC/bpftrace cho mọi thứ khác (bộ nhớ, hệ thống tệp, đĩa, mạng, và truy vết ứng dụng).

## 4.6 Quan sát Khả năng Quan sát (Observing Observability)

Các công cụ khả năng quan sát và các thống kê mà chúng được xây dựng trên đều được triển khai trong phần mềm, và tất cả phần mềm đều có tiềm năng có lỗi (bug). Điều tương tự cũng đúng cho tài liệu mô tả phần mềm. Hãy nhìn nhận với sự hoài nghi lành mạnh bất kỳ thống kê nào mới đối với bạn, đặt câu hỏi về ý nghĩa thực sự của chúng và liệu chúng có thực sự chính xác hay không.

Các chỉ số có thể gặp bất kỳ vấn đề nào sau đây:

- Công cụ và phép đo đôi khi sai.
- Trang man không phải lúc nào cũng đúng.
- Các chỉ số có sẵn có thể không đầy đủ.
- Các chỉ số có sẵn có thể được thiết kế kém và gây nhầm lẫn.
- Bộ thu thập chỉ số (ví dụ: phân tích đầu ra công cụ) có thể có lỗi.<sup>13</sup>
- Xử lý chỉ số (thuật toán/bảng tính) cũng có thể giới thiệu lỗi.

Khi nhiều công cụ khả năng quan sát có phạm vi chồng chéo, bạn có thể sử dụng chúng để kiểm tra chéo lẫn nhau. Lý tưởng nhất, chúng sẽ nguồn từ các framework đo đạc khác nhau để kiểm tra lỗi trong cả framework. Thiết bị đo đạc động đặc biệt hữu ích cho mục đích này, vì có thể tạo các công cụ tùy chỉnh để kiểm tra lại các chỉ số.

Một kỹ thuật xác minh khác là áp dụng khối lượng công việc đã biết và sau đó kiểm tra xem các công cụ khả năng quan sát có đồng ý với kết quả bạn mong đợi hay không. Điều này có thể liên quan đến việc sử dụng các công cụ đo hiệu năng vi mô (micro-benchmarking) báo cáo thống kê riêng để so sánh.

Đôi khi không phải công cụ hay thống kê bị sai, mà là tài liệu mô tả nó, bao gồm trang man. Phần mềm có thể đã phát triển mà tài liệu không được cập nhật.

Thực tế, bạn có thể không có thời gian để kiểm tra lại mọi phép đo hiệu năng bạn sử dụng và sẽ chỉ làm điều này nếu bạn gặp kết quả bất thường hoặc kết quả quan trọng cho công ty. Ngay cả khi bạn không kiểm tra lại, có thể có giá trị khi nhận thức rằng bạn đã không kiểm tra và bạn giả định các công cụ là chính xác.

Các chỉ số cũng có thể không đầy đủ. Khi đối mặt với số lượng lớn công cụ và chỉ số, có thể hấp dẫn khi giả định rằng chúng cung cấp phạm vi đầy đủ và hiệu quả. Điều này thường không đúng: các chỉ số có thể đã được thêm bởi lập trình viên để gỡ lỗi mã riêng của họ, và sau đó được xây dựng vào công cụ khả năng quan sát mà không nghiên cứu nhiều về nhu cầu thực tế của khách hàng. Một số lập trình viên có thể hoàn toàn không thêm bất kỳ chỉ số nào vào các hệ thống con mới.

> <sup>13</sup> Trong trường hợp này công cụ và phép đo là chính xác, nhưng bộ thu thập tự động đã giới thiệu lỗi. Tại Surge 2013, tôi đã có bài nói ngắn về một trường hợp đáng kinh ngạc [Gregg 13c]: một công ty đo hiệu năng báo cáo các chỉ số kém cho một sản phẩm tôi đang hỗ trợ, và tôi đã đào sâu. Hóa ra script shell họ sử dụng để tự động hóa benchmark có hai lỗi. Đầu tiên, khi xử lý đầu ra từ fio(1), nó lấy kết quả như "100KB/s" và sử dụng biểu thức chính quy để loại bỏ các ký tự không phải số, bao gồm "KB/s" để biến thành "100". Vì fio(1) báo cáo kết quả với đơn vị khác nhau (byte, Kbyte, Mbyte), điều này gây ra lỗi lớn (1024x). Thứ hai, họ cũng loại bỏ chữ số thập phân, nên kết quả "1.6" trở thành "16".

Sự vắng mặt của chỉ số có thể khó xác định hơn sự hiện diện của chỉ số kém. Chương 2, Phương pháp luận, có thể giúp bạn tìm các chỉ số thiếu bằng cách nghiên cứu các câu hỏi bạn cần trả lời cho phân tích hiệu năng.

## 4.7 Bài tập (Exercises)

Trả lời các câu hỏi sau về công cụ khả năng quan sát (bạn có thể muốn xem lại phần giới thiệu về một số thuật ngữ này trong Chương 1):

1. Liệt kê một số công cụ hiệu năng tĩnh.
2. Lập hồ sơ (profiling) là gì?
3. Tại sao các trình lập hồ sơ sử dụng 99 Hertz thay vì 100 Hertz?
4. Truy vết (tracing) là gì?
5. Thiết bị đo đạc tĩnh (static instrumentation) là gì?
6. Mô tả tại sao thiết bị đo đạc động (dynamic instrumentation) quan trọng.
7. Sự khác biệt giữa tracepoint và kprobe là gì?
8. Mô tả chi phí CPU dự kiến (thấp/trung bình/cao) từ các hoạt động sau:
   - Bộ đếm IOPS đĩa (như iostat(1) thấy)
   - Truy vết I/O đĩa theo-sự-kiện qua tracepoint hoặc kprobe
   - Truy vết chuyển đổi ngữ cảnh theo-sự-kiện (tracepoint/kprobe)
   - Truy vết thực thi tiến trình theo-sự-kiện (execve(2)) (tracepoint/kprobe)
   - Truy vết malloc() libc theo-sự-kiện qua uprobe
9. Mô tả tại sao PMC có giá trị cho phân tích hiệu năng.
10. Cho một công cụ khả năng quan sát, mô tả cách bạn có thể xác định nó sử dụng nguồn đo đạc nào.

## 4.8 Tài liệu Tham khảo (References)

[Eigler 05] Eigler, F. Ch., et al. "Architecture of SystemTap: A Linux Trace/Probe Tool," http://sourceware.org/systemtap/archpaper.pdf, 2005.

[Drongowski 07] Drongowski, P., "Instruction-Based Sampling: A New Performance Analysis Technique for AMD Family 10h Processors," AMD (Whitepaper), 2007.

[Ayuso 12] Ayuso, P., "The Conntrack-Tools User Manual," http://conntrack-tools.netfilter.org/manual.html, 2012.

[Gregg 13c] Gregg, B., "Benchmarking Gone Wrong," Surge 2013: Lightning Talks, https://www.youtube.com/watch?v=vm1GJMp0QN4#t=17m48s, 2013.

[Weisbecker 13] Weisbecker, F., "Status of Linux dynticks," OSPERT, http://www.ertl.jp/~shinpei/conf/ospert13/slides/FredericWeisbecker.pdf, 2013.

[Intel 16] Intel 64 and IA-32 Architectures Software Developer's Manual Volume 3B: System Programming Guide, Part 2, September 2016.

[AMD 18] Open-Source Register Reference for AMD Family 17h Processors Models 00h-2Fh, https://developer.amd.com/resources/developer-guides-manuals, 2018.

[ARM 19] Arm® Architecture Reference Manual Armv8, for Armv8-A architecture profile, 2019.

[Gregg 19] Gregg, B., BPF Performance Tools: Linux System and Application Observability, Addison-Wesley, 2019.

[Atoptool 20] "Atop," www.atoptool.nl/index.php, accessed 2020.

[Bowden 20] Bowden, T., Bauer, B., et al., "The /proc Filesystem," Linux documentation, https://www.kernel.org/doc/html/latest/filesystems/proc.html, accessed 2020.

[Gregg 20a] Gregg, B., "Linux Performance," http://www.brendangregg.com/linuxperf.html, accessed 2020.

[LTTng 20] "LTTng," https://lttng.org, accessed 2020.

[PCP 20] "Performance Co-Pilot," https://pcp.io, accessed 2020.

[Prometheus 20] "Exporters and Integrations," https://prometheus.io/docs/instrumenting/exporters, accessed 2020.

[Sourceware 20] "SystemTap," https://sourceware.org/systemtap, accessed 2020.

[Ts'o 20] Ts'o, T., Zefan, L., and Zanussi, T., "Event Tracing," Linux documentation, https://www.kernel.org/doc/html/latest/trace/events.html, accessed 2020.

[Xenbits 20] "Xen Hypervisor Command Line Options," https://xenbits.xen.org/docs/4.11-testing/misc/xen-command-line.html, accessed 2020.

[UTK 20] "Performance Application Programming Interface," http://icl.cs.utk.edu/papi, accessed 2020.
