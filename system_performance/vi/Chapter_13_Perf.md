# Chương 13: perf

perf(1) là trình tạo hồ sơ (profiler) chính thức của Linux và nằm trong mã nguồn Linux kernel dưới thư mục tools/perf.¹ Nó là một công cụ đa năng (multi-tool) có các khả năng tạo hồ sơ (profiling), truy vết (tracing), và lập kịch bản (scripting), và là front-end cho hệ thống con quan sát perf_events của kernel. perf_events cũng được gọi là Performance Counters for Linux (PCL) hoặc Linux Performance Events (LPE). perf_events và front-end perf(1) bắt đầu với các khả năng bộ đếm giám sát hiệu năng (Performance Monitoring Counter - PMC), nhưng từ đó đã phát triển để hỗ trợ cả các nguồn truy vết dựa trên sự kiện: tracepoints, kprobes, uprobes, và USDT.

Chương này, cùng với Chương 14, Ftrace, và Chương 15, BPF, là tài liệu đọc tùy chọn cho những ai muốn tìm hiểu chi tiết hơn về một hoặc nhiều trình truy vết hệ thống.

So với các trình truy vết khác, perf(1) đặc biệt phù hợp cho phân tích CPU: tạo hồ sơ (lấy mẫu) vết ngăn xếp CPU (CPU stack traces), truy vết hành vi trình lập lịch CPU, và kiểm tra các PMCs để hiểu hiệu năng CPU ở cấp độ vi kiến trúc (micro-architectural) bao gồm cả hành vi chu kỳ (cycle behavior). Khả năng truy vết của nó cũng cho phép nó phân tích các mục tiêu khác, bao gồm cả đĩa I/O và các hàm phần mềm.

perf(1) có thể được sử dụng để trả lời các câu hỏi chẳng hạn như:
- Những đường dẫn mã nào đang tiêu thụ tài nguyên CPU?
- Các CPUs có đang bị đình trệ (stalled) do các lệnh nạp/ghi bộ nhớ không?
- Vì những lý do gì mà các luồng rời khỏi CPU?
- Mẫu của đĩa I/O là gì?

Các phần sau đây được cấu trúc để giới thiệu perf(1), chỉ ra các nguồn sự kiện, và sau đó chỉ ra các lệnh phụ (subcommands) sử dụng chúng. Các phần là:
- 13.1: Tổng quan về các lệnh phụ (Subcommands Overview)
- 13.2: Các lệnh một dòng ví dụ (Example One-Liners)
- Các Sự kiện (Events):
  - 13.3: Tổng quan về sự kiện (Events Overview)
  - 13.4: Các sự kiện phần cứng (Hardware Events)
  - 13.5: Các sự kiện phần mềm (Software Events)
  - 13.6: Các điểm truy vết (Tracepoints)
  - 13.7: Các sự kiện thăm dò (Probe Events)
- Các Lệnh (Commands):
  - 13.8: perf stat
  - 13.9: perf record
  - 13.10: perf report
  - 13.11: perf script
  - 13.12: perf trace
  - 13.13: Các lệnh khác
- 13.14: Tài liệu (Documentation)
- 13.15: Tài liệu tham khảo (References)

Các chương trước đã chỉ ra cách sử dụng perf(1) cho việc phân tích các mục tiêu cụ thể. Chương này tập trung vào chính perf(1).

---
¹ perf(1) là bất thường ở chỗ nó là một chương trình cấp người dùng lớn, phức tạp nằm trong cây mã nguồn Linux kernel. Người duy trì Arnaldo Carvalho de Melo đã mô tả tình huống này với tôi như một "thực nghiệm." Trong khi điều này đã mang lại lợi ích cho perf(1) và Linux vì chúng đã được phát triển song hành (lockstep), một số người cảm thấy không thoải mái với sự bao gồm của nó, và nó có thể vẫn là phần mềm người dùng phức tạp duy nhất từng được đưa vào trong mã nguồn Linux.

---

## 13.1 Tổng quan về các Lệnh phụ (Subcommands Overview)
Các khả năng của perf(1) được gọi qua các lệnh phụ (subcommands). Như một ví dụ sử dụng phổ biến, phần sau đây sử dụng hai lệnh phụ: `record` để instrument các sự kiện và lưu chúng vào một tập tin, và sau đó là `report` để tóm tắt nội dung của tập tin đó. Những lệnh phụ này được giải thích trong Mục 13.9, perf record, và Mục 13.10, perf report.

```bash
# perf record -F 99 -a -- sleep 30
[ perf record: Woken up 193 times to write data ]
[ perf record: Captured and wrote 48.916 MB perf.data (11880 samples) ]
# perf report --stdio
[...]
# Overhead  Command          Shared Object               Symbol
# ........  ................  ..........................  ...........................
#
    21.10%  swapper           [kernel.vmlinux]            [k] native_safe_halt
     6.39%  mysqld            [kernel.vmlinux]            [k] _raw_spin_unlock_irqrest
     4.66%  mysqld            mysqld                      [.] _Z8ut_delaym
     2.64%  mysqld            [kernel.vmlinux]            [k] finish_task_switch
[...]
```

Ví dụ cụ thể này đã lấy mẫu bất kỳ chương trình nào đang chạy trên bất kỳ CPU nào tại tần số 99 Hertz trong 30 giây, và sau đó hiển thị các hàm được lấy mẫu thường xuyên nhất.

Các lệnh phụ được lựa chọn từ một phiên bản perf(1) gần đây (từ Linux 5.6) được liệt kê trong Bảng 13.1.

Bảng 13.1 Các lệnh phụ perf được lựa chọn
| Mục | Lệnh | Mô tả |
| --- | --- | --- |
| - | annotate | Đọc perf.data (được tạo bởi perf record) và hiển thị mã được chú giải. |
| - | archive | Tạo một tập tin perf.data di động chứa thông tin gỡ lỗi và biểu tượng (symbol info). |
| - | bench | Các microbenchmarks hệ thống. |
| - | buildid-cache | Quản lý build-id cache (được sử dụng bởi các thăm dò USDT). |
| - | c2c | Các công cụ phân tích cache line. |
| - | diff | Đọc hai tập tin perf.data và hiển thị hồ sơ sai biệt (differential profile). |
| - | evlist | Liệt kê các tên sự kiện trong một tập tin perf.data. |
| 14.12 | ftrace | Một giao diện perf(1) tới trình truy vết Ftrace. |
| - | inject | Bộ lọc để tăng cường dòng sự kiện với thông tin bổ sung. |
| - | kmem | Truy vết/đo lường các thuộc tính bộ nhớ kernel (slab). |
| 11.3.3 | kvm | Truy vết/đo lường các thực thể khách kvm. |
| 13.3 | list | Liệt kê các loại sự kiện. |
| - | lock | Phân tích các sự kiện khóa (lock events). |
| - | mem | Tạo hồ sơ truy cập bộ nhớ. |
| 13.7 | probe | Định nghĩa các điểm truy vết động mới. |
| 13.9 | record | Chạy một lệnh và ghi lại hồ sơ của nó vào perf.data. |
| 13.10 | report | Đọc perf.data (được tạo bởi perf record) và hiển thị hồ sơ. |
| 6.6.13 | sched | Truy vết/đo lường các thuộc tính trình lập lịch (các độ trễ). |
| 5.5.1 | script | Đọc perf.data (được tạo bởi perf record) và hiển thị kết quả truy vết. |
| 13.8 | stat | Chạy một lệnh và thu thập các thống kê bộ đếm hiệu năng. |
| - | timechart | Hình ảnh hóa hành vi toàn hệ thống trong một khối lượng công việc. |
| - | top | Công cụ tạo hồ sơ hệ thống với các cập nhật màn hình thời gian thực. |
| 13.12 | trace | Một trình truy vết trực tiếp (các system calls theo mặc định). |

Hình 13.1 hiển thị các lệnh phụ perf thường được sử dụng với các nguồn dữ liệu và các loại kết quả của chúng.

(Hình 13.1 Các lệnh phụ perf thường được sử dụng)

Nhiều trong số này và các lệnh phụ khác được giải thích trong các phần tiếp theo. Một số lệnh phụ đã được bao quát trong các chương trước, như được trình bày trong Bảng 13.1.

Các phiên bản tương lai của perf(1) có thể thêm nhiều khả năng hơn: hãy chạy `perf` mà không có đối số để xem danh sách đầy đủ các lệnh phụ cho hệ thống của bạn.

## 13.2 Các lệnh Một dòng (One-Liners)
Các lệnh một dòng sau đây cho thấy các khả năng khác nhau của perf(1) qua các ví dụ. Đây là những lệnh từ một danh sách lớn hơn mà tôi đã công bố trực tuyến [Gregg 20h], thứ đã chứng tỏ là một cách hiệu quả để giải thích các khả năng của perf(1). Cú pháp của những lệnh này được bao quát trong các phần sau và trong các trang man của perf(1).

Lưu ý rằng nhiều lệnh một dòng này sử dụng `-a` để chỉ định tất cả các CPUs, nhưng điều này đã trở thành mặc định trong Linux 4.11 và có thể được lược bỏ trong đó và các kernel sau này.

**Liệt kê các Sự kiện (Listing Events)**
Liệt kê tất cả các sự kiện hiện đã biết:
`perf list`

Liệt kê các tracepoints sched:
`perf list 'sched:*'`

Liệt kê các sự kiện với tên chứa chuỗi "block":
`perf list block`

Liệt kê các probes động hiện có:
`perf probe -l`

**Đếm các Sự kiện (Counting Events)**
Hiển thị các thống kê PMC cho lệnh được chỉ định:
`perf stat command`

Hiển thị các thống kê PMC cho PID được chỉ định, cho đến khi nhấn Ctrl-C:
`perf stat -p PID`

Hiển thị các thống kê PMC cho toàn bộ hệ thống, trong 5 giây:
`perf stat -a sleep 5`

Hiển thị các thống kê bộ đệm ẩn cấp cuối cùng (last level cache - LLC) cho lệnh:
`perf stat -e LLC-loads,LLC-load-misses,LLC-stores,LLC-prefetches command`

Đếm các chu kỳ lõi không bị đình trệ (unhalted core cycles) sử dụng một đặc tả PMC thô (Intel):
`perf stat -e r003c -a sleep 5`

Đếm các lần đình trệ front-end sử dụng một đặc tả PMC thô dài dòng (Intel):
`perf stat -e cpu/event=0x0e,umask=0x01,inv,cmask=0x01/ -a sleep 5`

Đếm các syscalls mỗi giây trên toàn hệ thống:
`perf stat -e raw_syscalls:sys_enter -I 1000 -a`

Đếm các lệnh gọi hệ thống theo loại cho PID được chỉ định:
`perf stat -e 'syscalls:sys_enter_*' -p PID`

Đếm các sự kiện I/O thiết bị khối cho toàn bộ hệ thống, trong 10 giây:
`perf stat -e 'block:*' -a sleep 10`

