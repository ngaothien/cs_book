# Chương 6: CPU (CPUs)

Các CPU điều khiển tất cả phần mềm và thường là mục tiêu đầu tiên cho phân tích hiệu năng hệ thống. Chương này giải thích phần cứng và phần mềm CPU, và chỉ ra cách sử dụng CPU có thể được kiểm tra chi tiết để tìm kiếm các cải thiện hiệu năng.

Ở mức độ cao, mức độ sử dụng CPU toàn hệ thống (system-wide CPU utilization) có thể được giám sát, và việc sử dụng theo tiến trình hoặc luồng (process or thread) có thể được kiểm tra. Ở mức độ thấp hơn, các đường dẫn mã (code paths) trong các ứng dụng và nhân (kernel) có thể được lập hồ sơ (profiled) và nghiên cứu, cũng như việc sử dụng CPU bởi các ngắt (interrupts). Ở mức độ thấp nhất, thực thi lệnh (instruction execution) CPU và hành vi chu kỳ (cycle behavior) có thể được phân tích. Các hành vi khác cũng có thể được điều tra, bao gồm độ trễ bộ lập lịch (scheduler latency) khi các tác vụ chờ đến lượt trên các CPU, điều này làm giảm hiệu năng.

Các mục tiêu học tập của chương này là:
- Hiểu các mô hình và khái niệm về CPU.
- Làm quen với nội bộ phần cứng CPU.
- Làm quen với nội bộ bộ lập lịch CPU (CPU scheduler).
- Tuân theo các phương pháp luận khác nhau cho phân tích CPU.
- Diễn giải các mức tải trung bình (load averages) và PSI.
- Đặc trưng hóa mức sử dụng toàn hệ thống và trên mỗi CPU (per-CPU utilization).
- Xác định và định lượng các vấn đề về độ trễ bộ lập lịch.
- Thực hiện phân tích chu kỳ CPU để xác định sự kém hiệu quả.
- Điều tra sử dụng CPU bằng các trình lập hồ sơ (profilers) và CPU flame graphs.
- Xác định bộ tiêu thụ CPU IRQ cứng và mềm.
- Diễn giải CPU flame graphs và các biểu đồ trực quan hóa CPU khác.
- Nhận biết các tham số có thể tinh chỉnh (tunable parameters) của CPU.

Chương này có sáu phần. Ba phần đầu tiên cung cấp cơ sở cho phân tích CPU, và ba phần cuối hiển thị ứng dụng thực tế của nó cho các hệ thống dựa trên Linux. Các phần đó là:
- **Tiểu sử (Background)**: giới thiệu thuật ngữ liên quan đến CPU, các mô hình cơ bản của CPU, và các khái niệm hiệu năng CPU chính.
- **Kiến trúc (Architecture)**: giới thiệu kiến trúc vi xử lý và bộ lập lịch nhân.
- **Phương pháp luận (Methodology)**: mô tả các phương pháp luận phân tích hiệu năng, cả quan sát và thực nghiệm.
- **Công cụ Quan sát (Observability Tools)**: mô tả các công cụ phân tích hiệu năng CPU trên các hệ thống dựa trên Linux, bao gồm lập hồ sơ, truy vết, và trực quan hóa.
- **Thực nghiệm (Experimentation)**: tóm tắt các công cụ benchmark CPU.
- **Tinh chỉnh (Tuning)**: bao gồm các ví dụ về các tham số có thể tinh chỉnh.

Các ảnh hưởng của I/O bộ nhớ đối với hiệu năng CPU cũng được đề cập, bao gồm chu kỳ CPU bị đình trệ (stalled) do bộ nhớ và hiệu năng của các bộ nhớ đệm CPU (CPU caches). Chương 7, Bộ nhớ, tiếp tục cuộc thảo luận về I/O bộ nhớ, bao gồm MMU, NUMA/UMA, kết nối liên thông hệ thống (system interconnects), và bus bộ nhớ.

## 6.1 Thuật ngữ (Terminology)

Để tham khảo, các thuật ngữ liên quan đến CPU được sử dụng trong chương này bao gồm:
- **Bộ vi xử lý (Processor)**: Con chip vật lý cắm vào một đế (socket) trên hệ thống hoặc bo mạch vi xử lý và chứa một hoặc nhiều CPU được triển khai dưới dạng các lõi (cores) hoặc các luồng phần cứng (hardware threads).
- **Lõi (Core)**: Một phiên bản CPU độc lập trên một bộ đa xử lý (multicore processor). Việc sử dụng các lõi là một cách để mở rộng quy mô các bộ vi xử lý, được gọi là chip-level multiprocessing (CMP).
- **Luồng phần cứng (Hardware thread)**: Một kiến trúc CPU hỗ trợ thực thi nhiều luồng song song trên một lõi duy nhất (bao gồm Công nghệ Hyper-Threading của Intel), trong đó mỗi luồng là một phiên bản CPU độc lập. Cách tiếp cận mở rộng quy mô này được gọi là simultaneous multithreading (SMT) (đa luồng đồng thời).
- **Lệnh CPU (CPU instruction)**: Một thao tác duy nhất của CPU, từ tập lệnh của nó. Có các lệnh cho các phép toán số học, I/O bộ nhớ, và logic điều khiển.
- **CPU logic (Logical CPU)**: Còn được gọi là bộ vi xử lý ảo (virtual processor), một phiên bản CPU của hệ điều hành (một thực thể CPU có thể lập lịch). Điều này có thể được vi xử lý triển khai như một luồng phần cứng (trong trường hợp đó nó cũng có thể được gọi là lõi ảo - virtual core), một lõi, hoặc một bộ vi xử lý lõi đơn. (Nó cũng đôi khi được gọi là virtual CPU; tuy nhiên, thuật ngữ đó thường được sử dụng hơn để chỉ các phiên bản CPU ảo được cung cấp bởi một công nghệ ảo hóa. Xem Chương 11, Điện toán Đám mây.)
- **Bộ lập lịch (Scheduler)**: Hệ thống con của nhân gán các luồng để chạy trên các CPU.
- **Hàng đợi chạy (Run queue)**: Một hàng đợi của các luồng có thể chạy (runnable threads) đang chờ được phục vụ bởi các CPU. Các nhân hiện đại có thể sử dụng một số cấu trúc dữ liệu khác (ví dụ: cây đỏ-đen) để lưu trữ các luồng có thể chạy, nhưng chúng ta vẫn thường dùng thuật ngữ "hàng đợi chạy".

Các thuật ngữ khác được giới thiệu xuyên suốt chương này. Bảng thuật ngữ (Glossary) bao gồm các thuật ngữ cơ bản để tham khảo, bao gồm CPU, chu kỳ CPU (CPU cycle), và ngăn xếp (stack). Xem thêm các phần thuật ngữ trong Chương 2 và Chương 3.

## 6.2 Các Mô hình (Models)

Các mô hình đơn giản sau đây minh họa một số nguyên tắc cơ bản của CPU và hiệu năng CPU. Mục 6.4, Kiến trúc, đi sâu hơn nhiều và bao gồm các chi tiết dành riêng cho việc triển khai.

### 6.2.1 Kiến trúc CPU (CPU Architecture)

Hình 6.1 hiển thị một ví dụ về kiến trúc CPU, cho một bộ vi xử lý lõi tứ và có tám luồng phần cứng. Kiến trúc vật lý được vẽ ra, cùng với cách nó được hệ điều hành nhìn thấy. (Có một công cụ dành cho Linux là lstopo(1) có thể tạo các sơ đồ tương tự như hình này cho hệ thống hiện tại, một ví dụ có ở Mục 6.6.21, Các Công cụ khác.)

*Hình 6.1: Kiến trúc CPU*

Mỗi luồng phần cứng có thể định địa chỉ như một CPU logic, vì vậy bộ vi xử lý này xuất hiện dưới dạng tám CPU. Hệ điều hành có thể có thêm một số kiến thức về topology (cấu trúc mạng) để cải thiện các quyết định lập lịch của nó, chẳng hạn như CPU nào nằm trên cùng một lõi và cách các bộ nhớ đệm CPU được chia sẻ.

### 6.2.2 Các Bộ nhớ đệm CPU (CPU Memory Caches)

Các bộ vi xử lý cung cấp nhiều bộ nhớ đệm phần cứng để cải thiện hiệu năng I/O bộ nhớ. Hình 6.2 hiển thị mối quan hệ của các kích thước bộ nhớ đệm, sẽ trở nên nhỏ hơn và nhanh hơn (sự đánh đổi) khi chúng ngày càng gần CPU hơn.

Các bộ nhớ đệm nào có mặt, và liệu chúng có nằm trên bộ vi xử lý (tích hợp - integrated) hay bên ngoài bộ vi xử lý (external) phụ thuộc vào loại vi xử lý. Các bộ vi xử lý trước đây cung cấp ít bộ nhớ đệm tích hợp hơn.

*Hình 6.2: Kích thước bộ nhớ đệm CPU*

### 6.2.3 Các Hàng đợi Chạy CPU (CPU Run Queues)

Hình 6.3 hiển thị một hàng đợi chạy CPU được quản lý bởi bộ lập lịch của nhân.

*Hình 6.3: Hàng đợi chạy CPU*

Các trạng thái luồng được hiển thị trong hình: "sẵn sàng để chạy" (ready to run) và "trên CPU" (on-CPU), được trình bày trong Hình 3.8 ở Chương 3, Hệ điều hành.

Số lượng các luồng phần mềm được xếp hàng và sẵn sàng chạy là một số liệu hiệu năng quan trọng chỉ ra mức độ bão hòa (saturation) của CPU. Trong hình này (tại khoảnh khắc này) có bốn luồng, cùng với một luồng bổ sung đang chạy trên CPU. Thời gian chờ đợi trên một hàng đợi chạy CPU đôi khi được gọi là độ trễ hàng đợi chạy (run-queue latency) hoặc độ trễ hàng đợi điều phối (dispatcher-queue latency). Trong cuốn sách này, thuật ngữ "độ trễ bộ lập lịch" (scheduler latency) thường được sử dụng, vì nó phù hợp cho tất cả các bộ lập lịch, bao gồm cả những bộ không sử dụng hàng đợi (xem phần thảo luận về CFS trong Mục 6.4.2, Phần mềm).

Đối với các hệ thống đa vi xử lý (multiprocessor), nhân thường cung cấp một hàng đợi chạy cho mỗi CPU, và nhắm mục tiêu giữ các luồng trên cùng một hàng đợi chạy. Điều này có nghĩa là các luồng có nhiều khả năng sẽ tiếp tục chạy trên cùng các CPU nơi mà các bộ nhớ đệm CPU đã đệm sẵn dữ liệu của chúng. Các bộ nhớ đệm này được mô tả là độ ấm bộ nhớ đệm (cache warmth), và chiến lược này để giữ cho các luồng chạy trên cùng các CPU được gọi là ái lực CPU (CPU affinity). Trên các hệ thống NUMA, các hàng đợi chạy trên mỗi CPU (per-CPU run queues) cũng cải thiện tính cục bộ của bộ nhớ (memory locality). Điều này cải thiện hiệu năng bằng cách giữ cho các luồng chạy trên cùng một node bộ nhớ (được mô tả trong Chương 7, Bộ nhớ), và tránh chi phí đồng bộ hóa luồng (khóa mutex) đối với các phép toán trên hàng đợi, vốn có thể làm giảm khả năng mở rộng (scalability) nếu hàng đợi chạy là toàn cục và chia sẻ chung giữa mọi CPU.


## 6.3 Khái niệm (Concepts)

Sau đây là một số khái niệm quan trọng liên quan đến hiệu năng CPU, bắt đầu bằng tóm tắt về cơ cấu bên trong vi xử lý: tốc độ đồng hồ CPU và cách các lệnh được thực thi. Đây là nền tảng cho phân tích hiệu năng sau này, đặc biệt để hiểu chỉ số instructions-per-cycle (IPC — số lệnh trên mỗi chu kỳ).

### 6.3.1 Tốc độ Đồng hồ (Clock Rate)

Đồng hồ là một tín hiệu số điều khiển tất cả logic vi xử lý. Mỗi lệnh CPU có thể mất một hoặc nhiều chu kỳ đồng hồ (gọi là chu kỳ CPU — CPU cycles) để thực thi. CPU thực thi theo tốc độ đồng hồ nhất định; ví dụ, CPU 4 GHz thực hiện 4 tỷ chu kỳ đồng hồ mỗi giây.

Một số vi xử lý có thể thay đổi tốc độ đồng hồ của chúng, tăng lên để cải thiện hiệu năng hoặc giảm xuống để giảm tiêu thụ điện. Tốc độ có thể được thay đổi theo yêu cầu của hệ điều hành, hoặc tự động bởi chính vi xử lý. Ví dụ, luồng nhàn rỗi của nhân (kernel idle thread) có thể yêu cầu CPU giảm tốc để tiết kiệm điện.

Tốc độ đồng hồ thường được quảng cáo là tính năng chính của vi xử lý, nhưng điều này có thể hơi gây hiểu lầm. Ngay cả khi CPU trong hệ thống của bạn có vẻ được sử dụng đầy đủ (là điểm nghẽn cổ chai), tốc độ đồng hồ nhanh hơn có thể không tăng tốc hiệu năng — nó phụ thuộc vào những chu kỳ CPU nhanh đó thực sự đang làm gì. Nếu chúng chủ yếu là các chu kỳ đình trệ (stall cycles) trong khi chờ truy cập bộ nhớ, việc thực thi chúng nhanh hơn không thực sự tăng tốc độ lệnh CPU hay thông lượng khối lượng công việc.

### 6.3.2 Các Lệnh (Instructions)

CPU thực thi các lệnh được chọn từ tập lệnh của chúng. Một lệnh bao gồm các bước sau, mỗi bước được xử lý bởi một thành phần của CPU gọi là đơn vị chức năng (functional unit):

1. Nạp lệnh (Instruction fetch)
2. Giải mã lệnh (Instruction decode)
3. Thực thi (Execute)
4. Truy cập bộ nhớ (Memory access)
5. Ghi lại thanh ghi (Register write-back)

Hai bước cuối là tùy chọn, tùy thuộc vào lệnh. Nhiều lệnh chỉ hoạt động trên các thanh ghi và không yêu cầu bước truy cập bộ nhớ.

Mỗi bước này mất ít nhất một chu kỳ đồng hồ để thực thi. Truy cập bộ nhớ thường là bước chậm nhất, vì nó có thể mất hàng chục chu kỳ đồng hồ để đọc hoặc ghi vào bộ nhớ chính, trong suốt thời gian đó việc thực thi lệnh đã bị đình trệ (và các chu kỳ trong khi bị đình trệ được gọi là stall cycles). Đây là lý do tại sao bộ nhớ đệm CPU (CPU caching) quan trọng, như được mô tả trong Mục 6.4.1, Phần cứng: nó có thể làm giảm đáng kể số chu kỳ cần thiết cho truy cập bộ nhớ.

### 6.3.3 Pipeline Lệnh (Instruction Pipeline)

Pipeline lệnh (instruction pipeline) là kiến trúc CPU có thể thực thi nhiều lệnh song song bằng cách thực thi các thành phần khác nhau của các lệnh khác nhau cùng một lúc. Nó tương tự như một dây chuyền lắp ráp nhà máy, nơi các giai đoạn sản xuất có thể được thực thi song song, tăng thông lượng.

Trong trường hợp pipeline bị đình trệ ở một bước, các bộ vi xử lý hiện đại có thể thực hiện thực thi không theo thứ tự (out-of-order execution), nơi các lệnh sau có thể hoàn thành trong khi các lệnh trước đó bị đình trệ.

Các bước lệnh trong pipeline có thể được chia nhỏ thành các thao tác đơn giản hơn gọi là micro-operations (uOps) để thực thi bởi một vùng của vi xử lý gọi là back-end. Front-end của vi xử lý như vậy chịu trách nhiệm nạp lệnh và dự đoán nhánh.

**Dự đoán Nhánh (Branch Prediction)**

Các lệnh rẽ nhánh có điều kiện (conditional branch instructions) đặt ra vấn đề cho pipeline. Để tối ưu hóa, các vi xử lý thường triển khai dự đoán nhánh (branch prediction), nơi chúng sẽ đoán kết quả của bài kiểm tra và bắt đầu xử lý các lệnh kết quả. Nếu dự đoán sau đó chứng minh là sai, tiến trình trong pipeline lệnh phải bị loại bỏ, ảnh hưởng đến hiệu năng. Để cải thiện cơ hội đoán đúng, các lập trình viên có thể đặt gợi ý trong mã (ví dụ: macro `likely()` và `unlikely()` trong các nguồn nhân Linux).

### 6.3.4 Độ rộng Lệnh (Instruction Width)

Nhiều đơn vị chức năng cùng loại có thể được đưa vào, để thậm chí nhiều lệnh hơn có thể tiến triển with mỗi chu kỳ đồng hồ. Kiến trúc CPU này được gọi là superscalar và thường được sử dụng với pipeline để đạt được thông lượng lệnh cao.

Độ rộng lệnh (instruction width) mô tả số lệnh mục tiêu cần xử lý song song. Các vi xử lý hiện đại có độ rộng 3 hoặc 4, có nghĩa là chúng có thể hoàn thành tới ba hoặc bốn lệnh mỗi chu kỳ.

### 6.3.5 Kích thước Lệnh (Instruction Size)

Một đặc điểm lệnh khác là kích thước lệnh: đối với một số kiến trúc vi xử lý, nó là biến đổi. Ví dụ, x86, được phân loại là máy tính tập lệnh phức tạp (CISC — complex instruction set computer), cho phép các lệnh tối đa 15 byte. ARM, là máy tính tập lệnh rút gọn (RISC — reduced instruction set computer), có các lệnh 4 byte với căn chỉnh 4 byte cho AArch32/A32, và lệnh 2- hoặc 4 byte cho ARM Thumb.

### 6.3.6 SMT (Simultaneous Multithreading — Đa luồng Đồng thời)

Đa luồng đồng thời (SMT) sử dụng kiến trúc superscalar và hỗ trợ đa luồng phần cứng (bởi vi xử lý) để cải thiện tính song song. Nó cho phép một lõi CPU chạy nhiều hơn một luồng, lập lịch một cách hiệu quả giữa chúng trong các lệnh, ví dụ khi một lệnh bị đình trệ trên I/O bộ nhớ.

Một ví dụ triển khai là Công nghệ Hyper-Threading của Intel, nơi mỗi lõi thường có hai luồng phần cứng. Một ví dụ khác là POWER8, có tám luồng phần cứng trên mỗi lõi.

Hiệu năng của mỗi luồng phần cứng không giống như một lõi CPU riêng biệt, và phụ thuộc vào khối lượng công việc. Để tránh các vấn đề hiệu năng, các nhân có thể phân tán tải CPU trên các lõi để chỉ một luồng phần cứng trên mỗi lõi bận rộn, tránh tranh chấp luồng phần cứng.

### 6.3.7 IPC, CPI

Số lệnh trên mỗi chu kỳ (IPC — Instructions per cycle) là một chỉ số cấp cao quan trọng để mô tả cách một CPU đang dành các chu kỳ đồng hồ và để hiểu bản chất của mức sử dụng CPU. Chỉ số này cũng có thể được biểu thị là chu kỳ trên mỗi lệnh (CPI — cycles per instruction), nghịch đảo của IPC.

IPC thấp cho thấy các CPU thường bị đình trệ, thường là vì truy cập bộ nhớ. IPC cao cho thấy các CPU thường không bị đình trệ và có thông lượng lệnh cao.

- Các khối lượng công việc yêu cầu nhiều bộ nhớ có thể được cải thiện bằng cách cài đặt bộ nhớ nhanh hơn (DRAM), cải thiện tính cục bộ bộ nhớ (cấu hình phần mềm), hoặc giảm lượng I/O bộ nhớ.
- Ví dụ, tại Netflix, khối lượng công việc đám mây dao động từ IPC 0.2 (được coi là chậm) đến 1.5 (được coi là tốt). Biểu thị theo CPI, phạm vi này là 5.0 đến 0.66.

Cần lưu ý rằng IPC cho thấy hiệu quả của việc xử lý lệnh, nhưng không phải của các lệnh đó. Một thay đổi phần mềm thêm vòng lặp phần mềm kém hiệu quả, hoạt động chủ yếu trên các thanh ghi CPU (không có stall cycles): sự thay đổi như vậy có thể dẫn đến IPC tổng thể cao hơn, nhưng cũng sử dụng và mức sử dụng CPU cao hơn.

### 6.3.8 Mức sử dụng (Utilization)

Mức sử dụng CPU (CPU utilization) được đo bằng thời gian một CPU đang bận rộn thực hiện công việc trong một khoảng thời gian, được biểu thị dưới dạng phần trăm. Nó có thể được đo bằng thời gian CPU không chạy luồng nhàn rỗi của nhân mà thay vào đó chạy các luồng ứng dụng cấp người dùng hoặc các luồng nhân khác, hoặc xử lý các ngắt.

Mức sử dụng CPU cao không nhất thiết là vấn đề, mà có thể là dấu hiệu cho thấy hệ thống đang thực hiện công việc. Một số người cũng coi đây là chỉ số hoàn vốn đầu tư (ROI): hệ thống được sử dụng cao được coi là có ROI tốt. Không giống như các loại tài nguyên khác (đĩa), hiệu năng không giảm mạnh dưới mức sử dụng cao, vì nhân hỗ trợ các ưu tiên, chiếm quyền ưu tiên (preemption), và chia sẻ thời gian.

Phép đo mức sử dụng CPU bao gồm tất cả các chu kỳ đồng hồ cho các hoạt động đủ điều kiện, bao gồm cả stall cycles bộ nhớ. Điều này có thể gây hiểu lầm: một CPU có thể được sử dụng ở mức cao vì nó thường bị đình trệ chờ I/O bộ nhớ, không chỉ thực thi lệnh.

