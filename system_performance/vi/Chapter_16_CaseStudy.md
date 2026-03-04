# Chương 16: Nghiên cứu Điển hình (Case Study)

Chương này là một nghiên cứu điển hình về hiệu năng hệ thống: câu chuyện về một vấn đề hiệu năng trong thế giới thực, từ báo cáo ban đầu cho đến khi giải quyết xong. Vấn đề cụ thể này đã xảy ra trong một môi trường điện toán đám mây sản xuất; tôi chọn nó như một ví dụ thường ngày về phân tích hiệu năng hệ thống.

Ý định của tôi trong chương này không phải là để giới thiệu nội dung kỹ thuật mới mà là sử dụng lối kể chuyện để chỉ ra cách các công cụ và phương pháp luận có thể được áp dụng trong thực tế, trong một môi trường làm việc thực sự. Điều này sẽ đặc biệt hữu ích cho những người mới bắt đầu, những người chưa từng làm việc với các vấn đề hiệu năng hệ thống trong thế giới thực, cung cấp một góc nhìn cận cảnh về cách một chuyên gia tiếp cận chúng, đưa ra một bản bình luận về những gì chuyên gia đó có thể đang nghĩ trong quá trình phân tích, và tại sao. Đây không nhất thiết là tài liệu về cách tiếp cận tốt nhất có thể, mà là lý do tại sao một cách tiếp cận đã được chọn.

## 16.1 Một Chiến thắng không giải thích được (An Unexplained Win)
Một microservice tại Netflix đã được kiểm tra trên một nền tảng dựa trên container mới và được tìm thấy là đã giảm độ trễ yêu cầu theo một hệ số từ ba đến bốn lần. Trong khi nền tảng container mang lại nhiều lợi ích, một mức độ cải thiện lớn như vậy là không ngờ tới! Điều này nghe có vẻ quá tốt để có thể là sự thật, và tôi đã được yêu cầu điều tra và giải thích cách nó đã xảy ra.

Cho việc phân tích tôi đã sử dụng nhiều loại công cụ, bao gồm những công cụ dựa trên các bộ đếm, cấu hình tĩnh, PMCs, các sự kiện phần mềm, và truy vết. Tất cả những loại công cụ này đều đóng một vai trò và cung cấp các manh mối ăn khớp với nhau. Vì điều này đã tạo thành một đợt khảo sát rộng về phân tích hiệu năng hệ thống, tôi đã sử dụng nó làm câu chuyện mở đầu cho bài nói chuyện USENIX LISA 2019 của tôi về Hiệu năng Hệ thống [Gregg 19h] và bao gồm nó ở đây như một nghiên cứu điển hình.

### 16.1.1 Tuyên bố Vấn đề (Problem Statement)
Bằng cách nói chuyện với nhóm dịch vụ, tôi đã tìm hiểu được các chi tiết của microservice: Đó là một ứng dụng Java để tính toán các khuyến nghị cho khách hàng, và hiện đang chạy trên các thực thể máy ảo (VM) trong đám mây AWS EC2. Microservice được cấu tạo từ hai thành phần, và một trong số chúng đang được kiểm tra trên một nền tảng container Netflix mới mang tên Titus, cũng chạy trên AWS EC2. Thành phần này có độ trễ yêu cầu từ ba tới bốn giây trên các thực thể VM, thứ trở thành một giây trên các containers: nhanh hơn ba tới bốn lần!

Vấn đề là giải thích sự khác biệt hiệu năng này. Nếu nó đơn giản chỉ là do việc di chuyển container, microservice có thể kỳ vọng một chiến thắng 3-4 lần vĩnh viễn bằng cách di chuyển. Nếu nó là do một số yếu tố khác, sẽ đáng giá để hiểu nó là gì và liệu nó có duy trì vĩnh viễn hay không. Có lẽ nó cũng có thể được áp dụng ở những nơi khác và ở mức độ lớn hơn.

Những gì ngay lập tức xuất hiện trong tâm trí là lợi ích của việc chạy một thành phần của khối lượng công việc một cách cô lập: nó sẽ có khả năng sử dụng toàn bộ các bộ đệm ẩn CPU mà không có sự tranh chấp từ thành phần kia, cải thiện tỷ lệ trúng bộ đệm ẩn và do đó cải thiện hiệu năng. Một dự đoán khác là bursting trên nền tảng container, nơi một container có thể sử dụng các tài nguyên CPU rảnh rỗi từ các containers khác.

### 16.1.2 Chiến lược Phân tích (Analysis Strategy)
Vì lưu lượng được xử lý bởi một trình cân bằng tải (AWS ELB), có thể chia tách lưu lượng giữa VM và các containers sao cho tôi có thể đăng nhập vào cả hai cùng một lúc. Đây là một tình huống lý tưởng cho phân tích so sánh: Tôi có thể chạy cùng một lệnh phân tích trên cả hai tại cùng một thời điểm trong ngày (cùng sự pha trộn lưu lượng và tải) và so sánh kết quả ngay lập tức.