**Tạo hồ sơ (Profiling)**
Lấy mẫu các hàm on-CPU cho lệnh được chỉ định, tại 99 Hertz:
`perf record -F 99 command`

Lấy mẫu vết ngăn xếp CPU (qua các con trỏ khung hình - frame pointers) trên toàn hệ thống trong 10 giây:
`perf record -F 99 -a -g -- sleep 10`

Lấy mẫu vết ngăn xếp CPU cho PID, sử dụng dwarf (debuginfo) để unwind các ngăn xếp:
`perf record -F 99 -p PID --call-graph dwarf sleep 10`

Lấy mẫu vết ngăn xếp CPU cho một container bằng its /sys/fs/cgroup/perf_event cgroup:
`perf record -F 99 -e cpu-clock --cgroup=docker/1d567f439319...etc... -a sleep 10`

Lấy mẫu vết ngăn xếp CPU cho toàn bộ hệ thống, sử dụng last branch record (LBR; Intel):
`perf record -F 99 -a --call-graph lbr sleep 10`

Lấy mẫu các vết ngăn xếp CPU, một lần sau mỗi 100 lần trượt bộ đệm ẩn cấp cuối cùng, trong 5 giây:
`perf record -e LLC-load-misses -c 100 -ag sleep 5`

Lấy mẫu các chỉ lệnh CPU cấp người dùng một cách chính xác (ví dụ: sử dụng Intel PEBS), trong 5 giây:
`perf record -e cycles:up -a sleep 5`

Lấy mẫu các CPUs tại 49 Hertz, và hiển thị các tên tiến trình hàng đầu và các phân đoạn (segments), trực tiếp:
`perf top -F 49 -ns comm,dso`

**Truy vết Tĩnh (Static Tracing)**
Truy vết các tiến trình mới, cho đến khi nhấn Ctrl-C:
`perf record -e sched:sched_process_exec -a`

Lấy mẫu một tập con các đợt chuyển đổi ngữ cảnh (context switches) với các vết ngăn xếp trong 1 giây:
`perf record -e context-switches -a -g sleep 1`

Truy vết tất cả các đợt chuyển đổi ngữ cảnh với các vết ngăn xếp trong 1 giây:
`perf record -e sched:sched_switch -a -g sleep 1`

Truy vết tất cả các đợt chuyển đổi ngữ cảnh với các vết ngăn xếp sâu 5-tầng trong 1 giây:
`perf record -e sched:sched_switch/max-stack=5/ -a sleep 1`

Truy vết connect(2) (các kết nối outbound) với các vết ngăn xếp, cho đến khi nhấn Ctrl-C:
`perf record -e syscalls:sys_enter_connect -a -g`

Lấy mẫu tại tối đa 100 yêu cầu thiết bị khối mỗi giây, cho đến khi nhấn Ctrl-C:
`perf record -F 100 -e block:block_rq_issue -a`

Truy vết tất cả các đợt phát hành và hoàn thành thiết bị khối (có dấu thời gian), cho đến khi nhấn Ctrl-C:
`perf record -e block:block_rq_issue,block:block_rq_complete -a`

Truy vết tất cả các yêu cầu khối, có kích thước ít nhất 64 Kbytes, cho đến khi nhấn Ctrl-C:
`perf record -e block:block_rq_issue --filter 'bytes >= 65536' -a`

Truy vết tất cả các lệnh gọi ext4, và ghi vào một vị trí không phải ext4, cho đến khi nhấn Ctrl-C:
`perf record -e 'ext4:*' -o /tmp/perf.data -a`

Truy vết sự kiện http__server__request USDT từ Node.js; Linux 4.10+:
`perf record -e sdt_node:http__server__request -a`

Truy vết các yêu cầu thiết bị khối với kết quả trực tiếp (không phải perf.data) cho đến khi nhấn Ctrl-C:
`perf trace -e block:block_rq_issue`

Truy vết các yêu cầu và hoàn thành thiết bị khối với kết quả trực tiếp:
`perf trace -e block:block_rq_issue,block:block_rq_complete`

Truy vết các lệnh gọi hệ thống trên toàn hệ thống với kết quả trực tiếp (dài dòng):
`perf trace`

**Truy vết Động (Dynamic Tracing)**
Thêm một thăm dò (probe) cho hàm kernel entry tcp_sendmsg() (--add là tùy chọn):
`perf probe --add tcp_sendmsg`

Xóa tracepoint (hoặc -d) tcp_sendmsg():
`perf probe --del tcp_sendmsg`

Liệt kê các biến có sẵn cho tcp_sendmsg(), cộng với các biến bên ngoài (externals) (cần debuginfo kernel):
`perf probe -V tcp_sendmsg --externs`

Liệt kê các thăm dò dòng (line probes) có sẵn cho tcp_sendmsg() (cần debuginfo):
`perf probe -L tcp_sendmsg`

Liệt kê các biến có sẵn cho tcp_sendmsg() tại dòng số 81 (cần debuginfo):
`perf probe -V tcp_sendmsg:81`

Thêm một thăm dò cho tcp_sendmsg() với các thanh ghi đối số đầu vào (đặc thù theo bộ xử lý):
`perf probe 'tcp_sendmsg %ax %dx %cx'`

Thêm một thăm dò cho tcp_sendmsg(), với một bí danh (“bytes”) cho thanh ghi %cx:
`perf probe 'tcp_sendmsg bytes=%cx'`

Truy vết thăm dò đã tạo ra trước đó khi bytes (bí danh) lớn hơn 100:
`perf record -e probe:tcp_sendmsg --filter 'bytes > 100' -a`

Thêm một tracepoint cho kết quả trả về của tcp_sendmsg(), và bắt giá trị trả về:
`perf probe 'tcp_sendmsg%return $retval'`

Thêm một thăm dò cho tcp_sendmsg(), với kích thước sk và trạng thái socket (cần debuginfo):
`perf probe 'tcp_sendmsg size sk->__sk_common.skc_state'`

Thêm một tracepoint cho do_sys_open() với tên tệp dưới dạng một chuỗi (cần debuginfo):
`perf probe 'do_sys_open filename:string'`

Thêm một thăm dò cho hàm fopen(3) cấp người dùng từ libc:
`perf probe -x /lib/x86_64-linux-gnu/libc.so.6 --add fopen`

**Báo cáo (Reporting)**
Hiển thị perf.data trong một trình duyệt ncurses (TUI) nếu có thể:
`perf report`

Hiển thị perf.data dưới dạng một báo cáo văn bản, với dữ liệu được hợp nhất cùng số lượng và phần trăm:
`perf report -n --stdio`

Liệt kê tất cả các sự kiện perf.data, với tiêu đề dữ liệu (khuyến nghị):
`perf script --header`

Liệt kê tất cả các sự kiện perf.data, với các trường được khuyến nghị (cần record -a; Linux < 4.1 đã sử dụng -f thay vì -F):
`perf script --header -F comm,pid,tid,cpu,time,event,ip,sym,dso`

Tạo một hình ảnh hóa flame graph (Linux 5.8+):
`perf script report flamegraph`

Tháo rời (Disassemble) và chú giải các chỉ lệnh với các phần trăm (cần một số debuginfo):
`perf annotate --stdio`

Đây là sự lựa chọn các lệnh một dòng của tôi; còn nhiều khả năng khác không được bao quát ở đây. Xem các lệnh phụ trong phần trước, và các phần sau đó trong chương này cùng các chương khác cho các lệnh perf(1).

---

## 13.3 Các sự kiện perf (perf Events)
Các sự kiện có thể được liệt kê bằng cách sử dụng `perf list`. Tôi đã bao gồm một sự lựa chọn ở đây từ Linux 5.8 để hiển thị các loại sự kiện khác nhau, được tô đậm:

```bash
# perf list

List of pre-defined events (to be used in -e):

  branch-instructions OR branches                    [Hardware event]
  branch-misses                                      [Hardware event]
  bus-cycles                                         [Hardware event]
  cache-misses                                       [Hardware event]
[...]
  context-switches OR cs                             [Software event]
  cpu-clock                                          [Software event]
[...]
  L1-dcache-load-misses                              [Hardware cache event]
  L1-dcache-loads                                    [Hardware cache event]
[...]
  branch-instructions OR cpu/branch-instructions/    [Kernel PMU event]
  branch-misses OR cpu/branch-misses/                [Kernel PMU event]
[...]
cache:
  l1d.replacement
       [L1D data line replacements] [...]
floating point:
  fp_arith_inst_retired.128b_packed_double
       [Number of SSE/AVX computational 128-bit packed double precision [...]
frontend:
  dsb2mite_switches.penalty_cycles
       [Decode Stream Buffer (DSB)-to-MITE switch true penalty cycles] [...]
memory:
  cycle_activity.cycles_l3_miss
       [Cycles while L3 cache miss demand load is outstanding] [...]
  offcore_response.demand_code_rd.l3_miss.any_snoop
       [DEMAND_CODE_RD & L3_MISS & ANY_Snoop] [...]
other:
  hw_interrupts.received
       [Number of hardware interrupts received by the processor]
pipeline:
  arith.divider_active
       [Cycles when divide unit is busy executing divide or square root [...]
uncore:
  unc_arb_coh_trk_requests.all
       [Unit: uncore_arb Number of entries allocated. Account for Any type:
        e.g. Snoop, Core aperture, etc]
[...]
  rNNN                                               [Raw hardware event descriptor]
  cpu/t1=v1[,t2=v2,t3 ...]/modifier                  [Raw hardware event descriptor]
       (see 'man perf-list' on how to encode it)
  mem:<addr>[/len][:access]                          [Hardware breakpoint]
  alarmtimer:alarmtimer_cancel                       [Tracepoint event]
  alarmtimer:alarmtimer_fired                        [Tracepoint event]
[...]
  probe:do_nanosleep                                 [Tracepoint event]
[...]
  sdt_hotspot:class__initialization__clinit          [SDT event]
  sdt_hotspot:class__initialization__concurrent      [SDT event]
[...]
List of pre-defined events (to be used in --pfm-events):

ix86arch:
  UNHALTED_CORE_CYCLES
       [count core clock cycles whenever the clock signal on the specific core is
running (not halted)]
  INSTRUCTION_RETIRED
[...]
```

Kết quả đã bị lược bớt rất nhiều ở nhiều chỗ, vì kết quả đầy đủ là 4,402 dòng trên hệ thống kiểm tra này. Các loại sự kiện là:
- **Hardware event:** Hầu hết là các sự kiện của bộ xử lý (được triển khai bằng cách sử dụng PMCs)
- **Software event:** Một bộ đếm sự kiện kernel
- **Hardware cache event:** Các sự kiện cache của bộ xử lý (PMCs)
- **Kernel PMU event:** Các sự kiện của Đơn vị Giám sát Hiệu năng (Performance Monitoring Unit - PMU) (PMCs)
- **cache, floating point...:** Các sự kiện của nhà cung cấp bộ xử lý (PMCs) và các mô tả ngắn gọn
- **Raw hardware event descriptor:** PMCs được chỉ định bằng các mã thô
- **Hardware breakpoint:** Sự kiện điểm dừng của bộ xử lý
- **Tracepoint event:** Các sự kiện instrumentation tĩnh của kernel
- **SDT event:** Các sự kiện instrumentation tĩnh cấp người dùng (USDT)
- **pfm-events:** Các sự kiện libpfm (được thêm vào trong Linux 5.8)

