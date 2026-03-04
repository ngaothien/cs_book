# Chương 14: Ftrace

Ftrace là trình truy vết (tracer) chính thức của Linux, một công cụ đa năng bao gồm các tiện ích truy vết khác nhau. Ftrace được tạo ra bởi Steven Rostedt và được thêm lần đầu vào Linux 2.6.27 (2008). Nó có thể được sử dụng mà không cần bất kỳ front-end cấp người dùng bổ sung nào, giúp nó đặc biệt phù hợp cho các môi trường Linux nhúng nơi không gian lưu trữ là hạn hẹp. Nó cũng hữu ích cho các môi trường máy chủ.

Chương này, cùng với Chương 13, perf, và Chương 15, BPF, là tài liệu đọc tùy chọn cho những ai muốn tìm hiểu chi tiết hơn về một hoặc nhiều trình truy vết hệ thống.

Ftrace có thể được sử dụng để trả lời các câu hỏi chẳng hạn như:
- Tần suất các hàm kernel nhất định được gọi là bao nhiêu?
- Đường dẫn mã nào đã dẫn tới việc gọi hàm này?
- Những hàm con nào mà hàm kernel này gọi?
- Độ trễ cao nhất gây ra bởi các đường dẫn mã bị vô hiệu hóa chiếm quyền ưu tiên (preemption disabled) là bao nhiêu?

Các phần sau đây được cấu trúc để giới thiệu Ftrace, trình bày một số trình tạo hồ sơ (profilers) và trình truy vết (tracers) của nó, và sau đó chỉ ra các front-ends sử dụng chúng. Các phần là:
- 14.1: Tổng quan về các khả năng (Capabilities Overview)
- 14.2: tracefs (/sys)
- Các trình tạo hồ sơ (Profilers):
  - 14.3: Ftrace Function Profiler
  - 14.10: Ftrace Hist Triggers
- Các trình truy vết (Tracers):
  - 14.4: Ftrace Function Tracing
  - 14.5: Tracepoints
  - 14.6: kprobes
  - 14.7: uprobes
  - 14.8: Ftrace function_graph
  - 14.9: Ftrace hwlat
- Các Front-ends:
  - 14.11: trace-cmd
  - 14.12: perf ftrace
  - 14.13: perf-tools
- 14.14: Tài liệu Ftrace (Ftrace Documentation)
- 14.15: Tài liệu tham khảo (References)

Ftrace hist triggers là một chủ đề nâng cao yêu cầu phải bao quát cả các trình tạo hồ sơ và trình truy vết trước, do đó nó nằm ở vị trí sau này trong chương. Các phần kprobes và uprobes cũng bao gồm các khả năng tạo hồ sơ cơ bản.

Hình 14.1 là tổng quan về Ftrace và các front-ends của nó, với các mũi tên chỉ ra đường dẫn từ các sự kiện tới các loại kết quả.

(Hình 14.1 Ftrace profilers, tracers, và front ends)

Những nội dung này được giải thích trong các phần tiếp theo.

## 14.1 Tổng quan về các Khả năng (Capabilities Overview)
Trong khi perf(1) sử dụng các lệnh phụ cho các chức năng khác nhau, Ftrace có *profilers* và *tracers*. Các profilers cung cấp các bản tóm tắt thống kê chẳng hạn như số lượng và biểu đồ histograms, và các tracers cung cấp các chi tiết cho mỗi sự kiện.

Như một ví dụ về Ftrace, công cụ funcgraph(8) sau đây sử dụng một Ftrace tracer để chỉ ra các lần gọi hàm con của hàm kernel vfs_read():

```bash
# funcgraph vfs_read
Tracing "vfs_read"... Ctrl-C to end.
 1)               |  vfs_read() {
 1)               |    rw_verify_area() {
 1)               |      security_file_permission() {
 1)               |        apparmor_file_permission() {
 1)               |          common_file_perm() {
 1)   0.763 us    |            aa_file_perm();
 1)   2.209 us    |          }
 1)   3.329 us    |        }
 1)   0.571 us    |        __fsnotify_parent();
 1)   0.612 us    |        fsnotify();
 1)   7.019 us    |      }
 1)   8.416 us    |    }
 1)               |    __vfs_read() {
 1)               |      new_sync_read() {
 1)               |        ext4_file_read_iter() {
[...]
```

Kết quả cho thấy vfs_read() đã gọi rw_verify_area(), thứ đã gọi security_file_permission(), và cứ tiếp tục như vậy. Cột thứ hai hiển thị thời lượng trong mỗi hàm ("us" là micro giây) sao cho bạn có thể thực hiện phân tích hiệu năng, nhận diện các hàm con đã khiến một hàm cha chạy chậm. Khả năng Ftrace cụ thể này được gọi là function graph tracing (và được bao quát trong Mục 14.8, Ftrace function_graph).

Các profilers và tracers của Ftrace từ một phiên bản Linux gần đây (5.2) được liệt kê trong Bảng 14.1 và 14.2, cùng với các *event tracers* của Linux: tracepoints, kprobes, và uprobes. Những event tracers này tương tự như Ftrace, chia sẻ cùng cấu hình và giao diện kết quả, và được bao gồm trong chương này. Các tên trình truy vết phông chữ monospace được chỉ ra trong Bảng 14.2 là các Ftrace tracers, và cũng là các từ khóa dòng lệnh được sử dụng để cấu hình chúng.

Bảng 14.1 Các profilers của Ftrace
| Profiler | Mô tả | Mục |
| --- | --- | --- |
| function | Các thống kê hàm kernel | 14.3 |
| kprobe profiler | Các số lượng kprobe đã bật | 14.6.5 |
| uprobe profiler | Các số lượng uprobe đã bật | 14.7.4 |
| hist triggers | Các biểu đồ histograms tùy chỉnh trên các sự kiện | 14.10 |

Bảng 14.2 Ftrace và các event tracers
| Tracer | Mô tả | Mục |
| --- | --- | --- |
| function | Trình truy vết lệnh gọi hàm kernel | 14.4 |
| tracepoints | Các sự kiện instrumentation tĩnh của kernel | 14.5 |
| kprobes | Instrumentation động kernel (event tracer) | 14.6 |
| uprobes | Instrumentation động cấp người dùng (event tracer) | 14.7 |
| function_graph | Truy vết lệnh gọi hàm kernel với một biểu đồ phân cấp của các lần gọi con. | 14.8 |
| wakeup | Đo lường độ trễ trình lập lịch CPU tối đa | - |
| wakeup_rt | Đo lường độ trễ trình lập lịch CPU tối đa cho các tác vụ thời gian thực (RT) | - |
| irqsoff | Truy vết các sự kiện tắt IRQs với vị trí mã và độ trễ (độ trễ bị vô hiệu hóa ngắt)¹ | - |
| preemptoff | Truy vết các sự kiện bị vô hiệu hóa chiếm quyền ưu tiên với vị trí mã và độ trễ | - |
| preemptirqsoff | Một trình truy vết kết hợp irqsoff và preemptoff | - |
| blk | Trình truy vết I/O khối (được sử dụng bởi blktrace(8)). | - |
| hwlat | Trình truy vết độ trễ phần cứng: có thể phát hiện các nhiễu loạn bên ngoài gây ra độ trễ | 14.9 |
| mmiotrace | Truy vết các lệnh gọi mà một mô-đun thực hiện tới phần cứng | - |
| nop | Một trình truy vết đặc biệt để vô hiệu hóa các tracers khác | - |

Bạn có thể liệt kê các Ftrace tracers có sẵn trên phiên bản kernel của mình bằng cách sử dụng:
`# cat /sys/kernel/debug/tracing/available_tracers`
`hwlat blk mmiotrace function_graph wakeup_dl wakeup_rt wakeup function nop`

Việc này sử dụng giao diện tracefs được mount dưới /sys, thứ được giới thiệu trong phần tiếp theo. Các phần tiếp theo bao quát các profilers, tracers, và các công cụ sử dụng chúng.

Các phiên bản kernel tương lai có thể thêm nhiều profilers và tracers hơn vào Ftrace: hãy kiểm tra tài liệu Ftrace trong mã nguồn Linux dưới Documentation/trace/ftrace.rst [Rostedt 08].

---
¹ Cái này (và preemptoff, preemptirqsoff) yêu cầu CONFIG_PREEMPTIRQ_EVENTS phải được bật.

---

## 14.2 tracefs (/sys)
Giao diện để sử dụng các khả năng của Ftrace là hệ thống tập tin tracefs. Nó nên được mount trên `/sys/kernel/tracing`; ví dụ, bằng cách sử dụng:
`mount -t tracefs tracefs /sys/kernel/tracing`

Ftrace ban đầu là một phần của hệ thống tập tin debugfs cho đến khi nó được tách thành tracefs của riêng nó. Khi debugfs được mount, nó vẫn bảo toàn cấu trúc thư mục ban đầu bằng cách mount tracefs như một thư mục con của tracing. Bạn có thể liệt kê cả hai điểm mount debugfs và tracefs bằng cách sử dụng:
`# mount -t debugfs,tracefs`
`debugfs on /sys/kernel/debug type debugfs (rw,relatime)`
`tracefs on /sys/kernel/debug/tracing type tracefs (rw,relatime)`

Kết quả này là từ Ubuntu 19.10, thứ cho thấy tracefs được mount trong `/sys/kernel/debug/tracing`. Các ví dụ trong các phần tiếp theo tuân theo vị trí này vì nó vẫn được sử dụng rộng rãi, nhưng trong tương lai nó nên chuyển sang `/sys/kernel/tracing`.

Lưu ý rằng nếu tracefs thất bại khi mount, một lý do khả thi là kernel của bạn đã được xây dựng mà không có các tùy chọn cấu hình Ftrace (CONFIG_FTRACE, v.v.).

### 14.2.1 Nội dung của tracefs (tracefs Contents)
Một khi tracefs được mount, bạn nên có khả năng thấy các tập tin điều khiển và kết quả trong thư mục tracing:

```bash
# ls -F /sys/kernel/debug/tracing
available_events            max_graph_depth        stack_trace_filter
available_filter_functions  options/               synthetic_events
available_tracers           per_cpu/               timestamp_mode
buffer_percent              printk_formats         trace
buffer_size_kb              README                 trace_clock
buffer_total_size_kb        saved_cmdlines         trace_marker
current_tracer              saved_cmdlines_size    trace_marker_raw
dynamic_events              saved_tgids            trace_options
dyn_ftrace_total_info       set_event              trace_pipe
enabled_functions           set_event_pid          trace_stat/
error_log                   set_ftrace_filter      tracing_cpumask
events/                     set_ftrace_notrace     tracing_max_latency
free_buffer                 set_ftrace_pid         tracing_on
function_profile_enabled    set_graph_function     tracing_thresh
hwlat_detector/             set_graph_notrace      uprobe_events
instances/                  snapshot               uprobe_profile
kprobe_events               stack_max_size
kprobe_profile              stack_trace
```

Tên của nhiều trong số này là mang tính trực quan. Các tập tin và thư mục then chốt bao gồm những thứ được liệt kê trong Bảng 14.3.

Bảng 14.3 Các tập tin then chốt của tracefs
| Tập tin | Quyền truy cập | Mô tả |
| --- | --- | --- |
| available_tracers | read | Liệt kê các tracers có sẵn (xem Bảng 14.2) |
| current_tracer | read/write | Hiển thị tracer hiện tại đã bật |
| function_profile_enabled | read/write | Bật trình tạo hồ sơ hàm (function profiler) |
| available_filter_functions | read | Liệt kê các hàm có sẵn để truy vết |
| set_ftrace_filter | read/write | Chọn các hàm để truy vết |
| tracing_on | read/write | Một công tắc để bật/vô hiệu hóa buffer vòng kết quả (output ring buffer) |
| trace | read/write | Kết quả của các tracers (ring buffer) |
| trace_pipe | read | Kết quả của các tracers; phiên bản này tiêu thụ các trace và block cho đầu vào |
| trace_options | read/write | Các tùy chọn để tùy chỉnh kết quả buffer vòng |
| trace_stat (thư mục) | read/write | Kết quả của trình tạo hồ sơ hàm |
| kprobe_events | read/write | Cấu hình kprobe đã bật |
| uprobe_events | read/write | Cấu hình uprobe đã bật |
| events (thư mục) | read/write | Các tệp điều khiển trình truy vết sự kiện: tracepoints, kprobes, uprobes |
| instances (thư mục) | read/write | Các thực thể Ftrace cho các người dùng đồng thời |

Giao diện /sys này được tài liệu hóa trong mã nguồn Linux dưới Documentation/trace/ftrace.rst [Rostedt 08]. Nó có thể được sử dụng trực tiếp từ shell hoặc bằng các scripts và các thư viện. Như một ví dụ, để xem liệu có bất kỳ trình truy vết Ftrace nào hiện đang được sử dụng hay không, bạn có thể dùng cat(1) lên tập tin current_tracer:

```bash
# cat /sys/kernel/debug/tracing/current_tracer
nop
```

Kết quả hiển thị nop (no operation), có nghĩa là không có trình truy vết nào hiện đang được sử dụng. Để bật một trình truy vết, hãy ghi tên của nó vào tập tin này. Ví dụ, để bật trình truy vết blk:

`# echo blk > /sys/kernel/debug/tracing/current_tracer`

Các điều khiển và tập tin kết quả Ftrace khác cũng có thể được sử dụng qua echo(1) và cat(1). Điều này có nghĩa là Ftrace có hầu như không có sự phụ thuộc nào để được sử dụng (chỉ cần một shell là đủ²).

Steven Rostedt đã xây dựng Ftrace cho mục đích sử dụng riêng của mình trong khi phát triển bộ bản vá thời gian thực (realtime patch set), và ban đầu nó đã không hỗ trợ người dùng đồng thời. Khả năng hỗ trợ người dùng đồng thời đã được thêm vào sau đó, dưới dạng các thực thể có thể được tạo ra trong thư mục "instances". Mỗi thực thể có các tập tin điều khiển và kết quả riêng của nó sao cho nó có thể thực hiện việc truy vết một cách độc lập.

