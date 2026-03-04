# Chương 15: BPF

Chương này mô tả các tracing front ends BCC và bpftrace cho BPF mở rộng. Những front ends này cung cấp một bộ sưu tập các công cụ phân tích hiệu năng, và những công cụ này đã được sử dụng trong các chương trước. Công nghệ BPF đã được giới thiệu trong Chương 3, Hệ điều hành, Mục 3.4.4, BPF mở rộng. Tóm lại, BPF mở rộng là một môi trường thực thi kernel có thể cung cấp các khả năng lập trình cho các trình truy vết.

Chương này, cùng với Chương 13, perf, và Chương 14, Ftrace, là tài liệu đọc tùy chọn cho những ai muốn tìm hiểu chi tiết hơn về một hoặc nhiều trình truy vết hệ thống.

Các công cụ BPF mở rộng có thể được sử dụng để trả lời các câu hỏi chẳng hạn như:
- Độ trễ của đĩa I/O là bao nhiêu, dưới dạng một biểu đồ histogram?
- Độ trễ trình lập lịch CPU có đủ cao để gây ra các vấn đề không?
- Các ứng dụng có đang chịu đựng độ trễ hệ thống tập tin không?
- Những phiên TCP nào đang xảy ra và với những thời lượng nào?
- Những đường dẫn mã nào đang bị chặn và trong bao lâu?

Điều làm cho BPF khác biệt so với các trình truy vết khác là nó có thể lập trình được. Nó cho phép các chương trình do người dùng định nghĩa được thực thi trên các sự kiện, các chương trình có thể thực hiện lọc, lưu và truy xuất thông tin, tính toán độ trễ, thực hiện tổng hợp trong kernel và các tóm tắt tùy chỉnh, và nhiều hơn nữa. Trong khi các trình truy vết khác có thể yêu cầu đổ tất cả các sự kiện tới không gian người dùng và xử lý hậu kỳ chúng, BPF cho phép việc xử lý diễn ra hiệu quả trong ngữ cảnh kernel. Điều này khiến cho việc tạo ra các công cụ hiệu năng thứ mà mặt khác sẽ tiêu tốn quá nhiều chi phí cho mục đích sử dụng sản xuất trở nên thực tế.

Chương này có một phần chính cho mỗi front end được khuyến nghị. Các phần then chốt là:
- **15.1: BCC**
  - 15.1.1: Cài đặt (Installation)
  - 15.1.2: Phạm vi bao phủ của công cụ (Tool Coverage)
  - 15.1.3: Các công cụ đơn mục đích (Single-Purpose Tools)
  - 15.1.4: Các công cụ đa mục đích (Multi-Purpose Tools)
  - 15.1.5: Các lệnh một dòng (One-Liners)
- **15.2: bpftrace**
  - 15.2.1: Cài đặt (Installation)
  - 15.2.2: Các công cụ (Tools)
  - 15.2.3: Các lệnh một dòng (One-Liners)
  - 15.2.4: Lập trình (Programming)
  - 15.2.5: Tham chiếu (Reference)

Sự khác biệt giữa BCC và bpftrace có thể rõ ràng từ việc sử dụng chúng trong các chương trước: BCC phù hợp cho các công cụ phức tạp, và bpftrace phù hợp cho các chương trình tùy chỉnh tùy biến (ad hoc). Một số công cụ được triển khai trong cả hai, như được trình bày trong Hình 15.1.

(Hình 15.1 BPF tracing front ends)

Các sự khác biệt cụ thể giữa BCC và bpftrace được tóm tắt trong Bảng 15.1.

Bảng 15.1 BCC so với bpftrace
| Đặc tính | BCC | bpftrace |
| --- | --- | --- |
| Số lượng công cụ theo kho lưu trữ | >80 (bcc) | >30 (bpftrace) >120 (bpf-perf-tools-book) |
| Cách sử dụng công cụ | Thường hỗ trợ các tùy chọn phức tạp (-h, -p PID, v.v.) và các đối số | Thông thường đơn giản: không có tùy chọn, và không có hoặc có một đối số |
| Tài liệu công cụ | Các trang man, các tệp ví dụ | Các trang man, các tệp ví dụ |
| Ngôn ngữ lập trình | Không gian người dùng: Python, Lua, C, hoặc C++ Không gian kernel: C | bpftrace |
| Độ khó lập trình | Khó | Dễ |
| Các loại kết quả cho mỗi sự kiện | Bất cứ thứ gì | Văn bản, JSON |
| Các loại tóm tắt | Bất cứ thứ gì | Các số lượng, min, max, sum, avg, log2 histograms, linear histograms; theo không có hoặc có thêm nhiều khóa |
| Hỗ trợ thư viện | Có (ví dụ: Python import) | Không |
| Độ dài chương trình trung bình¹ (không có lời bình luận) | 228 dòng | 28 dòng |

---
¹ Dựa trên các công cụ được cung cấp trong kho lưu trữ chính thức và kho lưu trữ sách BPF của tôi.

---

Cả BCC và bpftrace đều đang được sử dụng tại nhiều công ty bao gồm Facebook và Netflix. Netflix cài đặt chúng theo mặc định trên tất cả các thực thể đám mây, và sử dụng chúng cho phân tích sâu hơn sau khi giám sát và các dashboards trên toàn đám mây, cụ thể là [Gregg 18e]:
- **BCC:** Các công cụ có sẵn được sử dụng tại dòng lệnh để phân tích I/O lưu trữ, mạng I/O, và thực thi tiến trình, khi cần thiết. Một số công cụ BCC được thực thi tự động bởi một hệ thống dashboard hiệu năng đồ họa để cung cấp dữ liệu cho các bản đồ nhiệt (heat maps) độ trễ đĩa I/O và trình lập lịch. Ngoài ra, một công cụ BCC tùy chỉnh luôn chạy dưới dạng một daemon (dựa trên tcplife(8)) ghi nhật ký các sự kiện mạng tới lưu trữ đám mây cho việc phân tích luồng.
- **bpftrace:** Các công cụ bpftrace tùy chỉnh được phát triển khi cần thiết để hiểu các bệnh lý kernel và ứng dụng.

Các phần sau đây giải thích các công cụ BCC, các công cụ bpftrace, và lập trình bpftrace.

## 15.1 BCC
Bộ sưu tập Trình biên dịch BPF (BPF Compiler Collection - hay gọi là “bcc” theo tên dự án và gói) là một dự án mã nguồn mở chứa một bộ sưu tập lớn các công cụ phân tích hiệu năng nâng cao, cũng như một framework để xây dựng chúng. BCC được tạo ra bởi Brenden Blanco; tôi đã giúp đỡ với quá trình phát triển của nó và tạo ra nhiều công cụ truy vết.

Như một ví dụ về một công cụ BCC, biolatency(8) hiển thị phân phối độ trễ của đĩa I/O dưới dạng các biểu đồ histograms lũy thừa của hai, và có thể chia nhỏ nó theo các cờ I/O:

```bash
# biolatency.py -mF
Tracing block device I/O... Hit Ctrl-C to end.
^C

flags = Priority-Metadata-Read
     msecs               : count     distribution
         0 -> 1          : 90        |****************************************|

flags = Write
     msecs               : count     distribution
         0 -> 1          : 24        |****************************************|
         2 -> 3          : 0         |                                        |
         4 -> 7          : 8         |*************                           |

flags = ReadAhead-Read
     msecs               : count     distribution
         0 -> 1          : 3031      |****************************************|
         2 -> 3          : 10        |                                        |
         4 -> 7          : 5         |                                        |
         8 -> 15         : 3         |                                        |
```

Kết quả này cho thấy một phân phối ghi (write) hai chế độ (bi-model), và nhiều I/O với các cờ “ReadAhead-Read.” Công cụ này sử dụng BPF để tóm tắt các biểu đồ histograms trong không gian kernel nhằm đạt hiệu quả, sao cho thành phần không gian người dùng chỉ cần đọc các biểu đồ histograms đã được tóm tắt sẵn (các cột số lượng) và in chúng ra.

Những công cụ BCC này thông thường có các thông điệp sử dụng (-h), các trang man, và các tệp ví dụ trong kho lưu trữ BCC:
https://github.com/iovisor/bcc

Phần này tóm tắt BCC và các công cụ phân tích hiệu năng đơn mục đích và đa mục đích của nó.

### 15.1.1 Cài đặt (Installation)
Các gói của BCC có sẵn cho nhiều bản phân phối Linux, bao gồm Ubuntu, Debian, RHEL, Fedora, và Amazon Linux, giúp việc cài đặt trở nên tầm thường. Hãy tìm kiếm “bcc-tools” hoặc “bpfcc-tools” hoặc “bcc” (các bên duy trì gói đã đặt tên cho chúng khác nhau).

Bạn cũng có thể xây dựng BCC từ mã nguồn. Để biết các hướng dẫn cài đặt và xây dựng mới nhất, hãy kiểm tra INSTALL.md trong kho lưu trữ BCC [Iovisor 20b]. INSTALL.md cũng liệt kê các yêu cầu cấu hình kernel (bao gồm CONFIG_BPF=y, CONFIG_BPF_SYSCALL=y, CONFIG_BPF_EVENTS=y). BCC yêu cầu ít nhất Linux 4.4 cho một số công cụ để hoạt động; cho hầu hết các công cụ, yêu cầu Linux 4.9 hoặc mới hơn.

### 15.1.2 Phạm vi bao phủ của công cụ (Tool Coverage)
Các công cụ truy vết BCC được hình ảnh hóa trong Hình 15.2 (một số được nhóm lại sử dụng các ký tự đại diện: ví dụ, java* cho tất cả các công cụ bắt đầu với “java”).