Trong trường hợp này tôi đã có quyền truy cập vào host container, không chỉ là container, thứ cho phép tôi sử dụng bất kỳ công cụ phân tích nào và cung cấp quyền hạn cho những công cụ đó để thực hiện bất kỳ syscall nào. Nếu tôi chỉ có quyền truy cập container, việc phân tích sẽ tiêu tốn nhiều thời gian hơn do các nguồn quan sát và quyền hạn kernel bị giới hạn, yêu cầu sự suy luận nhiều hơn từ các chỉ số giới hạn thay vì đo lường trực tiếp. Một số vấn đề hiệu năng hiện nay là không thực tế để phân tích chỉ từ riêng container (xem Chương 11, Điện toán đám mây).

Về các phương pháp luận, tôi đã lên kế hoạch bắt đầu với 60-second checklist (Chương 1, Giới thiệu, Mục 1.10.1, Linux Perf Analysis in 60s) và phương pháp USE (Chương 2, Các phương pháp luận, Mục 2.5.9, Phương pháp USE), và dựa trên những manh mối của họ để thực hiện phân tích drill-down (Mục 2.5.12, Phân tích Drill-Down) và các phương pháp luận khác.

Tôi đã bao gồm các lệnh tôi đã chạy và kết quả của chúng trong các phần tiếp theo, sử dụng dấu nhắc "serverA#" cho thực thể VM, và "serverB#" cho host container.

### 16.1.3 Thống kê (Statistics)
Tôi đã bắt đầu bằng việc chạy uptime(1) để kiểm tra các thống kê mức trung bình tải. Trên cả hai hệ thống:

```bash
serverA# uptime
 22:07:23 up 15 days,  5:01,  1 user,  load average: 85.09, 89.25, 91.26

serverB# uptime
 22:06:24 up 91 days, 23:52,  1 user,  load average: 17.94, 16.92, 16.62
```

Điều này cho thấy tải là khá ổn định, trở nên nhẹ hơn một chút trên thực thể VM (85.09 so với 91.26) và nặng hơn một chút trên container (17.94 so với 16.62). Tôi đã kiểm tra các xu hướng để xem liệu vấn đề có đang tăng lên, giảm xuống, hay ổn định: điều này đặc biệt quan trọng trong các môi trường đám mây thứ có thể tự động di chuyển tải đi khỏi một thực thể không khỏe mạnh. Thêm nữa, nhiều lần sau khi tôi đăng nhập vào một thực thể gặp vấn đề lại thấy rất ít hoạt động, và một mức trung bình tải một phút tiến dần về không.

Các mức trung bình tải cũng cho thấy VM có tải cao hơn nhiều so với host container (85.09 so với 17.94), mặc dù tôi sẽ cần các thống kê từ các công cụ khác để hiểu điều này có ý nghĩa gì. Các mức trung bình tải cao thường chỉ ra nhu cầu CPU, nhưng cũng có thể liên quan đến I/O (xem Chương 6, CPUs, Mục 6.6.1, uptime).

Để khám phá tải CPU, tôi đã chuyển sang mpstat(1), bắt đầu với các mức trung bình trên toàn hệ thống. Trên máy ảo:

```bash
serverA# mpstat 10
Linux 4.4.0-130-generic (...) 07/18/2019      _x86_64_  (48 CPU)

10:07:55 PM  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
10:08:05 PM  all   89.72    0.00    7.84    0.00    0.00    0.04    0.00    0.00    0.00    2.40
10:08:15 PM  all   88.60    0.00    9.18    0.00    0.00    0.05    0.00    0.00    0.00    2.17
10:08:25 PM  all   89.71    0.00    9.01    0.00    0.00    0.05    0.00    0.00    0.00    1.23
10:08:35 PM  all   89.55    0.00    8.11    0.00    0.00    0.06    0.00    0.00    0.00    2.28
10:08:45 PM  all   89.87    0.00    8.21    0.00    0.00    0.05    0.00    0.00    0.00    1.86
^C
Average:     all   89.49    0.00    8.47    0.00    0.00    0.05    0.00    0.00    0.00    1.99
```

Và trên container:

```bash
serverB# mpstat 10
Linux 4.19.26 (...) 07/18/2019      _x86_64_  (64 CPU)

09:56:11 PM  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
09:56:21 PM  all   23.21    0.01    0.32    0.00    0.00    0.10    0.00    0.00    0.00   76.37
09:56:31 PM  all   20.21    0.00    0.38    0.00    0.00    0.08    0.00    0.00    0.00   79.33
09:56:41 PM  all   21.58    0.00    0.39    0.00    0.00    0.10    0.00    0.00    0.00   77.92
09:56:51 PM  all   21.57    0.01    0.39    0.02    0.00    0.09    0.00    0.00    0.00   77.93
09:57:01 PM  all   20.93    0.00    0.35    0.00    0.00    0.09    0.00    0.00    0.00   78.63
^C
Average:     all   21.50    0.00    0.36    0.00    0.00    0.09    0.00    0.00    0.00   78.04
```