Các phần sau đây (14.3 tới 14.10) trình bày thêm nhiều ví dụ về giao diện /sys; sau đó các phần sau này (14.11 tới 14.13) chỉ ra các front ends được xây dựng dựa trên nó: trace-cmd, trình truy vết perf(1) ftrace, và perf-tools.

---
² echo(1) là một shell builtin, cat(1) có thể được xấp xỉ là: function shellcat { (while read line; do echo "$line"; done) < $1; }. Hoặc busybox có thể được sử dụng để bao gồm một shell, cat(1), và các kiến thức cơ bản khác.

---

## 14.3 Ftrace Function Profiler
Trình tạo hồ sơ hàm (function profiler) cung cấp các thống kê về các lệnh gọi hàm kernel, và phù hợp cho việc khám phá những hàm kernel nào đang được sử dụng và nhận diện cái nào là chậm nhất. Tôi thường xuyên sử dụng trình tạo hồ sơ hàm như một điểm bắt đầu để hiểu việc thực thi mã kernel cho một khối lượng công việc tải nhất định, đặc biệt là vì nó hiệu quả và tiêu tốn chi phí tương đối thấp. Sử dụng nó, tôi có thể nhận diện các hàm để phân tích sử dụng việc truy vết theo từng sự kiện (per-event tracing) tốn kém hơn. Nó yêu cầu tùy chọn kernel CONFIG_FUNCTION_PROFILER=y.

Trình tạo hồ sơ hàm hoạt động bằng cách sử dụng các instrumentation calls tại điểm bắt đầu của mỗi hàm kernel. Cách tiếp cận này dựa trên cách các trình tạo hồ sơ mã nguồn hoạt động, chẳng hạn như tùy chọn `-pg` của gcc(1), thứ chèn các lệnh gọi mcount() cho việc sử dụng với gprof(1). Kể từ phiên bản gcc(1) 4.6, lệnh gọi mcount() này hiện là `__fentry__()`. Việc thêm các lệnh gọi tới *mọi* hàm kernel nghe có vẻ như nó sẽ gây ra chi phí đáng kể, thứ sẽ là một mối lo ngại cho những thứ hiếm khi được sử dụng, nhưng vấn đề chi phí đã được giải quyết: khi không sử dụng, những lệnh gọi này thường được thay thế bằng các chỉ lệnh no-op nhanh, và chỉ được chuyển đổi sang các lệnh gọi `__fentry__()` khi cần thiết [Gregg 19f].

Phần sau đây trình diễn trình tạo hồ sơ hàm sử dụng giao diện tracefs trong /sys. Để tham khảo, phần sau đây chỉ ra trạng thái ban đầu không được bật của trình tạo hồ sơ hàm:

```bash
# cd /sys/kernel/debug/tracing
# cat set_ftrace_filter
#### all functions enabled ####
# cat function_profile_enabled
0
```

Bây giờ (từ cùng thư mục) các lệnh này sử dụng trình tạo hồ sơ hàm để đếm tất cả các lệnh gọi kernel bắt đầu với "tcp" trong khoảng 10 giây:

```bash
# echo 'tcp*' > set_ftrace_filter
# echo 1 > function_profile_enabled
# sleep 10
# echo 0 > function_profile_enabled
# echo > set_ftrace_filter
```

Lệnh sleep(1) đã được sử dụng để thiết lập một thời lượng (thô) của hồ sơ. Các lệnh sau đó đã vô hiệu hóa việc tạo hồ sơ hàm và thiết lập lại bộ lọc. Mẹo: hãy chắc chắn sử dụng “0 >” và không phải “0>”—cái sau không giống nhau; cái sau là một sự chuyển hướng của file descriptor 0. Tương tự hãy tránh “1>” như một sự chuyển hướng của file descriptor 1.

Các thống kê hồ sơ bây giờ có thể được đọc từ các tập tin trace_stat, thứ giữ chúng trong "function" files cho từng CPU. Đây là một hệ thống 2-CPU. Sử dụng head(1) để chỉ hiển thị mười dòng đầu tiên từ mỗi tập tin:

```bash
# head trace_stat/function*
==> trace_stat/function0 <==
  Function                               Hit    Time            Avg             s^2
  --------                               ---    ----            ---             ---
  tcp_sendmsg                         955912    2788479 us      2.917 us        3734541 us
  tcp_sendmsg_locked                  955912    2248025 us      2.351 us        2600545 us
  tcp_push                            955912    852421.5 us     0.891 us        1057342 us
  tcp_write_xmit                      926777    674611.1 us     0.727 us        1386620 us
  tcp_send_mss                        955912    504021.1 us     0.527 us        95650.41 us
  tcp_current_mss                     964399    317931.5 us     0.329 us        136101.4 us
  tcp_poll                            966848    216701.2 us     0.224 us        201483.9 us
  tcp_release_cb                      956155    102312.4 us     0.107 us        188001.9 us

==> trace_stat/function1 <==
  Function                               Hit    Time            Avg             s^2
  --------                               ---    ----            ---             ---
  tcp_sendmsg                         317935    936055.4 us     2.944 us        13488147 us
  tcp_sendmsg_locked                  317935    770290.2 us     2.422 us        8886817 us
  tcp_write_xmit                      348064    423766.6 us     1.217 us        226639782 us
  tcp_push                            317935    310040.7 us     0.975 us        4150989 us
  tcp_tasklet_func                     38109    189797.2 us     4.980 us        2239985 us
  tcp_tsq_handler                      38109    180516.6 us     4.736 us        2239552 us
  tcp_tsq_write.part.0                 29977    173955.7 us     5.802 us        1037352 us
  tcp_send_mss                        317935    165881.9 us     0.521 us        352309.0 us
```

Các cột hiển thị tên hàm (Function), số lượng lần gọi (Hit), tổng thời gian trong hàm (Time), thời gian hàm trung bình (Avg), và độ lệch tiêu chuẩn (s^2). Kết quả cho thấy hàm tcp_sendmsg() là thường xuyên nhất trên cả hai CPUs; nó được gọi hơn 955k lần trên CPU0 và hơn 317k lần trên CPU1. Thời lượng trung bình của nó là 2.9 micro giây.

Một lượng nhỏ chi phí bổ sung được thêm vào các hàm được tạo hồ sơ trong quá trình profiling. Nếu bộ lọc set_ftrace_filter được để trống, tất cả các hàm kernel đều được tạo hồ sơ (như chúng ta đã được cảnh báo bởi trạng thái ban đầu đã thấy sớm hơn: “all functions enabled”). Hãy ghi nhớ điều này khi sử dụng trình tạo hồ sơ, và cố gắng sử dụng chức năng bộ lọc hàm để giới hạn chi phí.

Các front ends Ftrace, được bao quát sau này, tự động hóa các bước này và có thể kết hợp kết quả cho từng CPU thành một bản tóm tắt trên toàn hệ thống.

## 14.4 Ftrace Function Tracing
Trình truy vết hàm in các chi tiết cho mỗi sự kiện của các lệnh gọi hàm kernel, và sử dụng instrumentation tạo hồ sơ đã mô tả trong phần trước. Điều này có thể chỉ ra chuỗi của các hàm khác nhau, tên tiến trình và PID tại thời điểm xảy ra sự kiện và điều đó mang lại cho bạn cái nhìn sâu sắc thấu đáo nhất có thể. Chi phí của việc truy vết hàm cao hơn so với việc tạo hồ sơ hàm, và do đó truy vết là tốt nhất cho các hàm tương đối không thường xuyên (ít hơn 1,000 lần gọi mỗi giây). Bạn có thể sử dụng trình tạo hồ sơ hàm từ phần trước để tìm hiểu tốc độ của các hàm trước khi truy vết chúng.

Các tệp tracefs then chốt liên quan đến việc truy vết hàm được trình bày trong Hình 14.2.

(Hình 14.2 Các tệp tracefs truy vết hàm Ftrace)

Kết quả truy vết cuối cùng được đọc từ các tệp trace hoặc trace_pipe, được mô tả trong các phần sau. Cả hai giao diện này cũng có các cách thức để xóa output buffer (do đó có các mũi tên quay ngược lại buffer).

### 14.4.1 Sử dụng trace
Phần sau đây trình diễn việc truy vết hàm với tệp kết quả trace. Để tham khảo, phần sau đây chỉ ra trạng thái ban đầu không được bật của trình truy vết hàm:

```bash
# cd /sys/kernel/debug/tracing
# cat set_ftrace_filter
#### all functions enabled ####
# cat current_tracer
nop
```

Hiện tại không có trình truy vết nào đang được sử dụng.

Cho ví dụ này, tất cả các hàm kernel kết thúc bằng "sleep" đều được truy vết, và các sự kiện cuối cùng được lưu vào tệp `/tmp/out.trace01.txt`. Một lệnh sleep(1) giả được sử dụng để thu thập ít nhất 10 giây truy vết. Chuỗi lệnh này kết thúc bằng cách vô hiệu hóa trình truy vết hàm và đưa hệ thống trở lại bình thường:

```bash
# cd /sys/kernel/debug/tracing
# echo 1 > tracing_on
# echo '*sleep' > set_ftrace_filter
# echo function > current_tracer
# sleep 10
# cat trace > /tmp/out.trace01.txt
# echo nop > current_tracer
# echo > set_ftrace_filter
```

Việc thiết lập tracing_on có thể là một bước không cần thiết (trên hệ thống Ubuntu của tôi, nó được thiết lập thành 1 theo mặc định). Tôi đã bao gồm nó đề phòng trường hợp nó không được thiết lập trên hệ thống của bạn.

Lệnh sleep(1) giả đã được bắt trong kết quả truy vết trong khi chúng ta đang truy vết các lệnh gọi hàm "sleep":

```bash
# more /tmp/out.trace01.txt
# tracer: function
#
# entries-in-buffer/entries-written: 57/57   #P:2
#
#                              _-----=> irqs-off
#                             / _----=> need-resched
#                            | / _---=> hardirq/softirq
#                            || / _--=> preempt-depth
#                            ||| /     delay
#           TASK-PID   CPU#  ||||    TIMESTAMP  FUNCTION
#              | |       |   ||||       |         |
       multipathd-348   [001] .... 332762.532877: __x64_sys_nanosleep <-do_syscall_64
       multipathd-348   [001] .... 332762.532879: hrtimer_nanosleep <-__x64_sys_nanosleep
       multipathd-348   [001] .... 332762.532880: do_nanosleep <-hrtimer_nanosleep
            sleep-4203  [001] .... 332762.722497: __x64_sys_nanosleep <-do_syscall_64
            sleep-4203  [001] .... 332762.722498: hrtimer_nanosleep <-__x64_sys_nanosleep
            sleep-4203  [001] .... 332762.722498: do_nanosleep <-hrtimer_nanosleep
       multipathd-348   [001] .... 332763.532966: __x64_sys_nanosleep <-do_syscall_64
[...]
```

Kết quả bao gồm các tiêu đề trường và metadata truy vết. Ví dụ này cho thấy một tiến trình mang tên multipathd với PID 348 gọi các hàm sleep, cũng như lệnh sleep(1). Các trường cuối cùng cho biết hàm và hàm cha đã gọi nó. Ví dụ, dòng đầu tiên, hàm là `__x64_sys_nanosleep()` và nó được gọi bởi `do_syscall_64()`.

Tệp trace là một giao diện cho buffer vòng của các sự kiện truy vết. Việc đọc nó cho thấy nội dung buffer; bạn có thể xóa nội dung bằng cách ghi một dòng mới vào nó:

`# > trace`

Buffer vòng cũng được xóa khi current_tracer được thiết lập trở lại nop như tôi đã làm trong các bước ví dụ để vô hiệu hóa truy vết. Nó cũng được xóa khi trace_pipe được sử dụng.

### 14.4.2 Sử dụng trace_pipe
Tệp trace_pipe là một giao diện khác cho việc đọc buffer truy vết. Các lệnh đọc từ tập tin này trả về một dòng truyền phát (stream) vô tận các sự kiện. Nó cũng tiêu thụ các sự kiện, sao sau khi đọc chúng một lần chúng không còn nằm trong buffer truy vết nữa.

Ví dụ, sử dụng trace_pipe để xem các sự kiện sleep trực tiếp:

```bash
# echo '*sleep' > set_ftrace_filter
# echo function > current_tracer
# cat trace_pipe
       multipathd-348   [001] .... 332624.519190: __x64_sys_nanosleep <-do_syscall_64
       multipathd-348   [001] .... 332624.519192: hrtimer_nanosleep <-__x64_sys_nanosleep
       multipathd-348   [001] .... 332624.519192: do_nanosleep <-hrtimer_nanosleep
       multipathd-348   [001] .... 332625.519272: __x64_sys_nanosleep <-do_syscall_64
       multipathd-348   [001] .... 332625.519274: hrtimer_nanosleep <-__x64_sys_nanosleep
       multipathd-348   [001] .... 332625.519274: do_nanosleep <-hrtimer_nanosleep
             cron-504   [001] .... 332625.560150: __x64_sys_nanosleep <-do_syscall_64
             cron-504   [001] .... 332625.560152: hrtimer_nanosleep <-__x64_sys_nanosleep
             cron-504   [001] .... 332625.560152: do_nanosleep <-hrtimer_nanosleep
^C
# echo nop > current_tracer
# echo > set_ftrace_filter
```

Kết quả hiển thị một số lần ngủ từ các tiến trình multipathd và cron. Các trường là giống như kết quả tệp trace đã chỉ ra trước đó, nhưng lần này không có các tiêu đề cột.

Tệp trace_pipe rất tiện lợi để theo dõi các sự kiện tần suất thấp, nhưng đối với các sự kiện tần suất cao, bạn sẽ muốn chuyển hướng chúng tới một tệp để phân tích sau này bằng cách sử dụng tệp truy vết đã trình bày trước đó.

### 14.4.3 Các tùy chọn (Options)
Ftrace cung cấp các tùy chọn để tùy chỉnh kết quả truy vết, thứ có thể được điều khiển từ một tệp trace_options hoặc thư mục options. Ví dụ (từ cùng thư mục) vô hiệu hóa cột cờ irq-info (trong kết quả trước đó đây là “....”):