Nhiều công cụ là các công cụ đơn mục đích được hiển thị với một đầu mũi tên duy nhất; một số là các công cụ đa mục đích được liệt kê ở bên trái với một mũi tên kép để chỉ ra phạm vi bao phủ của chúng.

(Hình 15.2 Các công cụ BCC)

### 15.1.3 Các công cụ Đơn mục đích (Single-Purpose Tools)
Tôi đã phát triển nhiều trong số này theo cùng triết lý “làm một việc và làm nó tốt” như những công cụ trong perf-tools trong Chương 14. Thiết kế này bao gồm việc làm cho kết quả mặc định của chúng súc tích và thường là đủ. Bạn có thể “just run biolatency” mà không cần phải học bất kỳ tùy chọn dòng lệnh nào, và thông thường nhận được kết quả đủ để giải quyết vấn đề của mình mà không bị lộn xộn. Các tùy chọn thông thường tồn tại cho việc tùy chỉnh, chẳng hạn như biolatency(8) -F để chia nhỏ theo các cờ I/O, đã trình bày trước đó.

Một sự lựa chọn các công cụ đơn mục đích được mô tả trong Bảng 15.2, bao gồm cả vị trí của chúng trong cuốn sách này nếu hiện diện. Xem kho lưu trữ BCC cho danh sách đầy đủ [Iovisor 20a].

Bảng 15.2 Các công cụ BCC đơn mục đích được lựa chọn
| Công cụ | Mô tả | Mục |
| --- | --- | --- |
| biolatency(8) | Tóm tắt độ trễ I/O khối (đĩa I/O) dưới dạng một biểu đồ histogram | 9.6.6 |
| biotop(8) | Tóm tắt I/O khối theo tiến trình | 9.6.8 |
| biosnoop(8) | Truy vết I/O khối với độ trễ và các chi tiết khác | 9.6.7 |
| bitesize(8) | Tóm tắt kích thước I/O khối dưới dạng các biểu đồ histograms tiến trình | - |
| btrfsdist(8) | Tóm tắt độ trễ thao tác btrfs dưới dạng các biểu đồ histograms | 8.6.13 |
| btrfsslower(8) | Truy vết các thao tác btrfs chậm | 8.6.14 |
| cpudist(8) | Tóm tắt thời gian on- và off-CPU theo từng tiến trình dưới dạng một biểu đồ histogram | 6.6.15, 16.1.7 |
| cpuunclaimed(8) | Hiển thị CPU không được yêu cầu và rảnh rỗi bất chấp nhu cầu | - |
| criticalstat(8) | Truy vết các đoạn mã kernel quan trọng nguyên tử dài | - |
| dbslower(8) | Truy vết các truy vấn chậm của cơ sở dữ liệu | - |
| dbstat(8) | Tóm tắt độ trễ thao tác cơ sở dữ liệu dưới dạng một biểu đồ histogram | - |
| drsnoop(8) | Truy vết các sự kiện thu hồi bộ nhớ trực tiếp (direct memory reclaim events) với PID và độ trễ | 7.5.11 |
| execsnoop(8) | Truy vết các tiến trình mới qua các syscall execve(2) | 1.7.3, 5.5.5 |
| ext4dist(8) | Tóm tắt độ trễ thao tác ext4 dưới dạng các biểu đồ histograms | 8.6.13 |
| ext4slower(8) | Truy vết các thao tác ext4 chậm | 8.6.14 |
| filelife(8) | Truy vết tuổi thọ của các tệp tồn tại ngắn ngủi | - |
| gethostlatency(8) | Truy vết độ trễ DNS qua các hàm phân giải | - |
| hardirqs(8) | Tóm tắt thời gian sự kiện hardirq | 6.6.19 |
| killsnoop(8) | Truy vết các tín hiệu được phát ra bởi syscall kill(2) | - |
| klockstat(8) | Tóm tắt các thống kê khóa mutex kernel | - |
| llcstat(8) | Tóm tắt các tham chiếu và trượt bộ đệm ẩn CPU theo từng tiến trình | - |
| memleak(8) | Hiển thị các lần cấp phát bộ nhớ chưa giải phóng (outstanding memory allocations) | - |
| mysqld_qslower(8) | Truy vết các truy vấn chậm của MySQL | - |
| nfsdist(8) | Tóm tắt các thao tác NFS chậm | 8.6.13 |
| nfsslower(8) | Tóm tắt độ trễ thao tác NFS dưới dạng các biểu đồ histograms | 8.6.14 |
| offcputime(8) | Tóm tắt thời gian off-CPU theo vết ngăn xếp | 5.5.3 |
| offwaketime(8) | Tóm tắt thời gian bị chặn theo ngăn xếp off-CPU và ngăn xếp waker | - |
| oomkill(8) | Truy vết trình giết hết bộ nhớ (out-of-memory - OOM) killer | - |
| readdist(8) | Tóm tắt độ trễ thao tác đọc dưới dạng biểu đồ histogram | 8.6.10 |
| profile(8) | Hồ sơ sử dụng CPU bằng cách sử dụng lấy mẫu theo thời gian các vết ngăn xếp | 5.5.2 |
| runqlat(8) | Tóm tắt độ trễ hàng đợi chạy (trình lập lịch) dưới dạng một biểu đồ histogram | 6.6.16 |
| runqlen(8) | Tóm tắt độ dài hàng đợi chạy sử dụng lấy mẫu theo thời gian | 6.6.17 |
| runqslower(8) | Truy vết các độ trễ hàng đợi chạy dài | - |
| syncsnoop(8) | Truy vết các syscall họ sync(2) | - |
| syscount(8) | Tóm tắt số lượng và độ trễ của syscall | 5.5.6 |
| tcplife(8) | Truy vết các phiên TCP và tóm tắt thời lượng của chúng | 10.6.9 |
| tcpretrans(8) | Truy vết các lần truyền lại TCP với các chi tiết bao gồm trạng thái kernel | 10.6.11 |
| tcptop(8) | Tóm tắt thông lượng gửi/nhận TCP theo host và PID | 10.6.10 |
| wakeuptime(8) | Tóm tắt thời gian ngủ tới khi thức dậy theo vết ngăn xếp | - |
| xfsdist(8) | Tóm tắt độ trễ thao tác xfs dưới dạng các biểu đồ histograms | 8.6.13 |
| xfsslower(8) | Truy vết các thao tác xfs chậm | 8.6.14 |
| zfsdist(8) | Tóm tắt độ trễ thao tác zfs dưới dạng các biểu đồ histograms | 8.6.13 |
| zfsslower(8) | Truy vết các thao tác zfs chậm | 8.6.14 |

Để có các ví dụ về những công cụ này, hãy xem các chương trước cũng như các tệp *_example.txt trong kho lưu trữ BCC (nhiều cái trong số đó tôi cũng đã viết). Cho các công cụ không được bao quát trong cuốn sách này, cũng hãy xem [Gregg 19].

### 15.1.4 Các công cụ Đa mục đích (Multi-Purpose Tools)
Các công cụ đa mục đích được liệt kê ở bên trái của Hình 15.2. Những thứ này hỗ trợ nhiều nguồn sự kiện và có thể thực hiện nhiều vai trò, tương tự như perf(1), mặc dù điều này cũng làm cho chúng trở nên phức tạp để sử dụng. Chúng được mô tả trong Bảng 15.3.

Bảng 15.3 Các công cụ perf-tools đa mục đích
| Công cụ | Mô tả | Mục |
| --- | --- | --- |
| argdist(8) | Hiển thị các giá trị tham số hàm dưới dạng một biểu đồ histogram hoặc số lượng | 15.1.15 |
| funccount(8) | Đếm các lệnh gọi hàm kernel hoặc cấp người dùng | 15.1.15 |
| funcslower(8) | Truy vết các lệnh gọi hàm kernel hoặc cấp người dùng chậm | - |
| funclatency(8) | Tóm tắt độ trễ hàm dưới dạng một biểu đồ histogram | - |
| stackcount(8) | Đếm các vết ngăn xếp đã dẫn tới một sự kiện | 15.1.15 |
| trace(8) | Truy vết các hàm tùy ý với các bộ lọc | 15.1.15 |

Để giúp bạn nhớ những lần gọi hữu ích, bạn có thể thu thập các lệnh một dòng. Tôi đã cung cấp một số trong phần tiếp theo, tương tự như các phần lệnh một dòng của tôi cho perf(1) và trace-cmd.

### 15.1.5 One-Liners
Các lệnh một dòng sau đây truy vết trên toàn hệ thống cho đến khi nhấn Ctrl-C, trừ khi có quy định khác. Chúng được nhóm theo công cụ.

**funccount(8)**
Đếm các lệnh gọi VFS kernel:
`funccount 'vfs_*'`

Đếm các lệnh gọi TCP kernel:
`funccount 'tcp_*'`

Đếm các lệnh gọi gửi TCP mỗi giây:
`funccount -i 1 'tcp_send*'`

Hiển thị tốc độ của các sự kiện I/O khối mỗi giây:
`funccount -i 1 't:block:*'`

Hiển thị tốc độ của libc getaddrinfo() (phân giải tên) mỗi giây:
`funccount -i 1 c:getaddrinfo`

**stackcount(8)**
Đếm các vết ngăn xếp đã tạo ra I/O khối:
`stackcount t:block:block_rq_insert`

Đếm các vết ngăn xếp đã dẫn tới việc gửi các gói tin IP, với PID chịu trách nhiệm:
`stackcount -P ip_output`

Đếm các vết ngăn xếp đã dẫn tới việc luồng bị chặn và rời khỏi CPU:
`stackcount t:sched:sched_switch`

**trace(8)**
Truy vết hàm kernel do_sys_open() với tên tệp:
`trace 'do_sys_open "%s", arg2'`