### 6.3.9 Thời gian User/Kernel (User Time/Kernel Time)

Thời gian CPU được dành để thực thi phần mềm cấp người dùng được gọi là thời gian user (user time), và phần mềm cấp nhân là thời gian kernel (kernel time). Thời gian kernel bao gồm thời gian trong các lời gọi hệ thống, luồng nhân, và ngắt. Khi được đo trên toàn hệ thống, tỷ lệ user time/kernel time cho thấy loại khối lượng công việc được thực hiện.

- Các ứng dụng có cường độ tính toán cao có thể dành gần như toàn bộ thời gian của chúng để thực thi mã cấp người dùng và có tỷ lệ user/kernel tiếp cận 99/1. Ví dụ bao gồm xử lý hình ảnh, học máy, bộ gen học, và phân tích dữ liệu.
- Các ứng dụng có cường độ I/O cao có tốc độ lời gọi hệ thống cao, thực thi mã nhân để thực hiện I/O. Ví dụ, một máy chủ web thực hiện I/O mạng có thể có tỷ lệ user/kernel khoảng 70/30.

### 6.3.10 Bão hòa (Saturation)

Một CPU ở 100% mức sử dụng là bão hòa, và các luồng sẽ gặp phải độ trễ bộ lập lịch khi chúng chờ để chạy trên CPU, làm giảm hiệu năng tổng thể. Độ trễ này là thời gian chờ đợi trên hàng đợi chạy CPU hoặc cấu trúc khác được sử dụng để quản lý các luồng.

Một hình thức bão hòa CPU khác liên quan đến các kiểm soát tài nguyên CPU, có thể được áp đặt trong môi trường điện toán đám mây đa người thuê (multi-tenant). Mặc dù CPU có thể không sử dụng 100%, giới hạn được áp đặt đã đạt đến và các luồng có thể chạy phải chờ đến lượt của chúng. Xem Chương 11, Điện toán Đám mây.

CPU chạy ở bão hòa ít gây vấn đề hơn so với các loại tài nguyên khác, vì công việc có ưu tiên cao hơn có thể chiếm quyền ưu tiên luồng hiện tại.

### 6.3.11 Chiếm quyền ưu tiên (Preemption)

Chiếm quyền ưu tiên (Preemption), được giới thiệu trong Chương 3, Hệ điều hành, cho phép một luồng có ưu tiên cao hơn chiếm quyền ưu tiên luồng đang chạy hiện tại và bắt đầu thực thi của chính nó thay thế. Điều này loại bỏ độ trễ hàng đợi chạy cho công việc có ưu tiên cao hơn, cải thiện hiệu năng của nó.

### 6.3.12 Đảo ngược Ưu tiên (Priority Inversion)

Đảo ngược ưu tiên xảy ra khi một luồng có ưu tiên thấp hơn giữ một tài nguyên và chặn một luồng có ưu tiên cao hơn không thể chạy. Điều này làm giảm hiệu năng của công việc có ưu tiên cao hơn, vì nó bị chặn chờ đợi.

Điều này có thể được giải quyết bằng cách sử dụng cơ chế kế thừa ưu tiên (priority inheritance). Đây là một ví dụ về cách thức hoạt động (dựa trên trường hợp thực tế):

1. Luồng A thực hiện giám sát và có ưu tiên thấp. Nó lấy khóa không gian địa chỉ cho cơ sở dữ liệu sản xuất, để kiểm tra sử dụng bộ nhớ.
2. Luồng B, một tác vụ thường lệ để nén nhật ký hệ thống, bắt đầu chạy.
3. Không đủ CPU để chạy cả hai. Luồng B chiếm quyền ưu tiên A và chạy.
4. Luồng C từ cơ sở dữ liệu sản xuất, có ưu tiên cao và đã đang ngủ chờ I/O. I/O này giờ hoàn thành, đưa luồng C trở lại trạng thái có thể chạy.
5. Luồng C chiếm quyền ưu tiên B, chạy, nhưng sau đó bị chặn trên khóa không gian địa chỉ mà luồng A đang giữ. Luồng C rời CPU.
6. Bộ lập lịch chọn luồng có ưu tiên cao tiếp theo để chạy: B.
7. Với luồng B đang chạy, luồng có ưu tiên cao, C, thực sự bị chặn trên luồng có ưu tiên thấp hơn, B. Đây là đảo ngược ưu tiên.
8. Kế thừa ưu tiên cấp cho luồng A ưu tiên cao của luồng C, chiếm quyền ưu tiên B, cho đến khi nó giải phóng khóa. Luồng C giờ có thể chạy.

Linux kể từ 2.6.18 đã cung cấp một mutex cấp người dùng hỗ trợ kế thừa ưu tiên, được thiết kế cho các khối lượng công việc thời gian thực [Corbet 06a].

### 6.3.13 Đa tiến trình, Đa luồng (Multiprocess, Multithreading)

Hầu hết các vi xử lý cung cấp nhiều CPU ở một số hình thức. Để một ứng dụng sử dụng chúng, nó cần các luồng thực thi riêng biệt để có thể chạy song song. Ví dụ, đối với hệ thống 64 CPU, điều này có thể có nghĩa là một ứng dụng có thể thực thi nhanh hơn tới 64 lần nếu nó có thể sử dụng tất cả các CPU song song, hoặc xử lý 64 lần tải. Mức độ mà ứng dụng có thể mở rộng hiệu quả với việc tăng số lượng CPU là một thước đo khả năng mở rộng (scalability).

Hai kỹ thuật để mở rộng ứng dụng trên các CPU là đa tiến trình (multiprocess) và đa luồng (multithreading), được minh họa trong Hình 6.4 (điều này là đa luồng phần mềm, không phải SMT dựa trên phần cứng được đề cập trước đó).

*Hình 6.4: Các kỹ thuật khả năng mở rộng CPU phần mềm*

Trên Linux cả mô hình đa tiến trình và đa luồng có thể được sử dụng, và cả hai đều được triển khai bởi các tác vụ (tasks).

**Bảng 6.1: Thuộc tính đa tiến trình và đa luồng**

| Thuộc tính | Đa tiến trình | Đa luồng |
|---|---|---|
| Phát triển | Có thể dễ hơn. Sử dụng fork(2) hoặc clone(2). | Sử dụng threads API (pthreads). |
| Chi phí bộ nhớ | Không gian địa chỉ riêng biệt cho mỗi tiến trình tiêu thụ một số tài nguyên bộ nhớ (giảm một phần bởi copy-on-write cấp trang). | Nhỏ. Chỉ yêu cầu thêm không gian ngăn xếp và thanh ghi, và không gian cho dữ liệu cục bộ luồng. |
| Chi phí CPU | Chi phí của fork(2)/clone(2)/exit(2), bao gồm công việc MMU để quản lý không gian địa chỉ. | Nhỏ. Các lời gọi API. |
| Giao tiếp | Qua IPC. Điều này phát sinh chi phí CPU bao gồm chuyển ngữ cảnh để di chuyển dữ liệu giữa các không gian địa chỉ, trừ khi các vùng bộ nhớ chia sẻ được sử dụng. | Nhanh nhất. Truy cập trực tiếp vào bộ nhớ chia sẻ. Toàn vẹn qua các nguyên thủy đồng bộ hóa (ví dụ: khóa mutex). |
| Khả năng chịu lỗi | Cao, các tiến trình độc lập. | Thấp, bất kỳ lỗi nào cũng có thể làm sập toàn bộ ứng dụng. |
| Sử dụng bộ nhớ | Mặc dù một số bộ nhớ có thể bị sao chép, các tiến trình riêng biệt có thể exit(2) và trả lại tất cả bộ nhớ về hệ thống. | Qua bộ phân bổ hệ thống. Điều này có thể gây ra một số tranh chấp CPU từ nhiều luồng và phân mảnh trước khi bộ nhớ được tái sử dụng. |

Với tất cả các ưu điểm được hiển thị trong bảng, đa luồng nói chung được coi là vượt trội hơn, mặc dù phức tạp hơn để nhà phát triển triển khai.

Dù kỹ thuật nào được sử dụng, điều quan trọng là phải tạo đủ tiến trình hoặc luồng để bao phủ số lượng CPU mong muốn — để đạt hiệu năng tối đa, có thể là tất cả CPU có sẵn. Một số ứng dụng có thể hoạt động tốt hơn khi chạy trên ít CPU hơn, khi chi phí đồng bộ hóa luồng và giảm tính cục bộ bộ nhớ (NUMA) vượt qua lợi ích của việc chạy trên nhiều CPU hơn.

### 6.3.14 Kích thước từ (Word Size)

Các vi xử lý được thiết kế xung quanh kích thước từ tối đa — 32-bit hoặc 64-bit — đây là kích thước số nguyên và kích thước thanh ghi. Kích thước từ cũng thường được sử dụng, tùy thuộc vào vi xử lý, cho kích thước không gian địa chỉ và chiều rộng đường dẫn dữ liệu.

Kích thước lớn hơn có thể có nghĩa là hiệu năng tốt hơn, mặc dù không đơn giản như vẻ ngoài. Đối với kiến trúc x86 64-bit, các chi phí này được bù đắp bằng sự tăng thanh ghi và quy ước gọi thanh ghi hiệu quả hơn, vì vậy các ứng dụng 64-bit có thể sẽ nhanh hơn phiên bản 32-bit của chúng.

### 6.3.15 Tối ưu hóa trình biên dịch (Compiler Optimization)

Thời gian chạy CPU của các ứng dụng có thể được cải thiện đáng kể thông qua các tùy chọn trình biên dịch (bao gồm đặt kích thước từ) và các tối ưu hóa. Các trình biên dịch cũng thường xuyên được cập nhật để tận dụng các tập lệnh CPU mới nhất và triển khai các tối ưu hóa khác. Đôi khi hiệu năng ứng dụng có thể được cải thiện đáng kể chỉ đơn giản bằng cách sử dụng trình biên dịch mới hơn.

Chủ đề này được đề cập chi tiết hơn trong Chương 5, Ứng dụng, Mục 5.3.1, Ngôn ngữ Biên dịch.


## 6.4 Kiến trúc (Architecture)

Phần này giới thiệu kiến trúc và triển khai CPU, cho cả phần cứng và phần mềm. Các mô hình CPU đơn giản đã được giới thiệu trong Mục 6.2, Các Mô hình, và các khái niệm chung trong phần trước.

### 6.4.1 Phần cứng (Hardware)

Phần cứng CPU bao gồm vi xử lý và các hệ thống phụ của nó, và kết nối liên thông CPU (CPU interconnect) cho các hệ thống đa vi xử lý.

**Vi xử lý (Processor)**

Các thành phần của một vi xử lý hai lõi chung được hiển thị trong Hình 6.5.

*Hình 6.5: Các thành phần vi xử lý hai lõi chung*

Đơn vị điều khiển (control unit) là trung tâm của CPU, thực hiện nạp lệnh, giải mã, quản lý thực thi và lưu trữ kết quả.

Ví dụ này mô tả một đơn vị dấu phẩy động (floating-point unit) chia sẻ và bộ nhớ đệm Level 3 tùy chọn chia sẻ. Các thành phần khác liên quan đến hiệu năng có thể có bao gồm:
- **P-cache**: Bộ nhớ đệm prefetch (mỗi lõi CPU)
- **W-cache**: Bộ nhớ đệm ghi (mỗi lõi CPU)
- **Clock**: Bộ tạo tín hiệu cho đồng hồ CPU
- **Timestamp counter**: Cho thời gian độ phân giải cao
- **Microcode ROM**: Nhanh chóng chuyển đổi lệnh thành tín hiệu mạch
- **Temperature sensors**: Để giám sát nhiệt
- **Network interfaces**: Nếu có trên-chip

**P-States và C-States**

Tiêu chuẩn giao diện cấu hình và nguồn nâng cao (ACPI — Advanced Configuration and Power Interface), được sử dụng bởi các vi xử lý Intel, định nghĩa các trạng thái hiệu năng vi xử lý (P-states) và các trạng thái nguồn vi xử lý (C-states).

P-states cung cấp các mức hiệu năng khác nhau trong quá trình thực thi bình thường bằng cách thay đổi tần số CPU: P0 là tần số cao nhất và P1...N là các trạng thái tần số thấp hơn.

C-states cung cấp các trạng thái nhàn rỗi khác nhau khi thực thi bị tạm dừng, tiết kiệm điện:
- **C0**: Thực thi. CPU hoàn toàn hoạt động.
- **C1**: Tạm dừng thực thi bằng lệnh `hlt`. Bộ nhớ đệm được duy trì. Độ trễ đánh thức thấp nhất.
- **C1E**: Tạm dừng nâng cao với tiêu thụ điện thấp hơn.
- **C2**: Tạm dừng thực thi. Trạng thái ngủ sâu hơn.
- **C3**: Trạng thái ngủ sâu hơn với tiết kiệm điện được cải thiện.

**Bộ nhớ đệm CPU (CPU Caches)**

Có nhiều cấp bộ nhớ đệm phần cứng được bao gồm trong vi xử lý (on-chip) hoặc nằm cùng vi xử lý (external). Chúng bao gồm:
- Bộ nhớ đệm lệnh Level 1 (I$)
- Bộ nhớ đệm dữ liệu Level 1 (D$)
- Translation lookaside buffer (TLB)
- Bộ nhớ đệm Level 2 (E$)
- Bộ nhớ đệm Level 3 (tùy chọn)

Intel sử dụng thuật ngữ last-level cache (LLC — bộ nhớ đệm mức cuối) để chỉ bộ nhớ đệm cuối cùng trước bộ nhớ chính.

**Độ trễ (Latency)**

Thời gian truy cập cho bộ nhớ đệm Level 1 là thường vài chu kỳ đồng hồ CPU, và cho Level 2 khoảng một chục chu kỳ. Truy cập bộ nhớ chính có thể mất khoảng 60 ns (khoảng 240 chu kỳ cho bộ vi xử lý 4 GHz).

**Liên kết (Associativity)**

Liên kết là đặc điểm bộ nhớ đệm mô tả một ràng buộc để định vị các mục mới trong bộ nhớ đệm:
- **Fully associative**: Bộ nhớ đệm có thể định vị mục mới ở bất kỳ đâu.
- **Direct mapped**: Mỗi mục chỉ có một vị trí hợp lệ trong bộ nhớ đệm.
- **Set associative**: Một tập con của bộ nhớ đệm được xác định bằng ánh xạ, trong đó một thuật toán khác có thể được thực hiện.

**Cache Line**

Cache line là một phạm vi byte được lưu trữ và truyền như một đơn vị, cải thiện thông lượng bộ nhớ. Kích thước cache line điển hình cho các vi xử lý x86 là 64 byte.

**Tính nhất quán bộ nhớ đệm (Cache Coherency)**

Bộ nhớ có thể được đệm trong nhiều bộ nhớ đệm CPU trên các vi xử lý khác nhau cùng một lúc. Khi một CPU sửa đổi bộ nhớ, tất cả các bộ nhớ đệm cần biết rằng bản sao đệm của chúng hiện đã cũ và nên bị loại bỏ. Quá trình này, gọi là tính nhất quán bộ nhớ đệm (cache coherency), đảm bảo rằng các CPU luôn truy cập trạng thái bộ nhớ đúng.

**MMU**

Đơn vị quản lý bộ nhớ (MMU — Memory management unit) chịu trách nhiệm chuyển đổi địa chỉ ảo sang địa chỉ vật lý. MMU sử dụng TLB on-chip để đệm các chuyển đổi địa chỉ. Cache miss được thỏa mãn bởi các bảng chuyển đổi trong bộ nhớ chính (DRAM), gọi là page tables.

**Kết nối liên thông (Interconnects)**

Đối với các kiến trúc đa vi xử lý, các vi xử lý được kết nối bằng một bus hệ thống chia sẻ hoặc kết nối liên thông chuyên dụng. Các ví dụ về kết nối liên thông bao gồm Intel's Quick Path Interconnect (QPI), Intel's Ultra Path Interconnect (UPI), AMD's HyperTransport (HT), và IBM's Coherent Accelerator Processor Interface (CAPI).

### 6.4.2 Phần mềm (Software)

Phần mềm nhân để hỗ trợ CPU bao gồm bộ lập lịch, các lớp lập lịch, và luồng nhàn rỗi.

**Bộ lập lịch (Scheduler)**

Các chức năng chính của bộ lập lịch CPU nhân là:
- **Chia sẻ thời gian (Time sharing)**: Đa nhiệm giữa các luồng có thể chạy, thực thi những luồng có ưu tiên cao nhất trước.
- **Chiếm quyền ưu tiên (Preemption)**: Đối với các luồng đã trở nên có thể chạy ở mức độ ưu tiên cao, bộ lập lịch có thể chiếm quyền ưu tiên luồng đang chạy hiện tại.
- **Cân bằng tải (Load balancing)**: Di chuyển các luồng có thể chạy đến các hàng đợi chạy của các CPU nhàn rỗi hoặc ít bận hơn.

Trong Linux, chia sẻ thời gian được điều khiển bởi ngắt hẹn giờ hệ thống bằng cách gọi `scheduler_tick()`. Bộ lập lịch Linux cũng sử dụng logic để tránh di chuyển khi chi phí dự kiến vượt qua lợi ích, ưu tiên giữ các luồng bận chạy trên cùng một CPU nơi bộ nhớ đệm CPU vẫn còn ấm (CPU affinity).

**Các lớp lập lịch (Scheduling Classes)**

Các lớp lập lịch quản lý hành vi của các luồng có thể chạy, cụ thể là ưu tiên của chúng, liệu thời gian trên CPU có bị chia lát thời gian (time-sliced) hay không, và thời gian của các lát thời gian đó.

Đối với nhân Linux, các lớp lập lịch là:
- **RT**: Cung cấp các ưu tiên cố định và cao cho khối lượng công việc thời gian thực. Phạm vi ưu tiên là 0–99.
- **O(1)**: Bộ lập lịch O(1) được giới thiệu trong Linux 2.6 như bộ lập lịch chia sẻ thời gian mặc định cho các tiến trình người dùng.
- **CFS**: Lập lịch hoàn toàn công bằng (Completely Fair Scheduling) được thêm vào nhân Linux 2.6.23 như bộ lập lịch chia sẻ thời gian mặc định. CFS quản lý các tác vụ trên cây đỏ-đen (red-black tree), cho phép những người tiêu thụ CPU thấp dễ dàng được tìm thấy và thực thi.
- **Idle**: Chạy các luồng với ưu tiên thấp nhất có thể.
- **Deadline**: Được thêm vào Linux 3.14, áp dụng lập lịch earliest deadline first (EDF).

Các chính sách lập lịch (scheduling policies):
- **SCHED_RR**: Lập lịch vòng tròn (round-robin). Sau khi một luồng đã sử dụng hết thời gian lượng tử của nó, nó được chuyển đến cuối hàng đợi chạy. Sử dụng lớp RT.
- **SCHED_FIFO**: Lập lịch vào trước ra trước (first-in, first-out). Tiếp tục chạy luồng ở đầu hàng đợi cho đến khi nó tự nguyện rời hoặc một luồng ưu tiên cao hơn đến. Sử dụng lớp RT.
- **SCHED_NORMAL**: Lập lịch chia sẻ thời gian và là mặc định cho các tiến trình người dùng. Sử dụng lớp CFS.
- **SCHED_BATCH**: Tương tự SCHED_NORMAL nhưng không được lập lịch để ngắt công việc I/O-bound tương tác khác. Sử dụng lớp CFS.
- **SCHED_IDLE**: Sử dụng lớp Idle.
- **SCHED_DEADLINE**: Sử dụng lớp Deadline.

**Luồng nhàn rỗi (Idle Thread)**

Luồng "nhàn rỗi" của nhân chạy trên CPU khi không có luồng nào khác có thể chạy và có ưu tiên thấp nhất có thể. Nó thường được lập trình để thông báo cho vi xử lý rằng thực thi CPU có thể bị tạm dừng (lệnh halt) hoặc giảm tốc để tiết kiệm điện.

**Nhóm NUMA (NUMA Grouping)**

Hiệu năng trên các hệ thống NUMA có thể được cải thiện đáng kể bằng cách làm cho nhân nhận thức được NUMA, để nó có thể đưa ra các quyết định lập lịch và đặt bộ nhớ tốt hơn. Trên Linux, chúng được gọi là miền lập lịch (scheduling domains).


## 6.5 Phương pháp luận (Methodology)

Phần này mô tả các phương pháp luận và bài tập khác nhau cho phân tích và tinh chỉnh CPU.

**Bảng 6.7: Phương pháp luận hiệu năng CPU**

| Mục | Phương pháp | Loại |
|-----|------------|-------|
| 6.5.1 | Phương pháp Công cụ (Tools method) | Phân tích quan sát |
| 6.5.2 | Phương pháp USE | Phân tích quan sát |
| 6.5.3 | Đặc trưng hóa khối lượng công việc | Phân tích quan sát, lập kế hoạch năng lực |
| 6.5.4 | Lập hồ sơ (Profiling) | Phân tích quan sát |
| 6.5.5 | Phân tích chu kỳ (Cycle analysis) | Phân tích quan sát |
| 6.5.6 | Giám sát hiệu năng | Phân tích quan sát, lập kế hoạch năng lực |
| 6.5.7 | Tinh chỉnh hiệu năng tĩnh | Phân tích quan sát, lập kế hoạch năng lực |
| 6.5.8 | Tinh chỉnh ưu tiên | Tinh chỉnh |
| 6.5.9 | Kiểm soát tài nguyên | Tinh chỉnh |
| 6.5.10 | Ràng buộc CPU (CPU binding) | Tinh chỉnh |
| 6.5.11 | Micro-benchmarking | Phân tích thực nghiệm |