```bash
# echo 0 > options/irq-info
# cat trace
# tracer: function
#
# entries-in-buffer/entries-written: 3300/3300   #P:2
#
#           TASK-PID   CPU#      TIMESTAMP  FUNCTION
#              | |       |          |         |
       multipathd-348   [001] 332762.532877: __x64_sys_nanosleep <-do_syscall_64
       multipathd-348   [001] 332762.532879: hrtimer_nanosleep <-__x64_sys_nanosleep
       multipathd-348   [001] 332762.532880: do_nanosleep <-hrtimer_nanosleep
[...]
```

Bây giờ cờ không còn hiện diện trong kết quả. Bạn có thể thiết lập lại bằng cách sử dụng:

`# echo 1 > options/irq-info`

Có rất nhiều tùy chọn, bạn có thể liệt kê từ thư mục options; chúng có một số cái tên khá trực quan.

```bash
# ls options/
annotate             funcgraph-abstime    hex                  stacktrace
bin                  funcgraph-cpu        irq-info             sym-addr
blk_cgname           funcgraph-duration   latency-format       sym-offset
blk_cgroup           funcgraph-irqs       markers              sym-userobj
blk_classic          funcgraph-overhead   overwrite            test_nop_accept
block                funcgraph-overrun    print-parent         test_nop_refuse
context-info         funcgraph-proc       printk-msg-only      trace_printk
disable_on_free      funcgraph-tail       raw                  userstacktrace
display-graph        function-fork        record-cmd           verbose
event-fork           function-trace       record-tgid
func_stack_trace     graph-time           sleep-time
```

Những tùy chọn này bao gồm stacktrace và userstacktrace, thứ sẽ thêm kernel và user stack traces vào kết quả: điều này hữu ích để hiểu tại sao các hàm được gọi. Tất cả những tùy chọn này đều được tài liệu hóa trong tài liệu Ftrace trong mã nguồn Linux [Rostedt 08].

## 14.5 Tracepoints
Tracepoints là instrumentation tĩnh của kernel, và đã được giới thiệu trong Chương 4, Các Công cụ Quan trắc, Mục 4.3.5, Tracepoints. Tracepoints về mặt kỹ thuật chỉ là các hàm truy vết được đặt trong mã nguồn kernel; chúng được sử dụng từ một giao diện sự kiện truy vết (trace event interface) định nghĩa và định dạng các đối số của chúng. Các sự kiện truy vết là nhìn thấy được trong tracefs, và chia sẻ giao diện kết quả và điều khiển với Ftrace.

Như một ví dụ, phần sau đây kích hoạt tracepoint block:block_rq_issue và theo dõi các sự kiện trực tiếp. Ví dụ này kết thúc bằng cách vô hiệu hóa tracepoint:

```bash
# cd /sys/kernel/debug/tracing
# echo 1 > events/block/block_rq_issue/enable
# cat trace_pipe
            sync-4844  [001] .... 343996.918805: block_rq_issue: 259,0 WS 4096 ()
2048 + 8 [sync]
            sync-4844  [001] .... 343996.918808: block_rq_issue: 259,0 WSM 4096 ()
10560 + 8 [sync]
            sync-4844  [001] .... 343996.918809: block_rq_issue: 259,0 WSM 4096 ()
38424 + 8 [sync]
            sync-4844  [001] .... 343996.918809: block_rq_issue: 259,0 WSM 4096 ()
4196384 + 8 [sync]
            sync-4844  [001] .... 343996.918810: block_rq_issue: 259,0 WSM 4096 ()
4462592 + 8 [sync]
^C
# echo 0 > events/block/block_rq_issue/enable
```

Năm cột đầu tiên giống như đã trình bày trong 4.6.4, và là: tên tiến trình “-” PID, ID CPU, các cờ, dấu thời gian (giây), và tên sự kiện. Phần còn lại là tracepoint được định dạng, được mô tả trong Mục 4.3.5.

Như có thể được nhìn thấy trong ví dụ này, tracepoints có các tệp điều khiển trong một cấu trúc thư mục dưới events. Có một thư mục cho từng hệ thống truy vết (ví dụ: “block”) và bên trong đó là các thư mục con cho mỗi sự kiện (ví dụ: “block_rq_issue”). Liệt kê thư mục này:

```bash
# ls events/block/block_rq_issue/
enable  filter  format  hist  id  trigger
```

Các tệp điều khiển này được tài liệu hóa trong mã nguồn Linux dưới Documentation/trace/events.rst [Ts’o 20]. Trong ví dụ này, tệp enable đã được sử dụng để bật và tắt tracepoint. Các tệp khác cung cấp các khả năng lọc và kích hoạt (filtering and triggered capabilities).

### 14.5.1 Filter (Bộ lọc)
Một bộ lọc có thể được bao gồm để chỉ ghi lại sự kiện khi một biểu thức Boolean được đáp ứng. Nó có một cú pháp hạn chế:

`field operator value`

Trường này là từ tệp format được mô tả trong Mục 4.3.5, dưới tiêu đề Tracepoints Arguments và Format String. Các toán tử cho các con số là một trong số: ==, !=, <, <=, >, >=, &; và cho các chuỗi: ==, !=, ~. Toán tử ~ thực hiện khớp kiểu shell glob, với các ký tự đại diện: *, ?. Những biểu thức Boolean này có thể được nhóm lại với các dấu ngoặc đơn và kết hợp bằng cách sử dụng: &&, ||.

Như một ví dụ, phần sau đây thiết lập một bộ lọc trên tracepoint block:block_rq_insert đã được bật để chỉ truy vết các đợt đĩa I/O lớn hơn 64 Kbytes:

```bash
# echo 'bytes > 65536' > events/block/block_rq_insert/filter
# cat trace_pipe
    kworker/u4:1-7173  [000] .... 378115.779394: block_rq_insert: 259,0 W 262144 ()
5920256 + 512 [kworker/u4:1]
    kworker/u4:1-7173  [000] .... 378115.784654: block_rq_insert: 259,0 W 262144 ()
5924336 + 512 [kworker/u4:1]
    kworker/u4:1-7173  [000] .... 378115.789136: block_rq_insert: 259,0 W 262144 ()
5928432 + 512 [kworker/u4:1]
^C
```

Kết quả bây giờ chỉ chứa I/O lớn hơn.

`# echo 0 > events/block/block_rq_insert/filter`

Việc echo 0 này sẽ reset bộ lọc.

### 14.5.2 Trigger (Kích hoạt)
Một trigger chạy một lệnh truy vết bổ sung khi một sự kiện được kích hoạt. Lệnh đó có thể là để bật hoặc vô hiệu hóa việc truy vết khác, in một vết ngăn xếp, hoặc lấy một ảnh chụp nhanh của buffer truy vết. Các lệnh trigger khả dụng có thể được liệt kê từ tệp trigger khi không có trigger nào hiện đang được thiết lập. Ví dụ:

```bash
# cat events/block/block_rq_issue/trigger
# Available triggers:
# traceon traceoff snapshot stacktrace enable_event disable_event enable_hist
disable_hist hist
```

Một mục đích sử dụng cho triggers là khi bạn mong muốn thấy các sự kiện đã dẫn tới một tình trạng lỗi: một trigger có thể được đặt trên tình trạng lỗi thứ hoặc là vô hiệu hóa việc truy vết (traceoff) sao cho trace buffer chỉ chứa các sự kiện trước đó, hoặc lấy một ảnh chụp nhanh (snapshot) để bảo toàn nó.

Triggers có thể được kết hợp với các bộ lọc, được hiển thị trong phần trước, bằng cách sử dụng từ khóa `if`. Việc này có thể là cần thiết để khớp với một tình trạng lỗi hoặc một sự kiện thú vị. Ví dụ, để dừng ghi lại các sự kiện khi một đợt khối I/O lớn hơn 64 Kbytes được xếp hàng:

`# echo 'traceoff if bytes > 65536' > events/block/block_rq_insert/trigger`

Các hành động phức tạp hơn có thể được thực hiện bằng cách sử dụng hist triggers, được giới thiệu trong Mục 14.10, Ftrace Hist Triggers.

## 14.6 kprobes
kprobes là instrumentation động của kernel, và đã được giới thiệu trong Chương 4, Các Công cụ Quan trắc, Mục 4.3.6, kprobes. kprobes tạo ra các sự kiện kprobe cho các trình truy vết sử dụng, thứ chia sẻ các tệp kết quả và điều khiển tracefs với Ftrace. kprobes là tương tự như Ftrace tracers, được bao quát trong Mục 14.4, ở chỗ chúng truy vết các hàm kernel. Tuy nhiên, kprobes có thể được tùy chỉnh hơn nữa, có thể được đặt trên các độ dời hàm (các chỉ lệnh riêng lẻ), và có thể báo cáo các đối số của hàm và các giá trị trả về.

Phần này bao quát việc truy vết sự kiện kprobe và trình tạo hồ sơ Ftrace kprobe.

### 14.6.1 Truy vết Sự kiện (Event Tracing)
Như một ví dụ, phần sau đây sử dụng kprobes để instrument hàm kernel do_nanosleep():

```bash
# echo 'p:brendan do_nanosleep' >> kprobe_events
# echo 1 > events/kprobes/brendan/enable
# cat trace_pipe
       multipathd-348   [001] .... 345995.823380: brendan: (do_nanosleep+0x0/0x170)
       multipathd-348   [001] .... 345996.823473: brendan: (do_nanosleep+0x0/0x170)
       multipathd-348   [001] .... 345997.823558: brendan: (do_nanosleep+0x0/0x170)
^C
# echo 0 > events/kprobes/brendan/enable
# echo '-:brendan' >> kprobe_events
```

Cú pháp kprobe được tạo và xóa bằng cách nối thêm một cú pháp đặc biệt vào kprobe_events. Sau khi nó đã được tạo ra, nó xuất hiện trong thư mục events cùng với tracepoints, và có thể được sử dụng theo một cách thức tương tự.

Cú pháp kprobe được giải thích đầy đủ trong mã nguồn kernel dưới Documentation/trace/kprobetracer.rst [Hiramatsu 20]. kprobes có thể truy vết đầu vào (entry) và kết quả trả về của các hàm kernel cũng như các độ dời hàm. Cú pháp tóm tắt là:

`p[:[GRP/]EVENT] [MOD:]SYM[+offs]|MEMADDR [FETCHARGS]` : Thiết lập một probe
`r[MAXACTIVE][:[GRP/]EVENT] [MOD:]SYM[+0] [FETCHARGS]` : Thiết lập một return probe
`-:[GRP/]EVENT` : Xóa một probe

Trong ví dụ của tôi, chuỗi “p:brendan do_nanosleep” tạo ra một thăm dò (p:) với tên “brendan” cho biểu tượng kernel do_nanosleep(). Chuỗi “-:brendan” xóa thăm dò có tên “brendan”.

Các tên tùy chỉnh đã tỏ ra hữu ích cho việc phân biệt các người dùng kprobes khác nhau. Trình truy vết BCC (được bao quát trong Chương 15, BPF, Mục 15.1, BCC) sử dụng các tên bao gồm hàm được truy vết, chuỗi “bcc”, và PID của BCC. Ví dụ:

```bash
# cat /sys/kernel/debug/tracing/kprobe_events
p:kprobes/p_blk_account_io_start_bcc_19454 blk_account_io_start
p:kprobes/p_blk_mq_start_request_bcc_19454 blk_mq_start_request
```

Lưu ý rằng, trên các kernel mới hơn, BCC đã chuyển sang sử dụng một giao diện dựa trên perf_event_open(2) để sử dụng kprobes thay vì tệp kprobe_events (và các sự kiện được bật sẽ không xuất hiện trong kprobe_events).

### 14.6.2 Các đối số (Arguments)
Không giống như truy vết hàm (Mục 14.4, Ftrace Function Tracing), kprobes có thể kiểm tra các đối số của hàm và các giá trị trả về. Như một ví dụ, dưới đây là khai báo cho hàm do_nanosleep() đã được truy vết sớm hơn, từ kernel/time/hrtimer.c, với các kiểu biến được tô đậm:

```c
static int __sched do_nanosleep(struct hrtimer_sleeper *t, enum hrtimer_mode mode)
{
[...]
```

Truy vết hai đối số đầu tiên trên một hệ thống Intel x86_64 và in chúng dưới dạng thập lục phân (mặc định):

```bash
# echo 'p:brendan do_nanosleep hrtimer_sleeper=$arg1 hrtimer_mode=$arg2' >> kprobe_events
# echo 1 > events/kprobes/brendan/enable
# cat trace_pipe
       multipathd-348   [001] .... 349138.128610: brendan: (do_nanosleep+0x0/0x170)
hrtimer_sleeper=0xffffaa6a4030be80 hrtimer_mode=0x1
       multipathd-348   [001] .... 349139.128695: brendan: (do_nanosleep+0x0/0x170)
hrtimer_sleeper=0xffffaa6a4030be80 hrtimer_mode=0x1
       multipathd-348   [001] .... 349140.128785: brendan: (do_nanosleep+0x0/0x170)
hrtimer_sleeper=0xffffaa6a4030be80 hrtimer_mode=0x1
^C
# echo 0 > events/kprobes/brendan/enable
# echo '-:brendan' >> kprobe_events
```

Có cú pháp bổ sung được thêm vào phần mô tả sự kiện trong dòng đầu tiên: chuỗi “hrtimer_sleeper=$arg1”, ví dụ, truy vết đối số đầu tiên của hàm và sử dụng cái tên tùy chỉnh "hrtimer_sleeper". Điều này đã được tô đậm trong kết quả.

Việc truy cập vào các đối số như $arg1, $arg2, v.v., đã được thêm vào trong Linux 4.20. Các phiên bản Linux trước đó yêu cầu việc sử dụng các tên thanh ghi (register names).³ Dưới đây là định nghĩa kprobe tương đương sử dụng các tên thanh ghi:

`# echo 'p:brendan do_nanosleep hrtimer_sleeper=%di hrtimer_mode=%si' >> kprobe_events`

Để sử dụng các tên thanh ghi, bạn cần biết loại bộ xử lý và quy ước gọi hàm đang được sử dụng. x86_64 sử dụng bộ ABI AMD64 [Matz 13], vì vậy hai đối số đầu tiên có sẵn trong các thanh ghi rdi và rsi.⁴ Cú pháp này cũng được sử dụng bởi perf(1), và tôi đã cung cấp một ví dụ phức tạp hơn về nó trong Chương 13, perf, Mục 13.7.2, uprobes, thứ đã giải tham chiếu một con trỏ chuỗi.