Truy vết kết quả trả về của hàm kernel do_sys_open() và in giá trị trả về:
`trace 'r::do_sys_open "ret: %d", retval'`

Truy vết hàm kernel do_nanosleep() với chế độ và các ngăn xếp cấp người dùng:
`trace -U 'do_nanosleep "mode: %d", arg2'`

Truy vết các yêu cầu xác thực qua thư viện pam:
`trace 'pam:pam_start "%s: %s", arg1, arg2'`

**argdist(8)**
Tóm tắt các lần đọc VFS theo giá trị trả về (kích thước hoặc lỗi):
`argdist -H 'r::vfs_read()'`

Tóm tắt lệnh gọi libc read() theo giá trị trả về (kích thước hoặc lỗi) cho PID 1005:
`argdist -p 1005 -H 'r:c:read()'`

Đếm các syscalls theo ID syscall:
`argdist.py -C 't:raw_syscalls:sys_enter():int:args->id'`

Tóm tắt đối số kích thước tcp_sendmsg() của kernel bằng các số lượng:
`argdist -C 'p::tcp_sendmsg(struct sock *sk, struct msghdr *msg, size_t size):u32:size'`

Tóm tắt kích thước tcp_sendmsg() dưới dạng một biểu đồ histogram lũy thừa của hai:
`argdist -H 'p::tcp_sendmsg(struct sock *sk, struct msghdr *msg, size_t size):u32:size'`

Đếm lệnh gọi libc write() cho PID 181 theo file descriptor:
`argdist -p 181 -C 'p:c:write(int fd):int:fd'`

Tóm tắt các lệnh đọc theo tiến trình khi độ trễ là >100 μs:
`argdist -C 'r::___vfs_read():u32:$PID:$latency > 100000'`

### 15.1.6 Multi-Tool Example
Như một ví dụ về việc sử dụng một công cụ đa năng, phần sau đây chỉ ra việc truy vết hàm kernel do_sys_open() bằng công cụ trace(8), và in đối số thứ hai dưới dạng một chuỗi:

```bash
# trace 'do_sys_open "%s", arg2'
PID    TID    COMM      FUNC             -
28887  28887  ls        do_sys_open      /etc/ld.so.cache
28887  28887  ls        do_sys_open      /lib/x86_64-linux-gnu/libselinux.so.1
28887  28887  ls        do_sys_open      /lib/x86_64-linux-gnu/libc.so.6
28887  28887  ls        do_sys_open      /lib/x86_64-linux-gnu/libpcre2-8.so.0
28887  28887  ls        do_sys_open      /lib/x86_64-linux-gnu/libdl.so.2
28887  28887  ls        do_sys_open      /lib/x86_64-linux-gnu/libpthread.so.0
28887  28887  ls        do_sys_open      /proc/filesystems
28887  28887  ls        do_sys_open      /usr/lib/locale/locale-archive
[...]
```

Cú pháp trace được lấy cảm hứng từ printf(3), hỗ trợ một chuỗi định dạng và các đối số. Trong trường hợp này arg2, đối số thứ hai, đã được in dưới dạng một chuỗi vì nó chứa tên tệp.

Cả trace(8) và argdist(8) đều hỗ trợ cú pháp cho phép nhiều lệnh một dòng tùy chỉnh được tạo ra. bpftrace, được bao quát trong các phần sau, tiến xa hơn nữa, cung cấp một ngôn ngữ hoàn chỉnh cho việc viết các chương trình một dòng hoặc đa dòng.

### 15.1.7 BCC so với bpftrace
Các sự khác biệt đã được tóm tắt ở phần đầu của chương này. BCC phù hợp cho các công cụ tùy chỉnh và phức tạp, hỗ trợ nhiều loại đối số, hoặc sử dụng một loạt các thư viện. bpftrace rất phù hợp cho các lệnh một dòng hoặc các chương trình ngắn chấp nhận không có đối số, hoặc một đối số số nguyên đơn lẻ. BCC cho phép chương trình BPF tại trái tim của công cụ truy vết được viết bằng C, cho phép kiểm soát hoàn toàn. Điều này đi kèm với cái giá là độ phức tạp: các công cụ BCC có thể mất thời gian gấp mười lần để phát triển so với các chương trình bpftrace tương đương. Vì việc phát triển một công cụ điển hình yêu cầu nhiều lần lặp lại, tôi thấy rằng việc phát triển các công cụ trong bpftrace trước tiên sẽ tiết kiệm thời gian, thứ nhanh hơn, và sau đó chuyển chúng sang BCC nếu cần thiết.

Sự khác biệt giữa BCC và bpftrace giống như sự khác biệt giữa lập trình C và lập trình shell, nơi BCC giống như lập trình C (một phần trong số đó *là* lập trình C) và bpftrace giống như lập trình shell. Trong công việc hàng ngày của mình, tôi sử dụng nhiều chương trình C được xây dựng sẵn (top(1), vmstat(1), v.v.) và phát triển các shell scripts tùy chỉnh một lần. Tương tự như vậy, tôi cũng sử dụng nhiều công cụ BCC được xây dựng sẵn, và phát triển các công cụ bpftrace tùy chỉnh một lần.

Tôi đã cung cấp tài liệu trong cuốn sách này để hỗ trợ cách sử dụng này: nhiều chương chỉ ra các công cụ BCC bạn có thể sử dụng, và các phần sau đó trong chương này chỉ ra cách bạn có thể phát triển các công cụ bpftrace tùy chỉnh.

### 15.1.8 Tài liệu
Các công cụ thường có một thông điệp sử dụng để tóm tắt cú pháp của chúng. Ví dụ:

```bash
# funccount -h
usage: funccount [-h] [-p PID] [-i INTERVAL] [-d DURATION] [-T] [-r] [-D]
                 pattern

Count functions, tracepoints, and USDT probes

positional arguments:
  pattern               search expression for events

optional arguments:
  -h, --help            show this help message and exit
  -p PID, --pid PID     trace this PID only
  -i INTERVAL, --interval INTERVAL
                        summary interval, seconds
  -d DURATION, --duration DURATION
                        total duration of trace, seconds
  -T, --timestamp       include timestamp on output
  -r, --regexp          use regular expressions. Default is "*" wildcards
                        only.
  -D, --debug           print BPF program before starting (for debugging
                        purposes)

examples:
    ./funccount 'vfs_*'             # count kernel fns starting with "vfs"
    ./funccount -r '^vfs.*'         # same as above, using regular expressions
    ./funccount -Ti 5 'vfs_*'       # output every 5 seconds, with timestamps
    ./funccount -d 10 'vfs_*'       # trace for 10 seconds only
    ./funccount -p 185 'vfs_*'      # count vfs calls for PID 181 only
    ./funccount t:sched:sched_fork  # count calls to the sched_fork tracepoint
    ./funccount -p 185 u:node:gc*   # count all GC USDT probes in node, PID 185
    ./funccount c:malloc            # count all malloc() calls in libc
    ./funccount go:os.*             # count all "os.*" calls in libgo
    ./funccount -p 185 go:os.*      # count all "os.*" calls in libgo, PID 185
    ./funccount ./test:read*        # count "read*" calls in the ./test binary
```

Mọi công cụ cũng có một trang man (man/man8/funccount.8) và một tệp các ví dụ (examples/funccount_example.txt) trong kho lưu trữ bcc. Các tệp ví dụ chứa kết quả mẫu với lời bình luận.

Tôi cũng đã tạo ra các tài liệu sau đây trong kho lưu trữ BCC [Iovisor 20b]:
- **Hướng dẫn cho người dùng cuối (Tutorial for end users):** docs/tutorial.md
- **Hướng dẫn cho các nhà phát triển BCC (Tutorial for BCC developers):** docs/tutorial_bcc_python_developer.md
- **Hướng dẫn Tham chiếu (Reference Guide):** docs/reference_guide.md

Chương 4 trong cuốn sách trước đó của tôi tập trung vào BCC [Gregg 19].

---

## 15.2 bpftrace
bpftrace là một trình truy vết mã nguồn mở được xây dựng dựa trên BPF và BCC, thứ cung cấp không chỉ một bộ các công cụ phân tích hiệu năng, mà còn là một ngôn ngữ lập trình cấp cao để giúp bạn phát triển những công cụ mới. Ngôn ngữ này đã được thiết kế để đơn giản và dễ học. Nó là awk(1) của việc truy vết, và dựa trên awk(1). Trong bpftrace, bạn viết một stanza chương trình để xử lý một sự kiện đầu vào, và với bpftrace bạn viết một chương trình để xử lý một dòng văn bản đầu vào. bpftrace được tạo ra bởi Alastair Robertson, và tôi đã trở thành một bên đóng góp chính.

Như một ví dụ về bpftrace, lệnh một dòng sau đây hiển thị phân phối kích thước thông điệp nhận TCP theo tên tiến trình:

```bash
# bpftrace -e 'kr:tcp_recvmsg /retval >= 0/ { @recv_bytes[comm] = hist(retval); }'
Attaching 1 probe...
^C

@recv_bytes[sshd]:
[32, 64)               7 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[64, 128)              2 |@@@@@@@@@@@@@@                                      |

@recv_bytes[nodejs]:
[0]                   82 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@                        |
[1]                  135 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      |
[2, 4)               153 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[4, 8)                12 |@@@@                                                |
[8, 16)                6 |@@                                                  |
[16, 32)              32 |@@@@@@@@@@                                          |
[32, 64)             158 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[64, 128)            155 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[128, 256)            14 |@@@@                                                |
```

Kết quả này cho thấy các tiến trình nodejs có kích thước nhận hai chế độ (bi-modal), với một chế độ xấp xỉ 0 tới 4 byte và một chế độ khác trong khoảng từ 32 tới 128 byte.

