# Chương 3: Hệ Điều Hành

Sự hiểu biết về hệ điều hành và nhân (kernel) của nó là thiết yếu cho việc phân tích hiệu năng hệ thống. Bạn sẽ thường xuyên cần phát triển và sau đó kiểm tra các giả thuyết về hành vi của hệ thống, chẳng hạn như cách các lời gọi hệ thống (system call) được thực hiện, cách nhân lập lịch các luồng (thread) trên CPU, cách bộ nhớ hạn chế có thể ảnh hưởng đến hiệu năng, hoặc cách hệ thống tệp xử lý I/O. Những hoạt động này sẽ yêu cầu bạn vận dụng kiến thức của mình về hệ điều hành và nhân.

Các mục tiêu học tập của chương này là:

- Học thuật ngữ về nhân: chuyển đổi ngữ cảnh (context switch), hoán đổi (swapping), phân trang (paging), chiếm quyền ưu tiên (preemption), v.v.
- Hiểu vai trò của nhân và các lời gọi hệ thống.
- Có kiến thức thực hành về các thành phần bên trong của nhân, bao gồm: ngắt (interrupt), bộ lập lịch (scheduler), bộ nhớ ảo (virtual memory), và ngăn xếp I/O (I/O stack).
- Thấy cách các tính năng hiệu năng của nhân đã được thêm vào từ Unix đến Linux.
- Phát triển hiểu biết cơ bản về extended BPF.

Chương này cung cấp tổng quan về các hệ điều hành và nhân, và được coi là kiến thức nền tảng cho phần còn lại của cuốn sách. Nếu bạn đã bỏ lỡ lớp học về hệ điều hành, bạn có thể coi đây là một khóa học cấp tốc. Hãy chú ý đến bất kỳ lỗ hổng nào trong kiến thức của bạn, vì sẽ có một bài kiểm tra ở cuối (tôi đùa thôi; nó chỉ là một bài trắc nghiệm). Để biết thêm về các thành phần bên trong của nhân, hãy xem phần tài liệu tham khảo ở cuối chương này.

Chương này có ba phần:

- **Thuật ngữ** liệt kê các thuật ngữ thiết yếu.
- **Kiến thức nền** tóm tắt các khái niệm chính về hệ điều hành và nhân.
- **Các nhân** tóm tắt các chi tiết triển khai cụ thể của Linux và các nhân khác.

Các lĩnh vực liên quan đến hiệu năng, bao gồm lập lịch CPU, bộ nhớ, đĩa, hệ thống tệp, mạng, và nhiều công cụ hiệu năng cụ thể, được đề cập chi tiết hơn trong các chương tiếp theo.

## 3.1 Thuật ngữ

Để tham khảo, đây là thuật ngữ cốt lõi về hệ điều hành được sử dụng trong cuốn sách này. Nhiều trong số này cũng là các khái niệm được giải thích chi tiết hơn trong chương này và các chương sau.

- **Hệ điều hành (Operating system):** Đề cập đến phần mềm và các tệp được cài đặt trên một hệ thống để nó có thể khởi động và thực thi các chương trình. Nó bao gồm nhân, các công cụ quản trị, và các thư viện hệ thống.
- **Nhân (Kernel):** Nhân là chương trình quản lý hệ thống, bao gồm (tùy thuộc vào mô hình nhân) các thiết bị phần cứng, bộ nhớ, và lập lịch CPU. Nó chạy trong chế độ CPU đặc quyền cho phép truy cập trực tiếp vào phần cứng, gọi là chế độ nhân (kernel mode).
- **Tiến trình (Process):** Một sự trừu tượng hóa và môi trường của hệ điều hành để thực thi một chương trình. Chương trình chạy trong chế độ người dùng (user mode), với quyền truy cập vào chế độ nhân (ví dụ: để thực hiện I/O thiết bị) thông qua các lời gọi hệ thống hoặc trap vào nhân.
- **Luồng (Thread):** Một ngữ cảnh thực thi có thể được lập lịch để chạy trên CPU. Nhân có nhiều luồng, và một tiến trình chứa một hoặc nhiều luồng.
- **Tác vụ (Task):** Một thực thể có thể chạy trong Linux, có thể đề cập đến một tiến trình (với một luồng đơn), một luồng từ một tiến trình đa luồng, hoặc các luồng nhân.
- **Chương trình BPF (BPF program):** Một chương trình chế độ nhân chạy trong môi trường thực thi BPF<sup>1</sup>.
- **Bộ nhớ chính (Main memory):** Bộ nhớ vật lý của hệ thống (ví dụ: RAM).
- **Bộ nhớ ảo (Virtual memory):** Một sự trừu tượng hóa của bộ nhớ chính hỗ trợ đa nhiệm và đăng ký vượt mức (over-subscription). Trên thực tế, nó là một tài nguyên vô hạn.
- **Không gian nhân (Kernel space):** Không gian địa chỉ bộ nhớ ảo dành cho nhân.
- **Không gian người dùng (User space):** Không gian địa chỉ bộ nhớ ảo dành cho các tiến trình.
- **User land:** Các chương trình và thư viện cấp người dùng (/usr/bin, /usr/lib...).
- **Chuyển đổi ngữ cảnh (Context switch):** Việc chuyển từ chạy một luồng hoặc tiến trình sang một luồng/tiến trình khác. Đây là một chức năng bình thường của bộ lập lịch CPU của nhân, và bao gồm việc chuyển đổi tập các thanh ghi CPU đang chạy (ngữ cảnh luồng) sang một tập mới.
- **Chuyển đổi chế độ (Mode switch):** Việc chuyển đổi giữa chế độ nhân và chế độ người dùng.
- **Lời gọi hệ thống (System call / syscall):** Một giao thức được định nghĩa rõ ràng để các chương trình người dùng yêu cầu nhân thực hiện các thao tác đặc quyền, bao gồm I/O thiết bị.
- **Bộ xử lý (Processor):** Không nên nhầm lẫn với tiến trình (process), bộ xử lý là một chip vật lý chứa một hoặc nhiều CPU.
- **Trap:** Một tín hiệu được gửi đến nhân để yêu cầu một thủ tục hệ thống (hành động đặc quyền). Các loại trap bao gồm lời gọi hệ thống, ngoại lệ bộ xử lý, và ngắt.
- **Ngắt phần cứng (Hardware interrupt):** Một tín hiệu được gửi bởi các thiết bị vật lý đến nhân, thường để yêu cầu phục vụ I/O. Ngắt là một loại trap.

> <sup>1</sup> BPF ban đầu là viết tắt của Berkeley Packet Filter, nhưng công nghệ ngày nay có rất ít liên quan đến Berkeley, các gói tin, hay lọc, nên BPF đã trở thành một tên gọi riêng thay vì một từ viết tắt.

Bảng thuật ngữ bao gồm thêm các thuật ngữ để tham khảo nếu cần cho chương này, bao gồm không gian địa chỉ (address space), bộ đệm (buffer), CPU, bộ mô tả tệp (file descriptor), POSIX, và các thanh ghi (register).

## 3.2 Kiến thức nền

Các phần sau mô tả các khái niệm chung về hệ điều hành và nhân, và sẽ giúp bạn hiểu bất kỳ hệ điều hành nào. Để hỗ trợ sự hiểu biết của bạn, phần này bao gồm một số chi tiết triển khai của Linux. Các phần tiếp theo, 3.3 Các nhân, và 3.4 Linux, tập trung vào các chi tiết triển khai cụ thể của nhân Unix, BSD, và Linux.

### 3.2.1 Nhân (Kernel)

Nhân là phần mềm cốt lõi của hệ điều hành. Những gì nó làm phụ thuộc vào mô hình nhân: các hệ điều hành giống Unix bao gồm Linux và BSD có nhân nguyên khối (monolithic kernel) quản lý lập lịch CPU, bộ nhớ, hệ thống tệp, giao thức mạng, và các thiết bị hệ thống (đĩa, giao diện mạng, v.v.). Mô hình nhân này được minh họa trong Hình 3.1.

*Hình 3.1: Vai trò của nhân hệ điều hành nguyên khối*

Cũng được hiển thị là các thư viện hệ thống, thường được sử dụng để cung cấp giao diện lập trình phong phú và dễ sử dụng hơn so với chỉ các lời gọi hệ thống. Các ứng dụng bao gồm tất cả phần mềm cấp người dùng đang chạy, bao gồm cơ sở dữ liệu, máy chủ web, công cụ quản trị, và shell hệ điều hành.

Các thư viện hệ thống được minh họa ở đây dưới dạng vòng tròn bị đứt để cho thấy rằng các ứng dụng có thể gọi trực tiếp các lời gọi hệ thống (syscall).<sup>2</sup> Ví dụ, runtime của Golang có lớp syscall riêng không yêu cầu thư viện hệ thống libc. Theo truyền thống, sơ đồ này được vẽ với các vòng tròn hoàn chỉnh, phản ánh các mức đặc quyền giảm dần bắt đầu với nhân ở trung tâm (một mô hình có nguồn gốc từ Multics [Graham 68], tiền thân của Unix).

Các mô hình nhân khác cũng tồn tại: nhân vi mô (microkernel) sử dụng một nhân nhỏ với chức năng được chuyển sang các chương trình chế độ người dùng; và unikernel biên dịch mã nhân và ứng dụng cùng nhau thành một chương trình duy nhất. Cũng có các nhân lai (hybrid kernel), chẳng hạn như nhân Windows NT, sử dụng các cách tiếp cận từ cả nhân nguyên khối và nhân vi mô. Những điều này được tóm tắt trong Mục 3.5, Các chủ đề khác.

Linux gần đây đã thay đổi mô hình của mình bằng cách cho phép một loại phần mềm mới: Extended BPF, cho phép các ứng dụng chế độ nhân an toàn cùng với API nhân riêng của nó: BPF helper. Điều này cho phép một số ứng dụng và chức năng hệ thống được viết lại bằng BPF, cung cấp mức độ bảo mật và hiệu năng cao hơn. Điều này được minh họa trong Hình 3.2.

*Hình 3.2: Các ứng dụng BPF*

Extended BPF được tóm tắt trong Mục 3.4.4, Extended BPF.

> <sup>2</sup> Có một số ngoại lệ cho mô hình này. Các công nghệ bỏ qua nhân (kernel bypass), đôi khi được sử dụng cho mạng, cho phép cấp người dùng truy cập trực tiếp vào phần cứng (xem Chương 10, Mạng, Mục 10.4.3, Phần mềm, đề mục Kernel Bypass). I/O đến phần cứng cũng có thể được gửi mà không tốn chi phí của giao diện syscall (mặc dù syscall là bắt buộc để khởi tạo), ví dụ, với I/O ánh xạ bộ nhớ (memory-mapped I/O), lỗi trang lớn (major fault) (xem Chương 7, Bộ nhớ, Mục 7.2.3, Phân trang theo yêu cầu), sendfile(2), và Linux io_uring (xem Chương 5, Ứng dụng, Mục 5.2.6, I/O không chặn).

**Thực thi nhân**

Nhân là một chương trình lớn, thường có hàng triệu dòng mã. Nó chủ yếu thực thi theo yêu cầu, khi một chương trình cấp người dùng thực hiện lời gọi hệ thống, hoặc một thiết bị gửi ngắt. Một số luồng nhân hoạt động bất đồng bộ để thực hiện các tác vụ bảo trì, có thể bao gồm thủ tục đồng hồ nhân và các tác vụ quản lý bộ nhớ, nhưng chúng cố gắng hoạt động nhẹ nhàng và tiêu thụ rất ít tài nguyên CPU.

Các khối lượng công việc thực hiện I/O thường xuyên, chẳng hạn như máy chủ web, thực thi chủ yếu trong ngữ cảnh nhân. Các khối lượng công việc tính toán chuyên sâu thường chạy trong chế độ người dùng, không bị nhân gián đoạn. Có thể bạn sẽ nghĩ rằng nhân không thể ảnh hưởng đến hiệu năng của các khối lượng công việc tính toán chuyên sâu này, nhưng có nhiều trường hợp nó có ảnh hưởng. Rõ ràng nhất là tranh chấp CPU, khi các luồng khác đang cạnh tranh tài nguyên CPU và bộ lập lịch nhân cần quyết định luồng nào sẽ chạy và luồng nào sẽ chờ. Nhân cũng chọn CPU nào mà luồng sẽ chạy trên đó và có thể chọn các CPU có bộ nhớ đệm phần cứng ấm hơn hoặc vị trí bộ nhớ tốt hơn cho tiến trình, để cải thiện đáng kể hiệu năng.

### 3.2.2 Chế độ nhân và chế độ người dùng

Nhân chạy trong một chế độ CPU đặc biệt gọi là chế độ nhân (kernel mode), cho phép truy cập đầy đủ vào các thiết bị và thực thi các lệnh đặc quyền. Nhân phân xử quyền truy cập thiết bị để hỗ trợ đa nhiệm, ngăn các tiến trình và người dùng truy cập dữ liệu của nhau trừ khi được phép rõ ràng.

Các chương trình người dùng (tiến trình) chạy trong chế độ người dùng (user mode), nơi chúng yêu cầu các thao tác đặc quyền từ nhân thông qua lời gọi hệ thống, chẳng hạn như cho I/O.

Chế độ nhân và người dùng được triển khai trên bộ xử lý sử dụng các vòng đặc quyền (privilege ring) (hoặc vòng bảo vệ - protection ring) theo mô hình trong Hình 3.1. Ví dụ, bộ xử lý x86 hỗ trợ bốn vòng đặc quyền, được đánh số từ 0 đến 3. Thông thường chỉ có hai hoặc ba vòng được sử dụng: cho chế độ người dùng, chế độ nhân, và hypervisor nếu có. Các lệnh đặc quyền để truy cập thiết bị chỉ được phép trong chế độ nhân; thực thi chúng trong chế độ người dùng gây ra các ngoại lệ, sau đó được xử lý bởi nhân (ví dụ: để tạo lỗi từ chối quyền).

Trong nhân truyền thống, một lời gọi hệ thống được thực hiện bằng cách chuyển sang chế độ nhân và sau đó thực thi mã lời gọi hệ thống. Điều này được minh họa trong Hình 3.3.

*Hình 3.3: Các chế độ thực thi lời gọi hệ thống*

Chuyển đổi giữa chế độ người dùng và chế độ nhân là chuyển đổi chế độ (mode switch).

Tất cả các lời gọi hệ thống đều chuyển đổi chế độ. Một số lời gọi hệ thống cũng chuyển đổi ngữ cảnh: những lời gọi bị chặn (blocking), chẳng hạn như cho I/O đĩa và mạng, sẽ chuyển đổi ngữ cảnh để luồng khác có thể chạy trong khi luồng đầu tiên bị chặn.

Vì chuyển đổi chế độ và ngữ cảnh tốn một lượng nhỏ chi phí (chu kỳ CPU),<sup>3</sup> có nhiều tối ưu hóa để tránh chúng, bao gồm:

- **Syscall chế độ người dùng:** Có thể triển khai một số syscall chỉ trong thư viện chế độ người dùng. Nhân Linux thực hiện điều này bằng cách xuất một đối tượng chia sẻ động ảo (vDSO) được ánh xạ vào không gian địa chỉ tiến trình, chứa các syscall như gettimeofday(2) và getcpu(2) [Drysdale 14].
- **Ánh xạ bộ nhớ (Memory mapping):** Được sử dụng cho phân trang theo yêu cầu (demand paging) (xem Chương 7, Bộ nhớ, Mục 7.2.3, Phân trang theo yêu cầu), nó cũng có thể được sử dụng cho kho dữ liệu và I/O khác, tránh chi phí syscall.
- **Bỏ qua nhân (Kernel bypass):** Cho phép các chương trình chế độ người dùng truy cập trực tiếp vào thiết bị, bỏ qua syscall và đường dẫn mã nhân thông thường. Ví dụ, DPDK cho mạng: Data Plane Development Kit.
- **Ứng dụng chế độ nhân:** Bao gồm máy chủ web TUX [Lever 00], được triển khai trong nhân, và gần đây hơn là công nghệ extended BPF được minh họa trong Hình 3.2.

Chế độ nhân và người dùng có ngữ cảnh thực thi phần mềm riêng, bao gồm ngăn xếp và thanh ghi. Một số kiến trúc bộ xử lý (ví dụ: SPARC) sử dụng không gian địa chỉ riêng cho nhân, có nghĩa là chuyển đổi chế độ cũng phải thay đổi ngữ cảnh bộ nhớ ảo.

> <sup>3</sup> Với biện pháp giảm thiểu hiện tại cho lỗ hổng Meltdown, chuyển đổi ngữ cảnh giờ đây tốn kém hơn. Xem Mục 3.4.3 KPTI (Meltdown).

### 3.2.3 Lời gọi hệ thống (System Call)

Lời gọi hệ thống yêu cầu nhân thực hiện các thủ tục hệ thống đặc quyền. Có hàng trăm lời gọi hệ thống khả dụng, nhưng những người bảo trì nhân cố gắng giữ con số đó càng nhỏ càng tốt, để giữ cho nhân đơn giản (triết lý Unix; [Thompson 78]). Các giao diện phức tạp hơn có thể được xây dựng trên chúng trong user-land dưới dạng thư viện hệ thống, nơi chúng dễ phát triển và bảo trì hơn. Các hệ điều hành thường bao gồm thư viện C chuẩn cung cấp giao diện dễ sử dụng hơn cho nhiều syscall phổ biến (ví dụ: thư viện libc hoặc glibc).

Các lời gọi hệ thống chính cần nhớ được liệt kê trong Bảng 3.1.

**Bảng 3.1: Các lời gọi hệ thống chính**

| Lời gọi hệ thống | Mô tả |
|---|---|
| read(2) | Đọc các byte |
| write(2) | Ghi các byte |
| open(2) | Mở một tệp |
| close(2) | Đóng một tệp |
| fork(2) | Tạo một tiến trình mới |
| clone(2) | Tạo một tiến trình hoặc luồng mới |
| exec(2) | Thực thi một chương trình mới |
| connect(2) | Kết nối đến một máy chủ mạng |
| accept(2) | Chấp nhận một kết nối mạng |
| stat(2) | Lấy thống kê tệp |
| ioctl(2) | Thiết lập thuộc tính I/O, hoặc các chức năng linh tinh khác |
| mmap(2) | Ánh xạ tệp vào không gian địa chỉ bộ nhớ |
| brk(2) | Mở rộng con trỏ heap |
| futex(2) | Mutex nhanh trong không gian người dùng |

Các lời gọi hệ thống được tài liệu hóa tốt, mỗi lời gọi có một trang man thường được phân phối cùng với hệ điều hành. Chúng cũng có giao diện đơn giản và nhất quán, và sử dụng mã lỗi để mô tả lỗi khi cần (ví dụ: ENOENT cho "không tìm thấy tệp hoặc thư mục").<sup>4</sup>

Nhiều trong số các lời gọi hệ thống này có mục đích rõ ràng. Dưới đây là một số lời gọi mà cách sử dụng phổ biến có thể ít rõ ràng hơn:

- **ioctl(2):** Thường được sử dụng để yêu cầu các hành động linh tinh từ nhân, đặc biệt cho các công cụ quản trị hệ thống, nơi mà một lời gọi hệ thống khác (rõ ràng hơn) không phù hợp. Xem ví dụ bên dưới.
- **mmap(2):** Thường được sử dụng để ánh xạ các tệp thực thi và thư viện vào không gian địa chỉ tiến trình, và cho các tệp ánh xạ bộ nhớ. Đôi khi được sử dụng để cấp phát bộ nhớ làm việc của tiến trình, thay vì malloc(2) dựa trên brk(2), để giảm tần suất syscall và cải thiện hiệu năng (điều này không phải lúc nào cũng hiệu quả do sự đánh đổi liên quan: quản lý ánh xạ bộ nhớ).
- **brk(2):** Được sử dụng để mở rộng con trỏ heap, xác định kích thước bộ nhớ làm việc của tiến trình. Nó thường được thực hiện bởi thư viện cấp phát bộ nhớ hệ thống, khi lời gọi malloc(3) (cấp phát bộ nhớ) không thể được đáp ứng từ không gian hiện có trong heap. Xem Chương 7, Bộ nhớ.
- **futex(2):** Syscall này được sử dụng để xử lý một phần của khóa không gian người dùng: phần có khả năng bị chặn.

Nếu một lời gọi hệ thống không quen thuộc, bạn có thể tìm hiểu thêm trong trang man của nó (đây là phần 2 của các trang man: syscalls).