### 14.6.3 Giá trị Trả về (Return Values)
Bí danh đặc biệt `$retval` cho giá trị trả về là có sẵn cho việc sử dụng với kretprobes. Ví dụ sau đây sử dụng nó để hiển thị giá trị trả về của do_nanosleep():

```bash
# echo 'r:brendan do_nanosleep ret=$retval' >> kprobe_events
# echo 1 > events/kprobes/brendan/enable
# cat trace_pipe
       multipathd-348   [001] d... 349782.180370: brendan: (hrtimer_nanosleep+0xce/0x1e0 <- do_nanosleep) ret=0x0
       multipathd-348   [001] d... 349783.180443: brendan: (hrtimer_nanosleep+0xce/0x1e0 <- do_nanosleep) ret=0x0
       multipathd-348   [001] d... 349784.180530: brendan: (hrtimer_nanosleep+0xce/0x1e0 <- do_nanosleep) ret=0x0
^C
# echo 0 > events/kprobes/brendan/enable
# echo '-:brendan' >> kprobe_events
```

Kết quả này cho thấy, trong khi truy vết, giá trị trả về của do_nanosleep() luôn là “0” (thành công).

### 14.6.4 Bộ lọc và Kích hoạt (Filters and Triggers)
Các bộ lọc và triggers có thể được sử dụng từ thư mục `events/kprobes/...`, giống như với tracepoints (xem Mục 14.5, Tracepoints). Dưới đây là tệp format cho kprobe trước đó trên do_nanosleep() với các đối số (từ Mục 14.6.2, Các đối số):

```bash
# cat events/kprobes/brendan/format
name: brendan
ID: 2024
format:
        field:unsigned short common_type;       offset:0;       size:2; signed:0;
        field:unsigned char common_flags;       offset:2;       size:1; signed:0;
        field:unsigned char common_preempt_count;       offset:3;       size:1; signed:0;
        field:int common_pid;   offset:4;       size:4; signed:1;

        field:unsigned long __probe_ip;         offset:8;       size:8; signed:0;
        field:u64 hrtimer_sleeper;      offset:16;      size:8;         signed:0;
        field:u64 hrtimer_mode;         offset:24;      size:8;         signed:0;

print fmt: "(%lx) hrtimer_sleeper=0x%lx hrtimer_mode=0x%lx", REC->__probe_ip, REC->
hrtimer_sleeper, REC->hrtimer_mode
```

Lưu ý rằng các tên biến hrtimer_sleeper và hrtimer_mode tùy chỉnh của tôi là nhìn thấy được như các trường có thể được sử dụng với một bộ lọc. Ví dụ:

`# echo 'hrtimer_mode != 1' > events/kprobes/brendan/filter`

Việc này sẽ chỉ truy vết các lệnh gọi do_nanosleep() nơi hrtimer_mode không bằng 1.

---
⁴ Trang man syscall(2) tóm tắt các quy ước gọi hàm cho các bộ xử lý khác nhau. Một đoạn trích có trong Mục 14.13.4, perf-tools One-Liners.

---

### 14.6.5 kprobe Profiling
Khi kprobes được bật, Ftrace đếm các sự kiện của chúng. Những số lượng này có thể được in trong tệp kprobe_profile. Ví dụ:

```bash
# cat /sys/kernel/debug/tracing/kprobe_profile
  p_blk_account_io_start_bcc_19454                   1808               0
  p_blk_mq_start_request_bcc_19454                    677               0
  p_blk_account_io_completion_bcc_19454               521              11
  p_kbd_event_1_bcc_1119                              632               0
```

Các cột là: tên thăm dò (định nghĩa của nó có thể được nhìn thấy bằng cách in tệp kprobe_events), số lượng trúng (hit count), và số lượng trượt-lỗi (miss-hits count) (nơi thăm dò được trúng nhưng sau đó có một lỗi xảy ra và nó đã không được ghi lại: nó đã bị bỏ lỡ).

Trong khi bạn đã có thể có được các số lượng hàm bằng cách sử dụng trình tạo hồ sơ hàm (Mục 14.3), tôi thấy trình tạo hồ sơ kprobe hữu ích cho việc kiểm tra các kprobes luôn-được-bật được sử dụng bởi các phần mềm giám sát, đề phòng trường hợp một số đang kích hoạt quá thường xuyên và nên bị vô hiệu hóa (nếu có thể).

## 14.7 uprobes
uprobes là instrumentation động cấp người dùng, và đã được giới thiệu trong Chương 4, Các Công cụ Quan trắc, Mục 4.3.7, uprobes. uprobes tạo ra các sự kiện uprobe cho các trình truy vết sử dụng, thứ chia sẻ kết quả tracefs và các tệp điều khiển với Ftrace.

Phần này bao quát việc truy vết sự kiện uprobe và trình tạo hồ sơ Ftrace uprobe.

### 14.7.1 Truy vết Sự kiện (Event Tracing)
Đối với uprobes, tệp điều khiển là uprobe_events, với cú pháp được tài liệu hóa trong mã nguồn Linux dưới Documentation/trace/uprobetracer.rst [Dronamraju 20]. Bản tóm tắt là:

`p[:[GRP/]EVENT] PATH:OFFSET [FETCHARGS]` : Thiết lập một uprobe
`r[:[GRP/]EVENT] PATH:OFFSET [FETCHARGS]` : Thiết lập một return uprobe (uretprobe)
`-:[GRP/]EVENT` : Xóa một uprobe hoặc uretprobe sự kiện

Cú pháp bây giờ yêu cầu một đường dẫn và một độ dời (offset) cho uprobe. Kernel không có thông tin biểu tượng cho phần mềm không gian người dùng, vì vậy độ dời này phải được xác định và cung cấp bằng các công cụ không gian người dùng.

Phần sau đây sử dụng uprobes để instrument hàm readline() từ bash(1), bắt đầu bằng việc tìm kiếm độ dời biểu tượng:

```bash
# readelf -s /bin/bash | grep -w readline
   882: 000000000008b6e0   153 FUNC    GLOBAL DEFAULT   14 readline
# echo 'p:brendan /bin/bash:0x8b6e0' >> uprobe_events
# echo 1 > events/uprobes/brendan/enable
# cat trace_pipe
            bash-3970  [000] d... 347549.225818: brendan: (0x55d0857b71e0)
            bash-4802  [000] d... 347552.666943: brendan: (0x560bcc1821e0)
            bash-4802  [000] d... 347552.799480: brendan: (0x560bcc1821e0)
^C
# echo 0 > events/uprobes/brendan/enable
# echo '-:brendan' >> uprobe_events
```

CẢNH BÁO: Nếu bạn vô tình sử dụng một độ dời biểu tượng nằm ở giữa một chỉ lệnh, bạn sẽ làm hỏng tiến trình mục tiêu (và đối với văn bản chỉ lệnh được chia sẻ, tất cả các tiến trình chia sẻ nó!). Ví dụ kỹ thuật sử dụng readelf(1) để tìm độ dời biểu tượng có thể không hoạt động nếu file nhị phân mục tiêu đã được biên dịch dưới dạng một position-independent executable (PIE) với address space layout randomization (ASLR). Tôi không khuyên bạn sử dụng giao diện này chút nào: hãy chuyển sang một trình truy vết cấp cao hơn thứ đảm nhận việc ánh xạ biểu tượng cho bạn (ví dụ: BCC hoặc bpftrace).

### 14.7.2 Các đối số và Giá trị Trả về
Những điều này tương tự như kprobes được trình diễn trong Mục 14.6, kprobes. Các đối số và giá trị trả về của uprobe có thể được kiểm tra bằng cách chỉ định chúng khi uprobe được tạo ra. Xem uprobetracer.rst [Dronamraju 20].

### 14.7.3 Các bộ lọc và Kích hoạt (Filters and Triggers)
Các bộ lọc và triggers có thể được sử dụng từ thư mục `events/uprobes/...`, như chúng đã được thực hiện với kprobes (xem Mục 14.6, kprobes).

### 14.7.4 uprobe Profiling
Khi uprobes được bật, Ftrace đếm các sự kiện của chúng. Những số lượng này có thể được in trong tệp uprobe_profile. Ví dụ:

```bash
# cat /sys/kernel/debug/tracing/uprobe_profile
/bin/bash brendan                                  11
```

Các cột là: đường dẫn, tên thăm dò (định nghĩa của nó có thể được nhìn thấy bằng cách in tệp uprobe_events), và số lượng trúng.

## 14.8 Ftrace function_graph
Trình truy vết function_graph in biểu đồ phân cấp hàm (call graph) cho các hàm, để lộ luồng của mã. Chương này bắt đầu với một ví dụ qua funcgraph(8) từ perf-tools. Sau đây là giao diện tracefs.

Để tham khảo, dưới đây là trạng thái ban đầu không được bật của trình truy vết biểu đồ hàm:

```bash
# cd /sys/kernel/debug/tracing
# cat set_graph_function
#### all functions enabled ####
# cat current_tracer
nop
```

Hiện tại không có trình truy vết nào đang được sử dụng.

### 14.8.1 Graph Tracing
Phần sau đây sử dụng trình truy vết function_graph trên hàm do_nanosleep(), để chỉ ra các lần gọi hàm con của nó:

```bash
# echo do_nanosleep > set_graph_function
# echo function_graph > current_tracer
# cat trace_pipe
 1)   2.731 us    |  get_xsave_addr();
 1)               |  do_nanosleep() {
 1)               |    hrtimer_start_range_ns() {
 1)               |      lock_hrtimer_base.isra.0() {
 1)               |        _raw_spin_lock_irqsave();
 1)   0.297 us    |      }
 1)   0.843 us    |    }
 1)   0.276 us    |    ktime_get();
 1)   0.340 us    |    get_nohz_timer_target();
 1)   0.474 us    |    enqueue_hrtimer();
 1)   0.339 us    |    _raw_spin_unlock_irqrestore();
 1)   4.438 us    |  }
 1)               |  schedule() {
 1)               |    rcu_note_context_switch() {
[...]
 5) $ 1000383 us  |  } /* do_nanosleep */
^C
# echo nop > current_tracer
# echo > set_graph_function
```

Kết quả hiển thị các lần gọi con và luồng mã: do_nanosleep() gọi hrtimer_start_range_ns(), thứ gọi lock_hrtimer_base.isra.0(), và cứ tiếp tục như vậy. Cột ở bên trái hiển thị CPU (trong kết quả này, hầu hết là CPU 1) và thời lượng trong các hàm, sao cho độ trễ có thể được nhận diện. Các độ trễ cao bao gồm một ký hiệu ký tự để giúp thu hút sự chú ý của bạn tới chúng, trong kết quả này là dấu "$" bên cạnh một độ trễ 1000383 micro giây (1.0 giây). Các ký tự là [Rostedt 08]:
- **$:** Lớn hơn 1 giây
- **@:** Lớn hơn 100 ms
- *****: Lớn hơn 10 ms
- **#:** Lớn hơn 1 ms
- **!:** Lớn hơn 100 μs
- **+:** Lớn hơn 10 μs

Ví dụ này đã cố ý không thiết lập một bộ lọc hàm (set_ftrace_filter), sao cho tất cả các lần gọi con đều được ghi lại. Tuy nhiên, điều này tiêu tốn một số chi phí, làm thổi phồng các thời lượng được báo cáo. Nó vẫn nói chung là hữu ích cho việc xác định vị trí nguồn gốc của các độ trễ cao, thứ có thể lấn át các chi phí được thêm vào. Khi bạn muốn thời gian chính xác hơn cho một hàm nhất định, bạn có thể sử dụng bộ lọc hàm để giảm bớt các hàm được truy vết. Ví dụ, để chỉ truy vết do_nanosleep():

```bash
# echo do_nanosleep > set_ftrace_filter
# cat trace_pipe
[...]
 7) $ 1000130 us  |  } /* do_nanosleep */
^C
```

Tôi đang truy vết cùng một khối lượng công việc (sleep 1). Sau khi áp dụng một bộ lọc, thời lượng được báo cáo của do_nanosleep() đã giảm từ 1000383 μs xuống 1000130 μs (cho những kết quả ví dụ này), vì nó không còn bao gồm chi phí của việc truy vết tất cả các hàm con.

Những ví dụ này cũng sử dụng trace_pipe để xem kết quả trực tiếp, nhưng điều này là dài dòng, và thực tế hơn là chuyển hướng tệp truy vết tới một tệp kết quả, như tôi đã trình diễn trong Mục 14.4, Ftrace Function Tracing.

### 14.8.2 Các tùy chọn (Options)
Các tùy chọn có sẵn để thay đổi kết quả, thứ có thể được liệt kê trong thư mục options:

```bash
# ls options/funcgraph-*
options/funcgraph-abstime    options/funcgraph-irqs       options/funcgraph-proc
options/funcgraph-cpu        options/funcgraph-overhead   options/funcgraph-tail
options/funcgraph-duration   options/funcgraph-overrun
```

Những tùy chọn này điều chỉnh kết quả và có thể bao gồm hoặc loại trừ các chi tiết, chẳng hạn như ID CPU (funcgraph-cpu), tên tiến trình (funcgraph-proc), thời lượng hàm (funcgraph-duration), và các đánh dấu trì hoãn (delay markers) (funcgraph-overhead).

## 14.9 Ftrace hwlat
Trình truy vết độ trễ phần cứng (hwlat) là một ví dụ về một trình truy vết mục đích đặc biệt. Nó có thể phát hiện các nhiễu loạn hiệu năng CPU bên ngoài: các sự kiện mà mặt khác là không nhìn thấy được đối với kernel và các công cụ khác. Ví dụ, các ngắt quản lý hệ thống (system management interrupt - SMI) và các nhiễu loạn hypervisor (bao gồm những cái gây ra bởi những người hàng xóm ồn ào).