Sử dụng một cú pháp súc tích, lệnh một dòng bpftrace này đã sử dụng một kretprobe để instrument tcp_recvmsg(), được lọc cho trường hợp khi giá trị trả về là số dương (để loại trừ các mã lỗi âm), và nạp vào một đối tượng bản đồ BPF mang tên @recv_bytes với một biểu đồ histogram của giá trị trả về, sử dụng tên tiến trình (comm) làm khóa. Khi Ctrl-C được nhấn và bpftrace nhận được tín hiệu (SIGINT), nó sẽ kết thúc và tự động in ra các bản đồ BPF. Cú pháp này được giải thích chi tiết hơn trong các phần tiếp theo.

Bên cạnh việc cho phép bạn viết mã cho các lệnh một dòng của riêng mình, bpftrace đi kèm với nhiều công cụ sẵn có trong kho lưu trữ của nó:
https://github.com/iovisor/bpftrace

Phần này tóm tắt các công cụ bpftrace và ngôn ngữ lập trình bpftrace. Phần này dựa trên tài liệu bpftrace trong [Gregg 19], thứ khám phá bpftrace sâu hơn.

### 15.2.1 Cài đặt
Các gói cho bpftrace có sẵn cho nhiều bản phân phối Linux, bao gồm Ubuntu, giúp việc cài đặt trở nên tầm thường. Hãy tìm kiếm các gói mang tên “bpftrace”; chúng tồn tại cho Ubuntu, Fedora, Gentoo, Debian, OpenSUSE, và CentOS. RHEL 8.2 có bpftrace dưới dạng một Technology Preview.

Bên cạnh các gói, cũng có các Docker images của bpftrace, file nhị phân bpftrace thứ không yêu cầu sự phụ thuộc nào ngoài glibc, và các hướng dẫn để xây dựng bpftrace từ mã nguồn. Đối với tài liệu về những tùy chọn này hãy xem INSTALL.md trong kho lưu trữ bpftrace [Iovisor 20a], tệp này cũng liệt kê các yêu cầu kernel (bao gồm CONFIG_BPF=y, CONFIG_BPF_SYSCALL=y, CONFIG_BPF_EVENTS=y). bpftrace yêu cầu Linux 4.9 hoặc mới hơn.

### 15.2.2 Các công cụ
Các công cụ truy vết bpftrace được hình ảnh hóa trong Hình 15.3.

Các công cụ trong kho lưu trữ bpftrace được hiển thị bằng màu đen. Cho cuốn sách trước của tôi, tôi đã phát triển nhiều công cụ truy vết bpftrace hơn và phát hành chúng dưới dạng mã nguồn mở trong kho lưu trữ bpf-perf-tools-book: chúng được hiển thị bằng màu đỏ/xám [Gregg 19g].

(Hình 15.3 Các công cụ bpftrace)

### 15.2.3 One-Liners
Các lệnh một dòng sau đây truy vết trên toàn hệ thống cho đến khi nhấn Ctrl-C, trừ khi có quy định khác. Bên cạnh tính hữu ích thực tế của chúng, chúng cũng có thể phục vụ như các ví dụ nhỏ về ngôn ngữ lập trình bpftrace. Những lệnh này được nhóm theo mục tiêu. Nhiều danh sách các lệnh một dòng bpftrace có thể tìm thấy trong mỗi chương tài nguyên.

**CPUs**
Truy vết các tiến trình mới với các đối số:
`bpftrace -e 'tracepoint:syscalls:sys_enter_execve { join(args->argv); }'`

Đếm các syscalls theo tiến trình:
`bpftrace -e 'tracepoint:raw_syscalls:sys_enter { @[pid, comm] = count(); }'`

Lấy mẫu các vết ngăn xếp cấp người dùng tại 49 Hertz, cho PID 189:
`bpftrace -e 'profile:hz:49 /pid == 189/ { @[ustack] = count(); }'`

**Memory (Bộ nhớ)**
Đếm việc mở rộng vùng heap của tiến trình (brk()) theo đường dẫn mã:
`bpftrace -e 'tracepoint:syscalls:sys_enter_brk { @[ustack, comm] = count(); }'`

Đếm lỗi trang người dùng (user page faults) theo vết ngăn xếp cấp người dùng:
`bpftrace -e 'tracepoint:exceptions:page_fault_user { @[ustack, comm] = count(); }'`

Đếm các đợt quét vmscan theo tracepoint:
`bpftrace -e 'tracepoint:vmscan:* { @[probe]++; }'`

**File Systems (Hệ thống tập tin)**
Truy vết các tệp được mở qua openat(2) với tên tiến trình:
`bpftrace -e 't:syscalls:sys_enter_openat { printf("%s %s
", comm, str(args->filename)); }'`

Hiển thị phân phối các byte đọc của syscall read(2) (và các lỗi):
`bpftrace -e 'tracepoint:syscalls:sys_exit_read { @ = hist(args->ret); }'`

Đếm các lệnh gọi VFS:
`bpftrace -e 'kprobe:vfs_* { @[probe] = count(); }'`

Đếm các lệnh gọi ext4 tracepoint:
`bpftrace -e 'tracepoint:ext4:* { @[probe] = count(); }'`

**Disk (Đĩa)**
Tóm tắt kích thước I/O khối dưới dạng một biểu đồ histogram:
`bpftrace -e 't:block:block_rq_issue { @bytes = hist(args->bytes); }'`

Đếm các vết ngăn xếp yêu cầu đĩa I/O:
`bpftrace -e 't:block:block_rq_issue { @[ustack] = count(); }'`

Đếm các cờ loại I/O khối:
`bpftrace -e 't:block:block_rq_issue { @[args->rwbs] = count(); }'`

**Networking (Mạng)**
Đếm các socket accept(2) theo PID và tên tiến trình:
`bpftrace -e 't:syscalls:sys_enter_accept* { @[pid, comm] = count(); }'`

Đếm số byte gửi/nhận của socket theo PID on-CPU và tên tiến trình:
`bpftrace -e 'kr:sock_sendmsg,kr:sock_recvmsg /retval > 0/ { @[pid, comm] = sum(retval); }'`

Gửi byte TCP dưới dạng một biểu đồ histogram:
`bpftrace -e 'k:tcp_sendmsg { @send_bytes = hist(arg2); }'`

Nhận byte TCP dưới dạng một biểu đồ histogram:
`bpftrace -e 'kr:tcp_recvmsg /retval >= 0/ { @recv_bytes = hist(retval); }'`

Gửi byte UDP dưới dạng một biểu đồ histogram:
`bpftrace -e 'k:udp_sendmsg { @send_bytes = hist(arg2); }'`

**Applications (Các ứng dụng)**
Tổng số byte malloc() được yêu cầu theo vết ngăn xếp cấp người dùng (chi phí cao):
`bpftrace -e 'u:/lib/x86_64-linux-gnu/libc-2.27.so:malloc { @[ustack(5)] = sum(arg0); }'`

Truy vết các tín hiệu kill() hiển thị tên tiến trình gửi, PID mục tiêu, và số tín hiệu:
`bpftrace -e 't:syscalls:sys_enter_kill { printf("%s -> %d SIG %d
", comm, args->pid, args->sig); }'`

**Kernel**
Đếm các lệnh gọi hệ thống theo hàm syscall:
`bpftrace -e 'tracepoint:raw_syscalls:sys_enter { @[ksym(*(kaddr("sys_call_table") + args->id * 8))] = count(); }'`

Đếm các lần gọi hàm kernel bắt đầu bằng “attach”:
`bpftrace -e 'kprobe:attach* { @[probe] = count(); }'`

Tần suất đối số thứ ba tới vfs_write() (kích thước):
`bpftrace -e 'kprobe:vfs_write { @[arg2] = count(); }'`

Thời gian hàm kernel vfs_read() và tóm tắt dưới dạng một biểu đồ histogram:
`bpftrace -e 'k:vfs_read { @ts[tid] = nsecs; } kr:vfs_read /@ts[tid]/ { @ = hist(nsecs - @ts[tid]); delete(@ts[tid]); }'`

Đếm các vết ngăn xếp switch ngữ cảnh (context switch stack traces):
`bpftrace -e 't:sched:sched_switch { @[kstack, ustack, comm] = count(); }'`

Lấy mẫu các ngăn xếp ở cấp độ kernel tại 99 Hertz, loại trừ rảnh rỗi:
`bpftrace -e 'profile:hz:99 /pid/ { @[kstack] = count(); }'`

### 15.2.4 Lập trình
Phần này cung cấp một hướng dẫn ngắn gọn để sử dụng bpftrace và ngôn ngữ bpftrace. Định dạng của ngôn ngữ này được lấy cảm hứng từ awk [Aho 78][Aho 88], thứ đã bao quát ngôn ngữ đó trong sáu trang. Ngôn ngữ bpftrace tự nó được lấy cảm hứng từ cả awk và C, và bởi các trình truy vết bao gồm DTrace và SystemTap.

Sau đây là một ví dụ về lập trình bpftrace: Nó đo lường thời gian trong hàm vfs_read() kernel và in thời gian đó, tính bằng micro giây, dưới dạng một biểu đồ histogram.

```c
#!/usr/local/bin/bpftrace

// chương trình này tính thời gian vfs_read()

kprobe:vfs_read
{
          @start[tid] = nsecs;
}

kretprobe:vfs_read
/@start[tid]/
{
          $duration_us = (nsecs - @start[tid]) / 1000;
          @us = hist($duration_us);
          delete(@start[tid]);
}
```