Tracepoint và SDT events chủ yếu liệt kê các điểm instrumentation tĩnh, nhưng nếu bạn đã tạo ra một số probes instrumentation động, những cái đó cũng sẽ được liệt kê. Tôi đã bao gồm một ví dụ trong kết quả: probe:do_nanosleep được mô tả như một "Tracepoint event" dựa trên một kprobe.

Lệnh `perf list` chấp nhận một chuỗi tìm kiếm làm đối số. Ví dụ, liệt kê các sự kiện chứa "mem_load_l3" với các sự kiện được tô đậm:

```bash
# perf list mem_load_l3

List of pre-defined events (to be used in -e):

cache:
  mem_load_l3_hit_retired.xsnp_hit
       [Retired load instructions which data sources were L3 and cross-core snoop
hits in on-pkg core cache Supports address when precise (Precise event)]
  mem_load_l3_hit_retired.xsnp_hitm
       [Retired load instructions which data sources were HitM responses from shared
L3 Supports address when precise (Precise event)]
  mem_load_l3_hit_retired.xsnp_miss
       [Retired load instructions which data sources were L3 hit and cross-core snoop
missed in on-pkg core cache Supports address when precise (Precise event)]
  mem_load_l3_hit_retired.xsnp_none
       [Retired load instructions which data sources were hits in L3 without snoops
required Supports address when precise (Precise event)]
[...]
```

Đây là các sự kiện phần cứng (dựa trên PMC), và kết quả bao gồm các mô tả ngắn gọn. (Precise event) đề cập đến các sự kiện có khả năng lấy mẫu dựa trên sự kiện chính xác (precise event-based sampling - PEBS).

## 13.4 Các sự kiện Phần cứng (Hardware Events)
Các sự kiện phần cứng đã được giới thiệu trong Chương 4, Các Công cụ Quan trắc, Mục 4.3.9, Các Bộ đếm Phần cứng (PMCs). Chúng thường được triển khai bằng các PMCs, thứ được cấu hình sử dụng các mã cụ thể cho bộ xử lý; ví dụ, các chỉ lệnh nhánh trên các bộ xử lý Intel thường có thể được instrument bằng perf(1) bằng cách sử dụng bộ mô tả sự kiện phần cứng thô "r00c4," viết tắt của các mã đăng ký: umask 0x0 và event select 0xc4. Những mã này được công bố trong các hướng dẫn sử dụng bộ xử lý [Intel 16][AMD 18][ARM 19]; Intel cũng làm cho chúng có sẵn dưới dạng các tệp JSON [Intel 20c].

Bạn không được kỳ vọng phải ghi nhớ những mã này, và bạn sẽ chỉ tham khảo chúng trong các hướng dẫn sử dụng bộ xử lý khi cần thiết. Để dễ sử dụng, perf(1) cung cấp các ánh xạ mà con người có thể đọc được để thay thế. Ví dụ, sự kiện "branch-instructions" hy vọng sẽ ánh xạ tới PMC chỉ lệnh nhánh trên hệ thống của bạn.² Một số tên dễ đọc này có thể thấy được trong danh sách trước đó (các sự kiện phần cứng và PMU).

Có nhiều loại bộ xử lý, và các phiên bản mới được phát hành thường xuyên. Có khả năng là các ánh xạ dễ đọc cho bộ xử lý của bạn chưa có sẵn trong perf(1) hoặc nằm trong một phiên bản kernel mới hơn. Một số PMCs có thể không bao giờ được để lộ qua một tên dễ đọc. Tôi thường chuyển từ các tên dễ đọc sang các bộ mô tả sự kiện thô một khi tôi di chuyển sang các PMCs sâu hơn mà thiếu các ánh xạ. Cũng có các lỗi trong các ánh xạ, và nếu bạn gặp phải một kết quả PMC đáng nghi ngờ, bạn có thể muốn thử bộ mô tả sự kiện thô để kiểm tra lại.

---
² Tôi đã gặp phải các vấn đề với các ánh xạ trong quá khứ, nơi tên dễ đọc không ánh xạ tới đúng PMC. Rất khó để nhận diện điều này chỉ từ kết quả perf(1): bạn cần kinh nghiệm trước đó với PMC và có kỳ vọng về những gì là bình thường, để phát hiện ra sự bất thường. Hãy nhận thức được khả năng này. Với tốc độ cập nhật bộ xử lý, tôi kỳ vọng các lỗi với các ánh xạ trong tương lai cũng vậy.

---

### 13.4.1 Lấy mẫu Tần số (Frequency Sampling)
Khi sử dụng `perf record` với các PMCs, một tần số lấy mẫu mặc định được sử dụng sao cho không phải mọi sự kiện đều được ghi lại. Ví dụ, ghi lại các chu kỳ sự kiện:

```bash
# perf record -vve cycles -a sleep 1
Using CPUID GenuineIntel-6-8E
intel_pt default config: tsc,mtc,mtc_period=3,psb_period=3,pt,branch
------------------------------------------------------------
perf_event_attr:
  size                             112
  { sample_period, sample_freq }   4000
  sample_type                      IP|TID|TIME|CPU|PERIOD
  disabled                         1
  inherit                          1
  mmap                             1
  comm                             1
  freq                             1
[...]
[ perf record: Captured and wrote 3.360 MB perf.data (3538 samples) ]
```

Kết quả cho thấy *frequency sampling* được bật (freq 1) với một tần số lấy mẫu là 4000. Điều này báo cho kernel điều chỉnh tỷ lệ lấy mẫu sao cho có xấp xỉ 4,000 sự kiện mỗi giây cho mỗi CPU được bắt. Điều này là mong muốn, vì một số sự kiện instrument PMC có thể xảy ra hàng tỷ lần mỗi giây (ví dụ: các chu kỳ CPU) và chi phí ghi lại mọi sự kiện đơn lẻ sẽ là cấm đoán.³ Nhưng đây cũng là một điểm yếu: kết quả mặc định của perf(1) (mà không có tùy chọn rất dài dòng -vv) không cho biết rằng tần số lấy mẫu đang được sử dụng, và bạn có thể đang mong đợi được ghi lại tất cả các sự kiện. Tần số sự kiện này chỉ ảnh hưởng đến lệnh phụ record; stat đếm tất cả các sự kiện.

---
³ Mặc dù kernel sẽ điều tiết tốc độ lấy mẫu và đánh rơi các sự kiện nếu chi phí quá cao. Luôn kiểm tra các sự kiện bị mất để xem liệu điều này có xảy ra hay không (ví dụ: kiểm tra các số lượng tóm tắt từ: `perf report -D | tail -20`).

---

Tần số sự kiện có thể được sửa đổi bằng tùy chọn `-F`, hoặc thay đổi thành một chu kỳ (period) sử dụng `-c`, thứ bắt các sự kiện một-trong-mỗi-khoảng-thời-gian (còn được gọi là *overflow sampling*). Như một ví dụ về việc sử dụng `-F`:

`perf record -F 99 -e cycles -a sleep 1`

Lệnh này lấy mẫu tại một tỷ lệ mục tiêu là 99 Hertz (các sự kiện mỗi giây). Nó tương tự như các lệnh một dòng profiling trong Mục 13.2, Các lệnh một dòng: họ đã không chỉ định `-e cycles`, thứ khiến perf(1) mặc định là các chu kỳ nếu PMCs khả dụng, hoặc tới sự kiện cpu-clock nếu không. Xem Mục 13.9.2, Profiling CPU, để biết thêm chi tiết.

Lưu ý rằng có một giới hạn cho tốc độ tần số, cũng như một giới hạn phần trăm sử dụng CPU cho perf(1), thứ có thể được xem và thiết lập bằng sysctl(8):

```bash
# sysctl kernel.perf_event_max_sample_rate
kernel.perf_event_max_sample_rate = 15500
# sysctl kernel.perf_event_cpu_time_max_percent
kernel.perf_event_cpu_time_max_percent = 25
```

Điều này cho thấy tỷ lệ lấy mẫu tối đa trên hệ thống này là 15,500 Hertz, và mức sử dụng CPU tối đa cho phép bởi perf(1) (cụ thể là ngắt PMU) là 25%.

## 13.5 Các sự kiện Phần mềm (Software Events)
Đây là những sự kiện điển hình ánh xạ tới các sự kiện kernel, nhưng được instrument trong phần mềm. Giống như các sự kiện phần cứng, chúng có một tần số lấy mẫu mặc định, điển hình là 4000, sao cho chỉ một tập con được bắt khi sử dụng lệnh phụ record.

Lưu ý sự khác biệt sau đây giữa sự kiện context-switches, và tracepoint tương đương. Bắt đầu với sự kiện phần mềm:

```bash
# perf record -vve context-switches -a -- sleep 1
[...]
------------------------------------------------------------
perf_event_attr:
  type                             1
  size                             112
  config                           0x3
  { sample_period, sample_freq }   4000
  sample_type                      IP|TID|TIME|CPU|PERIOD
[...]
  freq                             1
[...]
[ perf record: Captured and wrote 3.227 MB perf.data (660 samples) ]
```

Kết quả này cho thấy sự kiện phần mềm này đã mặc định là lấy mẫu tần số tại một tốc độ 4000 Hertz. Bây giờ là tracepoint tương đương:

```bash
# perf record -vve sched:sched_switch -a sleep 1
[...]
------------------------------------------------------------
perf_event_attr:
  type                             2
  size                             112
  config                           0x131
  { sample_period, sample_freq }   1
  sample_type                      IP|TID|TIME|CPU|PERIOD|RAW
[...]
[ perf record: Captured and wrote 3.360 MB perf.data (3538 samples) ]
```

Lần này, lấy mẫu chu kỳ được sử dụng (no freq 1), với một giá trị chu kỳ là 1 (tương đương với `-c 1`). Điều này bắt mọi sự kiện. Bạn cũng có thể thực hiện tương tự với các sự kiện phần mềm bằng cách chỉ định `-c 1`, ví dụ:

`perf record -vve context-switches -a -c 1 -- sleep 1`

Hãy cẩn thận với khối lượng ghi lại mọi sự kiện và các chi phí liên quan, đặc biệt là các đợt chuyển đổi ngữ cảnh, thứ có thể diễn ra thường xuyên. Bạn có thể sử dụng `perf stat` để kiểm tra tần suất của chúng: xem Mục 13.8, perf stat.

## 13.6 Các điểm truy vết (Tracepoint Events)
Tracepoints đã được giới thiệu trong Chương 4, Các Công cụ Quan trắc, Mục 4.3.5, Tracepoints, bao gồm các ví dụ về việc instrument chúng bằng cách sử dụng perf(1). Để tóm tắt lại, tôi đã sử dụng tracepoint `block:block_rq_issue` và các ví dụ sau đây.