Đề xuất của tôi là sử dụng các phương pháp sau, theo thứ tự này: giám sát hiệu năng, phương pháp USE, lập hồ sơ, micro-benchmarking, và tinh chỉnh hiệu năng tĩnh.

### 6.5.1 Phương pháp Công cụ (Tools Method)

Phương pháp công cụ là quá trình lặp đi lặp lại thông qua các công cụ có sẵn, kiểm tra các chỉ số chính mà chúng cung cấp.

Đối với CPU, phương pháp công cụ có thể bao gồm:
- **uptime/top**: Kiểm tra mức tải trung bình để xem tải có tăng hay giảm theo thời gian không.
- **vmstat**: Chạy vmstat(1) với khoảng cách một giây và kiểm tra mức sử dụng CPU toàn hệ thống ("us" + "sy").
- **mpstat**: Kiểm tra thống kê trên mỗi CPU và tìm các CPU riêng lẻ nóng (bận), xác định vấn đề khả năng mở rộng của luồng.
- **top**: Xem tiến trình và người dùng nào là người tiêu thụ CPU hàng đầu.
- **pidstat**: Phân tích người tiêu thụ CPU hàng đầu thành user-time và system-time.
- **perf/profile**: Lập hồ sơ dấu vết ngăn xếp sử dụng CPU cho cả user-time và kernel-time.
- **perf**: Đo IPC như một chỉ số về kém hiệu quả dựa trên chu kỳ.
- **showboost/turboboost**: Kiểm tra tốc độ đồng hồ CPU hiện tại.
- **dmesg**: Kiểm tra các thông báo đình trệ nhiệt độ CPU ("cpu clock throttled").

### 6.5.2 Phương pháp USE (USE Method)

Phương pháp USE có thể được sử dụng để xác định các điểm nghẽn và lỗi trên tất cả các thành phần sớm trong điều tra hiệu năng.

Đối với mỗi CPU, kiểm tra:
- **Mức sử dụng (Utilization)**: Thời gian CPU bận rộn (không ở trong luồng nhàn rỗi)
- **Bão hòa (Saturation)**: Mức độ các luồng có thể chạy đang xếp hàng chờ đến lượt trên CPU
- **Lỗi (Errors)**: Lỗi CPU, bao gồm cả lỗi có thể sửa được

Đối với các môi trường triển khai giới hạn CPU hoặc hạn mức (kiểm soát tài nguyên), chẳng hạn như môi trường điện toán đám mây, mức sử dụng CPU nên được đo so với giới hạn được áp đặt.

### 6.5.3 Đặc trưng hóa Khối lượng Công việc (Workload Characterization)

Đặc trưng hóa tải được áp dụng là quan trọng trong lập kế hoạch năng lực, đo điểm chuẩn, và mô phỏng khối lượng công việc. Nó cũng có thể dẫn đến một số cải thiện hiệu năng lớn nhất bằng cách xác định công việc không cần thiết có thể được loại bỏ.

Các thuộc tính cơ bản để đặc trưng hóa khối lượng công việc CPU:
- Mức tải trung bình CPU (mức sử dụng + bão hòa)
- Tỷ lệ user-time đến system-time
- Tốc độ syscall
- Tốc độ chuyển ngữ cảnh tự nguyện
- Tốc độ ngắt

**Danh sách kiểm tra:**
- Mức sử dụng CPU toàn hệ thống là gì? Trên mỗi CPU? Trên mỗi lõi?
- Tải CPU song song như thế nào? Có phải đơn luồng không? Bao nhiêu luồng?
- Ứng dụng hoặc người dùng nào đang sử dụng các CPU? Bao nhiêu?
- Luồng nhân nào đang sử dụng các CPU? Bao nhiêu?
- Mức sử dụng CPU của các ngắt là gì?
- Mức sử dụng kết nối liên thông CPU là gì?
- Tại sao các CPU đang được sử dụng (các đường dẫn gọi ở cấp user và kernel)?
- Loại stall cycles nào đang gặp phải?

### 6.5.4 Lập hồ sơ (Profiling)

Lập hồ sơ xây dựng bức tranh về mục tiêu để nghiên cứu. Lập hồ sơ CPU có thể được thực hiện theo các cách khác nhau:
- **Lấy mẫu theo thời gian (Timer-based sampling)**: Thu thập các mẫu dựa trên hẹn giờ của hàm hiện đang chạy hoặc dấu vết ngăn xếp. Tốc độ điển hình là 99 Hertz (mẫu mỗi giây) mỗi CPU. 99 Hz được sử dụng để tránh lấy mẫu khóa bước có thể xảy ra ở 100 Hz.
- **Truy vết hàm (Function tracing)**: Thiết bị đo đạc tất cả hoặc một số lời gọi hàm để đo thời gian của chúng. Cung cấp dạng xem chi tiết nhưng trên có thể không phù hợp cho môi trường sản xuất.

**Diễn giải Hồ sơ (Profile Interpretation)**

Phương pháp của tôi để tìm cải thiện hiệu năng trong CPU flame graphs:

1. **Nhìn từ trên xuống (lá đến gốc) để tìm các "cao nguyên" lớn.** Đây cho thấy một hàm đơn đang on-CPU trong nhiều mẫu, và có thể dẫn đến một số cải thiện nhanh.
2. **Nhìn từ dưới lên để hiểu phân cấp mã.** Điều này giúp xác định liệu có thể tránh các thao tác tốn kém không.
3. **Nhìn kỹ hơn từ trên xuống để tìm mức sử dụng CPU rải rác nhưng phổ biến.** Có thể có nhiều khung nhỏ liên quan đến cùng một vấn đề, chẳng hạn như tranh chấp khóa.

### 6.5.5 Phân tích Chu kỳ (Cycle Analysis)

Bạn có thể sử dụng Bộ đếm giám sát hiệu năng (PMCs — Performance Monitoring Counters) để hiểu mức sử dụng CPU ở cấp độ chu kỳ. Điều này có thể tiết lộ rằng các chu kỳ được dành ở trạng thái đình trệ trên Level 1, 2, hoặc 3 cache miss, bộ nhớ hoặc tài nguyên I/O.

Bắt đầu phân tích chu kỳ bằng cách đo IPC:
- Nếu IPC thấp — tiếp tục điều tra các loại stall cycles.
- Nếu IPC cao — tìm cách trong mã để giảm các lệnh được thực hiện.

Các công cụ như Intel vTune và AMD uprof có thể tiết kiệm thời gian vì chúng được lập trình để tự động tìm các PMC quan trọng.

### 6.5.6 Giám sát Hiệu năng (Performance Monitoring)

Giám sát hiệu năng có thể xác định các vấn đề đang hoạt động và các mẫu hành vi theo thời gian. Các chỉ số chính cho CPU:
- **Mức sử dụng (Utilization)**: Phần trăm bận rộn
- **Bão hòa (Saturation)**: Độ dài hàng đợi chạy hoặc độ trễ bộ lập lịch

Mức sử dụng nên được giám sát trên cơ sở trên mỗi CPU để xác định các vấn đề khả năng mở rộng luồng. Các khoảng thời gian đo lường trên mỗi giây được ưu tiên hơn. Các đợt bùng phát trong vòng một giây có thể được xác định từ bão hòa và được kiểm tra bằng FlameScope.

### 6.5.7 Tinh chỉnh Hiệu năng Tĩnh (Static Performance Tuning)

Tinh chỉnh hiệu năng tĩnh tập trung vào các vấn đề của môi trường được cấu hình. Đối với hiệu năng CPU, kiểm tra:
- Có bao nhiêu CPU có sẵn để sử dụng? Chúng có phải là lõi không? Luồng phần cứng?
- Có GPU hoặc bộ tăng tốc khác có sẵn và đang sử dụng không?
- Kiến trúc CPU là đơn hay đa vi xử lý?
- Kích thước của bộ nhớ đệm CPU là gì? Chúng có được chia sẻ không?
- Tốc độ đồng hồ CPU là gì? Nó có động không (ví dụ: Intel Turbo Boost)?
- Các tính năng liên quan đến CPU khác nào được bật hoặc tắt trong BIOS?
- Có các vấn đề hiệu năng (lỗi) với mô hình vi xử lý này không?
- Phiên bản microcode là gì? Nó có bao gồm các biện pháp giảm thiểu ảnh hưởng đến hiệu năng cho các lỗ hổng bảo mật (Spectre/Meltdown) không?
- Có giới hạn sử dụng CPU do phần mềm áp đặt (kiểm soát tài nguyên) không?

### 6.5.8 Tinh chỉnh Ưu tiên (Priority Tuning)

Unix luôn cung cấp lời gọi hệ thống nice(2) để điều chỉnh ưu tiên tiến trình, đặt giá trị "niceness". Giá trị nice dương dẫn đến ưu tiên tiến trình thấp hơn, và giá trị âm dẫn đến ưu tiên cao hơn.

Giá trị nice vẫn hữu ích ngày nay để điều chỉnh ưu tiên tiến trình. Điều này hiệu quả nhất khi có sự tranh chấp cho CPU, gây ra độ trễ bộ lập lịch cho công việc có ưu tiên cao.

Ngoài nice, hệ điều hành có thể cung cấp các kiểm soát nâng cao hơn cho ưu tiên tiến trình như thay đổi lớp bộ lập lịch và chính sách bộ lập lịch. Linux bao gồm lớp lập lịch thời gian thực (real-time scheduling class). Kể từ Linux 2.6.25, RLIMIT_RTTIME có thể đặt giới hạn microsecond về thời gian CPU mà luồng thời gian thực có thể tiêu thụ.

### 6.5.9 Kiểm soát Tài nguyên (Resource Controls)

Hệ điều hành có thể cung cấp các kiểm soát chi tiết để phân bổ chu kỳ CPU cho các tiến trình hoặc nhóm tiến trình. Chúng có thể bao gồm các giới hạn cố định cho mức sử dụng CPU và các chia sẻ (shares) cho một cách tiếp cận linh hoạt hơn. Cách thức hoạt động của chúng phụ thuộc vào triển khai và được thảo luận trong Mục 6.9, Tinh chỉnh.

### 6.5.10 Ràng buộc CPU (CPU Binding)

Một cách khác để tinh chỉnh hiệu năng CPU bao gồm ràng buộc các tiến trình và luồng với các CPU riêng lẻ, hoặc tập hợp các CPU. Điều này có thể tăng độ ấm bộ nhớ đệm CPU cho tiến trình, cải thiện hiệu năng I/O bộ nhớ của nó.

Có thường hai cách thực hiện:
- **Ràng buộc CPU (CPU binding)**: Cấu hình tiến trình chỉ chạy trên một CPU đơn, hoặc chỉ trên một CPU từ một tập được định nghĩa.
- **Tập CPU độc quyền (Exclusive CPU sets)**: Phân vùng một tập CPU chỉ có thể được sử dụng bởi (các) tiến trình được gán cho chúng.

Trên các hệ thống Linux, phương pháp tập CPU độc quyền có thể được triển khai bằng cách sử dụng cpusets.

### 6.5.11 Micro-Benchmarking

Các công cụ cho CPU micro-benchmarking thường đo thời gian cần thiết để thực hiện một thao tác đơn giản nhiều lần. Thao tác có thể dựa trên:
- **Lệnh CPU**: Phép toán số nguyên, phép toán dấu phẩy động, tải và lưu bộ nhớ, nhánh và các lệnh khác
- **Truy cập bộ nhớ**: Để điều tra độ trễ của các bộ nhớ đệm CPU khác nhau và thông lượng bộ nhớ chính
- **Ngôn ngữ cấp cao**: Tương tự như kiểm tra lệnh CPU, nhưng được viết bằng ngôn ngữ diễn giải hoặc biên dịch cấp cao hơn
- **Các hoạt động hệ điều hành**: Kiểm tra các hàm thư viện hệ thống và syscall bị ràng buộc bởi CPU

Dù benchmark nào bạn sử dụng, khi so sánh kết quả giữa các hệ thống, điều quan trọng là bạn phải hiểu những gì thực sự đang được kiểm tra.


## 6.6 Công cụ Quan sát (Observability Tools)

Phần này giới thiệu các công cụ quan sát hiệu năng CPU cho các hệ điều hành dựa trên Linux. Xem phần trước để biết các phương pháp luận cần tuân theo khi sử dụng chúng.

Các công cụ trong phần này được liệt kê trong Bảng 6.8.

**Bảng 6.8: Các công cụ quan sát CPU của Linux**

| Mục | Công cụ | Mô tả |
|-----|---------|-------|
| 6.6.1 | `uptime` | Các mức tải trung bình (Load averages) |
| 6.6.2 | `vmstat` | Bao gồm các mức trung bình CPU toàn hệ thống |
| 6.6.3 | `mpstat` | Số liệu thống kê trên mỗi CPU |
| 6.6.4 | `sar` | Số liệu thống kê lịch sử |
| 6.6.5 | `ps` | Trạng thái tiến trình |
| 6.6.6 | `top` | Giám sát mức sử dụng CPU trên mỗi tiến trình/luồng |
| 6.6.7 | `pidstat` | Phân tích mức sử dụng CPU trên mỗi tiến trình/luồng |
| 6.6.8 | `time`, `ptime` | Đo thời gian chạy một lệnh, cùng với phân tích mức sử dụng CPU |
| 6.6.9 | `turboboost` | Hiển thị tốc độ đồng hồ CPU và các trạng thái khác |
| 6.6.10 | `showboost` | Hiển thị tốc độ đồng hồ CPU và turbo boost |
| 6.6.11 | `pmcarch` | Hiển thị mức sử dụng chu kỳ CPU cấp cao |
| 6.6.12 | `tlbstat` | Tóm tắt các chu kỳ TLB |
| 6.6.13 | `perf` | Lập hồ sơ CPU và phân tích PMC |
| 6.6.14 | `profile` | Lấy mẫu dấu vết ngăn xếp CPU |
| 6.6.15 | `cpudist` | Tóm tắt thời gian trên CPU (on-CPU time) |
| 6.6.16 | `runqlat` | Tóm tắt độ trễ hàng đợi chạy CPU |
| 6.6.17 | `runqlen` | Tóm tắt độ dài hàng đợi chạy CPU |
| 6.6.18 | `softirqs` | Tóm tắt thời gian ngắt mềm |
| 6.6.19 | `hardirqs` | Tóm tắt thời gian ngắt cứng |
| 6.6.20 | `bpftrace` | Các chương trình truy vết cho phân tích CPU |

Đây là bộ công cụ và khả năng chọn lọc hỗ trợ cho Mục 6.5, Phương pháp luận. Chúng ta bắt đầu với các công cụ truyền thống cho thống kê CPU, sau đó tiến tới các công cụ cho phân tích sâu hơn bằng cách sử dụng lập hồ sơ đường dẫn mã, phân tích chu kỳ CPU và công cụ truy vết. Một số công cụ truyền thống có thể có sẵn trên (và đôi khi bắt nguồn từ) các hệ điều hành giống Unix khác, bao gồm: `uptime(1)`, `vmstat(8)`, `mpstat(1)`, `sar(1)`, `ps(1)`, `top(1)`, và `time(1)`. Các công cụ truy vết dựa trên BPF và front-end BCC và bpftrace (Chương 15), bao gồm: `profile(8)`, `cpudist(8)`, `runqlat(8)`, `runqlen(8)`, `softirqs(8)`, và `hardirqs(8)`.

Xem tài liệu cho từng công cụ, bao gồm trang man (man pages) của nó, để biết tham khảo đầy đủ về các tính năng.

### 6.6.1 uptime

`uptime(1)` là một trong nhiều lệnh in ra các mức tải trung bình (load averages) của hệ thống:

```
$ uptime
 9:04pm  up 268 day(s), 10:16,  2 users,  load average: 7.76, 8.32, 8.60
```

Ba số cuối cùng là các mức tải trung bình 1, 5, và 15 phút. Bằng cách so sánh ba con số, bạn có thể xác định xem tải đang tăng, đang giảm, hay ổn định trong 15 phút qua (hoặc lâu hơn). Điều này có thể hữu ích để biết: nếu bạn đang phản hồi một vấn đề hiệu năng sản xuất và thấy rằng tải đang giảm, bạn có thể đã bỏ lỡ vấn đề; nếu tải đang tăng, vấn đề có thể đang trở nên tồi tệ hơn!

Các phần tiếp theo giải thích chi tiết hơn về các mức tải trung bình, nhưng chúng chỉ là một điểm bắt đầu, vì vậy bạn không nên dành quá năm phút để xem xét chúng trước khi chuyển sang các số liệu khác.

**Các mức Tải trung bình (Load Averages)**

Các mức tải trung bình chỉ ra nhu cầu sử dụng tài nguyên hệ thống: số càng cao nghĩa là nhu cầu càng nhiều. Trên một số hệ điều hành (ví dụ: Solaris), các mức tải trung bình cho thấy nhu cầu CPU, giống như các phiên bản đầu của Linux. Nhưng vào năm 1993, Linux đã thay đổi các mức tải trung bình để chỉ ra nhu cầu toàn hệ thống: CPU, đĩa, và các tài nguyên khác. Điều này được thực hiện bằng cách bao gồm các luồng ở trạng thái `TASK_UNINTERRUPTIBLE`, được hiển thị bởi một số công cụ dưới dạng trạng thái "D" (trạng thái này đã được nhắc đến ở Chương 5, Ứng dụng, Mục 5.4.5, Phân tích Trạng thái Luồng).

Tải được đo bằng mức độ sử dụng tài nguyên hiện tại (mức sử dụng - utilization) cộng với các yêu cầu đang đợi xếp hàng (sự bão hòa - saturation). Tưởng tượng một trạm thu phí ô tô: bạn có thể đo tải tại các thời điểm khác nhau trong ngày bằng cách đếm số ô tô đang được phục vụ (utilization) cộng với số ô tô đang xếp hàng đợi (saturation).

Mức trung bình là mức trung bình động suy giảm theo hàm mũ (exponentially damped moving average), phản ánh tải vượt ra ngoài thời điểm 1, 5, và 15 phút (các thời gian này thực tế là các hằng số được sử dụng trong tổng di chuyển hàm mũ). Hình 6.17 cho thấy kết quả của một thử nghiệm đơn giản trong đó một luồng duy nhất phụ thuộc CPU (CPU-bound) được khởi chạy và các mức tải trung bình được vẽ sơ đồ.

*Hình 6.17: Các mức tải trung bình suy giảm theo hàm mũ*

Tính đến các mốc 1, 5, và 15 phút, các mức tải trung bình đã đạt khoảng 61% của mức tải thực tế là 1.0.

Làm ví dụ hiện đại, hãy xem xét một hệ thống 64 CPU với load average là 128. Nếu tải chỉ là do CPU, thì điều đó có nghĩa là trung bình luôn có một luồng chạy trên mỗi CPU và một luồng chờ cho mỗi CPU. Cùng hệ thống đó với tải CPU là 20 sẽ cho thấy hiệu năng còn dư dả đáng kể, vì nó có thể chạy thêm 44 luồng phụ thuộc CPU nữa trước khi tất cả các CPU bận rộn. (Một số công ty giám sát một chỉ số load average được chuẩn hóa, trong đó nó được tự động chia cho số lượng CPU, cho phép diễn giải nó dễ dàng mà không cần biết số lượng CPU.)

**Thông tin Điểm nghẽn Áp lực (Pressure Stall Information - PSI)**

Giao diện thông tin điểm nghẽn áp lực (PSI) đã được thêm vào Linux 4.20 cung cấp thông tin phân tích áp lực đối với cpu, bộ nhớ và I/O. Giá trị trung bình cho thấy phần trăm thời gian mà một nội dung nào đó bị đình trệ vì đợi tài nguyên (chỉ bão hòa). Bảng 6.9 so sánh nó với các mức tải trung bình.

**Bảng 6.9: Load averages vs PSI trên Linux**

| Thuộc tính | Các mức tải trung bình (Load Averages) | Thông tin điểm nghẽn áp lực (PSI) |
|---|---|---|
| Tài nguyên | Toàn hệ thống | cpu, memory, io (từng cái riêng rẽ) |
| Số liệu | Số lượng các tác vụ bận rộn và trong hàng đợi | Phần trăm thời gian bị đình trệ (đang chờ đợi) |
| Khoảng thời gian | 1 phút, 5 phút, 15 phút | 10 giây, 60 giây, 300 giây |
| Số trung bình | Tổng trung bình động suy giảm theo hàm mũ | Tổng trung bình động suy giảm theo hàm mũ |

Bảng 6.10 cho thấy số liệu hiển thị đối với các kịch bản khác nhau:

**Bảng 6.10: Các ví dụ Load average vs PSI trên Linux**

| Kịch bản Ví dụ | Các mức Tải trung bình | PSI |
|---|---|---|
| 2 CPU, 1 luồng bận | 1.0 | 0.0 |
| 2 CPU, 2 luồng bận | 2.0 | 0.0 |
| 2 CPU, 3 luồng bận | 3.0 | 50.0 |
| 2 CPU, 4 luồng bận | 4.0 | 100.0 |
| 2 CPU, 5 luồng bận | 5.0 | 100.0 |

Ví dụ, hiển thị kịch bản 2 CPU với 3 luồng bận:

```
$ uptime
 07:51:13 up 4 days,  9:56,  2 users,  load average: 3.00, 3.00, 2.55
$ cat /proc/pressure/cpu
some avg10=50.00 avg60=50.00 avg300=49.70 total=1031438206
```

Giá trị 50.0 này có nghĩa là một luồng ("some") đã bị đình trệ 50% thời gian. Các số liệu io và memory bao gồm một dòng thứ hai cho khi tất cả các luồng không nhàn rỗi (non-idle) đã bị đình trệ ("full"). PSI trả lời tốt nhất cho câu hỏi: xác suất một tác vụ sẽ phải chờ tài nguyên là bao nhiêu?