Các phần sau đây giải thích các thành phần của công cụ này, và có thể được coi như một bài hướng dẫn. Mục 15.2.5, Tham chiếu, là một bản tóm tắt hướng dẫn tham chiếu bao gồm các loại thăm dò (probe types), các bài kiểm tra, các toán tử, các biến, các hàm, và các loại bản đồ (map types).

**1. Cách sử dụng (Usage)**
Lệnh:
`bpftrace -e program`

sẽ thực thi chương trình, instrument bất kỳ sự kiện nào mà nó định nghĩa. Chương trình sẽ chạy cho đến khi nhấn Ctrl-C, hoặc cho đến khi nó gọi exit() một cách rõ ràng. Một đối số bpftrace được chạy dưới dạng -e được gọi là một *one-liner*. Ngoài ra, chương trình có thể được lưu vào một tệp và thực thi bằng cách sử dụng:
`bpftrace file.bt`

Phần mở rộng .bt là không cần thiết, nhưng hữu ích cho việc nhận dạng sau này. Bằng cách đặt một dòng trình thông dịch ở đầu tệp:²
`#!/usr/local/bin/bpftrace`

tệp có thể được làm thành tệp thực thi (chmod a+x file.bt) và chạy giống như bất kỳ chương trình nào khác:
`./file.bt`

bpftrace phải được thực thi bởi người dùng root (siêu người dùng).³ Đối với một số môi trường, shell gốc có thể được sử dụng để thực thi chương trình trực tiếp, trong khi những môi trường khác có thể có một sự ưu tiên cho việc chạy các lệnh có đặc quyền qua sudo(1):
`sudo ./file.bt`

---
² Một số người thích sử dụng #!/usr/bin/env bpftrace, sao cho bpftrace có thể được tìm thấy từ $PATH. Tuy nhiên, env(1) đi kèm với nhiều vấn đề khác nhau, và việc sử dụng nó trong các dự án khác đã bị hoàn tác (reverted).
³ bpftrace kiểm tra UID 0; một bản cập nhật trong tương lai có thể kiểm tra các đặc quyền cụ thể.

---

**2. Cấu trúc Chương trình (Program Structure)**
Một chương trình bpftrace là một chuỗi các thăm dò (probes) với các hành động liên kết:
`probes { actions }`
`probes { actions }`
`...`

Khi các thăm dò được kích hoạt, hành động liên kết sẽ được thực thi. Một biểu thức bộ lọc tùy chọn có thể được bao gồm trước hành động:
`probes /filter/ { actions }`

Cấu trúc này giống như cấu trúc chương trình awk(1):
`/pattern/ { actions }`

Lập trình awk(1) cũng tương tự như lập trình bpftrace: Nhiều khối hành động có thể được định nghĩa, và chúng có thể thực thi theo bất kỳ thứ tự nào, được kích hoạt khi mẫu, hoặc sự kiện thăm dò + biểu thức bộ lọc của họ là đúng.

**3. Lời bình luận (Comments)**
Đối với các tập tin chương trình bpftrace, các lời bình luận dòng đơn có thể được thêm vào với tiền tố “//”:
`// đây là một lời bình luận`

Những lời bình luận này sẽ không được thực thi. Các lời bình luận đa dòng sử dụng cùng định dạng như trong C:
```c
/*
 * Đây là một
 * lời bình luận đa dòng.
 */
```
Cú pháp này cũng có thể được sử dụng cho các lời bình luận một phần dòng (ví dụ: /* lời bình luận */).

**4. Định dạng Thăm dò (Probe Format)**
Một thăm dò bắt đầu với một tên loại thăm dò và sau đó là một phân cấp các mã định danh được phân tách bằng dấu hai chấm:
`type:identifier1[:identifier2[...]]`

Phân cấp này được định nghĩa bởi loại thăm dò. Cân nhắc hai ví dụ sau:
`kprobe:vfs_read`
`uprobe:/bin/bash:readline`

Loại thăm dò kprobe instrument các lệnh gọi hàm kernel, và chỉ cần một mã định danh: tên hàm kernel. Loại thăm dò uprobe instrument các lệnh gọi hàm cấp người dùng, và cần cả đường dẫn tới file nhị phân và tên hàm.

Nhiều thăm dò có thể được chỉ định với các dấu phẩy phân tách để thực thi cùng các hành động. Ví dụ:
`probe1,probe2,... { actions }`

Có hai loại thăm dò đặc biệt không yêu cầu thêm mã định danh: BEGIN và END kích hoạt tại thời điểm bắt đầu và khi kết thúc chương trình bpftrace (giống như awk(1)). Ví dụ, để in một thông điệp thông tin khi việc truy vết bắt đầu:
`BEGIN { printf("Tracing. Hit Ctrl-C to end.
"); }`

Để tìm hiểu thêm về các loại thăm dò và cách sử dụng chúng, xem Mục 15.2.5, Tham chiếu, dưới tiêu đề 1. Probe Types.

**5. Các ký tự đại diện Thăm dò (Probe Wildcards)**
Một số loại thăm dò chấp nhận các ký tự đại diện. Thăm dò:
`kprobe:vfs_*`

sẽ instrument tất cả các kprobes (các hàm kernel) bắt đầu với “vfs_”.

Việc instrument quá nhiều thăm dò có thể tiêu tốn chi phí hiệu năng không cần thiết. Để tránh việc chạm tới điều này một cách vô ý, bpftrace có một số lượng tối đa các thăm dò có thể tinh chỉnh được mà nó sẽ bật, được thiết lập qua biến môi trường BPFTRACE_MAX_PROBES (nó hiện mặc định là 512).⁴

Bạn có thể kiểm tra các ký tự đại diện của mình trước khi sử dụng chúng bằng cách chạy `bpftrace -l` để liệt kê các thăm dò khớp:

```bash
# bpftrace -l 'kprobe:vfs_*'
kprobe:vfs_fallocate
kprobe:vfs_truncate
kprobe:vfs_open
kprobe:vfs_setpos
kprobe:vfs_llseek
[...]
# bpftrace -l 'kprobe:vfs_*' | wc -l
56
```

Việc này đã khớp với 56 thăm dò. Tên thăm dò nằm trong ngoặc kép để ngăn chặn việc mở rộng shell không mong muốn.

---
⁴ Hơn 512 hiện tại làm cho bpftrace khởi động và tắt máy chậm, vì nó instrument từng cái một. Quá trình làm việc với kernel trong tương lai được lên kế hoạch để thực hiện việc instrument thăm dò theo đợt. Tại thời điểm đó, giới hạn này có thể được tăng lên đáng kể, hoặc thậm chí được loại bỏ.

---

**6. Các bộ lọc (Filters)**
Các bộ lọc là các biểu thức Boolean điều hướng liệu một hành động có được thực thi hay không. Bộ lọc:
`/pid == 123/`

sẽ chỉ thực thi hành động nếu biến tích hợp pid (process ID) bằng 123.

Nếu một phép kiểm tra không được chỉ định:
`/pid/`

bộ lọc sẽ kiểm tra xem nội dung là khác không (/pid/ là giống như /pid != 0/). Các bộ lọc có thể được kết hợp với các toán tử Boolean, chẳng hạn như logic AND (&&). Ví dụ:
`/pid > 100 && pid < 1000/`

Điều này yêu cầu cả hai biểu thức phải đánh giá là “đúng.”

**7. Các hành động (Actions)**
Một hành động có thể là một câu lệnh đơn lẻ hoặc nhiều câu lệnh được phân tách bằng dấu chấm phẩy:
`{ action one; action two; action three }`

Câu lệnh cuối cùng cũng có thể có dấu chấm phẩy được nối thêm. Các câu lệnh được viết bằng ngôn ngữ bpftrace, thứ tương tự như ngôn ngữ C, và có thể thao tác các biến và thực thi các hàm bpftrace. Ví dụ, hành động:
`{ $x = 42; printf("$x is %d
", $x); }`

thiết lập một biến, $x, thành 42, và sau đó in nó ra bằng cách sử dụng printf(). Để biết bản tóm tắt các lần gọi hàm có sẵn khác, xem Mục 15.2.5, Tham chiếu, dưới các tiêu đề 4. Functions và 5. Map Functions.

**8. Hello, World!**
Bây giờ bạn nên hiểu chương trình cơ bản sau đây, thứ in “Hello, World!” khi bpftrace bắt đầu chạy:

```bash
# bpftrace -e 'BEGIN { printf("Hello, World!
"); }'
Attaching 1 probe...
Hello, World!
^C
```

Dưới dạng một tệp, nó có thể được định dạng là:

```c
#!/usr/local/bin/bpftrace

BEGIN
{
          printf("Hello, World!
");
}
```

Việc trải rộng nhiều dòng với một khối hành động được thụt lề là không cần thiết, nhưng nó cải thiện khả năng đọc.

**9. Các hàm (Functions)**
Ngoài printf() cho việc in kết quả được định dạng, các hàm tích hợp bao gồm:
- **exit():** Thoát khỏi bpftrace
- **str(char *):** Trả về một chuỗi từ một con trỏ
- **system(format[, arguments ...]):** Chạy một lệnh tại shell

Hành động:
`printf("got: %llx %s
", $x, str($x)); exit();`

sẽ in biến $x dưới dạng một số nguyên thập lục phân, và sau đó coi nó như một mảng ký tự kết thúc bằng NULL (char *) và in nó ra dưới dạng một chuỗi, và sau đó thoát.

**10. Các biến (Variables)**
Có ba loại biến: tích hợp sẵn (built-ins), nháp (scratch), và bản đồ (maps).

**Biến tích hợp (Built-in variables)** là các nguồn thông tin được định nghĩa trước và được cung cấp bởi bpftrace, và thường chỉ được đọc. Chúng bao gồm pid cho ID tiến trình, comm cho tên tiến trình, nsecs cho một dấu thời gian tính bằng nano giây, và curtask cho địa chỉ của cấu trúc task_struct luồng hiện tại.