mpstat(1) in ra số lượng CPUs làm dòng đầu tiên. Kết quả cho thấy máy ảo có 48 CPUs, và host container có 64. Điều này giúp tôi diễn giải thêm về các mức trung bình tải: nếu chúng dựa trên CPU, nó sẽ cho thấy thực thể VM đang chạy tốt vào vùng bão hòa CPU, bởi vì các mức trung bình tải là xấp xỉ gấp đôi số lượng CPU, trong khi host container là dưới-mức-sử-dụng. Các chỉ số mpstat(1) đã hỗ trợ giả thuyết này: thời gian rảnh rỗi (idle) trên VM là khoảng 2%, trong khi trên host container nó là khoảng 78%.

Bằng việc kiểm tra các thống kê mpstat(1) khác, tôi đã nhận diện các manh mối khác:
- Mức sử dụng CPU (%usr + %sys + ...) cho thấy VM ở mức 98% so với container ở mức 22%. Những bộ xử lý này có hai hyperthreads cho mỗi lõi CPU, vì vậy việc vượt qua mốc sử dụng 50% thường có nghĩa là tranh chấp lõi hyperthread, làm suy giảm hiệu năng. VM đã nằm sâu trong vùng lãnh thổ này, trong khi host container có thể vẫn được hưởng lợi từ việc chỉ có một hyperthread bận rộn cho mỗi lõi.
- Thời gian hệ thống (%sys) trên VM cao hơn nhiều: khoảng 8% so với 0.38%. Nếu VM đang chạy ở mức bão hòa CPU, thời gian %sys tăng thêm này có thể bao gồm các đường dẫn mã context switch của kernel. Truy vết hoặc tạo hồ sơ kernel sẽ xác nhận điều này.

Tôi tiếp tục các lệnh khác từ 60-second checklist. vmstat(8) cho thấy các độ dài hàng đợi chạy tương tự như các mức trung bình tải, xác nhận rằng các mức trung bình tải là dựa trên CPU. iostat(1) cho thấy rất ít đĩa I/O, và sar(1) cho thấy mạng I/O thấp. (Những kết quả đó không được bao gồm ở đây.) Điều này xác nhận rằng VM đang chạy ở mức bão hòa CPU, khiến cho các luồng có thể chạy được (runnable threads) phải chờ tới lượt của chúng, trong khi host container thì không. top(1) trên host container cũng cho thấy chỉ có một container đang chạy.

Những lệnh này cung cấp các thống kê cho phương pháp USE, thứ cũng nhận diện vấn đề về tải CPU.

Liệu tôi có giải quyết được vấn đề không? Tôi đã thấy rằng VM có một mức trung bình tải là 85 trên một hệ thống 48-CPU, và mức trung bình tải đó là dựa trên CPU. Điều này có nghĩa là các luồng đã chờ đợi tới lượt của chúng xấp xỉ 77% thời gian (85/48 - 1), và việc loại bỏ thời gian chờ đợi này sẽ mang lại tốc độ nhanh hơn xấp xỉ 4 lần (1 / (1 - 0.77)). Trong khi độ lớn này tương ứng với vấn đề, tôi không thể giải thích tại sao mức trung bình tải lại cao hơn: cần phải phân tích thêm.

### 16.1.4 Cấu hình (Configuration)
Biết rằng đã có một vấn đề về CPU, tôi đã kiểm tra cấu hình của các CPUs và các giới hạn của chúng (tinh chỉnh hiệu năng tĩnh: Mục 2.5.17 và 6.5.7). Các bộ xử lý tự chúng là khác nhau giữa các VMs và containers. Dưới đây là /proc/cpuinfo cho máy ảo:

```bash
serverA# cat /proc/cpuinfo
processor           : 47
vendor_id           : GenuineIntel
cpu family          : 6
model               : 85
model name          : Intel(R) Xeon(R) Platinum 8175M CPU @ 2.50GHz
stepping            : 4
microcode           : 0x200005e
cpu MHz             : 2499.998
cache size          : 33792 KB
physical id         : 0
siblings            : 48
core id             : 23
cpu cores           : 24
apicid              : 47
initial apicid      : 47
fpu                 : yes
fpu_exception       : yes
cpuid level         : 13
wp                  : yes
flags               : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat
pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpelgb rdtscp lm constant_tsc
arch_perfmon rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq
monitor ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes
xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single kaiser
fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm mpx avx512f rdseed adx
smap clflushopt clwb avx512cd xsaveopt xsavec xgetbv1 ida arat
bugs                : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass
bogomips            : 4999.99
clflush size        : 64
cache_alignment     : 64
address sizes       : 46 bits physical, 48 bits virtual
power management:
```

Và của container:

```bash
serverB# cat /proc/cpuinfo
processor           : 63
vendor_id           : GenuineIntel
cpu family          : 6
model               : 79
model name          : Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
stepping            : 1
microcode           : 0xb000033
cpu MHz             : 1200.601
cache size          : 46080 KB
physical id         : 1
siblings            : 32
core id             : 15
cpu cores           : 16
apicid              : 95
initial apicid      : 95
fpu                 : yes
fpu_exception       : yes
cpuid level         : 13
wp                  : yes
flags               : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat
pse36 clflush mmx fxsr sse sse2 ht syscall nx pdpelgb rdtscp lm constant_tsc arch_
perfmon rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq monitor
est ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes
xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch cpuid_fault
invpcid_single pti fsgsbase bmi1 hle avx2 smep bmi2 erms invpcid rtm mpx avx512f rdseed adx
xsveopt ida
bugs                : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf
bogomips            : 4662.22
clflush size        : 64
cache_alignment     : 64
address sizes       : 46 bits physical, 48 bits virtual
power management:
```

Các CPUs cho container có tốc độ xung nhịp cơ bản thấp hơn một chút (2.30 so với 2.50 GHz); tuy nhiên, chúng có một bộ đệm ẩn cấp cuối (last-level cache) lớn hơn nhiều (45 so với 33 Mbytes). Tùy thuộc vào khối lượng công việc, kích thước bộ đệm ẩn lớn hơn có thể tạo ra sự khác biệt đáng kể cho hiệu năng CPU. Để điều tra thêm, tôi cần sử dụng các PMCs.

### 16.1.5 PMCs
Các bộ đếm giám sát hiệu năng (Performance monitoring counters - PMCs) có thể giải thích hiệu năng CPU ở cấp độ chu kỳ, và có sẵn trên một số thực thể nhất định trong AWS EC2. Tôi đã công bố một bộ công cụ cho phân tích PMC trên đám mây [Gregg 20e], thứ bao gồm pmcarch(8) (Mục 6.6.11, pmcarch). pmcarch(8) hiển thị Intel "architectural set" của các PMCs, thứ là các bộ PMCs cơ bản nhất sẵn có phổ biến.

Trên máy ảo:

```text
serverA# ./pmcarch -p 4093 10
K_CYCLES K_INSTR      IPC BR_RETIRED   BR_MISPRED  BMR% LLCREF      LLCMISS     LLC%
982412660 575706336 0.59 126424862460 2416880487  1.91 15724006692 10872315070 30.86
999621309 555043627 0.56 120449284756 2317302514  1.92 15378257714 11121882510 27.68
991146940 558145849 0.56 126350181501 2530383860  2.00 15965082710 11464682655 28.19
996314688 562276830 0.56 122215605985 2348638980  1.92 15558286345 10835594199 30.35
979890037 560268707 0.57 125609807909 2386085660  1.90 15828820588 11038597030 30.26
[...]
```

Trên thực thể container:

```text
serverB# ./pmcarch -p 1928219 10
K_CYCLES K_INSTR      IPC BR_RETIRED   BR_MISPRED  BMR% LLCREF      LLCMISS     LLC%
147523816 222396364 1.51 46053921119  641813770   1.39 8880477235  968809014   89.09
156634810 229801807 1.47 48236123575  653064504   1.35 9186609260  1183858023  87.11
152783226 237001219 1.55 49344315621  692819230   1.40 9314992450  8794944418  90.56
140787179 213570329 1.52 44518363978  631588112   1.42 8675999448  712318917   91.79
136822760 219706637 1.61 45129020910  651436401   1.44 8689831639  617678747   92.89
[...]
```

Điều này cho thấy số chỉ lệnh trên mỗi chu kỳ (IPC) khoảng 0.57 cho VM so với khoảng 1.52 cho container: một sự khác biệt gấp 2.6 lần.

Một lý do cho IPC thấp hơn có thể là tranh chấp hyperthread, vì VM host đang chạy ở mức trên 50% sử dụng CPU. Cột cuối cùng cho thấy một lý do bổ sung: tỷ lệ trúng (hit ratio) của bộ đệm ẩn cấp cuối (LLC) chỉ là 30% cho VM, so với khoảng 90% cho container. Điều này cho thấy các chỉ lệnh trên VM thường xuyên bị đình trệ trên bộ nhớ chính, làm giảm thông lượng chỉ lệnh (hiệu năng).

Tỷ lệ trúng LLC thấp hơn trên VM có thể là do ít nhất ba yếu tố:
- Kích thước LLC nhỏ hơn (33 so với 45 Mbytes).
- Chạy toàn bộ khối lượng công việc thay vì một thành phần con (như đã đề cập trong Tuyên bố Vấn đề); một thành phần con có khả năng sẽ tốt hơn: ít chỉ lệnh và dữ liệu hơn.
- Sự bão hòa CPU gây ra context switching nhiều hơn, và việc nhảy giữa các đường dẫn mã (bao gồm cả người dùng và kernel), làm tăng áp lực bộ đệm ẩn.

Yếu tố cuối cùng có thể được điều tra bằng các công cụ truy vết.