Syscall ioctl(2) có thể là syscall khó học nhất, do tính chất mơ hồ của nó. Như một ví dụ về cách sử dụng, công cụ perf(1) của Linux (được giới thiệu trong Chương 6, CPU) thực hiện các hành động đặc quyền để điều phối đo lường hiệu năng. Thay vì thêm các lời gọi hệ thống cho mỗi hành động, một lời gọi hệ thống duy nhất được thêm: perf_event_open(2), trả về một bộ mô tả tệp để sử dụng với ioctl(2). Sau đó ioctl(2) có thể được gọi với các đối số khác nhau để thực hiện các hành động mong muốn khác nhau. Ví dụ, ioctl(fd, PERF_EVENT_IOC_ENABLE) kích hoạt đo lường. Các đối số, trong ví dụ này là PERF_EVENT_IOC_ENABLE, có thể được thêm và thay đổi dễ dàng hơn bởi nhà phát triển.

> <sup>4</sup> glibc cung cấp các lỗi này trong biến số nguyên errno (error number).

### 3.2.4 Ngắt (Interrupt)

Ngắt là một tín hiệu đến bộ xử lý rằng một sự kiện nào đó đã xảy ra cần được xử lý, và làm gián đoạn việc thực thi hiện tại của bộ xử lý để xử lý nó. Nó thường làm cho bộ xử lý chuyển sang chế độ nhân nếu chưa ở đó, lưu trạng thái luồng hiện tại, và sau đó chạy một thủ tục phục vụ ngắt (interrupt service routine - ISR) để xử lý sự kiện.

Có các ngắt bất đồng bộ (asynchronous) được tạo bởi phần cứng bên ngoài và các ngắt đồng bộ (synchronous) được tạo bởi các lệnh phần mềm. Chúng được minh họa trong Hình 3.4.

*Hình 3.4: Các loại ngắt*

Để đơn giản, Hình 3.4 hiển thị tất cả các ngắt được gửi đến nhân để xử lý; thực tế chúng được gửi đến CPU trước, CPU chọn ISR trong nhân để chạy sự kiện.

**Ngắt bất đồng bộ**

Các thiết bị phần cứng có thể gửi các yêu cầu phục vụ ngắt (IRQ) đến bộ xử lý, đến một cách bất đồng bộ so với phần mềm đang chạy. Các ví dụ về ngắt phần cứng bao gồm:

- Thiết bị đĩa báo hiệu hoàn thành I/O đĩa
- Phần cứng chỉ báo một điều kiện lỗi
- Giao diện mạng báo hiệu sự đến của một gói tin
- Thiết bị đầu vào: đầu vào từ bàn phím và chuột

Để giải thích khái niệm ngắt bất đồng bộ, một kịch bản ví dụ được minh họa trong Hình 3.5 cho thấy sự trôi qua của thời gian khi cơ sở dữ liệu (MySQL) chạy trên CPU 0 đọc từ hệ thống tệp. Nội dung hệ thống tệp phải được lấy từ đĩa, vì vậy bộ lập lịch chuyển đổi ngữ cảnh sang luồng khác (ứng dụng Java) trong khi cơ sở dữ liệu đang chờ. Một lúc sau, I/O đĩa hoàn thành, nhưng tại thời điểm này cơ sở dữ liệu không còn chạy trên CPU 0. Ngắt hoàn thành đã xảy ra bất đồng bộ so với cơ sở dữ liệu, được thể hiện bằng đường nét đứt trong Hình 3.5.

*Hình 3.5: Ví dụ ngắt bất đồng bộ*

**Ngắt đồng bộ**

Ngắt đồng bộ được tạo bởi các lệnh phần mềm. Phần sau mô tả các loại ngắt phần mềm khác nhau sử dụng các thuật ngữ trap, ngoại lệ (exception), và lỗi trang (fault); tuy nhiên, các thuật ngữ này thường được sử dụng thay thế cho nhau.

- **Trap:** Một lời gọi có chủ đích vào nhân, chẳng hạn bởi lệnh int (interrupt). Một cách triển khai syscall liên quan đến việc gọi lệnh int với một vector cho trình xử lý syscall (ví dụ: int 0x80 trên Linux x86). int tạo ra một ngắt phần mềm.
- **Ngoại lệ (Exception):** Một điều kiện ngoại lệ, chẳng hạn bởi một lệnh thực hiện phép chia cho số không.
- **Lỗi trang (Fault):** Thuật ngữ thường được sử dụng cho các sự kiện bộ nhớ, chẳng hạn như lỗi trang được kích hoạt bởi việc truy cập một vị trí bộ nhớ mà không có ánh xạ MMU. Xem Chương 7, Bộ nhớ.

Đối với các ngắt này, phần mềm và lệnh chịu trách nhiệm vẫn đang ở trên CPU.

**Luồng ngắt (Interrupt Thread)**

Các thủ tục phục vụ ngắt (ISR) được thiết kế để hoạt động nhanh nhất có thể, nhằm giảm ảnh hưởng của việc gián đoạn các luồng đang hoạt động. Nếu một ngắt cần thực hiện nhiều hơn một ít công việc, đặc biệt nếu nó có thể bị chặn trên các khóa (lock), nó có thể được xử lý bởi một luồng ngắt có thể được lập lịch bởi nhân. Điều này được minh họa trong Hình 3.6.

*Hình 3.6: Xử lý ngắt*

Cách triển khai điều này phụ thuộc vào phiên bản nhân. Trên Linux, trình điều khiển thiết bị có thể được mô hình hóa thành hai nửa, với nửa trên (top half) xử lý ngắt nhanh chóng, và lập lịch công việc cho nửa dưới (bottom half) để xử lý sau [Corbet 05]. Xử lý ngắt nhanh chóng là quan trọng vì nửa trên chạy trong chế độ vô hiệu hóa ngắt để hoãn việc gửi các ngắt mới, điều này có thể gây ra vấn đề độ trễ cho các luồng khác nếu nó chạy quá lâu. Nửa dưới có thể là tasklet hoặc hàng đợi công việc (work queue); hàng đợi công việc là các luồng có thể được lập lịch bởi nhân và có thể ngủ khi cần thiết.

Ví dụ, trình điều khiển mạng Linux có nửa trên để xử lý IRQ cho các gói tin đến, gọi nửa dưới để đẩy gói tin lên ngăn xếp mạng. Nửa dưới được triển khai dưới dạng softirq (ngắt phần mềm).

Thời gian từ khi ngắt đến cho đến khi nó được phục vụ là độ trễ ngắt (interrupt latency), phụ thuộc vào phần cứng và cách triển khai. Đây là chủ đề nghiên cứu cho các hệ thống thời gian thực hoặc độ trễ thấp.

**Che ngắt (Interrupt Masking)**

Một số đường dẫn mã trong nhân không thể bị gián đoạn một cách an toàn. Một ví dụ là mã nhân giành một spin lock trong một lời gọi hệ thống, cho spin lock cũng có thể cần bởi một ngắt. Nhận một ngắt khi đang giữ khóa như vậy có thể gây ra deadlock. Để ngăn tình huống như vậy, nhân có thể tạm thời che (mask) ngắt bằng cách thiết lập thanh ghi mặt nạ ngắt (interrupt mask register) của CPU. Thời gian vô hiệu hóa ngắt nên càng ngắn càng tốt, vì nó có thể xáo trộn việc thực thi kịp thời của các ứng dụng được đánh thức bởi các ngắt khác. Đây là một yếu tố quan trọng cho các hệ thống thời gian thực — những hệ thống có yêu cầu nghiêm ngặt về thời gian phản hồi. Thời gian vô hiệu hóa ngắt cũng là mục tiêu của phân tích hiệu năng (phân tích như vậy được hỗ trợ trực tiếp bởi bộ truy vết irqsoff của Ftrace, được đề cập trong Chương 14, Ftrace).

Một số sự kiện ưu tiên cao không nên bị bỏ qua, và do đó được triển khai dưới dạng ngắt không thể che (non-maskable interrupt - NMI). Ví dụ, Linux có thể sử dụng bộ hẹn giờ watchdog Intelligent Platform Management Interface (IPMI) để kiểm tra xem nhân có bị khóa cứng hay không dựa trên sự thiếu ngắt trong một khoảng thời gian. Nếu vậy, watchdog có thể phát hành ngắt NMI để khởi động lại hệ thống.<sup>5</sup>

> <sup>5</sup> Linux cũng có watchdog NMI phần mềm để phát hiện tình trạng khóa cứng [Linux 20d].

### 3.2.5 Đồng hồ và trạng thái rỗi (Clock and Idle)

Một thành phần cốt lõi của nhân Unix ban đầu là thủ tục clock(), được thực thi từ ngắt hẹn giờ (timer interrupt). Nó trong lịch sử được thực thi 60, 100, hoặc 1.000 lần mỗi giây<sup>6</sup> (thường được biểu thị bằng Hertz: chu kỳ trên giây), và mỗi lần thực thi được gọi là một tick.<sup>7</sup> Các chức năng của nó bao gồm cập nhật thời gian hệ thống, hết hạn timer và lát thời gian (time slice) cho lập lịch luồng, duy trì thống kê CPU, và thực thi các thủ tục nhân đã lên lịch.

Đã có các vấn đề hiệu năng với đồng hồ, được cải thiện trong các nhân sau này, bao gồm:

- **Độ trễ tick:** Đối với đồng hồ 100 Hertz, có thể gặp thêm đến 10 ms độ trễ cho một timer khi nó chờ được xử lý trong tick tiếp theo. Điều này đã được khắc phục bằng cách sử dụng ngắt thời gian thực độ phân giải cao để thực thi ngay lập tức.
- **Chi phí tick:** Tick tiêu tốn chu kỳ CPU và gây nhiễu nhẹ cho các ứng dụng, và là một nguyên nhân của cái được biết đến là jitter hệ điều hành. Các bộ xử lý hiện đại cũng có tính năng quản lý năng lượng động, có thể tắt nguồn các phần trong thời gian rỗi. Thủ tục đồng hồ làm gián đoạn thời gian rỗi này, có thể tiêu tốn năng lượng một cách không cần thiết.

Các nhân hiện đại đã chuyển nhiều chức năng ra khỏi thủ tục đồng hồ sang ngắt theo yêu cầu, trong nỗ lực tạo ra nhân không tick (tickless kernel). Điều này giảm chi phí và cải thiện hiệu quả năng lượng bằng cách cho phép bộ xử lý duy trì trạng thái ngủ lâu hơn.

Thủ tục đồng hồ Linux là scheduler_tick(), và Linux có các cách để bỏ qua việc gọi đồng hồ khi không có tải CPU. Bản thân đồng hồ thường chạy ở 250 Hertz (được cấu hình bởi tùy chọn Kconfig CONFIG_HZ và các biến thể), và các lần gọi của nó được giảm bớt bởi chức năng NO_HZ (được cấu hình bởi CONFIG_NO_HZ và các biến thể), hiện thường được kích hoạt [Linux 20a].

> <sup>6</sup> Các tốc độ khác bao gồm 250 cho Linux 2.6.13, 256 cho Ultrix, và 1.024 cho OSF/1 [Mills 94].

> <sup>7</sup> Linux cũng theo dõi jiffies, một đơn vị thời gian tương tự như tick.

**Luồng rỗi (Idle Thread)**

Khi không có công việc cho CPU thực hiện, nhân lập lịch một luồng giữ chỗ chờ công việc, gọi là luồng rỗi (idle thread). Một triển khai đơn giản sẽ kiểm tra tính khả dụng của công việc mới trong một vòng lặp. Trong Linux hiện đại, tác vụ rỗi có thể gọi lệnh hlt (halt) để tắt nguồn CPU cho đến khi ngắt tiếp theo được nhận, tiết kiệm năng lượng.

### 3.2.6 Tiến trình (Process)

Một tiến trình là một môi trường để thực thi chương trình cấp người dùng. Nó bao gồm một không gian địa chỉ bộ nhớ, các bộ mô tả tệp, ngăn xếp luồng, và thanh ghi. Ở một số khía cạnh, một tiến trình giống như một máy tính thời kỳ đầu ảo, nơi mà chỉ có một chương trình đang thực thi với các thanh ghi và ngăn xếp riêng.

Các tiến trình được đa nhiệm bởi nhân, thường hỗ trợ thực thi hàng nghìn tiến trình trên một hệ thống đơn. Chúng được xác định riêng lẻ bởi ID tiến trình (PID), là một định danh số duy nhất.

Một tiến trình chứa một hoặc nhiều luồng, hoạt động trong không gian địa chỉ của tiến trình và chia sẻ cùng các bộ mô tả tệp. Một luồng là một ngữ cảnh thực thi bao gồm ngăn xếp, thanh ghi, và con trỏ lệnh (instruction pointer) (còn gọi là bộ đếm chương trình - program counter). Nhiều luồng cho phép một tiến trình đơn thực thi song song trên nhiều CPU. Trên Linux, luồng và tiến trình đều là tác vụ (task).

Tiến trình đầu tiên được khởi chạy bởi nhân được gọi là "init," từ /sbin/init (mặc định), với PID 1, khởi chạy các dịch vụ không gian người dùng. Trong Unix, điều này liên quan đến việc chạy các script khởi động từ /etc, một phương pháp nay được gọi là SysV (theo Unix System V). Các bản phân phối Linux ngày nay thường sử dụng phần mềm systemd để khởi động dịch vụ và theo dõi các phụ thuộc của chúng.

**Tạo tiến trình**

Các tiến trình thường được tạo bằng lời gọi hệ thống fork(2) trên các hệ thống Unix. Trên Linux, các thư viện C thường triển khai hàm fork bằng cách bọc quanh syscall đa năng clone(2). Các syscall này tạo bản sao của tiến trình, với ID tiến trình riêng. Lời gọi hệ thống exec(2) (hoặc biến thể, như execve(2)) sau đó có thể được gọi để bắt đầu thực thi một chương trình khác.

Hình 3.7 cho thấy ví dụ về tạo tiến trình cho shell bash thực thi lệnh ls.

*Hình 3.7: Tạo tiến trình*

Syscall fork(2) hoặc clone(2) có thể sử dụng chiến lược sao chép khi ghi (copy-on-write - COW) để cải thiện hiệu năng. Điều này thêm các tham chiếu đến không gian địa chỉ trước đó thay vì sao chép tất cả nội dung. Khi một trong hai tiến trình sửa đổi bộ nhớ được tham chiếu nhiều lần, một bản sao riêng biệt sau đó được tạo cho các sửa đổi. Chiến lược này hoãn lại hoặc loại bỏ nhu cầu sao chép bộ nhớ, giảm sử dụng bộ nhớ và CPU.

**Vòng đời tiến trình**

Vòng đời của một tiến trình được minh họa trong Hình 3.8. Đây là sơ đồ đơn giản hóa; đối với các hệ điều hành đa luồng hiện đại, chính các luồng được lập lịch và chạy, và có một số chi tiết triển khai bổ sung về cách chúng ánh xạ vào trạng thái tiến trình (xem Hình 5.6 và 5.7 trong Chương 5 để có sơ đồ chi tiết hơn).

*Hình 3.8: Vòng đời tiến trình*

Trạng thái on-proc là khi đang chạy trên bộ xử lý (CPU). Trạng thái ready-to-run (sẵn sàng chạy) là khi tiến trình có thể chạy nhưng đang chờ trên hàng đợi chạy (run queue) của CPU để đến lượt trên CPU. Hầu hết I/O sẽ chặn, đưa tiến trình vào trạng thái ngủ (sleep) cho đến khi I/O hoàn thành và tiến trình được đánh thức. Trạng thái zombie xảy ra trong quá trình kết thúc tiến trình, khi tiến trình chờ cho đến khi trạng thái tiến trình của nó được thu hồi bởi tiến trình cha hoặc cho đến khi nó bị loại bỏ bởi nhân.

**Môi trường tiến trình**

Môi trường tiến trình được minh họa trong Hình 3.9; nó bao gồm dữ liệu trong không gian địa chỉ của tiến trình và siêu dữ liệu (ngữ cảnh) trong nhân.

*Hình 3.9: Môi trường tiến trình*

Ngữ cảnh nhân bao gồm các thuộc tính và thống kê tiến trình khác nhau: ID tiến trình (PID), ID người dùng (UID) của chủ sở hữu, và các thời gian khác nhau. Những thông tin này thường được kiểm tra thông qua các lệnh ps(1) và top(1). Nó cũng có một tập các bộ mô tả tệp, tham chiếu đến các tệp đang mở và (thường) được chia sẻ giữa các luồng.

Ví dụ này minh họa hai luồng, mỗi luồng chứa một số siêu dữ liệu, bao gồm mức ưu tiên trong ngữ cảnh nhân<sup>8</sup> và ngăn xếp người dùng trong không gian địa chỉ người dùng. Sơ đồ không được vẽ theo tỷ lệ; ngữ cảnh nhân rất nhỏ so với không gian địa chỉ tiến trình.

Không gian địa chỉ người dùng chứa các phân đoạn bộ nhớ của tiến trình: tệp thực thi, thư viện, và heap. Để biết thêm chi tiết, xem Chương 7, Bộ nhớ.

Trên Linux, mỗi luồng có ngăn xếp người dùng riêng và ngăn xếp ngoại lệ nhân (kernel exception stack)<sup>9</sup> riêng [Owens 20].

> <sup>8</sup> Ngữ cảnh nhân có thể là không gian địa chỉ đầy đủ riêng (như với bộ xử lý SPARC) hoặc phạm vi hạn chế không trùng lặp với địa chỉ người dùng (như với bộ xử lý x86).

> <sup>9</sup> Cũng có các ngăn xếp nhân mục đích đặc biệt theo CPU, bao gồm các ngăn xếp được sử dụng cho ngắt.

### 3.2.7 Ngăn xếp (Stack)

Ngăn xếp là vùng lưu trữ bộ nhớ cho dữ liệu tạm thời, được tổ chức dưới dạng danh sách vào sau ra trước (LIFO - Last-In, First-Out). Nó được sử dụng để lưu trữ dữ liệu ít quan trọng hơn so với dữ liệu vừa trong tập thanh ghi CPU. Khi một hàm được gọi, địa chỉ trả về được lưu vào ngăn xếp. Một số thanh ghi cũng có thể được lưu vào ngăn xếp nếu giá trị của chúng cần thiết sau khi gọi.<sup>10</sup> Khi hàm được gọi đã hoàn thành, nó khôi phục bất kỳ thanh ghi nào cần thiết và, bằng cách lấy địa chỉ trả về từ ngăn xếp, chuyển thực thi đến hàm gọi. Ngăn xếp cũng có thể được sử dụng để truyền tham số cho các hàm. Tập dữ liệu trên ngăn xếp liên quan đến việc thực thi của một hàm được gọi là khung ngăn xếp (stack frame).

Đường dẫn gọi đến hàm đang thực thi hiện tại có thể được nhìn thấy bằng cách kiểm tra các địa chỉ trả về đã lưu qua tất cả các khung ngăn xếp trong ngăn xếp của luồng (một quá trình gọi là duyệt ngăn xếp - stack walking).<sup>11</sup> Đường dẫn gọi này được gọi là stack back trace hoặc stack trace. Trong kỹ thuật hiệu năng, nó thường chỉ được gọi ngắn gọn là "stack." Các ngăn xếp này có thể trả lời tại sao một thứ đang thực thi, và là công cụ vô giá cho gỡ lỗi và phân tích hiệu năng.

> <sup>10</sup> Quy ước gọi từ ABI bộ xử lý chỉ định thanh ghi nào nên giữ giá trị sau khi gọi hàm (chúng là non-volatile) và được lưu vào ngăn xếp bởi hàm được gọi ("callee-saves"). Các thanh ghi khác là volatile và có thể bị ghi đè bởi hàm được gọi; nếu hàm gọi muốn giữ giá trị của chúng, nó phải lưu chúng vào ngăn xếp ("caller-saves").

> <sup>11</sup> Để biết thêm chi tiết về duyệt ngăn xếp và các kỹ thuật khả dụng khác nhau (bao gồm: dựa trên frame-pointer, debuginfo, last branch record, và ORC) xem Chương 2, Kỹ thuật, Mục 2.4, Duyệt Stack Trace, của BPF Performance Tools [Gregg 19].

**Cách đọc một Stack**

Ví dụ ngăn xếp nhân sau (từ Linux) cho thấy đường dẫn được thực hiện cho truyền TCP, như được in bởi công cụ truy vết:

```
tcp_sendmsg+1
sock_sendmsg+62
SYSC_sendto+319
sys_sendto+14
do_syscall_64+115
entry_SYSCALL_64_after_hwframe+61
```

Ngăn xếp thường được in theo thứ tự từ lá đến gốc (leaf-to-root), vì vậy dòng đầu tiên được in là hàm đang thực thi hiện tại, và bên dưới nó là hàm cha, sau đó là hàm ông, v.v. Trong ví dụ này, hàm tcp_sendmsg() đang thực thi, được gọi bởi sock_sendmsg(). Trong ví dụ ngăn xếp này, bên phải tên hàm là độ lệch lệnh (instruction offset), cho thấy vị trí trong một hàm. Dòng đầu tiên hiển thị tcp_sendmsg() offset 1 (là lệnh thứ hai), được gọi bởi sock_sendmsg() offset 62. Offset này chỉ hữu ích nếu bạn muốn hiểu chi tiết cấp thấp về đường dẫn mã, xuống đến cấp lệnh.