**Biến nháp (Scratch variables)** có thể được sử dụng cho các tính toán tạm thời và có tiền tố "$". Tên và loại của chúng được thiết lập tại lần gán đầu tiên của chúng. Các câu lệnh:
```c
$x = 1;
$y = "hello";
$z = (struct task_struct *)curtask;
```
khai báo $x là một số nguyên, $y là một chuỗi, và $z là một con trỏ tới một cấu trúc task_struct. Những biến này chỉ có thể được sử dụng trong khối hành động mà chúng đã được gán. Nếu các biến được tham chiếu mà không có sự gán, bpftrace in ra một lỗi (thứ có thể giúp bạn phát hiện các lỗi đánh máy).

**Biến bản đồ (Map variables)** sử dụng đối tượng lưu trữ bản đồ BPF và có tiền tố "@". Chúng có thể được sử dụng cho lưu trữ toàn cầu, truyền dữ liệu giữa các hành động. Chương trình:
```c
probe1 { @a = 1; }
probe2 { $x = @a; }
```
gán 1 cho @a khi probe1 được kích hoạt, sau đó gán @a cho $x khi probe2 được kích hoạt. Nếu probe1 kích hoạt trước, thì $x sẽ được thiết lập thành 1; nếu không thì là 0 (chưa khởi tạo).

Một khóa có thể được cung cấp với một hoặc nhiều thành phần, sử dụng các bản đồ như một bảng băm (mảng kết hợp). Câu lệnh:
`@start[tid] = nsecs;`

thường xuyên được sử dụng: nsecs tích hợp sẵn được gán cho một bản đồ mang tên @start và được gắn khóa trên tid, ID luồng hiện tại. Điều này cho phép các luồng lưu trữ các dấu thời gian tùy chỉnh thứ sẽ không bị ghi đè bởi các luồng khác.
`@path[pid, $fd] = str(arg0);`

là một ví dụ về một bản đồ đa khóa, sử dụng cả pid tích hợp sẵn và biến $fd làm các khóa.

**11. Các hàm Bản đồ (Map Functions)**
Bản đồ có thể được gán cho các hàm đặc biệt. Những hàm này lưu trữ và in dữ liệu theo các cách tùy chỉnh. Sự gán:
`@x = count();`

đếm các sự kiện, và khi được in, nó sẽ in số lượng. Điều này sử dụng một bản đồ cho mỗi CPU, và @x trở thành một đối tượng đặc biệt của loại count. Câu lệnh sau đây cũng đếm các sự kiện:
`@x++;`

Tuy nhiên, điều này sử dụng một bản đồ CPU toàn cầu, thay vì một bản đồ cho mỗi CPU, để cung cấp @x như một số nguyên. Loại số nguyên toàn cầu này đôi khi cần thiết cho một số chương trình yêu cầu một số nguyên chứ không phải là một loại bản đồ, nhưng hãy lưu ý rằng có thể có một sai số nhỏ do các đợt cập nhật đồng thời.

Sự gán:
`@y = sum($x);`

tổng hợp biến $x, và khi được in sẽ in ra tổng đó. Sự gán:
`@z = hist($x);`

lưu trữ $x trong một biểu đồ histogram lũy thừa của hai, và khi được in sẽ in các số lượng xô và một biểu đồ histogram ASCII.

Một số hàm bản đồ hoạt động trực tiếp trên một bản đồ. Ví dụ:
`print(@x);`

sẽ in bản đồ @x. Điều này có thể được sử dụng, chẳng hạn, để in nội dung bản đồ theo một sự kiện khoảng thời gian (interval event). Điều này không được sử dụng thường xuyên vì, để thuận tiện, tất cả các bản đồ được tự động in khi bpftrace kết thúc.⁵

Một số hàm bản đồ hoạt động trên một khóa bản đồ. Ví dụ:
`delete(@start[tid]);`

xóa cặp khóa-giá trị khỏi bản đồ @start nơi khóa là tid.

**12. Định thời vfs_read()**
Bây giờ bạn đã biết cú pháp cần thiết để hiểu một ví dụ thực tế và phức tạp hơn. Chương trình này, vfsread.bt, định thời cho hàm kernel vfs_read() và tóm tắt dưới dạng một biểu đồ histogram thời lượng của nó tính theo micro giây (us):

```c
#!/usr/local/bin/bpftrace

// chương trình này tính thời gian vfs_read()

kprobe:vfs_read
{
          @start[tid] = nsecs;
}

kretprobe:vfs_read
/@start[tid]/
{
          $duration_us = (nsecs - @start[tid]) / 1000;
          @us = hist($duration_us);
          delete(@start[tid]);
}
```

Thao tác này tính toán thời lượng của hàm kernel vfs_read() bằng cách instrument sự khởi đầu của nó sử dụng một kprobe và lưu trữ một dấu thời gian trong một bản đồ băm được gắn khóa trên ID luồng, và sau đó instrument sự kết thúc của nó bằng cách sử dụng một kretprobe và tính toán giá trị delta: bây giờ - bắt đầu. Một bộ lọc được sử dụng để đảm bảo rằng thời gian bắt đầu đã được ghi lại; nếu không, phép tính delta sẽ trở nên giả mạo đối với các lệnh gọi vfs_read() đang diễn ra khi việc truy vết bắt đầu, vì kết thúc được nhìn thấy nhưng không phải là bắt đầu (delta sẽ trở thành: bây giờ - 0).

Kết quả mẫu:

```bash
# bpftrace vfsread.bt
Attaching 2 probes...
^C

@us:
[0]                   23 |@                                                   |
[1]                  138 |@@@@@@@@@                                           |
[2, 4)               538 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      |
[4, 8)               744 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[8, 16)              641 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       |
[16, 32)             122 |@@@@@@@@@                                           |
[32, 64)              13 |                                                    |
[64, 128)             17 |@                                                   |
[128, 256)             2 |                                                    |
[256, 512)             0 |                                                    |
[512, 1K)              1 |                                                    |
```

Chương trình đã chạy cho đến khi nhấn Ctrl-C; sau đó nó in kết quả này và kết thúc. Bản đồ histogram được đặt tên là “us” như một cách để bao gồm các đơn vị trong kết quả, vì tên bản đồ được in ra. Bằng cách đặt cho các bản đồ những cái tên có ý nghĩa như “bytes” và “latency_ns”, bạn có thể chú giải kết quả và làm cho nó tự giải thích.

Script này có thể được tùy chỉnh khi cần thiết. Cân nhắc việc thay đổi dòng gán hist() thành:
`@us[pid, comm] = hist($duration_us);`

Điều này lưu trữ một biểu đồ histogram cho mỗi cặp ID tiến trình và tên tiến trình. Với các công cụ hệ thống truyền thống, chẳng hạn như iostat(1) và vmstat(1), kết quả là cố định và không thể được tùy chỉnh một cách dễ dàng. Nhưng với bpftrace, các chỉ số bạn thấy có thể được chia nhỏ thêm thành các phần và được tăng cường với các chỉ số từ các thăm dò khác cho đến khi bạn có được những câu trả lời bạn cần.

Xem Chương 8, Hệ thống tập tin, Mục 8.6.15, dưới tiêu đề VFS Latency Tracing, cho một ví dụ mở rộng chia nhỏ độ trễ vfs_read() theo loại: file system, socket, v.v.

---
⁵ Cũng có ít chi phí hơn trong việc in các bản đồ khi bpftrace kết thúc, vì tại thời điểm chạy các bản đồ đang gặp phải các đợt cập nhật đồng thời, thứ có thể làm chậm việc duyệt qua bản đồ.

---

### 15.2.5 Reference
Sau đây là một bản tóm tắt các thành phần chính của lập trình bpftrace: các loại thăm dò, kiểm soát luồng, các biến, các hàm, và các hàm bản đồ.

**1. Probe Types (Các loại Thăm dò)**
Bảng 15.4 liệt kê các loại thăm dò có sẵn. Nhiều trong số này cũng có một bí danh viết tắt, thứ có thể giúp tạo ra các lệnh một dòng ngắn hơn.

Bảng 15.4 các loại thăm dò bpftrace
| Loại | Viết tắt | Mô tả |
| --- | --- | --- |
| tracepoint | t | Các điểm instrumentation tĩnh của kernel |
| usdt | U | Truy vết được định nghĩa tĩnh cấp người dùng |
| kprobe | k | Instrumentation động hàm kernel |
| kretprobe | kr | Instrumentation trả về của hàm kernel động |
| kfunc | f | Instrumentation hàm kernel động (dựa trên BPF) |
| kretfunc | fr | Instrumentation trả về của hàm kernel động (dựa trên BPF) |
| uprobe | u | Instrumentation động hàm cấp người dùng |
| uretprobe | ur | Instrumentation trả về của hàm cấp người dùng động |
| software | s | Các sự kiện dựa trên phần mềm kernel |
| hardware | h | Các sự kiện dựa trên bộ đếm phần cứng |
| watchpoint | w | Instrumentation điểm dừng bộ nhớ |
| profile | p | Lấy mẫu theo thời gian trên tất cả các CPUs |
| interval | i | Báo cáo theo thời gian (từ một CPU) |
| BEGIN | | Bắt đầu bpftrace |
| END | | Kết thúc bpftrace |

Hầu hết các loại thăm dò này là các giao diện với các công nghệ kernel hiện có. Chương 4 giải thích cách thức các công nghệ này hoạt động: kprobes, uprobes, tracepoints, USDT, và PMCs (được sử dụng bởi loại thăm dò phần cứng). Loại thăm dò kfunc/kretfunc là một giao diện chi phí thấp mới dựa trên eBPF trampolines và BTF.