Việc này hoạt động bằng cách chạy một vòng lặp mã miễn là một thực nghiệm với các ngắt bị vô hiệu hóa, đo lường thời gian thực hiện cho mỗi lần lặp của vòng lặp để chạy. Buffer vòng này được thực thi trên một CPU tại một thời điểm và xoay vòng qua từng CPU để chạy. Thời gian lặp chậm nhất cho mỗi CPU được in ra, với điều kiện nó vượt quá một ngưỡng (10 micro giây, thứ có thể được cấu hình qua tệp tracing_thresh).

Dưới đây là một ví dụ:

```bash
# cd /sys/kernel/debug/tracing
# echo hwlat > current_tracer
# cat trace_pipe
           <...>-5820  [001] d... 354016.973699: #1       inner/outer(us): 2152/1933    ts:1578801212.559595228
           <...>-5820  [000] d... 354017.985568: #2       inner/outer(us): 19/26        ts:1578801213.571460991
           <...>-5820  [001] dn.. 354019.009489: #3       inner/outer(us): 1699/5894    ts:1578801214.595380588
           <...>-5820  [000] d... 354020.033575: #4       inner/outer(us): 43/49        ts:1578801215.619463259
           <...>-5820  [001] d... 354021.057566: #5       inner/outer(us): 18/45        ts:1578801216.643451721
           <...>-5820  [000] d... 354022.081503: #6       inner/outer(us): 18/38        ts:1578801217.667385514
^C
# echo nop > current_tracer
```

Nhiều trường trong số này đã được mô tả trong các phần trước (xem Mục 14.4, Ftrace Function Tracing). Điều thú vị là sau dấu thời gian: có một số thứ tự (#1, ...), sau đó là các con số "inner/outer(us)", và cuối cùng là một dấu thời gian. Các con số inner/outer hiển thị thời gian vòng lặp bên trong (inner) và logic mã để quay vòng sang lần lặp tiếp theo (outer). Dòng đầu tiên cho thấy một lần lặp mất 2,152 micro giây (inner) và 1,933 micro giây (outer). Điều này vượt xa ngưỡng 10 micro giây, và là do một sự nhiễu loạn bên ngoài.

hwlat có các tham số có thể được cấu hình: vòng lặp chạy trong một khoảng thời gian được gọi là *width*, và chạy một thực nghiệm chiều rộng (width experiment) trong một khoảng thời gian được gọi là *window*. Lần lặp chậm nhất lâu hơn một ngưỡng (10 micro giây) trong mỗi chiều rộng được ghi lại. Những tham số này có thể được sửa đổi qua các tệp trong `/sys/kernel/debug/tracing/hwlat_detector`: các tệp width và window, thứ sử dụng các đơn vị micro giây.

CẢNH BÁO: Tôi muốn phân loại hwlat như một công cụ microbenchmark hơn là một công cụ quan sát, bởi vì nó thực hiện một thực nghiệm thứ tự nó sẽ làm nhiễu loạn hệ thống: nó sẽ làm cho một CPU bận rộn trong thời gian thực nghiệm, với các ngắt bị vô hiệu hóa.

## 14.10 Ftrace Hist Triggers
Hist triggers là một khả năng Ftrace tiên tiến được thêm vào Linux 4.7 bởi Tom Zanussi, cho phép tạo ra các biểu đồ histograms tùy chỉnh trên các sự kiện. Nó là một hình thức khác của tóm tắt thống kê, cho phép các số lượng được chia nhỏ theo một hoặc nhiều thành phần.

Cách sử dụng tổng thể cho một biểu đồ đơn lẻ là:
1. `echo 'hist:expression' > events/.../trigger`: Tạo một hist trigger.
2. sleep *duration*: Cho phép biểu đồ tích lũy dữ liệu.
3. `cat events/.../hist`: In biểu đồ histogram.
4. `echo '!hist:expression' > events/.../trigger`: Xóa nó.

Biểu thức hist có định dạng:
```text
hist:keys=<field1[,field2,...]>[:values=<field1[,field2,...]>]
[:sort=<field1[,field2,...]>][:size=#entries][:pause][:continue]
[:clear][:name=histname1][:<handler>.<action>] [if <filter>]
```
Cú pháp được tài liệu hóa đầy đủ trong mã nguồn Linux dưới Documentation/trace/histogram.rst, và sau đây là một số ví dụ [Zanussi 20].

### 14.10.1 Single Keys (Các khóa đơn lẻ)
Phần sau đây sử dụng hist triggers để đếm các syscalls qua tracepoint raw_syscalls:sys_enter, và cung cấp một biểu đồ histogram được chia nhỏ theo ID tiến trình:

```bash
# cd /sys/kernel/debug/tracing
# echo 'hist:key=common_pid' > events/raw_syscalls/sys_enter/trigger
# sleep 10
# cat events/raw_syscalls/sys_enter/hist
# event histogram
#
# trigger info: hist:keys=common_pid.execname:vals=hitcount:sort=hitcount:size=2048 [active]
#

{ common_pid:           347 } hitcount:          1
{ common_pid:           345 } hitcount:          3
{ common_pid:           504 } hitcount:          8
{ common_pid:           494 } hitcount:         20
{ common_pid:           502 } hitcount:         30
{ common_pid:           344 } hitcount:         32
{ common_pid:           348 } hitcount:         36
{ common_pid:         32399 } hitcount:        136
{ common_pid:         32400 } hitcount:        138
{ common_pid:         32379 } hitcount:        177
{ common_pid:         32296 } hitcount:        187
{ common_pid:         32396 } hitcount:     882604

Totals:
    Hits: 883372
    Entries: 12
    Dropped: 0
# echo '!hist:key=common_pid' > events/raw_syscalls/sys_enter/trigger
```

Kết quả cho thấy PID 32396 đã thực hiện 882,604 syscalls trong khi truy vết, và liệt kê các số lượng cho các PIDs khác. Một vài dòng cuối cùng hiển thị các thống kê của bảng băm (Hits), số lượng các mục trong bảng băm (Entries), và bao nhiêu lệnh ghi bị đánh rơi nếu các mục vượt quá kích thước băm (Dropped). Nếu các đợt rớt xảy ra, bạn có thể tăng kích thước của bảng băm khi khai báo nó; nó mặc định là 2048.

### 14.10.2 Fields (Các trường)
Các trường băm đến từ tệp format cho sự kiện. Đối với ví dụ này, trường common_pid đã được sử dụng:

```bash
# cat events/raw_syscalls/sys_enter/format
[...]
        field:int common_pid;   offset:4;       size:4; signed:1;

        field:long id;  offset:8;       size:8; signed:1;
        field:unsigned long args[6];    offset:16;      size:48;        signed:0;
```

Bạn cũng có thể sử dụng các trường khác. Đối với sự kiện này, trường id là ID của syscall. Sử dụng nó làm khóa băm:

```bash
# echo 'hist:key=id' > events/raw_syscalls/sys_enter/trigger
# cat events/raw_syscalls/sys_enter/hist
[...]
{ id:             14 } hitcount:         48
{ id:              1 } hitcount:      80362
{ id:              0 } hitcount:      80396
[...]
```

Biểu đồ histogram cho thấy các syscalls thường xuyên nhất có IDs 0 và 1. Trên hệ thống của tôi các syscall IDs này nằm trong tệp tiêu đề (header file) này:

```bash
# more /usr/include/x86_64-linux-gnu/asm/unistd_64.h
[...]
#define __NR_read 0
#define __NR_write 1
[...]
```

Điều này cho thấy 0 và 1 là dành cho các syscall read(2) và write(2).

### 14.10.3 Modifiers (Các sửa đổi)
Vì việc chia tách theo PID và syscall ID là phổ biến, hist triggers hỗ trợ các modifiers chú giải kết quả: `.execname` cho PIDs, và `.syscall` cho các syscall IDs. Ví dụ, thêm modifier .execname vào ví dụ trước đó:

```bash
# echo 'hist:key=common_pid.execname' > events/raw_syscalls/sys_enter/trigger
[...]
{ common_pid: bash             [     32379] } hitcount:        166
{ common_pid: sshd             [     32296] } hitcount:        259
{ common_pid: dd               [     32396] } hitcount:     869024
[...]
```

Kết quả bây giờ chứa tên tiến trình theo sau là PID trong ngoặc vuông, thay vì chỉ là PID.

### 14.10.4 PID Filters (Các bộ lọc PID)
Dựa trên PID trước đó bởi-PID và các kết quả ID syscall, bạn có thể giả định rằng cả hai có liên quan và lệnh dd(1) đang thực hiện các syscall read(2) và write(2). Để đo lường điều này trực tiếp, bạn có thể tạo một biểu đồ histogram cho syscall ID và sau đó sử dụng một bộ lọc để khớp trên PID:

```bash
# echo 'hist:key=id.syscall if common_pid==32396' > 
    events/raw_syscalls/sys_enter/trigger
# cat events/raw_syscalls/sys_enter/hist
# event histogram
#
# trigger info: hist:keys=id.syscall:vals=hitcount:sort=hitcount:size=2048 if common_
pid==32396 [active]
#

{ id: sys_write                [     1] } hitcount:     106425
{ id: sys_read                 [     0] } hitcount:     106425

Totals:
    Hits: 212850
    Entries: 2
    Dropped: 0
```

Biểu đồ histogram cho thấy các syscalls cho một PID đó, và modifier .syscall đã bao gồm tên các syscall. Điều này xác nhận rằng dd(1) đang gọi read(2) và write(2). Một giải pháp khác cho việc này là sử dụng nhiều khóa (multiple keys), như được trình bày trong phần tiếp theo.

### 14.10.5 Multiple Keys (Nhiều khóa)
Ví dụ sau đây bao gồm syscall ID dưới dạng một *khóa thứ hai*:

```bash
# echo 'hist:key=common_pid.execname,id' > events/raw_syscalls/sys_enter/trigger
# sleep 10
# cat events/raw_syscalls/sys_enter/hist
# event histogram
#
# trigger info: hist:keys=common_pid.execname,id:vals=hitcount:sort=hitcount:size=2048
[active]
#
[...]
{ common_pid: sshd             [     14250], id:             23 } hitcount:         36
{ common_pid: bash             [     14261], id:             13 } hitcount:         42
{ common_pid: sshd             [     14250], id:             14 } hitcount:         72
{ common_pid: dd               [     14325], id:              0 } hitcount:     9195176
{ common_pid: dd               [     14325], id:              1 } hitcount:     9195176

Totals:
    Hits: 18391064
    Entries: 75
    Dropped: 0
```

Kết quả bây giờ hiển thị tên tiến trình và PID, được chia nhỏ thêm bởi syscall ID. Biểu đồ histogram này cho thấy PID 142325 đang thực hiện các syscalls với IDs 0 và 1. Bạn có thể thêm modifier .syscall vào khóa thứ hai để làm cho nó bao gồm cả tên syscall.

### 14.10.6 Stack Trace Keys (Các khóa Vết ngăn xếp)
Tôi thường xuyên mong muốn biết đường dẫn mã dẫn tới sự kiện, và tôi đã gợi ý rằng Tom Zanussi thêm chức năng cho Ftrace để sử dụng toàn bộ kernel stack trace như một khóa.

Ví dụ, đếm các đường dẫn mã dẫn tới tracepoint block:block_rq_issue:

```bash
# echo 'hist:key=stacktrace' > events/block/block_rq_issue/trigger
# sleep 10
# cat events/block/block_rq_issue/hist
[...]
{ stacktrace:
          nvme_queue_rq+0x16c/0x1d0
          __blk_mq_try_issue_directly+0x116/0x1c0
          blk_mq_request_issue_directly+0x4b/0xe0
          blk_mq_try_issue_directly+0x46/0xb0
          blk_mq_sched_insert_requests+0xae/0x100
          blk_finish_plug+0x26/0x290
          blk_flush_plug_list+0xe3/0x110
          blk_finish_plug+0x26/0x34
          read_pages+0x86/0x1a0
          __do_page_cache_readahead+0x180/0x1a0
          ondemand_readahead+0x192/0x2d0
          page_cache_sync_readahead+0x78/0xc0
          generic_file_buffered_read+0x571/0xc00
          generic_file_read_iter+0xdc/0x140
          ext4_file_read_iter+0x4f/0x100
          new_sync_read+0x122/0x1b0
} hitcount:        266
[...]
```

Tôi đã lược bớt kết quả để chỉ hiển thị cái cuối cùng, vết ngăn xếp thường xuyên nhất. Nó cho thấy đĩa I/O đã được phát hành qua new_sync_read(), thứ đã gọi ext4_file_read_iter(), và cứ tiếp tục như vậy.

### 14.10.7 Synthetic Events (Các sự kiện Tổng hợp)
Đây là nơi mọi thứ bắt đầu trở nên thực sự kỳ lạ (nếu chúng chưa kỳ lạ). Một *synthetic event* có thể được tạo ra thứ được kích hoạt bởi các sự kiện khác, và có thể kết hợp các đối số sự kiện theo các cách tùy chỉnh. Để truy cập các đối số sự kiện từ các sự kiện trước đó, chúng có thể được lưu vào một biểu đồ histogram và được lấy bởi sự kiện tổng hợp sau này.

Điều này mang lại nhiều ý nghĩa hơn với một trường hợp sử dụng chính: các biểu đồ histograms độ trễ tùy chỉnh. Với các sự kiện tổng hợp, một dấu thời gian có thể được lưu trên một sự kiện và sau đó được truy xuất trên một sự kiện khác sao cho thời gian delta có thể được tính toán.

Ví dụ, phần sau đây sử dụng một sự kiện tổng hợp mang tên syscall_latency để tính toán độ trễ của tất cả các syscalls, và trình bày nó dưới dạng một biểu đồ histogram theo syscall ID và tên:

```bash
# cd /sys/kernel/debug/tracing
# echo 'syscall_latency u64 lat_us; long id' >> synthetic_events
# echo 'hist:keys=common_pid:ts0=common_timestamp.usecs' >> 
    events/raw_syscalls/sys_enter/trigger

# echo 'hist:keys=common_pid:lat_us=common_timestamp.usecs-$ts0:id=id' 
    'onmatch(raw_syscalls.sys_enter).trace(syscall_latency,$lat_us,id)' >> 
    events/raw_syscalls/sys_exit/trigger
# events/synthetic/syscall_latency/trigger
# sleep 10
# cat events/synthetic/syscall_latency/hist
[...]
{ lat_us:     5779085, id: sys_epoll_wait        } hitcount:          1
{ lat_us:     6232897, id: sys_poll              } hitcount:          1
{ lat_us:     6233840, id: sys_poll              } hitcount:          1
{ lat_us:     6233884, id: sys_futex             } hitcount:          1
{ lat_us:     7028672, id: sys_epoll_wait        } hitcount:          1
{ lat_us:     9999049, id: sys_poll              } hitcount:          1
{ lat_us:    10000097, id: sys_nanosleep         } hitcount:          1
{ lat_us:    10001535, id: sys_wait4             } hitcount:          1
{ lat_us:    10002176, id: sys_select            } hitcount:          1
[...]
```

Kết quả bị lược bớt để chỉ hiển thị các độ trễ cao nhất. Biểu đồ histogram đang đếm các cặp độ trễ (tính bằng micro giây) và syscall ID: kết quả này cho thấy sys_nanosleep đã có một lần xảy ra độ trễ 10000097 micro giây. Điều này rất có khả năng là do lệnh sleep 10 được sử dụng để thiết lập thời lượng ghi lại.

Kết quả cũng rất dài vì nó đang ghi lại một khóa cho mỗi tổ hợp micro giây và syscall ID, và trong thực tế tôi đã vượt quá kích thước hist mặc định là 2048. Bạn có thể tăng kích thước bằng cách thêm một toán tử `:size=...` vào khai báo hist, hoặc bạn có thể sử dụng công cụ sửa đổi `.log2` để ghi lại độ trễ dưới dạng log2. Điều này làm giảm đáng kể số lượng các mục hist, và vẫn có độ phân giải đủ để phân tích độ trễ.

Để vô hiệu hóa và dọn dẹp sự kiện này, hãy echo tất cả các chuỗi theo thứ tự ngược lại với một tiền tố “!”.

Trong Bảng 14.4, tôi giải thích cách thức sự kiện tổng hợp này hoạt động, với các đoạn mã (code snippets).

Bảng 14.4 Giải thích ví dụ sự kiện tổng hợp
| Mô tả | Cú pháp |
| --- | --- |
| Tôi muốn tạo một sự kiện tổng hợp mang tên syscall_latency với hai đối số: lat_us và id. | `echo 'syscall_latency u64 lat_us; long id' >> synthetic_events` |
| Khi sự kiện sys_enter xảy ra, hãy ghi lại một biểu đồ histogram sử dụng common_pid (PID hiện tại) làm khóa, | `echo 'hist:keys=common_pid: ... >> events/raw_syscalls/sys_enter/trigger` |
| và lưu thời gian hiện tại, tính bằng micro giây, vào một biến biểu đồ histogram mang tên ts0 thứ được liên kết với khóa biểu đồ histogram (common_pid). | `ts0=common_timestamp.usecs` |
| Trên sự kiện sys_exit, hãy sử dụng common_pid làm khóa biểu đồ histogram và, | `echo 'hist:keys=common_pid: ... >> events/raw_syscalls/sys_exit/trigger` |
| tính toán độ trễ như hiện tại trừ đi thời gian bắt đầu đã lưu trong ts0 bởi sự kiện trước đó, và lưu nó như một biến biểu đồ histogram mang tên lat_us, | `lat_us=common_timestamp.usecs-$ts0` |
| so sánh các khóa biểu đồ histogram của sự kiện này và sự kiện sys_enter. Nếu chúng khớp nhau (cùng một common_pid), thì hãy sử dụng giá trị lat_us đã tính toán (sys_enter tới sys_exit cho cùng một PID) để, | `onmatch(raw_syscalls.sys_enter)` |
| cuối cùng, kích hoạt sự kiện tổng hợp syscall_latency của chúng ta với lat_us và id làm các đối số. | `.trace(syscall_latency,$lat_us,id)` |
| Hiển thị sự kiện tổng hợp này như một biểu đồ histogram với lat_us và id làm các trường. | `echo 'hist:keys=lat_us,id.syscall:sort=lat_us' >> events/synthetic/syscall_latency/trigger` |

Các biểu đồ Ftrace histograms được triển khai như một đối tượng băm (khóa/giá trị), và các ví dụ trước đó chỉ sử dụng những bảng băm này cho đầu ra: hiển thị các số lượng syscall theo PID và ID. Với các sự kiện tổng hợp, chúng ta đang thực hiện hai điều bổ sung với những bảng băm này: A) lưu trữ các giá trị không phải là một phần của kết quả (dấu thời gian) và B) trong một sự kiện, lấy các cặp khóa/giá trị đã được thiết lập bởi một sự kiện khác. Chúng ta cũng đang thực hiện số học: một phép trừ. Trên thực tế, chúng ta đang bắt đầu viết các chương trình mini.