Bằng cách đọc xuống ngăn xếp, toàn bộ tổ tiên có thể được nhìn thấy: hàm, cha, ông, v.v. Hoặc, bằng cách đọc từ dưới lên, bạn có thể theo dõi đường dẫn thực thi đến hàm hiện tại: cách chúng ta đến đây.

Vì ngăn xếp phơi bày đường dẫn nội bộ qua mã nguồn, thường không có tài liệu cho các hàm này ngoài chính mã nguồn. Đối với ngăn xếp ví dụ này, đó là mã nguồn nhân Linux. Một ngoại lệ là khi các hàm là một phần của API và được tài liệu hóa.

**Ngăn xếp người dùng và nhân**

Trong khi thực thi một lời gọi hệ thống, một luồng tiến trình có hai ngăn xếp: ngăn xếp cấp người dùng và ngăn xếp cấp nhân. Phạm vi của chúng được minh họa trong Hình 3.10.

*Hình 3.10: Ngăn xếp người dùng và nhân*

Ngăn xếp cấp người dùng của luồng bị chặn không thay đổi trong suốt thời gian của lời gọi hệ thống, vì luồng đang sử dụng ngăn xếp cấp nhân riêng biệt trong khi thực thi trong ngữ cảnh nhân. (Một ngoại lệ là bộ xử lý tín hiệu (signal handler), có thể mượn ngăn xếp cấp người dùng tùy thuộc vào cấu hình của chúng.)

Trên Linux, có nhiều ngăn xếp nhân cho các mục đích khác nhau. Syscall sử dụng ngăn xếp ngoại lệ nhân liên kết với mỗi luồng, và cũng có các ngăn xếp liên kết với ngắt mềm và ngắt cứng (IRQ) [Bovet 05].

### 3.2.8 Bộ nhớ ảo (Virtual Memory)

Bộ nhớ ảo là một trừu tượng hóa của bộ nhớ chính, cung cấp cho các tiến trình và nhân cái nhìn riêng tư, gần như vô hạn,<sup>12</sup> về bộ nhớ chính. Nó hỗ trợ đa nhiệm, cho phép các tiến trình và nhân hoạt động trên không gian địa chỉ riêng mà không lo lắng về tranh chấp. Nó cũng hỗ trợ đăng ký vượt mức (oversubscription) bộ nhớ chính, cho phép hệ điều hành ánh xạ bộ nhớ ảo một cách minh bạch giữa bộ nhớ chính và bộ lưu trữ thứ cấp (đĩa) khi cần.

Vai trò của bộ nhớ ảo được minh họa trong Hình 3.11. Bộ nhớ sơ cấp (primary memory) là bộ nhớ chính (RAM), và bộ nhớ thứ cấp (secondary memory) là các thiết bị lưu trữ (đĩa).

*Hình 3.11: Không gian địa chỉ bộ nhớ ảo<sup>13</sup>*

Bộ nhớ ảo được thực hiện nhờ sự hỗ trợ từ cả bộ xử lý và hệ điều hành. Nó không phải là bộ nhớ thực, và hầu hết các hệ điều hành ánh xạ bộ nhớ ảo sang bộ nhớ thực chỉ khi có yêu cầu, khi bộ nhớ lần đầu được ghi dữ liệu (populated).

Xem Chương 7, Bộ nhớ, để tìm hiểu thêm về bộ nhớ ảo.

> <sup>12</sup> Trên bộ xử lý 64-bit. Đối với bộ xử lý 32-bit, bộ nhớ ảo bị giới hạn ở 4 Gbyte do giới hạn của địa chỉ 32-bit (và nhân có thể giới hạn nó xuống mức còn nhỏ hơn).

> <sup>13</sup> Bộ nhớ ảo của tiến trình được hiển thị bắt đầu từ 0 như một sự đơn giản hóa. Các nhân ngày nay thường bắt đầu không gian địa chỉ ảo của tiến trình tại một offset như 0x10000 hoặc địa chỉ ngẫu nhiên. Một lợi ích là lỗi lập trình phổ biến của việc truy xuất con trỏ NULL (0) sẽ làm chương trình crash (SIGSEGV) vì địa chỉ 0 là không hợp lệ. Điều này thường tốt hơn so với việc truy xuất dữ liệu tại địa chỉ 0 do nhầm lẫn, vì chương trình sẽ tiếp tục chạy với dữ liệu bị hỏng.

**Quản lý bộ nhớ**

Trong khi bộ nhớ ảo cho phép mở rộng bộ nhớ chính bằng bộ lưu trữ thứ cấp, nhân cố gắng giữ dữ liệu hoạt động nhất trong bộ nhớ chính. Có hai cơ chế nhân cho điều này:

- **Hoán đổi tiến trình (Process swapping):** di chuyển toàn bộ tiến trình giữa bộ nhớ chính và bộ lưu trữ thứ cấp.
- **Phân trang (Paging):** di chuyển các đơn vị bộ nhớ nhỏ gọi là trang (page) (ví dụ: 4 Kbyte).

Hoán đổi tiến trình là phương pháp Unix ban đầu và có thể gây mất hiệu năng nghiêm trọng. Phân trang hiệu quả hơn và được thêm vào BSD với sự ra đời của bộ nhớ ảo phân trang. Trong cả hai trường hợp, bộ nhớ ít được sử dụng gần đây nhất (hoặc không được sử dụng gần đây) được chuyển sang bộ lưu trữ thứ cấp và chỉ được chuyển lại bộ nhớ chính khi cần lại.

Trong Linux, thuật ngữ swapping được sử dụng để chỉ phân trang. Nhân Linux không hỗ trợ kiểu hoán đổi tiến trình Unix (cũ) của toàn bộ luồng và tiến trình.

Để biết thêm về phân trang và hoán đổi, xem Chương 7, Bộ nhớ.

### 3.2.9 Bộ lập lịch (Scheduler)

Unix và các hệ thống phái sinh của nó là các hệ thống chia sẻ thời gian (time-sharing), cho phép nhiều tiến trình chạy cùng lúc bằng cách chia thời gian thực thi giữa chúng. Việc lập lịch tiến trình trên bộ xử lý và các CPU riêng lẻ được thực hiện bởi bộ lập lịch (scheduler), một thành phần quan trọng của nhân hệ điều hành. Vai trò của bộ lập lịch được minh họa trong Hình 3.12, cho thấy bộ lập lịch hoạt động trên các luồng (trong Linux là tác vụ), ánh xạ chúng vào CPU.

*Hình 3.12: Bộ lập lịch nhân*

Mục đích cơ bản là chia thời gian CPU giữa các tiến trình và luồng hoạt động, và duy trì khái niệm về mức ưu tiên để công việc quan trọng hơn có thể thực thi sớm hơn. Bộ lập lịch theo dõi tất cả các luồng trong trạng thái sẵn sàng chạy, theo truyền thống trên các hàng đợi theo mức ưu tiên gọi là hàng đợi chạy (run queue) [Bach 86]. Các nhân hiện đại có thể triển khai các hàng đợi này theo CPU và cũng có thể sử dụng các cấu trúc dữ liệu khác, ngoài hàng đợi, để theo dõi các luồng. Khi có nhiều luồng muốn chạy hơn số CPU khả dụng, các luồng ưu tiên thấp hơn chờ đến lượt. Hầu hết các luồng nhân chạy với mức ưu tiên cao hơn so với các tiến trình cấp người dùng.

Mức ưu tiên tiến trình có thể được bộ lập lịch sửa đổi động để cải thiện hiệu năng cho các khối lượng công việc nhất định. Các khối lượng công việc có thể được phân loại thành:

- **CPU-bound (bị ràng buộc bởi CPU):** Các ứng dụng thực hiện tính toán nặng, ví dụ, phân tích khoa học và toán học, được dự kiến có thời gian chạy dài (giây, phút, giờ, ngày, hoặc thậm chí lâu hơn). Chúng trở nên bị giới hạn bởi tài nguyên CPU.
- **I/O-bound (bị ràng buộc bởi I/O):** Các ứng dụng thực hiện I/O, với ít tính toán, ví dụ, máy chủ web, máy chủ tệp, và shell tương tác, nơi phản hồi độ trễ thấp là mong muốn. Khi tải của chúng tăng, chúng bị giới hạn bởi I/O đến tài nguyên lưu trữ hoặc mạng.

Một chính sách lập lịch thường được sử dụng có từ UNIX nhận dạng các khối lượng công việc CPU-bound và giảm mức ưu tiên của chúng, cho phép các khối lượng công việc I/O-bound — nơi mà phản hồi độ trễ thấp được mong muốn hơn — chạy sớm hơn. Điều này có thể đạt được bằng cách tính tỷ lệ thời gian tính toán gần đây (thời gian thực thi trên CPU) so với thời gian thực (thời gian trôi qua) và giảm mức ưu tiên của các tiến trình có tỷ lệ (tính toán) cao [Thompson 78]. Cơ chế này ưu tiên các tiến trình chạy ngắn hơn, thường là những tiến trình thực hiện I/O, bao gồm các tiến trình tương tác con người.

Các nhân hiện đại hỗ trợ nhiều lớp lập lịch (scheduling class) hoặc chính sách lập lịch (scheduling policy) (Linux) áp dụng các thuật toán khác nhau để quản lý mức ưu tiên và các luồng có thể chạy. Chúng có thể bao gồm lập lịch thời gian thực (real-time scheduling), sử dụng mức ưu tiên cao hơn tất cả công việc không quan trọng, bao gồm các luồng nhân. Cùng với hỗ trợ chiếm quyền ưu tiên (preemption) (được mô tả sau), lập lịch thời gian thực cung cấp lập lịch có thể dự đoán và độ trễ thấp cho các hệ thống yêu cầu.

Xem Chương 6, CPU, để biết thêm về bộ lập lịch nhân và các thuật toán lập lịch khác.

### 3.2.10 Hệ thống tệp (File System)

Hệ thống tệp là tổ chức dữ liệu dưới dạng tệp và thư mục. Chúng có giao diện dựa trên tệp để truy cập, thường dựa trên chuẩn POSIX. Nhân hỗ trợ nhiều loại và thể hiện hệ thống tệp. Cung cấp hệ thống tệp là một trong những vai trò quan trọng nhất của hệ điều hành, từng được mô tả là vai trò quan trọng nhất [Ritchie 74].

Hệ điều hành cung cấp không gian tên tệp toàn cục, được tổ chức dưới dạng cấu trúc cây từ trên xuống bắt đầu với cấp gốc ("/"). Các hệ thống tệp tham gia vào cây bằng cách gắn kết (mounting), gắn cây riêng của chúng vào một thư mục (điểm gắn kết - mount point). Điều này cho phép người dùng cuối điều hướng không gian tên tệp một cách minh bạch, bất kể loại hệ thống tệp bên dưới.

Một hệ điều hành điển hình có thể được tổ chức như trong Hình 3.13.

*Hình 3.13: Phân cấp tệp hệ điều hành*

Các thư mục cấp cao bao gồm etc cho tệp cấu hình hệ thống, usr cho chương trình và thư viện cấp người dùng do hệ thống cung cấp, dev cho các node thiết bị, var cho các tệp thay đổi bao gồm nhật ký hệ thống, tmp cho tệp tạm thời, và home cho thư mục chủ người dùng. Trong ví dụ được minh họa, var và home có thể nằm trên các thể hiện hệ thống tệp riêng và thiết bị lưu trữ riêng biệt; tuy nhiên, chúng có thể được truy cập như bất kỳ thành phần nào khác của cây.

Hầu hết các loại hệ thống tệp sử dụng thiết bị lưu trữ (đĩa) để chứa nội dung. Một số loại hệ thống tệp được tạo động bởi nhân, chẳng hạn như /proc và /dev.

Nhân thường cung cấp các cách khác nhau để cô lập tiến trình vào một phần của không gian tên tệp, bao gồm chroot(8), và trên Linux, mount namespace, thường được sử dụng cho container (xem Chương 11, Điện toán đám mây).

**VFS**

Hệ thống tệp ảo (virtual file system - VFS) là giao diện nhân để trừu tượng hóa các loại hệ thống tệp, ban đầu được phát triển bởi Sun Microsystems để hệ thống tệp Unix (UFS) và hệ thống tệp mạng (NFS) có thể cùng tồn tại dễ dàng hơn. Vai trò của nó được minh họa trong Hình 3.14.

*Hình 3.14: Hệ thống tệp ảo*

Giao diện VFS giúp dễ dàng thêm các loại hệ thống tệp mới vào nhân. Nó cũng hỗ trợ cung cấp không gian tên tệp toàn cục, được minh họa trước đó, để chương trình và ứng dụng người dùng có thể truy cập các loại hệ thống tệp khác nhau một cách minh bạch.

**Ngăn xếp I/O**

Đối với các hệ thống tệp dựa trên thiết bị lưu trữ, đường dẫn từ phần mềm cấp người dùng đến thiết bị lưu trữ được gọi là ngăn xếp I/O (I/O stack). Đây là một tập con của toàn bộ ngăn xếp phần mềm được hiển thị trước đó. Một ngăn xếp I/O chung được minh họa trong Hình 3.15.

*Hình 3.15: Ngăn xếp I/O chung*

Hình 3.15 cho thấy đường dẫn trực tiếp đến thiết bị khối (block device) ở bên trái, bỏ qua hệ thống tệp. Đường dẫn này đôi khi được sử dụng bởi các công cụ quản trị và cơ sở dữ liệu.

Hệ thống tệp và hiệu năng của chúng được đề cập chi tiết trong Chương 8, Hệ thống tệp, và các thiết bị lưu trữ mà chúng được xây dựng trên đó được đề cập trong Chương 9, Đĩa.

### 3.2.11 Bộ nhớ đệm (Caching)

Vì I/O đĩa trong lịch sử có độ trễ cao, nhiều lớp của ngăn xếp phần mềm cố gắng tránh nó bằng cách đệm (cache) các lần đọc và đệm (buffer) các lần ghi. Bộ nhớ đệm có thể bao gồm những lớp được hiển thị trong Bảng 3.2 (theo thứ tự chúng được kiểm tra).

**Bảng 3.2: Các lớp bộ nhớ đệm ví dụ cho I/O đĩa**

| # | Bộ nhớ đệm | Ví dụ |
|---|---|---|
| 1 | Bộ nhớ đệm máy khách (Client cache) | Bộ nhớ đệm trình duyệt web |
| 2 | Bộ nhớ đệm ứng dụng (Application cache) | — |
| 3 | Bộ nhớ đệm máy chủ web (Web server cache) | Bộ đệm Apache |
| 4 | Máy chủ đệm (Caching server) | memcached |
| 5 | Bộ nhớ đệm cơ sở dữ liệu (Database cache) | Bộ đệm MySQL |
| 6 | Bộ nhớ đệm thư mục (Directory cache) | dcache |
| 7 | Bộ nhớ đệm siêu dữ liệu tệp (File metadata cache) | inode cache |
| 8 | Bộ đệm hệ điều hành (OS buffer cache) | Buffer cache |
| 9 | Bộ nhớ đệm sơ cấp hệ thống tệp (FS primary cache) | Page cache, ZFS ARC |
| 10 | Bộ nhớ đệm thứ cấp hệ thống tệp (FS secondary cache) | ZFS L2ARC |
| 11 | Bộ nhớ đệm thiết bị (Device cache) | ZFS vdev |
| 12 | Bộ nhớ đệm khối (Block cache) | Buffer cache |
| 13 | Bộ nhớ đệm bộ điều khiển đĩa (Disk controller cache) | Bộ đệm thẻ RAID |
| 14 | Bộ nhớ đệm mảng lưu trữ (Storage array cache) | — |
| 15 | Bộ nhớ đệm trên đĩa (On-disk cache) | — |

Ví dụ, buffer cache là một vùng bộ nhớ chính lưu trữ các khối đĩa được sử dụng gần đây. Các lần đọc đĩa có thể được phục vụ ngay lập tức từ bộ nhớ đệm nếu khối được yêu cầu có mặt, tránh được độ trễ cao của I/O đĩa.

Các loại bộ nhớ đệm có mặt sẽ khác nhau tùy thuộc vào hệ thống và môi trường.

### 3.2.12 Mạng (Networking)

Các nhân hiện đại cung cấp một ngăn xếp giao thức mạng tích hợp, cho phép hệ thống giao tiếp qua mạng và tham gia vào các môi trường hệ thống phân tán. Ngăn xếp này được gọi là ngăn xếp mạng (networking stack) hoặc ngăn xếp TCP/IP, theo tên các giao thức TCP và IP thường được sử dụng. Các ứng dụng cấp người dùng truy cập mạng thông qua các điểm cuối lập trình được (programmable endpoint) gọi là socket.

Thiết bị vật lý kết nối với mạng là giao diện mạng (network interface) và thường được cung cấp trên card giao diện mạng (NIC - network interface card). Một nhiệm vụ lịch sử của quản trị viên hệ thống là liên kết địa chỉ IP với giao diện mạng, để nó có thể giao tiếp với mạng; các ánh xạ này hiện thường được tự động hóa thông qua giao thức cấu hình máy chủ động (DHCP - dynamic host configuration protocol).

Các giao thức mạng không thay đổi thường xuyên, nhưng có một giao thức truyền tải mới đang được chấp nhận ngày càng nhiều: QUIC (được tóm tắt trong Chương 10, Mạng). Các cải tiến và tùy chọn giao thức thay đổi thường xuyên hơn, chẳng hạn như các tùy chọn TCP mới hơn và thuật toán kiểm soát tắc nghẽn TCP. Các giao thức và cải tiến mới hơn thường yêu cầu hỗ trợ nhân (ngoại trừ các triển khai giao thức trong không gian người dùng). Một thay đổi khác là hỗ trợ cho các card giao diện mạng khác nhau, yêu cầu trình điều khiển thiết bị mới cho nhân.

Để biết thêm về mạng và hiệu năng mạng, xem Chương 10, Mạng.

### 3.2.13 Trình điều khiển thiết bị (Device Driver)

Nhân phải giao tiếp với nhiều loại thiết bị vật lý. Giao tiếp như vậy được thực hiện thông qua trình điều khiển thiết bị (device driver): phần mềm nhân để quản lý và I/O thiết bị. Trình điều khiển thiết bị thường được cung cấp bởi các nhà cung cấp phát triển thiết bị phần cứng. Một số nhân hỗ trợ trình điều khiển thiết bị có thể cắm (pluggable), có thể được tải và gỡ mà không yêu cầu khởi động lại hệ thống.

Trình điều khiển thiết bị có thể cung cấp giao diện ký tự (character) và/hoặc giao diện khối (block) cho thiết bị. Thiết bị ký tự, còn gọi là thiết bị thô (raw device), cung cấp truy cập tuần tự không đệm với bất kỳ kích thước I/O nào xuống đến một ký tự đơn, tùy thuộc vào thiết bị. Các thiết bị như vậy bao gồm bàn phím và cổng nối tiếp (và trong Unix ban đầu, thiết bị băng giấy và máy in dòng).

Thiết bị khối thực hiện I/O theo đơn vị khối, trong lịch sử có kích thước 512 byte mỗi khối. Chúng có thể được truy cập ngẫu nhiên dựa trên offset khối, bắt đầu từ 0 ở đầu thiết bị khối. Trong Unix ban đầu, giao diện thiết bị khối cũng cung cấp bộ nhớ đệm cho các bộ đệm thiết bị khối để cải thiện hiệu năng, trong một vùng bộ nhớ chính gọi là buffer cache. Trong Linux, buffer cache này hiện là một phần của page cache.

### 3.2.14 Đa bộ xử lý (Multiprocessor)

Hỗ trợ đa bộ xử lý cho phép hệ điều hành sử dụng nhiều thể hiện CPU để thực thi công việc song song. Nó thường được triển khai dưới dạng đa xử lý đối xứng (symmetric multiprocessing - SMP) trong đó tất cả CPU được xử lý bình đẳng. Điều này khó khăn về mặt kỹ thuật, gây ra các vấn đề cho việc truy cập và chia sẻ bộ nhớ và CPU giữa các luồng chạy song song. Trên hệ thống đa bộ xử lý, cũng có thể có các ngân hàng bộ nhớ chính được kết nối với các socket khác nhau (bộ xử lý vật lý) trong kiến trúc truy cập bộ nhớ không đồng nhất (non-uniform memory access - NUMA), cũng đặt ra thách thức về hiệu năng. Xem Chương 6, CPU, để biết chi tiết, bao gồm lập lịch và đồng bộ hóa luồng, và Chương 7, Bộ nhớ, để biết chi tiết về truy cập bộ nhớ và kiến trúc.