Cho dù bạn sử dụng load averages hay PSI, bạn nên nhanh chóng chuyển sang các số đo chi tiết hơn để hiểu tải, chẳng hạn như được cung cấp bởi `vmstat(1)` và `mpstat(1)`.

### 6.6.2 vmstat

Lệnh thống kê bộ nhớ ảo (virtual memory statistics), `vmstat(8)`, in các mức trung bình CPU toàn hệ thống trong các cột cuối cùng, và số lượng các luồng có thể chạy (runnable threads) trong cột đầu tiên. Dưới đây là kết quả đầu ra ví dụ từ phiên bản Linux:

```
$ vmstat 1
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
15  0      0 451732  70588 866628    0    0     1    10   43   38  2  1 97  0  0
15  0      0 450968  70588 866628    0    0     0   612 1064 2969 72 28  0  0  0
15  0      0 450660  70588 866632    0    0     0     0  961 2932 72 28  0  0  0
15  0      0 450952  70588 866632    0    0     0     0 1015 3238 74 26  0  0  0
[...]
```

Dòng đầu ra đầu tiên được giả định là bản tóm tắt kể từ lúc khởi động. Tuy nhiên, trên Linux, các cột tiến trình (procs) và bộ nhớ bắt đầu bằng cách hiển thị trạng thái hiện tại. (Có lẽ một ngày nào đó chúng sẽ được sửa lại.) Các cột liên quan đến CPU bao gồm:

- **r**: Độ dài hàng đợi chạy (Run-queue length) — tổng số lượng luồng có thể chạy
- **us**: Phần trăm user-time (thời gian chạy mã người dùng)
- **sy**: Phần trăm system-time (thời gian nhân)
- **id**: Phần trăm nhàn rỗi (idle)
- **wa**: Phần trăm chờ I/O (wait I/O), đo lường CPU nhàn rỗi trong khi các luồng bị chặn ở I/O ổ đĩa
- **st**: Phần trăm bị lấy đi (stolen), cho các môi trường ảo hóa hiển thị thời gian CPU được dành để phục vụ các khách (tenants) khác

Tất cả các giá trị này là các mức trung bình toàn hệ thống trên tất cả các CPU, ngoại trừ cột `r`, là tổng số.

Trên Linux, cột `r` là tổng số tác vụ đang chờ công thêm những tác vụ đang chạy. Đối với các hệ điều hành khác (ví dụ: Solaris), cột `r` chỉ hiển thị các tác vụ đang chờ, không bao gồm các tác vụ đang chạy.

### 6.6.3 mpstat

Công cụ thống kê đa vi xử lý (multiprocessor statistics), `mpstat(1)`, có thể báo cáo các thống kê trên mỗi CPU. Dưới đây là kết quả đầu ra ví dụ từ phiên bản Linux:

```
$ mpstat -P ALL 1
Linux 5.3.0-1009-aws (ip-10-0-239-218)     02/01/20      _x86_64_   (2 CPU)

18:00:32     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
18:00:33     all   32.16    0.00   61.81    0.00    0.00    0.00    0.00    0.00    0.00    6.03
18:00:33       0   32.00    0.00   64.00    0.00    0.00    0.00    0.00    0.00    0.00    4.00
18:00:33       1   32.32    0.00   59.60    0.00    0.00    0.00    0.00    0.00    0.00    8.08
[...]
```

Tùy chọn `-P ALL` đã được sử dụng để in ra bản báo cáo trên mỗi CPU. Theo mặc định, `mpstat(1)` chỉ in ra dòng tóm tắt toàn hệ thống (all). Các cột là:

- **CPU**: CPU logic ID hoặc all đối với tóm tắt
- **%usr**: User-time, loại trừ %nice
- **%nice**: User-time cho các tiến trình có mức độ ưu tiên đã được "nice"
- **%sys**: System-time (nhân)
- **%iowait**: CPU chờ I/O
- **%irq**: Mức độ sử dụng CPU thông qua ngắt phần cứng (hardware interrupt)
- **%soft**: Mức độ sử dụng CPU thông qua ngắt phần mềm (software interrupt)
- **%steal**: Thời gian sử dụng để phục vụ các người thuê (tenants) ảo hóa khác
- **%guest**: Thời gian CPU phụ trách máy ảo khách (guest virtual machines)
- **%gnice**: Thời gian CPU để chạy máy ảo khách ưu tiên (niced guest)
- **%idle**: Nhàn rỗi

Các cột chính là `%usr`, `%sys` và `%idle`. Những cột này xác định mức sử dụng CPU trên mỗi CPU và hiển thị tỷ lệ thời gian user/kernel (xem Mục 6.3.9, Thời gian User/Kernel). Quá trình này cũng phân biệt ra các CPU "hot" — là các CPU chạy ở 100% tài nguyên (`%usr` + `%sys`) đang khi một vài cái khác còn dư dả — có thể do số lượng luồng quá ít trong quá trình ứng dụng làm việc cũng như là map sai device interrupt.

Lưu ý rằng thời gian CPU được ghi từ các công cụ cùng hạt nhân và thông số liệu `/proc/stat`, mức độ chính xác phụ thuộc cấu hình kernel đó (Xem "CPU Statistic Accuracy" ở Mục 4.3.1)

### 6.6.4 sar

Công cụ theo dõi hệ thống report `sar(1)` được giới thiệu trong Chương 4. Phiên bản Linux cho phép các cấu hình đo lường hiệu năng bao gồm:
- `-P ALL`: Giống như tùy chọn trong mpstat
- `-u`: Giống `mpstat(1)` định dạng in cấu trúc trung bình tóm tắt default.
- `-q`: Ghi số kích thước load vào runq-sz bao gồm các tiến trình có sẵn và pending, y hệt như load averages vậy.

`sar(1)` dùng được cho dữ liệu từ lúc trước trong lịch sử. Xem Mục 4.4, `sar` phần chi tiết thêm.

### 6.6.5 ps

Trạng thái quá trình (process status command), `ps(1)`, liệt kê thông tin cho mọi tiến trình gồm cả tỉ lệ sử dụng CPU:

```
$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0  23772  1948 ?        Ss   2012   0:04 /sbin/init
root         2  0.0  0.0      0     0 ?        S    2012   0:00 [kthreadd]
...
web      11715 11.3  0.0 632700 11540 pts/0    Sl   01:36   0:27 node indexer.js
web      11721 96.5  0.1 638116 52108 pts/1    Rl+  01:37   3:33 node proxy.js
```

Cách ghi cờ này từ hệ điều hành BSD. Để liệt kê mọi người dùng sử dụng `a`, với đầy đủ `u`, và bao gồm tiến trình chạy không trong command terminal (`x`). `TTY` đang hiển thị điều này cho thiết bị hiện tại ở cổng terminal.

Có thể áp dụng format từ SVR4 (đầu bằng `-`):

```
$ ps -ef
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 Nov13 ?        00:00:04 /sbin/init
...
```


Cột này liệt kê tất cả các tiến trình (`-e`) với đầy đủ chi tiết (`-f`). Có nhiều tùy chọn khác có sẵn cho `ps(1)` bao gồm `-o` để tùy chỉnh đầu ra và các cột được hiển thị.

Cột chính cho mức sử dụng CPU là `TIME` và `%CPU` (ví dụ trước).

Cột `TIME` hiển thị tổng thời gian CPU mà tiến trình đã tiêu thụ (user + system) kể từ khi nó được tạo, ở định dạng giờ:phút:giây.

Trên Linux, cột `%CPU` từ ví dụ đầu tiên hiển thị mức sử dụng CPU trung bình trong suốt thời gian tồn tại của tiến trình, được cộng dồn trên tất cả các CPU. Một tiến trình đơn luồng luôn phụ thuộc CPU (CPU-bound) sẽ báo cáo 100%. Một tiến trình phụ thuộc CPU có hai luồng sẽ báo cáo 200%. Các hệ điều hành khác có thể chuẩn hóa `%CPU` theo số lượng CPU để mức tối đa của nó là 100%, và chúng có thể chỉ hiển thị mức sử dụng CPU gần đây hoặc hiện tại thay vì mức trung bình trong suốt thời gian tồn tại. Trên Linux, để xem mức sử dụng CPU hiện tại của các tiến trình, bạn có thể sử dụng `top(1)`.

### 6.6.6 top

`top(1)` được tạo bởi William LeFebvre vào năm 1984 cho BSD. Ông lấy cảm hứng từ lệnh `MONITOR PROCESS/TOPCPU` của VMS, hiển thị các công việc tiêu thụ CPU hàng đầu với tỷ lệ phần trăm CPU và biểu đồ thanh (bar chart) ASCII (nhưng không có các cột dữ liệu).

Lệnh `top(1)` giám sát các tiến trình đang chạy hàng đầu, cập nhật màn hình theo các khoảng thời gian đều đặn. Ví dụ, trên Linux:

```
$ top
top - 01:38:11 up 63 days,  1:17,  2 users,  load average: 1.57, 1.81, 1.77
Tasks: 256 total,   2 running, 254 sleeping,   0 stopped,   0 zombie
Cpu(s):  2.0%us,  3.6%sy,  0.0%ni, 94.2%id,  0.0%wa,  0.0%hi,  0.2%si,  0.0%st
Mem:  49548744k total, 16746572k used, 32802172k free,    182900k buffers
Swap: 100663292k total,         0k used, 100663292k free, 14925240k cached

  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
11721 web       20   0  623m  50m 4984 R   93  0.1   0:59.50 node
11715 web       20   0  619m  20m 4916 S   25  0.0   0:07.52 node
   10 root      20   0     0    0    0 S    1  0.0 248:52.56 ksoftirqd/2
   51 root      20   0     0    0    0 S    0  0.0   0:35.66 events/0
11724 admin     20   0 19412 1444  960 R    0  0.0   0:00.07 top
    1 root      20   0 23772 1948 1296 S    0  0.0   0:04.35 init
```

Một bản tóm tắt toàn hệ thống ở trên cùng và danh sách tiến trình/tác vụ ở dưới cùng, được sắp xếp theo người tiêu thụ CPU hàng đầu theo mặc định. Bản tóm tắt toàn hệ thống bao gồm các load average và trạng thái CPU: `%us`, `%sy`, `%ni`, `%id`, `%wa`, `%hi`, `%si`, `%st`. Các trạng thái này tương đương với các trạng thái được in bởi `mpstat(1)`, như đã mô tả trước đó, và được tính trung bình trên tất cả các CPU.

Mức sử dụng CPU được hiển thị ở các cột `TIME` và `%CPU`. `TIME` là tổng thời gian CPU được tiêu thụ bởi tiến trình ở độ phân giải phần trăm giây. Ví dụ: "1:36.53" có nghĩa là tổng cộng 1 phút 36.53 giây thời gian trên CPU (on-CPU time). Một số phiên bản của `top(1)` cung cấp chế độ "thời gian tích lũy" (cumulative time) tùy chọn, bao gồm thời gian CPU từ các tiến trình con đã thoát.

Cột `%CPU` hiển thị tổng mức sử dụng CPU cho khoảng thời gian cập nhật màn hình hiện tại. Trên Linux, giá trị này không được chuẩn hóa theo số lượng CPU, do đó, một tiến trình phụ thuộc CPU với hai luồng sẽ báo cáo 200%; `top(1)` gọi đây là "chế độ Irix" (Irix mode), theo tên hành vi của nó trên IRIX. Chế độ này có thể được chuyển sang "chế độ Solaris" (Solaris mode) (bằng cách nhấn `I` để chuyển đổi), làm chia mức sử dụng CPU cho số lượng CPU. Trong trường hợp đó, tiến trình hai luồng trên máy chủ 16 CPU sẽ báo cáo CPU là 12.5%.

Mặc dù `top(1)` thường là công cụ dành cho người mới bắt đầu phân tích hiệu năng, bạn nên lưu ý rằng bản thân mức sử dụng CPU của `top(1)` có thể trở nên đáng kể và khiến `top(1)` trở thành tiến trình tiêu thụ CPU hàng đầu! Điều này là do các lời gọi hệ thống mà nó sử dụng để đọc `/proc` — `open(2)`, `read(2)`, `close(2)` — và gọi các hàm này trên nhiều tiến trình. Một số phiên bản của `top(1)` trên các hệ điều hành khác đã giảm chi phí này bằng cách để mở file descriptors và gọi `pread(2)`.

Có một biến thể của `top(1)` tên là `htop(1)`, cung cấp nhiều tính năng tương tác, tùy chỉnh, và biểu đồ thanh ASCII để hiển thị lượng CPU đang dùng. Nó dùng lượng system calls gấp 4 lần, gây tác động đến hiệu năng hệ thống nhiều hơn (Tôi hiếm khi sử dụng nó).

Có một biến thể của `top(1)` cho Linux gọi là `atop(1)`, sử dụng hệ thống kế toán quá trình (process accounting) để bắt các tiến trình thời gian ngắn sẽ kết thúc giữa những lần snapshot của `/proc`.

### 6.6.7 pidstat

Công cụ `pidstat(1)` của Linux in lượng CPU đang được sử dụng dựa trên từng tiến trình (process) hoặc luồng (thread), bao gồm chia nhỏ thành thời gian người dùng (user) và hệ thống (system-time). Theo mặc định, có một bảng báo cáo liên tục cho các tiến trình đang hoạt động. Ví dụ:

```
$ pidstat 1
Linux 2.6.35-32-server (dev7)   11/12/12   _x86_64_   (16 CPU)

22:24:42          PID   %usr %system   %guest   %CPU   CPU  Command
22:24:43         7814   0.00    1.98     0.00   1.98     3  tar
22:24:43         7815  97.03    2.97     0.00 100.00    11  gzip

22:24:43          PID   %usr %system   %guest   %CPU   CPU  Command
22:24:44          448   0.00    1.00     0.00   1.00     0  kjournald
...
```

Ví dụ này được thu thập lúc đang backup hệ thống, trong đó lệnh `tar(1)` đọc các files từ file system, còn `gzip(1)` compress chúng. User-time cho lệnh gzip(1) cao vì mã nén cần dùng cực lớn CPU. Trong khi tar(1) tốn nhiều thời gian kernel để đọc từ file system.

Có thẻ dùng cờ `-p ALL` để hiển thị mọi luồng bao gồm mọi tiến trình idle. Tùy chọn `-t` để hiện thống kê trên từng luồng (thread). Cờ khác có nhắc tới ở chương khác.

### 6.6.8 time, ptime

Lệnh `time(1)` là loại dùng chạy 1 cấu trúc lập trình và báo cáo CPU, có sẵn ở `/usr/bin` nhưng cũng có sẵn trên nhiều shell với tính năng tích hợp (shell built-in).

Ví dụ tính checksum từ 1 đoạn file dài 2 lần:

```
$ time cksum ubuntu-19.10-live-server-amd64.iso
1044945083 883949568 ubuntu-19.10-live-server-amd64.iso

real    0m5.590s
user    0m2.776s
sys     0m0.359s
$ time cksum ubuntu-19.10-live-server-amd64.iso
1044945083 883949568 ubuntu-19.10-live-server-amd64.iso

real    0m2.857s
user    0m2.733s
sys     0m0.114s
```

Lượt chạy đầu cần 5.6s, trong số này 2.8s cho tính checksum (user-mode). Thêm 0.4s (system-time) để trả tài nguyên vì gọi đọc file. Quãng trống có thể do đĩa chờ Disk I/O (file đang vào cache) (5.6 - 2.8 - 0.4 = 2.4). Lần thứ 2 tốn 2.9s vì tất cả data của cái này đã được để trong RAM chính (main memory).

Trên Linux, bản `/usr/bin/time` hỗ trợ cờ `-v` với các thông tin chi tiết khác:

```
$ /usr/bin/time -v cp fileA fileB
    Command being timed: "cp fileA fileB"
    User time (seconds): 0.00
    System time (seconds): 0.26
    Percent of CPU this job got: 24%
    Elapsed (wall clock) time (h:mm:ss or m:ss): 0:01.08
    ...
    Major (requiring I/O) page faults: 0
    Minor (reclaiming a frame) page faults: 294
    Voluntary context switches: 1082
    Involuntary context switches: 1
    ...
```

Tùy chọn `-v` thường không có trong shell built-in.

### 6.6.9 turbostat

`turbostat(1)` là công cụ dựa trên MSR (Model-Specific Register) để xem tình trạng của CPU (cấu hình các module cho hệ linux `linux-tools-common`). MSRs được nhắc ở phần 4.3.10. Một dòng đầu ra:

```
# turbostat
turbostat version 17.06.23 - Len Brown <lenb@kernel.org>
CPUID(0): GenuineIntel 22 CPUID levels; family:model:stepping 0x6:8e:a (6:142:10)
CPUID(1): SSE3 MONITOR SMX EIST TM2 TSC MSR ACPI-TM TM
...
Core   CPU  Avg_MHz  Busy%  Bzy_MHz  TSC_MHz  IRQ  SMI  C1  C1E
            C3 C6 C7s C8 C9 C10 C1% C1E% C3%
...
0      0    97      2.70   3609     2112      1370 0    41  293
...
```