Có nhiều nội dung hơn cho các sự kiện tổng hợp, được bao quát trong tài liệu [Zanussi 20]. Tôi đã cung cấp phản hồi, trực tiếp hoặc gián tiếp, cho các kỹ sư Ftrace và BPF trong nhiều năm, và theo quan điểm của tôi sự phát triển của Ftrace mang lại ý nghĩa vì nó giải quyết các vấn đề mà tôi đã nêu ra trước đó. Tôi tóm tắt sự phát triển này như sau:

> “Ftrace thật tuyệt, nhưng tôi cần sử dụng BPF để đếm theo PID và stack trace.”
> “Của bạn đây, hist triggers.”
> “Thật tuyệt, nhưng tôi vẫn cần sử dụng BPF để thực hiện các tính toán độ trễ tùy chỉnh.”
> “Của bạn đây, synthetic events.”
> “Thật tuyệt, tôi sẽ kiểm tra nó sau khi tôi viết xong *BPF Performance Tools*.”
> “Thật sự ư?”

Vâng, bây giờ tôi thực sự cần khám phá việc áp dụng các sự kiện tổng hợp cho một số trường hợp sử dụng. Nó cực kỳ mạnh mẽ, được tích hợp vào kernel, và có thể được sử dụng chỉ thông qua lập trình shell đơn thuần. (Và tôi đã hoàn thành cuốn sách BPF, nhưng sau đó bận rộn với cuốn sách này.)

## 14.11 trace-cmd
trace-cmd là một front end Ftrace mã nguồn mở được phát triển bởi Steven Rostedt và những người khác [trace-cmd 20]. Nó hỗ trợ các lệnh phụ và các tùy chọn cho việc cấu hình hệ thống truy vết, một định dạng kết quả nhị phân, và các tính năng khác. Đối với các nguồn sự kiện, nó có thể sử dụng các trình truy vết function và function_graph, cũng như các tracepoints và các kprobes cùng uprobes đã được cấu hình sẵn.

Ví dụ, sử dụng trace-cmd để ghi lại hàm kernel do_nanosleep() qua trình truy vết function trong mười giây (sử dụng một lệnh sleep(1) giả):

```bash
# trace-cmd record -p function -l do_nanosleep sleep 10
  plugin 'function'
CPU0 data recorded at offset=0x4fe000
    0 bytes in size
CPU1 data recorded at offset=0x4fe000
    4096 bytes in size
# trace-cmd report
CPU 0 is empty
cpus=2
           sleep-21145 [001] 573259.213076: function:             do_nanosleep
       multipathd-348   [001] 573259.523759: function:             do_nanosleep
       multipathd-348   [001] 573260.523923: function:             do_nanosleep
       multipathd-348   [001] 573261.524022: function:             do_nanosleep
       multipathd-348   [001] 573262.524119: function:             do_nanosleep
[...]
```

Kết quả bắt đầu với lệnh sleep(1) được gọi bởi trace-cmd (nó cấu hình việc truy vết và sau đó khởi chạy lệnh được cung cấp), và sau đó là các lệnh gọi khác nhau từ multipathd PID 348. Ví dụ này cũng cho thấy trace-cmd là ngắn gọn hơn so với các lệnh tracefs tương đương trong /sys. Nó cũng an toàn hơn: nhiều lệnh phụ xử lý việc dọn dẹp trạng thái truy vết khi hoàn thành.

trace-cmd thường có thể được cài đặt qua một gói “trace-cmd”, và nếu không, mã nguồn có sẵn trên trang web trace-cmd [trace-cmd 20].

Phần này chỉ ra một sự lựa chọn các lệnh phụ và khả năng truy vết của trace-cmd. Hãy tham khảo tài liệu trace-cmd đi kèm cho tất cả các khả năng của nó, và cho cú pháp được sử dụng trong các ví dụ sau đây.

### 14.11.1 Tổng quan về các Lệnh phụ (Subcommands Overview)
Các khả năng của trace-cmd có sẵn bằng cách chỉ định trước tiên một lệnh phụ, chẳng hạn như trace-cmd record cho lệnh phụ record. Một sự lựa chọn các lệnh phụ từ một phiên bản trace-cmd gần đây (2.8.3) được liệt kê trong Bảng 14.5.

Bảng 14.5 Các lệnh phụ trace-cmd được lựa chọn
| Lệnh | Mô tả |
| --- | --- |
| record | Truy vết và ghi lại vào một tệp trace.dat |
| report | Đọc truy vết từ tệp trace.dat |
| stream | Truy vết và sau đó in ra stdout |
| list | Liệt kê các sự kiện truy vết khả dụng |
| stat | Hiển thị trạng thái của hệ thống con truy vết kernel |
| profile | Truy vết và tạo một báo cáo tùy chỉnh hiển thị thời gian kernel và các độ trễ |
| listen | Chấp nhận các yêu cầu mạng cho các đợt truy vết |

Các lệnh phụ khác bao gồm start, stop, restart, và clear cho việc kiểm soát truy vết vượt ra ngoài một lần gọi record duy nhất. Các phiên bản tương lai của trace-cmd có thể thêm nhiều lệnh phụ hơn; hãy chạy trace-cmd mà không có đối số để xem danh sách đầy đủ.

Mỗi lệnh phụ hỗ trợ nhiều tùy chọn khác nhau. Những thứ này có thể được liệt kê với -h, ví dụ, cho lệnh phụ record:

```bash
# trace-cmd record -h

trace-cmd version 2.8.3

usage:
  trace-cmd record [-v][-e event [-f filter]][-p plugin][-F][-d][-o file] 
           [-q][-s usecs][-O option ][-l func][-g func][-n func] 
           [-P pid][-N host:port][-t][-r prio][-b size][-B buf][command ...] 
           [-m max][-C clock]
          -e run command with event enabled
          -f filter for previous -e event
          -R trigger for previous -e event
          -p run command with plugin enabled
          -F filter only on the given process
          -P trace the given pid like -F for the command
          -c also trace the children of -F (or -P if kernel supports it)
          -C set the trace clock
          -T do a stacktrace on all events
          -l filter function name
          -g set graph function
          -n do not trace function
[...]
```

Các tùy chọn đã bị lược bớt trong kết quả này, chỉ hiển thị 12 trong số 35 tùy chọn. 12 tùy chọn đầu tiên này bao gồm những thứ được sử dụng phổ biến nhất. Lưu ý rằng thuật ngữ *plugin* (-p) đề cập đến các Ftrace tracers, bao gồm function, function_graph, và hwlat.

### 14.11.2 trace-cmd One-Liners
Các lệnh một dòng sau đây cho thấy các khả năng khác nhau của trace-cmd. Các ví dụ này được bao quát chi tiết hơn trong các trang man của họ.

**Liệt kê các Sự kiện (Listing Events)**
Liệt kê tất cả các sự kiện và tùy chọn truy vết:
`trace-cmd list`

Liệt kê các trình truy vết Ftrace:
`trace-cmd list -t`

Liệt kê các nguồn sự kiện (tracepoints, kprobe events, và uprobe events):
`trace-cmd list -e`

Liệt kê các tracepoints syscall:
`trace-cmd list -e syscalls`

Hiển thị tệp format cho một tracepoint nhất định:
`trace-cmd list -e syscalls:sys_enter_nanosleep -F`

**Truy vết Hàm (Function Tracing)**
Truy vết một hàm kernel trên toàn hệ thống:
`trace-cmd record -p function -l function_name`

Truy vết tất cả các hàm kernel bắt đầu với “tcp_”, trên toàn hệ thống, cho đến khi nhấn Ctrl-C:
`trace-cmd record -p function -l 'tcp_*'`

Truy vết tất cả các hàm kernel bắt đầu với “tcp_”, trên toàn hệ thống, trong 10 giây:
`trace-cmd record -p function -l 'tcp_*' sleep 10`

Truy vết tất cả các hàm kernel bắt đầu với “vfs_” cho lệnh ls(1):
`trace-cmd record -p function -l 'vfs_*' -F ls`

Truy vết tất cả các hàm kernel bắt đầu với “vfs_” cho bash(1) và các con của nó:
`trace-cmd record -p function -l 'vfs_*' -F -c bash`

Truy vết tất cả các hàm kernel bắt đầu với “vfs_” cho PID 21124:
`trace-cmd record -p function -l 'vfs_*' -P 21124`

**Truy vết Biểu đồ hàm (Function Graph Tracing)**
Truy vết một hàm kernel và các lần gọi con của nó, trên toàn hệ thống:
`trace-cmd record -p function_graph -g function_name`

Truy vết hàm kernel do_nanosleep() và các con của nó, trên toàn hệ thống, trong 10 giây:
`trace-cmd record -p function_graph -g do_nanosleep sleep 10`

**Truy vết Sự kiện (Event Tracing)**
Truy vết các tiến trình mới qua tracepoint sched:sched_process_exec, cho đến khi nhấn Ctrl-C:
`trace-cmd record -e sched:sched_process_exec`

Truy vết các tiến trình mới qua tracepoint sched:sched_process_exec (phiên bản ngắn hơn):
`trace-cmd record -e sched_process_exec`

Truy vết các yêu cầu khối I/O với các vết ngăn xếp kernel:
`trace-cmd record -e block_rq_issue -T`

Truy vết tất cả các tracepoints block cho đến khi nhấn Ctrl-C:
`trace-cmd record -e block`

Truy vết một kprobe đã được tạo ra trước đó mang tên “brendan” trong 10 giây:
`trace-cmd record -e probe:brendan sleep 10`