**IPI**

Đối với hệ thống đa bộ xử lý, có những lúc CPU cần phối hợp, chẳng hạn cho tính nhất quán bộ nhớ đệm của các mục dịch bộ nhớ (thông báo cho các CPU khác rằng một mục, nếu được đệm, hiện đã cũ). Một CPU có thể yêu cầu các CPU khác, hoặc tất cả CPU, thực hiện ngay lập tức công việc đó bằng ngắt liên xử lý (inter-processor interrupt - IPI) (còn gọi là lời gọi SMP hoặc CPU cross call). IPI là các ngắt bộ xử lý được thiết kế để thực thi nhanh chóng, nhằm giảm thiểu sự gián đoạn đối với các luồng khác.

IPI cũng có thể được sử dụng bởi cơ chế chiếm quyền ưu tiên (preemption).

### 3.2.15 Chiếm quyền ưu tiên (Preemption)

Hỗ trợ chiếm quyền ưu tiên nhân (kernel preemption) cho phép các luồng cấp người dùng ưu tiên cao gián đoạn nhân và thực thi. Điều này cho phép các hệ thống thời gian thực có thể thực thi công việc trong một ràng buộc thời gian nhất định, bao gồm các hệ thống được sử dụng bởi máy bay và thiết bị y tế. Một nhân hỗ trợ chiếm quyền ưu tiên được gọi là hoàn toàn có thể chiếm quyền (fully preemptible), mặc dù trên thực tế nó vẫn sẽ có một số đường dẫn mã quan trọng nhỏ không thể bị gián đoạn.

Một cách tiếp cận khác được Linux hỗ trợ là chiếm quyền ưu tiên nhân tự nguyện (voluntary kernel preemption), trong đó các điểm dừng logic trong mã nhân có thể kiểm tra và thực hiện chiếm quyền ưu tiên. Điều này tránh một số phức tạp của việc hỗ trợ nhân hoàn toàn có thể chiếm quyền và cung cấp chiếm quyền ưu tiên độ trễ thấp cho các khối lượng công việc phổ biến. Chiếm quyền ưu tiên nhân tự nguyện thường được kích hoạt trong Linux thông qua tùy chọn Kconfig CONFIG_PREEMPT_VOLUNTARY; cũng có CONFIG_PREEMPT cho phép tất cả mã nhân (trừ các đoạn quan trọng) có thể bị chiếm quyền, và CONFIG_PREEMPT_NONE để vô hiệu hóa chiếm quyền ưu tiên, cải thiện thông lượng với chi phí là độ trễ cao hơn.

### 3.2.16 Quản lý tài nguyên (Resource Management)

Hệ điều hành có thể cung cấp nhiều kiểm soát có thể cấu hình để tinh chỉnh quyền truy cập vào tài nguyên hệ thống, chẳng hạn như CPU, bộ nhớ, đĩa, và mạng. Đây là các kiểm soát tài nguyên (resource control) và có thể được sử dụng để quản lý hiệu năng trên các hệ thống chạy các ứng dụng khác nhau hoặc lưu trữ nhiều người thuê (tenant) (điện toán đám mây). Các kiểm soát như vậy có thể áp đặt giới hạn cố định cho mỗi tiến trình (hoặc nhóm tiến trình) về sử dụng tài nguyên, hoặc cách tiếp cận linh hoạt hơn — cho phép dung lượng dư thừa được chia sẻ giữa chúng.

Các phiên bản đầu tiên của Unix và BSD có các kiểm soát tài nguyên cơ bản cho mỗi tiến trình, bao gồm mức ưu tiên CPU với nice(1), và một số giới hạn tài nguyên với ulimit(1).

Đối với Linux, các nhóm kiểm soát (control group - cgroup) đã được phát triển và tích hợp trong Linux 2.6.24 (2008), và nhiều kiểm soát bổ sung đã được thêm kể từ đó. Chúng được tài liệu hóa trong mã nguồn nhân dưới Documentation/cgroups. Cũng có một lược đồ phân cấp thống nhất cải tiến gọi là cgroup v2, khả dụng trong Linux 4.5 (2016) và được tài liệu hóa trong Documentation/admin-guide/cgroup-v2.rst.

Các kiểm soát tài nguyên cụ thể được đề cập trong các chương sau khi thích hợp. Một trường hợp sử dụng mẫu được mô tả trong Chương 11, Điện toán đám mây, để quản lý hiệu năng của các người thuê ảo hóa ở cấp hệ điều hành.

### 3.2.17 Khả năng quan sát (Observability)

Hệ điều hành bao gồm nhân, thư viện, và chương trình. Các chương trình này bao gồm công cụ để quan sát hoạt động hệ thống và phân tích hiệu năng, thường được cài đặt trong /usr/bin và /usr/sbin. Các công cụ bên thứ ba cũng có thể được cài đặt trên hệ thống để cung cấp khả năng quan sát bổ sung.

Các công cụ quan sát, và các thành phần hệ điều hành mà chúng được xây dựng trên đó, được giới thiệu trong Chương 4.

## 3.3 Các nhân (Kernel)

Các phần tiếp theo thảo luận về các chi tiết triển khai nhân giống Unix với trọng tâm là hiệu năng. Như kiến thức nền, các tính năng hiệu năng của các nhân trước đó được thảo luận: Unix, BSD, và Solaris. Nhân Linux được thảo luận chi tiết hơn trong Mục 3.4, Linux.

Sự khác biệt giữa các nhân có thể bao gồm các hệ thống tệp chúng hỗ trợ (xem Chương 8, Hệ thống tệp), giao diện lời gọi hệ thống (syscall), kiến trúc ngăn xếp mạng, hỗ trợ thời gian thực, và thuật toán lập lịch cho CPU, I/O đĩa, và mạng.

Bảng 3.3 cho thấy Linux và các phiên bản nhân khác để so sánh, với số lượng syscall dựa trên số mục trong phần 2 của trang man hệ điều hành. Đây là so sánh thô, nhưng đủ để thấy một số khác biệt.

**Bảng 3.3: Các phiên bản nhân với số lượng syscall được tài liệu hóa**

| Phiên bản nhân | Syscall |
|---|---|
| UNIX Version 7 | 48 |
| SunOS (Solaris) 5.11 | 142 |
| FreeBSD 12.0 | 222 |
| Linux 2.6.32-21-server | 408 |
| Linux 2.6.32-220.el6.x86_64 | 427 |
| Linux 3.2.6-3.fc16.x86_64 | 431 |
| Linux 4.15.0-66-generic | 480 |
| Linux 5.3.0-1010-aws | 493 |

Đây chỉ là các syscall có tài liệu; thông thường nhân cung cấp nhiều hơn cho mục đích sử dụng riêng bởi phần mềm hệ điều hành.

> "UNIX had twenty system calls at the very first, and today Linux—which is a direct descendant—has over a thousand . . . I just worry about the complexity and the size of things that grow."
>
> — Ken Thompson, ACM Turing Centenary Celebration, 2012

Linux đang gia tăng về độ phức tạp và phơi bày sự phức tạp này cho user-land bằng cách thêm các lời gọi hệ thống mới hoặc thông qua các giao diện nhân khác. Độ phức tạp bổ sung làm cho việc học, lập trình, và gỡ lỗi tốn thời gian hơn.

### 3.3.1 Unix

Unix được phát triển bởi Ken Thompson, Dennis Ritchie, và những người khác tại AT&T Bell Labs trong năm 1969 và những năm tiếp theo. Nguồn gốc chính xác của nó được mô tả trong *The UNIX Time-Sharing System* [Ritchie 74]:

> "The first version was written when one of us (Thompson), dissatisfied with the available computer facilities, discovered a little-used PDP-7 and set out to create a more hospitable environment."

Các nhà phát triển của UNIX trước đó đã làm việc trên hệ điều hành Multiplexed Information and Computer Services (Multics). UNIX được phát triển như một hệ điều hành và nhân đa nhiệm nhẹ, ban đầu được đặt tên là UNiplexed Information and Computing Service (UNICS), như một cách chơi chữ với Multics. Từ *UNIX Implementation* [Thompson 78]:

> "The kernel is the only UNIX code that cannot be substituted by a user to his own liking. For this reason, the kernel should make as few real decisions as possible. This does not mean to allow the user a million options to do the same thing. Rather, it means to allow only one way to do one thing, but have that way be the least-common divisor of all the options that might have been provided."

Mặc dù nhân nhỏ, nó có cung cấp một số tính năng cho hiệu năng cao. Các tiến trình có mức ưu tiên bộ lập lịch, giảm độ trễ hàng đợi chạy cho công việc ưu tiên cao hơn. I/O đĩa được thực hiện theo các khối lớn (512 byte) để tăng hiệu quả và được đệm trong bộ nhớ đệm theo thiết bị (buffer cache) trong bộ nhớ. Các tiến trình nhàn rỗi có thể được hoán đổi ra bộ lưu trữ, cho phép các tiến trình bận hơn chạy trong bộ nhớ chính. Và hệ thống tất nhiên là đa nhiệm — cho phép nhiều tiến trình chạy đồng thời, cải thiện thông lượng công việc.

Để hỗ trợ mạng, nhiều hệ thống tệp, phân trang, và các tính năng khác mà chúng ta hiện coi là tiêu chuẩn, nhân đã phải phát triển. Và với nhiều phiên bản phái sinh, bao gồm BSD, SunOS (Solaris), và sau đó là Linux, hiệu năng nhân trở nên cạnh tranh, thúc đẩy việc bổ sung thêm tính năng và mã.

### 3.3.2 BSD

Berkeley Software Distribution (BSD) OS bắt đầu như các cải tiến cho Unix phiên bản 6 tại Đại học California, Berkeley, và được phát hành lần đầu vào năm 1978. Vì mã Unix ban đầu yêu cầu giấy phép phần mềm AT&T, đến đầu những năm 1990, mã Unix này đã được viết lại trong BSD theo giấy phép BSD mới, cho phép các bản phân phối tự do bao gồm FreeBSD.

Các phát triển nhân BSD chính, đặc biệt liên quan đến hiệu năng, bao gồm:

- **Bộ nhớ ảo phân trang (Paged virtual memory):** BSD mang bộ nhớ ảo phân trang đến Unix: thay vì hoán đổi toàn bộ tiến trình để giải phóng bộ nhớ chính, các phần bộ nhớ nhỏ hơn ít được sử dụng gần đây nhất có thể được di chuyển (phân trang). Xem Chương 7, Bộ nhớ, Mục 7.2.2, Phân trang.
- **Phân trang theo yêu cầu (Demand paging):** Hoãn việc ánh xạ bộ nhớ vật lý vào bộ nhớ ảo cho đến khi nó được ghi lần đầu, tránh chi phí hiệu năng và bộ nhớ sớm và đôi khi không cần thiết cho các trang có thể không bao giờ được sử dụng. Phân trang theo yêu cầu được BSD mang đến Unix. Xem Chương 7, Bộ nhớ, Mục 7.2.2, Phân trang.
- **FFS:** Berkeley Fast File System (FFS) nhóm cấp phát đĩa thành các nhóm cylinder, giảm đáng kể phân mảnh và cải thiện hiệu năng trên đĩa quay, cũng như hỗ trợ đĩa lớn hơn và các cải tiến khác. FFS trở thành nền tảng cho nhiều hệ thống tệp khác, bao gồm UFS. Xem Chương 8, Hệ thống tệp, Mục 8.4.5, Các loại hệ thống tệp.
- **Ngăn xếp mạng TCP/IP:** BSD phát triển ngăn xếp mạng TCP/IP hiệu năng cao đầu tiên cho Unix, được bao gồm trong 4.2BSD (1983). BSD vẫn nổi tiếng với ngăn xếp mạng hiệu năng của mình.
- **Socket:** Berkeley socket là API cho các điểm cuối kết nối. Được bao gồm trong 4.2BSD, chúng đã trở thành tiêu chuẩn cho mạng. Xem Chương 10, Mạng.
- **Jail:** Ảo hóa nhẹ cấp hệ điều hành, cho phép nhiều khách (guest) chia sẻ một nhân. Jail được phát hành lần đầu trong FreeBSD 4.0.
- **Kernel TLS:** Khi bảo mật lớp truyền tải (TLS - transport layer security) hiện được sử dụng phổ biến trên Internet, kernel TLS chuyển phần lớn xử lý TLS vào nhân, cải thiện hiệu năng<sup>14</sup> [Stewart 15].

Mặc dù không phổ biến bằng Linux, BSD được sử dụng cho một số môi trường quan trọng về hiệu năng, bao gồm cho mạng phân phối nội dung (CDN) của Netflix, cũng như máy chủ tệp từ NetApp, Isilon, và những hãng khác. Netflix tóm tắt hiệu năng FreeBSD trên CDN của mình vào năm 2019 như sau [Looney 19]:

> "Using FreeBSD and commodity parts, we achieve 90 Gb/s serving TLS-encrypted connections with ~55% CPU on a 16-core 2.6-GHz CPU."

Có một tài liệu tham khảo xuất sắc về nội bộ FreeBSD, từ cùng nhà xuất bản mang đến bạn cuốn sách này: *The Design and Implementation of the FreeBSD Operating System, 2nd Edition* [McKusick 15].

> <sup>14</sup> Được phát triển để cải thiện hiệu năng của các thiết bị Netflix FreeBSD open connect (OCA) là CDN của Netflix.

### 3.3.3 Solaris

Solaris là nhân và hệ điều hành có nguồn gốc từ Unix và BSD, được tạo bởi Sun Microsystems vào năm 1982. Ban đầu được đặt tên SunOS và tối ưu hóa cho các máy trạm Sun. Vào cuối những năm 1980, AT&T phát triển một chuẩn Unix mới, Unix System V Release 4 (SVR4) dựa trên công nghệ từ SVR3, SunOS, BSD, và Xenix. Sun tạo nhân mới dựa trên SVR4, và đổi tên hệ điều hành thành Solaris.

Các phát triển nhân Solaris chính, đặc biệt liên quan đến hiệu năng, bao gồm:

- **VFS:** Hệ thống tệp ảo (VFS) là trừu tượng hóa và giao diện cho phép nhiều hệ thống tệp dễ dàng cùng tồn tại. Sun ban đầu tạo nó để NFS và UFS có thể cùng tồn tại. VFS được đề cập trong Chương 8, Hệ thống tệp.
- **Nhân hoàn toàn có thể chiếm quyền (Fully preemptible kernel):** Cung cấp độ trễ thấp cho công việc ưu tiên cao, bao gồm công việc thời gian thực.
- **Hỗ trợ đa bộ xử lý:** Đầu những năm 1990, Sun đầu tư mạnh vào hỗ trợ hệ điều hành đa bộ xử lý, phát triển hỗ trợ nhân cho cả đa xử lý bất đối xứng và đối xứng (ASMP và SMP) [Mauro 01].
- **Bộ cấp phát slab (Slab allocator):** Thay thế bộ cấp phát buddy của SVR4, bộ cấp phát bộ nhớ nhân slab cung cấp hiệu năng tốt hơn thông qua các bộ nhớ đệm theo CPU chứa các bộ đệm được cấp phát trước có thể được tái sử dụng nhanh chóng. Loại bộ cấp phát này, và các phiên bản phái sinh của nó, đã trở thành tiêu chuẩn cho các nhân bao gồm Linux.
- **DTrace:** Khung truy vết tĩnh và động cùng công cụ cung cấp khả năng quan sát gần như không giới hạn của toàn bộ ngăn xếp phần mềm, trong thời gian thực và trong sản xuất. Linux có BPF và bpftrace cho loại khả năng quan sát này.
- **Zone:** Công nghệ ảo hóa dựa trên hệ điều hành để tạo các thể hiện hệ điều hành chia sẻ một nhân, tương tự công nghệ jail trước đó của FreeBSD. Ảo hóa hệ điều hành hiện được sử dụng rộng rãi dưới dạng container Linux. Xem Chương 11, Điện toán đám mây.
- **ZFS:** Hệ thống tệp với các tính năng và hiệu năng cấp doanh nghiệp. Nó hiện khả dụng cho các hệ điều hành khác, bao gồm Linux. Xem Chương 8, Hệ thống tệp.

Oracle mua Sun Microsystems vào năm 2010, và Solaris hiện được gọi là Oracle Solaris. Solaris được đề cập chi tiết hơn trong ấn bản đầu tiên của cuốn sách này.

### 3.2.4 Ngắt (Interrupt)

Ngắt là một tín hiệu đến bộ xử lý rằng một sự kiện nào đó đã xảy ra cần được xử lý, và làm gián đoạn việc thực thi hiện tại của bộ xử lý để xử lý nó. Nó thường làm cho bộ xử lý chuyển sang chế độ nhân nếu chưa ở đó, lưu trạng thái luồng hiện tại, và sau đó chạy một thủ tục phục vụ ngắt (interrupt service routine - ISR) để xử lý sự kiện.

Có các ngắt bất đồng bộ (asynchronous) được tạo bởi phần cứng bên ngoài và các ngắt đồng bộ (synchronous) được tạo bởi các lệnh phần mềm. Chúng được minh họa trong Hình 3.4.

*Hình 3.4: Các loại ngắt*

Để đơn giản, Hình 3.4 hiển thị tất cả các ngắt được gửi đến nhân để xử lý; thực tế chúng được gửi đến CPU trước, CPU chọn ISR trong nhân để chạy sự kiện.

**Ngắt bất đồng bộ**

Các thiết bị phần cứng có thể gửi các yêu cầu phục vụ ngắt (IRQ) đến bộ xử lý, đến một cách bất đồng bộ so với phần mềm đang chạy. Các ví dụ về ngắt phần cứng bao gồm:

- Thiết bị đĩa báo hiệu hoàn thành I/O đĩa
- Phần cứng chỉ báo một điều kiện lỗi
- Giao diện mạng báo hiệu sự đến của một gói tin
- Thiết bị đầu vào: đầu vào từ bàn phím và chuột

Để giải thích khái niệm ngắt bất đồng bộ, một kịch bản ví dụ được minh họa trong Hình 3.5 cho thấy sự trôi qua của thời gian khi cơ sở dữ liệu (MySQL) chạy trên CPU 0 đọc từ hệ thống tệp. Nội dung hệ thống tệp phải được lấy từ đĩa, vì vậy bộ lập lịch chuyển đổi ngữ cảnh sang luồng khác (ứng dụng Java) trong khi cơ sở dữ liệu đang chờ. Một lúc sau, I/O đĩa hoàn thành, nhưng tại thời điểm này cơ sở dữ liệu không còn chạy trên CPU 0. Ngắt hoàn thành đã xảy ra bất đồng bộ so với cơ sở dữ liệu, được thể hiện bằng đường nét đứt trong Hình 3.5.

*Hình 3.5: Ví dụ ngắt bất đồng bộ*

**Ngắt đồng bộ**

Ngắt đồng bộ được tạo bởi các lệnh phần mềm. Phần sau mô tả các loại ngắt phần mềm khác nhau sử dụng các thuật ngữ trap, ngoại lệ (exception), và lỗi trang (fault); tuy nhiên, các thuật ngữ này thường được sử dụng thay thế cho nhau.

- **Trap:** Một lời gọi có chủ đích vào nhân, chẳng hạn bởi lệnh int (interrupt). Một cách triển khai syscall liên quan đến việc gọi lệnh int với một vector cho trình xử lý syscall (ví dụ: int 0x80 trên Linux x86). int tạo ra một ngắt phần mềm.
- **Ngoại lệ (Exception):** Một điều kiện ngoại lệ, chẳng hạn bởi một lệnh thực hiện phép chia cho số không.
- **Lỗi trang (Fault):** Thuật ngữ thường được sử dụng cho các sự kiện bộ nhớ, chẳng hạn như lỗi trang được kích hoạt bởi việc truy cập một vị trí bộ nhớ mà không có ánh xạ MMU. Xem Chương 7, Bộ nhớ.

Đối với các ngắt này, phần mềm và lệnh chịu trách nhiệm vẫn đang ở trên CPU.

**Luồng ngắt (Interrupt Thread)**

Các thủ tục phục vụ ngắt (ISR) được thiết kế để hoạt động nhanh nhất có thể, nhằm giảm ảnh hưởng của việc gián đoạn các luồng đang hoạt động. Nếu một ngắt cần thực hiện nhiều hơn một ít công việc, đặc biệt nếu nó có thể bị chặn trên các khóa (lock), nó có thể được xử lý bởi một luồng ngắt có thể được lập lịch bởi nhân. Điều này được minh họa trong Hình 3.6.

*Hình 3.6: Xử lý ngắt*

