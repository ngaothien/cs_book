550
11.1 Sự gia tốc Các nguyên tắc cơ bản (Acceleration Fundamentals)
Phần cứng sự gia tốc bật
máy trục (Hardware acceleration turns on the machine axis).
Sự học hỏi Các mục tiêu (Learning Objectives)
• Giải thích phần cứng sự gia tốc như máy-trục sự chuyên biệt hóa cho tensor các khối lượng công việc, dữ liệu sự tái sử dụng, và hiệu suất trên watt (Explain hardware acceleration as machine-axis specialization for tensor workloads, data reuse, and performance per watt)
• Tính toán số học cường độ và roofline các trần nhà để phân loại các hạt nhân như bị ràng buộc-bởi-tính toán hoặc bị ràng buộc-bởi-bộ nhớ (Calculate arithmetic intensity and roofline ceilings to classify kernels as compute bound or memory bound)
• Chẩn đoán bộ nhớ-bức tường các nút thắt cổ chai việc sử dụng băng thông, bộ nhớ đệm hệ thống phân cấp, máy chủ-thiết bị sự truyền, và năng lượng-sự di chuyển các chi phí (Diagnose memory-wall bottlenecks using bandwidth, cache hierarchy, host-device transfer, and energy-movement costs)
• So sánh Tensor Các lõi, tâm thu các mảng, SIMD/SIMT các đơn vị, và thưa thớt sự thực thi cho ML tính toán các nguyên thủy (Compare Tensor Cores, systolic arrays, SIMD/SIMT units, and sparse execution for ML compute primitives)
• Chọn dòng dữ liệu, sự lợp ngói, và sự ánh xạ các chiến lược thứ mà tối đa hóa sự tái sử dụng dưới bộ nhớ-dung lượng các sự ràng buộc (Select dataflow, tiling, and mapping strategies that maximize reuse under memory-capacity constraints)
• Phân tích trình biên dịch và thời gian chạy các sự tối ưu hóa thứ mà hợp nhất các hạt nhân, lập kế hoạch bộ nhớ, và lên lịch các máy gia tốc (Analyze compiler and runtime optimizations that fuse kernels, plan memory, and schedule accelerators)
• Đánh giá máy gia tốc các sự chọn lựa qua thông lượng, độ trễ, năng lượng, chi phí, và sự triển khai-ngữ cảnh các sự ràng buộc (Evaluate accelerator choices across throughput, latency, power, cost, and deployment-context constraints)
11.1 Sự gia tốc Các nguyên tắc cơ bản (Acceleration Fundamentals)
Việc làm giảm bớt các tham số, độ chính xác, hoặc các hoạt động chỉ quan trọng khi máy có thể thực thi kết quả sự đại diện một cách hiệu quả (Reducing parameters, precision, or operations only matters when the machine can execute the resulting representation efficiently). Dữ liệu sự chọn lựa đã làm giảm bớt dữ liệu số hạng, và sự nén đã làm giảm bớt thuật toán của công việc; phần cứng sự gia tốc hỏi máy có thể thực sự phân phối cái gì (Data selection reduced the data term, and compression reduced the algorithm’s work; hardware acceleration asks what the machine can actually deliver). Câu trả lời bắt đầu với bộ nhớ bức tường: số học là rẻ, nhưng việc di chuyển dữ liệu là đắt đỏ (The answer starts with the memory wall: arithmetic is cheap, but moving data is expensive). Trong thời gian một hiện đại máy gia tốc tính toán một ngàn dấu phẩy-động các hoạt động, một đơn giá trị di chuyển từ chính bộ nhớ (In the time a modern accelerator computes a thousand floating-point operations, a single value travels from main memory). Chuyên biệt phần cứng quan trọng bởi vì nó nâng cao tính toán thông lượng trong khi việc tổ chức bộ nhớ, dòng dữ liệu, và sự song song sao cho những số học các đơn vị đó giữ nguyên được nuôi dưỡng (Specialized hardware matters because it raises compute throughput while organizing memory, dataflow, and parallelism so those arithmetic units stay fed).
Định nghĩa 11.1: Phần cứng sự gia tốc (Hardware acceleration)
Phần cứng Sự gia tốc là thực tiễn của việc thay thế đa-mục đích bộ xử lý logic với cụ thể-miền silicon được tối ưu hóa cho thường xuyên tensor các hoạt động của ML các khối lượng công việc, việc đánh đổi tính có thể lập trình cho tính toán mật độ (𝑅peak) và hiệu suất-trên-watt các phần tăng thứ mà song song-dữ liệu ma trận phép nhân có thể khai thác (Hardware Acceleration is the practice of replacing general-purpose processor logic with domain-specific silicon optimized for the regular tensor operations of ML workloads, trading programmability for the compute density (𝑅peak) and performance-per-watt gains that data-parallel matrix multiplication can exploit).
1. Tầm quan trọng: Thông lượng phần tăng là các bậc của độ lớn (Significance: The throughput gain is orders of magnitude). Một A100 GPU phân phối 312 TFLOP/s cho FP16/BF16 ma trận phép nhân, trong khi một cấp-máy chủ CPU phân phối đại khái 1–2 TFLOP/s cho cùng hoạt động, một 156–312× khoảng cách đạt được bởi việc cống hiến 80+ tỷ các transistor cho song song số học các đơn vị thay vì cho nhánh các bộ dự đoán, ngoài-thứ tự các bộ lập lịch, và lớn các bộ nhớ đệm (NVIDIA Corporation 2020; Choquette et al. 2021) (An A100 GPU delivers 312 TFLOP/s for FP16/BF16 matrix multiplication, while a server-class CPU delivers roughly 1–2 TFLOP/s for the same operation, a 156–312× gap achieved by dedicating 80+ billion transistors to parallel arithmetic units rather than to branch predictors, out-of-order schedulers, and large caches (NVIDIA Corporation 2020; Choquette et al. 2021)).
2. Sự khác biệt: Không giống một đa-mục đích CPU, thứ mà được tối ưu hóa để tối thiểu hóa độ trễ cho bất kỳ đơn lệnh trong một tùy ý nối tiếp chương trình, một máy gia tốc được tối ưu hóa để tối đa hóa thông lượng cho một cụ thể hoạt động lớp—có nghĩa là nó đạt được của nó các phần tăng chỉ khi khối lượng công việc xuất trình đủ song song công việc để giữ tất cả số học các đơn vị bận rộn một cách đồng thời (Distinction: Unlike a general-purpose CPU, which is optimized to minimize latency for any single instruction in an arbitrary serial program, an accelerator is optimized to maximize throughput for a specific operation class—meaning it achieves its gains only when the workload presents enough parallel work to keep all arithmetic units busy simultaneously).
3. Phổ biến cạm bẫy: Một thường xuyên sự quan niệm sai lầm là rằng một máy gia tốc của được quảng cáo đỉnh thông lượng là thông lượng một khối lượng công việc nhận được (Common pitfall: A frequent misconception is that an accelerator’s advertised peak throughput is the throughput a workload receives). Được phân phối hiệu suất là thấp hơn của tính toán trần nhà và cái gì bộ nhớ băng thông có thể nuôi dưỡng, roofline sự ràng buộc: một thấp-số học-cường độ hạt nhân có thể ngồi ở một nhỏ phần nhỏ của đỉnh FLOP/s không có vấn đề thế nào nhanh silicon được đánh giá, bởi vì nó chết đói cho dữ liệu thay vì cho số học (Delivered performance is the lower of the compute ceiling and what memory bandwidth can feed, the roofline constraint: a low-arithmetic-intensity kernel can sit at a small fraction of peak FLOP/s no matter how fast the silicon is rated, because it starves for data rather than for arithmetic).
Trước định nghĩa đóng khung chương của trung tâm kỹ thuật sự đánh đổi (The preceding definition frames the chapter’s central engineering trade-off). Đa-mục đích các bộ xử lý cống hiến đáng kể silicon diện tích cho nhánh sự dự đoán, đầu cơ sự thực thi, và phức tạp bộ nhớ đệm sự kết hợp các giao thức (General-purpose processors devote substantial silicon area to branch prediction, speculative execution, and complex cache coherence protocols). Các máy gia tốc tước đi đi đó tính tổng quát, việc lấp đầy khuôn với số học các đơn vị được tinh chỉnh tới thường xuyên, song song-dữ liệu các mẫu thứ mà đặc trưng thần kinh mạng sự tính toán (Accelerators strip away that generality, filling the die with arithmetic units tuned to the regular, data-parallel patterns that characterize neural network computation).

================ PAGE 589 ================

11. Phần cứng Sự gia tốc (Hardware Acceleration)
551
kết quả là bậc-của-độ lớn các sự cải thiện trong thông lượng trên watt cho các khối lượng công việc thứ mà khớp những các mẫu này (The result is order-of-magnitude improvements in throughput per watt for the workloads that match these patterns).
Phần cứng một mình, tuy nhiên, không thể đạt được những các phần tăng này (Hardware alone, however, cannot achieve these gains). Các thuật toán phải được thiết kế để khai thác cái gì phần cứng cung cấp, và phần cứng phải được xây dựng để tăng tốc các hoạt động các thuật toán thực sự sử dụng (The algorithms must be designed to exploit what the hardware offers, and the hardware must be built to accelerate the operations algorithms actually use). Điều này sự cộng sinh thúc đẩy một bổ sung nguyên lý: phần cứng-phần mềm sự đồng thiết kế (This symbiosis motivates a complementary principle: hardware-software co-design).
Định nghĩa 11.2: Phần cứng-phần mềm sự đồng thiết kế (Hardware-software co-design)
Phần cứng-Phần mềm Sự đồng thiết kế là ML máy gia tốc sự phát triển phương pháp luận thứ mà một cách có chủ ý vi phạm truyền thống phần cứng-phần mềm sự trừu tượng các lớp, việc cho phép thuật toán các sự ràng buộc để thông báo silicon thiết kế và phần cứng các khả năng để trực tiếp định hình thuật toán sự hình thành (Hardware-Software Co-design is the ML accelerator development methodology that intentionally violates traditional hardware-software abstraction layers, allowing algorithm constraints to inform silicon design and hardware capabilities to directly shape algorithm formulation).
1. Tầm quan trọng: Sự đồng thiết kế mở khóa các phần tăng không có sẵn tới một trong hai lớp việc hành động một mình (Significance: Co-design unlocks gains unavailable to either layer acting alone). INT8 sự lượng tử hóa có thể phân phối đa-lần thông lượng sự cải thiện không bởi vì 8-bit số học là nhanh hơn trong trừu tượng, nhưng bởi vì hiện đại tensor-lõi các đường dữ liệu đóng gói thấp hơn-độ chính xác các hoạt động một cách dày đặc hơn so với FP32 các hoạt động; thuật toán sự thay đổi mang lại lợi ích chỉ khi phần cứng đã được đồng thiết kế để khai thác nó (NVIDIA Corporation 2020; Dally et al. 2021; Dally 2023) (INT8 quantization can deliver multi-fold throughput improvement not because 8-bit arithmetic is faster in the abstract, but because modern tensor-core datapaths pack lower-precision operations more densely than FP32 operations; the algorithm change pays off only when the hardware was co-designed to exploit it (NVIDIA Corporation 2020; Dally et al. 2021; Dally 2023)).
2. Sự khác biệt: Không giống được xếp lớp sự trừu tượng (nơi phần mềm gọi một phần cứng API mà không có việc biết silicon các chi tiết), sự đồng thiết kế phơi bày phần cứng các sự ràng buộc một cách trực tiếp tới thuật toán và trình biên dịch các tác giả: dữ liệu sự căn chỉnh các yêu cầu, độ chính xác các định dạng, và bộ nhớ truy cập các mẫu tất cả trở nên có thể nhìn thấy các đầu vào tới toàn cầu xuyên-lớp sự tối ưu hóa (Distinction: Unlike layered abstraction (where software calls a hardware API without knowing the silicon details), co-design exposes hardware constraints directly to algorithm and compiler authors: data alignment requirements, precision formats, and memory access patterns all become visible inputs to global cross-layer optimization).
3. Phổ biến cạm bẫy: Một thường xuyên sự quan niệm sai lầm là rằng sự đồng thiết kế là một một-lần phần cứng thiết kế sự chọn lựa (Common pitfall: A frequent misconception is that co-design is a one-time hardware design choice). Trong thực tế, sự đồng thiết kế là một liên tục phản hồi vòng lặp: NVIDIA Tensor Các lõi đã được thiết kế cho FP16 ma trận phép nhân, sau đó được nâng cấp để hỗ trợ TF32 và INT8 sau khi việc quan sát rằng ML các khối lượng công việc đã yêu cầu chúng, sau đó được mở rộng lần nữa tới thưa thớt 2:4 các mẫu sau khi thuật toán sự cắt tỉa nghiên cứu đã chứng minh có cấu trúc sự thưa thớt đã từng có thể đào tạo (NVIDIA 2017; NVIDIA Corporation 2020) (In practice, co-design is a continuous feedback loop: NVIDIA Tensor Cores were designed for FP16 matrix multiply, then upgraded to support TF32 and INT8 after observing that ML workloads demanded them, then extended again to sparse 2:4 patterns after algorithmic pruning research demonstrated structured sparsity was trainable (NVIDIA 2017; NVIDIA Corporation 2020)).
Sự đồng thiết kế giải thích tại sao sự nén các kỹ thuật được giới thiệu trong Chương 10 phân phối thực tế các phần tăng tốc (Co-design explains why the compression techniques introduced in Chapter 10 deliver real speedups). Sự lượng tử hóa các kỹ thuật trong phần 10.4 cho thấy tại sao việc chuyển đổi FP32 tới INT8 mang lại 2–4× sự gia tốc: không bởi vì của ít hơn các bit trong trừu tượng, nhưng bởi vì các máy gia tốc đóng gói đại khái 4× nhiều hơn thấp-độ chính xác các hoạt động vào cùng silicon và di chuyển ít hơn các byte trên mỗi giá trị (NVIDIA Corporation 2020) (The quantization techniques in section 10.4 show why converting FP32 to INT8 yields 2–4× acceleration: not because of fewer bits in the abstract, but because accelerators pack roughly 4× more low-precision operations into the same silicon and move fewer bytes per value (NVIDIA Corporation 2020)). Có cấu trúc sự cắt tỉa cải thiện hiệu suất trong khi không có cấu trúc sự cắt tỉa thường không, bởi vì có cấu trúc các mẫu bảo tồn thường xuyên bộ nhớ truy cập các mẫu thứ mà phần cứng có thể tối ưu hóa (Structured pruning improves performance while unstructured pruning often does not, because structured patterns preserve the regular memory access patterns that hardware can optimize). Sự phân tích bây giờ theo sau đường dẫn từ khối lượng công việc tới silicon: tính toán các nguyên thủy, bộ nhớ các hệ thống, roofline sự chẩn đoán, sự ánh xạ và dòng dữ liệu, sau đó trình biên dịch và thời gian chạy sự hỗ trợ (The analysis now follows the path from workload to silicon: compute primitives, memory systems, roofline diagnosis, mapping and dataflow, then compiler and runtime support).
Lặp lại câu hỏi là tại sao một số hứa hẹn thuật toán các sự tối ưu hóa sống sót sự tiếp xúc với phần cứng trong khi những thứ khác giữ nguyên giấy các sự tiết kiệm (The recurring question is why some promising algorithmic optimizations survive contact with hardware while others remain paper savings).
Định lý 11.1: Cơ bản giới hạn của sự gia tốc (Amdahl của Định luật) (Theorem 11.1: The fundamental limit of acceleration (Amdahl’s Law))
Phần cứng sự gia tốc không tăng tốc toàn bộ hệ thống; nó chỉ tăng tốc có thể song song hóa phần nhỏ (𝑝) (Hardware acceleration does not speed up the entire system; it only speeds up the parallelizable fraction (𝑝)). Điều này là được chi phối bởi Amdahl của Định luật cho AI (Amdahl 1967), được hình thức hóa trong phương trình 11.1 (This is governed by Amdahl’s Law for AI (Amdahl 1967), formalized in equation 11.1):
Phần tăng tốc (Speedup) = 1 / ((1−𝑝) + 𝑝 / 𝐺accel) (11.1)
• Song song phần nhỏ (𝑝): Các ma trận các phép nhân (điển hình 90–99 phần trăm của một ML khối lượng công việc) (Parallel fraction (𝑝): The matrix multiplications (typically 90–99 percent of an ML workload)).
• Máy gia tốc phần tăng (𝐺accel): Thô tốc độ lợi thế của GPU hoặc Tensor Xử lý Đơn vị (TPU) qua CPU cho được tăng tốc phần của khối lượng công việc (Accelerator gain (𝐺accel): The raw speed advantage of the GPU or Tensor Processing Unit (TPU) over the CPU for the accelerated portion of the workload).
• Nối tiếp phần nhỏ (1−𝑝): Dữ liệu việc tải, Python chi phí quản lý, và hạt nhân sự khởi chạy độ trễ (Serial fraction (1−𝑝): Data loading, Python overhead, and kernel launch latency).

================ PAGE 590 ================

552
11.1 Sự gia tốc Các nguyên tắc cơ bản (Acceleration Fundamentals)
1
Amdahl của Định luật (Amdahl’s Law): Ánh xạ một cách trực tiếp lên sắt định luật của cộng thêm các số hạng (Maps directly onto the iron law’s additive terms). Thậm chí nếu phần cứng lái sự tính toán số hạng (𝑂/(𝑅peak ⋅𝜂hw)) tới gần không, tổng thời gian là vẫn bị giới hạn bên dưới bởi nối tiếp dữ liệu-việc tải (𝐷vol/BW) và cố định-độ trễ (𝐿lat) các số hạng, thứ mà sự gia tốc không thể chạm tới (Even if hardware drives the computation term (𝑂/(𝑅peak ⋅𝜂hw)) to near zero, total time is still bounded below by the serial data-loading (𝐷vol/BW) and fixed-latency (𝐿lat) terms, which acceleration cannot touch). Điều này là tại sao lớn các sự cải thiện trong thô máy gia tốc thông lượng có thể sản xuất nhỏ hơn nhiều đầu-tới-đầu nhiệm vụ các phần tăng tốc khi dữ liệu việc tải, khởi chạy chi phí quản lý, hoặc sự tiền xử lý giữ nguyên nối tiếp (This is why large improvements in raw accelerator throughput can produce much smaller end-to-end task speedups when data loading, launch overhead, or preprocessing remains serial).
Cạm bẫy: Nối tiếp công việc giới hạn tổng máy gia tốc phần tăng tốc (Pitfall: Serial work caps total accelerator speedup). Nếu dữ liệu việc tải lấy 10 phần trăm của thời gian (𝑝= 0.9), thậm chí một vô hạn tốc độ máy gia tốc (𝐺accel = ∞) có thể chỉ đạt được một 10× tổng phần tăng tốc (If data loading takes 10 percent of the time (𝑝= 0.9), even an infinite speed accelerator (𝐺accel = ∞) can only achieve a 10× total speedup). Nối tiếp thành phần thống trị song song máy gia tốc thành phần một khi cái sau là đủ nhanh (The serial component dominates the parallel accelerator component once the latter is sufficiently fast).
Phần cứng sự gia tốc nhắm mục tiêu cụ thể các số hạng trong sắt định luật của ML các hệ thống (phần 1.7), thứ mà phân rã đầu-tới-đầu thời gian thành dữ liệu khối lượng (𝐷vol/BW), sự tính toán (𝑂/(𝑅peak ⋅𝜂hw)), và cố định độ trễ (𝐿lat) (Hardware acceleration targets specific terms in the iron law of ML systems (section 1.7), which decomposes end-to-end time into data volume (𝐷vol/BW), computation (𝑂/(𝑅peak ⋅𝜂hw)), and fixed latency (𝐿lat)). Trong khi dữ liệu sự chọn lựa đã làm giảm bớt tổng dữ liệu và mô hình sự nén đã làm giảm bớt 𝑂trên mỗi mẫu, phần cứng sự gia tốc làm tăng lên tốc độ ở đó những các hoạt động đó thực thi bằng cách việc cải thiện 𝑅peak, 𝜂hw, và BW (While data selection reduced the total data and model compression reduced 𝑂per sample, hardware acceleration increases the rate at which those operations execute by improving 𝑅peak, 𝜂hw, and BW). Phần D.2 cung cấp phân tích hiệu suất các mô hình thứ mà chẩn đoán cái nào của những các số hạng này thống trị một được cho khối lượng công việc, bao gồm chiều sự phân tích thứ mà xác nhận mỗi sắt định luật số hạng giải quyết tới các giây (Section D.2 supplies the analytical performance models that diagnose which of these terms dominates a given workload, including the dimensional analysis that confirms each iron law term resolves to seconds). Tuy nhiên sự gia tốc có một cứng trần nhà, được thiết lập bởi Amdahl của Định luật1 (Yet acceleration has a hard ceiling, established by Amdahl’s Law1).
Amdahl của Định luật là không chỉ đơn thuần lý thuyết: nó giải thích tại sao nhiều GPU các sự nâng cấp làm thất vọng trong thực tế (Amdahl’s Law is not merely theoretical: it explains why many GPU upgrades disappoint in practice). Sau đây bản đồ nhiệt (hình 11.1) trực quan hóa sự gia tốc bức tường, giảm dần các lợi nhuận từ nhanh hơn phần cứng khi nối tiếp các nút thắt cổ chai dai dẳng (The following heatmap (figure 11.1) visualizes the acceleration wall, the diminishing returns from faster hardware when serial bottlenecks persist). Trừ khi một khối lượng công việc là cao độ có thể song song hóa (𝑝> 0.99), việc đầu tư trong nhanh hơn phần cứng mang lại giảm dần các lợi nhuận (Unless a workload is highly parallelizable (𝑝> 0.99), investing in faster hardware yields diminishing returns). Đường viền các giá trị là mang tính minh họa các phạm vi cho trực giác (The contour values are illustrative ranges for intuition).
Máy gia tốc phần tăng (Accelerator gain) (Gaccel)
Có thể song song hóa Phần nhỏ (Parallelizable Fraction) (p)
Bị ràng buộc Tính toán (Compute Bound)
Bị ràng buộc Nối tiếp (Serial Bound)
Hình 11.1: Sắt Định luật Bản đồ nhiệt: Tổng hệ thống phần tăng tốc như một hàm của máy gia tốc phần tăng (𝐺accel) và song song phần nhỏ (𝑝) (Figure 11.1: The Iron Law Heatmap: Total system speedup as a function of accelerator gain (𝐺accel) and parallel fraction (𝑝)). Cao phần tăng tốc xuất hiện chỉ gần trên cùng-phải góc, nơi cả hai máy gia tốc phần tăng và song song phần nhỏ là cao (High speedup appears only near the top-right corner, where both accelerator gain and parallel fraction are high). Sự gia tốc bức tường là thấp-𝑝vùng: nếu một khối lượng công việc là thậm chí hơi nối tiếp (𝑝< 0.9), việc làm tăng lên phần cứng tốc độ mang lại ít lợi ích (The acceleration wall is the low-𝑝region: if a workload is even slightly serial (𝑝< 0.9), increasing hardware speed yields little benefit). Các đường viền trải dài đại khái 1×–500× phần tăng tốc (Contours span roughly 1×–500× speedup).
Chính trực giác để mang vào cụ thể phần cứng các kiến trúc là rằng thô các phần tăng tốc quan trọng chỉ sau khi nối tiếp phần nhỏ đã được làm giảm bớt (The key intuition to carry into specific hardware architectures is that raw speedups matter only after the serial fraction has been reduced).
Song song phần nhỏ 𝑝khác biệt một cách ngoạn mục giữa khối lượng công việc các nguyên mẫu việc chạy trên cùng phần cứng, và ở hạm đội quy mô những các sự khác biệt này xác định liệu một máy gia tốc sự đầu tư mang lại lợi ích hoặc đình trệ ở nối tiếp nút thắt cổ chai (The parallel fraction 𝑝differs dramatically between workload archetypes running on the same hardware, and at fleet scale these differences determine whether an accelerator investment pays off or stalls at the serial bottleneck).
Điểm kiểm tra 11.1: Sự song song cổng (Checkpoint 11.1: The parallelism gate)
Phần cứng các phần tăng tốc là bị giới hạn bởi tuần tự các nút thắt cổ chai (Hardware speedups are capped by sequential bottlenecks).
Amdahl của Thực tế (Amdahl’s Reality)
□ Nối tiếp các nút thắt cổ chai: Sử dụng Amdahl của giới hạn để giải thích tại sao một 1,000× nhanh hơn GPU có thể chỉ tăng tốc việc đào tạo bởi 5× khi dữ liệu việc tải là chậm (Serial bottlenecks: Use Amdahl’s bound to explain why a 1,000× faster GPU may only speed up training by 5× when data loading is slow).
□ Khối lượng công việc sự biến đổi: So sánh có thể song song hóa các phần nhỏ của ResNet-50 và MobileNet, sau đó dự đoán cái nào hưởng lợi nhiều hơn từ máy gia tốc thông lượng (Workload variation: Compare the parallelizable fractions of ResNet-50 and MobileNet, then predict which benefits more from accelerator throughput).

================ PAGE 591 ================

554
11.2 Phần cứng Sự chuyên biệt hóa (Hardware Specialization)
3
TPU (Tensor Xử lý Đơn vị) (TPU (Tensor Processing Unit)):
Đầu tiên TPU đã thực hiện một một cách có chủ ý hẹp vụ cá cược, việc lấp đầy khuôn với một đơn 256×256 tâm thu mảng cho 8-bit ma trận phép nhân và việc tước đi đi các bộ nhớ đệm, nhánh các bộ dự đoán, và ngoài-thứ tự logic trên đó một đa-mục đích lõi tiêu xài hầu hết của của nó diện tích (Jouppi et al. 2017) (The first TPU made a deliberately narrow bet, filling the die with a single 256×256 systolic array for 8-bit matrix multiplication and stripping away the caches, branch predictors, and out-of-order logic on which a general-purpose core spends most of its area (Jouppi et al. 2017)). Đó sự đánh đổi mua cực độ tính toán mật độ trên dày đặc ma trận nhân ở chi phí của tính linh hoạt: cùng chip thứ mà xuất sắc ở thần kinh mạng sự suy luận là kém phù hợp tới không đều hoặc nặng-nhánh mã, đó là tại sao mảng chiều bản thân nó trở thành một thiết kế sự ràng buộc, vì các lớp của đó các chiều là không các bội số của 256 để lại các hàng và các cột của mảng nhàn rỗi (That trade buys extreme compute density on dense matrix multiply at the cost of flexibility: the same chip that excels at neural network inference is poorly suited to irregular or branch-heavy code, which is why the array dimension itself becomes a design constraint, since layers whose dimensions are not multiples of 256 leave rows and columns of the array idle).
4
Intel 8087 (Intel 8087):
Bộ đồng xử lý đã triển khai dấu phẩy-động logic một cách trực tiếp trong silicon, việc tránh CPU của chậm, đa-lệnh phần mềm sự mô phỏng cho mỗi sự tính toán (The coprocessor implemented floating-point logic directly in silicon, avoiding the CPU’s slow, multi-instruction software emulation for each calculation). Điều này sự giảm tải chiến lược đã từng là duy nhất cơ chế đằng sau 100× hiệu suất phần tăng, một kết quả chỉ có thể đạt được bởi vì khoa học các khối lượng công việc đã tiêu xài phần lớn đa số của của chúng các chu kỳ trên những cụ thể số học các hoạt động này (This offload strategy was the sole mechanism behind the 100× performance gain, a result only achievable because scientific workloads spent the vast majority of their cycles on these specific arithmetic operations).
8087 của sự thành công do đó đã cung cấp kinh điển bằng chứng rằng việc chuyên biệt hóa phần cứng cho một thống trị tính toán hạt nhân mang lại hiệu suất các sự cải thiện 10–100× lớn hơn đa-mục đích sự chia tỷ lệ (The 8087’s success thus provided the canonical proof that specializing hardware for a dominant computational kernel yields performance improvements 10–100× greater than general-purpose scaling).
tới đó lý thuyết phần cứng các khả năng dịch thành có thể đo lường hiệu suất (to which theoretical hardware capabilities translate into measurable performance). Xuyên suốt, cốt lõi sự phân tích ở lại với đơn-máy gia tốc và đơn-nút các hệ thống; phần đóng tài liệu sử dụng đa-thiết bị các ví dụ chỉ để cho thấy cách nào cùng nút thắt cổ chai các sự chẩn đoán chia tỷ lệ (Throughout, the core analysis stays with single-accelerator and single-node systems; the closing material uses multi-device examples only to show how the same bottleneck diagnoses scale). Lịch sử của chuyên biệt phần cứng tiết lộ lặp lại thiết kế các mẫu thứ mà giải thích tại sao các máy gia tốc lấy của chúng hình thức (The history of specialized hardware reveals recurring design patterns that explain why accelerators take their form).
11.2 Phần cứng Sự chuyên biệt hóa (Hardware Specialization)
TPUv1/K80 hiệu quả cú sốc là hiện đại AI trường hợp của một lặp lại phần cứng mẫu: khi một khối lượng công việc trở nên quan trọng và đủ thường xuyên, đa-mục đích các bộ xử lý nhường đường tới chuyên biệt phần cứng (The TPUv1/K80 efficiency shock is the modern AI instance of a recurring hardware pattern: when a workload becomes important and regular enough, general-purpose processors give way to specialized hardware). Máy học hỏi sự gia tốc theo sau cùng quỹ đạo được thấy trong dấu phẩy-động số học, đồ họa việc xử lý, và kỹ thuật số tín hiệu việc xử lý (Machine learning acceleration follows the same trajectory seen in floating-point arithmetic, graphics processing, and digital signal processing). Mỗi kỷ nguyên đã đối mặt cùng sự ràng buộc được giới thiệu trong Mục đích phần: dữ liệu sự di chuyển các chi phí thống trị sự tính toán các chi phí, và sự chuyên biệt hóa thành công bằng cách việc tối thiểu hóa không cần thiết dữ liệu sự di chuyển (Each era confronted the same constraint introduced in the Purpose section: data movement costs dominate computation costs, and specialization succeeds by minimizing unnecessary data movement).
Hiện đại ML các máy gia tốc (hạng-DianNao thần kinh-mạng các máy gia tốc (Chen et al. 2014), các GPU với tensor các lõi, Google của các TPU3, Apple của Thần kinh Động cơ) đã nổi lên từ những được thiết lập thuộc về kiến trúc các nguyên lý này (Modern ML accelerators (DianNao-class neural-network accelerators (Chen et al. 2014), GPUs with tensor cores, Google’s TPUs3, Apple’s Neural Engine) emerged from these established architectural principles). Sự tiến hóa trải dài bốn các giai đoạn: chuyên biệt việc điện toán các nguồn gốc, song song đồ họa việc xử lý, cụ thể-miền các kiến trúc, và sự nổi lên của cụ thể-ML phần cứng (The evolution spans four phases: specialized computing origins, parallel graphics processing, domain-specific architectures, and the emergence of ML-specific hardware). Mỗi giai đoạn tiết lộ thiết kế các nguyên lý thứ mà giữ nguyên có liên quan cho việc hiểu và việc tối ưu hóa đương thời AI các hệ thống (Each phase reveals design principles that remain relevant for understanding and optimizing contemporary AI systems).
Ví dụ 11.1: TPUv1 so với K80 hiệu quả cú sốc (Example 11.1: The TPUv1 vs. K80 efficiency shock)
Ngữ cảnh: Trong 2015, Google đã triển khai của nó đầu tiên Tensor Xử lý Đơn vị (TPUv1) và so sánh nó tới thống trị GPU của kỷ nguyên, NVIDIA K80 (Context: In 2015, Google deployed its first Tensor Processing Unit (TPUv1) and compared it to the dominant GPU of the era, the NVIDIA K80).
Kết quả: TPUv1 đã không chỉ hơi nhanh hơn; nó đã từng 15–30× nhanh hơn trên sự suy luận các khối lượng công việc và đạt được 30–80× tốt hơn hiệu suất-trên-watt trong Google của được xuất bản sự so sánh (Jouppi et al. 2017) (Result: The TPUv1 was not just slightly faster; it was 15–30× faster on inference workloads and achieved 30–80× better performance-per-watt in Google’s published comparison (Jouppi et al. 2017)).
Cơ chế: K80 đã từng một đa-mục đích bộ xử lý (tốt cho đồ họa, vật lý, đa dạng toán học) (Mechanism: The K80 was a general-purpose processor (good for graphics, physics, diverse math)). TPU đã từng một cụ thể-miền kiến trúc (DSA) được xây dựng cho một thứ: 8-bit số nguyên ma trận phép nhân (The TPU was a domain-specific architecture (DSA) built for one thing: 8-bit integer matrix multiplication). Nó đã tước đi đi các bộ nhớ đệm, nhánh sự dự đoán, và ngoài-thứ tự sự thực thi logic để lấp đầy chip với thuần túy số học các đơn vị (tâm thu các mảng) (It stripped away caches, branch prediction, and out-of-order execution logic to fill the chip with pure arithmetic units (systolic arrays)).
Các hệ thống bài học: Điều này kết quả đã kết thúc "Đa Mục đích" kỷ nguyên cho AI (Systems lesson: This result ended the “General Purpose” era for AI). Nó đã chứng minh rằng việc may đo silicon tới thuật toán nguyên thủy (ma trận phép nhân) mang lại bậc-của-độ lớn các phần tăng thứ mà Moore của Định luật một mình không thể phân phối cho các thập kỷ (It proved that tailoring silicon to the algorithmic primitive (matrix multiplication) yields order-of-magnitude gains that Moore’s Law alone could not deliver for decades).
Phần cứng sự chuyên biệt hóa cải thiện hiệu suất bằng cách việc triển khai thường xuyên các mẫu trong được cống hiến các mạch điện, nhưng giới thiệu các sự đánh đổi trong tính linh hoạt, silicon diện tích, và lập trình tính phức tạp (Hardware specialization improves performance by implementing frequent patterns in dedicated circuits, but introduces trade-offs in flexibility, silicon area, and programming complexity). Các nguyên lý thứ mà đã định hình sớm dấu phẩy-động và đồ họa các máy gia tốc bây giờ thông báo AI phần cứng thiết kế (The principles that shaped early floating-point and graphics accelerators now inform AI hardware design).
11.2.1 Chuyên biệt việc điện toán (Specialized computing)
Phần cứng sự chuyên biệt hóa nổi lên khi cụ thể tính toán các mẫu trở thành chính hệ thống nút thắt cổ chai, việc ngăn cản đa-mục đích các bộ xử lý từ việc chia tỷ lệ một cách hiệu quả (Hardware specialization emerges when specific computational patterns become the primary system bottleneck, preventing general-purpose processors from scaling efficiently). Về mặt lịch sử, này sự tiến triển theo sau ba khác biệt các giai đoạn: độ chính xác nút thắt cổ chai (vô hướng dấu phẩy-động), thông lượng nút thắt cổ chai (song song đồ họa), và sự tích hợp nút thắt cổ chai (bộ nhớ-tính toán tính cục bộ) (Historically, this progression follows three distinct phases: the precision bottleneck (scalar floating-point), the throughput bottleneck (parallel graphics), and the integration bottleneck (memory-compute locality)).
Đầu tiên giai đoạn, độ chính xác nút thắt cổ chai, đã xảy ra khi khoa học và kỹ thuật các ứng dụng đã yêu cầu cao-độ chính xác thập phân toán học thứ mà đa-mục đích các CPU đã thực hiện một cách kém cỏi (The first phase, the precision bottleneck, occurred when scientific and engineering applications required high-precision decimal math that general-purpose CPUs performed poorly). Trong muộn các 1970s, các CPU điển hình đã mô phỏng dấu phẩy-động các hoạt động trong phần mềm, việc yêu cầu hàng trăm của các chu kỳ cho một đơn phép nhân (In the late 1970s, CPUs typically emulated floating-point operations in software, requiring hundreds of cycles for a single multiplication). Điều này vô hướng sự không hiệu quả đã dẫn tới đầu tiên chính trường hợp của phần cứng sự chuyên biệt hóa: toán học bộ đồng xử lý (This scalar inefficiency led to the first major instance of hardware specialization: the mathematics coprocessor).
Intel 8087 (1980)4 đã giải quyết này nút thắt cổ chai bằng cách việc giảm tải thâm dụng-số học các nhiệm vụ tới một được cống hiến đơn vị (The Intel 8087 (1980)4 addressed this bottleneck by offloading arithmetic-intensive tasks to a dedicated unit). Bằng cách việc triển khai dấu phẩy-động logic trong phần cứng thay vì phần mềm sự mô phỏng, 8087 đã đạt được lên tới 100× hiệu suất các phần tăng cho khoa học các khối lượng công việc (Palmer 1980) (By implementing floating-point logic in hardware rather than software emulation, the 8087 achieved up to 100× performance gains for scientific workloads (Palmer 1980)). Điều này đã thiết lập một cốt lõi nguyên lý: khi một cụ thể dữ liệu loại hoặc hoạt động tiêu thụ phần lớn đa số của sự thực thi các chu kỳ, việc di chuyển nó tới chuyên biệt silicon cung cấp 10–100× các sự cải thiện (This established a core principle: when a specific data type or operation consumes the majority of execution cycles, moving it to specialized silicon provides 10–100× improvements).

================ PAGE 593 ================

11. Phần cứng Sự gia tốc (Hardware Acceleration)
555
Khi chuyên biệt các hàm giống như dấu phẩy-động toán học đã chứng minh của chúng giá trị, chúng đã theo sau một lặp lại mẫu của sự tích hợp (As specialized functions like floating-point math proved their value, they followed a recurring pattern of integration). Intel 486DX (1989) đã di chuyển FPU một cách trực tiếp lên CPU khuôn, việc loại bỏ ngoài-chip giao tiếp độ trễ và việc làm cao-độ chính xác toán học thành một tiêu chuẩn tính năng thay vì một tùy chọn máy gia tốc (Patterson và Hennessy 2017) (The Intel 486DX (1989) moved the FPU directly onto the CPU die, eliminating the off-chip communication latency and making high-precision math a standard feature rather than an optional accelerator (Patterson and Hennessy 2017)). Điều này chu kỳ (sự chuyên biệt hóa để giải quyết một nút thắt cổ chai, được theo sau bởi sự tích hợp vào đa-mục đích ngăn xếp) lặp lại qua mỗi kỷ nguyên của phần cứng sự tiến hóa (This cycle (specialization to solve a bottleneck, followed by integration into the general-purpose stack) repeats across every era of hardware evolution).
Sự tiến triển từ sự chuyên biệt hóa tới sự tích hợp đã định hình hiện đại việc điện toán (The progression from specialization to integration has shaped modern computing). Mỗi miền (đồ họa, tín hiệu việc xử lý, máy học hỏi) đã giới thiệu chuyên biệt các kiến trúc thứ mà đã từng sau này được hấp thụ vào đa-mục đích các nền tảng (Each domain (graphics, signal processing, machine learning) introduced specialized architectures that were later absorbed into general-purpose platforms).
Hình 11.2 truy tìm này lặp lại chu kỳ của sự chuyên biệt hóa và sự tích hợp qua năm các kỷ nguyên, mỗi giải quyết thống trị tính toán nút thắt cổ chai của của nó thời kỳ: các 1980s dấu phẩy-động và tín hiệu-việc xử lý các đơn vị (Intel 8087, TI TMS32010 DSP), 1990s 3D đồ họa (NVIDIA GeForce 256), 2000s phương tiện và mạng việc xử lý (H.264 các codec, Intel IXP2800), 2010s sâu-sự học hỏi tensor các hoạt động (Google TPU v1, NVIDIA Tensor Các lõi), và 2020s cụ thể-ứng dụng các máy gia tốc (AI các động cơ, quy mô-tấm wafer ML các chip) (Figure 11.2 traces this recurring cycle of specialization and integration across five eras, each addressing the dominant computational bottleneck of its period: the 1980s floating-point and signal-processing units (Intel 8087, TI TMS32010 DSP), 1990s 3D graphics (NVIDIA GeForce 256), 2000s media and network processing (H.264 codecs, Intel IXP2800), 2010s deep-learning tensor operations (Google TPU v1, NVIDIA Tensor Cores), and 2020s application-specific accelerators (AI engines, wafer-scale ML chips)). Các khả năng chẳng hạn như thời gian-thực sự dịch thuật, các sự giới thiệu, và trên-thiết bị sự suy luận xây dựng một cách trực tiếp trên các nguyên lý được thiết lập trong những sớm hơn sự chuyên biệt hóa các làn sóng này (Capabilities such as real-time translation, recommendations, and on-device inference build directly on principles established in these earlier specialization waves).
Các 1980s (1980s)
Các 1990s (1990s)
Các 2000s (2000s)
Các 2010s (2010s)
Các 2020s (2020s)
Dấu phẩy-Động &
Tín hiệu Việc xử lý (Floating-Point & Signal Processing)
Intel 8087 FPU (1980)
Texas Instruments
TMS32010 DSP (1983)
Sự tích hợp của FPU
vào Intel 486DX (1989) (Integration of FPU into Intel 486DX (1989))
3D Đồ họa &
Đa phương tiện (3D Graphics & Multimedia)
Sự giới thiệu của
Sớm các GPU (Introduction of Early GPUs)
NVIDIA GeForce 256 –
Đầu tiên GPU với
Phần cứng T&L (1999) (NVIDIA GeForce 256 – First GPU with Hardware T&L (1999))
Sự trỗi dậy của SIMD
Việc xử lý Các đơn vị (Rise of SIMD Processing Units)
Thời gian-thực Phương tiện
Việc mã hóa &
Mạng Việc xử lý (Real-time Media Coding & Network Processing)
Phương tiện Các codec
(H.264, MP3) (Media Codecs (H.264, MP3))
Intel IXP2800
Mạng Bộ xử lý (Intel IXP2800 Network Processor)
Được cống hiến phần cứng
cho việc phát trực tuyến
và việc mã hóa (Dedicated hardware for streaming and encoding)
Sâu Sự học hỏi
Tensor Các hoạt động (Deep Learning Tensor Operations)
Google TPU v1 cho
ML Sự suy luận (2015) (Google TPU v1 for ML Inference (2015))
NVIDIA Tensor Các lõi
cho DL Sự gia tốc (NVIDIA Tensor Cores for DL Acceleration)
Cụ thể-AI bộ nhớ
các sự tối ưu hóa (AI-specific memory optimizations)
Cụ thể-Ứng dụng
Sự gia tốc (Application-Specific Acceleration)
AI Các động cơ &
Các SmartNIC (AI Engines & SmartNICs)
Đa-chip và
quy mô-tấm wafer ML
sự gia tốc (Multi-chip and wafer-scale ML acceleration)
ML các khuôn khổ
việc tối ưu hóa cho
chuyên biệt phần cứng (ML frameworks optimizing for specialized hardware)
Hình 11.2: Phần cứng Sự chuyên biệt hóa Dòng thời gian: Việc điện toán các kiến trúc một cách tiến bộ kết hợp chuyên biệt các máy gia tốc để giải quyết đang nổi lên hiệu suất các nút thắt cổ chai, từ dấu phẩy-động các đơn vị tới đồ họa các bộ xử lý và máy học hỏi các máy gia tốc (Figure 11.2: Hardware Specialization Timeline: Computing architectures progressively incorporate specialized accelerators to address emerging performance bottlenecks, from floating-point units to graphics processors and machine learning accelerators). Mỗi kỷ nguyên đã sản xuất phần cứng được may đo tới thống trị tính toán các mẫu của của nó thời kỳ (Each era produced hardware tailored to the dominant computational patterns of its period).
11.2.2 Song song việc điện toán và đồ họa việc xử lý (Parallel computing and graphics processing)
Các nguyên lý được thiết lập thông qua dấu phẩy-động sự gia tốc đã cung cấp một bản thiết kế cho việc giải quyết tiếp theo tính toán các thách thức (The principles established through floating-point acceleration provided a blueprint for addressing subsequent computational challenges). Khi việc điện toán các ứng dụng đã đa dạng hóa, mới tính toán các mẫu đã nổi lên thứ mà đã vượt quá các khả năng của đa-mục đích các bộ xử lý, và mỗi miền đã đóng góp độc đáo các sự thấu hiểu tới phần cứng sự gia tốc các chiến lược (As computing applications diversified, new computational patterns emerged that exceeded the capabilities of general-purpose processors, and each domain contributed unique insights to hardware acceleration strategies).
Đồ họa việc xử lý đã nổi lên như một chính bộ dẫn động của phần cứng sự chuyên biệt hóa trong các 1990s (Graphics processing emerged as a primary driver of hardware specialization in the 1990s). Sớm đồ họa các máy gia tốc đã tập trung trên cụ thể các hoạt động giống như bitmap các sự truyền và đa giác việc điền (Early graphics accelerators focused on specific operations like bitmap transfers and polygon filling). NVIDIA của GeForce 256 trong 1999 đã đại diện một cột mốc trong chuyên biệt việc điện toán (NVIDIA’s GeForce 256 in 1999 represented a milestone in specialized computing). GeForce 256 đã triển khai được gia tốc-bởi-phần cứng biến đổi và chiếu sáng (T&L), việc di chuyển những các sự tính toán này từ CPU tới được cống hiến silicon (The GeForce 256 implemented hardware-accelerated transform and lighting (T&L), moving these computations from CPU to dedicated silicon). Trong khi chưa có thể lập trình, những Đồ họa Việc xử lý Các đơn vị (các GPU) này đã chứng minh cách nào cố định-chức năng song song các kiến trúc có thể một cách hiệu quả xử lý song song-dữ liệu các khối lượng công việc chẳng hạn như kết cấu sự ánh xạ và đỉnh sự biến đổi (While not yet programmable, these Graphics Processing Units (GPUs) demonstrated how fixed-function parallel architectures could efficiently handle data-parallel workloads such as texture mapping and vertex transformation). Sự chuyển đổi tới có thể lập trình các shader với GeForce 3 (2001) và được hợp nhất shader các kiến trúc với GeForce 8 (2006) cuối cùng đã cho phép GPU việc điện toán cho đa-mục đích các khối lượng công việc (The transition to programmable shaders with the GeForce 3 (2001) and unified shader architectures with the GeForce 8 (2006) eventually enabled GPU computing for general-purpose workloads). Bởi 2004, cao-cấp các GPU có thể xử lý hơn 100 triệu các đa giác trên giây (Owens et al. 2008) (By 2004, high-end GPUs could process over 100 million polygons per second (Owens et al. 2008)).
Cùng lúc, Kỹ thuật số Tín hiệu Việc xử lý (DSP) các bộ xử lý đã thiết lập song song dữ liệu đường dẫn các kiến trúc với chuyên biệt nhân-tích lũy các đơn vị và tròn các bộ đệm được tối ưu hóa cho việc lọc và biến đổi các hoạt động (Concurrently, Digital Signal Processing (DSP) processors established parallel data path architectures with specialized multiply-accumulate units and circular buffers optimized for filtering and transform operations). Texas Instruments của TMS32010 (1983) đã chứng minh cách nào cụ thể-miền lệnh các tập hợp có thể một cách ngoạn mục cải thiện hiệu suất cho tín hiệu việc xử lý các ứng dụng (Lyons 2011) (Texas Instruments’ TMS32010 (1983) demonstrated how domain-specific instruction sets could dramatically improve performance for signal processing applications (Lyons 2011)).

================ PAGE 594 ================

556
11.2 Phần cứng Sự chuyên biệt hóa (Hardware Specialization)
5
AlexNet:
Krizhevsky,
Sutskever,
và
Hinton của
60-triệu-tham số
tích chập
thần kinh
mạng
(CNN) thứ mà đã thắng ImageNet
2012 bởi một 10.8-phần trăm-điểm
khoảng cách
trên
hai
cấp người tiêu dùng GTX 580 các GPU
với chỉ 3 GB của VRAM
mỗi cái (Krizhevsky, Sutskever, and Hinton’s 60-million-parameter convolutional neural network (CNN) that won ImageNet 2012 by a 10.8-percentage-point margin on two consumer GTX 580 GPUs with only 3 GB of VRAM each).
Bởi vì mô hình
đã vượt quá đơn-GPU bộ nhớ,
Krizhevsky
một cách thủ công
đã phân vùng
các lớp
qua
hai
các thẻ,
việc chọn
cái nào các lớp đã giao tiếp
qua PCIe để tối thiểu hóa
dữ liệu-sự truyền nút thắt cổ chai—một
đặc biệt
mô hình
sự song song
thứ mà
đã báo trước
sau này
có hệ thống
tensor
và
đường ống sự song song các chiến lược (Because the model exceeded single-GPU memory, Krizhevsky manually partitioned layers across the two cards, choosing which layers communicated across PCIe to minimize the data-transfer bottleneck—an ad-hoc model parallelism that foreshadowed later systematic tensor and pipeline parallelism strategies). Việc đào tạo đã lấy năm tới sáu
ngày thay vì các tuần trên
các CPU, việc chứng minh rằng việc khớp
một
khối lượng công việc của
sự song song
tới
GPU
phần cứng
có thể
mang lại
bậc-của-độ lớn
các sự giảm bớt trong thời gian-để-đào tạo (Training took five to six days rather than weeks on CPUs, proving that matching a workload’s parallelism to GPU hardware could yield order-of-magnitude reductions in time-to-train).
6
Cụ thể-Miền Kiến trúc (Domain-Specific Architecture) (DSA): Silicon được tối ưu hóa
cho một đơn ứng dụng
miền, việc hy sinh đa-mục đích
tính có thể lập trình cho
tính hiệu quả (Silicon optimized for a single application domain, sacrificing general-purpose programmability for efficiency). Google của TPUv1 đã đạt được 15–30× tốt hơn hiệu suất và 30–80× tốt hơn hiệu suất
trên watt so với đương thời
các CPU và các GPU
trên Google của sự suy luận các chuẩn đối sánh
bằng cách việc loại bỏ nhánh
sự dự đoán, các bộ nhớ đệm, và ngoài-thứ tự
logic trong ân huệ của một tâm thu
mảng (Jouppi et al. 2017) (Google’s TPUv1 achieved 15–30× better performance and 30–80× better performance per watt than contemporary CPUs and GPUs on Google’s inference benchmarks by eliminating branch prediction, caches, and out-of-order logic in favor of a systolic array (Jouppi et al. 2017)).
Sự đánh đổi là tính không linh hoạt: một
DSA thứ mà xuất sắc ở dày đặc ma trận
phép nhân có thể thực hiện
kém hơn một CPU trên không đều
các khối lượng công việc giống như đồ thị
sự đi ngang qua, việc làm khối lượng công việc-phần cứng
sự căn chỉnh thành trung tâm
thiết kế quyết định (The trade-off is inflexibility: a DSA that excels at dense matrix multiplication may perform worse than a CPU on irregular workloads like graph traversal, making workload-hardware alignment the central design decision).
Hennessy
và Patterson của quy tắc của
ngón tay cái là rằng một mới kiến trúc
phải phân phối ít nhất 10×
hiệu quả qua đa-mục đích
sự thay thế để biện minh
hệ sinh thái chi phí của sự áp dụng (Hennessy và Patterson 2019; Patterson và Hennessy 2017) (Hennessy and Patterson’s rule of thumb is that a new architecture must deliver at least 10× efficiency over the general-purpose alternative to justify the ecosystem cost of adoption (Hennessy and Patterson 2019; Patterson and Hennessy 2017)).
Mạng việc xử lý đã giới thiệu bổ sung các mẫu của sự chuyên biệt hóa (Network processing introduced additional patterns of specialization). Mạng các bộ xử lý đã phát triển độc đáo các kiến trúc để xử lý gói việc xử lý ở dòng tỷ lệ, việc kết hợp nhiều việc xử lý các lõi, chuyên biệt gói sự thao tác các đơn vị, và được phân tầng bộ nhớ sự quản lý các hệ thống (Network processors developed unique architectures to handle packet processing at line rate, incorporating multiple processing cores, specialized packet manipulation units, and tiered memory management systems). Intel của IXP2800 mạng bộ xử lý cho thấy hậu quả của một cứng sự ràng buộc: việc đáp ứng dòng-tỷ lệ gói các hạn chót để lại không sự chùng cho bộ nhớ đệm các sự trượt, vì vậy thiết kế sắp xếp nhiều song song các lõi xung quanh được phân tầng trên-chip bộ nhớ để giữ dữ liệu liền kề tới tính toán (Intel’s IXP2800 network processor shows the consequence of one hard constraint: meeting line-rate packet deadlines leaves no slack for cache misses, so the design arranges many parallel cores around tiered on-chip memory to keep data adjacent to compute). Đó tính toán-gần-bộ nhớ tổ chức, được ép buộc ở đây bởi gói việc định thời, là cùng sự sắp xếp ML các máy gia tốc sau này áp dụng để giữ của chúng việc xử lý-phần tử các lưới được nuôi dưỡng (That compute-near-memory organization, forced here by packet timing, is the same arrangement ML accelerators later adopt to keep their processing-element grids fed).
Qua những các miền này, một phổ biến bản thiết kế nổi lên: nhận dạng thống trị tính toán các mẫu, xây dựng chuyên biệt việc xử lý các phần tử và bộ nhớ các hệ thống phân cấp xung quanh chúng, tạo được may đo lập trình các mô hình, và một cách tiến bộ tiến hóa hướng tới linh hoạt hơn các kiến trúc (Across these domains, a common blueprint emerges: identify the dominant computational patterns, build specialized processing elements and memory hierarchies around them, create tailored programming models, and progressively evolve toward more flexible architectures). Điều này mẫu của thuộc về kiến trúc sự đồng tiến hóa đã thiết lập nền tảng cho đương thời AI phần cứng thiết kế (This pattern of architectural co-evolution established the foundation for contemporary AI hardware design). DSP các sự đổi mới trong thấp-năng lượng tín hiệu việc xử lý đã cho phép thời gian-thực sự suy luận trên rìa các thiết bị, bao gồm giọng nói các trợ lý và có thể mặc được các thiết bị (DSP innovations in low-power signal processing enabled real-time inference on edge devices, including voice assistants and wearables). Cùng nhau, những các miền này đã thông báo ML phần cứng các thiết kế và đã chứng minh rằng các máy gia tốc có thể được triển khai qua cả hai đám mây và được nhúng các ngữ cảnh (Together, these domains informed ML hardware designs and demonstrated that accelerators could be deployed across both cloud and embedded contexts).
Một đơn kết quả đã chứng minh GPU của sự liên quan tới AI đã từng không lý thuyết (A single result proved the GPU’s relevance to AI was not theoretical). AlexNet5 (Krizhevsky et al. 2012) đã thắng ImageNet cuộc thi bởi một 10.8-phần trăm-điểm khoảng cách—trên hai cấp-người tiêu dùng NVIDIA GTX 580 đồ họa các thẻ, mỗi cái với chỉ 3 GB của VRAM (AlexNet5 (Krizhevsky et al. 2012) won the ImageNet competition by a 10.8-percentage-point margin—on two consumer-grade NVIDIA GTX 580 graphics cards, each with only 3 GB of VRAM). Các hệ thống bài học đã từng không thể để phớt lờ: việc khớp một khối lượng công việc của dữ liệu sự song song tới GPU phần cứng có thể mang lại bậc-của-độ lớn các sự cải thiện trong thời gian-để-đào tạo (The systems lesson was impossible to ignore: matching a workload’s data parallelism to GPU hardware could yield order-of-magnitude improvements in time-to-train). Kỷ nguyên của lấy-GPU-làm-trung tâm sâu sự học hỏi đã bắt đầu (The era of GPU-centric deep learning had begun).
11.2.3 Sự nổi lên của cụ thể-miền các kiến trúc (Emergence of domain-specific architectures)
Những đa dạng sự gia tốc các mẫu này đã hội tụ trong một rộng hơn thuộc về kiến trúc sự dịch chuyển (These diverse acceleration patterns converged in a broader architectural shift). Sự nổi lên của cụ thể-miền các kiến trúc (DSAs)6 đánh dấu một sự chuyển đổi trong máy tính hệ thống thiết kế, được dẫn dắt bởi hai đang hội tụ các yếu tố: sự phá vỡ của truyền thống sự chia tỷ lệ các định luật (Esmaeilzadeh et al. 2011) và đang gia tăng tính toán các nhu cầu của chuyên biệt các khối lượng công việc (The emergence of domain-specific architectures (DSAs)6 marks a transition in computer system design, driven by two converging factors: the breakdown of traditional scaling laws (Esmaeilzadeh et al. 2011) and the increasing computational demands of specialized workloads). Moore của Định luật7 đã từng trước đó đảm bảo có thể dự đoán các sự nâng cao trong transistor mật độ mỗi 18 tới 24 các tháng (Moore 1998) (Moore’s Law7 had previously ensured predictable enhancements in transistor density every 18 to 24 months (Moore 1998)). Dennard sự chia tỷ lệ8 (Dennard et al. 1974) đã từng cho phép tần số các sự làm tăng lên mà không có tương ứng năng lượng-mật độ các sự làm tăng lên; của nó sự phá vỡ đã loại bỏ đó đường dẫn tới dễ dàng hiệu suất các phần tăng (Dennard scaling8 (Dennard et al. 1974) had permitted frequency increases without corresponding power-density increases; its breakdown removed that path to easy performance gains). Cùng nhau, những các sự dịch chuyển này đã tạo ra một hiệu suất và tính hiệu quả nút thắt cổ chai trong đa-mục đích việc điện toán (Together, these shifts created a performance and efficiency bottleneck in general-purpose computing). Như Hennessy và Patterson (2019) đã lưu ý trong 2017 Turing Bài giảng, những các sự giới hạn này đã báo hiệu sự khởi đầu của một mới kỷ nguyên trong máy tính kiến trúc được tập trung trên cụ thể-miền các giải pháp thứ mà tối ưu hóa phần cứng cho chuyên biệt các khối lượng công việc (As Hennessy and Patterson (2019) noted in the 2017 Turing Lecture, these limitations signaled the onset of a new era in computer architecture centered on domain-specific solutions that optimize hardware for specialized workloads).
2012
2014
2016
2018
2020
2022
2024
Năm (Year)
Tương đối Sự tăng trưởng (2012 = 1.0) (Relative Growth (2012 = 1.0))
CÁC HỆ THỐNG KHOẢNG CÁCH
(Được đóng bởi Sự song song,
Kiến trúc & Sự đồng thiết kế) (THE SYSTEMS GAP (Closed by Parallelism, Architecture & Co-design))
AlexNet
Transformer
GPT-3
GPT-4
CPU Hiệu suất Xu hướng (CPU Performance Trend)
GPU Đỉnh (Huang của Định luật) (GPU Peak (Huang's Law))
Mô hình Nhu cầu (Sự chia tỷ lệ Các định luật) (Model Demand (Scaling Laws))
Hình 11.3: Các Hệ thống Khoảng cách: Tương đối tính toán sự tăng trưởng (log quy mô) việc so sánh mô hình nhu cầu tới phần cứng nguồn cung, được chuẩn hóa tới 2012 = 1.0 (Figure 11.3: The Systems Gap: Relative compute growth (log scale) comparing model demand to hardware supply, normalized to 2012 = 1.0). Xám chấm dòng (CPU) và xanh dương đứt nét dòng (GPU) phản ánh phần cứng tiến bộ, thứ mà tụt hậu số mũ đỏ liền mạch dòng (Mô hình Nhu cầu) (The gray dotted line (CPU) and blue dashed line (GPU) reflect hardware progress, which lags the exponential red solid line (Model Demand)). Tím vùng là 'Các Hệ thống Khoảng cách' thứ mà phải được nối cầu thông qua sự song song và sự đồng thiết kế (The purple region is the ‘Systems Gap’ that must be bridged through parallelism and co-design).
Quy mô của này thách thức trở nên rõ rệt trong hình 11.3, thứ mà vẽ đồ thị các hệ thống khoảng cách: sự phân kỳ giữa cái gì các mô hình yêu cầu và cái gì phần cứng một cách tự nhiên cung cấp (The scale of this challenge becomes stark in figure 11.3, which plots the systems gap: the divergence between what models demand and what hardware naturally provides). Trong được vẽ đồ thị sự chuẩn hóa,

================ PAGE 595 ================

557
7
Moore của Định luật (Moore’s Law):
Hệ quả
cho
ML
là
không
chỉ
chậm hơn
phần cứng
sự cải thiện mà một cấu trúc
khoảng cách đang nới rộng (The consequence for ML is not just slower hardware improvement but a structurally widening gap):
trong
các mang tính minh họa giả định
được sử dụng bởi hình 11.3, mô hình
tính toán
nhu cầu
tăng trưởng
đại khái 6.1× mỗi năm trong khi
máy gia tốc
đỉnh
nguồn cung
cải thiện đại khái 2× mỗi năm,
việc nới rộng nhu cầu/nguồn cung khoảng cách bởi khoảng 3.5× mỗi
năm (in the illustrative assumptions used by figure 11.3, model compute demand grows roughly 6.1× per year while accelerator peak supply improves roughly 2× per year, widening the demand/supply gap by about 3.5× per year). Điều này sự phân kỳ, có thể nhìn thấy
trong tính toán-xu hướng các sự phân tích
từ
OpenAI
và
Epoch
AI,
làm
thuật toán
tính hiệu quả các kỹ thuật—mô hình
sự nén,
sự lượng tử hóa,
sự thưa thớt—một cách có cấu trúc
cần thiết
thay vì tùy chọn
các sự tối ưu hóa (Amodei và
Hernandez 2018a; Epoch AI
2024) (This divergence, visible in compute-trend analyses from OpenAI and Epoch AI, makes algorithmic efficiency techniques—model compression, quantization, sparsity—structurally necessary rather than optional optimizations (Amodei and Hernandez 2018a; Epoch AI 2024)).
8
Dennard Sự chia tỷ lệ (Dennard Scaling):
1974 nguyên lý rằng khi transistor các chiều đã thu nhỏ, của chúng
hoạt động điện áp có thể được
hạ thấp để giữ năng lượng mật độ
không đổi (Dennard et al.
1974) (The 1974 principle that as transistor dimensions shrank, their operating voltage could be lowered to keep power density constant (Dennard et al. 1974)).
Của nó sự phá vỡ sau
~2005 có nghĩa là xung nhịp
các tốc độ không thể lâu hơn được
làm tăng lên mà không có việc vi phạm
chip của nhiệt thiết kế
năng lượng (TDP) các giới hạn, việc tạo ra
"tối silicon" vấn đề:
ở tiên tiến các nút, nhiệt
các sự ràng buộc ngăn cản việc cấp nguồn
nhiều hơn đại khái 30–50 phần trăm
của các transistor một cách đồng thời (Esmaeilzadeh et al.
2011) (Its breakdown after ~2005 meant that clock speeds could no longer be increased without violating the chip’s thermal design power (TDP) limits, creating the “dark silicon” problem: at advanced nodes, thermal constraints prevent powering more than roughly 30–50 percent of transistors simultaneously (Esmaeilzadeh et al. 2011)).
Điều này một cách trực tiếp ép buộc
sự chuyên biệt hóa—chỉ bằng cách việc cống hiến được cấp nguồn các transistor tới
hẹp các khối lượng công việc (giống như ma trận
phép nhân) có thể các kiến trúc sư
trích xuất hữu ích hiệu suất
từ có sẵn silicon
ngân sách (This directly forces specialization—only by dedicating powered transistors to narrow workloads (like matrix multiplication) can architects extract useful performance from the available silicon budget).
9
Huang của Định luật (Huang’s Law): Sự quan sát
rằng GPU hiệu suất
cho AI các khối lượng công việc về mặt lịch sử
đã cải thiện nhanh hơn
truyền thống Moore của Định luật, một
tốc độ đạt được thông qua thuộc về kiến trúc
các sự đổi mới (ví
dụ, Tensor Các lõi) thay vì
transistor sự chia tỷ lệ một mình (The observation that GPU performance for AI workloads historically improved faster than traditional Moore’s Law, a pace achieved through architectural innovations (for example, Tensor Cores) rather than transistor scaling alone).
Được chuẩn hóa hình sử dụng
một đại diện GPU-nguồn cung
đường cong của khoảng 1.7× mỗi năm
và một mô hình-nhu cầu đường cong
của khoảng 6× mỗi năm, việc minh họa
một khoảng cách thứ mà nới rộng bởi
đại khái 3–4× hàng năm trừ khi
phần mềm và kiến trúc sự đồng thiết kế
đóng nó (Amodei và
Hernandez 2018a; Epoch AI
2024; NVIDIA Corporation
2020; Choquette 2023) (The normalized figure uses a representative GPU-supply curve of about 1.7× per year and a model-demand curve of about 6× per year, illustrating a gap that widens by roughly 3–4× annually unless software and architecture co-design close it (Amodei and Hernandez 2018a; Epoch AI 2024; NVIDIA Corporation 2020; Choquette 2023)).
GPU nguồn cung, thường được đóng khung như Huang của Định luật,9 tăng khoảng 1.7× mỗi năm trong khi mô hình nhu cầu tăng khoảng 6× mỗi năm, vì vậy các hệ thống khoảng cách nới rộng bởi đại khái 3–4× mỗi năm (Amodei và Hernandez 2018a; Epoch AI 2024) (GPU supply, often framed as Huang’s Law,9 rises about 1.7× per year while model demand rises about 6× per year, so the systems gap widens by roughly 3–4× each year (Amodei and Hernandez 2018a; Epoch AI 2024)).
Đồ thị được chuẩn hóa tới một 2012 đường cơ sở để nhấn mạnh tương đối sự tăng trưởng (The plot is normalized to a 2012 baseline to emphasize relative growth). Chú ý cách nào được tô màu-tím vùng giữa các đường cong tiếp tục nới rộng—này khoảng cách không thể được đóng bằng cách việc chờ đợi cho nhanh hơn các chip; nó yêu cầu thuộc về kiến trúc sự đổi mới (Notice how the purple-shaded region between the curves keeps widening—this gap cannot be closed by waiting for faster chips; it requires architectural innovation).
11.2.4 Công nghệ S-đường cong: Tại sao chúng ta phải dịch chuyển (The technology S-curve: Why we must shift)
Mỗi việc điện toán mô thức theo sau một độc đáo vòng đời của ba các giai đoạn: sự lên men (ban đầu chậm tiến bộ), cất cánh (số mũ sự tăng trưởng), và sự bão hòa (giảm dần các lợi nhuận ở vật lý các giới hạn) (Every computing paradigm follows a distinct lifecycle of three phases: ferment (initial slow progress), take-off (exponential growth), and saturation (diminishing returns at physical limits)). Công nghệ S-đường cong mẫu này xuất hiện trong hai đang chồng lấp các đường cong trong hình 11.4: khi một đa-mục đích đường cong bão hòa, cụ thể-miền các kiến trúc có thể mở một mới tính hiệu quả đường cong cho các khối lượng công việc với ổn định tính toán cấu trúc (This technology S-curve pattern appears in the two overlapping curves in figure 11.4: as a general-purpose curve saturates, domain-specific architectures can open a new efficiency curve for workloads with stable computational structure).
1980
1990
2000
2010
2020
2030
Năm (Year)
Hiệu suất/Tính hiệu quả (Log Quy mô) (Performance/Efficiency (Log Scale))
Moore của Định luật
(Số mũ Sự tăng trưởng) (Moore's Law (Exponential Growth))
Dennard Sự chia tỷ lệ Kết thúc
(Sự bão hòa) (Dennard Scaling Ends (Saturation))
Mô thức Sự dịch chuyển
(Phần cứng-Phần mềm Sự đồng thiết kế) (The Paradigm Shift (Hardware-Software Co-design))
Kỷ nguyên của Các máy gia tốc
(Ma trận Toán học trọng tâm) (Era of Accelerators (Matrix Math focus))
Các Hệ thống
Khoảng cách (~100×) (The Systems Gap (~100×))
Đa Mục đích (CPU) (General Purpose (CPU))
Cụ thể Miền (Máy gia tốc) (Domain Specific (Accelerator))
Hình 11.4: Đôi S-Các đường cong của Chuyên biệt Việc điện toán: Đa-mục đích các CPU (xám) đã tận hưởng các thập kỷ của số mũ sự tăng trưởng được dẫn dắt bởi Moore của Định luật và Dennard Sự chia tỷ lệ (Figure 11.4: The Twin S-Curves of Specialized Computing: General-purpose CPUs (gray) enjoyed decades of exponential growth driven by Moore’s Law and Dennard Scaling). Khi vật lý đã ràng buộc này đường cong xung quanh 2010 (Sự bão hòa), cụ thể-miền các kiến trúc (xanh dương) đã cung cấp một mới tính hiệu quả đường cong (As physics constrained this curve around 2010 (Saturation), domain-specific architectures (blue) provided a new efficiency curve). Bền vững mẫu là rằng lớn tính hiệu quả các phần tăng đến từ việc chuyên biệt hóa phần cứng cho tuyến tính đại số, mặc dù ở chi phí của đa-mục đích tính có thể lập trình (The durable pattern is that large efficiency gains come from specializing hardware for linear algebra, albeit at the cost of general programmability).
"Dễ dàng" các phần tăng từ việc thu nhỏ các transistor là đã biến mất (The “easy” gains from shrinking transistors are gone). Để duy trì số mũ sự tăng trưởng được yêu cầu bởi AI các mô hình (thứ mà đang tăng trưởng 4–10× nhanh hơn Moore của Định luật), chúng ta không thể chờ đợi cho tiếp theo CPU thế hệ (To sustain the exponential growth required by AI models (which are growing 4–10× faster than Moore’s Law), we cannot wait for the next CPU generation). Chúng ta phải dịch chuyển tới một mới đường cong, một được định nghĩa không bởi xung nhịp tốc độ mà bởi kiến trúc (We must shift to a new curve, one defined not by clock speed but by architecture).
Để hiểu cách nào chúng ta đã đạt tới này điểm uốn, chúng ta phải đầu tiên kiểm tra cơ học của sự chia tỷ lệ các định luật thứ mà đã từng cung cấp nhiên liệu đa-mục đích kỷ nguyên (To understand how we reached this inflection point, we must first examine the mechanics of the scaling laws that once fueled the general-purpose era).
Về mặt lịch sử, các sự cải thiện trong bộ xử lý hiệu suất đã phụ thuộc trên bán dẫn quá trình sự chia tỷ lệ và việc làm tăng lên xung nhịp các tốc độ (Historically, improvements in processor performance depended on semiconductor process scaling and increasing clock speeds). Khi năng lượng mật độ các sự giới hạn đã hạn chế thêm nữa tần số sự chia tỷ lệ và transistor sự thu nhỏ đã gặp phải đang gia tăng vật lý và kinh tế các sự ràng buộc, các kiến trúc sư đã khám phá thay thế các phương pháp tiếp cận để duy trì tính toán sự tăng trưởng (As power density limitations restricted further frequency scaling and transistor miniaturization encountered increasing physical and economic constraints, architects explored alternative approaches to sustain computational growth). Kết quả đã từng một sự dịch chuyển hướng tới cụ thể-miền các kiến trúc, thứ mà cống quyết silicon các tài nguyên để tối ưu hóa sự tính toán cho cụ thể ứng dụng các miền, việc đánh đổi tính linh hoạt cho tính hiệu quả (The result was a shift toward domain-specific architectures, which dedicate silicon resources to optimize computation for specific application domains, trading flexibility for efficiency).
Cụ thể-miền các kiến trúc đạt được vượt trội hiệu suất và năng lượng tính hiệu quả khi phần cứng dừng việc đối xử khối lượng công việc như tùy ý mã (Domain-specific architectures achieve superior performance and energy efficiency when the hardware stops treating the workload as arbitrary code). Đầu tiên sự dịch chuyển là một được tùy chỉnh dữ liệu đường dẫn: ma trận phép nhân các đơn vị trong AI các máy gia tốc, cho ví dụ, triển khai tâm thu các mảng, giống-lưới các mạng của việc xử lý các phần tử thứ mà một cách nhịp nhàng tính toán và truyền dữ liệu thông qua lân cận các đơn vị (The first shift is a customized data path: matrix multiplication units in AI accelerators, for example, implement systolic arrays, grid-like networks of processing elements that rhythmically compute and pass data through neighboring units). Một khi đó dữ liệu đường dẫn là cố định, bộ nhớ hệ thống phân cấp có thể được tinh chỉnh xung quanh sự tái sử dụng mẫu khối lượng công việc thực sự cần, với bộ nhớ đệm các cấu hình, việc tìm nạp trước logic, và bộ nhớ các bộ điều khiển được thiết kế cho mong đợi tensor dòng (Once that data path is fixed, the memory hierarchy can be tuned around the reuse pattern the workload actually needs, with cache configurations, prefetching logic, and memory controllers designed for the expected tensor flow).
Cùng sự chuyên biệt hóa sau đó làm giảm bớt kiểm soát chi phí quản lý (The same specialization then reduces control overhead). Cụ thể-miền lệnh các tập hợp mã hóa phổ biến hoạt động các chuỗi thành đơn các lệnh, việc tối thiểu hóa sự giải mã và sự điều phối tính phức tạp, trong khi cố định-chức năng mạch điện các khối bỏ qua phần mềm sự diễn giải cho các hoạt động thứ mà xuất hiện

================ PAGE 596 ================

558
11.2 Phần cứng Sự chuyên biệt hóa (Hardware Specialization)
10
Codec (Codec): Một từ ghép
của "coder-decoder" (bộ mã hóa-bộ giải mã), việc phản ánh
phần cứng của kép chức năng (A portmanteau of “coder-decoder,” reflecting the hardware’s dual function).
Việc mã hóa (sự nén) là
thâm dụng-tính toán
bởi vì
nó
tìm kiếm
cho
tối ưu
các sự đại diện,
trong khi
việc giải mã (sự giải nén) là
thâm dụng-băng thông bởi vì
nó tái tạo đầy đủ-độ phân giải
các khung hình
từ
được nén
các luồng (Encoding (compression) is compute-intensive because it searches for optimal representations, while decoding (decompression) is bandwidth-intensive because it reconstructs full-resolution frames from compressed streams).
Được cống hiến codec
silicon triển khai cả hai các đường dẫn
trong cố định-chức năng phần cứng,
vì vậy
không cái nào
đường dẫn
lãng phí
các transistor
trên
không liên quan
đa-mục đích
kiểm soát
logic (Dedicated codec silicon implements both paths in fixed-function hardware, so neither path wastes transistors on unrelated general-purpose control logic).
11
ASIC (Cụ thể-Ứng dụng
Tích hợp Mạch điện) (ASIC (Application-Specific Integrated Circuit)):
Những các mạch điện này đạt được của chúng
cực độ tính hiệu quả bằng cách việc triển khai một đơn thuật toán một cách trực tiếp trong silicon, thường việc cải thiện hiệu suất-trên-watt bởi
103× tới 105× (These circuits achieve their extreme efficiency by implementing a single algorithm directly in silicon, often improving performance-per-watt by 103× to 105×).
Các ví dụ
bao gồm mật mã việc băm cho blockchain việc khai thác và
chuỗi sự căn chỉnh cho hệ gen học (Examples include cryptographic hashing for blockchain mining and sequence alignment for genomics). Sự đánh đổi là tổng
tính không linh hoạt: nếu đó cốt lõi thuật toán thay đổi, ASIC không thể được lập trình lại và trở nên lỗi thời, việc khóa
phần cứng thiết kế tới cụ thể vấn đề phiên bản nó đã từng
được xây dựng để giải quyết (The trade-off is total inflexibility: if that core algorithm changes, the ASIC cannot be reprogrammed and becomes obsolete, locking the hardware design to the specific problem version it was built to solve).
liên tục (constantly). Kết quả là không một thủ thuật mà một ngăn xếp của khớp các quyết định: dữ liệu sự di chuyển, bộ nhớ tính cục bộ, lệnh chi phí quản lý, và mạch điện sự triển khai tất cả căn chỉnh xung quanh cùng tính toán mẫu (The result is not one trick but a stack of matching decisions: data movement, memory locality, instruction overhead, and circuit implementation all align around the same computational pattern).
Hiện đại các điện thoại thông minh minh họa những các nguyên lý này một cách hấp dẫn (Modern smartphones illustrate these principles compellingly). Chúng có thể giải mã cao-độ phân giải video trong vòng chặt chẽ năng lượng và nhiệt các vỏ bọc mặc dù video việc xử lý yêu cầu hàng tỷ của các hoạt động trên giây (They can decode high-resolution video within tight power and thermal envelopes even though video processing requires billions of operations per second). Này tính hiệu quả được đạt được thông qua được cống hiến phần cứng video các codec10 thứ mà triển khai công nghiệp các tiêu chuẩn chẳng hạn như H.264/AVC và H.265/HEVC (Sullivan et al. 2012) (This efficiency is achieved through dedicated hardware video codecs10 that implement industry standards such as H.264/AVC and H.265/HEVC (Sullivan et al. 2012)). Những chuyên biệt các mạch điện này có thể cung cấp bậc-của-độ lớn hiệu suất-trên-watt các phần tăng được so sánh với phần mềm việc giải mã trên đa-mục đích các bộ xử lý, với chính xác phần tăng phụ thuộc trên codec, độ phân giải, quá trình nút, và CPU đường cơ sở (These specialized circuits can provide order-of-magnitude performance-per-watt gains compared with software decoding on general-purpose processors, with the exact gain depending on codec, resolution, process node, and CPU baseline).
Những sau này các miền là không riêng biệt các giai thoại; chúng lặp lại cùng nút thắt cổ chai phản hồi (These later domains are not separate anecdotes; they repeat the same bottleneck response). Hệ gen học việc xử lý hưởng lợi từ tùy chỉnh các máy gia tốc bởi vì chuỗi sự căn chỉnh và biến thể việc gọi phơi bày ổn định các hạt nhân thứ mà chuyên biệt silicon có thể thực thi với ít hơn bị lãng phí sự di chuyển (Shang et al. 2018) (Genomics processing benefits from custom accelerators because sequence alignment and variant calling expose stable kernels that specialized silicon can execute with less wasted movement (Shang et al. 2018)). Blockchain sự tính toán đã sản xuất cụ thể-ứng dụng tích hợp các mạch điện (các ASIC)11 cho cùng lý do: mật mã việc băm là đủ cố định để biện minh silicon thứ mà đánh đổi tính linh hoạt cho tính hiệu quả (Bedford Taylor 2017) (Blockchain computation produced application-specific integrated circuits (ASICs)11 for the same reason: cryptographic hashing is fixed enough to justify silicon that trades flexibility for efficiency (Bedford Taylor 2017)).
Quỹ đạo mang lại một kỹ thuật quy tắc: kỷ nguyên của "miễn phí" hiệu suất các phần tăng từ đa-mục đích sự chia tỷ lệ là qua (The trajectory yields an engineering rule: the era of “free” performance gains from general-purpose scaling is over). Cho các thập kỷ, phần mềm các kỹ sư có thể dựa dẫm trên Moore của Định luật để tăng tốc tồn tại mã mà không có thuộc về kiến trúc các thay đổi (For decades, software engineers could rely on Moore’s Law to accelerate existing code without architectural changes). Sự phá vỡ của Dennard sự chia tỷ lệ đã ép buộc một dứt khoát sự thay đổi: các kỹ sư không thể lâu hơn chờ đợi cho nhanh hơn các CPU để giải quyết tính toán các nút thắt cổ chai mà phải thay vào đó thiết kế phần cứng để khớp thuật toán (The breakdown of Dennard scaling forced a decisive change: engineers can no longer wait for faster CPUs to solve computational bottlenecks but must instead design the hardware to fit the algorithm). Này sự cần thiết của phần cứng-phần mềm sự đồng thiết kế là tại sao hiện đại AI kỹ thuật yêu cầu sâu sự hiểu biết của nằm bên dưới silicon (This necessity of hardware-software co-design is why modern AI engineering requires deep understanding of the underlying silicon). Hiệu suất là bây giờ được xác định bởi cách nào tốt thuật toán của bộ nhớ truy cập các mẫu và sự song song ánh xạ tới chuyên biệt vật lý các cấu trúc của cụ thể-miền các kiến trúc (Performance is now determined by how well the algorithm’s memory access patterns and parallelism map to the specialized physical structures of domain-specific architectures).
11.2.5 Máy học hỏi phần cứng sự chuyên biệt hóa (Machine learning hardware specialization)
Máy học hỏi tạo thành một tính toán miền với độc đáo các đặc điểm thứ mà đã dẫn dắt sự phát triển của chuyên biệt phần cứng các kiến trúc (Machine learning constitutes a computational domain with unique characteristics that have driven the development of specialized hardware architectures). Không giống truyền thống việc điện toán các khối lượng công việc thứ mà trưng bày không đều bộ nhớ truy cập các mẫu và đa dạng lệnh các luồng, thần kinh các mạng được đặc trưng bởi có thể dự đoán các mẫu: dày đặc ma trận các phép nhân, đều đặn dữ liệu dòng, và sự dung sai cho được làm giảm bớt độ chính xác (Unlike traditional computing workloads that exhibit irregular memory access patterns and diverse instruction streams, neural networks are characterized by predictable patterns: dense matrix multiplications, regular data flow, and tolerance for reduced precision). Những các đặc điểm này cho phép chuyên biệt phần cứng các sự tối ưu hóa thứ mà sẽ không hiệu quả cho đa-mục đích việc điện toán nhưng cung cấp đáng kể các phần tăng tốc cho ML các khối lượng công việc (These characteristics enable specialized hardware optimizations that would be ineffective for general-purpose computing but provide substantial speedups for ML workloads).
Phần cứng được xây dựng để khai thác những các mẫu này tạo thành một lớp của các thiết bị được biết như ML các máy gia tốc, và kinh tế kích hoạt cho sự chuyên biệt hóa xuất hiện khi những đều đặn thần kinh-mạng các mẫu đó thống trị một hạm đội thay vì một chuẩn đối sánh (The hardware built to exploit these patterns constitutes a class of devices known as ML accelerators, and the economic trigger for specialization appears when those regular neural-network patterns dominate a fleet rather than a benchmark).
Chiến tranh Câu chuyện 11.1: TPU dung lượng vách đá (War Story 11.1: The TPU capacity cliff)
Ngữ cảnh: Google đã xem xét một cụ thể-ứng dụng chip cho thần kinh các mạng sớm nhất là 2006 nhưng đã không đối xử nó như khẩn cấp: tồn tại dữ liệu-trung tâm dung lượng đã hấp thụ sớm sâu-sự học hỏi các khối lượng công việc (Jouppi et al. 2017) (Context: Google had considered an application-specific chip for neural networks as early as 2006 but did not treat it as urgent: existing data-center capacity absorbed the early deep-learning workloads (Jouppi et al. 2017)).
Sự thất bại chế độ: Trong 2013, nội bộ các dự phóng đã thay đổi sự tính toán (Failure mode: In 2013, internal projections changed the calculus). Nếu người dùng đã áp dụng được dẫn dắt-bởi-giọng nói-sự tìm kiếm tiếng nói sự nhận diện cho thậm chí một vài các phút mỗi ngày, kết quả sự suy luận tải trọng từ sâu thần kinh các mạng sẽ đại khái nhân đôi số lượng của các dữ liệu trung tâm Google cần thiết để vận hành (If users adopted voice-search-driven speech recognition for even a few minutes per day, the resulting inference load from deep neural networks would roughly double the number of data centers Google needed to operate). Đã có không thực tế vốn kế hoạch để hấp thụ điều đó, và thông thường các CPU đã cung cấp không đường dẫn để đóng khoảng cách trên hiệu suất trên watt hoặc hiệu suất trên đô la (Jouppi et al. 2017) (There was no realistic capital plan to absorb that, and conventional CPUs offered no path to close the gap on performance per watt or performance per dollar (Jouppi et al. 2017)).
Sự giải quyết: Google đã bắt đầu một cao-sự ưu tiên tùy chỉnh-ASIC nỗ lực và, trong mười lăm các tháng, đã thiết kế, xác minh, xây dựng, và triển khai đầu tiên-thế hệ Tensor Xử lý Đơn vị (TPU) vào sản xuất dữ liệu các trung tâm trong 2015, việc tối ưu hóa cho sự suy luận độ trễ, chi phí, và hiệu suất trên watt thay vì đa-mục đích tính linh hoạt (Jouppi et al. 2017) (Resolution: Google started a high-priority custom-ASIC effort and, in fifteen months, designed, verified, built, and deployed the first-generation Tensor Processing Unit (TPU) into production data centers in 2015, optimizing for inference latency, cost, and performance per watt rather than general-purpose flexibility (Jouppi et al. 2017)).
Các hệ thống bài học: Phần cứng sự gia tốc trở thành bắt buộc khi một đơn khối lượng công việc vượt qua một cấp-hạm đội kinh tế ngưỡng (Systems lesson: Hardware acceleration becomes mandatory when a single workload crosses a fleet-level economic threshold). Quyết định là không "CPU so với GPU so với TPU" trong trừu tượng; nó là liệu khối lượng công việc của số học cường độ, độ trễ mục tiêu, và tổng khối lượng làm đa-mục đích dung lượng không thể chi trả (The decision is not “CPU vs. GPU vs. TPU” in the abstract; it is whether the workload’s arithmetic intensity, latency target, and aggregate volume make general-purpose capacity unaffordable).

================ PAGE 597 ================

11. Phần cứng Sự gia tốc (Hardware Acceleration)
559
Một DRAM truy cập chi phí ~100× một
MAC; dữ liệu sự di chuyển thống trị
năng lượng (A DRAM access costs ~100× a MAC; data movement dominates energy).
12
Độ trễ so với Thông lượng
trong Máy gia tốc Thiết kế (Latency vs. Throughput in Accelerator Design): Việc đào tạo của hai chiều dữ liệu dòng
và lớn sự kích hoạt bộ nhớ
dấu chân ủng hộ hướng-thông lượng các thiết kế thứ mà sử dụng
lớn các lô để tối đa hóa
số học sự tận dụng (Training’s bidirectional data flow and large activation memory footprint favor throughput-oriented designs that use large batches to maximize arithmetic utilization). Sự suy luận của đơn giản chuyển tiếp-lượt
sự tính toán, bởi sự tương phản, là
được đánh giá trên độ trễ,
nơi
đơn-yêu cầu phản hồi thời gian
là chỉ số quan trọng (Inference’s simple forward-pass computation, by contrast, is judged on latency, where single-request response time is the critical metric).
Điều này
ép buộc một phần cứng sự đánh đổi:
một được tối ưu hóa-sự đào tạo kiến trúc được xây dựng để tối đa hóa
FLOP/s
có thể
giới thiệu
đường ống và việc tạo lô chi phí quản lý
thứ mà làm tồi tệ hơn đuôi độ trễ
cho nhạy cảm-độ trễ sự suy luận
các khối lượng công việc được so sánh với
một
chip
hoặc
thời gian chạy
đường dẫn
được tối ưu hóa cho đơn-yêu cầu
dịch vụ (This forces a hardware trade-off: a training-optimized architecture built to maximize FLOP/s can introduce pipeline and batching overhead that worsens tail latency for latency-sensitive inference workloads compared with a chip or runtime path optimized for single-request service).
Định nghĩa 11.3: ML máy gia tốc (ML accelerator)
Máy Học hỏi Các máy gia tốc là cụ thể-miền các bộ xử lý của đó silicon được thiết kế chủ yếu cho dày đặc ma trận các hoạt động và đều đặn dữ liệu dòng của thần kinh các mạng, việc đạt được cao 𝑅peak và bộ nhớ băng thông sự tận dụng cho những các khối lượng công việc này bằng cách việc cống hiến khuôn diện tích tới số học các đơn vị thay vì tới đa-mục đích kiểm soát logic (Machine Learning Accelerators are domain-specific processors whose silicon is designed primarily for the dense matrix operations and regular data flow of neural networks, achieving high 𝑅peak and memory bandwidth utilization for these workloads by devoting die area to arithmetic units rather than to general-purpose control logic).
1. Tầm quan trọng: Một ML máy gia tốc của định nghĩa tính năng là không thô số học mà một cân bằng nguồn cấp của dữ liệu tới đó số học (Significance: An ML accelerator’s defining feature is not raw arithmetic but a balanced feed of data to that arithmetic). A100 của 2.04 TB/s của bộ nhớ băng thông, đại khái một 10× khoảng cách qua một máy chủ CPU của 200 GB/s, là cái gì để nó của 312 TFLOP/s của FP16/BF16 thông lượng giữ nguyên được nuôi dưỡng thay vì bị chết đói (NVIDIA Corporation 2020; Choquette et al. 2021) (The A100’s 2.04 TB/s of memory bandwidth, roughly a 10× gap over a server CPU’s 200 GB/s, is what lets its 312 TFLOP/s of FP16/BF16 throughput stay fed rather than starved (NVIDIA Corporation 2020; Choquette et al. 2021)). Đó sự cân bằng là sau đó được chuyên biệt hóa bởi khối lượng công việc: sự đào tạo các máy gia tốc định cỡ FLOP/s và băng thông cho hai chiều gradient dòng và lớn sự kích hoạt các dấu chân, trong khi sự suy luận các máy gia tốc đánh đổi chúng cho năng lượng tính hiệu quả và xác định đơn-yêu cầu độ trễ (That balance is then specialized by workload: training accelerators size FLOP/s and bandwidth for bidirectional gradient flow and large activation footprints, while inference accelerators trade those for energy efficiency and deterministic single-request latency).
2. Sự khác biệt: Máy gia tốc của các phần tăng là có điều kiện trên dữ liệu việc chảy thông qua nó là song song và đều đặn (Distinction: The accelerator’s gains are conditional on the data flowing through it being parallel and regular). Một ML máy gia tốc xử lý hàng ngàn của độc lập số học các hoạt động ở một lần với có thể dự đoán bộ nhớ truy cập, vì vậy nó là các bậc của độ lớn nhanh hơn một CPU trên dày đặc ma trận phép nhân nhưng có thể chậm hơn trên không đều kiểm soát dòng chẳng hạn như cây sự đi ngang qua hoặc động quy hoạch, nơi có không song song dữ liệu luồng để nuôi dưỡng (An ML accelerator processes thousands of independent arithmetic operations at once with predictable memory access, so it is orders of magnitude faster than a CPU on dense matrix multiplication but can be slower on irregular control flow such as tree traversal or dynamic programming, where there is no parallel data stream to feed).
3. Phổ biến cạm bẫy: Một thường xuyên sự quan niệm sai lầm là rằng ML các máy gia tốc luôn luôn tăng tốc ML (Common pitfall: A frequent misconception is that ML accelerators always accelerate ML). Một máy gia tốc chỉ phân phối của nó đỉnh thông lượng khi khối lượng công việc cung cấp đủ song song công việc để bão hòa tất cả số học các đơn vị một cách đồng thời: một lô-1 tự hồi quy sự suy luận yêu cầu có thể sử dụng chỉ một nhỏ phần nhỏ của một lớn sự đào tạo máy gia tốc của tính toán dung lượng bởi vì tuần tự token sự sinh ra không thể lấp đầy hàng ngàn của song song tính toán các làn đường (An accelerator only delivers its peak throughput when the workload provides enough parallel work to saturate all arithmetic units simultaneously: a batch-1 autoregressive inference request may use only a small fraction of a large training accelerator’s compute capacity because sequential token generation cannot fill thousands of parallel compute lanes).
Máy học hỏi tính toán các yêu cầu tiết lộ các sự giới hạn trong truyền thống các bộ xử lý (Machine learning computational requirements reveal limitations in traditional processors). Các CPU đạt tới chỉ 5 phần trăm–10 phần trăm sự tận dụng trên thần kinh mạng các khối lượng công việc, việc phân phối xấp xỉ 100 GFLOP/s (hàng tỷ của dấu phẩy-động các hoạt động trên giây) trong khi việc tiêu thụ hàng trăm của các watt (CPUs reach only 5 percent–10 percent utilization on neural network workloads, delivering approximately 100 GFLOP/s (billions of floating-point operations per second) while consuming hundreds of watts). Này sự không hiệu quả là kết quả từ thuộc về kiến trúc các sự không khớp: các CPU tối ưu hóa cho đơn-luồng hiệu suất và không đều bộ nhớ truy cập, trong khi thần kinh các mạng yêu cầu đồ sộ sự song song và có thể dự đoán dữ liệu các luồng (This inefficiency results from architectural mismatches: CPUs optimize for single-thread performance and irregular memory access, while neural networks require massive parallelism and predictable data streams). Bộ nhớ băng thông sự ràng buộc làm phức tạp vấn đề: một đơn thần kinh mạng lớp có thể yêu cầu việc truy cập các gigabyte của các tham số, việc áp đảo CPU bộ nhớ đệm các hệ thống phân cấp được thiết kế cho cấp-kilobyte làm việc các tập hợp (The memory bandwidth constraint compounds the problem: a single neural network layer may require accessing gigabytes of parameters, overwhelming CPU cache hierarchies designed for kilobyte-scale working sets).
Năng lượng kinh tế của dữ liệu sự di chuyển ảnh hưởng máy gia tốc thiết kế (The energy economics of data movement influence accelerator design). Việc truy cập dữ liệu từ DRAM có thể tiêu thụ trên bậc của 102× nhiều hơn năng lượng so với một nhân-tích lũy hoạt động (chính xác các giá trị thay đổi bởi công nghệ nút và thiết kế), việc làm việc tối thiểu hóa dữ liệu sự di chuyển một chính sự tối ưu hóa mục tiêu (Horowitz 2014; Sze et al. 2017) (Accessing data from DRAM can consume on the order of 102× more energy than a multiply-accumulate operation (exact values vary by technology node and design), making minimizing data movement a primary optimization target (Horowitz 2014; Sze et al. 2017)). Sự chênh lệch này giúp giải thích sự tiến triển từ được tái sử dụng đồ họa các bộ xử lý tới được xây dựng-cho-mục đích thần kinh mạng các máy gia tốc (This disparity helps explain the progression from repurposed graphics processors to purpose-built neural network accelerators). Các TPU và khác tùy chỉnh các máy gia tốc có thể duy trì cao sự tận dụng trên dày đặc các hạt nhân bằng cách việc triển khai tâm thu các mảng và khác các kiến trúc thứ mà tối đa hóa dữ liệu sự tái sử dụng trong khi việc tối thiểu hóa sự di chuyển (TPUs and other custom accelerators can sustain high utilization on dense kernels by implementing systolic arrays and other architectures that maximize data reuse while minimizing movement).
Việc đào tạo và sự suy luận xuất trình khác biệt tính toán các hồ sơ thứ mà ảnh hưởng máy gia tốc thiết kế (Training and inference present distinct computational profiles that influence accelerator design). Việc đào tạo nói chung dựa dẫm trên dấu phẩy-động số học cho gradient sự tính toán và trọng số các sự cập nhật: FP32 và FP16 là được tiêu chuẩn hóa nhị phân dấu phẩy-động các định dạng (IEEE Standards Association 2019b), trong khi hỗn hợp-độ chính xác sự đào tạo sử dụng thấp hơn-độ chính xác tensor các hoạt động với cao hơn-độ chính xác sự tích lũy khi độ chính xác cho phép (Micikevicius et al. 2017) (Training generally relies on floating-point arithmetic for gradient computation and weight updates: FP32 and FP16 are standardized binary floating-point formats (IEEE Standards Association 2019b), while mixed-precision training uses lower-precision tensor operations with higher-precision accumulation when accuracy permits (Micikevicius et al. 2017)). Việc đào tạo cũng yêu cầu hai chiều dữ liệu dòng cho lan truyền ngược (xem phần 8.3.3.1 cho sự kích hoạt bộ nhớ sự phân tích), và lớn bộ nhớ dung lượng cho việc lưu trữ các sự kích hoạt (Training also requires bidirectional data flow for backpropagation (see section 8.3.3.1 for activation memory analysis), and large memory capacity for storing activations). Sự suy luận có thể khai thác được làm giảm bớt độ chính xác (INT8 hoặc INT4), yêu cầu chỉ chuyển tiếp sự tính toán, và ưu tiên độ trễ qua thông lượng12 (Inference can exploit reduced precision (INT8 or INT4), requires only forward computation, and prioritizes latency over throughput12). Những các sự khác biệt này dẫn dắt chuyên biệt các kiến trúc: sự đào tạo các máy gia tốc tối đa hóa FLOP/s và bộ nhớ băng thông, trong khi sự suy luận các máy gia tốc tối ưu hóa cho năng lượng tính hiệu quả và xác định độ trễ (These differences drive specialized architectures: training accelerators maximize FLOP/s and memory bandwidth, while inference accelerators optimize for energy efficiency and deterministic latency).
Sự triển khai ngữ cảnh định hình thuộc về kiến trúc các sự chọn lựa bằng cách việc nhận dạng sự ràng buộc (Deployment context shapes architectural choices by identifying the binding constraint). Trong dữ liệu các trung tâm, sự ràng buộc là thời gian-tới-kết quả cho việc đào tạo đồ sộ các mô hình (In data centers, the constraint is time-to-result for training massive models). Một NVIDIA H100 việc tiêu thụ

================ PAGE 598 ================

560
11.2 Phần cứng Sự chuyên biệt hóa (Hardware Specialization)
hàng trăm của các watt là được biện minh về mặt kinh tế nếu nó làm giảm bớt một cấp-GPT sự đào tạo chạy từ các tuần tới các ngày, bởi vì tích lũy chi phí của được thuê máy gia tốc thời gian thường làm lu mờ năng lượng hóa đơn (Choquette 2023) (hundreds of watts is economically justified if it reduces a GPT-scale training run from weeks to days, because the cumulative cost of rented accelerator time usually dwarfs the energy bill (Choquette 2023)). Google của TPUv4 tạo ra một tương tự sự đánh đổi, việc ưu tiên thô thông lượng thông qua đồ sộ tâm thu các mảng và cao-băng thông bộ nhớ (Jouppi et al. 2023), việc chấp nhận cao năng lượng sự tiêu thụ bởi vì nhanh hơn sự lặp lại làm giảm bớt cả hai thời gian-để-triển khai và tổng sự đào tạo chi phí (Google’s TPUv4 makes a similar trade-off, prioritizing raw throughput through massive systolic arrays and high-bandwidth memory (Jouppi et al. 2023), accepting high power consumption because faster iteration reduces both time-to-deploy and total training cost).
Ở đối diện thái cực, rìa sự triển khai đảo ngược điều này sự ưu tiên: sự ràng buộc là năng lượng trên sự suy luận, không thông lượng (At the opposite extreme, edge deployment inverts this priority: the binding constraint is energy per inference, not throughput). Một điện thoại thông minh máy ảnh hoặc luôn-bật âm thanh đường dẫn hoạt động bên trong một vài-watt năng lượng ngân sách không thể chi trả thâm dụng-DRAM truy cập các mẫu của một dữ liệu trung tâm máy gia tốc (A smartphone camera or always-on audio path operating inside a few-watt power budget cannot afford the DRAM-intensive access patterns of a data center accelerator). Thay vào đó, rìa các kiến trúc tối thiểu hóa dữ liệu sự di chuyển thông qua cục bộ các sổ nháp, chặt chẽ được tích hợp các máy gia tốc, động điện áp sự chia tỷ lệ, và được dẫn dắt-bởi-sự kiện việc xử lý khi khối lượng công việc cho phép nó (Instead, edge architectures minimize data movement through local scratchpads, tightly integrated accelerators, dynamic voltage scaling, and event-driven processing when the workload allows it). Các hệ thống sự thấu hiểu là rằng cùng bộ nhớ bức tường nguyên lý áp dụng ở cả hai các thái cực: dữ liệu trung tâm các chip chiến đấu nó với băng thông (các terabyte trên giây của HBM), trong khi rìa các chip chiến đấu nó với sự gần gũi (việc giữ dữ liệu trong các thanh ghi và các sổ nháp) (The systems insight is that the same memory wall principle applies at both extremes: data center chips fight it with bandwidth (terabytes per second of HBM), while edge chips fight it with proximity (keeping data in registers and scratchpads)).
Sự thành công của cụ thể-ứng dụng các máy gia tốc chứng minh rằng không đơn kiến trúc có thể một cách hiệu quả giải quyết tất cả ML các khối lượng công việc (The success of application-specific accelerators demonstrates that no single architecture can efficiently address all ML workloads). Một đồ sộ được cài đặt cơ sở của rìa các thiết bị yêu cầu các kiến trúc được tối ưu hóa cho năng lượng tính hiệu quả và thời gian-thực độ trễ các mục tiêu, trong khi cấp-đám mây sự đào tạo tiếp tục việc nâng cao các ranh giới của tính toán thông lượng (A massive installed base of edge devices demands architectures optimized for energy efficiency and real-time latency targets, while cloud-scale training continues advancing the boundaries of computational throughput). Sự đa dạng này dẫn dắt tiếp tục sự đổi mới trong chuyên biệt các kiến trúc, mỗi cái được tối ưu hóa cho của nó cụ thể sự triển khai ngữ cảnh và tính toán các yêu cầu (This diversity drives continued innovation in specialized architectures, each optimized for its specific deployment context and computational requirements). Tuy nhiên, mặc dù điều này sự đa dạng, tất cả các máy gia tốc hoạt động dưới cùng vật lý sự ràng buộc: năng lượng chi phí của việc di chuyển dữ liệu (However, despite this diversity, all accelerators operate under the same physical constraint: the energy cost of moving data).
Điểm kiểm tra 11.2: Máy gia tốc cổng (Checkpoint 11.2: The accelerator gate)
Phần cứng sự chuyên biệt hóa là được dẫn dắt bởi năng lượng vật lý (Hardware specialization is driven by energy physics).
Năng lượng Sự đảo ngược (The Energy Inversion)
□ Dữ liệu sự di chuyển chi phí: Bạn có thể giải thích tại sao việc di chuyển dữ liệu từ DRAM tốn 100× nhiều hơn năng lượng so với việc tính toán trên nó? (Data movement cost: Can you explain why moving data from DRAM costs 100× more energy than computing on it?)
□ Thuộc về kiến trúc phản hồi: Giải thích cách nào tâm thu các mảng (TPU) và Tensor Các lõi (GPU) làm giảm bớt lặp lại sự di chuyển của cùng các toán hạng (Architectural response: Explain how systolic arrays (TPU) and Tensor Cores (GPU) reduce repeated movement of the same operands.)
Sự chọn lựa Logic (Selection Logic)
□ Việc đào tạo so với sự suy luận: Tại sao sự đào tạo các chip cần đồ sộ HBM băng thông, trong khi sự suy luận các chip ưu tiên thấp độ trễ và INT8 các hoạt động? (Training vs. inference: Why do training chips need massive HBM bandwidth, while inference chips prioritize low latency and INT8 ops?)
Điều này lịch sử sự tiến triển tiết lộ một chính mẫu: mỗi làn sóng của phần cứng sự chuyên biệt hóa đã phản hồi tới một cụ thể tính toán nút thắt cổ chai (This historical progression reveals a key pattern: each wave of hardware specialization responded to a specific computational bottleneck). Dấu phẩy-động các bộ đồng xử lý đã giải quyết số học độ chính xác; các GPU đã giải quyết đồ họa thông lượng; AI sự gia tốc nhắm mục tiêu một cách chất lượng khác nhau sự ràng buộc, sự tích hợp nút thắt cổ chai được kiểm tra trong phần 11.2.6 (Floating-point coprocessors addressed arithmetic precision; GPUs addressed graphics throughput; AI acceleration targets a qualitatively different constraint, the integration bottleneck examined in section 11.2.6). Bảng 11.1 tóm tắt chính các cột mốc trong phần cứng sự chuyên biệt hóa (Table 11.1 summarizes the key milestones in hardware specialization). Thuộc về kiến trúc các chiến lược được giới thiệu cho những sớm hơn chuyên biệt các khối lượng công việc này (dấu phẩy-động các hoạt động, đồ họa việc kết xuất, phương tiện việc xử lý) bây giờ củng cố thiết kế của hiện đại AI các máy gia tốc và cung cấp ngữ cảnh cho việc hiểu cách nào phần cứng sự chuyên biệt hóa tiếp tục để cho phép có thể chia tỷ lệ, hiệu quả sự thực thi của máy học hỏi các khối lượng công việc qua đa dạng sự triển khai các môi trường (The architectural strategies introduced for these earlier specialized workloads (floating-point operations, graphics rendering, media processing) now underpin the design of modern AI accelerators and provide context for understanding how hardware specialization continues to enable scalable, efficient execution of machine learning workloads across diverse deployment environments).
Cái gì phân biệt AI sự gia tốc từ sớm hơn sự chuyên biệt hóa các làn sóng là quy mô của sự tích hợp được yêu cầu (What distinguishes AI acceleration from earlier specialization waves is the scale of integration required). AI các máy gia tốc phải làm việc một cách liền mạch với các khuôn khổ giống như TensorFlow, PyTorch, và JAX (AI accelerators must work seamlessly with frameworks like TensorFlow, PyTorch, and JAX). Chúng yêu cầu sâu trình biên dịch sự hỗ trợ cho cấp-đồ thị các sự biến đổi, hạt nhân sự hợp nhất, và bộ nhớ việc lập lịch (They require deep compiler support for graph-level transformations, kernel fusion, and memory scheduling). Chúng phải cũng triển khai qua các môi trường từ dữ liệu các trung tâm tới di động các thiết bị, mỗi cái với khác biệt hiệu suất và tính hiệu quả các yêu cầu (They must also deploy across environments from data centers to mobile devices, each with distinct performance and efficiency requirements). Như vậy cấp-hệ thống sự biến đổi yêu cầu chặt chẽ phần cứng-phần mềm sự ghép cặp, một chủ đề thứ mà lặp lại xuyên suốt điều này chương (Such system-level transformation requires tight hardware-software coupling, a theme that recurs throughout this chapter).
AI các máy gia tốc nhắm mục tiêu một cụ thể nút thắt cổ chai của đó danh tính định hình mọi tiếp theo thuộc về kiến trúc quyết định (AI accelerators target a specific bottleneck whose identity shapes every subsequent architectural decision). Không giống dấu phẩy-động các bộ đồng xử lý thứ mà đã giải quyết số học độ chính xác hoặc các GPU thứ mà đã giải quyết đồ họa thông lượng, AI các máy gia tốc nhắm mục tiêu một cách chất lượng khác nhau sự ràng buộc: sự tích hợp nút thắt cổ chai được giới thiệu tiếp theo (Unlike floating-point coprocessors that addressed arithmetic precision or GPUs that addressed graphics throughput, AI accelerators target a qualitatively different constraint: the integration bottleneck introduced next).

================ PAGE 599 ================

11. Phần cứng Sự gia tốc (Hardware Acceleration)
561
13
Sổ nháp Bộ nhớ (Scratchpad Memory):
Bởi vì
dữ liệu dòng
cho
một thần kinh mạng là về mặt toán học
được xác định,
một
trình biên dịch có thể lập lịch
chính xác dữ liệu được cần vào này
nhanh, được kiểm soát-bởi-phần mềm cục bộ
bộ nhớ (Because the dataflow for a neural network is mathematically determined, a compiler can schedule the exact data needed into this fast, software-controlled local memory). Điều này bỏ qua
phức tạp và thâm dụng-năng lượng
phần cứng logic một CPU bộ nhớ đệm
sử dụng để đoán ở tương lai dữ liệu
nhu cầu
cho
không thể dự đoán
các khối lượng công việc (This bypasses the complex and energy-intensive hardware logic a CPU cache uses to guess at future data needs for unpredictable workloads).
Cho ví dụ,
Google của TPU v1 sử dụng một 24 MB
được quản lý-bởi-phần mềm
Được hợp nhất
Bộ đệm thay vì việc dựa dẫm trên
kiểu-CPU phần cứng các bộ nhớ đệm
cho các sự kích hoạt,
một chính
bộ dẫn động của của nó tính hiệu quả trên ML
các khối lượng công việc (Jouppi et al. 2017) (For example, Google’s TPU v1 uses a 24 MB software-managed Unified Buffer rather than relying on CPU-style hardware caches for activations, a primary driver of its efficiency on ML workloads (Jouppi et al. 2017)).
14
HBM (Cao Băng thông
Bộ nhớ) (HBM (High Bandwidth Memory)): Đạt được 2.0–3.4
TB/s băng thông trong hiện tại
dữ liệu
trung tâm
các máy gia tốc
(A100 của HBM2e tới H100 của
HBM3)
thông qua
3D
khuôn
việc xếp chồng
với
hàng ngàn
của
xuyên-silicon
các via
(TSVs),
được so sánh
tới
760
GB/s cho GDDR6X (NVIDIA
Corporation 2020; Choquette
2023) (Achieves 2.0–3.4 TB/s bandwidth in current data center accelerators (A100’s HBM2e to H100’s HBM3) through 3D die stacking with thousands of through-silicon vias (TSVs), compared to 760 GB/s for GDDR6X (NVIDIA Corporation 2020; Choquette 2023)).
Điều này 2.7–4.4× băng thông
lợi thế biến đổi
bị ràng buộc-bởi-bộ nhớ
ML
các khối lượng công việc
hướng tới bị ràng buộc-bởi-tính toán
hiệu suất, thứ mà là tại sao
cao-cấp dữ liệu trung tâm AI các máy gia tốc
chẳng hạn như H100, A100,
và TPUv4 sử dụng HBM (Jouppi
et al. 2023) (This 2.7–4.4× bandwidth advantage transforms memory-bound ML workloads toward compute-bound performance, which is why high-end data center AI accelerators such as H100, A100, and TPUv4 use HBM (Jouppi et al. 2023)). Sự đánh đổi là
chi phí: HBM là một thống trị chi phí
thành phần trong dữ liệu trung tâm
AI các máy gia tốc, việc giới hạn nó
tới các ứng dụng nơi
băng thông-trên-đô la
biện minh
đáng kể phần bù
qua cấp-người tiêu dùng GDDR (The trade-off is cost: HBM is a dominant cost component in data center AI accelerators, limiting it to applications where the bandwidth-per-dollar justifies the substantial premium over consumer-grade GDDR).
Bảng 11.1: Phần cứng Sự chuyên biệt hóa Các xu hướng: Kế tiếp việc điện toán các kỷ nguyên một cách tiến bộ tích hợp chuyên biệt phần cứng để tăng tốc phổ biến các khối lượng công việc, việc di chuyển từ đa-mục đích các CPU tới cụ thể-miền các kiến trúc và cuối cùng tới có thể tùy chỉnh AI các máy gia tốc (Table 11.1: Hardware Specialization Trends: Successive computing eras progressively integrate specialized hardware to accelerate prevalent workloads, moving from general-purpose CPUs to domain-specific architectures and ultimately to customizable AI accelerators). Việc may đo phần cứng tới tính toán các mẫu cải thiện hiệu suất và năng lượng tính hiệu quả, việc dẫn dắt sự đổi mới trong máy học hỏi các hệ thống (Tailoring hardware to computational patterns improves performance and energy efficiency, driving innovation in machine learning systems).
Kỷ nguyên (Era)
Tính toán Mẫu (Computational Pattern)
Kiến trúc Các ví dụ (Architecture Examples)
Các đặc điểm (Characteristics)
Các 1980s
Dấu phẩy-Động & Tín hiệu
Việc xử lý (Floating-Point & Signal Processing)
FPU, DSP
• Đơn-mục đích các động cơ (Single-purpose engines)
• Được tập trung lệnh các tập hợp (Focused instruction sets)
• Bộ đồng xử lý các giao diện (Coprocessor interfaces)
Các 1990s
3D Đồ họa & Đa phương tiện (3D Graphics & Multimedia)
GPU, SIMD Các đơn vị (GPU, SIMD Units)
• Nhiều giống hệt nhau tính toán các đơn vị (Many identical compute units)
• Đều đặn dữ liệu các mẫu (Regular data patterns)
• Rộng bộ nhớ các giao diện (Wide memory interfaces)
Các 2000s
Thời gian-thực Phương tiện Việc mã hóa (Real-time Media Coding)
Phương tiện Các codec, Mạng
Các bộ xử lý (Media Codecs, Network Processors)
• Cố định-chức năng các đường ống (Fixed-function pipelines)
• Cao thông lượng việc xử lý (High throughput processing)
• Năng lượng-hiệu suất sự tối ưu hóa (Power-performance optimization)
Các 2010s
Sâu Sự học hỏi Tensor
Các hoạt động (Deep Learning Tensor Operations)
TPU, GPU Tensor Các lõi (TPU, GPU Tensor Cores)
• Ma trận phép nhân các đơn vị (Matrix multiplication units)
• Đồ sộ sự song song (Massive parallelism)
• Bộ nhớ băng thông sự tối ưu hóa (Memory bandwidth optimization)
Các 2020s
Cụ thể-Ứng dụng
Sự gia tốc (Application-Specific Acceleration)
ML Các động cơ, Các Smart NIC,
Miền Các máy gia tốc (ML Engines, Smart NICs, Domain Accelerators)
• Cụ thể-khối lượng công việc các đường dữ liệu (Workload-specific datapaths)
• Được tùy chỉnh bộ nhớ các hệ thống phân cấp (Customized memory hierarchies)
• Được tối ưu hóa-bởi-ứng dụng các thiết kế (Application-optimized designs)
11.2.6 Sự tích hợp nút thắt cổ chai (The integration bottleneck)
Máy học hỏi đại diện một tính toán miền nơi chính hiệu suất giới hạn đã dịch chuyển từ số học tới sự tích hợp (Machine learning represents a computational domain where the primary performance limit has shifted from arithmetic to integration). Trong khi sớm các bộ đồng xử lý đã giải quyết độ chính xác nút thắt cổ chai (8087) và các GPU đã giải quyết thông lượng nút thắt cổ chai (rasterization), hiện đại AI các khối lượng công việc là bị ràng buộc bởi sự tích hợp nút thắt cổ chai: năng lượng và độ trễ chi phí của việc di chuyển đồ sộ các lượng của dữ liệu giữa bộ nhớ và hàng ngàn của song song tính toán các đơn vị (While early coprocessors solved the precision bottleneck (8087) and GPUs solved the throughput bottleneck (rasterization), modern AI workloads are constrained by the integration bottleneck: the energy and latency cost of moving massive amounts of data between memory and thousands of parallel compute units).
Ba độc đáo các thuộc tính của thần kinh các mạng dẫn dắt điều này sự dịch chuyển (Three unique properties of neural networks drive this shift). Của chúng đồ sộ sự song song là đầu tiên: không giống đa-mục đích mã với phức tạp việc phân nhánh, thần kinh các mạng thực thi hàng tỷ của độc lập ma trận các phép nhân và các sự tích chập, và điều này đều đặn cấu trúc cho phép việc thay thế phức tạp CPU kiểm soát logic với dày đặc các mảng của việc xử lý các phần tử (tâm thu các mảng) (Their massive parallelism is the first: unlike general-purpose code with complex branching, neural networks execute billions of independent matrix multiplications and convolutions, and this regular structure allows replacing complex CPU control logic with dense arrays of processing elements (systolic arrays)). Của chúng dữ liệu dòng là cũng có thể dự đoán, về mặt toán học được xác định bởi mạng của các lớp, thứ mà cho phép phần cứng để "tìm nạp trước" dữ liệu vào cục bộ các sổ nháp13 và bỏ qua đắt đỏ ngẫu nhiên-truy cập bộ nhớ đệm các hệ thống phân cấp của các CPU (Their data flow is also predictable, mathematically determined by the network’s layers, which enables hardware to “prefetch” data into local scratchpads13 and bypass the expensive random-access cache hierarchies of CPUs). Cuối cùng, thần kinh các mạng dung thứ được làm giảm bớt độ chính xác, việc giữ nguyên mạnh mẽ khi được chọn các hoạt động sử dụng 8-bit hoặc 4-bit các số nguyên thay vì 32- hoặc 64-bit dấu phẩy-động các số; điều này tính linh hoạt để các kiến trúc sư phù hợp đáng kể nhiều hơn thấp-độ chính xác tính toán vào cùng silicon diện tích và làm giảm bớt bộ nhớ lưu lượng trên mỗi giá trị (Dally et al. 2021; Dally 2023) (Finally, neural networks tolerate reduced precision, remaining robust when selected operations use 8-bit or 4-bit integers instead of 32- or 64-bit floating-point numbers; this flexibility lets architects fit substantially more low-precision compute into the same silicon area and reduce memory traffic per value (Dally et al. 2021; Dally 2023)).
Chính kỹ thuật thách thức là không lâu hơn việc tối đa hóa sự tính toán tỷ lệ mà việc giữ dữ liệu gần tới sự tính toán (The primary engineering challenge is no longer maximizing calculation rate but keeping data close to the calculation). Trong hiện đại các máy gia tốc, việc truy cập dữ liệu từ bên ngoài bộ nhớ (DRAM) có thể tiêu thụ 100× nhiều hơn năng lượng so với thực tế số học hoạt động (In modern accelerators, accessing data from external memory (DRAM) can consume 100× more energy than the actual arithmetic operation). Sự chênh lệch này là chính xác tại sao hiện đại máy gia tốc các kiến trúc ưu tiên cao-băng thông bộ nhớ (HBM)14 và lớn trên-chip các sổ nháp qua việc đơn giản thêm nhiều hơn tính toán các đơn vị (This disparity is precisely why modern accelerator architectures prioritize high-bandwidth memory (HBM)14 and large on-chip scratchpads over simply adding more compute units).
Để thấy cách nào các máy gia tốc giải quyết điều này sự tích hợp nút thắt cổ chai trong thực tế, kiểm tra thuộc về kiến trúc bản thiết kế trong hình 11.5 (To see how accelerators address this integration bottleneck in practice, examine the architectural blueprint in figure 11.5). Chú ý cách nào mọi thiết kế quyết định, từ việc xử lý phần tử lưới tới đa cấp bộ nhớ đệm hệ thống phân cấp, nhắm mục tiêu dữ liệu sự di chuyển sự giảm bớt thay vì thô tính toán phép nhân (Notice how every design decision, from the processing element grid to the multilevel cache hierarchy, targets data movement reduction rather than raw compute multiplication). Sự tiến hóa từ Intel 8087 tới Google TPU tiết lộ một nhất quán mẫu: phần cứng tiến hóa để khớp thuật toán của thống trị nút thắt cổ chai (The evolution from the Intel 8087 to the Google TPU reveals a consistent pattern: hardware evolves to fit the algorithm’s dominant bottleneck). Nơi 8087 đã giải quyết dấu phẩy-động các hoạt động thứ mà đã thống trị nhiều khoa học các khối lượng công việc, hiện đại AI các máy gia tốc giải quyết dày đặc ma trận và tích chập các hoạt động thứ mà thống trị nhiều của thần kinh-mạng sự đào tạo và sự suy luận (Palmer 1980; Goodfellow et al. 2016; Sze et al. 2017; Jouppi et al. 2017) (Where the 8087 addressed floating-point operations that dominated many scientific workloads, modern AI accelerators address dense matrix and convolution operations that dominate much of neural-network training and inference (Palmer 1980; Goodfellow et al. 2016; Sze et al. 2017; Jouppi et al. 2017)). Điều này sự tập trung của nhu cầu giải thích tại sao chuyên biệt AI silicon có thể phân phối lớn hiệu suất-trên-watt các sự cải thiện qua đa-mục đích các bộ xử lý trên khớp các khối lượng công việc (This concentration of demand explains why specialized AI silicon can deliver large performance-per-watt improvements over general-purpose processors on matching workloads).
Cùng ba các thuộc tính này, đồ sộ sự song song, có thể dự đoán dữ liệu dòng, và sự dung sai cho được làm giảm bớt độ chính xác, định hình mọi máy gia tốc kiến trúc quyết định (These same three properties, massive parallelism, predictable data flow, and tolerance for reduced precision, shape every accelerator architecture decision). Trước khi việc kiểm tra tính toán các nguyên thủy thứ mà khai thác chúng, chúng ta kiểm tra thuộc về kiến trúc tổ chức thứ mà cho phép của chúng hiệu quả sự thực thi (Before examining the computational primitives that exploit them, we examine the architectural organization that enables their efficient execution). Hiện đại AI các máy gia tốc đạt được của chúng ngoạn mục hiệu suất các sự cải thiện thông qua một một cách cẩn thận được dàn dựng hệ thống phân cấp của chuyên biệt các thành phần hoạt động trong sự hòa hợp (Modern AI accelerators achieve their dramatic performance improvements through a carefully orchestrated hierarchy of specialized components operating in concert).

================ PAGE 600 ================

562
11.2 Phần cứng Sự chuyên biệt hóa (Hardware Specialization)
L2 Bộ nhớ đệm (Được chia sẻ) (L2 Cache (Shared))
PE (PE)
PE (PE)
PE (PE)
PE (PE)
• • •
PE (PE)
PE (PE)
PE (PE)
PE (PE)
• • •
L1 Bộ nhớ đệm / Sổ nháp (L1 Cache / Scratchpad)
Tensor Lõi (Tensor Core)
Vector Đơn vị (Vector Unit)
SFU (SFU)
Việc xử lý Phần tử (Processing Element)
AI Máy gia tốc Chip (AI Accelerator Chip)
CPU (CPU)
Máy chủ CPU (Host CPU)
Máy chủ DRAM (Host DRAM)
Máy chủ Giao diện
(PCIe/NVLink) (Host Interface (PCIe/NVLink))
Cao-Băng thông
Bộ nhớ (HBM) (High-Bandwidth Memory (HBM))
Bộ nhớ
Giao diện (Memory Interface)
Hình 11.5: Giải phẫu của một Hiện đại AI Máy gia tốc: AI các máy gia tốc tích hợp chuyên biệt việc xử lý các phần tử việc chứa tensor các lõi, vector các đơn vị, và đặc biệt chức năng các đơn vị, được hỗ trợ bởi một phân cấp bộ nhớ hệ thống từ cao-băng thông bộ nhớ xuống tới cục bộ các bộ nhớ đệm (Figure 11.5: Anatomy of a Modern AI Accelerator: AI accelerators integrate specialized processing elements containing tensor cores, vector units, and special function units, supported by a hierarchical memory system from high-bandwidth memory down to local caches). Điều này kiến trúc tối đa hóa dữ liệu sự tái sử dụng và song song sự thực thi trong khi việc tối thiểu hóa thâm dụng-năng lượng dữ liệu sự di chuyển, thứ mà là nền tảng cho lớn hiệu suất-trên-watt các sự cải thiện qua đa-mục đích các bộ xử lý (This architecture maximizes data reuse and parallel execution while minimizing energy-intensive data movement, which is the foundation for large performance-per-watt improvements over general-purpose processors).
Việc xử lý chất nền bao gồm của một mảng của việc xử lý các phần tử (có thể nhìn thấy như "PE" lưới trong hình 11.5), mỗi cái chứa được cống hiến tính toán các đơn vị được tối ưu hóa cho cụ thể các hoạt động: tensor các lõi thực thi ma trận phép nhân, vector các đơn vị thực hiện theo-phần tử các hoạt động, và đặc biệt chức năng các đơn vị tính toán sự kích hoạt các hàm (The processing substrate consists of an array of processing elements (visible as the “PE” grid in figure 11.5), each containing dedicated computational units optimized for specific operations: tensor cores execute matrix multiplication, vector units perform element-wise operations, and special function units compute activation functions). Những việc xử lý các phần tử này là được tổ chức trong một lưới cấu trúc liên kết thứ mà cho phép đồ sộ sự song song, với hàng chục tới hàng trăm của các đơn vị hoạt động một cách đồng thời trên khác nhau các phần của sự tính toán, việc khai thác cấp-dữ liệu sự song song vốn có trong thần kinh mạng các khối lượng công việc (These processing elements are organized in a grid topology that enables massive parallelism, with dozens to hundreds of units operating simultaneously on different portions of the computation, exploiting the data-level parallelism inherent in neural network workloads).
Bộ nhớ hệ thống phân cấp tạo thành một bằng nhau quan trọng thuộc về kiến trúc thành phần (The memory hierarchy forms an equally critical architectural component). Cao-băng thông bộ nhớ cung cấp tổng thông lượng được yêu cầu để duy trì những nhiều việc xử lý các phần tử này, trong khi một đa cấp bộ nhớ đệm hệ thống phân cấp từ được chia sẻ L2 các bộ nhớ đệm xuống tới trên-phần tử L1 các bộ nhớ đệm và các sổ nháp tối thiểu hóa năng lượng chi phí của dữ liệu sự di chuyển (High-bandwidth memory provides the aggregate throughput required to sustain these numerous processing elements, while a multilevel cache hierarchy from shared L2 caches down to per-element L1 caches and scratchpads minimizes the energy cost of data movement). Điều này phân cấp tổ chức hiện thân một cốt lõi thiết kế nguyên lý: trong AI các máy gia tốc, dữ liệu sự di chuyển điển hình tiêu thụ nhiều hơn năng lượng so với sự tính toán bản thân nó, việc đòi hỏi thuộc về kiến trúc các chiến lược thứ mà ưu tiên dữ liệu sự tái sử dụng bằng cách việc duy trì một cách thường xuyên được truy cập các giá trị (bao gồm các trọng số và một phần các kết quả) trong sự gần gũi tới tính toán các đơn vị (This hierarchical organization embodies a core design principle: in AI accelerators, data movement typically consumes more energy than computation itself, necessitating architectural strategies that prioritize data reuse by maintaining frequently accessed values (including weights and partial results) in proximity to compute units). Máy các nền tảng phụ lục thu thập tham chiếu các thông số kỹ thuật cho hiện đại các máy gia tốc (H100, TPU v5) và tóm tắt độ trễ các hình phạt qua mỗi bộ nhớ cấp (The machine foundations appendix collects reference specifications for modern accelerators (H100, TPU v5) and summarizes the latency penalties across each memory level).
Máy chủ giao diện thiết lập tính kết nối giữa chuyên biệt máy gia tốc và rộng hơn việc điện toán hệ thống, việc cho phép sự phối hợp giữa đa-mục đích các CPU thứ mà quản lý chương trình kiểm soát dòng và máy gia tốc thứ mà thực thi một cách thâm dụng tính toán thần kinh mạng các hoạt động (The host interface establishes connectivity between the specialized accelerator and the broader computing system, enabling coordination between general-purpose CPUs that manage program control flow and the accelerator that executes computationally intensive neural network operations). Điều này thuộc về kiến trúc sự phân vùng phản ánh sự chuyên biệt hóa ở cấp hệ thống: các CPU giải quyết kiểm soát dòng, có điều kiện logic, và hệ thống sự phối hợp, trong khi các máy gia tốc tập trung trên đều đặn, đồ sộ song song số học các hoạt động thứ mà thống trị thần kinh mạng sự thực thi (This architectural partitioning reflects specialization at the system level: CPUs address control flow, conditional logic, and system coordination, while accelerators focus on the regular, massively parallel arithmetic operations that dominate neural network execution). Dữ liệu đường dẫn trong hình 11.5 chạy từ máy chủ giao diện thông qua bộ nhớ hệ thống phân cấp và vào việc xử lý phần tử lưới; đó đầu-tới-đầu sự tích hợp là cái gì làm hệ thống được tối ưu hóa cho AI các khối lượng công việc thay vì đa-mục đích sự tính toán (The data path in figure 11.5 runs from the host interface through the memory hierarchy and into the processing element grid; that end-to-end integration is what makes the system optimized for AI workloads rather than general computation).
Với máy gia tốc của vật lý kiến trúc được thiết lập, tiếp theo bước là để giải thích tại sao những cụ thể các thành phần này thống trị (With the accelerator’s physical architecture established, the next step is to explain why these specific components dominate). Tensor các lõi, vector các đơn vị, và phân cấp bộ nhớ không tồn tại bởi tai nạn; chúng tồn tại bởi vì thần kinh mạng các sự tính toán một cách lặp lại gọi một nhỏ tập hợp của các hoạt động (Tensor cores, vector units, and hierarchical memory do not exist by accident; they exist because neural network computations repeatedly invoke a small set of operations). Việc hiểu những các mẫu này là thiết yếu bởi vì chúng giải thích cái nào thuật toán các thay đổi dịch tới thực tế các phần tăng tốc (những thứ đó mà căn chỉnh với phần cứng các nguyên thủy) và cái nào giữ nguyên thuần túy lý thuyết (Understanding these patterns is essential because they explain which algorithmic changes translate to real speedups (those that align with hardware primitives) and which remain purely theoretical).

11. Phần cứng Sự gia tốc (Hardware Acceleration)
563
11.3 AI Tính toán Các nguyên thủy (AI Compute Primitives)
Bất kể của lớp loại (được kết nối đầy đủ, tích chập, hoặc dựa trên-sự chú ý), thống trị hoạt động trong thần kinh các mạng là việc nhân đầu vào các giá trị bởi được học các trọng số và việc tích lũy các kết quả (Regardless of the layer type (fully connected, convolutional, or attention-based), the dominant operation in neural networks is multiplying input values by learned weights and accumulating the results). Này nhân-tích lũy (MAC) mẫu thường thống trị sự thực thi thời gian và có thể xuất hiện hàng tỷ của các lần trên mỗi sự suy luận lượt (This multiply-accumulate (MAC) pattern often dominates execution time and can appear billions of times per inference pass). Của nó tính đều đặn là cái gì làm phần cứng sự chuyên biệt hóa khả thi: không giống đa-mục đích mã với không thể dự đoán các nhánh và không đều bộ nhớ truy cập, các MAC theo sau cố định dữ liệu-dòng các mẫu với có thể dự đoán sự tái sử dụng, việc cho phép các kiến trúc thứ mà đánh đổi đi tính tổng quát cho thô thông lượng (Its regularity is what makes hardware specialization possible: unlike general-purpose code with unpredictable branches and irregular memory access, MACs follow fixed data-flow patterns with predictable reuse, enabling architectures that trade away generality for raw throughput). Sự chuyển đổi từ các CPU việc đạt được xấp xỉ 100 GFLOP/s tới các máy gia tốc việc phân phối 100,000+ GFLOP/s phản ánh điều này thuộc về kiến trúc vụ cá cược: việc loại bỏ tính linh hoạt để tối ưu hóa cho cụ thể các hoạt động thứ mà thần kinh các mạng thực sự thực hiện (The transition from CPUs achieving approximately 100 GFLOP/s to accelerators delivering 100,000+ GFLOP/s reflects this architectural bet: eliminating flexibility to optimize for the specific operations that neural networks actually perform).
Chúng ta gọi phần cứng các đơn vị thứ mà khai thác những các mẫu này AI tính toán các nguyên thủy: chuyên biệt chức năng các khối, mỗi cái được tối ưu hóa cho một cụ thể lớp của hoạt động (We call the hardware units that exploit these patterns AI compute primitives: specialized functional blocks, each optimized for a particular class of operation). Ba các nguyên thủy là đặc biệt phổ biến trong các máy gia tốc, mỗi cái nhắm mục tiêu một khác biệt tính toán mẫu được tìm thấy trong thần kinh các mạng (Three primitives are especially common in accelerators, each targeting a distinct computational pattern found in neural networks).
Danh sách 11.1 chứng minh cách nào một dày đặc lớp phân rã ở cấp khuôn khổ, việc đóng gói hàng ngàn của nhân-tích lũy các hoạt động trong một đơn cao-cấp lệnh gọi (Listing 11.1 demonstrates how a dense layer decomposes at the framework level, encapsulating thousands of multiply-accumulate operations in a single high-level call).
Danh sách 11.1: Dày đặc Lớp Sự trừu tượng: Cao-cấp khuôn khổ các API đóng gói 131,072 các MAC (256 các đầu vào nhân 512 các đầu ra) trong một đơn hàm lệnh gọi, việc ẩn đi tính toán tính phức tạp khỏi các nhà phát triển trong khi việc cho phép tự động phần cứng sự tối ưu hóa (Listing 11.1: Dense Layer Abstraction: High-level framework APIs encapsulate 131,072 MACs (256 inputs times 512 outputs) in a single function call, hiding the computational complexity from developers while enabling automatic hardware optimization).
# Khuôn khổ trừu tượng hóa thâm dụng-tính toán các hoạt động (Framework abstracts compute-intensive operations)
dense = Dense(512)(input_tensor)
# $256{\times}512$ các MAC trên mẫu ($256{\times}512$ MACs per sample)
Này đơn dòng của mã che giấu tính toán tính phức tạp thứ mà các máy gia tốc phải xử lý (This single line of code conceals the computational complexity that accelerators must handle).
Danh sách 11.2 tiết lộ cách nào khuôn khổ mở rộng này cao-cấp lệnh gọi thành toán học các hoạt động (Listing 11.2 reveals how the framework expands this high-level call into mathematical operations).
Danh sách 11.2: Ma trận Hoạt động Sự mở rộng: Mỗi dày đặc lớp phân rã thành ma trận phép nhân và theo-phần tử các hoạt động, việc phơi bày thống trị tính toán mẫu thứ mà nhiều thần kinh-mạng các hạt nhân được xây dựng xung quanh (Listing 11.2: Matrix Operation Expansion: Each dense layer decomposes into matrix multiplication and element-wise operations, exposing the dominant compute pattern that many neural-network kernels are built around).
# Tuyến tính sự biến đổi công việc chia tỷ lệ với đầu_vào_chiều x đầu_ra_chiều x lô (Linear transformation work scales with input_dim x output_dim x batch)
output = (
matmul(input, weights) + bias
)
# Ma trận nhân thống trị chi phí (Matrix multiply dominates cost)
output = activation(
output
)
# Theo-phần tử: tỷ lệ thuận với đầu_ra_chiều x lô (Element-wise: proportional to output_dim x batch)
Ma trận phép nhân thống trị sự tính toán thời gian, nhưng điều này sự trừu tượng vẫn ẩn đi nằm bên dưới vòng lặp cấu trúc (The matrix multiplication dominates computation time, but this abstraction still hides the underlying loop structure). Ở cấp bộ xử lý, danh sách 11.3 tiết lộ cách nào lồng nhau các vòng lặp nhân các đầu vào và các trọng số, tính tổng các kết quả, và áp dụng một phi tuyến tính hàm, việc phơi bày 𝒪(𝐵×𝑑in ×𝑑out) tính phức tạp thứ mà các máy gia tốc phải xử lý một cách hiệu quả (At the processor level, listing 11.3 reveals how nested loops multiply inputs and weights, sum the results, and apply a nonlinear function, exposing the 𝒪(𝐵×𝑑in ×𝑑out) complexity that accelerators must handle efficiently).
Danh sách 11.3: Cấp-Bộ xử lý Sự thực thi: Lồng nhau các vòng lặp tiết lộ 𝒪(𝐵× 𝑑in × 𝑑out) nhân-tích lũy các hoạt động thứ mà các máy gia tốc phải thực thi, với 4.2M các MAC cho 𝐵=32, 𝑑in=256, 𝑑out=512 các cấu hình (Listing 11.3: Processor-Level Execution: Nested loops reveal the 𝒪(𝐵× 𝑑in × 𝑑out) multiply-accumulate operations that accelerators must execute, with 4.2M MACs for 𝐵=32, 𝑑in=256, 𝑑out=512 configurations).
# Tổng các hoạt động: lô_kích_thước × đầu_ra_kích_thước × đầu_vào_kích_thước các MAC (Total operations: batch_size × output_size × input_size MACs)
for n in range(batch_size):
# Lô chiều: có thể song song hóa (Batch dimension: parallelizable)
for m in range(output_size):
# Đầu ra các nơ-ron: có thể song song hóa (Output neurons: parallelizable)
sum = bias[m]
# Khởi tạo bộ tích lũy (Initialize accumulator)
for k in range(input_size):
# Sự giảm bớt chiều: tuần tự (Reduction dimension: sequential)
sum += input[n, k] * weights[k, m]
# MAC hoạt động (MAC operation)
output[n, m] = activation(sum)
# Phi tuyến tính sự biến đổi (Nonlinear transformation)
# Ví dụ công việc chia tỷ lệ như lô_kích_thước × đầu_ra_kích_thước ×
# đầu_vào_kích_thước nhân-tích lũy các hoạt động (Example work scales as batch_size × output_size × input_size multiply-accumulate operations)
Điều này vòng lặp cấu trúc tiết lộ ba khác biệt tính toán các mẫu thứ mà lặp lại qua tất cả thần kinh mạng các kiến trúc: theo-phần tử các hoạt động dọc theo các vector (sự kích hoạt hàm được áp dụng tới (This loop structure reveals three distinct computational patterns that recur across all neural network architectures: element-wise operations along vectors (the activation function applied to

================ PAGE 602 ================

564
11.3 AI Tính toán Các nguyên thủy (AI Compute Primitives)
15
RISC-V (Được làm giảm bớt Lệnh
Tập hợp Máy tính V (Reduced Instruction Set Computer V)):
Mở ISA cho phép phần cứng
các đội thêm tùy chỉnh
ML các lệnh—vector chấm-
tích, sự kích hoạt các hàm,
thưa thớt tensor các hoạt động—mà không có
cấp phép các khoản phí hoặc các NDA được
yêu cầu bởi ARM hoặc x86 (The open ISA allows hardware teams to add custom ML instructions—vector dot-product, activation functions, sparse tensor ops—without the licensing fees or NDAs required by ARM or x86). Sự ràng buộc
điều này loại bỏ là
5–10 năm chờ đợi cho độc quyền
các nhà cung cấp thêm ML-
cụ thể các phần mở rộng tới của họ
các lộ trình (The constraint this removes is the 5–10 year wait for proprietary vendors to add ML-specific extensions to their roadmaps).
Sự đánh đổi là
phần mềm hệ sinh thái sự trưởng thành:
RISC-V ML các máy gia tốc thiếu
cuDNN/TensorRT tương đương
những thứ đó mà làm GPU việc lập trình
thực tế, việc giới hạn
sự áp dụng tới rìa và được nhúng
sự suy luận nơi phần mềm
ngăn xếp là đủ hẹp
để xây dựng từ đầu (The trade-off is software ecosystem maturity: RISC-V ML accelerators lack the cuDNN/TensorRT equivalents that make GPU programming practical, limiting adoption to edge and embedded inference where the software stack is narrow enough to build from scratch).
mỗi đầu ra), cấp-ma trận các sự giảm bớt (được đánh trọng số tổng qua tất cả đầu vào các đặc trưng), và phi tuyến tính các sự biến đổi (sự kích hoạt hàm bản thân nó) (each output), matrix-level reductions (the weighted sum across all input features), and nonlinear transformations (the activation function itself)). Mỗi mẫu là đủ thường xuyên để biện minh được cống hiến silicon, cung cấp các bậc-của-độ lớn phần tăng tốc khi được chuyên biệt hóa, và đã giữ nguyên ổn định qua nhiều thập kỷ của thần kinh mạng sự tiến hóa, từ sớm các perceptron thông qua các transformer (Each pattern is frequent enough to justify dedicated silicon, offers orders-of-magnitude speedup when specialized, and has remained stable across decades of neural network evolution, from early perceptrons through transformers). Những các mẫu này trở thành phần cứng các khối: vector các đơn vị cho độc lập các phần tử, ma trận các động cơ cho các sự giảm bớt, và đặc biệt-chức năng các đơn vị cho phi tuyến tính toán học (These patterns become hardware blocks: vector units for independent elements, matrix engines for reductions, and special-function units for nonlinear math).
11.3.1 Vector các hoạt động (Vector operations)
Vector các hoạt động cung cấp đầu tiên cấp của phần cứng sự gia tốc bằng cách việc xử lý nhiều dữ liệu các phần tử một cách đồng thời (Vector operations provide the first level of hardware acceleration by processing multiple data elements simultaneously). Gợi nhớ lại lồng nhau-vòng lặp cấu trúc được phơi bày trong danh sách 11.3: một lô của 32 các mẫu thông qua một 256-tới-512 dày đặc lớp yêu cầu 4.2M các MAC nhân-tích lũy các hoạt động (Recall the nested-loop structure exposed in listing 11.3: a batch of 32 samples through a 256-to-512 dense layer requires 4.2M MACs multiply-accumulate operations). Một truyền thống vô hướng bộ xử lý thực thi những cái này từng cái một ở một thời điểm, việc tải một đầu vào giá trị và một trọng số giá trị, việc nhân chúng, và việc tích lũy kết quả (A traditional scalar processor executes these one at a time, loading an input value and a weight value, multiplying them, and accumulating the result). Điều này tuần tự cách tiếp cận là một cách vô vọng không hiệu quả cho thần kinh các mạng thứ mà lặp lại điều này mẫu qua hàng triệu của các tham số (This sequential approach is hopelessly inefficient for neural networks that repeat this pattern across millions of parameters).
Vector việc xử lý các đơn vị giải quyết điều này bằng cách việc hoạt động trên nhiều dữ liệu các phần tử một cách đồng thời (Vector processing units solve this by operating on multiple data elements simultaneously). RISC-
V15, thứ năm thế hệ của được làm giảm bớt lệnh tập hợp máy tính (RISC) kiến trúc (Waterman et al. 2013), cung cấp một hữu ích bối cảnh cho việc minh họa điều này ý tưởng (RISC-V15, the fifth generation of the reduced instruction set computer (RISC) architecture (Waterman et al. 2013), provides a useful setting for illustrating this idea). Danh sách 11.4 sử dụng kiểu-vector hợp ngữ mã trong đó một đơn lệnh xử lý một vector của dữ liệu các phần tử một cách song song (Listing 11.4 uses vector-style assembly code in which a single instruction processes a vector of data elements in parallel). Vòng lặp có năm có thể nhìn thấy-bởi-phần cứng các giai đoạn (The loop has five hardware-visible stages):
1. Vector chiều dài cấu hình: Cấu hình vector các đơn vị để xử lý 32-bit các phần tử, một cách tự động việc xác định bao nhiêu các hoạt động xảy ra một cách song song dựa trên phần cứng chiều rộng (VLEN) (Vector length configuration: Configures the vector units to process 32-bit elements, automatically determining how many operations happen in parallel based on hardware width (VLEN)).
2. Vector sự khởi tạo: Xóa bộ tích lũy vector v0 (việc chứa, cho ví dụ, tám song song các tổng) việc sử dụng một độc quyền-HOẶC hoạt động, thứ mà là hiệu quả hơn so với một tải ngay lập tức (Vector initialization: Clears the accumulator vector v0 (containing, for example, eight parallel sums) using an exclusive-OR operation, which is more efficient than a load immediate).
3. Vector các lệnh tải: Tải liên tục 32-bit đầu vào và trọng số các giá trị từ bộ nhớ vào vector các thanh ghi v1 và v2 trong một đơn lệnh, việc tối đa hóa bộ nhớ băng thông sự sử dụng (Vector loads: Loads continuous 32-bit input and weight values from memory into vector registers v1 and v2 in a single instruction, maximizing memory bandwidth utilization).
4. Được hợp nhất Nhân-Tích lũy: Thực hiện song song nhân-cộng các hoạt động (𝑣0 = 𝑣0 +𝑣1 ×𝑣2) (Fused Multiply-Accumulate: Performs parallel multiply-add operations (𝑣0 = 𝑣0 +𝑣1 ×𝑣2)). Này là cốt lõi tính toán nguyên thủy, việc nhân đôi thông lượng được so sánh tới tách biệt nhân và cộng các lệnh (This is the core computational primitive, doubling throughput compared to separate multiply and add instructions).
5. Con trỏ số học: Cập nhật bộ nhớ các con trỏ bởi vector byte chiều dài để chuẩn bị cho tiếp theo dữ liệu đoạn (Pointer arithmetic: Updates memory pointers by the vector byte length to prepare for the next data chunk).
Danh sách 11.4: Được vector hóa Nhân-Tích lũy Vòng lặp: Này mang tính minh họa vòng lặp hiển thị cách nào kiểu-vector các lệnh cho phép hiệu quả lô việc xử lý bằng cách việc thực hiện nhiều nhân-cộng các hoạt động một cách đồng thời, việc làm giảm bớt tính toán độ trễ trong thần kinh mạng các hạt nhân (Listing 11.4: Vectorized Multiply-Accumulate Loop: This illustrative loop shows how vector-style instructions enable efficient batch processing by performing multiple multiply-add operations simultaneously, reducing computational latency in neural network kernels).
vsetvli t0, a0, e32
loop_batch:
loop_neuron:
vxor.vv v0, v0, v0
loop_feature:
vle32.v v1, (in_ptr)
vle32.v v2, (wt_ptr)
vfmacc.vv v0, v1, v2
add in_ptr, in_ptr, 32
add wt_ptr, wt_ptr, 32
bnez feature_cnt, loop_feature
Chính sự thấu hiểu từ này hợp ngữ chuỗi là rằng được hợp nhất nhân-tích lũy lệnh (vfmacc.vv) thực hiện cùng hoạt động thứ mà sẽ yêu cầu tách biệt nhân và cộng các lệnh trên một vô hướng bộ xử lý, trong khi vector lệnh tải các lệnh (vle32.v) khấu hao bộ nhớ truy cập chi phí chung qua nhiều dữ liệu các phần tử (The key insight from this assembly sequence is that the fused multiply-accumulate instruction (vfmacc.vv) performs the same operation that would require separate multiply and add instructions on a scalar processor, while the vector load instructions (vle32.v) amortize memory access overhead across multiple data elements). Điều này vector sự triển khai xử lý tám dữ liệu các phần tử một cách song song, việc làm giảm bớt cả hai sự tính toán thời gian và năng lượng sự tiêu thụ (This vector implementation processes eight data elements in parallel, reducing both computation time and energy consumption). Vector lệnh tải các lệnh truyền tải tám các giá trị một cách đồng thời, việc tối đa hóa bộ nhớ băng thông sự sử dụng (Vector load instructions transfer eight values simultaneously, maximizing memory bandwidth utilization). Vector nhân-tích lũy lệnh xử lý tám các cặp của các giá trị một cách song song, một cách đáng kể việc làm giảm bớt tổng lệnh số đếm từ 4.2M các MAC vô hướng các hoạt động tới xấp xỉ 524,288 vector các đoạn (The vector multiply-accumulate instruction processes eight pairs of values in parallel, dramatically reducing the total instruction count from 4.2M MACs scalar operations to roughly 524,288 vector chunks).

================ PAGE 603 ================

11. Phần cứng Sự gia tốc (Hardware Acceleration)
565
16
Cray-1 Vector Di sản (Cray-1 Vector Legacy):
Cray-1 (1975) đã đạt được
160
MFLOP/s—1,000×
nhanh hơn
so với
đương thời
các máy tính—bằng cách
việc xử lý
64 các phần tử một cách đồng thời
thông qua
được tạo đường ống
vector
các đơn vị, ở một chi phí của $8.8 triệu
($40–45
triệu
trong
2024
các đô la) (The Cray-1 (1975) achieved 160 MFLOP/s—1,000× faster than contemporary computers—by processing 64 elements simultaneously through pipelined vector units, at a cost of $8.8 million ($40–45 million in 2024 dollars)).
Của nó thuộc về kiến trúc
bản mẫu (rộng vector các thanh
ghi,
được tạo đường ống sự thực thi,
việc truyền phát
dữ liệu
thông qua
số học các đơn vị) là chính xác
thiết kế thứ mà hiện đại AI
các máy gia tốc chia tỷ lệ tới hàng ngàn
của các phần tử: một H100 của
tensor các lõi là thuộc về khái niệm
các hậu duệ của Cray của vector
các đơn vị, việc hoạt động trên ma trận
các ô gạch thay vì các vector (Its architectural template (wide vector registers, pipelined execution, streaming data through arithmetic units) is precisely the design that modern AI accelerators scale to thousands of elements: an H100’s tensor cores are conceptual descendants of Cray’s vector units, operating on matrix tiles rather than vectors).
Chính vector các hoạt động ánh xạ một cách trực tiếp tới phổ biến sâu sự học hỏi các mẫu (Key vector operations map directly to common deep learning patterns). Bảng 11.2 liệt kê cách nào các hoạt động chẳng hạn như sự giảm bớt, tập hợp, phân tán, và được che giấu các hoạt động xuất hiện một cách thường xuyên trong việc gộp, nhúng các tra cứu, và sự chú ý các cơ chế, việc làm rõ trực tiếp ánh xạ giữa thấp-cấp vector phần cứng và cao-cấp máy học hỏi các khối lượng công việc (Table 11.2 enumerates how operations such as reduction, gather, scatter, and masked operations appear frequently in pooling, embedding lookups, and attention mechanisms, clarifying the direct mapping between low-level vector hardware and high-level machine learning workloads).
Bảng 11.2: Vector Các hoạt động: Cốt lõi vector các hoạt động ánh xạ một cách trực tiếp tới sâu sự học hỏi các nguyên thủy: các sự giảm bớt thực triển việc gộp các lớp, các lệnh tập hợp cho phép nhúng các tra cứu, các lệnh phân tán cập nhật nhúng các gradient, và được che giấu các hoạt động xử lý sự chú ý các mặt nạ (Table 11.2: Vector Operations: Core vector operations map directly to deep learning primitives: reductions implement pooling layers, gathers enable embedding lookups, scatters update embedding gradients, and masked operations handle attention masks). Mỗi hoạt động khai thác cấp-dữ liệu sự song song để xử lý nhiều các phần tử một cách đồng thời, việc giải thích tại sao vector các đơn vị là phổ quát qua tất cả máy gia tốc các thiết kế (Each operation exploits data-level parallelism to process multiple elements simultaneously, explaining why vector units are universal across all accelerator designs).
Vector Hoạt động (Vector Operation)
Sự mô tả (Description)
Thần kinh Mạng Ứng dụng (Neural Network Application)
Sự giảm bớt (Reduction)
Kết hợp các phần tử qua một vector (cho ví dụ, tổng, lớn nhất) (Combines elements across a vector (for example, sum, max))
Việc gộp các lớp, sự chú ý điểm số sự tính toán (Pooling layers, attention score computation)
Tập hợp (Gather)
Tải nhiều không liên tiếp bộ nhớ các phần tử (Loads multiple nonconsecutive memory elements)
Nhúng các tra cứu, thưa thớt các hoạt động (Embedding lookups, sparse operations)
Phân tán (Scatter)
Ghi tới nhiều không liên tiếp bộ nhớ các vị trí (Writes to multiple nonconsecutive memory locations)
Gradient các cập nhật cho các lệnh nhúng (Gradient updates for embeddings)
Được che giấu các hoạt động (Masked operations)
Một cách có chọn lọc hoạt động trên vector các phần tử (Selectively operates on vector elements)
Sự chú ý các mặt nạ, khoảng đệm việc xử lý (Attention masks, padding handling)
Vector-vô hướng sự phát sóng (Vector-scalar broadcast)
Áp dụng vô hướng tới tất cả vector các phần tử (Applies scalar to all vector elements)
Độ lệch sự bổ sung, việc chia tỷ lệ các hoạt động (Bias addition, scaling operations)
Những tính hiệu quả các lợi ích này mở rộng vượt ra ngoài lệnh số đếm sự giảm bớt (These efficiency gains extend beyond instruction count reduction). Bộ nhớ băng thông sự sử dụng cải thiện như vector các lệnh tải truyền tải nhiều các giá trị trên mỗi hoạt động, và năng lượng tính hiệu quả tăng bởi vì kiểm soát logic là được khấu hao qua nhiều dữ liệu các phần tử (Memory bandwidth utilization improves as vector loads transfer multiple values per operation, and energy efficiency increases because control logic is amortized across many data elements). Những các sự cải thiện này hợp chất qua sâu các lớp của hiện đại thần kinh các mạng, nơi hàng tỷ của theo-phần tử các hoạt động thực thi trên mỗi tiến lượt (These improvements compound across the deep layers of modern neural networks, where billions of element-wise operations execute per forward pass). Thuộc về kiến trúc mẫu là không mới (The architectural pattern is not new). Cray-116 đã tiên phong cùng cách tiếp cận cho khoa học việc điện toán trong 1975 (Jordan 1982), nhưng thần kinh các mạng đã đưa nó chưa từng có thương mại tầm quan trọng (The Cray-116 pioneered the same approach for scientific computing in 1975 (Jordan 1982), but neural networks have given it unprecedented commercial importance).
Vector các hoạt động xuất sắc ở theo-phần tử các sự biến đổi giống như sự kích hoạt các hàm, nơi mỗi đầu ra phụ thuộc chỉ trên của nó tương ứng đầu vào (Vector operations excel at element-wise transformations like activation functions, where each output depends only on its corresponding input). Thần kinh các mạng, tuy nhiên, cũng yêu cầu được cấu trúc các sự tính toán nơi mỗi đầu ra phụ thuộc trên tất cả các đầu vào—được đánh trọng số các tổng thứ mà định nghĩa lớp các sự biến đổi (Neural networks, however, also require structured computations where each output depends on all inputs—the weighted sums that define layer transformations). Những nhiều-tới-nhiều các hoạt động này một cách tự nhiên biểu diễn chính chúng như ma trận các phép nhân, của chúng ta thứ hai tính toán nguyên thủy (These many-to-many operations naturally express themselves as matrix multiplications, our second compute primitive).
11.3.2 Ma trận các hoạt động (Matrix operations)
Ma trận phép nhân thống trị thần kinh mạng sự tính toán, việc biến đổi cao-chiều dữ liệu thông qua được cấu trúc các mẫu của các trọng số, các sự kích hoạt, và các gradient (Goodfellow et al. 2016) (Matrix multiplication dominates neural network computation, transforming high-dimensional data through structured patterns of weights, activations, and gradients (Goodfellow et al. 2016)). Trong khi vector các hoạt động xử lý các phần tử một cách độc lập, ma trận các hoạt động dàn dựng các sự tính toán qua nhiều các chiều một cách đồng thời (While vector operations process elements independently, matrix operations orchestrate computations across multiple dimensions simultaneously). Những các hoạt động này tiết lộ các mẫu thứ mà dẫn dắt phần cứng sự gia tốc các chiến lược (These operations reveal patterns that drive hardware acceleration strategies).
11.3.2.1 Ma trận các hoạt động trong thần kinh các mạng (Matrix operations in neural networks)
Thần kinh mạng các sự tính toán phân rã thành phân cấp ma trận các hoạt động (Neural network computations decompose into hierarchical matrix operations). Danh sách 11.5 nắm bắt này hệ thống phân cấp thông qua một tuyến tính lớp thứ mà biến đổi đầu vào các đặc trưng thành đầu ra các nơ-ron qua một lô (Listing 11.5 captures this hierarchy through a linear layer that transforms input features into output neurons over a batch).
Danh sách 11.5: Ma trận Các hoạt động: Thần kinh các mạng thực hiện các sự biến đổi việc sử dụng ma trận các phép nhân và các độ lệch để đạt được đầu ra các dự đoán (Listing 11.5: Matrix Operations: Neural networks perform transformations using matrix multiplications and biases to achieve output predictions). Sự đào tạo yêu cầu cẩn thận sự quản lý của đầu vào các lô và sự kích hoạt các hàm để tối ưu hóa mô hình hiệu suất (Training requires careful management of input batches and activation functions to optimize model performance).
layer = nn.Linear(256, 512)
# Lớp biến đổi 256 các đầu vào tới (Layer transforms 256 inputs to)
# 512 các đầu ra (512 outputs)
output = layer(input_batch)
# Xử lý một lô của 32 các mẫu (Process a batch of 32 samples)
# Khuôn khổ Nội bộ: Cốt lõi các hoạt động (cột-lô quy ước) (Framework Internal: Core operations (column-batch convention))
Z = matmul(weights, input)
# Ma trận: biến đổi [256×32] (Matrix: transforms [256×32])
# đầu vào tới [512×32] đầu ra (input to [512×32] output)
Z = Z + bias
# Vector: thêm độ lệch tới mỗi (Vector: adds bias to each)
# đầu ra một cách độc lập (output independently)
output = relu(Z)
# Vector: áp dụng sự kích hoạt tới (Vector: applies activation to)
# mỗi phần tử một cách độc lập (each element independently)

================ PAGE 604 ================

566
11.3 AI Tính toán Các nguyên thủy (AI Compute Primitives)
17
Im2col
(Hình ảnh-tới-
Cột (Image-to-Column)):
Biến đổi
sự tích chập thành một ma trận
phép nhân bằng cách một cách rõ ràng
việc sao chép chồng chéo đầu-
vào các vùng thành các cột
của
một
mới,
lớn hơn
ma trận (Transforms convolution into a matrix multiplication by explicitly duplicating overlapping input regions into the columns of a new, larger matrix).
Này
bộ nhớ-cho-tính toán
sự đánh đổi là chính xác cái gì
cho phép sự thực thi trên được tối ưu hóa-cho-ma trận
phần cứng, như
ngữ cảnh câu phát biểu (This memory-for-compute trade-off is precisely what enables execution on matrix-optimized hardware, as the context sentence states).
Chi phí là đáng kể bộ nhớ
sự khuếch đại;
một
tiêu chuẩn
3×3
hạt nhân
tăng
đầu vào của
bộ nhớ
dấu chân
bởi 9× để tạo ra được yêu cầu
dày đặc ma trận cấu trúc (The cost is significant memory amplification; a standard 3×3 kernel increases the input’s memory footprint by 9× to create the required dense matrix structure).
Điều này sự tính toán chứng minh quy mô của ma trận các hoạt động trong thần kinh các mạng (This computation demonstrates the scale of matrix operations in neural networks). Mỗi đầu ra nơ-ron (512 tổng) phải xử lý tất cả đầu vào các đặc trưng (256 tổng) cho mọi mẫu trong lô (32 các mẫu) (Each output neuron (512 total) must process all input features (256 total) for every sample in the batch (32 samples)). Trọng số ma trận một mình nó chứa 256 × 512 = 131,072 các tham số thứ mà định nghĩa những các sự biến đổi này, việc minh họa tại sao hiệu quả ma trận phép nhân thống trị hiệu suất các sự cân nhắc (The weight matrix alone contains 256 × 512 = 131,072 parameters that define these transformations, illustrating why efficient matrix multiplication dominates performance considerations).
Thần kinh các mạng sử dụng ma trận các hoạt động qua đa dạng thuộc về kiến trúc các mẫu vượt ra ngoài đơn giản tuyến tính các lớp (Neural networks employ matrix operations across diverse architectural patterns beyond simple linear layers). Ma trận các hoạt động xuất hiện một cách nhất quán qua hiện đại thần kinh các kiến trúc (Matrix operations appear consistently across modern neural architectures). Tích chập các hoạt động biến đổi thành ma trận các phép nhân thông qua im2col kỹ thuật17, việc cho phép hiệu quả sự thực thi trên được tối ưu hóa-cho-ma trận phần cứng (Convolution operations transform into matrix multiplications through the im2col technique17, enabling efficient execution on matrix-optimized hardware). Danh sách 11.6 minh họa những đa dạng các ứng dụng này (Listing 11.6 illustrates these diverse applications).
Danh sách 11.6: Ma trận Các mẫu Qua Các kiến trúc: Tuyến tính các lớp, sự chú ý các cơ chế, và các sự tích chập tất cả giảm chính công việc tới ma trận các phép nhân, việc làm ma trận phần cứng được chia sẻ nguyên thủy qua hiện đại thần kinh các kiến trúc (Listing 11.6: Matrix Patterns Across Architectures: Linear layers, attention mechanisms, and convolutions all reduce key work to matrix multiplications, making matrix hardware the shared primitive across modern neural architectures).
hidden = matmul(weights, inputs)
# các trọng số: [đầu_ra_chiều x đầu_vào_chiều], các đầu vào: [đầu_vào_chiều x lô] (weights: [out_dim x in_dim], inputs: [in_dim x batch])
# Kết quả kết hợp tất cả các đầu vào cho mỗi đầu ra (Result combines all inputs for each output)
# Sự chú ý Các cơ chế - Nhiều ma trận các hoạt động (Attention Mechanisms - Multiple matrix operations)
Q = matmul(Wq, inputs)
# Chiếu các đầu vào tới truy vấn không gian [truy vấn_chiều x lô] (Project inputs to query space [query_dim x batch])
K = matmul(Wk, inputs)
# Chiếu các đầu vào tới khóa không gian [khóa_chiều x lô] (Project inputs to key space [key_dim x batch])
attention = matmul(Q, K.T)
# So sánh tất cả các truy vấn với tất cả các khóa [truy vấn_chiều x khóa_chiều] (Compare all queries with all keys [query_dim x key_dim])
# Các sự tích chập - Ma trận nhân sau khi việc định hình lại (Convolutions - Matrix multiply after reshaping)
patches = im2col(input)
# Chuyển đổi [H x W x C] hình ảnh tới ma trận của các mảnh (Convert [H x W x C] image to matrix of patches)
output = matmul(kernel, patches)
# Áp dụng các hạt nhân tới tất cả các mảnh một cách đồng thời (Apply kernels to all patches simultaneously)
11.3.2.2 Ma trận các hoạt động phần cứng sự gia tốc (Matrix operations hardware acceleration)
Điều này lan tỏa mẫu của ma trận phép nhân có trực tiếp các hệ lụy cho phần cứng thiết kế: các máy gia tốc cần chuyên biệt các đơn vị thứ mà có thể xử lý những các sự tính toán này ở quy mô (This pervasive pattern of matrix multiplication has direct implications for hardware design: accelerators need specialized units that can handle these computations at scale). Danh sách 11.7 chứng minh một tiêu biểu được cống hiến ma trận đơn vị thứ mà xử lý một toàn bộ 16×16 khối cùng một lúc, việc minh họa tại sao ma trận các lệnh và tensor các lõi có thể phân phối nhiều cao hơn thông lượng so với vô hướng hoặc chỉ-vector sự thực thi các đường dẫn (NVIDIA 2017; Intel Corporation 2021a) (Listing 11.7 demonstrates a representative dedicated matrix unit that processes an entire 16×16 block at once, illustrating why matrix instructions and tensor cores can deliver much higher throughput than scalar or vector-only execution paths (NVIDIA 2017; Intel Corporation 2021a)).
Danh sách 11.7: Ma trận Đơn vị Hoạt động: Cho phép hiệu quả theo-khối ma trận phép nhân và sự tích lũy trong được gia tốc-bởi-phần cứng các hệ thống, việc chứng minh cách nào chuyên biệt các đơn vị hợp lý hóa tính toán các nhiệm vụ cho AI/ML các hoạt động (Listing 11.7: Matrix Unit Operation: Enables efficient block-wise matrix multiplication and accumulation in hardware-accelerated systems, demonstrating how specialized units streamline computational tasks for AI/ML operations).
mload mr1, (weight_ptr)
# Tải cho ví dụ, $16{\times}16$ khối của (Load e.g., $16{\times}16$ block of)
# trọng số ma trận (weight matrix)
mload mr2, (input_ptr)
# Tải tương ứng đầu vào khối (Load corresponding input block)
matmul.mm mr3, mr1, mr2
# Nhân và tích lũy toàn bộ (Multiply and accumulate entire)
# các khối cùng một lúc (blocks at once)
mstore (output_ptr), mr3
# Lưu trữ được tính toán đầu ra khối (Store computed output block)
Này ma trận việc xử lý đơn vị có thể xử lý 16×16 các khối của tuyến tính lớp sự tính toán được mô tả sớm hơn, việc xử lý 256 nhân-tích lũy các hoạt động một cách đồng thời được so sánh tới tám các hoạt động khả thi với vector việc xử lý (This matrix processing unit can handle 16×16 blocks of the linear layer computation described earlier, processing 256 multiply-accumulate operations simultaneously compared to the eight operations possible with vector processing). Những ma trận các hoạt động này bổ sung được vector hóa sự tính toán bằng cách việc cho phép được cấu trúc nhiều-tới-nhiều các sự biến đổi (These matrix operations complement vectorized computation by enabling structured many-to-many transformations). Sự tương tác giữa ma trận và vector các hoạt động định hình tính hiệu quả của thần kinh mạng sự thực thi (The interplay between matrix and vector operations shapes the efficiency of neural network execution).
Giống như vector việc xử lý, ma trận sự gia tốc có sâu lịch sử các gốc rễ—các DSP và các GPU được tối ưu hóa cho ma trận các sự tính toán trong các 1980s-1990s cho hình ảnh việc xử lý, khoa học việc điện toán, và 3D việc kết xuất (Golub and Loan 1996; Owens et al. 2008; Hwu 2011) (Like vector processing, matrix acceleration has deep historical roots—DSPs and GPUs optimized for matrix computations in the 1980s-1990s for image processing, scientific computing, and 3D rendering (Golub and Loan 1996; Owens et al. 2008; Hwu 2011)). Thần kinh các mạng đã làm ma trận phép nhân về mặt thương mại thống trị, việc dẫn dắt sự phát triển của được cống hiến tensor các lõi và các TPU thứ mà xử lý những các hoạt động này ở chưa từng có quy mô (Neural networks have made matrix multiplication commercially dominant, driving the development of dedicated tensor cores and TPUs that process these operations at unprecedented scale).

================ PAGE 605 ================

11. Phần cứng Sự gia tốc (Hardware Acceleration)
567
Ma trận và vector các hoạt động cùng nhau xử lý tuyến tính đại số của thần kinh các mạng (Matrix and vector operations together handle the linear algebra of neural networks). Giữa mọi tuyến tính sự biến đổi, tuy nhiên, ngồi một phi tuyến tính sự kích hoạt hàm—và những siêu việt các sự tính toán này (các hàm mũ, các căn bậc hai, lượng giác các hàm) không thể được một cách hiệu quả biểu diễn thông qua nhân-tích lũy một mình nó (Between every linear transformation, however, sits a nonlinear activation function—and these transcendental computations (exponentials, square roots, trigonometric functions) cannot be efficiently expressed through multiply-accumulate alone). Bảng 11.3 đối chiếu hai nguyên thủy các loại, việc làm rõ cái nào thần kinh mạng các hoạt động ánh xạ tới mỗi cái (Table 11.3 contrasts the two primitive types, clarifying which neural network operations map to each).
Bảng 11.3: Hoạt động Các đặc điểm: Ma trận các hoạt động xuất sắc ở nhiều-tới-nhiều các sự biến đổi phổ biến trong thần kinh mạng các lớp, trong khi vector các hoạt động một cách hiệu quả xử lý một-tới-một các sự biến đổi giống như sự kích hoạt các hàm và lớp sự chuẩn hóa (Table 11.3: Operation Characteristics: Matrix operations excel at many-to-many transformations common in neural network layers, while vector operations efficiently handle one-to-one transformations like activation functions and normalization). Sự phân biệt xác định cái nào phần cứng nguyên thủy (tensor lõi hoặc vector đơn vị) phân phối tối ưu hiệu suất cho mỗi hoạt động (The distinction determines which hardware primitive (tensor core or vector unit) delivers optimal performance for each operation).
Hoạt động Loại (Operation Type)
Tốt nhất Cho (Best For)
Các ví dụ (Examples)
Chính Đặc điểm (Key Characteristic)
Ma trận Các hoạt động (Matrix Operations)
Nhiều-tới-nhiều các lệnh biến đổi (Many-to-many transforms)
Lớp các sự biến đổi, sự chú ý, các sự tích chập (Layer transformations, attention, convolutions)
Mỗi đầu ra phụ thuộc trên nhiều các đầu vào (Each output depends on multiple inputs)
Vector Các hoạt động (Vector Operations)
Một-tới-một các lệnh biến đổi (One-to-one transforms)
Sự kích hoạt các hàm, lớp sự chuẩn hóa, theo-phần tử các gradient (Activation functions, layer normalization, element-wise gradients)
Mỗi đầu ra phụ thuộc chỉ trên tương ứng đầu vào (Each output depends only on corresponding input)
11.3.3 Đặc biệt chức năng các đơn vị (Special function units)
Đặc biệt Chức năng Các đơn vị (SFUs) cung cấp được cống hiến phần cứng cho những phi tuyến tính các sự tính toán này, việc hoàn thành bộ ba của cốt lõi việc xử lý các nguyên thủy (Special Function Units (SFUs) provide dedicated hardware for these nonlinear computations, completing the trio of core processing primitives). Nhu cầu cho như vậy các đơn vị là không mới: dấu phẩy-động các bộ đồng xử lý đã giải quyết vô hướng số học các nút thắt cổ chai (Palmer 1980), và kỹ thuật số tín hiệu việc xử lý phần cứng đã giải quyết có liên quan các nhu cầu cho chuyên biệt số học trong khoa học và việc xử lý-tín hiệu các khối lượng công việc (Smith 1997) (The need for such units is not new: floating-point coprocessors addressed scalar arithmetic bottlenecks (Palmer 1980), and digital signal processing hardware addressed related demands for specialized arithmetic in scientific and signal-processing workloads (Smith 1997)). Thần kinh các mạng đã làm tăng cường điều này nhu cầu bởi vì sự kích hoạt các hàm, sự chuẩn hóa các lớp, và softmax các sự biến đổi xuất hiện sau mọi tuyến tính lớp, việc làm chúng một thông lượng nút thắt cổ chai thay vì một thỉnh thoảng sự tiện lợi (Neural networks have intensified this demand because activation functions, normalization layers, and softmax transformations appear after every linear layer, making them a throughput bottleneck rather than an occasional convenience).
11.3.3.1 Phi tuyến tính các hàm (Nonlinear functions)
Để thấy tại sao được cống hiến phần cứng quan trọng, xem xét một tiêu biểu lớp chuỗi (Goodfellow et al. 2016) (To see why dedicated hardware matters, consider a typical layer sequence (Goodfellow et al. 2016)). Danh sách 11.8 kết hợp tuyến tính các sự biến đổi với phi tuyến tính các sự kích hoạt—các hoạt động thứ mà xuất hiện đơn giản trong Python nhưng tiết lộ đáng kể tính toán tính phức tạp ở phần cứng cấp (Listing 11.8 combines linear transformations with nonlinear activations—operations that appear simple in Python but reveal substantial computational complexity at the hardware level).
Danh sách 11.8: Phi tuyến tính Các sự biến đổi: Thần kinh các mạng xử lý đầu vào dữ liệu thông qua một chuỗi của tuyến tính các sự biến đổi được theo sau bởi phi tuyến tính các sự kích hoạt để nắm bắt phức tạp các mẫu (Listing 11.8: Nonlinear Transformations: Neural networks process input data through a sequence of linear transformations followed by nonlinear activations to capture complex patterns). Này lớp chuỗi nâng cao mô hình tính biểu đạt và sự học hỏi các khả năng (This layer sequence enhances model expressiveness and learning capabilities).
layer = nn.Sequential(
nn.Linear(256, 512), nn.ReLU(), nn.BatchNorm1d(512)
)
output = layer(input_tensor)
Điều này chuỗi giới thiệu nhiều phi tuyến tính các sự biến đổi thứ mà mở rộng vượt ra ngoài đơn giản ma trận các hoạt động (This sequence introduces multiple nonlinear transformations that extend beyond simple matrix operations). Danh sách 11.9 phá vỡ những các hoạt động này thành của chúng toán học các thành phần, việc phơi bày tính toán tính phức tạp thứ mà phần cứng phải giải quyết (Listing 11.9 breaks down these operations into their mathematical components, exposing the computational complexity that hardware must address).
Danh sách 11.9: Phi tuyến tính Các sự biến đổi: Thần kinh các mạng áp dụng tuyến tính và phi tuyến tính các hoạt động để biến đổi đầu vào dữ liệu thành có ý nghĩa các đặc trưng cho sự học hỏi (Listing 11.9: Nonlinear Transformations: Neural networks apply linear and nonlinear operations to transform input data into meaningful features for learning). Máy học hỏi các mô hình sử dụng những các sự biến đổi này để nắm bắt phức tạp các mẫu trong dữ liệu một cách hiệu quả (Machine learning models use these transformations to capture complex patterns in data efficiently).
Z = matmul(weights, input) + bias
# Tuyến tính sự biến đổi (Linear transformation)
H = max(0, Z)
# ReLU sự kích hoạt (ReLU activation)
mean = reduce_mean(H, axis=0)
# BatchNorm các thống kê (BatchNorm statistics)
var = reduce_mean((H - mean) ** 2)
# Phương sai sự tính toán (Variance computation)
output = gamma * (H - mean) / sqrt(var + eps) + beta
# Sự chuẩn hóa (Normalization)
11.3.3.2 Phần cứng sự triển khai của phi tuyến tính các hàm (Hardware implementation of nonlinear functions)
Tính toán tính phức tạp của những các hoạt động này trở nên rõ ràng khi việc kiểm tra của chúng sự triển khai trên truyền thống các bộ xử lý (The computational complexity of these operations becomes apparent when examining their implementation on traditional processors). Những dường như đơn giản toán học các hoạt động này dịch (These seemingly simple mathematical operations translate

568
11.3 AI Tính toán Các nguyên thủy (AI Compute Primitives)
thành phức tạp các chuỗi của các lệnh (into complex sequences of instructions). Xem xét lô sự chuẩn hóa (Ioffe and Szegedy 2015): việc tính toán sự chuẩn hóa yêu cầu các sự giảm bớt, phương sai sự tính toán, và một căn bậc hai, trong khi các hoạt động giống như softmax giới thiệu các hàm mũ của đó chi phí phụ thuộc trên bộ xử lý sự triển khai (Consider batch normalization (Ioffe and Szegedy 2015): computing the normalization requires reductions, variance calculation, and a square root, while operations like softmax introduce exponentials whose cost depends on the processor implementation). Một được chỉnh lưu tuyến tính đơn vị (ReLU) là về mặt toán học đơn giản, nhưng một ngây thơ vô hướng sự triển khai vẫn thực hiện một sự so sánh và sự lựa chọn cho mọi phần tử; được tối ưu hóa ML các hạt nhân thường làm đó bước không có nhánh (A rectified linear unit (ReLU) is mathematically simple, but a naive scalar implementation still performs a comparison and selection for every element; optimized ML kernels usually make that step branchless). Danh sách 11.10 do đó sử dụng ReLU và lô sự chuẩn hóa để hiển thị hai khác nhau các nguồn của chi phí chung: theo-phần tử các lượt thông qua bộ nhớ và nhiều-lượt sự chuẩn hóa công việc (Listing 11.10 therefore uses ReLU and batch normalization to show two different sources of overhead: element-wise passes through memory and multi-pass normalization work).
Danh sách 11.10: ReLU và BatchNorm Các hoạt động: Thần kinh các mạng xử lý đầu vào dữ liệu thông qua theo-phần tử các sự lựa chọn và nhiều sự chuẩn hóa các lượt, việc làm nổi bật tính hiệu quả các thách thức trong ngây thơ các sự triển khai (Listing 11.10: ReLU and BatchNorm Operations: Neural networks process input data through element-wise selections and multiple normalization passes, highlighting efficiency challenges in naive implementations).
for batch in range(32):
for feature in range(512):
# ReLU: Ngây thơ vô hướng so sánh/lựa chọn; được tối ưu hóa các hạt nhân (ReLU: Naive scalar compare/select; optimized kernels)
# thường triển khai điều này một cách không có nhánh (usually implement this branchlessly.)
z = matmul_output[batch, feature]
h = max(0.0, z)
# Có điều kiện hoạt động (Conditional operation)
# BatchNorm: Nhiều lượt qua dữ liệu (BatchNorm: Multiple passes over data)
mean_sum[feature] += h
# Đầu tiên lượt cho trung bình (First pass for mean)
var_sum[feature] += h * h # Bổ sung lượt cho phương sai (Additional pass for variance)
temp[batch, feature] = h
# Thêm bộ nhớ lưu trữ được cần (Extra memory storage needed)
# Sự chuẩn hóa yêu cầu phức tạp số học (Normalization requires complex arithmetic)
for feature in range(512):
mean = mean_sum[feature] / batch_size
var = (var_sum[feature] / batch_size) - mean * mean
# Căn bậc hai sự tính toán: Nhiều sự lặp lại (Square root computation: Multiple iterations)
scale = gamma[feature] / sqrt(var + eps)
# Có tính lặp lại (Iterative)
# sự xấp xỉ (approximation)
shift = beta[feature] - mean * scale
# Bổ sung lượt qua dữ liệu cho cuối cùng sự tính toán (Additional pass over data for final computation)
for batch in range(32):
output[batch, feature] = temp[batch, feature] *
scale + shift
Những các hoạt động này giới thiệu một vài có liên quan với nhau các sự không hiệu quả thứ mà hợp chất qua sâu các lớp của hiện đại các mạng (These operations introduce several interrelated inefficiencies that compound across the deep layers of modern networks). Nhiều lượt qua dữ liệu làm lạm phát bộ nhớ băng thông các yêu cầu, trong khi phức tạp số học các hoạt động giống như căn bậc hai và hàm mũ đòi hỏi nhiều lệnh các chu kỳ mỗi cái (Multiple passes over data inflate memory bandwidth requirements, while complex arithmetic operations like square root and exponential demand many instruction cycles each). Theo-phần tử các sự lựa chọn chẳng hạn như ReLU là rẻ trên mỗi phần tử nhưng vẫn tạo ra thêm bộ nhớ lưu lượng khi chúng được khởi chạy như tách biệt các hạt nhân, và nhu cầu cho trung gian lưu trữ giữa các lượt xa hơn tăng bộ nhớ áp lực (Element-wise selections such as ReLU are cheap per element but still create extra memory traffic when they are launched as separate kernels, and the need for intermediate storage between passes further increases memory pressure). Vector việc xử lý các đơn vị, được thiết kế cho đều đặn các sự tính toán, không thể hoàn toàn sử dụng của chúng chiều rộng trên các hoạt động giống như các hàm mũ và các căn bậc hai khi những các hàm đó yêu cầu chuyên biệt hoặc thấp hơn-thông lượng các đường dẫn (Vector processing units, designed for regular computations, cannot fully use their width on operations like exponentials and square roots when those functions require specialized or lower-throughput paths).
Nhiều cụ thể hơn, mỗi hoạt động giới thiệu khác biệt các thách thức (More specifically, each operation introduces distinct challenges). Lô sự chuẩn hóa yêu cầu nhiều lượt thông qua dữ liệu: một cho trung bình sự tính toán, một cái khác cho phương sai, và một cuối cùng lượt cho đầu ra sự biến đổi (Batch normalization requires multiple passes through data: one for mean computation, another for variance, and a final pass for output transformation). Mỗi lượt tải và lưu trữ dữ liệu thông qua bộ nhớ hệ thống phân cấp (Each pass loads and stores data through the memory hierarchy). Các hoạt động thứ mà xuất hiện đơn giản trong toán học ký hiệu thường mở rộng thành nhiều các lệnh, đặc biệt cho các căn bậc hai và các hàm mũ trên các bộ xử lý mà không có chuyên biệt phần cứng các đường dẫn (Operations that appear simple in mathematical notation often expand into many instructions, especially for square roots and exponentials on processors without specialized hardware paths). ReLU nói chung ánh xạ tới một so sánh-và-chọn hoặc lớn nhất hoạt động, vì vậy độc lập chi phí của nó bị thống trị ít hơn bởi số học so với bởi bổ sung đọc và ghi nếu nó là không được hợp nhất với lân cận công việc (ReLU generally maps to a compare-and-select or maximum operation, so its standalone cost is dominated less by arithmetic than by the additional read and write if it is not fused with neighboring work). Sự triển khai cần tạm thời lưu trữ cho trung gian các giá trị, việc tăng bộ nhớ sự sử dụng và băng thông sự tiêu thụ (The implementation needs temporary storage for intermediate values, increasing memory usage and bandwidth consumption). Trong khi vector các đơn vị xuất sắc ở đều đặn các sự tính toán, các hàm giống như các hàm mũ và các căn bậc hai thường yêu cầu chuyên biệt các sự triển khai thứ mà có thể không hoàn toàn sử dụng vector việc xử lý các khả năng (While vector units excel at regular computations, functions like exponentials and square roots often require specialized implementations that may not fully use vector processing capabilities).

================ PAGE 607 ================

11. Phần cứng Sự gia tốc (Hardware Acceleration)
569
11.3.3.3 SFU phần cứng sự triển khai (SFU hardware implementation)
Các SFU giải quyết những các sự không hiệu quả này thông qua được cống hiến phần cứng sự triển khai (SFUs address these inefficiencies through dedicated hardware implementation). Hiện đại ML các máy gia tốc bao gồm chuyên biệt các mạch thứ mà biến đổi những phức tạp các hoạt động này thành thấp-độ trễ, cố định-chức năng các sự tính toán (Modern ML accelerators include specialized circuits that transform these complex operations into low-latency, fixed-function computations). Danh sách 11.11 chứng minh điều này tính hiệu quả: việc tải một vector của các giá trị cho phép máy gia tốc để áp dụng ReLU, sigmoid, và kiểu-căn bậc hai các hoạt động thông qua được cống hiến sự thực thi các đường dẫn, việc loại bỏ nhiều phần mềm các lượt và phức tạp lệnh các chuỗi (Listing 11.11 demonstrates this efficiency: loading a vector of values allows the accelerator to apply ReLU, sigmoid, and square-root-style operations through dedicated execution paths, eliminating multiple software passes and complex instruction sequences).
Danh sách 11.11: Phần cứng Sự gia tốc: Đơn-chu kỳ phi tuyến tính các hoạt động cho phép hiệu quả vector việc xử lý trong ML các máy gia tốc, việc chứng minh cách nào chuyên biệt phần cứng làm làm giảm bớt tính toán độ trễ (Listing 11.11: Hardware Acceleration: Single-cycle nonlinear operations enable efficient vector processing in ML accelerators, demonstrating how specialized hardware reduces computational latency).
vld.v v1, (input_ptr)
# Tải vector của các giá trị (Load vector of values)
vrelu.v v2, v1
# Đơn-chu kỳ ReLU trên toàn bộ vector (Single-cycle ReLU on entire vector)
vsigm.v v3, v1
# Cố định-độ trễ sigmoid sự tính toán (Fixed-latency sigmoid computation)
vtanh.v v4, v1
# Trực tiếp phần cứng tanh sự triển khai (Direct hardware tanh implementation)
vrsqrt.v v5, v1
# Nhanh nghịch đảo căn bậc hai (Fast reciprocal square root)
Mỗi SFU triển khai một cụ thể hàm thông qua chuyên biệt mạch (Each SFU implements a specific function through specialized circuitry). Cho ví dụ, một ReLU đơn vị thực hiện sự so sánh và sự lựa chọn trong được cống hiến logic, việc loại bỏ việc phân nhánh chi phí chung (For instance, a ReLU unit performs the comparison and selection in dedicated logic, eliminating branching overhead). Căn bậc hai các hoạt động sử dụng phần cứng các sự triển khai của các thuật toán giống như Newton-Raphson với cố định sự lặp lại các số đếm, việc cung cấp có thể dự đoán độ trễ các giới hạn (Square root operations use hardware implementations of algorithms like Newton-Raphson with fixed iteration counts, providing predictable latency bounds). Hàm mũ và logarit các hàm thường kết hợp nhỏ tra cứu các bảng với phần cứng sự nội suy các mạch (Exponential and logarithmic functions often combine small lookup tables with hardware interpolation circuits). Bảng 11.4 tóm tắt đa dạng phần cứng các sự triển khai và của chúng tiêu biểu các độ trễ, việc kéo dài từ đơn-chu kỳ các sự kích hoạt tới logarit-thời gian các sự giảm bớt (Table 11.4 summarizes the various hardware implementations and their typical latencies, spanning from single-cycle activations to logarithmic-time reductions).
Bảng 11.4: Đặc biệt Chức năng Các đơn vị: Được cống hiến phần cứng các sự triển khai của phổ biến toán học các hàm (giống như relu, sigmoid, và nghịch đảo căn bậc hai) tăng tốc máy học hỏi các sự tính toán bằng cách việc loại bỏ phần mềm chi phí chung và việc cho phép song song việc xử lý của vector dữ liệu (Table 11.4: Special Function Units: Dedicated hardware implementations of common mathematical functions (like relu, sigmoid, and reciprocal square root) accelerate machine learning computations by eliminating software overhead and enabling parallel processing of vector data). Độ trễ các phạm vi là mang tính đại diện thiết kế các mục tiêu, không phổ quát sản phẩm các thông số kỹ thuật; quan trọng điểm là rằng phi tuyến tính các nguyên thủy có khác nhau phần cứng các chi phí (The latency ranges are representative design targets, not universal product specifications; the important point is that nonlinear primitives have different hardware costs).
Chức năng Đơn vị (Function Unit)
Hoạt động (Operation)
Sự triển khai Chiến lược (Implementation Strategy)
Mang tính minh họa Độ trễ (Illustrative Latency)
Sự kích hoạt Đơn vị (Activation Unit)
ReLU, sigmoid, tanh
Từng-mảnh sự xấp xỉ các mạch (Piece-wise approximation circuits)
1–2 các chu kỳ (1–2 cycles)
Các thống kê Đơn vị (Statistics Unit)
Trung bình, phương sai (Mean, variance)
Song song sự giảm bớt các cây (Parallel reduction trees)
log(𝑁) các chu kỳ (log(𝑁) cycles)
Hàm mũ Đơn vị (Exponential Unit)
exp, log
Bảng tra cứu + phần cứng sự nội suy (Table lookup + hardware interpolation)
2–4 các chu kỳ (2–4 cycles)
Căn bậc/Lũy thừa Đơn vị (Root/Power Unit)
sqrt, rsqrt
Cố định-sự lặp lại Newton-Raphson (Fixed-iteration Newton-Raphson)
4–8 các chu kỳ (4–8 cycles)
Vector các hoạt động, ma trận các hoạt động, và đặc biệt chức năng các đơn vị cấu thành ba cốt lõi tính toán các nguyên thủy, nhưng các nguyên thủy một mình chúng không xác định thông lượng (Vector operations, matrix operations, and special function units constitute the three core computational primitives, but primitives alone do not determine throughput). Các nguyên thủy cho chúng ta biết cái gì các hoạt động các máy gia tốc thực hiện một cách hiệu quả; sự thực thi các mô hình cho chúng ta biết cách nào những các hoạt động đó được song song hóa qua hàng ngàn của việc xử lý các phần tử (The primitives tell us what operations accelerators perform efficiently; the execution models tell us how those operations are parallelized across thousands of processing elements). Sự phân biệt này quan trọng bởi vì cùng ma trận phép nhân có thể đạt được 10 phần trăm hoặc 90 phần trăm của đỉnh hiệu suất tùy thuộc trên cách nào nó ánh xạ tới sự thực thi mô hình: một sự khác biệt được dẫn dắt bởi luồng sự tổ chức, bộ nhớ truy cập các mẫu, và sự đồng bộ hóa chi phí chung thay vì thuật toán tính phức tạp (This distinction matters because the same matrix multiplication can achieve 10 percent or 90 percent of peak performance depending on how it maps to the execution model: a difference driven by thread organization, memory access patterns, and synchronization overhead rather than algorithmic complexity).
11.4 Tính toán Các đơn vị và Sự thực thi Các mô hình (Compute Units and Execution Models)
Việc áp dụng ReLU tới một 512-phần tử vector hiển thị tại sao sự thực thi các mô hình quan trọng: hoạt động là đơn giản, nhưng thông lượng phụ thuộc trên liệu phần cứng xử lý những 512 các sự so sánh đó như vô hướng các lệnh, SIMD các làn, GPU các luồng, hoặc tensor-chương trình các đoạn (Applying ReLU to a 512-element vector shows why execution models matter: the operation is simple, but throughput depends on whether the hardware treats those 512 comparisons as scalar instructions, SIMD lanes, GPU threads, or tensor-program fragments). Hiện đại AI các bộ xử lý đóng gói ba tính toán các nguyên thủy thành khác biệt sự thực thi các đơn vị: đơn lệnh, nhiều dữ liệu (SIMD) các đơn vị, tensor các lõi, và việc xử lý các phần tử thứ mà định nghĩa cách nào các sự tính toán được cấu trúc và được phơi bày tới các lập trình viên (Modern AI processors package the three compute primitives into distinct execution units: single instruction, multiple data (SIMD) units, tensor cores, and processing elements that define how computations are structured and exposed to programmers). Việc hiểu sự tổ chức này tiết lộ cả hai lý thuyết các khả năng và thực tế hiệu suất các đặc điểm thứ mà xác định thế giới-thực thông lượng (Understanding this organization reveals both the theoretical capabilities and practical performance characteristics that determine real-world throughput).
11.4.1 Việc ánh xạ các nguyên thủy tới sự thực thi các đơn vị (Mapping primitives to execution units)
Sự tiến triển từ tính toán các nguyên thủy tới sự thực thi các đơn vị theo sau một được cấu trúc hệ thống phân cấp thứ mà phản ánh ngày càng tăng tính phức tạp và sự chuyên biệt hóa của AI các máy gia tốc (The progression from computational primitives to execution units follows a structured hierarchy that reflects the increasing complexity and specialization of AI accelerators):

================ PAGE 608 ================

570
11.4 Tính toán Các đơn vị và Sự thực thi Các mô hình (Compute Units and Execution Models)
18
Được làm giảm bớt-Độ chính xác ML (Reduced-Precision ML):
Độ chính xác-hiệu suất
sự đánh đổi
là
có thể định lượng
(Dally et al. 2021; Dally 2023):
việc chia đôi bit-chiều rộng của một
toán hạng
nhân bốn
số lượng của các ALU thứ mà vừa trong
cùng silicon diện tích và chia đôi
bộ nhớ
băng thông
được tiêu thụ
trên mỗi
phần tử (The precision-performance trade-off is quantifiable (Dally et al. 2021; Dally 2023): halving the bit-width of an operand quadruples the number of ALUs that fit in the same silicon area and halves the memory bandwidth consumed per element).
NVIDIA của thuộc về kiến trúc sự dịch chuyển
từ
nặng-FP64
các thiết kế
(Fermi,
Kepler) tới hỗn hợp-
độ chính xác Tensor Các lõi (Volta,
2017) đã phân phối 125 TFLOP/s
của FP16 tensor thông lượng
so với trước thế hệ của 21
TFLOP/s của FP16—xấp xỉ
6× ở cùng 300 W TDP (NVIDIA’s architectural shift from FP64-heavy designs (Fermi, Kepler) to mixed-precision Tensor Cores (Volta, 2017) delivered 125 TFLOP/s of FP16 tensor throughput vs. the prior generation’s 21 TFLOP/s of FP16—roughly 6× at the same 300 W TDP).
Điều này
đã thiết lập
độ chính xác
sự lựa chọn
như
một
hạng-nhất
thuộc về kiến trúc quyết định:
chính xác độ chính xác là thấp nhất
cái thứ mà bảo tồn mô hình
độ chính xác, không cao nhất cái
phần cứng hỗ trợ (This established precision selection as a first-class architectural decision: the correct precision is the lowest one that preserves model accuracy, not the highest one the hardware supports).
19
Việc truyền phát Đa bộ xử lý
(SM) (Streaming Multiprocessor (SM)): Vật lý phần
cứng động cơ thứ mà triển khai
SIMT mô hình bằng cách việc sử dụng
warp các bộ lập lịch để phối
hợp hàng ngàn của song song
các luồng được đề cập trong văn bản (The physical hardware engine that implements the SIMT model by using warp schedulers to coordinate the thousands of parallel threads mentioned in the text).
"Hiệu quả sự chia tỷ lệ" của thần
kinh các mạng là do đó hoàn
toàn phụ thuộc trên việc duy
trì cao SM sự chiếm dụng—
phần của hoạt động các warp có
sẵn tới các bộ lập lịch (The “efficient scaling” of neural networks is therefore entirely dependent on maintaining high SM occupancy—the fraction of active warps available to the schedulers). Nếu sự
chiếm dụng là thấp, SM của sự
thực thi các đơn vị bị chết đói cho
công việc và ngồi nhàn rỗi, việc có nghĩa
GPU là bị ràng buộc bởi bộ nhớ và
không thể đạt được của nó đỉnh tính
toán thông lượng (If occupancy is low, the SM’s execution units are starved for work and sit idle, meaning the GPU is memory bound and cannot achieve its peak computational throughput).
20
Warp (Warp):
Cơ bản sự thực
thi đơn vị của 32 các luồng
thứ mà cho phép SIMT tính hiệu quả
bằng cách việc chia sẻ một đơn lệnh
tìm nạp và việc thực thi trong
bước-khóa (The basic execution unit of 32 threads that enables SIMT efficiency by sharing a single instruction fetch and executing in lock-step). Trực tiếp sự đánh đổi
cho điều này tính hiệu quả là warp sự
phân kỳ: khi các luồng lấy
khác nhau kiểm soát-dòng các đường dẫn,
phần cứng phải tuần tự hóa
mỗi đường dẫn sự thực thi cho tất cả
32 các luồng, có khả năng việc cắt
thông lượng bởi 50 phần trăm hoặc
nhiều hơn (The direct trade-off for this efficiency is warp divergence: when threads take different control-flow paths, the hardware must serialize each path’s execution for all 32 threads, potentially cutting throughput by 50 percent or more). Điều này là tại sao ML các hạt nhân
sử dụng không có nhánh được dự đoán các hoạt
động để duy trì đầy đủ warp
tính hiệu quả (This is why ML kernels use branchless predicated operations to maintain full warp efficiency).
• Vector các hoạt động →SIMD/SIMT các đơn vị thứ mà cho phép song song việc xử lý của độc lập dữ liệu
các phần tử (Vector operations →SIMD/SIMT units that enable parallel processing of independent data elements)
• Ma trận các hoạt động →Tensor các lõi và tâm thu các mảng thứ mà cung cấp được cấu trúc ma trận phép nhân
(Matrix operations →Tensor cores and systolic arrays that provide structured matrix multiplication)
• Đặc biệt các hàm →Được cống hiến phần cứng các đơn vị được tích hợp bên trong việc xử lý các phần tử
(Special functions →Dedicated hardware units integrated within processing elements)
Mỗi sự thực thi đơn vị kết hợp những tính toán các nguyên thủy này với chuyên biệt bộ nhớ và
kiểm soát các cơ chế, việc tối ưu hóa cả hai hiệu suất và năng lượng tính hiệu quả (Each execution unit combines these computational primitives with specialized memory and control mechanisms, optimizing both performance and energy efficiency). Điều này được cấu trúc sự đóng gói
cho phép phần cứng các nhà cung cấp để phơi bày được tiêu chuẩn hóa việc lập trình các giao diện trong khi việc triển khai
đa dạng nằm bên dưới các kiến trúc được may đo tới cụ thể khối lượng công việc các yêu cầu (This structured packaging allows hardware vendors to expose standardized programming interfaces while implementing diverse underlying architectures tailored to specific workload requirements). Sự lựa chọn của sự thực thi
đơn vị một cách đáng kể ảnh hưởng tổng thể hệ thống tính hiệu quả bằng cách việc xác định dữ liệu tính cục bộ, tính toán mật độ,
sự đồng bộ hóa chi phí chung, và bao nhiêu của lý thuyết đỉnh khối lượng công việc có thể thực sự sử dụng (The choice of execution unit significantly influences overall system efficiency by determining data locality, compute density, synchronization overhead, and how much of the theoretical peak the workload can actually use).
11.4.2 Sự tiến hóa từ SIMD tới SIMT các kiến trúc (Evolution from SIMD to SIMT architectures)
Tưởng tượng việc áp dụng ReLU sự kích hoạt tới một 512-phần tử vector (Imagine applying ReLU activation to a 512-element vector).
Một vô hướng bộ xử lý thực thi 512
sự so sánh-và-chọn các hoạt động một cách tuần tự (A scalar processor executes 512 comparison-and-select operations sequentially). Một SIMD (Đơn Lệnh, Nhiều Dữ liệu) đơn vị
xử lý 8 hoặc 16 các phần tử trên mỗi lệnh, việc làm giảm bớt công việc tới 32–64 các lệnh (A SIMD (Single Instruction, Multiple Data) unit processes 8 or 16 elements per instruction, reducing the work to 32–64 instructions). Một SIMT (Đơn
Lệnh, Nhiều Luồng) GPU có thể khởi chạy một hạng nhẹ luồng trên mỗi phần tử; phần cứng
lập lịch những các luồng đó trong các warp hoặc các làn sóng, việc hoàn thành vector thông qua nhiều song song các nhóm
trong khi việc che giấu độ trễ (An SIMT (Single Instruction, Multiple Thread) GPU can launch one lightweight thread per element; the hardware schedules those threads in warps or waves, completing the vector through multiple parallel groups while hiding latency). Sự tiến triển này phản ánh hai có liên quan các ý tưởng: Flynn của SIMD phân loại học đã chính thức hóa
dữ liệu-song song sự thực thi (Flynn 1966), và GPU SIMT các kiến trúc mở rộng đó nguyên lý tới nhiều
hạng nhẹ các luồng được lập lịch trong các warp (Lindholm et al. 2008; Nickolls et al. 2008) (This progression reflects two related ideas: Flynn’s SIMD taxonomy formalized data-parallel execution (Flynn 1966), and GPU SIMT architectures extend that principle to many lightweight threads scheduled in warps (Lindholm et al. 2008; Nickolls et al. 2008)).
SIMD sự thực thi áp dụng giống hệt nhau các hoạt động tới nhiều dữ liệu các phần tử một cách song song, việc tối thiểu hóa
lệnh chi phí chung trong khi việc tối đa hóa dữ liệu thông lượng (SIMD execution applies identical operations to multiple data elements in parallel, minimizing instruction overhead while maximizing data throughput). Điều này sự thực thi mô hình là một cách rộng rãi được sử dụng để
tăng tốc các khối lượng công việc với đều đặn, độc lập dữ liệu sự song song, chẳng hạn như thần kinh mạng các sự tính
toán (This execution model is widely used to accelerate workloads with regular, independent data parallelism, such as neural network computations). Arm Có thể chia tỷ lệ Vector Phần mở rộng (SVE) cung cấp một mang tính đại diện ví dụ của cách nào hiện đại
các kiến trúc triển khai có thể chia tỷ lệ SIMD các hoạt động một cách hiệu quả (Stephens et al. 2017) (The Arm Scalable Vector Extension (SVE) provides a representative example of how modern architectures implement scalable SIMD operations efficiently (Stephens et al. 2017)). Danh sách 11.12
chứng minh điều này cách tiếp cận (Listing 11.12 demonstrates this approach).
Danh sách 11.12: Vector Hoạt động: Vector phép nhân và phép cộng các hoạt động cho phép hiệu quả song song việc xử lý trong máy
học hỏi các mô hình (Listing 11.12: Vector Operation: Vector multiplication and addition operations enable efficient parallel processing in machine learning models).
ptrue p0.s
# Tạo vị ngữ cho vector chiều dài (Create predicate for vector length)
ld1w z0.s, p0/z, [x0]
# Tải vector của các đầu vào (Load vector of inputs)
fmul z1.s, z0.s, z0.s
# Nhân các phần tử (Multiply elements)
fadd z2.s, z1.s, z0.s
# Cộng các phần tử (Add elements)
st1w z2.s, p0, [x1]
# Lưu trữ các kết quả (Store results)
ptrue vị ngữ thứ mà mở này chuỗi là cái gì làm SVE có thể chia tỷ lệ: nó truy vấn phần cứng của
bản địa vector chiều dài ở chạy thời gian, vì vậy cùng nhị phân bão hòa một hẹp 128-bit vector đơn vị và một
rộng 2048-bit một cái mà không có sự biên dịch lại (Stephens et al. 2017) (The ptrue predicate that opens this sequence is what makes SVE scalable: it queries the hardware’s native vector length at run time, so the same binary saturates a narrow 128-bit vector unit and a wide 2048-bit one without recompilation (Stephens et al. 2017)). Intel của Tiên tiến Ma trận Các phần mở rộng
(AMX) là một khác biệt loại của sự chuyên biệt hóa: ô gạch các thanh ghi và ma trận các lệnh phơi bày hai-
chiều ma trận các hoạt động một cách trực tiếp tới phần mềm thay vì chỉ đơn thuần việc làm rộng một vector làn (Intel
Corporation 2021a) (Intel’s Advanced Matrix Extensions (AMX) are a different kind of specialization: tile registers and matrix instructions expose two-dimensional matrix operations directly to software rather than merely widening a vector lane (Intel Corporation 2021a)). Cùng nhau, SVE và AMX hiển thị hai hướng về-phần cứng các đường dẫn cho ML các hạt nhân:
vector-chiều dài-có thể di chuyển SIMD và cố định dựa trên-ô gạch ma trận sự gia tốc (Together, SVE and AMX show two hardware-facing paths for ML kernels: vector-length-portable SIMD and fixed tile-based matrix acceleration).
Để giải quyết những các giới hạn này, SIMT18 mở rộng SIMD các nguyên lý bằng cách việc cho phép song song sự thực thi
qua nhiều độc lập các luồng, mỗi cái việc duy trì của chính nó chương trình bộ đếm và thuộc về kiến trúc
trạng thái (Lindholm et al. 2008; Nickolls et al. 2008) (To address these limitations, SIMT18 extends SIMD principles by enabling parallel execution across multiple independent threads, each maintaining its own program counter and architectural state (Lindholm et al. 2008; Nickolls et al. 2008)). Này mô hình ánh xạ một cách tự nhiên tới ma trận các sự tính toán,
nơi mỗi luồng xử lý khác nhau các phần của một khối lượng công việc trong khi vẫn việc hưởng lợi từ được chia sẻ
lệnh sự thực thi (This model maps naturally to matrix computations, where each thread processes different portions of a workload while still benefiting from shared instruction execution). Trong NVIDIA của GPU các kiến trúc, mỗi Việc truyền phát Đa bộ xử lý (SM)19
phối hợp hàng ngàn của các luồng việc thực thi trong song song, việc cho phép cho hiệu quả sự chia tỷ lệ của thần kinh
mạng các sự tính toán (In NVIDIA’s GPU architectures, each Streaming Multiprocessor (SM)19 coordinates thousands of threads executing in parallel, allowing for efficient scaling of neural network computations). Các luồng được tổ chức thành các warp20, thứ mà là cơ bản sự thực thi các đơn vị thứ mà
cho phép SIMT tính hiệu quả (Threads are organized into warps20, which are the basic execution units that enable SIMT efficiency). Danh sách 11.13 hiển thị điều này song song việc xử lý mô hình trong hành động (Listing 11.13 shows this parallel processing model in action).

================ PAGE 609 ================

572
11.4 Tính toán Các đơn vị và Sự thực thi Các mô hình (Compute Units and Execution Models)
23
Tensor Lõi (Tensor Core):
Một đơn
tensor lõi lệnh
thực thi một hoàn chỉnh ma trận-
nhân-tích lũy hoạt động
trên một nhỏ ô gạch của dữ liệu
việc sử dụng một được cống hiến phần cứng
khối (NVIDIA 2017; NVIDIA Corporation 2020) (A single tensor core instruction executes a complete matrix-multiply-accumulate operation on a small tile of data using a dedicated hardware block (NVIDIA 2017; NVIDIA Corporation 2020)). Cách tiếp cận này bỏ qua chi phí chung
của việc tìm nạp và việc lập lịch
hàng chục của cá nhân số
học các lệnh trên đa-
mục đích CUDA các lõi (This approach bypasses the overhead of fetching and scheduling dozens of individual arithmetic instructions on general-purpose CUDA cores).
Bởi
vì những các khối này cấu thành
một lớn phần của một hiện
đại máy gia tốc của được quảng cáo
tensor thông lượng, việc thất bại để
sử dụng chúng có thể để lại hầu hết của
chip của lý thuyết đỉnh không
có sẵn tới khối lượng công việc (Because these blocks constitute a large fraction of a modern accelerator’s advertised tensor throughput, failing to use them can leave most of the chip’s theoretical peak unavailable to the workload).
24
Thần kinh Việc xử lý Đơn vị
(NPU) (Neural Processing Unit (NPU)): Di động các NPU đạt được
thấp-năng lượng sự suy luận bằng cách việc
triển khai phổ biến tensor
các hoạt động trong cố định-chức năng
hoặc một cách hẹp có thể lập trình
phần cứng thay vì như hoàn toàn
đa-mục đích GPU các hạt nhân (Mobile NPUs achieve low-power inference by implementing common tensor operations in fixed-function or narrowly programmable hardware rather than as fully general GPU kernels). Này thuộc về
kiến trúc sự cam kết có thể
phân phối lớn năng lượng-tính hiệu quả
các lợi ích cho được hỗ trợ các hạt nhân,
nhưng nó làm sự triển khai phụ
thuộc trên toán tử phạm vi phủ sóng:
không được hỗ trợ các hàm phải
rơi trở lại tới một CPU hoặc GPU
đường dẫn thứ mà có thể là kém hơn nhiều hiệu
quả cho đó khối lượng công việc (Sze et al. 2017) (This architectural commitment can deliver large energy-efficiency gains for supported kernels, but it makes deployment dependent on operator coverage: unsupported functions must fall back to a CPU or GPU path that may be far less efficient for that workload (Sze et al. 2017)).
vô hướng hoặc vector các hoạt động (scalar or vector operations). Điều này được cấu trúc cách tiếp cận cho phép phần cứng để đạt được cao thông lượng trong khi việc làm giảm bớt gánh nặng của rõ ràng vòng lặp việc mở cuộn và dữ liệu sự quản lý ở phần mềm cấp (This structured approach enables hardware to achieve high throughput while reducing the burden of explicit loop unrolling and data management at the software level).
Thiết kế các sự ưu tiên xác định cách nào ma trận các động cơ xuất hiện trong khác nhau bộ xử lý các họ (Design priorities determine how matrix engines appear in different processor families). GPU tensor các lõi bảo tồn tính có thể lập trình trong khi việc tăng tốc đa-mục đích sâu sự học hỏi các hạt nhân (GPU tensor cores preserve programmability while accelerating general-purpose deep learning kernels). Kiểu-TPU các thiết kế sử dụng lớn-quy mô ma trận các đơn vị được sắp xếp trong tâm thu các mảng để tối đa hóa được duy trì sự đào tạo thông lượng trên dày đặc tensor các hạt nhân (TPU-style designs use large-scale matrix units arranged in systolic arrays to maximize sustained training throughput on dense tensor kernels). Di động các NPU24 thu nhỏ cùng ý tưởng thành thấp-năng lượng sự suy luận các khối, trong khi máy chủ các CPU thêm ma trận lệnh các phần mở rộng (kiểu-AMX các ô gạch) cho sự suy luận và hỗn hợp các khối lượng công việc (Mobile NPUs24 shrink the same idea into low-power inference blocks, while server CPUs add matrix instruction extensions (AMX-class tiles) for inference and mixed workloads). Mỗi phiên bản thay đổi cùng hợp đồng: bao nhiêu tính linh hoạt phần cứng giữ trong khi việc làm giảm bớt sự di chuyển xung quanh dày đặc ma trận các hoạt động (Each version changes the same contract: how much flexibility the hardware keeps while reducing movement around dense matrix operations).
Ngày càng tăng sự chuyên biệt hóa của AI phần cứng đã dẫn dắt có thể đo lường hiệu suất các sự cải thiện trong sâu sự học hỏi các khối lượng công việc (The increasing specialization of AI hardware has driven measurable performance improvements in deep learning workloads). Để đánh giá cao độ lớn của sự dịch chuyển này, theo dõi đường cong trong hình 11.6 từ trái sang phải: qua một đơn thập kỷ, NVIDIA của được quảng cáo đơn-chip thông lượng đã tăng xấp xỉ 1,000× (ba các bậc của độ lớn) từ K20X của 3.9 TFLOP/s trong FP32 tới H100 của xấp xỉ 4,000 TFLOP/s trong FP8, như kiến trúc đã chuyển đổi từ đa-mục đích dấu phẩy-động sự thực thi các đơn vị tới được cống hiến xử lý-tensor các lõi, thấp hơn độ chính xác các định dạng, và được cấu trúc sự thưa thớt sự hỗ trợ (NVIDIA Corporation 2017, 2020, 2024; Choquette 2023) (To appreciate the magnitude of this shift, trace the curve in figure 11.6 from left to right: over a single decade, NVIDIA’s advertised single-chip throughput rose roughly 1,000× (three orders of magnitude) from the K20X’s 3.9 TFLOP/s in FP32 to the H100’s roughly 4,000 TFLOP/s in FP8, as the architecture transitioned from general-purpose floating-point execution units to dedicated tensor-processing cores, lower precision formats, and structured sparsity support (NVIDIA Corporation 2017, 2020, 2024; Choquette 2023)). Bởi vì được vẽ biểu đồ các điểm trộn lẫn độ chính xác các định dạng và FLOP/s với INT8 TOPS, đường cong theo dõi thế hệ-qua-thế hệ khả năng thay vì một nhất quán đơn vị, vì vậy sau này B200 ngồi thậm chí cao hơn (Because the plotted points mix precision formats and FLOP/s against INT8 TOPS, the curve tracks generation-over-generation capability rather than one consistent unit, so the later B200 sits even higher).
2012
2014
2016 2017
2020
2022
2024
1
10
100
1,000
10,000
K20X
3.9 TFLOP/s FP32
M40
6.8 TFLOP/s FP32
P40
47 TOPS INT8
V100
125 TFLOP/s FP16
A100
1,248 TOPS INT8
H100
4,000 TFLOP/s FP8
B200
9,000 TFLOP/s FP8
Năm (Year)
Đỉnh thông lượng (như được dán nhãn) (Peak throughput (as labeled))
NVIDIA GPU Sự suy luận Hiệu suất (NVIDIA GPU Inference Performance)
TFLOP/s cho dấu phẩy động; TOPS cho INT8, logarit thang đo (TFLOP/s for ﬂoating point; TOPS for INT8, logarithmic scale)
1,000×
Hình 11.6: GPU Hiệu suất Sự chia tỷ lệ: NVIDIA được quảng cáo đơn-chip đỉnh thông lượng đã tăng bởi nhiều hơn 1,000× qua xấp xỉ một thập kỷ, từ kỷ nguyên-K20X FP32 thông lượng tới H100/B200 tensor-hoạt động các đỉnh (Figure 11.6: GPU Performance Scaling: NVIDIA advertised single-chip peak throughput increased by more than 1,000× over roughly a decade, from K20X-era FP32 throughput to H100/B200 tensor-operation peaks). Được vẽ biểu đồ các nhãn trộn lẫn độ chính xác các chế độ, vì vậy hình nên được đọc như một thuộc về kiến trúc xu hướng, không một táo-tới-táo FP32 sự so sánh (The plotted labels mix precision modes, so the figure should be read as an architectural trend, not an apples-to-apples FP32 comparison). Điều này lợi ích đã được dẫn dắt bởi tensor lõi sự gia tốc, được làm giảm bớt độ chính xác (FP16, INT8, FP8, FP4), và được gia tốc-bởi-phần cứng được cấu trúc sự thưa thớt (NVIDIA Corporation 2017, 2020, 2024; Choquette 2023) (This gain was driven by tensor core acceleration, reduced precision (FP16, INT8, FP8, FP4), and hardware-accelerated structured sparsity (NVIDIA Corporation 2017, 2020, 2024; Choquette 2023)).
11.4.4 Việc xử lý các phần tử (Processing elements)
Cao nhất cấp của sự thực thi đơn vị sự tổ chức tích hợp nhiều tensor các lõi với cục bộ bộ nhớ thành việc xử lý các phần tử (PE) (The highest level of execution unit organization integrates multiple tensor cores with local memory into processing elements (PEs)). Một việc xử lý phần tử phục vụ như chính xây dựng khối trong nhiều AI các máy gia tốc, việc kết hợp khác nhau tính toán các đơn vị để một cách hiệu quả thực thi thần kinh mạng các hoạt động (A processing element serves as the primary building block in many AI accelerators, combining different computational units to efficiently execute neural network operations). Mỗi PE điển hình bao gồm vector các đơn vị cho theo-phần tử các hoạt động, tensor các lõi cho ma trận sự tính toán, đặc biệt chức năng các đơn vị cho phi tuyến tính các sự biến đổi, và được cống hiến bộ nhớ các tài nguyên để tối ưu hóa dữ liệu tính cục bộ và tối thiểu hóa dữ liệu sự di chuyển chi phí chung (Each PE typically includes vector units for element-wise operations, tensor cores for matrix computation, special function units for nonlinear transformations, and dedicated memory resources to optimize data locality and minimize data movement overhead).
Việc xử lý phần tử thiết kế thay đổi bởi vì mỗi kiến trúc chọn một khác nhau sự cân bằng giữa tính toán mật độ, cục bộ bộ nhớ, và khoảng cách kết nối liên thông (Processing element design varies because each architecture chooses a different balance between compute density, local memory, and interconnect distance). Graphcore của Sự thông minh Việc xử lý Đơn vị (Graphcore’s Intelligence Processing Unit)

================ PAGE 611 ================

11. Phần cứng Sự gia tốc (Hardware Acceleration)
573
25
N:M Được cấu trúc Sự thưa
thớt (N:M Structured Sparsity): 2:4 tỷ lệ (50 phần trăm
mật độ) được sử dụng bởi NVIDIA của
Ampere Thưa thớt Tensor Các lõi
là một thân thiện-với-phần cứng sự thỏa
hiệp:
mọi liên tiếp
bốn-giá trị nhóm giữ lại hai
khác không các giá trị, việc bảo tồn
đều đặn việc lập chỉ mục trong khi việc chia
đôi dày đặc giá trị tải
trọng (NVIDIA Corporation
2020) (The 2:4 ratio (50 percent density) used by NVIDIA’s Ampere Sparse Tensor Cores is a hardware-friendly compromise: every contiguous four-value group retains two nonzero values, preserving regular indexing while halving the dense value payload (NVIDIA Corporation 2020)).
Ở 2:4, siêu
dữ liệu chi phí chung là nhỏ gọn
đủ để lưu trữ cùng với
các trọng số mà không làm choáng
ngợp bộ nhớ-lưu lượng các khoản tiết
kiệm, thứ mà là sự ràng buộc
thứ mà làm được quảng cáo 2×
tensor-toán học thông lượng đường dẫn
hợp lý khi các hạt nhân và
mô hình các trọng số thỏa mãn mẫu (At 2:4, the metadata overhead is compact enough to store alongside the weights without overwhelming the memory-traffic savings, which is the constraint that makes the advertised 2× tensor-math throughput path plausible when kernels and model weights satisfy the pattern).
(IPU) phân phối sự tính toán qua 1,472 các ô gạch, mỗi cái việc chứa độc lập việc xử lý các phần tử được tối ưu hóa cho mịn-hạt sự song song (Graphcore 2020) ((IPU) distributes computation across 1,472 tiles, each containing independent processing elements optimized for fine-grained parallelism (Graphcore 2020)). Cerebras mở rộng cùng cục bộ-tính toán nguyên lý trong CS-2 hệ thống, việc tích hợp xấp xỉ 850,000 được tối ưu hóa-cho-AI các lõi qua một cấp-tấm bán dẫn thiết bị cho sâu sự học hỏi sự gia tốc (Systems 2021) (Cerebras extends the same local-compute principle in the CS-2 system, integrating roughly 850,000 AI-optimized cores across a wafer-scale device for deep learning acceleration (Systems 2021)). Tesla của D1 bộ xử lý nhấn mạnh đáng kể cục bộ bộ nhớ bên trong của nó việc xử lý các phần tử, việc tối ưu hóa thông lượng và độ trễ cho thời gian-thực tự trị phương tiện các khối lượng công việc (Tesla, Inc. 2021) (Tesla’s D1 processor emphasizes substantial local memory inside its processing elements, optimizing throughput and latency for real-time autonomous vehicle workloads (Tesla, Inc. 2021)).
Qua những các thiết kế này, sự ràng buộc đánh đổi là cái danh sách minh họa: tính toán mật độ so với dữ liệu tính cục bộ (Across these designs, the binding trade-off is the one the roster illustrates: compute density versus data locality). Việc đóng gói nhiều hơn các lõi nâng cao đỉnh thông lượng chỉ nếu mỗi cái có thể được giữ được nuôi, vì vậy một việc xử lý phần tử của được phân phối tính hiệu quả phụ thuộc nhiều như trên kết nối liên thông chiến lược và bộ nhớ tính cục bộ như trên thô số học khả năng (Packing more cores raises peak throughput only if each one can be kept fed, so a processing element’s delivered efficiency depends as much on interconnect strategy and memory locality as on raw arithmetic capability).
Đó cùng sự phụ thuộc trên tính cục bộ chi phối cái nào thuật toán các sự tối ưu hóa phần cứng có thể thực sự khai thác (That same dependence on locality governs which algorithmic optimizations the hardware can actually exploit). Một đều đặn lưới của việc xử lý các phần tử tăng tốc sự thưa thớt chỉ khi những cái sống sót khác không các giá trị bảo tồn có thể dự đoán truy cập các mẫu thứ mà lưới phụ thuộc trên, thứ mà là chính xác sự ràng buộc thứ mà N:M được cấu trúc sự thưa thớt là được thiết kế để thỏa mãn (A regular grid of processing elements accelerates sparsity only when the surviving nonzero values preserve the predictable access patterns the grid depends on, which is precisely the constraint that N:M structured sparsity is designed to satisfy).
11.4.5 N:M được cấu trúc sự thưa thớt cơ học (N:M structured sparsity mechanics)
Trong khi không được cấu trúc việc cắt tỉa làm giảm bớt mô hình kích thước, nó hiếm khi dịch tới phần cứng phần tăng tốc bởi vì bộ nhớ truy cập trở nên không đều (While unstructured pruning reduces model size, it rarely translates to hardware speedup because memory access becomes irregular). Phần cứng các máy gia tốc giải quyết điều này với N:M Được cấu trúc Sự thưa thớt25, một dựa trên-mẫu cách tiếp cận thứ mà thực thi tính đều đặn (Hardware accelerators solve this with N:M Structured Sparsity25, a pattern-based approach that enforces regularity). Ký hiệu “𝑁∶𝑀” chỉ định rằng chính xác 𝑁 các giá trị phải là khác không bên trong mọi liên tiếp khối của 𝑀 các giá trị, việc tạo ra một có thể dự đoán mẫu thứ mà phần cứng có thể khai thác (The notation “𝑁∶𝑀” specifies that exactly 𝑁 values must be nonzero within every contiguous block of 𝑀values, creating a predictable pattern that hardware can exploit).
NVIDIA của Thưa thớt Tensor Các lõi triển khai một cụ thể phiên bản của này mẫu: 2:4 sự ràng buộc, thứ mà yêu cầu rằng chính xác hai của mọi liên tiếp khối của bốn các giá trị là khác không (một cách tương đương, hai phải là không) (NVIDIA Corporation 2020; NVIDIA 2020a) (NVIDIA’s Sparse Tensor Cores implement a concrete instance of this pattern: the 2:4 constraint, which requires that exactly two of every contiguous block of four values be nonzero (equivalently, two must be zero) (NVIDIA Corporation 2020; NVIDIA 2020a)). Sự ràng buộc này cho phép phần cứng để nén ma trận bởi 50 phần trăm trong bộ nhớ cộng với siêu dữ liệu (This constraint allows the hardware to compress the matrix by 50 percent in memory plus metadata). Sự thực thi tiến hành trong ba các giai đoạn: đầu tiên, phần cứng lưu trữ chỉ hai khác không các giá trị và nhỏ gọn siêu dữ liệu cho mọi bốn-phần tử khối (sự nén); thứ hai, trong suốt ma trận phép nhân, Thưa thớt Tensor Lõi đọc siêu dữ liệu để chọn tương ứng các sự kích hoạt và thực hiện toán học chỉ trên khác không các trọng số (sự tính toán); thứ ba, điều này tăng hiệu quả FLOP/byte tỷ lệ, việc cung cấp một lên-tới-2× tensor-toán học thông lượng đường dẫn qua dày đặc ma trận phép nhân khi mô hình là được tinh chỉnh để tôn trọng 2:4 sự ràng buộc (The execution proceeds in three stages: first, the hardware stores only the two nonzero values and compact metadata for every four-element block (compression); second, during matrix multiplication, the Sparse Tensor Core reads the metadata to select the corresponding activations and performs math only on the nonzero weights (compute); third, this increases the effective FLOP/byte ratio, providing an up-to-2× tensor-math throughput path over dense matrix multiplication when the model is fine-tuned to respect the 2:4 constraint).
Để hiểu tại sao "Được cấu trúc" các mẫu được yêu cầu cho phần cứng phần tăng tốc, xem xét cách nào thưa thớt các ma trận được thực sự lưu trữ trong bộ nhớ (To understand why “Structured” patterns are required for hardware speedup, consider how sparse matrices are actually stored in memory). Phần C.1.5 đối xử thưa thớt ma trận các định dạng chẳng hạn như CSR và khối thưa thớt lưu trữ một cách chính thức; chúng làm sự ràng buộc có thể nhìn thấy, vì các chỉ mục phải được lưu trữ cùng với các giá trị (Section C.1.5 treats sparse matrix formats such as CSR and block sparse storage formally; they make the constraint visible, since indices must be stored alongside values). So sánh lưu trữ các bố cục trong hình 11.7 (Compare the storage layouts in figure 11.7). Nếu sự thưa thớt là ngẫu nhiên, chỉ mục chi phí chung và không đều truy cập giết chết hiệu suất (If the sparsity is random, the index overhead and irregular access kill performance). Được cấu trúc sự thưa thớt, cho dù ở lớn khối quy mô hoặc mịn-hạt N:M quy mô, làm việc lập chỉ mục này có thể dự đoán và nhỏ gọn, việc cho phép phần cứng để tìm nạp dữ liệu một cách hiệu quả (Structured sparsity, whether at the large block scale or the fine-grained N:M scale, makes this indexing predictable and compact, allowing hardware to fetch data efficiently).
2:4 mẫu minh họa một rộng hơn nguyên lý: phần cứng đạt được tính hiệu quả không bằng cách việc tính toán các số không nhanh hơn, mà bằng cách không bao giờ việc tải chúng trong đầu tiên nơi (The 2:4 pattern illustrates a broader principle: hardware achieves efficiency not by computing zeros faster, but by never loading them in the first place). Sự thấu hiểu này kết nối sự thưa thớt tới bộ nhớ bức tường, vì được cấu trúc các mẫu làm giảm bớt bộ nhớ lưu lượng, thứ mà là nơi thực sự chi phí nằm ở (This insight connects sparsity to the memory wall, since structured patterns reduce memory traffic, which is where the real cost lies).
Vượt ra ngoài được cấu trúc sự thưa thớt các sự tối ưu hóa, khác nhau phần cứng các kiến trúc triển khai ma trận các hoạt động thông qua khác biệt tính toán các cấu trúc (Beyond structured sparsity optimizations, different hardware architectures implement matrix operations through distinct computational structures). Tâm thu các mảng đại diện một như vậy cách tiếp cận thứ mà đã chứng minh đặc biệt hiệu quả cho AI các khối lượng công việc (Systolic arrays represent one such approach that has proven particularly effective for AI workloads).
11.4.6 Tâm thu các mảng (Systolic arrays)
Trong khi tensor các lõi đóng gói ma trận các hoạt động thành được cấu trúc tính toán các đơn vị, tâm thu các mảng cung cấp một thay thế cách tiếp cận được tối ưu hóa cho liên tục dữ liệu dòng và toán hạng sự tái sử dụng (While tensor cores package matrix operations into structured computational units, systolic arrays provide an alternative approach optimized for continuous data flow and operand reuse). Cốt lõi động lực cho tâm thu các kiến trúc bắt nguồn từ cùng năng lượng sự ràng buộc thứ mà dẫn dắt máy gia tốc thiết kế: việc tối thiểu hóa tác động của bộ nhớ truy cập các hình phạt thông qua thuộc về kiến trúc thiết kế (The core motivation for systolic architectures stems from the same energy constraint that drives accelerator design: minimizing the impact of memory access penalties through architectural design). Một đơn giản năng lượng sự so sánh thông qua mảng tiết lộ tại sao kiến trúc này đã trở thành trung tâm tới hiện đại AI các máy gia tốc (A simple energy comparison through the array reveals why this architecture has become central to modern AI accelerators).
Tâm thu kiến trúc cải thiện năng lượng tính hiệu quả bằng cách việc giữ các toán hạng cục bộ như công việc mạch đập thông qua mảng (The systolic architecture improves energy efficiency by keeping operands local as work pulses through the array).

================ PAGE 612 ================

574
11.4 Tính toán Các đơn vị và Sự thực thi Các mô hình (Compute Units and Execution Models)
1
2
4
5
7
9
Dày đặc Ma trận (Dense Matrix)
Thưa thớt Ma trận (CSR) (Sparse Matrix (CSR))
Khối Thưa thớt Ma trận (Block Sparse Matrix)
Khối Thưa thớt (BSR) (Block Sparse (BSR))
Khác-không Khối Các chỉ mục (Non-zero Block Indices)
Hình 11.7: Thưa thớt Lưu trữ Các định dạng: Phần cứng tính hiệu quả phụ thuộc trên cách nào thưa thớt các ma trận được lưu trữ (Figure 11.7: Sparse Storage Formats: Hardware efficiency depends on how sparse matrices are stored). Bốn các bảng hiển thị dày đặc lưu trữ (đơn giản nhưng lãng phí cho các số không), CSR, khối thưa thớt, và khối-thưa thớt BSR bố cục, thứ mà nén ma trận bằng cách việc lưu trữ chỉ khác không các giá trị cộng với chỉ mục của mỗi được lưu trữ khối (The four panels show dense storage (simple but wasteful for zeros), CSR, block sparse, and the block-sparse BSR layout, which compress the matrix by storing only nonzero values plus the index of each stored block). Tách biệt Khác-không Khối Các chỉ mục cột là đó chỉ mục chi phí chung: nó là giá được trả cho việc bỏ qua các số không, và được cấu trúc sự thưa thớt (giống như N:M hoặc các khối) giữ nó có thể dự đoán và nhỏ gọn vì vậy phần cứng có thể tìm nạp dữ liệu một cách hiệu quả (The separate Non-zero Block Indices column is that index overhead: it is the price paid for skipping zeros, and structured sparsity (like N:M or blocks) keeps it predictable and compact so hardware can fetch data efficiently).
26
Tâm thu Mảng (Systolic Array): Từ
Hy Lạp sustole ("sự co bóp"),
được mượn từ tim mạch học
nơi nó mô tả trái tim của
nhịp nhàng
việc bơm
chu kỳ (From Greek sustole (“contraction”), borrowed from cardiology where it describes the heart’s rhythmic pumping cycle).
Kung và Leiserson đã chọn
cái tên bởi vì dữ liệu mạch đập
thông qua
việc xử lý
lưới chính xác như máu mạch đập
thông qua
tuần hoàn
hệ thống—mỗi
phần tử
co bóp
(tính toán)
và
đẩy các kết quả tới của nó hàng xóm
trong bước-khóa (Kung and Leiserson chose the name because data pulses through the processing grid exactly as blood pulses through the circulatory system—each element contracts (computes) and pushes results to its neighbor in lock-step).
Điều này
cứng nhắc
nhịp nhàng dữ liệu đường dẫn là
kiến trúc của cốt lõi sự đánh đổi:
nó xuất sắc ở dày đặc ma trận
phép nhân được mô tả nhưng
chứng minh không linh hoạt cho không đều
các khối lượng công việc, bởi vì một đơn
trọng số được tái sử dụng cho tất cả 128
MAC các hoạt động trong một TPUv4
mảng cột,
việc loại bỏ
hàng trăm
của
cá nhân
bộ nhớ các truy cập (This rigid rhythmic data path is the architecture’s core trade-off: it excels at the dense matrix multiplication described but proves inflexible for irregular workloads, because a single weight is reused for all 128 MAC operations in a TPUv4 array column, eliminating hundreds of individual memory accesses).
Khăn ăn Toán học 11.1 (Napkin Math 11.1): Năng lượng lợi thế của việc mạch đập dữ liệu (The energy advantage of pulsing data)
Kịch bản: "Tâm thu" (nhịp tim) ẩn dụ là không chỉ về thời gian; nó phản ánh một mang tính quyết định năng lượng tính hiệu quả lợi thế (Scenario: The “Systolic” (heartbeat) metaphor is not just about timing; it reflects a decisive energy efficiency advantage). Chúng ta có thể định lượng năng lượng lợi thế của tâm thu dữ liệu dòng qua truyền thống vector các đơn vị việc sử dụng năng lượng hệ quả tất yếu (We can quantify the energy advantage of systolic dataflow over traditional vector units using the energy corollary):
1. Vector đơn vị (Vector unit): Tải 𝐴, tải 𝐵, tính toán 𝐴×𝐵+𝐶, ghi 𝐶. (Loads 𝐴, loads 𝐵, computes 𝐴×𝐵+𝐶, writes 𝐶.)
• Dữ liệu sự di chuyển: 3 các lệnh tải + 1 lệnh ghi = 4 DRAM các truy cập (trên mỗi hoạt động) (Data movement: 3 loads + 1 write = 4 DRAM accesses (per operation)).
• Năng lượng: ≈4 × 640 pJ + 1 pJ (tính toán) = 2561 pJ/op (Energy: ≈4 × 640 pJ + 1 pJ (compute) = 2561 pJ/op).
2. Tâm thu Mảng (128 × 128 kích thước) (Systolic Array (128 × 128 size)): Tải A và B một lần ở các rìa. Dữ liệu "mạch đập" thông qua 128 việc xử lý các phần tử (Loads A and B once at the edges. Data “pulses” through 128 processing elements).
• Dữ liệu sự di chuyển: 2 các lệnh tải trên mỗi 128 các hoạt động = 0.016 DRAM các truy cập (trên mỗi hoạt động) (Data movement: 2 loads per 128 operations = 0.016 DRAM accesses (per operation)).
• Năng lượng: ≈0.016 × 640 pJ + 1 pJ (tính toán) ≈11 pJ/op (Energy: ≈0.016 × 640 pJ + 1 pJ (compute) ≈11 pJ/op).
Các hệ thống sự thấu hiểu (Systems insight): Trong điều này được làm việc năng lượng mô hình, một tâm thu mảng là 232.8× nhiều hơn hiệu quả-năng lượng so với một ngây thơ vector đơn vị cho lớn ma trận các phép nhân (In this worked energy model, a systolic array is 232.8× more energy-efficient than a naive vector unit for large matrix multiplications).
• Một cách cụ thể, một 128×128 mảng có thể đạt được qua 16,384 các MAC/chu kỳ với một lớn năng lượng cổ tức bằng cách việc mạch đập dữ liệu thông qua việc xử lý các phần tử thay vì một cách lặp lại việc tải nó từ DRAM (Horowitz 2014; Jouppi et al. 2023) (Concretely, a 128×128 array can achieve over 16,384 MACs/cycle with a large energy dividend by pulsing data through processing elements instead of repeatedly loading it from DRAM (Horowitz 2014; Jouppi et al. 2023)).
• Điều này tính hiệu quả là cái gì cho phép một Google TPU đóng gói 100,000+ MAC các đơn vị vào một đơn chip mà không bị tan chảy (This efficiency is what allows a Google TPU to pack 100,000+ MAC units into a single chip without melting).
• Sự giới hạn (Limitation): Này "Năng lượng Cổ tức" chỉ trả ra nếu ma trận là đủ lớn để lấp đầy mảng (This “Energy Dividend” only pays out if the matrix is large enough to fill the array). Cho nhỏ các ma trận (phổ biến trong thời gian-thực sự suy luận), mảng là bị sử dụng dưới mức, và năng lượng tính hiệu quả rơi trở lại hướng tới vector đơn vị đường cơ sở (For small matrices (common in real-time inference), the array is underused, and the energy efficiency drops back toward the vector unit baseline).
Một tâm thu mảng sắp xếp việc xử lý các phần tử trong một lưới mẫu, nơi dữ liệu chảy một cách nhịp nhàng giữa lân cận các đơn vị trong một được đồng bộ hóa cách thức, việc cho phép mỗi toán hạng tham gia trong nhiều các sự tính toán như nó lan truyền thông qua mảng (A systolic array arranges processing elements in a grid pattern, where data flows rhythmically between neighboring units in a synchronized manner, enabling each operand to participate in multiple computations as it propagates through the array). Điều này được cấu trúc sự di chuyển tối thiểu hóa bên ngoài bộ nhớ các truy cập bằng cách việc tối đa hóa cục bộ dữ liệu sự tái sử dụng (This structured movement minimizes external memory accesses by maximizing local data reuse). Một đơn trọng số giá trị có thể đóng góp tới hàng chục của các hoạt động như nó di chuyển thông qua việc xử lý các phần tử, việc biến đổi năng lượng hồ sơ từ bị ràng buộc-bởi-bộ nhớ tới hiệu quả-tính toán sự thực thi (A single weight value can contribute to dozens of operations as it moves through the processing elements, transforming the energy profile from memory-bound to compute-efficient execution).
Kung và Leiserson26 (Kung and Leiserson 1979) đầu tiên đã giới thiệu tâm thu các mảng, việc chính thức hóa

================ PAGE 613 ================

11. Phần cứng Sự gia tốc (Hardware Acceleration)
575
của chúng sự sử dụng trong song song việc tính toán các kiến trúc cho hiệu quả ma trận các hoạt động (Kung 1982) (their use in parallel computing architectures for efficient matrix operations (Kung 1982)). Không giống
đa-mục đích sự thực thi các đơn vị, tâm thu các mảng khai thác không gian và thời gian tính cục bộ bằng cách việc tái sử dụng
các toán hạng như chúng lan truyền thông qua lưới (Unlike general-purpose execution units, systolic arrays exploit spatial and temporal locality by reusing operands as they propagate through the grid). Google của TPU làm ví dụ điển hình điều này thuộc về kiến trúc cách tiếp cận:
trong TPUv4, một 128×128 tâm thu mảng của nhân-tích lũy các đơn vị xử lý ma trận các hoạt động bằng cách
việc truyền phát dữ liệu thông qua mảng trong một được đường ống hóa cách thức (Jouppi et al. 2023) (Google’s TPU exemplifies this architectural approach: in the TPUv4, a 128×128 systolic array of multiply-accumulate units processes matrix operations by streaming data through the array in a pipelined manner (Jouppi et al. 2023)). Hình 11.8 theo sau
những dữ liệu các đường dẫn này: một kiểm soát đơn vị nuôi đầu vào các bộ đệm thứ mà truyền phát dữ liệu một cách ngang vào mảng, trong khi
từng phần các tổng mỗi tế bào sản xuất chảy một cách dọc xuống tới bộ tích lũy chuỗi ở đáy,
thứ mà thu thập hoàn thành các kết quả (Figure 11.8 follows these data paths: a control unit feeds input buffers that stream data horizontally into the array, while the partial sums each cell produces flow vertically down to the accumulator chain at the bottom, which collects the finished results). Mỗi việc xử lý phần tử thực hiện một nhân-tích lũy trên mỗi
chu kỳ và truyền của nó các toán hạng tới của nó các hàng xóm, vì vậy một giá trị được tải một lần được tái sử dụng qua một toàn bộ hàng
hoặc cột thay vì được tìm nạp lại từ bộ nhớ (Each processing element performs one multiply-accumulate per cycle and passes its operands to its neighbors, so a value loaded once is reused across an entire row or column rather than refetched from memory).
+
+
+
+
...
Hoàn thành (Done)
...
Kiểm soát (Control)
Dữ liệu (Data)
Từng phần Các tổng (Partial Sums)
Hình 11.8: Tâm thu Mảng Dữ liệu dòng: Một kiểm soát đơn vị nuôi đầu vào dữ liệu các luồng vào một lưới của việc xử lý các phần tử, mỗi cái
việc thực hiện nhân-tích lũy các hoạt động (Figure 11.8: Systolic Array Dataflow: A control unit feeds input data streams into a grid of processing elements, each performing multiply-accumulate operations). Dữ liệu chảy một cách ngang và một cách dọc thông qua mảng trong một được đường ống hóa cách thức,
việc tối đa hóa toán hạng sự tái sử dụng và việc tối thiểu hóa bộ nhớ truy cập, như được làm ví dụ điển hình bởi Google của TPUv4 (Data flows horizontally and vertically through the array in a pipelined manner, maximizing operand reuse and minimizing memory access, as exemplified by Google’s TPUv4).
11.4.7 Việc xếp ô gạch nguyên lý: Việc kết nối đồ thị và silicon (The tiling principle: Bridging graph and silicon)
Một cơ bản sự không khớp tồn tại giữa tính toán đồ thị (thứ mà nhìn thấy một đơn 4,096 × 4,096
ma trận phép nhân) và vật lý silicon (thứ mà sở hữu một cố định 128 × 128 tâm thu mảng) (A fundamental mismatch exists between the computational graph (which sees a single 4,096 × 4,096 matrix multiplication) and the physical silicon (which possesses a fixed 128 × 128 systolic array)).
Việc kết nối khoảng trống này yêu cầu việc xếp ô gạch: quá trình của việc phân vùng lớn tensor các hoạt động thành "các ô gạch" thứ mà
vừa chính xác vào phần cứng của nhanh cục bộ bộ nhớ (SRAM hoặc Scratchpad) (Bridging this gap requires tiling: the process of partitioning large tensor operations into “tiles” that fit exactly into the hardware’s fast local memory (SRAM or Scratchpad)).
Để xử lý của chúng ta 4,096-chiều rộng được làm việc-ví dụ lớp trên một 128-chiều rộng tâm thu mảng, trình biên dịch phải
phân rã hoạt động thành 1,024 cá nhân các ô gạch (To process our 4,096-wide worked-example layer on a 128-wide systolic array, the compiler must decompose the operation into 1,024 individual tiles). Điều này là không chỉ đơn thuần một phần mềm sự thuận tiện; nó
là một vật lý yêu cầu (This is not merely a software convenience; it is a physical requirement). Mỗi ô gạch được tìm nạp từ chậm HBM, "được tổ chức" trong nhanh SRAM, và sau đó
"được mạch đập" thông qua tâm thu mảng (Each tile is fetched from slow HBM, “staged” in fast SRAM, and then “pulsed” through the systolic array). Thuật toán 11.1 phát biểu vòng lặp tổ trình biên dịch phát ra cho điều này
sự phân rã: truyền phát các ô gạch của 𝐴 và 𝐵 trên chip và tích lũy của chúng tích thành một ô gạch của 𝐶 trước khi
việc ghi nó trở lại (Algorithm 11.1 states the loop nest a compiler emits for this decomposition: stream tiles of 𝐴and 𝐵on chip and accumulate their product into a tile of 𝐶before writing it back).
Các ô gạch các kích thước là đòn bẩy (The tile sizes are the lever). Một lớn hơn ô gạch tái sử dụng mỗi được tải byte qua nhiều hơn nhân-tích lũy
các hoạt động, việc nâng cao hạt nhân của số học cường độ và việc đẩy nó hướng tới bị ràng buộc-bởi-tính toán phía
của đường mái nhà; trần nhà là bao nhiêu của 𝐴, 𝐵, và 𝐶 vừa trong nhanh trên-chip bộ nhớ cùng một lúc (A larger tile reuses each loaded byte across more multiply-accumulate operations, raising the kernel’s arithmetic intensity and pushing it toward the compute-bound side of the roofline; the ceiling is how much of 𝐴, 𝐵, and 𝐶fits in fast on-chip memory at once). Này việc xếp ô gạch
mẫu là trung tâm cơ chế phía sau hiệu suất-cao ML các hệ thống (This tiling pattern is the central mechanism behind high-performance ML systems). Nó cho phép phần cứng để
duy trì cao hệ thống tính hiệu quả (𝜂hw) bằng cách việc đảm bảo rằng cho mọi byte được tải từ chính bộ nhớ,
dữ liệu được tái sử dụng 128× bên trong tâm thu lưới (It allows the hardware to maintain high system efficiency (𝜂hw) by ensuring that for every byte loaded from main memory, the data is reused 128× within the systolic grid). Một kỹ sư người mà hiểu việc xếp ô gạch hiểu
"silicon hợp đồng": nếu một lớp của các chiều không phải là các bội số của ô gạch kích thước (cho ví dụ, một chiều rộng
của 129 trên một 128 mảng), hệ thống trả một rìa thuế trong bị sử dụng dưới mức silicon, nơi 127 các đơn vị ngồi nhàn rỗi
trong khi một đơn vị hoàn thành "phần dư" ô gạch (An engineer who understands tiling understands the “silicon contract”: if a layer’s dimensions are not multiples of the tile size (for example, a width of 129 on a 128 array), the system pays a fringe tax in underutilized silicon, where 127 units sit idle while one unit finishes the “remainder” tile).

================ PAGE 614 ================

576
11.4 Tính toán Các đơn vị và Sự thực thi Các mô hình (Compute Units and Execution Models)
Một thêm chiều qua ô gạch
chiều rộng lật sự sử dụng khỏi một vách đá (One extra dimension past the tile width tips utilization off a cliff).
Thuật toán 11.1 (Algorithm 11.1) Được xếp ô gạch (được chia khối) ma trận phép nhân (Tiled (blocked) matrix multiply)
Yêu cầu (Require): 𝐴∈ℝ𝑀×𝐾, 𝐵∈ℝ𝐾×𝑁; ô gạch các kích thước 𝑇𝑀,𝑇𝑁,𝑇𝐾 (𝐴∈ℝ𝑀×𝐾, 𝐵∈ℝ𝐾×𝑁; tile sizes 𝑇𝑀,𝑇𝑁,𝑇𝐾)
Đảm bảo (Ensure): 𝐶= 𝐴𝐵 (𝐶= 𝐴𝐵)
1: for mỗi hàng ô gạch 𝑖0 (kích thước 𝑇𝑀) do (for each row tile 𝑖0 (size 𝑇𝑀) do)
2:
for mỗi cột ô gạch 𝑗0 (kích thước 𝑇𝑁) do (for each column tile 𝑗0 (size 𝑇𝑁) do)
3:
khởi tạo 𝐶-ô gạch bộ tích lũy tới không trên chip (initialize the 𝐶-tile accumulator to zero on chip)
4:
for mỗi 𝑘0 qua 𝐾 trong các bước của 𝑇𝐾 do (for each 𝑘0 over 𝐾in steps of 𝑇𝐾do)
5:
tải 𝐴-ô gạch [𝑖0,𝑘0] và 𝐵-ô gạch [𝑘0,𝑗0] trên chip (load 𝐴-tile [𝑖0,𝑘0] and 𝐵-tile [𝑘0,𝑗0] on chip)
6:
tích lũy ô gạch tích trên chip ▷tái sử dụng 𝑇𝑁/𝑇𝑀 trên mỗi byte (accumulate the tile product on chip ▷reuse 𝑇𝑁/𝑇𝑀per byte)
7:
end for
8:
ghi 𝐶-ô gạch trở lại tới bộ nhớ (write the 𝐶-tile back to memory)
9:
end for
10: end for
Tâm thu mảng kiến trúc đạt được tính toán tính hiệu quả thông qua được đồng bộ hóa dữ liệu
sự di chuyển qua một được cấu trúc lưới của việc xử lý các phần tử (The systolic array architecture achieves computational efficiency through synchronized data movement across a structured grid of processing elements). Tâm thu các mảng tổ chức sự tính toán
xung quanh bốn các thành phần (Systolic arrays organize computation around four components):
• Kiểm soát đơn vị (Control unit): Phối hợp thời gian và dữ liệu sự phân phối qua mảng, việc duy trì được đồng bộ
hóa hoạt động trong suốt tính toán lưới (Coordinates timing and data distribution across the array, maintaining synchronized operation throughout the computational grid).
• Dữ liệu các luồng (Data streams): Đầu vào các ma trận lan truyền thông qua được phối hợp các đường dẫn nơi ma trận A
các phần tử đi ngang một cách ngang trong khi ma trận B các phần tử chảy một cách dọc thông qua việc xử lý
lưới (Input matrices propagate through coordinated pathways where matrix A elements traverse horizontally while matrix B elements flow vertically through the processing grid).
• Việc xử lý phần tử lưới (Processing element grid): Cá nhân việc xử lý các phần tử thực thi nhân-tích lũy các hoạt
động trên việc truyền phát dữ liệu, việc tạo ra từng phần các kết quả thứ mà tích lũy hướng tới cuối cùng sự tính
toán (Individual processing elements execute multiply-accumulate operations on streaming data, generating partial results that accumulate toward the final computation).
• Đầu ra sự thu thập (Output collection): Các kết quả tập hợp ở được chỉ định đầu ra các ranh giới nơi được tích lũy
từng phần các tổng tạo thành hoàn chỉnh ma trận các phần tử (Results aggregate at designated output boundaries where accumulated partial sums form complete matrix elements).
Các hệ thống Phối cảnh 11.1 (Systems Perspective 11.1): Việc nối khớp kiến trúc tới khối lượng công việc (Matching architecture to workload)
Các kiến trúc sư của tình thế tiến thoái lưỡng nan: Tâm thu các mảng phải chọn cái nào dữ liệu để giữ tĩnh (trong các thanh ghi)
để tối thiểu hóa sự di chuyển (The architects’ dilemma: Systolic arrays must choose which data to keep stationary (in registers) to minimize movement). Sự lựa chọn này mã hóa cứng phần cứng của sự ưa thích cho nhất định mô hình
các loại (This choice hard-codes the hardware’s preference for certain model types). Bảng 11.5 xem trước ba tĩnh-toán hạng các chiến lược và các khối lượng công việc mỗi cái
thiên vị; phần 11.8 phát triển mỗi cái trong đầy đủ như một chung việc ánh xạ quyết định (Table 11.5 previews the three stationary-operand strategies and the workloads each favors; section 11.8 develops each one in full as a general mapping decision).
Bảng 11.5: Tâm thu-Mảng Dữ liệu dòng Các chiến lược: Ba tĩnh-toán hạng các lựa chọn cho tâm thu các mảng, tái sử dụng mẫu
mỗi cái tối đa hóa, và khối lượng công việc lớp thứ mà hưởng lợi, việc hiển thị cách nào một cố định dữ liệu dòng lựa chọn mã hóa cứng một máy gia tốc của
sự ái lực cho cụ thể các mô hình (Table 11.5: Systolic-Array Dataflow Strategies: Three stationary-operand choices for systolic arrays, the reuse pattern each maximizes, and the workload class that benefits, showing how a fixed dataflow choice hard-codes an accelerator’s affinity for specific models).
Chiến lược (Strategy)
Tĩnh Mục (Stationary Item)
Được tối ưu hóa Cho (Optimized For)
Ví dụ Khối lượng công việc (Example Workload)
Trọng số-Tĩnh (Weight-Stationary)
Các trọng số (𝑊) (Weights (𝑊))
Cao Sự tái sử dụng của
Các trọng số (High Reuse of Weights)
Các CNN (Conv2D): Các bộ lọc là nhỏ và được tái sử dụng
qua toàn bộ hình ảnh (CNNs (Conv2D): Filters are small and reused across the entire image).
Đầu ra-Tĩnh (Output-Stationary)
Từng phần Các tổng (𝐶) (Partial Sums (𝐶))
Cao Sự tái sử dụng của
Các bộ tích lũy (High Reuse of Accumulators)
Lớn Lô MatMul: Việc tích lũy các kết quả cho
nhiều các đầu vào chống lại một lớn trọng số ma trận (Large Batch MatMul: Accumulating results for many inputs against a large weight matrix).
Đầu vào-Tĩnh (Input-Stationary)
Các đầu vào (𝐴) (Inputs (𝐴))
Cao Sự tái sử dụng của
Các sự kích hoạt (High Reuse of Activations)
Các Transformer: Cùng các sự kích hoạt nuôi nhiều
trọng số các ma trận qua sự chú ý các đầu (Transformers: The same activations feed many weight matrices across attention heads).
Không có "hoàn hảo" máy gia tốc (There is no “perfect” accelerator). Một chip được tối ưu hóa cho Trọng số-Tĩnh dòng (giống như đầu các TPU)
xuất sắc ở các CNN nơi các bộ lọc là nhỏ và một cách nặng nề được tái sử dụng, nhưng đối mặt các thách thức với LLM
sự suy luận ở nhỏ lô các kích thước, nơi trọng số ma trận được đọc một lần trên mỗi token với tối thiểu
sự tái sử dụng, việc đẩy các kiến trúc hướng tới đầu ra-tĩnh hoặc lai dữ liệu dòng các mẫu (A chip optimized for Weight-Stationary flow (like early TPUs) excels at CNNs where filters are small and heavily reused, but faces challenges with LLM inference at small batch sizes, where the weight matrix is read once per token with minimal reuse, pushing architectures toward output-stationary or hybrid dataflow patterns).

================ PAGE 615 ================

11. Phần cứng Sự gia tốc (Hardware Acceleration)
577
Bởi vì tâm thu các mảng về mặt vật lý cố định cách nào dữ liệu chảy thông qua lưới, các nhà thiết kế phải quyết định
cái nào toán hạng để giữ tĩnh, một sự lựa chọn thứ mà một cách vĩnh viễn định hình phần cứng của sự ái lực cho
nhất định các khối lượng công việc (Because systolic arrays physically fix how data flows through the grid, designers must decide which operand to keep stationary, a choice that permanently shapes the hardware’s affinity for certain workloads). Điều này là không chỉ đơn thuần một sự triển khai chi tiết mà là một vĩnh viễn thuộc về kiến trúc
sự cam kết: quyết định được tạo ra ở chip thiết kế thời gian xác định cái nào thần kinh mạng các hoạt động
sẽ đạt được cao sự sử dụng và cái nào sẽ bị chết đói cho dữ liệu (This is not merely an implementation detail but a permanent architectural commitment: the decision made at chip design time determines which neural network operations will achieve high utilization and which will be starved for data).
Được đồng bộ hóa dữ liệu dòng đảm bảo rằng ma trận phần tử 𝐴[𝑖,𝑘] bắt gặp tương ứng 𝐵[𝑘,𝑗]
các phần tử ở chính xác thuộc về thời gian các khoảng thời gian, việc thực thi nhân-tích lũy các hoạt động được yêu cầu
cho ma trận phép nhân 𝐶[𝑖,𝑗] = ∑𝑘𝐴[𝑖,𝑘] × 𝐵[𝑘,𝑗] (The synchronized data flow ensures that matrix element 𝐴[𝑖,𝑘] encounters corresponding 𝐵[𝑘,𝑗] elements at precise temporal intervals, executing the multiply-accumulate operations required for matrix multiplication 𝐶[𝑖,𝑗] = ∑𝑘𝐴[𝑖,𝑘] × 𝐵[𝑘,𝑗]). Này có hệ thống sự tái sử dụng của các toán hạng qua
nhiều việc xử lý các phần tử một cách đáng kể làm giảm bớt bộ nhớ băng thông các yêu cầu bằng cách việc loại bỏ
dư thừa dữ liệu các lượt tìm nạp từ bên ngoài bộ nhớ các hệ thống con (This systematic reuse of operands across multiple processing elements substantially reduces memory bandwidth requirements by eliminating redundant data fetches from external memory subsystems).
Xem xét phép nhân của 2×2 các ma trận A và B bên trong một tâm thu mảng (Consider the multiplication of 2×2 matrices A and B within a systolic array). Trong suốt đầu tiên
tính toán chu kỳ, phần tử 𝐴[0,0] = 2 lan truyền một cách ngang trong khi 𝐵[0,0] = 1 di chuyển một cách dọc,
việc hội tụ ở việc xử lý phần tử PE(0,0) để thực thi phép nhân 2×1 = 2 (During the first computational cycle, element 𝐴[0,0] = 2 propagates horizontally while 𝐵[0,0] = 1 moves vertically, converging at processing element PE(0,0) to execute the multiplication 2×1 = 2). Trong tiếp theo
chu kỳ, cùng 𝐴[0,0] = 2 tiến tới PE(0,1) nơi nó bắt gặp 𝐵[0,1] = 3, việc tính toán 2×3 = 6 (In the subsequent cycle, the same 𝐴[0,0] = 2 advances to PE(0,1) where it encounters 𝐵[0,1] = 3, computing 2×3 = 6).
Đồng thời, 𝐴[0,1] = 4 đi vào PE(0,0) để tham gia với tiếp theo B ma trận phần tử (Concurrently, 𝐴[0,1] = 4 enters PE(0,0) to engage with the next B matrix element). Điều này được phối hợp
dữ liệu sự di chuyển cho phép có hệ thống toán hạng sự tái sử dụng qua nhiều tính toán các hoạt động, việc loại bỏ
dư thừa bộ nhớ các truy cập và việc làm ví dụ điển hình tính hiệu quả nguyên lý nằm bên dưới tâm thu
mảng các kiến trúc (This coordinated data movement enables systematic operand reuse across multiple computational operations, eliminating redundant memory accesses and exemplifying the efficiency principle underlying systolic array architectures).
Mỗi việc xử lý phần tử trong mảng thực hiện một nhân-tích lũy hoạt động trong mọi chu kỳ (Each processing element in the array performs a multiply-accumulate operation in every cycle). Trong
cấu hình được hiển thị ở đây (việc khớp với trước ví dụ, nơi ma trận 𝐴 chảy một cách ngang
và 𝐵 chảy một cách dọc) (In the configuration shown here (matching the preceding example, where matrix 𝐴flows horizontally and 𝐵flows vertically)):
1. Nhận một trọng số giá trị từ bên trái (𝐴 ma trận, việc chảy một cách ngang) (Receives a weight value from the left (the 𝐴matrix, flowing horizontally))
2. Nhận một đầu vào sự kích hoạt từ bên trên (𝐵 ma trận, việc chảy một cách dọc) (Receives an input activation from above (the 𝐵matrix, flowing vertically))
3. Nhân những các giá trị này và cộng tới của nó đang chạy tổng (Multiplies these values and adds to its running sum)
4. Truyền trọng số giá trị về phía phải và đầu vào sự kích hoạt về phía dưới tới lân cận các phần tử (Passes the weight value rightward and the input activation downward to neighboring elements)
Thực tế dữ liệu dòng các hướng thay đổi qua các sự triển khai; một số kiến trúc đảo ngược những vai trò này
hoặc sử dụng trọng số-tĩnh các cấu hình nơi các trọng số được tải trước thay vì được truyền phát (Actual data flow directions vary across implementations; some architectures reverse these roles or use weight-stationary configurations where weights are preloaded rather than streamed).
Điều này được cấu trúc sự tính toán mô hình tối thiểu hóa dữ liệu sự di chuyển giữa toàn cầu bộ nhớ và
việc xử lý các phần tử, việc cải thiện cả hai tính hiệu quả và tính có thể chia tỷ lệ (This structured computation model minimizes data movement between global memory and processing elements, improving both efficiency and scalability). Như tâm thu các mảng hoạt động trong một
việc truyền phát phong cách, chúng là đặc biệt hiệu quả cho cao-thông lượng các khối lượng công việc chẳng hạn như sâu
sự học hỏi sự đào tạo và sự suy luận (As systolic arrays operate in a streaming fashion, they are particularly effective for high-throughput workloads such as deep learning training and inference).
Trong khi hình 11.8 nắm bắt cốt lõi dữ liệu dòng nguyên lý, tâm thu các kiến trúc thay đổi một cách đáng kể
qua khác nhau máy gia tốc các thiết kế trong thực tế (While figure 11.8 captures the core dataflow principle, systolic architectures vary significantly across different accelerator designs in practice). Sự đào tạo-tập trung các kiến trúc giống như Google của TPU sử dụng
lớn các mảng (128×128 hoặc lớn hơn) được tối ưu hóa cho cao tính toán thông lượng, trong khi sự suy luận-
định hướng các thiết kế được tìm thấy trong biên các thiết bị ưu tiên năng lượng tính hiệu quả với nhỏ hơn các cấu hình (8×8
tới 32×32) (Training-focused architectures like Google’s TPU employ large arrays (128×128 or larger) optimized for high computational throughput, while inference-oriented designs found in edge devices prioritize energy efficiency with smaller configurations (8×8 to 32×32)).
Nằm bên dưới nguyên lý duy trì nhất quán: dữ liệu chảy một cách có hệ thống thông qua việc xử lý các phần
tử, với các đầu vào việc di chuyển một cách ngang và một cách dọc để tính toán từng phần các tổng trong một được đồng bộ hóa
cách thức (The underlying principle remains consistent: data flows systematically through processing elements, with inputs moving horizontally and vertically to compute partial sums in a synchronized fashion). Tuy nhiên, như được chi tiết trong phần 11.5.1, thực tế tính hiệu quả bị cuối cùng ràng buộc bởi
bộ nhớ băng thông các nút thắt cổ chai (However, as detailed in section 11.5.1, practical effectiveness is ultimately constrained by memory bandwidth bottlenecks).
Một 128 × 128 tâm thu mảng có khả năng của 16,384 các hoạt động trên mỗi chu kỳ yêu cầu liên tục dữ liệu việc nuôi để
duy trì sự sử dụng (A 128 × 128 systolic array capable of 16,384 operations per cycle requires continuous data feed to maintain utilization). Mỗi chu kỳ đòi hỏi tươi đầu vào các sự kích hoạt và trọng số các tham số thứ mà phải
đi ngang từ ngoài-chip bộ nhớ thông qua trên-chip các bộ đệm tới mảng các rìa (Each cycle demands fresh input activations and weight parameters that must traverse from off-chip memory through on-chip buffers to the array edges). TPU v4 của 1,200 GB/s
HBM2 băng thông cho phép cao sự sử dụng, nhưng thậm chí này đáng kể băng thông trở nên việc giới hạn
khi việc xử lý lớn transformer các mô hình nơi bộ nhớ các yêu cầu vượt quá trên-chip khả năng (The TPU v4’s 1,200 GB/s HBM2 bandwidth enables high utilization, but even this substantial bandwidth becomes limiting when processing large transformer models where memory requirements exceed on-chip capacity).
Các lượng tử hóa kỹ thuật trong phần 10.4 làm giảm bớt mô hình bộ nhớ dấu chân bằng cách việc chuyển đổi FP32
các trọng số tới INT8 các sự biểu diễn (The quantization techniques in section 10.4 reduce model memory footprint by converting FP32 weights to INT8 representations). Sự tối ưu hóa này một cách trực tiếp giải quyết bộ nhớ băng thông
các sự ràng buộc được xác định ở đây (This optimization directly addresses the memory bandwidth constraints identified here). Việc chuyển đổi 32-bit dấu phẩy-động các trọng số tới 8-bit các số nguyên có thể làm giảm bớt
trọng số lưu lượng bởi 4×; liệu điều đó thay đổi một hạt nhân từ bị ràng buộc băng thông tới bị ràng buộc tính toán
phụ thuộc trên hoạt động của ban đầu số học cường độ, máy gia tốc của INT8 đỉnh điểm (the ridge point) (
cường độ ngưỡng ở cái mà của nó INT8 tính toán bão hòa), và chi phí chung của sự lượng tử hóa và
sự giải lượng tử hóa (Converting 32-bit floating-point weights to 8-bit integers can reduce weight traffic by 4×; whether that changes a kernel from bandwidth bound to compute bound depends on the operation’s original arithmetic intensity, the accelerator’s INT8 ridge point (the intensity threshold at which its INT8 compute saturates), and the overhead of quantization and dequantization). Tương tự, được cấu trúc việc cắt tỉa loại bỏ toàn bộ các hàng hoặc các cột của trọng số các ma trận,
việc làm giảm bớt cả hai dữ liệu thể tích thứ mà phải đi ngang bộ nhớ các hệ thống phân cấp và sự tính toán được yêu cầu (Similarly, structured pruning removes entire rows or columns of weight matrices, reducing both the data volume that must traverse memory hierarchies and the computation required).

================ PAGE 616 ================

578
11.4 Tính toán Các đơn vị và Sự thực thi Các mô hình (Compute Units and Execution Models)
Những thuật toán các sự tối ưu hóa này chứng minh có giá trị chính xác bởi vì chúng mục tiêu bộ nhớ nút thắt cổ chai
thứ mà giới hạn máy gia tốc hiệu suất trong thực tế (These algorithmic optimizations prove valuable precisely because they target the memory bottleneck that limits accelerator performance in practice).
11.4.8 Kỹ thuật số (Numerics) trong AI sự gia tốc (Numerics in AI acceleration)
Tâm thu các mảng và tensor các lõi đạt được của chúng tính hiệu quả một phần thông qua chuyên biệt sự hỗ trợ cho
được làm giảm bớt-độ chính xác số học (Systolic arrays and tensor cores achieve their efficiency partly through specialized support for reduced-precision arithmetic). Này sự kết nối là trực tiếp: 2× phần tăng tốc từ FP16 so với FP32 là không
chỉ đơn thuần "việc sử dụng ít hơn các bit" mà phản ánh rằng các máy gia tốc về mặt vật lý đóng gói 2× nhiều hơn FP16 nhân-
tích lũy các đơn vị vào cùng silicon diện tích (This connection is direct: the 2× speedup from FP16 vs. FP32 is not merely “using fewer bits” but reflects that accelerators physically pack 2× more FP16 multiply-accumulate units into the same silicon area). Việc xây dựng trên sự lượng tử hóa và hỗn hợp-độ chính xác
các kỹ thuật được thiết lập trong Chương 10, được làm giảm bớt độ chính xác trở thành một phần cứng thiết kế quyết định:
thuộc về số định dạng xác định sự cân bằng giữa độ chính xác, thông lượng, năng lượng sự tiêu thụ, và
dữ liệu sự di chuyển qua SIMD và SIMT các đơn vị, tensor các lõi, và tâm thu các mảng (Building on the quantization and mixed-precision techniques established in Chapter 10, reduced precision becomes a hardware design decision: the numerical format determines the balance among accuracy, throughput, energy consumption, and data movement across SIMD and SIMT units, tensor cores, and systolic arrays).
11.4.8.1 Độ chính xác các sự đánh đổi (Precision trade-offs)
Thấp hơn độ chính xác là không miễn phí: mỗi bước xuống, từ FP32 tới FP16 tới INT8, đánh đổi động phạm vi và
định trị (mantissa) các bit cho thông lượng và băng thông các lợi ích vừa được mô tả (Lower precision is not free: each step down, from FP32 to FP16 to INT8, trades dynamic range and mantissa bits for the throughput and bandwidth gains just described). Phần cứng các kiến trúc sư cân bằng
đó sự đánh đổi khi việc thiết kế máy gia tốc các đường dẫn dữ liệu (Hardware architects balance that trade-off when designing accelerator datapaths).
Sự tiến hóa của AI phần cứng phản ánh điều này sự đồng-thiết kế giữa phần mềm sự tối ưu hóa và phần
cứng khả năng (The evolution of AI hardware reflects this co-design between software optimization and hardware capability). Đầu GPU các kiến trúc đã hỗ trợ chỉ FP32 cho sâu sự học hỏi các khối lượng công việc, nhưng
độ chính xác-sự giảm bớt các chiến lược trong phần 10.4.4 đã hiển thị rằng được làm giảm bớt độ chính xác có thể duy trì
mô hình độ chính xác, vì vậy phần cứng các nhà cung cấp đã phản hồi bằng cách việc thêm bản địa sự hỗ trợ cho FP16, BF16, và
số nguyên các định dạng (Early GPU architectures supported only FP32 for deep learning workloads, but the precision-reduction strategies in section 10.4.4 showed that reduced precision could maintain model accuracy, so hardware vendors responded by adding native support for FP16, BF16, and integer formats). Điều này phần cứng sự tiến hóa cho phép phần mềm các sự tối ưu hóa để dịch một cách trực tiếp thành
hiệu suất các lợi ích, như được làm giảm bớt-độ chính xác các hoạt động thực thi trên được cống hiến các mạch được tối ưu hóa cho
những cụ thể các định dạng đó (This hardware evolution enables software optimizations to translate directly into performance gains, as reduced-precision operations execute on dedicated circuits optimized for those specific formats).
Sự chuyển đổi từ cao-độ chính xác tới thấp hơn-độ chính xác các định dạng là một cách sâu sắc được tích hợp vào phần cứng
sự thực thi các mô hình (The transition from high-precision to lower-precision formats is deeply integrated into hardware execution models). Như được chi tiết trong phần 11.4.2, SIMD và SIMT các đơn vị cung cấp linh hoạt sự hỗ trợ cho
nhiều các độ chính xác (As detailed in section 11.4.2, SIMD and SIMT units provide flexible support for multiple precisions). Tensor các lõi (phần 11.4.3) tăng tốc sự tính toán việc sử dụng được làm giảm bớt-độ chính xác
số học, trong khi tâm thu các mảng (phần 11.4.6) tối ưu hóa hiệu suất bằng cách việc tối thiểu hóa bộ nhớ
băng thông các sự ràng buộc thông qua thấp-độ chính xác các định dạng thứ mà tối đa hóa toán hạng sự tái sử dụng (Tensor cores (section 11.4.3) accelerate computation using reduced-precision arithmetic, while systolic arrays (section 11.4.6) optimize performance by minimizing memory bandwidth constraints through low-precision formats that maximize operand reuse).
Mặc dù các lợi thế của được làm giảm bớt độ chính xác, sâu sự học hỏi các mô hình không thể luôn luôn dựa duy nhất
trên thấp-bit các sự biểu diễn (Despite the advantages of reduced precision, deep learning models cannot always rely solely on low-bit representations). Để giải quyết này thách thức, hiện đại AI các máy gia tốc triển khai hỗn hợp-
độ chính xác việc tính toán, nơi khác nhau thuộc về số các định dạng được sử dụng ở khác nhau các giai đoạn của sự thực thi (To address this challenge, modern AI accelerators implement mixed-precision computing, where different numerical formats are used at different stages of execution).
Những độ chính xác các lựa chọn này ảnh hưởng thuộc về số độ tin cậy: ma trận các phép nhân có thể được thực hiện trong FP16
hoặc BF16, trong khi các sự tích lũy được duy trì trong FP32 để ngăn chặn độ chính xác sự mất mát (These precision choices affect numerical reliability: matrix multiplications may be performed in FP16 or BF16, while accumulations are maintained in FP32 to prevent precision loss). Tương tự, sự suy luận
các động cơ sử dụng INT8 số học trong khi việc bảo tồn chính các sự kích hoạt trong cao hơn độ chính xác khi cần thiết (Similarly, inference engines use INT8 arithmetic while preserving key activations in higher precision when necessary).
11.4.8.2 Hỗn hợp-độ chính xác việc tính toán (Mixed-precision computing)
Hiện đại AI các máy gia tốc ngày càng hỗ trợ hỗn hợp-độ chính xác sự thực thi, việc cho phép khác nhau thuộc về số
các định dạng để được sử dụng ở đa dạng các giai đoạn của sự tính toán (Modern AI accelerators increasingly support mixed-precision execution, allowing different numerical formats to be used at various stages of computation). Sự đào tạo các khối lượng công việc thường sử dụng FP16 hoặc BF16 cho
ma trận các phép nhân, trong khi việc duy trì FP32 các sự tích lũy để bảo tồn độ chính xác (Micikevicius
et al. 2017; Mellempudi et al. 2019) (Training workloads often use FP16 or BF16 for matrix multiplications, while maintaining FP32 accumulations to preserve precision (Micikevicius et al. 2017; Mellempudi et al. 2019)). Phần mềm sự triển khai của hỗn hợp-độ chính xác sự đào tạo,
bao gồm mất mát sự chia tỷ lệ các kỹ thuật và framework sự hỗ trợ, được bao phủ trong phần 8.6.3 (The software implementation of mixed-precision training, including loss scaling techniques and framework support, is covered in section 8.6.3). Sự suy luận
các khối lượng công việc, ngược lại, tối ưu hóa cho INT8 hoặc thậm chí INT4, việc đạt được cao tính hiệu quả trong khi việc giữ lại
có thể chấp nhận độ chính xác (Inference workloads, by contrast, optimize for INT8 or even INT4, achieving high efficiency while retaining acceptable accuracy).
Sự dịch chuyển hướng tới độ chính xác tính đa dạng là rõ ràng trong sự tiến hóa của AI phần cứng (The shift toward precision diversity is evident in the evolution of AI hardware). Đầu các kiến trúc
chẳng hạn như NVIDIA Volta đã cung cấp giới hạn sự hỗ trợ cho thấp hơn độ chính xác vượt ra ngoài FP16, trong khi sau này
các kiến trúc, bao gồm Turing và Ampere, đã mở rộng phạm vi của được hỗ trợ các định dạng (Early architectures such as NVIDIA Volta provided limited support for lower precision beyond FP16, whereas later architectures, including Turing and Ampere, expanded the range of supported formats). Bảng 11.6
theo dõi này sự tiến triển: Ampere các GPU đã giới thiệu TF32 như một con lai giữa FP32 và FP16 (NVIDIA
2020b), cùng với rộng hơn sự hỗ trợ cho BF16, INT8, và INT4 (NVIDIA Corporation 2017, 2018, 2020) (Table 11.6 traces this progression: Ampere GPUs introduced TF32 as a hybrid between FP32 and FP16 (NVIDIA 2020b), alongside broader support for BF16, INT8, and INT4 (NVIDIA Corporation 2017, 2018, 2020)).
Mới hơn các kiến trúc kết hợp một đang phát triển tính đa dạng của thuộc về số các định dạng bởi vì khác nhau
các khối lượng công việc ràng buộc ở khác nhau các điểm trên độ chính xác-thông lượng-năng lượng sự đánh đổi (Newer architectures incorporate a growing diversity of numerical formats because different workloads bind at different points on the accuracy-throughput-energy trade-off). Độ chính xác sự hỗ trợ
là do đó một cái khác hình thức của khối lượng công việc sự nối khớp, không một chung tính năng danh sách kiểm tra (Precision support is therefore another form of workload matching, not a generic feature checklist).
Độ chính xác định dạng được sử dụng trong phần cứng thiết kế có xếp tầng các hệ quả qua toàn bộ hệ thống (The precision format used in hardware design has cascading implications across the entire system).
Việc làm giảm bớt từ FP32 tới FP16 cắt bộ nhớ lưu lượng làm một nửa, thứ mà quan trọng nhiều hơn nó có thể dường như:
bởi vì bộ nhớ truy cập thống trị năng lượng sự tiêu thụ, việc chia đôi bộ nhớ lưu lượng có thể một cách đáng kể
làm giảm bớt năng lượng trên mỗi sự suy luận khi dữ liệu sự di chuyển là nút thắt cổ chai (Horowitz 2014) (Reducing from FP32 to FP16 cuts memory traffic in half, which matters far more than it might seem: because memory access dominates energy consumption, halving memory traffic can substantially reduce energy per inference when data movement is the bottleneck (Horowitz 2014)). Đồng thời,

================ PAGE 617 ================

11. Phần cứng Sự gia tốc (Hardware Acceleration)
579
tensor các lõi và tâm thu các mảng có thể đóng gói nhiều hơn được làm giảm bớt-độ chính xác nhân-tích lũy các đơn vị vào
cùng silicon diện tích, việc nâng cao đỉnh thông lượng (Dally et al. 2021; Dally 2023) (tensor cores and systolic arrays can pack more lower-precision multiply-accumulate units into the same silicon area, raising peak throughput (Dally et al. 2021; Dally 2023)). Số nguyên các định dạng đẩy điều này
xa hơn—INT8 số học yêu cầu xấp xỉ 30× ít hơn năng lượng so với FP32 trên mỗi hoạt động, thứ mà là tại sao
sự suy luận-tập trung các máy gia tốc giống như TPUv1 đã được xây dựng xung quanh INT8 từ đầu (Jouppi et al. 2017) (Integer formats push this further—INT8 arithmetic requires roughly 30× less energy than FP32 per operation, which is why inference-focused accelerators like the TPUv1 were built around INT8 from the start (Jouppi et al. 2017)). Các hệ thống sự thấu hiểu là rằng được làm giảm bớt độ chính xác không chỉ đơn thuần "cứu các bit": nó đồng thời
làm giảm bớt bộ nhớ băng thông nút thắt cổ chai và tăng tính toán mật độ, việc tấn công cả hai phía của
đường mái nhà cùng một lúc (The systems insight is that reduced precision does not merely “save bits”: it simultaneously relieves the memory bandwidth bottleneck and increases compute density, attacking both sides of the roofline at once).
Bảng 11.6: Độ chính xác Sự hỗ trợ Sự tiến hóa: GPU các kiến trúc dần dần đã mở rộng sự hỗ trợ cho thấp hơn-độ chính xác dữ liệu các loại,
việc cho phép hiệu suất các lợi ích và tính hiệu quả các sự cải thiện trong AI các khối lượng công việc (Table 11.6: Precision Support Evolution: GPU architectures progressively expanded support for lower-precision data types, enabling performance gains and efficiency improvements in AI workloads). Đầu các kiến trúc chủ yếu đã sử dụng FP32, trong khi sau này
các thế hệ đã kết hợp FP16, BF16, INT8, và INT4 để tăng tốc cả hai sự đào tạo và sự suy luận các nhiệm vụ (Early architectures primarily used FP32, while later generations incorporated FP16, BF16, INT8, and INT4 to accelerate both training and inference tasks).
Kiến trúc (Architecture)
Năm (Year)
Được hỗ trợ Tensor Lõi Các độ chính xác (Supported Tensor Core Precisions)
Được hỗ trợ CUDA Lõi Các độ chính xác (Supported CUDA Core Precisions)
Volta
2017
FP16
FP64, FP32, FP16
Turing
2018
FP16, INT8, INT4, INT1
FP64, FP32, FP16, INT8
Ampere
2020
FP64, TF32, BF16, FP16, INT8, INT4
FP64, FP32, FP16, BF16, INT8
Như AI các mô hình tiếp tục để chia tỷ lệ, độ chính xác sự hỗ trợ kết nối tính toán nguyên thủy cuộc thảo luận
trở lại tới bộ nhớ bức tường: thấp hơn-bit các định dạng quan trọng khi chúng làm giảm bớt các byte được di chuyển và giữ
phần cứng của ma trận các động cơ được nuôi (As AI models continue to scale, precision support connects the compute primitive discussion back to the memory wall: lower-bit formats matter when they reduce the bytes moved and keep the hardware’s matrix engines fed). Còn lại thuộc về kiến trúc câu hỏi là cách nào những sự thực thi
các đơn vị này, độ chính xác các định dạng, và bộ nhớ các đường dẫn tích hợp vào hoàn chỉnh máy gia tốc các hệ thống (The remaining architectural question is how these execution units, precision formats, and memory paths integrate into complete accelerator systems). Thuộc về kiến
trúc sự tích hợp xác định cách nào một cách hiệu quả tính toán các nguyên thủy trở thành có thể sử dụng máy gia tốc
thông lượng (Architectural integration determines how efficiently computational primitives become usable accelerator throughput). SIMD các làn, tensor các lõi, và tâm thu các mảng là các khối xây dựng, nhưng của chúng toàn-chip
sự tổ chức thay đổi một cách đáng kể qua AI các bộ xử lý; sự lựa chọn của sự thực thi các đơn vị, của chúng thuộc về số
độ chính xác sự hỗ trợ, và của chúng tính kết nối định hình cách nào một cách hiệu quả phần cứng có thể chia tỷ lệ cho sâu sự học hỏi
các khối lượng công việc (SIMD lanes, tensor cores, and systolic arrays are building blocks, but their full-chip organization varies significantly across AI processors; the choice of execution units, their numerical precision support, and their connectivity shape how effectively hardware can scale for deep learning workloads).
11.4.9 Nội-nút các kết nối liên thông: Việc chia tỷ lệ ngăn xếp (Intra-node interconnects: Scaling the stack)
Sự thành thạo của đơn-máy ngăn xếp yêu cầu việc hiểu cách nào các bit di chuyển giữa các GPU và
CPU (Mastery of the single-machine stack requires understanding how bits move between GPUs and the CPU). Trong 1–8 GPU chế độ, sự chia tỷ lệ được đạt được thông qua cao-tốc độ nội-nút các kết nối liên thông
chẳng hạn như NVLink và máy lưu trữ-tới-thiết bị PCIe các sự truyền tải thứ mà làm nhẹ bộ nhớ bức tường (In the 1–8 GPU regime, scaling is achieved through high-speed intra-node interconnects such as NVLink and host-to-device PCIe transfers that mitigate the memory wall). Những các liên kết này tạo thành
một băng thông dạng côn: dữ liệu-sự di chuyển tốc độ rơi ở mỗi bước xa từ tính toán các đơn vị, từ
trên-gói HBM thông qua GPU-tới-GPU NVLink cầu nối xuống tới máy lưu trữ PCIe liên kết (These links form a bandwidth taper: data-movement speed falls at each step away from the compute units, from on-package HBM through the GPU-to-GPU NVLink bridge down to the host PCIe link). PCIe
bước là chậm hơn nhiều so với máy gia tốc-cục bộ bộ nhớ và liên-GPU vải, vì vậy bất kỳ dữ liệu đường dẫn thứ mà
chạm CPU có thể trở thành một hiệu suất mối nguy hiểm, "PCIe Bức tường" thứ mà NVLink tồn tại để tránh
(C. NVIDIA 2020) (The PCIe step is much slower than the accelerator-local memory and inter-GPU fabric, so any data path that touches the CPU can become a performance hazard, the “PCIe Wall” that NVLink exists to avoid (C. NVIDIA 2020)). Phần 11.5.5.1 phát triển này hệ thống phân cấp một cách định lượng, nơi máy lưu trữ-máy gia tốc
sự giao tiếp là mang tính hoạt động mối quan tâm (Section 11.5.5.1 develops this hierarchy quantitatively, where host-accelerator communication is the operative concern).
Hiện đại AI các bộ xử lý trưng bày một phạm vi của thiết kế các sự đánh đổi dựa trên của chúng dự định các ứng dụng, và
việc so sánh của chúng các cấu hình tiết lộ cách nào sự triển khai các sự ràng buộc dẫn dắt thuộc về kiến trúc sự phân kỳ (Modern AI processors exhibit a range of design trade-offs based on their intended applications, and comparing their configurations reveals how deployment constraints drive architectural divergence).
Một sự đào tạo-được tối ưu hóa máy gia tốc giống như NVIDIA A100 đóng gói nhiều Việc truyền phát Đa bộ xử lý
với rộng SIMD các đơn vị và FP16 tensor các lõi bởi vì sự đào tạo thông lượng chia tỷ lệ với tổng hợp
nhân-tích lũy khả năng (NVIDIA Corporation 2020) (A training-optimized accelerator like the NVIDIA A100 packs many Streaming Multiprocessors with wide SIMD units and FP16 tensor cores because training throughput scales with aggregate multiply-accumulate capacity (NVIDIA Corporation 2020)). Google của TPUv4 tạo ra một một cách triệt để
khác biệt vụ cá cược: chỉ hai các lõi trên mỗi chip, mỗi cái việc chứa khổng lồ BF16 tâm thu các mảng, một thiết kế thứ mà
đánh đổi lập trình viên tính linh hoạt cho tính hiệu quả trên dày đặc ma trận các phép nhân (Jouppi et al. 2023) (Google’s TPUv4 makes a radically different bet: just two cores per chip, each containing massive BF16 systolic arrays, a design that trades programmer flexibility for efficiency on dense matrix multiplications (Jouppi et al. 2023)).
Ở sự suy luận cuối, Intel của Sapphire Rapids cống hiến Tiên tiến Ma trận Các phần mở rộng (AMX) ô gạch
các động cơ tới INT8 và BF16, việc phản ánh sự thấu hiểu từ Chương 10 rằng sự suy luận các mô hình dung thứ
được làm giảm bớt độ chính xác (Intel Corporation 2021a) (At the inference end, Intel’s Sapphire Rapids dedicates Advanced Matrix Extensions (AMX) tile engines to INT8 and BF16, reflecting the insight from Chapter 10 that inference models tolerate reduced precision (Intel Corporation 2021a)). Di động thần kinh các động cơ lấy điều này xa hơn bằng cách việc thu nhỏ
ma trận các động cơ thành thấp-năng lượng SoC các khối, việc ưu tiên năng lượng tính hiệu quả trên mỗi hoạt động qua đỉnh
thông lượng (Mobile neural engines take this further by shrinking matrix engines into low-power SoC blocks, prioritizing energy efficiency per operation over peak throughput). Bảng 11.7 so sánh những thuộc về kiến trúc các cấu hình này (Table 11.7 compares these architectural configurations).
Mẫu qua những các cấu hình này tiết lộ một nhất quán kỹ thuật nguyên lý: mỗi thiết kế
hy sinh tính tổng quát để tối ưu hóa cho của nó mục tiêu khối lượng công việc của thống trị hoạt động và độ chính xác (The pattern across these configurations reveals a consistent engineering principle: each design sacrifices generality to optimize for its target workload’s dominant operation and precision). Sự đào tạo
các chip đầu tư silicon trong rộng dấu phẩy-động các đường dẫn dữ liệu; sự suy luận các chip đánh đổi độ chính xác cho thông lượng;
di động các chip đánh đổi thông lượng cho năng lượng tính hiệu quả (Training chips invest silicon in wide floating-point datapaths; inference chips trade precision for throughput; mobile chips trade throughput for energy efficiency). Không có đơn thiết kế thống trị qua tất cả các khối lượng công việc,
thứ mà là chính xác tại sao phần cứng sự lựa chọn phụ thuộc trên khối lượng công việc sự phân tích thay vì tiêu đề
các thông số kỹ thuật (No single design dominates across all workloads, which is precisely why hardware selection depends on workload analysis rather than headline specifications).

================ PAGE 618 ================

580
11.4 Tính toán Các đơn vị và Sự thực thi Các mô hình (Compute Units and Execution Models)
Bảng 11.7: AI Bộ xử lý Các cấu hình: Hiện đại AI các bộ xử lý ưu tiên khác nhau sự thực thi đơn vị các đặc điểm cho cụ thể
các khối lượng công việc (Table 11.7: AI Processor Configurations: Modern AI processors prioritize different execution unit characteristics for specific workloads): NVIDIA A100 sử dụng rộng SIMD và tensor các lõi cho sự đào tạo, Google TPUv4 nhấn mạnh cao-thông lượng BF16
ma trận phép nhân, Intel Sapphire Rapids tập trung trên INT8-được tối ưu hóa sự suy luận, và di động các NPU ưu tiên thấp-năng lượng
sự thực thi (NVIDIA A100 uses wide SIMD and tensor cores for training, Google TPUv4 emphasizes high-throughput BF16 matrix multiplication, Intel Sapphire Rapids focuses on INT8-optimized inference, and mobile NPUs prioritize low-power execution). Những các sự biến thiên này trong SIMD chiều rộng, tensor lõi kích thước, và việc xử lý phần tử số đếm phản ánh đang phát triển tính đa dạng trong AI
phần cứng các kiến trúc (These variations in SIMD width, tensor core size, and processing element count reflect the growing diversity in AI hardware architectures).
Bộ xử lý (Processor)
SIMD Chiều rộng (SIMD Width)
Tensor Lõi Kích thước (Tensor Core Size)
việc xử lý các phần tử (processing elements)
Chính Các khối lượng công việc (Primary Workloads)
NVIDIA A100
1024-bit
4×4×4 FP16
108 SMs
Sự đào tạo, HPC (Training, HPC)
Google TPUv4
128-rộng (128-wide)
128×128 BF16
2 các lõi/chip (2 cores/chip)
Sự đào tạo (Training)
Intel Sapphire
512-bit AVX
32×32 INT8/BF16
56 các lõi (56 cores)
Sự suy luận (Inference)
Di động NPU (Mobile NPU)
CPU/GPU/DSP các vector (CPU/GPU/DSP vectors)
Nhỏ ma trận các ô gạch (Small matrix tiles)
Được tích hợp NPU các khối (Integrated NPU blocks)
Di động sự suy luận (Mobile inference)
11.4.10 Chi phí-hiệu suất sự phân tích (Cost-performance analysis)
Trong khi thuộc về kiến trúc các thông số kỹ thuật định nghĩa tính toán tiềm năng, thực tế sự triển khai các quyết định
yêu cầu việc hiểu chi phí-hiệu suất các sự đánh đổi qua khác nhau máy gia tốc các lựa chọn (While architectural specifications define computational potential, practical deployment decisions require understanding cost-performance trade-offs across different accelerator options). Tuy nhiên,
thô tính toán các số liệu một mình chúng cung cấp một không hoàn chỉnh bức tranh (However, raw computational metrics alone provide an incomplete picture). Thống trị sự ràng buộc trong hiện đại
AI sự gia tốc là không phải tính toán khả năng mà là dữ liệu sự di chuyển tính hiệu quả (The dominant constraint in modern AI acceleration is not compute capacity but data movement efficiency).
Năng lượng sự chênh lệch được thiết lập sớm hơn (nơi bộ nhớ truy cập các chi phí thống trị sự tính toán)
dẫn dắt toàn bộ được chuyên biệt hóa phần cứng cuộc cách mạng (The energy differential established earlier (where memory access costs dominate computation) drives the entire specialized hardware revolution). Sự chênh lệch này giúp giải thích tại sao nhiều máy gia tốc
đạt được chỉ một phần của đỉnh tính toán trên bị ràng buộc-bởi-bộ nhớ các khối lượng công việc, trong khi các kiến trúc thứ mà
tối đa hóa dữ liệu sự tái sử dụng (cho ví dụ, tâm thu các mảng trên dày đặc ma trận các hạt nhân) có thể duy trì một cách đáng kể
cao hơn sự sử dụng dưới thuận lợi các điều kiện (This disparity helps explain why many accelerators achieve only a fraction of peak compute on memory-bound workloads, while architectures that maximize data reuse (for example, systolic arrays on dense matrix kernels) can sustain substantially higher utilization under favorable conditions).
Xem xét một tổ chức việc chọn giữa "nhiều hơn của một cũ hơn máy gia tốc" so với "ít hơn của một mới hơn
máy gia tốc" (Consider an organization choosing between “more of an older accelerator” vs. “fewer of a newer accelerator.”). Đỉnh FLOP/s có thể là gây hiểu lầm cho kiểu-transformer các khối lượng công việc với thấp số học
cường độ, nơi sự đào tạo là thường bị ràng buộc băng thông-bộ nhớ thay vì bị ràng buộc tính toán (Peak FLOP/s can be misleading for transformer-style workloads with low arithmetic intensity, where training is often memory-bandwidth bound rather than compute bound). Trong như vậy
các trường hợp, băng thông trên mỗi đô la và có thể đạt được sự sử dụng có thể quan trọng nhiều hơn so với tiêu đề tính toán, vì vậy
một mới hơn máy gia tốc với một cách đáng kể cao hơn băng thông có thể phân phối một cách vật chất tốt hơn được duy trì
hiệu suất thậm chí nếu đỉnh FLOP/s cải thiện bởi một nhỏ hơn hệ số (In such cases, bandwidth per dollar and achievable utilization can matter more than headline compute, so a newer accelerator with substantially higher bandwidth can deliver materially better sustained performance even if peak FLOP/s improves by a smaller factor).
Những các động lực này giúp giải thích nhanh chóng sự áp dụng của mới hơn các máy gia tốc mặc dù cao hơn đơn vị các giá (These dynamics help explain the rapid adoption of newer accelerators despite higher unit prices).
Cho bị ràng buộc-bởi-bộ nhớ các khối lượng công việc, các sự cải thiện trong hiệu quả băng thông (và phần mềm ngăn xếp của
khả năng để sử dụng nó) có thể thống trị thế giới-thực hiệu suất (For memory-bound workloads, improvements in effective bandwidth (and the software stack’s ability to use it) can dominate real-world performance). Đám mây sự triển khai xa hơn làm phức tạp
sự phân tích, như cho thuê việc định giá, sự sử dụng, và thuộc về hoạt động các chi phí chung có thể thay đổi điểm hòa vốn
giữa việc mua và việc thuê phần cứng (Cloud deployment further complicates the analysis, as rental pricing, utilization, and operational overheads can change the break-even point between purchasing and renting hardware).
Bảng 11.8 cung cấp mang tính đại diện chi phí-hiệu suất dữ liệu cho phổ biến các máy gia tốc (Table 11.8 provides representative cost-performance data for common accelerators). Những các con số này
là xấp xỉ và thay đổi bởi nhà cung cấp, khu vực, và mua khối lượng; chính sự thấu hiểu là xu hướng
thay vì tuyệt đối các con số (These figures are approximate and vary by vendor, region, and purchase volume; the key insight is the trend rather than the absolute numbers). Chi phí trên mỗi TFLOP/s đã cải thiện một cách đáng kể từ V100 tới
mới hơn các máy gia tốc, thậm chí như tuyệt đối năng lượng yêu cầu (TDP) đã leo lên tới gần 1,000 W
cho hàng đầu các đơn vị, việc phản ánh ngành công nghiệp của sự dịch chuyển hướng tới mật độ qua thô đơn vị chi phí (The cost per TFLOP/s has improved substantially from V100 to newer accelerators, even as the absolute power requirement (TDP) has climbed to nearly 1,000 W for flagship units, reflecting the industry’s shift toward density over raw unit cost). Xu hướng là không
nghiêm ngặt đơn điệu ở mọi thế hệ dưới tất cả độ chính xác các chế độ: dưới mang tính đại diện TF32
sự tính toán được hiển thị ở đây, H100 của giá trên mỗi TFLOP/s chạy hơi bên trên A100 của bởi vì danh sách giá
đã chia tỷ lệ nhanh hơn so với TF32 thông lượng (The trend is not strictly monotonic at every generation under all precision modes: under the representative TF32 calculation shown here, H100’s price per TFLOP/s runs slightly above A100’s because list price scaled faster than TF32 throughput).
Bảng 11.8: Máy gia tốc Chi phí-Hiệu suất Sự so sánh: Phần cứng các chi phí được đánh giá chống lại mang tính đại diện đỉnh tính toán
các khả năng cho tối ưu sự triển khai chiến lược sự lựa chọn (Table 11.8: Accelerator Cost-Performance Comparison: Hardware costs evaluated against representative peak computational capabilities for optimal deployment strategy selection). Các độ chính xác các chế độ khác biệt bởi hàng, vì vậy giá/hiệu suất các mục là
hữu dụng cho xu hướng trực giác nhưng là không một táo-tới-táo FP16 sự so sánh (The precision modes differ by row, so price/performance entries are useful for trend intuition but are not an apples-to-apples FP16 comparison). Mới hơn các máy gia tốc cung cấp tốt hơn giá-hiệu suất
các tỷ lệ, mặc dù tổng chi phí của sự sở hữu bao gồm năng lượng sự tiêu thụ, làm mát các yêu cầu, và cơ sở hạ tầng các chi phí (Newer accelerators offer better price-performance ratios, though total cost of ownership includes power consumption, cooling requirements, and infrastructure costs). Các giá là
xấp xỉ danh sách các giá và thay đổi bởi khu vực và khối lượng; TPU việc định giá được ước tính từ đám mây các tỷ lệ (Prices are approximate list prices and vary by region and volume; TPU pricing estimated from cloud rates).
Máy gia tốc (Accelerator)
Danh sách Giá (List Price)
Mang tính đại diện Đỉnh Thông lượng
(độ chính xác được hiển thị) (Representative Peak Throughput (precision shown))
Bộ nhớ
Băng thông (Memory Bandwidth)
Giá/Hiệu suất (Price/Performance)
NVIDIA V100
~$10,000
125 TFLOP/s
900 GB/s
$80/(TFLOP/s)
NVIDIA A100
~$15,000
312 TFLOP/s
2,039 GB/s
$48.1/(TFLOP/s)
NVIDIA H100
~$25,000–30,000
494 TFLOP/s (TF32)
3,350 GB/s
~$50.6/(TFLOP/s)
Google TPUv4
~$8,000*
275 TFLOP/s (BF16)
1,200 GB/s
~$29.1/(TFLOP/s)
Intel Gaudi 2
~$12,000
865 TFLOP/s (FP8)
2,450 GB/s
$13.9/(TFLOP/s)

================ PAGE 619 ================

11. Phần cứng Sự gia tốc (Hardware Acceleration)
581
Bảng tiết lộ một vài quan trọng các mẫu (The table reveals several important patterns). Đầu tiên, giá-hiệu suất nói chung cải thiện qua
các thế hệ, mặc dù không một cách đơn điệu dưới mọi giá và độ chính xác giả định (First, price-performance generally improves across generations, though not monotonically under every price and precision assumption). Thứ hai, bộ nhớ
băng thông thường cải thiện nhanh hơn so với giá-hiệu suất tỷ lệ gợi ý, việc làm mới hơn
các máy gia tốc không cân xứng có giá trị cho bị ràng buộc-bởi-bộ nhớ các khối lượng công việc (Second, memory bandwidth often improves faster than the price-performance ratio suggests, making newer accelerators disproportionately valuable for memory-bound workloads). Thứ ba, "tốt nhất" máy gia tốc
phụ thuộc một cách nặng nề trên khối lượng công việc các đặc điểm: một transformer sự đào tạo khối lượng công việc thứ mà là bị ràng buộc
băng thông-bộ nhớ có thể hưởng lợi nhiều hơn từ H100 của 3,350 GB/s băng thông so với từ thô FLOP/s
các sự cải thiện (Third, the “best” accelerator depends heavily on workload characteristics: a transformer training workload that is memory-bandwidth bound may benefit more from H100’s 3,350 GB/s bandwidth than from raw FLOP/s improvements). Băng thông một cách nhất quán nổi lên như việc quyết định thuộc về kinh tế hệ số, thứ mà dẫn
một cách trực tiếp tới vật lý nguồn gốc của AI bộ nhớ bức tường (Bandwidth consistently emerges as the deciding economic factor, which leads directly to the physical origin of the AI memory wall).
Framework sự lựa chọn một cách đáng kể ảnh hưởng những thuộc về kinh tế các quyết định này (Framework selection significantly impacts these economic decisions). Chi tiết phần cứng-framework
sự tối ưu hóa các chiến lược được bao phủ trong Chương 7, trong khi hiệu suất sự đánh giá các phương pháp luận là
được thảo luận trong Chương 12 (Detailed hardware-framework optimization strategies are covered in Chapter 7, while performance evaluation methodologies are discussed in Chapter 12).
Trước các phần đã tiết lộ ấn tượng tính toán máy móc: vector các đơn vị việc đạt được 8×
sự song song thông qua SIMD sự thực thi, ma trận các hoạt động việc xử lý 256 các phần tử một cách đồng thời,
và tensor các lõi việc thực thi 16×16×16 được hợp nhất nhân-tích lũy các khối như được cống hiến ô gạch các hoạt động (The preceding sections revealed impressive computational machinery: vector units achieving 8× parallelism through SIMD execution, matrix operations processing 256 elements simultaneously, and tensor cores executing 16×16×16 fused multiply-accumulate blocks as dedicated tile operations).
Một NVIDIA A100 của tensor các lõi có thể thực thi 312 TFLOP/s, và mới hơn các máy gia tốc mở rộng xu hướng này
với FP8 sự hỗ trợ cho thấp hơn-độ chính xác sâu sự học hỏi các khối lượng công việc (NVIDIA Corporation 2020; Kuzmin
et al. 2022; Micikevicius et al. 2022) (An NVIDIA A100’s tensor cores can execute 312 TFLOP/s, and newer accelerators extend this trend with FP8 support for lower-precision deep learning workloads (NVIDIA Corporation 2020; Kuzmin et al. 2022; Micikevicius et al. 2022)). Ở những các tỷ lệ này, thuần túy số học cho một ResNet-50 tiến lượt
có thể hoàn thành trong các microgiây (At these rates, the pure arithmetic for a ResNet-50 forward pass could complete in microseconds).
NVIDIA của Blackwell (B200) kiến trúc mở rộng xu hướng này bằng cách việc giới thiệu bản địa FP4 sự hỗ trợ,
với NVIDIA việc báo cáo lên tới 9 PFLOP/s (dày đặc) hoặc 18 PFLOP/s (thưa thớt) đỉnh thông lượng trong FP4
trên mỗi chip (NVIDIA Corporation 2024) (NVIDIA’s Blackwell (B200) architecture extends this trend by introducing native FP4 support, with NVIDIA reporting up to 9 PFLOP/s (dense) or 18 PFLOP/s (sparse) peak throughput in FP4 per chip (NVIDIA Corporation 2024)). Điều này xác nhận độ chính xác nút thắt cổ chai xu hướng: như các mô hình phát triển,
phần cứng thích nghi bằng cách việc đánh đổi độ chính xác cho khổng lồ sự song song, việc yêu cầu các hệ thống các kỹ sư để thành thạo
dần dần thấp hơn-bit các kỹ thuật số (FP8, FP4) để mở khóa silicon của đầy đủ tiềm năng (This confirms the precision bottleneck trend: as models grow, hardware adapts by trading precision for massive parallelism, requiring systems engineers to master progressively lower-bit numerics (FP8, FP4) to unlock the silicon’s full potential).
Tuy nhiên thực tế ResNet-50 sự suy luận tốn các mili giây, không các microgiây (Yet real ResNet-50 inference takes milliseconds, not microseconds). Khoảng trống giữa lý thuyết
khả năng và thực tế hiệu suất tiết lộ chương của trung tâm sự căng thẳng, đầu tiên được đặt ra trong Mục đích
phần: tính toán khả năng đã vượt xa của chúng ta khả năng để nuôi dữ liệu tới các bộ xử lý (The gap between theoretical capability and practical performance reveals the chapter’s central tension, first posed in the Purpose section: computational capability has outpaced our ability to feed data to processors). Việc di chuyển
dữ liệu từ bộ nhớ tốn các bậc của độ lớn nhiều hơn năng lượng so với số học, và bộ nhớ băng thông đã
cải thiện chậm hơn so với tensor số học thông lượng (Moving data from memory costs orders of magnitude more energy than arithmetic, and memory bandwidth has improved more slowly than tensor arithmetic throughput). Sự chênh lệch này xác định liệu những
312 TFLOP/s đó dịch thành thấp được duy trì sự sử dụng hay cao được duy trì sự sử dụng trên một cụ thể
khối lượng công việc (Horowitz 2014; Gholami et al. 2024) (This disparity determines whether those 312 TFLOP/s translate into low sustained utilization or high sustained utilization on a particular workload (Horowitz 2014; Gholami et al. 2024)).
Việc hiểu tại sao này khoảng trống tồn tại, và cái gì thuộc về kiến trúc các sự đổi mới giải quyết nó, yêu cầu việc kiểm tra
bộ nhớ các hệ thống thứ mà nuôi dữ liệu tới tính toán các nguyên thủy được phân tích sớm hơn (Understanding why this gap exists, and what architectural innovations address it, requires examining the memory systems that feed data to the compute primitives analyzed earlier). Bộ nhớ
hệ thống phân cấp là không chỉ đơn thuần một hỗ trợ hệ thống con; nó là chính yếu tố quyết định của liệu các máy gia tốc
đạt được của chúng lý thuyết tiềm năng (The memory hierarchy is not merely a supporting subsystem; it is the primary determinant of whether accelerators achieve their theoretical potential).
11.5 AI Bộ nhớ Các hệ thống (AI Memory Systems)
ResNet-50 có thể phơi bày khoảng trống giữa máy gia tốc số học và máy gia tốc bộ nhớ: tensor
các lõi có thể cung cấp khổng lồ thấp-độ chính xác thông lượng, nhưng tích chập các trọng số, các sự kích hoạt, và
trung gian các kết quả vẫn phải đến đúng giờ (ResNet-50 can expose the gap between accelerator arithmetic and accelerator memory: tensor cores may offer enormous low-precision throughput, but convolution weights, activations, and intermediate results still have to arrive on time). Sự thực thi các đơn vị được kiểm tra trong trước các phần
(SIMD các đơn vị, tensor các lõi, và tâm thu các mảng) cung cấp ấn tượng tính toán thông lượng, với
hiện đại các máy gia tốc việc đạt tới hàng trăm của TFLOP/s hoặc nhiều hơn cho thấp-độ chính xác thần kinh-mạng
các hoạt động (NVIDIA Corporation 2020, 2024; Choquette 2023) (The execution units examined in previous sections (SIMD units, tensor cores, and systolic arrays) provide impressive computational throughput, with modern accelerators reaching hundreds of TFLOP/s or more for low-precision neural-network operations (NVIDIA Corporation 2020, 2024; Choquette 2023)). Những lý thuyết các khả năng đó vẫn
chưa được hiện thực hóa khi bộ nhớ các hệ thống con không thể cung cấp dữ liệu ở đủ các tốc độ (Those theoretical capabilities remain unrealized when memory subsystems cannot supply data at sufficient rates). Sự ràng buộc này, được gọi là
AI bộ nhớ bức tường, là cũng vật lý cốt lõi của các hệ thống khoảng trống thứ mà hình 11.3 đã lập biểu đồ: của tất cả
các cách mô hình nhu cầu chạy vượt qua phần cứng nguồn cung, sự tụt hậu của bộ nhớ băng thông phía sau số học
thông lượng là thống trị thành phần (This constraint, termed the AI memory wall, is also the physical core of the systems gap that figure 11.3 charted: of all the ways model demand outruns hardware supply, the lag of memory bandwidth behind arithmetic throughput is the dominant component).
Không giống thông thường các khối lượng công việc, ML các mô hình yêu cầu thường xuyên truy cập tới lớn các thể tích của các tham số,
các sự kích hoạt, và trung gian các kết quả, việc dẫn tới đáng kể bộ nhớ băng thông các nhu cầu (Unlike conventional workloads, ML models require frequent access to large volumes of parameters, activations, and intermediate results, leading to substantial memory bandwidth demands).
Này thách thức giao nhau với dữ liệu sự quản lý các chiến lược được bao phủ trong Chương 4 (This challenge intersects with the data management strategies covered in Chapter 4). Hiện đại AI
phần cứng giải quyết những các nhu cầu này thông qua tiên tiến bộ nhớ các hệ thống phân cấp, hiệu quả dữ liệu sự di chuyển
các kỹ thuật, và sự nén các chiến lược thứ mà thúc đẩy hiệu quả sự thực thi (Modern AI hardware addresses these demands through advanced memory hierarchies, efficient data movement techniques, and compression strategies that promote efficient execution).
11.5.1 Việc hiểu AI bộ nhớ bức tường (Understanding the AI memory wall)
AI bộ nhớ bức tường đại diện chính nút thắt cổ chai việc ràng buộc hiện đại máy gia tốc hiệu suất:
đang phát triển sự chênh lệch giữa tính toán thông lượng và bộ nhớ băng thông thứ mà (The AI memory wall represents the primary bottleneck constraining modern accelerator performance: the growing disparity between computational throughput and memory bandwidth that)

================ PAGE 620 ================

582
11.5 AI Bộ nhớ Các hệ thống (AI Memory Systems)
27
Von Neumann Nút thắt cổ chai
(Von Neumann Bottleneck): Vật lý sự tách biệt
của bộ xử lý từ của nó bộ
nhớ buộc tất cả các lệnh và
dữ liệu để đi ngang một dùng nhiều-
năng lượng bus (The physical separation of the processor from its memory forces all instructions and data to traverse an energy-intensive bus). Khoảng cách này
là trực tiếp nguyên nhân của cao
năng lượng chi phí của dữ liệu sự di chuyển;
mọi byte phải được tìm nạp,
việc trả một vật lý thuế (This distance is the direct cause of the high energy cost of data movement; every byte must be fetched, paying a physical tax).
Việc
truy cập một giá trị từ bên ngoài
DRAM có thể tốn hơn 20,000×
nhiều hơn năng lượng so với việc thực hiện
một 8-bit số nguyên hoạt động trên
giá trị đó (Horowitz 2014) (Accessing a value from external DRAM can cost over 20,000× more energy than performing an 8-bit integer operation on that value (Horowitz 2014)).
ngăn chặn các máy gia tốc khỏi việc đạt được của chúng lý thuyết các khả năng (prevents accelerators from achieving their theoretical capabilities). Trong khi tính toán các đơn vị có thể thực thi
hàng triệu của các hoạt động trên mỗi giây thông qua được chuyên biệt hóa các nguyên thủy giống như vector các hoạt động và ma trận
các phép nhân, chúng phụ thuộc một cách tới hạn trên bộ nhớ các hệ thống để cung cấp liên tục luồng của
các trọng số, các sự kích hoạt, và trung gian các kết quả thứ mà những các hoạt động này yêu cầu (While compute units can execute millions of operations per second through specialized primitives like vector operations and matrix multiplications, they depend critically on memory systems to supply the continuous stream of weights, activations, and intermediate results these operations require).
Định nghĩa 11.4 (Definition 11.4): AI bộ nhớ bức tường (AI memory wall)
AI Bộ nhớ Bức tường là ML máy gia tốc hiệu suất sự ràng buộc thứ mà phát sinh khi số học
thông lượng (𝑅peak) chạy vượt qua bộ nhớ băng thông (BW) (The AI Memory Wall is the ML accelerator performance constraint that arises when arithmetic throughput (𝑅peak) outpaces memory bandwidth (BW)).
1. Ý nghĩa (Significance): Nó ra lệnh rằng hệ thống hiệu suất là không còn bị giới hạn bởi FLOP/s, mà
bởi năng lượng và độ trễ chi phí của việc di chuyển dữ liệu (It dictates that system performance is no longer bounded by FLOP/s, but by the energy and latency cost of moving data). Bên trong sắt quy luật, nó là điểm nơi
𝐷vol / BW thuật ngữ thống trị tổng sự thực thi thời gian (𝑇) (Within the iron law, it is the point where the 𝐷vol/BW term dominates the total execution time (𝑇)).
2. Sự phân biệt (Distinction): Không giống một đa-mục đích bộ nhớ bức tường, thứ mà ảnh hưởng tất cả việc tính toán, AI
bộ nhớ bức tường được dẫn dắt bởi khổng lồ mô hình trạng thái và sự kích hoạt sự lưu trữ được yêu cầu bởi
sâu sự học hỏi (Unlike a general-purpose memory wall, which affects all computing, the AI memory wall is driven by the massive model state and activation storage required by deep learning).
3. Phổ biến cạm bẫy (Common pitfall): Một thường xuyên quan niệm sai lầm là rằng bộ nhớ bức tường được "sửa chữa" bởi nhiều hơn
bộ nhớ (A frequent misconception is that the memory wall is “fixed” by more memory). Trong thực tế, nó là một băng thông-độ trễ khoảng trống: thậm chí với vô hạn khả năng, tốc độ của
việc di chuyển dữ liệu giữa bộ nhớ và tính toán duy trì cơ bản vật lý nút thắt cổ chai (In reality, it is a bandwidth-latency gap: even with infinite capacity, the speed of moving data between memory and compute remains the fundamental physical bottleneck).
Nằm bên dưới nguyên nhân của bức tường này là vật lý: Von Neumann27 Nút thắt cổ chai, thứ mà đã
ràng buộc việc tính toán kể từ 1945, làm việc di chuyển dữ liệu tốn các bậc của độ lớn nhiều hơn năng lượng so với
việc xử lý nó, và hình 11.9 hiển thị tại sao AI các máy gia tốc phải ưu tiên dữ liệu tính cục bộ qua thô
số học thông lượng (The underlying cause of this wall is physical: the Von Neumann27 Bottleneck, which has constrained computing since 1945, makes moving data cost orders of magnitude more energy than processing it, and figure 11.9 shows why AI accelerators must prioritize data locality over raw arithmetic throughput).
10^-2
10^-1
10^0
10^1
10^2
10^3
Năng lượng trên mỗi Hoạt động (picojoules) [Log Thang đo] (Energy per Operation (picojoules) [Log Scale])
INT8 Cộng (INT8 Add)
FP32 Cộng (FP32 Add)
FP32 Nhân (FP32 Mult)
SRAM Đọc (8 KB) (SRAM Read (8 KB))
DRAM Đọc (DRAM Read)
0.03 pJ
0.9 pJ
3.7 pJ
5.0 pJ
640.0 pJ
~128× Chi phí (Bộ nhớ Bức tường) (~128× Cost (The Memory Wall))
Hình 11.9: Năng lượng Hệ thống phân cấp: Năng lượng chi phí trên mỗi hoạt động (Log Thang đo) dựa trên 'Horowitz Các con số' (Figure 11.9: The Energy Hierarchy: Energy cost per operation (Log Scale) based on the ‘Horowitz Numbers’). Việc tìm nạp dữ liệu
từ ngoài-chip DRAM tốn ~128× nhiều hơn năng lượng so với một SRAM truy cập và ~20,000× nhiều hơn so với một INT8 sự cộng (Fetching data from off-chip DRAM costs ~128× more energy than an SRAM access and ~20,000× more than an INT8 addition). Này rõ ràng
vật lý sự chênh lệch ra lệnh rằng AI các máy gia tốc phải ưu tiên dữ liệu tính cục bộ (việc giữ các trọng số trong SRAM/Các thanh ghi) qua thô
số học thông lượng để duy trì bên trong năng lượng các ngân sách (This stark physical disparity dictates that AI accelerators must prioritize data locality (keeping weights in SRAM/Registers) over raw arithmetic throughput to remain within power budgets).
11.5.1.1 Việc định lượng tính toán-bộ nhớ hiệu suất khoảng trống (Quantifying the compute-memory performance gap)
Năng lượng sự chênh lệch thứ mà hình 11.9 nắm bắt phát triển nhiều hơn nghiêm trọng với mỗi phần cứng thế hệ (The energy disparity that figure 11.9 captures grows more severe with each hardware generation).
Qua qua hai các thập kỷ, đỉnh tính toán các khả năng đã phát triển một cách đáng kể nhanh hơn so với
DRAM băng thông (Gholami et al. 2024) (Over the past two decades, peak computational capabilities have grown substantially faster than DRAM bandwidth (Gholami et al. 2024)). Sự phân kỳ này tạo ra một việc mở rộng khoảng trống nơi các máy gia tốc
sở hữu khổng lồ tính toán sức mạnh nhưng không thể truy cập dữ liệu đủ nhanh để sử dụng nó (This divergence creates a widening gap where accelerators possess massive computational power but cannot access data quickly enough to use it). Mang tính đại diện
cao-cấp các máy gia tốc có thể phân phối trên bậc của 10^3 TFLOP/s của đỉnh tensor thông lượng (cho
ví dụ, NVIDIA H100 việc phân phối 989 TFLOP/s trong FP16 hoặc gần 2,000 TFLOP/s trong FP8) trong khi (Representative high-end accelerators can deliver on the order of 103 TFLOP/s of peak tensor throughput (for example, NVIDIA H100 delivering 989 TFLOP/s in FP16 or nearly 2,000 TFLOP/s in FP8) while)

================ PAGE 621 ================

11. Phần cứng Sự gia tốc (Hardware Acceleration)
583
việc cung cấp xấp xỉ 3.35 TB/s của bộ nhớ băng thông (Choquette 2023) (providing approximately 3.35 TB/s of memory bandwidth (Choquette 2023)). Điều này ngụ ý rằng trên
bậc của 10^2 FLOP của công việc trên mỗi byte được di chuyển là được yêu cầu để hoàn toàn sử dụng tính toán, thứ mà có thể
vượt quá số học cường độ của nhiều thực tế thần kinh mạng các khối lượng công việc (This implies that on the order of 102 FLOP of work per byte moved is required to fully use the compute, which can exceed the arithmetic intensity of many practical neural network workloads).
Bộ nhớ bức tường biểu hiện thông qua ba tới hạn các sự ràng buộc (The memory wall manifests through three critical constraints). Đầu tiên, năng lượng sự chênh lệch: việc truy cập
DRAM có thể tiêu thụ các bậc của độ lớn nhiều hơn năng lượng so với một nhân-tích lũy hoạt động
(Horowitz 2014; Sze et al. 2017), thứ mà thường dịch chuyển các nút thắt cổ chai từ thô tính toán sang năng lượng và
dữ liệu sự di chuyển (First, the energy disparity: accessing DRAM can consume orders of magnitude more energy than a multiply-accumulate operation (Horowitz 2014; Sze et al. 2017), which often shifts bottlenecks from raw compute to power and data movement). Thứ hai, băng thông sự giới hạn: thậm chí TB/s bộ nhớ các hệ thống có thể không nuôi lớn
song song tính toán các mảng một cách liên tục trên bị ràng buộc-bởi-bộ nhớ các khối lượng công việc, việc để lại tính toán bị sử dụng dưới mức (Second, the bandwidth limitation: even TB/s memory systems may not feed large parallel compute arrays continuously on memory-bound workloads, leaving compute underutilized).
Thứ ba, độ trễ hệ thống phân cấp: ngoài-chip bộ nhớ truy cập có thể yêu cầu hàng trăm của các chu kỳ, việc tạo ra đường ống
các sự đình trệ thứ mà xếp tầng thông qua song song sự thực thi các đơn vị (Third, the latency hierarchy: off-chip memory access can require hundreds of cycles, creating pipeline stalls that cascade through parallel execution units).
11.5.2 Phần cứng sự cân bằng (𝐼ridge): Mô hình sự phân vùng (Hardware balance (𝐼ridge): The paradigm partition)
Khác nhau các mô hình cư trú khác nhau các vùng của này "bộ nhớ bức tường" (Different paradigms inhabit different regions of this “memory wall.”). Chúng ta định lượng điều này việc sử dụng
phần cứng sự cân bằng (𝐼ridge), được định nghĩa như số học cường độ được yêu cầu để che giấu chi phí của việc tìm nạp
một byte của dữ liệu; đường mái nhà tài liệu gọi này ngưỡng là đỉnh điểm (We quantify this using the hardware balance (𝐼ridge), defined as the arithmetic intensity required to hide the cost of fetching one byte of data; the roofline literature calls this threshold the ridge point):
𝐼ridge = 𝑅peak / BW
Này tỷ lệ phân vùng sự triển khai phổ thành hai riêng biệt các chế độ (This ratio partitions the deployment spectrum into two distinct regimes). Cao-cấp các máy gia tốc giống như
NVIDIA H100 có một sự cân bằng của ≈150–300, việc làm chúng "Đói-Băng thông" những người khổng lồ nơi
thách thức là việc di chuyển dữ liệu đủ nhanh để bão hòa các ALU (High-end accelerators like the NVIDIA H100 have a balance of ≈150–300, making them “Bandwidth-Hungry” giants where the challenge is moving data fast enough to saturate the ALUs). Ngược lại, TinyML các vi điều khiển
thường có một sự cân bằng của < 10, việc làm chúng "Đói-Tính toán" nhưng một cách tương đối hiệu quả-băng thông (In contrast, TinyML microcontrollers often have a balance of < 10, making them “Compute-Starved” but relatively bandwidth-efficient).
Điều này giải thích tại sao một kiến trúc thứ mà là hiệu quả trong đám mây (nơi chúng ta tối ưu hóa cho BW các giới hạn)
có thể là một thảm họa ở biên: phần cứng sự cân bằng đã dịch chuyển dưới mô hình, việc biến đổi một
bị ràng buộc-bởi-bộ nhớ sự thành công thành một bị ràng buộc-bởi-tính toán sự thất bại (This explains why an architecture that is efficient in the cloud (where we optimize for BW limits) can be a disaster at the edge: the hardware balance has shifted under the model, transforming a memory-bound success into a compute-bound failure).
Sự phân kỳ giữa hai này sự chia tỷ lệ các tốc độ được định lượng trong hình 11.10 (The divergence between these two scaling rates is quantified in figure 11.10). Khoảng trống giữa
tính toán đường cong và băng thông đường cong mở rộng năm qua năm, việc xác nhận rằng bộ nhớ băng thông,
không phải tính toán, là chính sự ràng buộc trong AI sự gia tốc (The gap between the compute curve and the bandwidth curve widens year over year, confirming that memory bandwidth, not compute, is the primary constraint in AI acceleration). Các giá trị là mang tính minh họa để nhấn mạnh
sự phân kỳ xu hướng (The values are illustrative to emphasize the divergence trend).
2000
2005
2010
2015
2020
2025
Năm (Year)
10^1
10^3
10^5
10^7
10^9
10^11
10^13
10^15
Hiệu suất (FLOP/s hoặc GB/s, log thang đo) (Performance (FLOP/s or GB/s, log scale))
Bộ nhớ Bức tường (Memory Wall)
Tính toán Hiệu suất (Compute Performance)
Bộ nhớ Băng thông (Memory Bandwidth)
Hình 11.10: Tính toán-Băng thông Sự phân kỳ: Tính toán thông lượng (FLOP/s) và bộ nhớ băng thông (GB/s) được lập biểu đồ
trên một log thang đo (2000–2025) (Figure 11.10: The Compute-Bandwidth Divergence: Compute throughput (FLOP/s) and memory bandwidth (GB/s) plotted on a log scale (2000–2025)). Trong khi số học thông lượng đã phát triển một cách theo hàm mũ, băng thông đã cải thiện chậm hơn (While arithmetic throughput has grown exponentially, bandwidth has improved more slowly). Các giá trị
là mang tính minh họa để hiển thị việc mở rộng AI bộ nhớ bức tường (Values are illustrative to show the widening AI memory wall).
Sự mất cân bằng có một trực tiếp thuộc về kiến trúc hệ quả có thể nhìn thấy trong hình 11.11: phần cứng đỉnh
điểm đã leo lên một cách sắc bén và duy trì cao, việc đẩy thưa thớt và thấp-sự tái sử dụng các hoạt động xa hơn vào
bị ràng buộc-bởi-bộ nhớ chế độ trên hiện đại các máy gia tốc (The imbalance has a direct architectural consequence visible in figure 11.11: the hardware ridge point has climbed sharply and remains high, pushing sparse and low-reuse operations further into the memory-bound regime on modern accelerators).

================ PAGE 622 ================

584
11.5 AI Bộ nhớ Các hệ thống (AI Memory Systems)
2017
2020
2022
2024
Phát hành Năm (Release Year)
0
100
200
300
400
500
600
Số học Cường độ (FLOP/byte) (Arithmetic Intensity (FLOP/byte))
V100
139
A100
153
H100
295
B200
281
Giàu-Bộ nhớ Vùng (Memory-Rich Zone)
(Cũ Các hoạt động An toàn (Legacy Ops Safe))
Đậm đặc-Tính toán Vùng (Compute-Dense Zone)
(Các Transformer Được yêu cầu (Transformers Required))
Hình 11.11: Đang tăng Đỉnh (The Rising Ridge): Phần cứng số học cường độ (FLOP/byte) qua thời gian việc sử dụng dày đặc FP16 tensor các đỉnh và
bộ nhớ băng thông từ cục bộ phần cứng các hằng số (Figure 11.11: The Rising Ridge: Hardware arithmetic intensity (FLOP/byte) over time using dense FP16 tensor peaks and memory bandwidth from the local hardware constants). Như tính toán khả năng phát triển nhanh hơn so với bộ nhớ băng thông, đỉnh
điểm tăng từ V100 thông qua H100 và duy trì cao trên B200 (As compute capability grows faster than memory bandwidth, the ridge point rises from V100 through H100 and remains high on B200). Xu hướng này giải thích tại sao các kiến trúc với cao dữ liệu sự tái sử dụng
hưng thịnh trong khi thấp-sự tái sử dụng các khối lượng công việc đối mặt một đang phát triển phần cứng thuế (This trend explains why architectures with high data reuse flourish while low-reuse workloads face a growing hardware tax).
Vượt ra ngoài hiệu suất các sự giới hạn, bộ nhớ truy cập áp đặt một dốc năng lượng chi phí (Beyond performance limitations, memory access imposes a steep energy cost). Việc tìm nạp dữ liệu
từ ngoài-chip DRAM tiêu thụ xa nhiều hơn năng lượng so với việc thực hiện số học các hoạt động (Horowitz
2014) (Fetching data from off-chip DRAM consumes far more energy than performing arithmetic operations (Horowitz 2014)). Này sự không hiệu quả là đặc biệt rõ ràng trong máy học các mô hình, nơi lớn tham số
các kích thước, thường xuyên bộ nhớ các truy cập, và không đồng đều dữ liệu sự di chuyển các mẫu làm trầm trọng thêm bộ nhớ
các nút thắt cổ chai (This inefficiency is particularly evident in machine learning models, where large parameter sizes, frequent memory accesses, and nonuniform data movement patterns exacerbate memory bottlenecks). Năng lượng sự chênh lệch dẫn dắt thuộc về kiến trúc các quyết định: Google của TPUv1 đã đạt được 30–80×
tốt hơn hiệu suất trên mỗi watt so với đương thời các CPU và các GPU trên Google của sự suy luận các điểm chuẩn
bằng cách việc tối thiểu hóa dữ liệu sự di chuyển thông qua tâm thu các mảng và lớn trên-chip bộ nhớ (Jouppi et al.
2017) (The energy differential drives architectural decisions: Google’s TPUv1 achieved 30–80× better performance per watt than contemporary CPUs and GPUs on Google’s inference benchmarks by minimizing data movement through systolic arrays and large on-chip memory (Jouppi et al. 2017)). Những thiết kế các sự lựa chọn này chứng minh rằng năng lượng các sự ràng buộc, không phải tính toán các giới hạn, thường
xác định thực tế sự triển khai tính khả thi (These design choices demonstrate that energy constraints, not computational limits, often determine practical deployment feasibility).
11.5.2.1 Bộ nhớ truy cập các mẫu trong ML các khối lượng công việc (Memory access patterns in ML workloads)
Để làm những năng lượng các chi phí này cụ thể, chúng ta có thể theo dõi một đơn tensor thông qua mọi cấp độ của bộ nhớ
hệ thống phân cấp trong suốt một thực sự sự suy luận lượt (To make these energy costs concrete, we can trace a single tensor through every level of the memory hierarchy during a real inference pass).
Ngọn hải đăng 11.2 (Lighthouse 11.2): Cuộc đời của một tensor: Được lưu trữ-bởi-GPU KWS (Life of a tensor: GPU-hosted KWS)
Gợi nhớ Từ khóa Phát hiện (Keyword Spotting) ngọn hải đăng được tóm tắt trong bảng 2.2 (Recall the Keyword Spotting lighthouse summarized in table 2.2). Nếu cùng một-giây âm thanh
đoạn được đóng lô trên một được lưu trữ-bởi-GPU sự suy luận đường dẫn, của nó vật lý hành trình thông qua bộ nhớ
hệ thống phân cấp trông giống như điều này (If the same one-second audio clip is batched on a GPU-hosted inference path, its physical journey through the memory hierarchy looks like this):
1. DRAM (HBM): Tensor bắt đầu ở đây (DRAM (HBM): The tensor starts here).
• Kích thước (Size): 16,000 các mẫu × 2 bytes (FP16) = 32 KB (16,000 samples × 2 bytes (FP16) = 32 KB).
• Độ trễ (Latency): Việc tìm nạp điều này từ ngoài-chip bộ nhớ tốn ~300 ns (cộng việc xếp hàng sự chậm trễ) (Fetching this from off-chip memory takes ~300 ns (plus queuing delay)).
• Năng lượng (Energy): Chi phí là ~20 pJ/bit (Cost is ~20 pJ/bit). Cao chi phí (High cost).
2. L2 bộ nhớ cache (L2 cache): GPU của DMA động cơ kéo nó tới đây (The GPU’s DMA engine pulls it here).
• Độ trễ (Latency): ~4 ns.
• Truy cập (Access): Được chia sẻ qua nhiều Việc truyền phát Đa bộ xử lý (SMs) (Shared across multiple Streaming Multiprocessors (SMs)).
3. L1 bộ nhớ cache/được chia sẻ bộ nhớ (L1 cache/shared memory): Một cụ thể SM yêu cầu một ô gạch của âm thanh (A specific SM claims a tile of the audio).
• Độ trễ (Latency): ~1 ns.
• Tính cục bộ (Locality): Tới hạn bước (Critical step). Nếu dữ liệu rời khỏi cấp độ này, chúng ta trả "HBM Thuế" lần nữa (If the data leaves this level, we pay the “HBM Tax” again).

================ PAGE 623 ================

11. Phần cứng Sự gia tốc (Hardware Acceleration)
585
4. Các thanh ghi (Registers): Tensor Lõi hoạt hoạt động ở đây (The Tensor Core operates here).
• Độ trễ (Latency): ~0 ns (đơn chu kỳ) (~0 ns (single cycle)).
• Thông lượng (Throughput): 312 TFLOP/s.
• Năng lượng (Energy): Chi phí là ~0.1 pJ/bit (Cost is ~0.1 pJ/bit).
Các hệ thống sự thấu hiểu (Systems insight): "Tốc độ của Ánh sáng" giới hạn có nghĩa là chúng ta không thể tính toán nhanh hơn so với chúng ta có thể
di chuyển dữ liệu từ Bước 1 tới Bước 4 (The “Speed of Light” limit means we cannot compute faster than we can move data from Step 1 to Step 4). Đường mái nhà được xác định bởi băng thông của Bước 1 →
Bước 2 liên kết (The roofline is determined by the bandwidth of the Step 1 → Step 2 link).
Vượt ra ngoài thô tính toán thông lượng, một máy gia tốc của tính hiệu quả phụ thuộc trên của nó khả năng để liên tục
cung cấp dữ liệu tới việc xử lý các đơn vị mà không các sự đình trệ (Beyond raw computational throughput, an accelerator’s efficiency depends on its ability to continuously supply data to processing units without stalls). Thần kinh các mạng áp đặt ba đồng thời
các nhu cầu trên này dữ liệu nguồn cung (Neural networks impose three concurrent demands on this data supply). Mô hình các tham số (các trọng số và các độ lệch) có thể đếm ở hàng tỷ,
việc yêu cầu hiệu quả sự lưu trữ và sự truyền phát để duy trì thông lượng (Model parameters (weights and biases) may number in the billions, requiring efficient storage and streaming to maintain throughput). Trung gian các sự kích hoạt được sản xuất
ở mỗi lớp phải được tạm thời giữ cho tiếp theo các hoạt động, việc đóng góp vào bộ nhớ chi phí chung
trong sâu các kiến trúc (Intermediate activations produced at each layer must be temporarily held for subsequent operations, contributing to memory overhead in deep architectures). Trong suốt sự đào tạo, lan truyền ngược cộng một thứ ba nhu cầu: việc lưu trữ và việc truy cập
các gradient cho mọi tham số, xa hơn việc tăng dữ liệu sự di chuyển thể tích giữa tính toán các đơn vị
và bộ nhớ (During training, backpropagation adds a third demand: storing and accessing gradients for every parameter, further increasing data movement volume between compute units and memory).
Như các mô hình tăng trong kích thước và độ phức tạp, các sự cải thiện trong bộ nhớ khả năng và băng thông
trở nên ngày càng quan trọng (As models increase in size and complexity, improvements in memory capacity and bandwidth become increasingly important). Mặc dù được chuyên biệt hóa tính toán các đơn vị tăng tốc các hoạt động giống như
ma trận các phép nhân, của chúng tổng thể hiệu suất phụ thuộc trên liên tục, hiệu quả sự phân phối của
dữ liệu tới việc xử lý các phần tử (Although specialized compute units accelerate operations like matrix multiplications, their overall performance depends on the continuous, efficient delivery of data to the processing elements). Trong quy mô-lớn các ứng dụng chẳng hạn như tự nhiên ngôn ngữ sự xử lý và
máy tính thị giác, các mô hình thường kết hợp hàng triệu tới hàng tỷ của các tham số (Brown et al. 2020),
và việc đạt được cao hiệu suất yêu cầu việc tối thiểu hóa các sự chậm trễ và các sự đình trệ được gây ra bởi không hiệu quả dữ liệu
sự di chuyển giữa bộ nhớ và tính toán các đơn vị (Narayanan et al. 2021; Kwon và Rhu 2018) (In large-scale applications such as natural language processing and computer vision, models often incorporate millions to billions of parameters (Brown et al. 2020), and achieving high performance requires minimizing delays and stalls caused by inefficient data movement between memory and compute units (Narayanan et al. 2021; Kwon and Rhu 2018)).
Một cách để định lượng này thách thức là bằng cách việc so sánh dữ liệu sự truyền tải thời gian với thời gian được yêu cầu
cho các sự tính toán (One way to quantify this challenge is by comparing the data transfer time with the time required for computations). Để làm điều này, theo sau các biến được định nghĩa: 𝐷vol là tổng dữ liệu thể tích (bytes),
BW là có sẵn bộ nhớ băng thông (bytes/s), 𝑂 là số đếm của dấu phẩy-động các hoạt động,
𝑅peak là đỉnh phần cứng thông lượng (FLOP/s), và 𝜂hw là được hiện thực hóa phần cứng sự sử dụng (To do this, the following variables are defined: 𝐷vol is the total data volume (bytes), BW is the available memory bandwidth (bytes/s), 𝑂is the number of floating-point operations, 𝑅peak is the peak hardware throughput (FLOP/s), and 𝜂hw is the realized hardware utilization).
Chúng ta có thể biểu diễn bộ nhớ sự truyền tải thời gian 𝑇mem và tính toán thời gian 𝑇compute như (We can express the memory transfer time 𝑇mem and compute time 𝑇compute as):
𝑇mem = 𝐷vol / BW
𝑇compute = 𝑂 / (𝑅peak ⋅ 𝜂hw)
Khi 𝑇mem > 𝑇compute, hệ thống trở nên bị ràng buộc bộ nhớ (When 𝑇mem > 𝑇compute, the system becomes memory bound). Này sự mất cân bằng buộc việc xử lý
các phần tử để dành nhiều hơn thời gian việc chờ đợi cho dữ liệu so với việc thực hiện các sự tính toán, việc chứng minh
nhu cầu cho được tối ưu hóa-bộ nhớ các kiến trúc và hiệu quả dữ liệu sự di chuyển các chiến lược để duy trì cao
hiệu suất (This imbalance forces the processing elements to spend more time waiting for data than performing computations, demonstrating the need for memory-optimized architectures and efficient data movement strategies to sustain high performance).
Hình 11.12 định lượng sự chênh lệch này cho cụ thể công khai-số đếm các mô hình và phần cứng các thế hệ,
việc hiển thị cách nào mô hình tham số các số đếm đã chạy vượt qua bộ nhớ băng thông các sự cải thiện (Figure 11.12 quantifies this disparity for specific public-count models and hardware generations, showing how model parameter counts have outpaced memory bandwidth improvements). Khoảng trống
giữa những các đường cong này, từ AlexNet của 60 triệu các tham số tới công khai được tiết lộ trăm-tỷ-
tham số các mô hình, đại diện kỹ thuật thách thức thứ mà dẫn dắt máy gia tốc bộ nhớ hệ thống
thiết kế (Krizhevsky et al. 2012; Brown et al. 2020; Chowdhery et al. 2022; Dubey et al. 2024) (The gap between these curves, from AlexNet’s 60 million parameters to publicly disclosed hundred-billion-parameter models, represents the engineering challenge that drives accelerator memory system design (Krizhevsky et al. 2012; Brown et al. 2020; Chowdhery et al. 2022; Dubey et al. 2024)). Thậm chí
cao-băng thông các máy gia tốc giống như NVIDIA của B200 và AMD của MI300X/MI325X-lớp các thiết bị không thể
đóng này khoảng trống bởi băng thông một mình: băng thông đã cải thiện xa ít hơn so với công khai biên giới-mô hình
tham số các số đếm qua cùng giai đoạn (NVIDIA Corporation 2024; AMD 2023) (Even high-bandwidth accelerators like NVIDIA’s B200 and AMD’s MI300X/MI325X-class devices cannot close this gap by bandwidth alone: bandwidth has improved far less than public frontier-model parameter counts over the same period (NVIDIA Corporation 2024; AMD 2023)). Tham số các số đếm
cho độc quyền các hệ thống chẳng hạn như GPT-4 và Gemini là không chính thức được tiết lộ, vì vậy chúng là không được lập biểu đồ
như thực tế dữ liệu các điểm (Parameter counts for proprietary systems such as GPT-4 and Gemini are not officially disclosed, so they are not plotted as factual data points).
11.5.2.2 Không đều bộ nhớ truy cập (Irregular memory access)
Nhiều ML các khối lượng công việc kết hợp đều dày đặc các hạt nhân với không đều bộ nhớ áp lực từ sự thưa thớt,
việc nhúng các lượt tra cứu, biến đổi chuỗi các độ dài, sự chú ý/KV-bộ nhớ cache lưu lượng, và nhỏ các lô (Many ML workloads combine regular dense kernels with irregular memory pressure from sparsity, embedding lookups, variable sequence lengths, attention/KV-cache traffic, and small batches). Các
dày đặc các phần là chính xác tại sao các máy gia tốc hoạt động quá tốt; các không đều các phần là nơi tiêu chuẩn việc lưu bộ nhớ cache (The dense parts are exactly why accelerators work so well; the irregular parts are where standard caching)

================ PAGE 624 ================

586
11.5 AI Bộ nhớ Các hệ thống (AI Memory Systems)
2012
2014
2016
2018
2020
2022
2024
2026
Năm (Year)
2
3
4
5
6
Log thang đo, cơ số 10 (các tham số hoặc GB/s) (Log scale, base 10 (params or GB/s))
NVIDIA Tesla K80
Google TPU v2
NVIDIA Tesla V100
Google TPU v6e
AMD MI325X
NVIDIA B200
PaLM
DeepSeek-V3
Llama 4 Maverick
AI Bộ nhớ Bức tường (AI Memory Wall)
Phần cứng băng thông (Hardware bandwidth)
Mô hình kích thước (Model size)
Hình 11.12: Mô hình Kích thước so với Phần cứng Băng thông: Công khai được tiết lộ mô hình tham số các số đếm và phần cứng bộ nhớ
băng thông được lập biểu đồ từ 2012 tới 2025, việc hiển thị cách nào mô hình sự phát triển từ AlexNet tới trăm-tỷ-tham số các mô hình đã xa
chạy vượt qua băng thông các sự cải thiện qua GPU và TPU các thế hệ (Figure 11.12: Model Size vs. Hardware Bandwidth: Publicly disclosed model parameter counts and hardware memory bandwidth plotted from 2012 to 2025, showing how model growth from AlexNet to hundred-billion-parameter models has far outpaced bandwidth improvements across GPU and TPU generations).
các cơ chế và bộ nhớ các hệ thống phân cấp đấu tranh, việc dẫn tới được tăng bộ nhớ độ trễ và không hiệu quả
băng thông sự sử dụng (mechanisms and memory hierarchies struggle, leading to increased memory latency and inefficient bandwidth utilization).
Việc so sánh ML bộ nhớ truy cập các mẫu chống lại truyền thống việc tính toán các khối lượng công việc tiết lộ
quy mô của thách thức (Comparing ML memory access patterns against traditional computing workloads reveals the scale of the challenge). Truyền thống các khối lượng công việc, chẳng hạn như khoa học việc tính toán, đa-mục đích CPU
các ứng dụng, và cơ sở dữ liệu sự xử lý, điển hình trưng bày được xác định-tốt bộ nhớ truy cập các đặc điểm
thứ mà hưởng lợi từ tiêu chuẩn việc lưu bộ nhớ cache và việc tìm nạp trước các kỹ thuật (Traditional workloads, such as scientific computing, general-purpose CPU applications, and database processing, typically exhibit well-defined memory access characteristics that benefit from standard caching and prefetching techniques). ML các khối lượng công việc, trên cái khác
tay, giới thiệu một cách cao động truy cập các mẫu (bảng 11.9) thứ mà thách thức thông thường bộ nhớ
sự tối ưu hóa các chiến lược (ML workloads, on the other hand, introduce highly dynamic access patterns (table 11.9) that challenge conventional memory optimization strategies).
Bảng 11.9: Bộ nhớ Truy cập Các đặc điểm: Truyền thống các khối lượng công việc trưng bày có thể dự đoán, tuần tự bộ nhớ truy cập việc hưởng lợi
từ tiêu chuẩn việc lưu bộ nhớ cache, trong khi máy học các khối lượng công việc giới thiệu không đều và động các mẫu do sự thưa thớt và dữ liệu
các sự phụ thuộc (Table 11.9: Memory Access Characteristics: Traditional workloads exhibit predictable, sequential memory access benefiting from standard caching, while machine learning workloads introduce irregular and dynamic patterns due to sparsity and data dependencies). Những các sự khác biệt này thông tin cho thiết kế của bộ nhớ các hệ thống thứ mà một cách hiệu quả hỗ trợ hiện đại AI các ứng dụng (These differences inform the design of memory systems that efficiently support modern AI applications).
Tính năng (Feature)
Truyền thống Việc tính toán Các khối lượng công việc (Traditional Computing Workloads)
Máy Học Các khối lượng công việc (Machine Learning Workloads)
Bộ nhớ Truy cập Mẫu (Memory Access Pattern)
Đều và có thể dự đoán (cho ví dụ, tuần tự các lượt đọc,
được cấu trúc các mẫu) (Regular and predictable (e.g., sequential reads, structured patterns))
Không đều và động (cho ví dụ, sự thưa thớt,
sự chú ý các cơ chế) (Irregular and dynamic (e.g., sparsity, attention mechanisms))
Bộ nhớ cache Tính cục bộ (Cache Locality)
Cao thuộc về thời gian và thuộc về không gian tính cục bộ (High temporal and spatial locality)
Thường thấp tính cục bộ, đặc biệt trong lớn
các mô hình (Often low locality, especially in large models)
Dữ liệu Sự tái sử dụng (Data Reuse)
Được cấu trúc các vòng lặp với thường xuyên dữ liệu sự tái sử dụng (Structured loops with frequent data reuse)
Thưa thớt và động sự tái sử dụng việc phụ thuộc trên
lớp loại (Sparse and dynamic reuse depending on layer type)
Dữ liệu Các sự phụ thuộc (Data Dependencies)
Được xác định-tốt các sự phụ thuộc cho phép hiệu quả
việc tìm nạp trước (Well-defined dependencies allow efficient prefetching)
Biến đổi các sự phụ thuộc dựa trên mạng
cấu trúc (Variable dependencies based on network structure)
Khối lượng công việc Ví dụ (Workload Example)
Khoa học việc tính toán (cho ví dụ, ma trận các sự phân tích thành nhân tử,
vật lý các mô phỏng) (Scientific computing (e.g., matrix factorizations, physics simulations))
Thần kinh các mạng (cho ví dụ, các CNN, các Transformer,
thưa thớt các mô hình) (Neural networks (e.g., CNNs, Transformers, sparse models))
Bộ nhớ Nút thắt cổ chai (Memory Bottleneck)
DRAM độ trễ, bộ nhớ cache các lượt trượt (DRAM latency, cache misses)
Ngoài-chip băng thông các sự ràng buộc, bộ nhớ
sự phân mảnh (Off-chip bandwidth constraints, memory fragmentation)
Tác động trên Năng lượng
Sự tiêu thụ (Impact on Energy Consumption)
Trung bình, được dẫn dắt bởi nặng-FLOP sự thực thi (Moderate, driven by FLOP-heavy execution)
Cao, được thống trị bởi dữ liệu sự di chuyển các chi phí (High, dominated by data movement costs)
Một chính nguồn của sự không đều trong ML các khối lượng công việc bắt nguồn từ lô kích thước và sự thực thi thứ tự (One key source of irregularity in ML workloads stems from batch size and execution order).
Cách nào đầu vào dữ liệu được xử lý trong các lô một cách trực tiếp ảnh hưởng bộ nhớ sự tái sử dụng, việc tạo ra một phức tạp
sự tối ưu hóa thách thức (The way input data is processed in batches directly affects memory reuse, creating a complex optimization challenge). Nhỏ lô các kích thước làm giảm bớt khả năng của việc tái sử dụng được lưu bộ nhớ cache các sự kích hoạt và
các trọng số, việc dẫn tới thường xuyên bộ nhớ các lượt tìm nạp từ chậm hơn, ngoài-chip bộ nhớ (Small batch sizes decrease the likelihood of reusing cached activations and weights, resulting in frequent memory fetches from slower, off-chip memory). Lớn hơn lô các kích thước có thể
cải thiện sự tái sử dụng và khấu hao bộ nhớ truy cập các chi phí, nhưng đồng thời đặt cao hơn các nhu cầu trên
có sẵn bộ nhớ băng thông, có tiềm năng việc tạo ra sự tắc nghẽn ở khác nhau bộ nhớ hệ thống phân cấp các cấp độ (Larger batch sizes can improve reuse and amortize memory access costs, but simultaneously place higher demands on available memory bandwidth, potentially creating congestion at different memory hierarchy levels).
Này tinh tế sự cân bằng yêu cầu cẩn thận sự xem xét của mô hình kiến trúc và có sẵn phần cứng
các tài nguyên (This delicate balance requires careful consideration of model architecture and available hardware resources).

================ PAGE 625 ================

11. Phần cứng Sự gia tốc (Hardware Acceleration)
587
28
Sự thưa thớt và Sự không đều của Bộ
nhớ (Sparsity and Memory Irregularity): Sự không đều này phát
sinh bởi vì các kỹ
thuật giống như việc cắt tỉa và động
các sự kích hoạt buộc bộ nhớ
các bộ điều khiển để thu thập rải
rác khác không các phần tử thông qua
gián tiếp việc lập địa chỉ,
việc phá
vỡ tuần tự truy cập các mẫu
thứ mà phần cứng các bộ nhớ cache
và các bộ tìm nạp trước phụ thuộc trên (This irregularity arises because techniques like pruning and dynamic activations force memory controllers to gather scattered nonzero elements via indirect addressing, breaking the sequential access patterns that hardware caches and prefetchers depend on).
Hậu quả sự đánh đổi là nghiêm
trọng, như độ trễ hình phạt
từ những ngẫu nhiên, không thể
dự đoán bộ nhớ các truy cập này có thể
dễ dàng phủ nhận tính toán
các sự tiết kiệm từ việc thực
hiện ít hơn các hoạt động (The resulting trade-off is severe, as the latency penalty from these random, unpredictable memory accesses can easily negate the computational savings from performing fewer operations). Không
có được chuyên biệt hóa phần cứng sự hỗ
trợ cho được cấu trúc sự thưa thớt,
một không được cấu trúc thưa thớt mô hình
có thể trở thành hoàn toàn bị ràng buộc
bởi bộ nhớ và chạy chậm hơn so với của nó
dày đặc bản sao, thậm chí với
hơn 90 phần trăm của của nó các trọng số
được loại bỏ (Without specialized hardware support for structured sparsity, an unstructured sparse model can become entirely memory bound and run slower than its dense counterpart, even with over 90 percent of its weights removed).
Khác nhau thần kinh mạng các lớp tương tác với bộ nhớ theo riêng biệt các cách vượt ra ngoài lô kích thước các sự xem xét (Different neural network layers interact with memory in distinct ways beyond batch size considerations). Tích chập các lớp hưởng lợi từ thuộc về không gian tính cục bộ, như lân cận các pixel trong một hình ảnh là
được xử lý cùng nhau, việc cho phép hiệu quả việc lưu bộ nhớ cache của nhỏ trọng số các hạt nhân (Convolutional layers benefit from spatial locality, as neighboring pixels in an image are processed together, enabling efficient caching of small weight kernels). Ngược lại, hoàn toàn được kết nối
các lớp yêu cầu thường xuyên truy cập tới lớn trọng số các ma trận, thường việc dẫn tới nhiều hơn được ngẫu nhiên hóa bộ nhớ
truy cập các mẫu thứ mà kém căn chỉnh với tiêu chuẩn việc lưu bộ nhớ cache các chính sách (Conversely, fully connected layers require frequent access to large weight matrices, often leading to more randomized memory access patterns that poorly align with standard caching policies). Các Transformer giới thiệu bổ sung
độ phức tạp, như sự chú ý các cơ chế đòi hỏi việc truy cập lớn khóa-giá trị các cặp được lưu trữ qua đa dạng
bộ nhớ các vị trí (Transformers introduce additional complexity, as attention mechanisms demand accessing large key-value pairs stored across varied memory locations). Động bản chất của chuỗi độ dài và sự chú ý khoảng thời gian làm truyền thống
việc tìm nạp trước các chiến lược không hiệu quả, việc dẫn tới không thể dự đoán bộ nhớ các độ trễ (The dynamic nature of sequence length and attention span renders traditional prefetching strategies ineffective, resulting in unpredictable memory latencies).
Một cái khác hệ số việc đóng góp vào không đều bộ nhớ truy cập là sự thưa thớt28 trong thần kinh các mạng (Another factor contributing to irregular memory access is sparsity28 in neural networks). Nhiều
hiện đại ML các mô hình triển khai các kỹ thuật chẳng hạn như trọng số việc cắt tỉa, sự kích hoạt sự thưa thớt, và được cấu trúc
sự thưa thớt để làm giảm bớt tính toán chi phí chung (Many modern ML models employ techniques such as weight pruning, activation sparsity, and structured sparsity to reduce computational overhead). Tuy nhiên, những các sự tối ưu hóa này thường dẫn tới không đồng đều
bộ nhớ truy cập, như thưa thớt các sự biểu diễn đòi hỏi việc tìm nạp rải rác các phần tử thay vì tuần tự
các khối, việc làm phần cứng việc lưu bộ nhớ cache kém hiệu quả (However, these optimizations often lead to nonuniform memory access, as sparse representations necessitate fetching scattered elements rather than sequential blocks, making hardware caching less effective). Các mô hình thứ mà kết hợp động tính toán
các đường dẫn, chẳng hạn như Hỗn hợp của Các chuyên gia (Mixture of Experts) và Thích ứng Tính toán Thời gian (Adaptive Computation Time), giới thiệu một cách cao phi-quyết-
định bộ nhớ truy cập các mẫu, nơi hoạt động các nơ-ron hoặc mô hình các thành phần có thể thay đổi với mỗi
sự suy luận bước (Models that incorporate dynamic computation paths, such as Mixture of Experts and Adaptive Computation Time, introduce highly nondeterministic memory access patterns, where the active neurons or model components can vary with each inference step). Sự biến thiên này thách thức hiệu quả việc tìm nạp trước và việc lưu bộ nhớ cache các chiến lược (This variability challenges efficient prefetching and caching strategies).
Những sự không đều này có thể đo lường các hệ quả (These irregularities have measurable consequences). ML các khối lượng công việc thường trải nghiệm được làm giảm bớt
bộ nhớ cache tính hiệu quả, như các sự kích hoạt và các trọng số có thể không được truy cập theo có thể dự đoán các chuỗi (ML workloads often experience reduced cache efficiency, as activations and weights may not be accessed in predictable sequences). Điều này
dẫn tới được tăng sự phụ thuộc trên ngoài-chip bộ nhớ lưu lượng, thứ mà làm chậm xuống sự thực thi và tiêu thụ
nhiều hơn năng lượng (This leads to increased reliance on off-chip memory traffic, which slows down execution and consumes more energy). Không đều truy cập các mẫu đóng góp vào bộ nhớ sự phân mảnh, nơi cách nào dữ liệu được
phân bổ và được truy xuất dẫn tới không hiệu quả sự sử dụng của có sẵn bộ nhớ các tài nguyên (Irregular access patterns contribute to memory fragmentation, where the way data is allocated and retrieved results in inefficient use of available memory resources). Kết hợp hiệu ứng
là rằng ML các máy gia tốc thường xuyên bắt gặp bộ nhớ các nút thắt cổ chai thứ mà giới hạn của chúng khả năng để hoàn toàn sử dụng
có sẵn tính toán sức mạnh (The combined effect is that ML accelerators frequently encounter memory bottlenecks that limit their ability to fully use available compute power).
Không đều truy cập các mẫu và bộ nhớ bức tường các sự ràng buộc được kiểm tra sớm hơn tạo ra đáng gờm
các thách thức, nhưng chúng cũng tiết lộ sự tối ưu hóa các cơ hội (The irregular access patterns and memory wall constraints examined earlier create formidable challenges, but they also reveal optimization opportunities). Mặc dù cá nhân bộ nhớ các truy cập
có thể dường như không thể dự đoán, ML các khối lượng công việc trưng bày được cấu trúc sự tái sử dụng các mẫu ở một cao hơn cấp độ:
cùng các trọng số được áp dụng qua lô các phần tử, cùng các hạt nhân trượt qua thuộc về không gian các chiều,
và cùng sự chú ý các mẫu tái diễn qua chuỗi các vị trí (Although individual memory accesses may appear unpredictable, ML workloads exhibit structured reuse patterns at a higher level: the same weights are applied across batch elements, the same kernels slide across spatial dimensions, and the same attention patterns recur across sequence positions). Phần cứng các nhà thiết kế khai thác những
sự đều đặn này thông qua một cách cẩn thận được cấu trúc bộ nhớ các hệ thống phân cấp thứ mà duy trì thường xuyên được truy cập dữ liệu
gần tới tính toán các đơn vị, thậm chí khi cụ thể truy cập chuỗi thay đổi (Hardware designers exploit these regularities through carefully structured memory hierarchies that maintain frequently accessed data close to compute units, even when the specific access sequence varies).
11.5.3 Bộ nhớ hệ thống phân cấp (Memory hierarchy)
Hiện đại AI các máy gia tốc khai thác những được cấu trúc sự tái sử dụng các mẫu này thông qua đa-cấp độ bộ nhớ các hệ thống phân
cấp: thay vì việc đối xử bộ nhớ như một nguyên khối tài nguyên, chúng tổ chức sự lưu trữ thành riêng biệt các tầng
được tối ưu hóa cho khác nhau truy cập các mẫu, sự tái sử dụng các khoảng cách, và năng lượng các chi phí (Modern AI accelerators exploit these structured reuse patterns through multilevel memory hierarchies: rather than treating memory as a monolithic resource, they organize storage into distinct tiers optimized for different access patterns, reuse distances, and energy costs). Trong khi đa-mục đích
việc tính toán đấu tranh với không thể dự đoán bộ nhớ truy cập, ML các khối lượng công việc trưng bày được cấu trúc sự tái sử dụng
thứ mà có thể được tối ưu hóa thông qua cẩn thận dữ liệu sự tổ chức qua nhiều bộ nhớ các cấp độ (While general-purpose computing contends with unpredictable memory access, ML workloads exhibit structured reuse that can be optimized through careful data organization across multiple memory levels).
Ở cao nhất cấp độ, lớn-khả năng nhưng chậm lưu trữ các thiết bị cung cấp dài-hạn mô hình sự lưu trữ (At the highest level, large-capacity but slow storage devices provide long-term model storage). Ở
thấp nhất cấp độ, cao-tốc độ các thanh ghi và các bộ nhớ cache đảm bảo rằng tính toán các đơn vị có thể truy cập các toán hạng
với tối thiểu độ trễ (At the lowest level, high-speed registers and caches ensure that compute units can access operands with minimal latency). Giữa những các thái cực này, trung gian bộ nhớ các cấp độ, chẳng hạn như bộ nhớ nháp (scratchpad memory), cao-băng thông bộ nhớ, và ngoài-chip DRAM, cung cấp các sự đánh đổi giữa hiệu suất và
khả năng (Between these extremes, intermediate memory levels, such as scratchpad memory, high-bandwidth memory, and off-chip DRAM, offer trade-offs between performance and capacity).
Chính mẫu trong bảng 11.10 là rằng mỗi bước xuống hệ thống phân cấp đánh đổi xấp xỉ một bậc của
độ lớn trong độ trễ cho một bậc của độ lớn trong khả năng—và năng lượng chi phí của một bộ nhớ
truy cập ở bất kỳ cấp độ nào làm lùn đi năng lượng chi phí của số học thứ mà nó nuôi (The key pattern in table 11.10 is that each step down the hierarchy trades roughly an order of magnitude in latency for an order of magnitude in capacity—and the energy cost of a memory access at any level dwarfs the energy cost of the arithmetic it feeds).
Bảng 11.10: Bộ nhớ Hệ thống phân cấp Các sự đánh đổi: AI các máy gia tốc sử dụng một đa-cấp độ bộ nhớ hệ thống phân cấp để cân bằng hiệu suất và
khả năng (Table 11.10: Memory Hierarchy Trade-Offs: AI accelerators use a multilevel memory hierarchy to balance performance and capacity). Mỗi cấp độ cung cấp riêng biệt độ trễ, băng thông, và khả năng các đặc điểm thứ mà ra lệnh cách nào thần kinh mạng
các thành phần (các trọng số, các sự kích hoạt, và trung gian các kết quả) nên được phân bổ để tối thiểu hóa các nút thắt cổ chai và tối đa hóa
thông lượng (Each level provides distinct latency, bandwidth, and capacity characteristics that dictate how neural network components (weights, activations, and intermediate results) should be allocated to minimize bottlenecks and maximize throughput).
Bộ nhớ Cấp độ (Memory Level)
Xấp xỉ. Độ trễ (Approx. Latency)
Băng thông (Bandwidth)
Khả năng (Capacity)
Ví dụ Sự sử dụng trong Sâu Sự học hỏi (Example Use in Deep Learning)
Các thanh ghi (Registers)
~1 chu kỳ (~1 cycle)
Cao nhất (Highest)
Vài các giá trị (Few values)
Việc lưu trữ các toán hạng cho ngay lập tức
sự tính toán (Storing operands for immediate computation)
L1/L2 Bộ nhớ cache (SRAM) (L1/L2 Cache (SRAM))
~1–10 ns
Cao (High)
KB–MB
Việc lưu bộ nhớ cache thường xuyên được truy cập
các sự kích hoạt và nhỏ trọng số các khối (Caching frequently accessed activations and small weight blocks)

================ PAGE 626 ================

588
11.5 AI Bộ nhớ Các hệ thống (AI Memory Systems)
Bộ nhớ Cấp độ (Memory Level)
Xấp xỉ. Độ trễ (Approx. Latency)
Băng thông (Bandwidth)
Khả năng (Capacity)
Ví dụ Sự sử dụng trong Sâu Sự học hỏi (Example Use in Deep Learning)
Bộ nhớ nháp (Scratchpad Memory)
~5–20 ns
Cao (High)
MB
Được quản lý-bởi-phần mềm sự lưu trữ cho
trung gian các sự tính toán (Software-managed storage for intermediate computations)
Cao-Băng thông
Bộ nhớ (HBM) (High-Bandwidth Memory (HBM))
~100 ns
Rất Cao (Very High)
GB
Việc lưu trữ lớn mô hình các tham số và
các sự kích hoạt cho cao-tốc độ truy cập (Storing large model parameters and activations for high-speed access)
Ngoài-Chip DRAM
(DDR, GDDR, LPDDR) (Off-Chip DRAM (DDR, GDDR, LPDDR))
~50–150 ns
Trung bình (Moderate)
GB–TB
Việc lưu trữ toàn bộ mô hình các trọng số thứ mà không
vừa trên-chip (Storing entire model weights that do not fit on-chip)
Flash Sự lưu trữ
(SSD/NVMe) (Flash Storage (SSD/NVMe))
~100 µs–1 ms
Thấp (Low)
TB
Việc lưu trữ được đào tạo-trước các mô hình và
các điểm kiểm tra cho sau này việc tải (Storing pretrained models and checkpoints for later loading)
Hệ thống phân cấp mời một dường như đơn giản giải pháp: xây dựng lớn hơn, nhanh hơn ngoài-chip bộ nhớ và
loại bỏ nhu cầu cho trên-chip SRAM hoàn toàn (The hierarchy invites an apparently simple solution: build larger, faster off-chip memory and eliminate the need for on-chip SRAM entirely). Câu trả lời được bắt nguồn từ vật lý: tín hiệu sự lan truyền
bên trong và giữa các chip áp đặt một cứng độ trễ sàn (The answer is rooted in physics: signal propagation within and between chips imposes a hard latency floor).
Giấy ăn Toán học 11.2 (Napkin Math 11.2): Tốc độ của ánh sáng giới hạn (The speed of light limit)
Vấn đề: Tại sao trên-chip SRAM là cần thiết thay vì việc tìm nạp tất cả dữ liệu từ HBM? (Problem: Why is on-chip SRAM necessary instead of fetching all data from HBM?)
Vật lý (Physics):
1. Khoảng cách (Distance): Trên một H100-lớp 814 mm² khuôn, các tín hiệu di chuyển ~20 mm (On an H100-class 814 mm² die, signals travel ~20 mm).
2. Tốc độ (Speed): Các tín hiệu trong silicon di chuyển ở ≈0.5𝑐 (nửa tốc độ của ánh sáng) (Signals in silicon travel at ≈0.5𝑐(half speed of light)).
3. Độ trễ (Latency): 20 mm tốn ≈130 ps (20 mm takes ≈130 ps).
4. Xung nhịp chu kỳ (Clock cycle): Ở 2 GHz, một chu kỳ là 500 ps (At 2 GHz, a cycle is 500 ps).
5. DRAM: Ngoài-chip HBM ngồi các milimet cách xa trên gói, nhưng DRAM truy cập độ trễ
cộng giao thức chi phí chung = 100+ các chu kỳ (Off-chip HBM sits millimeters away on the package, but DRAM access latency plus protocol overhead = 100+ cycles).
Các hệ thống sự thấu hiểu (Systems insight): Dữ liệu không thể được tìm nạp từ DRAM trong một đơn chu kỳ (Data cannot be fetched from DRAM in a single cycle). Nó là về mặt vật lý không thể (It is physically impossible).
Cục bộ các thanh ghi và SRAM (L1) là được yêu cầu để nuôi tính toán các đơn vị ở 2 GHz (Local registers and SRAM (L1) are required to feed compute units at 2 GHz). "Bộ nhớ
bức tường" là một phần một khoảng cách bức tường—và cho transformer các mô hình điều này là trực tiếp lý do các trọng số
phải được tổ chức trong SRAM trong các ô gạch thay vì được đọc trong một lượt từ HBM: khứ hồi độ trễ
tới HBM là quá dài để duy trì tâm thu mảng của đường ống (The “memory wall” is partially a distance wall—and for transformer models this is the direct reason weights must be staged in SRAM in tiles rather than read in one pass from HBM: the round-trip latency to HBM is too long to sustain the systolic array’s pipeline). Nó là cũng tại sao việc đọc một toàn bộ
KV-bộ nhớ cache từ HBM trên mọi token sự tạo ra bước làm sụp đổ sự suy luận thông lượng—sự
truy cập mẫu không thể được che giấu phía sau số học theo cách một được xếp ô gạch matmul có thể (It is also why reading an entire KV-cache from HBM on every token generation step collapses inference throughput—the access pattern cannot be hidden behind arithmetic the way a tiled matmul can).
11.5.3.1 Trên-chip bộ nhớ (On-chip memory)
Trên-chip bộ nhớ là nhanh cục bộ sự lưu trữ được đặt trên hoặc gần máy gia tốc khuôn, bao gồm các thanh ghi,
SRAM các bộ nhớ cache, và được quản lý-bởi-phần mềm các bộ nhớ nháp (On-chip memory is the fast local storage located on or near the accelerator die, including registers, SRAM caches, and software-managed scratchpads). Mỗi cấp độ của bộ nhớ hệ thống phân cấp phục vụ một
riêng biệt vai trò trong AI sự gia tốc, với khác nhau các sự đánh đổi trong tốc độ, khả năng, và tính có thể truy cập (Each level of the memory hierarchy serves a distinct role in AI acceleration, with different trade-offs in speed, capacity, and accessibility). Các thanh ghi,
được đặt bên trong tính toán các lõi, cung cấp nhanh nhất truy cập nhưng có thể chỉ lưu trữ một vài các toán hạng tại một
thời điểm (Registers, located within compute cores, provide the fastest access but can only store a few operands at a time). Những thứ này là tốt nhất được sử dụng cho ngay lập tức các sự tính toán, nơi các toán hạng được cần thiết cho một hoạt động
có thể được tải và được tiêu thụ bên trong một vài các chu kỳ (These are best used for immediate computations, where the operands needed for an operation can be loaded and consumed within a few cycles). Tuy nhiên, bởi vì thanh ghi sự lưu trữ là quá bị giới hạn,
thường xuyên bộ nhớ các truy cập là được yêu cầu để tìm nạp mới các toán hạng và lưu trữ trung gian các kết quả (However, because register storage is so limited, frequent memory accesses are required to fetch new operands and store intermediate results).
Để làm giảm bớt nhu cầu cho liên tục dữ liệu sự di chuyển giữa các thanh ghi và bên ngoài bộ nhớ, nhỏ nhưng
nhanh các bộ nhớ cache phục vụ như một trung gian bộ đệm (To reduce the need for constant data movement between registers and external memory, small but fast caches serve as an intermediary buffer). Những các bộ nhớ cache này lưu trữ gần đây được truy cập các sự kích hoạt, các trọng số,
và trung gian các giá trị, việc đảm bảo rằng thường xuyên được sử dụng dữ liệu duy trì có sẵn với tối thiểu sự chậm trễ (These caches store recently accessed activations, weights, and intermediate values, ensuring that frequently used data remains available with minimal delay).
Tuy nhiên, kích thước của các bộ nhớ cache là bị giới hạn, việc làm chúng không đủ cho việc lưu trữ đầy đủ đặc trưng các bản đồ hoặc lớn
trọng số các tensor trong máy học các mô hình (However, the size of caches is limited, making them insufficient for storing full feature maps or large weight tensors in machine learning models). Như một kết quả, chỉ những thường xuyên nhất được sử dụng các phần của một
mô hình của các tham số hoặc các sự kích hoạt có thể cư trú ở đây tại bất kỳ cho trước thời điểm (As a result, only the most frequently used portions of a model’s parameters or activations can reside here at any given time).
Cho lớn hơn việc làm việc các tập dữ liệu, nhiều AI các máy gia tốc bao gồm bộ nhớ nháp, thứ mà cung cấp nhiều hơn
sự lưu trữ so với các bộ nhớ cache nhưng với một chính sự khác biệt: nó cho phép tường minh phần mềm sự kiểm soát qua cái gì dữ liệu
được lưu trữ và khi nào nó bị đuổi (For larger working datasets, many AI accelerators include scratchpad memory, which offers more storage than caches but with a key difference: it allows explicit software control over what data is stored and when it is evicted). Không giống các bộ nhớ cache, thứ mà dựa trên dựa trên-phần cứng sự đuổi các chính sách,
bộ nhớ nháp cho phép máy học các khối lượng công việc để giữ lại chính các giá trị chẳng hạn như các sự kích hoạt và
bộ lọc các trọng số cho nhiều các lớp của sự tính toán (Unlike caches, which rely on hardware-based eviction policies, scratchpad memory enables machine learning workloads to retain key values such as activations and filter weights for multiple layers of computation). Khả năng này là hữu dụng trong các mô hình giống như tích chập
thần kinh các mạng, nơi cùng đầu vào đặc trưng các bản đồ và bộ lọc các trọng số được tái sử dụng qua nhiều (This capability is useful in models like convolutional neural networks, where the same input feature maps and filter weights are reused across multiple)

================ PAGE 627 ================

11. Phần cứng Sự gia tốc (Hardware Acceleration)
589
các hoạt động (operations). Bằng cách việc giữ dữ liệu này trong bộ nhớ nháp thay vì việc tải lại nó từ bên ngoài
bộ nhớ, các máy gia tốc có thể một cách đáng kể làm giảm bớt không cần thiết bộ nhớ các sự truyền tải và cải thiện tổng thể
tính hiệu quả (Chen, Emer, et al. 2017) (By keeping this data in scratchpad memory rather than reloading it from external memory, accelerators can significantly reduce unnecessary memory transfers and improve overall efficiency (Chen, Emer, et al. 2017)). Trên NVIDIA các GPU, phần cứng phơi bày bộ nhớ nháp tới
các lập trình viên như được chia sẻ bộ nhớ (shared memory): một nhanh, được quản lý-bởi-phần mềm SRAM vùng thứ mà tất cả các luồng trong một luồng
khối có thể đọc và ghi, riêng biệt từ được quản lý-bởi-phần cứng L1/L2 các bộ nhớ cache (On NVIDIA GPUs, the hardware exposes scratchpad memory to programmers as shared memory: a fast, software-managed SRAM region that all threads in a thread block can read and write, distinct from the hardware-managed L1/L2 caches). Tùy chỉnh ML các hạt nhân
được viết trong CUDA hoặc Triton kiểm soát bộ nhớ này một cách tường minh (Custom ML kernels written in CUDA or Triton control this memory explicitly). FlashAttention đạt được của nó đáng kể
thông lượng các lợi ích cho transformer sự chú ý các lớp chính xác bằng cách việc khai thác này cơ chế: thay
vì việc vật chất hóa đầy đủ 𝑆×𝑆 sự chú ý điểm số ma trận trong HBM, nó xếp ô gạch các truy vấn, các khóa, và các giá trị
thông qua SRAM/được chia sẻ bộ nhớ và ghi chỉ cuối cùng đầu ra trở lại tới HBM (T. Dao et al. 2022) (FlashAttention achieves its substantial throughput gains for transformer attention layers precisely by exploiting this mechanism: rather than materializing the full 𝑆×𝑆attention score matrix in HBM, it tiles queries, keys, and values through SRAM/shared memory and writes only the final output back to HBM (T. Dao et al. 2022)).
Sự giảm bớt trong HBM các khứ hồi—không phải ít hơn số học các hoạt động—là chính nguồn của
phần tăng tốc (The reduction in HBM round-trips—not fewer arithmetic operations—is the primary source of the speedup).
Ví dụ 11.2 (Example 11.2): Tensor Lõi hợp đồng (The Tensor Core contract)
Kịch bản (Scenario): Một transformer khối lượng công việc di chuyển từ cũ hơn các GPU tới NVIDIA A100 các GPU, việc mong đợi
một lớn phần tăng tốc từ Tensor Các lõi (A transformer workload moves from older GPUs to NVIDIA A100 GPUs, expecting a large speedup from Tensor Cores).
Sự thất bại chế độ (Failure mode): Việc lập hồ sơ hiển thị rằng Tensor Các lõi là hầu như không hoạt động (Profiling shows that the Tensor Cores are barely active). Khối lượng công việc sử dụng
độ chính xác các định dạng, các chiều, hoặc tùy chỉnh các hạt nhân thứ mà không khớp phần cứng của được tăng tốc
tensor-hoạt động các đường dẫn (The workload uses precision formats, dimensions, or custom kernels that do not match the hardware’s accelerated tensor-operation paths). Tensor Các lõi trên các A100 chỉ kích hoạt cho cụ thể độ chính xác các định dạng
(FP16, BF16, hoặc TF32) (Tensor Cores on A100s only trigger for specific precision formats (FP16, BF16, or TF32)). Bằng cách việc buộc FP32 sự tích lũy theo một cách phần cứng đã không hỗ trợ cho
sự gia tốc, mã đã rơi lùi lại tới tiêu chuẩn CUDA các lõi, thứ mà có 1/16th thông lượng (By forcing FP32 accumulation in a way the hardware did not support for acceleration, the code fell back to the standard CUDA cores, which have 1/16th the throughput).
Các hệ thống sự thấu hiểu (Systems insight): Phần cứng các tính năng là giòn các hợp đồng (Hardware features are brittle contracts). Nếu khối lượng công việc không trình bày
được hỗ trợ dữ liệu các loại và ô gạch các hình dạng, máy gia tốc rơi lùi lại tới chung sự thực thi (If the workload does not present supported data types and tile shapes, the accelerator falls back to generic execution). Phần cứng
không thể được khai thác mà không việc tuân thủ tới của nó các hợp đồng (NVIDIA Corporation 2020) (Hardware cannot be exploited without conforming to its contracts (NVIDIA Corporation 2020)).
11.5.3.2 Ngoài-chip bộ nhớ (Off-chip memory)
Một khi một mô hình của làm việc tập phát triển quá mức trên-chip SRAM, thiết kế câu hỏi là không còn cách nào nhanh mỗi
tầng là mà là cái nào ngoài-chip tầng dữ liệu hạ cánh trong đó, bởi vì mọi bước xuống bảng 11.10 đánh đổi độ trễ
cho khả năng (Once a model’s working set outgrows on-chip SRAM, the design question is no longer how fast each tier is but which off-chip tier the data lands in, because every step down table 11.10 trades latency for capacity). Mô hình kích thước thiết lập câu trả lời: các trọng số thứ mà vừa trong HBM truyền phát ở một vài TB/s; các trọng số thứ mà
tràn vào hàng hóa DRAM trả cao hơn truy cập độ trễ trên mọi lượt tìm nạp; và các trọng số thứ mà sống
chỉ trên flash phải được tổ chức vào nhanh hơn bộ nhớ trước khi máy gia tốc có thể sản xuất một đơn kết quả (Model size sets the answer: weights that fit in HBM stream at a few TB/s; weights that overflow into commodity DRAM pay higher access latency on every fetch; and weights that live only on flash must be staged into faster memory before the accelerator can produce a single result).
Các tầng bên dưới mô tả cái gì mỗi cấp độ cung cấp để mà này khả năng-so với-độ trễ sự lựa chọn có thể được
tạo ra một cách có chủ ý thay vì bởi mặc định (The tiers below describe what each level offers so that this capacity-versus-latency choice can be made deliberately rather than by default).
Vượt ra ngoài trên-chip bộ nhớ, cao-băng thông bộ nhớ cung cấp nhanh truy cập tới lớn hơn mô hình các tham
số và các sự kích hoạt thứ mà không vừa bên trong các bộ nhớ cache hoặc bộ nhớ nháp các bộ đệm (Beyond on-chip memory, high-bandwidth memory provides rapid access to larger model parameters and activations that do not fit within caches or scratchpad buffers). HBM đạt được của nó cao
hiệu suất bằng cách việc xếp chồng nhiều bộ nhớ các khuôn và việc sử dụng rộng bộ nhớ các giao diện, việc cho phép nó để
truyền tải lớn các lượng của dữ liệu với tối thiểu độ trễ so với truyền thống DRAM (HBM achieves its high performance by stacking multiple memory dies and using wide memory interfaces, allowing it to transfer large amounts of data with minimal latency compared to traditional DRAM). Bởi vì của nó
cao băng thông và thấp hơn độ trễ, HBM là thường được sử dụng để lưu trữ toàn bộ các lớp của máy học các mô
hình thứ mà phải được truy cập một cách nhanh chóng trong suốt sự thực thi (Because of its high bandwidth and lower latency, HBM is often used to store entire layers of machine learning models that must be accessed quickly during execution). Tuy nhiên, của nó chi phí và năng lượng sự tiêu thụ giới hạn
của nó sự sử dụng chủ yếu tới cao-hiệu suất AI các máy gia tốc, việc làm nó ít phổ biến trong bị ràng buộc-năng lượng
các môi trường chẳng hạn như biên các thiết bị (However, its cost and power consumption limit its use primarily to high-performance AI accelerators, making it less common in power-constrained environments such as edge devices).
Khi một máy học mô hình vượt quá khả năng của trên-chip bộ nhớ và HBM, nó phải dựa
trên ngoài-chip DRAM, chẳng hạn như DDR, GDDR, hoặc LPDDR (When a machine learning model exceeds the capacity of on-chip memory and HBM, it must rely on off-chip DRAM, such as DDR, GDDR, or LPDDR). Trong khi DRAM cung cấp một cách đáng kể lớn hơn sự lưu trữ
khả năng, của nó truy cập độ trễ là cao hơn, việc có nghĩa là thường xuyên các lượt truy xuất từ DRAM có thể giới thiệu
sự thực thi các nút thắt cổ chai (While DRAM offers significantly greater storage capacity, its access latency is higher, meaning that frequent retrievals from DRAM can introduce execution bottlenecks). Để tạo ra hiệu quả sự sử dụng của DRAM, các mô hình phải được cấu trúc để mà chỉ những
cần thiết các phần của các trọng số và các sự kích hoạt được truy xuất tại bất kỳ cho trước thời điểm, việc tối thiểu hóa tác động
của dài bộ nhớ tìm nạp các thời gian (To make effective use of DRAM, models must be structured so that only the necessary portions of weights and activations are retrieved at any given time, minimizing the impact of long memory fetch times).
Ở cao nhất cấp độ của hệ thống phân cấp, flash sự lưu trữ và rắn-trạng thái các ổ đĩa (SSDs) lưu trữ lớn được đào
tạo-trước các mô hình, các tập dữ liệu, và được kiểm tra các trọng số (At the highest level of the hierarchy, flash storage and solid-state drives (SSDs) store large pretrained models, datasets, and checkpointed weights). Những lưu trữ các thiết bị này cung cấp lớn các khả năng nhưng
là quá chậm cho thời gian-thực sự thực thi, việc yêu cầu các mô hình để được tải vào nhanh hơn bộ nhớ các tầng trước khi
sự tính toán bắt đầu (These storage devices offer large capacities but are too slow for real-time execution, requiring models to be loaded into faster memory tiers before computation begins). Cho ví dụ, trong sự đào tạo các kịch bản, được kiểm tra các mô hình được lưu trữ trong các SSD phải
được tải vào DRAM hoặc HBM trước khi việc tiếp tục sự tính toán, như trực tiếp sự thực thi từ các SSD sẽ
là quá chậm để duy trì hiệu quả máy gia tốc sự sử dụng (Narayanan et al. 2021) (For instance, in training scenarios, checkpointed models stored in SSDs must be loaded into DRAM or HBM before resuming computation, as direct execution from SSDs would be too slow to maintain efficient accelerator utilization (Narayanan et al. 2021)).

================ PAGE 628 ================

590
11.5 AI Bộ nhớ Các hệ thống (AI Memory Systems)
Băng thông thon nhỏ một cách dốc khi dữ
liệu di chuyển xa hơn từ máy
gia tốc (Bandwidth tapers steeply as data moves farther from the accelerator).
Bộ nhớ hệ thống phân cấp do đó cân bằng cạnh tranh các mục tiêu của tốc độ, khả năng, và năng lượng tính hiệu quả (The memory hierarchy thus balances competing objectives of speed, capacity, and energy efficiency).
Tuy nhiên, việc di chuyển dữ liệu thông qua nhiều bộ nhớ các cấp độ giới thiệu các nút thắt cổ chai thứ mà giới hạn máy gia tốc
hiệu suất (However, moving data through multiple memory levels introduces bottlenecks that limit accelerator performance). Dữ liệu các sự truyền tải giữa bộ nhớ các cấp độ gánh chịu độ trễ các chi phí, đặc biệt cho ngoài-chip
các truy cập (Data transfers between memory levels incur latency costs, particularly for off-chip accesses). Bị giới hạn băng thông hạn chế dữ liệu luồng giữa bộ nhớ các tầng (Limited bandwidth restricts data flow between memory tiers). Bộ nhớ khả năng các sự ràng buộc
buộc liên tục dữ liệu sự di chuyển như các mô hình vượt quá cục bộ sự lưu trữ (Memory capacity constraints force constant data movement as models exceed local storage). Những các sự ràng buộc này làm bộ nhớ
băng thông chính yếu tố quyết định của thế giới-thực máy gia tốc hiệu suất, một chủ đề chúng ta kiểm tra
tiếp theo (These constraints make memory bandwidth the primary determinant of real-world accelerator performance, a topic we examine next).
11.5.4 Bộ nhớ băng thông và thuộc về kiến trúc các sự đánh đổi (Memory bandwidth and architectural trade-offs)
Được quảng cáo bộ nhớ băng thông là chỉ một trần; có thể đạt được băng thông phụ thuộc trên truy cập mẫu,
việc đóng lô, tính cục bộ, và máy chủ giao diện thứ mà nuôi máy gia tốc (Advertised memory bandwidth is only a ceiling; achievable bandwidth depends on access pattern, batching, locality, and the host interface that feeds the accelerator). Hiện đại các máy gia tốc trưng bày
riêng biệt băng thông-khả năng các sự đánh đổi thứ mà một cách trực tiếp định hình cái nào các khối lượng công việc chúng có thể phục vụ một cách hiệu quả (Modern accelerators exhibit distinct bandwidth-capacity trade-offs that directly shape which workloads they can serve efficiently).
Mang tính đại diện trung tâm dữ liệu các máy gia tốc cung cấp bộ nhớ băng thông trên bậc của một vài TB/s, thường
được ghép nối với hàng chục của GB của cao-băng thông bộ nhớ (Representative data center accelerators provide memory bandwidth on the order of a few TB/s, often paired with tens of GB of high-bandwidth memory). Thô băng thông một mình, tuy nhiên, là gây hiểu lầm:
cái gì quan trọng là có thể đạt được băng thông cho một cho trước truy cập mẫu (Raw bandwidth alone, however, is misleading: what matters is achievable bandwidth for a given access pattern). Transformer sự chú ý, tích chập,
và hoàn toàn được kết nối các lớp có thể tất cả hiện thực hóa khác nhau các phân số của đỉnh băng thông bởi vì của chúng sự tái sử dụng,
việc xếp ô gạch, và truy cập sự đều đặn khác biệt (Transformer attention, convolution, and fully connected layers can all realize different fractions of peak bandwidth because their reuse, tiling, and access regularity differ). Hoàn toàn được kết nối các lớp tiếp cận đỉnh băng thông chỉ khi lô
các kích thước là đủ lớn để khấu hao chi phí của việc tải trọng số các ma trận—thứ mà kết nối một cách trực tiếp tới
lô-kích thước độ nhạy được thảo luận trong theo sau đường mái nhà sự phân tích (Fully connected layers approach peak bandwidth only when batch sizes are large enough to amortize the cost of loading weight matrices—which connects directly to the batch-size sensitivity discussed in the following roofline analysis). Thực tế hệ quả là
rằng một máy gia tốc của hiệu quả băng thông cho một cụ thể khối lượng công việc có thể là tốt bên dưới của nó được quảng cáo
đỉnh, việc làm băng thông-trên mỗi-đô la một đáng tin cậy hơn việc mua số liệu so với đỉnh băng thông một mình (The practical consequence is that an accelerator’s effective bandwidth for a specific workload may be well below its advertised peak, making bandwidth-per-dollar a more reliable purchasing metric than peak bandwidth alone).
Như được thiết lập sớm hơn, trên-chip bộ nhớ truy cập điển hình tiêu thụ năng lượng trong đơn-chữ số-tới-hàng chục
của picojoules trên mỗi truy cập, trong khi bên ngoài DRAM có thể là trên bậc của hàng trăm của picojoules trên mỗi
truy cập, một các bậc-của-độ lớn năng lượng hình phạt (As established earlier, on-chip memory access typically consumes energy in the single-digit-to-tens of picojoules per access, while external DRAM can be on the order of hundreds of picojoules per access, an orders-of-magnitude energy penalty). AI các máy gia tốc tối thiểu hóa DRAM truy cập thông qua
ba chính các chiến lược: trọng số tính cố định (việc giữ mô hình các tham số trong trên-chip bộ nhớ), đầu vào
tính cố định (việc đệm đầu vào các sự kích hoạt một cách cục bộ), và đầu ra tính cố định (việc tích lũy một phần các tổng
trên-chip) (AI accelerators minimize DRAM access through three key strategies: weight stationarity (keeping model parameters in on-chip memory), input stationarity (buffering input activations locally), and output stationarity (accumulating partial sums on-chip)).
Bộ nhớ băng thông sự chia tỷ lệ theo sau khác nhau các quỹ đạo qua máy gia tốc các thiết kế (Memory bandwidth scaling follows different trajectories across accelerator designs). GPU các kiến
trúc chia tỷ lệ băng thông bằng cách việc cộng bộ nhớ các kênh, việc đạt tới trên bậc của 1 TB/s trong luồng chính
các sản phẩm và một vài TB/s trong cao-cấp các hệ thống (GPU architectures scale bandwidth by adding memory channels, reaching on the order of 1 TB/s in mainstream products and a few TB/s in high-end systems). TPU-lớp các thiết kế đạt được của chúng băng thông tính hiệu quả
thông qua tâm thu mảng dữ liệu luồng và quyết liệt trên-chip sự tái sử dụng, thường việc đánh đổi tính linh hoạt cho tính hiệu quả
trên dày đặc tensor các hạt nhân (TPU-class designs achieve their bandwidth efficiency through systolic array dataflow and aggressive on-chip reuse, often trading flexibility for efficiency on dense tensor kernels). Di động hệ thống trên chip (SoC) các thiết kế đối mặt chặt chẽ nhất các sự ràng buộc, việc phân phối
trên bậc của hàng trăm của GB/s của được hợp nhất bộ nhớ băng thông bên trong một vài-watt năng lượng phong bì,
thứ mà đòi hỏi cẩn thận khối lượng công việc việc lập lịch và nhiệt sự quản lý (Mobile system on chip (SoC) designs face the tightest constraints, delivering on the order of hundreds of GB/s of unified memory bandwidth within a few-watt power envelope, which demands careful workload scheduling and thermal management).
HBM cung cấp xa cao hơn băng thông so với hàng hóa DDR bộ nhớ, nhưng ở một cách đáng kể cao hơn
chi phí và đóng gói độ phức tạp (HBM provides far higher bandwidth than commodity DDR memory, but at substantially higher cost and packaging complexity). Cao-băng thông các máy gia tốc do đó đánh đổi cao hơn bộ nhớ-hệ thống
chi phí cho cao hơn được duy trì hiệu suất trên bị ràng buộc-băng thông các khối lượng công việc (High-bandwidth accelerators therefore trade higher memory-system cost for higher sustained performance on bandwidth-bound workloads). Biên các máy gia tốc thường
hy sinh băng thông để gặp chặt chẽ chi phí và năng lượng các mục tiêu trong khi việc duy trì đủ hiệu suất
cho sự suy luận các khối lượng công việc (Edge accelerators often sacrifice bandwidth to meet tight cost and power targets while maintaining sufficient performance for inference workloads).
Những băng thông các đặc điểm này một cách trực tiếp ảnh hưởng sự triển khai các quyết định: đám mây sự đào tạo ưu tiên
thô băng thông cho tối đa mô hình khả năng, biên sự suy luận tối ưu hóa băng thông tính hiệu quả cho
năng lượng các sự ràng buộc, và di động sự triển khai cân bằng băng thông với chi phí các sự giới hạn (These bandwidth characteristics directly influence deployment decisions: cloud training prioritizes raw bandwidth for maximum model capacity, edge inference optimizes bandwidth efficiency for energy constraints, and mobile deployment balances bandwidth with cost limitations). Vượt ra ngoài
máy gia tốc của bên trong bộ nhớ hệ thống, tuy nhiên, dữ liệu phải cũng chảy giữa máy chủ CPU và
máy gia tốc, việc giới thiệu một cái khác có tiềm năng nút thắt cổ chai (Beyond the accelerator’s internal memory system, however, data must also flow between the host CPU and the accelerator, introducing another potential bottleneck). Này máy chủ-máy gia tốc giao diện thường trở thành
không mong đợi điểm thắt: thậm chí với 2 TB/s của HBM băng thông trên máy gia tốc, dữ liệu phải đầu tiên
đi ngang một PCIe liên kết thứ mà cung cấp chỉ 64 GB/s, một 30× băng thông sự giảm bớt thứ mà có thể thống trị tổng
độ trễ cho nhỏ, thường xuyên các sự truyền tải (NVIDIA Corporation 2020; C. NVIDIA 2020) (This host-accelerator interface often becomes the unexpected chokepoint: even with 2 TB/s of HBM bandwidth on the accelerator, data must first traverse a PCIe link that provides only 64 GB/s, a 30× bandwidth reduction that can dominate total latency for small, frequent transfers (NVIDIA Corporation 2020; C. NVIDIA 2020)).
11.5.5 Máy chủ-máy gia tốc sự giao tiếp (Host-accelerator communication)
Máy học các máy gia tốc, chẳng hạn như các GPU và các TPU, đạt được cao tính toán thông lượng
thông qua song song sự thực thi (Machine learning accelerators, such as GPUs and TPUs, achieve high computational throughput through parallel execution). Tuy nhiên, của chúng tính hiệu quả là thường bị ràng buộc bởi máy chủ-máy gia tốc dữ liệu
sự di chuyển giữa CPU và máy gia tốc bộ nhớ (However, their efficiency is often constrained by host-accelerator data movement between the CPU and accelerator memory). So với nhiều truyền thống các khối lượng công việc
thứ mà giữ hầu hết dữ liệu bên trong một đơn bộ nhớ miền, AI các khối lượng công việc có thể yêu cầu thường xuyên các sự truyền tải
giữa CPU bộ nhớ và máy gia tốc bộ nhớ, việc giới thiệu độ trễ, việc tiêu thụ băng thông, và
việc ảnh hưởng tổng thể hiệu suất (Compared to many traditional workloads that keep most data within a single memory domain, AI workloads can require frequent transfers between CPU memory and accelerator memory, introducing latency, consuming bandwidth, and affecting overall performance).

11. Phần cứng Sự gia tốc (Hardware Acceleration)
591
29
NVLink (NVIDIA Link): Trực tiếp
GPU-tới-GPU kết nối liên thông này tồn
tại để giữ máy gia tốc-tới-
máy gia tốc lưu lượng khỏi PCIe khi các tensor
phải di chuyển bên trong một máy chủ (This direct GPU-to-GPU interconnect exists to keep accelerator-to-accelerator traffic off PCIe when tensors must move inside a server).
Của nó 600–900 GB/s tổng
băng thông là gần tới một
bậc của độ lớn nhiều hơn, trên mỗi
hướng, so với tiêu chuẩn
PCIe bus, vì vậy các khối lượng công việc với
thường xuyên chéo-thiết bị tensor
sự di chuyển có thể duy trì trong
nhanh phần của băng thông
sự thon nhỏ (C. NVIDIA 2020; Choquette 2023) (Its 600–900 GB/s aggregate bandwidth is close to an order of magnitude more, per direction, than the standard PCIe bus, so workloads with frequent cross-device tensor movement can remain in the fast part of the bandwidth taper (C. NVIDIA 2020; Choquette 2023)). Sự đào tạo
các thuật toán thứ mà xác định
bao nhiêu tensor lưu lượng phải
băng qua liên kết này là được phát triển
sau này; phần cứng sự thật
được cần thiết ở đây là băng thông
khoảng trống (The training algorithms that determine how much tensor traffic must cross this link are developed later; the hardware fact needed here is the bandwidth gap).
30
InfiniBand: Của nó chính tính năng
cho đa-nút sự chia tỷ lệ là
RDMA (Remote Direct Memory
Access), thứ mà cho phép một
GPU trong một nút để truy cập
bộ nhớ trong một cái khác một cách trực tiếp,
việc bỏ qua máy chủ CPU (Its key feature for multi-node scaling is RDMA (Remote Direct Memory Access), which allows a GPU in one node to access memory in another directly, bypassing the host CPU). Không
có RDMA, máy chủ sự liên quan
và giao thức chi phí chung có thể
trở thành phần của gradient-
sự đồng bộ hóa đường dẫn (Without RDMA, host involvement and protocol overhead can become part of the gradient-synchronization path). RDMA
làm giảm bớt sự chi phí chung đó để mà sự
chia tỷ lệ là thường hơn bị ràng buộc
bởi thô vật lý băng thông,
cấu trúc liên kết, và tập thể sự triển khai
thay vì được quản lý-bởi-CPU
gói sự xử lý (RDMA reduces that overhead so scaling is more often constrained by raw physical bandwidth, topology, and collective implementation rather than CPU-managed packet processing).
Máy chủ-máy gia tốc dữ liệu sự di chuyển theo sau một được cấu trúc chuỗi, được hiển thị trong hình 11.13 cho một
GPU như cụ thể máy gia tốc (của nó "Bộ nhớ cho GPU" làn đường là máy gia tốc của bộ nhớ) (Host-accelerator data movement follows a structured sequence, shown in figure 11.13 for a GPU as the concrete accelerator (its “Memory for GPU” lane is the accelerator’s memory)). Trước khi
sự tính toán bắt đầu, dữ liệu được sao chép từ CPU bộ nhớ tới máy gia tốc của bộ nhớ (bước 1) (Before computation begins, data is copied from CPU memory to the accelerator’s memory (step 1)).
CPU sau đó phát hành sự thực thi các lệnh (bước 2), và máy gia tốc xử lý dữ liệu song song
(bước 3) (The CPU then issues execution instructions (step 2), and the accelerator processes the data in parallel (step 3)). Một khi sự tính toán hoàn thành, máy gia tốc ghi của nó đầu ra tới máy gia tốc bộ nhớ (
"Lưu trữ các kết quả" mũi tên), và kết quả đó được sao chép trở lại tới CPU (bước 4) (Once computation completes, the accelerator writes its output to accelerator memory (the “Store results” arrow), and that result is copied back to the CPU (step 4)). Xem xét độ trễ chi phí
ở mọi mũi tên: mỗi sự truyền tải đại diện một có tiềm năng nút thắt cổ chai thứ mà phải được quản lý để tối ưu hóa
cuối-tới-cuối hiệu suất (Consider the latency cost at every arrow: each transfer represents a potential bottleneck that must be managed to optimize end-to-end performance).
Chính Bộ nhớ (Main Memory)
CPU
Bộ nhớ cho GPU (Memory for GPU)
GPU
Chính Bộ nhớ (Main Memory)
CPU
Bộ nhớ cho GPU (Memory for GPU)
GPU
Sao chép việc xử lý dữ liệu (1) (Copy processing data (1))
Hướng dẫn sự xử lý (2) (Instruct the processing (2))
Lưu trữ các kết quả (Store results)
Sao chép kết quả (4) (Copy the result (4))
Thực thi song song trong mỗi lõi (3) (Execute parallel in each core (3))
Hình 11.13: Máy chủ-Máy gia tốc Dữ liệu Sự truyền tải: AI các khối lượng công việc yêu cầu thường xuyên dữ liệu sự di chuyển giữa CPU bộ nhớ và
các máy gia tốc (Figure 11.13: Host-Accelerator Data Transfer: AI workloads require frequent data movement between CPU memory and accelerators). Bốn tuần tự các bước của việc sao chép đầu vào dữ liệu, việc phát hành sự thực thi các lệnh, song song sự tính toán, và
việc truyền tải các kết quả mỗi cái giới thiệu có tiềm năng hiệu suất các nút thắt cổ chai (The four sequential steps of copying input data, issuing execution instructions, parallel computation, and transferring results each introduce potential performance bottlenecks).
Các chính các thách thức trong máy chủ-máy gia tốc dữ liệu sự di chuyển bao gồm độ trễ, băng thông các sự ràng buộc,
và sự đồng bộ hóa các chi phí chung (The key challenges in host-accelerator data movement include latency, bandwidth constraints, and synchronization overheads). Tính hiệu quả của ML các máy gia tốc phụ thuộc không chỉ trên của chúng tính toán
sức mạnh mà còn trên liên tục nguồn cung của dữ liệu (The efficiency of ML accelerators depends not only on their computational power but also on the continuous supply of data). Thậm chí cao-hiệu suất các GPU và các TPU
duy trì bị sử dụng dưới mức nếu dữ liệu các sự truyền tải là không hiệu quả (Even high-performance GPUs and TPUs remain underutilized if data transfers are inefficient). Máy chủ và máy gia tốc bộ nhớ tồn tại như riêng biệt
các miền, việc yêu cầu tường minh các sự truyền tải qua các kết nối liên thông chẳng hạn như PCIe, NVLink, hoặc độc quyền các liên kết (Host and accelerator memory exist as separate domains, requiring explicit transfers over interconnects such as PCIe, NVLink, or proprietary links).
Không hiệu quả dữ liệu sự di chuyển gây ra sự thực thi các sự đình trệ, việc làm sự truyền tải sự tối ưu hóa một sự ưu tiên (Ineffective data movement causes execution stalls, making transfer optimization a priority).
11.5.5.1 Nút-cấp độ kết nối liên thông cấu trúc liên kết (Node-level interconnect topology)
Để tối ưu hóa dữ liệu sự di chuyển, chúng ta phải hiểu vật lý cấu trúc liên kết của tính toán nút (To optimize data movement, we must understand the physical topology of the compute node). Một
điển hình AI máy chủ là không một phẳng lưới của được kết nối các thiết bị mà là một hệ thống phân cấp của các băng thông thứ mà thon nhỏ
khi chúng ta di chuyển ra xa từ khuôn (A typical AI server is not a flat mesh of connected devices but a hierarchy of bandwidths that tapers as we move away from the chip).
Ở nút cấp độ, ba các liên kết định nghĩa băng thông sự thon nhỏ (At node level, three links define the bandwidth taper):
1. Thiết bị-thiết bị kết nối liên thông (NVLink/Infinity Fabric): Hiện đại đa-GPU các nút sử dụng được chuyên
biệt hóa cao-tốc độ các cầu nối giống như NVLink29 để kết nối các máy gia tốc một cách trực tiếp, việc bỏ qua máy chủ
CPU (Device-device interconnect (NVLink/Infinity Fabric): Modern multi-GPU nodes use specialized high-speed bridges like NVLink29 to connect accelerators directly, bypassing the host CPU). Băng thông dao động từ 600 GB/s tới 900 GB/s trên mỗi GPU (C. NVIDIA 2020; Choquette
2023) (Bandwidth ranges from 600 GB/s to 900 GB/s per GPU (C. NVIDIA 2020; Choquette 2023)). Liên kết này quan trọng bất cứ khi nào các tensor phải di chuyển giữa các máy gia tốc bên trong một máy chủ,
bao gồm mô hình sự phân vùng, sự kích hoạt sự trao đổi, và gradient sự đồng bộ hóa trong suốt sự đào
tạo (This link matters whenever tensors must move between accelerators within one server, including model partitioning, activation exchange, and gradient synchronization during training). Phần cứng bài học cho chương này là biên giới: lưu lượng thứ mà duy trì trên máy gia tốc
vải là xa rẻ hơn so với lưu lượng thứ mà rơi lùi lại thông qua máy chủ (The hardware lesson for this chapter is the boundary: traffic that stays on the accelerator fabric is far cheaper than traffic that falls back through the host).
2. Máy chủ-thiết bị kết nối liên thông (PCIe): Liên kết giữa CPU và máy gia tốc (Host-device interconnect (PCIe): The link between the CPU and the accelerator). Băng thông
dao động từ 32 tới 64 GB/s (PCIe Gen4/Gen5) (Bandwidth ranges from 32 to 64 GB/s (PCIe Gen4/Gen5)). Liên kết này đại diện "Dữ liệu Việc tải Nút thắt cổ
chai": tất cả sự đào tạo dữ liệu phải đi ngang qua mỏng đường ống này (This link represents the “Data Loading Bottleneck”: all training data must pass through this thin pipe). Thậm chí với tám các GPU việc cung cấp 5
TB/s của tổng tính toán băng thông, hệ thống được nuôi bởi một đơn ~64 GB/s PCIe bộ chuyển mạch (Even with eight GPUs providing 5 TB/s of aggregate compute bandwidth, the system is fed by a single ~64 GB/s PCIe switch).
3. Nút-mạng kết nối liên thông (NIC): Liên kết tới bên ngoài thế giới, việc kết nối tới khác các nút (Node-network interconnect (NIC): The link to the outside world, connecting to other nodes).
Băng thông dao động từ 25 tới 50 GB/s (200 Gb/s tới 400 Gb/s Ethernet/InfiniBand30) (Bandwidth ranges from 25 to 50 GB/s (200 Gb/s to 400 Gb/s Ethernet/InfiniBand30)). Này
kết nối liên thông là đầu tiên bước từ đơn-nút phần cứng sự suy luận vào tiếp theo biên giới: quy mô (This interconnect is the first step from single-node hardware reasoning into the next frontier: scale).
Ở đây, điểm là rằng việc rời khỏi nút di chuyển lưu lượng lên một nhiều hẹp hơn và cao hơn-độ trễ
đường dẫn (Here, the point is that leaving the node moves traffic onto a much narrower and higher-latency path).

592
11.5 AI Bộ nhớ Các hệ thống (AI Memory Systems)
31
DMA (Trực tiếp Bộ nhớ
Truy cập): Một dành riêng phần
cứng đơn vị thứ mà quản lý
dữ liệu bản sao (bước 1) mà không trực
tiếp CPU sự quản lý, việc giải
phóng CPU để ngay lập tức
phát hành sự tính toán các lệnh
(bước 2) (DMA (Direct Memory Access): A dedicated hardware unit that manages the data copy (step 1) without direct CPU management, freeing the CPU to immediately issue computation commands (step 2)). Tính đồng thời này là
tới hạn: không có nó, máy gia
tốc có thể nhàn rỗi giữa tính
toán các lô, đặc biệt khi
máy chủ-tới-thiết bị sự di chuyển là
trên tới hạn đường dẫn (This concurrency is critical: without it, the accelerator can idle between compute batches, especially when host-to-device movement is on the critical path).
Những ba cấp độ này sản xuất một đặc trưng băng thông sự thon nhỏ (These three levels produce a characteristic bandwidth taper):
HBM (3350 GB/s) ≫ NVLink (900 GB/s)
≫ PCIe (64 GB/s) ≫ Mạng (50 GB/s)
Hệ thống tính hiệu quả phụ thuộc trên việc giữ dữ liệu càng cao lên hệ thống phân cấp này càng có thể (System efficiency depends on keeping data as high up this hierarchy as possible). Một khi dữ liệu
rơi tới PCIe hoặc mạng các tốc độ, nó bắt gặp một 30–100× sự làm chậm, vì vậy sự sắp đặt và việc lập lịch
các quyết định phải ngăn chặn có thể tránh được máy chủ và mạng các sự băng qua (Once data drops to PCIe or network speeds, it encounters a 30–100× slowdown, so placement and scheduling decisions must prevent avoidable host and network crossings).
Máy chủ-máy gia tốc chuỗi trong hình 11.13 bắt đầu với bước (1), nơi dữ liệu được sao chép từ
CPU bộ nhớ tới máy gia tốc bộ nhớ, như các GPU không thể một cách trực tiếp truy cập máy chủ bộ nhớ ở cao các tốc độ (The host-accelerator sequence in figure 11.13 begins with step (1), where data is copied from CPU memory to accelerator memory, as GPUs cannot directly access host memory at high speeds).
Một trực tiếp bộ nhớ truy cập (DMA)31 động cơ điển hình xử lý này sự truyền tải mà không việc tiêu thụ CPU
các chu kỳ (A direct memory access (DMA)31 engine typically handles this transfer without consuming CPU cycles). Trong bước (2), CPU phát hành sự thực thi các lệnh thông qua các API giống như CUDA, ROCm, hoặc OpenCL (In step (2), the CPU issues execution commands via APIs like CUDA, ROCm, or OpenCL).
Bước (3) liên quan song song sự thực thi trên máy gia tốc, nơi các sự đình trệ có thể xảy ra nếu dữ liệu là không có sẵn
khi được cần thiết (Step (3) involves parallel execution on the accelerator, where stalls can occur if data is not available when needed). Cuối cùng, trong bước (4), được tính toán các kết quả được sao chép trở lại tới CPU bộ nhớ cho xa hơn
sự xử lý (Finally, in step (4), computed results are copied back to CPU memory for further processing).
Độ trễ và băng thông các sự giới hạn một cách trực tiếp tác động AI các khối lượng công việc (Latency and bandwidth limitations directly impact AI workloads). PCIe-lớp máy chủ các kết nối liên thông
là điển hình nhiều chậm hơn so với một máy gia tốc của trên-gói cao-băng thông bộ nhớ, vì vậy lớn
các sự truyền tải có thể trở thành các nút thắt cổ chai, đặc biệt trong sâu sự học hỏi các tác vụ (PCIe-class host interconnects are typically much slower than an accelerator’s on-package high-bandwidth memory, so large transfers can become bottlenecks, particularly in deep learning tasks). Sự đồng bộ hóa các chi phí chung
làm phức tạp thêm vấn đề này khi sự tính toán phải đợi cho dữ liệu các sự truyền tải để hoàn thành (Synchronization overheads compound this problem when computation must wait for data transfers to complete). Hiệu quả
việc lập lịch và việc chồng lấp các sự truyền tải với sự thực thi là cần thiết để làm giảm bớt những sự không hiệu quả này (Efficient scheduling and overlapping transfers with execution are necessary to mitigate these inefficiencies).
11.5.5.2 Sự truyền tải sự tối ưu hóa (Transfer optimization)
Băng thông sự thon nhỏ được mô tả sớm hơn tạo ra một rõ ràng sự tối ưu hóa hệ thống phân cấp (The bandwidth taper described earlier creates a clear optimization hierarchy). Các nhà thực hành có
hai bổ sung các chiến lược cho việc làm giảm bớt sự truyền tải các chi phí chung: bất đồng bộ dữ liệu sự di chuyển và
được hợp nhất bộ nhớ sự trừu tượng (Practitioners have two complementary strategies for mitigating transfer overheads: asynchronous data movement and unified memory abstraction).
DMA các động cơ kích hoạt đầu tiên chiến lược bằng cách việc giảm tải dữ liệu các sự truyền tải từ CPU hoàn toàn (DMA engines enable the first strategy by offloading data transfers from the CPU entirely). Trong khi
sự tính toán tiến hành trên máy gia tốc, một DMA động cơ sao chép tiếp theo lô của sự đào tạo dữ liệu
từ máy chủ bộ nhớ vào máy gia tốc bộ nhớ trong nền (While computation proceeds on the accelerator, a DMA engine copies the next batch of training data from host memory into accelerator memory in the background). Sự chồng lấp này của sự tính toán và
sự giao tiếp là cần thiết cho việc duy trì cao sự sử dụng: không có nó, máy gia tốc có thể nhàn rỗi
trong suốt các sự truyền tải bất cứ khi nào đầu vào đường ống hoặc máy chủ liên kết trở thành tới hạn đường dẫn (This overlap of computation and communication is essential for maintaining high utilization: without it, the accelerator can idle during transfers whenever the input pipeline or host link becomes the critical path).
Được Hợp nhất Bộ nhớ cung cấp thứ hai chiến lược, việc cung cấp một đơn địa chỉ không gian có thể truy cập bởi cả
CPU và máy gia tốc (Unified Memory provides the second strategy, offering a single address space accessible by both CPU and accelerator). Thay vì việc yêu cầu tường minh các bản sao, thời gian chạy di chuyển bộ nhớ các trang theo
nhu cầu khi một trong hai bộ xử lý truy cập chúng (Rather than requiring explicit copies, the runtime migrates memory pages on demand when either processor accesses them). Lập trình mô hình đơn giản hóa một cách đáng kể (một
đơn malloc thay thế phức tạp việc tổ chức logic), nhưng giới thiệu hiệu suất sự không thể dự đoán (The programming model simplifies dramatically (a single malloc replaces complex staging logic), but introduces performance unpredictability). Trang
các sự di chuyển được kích hoạt bởi truy cập các mẫu có thể gây ra độ trễ các sự gia tăng đột biến, và nhỏ hoặc rải trực các truy cập có thể
thrash các trang qua lại qua kết nối liên thông (Page migrations triggered by access patterns can cause latency spikes, and small or scattered accesses may thrash pages back and forth across the interconnect). Cho lý do này, sản xuất sự đào tạo các khối lượng công việc
điển hình sử dụng tường minh dựa trên-DMA các sự truyền tải cho có thể dự đoán hiệu suất, trong khi Được Hợp nhất Bộ nhớ tìm thấy
của nó vị trí thích hợp trong việc tạo nguyên mẫu và các khối lượng công việc nơi sự phát triển tốc độ lớn hơn tuyệt đối thông lượng (For this reason, production training workloads typically use explicit DMA-based transfers for predictable performance, while Unified Memory finds its niche in prototyping and workloads where development speed outweighs absolute throughput).
Những các chi phí chung này (kết nối liên thông độ trễ, băng thông sự thon nhỏ, và sự đồng bộ hóa các sự chậm trễ) là không
chỉ sự triển khai các chi tiết (These overheads (interconnect latency, bandwidth taper, and synchronization delays) are not merely implementation details). Chúng một cách trực tiếp định hình cách nào thần kinh mạng các kiến trúc tương tác với
phần cứng, bởi vì khác nhau mô hình các loại tạo ra một cách đáng kể khác nhau bộ nhớ áp lực các mẫu (They directly shape how neural network architectures interact with hardware, because different model types create dramatically different memory pressure patterns).
Một tích chập lớp việc xử lý các hình ảnh trưng bày đều thuộc về không gian tính cục bộ thứ mà ánh xạ tốt tới được xếp ô gạch
việc tìm nạp trước, trong khi một transformer của sự chú ý cơ chế yêu cầu việc truy cập xa các token qua
dài các chuỗi, việc nhấn mạnh băng thông theo một cách định tính khác nhau các cách (A convolutional layer processing images exhibits regular spatial locality that maps well to tiled prefetching, while a transformer’s attention mechanism requires accessing distant tokens across long sequences, stressing bandwidth in qualitatively different ways).
11.5.6 Mô hình bộ nhớ áp lực (Model memory pressure)
Mô hình kiến trúc xác định cái nào bộ nhớ thuật ngữ ràng buộc (Model architecture determines which memory term binds). Trong khi đa lớp các perceptron (MLPs),
tích chập thần kinh các mạng (CNNs), và transformer các mạng mỗi cái yêu cầu lớn tham số các tập hợp,
của chúng riêng biệt truy cập các mẫu tạo ra khác nhau áp lực trên các trọng số, các sự kích hoạt, băng thông, và máy chủ
các sự truyền tải, vì vậy mỗi cái đòi hỏi một khác nhau máy gia tốc sự tối ưu hóa chiến lược (While multilayer perceptrons (MLPs), convolutional neural networks (CNNs), and transformer networks each require large parameter sets, their distinct access patterns create different pressure on weights, activations, bandwidth, and host transfers, so each demands a different accelerator optimization strategy).
Để làm cơ sở cho này sự phân tích, chúng ta trở lại tới Ngọn hải đăng Các mô hình được giới thiệu trong bảng 1.6: ResNet-50
đại diện CNN các khối lượng công việc với cao thuộc về không gian sự tái sử dụng, GPT-2/Llama làm ví dụ cho transformer bộ nhớ
áp lực, DLRM minh họa thưa thớt việc nhúng các lượt tra cứu thứ mà nhấn mạnh bộ nhớ các hệ thống một cách khác biệt so với
dày đặc các hoạt động, và MobileNetV2 chứng minh được tối ưu hóa-tính hiệu quả các kiến trúc với theo chiều sâu
các tích chập (To ground this analysis, we return to the Lighthouse Models introduced in table 1.6: ResNet-50 represents CNN workloads with high spatial reuse, GPT-2/Llama exemplifies transformer memory pressure, DLRM illustrates sparse embedding lookups that stress memory systems differently than dense operations, and MobileNetV2 demonstrates efficiency-optimized architectures with depthwise convolutions). Những các ví dụ này sẽ tái diễn xuyên suốt phần còn lại của chương này như chúng ta phân tích
cách nào bộ nhớ các đặc điểm dịch chuyển sang phần cứng sự sử dụng (These examples will recur throughout the remainder of this chapter as we analyze how memory characteristics translate to hardware utilization).

11. Phần cứng Sự gia tốc (Hardware Acceleration)
593
32
Sự chú ý Cơ chế (Attention Mechanism):
Được giới thiệu
tới
thần kinh
các mạng bởi Bahdanau,
Cho,
và Bengio trong 2014, sự chú ý
cho phép mỗi token để tương tác
với mọi khác token trong
đầu vào chuỗi (Introduced to neural networks by Bahdanau, Cho, and Bengio in 2014, attention allows each token to interact with every other token in the input sequence).
Phần cứng
hệ quả
là
bậc hai bộ nhớ sự phát triển (The hardware consequence is quadratic memory growth):
sự chú ý các điểm số cho một chu
ỗi của độ dài 𝑆 yêu cầu
một 𝑆×𝑆 ma trận, vì vậy việc nhân đôi
chuỗi độ dài nhân bốn
bộ nhớ sự tiêu thụ (attention scores for a sequence of length 𝑆require an 𝑆×𝑆matrix, so doubling sequence length quadruples memory consumption). Này
sự chia tỷ lệ
dẫn dắt
cả
KV-bộ nhớ cache
nút thắt cổ chai
trong
sự suy luận (xem phần 13.8.3)
và
sự phát triển
của
hiệu quả-bộ nhớ các sự thay thế
giống như FlashAttention,
thứ mà
xếp ô gạch
sự tính toán
để
tránh việc vật chất hóa đầy đủ
sự chú ý ma trận trong HBM (This scaling drives both the KV-cache bottleneck in inference (see section 13.8.3) and the development of memory-efficient alternatives like FlashAttention, which tiles the computation to avoid materializing the full attention matrix in HBM).
11.5.6.1 Đa lớp các perceptron (Multilayer perceptrons)
Các MLP, cũng được tham chiếu tới như hoàn toàn được kết nối các mạng, là trong số đơn giản nhất thần kinh các kiến trúc (MLPs, also referred to as fully connected networks, are among the simplest neural architectures).
Mỗi lớp bao gồm của một dày đặc ma trận sự nhân, việc yêu cầu mọi nơ-ron để tương tác với tất cả
các nơ-ron trong đứng trước lớp (Each layer consists of a dense matrix multiplication, requiring every neuron to interact with all neurons in the preceding layer). Điều này dẫn tới cao bộ nhớ băng thông các nhu cầu, đặc biệt cho
các trọng số, như mọi đầu vào sự kích hoạt đóng góp vào một lớn tập hợp của các sự tính toán (This results in high memory bandwidth demands, particularly for weights, as every input activation contributes to a large set of computations).
Từ một bộ nhớ góc nhìn, các MLP dựa trên lớn, dày đặc trọng số các ma trận thứ mà thường xuyên vượt quá
trên-chip bộ nhớ khả năng, việc đòi hỏi ngoài-chip bộ nhớ các truy cập (From a memory perspective, MLPs rely on large, dense weight matrices that frequently exceed on-chip memory capacity, necessitating off-chip memory accesses). Vì các máy gia tốc không thể một cách trực tiếp
truy cập máy chủ bộ nhớ ở cao tốc độ, dữ liệu các sự truyền tải phải được quản lý một cách tường minh thông qua các kết nối liên thông chẳng hạn
như PCIe hoặc NVLink (Since accelerators cannot directly access host memory at high speed, data transfers must be explicitly managed via interconnects such as PCIe or NVLink). Những các sự truyền tải này giới thiệu độ trễ và tiêu thụ băng thông, việc ảnh hưởng sự thực thi
tính hiệu quả (These transfers introduce latency and consume bandwidth, affecting execution efficiency).
Mặc dù của chúng nặng-băng thông bản chất, các MLP trưng bày đều và có thể dự đoán bộ nhớ truy cập
các mẫu, việc làm chúng có thể chịu được tới các sự tối ưu hóa chẳng hạn như việc tìm nạp trước và việc truyền phát bộ nhớ
các truy cập (Despite their bandwidth-heavy nature, MLPs exhibit regular and predictable memory access patterns, making them amenable to optimizations such as prefetching and streaming memory accesses). Dành riêng AI các máy gia tốc làm giảm bớt truyền tải chi phí chung bằng cách việc tổ chức trọng số các ma trận trong nhanh
SRAM các bộ nhớ cache và việc chồng lấp dữ liệu sự di chuyển với sự tính toán thông qua trực tiếp bộ nhớ truy cập
các động cơ, việc làm giảm bớt sự thực thi các sự đình trệ (Dedicated AI accelerators mitigate transfer overhead by staging weight matrices in fast SRAM caches and overlapping data movement with computation through direct memory access engines, reducing execution stalls). Những các sự tối ưu hóa này cho phép các máy gia tốc để duy trì cao thông lượng
thậm chí khi việc xử lý lớn tham số các tập hợp (Chen, Emer, et al. 2017) (These optimizations allow accelerators to sustain high throughput even when handling large parameter sets (Chen, Emer, et al. 2017)).
11.5.6.2 Tích chập thần kinh các mạng (Convolutional neural networks)
Tích chập Thần kinh Các mạng (CNNs) là rộng rãi được sử dụng trong hình ảnh sự xử lý và máy tính thị giác
các tác vụ (Convolutional Neural Networks (CNNs) are widely used in image processing and computer vision tasks). Không giống các MLP, thứ mà yêu cầu dày đặc ma trận các phép nhân, các CNN xử lý đầu vào đặc trưng các bản đồ
việc sử dụng nhỏ bộ lọc các hạt nhân thứ mà trượt qua hình ảnh (Unlike MLPs, which require dense matrix multiplications, CNNs process input feature maps using small filter kernels that slide across the image). Được cục bộ hóa tính toán cấu trúc này dẫn tới
cao thuộc về không gian dữ liệu sự tái sử dụng, nơi cùng đầu vào các pixel đóng góp vào nhiều các tích chập (This localized computation structure results in high spatial data reuse, where the same input pixels contribute to multiple convolutions).
CNN các máy gia tốc hưởng lợi từ trên-chip bộ nhớ các sự tối ưu hóa, như tích chập các bộ lọc trưng bày
rộng rãi sự tái sử dụng, việc cho phép các trọng số để được lưu trữ trong nhanh cục bộ SRAM thay vì thường xuyên việc truy cập
ngoài-chip bộ nhớ (CNN accelerators benefit from on-chip memory optimizations, as convolution filters exhibit extensive reuse, allowing weights to be stored in fast local SRAM instead of frequently accessing off-chip memory). Tuy nhiên, sự kích hoạt các bản đồ yêu cầu cẩn thận sự quản lý do kích thước của chúng (However, activation maps require careful management due to their size). Vì
việc truy cập chính bộ nhớ qua các kết nối liên thông giống như PCIe giới thiệu độ trễ và băng thông các nút thắt cổ chai,
CNN các máy gia tốc triển khai việc xếp ô gạch các kỹ thuật để chia đặc trưng các bản đồ thành nhỏ hơn các vùng thứ mà vừa bên trong
trên-chip các bộ đệm (Since accessing main memory over interconnects like PCIe introduces latency and bandwidth bottlenecks, CNN accelerators employ tiling techniques to divide feature maps into smaller regions that fit within on-chip buffers). Điều này tối thiểu hóa tốn kém bên ngoài bộ nhớ các sự truyền tải, việc cải thiện tổng thể tính hiệu quả (Chen,
Emer, et al. 2017) (This minimizes costly external memory transfers, improving overall efficiency (Chen, Emer, et al. 2017)).
Trong khi CNN các khối lượng công việc là nhiều hơn hiệu quả-bộ nhớ so với các MLP, việc quản lý trung gian các sự kích hoạt
duy trì một thách thức (While CNN workloads are more memory-efficient than MLPs, managing intermediate activations remains a challenge). Các máy gia tốc sử dụng phân cấp việc lưu bộ nhớ cache các chiến lược và DMA các động cơ để tối ưu hóa
bộ nhớ sự di chuyển, việc đảm bảo rằng các sự tính toán là không bị đình trệ bởi không hiệu quả máy chủ-máy gia tốc dữ liệu
các sự truyền tải (Accelerators use hierarchical caching strategies and DMA engines to optimize memory movement, ensuring that computations are not stalled by inefficient host-accelerator data transfers). Những bộ nhớ các sự tối ưu hóa này giúp CNN các máy gia tốc duy trì cao thông lượng bằng cách việc làm giảm
bớt sự phụ thuộc trên ngoài-chip bộ nhớ băng thông (These memory optimizations help CNN accelerators maintain high throughput by reducing reliance on off-chip memory bandwidth). Tiên phong các kiến trúc giống như Eyeriss đã giới thiệu
hàng-tính cố định các dữ liệu luồng để tối đa hóa dữ liệu sự tái sử dụng cho tích chập các khối lượng công việc (Chen, Krishna, et
al. 2017) (Pioneering architectures like Eyeriss introduced row-stationary dataflows to maximize data reuse for convolutional workloads (Chen, Krishna, et al. 2017)). Hàng-tính cố định là một đặc thù-tích chập lai trong rộng hơn dữ liệu luồng phân loại của
phần 11.8: nó giữ các hàng và một phần các tổng cục bộ khi mẫu đó mang lại tốt hơn sự tái sử dụng so với một hoàn toàn
trọng số-, đầu vào-, hoặc đầu ra-tính cố định sự ánh xạ (Row-stationary is a convolution-specific hybrid in the broader dataflow taxonomy of section 11.8: it keeps rows and partial sums local when that pattern gives better reuse than a purely weight-, input-, or output-stationary mapping).
11.5.6.3 Transformer các mạng (Transformer networks)
Transformer các kiến trúc được giới thiệu trong phần 6.6 đã trở thành thống trị kiến trúc
cho tự nhiên ngôn ngữ sự xử lý và là ngày càng được sử dụng trong khác các miền chẳng hạn như thị giác và
tiếng nói sự nhận dạng (The transformer architectures introduced in section 6.6 have become the dominant architecture for natural language processing and are increasingly used in other domains such as vision and speech recognition). Không giống các CNN, thứ mà dựa trên cục bộ các sự tính toán, các transformer thực hiện toàn cầu
sự chú ý32 các cơ chế, nơi mỗi token trong một đầu vào chuỗi có thể tương tác với tất cả khác các token (Unlike CNNs, which rely on local computations, transformers perform global attention32 mechanisms, where each token in an input sequence can interact with all other tokens).
Những các mô hình này là đặc biệt thách thức cho các máy gia tốc bởi vì toàn cầu token sự tương tác tạo ra
lớn sự chú ý trạng thái trong khi GPT-3-quy mô ngôn ngữ các mô hình (Brown et al. 2020) có thể vượt quá trên-chip
bộ nhớ khả năng thông qua tuyệt đối tham số số đếm (These models are particularly challenging for accelerators because global token interaction creates large attention state while GPT-3-scale language models (Brown et al. 2020) can exceed on-chip memory capacity through sheer parameter count). Như một kết quả, thường xuyên sự di chuyển giữa HBM,
các bộ nhớ cache, và tính toán các đơn vị tạo ra đáng kể độ trễ và băng thông áp lực (As a result, frequent movement between HBM, caches, and compute units creates substantial latency and bandwidth pressure). Nếu mô hình tràn
vượt ra ngoài máy gia tốc bộ nhớ hoặc sử dụng máy chủ sự giảm tải, PCIe hoặc NVLink các sự truyền tải cộng một cái khác nút thắt cổ chai (If the model spills beyond accelerator memory or uses host offload, PCIe or NVLink transfers add another bottleneck).
Được Hợp nhất Bộ nhớ các kiến trúc có thể làm giảm bớt một số lập trình độ phức tạp bằng cách việc xử lý sự di chuyển
giữa máy chủ và thiết bị bộ nhớ tại thời gian chạy, nhưng chúng giới thiệu bổ sung độ trễ khi trang
các sự di chuyển xảy ra một cách không thể dự đoán (Unified Memory architectures can mitigate some programming complexity by handling movement between host and device memory at runtime, but they introduce additional latency when page migrations occur unpredictably). Những các áp lực này làm cao-băng thông bộ nhớ, tensor việc xếp ô gạch, và
bộ nhớ sự phân vùng trung tâm máy gia tốc thiết kế các mối quan tâm cho transformer các khối lượng công việc (These pressures make high-bandwidth memory, tensor tiling, and memory partitioning central accelerator design concerns for transformer workloads).
Sự chú ý việc lưu bộ nhớ cache các cơ chế và được chuyên biệt hóa tensor các bố cục xa hơn làm giảm bớt dư thừa bộ nhớ
các lượt tìm nạp, việc cải thiện sự thực thi tính hiệu quả (Attention caching mechanisms and specialized tensor layouts further reduce redundant memory fetches, improving execution efficiency). Cho trước băng thông các sự giới hạn của truyền thống các kết nối liên thông,

594
11.6 Đường mái nhà Mô hình (Roofline Model)
Thấp số học cường độ ghim
khối lượng công việc trong bị ràng buộc-bởi-bộ nhớ
chế độ (Low arithmetic intensity pins the workload in the memory-bound regime).
33
Đường mái nhà Mô hình (Roofline Model):
Được giới
thiệu bởi Williams et al.
(2009) tại UC Berkeley, việc xây
dựng trên sớm hơn I/O độ phức tạp
công việc từ những năm 1980 (Introduced by Williams et al. (2009) at UC Berkeley, building on earlier I/O complexity work from the 1980s). Của họ
cụ thể đóng góp là việc làm
tính toán so với băng
thông sự đánh đổi trực quan và
có thể hành động: đặc trưng
đường mái nhà biểu đồ ngay lập tức tiết
lộ liệu một hạt nhân là bị ràng buộc
bởi tính toán (việc chạm phẳng
trần) hoặc bị ràng buộc bởi bộ nhớ
(việc chạm dốc băng thông
đường) và định lượng khoảng trống tới
phần cứng các giới hạn (Their specific contribution was making the compute vs. bandwidth trade-off visual and actionable: the characteristic roofline plot immediately reveals whether a kernel is compute bound (hitting the flat ceiling) or memory bound (hitting the sloped bandwidth line) and quantifies the gap to hardware limits). Một hạt nhân hoạt
động ở chỉ 50 phần trăm của của nó
trần có một rõ ràng 2× sự sử dụng
khoảng trống để đóng, việc làm điều này
tiêu chuẩn chẩn đoán công cụ
cho máy gia tốc sự tối ưu hóa (A kernel operating at only 50 percent of its ceiling has a clear 2× utilization gap to close, making this the standard diagnostic tool for accelerator optimization).
Được kích hoạt-bởi-NVLink các kiến trúc cung cấp rõ ràng các lợi thế cho quy mô-lớn transformer sự đào tạo, như chúng
cung cấp cao hơn thông lượng và thấp hơn độ trễ so với PCIe (NVLink-enabled architectures offer clear advantages for large-scale transformer training, as they provide higher throughput and lower latency compared to PCIe). Dựa trên-DMA bất đồng bộ bộ nhớ
các sự truyền tải kích hoạt việc chồng lấp sự tính toán với dữ liệu sự di chuyển, việc làm giảm bớt sự thực thi các sự đình trệ (Narayanan
et al. 2021) (DMA-based asynchronous memory transfers enable overlapping computation with data movement, reducing execution stalls (Narayanan et al. 2021)).
11.5.7 Máy gia tốc thiết kế các hệ ý (Accelerator design implications)
Đa dạng bộ nhớ các yêu cầu của các MLP, các CNN, và các transformer làm nổi bật nhu cầu cho
cụ thể-cho-khối lượng công việc máy gia tốc thiết kế (The diverse memory requirements of MLPs, CNNs, and transformers highlight the need for workload-specific accelerator design). Bảng 11.11 tiết lộ cách nào bộ nhớ truy cập các mẫu thay đổi một cách đáng
kể qua mô hình các loại (Table 11.11 reveals how memory access patterns vary dramatically across model types).
Bảng 11.11: ML Mô hình Bộ nhớ Truy cập: Khác nhau máy học các mô hình trưng bày riêng biệt bộ nhớ truy cập các mẫu và
các nút thắt cổ chai do các sự biến thiên trong trọng số kích thước, sự kích hoạt sự tái sử dụng, và dữ liệu sự di chuyển (Table 11.11: ML Model Memory Access: Different machine learning models exhibit distinct memory access patterns and bottlenecks due to variations in weight size, activation reuse, and data movement). Tiêu chuẩn dày đặc các transformer đòi hỏi cao
băng thông và khả năng bởi vì lớn các trọng số, KV các bộ nhớ cache, và sự chú ý lưu lượng thống trị bộ nhớ áp lực; thưa thớt MoE hoặc
được cắt tỉa các biến thể cộng xa hơn định tuyến và sự thưa thớt các sự xem xét (Standard dense transformers demand high bandwidth and capacity because large weights, KV caches, and attention traffic dominate memory pressure; sparse MoE or pruned variants add further routing and sparsity considerations). Các CNN hưởng lợi từ thuộc về không gian tính cục bộ và cao sự kích hoạt sự tái sử dụng,
việc làm giảm bớt bộ nhớ áp lực (CNNs benefit from spatial locality and high activation reuse, reducing memory pressure).
Mô hình Loại (Model Type)
Trọng số Kích thước (Weight Size)
Sự kích hoạt Sự tái sử dụng (Activation Reuse)
Bộ nhớ Truy cập Mẫu (Memory Access Pattern)
Chính Nút thắt cổ chai (Primary Bottleneck)
MLP (Dày đặc) (MLP (Dense))
Lớn, dày đặc (Large, dense)
Thấp (Low)
Đều, tuần tự
(được truyền phát) (Regular, sequential (streamed))
Băng thông
(ngoài-chip) (Bandwidth (off-chip))
CNN
Nhỏ, được tái sử dụng (Small, reused)
Cao (High)
Thuộc về không gian tính cục bộ (Spatial locality)
Đặc trưng bản đồ
sự di chuyển (Feature map movement)
Transformer
Lớn, thường dày đặc; thưa thớt
trong MoE/được cắt tỉa các biến thể (Large, usually dense; sparse in MoE/pruned variants)
Thấp-tới-trung bình (Low-to-medium)
Hầu hết đều GEMM cộng
KV-bộ nhớ cache/sự chú ý lưu lượng (Mostly regular GEMM plus KV-cache/attention traffic)
Bộ nhớ khả năng +
băng thông (Memory capacity + bandwidth)
Mỗi mô hình loại trình bày độc nhất các thách thức thứ mà một cách trực tiếp tác động máy gia tốc thiết kế (Each model type presents unique challenges that directly impact accelerator design). Các MLP hưởng lợi
từ nhanh truyền phát truy cập tới dày đặc trọng số các ma trận, việc làm bộ nhớ băng thông một tới hạn yếu tố trong
hiệu suất, đặc biệt khi việc truyền tải lớn các trọng số từ máy chủ bộ nhớ tới máy gia tốc bộ nhớ (MLPs benefit from fast streaming access to dense weight matrices, making memory bandwidth a critical factor in performance, especially when transferring large weights from host memory to accelerator memory).
Các CNN, với của chúng cao sự kích hoạt sự tái sử dụng và được cấu trúc bộ nhớ truy cập các mẫu, có thể khai thác trên-chip
việc lưu bộ nhớ cache và việc xếp ô gạch các chiến lược để tối thiểu hóa ngoài-chip bộ nhớ các sự truyền tải (CNNs, with their high activation reuse and structured memory access patterns, can exploit on-chip caching and tiling strategies to minimize off-chip memory transfers). Các Transformer, tuy nhiên, áp đặt
nặng các nhu cầu trên cả băng thông và khả năng: sự chú ý các cơ chế yêu cầu thường xuyên truy cập tới
lớn khóa-giá trị các ma trận, việc tạo ra cao kết nối liên thông lưu lượng và đáng kể bộ nhớ áp lực (Transformers, however, impose heavy demands on both bandwidth and capacity: attention mechanisms require frequent access to large key-value matrices, generating high interconnect traffic and substantial memory pressure).
Để giải quyết những các thách thức này, hiện đại AI các máy gia tốc kết hợp đa-tầng bộ nhớ các hệ thống phân cấp
thứ mà cân bằng tốc độ, khả năng, và năng lượng tính hiệu quả (To address these challenges, modern AI accelerators incorporate multi-tier memory hierarchies that balance speed, capacity, and energy efficiency). Trên-chip SRAM các bộ nhớ cache và bộ nhớ nháp các bộ nhớ
lưu trữ thường xuyên được truy cập dữ liệu, trong khi cao-băng thông bên ngoài bộ nhớ cung cấp tính có thể chia tỷ lệ cho lớn
các mô hình (On-chip SRAM caches and scratchpad memories store frequently accessed data, while high-bandwidth external memory provides scalability for large models). Hiệu quả các kết nối liên thông, chẳng hạn như NVLink, giúp làm giảm bớt máy chủ-máy gia tốc truyền tải các nút thắt cổ chai,
đặc biệt trong transformer các khối lượng công việc nơi bộ nhớ sự di chuyển các sự ràng buộc có thể thống trị sự thực thi
thời gian (Efficient interconnects, such as NVLink, help alleviate host-accelerator transfer bottlenecks, particularly in transformer workloads where memory movement constraints can dominate execution time).
Như ML các khối lượng công việc tiếp tục để phát triển trong độ phức tạp, bộ nhớ tính hiệu quả trở nên cũng tới hạn như thô
tính toán sức mạnh (As ML workloads continue to grow in complexity, memory efficiency becomes as critical as raw compute power). Sự phân tích tiết lộ cách nào bộ nhớ các hệ thống thống trị máy gia tốc hiệu suất:
DRAM truy cập có 100× hoặc cao hơn năng lượng chi phí so với trên-chip số học, một cách cẩn thận được cấu trúc bộ nhớ
các hệ thống phân cấp có thể cải thiện hiệu quả băng thông một cách đáng kể, và khác nhau thần kinh mạng các kiến trúc
tạo ra riêng biệt bộ nhớ áp lực các mẫu (The analysis reveals how memory systems dominate accelerator performance: DRAM access has 100× or higher energy cost than on-chip arithmetic, carefully structured memory hierarchies can improve effective bandwidth substantially, and different neural network architectures create distinct memory pressure patterns). Những các sự ràng buộc này (băng thông các sự giới hạn, năng lượng các chi phí,
và sự giao tiếp các chi phí chung) xác định liệu lý thuyết tính toán các khả năng chuyển đổi
vào thế giới-thực hiệu suất (These constraints (bandwidth limitations, energy costs, and communication overheads) determine whether theoretical computational capabilities translate into real-world performance). Phần còn lại câu hỏi là liệu một cụ thể khối lượng công việc là bị giới hạn bởi
tính toán hoặc bộ nhớ trên một cho trước máy gia tốc (The remaining question is whether a specific workload is limited by compute or memory on a given accelerator). Bộ nhớ bức tường sự phân tích thiết lập tại sao bộ nhớ
quan trọng, nhưng các nhà thực hành cần một định lượng bộ khung để dự đoán cái nào các hoạt động sẽ làm nút thắt cổ chai
trên một cụ thể phần cứng cấu hình (The memory wall analysis establishes why memory matters, but practitioners need a quantitative framework to predict which operations will bottleneck on a specific hardware configuration). Không có một như vậy bộ khung, sự tối ưu hóa trở thành sự phỏng đoán:
các kỹ sư có thể dành các tuần việc tối ưu hóa tính toán thông lượng cho một hoạt động thứ mà đã bị ràng buộc-bởi-bộ nhớ
tất cả dọc theo (Without such a framework, optimization becomes guesswork: engineers might spend weeks optimizing compute throughput for an operation that was memory-bound all along).
11.6 Đường mái nhà Mô hình (Roofline Model)
Đường mái nhà mô hình trả lời câu hỏi này bằng cách việc lập biểu đồ số học cường độ chống lại có thể đạt được hiệu
suất, việc tiết lộ liệu mỗi hoạt động chạm một tính toán trần hoặc một bộ nhớ băng thông trần (The roofline model answers this question by plotting arithmetic intensity against attainable performance, revealing whether each operation hits a compute ceiling or a memory bandwidth ceiling).
Thay vì việc dựa trên trên đỉnh FLOP/s các con số, thứ mà phản ánh tiếp thị thay vì có thể đạt được thông
lượng, đường mái nhà mô hình ánh xạ một khối lượng công việc lên một cụ thể phần cứng nền tảng và phơi bày ràng buộc
sự ràng buộc (Rather than relying on peak FLOP/s figures, which reflect marketing rather than achievable throughput, the roofline model maps a workload onto a specific hardware platform and exposes the binding constraint).

11. Phần cứng Sự gia tốc (Hardware Acceleration)
595
Đường mái nhà mô hình33 (Williams et al. 2009) cung cấp tiêu chuẩn bộ khung cho việc hiểu
liệu các khối lượng công việc là bị ràng buộc bởi tính toán hoặc bị ràng buộc bởi bộ nhớ, một cách trực tiếp việc kết nối bộ nhớ bức tường
cuộc thảo luận tới thực hành hiệu suất sự phân tích (The roofline model33 (Williams et al. 2009) provides the standard framework for understanding whether workloads are compute bound or memory bound, directly connecting the memory wall discussion to practical performance analysis). Mô hình này kích hoạt định lượng sự lập luận về
máy gia tốc sự sử dụng và dẫn dắt sự tối ưu hóa các quyết định (This model enables quantitative reasoning about accelerator utilization and guides optimization decisions).
Hiệu suất là bị giới hạn bởi hai các trần, như phương trình 11.2 chính thức hóa (Performance is bounded by two ceilings, as equation 11.2 formalizes). Ở đây, có thể đạt được hiệu suất
𝑅attain và đỉnh tính toán 𝑅peak là trong FLOP/s (thường được báo cáo như TFLOP/s), đỉnh băng thông BW là
trong bytes/s (thường TB/s), và số học cường độ 𝐼 là trong FLOP/byte (Here, attainable performance 𝑅attain and peak compute 𝑅peak are in FLOP/s (often reported as TFLOP/s), peak bandwidth BW is in bytes/s (often TB/s), and arithmetic intensity 𝐼is in FLOP/byte):
𝑅attain = min(𝑅peak, BW × 𝐼)
(11.2)
Chính số liệu thứ mà xác định cái nào trần một khối lượng công việc chạm là số học cường độ, tỷ lệ của
sự tính toán tới bộ nhớ lưu lượng (The key metric that determines which ceiling a workload hits is arithmetic intensity, the ratio of computation to memory traffic).
Định nghĩa 11.5 (Definition 11.5): Số học cường độ (Arithmetic intensity)
Số học Cường độ là tỷ lệ của dấu phẩy-động các hoạt động tới các byte của bộ nhớ lưu lượng cho một
cho trước sự tính toán (FLOP/byte), việc xác định liệu khối lượng công việc là bị giới hạn bởi tính toán
thông lượng (𝑅peak) hoặc bộ nhớ băng thông (BW) trên một cho trước máy gia tốc (Arithmetic Intensity is the ratio of floating-point operations to bytes of memory traffic for a given computation (FLOP/byte), determining whether the workload is limited by compute throughput (𝑅peak) or memory bandwidth (BW) on a given accelerator).
1. Ý nghĩa (Significance): Cường độ ngưỡng việc phân tách bị ràng buộc-bởi-bộ nhớ từ bị ràng buộc-bởi-tính toán
các chế độ là đường mái nhà đỉnh điểm: 𝑅peak/BW (The intensity threshold separating memory-bound from compute-bound regimes is the roofline ridge point: 𝑅peak/BW). Cho một A100 (312 TFLOP/s FP16/BF16, 2.04
TB/s), đỉnh điểm là xấp xỉ 153 FLOP/byte (For an A100 (312 TFLOP/s FP16/BF16, 2.04 TB/s), the ridge point is roughly 153 FLOP/byte). Ma trận các phép nhân xung quanh 100–200
FLOP/byte đứng giang chân ngưỡng đó, trong khi một lớn hơn được xếp ô gạch-tốt 1024 × 1024 ma trận nhân
đạt tới khoảng 341.3 FLOP/byte và là bị ràng buộc bởi tính toán; một theo điểm ReLU thực hiện
xung quanh 0.125 FLOP/byte dưới một đọc-cộng-ghi lưu lượng mô hình (bị ràng buộc bởi bộ nhớ), việc đặt
những các hoạt động này trong khác nhau sự tối ưu hóa các chế độ trên cùng phần cứng (Matrix multiplications around 100–200 FLOP/byte straddle that threshold, while a larger well-tiled 1024 × 1024 matrix multiply reaches about 341.3 FLOP/byte and is compute bound; a pointwise ReLU performs around 0.125 FLOP/byte under a read-plus-write traffic model (memory bound), placing these operations in different optimization regimes on the same hardware).
2. Sự phân biệt (Distinction): Không giống tổng các FLOP (một số đếm của các hoạt động), số học cường độ là một tỷ lệ thứ mà
đặc trưng hóa hình dạng của một khối lượng công việc của phần cứng nhu cầu (Unlike total FLOPs (a count of operations), arithmetic intensity is a ratio that characterizes the shape of a workload’s hardware demand). Hai các hạt nhân với giống hệt
các FLOP nhưng khác nhau bộ nhớ truy cập các mẫu có khác nhau số học các cường độ và sẽ
bị làm nút thắt cổ chai bởi khác nhau phần cứng các tài nguyên (Two kernels with identical FLOPs but different memory access patterns have different arithmetic intensities and will be bottlenecked by different hardware resources).
3. Phổ biến cạm bẫy (Common pitfall): Một thường xuyên quan niệm sai lầm là rằng số học cường độ là một cố định thuộc tính
của một hoạt động (A frequent misconception is that arithmetic intensity is a fixed property of an operation). Trong thực tế, nó phụ thuộc trên sự triển khai các chi tiết: một ngây thơ ma trận-nhân
thứ mà tải lại các toán hạng từ DRAM cho mỗi đầu ra phần tử có thấp số học cường độ; một
được khối hóa (được xếp ô gạch) sự triển khai thứ mà tái sử dụng dữ liệu từ nhanh SRAM đạt được cao số học
cường độ—cùng toán học hoạt động, các bậc của độ lớn cách xa nhau trong phần cứng
tính hiệu quả (In practice, it depends on implementation details: a naive matrix-multiply that reloads operands from DRAM for each output element has low arithmetic intensity; a blocked (tiled) implementation that reuses data from fast SRAM achieves high arithmetic intensity—the same mathematical operation, orders of magnitude apart in hardware efficiency).
Số học cường độ (AI) đo lường dấu phẩy-động các hoạt động trên mỗi byte của bộ nhớ lưu lượng (Arithmetic intensity (AI) measures floating-point operations per byte of memory traffic). Số
hoạt động số đếm 𝑂 là một không thứ nguyên số đếm của dấu phẩy-động các hoạt động và dữ liệu thể tích 𝐷vol là
được đo lường trong các byte, vì vậy AI có các đơn vị của FLOP/byte, được định nghĩa bởi phương trình 11.3 (The operation count 𝑂is a dimensionless count of floating-point operations and the data volume 𝐷vol is measured in bytes, so AI has units of FLOP/byte, defined by equation 11.3):
𝐼= 𝑂 / 𝐷vol
(11.3)
Đường mái nhà sự trực quan hóa hiển thị hiệu suất (TFLOP/s) trên dọc trục và số học
cường độ (FLOP/byte) trên ngang trục (The roofline visualization shows performance (TFLOP/s) on the vertical axis and arithmetic intensity (FLOP/byte) on the horizontal axis). Ở thấp số học cường độ, hiệu suất tăng
một cách tuyến tính với cường độ (bị ràng buộc-bởi-bộ nhớ vùng) (At low arithmetic intensity, performance increases linearly with intensity (memory-bound region)). Phía trên đỉnh điểm, hiệu suất bão hòa
ở đỉnh tính toán (bị ràng buộc-bởi-tính toán vùng) (Above the ridge point, performance saturates at peak compute (compute-bound region)). Phần A.5.1 ánh xạ mỗi chế độ tới các sự tối ưu hóa
thứ mà mang lại kết quả và những cái thứ mà lãng phí nỗ lực, để mà việc phân loại một khối lượng công việc như bị ràng buộc-bởi-bộ nhớ hoặc
bị ràng buộc-bởi-tính toán nói cho kỹ sư một cách trực tiếp liệu một nhanh hơn máy gia tốc hoặc nhiều hơn băng thông là ràng buộc
sự đầu tư (Section A.5.1 maps each regime to the optimizations that pay off and the ones that waste effort, so that classifying a workload as memory-bound or compute-bound tells the engineer directly whether a faster accelerator or more bandwidth is the binding investment).
11.6.1 Phần cứng đỉnh các điểm (Hardware ridge points)
Đỉnh điểm, phần cứng sự cân bằng 𝐼ridge được thiết lập trong phần 11.5.2, là số học-cường độ
ngưỡng tại đó một máy gia tốc chuyển từ bị ràng buộc-bởi-bộ nhớ sang bị ràng buộc-bởi-tính toán (The ridge point, the hardware balance 𝐼ridge established in section 11.5.2, is the arithmetic-intensity threshold at which an accelerator turns from memory-bound to compute-bound). Bảng 11.12 định
lượng cách nào khác nhau các máy gia tốc trưng bày riêng biệt các đặc điểm dựa trên của chúng tính toán-tới-băng thông
các tỷ lệ (Table 11.12 quantifies how different accelerators exhibit distinct characteristics based on their compute-to-bandwidth ratios):

596
11.6 Đường mái nhà Mô hình (Roofline Model)
Bảng 11.12: Phần cứng Đỉnh Các điểm: Mang tính đại diện đỉnh điểm các phạm vi cho khác nhau máy gia tốc các thế hệ, được xác định bởi
của chúng tính toán-tới-băng thông các tỷ lệ (Table 11.12: Hardware Ridge Points: Representative ridge point ranges for different accelerator generations, determined by their compute-to-bandwidth ratios). Các giá trị được hiển thị là các bậc-của-độ lớn các sự xấp xỉ; thực tế đỉnh các điểm thay đổi bởi độ chính xác
chế độ và cụ thể SKU (Values shown are order-of-magnitude approximations; actual ridge points vary by precision mode and specific SKU). Cao hơn đỉnh các điểm yêu cầu cao hơn FLOP/byte cường độ để đạt được đỉnh sự sử dụng (Higher ridge points require higher FLOP/byte intensity to achieve peak utilization).
Máy gia tốc (Accelerator)
Đỉnh FP16 (Peak FP16)
Băng thông (Bandwidth)
Đỉnh Điểm (Ridge Point)
GPU (2017-kỷ nguyên) (GPU (2017-era))
∼10^2 TFLOP/s
∼10^3 GB/s
∼10^2 FLOP/byte
GPU (2020-kỷ nguyên) (GPU (2020-era))
∼10^2 TFLOP/s
∼10^3 GB/s tới ∼10^0 TB/s (∼103 GB/s to ∼100 TB/s)
∼10^2 FLOP/byte
GPU (2023-kỷ nguyên) (GPU (2023-era))
∼10^3 TFLOP/s
một vài TB/s (a few TB/s)
∼10^2 FLOP/byte
TPU-lớp (2023-kỷ nguyên) (TPU-class (2023-era))
∼10^2 tới ∼10^3 TFLOP/s (∼102 to ∼103 TFLOP/s)
∼1 TB/s
∼10^2 FLOP/byte
Những đỉnh điểm các giá trị này tiết lộ một đáng ngạc nhiên xu hướng: như phần cứng đã trở nên mạnh mẽ hơn,
việc giữ nó hoàn toàn trong sự sử dụng đã trở nên khó hơn (These ridge point values reveal a surprising trend: as hardware has become more powerful, keeping it fully in use has become harder). Một đỉnh-điểm sự so sánh làm xu hướng đó cụ thể (A ridge-point comparison makes that trend concrete).
Giấy ăn Toán học 11.3 (Napkin Math 11.3): Sự sử dụng khoảng trống (The utilization gap)
Sự sử dụng vật lý: Tại sao nó là khó hơn để đạt được 100 phần trăm sự sử dụng trên một H100 so với một V100? (The utilization physics: Why is it harder to get 100 percent utilization on an H100 than a V100?)
Số liệu (Metric): Đỉnh điểm 𝐼ridge = 𝑅peak/BW (FLOP/byte) từ phần 11.5.2: bao nhiêu toán học
các hoạt động phần cứng phải thực hiện cho mỗi byte của dữ liệu được tải để giữ tính toán các đơn vị
bận rộn (The ridge point 𝐼ridge = 𝑅peak/BW (FLOP/byte) from section 11.5.2: how many math operations the hardware must perform for every byte of data loaded to keep the compute units busy).
Sự tiến hóa (Evolution):
• V100 (2017): 125 TFLOP/s / 0.9 TB/s ≈ 138.9 FLOP/byte.
• A100 (2020): 312 TFLOP/s / 2.04 TB/s ≈ 153 FLOP/byte.
• H100 (2023): 989 TFLOP/s / 3.35 TB/s ≈ 295.2 FLOP/byte.
Các hệ thống sự thấu hiểu (Systems insight): "Thanh chắn" cho tính toán cường độ đã nhân đôi (The “bar” for compute intensity has doubled). Một thuật toán với 𝐼 = 200
FLOP/byte đã bị ràng buộc bởi tính toán (tốt) trên A100 nhưng là bị ràng buộc bởi băng thông (tệ) trên H100 (An algorithm with 𝐼= 200 FLOP/byte was compute-bound (good) on A100 but is bandwidth-bound (bad) on H100). Điều này
giải thích tại sao "di sản" mã thường nhìn thấy chỉ 1.6× phần tăng tốc trên H100 (băng thông tỷ lệ) thay vì
được quảng cáo 3.2× (FLOPs tỷ lệ) (This explains why “legacy” code often sees only 1.6× speedup on H100 (bandwidth ratio) instead of the advertised 3.2× (FLOPs ratio)).
Thực tế các ví dụ (Practical examples): Một tiêu chuẩn ReLU thực hiện 1 hoạt động cho mỗi 8 bytes (0.125 FLOP/byte),
việc đặt nó 2,361.8× bên dưới H100 đường mái nhà (A standard ReLU performs 1 operation for every 8 bytes (0.125 FLOP/byte), placing it 2,361.8× below the H100 roofline). Một được xếp ô gạch-tốt 1024 × 1024 dày đặc MatMul đạt tới
khoảng 341.3 FLOP/byte, việc làm nó bị ràng buộc bởi tính toán thậm chí trên H100 (A well-tiled 1024 × 1024 dense MatMul reaches about 341.3 FLOP/byte, making it compute bound even on H100). Hầu hết các hoạt động rơi ngắn của
đỉnh điểm, thứ mà là tại sao hạt nhân sự hợp nhất là quan trọng nhất sự tối ưu hóa, như được khám phá trong
phần 11.8.1.3 (Most operations fall short of the ridge point, which is why kernel fusion is the most important optimization, as explored in section 11.8.1.3).
Theo chiều sâu tích chập, việc nhúng lượt tra cứu, LayerNorm, và softmax là hữu dụng thấp-cường độ
tham chiếu các điểm bởi vì chúng dành nhiều hơn thời gian việc di chuyển các byte so với việc làm số học (Depthwise convolution, embedding lookup, LayerNorm, and softmax are useful low-intensity reference points because they spend more time moving bytes than doing arithmetic). Bảng 11.13
ánh xạ phổ biến thần kinh mạng các hoạt động tới Đường mái nhà mô hình (Table 11.13 maps common neural network operations to the Roofline model).
Bảng 11.13: Các hoạt động trên Đường mái nhà: Thần kinh mạng các lớp trải dài một rộng phạm vi của số học các cường độ (Table 11.13: Operations on the Roofline: Neural network layers span a wide range of arithmetic intensities). Lớn, được xếp ô gạch-tốt
các tích chập và được đóng lô các GEMM có thể là bị ràng buộc-bởi-tính toán, trong khi nhỏ-lô dày đặc các phép chiếu, MobileNet theo chiều sâu các lớp,
sự chú ý softmax, sự chuẩn hóa, và DLRM các việc nhúng là thường bị ràng buộc-bởi-bộ nhớ (Large, well-tiled convolutions and batched GEMMs can be compute-bound, while small-batch dense projections, MobileNet depthwise layers, attention softmax, normalization, and DLRM embeddings are often memory-bound).
Hoạt động (Operation)
Số học Cường độ (Arithmetic Intensity)
Sự phân loại (Classification)
Ngọn hải đăng Ví dụ (Lighthouse Example)
Conv2D (Dày đặc) (Conv2D (Dense))
50–200 FLOP/byte
Đứng giang chân đỉnh; cao-sự tái sử dụng
các trường hợp bị ràng buộc-bởi-tính toán (Straddles ridge; high-reuse cases compute-bound)
ResNet-50
Dày đặc MatMul (lớn lô,
được xếp ô gạch-tốt) (Dense MatMul (large batch, well-tiled))
64–256+ FLOP/byte
Thường bị ràng buộc-bởi-tính toán ở
lớn lô (Often compute-bound at large batch)
GPT-2 (được đóng lô các phép chiếu) (GPT-2 (batched projections))
Theo chiều sâu Conv (Depthwise Conv)
10–20 FLOP/byte
Bị ràng buộc-bởi-bộ nhớ (Memory-bound)
MobileNet
Sự chú ý Softmax (Attention Softmax)
2–5 FLOP/byte
Bị ràng buộc-bởi-bộ nhớ (Memory-bound)
GPT-2 (Sự tạo ra) (GPT-2 (Generation))
LayerNorm
1–2 FLOP/byte
Bị ràng buộc-bởi-bộ nhớ (Memory-bound)
GPT-2/Llama
Việc nhúng lượt tra cứu (Embedding lookup)
<1 FLOP/byte
Bị ràng buộc-bởi-bộ nhớ (Memory-bound)
DLRM
Để nhìn thấy cách nào những cường độ các giá trị này chuyển đổi thành thực sự hiệu suất các dự đoán, một transformer lớp
cung cấp một hoàn chỉnh số học-cường độ sự tính toán qua của nó chính các tiểu-hoạt động (To see how these intensity values translate into real performance predictions, a transformer layer provides a complete arithmetic-intensity calculation across its major sub-operations).

11. Phần cứng Sự gia tốc (Hardware Acceleration)
597
Giấy ăn Toán học 11.4 (Napkin Math 11.4): Transformer lớp sự phân tích (Transformer layer analysis)
Cho một transformer với hidden_dim = 768, batch = 32, seq = 512 (For a transformer with hidden_dim = 768, batch = 32, seq = 512):
Sự chú ý QKV phép chiếu (Attention QKV projection):
• Các FLOP (FLOPs): 2 × 3 × 32 × 512 × 768 × 768 = 58 GFLOP
• Các byte (Bytes): (đầu vào + các trọng số + đầu ra) (input + weights + output) = (32 × 512 × 768 + 3 × 768 × 768 + 32 × 512 × 768 ×
3) × 2 ≈104.2 MB
• AI = 58 GFLOP / 104.2 MB = 556.4 FLOP/byte, thứ mà là bị ràng buộc bởi tính toán trên A100 (phía trên
153 FLOP/byte ngưỡng) (which is compute bound on A100 (above 153 FLOP/byte threshold))
Softmax:
• Các FLOP (FLOPs): 32 × 12 × 512 × 512 × 3 ≈302 MFLOP (exp, sum, div)
• Các byte (Bytes): 32 × 12 × 512 × 512 × 2 × 2 = 402.7 MB
• AI = 302 MFLOP / 402.7 MB = 0.75 FLOP/byte, thứ mà là bị ràng buộc-bởi-bộ nhớ (which is memory-bound)
Sự phân tích này giải thích tại sao FlashAttention tập trung trên việc làm giảm bớt bộ nhớ lưu lượng trong sự chú ý
thay vì việc làm giảm bớt các FLOP (This analysis explains why FlashAttention focuses on reducing memory traffic in attention rather than reducing FLOPs).
Những các sự phân loại này một cách trực tiếp thông báo sự tối ưu hóa chiến lược (These classifications directly inform optimization strategy). Bị ràng buộc-bởi-bộ nhớ các hoạt động hưởng lợi
từ việc làm giảm bớt dữ liệu sự di chuyển thông qua toán tử sự hợp nhất, việc sử dụng được giảm bớt độ chính xác (FP16, INT8),
và việc làm tăng số học cường độ thông qua thuật toán các sự thay đổi giống như FlashAttention (Memory-bound operations benefit from reducing data movement through operator fusion, using reduced precision (FP16, INT8), and increasing arithmetic intensity through algorithmic changes like FlashAttention). Bị ràng buộc-
bởi-tính toán các hoạt động, bởi sự tương phản, hưởng lợi từ việc tối đa hóa phần cứng sự sử dụng thông qua việc đóng lô
và tính song song, việc khai thác Tensor Các lõi và được chuyên biệt hóa tính toán các đơn vị, và việc tối ưu hóa tính toán
tính hiệu quả thông qua việc xếp ô gạch và việc lập lịch trình (Compute-bound operations, by contrast, benefit from maximizing hardware utilization through batching and parallelism, exploiting Tensor Cores and specialized compute units, and optimizing compute efficiency through tiling and scheduling).
11.6.2 Việc tính toán bộ nhớ băng thông các giới hạn (Calculating memory bandwidth bounds)
Đường mái nhà mô hình của bị ràng buộc-bởi-bộ nhớ vùng là được xác định bởi đỉnh bộ nhớ băng thông (The roofline model’s memory-bound region is determined by the peak memory bandwidth). Cho một
hoạt động để đạt được thông lượng 𝑅ops (FLOP/s, thường được biểu diễn trong TFLOP/s) trong bị ràng buộc-bởi-bộ nhớ
chế độ, phương trình 11.4 cho yêu cầu băng thông (For an operation to achieve throughput 𝑅ops (FLOP/s, often expressed in TFLOP/s) in the memory-bound regime, equation 11.4 gives the required bandwidth):
BWreq = 𝑅ops / 𝐼
bytes/s
(11.4)
Khi yêu cầu băng thông vượt quá đỉnh băng thông, hiệu suất là bị giới hạn theo phương
trình 11.5 (When required bandwidth exceeds peak bandwidth, performance is capped according to equation 11.5). Ở đây 𝑅ops và 𝑅attain là trong FLOP/s và 𝐼 là trong FLOP/byte (Here 𝑅ops and 𝑅attain are in FLOP/s and 𝐼is in FLOP/byte).
𝑅attain = BW × 𝐼
(11.5)
Một tích chập lớp cung cấp bị ràng buộc-bởi-tính toán sự tương phản (A convolution layer provides the compute-bound contrast).
Giấy ăn Toán học 11.5 (Napkin Math 11.5): Tích chập lớp sự phân tích (Convolutional layer analysis)
Xem xét một Conv2D lớp với đầu vào hình dạng (batch = 32, channels = 128, height = 56, width =
56), đầu ra các kênh = 256, hạt nhân kích thước 3×3 trên một A100 GPU (Consider a Conv2D layer with input shape (batch = 32, channels = 128, height = 56, width = 56), output channels = 256, kernel size 3×3 on an A100 GPU):
Tính toán các yêu cầu (Computational requirements):
• Đầu ra kích thước (Output size): 32×256×56×56 = 25.7M các phần tử (elements)
• Các FLOP trên mỗi đầu ra (FLOPs per output): 128×3×3×2 = 2,304 (multiply-add)
• Tổng các FLOP (Total FLOPs): 25.7M × 2,304 = 59.2 GFLOP
Bộ nhớ lưu lượng sự phân tích (Memory traffic analysis):
• Đầu vào (Input): 32×128×56×56×2 = 25.7 MB (FP16)
• Các trọng số (Weights): 256×128×3×3×2 ≈0.6 MB (FP16)

598
11.6 Đường mái nhà Mô hình (Roofline Model)
• Đầu ra (Output): 32×256×56×56×2 = 51.4 MB (FP16)
• Tổng (Total): 77.7 MB
Số học cường độ (Arithmetic intensity): 𝐼 = 59.2 GFLOP / 77.7 MB = 762.2 FLOP/byte
Điều này là tốt phía trên A100 của đỉnh điểm của 153 FLOP/byte, việc làm này hoạt động bị ràng buộc-bởi-tính toán (This is well above A100’s ridge point of 153 FLOP/byte, making this operation compute-bound).
Lớp sẽ đạt được gần-đỉnh hiệu suất của ~312 TFLOP/s (FP16 với Tensor Các lõi) (The layer will achieve near-peak performance of ~312 TFLOP/s (FP16 with Tensor Cores)).
Tích chập lớp của cao số học cường độ phát sinh từ của nó trọng số sự tái sử dụng mẫu: cùng
3×3 hạt nhân là được áp dụng qua tất cả thuộc về không gian các vị trí, việc khấu hao chi phí của việc tải các trọng số qua
hàng triệu của đầu ra các sự tính toán (The convolutional layer’s high arithmetic intensity arises from its weight reuse pattern: the same 3×3 kernel is applied across all spatial locations, amortizing the cost of loading weights across millions of output computations). Điều này là kiến trúc mẫu thứ mà làm các CNN vì vậy hiệu quả trên
hiện đại các máy gia tốc (This is the architectural pattern that makes CNNs so efficient on modern accelerators).
Tuy nhiên, không phải tất cả các lớp trong một thần kinh mạng trưng bày này thuận lợi hồ sơ (However, not all layers in a neural network exhibit this favorable profile). Hoàn toàn được kết nối
(dày đặc) các lớp thứ mà một cách điển hình xuất hiện ở kết thúc của sự phân loại các mạng, hoặc như phép chiếu các lớp trong
các transformer, có khác nhau số học cường độ các đặc điểm (The fully connected (dense) layers that typically appear at the end of classification networks, or as the projection layers in transformers, have different arithmetic intensity characteristics). Một dày đặc lớp cung cấp bị ràng buộc-bởi-bộ nhớ
sự tương phản được cần thiết để dự đoán nơi các nút thắt cổ chai sẽ xảy ra trong đầu-cuối tới-đầu-cuối mô hình sự thực thi (A dense layer provides the memory-bound contrast needed to predict where bottlenecks will occur in end-to-end model execution).
Giấy ăn Toán học 11.6 (Napkin Math 11.6): Dày đặc lớp sự phân tích (Dense layer analysis)
Xem xét một hoàn toàn được kết nối lớp: đầu vào (batch = 32, features = 2048) → đầu ra (batch = 32,
features = 2048) trên cùng A100 (Consider a fully connected layer: input (batch = 32, features = 2048) →output (batch = 32, features = 2048) on the same A100):
Tính toán các yêu cầu (Computational requirements):
• Ma trận nhân (Matrix multiply): (32×2048)×(2048×2048)
• Tổng các FLOP (Total FLOPs): 2×32×2048×2048 = 268.4 MFLOP
Bộ nhớ lưu lượng sự phân tích (Memory traffic analysis):
• Đầu vào (Input): 32×2048×2 = 131.1 KB (FP16)
• Các trọng số (Weights): 2048×2048×2 = 8.4 MB (FP16)
• Đầu ra (Output): 32×2048×2 = 131.1 KB (FP16)
• Tổng (Total): 8.7 MB
Số học cường độ (Arithmetic intensity): 𝐼 = 268.4 MFLOP / 8.7 MB = 31 FLOP/byte
Điều này là bên dưới A100 của đỉnh điểm của 153 FLOP/byte, việc làm này hoạt động bị ràng buộc-bởi-bộ nhớ (This is below A100’s ridge point of 153 FLOP/byte, making this operation memory-bound).
Có thể đạt được hiệu suất (Attainable performance): 𝑅attain = 2,039 GB/s × 31 FLOP/byte = 63.3 TFLOP/s
Điều này là chỉ 20.3 phần trăm của đỉnh tính toán khả năng, việc chứng minh bộ nhớ bức tường hiệu ứng cho
nhỏ lô các kích thước (This is only 20.3 percent of peak compute capability, demonstrating the memory wall effect for small batch sizes).
Dày đặc lớp của thấp hơn số học cường độ bắt nguồn từ bị giới hạn trọng số sự tái sử dụng: mỗi trọng số là
được tái sử dụng qua lô nhưng thiếu bổ sung thuộc về không gian sự tái sử dụng của tích chập các bộ lọc, vì vậy nhỏ-lô
dày đặc các lớp có nhiều thấp hơn số học cường độ so với các tích chập (The dense layer’s lower arithmetic intensity stems from limited weight reuse: each weight is reused across the batch but lacks the additional spatial reuse of convolutional filters, so small-batch dense layers have much lower arithmetic intensity than convolutions). Sự khác biệt này giải thích tại sao
transformer sự suy luận (bị thống trị bởi dày đặc các phép chiếu) là một cách điển hình bị ràng buộc bởi bộ nhớ trong khi CNN
sự suy luận có thể là bị ràng buộc bởi tính toán (This difference explains why transformer inference (dominated by dense projections) is typically memory bound while CNN inference can be compute bound).
Giấy ăn Toán học 11.7 (Napkin Math 11.7): LayerNorm sự phân tích (LayerNorm analysis)
LayerNorm với đầu vào hình dạng (batch = 32, seq = 512, hidden = 768) (LayerNorm with input shape (batch = 32, seq = 512, hidden = 768)):
Tính toán các yêu cầu (Computational requirements):
• Các phần tử (Elements): 32×512×768 = 12.6M
• Các hoạt động trên mỗi phần tử (Operations per element): trung bình (1 ADD), phương sai (1 ADD, 1 MUL), chuẩn hóa (1 ADD, 1
MUL, 1 DIV) ≈6 (mean (1 ADD), variance (1 ADD, 1 MUL), normalize (1 ADD, 1 MUL, 1 DIV) ≈6)
• Tổng các FLOP (Total FLOPs): 12.6M × 6 = 75.5 MFLOP

11. Phần cứng Sự gia tốc (Hardware Acceleration)
599
Bộ nhớ lưu lượng (Memory traffic):
• Đầu vào (Input): 12.6M × 2 = 25.2 MB
• Các tham số (tỷ lệ, độ lệch) (Parameters (scale, bias)): 768×2×2 = 3.1 KB (không đáng kể) (negligible)
• Đầu ra (Output): 12.6M × 2 = 25.2 MB
• Tổng (Total): 50.3 MB
Số học cường độ (Arithmetic intensity): 𝐼 = 75.5 MFLOP / 50.3 MB = 1.5 FLOP/byte
Điều này là nghiêm trọng bị ràng buộc-bởi-bộ nhớ (102× bên dưới A100 đỉnh điểm) (This is severely memory-bound (102× below the A100 ridge point)). Hiệu suất là bị giới hạn tới (Performance is limited to):
𝑅attain = 2039 GB/s × 1.5 FLOP/byte = 3.1 TFLOP/s
Điều này đại diện ít hơn 1 phần trăm của A100 của tính toán khả năng, việc giải thích tại sao sự chuẩn hóa
các lớp đóng góp không đáng kể tính toán thời gian nhưng đáng kể độ trễ (This represents less than 1 percent of A100’s compute capacity, explaining why normalization layers contribute negligible compute time but significant latency).
Tình huống trở nên thậm chí nhiều hơn cực đoan cho theo-phần-tử các hoạt động giống như sự chuẩn hóa các lớp (The situation becomes even more extreme for element-wise operations like normalization layers).
Những các hoạt động này thực hiện không đáng kể sự tính toán liên quan tới dữ liệu chúng chạm, như LayerNorm
làm rõ ràng (These operations perform negligible computation relative to the data they touch, as LayerNorm makes clear). Mỗi phần tử là được tải, được biến đổi bởi một đơn giản công thức, và được ghi lại, việc để lại
cơ bản không cơ hội cho dữ liệu sự tái sử dụng (Each element is loaded, transformed by a simple formula, and written back, leaving essentially no opportunity for data reuse).
11.6.3 Sự tối ưu hóa bởi cường độ chế độ (Optimization by intensity regime)
Đường mái nhà sự phân tích một cách trực tiếp thông báo sự tối ưu hóa các ưu tiên, được tóm tắt trong bảng 11.14 (The roofline analysis directly informs optimization priorities, summarized in table 11.14).
Bảng 11.14: Sự tối ưu hóa bởi Số học Cường độ Chế độ: Đường mái nhà vị trí xác định liệu một sự tối ưu hóa nên
đuổi theo tính toán sự sử dụng, bộ nhớ-lưu lượng sự làm giảm, hoặc hoàn toàn sự loại bỏ của bộ nhớ các chuyến đi-khứ-hồi (Table 11.14: Optimization by Arithmetic Intensity Regime: Roofline position determines whether an optimization should chase compute utilization, memory-traffic reduction, or complete elimination of memory round-trips). Càng thấp số học
cường độ, càng có giá trị sự hợp nhất và dữ liệu-sự di chuyển sự tránh né trở nên (The lower the arithmetic intensity, the more valuable fusion and data-movement avoidance become).
Cường độ
chế độ (Intensity regime)
Điển hình các hoạt động (Typical operations)
Sự tối ưu hóa
ưu tiên (Optimization priority)
Phổ biến các kỹ thuật (Common techniques)
Được mong đợi tác động (Expected impact)
Cao AI (>200
FLOP/byte) (High AI (>200 FLOP/byte))
Lớn các tích chập (Large convolutions)
Tối đa hóa
tính toán
sự sử dụng (Maximize compute utilization).
Tensor Các lõi, luồng-khối
sự tinh chỉnh, và cao
tỷ lệ lấp đầy (Tensor Cores, thread-block tuning, and high occupancy).
Có thể tiếp cận 90–95% của đỉnh
TFLOP/s (Can approach 90–95% of peak TFLOP/s).
Trung bình AI
(20–200
FLOP/byte) (Medium AI (20–200 FLOP/byte))
Kích thước-trung bình dày đặc
các lớp (Medium-sized dense layers)
Cân bằng
tính toán và
bộ nhớ
sự tối ưu hóa (Balance compute and memory optimization).
Lớn hơn các lô, thanh ghi
việc xếp ô gạch, và sự hợp nhất với
liền kề các hoạt động (Larger batches, register tiling, and fusion with adjacent operations).
Có thể di chuyển từ
bị ràng buộc-bởi-bộ nhớ sang
bị ràng buộc-bởi-tính toán sự thực thi (Can move from memory-bound to compute-bound execution).
Thấp AI (<20
FLOP/byte) (Low AI (<20 FLOP/byte))
Nhỏ dày đặc các lớp
và theo-phần-tử
các hoạt động (Small dense layers and element-wise operations)
Giảm bộ nhớ
lưu lượng (Reduce memory traffic).
Tích cực toán tử sự hợp nhất,
được giảm bớt độ chính xác (FP16 →
INT8), và thuật toán
các sự thay đổi (Aggressive operator fusion, reduced precision (FP16 →INT8), and algorithmic changes).
Sự hợp nhất một mình có thể mang lại 2–4×
các phần tăng tốc (Fusion alone can yield 2–4× speedups).
Rất thấp AI
(<2
FLOP/byte) (Very low AI (<2 FLOP/byte))
Sự chuẩn hóa các lớp
và sự kích hoạt
các hàm (Normalization layers and activation functions)
Loại bỏ
bộ nhớ
các chuyến đi-khứ-hồi (Eliminate memory round-trips).
Bắt buộc sự hợp nhất với
liền kề các hoạt động và
tại-chỗ sự tính toán nơi
có thể (Mandatory fusion with adjacent operations and in-place computation where possible).
Sự hợp nhất có thể mang lại 10× các phần tăng tốc;
cho ví dụ, LayerNorm
được kết hợp với Gaussian
Lỗi Tuyến tính Đơn vị (GELU) có thể
trở thành một đơn được hợp nhất hạt nhân (Fusion can yield 10× speedups; for example, LayerNorm combined with the Gaussian Error Linear Unit (GELU) can become a single fused kernel).
Cho thấp-AI các hoạt động, toán tử sự hợp nhất là thường quyết định sự tối ưu hóa: LayerNorm được kết hợp
với Gaussian Lỗi Tuyến tính Đơn vị (GELU), cho ví dụ, có thể trở thành một đơn được hợp nhất hạt nhân (For low-AI operations, operator fusion is often the decisive optimization: LayerNorm combined with the Gaussian Error Linear Unit (GELU), for example, can become a single fused kernel). Một của
dễ tiếp cận nhất các đòn bẩy cho việc di chuyển một hoạt động lên và phải trên đường mái nhà là việc đóng lô (One of the most accessible levers for moving an operation up and right on the roofline is batching).
Giấy ăn Toán học 11.8 (Napkin Math 11.8): Lô kích thước và số học cường độ (Batch size and arithmetic intensity)
Việc làm tăng lô kích thước cải thiện số học cường độ cho ma trận các hoạt động bằng cách việc khấu hao trọng số
việc tải (Increasing batch size improves arithmetic intensity for matrix operations by amortizing weight loading). Phương trình 11.6 chính thức hóa này mối quan hệ cho một dày đặc lớp (𝐵×𝑀)×(𝑀×𝑁) (Equation 11.6 formalizes this relationship for a dense layer (𝐵×𝑀)×(𝑀×𝑁)):
𝐼 = 2𝐵𝑀𝑁 / (2𝐵𝑀+2𝑀𝑁+2𝐵𝑁) ≈ 2𝐵𝑀𝑁 / 2𝑀𝑁 = 𝐵
(khi 2𝑀𝑁≫2𝐵(𝑀+𝑁)) ((when 2𝑀𝑁≫2𝐵(𝑀+𝑁)))
(11.6)
Ví dụ (Example): Dày đặc lớp với M=N=2048 (FP16) (Dense layer with M=N=2048 (FP16))
• Batch = 1: AI ≈1 FLOP/byte (bị ràng buộc bởi bộ nhớ) (memory bound)

600
11.6 Đường mái nhà Mô hình (Roofline Model)
• Batch = 32: AI ≈31 FLOP/byte (bị ràng buộc bởi bộ nhớ) (memory bound)
• Batch = 256: AI ≈204.8 FLOP/byte (bị ràng buộc bởi tính toán trên A100) (compute bound on A100)
Điều này giải thích tại sao việc đóng lô có thể sản xuất lớn thông lượng các sự cải thiện trong sản xuất sự suy
luận các hệ thống, như MLPerf Inference, được tiêu chuẩn hóa điểm chuẩn bộ chương trình được bao phủ trong Chương 12,
chứng minh bằng cách việc phân tách số lượng lớn-thông lượng các lần chạy từ bị ràng buộc-bởi-độ trễ việc phục vụ các lần chạy
(Reddi et al. 2019) (This explains why batching can produce large throughput improvements in production inference systems, as MLPerf Inference, the standardized benchmark suite covered in Chapter 12, demonstrates by separating bulk-throughput runs from latency-constrained serving runs (Reddi et al. 2019)).
Lô kích thước sự phân tích tiết lộ tại sao sự suy luận việc phục vụ các hệ thống là được thiết kế xung quanh việc đóng lô: nó
thay đổi số học cường độ chế độ của bị ràng buộc-bởi-bộ nhớ các khối lượng công việc (The batch size analysis reveals why inference serving systems are designed around batching: it changes the arithmetic intensity regime of memory-bound workloads). Tuy nhiên, việc đóng lô giới thiệu
độ trễ các sự đánh đổi, vì các yêu cầu phải chờ trong một hàng đợi cho đến khi một lô hình thành (However, batching introduces latency trade-offs, since requests must wait in a queue until a batch forms). Sự căng thẳng này giữa
thông lượng (việc thiên vị lớn các lô) và độ trễ (việc thiên vị nhỏ các lô) là một trung tâm thách thức trong
ML việc phục vụ các hệ thống, được khám phá trong độ sâu trong phần 13.7.3 (This tension between throughput (favoring large batches) and latency (favoring small batches) is a central challenge in ML serving systems, explored in depth in section 13.7.3).
Cho các khối lượng công việc nơi việc đóng lô là không thực tế, chẳng hạn như tương tác LLM sự tạo ra nơi người dùng
mong đợi truyền phát các phản hồi, số học cường độ duy trì vốn có thấp (For workloads where batching is impractical, such as interactive LLM generation where users expect streaming responses, the arithmetic intensity remains inherently low). Việc hiểu này
trần là cần thiết cho việc thiết lập thực tế hiệu suất các kỳ vọng (Understanding this ceiling is essential for setting realistic performance expectations).
Một lô-1 GPT-2 sự tính toán làm này băng thông trần cụ thể (A batch-1 GPT-2 calculation makes this bandwidth ceiling concrete).
Giấy ăn Toán học 11.9 (Napkin Math 11.9): Thông lượng trần (The throughput ceiling)
Vấn đề: Cái gì là tối đa có thể sự sử dụng của một NVIDIA A100 khi việc chạy GPT-2
sự suy luận (lô kích thước 1)? (Problem: What is the maximum possible utilization of an NVIDIA A100 when running GPT-2 inference (batch size 1)?)
Phần cứng các sự ràng buộc (các mẫu số) (The hardware constraints (the denominators))
• Đỉnh tính toán (Peak compute): 312 TFLOP/s (FP16 Tensor Core).
• Đỉnh băng thông (Peak bandwidth): 2.04 TB/s (HBM2e).
• Đỉnh điểm (𝑅peak/BW) (Ridge point (𝑅peak/BW)): 312 TFLOP/s / 2.04 TB/s = 153 FLOP/byte (cho FP16 Tensor
Core) ((for FP16 Tensor Core)).
– Ý nghĩa (Meaning): Việc bão hòa này chip ở FP16 độ chính xác yêu cầu 153 FLOP/byte các hoạt động
cho mỗi byte được tải (Saturating this chip at FP16 precision requires 153 FLOP/byte operations for every byte loaded). Đỉnh điểm thay đổi bởi độ chính xác: FP32 các hoạt động (19.5
TFLOP/s đỉnh) có một đỉnh điểm của chỉ ~9.6 FLOP/byte (The ridge point varies by precision: FP32 operations (19.5 TFLOP/s peak) have a ridge point of only ~9.6 FLOP/byte).
Khối lượng công việc các đặc điểm (tử số) (The workload characteristics (the numerator))
• Mô hình (Model): GPT-2 XL (1.5 tỷ các tham số) (GPT-2 XL (1.5 billion parameters)).
• Hoạt động (Operation): Tự hồi quy sự tạo ra (1 token tại một thời gian) (Autoregressive generation (1 token at a time)).
• Dữ liệu sự di chuyển (Data movement): Phải tải tất cả các trọng số (3 GB @ FP16) cho mỗi token (Must load all weights (3 GB @ FP16) for every token).
• Tính toán (Compute): Vector-Ma trận phép nhân (Vector-Matrix multiplication). 2 × Params ≈ 3 GFLOP.
• Số học cường độ (Arithmetic intensity): 3 GFLOP / 3 GB = 1 FLOP/byte
Dự đoán (sắt luật) (The prediction (iron law))
Vì Thực tế Cường độ (1) < Đỉnh Điểm (153 FLOP/byte), hệ thống là bị ràng buộc bởi băng thông (Since Actual Intensity (1) ฀Ridge Point (153 FLOP/byte), the system is bandwidth bound).
• Tối đa thông lượng (Maximum throughput): 1 FLOP/byte × 2.04 TB/s = 2.04 TFLOP/s.
• Sự sử dụng trần (Utilization ceiling): 2.04 TFLOP/s (Thực tế) / 312 TFLOP/s (Đỉnh) ≈0.7% (2.04 TFLOP/s (Actual) / 312 TFLOP/s (Peak) ≈0.7%)
Các hệ thống sự thấu hiểu (Systems insight): Không có việc đóng lô hoặc việc lưu bộ nhớ cache, một $15,000 chạy ở ít hơn 1 phần trăm tính hiệu quả trên
LLM sự suy luận (Without batching or caching, a $15,000 runs at less than 1 percent efficiency on LLM inference). Này "sự sử dụng khoảng trống" dẫn dắt nhu cầu cho khóa-giá trị việc lưu bộ nhớ cache và sự lượng tử hóa (This “utilization gap” drives the need for key-value caching and quantization).
Như này sự dẫn xuất chứng minh, Đường mái nhà mô hình cung cấp chẩn đoán bộ khung cho
việc xác định liệu các hoạt động là bị ràng buộc bởi tính toán hoặc bị ràng buộc bởi bộ nhớ (As this derivation demonstrates, the Roofline model provides the diagnostic framework for identifying whether operations are compute bound or memory bound). Việc biết rằng một khối lượng công việc là
bị ràng buộc bởi bộ nhớ ở 0.7 phần trăm sự sử dụng là chỉ đầu tiên bước; tiếp theo thách thức là việc chuyển đổi này
sự chẩn đoán thành hiệu quả sự thực thi các kế hoạch thứ mà khai thác máy gia tốc các kiến trúc (Knowing that a workload is memory bound at 0.7 percent utilization is only the first step; the next challenge is translating this diagnosis into efficient execution plans that exploit accelerator architectures).

11. Phần cứng Sự gia tốc (Hardware Acceleration)
601
11.7 Phần cứng Sự ánh xạ (Hardware Mapping)
Đường mái nhà sự phân tích đã dạy chúng ta để chẩn đoán liệu cụ thể các hoạt động là bị ràng buộc bởi tính toán hoặc
bị ràng buộc bởi bộ nhớ trên cho trước phần cứng (The Roofline analysis taught us to diagnose whether specific operations are compute bound or memory bound on given hardware). Chúng ta đã thấy rằng ResNet-50 của các tích chập có thể đạt tới cao số học
cường độ (50–200 FLOP/byte), với cao-sự tái sử dụng các trường hợp việc đi qua vào bị ràng buộc-bởi-tính toán
chế độ, trong khi GPT-2 của sự chú ý các lớp đạt được chỉ 2–5 FLOP/byte và là nghiêm trọng bị ràng buộc bởi bộ nhớ (We saw that ResNet-50’s convolutions can reach high arithmetic intensity (50–200 FLOP/byte), with the high-reuse cases crossing into the compute-bound regime, while GPT-2’s attention layers achieve only 2–5 FLOP/byte and are severely memory bound).
Sự chẩn đoán, tuy nhiên, là chỉ một nửa thách thức (Diagnosis, however, is only half the challenge). Một khi chúng ta biết rằng LayerNorm đạt được chỉ 1–2
FLOP/byte trên một A100, thách thức trở thành việc thực thi nó một cách hiệu quả mặc dù của này sự giới hạn (Once we know that LayerNorm achieves only 1–2 FLOP/byte on an A100, the challenge becomes executing it efficiently despite this limitation). Điều này là
miền của phần cứng sự ánh xạ, nghệ thuật của việc dịch trừu tượng tính toán các đồ thị thành cụ thể
sự thực thi các kế hoạch thứ mà khai thác máy gia tốc các kiến trúc trong khi việc tôn trọng của chúng các sự ràng buộc (This is the domain of hardware mapping, the art of translating abstract computational graphs into concrete execution plans that exploit accelerator architectures while respecting their constraints).
Bộ nhớ hệ thống các thách thức được kiểm tra trong phần 11.5.1 đã thiết lập tại sao bộ nhớ truy cập thống
trị hiện đại AI các hệ thống: như hình 11.9 đã định lượng, DRAM truy cập tiêu thụ 100–200× nhiều hơn năng lượng
so với một nhân-tích lũy hoạt động (Horowitz 2014) (The memory system challenges examined in section 11.5.1 established why memory access dominates modern AI systems: as figure 11.9 quantified, DRAM access consumes 100–200× more energy than a multiply-accumulate operation (Horowitz 2014)). Đường mái nhà mô hình đã thiết lập cách nào để
đo lường liệu một khối lượng công việc là bị ràng buộc bởi tính toán hoặc bị ràng buộc bởi bộ nhớ (The Roofline model established how to measure whether a workload is compute bound or memory bound). Phần này giải quyết tới hạn
tiếp-theo: cách nào để ánh xạ các sự tính toán để tối đa hóa dữ liệu sự tái sử dụng và tối thiểu hóa chuyên sâu-năng lượng
các sự truyền tải thứ mà Đường mái nhà sự phân tích đã tiết lộ như chính nút thắt cổ chai (This section addresses the critical follow-up: how to map computations to maximize data reuse and minimize the energy-intensive transfers that the Roofline analysis revealed as the primary bottleneck).
Xem xét một 3×3 tích chập đang chạy trên một máy gia tốc ô gạch (Consider a 3×3 convolution running on an accelerator tile). Toán học hoạt động là cố định,
nhưng sự thực thi kế hoạch là không (The mathematical operation is fixed, but the execution plan is not). Một lịch trình có thể giữ một bộ lọc trong cục bộ các thanh ghi trong khi nhiều đầu ra
các pixel truyền phát qua nó; một cái khác có thể tiến lên pixel qua pixel và tải lại cùng bộ lọc các giá trị một cách lặp lại
từ một chậm hơn bộ nhớ tầng (One schedule can keep a filter in local registers while many output pixels stream past it; another can advance pixel by pixel and reload the same filter values repeatedly from a slower memory tier). Cả hai lịch trình tính toán cùng tensor (Both schedules compute the same tensor). Chỉ một biến sự tái sử dụng trong
tích chập thành thực sự băng thông các khoản tiết kiệm (Only one turns the reuse in the convolution into real bandwidth savings). Phần cứng sự ánh xạ là kỷ luật thứ mà làm sự khác
biệt đó tường minh: nó quyết định nơi công việc chạy, nơi dữ liệu sống trong khi nó là được tái sử dụng, và khi
mỗi vòng lặp hoặc hạt nhân thực thi để mà máy gia tốc là được nuôi dưỡng thay vì nhàn rỗi (Hardware mapping is the discipline that makes that difference explicit: it decides where the work runs, where the data lives while it is reused, and when each loop or kernel executes so the accelerator is fed rather than idle).
Định nghĩa 11.6 (Definition 11.6): Sự ánh xạ trong AI sự gia tốc (Mapping in AI acceleration)
Sự ánh xạ trong AI Sự gia tốc là máy gia tốc-trình biên dịch quá trình của việc ràng buộc Hợp lý Tính
toán Đồ thị vào Vật lý Phần cứng Cấu trúc liên kết bằng cách việc quyết định cái nào các hoạt động thực thi trên
cái nào xử lý các phần tử, cái nào dữ liệu cư trú trong cái nào bộ nhớ tầng, và trong cái gì thuộc về thời gian
thứ tự (Mapping in AI Acceleration is the accelerator-compiler process of binding the Logical Computation Graph to the Physical Hardware Topology by deciding which operations execute on which processing elements, which data resides in which memory tier, and in what temporal order).
1. Ý nghĩa (Significance): Bên trong D·A·M phân loại, sự ánh xạ là máy-trục quyết định thứ mà
xác định liệu thuật toán của các hoạt động chạy ở 𝑅peak hoặc ở BW × 𝐼 (Within the D·A·M taxonomy, mapping is the machine-axis decision that determines whether the algorithm’s operations run at 𝑅peak or at BW×𝐼). Một cách cụ thể, một
chung ma trận nhân (GEMM) với số học cường độ 𝐼 chạy ở min(𝑅peak, BW ×
𝐼); một tồi xếp ô gạch sự lựa chọn thứ mà ép buộc không cần thiết DRAM các truy cập có thể làm giảm hiệu quả 𝐼
đủ để làm sụp đổ một bị ràng buộc-bởi-tính toán hoạt động thành một bị ràng buộc-bởi-băng thông một cái và gây ra một
tương xứng sự giảm trong được duy trì thông lượng (Specifically, a general matrix multiply (GEMM) with arithmetic intensity 𝐼runs at min(𝑅peak, BW×𝐼); a poor tiling choice that forces unnecessary DRAM accesses can reduce effective 𝐼 enough to collapse a compute-bound operation into a bandwidth-bound one and cause a commensurate drop in sustained throughput).
2. Sự phân biệt (Distinction): Không giống Truyền thống Sự biên dịch (thứ mà nhắm mục tiêu một tuyến tính lệnh luồng
trên một von Neumann bộ xử lý), Sự ánh xạ nhắm mục tiêu một Dữ liệu luồng Kiến trúc nơi
sự di chuyển của dữ liệu là cũng tốn kém như sự tính toán chính nó: ngoài-chip DRAM truy cập tiêu thụ
~200× nhiều hơn năng lượng so với một nhân-tích lũy trong cục bộ các thanh ghi (Unlike Traditional Compilation (which targets a linear instruction stream on a von Neumann processor), Mapping targets a Dataflow Architecture where the movement of data is as costly as the computation itself: off-chip DRAM access consumes ~200× more energy than a multiply-accumulate in local registers).
3. Phổ biến cạm bẫy (Common pitfall): Một thường xuyên quan niệm sai lầm là rằng sự ánh xạ là một cách tự động được xử lý
bởi các bộ khung (A frequent misconception is that mapping is automatically handled by frameworks). Cho chung GPU các khối lượng công việc, các trình biên dịch giống như Được gia tốc Tuyến tính Đại số
(XLA) có thể tìm thấy mạnh mẽ các sự ánh xạ cho phổ biến các hạt nhân; cho được chuyên biệt hóa các máy gia tốc (tâm thu
các mảng, tùy chỉnh các ASIC), được tạo ra-bởi-trình biên dịch các sự ánh xạ có thể vẫn tụt hậu được tinh chỉnh-bởi-bàn tay các lịch trình
bởi vì trình biên dịch của tìm kiếm không gian là bị giới hạn bởi thời gian ngân sách tại sự biên dịch (For general GPU workloads, compilers like Accelerated Linear Algebra (XLA) can find strong mappings for common kernels; for specialized accelerators (systolic arrays, custom ASICs), compiler-generated mappings may still lag hand-tuned schedules because the compiler’s search space is limited by the time budget at compilation).
Tích chập ví dụ phơi bày ba các quyết định thứ mà lặp lại trong suốt máy gia tốc sự biên
dịch (The convolution example exposes the three decisions that recur throughout accelerator compilation). Sự sắp đặt chỉ định nhân-tích lũy công việc tới xử lý các phần tử để mà tính song song không
biến thành nhàn rỗi thời gian hoặc kết nối liên thông sự tắc nghẽn (Placement assigns the multiply-accumulate work to processing elements so parallelism does not turn into idle time or interconnect congestion). Sự phân bổ giữ các trọng số, các sự kích hoạt, và một phần
các tổng trong bộ nhớ tầng nơi của chúng tiếp theo sự sử dụng sẽ xảy ra, thay vì việc để cho sự tái sử dụng tràn lại về
DRAM (Allocation keeps weights, activations, and partial sums in the memory tier where their next use will occur, rather than letting reuse spill back to DRAM). Việc lập lịch trình sắp xếp thứ tự các vòng lặp và các hạt nhân để mà được chọn sự sắp đặt và sự phân bổ duy trì hợp lệ
qua thời gian (Scheduling orders loops and kernels so the chosen placement and allocation remain valid over time). Một tồi sự lựa chọn trong bất kỳ một chiều hướng nào có thể làm sụp đổ một cao-số học-cường độ hoạt động
lại về thành một bị ràng buộc-bởi-băng thông sự thực thi (A poor choice in any one dimension can collapse a high-arithmetic-intensity operation back into a bandwidth-bound execution). Trong thực tế, những các sự lựa chọn này là quá được ghép nối cho các nhà phát triển
để quản lý bằng tay ở mô hình quy mô, thứ mà là tại sao một được chuyên biệt hóa trình biên dịch chẳng hạn như NVIDIA của NVCC

602
11.7 Phần cứng Sự ánh xạ (Hardware Mapping)
hoặc Google của XLA tiếp quản: nó chấp nhận cấp độ-cao mô hình từ bộ khung và tìm kiếm
sự ánh xạ không gian cho một tốt sự thực thi kế hoạch bên trong tại-thời-gian-biên-dịch và phần cứng ngân sách nó được cung cấp (or Google’s XLA takes over: it accepts the high-level model from the framework and searches the mapping space for a good execution plan within the compile-time and hardware budget it is given).
Phần 11.9 kiểm tra đó trình biên dịch sự hỗ trợ trong chi tiết (Section 11.9 examines that compiler support in detail).
11.7.1 Sự sắp đặt và sự phân bổ (Placement and allocation)
Việc dịch một mô hình của tính toán đồ thị thành hiệu quả phần cứng sự thực thi yêu cầu việc giải quyết hai
được ghép nối-chặt chẽ các vấn đề (Translating a model’s computational graph into efficient hardware execution requires solving two tightly coupled problems). Tính toán sự sắp đặt xác định cái nào các hoạt động chạy trên cái nào
xử lý các phần tử, việc cân bằng tính song song chống lại sự giao tiếp các chi phí (Computation placement determines which operations run on which processing elements, balancing parallelism against communication costs). Bộ nhớ sự phân bổ xác
định nơi dữ liệu cư trú bên trong bộ nhớ hệ thống phân cấp, việc đánh đổi khả năng chống lại truy cập độ trễ (Memory allocation determines where data resides within the memory hierarchy, trading capacity against access latency).
Những hai các quyết định này tương tác: việc sắp đặt các hoạt động trên xa xử lý các phần tử làm tăng bộ nhớ băng thông được yêu cầu để đưa đón dữ liệu giữa chúng, trong khi việc phân bổ dữ liệu tới nhanh nhưng nhỏ trên-chip
bộ nhớ giới hạn cái nào các hoạt động có thể thực thi một cách đồng thời (These two decisions interact: placing operations on distant processing elements increases the memory bandwidth required to shuttle data between them, while allocating data to fast but small on-chip memory limits which operations can execute concurrently). Việc làm sai một trong hai để lại hàng ngàn
của xử lý các phần tử nhàn rỗi hoặc bị bỏ đói cho dữ liệu (Getting either wrong leaves thousands of processing elements idle or starved for data).
11.7.1.1 Tính toán sự sắp đặt (Computation placement)
Tính toán sự sắp đặt là quá trình của một cách có chiến lược việc chỉ định các hoạt động tới một máy gia tốc của
xử lý các phần tử (PEs) để tối đa hóa tính song song, tối thiểu hóa nhàn rỗi thời gian, và làm giảm không cần thiết
dữ liệu sự di chuyển (Computation placement is the process of strategically assigning operations to an accelerator’s processing elements (PEs) to maximize parallelism, minimize idle time, and reduce unnecessary data movement). Hiện đại các máy gia tốc chứa khổng lồ các con số của các PE: NVIDIA H100 có hơn
16,000 truyền phát các bộ xử lý và nhiều hơn 500 tensor các lõi (Choquette 2023), các TPU sử dụng tâm thu
các mảng của hàng ngàn của nhân-tích lũy các đơn vị (Jouppi et al. 2017), và quy mô-tấm-wafer các bộ xử lý giống như
Cerebras của CS-2 tích hợp hơn 850,000 các lõi (Systems 2021) (Modern accelerators contain enormous numbers of PEs: the NVIDIA H100 has over 16,000 streaming processors and more than 500 tensor cores (Choquette 2023), TPUs use systolic arrays of thousands of multiply-accumulate units (Jouppi et al. 2017), and wafer-scale processors like Cerebras’ CS-2 integrate over 850,000 cores (Systems 2021)). Ở những các quy mô này, thậm chí nhỏ sự sắp đặt
các sự không hiệu quả cộng gộp thành có thể đo lường hiệu suất các sự mất mát bởi vì nhàn rỗi các lõi và dư thừa
bộ nhớ các sự truyền tải lãng phí cả thời gian và năng lượng (At these scales, even small placement inefficiencies compound into measurable performance losses because idle cores and redundant memory transfers waste both time and energy).
Độ khó của sự sắp đặt phụ thuộc trên khối lượng công việc tính đều đặn (The difficulty of placement depends on workload regularity). Các CNN trưng bày được cấu trúc, thuộc về không gian
cục bộ sự tính toán: một 256×256 hình ảnh có thể được xếp ô gạch qua hàng ngàn của GPU các lõi với mỗi ô gạch
được xử lý một cách độc lập, việc mang lại được cân bằng sự sử dụng (CNNs exhibit structured, spatially local computation: a 256×256 image can be tiled across thousands of GPU cores with each tile processed independently, yielding balanced utilization). Các transformer là khó hơn bởi vì tự-
sự chú ý yêu cầu mọi token để tương tác với mọi khác, việc tạo ra không đồng đều các nhu cầu nơi
sự chú ý điểm số sự tính toán là xa nặng hơn so với khác các hoạt động (Transformers are harder because self-attention requires every token to interact with every other, creating nonuniform demands where attention score computation is far heavier than other operations). Đồ thị Thần kinh Các mạng (GNNs)
là khó hơn nữa, như thưa thớt, một cách động thay đổi đồ thị các cấu trúc làm tĩnh sự phân vùng không hiệu quả (Graph Neural Networks (GNNs) are harder still, as sparse, dynamically changing graph structures make static partitioning ineffective).
Bảng 11.15 liệt kê chính các thách thức sự sắp đặt phải giải quyết qua những khối lượng công việc các loại này (Table 11.15 lists the core challenges placement must address across these workload types). Các
chung sợi chỉ là tính đều đặn: càng ít đều đặn sự tính toán, càng ít một tĩnh sự sắp đặt có thể
cân bằng tải trọng và tính cục bộ, thứ mà là tại sao thích ứng, nhận thức-thời gian chạy sự sắp đặt trở thành bắt buộc cho
các transformer và các GNN thậm chí mặc dù nó là không cần thiết cho các CNN (The common thread is regularity: the less regular the computation, the less a static placement can balance load and locality, which is why adaptive, runtime-aware placement becomes mandatory for transformers and GNNs even though it is unnecessary for CNNs).
Bảng 11.15: Tính toán Sự sắp đặt Các thách thức: Hiệu quả thần kinh mạng sự triển khai yêu cầu có chiến lược sự phân bổ của
các sự tính toán tới xử lý các phần tử, việc cân bằng khối lượng công việc sự phân phối, dữ liệu sự di chuyển các chi phí, và phần cứng các sự ràng buộc để
tối đa hóa sự thực thi tính hiệu quả (Table 11.15: Computation Placement Challenges: Effective neural network deployment requires strategic allocation of computations to processing elements, balancing workload distribution, data movement costs, and hardware constraints to maximize execution efficiency). Những các thách thức này dẫn dắt thiết kế của sự ánh xạ các chiến lược thứ mà tối ưu hóa tài nguyên sự sử dụng và
tối thiểu hóa sự giao tiếp chi phí chung (These challenges guide the design of mapping strategies that optimize resource utilization and minimize communication overhead).
Thách thức (Challenge)
Tác động trên Sự thực thi (Impact on Execution)
Chính Các sự xem xét cho Sự sắp đặt (Key Considerations for Placement)
Khối lượng công việc Sự mất cân bằng (Workload Imbalance)
Một số xử lý các phần tử kết thúc sớm trong khi những cái khác
duy trì bị quá tải, việc dẫn tới nhàn rỗi tính toán các tài nguyên (Some processing elements finish early while others remain overloaded, leading to idle compute resources).
Phân phối các hoạt động một cách đồng đều để ngăn chặn
các sự đình trệ và đảm bảo đầy đủ sự sử dụng của các PE (Distribute operations evenly to prevent stalls and ensure full utilization of PEs).
Không đều Tính toán
Các mẫu (Irregular Computation Patterns)
Các mô hình giống như các transformer và các GNN giới thiệu
không đồng đều tính toán các nhu cầu, việc làm tĩnh
sự sắp đặt khó khăn (Models like transformers and GNNs introduce nonuniform computation demands, making static placement difficult).
Sử dụng thích ứng sự sắp đặt các chiến lược thứ mà
điều chỉnh sự thực thi dựa trên khối lượng công việc
các đặc điểm (Use adaptive placement strategies that adjust execution based on workload characteristics).
Quá mức Dữ liệu
Sự di chuyển (Excessive Data Movement)
Thường xuyên bộ nhớ các sự truyền tải giới thiệu độ trễ và
làm tăng năng lượng sự tiêu thụ (Frequent memory transfers introduce latency and increase power consumption).
Giữ thường xuyên được sử dụng dữ liệu gần tới
tính toán các đơn vị và tối thiểu hóa ngoài-chip
bộ nhớ các truy cập (Keep frequently used data close to the compute units and minimize off-chip memory accesses).
Bị giới hạn Kết nối liên thông
Băng thông (Limited Interconnect Bandwidth)
Tồi được sắp đặt các hoạt động có thể tạo ra sự tắc nghẽn,
việc làm chậm dữ liệu sự di chuyển giữa các PE (Poorly placed operations can create congestion, slowing data movement between PEs).
Tối ưu hóa thuộc về không gian và thuộc về thời gian sự sắp đặt
để làm giảm sự giao tiếp chi phí chung (Optimize spatial and temporal placement to reduce communication overhead).
Cụ thể-cho-mô hình
Sự thực thi Các nhu cầu (Model-Specific Execution Needs)
Các CNN, các transformer, và các GNN yêu cầu khác nhau
sự thực thi các mẫu, việc làm một đơn sự sắp đặt
chiến lược không hiệu quả (CNNs, transformers, and GNNs require different execution patterns, making a single placement strategy ineffective).
May đo sự sắp đặt các chiến lược để khớp
tính toán cấu trúc của mỗi mô hình
loại (Tailor placement strategies to match the computational structure of each model type).
Bởi vì một tốt-được sắp đặt khối lượng công việc có thể làm giảm độ trễ bởi 10 tới 100 lần trong khi một tồi được sắp đặt một cái
để lại hàng ngàn của các PE nhàn rỗi, hiện đại các máy gia tốc ngày càng dựa trên nhận thức-thời gian chạy việc lập lịch trình
thứ mà thích ứng sự sắp đặt tới thời gian-thực khối lượng công việc hành vi thay vì tĩnh sự thực thi các kế hoạch (Because a well-placed workload can reduce latency by 10 to 100 times while a poorly placed one leaves thousands of PEs idle, modern accelerators increasingly rely on runtime-aware scheduling that adapts placement to real-time workload behavior rather than static execution plans). Sự sắp đặt

11. Phần cứng Sự gia tốc (Hardware Acceleration)
603
các quyết định cũng tương tác một cách trực tiếp với tiếp theo mối quan tâm: nơi dữ liệu những các PE đó cần thực sự cư trú
trong bộ nhớ hệ thống phân cấp (Placement decisions also interact directly with the next concern: where the data those PEs need actually resides in the memory hierarchy).
11.7.1.2 Bộ nhớ sự phân bổ (Memory allocation)
Trong khi tính toán sự sắp đặt xác định nơi các hoạt động thực thi, bộ nhớ sự phân bổ định nghĩa
nơi dữ liệu cư trú và cách nào nó chảy thông qua bộ nhớ hệ thống phân cấp trong suốt sự thực thi (While computation placement determines where operations execute, memory allocation defines where data resides and how it flows through the memory hierarchy during execution). Chính
mục tiêu là để giữ thường xuyên được truy cập dữ liệu cũng gần như có thể tới xử lý các phần tử, việc tối thiểu hóa
độ trễ và năng lượng sự tiêu thụ (The primary goal is to keep frequently accessed data as close as possible to the processing elements, minimizing latency and power consumption). Các GPU đạt được điều này thông qua một hỗn hợp của toàn cầu bộ nhớ, được chia sẻ
bộ nhớ, và các thanh ghi với cẩn thận việc xếp ô gạch các chiến lược (NVIDIA Corporation 2020) (GPUs achieve this through a mix of global memory, shared memory, and registers with careful tiling strategies (NVIDIA Corporation 2020)). Các TPU sử dụng trên-
chip SRAM các bộ nhớ nháp nơi các sự kích hoạt và các trọng số phải được tải trước để duy trì tâm thu mảng
sự thực thi (hình 11.8), với các trọng số được truyền phát trong hoàn hảo sự đồng bộ hóa với đầu vào các sự kích hoạt
để duy trì được đường ống hóa sự tính toán luồng (Jouppi et al. 2017) (TPUs use on-chip SRAM scratchpads where activations and weights must be preloaded to sustain systolic array execution (figure 11.8), with weights streamed in perfect synchronization with input activations to maintain pipelined computation flow (Jouppi et al. 2017)). Quy mô-tấm-wafer các bộ xử lý đòi hỏi
cẩn thận bộ nhớ sự phân vùng để tránh quá mức kết nối liên thông lưu lượng (Systems 2021) (Wafer-scale processors demand careful memory partitioning to avoid excessive interconnect traffic (Systems 2021)). Không giống đa-
mục đích việc điện toán, nơi các bộ nhớ cache trừu tượng hóa bộ nhớ sự quản lý, AI các máy gia tốc yêu cầu tường minh
dữ liệu sự sắp đặt các chiến lược bởi vì tồi sự phân bổ dẫn tới ba cộng gộp các hình phạt: được làm tăng
bộ nhớ độ trễ khi dữ liệu phải được lấy từ cao hơn-độ trễ các tầng, cao hơn năng lượng sự tiêu thụ
từ ngoài-chip các truy cập thứ mà tốn các bậc của độ lớn nhiều hơn năng lượng so với trên-chip lưu trữ, và được làm giảm
tính toán thông lượng khi xử lý các phần tử đình trệ việc chờ cho dữ liệu (Unlike general-purpose computing, where caches abstract memory management, AI accelerators require explicit data placement strategies because poor allocation leads to three compounding penalties: increased memory latency when data must be fetched from higher-latency tiers, higher power consumption from off-chip accesses that cost orders of magnitude more energy than on-chip storage, and reduced computational throughput when processing elements stall waiting for data).
Độ nghiêm trọng của những các hình phạt này thay đổi bởi khối lượng công việc (The severity of these penalties varies by workload). Các CNN dựa trên được cấu trúc, được cục bộ hóa truy cập
các mẫu và hưởng lợi từ được định nghĩa-tốt bộ nhớ các bố cục thứ mà tạo điều kiện có thể dự đoán sự tái sử dụng (Chen,
Krishna, et al. 2017) (CNNs rely on structured, localized access patterns and benefit from well-defined memory layouts that facilitate predictable reuse (Chen, Krishna, et al. 2017)). Transformer các mô hình yêu cầu thường xuyên truy cập tới lớn tham số các tập hợp và
trung gian các sự kích hoạt, việc làm chúng đánh kể nhạy cảm tới bộ nhớ băng thông các sự ràng buộc (Transformer models require frequent access to large parameter sets and intermediate activations, making them highly sensitive to memory bandwidth constraints). Các GNN
giới thiệu lớn nhất thách thức, như của chúng không đều và thưa thớt dữ liệu các cấu trúc sản xuất không thể dự đoán
truy cập các mẫu thứ mà chống lại tĩnh sự phân bổ các chiến lược (GNNs introduce the greatest challenge, as their irregular and sparse data structures produce unpredictable access patterns that resist static allocation strategies). Bảng 11.16 tóm tắt những sự phân bổ
các thách thức này (Table 11.16 summarizes these allocation challenges). Như mô hình các kích thước tiếp tục để phát triển, các máy gia tốc phải một cách động quản lý bộ nhớ
các tài nguyên thay vì việc dựa trên trên tĩnh sự phân bổ các lược đồ, và bộ nhớ khả năng ngày càng quyết định
cách nào lớn một mô hình có thể được triển khai trên một cho trước máy gia tốc (As model sizes continue to grow, accelerators must dynamically manage memory resources rather than relying on static allocation schemes, and memory capacity increasingly dictates how large a model can be deployed on a given accelerator).
Bảng 11.16: Bộ nhớ Sự phân bổ Các thách thức: Hiệu quả bộ nhớ sự quản lý trong AI các máy gia tốc cân bằng dữ liệu truy cập tốc độ với
phần cứng các sự ràng buộc, việc làm giảm bớt hiệu suất các nút thắt cổ chai được gây ra bởi độ trễ, băng thông các sự giới hạn, và không đều dữ liệu các mẫu (Table 11.16: Memory Allocation Challenges: Efficient memory management in AI accelerators balances data access speed with hardware constraints, mitigating performance bottlenecks caused by latency, bandwidth limitations, and irregular data patterns).
Phức tạp các mô hình chẳng hạn như các transformer và đồ thị các mạng áp đặt biến đổi và đòi hỏi bộ nhớ các yêu cầu thứ mà khuếch đại
những các thách thức này (Complex models such as transformers and graph networks impose variable and demanding memory requirements that amplify these challenges).
Thách thức (Challenge)
Tác động trên Sự thực thi (Impact on Execution)
Chính Các sự xem xét cho Sự phân bổ (Key Considerations for Allocation)
Cao Bộ nhớ
Độ trễ (High Memory Latency)
Chậm dữ liệu truy cập trì hoãn sự thực thi và làm giảm
thông lượng (Slow data access delays execution and reduces throughput).
Ưu tiên việc đặt thường xuyên được truy cập dữ liệu trong
nhanh hơn bộ nhớ các vị trí (Prioritize placing frequently accessed data in faster memory locations).
Bị giới hạn Trên-Chip
Lưu trữ (Limited On-Chip Storage)
Nhỏ cục bộ bộ nhớ ràng buộc lượng của
dữ liệu có sẵn gần tính toán các đơn vị (Small local memory constrains the amount of data available near compute units).
Phân bổ lưu trữ một cách hiệu quả để tối đa hóa dữ liệu
tính có sẵn mà không việc vượt quá phần cứng các giới hạn (Allocate storage efficiently to maximize data availability without exceeding hardware limits).
Cao Ngoài-Chip
Băng thông
Nhu cầu (High Off-Chip Bandwidth Demand)
Thường xuyên truy cập tới bên ngoài bộ nhớ làm tăng
các sự trì hoãn và năng lượng sự tiêu thụ (Frequent access to external memory increases delays and power consumption).
Làm giảm không cần thiết bộ nhớ các sự truyền tải bằng cách
một cách cẩn thận việc quản lý khi nào và cách nào dữ liệu là được di chuyển (Reduce unnecessary memory transfers by carefully managing when and how data is moved).
Không đều Bộ nhớ
Truy cập Các mẫu (Irregular Memory Access Patterns)
Một số các mô hình yêu cầu việc truy cập dữ liệu
một cách không thể dự đoán, việc dẫn tới không hiệu quả bộ nhớ
sự sử dụng (Some models require accessing data unpredictably, leading to inefficient memory usage).
Tổ chức bộ nhớ bố cục để căn chỉnh với truy cập
các mẫu và tối thiểu hóa không cần thiết dữ liệu
sự di chuyển (Organize memory layout to align with access patterns and minimize unnecessary data movement).
Cụ thể-cho-mô hình
Bộ nhớ Các nhu cầu (Model-Specific Memory Needs)
Khác nhau các mô hình yêu cầu khác nhau sự phân bổ
các chiến lược để tối ưu hóa hiệu suất (Different models require different allocation strategies to optimize performance).
May đo sự phân bổ các quyết định dựa trên cấu trúc
và sự thực thi các đặc điểm của khối lượng công việc (Tailor allocation decisions based on the structure and execution characteristics of the workload).
11.7.2 Tổ hợp độ phức tạp (Combinatorial complexity)
Nhỏ tích chập ví dụ cũng giải thích tại sao phần cứng sự ánh xạ trở thành một tổ hợp
tìm kiếm vấn đề (The small convolution example also explains why hardware mapping becomes a combinatorial search problem). Việc giữ một bộ lọc cục bộ cải thiện sự tái sử dụng chỉ nếu được chọn xử lý các phần tử có
đủ lân cận lưu trữ và nếu vòng lặp thứ tự truy cập lại đó bộ lọc trước khi dữ liệu là bị trục xuất (Keeping a filter local improves reuse only if the chosen processing elements have enough nearby storage and if the loop order revisits that filter before the data is evicted). Việc song song hóa
qua nhiều hơn xử lý các phần tử cải thiện thông lượng chỉ cho đến khi sự đồng bộ hóa và kết nối liên thông
lưu lượng tiêu thụ phần tăng (Parallelizing across more processing elements improves throughput only until synchronization and interconnect traffic consume the gain). Bảng 11.17 liệt kê những lặp lại các sự căng thẳng này: mỗi hàng là một cái khác cách cùng
ba các quyết định, sự sắp đặt, sự phân bổ, và việc lập lịch trình, ràng buộc lẫn nhau (Table 11.17 lists these recurring tensions: each row is another way the same three decisions, placement, allocation, and scheduling, constrain one another). Bởi vì mỗi hàng là
một độc lập sự đánh đổi với không chiếm ưu thế sự lựa chọn, tối ưu sự ánh xạ không thể được chọn một cách tham lam
một hàng tại một thời gian; các quyết định phải được tìm kiếm một cách chung, thứ mà là chính xác cái gì làm sự ánh xạ một
tổ hợp-tìm kiếm vấn đề với không có dạng-đóng mức tối ưu (Because every row is an independent trade-off with no dominant choice, the optimal mapping cannot be picked greedily one row at a time; the decisions must be searched jointly, which is precisely what makes mapping a combinatorial-search problem with no closed-form optimum).

604
11.7 Phần cứng Sự ánh xạ (Hardware Mapping)
Sự ánh xạ các sự lựa chọn bùng nổ
một cách tổ hợp như vòng lặp các chiều hướng
phát triển (Mapping choices explode combinatorially as loop dimensions grow).
Bảng 11.17: Sự sắp đặt-Sự phân bổ-Việc lập lịch trình Các sự đánh đổi: AI máy gia tốc hiệu suất phụ thuộc trên việc ánh xạ các sự tính toán tới
phần cứng, việc phân bổ dữ liệu tới bộ nhớ các tầng, và việc lập lịch trình sự thực thi qua thời gian (Table 11.17: Placement-Allocation-Scheduling Trade-Offs: AI accelerator performance depends on mapping computations to hardware, allocating data to memory tiers, and scheduling execution over time). Cẩn thận sự xem xét của những phụ thuộc lẫn nhau
các yếu tố này là cần thiết cho việc tối đa hóa thông lượng và việc tối thiểu hóa năng lượng sự tiêu thụ (Careful consideration of these interdependent factors is essential for maximizing throughput and minimizing energy consumption).
Chiều hướng (Dimension)
Sự sắp đặt Các sự xem xét (Placement Considerations)
Sự phân bổ và Việc lập lịch trình Các sự xem xét (Allocation and Scheduling Considerations)
Tính toán Độ hạt (Computational Granularity)
Độ hạt-mịn sự sắp đặt kích hoạt lớn hơn
tính song song nhưng làm tăng sự đồng bộ hóa
chi phí chung (Fine-grained placement enables greater parallelism but increases synchronization overhead).
Độ hạt-thô việc lập lịch trình làm giảm
sự đồng bộ hóa chi phí chung nhưng có thể giới hạn
tính linh hoạt (Coarse-grained scheduling reduces synchronization overhead but may limit flexibility).
Thuộc về không gian so với Thuộc về thời gian
Sự ánh xạ (Spatial vs. Temporal Mapping)
Thuộc về không gian sự sắp đặt tăng cường song song
sự thực thi nhưng có thể dẫn tới tài nguyên sự tranh chấp
và bộ nhớ sự tắc nghẽn (Spatial placement enhances parallel execution but can lead to resource contention and memory congestion).
Thuộc về thời gian việc lập lịch trình cân bằng tài nguyên
sự chia sẻ nhưng có thể làm giảm tổng thể thông lượng (Temporal scheduling balances resource sharing but may reduce overall throughput).
Bộ nhớ và Dữ liệu Tính cục bộ (Memory and Data Locality)
Việc đặt dữ liệu gần hơn tới tính toán các đơn vị
tối thiểu hóa độ trễ nhưng có thể làm giảm tổng thể
bộ nhớ tính có sẵn (Placing data closer to compute units minimizes latency but may reduce overall memory availability).
Việc phân bổ dữ liệu qua nhiều bộ nhớ
các cấp độ làm tăng khả năng nhưng giới thiệu
cao hơn truy cập các chi phí (Allocating data across multiple memory levels increases capacity but introduces higher access costs).
Sự giao tiếp và
Sự đồng bộ hóa (Communication and Synchronization)
Việc đồng-định vị tính toán các đơn vị làm giảm
sự giao tiếp độ trễ nhưng có thể giới thiệu
sự tranh chấp (Co-locating compute units reduces communication latency but may introduce contention).
Việc lập lịch trình sự đồng bộ hóa các cơ chế
làm giảm bớt các sự đình trệ nhưng có thể giới thiệu bổ sung
chi phí chung (Scheduling synchronization mechanisms mitigates stalls but can introduce additional overhead).
Dữ liệu luồng và Sự thực thi
Sự sắp xếp thứ tự (Dataflow and Execution Ordering)
Tĩnh sự sắp đặt làm đơn giản hóa sự thực thi nhưng
giới hạn khả năng thích ứng tới khối lượng công việc các sự biến thiên (Static placement simplifies execution but limits adaptability to workload variations).
Động việc lập lịch trình cải thiện khả năng thích ứng
nhưng cộng việc lập lịch trình độ phức tạp (Dynamic scheduling improves adaptability but adds scheduling complexity).
Những tương tác các yếu tố này định nghĩa một rộng lớn tổ hợp thiết kế không gian nơi nhỏ các sự biến thiên trong sự ánh xạ
các quyết định dẫn tới lớn các sự khác biệt trong hiệu suất và năng lượng tính hiệu quả (These interacting factors define a vast combinatorial design space where small variations in mapping decisions lead to large differences in performance and energy efficiency). Không giống truyền thống
các khối lượng công việc với có thể dự đoán sự thực thi các mẫu, máy học các mô hình giới thiệu đa dạng tính toán
các cấu trúc thứ mà yêu cầu các sự ánh xạ được thích ứng tới dữ liệu sự tái sử dụng, sự song song hóa các cơ hội, và
bộ nhớ các sự ràng buộc (Unlike traditional workloads with predictable execution patterns, machine learning models introduce diverse computational structures that require mappings adapted to data reuse, parallelization opportunities, and memory constraints). Tìm kiếm không gian phát triển một cách tổ hợp, việc làm cạn kiệt tìm kiếm không thể thực thi (The search space grows combinatorially, making exhaustive search infeasible).
Ba các nguồn của sự biến thiên đóng góp vào này độ phức tạp (Three sources of variation contribute to this complexity):
11.7.2.1 Việc sắp xếp thứ tự sự tính toán và sự thực thi (Ordering computation and execution)
Máy học các khối lượng công việc là thường được cấu trúc như lồng nhau các vòng lặp thứ mà lặp qua đa dạng các chiều hướng
của sự tính toán (Machine learning workloads are often structured as nested loops that iterate over various dimensions of computation). Cho ví dụ, một ma trận phép nhân hạt nhân có thể lặp qua lô kích thước (𝐵), đầu vào
các đặc trưng (𝐶in), và đầu ra các đặc trưng (𝐶out) (For instance, a matrix multiplication kernel may loop over batch size (𝐵), input features (𝐶in), and output features (𝐶out)). Thứ tự trong đó những vòng lặp này thực thi có một sâu sắc
hiệu ứng trên dữ liệu tính cục bộ, sự tái sử dụng các mẫu, và tính toán tính hiệu quả (The order in which these loops execute has a profound effect on data locality, reuse patterns, and computational efficiency).
Số lượng của các cách để sắp xếp 𝑛loops các vòng lặp tuân theo một giai thừa sự phát triển mẫu (The number of ways to arrange 𝑛loops loops follows a factorial growth pattern):
𝑁order = 𝑛loops!
thứ mà chia tỷ lệ một cách nhanh chóng (which scales rapidly). Một điển hình tích chập lớp có thể bao gồm lên tới bảy vòng lặp các chiều hướng, việc dẫn tới (A typical convolutional layer may involve up to seven loop dimensions, leading to):
7! = 5,040 có thể sự thực thi các thứ tự (possible execution orders).
Khi việc xem xét nhiều bộ nhớ các cấp độ, tìm kiếm không gian mở rộng như (When considering multiple memory levels, the search space expands as):
(𝑛loops!)𝑁mem
nơi 𝑁mem là số lượng của bộ nhớ hệ thống phân cấp các cấp độ (where 𝑁mem is the number of memory hierarchy levels). Này nhanh chóng sự mở rộng hiển thị tại sao sự thực thi
thứ tự sự tối ưu hóa quan trọng: tồi vòng lặp việc sắp xếp thứ tự có thể dẫn tới quá mức bộ nhớ lưu lượng, trong khi một
được tối ưu hóa thứ tự cải thiện bộ nhớ cache sự sử dụng (Sze et al. 2017) (This rapid expansion shows why execution order optimization matters: poor loop ordering can lead to excessive memory traffic, while an optimized order improves cache utilization (Sze et al. 2017)).
11.7.2.2 Sự song song hóa qua xử lý các phần tử (Parallelization across processing elements)
Hiện đại AI các máy gia tốc sử dụng hàng ngàn của xử lý các phần tử để tối đa hóa tính song song, nhưng việc xác
định cái nào các sự tính toán nên được song song hóa yêu cầu cẩn thận sự phân tích (Modern AI accelerators use thousands of processing elements to maximize parallelism, but determining which computations should be parallelized requires careful analysis). Quá mức sự song song hóa
có thể giới thiệu sự đồng bộ hóa các chi phí chung và được làm tăng băng thông các nhu cầu, trong khi không đủ
sự song song hóa dẫn tới bị sử dụng dưới mức phần cứng (Excessive parallelization can introduce synchronization overheads and increased bandwidth demands, while insufficient parallelization leads to underutilized hardware).
Số lượng của có thứ tự các cách để phân phối các sự tính toán giữa song song các đơn vị tuân theo sự hoán vị
số đếm (The number of ordered ways to distribute computations among parallel units follows the permutation count):
𝒫parallel = 𝑛loops! / (𝑛loops −𝑘parallel)!

11. Phần cứng Sự gia tốc (Hardware Acceleration)
605
nơi 𝑛loops là số lượng của các vòng lặp, và 𝑘parallel là số lượng được chọn cho song song sự thực thi (where 𝑛loops is the number of loops, and 𝑘parallel is the number selected for parallel execution). Cho
một sáu-vòng lặp sự tính toán nơi ba vòng lặp là được chọn cho song song sự thực thi, số lượng của hợp lệ
các cấu hình là (For a six-loop computation where three loops are chosen for parallel execution, the number of valid configurations is):
6! / (6−3)! = 120.
Thậm chí cho một đơn lớp, có thể có hàng trăm của hợp lệ sự song song hóa các chiến lược, mỗi cái việc ảnh hưởng
dữ liệu sự đồng bộ hóa, bộ nhớ sự tranh chấp, và tổng thể tính toán tính hiệu quả (Even for a single layer, there can be hundreds of valid parallelization strategies, each affecting data synchronization, memory contention, and overall compute efficiency). Việc mở rộng điều này qua
nhiều các lớp và mô hình các kiến trúc xa hơn phóng đại độ phức tạp (Expanding this across multiple layers and model architectures further magnifies the complexity).
11.7.2.3 Bộ nhớ sự sắp đặt và dữ liệu sự di chuyển (Memory placement and data movement)
Phân cấp bộ nhớ cấu trúc của AI các máy gia tốc giới thiệu bổ sung các sự ràng buộc, như dữ liệu phải
được một cách hiệu quả được đặt qua các thanh ghi, các bộ nhớ cache, được chia sẻ bộ nhớ, và ngoài-chip DRAM (The hierarchical memory structure of AI accelerators introduces additional constraints, as data must be efficiently placed across registers, caches, shared memory, and off-chip DRAM). Dữ liệu sự sắp đặt
tác động độ trễ, băng thông sự tiêu thụ, và năng lượng tính hiệu quả (Data placement impacts latency, bandwidth consumption, and energy efficiency). Thường xuyên truy cập tới chậm bộ nhớ
tạo ra các nút thắt cổ chai, trong khi được tối ưu hóa sự sắp đặt làm giảm tốn kém bộ nhớ các sự truyền tải (Frequent access to slow memory creates bottlenecks, while optimized placement reduces costly memory transfers).
Số lượng của các cách để phân bổ dữ liệu qua bộ nhớ các cấp độ tuân theo một hàm mũ sự phát triển hàm (The number of ways to allocate data across memory levels follows an exponential growth function):
ℳplacement = 𝑛^(𝑁comp×𝑁mem)
nơi (where):
• 𝑛 = số lượng của sự sắp đặt các sự lựa chọn trên mỗi cấp độ (number of placement choices per level),
• 𝑁comp = số lượng của tính toán các chiều hướng (number of computational dimensions),
• 𝑁mem = số lượng của bộ nhớ hệ thống phân cấp các cấp độ (number of memory hierarchy levels).
Cho một mô hình với (For a model with):
• 𝑁comp = 5 tính toán các chiều hướng (computational dimensions),
• 𝑁mem = 3 bộ nhớ các cấp độ (memory levels),
• 𝑛 = 4 có thể sự sắp đặt các sự lựa chọn trên mỗi cấp độ (possible placement choices per level),
số lượng của có thể bộ nhớ các sự phân bổ là (the number of possible memory allocations is):
4^(5×3) = 4^15 = 1,073,741,824.
11.7.2.4 Sự ánh xạ tìm kiếm không gian (Mapping search space)
Thậm chí một đơn lớp có thể có hơn một tỷ có thể bộ nhớ các cấu hình, việc làm thủ công sự tối
ưu hóa không thực tế (Even a single layer may have over a billion possible memory configurations, making manual optimization impractical). Bằng cách việc kết hợp độ phức tạp từ tính toán việc sắp xếp thứ tự, sự song song hóa, và
bộ nhớ sự sắp đặt, tổng sự ánh xạ tìm kiếm không gian có thể được xấp xỉ như (By combining the complexity from computation ordering, parallelization, and memory placement, the total mapping search space can be approximated as):
𝒮mapping = (𝑛^𝑁comp × 𝑛loops! × (𝑛loops! / (𝑛loops −𝑘parallel)!))^𝑁mem
nơi (where):
• 𝑛^𝑁comp đại diện bộ nhớ sự sắp đặt các sự lựa chọn (represents memory placement choices),
• 𝑛loops! giải thích cho tính toán việc sắp xếp thứ tự các sự lựa chọn (accounts for computation ordering choices),
• 𝑛loops! / (𝑛loops−𝑘parallel)! nắm bắt sự song song hóa các khả năng (captures parallelization possibilities),
• 𝑁mem là số lượng của bộ nhớ hệ thống phân cấp các cấp độ (is the number of memory hierarchy levels).
Phương trình này minh họa hàm mũ sự phát triển của tìm kiếm không gian, việc làm vét cạn tìm kiếm
không thể thực thi cho tất cả ngoại trừ đơn giản nhất các trường hợp (This equation illustrates the exponential growth of the search space, making brute-force search infeasible for all but the simplest cases). Một cụ thể ví dụ làm tác động của những các sự lựa chọn này
hữu hình (A concrete example makes the impact of these choices tangible).
Ví dụ 11.3 (Example 11.3): Vòng lặp việc sắp xếp thứ tự trong một nhỏ tích chập (Loop ordering in a small convolution)
Xem xét một tích chập việc áp dụng 16 các bộ lọc của kích thước 3×3 tới một 8×8 đơn-kênh đầu vào (Consider a convolution applying 16 filters of size 3×3 to an 8×8 single-channel input). Các
sự tính toán có thể được biểu diễn như năm lồng nhau các vòng lặp việc lặp qua đầu ra các hàng (𝐻out), đầu ra (The computation can be expressed as five nested loops iterating over output rows (𝐻out), output)

606
11.8 Dữ liệu luồng Sự tối ưu hóa (Dataflow Optimization)
các cột (𝑊out), bộ lọc số đếm (𝐶out), bộ lọc chiều cao (𝐹ℎ), và bộ lọc chiều rộng (𝐹𝑤) (columns (𝑊out), filter count (𝐶out), filter height (𝐹ℎ), and filter width (𝐹𝑤)). Các 5! = 120 có thể
các sự sắp xếp thứ tự của những vòng lặp này tất cả sản xuất cùng bằng số kết quả, nhưng chúng tạo ra một cách đáng kể
khác nhau bộ nhớ lưu lượng (The 5! = 120 possible orderings of these loops all produce the same numerical result, but they generate dramatically different memory traffic).
Sự sắp xếp thứ tự A (trọng số-tính cố định) (Ordering A (weight-stationary)): Đặt bộ lọc các vòng lặp (𝐶out, 𝐹ℎ, 𝐹𝑤) ngoài cùng và thuộc về không gian
các vòng lặp (𝐻out, 𝑊out) trong cùng (Place the filter loops (𝐶out, 𝐹ℎ, 𝐹𝑤) outermost and the spatial loops (𝐻out, 𝑊out) innermost). Mỗi 3×3 bộ lọc là được tải vào các thanh ghi một lần và sau đó được áp dụng
qua tất cả 36 đầu ra các vị trí trước khi tiếp theo bộ lọc là được tải (Each 3×3 filter is loaded into registers once and then applied across all 36 output positions before the next filter is loaded). Tổng trọng số các lượt tải: 16×9 = 144
các giá trị, mỗi cái được tải chính xác một lần (Total weight loads: 16×9 = 144 values, each loaded exactly once).
Sự sắp xếp thứ tự B (đầu ra-tính cố định) (Ordering B (output-stationary)): Đặt thuộc về không gian các vòng lặp ngoài cùng và bộ lọc các vòng lặp trong
cùng (Place the spatial loops outermost and the filter loops innermost). Cho mọi đầu ra vị trí, tất cả 16 các bộ lọc phải được tải, được áp dụng, và của chúng một phần các tổng
được tích lũy trước khi việc tiến lên tới tiếp theo vị trí (For every output position, all 16 filters must be loaded, applied, and their partial sums accumulated before advancing to the next position). Nếu thanh ghi tệp không thể giữ tất cả 16 các bộ lọc
một cách đồng thời, các bộ lọc là một cách lặp lại được lấy từ bộ nhớ cache hoặc DRAM (If the register file cannot hold all 16 filters simultaneously, filters are repeatedly fetched from cache or DRAM). Trong tệ nhất trường hợp, mỗi của
36 đầu ra các vị trí tải lại tất cả 144 bộ lọc các trọng số, việc sản xuất 36×144 = 5,184 trọng số các lượt đọc (In the worst case, each of the 36 output positions reloads all 144 filter weights, producing 36×144 = 5,184 weight reads).
Các hệ thống sự thấu hiểu (Systems insight): Sự sắp xếp thứ tự A làm giảm trọng số lưu lượng bởi 36× so với Sự sắp xếp thứ tự B bằng cách việc khớp
vòng lặp cấu trúc tới một trọng số-tính cố định dữ liệu luồng (Ordering A reduces weight traffic by 36× compared to Ordering B by matching the loop structure to a weight-stationary dataflow). Này đơn sự sắp xếp lại quyết định, một của
120 các khả năng được dự đoán bởi 𝑛loops! = 5! = 120 công thức, xác định liệu máy gia
tốc dành của nó bộ nhớ băng thông việc tải tươi mới dữ liệu hoặc một cách dư thừa việc lấy-lại các trọng số nó
đã nhìn thấy (This single reordering decision, one of the 120 possibilities predicted by the 𝑛loops! = 5! = 120 formula, determines whether the accelerator spends its memory bandwidth loading fresh data or redundantly re-fetching weights it has already seen).
Tổ hợp sự bùng nổ được tiết lộ bởi này sự phân tích, có khả năng hàng tỷ của hợp lệ các cấu hình
cho một đơn thần kinh mạng lớp, đặt ra một thực tế thách thức: việc giải thích cách nào các nhà thực hành đạt được
mạnh mẽ hiệu suất mặc dù này rộng lớn tìm kiếm không gian (The combinatorial explosion revealed by this analysis, potentially billions of valid configurations for a single neural network layer, poses a practical challenge: explaining how practitioners achieve strong performance despite this vast search space). Vét cạn sự liệt kê là không thể, tuy nhiên
sản xuất các hệ thống một cách thường lệ tìm thấy hữu dụng các lịch trình cho phổ biến các hạt nhân (Exhaustive enumeration is impossible, yet production systems routinely find useful schedules for common kernels). Câu trả lời nằm trong một nhỏ
tập hợp của có nguyên tắc dữ liệu luồng các mẫu thứ mà làm giảm này khó xử lý cấu hình không gian tới một có thể quản lý
tập hợp của có chiến lược các sự lựa chọn (The answer lies in a small set of principled dataflow patterns that reduce this intractable configuration space to a manageable set of strategic choices).
11.8 Dữ liệu luồng Sự tối ưu hóa (Dataflow Optimization)
Sự ánh xạ các chiến lược từ đứng trước phần thiết lập nơi các sự tính toán thực thi và nơi
dữ liệu cư trú, nhưng chúng không chỉ định dữ liệu luồng sự tối ưu hóa: cách nào dữ liệu chảy thông qua xử lý
các phần tử trong suốt sự thực thi (The mapping strategies from the preceding section establish where computations execute and where data resides, but they do not specify dataflow optimization: how data flows through processing elements during execution). Một tâm thu mảng có thể xử lý một ma trận phép nhân với các trọng số trong
cục bộ bộ nhớ, nhưng thứ tự trong đó các trọng số, các đầu vào, và các đầu ra di chuyển thông qua mảng một cách trực tiếp
xác định bộ nhớ băng thông sự tiêu thụ và năng lượng tính hiệu quả (A systolic array might process a matrix multiplication with weights in local memory, but the order in which weights, inputs, and outputs move through the array directly determines memory bandwidth consumption and energy efficiency). Sự lựa chọn giữa các chiến lược
một cách trực tiếp tác động liệu một máy gia tốc hoạt động trong bị ràng buộc-bởi-tính toán hoặc bị ràng buộc-bởi-bộ nhớ vùng
được xác định bởi Đường mái nhà sự phân tích—thứ mà là tại sao các trình biên dịch (phần 11.9) và thời gian chạy các hệ thống
(phần 11.10) phải chọn thích hợp dữ liệu luồng các mẫu dựa trên khối lượng công việc các đặc điểm (The choice among strategies directly impacts whether an accelerator operates in the compute-bound or memory-bound region identified by the Roofline analysis—which is why compilers (section 11.9) and runtime systems (section 11.10) must select appropriate dataflow patterns based on workload characteristics).
Ba các quyết định cấu trúc tất cả dữ liệu luồng sự tối ưu hóa (Three decisions structure all dataflow optimization):
1. Tính cục bộ (Locality): Trọng số-tính cố định, đầu ra-tính cố định, và đầu vào-tính cố định các chiến lược mỗi cái thực hiện
khác nhau các sự lựa chọn về cái gì để lưu bộ nhớ cache gần tính toán các đơn vị, việc đánh đổi khác nhau bộ nhớ truy cập
các mẫu (Weight-stationary, output-stationary, and input-stationary strategies each make different choices about what to cache near compute units, trading off different memory access patterns).
2. Sự tổ chức (Organization): Tensor các bố cục (NHWC so với NCHW) xác định liệu bộ nhớ các truy cập
căn chỉnh với phần cứng các sở thích, với hiệu suất các tác động thứ mà có thể là lớn khi bố cục
các sự chuyển đổi hoặc không được kết hợp truy cập chặn nhanh đường dẫn (Tensor layouts (NHWC vs. NCHW) determine whether memory accesses align with hardware preferences, with performance impacts that can be large when layout conversions or uncoalesced access block the fast path).
3. Sự kết hợp (Combination): Hạt nhân sự hợp nhất và việc xếp ô gạch tái cấu trúc sự tính toán để tối thiểu hóa bộ nhớ lưu lượng, thường
xuyên việc sản xuất lớn các phần tăng tốc trên thấp-số học-cường độ các hoạt động bằng cách việc tránh trung gian
các lượt ghi và các lượt tải lại (Kernel fusion and tiling restructure computation to minimize memory traffic, often producing large speedups on low-arithmetic-intensity operations by avoiding intermediate writes and reloads).
Bằng cách việc làm chủ những các mẫu này, chúng ta có thể lập luận về 90 phần trăm của dữ liệu luồng sự tối ưu hóa các quyết định
mà không vét cạn tìm kiếm (By mastering these patterns, we can reason about 90 percent of dataflow optimization decisions without exhaustive search). Tiếp theo các phần kiểm tra mỗi quyết định trong lượt, sau đó hiển thị cách nào chúng
kết hợp cho cụ thể thần kinh mạng các kiến trúc bao gồm ResNet-50, GPT-2, và các MLP (The next sections examine each decision in turn, then show how they combine for specific neural network architectures including ResNet-50, GPT-2, and MLPs).
11.8.1 Xây dựng các khối của sự ánh xạ các chiến lược (Building blocks of mapping strategies)
Đứng trước ba các quyết định ánh xạ tới bốn nền tảng các kỹ thuật: dữ liệu sự di chuyển các mẫu
(trọng số-tính cố định, đầu ra-tính cố định, đầu vào-tính cố định), hiệu quả-bộ nhớ tensor các bố cục (hàng-chính
so với kênh-chính), hạt nhân sự hợp nhất (việc kết hợp các hoạt động để loại bỏ trung gian các lượt ghi), và việc xếp ô gạch (The preceding three decisions map to four foundational techniques: data movement patterns (weight-stationary, output-stationary, input-stationary), memory-efficient tensor layouts (row-major vs. channel-major), kernel fusion (combining operations to eliminate intermediate writes), and tiling)

11. Phần cứng Sự gia tốc (Hardware Acceleration)
607
(việc phân vùng các sự tính toán thành thân thiện-với-bộ nhớ các khối) ((partitioning computations into memory-friendly blocks)). Cùng nhau, những xây dựng các khối này làm giảm
sự ánh xạ tìm kiếm không gian: theo kinh nghiệm và được dẫn dắt-bởi-mô hình các bộ tối ưu hóa có thể kết hợp chúng thay vì
việc khám phá lại cùng dữ liệu-sự di chuyển các sự lựa chọn từ đầu (Together, these building blocks reduce the mapping search space: heuristic and model-driven optimizers can combine them instead of rediscovering the same data-movement choices from scratch).
11.8.1.1 Dữ liệu sự di chuyển các mẫu (Data movement patterns)
Trong khi tính toán sự ánh xạ xác định nơi và khi nào các hoạt động xảy ra, của nó sự thành công phụ thuộc
nặng nề trên cách nào một cách hiệu quả dữ liệu là được truy cập và được truyền tải qua bộ nhớ hệ thống phân cấp (While computational mapping determines where and when operations occur, its success depends heavily on how efficiently data is accessed and transferred across the memory hierarchy). Như được thảo luận
trong phần 11.5.2.2, máy học các khối lượng công việc trưng bày không đều truy cập các mẫu thứ mà thách thức
tiêu chuẩn việc lưu bộ nhớ cache các cơ chế (As discussed in section 11.5.2.2, machine learning workloads exhibit irregular access patterns that challenge standard caching mechanisms). Này tính không đều làm dữ liệu sự di chuyển chiến lược tới hạn tới tổng thể
hệ thống hiệu suất (This irregularity makes data movement strategy critical to overall system performance).
Thậm chí khi tính toán các đơn vị là được ánh xạ một cách hiệu quả, tồi dữ liệu sự di chuyển các chiến lược làm giảm
hiệu suất bằng cách việc gây ra thường xuyên bộ nhớ các sự đình trệ và việc để lại phần cứng các tài nguyên nhàn rỗi (Even when computational units are mapped efficiently, poor data movement strategies degrade performance by causing frequent memory stalls and leaving hardware resources idle). Nếu dữ liệu không thể
được cung cấp tới xử lý các phần tử tại yêu cầu tỷ lệ, tính toán các đơn vị đình trệ, việc làm tăng độ trễ,
bộ nhớ lưu lượng, và năng lượng sự tiêu thụ (Chen, Krishna, et al. 2017) (If data cannot be supplied to processing elements at the required rate, computational units stall, increasing latency, memory traffic, and energy consumption (Chen, Krishna, et al. 2017)). Danh sách 11.15 minh họa cách nào
dữ liệu sự di chuyển các sự không hiệu quả ảnh hưởng xương sống sự tính toán của nhiều máy học các mô hình
thông qua một điển hình ma trận phép nhân hoạt động (Listing 11.15 illustrates how data movement inefficiencies affect the backbone computation of many machine learning models through a typical matrix multiplication operation).
Danh sách 11.15: Ma trận Phép nhân: Dữ liệu sự di chuyển các nút thắt cổ chai để lại phần cứng các tài nguyên nhàn rỗi, việc chứng minh tại sao hiệu quả
dữ liệu luồng xác định máy học mô hình hiệu suất (Listing 11.15: Matrix Multiplication: Data movement bottlenecks leave hardware resources idle, demonstrating why efficient data flow determines machine learning model performance).
## Ma trận phép nhân nơi (Matrix multiplication where):
## các trọng số (weights): [$512{\times}256$] - mô hình các tham số (model parameters)
## đầu vào (input):
[$256{\times}32$]
- lô của các sự kích hoạt (batch of activations)
## Z:
[$512{\times}32$]
- đầu ra các sự kích hoạt (output activations)
## Việc tính toán mỗi đầu ra phần tử Z[i,j] (Computing each output element Z[i,j]):
cho (for) i trong phạm vi (in range)(512):
cho (for) j trong phạm vi (in range)(32):
cho (for) k trong phạm vi (in range)(256):
Z[i, j] += weights[i, k] * input[k, j]
Sự tính toán này tiết lộ một vài tới hạn dữ liệu luồng các thách thức (This computation reveals several critical dataflow challenges). Đầu tiên thách thức là số lượng
của bộ nhớ các truy cập được yêu cầu (The first challenge is the number of memory accesses required). Cho mỗi đầu ra 𝑍[𝑖,𝑗], sự tính toán phải lấy một toàn bộ hàng của
các trọng số từ trọng số ma trận và một đầy đủ cột của các sự kích hoạt từ đầu vào ma trận (For each output 𝑍[𝑖,𝑗], the computation must fetch an entire row of weights from the weight matrix and a full column of activations from the input matrix). Vì
trọng số ma trận chứa 512 các hàng và đầu vào ma trận chứa 32 các cột, điều này dẫn tới lặp lại
bộ nhớ các truy cập thứ mà đặt một nặng gánh nặng trên bộ nhớ băng thông (Since the weight matrix contains 512 rows and the input matrix contains 32 columns, this results in repeated memory accesses that place a heavy burden on memory bandwidth).
Thứ hai thách thức đến từ trọng số sự tái sử dụng (The second challenge comes from weight reuse). Cùng các trọng số là được áp dụng tới nhiều các đầu vào,
việc có nghĩa rằng một lý tưởng sự ánh xạ chiến lược nên tối đa hóa trọng số tính cục bộ để tránh dư thừa
bộ nhớ các lượt lấy (The same weights are applied to multiple inputs, meaning that an ideal mapping strategy should maximize weight locality to avoid redundant memory fetches). Không có thích hợp sự tái sử dụng, máy gia tốc sẽ lãng phí băng thông việc tải cùng
các trọng số nhiều lần (Chen et al. 2018) (Without proper reuse, the accelerator would waste bandwidth loading the same weights multiple times (Chen et al. 2018)).
Thứ ba thách thức liên quan tới sự tích lũy của trung gian các kết quả (The third challenge involves the accumulation of intermediate results). Vì mỗi phần tử trong
𝑍[𝑖,𝑗] yêu cầu các sự đóng góp từ 256 khác nhau trọng số-đầu vào các cặp, một phần các tổng phải được lưu trữ và
được lấy lại trước khi cuối cùng giá trị là được tính toán (Since each element in 𝑍[𝑖,𝑗] requires contributions from 256 different weight-input pairs, partial sums must be stored and retrieved before the final value is computed). Nếu những trung gian các giá trị này là được lưu trữ một cách không hiệu quả,
hệ thống sẽ yêu cầu thường xuyên bộ nhớ các truy cập, xa hơn việc làm tăng băng thông các nhu cầu (If these intermediate values are stored inefficiently, the system will require frequent memory accesses, further increasing bandwidth demands).
Một cách để làm giảm bớt những các thách thức này là để sử dụng SIMD và SIMT sự thực thi các mô hình, thứ mà cho phép
nhiều các giá trị để được lấy trong song song (One way to mitigate these challenges is to use SIMD and SIMT execution models, which allow multiple values to be fetched in parallel). Tuy nhiên, thậm chí với những các sự tối ưu hóa này, dữ liệu sự di chuyển
duy trì một nút thắt cổ chai (However, even with these optimizations, data movement remains a bottleneck). Vấn đề là không chỉ cách nào nhanh chóng dữ liệu là được lấy lại mà cách nào thường xuyên nó phải được
di chuyển và nơi nó là được đặt bên trong bộ nhớ hệ thống phân cấp (Han, Liu, et al. 2016) (The issue is not just how quickly data is retrieved but how often it must be moved and where it is placed within the memory hierarchy (Han, Liu, et al. 2016)).
Bởi vì việc di chuyển dữ liệu thống trị năng lượng ngân sách thứ mà hình 11.9 lập biểu đồ, đơn quan trọng nhất mục
tiêu của một máy gia tốc là để tối thiểu hóa bộ nhớ truy cập (Because moving data dominates the energy budget that figure 11.9 charts, the single most important goal of an accelerator is to minimize memory access). Dữ liệu luồng các chiến lược đạt được điều này bằng cách
việc tối đa hóa dữ liệu sự tái sử dụng (Dataflow strategies achieve this by maximizing data reuse). Trung tâm quyết định là cái nào dữ liệu là có giá trị nhất để giữ cục bộ (The central decision is which data is most valuable to keep local). Các máy gia
tốc trả lời đó quyết định bằng cách việc xác định cái nào dữ liệu duy trì cố định trong bộ nhớ và cái nào dữ liệu
truyền phát một cách động: trọng số-tính cố định giữ mô hình các tham số cục bộ, đầu vào-tính cố định duy trì
sự kích hoạt dữ liệu, và đầu ra-tính cố định bảo tồn trung gian các kết quả (Accelerators answer that decision by determining which data remains fixed in memory and which data streams dynamically: weight-stationary keeps model parameters local, input-stationary maintains activation data, and output-stationary preserves intermediate results). Mỗi cách tiếp cận đánh đổi khác
nhau bộ nhớ truy cập các mẫu để tối đa hóa dữ liệu sự tái sử dụng và tối thiểu hóa chuyên sâu-năng lượng các sự truyền tải
thứ mà cấu thành chính nút thắt cổ chai trong AI sự gia tốc (Each approach trades off different memory access patterns to maximize data reuse and minimize the energy-intensive transfers that constitute the primary bottleneck in AI acceleration).

608
11.8 Dữ liệu luồng Sự tối ưu hóa (Dataflow Optimization)
Trọng số tính cố định (Weight stationary) Trọng số tính cố định chiến lược giữ các trọng số cố định trong cục bộ bộ nhớ, trong khi đầu vào
các sự kích hoạt và một phần các tổng là được truyền phát thông qua hệ thống (The weight stationary strategy keeps weights fixed in local memory, while input activations and partial sums are streamed through the system). Trọng số tính cố định các cách tiếp cận chứng minh
đặc biệt có lợi trong các CNN và ma trận các phép nhân, nơi cùng tập hợp của các trọng số là được áp dụng
qua nhiều các đầu vào (Weight stationary approaches prove particularly beneficial in CNNs and matrix multiplications, where the same set of weights is applied across multiple inputs). Bằng cách việc đảm bảo các trọng số duy trì tĩnh, này phương pháp làm giảm dư thừa
bộ nhớ các lượt lấy, thứ mà giúp làm giảm bớt băng thông các nút thắt cổ chai và cải thiện năng lượng tính hiệu quả (By ensuring weights remain stationary, this method reduces redundant memory fetches, which helps alleviate bandwidth bottlenecks and improves energy efficiency).
Một chính lợi thế của trọng số tính cố định là rằng nó tối đa hóa trọng số sự tái sử dụng, việc làm giảm tần suất
của bộ nhớ các truy cập tới bên ngoài lưu trữ (A key advantage of weight stationary is that it maximizes weight reuse, reducing the frequency of memory accesses to external storage). Vì trọng số các tham số là thường được chia sẻ qua nhiều
các sự tính toán, việc giữ chúng trong cục bộ bộ nhớ loại bỏ không cần thiết dữ liệu sự di chuyển, việc hạ thấp
tổng thể năng lượng chi phí của sự tính toán (Since weight parameters are often shared across multiple computations, keeping them in local memory eliminates unnecessary data movement, lowering the overall energy cost of computation). Điều này làm nó đặc biệt hiệu quả cho các kiến trúc nơi
các trọng số đại diện thống trị bộ nhớ chi phí chung, chẳng hạn như tâm thu các mảng và tùy chỉnh các máy gia tốc
được thiết kế cho máy học (This makes it particularly effective for architectures where weights represent the dominant memory overhead, such as systolic arrays and custom accelerators designed for machine learning). Danh sách 11.16 chứng minh cách nào Trọng số Tính cố định sự thực thi giữ
các trọng số cố định trong cục bộ bộ nhớ trong khi việc truyền phát các đầu vào và việc tích lũy một phần các tổng (Listing 11.16 demonstrates how Weight Stationary execution keeps weights fixed in local memory while streaming inputs and accumulating partial sums).
Danh sách 11.16: Trọng số Tính cố định Dữ liệu luồng: Các trọng số ở lại thường trú trong cục bộ bộ nhớ trong khi các đầu vào và một phần các tổng truyền phát thông qua,
việc tối thiểu hóa tham số đọc lưu lượng; tốt nhất cho các CNN và ma trận các phép nhân với nặng trọng số sự tái sử dụng (Listing 11.16: Weight Stationary Dataflow: Weights stay resident in local memory while inputs and partial sums stream through, minimizing parameter read traffic; best for CNNs and matrix multiplications with heavy weight reuse).
## Trọng số Tính cố định Ma trận Phép nhân (Weight Stationary Matrix Multiplication)
## - Các trọng số duy trì cố định trong cục bộ bộ nhớ (Weights remain fixed in local memory)
## - Đầu vào các sự kích hoạt truyền phát thông qua (Input activations stream through)
## - Một phần các tổng tích lũy cho cuối cùng đầu ra (Partial sums accumulate for final output)
cho (for) weight_block trong (in) weights:
# Tải và giữ các trọng số cố định (Load and keep weights stationary)
load_to_local(weight_block)
# Cố định trong cục bộ lưu trữ (Fixed in local storage)
cho (for) input_block trong (in) inputs:
# Truyền phát các đầu vào một cách động (Stream inputs dynamically)
cho (for) output_block trong (in) outputs:
# Tính toán các kết quả (Compute results)
output_block += compute(weight_block, input_block)
# Tái sử dụng các trọng số qua các đầu vào (Reuse weights across inputs)
Trong trọng số tính cố định sự thực thi, các trọng số là được tải một lần vào cục bộ bộ nhớ và duy trì cố định
trong suốt sự tính toán trong khi các đầu vào truyền phát một cách động, việc làm giảm dư thừa bộ nhớ các truy cập (In weight stationary execution, weights are loaded once into local memory and remain fixed throughout the computation while inputs stream dynamically, reducing redundant memory accesses).
Một phần các tổng tích lũy một cách hiệu quả, việc tối thiểu hóa không cần thiết dữ liệu sự di chuyển (Partial sums accumulate efficiently, minimizing unnecessary data movement). Bởi vì các trọng số cần
không được tải lại cho mỗi mới sự tính toán, băng thông các yêu cầu giảm một cách đáng kể, việc làm này
dữ liệu luồng cao hiệu quả cho các khối lượng công việc với nặng trọng số sự tái sử dụng các mẫu chẳng hạn như các CNN và ma trận
các phép nhân (Because weights need not be reloaded for each new computation, bandwidth requirements drop significantly, making this dataflow highly effective for workloads with heavy weight reuse patterns such as CNNs and matrix multiplications).
Tuy nhiên, trong khi này chiến lược làm giảm liên quan-tới-trọng số bộ nhớ lưu lượng, nó giới thiệu các sự đánh đổi trong
đầu vào và đầu ra sự di chuyển (However, while this strategy reduces weight-related memory traffic, it introduces trade-offs in input and output movement). Vì các đầu vào phải được truyền phát một cách động trong khi các trọng số duy trì
cố định, tính hiệu quả của này cách tiếp cận phụ thuộc trên cách nào tốt đầu vào các sự kích hoạt có thể được phân phối tới
tính toán các đơn vị mà không việc gây ra các sự đình trệ (Since inputs must be streamed dynamically while weights remain fixed, the efficiency of this approach depends on how well input activations can be delivered to the computational units without causing stalls). Một phần các tổng, thứ mà đại diện trung gian các kết quả, phải
cũng được một cách cẩn thận được tích lũy để tránh quá mức bộ nhớ lưu lượng (Partial sums, which represent intermediate results, must also be carefully accumulated to avoid excessive memory traffic). Tổng hiệu suất phần tăng phụ thuộc
trên kích thước của có sẵn trên-chip bộ nhớ, như việc lưu trữ lớn hơn trọng số các ma trận một cách cục bộ có thể trở thành một
sự ràng buộc trong các mô hình với hàng triệu hoặc hàng tỷ của các tham số (The total performance gain depends on the size of available on-chip memory, as storing larger weight matrices locally can become a constraint in models with millions or billions of parameters).
Trọng số tính cố định chiến lược là phù hợp-tốt cho các khối lượng công việc nơi các trọng số trưng bày cao sự tái sử dụng
và bộ nhớ băng thông là một giới hạn yếu tố (The weight stationary strategy is well-suited for workloads where weights exhibit high reuse and memory bandwidth is a limiting factor). Nó là một cách phổ biến được tuyển dụng trong các CNN, tâm thu các mảng,
và ma trận phép nhân các hạt nhân, nơi được cấu trúc trọng số sự tái sử dụng dẫn tới có thể đo lường hiệu suất
các sự cải thiện (It is commonly employed in CNNs, systolic arrays, and matrix multiplication kernels, where structured weight reuse leads to measurable performance improvements). Tuy nhiên, cho các mô hình nơi đầu vào hoặc đầu ra sự tái sử dụng là nhiều hơn tới hạn, thay thế
dữ liệu luồng các chiến lược, chẳng hạn như đầu ra tính cố định hoặc đầu vào tính cố định, có thể cung cấp tốt hơn các sự đánh đổi (However, for models where input or output reuse is more critical, alternative dataflow strategies, such as output stationary or input stationary, may provide better trade-offs).
Đầu ra tính cố định (Output stationary) Trọng số tính cố định giữ các trọng số cục bộ và truyền phát các đầu vào thông qua hệ thống (Weight stationary keeps weights local and streams inputs through the system).
Thống trị chi phí chuyển đổi, tuy nhiên, khi nút thắt cổ chai là không trọng số việc tải mà thường xuyên
các lượt ghi của một phần các tổng (The dominant cost shifts, however, when the bottleneck is not weight loading but the frequent writes of partial sums). Trong hoàn toàn được kết nối các lớp và transformer sự chú ý các cơ chế, mỗi đầu ra
phần tử tích lũy các sự đóng góp từ hàng trăm hoặc hàng ngàn của trọng số-đầu vào các cặp (In fully connected layers and transformer attention mechanisms, each output element accumulates contributions from hundreds or thousands of weight-input pairs). Việc ghi
những trung gian một phần các tổng đó tới bên ngoài bộ nhớ sau mọi tích lũy bước sẽ tạo ra một
ghi-băng thông nút thắt cổ chai xa nhiều hơn nghiêm trọng so với đọc chi phí chung thứ mà trọng số tính cố định giải quyết (Writing those intermediate partial sums to external memory after every accumulation step would create a write-bandwidth bottleneck far more severe than the read overhead that weight stationary addresses).
Đầu ra tính cố định chiến lược đảo ngược ưu tiên: nó giữ một phần các tổng cố định trong cục bộ bộ nhớ trong khi
việc truyền phát cả các trọng số và đầu vào các sự kích hoạt thông qua hệ thống, để mà mỗi đầu ra phần tử là
được ghi tới bên ngoài bộ nhớ chỉ một lần, sau khi tất cả của nó các sự đóng góp đã được tích lũy (Chen,
Krishna, et al. 2017) (The output stationary strategy inverts the priority: it keeps partial sums fixed in local memory while streaming both weights and input activations through the system, so that each output element is written to external memory only once, after all its contributions have been accumulated (Chen, Krishna, et al. 2017)).

11. Phần cứng Sự gia tốc (Hardware Acceleration)
609
Danh sách 11.17 chứng minh cách nào việc tích lũy một phần các tổng một cách cục bộ tối thiểu hóa bộ nhớ các lượt ghi
và tăng cường tính hiệu quả trong suốt ma trận phép nhân (Listing 11.17 demonstrates how accumulating partial sums locally minimizes memory writes and enhances efficiency during matrix multiplication). Trong này sự triển khai, bộ tích lũy
bộ đệm ở lại trong cục bộ các thanh ghi hoặc bộ nhớ nháp trong suốt trong cùng vòng lặp; các trọng số và các đầu vào truyền phát
vào, đóng góp tới đang chạy tổng, và là bị loại bỏ (In this implementation, the accumulator buffer stays in local registers or scratchpad throughout the inner loop; weights and inputs stream in, contribute to the running sum, and are discarded). Cuối cùng kết quả là được ghi ra chỉ một lần trên mỗi
đầu ra phần tử, việc loại bỏ lặp lại ghi lưu lượng thứ mà sẽ nếu không thống trị băng thông (The final result is written out only once per output element, eliminating the repeated write traffic that would otherwise dominate bandwidth).
Danh sách 11.17: Đầu ra Tính cố định Dữ liệu luồng: Một phần các tổng ở lại thường trú trong cục bộ bộ nhớ trong khi các trọng số và các đầu vào truyền phát thông qua,
vì vậy mỗi đầu ra là được ghi ra chỉ một lần, việc tối thiểu hóa sự tích lũy ghi lưu lượng; tốt nhất cho hoàn toàn được kết nối các lớp và sự chú ý (Listing 11.17: Output Stationary Dataflow: Partial sums stay resident in local memory while weights and inputs stream through, so each output is written out only once, minimizing accumulation write traffic; best for fully connected layers and attention).
## - Một phần các tổng duy trì trong cục bộ bộ nhớ (Partial sums remain in local memory)
## - Các trọng số và đầu vào các sự kích hoạt truyền phát thông qua một cách động (Weights and input activations stream through dynamically)
## - Cuối cùng các đầu ra là được ghi chỉ một lần (Final outputs are written only once)
cho (for) output_block trong (in) outputs:
# Giữ một phần các tổng tĩnh (Keep partial sums stationary)
accumulator = 0
# Khởi tạo sự tích lũy bộ đệm (Initialize accumulation buffer)
cho (for) weight_block, input_block trong (in) zip(weights, inputs):
accumulator += compute(weight_block, input_block)
# Tích lũy một phần các tổng (Accumulate partial sums)
store_output(accumulator)
# Đơn lượt ghi tới bộ nhớ (Single write to memory)
Cách tiếp cận này căn chỉnh một cách tự nhiên với tâm thu các mảng, nơi sự tính toán tiến triển thông qua một
lưới của xử lý các phần tử và một phần các tổng có thể chảy dọc theo một trục mà không việc rời khỏi chip (This approach aligns naturally with systolic arrays, where computation progresses through a grid of processing elements and partial sums can flow along one axis without leaving the chip). Sự
đánh đổi là rằng cả các trọng số và các sự kích hoạt phải bây giờ được truyền phát một cách động, vì vậy hệ thống
phải duy trì cao đọc băng thông cho hai dữ liệu các luồng một cách đồng thời (The trade-off is that both weights and activations must now be streamed dynamically, so the system must sustain high read bandwidth for two data streams simultaneously). Song song các sự triển khai
cũng yêu cầu cẩn thận sự đồng bộ hóa khi nhiều các PE đóng góp tới cùng đầu ra phần tử (Parallel implementations also require careful synchronization when multiple PEs contribute to the same output element).
Đầu ra tính cố định là do đó hiệu quả nhất cho các khối lượng công việc nơi sự tích lũy thống trị, chẳng hạn như
hoàn toàn được kết nối các lớp và sự chú ý các cơ chế, nhưng kém phù hợp hơn khi đầu vào sự tái sử dụng là tới hạn
nút thắt cổ chai (Output stationary is therefore most effective for workloads where accumulation dominates, such as fully connected layers and attention mechanisms, but less suitable when input reuse is the critical bottleneck).
Đầu vào tính cố định (Input stationary) Hai các chiến lược được kiểm tra cho đến nay mỗi cái cố định một khác nhau toán hạng trong cục bộ bộ nhớ:
trọng số tính cố định cố định các trọng số để làm giảm đọc băng thông cho các tham số, và đầu ra tính cố định
cố định một phần các tổng để làm giảm ghi băng thông cho các sự tích lũy (The two strategies examined so far each fix a different operand in local memory: weight stationary fixes weights to reduce read bandwidth for parameters, and output stationary fixes partial sums to reduce write bandwidth for accumulations). Thứ ba chiến lược hoàn thành
bức tranh bằng cách việc cố định còn lại toán hạng: đầu vào các sự kích hoạt (The third strategy completes the picture by fixing the remaining operand: input activations). Trong transformer các mô hình, một đơn đầu vào
token tham gia trong các sự tính toán qua nhiều sự chú ý các đầu và các lớp; trong lô quá trình,
cùng sự kích hoạt lô nạp vào nhiều khác nhau trọng số các ma trận (In transformer models, a single input token participates in computations across multiple attention heads and layers; in batch processing, the same activation batch feeds into many different weight matrices). Khi sự kích hoạt sự tái sử dụng là
thống trị bộ nhớ chi phí, việc giữ các đầu vào tĩnh và việc truyền phát các trọng số thông qua hệ thống mang lại
tốt nhất năng lượng và băng thông sự đánh đổi (When activation reuse is the dominant memory cost, keeping inputs stationary and streaming weights through the system yields the best energy and bandwidth trade-off). Danh sách 11.18 minh họa này cách tiếp cận, việc tối đa hóa sự tái sử dụng
bằng cách việc giữ đầu vào các sự kích hoạt tĩnh trong cục bộ bộ nhớ trong khi một cách động việc truyền phát các trọng số (Listing 11.18 illustrates this approach, maximizing reuse by keeping input activations stationary in local memory while dynamically streaming weights).
Danh sách 11.18: Đầu vào Tính cố định Dữ liệu luồng: Đầu vào các sự kích hoạt ở lại thường trú trong cục bộ bộ nhớ trong khi các trọng số truyền phát thông qua,
việc tối thiểu hóa sự kích hoạt đọc lưu lượng; tốt nhất cho các transformer và lớn-lô suy luận nơi mỗi sự kích hoạt là được tái sử dụng (Listing 11.18: Input Stationary Dataflow: Input activations stay resident in local memory while weights stream through, minimizing activation read traffic; best for transformers and large-batch inference where each activation is reused).
## - Đầu vào các sự kích hoạt duy trì trong cục bộ bộ nhớ (Input activations remain in local memory)
## - Các trọng số truyền phát thông qua một cách động (Weights stream through dynamically)
## - Một phần các tổng tích lũy và là được ghi ra (Partial sums accumulate and are written out)
cho (for) input_block trong (in) inputs:
# Giữ đầu vào các sự kích hoạt tĩnh (Keep input activations stationary)
load_to_local(input_block)
# Cố định trong cục bộ lưu trữ (Fixed in local storage)
cho (for) weight_block trong (in) weights:
# Truyền phát các trọng số một cách động (Stream weights dynamically)
cho (for) output_block trong (in) outputs:
# Tính toán các kết quả (Compute results)
output_block += compute(weight_block, input_block)
# Tái sử dụng các đầu vào qua các trọng số (Reuse inputs across weights)
Ở đây, đầu vào các sự kích hoạt là được tải một lần và được giữ cố định trong khi các trọng số truyền phát thông qua (Here, input activations are loaded once and held fixed while weights stream through). Một phần
các tổng tích lũy và là cuối cùng được ghi ra, nhưng không giống đầu ra tính cố định, sự tích lũy
bộ đệm là không chính người thụ hưởng của tính cục bộ; thay vào đó, đầu vào dữ liệu là (Partial sums accumulate and are eventually written out, but unlike output stationary, the accumulation buffer is not the primary beneficiary of locality; instead, the input data is).
Sự đánh đổi phản chiếu những hai các chiến lược khác: các trọng số phải bây giờ được truyền phát một cách động,
vì vậy hệ thống cần được duy trì đọc băng thông cho trọng số luồng, và một phần các tổng yêu cầu

610
11.8 Dữ liệu luồng Sự tối ưu hóa (Dataflow Optimization)
việc tạo bộ đệm trước khi ghi-trở lại (buffering before write-back). Đầu vào tính cố định là hiệu quả nhất trong các transformer (nơi mỗi token là
được tái sử dụng qua sự chú ý các đầu), hồi quy các mạng (nơi ẩn trạng thái tham gia trong lặp lại
các sự tính toán), và lớn-lô suy luận (nơi cùng sự kích hoạt lô nạp nhiều trọng số
các ma trận) (Input stationary is most effective in transformers (where each token is reused across attention heads), recurrent networks (where the hidden state participates in repeated computations), and large-batch inference (where the same activation batch feeds many weight matrices)).
Được lấy cùng nhau, ba dữ liệu luồng các chiến lược minh họa một trung tâm thiết kế sự lựa chọn thay vì một
hệ thống phân cấp của chất lượng (Taken together, the three dataflow strategies illustrate a central design choice rather than a hierarchy of quality). Trọng số tính cố định tối thiểu hóa đọc lưu lượng cho các tham số và phù hợp các CNN với
nhỏ, nặng nề được tái sử dụng các bộ lọc (Weight stationary minimizes read traffic for parameters and suits CNNs with small, heavily reused filters). Đầu ra tính cố định tối thiểu hóa ghi lưu lượng cho các sự tích lũy và phù hợp
hoàn toàn được kết nối các lớp với cao quạt-vào (Output stationary minimizes write traffic for accumulations and suits fully connected layers with high fan-in). Đầu vào tính cố định tối thiểu hóa đọc lưu lượng cho các sự kích hoạt và
phù hợp các transformer và lô quá trình với cao sự kích hoạt sự tái sử dụng (Input stationary minimizes read traffic for activations and suits transformers and batch processing with high activation reuse). Không đơn chiến lược thống trị;
tối ưu sự lựa chọn phụ thuộc trên cái nào dữ liệu phần tử có cao nhất sự tái sử dụng tỷ lệ tương đối tới của nó kích thước, một
sự xác định thứ mà trình biên dịch và phần cứng nhà thiết kế phải làm dựa trên cụ thể khối lượng công việc
và bộ nhớ hệ thống phân cấp (No single strategy dominates; the optimal choice depends on which data element has the highest reuse ratio relative to its size, a determination that the compiler and hardware designer must make based on the specific workload and memory hierarchy). Tích chập-cụ thể các thiết kế cộng một thứ tư nhãn, hàng-tính cố định (như trong
Eyeriss), nhưng nó là không một tách biệt nguyên thủy: nó là một lai tạp thứ mà giữ các hàng của các đầu vào và một phần các tổng
cục bộ khi đó sự ánh xạ mang lại cao hơn sự tái sử dụng so với việc cố định bất kỳ đơn toán hạng (phần 11.5.6.2) (Convolution-specific designs add a fourth label, row-stationary (as in Eyeriss), but it is not a separate primitive: it is a hybrid that keeps rows of inputs and partial sums local when that mapping yields higher reuse than fixing any single operand (section 11.5.6.2)).
11.8.1.2 Hiệu quả-bộ nhớ tensor các bố cục (Memory-efficient tensor layouts)
Đứng trước dữ liệu luồng các chiến lược xác định cái nào dữ liệu ở lại gần tới tính toán; tensor các bố cục
xác định liệu đó dữ liệu có thể được truy cập một cách hiệu quả một khi nó đến (The preceding dataflow strategies determine which data stays close to compute; tensor layouts determine whether that data can be accessed efficiently once it arrives). Một một cách hoàn hảo được chọn trọng số-
tính cố định dữ liệu luồng vẫn chịu đựng nếu các trọng số là được lưu trữ trong một định dạng thứ mà gây ra bị phân tán bộ nhớ
các truy cập (A perfectly chosen weight-stationary dataflow still suffers if weights are stored in a format that causes scattered memory accesses). Tensor bố cục là do đó một hạt nhân hợp đồng: vật lý sự sắp xếp của đa chiều
dữ liệu phải khớp truy cập mẫu được mong đợi bởi được chọn phần cứng đường dẫn, hoặc máy gia tốc trả
trong bộ nhớ các sự đình trệ, không hiệu quả bộ nhớ cache sự sử dụng, và được làm tăng dữ liệu sự di chuyển (Tensor layout is therefore a kernel contract: the physical arrangement of multidimensional data must match the access pattern expected by the selected hardware path, or the accelerator pays in memory stalls, inefficient cache usage, and increased data movement).
Trong AI các máy gia tốc, tensor bố cục sự tối ưu hóa là đặc biệt quan trọng bởi vì dữ liệu là thường xuyên
được truy cập trong các mẫu được ra lệnh bởi cơ sở phần cứng kiến trúc (In AI accelerators, tensor layout optimization is particularly important because data is frequently accessed in patterns dictated by the underlying hardware architecture). Việc chọn đúng bố cục
đảm bảo rằng bộ nhớ các truy cập căn chỉnh với thân thiện-phần cứng truy cập các mẫu, việc tối thiểu hóa chi phí chung
từ tốn kém bộ nhớ các giao dịch (NVIDIA Corporation 2021) (Choosing the right layout ensures that memory accesses align with hardware-friendly access patterns, minimizing overhead from costly memory transactions (NVIDIA Corporation 2021)).
Trong khi các nhà phát triển có thể đôi khi một cách thủ công chỉ định tensor các bố cục, sự lựa chọn là thường được xác định
một cách tự động bởi máy học các bộ khung chẳng hạn như TensorFlow, PyTorch, và JAX, bởi các trình biên dịch,
hoặc bởi AI máy gia tốc các thời gian chạy (While developers can sometimes manually specify tensor layouts, the choice is often determined automatically by machine learning frameworks such as TensorFlow, PyTorch, and JAX, by compilers, or by AI accelerator runtimes). Cấp độ-thấp sự tối ưu hóa các công cụ chẳng hạn như cuDNN (cho NVIDIA các GPU),
XLA (cho TensorFlow các đồ thị), và dựa trên-MLIR trình biên dịch các ngăn xếp có thể áp đặt hoặc biến đổi tensor
các bố cục khi chúng hạ thấp các hoạt động tới cụ thể-cho-phần phụ trợ các hạt nhân (NVIDIA Corporation 2021; Google
2025; Lattner et al. 2020) (Low-level optimization tools such as cuDNN (for NVIDIA GPUs), XLA (for TensorFlow graphs), and MLIR-based compiler stacks may impose or transform tensor layouts as they lower operations to backend-specific kernels (NVIDIA Corporation 2021; Google 2025; Lattner et al. 2020)). Trong cấp độ-cao các bộ khung, bố cục các sự biến đổi là một cách điển hình được áp dụng
một cách minh bạch, nhưng các nhà phát triển việc làm việc với tùy chỉnh các hạt nhân hoặc cấp độ-thấp các thư viện chẳng hạn như CUDA,
Metal, hoặc OpenCL có thể có trực tiếp quyền kiểm soát qua tensor định dạng sự lựa chọn (In high-level frameworks, layout transformations are typically applied transparently, but developers working with custom kernels or low-level libraries such as CUDA, Metal, or OpenCL may have direct control over tensor format selection).
Cho ví dụ, PyTorch phơi bày tensor bố cục các hoạt động chẳng hạn như tensor.permute() và tensor.con-
tiguous() cho tường minh bộ nhớ-định dạng quyền kiểm soát (Paszke et al. 2019) (For example, PyTorch exposes tensor layout operations such as tensor.permute() and tensor.contiguous() for explicit memory-format control (Paszke et al. 2019)). TensorFlow thường áp dụng bố cục
các sự tối ưu hóa một cách nội bộ thông qua XLA trình biên dịch, việc chọn giữa NHWC (hàng-chính) và
NCHW (kênh-chính) dựa trên mục tiêu phần cứng (Brain 2022) (TensorFlow often applies layout optimizations internally through the XLA compiler, choosing between NHWC (row-major) and NCHW (channel-major) based on the target hardware (Brain 2022)). Nhận thức-phần cứng các thư viện chẳng hạn
như cuDNN cho các GPU và oneDNN cho các CPU thực thi cụ thể bộ nhớ các bố cục để tối đa hóa bộ nhớ cache
tính cục bộ và SIMD tính hiệu quả (Hardware-aware libraries such as cuDNN for GPUs and oneDNN for CPUs enforce specific memory layouts to maximize cache locality and SIMD efficiency). Thực tế quy tắc là để đối xử bố cục như phần của được chọn phần phụ trợ đường dẫn:
nhanh nhất tensor định dạng là cái thứ mà tránh sự chuyển đổi chi phí chung và làm hạt nhân của bộ nhớ
các truy cập liên tiếp (The practical rule is to treat layout as part of the selected backend path: the fastest tensor format is the one that avoids conversion overhead and makes the kernel’s memory accesses contiguous).
Hàng-chính bố cục (Row-major layout) Hàng-chính bố cục là bộ nhớ lưu trữ quy ước nơi đa-chiều
tensor các phần tử là được sắp xếp hàng bởi hàng, việc đảm bảo rằng tất cả các giá trị trong một cho trước hàng là được đặt một cách liên
tiếp trước khi việc di chuyển tới tiếp theo hàng (Row-major layout is the memory storage convention where multi-dimensional tensor elements are arranged row by row, ensuring that all values in a given row are placed contiguously before moving to the next row). Này lưu trữ định dạng là một cách rộng rãi được sử dụng trong đa-mục đích các CPU
và một số máy học các bộ khung bởi vì nó căn chỉnh một cách tự nhiên với tuần tự bộ nhớ truy cập
các mẫu, việc làm nó hiệu quả-bộ nhớ cache hơn cho một số các loại của các hoạt động (Intel Corporation 2021b) (This storage format is widely used in general-purpose CPUs and some machine learning frameworks because it aligns naturally with sequential memory access patterns, making it more cache-efficient for certain types of operations (Intel Corporation 2021b)).
Để hiểu cách nào hàng-chính bố cục hoạt động, xem xét một đơn RGB hình ảnh được biểu diễn như một tensor
của hình dạng (Chiều cao, Chiều rộng, Các kênh) (To understand how row-major layout works, consider a single RGB image represented as a tensor of shape (Height, Width, Channels)). Nếu hình ảnh có một kích thước của 3×3 các pixel với 3 các kênh (RGB),
tương ứng tensor là được cấu trúc như (3, 3, 3) (If the image has a size of 3×3 pixels with 3 channels (RGB), the corresponding tensor is structured as (3, 3, 3)). Các giá trị là được lưu trữ trong bộ nhớ như sau:
𝐼(0,0,0),𝐼(0,0,1),𝐼(0,0,2),𝐼(0,1,0),𝐼(0,1,1),
𝐼(0,1,2),𝐼(0,2,0),𝐼(0,2,1),𝐼(0,2,2),…
Mỗi hàng là được lưu trữ một cách liên tiếp, việc có nghĩa tất cả pixel các giá trị trong đầu tiên hàng là được đặt một cách tuần tự
trong bộ nhớ trước khi việc di chuyển vào tới thứ hai hàng (Each row is stored contiguously, meaning all pixel values in the first row are placed sequentially in memory before moving on to the second row). Này sự sắp xếp thứ tự là có lợi thế bởi vì các CPU và

11. Phần cứng Sự gia tốc (Hardware Acceleration)
611
34
Bộ nhớ Sự kết hợp (Memory Coalescing):
GPU phần cứng cơ
chế thứ mà hợp nhất bộ nhớ các yêu
cầu từ các luồng trong một nhóm (warp)
thành một đơn giao dịch khi
những các luồng đó truy cập liên
tiếp bộ nhớ (The GPU hardware mechanism that fuses memory requests from threads in a warp into a single transaction when those threads access contiguous memory).
Tensor bố
cục ảnh hưởng sự kết hợp, nhưng
dấu hiệu của hiệu ứng phụ thuộc
trên hạt nhân (Tensor layout affects coalescing, but the sign of the effect depends on the kernel):
NCHW có thể
là hiệu quả cho một số tích
chập các sự triển khai, trong khi
NHWC/kênh-cuối là thường
được ưa thích cho hiện đại Tensor
Lõi tích chập và sự hợp nhất
các đường dẫn (NCHW can be efficient for some convolution implementations, while NHWC/channels-last is often preferred for modern Tensor Core convolution and fusion paths). Tồi bố cục các sự lựa chọn có thể
vẫn tạo ra nhiều-lần hiệu
suất các khoảng trống, nhưng đúng
sửa chữa là để khớp bố cục tới
phần phụ trợ thay vì việc ghi
nhớ một toàn cầu định dạng (Poor layout choices can still create multi-fold performance gaps, but the correct fix is to match the layout to the backend rather than memorize one universal format).
35
NHWC so với NCHW (NHWC vs. NCHW):
NHWC liệt kê các chiều hướng như
lô, chiều cao, chiều rộng, kênh
(batch, height, width, channel); NCHW liệt kê lô, kênh,
chiều cao, chiều rộng (batch, channel, height, width). Vật lý
bộ nhớ định dạng xác định
liệu liền kề các luồng đọc
liền kề các địa chỉ, vì vậy hiệu
suất hiệu ứng là cụ thể-cho-
phần phụ trợ (Physical memory format determines whether adjacent threads read adjacent addresses, so the performance effect is backend-specific). Bố cục-tới-phần cứng
sự không khớp là không một vi-
sự tối ưu hóa; nó có thể tạo ra
nhiều-lần hiệu suất các khoảng trống,
đặc biệt khi một sự chuyển đổi
ngăn chặn Tensor Lõi tích
chập hoặc sự hợp nhất các đường dẫn khỏi việc
được sử dụng (Layout-to-hardware mismatch is not a micro-optimization; it can create multi-fold performance gaps, especially when a conversion prevents Tensor Core convolution or fusion paths from being used).
bộ nhớ cache các hệ thống phân cấp là được tối ưu hóa cho tuần tự bộ nhớ truy cập (cache hierarchies are optimized for sequential memory access). Khi dữ liệu là được truy cập trong một theo-hàng
cách thức, chẳng hạn như khi việc áp dụng theo-phần tử các hoạt động giống như sự kích hoạt các hàm hoặc cơ bản số học
các sự biến đổi, bộ nhớ các lượt lấy là hiệu quả, và bộ nhớ cache sự sử dụng là được tối đa hóa (Sodani 2015) (When data is accessed in a row-wise fashion, such as when applying element-wise operations like activation functions or basic arithmetic transformations, memory fetches are efficient, and cache utilization is maximized (Sodani 2015)).
Tính hiệu quả của hàng-chính lưu trữ trở thành đặc biệt rõ ràng trong dựa trên-CPU máy học
các khối lượng công việc, nơi các hoạt động chẳng hạn như lô chuẩn hóa, ma trận các phép nhân, và theo-phần
tử số học thường xuyên xử lý các hàng của dữ liệu một cách tuần tự (The efficiency of row-major storage becomes particularly evident in CPU-based machine learning workloads, where operations such as batch normalization, matrix multiplications, and element-wise arithmetic frequently process rows of data sequentially). Vì hiện đại các CPU tuyển dụng bộ nhớ cache
việc lấy trước các cơ chế, một hàng-chính bố cục cho phép tiếp theo yêu cầu dữ liệu các giá trị để được tải trước
vào bộ nhớ cache trước của sự thực thi, việc làm giảm bộ nhớ độ trễ và việc cải thiện tổng thể tính toán
thông lượng (Since modern CPUs employ cache prefetching mechanisms, a row-major layout allows the next required data values to be preloaded into cache ahead of execution, reducing memory latency and improving overall computational throughput).
Tuy nhiên, bố cục sự lựa chọn trở thành tinh tế cho các tích chập bởi vì logic chiều hướng thứ tự và
vật lý bộ nhớ định dạng là không cùng thứ (However, layout choice becomes subtle for convolutions because logical dimension order and physical memory format are not the same thing). Một tensor có thể được mô tả như NHWC hoặc NCHW, nhưng
phần phụ trợ cuối cùng quan tâm liệu bộ nhớ các địa chỉ được tiêu thụ bởi một hạt nhân là liên tiếp,
được căn chỉnh, và được kết hợp cho cụ thể toán tử và độ chính xác chế độ (a tensor may be described as NHWC or NCHW, but the backend ultimately cares whether the memory addresses consumed by a kernel are contiguous, aligned, and coalesced for the specific operator and precision mode).
Mặc dù những các sự giới hạn này, hàng-chính bố cục duy trì quan trọng trong dựa trên-CPU máy học
các bộ khung (Despite these limitations, row-major layout remains important in CPU-based machine learning frameworks). TensorFlow, cho ví dụ, một cách phổ biến sử dụng NHWC các quy ước, trong khi PyTorch một cách phổ
biến phơi bày NCHW các tensor với một tách biệt các kênh-cuối bộ nhớ định dạng tùy chọn (TensorFlow, for instance, commonly uses NHWC conventions, while PyTorch commonly exposes NCHW tensors with a separate channels-last memory format option). Khi việc nhắm mục tiêu
các GPU, các bộ khung và các thư viện có thể chèn, lan truyền, hoặc một cách nội bộ thực hiện bố cục các sự biến đổi
để khớp nhanh nhất hạt nhân đường dẫn (When targeting GPUs, frameworks and libraries may insert, propagate, or internally perform layout transformations to match the fastest kernel path).
Kênh-chính bố cục (Channel-major layout) Trái ngược tới hàng-chính bố cục, kênh-chính bố cục sắp xếp dữ liệu trong
bộ nhớ sao cho tất cả các giá trị cho một cho trước kênh là được lưu trữ cùng nhau trước khi việc di chuyển tới tiếp theo
kênh (In contrast to row-major layout, channel-major layout arranges data in memory such that all values for a given channel are stored together before moving to the next channel). Chính sự thấu hiểu là rằng các GPU xử lý dữ liệu trong song song qua các luồng, và khi các luồng
truy cập liên tiếp bộ nhớ các địa chỉ, phần cứng có thể kết hợp những các yêu cầu này thành một đơn hiệu quả
giao dịch (bộ nhớ sự kết hợp) (The key insight is that GPUs process data in parallel across threads, and when threads access consecutive memory addresses, the hardware can combine these requests into a single efficient transaction (memory coalescing)). Về mặt lịch sử, nhiều GPU tích chập các đường dẫn sử dụng NCHW một cách hiệu quả,
trong khi hiện đại Tensor Lõi tích chập và sự hợp nhất các đường dẫn thường ưa thích NHWC hoặc các kênh-cuối
vật lý các bố cục bởi vì những các bố cục đó căn chỉnh tốt hơn với được vector hóa lõi-tensor các hạt nhân (Historically, many GPU convolution paths used NCHW effectively, while modern Tensor Core convolution and fusion paths often prefer NHWC or channels-last physical layouts because those layouts align better with vectorized tensor-core kernels).
Để hiểu cách nào kênh-chính bố cục hoạt động, xem xét cùng RGB hình ảnh tensor của kích thước
(Chiều cao, Chiều rộng, Các kênh) = (3, 3, 3) (To understand how channel-major layout works, consider the same RGB image tensor of size (Height, Width, Channels) = (3, 3, 3)). Thay vì việc lưu trữ pixel các giá trị hàng bởi hàng, dữ liệu là được cấu trúc
kênh-đầu tiên trong bộ nhớ như sau (Instead of storing pixel values row by row, the data is structured channel-first in memory as follows):
𝐼(0,0,0),𝐼(0,1,0),𝐼(0,2,0),𝐼(1,0,0),𝐼(1,1,0),𝐼(1,2,0),…,
𝐼(0,0,1),𝐼(0,1,1),𝐼(0,2,1),…,𝐼(0,0,2),𝐼(0,1,2),𝐼(0,2,2),…
Trong này định dạng, tất cả đỏ kênh các giá trị cho toàn bộ hình ảnh là được lưu trữ đầu tiên, được theo sau bởi tất cả xanh lá
các giá trị, và sau đó tất cả xanh lam các giá trị (In this format, all red channel values for the entire image are stored first, followed by all green values, and then all blue values). Này sự sắp xếp thứ tự có thể cho phép một số phần cứng các máy gia tốc để một cách hiệu quả
tải và xử lý dữ liệu qua các kênh trong song song, thứ mà là quan trọng cho tích chập các hoạt động
và SIMD (Đơn Lệnh, Nhiều Dữ liệu) sự thực thi các mô hình (Chetlur et al. 2014) (This ordering can allow some hardware accelerators to efficiently load and process data across channels in parallel, which is important for convolution operations and SIMD (Single Instruction, Multiple Data) execution models (Chetlur et al. 2014)).
Lợi thế của một cho trước bố cục trở thành rõ ràng chỉ tương đối tới một cụ thể phần phụ trợ (The advantage of a given layout becomes clear only relative to a specific backend). Tích chập
các lớp xử lý các hình ảnh bằng cách việc áp dụng một được chia sẻ tập hợp của các bộ lọc qua tất cả các kênh (Convolutional layers process images by applying a shared set of filters across all channels). Phụ thuộc trên hạt nhân
sự triển khai, NCHW, NHWC, hoặc một được đóng khối nội bộ bố cục có thể tối thiểu hóa bị phân tán bộ nhớ
các lượt lấy, làm giảm bộ nhớ độ trễ, và cải thiện dữ liệu tính cục bộ cho được hạ thấp ma trận các phép nhân
thứ mà thực thi tích chập (Depending on the kernel implementation, NCHW, NHWC, or a blocked internal layout may minimize scattered memory fetches, reduce memory latency, and improve data locality for the lowered matrix multiplications that implement convolution).
Bởi vì các GPU và các TPU dựa trên bộ nhớ sự kết hợp34, một kỹ thuật trong đó liên tiếp các luồng
lấy liên tiếp bộ nhớ các địa chỉ, tốt nhất bố cục là cái thứ mà làm hạt nhân của thực tế luồng-
truy cập mẫu liên tiếp (Because GPUs and TPUs rely on memory coalescing34, a technique in which consecutive threads fetch contiguous memory addresses, the best layout is the one that makes the kernel’s actual thread-access pattern contiguous). Cho ví dụ, trong NVIDIA GPU tích chập các đường dẫn, cuDNN có thể sử dụng hoặc
một cách nội bộ chuyển đổi tới NHWC/các kênh-cuối cho Tensor Lõi các hạt nhân, trong khi khác các hạt nhân có thể vẫn
thực hiện tốt với NCHW (For example, in NVIDIA GPU convolution paths, cuDNN may use or internally convert to NHWC/channels-last for Tensor Core kernels, while other kernels may still perform well with NCHW). Quy tắc là phụ thuộc-phần phụ trợ và phụ thuộc-toán tử thay vì một phổ quát
CPU=NHWC, GPU=NCHW sự chia tách (The rule is backend- and operator-dependent rather than a universal CPU=NHWC, GPU=NCHW split).
Mặc dù của nó các lợi thế cho một số máy gia tốc các hạt nhân, kênh-chính bố cục có thể giới thiệu các sự không hiệu
quả khi việc chạy trên đa-mục đích các CPU hoặc các hạt nhân được tối ưu hóa cho các kênh-cuối truy cập (Despite its advantages for some accelerator kernels, channel-major layout can introduce inefficiencies when running on general-purpose CPUs or kernels optimized for channels-last access). Vì
các CPU tối ưu hóa cho tuần tự bộ nhớ truy cập và được vector hóa các vòng lặp, hiệu quả nhất bố cục phụ thuộc
trên hoạt động, bộ khung quy ước, và thư viện sự triển khai (Since CPUs optimize for sequential memory access and vectorized loops, the most efficient layout depends on the operation, framework convention, and library implementation).
Hiện đại AI các bộ khung và các trình biên dịch thường biến đổi tensor các bố cục một cách động phụ thuộc trên
sự thực thi môi trường, nhưng điều này là không được đảm bảo cho mọi mô hình hoặc hoạt động35 (Modern AI frameworks and compilers often transform tensor layouts dynamically depending on the execution environment, but this is not guaranteed for every model or operation35). TensorFlow,
XLA, cuDNN, và TensorRT có thể chèn hoặc chọn bố cục các sự chuyển đổi một cách nội bộ; PyTorch phơi bày
tường minh các kênh-cuối sự chuyển đổi và sự lan truyền các đường dẫn (TensorFlow, XLA, cuDNN, and TensorRT may insert or choose layout conversions internally; PyTorch exposes explicit channels-last conversion and propagation paths). Các nhà phát triển vẫn cần để lập hồ sơ bố cục
các sự lựa chọn khi tích chập hiệu suất là đáng kể (Developers still need to profile layout choices when convolution performance is material).

612
11.8 Dữ liệu luồng Sự tối ưu hóa (Dataflow Optimization)
36
Hạt nhân Sự hợp nhất (Kernel Fusion): "trung
gian dữ liệu sự di chuyển"
được tham chiếu xảy
ra bởi
vì mỗi tách biệt GPU hàm,
hoặc hạt nhân, phải ghi của nó kết quả
trở lại tới cao-băng thông
bộ nhớ (HBM) trước khi
tiếp theo cái bắt đầu (The “intermediate data movement” referenced occurs because each separate GPU function, or kernel, must write its result back to high-bandwidth memory (HBM) before the next one begins).
Bằng cách việc biên
dịch nhiều
các hoạt động
thành một đơn hạt nhân, sự hợp nhất
cho phép trung gian các giá trị để
sống trong nhanh trên-chip bộ nhớ,
hoàn toàn việc tránh
HBM ghi/đọc chu kỳ (By compiling multiple operations into a single kernel, fusion allows intermediate values to live in fast on-chip memory, completely avoiding the HBM write/read cycle). Cho
bị ràng buộc-bởi-bộ nhớ các hoạt động
phổ biến trong
các transformer,
này sự làm giảm trong bộ nhớ
lưu lượng (thường 2–3×) dịch
một cách trực tiếp tới một tỷ lệ
phần tăng trong hiệu suất (For memory-bound operations common in transformers, this reduction in memory traffic (often 2–3×) translates directly to a proportional increase in performance).
Việc so sánh hàng-chính và kênh-chính các bố cục (Comparing row-major and channel-major layouts) Cả hàng-chính (NHWC) và kênh-chính
(NCHW) các bố cục phục vụ khác biệt các mục đích trong máy học các khối lượng công việc, với của chúng tính hiệu quả phần lớn
được xác định bởi phần cứng kiến trúc, bộ nhớ truy cập các mẫu, và tính toán các yêu cầu (Both row-major (NHWC) and channel-major (NCHW) layouts serve distinct purposes in machine learning workloads, with their efficiency largely determined by the hardware architecture, memory access patterns, and computational requirements).
Sự lựa chọn của bố cục một cách trực tiếp ảnh hưởng bộ nhớ cache sự sử dụng, bộ nhớ băng thông tính hiệu quả, và xử lý
thông lượng (The choice of layout directly influences cache utilization, memory bandwidth efficiency, and processing throughput). Bảng 11.18 đối chiếu hiệu suất các sự đánh đổi và phần cứng khả năng tương thích
giữa những hai các cách tiếp cận này (Table 11.18 contrasts the performance trade-offs and hardware compatibility between these two approaches).
Bảng 11.18: Dữ liệu Bố cục Các chiến lược: Hàng-chính (NHWC) và kênh-chính (NCHW) các bố cục tối ưu hóa bộ nhớ truy cập
các mẫu cho khác nhau phần phụ trợ các hạt nhân (Table 11.18: Data Layout Strategies: Row-major (NHWC) and channel-major (NCHW) layouts optimize memory access patterns for different backend kernels). NHWC/các kênh-cuối thường phù hợp CPU sự vector hóa và hiện đại Tensor Lõi
tích chập/sự hợp nhất các đường dẫn, trong khi NCHW duy trì phổ biến trong PyTorch mô hình mã và nhiều GPU các hạt nhân (NHWC/channels-last often suits CPU vectorization and modern Tensor Core convolution/fusion paths, while NCHW remains common in PyTorch model code and many GPU kernels). Việc chọn
thích hợp bố cục một cách trực tiếp tác động hiệu suất bằng cách việc tối đa hóa bộ nhớ cache sự sử dụng và bộ nhớ băng thông tính hiệu quả (Choosing the appropriate layout directly impacts performance by maximizing cache utilization and memory bandwidth efficiency).
Đặc trưng (Feature)
Hàng-Chính (NHWC) (Row-Major (NHWC))
Kênh-Chính (NCHW) (Channel-Major (NCHW))
Bộ nhớ Lưu trữ
Thứ tự (Memory Storage Order)
Các pixel là được lưu trữ hàng-bởi-hàng, kênh được xen kẽ
(Pixels are stored row-by-row, channel interleaved)
Tất cả các giá trị cho một cho trước kênh là được lưu trữ cùng nhau
đầu tiên (All values for a given channel are stored together first)
Tốt nhất cho (Best for)
CPU các vòng lặp, theo-phần tử các hoạt động, nhiều
các kênh-cuối các hạt nhân (CPU loops, element-wise operations, many channels-last kernels)
Nhiều di sản GPU tích chập các đường dẫn và
kênh-đầu tiên mô hình mã (Many legacy GPU convolution paths and channel-first model code)
Bộ nhớ cache Tính hiệu quả (Cache Efficiency)
Cao bộ nhớ cache tính cục bộ cho tuần tự
hàng/kênh-cuối truy cập (High cache locality for sequential row/channel-last access)
Có thể cải thiện sự kết hợp cho kênh-đầu tiên các hạt nhân (Can improve coalescing for channel-first kernels)
Tích chập
Hiệu suất (Convolution Performance)
Thường được ưa thích bởi hiện đại Tensor Lõi
tích chập/sự hợp nhất các đường dẫn (Often preferred by modern Tensor Core convolution/fusion paths)
Hiệu quả cho nhiều cuDNN và bộ khung
các hạt nhân (Efficient for many cuDNN and framework kernels)
Bộ nhớ Lấy (Memory Fetching)
Tốt khi các hạt nhân vector hóa qua liền kề
kênh dữ liệu (Good when kernels vectorize over adjacent channel data)
Tốt khi các hạt nhân xử lý kênh-chính các ô gạch (Good when kernels process channel-major tiles)
Mặc định trong
Các bộ khung (Default in Frameworks)
Phổ biến TensorFlow quy ước; PyTorch
các kênh-cuối tùy chọn (Common TensorFlow convention; PyTorch channels-last option)
Phổ biến PyTorch tensor hình dạng quy ước (Common PyTorch tensor shape convention)
Quyết định để sử dụng hàng-chính (NHWC) hoặc kênh-chính (NCHW) các bố cục là không luôn luôn được thực hiện
một cách thủ công bởi các nhà phát triển (The decision to use row-major (NHWC) or channel-major (NCHW) layouts is not always made manually by developers). Thay vào đó, máy học các bộ khung và AI các trình biên dịch thường xác định
tối ưu bố cục một cách động dựa trên mục tiêu phần cứng và hoạt động loại (Instead, machine learning frameworks and AI compilers often determine the optimal layout dynamically based on the target hardware and operation type).
Trong thực tế, hiện đại AI các trình biên dịch chẳng hạn như TensorFlow của XLA, cuDNN, TensorRT, và PyTorch
sự biên dịch các đường dẫn có thể thực hiện bố cục các sự biến đổi hoặc lan truyền bố cục siêu dữ liệu (In practice, modern AI compilers such as TensorFlow’s XLA, cuDNN, TensorRT, and PyTorch compilation paths may perform layout transformations or propagate layout metadata). Kết quả
có thể là cao thông lượng mà không có thủ công tensor các lượt viết lại, nhưng nhạy cảm-hiệu suất các sự triển khai
nên vẫn lập hồ sơ cả bố cục và sự chuyển đổi chi phí chung trên mục tiêu phần cứng (The result can be high throughput without manual tensor rewrites, but performance-sensitive deployments should still profile both layout and conversion overhead on the target hardware).
11.8.1.3 Hạt nhân sự hợp nhất (Kernel fusion)
Một trong những tác động nhất sự tối ưu hóa các kỹ thuật trong AI sự gia tốc liên quan tới việc làm giảm chi phí chung
của trung gian dữ liệu sự di chuyển giữa các hoạt động (One of the most impactful optimization techniques in AI acceleration involves reducing the overhead of intermediate data movement between operations). Hạt nhân sự hợp nhất36 biến đổi nhiều tách biệt
các sự tính toán thành được thống nhất các hoạt động, một cách đáng kể việc cải thiện bộ nhớ tính hiệu quả và sự thực thi
hiệu suất (Kernel fusion36 transforms multiple separate computations into unified operations, dramatically improving memory efficiency and execution performance). Bộ nhớ các nút thắt cổ chai được tạo ra bởi trung gian các lượt ghi thúc đẩy hạt nhân sự hợp nhất, thứ mà
loại bỏ những các sự không hiệu quả này (The memory bottlenecks created by intermediate writes motivate kernel fusion, which eliminates these inefficiencies).
Trung gian bộ nhớ ghi (Intermediate memory write) AI mô hình hiệu suất là thường bị ràng buộc bởi bộ nhớ băng thông
và trung gian bộ nhớ các lượt ghi thay vì thuần túy số học các hoạt động (AI model performance is often constrained by memory bandwidth and intermediate memory writes rather than pure arithmetic operations). Mọi thời gian một hoạt động
sản xuất một trung gian kết quả thứ mà phải được ghi tới bộ nhớ và sau đó được đọc trở lại, sự thực thi
đình trệ từ dữ liệu sự di chuyển chi phí chung (Every time an operation produces an intermediate result that must be written to memory and later read back, execution stalls from the data movement overhead).
Hạt nhân sự hợp nhất đại diện tới hạn cây cầu giữa phần mềm sự tối ưu hóa các kỹ thuật được giới
thiệu trong phần 10.5.1.5 và bộ nhớ băng thông các sự ràng buộc được phân tích trong phần 11.5.1 (Kernel fusion represents the critical bridge between the software optimization techniques introduced in section 10.5.1.5 and the memory bandwidth constraints analyzed in section 11.5.1). Nhiều
AI các khối lượng công việc giới thiệu không cần thiết trung gian bộ nhớ các lượt ghi, việc làm tăng bộ nhớ băng thông
sự tiêu thụ và việc làm giảm sự thực thi tính hiệu quả (NVIDIA Corporation 2017) (Many AI workloads introduce unnecessary intermediate memory writes, increasing memory bandwidth consumption and reducing execution efficiency (NVIDIA Corporation 2017)).
Danh sách 11.19 tiết lộ cách nào mỗi hoạt động trở thành một tách biệt hạt nhân trong một ngây thơ sự thực thi mô hình,
việc ép buộc trung gian các kết quả để được ghi tới bộ nhớ và sau đó được đọc trở lại cho tiếp theo hoạt động (Listing 11.19 reveals how each operation becomes a separate kernel in a naïve execution model, forcing intermediate results to be written to memory and then read back for the next operation).
Mỗi hoạt động sản xuất một trung gian tensor thứ mà phải được ghi tới bộ nhớ và được lấy lại cho
tiếp theo hoạt động (Each operation produces an intermediate tensor that must be written to memory and retrieved for the next operation). Trên lớn các tensor, này chi phí chung của việc di chuyển dữ liệu có thể lớn hơn tính toán
chi phí của các hoạt động (Shazeer et al. 2018) (On large tensors, this overhead of moving data can outweigh the computational cost of the operations (Shazeer et al. 2018)). Bảng 11.19 minh họa bộ nhớ chi phí chung trong một ngây thơ
sự thực thi mô hình (Table 11.19 illustrates the memory overhead in a naïve execution model). Trong khi chỉ cuối cùng kết quả 𝑌 là được cần, việc lưu trữ nhiều trung gian các tensor
tạo ra không cần thiết bộ nhớ lưu lượng và không hiệu quả bộ nhớ sự sử dụng (While only the final result 𝑌 is needed, storing multiple intermediate tensors creates unnecessary memory traffic and inefficient memory usage).

11. Phần cứng Sự gia tốc (Hardware Acceleration)
613
Danh sách 11.19: Ngây thơ Sự thực thi: Mỗi bước ghi trung gian các kết quả tới bộ nhớ trước khi việc xử lý tiếp theo cái, việc dẫn tới được làm tăng
băng thông sự sử dụng và được làm giảm tính hiệu quả (Listing 11.19: Naïve Execution: Each step writes intermediate results to memory before processing the next, leading to increased bandwidth usage and reduced efficiency).
import torch
## Đầu vào tensor (Input tensor)
X = torch.randn(1024, 1024).cuda()
## Bước-bởi-bước sự thực thi (ngây thơ cách tiếp cận) (Step-by-step execution (naïve approach))
X1 = torch.relu(X)
# Trung gian tensor được lưu trữ (Intermediate tensor stored)
# trong bộ nhớ (in memory)
X2 = torch.batch_norm(X1)
# Một cái khác trung gian tensor được lưu trữ (Another intermediate tensor stored)
Y = 2.0 * X2 + 1.0
# Cuối cùng kết quả (Final result)
Bảng 11.19: Trung gian Tensor Lưu trữ: Ngây thơ sự thực thi các mô hình yêu cầu đáng kể bộ nhớ để lưu trữ trung gian các tensor
được tạo ra bởi mỗi hoạt động (Table 11.19: Intermediate Tensor Storage: Naive execution models require substantial memory to store intermediate tensors generated by each operation). Cho một 1024×1024 tensor, việc lưu trữ trung gian các kết quả (thậm chí khi chỉ cuối cùng đầu ra là được cần)
tăng gấp bốn tổng bộ nhớ dấu chân từ 4.2 MB tới 16.8 MB (For a 1024×1024 tensor, storing intermediate results (even when only the final output is needed) quadruples the total memory footprint from 4.2 MB to 16.8 MB). Việc tối thiểu hóa trung gian dữ liệu lưu trữ là cần thiết cho việc cải thiện
bộ nhớ tính hiệu quả (Minimizing intermediate data storage is essential for improving memory efficiency).
Tensor
Kích thước (Size) (MB) cho 1024×1024 Tensor
X
4.2 MB
X’
4.2 MB
X’ ’
4.2 MB
Y
4.2 MB
Tổng Bộ nhớ (Total Memory)
16.8 MB
Hạt nhân sự hợp nhất cho bộ nhớ tính hiệu quả (Kernel fusion for memory efficiency) Ba trung gian các tensor lãng phí cả bộ nhớ khả năng
và băng thông, việc giới hạn khả năng mở rộng trên AI các máy gia tốc nơi dữ liệu sự di chuyển thống trị sự thực thi
chi phí (The three intermediate tensors waste both memory capacity and bandwidth, limiting scalability on AI accelerators where data movement dominates execution cost). Hạt nhân sự hợp nhất tối thiểu hóa trung gian bộ nhớ các lượt ghi, việc làm giảm bộ nhớ dấu chân và
băng thông sự tiêu thụ của máy học các khối lượng công việc (Jia et al. 2018) (Kernel fusion minimizes intermediate memory writes, reducing the memory footprint and bandwidth consumption of machine learning workloads (Jia et al. 2018)). Hạt nhân sự hợp nhất hợp nhất
nhiều tính toán các bước thành một đơn, được tối ưu hóa hoạt động, việc loại bỏ nhu cầu cho việc lưu trữ và
việc tải lại trung gian các tensor (Kernel fusion merges multiple computation steps into a single, optimized operation, eliminating the need for storing and reloading intermediate tensors). Thay vì việc thực thi mỗi lớp hoặc theo-phần tử hoạt động một cách tách biệt,
trong đó mỗi bước ghi của nó đầu ra tới bộ nhớ trước khi tiếp theo bước bắt đầu, sự hợp nhất kích hoạt trực tiếp
dữ liệu sự lan truyền giữa các hoạt động, việc giữ các sự tính toán bên trong cao-tốc độ các thanh ghi hoặc cục bộ
bộ nhớ (Instead of executing each layer or element-wise operation separately, in which each step writes its output to memory before the next step begins, fusion enables direct data propagation between operations, keeping computations within high-speed registers or local memory).
Một phổ biến máy học chuỗi có thể liên quan tới việc áp dụng một phi tuyến sự kích hoạt hàm
(ví dụ, ReLU), được theo sau bởi lô chuẩn hóa, và sau đó việc thay đổi tỷ lệ các giá trị cho đầu vào tới tiếp theo lớp (A common machine learning sequence might involve applying a nonlinear activation function (e.g., ReLU), followed by batch normalization, and then scaling the values for input to the next layer).
Trong một ngây thơ sự triển khai, mỗi của những các bước này tạo ra một trung gian tensor, thứ mà là được ghi tới
bộ nhớ, được đọc trở lại, và sau đó được sửa đổi một lần nữa (In a naïve implementation, each of these steps generates an intermediate tensor, which is written to memory, read back, and then modified again):
𝑋′ = ReLU(𝑋)
𝑋″ = BatchNorm(𝑋′)
𝑌 = 𝛼⋅𝑋″ +𝛽
Với hạt nhân sự hợp nhất, những các hoạt động này là được kết hợp thành một đơn tính toán bước, việc cho phép
toàn bộ sự biến đổi để xảy ra mà không việc tạo ra không cần thiết trung gian các tensor (With kernel fusion, these operations are combined into a single computation step, allowing the entire transformation to occur without generating unnecessary intermediate tensors):
𝑌 = 𝛼⋅BatchNorm(ReLU(𝑋))+𝛽
Bảng 11.20 định lượng cục bộ-bộ nhớ lợi ích của sự hợp nhất trước khi phần tổng quát hóa quy tắc:
việc loại bỏ trung gian các tensor cắt giảm cả được lưu trữ trạng thái và bộ nhớ lưu lượng (Table 11.20 quantifies the local-memory benefit of fusion before the section generalizes the rule: eliminating intermediate tensors cuts both stored state and memory traffic).
Bảng 11.20 làm nổi bật tác động của hoạt động sự hợp nhất trên bộ nhớ tính hiệu quả (Table 11.20 highlights the impact of operation fusion on memory efficiency). Bằng cách việc giữ trung
gian các kết quả trong các thanh ghi hoặc cục bộ bộ nhớ thay vì việc ghi chúng tới chính bộ nhớ, sự hợp nhất
một cách đáng kể làm giảm bộ nhớ lưu lượng (By keeping intermediate results in registers or local memory rather than writing them to main memory, fusion significantly reduces memory traffic). Này sự tối ưu hóa là đặc biệt có lợi trên cao độ song song
các kiến trúc giống như các GPU và các TPU, nơi việc tối thiểu hóa bộ nhớ các truy cập dịch một cách trực tiếp thành được cải
thiện sự thực thi thông lượng (This optimization is especially beneficial on highly parallel architectures like GPUs and TPUs, where minimizing memory accesses translates directly into improved execution throughput). So với ngây thơ sự thực thi mô hình, được hợp nhất sự thực thi loại bỏ

614
11.8 Dữ liệu luồng Sự tối ưu hóa (Dataflow Optimization)
nhu cầu cho việc lưu trữ trung gian các tensor, một cách đáng kể việc hạ thấp tổng bộ nhớ dấu chân và
việc cải thiện tổng thể tính hiệu quả (the need for storing intermediate tensors, dramatically lowering the total memory footprint and improving overall efficiency).
Bảng 11.20: Hoạt động Sự hợp nhất Các lợi ích: Được hợp nhất sự thực thi làm giảm bộ nhớ sự sử dụng bằng cách việc loại bỏ nhu cầu để lưu trữ trung gian
các tensor, một cách trực tiếp việc cải thiện tính hiệu quả trên bị ràng buộc-bởi-bộ nhớ phần cứng giống như các GPU và các TPU (Table 11.20: Operation Fusion Benefits: Fused execution reduces memory usage by eliminating the need to store intermediate tensors, directly improving efficiency on memory-bound hardware like GPUs and TPUs). Bộ nhớ sự tiêu thụ giảm từ 16.8
MB trong ngây thơ sự thực thi tới 4.2 MB với được hợp nhất các hoạt động, một 4× sự làm giảm (Memory consumption drops from 16.8 MB in naive execution to 4.2 MB with fused operations, a 4× reduction).
Sự thực thi Mô hình (Execution Model)
Trung gian Các tensor Được lưu trữ (Intermediate Tensors Stored)
Tổng Bộ nhớ Sự sử dụng (MB) (Total Memory Usage (MB))
Ngây thơ Sự thực thi (Naïve Execution)
X’, X’ ’
16.8 MB
Được hợp nhất Sự thực thi (Fused Execution)
Không có (None)
4.2 MB
Hiệu suất các lợi ích và các sự ràng buộc (Performance benefits and constraints) Hạt nhân sự hợp nhất mang lại một vài chính các lợi thế thứ mà tăng cường
bộ nhớ tính hiệu quả và sự tính toán thông lượng (Kernel fusion brings several key advantages that enhance memory efficiency and computation throughput). Bằng cách việc làm giảm bộ nhớ các truy cập, được hợp nhất các hạt nhân
đảm bảo rằng trung gian các giá trị ở lại bên trong các thanh ghi thay vì việc bị một cách lặp lại được ghi tới và được đọc
từ bộ nhớ (By reducing memory accesses, fused kernels ensure that intermediate values stay within registers instead of being repeatedly written to and read from memory). Điều này một cách đáng kể làm hạ thấp bộ nhớ lưu lượng, thứ mà là một trong những chính các nút thắt cổ chai
trong máy học các khối lượng công việc (This significantly lowers memory traffic, which is one of the primary bottlenecks in machine learning workloads). Các GPU và các TPU, một cách cụ thể, hưởng lợi từ hạt nhân sự hợp nhất bởi vì
cao-băng thông bộ nhớ là một khan hiếm tài nguyên, và việc làm giảm bộ nhớ các giao dịch dẫn tới tốt hơn
sự sử dụng của tính toán các đơn vị (NVIDIA Corporation 2020) (GPUs and TPUs, in particular, benefit from kernel fusion because high-bandwidth memory is a scarce resource, and reducing memory transactions leads to better utilization of compute units (NVIDIA Corporation 2020)).
Tuy nhiên, không tất cả các hoạt động có thể được hợp nhất một cách tùy ý (However, not all operations can be fused arbitrarily). Theo-phần tử các hoạt động, chẳng hạn như ReLU, lô
chuẩn hóa, và đơn giản số học các sự biến đổi, là lý tưởng các ứng cử viên cho sự hợp nhất vì của chúng
các sự tính toán phụ thuộc chỉ trên đơn các phần tử từ đầu vào tensor (Element-wise operations, such as ReLU, batch normalization, and simple arithmetic transformations, are ideal candidates for fusion since their computations depend only on single elements from the input tensor). Ma trận các phép nhân và
các tích chập ràng buộc sự hợp nhất bởi vì chúng liên quan tới các sự rút gọn và lớn dữ liệu sự di chuyển; chúng là
thường được hợp nhất với theo-phần tử các phần kết (epilogues) chẳng hạn như độ chệch (bias), sự chuẩn hóa các biến thể, hoặc sự kích hoạt, nhưng
không thể được tự do được hợp nhất với không liên quan toàn cầu các hoạt động (Matrix multiplications and convolutions constrain fusion because they involve reductions and large data movement; they are often fused with element-wise epilogues such as bias, normalization variants, or activation, but cannot be freely fused with unrelated global operations).
Một cái khác chính sự xem xét là thanh ghi áp lực (Another major consideration is register pressure). Việc hợp nhất nhiều các hoạt động có nghĩa tất cả tạm thời
các giá trị phải được giữ trong các thanh ghi thay vì bộ nhớ (Fusing multiple operations means all temporary values must be kept in registers rather than memory). Trong khi điều này loại bỏ dư thừa bộ nhớ các lượt ghi,
nó cũng làm tăng thanh ghi nhu cầu (While this eliminates redundant memory writes, it also increases register demand). Nếu một được hợp nhất hạt nhân vượt quá có sẵn các thanh ghi trên mỗi luồng,
hệ thống phải làm tràn dư thừa các giá trị vào được chia sẻ bộ nhớ, việc giới thiệu bổ sung độ trễ và có khả năng
việc phủ định các lợi ích của sự hợp nhất (If a fused kernel exceeds the available registers per thread, the system must spill excess values into shared memory, introducing additional latency and potentially negating the benefits of fusion). Trên các GPU, nơi luồng sự chiếm đóng (số lượng của các luồng thứ mà có thể
chạy trong song song) là bị giới hạn bởi có sẵn các thanh ghi, quá mức sự hợp nhất có thể làm giảm tính song song, việc dẫn tới
giảm dần các phần thu về (On GPUs, where thread occupancy (the number of threads that can run in parallel) is limited by available registers, excessive fusion can reduce parallelism, leading to diminishing returns).
Khác nhau AI các máy gia tốc và các trình biên dịch xử lý sự hợp nhất trong khác biệt các cách (Different AI accelerators and compilers handle fusion in distinct ways). NVIDIA các GPU, cho ví dụ,
thiên vị cấp độ-nhóm (warp) tính song song, nơi theo-phần tử sự hợp nhất là thẳng thắn (NVIDIA Corporation
2020) (NVIDIA GPUs, for example, favor warp-level parallelism, where element-wise fusion is straightforward (NVIDIA Corporation 2020)). Các TPU, trên mặt khác, ưu tiên tâm thu mảng sự thực thi cho dày đặc ma trận các hoạt động
(Jouppi et al. 2017) (TPUs, on the other hand, prioritize systolic array execution for dense matrix operations (Jouppi et al. 2017)). Trình biên dịch và suy luận các ngăn xếp chẳng hạn như TVM, XLA, TensorRT, và MLIR áp dụng
đồ thị các lượt viết lại, việc hạ thấp các đường truyền (passes), hoặc xây dựng-công cụ (engine-building) các kinh nghiệm để cân bằng bộ nhớ các khoản tiết kiệm chống lại
sự thực thi các sự ràng buộc (Chen et al. 2018; Google 2025; NVIDIA 2024c; Lattner et al. 2020) (Compiler and inference stacks such as TVM, XLA, TensorRT, and MLIR apply graph rewrites, lowering passes, or engine-building heuristics to balance memory savings against execution constraints (Chen et al. 2018; Google 2025; NVIDIA 2024c; Lattner et al. 2020)).
Mặc dù của nó các lợi thế, sự hợp nhất là không luôn luôn có lợi (Despite its advantages, fusion is not always beneficial). Một số AI các bộ khung cho phép các nhà phát triển
để vô hiệu hóa sự hợp nhất một cách có chọn lọc, đặc biệt khi việc gỡ lỗi hiệu suất các vấn đề hoặc việc tạo ra thường xuyên
mô hình các sự sửa đổi (Some AI frameworks allow developers to disable fusion selectively, especially when debugging performance issues or making frequent model modifications). Quyết định để hợp nhất các hoạt động phải xem xét các sự đánh đổi giữa bộ nhớ
tính hiệu quả, thanh ghi sự sử dụng, và phần cứng sự thực thi các sự ràng buộc để đảm bảo rằng sự hợp nhất dẫn tới hữu hình
hiệu suất các sự cải thiện (The decision to fuse operations must consider trade-offs between memory efficiency, register usage, and hardware execution constraints to ensure that fusion leads to tangible performance improvements).
Những sự hợp nhất các quyết định này là cuối cùng về dữ liệu tính cục bộ, thứ mà bây giờ buộc cùng nhau của chương
chính dữ liệu sự di chuyển các chiến lược (These fusion decisions are ultimately about data locality, which now ties together the chapter’s core data movement strategies).
Điểm kiểm tra 11.3 (Checkpoint 11.3): Dữ liệu sự di chuyển và hạt nhân sự hợp nhất (Data movement and kernel fusion)
Dữ liệu luồng xây dựng các khối là bây giờ ở vị trí: dữ liệu tính cục bộ, tensor bố cục, và hạt nhân sự hợp nhất (The dataflow building blocks are now in place: data locality, tensor layout, and kernel fusion).
Bạn nên có khả năng để lập luận thông qua mỗi cái (You should be able to reason through each one):
□Tính cục bộ sự lựa chọn (Locality choice):
Cho trước trọng số-tính cố định, đầu ra-tính cố định, và đầu vào-tính cố định
các dữ liệu luồng, cái nào tensor thực hiện mỗi cái giữ gần tính toán các đơn vị, và cách nào làm đó
sự lựa chọn chuyển đổi nơi bộ nhớ lưu lượng hạ cánh (Given weight-stationary, output-stationary, and input-stationary dataflows, which tensor does each hold near the compute units, and how does that choice shift where the memory traffic lands)?
□Bố cục sự khớp (Layout match): Một hạt nhân chạy trên một phần phụ trợ việc mong đợi NHWC nhưng nhận một NCHW
tensor (A kernel runs on a backend expecting NHWC but receives an NCHW tensor). Dự đoán cái gì xảy ra tới của nó bộ nhớ truy cập mẫu và tới được phân phối thông lượng (Predict what happens to its memory access pattern and to delivered throughput).

11. Phần cứng Sự gia tốc (Hardware Acceleration)
615
37
Việc xếp ô gạch (Vòng lặp Sự đóng khối) (Tiling (Loop Blocking)):
Này sự tái cấu trúc một cách trực
tiếp kích hoạt "ít chuyến đi tới bộ
nhớ" sự thấu hiểu bằng cách việc phân
vùng một sự tính toán thành các khối thứ
mà vừa vặn hoàn toàn bên trong nhanh cục
bộ bộ nhớ cache (This restructuring directly enables the “fewer trips to memory” insight by partitioning a computation into blocks that fit entirely within fast local cache).
Thay vì việc lấy
một phần tử từ chậm DRAM
𝒪(𝑁) lần trong một ngây thơ ma trận
phép nhân, nó là được lấy một lần trên mỗi
ô gạch và sau đó được tái sử dụng trong khi thường
trú trong nhanh tầng (Lam et
al. 1991) (Instead of fetching an element from slow DRAM 𝒪(𝑁) times in a naive matrix multiply, it is fetched once per tile and then reused while resident in the fast tier (Lam et al. 1991)). Này sự làm giảm trong
bộ nhớ lưu lượng là chính
nguồn của lớn khoảng trống giữa
ngây thơ ma trận phép nhân
và được tối ưu hóa GEMM
các thủ tục (This reduction in memory traffic is the primary source of the large gap between naive matrix multiplication and optimized GEMM routines).
□Sự hợp nhất tính đủ điều kiện (Fusion eligibility): Cho một Conv2D, một BatchNorm, và một ReLU được thực thi theo trình tự, quyết định
cái nào các cặp là đáng giá việc hợp nhất và cái gì xác định liệu việc hợp nhất chúng mang lại lợi ích (For a Conv2D, a BatchNorm, and a ReLU executed in sequence, decide which pairs are worth fusing and what determines whether fusing them pays off).
□Còn lại khoảng trống (Remaining gap): Tính cục bộ, bố cục, và sự hợp nhất là tất cả được chọn tốt, tuy nhiên hoạt động vẫn
đình trệ trên bộ nhớ (Locality, layout, and fusion are all chosen well, yet the operation still stalls on memory). Cái gì là bị thiếu sự biến đổi, và tại sao làm ba cái khác không
giải quyết nó (What is the missing transformation, and why do the other three not address it)?
11.8.1.4 Hiệu quả-bộ nhớ việc xếp ô gạch các chiến lược (Memory-efficient tiling strategies)
Trong khi hiện đại AI các máy gia tốc cung cấp cao tính toán thông lượng, của chúng hiệu suất là thường
bị giới hạn bởi bộ nhớ băng thông thay vì thô xử lý sức mạnh (While modern AI accelerators offer high computational throughput, their performance is often limited by memory bandwidth rather than raw processing power). Nếu dữ liệu không thể được cung cấp tới
xử lý các đơn vị đủ nhanh, sự thực thi các sự đình trệ xảy ra, việc dẫn tới bị lãng phí các chu kỳ và không hiệu quả phần cứng
sự sử dụng (If data cannot be supplied to processing units fast enough, execution stalls occur, leading to wasted cycles and inefficient hardware utilization).
Việc xếp ô gạch37 làm giảm bớt này vấn đề bằng cách việc tái cấu trúc các sự tính toán thành nhỏ hơn, thân thiện-với-bộ nhớ các bài
toán con (Tiling37 mitigates this issue by restructuring computations into smaller, memory-friendly subproblems). Chính sự thấu hiểu là trực tiếp: nếu chúng ta không thể làm bộ nhớ nhanh hơn, chúng ta có thể ít nhất tạo
ít chuyến đi tới nó (The core insight is direct: if we cannot make memory faster, we can at least make fewer trips to it). Thay vì việc xử lý toàn bộ các ma trận hoặc các tensor cùng lúc, thứ mà dẫn tới quá mức bộ nhớ
lưu lượng, việc xếp ô gạch phân vùng các sự tính toán thành nhỏ hơn các khối (các ô gạch) thứ mà vừa vặn bên trong nhanh cục bộ bộ nhớ (cho
ví dụ, các bộ nhớ cache, được chia sẻ bộ nhớ, hoặc các thanh ghi) (Lam et al. 1991) (Instead of processing entire matrices or tensors at once, which leads to excessive memory traffic, tiling partitions computations into smaller blocks (tiles) that fit within fast local memory (for example, caches, shared memory, or registers) (Lam et al. 1991)).
Ma trận phép nhân, một cách rộng rãi được sử dụng trong AI các mô hình, chứng minh không hiệu quả bộ nhớ truy cập khi
được triển khai một cách ngây thơ (Matrix multiplication, widely used in AI models, demonstrates inefficient memory access when implemented naively). Danh sách 11.20 hiển thị cách nào, mà không việc xếp ô gạch, lặp lại bộ nhớ các truy cập cho
cùng dữ liệu dẫn tới không cần thiết băng thông sự tiêu thụ (Listing 11.20 shows how, without tiling, repeated memory accesses for the same data lead to unnecessary bandwidth consumption).
Danh sách 11.20: Ngây thơ Ma trận Phép nhân: Trực tiếp sự triển khai mà không việc xếp ô gạch yêu cầu 𝒪(𝑁3) bộ nhớ các truy cập cho 𝑁×𝑁
các ma trận, một cách lặp lại việc lấy cùng các phần tử từ chậm DRAM bộ nhớ và việc giới hạn hiệu suất tới một phần nhỏ của lý thuyết
đỉnh thông lượng (Listing 11.20: Naïve Matrix Multiplication: Direct implementation without tiling requires 𝒪(𝑁3) memory accesses for 𝑁×𝑁 matrices, repeatedly fetching the same elements from slow DRAM memory and limiting performance to a fraction of theoretical peak throughput).
cho (for) i trong phạm vi (in range)(N):
cho (for) j trong phạm vi (in range)(N):
cho (for) k trong phạm vi (in range)(N):
C[i, j] += A[i, k] * B[k, j]
# Một cách lặp lại việc lấy (Repeatedly fetching)
# A[i, k] và (and) B[k, j]
Mỗi sự lặp lại yêu cầu việc tải các phần tử từ các ma trận 𝐴 và 𝐵 nhiều lần từ bộ nhớ,
việc gây ra quá mức dữ liệu sự di chuyển (Each iteration requires loading elements from matrices 𝐴 and 𝐵 multiple times from memory, causing excessive data movement). Như kích thước của các ma trận tăng, bộ nhớ nút thắt cổ chai
tồi tệ hơn, việc giới hạn hiệu suất (As the size of the matrices increases, the memory bottleneck worsens, limiting performance).
Việc xếp ô gạch giải quyết này vấn đề bằng cách việc đảm bảo rằng nhỏ hơn các phần của các ma trận là được tải vào
nhanh bộ nhớ, được tái sử dụng một cách hiệu quả, và chỉ được ghi trở lại tới chính bộ nhớ khi cần thiết (Tiling addresses this problem by ensuring that smaller portions of matrices are loaded into fast memory, reused efficiently, and only written back to main memory when necessary). Này
kỹ thuật là đặc biệt quan trọng trong AI các máy gia tốc, nơi bộ nhớ các truy cập thống trị sự thực thi
thời gian (This technique is especially important in AI accelerators, where memory accesses dominate execution time). Hình 11.14 dán nhãn tích 𝐶 = 𝐴𝐵 bởi của nó ba các chiều hướng: 𝑀 các hàng và 𝐾 các cột trong
𝐴, 𝐾 các hàng và 𝑁 các cột trong 𝐵, và 𝑀×𝑁 trong đầu ra 𝐶 (Figure 11.14 labels the product 𝐶= 𝐴𝐵 by its three dimensions: 𝑀 rows and 𝐾 columns in 𝐴, 𝐾 rows and 𝑁 columns in 𝐵, and 𝑀×𝑁 in the output 𝐶). Mỗi được làm nổi bật ô gạch là làm việc
tập hợp thứ mà vừa vặn trong nhanh bộ nhớ tại một khoảnh khắc: một xanh lá 𝑀tile×𝐾tile hàng dải của 𝐴 nhân một hồng
𝐾tile×𝑁tile cột dải của 𝐵 để tích lũy một xanh lam 𝑀tile×𝑁tile đầu ra khối (Block𝑚,𝑛) của 𝐶 (Each highlighted tile is the working set that fits in fast memory at one moment: a green 𝑀tile×𝐾tile row band of 𝐴 multiplies a pink 𝐾tile×𝑁tile column band of 𝐵 to accumulate one blue 𝑀tile×𝑁tile output block (Block𝑚,𝑛) of 𝐶). Chính
sự thấu hiểu là rằng chúng ta xử lý tất cả các sự tính toán cho mỗi ô gạch trước khi việc di chuyển tới tiếp theo cái, thay vì
việc nảy lên giữa các ô gạch và một cách lặp lại việc trả DRAM truy cập hình phạt (The key insight is that we process all computations for each tile before moving to the next, rather than bouncing between tiles and repeatedly paying the DRAM access penalty).
Việc xếp ô gạch các nguyên tắc cơ bản (Tiling fundamentals) Việc xếp ô gạch là dựa trên một thẳng thắn nguyên tắc: thay vì việc hoạt động trên một toàn bộ
dữ liệu cấu trúc cùng lúc, các sự tính toán là được chia thành nhỏ hơn các ô gạch thứ mà vừa vặn bên trong có sẵn nhanh
bộ nhớ (Tiling is based on a straightforward principle: instead of operating on an entire data structure at once, computations are divided into smaller tiles that fit within the available fast memory). Bằng cách việc cấu trúc sự thực thi xung quanh những các ô gạch này, dữ liệu sự tái sử dụng là được tối đa hóa, việc làm giảm dư thừa
bộ nhớ các truy cập và việc cải thiện tổng thể tính hiệu quả (By structuring execution around these tiles, data reuse is maximized, reducing redundant memory accesses and improving overall efficiency).
Xem xét ma trận phép nhân, một chính hoạt động trong máy học các khối lượng công việc (Consider matrix multiplication, a key operation in machine learning workloads). Hoạt động
tính toán 𝐶 = 𝐴×𝐵 nơi mỗi phần tử 𝐶[𝑖,𝑗] = ∑𝑘𝐴[𝑖,𝑘]×𝐵[𝑘,𝑗] (The operation computes 𝐶= 𝐴×𝐵 where each element 𝐶[𝑖,𝑗] = ∑𝑘𝐴[𝑖,𝑘]×𝐵[𝑘,𝑗]). Ngây thơ sự triển khai
được hiển thị sớm hơn trong danh sách 11.20 chứng minh chính vấn đề: mọi sự lặp lại của trong cùng vòng lặp
lấy các phần tử từ các ma trận 𝐴 và 𝐵 từ bộ nhớ, thực hiện một phép nhân, và cập nhật
ma trận 𝐶 (The naive implementation shown earlier in listing 11.20 demonstrates the core problem: every iteration of the innermost loop fetches elements from matrices 𝐴 and 𝐵 from memory, performs a multiplication, and updates matrix 𝐶). Bởi vì các ma trận là lớn, bộ xử lý một cách lặp lại tải lại cùng các giá trị từ bộ nhớ,
thậm chí mặc dù chúng đã vừa được sử dụng trong trước đó các sự tính toán (Because matrices are large, the processor repeatedly reloads the same values from memory, even though they were just used in previous computations).
Này dữ liệu sự di chuyển chi phí chung là đắt đỏ: việc lấy từ DRAM là 100–1,000× chậm hơn so với
việc truy cập trên-chip bộ nhớ cache hoặc các thanh ghi (Horowitz 2014; Sze et al. 2017) (This data movement overhead is expensive: fetching from DRAM is 100–1,000× slower than accessing on-chip cache or registers (Horowitz 2014; Sze et al. 2017)). Giải pháp là việc xếp ô gạch (The solution is tiling).

616
11.8 Dữ liệu luồng Sự tối ưu hóa (Dataflow Optimization)
N
K
Ktile
Ntile
B ma trận (B matrix)
Mtile
Ntile
Khối (Block) m,n
C ma trận (C matrix)
K
M
Mtile
Ktile
A ma trận (A matrix)
Hình 11.14: Ma trận Việc xếp ô gạch: Việc phân vùng lớn các ma trận thành nhỏ hơn các ô gạch tối ưu hóa dữ liệu sự tái sử dụng và làm giảm bộ nhớ truy cập
chi phí chung trong suốt sự tính toán (Figure 11.14: Matrix Tiling: Partitioning large matrices into smaller tiles optimizes data reuse and reduces memory access overhead during computation). Này kỹ thuật cải thiện hiệu suất trên AI các máy gia tốc bằng cách việc kích hoạt hiệu quả việc tải và
việc xử lý của dữ liệu trong nhanh bộ nhớ, việc tối thiểu hóa các sự truyền tải từ chậm hơn chính bộ nhớ (This technique improves performance on AI accelerators by enabling efficient loading and processing of data in fast memory, minimizing transfers from slower main memory).
Hiệu suất các lợi ích của việc xếp ô gạch (Performance benefits of tiling) Thay vì việc tính toán một phần tử tại một thời gian và một cách liên tục việc di chuyển
dữ liệu vào và ra của chậm bộ nhớ, việc xếp ô gạch xử lý các ma trận con (các ô gạch) tại một thời gian, việc giữ thường xuyên
được sử dụng các giá trị trong nhanh bộ nhớ (Instead of computing one element at a time and constantly moving data in and out of slow memory, tiling processes submatrices (tiles) at a time, keeping frequently used values in fast memory). Ý tưởng là để chia các ma trận thành nhỏ hơn các khối thứ mà vừa vặn bên trong
bộ nhớ cache hoặc được chia sẻ bộ nhớ của bộ xử lý, việc đảm bảo rằng một khi một khối là được tải, nó là được tái sử dụng nhiều
lần trước khi việc di chuyển tới tiếp theo cái (The idea is to divide the matrices into smaller blocks that fit within the processor’s cache or shared memory, ensuring that once a block is loaded, it is reused multiple times before moving to the next one). Danh sách 11.21 chứng minh thân thiện-với-bộ nhớ cache vòng lặp sự đóng khối: các
vòng lặp các ranh giới phân vùng các ma trận thành các ô gạch, và phần cứng bộ nhớ cache hệ thống phân cấp giữ gần đây được sử dụng
ô gạch dữ liệu gần tới tính toán các đơn vị khi truy cập thứ tự có tính cục bộ (Listing 11.21 demonstrates cache-friendly loop blocking: the loop bounds partition the matrices into tiles, and the hardware cache hierarchy keeps recently used tile data close to the compute units when access order has locality).
Danh sách 11.21: Được đóng khối-Bởi-Bộ nhớ cache Ma trận Phép nhân: Này cấp độ-cao vòng lặp sự đóng khối cách tiếp cận chia các ma trận thành nhỏ hơn
chỉ mục các phạm vi để phần cứng các bộ nhớ cache có thể tái sử dụng dữ liệu bên trong mỗi ô gạch, việc cải thiện tính toán tính hiệu quả mà không có tường minh bộ nhớ nháp
các lượt tải (Listing 11.21: Cache-Blocked Matrix Multiplication: This high-level loop blocking approach divides matrices into smaller index ranges so hardware caches can reuse data within each tile, improving computational efficiency without explicit scratchpad loads).
TILE_SIZE = 32
# Chọn một ô gạch kích thước dựa trên (Choose a tile size based on)
# phần cứng các sự ràng buộc (hardware constraints)
# Bộ nhớ cache sự đóng khối: phân vùng dữ liệu thông qua vòng lặp các ranh giới. (Cache blocking: partition data via loop bounds.)
# Các lượt tải là ngầm định thông qua phần cứng bộ nhớ cache hệ thống phân cấp. (Loads are implicit through the hardware cache hierarchy.)
cho (for) i trong phạm vi (in range)(0, N, TILE_SIZE):
cho (for) j trong phạm vi (in range)(0, N, TILE_SIZE):
cho (for) k trong phạm vi (in range)(0, N, TILE_SIZE):
# Mỗi ô gạch được tính toán một cách độc lập (Each tile computed independently)
cho (for) ii trong phạm vi (in range)(i, i + TILE_SIZE):
cho (for) jj trong phạm vi (in range)(j, j + TILE_SIZE):
cho (for) kk trong phạm vi (in range)(k, k + TILE_SIZE):
C[ii, jj] += A[ii, kk] * B[kk, jj]
Này sự tái cấu trúc một cách đáng kể cải thiện hiệu suất thông qua ba củng cố các hiệu ứng (This restructuring significantly improves performance through three reinforcing effects). Bộ nhớ
sự tái sử dụng cải thiện bởi vì cách tiếp cận truy cập một nhỏ ô gạch một cách lặp lại trong khi nó là có khả năng để duy trì trong
bộ nhớ cache trước khi việc di chuyển vào tới tiếp theo ô gạch, thay vì việc lấy các phần tử từ 𝐴 và 𝐵 một cách lặp lại từ
chậm bộ nhớ, thứ mà tối thiểu hóa dư thừa bộ nhớ các truy cập (Memory reuse improves because the approach visits a small tile repeatedly while it is likely to remain in cache before moving on to the next tile, rather than fetching elements from 𝐴 and 𝐵 repeatedly from slow memory, which minimizes redundant memory accesses). Bộ nhớ băng thông sự sử dụng giảm

11. Phần cứng Sự gia tốc (Hardware Acceleration)
617
như một trực tiếp hệ quả: vì mỗi ô gạch là được sử dụng nhiều lần trước khi việc bị trục xuất, hầu hết được yêu cầu
dữ liệu là có sẵn trong L1/L2 bộ nhớ cache hoặc được chia sẻ bộ nhớ thay vì DRAM, vì vậy lưu lượng giảm và sự thực thi
tăng tốc độ (as a direct consequence: since each tile is used multiple times before being evicted, most required data is available in L1/L2 cache or shared memory rather than DRAM, so traffic falls and execution speeds up). Tính toán tính hiệu quả tăng lên trong lượt, bởi vì các bộ xử lý dành ít thời gian chờ cho dữ liệu
và nhiều thời gian thực hiện hữu ích công việc; trong các kiến trúc giống như các GPU và các TPU, nơi hàng ngàn của
song song xử lý các đơn vị hoạt động một cách đồng thời, việc xếp ô gạch giữ dữ liệu được đọc và được xử lý trong một được cấu trúc
cách thức thứ mà tránh không cần thiết các sự đình trệ (Compute efficiency rises in turn, because processors spend less time waiting for data and more time performing useful work; in architectures like GPUs and TPUs, where thousands of parallel processing units operate simultaneously, tiling keeps data read and processed in a structured manner that avoids unnecessary stalls).
Này kỹ thuật là đặc biệt hiệu quả trong AI các máy gia tốc, nơi máy học các khối lượng công việc
bao gồm của lớn ma trận các phép nhân và tensor các sự biến đổi (This technique is particularly effective in AI accelerators, where machine learning workloads consist of large matrix multiplications and tensor transformations). Mà không việc xếp ô gạch, những các khối lượng công việc này
một cách nhanh chóng trở thành bị ràng buộc bởi bộ nhớ, việc có nghĩa hiệu suất là bị ràng buộc bởi cách nào nhanh dữ liệu có thể được
lấy lại thay vì bởi thô tính toán sức mạnh của bộ xử lý (Without tiling, these workloads quickly become memory bound, meaning performance is constrained by how fast data can be retrieved rather than by the raw computational power of the processor).
Việc xếp ô gạch các phương pháp (Tiling methods) Trong khi tổng quát nguyên tắc của việc xếp ô gạch duy trì cùng, thứ mà liên quan tới việc phân vùng
lớn các sự tính toán thành nhỏ hơn các bài toán con để cải thiện bộ nhớ sự tái sử dụng, có khác nhau các cách để
áp dụng việc xếp ô gạch dựa trên cấu trúc của sự tính toán và phần cứng các sự ràng buộc (While the general principle of tiling remains the same, which involves partitioning large computations into smaller subproblems to improve memory reuse, there are different ways to apply tiling based on the structure of the computation and hardware constraints). Hai chính
việc xếp ô gạch các chiến lược là thuộc về không gian việc xếp ô gạch và thuộc về thời gian việc xếp ô gạch (The two primary tiling strategies are spatial tiling and temporal tiling). Những các chiến lược này tối ưu hóa khác nhau các khía cạnh
của sự tính toán và bộ nhớ truy cập, và trong thực tế, chúng là thường được kết hợp để đạt được tốt nhất
hiệu suất (These strategies optimize different aspects of computation and memory access, and in practice, they are often combined to achieve the best performance).
Thuộc về không gian việc xếp ô gạch phân vùng dữ liệu các cấu trúc thành nhỏ hơn các khối thứ mà vừa vặn bên trong nhanh bộ nhớ (Spatial tiling partitions data structures into smaller blocks that fit within fast memory). Được xếp ô gạch
ma trận phép nhân trong danh sách 11.21 chứng minh thân thiện-với-bộ nhớ cache vòng lặp sự đóng khối: mã làm
không phát ra tường minh bộ nhớ nháp các lượt tải, nhưng có dạng-ô gạch truy cập mẫu để phần cứng các bộ nhớ cache tái sử dụng
lân cận các giá trị trước khi chúng là bị trục xuất (The tiled matrix multiplication in listing 11.21 demonstrates cache-friendly loop blocking: the code does not issue explicit scratchpad loads, but the tile-shaped access pattern lets hardware caches reuse nearby values before they are evicted). Này chiến lược là đặc biệt có lợi cho lớn các tensor thứ mà
vượt quá nhanh bộ nhớ khả năng—bằng cách việc chia các sự tính toán thành nhỏ hơn các ô gạch, dữ liệu sự di chuyển giữa
bộ nhớ các cấp độ là được tối thiểu hóa, việc giữ các hoạt động được cục bộ hóa bên trong bộ nhớ cache các hệ thống phân cấp (This strategy is particularly beneficial for large tensors that exceed fast memory capacity—by breaking computations into smaller tiles, data movement between memory levels is minimized, keeping operations localized within cache hierarchies).
Thuộc về thời gian việc xếp ô gạch bổ sung thuộc về không gian việc xếp ô gạch bằng cách một cách tường minh việc dàn dựng dữ liệu trong được chia sẻ bộ nhớ hoặc các thanh ghi
và việc tổ chức lại sự tính toán thứ tự xung quanh đó được dàn dựng dữ liệu (Temporal tiling complements spatial tiling by explicitly staging data in shared memory or registers and reorganizing the computation order around that staged data). Nhiều ML các khối lượng công việc truy cập
cùng dữ liệu một cách lặp lại qua các sự lặp lại—mà không thuộc về thời gian việc xếp ô gạch, điều này dẫn tới dư thừa bộ nhớ
các lượt lấy (Many ML workloads access the same data repeatedly across iterations—without temporal tiling, this results in redundant memory fetches). Thuộc về thời gian việc xếp ô gạch tái cấu trúc sự tính toán để đảm bảo rằng thường xuyên được sử dụng dữ liệu ở lại trong
nhanh bộ nhớ cho cũng lâu như có thể trước khi tiếp theo sự tính toán bắt đầu (Temporal tiling restructures the computation to ensure that frequently used data stays in fast memory for as long as possible before the next computation begins).
Một kinh điển ví dụ nơi thuộc về thời gian việc xếp ô gạch là có lợi là tích chập các hoạt động, nơi cùng
tập hợp của các trọng số là được áp dụng tới nhiều đầu vào các vùng (A classic example where temporal tiling is beneficial is convolutional operations, where the same set of weights is applied to multiple input regions). Mà không vòng lặp sự đóng khối, những các trọng số này có thể được
tải từ bộ nhớ nhiều lần cho mỗi sự tính toán (Without loop blocking, these weights might be loaded from memory multiple times for each computation). Với thuộc về thời gian việc xếp ô gạch, sự tính toán là
được sắp xếp lại để mà các trọng số duy trì trong nhanh bộ nhớ qua nhiều các đầu vào, việc làm giảm không cần thiết
bộ nhớ các lượt lấy và việc cải thiện tổng thể tính hiệu quả (With temporal tiling, the computation is reordered so that the weights remain in fast memory across multiple inputs, reducing unnecessary memory fetches and improving overall efficiency). Danh sách 11.22 minh họa tường minh ô gạch sự dàn dựng:
mã tải các khối của 𝐴 và 𝐵 vào tạm thời nhanh lưu trữ, sau đó tái sử dụng chúng qua nhiều trong cùng-vòng lặp
các hoạt động (Listing 11.22 illustrates explicit tile staging: the code loads blocks of 𝐴 and 𝐵 into temporary fast storage, then reuses them across multiple inner-loop operations).
Danh sách 11.22: Tường minh Ô gạch Sự dàn dựng: Làm giảm dư thừa bộ nhớ các truy cập bằng cách việc tải các ô gạch vào nhanh tạm thời lưu trữ và
việc tái sử dụng chúng qua nhiều trong cùng-vòng lặp các hoạt động (Listing 11.22: Explicit Tile Staging: Reduces redundant memory accesses by loading tiles into fast temporary storage and reusing them across multiple inner-loop operations).
# Tường minh ô gạch sự dàn dựng: tải dữ liệu vào nhanh (Explicit tile staging: load data into fast)
# tạm thời lưu trữ trước trong cùng các vòng lặp. (temporary storage before the inner loops.)
cho (for) i trong phạm vi (in range)(0, N, TILE_SIZE):
cho (for) j trong phạm vi (in range)(0, N, TILE_SIZE):
cho (for) k trong phạm vi (in range)(0, N, TILE_SIZE):
# Một cách tường minh tải các ô gạch vào nhanh bộ nhớ (Explicitly load tiles into fast memory)
A_tile = A[i:i+TILE_SIZE, k:k+TILE_SIZE]
B_tile = B[k:k+TILE_SIZE, j:j+TILE_SIZE]
# Tái sử dụng được tải các ô gạch cho tất cả trong cùng các sự lặp lại (Reuse loaded tiles for all inner iterations)
cho (for) ii trong phạm vi (in range)(TILE_SIZE):
cho (for) jj trong phạm vi (in range)(TILE_SIZE):
cho (for) kk trong phạm vi (in range)(TILE_SIZE):
C[i+ii, j+jj] += A_tile[ii, kk] *
B_tile[kk, jj]
Tường minh ô gạch sự dàn dựng cải thiện hiệu suất bằng cách việc đảm bảo rằng dữ liệu được tải vào nhanh bộ nhớ là
được sử dụng nhiều lần trước khi việc bị trục xuất (Explicit tile staging improves performance by ensuring that the data loaded into fast memory is used multiple times before being evicted). Trong này sự triển khai, nhỏ các ô gạch của các ma trận 𝐴 và 𝐵
là một cách tường minh được tải vào tạm thời lưu trữ trước khi việc thực hiện các sự tính toán, việc làm giảm bộ nhớ

618
11.8 Dữ liệu luồng Sự tối ưu hóa (Dataflow Optimization)
lấy chi phí chung (fetch overhead). Này sự tái cấu trúc cho phép sự tính toán để xử lý một toàn bộ ô gạch trước khi việc di chuyển tới
tiếp theo cái, do đó việc làm giảm số lượng của các lần dữ liệu phải được tải từ chậm hơn bộ nhớ (This restructuring allows the computation to process an entire tile before moving to the next, thereby reducing the number of times data must be loaded from slower memory).
Này kỹ thuật là đặc biệt hữu dụng trong các khối lượng công việc nơi một số các giá trị là được sử dụng một cách lặp lại, chẳng hạn
như các tích chập, hồi quy thần kinh các mạng (RNNs), và tự-sự chú ý các cơ chế trong các transformer (This technique is particularly useful in workloads where certain values are used repeatedly, such as convolutions, recurrent neural networks (RNNs), and self-attention mechanisms in transformers).
Bằng cách việc áp dụng vòng lặp sự đóng khối, AI các máy gia tốc có thể một cách đáng kể làm giảm bộ nhớ các sự đình trệ và cải thiện
sự thực thi thông lượng (By applying loop blocking, AI accelerators can significantly reduce memory stalls and improve execution throughput).
Việc xếp ô gạch các thách thức và các sự đánh đổi (Tiling challenges and trade-offs) Việc xếp ô gạch cải thiện hiệu suất chỉ khi ô gạch khớp
tính cục bộ ngân sách của phần cứng (Tiling improves performance only when the tile matches the locality budget of the hardware). Nếu ô gạch là quá nhỏ, bộ nhớ các lượt lấy vẫn thống trị sự thực thi thời gian
bởi vì sự tái sử dụng là quá bị giới hạn (If the tile is too small, memory fetches still dominate execution time because reuse is too limited). Nếu ô gạch là quá lớn, nó vượt quá nhanh bộ nhớ và gây ra bộ nhớ cache sự giằng co (thrashing)
hoặc bộ nhớ nháp các sự tràn (If the tile is too large, it exceeds fast memory and causes cache thrashing or scratchpad spills). Việc chọn đúng ô gạch kích thước do đó một cách trực tiếp xác định tính toán tính hiệu quả
và bộ nhớ băng thông sự sử dụng (Selecting the right tile size therefore directly determines computational efficiency and memory bandwidth usage).
Ô gạch sự lựa chọn cũng kiểm soát tải trọng sự cân bằng (The tile choice also controls load balance). Trong các kiến trúc chẳng hạn như các GPU và các TPU, các sự tính toán
thực thi trong song song qua hàng ngàn của xử lý các đơn vị (In architectures such as GPUs and TPUs, computations execute in parallel across thousands of processing units). Nếu các ô gạch là không được phân phối một cách đồng đều, một số
các đơn vị duy trì nhàn rỗi trong khi những cái khác là bị quá tải, việc dẫn tới dưới mức tối ưu sự sử dụng của tính toán
các tài nguyên (If tiles are not evenly distributed, some units remain idle while others are overloaded, leading to suboptimal utilization of computational resources). Hiệu quả ô gạch việc lập lịch trình giữ song song sự thực thi được cân bằng và hiệu quả (Effective tile scheduling keeps parallel execution balanced and efficient).
Dữ liệu sự di chuyển duy trì giới hạn chi phí thậm chí sau khi việc xếp ô gạch (Data movement remains the limiting cost even after tiling). Mặc dù việc xếp ô gạch làm giảm số lượng của
chậm bộ nhớ các truy cập, việc truyền tải các ô gạch giữa hệ thống phân cấp các cấp độ vẫn gánh chịu độ trễ và năng lượng chi phí,
đặc biệt khi dữ liệu rơi từ bộ nhớ cache hoặc bộ nhớ nháp trở lại tới DRAM (Although tiling reduces the number of slow memory accesses, transferring tiles between hierarchy levels still incurs latency and energy cost, especially when data falls from cache or scratchpad back to DRAM). Hiệu quả bộ nhớ việc lấy trước
và việc lập lịch trình các chiến lược tối thiểu hóa này phần dư sự di chuyển và đảm bảo rằng dữ liệu là có sẵn khi
được cần (Efficient memory prefetching and scheduling strategies minimize this residual movement and ensure that data is available when needed).
Lai tạp việc xếp ô gạch kết hợp thuộc về không gian và thuộc về thời gian các chiến lược khi không chiều hướng một mình nắm bắt
khối lượng công việc của sự tái sử dụng mẫu (Hybrid tiling combines spatial and temporal strategies when neither dimension alone captures the workload’s reuse pattern). Một số AI các máy gia tốc sử dụng thuộc về không gian việc xếp ô gạch cho ma trận các phép nhân trong khi
việc tuyển dụng thuộc về thời gian việc xếp ô gạch cho trọng số sự tái sử dụng trong tích chập các lớp, một cách động việc điều chỉnh ô gạch các kích thước
hoặc việc sắp xếp lại các sự tính toán dựa trên thời gian-thực sự thực thi các điều kiện (Some AI accelerators use spatial tiling for matrix multiplications while employing temporal tiling for weight reuse in convolutional layers, dynamically adjusting tile sizes or reordering computations based on real-time execution conditions).
Thanh ghi sự đóng khối, đôi việc tạo bộ đệm, và phân cấp việc xếp ô gạch mở rộng cùng tính cục bộ nguyên tắc tại
nhỏ hơn và lớn hơn bộ nhớ các tầng (Register blocking, double buffering, and hierarchical tiling extend the same locality principle at smaller and larger memory tiers). AI các trình biên dịch và thời gian chạy các hệ thống chẳng hạn như TensorFlow XLA, TVM,
và MLIR một cách tự động chọn những việc xếp ô gạch các chiến lược này dựa trên phần cứng các sự ràng buộc, việc kích hoạt tinh-
chỉnh hiệu suất sự tối ưu hóa mà không có thủ công sự can thiệp (AI compilers and runtime systems such as TensorFlow XLA, TVM, and MLIR automatically select these tiling strategies based on hardware constraints, enabling fine-tuned performance optimization without manual intervention). Bảng 11.21 cung cấp một so sánh
tổng quan của thuộc về không gian, thuộc về thời gian, và lai tạp việc xếp ô gạch các cách tiếp cận, việc làm nổi bật của chúng tương ứng các lợi ích
và các sự đánh đổi (Table 11.21 provides a comparative overview of spatial, temporal, and hybrid tiling approaches, highlighting their respective benefits and trade-offs).
Bảng 11.21: Việc xếp ô gạch Các chiến lược: Thuộc về không gian, thuộc về thời gian, và lai tạp việc xếp ô gạch tối ưu hóa bộ nhớ truy cập các mẫu cho được cải thiện hiệu suất (Table 11.21: Tiling Strategies: Spatial, temporal, and hybrid tiling optimize memory access patterns for improved performance).
Thuộc về không gian việc xếp ô gạch tối đa hóa dữ liệu sự tái sử dụng bên trong nhanh bộ nhớ, thuộc về thời gian việc xếp ô gạch khai thác vòng lặp cấu trúc cho được làm giảm các truy cập, và lai tạp
việc xếp ô gạch kết hợp cả hai các cách tiếp cận (Spatial tiling maximizes data reuse within fast memory, temporal tiling exploits loop structure for reduced accesses, and hybrid tiling combines both approaches). AI các trình biên dịch và thời gian chạy các hệ thống sử dụng những các kỹ thuật này để một cách tự động tối ưu hóa mô hình
sự thực thi trên đa dạng phần cứng (AI compilers and runtime systems use these techniques to automatically optimize model execution on diverse hardware).
Khía cạnh (Aspect)
Thuộc về không gian Việc xếp ô gạch (Dữ liệu Việc xếp ô gạch) (Spatial Tiling (Data Tiling))
Thuộc về thời gian Việc xếp ô gạch (Vòng lặp Sự đóng khối) (Temporal Tiling (Loop Blocking))
Lai tạp Việc xếp ô gạch (Hybrid Tiling)
Chính Mục tiêu (Primary Goal)
Làm giảm bộ nhớ các truy cập bằng cách
việc giữ dữ liệu trong nhanh bộ nhớ lâu hơn (Reduce memory accesses by keeping data in fast memory longer)
Làm tăng dữ liệu sự tái sử dụng qua vòng lặp
các sự lặp lại (Increase data reuse across loop iterations)
Thích ứng một cách động tới
khối lượng công việc các sự ràng buộc (Adapt dynamically to workload constraints)
Sự tối ưu hóa
Trọng tâm (Optimization Focus)
Việc phân vùng dữ liệu các cấu trúc thành
nhỏ hơn, thân thiện-với-bộ nhớ các khối (Partitioning data structures into smaller, memory-friendly blocks)
Việc sắp xếp lại các sự tính toán để
tối đa hóa sự tái sử dụng trước khi sự trục xuất (Reordering computations to maximize reuse before eviction)
Việc cân bằng thuộc về không gian và
thuộc về thời gian sự tái sử dụng các chiến lược (Balancing spatial and temporal reuse strategies)
Bộ nhớ Sự sử dụng (Memory Usage)
Cải thiện bộ nhớ cache tính cục bộ và
làm giảm DRAM truy cập (Improves cache locality and reduces DRAM access)
Giữ thường xuyên được sử dụng dữ liệu trong
nhanh bộ nhớ cho nhiều
các sự lặp lại (Keeps frequently used data in fast memory for multiple iterations)
Tối thiểu hóa dữ liệu sự di chuyển
trong khi việc đảm bảo cao sự tái sử dụng (Minimizes data movement while ensuring high reuse)
Phổ biến Sử dụng
Các trường hợp (Common Use Cases)
Ma trận các phép nhân, các CNN,
tự-sự chú ý trong các transformer (Matrix multiplications, CNNs, self-attention in transformers)
Các tích chập, hồi quy thần kinh
các mạng (RNNs), lặp lại
các sự tính toán (Convolutions, recurrent neural networks (RNNs), iterative computations)
AI các máy gia tốc với
phân cấp bộ nhớ, hỗn hợp
các khối lượng công việc (AI accelerators with hierarchical memory, mixed workloads)
Hiệu suất
Các phần tăng (Performance Gains)
Được làm giảm bộ nhớ băng thông
các yêu cầu, tốt hơn bộ nhớ cache
sự sử dụng (Reduced memory bandwidth requirements, better cache utilization)
Thấp hơn bộ nhớ lấy độ trễ,
được cải thiện dữ liệu tính cục bộ (Lower memory fetch latency, improved data locality)
Được tối đa hóa tính hiệu quả qua
nhiều phần cứng các loại (Maximized efficiency across multiple hardware types)
Các thách thức (Challenges)
Yêu cầu cẩn thận ô gạch kích thước sự lựa chọn,
không hiệu quả cho các khối lượng công việc với
tối thiểu thuộc về không gian sự tái sử dụng (Requires careful tile size selection, inefficient for workloads with minimal spatial reuse)
Có thể làm tăng thanh ghi áp lực,
yêu cầu vòng lặp sự tái cấu trúc (Can increase register pressure, requires loop restructuring)
Độ phức tạp trong việc tinh chỉnh ô gạch kích thước
và sự thực thi thứ tự
một cách động (Complexity in tuning tile size and execution order dynamically)
Tốt nhất Khi (Best When)
Dữ liệu là lớn và cần để được
được phân vùng cho hiệu quả xử lý (Data is large and needs to be partitioned for efficient processing)
Cùng dữ liệu là được truy cập
nhiều lần qua các sự lặp lại (The same data is accessed multiple times across iterations)
Cả dữ liệu sự phân vùng và
dựa trên-sự lặp lại sự tái sử dụng là
quan trọng (Both data partitioning and iteration-based reuse are important)

11. Phần cứng Sự gia tốc (Hardware Acceleration)
619
Khi máy học các mô hình phát triển trong kích thước và độ phức tạp, việc xếp ô gạch duy trì một tới hạn công cụ cho
việc cải thiện phần cứng tính hiệu quả, việc đảm bảo rằng AI các máy gia tốc hoạt động gần của chúng thực tế tiềm năng (When machine learning models grow in size and complexity, tiling remains a critical tool for improving hardware efficiency, ensuring that AI accelerators operate near their practical potential).
Trong khi thủ công việc xếp ô gạch các chiến lược có thể cung cấp đáng kể các lợi ích, các trình biên dịch và nhận thức-phần cứng
sự tối ưu hóa các kỹ thuật xa hơn tăng cường hiệu suất bằng cách một cách tự động việc chọn hiệu quả việc xếp ô gạch
các chiến lược cho một cho trước khối lượng công việc (While manual tiling strategies can provide substantial benefits, compilers and hardware-aware optimization techniques further enhance performance by automatically selecting effective tiling strategies for a given workload).
11.8.2 Việc áp dụng ánh xạ các chiến lược tới thần kinh các mạng (Applying mapping strategies to neural networks)
Trong khi những nền tảng ánh xạ các kỹ thuật này áp dụng một cách rộng rãi, của chúng tính hiệu quả thay đổi dựa trên
tính toán cấu trúc, dữ liệu truy cập các mẫu, và sự song song hóa các cơ hội của khác nhau
thần kinh mạng các kiến trúc (While these foundational mapping techniques apply broadly, their effectiveness varies based on the computational structure, data access patterns, and parallelization opportunities of different neural network architectures). Mỗi kiến trúc áp đặt khác biệt các sự ràng buộc trên dữ liệu sự di chuyển,
bộ nhớ hệ thống phân cấp, và sự tính toán việc lập lịch trình, việc yêu cầu được điều chỉnh ánh xạ các chiến lược để tối ưu hóa
hiệu suất (Each architecture imposes distinct constraints on data movement, memory hierarchy, and computation scheduling, requiring tailored mapping strategies to optimize performance).
Một được cấu trúc cách tiếp cận tới việc ánh xạ là được yêu cầu để giải quyết tổ hợp sự bùng nổ của các sự lựa chọn
thứ mà phát sinh khi việc gán các sự tính toán tới AI các máy gia tốc (A structured approach to mapping is required to address the combinatorial explosion of choices that arise when assigning computations to AI accelerators). Thay vì việc đối xử mỗi mô hình như
một tách biệt sự tối ưu hóa bài toán, chúng ta nhận ra rằng cùng các nguyên tắc áp dụng qua khác nhau
các kiến trúc; chỉ của chúng ưu tiên chuyển đổi dựa trên khối lượng công việc các đặc trưng (Rather than treating each model as a separate optimization problem, we recognize that the same principles apply across different architectures; only their priority shifts based on workload characteristics). Mục tiêu là để một cách có hệ thống
chọn và áp dụng ánh xạ các chiến lược thứ mà tối đa hóa tính hiệu quả cho khác nhau các loại của máy học
các mô hình (The goal is to systematically select and apply mapping strategies that maximize efficiency for different types of machine learning models).
Những các nguyên tắc này áp dụng tới ba tiêu biểu AI các khối lượng công việc, mỗi cái được đặc trưng bởi khác biệt tính
toán các nhu cầu (These principles apply to three representative AI workloads, each characterized by distinct computational demands). Các CNN hưởng lợi từ thuộc về không gian dữ liệu sự tái sử dụng, việc làm cho trọng số-tính cố định sự thực thi
và sự ứng dụng của việc xếp ô gạch các kỹ thuật đặc biệt hiệu quả (CNNs benefit from spatial data reuse, making weight-stationary execution and the application of tiling techniques especially effective). Trong sự đối lập, các transformer là vốn dĩ
bị ràng buộc-bởi-bộ nhớ và phụ thuộc trên các chiến lược chẳng hạn như hiệu quả KV-bộ nhớ cache sự quản lý, được hợp nhất sự chú ý các cơ
chế, và cao độ song song sự thực thi để làm giảm bớt bộ nhớ lưu lượng (In contrast, transformers are inherently memory bound and rely on strategies such as efficient KV-cache management, fused attention mechanisms, and highly parallel execution to mitigate memory traffic). Các MLP, thứ mà liên quan tới đáng kể
ma trận phép nhân các hoạt động, đòi hỏi sự sử dụng của được cấu trúc việc xếp ô gạch, được tối ưu hóa trọng số các bố cục,
và nhận thức-bộ nhớ sự thực thi để tăng cường tổng thể hiệu suất (MLPs, which involve substantial matrix multiplication operations, demand the use of structured tiling, optimized weight layouts, and memory-aware execution to enhance overall performance).
Mặc dù của chúng các sự khác biệt, mỗi của những các mô hình này theo sau một chung tập hợp của ánh xạ các nguyên tắc, với
các sự biến đổi trong cách nào các sự tối ưu hóa là được ưu tiên (Despite their differences, each of these models follows a common set of mapping principles, with variations in how optimizations are prioritized). Bảng 11.22 tóm tắt sự phù hợp của khác nhau
sự tối ưu hóa các chiến lược cho các CNN, các transformer, và các MLP (Table 11.22 summarizes the suitability of different optimization strategies for CNNs, transformers, and MLPs).
Bảng 11.22: Cụ thể-Kiến trúc Ánh xạ Các chiến lược: Mỗi thần kinh mạng kiến trúc hưởng lợi từ khác nhau sự tối ưu hóa
các ưu tiên dựa trên của nó tính toán và bộ nhớ các đặc trưng (Table 11.22: Architecture-Specific Mapping Strategies: Each neural network architecture benefits from different optimization priorities based on its computational and memory characteristics).
Sự tối ưu hóa
Kỹ thuật (Optimization Technique)
Các CNN (CNNs)
Các transformer (Transformers)
Các MLP (MLPs)
Lý do căn bản (Rationale)
Dữ liệu luồng Chiến lược (Dataflow Strategy)
Trọng số Tính cố định (Weight Stationary)
Đầu vào
Tính cố định (Input Stationary)
Trọng số
Tính cố định (Weight Stationary)
Các CNN tái sử dụng các bộ lọc qua thuộc về không gian các vị trí;
các transformer tái sử dụng các sự kích hoạt (KV-bộ nhớ cache)
dưới đầu vào-tính cố định chiến lược được giới thiệu
sớm hơn; Các MLP tái sử dụng các trọng số qua các lô (CNNs reuse filters across spatial locations; transformers reuse activations (KV-cache) under the input-stationary strategy introduced earlier; MLPs reuse weights across batches).
Nhận thức-Bộ nhớ
Tensor Các bố cục (Memory-Aware Tensor Layouts)
Phụ thuộc-
Phần phụ trợ (thường (Backend-dependent (often)
NCHW cho (for)
cuDNN
các tích chập, (convolutions,)
các kênh-cuối trên (channels-last on)
Tensor Các lõi) (Tensor Cores))
Phụ thuộc-
Phần phụ trợ (Backend-dependent)
(hàng-chính ((row-major)
các sự kích hoạt (activations)
điển hình) (typical))
Hàng-chính
điển hình (Row-major typical)
Bố cục sự lựa chọn phụ thuộc trên phần phụ trợ hạt nhân đường dẫn
và độ chýnh xác chế độ (xem bố cục cuộc thảo luận
bên trên); các mục nhập gọi tên phổ biến các mặc định, không
phổ quát các sự quy định (Layout choice depends on backend kernel path and precision mode (see the layout discussion above); the entries name common defaults, not universal prescriptions).
Hạt nhân Sự hợp nhất (Kernel Fusion)
Tích chập + (Convolution +)
Sự kích hoạt (Activation)
Được hợp nhất
Sự chú ý (Fused Attention)
GEMM
Sự hợp nhất (GEMM Fusion)
Các CNN tối ưu hóa tích chập+sự kích hoạt sự hợp nhất;
Các transformer hợp nhất sự chú ý các cơ chế;
Các MLP hưởng lợi từ được hợp nhất ma trận
các phép nhân (CNNs optimize convolution+activation fusion; Transformers fuse attention mechanisms; MLPs benefit from fused matrix multiplications).
Việc xếp ô gạch cho Bộ nhớ
Tính hiệu quả (Tiling for Memory Efficiency)
Thuộc về không gian Việc xếp ô gạch (Spatial Tiling)
Thuộc về thời gian
Việc xếp ô gạch (Temporal Tiling)
Được đóng khối
Việc xếp ô gạch (Blocked Tiling)
Các CNN xếp ô gạch dọc theo thuộc về không gian các chiều hướng;
Các transformer sử dụng vòng lặp sự đóng khối để cải thiện
chuỗi bộ nhớ tính hiệu quả; Các MLP sử dụng
được đóng khối việc xếp ô gạch cho lớn ma trận các phép nhân (CNNs tile along spatial dimensions; Transformers use loop blocking to improve sequence memory efficiency; MLPs use blocked tiling for large matrix multiplications).
Với ánh xạ các chiến lược được tóm tắt trong bảng 11.22, chúng ta bây giờ kiểm tra tại sao mỗi kiến trúc
ánh xạ cách nó làm (With the mapping strategies summarized in table 11.22, we now examine why each architecture maps the way it does). Bảng nắm bắt cụ thể chiến lược các sự lựa chọn; tiếp theo các tiểu phần
giải thích kiến trúc sự thấu hiểu đằng sau mỗi cái (The table captures the specific strategy choices; the following subsections explain the architectural insight behind each one).

620
11.8 Dữ liệu luồng Sự tối ưu hóa (Dataflow Optimization)
38
GEMM (Tổng quát Ma trận
Phép nhân (General Matrix Multiplication)): Hoạt
động 𝐶 = 𝛼𝐴𝐵 + 𝛽𝐶 là
dày đặc tuyến tính-đại số nguyên thủy
thứ mà
nhiều
sâu-học tập
các lớp hạ thấp tới (The operation 𝐶= 𝛼𝐴𝐵+ 𝛽𝐶 is the dense linear-algebra primitive that many deep-learning layers lower to).
Được tối ưu hóa
GEMM
các thư viện
chẳng hạn
như
cuBLAS và oneDNN sử dụng
thanh ghi
sự đóng khối,
sự vector
hóa,
và
phân cấp
việc xếp ô gạch để tiếp cận phần cứng
các giới hạn trên thuận lợi các hình dạng
(NVIDIA 2024a;
Intel Cor-
poration 2021b) (Optimized GEMM libraries such as cuBLAS and oneDNN use register blocking, vectorization, and hierarchical tiling to approach hardware limits on favorable shapes (NVIDIA 2024a; Intel Corporation 2021b)).
Hiện đại
AI các máy gia tốc là nặng nề
được chuyên biệt hóa cho giống-GEMM
các ô gạch:
tensor các lõi, tâm thu
các mảng, và ma trận các tiện ích mở rộng
tất cả tồn tại để gia tốc này
nguyên thủy,
thứ mà
là
tại sao
GEMM
hiệu suất
là
một quan trọng chỉ báo của
đầu-cuối thông lượng qua
các kiến trúc (Modern AI accelerators are heavily specialized for GEMM-like tiles: tensor cores, systolic arrays, and matrix extensions all exist to accelerate this primitive, which is why GEMM performance is an important predictor of end-to-end throughput across architectures).
11.8.2.1 Tích chập thần kinh các mạng (ResNet-50) (Convolutional neural networks (ResNet-50))
Cho ResNet-50 và tương tự các CNN, định nghĩa đặc trưng từ một phần cứng ánh xạ góc nhìn
là thuộc về không gian trọng số sự tái sử dụng (For ResNet-50 and similar CNNs, the defining characteristic from a hardware mapping perspective is spatial weight reuse). Một đơn nhỏ bộ lọc là được áp dụng tới mọi thuộc về không gian vị trí trong đầu vào đặc trưng
bản đồ, việc có nghĩa cùng các trọng số tham gia trong hàng trăm hoặc hàng ngàn của nhân-tích lũy
các hoạt động trước khi tiếp theo bộ lọc là được cần (A single small filter is applied to every spatial location in the input feature map, meaning the same weights participate in hundreds or thousands of multiply-accumulate operations before the next filter is needed). Này sự tái sử dụng mẫu làm cho trọng số tính cố định sự thực thi
tự nhiên sự lựa chọn: việc ghim bộ lọc các trọng số trong nhanh trên-chip bộ nhớ và việc truyền phát các sự kích hoạt thông qua
tính toán các đơn vị tránh một cách lặp lại việc lấy cùng các trọng số từ chậm hơn bên ngoài bộ nhớ (This reuse pattern makes weight stationary execution the natural choice: pinning filter weights in fast on-chip memory and streaming activations through the compute units avoids repeatedly fetching the same weights from slower external memory).
Kết quả là cao số học cường độ với khiêm tốn băng thông nhu cầu, thứ mà là chính xác hồ sơ
thứ mà tensor các lõi và tâm thu các mảng là được thiết kế để khai thác (The result is high arithmetic intensity with modest bandwidth demand, which is precisely the profile that tensor cores and systolic arrays are designed to exploit).
Này thuộc về không gian tính đều đặn cũng kích hoạt tích cực sự hợp nhất và việc xếp ô gạch (This spatial regularity also enables aggressive fusion and tiling). Bởi vì tích chập, lô
chuẩn hóa, và sự kích hoạt là được áp dụng tại mọi thuộc về không gian vị trí trong khóa cứng (lockstep), các trình biên dịch có thể hợp nhất
chuỗi thành các hạt nhân thứ mà tránh không cần thiết trung gian các lượt ghi (Because convolution, batch normalization, and activation are applied at every spatial position in lockstep, compilers can fuse the sequence into kernels that avoid unnecessary intermediate writes). Thuộc về không gian việc xếp ô gạch sau đó phân vùng
đặc trưng bản đồ thành các vùng con được định kích thước để vừa vặn bên trong trên-chip SRAM, vì vậy được hợp nhất hạt nhân xử lý mỗi ô gạch
hoàn toàn từ nhanh bộ nhớ trước khi việc di chuyển tới tiếp theo cái (Spatial tiling then partitions the feature map into subregions sized to fit within on-chip SRAM, so the fused kernel processes each tile entirely from fast memory before moving to the next). Sự kết hợp của trọng số tính cố định, hạt nhân
sự hợp nhất, và thuộc về không gian việc xếp ô gạch là cái gì làm cho các CNN nằm trong số nhất thân thiện-với-phần cứng các kiến trúc (The combination of weight stationarity, kernel fusion, and spatial tiling is what makes CNNs among the most hardware-friendly architectures).
11.8.2.2 Transformer các kiến trúc (GPT-2/Llama) (Transformer architectures (GPT-2/Llama))
Nơi các CNN là được định nghĩa bởi trọng số sự tái sử dụng, các transformer là được định nghĩa bởi bộ nhớ áp lực của
khóa-giá trị (KV) bộ nhớ cache (Where CNNs are defined by weight reuse, transformers are defined by the memory pressure of the key-value (KV) cache). Trong suốt sự chú ý sự tính toán, mọi truy vấn vector phải truy cập được lưu trữ khóa và
giá trị các cặp qua toàn bộ chuỗi độ dài (During attention computation, every query vector must access stored key and value pairs across the entire sequence length). Như các chuỗi phát triển, đầy đủ KV bộ nhớ cache thường sống trong
HBM hoặc thiết bị DRAM, trong khi sự chú ý các hạt nhân xếp ô gạch hoạt động các khối thông qua SRAM, các thanh ghi, hoặc được chia sẻ
bộ nhớ (As sequences grow, the full KV cache usually lives in HBM or device DRAM, while attention kernels tile active blocks through SRAM, registers, or shared memory). Này truy cập mẫu thúc đẩy sự kích hoạt tính cố định sự thực thi: giữ hiện tại được sử dụng KV
các ô gạch gần tới tính toán trong khi việc truyền phát các truy vấn thông qua chúng, thay vì một cách lặp lại việc vật chất hóa
lớn sự chú ý các phần trung gian trong bên ngoài bộ nhớ (This access pattern motivates activation stationary execution: keep the currently used KV tiles close to compute while streaming queries through them, rather than repeatedly materializing large attention intermediates in external memory).
Bị ràng buộc-bởi-bộ nhớ bản chất của sự chú ý cũng giải thích tại sao được hợp nhất sự chú ý các hạt nhân, chẳng hạn như FlashAt-
tention (T. Dao et al. 2022), phân phối ngoại cỡ hiệu suất các phần thu về cho các transformer (The memory-bound nature of attention also explains why fused attention kernels, such as FlashAttention (T. Dao et al. 2022), deliver outsized performance gains for transformers). Bằng cách việc hợp nhất
truy vấn-khóa vô hướng tích (dot product), softmax sự chuẩn hóa, và được đánh trọng số-giá trị sự tính tổng thành một đơn hạt nhân
thứ mà xếp ô gạch dọc theo chuỗi chiều hướng, những các sự triển khai này tránh việc vật chất hóa đầy đủ sự chú ý
ma trận trong chính bộ nhớ (By fusing the query-key dot product, softmax normalization, and value-weighted summation into a single kernel that tiles along the sequence dimension, these implementations avoid materializing the full attention matrix in main memory). Này thuộc về thời gian việc xếp ô gạch cách tiếp cận xử lý chuỗi các khối thứ mà vừa vặn bên trong trên-
chip SRAM, một cách đáng kể việc làm giảm HBM lưu lượng trong khi việc bảo tồn 𝒪(𝑆2) sự chú ý sự tính toán (This temporal tiling approach processes sequence blocks that fit within on-chip SRAM, substantially reducing HBM traffic while preserving the 𝒪(𝑆2) attention computation).
Cho các transformer, ánh xạ chiến lược là chủ yếu một bài tập trong bộ nhớ sự quản lý thay vì
tính toán việc lập lịch trình (For transformers, the mapping strategy is primarily an exercise in memory management rather than compute scheduling).
11.8.2.3 Đa lớp perceptron (DLRM) (Multilayer perceptrons (DLRM))
Các MLP trình bày nhất thẳng thắn ánh xạ bài toán bởi vì của chúng sự tính toán rút gọn
phần lớn tới dày đặc Tổng quát Ma trận Phép nhân (GEMM)38 (MLPs present the most straightforward mapping problem because their computation reduces largely to dense General Matrix Multiplication (GEMM)38). Mỗi được kết nối đầy đủ lớp nhân
một sự kích hoạt ma trận bởi một trọng số ma trận (Each fully connected layer multiplies an activation matrix by a weight matrix). Trọng số ma trận là được cố định qua tất cả các mẫu trong một lô,
vì vậy trọng số tính cố định sự thực thi cho phép máy gia tốc để tải các trọng số một lần và tái sử dụng chúng qua
mọi lô phần tử, với sự tái sử dụng việc thay đổi tỷ lệ một cách tuyến tính với lô kích thước (so weight stationary execution allows the accelerator to load weights once and reuse them across every batch element, with reuse scaling linearly with batch size). Điều này làm cho các MLP cao độ nhạy cảm
tới việc phân lô: một lô kích thước của một để trọng số ma trận được sử dụng dưới mức, trong khi lớn các lô đẩy
số học cường độ vào bị ràng buộc-bởi-tính toán chế độ nơi các máy gia tốc hoạt động hiệu quả nhất (This makes MLPs highly sensitive to batching: a batch size of one leaves the weight matrix underutilized, while large batches push arithmetic intensity into the compute-bound regime where accelerators operate most efficiently).
Phần C.1.4 dẫn xuất tuyến tính tỷ lệ thứ mà chi phối này độ nhạy cảm, việc cho thấy rằng một vuông GEMM
trong FP16 đạt tới một số học cường độ của chỉ 𝑛/3 FLOP/byte, vì vậy một nhỏ 64×64 phép nhân rơi xa
bên dưới máy gia tốc của điểm đỉnh (ridge point) (Section C.1.4 derives the linear scaling that governs this sensitivity, showing that a square GEMM in FP16 reaches an arithmetic intensity of only 𝑛/3 FLOP/byte, so a small 64×64 multiply falls far below the accelerator’s ridge point).
Bởi vì MLP các lớp là điển hình được theo sau bởi sự kích hoạt các hàm và độ chệch các phép cộng, GEMM
sự hợp nhất kết hợp những các bước này thành một đơn hạt nhân, việc tránh trung gian bộ nhớ các lượt ghi (Because MLP layers are typically followed by activation functions and bias additions, GEMM fusion combines these steps into a single kernel, avoiding intermediate memory writes). Được đóng khối việc xếp ô gạch
phân vùng lớn ma trận các phép nhân thành các khối con được định kích thước cho máy gia tốc của được chia sẻ bộ nhớ,
việc đảm bảo cao bộ nhớ cache sự sử dụng xuyên suốt sự tính toán (Blocked tiling partitions the large matrix multiplications into sub-blocks sized for the accelerator’s shared memory, ensuring high cache utilization throughout computation). Sự đơn giản của MLP ánh xạ,
bị thống trị bởi một đơn nguyên thủy với có thể dự đoán truy cập các mẫu, là chính xác tại sao phần cứng các nhà cung cấp
tối ưu hóa GEMM các thư viện tích cực như vậy: các phần thu về trong GEMM hiệu suất dịch một cách trực tiếp tới MLP
thông lượng (The simplicity of the MLP mapping, dominated by a single primitive with predictable access patterns, is precisely why hardware vendors optimize GEMM libraries so aggressively: gains in GEMM performance translate directly to MLP throughput).
11.8.3 Lai tạp ánh xạ các chiến lược (Hybrid mapping strategies)
Trước đó các tiểu phần đối xử mỗi kiến trúc trong sự cô lập, nhưng thực các mô hình hiếm khi bao gồm của
một đơn lớp loại (The preceding subsections treat each architecture in isolation, but real models rarely consist of a single layer type). Một thị giác transformer, cho ví dụ, kết hợp một bản vá (patch) việc nhúng giai đoạn, tự-
sự chú ý các lớp, và MLP các khối (Dosovitskiy et al. 2021) (A vision transformer, for example, combines a patch embedding stage, self-attention layers, and MLP blocks (Dosovitskiy et al. 2021)). Những các lớp đó tạo ra khác nhau sự tái sử dụng

11. Phần cứng Sự gia tốc (Hardware Acceleration)
621
các mẫu: việc nhúng giai đoạn có thể hưởng lợi từ trọng số-tính cố định ánh xạ, sự chú ý nhấn mạnh
sự kích hoạt sự di chuyển và việc xếp ô gạch, và MLP các khối đòi hỏi được đóng khối GEMM việc xếp ô gạch và sự hợp nhất (patterns: the embedding stage can benefit from weight-stationary mapping, attention emphasizes activation movement and tiling, and MLP blocks demand blocked GEMM tiling and fusion). Không
đơn dữ liệu luồng chiến lược là tối ưu qua tất cả những các lớp này, vì vậy phần cứng ánh xạ trở thành lai tạp
và cụ thể-lớp (No single dataflow strategy is optimal across all these layers, so hardware mapping becomes hybrid and layer-specific).
Lai tạp ánh xạ giải quyết này tính không đồng nhất bằng cách việc cho phép máy gia tốc để chuyển đổi các chiến lược
tại lớp các ranh giới (Hybrid mapping addresses this heterogeneity by allowing the accelerator to switch strategies at layer boundaries). Mỗi lớp trình bày một khác nhau sự cân bằng của tính toán cường độ, dữ liệu sự tái sử dụng, và
bộ nhớ truy cập mẫu, và tối ưu ánh xạ phải chuyển đổi một cách tương ứng (Sze et al. 2017) (Each layer presents a different balance of compute intensity, data reuse, and memory access pattern, and the optimal mapping must shift accordingly (Sze et al. 2017)). Thay
vì việc cam kết tới một dữ liệu luồng cho toàn bộ mô hình, lai tạp các cách tiếp cận chọn trọng số tính cố định
sự thực thi cho các lớp với cao trọng số sự tái sử dụng, sự kích hoạt tính cố định sự thực thi cho sự chú ý các lớp với
lớn KV các bộ nhớ cache, và đầu ra tính cố định sự thực thi cho các lớp nơi việc tối thiểu hóa ghi lưu lượng quan trọng
nhất (Rather than committing to one dataflow for the entire model, hybrid approaches select weight stationary execution for layers with high weight reuse, activation stationary execution for attention layers with large KV caches, and output stationary execution for layers where minimizing write traffic matters most).
Hiện đại các máy gia tốc cung cấp kiến trúc các đặc trưng được cần để nhận ra lai tạp ánh xạ trong
thực tế (Modern accelerators provide the architectural features needed to realize hybrid mapping in practice). Kiểu-TPU tâm thu các mảng, NVIDIA các GPU, và dựa trên-ô gạch máy gia tốc các thiết kế phơi bày khác nhau
các sự kết hợp của cục bộ bộ nhớ, tensor các bố cục, sự hợp nhất, và việc lập lịch trình các kiểm soát, việc cho phép các trình biên dịch
và các thời gian chạy để chọn cụ thể-lớp các chiến lược thay vì một toàn cầu dữ liệu luồng cho toàn bộ mô hình
(Jouppi et al. 2023; NVIDIA Corporation 2020; Chen et al. 2018) (TPU-style systolic arrays, NVIDIA GPUs, and tile-based accelerator designs expose different combinations of local memory, tensor layouts, fusion, and scheduling controls, allowing compilers and runtimes to choose layer-specific strategies rather than one global dataflow for the whole model (Jouppi et al. 2023; NVIDIA Corporation 2020; Chen et al. 2018)). Những các sự triển khai này yêu cầu
có thể lập trình bộ nhớ các hệ thống phân cấp, hiệu quả các kết nối (interconnects), và được chuyên biệt hóa sự thực thi các đường ống,
việc củng cố phần cứng-phần mềm đồng-thiết kế nguyên tắc (These implementations require programmable memory hierarchies, efficient interconnects, and specialized execution pipelines, reinforcing the hardware-software co-design principle).
Tuy nhiên, lai tạp ánh xạ duy trì một thời gian-thiết kế sự tối ưu hóa (However, hybrid mapping remains a design-time optimization). Trong sản xuất các khối lượng công việc, sự thực thi
các điều kiện thay đổi một cách động do việc thay đổi đầu vào các kích thước, bộ nhớ sự tranh chấp, và phần cứng
tài nguyên tính sẵn có (In production workloads, execution conditions change dynamically due to varying input sizes, memory contention, and hardware resource availability). Máy học các trình biên dịch và thời gian chạy các hệ thống mở rộng những tĩnh ánh xạ
các sự lựa chọn này bằng cách việc giới thiệu động việc lập lịch trình, bộ nhớ các sự tối ưu hóa, và tự động việc điều chỉnh, việc đảm
bảo rằng sâu học tập các khối lượng công việc hoạt động một cách hiệu quả qua đa dạng các máy gia tốc và sự triển khai
các môi trường (Machine learning compilers and runtime systems extend these static mapping choices by introducing dynamic scheduling, memory optimizations, and automatic tuning, ensuring that deep learning workloads operate efficiently across diverse accelerators and deployment environments).
Ánh xạ các chiến lược và dữ liệu luồng các sự tối ưu hóa được kiểm tra trong trước đó các phần đại diện cho
"cái gì" của hiệu quả sự thực thi: cái nào dữ liệu để giữ cục bộ, cách nào để xếp ô gạch các sự tính toán, và cái nào
sự song song hóa các chiến lược để tuyển dụng (The mapping strategies and dataflow optimizations examined in preceding sections represent the “what” of efficient execution: which data to keep local, how to tile computations, and which parallelization strategies to employ). Việc xác định tối ưu các cấu hình cho cụ thể phần cứng và
các khối lượng công việc, tuy nhiên, yêu cầu có hệ thống sự tự động hóa (Determining optimal configurations for specific hardware and workloads, however, requires systematic automation). Máy học các trình biên dịch giải quyết này
khoảng trống bằng cách việc biến đổi trừu tượng ánh xạ các nguyên tắc thành cụ thể sự thực thi các kế hoạch được điều chỉnh tới mục tiêu
các máy gia tốc (Machine learning compilers address this gap by transforming abstract mapping principles into concrete execution plans tailored to target accelerators).
11.9 Trình biên dịch Sự hỗ trợ (Compiler Support)
Máy học các trình biên dịch tự động hóa sự dịch thuật của dữ liệu luồng các chiến lược thành có thể thực thi mã, việc giải
quyết một tới hạn thách thức: ánh xạ các quyết định được phân tích sớm hơn phải được khởi tạo một cách khác nhau
cho mỗi phần cứng mục tiêu (Machine learning compilers automate the translation of dataflow strategies into executable code, addressing a critical challenge: the mapping decisions analyzed earlier must be instantiated differently for each hardware target). Khoảng trống giữa "việc biết cái gì các sự tối ưu hóa tồn tại" và "việc áp dụng chúng
một cách chýnh xác" là rộng lớn: một đơn tích chập có thể được triển khai với hàng tá của hợp lệ việc xếp ô gạch các chiến lược,
hạt nhân các biến thể, và bộ nhớ các bố cục, hầu hết của cái mà biểu diễn kém trên bất kỳ cho trước phần cứng (The gap between “knowing what optimizations exist” and “applying them correctly” is vast: a single convolution can be implemented with dozens of valid tiling strategies, kernel variants, and memory layouts, most of which perform poorly on any given hardware). Các trình biên
dịch điều hướng này độ phức tạp một cách có hệ thống (Compilers navigate this complexity systematically). Việc biên dịch ResNet-50 cho GPU suy luận làm ví dụ cho
quá trình (Compiling ResNet-50 for GPU inference exemplifies the process):
1. Đồ thị sự tối ưu hóa hợp nhất được lặp lại Conv2D-BatchNorm-ReLU các mẫu thành ít hơn các hạt nhân,
việc loại bỏ trung gian các lượt ghi thứ mà sẽ nếu không tiêu thụ băng thông (Graph optimization fuses repeated Conv2D-BatchNorm-ReLU patterns into fewer kernels, eliminating intermediate writes that would otherwise consume bandwidth)
2. Hạt nhân sự lựa chọn chọn Tensor Lõi các sự triển khai cho tương thích các tích chập, việc khai thác
cao số học cường độ được tính toán trong Roofline phân tích (Kernel selection chooses Tensor Core implementations for compatible convolutions, exploiting the high arithmetic intensity calculated in the Roofline analysis)
3. Bộ nhớ việc lập kế hoạch xác định liệu trung gian các sự kích hoạt vừa vặn trong máy gia tốc bộ nhớ
và liệu các bộ đệm có thể được tái sử dụng một cách an toàn (Memory planning determines whether intermediate activations fit in accelerator memory and whether buffers can be reused safely)
4. Sự tính toán việc lập lịch trình chồng chéo bộ nhớ các sự truyền tải với sự tính toán khi các sự phụ thuộc
cho phép, việc ẩn phần của truyền tải độ trễ (Computation scheduling overlaps memory transfers with computation when dependencies allow, hiding part of the transfer latency)
Trong được làm việc ví dụ, suy luận thời gian giảm từ xấp xỉ 47 ms (ngây thơ sự thực thi) tới
xấp xỉ 8 ms (được tối ưu hóa), đại khái một 5.9× sự cải thiện từ sự biên dịch một mình, trước bất kỳ
thuật toán các sự thay đổi tới mô hình (In the worked example, inference time drops from approximately 47 ms (naive execution) to approximately 8 ms (optimized), roughly a 5.9× improvement from compilation alone, before any algorithmic changes to the model). Các giá trị là mang tính minh họa, nhưng cơ chế là cùng
một cái được sử dụng bởi sản xuất trình biên dịch và suy luận các ngăn xếp: đồ thị các lượt viết lại, hạt nhân sự lựa chọn, bộ nhớ
việc lập kế hoạch, và việc lập lịch trình dịch dữ liệu luồng các chiến lược chẳng hạn như sự hợp nhất (phần 11.8.1.3) và việc xếp ô gạch
(phần 11.8.1.4) thành thực hiệu suất (Chen et al. 2018; NVIDIA 2024c) (The values are illustrative, but the mechanism is the same one used by production compiler and inference stacks: graph rewrites, kernel selection, memory planning, and scheduling translate dataflow strategies such as fusion (section 11.8.1.3) and tiling (section 11.8.1.4) into real performance (Chen et al. 2018; NVIDIA 2024c)).

622
11.9 Trình biên dịch Sự hỗ trợ (Compiler Support)
Này quá trình làm ví dụ cho phần cứng-phần mềm đồng-thiết kế nguyên tắc được thiết lập trong phần 11.1,
nơi máy học các trình biên dịch kết nối mức-cao mô hình các sự đại diện với mức-thấp phần cứng
sự thực thi (This process exemplifies the hardware-software co-design principle established in section 11.1, where machine learning compilers bridge high-level model representations with low-level hardware execution). Trình biên dịch tối ưu hóa các mô hình bằng cách việc tái cấu trúc các sự tính toán, việc chọn hiệu quả sự thực
thi các hạt nhân, và việc tối đa hóa phần cứng sự sử dụng (Chen et al. 2018) (The compiler optimizes models by restructuring computations, selecting efficient execution kernels, and maximizing hardware utilization (Chen et al. 2018)). Không giống như truyền thống các trình biên dịch
được thiết kế cho tổng quát-mục đích tính toán, ML các khối lượng công việc yêu cầu được chuyên biệt hóa các cách tiếp cận cho tensor
các sự tính toán và song song sự thực thi (Unlike traditional compilers designed for general-purpose computing, ML workloads require specialized approaches for tensor computations and parallel execution).
11.9.1 ML trình biên dịch thiết kế (ML compiler design)
Máy học các trình biên dịch khác biệt từ truyền thống các trình biên dịch bởi vì ML các khối lượng công việc là được biểu diễn
như tính toán các đồ thị thứ mà mô tả quy mô-lớn tensor các hoạt động thay vì chủ yếu tuần tự
hoặc đa-luồng chương trình luồng (Machine learning compilers differ from traditional compilers because ML workloads are expressed as computation graphs that describe large-scale tensor operations rather than primarily sequential or multi-threaded program flow). Những các đồ thị này yêu cầu được chuyên biệt hóa các sự tối ưu hóa thứ mà truyền thống
các trình biên dịch không thể một cách hiệu quả áp dụng (Li et al. 2021) (These graphs require specialized optimizations that traditional compilers cannot efficiently apply (Li et al. 2021)).
Sự khác biệt là không chỉ định lượng (nhiều tính song song hơn) mà định tính: nơi truyền thống
các trình biên dịch tối ưu hóa cá nhân các lệnh bên trong tuần tự kiểm soát luồng, ML các trình biên dịch tối ưu hóa
toàn bộ dữ liệu luồng các đồ thị trong đó thống trị chi phí là dữ liệu sự di chuyển thay vì sự tính toán (The distinction is not merely quantitative (more parallelism) but qualitative: where traditional compilers optimize individual instructions within sequential control flow, ML compilers optimize entire dataflow graphs in which the dominant cost is data movement rather than computation).
Bảng 11.23 làm nổi bật này sự phân kỳ qua đầu vào sự đại diện, sự thực thi mô hình, sự tối ưu hóa
các ưu tiên, và sự biên dịch đầu ra—chú ý cách nào mọi hàng phản ánh sự chuyển đổi từ lấy-lệnh-làm-trung tâm
tới lấy-dữ-liệu-sự di chuyển-làm-trung tâm sự tối ưu hóa (Table 11.23 highlights this divergence across input representation, execution model, optimization priorities, and compilation output—notice how every row reflects the shift from instruction-centric to data-movement-centric optimization).
Bảng 11.23: Trình biên dịch Sự tối ưu hóa Các ưu tiên: Truyền thống và máy học các trình biên dịch phân kỳ trong của chúng sự tối ưu hóa
các mục tiêu: truyền thống các trình biên dịch ưu tiên hiệu quả sự thực thi của tuần tự mã, trong khi ML các trình biên dịch tập trung trên việc tối ưu hóa tensor
các hoạt động bên trong tính toán các đồ thị cho được chuyên biệt hóa phần cứng (Table 11.23: Compiler Optimization Priorities: Traditional and machine learning compilers diverge in their optimization targets: traditional compilers prioritize efficient execution of sequential code, while ML compilers focus on optimizing tensor operations within computation graphs for specialized hardware). ML các trình biên dịch kết hợp cụ thể-miền các sự biến đổi
chẳng hạn như hạt nhân sự hợp nhất và nhận thức-bộ nhớ việc lập lịch trình, không giống như lệnh việc lập lịch trình và thanh ghi sự phân bổ các kỹ thuật được sử dụng
trong thông thường sự biên dịch (ML compilers incorporate domain-specific transformations such as kernel fusion and memory-aware scheduling, unlike the instruction scheduling and register allocation techniques used in conventional compilation).
Khía cạnh (Aspect)
Truyền thống Trình biên dịch (Traditional Compiler)
Máy Học Trình biên dịch (Machine Learning Compiler)
Đầu vào Sự đại diện (Input Representation)
Tuyến tính chương trình mã (C, Python) (Linear program code (C, Python))
Tính toán đồ thị (ML các mô hình) (Computational graph (ML models))
Sự thực thi Mô hình (Execution Model)
Tuần tự hoặc đa-luồng sự thực thi (Sequential or multi-threaded execution)
Một cách ồ ạt song song dựa trên-tensor sự thực thi (Massively parallel tensor-based execution)
Sự tối ưu hóa Các ưu tiên (Optimization Priorities)
Lệnh việc lập lịch trình, vòng lặp sự mở ra (unrolling), thanh ghi
sự phân bổ (Instruction scheduling, loop unrolling, register allocation)
Đồ thị các sự biến đổi, hạt nhân sự hợp nhất,
nhận thức-bộ nhớ sự thực thi (Graph transformations, kernel fusion, memory-aware execution)
Bộ nhớ Sự quản lý (Memory Management)
Ngăn xếp và vùng nhớ heap (heap) bộ nhớ sự phân bổ (Stack and heap memory allocation)
Tensor bố cục các sự biến đổi, việc xếp ô gạch,
nhận thức-bộ nhớ việc lập lịch trình (Tensor layout transformations, tiling, memory-aware scheduling)
Mục tiêu Phần cứng (Target Hardware)
Các CPU (tổng quát-mục đích sự thực thi) (CPUs (general-purpose execution))
Các GPU, các TPU, và tùy chỉnh các máy gia tốc (GPUs, TPUs, and custom accelerators)
Sự biên dịch Đầu ra (Compilation Output)
Cụ thể-CPU máy mã (CPU-specific machine code)
Cụ thể-phần cứng sự thực thi kế hoạch (các hạt nhân,
bộ nhớ việc lập lịch trình) (Hardware-specific execution plan (kernels, memory scheduling))
Bảng giải thích tại sao trình biên dịch cấu hình có thể thay đổi hiệu suất thậm chí khi mô hình mã
là không thay đổi (The table explains why compiler configuration can change performance even when model code is unchanged). ML các trình biên dịch sở hữu bị ẩn lớp thứ mà ánh xạ cấp độ-đồ thị tensor các hoạt động lên
cụ thể-phần cứng các hạt nhân, các bố cục, và các lịch trình; khi đó ánh xạ là kém, mô hình để lại
số học các đơn vị nhàn rỗi hoặc di chuyển cùng các byte một cách lặp lại (ML compilers own the hidden layer that maps graph-level tensor operations onto hardware-specific kernels, layouts, and schedules; when that mapping is poor, the model leaves arithmetic units idle or moves the same bytes repeatedly).
Các hệ thống Góc nhìn 11.2 (Systems Perspective 11.2): Bị ẩn sự tối ưu hóa lớp (The hidden optimization layer)
Hầu hết các học viên không bao giờ tương tác một cách trực tiếp với ML các trình biên dịch, tuy nhiên trình biên dịch chất lượng thường xác
định liệu một mô hình đạt được một thấp hoặc cao tỷ lệ của phần cứng đỉnh hiệu suất (Most practitioners never interact directly with ML compilers, yet compiler quality often determines whether a model achieves a low or high fraction of hardware peak performance). Việc gọi
model.compile() trong Keras, torch.compile() trong PyTorch, hoặc việc triển khai thông qua TensorRT gọi
nhiều-giai đoạn sự tối ưu hóa các đường ống (Calling model.compile() in Keras, torch.compile() in PyTorch, or deploying through TensorRT invokes multi-stage optimization pipelines). Những các đường ống này thực hiện bốn bị ẩn các sự tối ưu hóa (These pipelines perform four hidden optimizations):
• Hợp nhất các hoạt động không bao giờ một cách tường minh được kết hợp bởi nhà phát triển (Conv2D + BatchNorm +
ReLU →đơn hạt nhân) (Fuse operations never explicitly combined by the developer (Conv2D + BatchNorm + ReLU →single kernel))
• Sắp xếp lại các sự tính toán để cải thiện bộ nhớ tính cục bộ (việc xếp ô gạch lớn ma trận các phép nhân) (Reorder computations to improve memory locality (tiling large matrix multiplies))
• Chọn các hạt nhân từ các thư viện việc chứa hàng trăm của được tinh chỉnh-thủ công các sự triển khai (Select kernels from libraries containing hundreds of hand-tuned implementations)
• Biến đổi tensor các bố cục giữa cái gì mô hình định nghĩa mong đợi và cái gì phần cứng
ưa thích (Transform tensor layouts between what the model definition expects and what hardware prefers)

11. Phần cứng Sự gia tốc (Hardware Acceleration)
623
Điều này quan trọng một cách thực tế: cùng mô hình định nghĩa có thể chạy một cách đáng kể nhanh hơn hoặc chậm hơn phụ
thuộc trên sự biên dịch phần phụ trợ, đồ thị sự hạ thấp, hạt nhân sự lựa chọn, và thời gian chạy cấu hình (This matters practically: the same model definition can run substantially faster or slower depending on compilation backend, graph lowering, kernel selection, and runtime configuration).
Khi hiệu suất không đáp ứng các kỳ vọng, trình biên dịch cấu hình và phần phụ trợ sự lựa chọn
là thường đầu tiên sự tối ưu hóa các đòn bẩy, việc yêu cầu không các sự thay đổi tới mô hình kiến trúc hoặc huấn luyện
thủ tục (When performance does not meet expectations, compiler configuration and backend selection are often the first optimization levers, requiring no changes to model architecture or training procedure).
11.9.2 ML sự biên dịch đường ống (ML compilation pipeline)
Máy học các mô hình, như được định nghĩa trong hiện đại các bộ khung, là ban đầu được biểu diễn trong một mức-cao
tính toán đồ thị thứ mà mô tả các hoạt động trên các tensor (Machine learning models, as defined in modern frameworks, are initially represented in a high-level computation graph that describes operations on tensors). Tuy nhiên, những các sự đại diện này là không
một cách trực tiếp có thể thực thi trên phần cứng các máy gia tốc chẳng hạn như các GPU, các TPU, và tùy chỉnh AI các chip (However, these representations are not directly executable on hardware accelerators such as GPUs, TPUs, and custom AI chips). Để đạt được
hiệu quả sự thực thi, các mô hình phải đi qua một ML sự biên dịch đường ống thứ mà biến đổi chúng thành
được tối ưu hóa sự thực thi các kế hoạch phù hợp cho mục tiêu phần cứng (Chen et al. 2018; Google 2025; Lattner et
al. 2020) (To achieve efficient execution, models must go through an ML compilation pipeline that transforms them into optimized execution plans suited for the target hardware (Chen et al. 2018; Google 2025; Lattner et al. 2020)).
Máy học sự biên dịch quy trình làm việc tiến hành thông qua năm các giai đoạn thứ mà một cách lũy tiến hạ thấp
sự trừu tượng (The machine learning compilation workflow proceeds through five stages that progressively lower abstraction). Đồ thị sự tối ưu hóa tái cấu trúc tính toán đồ thị để loại bỏ các sự không hiệu quả (Graph optimization restructures the computation graph to eliminate inefficiencies).
Hạt nhân sự lựa chọn sau đó ánh xạ mỗi hoạt động tới một cụ thể-phần cứng sự triển khai được tối ưu hóa cho
mục tiêu máy gia tốc (Kernel selection then maps each operation to a hardware-specific implementation optimized for the target accelerator). Bộ nhớ việc lập kế hoạch tối ưu hóa tensor các bố cục và truy cập các mẫu để làm giảm
băng thông sự tiêu thụ (Memory planning optimizes tensor layouts and access patterns to reduce bandwidth consumption). Sự tính toán việc lập lịch trình phân phối các khối lượng công việc qua song song xử lý
các phần tử để tối đa hóa phần cứng sự sử dụng (Computation scheduling distributes workloads across parallel processing elements to maximize hardware utilization). Cuối cùng, mã sự sinh dịch được tối ưu hóa kế hoạch
thành cụ thể-máy các lệnh cho sự thực thi (Finally, code generation translates the optimized plan into machine-specific instructions for execution).
Tại mỗi giai đoạn, trình biên dịch áp dụng các sự tối ưu hóa được phát triển trong phần 11.8: hạt nhân sự hợp nhất,
việc xếp ô gạch, dữ liệu sự di chuyển các chiến lược, và sự tính toán vị trí (At each stage, the compiler applies the optimizations developed in section 11.8: kernel fusion, tiling, data movement strategies, and computation placement). Những các sự tối ưu hóa này là một cách có hệ thống
được kết hợp vào cuối cùng sự thực thi kế hoạch, thứ mà là tại sao máy học sự gia tốc phụ thuộc cũng
nhiều trên được thúc đẩy-bởi-trình biên dịch phần mềm sự tối ưu hóa như trên phần cứng các sự cải thiện (These optimizations are systematically incorporated into the final execution plan, which is why machine learning acceleration depends as much on compiler-driven software optimization as on hardware improvements).
11.9.3 Đồ thị sự tối ưu hóa (Graph optimization)
AI các máy gia tốc cung cấp được chuyên biệt hóa phần cứng để tăng tốc sự tính toán, nhưng thô mô hình các sự đại
diện là không vốn dĩ được tối ưu hóa cho sự thực thi trên những các máy gia tốc này (AI accelerators provide specialized hardware to speed up computation, but raw model representations are not inherently optimized for execution on these accelerators). Máy học các bộ khung
định nghĩa các mô hình việc sử dụng mức-cao tính toán các đồ thị, nơi các nút đại diện cho các hoạt động (chẳng hạn như các
tích chập, ma trận các phép nhân, và các sự kích hoạt), và các cạnh định nghĩa dữ liệu các sự phụ thuộc (Machine learning frameworks define models using high-level computation graphs, where nodes represent operations (such as convolutions, matrix multiplications, and activations), and edges define data dependencies). Tuy nhiên,
nếu được thực thi như được định nghĩa, những các đồ thị này thường chứa dư thừa các hoạt động, không hiệu quả bộ nhớ truy cập
các mẫu, và dưới mức tối ưu sự thực thi các chuỗi thứ mà có thể ngăn cản phần cứng từ việc hoạt động tại đỉnh
tính hiệu quả (However, if executed as defined, these graphs often contain redundant operations, inefficient memory access patterns, and suboptimal execution sequences that can prevent the hardware from operating at peak efficiency).
Cho ví dụ, transformer tự-sự chú ý có thể tạo ra lớn trung gian điểm (score) và xác suất các ma
trận (For example, transformer self-attention can create large intermediate score and probability matrices). Một ngây thơ sự triển khai thứ mà vật chất hóa và đọc lại những các phần trung gian đó từ cao-băng thông
bộ nhớ trả quá mức bộ nhớ lưu lượng, trong khi nhận thức-IO sự chú ý các hạt nhân xếp ô gạch sự tính toán
thông qua nhanh bộ nhớ để tránh đó lưu lượng (T. Dao et al. 2022) (A naïve implementation that materializes and rereads those intermediates from high-bandwidth memory pays excessive memory traffic, while IO-aware attention kernels tile the computation through fast memory to avoid that traffic (T. Dao et al. 2022)). Tương tự, trong một CNN, việc áp dụng lô
chuẩn hóa và sự kích hoạt các hàm như tách biệt các hoạt động sau mỗi tích chập dẫn tới không cần
thiết trung gian bộ nhớ các lượt ghi, việc làm tăng bộ nhớ băng thông sự sử dụng (Similarly, in a CNN, applying batch normalization and activation functions as separate operations after each convolution leads to unnecessary intermediate memory writes, increasing memory bandwidth usage). Những các sự không hiệu quả này là
được giải quyết trong suốt đồ thị sự tối ưu hóa, nơi trình biên dịch tái cấu trúc tính toán đồ thị để
loại bỏ không cần thiết các hoạt động và cải thiện bộ nhớ tính cục bộ (Chen et al. 2018) (These inefficiencies are addressed during graph optimization, where the compiler restructures the computation graph to eliminate unnecessary operations and improve memory locality (Chen et al. 2018)).
Đồ thị sự tối ưu hóa biến đổi này mức-cao tính toán đồ thị thành một được tối ưu hóa sự thực thi
kế hoạch trước khi phần cứng ánh xạ (Graph optimization transforms this high-level computation graph into an optimized execution plan before hardware mapping). Thay vì việc yêu cầu thủ công sự tối ưu hóa, trình biên dịch một cách có hệ
thống áp dụng các sự biến đổi thứ mà cải thiện dữ liệu sự di chuyển, làm giảm dư thừa các sự tính toán,
và tái cấu trúc các hoạt động cho hiệu quả song song sự thực thi (Chen et al. 2018; Jia et al. 2019) (Rather than requiring manual optimization, the compiler systematically applies transformations that improve data movement, reduce redundant computations, and restructure operations for efficient parallel execution (Chen et al. 2018; Jia et al. 2019)). Tại này
giai đoạn, trình biên dịch làm việc tại một bất khả tri-phần cứng (hardware-agnostic) cấp độ, việc tập trung trên mức-cao sự tái cấu trúc trước khi
cụ thể-phần cứng các sự tối ưu hóa là được áp dụng trong sau đó các pha (At this stage, the compiler works at a hardware-agnostic level, focusing on high-level restructuring before hardware-specific optimizations are applied in later phases).
Đồ thị sự tối ưu hóa đầu tiên loại bỏ lưu lượng thứ mà mức-cao đồ thị sự đại diện sẽ nếu không
tạo ra (Graph optimization first removes traffic that the high-level graph representation would otherwise create). Hạt nhân sự hợp nhất hợp nhất liên tiếp các hoạt động để loại bỏ không cần thiết bộ nhớ các lượt ghi
và làm giảm số lượng của hạt nhân các lượt khởi chạy, thứ mà là đặc biệt hiệu quả trong tích chập thần kinh
các mạng nơi tích chập, lô chuẩn hóa, và sự kích hoạt các hàm xuất hiện trong được cố định các chuỗi (Kernel fusion merges consecutive operations to eliminate unnecessary memory writes and reduce the number of kernel launches, which is particularly effective in convolutional neural networks where convolution, batch normalization, and activation functions appear in fixed sequences).
Sự tính toán việc sắp xếp lại điều chỉnh sự thực thi thứ tự để cải thiện dữ liệu tính cục bộ và song song sự thực thi; trong
transformer các mô hình, này việc sắp xếp lại kích hoạt sự tái sử dụng của được lưu trữ bộ nhớ cache khóa-giá trị các cặp thay vì được lặp lại
bộ nhớ các lượt tải lại (Computation reordering adjusts execution order to improve data locality and parallel execution; in transformer models, this reordering enables reuse of cached key-value pairs rather than repeated memory reloads).

624
11.9 Trình biên dịch Sự hỗ trợ (Compiler Support)
39
Kinh nghiệm trong Hạt nhân Sự lựa
chọn (Heuristic in Kernel Selection): Một thực tế quy tắc-của-
ngón tay cái (rule-of-thumb) thứ mà tìm kiếm tốt các giải
pháp một cách nhanh chóng mà không một cách cạn
kiệt việc tìm kiếm tất cả các khả
năng (A practical rule-of-thumb that finds good solutions quickly without exhaustively searching all possibilities). AI các trình biên dịch đối mặt một theo số
mũ tìm kiếm không gian khi
việc chọn các hạt nhân: cho một đơn
GEMM hoạt động, ô gạch các kích thước,
dữ liệu các bố cục, độ chýnh xác các chế độ,
và sự hợp nhất các cơ hội tạo
ra hàng ngàn của hợp lệ các cấu
hình (AI compilers face an exponential search space when selecting kernels: for a single GEMM operation, tile sizes, data layouts, precision modes, and fusion opportunities create thousands of valid configurations). Các kinh nghiệm mã hóa
chuyên gia kiến thức về phần
cứng hành vi (cho ví dụ,
"sử dụng tensor các lõi khi ma
trận các chiều hướng là các bội số
của 16") để thực hiện nhanh các quyết định,
mặc dù chúng có thể bỏ lỡ 10–30
phần trăm của có thể đạt được hiệu
suất so với tự động điều
chỉnh (autotuning) các cách tiếp cận giống như TVM của
AutoTVM, thứ mà lập hồ sơ thực
tế phần cứng (Heuristics encode expert knowledge about hardware behavior (for example, “use tensor cores when matrix dimensions are multiples of 16”) to make fast decisions, though they can miss 10–30 percent of achievable performance compared to autotuning approaches like TVM’s AutoTVM, which profile actual hardware).
Dư thừa sự tính toán sự loại bỏ phục vụ cùng mục tiêu từ tính toán phía (Redundant computation elimination serves the same goal from the compute side). Bằng cách việc xác định
và việc xóa trùng lặp hoặc không cần thiết các hoạt động, trình biên dịch tránh được lặp lại công việc trong các mô hình
với thặng dư (residual) các kết nối nơi phổ biến các biểu thức con có thể nếu không được tính toán lại (By identifying and removing duplicate or unnecessary operations, the compiler avoids repeated work in models with residual connections where common subexpressions might otherwise be recomputed). Nhận thức-
Bộ nhớ dữ liệu luồng các sự điều chỉnh sau đó tinh chỉnh tensor các bố cục và tối ưu hóa sự di chuyển; cho ví dụ, việc xếp ô gạch
ma trận các phép nhân để đáp ứng cấu trúc các yêu cầu của tâm thu các mảng trong các TPU căn chỉnh
đồ thị với máy gia tốc của các điểm mạnh (Memory-aware dataflow adjustments then refine tensor layouts and optimize movement; for example, tiling matrix multiplications to meet the structural requirements of systolic arrays in TPUs aligns the graph with the accelerator’s strengths). Cùng nhau, những các kỹ thuật này chuẩn bị mô hình cho sự gia tốc
bằng cách việc tối thiểu hóa chi phí chung và việc cân bằng sự tính toán chống lại bộ nhớ các tài nguyên (Together, these techniques prepare the model for acceleration by minimizing overhead and balancing computation against memory resources).
Hiện đại AI các trình biên dịch triển khai những các lượt viết lại này thông qua được tự động hóa mẫu sự nhận dạng và được cấu
trúc các quy tắc, nhưng chính các trách nhiệm là cùng qua trình biên dịch các ngăn xếp: tìm kiếm có thể hợp nhất các mẫu,
chọn các bố cục thứ mà khớp mục tiêu bộ nhớ hệ thống phân cấp, và bảo tồn mô hình của toán học
ý nghĩa trong khi việc phơi bày cụ thể-phần cứng sự tối ưu hóa các cơ hội (Modern AI compilers implement these rewrites through automated pattern recognition and structured rules, but the core responsibilities are the same across compiler stacks: find fusible patterns, choose layouts that match the target memory hierarchy, and preserve the model’s mathematical meaning while exposing hardware-specific optimization opportunities). XLA, TVM, TensorRT, và
MLIR là tiêu biểu các hệ thống thứ mà nhấn mạnh khác nhau mục tiêu các sự ràng buộc, từ cấp độ-đồ thị sự hợp nhất
tới tensor-bố cục sự tìm kiếm và nhiều-giai đoạn sự hạ thấp (XLA, TVM, TensorRT, and MLIR are representative systems that emphasize different target constraints, from graph-level fusion to tensor-layout search and multi-stage lowering). Các hệ thống bài học là không phải sản phẩm danh sách; nó là
rằng trình biên dịch sự tái cấu trúc biến một bộ khung đồ thị thành một sự thực thi kế hoạch máy gia tốc có thể
duy trì (The systems lesson is not the product list; it is that compiler restructuring turns a framework graph into an execution plan the accelerator can sustain). Mà không này sự tái cấu trúc, một lớn transformer mô hình trên một biên thiết bị có thể gánh chịu quá mức
bộ nhớ các sự đình trệ; với nó, được làm giảm băng thông sự tiêu thụ và độ trễ có thể làm cho thời gian-thực suy luận
khả thi trên bị ràng buộc-tài nguyên các thiết bị (Without this restructuring, a large transformer model on an edge device may suffer excessive memory stalls; with it, reduced bandwidth consumption and latency can make real-time inference feasible on resource-constrained devices).
Với tính toán đồ thị bây giờ hoàn toàn được tối ưu hóa, tiếp theo bước trong sự biên dịch là hạt nhân sự lựa chọn,
nơi trình biên dịch xác định cái nào cụ thể-phần cứng sự triển khai để sử dụng cho mỗi hoạt động (With the computation graph now fully optimized, the next step in compilation is kernel selection, where the compiler determines which hardware-specific implementation to use for each operation).
Hạt nhân sự lựa chọn dịch được cấu trúc sự thực thi kế hoạch thành được tối ưu hóa mức-thấp các lệnh cho
mục tiêu máy gia tốc (Kernel selection translates the structured execution plan into optimized low-level instructions for the target accelerator).
11.9.4 Hạt nhân sự lựa chọn (Kernel selection)
Hạt nhân sự lựa chọn biến được tối ưu hóa đồ thị thành một phần cứng hợp đồng (Kernel selection turns the optimized graph into a hardware contract). Một hạt nhân là một được chuyên biệt hóa
sự triển khai của một tính toán hoạt động được thiết kế để chạy một cách hiệu quả trên một cụ thể phần cứng
kiến trúc (A kernel is a specialized implementation of a computational operation designed to run efficiently on a particular hardware architecture). Hầu hết các máy gia tốc, bao gồm các GPU, các TPU, và tùy chỉnh AI các chip, cung cấp nhiều
hạt nhân các sự triển khai cho cùng hoạt động, mỗi cái được tối ưu hóa cho khác nhau sự thực thi các kịch bản (Most accelerators, including GPUs, TPUs, and custom AI chips, provide multiple kernel implementations for the same operation, each optimized for different execution scenarios).
Việc chọn đúng hạt nhân xác định liệu máy gia tốc tối đa hóa tính toán thông lượng,
tránh bộ nhớ các sự đình trệ, và giữ được chuyên biệt hóa xử lý các phần tử bận rộn (Chen et al. 2018; Zheng et
al. 2020) (Choosing the right kernel determines whether the accelerator maximizes computational throughput, avoids memory stalls, and keeps specialized processing elements busy (Chen et al. 2018; Zheng et al. 2020)).
Hạt nhân sự lựa chọn xây dựng trên đồ thị sự tối ưu hóa, việc ánh xạ được cấu trúc sự thực thi kế hoạch tới
nhất hiệu quả sự triển khai có sẵn cho mỗi hoạt động (Kernel selection builds upon graph optimization, mapping the structured execution plan to the most efficient implementation available for each operation). Kém hạt nhân các sự lựa chọn có thể làm vô hiệu
các lợi ích của trước đó các sự tối ưu hóa bằng cách việc giới thiệu không cần thiết sự tính toán chi phí chung hoặc bộ nhớ
các nút thắt cổ chai (Chen et al. 2018) (Poor kernel choices can nullify the benefits of prior optimizations by introducing unnecessary computation overhead or memory bottlenecks (Chen et al. 2018)).
Trong một transformer mô hình, ma trận các phép nhân thứ mà thống trị tự-sự chú ý các sự tính toán
có thể được thực thi việc sử dụng khác nhau các chiến lược phụ thuộc trên có sẵn phần cứng (In a transformer model, the matrix multiplications that dominate self-attention computations can be executed using different strategies depending on the available hardware). Trên một CPU, một
tổng quát-mục đích ma trận phép nhân thủ tục là điển hình được tuyển dụng, việc khai thác được vector hóa sự thực thi
để cải thiện tính hiệu quả (On a CPU, a general-purpose matrix multiplication routine is typically employed, exploiting vectorized execution to improve efficiency). Trong sự đối lập, trên một GPU, trình biên dịch có thể chọn một sự triển khai thứ mà
sử dụng tensor các lõi để gia tốc ma trận các phép nhân việc sử dụng hỗn hợp-độ chýnh xác số học (In contrast, on a GPU, the compiler may select an implementation that uses tensor cores to accelerate matrix multiplications using mixed-precision arithmetic). Khi
mô hình là được triển khai trên một TPU, hoạt động có thể được ánh xạ lên một tâm thu mảng, việc đảm bảo rằng dữ liệu
chảy thông qua máy gia tốc trong một cách thức thứ mà tối đa hóa sự tái sử dụng và tối thiểu hóa ngoài-chip bộ nhớ
các truy cập (When the model is deployed on a TPU, the operation can be mapped onto a systolic array, ensuring that data flows through the accelerator in a manner that maximizes reuse and minimizes off-chip memory accesses). Cho suy luận các khối lượng công việc, một số nguyên số học hạt nhân có thể là được ưa thích hơn, vì nó thực hiện
các sự tính toán trong INT8 thay vì số thực-dấu phẩy (floating-point) độ chýnh xác, do đó việc làm giảm điện năng sự tiêu thụ
mà không một cách đáng kể việc thỏa hiệp độ chýnh xác (For inference workloads, an integer arithmetic kernel may be preferable, as it performs computations in INT8 instead of floating-point precision, thereby reducing power consumption without significantly compromising accuracy).
Trong nhiều các trường hợp, trình biên dịch của quyết định là cái nào tồn tại sự triển khai để tin tưởng thay vì
liệu để tạo ra một hạt nhân từ đầu (In many cases, the compiler’s decision is which existing implementation to trust rather than whether to generate a kernel from scratch). cuDNN và cuBLAS cung cấp được tối ưu hóa các hạt nhân cho sâu
học tập trên NVIDIA các GPU, oneDNN cung cấp được tối ưu hóa sự thực thi cho Intel các kiến trúc, ACL
(Arm Tính toán Thư viện) (Arm Compute Library) nhắm mục tiêu dựa trên-Arm các thiết bị, và Eigen và BLIS cung cấp hiệu quả dựa trên-CPU
các sự triển khai (cuDNN and cuBLAS offer optimized kernels for deep learning on NVIDIA GPUs, oneDNN provides optimized execution for Intel architectures, ACL (Arm Compute Library) targets Arm-based devices, and Eigen and BLIS provide efficient CPU-based implementations). Những các thư viện này mã hóa cụ thể-phần cứng kiến thức để trình biên dịch có thể chọn một
được tối ưu hóa trước hạt nhân thay vì việc phát minh lại một sự thực thi chiến lược cho mỗi nền tảng (These libraries encode hardware-specific knowledge so the compiler can choose a preoptimized kernel rather than reinventing an execution strategy for each platform).
AI các trình biên dịch sử dụng các kinh nghiệm39, việc lập hồ sơ, và chi phí các mô hình để quyết định trong số những các tùy chọn này (AI compilers use heuristics39, profiling, and cost models to decide among these options).
Sự lựa chọn phương pháp phụ thuộc trên bao nhiêu sự không chắc chắn trình biên dịch có thể chịu đựng trước khi sự thực thi
bắt đầu (The selection method depends on how much uncertainty the compiler can tolerate before execution begins).
Dựa trên-quy tắc sự lựa chọn áp dụng được xác định trước các kinh nghiệm dựa trên được biết phần cứng các khả năng (Rule-based selection applies predefined heuristics based on known hardware capabilities). Cho
ví dụ, XLA, trình biên dịch được sử dụng trong TensorFlow, một cách tự động chọn tensor lõi-được tối ưu hóa các hạt nhân (For instance, XLA, the compiler used in TensorFlow, automatically selects tensor core-optimized kernels)

11. Phần cứng Sự gia tốc (Hardware Acceleration)
625
cho NVIDIA các GPU khi hỗn hợp-độ chýnh xác sự thực thi là được kích hoạt (for NVIDIA GPUs when mixed-precision execution is enabled). Những được xác định trước các quy tắc này cho phép nhanh,
đáng tin cậy các quyết định mà không mở rộng sự phân tích (These predefined rules allow fast, reliable decisions without extensive analysis).
Được hướng dẫn bởi-hồ sơ (Profile-guided) sự lựa chọn trả nhiều hơn tìm kiếm chi phí để làm giảm sự không chắc chắn (Profile-guided selection pays more search cost to reduce uncertainty). TVM sử dụng AutoTVM để
đo chuẩn hạt nhân các tùy chọn một cách theo kinh nghiệm và tinh chỉnh sự thực thi các chiến lược dựa trên thực tế sự thực thi các thời gian, để
các hoạt động là được gán cho các sự triển khai thứ mà hoạt động tốt dưới thực tế sự triển khai các điều kiện (TVM uses AutoTVM to benchmark kernel options empirically and tune execution strategies based on real execution times, so operations are assigned to implementations that perform well under actual deployment conditions).
Dựa trên-chi phí mô hình (Cost model-based) sự lựa chọn ước tính sự thực thi thời gian và bộ nhớ sự tiêu thụ trước khi việc lập hồ sơ
mọi tùy chọn (Cost model-based selection estimates execution time and memory consumption before profiling every option). MLIR áp dụng này kỹ thuật để xác định hiệu quả việc xếp ô gạch và bộ nhớ truy cập các chiến lược
(Lattner et al. 2020) (MLIR applies this technique to determine effective tiling and memory access strategies (Lattner et al. 2020)). Bằng cách việc mô hình hóa cách nào ứng cử viên các hạt nhân tương tác với máy gia tốc của tính toán
các đơn vị và bộ nhớ hệ thống phân cấp, trình biên dịch có thể chọn một hạt nhân thứ mà tối thiểu hóa sự thực thi chi phí trong khi
việc tối đa hóa hiệu suất (By modeling how candidate kernels interact with the accelerator’s compute units and memory hierarchy, the compiler can select a kernel that minimizes execution cost while maximizing performance).
Nhận thức-Độ chýnh xác sự lựa chọn thêm toán học sự ràng buộc vào cùng quyết định (Precision-aware selection adds the numerical constraint to the same decision). Huấn luyện các khối lượng công việc
thường ưu tiên FP32 hoặc BF16 để duy trì mô hình độ chýnh xác, trong khi suy luận các khối lượng công việc ủng hộ FP16
hoặc INT8 để làm tăng tốc độ và làm giảm điện năng sự tiêu thụ (Training workloads often prioritize FP32 or BF16 to maintain model accuracy, whereas inference workloads favor FP16 or INT8 to increase speed and reduce power consumption). Cho ví dụ, một NVIDIA GPU việc chạy
suy luận với TensorRT có thể chọn trong số được hiệu chuẩn FP16 và INT8 công cụ (engine) các hồ sơ thứ mà được
xây dựng cho mô hình của độ chýnh xác các sự ràng buộc và đầu vào các hình dạng (For example, an NVIDIA GPU running inference with TensorRT can select among calibrated FP16 and INT8 engine profiles that were built for the model’s accuracy constraints and input shapes). Này sự đánh đổi giữa độ chýnh xác và
hiệu suất là một chính khía cạnh của hạt nhân sự lựa chọn, đặc biệt trong bị ràng buộc-tài nguyên các môi trường (This trade-off between precision and performance is a key aspect of kernel selection, especially in resource-constrained environments).
Một số các trình biên dịch mở rộng sự lựa chọn thành thích ứng sự tinh chỉnh, nơi sự thực thi các chiến lược điều chỉnh cho khối lượng công việc
và tài nguyên các điều kiện (Some compilers extend selection into adaptive tuning, where execution strategies adjust to workload and resource conditions). AutoTVM trong TVM đo lường hạt nhân hiệu suất qua các khối lượng công việc
và tinh chỉnh sự thực thi các chiến lược; TensorRT áp dụng được tối ưu hóa công cụ các hồ sơ dựa trên lô kích thước,
bộ nhớ các sự ràng buộc, và được hỗ trợ độ chýnh xác; Google của TPU trình biên dịch chuyên biệt hóa sự thực thi các kế hoạch cho
mục tiêu TPU cấu trúc (topology) và hình dạng hồ sơ (AutoTVM in TVM measures kernel performance across workloads and refines execution strategies; TensorRT applies optimized engine profiles based on batch size, memory constraints, and supported precision; Google’s TPU compiler specializes execution plans for the target TPU topology and shape profile). Các hậu quả của kém hạt nhân sự lựa chọn là đáng kể:
một transformer mô hình được gán một hạt nhân không phải-tensor-lõi cho ma trận các phép nhân có thể thực thi tại chỉ
một tỷ lệ của có thể hiệu suất, trong khi một mô hình được thiết kế cho FP32 sự thực thi có thể mất độ chýnh xác
nếu bị ép buộc lên một được tối ưu hóa-INT8 hạt nhân (The consequences of poor kernel selection are significant: a transformer model assigned a nontensor-core kernel for matrix multiplications may execute at only a fraction of possible performance, while a model designed for FP32 execution may lose accuracy if forced onto an INT8-optimized kernel). Hạt nhân sự lựa chọn là do đó cũng nhiều về toán học
tính chýnh xác như hiệu suất (Kernel selection is therefore as much about numerical correctness as performance).
Với hạt nhân sự lựa chọn hoàn tất, tiếp theo giai đoạn trong sự biên dịch bao gồm bộ nhớ việc lập kế hoạch và
sự tính toán việc lập lịch trình, nơi trình biên dịch xác định cách nào dữ liệu là được phân bổ qua bộ nhớ
hệ thống phân cấp và cách nào các hạt nhân là được khởi chạy cho sự thực thi (With kernel selection complete, the next stage in compilation involves memory planning and computation scheduling, where the compiler determines how data is allocated across the memory hierarchy and how kernels are launched for execution). Vì hạt nhân sự lựa chọn xác định cái gì để
thực thi, những tiếp theo các pha này chỉ ra khi nào và cách nào những các hoạt động đó chạy, việc đảm bảo rằng AI
các máy gia tốc hoạt động tại đỉnh tính hiệu quả (As kernel selection determines what to execute, these subsequent phases dictate when and how those operations run, ensuring that AI accelerators operate at peak efficiency).
11.9.5 Bộ nhớ việc lập kế hoạch (Memory planning)
Bộ nhớ việc lập kế hoạch pha đảm bảo rằng dữ liệu là được phân bổ và được truy cập trong một cách thứ mà tối thiểu hóa
bộ nhớ băng thông sự tiêu thụ, làm giảm độ trễ, và tối đa hóa bộ nhớ cache tính hiệu quả (Roesch et al.
2018; Chen et al. 2018) (The memory planning phase ensures that data is allocated and accessed in a way that minimizes memory bandwidth consumption, reduces latency, and maximizes cache efficiency (Roesch et al. 2018; Chen et al. 2018)). Thậm chí với nhất được tối ưu hóa sự thực thi kế hoạch, một mô hình có thể vẫn gánh chịu từ
nghiêm trọng hiệu suất sự suy thoái nếu bộ nhớ là không được quản lý một cách hiệu quả (Even with the most optimized execution plan, a model can still suffer from severe performance degradation if memory is not managed efficiently).
Máy học các khối lượng công việc là thâm dụng-bộ nhớ, việc yêu cầu thường xuyên sự di chuyển của lớn các tensor
giữa khác nhau các cấp độ của bộ nhớ hệ thống phân cấp (Machine learning workloads are memory-intensive, requiring frequent movement of large tensors between different levels of the memory hierarchy). Trình biên dịch phải xác định cách nào các tensor là
được lưu trữ, cách nào chúng là được truy cập, và cách nào trung gian các kết quả là được xử lý để ngăn cản bộ nhớ từ
việc trở thành nút thắt cổ chai (The compiler must determine how tensors are stored, how they are accessed, and how intermediate results are handled to prevent memory from becoming the bottleneck).
Bộ nhớ việc lập kế hoạch pha tối ưu hóa tensor các bố cục, bộ nhớ truy cập các mẫu, và bộ đệm sự tái sử dụng
để ngăn cản không cần thiết các sự đình trệ và bộ nhớ sự tranh chấp trong suốt sự thực thi (The memory planning phase optimizes tensor layouts, memory access patterns, and buffer reuse to prevent unnecessary stalls and memory contention during execution). Các tensor là được sắp xếp trong
các định dạng thứ mà căn chỉnh với phần cứng truy cập các mẫu, việc tối thiểu hóa định dạng các sự chuyển đổi (Tensors are arranged in formats that align with hardware access patterns, minimizing format conversions). Bộ nhớ các truy cập
là được cấu trúc để làm giảm bộ nhớ cache các sự bỏ lỡ (miss) và các sự đình trệ, việc làm thấp tổng thể băng thông sự tiêu thụ (Memory accesses are structured to reduce cache misses and stalls, lowering overall bandwidth consumption). Bộ đệm
sự tái sử dụng làm giảm dư thừa bộ nhớ các sự phân bổ bằng cách việc quản lý trung gian các kết quả để mà được hoàn tất
các bộ đệm là được thu hồi một cách nhanh chóng (Buffer reuse reduces redundant memory allocations by managing intermediate results so that completed buffers are reclaimed promptly). Cùng nhau, những các chiến lược này đảm bảo rằng dữ liệu là một cách hiệu quả được đặt và
được truy cập, việc nâng cao cả hai tính toán hiệu suất và năng lượng tính hiệu quả (Together, these strategies ensure that data is efficiently placed and accessed, enhancing both computational performance and energy efficiency).
Việc cân bằng bộ nhớ tính khả dụng, sự tái sử dụng, và truy cập tính hiệu quả qua nhiều hệ thống phân cấp các cấp độ làm cho
bộ nhớ việc lập kế hoạch một của nhất phức tạp trình biên dịch các vấn đề (Balancing memory availability, reuse, and access efficiency across multiple hierarchy levels makes memory planning one of the most complex compiler problems). AI các trình biên dịch sử dụng một vài các chiến lược
để quản lý bộ nhớ một cách hiệu quả và ngăn cản không cần thiết dữ liệu sự di chuyển (AI compilers use several strategies to manage memory effectively and prevent unnecessary data movement).
Tensor bố cục sự tối ưu hóa xác định cách nào các tensor nên được sắp xếp trong bộ nhớ để tối đa hóa
tính cục bộ và ngăn cản không cần thiết định dạng các sự chuyển đổi (Tensor layout optimization determines how tensors should be arranged in memory to maximize locality and prevent unnecessary format conversions). Như phần 11.8.1.2 đã thiết lập, khác nhau
phần cứng các máy gia tốc ủng hộ khác nhau vật lý các bố cục phụ thuộc trên phần phụ trợ hạt nhân và độ chýnh xác
chế độ (As section 11.8.1.2 established, different hardware accelerators favor different physical layouts depending on the backend kernel and precision mode). NVIDIA của cuDNN tích chập đường dẫn một cách lịch sử mong đợi NCHW cho nhiều FP32 các hạt nhân,
trong khi các kênh-cuối cùng (channels-last) NHWC bố cục căn chỉnh với Tensor Lõi bộ nhớ sự hợp nhất (coalescing) cho FP16 và

626
11.9 Trình biên dịch Sự hỗ trợ (Compiler Support)
INT8 các đường dẫn; TensorFlow/XLA có thể chọn bên trong các bố cục trong suốt sự hạ thấp cho mục tiêu phần phụ trợ (INT8 paths; TensorFlow/XLA may choose internal layouts during lowering for the target backend).
Trình biên dịch và thư viện các ngăn xếp biến đổi tensor các bố cục dựa trên hạt nhân và độ chýnh xác được chọn cho
mục tiêu phần cứng, việc đảm bảo rằng bộ nhớ các truy cập là được căn chỉnh cho tối đa tính hiệu quả (NVIDIA
Corporation 2021; Google 2025) (Compiler and library stacks transform tensor layouts based on the kernel and precision selected for the target hardware, ensuring that memory accesses are aligned for maximum efficiency (NVIDIA Corporation 2021; Google 2025)).
Bộ đệm sự phân bổ và sự tái sử dụng bổ sung cho bố cục sự tối ưu hóa: trình biên dịch tối thiểu hóa bộ nhớ
dấu chân bằng cách việc tái sử dụng trung gian lưu trữ bất cứ khi nào có thể (Buffer allocation and reuse complements layout optimization: the compiler minimizes memory footprint by reusing intermediate storage whenever possible). Sâu học tập các khối lượng công việc tạo ra
nhiều tạm thời các tensor, chẳng hạn như các sự kích hoạt và các gradient, thứ mà có thể một cách nhanh chóng áp đảo trên-chip
bộ nhớ nếu không một cách cẩn thận được quản lý (Deep learning workloads generate many temporary tensors, such as activations and gradients, which can quickly overwhelm on-chip memory if not carefully managed). Thay vì việc phân bổ mới bộ nhớ cho mỗi tensor, trình biên dịch
phân tích tính toán đồ thị để xác định các cơ hội cho bộ đệm sự tái sử dụng, việc đảm bảo rằng trung gian
các giá trị là được lưu trữ và được ghi đè một cách hiệu quả (Roesch et al. 2018) (Instead of allocating new memory for each tensor, the compiler analyzes the computation graph to identify opportunities for buffer reuse, ensuring that intermediate values are stored and overwritten efficiently (Roesch et al. 2018)).
Việc tối thiểu hóa dữ liệu sự di chuyển giữa hệ thống phân cấp các cấp độ là tương đương quan trọng (Minimizing data movement between hierarchy levels is equally critical). AI các máy gia tốc điển hình
có một sự kết hợp của cao-tốc độ trên-chip bộ nhớ (chẳng hạn như các bộ nhớ cache hoặc được chia sẻ SRAM) và lớn hơn, nhưng chậm hơn,
bên ngoài DRAM (AI accelerators typically have a mix of high-speed on-chip memory (such as caches or shared SRAM) and larger, but slower, external DRAM). Nếu tensor dữ liệu là một cách lặp lại được di chuyển giữa những bộ nhớ các cấp độ này, mô hình có thể
trở nên bị ràng buộc-bộ nhớ, việc làm giảm tính toán tính hiệu quả (If tensor data is repeatedly moved between these memory levels, the model may become memory bound, reducing computational efficiency). Để ngăn cản điều này, các trình biên dịch sử dụng việc xếp ô gạch
các chiến lược thứ mà phá vỡ lớn các sự tính toán thành nhỏ hơn, thân thiện-bộ nhớ các phần, việc cho phép sự thực thi
để vừa vặn bên trong nhanh, cục bộ bộ nhớ và việc làm giảm nhu cầu cho đắt đỏ ngoài-chip bộ nhớ các truy cập (To prevent this, compilers use tiling strategies that break large computations into smaller, memory-friendly chunks, allowing execution to fit within fast, local memory and reducing the need for costly off-chip memory accesses). Các
hậu quả của việc bỏ bê bộ nhớ việc lập kế hoạch là cụ thể: một CNN việc chạy trên một GPU có thể đạt được
cao tính toán tính hiệu quả trong lý thuyết, nhưng nếu của nó tích chập đặc trưng các bản đồ là được lưu trữ trong một
không tương thích bố cục thứ mà đòi hỏi được lặp lại định dạng các sự chuyển đổi, kết quả chi phí chung có thể phủ định
các lợi ích từ đồ thị sự tối ưu hóa và hạt nhân sự lựa chọn hoàn toàn (The consequences of neglecting memory planning are concrete: a CNN running on a GPU may achieve high computational efficiency in theory, but if its convolutional feature maps are stored in an incompatible layout that necessitates repeated format conversions, the resulting overhead can negate the gains from graph optimization and kernel selection entirely). Với bộ nhớ sự phân bổ được xác định,
trình biên dịch phải tiếp theo quyết định khi nào và nơi nào mỗi sự tính toán thực thi (With memory allocation determined, the compiler must next decide when and where each computation executes).
11.9.6 Sự tính toán việc lập lịch trình (Computation scheduling)
Với đồ thị sự tối ưu hóa được hoàn tất, các hạt nhân được chọn, và bộ nhớ việc lập kế hoạch được chốt lại, sự tính toán
việc lập lịch trình xác định sự thực thi thứ tự và tài nguyên sự gán cho mỗi hoạt động (With graph optimization completed, kernels selected, and memory planning finalized, computation scheduling determines the execution order and resource assignment for each operation). Này pha
xác định khi nào và nơi nào mỗi sự tính toán nên được thực thi, việc đảm bảo rằng các khối lượng công việc là
một cách hiệu quả được phân phối qua có sẵn xử lý các phần tử trong khi việc tránh không cần thiết các sự đình trệ và
tài nguyên sự tranh chấp (Zheng et al. 2020) (This phase determines when and where each computation should be executed, ensuring that workloads are efficiently distributed across available processing elements while avoiding unnecessary stalls and resource contention (Zheng et al. 2020)).
Mà không hiệu quả việc lập lịch trình, ồ ạt tính song song đi đến lãng phí: tính toán các đơn vị ngồi nhàn rỗi,
bộ nhớ băng thông đi đến dưới mức sử dụng, và sự thực thi tính hiệu quả suy thoái (Without effective scheduling, massive parallelism goes to waste: computational units sit idle, memory bandwidth goes underutilized, and execution efficiency degrades). Sự tính toán việc lập lịch trình
giữ xử lý các phần tử hoạt động, quản lý sự thực thi các sự phụ thuộc một cách chýnh xác, và phân phối
các khối lượng công việc qua phần cứng lịch trình không gian (Chen et al. 2018; Zheng et al. 2020) (Computation scheduling keeps processing elements active, manages execution dependencies correctly, and distributes workloads across the hardware schedule space (Chen et al. 2018; Zheng et al. 2020)).
Việc lập lịch trình pha điều phối song song sự thực thi, sự đồng bộ hóa, và tài nguyên sự phân bổ (The scheduling phase coordinates parallel execution, synchronization, and resource allocation).
Nhiệm vụ sự phân vùng (Task partitioning) phân rã các sự tính toán thành các đơn vị thứ mà có thể được phân phối trong số nhiều
tính toán các lõi (Task partitioning decomposes computations into units that can be distributed among multiple compute cores). Sự thực thi thứ tự sự tối ưu hóa (Execution order optimization) xác định chuỗi cho việc khởi chạy các hoạt động,
việc tối đa hóa phần cứng hiệu suất trong khi việc làm giảm các sự đình trệ (Execution order optimization determines the sequence for launching operations, maximizing hardware performance while reducing stalls). Tài nguyên sự phân bổ và sự đồng bộ hóa
đảm bảo rằng tính toán các lõi, bộ nhớ băng thông, và được chia sẻ các bộ nhớ cache là được sử dụng mà không sự tranh chấp (Resource allocation and synchronization ensure that compute cores, memory bandwidth, and shared caches are used without contention).
11.9.6.1 Sự triển khai trong AI các trình biên dịch (Implementation in AI compilers)
Việc lập lịch trình các chiến lược là cao phụ thuộc trên cơ sở phần cứng kiến trúc, vì khác nhau
AI các máy gia tốc có duy nhất sự thực thi các mô hình (Scheduling strategies are highly dependent on the underlying hardware architecture, since different AI accelerators have unique execution models). AI các trình biên dịch triển khai một vài các chiến lược để tối ưu hóa
việc lập lịch trình cho hiệu quả sự thực thi (AI compilers implement several strategies to optimize scheduling for efficient execution).
Nhiệm vụ sự phân vùng chia lớn tính toán các đồ thị thành nhỏ hơn các đơn vị thứ mà có thể thực thi trong song song (Task partitioning divides large computational graphs into smaller units that can execute in parallel).
Trên các GPU, điều này điển hình có nghĩa là việc ánh xạ ma trận các phép nhân và các tích chập tới hàng ngàn
của CUDA các lõi, trong khi trên các TPU, các nhiệm vụ là được phân vùng để vừa vặn bên trong tâm thu các mảng thứ mà hoạt động trên
được cấu trúc dữ liệu các luồng (Norrie et al. 2021) (On GPUs, this typically means mapping matrix multiplications and convolutions to thousands of CUDA cores, while on TPUs, tasks are partitioned to fit within systolic arrays that operate on structured data flows (Norrie et al. 2021)). Trong các CPU, sự phân vùng là thường được tập trung trên việc phá vỡ
các sự tính toán thành được vector hóa các phần thứ mà căn chỉnh với SIMD sự thực thi (In CPUs, partitioning is often focused on breaking computations into vectorized chunks that align with SIMD execution). Trong mỗi trường hợp, mục tiêu là để
giữ mọi lõi hoạt động xuyên suốt sự thực thi (In each case, the goal is to keep every core active throughout execution).
Vượt ra ngoài nhiệm vụ sự phân vùng, việc lập lịch trình bao gồm việc tối ưu hóa sự thực thi thứ tự để tối thiểu hóa các sự phụ thuộc
và tối đa hóa thông lượng (Beyond task partitioning, scheduling involves optimizing execution order to minimize dependencies and maximize throughput). Nhiều AI các mô hình bao gồm các hoạt động thứ mà có thể được tính toán
một cách độc lập (cho ví dụ, khác nhau các lô trong một lô xử lý đường ống) bên cạnh các hoạt động
thứ mà có nghiêm ngặt các sự phụ thuộc (cho ví dụ, hồi quy các lớp trong một RNN) (Many AI models include operations that can be computed independently (for example, different batches in a batch processing pipeline) alongside operations that have strict dependencies (for example, recurrent layers in an RNN)). AI các trình biên dịch phân tích những
các sự phụ thuộc này và nỗ lực để sắp xếp lại sự thực thi nơi có thể, việc làm giảm nhàn rỗi thời gian và việc cải thiện
song song tính hiệu quả (AI compilers analyze these dependencies and attempt to rearrange execution where possible, reducing idle time and improving parallel efficiency). Trong transformer sự chú ý, nhận thức-IO các hạt nhân làm cho này việc lập lịch trình vấn đề cụ thể
bằng cách việc tải các khối của các truy vấn, các khóa, và các giá trị vào nhanh bộ nhớ, việc sử dụng chúng trong khi thường trú (resident), và
việc trục xuất (evicting) chúng trong một thứ tự thứ mà làm giảm cao-băng thông-bộ nhớ lưu lượng (T. Dao et al. 2022) (In transformer attention, IO-aware kernels make this scheduling problem concrete by loading blocks of queries, keys, and values into fast memory, using them while resident, and evicting them in an order that reduces high-bandwidth-memory traffic (T. Dao et al. 2022)).

11. Phần cứng Sự gia tốc (Hardware Acceleration)
627
40
FPGA
(Trường-
Có thể lập trình Cổng Mảng) (Field-Programmable Gate Array):
"Trường-có thể lập trình"
có nghĩa là logic kết cấu là
có thể cấu hình
sau
việc sản
xuất, việc tương phản với
cố định-hàm các ASIC (Field-programmable” means the logic fabric is configurable after manufacturing, contrasting with fixed-function ASICs). Các FPGA
có thể cải thiện hiệu suất cho
nhạy cảm-độ trễ dữ liệu trung tâm
các dịch vụ
bằng cách
việc triển khai
tùy chỉnh các đường ống
được khớp
tới
một
cụ thể
khối lượng công việc
(Putnam et al.
2014) (FPGAs can improve performance for latency-sensitive data center services by implementing custom pipelines matched to a particular workload (Putnam et al. 2014)).
Này
khả năng tái cấu hình
làm cho
các FPGA hấp dẫn cho một cách nhanh chóng
việc tiến hóa
ML
các kiến trúc
nơi việc cam kết tới một ASIC
rủi ro sự lỗi thời (obsolescence), nhưng
yêu cầu
cho
phần cứng
sự mô tả các ngôn ngữ (Ver-
ilog/VHDL) và sự biên dịch
các thời gian
được đo
trong
nhiều giờ
tạo ra một năng suất rào cản
thứ mà
giới hạn
sự áp dụng
tới
các sự triển khai
nơi
các
tính hiệu quả lợi ích biện minh cho
kỹ thuật chi phí (This reconfigurability makes FPGAs attractive for rapidly evolving ML architectures where committing to an ASIC risks obsolescence, but the requirement for hardware description languages (Verilog/VHDL) and compilation times measured in hours creates a productivity barrier that limits adoption to deployments where the efficiency benefit justifies the engineering cost).
Tài nguyên sự phân bổ và sự đồng bộ hóa xác định cách nào tính toán các lõi chia sẻ bộ nhớ và phối
hợp sự thực thi (Resource allocation and synchronization determine how compute cores share memory and coordinate execution). Hiện đại AI các máy gia tốc thường hỗ trợ việc chồng chéo sự tính toán và dữ liệu các sự truyền tải,
có nghĩa là trong khi một nhiệm vụ thực thi, tiếp theo nhiệm vụ có thể bắt đầu việc tìm nạp của nó được yêu cầu dữ liệu (Modern AI accelerators often support overlapping computation and data transfers, meaning that while one task executes, the next task can begin fetching its required data). Các trình biên
dịch tận dụng của điều này bằng cách việc lập lịch trình các nhiệm vụ trong một cách thứ mà giấu đi bộ nhớ độ trễ, việc đảm bảo rằng
sự thực thi duy trì bị ràng buộc-tính toán thay vì bị ràng buộc-bộ nhớ (Chen et al. 2018) (Compilers take advantage of this by scheduling tasks in a way that hides memory latency, ensuring that execution remains compute bound rather than memory-bound (Chen et al. 2018)). Trong sản xuất
suy luận các ngăn xếp, được tối ưu hóa các thời gian chạy và được sinh ra-bởi-trình biên dịch các lịch trình phối hợp hạt nhân khởi chạy
thứ tự, luồng sự thực thi, và sự đồng bộ hóa để máy gia tốc không đình trệ giữa phụ thuộc
các hạt nhân (NVIDIA 2024c; Zheng et al. 2020) (In production inference stacks, optimized runtimes and compiler-generated schedules coordinate kernel launch order, stream execution, and synchronization so the accelerator does not stall between dependent kernels (NVIDIA 2024c; Zheng et al. 2020)). Kém việc lập lịch trình các quyết định có thể phủ định các lợi ích của
tất cả trước đó sự biên dịch các pha: một CNN với cao được tối ưu hóa các hạt nhân và hiệu quả bộ nhớ các bố cục
sẽ vẫn gánh chịu được làm giảm thông lượng nếu tính toán các đơn vị duy trì nhàn rỗi giữa hạt nhân các lượt khởi chạy, và
một transformer trên một TPU có thể hoạt động kém nếu sự chú ý các lớp là không được lập lịch trình để chồng chéo với
bộ nhớ các sự truyền tải (Poor scheduling decisions can negate the benefits of all prior compilation phases: a CNN with highly optimized kernels and efficient memory layouts will still suffer reduced throughput if compute units remain idle between kernel launches, and a transformer on a TPU may underperform if attention layers are not scheduled to overlap with memory transfers).
11.9.6.2 Mã sự sinh (Code generation)
Với việc lập lịch trình hoàn tất, cuối cùng sự biên dịch giai đoạn dịch này được tối ưu hóa sự thực thi kế hoạch
thành cụ thể-phần cứng các lệnh (With scheduling complete, the final compilation stage translates this optimized execution plan into hardware-specific instructions). Không giống như trước đó các pha, thứ mà đã yêu cầu cụ thể-AI các sự tối
ưu hóa, mã sự sinh tuân theo nhiều của cùng các nguyên tắc như truyền thống các trình biên dịch (Unlike the previous phases, which required AI-specific optimizations, code generation follows many of the same principles as traditional compilers). Này
quá trình bao gồm lệnh sự lựa chọn, thanh ghi sự phân bổ, và cuối cùng sự tối ưu hóa các lượt (passes), việc đảm bảo
rằng sự thực thi tạo ra đầy đủ sự sử dụng của cụ thể-phần cứng các đặc tính chẳng hạn như được vector hóa sự thực thi, bộ nhớ
sự tìm nạp trước, và lệnh sự sắp xếp lại (This process includes instruction selection, register allocation, and final optimization passes, ensuring that execution makes full use of hardware-specific features such as vectorized execution, memory prefetching, and instruction reordering). Một cách quan trọng, tuy nhiên, lệnh sự lựa chọn cho ML các mục tiêu là
không tổng quát: trình biên dịch phải phát ra các lệnh thứ mà tham gia phần cứng của cụ thể-ma trận ISA
các sự mở rộng (Crucially, however, instruction selection for ML targets is not generic: the compiler must emit instructions that engage the hardware’s matrix-specific ISA extensions). Trên NVIDIA các GPU, điều này có nghĩa là việc phát ra Song song Luồng Sự thực thi (Parallel Thread Execution - PTX) các lệnh
chẳng hạn như mma.sync.aligned để gọi Tensor Các lõi một cách trực tiếp, như được cho thấy trong danh sách 11.14 (On NVIDIA GPUs, this means emitting Parallel Thread Execution (PTX) instructions such as mma.sync.aligned to invoke Tensor Cores directly, as shown in listing 11.14). Trên Intel các CPU
với Tiên tiến Ma trận Các sự mở rộng (Advanced Matrix Extensions - AMX), trình biên dịch nhắm mục tiêu ô gạch-nhân các lệnh việc hoạt động
trên 2D thanh ghi các ô gạch (On Intel CPUs with Advanced Matrix Extensions (AMX), the compiler targets tile-multiply instructions operating on 2D register tiles). Trên Arm các CPU với Mở rộng Ma trận Sự mở rộng (Scalable Matrix Extension), mục tiêu là ngoài-tích (outer-product)
sự tích lũy qua có thể mở rộng ma trận các ô gạch (On Arm CPUs with the Scalable Matrix Extension, the target is outer-product accumulation across scalable matrix tiles). Một mã sự sinh phần phụ trợ thứ mà phát ra tổng quát số thực-dấu
phẩy các lệnh thay vì những các sự mở rộng này để phần cứng của chính ma trận các công cụ nhàn rỗi,
thứ mà có thể làm giảm hiệu quả thông lượng bởi một bậc của cường độ bất kể cách nào tốt sớm hơn
sự biên dịch các pha đã thực hiện (A code generation backend that emits generic floating-point instructions instead of these extensions leaves the hardware’s primary matrix engines idle, which can reduce effective throughput by an order of magnitude regardless of how well the earlier compilation phases performed). Cho các CPU và các GPU, AI các trình biên dịch điển hình sinh ra máy mã
hoặc được tối ưu hóa hợp ngữ các lệnh, trong khi cho các TPU, các FPGA40, và khác các máy gia tốc, đầu ra
có thể là được tối ưu hóa bytecode hoặc sự thực thi các đồ thị thứ mà là được thông dịch bởi phần cứng của thời gian chạy
hệ thống (For CPUs and GPUs, AI compilers typically generate machine code or optimized assembly instructions, while for TPUs, FPGAs40, and other accelerators, the output may be optimized bytecode or execution graphs that are interpreted by the hardware’s runtime system).
11.9.7 Từ sự biên dịch tới thời gian chạy (From compilation to runtime)
Trình biên dịch biến đổi mức-cao máy học các mô hình thành được tối ưu hóa sự thực thi các kế hoạch được điều chỉnh
cho được chuyên biệt hóa phần cứng, nhưng đó kế hoạch là vẫn một sự giả định về tương lai thời gian chạy các điều kiện: lô
hình dạng, có sẵn bộ nhớ, máy gia tốc sự chiếm đóng (occupancy), và cạnh tranh các khối lượng công việc (The compiler transforms high-level machine learning models into optimized execution plans tailored to specialized hardware, but that plan is still an assumption about future runtime conditions: batch shape, available memory, accelerator occupancy, and competing workloads). Đồ thị sự tối ưu hóa
tái cấu trúc sự tính toán, hạt nhân sự lựa chọn ánh xạ các hoạt động tới hiệu quả-phần cứng các sự triển khai,
bộ nhớ việc lập kế hoạch tối ưu hóa dữ liệu vị trí, và sự tính toán việc lập lịch trình đảm bảo hiệu quả song song
sự thực thi (Graph optimization restructures computation, kernel selection maps operations to hardware-efficient implementations, memory planning optimizes data placement, and computation scheduling ensures efficient parallel execution). Cùng nhau, những các pha này kích hoạt AI các mô hình để hoàn toàn sử dụng hiện đại các máy gia tốc với cao
thông lượng, tối thiểu bộ nhớ chi phí chung, và hiệu quả sự thực thi các đường ống (Together, these phases enable AI models to fully use modern accelerators with high throughput, minimal memory overhead, and efficient execution pipelines).
Tất cả trình biên dịch các sự tối ưu hóa chia sẻ một quan trọng sự hạn chế: chúng xảy ra trước khi sự thực thi bắt đầu (All compiler optimizations share a critical limitation: they occur before execution begins). Này tĩnh
bản chất là cả hai một điểm mạnh, việc kích hoạt tích cực toàn-chương trình sự tối ưu hóa, và một điểm yếu, không thể
để thích ứng khi thực tế phân kỳ từ các sự giả định (This static nature is both a strength, enabling aggressive whole-program optimization, and a weakness, unable to adapt when reality diverges from assumptions). Trình biên dịch thực hiện các quyết định dựa trên cái gì nó
mong đợi để xảy ra, không cái gì thực tế xảy ra (The compiler makes decisions based on what it expects to happen, not what actually happens). Đồ thị sự tái cấu trúc, hạt nhân sự lựa chọn, bộ nhớ việc lập kế hoạch,
và sự tính toán việc lập lịch trình tất cả sản xuất một đơn, được tối ưu hóa sự thực thi kế hoạch dựa trên các sự giả định
về lô các kích thước, dành riêng phần cứng tính khả dụng, và sạch bộ nhớ trạng thái (Graph restructuring, kernel selection, memory planning, and computation scheduling all produce a single, optimized execution plan based on assumptions about batch sizes, dedicated hardware availability, and clean memory state).
Sản xuất AI các hệ thống cư ngụ một động thế giới thứ mà hiếm khi khớp những tĩnh các sự giả định này (Production AI systems inhabit a dynamic world that rarely matches these static assumptions).
Lô các kích thước biến đổi từ một (nhạy cảm-độ trễ đơn các yêu cầu) tới 128 (định hướng-thông lượng lô
việc phục vụ) bên trong cùng sự triển khai (Batch sizes vary from one (latency-sensitive single requests) to 128 (throughput-oriented batch serving) within the same deployment). GPU bộ nhớ phân mảnh trong suốt chạy-lâu suy luận
các máy chủ, việc ép buộc dưới mức tối ưu tensor các bố cục (GPU memory fragments during long-running inference servers, forcing suboptimal tensor layouts). Nhiều các khối lượng công việc cạnh tranh cho máy gia tốc các tài nguyên
trong nhiều-người thuê (multi-tenant) đám mây các môi trường (Multiple workloads compete for accelerator resources in multi-tenant cloud environments). Nhiệt sự điều chỉnh (Thermal throttling) làm giảm được duy trì hiệu suất dưới
các đỉnh được quan sát trong ngắn các điểm chuẩn (Thermal throttling reduces sustained performance below the peaks observed in short benchmarks). Thời gian chạy hệ thống kết nối tĩnh sự tối ưu hóa và động
thực tế, một cách liên tục việc thích ứng sự thực thi cho thực tế các điều kiện thay vì được giả định các điều kiện (The runtime system bridges static optimization and dynamic reality, continuously adapting execution to actual conditions rather than assumed conditions). Các
việc phục vụ chương sau đó đối xử việc tạo lô, sự cho phép kiểm soát, và cấp độ-dịch vụ các mục tiêu như đầu-tới-đầu (The serving chapter later treats batching, admission control, and service-level objectives as end-to-end)

628
11.10 Thời gian chạy Sự hỗ trợ (Runtime Support)
hệ thống các vấn đề (Chương 13) (system problems (Chapter 13)); ở đây hẹp hơn câu hỏi là cách nào máy gia tốc thời gian chạy giữ một
mô hình sự thực thi hiệu quả một khi một yêu cầu hoặc lô chạm đến phần cứng (here the narrower question is how the accelerator runtime keeps one model execution efficient once a request or batch reaches the hardware).
11.10 Thời gian chạy Sự hỗ trợ (Runtime Support)
AI các thời gian chạy giải quyết sản xuất sự biến thiên vấn đề bằng cách việc mở rộng biên dịch-thời gian các sự tối ưu hóa với
thời gian chạy các quyết định về bộ nhớ, các hạt nhân, và sự thực thi các hồ sơ; TensorRT là một tiêu biểu
sản xuất suy luận thời gian chạy cho này vai trò (NVIDIA 2024c) (AI runtimes solve the production variability problem by extending compile-time optimizations with runtime decisions about memory, kernels, and execution profiles; TensorRT is one representative production inference runtime for this role (NVIDIA 2024c)). Không giống như truyền thống được biên dịch các chương trình
thứ mà thực thi một cố định lệnh chuỗi, AI các khối lượng công việc yêu cầu thích ứng kiểm soát trên bộ nhớ
sự phân bổ, hạt nhân sự thực thi, và tài nguyên việc lập lịch trình, một cách liên tục việc giám sát sự thực thi các điều kiện
và việc thực hiện trên-đường-bay (on-the-fly) các sự điều chỉnh để duy trì phần cứng sự sử dụng bất chấp đang thay đổi sản xuất
các điều kiện (Unlike traditional compiled programs that execute a fixed instruction sequence, AI workloads require adaptive control over memory allocation, kernel execution, and resource scheduling, continuously monitoring execution conditions and making on-the-fly adjustments to maintain hardware utilization despite changing production conditions).
AI các thời gian chạy quản lý ba liên quan lẫn nhau các khía cạnh của sự thực thi (AI runtimes manage three interrelated aspects of execution). Đầu tiên, hạt nhân sự thực thi sự quản lý (kernel execution management):
các thời gian chạy một cách động chọn và phân phối (dispatch) tính toán các hạt nhân dựa trên hiện tại hệ thống trạng thái để
tối thiểu hóa độ trễ (First, kernel execution management: runtimes dynamically select and dispatch computation kernels based on the current system state to minimize latency). Thứ hai, bộ nhớ sự thích ứng (memory adaptation): bởi vì AI các khối lượng công việc xử lý lớn các tensor với
biến đổi các dấu chân (footprints), các thời gian chạy điều chỉnh sự phân bổ một cách động để ngăn cản các nút thắt cổ chai và quá mức dữ liệu
sự di chuyển (Second, memory adaptation: because AI workloads process large tensors with varying footprints, runtimes adjust allocation dynamically to prevent bottlenecks and excessive data movement). Thứ ba, sự thực thi sự mở rộng quy mô (execution scaling): các thời gian chạy và huấn luyện các hệ thống phân phối các khối lượng công việc qua
nhiều các máy gia tốc cho nhiều-chip, nhiều-nút, hoặc đám mây các môi trường, như trong đường ống-song song
các hệ thống chẳng hạn như GPipe [việc chia tách các lớp qua các máy gia tốc; Huang et al. (2019)] và thiết bị-vị trí
các phương pháp [tự động sự gán của các hoạt động tới các thiết bị; Mirhoseini et al. (2017)] (Third, execution scaling: runtimes and training systems distribute workloads across multiple accelerators for multi-chip, multi-node, or cloud environments, as in pipeline-parallel systems such as GPipe [splitting layers across accelerators; Huang et al. (2019)] and device-placement methods [automatic assignment of operations to devices; Mirhoseini et al. (2017)]).
AI các thời gian chạy bổ sung cho dựa trên-trình biên dịch các sự tối ưu hóa bằng cách việc xử lý những sự thực thi các khía cạnh này
một cách động (AI runtimes complement compiler-based optimizations by handling these execution aspects dynamically). Việc so sánh AI các thời gian chạy với truyền thống phần mềm các thời gian chạy làm rõ tại sao máy học
các khối lượng công việc yêu cầu được chuyên biệt hóa sự thực thi các chiến lược (Comparing AI runtimes to traditional software runtimes clarifies why machine learning workloads require specialized execution strategies).
11.10.1 ML thời gian chạy kiến trúc (ML runtime architecture)
Truyền thống phần mềm các thời gian chạy là được thiết kế cho việc quản lý tổng quát-mục đích chương trình sự thực thi,
chủ yếu việc xử lý tuần tự và đa-luồng các khối lượng công việc trên các CPU (Traditional software runtimes are designed for managing general-purpose program execution, primarily handling sequential and multi-threaded workloads on CPUs). Những các thời gian chạy này phân bổ
bộ nhớ, lập lịch trình các nhiệm vụ, và tối ưu hóa sự thực thi tại cấp độ của cá nhân hàm các lượt gọi và các lệnh
(These runtimes allocate memory, schedule tasks, and optimize execution at the level of individual function calls and instructions). Trong sự đối lập, AI các thời gian chạy là được chuyên biệt hóa cho máy học các khối lượng công việc, thứ mà yêu cầu
một cách ồ ạt song song sự tính toán, quy mô-lớn tensor các hoạt động, và động bộ nhớ sự quản lý (In contrast, AI runtimes are specialized for machine learning workloads, which require massively parallel computation, large-scale tensor operations, and dynamic memory management).
Bảng 11.24 làm nổi bật chính các sự khác biệt giữa truyền thống và AI các thời gian chạy (Table 11.24 highlights the key differences between traditional and AI runtimes). Một của chính
các sự khác biệt nằm ở trong sự thực thi luồng (One of the key distinctions lies in execution flow). Truyền thống phần mềm các thời gian chạy hoạt động trên một có thể dự đoán, được cấu trúc
sự thực thi mô hình nơi hàm các lượt gọi và CPU các luồng tuân theo một được xác định trước kiểm soát đường dẫn (Traditional software runtimes operate on a predictable, structured execution model where function calls and CPU threads follow a predefined control path). AI các thời gian chạy,
tuy nhiên, thực thi tính toán các đồ thị, việc yêu cầu phức tạp việc lập lịch trình các quyết định thứ mà tính đến
các sự phụ thuộc giữa tensor các hoạt động, song song hạt nhân sự thực thi, và hiệu quả bộ nhớ truy cập (AI runtimes, however, execute computational graphs, requiring complex scheduling decisions that account for dependencies between tensor operations, parallel kernel execution, and efficient memory access).
Bảng 11.24: Thời gian chạy Sự thực thi Các mô hình: Truyền thống các thời gian chạy ưu tiên tuần tự hoặc đa-luồng lệnh sự xử lý,
trong khi AI các thời gian chạy sử dụng một cách ồ ạt song song tensor các hoạt động cho được gia tốc sự tính toán trên máy học các khối lượng công việc (Table 11.24: Runtime Execution Models: Traditional runtimes prioritize sequential or multi-threaded instruction processing, while AI runtimes use massively parallel tensor operations for accelerated computation on machine learning workloads). Này
sự phân kỳ đòi hỏi được chuyên biệt hóa AI thời gian chạy các kiến trúc được thiết kế cho hiệu quả sự song song hóa và bộ nhớ sự quản lý của
quy mô-lớn tensor dữ liệu (This divergence necessitates specialized AI runtime architectures designed for efficient parallelization and memory management of large-scale tensor data).
Khía cạnh (Aspect)
Truyền thống Thời gian chạy (Traditional Runtime)
AI Thời gian chạy (AI Runtime)
Sự thực thi Mô hình (Execution Model)
Tuần tự hoặc đa-luồng sự thực thi (Sequential or multi-threaded execution)
Một cách ồ ạt song song tensor sự thực thi (Massively parallel tensor execution)
Nhiệm vụ Việc lập lịch trình (Task Scheduling)
CPU luồng sự quản lý (CPU thread management)
Hạt nhân sự phân phối qua các máy gia tốc (Kernel dispatch across accelerators)
Bộ nhớ Sự quản lý (Memory Management)
Mịn-hạt (Fine-grained) sự phân bổ (ngăn xếp và vùng nhớ heap) (Fine-grained allocation (stack and heap))
Động tensor sự phân bổ, bộ đệm sự tái sử dụng (Dynamic tensor allocation, buffer reuse)
Sự tối ưu hóa Các ưu tiên (Optimization Priorities)
Thấp-độ trễ lệnh sự thực thi (Low-latency instruction execution)
Việc tối thiểu hóa bộ nhớ các sự đình trệ, việc tối đa hóa song song
sự thực thi (Minimizing memory stalls, maximizing parallel execution)
Khả năng thích ứng (Adaptability)
Chủ yếu tĩnh sự thực thi kế hoạch (Mostly static execution plan)
Thích ứng cho lô kích thước và phần cứng tính khả dụng (Adapts to batch size and hardware availability)
Mục tiêu Phần cứng (Target Hardware)
Các CPU (tổng quát-mục đích sự thực thi) (CPUs (general-purpose execution))
Các GPU, các TPU, và tùy chỉnh các máy gia tốc (GPUs, TPUs, and custom accelerators)
Bộ nhớ sự quản lý là một cái khác chính sự phân biệt (Memory management is another major differentiator). Truyền thống phần mềm các thời gian chạy xử lý nhỏ,
thường xuyên bộ nhớ các sự phân bổ, việc tối ưu hóa cho bộ nhớ cache tính hiệu quả và thấp-độ trễ truy cập (Traditional software runtimes handle small, frequent memory allocations, optimizing for cache efficiency and low-latency access). AI các thời gian chạy, trong
sự đối lập, phải một cách động phân bổ, tái sử dụng, và tối ưu hóa lớn các tensor, việc đảm bảo rằng bộ nhớ truy cập
các mẫu căn chỉnh với thân thiện-máy gia tốc sự thực thi (AI runtimes, in contrast, must dynamically allocate, reuse, and optimize large tensors, ensuring that memory access patterns align with accelerator-friendly execution). Kém bộ nhớ sự quản lý trong AI các khối lượng công việc
có thể dẫn tới hiệu suất các nút thắt cổ chai, đặc biệt do quá mức ngoài-chip bộ nhớ các sự truyền tải và
không hiệu quả bộ nhớ cache sự sử dụng (Poor memory management in AI workloads can lead to performance bottlenecks, particularly due to excessive off-chip memory transfers and inefficient cache usage).

11. Phần cứng Sự gia tốc (Hardware Acceleration)
629
AI các thời gian chạy là vốn dĩ được thiết kế cho khả năng thích ứng (AI runtimes are inherently designed for adaptability). Trong khi truyền thống các thời gian chạy thường tuân theo một
chủ yếu tĩnh sự thực thi kế hoạch, AI các khối lượng công việc điển hình hoạt động trong cao biến thiên sự thực thi các môi
trường, chẳng hạn như dựa trên-đám mây các máy gia tốc hoặc nhiều-người thuê phần cứng (While traditional runtimes often follow a mostly static execution plan, AI workloads typically operate in highly variable execution environments, such as cloud-based accelerators or multi-tenant hardware). Như một kết quả, AI các thời gian chạy phải
một cách liên tục điều chỉnh lô các kích thước, phân bổ lại tính toán các tài nguyên, và quản lý thời gian-thực việc lập lịch trình
các quyết định để duy trì cao thông lượng và tối thiểu hóa sự thực thi các sự chậm trễ (As a result, AI runtimes must continuously adjust batch sizes, reallocate compute resources, and manage real-time scheduling decisions to maintain high throughput and minimize execution delays). AI các thời gian chạy phải giám sát
quy mô-lớn tensor sự thực thi, nhiều-thiết bị sự phối hợp, và thời gian-thực khối lượng công việc sự thích ứng, tất cả của
chúng trở nên một cách sâu sắc có thể nhìn thấy khi các mô hình di chuyển từ sự phát triển tới sản xuất (AI runtimes must oversee large-scale tensor execution, multi-device coordination, and real-time workload adaptation, all of which become acutely visible when models move from development to production).
Sâu sắc nhất lý do một AI thời gian chạy không thể chạy một cố định kế hoạch là rằng phát triển môi trường
nói dối về sản xuất môi trường (The deepest reason an AI runtime cannot run a fixed plan is that the development environment lies about the production one). Rõ ràng nhất trường hợp là nhiệt (thermal): một mô hình được tinh chỉnh trên một ngắn điểm chuẩn
không bao giờ thấy sự điều chỉnh thứ mà một được duy trì khối lượng công việc kích hoạt, và thậm chí cùng chip là không
cùng chip (The clearest case is thermal: a model tuned on a short benchmark never sees the throttling that a sustained workload triggers, and even the same chip is not the same chip). A100 SXM hoạt động tại 400 W TDP trong khi A100 PCIe hoạt động tại 300 W; những
cái này là khác nhau hình thức các yếu tố (form factors) với khác nhau làm mát các đường bao (cooling envelopes), không phải tăng tốc (boost) so với được duy trì các trạng thái, do đó một
hạt nhân thứ mà giữ đỉnh thông lượng trong phòng thí nghiệm có thể một cách lặng lẽ mất nó trong sản xuất phụ thuộc trên cái nào
biến thể là được triển khai (The A100 SXM operates at 400 W TDP while the A100 PCIe operates at 300 W; these are different form factors with different cooling envelopes, not boost versus sustained states, so a kernel that holds peak throughput in the lab can quietly lose it in production depending on which variant is deployed). Cùng phát triển-tới-sản xuất khoảng cách xuất hiện trong lô kích thước thứ mà đu đưa
từ đơn các yêu cầu tới các đợt bùng nổ, trong chạy-lâu các máy chủ thứ mà phân mảnh GPU bộ nhớ, và trong được chia sẻ
các máy gia tốc nơi một hàng xóm khối lượng công việc đánh cắp băng thông một độ trễ mục tiêu đã phụ thuộc trên (The same development-to-production gap shows up in batch size that swings from single requests to bursts, in long-running servers that fragment GPU memory, and in shared accelerators where a neighbor workload steals the bandwidth a latency target depended on). Không
những các điều kiện này là được biết khi mô hình là được biên dịch, thứ mà là tại sao thời gian chạy, không phải trình biên dịch,
phải hấp thụ chúng (None of these conditions is known when the model is compiled, which is why the runtime, not the compiler, has to absorb them).
Để xem cách nào những thời gian chạy các cơ chế này làm việc cùng nhau trong thực tế, hãy xem xét một cụ thể kịch bản:
một transformer suy luận yêu cầu đến tại một sản xuất máy chủ (To see how these runtime mechanisms work together in practice, consider a concrete scenario: a transformer inference request arrives at a production server). Thời gian chạy phải thích ứng sự thực thi
các tham số chẳng hạn như việc xếp ô gạch và bộ nhớ sự phân bổ cho hiện tại các điều kiện (động sự thực thi), xác
định cái nào hạt nhân sự triển khai để sử dụng cho mỗi hoạt động dựa trên thời gian-thực phần cứng trạng thái
(hạt nhân sự lựa chọn), và lập lịch trình các được chọn các hạt nhân qua có sẵn tính toán các đơn vị để tối đa hóa
sự sử dụng (hạt nhân việc lập lịch trình) (The runtime must adapt execution parameters such as tiling and memory allocation to current conditions (dynamic execution), determine which kernel implementation to use for each operation based on real-time hardware state (kernel selection), and schedule the selected kernels across available compute units to maximize utilization (kernel scheduling)). Những cái này là không độc lập các hệ thống mà ba liên quan lẫn nhau các pha của
một đơn thời gian chạy đường ống, và những tiếp theo các tiểu mục kiểm tra mỗi pha việc sử dụng này transformer
suy luận yêu cầu như một đang chạy ví dụ (These are not independent systems but three interrelated phases of a single runtime pipeline, and the following subsections examine each phase using this transformer inference request as a running example).
11.10.2 Động hạt nhân sự thực thi (Dynamic kernel execution)
Trong khi tĩnh sự biên dịch cung cấp một vững chắc nền tảng, hiệu quả sự thực thi của máy học các khối lượng
công việc yêu cầu thời gian-thực sự thích ứng cho dao động các điều kiện (While static compilation provides a solid foundation, efficient execution of machine learning workloads requires real-time adaptation to fluctuating conditions). Khi của chúng ta transformer suy luận
yêu cầu đến, thời gian chạy không thể thực thi một cố định kế hoạch: có sẵn bộ nhớ, đầu vào chuỗi chiều dài,
và tính toán tải có thể khác biệt từ cái gì trình biên dịch đã giả định (When our transformer inference request arrives, the runtime cannot execute a fixed plan: available memory, input sequence length, and computational load may differ from what the compiler assumed). Thời gian chạy một cách liên tục
điều chỉnh sự thực thi các chiến lược để khớp cả hai phần cứng các sự ràng buộc và khối lượng công việc các đặc điểm (The runtime continuously adjusts execution strategies to match both hardware constraints and workload characteristics).
Cá nhân tính toán các hoạt động (ma trận các phép nhân, các tích chập, sự kích hoạt các hàm)
phải được gán cho thích hợp xử lý các đơn vị, và này ánh xạ là không được cố định (Individual computational operations (matrix multiplications, convolutions, activation functions) must be assigned to appropriate processing units, and this mapping is not fixed). Vì đầu vào dữ liệu,
bộ nhớ tính khả dụng, và hệ thống tải thay đổi trong suốt sự thực thi, thời gian chạy thực hiện thời gian-thực các quyết
định về sự thực thi thứ tự và bộ nhớ sự quản lý để giữ các khối lượng công việc hiệu quả bất chấp đang dịch chuyển
các điều kiện (As input data, memory availability, and system load change during execution, the runtime makes real-time decisions about execution order and memory management to keep workloads efficient despite shifting conditions).
Cùng sự thích ứng xuất hiện trong hình ảnh phân loại (The same adaptation appears in image classification). Nếu một đang đến lô của cao-độ phân giải
các hình ảnh yêu cầu nhiều hơn bộ nhớ hơn trình biên dịch đã giả định, một tĩnh sự thực thi kế hoạch có thể gây ra bộ nhớ cache
sự đập (thrashing) hoặc quá mức ngoài-chip bộ nhớ các truy cập (If an incoming batch of high-resolution images requires more memory than the compiler assumed, a static execution plan can cause cache thrashing or excessive off-chip memory accesses). Một động thời gian chạy có thể điều chỉnh việc xếp ô gạch các chiến lược
trong suốt sự thực thi, việc phá vỡ tensor các hoạt động thành nhỏ hơn các ô gạch thứ mà vừa vặn bên trong cao-tốc độ trên-chip
bộ nhớ (A dynamic runtime can adjust tiling strategies during execution, breaking tensor operations into smaller tiles that fit within high-speed on-chip memory). Điều này ngăn cản bộ nhớ các sự đình trệ và cải thiện bộ nhớ cache sự sử dụng (This prevents memory stalls and improves cache utilization).
Cho đang chạy transformer suy luận yêu cầu, chuỗi chiều dài có thể biến đổi giữa các lượt gọi (For the running transformer inference request, sequence length may vary between calls). Một tĩnh
sự thực thi kế hoạch được tối ưu hóa cho một được cố định chuỗi chiều dài có thể dưới mức sử dụng tính toán các tài nguyên trên
ngắn hơn các chuỗi hoặc tạo ra quá mức bộ nhớ áp lực trên dài hơn các chuỗi (A static execution plan optimized for one fixed sequence length can underutilize compute resources on shorter sequences or create excessive memory pressure on longer sequences). Động hạt nhân
sự thực thi giảm nhẹ điều này bằng cách việc chọn hạt nhân các sự triển khai dựa trên thực tế chuỗi chiều dài
và việc điều chỉnh bộ nhớ sự phân bổ để duy trì tính hiệu quả (Dynamic kernel execution mitigates this by selecting kernel implementations based on the actual sequence length and adjusting memory allocation to maintain efficiency).
Việc chồng chéo sự tính toán với bộ nhớ sự di chuyển giảm nhẹ nút thắt cổ chai thứ mà đã chi phối
chương: dữ liệu sự di chuyển giữa bộ nhớ hệ thống phân cấp các cấp độ giới hạn sự tính toán tốc độ (Overlapping computation with memory movement mitigates the bottleneck that has governed the chapter: data movement between memory hierarchy levels limits computation speed). AI các thời gian chạy
triển khai không đồng bộ sự thực thi và kép việc tạo bộ đệm (double buffering) để các sự tính toán tiến hành mà không việc chờ đợi
cho bộ nhớ các sự truyền tải để hoàn tất (AI runtimes implement asynchronous execution and double buffering so computations proceed without waiting for memory transfers to complete). Trong một quy mô-lớn mô hình, một DMA công cụ truyền tải tiếp theo lô
của dữ liệu qua máy chủ-tới-thiết bị liên kết trong khi máy gia tốc thực thi hiện tại lô, việc duy trì
một ổn định luồng của dữ liệu và việc tránh đường ống các sự đình trệ (In a large-scale model, a DMA engine transfers the next batch of data over the host-to-device link while the accelerator executes the current batch, maintaining a steady flow of data and avoiding pipeline stalls). Bộ khung các API phơi bày này mẫu thông qua

630
11.10 Thời gian chạy Sự hỗ trợ (Runtime Support)
được khóa-trang (page-locked) máy chủ các bộ đệm và không đồng bộ các bản sao, nhưng cơ chế là thuộc về kiến trúc: truyền tải
lô 𝑛+1 trong khi việc tính toán lô 𝑛để máy gia tốc là không được tuần tự hóa đằng sau bộ nhớ sự di chuyển (page-locked host buffers and asynchronous copies, but the mechanism is architectural: transfer batch 𝑛+1 while computing batch 𝑛so the accelerator is not serialized behind memory movement).
Tích chập các lớp trên một GPU cho thấy việc lập lịch trình phiên bản của cùng vấn đề (Convolutional layers on a GPU show the scheduling version of the same problem). Khi nhiều
tích chập các hạt nhân khác biệt trong kích thước và tính toán nhu cầu, tĩnh việc lập lịch trình có thể để lại tính toán các đơn vị
một phần bị chiếm đóng (When multiple convolution kernels differ in size and compute demand, static scheduling can leave compute units partially occupied). Động việc lập lịch trình cho phép AI các thời gian chạy ưu tiên nhỏ hơn các hạt nhân khi dung lượng là
có sẵn, việc cải thiện phần cứng sự sử dụng (Dynamic scheduling lets AI runtimes prioritize smaller kernels when capacity is available, improving hardware utilization). NVIDIA của TensorRT thời gian chạy có thể hợp nhất nhỏ các hạt nhân thành
lớn hơn sự thực thi các đơn vị để tránh khởi chạy chi phí chung, việc tối ưu hóa nhạy cảm-độ trễ suy luận các nhiệm vụ (NVIDIA’s TensorRT runtime can fuse small kernels into larger execution units to avoid launch overhead, optimizing latency-sensitive inference tasks).
Động sự điều chỉnh của sự thực thi các chiến lược để đáp lại thời gian-thực hệ thống các điều kiện tối ưu hóa
cả hai huấn luyện và suy luận hiệu suất qua phần cứng các nền tảng (Dynamic adjustment of execution strategies in response to real-time system conditions optimizes both training and inference performance across hardware platforms). Những các sự thích ứng này, tuy nhiên,
phụ thuộc trên việc có đúng hạt nhân ở đầu tiên nơi (These adaptations, however, depend on having the right kernel in the first place). Việc quay trở lại của chúng ta transformer suy luận ví dụ:
trước khi thời gian chạy có thể điều chỉnh việc xếp ô gạch hoặc bộ nhớ sự phân bổ cho một ma trận phép nhân, nó phải đầu tiên
quyết định cái nào hạt nhân sự triển khai để gọi (Returning to our transformer inference example: before the runtime can adjust tiling or memory allocation for a matrix multiplication, it must first decide which kernel implementation to invoke).
11.10.3 Thời gian chạy hạt nhân sự lựa chọn (Runtime kernel selection)
Trong khi các trình biên dịch thực hiện một ban đầu sự lựa chọn của các hạt nhân dựa trên tĩnh sự phân tích, AI các thời gian chạy có thể vẫn
chọn trong số được biên dịch trước hoặc được cung cấp-bởi-thư viện các biến thể trong suốt sự thực thi (While compilers perform an initial selection of kernels based on static analysis, AI runtimes may still choose among precompiled or library-provided variants during execution). Thời gian-thực các yếu tố, chẳng hạn như
có sẵn bộ nhớ, phần cứng sự sử dụng, và khối lượng công việc các ưu tiên, có thể khác biệt từ các sự giả định
được thực hiện trong suốt sự biên dịch (Real-time factors, such as available memory, hardware utilization, and workload priorities, may differ from the assumptions made during compilation). Trong của chúng ta transformer ví dụ, trình biên dịch và bộ khung xác định
hợp lệ độ chýnh xác các đường dẫn, trong khi thời gian chạy chọn hạt nhân biến thể thứ mà tốt nhất vừa vặn hiện tại
chuỗi chiều dài, lô hình dạng, và có sẵn phần cứng các tài nguyên (In our transformer example, the compiler and framework determine the legal precision paths, while the runtime selects the kernel variant that best fits the current sequence length, batch shape, and available hardware resources). Thời gian chạy sự lựa chọn thích ứng sự thực thi
cho đang thay đổi các điều kiện, nhưng nó duy trì bị ràng buộc bởi toán học các định dạng và các hạt nhân mô hình
đã được chuẩn bị để sử dụng (Runtime selection adapts execution to changing conditions, but it remains bounded by the numerical formats and kernels the model has been prepared to use).
Cho ví dụ, hãy xem xét dựa trên-transformer ngôn ngữ các mô hình, nơi một đáng kể phần của sự thực thi
thời gian là được dành trên ma trận các phép nhân (For instance, consider transformer-based language models, where a significant portion of execution time is spent on matrix multiplications). Hỗn hợp-độ chýnh xác transformer các hệ thống chẳng hạn như Megatron-LM
sử dụng FP16 sự thực thi trên GPU Tensor Các lõi để làm tăng thông lượng (Shoeybi et al. 2019) (Mixed-precision transformer systems such as Megatron-LM use FP16 execution on GPU Tensor Cores to increase throughput (Shoeybi et al. 2019)). Tại việc phục vụ
thời gian, AI thời gian chạy phải vẫn xác định nhất hiệu quả hạt nhân biến thể dựa trên hiện tại
hệ thống trạng thái (At serving time, the AI runtime must still determine the most efficient kernel variant based on the current system state). Nếu thấp hơn độ chýnh xác gây ra không thể chấp nhận toán học sự mất ổn định cho một cụ thể hoạt động,
thời gian chạy có thể chọn cho hỗn hợp-độ chýnh xác sự thực thi, một cách có chọn lọc việc sử dụng FP32 nơi cao hơn độ chýnh xác là
cần thiết (If lower precision causes unacceptable numerical instability for a particular operation, the runtime can opt for mixed-precision execution, selectively using FP32 where higher precision is necessary).
Bộ nhớ các sự ràng buộc cũng ảnh hưởng hạt nhân sự lựa chọn (Memory constraints also influence kernel selection). Khi bộ nhớ băng thông là bị giới hạn,
thời gian chạy có thể điều chỉnh của nó sự thực thi chiến lược, việc sắp xếp lại các hoạt động hoặc việc thay đổi việc xếp ô gạch chiến lược để làm vừa vặn
các sự tính toán vào có sẵn bộ nhớ cache thay vì việc dựa dẫm trên chậm hơn chính bộ nhớ (When memory bandwidth is limited, the runtime may adjust its execution strategy, reordering operations or changing the tiling strategy to fit computations into the available cache rather than relying on slower main memory). Cho ví dụ, một
lớn ma trận phép nhân có thể được phá vỡ thành nhỏ hơn các phần, việc đảm bảo rằng sự tính toán vừa vặn
vào trên-chip bộ nhớ của GPU, việc làm giảm tổng thể độ trễ (For example, a large matrix multiplication may be broken into smaller chunks, ensuring that the computation fits into the on-chip memory of the GPU, reducing overall latency).
Lô kích thước cũng ảnh hưởng hạt nhân sự lựa chọn (Batch size also influences kernel selection). Cho các khối lượng công việc thứ mà xử lý một sự kết hợp của nhỏ và lớn
các lô, AI thời gian chạy có thể chọn một được tối ưu hóa-độ trễ hạt nhân cho nhỏ các lô và một được tối ưu hóa-thông lượng
hạt nhân cho quy mô-lớn lô sự xử lý (For workloads that handle a mix of small and large batches, the AI runtime may choose a latency-optimized kernel for small batches and a throughput-optimized kernel for large-scale batch processing). Này sự điều chỉnh đảm bảo rằng mô hình tiếp tục
để hoạt động một cách hiệu quả qua khác nhau sự thực thi các kịch bản, mà không nhu cầu cho thủ công sự tinh chỉnh (This adjustment ensures that the model continues to operate efficiently across different execution scenarios, without the need for manual tuning). Với
thích hợp các hạt nhân được chọn và của chúng sự thực thi các tham số được thích ứng, cuối cùng đường ống giai đoạn
xác định khi nào và nơi nào mỗi hạt nhân chạy (With the appropriate kernels selected and their execution parameters adapted, the final pipeline stage determines when and where each kernel runs).
11.10.4 Hạt nhân việc lập lịch trình và sự sử dụng (Kernel scheduling and utilization)
Hạt nhân việc lập lịch trình hoàn tất thời gian chạy đường ống bằng cách việc xác định cách nào được chọn các hạt nhân thực thi
qua có sẵn phần cứng để tối đa hóa tính song song và tài nguyên sự sử dụng (Kernel scheduling completes the runtime pipeline by determining how selected kernels execute across available hardware to maximize parallelism and resource utilization). Việc quay trở lại
transformer suy luận yêu cầu: thời gian chạy đã chọn FP16 các hạt nhân cho sự chú ý ma trận các phép
nhân và đã thích ứng việc xếp ô gạch để vừa vặn hiện tại chuỗi chiều dài (Returning to the transformer inference request: the runtime has selected FP16 kernels for the attention matrix multiplications and adapted tiling to fit the current sequence length). Bây giờ bộ lập lịch trình phải phân phối
những các hoạt động này qua GPU luồng các bộ đa xử lý, xen kẽ chúng với lớp sự chuẩn hóa
và sự kích hoạt các hạt nhân, và đảm bảo rằng trung gian dữ liệu là được tìm nạp trước trước khi mỗi hoạt động cần
nó (Now the scheduler must distribute these operations across GPU streaming multiprocessors, interleave them with layer normalization and activation kernels, and ensure that intermediate data is prefetched before each operation needs it). Không giống như truyền thống nhiệm vụ các bộ lập lịch trình thứ mà quản lý CPU các luồng, AI các thời gian chạy phối hợp một nhiều
lớn hơn số lượng của các nhiệm vụ qua song song sự thực thi các đơn vị: GPU các lõi, TPU tâm thu các mảng (Jouppi et al.
2017), hoặc tùy chỉnh AI các máy gia tốc (Unlike traditional task schedulers that manage CPU threads, AI runtimes coordinate a much larger number of tasks across parallel execution units: GPU cores, TPU systolic arrays (Jouppi et al. 2017), or custom AI accelerators). Việc giữ những các tài nguyên này hoàn toàn được tham gia ngăn cản các nút thắt cổ chai và
tối đa hóa thông lượng (Keeping these resources fully engaged prevents bottlenecks and maximizes throughput).
Trong hình ảnh sự nhận dạng các mô hình thứ mà sử dụng tích chập các lớp, bộ lập lịch trình có thể phân phối các bộ lọc
qua nhiều xử lý các đơn vị để độc lập công việc chạy một cách đồng thời (In image recognition models that use convolutional layers, the scheduler can distribute filters across multiple processing units so independent work runs concurrently). Lô sự chuẩn hóa và

11. Phần cứng Sự gia tốc (Hardware Acceleration)
631
sự kích hoạt các hàm sau đó trở nên việc lập lịch trình các mối nguy hiểm (hazards): nếu chúng là không được xen kẽ với khác sự tính toán, chúng chặn đường ống và làm giảm thông lượng (activation functions then become scheduling hazards: if they are not interleaved with other computation, they block the pipeline and reduce throughput). Thời gian chạy việc lập lịch trình bảo tồn sự sử dụng bằng
cách việc giữ những nhỏ hơn các hạt nhân này khỏi việc tuần tự hóa lớn hơn tích chập đường dẫn (Runtime scheduling preserves utilization by keeping these smaller kernels from serializing the larger convolution path).
Thời gian-thực bộ nhớ sự quản lý củng cố cùng việc lập lịch trình mục tiêu (Real-time memory management reinforces the same scheduling goal). AI các thời gian chạy tải trước (preload) trung
gian dữ liệu, chẳng hạn như đặc trưng các bản đồ trong sâu thần kinh các mạng, vào bộ nhớ cache trước khi các hạt nhân cần nó (AI runtimes preload intermediate data, such as feature maps in deep neural networks, into cache before kernels need it). Này
chủ động sự di chuyển ngăn cản các sự chậm trễ từ chậm hơn bộ nhớ các tầng (tiers) và giữ sự thực thi liên tục (This proactive movement prevents delays from slower memory tiers and keeps execution continuous).
Cùng nhau, hạt nhân sự lựa chọn, động sự thực thi sự thích ứng, và việc lập lịch trình hình thành một một cách chặt chẽ được ghép nối
thời gian chạy đường ống (Together, kernel selection, dynamic execution adaptation, and scheduling form a tightly coupled runtime pipeline). Cho của chúng ta transformer suy luận yêu cầu, đường ống đã xác định tốt nhất hạt nhân
cho mỗi hoạt động, đã thích ứng việc xếp ô gạch và độ chýnh xác cho hiện tại bộ nhớ và phần cứng các điều kiện, và
đã phân phối công việc qua tính toán các đơn vị để duy trì cao sự sử dụng (For our transformer inference request, the pipeline determined the best kernel for each operation, adapted tiling and precision to current memory and hardware conditions, and distributed work across compute units to sustain high utilization). Những ba các pha này hoạt động
một cách liên tục và phụ thuộc lẫn nhau: một việc lập lịch trình quyết định có thể kích hoạt sự lựa chọn-lại của một khác
hạt nhân, thứ mà đến lượt nó yêu cầu mới sự thực thi tham số sự thích ứng (These three phases operate continuously and interdependently: a scheduling decision may trigger re-selection of a different kernel, which in turn requires new execution parameter adaptation).
Trình biên dịch và thời gian chạy các hệ thống được kiểm tra cho đến nay tối ưu hóa sự thực thi bên trong đơn các máy gia tốc,
nhưng lớn nhất AI các khối lượng công việc vượt quá cái gì bất kỳ đơn chip có thể cung cấp (The compiler and runtime systems examined thus far optimize execution within single accelerators, but the largest AI workloads exceed what any single chip can deliver). Đơn-chip các sự tối ưu hóa
có thể đạt được ấn tượng các kết quả thông qua trình biên dịch sự tối ưu hóa, dữ liệu luồng sự lựa chọn, sự hợp nhất, và
bộ nhớ việc lập kế hoạch (Single-chip optimizations can achieve impressive results through compiler optimization, dataflow selection, fusion, and memory planning). Tuy nhiên cho lớn nhất AI các khối lượng công việc, thậm chí tốt-được tối ưu hóa đơn-chip sự thực thi
chứng tỏ không đủ (Yet for the largest AI workloads, even well-optimized single-chip execution proves insufficient).
Hãy xem xét quy mô của việc huấn luyện GPT-3, thứ mà đã yêu cầu xấp xỉ 3.14×10^23 dấu phẩy-số thực
các hoạt động (Brown et al. 2020), một con số quá lớn nó thách thức trực giác mà không cụ thể sự so sánh (Consider the scale of training GPT-3, which required approximately 3.14×1023 floating-point operations (Brown et al. 2020), a number so large it defies intuition without concrete comparison).
Để nắm bắt này độ lớn (magnitude): thậm chí tại H100 của đỉnh FP8 thông lượng của 1.98 PFLOP/s, việc hoàn tất
này sự tính toán trên một đơn máy gia tốc sẽ yêu cầu khoảng 5 năm của liên tục sự hoạt động tại
lý thuyết đỉnh, và xấp xỉ 8.4–12.6 năm dưới sự sử dụng các sự giả định được sử dụng trong này đã làm việc
ví dụ (Choquette 2023) (To grasp this magnitude: even at the H100’s peak FP8 throughput of 1.98 PFLOP/s, completing this computation on a single accelerator would require about 5 years of continuous operation at theoretical peak, and roughly 8.4–12.6 years under the utilization assumptions used in this worked example (Choquette 2023)). Cao-khối lượng suy luận các dịch vụ tạo ra cùng áp lực từ
đối lập hướng: mỗi yêu cầu là nhỏ hơn một đầy đủ huấn luyện lượt chạy, nhưng toàn cầu yêu cầu khối lượng
có thể vượt quá cái gì bất kỳ đơn máy gia tốc có thể phục vụ (High-volume inference services create the same pressure from the opposite direction: each request is smaller than a full training run, but global request volume can exceed what any single accelerator can serve). Những tính toán các yêu cầu này đòi hỏi
việc mở rộng quy mô vượt ra ngoài đơn-chip các hệ thống, việc giới thiệu khác nhau kỹ thuật các thách thức từ những cái chúng
ta đã kiểm tra (These computational requirements necessitate scaling beyond single-chip systems, introducing different engineering challenges from those we have examined).
11.11 Nhiều-Chip Sự mở rộng quy mô (Multi-Chip Scaling)
Một đơn H100 cung cấp gần 1.98 PFLOP/s của FP8 thông lượng, tuy nhiên việc huấn luyện một rất lớn ngôn ngữ
mô hình có thể vẫn yêu cầu hàng ngàn của như vậy các chip việc làm việc trong sự phối hợp (A single H100 delivers nearly 1.98 PFLOP/s of FP8 throughput, yet training a very large language model can still require thousands of such chips working in concert). Các kỹ thuật được bao phủ trong
trước đó các phần (dữ liệu luồng sự tối ưu hóa, hạt nhân sự hợp nhất, bộ nhớ hệ thống phân cấp sự khai thác, và trình biên
dịch sự tối ưu hóa) duy trì nền tảng cho hiệu quả sự thực thi thậm chí trong nhiều-chip sự mở rộng quy mô; mỗi
cá nhân máy gia tốc phải vẫn được tối ưu hóa việc sử dụng những các nguyên tắc này (The techniques covered in previous sections (dataflow optimization, kernel fusion, memory hierarchy exploitation, and compiler optimization) remain the foundation for efficient execution even in multi-chip scaling; each individual accelerator must still be optimized using these principles). Mới bài học là rằng sự giao
tiếp trở thành một cái khác bộ nhớ hệ thống phân cấp (The new lesson is that communication becomes another memory hierarchy). Việc di chuyển dữ liệu từ các thanh ghi tới SRAM, HBM, NVLink,
và sau đó một dữ liệu trung tâm kết cấu (fabric) trở nên một cách lũy tiến chậm hơn và nhiều đắt đỏ hơn, do đó sự mở rộng quy mô là không còn
chỉ một câu hỏi của việc thêm các chip (Moving data from registers to SRAM, HBM, NVLink, and then a data center fabric gets progressively slower and more expensive, so scaling is no longer only a question of adding chips). Mục tiêu ở đây là để hiểu phần cứng ranh giới nơi
sự giao tiếp bắt đầu để thống trị (The goal here is to understand the hardware boundary where communication starts to dominate).
Khi đơn-máy gia tốc dung lượng chứng tỏ không đủ, thiết kế vấn đề chuyển dịch từ việc nuôi
một chip tới việc chọn cái nào sự giao tiếp ranh giới khối lượng công việc có thể chịu đựng (When single-accelerator capacity proves insufficient, the design problem shifts from feeding one chip to choosing which communication boundary the workload can tolerate). Các học viên
gặp phải những các ranh giới này trong sản xuất thậm chí khi hầu hết sự tối ưu hóa công việc duy trì bên trong một
đơn máy gia tốc (Practitioners encounter these boundaries in production even when most optimization work remains inside a single accelerator).
11.11.1 Nhiều-chip sự mở rộng quy mô các cách tiếp cận (Multi-chip scaling approaches)
Lớn AI các hệ thống mở rộng quy mô vượt ra ngoài cá nhân các máy gia tốc bằng cách việc di chuyển sự giao tiếp ranh giới
ra ngoài, và mỗi ranh giới thay đổi thống trị sự đánh đổi (Large AI systems scale beyond individual accelerators by moving the communication boundary outward, and each boundary changes the dominant trade-off). Chuỗi bắt đầu bên trong
gói (package) (The sequence begins inside the package). Dựa trên-Chiplet các kiến trúc phân vùng lớn các thiết kế thành nhỏ hơn, mô đun (modular) các khuôn (dies) được kết nối
với nhau bên trong một gói, việc bỏ qua sản xuất các giới hạn của nguyên khối (monolithic) các chip trong khi việc bảo tồn
tương đối thấp sự giao tiếp độ trễ (Chiplet-based architectures partition large designs into smaller, modular dies interconnected within one package, bypassing manufacturing limits of monolithic chips while preserving relatively low communication latency). Tiếp theo ranh giới là nút: nhiều-máy gia tốc các máy chủ
kết nối một vài các chip thông qua cấp độ-bảng hoặc cấp độ-máy chủ các kết nối liên kết (The next boundary is the node: multi-accelerator servers connect several chips through board- or server-level interconnects). Mỗi máy gia tốc có dành riêng
bộ nhớ và tính toán các tài nguyên, do đó các khối lượng công việc chia tách thông qua dữ liệu tính song song (mỗi máy gia tốc
xử lý khác nhau các lô) hoặc mô hình tính song song (khác nhau các máy gia tốc xử lý khác nhau mạng
các lớp) (Each accelerator has dedicated memory and compute resources, so workloads split through data parallelism (each accelerator processes different batches) or model parallelism (different accelerators handle different network layers)). Cao-băng thông trong-nút các kết nối liên kết có thể kích hoạt hiệu quả gradient sự đồng bộ hóa,
mặc dù được nhận ra hiệu suất phụ thuộc trên cấu trúc (topology) và tập thể sự giao tiếp tính hiệu quả (High-bandwidth intra-node interconnects can enable efficient gradient synchronization, though realized performance depends on topology and collective communication efficiency).

632
11.12 Dị thể SoC Thiết kế (Heterogeneous SoC Design)
41
Amdahl của Định luật (Sự mở rộng quy mô
Giới hạn) (Amdahl’s Law (Scaling Limit)): phần D.2.3 chính thức
hóa Amdahl của Định luật, thứ mà
ràng buộc tốc độ tăng tốc bởi tuần tự
tỷ lệ của một khối lượng công việc (section D.2.3 formalizes Amdahl’s Law, which bounds speedup by the serial fraction of a workload).
Trong
nhiều-máy gia tốc
huấn luyện,
gradient
sự đồng bộ hóa
có thể
trở thành
một
thống trị
tuần tự tỷ lệ (In multi-accelerator training, gradient synchronization can become a dominant serial fraction):
tại chỉ 5
phần trăm được phơi bày sự đồng bộ
hóa
chi phí chung,
tối đa
tốc độ tăng tốc là được giới hạn (capped) tại 20×
bất kể
của
bao
nhiều
các máy gia tốc là được thêm vào (at just 5 percent exposed synchronization overhead, maximum speedup is capped at 20× regardless of how many accelerators are added). Này
cứng trần (hard ceiling) giải thích tại sao
được phân phối-huấn luyện các hệ thống
tập trung quá nặng nề trên việc làm giảm,
việc giấu đi,
hoặc
việc chồng chéo
sự giao tiếp (This hard ceiling explains why distributed-training systems focus so heavily on reducing, hiding, or overlapping communication).
42
AllReduce:
Một tập
thể hoạt động từ MPI thứ mà
tập hợp các giá trị qua các quá
trình ("reduce") và phân
phối kết quả trở lại tới mọi
quá trình ("all") (A collective operation from MPI that aggregates values across processes (the “reduce”) and distributes the result back to every process (the “all”)). Trong này
chương, thuật ngữ xuất hiện chỉ
để xác định tại sao máy gia tốc-
tới-máy gia tốc băng thông quan
trọng cho huấn luyện các khối lượng công việc (In this chapter, the term appears only to identify why accelerator-to-accelerator bandwidth matters for training workloads).
Tại quy mô, các thuật toán, cấu trúc
các sự lựa chọn, và thời gian chạy các giao
thức xác định làm thế nào tốn kém này
sự đồng bộ hóa trở thành (At scale, algorithms, topology choices, and runtime protocols determine how costly this synchronization becomes).
Vượt ra ngoài nút, ranh giới mở rộng thành cụm (Beyond the node, the boundary expands into the cluster). Được xây dựng-theo mục đích dữ liệu trung tâm các kết cấu
phối hợp hàng trăm của các máy gia tốc, việc làm cấu trúc và tập thể sự giao tiếp các thuật toán
trung tâm các yếu tố quyết định của sự mở rộng quy mô tính hiệu quả; gần-tuyến tính sự mở rộng quy mô là có thể đạt được trên một số các khối lượng công việc khi
sự giao tiếp chi phí chung là được kiểm soát (Purpose-built data center fabrics coordinate hundreds of accelerators, making topology and collective communication algorithms central determinants of scaling efficiency; near-linear scaling is achievable on some workloads when communication overhead is controlled). Quy mô-tấm wafer (Wafer-scale) sự tích hợp là phản-bước đi (counter-move): thay vì
việc đẩy ranh giới ra ngoài, nó thu gọn nhiều hơn sự tính toán trở lại thành một lớn thiết bị (Wafer-scale integration is the counter-move: instead of pushing the boundary outward, it collapses more computation back into one large device). Các nền tảng
chẳng hạn như Cerebras cấp-WSE các hệ thống tích hợp một cách cực kỳ lớn các số lượng của các transistor và các lõi trên một
đơn thiết bị, việc làm giảm giữa-chip sự giao tiếp chi phí chung trong khi việc giới thiệu của riêng chúng các thách thức
trong nhiệt sự tản nhiệt, lỗi khả năng chịu đựng, và sản xuất năng suất (Platforms such as Cerebras WSE-class systems integrate extremely large numbers of transistors and cores on a single device, reducing inter-chip communication overhead while introducing their own challenges in thermal dissipation, fault tolerance, and manufacturing yield).
11.11.2 Tại sao sự mở rộng quy mô giới thiệu mới các sự ràng buộc (Why scaling introduces new constraints)
Sự chuyển đổi từ đơn-chip tới nhiều-chip các kiến trúc giới thiệu sự giao tiếp chi phí chung và
khác một cách định tính khác nhau các sự ràng buộc thứ mà định hình lại hệ thống sự tối ưu hóa (The transition from single-chip to multi-chip architectures introduces communication overhead and other qualitatively different constraints that reshape system optimization). Sự giao tiếp chi phí chung
xuất hiện như chính giới hạn trên sự mở rộng quy mô tính hiệu quả (Communication overhead emerges as the primary limit on scaling efficiency). Amdahl của Định luật41 định lượng cách nào sự giao tiếp
trong suốt gradient sự đồng bộ hóa tạo ra tuần tự các nút thắt cổ chai (Amdahl’s Law41 quantifies how communication during gradient synchronization creates sequential bottlenecks). Cho hàng trăm-tỷ-tham số-
quy mô các mô hình, AllReduce các hoạt động42 có thể yêu cầu việc trao đổi hàng trăm của gigabyte của các gradient
mỗi huấn luyện bước (For hundred-billion-parameter-scale models, AllReduce operations42 can require exchanging hundreds of gigabytes of gradients per training step).
Bậc-đầu tiên (first-order) số lượng là gradient tải trọng (payload) (The first-order quantity is the gradient payload). Cho một mô hình với 𝑃các tham số, đó tải trọng
là xấp xỉ tham số số đếm được nhân bởi các byte được lưu trữ cho mỗi gradient phần tử trước khi
trình tối ưu hóa trạng thái, đệm (padding), và giao thức chi phí chung đi vào (For a model with 𝑃parameters, that payload is roughly the parameter count multiplied by the bytes stored for each gradient element before optimizer state, padding, and protocol overhead enter). Sự mở rộng quy mô do đó cải thiện chỉ khi được
tiết kiệm tính toán thời gian vượt quá thời gian để di chuyển này tải trọng thông qua được chọn kết nối liên kết và
tập thể thuật toán (Scaling therefore improves only when the saved compute time exceeds the time to move this payload through the chosen interconnect and collective algorithm).
Này sự giao tiếp chi phí chung giải thích tại sao việc mở rộng quy mô tới rất lớn máy gia tốc các số lượng có thể cho thấy
giảm dần các lợi nhuận trừ khi hệ thống làm giảm số lượng của dữ liệu được trao đổi, giấu sự giao tiếp
đằng sau hữu ích sự tính toán, hoặc chọn một sự song song hóa chiến lược với một tốt hơn sự giao tiếp mẫu (This communication overhead explains why scaling to very large accelerator counts can show diminishing returns unless the system reduces the amount of data exchanged, hides communication behind useful computation, or chooses a parallelization strategy with a better communication pattern).
Cùng sự mở rộng cũng thay đổi bộ nhớ mô hình (The same expansion also changes the memory model). Bộ nhớ tính nhất quán (coherence) trở nên đắt đỏ
bởi vì việc đảm bảo rằng tất cả các bộ xử lý thấy nhất quán các góc nhìn của được chia sẻ bộ nhớ thêm giao thức lưu lượng và
độ trễ (Memory coherence becomes expensive because ensuring that all processors see consistent views of shared memory adds protocol traffic and latency). Cho AI các máy gia tốc với hàng ngàn của các lõi, này chi phí chung có thể trở nên cấm kỵ (prohibitive), việc ép buộc
tường minh bộ nhớ sự quản lý nơi các lập trình viên kiểm soát dữ liệu vị trí và sự đồng bộ hóa
một cách thủ công (For AI accelerators with thousands of cores, this overhead can become prohibitive, forcing explicit memory management where programmers control data placement and synchronization manually).
Một khi sự tính toán kéo dài nhiều các liên kết, các chip, và bộ nhớ các ngăn xếp, độ tin cậy và năng lượng trở thành
phần của cùng sự mở rộng quy mô câu chuyện (Once computation spans many links, chips, and memory stacks, reliability and energy become part of the same scaling story). Quy mô-lớn các hệ thống phải xử lý thành phần các lỗi một cách duyên dáng
bởi vì xác suất của ít nhất một lỗi tăng lên với hệ thống kích thước (Large-scale systems must handle component failures gracefully because the probability of at least one failure rises with system size). Cho này chương, phần cứng
bài học là đủ: TPU Các nhóm (Pods) và quy mô-tấm wafer các hệ thống cả hai cần cấp độ-phần cứng sự dư thừa và
sự giao tiếp các đường dẫn thứ mà chịu đựng thành phần các lỗi (Jouppi et al. 2023; Systems 2021) (For this chapter, the hardware lesson is enough: TPU Pods and wafer-scale systems both need hardware-level redundancy and communication paths that tolerate component failures (Jouppi et al. 2023; Systems 2021)). Dữ liệu
sự di chuyển cũng phát triển nhiều đắt đỏ hơn với khoảng cách, việc biến đổi được phân phối huấn luyện thành một cẩn thận
sự cân bằng giữa sự tính toán tính song song và sự giao tiếp tính hiệu quả (Data movement also grows more expensive with distance, transforming distributed training into a careful balance between computation parallelism and communication efficiency).
Dữ liệu trung tâm sự mở rộng quy mô và biên (edge) sự triển khai đại diện cho đối lập các đầu cuối của một sự triển khai quang phổ,
tuy nhiên chúng chia sẻ cùng chính các nguyên tắc (Data center scaling and edge deployment represent opposite ends of a deployment spectrum, yet they share the same core principles). Dữ liệu trung tâm sự mở rộng quy mô phối hợp nhiều cao-thông lượng
các máy gia tốc, trong khi biên sự mở rộng quy mô làm vừa vặn hữu ích AI vào một vài bị ràng buộc các watt (Data center scaling coordinates many high-throughput accelerators, while edge scaling fits useful AI into a few constrained watts). Cả hai các trường hợp yêu cầu
việc khớp khối lượng công việc các đặc điểm với phần cứng các khả năng trong khi việc tối thiểu hóa dữ liệu sự di chuyển (Both cases require matching workload characteristics to hardware capabilities while minimizing data movement). Các
nguyên tắc của tính toán sự chuyên biệt hóa, bộ nhớ hệ thống phân cấp sự tối ưu hóa, và khối lượng công việc ánh xạ áp dụng
tại cả hai các quy mô; chỉ các sự ràng buộc khác biệt (The principles of compute specialization, memory hierarchy optimization, and workload mapping apply at both scales; only the constraints differ). Dữ liệu các trung tâm tối ưu hóa cho tổng hợp thông lượng bên trong
điện năng các ngân sách được đo trong các megawatt; biên các thiết bị tối ưu hóa cho độ nhạy bén bên trong chật hẹp
pin và nhiệt các đường bao (Data centers optimize for aggregate throughput within power budgets measured in megawatts; edge devices optimize for responsiveness within tight battery and thermal envelopes). Cùng tầm nhìn mô hình thứ mà chạy một cách thoải mái trong một dữ liệu trung tâm có thể
cần một một cách triệt để khác biệt ánh xạ chiến lược trên một điện thoại thông minh hoặc vi điều khiển (The same vision model that runs comfortably in a data center may need a radically different mapping strategy on a smartphone or microcontroller).
11.12 Dị thể SoC Thiết kế (Heterogeneous SoC Design)
Di động, ô tô, và IoT các sự triển khai hoạt động dưới nhiều chặt chẽ hơn điện năng, nhiệt, và độ trễ
các sự ràng buộc hơn dữ liệu trung tâm phần cứng (Mobile, automotive, and IoT deployments operate under much tighter power, thermal, and latency constraints than data center hardware). Những các sự ràng buộc này ép buộc được chuyên biệt hóa tính toán các đơn vị, bộ nhớ
hệ thống phân cấp sự tối ưu hóa, và khối lượng công việc ánh xạ các chiến lược để hoạt động dưới một cách đáng kể khác biệt
các quy tắc (These constraints force specialized compute units, memory hierarchy optimization, and workload mapping strategies to operate under dramatically different rules). Kết quả là dị thể Hệ thống-trên-Chip (System-on-Chip - SoC) các kiến trúc thứ mà tích hợp CPU các lõi,
GPU các shader, kỹ thuật số tín hiệu các bộ xử lý (digital signal processors - DSPs), và dành riêng thần kinh xử lý các đơn vị (neural processing units - NPUs) bên trong
một đơn chip (The result is heterogeneous System-on-Chip (SoC) architectures that integrate CPU cores, GPU shaders, digital signal processors (DSPs), and dedicated neural processing units (NPUs) within a single chip). Việc điều phối những đa dạng các bộ xử lý này để đạt được tối ưu hiệu suất dưới nghiêm ngặt
điện năng, nhiệt, và độ trễ các yêu cầu đòi hỏi hoàn toàn khác biệt các cách tiếp cận hơn dữ liệu trung tâm
các sự triển khai (Orchestrating these diverse processors to achieve optimal performance under strict power, thermal, and latency requirements demands wholly different approaches than data center deployments).

11. Phần cứng Sự gia tốc (Hardware Acceleration)
633
43
NPU (Thần kinh Xử lý
Đơn vị) (Neural Processing Unit): NPU của được chuyên biệt hóa
ma trận các công cụ là được tối ưu hóa
cho dày đặc tensor các hoạt động,
việc cung cấp phần cứng cơ
sở cho khối lượng công việc sự phân
phối được mô tả (The NPU’s specialized matrix engines are optimized for dense tensor operations, providing the hardware basis for the workload distribution described). Này sự chuyên
môn hóa tạo ra một quan trọng sự ràng
buộc cho bộ lập lịch trình: bất kỳ
AI toán tử không được ánh xạ tới
NPU của được hỗ trợ dữ liệu các đường dẫn
phải "rơi trở lại" (fall back) tới một GPU hoặc
CPU (This specialization creates a critical constraint for the scheduler: any AI operator not mapped to the NPU’s supported data paths must “fall back” to a GPU or CPU). Này sự dự phòng có thể xóa bỏ
NPU của năng lượng-tính hiệu quả
lợi thế, làm phức tạp thời
gian-thực độ trễ các ngân sách, và đóng
góp vào nhiệt áp lực trên
di động các thiết bị (This fallback can erase the NPU’s energy-efficiency advantage, complicate real-time latency budgets, and contribute to thermal pressure on mobile devices).
Ví dụ 11.4: Dị thể các vi điều khiển (Heterogeneous microcontrollers)
Bối cảnh: Thông minh Chuông cửa (Đánh thức Tầm nhìn) (Wake Vision) đẩy tính dị thể tới của nó logic giới hạn (Context: The Smart Doorbell (Wake Vision) pushes heterogeneity to its logical limit). Không giống như một
điện thoại thông minh SoC với một nhiều-watt ngân sách, một chuông cửa camera thường chạy trên một vi điều khiển
với một milliwatt ngân sách (Unlike a smartphone SoC with a multi-watt budget, a doorbell camera often runs on a microcontroller with a milliwatt budget).
Sự hiểu biết (Insight): Để đạt được thời gian-thực người sự phát hiện (30 FPS) bên trong này đường bao, các MCU có thể áp dụng
cùng dị thể chiến lược như của chúng lớn hơn di động các anh em họ nhưng tại một vi-quy mô (To achieve real-time person detection (30 FPS) within this envelope, MCUs can adopt the same heterogeneous strategy as their larger mobile cousins but at a micro-scale). Một điển hình
kiến trúc ghép nối một tổng quát-mục đích lõi (cho ví dụ, Cortex-M) cho hệ thống logic với một
dành riêng vi-NPU (cho ví dụ, Ethos-U) cho CNN sự gia tốc (A typical architecture pairs a general-purpose core (for example, Cortex-M) for system logic with a dedicated micro-NPU (for example, Ethos-U) for CNN acceleration).
Các hệ thống bài học (Systems lesson): Vi-NPU có thể thực thi Đánh thức Tầm nhìn MobileNetV2-phong cách khối lượng công việc xa
nhiều năng lượng hiệu quả hơn hơn CPU một mình khi của nó các toán tử ánh xạ tới máy gia tốc (The micro-NPU can execute the Wake Vision MobileNetV2-style workload far more energy efficiently than the CPU alone when its operators map to the accelerator). Mà không
được chuyên biệt hóa sự gia tốc, luôn-bật (always-on) lời hứa của Thông minh Chuông cửa sẽ là khó khăn để
đáp ứng bên trong một vi điều khiển-hạng (microcontroller-class) năng lượng ngân sách (Without specialized acceleration, the always-on promise of the Smart Doorbell would be difficult to meet within a microcontroller-class energy budget).
11.12.1 Di động SoC kiến trúc sự tiến hóa (Mobile SoC architecture evolution)
Hiện đại di động AI các công cụ làm ví dụ cho dị thể tính toán bằng cách việc phối hợp CPU các lõi, GPU
các shader, các DSP, và dành riêng các NPU43 qua một được chia sẻ bộ nhớ hệ thống phân cấp (Modern mobile AI engines exemplify heterogeneous computing by coordinating CPU cores, GPU shaders, DSPs, and dedicated NPUs43 across a shared memory hierarchy). Khối lượng công việc sự phân phối
cho phép máy tính tầm nhìn các hạt nhân thực thi trên GPU hoặc NPU các đường dẫn, âm thanh sự xử lý sử dụng DSP số học
các đơn vị, và nặng-ma trận thần kinh-mạng các lớp sử dụng được tối ưu hóa-NPU các công cụ khi toán tử tập hợp
là được hỗ trợ (Workload distribution lets computer vision kernels execute on GPU or NPU paths, audio processing use DSP arithmetic units, and matrix-heavy neural-network layers use NPU-optimized engines when the operator set is supported). Này sự phối hợp yêu cầu cẩn thận việc lập lịch trình để đáp ứng thời gian-thực các sự ràng buộc trong khi
việc quản lý nhiệt sự điều chỉnh (throttling) và pin tuổi thọ (This coordination requires careful scheduling to meet real-time constraints while managing thermal throttling and battery life).
Một số di động SoC các thiết kế nhấn mạnh đa dạng bộ xử lý sự chuyên biệt hóa, trong khi một cách dọc được tích hợp
các chiến lược làm nổi bật cách nào chặt chẽ phần cứng-phần mềm đồng-thiết kế có thể kích hoạt một cách chặt chẽ được phối hợp dị
thể sự thực thi (Some mobile SoC designs emphasize diverse processor specialization, while vertically integrated strategies highlight how tight hardware-software co-design can enable tightly coordinated heterogeneous execution). Thống nhất bộ nhớ các kiến trúc có thể làm giảm tường minh dữ liệu việc sao chép chi phí chung, và
khác nhau tính toán các khối có thể được lập lịch trình cho khác nhau toán tử các loại (cho ví dụ, nặng-ma trận
các lớp trên một NPU, tích chập các toán tử trên một GPU, và kiểm soát luồng trên CPU) (Unified memory architectures can reduce explicit data copying overhead, and different compute blocks can be scheduled for different operator types (for example, matrix-heavy layers on an NPU, convolutional operators on a GPU, and control flow on the CPU)). Này sự phối hợp
hỗ trợ tương tác trên-thiết bị các trải nghiệm, mặc dù được nhận ra độ trễ phụ thuộc trên đầy đủ đường ống
và thiết bị nhiệt các điều kiện (This coordination supports interactive on-device experiences, though realized latency depends on the full pipeline and device thermal conditions).
Vượt ra ngoài một cách dọc được tích hợp các giải pháp, IP việc cấp phép các mô hình cho phép SoC các nhà thiết kế để tùy chỉnh
bộ xử lý các sự kết hợp dựa trên mục tiêu các ứng dụng, việc trộn CPU, GPU, DSP, và NPU các khối (Beyond vertically integrated solutions, IP licensing models allow SoC designers to customize processor combinations based on target applications, mixing CPU, GPU, DSP, and NPU blocks). Này
mô đun tính linh hoạt cho phép ô tô các SoC để nhấn mạnh mang tính quyết định (deterministic) thời gian-thực sự xử lý trong khi
điện thoại thông minh các SoC tối ưu hóa cho tương tác hiệu suất và pin tính hiệu quả (This modular flexibility allows automotive SoCs to emphasize deterministic real-time processing while smartphone SoCs optimize for interactive performance and battery efficiency).
11.12.2 Các chiến lược cho động khối lượng công việc sự phân phối (Strategies for dynamic workload distribution)
Với nhiều được chuyên biệt hóa các bộ xử lý có sẵn trên dị thể các SoC, quan trọng thách thức trở thành
một cách thông minh việc phân phối thần kinh mạng các hoạt động qua những các tài nguyên này để tối đa hóa hiệu suất
trong khi việc tôn trọng điện năng và độ trễ các sự ràng buộc (With multiple specialized processors available on heterogeneous SoCs, the critical challenge becomes intelligently distributing neural network operations across these resources to maximize performance while respecting power and latency constraints). Hãy xem xét một cụ thể ví dụ: một kỹ sư việc triển khai
một thời gian-thực đối tượng sự phát hiện đường ống trên một di động SoC với một CPU, GPU, và NPU (Consider a concrete example: an engineer deploying a real-time object detection pipeline on a mobile SoC with a CPU, GPU, and NPU). Đường ống
có ba các giai đoạn: một MobileNet xương sống cho đặc trưng sự trích xuất, không cực đại sự ức chế (nonmaximum suppression - NMS)
cho sự xử lý hậu kỳ, và một hiển thị lớp phủ (overlay) cho việc hiển thị bao quanh các hộp (The pipeline has three stages: a MobileNet backbone for feature extraction, nonmaximum suppression (NMS) for postprocessing, and a display overlay for rendering bounding boxes). Xương sống bao gồm
của theo chiều sâu (depthwise) có thể tách rời các tích chập với đều đặn, có thể dự đoán truy cập các mẫu và thấp tính toán
chi phí, việc làm cho nó một tốt sự phù hợp cho một NPU khi toán tử tập hợp là được hỗ trợ, thậm chí mặc dù theo chiều sâu
các lớp là thường bị ràng buộc-bộ nhớ thay vì cao-số học-cường độ các hạt nhân (The backbone consists of depthwise separable convolutions with regular, predictable access patterns and low compute cost, making it a good fit for an NPU when the operator set is supported, even though depthwise layers are often memory-bound rather than high-arithmetic-intensity kernels). NMS, bằng sự tương phản,
bao gồm có điều kiện việc phân nhánh (branching) qua biến đổi-chiều dài ứng cử viên các danh sách, với không đều đặn bộ nhớ truy cập
thứ mà ánh xạ kém tới NPU của được cố định dữ liệu luồng (NMS, by contrast, involves conditional branching over variable-length candidate lists, with irregular memory access that maps poorly to the NPU’s fixed dataflow). CPU xử lý NMS một cách hiệu quả hơn bởi vì
của nó nhánh bộ dự đoán và lớn các bộ nhớ cache cung cấp chỗ cho không thể dự đoán kiểm soát luồng (The CPU handles NMS more efficiently because its branch predictor and large caches accommodate the unpredictable control flow). Cuối cùng, hiển
thị lớp phủ bao gồm cấp độ-pixel sự tổng hợp qua toàn bộ khung hình, một một cách ồ ạt song song nhưng
về mặt toán học đơn giản khối lượng công việc thứ mà ánh xạ một cách tự nhiên tới GPU của shader các lõi (Finally, the display overlay involves pixel-level compositing across the entire frame, a massively parallel but arithmetically simple workload that maps naturally to the GPU’s shader cores). Này ba-chiều sự phân chia,
NPU cho xương sống, CPU cho NMS, GPU cho lớp phủ, đạt được thấp hơn độ trễ và thấp hơn điện năng
hơn việc chạy toàn bộ đường ống trên bất kỳ đơn bộ xử lý (This three-way split, NPU for the backbone, CPU for NMS, GPU for the overlay, achieves lower latency and lower power than running the entire pipeline on any single processor).
Này ví dụ minh họa tổng quát nguyên tắc: thần kinh các mạng yêu cầu thông minh sự phân vùng
qua dị thể các bộ xử lý dựa trên hoạt động các đặc điểm và hiện tại hệ thống trạng thái (This example illustrates the general principle: neural networks require intelligent partitioning across heterogeneous processors based on operation characteristics and current system state). Tích
chập các lớp với đều đặn dữ liệu truy cập các mẫu điển hình thực thi một cách hiệu quả trên GPU shader các lõi
hoặc NPU ma trận các công cụ, trong khi các hoạt động với không đều đặn sự thưa thớt các mẫu hoặc có điều kiện kiểm soát (Convolutional layers with regular data access patterns typically execute efficiently on GPU shader cores or NPU matrix engines, while operations with irregular sparsity patterns or conditional control)

634
11.12 Dị thể SoC Thiết kế (Heterogeneous SoC Design)
luồng (flow) có thể thực hiện tốt hơn trên tổng quát-mục đích CPU các lõi với lớn các bộ nhớ cache (flow may perform better on general-purpose CPU cores with large caches). Sự chú ý các cơ chế trong
các transformer hưởng lợi từ NPU ma trận các công cụ khi các chuỗi là dài, nhưng có thể thực thi nhiều
hiệu quả hơn trên CPU khi chuỗi các chiều dài là nhỏ do NPU thiết lập chi phí chung (Attention mechanisms in transformers benefit from NPU matrix engines when sequences are long, but may execute more efficiently on CPU when sequence lengths are small due to the NPU setup overhead).
Vượt ra ngoài tĩnh hoạt động-tới-bộ xử lý ánh xạ, tối ưu sự gán có thể thay đổi từng khoảnh khắc
tới từng khoảnh khắc (Beyond static operation-to-processor mapping, the optimal assignment can change moment to moment). Việc quay trở lại đối tượng sự phát hiện ví dụ: trong suốt pin sự hoạt động, hệ thống
có thể chuyển dịch MobileNet xương sống từ NPU tới thấp hơn-điện năng DSP các lõi, việc chấp nhận cao hơn
độ trễ để kéo dài pin tuổi thọ (Returning to the object detection example: during battery operation, the system might shift the MobileNet backbone from the NPU to lower-power DSP cores, accepting higher latency to extend battery life). Nhiệt trạng thái giới thiệu một cái khác chiều: khi việc tiếp cận
nhiệt các giới hạn, thời gian chạy có thể làm giảm khung hình tốc độ, chuyển đổi tới một nhỏ hơn mô hình, giảm-xung nhịp (down-clock)
NPU, hoặc di chuyển không được hỗ trợ nặng-nhánh (branch-heavy) các giai đoạn tới CPU thay vì việc giả định CPU là
luôn luôn nhiều hiệu quả hơn thần kinh-mạng công cụ (Thermal state introduces another dimension: when approaching thermal limits, the runtime may reduce frame rate, switch to a smaller model, down-clock the NPU, or move unsupported branch-heavy stages to the CPU rather than assuming the CPU is always the more efficient neural-network engine). An toàn-tới hạn (Safety-critical) ô tô các ứng dụng thêm độ trễ
các yêu cầu thứ mà ưu tiên mang tính quyết định sự thực thi hơn đỉnh thông lượng (Safety-critical automotive applications add latency requirements that prioritize deterministic execution over peak throughput). Cuối cùng, đồng thời
khối lượng công việc sự can thiệp (interference) từ nhiều AI các ứng dụng có thể yêu cầu tải sự cân bằng (load balancing) qua có sẵn
các bộ xử lý để duy trì chất lượng của dịch vụ (Finally, concurrent workload interference from multiple AI applications may require load balancing across available processors to maintain quality of service).
Việc làm phức tạp bộ xử lý sự lựa chọn thách thức, được chia sẻ bộ nhớ các kiến trúc yêu cầu sự phân xử (arbitration)
khi nhiều các bộ xử lý truy cập LPDDR một cách đồng thời (Compounding the processor selection challenge, shared memory architectures require arbitration when multiple processors access LPDDR simultaneously). Di động bộ nhớ các bộ điều khiển có thể ưu tiên
thời gian-thực camera hoặc hiển thị các đường dẫn hơn nền (background) AI các nhiệm vụ, việc ép buộc thần kinh-mạng các thời gian chạy để
thích ứng của chúng sự thực thi các mẫu với có sẵn băng thông (Mobile memory controllers may prioritize real-time camera or display paths over background AI tasks, forcing neural-network runtimes to adapt their execution patterns to available bandwidth). Này sự phân xử trở nên quan trọng trong suốt
chuyên sâu-bộ nhớ (memory-intensive) các hoạt động giống như lớn ngôn ngữ mô hình suy luận, nơi tham số luồng (streaming) từ
DRAM phải được một cách cẩn thận phối hợp qua các bộ xử lý (This arbitration becomes critical during memory-intensive operations like large language model inference, where parameter streaming from DRAM must be carefully coordinated across processors).
11.12.3 Điện năng và nhiệt sự quản lý (Power and thermal management)
Di động AI các khối lượng công việc phải duy trì cao hiệu suất trong khi việc hoạt động bên trong nghiêm ngặt điện năng các ngân sách
(budgets) và nhiệt các đường bao (Mobile AI workloads must maintain high performance while operating within strict power budgets and thermal envelopes). Những các sự ràng buộc này yêu cầu chặt紧 chẽ sự phối hợp qua dị thể
các bộ xử lý (These constraints require tight coordination across heterogeneous processors).
Dị thể các SoC triển khai được phối hợp động điện áp và tần số sự mở rộng quy mô (dynamic voltage and frequency scaling - DVFS)
qua nhiều các bộ xử lý để tối ưu hóa điện năng-hiệu suất đường bao (Heterogeneous SoCs implement coordinated dynamic voltage and frequency scaling (DVFS) across multiple processors to optimize the power-performance envelope). Khi một bộ xử lý
tăng lên tần số để đáp ứng độ trễ các nhu cầu, hệ thống có thể làm giảm điện áp trên khác các bộ xử lý để
duy trì tổng điện năng ngân sách (When one processor increases frequency to meet latency demands, the system may reduce voltage on other processors to maintain total power budget). Này sự phối hợp trở nên phức tạp trong AI các khối lượng công việc nơi tính toán
các pha có thể chuyển dịch một cách nhanh chóng giữa các bộ xử lý (This coordination becomes complex in AI workloads where computational phases may shift rapidly between processors). Hệ thống phải dự đoán sắp tới khối lượng công việc
các sự chuyển đổi để một cách ưu tiên (preemptively) điều chỉnh việc hoạt động các điểm trong khi việc tránh điện áp/tần số các sự dao động (oscillations)
thứ mà làm suy giảm tính hiệu quả (The system must predict upcoming workload transitions to preemptively adjust operating points while avoiding voltage/frequency oscillations that degrade efficiency).
Khi DVFS một mình không thể duy trì điện năng đường bao, di động các SoC triển khai nhiệt sự điều chỉnh
thông qua một hỗn hợp của tần số sự làm giảm, mô hình sự thích ứng, và nhiệm vụ sự di chuyển (migration) (When DVFS alone cannot maintain the power envelope, mobile SoCs implement thermal throttling through a mixture of frequency reduction, model adaptation, and task migration). Khi NPU
tiếp cận nhiệt các giới hạn trong suốt chuyên sâu thần kinh mạng sự xử lý, thời gian chạy có thể chuyển dịch được chọn
các toán tử tới một cái khác được hỗ trợ bộ xử lý, hạ thấp suy luận tần số, hoặc chọn một nhỏ hơn mô hình
hồ sơ (profile) (When the NPU approaches thermal limits during intensive neural network processing, the runtime can shift selected operators to another supported processor, lower inference frequency, or choose a smaller model profile). Này cách tiếp cận bảo tồn dịch vụ tính khả dụng trong suốt nhiệt các sự kiện, mặc dù nó yêu cầu
chi tiết khối lượng công việc sự đặc trưng hóa để dự đoán sự thực thi thời gian và điện năng sự tiêu thụ qua khác nhau
các bộ xử lý (This approach preserves service availability during thermal events, though it requires detailed workload characterization to predict execution time and power consumption across different processors).
Vượt ra ngoài thời gian-thực điện năng và nhiệt sự quản lý, di động AI các hệ thống phải cũng thích ứng của chúng
tính toán các chiến lược dựa trên pin trạng thái và sạc tình trạng (Beyond real-time power and thermal management, mobile AI systems must also adapt their computational strategies based on battery state and charging status). Trong suốt thấp pin các điều kiện,
hệ thống có thể chuyển đổi từ cao-độ chính xác các mô hình tới hiệu quả các sự xấp xỉ, di chuyển các khối lượng công việc
từ đói-điện năng (power-hungry) NPU tới năng lượng-hiệu quả DSP, hoặc làm giảm suy luận tần số trong khi việc duy trì
ứng dụng độ nhạy bén (During low battery conditions, the system may switch from high-accuracy models to efficient approximations, migrate workloads from power-hungry NPU to energy-efficient DSP, or reduce inference frequency while maintaining application responsiveness). Ngược lại, trong suốt việc sạc, hệ thống có thể kích hoạt cao hơn-hiệu suất
các mô hình và tăng lên xử lý tần số để cung cấp được nâng cao người dùng các trải nghiệm (Conversely, during charging, the system can enable higher-performance models and increase processing frequency to deliver enhanced user experiences).
11.12.4 Ô tô dị thể AI các hệ thống (Automotive heterogeneous AI systems)
Ô tô các ứng dụng giới thiệu độc đáo dị thể tính toán các thách thức thứ mà kết hợp
di động-phong cách điện năng tính hiệu quả với cứng thời gian-thực độ trễ các yêu cầu và chức năng an toàn các yêu
cầu (Automotive applications introduce unique heterogeneous computing challenges that combine mobile-style power efficiency with hard real-time latency requirements and functional safety requirements). Này sự kết hợp đòi hỏi khác biệt thuộc về kiến trúc các cách tiếp cận (This combination demands distinct architectural approaches).
Ô tô các SoC nhắm tới để cung cấp mang tính quyết định suy luận độ trễ cho an toàn-tới hạn các chức năng trong khi
việc hỗ trợ tiên tiến người lái xe sự hỗ trợ các hệ thống (advanced driver assistance systems - ADAS) (Automotive SoCs aim to provide deterministic inference latency for safety-critical functions while supporting advanced driver assistance systems (ADAS)). Dư thừa xử lý các phần tử hỗ trợ
chức năng an toàn các mục tiêu trong khi cao-hiệu suất các máy gia tốc xử lý sự nhận thức (perception), việc lập kế hoạch (planning), và
kiểm soát các thuật toán (Redundant processing elements support functional safety objectives while high-performance accelerators handle perception, planning, and control algorithms). Này kiến trúc yêu cầu thời gian sự cô lập (temporal isolation) giữa an toàn-tới hạn và sự tiện
lợi (convenience) các chức năng, được triển khai thông qua phần cứng sự phân vùng và được kích hoạt-thời gian (time-triggered) việc lập lịch trình (This architecture requires temporal isolation between safety-critical and convenience functions, implemented through hardware partitioning and time-triggered scheduling).
Cụ thể ML khối lượng công việc động lực là băng thông sự tranh chấp (contention): một tự nhiên-ngôn ngữ giọng nói trợ lý (The concrete ML workload motivation is bandwidth contention: a natural-language voice assistant)

11. Phần cứng Sự gia tốc (Hardware Acceleration)
635
việc chạy một lớn ngôn ngữ mô hình trên cùng SoC có thể tiêu thụ đáng kể bộ nhớ băng thông
trong suốt việc giải mã, việc can thiệp với băng thông được yêu cầu bởi một an toàn-tới hạn 3D đối tượng sự phát hiện
mạng thứ mà phải hoàn tất của nó tiếp theo suy luận bên trong một cứng hạn chót (running a large language model on the same SoC can consume substantial memory bandwidth during decoding, interfering with the bandwidth required by a safety-critical 3D object detection network that must complete its next inference within a hard deadline). Thời gian sự cô lập ngăn cản
sự tiện lợi các khối lượng công việc khỏi việc xuất hiện trong đối tượng sự phát hiện mạng của việc lập lịch trình cửa sổ (Temporal isolation prevents convenience workloads from appearing in the object detection network’s scheduling window). Tương
tự, cảm biến sự kết hợp (fusion) các mô hình thứ mà ăn radar, lidar, và camera các luồng một cách đồng thời phải đáp ứng
nghiêm ngặt mỗi-khung hình các hạn chót được phối hợp bởi được kích hoạt-thời gian bộ lập lịch trình; bất kỳ băng thông hoặc tính toán
sự can thiệp từ một thấp hơn-sự ưu tiên AI dịch vụ có thể đẩy những các mô hình này qua của chúng hạn chót và kích hoạt
một an toàn sự dự phòng (fallback) (Similarly, sensor fusion models that ingest radar, lidar, and camera streams simultaneously must meet strict per-frame deadlines coordinated by the time-triggered scheduler; any bandwidth or compute interference from a lower-priority AI service can push these models past their deadline and trigger a safety fallback).
Những an toàn các yêu cầu này trở nên thậm chí nhiều phức tạp hơn khi việc xem xét rằng hiện đại các phương tiện
tích hợp nhiều được kích hoạt-AI các SoC cho khác nhau các miền (These safety requirements become even more complex when considering that modern vehicles integrate multiple AI-enabled SoCs for different domains). Tầm nhìn sự xử lý các SoC xử lý dựa trên-camera
sự nhận thức, radar sự xử lý các SoC quản lý RF cảm biến dữ liệu, trong khi trung tâm tính toán các nền tảng
phối hợp cao-cấp độ việc ra quyết định (Vision processing SoCs handle camera-based perception, radar processing SoCs manage RF sensor data, while central compute platforms coordinate high-level decision-making). Những được phân phối các hệ thống này phải duy trì thời gian tính nhất quán
qua cảm biến các phương thức (modalities), việc yêu cầu được chuyên biệt hóa giữa-SoC sự giao tiếp các giao thức và được phân phối
sự đồng bộ hóa các cơ chế (These distributed systems must maintain temporal coherence across sensor modalities, requiring specialized inter-SoC communication protocols and distributed synchronization mechanisms).
Việc mở rộng vượt ra ngoài phương tiện của bên trong các cảm biến, phương tiện-tới-mọi thứ (vehicle-to-everything - V2X) sự giao tiếp
thêm một cái khác lớp của dị thể sự xử lý nơi AI các thuật toán phải phối hợp cục bộ cảm biến
sự xử lý với thông tin được nhận từ khác các phương tiện và cơ sở hạ tầng (Extending beyond the vehicle’s internal sensors, vehicle-to-everything (V2X) communication adds another layer of heterogeneous processing where AI algorithms must coordinate local sensor processing with information received from other vehicles and infrastructure). Điều này yêu cầu thấp-
độ trễ sự xử lý các chuỗi nơi các modem, AI các máy gia tốc, và kiểm soát các hệ thống hoạt động dưới nghiêm ngặt
thời gian và chức năng-an toàn các yêu cầu (This requires low-latency processing chains where modems, AI accelerators, and control systems operate under strict timing and functional-safety requirements).
11.12.5 Phần mềm ngăn xếp các thách thức (Software stack challenges)
Thuộc về kiến trúc sự tinh vi của dị thể các SoC biến phần mềm thành sự phối hợp lớp
cho điện năng, nhiệt trạng thái, tính mang tính quyết định, và toán tử sự dự phòng (The architectural sophistication of heterogeneous SoCs turns software into the coordination layer for power, thermal state, determinism, and operator fallback). Việc lập trình dị thể các SoC
yêu cầu các bộ khung thứ mà trừu tượng hóa bộ xử lý các sự khác biệt trong khi vẫn việc phơi bày quan trọng-hiệu suất
sự tối ưu hóa các cơ hội (Programming heterogeneous SoCs requires frameworks that abstract processor differences while still exposing performance-critical optimization opportunities). OpenCL và Vulkan cung cấp chéo-bộ xử lý sự thực thi, nhưng tối ưu
hiệu suất vẫn phụ thuộc trên cụ thể-bộ xử lý sự tinh chỉnh thứ mà làm phức tạp tính di động (portability) (OpenCL and Vulkan provide cross-processor execution, but optimal performance still depends on processor-specific tuning that complicates portability). Hiện đại ML
các bộ khung chẳng hạn như TensorFlow Lite và PyTorch Mobile triển khai tự động bộ xử lý sự lựa chọn,
nhưng các nhà phát triển vẫn cần để hiểu dị thể sự thực thi các mẫu bởi vì không được hỗ trợ
các toán tử có thể rơi trở lại tới kém hiệu quả hơn các bộ xử lý (Modern ML frameworks such as TensorFlow Lite and PyTorch Mobile implement automatic processor selection, but developers still need to understand heterogeneous execution patterns because unsupported operators may fall back to less efficient processors).
Được chia sẻ bộ nhớ các kiến trúc làm phức tạp sự phối hợp vấn đề (Shared memory architectures compound the coordination problem). Bộ nhớ sự quản lý phải
tính đến cho cụ thể-bộ xử lý việc tạo bộ nhớ cache hành vi, bộ nhớ truy cập các mẫu, và tính nhất quán (coherency) các yêu
cầu (Memory management must account for processor-specific caching behavior, memory access patterns, and coherency requirements). CPU các bộ nhớ cache có thể can thiệp với GPU bộ nhớ truy cập các mẫu, trong khi NPU trực tiếp bộ nhớ
truy cập (direct memory access - DMA) các hoạt động phải được đồng bộ hóa với CPU bộ nhớ cache các hoạt động để duy trì dữ liệu tính nhất
quán (CPU caches may interfere with GPU memory access patterns, while NPU direct memory access (DMA) operations must be synchronized with CPU cache operations to maintain data consistency).
Dị thể các SoC giải quyết này sự phức tạp thông qua dựa trên-máy học thời gian chạy sự tối ưu hóa
thứ mà học từ sự thực thi các mẫu để cải thiện bộ xử lý sự lựa chọn, nhiệt sự quản lý, và
điện năng sự phân bổ (Heterogeneous SoCs address this complexity through machine learning-based runtime optimization that learns from execution patterns to improve processor selection, thermal management, and power allocation). Những các hệ thống này thu thập viễn trắc (telemetry) trên khối lượng công việc các đặc điểm, bộ xử lý sự sử dụng,
và điện năng sự tiêu thụ để dự đoán sự thực thi các chiến lược cho mới các khối lượng công việc (These systems collect telemetry on workload characteristics, processor utilization, and power consumption to predict execution strategies for new workloads).
Không đơn bộ xử lý kiến trúc nào có thể một cách tối ưu xử lý đa dạng tính toán các mẫu trong AI
các ứng dụng, do đó dị thể sự gia tốc trở thành một sự phối hợp vấn đề thay vì một phần cứng
hàng tồn kho (inventory) (No single processor architecture can optimally handle the diverse computational patterns in AI applications, so heterogeneous acceleration becomes a coordination problem rather than a hardware inventory). Hiệu quả di động AI các hệ thống cung cấp cao hiệu suất chỉ khi bộ xử lý sự gán,
bộ nhớ tính nhất quán, nhiệt các giới hạn, và độ trễ các sự ràng buộc là được quản lý cùng nhau (Efficient mobile AI systems deliver high performance only when processor assignment, memory coherence, thermal limits, and latency constraints are managed together).
Cùng sự phối hợp vấn đề cũng có một năng lượng hậu quả (The same coordination problem also has an energy consequence). Nếu phần cứng sự lựa chọn xác định
bao nhiêu dữ liệu di chuyển, bao lâu một lần các máy gia tốc đình trệ, và cách nào một cách hiệu quả số học ánh xạ tới silicon,
thì nó cũng xác định bao nhiêu năng lượng sự triển khai tiêu thụ cho mỗi hữu ích sự dự đoán (If hardware selection determines how much data moves, how often accelerators stall, and how efficiently arithmetic maps to silicon, then it also determines how much energy the deployment consumes for each useful prediction).
11.13 Phần cứng Tính bền vững (Hardware Sustainability)
Tại hạm đội (fleet) quy mô, năng lượng một chip đốt cháy mỗi suy luận dừng việc là một chú thích cuối trang và trở thành một chính
phần cứng-sự lựa chọn tiêu chí (At fleet scale, the energy a chip burns per inference stops being a footnote and becomes a primary hardware-selection criterion). Một đơn cao-khối lượng suy luận khối lượng công việc, được nhân bản qua hàng ngàn
của các máy chủ, biến một khiêm tốn mỗi-hoạt động tính hiệu quả khoảng cách thành hàng trăm của tấn (metric tons) của CO2 mỗi năm (A single high-volume inference workload, replicated across thousands of servers, turns a modest per-operation efficiency gap into hundreds of metric tons of CO2 per year).
Hiệu suất mỗi watt do đó chi phối một AI dịch vụ của vận hành carbon dấu chân và điện năng
hóa đơn, không chỉ pin tuổi thọ trên một điện thoại (Performance per watt therefore governs an AI service’s operational carbon footprint and electricity bill, not only battery life on a phone). Cuốn sổ tay bên dưới làm cho số tiền đặt cược cụ thể, việc so sánh một
tổng quát-CPU hạm đội so với được chuyên biệt hóa các máy gia tốc trên cùng một-tỷ-suy luận-mỗi-ngày khối lượng công việc (The notebook below makes the stake concrete, comparing a generic-CPU fleet against specialized accelerators on the same billion-inference-per-day workload).

636
11.14 Các ngụy biện và Các cạm bẫy (Fallacies and Pitfalls)
Khăn ăn Toán học (Napkin Math) 11.10: Carbon ROI của được chuyên biệt hóa silicon
Vấn đề (Problem): Nên một suy luận hạm đội chạy trên tổng quát các CPU hay đầu tư vào được chuyên biệt hóa các NPU (Thần kinh
Xử lý Các đơn vị)? (Should an inference fleet run on generic CPUs or invest in specialized NPUs (Neural Processing Units)?)
Vật lý (Physics): Được chuyên biệt hóa phần cứng phân bổ một lớn hơn tỷ lệ của của nó các transistor cho số học các đơn vị
và ít hơn cho kiểm soát logic (Specialized hardware allocates a larger fraction of its transistors to arithmetic units and fewer to control logic).
• CPU suy luận (CPU inference): 100 W cho 1 TFLOP/s (tính hiệu quả = 0.01 TFLOP/s/W) (100 W for 1 TFLOP/s (efficiency = 0.01 TFLOP/s/W)).
• NPU suy luận (NPU inference): 5 W cho 10 TFLOP/s (tính hiệu quả = 2 TFLOP/s/W) (5 W for 10 TFLOP/s (efficiency = 2 TFLOP/s/W)).
• Khoảng cách (The gap): NPU là 200× nhiều năng lượng-hiệu quả hơn mỗi hoạt động (The NPU is 200× more energy-efficient per operation).
Toán học (Math):
1. Khối lượng công việc (Workload): 1 tỷ các suy luận mỗi ngày (1 billion inferences per day).
2. CPU hạm đội năng lượng (CPU fleet energy): 1,000 CPU các máy chủ × 100 W × 24 h ≈2,400 kWh/ngày (1,000 CPU servers × 100 W × 24 h ≈2,400 kWh/day).
3. NPU hạm đội năng lượng (NPU fleet energy): 100 NPU các chip × 5 W × 24 h ≈12 kWh/ngày (100 NPU chips × 5 W × 24 h ≈12 kWh/day).
4. Carbon các khoản tiết kiệm (Carbon savings): Tại 0.429 kg/kWh, việc chuyển đổi tới các NPU tiết kiệm ~373.9 t của CO2 mỗi năm (At 0.429 kg/kWh, switching to NPUs saves ~373.9 t of CO2 per year).
Các hệ thống sự hiểu biết (Systems insight): Được chuyên biệt hóa các máy gia tốc có thể một cách vật chất làm giảm năng lượng sự sử dụng của được khớp
suy luận các khối lượng công việc (Specialized accelerators can materially reduce the energy use of matched inference workloads). Cho các khối lượng công việc với ổn định số học các mẫu và cao sự triển khai
khối lượng, mỗi-hoạt động năng lượng các khoản đạt được kết hợp thành đáng kể các sự làm giảm trong vận hành
carbon dấu chân tương đối với tổng quát-mục đích phần cứng (For workloads with stable arithmetic patterns and high deployment volume, the per-operation energy gains compound into substantial reductions in operational carbon footprint relative to general-purpose hardware).
Tính bền vững quan điểm củng cố một chủ đề thứ mà đã lặp lại xuyên suốt này chương:
phần cứng sự lựa chọn là không bao giờ một một cách hoàn toàn kỹ thuật quyết định (The sustainability perspective reinforces a theme that has recurred throughout this chapter: hardware selection is never a purely technical decision). Hiệu suất mỗi watt, carbon chi phí, và
tổng chi phí của quyền sở hữu phải tất cả đi vào quyết định bộ khung bên cạnh đỉnh FLOP/s và bộ nhớ
băng thông (Performance per watt, carbon cost, and total cost of ownership must all enter the decision framework alongside peak FLOP/s and memory bandwidth). Với sự mở rộng quy mô, tính dị thể, và tính bền vững bây giờ trong tầm nhìn, còn lại bước là để
xác định các quan niệm sai lầm thứ mà gây ra các nhóm để chọn sai phần cứng đường dẫn (With scaling, heterogeneity, and sustainability now in view, the remaining step is to identify the misconceptions that cause teams to choose the wrong hardware path).
11.14 Các ngụy biện và Các cạm bẫy (Fallacies and Pitfalls)
Phần cứng sự gia tốc liên quan đến phản trực giác hiệu suất các đặc điểm nơi ấn tượng
các thông số kỹ thuật che giấu tiềm ẩn các nút thắt cổ chai (Hardware acceleration involves counterintuitive performance characteristics where impressive specifications mask underlying bottlenecks). Các ngụy biện và các cạm bẫy ở đây nắm bắt phần cứng sự lựa chọn
và sự tối ưu hóa các lỗi thứ mà lãng phí đắt đỏ máy gia tốc các tài nguyên và dẫn tới các sự triển khai thứ mà
đạt được chỉ 10–30 phần trăm của lý thuyết hiệu suất (The fallacies and pitfalls here capture hardware selection and optimization errors that waste expensive accelerator resources and lead to deployments that achieve only 10–30 percent of theoretical performance).
Ngụy biện: Nhiều được chuyên biệt hóa phần cứng luôn luôn cung cấp tốt hơn hiệu suất hơn tổng quát-mục đích các giải pháp thay thế (Fallacy: More specialized hardware always provides better performance than general-purpose alternatives).
Các kỹ sư giả định được chuyên biệt hóa các máy gia tốc tự động vượt trội hơn tổng quát-mục đích các bộ xử lý
cho tất cả AI các khối lượng công việc (Engineers assume specialized accelerators automatically outperform general-purpose processors for all AI workloads). Trong thực tế, được chuyên biệt hóa phần cứng đạt được đỉnh hiệu suất chỉ khi các khối lượng công
việc khớp thuộc về kiến trúc các sự giả định, cốt lõi của thuật toán-máy móc đồng-thiết kế (In reality, specialized hardware achieves peak performance only when workloads match architectural assumptions, the core of algorithm-machine co-design). Như được chứng minh
trong phần 11.6, các hoạt động phải vượt quá máy gia tốc của sườn núi điểm (ridge point) để là bị ràng buộc-tính toán (compute bound); một A100
GPU có một sườn núi điểm của 153 FLOP/byte, có nghĩa là các hoạt động với số học cường độ bên dưới
này ngưỡng là bị ràng buộc-bộ nhớ (memory bound) bất kể của máy gia tốc của 312 TFLOP/s đỉnh tính toán (As demonstrated in section 11.6, operations must exceed the accelerator’s ridge point to be compute bound; an A100 GPU has a ridge point of 153 FLOP/byte, meaning operations with arithmetic intensity below this threshold are memory bound regardless of the accelerator’s 312 TFLOP/s peak compute). Một
transformer sự chú ý softmax với AI = 2 FLOP/byte–5 FLOP/byte đạt được chỉ 4.1 TFLOP/s–10.2
TFLOP/s (3.3 phần trăm sự sử dụng) trên một A100 (A transformer attention softmax with AI = 2 FLOP/byte–5 FLOP/byte achieves only 4.1 TFLOP/s–10.2 TFLOP/s (3.3 percent utilization) on an A100). Các CPU với sườn núi các điểm xung quanh 10 FLOP/byte–20
FLOP/byte vẫn coi này hạt nhân như bị ràng buộc-bộ nhớ, nhưng cùng AI phạm vi tương ứng với khoảng
10 phần trăm–50 phần trăm của một CPU của thấp hơn đỉnh (CPUs with ridge points around 10 FLOP/byte–20 FLOP/byte still treat this kernel as memory-bound, but the same AI range corresponds to about 10 percent–50 percent of a CPU’s lower peak). Các mô hình với không đều đặn bộ nhớ truy cập, nhỏ lô
các kích thước, hoặc động tính toán các đồ thị có thể thực hiện tốt hơn trên linh hoạt các bộ xử lý (Models with irregular memory access, small batch sizes, or dynamic computation graphs may perform better on flexible processors). Hiệu quả phần cứng
sự lựa chọn yêu cầu việc khớp khối lượng công việc số học cường độ với thuộc về kiến trúc sườn núi các điểm, không phải việc giả định
sự chuyên môn hóa luôn luôn chiến thắng (Effective hardware selection requires matching workload arithmetic intensity to architectural ridge points, not assuming specialization always wins).
Cạm bẫy: Việc bỏ qua bộ nhớ băng thông các giới hạn khi việc chọn sự gia tốc các chiến lược (Pitfall: Ignoring memory bandwidth limitations when selecting acceleration strategies).
Các học viên tập trung trên đỉnh TFLOP/s mà không việc phân tích liệu của chúng các khối lượng công việc có thể đạt được
bị ràng buộc-tính toán hiệu suất (Practitioners focus on peak TFLOP/s without analyzing whether their workloads can achieve compute-bound performance). Như được định lượng trong phần 11.5.1, năng lượng mô hình được sử dụng ở đây gán
khoảng 640 pJ cho một DRAM truy cập so với 0.5 pJ cho một trên-chip SRAM truy cập, việc tạo ra các bậc-của-
độ lớn (orders-of-magnitude) năng lượng các hình phạt (As quantified in section 11.5.1, the energy model used here assigns about 640 pJ to a DRAM access versus 0.5 pJ for an on-chip SRAM access, creating orders-of-magnitude energy penalties). Một máy gia tốc việc quảng cáo 300 TFLOP/s với 2 TB/s băng thông có
một sườn núi điểm của 150 FLOP/byte; LayerNorm các hoạt động với AI = 1.5 FLOP/byte đạt được chỉ
3 TFLOP/s (1 phần trăm sự sử dụng) trong này đã làm việc ví dụ (An accelerator advertising 300 TFLOP/s with 2 TB/s bandwidth has a ridge point of 150 FLOP/byte; LayerNorm operations with AI = 1.5 FLOP/byte achieve only 3 TFLOP/s (1 percent utilization) in this worked example). Các tổ chức có thể triển khai đắt đỏ

11. Phần cứng Sự gia tốc (Hardware Acceleration)
637
các máy gia tốc tính toán-cao cho bị ràng buộc-bộ nhớ các khối lượng công việc và vẫn thấy thấp sự sử dụng nếu băng thông,
không phải tính toán, là nút thắt cổ chai (high-compute accelerators for memory-bound workloads and still see low utilization if bandwidth, not compute, is the bottleneck). Các nhóm phải tính toán khối lượng công việc số học cường độ và so sánh
đối nghịch phần cứng sườn núi các điểm trước khi việc mua các máy gia tốc (Teams must calculate workload arithmetic intensity and compare against hardware ridge points before purchasing accelerators).
Ngụy biện: Phần cứng sự gia tốc các lợi ích mở rộng quy mô một cách tuyến tính với bổ sung các máy gia tốc (Fallacy: Hardware acceleration benefits scale linearly with additional accelerators).
Các nhóm mong đợi tám các GPU để huấn luyện 8× nhanh hơn một GPU (Teams expect eight GPUs to train 8× faster than one GPU). Nhiều-máy gia tốc sự mở rộng quy mô giới thiệu
sự giao tiếp chi phí chung thứ mà vi phạm tuyến tính sự mở rộng quy mô các sự giả định (Multi-accelerator scaling introduces communication overhead that violates linear scaling assumptions). Như được lưu ý trong phần 11.11, AllRe-
duce các hoạt động cho gradient sự đồng bộ hóa có thể yêu cầu việc trao đổi lớn gradient các tải trọng cho
lớn các mô hình (As noted in section 11.11, AllReduce operations for gradient synchronization can require exchanging large gradient payloads for large models). Với NVLink việc cung cấp 600 GB/s hai chiều (một nửa đó, mỗi hướng, cho một một-
chiều gradient luồng), việc đồng bộ hóa 1 GB của các gradient yêu cầu 3.33 ms; cho một 50 ms huấn luyện bước,
điều này đại diện cho 6.7 phần trăm của bước thời gian (With NVLink delivering 600 GB/s bidirectional (half that, per direction, for a one-way gradient stream), synchronizing 1 GB of gradients requires 3.33 ms; for a 50 ms training step, this represents 6.7 percent of step time). Mà không tính toán-sự giao tiếp sự chồng chéo, này đã làm việc
tám-GPU kịch bản đạt được khoảng 7.5× tốc độ tăng tốc (93.8 phần trăm tính hiệu quả) trước khi tải sự mất cân bằng,
sự đồng bộ hóa các rào cản, và không đủ song song công việc làm giảm sự mở rộng quy mô xa hơn (Without compute-communication overlap, this worked eight-GPU scenario achieves about 7.5× speedup (93.8 percent efficiency) before load imbalance, synchronization barriers, and insufficient parallel work reduce scaling further).
Cạm bẫy: Việc lập kế hoạch máy gia tốc dung lượng từ đỉnh FLOP/s các thông số kỹ thuật (Pitfall: Planning accelerator capacity from peak FLOP/s specifications).
Các nhà cung cấp quảng cáo đỉnh FLOP/s như dứt khoát thước đo của máy gia tốc khả năng, nhưng thế giới-thực
hiệu suất bằng Đỉnh FLOP/s × Sự sử dụng, nơi sự sử dụng là được ra lệnh bởi roofline mô hình
(phần 11.6) (Vendors advertise peak FLOP/s as the definitive measure of accelerator capability, but real-world performance equals Peak FLOP/s × Utilization, where utilization is dictated by the roofline model (section 11.6)). Một A100 quảng cáo 312 TFLOP/s tại FP16, tuy nhiên đại diện việc lập ngân sách kịch bản
ở đây duy trì chỉ 120 TFLOP/s–180 TFLOP/s (40 phần trăm–60 phần trăm sự sử dụng) cho transformer
huấn luyện bởi vì bị ràng buộc-bộ nhớ các hoạt động chẳng hạn như sự chú ý và LayerNorm kéo xuống trung bình
thông lượng (An A100 advertises 312 TFLOP/s at FP16, yet the representative budgeting scenario here sustains only 120 TFLOP/s–180 TFLOP/s (40 percent–60 percent utilization) for transformer training because memory-bound operations such as attention and LayerNorm drag down the average throughput). Hệ thống-khuyến nghị (recommender-system) kịch bản thậm chí tệ hơn, việc đạt tới chỉ 10 TFLOP/s–30
TFLOP/s (3.2 phần trăm–9.6 phần trăm sự sử dụng) bởi vì thưa thớt, không đều đặn bộ nhớ truy cập các mẫu để lại
tính toán các đơn vị nhàn rỗi (The recommender-system scenario fares even worse, reaching only 10 TFLOP/s–30 TFLOP/s (3.2 percent–9.6 percent utilization) because sparse, irregular memory access patterns leave compute units idle). Các kỹ sư nên lập ngân sách các dự án dựa trên được duy trì thông lượng, được đo lường hoặc
được ước tính thông qua roofline mô hình, thay vì đỉnh tiếp thị các thông số kỹ thuật (Engineers should budget projects based on sustained throughput, measured or estimated via the roofline model, rather than peak marketing specifications).
Ngụy biện: Bất kỳ FLOP/s xếp hạng nào có thể ước tính một thấp-độ chính xác khối lượng công việc (Fallacy: Any FLOP/s rating can estimate a low-precision workload).
Các máy gia tốc có tách biệt các đường dẫn dữ liệu cho khác nhau các độ chính xác, và đỉnh thông lượng biến đổi
một cách đáng kể qua chúng (Accelerators have separate datapaths for different precisions, and the peak throughput varies dramatically across them). Một H100 cung cấp xấp xỉ 1,000 TFLOP/s trong FP16 tensor các hoạt động
nhưng chỉ khoảng 67 TFLOP/s trong FP32 CUDA-lõi các hoạt động: một 15–16× khoảng cách bên trong cùng chip
(Choquette 2023) (An H100 delivers roughly 1,000 TFLOP/s in FP16 tensor operations but only about 67 TFLOP/s in FP32 CUDA-core operations: a 15–16× gap within the same chip (Choquette 2023)). Việc ước tính huấn luyện thời gian với FP32 con số khi khối lượng công việc thực sự
sử dụng BF16 tạo ra sự sử dụng các con số thứ mà trông thảm khốc không vì lý do nào, và việc khớp với
sai roofline phân loại sai các hạt nhân như bị ràng buộc-tính toán khi chúng là bị ràng buộc-bộ nhớ (hoặc ngược
lại) (Estimating training time with the FP32 number when the workload actually uses BF16 produces utilization figures that look catastrophic for no reason, and matching against the wrong roofline misclassifies kernels as compute-bound when they are memory-bound (or vice versa)). Luôn luôn khớp đỉnh hằng số với độ chính xác khối lượng công việc thực sự phát hành, và trích dẫn
độ chính xác một cách tường minh khi việc báo cáo MFU (Always match the peak constant to the precision the workload actually issues, and quote precision explicitly when reporting MFU).
Cạm bẫy: Việc triển khai nhỏ-lô suy luận các khối lượng công việc trên tính toán-cao các máy gia tốc (Pitfall: Deploying small-batch inference workloads on high-compute accelerators).
Các nhóm triển khai cao-thông lượng huấn luyện các máy gia tốc (A100, H100) cho nhạy cảm-độ trễ suy luận
với lô kích thước 1–4 (Teams deploy high-throughput training accelerators (A100, H100) for latency-sensitive inference with batch size 1–4). Như roofline mô hình (phần 11.6) dự đoán, nhỏ các lô một cách nghiêm trọng làm giảm
số học cường độ: một dày đặc lớp với M=N=2048 đạt được AI = 1 FLOP/byte tại lô=1 so với AI =
204.8 FLOP/byte tại lô=256 (As the roofline model (section 11.6) predicts, small batches severely reduce arithmetic intensity: a dense layer with M=N=2048 achieves AI = 1 FLOP/byte at batch=1 vs. AI = 204.8 FLOP/byte at batch=256). Tại lô=1, bị ràng buộc-bộ nhớ roofline trần là chỉ khoảng 2.04
TFLOP/s trên A100 và 0.3 TFLOP/s trên T4 (At batch=1, the memory-bound roofline ceiling is only about 2.04 TFLOP/s on A100 and 0.3 TFLOP/s on T4). T4 của đỉnh là 65 TFLOP/s (FP16 Tensor Lõi) với một
sườn núi điểm của 203.1 FLOP/byte (65 TFLOP/s / 320 GB/s) (The T4’s peak is 65 TFLOP/s (FP16 Tensor Core) with a ridge point of 203.1 FLOP/byte (65 TFLOP/s / 320 GB/s)). Nhỏ-lô suy luận duy trì bị ràng buộc-bộ nhớ
trên cả hai các máy gia tốc, do đó T4 của thấp hơn chi phí có thể làm cho nó nhiều kinh tế hơn bất chấp của nó nhiều
thấp hơn đỉnh tính toán (Small-batch inference remains memory bound on both accelerators, so the T4’s lower cost can make it more economical despite its much lower peak compute). Huấn luyện-hạng máy gia tốc các phiên bản (instances) thường thuê cho một vài lần nhiều hơn
suy luận-hạng các phiên bản cho ít độ trễ khoản đạt được trong này chế độ (Training-class accelerator instances often rent for several times more than inference-class instances for little latency gain in this regime). Suy luận các sự triển khai nên khớp
lô kích thước với máy gia tốc các đặc điểm, việc sử dụng tính toán-cao các máy gia tốc chỉ cho được làm theo lô việc phục vụ
nơi số học cường độ vượt quá sườn núi các điểm (Inference deployments should match batch size to accelerator characteristics, using high-compute accelerators only for batched serving where arithmetic intensity exceeds ridge points).
Ngụy biện: Cụ thể-nhà cung cấp các sự tối ưu hóa không có dài hạn tính di động chi phí (Fallacy: Vendor-specific optimizations have no long-term portability cost).
Các tổ chức tối ưu hóa một cách độc quyền cho cụ thể các nhà cung cấp để tối đa hóa hiệu suất mà không việc xem
xét hệ thống tính linh hoạt (Organizations optimize exclusively for specific vendors to maximize performance without considering system flexibility). Như được thảo luận trong phần 11.9, sâu sự tích hợp với cụ thể-nhà cung cấp các thư viện
(CUDA, TensorRT, XLA) và tùy chỉnh các hạt nhân tạo ra sự khóa chặt (lock-in) (As discussed in section 11.9, deep integration with vendor-specific libraries (CUDA, TensorRT, XLA) and custom kernels creates lock-in). Một cơ sở mã với nhiều được viết bằng tay
máy gia tốc các hạt nhân có thể yêu cầu đáng kể kỹ thuật nỗ lực để chuyển (port) tới một khác nhà cung cấp, việc trì hoãn
phần cứng các sự nâng cấp và việc ngăn cản nhiều-nhà cung cấp các sự triển khai (A codebase with many hand-written accelerator kernels can require substantial engineering effort to port to a different vendor, delaying hardware upgrades and preventing multi-vendor deployments). Cụ thể-nhà cung cấp các sự tối ưu hóa
nên do đó được cô lập đằng sau phần cứng sự trừu tượng hóa các lớp (Vendor-specific optimizations should therefore be isolated behind hardware abstraction layers). Việc duy trì di động mã các đường dẫn
kích hoạt nhà cung cấp sự cạnh tranh, phần cứng tính linh hoạt, và nhanh hơn sự áp dụng của đang nổi lên các máy gia tốc trong khi
vẫn việc nắm bắt hầu hết hiệu suất các lợi ích thông qua cấp độ-bộ khung các sự tối ưu hóa (Maintaining portable code paths enables vendor competition, hardware flexibility, and faster adoption of emerging accelerators while still capturing most performance benefits through framework-level optimizations).
Cạm bẫy: Việc nhúng cụ thể-nhà cung cấp các hạt nhân trực tiếp vào ứng dụng logic (Pitfall: Embedding vendor-specific kernels directly into application logic).
Tính di động chi phí trở thành khó nhất để quản lý khi cụ thể-máy gia tốc mã là rải rác xuyên qua
mô hình mã, sự tiền xử lý, bản dựng (build) các tập lệnh, và việc phục vụ các đường dẫn (The portability cost becomes hardest to manage when accelerator-specific code is scattered through model code, preprocessing, build scripts, and serving paths). Một sạch hơn thiết kế cô lập cụ thể-nhà cung cấp

638
11.15 Tóm tắt (Summary)
các hạt nhân đằng sau khả năng các kiểm tra (capability checks), bộ khung sự phân phối các lớp, hoặc hẹp toán tử các thư viện, do đó
hệ thống có thể giữ một nhanh đường dẫn mà không việc làm cho mọi cao hơn-cấp độ thành phần nhận thức-nhà cung cấp (kernels behind capability checks, framework dispatch layers, or narrow operator libraries, so the system can keep a fast path without making every higher-level component vendor-aware). Các
kỹ thuật mục tiêu là không phải để tránh sự chuyên môn hóa; nó là để giữ sự chuyên môn hóa có thể thay thế khi
phần cứng hạm đội thay đổi (The engineering goal is not to avoid specialization; it is to keep specialization replaceable when the hardware fleet changes).
Các ngụy biện bên trên giảm tới một cụ thể sự mua sắm (procurement) kiểm tra (The fallacies above reduce to a concrete procurement test).
Điểm kiểm tra (Checkpoint) 11.4: Tính khả thi sự đánh giá: Có thể bạn chạy nó? (Feasibility assessment: Can you run it?)
Trước khi việc mua sắm phần cứng, xác nhận tất cả ba cứng các sự ràng buộc (Before procuring hardware, validate all three hard constraints).
□Bộ nhớ dung lượng (Memory capacity): Tính toán 𝑀req = Các trọng số + KV Bộ nhớ cache + Sự kích hoạt Bộ đệm và xác nhận
𝑀req < 𝑀device cho một 7-tỷ-tham số Llama mô hình với 14 GB FP16 các trọng số trên một 16
GB GPU (Compute 𝑀req = Weights+KV Cache+Activation Buffer and verify 𝑀req < 𝑀device for a 7-billion-parameter Llama model with 14 GB FP16 weights on a 16 GB GPU).
□Băng thông (Bandwidth): Tính toán 𝑇token = 𝐷vol/BW cho một 70-tỷ-tham số mô hình (140 GB) trên 1
TB/s bộ nhớ băng thông, sau đó so sánh kết quả với một 50 ms độ trễ mục tiêu (Compute 𝑇token = 𝐷vol/BW for a 70-billion-parameter model (140 GB) on 1 TB/s memory bandwidth, then compare the result with a 50 ms latency target).
□Tính toán (Compute): Tính toán 𝑇process = 𝑂/(𝑅peak ⋅𝜂hw) và so sánh nó với thông lượng mục tiêu (Compute 𝑇process = 𝑂/(𝑅peak ⋅𝜂hw) and compare it with the throughput target).
Việc xử lý video tại 30 FPS yêu cầu việc hoàn tất suy luận bên trong 33.3 ms (Processing video at 30 FPS requires completing inference within 33.3 ms).
□Roofline vị trí (Roofline placement): Cho một máy gia tốc tại xấp xỉ 2 TFLOP/s đỉnh và 200 GB/s băng
thông, ước tính sườn núi-điểm số học cường độ, sau đó đặt một 10 FLOP/byte hạt nhân
chống lại nó: là nó bị ràng buộc-tính toán- hay bị ràng buộc-bộ nhớ, và sẽ một nhanh hơn xung nhịp (clock) giúp nó hoàn toàn? (For an accelerator at roughly 2 TFLOP/s peak and 200 GB/s bandwidth, estimate the ridge-point arithmetic intensity, then place a 10 FLOP/byte kernel against it: is it compute- or memory-bound, and would a faster clock help it at all?)
Danh sách kiểm tra này tổng hợp các nguyên tắc được phát triển xuyên suốt này chương, việc dịch thuật lý thuyết
sự hiểu biết thành thực tế kỹ thuật các quyết định (This checklist synthesizes the principles developed throughout this chapter, translating theoretical understanding into practical engineering decisions). Cùng nhau, những các ngụy biện này giảm chương của
bộ máy tới một chẩn đoán thói quen: bắt đầu từ khối lượng công việc, chọn nút thắt cổ chai số liệu, khớp
phần cứng đường dẫn với đó số liệu, và lập ngân sách cho tính di động, sự mở rộng quy mô, và năng lượng các hậu quả của
đó sự lựa chọn (Together, these fallacies reduce the chapter’s machinery to a diagnostic habit: start from the workload, choose the bottleneck metric, match the hardware path to that metric, and budget for the portability, scaling, and energy consequences of that choice).
11.15 Tóm tắt (Summary)
Phần cứng sự gia tốc là lực lượng thứ mà đã biến đổi máy học từ học thuật sự tò mò thành
thực tế thực tế, việc định hình lại cách nào chúng ta thiết kế cả hai tính toán các hệ thống và các thuật toán thứ mà chạy
trên chúng (Hardware acceleration is the force that transformed machine learning from academic curiosity to practical reality, reshaping how we design both computational systems and the algorithms that run on them). Sự tiến hóa từ tổng quát-mục đích các bộ xử lý tới được chuyên biệt hóa AI các máy gia tốc phản ánh một
sự chuyển dịch hướng tới cụ thể-miền (domain-specific) tính toán nơi phần cứng và phần mềm là được đồng-thiết kế để tối ưu hóa
cụ thể tính toán các mẫu (The evolution from general-purpose processors to specialized AI accelerators reflects a shift toward domain-specific computing where hardware and software are co-designed to optimize specific computational patterns). Sự tiến triển từ các CPU thông qua các GPU tới được chuyên biệt hóa các TPU,
các NPU, và quy mô-tấm wafer các hệ thống chứng minh cách nào việc hiểu khối lượng công việc các đặc điểm thúc đẩy
thuộc về kiến trúc sự đổi mới, việc tạo ra các cơ hội cho bậc-của-độ lớn hiệu suất các sự cải thiện
thông qua được nhắm mục tiêu sự chuyên môn hóa (The progression from CPUs through GPUs to specialized TPUs, NPUs, and wafer-scale systems demonstrates how understanding workload characteristics drives architectural innovation, creating opportunities for orders-of-magnitude performance improvements through targeted specialization).
Kỹ thuật các thách thức của AI sự gia tốc kéo dài nhiều các lớp của tính toán ngăn xếp, từ
thấp-cấp độ bộ nhớ hệ thống phân cấp sự tối ưu hóa tới cao-cấp độ trình biên dịch các sự biến đổi và thời gian chạy
sự phối hợp (The technical challenges of AI acceleration span multiple layers of the computing stack, from low-level memory hierarchy optimization to high-level compiler transformations and runtime orchestration). Bộ nhớ băng thông các giới hạn tạo ra các nút thắt cổ chai thứ mà yêu cầu được nhắm mục tiêu các kỹ thuật
giống như dữ liệu việc xếp ô gạch, hạt nhân sự hợp nhất, và nhận thức-hệ thống phân cấp việc lập lịch trình để vượt qua (Memory bandwidth limitations create bottlenecks that require targeted techniques like data tiling, kernel fusion, and hierarchy-aware scheduling to overcome). Việc ánh xạ thần kinh
mạng các sự tính toán tới phần cứng liên quan đến phức tạp các sự đánh đổi giữa khác nhau dữ liệu luồng các mẫu,
bộ nhớ sự phân bổ các chiến lược, và sự thực thi việc lập lịch trình các cách tiếp cận thứ mà phải cân bằng tính toán
tính hiệu quả với tài nguyên sự sử dụng (Mapping neural network computations to hardware involves complex trade-offs between different dataflow patterns, memory allocation strategies, and execution scheduling approaches that must balance computational efficiency with resource utilization). Nhiều-chip và được phân phối sự gia tốc mở rộng cùng logic
ra ngoài, việc thêm sự giao tiếp chi phí chung, bộ nhớ tính nhất quán, và khối lượng công việc sự phân vùng tới
cấp độ-hệ thống sự tối ưu hóa vấn đề (Multi-chip and distributed acceleration extend the same logic outward, adding communication overhead, memory coherence, and workload partitioning to the system-level optimization problem).
Chính Những điểm rút ra (Key Takeaways): Việc di chuyển dữ liệu tốn kém nhiều hơn hơn việc tính toán nó (Moving data costs more than computing it)
• Roofline mô hình xác định hiệu suất các nút thắt cổ chai: Việc vẽ đồ thị số học cường độ
chống lại thông lượng tiết lộ liệu các khối lượng công việc là bị ràng buộc-bộ nhớ (sự chú ý, các sự nhúng)
yêu cầu băng thông sự tối ưu hóa, hay bị ràng buộc-tính toán (cao-sự tái sử dụng các tích chập,
các GEMM) yêu cầu FLOP/s sự tối ưu hóa (The Roofline model identifies performance bottlenecks: Plotting arithmetic intensity against throughput reveals whether workloads are memory bound (attention, embeddings) requiring bandwidth optimization, or compute bound (high-reuse convolutions, GEMMs) requiring FLOP/s optimization).
11. Phần cứng Sự gia tốc (Hardware Acceleration)
639
• Bộ nhớ băng thông ràng buộc hiệu suất: GPU tính toán dung lượng đã phát triển các bậc
của độ lớn nhanh hơn hơn bộ nhớ băng thông trong qua hai thập kỷ (Memory bandwidth constrains performance: GPU compute capacity has grown orders of magnitude faster than memory bandwidth over the past two decades). Hầu hết suy luận
các khối lượng công việc là bị ràng buộc-bộ nhớ, việc làm cho dữ liệu sự di chuyển sự tối ưu hóa chính mối quan tâm (Most inference workloads are memory bound, making data movement optimization the primary concern).
• Phần cứng-phần mềm đồng-thiết kế ghép lại hiệu suất: Việc khớp thuật toán các mẫu với
thuộc về kiến trúc các khả năng (tâm thu các mảng cho dày đặc GEMM, thưa thớt các máy gia tốc cho được cắt tỉa
các mô hình) có thể tạo ra lớn các sự cải thiện và điển hình vượt trội hơn thô phần cứng
các sự nâng cấp (Hardware-software co-design compounds performance: Matching algorithm patterns to architectural capabilities (systolic arrays for dense GEMM, sparse accelerators for pruned models) can produce large improvements and typically outperforms raw hardware upgrades).
• Tensor Các lõi yêu cầu cụ thể các điều kiện: Một được hỗ trợ độ chính xác định dạng (TF32, BF16,
FP16, hoặc INT8 phụ thuộc trên kiến trúc), thích hợp tensor các chiều, và đủ
lô kích thước là cần thiết cho đỉnh sự sử dụng (Tensor Cores require specific conditions: A supported precision format (TF32, BF16, FP16, or INT8 depending on architecture), appropriate tensor dimensions, and sufficient batch size are necessary for peak utilization). Lô kích thước một cách trực tiếp ảnh hưởng số học cường độ
và xác định liệu các khối lượng công việc tiếp cận bị ràng buộc-tính toán chế độ (Batch size directly affects arithmetic intensity and determines whether workloads reach the compute-bound regime).
• Số học cường độ xác định sự tối ưu hóa chiến lược: Các hoạt động với thấp số học
cường độ (1–2 FLOP/byte, giống như LayerNorm) là bị ràng buộc-bộ nhớ; các hoạt động xung quanh 50–200
FLOP/byte, giống như các tích chập, dạng chân dang tay (straddle) hiện đại máy gia tốc sườn núi các điểm và trở thành
bị ràng buộc-tính toán chỉ khi sự tái sử dụng và việc xếp ô gạch đẩy chúng lên trên ngưỡng (Arithmetic intensity determines optimization strategy: Operations with low arithmetic intensity (1–2 FLOP/byte, like LayerNorm) are memory bound; operations around 50–200 FLOP/byte, like convolutions, straddle modern accelerator ridge points and become compute bound only when reuse and tiling push them above the threshold). Sườn núi
điểm (cho ví dụ, 153 FLOP/byte cho A100) đánh dấu sự chuyển tiếp (The ridge point (for example, 153 FLOP/byte for A100) marks the transition).
Các kỹ sư những người nội tâm hóa (internalize) Roofline mô hình và số học cường độ sự phân tích đạt được một chẩn đoán
bộ khung: khi suy luận chạy chậm hơn hơn được mong đợi, họ có thể ngay lập tức xác định liệu
nút thắt cổ chai nằm ở trong tính toán thông lượng, bộ nhớ băng thông, hay phần mềm chi phí chung, và sau đó
chọn thích hợp sự tối ưu hóa chiến lược (Engineers who internalize the Roofline model and arithmetic intensity analysis gain a diagnostic framework: when inference runs slower than expected, they can immediately determine whether the bottleneck lies in compute throughput, memory bandwidth, or software overhead, and then select the appropriate optimization strategy). Này cấp độ-các hệ thống sự hiểu biết biến đổi phần cứng
sự lựa chọn từ nhà cung cấp sự so sánh thành có nguyên tắc kỹ thuật (This systems-level understanding transforms hardware selection from vendor comparison into principled engineering).
Một máy gia tốc là dễ dàng để nhầm lẫn cho một nhanh hơn máy tính (An accelerator is easy to mistake for a faster computer). Nó là tốt hơn được hiểu như một cỗ máy được xây dựng
để di chuyển ít dữ liệu hơn mỗi hữu ích hoạt động, bởi vì chi phí nó chiến đấu là được cố định bởi vật lý; việc di chuyển một byte
mất xa nhiều hơn thời gian và năng lượng hơn việc tính toán trên nó (It is better understood as a machine built to move less data per useful operation, because the cost it fights is fixed by physics; moving a byte takes far more time and energy than computing on it). Mỗi kỹ thuật trong này chương (việc xếp ô gạch, hạt nhân
sự hợp nhất, bộ nhớ hệ thống phân cấp, tâm thu mảng) tồn tại để nâng cao số học cường độ, tỷ lệ của
sự tính toán trên dữ liệu sự di chuyển, và roofline là việc ghi chép sổ sách của đó duy nhất thực tế (Every technique in this chapter (tiling, kernel fusion, the memory hierarchy, the systolic array) exists to raise arithmetic intensity, the ratio of computation to data movement, and the roofline is the bookkeeping of that single fact). Không
chúng nào bãi bỏ chi phí; chúng chỉ chuyển vị trí nút thắt cổ chai giữa băng thông và tính toán (None of them repeals the cost; they only relocate the bottleneck between bandwidth and compute). Đây là
cỗ máy sự ràng buộc được làm cho cụ thể: máy gia tốc không thể làm cho một byte rẻ hơn để di chuyển, chỉ
đảm bảo rằng ít hơn các byte phải di chuyển cho mỗi kết quả đáng việc giữ lại (This is the machine constraint made concrete: the accelerator cannot make a byte cheaper to move, only ensure that fewer bytes must move for each result worth keeping).
Cái gì Tiếp theo: Từ sự tối ưu hóa tới sự xác nhận (What’s Next: From optimization to validation)
Chúng ta đã bây giờ tối ưu hóa đầy đủ D·A·M ngăn xếp: dữ liệu sự lựa chọn tối thiểu hóa huấn luyện các yêu cầu,
mô hình sự nén làm giảm thuật toán sự phức tạp, và phần cứng sự gia tốc tối đa hóa
cỗ máy thông lượng (We have now optimized the full D·A·M stack: data selection minimized training requirements, model compression reduced algorithmic complexity, and hardware acceleration maximized machine throughput). Sự tối ưu hóa mà không sự đo lường, tuy nhiên, là sự phỏng đoán (Optimization without measurement, however, is guesswork). Trong Chương
12, chúng ta di chuyển từ lý thuyết FLOPs tới được đo lường độ trễ, việc áp dụng roofline mô hình và
thống kê các phương pháp để xác nhận của chúng ta sự tối ưu hóa các tuyên bố chống lại thực tế (In Chapter 12, we move from theoretical FLOPs to measured latency, applying the roofline model and statistical methods to validate our optimization claims against reality).
Nghiên cứu Các câu hỏi: Cho xa hơn cuộc điều tra (Research Questions: For further inquiry)
• Nên roofline sự phân tích quyết định liệu để tối ưu hóa băng thông, tính toán, hay phần
mềm chi phí chung như thế nào? (How should roofline analysis decide whether to optimize bandwidth, compute, or software overhead?)
• Khi nào được chuyên biệt hóa phần cứng thất bại để vượt trội hơn một tổng quát-mục đích giải pháp thay thế? (When does specialized hardware fail to outperform a general-purpose alternative?)
• Cách nào việc xếp ô gạch, dữ liệu luồng, và sự hợp nhất chuyển vị trí bộ nhớ-sự di chuyển chi phí thay vì loại bỏ
nó? (How do tiling, dataflow, and fusion relocate memory-movement cost rather than eliminate it?)
• Cái gì bằng chứng nên hướng dẫn máy gia tốc sự lựa chọn qua thông lượng, băng thông, dung lượng,
năng lượng, chi phí, và tính di động? (What evidence should guide accelerator selection across throughput, bandwidth, capacity, energy, cost, and portability?)