Một số thăm dò có thể kích hoạt thường xuyên, chẳng hạn như cho các sự kiện trình lập lịch, cấp phát bộ nhớ, và các gói tin mạng. Để giảm chi phí, hãy cố gắng giải quyết các vấn đề của bạn bằng cách sử dụng các sự kiện ít thường xuyên hơn bất cứ khi nào có thể. Nếu bạn không chắc chắn về chi phí thăm dò, bạn có thể đo lường nó bằng bpftrace. Ví dụ, đếm các lần gọi kprobe vfs_read() chỉ trong một giây:

`# bpftrace -e 'k:vfs_read { @ = count(); } interval:s:1 { exit(); }'`

Tôi đã chọn một thời lượng ngắn để giảm thiểu chi phí, trong trường hợp nó là đáng kể. Những gì tôi sẽ coi là tần suất cao hay thấp phụ thuộc vào tốc độ CPU của bạn, số lượng CPU, và các chi phí của việc instrumentation thăm dò. Theo quy tắc chung cho các máy chủ ngày nay, tôi lo ngại việc có ít hơn 100k sự kiện kprobe hoặc tracepoint mỗi giây là tần suất thấp.

**Probe Arguments (Các đối số Thăm dò)**
Mỗi loại thăm dò cung cấp các loại đối số khác nhau cho ngữ cảnh sâu hơn về các sự kiện. Ví dụ, các tracepoints cung cấp các trường từ tệp format trong /sys hoặc từ bpftrace sử dụng -lv:

`bpftrace -e 'tracepoint:syscalls:sys_enter_read { @read_bytes = hist(args->count); }'`

Các trường này có thể được liệt kê từ tệp format trong /sys hoặc từ bpftrace bằng cách sử dụng -lv:

```bash
# bpftrace -lv 'tracepoint:syscalls:sys_enter_read'
tracepoint:syscalls:sys_enter_read
    int __syscall_nr;
    unsigned int fd;
    char * buf;
    size_t count;
```

Xem “bpftrace Reference Guide” trực tuyến để biết mô tả về từng loại thăm dò và các đối số của nó [Iovisor 20c].

**2. Flow Control (Kiểm soát Luồng)**
Có ba loại bài kiểm tra trong bpftrace: filters (bộ lọc), ternary operators (toán tử ba ngôi), và if statements (câu lệnh if). Những bài kiểm tra này thay đổi có điều kiện luồng của chương trình dựa trên các biểu thức Boolean, thứ hỗ trợ những gì được trình bày trong Bảng 15.5.

Bảng 15.5 các biểu thức Boolean của bpftrace
| Biểu thức | Mô tả |
| --- | --- |
| == | Bằng với |
| != | Không bằng với |
| > | Lớn hơn |
| < | Nhỏ hơn |
| >= | Lớn hơn hoặc bằng với |
| <= | Nhỏ hơn hoặc bằng với |
| && | Và |
| || | Hoặc |

Các biểu thức có thể được nhóm lại sử dụng các dấu ngoặc đơn.

**Filter (Bộ lọc)**
Đã được giới thiệu sớm hơn, những thứ này điều hướng liệu một hành động có được thực hiện hay không. Định dạng:
`probe /filter/ { action }`

Các toán tử Boolean có thể được sử dụng. Bộ lọc /pid == 123/ chỉ thực thi hành động nếu pid tích hợp bằng 123.
Nếu một bài kiểm tra không được chỉ định:
`/pid/`
trình truy vết sẽ kiểm tra xem nội dung là khác không (/pid/ là giống như /pid != 0/). Các bộ lọc có thể được kết hợp với các toán tử Boolean, chẳng hạn như logic AND (&&). Ví dụ:
`/pid > 100 && pid < 1000/`
Điều này yêu cầu cả hai biểu thức phải đánh giá là “đúng.”

**Ternary Operators (Toán tử Ba ngôi)**
Một toán tử ba ngôi là một toán tử ba thành phần bao gồm một bài kiểm tra và hai kết quả. Định dạng:
`test ? true_statement : false_statement`

Như một ví dụ, bạn có thể sử dụng một toán tử ba ngôi để tìm giá trị tuyệt đối của $x:
`$abs = $x >= 0 ? $x : - $x;`

**If Statements (Câu lệnh If)**
Các câu lệnh if có cú pháp sau:
`if (test) { true_statements }`
`if (test) { true_statements } else { false_statements }`

Một trường hợp sử dụng là với các chương trình thực hiện các hành động khác nhau trên IPv4 so với IPv6 (để đơn giản, điều này bỏ qua các họ khác ngoài IPv4 và IPv6):
```c
if ($inet_family == $AF_INET) {
    // IPv4
    ...
} else {
    // giả định IPv6
    ...
}
```
Các câu lệnh `else if` được hỗ trợ kể từ bpftrace v0.10.0.⁶

**Loops (Vòng lặp)**
bpftrace hỗ trợ các vòng lặp được unrolled (unrolled loops) bằng cách sử dụng unroll(). Đối với Linux 5.3 và các kernels sau này, các vòng lặp while() cũng được hỗ trợ:⁷
```c
while (test) {
    statements
}
```
Điều này đã sử dụng vòng lặp BPF được thêm vào trong Linux 5.3.