Truy vết trên toàn hệ thống trong 10 giây và in các sự kiện:
`perf record -e block:block_rq_issue -a sleep 10; perf script`

In các đối số cho tracepoint này và chuỗi định dạng của nó (tóm tắt metadata):
`cat /sys/kernel/debug/tracing/events/block/block_rq_issue/format`

Lọc đĩa I/O chỉ lấy những cái lớn hơn 65536 byte:
`perf record -e block:block_rq_issue --filter 'bytes > 65536' -a sleep 10`

Có các ví dụ bổ sung về perf(1) và tracepoints trong Mục 13.2, Các lệnh Một dòng, và trong các chương khác của cuốn sách này.

Lưu ý rằng `perf list` sẽ hiển thị các sự kiện thăm dò đã được khởi tạo bao gồm kprobes (kernel instrumentation động) dưới dạng "Tracepoint event"; xem Mục 13.7, Probe Events.

## 13.7 Các sự kiện Thăm dò (Probe Events)
perf(1) sử dụng thuật ngữ *probe events* để đề cập đến kprobes, uprobes, và các thăm dò USDT. Những thứ này là "động" và trước tiên phải được khởi tạo trước khi chúng có thể được truy vết: chúng không hiện diện trong kết quả của `perf list` theo mặc định (một số thăm dò USDT có thể hiện diện vì chúng đã được tự động khởi tạo). Sau khi khởi tạo, chúng được liệt kê dưới dạng "Tracepoint event."

### 13.7.1 kprobes
kprobes đã được giới thiệu trong Chương 4, Các Công cụ Quan trắc, Mục 4.3.6, kprobes. Dưới đây là một quy trình điển hình để tạo và sử dụng một kprobe, trong ví dụ này cho việc instrument hàm kernel do_nanosleep():

```bash
perf probe --add do_nanosleep
perf record -e probe:do_nanosleep -a sleep 5
perf script
perf probe --del do_nanosleep
```

Kprobe được tạo ra bằng lệnh phụ `probe` và `--add` (`--add` là tùy chọn), và khi nó không còn cần thiết nữa, nó được xóa bằng cách sử dụng `probe` và `--del`. Dưới đây là kết quả từ chuỗi này, bao gồm việc liệt kê sự kiện thăm dò:

```bash
# perf probe --add do_nanosleep
Added new event:
  probe:do_nanosleep   (on do_nanosleep)

You can now use it in all perf tools, such as:

        perf record -e probe:do_nanosleep -aR sleep 1

# perf list probe:do_nanosleep

List of pre-defined events (to be used in -e):

  probe:do_nanosleep                                 [Tracepoint event]

# perf record -e probe:do_nanosleep -aR sleep 1
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 3.368 MB perf.data (604 samples) ]
# perf script
            sleep 11898 [002] 922215.458572: probe:do_nanosleep: (ffffffff83dbb6b0)
  SendControllerT 15713 [002] 922215.459871: probe:do_nanosleep: (ffffffff83dbb6b0)
  SendControllerT  5460 [001] 922215.459942: probe:do_nanosleep: (ffffffff83dbb6b0)
[...]
```

```bash
# perf probe --del probe:do_nanosleep
Removed event: probe:do_nanosleep
```

Kết quả của perf script cho thấy các lệnh gọi do_nanosleep() đã xảy ra trong khi truy vết, đầu tiên là từ một lệnh gọi sleep(1) (có khả năng là lệnh sleep(1) mà perf(1) đã chạy) theo sau là các lệnh gọi bởi SendControllerT (đã bị lược bớt).

Kết quả trả về của các hàm có thể được instrument bằng cách thêm `%return`:

`perf probe --add do_nanosleep%return`

Việc này sử dụng một kretprobe.

**Các đối số kprobe**
Có ít nhất bốn cách khác nhau để instrument các đối số cho các hàm kernel.

Đầu tiên, nếu kernel debuginfo có sẵn, thì thông tin về các biến hàm, bao gồm các đối số, là sẵn có cho perf(1). Liệt kê các biến cho kprobe do_nanosleep() bằng tùy chọn `--vars`:

```bash
# perf probe --vars do_nanosleep
Available variables at do_nanosleep
        @<do_nanosleep+0>
                enum hrtimer_mode       mode
                struct hrtimer_sleeper* t
```

Kết quả này hiển thị các biến mang tên mode và t, là các đối số đầu vào của do_nanosleep(). Những thứ này có thể được thêm vào khi tạo thăm dò sao cho chúng được ghi lại khi được gọi. Ví dụ, thêm mode:

```bash
# perf probe 'do_nanosleep mode'
[...]
# perf record -e probe:do_nanosleep -a
[...]
# perf script
            svscan  1470 [012] 4731125.216396: probe:do_nanosleep: (ffffffffa8e4e440) mode=0x1
```

Kết quả này hiển thị mode=0x1.

Thứ hai, nếu kernel debuginfo không có sẵn (như tôi thường thấy trong sản xuất), thì các đối số có thể được đọc qua các vị trí đăng ký (register locations) của chúng. Một mẹo là sử dụng một hệ thống giống hệt (cùng phần cứng và kernel) và cài đặt kernel debuginfo trên đó để tham khảo. Hệ thống tham chiếu này sau đó có thể được truy vấn để tìm các vị trí đăng ký bằng các tùy chọn `-n` (dry run) và `-v` (verbose) cho perf probe:

```bash
# perf probe -nv 'do_nanosleep mode'
[...]
Writing event: p:probe/do_nanosleep _text+10806336 mode=%si:x32
[...]
```

Vì nó là một dry run, nó không tạo ra sự kiện. Kết quả hiển thị vị trí của biến mode (được tô đậm): nó nằm trong thanh ghi `%si` và được in dưới dạng một số thập lục phân 32-bit (`x32`). Cú pháp này được giải thích trong phần tiếp theo về uprobes. Bây giờ bạn có thể sử dụng điều này trên hệ thống thiếu debuginfo bằng cách sao chép và dán chuỗi khai báo mode (`mode=%si:x32`):

```bash
# perf probe 'do_nanosleep mode=%si:x32'
[...]
# perf record -e probe:do_nanosleep -a
[...]
# perf script
            svscan  1470 [000] 4732120.231245: probe:do_nanosleep: (ffffffffa8e4e440) mode=0x1
```

Điều này chỉ hoạt động nếu các hệ thống có cùng phiên bản bộ xử lý ABI và kernels, nếu không thì các vị trí đăng ký sai có thể được instrument.

Thứ ba, nếu bạn biết bộ xử lý ABI, bạn có thể tự mình xác định các vị trí đăng ký. Một ví dụ cho uprobes được đưa ra trong phần tiếp theo.

Thứ tư, có một nguồn thông tin gỡ lỗi kernel mới: BPF type format (BTF). Điều này có nhiều khả năng có sẵn theo mặc định, và một phiên bản perf(1) tương lai nên hỗ trợ nó như một nguồn debuginfo thay thế.

Đối với kretprobes, giá trị trả về có thể được đọc bằng cách sử dụng biến đặc biệt `$retval`:

`perf probe 'do_nanosleep%return $retval'`

Xem mã nguồn kernel để xác định giá trị trả về chứa những gì.

### 13.7.2 uprobes
uprobes đã được giới thiệu trong Chương 4, Các Công cụ Quan trắc, Mục 4.3.7, uprobes. uprobes được tạo ra tương tự như kprobes khi sử dụng perf(1). Ví dụ, để tạo một uprobe cho hàm mở tập tin của libc, fopen(3):

```bash
# perf probe -x /lib/x86_64-linux-gnu/libc.so.6 --add fopen
Added new event:
  probe_libc:fopen     (on fopen in /lib/x86_64-linux-gnu/libc-2.27.so)
```

Bây giờ bạn có thể sử dụng nó trong tất cả các công cụ perf, chẳng hạn như:

`perf record -e probe_libc:fopen -aR sleep 1`

Đường dẫn nhị phân được chỉ định bằng `-x`. uprobe, mang tên probe_libc:fopen, bây giờ có thể được sử dụng với `perf record` để ghi lại các sự kiện. Khi bạn hoàn thành với uprobe, bạn có thể xóa nó bằng cách sử dụng `--del`:

```bash
# perf probe --del probe_libc:fopen
Removed event: probe_libc:fopen
```

Kết quả trả về của hàm có thể được instrument bằng cách thêm `%return`:

`perf probe -x /lib/x86_64-linux-gnu/libc.so.6 --add fopen%return`

Việc này sử dụng một uretprobe.

**Các đối số uprobe**
Nếu hệ thống của bạn có debuginfo cho file nhị phân đích, thì thông tin về biến, bao gồm các đối số, có thể được liệt kê bằng cách sử dụng `--vars`:

```bash
# perf probe -x /lib/x86_64-linux-gnu/libc.so.6 --vars fopen
Available variables at fopen
        @<_IO_vfscanf+15344>
                char*   filename
                char*   mode
```

Kết quả cho thấy fopen(3) có các biến filename và mode. Những thứ này có thể được thêm vào khi tạo thăm dò:

`perf probe -x /lib/x86_64-linux-gnu/libc.so.6 --add 'fopen filename mode'`

Debuginfo có thể được cung cấp qua một gói -dbg hoặc -dbgsym. Nếu điều đó không có sẵn trên hệ thống mục tiêu nhưng có trên một hệ thống khác, hệ thống khác có thể được sử dụng như một hệ thống tham chiếu, như đã chỉ ra trong phần trước về kprobes.

Thậm chí nếu debuginfo không có sẵn ở bất cứ đâu, bạn vẫn có các tùy chọn. Một là biên dịch lại phần mềm với debuginfo (nếu phần mềm là mã nguồn mở). Một tùy chọn khác là tìm ra các vị trí thanh ghi của chính bạn, dựa trên bộ xử lý ABI. Ví dụ sau đây là cho x86_64:

```bash
# perf probe -x /lib/x86_64-linux-gnu/libc.so.6 --add 'fopen filename=+0(%di):string mode=%si:u8'
[...]
# perf record -e probe_libc:fopen -a
[...]
```

```bash
# perf script
            run 28882 [013] 4503285.383830: probe_libc:fopen: (7fbe130e6e30) filename="/etc/nsswitch.conf" mode=147
            run 28882 [013] 4503285.383997: probe_libc:fopen: (7fbe130e6e30) filename="/etc/passwd" mode=17
       setuidgid 28882 [013] 4503285.384447: probe_libc:fopen: (7fed1ad56e30) filename="/etc/nsswitch.conf" mode=147
       setuidgid 28882 [013] 4503285.384589: probe_libc:fopen: (7fed1ad56e30) filename="/etc/passwd" mode=17
            run 28883 [014] 4503285.392096: probe_libc:fopen: (7f9be2f55e30) filename="/etc/nsswitch.conf" mode=147
            run 28883 [014] 4503285.392251: probe_libc:fopen: (7f9be2f55e30) filename="/etc/passwd" mode=17
          mkdir 28884 [015] 4503285.392913: probe_libc:fopen: (7fad6ea0be30) filename="/proc/filesystems" mode=22
          chown 28885 [015] 4503285.393536: probe_libc:fopen: (7efcd22d5e30) filename="/etc/nsswitch.conf" mode=147
[...]
```