Cách triển khai điều này phụ thuộc vào phiên bản nhân. Trên Linux, trình điều khiển thiết bị có thể được mô hình hóa thành hai nửa, với nửa trên (top half) xử lý ngắt nhanh chóng, và lập lịch công việc cho nửa dưới (bottom half) để xử lý sau [Corbet 05]. Xử lý ngắt nhanh chóng là quan trọng vì nửa trên chạy trong chế độ vô hiệu hóa ngắt để hoãn việc gửi các ngắt mới, điều này có thể gây ra vấn đề độ trễ cho các luồng khác nếu nó chạy quá lâu. Nửa dưới có thể là tasklet hoặc hàng đợi công việc (work queue); hàng đợi công việc là các luồng có thể được lập lịch bởi nhân và có thể ngủ khi cần thiết.

Ví dụ, trình điều khiển mạng Linux có nửa trên để xử lý IRQ cho các gói tin đến, gọi nửa dưới để đẩy gói tin lên ngăn xếp mạng. Nửa dưới được triển khai dưới dạng softirq (ngắt phần mềm).

Thời gian từ khi ngắt đến cho đến khi nó được phục vụ là độ trễ ngắt (interrupt latency), phụ thuộc vào phần cứng và cách triển khai. Đây là chủ đề nghiên cứu cho các hệ thống thời gian thực hoặc độ trễ thấp.

**Che ngắt (Interrupt Masking)**

Một số đường dẫn mã trong nhân không thể bị gián đoạn một cách an toàn. Một ví dụ là mã nhân giành một spin lock trong một lời gọi hệ thống, cho spin lock cũng có thể cần bởi một ngắt. Nhận một ngắt khi đang giữ khóa như vậy có thể gây ra deadlock. Để ngăn tình huống như vậy, nhân có thể tạm thời che (mask) ngắt bằng cách thiết lập thanh ghi mặt nạ ngắt của CPU. Thời gian vô hiệu hóa ngắt nên càng ngắn càng tốt, vì nó có thể xáo trộn việc thực thi kịp thời của các ứng dụng được đánh thức bởi các ngắt khác. Đây là một yếu tố quan trọng cho các hệ thống thời gian thực — những hệ thống có yêu cầu nghiêm ngặt về thời gian phản hồi. Thời gian vô hiệu hóa ngắt cũng là mục tiêu của phân tích hiệu năng (phân tích như vậy được hỗ trợ trực tiếp bởi bộ truy vết irqsoff của Ftrace, được đề cập trong Chương 14, Ftrace).

Một số sự kiện ưu tiên cao không nên bị bỏ qua, và do đó được triển khai dưới dạng ngắt không thể che (non-maskable interrupt - NMI). Ví dụ, Linux có thể sử dụng bộ hẹn giờ watchdog IPMI để kiểm tra xem nhân có bị khóa cứng hay không dựa trên sự thiếu ngắt trong một khoảng thời gian. Nếu vậy, watchdog có thể phát hành ngắt NMI để khởi động lại hệ thống.<sup>5</sup>

> <sup>5</sup> Linux cũng có watchdog NMI phần mềm để phát hiện tình trạng khóa cứng [Linux 20d].

### 3.2.5 Đồng hồ và trạng thái rỗi (Clock and Idle)

Một thành phần cốt lõi của nhân Unix ban đầu là thủ tục clock(), được thực thi từ ngắt hẹn giờ. Nó trong lịch sử được thực thi 60, 100, hoặc 1.000 lần mỗi giây (thường được biểu thị bằng Hertz), và mỗi lần thực thi được gọi là một tick. Các chức năng của nó bao gồm cập nhật thời gian hệ thống, hết hạn timer và lát thời gian cho lập lịch luồng, duy trì thống kê CPU, và thực thi các thủ tục nhân đã lên lịch.

Đã có các vấn đề hiệu năng với đồng hồ, được cải thiện trong các nhân sau này, bao gồm:

- **Độ trễ tick:** Đối với đồng hồ 100 Hertz, có thể gặp thêm đến 10 ms độ trễ cho một timer khi nó chờ được xử lý trong tick tiếp theo. Điều này đã được khắc phục bằng cách sử dụng ngắt thời gian thực độ phân giải cao.
- **Chi phí tick:** Tick tiêu tốn chu kỳ CPU và gây nhiễu nhẹ cho các ứng dụng, và là một nguyên nhân của jitter hệ điều hành. Các bộ xử lý hiện đại cũng có tính năng quản lý năng lượng động, có thể tắt nguồn các phần trong thời gian rỗi. Thủ tục đồng hồ làm gián đoạn thời gian rỗi này, có thể tiêu tốn năng lượng không cần thiết.

Các nhân hiện đại đã chuyển nhiều chức năng ra khỏi thủ tục đồng hồ sang ngắt theo yêu cầu, trong nỗ lực tạo ra nhân không tick (tickless kernel). Điều này giảm chi phí và cải thiện hiệu quả năng lượng bằng cách cho phép bộ xử lý duy trì trạng thái ngủ lâu hơn.

Thủ tục đồng hồ Linux là scheduler_tick(), và Linux có các cách để bỏ qua việc gọi đồng hồ khi không có tải CPU. Bản thân đồng hồ thường chạy ở 250 Hertz (được cấu hình bởi CONFIG_HZ), và các lần gọi được giảm bởi chức năng NO_HZ (CONFIG_NO_HZ), hiện thường được kích hoạt [Linux 20a].

**Luồng rỗi (Idle Thread)**

Khi không có công việc cho CPU thực hiện, nhân lập lịch một luồng giữ chỗ chờ công việc, gọi là luồng rỗi. Một triển khai đơn giản sẽ kiểm tra tính khả dụng của công việc mới trong một vòng lặp. Trong Linux hiện đại, tác vụ rỗi có thể gọi lệnh hlt (halt) để tắt nguồn CPU cho đến khi ngắt tiếp theo được nhận, tiết kiệm năng lượng.


### 3.2.4 Ngắt (Interrupt)

Ngắt là một tín hiệu đến bộ xử lý rằng một sự kiện nào đó đã xảy ra cần được xử lý, và làm gián đoạn việc thực thi hiện tại của bộ xử lý để xử lý nó. Nó thường làm cho bộ xử lý chuyển sang chế độ nhân nếu chưa ở đó, lưu trạng thái luồng hiện tại, và sau đó chạy một thủ tục phục vụ ngắt (interrupt service routine - ISR) để xử lý sự kiện.

Có các ngắt bất đồng bộ (asynchronous) được tạo bởi phần cứng bên ngoài và các ngắt đồng bộ (synchronous) được tạo bởi các lệnh phần mềm. Chúng được minh họa trong Hình 3.4.

*Hình 3.4: Các loại ngắt*

Để đơn giản, Hình 3.4 hiển thị tất cả các ngắt được gửi đến nhân để xử lý; thực tế chúng được gửi đến CPU trước, CPU chọn ISR trong nhân để chạy sự kiện.

**Ngắt bất đồng bộ**

Các thiết bị phần cứng có thể gửi các yêu cầu phục vụ ngắt (IRQ) đến bộ xử lý, đến một cách bất đồng bộ so với phần mềm đang chạy. Các ví dụ về ngắt phần cứng bao gồm:

- Thiết bị đĩa báo hiệu hoàn thành I/O đĩa
- Phần cứng chỉ báo một điều kiện lỗi
- Giao diện mạng báo hiệu sự đến của một gói tin
- Thiết bị đầu vào: đầu vào từ bàn phím và chuột

Để giải thích khái niệm ngắt bất đồng bộ, một kịch bản ví dụ được minh họa trong Hình 3.5 cho thấy sự trôi qua của thời gian khi cơ sở dữ liệu (MySQL) chạy trên CPU 0 đọc từ hệ thống tệp. Nội dung hệ thống tệp phải được lấy từ đĩa, vì vậy bộ lập lịch chuyển đổi ngữ cảnh sang luồng khác (ứng dụng Java) trong khi cơ sở dữ liệu đang chờ. Một lúc sau, I/O đĩa hoàn thành, nhưng tại thời điểm này cơ sở dữ liệu không còn chạy trên CPU 0. Ngắt hoàn thành đã xảy ra bất đồng bộ so với cơ sở dữ liệu, được thể hiện bằng đường nét đứt trong Hình 3.5.

*Hình 3.5: Ví dụ ngắt bất đồng bộ*

**Ngắt đồng bộ**

Ngắt đồng bộ được tạo bởi các lệnh phần mềm. Phần sau mô tả các loại ngắt phần mềm khác nhau sử dụng các thuật ngữ trap, ngoại lệ (exception), và lỗi trang (fault); tuy nhiên, các thuật ngữ này thường được sử dụng thay thế cho nhau.

- **Trap:** Một lời gọi có chủ đích vào nhân, chẳng hạn bởi lệnh int (interrupt). Một cách triển khai syscall liên quan đến việc gọi lệnh int với một vector cho trình xử lý syscall (ví dụ: int 0x80 trên Linux x86). int tạo ra một ngắt phần mềm.
- **Ngoại lệ (Exception):** Một điều kiện ngoại lệ, chẳng hạn bởi một lệnh thực hiện phép chia cho số không.
- **Lỗi trang (Fault):** Thuật ngữ thường được sử dụng cho các sự kiện bộ nhớ, chẳng hạn như lỗi trang được kích hoạt bởi việc truy cập một vị trí bộ nhớ mà không có ánh xạ MMU. Xem Chương 7, Bộ nhớ.

Đối với các ngắt này, phần mềm và lệnh chịu trách nhiệm vẫn đang ở trên CPU.

**Luồng ngắt (Interrupt Thread)**

Các thủ tục phục vụ ngắt (ISR) được thiết kế để hoạt động nhanh nhất có thể, nhằm giảm ảnh hưởng của việc gián đoạn các luồng đang hoạt động. Nếu một ngắt cần thực hiện nhiều hơn một ít công việc, đặc biệt nếu nó có thể bị chặn trên các khóa (lock), nó có thể được xử lý bởi một luồng ngắt có thể được lập lịch bởi nhân. Điều này được minh họa trong Hình 3.6.

*Hình 3.6: Xử lý ngắt*

Cách triển khai điều này phụ thuộc vào phiên bản nhân. Trên Linux, trình điều khiển thiết bị có thể được mô hình hóa thành hai nửa, với nửa trên (top half) xử lý ngắt nhanh chóng, và lập lịch công việc cho nửa dưới (bottom half) để xử lý sau [Corbet 05]. Xử lý ngắt nhanh chóng là quan trọng vì nửa trên chạy trong chế độ vô hiệu hóa ngắt để hoãn việc gửi các ngắt mới, điều này có thể gây ra vấn đề độ trễ cho các luồng khác nếu nó chạy quá lâu. Nửa dưới có thể là tasklet hoặc hàng đợi công việc (work queue); hàng đợi công việc là các luồng có thể được lập lịch bởi nhân và có thể ngủ khi cần thiết.

Ví dụ, trình điều khiển mạng Linux có nửa trên để xử lý IRQ cho các gói tin đến, gọi nửa dưới để đẩy gói tin lên ngăn xếp mạng. Nửa dưới được triển khai dưới dạng softirq (ngắt phần mềm).

Thời gian từ khi ngắt đến cho đến khi nó được phục vụ là độ trễ ngắt (interrupt latency), phụ thuộc vào phần cứng và cách triển khai. Đây là chủ đề nghiên cứu cho các hệ thống thời gian thực hoặc độ trễ thấp.

**Che ngắt (Interrupt Masking)**

Một số đường dẫn mã trong nhân không thể bị gián đoạn một cách an toàn. Một ví dụ là mã nhân giành một spin lock trong một lời gọi hệ thống, cho spin lock cũng có thể cần bởi một ngắt. Nhận một ngắt khi đang giữ khóa như vậy có thể gây ra deadlock. Để ngăn tình huống như vậy, nhân có thể tạm thời che (mask) ngắt bằng cách thiết lập thanh ghi mặt nạ ngắt của CPU. Thời gian vô hiệu hóa ngắt nên càng ngắn càng tốt, vì nó có thể xáo trộn việc thực thi kịp thời của các ứng dụng được đánh thức bởi các ngắt khác. Đây là một yếu tố quan trọng cho các hệ thống thời gian thực — những hệ thống có yêu cầu nghiêm ngặt về thời gian phản hồi. Thời gian vô hiệu hóa ngắt cũng là mục tiêu của phân tích hiệu năng (phân tích như vậy được hỗ trợ trực tiếp bởi bộ truy vết irqsoff của Ftrace, được đề cập trong Chương 14, Ftrace).

Một số sự kiện ưu tiên cao không nên bị bỏ qua, và do đó được triển khai dưới dạng ngắt không thể che (non-maskable interrupt - NMI). Ví dụ, Linux có thể sử dụng bộ hẹn giờ watchdog IPMI để kiểm tra xem nhân có bị khóa cứng hay không dựa trên sự thiếu ngắt trong một khoảng thời gian. Nếu vậy, watchdog có thể phát hành ngắt NMI để khởi động lại hệ thống.<sup>5</sup>

> <sup>5</sup> Linux cũng có watchdog NMI phần mềm để phát hiện tình trạng khóa cứng [Linux 20d].

### 3.2.5 Đồng hồ và trạng thái rỗi (Clock and Idle)

Một thành phần cốt lõi của nhân Unix ban đầu là thủ tục clock(), được thực thi từ ngắt hẹn giờ. Nó trong lịch sử được thực thi 60, 100, hoặc 1.000 lần mỗi giây (thường được biểu thị bằng Hertz), và mỗi lần thực thi được gọi là một tick. Các chức năng của nó bao gồm cập nhật thời gian hệ thống, hết hạn timer và lát thời gian cho lập lịch luồng, duy trì thống kê CPU, và thực thi các thủ tục nhân đã lên lịch.

Đã có các vấn đề hiệu năng với đồng hồ, được cải thiện trong các nhân sau này, bao gồm:

- **Độ trễ tick:** Đối với đồng hồ 100 Hertz, có thể gặp thêm đến 10 ms độ trễ cho một timer khi nó chờ được xử lý trong tick tiếp theo. Điều này đã được khắc phục bằng cách sử dụng ngắt thời gian thực độ phân giải cao.
- **Chi phí tick:** Tick tiêu tốn chu kỳ CPU và gây nhiễu nhẹ cho các ứng dụng, và là một nguyên nhân của jitter hệ điều hành. Các bộ xử lý hiện đại cũng có tính năng quản lý năng lượng động, có thể tắt nguồn các phần trong thời gian rỗi. Thủ tục đồng hồ làm gián đoạn thời gian rỗi này, có thể tiêu tốn năng lượng không cần thiết.

Các nhân hiện đại đã chuyển nhiều chức năng ra khỏi thủ tục đồng hồ sang ngắt theo yêu cầu, trong nỗ lực tạo ra nhân không tick (tickless kernel). Điều này giảm chi phí và cải thiện hiệu quả năng lượng bằng cách cho phép bộ xử lý duy trì trạng thái ngủ lâu hơn.

Thủ tục đồng hồ Linux là scheduler_tick(), và Linux có các cách để bỏ qua việc gọi đồng hồ khi không có tải CPU. Bản thân đồng hồ thường chạy ở 250 Hertz (được cấu hình bởi CONFIG_HZ), và các lần gọi được giảm bởi chức năng NO_HZ (CONFIG_NO_HZ), hiện thường được kích hoạt [Linux 20a].

**Luồng rỗi (Idle Thread)**

Khi không có công việc cho CPU thực hiện, nhân lập lịch một luồng giữ chỗ chờ công việc, gọi là luồng rỗi. Một triển khai đơn giản sẽ kiểm tra tính khả dụng của công việc mới trong một vòng lặp. Trong Linux hiện đại, tác vụ rỗi có thể gọi lệnh hlt (halt) để tắt nguồn CPU cho đến khi ngắt tiếp theo được nhận, tiết kiệm năng lượng.


### 3.2.6 Tiến trình (Process)

Một tiến trình là một môi trường để thực thi chương trình cấp người dùng. Nó bao gồm một không gian địa chỉ bộ nhớ, các bộ mô tả tệp, ngăn xếp luồng, và thanh ghi. Ở một số khía cạnh, một tiến trình giống như một máy tính thời kỳ đầu ảo, nơi mà chỉ có một chương trình đang thực thi với các thanh ghi và ngăn xếp riêng.

Các tiến trình được đa nhiệm bởi nhân, thường hỗ trợ thực thi hàng nghìn tiến trình trên một hệ thống đơn. Chúng được xác định riêng lẻ bởi ID tiến trình (PID), là một định danh số duy nhất.

Một tiến trình chứa một hoặc nhiều luồng, hoạt động trong không gian địa chỉ của tiến trình và chia sẻ cùng các bộ mô tả tệp. Một luồng là một ngữ cảnh thực thi bao gồm ngăn xếp, thanh ghi, và con trỏ lệnh (còn gọi là bộ đếm chương trình). Nhiều luồng cho phép một tiến trình đơn thực thi song song trên nhiều CPU. Trên Linux, luồng và tiến trình đều là tác vụ (task).

Tiến trình đầu tiên được khởi chạy bởi nhân được gọi là "init," từ /sbin/init (mặc định), với PID 1, khởi chạy các dịch vụ không gian người dùng. Trong Unix, điều này liên quan đến việc chạy các script khởi động từ /etc, một phương pháp nay được gọi là SysV (theo Unix System V). Các bản phân phối Linux ngày nay thường sử dụng phần mềm systemd để khởi động dịch vụ và theo dõi các phụ thuộc của chúng.

**Tạo tiến trình**

Các tiến trình thường được tạo bằng lời gọi hệ thống fork(2) trên các hệ thống Unix. Trên Linux, các thư viện C thường triển khai hàm fork bằng cách bọc quanh syscall đa năng clone(2). Các syscall này tạo bản sao của tiến trình, với ID tiến trình riêng. Lời gọi hệ thống exec(2) (hoặc biến thể, như execve(2)) sau đó có thể được gọi để bắt đầu thực thi một chương trình khác.

*Hình 3.7: Tạo tiến trình*

Syscall fork(2) hoặc clone(2) có thể sử dụng chiến lược sao chép khi ghi (copy-on-write - COW) để cải thiện hiệu năng. Điều này thêm các tham chiếu đến không gian địa chỉ trước đó thay vì sao chép tất cả nội dung. Khi một trong hai tiến trình sửa đổi bộ nhớ được tham chiếu nhiều lần, một bản sao riêng biệt sau đó được tạo cho các sửa đổi. Chiến lược này hoãn lại hoặc loại bỏ nhu cầu sao chép bộ nhớ, giảm sử dụng bộ nhớ và CPU.

**Vòng đời tiến trình**

*Hình 3.8: Vòng đời tiến trình*

Trạng thái on-proc là khi đang chạy trên bộ xử lý (CPU). Trạng thái ready-to-run là khi tiến trình có thể chạy nhưng đang chờ trên hàng đợi chạy của CPU để đến lượt. Hầu hết I/O sẽ chặn, đưa tiến trình vào trạng thái ngủ cho đến khi I/O hoàn thành và tiến trình được đánh thức. Trạng thái zombie xảy ra trong quá trình kết thúc tiến trình, khi tiến trình chờ cho đến khi trạng thái của nó được thu hồi bởi tiến trình cha hoặc bị loại bỏ bởi nhân.

**Môi trường tiến trình**

*Hình 3.9: Môi trường tiến trình*

Ngữ cảnh nhân bao gồm các thuộc tính và thống kê tiến trình: ID tiến trình (PID), ID người dùng chủ sở hữu (UID), và các thời gian khác nhau, thường được kiểm tra qua ps(1) và top(1). Nó cũng có tập bộ mô tả tệp, tham chiếu tệp đang mở và (thường) được chia sẻ giữa các luồng.

Trên Linux, mỗi luồng có ngăn xếp người dùng riêng và ngăn xếp ngoại lệ nhân riêng [Owens 20].

### 3.2.7 Ngăn xếp (Stack)

Ngăn xếp là vùng lưu trữ bộ nhớ cho dữ liệu tạm thời, được tổ chức dưới dạng danh sách vào sau ra trước (LIFO). Nó được sử dụng để lưu trữ dữ liệu ít quan trọng hơn so với dữ liệu vừa trong tập thanh ghi CPU. Khi một hàm được gọi, địa chỉ trả về được lưu vào ngăn xếp. Khi hàm được gọi hoàn thành, nó khôi phục thanh ghi cần thiết và chuyển thực thi đến hàm gọi. Tập dữ liệu trên ngăn xếp liên quan đến thực thi của một hàm được gọi là khung ngăn xếp (stack frame).

Đường dẫn gọi đến hàm đang thực thi hiện tại có thể được xem bằng cách kiểm tra các địa chỉ trả về đã lưu qua tất cả các khung ngăn xếp (duyệt ngăn xếp - stack walking). Đường dẫn gọi này được gọi là stack back trace hoặc stack trace, và là công cụ vô giá cho gỡ lỗi và phân tích hiệu năng.