Truy vết tất cả các syscalls cho lệnh ls(1):
`trace-cmd record -e syscalls -F ls`

**Báo cáo (Reporting)**
In nội dung của tệp kết quả trace.dat:
`trace-cmd report`

In nội dung của tệp kết quả trace.dat, chỉ dành cho CPU 0:
`trace-cmd report --cpu 0`

**Các khả năng khác (Other Capabilities)**
Truy vết các sự kiện từ plugin sched_switch:
`trace-cmd record -p sched_switch`

Lắng nghe các yêu cầu truy vết trên cổng TCP 8081:
`trace-cmd listen -p 8081`

Kết nối tới host từ xa để chạy một lệnh phụ record:
`trace-cmd record ... -N addr:port`

### 14.11.3 trace-cmd so với perf(1)
Phong cách của các lệnh phụ trace-cmd có thể gợi nhắc bạn về perf(1), đã được bao quát trong Chương 13, và hai công cụ này có những khả năng tương tự nhau. Bảng 14.6 so sánh trace-cmd và perf(1).

Bảng 14.6 perf(1) so với trace-cmd
| Thuộc tính | perf(1) | trace-cmd |
| --- | --- | --- |
| File kết quả nhị phân | perf.data | trace.dat |
| Tracepoints | Có | Có |
| kprobes | Có | Partial(1) |
| uprobes | Có | Partial(1) |
| USDT | Có | Partial(1) |
| PMCs | Có | Không |
| Lấy mẫu theo thời gian | Có | Không |
| Truy vết hàm | Partial(2) | Có |
| Truy vết function_graph | Partial(2) | Có |
| Mạng client/server | Không | Có |
| Chi phí tệp kết quả | Thấp | Rất thấp |
| Front ends | Đa dạng | KernelShark |
| Mã nguồn | Trong Linux tools/perf | git.kernel.org |

- **Partial(1):** trace-cmd chỉ hỗ trợ các sự kiện này nếu chúng đã được tạo ra thông qua các phương tiện khác, và xuất hiện trong `/sys/kernel/debug/tracing/events`.
- **Partial(2):** perf(1) hỗ trợ những thứ này qua lệnh phụ ftrace, mặc dù nó chưa được tích hợp hoàn toàn vào perf.data, ví dụ.

Như một ví dụ về sự tương đồng, lệnh sau đây truy vết tracepoint syscalls:sys_enter_read trên toàn hệ thống trong mười giây và sau đó liệt kê vết bằng perf(1):

```bash
# perf record -e syscalls:sys_enter_nanosleep -a sleep 10
# perf script
```

...và sử dụng trace-cmd:

```bash
# trace-cmd record -e syscalls:sys_enter_nanosleep sleep 10
# trace-cmd report
```

Một ưu điểm của trace-cmd là hỗ trợ tốt hơn cho các trình truy vết function và function_graph.

### 14.11.4 trace-cmd function_graph
Phần mở đầu của Mục này đã trình diễn trình truy vết function bằng trace-cmd. Phần sau đây trình diễn trình truy vết function_graph cho cùng một hàm kernel, do_nanosleep():

```bash
# trace-cmd record -p function_graph -g do_nanosleep sleep 10
  plugin 'function_graph'
CPU0 data recorded at offset=0x4fe000
    12288 bytes in size
CPU1 data recorded at offset=0x501000
    45056 bytes in size
# trace-cmd report | cut -c 66-

          |  do_nanosleep() {
          |    hrtimer_start_range_ns() {
          |      lock_hrtimer_base.isra.0() {
          |        _raw_spin_lock_irqsave();
 0.250 us |      }
 0.688 us |    }
 0.190 us |    ktime_get();
 0.153 us |    get_nohz_timer_target();
[...]
```

Để rõ ràng trong ví dụ này, tôi đã sử dụng cut(1) để cô lập các cột biểu đồ hàm và định thời. Kết quả này bị lược bớt các trường truy vết điển hình đã chỉ ra trong ví dụ truy vết hàm trước đó.

### 14.11.5 KernelShark
KernelShark là một giao diện người dùng trực quan cho các tệp kết quả trace-cmd, được tạo ra bởi người tạo ra Ftrace, Steven Rostedt. Ban đầu là GTK, KernelShark kể từ đó đã được viết lại bằng Qt bởi Yordan Karadzhov, người duy trì dự án. KernelShark có thể được cài đặt từ một gói kernelshark nếu có sẵn, hoặc qua các liên kết mã nguồn trên trang web của nó [KernelShark 20]. Phiên bản 1.0 là phiên bản Qt, và 0.99 và cũ hơn là phiên bản GTK.

Như một ví dụ về việc sử dụng KernelShark, phần sau đây ghi lại tất cả các tracepoints của trình lập lịch và sau đó hình ảnh hóa chúng:

```bash
# trace-cmd record -e 'sched:*'
# kernelshark
```

KernelShark đọc tệp kết quả trace-cmd mặc định, trace.dat (bạn có thể chỉ định một tệp khác bằng cách sử dụng -i). Hình 14.3 hiển thị KernelShark đang hình ảnh hóa tệp này.

(Hình 14.3 KernelShark)

Phần trên cùng của màn hình hiển thị một dòng thời gian cho mỗi CPU, với các tác vụ có màu sắc khác nhau. Phần dưới cùng là một bảng các sự kiện. KernelShark mang tính tương tác: một cú nhấp và kéo chuột phải sẽ phóng to phạm vi thời gian đã chọn, và một cú nhấp và kéo trái sẽ thu nhỏ. Nhấp chuột phải vào các sự kiện cung cấp các hành động bổ sung, chẳng hạn như thiết lập các bộ lọc.

KernelShark có thể được sử dụng để nhận diện các vấn đề hiệu năng gây ra bởi sự tương tác giữa các luồng khác nhau.

### 14.11.6 trace-cmd Documentation
Đối với các cài đặt gói, tài liệu trace-cmd nên có sẵn dưới dạng trace-cmd(1) và các trang man khác (ví dụ: trace-cmd-record(1)), cũng nằm trong thư mục Documentation của mã nguồn trace-cmd. Tôi cũng khuyên bạn nên xem một bài nói chuyện của người duy trì Steven Rostedt về Ftrace và trace-cmd, chẳng hạn như “Understanding the Linux Kernel (via ftrace)”:
- **Slides:** https://www.slideshare.net/ennael/kernel-recipes-2017-understanding-the-linux-kernel-via-ftrace-steven-rostedt
- **Video:** https://www.youtube.com/watch?v=2ff-7UTg5rE

## 14.12 perf ftrace
Tiện ích perf(1), được bao quát trong Chương 13, có một lệnh phụ ftrace sao cho nó có thể truy cập vào các trình truy vết function và function_graph.

Ví dụ, sử dụng trình truy vết function trên hàm kernel do_nanosleep():

```bash
# perf ftrace -T do_nanosleep -a sleep 10
 0)  sleep-22821    |            |  do_nanosleep() {
 1)  multipa-348      |            |  do_nanosleep() {
 1)  multipa-348      | $ 1000068 us |  }
 1)  multipa-348      |            |  do_nanosleep() {
 1)  multipa-348      | $ 1000068 us |  }
[...]
```

Và sử dụng trình truy vết function_graph:

```bash
# perf ftrace -G do_nanosleep -a sleep 10
 1)  sleep-22828    |            |  do_nanosleep() {
 1)  sleep-22828    |  ==========> |
 1)  sleep-22828    |            |    smp_irq_work_interrupt() {
 1)  sleep-22828    |            |      irq_enter() {
 1)  sleep-22828    |   0.258 us   |        rcu_irq_enter();
 1)  sleep-22828    |   0.800 us   |      }
 1)  sleep-22828    |            |      wake_up() {
 1)  sleep-22828    |            |        wake_up_common_lock() {
 1)  sleep-22828    |   0.491 us   |          _raw_spin_lock_irqsave();
[...]
```

Lệnh phụ ftrace hỗ trợ một vài tùy chọn bao gồm `-p` để khớp trên một PID. Đây là một trình bao bọc (wrapper) đơn giản thứ không tích hợp với các khả năng perf(1) khác: nó in vết ra stdout và không sử dụng tệp perf.data.

## 14.13 perf-tools
perf-tools là một bộ sưu tập mã nguồn mở của các công cụ phân tích hiệu năng nâng cao dựa trên Ftrace và perf(1) được phát triển bởi chính tôi và được cài đặt theo mặc định trên các máy chủ tại Netflix [Gregg 20i]. Tôi đã thiết kế các công cụ này để dễ cài đặt (ít phụ thuộc) và đơn giản để sử dụng: mỗi công cụ nên thực hiện một việc và thực hiện nó tốt. Bản thân các công cụ perf-tools chủ yếu được triển khai dưới dạng các shell scripts tự động hóa việc thiết lập các tệp tracefs /sys.

Ví dụ, sử dụng execsnoop(8) để truy vết các tiến trình mới:

```bash
# execsnoop
Tracing exec()s. Ctrl-C to end.
   PID   PPID ARGS
  6684   6682 cat -v trace_pipe
  6683   6679 gawk -v o=1 -v opt_name=0 -v name= -v opt_duration=0 [...]
  6685  20997 man ls
  6685   6685 pager
  6691   6685 preconv -e UTF-8
  6692   6685 tbl
  6693   6685 nroff -mandoc -rLL=148n -rLT=148n
  6698   6693 locale charmap
  6693   6693 groff -mtty-char -mandoc -rLL=148n -rLT=148n
  6700   6699 troff -mtty-char -mandoc -rLL=148n -rLT=148n
  6701   6699 grotty
[...]
```

Kết quả này bắt đầu bằng việc hiển thị một lệnh cat(1) và gawk(1) được sử dụng bởi chính execsnoop(8), tiếp theo là các lệnh được thực thi bởi một man ls. Nó có thể được sử dụng để gỡ lỗi các vấn đề của các tiến trình tồn tại ngắn ngủi thứ có thể không nhìn thấy được đối với các công cụ khác.

execsnoop(8) hỗ trợ các tùy chọn bao gồm `-t` cho dấu thời gian và `-h` để tóm tắt cách sử dụng lệnh. execsnoop(8) và tất cả các công cụ khác cũng có một trang man và một tệp các ví dụ.

### 14.13.1 Tool Coverage
Hình 14.4 hiển thị các công cụ perf-tools khác nhau và các khu vực của một hệ thống mà chúng có thể quan sát.

(Hình 14.4 perf-tools)

Nhiều công cụ là công cụ đơn mục đích (single-purpose) được hiển thị với một đầu mũi tên duy nhất; một số là công cụ đa mục đích (multi-purpose) được liệt kê ở bên trái với một mũi tên kép để chỉ ra phạm vi bao phủ của chúng.

### 14.13.2 Các công cụ Đơn mục đích (Single-Purpose Tools)
Như đã lưu ý, những công cụ này được hiển thị với các đầu mũi tên duy nhất trong Hình 14.4. Một số đã được giới thiệu trong các chương trước.

Các công cụ đơn mục đích chẳng hạn như execsnoop(8) thực hiện một công việc và thực hiện nó tốt (triết lý Unix). Thiết kế này bao gồm việc làm cho kết quả mặc định của chúng súc tích và thường là đủ, giúp việc học hỏi trở nên dễ dàng. Bạn có thể “just run execsnoop” mà không cần phải học bất kỳ tùy chọn dòng lệnh nào, và nhận được đủ kết quả để giải quyết vấn đề của mình mà không bị lộn xộn không cần thiết. Các tùy chọn điển hình là có sẵn cho việc tùy chỉnh.

Các công cụ đơn mục đích được mô tả trong Bảng 14.7.

Bảng 14.7 Các công cụ perf-tools đơn mục đích
| Công cụ | Sử dụng | Mô tả |
| --- | --- | --- |
| bitesize(8) | perf | Tóm tắt kích thước đĩa I/O dưới dạng một biểu đồ histogram |
| cachestat(8) | Ftrace | Hiển thị các thống kê trúng/trượt của page cache |
| execsnoop(8) | Ftrace | Truy vết các tiến trình mới (qua execve(2)) với các đối số |
| iolatency(8) | Ftrace | Tóm tắt độ trễ đĩa I/O dưới dạng một biểu đồ histogram |
| iosnoop(8) | Ftrace | Truy vết đĩa I/O với các chi tiết bao gồm độ trễ |
| killsnoop(8) | Ftrace | Truy vết các tín hiệu kill(2) hiển thị tiến trình và các chi tiết tín hiệu |
| opensnoop(8) | Ftrace | Truy vết các syscalls thuộc họ open(2) hiển thị các tên tệp |
| tcpretrans(8) | Ftrace | Truy vết các lần truyền lại TCP, hiển thị các địa chỉ và trạng thái kernel |

execsnoop(8) đã được trình diễn sớm hơn. Như một ví dụ khác, iolatency(8) hiển thị độ trễ đĩa I/O dưới dạng một biểu đồ histogram:

```bash
# iolatency
Tracing block I/O. Output every 1 seconds. Ctrl-C to end.

  >=(ms) .. <(ms)   : I/O      |Distribution                          |
       0 -> 1       : 731      |######################################|
       1 -> 2       : 318      |################                      |
       2 -> 4       : 160      |########                              |

  >=(ms) .. <(ms)   : I/O      |Distribution                          |
       0 -> 1       : 2973     |######################################|
       1 -> 2       : 497      |######                                |
       2 -> 4       : 26       |#                                     |
       4 -> 8       : 3        |#                                     |
^C
```

Kết quả này cho thấy độ trễ đĩa I/O thông thường là thấp, trong khoảng từ 0 tới 1 mili giây.

Cách tôi triển khai điều này để giải thích nhu cầu về BPF mở rộng. iolatency(8) truy vết các sự kiện phát hành và hoàn thành I/O khối, đọc tất cả các sự kiện trong không gian người dùng, phân tích chúng, và xử lý hậu kỳ chúng vào các biểu đồ histograms này bằng cách sử dụng awk(1). Vì đĩa I/O có tần suất tương đối thấp trên hầu hết các máy chủ, cách tiếp cận này là khả thi mà không gặp phải chi phí đáng kể. Nhưng chi phí sẽ là cấm đoán cho các sự kiện thường xuyên hơn, chẳng hạn như mạng I/O hoặc lập lịch. BPF mở rộng đã giải quyết vấn đề này bằng cách cho phép bản tóm tắt biểu đồ histogram được tính toán trong không gian kernel, và chỉ bản tóm tắt được truyền tới không gian người dùng, làm giảm đáng kể chi phí. Ftrace hiện nay hỗ trợ các khả năng tương tự với hist triggers và các sự kiện tổng hợp, được mô tả trong Mục 14.10, Ftrace Hist Triggers (tôi cần cập nhật iolatency(8) để sử dụng chúng).