Kết quả bao gồm một số lệnh gọi fopen(3), hiển thị các tên tệp của /etc/nsswitch.conf, /etc/passwd, v.v.

Phân tích cú pháp tôi đã sử dụng:
- **filename=:** Đây là một bí danh ("filename") được sử dụng để chú giải kết quả.
- **%di, %si:** Trên x86_64, các thanh ghi chứa hai đối số hàm đầu tiên, theo bộ ABI AMD64 [Matz 13].
- **+0(...):** Giải tham chiếu (Dereference) nội dung tại độ dời (offset) không. Nếu không có điều này, chúng ta sẽ vô tình in địa chỉ dưới dạng một chuỗi, thay vì nội dung của địa chỉ dưới dạng một chuỗi.
- **:string:** In giá trị này dưới dạng một chuỗi.
- **:u8:** In giá trị này dưới dạng một số nguyên 8-bit không dấu.

Cú pháp được tài liệu hóa trong trang man perf-probe(1).

Đối với uretprobe, giá trị trả về có thể được đọc bằng cách sử dụng `$retval`:

`perf probe -x /lib/x86_64-linux-gnu/libc.so.6 --add 'fopen%return $retval'`

Xem mã nguồn ứng dụng để xác định giá trị trả về chứa những gì.

Mặc dù uprobes có thể cung cấp khả năng hiển thị vào các thành phần nội bộ ứng dụng, chúng là một giao diện không ổn định vì chúng instrument trực tiếp file nhị phân, thứ có thể thay đổi giữa các phiên bản phần mềm. Các thăm dò USDT được ưa chuộng hơn bất cứ khi nào có sẵn.

### 13.7.3 USDT
Các thăm dò USDT đã được giới thiệu trong Chương 4, Các Công cụ Quan trắc, Mục 4.3.8, USDT. Những thứ này cung cấp một giao diện ổn định cho việc truy vết các sự kiện.

Với một file nhị phân có các thăm dò USDT,⁴ perf(1) có thể nhận biết chúng bằng cách sử dụng lệnh phụ `buildid-cache`. Ví dụ, cho một file nhị phân Node.js được biên dịch với các thăm dò USDT (được xây dựng bằng cách sử dụng: `./configure --with-dtrace`):

```bash
# perf buildid-cache --add $(which node)
```

Các thăm dò USDT sau đó có thể được nhìn thấy trong kết quả của `perf list`:

```bash
# perf list | grep sdt_node
  sdt_node:gc__done                                  [SDT event]
  sdt_node:gc__start                                 [SDT event]
  sdt_node:http__client__request                     [SDT event]
  sdt_node:http__client__response                    [SDT event]
  sdt_node:http__server__request                     [SDT event]
  sdt_node:http__server__response                    [SDT event]
  sdt_node:net__server__connection                   [SDT event]
  sdt_node:net__stream__end                          [SDT event]
```

Tại thời điểm này, chúng là các sự kiện SDT (các sự kiện truy vết tĩnh được định nghĩa tĩnh): metadata mô tả vị trí của sự kiện trong văn bản hướng dẫn của chương trình. Để thực sự instrument chúng, các sự kiện phải được tạo ra theo cùng một cách như uprobes từ phần trước (các thăm dò USDT cũng sử dụng uprobes để instrument các vị trí USDT).⁵ Ví dụ, cho `sdt_node:http__server__request`:

```bash
# perf probe sdt_node:http__server__request
Added new event:
  sdt_node:http__server__request (on %http__server__request in
/home/bgregg/Build/node-v12.4.0/out/Release/node)

You can now use it in all perf tools, such as:

        perf record -e sdt_node:http__server__request -aR sleep 1

# perf list | grep http__server__request
  sdt_node:http__server__request                     [Tracepoint event]
  sdt_node:http__server__request                     [SDT event]
```

---
⁴ Bạn có thể chạy `readelf -n` trên file nhị phân để kiểm tra sự tồn tại của các thăm dò USDT: chúng được liệt kê trong phần ghi chú ELF.
⁵ Trong tương lai bước này có thể trở nên không cần thiết: lệnh perf record sau đây có thể tự động quảng bá các sự kiện SDT sang các tracepoints khi cần thiết.

---

Lưu ý rằng sự kiện hiện hiển thị dưới dạng cả sự kiện SDT (USDT metadata) và một Tracepoint event (một sự kiện truy vết có thể được instrument bằng cách sử dụng perf(1) và các công cụ khác). Nó có thể cảm thấy lạ khi thấy hai mục cho cùng một thứ, nhưng nó nhất quán với cách các sự kiện khác hoạt động. Có một tracepoint cho cùng một thứ, ngoại trừ perf(1) không liệt kê các tracepoints, nó chỉ liệt kê các tracepoint events tương ứng (nếu chúng tồn tại).⁶

Ghi lại sự kiện USDT:

```bash
# perf record -e sdt_node:http__server__request -a
^C[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 3.924 MB perf.data (2 samples) ]
# perf script
            node 16282 [006] 510375.595203: sdt_node:http__server__request:
(55c3d8b03530) arg1=140725176825920 arg2=140725176825888 arg3=140725176829208
arg4=39090 arg5=140725176827096 arg6=140725176826040 arg7=20
            node 16282 [006] 510375.844040: sdt_node:http__server__request:
(55c3d8b03530) arg1=140725176825920 arg2=140725176825888 arg3=140725176829208
arg4=39092 arg5=140725176827096 arg6=140725176826040 arg7=20
```

Kết quả cho thấy hai thăm dò sdt_node:http__server__request đã được kích hoạt trong khi ghi lại. Nó cũng đã in các đối số cho thăm dò USDT, nhưng một số trong số này là các cấu trúc và các chuỗi, vì vậy perf(1) đã in chúng dưới dạng các địa chỉ con trỏ. Có thể truyền các đối số tới loại chính xác khi tạo thăm dò; ví dụ, để cast đối số thứ ba dưới dạng một chuỗi mang tên "address":

`perf probe --add 'sdt_node:http__server__request address=+0(arg3):string'`

Tại thời điểm viết bài, điều này không hoạt động.

Một vấn đề phổ biến, đã được sửa kể từ Linux 4.20, là một số thăm dò USDT yêu cầu một đèn hiệu (semaphore) trong không gian địa chỉ tiến trình được tăng lên để kích hoạt chúng một cách chính xác. `sdt_node:http__server__request` là một thăm dò như vậy, và không tăng đèn hiệu nó sẽ không ghi lại bất kỳ sự kiện nào.

---
⁶ Tài liệu kernel có tuyên bố rằng một số tracepoints có thể không có các sự kiện truy vết tương ứng, mặc dù tôi chưa gặp trường hợp nào về điều này.

---

## 13.8 perf stat
Lệnh phụ perf stat đếm các sự kiện. Điều này có thể được sử dụng để đo lường tốc độ của các sự kiện, hoặc để kiểm tra xem một sự kiện có đang xảy ra hay không. perf stat là hiệu quả: nó đếm các sự kiện phần mềm trong ngữ cảnh kernel và các sự kiện phần cứng bằng cách sử dụng các thanh ghi PMC. Điều này làm cho nó phù hợp để đánh giá chi phí của một lệnh phụ perf record tốn kém hơn bằng cách kiểm tra tốc độ sự kiện bằng perf stat trước.

Ví dụ, đếm tracepoint sched:sched_switch (sử dụng `-e` cho sự kiện), trên toàn hệ thống (`-a`) và trong một giây (`sleep 1`: một lệnh giả):

```bash
# perf stat -e sched:sched_switch -a -- sleep 1
 Performance counter stats for 'system wide':

             5,705      sched:sched_switch

       1.001892925 seconds time elapsed
```

Điều này cho thấy tracepoint sched:sched_switch đã được kích hoạt 5,705 lần trong một giây đó.

Tôi thường sử dụng dấu tách shell “--” giữa các tùy chọn lệnh perf(1) và lệnh giả mà nó chạy, mặc dù nó không hoàn toàn cần thiết trong trường hợp này.

Các phần sau đây giải thích các tùy chọn và ví dụ sử dụng.

### 13.8.1 Các tùy chọn (Options)
Lệnh phụ stat hỗ trợ nhiều tùy chọn, bao gồm:
- **-a:** Ghi lại trên tất cả các CPUs (điều này đã trở thành mặc định trong Linux 4.11)
- **-e event:** Ghi lại (các) sự kiện này
- **--filter filter:** Thiết lập một bộ lọc Boolean cho một sự kiện
- **-p PID:** Chỉ ghi lại PID này
- **-t TID:** Chỉ ghi lại ID luồng (thread ID) này
- **-G cgroup:** Chỉ ghi lại cgroup này (được sử dụng cho các containers)
- **-A:** Hiển thị các số lượng cho mỗi CPU
- **-I interval_ms:** In kết quả sau mỗi khoảng thời gian (mili giây)
- **-v:** Hiển thị các thông điệp rườm rà; **-vv** để có thêm nhiều thông điệp

Các sự kiện có thể là tracepoints, software events, hardware events, kprobes, uprobes, và USDT probes (xem các Mục 13.3 tới 13.7). Các ký tự đại diện (wildcards) có thể được sử dụng để khớp nhiều sự kiện của kiểu globbing tệp (“*” khớp với bất cứ thứ gì, và “?” khớp với bất kỳ một ký tự nào). Ví dụ, phần sau đây khớp với tất cả các tracepoints thuộc loại sched:

`# perf stat -e 'sched:*' -a`

Nhiều tùy chọn `-e` có thể được sử dụng để khớp nhiều mô tả sự kiện. Để đếm cả hai sched và block tracepoints, bất kỳ cách nào sau đây cũng có thể được sử dụng:

`# perf stat -e 'sched:*' -e 'block:*' -a`
`# perf stat -e 'sched:*,block:*' -a`

Nếu không có sự kiện nào được chỉ định, perf stat sẽ mặc định là các PMCs kiến trúc: bạn có thể xem một ví dụ trong Chương 4, Các Công cụ Quan trắc, Mục 4.3.9, Các Bộ đếm Phần cứng (PMCs).

### 13.8.2 Các thống kê theo Khoảng thời gian (Interval Statistics)
Các thống kê theo khoảng thời gian có thể được in bằng tùy chọn `-I`. Ví dụ, in tracepoint sched:sched_switch sau mỗi 1000 mili giây:

```bash
# perf stat -e sched:sched_switch -a -I 1000
#           time             counts unit events
     1.000791768              5,308      sched:sched_switch
     2.001650037              4,879      sched:sched_switch
     3.002348559              5,112      sched:sched_switch
     4.003017555              5,335      sched:sched_switch
     5.003760359              5,300      sched:sched_switch
^C   5.217339333              1,256      sched:sched_switch
```