**Cách đọc một Stack**

```
tcp_sendmsg+1
sock_sendmsg+62
SYSC_sendto+319
sys_sendto+14
do_syscall_64+115
entry_SYSCALL_64_after_hwframe+61
```

Ngăn xếp thường được in theo thứ tự từ lá đến gốc. Bằng cách đọc từ dưới lên, bạn có thể theo dõi đường dẫn thực thi đến hàm hiện tại.

**Ngăn xếp người dùng và nhân**

Trong khi thực thi một lời gọi hệ thống, một luồng tiến trình có hai ngăn xếp: ngăn xếp cấp người dùng và ngăn xếp cấp nhân.

*Hình 3.10: Ngăn xếp người dùng và nhân*

Ngăn xếp cấp người dùng của luồng bị chặn không thay đổi trong suốt thời gian lời gọi hệ thống, vì luồng đang sử dụng ngăn xếp cấp nhân riêng biệt trong ngữ cảnh nhân.

### 3.2.8 Bộ nhớ ảo (Virtual Memory)

Bộ nhớ ảo là trừu tượng hóa của bộ nhớ chính, cung cấp cho tiến trình và nhân cái nhìn riêng tư, gần như vô hạn, về bộ nhớ chính. Nó hỗ trợ đa nhiệm và đăng ký vượt mức (oversubscription) bộ nhớ chính.

*Hình 3.11: Không gian địa chỉ bộ nhớ ảo*

**Quản lý bộ nhớ**

Có hai cơ chế nhân:

- **Hoán đổi tiến trình (Process swapping):** di chuyển toàn bộ tiến trình giữa bộ nhớ chính và bộ lưu trữ thứ cấp.
- **Phân trang (Paging):** di chuyển các đơn vị bộ nhớ nhỏ gọi là trang (ví dụ: 4 Kbyte).

Trong Linux, thuật ngữ swapping được sử dụng để chỉ phân trang. Nhân Linux không hỗ trợ kiểu hoán đổi tiến trình Unix cũ.

### 3.2.9 Bộ lập lịch (Scheduler)

Unix và các hệ thống phái sinh là các hệ thống chia sẻ thời gian. Bộ lập lịch ánh xạ luồng (tác vụ) vào CPU, chia thời gian CPU giữa chúng và duy trì khái niệm về mức ưu tiên.

*Hình 3.12: Bộ lập lịch nhân*

Các khối lượng công việc được phân loại thành:

- **CPU-bound:** Ứng dụng tính toán nặng, bị giới hạn bởi tài nguyên CPU.
- **I/O-bound:** Ứng dụng thực hiện I/O, bị giới hạn bởi I/O đến tài nguyên lưu trữ hoặc mạng.

Các nhân hiện đại hỗ trợ nhiều lớp lập lịch hoặc chính sách lập lịch (scheduling policy) áp dụng các thuật toán khác nhau, bao gồm lập lịch thời gian thực.

### 3.2.10 Hệ thống tệp (File System)

Hệ thống tệp là tổ chức dữ liệu dưới dạng tệp và thư mục, thường dựa trên chuẩn POSIX. Hệ điều hành cung cấp không gian tên tệp toàn cục, tổ chức dưới dạng cây bắt đầu từ gốc ("/").

*Hình 3.13: Phân cấp tệp hệ điều hành*

**VFS**

Hệ thống tệp ảo (VFS) là giao diện nhân để trừu tượng hóa các loại hệ thống tệp, ban đầu được phát triển bởi Sun Microsystems.

*Hình 3.14: Hệ thống tệp ảo*

**Ngăn xếp I/O**

*Hình 3.15: Ngăn xếp I/O chung*

### 3.2.11 Bộ nhớ đệm (Caching)

**Bảng 3.2: Các lớp bộ nhớ đệm ví dụ cho I/O đĩa**

| # | Bộ nhớ đệm | Ví dụ |
|---|---|---|
| 1 | Client cache | Bộ nhớ đệm trình duyệt web |
| 2 | Application cache | — |
| 3 | Web server cache | Apache cache |
| 4 | Caching server | memcached |
| 5 | Database cache | MySQL buffer cache |
| 6 | Directory cache | dcache |
| 7 | File metadata cache | inode cache |
| 8 | OS buffer cache | Buffer cache |
| 9 | FS primary cache | Page cache, ZFS ARC |
| 10 | FS secondary cache | ZFS L2ARC |
| 11 | Device cache | ZFS vdev |
| 12 | Block cache | Buffer cache |
| 13 | Disk controller cache | RAID card cache |
| 14 | Storage array cache | — |
| 15 | On-disk cache | — |

### 3.2.12 Mạng (Networking)

Các nhân hiện đại cung cấp ngăn xếp giao thức mạng tích hợp (ngăn xếp TCP/IP). Ứng dụng truy cập mạng qua socket.

### 3.2.13 Trình điều khiển thiết bị (Device Driver)

Trình điều khiển thiết bị là phần mềm nhân cho quản lý và I/O thiết bị. Chúng cung cấp giao diện ký tự (character) và/hoặc khối (block) cho thiết bị. Trong Linux, buffer cache hiện là một phần của page cache.

### 3.2.14 Đa bộ xử lý (Multiprocessor)

Hỗ trợ đa bộ xử lý thường được triển khai dưới dạng đa xử lý đối xứng (SMP). Trên hệ thống đa bộ xử lý cũng có thể có kiến trúc NUMA.

**IPI:** Ngắt liên xử lý (inter-processor interrupt) để phối hợp giữa các CPU.

### 3.2.15 Chiếm quyền ưu tiên (Preemption)

Hỗ trợ chiếm quyền ưu tiên nhân cho phép các luồng ưu tiên cao gián đoạn nhân. Linux hỗ trợ CONFIG_PREEMPT_VOLUNTARY (tự nguyện), CONFIG_PREEMPT (đầy đủ), và CONFIG_PREEMPT_NONE.

### 3.2.16 Quản lý tài nguyên (Resource Management)

Bao gồm kiểm soát tài nguyên (resource control) cho CPU, bộ nhớ, đĩa, mạng. Linux sử dụng cgroup (2.6.24) và cgroup v2 (4.5).

### 3.2.17 Khả năng quan sát (Observability)

Các công cụ quan sát được giới thiệu trong Chương 4.

## 3.3 Các nhân (Kernel)

**Bảng 3.3: Các phiên bản nhân với số lượng syscall**

| Phiên bản nhân | Syscall |
|---|---|
| UNIX Version 7 | 48 |
| SunOS (Solaris) 5.11 | 142 |
| FreeBSD 12.0 | 222 |
| Linux 5.3.0-1010-aws | 493 |

### 3.3.1 Unix

Unix được phát triển bởi Ken Thompson, Dennis Ritchie, và những người khác tại AT&T Bell Labs từ năm 1969.

### 3.3.2 BSD

BSD bắt đầu như các cải tiến cho Unix phiên bản 6 tại UC Berkeley (1978). Các phát triển chính: bộ nhớ ảo phân trang, phân trang theo yêu cầu, FFS, ngăn xếp TCP/IP, socket, jail, kernel TLS.

### 3.3.3 Solaris

Solaris được tạo bởi Sun Microsystems (1982). Các phát triển chính: VFS, nhân hoàn toàn có thể chiếm quyền, hỗ trợ đa bộ xử lý, slab allocator, DTrace, zone, ZFS.


## 3.4 Linux

Linux được tạo vào năm 1991 bởi Linus Torvalds như một hệ điều hành miễn phí cho máy tính cá nhân Intel. Nhân Linux được phát triển dựa trên ý tưởng chung từ nhiều tổ tiên, bao gồm: Unix (và Multics), BSD, Solaris, Plan 9.

### 3.4.1 Các phát triển nhân Linux

Các phát triển nhân Linux liên quan đến hiệu năng bao gồm (nhiều mô tả bao gồm phiên bản nhân Linux nơi chúng được giới thiệu lần đầu):

- **Lớp lập lịch CPU:** Nhiều thuật toán lập lịch CPU tiên tiến, bao gồm scheduling domain (2.6.7) cho quyết định tốt hơn về NUMA.
- **Lớp lập lịch I/O:** Các thuật toán lập lịch I/O khối khác nhau: deadline (2.5.39), anticipatory (2.5.75), CFQ (2.6.6).
- **Thuật toán tắc nghẽn TCP:** Linux cho phép cấu hình các thuật toán kiểm soát tắc nghẽn TCP khác nhau: Reno, Cubic, v.v.
- **Overcommit:** Cùng với OOM killer, đây là chiến lược để làm nhiều hơn với ít bộ nhớ chính hơn.
- **Futex (2.5.7):** Mutex nhanh trong không gian người dùng.
- **Huge pages (2.5.36):** Hỗ trợ trang bộ nhớ lớn được cấp phát trước.
- **OProfile (2.5.43):** Bộ profiler hệ thống cho CPU.
- **RCU (2.5.43):** Cơ chế đồng bộ hóa read-copy update.
- **epoll (2.5.46):** Lời gọi hệ thống cho chờ I/O hiệu quả trên nhiều bộ mô tả tệp.
- **Lập lịch I/O module (2.6.10):** Thuật toán lập lịch có thể cắm cho I/O thiết bị khối.
- **DebugFS (2.6.11):** Giao diện đơn giản cho nhân phơi bày dữ liệu cho cấp người dùng.
- **Cpusets (2.6.12):** Nhóm CPU độc quyền cho tiến trình.
- **Chiếm quyền ưu tiên nhân tự nguyện (2.6.13):** Lập lịch độ trễ thấp không cần phức tạp của chiếm quyền đầy đủ.
- **inotify (2.6.13):** Khung giám sát sự kiện hệ thống tệp.
- **blktrace (2.6.17):** Khung và công cụ truy vết sự kiện I/O khối.
- **splice (2.6.17):** Syscall di chuyển dữ liệu nhanh giữa bộ mô tả tệp và pipe.
- **Delay accounting (2.6.18):** Theo dõi trạng thái trễ theo tác vụ.
- **IO accounting (2.6.20):** Đo lường thống kê I/O lưu trữ theo tiến trình.
- **DynTicks (2.6.21):** Tick động cho phép ngắt hẹn giờ nhân không kích hoạt khi rỗi.
- **SLUB (2.6.22):** Phiên bản mới đơn giản hóa của bộ cấp phát bộ nhớ slab.
- **CFS (2.6.23):** Completely fair scheduler.
- **cgroups (2.6.24):** Nhóm kiểm soát cho đo lường và giới hạn sử dụng tài nguyên.
- **TCP LRO (2.6.24):** TCP Large Receive Offload.
- **latencytop (2.6.25):** Công cụ quan sát nguồn gốc độ trễ.
- **Tracepoints (2.6.28):** Điểm truy vết tĩnh nhân.
- **perf (2.6.31):** Linux Performance Events.
- **No BKL (2.6.37):** Loại bỏ cuối cùng big kernel lock.
- **Transparent huge pages (2.6.38):** Khung cho sử dụng dễ dàng trang bộ nhớ lớn.
- **KVM:** Kernel-based Virtual Machine.
- **BPF JIT (3.0):** Trình biên dịch Just-In-Time cho BPF.
- **CFS bandwidth control (3.2):** Hạn ngạch và điều tiết CPU.
- **TCP anti-bufferbloat (3.3+):** Các cải tiến chống bufferbloat.
- **uprobes (3.5):** Cơ sở hạ tầng truy vết động cấp người dùng.
- **TFO (3.6, 3.7, 3.13):** TCP Fast Open.
- **NUMA balancing (3.8+):** Cân bằng tự động vị trí bộ nhớ trên hệ thống đa NUMA.
- **SO_REUSEPORT (3.9):** Tùy chọn socket cho nhiều listener trên cùng cổng.
- **bcache (3.10):** Công nghệ đệm SSD cho giao diện khối.
- **TCP TLP (3.10):** TCP Tail Loss Probe.
- **NO_HZ_FULL (3.10, 3.12):** Nhân tickless.
- **Multiqueue block I/O (3.13):** Hàng đợi gửi I/O theo CPU.
- **SCHED_DEADLINE (3.14):** Lập lịch earliest deadline first (EDF).
- **TCP autocorking (3.14):** Nhân gộp các lần ghi nhỏ.
- **MCS locks và qspinlocks (3.15):** Khóa nhân hiệu quả.
- **Extended BPF (3.18+):** Môi trường thực thi trong nhân cho các chương trình chế độ nhân an toàn.
- **Overlayfs (3.18):** Hệ thống tệp union mount, thường dùng cho container.
- **DCTCP (3.18):** Thuật toán tắc nghẽn Data Center TCP.
- **DAX (4.0):** Direct Access cho bộ nhớ liên tục (persistent memory).
- **Queued spinlocks (4.2):** Hiệu năng tốt hơn dưới tranh chấp.
- **TCP lockless listener (4.4):** Đường dẫn nhanh TCP listener không khóa.
- **cgroup v2 (4.5, 4.15):** Phân cấp thống nhất cho cgroup.
- **epoll scalability (4.5):** Cải thiện khả năng mở rộng đa luồng cho epoll.
- **TCP NV (4.8):** New Vegas cho mạng băng thông cao.
- **XDP (4.8, 4.18):** eXpress Data Path cho mạng hiệu năng cao.
- **TCP BBR (4.9):** Thuật toán tắc nghẽn Bottleneck Bandwidth and RTT.
- **Hardware latency tracer (4.9):** Bộ truy vết Ftrace phát hiện độ trễ phần cứng.
- **perf c2c (4.10):** Xác định vấn đề hiệu năng bộ nhớ đệm CPU.
- **Intel CAT (4.10):** Cache Allocation Technology.
- **BFQ, Kyber (4.12):** Bộ lập lịch I/O đa hàng đợi.
- **Kernel TLS (4.13, 4.17):** Phiên bản Linux của kernel TLS.
- **MSG_ZEROCOPY (4.14):** Cờ send(2) tránh sao chép thêm byte gói tin.
- **PCID (4.14):** Hỗ trợ process-context ID, giảm chi phí TLB flush.
- **PSI (4.20, 5.2):** Pressure stall information.
- **TCP EDT (4.20):** Early Departure Time cho gửi gói tin.
- **Multi-queue I/O (5.0):** Mặc định từ 5.0.
- **UDP GRO (5.0):** UDP Generic Receive Offload.
- **io_uring (5.1):** Giao diện bất đồng bộ chung cho giao tiếp nhanh ứng dụng-nhân.
- **MADV_COLD, MADV_PAGEOUT (5.4):** Gợi ý madvise(2) cho quản lý bộ nhớ.
- **MultiPath TCP (5.6):** Nhiều liên kết mạng cho một kết nối TCP.
- **Boot-time tracing (5.6):** Ftrace truy vết quá trình khởi động sớm.
- **Thermal pressure (5.7):** Bộ lập lịch tính đến điều tiết nhiệt.
- **perf flame graphs (5.8):** Hỗ trợ trực quan hóa flame graph trong perf(1).

### 3.4.2 systemd

systemd là trình quản lý dịch vụ thường được sử dụng cho Linux. Một tác vụ thỉnh thoảng trong hiệu năng hệ thống là tinh chỉnh thời gian khởi động, và thống kê thời gian systemd có thể cho thấy nơi cần tinh chỉnh:

```
# systemd-analyze
Startup finished in 1.657s (kernel) + 10.272s (userspace) = 11.930s
graphical.target reached after 9.663s in userspace
```

```
# systemd-analyze critical-chain
graphical.target @9.663s
└─multi-user.target @9.661s
  └─snapd.seeded.service @9.062s +62ms
    └─basic.target @6.336s
       └─sockets.target @6.334s
         └─snapd.socket @6.316s +16ms
           └─sysinit.target @6.281s
              └─cloud-init.service @5.361s +905ms
                └─systemd-networkd-wait-online.service @3.498s +1.860s
                  └─systemd-networkd.service @3.254s +235ms
                     └─network-pre.target @3.251s
                       └─cloud-init-local.service @2.107s +1.141s
                          └─systemd-remount-fs.service @391ms +81ms
                            └─systemd-journald.socket @387ms
                              └─system.slice @366ms
                                 └─-.slice @366ms
```

### 3.4.3 KPTI (Meltdown)

Các bản vá kernel page table isolation (KPTI) được thêm vào Linux 4.14 năm 2018 là biện pháp giảm thiểu cho lỗ hổng bộ xử lý Intel gọi là "meltdown." Tác động hiệu năng được đánh giá từ 0.1% đến 6% cho khối lượng công việc sản xuất đám mây Netflix, tùy thuộc vào tần suất syscall [Gregg 18a].

### 3.4.4 Extended BPF

BPF là viết tắt của Berkeley Packet Filter, công nghệ ban đầu được phát triển năm 1992 để cải thiện hiệu năng các công cụ bắt gói tin [McCanne 92]. Năm 2013, Alexei Starovoitov đề xuất viết lại lớn BPF, được phát triển thêm bởi chính ông và Daniel Borkmann và đưa vào nhân Linux năm 2014. Điều này biến BPF thành một một engine thực thi mục đích chung có thể sử dụng cho mạng, khả năng quan sát, và bảo mật.

*Hình 3.16: Các thành phần BPF*

Bytecode BPF phải trước tiên qua bộ xác minh (verifier) kiểm tra an toàn. Chương trình BPF có thể xuất dữ liệu qua perf ring buffer hoặc qua map.

## 3.5 Các chủ đề khác

### 3.5.1 Nhân PGO (PGO Kernel)

Profile-guided optimization (PGO), còn gọi là feedback-directed optimization (FDO), sử dụng thông tin profile CPU để cải thiện quyết định trình biên dịch. Microsoft thấy cải thiện 5 đến 20% từ PGO [Bearman 20]. Google cũng sử dụng nhân LTO và PGO [Tolvanen 20].

### 3.5.2 Unikernel

Unikernel là image máy đơn ứng dụng kết hợp nhân, thư viện, và phần mềm ứng dụng, thường chạy trong một không gian địa chỉ duy nhất.

### 3.5.3 Nhân vi mô và nhân lai (Microkernel và Hybrid Kernel)

Nhân vi mô giữ phần mềm nhân ở mức tối thiểu. Nhân lai kết hợp lợi ích của cả hai. Ví dụ nhân lai: Windows NT, Plan 9.

### 3.5.4 Hệ điều hành phân tán (Distributed Operating System)

Hệ điều hành phân tán chạy một thể hiện hệ điều hành duy nhất trên tập các nút máy tính được nối mạng. Ví dụ: Plan 9, Inferno.

## 3.6 So sánh nhân (Kernel Comparison)

Nhân nào nhanh nhất phụ thuộc vào cấu hình hệ điều hành và khối lượng công việc. Nhìn chung, Linux được kỳ vọng sẽ vượt trội nhờ công việc mở rộng về cải thiện hiệu năng. Top 500 siêu máy tính trở thành 100% Linux vào năm 2017 [TOP500 17].

## 3.7 Bài tập

1. Trả lời các câu hỏi sau về thuật ngữ hệ điều hành:
   - Sự khác biệt giữa tiến trình, luồng, và tác vụ là gì?
   - Chuyển đổi chế độ và chuyển đổi ngữ cảnh là gì?
   - Sự khác biệt giữa phân trang và hoán đổi tiến trình là gì?
   - Sự khác biệt giữa khối lượng công việc I/O-bound và CPU-bound là gì?

2. Trả lời các câu hỏi khái niệm sau:
   - Mô tả vai trò của nhân.
   - Mô tả vai trò của lời gọi hệ thống.
   - Mô tả vai trò của VFS và vị trí của nó trong ngăn xếp I/O.

3. Trả lời các câu hỏi chuyên sâu sau:
   - Liệt kê các lý do tại sao một luồng sẽ rời khỏi CPU hiện tại.
   - Mô tả các lợi thế của bộ nhớ ảo và phân trang theo yêu cầu.

## 3.8 Tài liệu tham khảo

[Graham 68] Graham, B., "Protection in an Information Processing Utility," Communications of the ACM, May 1968.

[Ritchie 74] Ritchie, D. M., and Thompson, K., "The UNIX Time-Sharing System," Communications of the ACM 17, no. 7, pp. 365–75, July 1974.

[Thompson 78] Thompson, K., UNIX Implementation, Bell Laboratories, 1978.

[Bach 86] Bach, M. J., The Design of the UNIX Operating System, Prentice Hall, 1986.

[McCanne 92] McCanne, S., and Jacobson, V., "The BSD Packet Filter: A New Architecture for User-Level Packet Capture", USENIX Winter Conference, 1993.

[Bovet 05] Bovet, D., and Cesati, M., Understanding the Linux Kernel, 3rd Edition, O'Reilly, 2005.

[Corbet 05] Corbet, J., Rubini, A., and Kroah-Hartman, G., Linux Device Drivers, 3rd Edition, O'Reilly, 2005.