Tôi thực sự đã phát triển một giải pháp tiền-BPF cho các biểu đồ histograms tùy chỉnh, và để lộ nó như công cụ đa năng perf-stat-hist(8).

### 14.13.3 Các công cụ Đa mục đích (Multi-Purpose Tools)
Các công cụ đa mục đích được liệt kê và mô tả trong Hình 14.4. Những thứ này hỗ trợ nhiều nguồn sự kiện và có thể thực hiện nhiều vai trò, tương tự như perf(1) và trace-cmd, mặc dù điều này cũng làm cho việc sử dụng chúng trở nên phức tạp hơn.

Bảng 14.8 Các công cụ perf-tools đa mục đích
| Công cụ | Sử dụng | Mô tả |
| --- | --- | --- |
| funccount(8) | Ftrace | Đếm các lệnh gọi hàm kernel |
| funcgraph(8) | Ftrace | Truy vết các hàm kernel hiển thị luồng mã hàm con |
| functrace(8) | Ftrace | Truy vết các hàm kernel |
| funcslower(8) | Ftrace | Truy vết các hàm kernel chậm hơn một ngưỡng |
| kprobe(8) | Ftrace | Truy vết động các hàm kernel |
| perf-stat-hist(8) | perf(1) | Các đợt tổng hợp lũy thừa-của-2 tùy chỉnh cho các đối số tracepoint |
| syscount(8) | Ftrace | Tóm tắt các syscalls |
| tpoint(8) | Ftrace | Truy vết các tracepoints |
| uprobe(8) | Ftrace | Truy vết động các hàm cấp người dùng |

Để hỗ trợ việc sử dụng các công cụ này, bạn có thể thu thập và chia sẻ các lệnh một dòng. Tôi đã cung cấp chúng trong phần tiếp theo, tương tự như các phần lệnh một dòng của tôi cho perf(1) và trace-cmd.

### 14.13.4 perf-tools One-Liners
Các lệnh một dòng sau đây truy vết trên toàn hệ thống và cho đến khi Ctrl-C được nhấn, trừ khi có quy định khác. Chúng được nhóm thành những cái sử dụng Ftrace profiling, Ftrace tracers, và truy vết sự kiện (tracepoints, kprobes, uprobes).

**Ftrace Profilers**
Đếm tất cả các hàm TCP kernel:
`funccount 'tcp_*'`

Đếm tất cả các hàm VFS kernel, in ra top 10 sau mỗi 1 giây:
`funccount -t 10 -i 1 'vfs_*'`

**Ftrace Tracers**
Truy vết hàm kernel do_nanosleep() và hiển thị tất cả các lần gọi con:
`funcgraph do_nanosleep`

Truy vết hàm kernel do_nanosleep() và hiển thị các lần gọi con lên tới 3 cấp độ sâu:
`funcgraph -m 3 do_nanosleep`

Truy vết tất cả các hàm kernel kết thúc bằng “sleep” cho PID 198:
`functrace -p 198 '*sleep'`

Truy vết các lệnh gọi vfs_read() chậm hơn 10 ms:
`funcslower vfs_read 10000`

**Event Tracing**
Truy vết hàm kernel do_sys_open() bằng một kprobe:
`kprobe p:do_sys_open`

Truy vết kết quả trả về của do_sys_open() bằng một kretprobe, và in giá trị trả về:
`kprobe 'r:do_sys_open $retval'`

Truy vết đối số file mode của do_sys_open():
`kprobe 'p:do_sys_open mode=$arg3:u16'`

Truy vết đối số file mode của do_sys_open() (x86_64 cụ thể):
`kprobe 'p:do_sys_open mode=%dx:u16'`

Truy vết đối số tên tệp của do_sys_open() dưới dạng một chuỗi:
`kprobe 'p:do_sys_open filename=+0($arg2):string'`

Truy vết đối số tên tệp của do_sys_open() (x86_64 cụ thể) dưới dạng một chuỗi:
`kprobe 'p:do_sys_open filename=+0(%si):string'`

Truy vết do_sys_open() khi tên tệp khớp với “*stat*”:
`kprobe 'p:do_sys_open file=+0($arg2):string' 'file ~ "*stat*"'`

Truy vết tcp_retransmit_skb() với kernel stack traces:
`kprobe -s p:tcp_retransmit_skb`

Liệt kê các tracepoints:
`tpoint -l`

Truy vết đĩa I/O với các vết ngăn xếp kernel:
`tpoint -s block:block_rq_issue`

Truy vết readline() cấp người dùng trong tất cả các file thực thi “bash”:
`uprobe p:bash:readline`

Truy vết kết quả trả về của readline() từ “bash” và in giá trị trả về của nó dưới dạng một chuỗi:
`uprobe 'r:bash:readline +0($retval):string'`

Truy vết đầu vào readline() từ /bin/bash với đối số đầu vào (x86_64) dưới dạng một chuỗi:
`uprobe 'p:/bin/bash:readline prompt=+0(%di):string'`

Truy vết lệnh gọi libc gettimeofday() cho PID 1234 duy nhất:
`uprobe -p 1234 p:libc:gettimeofday`

Truy vết kết quả trả về của fopen() chỉ khi nó trả về NULL (và sử dụng một bí danh "file"):
`uprobe 'r:libc:fopen file=$retval' 'file == 0'`

**CPU Registers**
Các bí danh đối số hàm ($arg1, ..., $argN) là một khả năng Ftrace mới hơn (Linux 4.20+). Đối với các kernels cũ hơn (hoặc các kiến trúc bộ xử lý thiếu các bí danh), bạn sẽ cần sử dụng các tên thanh ghi CPU thay thế, như đã được giới thiệu trong Mục 14.6.2, Các đối số. Những lệnh một dòng này bao gồm một số thanh ghi x86_64 (%di, %si, %dx) làm ví dụ. Các quy ước gọi hàm được tài liệu hóa trong trang man syscall(2):

```bash
$ man 2 syscall
[...]
       Arch/ABI      arg1  arg2  arg3  arg4  arg5  arg6  arg7  Notes
[...]
       sparc/32      o0    o1    o2    o3    o4    o5    -
       sparc/64      o0    o1    o2    o3    o4    o5    -
       tile          R00   R01   R02   R03   R04   R05   -
       x86-64        rdi   rsi   rdx   r10   r8    r9    -
       x32           rdi   rsi   rdx   r10   r8    r9    -
[...]
```

### 14.13.5 Ví dụ
Như một ví dụ về việc sử dụng một công cụ, phần sau đây sử dụng funccount(8) để đếm các lệnh gọi VFS (các tên hàm khớp với "vfs_*"):

```bash
# funccount 'vfs_*'
Tracing "vfs_*"... Ctrl-C to end.
^C
FUNC                               COUNT
vfs_fsync_range                       10
vfs_statfs                            10
vfs_readlink                          35
vfs_statx                            673
vfs_write                            782
vfs_statx_fd                         922
vfs_open                            1003
vfs_getattr                         1390
vfs_getattr_nosec                   1390
vfs_read                            2604
```

Kết quả này cho thấy, trong quá trình truy vết, vfs_read() đã được gọi 2,604 lần. Tôi thường xuyên sử dụng funccount(8) để xác định tần suất các hàm kernel được gọi, và cái nào được gọi nhiều nhất. Vì chi phí của nó là tương đối thấp, tôi có thể sử dụng nó để kiểm tra xem liệu tốc độ gọi hàm có đủ thấp để thực hiện việc truy vết tốn kém hơn hay không.

### 14.13.6 perf-tools so với BCC/BPF
Ban đầu tôi đã phát triển perf-tools cho đám mây Netflix khi nó đang chạy Linux 3.2, thứ thiếu BPF mở rộng. Kể từ đó Netflix đã chuyển sang các kernels mới hơn, và tôi đã viết lại nhiều công cụ này để sử dụng BPF. Ví dụ, cả perf-tools và BCC đều có các phiên bản riêng của funccount(8), execsnoop(8), opensnoop(8), và nhiều hơn nữa.

BPF cung cấp khả năng lập trình và các khả năng mạnh mẽ hơn, và các front ends BCC và bpftrace BPF được bao quát trong Chương 15. Tuy nhiên, có một số ưu điểm của perf-tools:⁵
- **funccount(8):** Phiên bản perf-tools sử dụng Ftrace function profiling, thứ hiệu quả hơn nhiều và ít bị ràng buộc hơn so với phiên bản BCC dựa trên kprobe hiện tại.
- **funcgraph(8):** Công cụ này không tồn tại trong BCC, vì nó sử dụng Ftrace function_graph tracing.
- **Hist Triggers:** Điều này sẽ cung cấp sức mạnh cho perf-tools trong tương lai thứ nên hiệu quả hơn các phiên bản dựa trên kprobe của BCC.
- **Dependencies (Sự phụ thuộc):** perf-tools vẫn hữu ích cho các môi trường bị hạn chế tài nguyên (ví dụ: Linux nhúng) vì chúng điển hình chỉ yêu cầu một shell và awk(1).

Tôi cũng đôi khi sử dụng các công cụ perf-tools để kiểm tra chéo và gỡ lỗi các vấn đề với các công cụ BPF.⁶

---
⁵ Ban đầu tôi tin rằng mình sẽ khai tử perf-tools khi chúng ta hoàn thành việc truy vết BPF, nhưng tôi đã giữ cho nó tồn tại vì những lý do này.
⁶ Tôi có thể sửa đổi một câu nói nổi tiếng: một người đàn ông với một trình truy vết biết chuyện gì đã xảy ra; một người đàn ông với hai trình truy vết biết một trong số chúng bị hỏng, và tìm kiếm lkml hy vọng có một bản vá.

---

### 14.13.7 Tài liệu
Các công cụ thường có một thông điệp sử dụng để tóm tắt cú pháp của chúng. Ví dụ:

```bash
# funccount -h
USAGE: funccount [-hT] [-i secs] [-d secs] [-t top] funcstring
                -d seconds      # tổng thời lượng truy vết
                -h              # thông điệp sử dụng này
                -i seconds      # tóm tắt theo khoảng thời gian
                -t top          # chỉ hiển thị top số lượng các mục
                -T              # bao gồm dấu thời gian (cho -i)
eg,
       funccount 'vfs*'         # truy vết tất cả các hàm khớp với "vfs*"
       funccount -d 5 'tcp*'    # truy vết các hàm "tcp*" trong 5 giây
       funccount -t 10 'ext3*'  # hiển thị top 10 hàm "ext3*"
       funccount -i 1 'ext3*'   # tóm tắt mỗi 1 giây
       funccount -i 1 -d 5 'ext3*' # 5 x 1 tóm tắt thứ hai
```

Mỗi công cụ cũng có một trang man và một tệp các ví dụ trong kho lưu trữ perf-tools (ví dụ: funccount_example.txt) thứ chứa các ví dụ kết quả với lời bình luận.

## 14.14 Tài liệu Ftrace (Ftrace Documentation)
Ftrace (và các sự kiện truy vết) được tài liệu hóa tốt trong mã nguồn Linux, dưới thư mục Documentation/trace. Tài liệu này cũng trực tuyến tại:
- https://www.kernel.org/doc/html/latest/trace/ftrace.html
- https://www.kernel.org/doc/html/latest/trace/kprobetracer.html
- https://www.kernel.org/doc/html/latest/trace/uprobetracer.html
- https://www.kernel.org/doc/html/latest/trace/events.html
- https://www.kernel.org/doc/html/latest/trace/histogram.html

Các tài nguyên cho các front ends là:
- **trace-cmd:** https://trace-cmd.org
- **perf ftrace:** Trong mã nguồn Linux: tools/perf/Documentation/perf-ftrace.txt
- **perf-tools:** https://github.com/brendangregg/perf-tools

## 14.15 Tài liệu tham khảo (References)
- [Rostedt 08] Rostedt, S., “ftrace - Function Tracer,” *Linux documentation*, https://www.kernel.org/doc/html/latest/trace/ftrace.html, 2008+.
- [Matz 13] Matz, M., Hubička, J., Jaeger, A., and Mitchell, M., “System V Application Binary Interface, AMD64 Architecture Processor Supplement, Draft Version 0.99.6,” http://x86-64.org/documentation/abi.pdf, 2013.
- [Gregg 19f] Gregg, B., “Two Kernel Mysteries and the Most Technical Talk I’ve Ever Seen,” http://www.brendangregg.com/blog/2019-10-15/kernelrecipes-kernel-ftrace-internals.html, 2019.
- [Dronamraju 20] Dronamraju, S., “Uprobe-tracer: Uprobe-based Event Tracing,” *Linux documentation*, https://www.kernel.org/doc/html/latest/trace/uprobetracer.html, accessed 2020.
- [Gregg 20i] Gregg, B., “Performance analysis tools based on Linux perf_events (aka perf) and ftrace,” https://github.com/brendangregg/perf-tools, last updated 2020.
- [Hiramatsu 20] Hiramatsu, M., “Kprobe-based Event Tracing,” *Linux documentation*, https://www.kernel.org/doc/html/latest/trace/kprobetracer.html, accessed 2020.
- [KernelShark 20] “KernelShark,” https://www.kernelshark.org, accessed 2020.
- [trace-cmd 20] “TRACE-CMD,” https://trace-cmd.org, accessed 2020.
- [Ts’o 20] Ts’o, T., Zefan, L., and Zanussi, T., “Event Tracing,” *Linux documentation*, https://www.kernel.org/doc/html/latest/trace/events.html, accessed 2020.
- [Zanussi 20] Zanussi, T., “Event Histograms,” *Linux documentation*, https://www.kernel.org/doc/html/latest/trace/histogram.html, accessed 2020.