### 16.1.6 Các sự kiện Phần mềm (Software Events)
Để điều tra các đợt context switches, tôi bắt đầu với lệnh perf(1) để đếm các đợt context switches trên toàn hệ thống. Việc này sử dụng một sự kiện phần mềm, thứ tương tự như một sự kiện phần cứng (PMC) nhưng được triển khai trong phần mềm (xem Chương 4, Các Công cụ Quan trắc, Hình 4.5, và Chương 13, perf, Mục 13.5, Các sự kiện Phần mềm).

Trên máy ảo:

```bash
serverA# perf stat -e cs -a -I 1000
#           time             counts unit events
     1.000411740          2,063,105      cs
     2.000977435          2,065,354      cs
     3.001537756          1,527,297      cs
     4.002028407            515,509      cs
     5.002538455          2,447,126      cs
     6.003114251          2,021,182      cs
     7.003265091          2,329,157      cs
     8.004093520          1,740,898      cs
     9.004533912          1,235,641      cs
    10.005106500          2,340,443      cs
^C  10.513632795          1,496,555      cs
```

Kết quả này cho thấy một tốc độ khoảng hai triệu đợt context switches mỗi giây. Sau đó tôi đã chạy nó trên host container, lần này khớp trên PID của ứng dụng container để loại trừ các containers khả thi khác (tôi cũng đã thực hiện khớp PID tương tự trên VM, và nó đã không làm thay đổi đáng kể các kết quả trước đó¹):

---
¹ Thế thì tại sao tôi không bao gồm kết quả khớp-PID cho VM? Tôi không có nó.

---

```bash
serverB# perf stat -e cs -p 1928219 -I 1000
#           time             counts unit events
     1.001931945              1,172      cs
     2.002664012              1,370      cs
     3.003441563              1,034      cs
     4.004140394              1,207      cs
     5.004947675              1,053      cs
     6.005605844                955      cs
     7.006311221                619      cs
     8.007082057              1,050      cs
     9.007716475              1,215      cs
    10.008415042              1,373      cs
^C  10.584617028                894      cs
```

Kết quả này cho thấy tốc độ chỉ khoảng một nghìn đợt context switches mỗi giây.

Một tốc độ context switches cao có thể gây áp lực nhiều hơn lên các bộ đệm ẩn CPU, thứ đang chuyển đổi giữa các đường dẫn mã khác nhau, bao gồm cả kernel code để quản lý context switch, và có thể là các tiến trình khác nhau.² Để điều tra thêm các ngữ cảnh ngữ cảnh, tôi đã sử dụng các công cụ truy vết.

### 16.1.7 Truy vết (Tracing)
Có một số công cụ truy vết dựa trên BPF để phân tích mức sử dụng CPU và context switching sâu hơn, bao gồm, từ BCC: cpudist(8), cpuwalk(8), runqlen(8), runqlat(8), runqslower(8), cpuunclaimed(8), và nhiều hơn nữa (xem Hình 15.1).

cpudist(8) hiển thị thời lượng on-CPU của các luồng. Trên máy ảo:

```bash
serverA# cpudist -p 4093 10 1
Tracing on-CPU time... Hit Ctrl-C to end.

     usecs               : count     distribution
         0 -> 1          : 3618650   |****************************************|
         2 -> 3          : 2704935   |******************************          |
         4 -> 7          : 421179    |****                                    |
         8 -> 15         : 99416     |*                                       |
        16 -> 31         : 16951     |                                        |
        32 -> 63         : 6355      |                                        |
        64 -> 127        : 3586      |                                        |
       128 -> 255        : 3400      |                                        |
       256 -> 511        : 4004      |                                        |
       512 -> 1023       : 4445      |                                        |
      1024 -> 2047       : 8173      |                                        |
      2048 -> 4095       : 9165      |                                        |
      4096 -> 8191       : 7194      |                                        |
      8192 -> 16383      : 11954     |                                        |
     16384 -> 32767      : 1426      |                                        |
     32768 -> 65535      : 967       |                                        |
     65536 -> 131071     : 338       |                                        |
    131072 -> 262143     : 93        |                                        |
    262144 -> 524287     : 28        |                                        |
    524288 -> 1048575    : 4         |                                        |
```

Điều này cho thấy ứng dụng điển hình dành rất ít thời gian on-CPU, thường là ít hơn 7 micro giây. Các công cụ khác (stackcount(8) của t:sched:sched_switch, và /proc/PID/status) cho thấy ứng dụng thường rời khỏi CPU do các đợt context switches *không tự nguyện* (involuntary).³

---
² Đối với một số cấu hình bộ xử lý và kernel, context switching cũng có thể flush bộ đệm ẩn L1.
³ /proc/PID/status gọi chúng là nonvoluntary_ctxt_switches.

---

Trên host container:

```bash
serverB# cpudist -p 1928219 10 1
Tracing on-CPU time... Hit Ctrl-C to end.

     usecs               : count     distribution
         0 -> 1          : 0         |                                        |
         2 -> 3          : 16        |                                        |
         4 -> 7          : 6         |                                        |
         8 -> 15         : 7         |                                        |
        16 -> 31         : 8         |                                        |
        32 -> 63         : 10        |                                        |
        64 -> 127        : 18        |                                        |
       128 -> 255        : 40        |                                        |
       256 -> 511        : 44        |                                        |
       512 -> 1023       : 156       |*                                       |
      1024 -> 2047       : 238       |**                                      |
      2048 -> 4095       : 4511      |****************************************|
      4096 -> 8191       : 277       |**                                      |
      8192 -> 16383      : 286       |**                                      |
     16384 -> 32767      : 77        |                                        |
     32768 -> 65535      : 63        |                                        |
     65536 -> 131071     : 44        |                                        |
    131072 -> 262143     : 9         |                                        |
    262144 -> 524287     : 14        |                                        |
    524288 -> 1048575    : 5         |                                        |
```

Hiện tại ứng dụng thường dành từ 2 đến 4 mili giây on-CPU. Các công cụ khác cho thấy nó không bị gián đoạn nhiều bởi các đợt context switches không tự nguyện.

Các đợt context switches không tự nguyện trên VM, và tốc độ cao của các đợt context switches đã thấy sớm hơn, đã gây ra các vấn đề hiệu năng. Khiến ứng dụng rời khỏi CPU sau khi thường xuyên dành ít hơn 10 micro giây cũng không trao cho các bộ đệm ẩn CPU nhiều thời gian để làm ấm cho các đường dẫn mã hiện tại.

### 16.1.8 Kết luận (Conclusion)
Tôi đã kết luận rằng lý do cho sự cải thiện hiệu năng là:
- **Không có các hàng xóm container (No container neighbors):** Host container rảnh rỗi ngoại trừ một container đó. Điều này cho phép container có toàn bộ các bộ đệm ẩn CPU cho riêng mình, cũng như chạy mà không có tranh chấp CPU. Trong khi điều này tạo ra các kết quả thuận lợi cho container trong quá trình kiểm tra, đó không phải là tình huống dự kiến cho mục đích sử dụng sản xuất dài hạn nơi các containers lân cận sẽ là tiêu chuẩn. Microservice có thể thấy rằng thắng lợi hiệu năng 3-4 lần biến mất khi các bên thuê khác chuyển đến.
- **Sự khác biệt về kích thước LLC và khối lượng công việc:** IPC thấp hơn 2.6 lần trên VM, thứ có thể giải thích 2.6 lần sự chậm chạp này. Một nguyên nhân có thể là tranh chấp hyperthread khi VM host đang chạy ở mức hơn 50% sử dụng (và có hai hyperthreads cho mỗi lõi). Tuy nhiên, nguyên nhân chính có thể là tỷ lệ trúng LLC thấp hơn: 30% trên VM so với 90% trên container. Tỷ lệ trúng LLC thấp này có thể do ba lý do hợp lý:
  - Kích thước LLC nhỏ hơn trên VM: 33 Mbytes so với 45 Mbytes.
  - Một khối lượng công việc phức tạp hơn trên VM: toàn bộ ứng dụng, yêu cầu nhiều văn bản chỉ lệnh và dữ liệu hơn so với thành phần con chạy trên container.
  - Một tốc độ cao của context switches trên VM: khoảng 2 triệu mỗi giây. Những thứ này ngăn cản các luồng khỏi việc chạy on-CPU đủ lâu, gây nhiễu cho việc làm ấm bộ đệm ẩn. Các thời lượng on-CPU thường ít hơn 10 μs trên VM so với 2-4 ms trên host container.
- **Sự khác biệt về tải CPU:** Một tải cao hơn đã được hướng tới VM, thúc đẩy các CPUs tới bão hòa: một mức trung bình tải dựa trên CPU là 85 trên một hệ thống 48-CPU. Điều này gây ra một tốc độ khoảng 2 triệu đợt context switches mỗi giây, và độ trễ hàng đợi chạy khi các luồng chờ tới lượt của chúng. Độ trễ hàng đợi chạy được ngụ ý bởi các mức trung bình tải cho thấy VM đang chạy chậm hơn khoảng 4 lần.

Những vấn đề này giải thích sự khác biệt hiệu năng quan sát được.

## 16.2 Thông tin Bổ sung (Additional Information)
Để biết thêm các nghiên cứu điển hình trong phân tích hiệu năng hệ thống, hãy kiểm tra cơ sở dữ liệu lỗi (hoặc hệ thống ticketing) tại công ty của bạn cho các vấn đề liên quan đến hiệu năng trước đó, và các cơ sở dữ liệu lỗi công khai cho các ứng dụng và hệ điều hành bạn sử dụng. Những vấn đề này thường bắt đầu với một tuyên bố vấn đề và kết thúc với bản sửa lỗi cuối cùng. Nhiều hệ thống cơ sở dữ liệu lỗi cũng bao gồm một lịch sử bình luận có dấu thời gian, thứ có thể được nghiên cứu để thấy quá trình phân tích, bao gồm các giả thuyết đã khám phá và các lần chuyển hướng sai đã thực hiện. Việc thực hiện những đợt chuyển hướng sai, và nhận diện nhiều yếu tố đóng góp, là điều bình thường.