Cột counts hiển thị số lượng các sự kiện kể từ khoảng thời gian trước đó. Việc duyệt qua kết quả này có thể cho thấy sự biến động theo thời gian. Dòng cuối cùng hiển thị số lượng giữa dòng trước đó và thời điểm tôi nhấn Ctrl-C để kết thúc perf(1). Thời gian đó là 0.214 giây, như được thấy bởi delta trong cột thời gian.

### 13.8.3 Cân bằng cho mỗi CPU (Per-CPU Balance)
Sự cân bằng trên các CPUs có thể được kiểm tra bằng tùy chọn `-A`:

```bash
# perf stat -e sched:sched_switch -a -A -I 1000
#           time CPU                counts unit events
     1.000351429 CPU0                1,154      sched:sched_switch
     1.000351429 CPU1                  555      sched:sched_switch
     1.000351429 CPU2                  492      sched:sched_switch
     1.000351429 CPU3                  925      sched:sched_switch
[...]
```

Lệnh này in riêng biệt delta sự kiện trên mỗi khoảng thời gian cho từng CPU logic.

Cũng có các tùy chọn `--per-socket` và `--per-core` cho socket CPU và tổng hợp lõi.

### 13.8.4 Bộ lọc Sự kiện (Event Filters)
Một bộ lọc có thể được cung cấp cho một số loại sự kiện (các sự kiện Tracepoint) để kiểm tra các đối số sự kiện với một biểu thức Boolean. Sự kiện sẽ chỉ được đếm nếu biểu thức là đúng. Ví dụ, đếm tracepoint sched:sched_switch khi PID trước đó là 25467:

```bash
# perf stat -e sched:sched_switch --filter 'prev_pid == 25467' -a -I 1000
#           time             counts unit events
     1.000346518                131      sched:sched_switch
     2.000937838                145      sched:sched_switch
     3.001370500                 11      sched:sched_switch
     4.001905444                217      sched:sched_switch
[...]
```

Xem Các đối số Tracepoint (Tracepoint Arguments), Chương 4, Các Công cụ Quan trắc, Mục 4.3.5, Tracepoints, để biết giải thích về những đối số này. Chúng là tùy chỉnh cho từng sự kiện, và có thể được liệt kê từ tệp format trong /sys/kernel/debug/tracing/events.

### 13.8.5 Các thống kê Bóng (Shadow Statistics)
perf(1) có một loạt các thống kê bóng (shadow statistics) sẽ được in khi các tổ hợp nhất định của các sự kiện được instrument. Ví dụ, khi instrument các PMCs cho các chu kỳ (cycles) và các chỉ lệnh (instructions), thống kê *instructions per cycle* (IPC) được in:

```bash
# perf stat -e cycles,instructions -a
^C
 Performance counter stats for 'system wide':

     2,895,806,892      cycles
     6,452,798,206      instructions              #    2.23  insn per cycle

       1.040093176 seconds time elapsed
```