`turbostat(8)` in kết quả bắt đầu ở các tham số CPU thông tin (hơn 50 đầu ra - đã rút ngắn. Nó hiển thị cho ta trung bình ngắt quãng 5s cho hệ cpu, C-state, nhiệt độ (*Tmp) cũng như mức sử dụng nguồn diện (*Watt) trên cả tât cả CPU hay mỗi thiết bị liên quan.

### 6.6.10 showboost

Trước khi chức năng turbostat hỗ trợ cloud Netflix, công cụ `showboost(1)` được làm để đếm chỉ số này khi hiện mức CPU clock rate ("show turbo boost", cũng là tool dùng MSR). Đầu ra tham khảo:

```
# showboost
Base CPU MHz : 3000
Set CPU MHz  : 3000
Turbo MHz(s) : 3400 3500
Turbo Ratios : 113% 116%
CPU 0 summary every 1 seconds...

TIME      C0_MCYC     C0_ACYC      UTIL   RATIO    MHz
21:41:43  3021819807  3521745975   100%   116%     3496
21:41:44  3021682653  3521564103   100%   116%     3496
...
```

Tốc độ chạy đạt tới 3496MHz trên CPU0 (từ mức cơ sở Base CPU Frequency 3000), có thể đo lên qua quá trình intel turbo boost. Bước qua mức độ turbo của process: 3400 & 3500. `showboost(8)` có tại repos `msr-cloud-tools` của tác giả. Có khả năng hệ máy tính bản build khác và cần tool `turboboost(1)` cho khác.

### 6.6.11 pmcarch

`pmcarch(8)` cung cấp cái nhìn mức cao về hiệu năng của các chu kỳ (cycles) xử lý CPU. Là 1 dạng cấu hình thuộc intel "architectural set" dựa dẫm vô PMC. Trên 1 số môi trường mây điện toán (eg AWS EC2) đây là tool kiểm tra PMC duy nhất. Đầu ra tham khảo:

```
# pmcarch
K_CYCLES    K_INSTR     IPC BR_RETIRED   BR_MISPRED  BMR% LLCREF    LLCMISS     LLC%
96163187    87166313   0.91 19730994925  679187299   3.44 656597454 174313799   73.45
93988372    87205023   0.93 19669256586  724072315   3.68 666041693 169603955   74.54
...
```

In ra các cột dạng count/ratios (theo %, tỷ lệ):
- `K_CYCLES`: Chu kỳ (x 1000)
- `K_INSTR`: Câu lệnh vi xử lý (x 1000)
- `IPC`: Lệnh/Chu kỳ
- `BMR%`: Branch Misprediction Ratio (%)
- `LLC%`: Last Level Cache hit ratio (%)

BMR% & LLC% báo những tình huống bị stall cycles ở vị trí cụ thể (IPC đã được giới thiệu tại 6.3.7). Trong repos `pmc-cloud-tools` cũng gồm `cpucache(8)` cho PMC phân cấp cache cao. Nhờ `perf(1)` bạn có thể thiết lập hệ thống nếu tools này chập chờn trên cloud system của bạn.

### 6.6.12 tlbstat

Thêm công cụ trong repos PMC cloud này là tlbstat(8), trả chỉ số của cache về module TLB. Sample output:

```
# tlbstat -C0 1
K_CYCLES   K_INSTR    IPC DTLB_WALKS ITLB_WALKS K_DTLBCYC K_ITLBCYC DTLB% ITLB%
2875793    276051    0.10 89709496   65862302   787913    650834    27.40 22.63
2860557    273767    0.10 88829158   65213248   780301    644292    27.28 22.52
...
```

Đây mô tả tình thế tồi tệ của trường hợp bản vá lõi bảo mật Meltdown (KPTI patches) (đoạn 3.4.3 KPTI - Meltdown). `KPTI flush` liên tục các cache TLB khi gọi syscall khiến tăng stall cycles thông qua việc tiến trình đi bộ (walking TLB) trên các con đường vòng dẫn vào bộ nhớ TLB (hai cột bên phải cao nhất cho thấy nửa thời gian đã bị dùng vô đó, và tốc độ chương trình chạy bị hạ gần 2 lần).

- K_CYCLES: số lần Cycles (x1000)
- K_INSTR: lệnh instruction CPU (x1000)
- IPC: Instructions-Per-Cycle
- DTLB_WALKS: tổng đường dẫn cho Cache Data DTLB
- ITLB_WALKS: tổng count di chuyển trên Instruction TLB
- K_DTLBCYC: Lượng CPU tốn (Cycles at least one PMH is active with data TLB walks × 1000)
- K_ITLBCYC: Instruction lượng Cycle PMH Instruction TLB walks × 1000
- DTLB%: tỉ  số lượng chia đều cho toàn bộ tổng số
- ITLB%: tỉ  số lượng chia đều cho toàn bộ tổng số vòng cho Instruction

### 6.6.13 perf

`perf(1)` là bộ lập hồ sơ chính thức của hệ Linux, đa dạng tính năng và multi-tool (Ghi trong Chương 13 `perf`, còn chương này chỉ phân tích qua dạng CPU/PMCs).

**One-Liners**
Các câu lệnh 1 dòng hữu dụng để nhận phân tích dữ liệu hiệu năng CPU:

- Lấy mẫu function cho ứng dụng đang chạy command này, mỗi giây = 99
```
perf record -F 99 command
```
- Theo dấu (stack traces system-wide) trên bộ khung (frame point) hệ điều hành chừng 10s:
```
perf record -F 99 -a -g -- sleep 10
```
- Lấy mẫu stack bằng mã gỡ lỗi biên dịch dwarf(dbg):
```
perf record -F 99 -p PID --call-graph dwarf -- sleep 10
```
- Lấy mẫu cho chương trình mới gọi qua exec:
```
perf record -e sched:sched_process_exec -a
```
- Thống kê các context switch 10s cùm trace:
```
perf record -e sched:sched_switch -a -g -- sleep 10
```
- Xem việc điều hướng sang con CPU core khác (10s):
```
perf record -e migrations -a -- sleep 10
```
- Lưu quá trình chuyển con (cpu core transfer migrations) (10s)
```
perf record -e migrations -a -c 1 -- sleep 10
```
- Hiển thị theo các phần text gộp, tính % cho dữ kiện lưu trong config perf.data
```
perf report -n --stdio
```
- In chi tiết theo trình cho file perf.data cùng header
```
perf script --header
```
- Trích các trạng thái PMC từ cấu hình toàn hệ thống (5s)
```
perf stat -a -- sleep 5
```
- Bộ Last Level Cache (LLC) (cache cấp sau cùng) thông qua báo cáo hệ của CPU cho tool command
```
perf stat -e LLC-loads,LLC-load-misses,LLC-stores,LLC-prefetches command
```
- Thông lượng memory bus memory-wide per second (mỗi 1s tức là qua interval=1000):
```
perf stat -e uncore_imc/data_reads/,uncore_imc/data_writes/ -a -I 1000
```
- Rate switch các process task cho context switch / giây:
```
perf stat -e sched:sched_switch -a -I 1000
```
- Lưu giá trị context switch trong khi task cũ là TASK_RUNNING (involuntary switches):
```
perf stat -e sched:sched_switch --filter 'prev_state == 0' -a -I 1000
```
- Mode chuyển ring mức đặc quyền:
```
perf stat -e cpu_clk_unhalted.ring0_trans,cs -a -I 1000
```
- Hệ lịch hoạt động schedule cho hệ lập lịch của linux với timer profile (10s thu thập):
```
perf sched record -- sleep 10
```
- Latency chờ độ rỗi của các tiến trình CPU cho sched.
```
perf sched latency
```
- Độ chờ thời gian của hệ (scheduler timehist):
```
perf sched timehist
```


**Lập hồ sơ CPU Toàn hệ thống (System-Wide CPU Profiling)**

`perf(1)` có thể được sử dụng để lập hồ sơ các đường dẫn gọi (call paths) CPU, tóm tắt thời gian CPU được dành ở đâu trong cả không gian nhân (kernel-space) và không gian người dùng (user-space). Điều này được thực hiện bởi lệnh `record`, thu thập các mẫu vào một tệp `perf.data`. Một lệnh `report` sau đó có thể được sử dụng để xem nội dung của tệp. Nó hoạt động bằng cách sử dụng bộ đếm thời gian chính xác nhất có sẵn: dựa trên chu kỳ CPU (CPU-cycle-based) nếu có, nếu không thì dựa trên phần mềm (sự kiện `cpu-clock`).

Trong ví dụ sau, tất cả các CPU (`-a`) được lấy mẫu với các ngăn xếp gọi (`-g`) ở tần số 99 Hz (`-F 99`) trong 10 giây (`sleep 10`). Tùy chọn `--stdio` cho report được sử dụng để in toàn bộ đầu ra, thay vì hoạt động trong chế độ tương tác.

```
# perf record -a -g -F 99 -- sleep 10
[ perf record: Woken up 20 times to write data ]
[ perf record: Captured and wrote 5.155 MB perf.data (1980 samples) ]
# perf report --stdio
[...]
# Children      Self  Command          Shared Object        Symbol
# ........  ........  ...............  ...................  ...................
#
    29.49%     0.00%  mysqld           libpthread-2.30.so   [.] start_thread
               |
               ---start_thread
                   0x55dadd7b473a
                   0x55dadc140fe0
                   |
                    --29.44%--do_command
                                 |
                                 |--26.82%--dispatch_command
                                 |             |
                                 |              --25.51%--mysqld_stmt_execute
                                 |                          |
                                 |                           --25.05%--Prepared_statement::execute_loop
                                 |                                      |
                                 |                                       --24.90%--Prepared_statement::execute
                                 |                                                  |
                                 |                                                   --24.34%--mysql_execute_command
[...]
```

Đầu ra đầy đủ dài nhiều trang, theo thứ tự giảm dần của số lượng mẫu. Các số lượng mẫu này được đưa ra dưới dạng phần trăm, cho thấy thời gian CPU đã được sử dụng ở đâu. Trong ví dụ này, 29.44% thời gian được dành trong `do_command()` và các hàm con của nó, bao gồm `mysql_execute_command()`. Các ký hiệu (symbols) kernel và tiến trình này chỉ có sẵn nếu các tệp debuginfo của chúng có sẵn; nếu không, các địa chỉ hex sẽ được hiển thị.

Tùy chọn `-a` đã trở thành mặc định trong Linux 4.11.

Thứ tự ngăn xếp đã thay đổi trong Linux 4.4 từ callee (bắt đầu với hàm đang on-CPU và liệt kê tổ tiên) sang caller (bắt đầu với hàm cha và liệt kê các hàm con). Bạn có thể chuyển lại thành `callee` bằng cách sử dụng `-g callee`:

```
# perf report -g callee --stdio
[...]
      19.75%     0.00% mysqld          mysqld               [.] Sql_cmd_dml::execute_inner
                    |
                    ---Sql_cmd_dml::execute_inner
                        Sql_cmd_dml::execute
                        mysql_execute_command
                        Prepared_statement::execute
                        Prepared_statement::execute_loop
                        mysqld_stmt_execute
                        dispatch_command
                        do_command
                        0x55dadc140fe0
                        0x55dadd7b473a
                        start_thread
[...]
```

Để hiểu một hồ sơ, bạn có thể thử cả hai cách sắp xếp. Nếu bạn không thể hiểu nhanh ý nghĩa của nó tại dòng lệnh, hãy thử một hình ảnh hóa chẳng hạn như flame graphs.

**Biểu đồ ngọn lửa CPU (CPU Flame Graphs)**

CPU flame graphs có thể được tạo từ cùng cấu hình `perf.data` bằng cách dùng tuỳ chọn tạo `flamegraph` được hỗ trợ ở bản Linux 5.8. Cụ thể:

```
# perf record -F 99 -a -g -- sleep 10
# perf script report flamegraph
```

Sẽ sinh ra biểu đồ dựa trên cấu trúc bộ khung d3 tại `/usr/share/d3-flame-graph/d3-flamegraph-base.html` (chưa có bạn có thể cài thêm phần mềm bằng `d3-flame-graph`). Hoặc có thể chèn gọn trong 1 lệnh như sau:

```
# perf script flamegraph -a -F 99 sleep 10
```

Ở hệ điều hành Linux phiên bản cũ, bạn dùng file báo cáo trực tiếp từ ứng dụng tạo flamegraph của chính tác giả xuất cho script từ `perf script`. Các bước là:

```
# perf record -F 99 -a -g -- sleep 10
# perf script --header > out.stacks
$ git clone https://github.com/brendangregg/FlameGraph; cd FlameGraph
$ ./stackcollapse-perf.pl < ../out.stacks | ./flamegraph.pl --hash > out.svg
```

Cấu hình `out.svg` trả về là file hình vector biểu đồ Flame cho CPU, nó cho phép mở trên ứng dụng web browser. Cũng hỗ trợ tích hợp code JS (ví dụ: Ctrl-F để tìm thông tin hàm/symbol). Lấy xem tiếp ở Phần 6.5.4, Lập CPU Profiling, cũng như đồ họa ở hình 6.15.

Bạn có thể thay vì lưu một file log thì đẩy thẳng các biến pipeline qua code `stackcollapse-perf.pl` để tránh lưu tệp. Thế nhưng lưu tệp (file text dạng out.stacks) có ích để có thể xem cho công cụ phân tích khác sau đó (công cụ như FlameScope).

**Tuỳ Chọn (Options)**

Tệp phân giải `flamegraph.pl` cho phép thêm cờ:
- `--title TEXT`: Thiết lập tiêu đề.
- `--subtitle TEXT`: Thiết lập tiêu đề phụ (subtitle).
- `--width NUM`: Chỉnh chiếu ngang (wide) tệp svg xuất ra, cỡ định dạng gốc là 1200 pixel.
- `--countname TEXT`: Gọi tên biến là cấu hình count hiện tại (giá trị mặc định gọi là “samples”).
- `--colors PALETTE`: Thiết lập hệ thống sắc độ và tông màu (palette). Thay đổi sắc thái để nhìn dễ cấu hình tuỳ tính chất. Một số cờ gồm hệ mặc định (hot), hệ io, java, js, perl, green, red, ...
- `--bgcolors COLOR`: Thay đổi độ gradient cấu hình màu nền, từ xanh tới vàng ngả khói xám. Hoặc đặt màu cụ thể bằng RGB HEX “#rrggbb”.
- `--hash`: Bảng màu gán trực tiếp theo hệ thống hàm bằng giá trị hàm băm (hash).
- `--reverse`: Chuyển định tính ngược biểu đồ tính từ đỉnh chóp tới ngọn.
- `--inverted`: Hệ thống đảo y-axis trục Y, sẽ tạo thành các tia nước/băng.
- `--flamechart`: Sắp xếp cho dạng trục ngang theo dòng thời gian (time-axis x-axis).

Ví dụ dùng cấu hình màu theo mã màu cho luồng của Java:

```
$ ./flamegraph.pl --colors=java --hash --title="CPU Flame Graph, $(hostname), $(date)" < ...
```

Cấu lệnh có chèn biến từ bash shell cho thiết bị hostname và ngày. Dùng 6.7.3 xem phân tích kết quả Flame Graph.

**Duyệt Hồ Sơ cho CPU theo Tiến trình**

Ngoài cho lấy mẫu hệ thống chung, cờ của perf cho phép trích 1 thông số cho PID là: (`-p PID`), hoặc thi hành đo chi tiết 1 command line:

```
# perf record -F 99 -g command
```

Bạn hãy để ý để chèn dấu "--" để tách cái phần thiết lập flags không can thiệp vào tham số chạy config options của tool chạy kia.

**Độ trễ Bộ lập lịch (Scheduler Latency)**

Lệnh `sched` có thể phân tích thông số delay hàng chờ của scheduler.

```
# perf sched record -- sleep 10
[ perf record: Woken up 63 times to write data ]
[ perf record: Captured and wrote 125.873 MB perf.data (1117146 samples) ]
# perf sched latency
-------------------------------------------------------------------------------------
Task                    | Runtime ms     | Switches | Average delay ms | Maximum delay ms |
-------------------------------------------------------------------------------------
jbd2/nvme0n1p1-:175     |      0.209 ms |          3 | avg:       0.549 ms | max:       1.630 ms |
kauditd:22              |      0.180 ms |          6 | avg:       0.463 ms | max:       2.300 ms |
oltp_read_only.:(4)     | 3969.929 ms |       184629 | avg:       0.007 ms | max:       5.484 ms |
...
```

Kết quả độ chờ này cho bảng trung bình hay cực đại từ hệ điều hành về Scheduler delay (độ dài run queue). Ta thấy Dù cho số switch (context switches) cực nhiều (oltp_read_only, mysqld), nhưng độ chậm trễ lại khá nhỏ.

Với những tool sinh file, thì sẽ lưu ý hệ dữ liệu sinh ra quá nhanh. Dữ liệu ghi trên chỉ bằng 10 giây thu gom được tệp file đo độ đo hiệu năng tốn ~ 125 MB file dung lượng cho cấu hình ring buffers CPU. Dẫn tới dữ liệu ghi thiếu hoặc tràn bộ đệm. Thận trọng và theo dõi overhead báo về.

Chức năng phụ có tính phân nhánh như map hay timehist. `timehist` xuất ra từng dòng của process theo sched, tính bằng giây ms:
- `wait time`: sleep time wait
- `sch delay`: Scheduler runtime
- `run time`: cpu xử lý on cpus

**PMCs (Các sự kiện Phần cứng)**

Cờ `stat` giúp in giá trị gộp thành bảng, không tạo ra text perf.data, nó dùng đếm giá trị chu kỳ cpu trong phần cứng (đọc thanh ghi sự kiện). Thí dụ phân mềm zip:

```
$ perf stat gzip ubuntu-19.10-live-server-amd64.iso

 Performance counter stats for 'gzip ubuntu-19.10-live-server-amd64.iso':

      25235.652299      task-clock (msec)         #    0.997 CPUs utilized
               142      context-switches          #    0.006 K/sec
                25      cpu-migrations            #    0.001 K/sec
               128      page-faults               #    0.005 K/sec
    94,817,146,941      cycles                    #    3.757 GHz
   152,114,038,783      instructions              #    1.60  insn per cycle
    28,974,755,679      branches                  # 1148.167 M/sec
     1,020,287,443      branch-misses             #    3.52% of all branches

      25.312054797 seconds time elapsed
```

Sẽ hiển thị tỉ lệ cycle và câu lệnh in (instruction), và giá trị IPC. IPC với giá trị 1.6 là “good” cho mức đo tiến trình rỗi stall cycles.

Ví dụ dưới về hệ đo lường tinh chỉnh NUMA trong bài Shopify (thấy được tải giúp lên độ rộng IPC từ 20-30%, các command đều mất mỗi phần là 30s):

Trước:

```
# perf stat -a -- sleep 30
[...]
     404,155,631,577      instructions         #    0.72  insns per cycle
[...]
```

Sau khi tinh chỉnh NUMA:

```
# perf stat -a -- sleep 30
[...]
     490,026,784,002      instructions         #    0.89  insns per cycle
[...]
```
IPC lên mức chạy từ 0.72 đến 0.89: là đã tăng lên 24%.

**Lựa chọn Sự kiện Phần cứng (Hardware Event Selection)**

Sẽ có hàng loạt list sự kiện có thể trích từ công cụ perf(1) để thống kê phần cứng. (Tùy chọn hiển thị hệ thống). Lệnh là:

```
# perf list
[...]
  branch-instructions OR branches                    [Hardware event]
  branch-misses                                      [Hardware event]
  bus-cycles                                         [Hardware event]
  cache-misses                                       [Hardware event]
  cache-references                                   [Hardware event]
  cpu-cycles OR cycles                               [Hardware event]
  instructions                                       [Hardware event]
  ref-cycles                                         [Hardware event]
[...]
  LLC-load-misses                                    [Hardware cache event]
  LLC-loads                                          [Hardware cache event]
  LLC-store-misses                                   [Hardware cache event]
  LLC-stores                                         [Hardware cache event]
[...]
```

Chú ý trong mục "[Hardware event]" và "[Hardware cache event]". Tuỳ CPU mà bạn có thông tin mục riêng. Sự kiện gọi dưới biến cấu trúc dạng `-e`.

Ví dụ: intel Xeon

```
$ perf stat -e instructions,cycles,L1-dcache-load-misses,LLC-load-misses,dTLB-load-misses gzip ubuntu-19.10-live-server-amd64.iso

 Performance counter stats for 'gzip ubuntu-19.10-live-server-amd64.iso':

   152,226,453,131      instructions         #    1.61  insn per cycle
    94,697,951,648      cycles
     2,790,554,850      L1-dcache-load-misses
         9,612,234      LLC-load-misses
           357,906      dTLB-load-misses

      25.275276704 seconds time elapsed
```

Gồm các biến được gọi đo là:
- `L1-dcache-load-misses`: Lỗi rò rỉ L1 cho bộ cache nạp dữ liệu data. Sẽ hiển thị tình trạng nếu Level 1 không truy lùng ra để đi đọc. So các giá trị khác để tìm cache hit ratio.
- `LLC-load-misses`: LLC là (Last level cache) tải Miss, khi đã sai tại cấp cuổi (ngoài cùng), bộ CPU memory phải truy lùng bộ lưu lượng Ram Main Memory. Cho nên đánh giá dựa theo chỉ số này biết tốc độ sử dụng I/O bộ nhớ chính. Còn khác biệt lấy trên L1 biết năng lực cache đệm.
- `dTLB-load-misses`: Sai bộ chuyển ngữ dữ liệu Translation lookaside buffer cho data. Coi được cái sự hiệu năng trên MMU (Memory management unit).

Khác biệt này cho biết lượng memory I/O có mức hiệu suất như thế nào và các cache hiệu năng hoạt động có ổn không. Bảng trên cũng có thể chuyển số theo bảng mã phần HEX nếu ở cấu hình CPU của bạn báo lỗi.


**Truy vết Phần mềm (Software Tracing)**

`perf` cũng có thể ghi lại và đếm các sự kiện phần mềm. Liệt kê một số sự kiện liên quan đến CPU:

```
# perf list

[...]
  context-switches OR cs                             [Software event]
  cpu-migrations OR migrations                       [Software event]
[...]
  sched:sched_kthread_stop                           [Tracepoint event]
  sched:sched_kthread_stop_ret                       [Tracepoint event]
  sched:sched_wakeup                                 [Tracepoint event]
  sched:sched_wakeup_new                             [Tracepoint event]
  sched:sched_switch                                 [Tracepoint event]
[...]
```

Ví dụ sau sử dụng sự kiện phần mềm `context-switches` để truy vết khi các ứng dụng rời khỏi CPU, và làm báo cáo (call stacks) trong một giây:

```
# perf record -e sched:sched_switch -a -g -- sleep 1
[ perf record: Woken up 46 times to write data ]
[ perf record: Captured and wrote 11.717 MB perf.data (50649 samples) ]

# perf report --stdio
[...]
    16.18%    16.18% prev_comm=mysqld prev_pid=11995 prev_prio=120 prev_state=S ==>
next_comm=swapper/1 next_pid=0 next_prio=120
               |
               ---__sched_text_start
                   schedule
                   schedule_hrtimeout_range_clock
                   schedule_hrtimeout_range
                   poll_schedule_timeout.constprop.0
                   do_sys_poll
                   __x64_sys_ppoll
                   do_syscall_64
                   entry_SYSCALL_64_after_hwframe
                   ppoll
                   vio_socket_io_wait
                   vio_read
                   my_net_read
                   Protocol_classic::read_packet
                   Protocol_classic::get_command
                   do_command
                   start_thread
[...]
```

Đầu ra được cắt bớt này cho thấy mysql chuyển cảnh (context switching) để chặn trên một socket qua `poll(2)`. Để điều tra thêm, hãy xem phương pháp phân tích Off-CPU trong Chương 5, Ứng dụng, Mục 5.4.2, Phân tích Off-CPU, và các công cụ hỗ trợ trong Mục 5.5.3, `offcputime`.

Chương 9, Ổ đĩa, bao gồm một ví dụ khác về truy vết tĩnh với `perf(1)`: tracepoints I/O khối. Chương 10, Mạng, bao gồm một ví dụ về thiết bị đo đạc động với `perf(1)` cho hàm nhận nhân mạng `tcp_sendmsg()`.

**Truy vết Phần cứng (Hardware Tracing)**
`perf(1)` cũng có khả năng sử dụng thiết bị đo đạc phần cứng cho khả năng đọc từng lệnh chi tiết một (per-instruction), nếu hệ cấu hình của process hỗ trợ tính năng trên. Tuy đây là phần tính chuyên xâu cấp thấp nhưng Chương 13 (`perf`) Mục 13.13 (Other Commands) sẽ đi sâu về điều đó.

**Tài liệu (Documentation)**

Để biết thêm về `perf(1)`, vui lòng tham khảo Chương 13, `perf`. Cũng như xem trang cài hướng dẫn manual của nó, phần Documentation của kernel source trên linux thuộc mục `tools/perf/Documentation`, hoặc xem các file mẫu ở web ["perf Examples" page] của tác giả, cũng như "Perf Tutorial" và "The Unofficial Linux Perf Events Web-Page".

### 6.6.14 profile

`profile(8)` là công cụ BCC thực hiện việc lấy mẫu (sample) của stack traces trong những khoảng chờ thời gian định sẵn theo ngắt nhịp đếm định (frequency count). Tiện ích thiết thực nhất của trình BCC này chính là việc kiểm tra tiêu hao mức dùng CPU tại phần đa mọi nẻo vào bằng luồng mã code tiêu resource CPU (Xem tool hardirqs(8) của 6.6.19 cho những dạng tiêu dùng khác nữa về tài nguyên).
Việc cấp tính toán này (overhead) nhẹ đi nhiều so với code từ perf(1) làm, vì nó đơn thuận đếm thống số liệu ở kernel đưa dữ liệu về user space (xem Hình 6.15 ở trước cho dễ đối chiếu). Chương 5, Mục 5.5.2 về `profile` cũng bao hàm cách nó đo đạc ứng dụng chương trình như 1 profiler đích thực.

Theo cài đặt cấu trúc lúc đầu hệ thống, lệnh này quét trên 49 Hz đo mẫu cho tất tần tật luồng mã user stack hay kernel trace cho toàn bộ CPU list tổng. Ghi mẫu đo lệnh:

```
# profile
Sampling at 49 Hertz of all threads by user + kernel stack... Hit Ctrl-C to end.
^C
[...]
finish_task_switch
__sched_text_start
schedule
schedule_hrtimeout_range_clock
schedule_hrtimeout_range
poll_schedule_timeout.constprop.0
...
do_command(THD*)
start_thread
-                mysqld (5187)
```
Chuỗi xuất mô tả báo cáo các thông số thành list mã lệnh (hàm) nối giữa dấu vạch "-", cộng cùng tên tên của luồng ứng dụng và tiến trình ID PID. Mã ngăn xếp nào chạy với count nhiều nhất theo chiều tăng thì dồn vô đuôi chung cùng của mã (most frequent run).
Code trả này tuy được xuất (khoảng hơn 8 nghìn dòng lệnh), nhưng đã trích gọn lại xem phần đuôi của kết quả in là thấy: Các tiến trình của nhóm mã lên lịch on-CPU đã kích hoạt hàm thông qua luồng chạy lệnh của module hàm poll(2) mã mysql của tiến trình (pid là 5187). Chỗ mẫu đo stack này đếm tổng tốn 151 counts nhảy trong quá trình truy đo.

`profile(8)` có những mục flag khác tuỳ chọn bao hàm:
- `-U`: Lấy duy nhất trace chỉ phần code gọi của không gian mã người dùng (user-level stacks).
- `-K`: Thu nhận lấy dòng lệnh cho mã không gian kernel nội lệnh.
- `-a`: Làm nổi đoạn call để phân hoạch tính hiệu báo ("_[k]" nhằm ám hiệu kernel frame).
- `-d`: Bọc cái ký hiệu khung phân tách chuỗi mã giữa lớp nhân kernel cùng mã code user.
- `-f`: Báo hiệu trả code lệnh chuỗi dài báo xếp theo "gấp gọn" folded dạng. Dành định dạng cho hình biểu đồ nạp (flame graph importer).
- `-p PID`: Đo profiling đúng trên tham số tiến trình ID chạy đó mà thôi.
- `--stack-storage-size SIZE`: Sức chứa bộ chứa stack băm của bản thiết lập, bộ biến chuẩn thường số liệu lưu tới 16,384 dấu vết độc đáo.

Nếu gọi báo "WARNING: 5 stack traces could not be displayed." nghĩa là bị bão hoà giới hạn. Bạn có thể chỉnh cỡ bằng tuỳ chỉnh option lệnh kích thước biến `--stack-storage-size`.

**Biểu đồ ngọn lửa profile (profile CPU Flame Graphs)**
Lệnh định tham số folded bằng cờ `-f` dùng với trình importer của đồ thị hình flamegraph xuất svg code của tác giả. Tệp thiết lệnh bao gồm:
```
# profile -af 10 > out.stacks
# git clone https://github.com/brendangregg/FlameGraph; cd FlameGraph
# ./flamegraph.pl --hash < out.stacks > out.svg
```
Bạn sẽ sử dụng ứng dụng web để coi out.svg file xuất này.
Hai bộ này (`profile(8)`) cùng như chuỗi lệnh khác cho BCC (`runqlat`, `runqlen`, `softirqs`, `hardirqs`...) là bộ trình tools do BPF cung cấp.

### 6.6.15 cpudist

Trình `cpudist(8)` là tiện ích BCC nhằm trích lập lại thông số bảng phân phối tần suất khoảng chạy CPU thời gian cho số lượt gọi luồng ứng dụng đo lường (thread wakeup). Hỗ trợ kiểm tra thống kê tính cách thông số theo đặc trưng hiệu năng cung cấp dữ kiện quan trọng trước tinh chỉnh tham số, chọn quy tắc design. Với ví dụ là thiết lập cho môi trường 1 cơ sở dữ liệu trên cloud với 2 CPUs mã đo như sau (trích theo ms dùng thời gian 10s count một lần):

```
# cpudist 10 1
Tracing on-CPU time... Hit Ctrl-C to end.
     usecs               : count     distribution
         0 -> 1          : 0        |                                        |
         2 -> 3          : 135      |                                        |
         4 -> 7          : 26961    |********                                |
         8 -> 15         : 123341   |****************************************|
        16 -> 31         : 55939    |******************                      |
        32 -> 63         : 70860    |**********************                  |
        64 -> 127        : 12622    |****                                    |
...
```

Chạy in mức luồng ứng dụng database phần lớn tốn dải giữa 4 tới 63 micrô giây (microseconds) trên CPU. Đây là thời gian cực kì ngắn. Biến điều chỉnh (options) cung bao gồm:
- `-m`: Hiển thị xuất cho milli giây (milliseconds).
- `-O`: Theo dõi ngắt luồng lệnh ở off-CPU chứ không phải dạng the on-CPU bình thường.
- `-P`: Trả báo cáo dạng biểu đồ trên từng process thông thường 1.
- `-p PID`: Cấp ID duy nhất trace đúng đó thôi.
Đây dùng song trùng với `profile(8)` tổng báo cách ứng dụng của chương trình đang sống có ở cpu hay chạy cái trình dịch vụ ứng dụng nào rồi.

### 6.6.16 runqlat

Bạn dùng BCC, hay bản dùng bpftrace là trình lệnh `runqlat(8)` dùng thông báo hệ thống truy đo trễ Scheduler theo dạng danh xưng cũ thời gian chờ (run queue latency / hàng đợi chờ chạy task của cpu). Có tác dụng tìm những khúc bị tắc bão hào tài nguyên khi số nguồn demand lớn hơn CPU mà có năng xử lý tiếp, chỉ số đo là dạng biến đo các thời kỳ của những chuỗi tác vụ luồng nào cũng chịu ảnh hưởng bởi waiting time delay ở cpu cho quá trình chờ phần nó trong CPU.

Ví dụ dưới đo kết quả truy đo luồng thời lượng `runqlat(8)` chạy qua BCC với database mySQL trên hệ cpu đôi đám mây (2-CPU MySQL) đang tải ở cường độ thấp (khoảng hệ 15% của toàn phần tài nguyên tổng hệ CPU báo cáo). Đối số cung cấp báo `"10 1"` chạy lấy đếm ngắt báo trễ hàng chờ theo độ định khung 10s thời gian (thử một lần):

```
# runqlat 10 1
Tracing run queue latency... Hit Ctrl-C to end.
     usecs               : count     distribution
         0 -> 1          : 9017     |*****                                   |
         2 -> 3          : 7188     |****                                    |
         4 -> 7          : 5250     |***                                     |
...
    131072 -> 262143     : 88       |                                        |
```
Với thiết bị báo cáo số thấp như kia thì điều làm giật mình tại sao lại có độ delay đến như đoạn từ số lượng 88 lệnh nằm vào cung thời gian (65 mili đến 131 miligiay). Lý ra sau mới hay đám mây cho module của hypervisor bị cấu thiết tính throttling cpu, đâm tiêm nhồi gây độ trễ CPU scheduler run quá sức trễ. (Báo scheduler latency delay / throttling).
Có tuỳ lựa chọn (Options):
- `-P` Đưa số in lên thanh bar trên từng PID
- `-p PID`: Tập trung chạy với PID duy nhất cấp đi.
- `-m`: Hiển trị báo phân bổ miligiây.
- `--pidnss` Trả bar histogram báo trên mỗi namespace pid đó.

Đo qua lệnh này trích từ biến số thức wakeup hệ và đổi trạng thái (context switch) của nhóm quá trinh (time from wakeup to running) theo hàm trình sự kiện scheduler. Số sự kiện trên hệ mạnh sẽ tràn và quá 1 triệu một s, lúc dù có cấu BPF để xử tối ưu số đi nữa thế thì sự sinh ra có mỗi micro thứ n cũng tạo gánh nặng thêm cho tiến trình overhead đó.

### 6.6.17 runqlen

Với trình từ `runqlen(8)` trên BCC or bpftrace đo khoảng kích lượng dài có ở hàng chờ của schedulers (CPU run queue len), tính toán đếm count dòng số tiến trình còn đang đợi chờ và làm giá cáo bẳng sơ đồ biểu tuyến tính histogram. Cực công hiệu thông số chi dùng phân hoá làm rõ cho số báo delay do hệ thống của độ gọi (run queue latency) đo lường ước lượng giá phải chăng vì trích số định lượng theo tần count rate hệ 99 Hertz, mà overhead gần bằng số ko nhỏ và nhỉnh đi mức không gây ảnh. Ở đối lệnh khác của bên chạy `runqlat(8)` nó trích hết ngắt cho toàn chục triệu sự tác kiện thì sẽ tạo delay thêm.

Thử với test của BCC `runqlen(8)` trên nền 2-cpu database mySQL dùng định số lượng phân nhỏ ~15% công vụ. Chèn cấu 10 1 chạy trích mười giây theo chỉ số lượng 1 lượt cho in ra màn:

```
# runqlen 10 1
Sampling run queue length... Hit Ctrl-C to end.

     runqlen       : count     distribution
         0         : 1824     |****************************************|
         1         : 158      |***                                     |
```
Đầu báo thông báo đa thời gian chiều độ trên lệnh báo dòng dài hàng là zero, cơ mà cũng chiết xuất cỡ chừng là 8% lúc thời gian lúc này cấu hệ chiều rải lên hàng lượng của một (một số threads bận chờ đi vào phần tài nguyên CPU).

Với option đi theo là:
- `-C` chạy giá đo histogram với cpu rẽ.
- `-O` chỉ in của cấu tính của tiến trình điền của mốc waiting (run queue occupancy) thôi.
- `-T` Có thời gian hệ tham số timestamps in output bồi cùng.

`Run queue occupancy` chỉ số riêng để biểu thì tính chất tỷ lượng time số dư báo tiến trình ở số ngắt đợi CPU mà có, dùng nhiều mục đích kiểm báo hay tạo thông số tạo vẽ báo chuỗi đồ hoạ thời kì.

### 6.6.18 softirqs

Tính thời báo của ngắt sự kiện do trình tạo mềm `softirqs(8)` phân hệ BCC thông số hiện chi phí của sự chạy hàm cho module ngắt (soft interrupts hay tên soft IRQs). Tổng system thời theo soft IRQs được nhiều module đọc được chả hạn như `%soft` ở bộ check mpstat. Ngoài ra `/proc/softirqs` lưu chuỗi giá hàm gọi của Soft IRQ này dưới mục dạng số nguyên (counts of event) khác với BCC softirqs là tính tổng giá chu kỳ chạy thời lượng.

Cùng chạy ở thông qua cấu DB mysql cho hệ CPU 2 cái đo 10 giây thời báo sự kện ngắt mềm:

```
# softirqs 10 1
Tracing soft irq event time... Hit Ctrl-C to end.

SOFTIRQ          TOTAL_usecs
net_tx                     9
rcu                      751
sched                   3431
timer                   5542
tasklet                11368
net_rx                 12225
```
Thấy chỉ số chừng 12 milli giây ở hàm trả báo cho thông mạng (net_rx), cho hay phần CPU bị tiêu pha dùng từ ngắt nhưng có do ko liệt ở report mã trên cấu `perf` đo chả hạn mã phân tích CPU profiles nên bị dính lệnh không cho dừng đo (non-interruptible function) thế nên.
`softirqs` còn dùng đo các flag như cấu -d làm hệ báo cho histogram sự kiện báo trên biến IRQ chạy qua thời gian, và `-T` đi kèm timestamp xuất lệnh.

### 6.6.19 hardirqs

Còn theo dạng gọi phần cứng sinh cứng hệ IRQ trình `hardirqs` là công BCC (hardirqs(8)) nhằm thông thu đo hàm do Hard IRQs trả sinh. Chạy số cấu `%irq` từ máy trích cho theo mpstat thì dùng hệ count sinh từ tập /proc/interrupts trả danh số sự counts, tuy vậy trình `hardirqs(8)` đếm hệ dùng chuỗi đo mili/tính vi mô vi phân thời lúc sử dụng mà báo trên cpu bằng cách này mới đủ lượng sự phân bổ của lượng tài xử chứ không dùng event counts nguyên.

Trên máy test cấu 10 giây hệ:
```
# hardirqs 10 1
Tracing hard irq event time... Hit Ctrl-C to end.

HARDIRQ                    TOTAL_usecs
nvme0q2                             35
ena-mgmnt@pci:0000:00:05.0          72
ens5-Tx-Rx-1                       326
...
ens5-Tx-Rx-0                      5922
```
5.9 milli giây thu của tiến độ ngắt cứng cho thiết cổng mạng ens5... do dùng hàm phần cứng. Bạn sẽ bắt cấu lệnh gọi mà thường bị đo trượt do lọt qua kẽ hở của perf như với softirqs có bàn vậy cấu này là như các chức khác ở hệ module đó. Option lệnh tuỳ cấu chọn khá giống với softirqs(8).

### 6.6.20 bpftrace

Dùng công trình bộ truy bám ngôn ngữ qua công biên chạy lệnh bám với ứng dụng tracer lập trình gọi là thẻ `bpftrace`, cấu dựng BPF theo mức ngữ ngôn lệnh cho gõ script tạo dòng phân báo, chuyên dụng chèn những kịch tuỳ tu biến dò rỉ lỗi hiệu suất đo được (ví dụ script ngắt `runqlen(8)`, `runqlat(8)`... có kho tải của `bpftrace`). Xem thêm mô miêu về phân bpftrace qua chương hệ 15 kia, mục ở ta coi code chạy qua báo CPU trên nó cho ví như:

**Câu lệnh một dòng (One-liners)**
Các câu lệnh mẫu đo gọi tính truy trên thiết lập khác gồm:
- Truy dò lúc quá trình sinh thông args qua sys enter cấu : `bpftrace -e 'tracepoint:syscalls:sys_enter_execve { join(args->argv); }'`
- Đo qua giá count lệnh báo hàm bởi hệ theo pid/chuỗi : `bpftrace -e 'tracepoint:raw_syscalls:sys_enter { @[pid, comm] = count(); }'`
- Đo đếm bằng lệnh sys_enter tuỳ biến probe name: `bpftrace -e 'tracepoint:syscalls:sys_enter_* { @[probe] = count(); }'`
- Lấy mẫu chạy cho 99 hẹc theo mỗi tiến trình chạy được: `bpftrace -e 'profile:hz:99 { @[comm] = count(); }'`
- User and Kernel cấu ở mức profile 49 hertz (Tên và hàm count lại, toàn system-wide)
- Stack khung ngắt User-level bằng hertz 49 theo luồng `189`: `bpftrace -e 'profile:hz:49 /pid == 189/ { @[ustack] = count(); }'`
- Giới định báo trả 5 hàm báo level đo PID 189 `@[ustack(5)]`: `bpftrace -e 'profile:hz:49 /pid == 189/ { @[ustack(5)] = count(); }'`
- Báo quá theo định biến tiến quá trình của `mysqld` lấy count mức báo user_stack qua trace Hz 49:
```bpftrace -e 'profile:hz:49 /comm == "mysqld"/ { @[ustack] = count(); }'```
- Hàm thu scheduler qua trace kernel point `tracepoint:sched:* { @[probe] = count(); }`
- Hàng count sự thu off-CPU cho đệ ngắt đổi trace hệ chuyển point context switch (kstack tracepoint sched switch).
```bpftrace -e 'tracepont:sched:sched_switch { @[kstack] = count(); }'```

**Các Ví dụ:**
Trong báo trace lấy 3 stack top của biến MYSQL cho hệ profile chạy bpftrace 49 hz mức đếm (User-stack 3 khung cho tiến mysqld đếm hệ list danh):
```
# bpftrace -e 'profile:hz:49 /comm == "mysqld"/ { @[ustack(3)] = count(); }'
Attaching 1 probe...
^C
[...]
@[
   ppoll+166
   vio_socket_io_wait(Vio*, enum_vio_io_event)+22
   vio_read(Vio*, unsigned char*, unsigned long)+236
]: 10
[...]
```
Hai lệnh báo có mẫu ngắt 8 & 10 báo cpu truy theo hàm do trễ từ networking call (tải hệ số socket network poll ppoll).

**Hoạt động Hệ Lập Lịch nội hàm (Scheduling Internals)**
Nếu tự tạo script check hành vi scheduler, lấy bằng trình call liệt truy hàm tracepoint:
```
# bpftrace -l 'tracepoint:sched:*'
tracepoint:sched:sched_kthread_stop
tracepoint:sched:sched_waking
...
tracepoint:sched:sched_switch
...
```
Có dùng flag gõ `-lv` mà check hàm và option cho đối số (arguments) lệnh cấu đó. Với dùng truy kprobes ta chạy kprobe `kprobe:sched*` trích nội hàm bắt bằng sched trả (trên hệ Linux nhân 5.3):
Có 24 kprobe sched báo tracepoints cung trả cùng 104 ngắt hàm kprobe possible với mã 'sched' kia. Các báo event scheduler được gọi lặp thường khá là mức thu thập có độ chạy chi lớn vào system, cho nên hãy lấy gộp summary cho các biểu stat `maps` giảm lượng chi phí khi print ra output. Cẩn báo và ghi cho bớt tốn nhất phần cần trích thiết thôi.

### 6.6.21 Các Công cụ Khác (Other Tools)

Bảng dưới 6.11 chứa các nguồn công phụ dùng được đo của OS CPU qua Linux lấy trích trên (tài liệu: *BPF Performance Tools*).

**Bảng 6.11: Công cụ quan sát CPU khác**

| Mục | Công cụ | Mô tả |
|-----|---------|-------|
| 5.5.3 | `offcputime` | Profiling off-CPU sử dụng lập lịch trace của bộ scheduler |
| 5.5.5 | `execsnoop` | Các luồng command tạo từ app theo run event báo |
| 5.5.6 | `syscount` | Tính cho list system call của process chạy |
| [Gregg 19] | `runqslower` | Tìm ra hàng gọi lâu độ trễ run queue quá mấu threshold ngắt |
| [Gregg 19] | `cpufreq` | Trace CPU speed luồng với đo freq |
| [Gregg 19] | `smpcalls` | Call đo số lệnh SMP của chip CPU remote kia đi call số lượng |
| [Gregg 19] | `llcstat` | Tính theo miss của bộ LLC the hits hệ quá trình |

Nhiều nguồn cấu hiệu dụng đo công cụ tool Linux gồm:
- `oprofile`: Profile hệ cho process đo do John Levon viết.
- `atop`: Process tiến trình lấy bằng process accounting xem đo thông số lượng nhiều cái nhỏ theo hệ tiến trình short-lived quá trình đó qua hệ system-wide theo log của atop(1).
- `/proc/cpuinfo`: Danh CPU tốc tần flags báo thiết kế lõi hệ.
- `lscpu`: File cấu thông số hệ của chip CPU architecture.
- `lstopo`: Topological hwloc (hardware topology). (Ví dụ: `lstopo(1)` SVG đầu ra hình 6.18 bản map logic).
- `cpupower`: Dòng cấu check cấp nguồn năng điện (C-state power cpu config idle check power freq states) (ví dụ CPUidle governor, state C0 C1 C3... Latency usage & duration) chạy của nhân kernel C-system (`/sys/devices/system/cpu/cpuidle/`).
- `getdelays.c`: Đo task bằng OS config từ accounting tính CPU hệ.
- `valgrind`: Nhóm debugging profile memory [Valgrind 20]. Khung gồm có gọi `callgrind`, `cachegrind`... đo hiệu phần của cache hardware chạy tiến chương trình và code báo.

Cũng có hệ thiết như Intel vTune (cho Intel config profile) mà AMD thì dùng cấp (AMD uprof config profile tool) để tra CPU performance xịn xò với cả PMC nữa kia.

**GPUs**
Chưa có trọn các công phân GPUs theo dạng default sẵn tool gộp. GPUs thường cung mỗi hiệu riêng cấp driver tool GPU. Gồm có:
- `nvidia-smi` , `nvperf`, và bộ *Nvidia Visual Profiler*: Nvidia
- `intel_gpu_top` & *Intel vTune*: Mảng intel GPU.
- `radeontop`: Cúa dạng mã chip AMD/Radeon báo GPUs tool stat rate thông instruction resource GPU.
Sự trace từ PMCs cùng qua list gpu của hàm perf (`perf list | grep gpu`). Tool phân chia profile gpu thì đâu lấy gọi của CPU đo code run (no process runtime stack trace), vậy mới sinh lệnh API & transfer hàm đo riêng gpu chuyển thời memory vào GPU.

## 6.7 Hình ảnh hóa (Visualizations)

Mức sử dụng CPU trong lịch sử đã được hiển thị bằng các dạng biểu đồ đường (line graphs) của mức sử dụng (utilization) hoặc các mức tải trung bình (load average), kể cả cái tool tải trên bản X11 gốc (`xload(1)`). Đồ thị biểu đồ đường diễn tả hữu hiệu sự thăng trầm cho các đối chiếu với nhau bằng mắt thường, cũng giống cho hệ tham chiếu patterns qua mốc các quá trình xem diễn theo thời gian (coi đoạn 2.9, Monitoring ở Chương 2 Phương pháp luận).

Tuy nhiên, dạng biểu đồ đường vẽ lại không có tính linh hoạt thu phóng tỉ lệ dễ dàng khi các cấu thiết CPU mọc lên như nấm, riêng trên mô hình điện toán đám mây cho quy mô tới cả chục ngàn CPU—1 cái graph với 10000 dòng nhìn sẽ thành nét vẽ bôi bậy bạ vậy.

Những bản thống kê thay thế vẽ dưới dạng line graph, gồm việc đếm biểu đồ dòng thời gian cho trung bình đường chạy, độ sai số lệch ngắt, đỉnh cận mốc (maximums), và phần phân trăm (percentiles) tạo các giá gốc linh hoạt dùng được. Thế nhưng cấu đồ CPU báo cáo kiểu biểu chạy bimodal (phân bổ đôi) — tức 1 bộ phận chạy CPU rỗi (idle hay gần idle), cùng 1 bộ vút lên tải cấu hình chạy (100% utilitzation) nên cấu hình chả lột qua biểu thị đồ hoạ báo cáo đo vậy. Cần xem cho đúng phần trần mô phân phối. Hình kiểu bản đồ nhiệt (utilization heat map) là để cho các trường hợp làm vậy.

Phần mục của bảng đồ đồ nhiệt CPU (CPU utilization heat maps) mô tả cho mức đo hệ dùng cấp giây CPU (CPU subsecond-offset heat maps), kiểu Flame Graphs và FlameScope báo cáo ở phần sau. Tôi làm các loại báo cáo hiện thể hình hoạ đó nhằm giải những bài vướng ở điện toán đám mây với bộ analysis cho hệ enterprise doanh nghiệp.

### 6.7.1 Bản đồ Nhiệt Độ Sử Dụng (Utilization Heat Map)

Mức sử dụng (Utilization) theo thời gian được hiển thị với cấu bản đồ nhiệt dạng heat map bôi theo độ dày báo màu (darkness) của mỗi lượng chỉ số điểm ảnh theo lượng đo tỷ lệ CPU gộp của time range thời gian. Được giới thiệu ở mục 2 Chương Phương pháp luận (Heat maps).

Ví dụ biểu đồ từ hình hệ Hình 6.19 cho tải CPU ở trung tâm số liệu lớn cho môi trường nền cloud public. Tới 300+ lượng vật lý máy với hơn 5312 CPU hiện thị báo ở màn (Hình 6.19).

Bóng ở vạt đáy đồ heat map mô cho một số trần chạy cỡ quanh mức dưới rỗng từ 0% và lên ngấp nghé 30%. Sọc màu kéo cắt tại vạt chóp là qua quãng dòng time, luôn thấy có nhóm bị mức tải căng 100% tài nguyên CPU. Sọc xám ngắt bôi đậm nói lên việc là nhiều con nhóm CPU dính chấu chót đó, chớ không phải là cái.

### 6.7.2 Bản đồ Nhiệt Độ Lệch Dưới-Giây (Subsecond-Offset Heat Map)

Kiểu dạng biểu map này hỗ trợ quan sát sự kiện xảy từ ngắt dòng ở trong một hệ 1 giây. Việc của CPU được truy tìm do milli/micrô độ giây phân mảnh hoạt động; việc báo hệ gộp do chuỗi mảng trung bình cho độ dài toàn phút làm hụt xoá bỏ số kiện có tính chất rất thiết thực. Subsecond-offset báo cho đồ độ chững mức ngắt nhỏ tại đồ y-axis thời lượng cùng với biến CPU không bận theo lượng xám bôi màu đó. Biểu thị quy 1 giây thành một đường kéo mốc trục đọc quét xuôi thẳng từ lên ngọn.

Hình 6.20 cho cấu báo của subsecond-offset báo lượng heat map cơ sở cloud database dữ liệu mây của Riak.

Thứ lôi cuốn tại loại nhiệt bản đồ này chả phải ở khung CPU bị làm mệt để thao tác tải chạy cho database truy lùng dữ kiện, trái lại, tại cái quãng không chúng được rãnh làm trống trải trắng trơn như các cụm chỉ sọc ở khung hở màu trắng đoan kia. Một luồng chặn nghỉ cả trăm mili-giây (hundreds of milliseconds) chả có cái luồng nào từ cơ sở database đẩy qua chạy được cpus. Cung cấp dữ chỉ chỉ đến một đoạn lỗi truy vết locking chặn của toàn database đứng trệ lại theo mốc delay hàng hằng trăm nghìn mili giây của vòng thời gian delay.

Với hình báo này mà ta lại đi báo theo biểu thống thời gian đường dòng truyền thống line graph thì chắc mập mờ chững bị lỗi bỏ nhẹ theo việc đo xem như chỉ là tải rung lắc xê dịch thôi chả truy gì đi tiếp cả.

### 6.7.3 Biểu đồ Ngọn Lửa (Flame Graphs)

Soi hệ ngăn xếp hồ sơ luồng (profiling stack traces) quá hiệu suất để cắt nghĩa thời lượng CPU cho gọi (call paths code) do mã tại user/kernel layer chạy ra. Báo của nó tạo hàng dãy tờ văn thư quá dài. Sửa đi cái đó thì Flame graph sẽ hiển báo ngọn đuốc báo cấu độ sử theo từng độ chạy cpu được ngó theo một dạng sáng to và nhanh lẹ hơn lúc trace stack của nó. Ở Hình ví dụ của cái 6.21 là lệnh profiling hệ trình `perf(1)` gọi thành báo ngọn lửa.

Flame graph của biểu đó thành dạng dựng đo cho đủ dạng trích CPU nào sinh ra code chứa stack traces, mà đó từ `perf(1)`, `profile(8)`, cái của `bpftrace` hoặc tá hệ loại khác. Cấu biểu này chẳng phụ phần đo báo mỗi trích riêng tuỳ CPU profile riêng nào. Chương tiết dưới đây trích giải nghĩa code từ hàm cẩu FlameGraph của tác giả qua chạy hệ `flamegraph.pl` tạo báo flame graph nha. (Bạn dùng thêm các trích dạng hàm d3 flame graphs do cộng hoạ từ Martin Spier triển.

**Đặc điểm (Characteristics)**
CPU flame graph có những bộ dạng thế này:
- Mỗi thanh hàm ô chỉ thị ứng theo lệnh ở stack chạy.
- Đồ x-y gọi chiều y-axis chỉ độ ngập trong stack hố đệm call ngắt. Ô đụng ở chóp điểm chóp biểu trưng hệ đệm lệnh trực gọi tiếp đang diễn ra (on-CPU). Trượt đuôi các hàm xếp xuống theo cấu tầng cho dòng hàm con đang chạy cho hàm nội hàm cha phía đuôi móng (tổ tiên - ancestry).
- Đồ ở rải cho x-axis tính khoảng cho cái sample population tập con luồng ngắt mẫu thử được sinh. Không để đếm cho dòng thời theo như đồ hoạ thị trục của số biểu theo kiểu quét từ tả hữu (left-to-right passing of time). Sắp theo chữ mục từ A-Z mà ra cho chiều này chớ chiều của x chả mang ý hệ nào cả.
- Khung theo chiều mập phình của bề hóp (width) nói hàm trích đo chỉ ngắt on-cpu theo cái đếm ngắt báo sample đo về cho luồng cha của gốc rễ hay ở ngay cái tiến trình (ancestry/on-cpu). Béo bề to ra khung tuỳ hàm do làm chậm thao hoặc đếm gọi được truy call chạy vòng quá lớn tần suất lúc gọi. (chớ tổng lúc call count là không lưu báo ở flame graph được tuỳ cái sample nhé)

Giá sample lớn chênh lệch tổng với time nếu luồng threads tải và đong trích tại parallel song song nhịp đồng.

**Màu sắc (Colors)**
Khung sẽ chọn nhuộm độ biểu sắc các hệ sắc bảng (color schemes) trích. Dạng khung để khởi tạo đầu Hình 6.21 lấy các ánh hệ sặc màu tính chất warm (tông đồ dạng sắc nóng) ngẫu tính từng trích frame nên rất đễ tách lùng bằng mục thị khi nó nén san sát tại cùng một đoạn cao liên đới (adjacent towers). Sau bao năm mình bổ ra khá hệ loại mẫu màu đồ (color schemes). Tôi thì tìm sau hệ liệt theo cấu sau cho có sự đáp với end user đo FlameGraph nhé:
- Hue: Gam (hue) biểu cấu thiết tuỳ theo ngôn thuật cấu code loại ứng dạng báo (Native user -> Đỏ xám / orange - cho kernel. Màu yellow đại từ cấu ngôn ngữ C++; green thì dạng scripts phiên dịch, inlined dạng aqua thanh thiên.. v v tuỳ vào các bạn nếp code bạn lập ngôn định vị gì mà dùng nó thôi. Hệ code cho highlight match tìm thì đổi phát màu điến magenta (tím ngả đi). Bạn chốt định chỉnh code nào hệ chạy tuỳ chèn nó vô file code tự làm tô màu làm nổi khung cần theo Hue luôn được.
- Saturation: Tính giá mầu qua hàm tên hash hash function name của hàm trả code độ phủ bóng băm (hashed). Hỗ tính tách lập độ trích gần đệm kề (towers) đồng thì mang lưu được khung màu tuân thủ tại khung flame graph theo một màu không sai cho nhiều graph chạy riêng coi luôn (so chuẩn 2 cái nhiều khi cũng chả sao phân vân cả).
- Background color: (Đổ bg nền) Đừng cho background màu rối báo type graph do thiết đó là gì thôi. Default cho mầu xám yellow đo cpu chạy, off-cpu hay graph của i/o lấy cái màu thiên blue, memory đập qua màu green.

Bảng đồ theo IPC tính màu đong cũng đáng giá ở IPC theo lệnh đo ngắt đồ đo gradient ngả từ lam -> qua -> lục / vọt (blue to white to red).

**Tính tương tác (Interactivity)**
Có tính năng tác ở biểu Flame. Lệnh nguyên thủ code hàm `flamegraph.pl` nó bắn định ra `SVG` mã gộp chung `JavaScript` nhúng. Lúc trình web đẩy cấu đồ cho thấy bạn múa con trỏ lướt nhẹ các elements hiển phần báo giải của nó dưới footer cho hàm tương tác khác. Hình ví dụ 6.21 có điểm highlight ở `start_xmit()` để hiển thị có trong 72.55% mốc báo stacks rỗi đếm hàm.

Bằng 1 phím click nhấp thì nó phóng cái biểu hàm (to zoom), hoặc Ctr+F lùng đoạn mục gõ gọi kiếm chữ term báo tìm thì biểu sẽ dán mốc trăm trích tìm ra bao tần hiện ra ngắt tìm của stacks đâm có điểm đó thôi. Thấy đong coi luôn xem profile tính mất đâu cái mã phần chạy hệ lọt khu vực lệnh gì đó. (vd: gọi gõ lệnh "tcp_" -> hệ bôi xuất lượng thời chiếm chỗ vào khung mã tcp kernel tcp node kia).

**Diễn giải (Interpretation)**
Hướng dùng tham thông flame biểu hãy lấy ví cho cấu cpu rỗng giả tạo synthetic Flame graph đo lấy Hình 6.22 ở dòng kia đi coi thử nhé:
Dấu thanh cắt trên vạch nổi chóp định ngọn đã đánh dấu đỉnh chỉ rằng có bộ hàm chạy tức ngắt hàm trích của nó trích `func_c()` (70% thời gian đo system on-cpu), còn ngắt `func_b()` (20%), với ngắt lệnh báo đếm `func_e()` (10%). `func_a()` & ngắt lệnh `func_d()` thì chưa hề nhảy on-cpu qua hệ trace sample bao chừ.

Hãy đi dạo qua độ béo to khung nhấp chóp mập to trước của Flame Graph rành trước nhé lúc biểu diễn xem rồi coi tiếp nha. Dựa vô Hình 6.22 kia sẽ là đường rễ path: `func_a() -> func_b() -> ...func_c()`. Bãi rộng chóp cuối của `iowrite16()` cho cái Flame graph dòng hình bãi 6.21 đó.

Bộ lượng khung đếm của ngàn ngắt thì sẽ chia bé mảnh quá khung đâm chẳng trích nhét nổi tên cho khung nên rỗng. Ghi như vậy cho mình sẽ để con mắt mình dồn cho mảng hàm lấn rộng phình nhất khung biểu dễ theo mà lột được nguyên dạng gốc gác đằng hàm xử trước đã.
(Tuyến hàm truy khứ lặp recursive thì bị tạo mỗi nấc khung riêng dội khung đệm level 1 mà ngắt nha).

Trích 6.5.4 xem Lập Cpu Profiling và `6.6.13` để coi code đẻ ra đồ hình (perf tạo biểu flame).

### 6.7.4 FlameScope

Tool được phát và xây tại Netflix (open-source) cấu dựng tích hoà (marries) cả bộ dạng subsecond-offset heat map nhập với flame graphs kia. Báo cho đoạn khung 1 biểu profile đo rồi chèn bộ nhúng lấy khung rẽ time-offset chỉ biểu diễn qua bằng flame graph đồ hình ngay phạm trọn ở khoảng thời độ ngắt range chọn được. Khung 6.23 minh chứng bằng FlameScope và ghi phụ báo cho hàm đồ heat map.

Nghiên xét các đâm phá đứt đứt nghẽn chập và rung của hiệu biến đo chạy dùng FlameScope là chuẩn nhé. Nét vệt chỉ nhoè 100 ms nháy ngang cho 1 đo 30 giây cpu profile ngợp bảng chỉ gộp mất tầm 0.3% bề hoành khung biểu qua flame graph (đôi khi không trích do nó bị mảnh quá). Ngược đường cho Flamescope biểu biến báo vạch lôi xéo dọc đâm 1/10 dãi độ của trục đo. Nhiều cái kiểu quấy như vậy xuất rõ trên hình ngắt 6.23 kia. Lựa trích range dãi nhúng bôi xanh ở thanh cột báo ra mã chấu theo rãnh Flame cho chuỗi ứng ngay khoảng đó để chẻ nhỏ rãnh ngực đứt do mã gãy khúc nào (code paths responsible).

Hệ ứng từ Netflix nguồn báo phát cho hệ open source giúp dò thành tích lỗi ở đó rồi (Hình FlameScope).

## 6.8 Thực nghiệm (Experimentation)

Khoản lục mục hệ trình mô diễn tools kiểm thử test CPU performance hiệu năng được mô. Tìm 6.5.11 (Micro-Benchmarking) bổ thêm thông kiến nền. Dùng kiểm tra với đong nhịp cpu rễ (`mpstat(1)`) báo để cấu tải và đồng chạy khi dùng nha.

### 6.8.1 Ad Hoc

Tạo lặp chuỗi một chu trình kiểm không truy trích số liệu nhưng có hiệu nghiệm mảng check luồng thử xem báo cụ quan có hoạt trích số hệ trả số chính tính cho trích tool chớ chả phải vớ vẩn thì là ví dạng chạy đong ngắt (hot on one CPU) dùng rỗng đơn luồng (single-threaded) cpu-bound này:

```
# while :; do :; done &
```
Là kịch gọi vô cực lặp vô hạn ở bash loop ngầm dưới nền thui mà (bourn shell background run). Dùng tuỳ hứng xong bạn giết process khi thoả việc của xong là ngưng đó mà.

### 6.8.2 SysBench
Hệ khung tiện benchmarks ở cấu hình `SysBench` có 1 CPU benchmark nhỏ kiểm để làm thuật trích hệ prime numbers (số nguyên tố).
Ví dụ:
```
# sysbench --num-threads=8 --test=cpu --cpu-max-prime=100000 run
sysbench 0.4.12:  multi-threaded system evaluation benchmark

Running the test with following options:
Number of threads: 8

Doing CPU performance benchmark

Threads started!
Done.

Maximum prime number checked in CPU test: 100000

Test execution summary:
    total time:                          30.4125s
    total number of events:              10000
    total time taken by event execution: 243.2310
    per-request statistics:
         min:                                 24.31ms
         avg:                                 24.32ms
         max:                                 32.44ms
         approx.  95 percentile:              24.32ms

Threads fairness:
    events (avg/stddev):           1250.0000/1.22
    execution time (avg/stddev):   30.4039/0.01
```
Trích 8 thread ở ví, ngưỡng max đỉnh trích ngắt đong là giới nguyên tố ở 100,000 (prime numbers check maximum). Runtime đạt 30.4 s để mà coi lấy so đối cho cấu hình phần tải số liệu server/nhân (so chuẩn là code dùng cấu điều biên build bằng các module biên biên dịch tool (compiler options) cùng giống ngắt với nhau - ngó Chương 12 (Benchmarking)).


## 6.9 Tinh chỉnh (Tuning)

Đối với CPU, những chiến thắng lớn nhất về hiệu năng thường là những thứ loại bỏ được các công việc không cần thiết, đây là một hình thức tinh chỉnh hiệu quả. Phần 6.5, Phương pháp luận, và Phần 6.6, Các công cụ quan sát, đã giới thiệu nhiều cách để phân tích và xác định công việc được thực hiện, giúp bạn tìm ra bất kỳ công việc nào không cần thiết. Các phương pháp luận khác cho việc tinh chỉnh cũng đã được giới thiệu: tinh chỉnh độ ưu tiên (priority tuning) và liên kết CPU (CPU binding). Phần này bao gồm những ví dụ tinh chỉnh này và các ví dụ khác.

Các chi tiết cụ thể của việc tinh chỉnh—các tùy chọn có sẵn và đặt chúng thành gì—phụ thuộc vào loại bộ xử lý, phiên bản hệ điều hành và khối lượng công việc dự kiến. Những điều sau đây, được tổ chức theo loại, cung cấp các ví dụ về những tùy chọn nào có thể có sẵn và cách chúng được tinh chỉnh. Các phần phương pháp luận trước đó cung cấp hướng dẫn về thời điểm và lý do tại sao những tùy chọn này sẽ được tinh chỉnh.

### 6.9.1 Các tùy chọn Trình biên dịch (Compiler Options)

Các trình biên dịch, và các tùy chọn mà chúng cung cấp để tối ưu hóa mã, có thể có tác động đáng kể đến hiệu năng CPU. Các tùy chọn phổ biến bao gồm biên dịch cho 64-bit thay vì 32-bit, và chọn một mức độ tối ưu hóa. Tối ưu hóa trình biên dịch được thảo luận trong Chương 5, Ứng dụng.

### 6.9.2 Độ ưu tiên Lập lịch và Lớp (Scheduling Priority and Class)

Lệnh `nice(1)` có thể được sử dụng để điều chỉnh độ ưu tiên của tiến trình. Các giá trị nice dương làm giảm độ ưu tiên, và các giá trị nice âm (mà chỉ siêu người dùng - superuser mới có thể đặt) làm tăng độ ưu tiên. Phạm vi là từ -20 đến +19. Ví dụ:

```
$ nice -n 19 command
```

Chạy lệnh với giá trị nice là 19—độ ưu tiên thấp nhất mà `nice` có thể đặt. Để thay đổi độ ưu tiên của một tiến trình đang chạy, hãy sử dụng `renice(1)`.

Trên Linux, lệnh `chrt(1)` có thể hiển thị và thiết lập độ ưu tiên lập lịch trực tiếp, và chính sách lập lịch (scheduling policy). Ví dụ:

```
$ chrt -b command
```

Sẽ chạy lệnh trong `SCHED_BATCH` (xem Các lớp Lập lịch trong Phần 6.4.2, Phần mềm).
Cả `nice(1)` và `chrt(1)` cũng có thể được hướng vào một PID thay vì khởi chạy một lệnh (xem các trang man page của chúng).

Độ ưu tiên lập lịch cũng có thể được thiết lập trực tiếp bằng syscall `setpriority(2)`, và độ ưu tiên cùng chính sách lập lịch có thể được thiết lập bằng syscall `sched_setscheduler(2)`.

### 6.9.3 Tùy chọn Bộ lập lịch (Scheduler Options)

Nhân (kernel) của bạn có thể cung cấp các tham số có thể điều chỉnh để kiểm soát hành vi của bộ lập lịch, mặc dù không có khả năng là những tham số này sẽ cần được tinh chỉnh.

Trên các hệ thống Linux, các tùy chọn `CONFIG` khác nhau kiểm soát hành vi cục bộ của bộ lập lịch ở mức cấp cao và có thể thiết lập cờ này từ lúc biên dịch nhân kernel (kernel compilation). Ví dụ như Bảng 6.12 có tùy chọn trích trên Linux 5.3 và Ubuntu 19.10:

**Bảng 6.12 Tùy chọn CONFIG bộ lập lịch cho Linux**

| Tùy chọn | Mặc định | Mô tả |
|----------|----------|-------|
| `CONFIG_CGROUP_SCHED` | y | Nhóm các mã task processes, cấu chỉ định CPU chạy dựa trên mốc nhóm. |
| `CONFIG_FAIR_GROUP_SCHED` | y | Gói CFS task vào group nhóm. |
| `CONFIG_RT_GROUP_SCHED` | n | Nhóm gộp real-time tasks vô với nhau. |
| `CONFIG_SCHED_AUTOGROUP` | y | Gộp và dựng tự động nhóm task processes (như build job). |
| `CONFIG_SCHED_SMT` | y | Lõi hỗ trợ cấu dòng hyperthreading. |
| `CONFIG_SCHED_MC` | y | Tính chạy Multicore. |
| `CONFIG_HZ` | 250 | Mốc thiết độ dao động xung nhịp timer báo bộ interrupt đồng hồ OS. |
| `CONFIG_NO_HZ` | y | Nhịp đồng hồ Tickless. |
| `CONFIG_SCHED_HRTICK` | y | Giao thức thời hồ hỗ trợ High-resolution timers. |
| `CONFIG_PREEMPT` | n | Ngắt tài nguyên cấu trọn full nhân (full kernel preemption) (Cấu trừ những điểm lock do spin lock cũng như hàm interrupt chèn). |
| `CONFIG_PREEMPT_NONE` | n | Tắt tiền ngắt No preemption. |
| `CONFIG_PREEMPT_VOLUNTARY` | y | Dựng ở tự phát (voluntary) Kernel preemption. |

Cũng có những phần hệ tham số điều bộ cấu lịch qua biến lập `sysctl(8)` chỉnh sửa thay trong phiên vận hành máy sống ảo. Cho danh lục ở Bảng hệ 6.13 là từ Ubuntu:

**Bảng 6.13 Tùy chọn biến cấu cấu chỉnh qua sysctl(8) của bộ lịch**

| sysctl | Mặc định | Mô tả |
|--------|----------|-------|
| `kernel.sched_cfs_bandwidth_slice_us` | 5000 | Định mức thời tính khối lượng chạy chia cho băng tính hệ lượng CFS. |
| `kernel.sched_latency_ns` | 12000000 | Độ chậm chờ ngắt mục tiêu giới lượng. Cái này độ càng nống lên tăng sẽ dội giờ ứng chạy có time on-CPU trồi nhưng bù qua chịu chậm latency preemption. |
| `kernel.sched_migration_cost_ns` | 500000 | Phí độ do đổi dịch task hệ, dùng check dải tính (affinity config). Cái task nào rẽ sang hoạt thời gian trồi độ kia là đánh bị "cache hot". |
| `kernel.sched_nr_migrate` | 32 | Giới chừng bao task hệ chuyển đợt nhằm chuyển hệ tài chia gánh cân load. |
| `kernel.sched_schedstats` | 0 | Chạy chế mở thêm biến thống số phụ đo cấu cho bộ lập lịch, (dạng tracepoint như `sched:sched_stat*`). |

`sysctl(8)` đổi các biến hệ bằng thư `/proc/sys/sched`.

### 6.9.4 Thống đốc Tỉ lệ (Scaling Governors)

Linux hỗ cấu loại hệ điều bộ cpu độ tốc đồng hồ khác hệ thống governor cấp điều trích qua hệ (software The kernel). Cái nì cấu tuỳ thông theo chỉnh tập file thuộc thư cấp của `/sys`. Đo mẫu với báo thông biến CPU thứ `0`:

```
# cat /sys/devices/system/cpu/cpufreq/policy0/scaling_available_governors
performance powersave
# cat /sys/devices/system/cpu/cpufreq/policy0/scaling_governor
powersave
```
Chưa bật tính chạy governor: Hệ báo "powersave", mốc chạy với ép nhịp chu clock CPU số đong giảm mức xung giữ năng tiết điện. Cấp chuyển lên max cho "performance" lấy cho maximum cấu hiệu quả tần hệ cao tối kịch:

```
# echo performance > /sys/devices/system/cpu/cpufreq/policy0/scaling_governor
```

Để đổi mốc cần thi hành dải cpu khác cho bằng hết từ máy (`policy0..N`). Cụm file policy bao trong các tập đổi speed giới cho xung min với max hệ set bằng `scaling_setspeed`, hay dò `scaling_min_freq`, `scaling_max_freq`.

Ép bộ chạy maximum frequency đôi lúc bắt máy đài thọ nguồn gánh kinh tổn thiên môi nhiên trường năng vĩ. Thế nếu cắm cái mấu setting báo nó chạy cũng chả kéo chênh cấu cao hiệu ứng chênh năng bao lăm hiệu thì kệ nó hãy set để lại cho bộ chạy `powersave` đặng dung thứ cho địa trạch chúng sinh với (*Cước ghi: Đo báo số mức trích power host thường vẫn thiếu bao cấp tải chi số cho đồ công hoà không tủ nhiệt, làm hệ bảo sản vận hay di vận hao đồ*). Mấy máy cho khách cấu quyền móc thông MSRs mức tính số báo nguồn điện cho hệ CPU theo không thiết chấu hay không cho max giới độ frequency setting. Có chi thì đặng đo số môi sinh.

### 6.9.5 Trạng thái Năng lượng (Power States)

Tăng cấp và hạ dập cấu trạng hoạt công lực của chip (power states do bộ CPU chạy) lấy từ lệnh của tools do `cpupower(1)` làm. Xem tại cấu phần 6.6.21 Công tools khác để ngắt ngủ (sleep states deeper) làm trễ khá cho độ lỡ rút trễ rút wakeup (VD 890 micro giây tại trạng ngắt của hệ `C10`). Lấy rút state từ ngắt `-d`, ngắt cờ `-D latency` dập luôn dãi hệ làm ngắt dãi độ do cao lên hạn độ latency ngắt thoát lúc ra đụng đó theo trích số (vi tính đo micro-second). Cấu thế là cho để ngắt trạng ngủ mà lại rườm ngắt quá thể độ delay latency nha.

### 6.9.6 Gắn kết CPU (CPU Binding)

Móc neo ngắt dính vào từng dải hay một hệ con chip của tiến bộ cpu vào 1 OS process process gíp tối hiệu năng làm vì đẩy ưu hiệu độ ngâm độ ủ nhiệt hệ rò trong bộ nhớ tạm cache, chắp tính thông bộ memory gọi liền vùng gần.

Trên dòng như OS mã Linux, cái làm đó được tạo với lệnh ngắt của `taskset(1)`, thiết ngắt qua mã bit gọi báo mặt bộ (CPU mask), gãi mảng dãi range lấy giá trị đong biến liên dãi bộ (cpu affinity). Đo qua tỷ thử:

```
$ taskset -pc 7-10 10790
pid 10790's current affinity list: 0-15
pid 10790's new affinity list: 7-10
```

Bấm cho bộ PID số 10790 móc lấy số CPU cấp số gọi từ dải dòng cpu 7 đo đi đến 10.

Trình `numactl(8)` hỗ chạy cấu hệ móc gắn này cùng memory hệ node bộ nhớ (dò chương 7 (Memory) hệ phần mục 7.6.4 (NUMA Binding)).

### 6.9.7 Tập hợp CPU Độc quyền (Exclusive CPU Sets)

Cấu Linux gọi dùng với `cpusets`, gộp cho đám nhóm cụm tiến thiết với đính quy trình tiến OS process chung. Thiết lập chạy được thêm lợi đặng tốt ngang cpu binding thế kia nha mà cpusets đong bồi thêm quả hiệu cấu quyền làm chốt chặn bằng (exclusive), ngáng tiến process ngoại đi dùng nhóm đấy. Bất trắc chịu trả ngược bằng sự cấp của bầy CPU đong bị giảm hệ thù dư cấu dành bối ra để cho chung các mã làm kia nhé.

Tạo exclusive gọi cpusets trên:

```
# mount -t cgroup -ocpuset cpuset /sys/fs/cgroup/cpuset         # có thể không cần thiết
# cd /sys/fs/cgroup/cpuset
# mkdir prodset                        # tạo một cpuset gọi là "prodset"
# cd prodset
# echo 7-10 > cpuset.cpus              # gán các CPU từ 7-10
# echo 1 > cpuset.cpu_exclusive        # đặt prodset thành độc quyền (exclusive)
# echo 1159 > tasks                    # gán PID 1159 cho prodset
```

Để tham khảo, xem man page `cpuset(7)`.

Khi tạo các bộ cấp cấu tập CPU gộp, cần tra bộ hệ các cpu ngoài coi số nào lo được các biến gánh chia ngắt trả ngắt cờ do hardware (interrupts/IRQ). Cái tiến dải quỷ hệ điều chia interrupt ngắt được xử bởi (`irqbalance(1)` daemon) giúp chuyển số các interrupte dãi đếm ở cpu đặng chạy dãn tài hiệu. Thế nhưng mình có tuỳ manual theo phân cấp nhấp vào config tệp theo hàm qua file bộ nhớ (`/proc/irq/IRQ/smp_affinity`).

### 6.9.8 Kiểm soát Tài nguyên (Resource Controls)

Ngoài việc chạy thiết gắn gộp móc các dòng luồng vào 1 dòng trọn số OS CPU rễ, những môi cấu hệ HDH thế mới có phân tài chia mảnh gắt (fine-grained allocation) giới cho cpu usage.

Riêng theo OS phần Linux có cái điều khiển kiểm tra cục bầy cục (control groups hay đo là `cgroups`), cấu làm thông cho dải mức tải các nhóm nhóm con cho tiến OS quá mã process đong theo OS process list hay bộ nhóm hệ. Chỗ tính dùng CPU chỉnh nhờ hệ shares số, của cờ hệ cấp độ biểu định CFS scheduler đâm định ngạch mốc múc được cấp tính bằng số CPU bandwidth chạy qua chỉ của đếm giây (microseconds tính lượng chu của 1 thời khoản / interval gọi trích).

Để ví dùng cụ cấu hệ này của cấu thuê máy phần nhóm HDH (OS VMs), chia các OS shares để ép limit sử lượng tải chèn CPU ở nhau tuỳ hệ chung chạ trong đám thiết ảo cấu thì dòm OS Cloud Computing (chương 11).

### 6.9.9 Các tùy chọn Khởi động Bảo mật (Security Boot Options)

Có một dải trích những điểm ráo riếc che hệ yếu kẽ cho bộ bảo hệ thống báo lùng lỗi qua kẽ hở an toàn Meltdown và dòng Spectre dội lỗi cho giảm nhẹ thông báo nhân kernel mitigations có hiệu ứng lây đứt phụ chèn kềm chân cấu đo chèn tụt độ chạy hiệu suất của bạn (reducing performance). Cấu trích theo chỗ ở tình tiết này cũng lúc bảo tính không màng hệ thiết bắt cần nhưng cấu ưu đo là dội ở tốc lực cao đỉnh nên mình rút bỏ (disable) cờ chèn ngắt hệ dặm gánh ấy cho rảnh tay chạy đê. Cũng như nói theo đây là việc khuyến nghịch nên làm do cờ tính độ thủ rách rất to nên đoạn tôi không đưa nạp bầy bản lồng chít vô tuỳ này đây cả (chỉ nháy để anh coi thôi nghen). Mấy mục chỉnh dòng menu cho Grub của tuỳ chọn là cờ đính bỏ qua các báo spectre (nospectre_v1 và nospectre_v2). Liệt trích từ hệ OS Linux qua tệp (`Documentation/admin-guide/kernel-parameters.txt`) theo đoạn [Linux 20f] sau đây:

```
nospectre_v1      [PPC] Tắt các điểm trích gỡ bẫy kẽ do bọ dính kẽ Spectre Variant 1
                  (lỗi hệ check bypass). Bật mục sẽ làm rách dò dữ chui ra dải.

nospectre_v2      [X86,PPC_FSL_BOOK3E,ARM64] Tắt toàn kẽ điểm dặn bẫy chặn với variant
                  2 (spectre variant 2 - lỗ rách bọ hệ do luồn qua ngầm mảng báo rẽ nhành
                  chỉ mạch sai hàm do chạy đo - indirect branch prediction).
                  Cũng sẽ tạo đòn rỉ rụng dũ ra lỗ hệ làm tuồn báo data info leaks.
```
Cái này ghi lùng qua web `https://make-linux-fast-again.com` thì là liệt báo thôi chứ ko lùng dải warning dạn lời cho bạn nhé.

### 6.9.10 Tùy chọn Bộ xử lý (Tinh chỉnh BIOS)

Cấu tuỳ trong hệ tinh chip cung cấp các dọi dãi cho đặt cài và ngắt làm tắt và thiết vi thông những cấu cờ tại điểm (processor-level features). Hỗ cấu chip cho kiến phần x86 thiết sẽ chỉnh sửa thiết lập BIOS settings đo hệ setup tuỳ đoạn màn boot time thui.

Nó default trọn chẽ hiệu sức gồng tối max cho cài rồi để tuỳ chỉnh cái hệ đâm đo. Hệ ngắt lớn lý cớ nhất làm ở thời nay là tôi đập tịt cho báo Intel Turbo Boost thui, đặng thế lúc làm benchmark truy dò điểm cpu đo bằng các đồ thị clock báo rễ tần cùng một mức đặng xem (nhưng có coi chạy bộ cấp đo production dùng thật ngó bật dãi nhịp ngắt đó lên hệ nhấp để rút ngắn trích giây đâm lên hệ rẽ nha bạn).

## 6.10 Bài tập (Exercises)

1. Hãy giải các hàm mốc đo thuật cho dòng của CPU sau đây:
   - Sự khác biệt giữa một bộ vi xử lý (processor) và một tiến trình (process) là gì?
   - Một luồng phần cứng (hardware thread) là gì?
   - Hàng đợi chạy (run queue) là gì?
   - Sự khác biệt giữa thời gian không gian người dùng (user time) và thời gian nhân (kernel time) là gì?

2. Trả lời các câu hỏi về khái niệm sau:
   - Mô tả độ sử dụng (utilization) và độ bão hòa (saturation) của CPU.
   - Mô tả cách quy trình ống lệnh (instruction pipeline) cải thiện thông lượng CPU.
   - Mô tả cách độ rộng lệnh bộ xử lý (processor instruction width) cải thiện thông lượng CPU.
   - Mô tả các ưu điểm của mô hình đa tiến trình (multiprocess) và đa luồng (multithreaded).

3. Trả lời các câu hỏi sâu hơn sau:
   - Mô tả điều gì xảy ra khi các CPU của hệ thống bị quá tải với các công việc có thể chạy (runnable work), bao gồm ảnh hưởng đến hiệu năng của ứng dụng.
   - Khi không có công việc có thể chạy nào để thực hiện, các CPU làm gì?
   - Khi được giao một vấn đề nghi ngờ về hiệu năng CPU, hãy nêu tên hai phương pháp luận bạn sẽ sử dụng ở giai đoạn đầu phân tích, và giải thích tại sao.

4. Phát triển các quy trình sau cho môi trường của bạn:
   - Một danh sách kiểm tra phương pháp USE cho các tài nguyên CPU. Bao gồm cách lấy mỗi số liệu (ví dụ, thực thi lệnh nào) và cách giải thích kết quả. Cố gắng sử dụng các công cụ quan sát OS có sẵn trước khi cài đặt hoặc sử dụng các sản phẩm phần mềm bổ sung.
   - Một danh sách kiểm tra đặc tả khối lượng công việc (workload characterization) cho tài nguyên CPU. Bao gồm cách lấy mỗi số liệu và cố gắng sử dụng các công cụ quan sát OS có sẵn trước.

5. Thực hiện các tác vụ sau:
   - Tính tải trung bình (load average) cho hệ thống sau, với tải đang ở trạng thái ổn định, không có tải disk/lock đáng kể nào:
     - Hệ thống có 64 CPU.
     - Độ tải (utilization) toàn hệ thống là 50%.
     - Độ bão hòa (saturation) toàn hệ thống, đo lường bằng tổng số các luồng đang chạy và các luồng nằm ở hàng đợi đợi chạy trung bình là 2.0.
   - Chọn một ứng dụng và phân tích (profile) mức độ sử dụng CPU không gian người dùng (user-level) của nó. Xem đoạn code nào tiêu thụ nhiều sức mạnh CPU nhất.

6. (Tùy chọn, nâng cao) Hãy tạo ra công cụ `bustop(1)`—một công cụ hiển thị hiệu suất độ hoạt động của các nút liên kết hay bus vật lý (với một cách hiển thị tương tự như lệnh `iostat(1)`): biểu danh sách list buses, các cột phân bố tải thông lượng (throughput) trên từng 2 cung đường hai phía (each direction), cùng độ dụng (utilization). Đi cùng đó là thông số cho điểm bão hoà (saturation) cùng lượng rớt mắc lỗi (error metrics) nếu có tính năng đo nổi được. Công cụ này phải dùng truy dò từ phần cứng qua PMC.

## 6.11 Tài liệu tham khảo (References)

[Saltzer 70] Saltzer, J., và Gintell, J., “The Instrumentation of Multics,” Communications of the ACM, tháng 8 năm 1970.

[Bobrow 72] Bobrow, D. G., Burchfiel, J. D., Murphy, D. L., và Tomlinson, R. S., “TENEX: A Paged Time Sharing System for the PDP-10*,” Communications of the ACM, tháng 3 năm 1972.

[Myer 73] Myer, T. H., Barnaby, J. R., và Plummer, W. W., TENEX Executive Manual, Bolt, Baranek and Newman, Inc., tháng 4 năm 1973.

[Thomas 73] Thomas, B., “RFC 546: TENEX Load Averages for July 1973,” Network Working Group, http://tools.ietf.org/html/rfc546, 1973.

[TUHS 73] “V4,” The Unix Heritage Society, http://minnie.tuhs.org/cgi-bin/utree.pl?file=V4, các tài liệu từ năm 1973.

[Hinnant 84] Hinnant, D., “Benchmarking UNIX Systems,” Tạp chí BYTE số 9, kỳ 8, tháng 8 năm 1984.

[Bulpin 05] Bulpin, J., và Pratt, I., “Hyper-Threading Aware Process Scheduling Heuristics,” USENIX, 2005.

[Corbet 06a] Corbet, J., “Priority inheritance in the kernel,” LWN.net, http://lwn.net/Articles/178253, 2006.

[Otto 06] Otto, E., “Temperature-Aware Operating System Scheduling,” Đại học Virginia (Thesis), 2006.

[Ruggiero 08] Ruggiero, J., “Measuring Cache and Memory Latency and CPU to Memory Bandwidth,” Intel (Whitepaper), 2008.

[Intel 09] “An Introduction to the Intel QuickPath Interconnect,” Intel (Whitepaper), 2009.

[Levinthal 09] Levinthal, D., “Performance Analysis Guide for Intel® Core™ i7 Processor and Intel® Xeon™ 5500 Processors,” Intel (Whitepaper), 2009.

[Gregg 10a] Gregg, B., “Visualizing System Latency,” Communications of the ACM, tháng 7 năm 2010.

[Weaver 11] Weaver, V., “The Unofficial Linux Perf Events Web-Page,” http://web.eece.maine.edu/~vweaver/projects/perf_events, 2011.

[McVoy 12] McVoy, L., “LMbench - Tools for Performance Analysis,” http://www.bitmover.com/lmbench, 2012.

[Stevens 13] Stevens, W. R., và Rago, S., Advanced Programming in the UNIX Environment, Ấn bản lần 3, Addison-Wesley 2013.

[Perf 15] “Tutorial: Linux kernel profiling with perf,” perf wiki, https://perf.wiki.kernel.org/index.php/Tutorial, cập nhật lần cuối năm 2015.

[Gregg 16b] Gregg, B., “The Flame Graph,” Communications of the ACM, Tập số 59, Bản kỳ 6, trang 48–57, tháng 6 năm 2016.

[ACPI 17] Advanced Configuration and Power Interface (ACPI) Specification, https://uefi.org/sites/default/files/resources/ACPI%206_2_A_Sept29.pdf, 2017.

[Gregg 17b] Gregg, B., “CPU Utilization Is Wrong,” http://www.brendangregg.com/blog/2017-05-09/cpu-utilization-is-wrong.html, 2017.

[Gregg 17c] Gregg, B., “Linux Load Averages: Solving the Mystery,” http://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html, 2017.

[Mulnix 17] Mulnix, D., “Intel® Xeon® Processor Scalable Family Technical Overview,” https://software.intel.com/en-us/articles/intel-xeon-processor-scalable-family-technical-overview, 2017.

[Gregg 18b] Gregg, B., “Netflix FlameScope,” Netflix Technology Blog, https://netflixtechblog.com/netflix-flamescope-a57ca19d47bb, 2018.

[Ather 19] Ather, A., “General Purpose GPU Computing,” http://techblog.cloudperf.net/2019/12/general-purpose-gpu-computing.html, 2019.

[Gregg 19] Gregg, B., BPF Performance Tools: Linux System and Application Observability, Addison-Wesley, 2019.

[Intel 19a] Intel 64 and IA-32 Architectures Software Developer’s Manual, Các tập kết hợp 1, 2A, 2B, 2C, 3A, 3B, và 3C. Intel, 2019.

[Intel 19b] Intel 64 and IA-32 Architectures Software Developer’s Manual, Tập 3B, System Programming Guide, Phần 2. Intel, 2019.

[Netflix 19] “FlameScope Is a Visualization Tool for Exploring Different Time Ranges as Flame Graphs,” https://github.com/Netflix/flamescope, 2019.

[Wysocki 19] Wysocki, R., “CPU Idle Time Management,” Tài liệu Linux, https://www.kernel.org/doc/html/latest/driver-api/pm/cpuidle.html, 2019.

[AMD 20] “AMD μProf,” https://developer.amd.com/amd-uprof, truy cập 2020.

[Gregg 20d] Gregg, B., “MSR Cloud Tools,” https://github.com/brendangregg/msr-cloud-tools, cập nhật lần cuối năm 2020.

[Gregg 20e] Gregg, B., “PMC (Performance Monitoring Counter) Tools for the Cloud,” https://github.com/brendangregg/pmc-cloud-tools, cập nhật lần cuối năm 2020.

[Gregg 20f] Gregg, B., “perf Examples,” http://www.brendangregg.com/perf.html, truy cập 2020.

[Gregg 20g] Gregg, B., “FlameGraph: Stack Trace Visualizer,” https://github.com/brendangregg/FlameGraph, cập nhật lần cuối năm 2020.

[Intel 20a] “Product Specifications,” https://ark.intel.com, truy cập 2020.

[Intel 20b] “Intel® VTune™ Profiler,” https://software.intel.com/content/www/us/en/develop/tools/vtune-profiler.html, truy cập 2020.

[Iovisor 20a] “bpftrace: High-level Tracing Language for Linux eBPF,” https://github.com/iovisor/bpftrace, cập nhật lần cuối năm 2020.

[Linux 20f] “The Kernel’s Command-Line Parameters,” Tài liệu Linux, https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html, truy cập 2020.

[Spier 20a] Spier, M., “A D3.js Plugin That Produces Flame Graphs from Hierarchical Data,” https://github.com/spiermar/d3-flame-graph, cập nhật lần cuối năm 2020.

[Spier 20b] Spier, M., “Template,” https://github.com/spiermar/d3-flame-graph#template, cập nhật lần cuối năm 2020.

[Valgrind 20] “Valgrind Documentation,” http://valgrind.org/docs/manual, tháng 5 năm 2020.

[Verma 20] Verma, A., “CUDA Cores vs Stream Processors Explained,” https://graphicscardhub.com/cuda-cores-vs-stream-processors, 2020.