Một số nghiên cứu điển hình về hiệu năng hệ thống được công bố theo thời gian, ví dụ, trên blog của tôi [Gregg 20j]. Các tạp chí kỹ thuật với trọng tâm vào thực tế, chẳng hạn như *USENIX ;login:* [USENIX 20] và *ACM Queue* [ACM 20], cũng thường sử dụng các nghiên cứu điển hình làm ngữ cảnh khi mô tả các giải pháp kỹ thuật mới cho các vấn đề.

## 16.3 Tài liệu tham khảo (References)
- [Joy 81] Joy, W., “tcp-ip digest contribution,” http://www.rfc-editor.org/rfc/museum/tcp-ip-digest/tcp-ip-digest.v1n6.1, 1981.
- [Anon 85] Anon et al., “A Measure of Transaction Processing Power,” *Datamation*, April 1, 1985.
- [Shanley 98] Shanley, K., “History and Overview of the TPC,” http://www.tpc.org/information/about/history.asp, 1998.
- [Waldspurger 02] Waldspurger, C., “Memory Resource Management in VMware ESX Server,” *Proceedings of the 5th Symposium on Operating Systems Design and Implementation*, 2002.
- [Cherkasova 05] Cherkasova, L., and Gardner, R., “Measuring CPU Overhead for I/O Processing in the Xen Virtual Machine Monitor,” *USENIX ATEC*, 2005.
- [Adams 06] Adams, K., and Agesen, O., “A Comparison of Software and Hardware Techniques for x86 Virtualization,” *ASPLOS*, 2006.
- [Gupta 06] Gupta, D., Cherkasova, L., Gardner, R., and Vahdat, A., “Enforcing Performance Isolation across Virtual Machines in Xen,” *ACM/IFIP/USENIX Middleware*, 2006.
- [Qumranet 06] “KVM: Kernel-based Virtualization Driver,” Qumranet Whitepaper, 2006.
- [Cherkasova 07] Cherkasova, L., Gupta, D., and Vahdat, A., “Comparison of the Three CPU Schedulers in Xen,” *ACM SIGMETRICS*, 2007.
- [Liguori, 07] Liguori, A., “The Myth of Type I and Type II Hypervisors,” http://blog.codemonkey.ws/2007/10/myth-of-type-i-and-type-ii-hypervisors.html, 2007.
- [VMware 07] “Understanding Full Virtualization, Paravirtualization, and Hardware Assist,” https://www.vmware.com/techpapers/2007/understanding-full-virtualization-paravirtualizat-1008.html, 2007.
- [Matthews 08] Matthews, J., et al. *Running Xen: A Hands-On Guide to the Art of Virtualization*, Prentice Hall, 2008.
- [Bourbonnais 08] Bourbonnais, R., “Decoding Bonnie++,” https://blogs.oracle.com/roch/entry/decoding_bonnie, 2008.
- [Milewski 11] Milewski, B., “Virtual Machines: Virtualizing Virtual Memory,” http://corensic.wordpress.com/2011/12/05/virtual-machines-virtualizing-virtual-memory, 2011.
- [Adamczyk 12] Adamczyk, B., and Chydzinski, A., “Performance Isolation Issues in Network Virtualization in Xen,” *International Journal on Advances in Networks and Services*, 2012.
- [Hoff 12] Hoff, T., “Pinterest Cut Costs from $54 to $20 Per Hour by Automatically Shutting Down Systems,” http://highscalability.com/blog/2012/12/12/pinterest-cut-costs-from-54-to-20-per-hour-by-automatically.html, 2012.
- [Matz 13] Matz, M., Hubička, J., Jaeger, A., and Mitchell, M., “System V Application Binary Interface, AMD64 Architecture Processor Supplement, Draft Version 0.99.6,” http://x86-64.org/documentation/abi.pdf, 2013.
- [Gregg 14b] Gregg, B., “From Clouds to Roots: Performance Analysis at Netflix,” http://www.brendangregg.com/blog/2014-09-27/from-clouds-to-roots.html, 2014.
- [Gregg 14c] Gregg, B., “The Benchmark Paradox,” http://www.brendangregg.com/blog/2014-05-03/the-benchmark-paradox.html, 2014.
- [Gregg 14d] Gregg, B., “Active Benchmarking,” http://www.brendangregg.com/activebenchmarking.html, 2014.
- [Heo 15] Heo, T., “Control Group v2,” *Linux documentation*, https://www.kernel.org/doc/Documentation/cgroup-v2.txt, 2015.
- [Gregg 16a] Gregg, B., “Unikernel Profiling: Flame Graphs from dom0,” http://www.brendangregg.com/blog/2016-01-27/unikernel-profiling-from-dom0.html, 2016.
- [Kadera 16] Kadera, M., “Accelerating the Next 10,000 Clouds,” https://www.slideshare.net/Docker/accelerating-the-next-10000-clouds-by-michael-kadera-intel, 2016.
- [Borello 17] Borello, G., “Container Isolation Gone Wrong,” *Sysdig blog*, https://sysdig.com/blog/container-isolation-gone-wrong, 2017.
- [Gregg 17e] Gregg, B., “AWS EC2 Virtualization 2017: Introducing Nitro,” http://www.brendangregg.com/blog/2017-11-29/aws-ec2-virtualization-2017.html, 2017.
- [Gregg 17f] Gregg, B., “The PMCs of EC2: Measuring IPC,” http://www.brendangregg.com/blog/2017-05-04/the-pmcs-of-ec2.html, 2017.
- [Gregg 17g] Gregg, B., “Container Performance Analysis at DockerCon 2017,” http://www.brendangregg.com/blog/2017-05-15/container-performance-analysis-dockercon-2017.html, 2017.
- [Gregg 18d] Gregg, B., “Evaluating the Evaluation: A Benchmarking Checklist,” http://www.brendangregg.com/blog/2018-06-30/benchmarking-checklist.html, 2018.
- [Gregg 18e] Gregg, B., “YOW! 2018 Cloud Performance Root Cause Analysis at Netflix,” http://www.brendangregg.com/blog/2019-04-26/yow2018-cloud-performance-netflix.html, 2018.
- [Leonovich 18] Leonovich, M., “Another reason why your Docker containers may be slow,” https://hackernoon.com/another-reason-why-your-docker-containers-may-be-slow-d37207dec27f, 2018.
- [Gregg 19] Gregg, B., *BPF Performance Tools: Linux System and Application Observability*, Addison-Wesley, 2019.
- [Gregg 19e] Gregg, B., “kvmexits.bt,” https://github.com/brendangregg/bpf-perf-tools-book/blob/master/originals/Ch16_Hypervisors/kvmexits.bt, 2019.
- [Gregg 19f] Gregg, B., “Two Kernel Mysteries and the Most Technical Talk I’ve Ever Seen,” http://www.brendangregg.com/blog/2019-10-15/kernelrecipes-kernel-ftrace-internals.html, 2019.
- [Gregg 19h] Gregg, B., “LISA2019 Linux Systems Performance,” *USENIX LISA*, http://www.brendangregg.com/blog/2020-03-08/lisa2019-linux-systems-performance.html, 2019.
- [Kwiatkowski 19] Kwiatkowski, A., “Autoscaling in Reality: Lessons Learned from Adaptively Scaling Kubernetes,” https://conferences.oreilly.com/velocity/vl-eu/public/schedule/detail/78924, 2019.
- [Agache 20] Agache, A., et al., “Firecracker: Lightweight Virtualization for Serverless Applications,” https://www.usenix.org/publications/proceedings/firecracker-lightweight-virtualization-for-serverless-applications, 2020.
- [Borkmann 20] Borkmann, D., et al., “eBPF-based Networking, Security, and Observability,” https://github.com/cilium/cilium, last updated 2020.
- [Dronamraju 20] Dronamraju, S., “Uprobe-tracer: Uprobe-based Event Tracing,” *Linux documentation*, https://www.kernel.org/doc/html/latest/trace/uprobetracer.html, accessed 2020.
- [Gregg 20e] Gregg, B., “PMC (Performance Monitoring Counter) Tools for the Cloud,” https://github.com/brendangregg/pmc-cloud-tools, last updated 2020.
- [Gregg 20h] Gregg, B., “One-Liners,” http://www.brendangregg.com/perf.html#OneLiners, last updated 2020.
- [Gregg 20j] “Brendan Gregg’s Blog,” http://www.brendangregg.com/blog, last updated 2020.
- [Hiramatsu 20] Hiramatsu, M., “Kprobe-based Event Tracing,” *Linux documentation*, https://www.kernel.org/doc/html/latest/trace/kprobetracer.html, accessed 2020.
- [Iovisor 20a] “bpftrace: High-level Tracing Language for Linux eBPF,” https://github.com/iovisor/bpftrace, last updated 2020.
- [Iovisor 20b] “BCC - Tools for BPF-based Linux IO Analysis, Networking, Monitoring, and More,” https://github.com/iovisor/bcc, last updated 2020.
- [Iovisor 20c] “bpftrace Reference Guide,” https://github.com/iovisor/bpftrace/blob/master/docs/reference_guide.md, last updated 2020.
- [USENIX 20] “;login: The USENIX Magazine,” https://www.usenix.org/publications/login, accessed 2020.
- [Zanussi 20] Zanussi, T., “Event Histograms,” *Linux documentation*, https://www.kernel.org/doc/html/latest/trace/histogram.html, accessed 2020.