Trong kết quả này, IPC là 2.23. Những thống kê bóng này được in ở bên phải, sau một dấu thăng (#). Kết quả của `perf stat` không có sự kiện nào sẽ có một vài thống kê bóng này (xem Chương 4, Các Công cụ Quan trắc, Mục 4.3.9, Các Bộ đếm Phần cứng (PMCs), cho một ví dụ).

Để kiểm tra các sự kiện chi tiết hơn, `perf record` có thể được sử dụng để bắt chúng.

## 13.9 perf record
Lệnh phụ perf record ghi lại các sự kiện vào một tập tin để phân tích sau này. Các sự kiện được chỉ định sau `-e`, và nhiều sự kiện có thể được ghi lại đồng thời (hoặc bằng cách sử dụng nhiều `-e` hoặc được phân tách bằng dấu phẩy).

Theo mặc định, tên tệp kết quả là perf.data. Ví dụ:

```bash
# perf record -e sched:sched_switch -a
^C[ perf record: Woken up 9 times to write data ]
[ perf record: Captured and wrote 6.060 MB perf.data (23526 samples) ]
```

Lưu ý rằng kết quả bao gồm kích thước của tệp perf.data (6.060 Mbytes), số lượng mẫu nó chứa (23,526), và số lần perf(1) thức dậy để ghi dữ liệu (9 lần). Dữ liệu được chuyển từ kernel tới không gian người dùng qua các buffer ring cho mỗi CPU, và để giữ các chi phí context-switch ở mức tối thiểu, perf(1) được đánh thức một cách không thường xuyên và số lượng lần động để đọc chúng.

Lệnh trước đó đã ghi lại cho đến khi nhấn Ctrl-C. Một lệnh sleep(1) giả (hoặc bất kỳ lệnh nào) có thể được sử dụng để thiết lập thời lượng (như trường hợp của perf stat trước đó). Ví dụ:

`perf record -e tracepoint -a -- sleep 1`

Lệnh này ghi lại tracepoint trên toàn hệ thống (`-a`) chỉ trong 1 giây.

### 13.9.1 Các tùy chọn (Options)
Lệnh phụ record hỗ trợ nhiều tùy chọn, bao gồm:
- **-a:** Ghi lại trên tất cả các CPUs (điều này đã trở thành mặc định trong Linux 4.11)
- **-e event:** Ghi lại (các) sự kiện này
- **--filter filter:** Thiết lập một biểu thức bộ lọc Boolean cho một sự kiện
- **-p PID:** Ghi lại PID này duy nhất
- **-t TID:** Ghi lại ID luồng này duy nhất
- **-G cgroup:** Ghi lại cgroup này duy nhất (được sử dụng cho các containers)
- **-g:** Ghi lại các vết ngăn xếp (stack traces)
- **--call-graph mode:** Ghi lại các vết ngăn xếp bằng một phương thức nhất định (fp, dwarf, hoặc lbr)
- **-o file:** Thiết lập tệp kết quả
- **-v:** Hiển thị các thông điệp rườm rà; **-vv** để có thêm nhiều thông điệp

Các sự kiện tương tự có thể được ghi lại như với `perf stat` và được in trực tiếp (khi các sự kiện xảy ra) bằng `perf trace`.

### 13.9.2 Tạo hồ sơ CPU (CPU Profiling)
Một mục đích sử dụng thường xuyên của perf(1) là làm trình tạo hồ sơ CPU. Ví dụ profiling sau đây lấy mẫu các vết ngăn xếp trên tất cả các CPUs tại 99 Hertz trong 30 giây:

`perf record -F 99 -a -g -- sleep 30`

Sự kiện đã không được chỉ định (không có `-e`), vì vậy perf(1) sẽ mặc định là sự kiện đầu tiên trong số những sự kiện khả dụng (nhiều cái sử dụng *precise events*, được giới thiệu trong Chương 4, Các Công cụ Quan trắc, Mục 4.3.9, Các Bộ đếm Phần cứng (PMCs)):
1. **cycles:ppp:** Lấy mẫu tần số dựa trên chu kỳ CPU với mức precise được thiết lập về zero skid
2. **cycles:pp:** Lấy mẫu tần số dựa trên chu kỳ CPU với mức precise được thiết lập về yêu cầu zero skid (thứ có thể không phải là zero trong thực tế)
3. **cycles:p:** Lấy mẫu tần số dựa trên chu kỳ CPU với mức precise được thiết lập về yêu cầu hằng số skid
4. **cycles:** Lấy mẫu tần số dựa trên chu kỳ CPU (không chính xác)
5. **cpu-clock:** Lấy mẫu tần số CPU dựa trên phần mềm

Thứ tự ưu tiên chọn cơ chế profiling CPU chính xác nhất có sẵn. Cú pháp `:ppp`, `:pp`, và `:p` kích hoạt các chế độ lấy mẫu sự kiện chính xác, và có thể được áp dụng cho các sự kiện khác (ngoài các chu kỳ) có hỗ trợ chúng. Các sự kiện có thể hỗ trợ các cấp độ precise khác nhau. Trên Intel, precise events sử dụng PEBS; trên AMD, họ sử dụng IBS. Những thứ này đã được định nghĩa trong Mục 4.3.9, dưới tiêu đề PMC Challenges.

### 13.9.3 Duyệt Ngăn xếp (Stack Walking)
Thay vì sử dụng `-g` để chỉ định ghi lại các vết ngăn xếp, tùy chọn cấu hình max-stack có thể được sử dụng. Nó có hai lợi ích: độ sâu tối đa của ngăn xếp có thể được chỉ định, và các thiết lập khác nhau có thể được sử dụng cho các sự kiện khác nhau. Ví dụ:

`# perf record -e sched:sched_switch/max-stack=5/,sched:sched_wakeup/max-stack=1/ \ -a -- sleep 1`

Lệnh này ghi lại các sự kiện sched_switch với các ngăn xếp 5-khung hình, và các sự kiện sched_wakeup chỉ với ngăn xếp 1-khung hình.

Lưu ý rằng nếu các vết ngăn xếp xuất hiện dưới dạng bị hỏng, điều đó có thể là do phần mềm không tôn trọng con trỏ khung hình (frame pointer register). Điều này đã được thảo luận trong Chương 5, Các ứng dụng, Mục 5.6.2, Missing Stacks. Bên cạnh việc biên dịch lại phần mềm với các con trỏ khung hình (ví dụ: gcc(1) `-fno-omit-frame-pointer`), một phương thức duyệt ngăn xếp khác cũng có thể hoạt động, được lựa chọn bằng cách sử dụng `--call-graph`. Các tùy chọn bao gồm:
- **--call-graph dwarf:** Chọn duyệt ngăn xếp dựa trên debuginfo, thứ yêu cầu debuginfo cho file thực thi phải có sẵn (đối với một số phần mềm, việc này được thực hiện bằng cách cài đặt một gói với tên kết thúc bằng "-dbgsym" hoặc "-dbg").
- **--call-graph lbr:** Chọn duyệt ngăn xếp Last Branch Record (LBR) của Intel, một phương thức do bộ xử lý cung cấp (mặc dù nó thường giới hạn ở độ sâu ngăn xếp chỉ 16 khung hình,⁷ vì vậy tính hữu ích của nó cũng bị hạn chế).
- **--call-graph fp:** Chọn duyệt ngăn xếp dựa trên con trỏ khung hình (mặc định).

Duyệt ngăn xếp dựa trên con trỏ khung hình được mô tả trong Chương 3, Hệ điều hành, Mục 3.2.7, Stacks. Các loại khác (dwarf, LBR, và ORC) được mô tả trong Chương 2, Công nghệ, Mục 2.4, Stack Trace Walking, của *BPF Performance Tools* [Gregg 19].

Sau khi ghi lại các sự kiện, chúng có thể được kiểm tra bằng cách sử dụng `perf report` hoặc `perf script`.

---
⁷ Độ sâu ngăn xếp 16 kể từ Haswell, và 32 kể từ Skylake.

---

## 13.10 perf report
Lệnh phụ perf report tóm tắt nội dung của tệp perf.data. Các tùy chọn bao gồm:
- **--tui:** Sử dụng giao diện TUI (mặc định)
- **--stdio:** Phát ra một báo cáo văn bản
- **-i file:** Tập tin đầu vào

Cũng có thể tóm tắt perf.data bằng các công cụ bên ngoài. Những công cụ này có thể xử lý kết quả perf script, được bao quát trong Mục 13.11, perf script. Bạn có thể thấy `perf report` là đủ trong nhiều tình huống, và các công cụ bên ngoài chỉ cần thiết khi cần thiết. perf report tóm tắt bằng cách sử dụng một giao diện văn bản người dùng tương tác (TUI) hoặc một báo cáo văn bản (STDIO).

### 13.10.1 TUI
Ví dụ, tạo hồ sơ CPU của con trỏ chỉ lệnh tại 99 Hertz trong 10 giây (không có vết ngăn xếp) và khởi chạy TUI:

```bash
# perf record -F 99 -a -- sleep 30
[ perf record: Woken up 193 times to write data ]
[ perf record: Captured and wrote 48.916 MB perf.data (11880 samples) ]
# perf report
Samples: 11K of event 'cpu-clock:pppH', Event count (approx.): 11999998800
Overhead  Command          Shared Object               Symbol
  21.10%  swapper           [kernel.vmlinux]            [k] native_safe_halt
   6.39%  mysqld            [kernel.vmlinux]            [k] _raw_spin_unlock_irqrest
   4.66%  mysqld            mysqld                      [.] _Z8ut_delaym
   2.64%  mysqld            [kernel.vmlinux]            [k] finish_task_switch
   2.59%  oltp_read_write   [kernel.vmlinux]            [k] finish_task_switch
   2.03%  mysqld            [kernel.vmlinux]            [k] exit_to_usermode_loop
   1.68%  mysqld            mysqld                      [.] _Z15row_search_mvccPh15pag
   1.40%  oltp_read_write   [kernel.vmlinux]            [k] _raw_spin_unlock_irqrest
[...]
```

`perf report` là một giao diện tương tác nơi bạn có thể điều hướng dữ liệu, chọn các hàm và luồng để biết thêm chi tiết.

### 13.10.2 STDIO
Cùng một hồ sơ CPU đã được chỉ ra trong Mục 13.1, Tổng quan về các Lệnh phụ, sử dụng báo cáo dựa trên văn bản (`--stdio`). Nó không tương tác, nhưng phù hợp để chuyển hướng tới một tệp sao cho bản tóm tắt đầy đủ có thể được lưu lại dưới dạng văn bản. Những báo cáo văn bản độc lập như vậy có thể hữu ích cho việc chia sẻ với những người khác qua hệ thống chat, email, và các hệ thống hỗ trợ yêu cầu. Tôi thường sử dụng `-n` để bao gồm một cột số lượng mẫu.

Dưới dạng một ví dụ STDIO khác, phần sau đây chỉ ra một hồ sơ CPU với các vết ngăn xếp (`-g`):

```bash
# perf record -F 99 -a -g -- sleep 30
[ perf record: Woken up 8 times to write data ]
[ perf record: Captured and wrote 2.282 MB perf.data (11880 samples) ]
# perf report --stdio
[...]
# Children      Self  Command          Shared Object               Symbol
# ........  ........  ................  ..........................  ...........................
#
    50.45%     0.00%  mysqld            libpthread-2.27.so          [.] start_thread
            |
            ---start_thread
               |
               |--44.75%--pfs_spawn_thread
               |          |
               |           --44.70%--handle_connection
               |                     |
               |                      --44.55%--_Z10do_commandP3THD
               |                                |
               |                                |--42.93%--_Z16dispatch_commandP3THD
               |                                |          |
               |                                |           --40.92%--_Z19mysqld_stm
               |                                |                     |
[...]
```

Các mẫu vết ngăn xếp được hợp nhất thành một phân cấp, bắt đầu từ hàm gốc (root function) ở bên trái và di chuyển xuống thông qua các hàm con và sang bên phải. Hàm ngoài cùng bên phải là hàm tại thời điểm xảy ra sự kiện (trong trường hợp này, tiến trình mysqld (daemon) đã chạy start_thread(), thứ đã gọi pfs_spawn_thread(), thứ đã gọi handle_connection(), và cứ tiếp tục như vậy. Các hàm ngoài cùng bên phải bị lược bớt trong kết quả này.

Kiểu sắp xếp từ-trái-sang-phải này được gọi là *caller* bởi perf(1). Bạn có thể lật cái này sang kiểu sắp xếp *callee*, nơi hàm sự kiện ở bên trái và tổ tiên của nó ở bên phải bằng cách sử dụng: `-g callee` (nó là mặc định; perf(1) đã chuyển sang kiểu sắp xếp caller trong Linux 4.4).

## 13.11 perf script
Lệnh phụ perf script theo mặc định in từng mẫu từ perf.data, và hữu ích cho việc phát hiện các mẫu theo thời gian thứ có thể bị mất trong một bản báo cáo tóm tắt. Kết quả của nó có thể được sử dụng để tạo ra các flame graphs, và nó cũng có khả năng chạy các *trace scripts* thứ tự động hóa việc ghi lại và báo cáo các sự kiện theo các cách tùy chỉnh. Những chủ đề này được tóm tắt trong phần này.

Để bắt đầu, phần sau đây chỉ ra kết quả từ hồ sơ CPU trước đó, thứ đã được thu thập mà không có các vết ngăn xếp:

```bash
# perf script
          mysqld  8631 [000] 4142044.582702:   10101010 cpu-clock:pppH:
c08fd9 _Z19close_thread_tablesP3THD+0x49 (/usr/sbin/mysqld)
          mysqld  8619 [001] 4142044.582711:   10101010 cpu-clock:pppH:
79f81d _ZN5Field10make_fieldEP10Send_field+0x1d (/usr/sbin/mysqld)
          mysqld 22432 [002] 4142044.582713:   10101010 cpu-clock:pppH:
ffffffff95530302 get_futex_key_refs.isra.12+0x32 (/lib/modules/5.4.0-rc8-virtua...
[...]
```

Các trường kết quả là, cùng với nội dung trường từ dòng đầu tiên của kết quả:
- **Tên tiến trình (Process name):** mysqld
- **ID Luồng (Thread ID):** 8631
- **ID CPU (CPU ID):** [000]
- **Dấu thời gian (Timestamp):** 4142044.582702 (giây)
- **Khoảng thời gian (Period):** 10101010 (được suy ra từ -F 99); được bao gồm trong một số chế độ lấy mẫu
- **Tên sự kiện (Event name):** cpu-clock:pppH
- **Các đối số sự kiện (Event arguments):** Những trường này theo sau là các đối số sự kiện, thứ đặc thù cho sự kiện. Đối với sự kiện cpu-clock, chúng là con trỏ chỉ lệnh, tên hàm và độ dời (offset), và tên phân đoạn (segment name). Đối với nguồn gốc của những thứ này, xem Chương 4, Mục 4.3.5, dưới tiêu đề Tracepoints Arguments và Format String.

Những trường kết quả này tình cờ là mặc định hiện tại cho sự kiện này, nhưng có thể thay đổi trong phiên bản sau này của perf(1). Các sự kiện khác không bao gồm trường period.

Vì việc tạo ra kết quả nhất quán có thể là quan trọng, đặc biệt cho việc xử lý hậu kỳ, bạn có thể sử dụng tùy chọn `-F` để chỉ định các trường. Tôi thường sử dụng nó cho việc bao gồm ID tiến trình, thứ bị thiếu từ bộ trường mặc định. Tôi cũng khuyên bạn nên thêm `--header` để bao gồm các metadata của perf.data. Ví dụ, hiển thị một hồ sơ CPU với các vết ngăn xếp:

```bash
# perf script --header -F comm,pid,tid,cpu,time,event,ip,sym,dso,trace
# ========
# captured on          : Sun Jan  5 23:43:56 2020
# header version       : 1
# data offset          : 264
# data size            : 2393000
# feat offset          : 2393264
# hostname : bgregg-mysql
# os release : 5.4.0
# perf version : 5.4.0
# arch : x86_64
# nrcpus online : 4
# nrcpus avail : 4
# cpudesc : Intel(R) Xeon(R) Platinum 8175M CPU @ 2.50GHz
# cpuid : GenuineIntel,6,85,4
# total memory : 15923672 kB
# cmdline : /usr/bin/perf record -F 99 -a -g -- sleep 30
# event : name = cpu-clock:pppH, , id = { 5997, 5998, 5999, 6000 }, type = 1, size =
112, { sample_period, sample_freq } = 99, sample_ty
[...]
# ========
#
mysqld 21616/8583  [000] 4142769.671581: cpu-clock:pppH:
                                  c36299 [unknown] (/usr/sbin/mysqld)
                                  c3bad4 _ZN13QEP_tmp_table8end_sendEv (/usr/sbin/mysqld)
                                  c3c1a5 _Z13sub_select_opp4JOINP7QEP_TABb (/usr/sbin/mysqld)
                                  c346a8 _ZN4JOIN4execEv (/usr/sbin/mysqld)
                                  ca735a _Z12handle_queryP3THDP12Query_resultyy
[...]
```

Kết quả bao gồm tiêu đề, được tiền tố với “#”, mô tả hệ thống và lệnh perf(1) được sử dụng để tạo tệp perf.data. Nếu bạn lưu kết quả này vào tập tin để dùng sau, bạn sẽ mừng vì đã bao gồm tiêu đề, vì nó cung cấp rất nhiều thông tin mà bạn có thể cần sau này. Những tệp này có thể được đọc bởi các công cụ khác cho việc hình ảnh hóa, bao gồm cả flame graphs.

### 13.11.1 Flame Graphs
Flame graphs hình ảnh hóa các vết ngăn xếp. Trong khi thường được sử dụng cho các hồ sơ CPU, chúng có thể hình ảnh hóa bất kỳ tập hợp các vết ngăn xếp nào được thu thập bởi perf(1), bao gồm cả các sự kiện switch ngữ cảnh (context switch) để xem lý do tại sao các luồng rời khỏi CPU, và trên việc tạo khối I/O để xem những đường dẫn mã nào đang tạo ra I/O đĩa.

Hai triển khai flame graph được sử dụng phổ biến (của riêng tôi, và một phiên bản d3) hình ảnh hóa kết quả của `perf script`. Hỗ trợ flame graph trong perf(1) đã được thêm vào trong Linux 5.8. Các bước để tạo flame graphs bằng cách sử dụng perf(1) được bao gồm trong Chương 6, CPUs, Mục 6.6.13, dưới tiêu đề CPU Flame Graphs. Bản thân việc hình ảnh hóa được giải thích trong Mục 6.7.3, Flame Graphs.

FlameScope là một công cụ khác để hình ảnh hóa kết quả của `perf script`, kết hợp một bản đồ nhiệt độ lệch dưới giây (subsecond-offset heat map) để nghiên cứu các biến động theo thời gian với flame graphs. Nó cũng được bao gồm trong Chương 6, CPUs, Mục 6.7.4, FlameScope.

### 13.11.2 Trace Scripts
Các trace scripts perf(1) có sẵn có thể được liệt kê bằng cách sử dụng `-l`:

```bash
# perf script -l
List of available trace scripts:
[...]
  event_analyzing_sample             analyze all perf samples
  mem-phys-addr                      resolve physical address samples
  intel-pt-events                    print Intel PT Power Events and PTWRITE
  sched-migration                    sched migration overview
  net_dropmonitor                    display a table of dropped frames
  syscall-counts-by-pid [comm]       system-wide syscall counts, by pid
  failed-syscalls-by-pid [comm]      system-wide failed syscalls, by pid
  export-to-sqlite [database name] [columns] [calls] export perf data to a sqlite3
database
  stackcollapse                      produce callgraphs in short form for scripting
use
```

Những lệnh này có thể được thực thi như các đối số cho `perf script`. Bạn cũng có thể phát triển các trace scripts bổ sung bằng Perl hoặc Python.

## 13.12 perf trace
Lệnh phụ perf trace sẽ truy vết các system calls theo mặc định và in kết quả trực tiếp (không cần tệp perf.data). Nó đã được giới thiệu trong Chương 5, Các ứng dụng, Mục 5.5.1, như một phiên bản chi phí thấp hơn của strace(1) có thể truy vết trên toàn hệ thống. perf trace cũng có thể instrument bất kỳ sự kiện nào bằng cú pháp tương tự như `perf record`.

Ví dụ, truy vết các vấn đề và hoàn thành I/O đĩa:

```bash
# perf trace -e block:block_rq_issue,block:block_rq_complete
     0.000 auditd/391 block:block_rq_issue:259,0 WS 8192 () 16046032 + 16 [auditd]
     0.566 systemd-journa/28651 block:block_rq_complete:259,0 WS () 16046032 + 16 [0]
     0.748 jbd2/nvme0n1p1/174 block:block_rq_issue:259,0 WS 61440 () 2100744 + 120 [jbd2/nvme0n1p1-]
     1.436 systemd-journa/28651 block:block_rq_complete:259,0 WS () 2100744 + 120 [0]
     1.515 kworker/0:1H-k/365 block:block_rq_issue:259,0 FF 0 () 0 + 0 [kworker/0:1H]
     1.543 kworker/0:1H-k/365 block:block_rq_issue:259,0 WFS 4096 () 2100864 + 8 [kworker/0:1H]
     2.074 sshd/6463 block:block_rq_complete:259,0 WFS () 2100864 + 8 [0]
     2.077 sshd/6463 block:block_rq_complete:259,0 FF 0 () 0 + 0 [0]
  1087.562 kworker/0:1H-k/365 block:block_rq_issue:259,0 W 4096 () 16046040 + 8 [kworker/0:1H]
[...]
```

Cũng giống như với `perf record`, các bộ lọc cũng có thể được sử dụng trên các sự kiện. Những bộ lọc này có thể bao gồm một số hằng số chuỗi (string constants), được tạo ra từ các tiêu đề kernel. Ví dụ, truy vết các syscall mmap(2) nơi các cờ là MAP_SHARED bằng cách sử dụng chuỗi "SHARED":

```bash
# perf trace -e syscalls:*enter_mmap --filter='flags==SHARED'
     0.000 env/14780 syscalls:sys_enter_mmap(len: 27002, prot: READ, flags: SHARED,
fd: 3)
    16.145 grep/14787 syscalls:sys_enter_mmap(len: 27002, prot: READ, flags: SHARED,
fd: 3)
    18.704 cut/14791 syscalls:sys_enter_mmap(len: 27002, prot: READ, flags: SHARED,
fd: 3)
[...]
```

Lưu ý rằng perf(1) cũng đang sử dụng các chuỗi để cải thiện khả năng đọc của chuỗi định dạng: thay vì “prot: 1” nó đã in “prot: READ”. perf(1) gọi khả năng này là “beautification.”

### 13.12.1 Các phiên bản Kernel (Kernel Versions)
Trước Linux 4.19, `perf trace` sẽ instrument tất cả các syscalls theo mặc định (tùy chọn `--syscalls`) bên cạnh các sự kiện được chỉ định (`-e`). Để vô hiệu hóa các syscalls, hãy chỉ định `--no-syscalls` (thứ hiện nay là mặc định). Ví dụ:

`# perf trace -e block:block_rq_issue,block:block_rq_complete --no-syscalls`

Lưu ý rằng việc truy vết trên tất cả các CPUs (`-a`) đã là mặc định kể từ Linux 3.8. Các bộ lọc (`--filter`) đã được thêm vào trong Linux 5.5.

## 13.13 Các Lệnh Khác (Other Commands)
Có nhiều lệnh phụ và chức năng perf(1) hơn; tóm tắt các lệnh phụ bổ sung (xem Bảng 13.1 để biết danh sách đầy đủ):
- **perf c2c (Linux 4.10+):** Phân tích chia sẻ sai lệch (false sharing) cache-to-cache và cache line
- **perf kmem:** Phân tích cấp phát bộ nhớ kernel
- **perf kvm:** Phân tích thực thể khách KVM
- **perf lock:** Phân tích khóa
- **perf mem:** Phân tích truy cập bộ nhớ
- **perf sched:** Các thống kê trình lập lịch kernel
- **perf script:** Các công cụ perf tùy chỉnh

Các khả năng bổ sung nâng cao bao gồm khởi chạy các chương trình BPF trên các sự kiện, và sử dụng instrumentation phần cứng chẳng hạn như Intel processor trace (PT) hoặc ARM CoreSight để phân tích theo từng chỉ lệnh [Hunter 20].

Dưới đây là một ví dụ cơ bản về Intel processor trace. Việc này ghi lại các chu kỳ ở chế độ user-mode cho lệnh date(1):

```bash
# perf record -e intel_pt/cyc/u date
Sat Jul 11 05:52:40 PDT 2020
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.049 MB perf.data ]
```

Điều này có thể được in dưới dạng một vết chỉ lệnh (instruction trace) (các chỉ lệnh được tô đậm):

```bash
# perf script --insn-trace
          date 31979 [003] 653971.670163672:      7f3bfbf4d090 _start+0x0 (/lib/x86_64-linux-gnu/ld-2.27.so) insn: 48 89 e7
          date 31979 [003] 653971.670163672:      7f3bfbf4d093 _start+0x3 (/lib/x86_64-linux-gnu/ld-2.27.so) insn: e8 08 0e 00 00
[...]
```

Kết quả này bao gồm các chỉ lệnh dưới dạng mã máy. Việc cài đặt và sử dụng Intel x86 Encoder Decoder (XED) sẽ in các chỉ lệnh dưới dạng assembly [Intelxed 19]:

```bash
# perf script --insn-trace --xed
          date 31979 [003] 653971.670363672: ... (/lib/x86_64-linux-gnu/ld-2.27.so) mov %rsp, %rdi
          date 31979 [003] 653971.670363672: ... (/lib/x86_64-linux-gnu/ld-2.27.so) callq 0x7f3bfbf4dea0
          date 31979 [003] 653971.670363672: ... (/lib/x86_64-linux-gnu/ld-2.27.so) pushq %rbp
[...]
          date 31979 [003] 653971.670439432: ... (/bin/date) xor %ebp, %ebp
          date 31979 [003] 653971.670439432: ... (/bin/date) mov %rdx, %r9
          date 31979 [003] 653971.670439432: ... (/bin/date) popq %rsi
          date 31979 [003] 653971.670439432: ... (/bin/date) mov %rsp, %rdx
          date 31979 [003] 653971.670439432: ... (/bin/date) and $0xfffffffffffffff0, %rsp
[...]
```

Trong khi đây là chi tiết đáng kinh ngạc, nó cũng rất dài dòng. Kết quả đầy đủ là 266,105 dòng, và đó chỉ là cho lệnh date(1). Xem wiki của perf(1) cho các ví dụ khác [Hunter 20].

## 13.14 Tài liệu perf (perf Documentation)
Mỗi lệnh phụ cũng có một trang man để tham khảo bắt đầu với “perf-”, ví dụ, perf-record(1) cho lệnh phụ record. Những trang này nằm trong cây mã nguồn Linux kernel dưới tools/perf/Documentation.

Cũng có bài hướng dẫn perf(1) trên wiki.kernel.org [Perf 15], một trang perf(1) không chính thức bởi Vince Weaver [Weaver 11], và một trang các ví dụ perf(1) không chính thức khác của chính tôi [Gregg 20f].

Trang riêng của tôi chứa danh sách các lệnh một dòng đầy đủ, cũng như nhiều ví dụ khác.

Vì perf(1) thường xuyên đạt được các tính năng mới, hãy kiểm tra các bản cập nhật trong các phiên bản kernel sau này. Một nguồn tốt là danh sách changelog cho mỗi kernel được công bố trên KernelNewbies [KernelNewbies 20].

## 13.15 Tài liệu tham khảo (References)
- [Weaver 11] Weaver, V., “The Unofficial Linux Perf Events Web-Page,” http://web.eece.maine.edu/~vweaver/projects/perf_events, 2011.
- [Matz 13] Matz, M., Hubička, J., Jaeger, A., and Mitchell, M., “System V Application Binary Interface, AMD64 Architecture Processor Supplement, Draft Version 0.99.6,” http://x86-64.org/documentation/abi.pdf, 2013.
- [Perf 15] “Tutorial: Linux kernel profiling with perf,” *perf wiki*, https://perf.wiki.kernel.org/index.php/Tutorial, last updated 2015.
- [Intel 16] *Intel 64 and IA-32 Architectures Software Developer’s Manual Volume 3B: System Programming Guide, Part 2*, September 2016, https://www.intel.com/content/www/us/en/architecture-and-technology/64-ia-32-architectures-software-developer-vol-3b-part-2-manual.html, 2016.
- [AMD 18] *Open-Source Register Reference for AMD Family 17h Processors Models 00h-2Fh*, https://developer.amd.com/resources/developer-guides-manuals, 2018.
- [ARM 19] *Arm® Architecture Reference Manual Armv8, for Armv8-A architecture profile*, https://developer.arm.com/docs/ddi0487/latest/arm-architecture-reference-manual-armv8-for-armv8-a-architecture-profile, 2019.
- [Intelxed 19] “Intel XED,” https://intelxed.github.io, 2019.
- [Gregg 20h] Gregg, B., “One-Liners,” http://www.brendangregg.com/perf.html#OneLiners, last updated 2020.
- [Gregg 20f] Gregg, B., “perf Examples,” http://www.brendangregg.com/perf.html, last updated 2020.
- [Hunter 20] Hunter, A., “Perf tools support for Intel® Processor Trace,” https://perf.wiki.kernel.org/index.php/Perf_tools_support_for_Intel%C2%AE_Processor_Trace, last updated 2020.
- [Intel 20c] “perfmon/,” https://download.01.org/perfmon, accessed 2020.
- [KernelNewbies 20] “KernelNewbies: LinuxVersions,” https://kernelnewbies.org/LinuxVersions, accessed 2020.