[Drysdale 14] Drysdale, D., "Anatomy of a system call, part 2," LWN.net, 2014.

[Borkmann 14b] Borkmann, D., "[PATCH net-next 1/9] net: filter: add jited flag," netdev mailing list, 2014.

[Stewart 15] Stewart, R., et al., "Optimizing TLS for High-Bandwidth Applications in FreeBSD," AsiaBSDCon, 2015.

[McKusick 15] McKusick, M. K., et al., The Design and Implementation of the FreeBSD Operating System, 2nd Edition, Addison-Wesley, 2015.

[Gregg 16a] Gregg, B., "Unikernel Profiling: Flame Graphs from dom0," 2016.

[TOP500 17] TOP500, "List Statistics," 2017.

[Gregg 18a] Gregg, B., "KPTI/KAISER Meltdown Initial Performance Regressions," 2018.

[Gregg 19] Gregg, B., BPF Performance Tools: Linux System and Application Observability, Addison-Wesley, 2019.

[Looney 19] Looney, J., "Netflix and FreeBSD: Using Open Source to Deliver Streaming Video," FOSDEM, 2019.

[Bearman 20] Bearman, I., "Exploring Profile Guided Optimization of the Linux Kernel," Linux Plumber's Conference, 2020.

[Google 20a] Google, "AutoFDO," https://github.com/google/autofdo, accessed 2020.

[Tolvanen 20] Tolvanen, S., et al., "LTO, PGO, and AutoFDO in the Kernel," Linux Plumber's Conference, 2020.

[Owens 20] Owens, K., et al., "4. Kernel Stacks," Linux documentation, 2020.

### 3.8.1 Tài liệu đọc thêm

Hệ điều hành và nhân của chúng là một chủ đề hấp dẫn và rộng lớn. Chương này chỉ tóm tắt những điều thiết yếu. Ngoài các nguồn được đề cập trong chương này, các tài liệu tham khảo xuất sắc khác bao gồm:

[Goodheart 94] Goodheart, B., and Cox J., The Magic Garden Explained: The Internals of UNIX System V Release 4, Prentice Hall, 1994.

[Vahalia 96] Vahalia, U., UNIX Internals: The New Frontiers, Prentice Hall, 1996.

[Singh 06] Singh, A., Mac OS X Internals: A Systems Approach, Addison-Wesley, 2006.

[McDougall 06b] McDougall, R., and Mauro, J., Solaris Internals: Solaris 10 and OpenSolaris Kernel Architecture, Prentice Hall, 2006.

[Love 10] Love, R., Linux Kernel Development, 3rd Edition, Addison-Wesley, 2010.

[Tanenbaum 14] Tanenbaum, A., and Bos, H., Modern Operating Systems, 4th Edition, Pearson, 2014.

[Yosifovich 17] Yosifovich, P., et al., Windows Internals, Part 1, 7th Edition, Microsoft Press, 2017.

### 3.2.4 Ngắt (Interrupt)

Ngắt là một tín hiệu đến bộ xử lý rằng một sự kiện nào đó đã xảy ra cần được xử lý, và làm gián đoạn việc thực thi hiện tại của bộ xử lý để xử lý nó. Nó thường làm cho bộ xử lý chuyển sang chế độ nhân nếu chưa ở đó, lưu trạng thái luồng hiện tại, và sau đó chạy một thủ tục phục vụ ngắt (interrupt service routine - ISR) để xử lý sự kiện.

Có các ngắt bất đồng bộ (asynchronous) được tạo bởi phần cứng bên ngoài và các ngắt đồng bộ (synchronous) được tạo bởi các lệnh phần mềm. Chúng được minh họa trong Hình 3.4.

*Hình 3.4: Các loại ngắt*

Để đơn giản, Hình 3.4 hiển thị tất cả các ngắt được gửi đến nhân để xử lý; thực tế chúng được gửi đến CPU trước, CPU chọn ISR trong nhân để chạy sự kiện.

**Ngắt bất đồng bộ**

Các thiết bị phần cứng có thể gửi các yêu cầu phục vụ ngắt (IRQ) đến bộ xử lý, đến một cách bất đồng bộ so với phần mềm đang chạy. Các ví dụ về ngắt phần cứng bao gồm:

- Thiết bị đĩa báo hiệu hoàn thành I/O đĩa
- Phần cứng chỉ báo một điều kiện lỗi
- Giao diện mạng báo hiệu sự đến của một gói tin
- Thiết bị đầu vào: đầu vào từ bàn phím và chuột

Để giải thích khái niệm ngắt bất đồng bộ, một kịch bản ví dụ được minh họa trong Hình 3.5 cho thấy sự trôi qua của thời gian khi cơ sở dữ liệu (MySQL) chạy trên CPU 0 đọc từ hệ thống tệp. Nội dung hệ thống tệp phải được lấy từ đĩa, vì vậy bộ lập lịch chuyển đổi ngữ cảnh sang luồng khác (ứng dụng Java) trong khi cơ sở dữ liệu đang chờ. Một lúc sau, I/O đĩa hoàn thành, nhưng tại thời điểm này cơ sở dữ liệu không còn chạy trên CPU 0. Ngắt hoàn thành đã xảy ra bất đồng bộ so với cơ sở dữ liệu, được thể hiện bằng đường nét đứt trong Hình 3.5.

*Hình 3.5: Ví dụ ngắt bất đồng bộ*

**Ngắt đồng bộ**

Ngắt đồng bộ được tạo bởi các lệnh phần mềm. Phần sau mô tả các loại ngắt phần mềm khác nhau sử dụng các thuật ngữ trap, ngoại lệ (exception), và lỗi trang (fault); tuy nhiên, các thuật ngữ này thường được sử dụng thay thế cho nhau.

- **Trap:** Một lời gọi có chủ đích vào nhân, chẳng hạn bởi lệnh int (interrupt). Một cách triển khai syscall liên quan đến việc gọi lệnh int với một vector cho trình xử lý syscall (ví dụ: int 0x80 trên Linux x86). int tạo ra một ngắt phần mềm.
- **Ngoại lệ (Exception):** Một điều kiện ngoại lệ, chẳng hạn bởi một lệnh thực hiện phép chia cho số không.
- **Lỗi trang (Fault):** Thuật ngữ thường được sử dụng cho các sự kiện bộ nhớ, chẳng hạn như lỗi trang được kích hoạt bởi việc truy cập một vị trí bộ nhớ mà không có ánh xạ MMU. Xem Chương 7, Bộ nhớ.

Đối với các ngắt này, phần mềm và lệnh chịu trách nhiệm vẫn đang ở trên CPU.

**Luồng ngắt (Interrupt Thread)**

Các thủ tục phục vụ ngắt (ISR) được thiết kế để hoạt động nhanh nhất có thể, nhằm giảm ảnh hưởng của việc gián đoạn các luồng đang hoạt động. Nếu một ngắt cần thực hiện nhiều hơn một ít công việc, đặc biệt nếu nó có thể bị chặn trên các khóa (lock), nó có thể được xử lý bởi một luồng ngắt có thể được lập lịch bởi nhân. Điều này được minh họa trong Hình 3.6.

*Hình 3.6: Xử lý ngắt*

Cách triển khai điều này phụ thuộc vào phiên bản nhân. Trên Linux, trình điều khiển thiết bị có thể được mô hình hóa thành hai nửa, với nửa trên (top half) xử lý ngắt nhanh chóng, và lập lịch công việc cho nửa dưới (bottom half) để xử lý sau [Corbet 05]. Xử lý ngắt nhanh chóng là quan trọng vì nửa trên chạy trong chế độ vô hiệu hóa ngắt để hoãn việc gửi các ngắt mới, điều này có thể gây ra vấn đề độ trễ cho các luồng khác nếu nó chạy quá lâu. Nửa dưới có thể là tasklet hoặc hàng đợi công việc (work queue); hàng đợi công việc là các luồng có thể được lập lịch bởi nhân và có thể ngủ khi cần thiết.

Ví dụ, trình điều khiển mạng Linux có nửa trên để xử lý IRQ cho các gói tin đến, gọi nửa dưới để đẩy gói tin lên ngăn xếp mạng. Nửa dưới được triển khai dưới dạng softirq (ngắt phần mềm).

Thời gian từ khi ngắt đến cho đến khi nó được phục vụ là độ trễ ngắt (interrupt latency), phụ thuộc vào phần cứng và cách triển khai. Đây là chủ đề nghiên cứu cho các hệ thống thời gian thực hoặc độ trễ thấp.

**Che ngắt (Interrupt Masking)**

Một số đường dẫn mã trong nhân không thể bị gián đoạn một cách an toàn. Một ví dụ là mã nhân giành một spin lock trong một lời gọi hệ thống, cho spin lock cũng có thể cần bởi một ngắt. Nhận một ngắt khi đang giữ khóa như vậy có thể gây ra deadlock. Để ngăn tình huống như vậy, nhân có thể tạm thời che (mask) ngắt bằng cách thiết lập thanh ghi mặt nạ ngắt của CPU. Thời gian vô hiệu hóa ngắt nên càng ngắn càng tốt, vì nó có thể xáo trộn việc thực thi kịp thời của các ứng dụng được đánh thức bởi các ngắt khác. Đây là một yếu tố quan trọng cho các hệ thống thời gian thực — những hệ thống có yêu cầu nghiêm ngặt về thời gian phản hồi. Thời gian vô hiệu hóa ngắt cũng là mục tiêu của phân tích hiệu năng (phân tích như vậy được hỗ trợ trực tiếp bởi bộ truy vết irqsoff của Ftrace, được đề cập trong Chương 14, Ftrace).

Một số sự kiện ưu tiên cao không nên bị bỏ qua, và do đó được triển khai dưới dạng ngắt không thể che (non-maskable interrupt - NMI). Ví dụ, Linux có thể sử dụng bộ hẹn giờ watchdog IPMI để kiểm tra xem nhân có bị khóa cứng hay không dựa trên sự thiếu ngắt trong một khoảng thời gian. Nếu vậy, watchdog có thể phát hành ngắt NMI để khởi động lại hệ thống.<sup>5</sup>

> <sup>5</sup> Linux cũng có watchdog NMI phần mềm để phát hiện tình trạng khóa cứng [Linux 20d].

### 3.2.5 Đồng hồ và trạng thái rỗi (Clock and Idle)

Một thành phần cốt lõi của nhân Unix ban đầu là thủ tục clock(), được thực thi từ ngắt hẹn giờ. Nó trong lịch sử được thực thi 60, 100, hoặc 1.000 lần mỗi giây (thường được biểu thị bằng Hertz), và mỗi lần thực thi được gọi là một tick. Các chức năng của nó bao gồm cập nhật thời gian hệ thống, hết hạn timer và lát thời gian cho lập lịch luồng, duy trì thống kê CPU, và thực thi các thủ tục nhân đã lên lịch.

Đã có các vấn đề hiệu năng với đồng hồ, được cải thiện trong các nhân sau này, bao gồm:

- **Độ trễ tick:** Đối với đồng hồ 100 Hertz, có thể gặp thêm đến 10 ms độ trễ cho một timer khi nó chờ được xử lý trong tick tiếp theo. Điều này đã được khắc phục bằng cách sử dụng ngắt thời gian thực độ phân giải cao.
- **Chi phí tick:** Tick tiêu tốn chu kỳ CPU và gây nhiễu nhẹ cho các ứng dụng, và là một nguyên nhân của jitter hệ điều hành. Các bộ xử lý hiện đại cũng có tính năng quản lý năng lượng động, có thể tắt nguồn các phần trong thời gian rỗi. Thủ tục đồng hồ làm gián đoạn thời gian rỗi này, có thể tiêu tốn năng lượng không cần thiết.

Các nhân hiện đại đã chuyển nhiều chức năng ra khỏi thủ tục đồng hồ sang ngắt theo yêu cầu, trong nỗ lực tạo ra nhân không tick (tickless kernel). Điều này giảm chi phí và cải thiện hiệu quả năng lượng bằng cách cho phép bộ xử lý duy trì trạng thái ngủ lâu hơn.

Thủ tục đồng hồ Linux là scheduler_tick(), và Linux có các cách để bỏ qua việc gọi đồng hồ khi không có tải CPU. Bản thân đồng hồ thường chạy ở 250 Hertz (được cấu hình bởi CONFIG_HZ), và các lần gọi được giảm bởi chức năng NO_HZ (CONFIG_NO_HZ), hiện thường được kích hoạt [Linux 20a].

**Luồng rỗi (Idle Thread)**

Khi không có công việc cho CPU thực hiện, nhân lập lịch một luồng giữ chỗ chờ công việc, gọi là luồng rỗi. Một triển khai đơn giản sẽ kiểm tra tính khả dụng của công việc mới trong một vòng lặp. Trong Linux hiện đại, tác vụ rỗi có thể gọi lệnh hlt (halt) để tắt nguồn CPU cho đến khi ngắt tiếp theo được nhận, tiết kiệm năng lượng.

### 3.2.6 Tiến trình (Process)

Một tiến trình là một môi trường để thực thi chương trình cấp người dùng. Nó bao gồm một không gian địa chỉ bộ nhớ, các bộ mô tả tệp, ngăn xếp luồng, và thanh ghi. Ở một số khía cạnh, một tiến trình giống như một máy tính thời kỳ đầu ảo, nơi mà chỉ có một chương trình đang thực thi với các thanh ghi và ngăn xếp riêng.

Các tiến trình được đa nhiệm bởi nhân, thường hỗ trợ thực thi hàng nghìn tiến trình trên một hệ thống đơn. Chúng được xác định riêng lẻ bởi ID tiến trình (PID), là một định danh số duy nhất.

Một tiến trình chứa một hoặc nhiều luồng, hoạt động trong không gian địa chỉ của tiến trình và chia sẻ cùng các bộ mô tả tệp. Một luồng là một ngữ cảnh thực thi bao gồm ngăn xếp, thanh ghi, và con trỏ lệnh (còn gọi là bộ đếm chương trình). Nhiều luồng cho phép một tiến trình đơn thực thi song song trên nhiều CPU. Trên Linux, luồng và tiến trình đều là tác vụ (task).

Tiến trình đầu tiên được khởi chạy bởi nhân được gọi là "init," từ /sbin/init (mặc định), với PID 1, khởi chạy các dịch vụ không gian người dùng. Trong Unix, điều này liên quan đến việc chạy các script khởi động từ /etc, một phương pháp nay được gọi là SysV (theo Unix System V). Các bản phân phối Linux ngày nay thường sử dụng phần mềm systemd để khởi động dịch vụ và theo dõi các phụ thuộc của chúng.

**Tạo tiến trình**

Các tiến trình thường được tạo bằng lời gọi hệ thống fork(2) trên các hệ thống Unix. Trên Linux, các thư viện C thường triển khai hàm fork bằng cách bọc quanh syscall đa năng clone(2). Các syscall này tạo bản sao của tiến trình, với ID tiến trình riêng. Lời gọi hệ thống exec(2) (hoặc biến thể, như execve(2)) sau đó có thể được gọi để bắt đầu thực thi một chương trình khác.

*Hình 3.7: Tạo tiến trình*

Syscall fork(2) hoặc clone(2) có thể sử dụng chiến lược sao chép khi ghi (copy-on-write - COW) để cải thiện hiệu năng. Điều này thêm các tham chiếu đến không gian địa chỉ trước đó thay vì sao chép tất cả nội dung. Khi một trong hai tiến trình sửa đổi bộ nhớ được tham chiếu nhiều lần, một bản sao riêng biệt sau đó được tạo cho các sửa đổi. Chiến lược này hoãn lại hoặc loại bỏ nhu cầu sao chép bộ nhớ, giảm sử dụng bộ nhớ và CPU.

**Vòng đời tiến trình**

*Hình 3.8: Vòng đời tiến trình*

Trạng thái on-proc là khi đang chạy trên bộ xử lý (CPU). Trạng thái ready-to-run là khi tiến trình có thể chạy nhưng đang chờ trên hàng đợi chạy của CPU để đến lượt. Hầu hết I/O sẽ chặn, đưa tiến trình vào trạng thái ngủ cho đến khi I/O hoàn thành và tiến trình được đánh thức. Trạng thái zombie xảy ra trong quá trình kết thúc tiến trình, khi tiến trình chờ cho đến khi trạng thái của nó được thu hồi bởi tiến trình cha hoặc bị loại bỏ bởi nhân.

**Môi trường tiến trình**

*Hình 3.9: Môi trường tiến trình*

Ngữ cảnh nhân bao gồm các thuộc tính và thống kê tiến trình: ID tiến trình (PID), ID người dùng chủ sở hữu (UID), và các thời gian khác nhau, thường được kiểm tra qua ps(1) và top(1). Nó cũng có tập bộ mô tả tệp, tham chiếu tệp đang mở và (thường) được chia sẻ giữa các luồng.

Trên Linux, mỗi luồng có ngăn xếp người dùng riêng và ngăn xếp ngoại lệ nhân riêng [Owens 20].

### 3.2.7 Ngăn xếp (Stack)

Ngăn xếp là vùng lưu trữ bộ nhớ cho dữ liệu tạm thời, được tổ chức dưới dạng danh sách vào sau ra trước (LIFO). Nó được sử dụng để lưu trữ dữ liệu ít quan trọng hơn so với dữ liệu vừa trong tập thanh ghi CPU. Khi một hàm được gọi, địa chỉ trả về được lưu vào ngăn xếp. Khi hàm được gọi hoàn thành, nó khôi phục thanh ghi cần thiết và chuyển thực thi đến hàm gọi. Tập dữ liệu trên ngăn xếp liên quan đến thực thi của một hàm được gọi là khung ngăn xếp (stack frame).

Đường dẫn gọi đến hàm đang thực thi hiện tại có thể được xem bằng cách kiểm tra các địa chỉ trả về đã lưu qua tất cả các khung ngăn xếp (duyệt ngăn xếp - stack walking). Đường dẫn gọi này được gọi là stack back trace hoặc stack trace, và là công cụ vô giá cho gỡ lỗi và phân tích hiệu năng.

**Cách đọc một Stack**

```
tcp_sendmsg+1
sock_sendmsg+62
SYSC_sendto+319
sys_sendto+14
do_syscall_64+115
entry_SYSCALL_64_after_hwframe+61
```

Ngăn xếp thường được in theo thứ tự từ lá đến gốc. Bằng cách đọc từ dưới lên, bạn có thể theo dõi đường dẫn thực thi đến hàm hiện tại.

**Ngăn xếp người dùng và nhân**

Trong khi thực thi một lời gọi hệ thống, một luồng tiến trình có hai ngăn xếp: ngăn xếp cấp người dùng và ngăn xếp cấp nhân.

*Hình 3.10: Ngăn xếp người dùng và nhân*

Ngăn xếp cấp người dùng của luồng bị chặn không thay đổi trong suốt thời gian lời gọi hệ thống, vì luồng đang sử dụng ngăn xếp cấp nhân riêng biệt trong ngữ cảnh nhân.

### 3.2.8 Bộ nhớ ảo (Virtual Memory)

Bộ nhớ ảo là trừu tượng hóa của bộ nhớ chính, cung cấp cho tiến trình và nhân cái nhìn riêng tư, gần như vô hạn, về bộ nhớ chính. Nó hỗ trợ đa nhiệm và đăng ký vượt mức (oversubscription) bộ nhớ chính.

*Hình 3.11: Không gian địa chỉ bộ nhớ ảo*

**Quản lý bộ nhớ**

Có hai cơ chế nhân:

- **Hoán đổi tiến trình (Process swapping):** di chuyển toàn bộ tiến trình giữa bộ nhớ chính và bộ lưu trữ thứ cấp.
- **Phân trang (Paging):** di chuyển các đơn vị bộ nhớ nhỏ gọi là trang (ví dụ: 4 Kbyte).

Trong Linux, thuật ngữ swapping được sử dụng để chỉ phân trang. Nhân Linux không hỗ trợ kiểu hoán đổi tiến trình Unix cũ.

### 3.2.9 Bộ lập lịch (Scheduler)

Unix và các hệ thống phái sinh là các hệ thống chia sẻ thời gian. Bộ lập lịch ánh xạ luồng (tác vụ) vào CPU, chia thời gian CPU giữa chúng và duy trì khái niệm về mức ưu tiên.

*Hình 3.12: Bộ lập lịch nhân*

Các khối lượng công việc được phân loại thành:

- **CPU-bound:** Ứng dụng tính toán nặng, bị giới hạn bởi tài nguyên CPU.
- **I/O-bound:** Ứng dụng thực hiện I/O, bị giới hạn bởi I/O đến tài nguyên lưu trữ hoặc mạng.

Các nhân hiện đại hỗ trợ nhiều lớp lập lịch hoặc chính sách lập lịch (scheduling policy) áp dụng các thuật toán khác nhau, bao gồm lập lịch thời gian thực.