---
⁶ Cảm ơn Daniel Xu (PR#1211).
⁷ Cảm ơn Bas Smit vì đã thêm logic bpftrace (PR#1066).

---

**Operators (Toán tử)**
Một phần trước đó đã liệt kê các toán tử Boolean để sử dụng trong các bài kiểm tra. bpftrace cũng hỗ trợ các toán tử được trình bày trong Bảng 15.6.

Bảng 15.6 Các toán tử của bpftrace
| Toán tử | Mô tả |
| --- | --- |
| = | Gán (Assignment) |
| +, -, *, / | Cộng, trừ, nhân, chia (chỉ số nguyên) |
| ++, -- | Tăng tự động, giảm tự động |
| &, |, ^ | bitwise AND, bitwise OR, bitwise XOR |
| ! | Logic NOT |
| <<, >> | Dịch bit trái, dịch bit phải |
| +=, -=, *=, /=, %=, &=, ^=, <<=, >>= | Các toán tử hỗn hợp |

Những toán tử này được mô hình hóa theo các toán tử tương tự trong ngôn ngữ lập trình C.

**3. Variables (Các biến)**
Các biến tích hợp được cung cấp bởi bpftrace thường dành cho việc truy cập thông tin chỉ đọc. Các biến tích hợp quan trọng được liệt kê trong Bảng 15.7.

Bảng 15.7 Các biến tích hợp bpftrace được lựa chọn
| Biến tích hợp | Loại | Mô tả |
| --- | --- | --- |
| pid | integer | ID tiến trình (kernel tgid) |
| tid | integer | ID luồng (kernel pid) |
| uid | integer | User ID |
| username | string | Tên người dùng |
| nsecs | integer | Dấu thời gian, tính bằng nano giây |
| elapsed | integer | Dấu thời gian, tính bằng nano giây, kể từ khi bpftrace khởi tạo |
| cpu | integer | ID bộ xử lý |
| comm | string | Tên tiến trình |
| kstack | string | Vết ngăn xếp kernel |
| ustack | string | Vết ngăn xếp cấp người dùng |
| arg0, ..., argN | integer | Các đối số cho một số loại thăm dò |
| args | struct | Các đối số cho một số loại thăm dò |
| sarg0, ..., sargN | integer | Các đối số dựa trên ngăn xếp cho một số loại thăm dò |
| retval | integer | Giá trị trả về cho một số loại thăm dò |
| func | string | Tên của hàm được truy vết |
| probe | string | Tên đầy đủ của thăm dò hiện tại |
| curtask | struct/integer | Kernel task_struct (hoặc là một task_struct hoặc một số nguyên 64-bit không dấu, tùy thuộc vào tính sẵn có của thông tin loại) |
| cgroup | integer | ID cgroup v2 mặc định cho tiến trình hiện tại (để so sánh với cgroupid()) |
| $1, ..., $N | int, char * | Các tham số vị trí cho chương trình bpftrace |

Tất cả các số nguyên hiện nay là uint64. Những biến này đều đề cập đến luồng, tiến trình, và CPU hiện tại khi thăm dò kích hoạt.
Các biến tích hợp khác nhau đã được trình diễn sớm hơn trong chương này: retval, comm, tid, và nsecs. Xem "bpftrace Reference Guide" trực tuyến để biết danh sách đầy đủ và cập nhật các biến tích hợp [Iovisor 20c].

**4. Functions (Các hàm)**
Bảng 15.8 liệt kê các hàm tích hợp được lựa chọn cho các tác vụ khác nhau. Một số trong những hàm này đã được sử dụng trong các ví dụ trước đó, chẳng hạn như printf().

Bảng 15.8 các hàm tích hợp bpftrace được lựa chọn
| Hàm | Mô tả |
| --- | --- |
| printf(char *fmt [, ...]) | In được định dạng |
| time(char *fmt) | In thời gian được định dạng |
| join(char *arr[]) | In mảng các chuỗi, nối với nhau bởi một ký tự khoảng trắng |
| str(char *s [, int len]) | Trả về chuỗi từ con trỏ s, với một chiều dài tùy chọn |
| buf(void *d [, int length]) | Trả về một phiên bản chuỗi thập lục phân của con trỏ dữ liệu |
| strncmp(char *s1, char *s2, int length) | So sánh hai chuỗi lên tới độ dài ký tự |
| sizeof(expression) | Trả về kích thước của biểu thức hoặc loại dữ liệu |
| kstack([int limit]) | Trả về một ngăn xếp kernel sâu tới limit khung hình |
| ustack([int limit]) | Trả về một ngăn xếp người dùng sâu tới limit khung hình |
| ksym(void *p) | Phân giải địa chỉ kernel và trả về biểu tượng kernel |
| usym(void *p) | Phân giải địa chỉ không gian người dùng và trả về biểu tượng người dùng |
| kaddr(char *name) | Phân giải tên biểu tượng kernel thành một địa chỉ |
| uaddr(char *name) | Phân giải tên biểu tượng không gian người dùng thành một địa chỉ |
| reg(char *name) | Trả về giá trị được lưu trữ trong thanh ghi đã nêu |
| ntop([int af,] int addr) | Trả về một biểu diễn chuỗi của một địa chỉ IPv4/IPv6. |
| cgroupid(char *path) | Trả về một ID cgroup cho đường dẫn đã cho (/sys/fs/cgroup/...) |
| system(char *fmt [, ...]) | Thực thi một lệnh shell |
| cat(char *filename) | In nội dung của một tệp |
| signal(char[] sig | u32 sig) | Gửi một tín hiệu tới tác vụ hiện tại (ví dụ: SIGTERM) |
| override(u64 rc) | Ghi đè một giá trị trả về của kprobe⁸ |
| exit() | Thoát khỏi bpftrace |

Một số hàm này là bất đồng bộ: Kernel xếp hàng sự kiện, và một thời gian ngắn sau đó nó được xử lý trong không gian người dùng. Các hàm không gian người dùng là printf(), time(), cat(), join(), và system(). Các hàm kstack(), ustack(), ksym(), và usym() ghi lại các địa chỉ một cách đồng bộ, nhưng việc dịch biểu tượng diễn ra một cách bất đồng bộ.
Như một ví dụ, phần sau đây sử dụng cả hai hàm printf() và str() để hiển thị tên tệp của các syscall openat(2):

```bash
# bpftrace -e 't:syscalls:sys_enter_open { printf("%s %s
", comm, str(args->filename)); }'
Attaching 1 probe...
top /etc/ld.so.cache
top /lib/x86_64-linux-gnu/libprocps.so.7
top /lib/x86_64-linux-gnu/libtinfo.so.6
top /lib/x86_64-linux-gnu/libc.so.6
[...]
```

Xem “bpftrace Reference Guide” trực tuyến để biết danh sách đầy đủ và cập nhật các hàm [Iovisor 20c].

---
⁸ CẢNH BÁO: Chỉ sử dụng cái này nếu bạn biết bạn đang làm gì: một sai lầm nhỏ có thể gây ra kernel panic hoặc làm hỏng kernel.

---

**5. Map Functions (Các hàm Bản đồ)**
Bản đồ là các đối tượng lưu trữ bảng băm từ BPF có thể được sử dụng cho các mục đích khác nhau—ví dụ, như các bảng băm để lưu trữ các cặp khóa/giá trị hoặc cho các tóm tắt thống kê. Có các hàm tích hợp sẵn cho việc gán và thao tác bản đồ, chủ yếu cho việc hỗ trợ các bản đồ tóm tắt thống kê. Các hàm bản đồ quan trọng nhất được liệt kê trong Bảng 15.9.

Bảng 15.9 Các hàm bản đồ bpftrace được lựa chọn
| Hàm | Mô tả |
| --- | --- |
| count() | Đếm các lần xuất hiện |
| sum(int n) | Tính tổng giá trị |
| avg(int n) | Lấy trung bình giá trị |
| min(int n) | Ghi lại giá trị tối thiểu |
| max(int n) | Ghi lại giá trị tối đa |
| stats(int n) | Trả về số lượng, trung bình, và tổng |
| hist(int n) | In một biểu đồ histogram lũy thừa của hai các giá trị |
| lhist(int n, const int min, const int max, int step) | In một biểu đồ histogram tuyến tính của các giá trị |
| delete(@m[key]) | Xóa cặp khóa/giá trị bản đồ |
| print(@m [, top [, div]]) | In bản đồ, với các giới hạn top tùy chọn và một ước số |
| clear(@m) | Xóa tất cả các khóa khỏi bản đồ |
| zero(@m) | Thiết lập tất cả các giá trị bản đồ về không |

Một số hàm này là bất đồng bộ: Kernel xếp hàng sự kiện, và một thời gian ngắn sau đó nó được xử lý trong không gian người dùng. Các hành động bất đồng bộ là print(), clear(), và zero(). Hãy ghi nhớ sự trì hoãn này khi bạn đang viết chương trình.
Như một ví dụ khác về việc sử dụng một hàm bản đồ, phần sau đây sử dụng lhist() để tạo ra một biểu đồ histogram tuyến tính của kích thước các lệnh gọi read(2) theo tên tiến trình, với kích thước bước là một sao cho mỗi số file descriptor có thể được nhìn thấy một cách độc lập:

```bash
# bpftrace -e 'tracepoint:syscalls:sys_enter_read {
    @fd[comm] = lhist(args->fd, 0, 100, 1); }'
Attaching 1 probe...
^C
[...]
@fd[sshd]:
[4, 5)                22 |                                                    |
[5, 6)                 0 |                                                    |
[6, 7)                 0 |                                                    |
[7, 8)                 0 |                                                    |
[8, 9)                 0 |                                                    |
[9, 10)                0 |                                                    |
[10, 11)               0 |                                                    |
[11, 12)               0 |                                                    |
[12, 13)            7760 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
```

Kết quả cho thấy trên hệ thống này các tiến trình sshd thông thường đang đọc từ file descriptor 12. Kết quả sử dụng ký hiệu set, nơi “[” có nghĩa là >= và “)” có nghĩa là < (hay gọi là một khoảng đóng bên trái, mở bên phải - bounded left-closed, right-open interval).
Xem "bpftrace Reference Guide" trực tuyến để biết danh sách đầy đủ và cập nhật các hàm bản đồ [Iovisor 20c].

### 15.2.6 Tài liệu
Có nhiều bpftrace hơn trong các chương trước của cuốn sách này, trong các phần sau:
- Chương 5, Các ứng dụng, Mục 5.5.7
- Chương 6, CPUs, Mục 6.6.20
- Chương 7, Bộ nhớ, Mục 7.5.13
- Chương 8, Hệ thống tập tin, Mục 8.6.15
- Chương 9, Đĩa, Mục 9.6.11
- Chương 10, Mạng, Mục 10.6.12

Cũng có các ví dụ bpftrace trong Chương 4, Các Công cụ Quan trắc, và Chương 11, Điện toán đám mây.
Trong kho lưu trữ bpftrace tôi cũng đã tạo ra tài liệu sau đây:
- **Hướng dẫn Tham chiếu (Reference Guide):** docs/reference_guide.md [Iovisor 20c]
- **Hướng dẫn cho các lệnh một dòng (Tutorial docs):** tutorial_one_liners.md [Iovisor 20d]

Để biết thêm về bpftrace, vui lòng tham khảo cuốn sách trước đó của tôi *BPF Performance Tools* [Gregg 19] nơi Chương 5, bpftrace, khám phá ngôn ngữ lập trình với nhiều ví dụ, và các chương sau này cung cấp nhiều chương trình bpftrace hơn cho việc phân tích các mục tiêu khác nhau.
Lưu ý rằng một số khả năng bpftrace được mô tả trong [Gregg 19] dưới dạng "được lên kế hoạch" kể từ đó đã được thêm vào bpftrace và được bao gồm trong chương này. Đó là: các vòng lặp while(), các câu lệnh if-else, signal(), override(), và các sự kiện watchpoint. Các sự kiện bổ sung khác đã được thêm vào bpftrace là loại thăm dò kfunc, buf(), và sizeof(). Hãy kiểm tra các ghi chú phát hành (release notes) trong kho lưu trữ bpftrace cho các sự bổ sung trong tương lai, mặc dù đã có đủ nhiều cái được lên kế hoạch: bpftrace đã có đủ các khả năng cho hơn 120+ công cụ bpftrace đã được công bố.

## 15.3 Tài liệu tham khảo (References)
- [Aho 78] Aho, A. V., Kernighan, B. W., and Weinberger, P. J., “Awk: A Pattern Scanning and Processing Language (Second Edition),” *Unix 7th Edition man pages*, 1978. Online at http://plan9.bell-labs.com/7thEdMan/index.html.
- [Aho 88] Aho, A. V., Kernighan, B. W., and Weinberger, P. J., *The AWK Programming Language*, Addison Wesley, 1988.
- [Gregg 18e] Gregg, B., “YOW! 2018 Cloud Performance Root Cause Analysis at Netflix,” http://www.brendangregg.com/blog/2019-04-26/yow2018-cloud-performance-netflix.html, 2018.
- [Gregg 19] Gregg, B., *BPF Performance Tools: Linux System and Application Observability*, Addison-Wesley, 2019.
- [Gregg 19g] Gregg, B., “BPF Performance Tools (book): Tools,” http://www.brendangregg.com/bpf-performance-tools-book.html#tools, 2019.
- [Iovisor 20a] “bpftrace: High-level Tracing Language for Linux eBPF,” https://github.com/iovisor/bpftrace, last updated 2020.
- [Iovisor 20b] “BCC - Tools for BPF-based Linux IO Analysis, Networking, Monitoring, and More,” https://github.com/iovisor/bcc, last updated 2020.
- [Iovisor 20c] “bpftrace Reference Guide,” https://github.com/iovisor/bpftrace/blob/master/docs/reference_guide.md, last updated 2020.
- [Iovisor 20d] Gregg, B., et al., “The bpftrace One-Liner Tutorial,” https://github.com/iovisor/bpftrace/blob/master/docs/tutorial_one_liners.md, last updated 2020.