### 3.2.10 Hệ thống tệp (File System)

Hệ thống tệp là tổ chức dữ liệu dưới dạng tệp và thư mục, thường dựa trên chuẩn POSIX. Hệ điều hành cung cấp không gian tên tệp toàn cục, tổ chức dưới dạng cây bắt đầu từ gốc ("/").

*Hình 3.13: Phân cấp tệp hệ điều hành*

**VFS**

Hệ thống tệp ảo (VFS) là giao diện nhân để trừu tượng hóa các loại hệ thống tệp, ban đầu được phát triển bởi Sun Microsystems.

*Hình 3.14: Hệ thống tệp ảo*

**Ngăn xếp I/O**

*Hình 3.15: Ngăn xếp I/O chung*

### 3.2.11 Bộ nhớ đệm (Caching)

**Bảng 3.2: Các lớp bộ nhớ đệm ví dụ cho I/O đĩa**

| # | Bộ nhớ đệm | Ví dụ |
|---|---|---|
| 1 | Client cache | Bộ nhớ đệm trình duyệt web |
| 2 | Application cache | — |
| 3 | Web server cache | Apache cache |
| 4 | Caching server | memcached |
| 5 | Database cache | MySQL buffer cache |
| 6 | Directory cache | dcache |
| 7 | File metadata cache | inode cache |
| 8 | OS buffer cache | Buffer cache |
| 9 | FS primary cache | Page cache, ZFS ARC |
| 10 | FS secondary cache | ZFS L2ARC |
| 11 | Device cache | ZFS vdev |
| 12 | Block cache | Buffer cache |
| 13 | Disk controller cache | RAID card cache |
| 14 | Storage array cache | — |
| 15 | On-disk cache | — |

### 3.2.12 Mạng (Networking)

Các nhân hiện đại cung cấp ngăn xếp giao thức mạng tích hợp (ngăn xếp TCP/IP). Ứng dụng truy cập mạng qua socket.

### 3.2.13 Trình điều khiển thiết bị (Device Driver)

Trình điều khiển thiết bị là phần mềm nhân cho quản lý và I/O thiết bị. Chúng cung cấp giao diện ký tự (character) và/hoặc khối (block) cho thiết bị. Trong Linux, buffer cache hiện là một phần của page cache.

### 3.2.14 Đa bộ xử lý (Multiprocessor)

Hỗ trợ đa bộ xử lý thường được triển khai dưới dạng đa xử lý đối xứng (SMP). Trên hệ thống đa bộ xử lý cũng có thể có kiến trúc NUMA.

**IPI:** Ngắt liên xử lý (inter-processor interrupt) để phối hợp giữa các CPU.

### 3.2.15 Chiếm quyền ưu tiên (Preemption)

Hỗ trợ chiếm quyền ưu tiên nhân cho phép các luồng ưu tiên cao gián đoạn nhân. Linux hỗ trợ CONFIG_PREEMPT_VOLUNTARY (tự nguyện), CONFIG_PREEMPT (đầy đủ), và CONFIG_PREEMPT_NONE.

### 3.2.16 Quản lý tài nguyên (Resource Management)

Bao gồm kiểm soát tài nguyên (resource control) cho CPU, bộ nhớ, đĩa, mạng. Linux sử dụng cgroup (2.6.24) và cgroup v2 (4.5).

### 3.2.17 Khả năng quan sát (Observability)

Các công cụ quan sát được giới thiệu trong Chương 4.

## 3.3 Các nhân (Kernel)

**Bảng 3.3: Các phiên bản nhân với số lượng syscall**

| Phiên bản nhân | Syscall |
|---|---|
| UNIX Version 7 | 48 |
| SunOS (Solaris) 5.11 | 142 |
| FreeBSD 12.0 | 222 |
| Linux 5.3.0-1010-aws | 493 |

### 3.3.1 Unix

Unix được phát triển bởi Ken Thompson, Dennis Ritchie, và những người khác tại AT&T Bell Labs từ năm 1969.

### 3.3.2 BSD

BSD bắt đầu như các cải tiến cho Unix phiên bản 6 tại UC Berkeley (1978). Các phát triển chính: bộ nhớ ảo phân trang, phân trang theo yêu cầu, FFS, ngăn xếp TCP/IP, socket, jail, kernel TLS.

### 3.3.3 Solaris

Solaris được tạo bởi Sun Microsystems (1982). Các phát triển chính: VFS, nhân hoàn toàn có thể chiếm quyền, hỗ trợ đa bộ xử lý, slab allocator, DTrace, zone, ZFS.

## 3.4 Linux

Linux được tạo vào năm 1991 bởi Linus Torvalds như một hệ điều hành miễn phí cho máy tính cá nhân Intel. Nhân Linux được phát triển dựa trên ý tưởng chung từ nhiều tổ tiên, bao gồm: Unix (và Multics), BSD, Solaris, Plan 9.

### 3.4.1 Các phát triển nhân Linux

Các phát triển nhân Linux liên quan đến hiệu năng bao gồm (nhiều mô tả bao gồm phiên bản nhân Linux nơi chúng được giới thiệu lần đầu):

- **Lớp lập lịch CPU:** Nhiều thuật toán lập lịch CPU tiên tiến, bao gồm scheduling domain (2.6.7) cho quyết định tốt hơn về NUMA.
- **Lớp lập lịch I/O:** Các thuật toán lập lịch I/O khối khác nhau: deadline (2.5.39), anticipatory (2.5.75), CFQ (2.6.6).
- **Thuật toán tắc nghẽn TCP:** Linux cho phép cấu hình các thuật toán kiểm soát tắc nghẽn TCP khác nhau: Reno, Cubic, v.v.
- **Overcommit:** Cùng với OOM killer, đây là chiến lược để làm nhiều hơn với ít bộ nhớ chính hơn.
- **Futex (2.5.7):** Mutex nhanh trong không gian người dùng.
- **Huge pages (2.5.36):** Hỗ trợ trang bộ nhớ lớn được cấp phát trước.
- **OProfile (2.5.43):** Bộ profiler hệ thống cho CPU.
- **RCU (2.5.43):** Cơ chế đồng bộ hóa read-copy update.
- **epoll (2.5.46):** Lời gọi hệ thống cho chờ I/O hiệu quả trên nhiều bộ mô tả tệp.
- **Lập lịch I/O module (2.6.10):** Thuật toán lập lịch có thể cắm cho I/O thiết bị khối.
- **DebugFS (2.6.11):** Giao diện đơn giản cho nhân phơi bày dữ liệu cho cấp người dùng.
- **Cpusets (2.6.12):** Nhóm CPU độc quyền cho tiến trình.
- **Chiếm quyền ưu tiên nhân tự nguyện (2.6.13):** Lập lịch độ trễ thấp không cần phức tạp của chiếm quyền đầy đủ.
- **inotify (2.6.13):** Khung giám sát sự kiện hệ thống tệp.
- **blktrace (2.6.17):** Khung và công cụ truy vết sự kiện I/O khối.
- **splice (2.6.17):** Syscall di chuyển dữ liệu nhanh giữa bộ mô tả tệp và pipe.
- **Delay accounting (2.6.18):** Theo dõi trạng thái trễ theo tác vụ.
- **IO accounting (2.6.20):** Đo lường thống kê I/O lưu trữ theo tiến trình.
- **DynTicks (2.6.21):** Tick động cho phép ngắt hẹn giờ nhân không kích hoạt khi rỗi.
- **SLUB (2.6.22):** Phiên bản mới đơn giản hóa của bộ cấp phát bộ nhớ slab.
- **CFS (2.6.23):** Completely fair scheduler.
- **cgroups (2.6.24):** Nhóm kiểm soát cho đo lường và giới hạn sử dụng tài nguyên.
- **TCP LRO (2.6.24):** TCP Large Receive Offload.
- **latencytop (2.6.25):** Công cụ quan sát nguồn gốc độ trễ.
- **Tracepoints (2.6.28):** Điểm truy vết tĩnh nhân.
- **perf (2.6.31):** Linux Performance Events.
- **No BKL (2.6.37):** Loại bỏ cuối cùng big kernel lock.
- **Transparent huge pages (2.6.38):** Khung cho sử dụng dễ dàng trang bộ nhớ lớn.
- **KVM:** Kernel-based Virtual Machine.
- **BPF JIT (3.0):** Trình biên dịch Just-In-Time cho BPF.
- **CFS bandwidth control (3.2):** Hạn ngạch và điều tiết CPU.
- **TCP anti-bufferbloat (3.3+):** Các cải tiến chống bufferbloat.
- **uprobes (3.5):** Cơ sở hạ tầng truy vết động cấp người dùng.
- **TFO (3.6, 3.7, 3.13):** TCP Fast Open.
- **NUMA balancing (3.8+):** Cân bằng tự động vị trí bộ nhớ trên hệ thống đa NUMA.
- **SO_REUSEPORT (3.9):** Tùy chọn socket cho nhiều listener trên cùng cổng.
- **bcache (3.10):** Công nghệ đệm SSD cho giao diện khối.
- **TCP TLP (3.10):** TCP Tail Loss Probe.
- **NO_HZ_FULL (3.10, 3.12):** Nhân tickless.
- **Multiqueue block I/O (3.13):** Hàng đợi gửi I/O theo CPU.
- **SCHED_DEADLINE (3.14):** Lập lịch earliest deadline first (EDF).
- **TCP autocorking (3.14):** Nhân gộp các lần ghi nhỏ.
- **MCS locks và qspinlocks (3.15):** Khóa nhân hiệu quả.
- **Extended BPF (3.18+):** Môi trường thực thi trong nhân cho các chương trình chế độ nhân an toàn.
- **Overlayfs (3.18):** Hệ thống tệp union mount, thường dùng cho container.
- **DCTCP (3.18):** Thuật toán tắc nghẽn Data Center TCP.
- **DAX (4.0):** Direct Access cho bộ nhớ liên tục (persistent memory).
- **Queued spinlocks (4.2):** Hiệu năng tốt hơn dưới tranh chấp.
- **TCP lockless listener (4.4):** Đường dẫn nhanh TCP listener không khóa.
- **cgroup v2 (4.5, 4.15):** Phân cấp thống nhất cho cgroup.
- **epoll scalability (4.5):** Cải thiện khả năng mở rộng đa luồng cho epoll.
- **TCP NV (4.8):** New Vegas cho mạng băng thông cao.
- **XDP (4.8, 4.18):** eXpress Data Path cho mạng hiệu năng cao.
- **TCP BBR (4.9):** Thuật toán tắc nghẽn Bottleneck Bandwidth and RTT.
- **Hardware latency tracer (4.9):** Bộ truy vết Ftrace phát hiện độ trễ phần cứng.
- **perf c2c (4.10):** Xác định vấn đề hiệu năng bộ nhớ đệm CPU.
- **Intel CAT (4.10):** Cache Allocation Technology.
- **BFQ, Kyber (4.12):** Bộ lập lịch I/O đa hàng đợi.
- **Kernel TLS (4.13, 4.17):** Phiên bản Linux của kernel TLS.
- **MSG_ZEROCOPY (4.14):** Cờ send(2) tránh sao chép thêm byte gói tin.
- **PCID (4.14):** Hỗ trợ process-context ID, giảm chi phí TLB flush.
- **PSI (4.20, 5.2):** Pressure stall information.
- **TCP EDT (4.20):** Early Departure Time cho gửi gói tin.
- **Multi-queue I/O (5.0):** Mặc định từ 5.0.
- **UDP GRO (5.0):** UDP Generic Receive Offload.
- **io_uring (5.1):** Giao diện bất đồng bộ chung cho giao tiếp nhanh ứng dụng-nhân.
- **MADV_COLD, MADV_PAGEOUT (5.4):** Gợi ý madvise(2) cho quản lý bộ nhớ.
- **MultiPath TCP (5.6):** Nhiều liên kết mạng cho một kết nối TCP.
- **Boot-time tracing (5.6):** Ftrace truy vết quá trình khởi động sớm.
- **Thermal pressure (5.7):** Bộ lập lịch tính đến điều tiết nhiệt.
- **perf flame graphs (5.8):** Hỗ trợ trực quan hóa flame graph trong perf(1).

### 3.4.2 systemd

systemd là trình quản lý dịch vụ thường được sử dụng cho Linux. Một tác vụ thỉnh thoảng trong hiệu năng hệ thống là tinh chỉnh thời gian khởi động, và thống kê thời gian systemd có thể cho thấy nơi cần tinh chỉnh:

```
# systemd-analyze
Startup finished in 1.657s (kernel) + 10.272s (userspace) = 11.930s
graphical.target reached after 9.663s in userspace
```

```
# systemd-analyze critical-chain
graphical.target @9.663s
└─multi-user.target @9.661s
  └─snapd.seeded.service @9.062s +62ms
    └─basic.target @6.336s
       └─sockets.target @6.334s
         └─snapd.socket @6.316s +16ms
           └─sysinit.target @6.281s
              └─cloud-init.service @5.361s +905ms
                └─systemd-networkd-wait-online.service @3.498s +1.860s
                  └─systemd-networkd.service @3.254s +235ms
                     └─network-pre.target @3.251s
                       └─cloud-init-local.service @2.107s +1.141s
                          └─systemd-remount-fs.service @391ms +81ms
                            └─systemd-journald.socket @387ms
                              └─system.slice @366ms
                                 └─-.slice @366ms
```

### 3.4.3 KPTI (Meltdown)

Các bản vá kernel page table isolation (KPTI) được thêm vào Linux 4.14 năm 2018 là biện pháp giảm thiểu cho lỗ hổng bộ xử lý Intel gọi là "meltdown." Tác động hiệu năng được đánh giá từ 0.1% đến 6% cho khối lượng công việc sản xuất đám mây Netflix, tùy thuộc vào tần suất syscall [Gregg 18a].

### 3.4.4 Extended BPF

BPF là viết tắt của Berkeley Packet Filter, công nghệ ban đầu được phát triển năm 1992 để cải thiện hiệu năng các công cụ bắt gói tin [McCanne 92]. Năm 2013, Alexei Starovoitov đề xuất viết lại lớn BPF, được phát triển thêm bởi chính ông và Daniel Borkmann và đưa vào nhân Linux năm 2014. Điều này biến BPF thành một một engine thực thi mục đích chung có thể sử dụng cho mạng, khả năng quan sát, và bảo mật.

*Hình 3.16: Các thành phần BPF*

Bytecode BPF phải trước tiên qua bộ xác minh (verifier) kiểm tra an toàn. Chương trình BPF có thể xuất dữ liệu qua perf ring buffer hoặc qua map.

## 3.5 Các chủ đề khác

### 3.5.1 Nhân PGO (PGO Kernel)

Profile-guided optimization (PGO), còn gọi là feedback-directed optimization (FDO), sử dụng thông tin profile CPU để cải thiện quyết định trình biên dịch. Microsoft thấy cải thiện 5 đến 20% từ PGO [Bearman 20]. Google cũng sử dụng nhân LTO và PGO [Tolvanen 20].

### 3.5.2 Unikernel

Unikernel là image máy đơn ứng dụng kết hợp nhân, thư viện, và phần mềm ứng dụng, thường chạy trong một không gian địa chỉ duy nhất.

### 3.5.3 Nhân vi mô và nhân lai (Microkernel và Hybrid Kernel)

Nhân vi mô giữ phần mềm nhân ở mức tối thiểu. Nhân lai kết hợp lợi ích của cả hai. Ví dụ nhân lai: Windows NT, Plan 9.

### 3.5.4 Hệ điều hành phân tán (Distributed Operating System)

Hệ điều hành phân tán chạy một thể hiện hệ điều hành duy nhất trên tập các nút máy tính được nối mạng. Ví dụ: Plan 9, Inferno.

## 3.6 So sánh nhân (Kernel Comparison)

Nhân nào nhanh nhất phụ thuộc vào cấu hình hệ điều hành và khối lượng công việc. Nhìn chung, Linux được kỳ vọng sẽ vượt trội nhờ công việc mở rộng về cải thiện hiệu năng. Top 500 siêu máy tính trở thành 100% Linux vào năm 2017 [TOP500 17].

## 3.7 Bài tập

1. Trả lời các câu hỏi sau về thuật ngữ hệ điều hành:
   - Sự khác biệt giữa tiến trình, luồng, và tác vụ là gì?
   - Chuyển đổi chế độ và chuyển đổi ngữ cảnh là gì?
   - Sự khác biệt giữa phân trang và hoán đổi tiến trình là gì?
   - Sự khác biệt giữa khối lượng công việc I/O-bound và CPU-bound là gì?

2. Trả lời các câu hỏi khái niệm sau:
   - Mô tả vai trò của nhân.
   - Mô tả vai trò của lời gọi hệ thống.
   - Mô tả vai trò của VFS và vị trí của nó trong ngăn xếp I/O.

3. Trả lời các câu hỏi chuyên sâu sau:
   - Liệt kê các lý do tại sao một luồng sẽ rời khỏi CPU hiện tại.
   - Mô tả các lợi thế của bộ nhớ ảo và phân trang theo yêu cầu.

## 3.8 Tài liệu tham khảo

[Graham 68] Graham, B., "Protection in an Information Processing Utility," Communications of the ACM, May 1968.

[Ritchie 74] Ritchie, D. M., and Thompson, K., "The UNIX Time-Sharing System," Communications of the ACM 17, no. 7, pp. 365–75, July 1974.

[Thompson 78] Thompson, K., UNIX Implementation, Bell Laboratories, 1978.

[Bach 86] Bach, M. J., The Design of the UNIX Operating System, Prentice Hall, 1986.

[McCanne 92] McCanne, S., and Jacobson, V., "The BSD Packet Filter: A New Architecture for User-Level Packet Capture", USENIX Winter Conference, 1993.

[Bovet 05] Bovet, D., and Cesati, M., Understanding the Linux Kernel, 3rd Edition, O'Reilly, 2005.

[Corbet 05] Corbet, J., Rubini, A., and Kroah-Hartman, G., Linux Device Drivers, 3rd Edition, O'Reilly, 2005.

[Drysdale 14] Drysdale, D., "Anatomy of a system call, part 2," LWN.net, 2014.

[Borkmann 14b] Borkmann, D., "[PATCH net-next 1/9] net: filter: add jited flag," netdev mailing list, 2014.

[Stewart 15] Stewart, R., et al., "Optimizing TLS for High-Bandwidth Applications in FreeBSD," AsiaBSDCon, 2015.

[McKusick 15] McKusick, M. K., et al., The Design and Implementation of the FreeBSD Operating System, 2nd Edition, Addison-Wesley, 2015.

[Gregg 16a] Gregg, B., "Unikernel Profiling: Flame Graphs from dom0," 2016.

[TOP500 17] TOP500, "List Statistics," 2017.

[Gregg 18a] Gregg, B., "KPTI/KAISER Meltdown Initial Performance Regressions," 2018.

[Gregg 19] Gregg, B., BPF Performance Tools: Linux System and Application Observability, Addison-Wesley, 2019.

[Looney 19] Looney, J., "Netflix and FreeBSD: Using Open Source to Deliver Streaming Video," FOSDEM, 2019.

[Bearman 20] Bearman, I., "Exploring Profile Guided Optimization of the Linux Kernel," Linux Plumber's Conference, 2020.

[Google 20a] Google, "AutoFDO," https://github.com/google/autofdo, accessed 2020.

[Tolvanen 20] Tolvanen, S., et al., "LTO, PGO, and AutoFDO in the Kernel," Linux Plumber's Conference, 2020.

[Owens 20] Owens, K., et al., "4. Kernel Stacks," Linux documentation, 2020.

### 3.8.1 Tài liệu đọc thêm

Hệ điều hành và nhân của chúng là một chủ đề hấp dẫn và rộng lớn. Chương này chỉ tóm tắt những điều thiết yếu. Ngoài các nguồn được đề cập trong chương này, các tài liệu tham khảo xuất sắc khác bao gồm:

[Goodheart 94] Goodheart, B., and Cox J., The Magic Garden Explained: The Internals of UNIX System V Release 4, Prentice Hall, 1994.

[Vahalia 96] Vahalia, U., UNIX Internals: The New Frontiers, Prentice Hall, 1996.

[Singh 06] Singh, A., Mac OS X Internals: A Systems Approach, Addison-Wesley, 2006.

[McDougall 06b] McDougall, R., and Mauro, J., Solaris Internals: Solaris 10 and OpenSolaris Kernel Architecture, Prentice Hall, 2006.

[Love 10] Love, R., Linux Kernel Development, 3rd Edition, Addison-Wesley, 2010.

[Tanenbaum 14] Tanenbaum, A., and Bos, H., Modern Operating Systems, 4th Edition, Pearson, 2014.

[Yosifovich 17] Yosifovich, P., et al., Windows Internals, Part 1, 7th Edition, Microsoft Press, 2017.
