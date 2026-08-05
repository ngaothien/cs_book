Các Ứng dụng (Applications)
> _
Các Hoạt động (Operations)
Việc Phục vụ (Serving)
Huấn luyện (Training)
∇
Các Mô hình (Models)
Các Bộ khung (Frameworks)
Phần cứng (Hardware)
Dữ liệu (Data)
12
Việc đo điểm chuẩn (Benchmarking)
12.1 ML Việc đo điểm chuẩn
Bộ khung (ML Benchmarking Framework)
12.2 Lịch sử Các nền tảng (Historical Foundations)
12.3 Hệ thống Việc đo điểm chuẩn
Các bộ phần mềm (System Benchmarking Suites)
12.4 Việc đo điểm chuẩn
Độ chi tiết (Benchmarking Granularity)
12.5 Điểm chuẩn Các thành phần (Benchmark Components)
12.6 Huấn luyện so với Suy luận (Training vs. Inference)
12.7 Huấn luyện Các điểm chuẩn (Training Benchmarks)
12.8 Suy luận Các điểm chuẩn (Inference Benchmarks)
12.9 Điện năng Sự đo lường
Các kỹ thuật (Power Measurement Techniques)
12.10 Việc đo điểm chuẩn Tốt nhất
Các thực hành (Benchmarking Best Practices)
12.11 Mô hình và Dữ liệu
Sự đánh giá (Model and Data Evaluation)
12.12 Sản xuất
Các sự xem xét (Production Considerations)
12.13 Các ngụy biện và Các cạm bẫy (Fallacies and Pitfalls)
12.14 Tóm tắt (Summary)
Mục đích (Purpose)
Làm thế nào có thể ML các hệ thống được so sánh một cách công bằng khi phần cứng, các mô hình, dữ liệu, và sự triển khai tất cả tương tác? (How can ML systems be compared fairly when hardware, models, data, and deployment all interact?)
Việc đo điểm chuẩn mang lại cùng nhau các quyết định đã được phát triển qua phần cứng việc nhắm mục tiêu, mô hình
sự nén, dữ liệu sự lựa chọn, và sự triển khai hành vi (Benchmarking brings together decisions already developed across hardware targeting, model compression, data selection, and deployment behavior). Mỗi quyết định đã cải thiện một chiều
(độ trễ, độ chính xác, thông lượng, hoặc năng lượng), nhưng một ML hệ thống là sản phẩm của tất cả những các chiều này
một cách đồng thời (Each decision improved one dimension (latency, accuracy, throughput, or energy), but an ML system is the product of all these dimensions simultaneously). Một được cắt tỉa mô hình chạy nhanh hơn trên một máy gia tốc nhưng chậm hơn trên một cái khác (A pruned model runs faster on one accelerator but slower on another). Một lớn hơn
lô kích thước cải thiện máy gia tốc sự sử dụng nhưng vi phạm một độ trễ dịch vụ-cấp độ thỏa thuận (A larger batch size improves accelerator utilization but violates a latency service-level agreement). Một biên
thiết bị quảng cáo đỉnh thông lượng thứ mà nhiệt sự điều chỉnh cắt đi một nửa dưới được duy trì các khối lượng công việc (An edge device advertises peak throughput that thermal throttling halves under sustained workloads). Các
thách thức là không phải liệu cá nhân các sự tối ưu hóa làm việc trong sự cô lập (chúng làm) mà cách nào để đo lường
của chúng được kết hợp hiệu ứng dưới các điều kiện thứ mà thực sự quan trọng (The challenge is not whether individual optimizations work in isolation (they do) but how to measure their combined effect under conditions that actually matter). Việc đo điểm chuẩn là kỷ luật (discipline) của
việc làm cho những các sự so sánh này mang tính hệ thống thay vì mang tính giai thoại (Benchmarking is the discipline of making such comparisons systematic rather than anecdotal). Nó yêu cầu việc xác định cái gì để đo lường
(độ chính xác, độ trễ, thông lượng, năng lượng), tại cái gì độ chi tiết (một đơn hạt nhân, một đầy đủ mô hình, một đầu-tới-
đầu đường ống), và dưới cái nào các điều kiện (lô kích thước, đầu vào sự phân phối, nhiệt trạng thái, đồng thời
tải) (It requires defining what to measure (accuracy, latency, throughput, energy), at what granularity (a single kernel, a full model, an end-to-end pipeline), and under which conditions (batch size, input distribution, thermal state, concurrent load)). Mà không này cấu trúc, các nhóm so sánh các con số thứ mà chưa bao giờ được đo lường trên cùng
các điều khoản, và các quyết định thứ mà trông có vẻ hợp lý trong một bảng tính sụp đổ dưới sản xuất các khối lượng công việc (Without this structure, teams compare numbers that were never measured on the same terms, and decisions that looked sound in a spreadsheet collapse under production workloads).
Những các chương đó đã tối ưu hóa mô hình, đã chọn dữ liệu, và đã khớp phần cứng; việc đo điểm chuẩn là
nơi những các sự tối ưu hóa đó là được xác nhận: nơi các tuyên bố gặp gỡ bằng chứng, và nơi khoảng cách giữa
lời hứa và sự phân phối là được định lượng một cách trung thực hoặc được khám phá một cách đau đớn trong sản xuất (Those chapters optimized the model, selected the data, and matched the hardware; benchmarking is where those optimizations are validated: where claims meet evidence, and where the gap between promise and delivery is quantified honestly or discovered painfully in production). Trong D·A·M các điều khoản,
việc đo điểm chuẩn là nơi đồng-thiết kế là được giữ để chịu trách nhiệm: sự đo lường kỷ luật thứ mà tiết lộ
liệu Dữ liệu, Thuật toán, và Cỗ máy đã thực sự được khớp hay đơn thuần được lắp ráp (In D·A·M terms, benchmarking is where co-design is held to account: the measurement discipline that reveals whether Data, Algorithm, and Machine were actually matched or merely assembled).
641
642
12.1 ML Việc đo điểm chuẩn Bộ khung (ML Benchmarking Framework)
Học tập Các mục tiêu (Learning Objectives)
• Giải thích việc đo điểm chuẩn như D·A·M sự xác nhận thứ mà kiểm tra liệu sự tối ưu hóa các tuyên bố giữ vững
dưới đại diện các điều kiện (Explain benchmarking as D·A·M validation that tests whether optimization claims hold under representative conditions)
• So sánh huấn luyện và suy luận các điểm chuẩn việc sử dụng thông lượng, độ trễ các phân vị (percentiles),
năng lượng, độ chính xác, và khối lượng công việc phạm vi (Compare training and inference benchmarks using throughput, latency percentiles, energy, accuracy, and workload scope)
• Chọn vi (micro), vĩ (macro), hoặc đầu-tới-đầu độ chi tiết dựa trên kỹ thuật quyết định việc đang
được kiểm tra (Select micro, macro, or end-to-end granularity based on the engineering decision being tested)
• Áp dụng được chuẩn hóa điểm chuẩn chạy các quy tắc để căn chỉnh các tập dữ liệu, các số liệu, phần cứng cấu
hình, và việc báo cáo (Apply standardized benchmark run rules to align datasets, metrics, hardware configuration, and reporting)
• Thiết kế điểm chuẩn các giao thức thứ mà kiểm soát điện năng các ranh giới, đầu vào các sự phân phối, lô
các kích thước, và thống kê sự phương sai (Design benchmark protocols that control power boundaries, input distributions, batch sizes, and statistical variance)
• Đánh giá mô hình và dữ liệu chất lượng với sự hiệu chuẩn (calibration), tính mạnh mẽ (robustness), tính đại diện, và
cấp độ-lát cắt (slice-level) các số liệu (Evaluate model and data quality with calibration, robustness, representativeness, and slice-level metrics)
• Chẩn đoán điểm chuẩn-sản xuất các khoảng cách được gây ra bởi sự trôi dạt (drift), nhiệt sự điều chỉnh, động tải,
và thầm lặng sự xuống cấp (Diagnose benchmark-production gaps caused by drift, thermal throttling, dynamic load, and silent degradation)
12.1 ML Việc đo điểm chuẩn Bộ khung (ML Benchmarking Framework)
Một
mô hình được lượng tử hóa tới INT8 có thể đo điểm chuẩn 2× nhanh hơn trên một tổng hợp khối lượng công việc nhưng cho thấy không
sự cải thiện dưới thực tế lưu lượng các mẫu với biến đổi đầu vào các kích thước và đồng thời các yêu cầu (A model quantized to INT8 may benchmark 2× faster on a synthetic workload but show no improvement under real traffic patterns with variable input sizes and concurrent requests).
Một được cắt tỉa mô hình có thể duy trì độ chính xác trên kiểm tra tập hợp nhưng thất bại trên biên các trường hợp điểm chuẩn
chưa bao giờ bao phủ (A pruned model may maintain accuracy on the test set but fail on edge cases the benchmark never covered). Mỗi sự tối ưu hóa đến với một lời hứa: dữ liệu sự lựa chọn hứa hẹn nhiều hiệu quả hơn
huấn luyện, mô hình sự nén hứa hẹn nhỏ hơn, nhanh hơn các mô hình, và phần cứng sự gia tốc hứa hẹn
cao hơn thông lượng (Every optimization arrives with a promise: data selection promises more efficient training, model compression promises smaller, faster models, and hardware acceleration promises higher throughput). Việc xác minh rằng những các tuyên bố này giữ vững trong sản xuất là chính nó một kỹ thuật kỷ luật (Verifying that these claims hold in production is itself an engineering discipline).
Việc đo điểm chuẩn là nơi vật lý các định luật những các chương đó đã thiết lập (sắt định luật, sự bảo toàn
của sự phức tạp, bộ nhớ bức tường) đối mặt với thực nghiệm thực tế (Benchmarking is where the physical laws those chapters established (the iron law, the conservation of complexity, the memory wall) face empirical reality). Điểm chuẩn-sản xuất khoảng cách là không phải một
sự thất bại của phương pháp luận mà là thước đo của bao nhiêu vật lý thực tế vượt quá của chúng ta các mô hình của nó (The benchmark-production gap is not a failure of methodology but the measure of how much physical reality exceeds our models of it).
Việc đóng đó khoảng cách bằng cách việc thiết kế các sự đo lường thứ mà dự đoán sản xuất hành vi với định lượng
độ trung thực là cốt lõi năng lực thứ mà phân biệt ML các hệ thống kỹ thuật từ ML nghiên cứu (Closing that gap by designing measurements that predict production behavior with quantitative fidelity is the core competency that distinguishes ML systems engineering from ML research).
Việc đo điểm chuẩn là kỷ luật của việc nói lên sự thật chức năng: thực hành thứ mà chuyển đổi lý thuyết các tuyên bố
thành được xác minh kỹ thuật kiến thức (Benchmarking is the discipline’s truth-telling function: the practice that converts theoretical claims into verified engineering knowledge).
ML việc đo điểm chuẩn hoạt động qua ba phụ thuộc lẫn nhau các chiều thứ mà ánh xạ một cách trực tiếp tới các thành
phần của bất kỳ được triển khai hệ thống nào (ML benchmarking operates across three interdependent dimensions that map directly to the components of any deployed system). Hệ thống việc đo điểm chuẩn đo lường liệu phần cứng cung cấp
được hứa hẹn hiệu suất dưới thực tế các khối lượng công việc hay liệu bộ nhớ băng thông sự bão hòa và
phần mềm sự phân phối chi phí chung xói mòn các khoản đạt được (System benchmarking measures whether the hardware delivers promised performance under realistic workloads or whether memory bandwidth saturation and software dispatch overhead erode the gains). Mô hình việc đo điểm chuẩn đo lường liệu sự tối ưu hóa
các kỹ thuật bảo tồn mô hình chất lượng qua đầy đủ đầu vào sự phân phối, không chỉ trên được tuyển chọn kiểm tra các tập hợp (Model benchmarking measures whether optimization techniques preserve model quality across the full input distribution, not just on curated test sets).
Dữ liệu việc đo điểm chuẩn đo lường liệu mô hình khái quát hóa tới thực-thế giới dữ liệu với tất cả của nó tiếng ồn,
sự thiên lệch, và thuộc về phân phối sự chuyển dịch (Data benchmarking measures whether the model generalizes to real-world data with all its noise, bias, and distributional shift). Mỗi chiều có thể một cách độc lập tiết lộ các vấn đề vô hình tới
những cái khác, và một hệ thống thứ mà vượt qua tất cả ba cung cấp xa mạnh mẽ hơn sự triển khai sự tự tin hơn một cái
được đánh giá dọc theo bất kỳ đơn trục nào (Each dimension can independently reveal problems invisible to the others, and a system that passes all three provides far stronger deployment confidence than one evaluated along any single axis).
Định nghĩa 12.1: Máy học việc đo điểm chuẩn (Machine learning benchmarking)
Máy Học Việc đo điểm chuẩn là thực nghiệm sự đo lường của một hệ thống của đầu-tới-đầu hiệu
suất trên đại diện ML các khối lượng công việc, được thiết kế để tách rời được tiếp thị đỉnh các thông số kỹ thuật
khỏi được duy trì thông lượng và độ trễ có thể đạt được dưới thực tế hoạt động các điều kiện (Machine Learning Benchmarking is the empirical measurement of a system’s end-to-end performance on representative ML workloads, designed to decouple marketed peak specifications from the sustained throughput and latency achievable under realistic operating conditions).
1. Ý nghĩa (Significance): Khoảng cách giữa đỉnh và được duy trì hiệu suất là lớn và về mặt cấu trúc
không thể tránh khỏi (The gap between peak and sustained performance is large and structurally unavoidable). Một A100 GPU cung cấp 312 TFLOP/s (BF16) tại đỉnh, nhưng sản xuất
transformer huấn luyện các lượt chạy điển hình duy trì 93.6 TFLOP/s–156 TFLOP/s (30 phần trăm–50 phần trăm
MFU), khoảng một 2–3.5× khoảng cách thứ mà tồn tại thậm chí trong một cách tối ưu được tinh chỉnh các hệ thống do bộ nhớ (An A100 GPU delivers 312 TFLOP/s (BF16) at peak, but production transformer training runs typically sustain 93.6 TFLOP/s–156 TFLOP/s (30 percent–50 percent MFU), about a 2–3.5× gap that exists even in optimally tuned systems due to memory)

12. Việc đo điểm chuẩn (Benchmarking)
643
các sự đình trệ (stalls), đường ống các bong bóng, và hạt nhân sự khởi chạy chi phí chung (stalls, pipeline bubbles, and kernel launch overhead). Việc đo điểm chuẩn định lượng này 𝜂hw
khoảng cách; nhà cung cấp thông số kỹ thuật các trang tính không (Benchmarking quantifies this 𝜂hw gap; vendor spec sheets do not).
2. Sự phân biệt (Distinction): Không giống như vi-các điểm chuẩn, thứ mà đo lường cá nhân hạt nhân hiệu suất
chẳng hạn như một tổng quát ma trận nhân (GEMM) tại đỉnh ma trận các chiều, ML các điểm chuẩn
đo lường đầy đủ ngăn xếp: dữ liệu việc tải, sự tiền xử lý, tiến (forward) bước, gradient sự tính toán,
trình tối ưu hóa bước, và điểm kiểm tra I/O—việc phơi bày các nút thắt cổ chai thứ mà cá nhân-thành phần
các điểm chuẩn sẽ không bao giờ tiết lộ (Unlike micro-benchmarks, which measure individual kernel performance such as a general matrix multiply (GEMM) at peak matrix dimensions, ML benchmarks measure the full stack: data loading, preprocessing, forward pass, gradient computation, optimizer step, and checkpoint I/O—exposing bottlenecks that individual-component benchmarks will never reveal).
3. Chung cạm bẫy (Common pitfall): Một thường xuyên sự quan niệm sai lầm là rằng điểm chuẩn các con số là ổn định các tài liệu
tham khảo (A frequent misconception is that benchmark numbers are stable references). Cả hai khối lượng công việc (mới mô hình các kiến trúc) và phần cứng (mới GPU
các thế hệ) tiến hóa, do đó một kết quả thứ mà dẫn đầu một điểm chuẩn dưới một phiên bản thường trở thành
đường cơ sở dưới một sau này phiên bản, việc làm cho năm-qua-năm các sự so sánh có ý nghĩa chỉ
khi điểm chuẩn phiên bản là được giữ cố định (Both the workload (new model architectures) and the hardware (new GPU generations) evolve, so a result that leads a benchmark under one version often becomes the baseline under a later version, making year-over-year comparisons meaningful only when the benchmark version is held constant).
Không giống như truyền thống các hệ thống nơi các điểm chuẩn đại diện cho cố định các thông số kỹ thuật, ML các điểm chuẩn
nắm bắt chỉ một ảnh chụp nhanh (snapshot) của một đang thay đổi thực tế (Unlike traditional systems where benchmarks represent fixed specifications, ML benchmarks capture only a snapshot of a shifting reality). Khoảng cách giữa đỉnh và được duy trì hiệu suất
được tài liệu hóa bên trên là không được cố định hoặc: nó thay đổi khi cả hai các khối lượng công việc và phần cứng các thế hệ tiến hóa,
việc làm cho bất kỳ đơn điểm chuẩn kết quả nào được đóng dấu-thời gian thay vì mang tính phổ quát (The gap between peak and sustained performance documented above is not fixed either: it shifts as both workloads and hardware generations evolve, making any single benchmark result time-stamped rather than universal).
Các Hệ thống Phối cảnh 12.1: Các điểm chuẩn như đang di chuyển các mục tiêu (Systems Perspective 12.1: Benchmarks as moving targets)
Trong truyền thống các hệ thống (cho ví dụ, SPEC CPU), điểm chuẩn là một cứng nhắc thông số kỹ thuật (In traditional systems (for example, SPEC CPU), the benchmark is a rigid specification). Một việc sắp xếp
thuật toán là đúng nếu nó sắp xếp danh sách (A sorting algorithm is correct if it sorts the list). Sự đúng đắn là tuyệt đối và không thay đổi (Correctness is absolute and unchanging). Trong ML các hệ thống,
điểm chuẩn là một mềm thông số kỹ thuật: sự đúng đắn là được định nghĩa bởi một hữu hạn tập hợp của các ví dụ (ImageNet),
và thế giới di chuyển (In ML systems, the benchmark is a soft specification: correctness is defined by a finite set of examples (ImageNet), and the world moves). Một mô hình thứ mà ghi điểm cao trên ImageNet có thể vẫn hoạt động kém trên người dùng
các bức ảnh được chụp các năm sau khi điểm chuẩn đã được tạo (A model that scores highly on ImageNet can still underperform on user photos taken years after the benchmark was created).
Trong máy tính kiến trúc, các kỹ sư thiết kế cho điểm chuẩn bởi vì điểm chuẩn đại
diện cho khối lượng công việc (In computer architecture, engineers design for the benchmark because the benchmark represents the workload). Trong ML kỹ thuật, việc thiết kế duy nhất cho điểm chuẩn là sự quá khớp (overfitting) (In ML engineering, designing solely for the benchmark is overfitting).
Tính mạnh mẽ đến từ việc công nhận rằng điểm chuẩn là chỉ một đại diện (proxy) cho một đang thay đổi thực tế (Robustness comes from acknowledging that the benchmark is only a proxy for a shifting reality).
Để làm cho này ba-chiều bộ khung cụ thể, chúng ta nối đất nó trong một đang chạy ví dụ thứ mà
luồn qua toàn bộ chương, việc quay lại tới nó một cách lặp lại khi chúng ta phát triển mỗi chiều (To make this three-dimensional framework concrete, we ground it in a running example that threads through the entire chapter, returning to it repeatedly as we develop each dimension). Mo-
bileNetV2 sự triển khai sự xác nhận kéo dài tất cả ba sự đánh giá các chiều, việc minh họa cách nào mỗi cái
tiết lộ các vấn đề những cái khác không thể (MobileNetV2 deployment validation spans all three evaluation dimensions, illustrating how each reveals problems the others cannot).
Ngọn hải đăng (Lighthouse) 12.1: MobileNetV2 sự triển khai sự xác nhận (MobileNetV2 deployment validation)
MobileNetV2 (được giới thiệu trong phần 6.1.1) phục vụ như ngọn hải đăng ví dụ cho việc xác nhận
hoàn chỉnh sự tối ưu hóa đường ống (MobileNetV2 (introduced in section 6.1.1) serves as the lighthouse example for validating the complete optimization pipeline). MobileNetV2 tinh chỉnh v1’s theo chiều sâu có thể phân tách thiết kế với
được đảo ngược các phần dư và tuyến tính các nút thắt cổ chai trong khi việc duy trì một tương tự tham số quy mô (Sandler
et al. 2018) (MobileNetV2 refines v1’s depthwise separable design with inverted residuals and linear bottlenecks while maintaining a similar parameter scale (Sandler et al. 2018)). Nó là ví dụ điển hình cho sự triển khai các thách thức nơi việc đo điểm chuẩn xác định thành công
hay thất bại: sự nén có thể làm giảm mô hình kích thước, phần cứng sự gia tốc có thể làm giảm suy luận
độ trễ, và chỉ việc đo điểm chuẩn có thể xác định liệu những các khoản đạt được đó sống sót đầy đủ sự triển khai
đường ống (It exemplifies the deployment challenges where benchmarking determines success or failure: compression can reduce model size, hardware acceleration can reduce inference latency, and only benchmarking can determine whether those gains survive the full deployment pipeline).
1. Mô hình sự nén (Chương 10): INT8 sự lượng tử hóa làm giảm này MobileNetV2 đã làm việc
ví dụ từ 14 MB tới 3.5 MB (4× sự nén) (Model compression (Chapter 10): INT8 quantization reduces this MobileNetV2 worked example from 14 MB to 3.5 MB (4× compression))
2. Phần cứng sự gia tốc (Chương 11): mang tính minh họa EdgeTPU kịch bản sử dụng 2 ms suy-
luận so với 15 ms trên CPU (Hardware acceleration (Chapter 11): the illustrative EdgeTPU scenario uses 2 ms inference vs. 15 ms on CPU)
3. Việc đo điểm chuẩn sự xác nhận: Xác minh đường ống phân phối trong thực tế (Benchmarking validation: Verify the pipeline delivers in practice)
Các phần thứ mà theo sau giải quyết một chiều của này sự xác nhận ngăn xếp tại một thời điểm, việc xây dựng
hướng tới một mang tính hệ thống phương pháp luận thứ mà cô lập EdgeTPU độ trễ từ sự tiền xử lý và
dữ liệu sự truyền tải chi phí chung, xác nhận INT8 sự lượng tử hóa bảo tồn độ chính xác trên biên các trường hợp chẳng hạn như

644
12.2 Lịch sử Các nền tảng (Historical Foundations)
1
Goodhart’s Định luật: Good-
hart (1984) đã phát biểu
bản gốc 1975 Ngân hàng của Eng-
land sự quan sát trên tiền-
tệ chính sách; Strathern (1997)
đã tổng quát hóa nó thành hình thức
được trích dẫn bên trên (Goodhart’s Law: Goodhart (1984) articulated the original 1975 Bank of England observation on monetary policy; Strathern (1997) generalized it into the form quoted above). Bản gốc
ngữ cảnh là kinh tế vĩ mô:
một khi một tiền tệ tập hợp
trở thành một chính thức chính sách mục-
tiêu, các ngân hàng đã thay đổi hành vi
để chơi trò chơi (game) số liệu, việc phá hủy
của nó mang tính dự đoán giá trị (The original context was macroeconomics: once a monetary aggregate became an official policy target, banks changed behavior to game the metric, destroying its predictive value). Trong ML,
cùng thất bại chế độ tái diễn
về mặt cấu trúc: BLEU thưởng n-
gram sự chồng chéo (Papineni et al.
2002), ImageNet thưởng hiệu-
suất trên một cố định hình ảnh sự phân-
phối (Deng et al. 2009;
Recht et al. 2019), và điểm-
chuẩn các bảng xếp hạng có thể khuyến-
khích cụ thể-tập hợp-kiểm tra sự tinh chỉnh (In ML, the same failure mode recurs structurally: BLEU rewards n-gram overlap (Papineni et al. 2002), ImageNet rewards performance on a fixed visual distribution (Deng et al. 2009; Recht et al. 2019), and benchmark leaderboards can incentivize test-set-specific tuning).
Thành phần tốc độ tăng tốc hiếm khi sống
sót như đầu-tới-đầu điểm chuẩn
tốc độ tăng tốc (Component speedup rarely survives as end-to-end benchmark speedup).
2
Điểm chuẩn (Benchmark): Từ việc khảo-
sát, nơi một “điểm chuẩn”
đã là một nằm ngang vết cắt trong đá
việc phục vụ như một cố định độ cao
tài liệu tham khảo (Benchmark: From surveying, where a “bench mark” was a horizontal cut in stone serving as a fixed elevation reference). Thuật ngữ đã đi vào
máy tính trong các năm 1970 để miêu-
tả được chuẩn hóa sự so-
sánh các điểm, nhưng việc khảo-
sát ẩn dụ mang theo một hệ-
thống bài học: giống như một độ-
cao sự đo lường là vô-
nghĩa mà không một được hiệu chuẩn
tài liệu tham khảo, một ML thông-
lượng con số là vô nghĩa
mà không được kiểm soát các khối lượng công việc,
nhiệt trạng thái, và độ chính xác
các cài đặt (The term entered computing in the 1970s to describe standardized comparison points, but the surveying metaphor carries a systems lesson: just as an elevation measurement is meaningless without a calibrated reference, an ML throughput number is meaningless without controlled workloads, thermal state, and precision settings).
bất thường ánh sáng, và kiểm tra rằng hiệu suất giữ vững trên thực-thế giới điện thoại thông minh các hình ảnh thay vì
chỉ ImageNet kiểm tra các hình ảnh (unusual lighting, and checks that performance holds on real-world smartphone images rather than only ImageNet test images).
Trước khi việc kiểm tra những các chiều này trong chi tiết, chúng ta phải thiết lập tư duy thứ mà tách biệt nghiêm ngặt
sự đánh giá khỏi gây hiểu lầm các số liệu (Before examining these dimensions in detail, we must establish the mindset that separates rigorous evaluation from misleading metrics). Ba nguyên tắc phân biệt hiệu quả những người thực hành (Three principles distinguish effective practitioners).
Đầu tiên, các điểm chuẩn là các đại diện, không phải sự thật (First, benchmarks are proxies, not truth). Mỗi điểm chuẩn đo lường cụ thể các điều kiện thứ mà có thể không
khớp mục tiêu sự triển khai (Every benchmark measures specific conditions that may not match the target deployment). Một hệ thống có thể đạt được cao mẫu thông lượng trong Ngoại tuyến chế độ (hàng loạt
thông lượng với tất cả các đầu vào có sẵn) và nhiều thấp hơn QPS trong Máy chủ chế độ (bị ràng buộc-độ trễ
các yêu cầu đến qua thời gian) (A system can achieve high sample throughput in Offline mode (bulk throughput with all inputs available) and much lower QPS in Server mode (latency-constrained requests arriving over time)). Quan trọng câu hỏi là luôn luôn cái gì điểm chuẩn không đo lường (The critical question is always what the benchmark does not measure).
Thứ hai, Goodhart’s Định luật áp dụng mọi nơi.1 “Khi một thước đo trở thành một mục tiêu, nó chấm dứt để
là một tốt thước đo.” (Second, Goodhart’s Law applies everywhere.1 “When a measure becomes a target, it ceases to be a good measure.”) Các nhóm thứ mà tối ưu hóa cho điểm chuẩn các xếp hạng thường tạo ra các hệ thống thứ mà
xuất sắc trong sự đánh giá nhưng thất bại trong sản xuất (Teams that optimize for benchmark rankings often produce systems that excel in evaluation but fail in production). Cụ thể-điểm chuẩn các sự tối ưu hóa thường xuyên làm giảm
các đặc điểm thứ mà quan trọng cho sự triển khai: tính mạnh mẽ, sự hiệu chuẩn, và tính hiệu quả (Benchmark-specific optimizations frequently degrade characteristics that matter for deployment: robustness, calibration, and efficiency).
Thứ ba, đầu-tới-đầu đánh bại thành phần các số liệu (Third, end-to-end beats component metrics). Các nhà cung cấp báo cáo thành phần độ trễ (5–10 ms cho
mô hình suy luận), nhưng sản xuất độ trễ bao gồm sự tiền xử lý, việc xếp hàng, và sự hậu xử lý
(50–100 ms tổng cộng) (Vendors report component latency (5–10 ms for model inference), but production latency includes preprocessing, queuing, and postprocessing (50–100 ms total)). Một 3× suy luận tốc độ tăng tốc được áp dụng tới một 10 ms mô hình giai đoạn bên trong một 50 ms đường ống
mang lại chỉ khoảng 1.2× đầu-tới-đầu sự cải thiện, hoặc tệ hơn nếu sự tối ưu hóa làm tăng bộ nhớ
áp lực (A 3× inference speedup applied to a 10 ms model stage inside a 50 ms pipeline yields only about 1.2× end-to-end improvement, or worse if the optimization increases memory pressure). Những các nguyên tắc này xuất hiện lại xuyên suốt việc đo điểm chuẩn phương pháp luận và là được kiểm tra
trong độ sâu trong phần 12.13 (These principles reappear throughout the benchmarking methodology and are examined in depth in section 12.13).
Việc biết cái gì để đo lường, tuy nhiên, là chỉ một nửa vấn đề (Knowing what to measure, however, is only half the problem). Việc đo lường một cách không chính xác (với
sai các khối lượng công việc, bị thiên lệch các đường cơ sở, hoặc không được kiểm soát các biến số) tạo ra các con số thứ mà cảm thấy chính xác nhưng
làm lạc hướng các quyết định (Measuring incorrectly (with the wrong workloads, biased baselines, or uncontrolled variables) produces numbers that feel precise but mislead decisions). Lịch sử của máy tính việc đo điểm chuẩn là ngập tràn (littered) với các ví dụ của về mặt kỹ thuật
lành mạnh các số liệu được áp dụng với bị lỗi phương pháp luận, từ được chơi trò chơi-bởi-trình biên dịch Whetstone các điểm số tới được chọn-
lọc-cẩn thận (cherry-picked) GPU các điểm chuẩn thứ mà dự đoán không có gì về được duy trì các khối lượng công việc (The history of computing benchmarking is littered with examples of technically sound metrics applied with flawed methodology, from compiler-gamed Whetstone scores to cherry-picked GPU benchmarks that predict nothing about sustained workloads). Việc hiểu cách nào
sự đo lường phương pháp luận đã tiến hóa, và nơi nó đã thất bại, là cần thiết cho việc thiết kế các điểm chuẩn thứ mà
phân biệt xác thực các sự cải thiện khỏi sự đo lường các đồ tạo tác (Understanding how measurement methodology evolved, and where it failed, is essential for designing benchmarks that distinguish genuine improvements from measurement artifacts).
Lịch sử các nền tảng của việc đo điểm chuẩn2 quan trọng bởi vì chúng phơi bày sự xác nhận các thất bại
thứ mà vẫn tái diễn trong ML: được tối ưu hóa các số liệu thứ mà dừng việc dự đoán thực tế các khối lượng công việc, phần cứng các con số thứ mà
bỏ qua được duy trì hoạt động trạng thái, và mô hình các điểm số thứ mà bỏ lỡ sự triển khai chi phí (The historical foundations of benchmarking2 matter because they expose the validation failures that still recur in ML: optimized metrics that stop predicting real workloads, hardware numbers that ignore sustained operating state, and model scores that miss deployment cost). Cùng sự xác nhận
chuỗi chi phối hiện đại thực hành: đầu tiên xác minh rằng phần cứng cung cấp được hứa hẹn hiệu suất, sau đó
xác minh rằng mô hình và dữ liệu các sự tối ưu hóa được xây dựng bên trên đó phần cứng cung cấp của chúng được hứa hẹn các khoản đạt được (The same validation sequence governs modern practice: first verify that hardware delivers promised performance, then verify that the model and data optimizations built atop that hardware deliver their promised gains).
12.2 Lịch sử Các nền tảng (Historical Foundations)
Năm 1976, khi Whetstone đã trở thành một của đầu tiên được chuẩn hóa máy tính các điểm chuẩn, các nhà cung cấp
ngay lập tức bắt đầu việc tối ưu hóa của họ các trình biên dịch một cách cụ thể cho của nó dấu phẩy-động các bài kiểm tra—việc tạo ra
ấn tượng các con số thứ mà dự đoán không có gì về thực tế ứng dụng hiệu suất (In 1976, when Whetstone became one of the first standardized computing benchmarks, vendors immediately began optimizing their compilers specifically for its floating-point tests—producing impressive numbers that predicted nothing about real application performance). Này việc chơi trò chơi (gaming)
vấn đề đã làm khổ mỗi thế hệ của các điểm chuẩn kể từ (This gaming problem has plagued every generation of benchmarks since). Việc hiểu tại sao ML việc đo điểm chuẩn
yêu cầu của chúng ta ba-chiều cách tiếp cận đòi hỏi việc theo dõi cách nào sự đo lường các phương pháp luận đã tiến hóa,
và thường đã thất bại, qua nhiều thập kỷ của máy tính lịch sử (Understanding why ML benchmarking requires our three-dimensional approach demands tracing how measurement methodologies evolved, and often failed, over decades of computing history). Mỗi thế hệ của các điểm chuẩn đã nổi lên từ
các hạn chế của của nó các người tiền nhiệm, việc dạy các bài học thứ mà một cách trực tiếp thông tin hiện đại ML sự đánh giá (Each generation of benchmarks emerged from the limitations of its predecessors, teaching lessons that directly inform modern ML evaluation).
Trước khi đó lịch sử bắt đầu, một ranh giới điều kiện quan trọng: một điểm chuẩn là hữu ích chỉ khi nó
đặt tên lớp cái mà của nó tuyên bố nó xác nhận (Before that history begins, one boundary condition matters: a benchmark is useful only when it names the layer whose claim it validates).
Các Hệ thống Phối cảnh 12.2: Việc đo điểm chuẩn như chéo-lớp bằng chứng (Systems Perspective 12.2: Benchmarking as cross-layer evidence)
Một ML điểm chuẩn là có ý nghĩa chỉ khi nó nhận diện cái nào lớp của hệ thống đang
được xác nhận (An ML benchmark is meaningful only when it identifies which layer of the system is being validated). Dữ liệu sự lựa chọn các số liệu chẳng hạn như hiệu suất-mỗi-dữ liệu (PPD), diện tích dưới học tập
đường cong (AULC), và dữ liệu sự nén tỷ lệ (DCR), tất cả được phát triển trong Chương 9, đo lường liệu
ít hơn các ví dụ có thể bảo tồn học tập tín hiệu (Data selection metrics such as performance-per-data (PPD), area under the learning curve (AULC), and data compression ratio (DCR), all developed in Chapter 9, measure whether fewer examples can preserve learning signal). Sự nén các số liệu (Chương 10) đo lường
liệu ít hơn các tham số hay thấp hơn độ chính xác bảo tồn chất lượng (Compression metrics (Chapter 10) measure whether fewer parameters or lower precision preserve quality). Phần cứng các số liệu chẳng hạn như
roofline vị trí và TOPS/W (Chương 11) đo lường liệu cỗ máy thực thi khối lượng công-
việc một cách hiệu quả (Hardware metrics such as roofline position and TOPS/W (Chapter 11) measure whether the machine executes the workload efficiently). Hệ thống các điểm chuẩn trong phần 12.3.2 thông qua phần 12.9.4 kết nối những
các lớp này bằng cách việc kiểm tra liệu cục bộ các sự cải thiện sống sót trong một đầu-tới-đầu khối lượng công việc (The system benchmarks in section 12.3.2 through section 12.9.4 connect these layers by testing whether local improvements survive in an end-to-end workload).

12. Việc đo điểm chuẩn (Benchmarking)
645
3
Whetstone và LIN-
PACK: Whetstone (Curnow
và Wichmann 1976) đã được
đặt tên sau English Elec-
tric cơ sở trong Whetstone, Le-
icestershire, nơi bản gốc
ALGOL trình biên dịch đã được
xây dựng;
LINPACK (Dongarra
et al.
1979) đã là Jack Don-
garra’s điểm chuẩn cho dày đặc
tuyến tính các hệ thống, sau này được áp dụng
bởi Top500 danh sách năm 1993.
Cả hai đã đo lường một đơn hoạt-
động loại rất hẹp đến nỗi
các trình biên dịch có thể được tinh chỉnh để
chơi trò chơi kết quả: Whetstone’s
dấu phẩy-động các vòng lặp đã trở thành một
bài kiểm tra của trình biên dịch sự tối ưu hóa
thay vì phần cứng hiệu-
suất. ML việc đo điểm chuẩn thừa-
hưởng cùng lỗ hổng:
đơn-mô hình các điểm chuẩn
có thể bị chơi trò chơi thông qua cụ thể-mô hình
hạt nhân sự tinh chỉnh, thứ mà
là tại sao MLPerf yêu cầu nhiều
các khối lượng công việc kéo dài thị giác,
ngôn ngữ, và sự khuyến-
nghị (Dongarra et al.
2003) (Whetstone and LINPACK: Whetstone (Curnow and Wichmann 1976) was named after the English Electric facility in Whetstone, Leicestershire, where the original ALGOL compiler was built; LINPACK (Dongarra et al. 1979) was Jack Dongarra’s benchmark for dense linear systems, later adopted by the Top500 list in 1993. Both measured a single operation type so narrowly that compilers could be tuned to game the result: Whetstone’s floating-point loops became a test of compiler optimization rather than hardware performance. ML benchmarking inherited the same vulnerability: single-model benchmarks can be gamed through model-specific kernel tuning, which is why MLPerf requires multiple workloads spanning vision, language, and recommendation (Dongarra et al. 2003)).
4
MLPerf: Được thành lập năm 2018
bởi các nhà nghiên cứu từ Google,
NVIDIA, Intel, Harvard, Stan-
ford, và UC Berkeley, tên
kết hợp “ML” với
“Perf” (hiệu suất), việc lặp lại
SPEC’s
việc đo điểm chuẩn
truyền thống (MLPerf: Founded in 2018 by researchers from Google, NVIDIA, Intel, Harvard, Stanford, and UC Berkeley, the name combines “ML” with “Perf” (performance), echoing SPEC’s benchmarking tradition).
MLPerf’s thiết kế
các nguyên tắc—đại diện
các khối lượng công việc,
đầy đủ-hệ thống
sự đo lường,
và
mở
sự đệ trình—trực tiếp giải quyết
việc
chơi trò chơi
thứ mà
đã làm khổ
Whetstone
và
LINPACK:
các nhà cung cấp những người có thể trước
đây
báo cáo
đỉnh
hạt nhân
thông lượng trên được chọn-lọc-cẩn thận
vấn đề
các kích thước
phải
bây giờ
báo cáo
đầu-tới-đầu
hệ thống
hiệu suất trên được chuẩn hóa
các tác vụ (Mattson et al.
2020;
Reddi et al. 2019) (MLPerf’s design principles—representative workloads, full-system measurement, and open submission—directly address the gaming that plagued Whetstone and LINPACK: vendors who could previously report peak kernel throughput on cherry-picked problem sizes must now report end-to-end system performance on standardized tasks (Mattson et al. 2020; Reddi et al. 2019)).
5
SPEC Năng lượng: Được giới thiệu
năm 2007, SPEC Năng lượng đo-
lường hiệu suất mỗi watt
qua 11 tải các cấp độ từ nhàn rỗi
(0 phần trăm) thông qua 100 phần-
trăm trong 10 phần trăm các gia số
(Lange 2009). Này độ chi tiết
quan trọng cho ML việc phục vụ: suy-
luận các khối lượng công việc hiếm khi duy trì
100 phần trăm tải, và các máy chủ
thứ mà hiệu quả tại đỉnh nhưng
lãng phí tại một phần tải thổi phồng
năng lượng chi phí của thực-thế giới
sự triển khai (SPEC Power: Introduced in 2007, SPEC Power measures performance per watt across 11 load levels from idle (0 percent) through 100 percent in 10 percent increments (Lange 2009). This granularity matters for ML serving: inference workloads rarely sustain 100 percent load, and servers that are efficient at peak but wasteful at partial load inflate the energy cost of real-world deployment).
Đó chéo-lớp vai trò giải thích tại sao điểm chuẩn lịch sử quan trọng: mỗi thế hệ của hiệu suất
sự đo lường đã tiến bộ khi những người thực hành đã khám phá rằng trước đó phương pháp đã thất bại để dự đoán
thực-thế giới hành vi (That cross-layer role explains why benchmark history matters: each generation of performance measurement advanced when practitioners discovered that the previous method failed to predict real-world behavior). Sự tiến hóa từ đơn giản hiệu suất các số liệu tới ML việc đo điểm chuẩn tiết lộ
ba phương pháp luận các sự chuyển dịch (The evolution from simple performance metrics to ML benchmarking reveals three methodological shifts).
12.2.1 Hiệu suất các điểm chuẩn (Performance benchmarks)
Các sớm nhất máy tính các điểm chuẩn đã tiết lộ một vấn đề thứ mà làm khổ sự đánh giá tới này ngày: điểm chuẩn
việc chơi trò chơi (The earliest computing benchmarks revealed a problem that plagues evaluation to this day: benchmark gaming). Máy tính lớn các điểm chuẩn giống như Whetstone (Curnow and Wichmann 1976) và LINPACK3
(Dongarra et al. 1979) đã đo lường được cô lập các hoạt động (dấu phẩy-động thông lượng, ma trận giải quyết tốc độ),
và các nhà cung cấp nhanh chóng đã học để tối ưu hóa một cách cụ thể cho những các hẹp bài kiểm tra này thay vì cho thực tế
hiệu suất (Mainframe benchmarks like Whetstone (Curnow and Wichmann 1976) and LINPACK3 (Dongarra et al. 1979) measured isolated operations (floating-point throughput, matrix solve speed), and vendors quickly learned to optimize specifically for these narrow tests rather than for practical performance). Việc dẫn đến các con số đã nhìn ấn tượng trên giấy nhưng đã dự đoán ít về cách nào
các hệ thống đã hoạt động trên thực tế các khối lượng công việc (The resulting numbers looked impressive on paper but predicted little about how systems performed on actual workloads). SPEC CPU (1989) đã phá vỡ này chu kỳ bằng cách việc sử dụng một bộ phần mềm của
di động, định hướng-ứng dụng các chương trình thay vì một đơn tổng hợp hạt nhân (Dixit 1993) (SPEC CPU (1989) broke this cycle by using a suite of portable, application-oriented programs rather than a single synthetic kernel (Dixit 1993)). Này
bài học một cách trực tiếp định hình ML việc đo điểm chuẩn: sự tối ưu hóa các tuyên bố từ Chương 10 yêu cầu sự xác nhận
trên đại diện các tác vụ, và MLPerf’s sự bao gồm của thực các mô hình giống như ResNet-50 và BERT đảm bảo
các điểm chuẩn nắm bắt sự triển khai sự phức tạp thay vì được lý tưởng hóa kiểm tra các trường hợp (This lesson directly shapes ML benchmarking: optimization claims from Chapter 10 require validation on representative tasks, and MLPerf’s inclusion of real models like ResNet-50 and BERT ensures benchmarks capture deployment complexity rather than idealized test cases).
Khi sự triển khai các ngữ cảnh đa dạng hóa, một thứ hai hạn chế đã nổi lên: đơn-số liệu sự đánh giá đã chứng tỏ
không đủ (As deployment contexts diversified, a second limitation emerged: single-metric evaluation proved inadequate). Đồ họa các điểm chuẩn đã bắt đầu việc đo lường việc kết xuất (rendering) chất lượng song song khung tỷ lệ; di động
các điểm chuẩn đã thêm pin tuổi thọ như một đồng-bình đẳng mối quan tâm với hiệu suất (Graphics benchmarks began measuring rendering quality alongside frame rate; mobile benchmarks added battery life as a co-equal concern with performance). Đa-mục tiêu các thách-
thức từ Chương 1 (việc cân bằng độ chính xác, độ trễ, và năng lượng) biểu hiện một cách trực tiếp trong ML sự đánh giá,
nơi không đơn số liệu nào nắm bắt sự triển khai khả năng tồn tại (The multi-objective challenges from Chapter 1 (balancing accuracy, latency, and energy) manifest directly in ML evaluation, where no single metric captures deployment viability).
Một thứ ba sự chuyển dịch đã xảy ra khi được phân phối máy tính đã tiết lộ rằng cấp độ-thành phần sự tối ưu hóa
thất bại để dự đoán cấp độ-hệ thống hiệu suất (A third shift occurred when distributed computing revealed that component-level optimization fails to predict system-level performance). Một CPU điểm chuẩn không thể dự đoán cụm thông lượng khi
mạng sự giao tiếp chiếm ưu thế (A CPU benchmark cannot predict cluster throughput when network communication dominates). ML huấn luyện tương tự phụ thuộc trên sự tác động qua lại của máy gia tốc
tính toán (Chương 11), dữ liệu các đường ống, gradient sự đồng bộ hóa, và lưu trữ thông lượng (ML training similarly depends on the interplay of accelerator compute (Chapter 11), data pipelines, gradient synchronization, and storage throughput). MLPerf
đánh giá hoàn chỉnh các quy trình công việc, việc nhận ra rằng hiệu suất nổi lên từ thành phần các sự tương tác,
không phải từ các thành phần trong sự cô lập (MLPerf evaluates complete workflows, recognizing that performance emerges from component interactions, not from components in isolation).
DAWNBench (Coleman et al. 2019) đã nổi lên như một sớm ML điểm chuẩn thứ mà đã tiên phong thời gian-tới-
độ chính xác sự đánh giá, một cách trực tiếp việc ảnh hưởng MLPerf’s phương pháp luận cho việc đo lường huấn luyện tính hiệu quả (DAWNBench (Coleman et al. 2019) emerged as an early ML benchmark that pioneered time-to-accuracy evaluation, directly influencing MLPerf’s methodology for measuring training efficiency).
Những các bài học này đạt đến đỉnh cao (culminate) trong MLPerf4 (2018), thứ mà tổng hợp đại diện các khối lượng công việc, đa-
mục tiêu sự đánh giá, và được tích hợp sự đo lường trong khi việc giải quyết cụ thể-ML các thách thức (Mattson
et al. 2020; Reddi et al. 2019) (These lessons culminate in MLPerf4 (2018), which synthesizes representative workloads, multi-objective evaluation, and integrated measurement while addressing ML-specific challenges (Mattson et al. 2020; Reddi et al. 2019)).
12.2.2 Năng lượng các điểm chuẩn (Energy benchmarks)
Đa-mục tiêu sự đánh giá mô hình tự nhiên đã mở rộng tới năng lượng tính hiệu quả khi máy tính
đa dạng hóa vượt ra ngoài các máy tính lớn với ít bị ràng buộc điện năng các ngân sách hơn (The multi-objective evaluation paradigm naturally extended to energy efficiency as computing diversified beyond mainframes with less constrained power budgets). Di động các thiết bị đã yêu cầu
pin tuổi thọ sự tối ưu hóa, trong khi quy mô-nhà kho các hệ thống đã đối mặt với năng lượng các chi phí cạnh tranh với phần cứng
các chi phí (Mobile devices demanded battery life optimization, while warehouse-scale systems faced energy costs rivaling hardware expenses). Này sự chuyển dịch đã thiết lập năng lượng như một hạng-nhất số liệu song song hiệu suất, việc sinh ra
các điểm chuẩn giống như SPEC Năng lượng5 cho các máy chủ và Green5006 cho các siêu máy tính (This shift established energy as a first-class metric alongside performance, spawning benchmarks like SPEC Power5 for servers and Green5006 for supercomputers).
Đa dạng khối lượng công việc các mẫu và hệ thống các cấu hình tiếp tục để thách thức điện năng việc đo điểm chuẩn
qua máy tính các môi trường (Diverse workload patterns and system configurations continue to challenge power benchmarking across computing environments). MLPerf Năng lượng (MLCommons 2024b) giải quyết điều này với được chuyên biệt hóa
các phương pháp luận cho việc đo lường năng lượng tác động của máy học các khối lượng công việc, việc phản ánh
năng lượng tính hiệu quả’s trung tâm vai trò trong AI hệ thống thiết kế (MLPerf Power (MLCommons 2024b) addresses this with specialized methodologies for measuring the energy impact of machine learning workloads, reflecting energy efficiency’s central role in AI system design).
Năng lượng việc đo điểm chuẩn mở rộng vượt ra ngoài phần cứng điện năng sự đo lường để bao gồm thuật toán
tính hiệu quả (Energy benchmarking extends beyond hardware power measurement to include algorithmic efficiency). Mô hình sự nén các kỹ thuật (việc cắt tỉa, sự lượng tử hóa, kiến thức sự chưng cất) có thể làm giảm
năng lượng bằng cách việc thay đổi công việc một hệ thống thực hiện, không chỉ bằng cách việc thay đổi phần cứng thứ mà thực hiện
nó (Model compression techniques (pruning, quantization, knowledge distillation) can reduce energy by changing the work a system performs, not only by changing the hardware that performs it). Họ-MobileNet các kiến trúc sử dụng theo chiều sâu có thể phân tách các tích chập và liên quan thiết kế các sự lựa chọn
để làm giảm sự tính toán so với nặng hơn CNN các đường cơ sở chẳng hạn như ResNet (Howard et al. 2017;
Sandler et al. 2018; He et al. 2016a) (MobileNet-family architectures use depthwise separable convolutions and related design choices to reduce computation relative to heavier CNN baselines such as ResNet (Howard et al. 2017; Sandler et al. 2018; He et al. 2016a)). Những các kỹ thuật này, được chi tiết hóa trong Chương 10, thiết lập rằng nhận thức-
năng lượng việc đo điểm chuẩn phải đánh giá thuật toán tính hiệu quả song song phần cứng điện năng sự tiêu thụ;
phần 10.4.1.1 định lượng cụ thể năng lượng sự cố định (breakdown) của INT8 so với FP32 (These techniques, detailed in Chapter 10, establish that energy-aware benchmarking must evaluate algorithmic efficiency alongside hardware power consumption; section 10.4.1.1 quantifies the specific energy breakdown of INT8 vs. FP32). Khi AI các hệ thống mở rộng quy mô, này
bài học trở thành trung tâm cho bền vững máy tính các thực hành (As AI systems scale, this lesson becomes central to sustainable computing practices).

646
12.2 Lịch sử Các nền tảng (Historical Foundations)
6
Green500: Được bắt đầu năm 2007
như một đối tác của Top500,
Green500 xếp hạng các hệ thống theo
FLOP/s mỗi watt thay vì
thô hiệu suất (Feng and
Cameron 2007) (Green500: Started in 2007 as a counterpart to the Top500, Green500 ranks systems by FLOP/s per watt rather than raw performance (Feng and Cameron 2007)). Của nó bài học cho
ML các hệ thống là mang tính phương-
pháp luận: hiệu quả-chi phí nhất
huấn luyện cụm là không nhất-
thiết cái nhanh nhất, mà hệ thống
cái mà cung cấp hữu ích công việc
mỗi watt dưới khối lượng công việc
và sự đo lường ranh giới
thứ mà quan trọng (Its lesson for ML systems is methodological: the most cost-effective training cluster is not necessarily the fastest one, but the system that delivers useful work per watt under the workload and measurement boundary that matter).
12.2.3 Cụ thể-miền các điểm chuẩn (Domain-specific benchmarks)
Khi máy tính đa dạng hóa vượt ra ngoài tổng quát-mục đích các máy chủ, chung các điểm chuẩn đã chứng tỏ không đủ
cho được chuyên biệt hóa các miền (As computing diversified beyond general-purpose servers, generic benchmarks proved inadequate for specialized domains). Ba thể loại của sự chuyên môn hóa đã thúc đẩy này sự tiến hóa, mỗi cái phơi bày
sự đo lường các chiều thứ mà tổng quát-mục đích các điểm chuẩn không thể giải quyết (Three categories of specialization drove this evolution, each exposing measurement dimensions that general-purpose benchmarks could not address).
Sự triển khai các sự ràng buộc định hình cốt lõi số liệu các ưu tiên (Deployment constraints shape core metric priorities). Dữ liệu trung tâm các khối lượng công việc tối ưu hóa cho thông-
lượng với quy mô-giá đỡ và cụm điện năng các ngân sách, trong khi di động AI hoạt động bên trong chặt chẽ thiết bị nhiệt
các phong bì, và IoT các thiết bị yêu cầu quy mô-milliwatt hoạt động (Data center workloads optimize for throughput with rack- and cluster-scale power budgets, while mobile AI operates within tight device thermal envelopes, and IoT devices require milliwatt-scale operation). Những các sự ràng buộc này, được bắt rễ trong tính hiệu quả
các nguyên tắc từ Chương 1, xác định liệu các điểm chuẩn ưu tiên tổng thông lượng hay năng lượng mỗi
hoạt động (These constraints, rooted in efficiency principles from Chapter 1, determine whether benchmarks prioritize total throughput or energy per operation).
Ứng dụng các yêu cầu sau đó áp đặt chức năng và mang tính quy định các sự ràng buộc vượt ra ngoài thô hiệu-
suất (Application requirements then impose functional and regulatory constraints beyond raw performance). Chăm sóc sức khỏe AI đòi hỏi tính có thể diễn giải các số liệu song song độ chính xác; tài chính các hệ thống có thể
yêu cầu rất thấp độ trễ với kiểm toán sự tuân thủ; tự trị các phương tiện cần then chốt-an toàn độ tin cậy
và chính thức chức năng-an toàn sự xác nhận (Healthcare AI demands interpretability metrics alongside accuracy; financial systems may require very low latency with audit compliance; autonomous vehicles need safety-critical reliability and formal functional-safety validation). Những các yêu cầu này mở rộng sự đánh giá vượt ra ngoài truyền thống
hiệu suất các số liệu; Chương 15 sau đó hệ thống hóa có trách nhiệm-kỹ thuật các nguyên tắc đằng sau
sự công bằng, tính có thể diễn giải, và sự tuân thủ (These requirements extend evaluation beyond traditional performance metrics; Chapter 15 later systematizes the responsible-engineering principles behind fairness, interpretability, and compliance).
Hoạt động các điều kiện xác định thực-thế giới khả năng tồn tại (Operational conditions determine real-world viability). Tự trị các phương tiện đối mặt với rộng nhiệt-
độ các phạm vi và bị xuống cấp cảm biến các đầu vào; dữ liệu các trung tâm xử lý lớn đồng thời yêu cầu các khối lượng
với mạng các lỗi; công nghiệp IoT chịu đựng dài các sự triển khai mà không sự bảo trì (Autonomous vehicles face wide temperature ranges and degraded sensor inputs; data centers handle large concurrent request volumes with network faults; industrial IoT endures long deployments without maintenance). Phần cứng
các khả năng từ Chương 11 chỉ cung cấp giá trị khi được xác nhận dưới những các điều kiện này (The hardware capabilities from Chapter 11 only deliver value when validated under these conditions).
Máy học là ví dụ điển hình này sự chuyển tiếp tới cụ thể-miền sự đánh giá (Machine learning exemplifies this transition to domain-specific evaluation). Truyền thống CPU và
GPU các điểm chuẩn chứng tỏ không đủ cho việc đánh giá ML các khối lượng công việc, thứ mà liên quan đến phức tạp các sự tương tác
giữa sự tính toán, bộ nhớ băng thông, và dữ liệu sự di chuyển các mẫu (Traditional CPU and GPU benchmarks prove insufficient for assessing ML workloads, which involve complex interactions between computation, memory bandwidth, and data movement patterns). MLPerf cung cấp được chuẩn-
hóa hiệu suất sự đo lường cho máy học các mô hình qua những các thể loại này: MLPerf
Huấn luyện giải quyết dữ liệu trung tâm sự triển khai các sự ràng buộc với nhiều-nút sự mở rộng quy mô các điểm chuẩn (Matt-
son et al. 2020), MLPerf Suy luận đánh giá then chốt-độ trễ ứng dụng các yêu cầu qua máy chủ tới
biên các sự triển khai (Reddi et al. 2019), MLPerf Nhỏ bé (Tiny) đánh giá cực kỳ-bị ràng buộc hoạt động các điều kiện
cho vi điều khiển các sự triển khai (C. Banbury et al. 2021), và một chéo-cắt MLPerf Năng lượng theo dõi
đo lường năng lượng tính hiệu quả dưới mỗi của những các chế độ này (MLPerf provides standardized performance measurement for machine learning models across these categories: MLPerf Training addresses data center deployment constraints with multi-node scaling benchmarks (Mattson et al. 2020), MLPerf Inference evaluates latency-critical application requirements across server to edge deployments (Reddi et al. 2019), MLPerf Tiny assesses ultra-constrained operational conditions for microcontroller deployments (C. Banbury et al. 2021), and a cross-cutting MLPerf Power track measures energy efficiency under each of these regimes). Việc đọc bảng 12.1 xuống của nó sự ràng buộc
cột cho thấy ràng buộc giới hạn đang thắt chặt khi sự triển khai quy mô thu hẹp: nhiều-nút kết nối
băng thông trong dữ liệu trung tâm nhường đường tới độ trễ các SLA tại máy chủ và biên, sau đó tới cực kỳ-
thấp-điện năng hoạt động với kilobytes của bộ nhớ tại vi điều khiển (Reading table 12.1 down its constraint column shows the binding limit tightening as deployment scale shrinks: multi-node interconnect bandwidth in the data center gives way to latency SLAs at the server and edge, then to ultra-low-power operation with kilobytes of memory at the microcontroller). Cùng ba-thể loại
bộ khung, được áp dụng tới mỗi quy mô, tạo ra một bộ phần mềm của cái mà các số liệu theo dõi cái gì thực sự giới hạn
hệ thống tại đó quy mô thay vì một đơn mang tính phổ quát điểm số (The same three-category framework, applied to each scale, produces a suite whose metrics track what actually limits the system at that scale rather than a single universal score).
Bảng 12.1: MLPerf Điểm chuẩn Bộ phần mềm Các biến thể (Variants): Mỗi biến thể giải quyết một khác nhau sự triển khai ngữ cảnh, từ quy mô-trung tâm-dữ liệu
huấn luyện tới cực kỳ-bị ràng buộc vi điều khiển suy luận, việc nhắm mục tiêu cụ thể hoạt động các sự ràng buộc và việc đo lường các số liệu có liên quan
tới của nó sự triển khai kịch bản (Table 12.1: MLPerf Benchmark Suite Variants: Each variant addresses a different deployment context, from data-center-scale training to ultra-constrained microcontroller inference, targeting specific operational constraints and measuring metrics relevant to its deployment scenario).
MLPerf Biến thể (Variant)
Mục tiêu Miền (Target Domain)
Chính Các sự ràng buộc (Key Constraints)
Chính Các số liệu (Primary Metrics)
MLPerf Huấn luyện
Dữ liệu trung tâm
Nhiều-nút sự mở rộng quy mô, cao băng thông
các kết nối
Thời gian-tới-chất lượng, thông lượng
(các mẫu/giây)
MLPerf Suy luận
Máy chủ/Biên
Độ trễ các SLA, thông lượng các yêu cầu
QPS, độ trễ các phân vị, độ chính xác
sự bảo tồn
MLPerf Nhỏ bé
MCU/IoT
Cực kỳ-thấp-điện năng suy luận, bị giới hạn
bộ nhớ
Độ trễ, độ chính xác, năng lượng mỗi suy luận
MLPerf Năng lượng
Chéo-cắt
Năng lượng các ngân sách, nhiệt các sự ràng buộc
Hiệu suất/W, năng lượng mỗi truy vấn
MLPerf Năng lượng mở rộng cùng kỷ luật tới năng lượng tính hiệu quả, nơi được đo điểm chuẩn đại lượng là
hữu ích công việc mỗi watt thay vì thô thông lượng đơn thuần (MLPerf Power extends the same discipline to energy efficiency, where the benchmarked quantity is useful work per watt rather than raw throughput alone). Cụ thể-miền các điểm chuẩn thúc đẩy được nhắm mục tiêu
phần cứng và phần mềm các sự tối ưu hóa trong khi việc đảm bảo rằng các sự cải thiện dịch thuật thành sự triển khai
thành công thay vì hẹp phòng thí nghiệm các điều kiện (Domain-specific benchmarks drive targeted hardware and software optimizations while ensuring that improvements translate to deployment success rather than narrow laboratory conditions).
Này lịch sử sự tiến triển, từ tổng quát máy tính các điểm chuẩn thông qua nhận thức-năng lượng sự đo-
lường tới cụ thể-miền sự đánh giá các bộ khung, cung cấp nền tảng cho việc hiểu
ML việc đo điểm chuẩn các thách thức (This historical progression, from general computing benchmarks through energy-aware measurement to domain-specific evaluation frameworks, provides the foundation for understanding ML benchmarking challenges). Các bài học được học (đại diện các khối lượng công việc trên tổng hợp các bài kiểm tra,
đa-mục tiêu trên đơn các số liệu, được tích hợp các hệ thống trên được cô lập các thành phần) một cách trực tiếp định hình
AI hệ thống sự đánh giá (The lessons learned (representative workloads over synthetic tests, multi-objective over single metrics, integrated systems over isolated components) directly shape AI system evaluation). Bảng 12.2 tóm tắt này sự tiến triển và chính các bài học mỗi thế hệ
đã đóng góp (Table 12.2 summarizes this progression and the key lessons each generation contributed).

12. Việc đo điểm chuẩn (Benchmarking)
647
Bảng 12.2: Điểm chuẩn Sự tiến hóa (Benchmark Evolution): Sự tiến hóa của máy tính các điểm chuẩn từ tổng hợp các hoạt động tới cụ thể-ML sự đánh giá (Evolution of computing benchmarks from synthetic operations to ML-specific evaluation).
Mỗi thế hệ đã giải quyết các hạn chế của của nó các người tiền nhiệm, việc đạt đến đỉnh cao trong MLPerf’s sự tổng hợp của đại diện các khối lượng công việc,
đa-mục tiêu các số liệu, và được tích hợp hệ thống sự đo lường (Each generation addressed limitations of its predecessors, culminating in MLPerf’s synthesis of representative workloads, multi-objective metrics, and integrated system measurement).
Điểm chuẩn (Benchmark)
Năm (Year)
Chính Trọng tâm (Primary Focus)
Chính Số liệu(s) (Key Metric(s))
Bài học cho ML Việc đo điểm chuẩn (Lesson for ML Benchmarking)
Whetstone
1976
Tổng hợp dấu phẩy-động
các hoạt động
MWIPS
Việc chơi trò chơi tổng hợp các bài kiểm tra làm suy yếu
sự đánh giá tính hợp lệ (Gaming synthetic tests undermines evaluation validity)
LINPACK
1979
Tuyến tính đại số (ma trận
các hoạt động)
FLOP/s
Được cô lập các hoạt động bỏ lỡ cấp độ-hệ thống
sự phức tạp và các nút thắt cổ chai (Isolated operations miss system-level complexity and bottlenecks)
SPEC CPU
1989
Thực ứng dụng
các khối lượng công việc
SPECrate, SPECspeed
Đại diện các khối lượng công việc tiết lộ thực sự
sự triển khai hiệu suất (Representative workloads reveal true deployment performance)
SPEC Năng lượng (SPEC Power)
2007
Máy chủ năng lượng tính hiệu quả
ssj_ops/W qua tải
các cấp độ
Năng lượng tính hiệu quả yêu cầu đa-tải
sự đánh giá, không chỉ đỉnh hiệu suất (Energy efficiency requires multi-load evaluation, not just peak performance)
Green500
2007
HPC năng lượng tính hiệu quả
GFLOP/s mỗi watt
Tính hiệu quả các bảng xếp hạng bổ sung cho thô
hiệu suất các bảng xếp hạng (Efficiency rankings complement raw performance rankings)
MLPerf
2018
ML các hệ thống (huấn luyện +
suy luận)
Thời gian-tới-chất lượng, QPS,
độ trễ, độ chính xác
Tổng hợp tất cả các bài học: đại diện
các khối lượng công việc + đa-mục tiêu + hệ thống (Synthesizes all lessons: representative workloads + multi-objective + system)
Những các bài học này đạt đến đỉnh cao trong ML việc đo điểm chuẩn các bộ phần mềm, tuy nhiên ML các hệ thống đối mặt với một bổ sung thách thức
vắng mặt từ truyền thống các điểm chuẩn: vốn có mang tính xác suất sự biến thiên (These lessons culminate in ML benchmarking suites, yet ML systems face an additional challenge absent from traditional benchmarks: inherent probabilistic variability). Không giống như truyền thống các khối lượng công việc
với mang tính xác định hành vi, ML các hệ thống phải thỏa mãn tất cả ba lịch sử các bài học (đại diện
các khối lượng công việc, đa-mục tiêu sự đánh giá, được tích hợp sự đo lường) trong khi cũng việc tính toán cho ngẫu nhiên (stochastic)
các kết quả thứ mà biến đổi với huấn luyện dữ liệu, trọng số sự khởi tạo, và thậm chí hoạt động sự sắp xếp (Unlike traditional workloads with deterministic behavior, ML systems must satisfy all three historical lessons (representative workloads, multi-objective evaluation, integrated measurement) while also accounting for stochastic outcomes that vary with training data, weight initialization, and even operation ordering). Này
bổ sung chiều của sự biến thiên đòi hỏi sự đo lường các phương pháp luận thứ mà tính toán cho ngẫu nhiên
các kết quả (This additional dimension of variability demands measurement methodologies that account for stochastic outcomes).
Cá nhân các tổ chức đã học những các bài học này một cách độc lập, thường một cách đau đớn, nhưng được cô lập các sự đo-
lường không thể thúc đẩy một ngành công nghiệp (Individual organizations learned these lessons independently, often painfully, but isolated measurements cannot drive an industry). Khi một nhóm đo lường suy luận độ trễ việc bao gồm sự tiền xử-
lý và một cái khác loại trừ nó, khi độ chính xác các điểm chuẩn sử dụng khác nhau dữ liệu các sự chia tách (splits), hoặc khi điện năng
các sự đo lường vẽ khác nhau hệ thống các ranh giới, việc dẫn đến các con số là không thể so sánh được (The transition from ad-hoc measurement to standardized benchmarking suites transforms benchmarking from an internal validation exercise into a shared language that enables hardware procurement, architecture comparison, and deployment decisions across organizations) (when one team measures inference latency including preprocessing and another excludes it, when accuracy benchmarks use different data splits, or when power measurements draw different system boundaries, the resulting numbers are incommensurable). Sự
chuyển tiếp từ đặc biệt (ad-hoc) sự đo lường tới được chuẩn hóa việc đo điểm chuẩn các bộ phần mềm biến đổi việc đo điểm chuẩn
từ một nội bộ sự xác nhận bài tập thành một được chia sẻ ngôn ngữ thứ mà kích hoạt phần cứng sự mua sắm,
kiến trúc sự so sánh, và sự triển khai các quyết định qua các tổ chức (The transition from ad-hoc measurement to standardized benchmarking suites transforms benchmarking from an internal validation exercise into a shared language that enables hardware procurement, architecture comparison, and deployment decisions across organizations).
12.3 Hệ thống Việc đo điểm chuẩn Các bộ phần mềm (System Benchmarking Suites)
Một nhóm việc đánh giá biên sự triển khai phần cứng cần để so sánh năm khác nhau hệ thống trên chip (SoC)
các thiết kế cho một thông minh máy ảnh sản phẩm (A team evaluating edge deployment hardware needs to compare five different system on chip (SoC) designs for a smart camera product). Nhà cung cấp A báo cáo 8 TOPS tại INT8; Nhà cung cấp B báo cáo 15 TOPS tại
INT4; Nhà cung cấp C báo cáo suy luận độ trễ trên một độc quyền mô hình; Nhà cung cấp D trích dẫn MLPerf các điểm số từ
hai các thế hệ trước; Nhà cung cấp E cung cấp chỉ đỉnh thông lượng tại tối đa lô kích thước (Vendor A reports 8 TOPS at INT8; Vendor B reports 15 TOPS at INT4; Vendor C reports inference latency on a proprietary model; Vendor D cites MLPerf scores from two generations ago; Vendor E provides only peak throughput at maximum batch size). Không có cái nào của
những các con số này là có thể so sánh (None of these numbers are comparable). Nhóm không thể đưa ra một sự mua sắm quyết định bởi vì mỗi nhà cung cấp
đã đo lường một khác nhau thứ, dưới khác nhau các điều kiện, việc sử dụng khác nhau các định nghĩa của “hiệu suất.” (The team cannot make a procurement decision because every vendor measured a different thing, under different conditions, using different definitions of “performance.”)
Vấn đề là không phải một sự thiếu hụt của dữ liệu mà là một sự thiếu hụt của có thể so sánh dữ liệu, và việc đo điểm chuẩn các bộ phần mềm tồn tại để
giải quyết chính xác này sự phân mảnh (The problem is not a lack of data but a lack of commensurable data, and benchmarking suites exist to solve exactly this fragmentation).
Ba các bài học từ điểm chuẩn lịch sử (đại diện các khối lượng công việc, đa-mục tiêu sự đánh giá,
và được tích hợp sự đo lường) hội tụ với thách thức duy nhất cho ML: vốn có mang tính xác suất
sự biến thiên (Three lessons from benchmark history (representative workloads, multi-objective evaluation, and integrated measurement) converge with the challenge unique to ML: inherent probabilistic variability). Hiện đại việc đo điểm chuẩn các bộ phần mềm mã hóa những các bài học này thành được chuẩn hóa các bộ khung thứ mà
làm cho loại này của chéo-tổ chức sự so sánh của chúng ta phần cứng sự mua sắm nhóm cần có thể (Modern benchmarking suites encode these lessons into standardized frameworks that make the kind of cross-organization comparison our hardware procurement team needs possible).
ML các điểm chuẩn phải đánh giá sự tác động qua lại giữa các thuật toán, phần cứng, và dữ liệu, không đơn thuần
tính toán tính hiệu quả đơn thuần (ML benchmarks must evaluate the interplay between algorithms, hardware, and data, not merely computational efficiency alone). Sớm các điểm chuẩn đã tập trung trên thuật toán hiệu suất (LeCun et al.
1998), nhưng việc mở rộng quy mô các đòi hỏi đã mở rộng trọng tâm tới phần cứng tính hiệu quả (Jouppi et al. 2017), và cao-
hồ sơ sự triển khai các thất bại đã nâng tầm dữ liệu chất lượng như một thứ ba sự đánh giá chiều (Gebru et al. 2021) (Early benchmarks focused on algorithmic performance (LeCun et al. 1998), but scaling demands expanded the focus to hardware efficiency (Jouppi et al. 2017), and high-profile deployment failures elevated data quality as a third evaluation dimension (Gebru et al. 2021)).
Này mang tính xác suất bản chất nâng tầm độ chính xác thành một hạng-nhất sự đánh giá chiều song song tốc độ và
năng lượng sự tiêu thụ: cùng ML hệ thống có thể tạo ra khác nhau các kết quả phụ thuộc trên dữ liệu nó
bắt gặp (This probabilistic nature elevates accuracy to a first-class evaluation dimension alongside speed and energy consumption: the same ML system can produce different results depending on the data it encounters). Năng lượng tính hiệu quả cắt qua tất cả ba bộ khung các chiều, do thuật toán các sự lựa chọn
ảnh hưởng tính toán sự phức tạp, phần cứng các khả năng xác định năng lượng-hiệu suất các sự đánh đổi,
và tập dữ liệu các đặc điểm ảnh hưởng huấn luyện năng lượng các chi phí (Hernandez and Brown 2020) (Energy efficiency cuts across all three framework dimensions, since algorithmic choices affect computational complexity, hardware capabilities determine energy-performance trade-offs, and dataset characteristics influence training energy costs (Hernandez and Brown 2020)).

648
12.3 Hệ thống Việc đo điểm chuẩn Các bộ phần mềm (System Benchmarking Suites)
Một 1K kiểm tra tập hợp không thể một cách đáng tin cậy thấy
một một-điểm sự thụt lùi (A 1K test set cannot reliably see a one-point regression).
12.3.1 ML sự đo lường các thách thức (ML measurement challenges)
Các duy nhất các đặc điểm của ML các hệ thống tạo ra sự đo lường sự biến thiên thứ mà nhiều truyền thống
các điểm chuẩn đã không được thiết kế cho (The unique characteristics of ML systems create measurement variability that many traditional benchmarks were not designed for). Không giống như mang tính xác định các thuật toán thứ mà tạo ra giống hệt các đầu ra
được cho cùng các đầu vào, ML các hệ thống thể hiện vốn có sự biến thiên từ nhiều các nguồn: thuật toán
sự ngẫu nhiên từ trọng số sự khởi tạo và dữ liệu việc xáo trộn, phần cứng nhiệt các trạng thái việc ảnh hưởng xung nhịp
các tốc độ, hệ thống tải các sự biến thiên từ đồng thời các quá trình, và thuộc về môi trường các yếu tố bao gồm mạng
các điều kiện và điện năng sự quản lý (Unlike deterministic algorithms that produce identical outputs given the same inputs, ML systems exhibit inherent variability from multiple sources: algorithmic randomness from weight initialization and data shuffling, hardware thermal states affecting clock speeds, system load variations from concurrent processes, and environmental factors including network conditions and power management). Này sự biến thiên yêu cầu nghiêm ngặt thống kê phương pháp luận
để phân biệt xác thực hiệu suất các sự cải thiện khỏi sự đo lường tiếng ồn (This variability requires rigorous statistical methodology to distinguish genuine performance improvements from measurement noise).
Để giải quyết này sự biến thiên, hiệu quả điểm chuẩn các giao thức yêu cầu nhiều thực nghiệm các lượt chạy với
khác nhau ngẫu nhiên các hạt giống (To address this variability, effective benchmark protocols require multiple experimental runs with different random seeds). Việc chạy mỗi điểm chuẩn 5–10 lần và việc báo cáo thống kê các thước đo
vượt ra ngoài đơn giản các giá trị trung bình (bao gồm chuẩn các độ lệch hoặc 95 phần trăm sự tự tin các khoảng) định lượng
kết quả sự ổn định và cho phép những người thực hành để phân biệt xác thực hiệu suất các sự cải thiện khỏi
sự đo lường tiếng ồn (Running each benchmark 5–10 times and reporting statistical measures beyond simple means (including standard deviations or 95 percent confidence intervals) quantifies result stability and allows practitioners to distinguish genuine performance improvements from measurement noise).
Thực nghiệm các nghiên cứu đã cho thấy cách nào không đủ thống kê sự nghiêm ngặt có thể dẫn tới gây hiểu lầm các kết luận (Empirical studies have shown how inadequate statistical rigor can lead to misleading conclusions).
Nhiều củng cố học tập các bài báo báo cáo các sự cải thiện thứ mà rơi vào bên trong thống kê tiếng ồn (Hen-
derson et al. 2018), trong khi GAN các sự so sánh thường thiếu thích hợp thực nghiệm các giao thức, việc dẫn tới
không nhất quán các xếp hạng qua khác nhau ngẫu nhiên các hạt giống (Lucic et al. 2018) (Many reinforcement learning papers report improvements that fall within statistical noise (Henderson et al. 2018), while GAN comparisons often lack proper experimental protocols, leading to inconsistent rankings across different random seeds (Lucic et al. 2018)). Những các phát hiện này nhấn mạnh
tầm quan trọng của việc thiết lập sự đo lường các giao thức thứ mà tính toán cho ML’s mang tính xác suất bản chất (These findings underscore the importance of establishing measurement protocols that account for ML’s probabilistic nature).
Đại diện khối lượng công việc sự lựa chọn xác định điểm chuẩn tính hợp lệ (Representative workload selection determines benchmark validity). Tổng hợp vi điểm chuẩn (microbenchmarks)
thường thất bại để nắm bắt sự phức tạp của thực ML các khối lượng công việc nơi dữ liệu sự di chuyển, bộ nhớ sự phân bổ,
và động việc làm theo lô tạo ra hiệu suất các mẫu không vô hình trong được đơn giản hóa các bài kiểm tra (Synthetic microbenchmarks often fail to capture the complexity of real ML workloads where data movement, memory allocation, and dynamic batching create performance patterns not visible in simplified tests). Toàn diện
việc đo điểm chuẩn do đó yêu cầu các khối lượng công việc thứ mà phản ánh thực tế sự triển khai các mẫu: biến đổi chu-
ỗi các độ dài trong ngôn ngữ các mô hình, hỗn hợp độ chính xác huấn luyện các chế độ, và thực tế dữ liệu việc tải
các mẫu thứ mà bao gồm sự tiền xử lý chi phí chung (Comprehensive benchmarking therefore requires workloads that reflect actual deployment patterns: variable sequence lengths in language models, mixed precision training regimes, and realistic data loading patterns that include preprocessing overhead).
Khăn ăn (Napkin) Toán 12.1: Thống kê sự tự tin cạm bẫy (The statistical confidence trap)
Vấn đề: Một đường cơ sở hình ảnh bộ phân loại có 95 phần trăm độ chính xác (Problem: A baseline image classifier has 95 percent accuracy). Một “được nén” phiên bản là
được triển khai và của nó độ chính xác được đo lường trên một 1,000-hình ảnh kiểm tra tập hợp, việc mang lại 94 phần trăm (A “compressed” version is deployed and its accuracy measured on a 1,000-image test set, yielding 94 percent). Đã
sự tối ưu hóa gây ra một thực sự thụt lùi, hay là nó tiếng ồn? (Did the optimization cause a real regression, or is it noise?)
Toán (Math):
1. Được mong đợi các lỗi (Expected errors): Tại 95 phần trăm độ chính xác, kiểm tra tập hợp tạo ra 50 các lỗi (At 95 percent accuracy, the test set produces 50 errors). Tại 94 phần trăm, nó
tạo ra 60 các lỗi (At 94 percent, it produces 60 errors).
2. Chuẩn Độ lệch (Standard Deviation) (𝜎err): Việc sử dụng nhị thức sự phân phối với 𝑁test kiểm tra các ví dụ và
sự kiện xác suất 𝑝err = Pr(err) (Using the binomial distribution with 𝑁test test examples and event probability 𝑝err = Pr(err)):
𝜎err ≈√𝑁test ×𝑝err ×(1−𝑝err) =
√
1000×0.05×0.95
Điều này mang lại xấp xỉ 7 các lỗi (This yields approximately 7 errors).
3. Sự tự tin khoảng (Confidence interval) (95 phần trăm): 50 các lỗi ± 1.96 × 7 các lỗi ≈[36, 64].
Sự đo lường hàm ý: Cả hai 50 các lỗi và 60 các lỗi rơi vào bên trong cùng sự tự tự tin
khoảng (Measurement implication: Both 50 errors and 60 errors fall inside the same confidence interval). Một 1,000-mẫu kiểm tra tập hợp không thể một cách đáng tin cậy phát hiện một 1 phần trăm điểm độ chính xác sự sụt giảm (A 1,000-sample test set cannot reliably detect a 1 percentage point accuracy drop).
Khoảng 1,825 các mẫu là đủ để ước tính một 95 phần trăm độ chính xác tỷ lệ với một 95 phần trăm
sự tự tin khoảng của khoảng ±1 phần trăm điểm; việc phát hiện một 1-điểm sự thụt lùi giữa
hai một cách độc lập được đánh giá các mô hình yêu cầu một lớn hơn hai-tỷ lệ điện năng sự tính toán (About 1,825 samples are enough to estimate a 95 percent accuracy rate with a 95 percent confidence interval of about ±1 percentage point; detecting a 1-point regression between two independently evaluated models requires a larger two-proportion power calculation).
Các hệ thống sự thấu hiểu (Systems insight): Nhỏ các điểm chuẩn thể hiện cái mà số lượng tới một phòng thí nghiệm ngụy biện (Small benchmarks exhibit what amounts to a laboratory fallacy). Kiểm tra tập hợp,
được xem như một sự đo lường công cụ, phải được định cỡ để khớp độ chính xác của sự thay đổi nó là
có ý nghĩa để phát hiện (The test set, viewed as a measurement instrument, must be sized to match the precision of the change it is meant to detect).
Vượt ra ngoài khối lượng công việc tính đại diện, sự phân biệt giữa thống kê ý nghĩa và thực-
tế ý nghĩa yêu cầu cẩn thận sự diễn giải (Beyond workload representativeness, the distinction between statistical significance and practical significance requires careful interpretation). Một nhỏ hiệu suất sự cải thiện có thể đạt được
thống kê ý nghĩa qua hàng trăm của các thử nghiệm nhưng chứng tỏ thuộc về hoạt động không liên quan nếu nó rơi vào bên trong (A small performance improvement might achieve statistical significance across hundreds of trials but prove operationally irrelevant if it falls within)

12. Việc đo điểm chuẩn (Benchmarking)
649
sự đo lường tiếng ồn hoặc các chi phí vượt quá các lợi ích (measurement noise or costs exceed benefits). Điều này tạo ra cái mà chúng ta gọi là thống kê sự tự tin cạm bẫy,
nơi có vẻ như nghiêm ngặt sự đánh giá vẫn làm lạc hướng (This creates what we call the statistical confidence trap, where seemingly rigorous evaluation still misleads).
Thống kê sự tự tin là một sự đo lường-dung lượng vấn đề: điểm chuẩn có thể được chỉ
vào đúng đại lượng, nhưng kiểm tra tập hợp là quá nhỏ để giải quyết sự thay đổi (Statistical confidence is a measurement-capacity problem: the benchmark may be pointed at the right quantity, but the test set is too small to resolve the change). Một thứ hai thất bại chế độ là số liệu
sự căn chỉnh (A second failure mode is metric alignment). Ở đây sự đo lường có thể là chính xác và có thể tái tạo, tuy nhiên vẫn thưởng hành vi thứ mà
vi phạm được triển khai hệ thống’s mục tiêu (Here the measurement can be precise and reproducible, yet still reward behavior that violates the deployed system’s objective). Sự dịch thuật ví dụ làm cho đó sự phân biệt cụ thể bằng cách
việc cho thấy cách nào một BLEU sự cải thiện có thể đến tại chi phí của độ trễ (The translation example makes that distinction concrete by showing how a BLEU improvement can come at the expense of latency).
Ví dụ 12.1: Goodhart’s Định luật trong hành động (Goodhart’s Law in action)
Cạm bẫy: Việc tối ưu hóa cho một đơn số liệu thường làm giảm những cái khác (Trap: Optimizing for a single metric often degrades others).
Kịch bản: Một nhóm tối ưu hóa một sự dịch thuật mô hình cho BLEU điểm số, việc tạo ra một Goodhart’s Định luật
thất bại (Scenario: A team optimizes a translation model for BLEU score, creating a Goodhart’s Law failure).
• Ban đầu mô hình: BLEU = 28, Suy luận = 50 ms (Original model: BLEU = 28, Inference = 50 ms).
• Được tối ưu hóa mô hình: BLEU = 28.5 (một 0.5-điểm khoản đạt được), Suy luận = 200 ms (4× chậm hơn) (Optimized model: BLEU = 28.5 (a 0.5-point gain), Inference = 200 ms (4× slower)).
Sự phân tích (Analysis):
• 0.5 BLEU khoản đạt được đến từ một lớn hơn chùm tia (beam) tìm kiếm, thứ mà giữ 𝑘 nhiều hứa hẹn nhất
một phần các bản dịch tại mỗi việc giải mã bước thay vì một (beam_size = 10 so với beam_size =
1) (The 0.5 BLEU gain comes from a larger beam search, which keeps the 𝑘 most promising partial translations at each decoding step instead of one (beam_size = 10 vs. beam_size = 1)).
• Chi phí: 10× nhiều hơn ứng cử viên các sự đánh giá mỗi bước (Cost: 10× more candidate evaluations per step).
• Kết quả: Được tối ưu hóa mô hình chiến thắng bảng xếp hạng trong khi việc vi phạm được triển khai hệ thống’s
độ trễ ngân sách (Result: The optimized model wins the leaderboard while violating the deployed system’s latency budget).
Các hệ thống bài học (Systems lesson): Luôn luôn ràng buộc sự tối ưu hóa (Always constrain the optimization). Tối đa hóa Độ chính xác phụ thuộc vào Độ trễ <
100 ms (Maximize Accuracy subject to Latency < 100 ms).
Những các sự đo lường thất bại này chia sẻ một sâu hơn hạn chế: một điểm chuẩn trên một tĩnh tập dữ liệu đo lường
sự nhận dạng dưới một cố định sự phân phối, không phải tính mạnh mẽ tới một đang chuyển dịch cái mà sản xuất đòi hỏi (These measurement failures share a deeper limitation: a benchmark on a static dataset measures recognition under a fixed distribution, not the robustness to a shifting one that production demands).
Dữ liệu chiều của bộ khung được phát triển sau này trong này chương đối mặt chính xác đó khoảng cách (The data dimension of the framework developed later in this chapter confronts exactly that gap).
Trước đó sự đo lường các thách thức thúc đẩy việc đánh giá mỗi chiều của ba-
chiều bộ khung (hệ thống, mô hình, và dữ liệu) với khác biệt các phương pháp luận (The preceding measurement challenges motivate evaluating each dimension of the three-dimensional framework (system, model, and data) with distinct methodologies). Phần lớn của
này chương tập trung trên hệ thống việc đo điểm chuẩn (huấn luyện các điểm chuẩn, suy luận các điểm chuẩn, và
điện năng sự đo lường) bởi vì những cái này hình thành nền tảng của được chuẩn hóa sự đánh giá thông qua
MLPerf (The bulk of this chapter focuses on system benchmarking (training benchmarks, inference benchmarks, and power measurement) because these form the foundation of standardized evaluation through MLPerf). Mô hình và dữ liệu việc đo điểm chuẩn yêu cầu khác nhau các phương pháp luận và là được đối xử trong chi tiết trong
phần 12.11 sau khi chúng ta thiết lập hệ thống sự đánh giá các nền tảng (Model and data benchmarking require different methodologies and are treated in detail in section 12.11 after we establish system evaluation foundations).
12.3.2 Hệ thống các điểm chuẩn (System benchmarks)
Hệ thống các điểm chuẩn đo lường tính toán nền tảng thứ mà kích hoạt mô hình các khả năng, việc kiểm-
tra cách nào phần cứng các kiến trúc, bộ nhớ các hệ thống, và các kết nối ảnh hưởng tổng thể hiệu suất (System benchmarks measure the computational foundation that enables model capabilities, examining how hardware architectures, memory systems, and interconnects affect overall performance).
Này sự xác nhận là then chốt bởi vì phần cứng các thông số kỹ thuật thường miêu tả lý thuyết các đỉnh thứ mà thực tế
các khối lượng công việc không bao giờ đạt được (This validation is critical because hardware specifications often describe theoretical peaks that real workloads never achieve). Sự không nhất quán là đủ phổ biến để làm cho đỉnh-hiệu suất các tuyên bố
gây hiểu lầm (The discrepancy is common enough to make peak-performance claims misleading). Hệ thống các điểm chuẩn tiết lộ những các khoảng cách này bằng cách việc chạy được chuẩn hóa ML các khối lượng công việc thay vì
tổng hợp vi điểm chuẩn (System benchmarks reveal these gaps by running standardized ML workloads rather than synthetic microbenchmarks).
Các Hệ thống Phối cảnh 12.3: Ngụy biện của đỉnh hiệu suất (Systems Perspective 12.3: The fallacy of peak performance)
Dave Patterson thường tham khảo tới đỉnh hiệu suất như “hiệu suất nhà sản xuất đảm-
bảo bạn sẽ không vượt quá.” (Dave Patterson often refers to peak performance as “the performance the manufacturer guarantees you will not exceed.”) Cho ML các hệ thống, đó khoảng cách là đặc biệt rộng bởi vì của bộ nhớ
bức tường: một bị ràng buộc-bộ nhớ mô hình để lại hầu hết của được quảng cáo FLOP/s không thể tiếp cận không có vấn đề
cách nào nhanh số học các đơn vị chạy (For ML systems, that gap is especially wide because of the memory wall: a memory-bound model leaves most of the advertised FLOP/s unreachable no matter how fast the arithmetic units run). Được chuẩn hóa các điểm chuẩn giống như MLPerf là cần thiết bởi vì
chúng ép buộc các hệ thống để chạy thực các mô hình trên thực dữ liệu, việc tiết lộ thực sự “được duy trì hiệu suất”
thứ mà các kỹ sư có thể thực sự dựa vào (Standardized benchmarks like MLPerf are essential because they force systems to run real models on real data, revealing the true “sustained performance” that engineers can actually rely on).

650
12.3 Hệ thống Việc đo điểm chuẩn Các bộ phần mềm (System Benchmarking Suites)
7
TPU (Tensor Việc xử lý
Đơn vị (Unit)): Google’s tùy chỉnh ASIC
cho thần kinh mạng các khối lượng công việc
(kiến trúc các chi tiết trong Chương
11) (TPU (Tensor Processing Unit): Google’s custom ASIC for neural network workloads (architecture details in Chapter 11)). Một TPU v4 vỏ (pod) (4,096
các chip) cung cấp 1.1 exaFLOP/s
đỉnh BF16, nhưng việc đo điểm chuẩn
các TPU yêu cầu sự thận trọng: của chúng
tâm thu-mảng kiến trúc ưu-
tiên đều đặn tensor các hoạt động,
do đó đỉnh FLOP/s phóng đại hiệu-
suất trên không đều đặn các khối lượng-
công việc giống như thưa thớt sự chú ý hoặc
động điều khiển luồng (A TPU v4 pod (4,096 chips) delivers 1.1 exaFLOP/s peak BF16, but benchmarking TPUs requires caution: their systolic-array architecture favors regular tensor operations, so peak FLOP/s overstate performance on irregular workloads like sparse attention or dynamic control flow).
8
ASIC
(Cụ thể-
Ứng dụng Được tích hợp Mạch (Application-Specific Integrated Circuit)):
Một ASIC’s đỉnh TOPS con-
số áp dụng chỉ cho cụ thể
các toán tử nó đã được thiết kế
cho (ASIC (Application-Specific Integrated Circuit): An ASIC’s peak TOPS number applies only to the specific operators it was designed for).
Một đơn không được hỗ trợ
lớp ép buộc sự lùi lại tới một
tổng quát-mục đích
bộ xử lý,
có khả năng
việc phủ nhận
toàn bộ tính hiệu quả lợi thế (A single unsupported layer forces fallback to a general-purpose processor, potentially negating the entire efficiency advantage).
Điều này làm cho toán tử sự bao phủ
câu
hỏi
đầu tiên
trong
bất kỳ
ASIC điểm chuẩn nào:
khoảng cách
giữa đỉnh và đạt được
thông lượng là không phải một phần cứng
sự hạn chế mà một sự tương-
thích-
khối lượng công việc
sự hạn chế (This makes operator coverage the first question in any ASIC benchmark: the gap between peak and achieved throughput is not a hardware limitation but a workload-compatibility limitation).
9
FLOP/s (Dấu phẩy-Động
Các hoạt động
Mỗi
Giây (Second)):
Khoảng cách giữa được quảng cáo
đỉnh FLOP/s và đạt được
FLOP/s là trung tâm căng thẳng
trong phần cứng việc đo điểm chuẩn (FLOP/s (Floating-Point Operations Per Second): The gap between advertised peak FLOP/s and achieved FLOP/s is the central tension in hardware benchmarking).
A100
quảng cáo
312
TFLOP/s FP16 Tensor Lõi,
nhưng thực các khối lượng công việc đạt được
khác nhau các phần của đỉnh
phụ thuộc
trên
số học
cường độ, bộ nhớ truy cập các mẫu,
độ chính xác, và thời gian chạy
chi phí chung (The A100 advertises 312 TFLOP/s FP16 Tensor Core, but real workloads achieve different fractions of peak depending on arithmetic intensity, memory access patterns, precision, and runtime overhead).
Việc báo cáo đỉnh
FLOP/s mà không sự sử dụng
ngữ cảnh là phổ biến nhất
việc đo điểm chuẩn sự bóp méo (Reporting peak FLOP/s without utilization context is the most common benchmarking distortion).
Đỉnh-so với-được duy trì khoảng cách là về mặt cấu trúc được đảm bảo bởi bộ nhớ bức tường, không phải một thỉnh thoảng
sự bất thường thứ mà tốt hơn kỹ thuật có thể tránh (The peak-vs.-sustained gap is structurally guaranteed by the memory wall, not an occasional anomaly that better engineering can avoid). Việc nhận ra này mang tính cấu trúc bản chất đóng khung lại nhà cung cấp
sự đánh giá từ sự phỏng đoán thành một danh sách kiểm tra của cụ thể các tiêu chí (Recognizing this structural nature reframes vendor evaluation from guesswork into a checklist of concrete criteria).
Điểm kiểm tra (Checkpoint) 12.1: Việc giải mã nhà cung cấp điểm chuẩn các tuyên bố (Decoding vendor benchmark claims)
Khi việc đánh giá phần cứng hoặc phần mềm dựa trên được báo cáo-bởi-nhà cung cấp các điểm chuẩn, kiểm tra liệu
tuyên bố nhận diện khối lượng công việc, sự đo lường ranh giới, và hoạt động các điều kiện (When evaluating hardware or software based on vendor-reported benchmarks, check whether the claim identifies the workload, measurement boundary, and operating conditions).
□Được đo lường đại lượng: Có thể bạn phân biệt liệu một độ trễ con số bao gồm sự tiền xử lý và
sự hậu xử lý, không chỉ mô hình sự thực thi? (Measured quantity: Can you tell whether a latency number includes preprocessing and postprocessing, not just model execution?)
□Độ chính xác ranh giới: Có thể bạn nhận diện độ chính xác đằng sau một thông lượng tuyên bố, chẳng hạn như
INT4 so với INT8 hoặc FP16? (Precision boundary: Can you identify the precision behind a throughput claim, such as INT4 versus INT8 or FP16?)
□Khối lượng công việc ranh giới: Có thể bạn đặt tên mô hình, lô kích thước, và đầu vào sự phân phối được sử dụng
để tạo ra sự so sánh? (Workload boundary: Can you name the model, batch size, and input distribution used to produce the comparison?)
□Bị loại trừ các chi phí: Có thể bạn tính toán cho bộ nhớ các sự truyền tải, mô hình việc tải, sự khởi tạo,
được duy trì nhiệt hành vi, và điện năng tại được tuyên bố hiệu suất cấp độ? (Excluded costs: Can you account for memory transfers, model loading, initialization, sustained thermal behavior, and power at the claimed performance level?)
□Được tuyên bố so với Đạt được: Được cho một 1,000 TFLOP/s đỉnh tuyên bố và một điểm chuẩn thứ mà duy-
trì 350 TFLOP/s, ước tính MFU, và quyết định liệu sự thiếu hụt chỉ điểm nhiều hơn tới
số học cường độ hay tới bộ nhớ băng thông (Claimed vs. achieved: Given a 1,000 TFLOP/s peak claim and a benchmark that sustains 350 TFLOP/s, estimate the MFU, and decide whether the shortfall points more to arithmetic intensity or to memory bandwidth).
Bảng 12.3 dịch thuật chung tiếp thị các cụm từ thành kỹ thuật các lời cảnh báo (caveats) đằng sau mỗi cái (Table 12.3 translates common marketing phrases into the technical caveats behind each).
Bảng 12.3: Việc giải mã Nhà cung cấp Điểm chuẩn Các tuyên bố (Decoding Vendor Benchmark Claims): Bốn chung tiếp thị các cụm từ và kỹ thuật các lời cảnh báo thứ mà
xác định liệu một tuyên bố miêu tả đầu-tới-đầu hiệu suất, một hẹp máy gia tốc sự đo lường, hay một không được hỗ trợ
tính hiệu quả sự so sánh (Four common marketing phrases and the technical caveats that determine whether a claim describes end-to-end performance, a narrow accelerator measurement, or an unsupported efficiency comparison).
Nhà cung cấp Tuyên bố (Vendor Claim)
Cái gì Nó Thường Có nghĩa là (What It Often Means)
“Lên tới 10,000 các hình ảnh/giây” (“Up to 10,000 images/sec”)
Đỉnh thông lượng tại tối đa lô kích thước, INT8, mà không sự tiền xử lý (Peak throughput at maximum batch size, INT8, without preprocessing)
“Dưới-mili giây độ trễ” (“Sub-millisecond latency”)
Máy gia tốc tính toán chỉ, việc loại trừ dữ liệu sự truyền tải (Accelerator compute only, excluding data transfer)
“5× nhiều hiệu quả hơn” (“5× more efficient”)
Mỗi-hoạt động tính hiệu quả, không phải tổng hệ thống tính hiệu quả (Per-operation efficiency, not total system efficiency)
“Được tối ưu hóa cho AI” (“Optimized for AI”)
Có thể chỉ gia tốc cụ thể các hoạt động hoặc các độ chính xác (May only accelerate specific operations or precisions)
Quyết định quy tắc là để từ chối bất kỳ điểm chuẩn tuyên bố nào cái mà khối lượng công việc ranh giới, độ chính xác, và
bị loại trừ các chi phí không thể được tái tạo (The decision rule is to reject any benchmark claim whose workload boundary, precision, and excluded costs cannot be reconstructed). Một tiêu đề thông lượng hay độ trễ con số trở thành hữu ích
chỉ sau khi kỹ sư có thể ánh xạ nó tới thực sự mô hình, lô hình dạng, dữ liệu sự di chuyển, được duy trì
hoạt động điểm, và điện năng phong bì (A headline throughput or latency number becomes useful only after the engineer can map it to the actual model, batch shape, data movement, sustained operating point, and power envelope).
Cơ bản phần cứng cơ sở hạ tầng (các CPU, các GPU, Tensor Việc xử lý Các đơn vị (Các TPU)7, và
Các ASIC8) xác định tốc độ, tính hiệu quả, và khả năng mở rộng quy mô của ML các hệ thống (The underlying hardware infrastructure (CPUs, GPUs, Tensor Processing Units (TPUs)7, and ASICs8) determines the speed, efficiency, and scalability of ML systems). Hệ thống các điểm chuẩn thiết lập
được chuẩn hóa các phương pháp luận cho việc đánh giá phần cứng hiệu suất qua AI các khối lượng công việc, việc đo lường
các số liệu bao gồm tính toán thông lượng, bộ nhớ băng thông, điện năng tính hiệu quả, và việc mở rộng quy mô
các đặc điểm (Reddi et al. 2019; Mattson et al. 2020) (System benchmarks establish standardized methodologies for evaluating hardware performance across AI workloads, measuring metrics including computational throughput, memory bandwidth, power efficiency, and scaling characteristics (Reddi et al. 2019; Mattson et al. 2020)).
Hệ thống các điểm chuẩn phục vụ hai chức năng (System benchmarks serve two functions). Cho những người thực hành, chúng kích hoạt được thông tin phần cứng
sự lựa chọn bằng cách việc cung cấp mang tính so sánh dữ liệu qua các cấu hình (For practitioners, they enable informed hardware selection by providing comparative data across configurations). Cho các nhà sản xuất, chúng định lượng
thuộc về thế hệ các sự cải thiện và hướng dẫn máy gia tốc sự phát triển (For manufacturers, they quantify generational improvements and guide accelerator development). Sự đồng-tiến hóa đã là ấn tượng (dramatic):
khi GPU sự áp dụng đã tăng trưởng, độ chính xác đã cải thiện một cách nhanh chóng, việc chứng minh rằng phần cứng và thuật toán
các tiến bộ thúc đẩy tiến bộ trong song song (tandem) (The co-evolution has been dramatic: as GPU adoption grew, accuracy improved rapidly, demonstrating that hardware and algorithmic advances drive progress in tandem).
Hiệu quả điểm chuẩn sự diễn giải yêu cầu việc biết hiệu suất các đặc điểm của mục tiêu
phần cứng (Effective benchmark interpretation requires knowing the performance characteristics of target hardware). Liệu một cụ thể AI khối lượng công việc là bị ràng buộc tính toán hay bị ràng buộc-bộ nhớ cung cấp thiết yếu
sự thấu hiểu cho sự tối ưu hóa các quyết định (Whether a specific AI workload is compute bound or memory-bound provides essential insight for optimization decisions). Tính toán cường độ, được đo lường như FLOP/byte9, xác định
hiệu suất các giới hạn (Computational intensity, measured as FLOP/byte9, determines performance limits). Xem xét một NVIDIA A100 GPU với 312 TFLOP/s của FP16 Tensor Lõi
hiệu suất (FP32 là 19.5 TFLOP/s) và 2.04 TB/s bộ nhớ băng thông (SXM biến thể) (Consider an NVIDIA A100 GPU with 312 TFLOP/s of FP16 Tensor Core performance (FP32 is 19.5 TFLOP/s) and 2.04 TB/s memory bandwidth (SXM variant)). Việc chia
đỉnh tính toán cho đỉnh băng thông mang lại một số học cường độ ngưỡng của 153 FLOP/byte (Dividing peak compute by peak bandwidth yields an arithmetic intensity threshold of 153 FLOP/byte).
Các khối lượng công việc bên dưới này ngưỡng là bị nút thắt cổ chai bởi bộ nhớ băng thông, trong khi những cái bên trên là
bị nút thắt cổ chai bởi tính toán dung lượng (Workloads below this threshold are bottlenecked by memory bandwidth, while those above are bottlenecked by compute capacity). Roofline mô hình trong phần 11.6 cung cấp thuộc về kiến trúc

12. Việc đo điểm chuẩn (Benchmarking)
651
10
Roofline
Mô hình (Model):
Williams et al. (2009) đã giới-
thiệu Berkeley mô hình,
được đặt tên cho hình ảnh hình dạng
của của nó hiệu suất trần (Roofline Model: Williams et al. (2009) introduced the Berkeley model, named for the visual shape of its performance ceiling). Của nó
sườn núi điểm (đỉnh FLOP/s
được chia bởi đỉnh băng thông)
tách biệt
bị ràng buộc-bộ nhớ
khỏi bị ràng buộc-tính toán các khối lượng-
công việc,
việc cho thấy
liệu
sự tối ưu hóa nên nhắm mục tiêu
dữ liệu sự di chuyển hay số học (Its ridge point (peak FLOP/s divided by peak bandwidth) separates memory-bound from compute-bound workloads, showing whether optimization should target data movement or arithmetic).
Lớn hơn các lô đẩy transformer
suy luận từ bị ràng buộc-bộ nhớ tới
bị ràng buộc-tính toán (Larger batches push transformer inference from memory-bound to compute-bound).
nền tảng cho việc diễn giải những các điểm chuẩn các kết quả này (foundation for interpreting these benchmark results). Phần D.2.1 suy luận ra roofline phương trình và
sườn núi-điểm ngưỡng từ đầu tiên các nguyên tắc, do đó số học cường độ ranh giới được sử dụng ở đây có thể được
tái tạo cho bất kỳ máy gia tốc nào (Section D.2.1 derives the roofline equation and the ridge-point threshold from first principles, so the arithmetic intensity bound used here can be reconstructed for any accelerator).
Định nghĩa 12.2: Máy học hệ thống các điểm chuẩn (Machine learning system benchmarks)
Máy Học Hệ thống Các điểm chuẩn là được chuẩn hóa sự đánh giá các giao thức thứ mà giữ khối lượng
công việc và chất lượng mục tiêu cố định trong khi việc làm biến đổi phần cứng-phần mềm ngăn xếp, việc đo lường
𝜂hw = 𝑅sustained/𝑅peak và 𝐿lat để cô lập cơ sở hạ tầng tính hiệu quả khỏi thuật toán các sự cải
thiện (Machine Learning System Benchmarks are standardized evaluation protocols that hold the workload and quality target constant while varying the hardware-software stack, measuring 𝜂hw = 𝑅sustained/𝑅peak and 𝐿lat to isolate infrastructure efficiency from algorithmic improvements).
1. Ý nghĩa (Significance): Cùng ResNet-50 mô hình có thể cung cấp rất khác nhau thông lượng qua
phần cứng các ngăn xếp, độ chính xác các định dạng, lô các kích thước, và trình biên dịch các cấu hình, tuy nhiên vẫn báo-
cáo cùng ImageNet Top-1 độ chính xác (The same ResNet-50 model can deliver very different throughput across hardware stacks, precision formats, batch sizes, and compiler configurations, yet still report the same ImageNet Top-1 accuracy). Hệ thống các điểm chuẩn nắm bắt này sự triển khai
khoảng cách, thứ mà là vô hình tới thuật toán các điểm chuẩn thứ mà chỉ báo cáo độ chính xác (System benchmarks capture this implementation gap, which is invisible to algorithmic benchmarks that only report accuracy).
2. Sự phân biệt (Distinction): Không giống như thuật toán các điểm chuẩn (thứ mà làm biến đổi mô hình các kiến trúc và huấn-
luyện các thủ tục để cải thiện sự hội tụ độ chính xác), hệ thống các điểm chuẩn giữ thuật toán
cố định và làm biến đổi sự triển khai (hạt nhân các thư viện, sự lượng tử hóa các định dạng, lô các kích thước, và
phần cứng các thế hệ) để đo lường cách nào một cách hiệu quả phần cứng-phần mềm ngăn xếp thực thi
sắt định luật’s 𝑂/(𝑅peak ⋅𝜂hw) thuật ngữ (Unlike algorithmic benchmarks (which vary model architectures and training procedures to improve convergence accuracy), system benchmarks hold the algorithm fixed and vary the implementation (kernel libraries, quantization formats, batch sizes, and hardware generations) to measure how efficiently the hardware-software stack executes the iron law’s 𝑂/(𝑅peak ⋅𝜂hw) term).
3. Chung cạm bẫy (Common pitfall): Một thường xuyên sự quan niệm sai lầm là rằng một hệ thống điểm chuẩn kết quả khái quát hóa
qua các khối lượng công việc (A frequent misconception is that a system benchmark result generalizes across workloads). Một máy gia tốc thứ mà đạt được cao sự sử dụng trên ResNet-50 (một thân thiện-
tính toán thị giác khối lượng công việc) có thể đạt được nhiều thấp hơn sự sử dụng trên một sự khuyến nghị
hệ thống (một bị ràng buộc-băng thông-bộ nhớ khối lượng công việc) (An accelerator that achieves high utilization on ResNet-50 (a compute-friendly vision workload) may achieve much lower utilization on a recommendation system (a memory-bandwidth-bound workload)). Hệ thống các điểm chuẩn là cụ thể-
khối lượng công việc; không đơn số liệu nào đặc trưng cho một phần cứng nền tảng (System benchmarks are workload-specific; no single metric characterizes a hardware platform).
Roofline vị trí10 phụ thuộc trên khối lượng công việc (Roofline position10 depends on the workload). Trong này đã làm việc A100 ví dụ, cao-cường độ
các hoạt động chẳng hạn như dày đặc ma trận các phép nhân trong một ResNet-50 tiến bước tại lớn lô các kích thước
tiếp cận số học các cường độ xung quanh ~300 FLOP/byte, bên trên A100 sườn núi, và do đó hành xử
như bị ràng buộc-tính toán các hạt nhân (He et al. 2016a; Choquette et al. 2021) (In this worked A100 example, high-intensity operations such as dense matrix multiplications in a ResNet-50 forward pass at large batch sizes reach arithmetic intensities around ~300 FLOP/byte, above the A100 ridge, and therefore behave as compute-bound kernels (He et al. 2016a; Choquette et al. 2021)). Thấp-cường độ các hoạt động rơi
xa bên dưới sườn núi vào bị ràng buộc-bộ nhớ chế độ: một BERT suy luận tại lô kích thước một, việc đếm
chỉ việc tải-trọng số lưu lượng, tiếp cận chỉ ~50 FLOP/byte số học cường độ và một nhỏ phần của
đỉnh (Low-intensity operations fall far below the ridge into the memory-bound regime: a BERT inference at batch size one, counting only weight-loading traffic, reaches only ~50 FLOP/byte arithmetic intensity and a small fraction of peak). Việc làm tăng lô kích thước di chuyển đó cùng khối lượng công việc qua sườn núi từ bị ràng buộc-bộ nhớ tới
bị ràng buộc-tính toán (Pope et al. 2023) (Increasing the batch size moves that same workload across the ridge from memory-bound to compute-bound (Pope et al. 2023)). Phần D.2.1.1 làm việc cường độ-tới-sự sử dụng sự tính toán đầu
tới đầu trên A100, việc đối chiếu một bị ràng buộc-tính toán GEMM chống lại một bị ràng buộc-bộ nhớ khôn ngoan-theo-phần tử
hoạt động, do đó các bước khái quát hóa tới bất kỳ mô hình-phần cứng cặp nào (Section D.2.1.1 works the intensity-to-utilization calculation end to end on the A100, contrasting a compute-bound GEMM against a memory-bound element-wise operation, so the steps generalize to any model-hardware pair).
Một đã làm việc BERT suy luận ước tính cho thấy cách nào những roofline các nguyên tắc này dịch thuật thành cụ thể
sự triển khai các dự đoán (A worked BERT inference estimate shows how these roofline principles translate into concrete deployment predictions).
Khăn ăn (Napkin) Toán 12.2: Roofline sự phân tích cho BERT suy luận (Roofline analysis for BERT inference)
Vấn đề: BERT-Cơ sở phải được triển khai cho suy luận trên một A100 GPU (Problem: BERT-Base must be deployed for inference on an A100 GPU). Sự quản lý mong đợi
cao GPU sự sử dụng (Management expects high GPU utilization). Cái gì hiệu suất nên chúng ta dự đoán, và làm thế nào có thể chúng ta cải thiện nó? (What performance should we predict, and how can we improve it?)
Bước 1: Phần cứng các giới hạn (Hardware limits).
• Đỉnh tính toán: 312 TFLOP/s (FP16 Tensor Lõi) (Peak compute: 312 TFLOP/s (FP16 Tensor Core))
• Bộ nhớ băng thông: 2.04 TB/s (Memory bandwidth: 2.04 TB/s)
• Sườn núi điểm: 312 TFLOP/s ÷ 2.04 TB/s = 153 FLOP/byte (Ridge point: 312 TFLOP/s ÷ 2.04 TB/s = 153 FLOP/byte)
Bất kỳ khối lượng công việc nào với số học cường độ bên dưới 153 FLOP/byte là bị ràng buộc bộ nhớ; bên trên là
bị ràng buộc tính toán (Any workload with arithmetic intensity below 153 FLOP/byte is memory bound; above is compute bound).
Bước 2: BERT-cơ sở các đặc điểm (BERT-base characteristics).
• Các tham số: 110M = 440 MB (FP32) (Parameters: 110M = 440 MB (FP32))
652
12.3 Hệ thống Việc đo điểm chuẩn Các bộ phần mềm (System Benchmarking Suites)
• FLOPs mỗi suy luận: ~22 GFLOP (tiến bước với chuỗi độ dài 𝑆= 128) (FLOPs per inference: ~22 GFLOP (forward pass with sequence length 𝑆= 128))
• Dữ liệu sự di chuyển: ~440 MB (phải tải tất cả các trọng số từ bộ nhớ) (Data movement: ~440 MB (must load all weights from memory))
• Số học cường độ: (22×109)÷(440×106) = 50 FLOP/byte (chỉ-các trọng số mô hình; xem
lưu ý trong chính văn bản) (Arithmetic intensity: (22×109)÷(440×106) = 50 FLOP/byte (weights-only model; see note in main text))
Bước 3: Hiệu suất sự dự đoán (Performance prediction). Bởi vì 50 FLOP/byte < 153 FLOP/byte, BERT tại lô = 1 là
bị ràng buộc bộ nhớ (Since 50 FLOP/byte < 153 FLOP/byte, BERT at batch = 1 is memory bound):
Có thể đạt được hiệu suất = 50 FLOP/byte × 2.04 TB/s = 102 TFLOP/s (Achievable perf = 50 FLOP/byte × 2.04 TB/s = 102 TFLOP/s)
GPU sự sử dụng = 102 TFLOP/s ÷ 312 TFLOP/s = 32.7% (GPU utilization = 102 TFLOP/s ÷ 312 TFLOP/s = 32.7%)
Bước 4: Sự tối ưu hóa thông qua việc làm theo lô (Optimization via batching). Làm tăng lô kích thước lên 32 (Increase batch size to 32):
• Cùng 440 MB của các trọng số, nhưng 32× nhiều hơn tính toán (Same 440 MB of weights, but 32× more compute)
• Mới FLOPs: 22×109 ×32 = 704 GFLOP (New FLOPs: 22×109 ×32 = 704 GFLOP)
• Mới cường độ: (704×109)÷(440×106) = 1600 FLOP/byte (New intensity: (704×109)÷(440×106) = 1600 FLOP/byte)
Bởi vì 1600 FLOP/byte > 153 FLOP/byte, lô = 32 là bị ràng buộc tính toán (Since 1600 FLOP/byte > 153 FLOP/byte, batch = 32 is compute bound):
Có thể đạt được hiệu suất ≈85% × 312 TFLOP/s = 265.2 TFLOP/s (Achievable perf ≈85% × 312 TFLOP/s = 265.2 TFLOP/s)
GPU sự sử dụng ≈85% (GPU utilization ≈85%)
Các hệ thống sự thấu hiểu (Systems insight): Lô kích thước biến đổi bị ràng buộc-bộ nhớ suy luận (32.7 phần trăm sự sử dụng) thành
bị ràng buộc-tính toán suy luận (85 phần trăm sự sử dụng) (Batch size transforms memory-bound inference (32.7 percent utilization) into compute-bound inference (85 percent utilization)). Việc làm theo lô, tuy nhiên, làm tăng độ trễ bởi vì
hệ thống phải chờ để tích lũy các yêu cầu (Batching, however, increases latency because the system must wait to accumulate requests). Đây là cơ bản thông lượng-độ trễ
sự đánh đổi thứ mà MLPerf các kịch bản nắm bắt: Đơn Luồng (SingleStream) (lô = 1, được tối ưu hóa-độ trễ) so với Ngoại tuyến (Offline)
(tối đa lô, được tối ưu hóa-thông lượng) (This is the fundamental throughput-latency trade-off that MLPerf scenarios capture: SingleStream (batch = 1, latency-optimized) vs. Offline (maximum batch, throughput-optimized)).
Hệ thống các điểm chuẩn đánh giá hiệu suất qua các quy mô, trải dài từ đơn-chip các cấu hình
tới lớn được phân phối các hệ thống và việc bao phủ AI các khối lượng công việc thứ mà bao gồm cả hai huấn luyện và suy luận
các tác vụ (System benchmarks evaluate performance across scales, ranging from single-chip configurations to large distributed systems and covering AI workloads that include both training and inference tasks). Này sự đánh giá cách tiếp cận đảm bảo rằng các điểm chuẩn một cách chính xác phản ánh thực-thế giới sự triển khai
các kịch bản và cung cấp các sự thấu hiểu thứ mà thông báo cả hai phần cứng sự lựa chọn các quyết định và hệ thống kiến trúc
thiết kế (This evaluation approach ensures that benchmarks accurately reflect real-world deployment scenarios and deliver insights that inform both hardware selection decisions and system architecture design). Hình 12.1 tiết lộ sự tương quan giữa GPU sự áp dụng và ImageNet phân loại lỗi
các tỷ lệ từ 2010 tới 2014: khi GPU các mục (entries) dâng trào từ 0 lên 110, top-5 lỗi các tỷ lệ đã sụt giảm từ 28.2
phần trăm xuống 7.3 phần trăm (Russakovsky et al. 2015; Krizhevsky et al. 2012), việc minh họa cách nào phần cứng
các khả năng và thuật toán các tiến bộ có thể thúc đẩy tiến bộ trong song song (Figure 12.1 reveals the correlation between GPU adoption and ImageNet classification error rates from 2010 to 2014: as GPU entries surged from 0 to 110, top-5 error rates dropped from 28.2 percent to 7.3 percent (Russakovsky et al. 2015; Krizhevsky et al. 2012), illustrating how hardware capabilities and algorithmic advances can drive progress in tandem).
0.0
10.0
20.0
30.0
0.0
25.0
50.0
75.0
100.0
125.0
# of Entries Using GPUs
2010
2011
2012
2013
2014
0.0
10.0
20.0
30.0
Year
Top-5 Error Rate (%)
Hình 12.1: GPU Sự áp dụng và Lỗi Sự giảm bớt (GPU Adoption and Error Reduction): Khi GPU các mục (entries) trong ImageNet đã dâng trào từ 0 lên 110 giữa 2010 và 2014,
top-5 lỗi các tỷ lệ đã sụt giảm từ 28.2 phần trăm xuống 7.3 phần trăm, việc chứng minh sự đồng-tiến hóa của phần cứng các khả năng và
thuật toán các tiến bộ (As GPU entries in ImageNet surged from 0 to 110 between 2010 and 2014, top-5 error rates dropped from 28.2 percent to 7.3 percent, demonstrating the co-evolution of hardware capabilities and algorithmic advances). Các nguồn (Sources): (Russakovsky et al. 2015; Krizhevsky et al. 2012).
ImageNet ví dụ chứng minh cách nào phần cứng các tiến bộ kích hoạt thuật toán các bước đột phá (The ImageNet example demonstrates how hardware advances enable algorithmic breakthroughs).
(Chúng ta xem xét lại này sự tiến triển với cụ thể-mô hình thuộc về kiến trúc các cột mốc trong phần 12.11.1.) ((We revisit this progression with model-specific architectural milestones in section 12.11.1.)) Hiệu quả (Effective)

12. Việc đo điểm chuẩn (Benchmarking)
653
hệ thống việc đo điểm chuẩn, tuy nhiên, yêu cầu việc hiểu mối quan hệ giữa khối lượng công việc các đặc-
điểm và phần cứng sự sử dụng (system benchmarking, however, requires understanding the relationship between workload characteristics and hardware utilization). Hiện đại AI các hệ thống hiếm khi đạt được lý thuyết đỉnh hiệu suất
do các sự tương tác giữa tính toán các mẫu, bộ nhớ các hệ thống phân cấp, và hệ thống các kiến trúc (Modern AI systems rarely achieve theoretical peak performance due to interactions between computational patterns, memory hierarchies, and system architectures).
Này khoảng cách giữa lý thuyết và đạt được hiệu suất định hình cách nào chúng ta thiết kế có ý nghĩa hệ thống
các điểm chuẩn (This gap between theoretical and achieved performance shapes how we design meaningful system benchmarks).
Thực tế phần cứng sự sử dụng các mẫu là thiết yếu cho có thể hành động điểm chuẩn thiết kế (Realistic hardware utilization patterns are essential for actionable benchmark design). Như
trước đó roofline sự phân tích đã chứng minh, GPU sự sử dụng biến đổi một cách ấn tượng với lô kích thước và
mô hình kiến trúc—từ 85 phần trăm cho bị ràng buộc-tính toán các khối lượng công việc tới 32.7 phần trăm cho bị ràng buộc-
bộ nhớ đơn-yêu cầu suy luận (As the preceding roofline analysis demonstrated, GPU utilization varies dramatically with batch size and model architecture—from 85 percent for compute-bound workloads to 32.7 percent for memory-bound single-request inference). Những các mẫu này mở rộng tới bộ nhớ băng thông: nặng-tham số
transformer suy luận và nặng-sự kích hoạt tích chập các khối lượng công việc làm căng thẳng khác nhau các phần của
bộ nhớ hệ thống phân cấp, một cách trực tiếp việc tác động có thể đạt được hiệu suất qua khác nhau độ chính xác các cấp độ (These patterns extend to memory bandwidth: parameter-heavy transformer inference and activation-heavy convolutional workloads stress different parts of the memory hierarchy, directly impacting achievable performance across different precision levels).
Sự hợp nhất qua những các yếu tố này là rằng hiệu quả hệ thống các điểm chuẩn phải đo lường thực tế
sự sử dụng thay vì đỉnh lý thuyết khả năng, và một vài phạm vi các ranh giới rơi ra khỏi đó
yêu cầu (The consolidation across these factors is that effective system benchmarks must measure realistic utilization rather than peak theoretical capability, and several scope boundaries fall out of that requirement). Năng lượng là một chiều: hiệu suất mỗi watt biến đổi bởi ba các bậc của độ lớn
qua các nền tảng, và một máy gia tốc bị sử dụng dưới mức tiêu thụ không tương xứng điện năng cho của nó đầu ra,
việc phạt cả hai thuộc về hoạt động chi phí và thuộc về môi trường tác động (Energy is one dimension: performance per watt varies by three orders of magnitude across platforms, and an underutilized accelerator consumes disproportionate power for its output, penalizing both operational cost and environmental impact). Sự phân phối là một cái khác: nhiều-nút
huấn luyện thêm giao tiếp các nút thắt cổ chai, mạng-tô pô các hiệu ứng, và sự phối hợp chi phí chung thứ mà
đơn-nút các điểm chuẩn không thể nắm bắt và thứ mà đảm bảo được dành riêng sự đối xử vượt ra ngoài cuốn sách này (Distribution is another: multi-node training adds communication bottlenecks, network-topology effects, and coordination overhead that single-node benchmarks cannot capture and that warrant dedicated treatment beyond this book).
Bên trong đơn-máy phạm vi ở đây, nhiều-GPU việc đo điểm chuẩn thay vì đó tập trung trên nội-nút
giao tiếp, bộ nhớ-băng thông sự sử dụng qua các máy gia tốc, và gradient-sự đồng bộ hóa
tính hiệu quả trong được chia sẻ-bộ nhớ các hệ thống, nơi 4-8 các GPU trên NVLink hoặc PCIe cung cấp tính song song
mà không mạng các thách thức của nhiều-nút các cụm (Within the single-machine scope here, multi-GPU benchmarking instead focuses on intra-node communication, memory-bandwidth utilization across accelerators, and gradient-synchronization efficiency in shared-memory systems, where 4-8 GPUs on NVLink or PCIe deliver parallelism without the network challenges of multi-node clusters). Qua tất cả của những cái này, một điểm chuẩn kiếm được của nó
giá trị chỉ khi của nó hoạt động điểm khớp của sự triển khai, không phải của bảng dữ liệu (Across all of these, a benchmark earns its value only when its operating point matches the deployment’s, not the datasheet’s).
12.3.3 Được thúc đẩy bởi cộng đồng sự chuẩn hóa (Community-driven standardization)
Phần cứng sự sử dụng các sự thấu hiểu là chỉ hữu ích cho sự so sánh khi được đo lường một cách nhất quán, điều mà
yêu cầu được thúc đẩy bởi cộng đồng sự chuẩn hóa (The hardware utilization insights are only useful for comparison when measured consistently, which requires community-driven standardization). Khi một nhóm đo lường suy luận độ trễ với
sự tiền xử lý được bao gồm và một cái khác loại trừ nó, khi độ chính xác các điểm chuẩn sử dụng khác nhau dữ liệu
các sự chia tách (splits), hoặc khi điện năng các sự đo lường sử dụng khác nhau hệ thống các ranh giới, có ý nghĩa sự so sánh
trở thành không thể (When one team measures inference latency with preprocessing included and another excludes it, when accuracy benchmarks use different data splits, or when power measurements employ different system boundaries, meaningful comparison becomes impossible). Cá nhân các tổ chức không thể thiết lập sự đo lường các tiêu chuẩn một mình; sự
phát triển nhanh của các điểm chuẩn qua của chúng ta ba các chiều tạo ra sự phân mảnh thứ mà chỉ được phối hợp
nỗ lực có thể giải quyết (Individual organizations cannot establish measurement standards alone; the proliferation of benchmarks across our three dimensions creates fragmentation that only coordinated effort can resolve).
Nhiều thành công nhất các điểm chuẩn nổi lên thông qua rộng sự hợp tác giữa học thuật các tổ chức,
công nghiệp các đối tác, và miền các chuyên gia (The most successful benchmarks emerge through broad collaboration among academic institutions, industry partners, and domain experts). ImageNet’s lâu dài tác động chứng minh cách nào được duy trì
cộng đồng sự tham gia thông qua các hội thảo, các thách thức, và mở các tập dữ liệu thiết lập thẩm quyền thứ mà
được thúc đẩy bởi tập đoàn các điểm chuẩn hiếm khi đạt được (ImageNet’s lasting impact demonstrates how sustained community engagement through workshops, challenges, and open datasets establishes authority that corporate-driven benchmarks rarely achieve). Này mang tính hợp tác sự phát triển tạo ra một nền tảng
cho chính thức sự chuẩn hóa: IEEE làm việc các nhóm (IEEE Standards Association 2024) và ISO/IEC
kỹ thuật các ủy ban (ISO 2024) hệ thống hóa được phát triển bởi cộng đồng các phương pháp luận thành chính thức các tiêu chuẩn
(ví dụ, IEEE 2416 (IEEE Standards Association 2019a) cho hệ thống điện năng việc mô hình hóa), việc cung cấp
chính xác sự đo lường các thông số kỹ thuật thứ mà kích hoạt đáng tin cậy chéo-tổ chức sự so sánh (This collaborative development creates a foundation for formal standardization: IEEE working groups (IEEE Standards Association 2024) and ISO/IEC technical committees (ISO 2024) codify community-developed methodologies into official standards (for example, IEEE 2416 (IEEE Standards Association 2019a) for system power modeling), providing precise measurement specifications that enable reliable cross-institutional comparison). Các dự án
thứ mà cung cấp mã nguồn mở tham chiếu các sự triển khai, được đóng vùng chứa sự đánh giá các môi trường, và
toàn diện sự xác nhận các bộ phần mềm xa hơn giảm bớt các rào cản và đảm bảo nhất quán sự diễn giải qua
nghiên cứu các nhóm (Projects that provide open-source reference implementations, containerized evaluation environments, and comprehensive validation suites further reduce barriers and ensure consistent interpretation across research groups).
ML các điểm chuẩn phải cân bằng học thuật sự nghiêm ngặt với công nghiệp tính thực tế, do lý thuyết các tiến bộ
phải dịch thuật thành thực tế các sự cải thiện trong được triển khai các hệ thống (Mattson et al. 2020; Reddi et al. 2019) (ML benchmarks must balance academic rigor with industry practicality, since theoretical advances must translate to practical improvements in deployed systems (Mattson et al. 2020; Reddi et al. 2019)).
Các điểm chuẩn thứ mà nổi lên từ này sự cân bằng, với minh bạch sự quản trị và đều đặn sự tiến hóa,
trở thành bền bỉ tham chiếu các điểm; những cái được phát triển trong sự cô lập đấu tranh để giành được lực kéo (traction) bất kể của
kỹ thuật sự tinh vi (Benchmarks that emerge from this balance, with transparent governance and regular evolution, become durable reference points; those developed in isolation struggle to gain traction regardless of technical sophistication). Những sự đánh giá phương pháp luận các nguyên tắc này hướng dẫn cả hai huấn luyện và suy luận
điểm chuẩn thiết kế xuyên suốt này chương (These evaluation methodology principles guide both training and inference benchmark design throughout this chapter).
Cộng đồng các tiêu chuẩn đảm bảo tính có thể tái tạo, nhưng chúng không quy định cấp độ của chi tiết tại đó
các sự đo lường nên được lấy (Community standards ensure reproducibility, but they do not prescribe the level of detail at which measurements should be taken). Một điểm chuẩn có thể tính thời gian một đơn ma trận phép nhân hay một toàn bộ
huấn luyện lượt chạy—và mỗi sự lựa chọn tiết lộ khác nhau các loại của thông tin (A benchmark could time a single matrix multiplication or an entire training run—and each choice reveals different kinds of information). Chiều sâu của sự đo lường,
từ cá nhân các hoạt động tới hoàn chỉnh các hệ thống, xác định cái gì các sự thấu hiểu các điểm chuẩn có thể cung cấp
và cái nào các vấn đề chúng có thể chẩn đoán (The depth of measurement, from individual operations to complete systems, determines what insights benchmarks can provide and which problems they can diagnose).

654
12.4 Việc đo điểm chuẩn Tính hạt (Benchmarking Granularity)
11
cuDNN (CUDA Sâu
Thần kinh
Mạng
Thư viện (Library)):
Được phát hành bởi NVIDIA vào 2014,
cuDNN cung cấp được điều chỉnh thủ công
hạt nhân
các sự triển khai
cho
các tích chập,
việc gộp (pooling),
và
sự chuẩn hóa (cuDNN (CUDA Deep Neural Network Library): Released by NVIDIA in 2014, cuDNN provides hand-tuned kernel implementations for convolutions, pooling, and normalization).
Sự
việc đo điểm chuẩn
hàm ý:
được báo cáo suy luận các độ trễ
phụ thuộc nặng nề trên cái nào
cuDNN phiên bản và thuật-
toán tự động điều chỉnh các cài đặt đã được
sử dụng, việc làm cho cuDNN phiên bản
một bắt buộc phần tử của bất kỳ
có thể tái tạo
điểm chuẩn
sự thông số kỹ thuật nào (The benchmarking implication: reported inference latencies depend heavily on which cuDNN version and algorithm autotuner settings were used, making cuDNN version a mandatory element of any reproducible benchmark specification).
12.4 Việc đo điểm chuẩn Tính hạt (Benchmarking Granularity)
Một GPU hạt nhân thứ mà chạy 3× nhanh hơn trong sự cô lập có thể cung cấp không đầu-tới-đầu sự tăng tốc nếu dữ liệu
đường ống không thể giữ nhịp độ (A GPU kernel that runs 3× faster in isolation may deliver zero end-to-end speedup if the data pipeline cannot keep pace). Này mang tính chẩn đoán thất bại minh họa một cơ bản thiết kế sự lựa chọn: cấp độ
của chi tiết tại đó sự đánh giá xảy ra (This diagnostic failure illustrates a fundamental design choice: the level of detail at which evaluation occurs). Sự chuẩn hóa quy định cách nào sự đo lường là nhất quán, trong khi
việc đo điểm chuẩn tính hạt quy định cái gì được đo lường (Standardization specifies how measurement is consistent, while benchmarking granularity specifies what is measured). Mỗi sự xác nhận chiều có thể được đánh giá
tại khác nhau các quy mô, từ cá nhân các hoạt động tới hoàn chỉnh các quy trình làm việc, với mỗi tính hạt cấp độ
việc tiết lộ khác nhau các loại của các vấn đề (Each validation dimension can be assessed at different scales, from individual operations to complete workflows, with each granularity level revealing different kinds of problems):
• Vi (Micro) các điểm chuẩn cô lập cá nhân các thành phần: hạt nhân sự thực thi thời gian, bộ nhớ băng thông
sự sử dụng, đơn-lớp độ chính xác (Micro benchmarks isolate individual components: kernel execution time, memory bandwidth utilization, single-layer accuracy). Những cái này chẩn đoán nơi các vấn đề xảy ra (These diagnose where problems occur).
• Vĩ (Macro) các điểm chuẩn đánh giá các hệ thống con: đầy đủ mô hình huấn luyện sự hội tụ, suy luận đường ống
thông lượng, tập dữ liệu thiên vị các số liệu (Macro benchmarks evaluate subsystems: full model training convergence, inference pipeline throughput, dataset bias metrics). Những cái này tiết lộ cái gì các vấn đề tồn tại (These reveal what problems exist).
• Đầu-tới-đầu các điểm chuẩn đo lường hoàn chỉnh các quy trình làm việc: yêu cầu-tới-phản hồi độ trễ bao-
gồm sự tiền xử lý, huấn luyện thời gian-tới-độ chính xác bao gồm dữ liệu việc tải, mô hình hiệu suất trên
sản xuất dữ liệu các sự phân phối (End-to-end benchmarks measure complete workflows: request-to-response latency including preprocessing, training time-to-accuracy including data loading, model performance on production data distributions). Những cái này cho thấy liệu hệ thống làm việc (These show whether the system works).
Các sự tối ưu hóa các kỹ thuật từ Phần III hoạt động tại khác nhau các tính hạt (hạt nhân sự dung hợp nhắm mục tiêu
vi hiệu suất, việc cắt tỉa (pruning) ảnh hưởng vĩ mô hình hành vi, dữ liệu sự tuyển chọn (curation) xác định đầu-tới-đầu
sự khái quát hóa) và sự xác nhận phải khớp (The optimization techniques from Part III operate at different granularities (kernel fusion targets micro performance, pruning affects macro model behavior, data curation determines end-to-end generalization) and validation must match). Một vi điểm chuẩn có thể cho thấy hạt nhân sự tăng tốc trong khi
một vĩ điểm chuẩn tiết lộ bộ nhớ các nút thắt cổ chai thứ mà phủ nhận khoản đạt được; một đầu-tới-đầu điểm chuẩn
có thể phơi bày dữ liệu đường ống các sự đình trệ (stalls) vô hình tại bất kỳ cái khác cấp độ nào (A micro benchmark might show kernel speedup while a macro benchmark reveals memory bottlenecks that negate the gain; an end-to-end benchmark might expose data pipeline stalls invisible at any other level).
Hình 12.2 ánh xạ những tính hạt các cấp độ này lên ML ngăn xếp bằng cách việc phá vỡ ngăn xếp thành bốn
khác biệt sự đánh giá các phạm vi (Figure 12.2 maps these granularity levels onto the ML stack by breaking the stack into four distinct evaluation scopes). Mỗi phạm vi một cách tiến bộ mở rộng sự đo lường ranh giới: vi-
các điểm chuẩn cô lập thần kinh mạng các lớp, vĩ-các điểm chuẩn bao quanh hoàn chỉnh các mô hình, ứng-
dụng các điểm chuẩn thêm việc hỗ trợ tính toán, và đầu-tới-đầu các điểm chuẩn nắm bắt đầy đủ sự triển khai
ngữ cảnh bao gồm phi-AI các thành phần (Each scope progressively expands the measurement boundary: micro-benchmarks isolate neural network layers, macro-benchmarks encompass complete models, application benchmarks add supporting compute, and end-to-end benchmarks capture the full deployment context including non-AI components).
ML Các lớp (Layers)
Mô hình A (Model A)
Mô hình B (Model B)
ML Mô hình (Model)
AI Tác vụ 1 (AI Task 1)
Việc hỗ trợ Tính toán (Supporting Compute)
AI Tác vụ (AI Task)
AI Tính toán Nút (AI Compute Node)
Phi-AI Tính toán (Non-AI Compute)
Nút (Node)
AI Tính toán Nút (AI Compute Node)
Phi-AI Tính toán (Non-AI Compute)
Nút (Node)
Đầu-tới-Đầu Ứng dụng (End-to-End Application)
Hình 12.2: Việc đo điểm chuẩn Tính hạt (Benchmarking Granularity): Bốn-bảng khối biểu đồ việc cho thấy vi, vĩ, ứng dụng, và đầu-tới-đầu
sự đánh giá các lớp (Four-panel block diagram showing micro, macro, application, and end-to-end evaluation layers). Mỗi bảng ánh xạ một khác biệt phạm vi của sự đánh giá, từ được cô lập hạt nhân các hoạt động thông qua đầy đủ-hệ thống
sự triển khai, việc kích hoạt được nhắm mục tiêu sự tối ưu hóa tại mọi cấp độ của ML ngăn xếp (Each panel maps a distinct scope of assessment, from isolated kernel operations through full-system deployment, enabling targeted optimization at every level of the ML stack).
12.4.1 Vi các điểm chuẩn (Micro benchmarks)
Trong khi đầu-tới-đầu các điểm chuẩn tiết lộ tổng thể hệ thống hành vi, sự tối ưu hóa yêu cầu việc chỉ ra
chính xác cái nào các hoạt động tiêu thụ thời gian và năng lượng (While end-to-end benchmarks reveal overall system behavior, optimization requires pinpointing exactly which operations consume time and energy). Vi-các điểm chuẩn phục vụ này mang tính chẩn đoán mục đích
bằng cách việc cô lập cá nhân tensor các hoạt động, toán học các nguyên thủy (primitives) của cái mà phần cứng sự tối ưu hóa
chúng ta đã kiểm tra trong Chương 11 (Micro-benchmarks serve this diagnostic purpose by isolating individual tensor operations, the mathematical primitives whose hardware optimization we examined in Chapter 11).
Xem xét việc gỡ lỗi một chậm suy luận đường ống: vĩ các điểm chuẩn có thể cho thấy không thể chấp nhận được
độ trễ, nhưng chỉ vi-các điểm chuẩn tiết lộ liệu nút thắt cổ chai nằm trong các tích chập, sự chú ý
các cơ chế, hay bộ nhớ các bản sao (Consider debugging a slow inference pipeline: macro benchmarks might show unacceptable latency, but only micro-benchmarks reveal whether the bottleneck lies in convolutions, attention mechanisms, or memory copies). Này mang tính chẩn đoán độ chính xác làm cho vi-các điểm chuẩn thiết yếu cho
được nhắm mục tiêu sự tối ưu hóa thứ mà biến đổi lý thuyết phần cứng các khả năng thành được nhận ra hiệu suất
các khoản đạt được (This diagnostic precision makes micro-benchmarks essential for the targeted optimization that transforms theoretical hardware capabilities into realized performance gains). Những các điểm chuẩn này cô lập cá nhân các tác vụ để cung cấp chi tiết các sự thấu hiểu vào tính toán
các đòi hỏi của cụ thể hệ thống các phần tử, từ thần kinh mạng các lớp tới sự tối ưu hóa các kỹ thuật tới
sự kích hoạt các hàm (These benchmarks isolate individual tasks to provide detailed insights into the computational demands of particular system elements, from neural network layers to optimization techniques to activation functions).
Một chính lĩnh vực của vi-việc đo điểm chuẩn tập trung trên tensor các hoạt động, tính toán cốt lõi của sâu
học tập (A key area of micro-benchmarking focuses on tensor operations, the computational core of deep learning). Các thư viện giống như cuDNN11 (Chetlur et al. 2014) bởi NVIDIA cung cấp được tối ưu hóa các nguyên thủy
cho cốt lõi các tính toán chẳng hạn như các tích chập và ma trận các phép nhân qua khác nhau phần cứng
các cấu hình (Libraries like cuDNN11 (Chetlur et al. 2014) by NVIDIA provide optimized primitives for core computations such as convolutions and matrix multiplications across different hardware configurations). Vi-các điểm chuẩn xung quanh những các nguyên thủy này giúp các nhà phát triển hiểu cách nào của họ
phần cứng xử lý cốt lõi toán học các hoạt động thứ mà thống trị ML các khối lượng công việc (Micro-benchmarks around these primitives help developers understand how their hardware handles the core mathematical operations that dominate ML workloads).
Việc đo lường những các hoạt động này một cách chính xác yêu cầu kỷ luật (Measuring these operations correctly requires discipline). Một nhỏ tập hợp của sự đo lường các quy tắc
ngăn chặn chung các lỗi thứ mà có thể làm mất hiệu lực các kết quả hoàn toàn (A small set of measurement rules prevents common errors that can invalidate results entirely).

12. Việc đo điểm chuẩn (Benchmarking)
655
Các hệ thống Phối cảnh 12.4: Vi-việc đo điểm chuẩn các quy tắc (Systems Perspective 12.4: Micro-benchmarking rules)
Để tránh việc đo lường phần cứng các đồ tạo tác (artifacts) thay vì hạt nhân hiệu suất, theo sau Các Hệ thống
Thám tử’s Các quy tắc (To avoid measuring hardware artifacts instead of kernel performance, follow the Systems Detective’s Rules):
1. Khởi động quy tắc (The warm-up rule): Không đo lường lạnh-khởi động các vòng lặp như ổn định-trạng thái hiệu suất (Do not measure cold-start iterations as steady-state performance).
Hiện đại phần cứng sử dụng DVFS (động điện áp và tần số sự mở rộng quy mô) và Turbo Boost;
các bộ nhớ đệm, các hạt nhân, và các xung nhịp cần khởi động trước khi được đo lường vòng lặp đại diện được duy trì
hành vi (Modern hardware uses DVFS (dynamic voltage and frequency scaling) and Turbo Boost; caches, kernels, and clocks need warm-up before the measured loop represents sustained behavior).
2. Sự biến thiên quy tắc (The variance rule): Báo cáo Hệ số của Sự biến thiên (CV) (CV = 𝜎run/𝜇run), nơi
𝜎run và 𝜇run là chuẩn độ lệch và giá trị trung bình qua được lặp lại điểm chuẩn các lượt chạy (Report the Coefficient of Variation (CV) (CV = 𝜎run/𝜇run), where 𝜎run and 𝜇run are the standard deviation and mean across repeated benchmark runs). Nếu
CV > 0.05 (5 phần trăm), sự đo lường là ồn (If CV > 0.05 (5 percent), the measurement is noisy). Điều này thường chỉ ra nền OS
sự bồn chồn (jitter), nhiệt sự điều tiết (throttling), hay bộ nhớ sự tranh chấp (This usually indicates background OS jitter, thermal throttling, or memory contention).
3. “Tốc độ của ánh sáng” (SOL) kiểm tra (The “speed of light” (SOL) check): So sánh đạt được thông lượng chống lại roofline (Compare the achieved throughput against the roofline).
Nếu một hạt nhân đạt được 10 TFLOP/s trên một H100 (đỉnh ~989 TFLOP/s FP16, hay ~1,979 TFLOP/s
FP8 dày đặc), mang tính chẩn đoán bước là để nhận diện nguyên nhân của thấp sự sử dụng (thường hạt nhân
khởi chạy độ trễ từ quá nhiều nhỏ các hạt nhân) trước khi việc tối ưu hóa mã chính nó (If a kernel achieves 10 TFLOP/s on an H100 (peak ~989 TFLOP/s FP16, or ~1,979 TFLOP/s FP8 dense), the diagnostic step is to identify the cause of low utilization (often kernel launch latency from too many small kernels) before optimizing the code itself).
4. Sự xả quy tắc (The flush rule): Bộ nhớ băng thông các sự đo lường phải xả L2 bộ nhớ đệm giữa
các lượt chạy; nếu không được báo cáo “băng thông” phản ánh bộ nhớ đệm tốc độ (~5 TB/s–10 TB/s) thay vì
hơn DRAM tốc độ (~1 TB/s–2 TB/s) (Memory bandwidth measurements must flush the L2 cache between runs; otherwise the reported “bandwidth” reflects cache speed (~5 TB/s–10 TB/s) rather than DRAM speed (~1 TB/s–2 TB/s)).
Một bộ biên dịch (profiler) biến những sự đo lường các quy tắc này thành sắt-định luật bằng chứng bằng cách việc phân rã sự thực thi thời gian
thành các thuật ngữ được giới thiệu trong phần 1.7: dữ liệu sự di chuyển, tính toán thông lượng, và độ trễ chi phí chung (A profiler turns these measurement rules into iron-law evidence by decomposing execution time into the terms introduced in section 1.7: data movement, compute throughput, and latency overhead).
Các hệ thống Phối cảnh 12.5: Việc đo lường sắt định luật các thuật ngữ (Systems Perspective 12.5: Measuring the iron law terms)
Việc chuyển từ lý thuyết tới dấu vết (trace) có nghĩa là việc ánh xạ sắt định luật phương trình từ phần 1.7 lên một
bộ biên dịch (profiler) dòng thời gian (giống như Nsight Systems hoặc PyTorch Profiler) (Moving from theory to trace means mapping the iron law equation from section 1.7 onto a profiler timeline (like Nsight Systems or PyTorch Profiler)).
Việc đo lường dữ liệu thuật ngữ ( 𝐷vol
BW ) (Measuring the data term)
• Tín hiệu (Signal): Tìm kiếm cho “Bộ nhớ Thông lượng” hoặc “DRAM Băng thông” dòng (Look for the “Memory Throughput” or “DRAM Bandwidth” line).
• Công thức (Formula): BWeffective =
𝐷vol
𝑇kernel .
• Sự chẩn đoán (Diagnosis): Nếu BWeffective ≈BWpeak (ví dụ, >1.6 TB/s trên A100), hạt nhân là bị ràng buộc bộ nhớ
(If BWeffective ≈BWpeak (for example, >1.6 TB/s on A100), the kernel is memory bound). Việc tối ưu hóa tính toán (𝑂) sẽ làm không có gì (Optimizing compute (𝑂) will do nothing).
Việc đo lường đạt được tính toán thông lượng (𝑅peak ⋅𝜂hw) (Measuring achieved compute throughput)
• Tín hiệu (Signal): Tìm kiếm cho “SM Hoạt động” hoặc “Tính toán Thông lượng” (Look for “SM Active” or “Compute Throughput”).
• Công thức (Formula): Đạt được TFLOP/s =
𝑂
1012 𝑇kernel .
• Sự chẩn đoán (Diagnosis): Nếu Đạt được TFLOP/s ≪Đỉnh TFLOP/s VÀ BWeffective ≪BWpeak, hệ thống
là trong “Sự sử dụng Cạm bẫy”: có khả năng Bị ràng buộc Độ trễ (các hạt nhân quá nhỏ) hay Bị ràng buộc Lưới
(không đủ các luồng) (If Achieved TFLOP/s ≪Peak TFLOP/s AND BWeffective ≪BWpeak, the system is in the “Utilization Trap”: likely Latency Bound (kernels too small) or Grid Bound (not enough threads)).
Việc đo lường độ trễ thuật ngữ (𝐿lat) (Measuring the latency term)
• Tín hiệu (Signal): Tìm kiếm cho các khoảng cách (trống không gian) giữa có màu hạt nhân các thanh trên dòng thời gian (Look for gaps (empty space) between colored kernel bars on the timeline).
• Công thức (Formula): Chi phí chung Tỷ lệ =
𝑇gap
𝑇kernel+𝑇gap .
• Sự chẩn đoán (Diagnosis): Một “Răng cưa” mẫu (Tính toán, Khoảng cách, Tính toán, Khoảng cách) chỉ ra cao phần mềm
chi phí chung (A “Sawtooth” pattern (Compute, Gap, Compute, Gap) indicates high software overhead). Giải pháp là toán tử sự dung hợp, được bao phủ trong phần 11.8.1.3, hoặc CUDA Graphs,
thứ mà nắm bắt một được lặp lại chuỗi của GPU các sự khởi chạy do đó thời gian chạy có thể phát lại nó với
ít hơn CPU sự phân phối chi phí chung (The solution is operator fusion, covered in section 11.8.1.3, or CUDA Graphs, which capture a repeated sequence of GPU launches so the runtime can replay it with less CPU dispatch overhead).

656
12.4 Việc đo điểm chuẩn Tính hạt (Benchmarking Granularity)
Trong khi các điểm chuẩn giống như MLPerf tiết lộ cách nào nhanh một hệ thống là, vi-việc đo điểm chuẩn các công cụ tiết lộ tại sao nó
là chậm (While benchmarks like MLPerf reveal how fast a system is, micro-benchmarking tools reveal why it is slow). Để thực hiện này sự chẩn đoán, các kỹ sư sử dụng cấp độ-hạt nhân các bộ biên dịch (profilers) thứ mà nhìn lướt qua bên trong sự thực thi
của cá nhân các hoạt động (To perform this diagnosis, engineers use kernel-level profilers that peer inside the execution of individual operations).
Bộ khung các bộ biên dịch (profilers) (Framework profilers)
Các công cụ giống như PyTorch Profiler nắm bắt logic sự thực thi luồng của một huấn luyện hoặc suy luận bước (Tools like PyTorch Profiler capture the logical execution flow of a training or inference step). Chúng
nhận diện cái nào lớp thống trị thời gian chạy, liệu CPU và GPU công việc chồng chéo hay đồng bộ hóa
không cần thiết, và liệu dữ liệu bộ tải (loader) giữ máy gia tốc được cung cấp (They identify which layer dominates runtime, whether CPU and GPU work overlap or synchronize unnecessarily, and whether the data loader keeps the accelerator supplied). Mang tính chẩn đoán số liệu là
bước-thời gian sự phân tích qua dữ liệu việc tải, tính toán, và giao tiếp, bởi vì đó sự phân tích
nói cho kỹ sư cái nào hệ thống con sở hữu tiếp theo sự tối ưu hóa (The diagnostic metric is the step-time breakdown across data loading, compute, and communication, because that breakdown tells the engineer which subsystem owns the next optimization).
Hạt nhân các bộ biên dịch (profilers) (Kernel profilers)
Các công cụ giống như NVIDIA Nsight Systems và Compute nắm bắt vật lý sự thực thi trên phần cứng (Tools like NVIDIA Nsight Systems and Compute capture physical execution on the hardware). Chúng
xác định liệu một ma trận phép nhân là bị ràng buộc tính toán hay bị ràng buộc bộ nhớ, liệu
Luồng Các bộ đa xử lý đạt được cao sự chiếm chỗ, và liệu bộ nhớ các truy cập tuân theo việc hợp nhất (coalescing)
các quy tắc (They determine whether a matrix multiplication is compute bound or memory bound, whether the Streaming Multiprocessors reach high occupancy, and whether memory accesses obey coalescing rules). Mang tính chẩn đoán số liệu là roofline vị trí, bởi vì FLOP/s tương đối tới bộ nhớ băng thông
tiết lộ liệu nhiều hơn số học thông lượng có thể giúp hay liệu hạt nhân đang chờ đợi trên dữ liệu
sự di chuyển (The diagnostic metric is roofline position, because FLOP/s relative to memory bandwidth reveals whether more arithmetic throughput can help or whether the kernel is waiting on data movement).
Được khuyến nghị quy trình làm việc là để bắt đầu với Bộ khung Bộ biên dịch (Profiler) để tìm chậm lớp (ví
dụ, “Sự Chú ý Khối là chậm”) (The recommended workflow is to start with the Framework Profiler to find the slow layer (for example, “The Attention Block is slow”)). Sau đó, sử dụng Hạt nhân Bộ biên dịch (Profiler) để chẩn đoán vật lý (ví
dụ, “Softmax hạt nhân là bị ràng buộc bộ nhớ bởi vì nó đang đọc quá nhiều các byte mỗi FLOP”) (Then, use the Kernel Profiler to diagnose the physics (for example, “The Softmax kernel is memory bound because it is reading too many bytes per FLOP”)).
Này được nhắm mục tiêu cách tiếp cận tránh “sự tối ưu hóa mà không sự đo lường” cạm bẫy (This targeted approach avoids the “optimization without measurement” trap).
Vi-các điểm chuẩn cũng kiểm tra sự kích hoạt các hàm và thần kinh mạng các lớp trong sự cô lập (Micro-benchmarks also examine activation functions and neural network layers in isolation). Điều này
bao gồm việc đo lường hiệu suất của đa dạng sự kích hoạt các hàm giống như được chỉnh lưu tuyến tính đơn vị
(ReLU), Sigmoid, và Tanh dưới được kiểm soát các điều kiện, và việc đánh giá tính toán tính hiệu quả
của khác biệt thần kinh mạng các thành phần chẳng hạn như LSTM các tế bào (cells) hay transformer các khối khi việc xử lý
được chuẩn hóa các đầu vào (This includes measuring the performance of various activation functions like the rectified linear unit (ReLU), Sigmoid, and Tanh under controlled conditions, and evaluating the computational efficiency of distinct neural network components such as LSTM cells or transformer blocks when processing standardized inputs).
DeepBench (Baidu Nghiên cứu 2016), được phát triển bởi Baidu, là một của những cái đầu tiên để chứng minh
giá trị của toàn diện vi-việc đo điểm chuẩn (DeepBench (Baidu Research 2016), developed by Baidu, was one of the first to demonstrate the value of comprehensive micro-benchmarking). Nó đánh giá những cốt lõi các hoạt động này qua khác nhau
phần cứng các nền tảng, việc cung cấp chi tiết hiệu suất dữ liệu thứ mà giúp các nhà phát triển tối ưu hóa của họ sâu
học tập các sự triển khai (It evaluates these core operations across different hardware platforms, providing detailed performance data that helps developers optimize their deep learning implementations). Bằng cách việc cô lập và việc đo lường cá nhân các hoạt động, DeepBench kích hoạt
chính xác sự so sánh của phần cứng các nền tảng và sự nhận diện của tiềm năng hiệu suất các nút thắt cổ chai (By isolating and measuring individual operations, DeepBench enables precise comparison of hardware platforms and identification of potential performance bottlenecks).
Những có tính hạt các sự đo lường này kích hoạt chính xác sự tối ưu hóa, nhưng chúng không thể tiết lộ cách nào các thành-
phần tương tác khi được lắp ráp thành hoàn chỉnh các mô hình (These granular measurements enable precise optimization, but they cannot reveal how components interact when assembled into complete models). Vĩ-các điểm chuẩn giải quyết này khoảng cách (Macro-benchmarks address this gap).
12.4.2 Vĩ các điểm chuẩn (Macro benchmarks)
Vi-các điểm chuẩn xác nhận rằng cá nhân tích chập các hạt nhân chạy nhanh (Micro-benchmarks confirm that individual convolution kernels run fast). Vĩ-các điểm chuẩn tiết lộ
liệu hoàn chỉnh mô hình làm việc dưới thực tế các điều kiện (Macro-benchmarks reveal whether the complete model works under realistic conditions). Này sự chuyển dịch từ cấp độ-thành phần
tới cấp độ-mô hình sự đánh giá tiết lộ cách nào thuộc về kiến trúc các sự lựa chọn và thành phần các sự tương tác ảnh hưởng
tổng thể mô hình hành vi (This shift from component-level to model-level assessment reveals how architectural choices and component interactions affect overall model behavior). Cho ví dụ, trong khi vi-các điểm chuẩn có thể cho thấy tối ưu hiệu suất cho
cá nhân tích chập các lớp, vĩ-các điểm chuẩn tiết lộ cách nào những các lớp này làm việc cùng nhau bên trong một
hoàn chỉnh tích chập thần kinh mạng (For instance, while micro-benchmarks might show optimal performance for individual convolutional layers, macro-benchmarks reveal how these layers work together within a complete convolutional neural network).
Vĩ-các điểm chuẩn tồn tại để phục vụ một quyết định: việc chọn một mô hình hay kiến trúc dưới được chuẩn-
hóa các điều kiện (Macro-benchmarks exist to serve one decision: choosing a model or architecture under standardized conditions). Đó quyết định cần hiệu suất các chiều thứ mà nổi lên chỉ tại mô hình
cấp độ: sự dự đoán độ chính xác, thứ mà cho thấy cách nào tốt mô hình khái quát hóa tới mới dữ liệu; bộ nhớ
sự tiêu thụ các mẫu qua khác nhau lô các kích thước và chuỗi các độ dài; thông lượng dưới việc biến đổi
tính toán các tải; và độ trễ qua khác nhau phần cứng các cấu hình (That decision needs the performance dimensions that emerge only at the model level: prediction accuracy, which shows how well the model generalizes to new data; memory consumption patterns across different batch sizes and sequence lengths; throughput under varying computational loads; and latency across different hardware configurations). Những các chiều này
tương tác trong các cách một đơn-lớp vi-điểm chuẩn không thể phơi bày (These dimensions interact in ways a single-layer micro-benchmark cannot expose). Một mô hình thứ mà chiến thắng trên độ chính xác có thể
thua một khi của nó bộ nhớ dấu chân tại mục tiêu chuỗi độ dài ép buộc một nhỏ hơn lô, việc sụp đổ
thông lượng thứ mà đã làm cho nó hấp dẫn, một sự ghép nối vô hình chỉ khi hoàn chỉnh mô hình được đo lường như một
đơn vị (A model that wins on accuracy may lose once its memory footprint at the target sequence length forces a smaller batch, collapsing the throughput that made it attractive, a coupling visible only when the complete model is measured as a unit).
Sự đánh giá của hoàn chỉnh các mô hình xảy ra dưới được chuẩn hóa các điều kiện việc sử dụng được thiết lập
các tập dữ liệu và các tác vụ (The assessment of complete models occurs under standardized conditions using established datasets and tasks). Cho ví dụ, máy tính thị giác các mô hình có thể được đánh giá trên ImageNet (Deng
et al. 2024), việc đo lường cả hai tính toán tính hiệu quả và sự dự đoán độ chính xác (For example, computer vision models might be evaluated on ImageNet (Deng et al. 2024), measuring both computational efficiency and prediction accuracy). Tự nhiên ngôn ngữ
việc xử lý các mô hình có thể được đánh giá trên sự dịch thuật các tác vụ, việc kiểm tra cách nào chúng cân bằng chất lượng và
tốc độ qua khác nhau ngôn ngữ các cặp (Natural language processing models might be assessed on translation tasks, examining how they balance quality and speed across different language pairs).

12. Việc đo điểm chuẩn (Benchmarking)
657
Một vài tiêu chuẩn-ngành công nghiệp các điểm chuẩn làm cho cấp độ-mô hình sự so sánh có thể tái tạo qua các nền-
tảng (Several industry-standard benchmarks make model-level comparison reproducible across platforms). MLPerf gia đình (Suy luận, Di động, Máy khách (Client), và Nhỏ bé (Tiny)) cung cấp toàn diện kiểm tra
các bộ phần mềm được điều chỉnh (adapted) cho tính toán các môi trường từ dữ liệu trung tâm tới vi điều khiển, được chi tiết trong
phần 12.8.4 (The MLPerf family (Inference, Mobile, Client, and Tiny) provides comprehensive testing suites adapted for computational environments from data center to microcontroller, detailed in section 12.8.4). Cho nhúng các hệ thống, EEMBC’s MLMark nhấn mạnh cả hai hiệu suất và điện năng
tính hiệu quả, trong khi AI-Điểm chuẩn (Ignatov and Timofte 2024) bộ phần mềm chuyên môn hóa trong di động các nền tảng (For embedded systems, EEMBC’s MLMark emphasizes both performance and power efficiency, while the AI-Benchmark (Ignatov and Timofte 2024) suite specializes in mobile platforms).
12.4.3 Đầu-tới-đầu các điểm chuẩn (End-to-end benchmarks)
Đầu-tới-đầu các điểm chuẩn cung cấp bao gồm nhất (inclusive) sự đánh giá bằng cách việc bao quanh toàn bộ đường ống
của một AI hệ thống, không chỉ mô hình (End-to-end benchmarks provide the most inclusive evaluation by encompassing the entire pipeline of an AI system, not just the model). Điều này bao gồm trích xuất, biến đổi, tải (ETL) dữ liệu việc xử lý,
mô hình suy luận, sự hậu xử lý của các kết quả, và then chốt cơ sở hạ tầng các thành phần giống như lưu trữ và
mạng các hệ thống (This includes extract, transform, load (ETL) data processing, model inference, postprocessing of results, and critical infrastructure components like storage and network systems).
Dữ liệu việc xử lý (việc trích xuất từ nguồn các hệ thống, việc biến đổi thông qua việc làm sạch và đặc trưng
kỹ thuật, và việc tải thành sẵn sàng-mô hình các định dạng) hình thành nền tảng của đường ống (Data processing (extracting from source systems, transforming through cleaning and feature engineering, and loading into model-ready formats) forms the foundation of the pipeline). Những
sự tiền xử lý các bước này một cách trực tiếp ảnh hưởng tổng thể hiệu suất, và đầu-tới-đầu các điểm chuẩn phải đánh giá
được chuẩn hóa các tập dữ liệu thông qua hoàn chỉnh các đường ống để đảm bảo dữ liệu sự chuẩn bị không trở thành một
nút thắt cổ chai (These preprocessing steps directly affect overall performance, and end-to-end benchmarks must assess standardized datasets through complete pipelines to ensure data preparation does not become a bottleneck). Sự hậu xử lý một cách tương tự ảnh hưởng thực-thế giới hiệu suất: một máy tính thị giác hệ thống phải
hậu xử lý sự phát hiện các ranh giới, áp dụng sự tự tin các ngưỡng, và định dạng các kết quả cho xuôi dòng
các ứng dụng trước khi người dùng thấy một phản hồi (Postprocessing similarly affects real-world performance: a computer vision system must postprocess detection boundaries, apply confidence thresholds, and format results for downstream applications before the user sees a response).
Cơ sở hạ tầng các thành phần nặng nề ảnh hưởng tổng thể hiệu suất vượt ra ngoài AI khối lượng công việc chính nó (Infrastructure components heavily influence overall performance beyond the AI workload itself).
Lưu trữ các giải pháp có thể thống trị dữ liệu sự truy xuất (retrieval) các thời gian với lớn AI các tập dữ liệu, và mạng các sự tương tác
trong được phân phối các hệ thống có thể trở thành hiệu suất các nút thắt cổ chai (Storage solutions can dominate data retrieval times with large AI datasets, and network interactions in distributed systems can become performance bottlenecks). Đầu-tới-đầu các điểm chuẩn phải đánh giá
những các thành phần này dưới được quy định thuộc về môi trường các điều kiện để đảm bảo có thể tái tạo các sự đo lường
của toàn bộ hệ thống (End-to-end benchmarks must evaluate these components under specified environmental conditions to ensure reproducible measurements of the entire system).
Công cộng đầu-tới-đầu các điểm chuẩn hiếm khi tính toán cho dữ liệu lưu trữ, mạng, và tính toán hiệu suất
trong một sự đo lường (Public end-to-end benchmarks rarely account for data storage, network, and compute performance in one measurement). Trong khi MLPerf Huấn luyện và Suy luận tiếp cận đầu-tới-đầu sự đánh giá, chúng
chủ yếu tập trung trên mô hình hiệu suất thay vì thực-thế giới sự triển khai các kịch bản (While MLPerf Training and Inference approach end-to-end evaluation, they primarily focus on model performance rather than real-world deployment scenarios). Mặc dù vậy,
chúng cung cấp có giá trị đường cơ sở các số liệu cho việc đánh giá AI hệ thống các khả năng (Nonetheless, they provide valuable baseline metrics for assessing AI system capabilities).
Được cho vốn có tính cụ thể của đầu-tới-đầu việc đo điểm chuẩn, các tổ chức một cách điển hình thực hiện
những các sự đánh giá này một cách nội bộ bằng cách việc đo lường (instrumenting) sản xuất các sự triển khai (Given the inherent specificity of end-to-end benchmarking, organizations typically perform these evaluations internally by instrumenting production deployments). Sự nhạy cảm của những
các sự đo lường này có nghĩa là chúng hiếm khi xuất hiện một cách công khai, nhưng của chúng sự vắng mặt từ tài liệu (literature) không
làm giảm (diminish) của chúng tầm quan trọng (The sensitivity of these measurements means they rarely appear publicly, but their absence from the literature does not diminish their importance).
12.4.4 Tính hạt các sự đánh đổi và sự lựa chọn các tiêu chí (Granularity trade-offs and selection criteria)
Bảng 12.4 tiết lộ cách nào khác nhau các thách thức nổi lên tại khác nhau các giai đoạn của một AI hệ thống’s vòng đời (Table 12.4 reveals how different challenges emerge at different stages of an AI system’s lifecycle). Mỗi
việc đo điểm chuẩn cách tiếp cận cung cấp duy nhất các sự thấu hiểu: vi-các điểm chuẩn giúp các kỹ sư tối ưu hóa cụ-
thể các thành phần giống như GPU hạt nhân các sự triển khai hay dữ liệu việc tải các hoạt động, vĩ-các điểm chuẩn
hướng dẫn mô hình kiến trúc các quyết định và thuật toán sự lựa chọn, trong khi đầu-tới-đầu các điểm chuẩn tiết lộ
cấp độ-hệ thống các nút thắt cổ chai trong sản xuất các môi trường (Each benchmarking approach provides unique insights: micro-benchmarks help engineers optimize specific components like GPU kernel implementations or data loading operations, macro-benchmarks guide model architecture decisions and algorithm selection, while end-to-end benchmarks reveal system-level bottlenecks in production environments).
Bảng 12.4: Việc đo điểm chuẩn Tính hạt Các cấp độ (Benchmarking Granularity Levels): Khác nhau điểm chuẩn các phạm vi nhắm mục tiêu khác biệt các giai đoạn của ML hệ thống sự phát triển (Different benchmark scopes target distinct stages of ML system development).
Vi-các điểm chuẩn cô lập cá nhân các hoạt động cho thấp-cấp độ sự tối ưu hóa, vĩ-các điểm chuẩn đánh giá hoàn chỉnh các mô hình để
hướng dẫn thuộc về kiến trúc các sự lựa chọn, và đầu-tới-đầu các điểm chuẩn đánh giá đầy đủ hệ thống hiệu suất trong sản xuất các môi trường (Micro-benchmarks isolate individual operations for low-level optimization, macro-benchmarks evaluate complete models to guide architectural choices, and end-to-end benchmarks assess full system performance in production environments).
Thành phần (Component)
Vi Các điểm chuẩn (Micro Benchmarks)
Vĩ Các điểm chuẩn (Macro Benchmarks)
Đầu-tới-Đầu Các điểm chuẩn (End-to-End Benchmarks)
Trọng tâm (Focus)
Cá nhân các hoạt động (Individual operations)
Hoàn chỉnh các mô hình (Complete models)
Đầy đủ hệ thống đường ống (Full system pipeline)
Phạm vi (Scope)
Tensor ops, các lớp, các sự kích hoạt (Tensor ops, layers, activations)
Mô hình kiến trúc, huấn luyện,
suy luận (Model architecture, training, inference)
ETL, mô hình, cơ sở hạ tầng (ETL, model, infrastructure)
Ví dụ (Example)
Tích chập (Conv) lớp hiệu suất trên
cuDNN (Conv layer performance on cuDNN)
ResNet-50 trên ImageNet (ResNet-50 on ImageNet)
Sản xuất sự khuyến nghị
hệ thống (Production recommendation system)
Các lợi thế (Advantages)
Chính xác nút thắt cổ chai sự nhận diện,
Thành phần sự tối ưu hóa (Precise bottleneck identification, Component optimization)
Mô hình kiến trúc sự so sánh,
Được chuẩn hóa sự đánh giá (Model architecture comparison, Standardized evaluation)
Thực tế hiệu suất sự đánh giá,
Rộng-hệ thống các sự thấu hiểu (Realistic performance assessment, System-wide insights)
Các thách thức (Challenges)
Có thể bỏ lỡ sự tương tác các hiệu ứng (May miss interaction effects)
Bị giới hạn cơ sở hạ tầng các sự thấu hiểu (Limited infrastructure insights)
Phức tạp để chuẩn hóa, Thường
độc quyền (Complex to standardize, Often proprietary)
Điển hình Sử dụng (Typical Use)
Phần cứng sự lựa chọn, Hoạt động
sự tối ưu hóa (Hardware selection, Operation optimization)
Mô hình sự lựa chọn, Nghiên cứu
sự so sánh (Model selection, Research comparison)
Sản xuất hệ thống sự đánh giá (Production system evaluation)

658
12.5 Điểm chuẩn Các thành phần (Benchmark Components)
Việc chọn một đơn tính hạt cấp độ là hiếm khi đủ bởi vì một cốt lõi căng thẳng tồn tại giữa mang tính chẩn đoán
độ chính xác và thực-thế giới tính trung thực (fidelity) (Picking a single granularity level is rarely sufficient because a core tension exists between diagnostic precision and real-world fidelity). Hình 12.3 ánh xạ này sự đánh đổi, việc đặt vi-các điểm chuẩn tại
cao-sự cô lập cuối (chính xác nhưng hẹp) và đầu-tới-đầu các điểm chuẩn tại cao-tính đại diện
cuối (thực tế nhưng khó hơn để chẩn đoán) (Figure 12.3 maps this trade-off, placing micro-benchmarks at the high-isolation end (precise but narrow) and end-to-end benchmarks at the high-representativeness end (realistic but harder to diagnose)). Không đơn điểm nào trên này quang phổ cung cấp cả hai: vi-
các điểm chuẩn chỉ ra chính xác cái nào hạt nhân là chậm nhưng bỏ lỡ cấp độ-hệ thống các nút thắt cổ chai, trong khi đầu-tới-
đầu các điểm chuẩn nắm bắt sản xuất hành vi nhưng che khuất gốc các nguyên nhân (No single point on this spectrum provides both: micro-benchmarks pinpoint exactly which kernel is slow but miss system-level bottlenecks, while end-to-end benchmarks capture production behavior but obscure root causes). Thực tế bài học (takeaway) là
rằng hiệu quả ML hệ thống sự đánh giá yêu cầu việc kết hợp các sự thấu hiểu từ tất cả ba các cấp độ (The practical takeaway is that effective ML system evaluation requires combining insights from all three levels).
Sự cô lập/Mang tính chẩn đoán Điện năng (Isolation/Diagnostic Power)
Thực-Thế giới Tính đại diện (Real-World Representativeness)
Vi-các điểm chuẩn (Micro-benchmarks)
Vĩ-các điểm chuẩn (Macro-benchmarks)
Đầu-tới-Đầu các điểm chuẩn (End-to-End benchmarks)
Cao (High)
Thấp (Low)
Thấp (Low)
Cao (High)
Hình 12.3: Sự cô lập so với Tính đại diện (Isolation vs. Representativeness): Cốt lõi sự đánh đổi trong việc đo điểm chuẩn tính hạt (The core trade-off in benchmarking granularity). Vi-các điểm chuẩn cung cấp
cao mang tính chẩn đoán độ chính xác nhưng bị giới hạn thực-thế giới sự liên quan, trong khi đầu-tới-đầu các điểm chuẩn nắm bắt thực tế hệ thống hành vi nhưng
cung cấp ít chính xác cấp độ-thành phần các sự thấu hiểu (Micro-benchmarks provide high diagnostic precision but limited real-world relevance, while end-to-end benchmarks capture realistic system behavior but offer less precise component-level insights). Hiệu quả ML hệ thống sự đánh giá yêu cầu mang tính chiến lược sự kết hợp của tất cả ba các cấp độ (Effective ML system evaluation requires strategic combination of all three levels).
Thành phần sự tương tác thường tạo ra không được mong đợi các hành vi thứ mà đơn-cấp độ các điểm chuẩn bỏ lỡ (Component interaction often produces unexpected behaviors that single-level benchmarks miss).
Trong khi vi-các điểm chuẩn có thể cho thấy xuất sắc hiệu suất cho cá nhân các hoạt động và vĩ-
các điểm chuẩn có thể chứng minh mạnh mẽ mô hình độ chính xác, đầu-tới-đầu sự đánh giá có thể tiết lộ rằng
dữ liệu sự tiền xử lý tạo ra không được mong đợi các nút thắt cổ chai trong suốt cao-lưu lượng các khoảng thời gian (While micro-benchmarks might show excellent performance for individual operations and macro-benchmarks might demonstrate strong model accuracy, end-to-end evaluation can reveal that data preprocessing creates unexpected bottlenecks during high-traffic periods). Những cấp độ-hệ thống
các sự thấu hiểu này duy trì bị ẩn giấu khi các thành phần trải qua được cô lập việc kiểm tra (These system-level insights remain hidden when components undergo isolated testing).
Việc chọn một tính hạt cấp độ, tuy nhiên, là chỉ một nửa thiết kế vấn đề (Choosing a granularity level, however, is only half the design problem). Nửa kia là việc quy định
cụ thể các thành phần mọi điểm chuẩn yêu cầu: tác vụ, dữ liệu, mô hình, và các số liệu (The other half is specifying the concrete ingredients every benchmark requires: the task, data, model, and metrics). Mà không có
những các thành phần đó, thậm chí đúng tính hạt cấp độ tạo ra vô nghĩa các con số (Without those ingredients, even the right granularity level produces meaningless numbers). Các thành phần
của một điểm chuẩn xác định liệu các kết quả dịch thuật thành có thể hành động kỹ thuật sự thấu hiểu hay đơn thuần
tạo ra ấn tượng-trông có vẻ các con số thứ mà sụp đổ dưới sự giám sát (scrutiny) (The components of a benchmark determine whether results translate into actionable engineering insight or merely generate impressive-looking numbers that collapse under scrutiny).
12.5 Điểm chuẩn Các thành phần (Benchmark Components)
Việc chọn giữa vi, vĩ, và đầu-tới-đầu tính hạt xác định cái gì một điểm chuẩn có thể
chẩn đoán, nhưng mọi điểm chuẩn tại mọi tính hạt phải vẫn quy định tác vụ, dữ liệu, mô hình, các số-
liệu, khung chằng (harness), hệ thống ngữ cảnh, và chạy các quy tắc thứ mà làm cho của nó kết quả có thể diễn giải được (Choosing between micro, macro, and end-to-end granularity determines what a benchmark can diagnose, but every benchmark at every granularity must still specify the task, data, model, metrics, harness, system context, and run rules that make its result interpretable). Vi-các điểm chuẩn
yêu cầu tổng hợp các đầu vào thứ mà cô lập cụ thể tính toán các mẫu; vĩ-các điểm chuẩn đòi hỏi
đại diện các tập dữ liệu giống như ImageNet; đầu-tới-đầu các điểm chuẩn phải kết hợp thực-thế giới dữ liệu
với tất cả của nó tiếng ồn và mang tính phân phối sự chuyển dịch (Micro-benchmarks require synthetic inputs that isolate specific computational patterns; macro-benchmarks demand representative datasets like ImageNet; end-to-end benchmarks must incorporate real-world data with all its noise and distributional shift). Bất chấp này sự biến thiên, tất cả các điểm chuẩn chia sẻ một chung
sự triển khai vấn đề: mỗi thành phần phải ràng buộc tiếp theo cái do đó cuối cùng con số có một
có thể bảo vệ được ý nghĩa (Despite this variation, all benchmarks share a common implementation problem: each component must constrain the next one so the final number has a defensible meaning).
Thiết yếu các thành phần kết nối liên thông để hình thành một hoàn chỉnh sự đánh giá đường ống (The essential components interconnect to form a complete evaluation pipeline). Quy trình làm việc trong
hình 12.4 theo dấu chín các giai đoạn của một công nghiệp âm thanh sự bất thường sự phát hiện điểm chuẩn, từ vấn đề
sự định nghĩa thông qua sự lượng tử hóa tới ARM nhúng sự triển khai (The workflow in figure 12.4 traces nine stages of an industrial audio anomaly detection benchmark, from problem definition through quantization to ARM embedded deployment). Mang tính chuỗi (serial) sự phụ thuộc là
then chốt sự quan sát: tác vụ sự định nghĩa ràng buộc cái nào các tập dữ liệu là hợp lệ, tập dữ liệu các thuộc tính
xác định cái nào mô hình các kiến trúc là khả thi, và mục tiêu phần cứng sai khiến sự lượng tử hóa và
sự biên dịch các sự lựa chọn (The serial dependency is the critical observation: the task definition constrains which datasets are valid, the dataset properties determine which model architectures are feasible, and the target hardware dictates quantization and compilation choices). Sự bất thường sự phát hiện phục vụ như một hiệu quả sự minh họa chính xác bởi vì nó trải dài
đầy đủ ngăn xếp, việc ghép nối ML suy luận độ chính xác với nhúng các hệ thống các sự ràng buộc chẳng hạn như bộ nhớ
dấu chân, điện năng ngân sách, và thời gian-thực độ trễ (Anomaly detection serves as an effective illustration precisely because it spans the full stack, coupling ML inference accuracy with embedded systems constraints such as memory footprint, power budget, and real-time latency). Một điểm chuẩn thứ mà đã đo lường chỉ phân loại
độ chính xác hoặc chỉ suy luận tốc độ sẽ bỏ lỡ các sự tương tác giữa những các giai đoạn này, nơi một quyết định
tại bất kỳ điểm nào lan truyền về phía trước và thu hẹp mọi tiếp theo sự lựa chọn (A benchmark that measured only classification accuracy or only inference speed would miss the interactions between these stages, where a decision at any point propagates forward and narrows every subsequent choice).
...
Hình 12.4: Điểm chuẩn Quy trình làm việc Các thành phần (Benchmark Workflow Components): Một chín-giai đoạn quy trình làm việc cho việc thiết kế một máy học điểm chuẩn, việc sử dụng
một âm thanh sự bất thường sự phát hiện tác vụ như một ví dụ (A nine-stage workflow for designing a machine learning benchmark, using an audio anomaly detection task as an example). Quá trình chảy từ việc định nghĩa tác vụ, tập dữ liệu, mô hình, và các số liệu tới
việc quy định sự đo lường giao thức và sự phân tích các phương pháp (The process flows from defining the task, dataset, model, and metrics to specifying measurement protocol and analysis methods).
12
SQuAD (Stanford Hỏi
Trả lời Tập dữ liệu (Stanford Question Answering Dataset)): Được giới-
thiệu vào 2016 với nhiều hơn
100,000 câu hỏi-câu trả lời
các cặp từ Wikipedia (Ra-
jpurkar et al. 2016) (SQuAD (Stanford Question Answering Dataset): Introduced in 2016 with more than 100,000 question-answer pairs from Wikipedia (Rajpurkar et al. 2016)). AI các hệ-
thống đã vượt qua SQuAD 1.1
con người đường cơ sở của 91.2 phần-
trăm F1 vào 2018, nhưng này “siêu-
nhân” kết quả minh họa
một việc đo điểm chuẩn thất bại chế độ:
tác vụ’s mang tính trích xuất định dạng
(các câu trả lời là văn bản các nhịp (spans) bên trong
đoạn văn (passage)) làm cho nó dễ dàng
hơn mở-kết thúc câu hỏi trả-
lời, việc thổi phồng được nhận thức
khả năng tương đối tới sản-
xuất NLP các hệ thống (AI systems exceeded the SQuAD 1.1 human baseline of 91.2 percent F1 by 2018, but this “superhuman” result illustrates a benchmarking failure mode: the task’s extractive format (answers are text spans within the passage) makes it easier than open-ended question answering, inflating perceived capability relative to production NLP systems).
13
GLUE:
GLUE’s
sự bão hòa hình cung (arc) là một điểm chuẩn-
sự lỗi thời
trường hợp
nghiên cứu (GLUE: GLUE’s saturation arc is a benchmark-obsolescence case study).
Được giới thiệu vào 2018 như một rộng
ngôn ngữ-sự hiểu
điểm chuẩn (A. Wang et al.
2018),
GLUE đã nhanh chóng
bị áp lực bởi các hệ thống chẳng
hạn như BERT (Devlin et al. 2019)
và sau đó các mô hình (Introduced in 2018 as a broad language-understanding benchmark (A. Wang et al. 2018), GLUE was quickly pressured by systems such as BERT (Devlin et al. 2019) and later models).
Đây là
Goodhart’s Định luật trong hành động:
một khi GLUE đã trở thành một mục tiêu,
bảng xếp hạng
sự tối ưu hóa
đã làm giảm của nó mang tính phân biệt
sức mạnh (This is Goodhart’s Law in action: once GLUE became a target, leaderboard optimization reduced its discriminating power). Mẫu đã thúc đẩy
khó hơn theo-sau các sự đánh giá
chẳng
hạn
như
SuperGLUE
và
BIG-bench (The pattern motivated harder follow-on evaluations such as SuperGLUE and BIG-bench).
Hiệu quả điểm chuẩn thiết kế phải tính toán cho sự tối ưu hóa các kỹ thuật được thiết lập trong trước đó
các chương (Effective benchmark design must account for the optimization techniques established in preceding chapters). Sự lượng tử hóa và việc cắt tỉa ảnh hưởng mô hình độ chính xác-tính hiệu quả các sự đánh đổi, việc yêu cầu các điểm-
chuẩn thứ mà đo lường cả hai sự tăng tốc và độ chính xác sự bảo tồn một cách đồng thời (Quantization and pruning affect model accuracy-efficiency trade-offs, requiring benchmarks that measure both speedup and accuracy preservation simultaneously). Phần cứng sự gia tốc
các kỹ thuật ảnh hưởng số học cường độ và bộ nhớ băng thông sự sử dụng, việc đòi hỏi roofline
mô hình sự phân tích để diễn giải các kết quả một cách chính xác (Hardware acceleration techniques influence arithmetic intensity and memory bandwidth utilization, necessitating roofline model analysis to interpret results correctly). Việc hiểu những sự tối ưu hóa các nền tảng này kích hoạt
điểm chuẩn sự lựa chọn thứ mà xác nhận được tuyên bố các sự cải thiện thay vì việc đo lường nhân tạo các kịch bản (Understanding these optimization foundations enables benchmark selection that validates claimed improvements rather than measuring artificial scenarios).
12.5.1 Vấn đề sự định nghĩa (Problem definition)
Mọi điểm chuẩn bắt đầu bằng cách việc quy định chính xác cái gì hệ thống phải làm (Every benchmark begins by specifying exactly what the system must do). Sự bất thường sự phát hiện
hệ thống trong hình 12.4 xử lý âm thanh các tín hiệu để nhận diện các sự sai lệch từ bình thường hoạt động các mẫu,
một công nghiệp sự giám sát ứng dụng thứ mà là ví dụ điển hình cách nào chính thức tác vụ các thông số kỹ thuật dịch thuật thành
thực tế các sự triển khai (The anomaly detection system in figure 12.4 processes audio signals to identify deviations from normal operation patterns, an industrial monitoring application that exemplifies how formal task specifications translate into practical implementations). Trong khi cụ thể các tác vụ biến đổi một cách rộng rãi theo miền (tự nhiên ngôn ngữ việc xử lý
các tác vụ bao gồm máy dịch thuật, câu hỏi trả lời (Hirschberg và Manning 2015), và văn bản
sự phân loại; máy tính thị giác sử dụng đối tượng sự phát hiện và hình ảnh sự phân đoạn (Everingham et al.
2009; Lin et al. 2014)), mọi điểm chuẩn tác vụ thông số kỹ thuật phải định nghĩa ba thiết yếu các phần tử: một
đầu vào thông số kỹ thuật (cái gì dữ liệu hệ thống xử lý), một đầu ra thông số kỹ thuật (cái gì phản hồi hệ thống
phải tạo ra), và một hiệu suất thông số kỹ thuật (định lượng các yêu cầu cho độ chính xác, tốc độ, và
tài nguyên sự sử dụng) (While specific tasks vary widely by domain (natural language processing tasks include machine translation, question answering (Hirschberg and Manning 2015), and text classification; computer vision employs object detection and image segmentation (Everingham et al. 2009; Lin et al. 2014)), every benchmark task specification must define three essential elements: an input specification (what data the system processes), an output specification (what response the system must produce), and a performance specification (quantitative requirements for accuracy, speed, and resource utilization)).
Tác vụ thiết kế một cách trực tiếp tác động điểm chuẩn’s khả năng để đánh giá AI các hệ thống (Task design directly impacts the benchmark’s ability to evaluate AI systems). Âm thanh sự bất thường
sự phát hiện ví dụ minh họa điều này thông qua của nó cụ thể các yêu cầu: việc xử lý liên tục tín hiệu
dữ liệu, việc thích ứng tới việc biến đổi tiếng ồn các điều kiện, và việc hoạt động bên trong nghiêm ngặt thời gian các sự ràng buộc (The audio anomaly detection example illustrates this through its specific requirements: processing continuous signal data, adapting to varying noise conditions, and operating within strict time constraints). Những
thực tế các sự ràng buộc này tạo ra một bộ khung cho sự đánh giá thứ mà phản ánh thực-thế giới hoạt động các đòi hỏi (These practical constraints create a framework for assessment that reflects real-world operational demands).
Mỗi tiếp theo giai đoạn của điểm chuẩn sự triển khai, từ tập dữ liệu sự lựa chọn thông qua sự triển khai,
xây dựng một cách trực tiếp dựa trên những ban đầu các thông số kỹ thuật này (Each subsequent phase of benchmark implementation, from dataset selection through deployment, builds directly upon these initial specifications).
12.5.2 Được chuẩn hóa các tập dữ liệu (Standardized datasets)
Một tác vụ sự định nghĩa là chỉ tốt như dữ liệu được sử dụng để đánh giá nó (A task definition is only as good as the data used to evaluate it). Được chuẩn hóa các tập dữ liệu đảm bảo
rằng tất cả các mô hình trải qua việc kiểm tra dưới giống hệt các điều kiện, việc kích hoạt trực tiếp các sự so sánh qua
khác nhau các cách tiếp cận—mà không có chúng, mọi nhóm sẽ đánh giá trên riêng tư dữ liệu, việc làm cho chéo-phòng thí nghiệm
sự so sánh không thể (Standardized datasets ensure that all models undergo testing under identical conditions, enabling direct comparisons across different approaches—without them, every team would evaluate on private data, making cross-lab comparison impossible). Trong máy tính thị giác, ImageNet (Deng et al. 2024, 2009), COCO (Lin et al.
2014), và CIFAR-10 (Krizhevsky 2009) phục vụ như tham chiếu các tiêu chuẩn; trong tự nhiên ngôn ngữ việc xử lý,
SQuAD12 (Rajpurkar et al. 2016), GLUE13 (A. Wang et al. 2018), và WikiText (Merity 2016; Merity
et al. 2016) hoàn thành tương tự các vai trò, mỗi cái bao quanh một phạm vi của các sự phức tạp và biên các trường hợp (In computer vision, ImageNet (Deng et al. 2024, 2009), COCO (Lin et al. 2014), and CIFAR-10 (Krizhevsky 2009) serve as reference standards; in natural language processing, SQuAD12 (Rajpurkar et al. 2016), GLUE13 (A. Wang et al. 2018), and WikiText (Merity 2016; Merity et al. 2016) fulfill similar roles, each encompassing a range of complexities and edge cases).
Tập dữ liệu sự lựa chọn là đầu tiên nơi một điểm chuẩn có thể mất liên lạc với sự triển khai thực tế (Dataset selection is the first place a benchmark can lose contact with deployment reality). Trong
âm thanh sự bất thường sự phát hiện ví dụ (hình 12.4), tập dữ liệu phải bao gồm đại diện dạng sóng
các mẫu của bình thường hoạt động song song toàn diện các ví dụ của bất thường các điều kiện; cụ thể-miền
các bộ sưu tập giống như ToyADMOS14 (Koizumi et al. 2019) cho được kiểm soát sự bất thường-sự phát hiện nghiên cứu (In the audio anomaly detection example (figure 12.4), the dataset must include representative waveform samples of normal operation alongside comprehensive examples of anomalous conditions; domain-specific collections like ToyADMOS14 (Koizumi et al. 2019) for controlled anomaly-detection research)

660
12.5 Điểm chuẩn Các thành phần (Benchmark Components)
14
ToyADMOS: Được phát-
triển bởi NTT Communica-
tions vào 2019 cho âm thanh
sự bất thường sự phát hiện, việc chứa
âm thanh các bản thu âm từ đồ chơi
ô tô, đồ chơi băng chuyền (conveyor), và có liên quan
thu nhỏ-máy móc đang hoạt động
các âm thanh (Koizumi et al. 2019).
“Toy” tiền tố là có chủ ý:
được kiểm soát môi trường
kích hoạt có thể tái tạo việc đo điểm-
chuẩn nhưng có thể tạo ra một miền
khoảng cách khi các mô hình được
di chuyển tới ồn ào hơn công nghiệp các môi-
trường với khác nhau các máy
móc, các cảm biến, sự rung động, và
nền âm thanh (ToyADMOS: Developed by NTT Communications in 2019 for acoustic anomaly detection, containing audio recordings from toy car, toy conveyor, and related miniature-machine operating sounds (Koizumi et al. 2019). The “toy” prefix is intentional: the controlled environment enables reproducible benchmarking but can create a domain gap when models are moved to noisier industrial environments with different machines, sensors, vibration, and background sound).
15
BERT (Hai chiều (Bidirectional) Mã-
hóa Các biểu diễn từ
Các transformers (Bidirectional Encoder Representations from Transformers)): BERT-Lớn (Large)
(340M các tham số) đã trở thành
mặc định
NLP
đường cơ sở
bởi vì của nó cố định-kích thước bộ mã hóa
tạo ra
mang tính xác định
độ trễ
mỗi
đầu vào,
không giống
tự hồi quy các mô hình của cái mà
chi phí mở rộng quy mô với đầu ra độ dài (BERT (Bidirectional Encoder Representations from Transformers): BERT-Large (340M parameters) became the default NLP baseline because its fixed-size encoder produces deterministic latency per input, unlike autoregressive models whose cost scales with output length).
Này tính có thể dự đoán được là chính xác
tại sao
MLPerf
Suy luận
đã thông qua BERT như của nó NLP tham-
chiếu khối lượng công việc: một đường cơ sở
phải cô lập phần cứng và
phần mềm
các sự khác biệt
từ
vốn có-mô hình
sự biến thiên,
và
BERT’s
không đổi-chi phí
chuyển tiếp lượt chạy (forward pass) đạt được sự
tách biệt đó (This predictability is precisely why MLPerf Inference adopted BERT as its NLP reference workload: a baseline must isolate hardware and software differences from model-inherent variability, and BERT’s constant-cost forward pass achieves that separation).
16
Số liệu (Metric): Trong toán-
học, một metric là một khoảng cách
hàm việc thỏa mãn nghiêm ngặt các tiên-
đề bao gồm tam giác
bất đẳng thức (Metric: In mathematics, a metric is a distance function satisfying strict axioms including the triangle inequality). ML mượn
thuật ngữ một cách lỏng lẻo cho định lượng
các sự đo lường chẳng hạn như BLEU và
perplexity, thứ mà là việc ghi-
điểm các quy tắc thay vì toán-
học các metrics (ML borrows the term loosely for quantitative measures such as BLEU and perplexity, which are scoring rules rather than mathematical metrics).
Bảng xếp-
hạng các thứ hạng có thể thay đổi
khi sự đánh giá giao-
thức, tập dữ liệu lát cắt (slice), hay số liệu
sự đánh trọng số thay đổi, việc làm cho
sự lựa chọn của số liệu một kỹ-
thuật quyết định thứ mà định hình
cái nào hệ thống chiến thắng, không chỉ
cách nào chúng ta đo lường nó (Leaderboard rankings can change when the evaluation protocol, dataset slice, or metric weighting changes, making the choice of metric an engineering decision that shapes which system wins, not just how we measure it).
và Google Lời nói Các lệnh (Speech Commands) cho chung âm thanh sự nhận dạng giải quyết những các yêu cầu này (and Google Speech Commands for general sound recognition address these requirements). Hiệu quả
điểm chuẩn các tập dữ liệu phải cân bằng hai cạnh tranh các đòi hỏi: một cách chính xác việc đại diện thực-thế giới
các thách thức trong khi việc duy trì đủ sự phức tạp để phân biệt mô hình hiệu suất (Effective benchmark datasets must balance two competing demands: accurately representing real-world challenges while maintaining sufficient complexity to differentiate model performance). Được đơn giản hóa
các tập dữ liệu giống như ToyADMOS là có giá trị cho mang tính phương pháp luận sự phát triển nhưng có thể không nắm bắt đầy đủ
sự phức tạp của sản xuất các môi trường (Simplified datasets like ToyADMOS are valuable for methodological development but may not capture the full complexity of production environments).
12.5.3 Mô hình sự lựa chọn (Model selection)
Với tác vụ và dữ liệu được quy định, điểm chuẩn phải định nghĩa cái gì các mô hình để đánh giá và cái gì
các đường cơ sở để so sánh chống lại (With task and data specified, the benchmark must define which models to evaluate and what baselines to compare against). Này sự lựa chọn là ít đơn giản hơn nó có vẻ: một điểm chuẩn’s
mô hình sự lựa chọn xác định liệu các kết quả phản ánh thuộc về kiến trúc sự đổi mới, sự triển khai chất lượng,
hay đơn giản cụ thể-bộ khung các sự tối ưu hóa (This choice is less straightforward than it appears: a benchmark’s model selection determines whether results reflect architectural innovation, implementation quality, or simply framework-specific optimizations). Sự lựa chọn quá trình xây dựng dựa trên thuộc về kiến trúc
các nền tảng được thiết lập trong Chương 6 và phải tính toán cho bộ khung các sự xem xét được thảo luận
trong Chương 7 (The selection process builds upon the architectural foundations established in Chapter 6 and must account for the framework considerations discussed in Chapter 7).
Đường cơ sở các mô hình phục vụ như tham chiếu các điểm trải dài từ cơ bản các sự triển khai (tuyến tính hồi quy,
logistic hồi quy) tới tiên tiến các kiến trúc với đã được chứng minh sự thành công trong có thể so sánh các miền (Baseline models serve as reference points spanning from basic implementations (linear regression, logistic regression) to advanced architectures with proven success in comparable domains). Trong NLP,
các mô hình giống như BERT15 đã nổi lên như tiêu chuẩn các đường cơ sở (In NLP, models like BERT15 have emerged as standard baselines). Một cách then chốt, sự lựa chọn của đường cơ sở phụ thuộc
trên sự triển khai bộ khung: một PyTorch sự triển khai có thể thể hiện khác nhau hiệu suất
các đặc điểm hơn của nó TensorFlow tương đương do cụ thể-bộ khung các sự tối ưu hóa và toán tử
các sự triển khai, việc có nghĩa là điểm chuẩn phải kiểm soát cho này biến số (Critically, the choice of baseline depends on the deployment framework: a PyTorch implementation may exhibit different performance characteristics than its TensorFlow equivalent due to framework-specific optimizations and operator implementations, meaning the benchmark must control for this variable).
Một khi kiến trúc được chọn, mô hình sự phát triển theo sau hai song song sự tối ưu hóa các con đường thứ mà
điểm chuẩn phải theo dấu (Once the architecture is selected, model development follows two parallel optimization paths that the benchmark must track). Huấn luyện sự tối ưu hóa tập trung trên việc đạt được mục tiêu độ chính xác bên trong tính-
toán các sự ràng buộc (Training optimization focuses on achieving target accuracy within computational constraints). Suy luận sự tối ưu hóa giải quyết sự chuyển tiếp tới sản xuất—đặc biệt
độ chính xác sự giảm từ FP32 tới INT8 hay thấp hơn, thứ mà đòi hỏi cẩn thận sự hiệu chuẩn để duy trì
độ chính xác trong khi việc giảm tài nguyên các yêu cầu (Inference optimization addresses the transition to production—particularly precision reduction from FP32 to INT8 or lower, which demands careful calibration to maintain accuracy while reducing resource requirements). Điểm chuẩn phải quy định các yêu cầu cho
cả hai con đường, bởi vì một mô hình thứ mà huấn luyện một cách hiệu quả nhưng triển khai kém (hoặc ngược lại) thất bại đầy đủ
sự đánh giá (The benchmark must specify requirements for both paths, because a model that trains efficiently but deploys poorly (or vice versa) fails the full evaluation). Này kép sự tối ưu hóa một cách tự nhiên đòi hỏi định lượng sự đánh giá các số liệu thứ mà trải dài tất cả
ba các chiều của của chúng ta việc đo điểm chuẩn bộ khung (This dual optimization naturally demands quantitative evaluation metrics that span all three dimensions of our benchmarking framework).
12.5.4 Sự đánh giá các số liệu (Evaluation metrics)
Sự đánh giá các số liệu16 dịch thuật thô mô hình hành vi thành các con số thứ mà có thể được so sánh, được xếp hạng, và
được sử dụng để làm kỹ thuật các quyết định (Evaluation metrics16 translate raw model behavior into numbers that can be compared, ranked, and used to make engineering decisions). Thách thức là việc chọn đúng các con số: một số liệu thứ mà
nắm bắt độ chính xác nhưng phớt lờ độ trễ có thể tuyên bố người chiến thắng là một mô hình quá chậm cho sản xuất;
một cái thứ mà thưởng thông lượng nhưng phớt lờ năng lượng có thể tối ưu hóa cho một sự triển khai ngân sách thứ mà làm
không tồn tại (The challenge is choosing the right numbers: a metric that captures accuracy but ignores latency may declare the winner to be a model too slow for production; one that rewards throughput but ignores energy may optimize for a deployment budget that does not exist).
Bảng 12.5 nên được đọc như một quyết định sự hỗ trợ: nó phân loại các số liệu bởi thất bại chế độ mỗi cái phơi bày
và sự triển khai ngữ cảnh nó phục vụ (Table 12.5 should be read as a decision aid: it categorizes metrics by the failure mode each exposes and the deployment context it serves).
Bảng 12.5: ML Việc đo điểm chuẩn Số liệu Tính phân loại (Metric Taxonomy): Các số liệu được tổ chức bởi sự đánh giá danh mục, đơn vị, và chính sử dụng trường hợp (Metrics organized by evaluation category, unit, and primary use case).
Độ chính xác các số liệu định lượng mô hình chất lượng, thông lượng và độ trễ các số liệu nắm bắt hệ thống tốc độ, và tính hiệu quả các số liệu kết hợp
nhiều các chiều (Accuracy metrics quantify model quality, throughput and latency metrics capture system speed, and efficiency metrics combine multiple dimensions). Việc chọn đúng số liệu cho sự triển khai ngữ cảnh là thường quan trọng hơn hơn việc tối ưu hóa bất kỳ đơn
số liệu nào tới của nó tối đa (Selecting the right metric for the deployment context is often more important than optimizing any single metric to its maximum).
Danh mục (Category)
Số liệu (Metric)
Đơn vị (Unit)
Chính Sử dụng Trường hợp (Primary Use Case)
Độ chính xác (Accuracy)
Top-1/Top-5 Độ chính xác (Accuracy)
Phần trăm (Percentage)
Sự phân loại (Classification)
mAP (trung bình (mean) Trung bình (Average) Độ chính xác (Precision))
0-1 điểm số (score)
Đối tượng sự phát hiện (Object detection)
BLEU/ROUGE
0-100 điểm số (score)
NLP sự tạo ra (generation)
Perplexity
Điểm số (thấp hơn = tốt hơn) (Score (lower = better))
Ngôn ngữ việc mô hình hóa (Language modeling)
Thông lượng (Throughput)
Các mẫu/giây (Samples/second)
Các mẫu/s (Samples/s)
Lô suy luận (Batch inference)
Token thông lượng (Token throughput)
các tokens/s
LLM suy luận (LLM inference)
Thời gian-tới-huấn luyện (Time-to-train)
Các giờ/các ngày (Hours/days)
Huấn luyện các điểm chuẩn (Training benchmarks)
Độ trễ (Latency)
p50 độ trễ (latency)
Các mili giây (Milliseconds)
Trung vị phản hồi thời gian (Median response time)
p99 độ trễ (latency)
Các mili giây (Milliseconds)
Đuôi (Tail) độ trễ (SLA) (Tail latency (SLA))
Đầu tiên-token độ trễ (First-token latency)
Các mili giây (Milliseconds)
LLM tính đáp ứng (responsiveness)
Tính hiệu quả (Efficiency)
Các mẫu/giây/watt (Samples/second/watt)
Các mẫu/s/W (Samples/s/W)
Năng lượng tính hiệu quả (Energy efficiency)
Độ chính xác/FLOP (Accuracy/FLOP)
phần trăm/PFLOP (percent/PFLOP)
Thuật toán tính hiệu quả (Algorithmic efficiency)
TCO mỗi suy luận (TCO per inference)
$/suy luận ($/inference)
Kinh tế tính hiệu quả (Economic efficiency)

12. Việc đo điểm chuẩn (Benchmarking)
661
17
BLEU (Song ngữ Sự đánh-
giá Dự bị (Bilingual Evaluation Understudy)):
Được giới-
thiệu bởi IBM vào 2002, BLEU
đo lường sự dịch thuật chất lượng
thông qua được sửa đổi n-gram độ chính-
xác với một sự ngắn gọn hình phạt
chống lại tham chiếu các sự dịch thuật
(Papineni et al. 2002) (BLEU (Bilingual Evaluation Understudy): Introduced by IBM in 2002, BLEU measures translation quality through modified n-gram precision with a brevity penalty against reference translations (Papineni et al. 2002)). BLEU là
một kinh điển ví dụ của Good-
hart’s Định luật trong ML: việc tối ưu hóa
cho n-gram các sự khớp (matches) có thể thưởng bề-mặt-cấp độ từ sự chồng-
chéo (overlap) thậm chí khi ý nghĩa, sự trôi-
chảy (fluency), hay sự triển khai tính hữu-
ích phân kỳ từ mục tiêu (BLEU is a canonical example of Goodhart’s Law in ML: optimizing for n-gram matches can reward surface-level word overlap even when meaning, fluency, or deployment usefulness diverges from the target).
18
Poisson Sự phân phối (Distribution):
Được đặt tên theo Siméon Denis
Poisson, người đã chính thức hóa nó vào
1837 trong khi việc mô hình hóa sai-
trái sự kết án các tỷ lệ trong Pháp
các tòa án (Poisson Distribution: Named after Siméon Denis Poisson, who formalized it in 1837 while modeling wrongful conviction rates in French courts). Sự phân phối mô hình hóa độc lập các sự kiện tại một
không đổi trung bình tỷ lệ (𝜆arr),
việc làm cho nó tiêu chuẩn giả-
định cho máy chủ yêu cầu
các sự đến (arrivals) (The distribution models independent events at a constant average rate (𝜆arr), making it the standard assumption for server request arrivals). Việc đo điểm chuẩn
hậu quả: thực ML phục-
vụ lưu lượng thường vi phạm
Poisson sự giả định do
bùng nổ (bursty) các mẫu (cho ví dụ,
lan truyền (viral) nội dung các sự tăng vọt (spikes)), do đó các điểm-
chuẩn việc sử dụng Poisson các sự đến
một cách có hệ thống đánh giá thấp
đuôi độ trễ trong sản xuất (The benchmarking consequence: real ML serving traffic often violates the Poisson assumption due to bursty patterns (for example, viral content spikes), so benchmarks using Poisson arrivals systematically underestimate tail latency in production).
Một vài sự phân biệt bên trong này tính phân loại xứng đáng sự nhấn mạnh (Several distinctions within this taxonomy deserve emphasis). Thông lượng đo lường tổng (aggregate)
công suất (lý tưởng cho lô việc xử lý), trong khi độ trễ đo lường cá nhân yêu cầu định thời (quan trọng
cho tương tác các ứng dụng) (Throughput measures aggregate capacity (ideal for batch processing), while latency measures individual request timing (critical for interactive applications)). Những các số liệu này thường xuyên xung đột: việc tối đa hóa thông lượng thông qua
việc tạo lô thường tăng mỗi-yêu cầu độ trễ (These metrics frequently conflict: maximizing throughput through batching often increases per-request latency). Trung bình độ trễ có thể che giấu có vấn đề đuôi hành vi—một
hệ thống với 10 ms trung bình độ trễ có thể có 500 ms p99 độ trễ, việc thất bại SLA các yêu cầu (Mean latency can hide problematic tail behavior—a system with 10 ms mean latency might have 500 ms p99 latency, failing SLA requirements). Trong
sản xuất, các phân vị (percentiles) (p50, p95, p99) là xa hơn nhiều thông tin hơn các giá trị trung bình (In production, percentiles (p50, p95, p99) are far more informative than means). Cuối cùng, hợp chất (compound)
các số liệu giống như các mẫu/giây/watt kết hợp nhiều các chiều thành một đơn con số, việc kích hoạt
nhanh các sự so sánh nhưng việc che khuất cá nhân các nút thắt cổ chai (Finally, compound metrics like samples/second/watt combine multiple dimensions into a single number, enabling quick comparisons but obscuring individual bottlenecks). Việc báo cáo cả hai nguyên tử (atomic) và hợp chất
các số liệu cung cấp một hoàn chỉnh bức tranh (Reporting both atomic and compound metrics provides a complete picture).
Số liệu sự lựa chọn phải căn chỉnh với tác vụ các mục tiêu và sự triển khai các sự ràng buộc, bởi vì giống nhau
thô mô hình hành vi có thể tạo ra khác nhau các điểm số qua các bộ khung (Metric choice must align with task objectives and deployment constraints, because the same raw model behavior can produce different scores across frameworks). Huấn luyện các phương pháp luận
từ Chương 8 chứng minh cách nào khác nhau các bộ khung xử lý mất mát sự tính toán và gradient
sự tích lũy khác nhau, việc ảnh hưởng được báo cáo các số liệu (The training methodologies from Chapter 8 demonstrate how different frameworks handle loss computation and gradient accumulation differently, affecting reported metrics). Thậm chí nhỏ sự triển khai các sự khác biệt, chẳng
hạn như đánh giá-chế độ lô-sự chuẩn hóa sự xử lý, có thể chuyển dịch được đo lường độ chính xác đủ để quan trọng
khi điểm chuẩn các deltas là nhỏ (Even small implementation differences, such as evaluation-mode batch-normalization handling, can shift measured accuracy enough to matter when benchmark deltas are small).
Cụ thể-tác vụ các số liệu định lượng một mô hình’s hiệu suất trên của nó dự định chức năng (Task-specific metrics quantify a model’s performance on its intended function). Cho ví dụ, phân-
loại các tác vụ sử dụng các số liệu bao gồm độ chính xác (tổng thể chính xác các sự dự đoán), độ chính xác (precision) (tích cực
sự dự đoán độ chính xác), thu hồi (recall) (tích cực trường hợp sự phát hiện tỷ lệ), và F1 điểm số (độ chính xác-thu hồi điều hòa
trung bình) (Sokolova and Lapalme 2009) (For example, classification tasks employ metrics including accuracy (overall correct predictions), precision (positive prediction accuracy), recall (positive case detection rate), and F1 score (precision-recall harmonic mean) (Sokolova and Lapalme 2009)). Hồi quy các vấn đề sử dụng lỗi các sự đo lường giống như Trung bình (Mean)
Bình phương (Squared) Lỗi (MSE) và Trung bình (Mean) Tuyệt đối (Absolute) Lỗi (MAE) để đánh giá sự dự đoán độ chính xác (Regression problems use error measurements like Mean Squared Error (MSE) and Mean Absolute Error (MAE) to assess prediction accuracy). Cụ thể-
miền các ứng dụng thường yêu cầu chuyên môn hóa các số liệu; cho ví dụ, máy dịch thuật sử dụng BLEU17
để đo lường được sửa đổi n-gram độ chính xác chống lại một hoặc nhiều con người tham chiếu các sự dịch thuật (Papineni
et al. 2002) (Domain-specific applications often require specialized metrics; for example, machine translation uses BLEU17 to measure modified n-gram precision against one or more human reference translations (Papineni et al. 2002)).
Sản xuất sự triển khai thêm sự triển khai các số liệu tới tác vụ các số liệu (Production deployment adds implementation metrics to task metrics). Mô hình kích thước, được đo lường trong
các tham số hay bộ nhớ dấu chân, một cách trực tiếp ảnh hưởng sự triển khai tính khả thi qua khác nhau phần cứng
các nền tảng (Model size, measured in parameters or memory footprint, directly affects deployment feasibility across different hardware platforms). Việc xử lý độ trễ, một cách điển hình được đo lường trong các mili giây mỗi suy luận, xác định liệu
mô hình đáp ứng thời gian-thực các yêu cầu (Processing latency, typically measured in milliseconds per inference, determines whether the model meets real-time requirements). Năng lượng sự tiêu thụ, được đo lường trong các watts hay các joules mỗi
suy luận, chỉ ra hoạt động tính hiệu quả (Energy consumption, measured in watts or joules per inference, indicates operational efficiency). Những thực tế các sự xem xét này phản ánh đang phát triển nhu cầu
cho các giải pháp thứ mà cân bằng độ chính xác với tính toán tính hiệu quả (These practical considerations reflect the growing need for solutions that balance accuracy with computational efficiency). Hoạt động các thách thức
của việc duy trì những các số liệu này trong sản xuất các môi trường được khám phá trong sự triển khai các chiến lược
(Chương 14) (The operational challenges of maintaining these metrics in production environments are explored in deployment strategies (Chapter 14)).
Điểm chuẩn do đó cần một số liệu tập hợp thứ mà khớp cả hai tác vụ các yêu cầu và sự triển khai
các sự ràng buộc (The benchmark therefore needs a metric set that matches both task requirements and deployment constraints). Một đơn số liệu hiếm khi nắm bắt tất cả có liên quan các khía cạnh của hiệu suất trong thực-thế giới các kịch bản (A single metric rarely captures all relevant aspects of performance in real-world scenarios).
Cho ví dụ, trong sự bất thường sự phát hiện các hệ thống, cao độ chính xác một mình có thể không chỉ ra tốt hiệu suất
nếu mô hình tạo ra thường xuyên sai các báo động (For instance, in anomaly detection systems, high accuracy alone may not indicate good performance if the model generates frequent false alarms). Một cách tương tự, một nhanh mô hình với kém độ chính xác thất bại để
cung cấp thực tế giá trị (Similarly, a fast model with poor accuracy fails to provide practical value).
Này nhiều-số liệu sự đánh giá cách tiếp cận xuất hiện trong của chúng ta sự bất thường sự phát hiện hệ thống, thứ mà báo cáo
hiệu suất qua nhiều các chiều: mô hình kích thước (270K các tham số), việc xử lý tốc độ (10.4
ms/suy luận), sự phát hiện độ chính xác (0.86 AUC), và năng lượng sự tiêu thụ (516 µJ mỗi suy luận) (This multi-metric evaluation approach appears in our anomaly detection system, which reports performance across multiple dimensions: model size (270K parameters), processing speed (10.4 ms/inference), detection accuracy (0.86 AUC), and energy consumption (516 µJ per inference)). Này
sự kết hợp của các số liệu đảm bảo mô hình đáp ứng cả hai kỹ thuật và hoạt động các yêu cầu trong
thực-thế giới sự triển khai các kịch bản (This combination of metrics ensures the model meets both technical and operational requirements in real-world deployment scenarios).
12.5.5 Điểm chuẩn khung chằng (Benchmark harness)
Các số liệu định nghĩa cái gì để đo lường; điểm chuẩn khung chằng xác định cách nào để đo lường nó (Metrics define what to measure; the benchmark harness determines how to measure it). Một khung chằng
là kiểm tra cơ sở hạ tầng thứ mà phân phối các đầu vào tới hệ thống dưới bài kiểm tra, thu thập các sự đo lường, và
đảm bảo rằng toàn bộ quá trình là có thể tái tạo (A harness is the test infrastructure that delivers inputs to the system under test, collects measurements, and ensures that the entire process is reproducible). Mà không có một được thiết kế tốt khung chằng, thậm chí một cách hoàn hảo
được chọn các số liệu tạo ra không đáng tin cậy các con số (Without a well-designed harness, even perfectly chosen metrics produce unreliable numbers).
Khung chằng thiết kế phải căn chỉnh với dự định sự triển khai kịch bản (Harness design must align with the intended deployment scenario). Cho máy chủ các sự triển khai,
khung chằng tạo ra yêu cầu các mẫu thứ mà mô phỏng thực-thế giới lưu lượng, thường việc sử dụng một Poisson sự phân-
phối18 để mô hình hóa ngẫu nhiên nhưng thống kê nhất quán các khối lượng công việc, trong khi việc quản lý đồng thời các yêu cầu
và việc biến đổi tải các cường độ (For server deployments, the harness generates request patterns that simulate real-world traffic, often using a Poisson distribution18 to model random but statistically consistent workloads, while managing concurrent requests and varying load intensities).
Cho nhúng và di động các ứng dụng, khung chằng tạo ra đầu vào các mẫu thứ mà phản ánh thực tế
sự triển khai các điều kiện (For embedded and mobile applications, the harness generates input patterns that reflect actual deployment conditions). Điều này có thể liên quan tuần tự hình ảnh sự tiêm (injection) cho di động thị giác các ứng dụng
hay được đồng bộ hóa nhiều-cảm biến các luồng cho tự trị các hệ thống (This might involve sequential image injection for mobile vision applications or synchronized multi-sensor streams for autonomous systems). Như vậy chính xác đầu vào sự tạo ra và

662
12.5 Điểm chuẩn Các thành phần (Benchmark Components)
định thời sự kiểm soát đảm bảo hệ thống trải nghiệm thực tế hoạt động các mẫu, việc tiết lộ hiệu suất
các đặc điểm thứ mà sẽ nổi lên trong thực tế thiết bị sự triển khai (timing control ensures the system experiences realistic operational patterns, revealing performance characteristics that would emerge in actual device deployment).
Khung chằng phải cũng đáp ứng khác nhau thông lượng các mô hình (The harness must also accommodate different throughput models). Lô việc xử lý các kịch bản
yêu cầu khả năng để đánh giá hệ thống hiệu suất trên lớn các khối lượng của song song các đầu vào, trong khi thời gian-thực
các ứng dụng cần chính xác định thời sự kiểm soát cho tuần tự việc xử lý (Batch processing scenarios require the ability to evaluate system performance on large volumes of parallel inputs, while real-time applications need precise timing control for sequential processing). Trong nhúng sự triển khai
giai đoạn, khung chằng phải hỗ trợ chính xác sự đo lường của suy luận thời gian và năng lượng sự tiêu thụ
mỗi hoạt động (In the embedded implementation phase, the harness must support precise measurement of inference time and energy consumption per operation).
Khả năng tái tạo đòi hỏi rằng khung chằng duy trì nhất quán việc kiểm tra các điều kiện qua khác nhau
sự đánh giá các lượt chạy (Reproducibility demands that the harness maintain consistent testing conditions across different evaluation runs). Điều này bao gồm việc kiểm soát thuộc về môi trường các yếu tố chẳng hạn như nền các quá trình,
nhiệt các điều kiện, và điện năng các trạng thái thứ mà có thể ảnh hưởng hiệu suất các sự đo lường (This includes controlling environmental factors such as background processes, thermal conditions, and power states that might affect performance measurements). Khung chằng
phải cũng cung cấp các cơ chế cho việc thu thập và việc ghi nhật ký (logging) hiệu suất các số liệu mà không một cách có thể đo lường được
việc tác động hệ thống dưới bài kiểm tra (The harness must also provide mechanisms for collecting and logging performance metrics without measurably impacting the system under test).
12.5.6 Hệ thống các thông số kỹ thuật (System specifications)
Việc bổ sung khung chằng thứ mà kiểm soát bài kiểm tra sự thực thi, hệ thống các thông số kỹ thuật tài liệu hóa hoàn-
chỉnh tính toán môi trường: phần cứng và phần mềm ngăn xếp trên đó điểm chuẩn chạy (Complementing the harness that controls test execution, system specifications document the complete computational environment: the hardware and software stack on which the benchmark runs).
Mà không có chính xác các thông số kỹ thuật, một được báo cáo thông lượng con số là vô nghĩa: giống nhau mô hình
có thể huấn luyện nhanh hơn nhiều trên một mới hơn máy gia tốc hơn trên một cũ hơn cái, việc làm cho phần cứng ngữ cảnh
không thể tách rời từ kết quả (Without precise specifications, a reported throughput number is meaningless: the same model can train much faster on a newer accelerator than on an older one, making the hardware context inseparable from the result).
Trên phần cứng phía, các thông số kỹ thuật phải nắm bắt bộ xử lý loại và xung nhịp tỷ lệ, máy gia tốc
mô hình và bộ nhớ (GPU, TPU, hay tùy chỉnh ASIC), hệ thống RAM, lưu trữ loại, và mạng cấu-
hình cho được phân phối các thiết lập (On the hardware side, specifications must capture the processor type and clock rate, accelerator model and memory (GPU, TPU, or custom ASIC), system RAM, storage type, and network configuration for distributed setups). Trên phần mềm phía, chúng phải ghi lại hệ điều hành,
bộ khung các phiên bản (cho ví dụ, PyTorch 2.1 vs. TensorFlow 2.14), trình biên dịch các cờ, và môi trường
việc quản lý các công cụ chẳng hạn như Docker các vùng chứa (containers) hay ảo các môi trường (On the software side, they must record the operating system, framework versions (for example, PyTorch 2.1 vs. TensorFlow 2.14), compiler flags, and environment management tools such as Docker containers or virtual environments). Này cấp độ của chi tiết kích hoạt
khác các nhà nghiên cứu để sao chép điểm chuẩn môi trường với cao tính trung thực (fidelity) và cung cấp then chốt
ngữ cảnh cho việc diễn giải hiệu suất các sự khác biệt (This level of detail enables other researchers to replicate the benchmark environment with high fidelity and provides critical context for interpreting performance differences).
Nhiều các điểm chuẩn bao gồm các kết quả qua nhiều phần cứng các cấu hình, chính xác bởi vì
các sự đánh đổi giữa mô hình sự phức tạp, tính toán các tài nguyên, và hiệu suất chỉ trở nên có thể nhìn thấy
thông qua mang tính so sánh sự phân tích (Many benchmarks include results across multiple hardware configurations, precisely because the trade-offs between model complexity, computational resources, and performance only become visible through comparative analysis). Khi lĩnh vực ngày càng ưu tiên tính bền vững, các thông số kỹ thuật bây giờ
mở rộng tới năng lượng sự tiêu thụ các số liệu chẳng hạn như FLOP/s mỗi watt và tổng điện năng rút (draw) qua huấn luyện
thời gian, việc phản ánh đang phát triển nhận thức rằng tính toán tính hiệu quả là một kỹ thuật yêu cầu, không
đơn thuần một thuộc về môi trường khát vọng (As the field increasingly prioritizes sustainability, specifications now extend to energy consumption metrics such as FLOP/s per watt and total power draw over training time, reflecting growing awareness that computational efficiency is an engineering requirement, not merely an environmental aspiration).
12.5.7 Chạy các quy tắc (Run rules)
Hệ thống các thông số kỹ thuật mô tả cái gì điểm chuẩn chạy trên; chạy các quy tắc chi phối (govern) cách nào nó chạy (System specifications describe what the benchmark runs on; run rules govern how it runs). Những
mang tính thủ tục các sự ràng buộc này đảm bảo rằng các kết quả có thể được sao chép một cách đáng tin cậy, điều mà khó hơn hơn nó có vẻ
trong một lĩnh vực nơi ngẫu nhiên các quá trình (trọng số sự khởi tạo, dữ liệu sự xáo trộn, và dropout các mặt nạ) có nghĩa là
hai giống hệt các lượt chạy trên giống hệt phần cứng có thể tạo ra khác nhau các con số (These procedural constraints ensure that results can be reliably replicated, which is harder than it sounds in a field where stochastic processes (weight initialization, data shuffling, and dropout masks) mean that two identical runs on identical hardware can produce different numbers). Chạy các quy tắc thuần hóa (tame) này
sự ngẫu nhiên bằng cách việc bắt buộc (mandating) cố định các hạt giống (seeds), được kiểm soát dữ liệu sự sắp xếp, và có hệ thống sự xử lý của mọi
nguồn của tính không xác định (Run rules tame this randomness by mandating fixed seeds, controlled data ordering, and systematic handling of every source of nondeterminism).
Siêu tham số (Hyperparameter) tài liệu hóa là quan trọng một cách tương đương (Hyperparameter documentation is equally critical). Một học-tỷ lệ sự thay đổi có thể chuyển dịch sự hội tụ
và cuối cùng độ chính xác, do đó các điểm chuẩn yêu cầu thấu đáo việc ghi lại của mọi cấu hình cài đặt (A learning-rate change can shift convergence and final accuracy, so benchmarks require exhaustive recording of every configuration setting).
Một cách tương tự, các điểm chuẩn bắt buộc sự bảo tồn và sự chia sẻ của huấn luyện và sự đánh giá các tập dữ liệu;
khi quyền riêng tư hay cấp phép các sự ràng buộc ngăn cản trực tiếp sự chia sẻ, chi tiết sự tiền xử lý các thông số kỹ thuật
kích hoạt sự xây dựng của có thể so sánh các tập dữ liệu (Similarly, benchmarks mandate the preservation and sharing of training and evaluation datasets; when privacy or licensing constraints prevent direct sharing, detailed preprocessing specifications enable construction of comparable datasets).
Mã nguồn gốc (Code provenance) hoàn thành khả năng tái tạo chuỗi (Code provenance completes the reproducibility chain). Đương đại các điểm chuẩn một cách điển hình
yêu cầu sự xuất bản của sự triển khai mã trong được kiểm soát-phiên bản các kho lưu trữ—không chỉ mô hình,
nhưng đầy đủ đường ống của sự tiền xử lý, huấn luyện, và sự đánh giá các kịch bản (Contemporary benchmarks typically require publication of implementation code in version-controlled repositories—not just the model, but the full pipeline of preprocessing, training, and evaluation scripts). Tiên tiến các điểm chuẩn
phân phối được đóng vùng chứa các môi trường thứ mà đóng gói tất cả các sự phụ thuộc và các cấu hình, trong khi
việc bắt buộc chi tiết mang tính thực nghiệm việc ghi nhật ký: huấn luyện các số liệu, mô hình các điểm kiểm tra (checkpoints), và tài liệu hóa
của bất kỳ giữa-thực nghiệm các sự điều chỉnh nào (Advanced benchmarks distribute containerized environments that encapsulate all dependencies and configurations, while mandating detailed experimental logging: training metrics, model checkpoints, and documentation of any mid-experiment adjustments). Cùng nhau, những các giao thức này biến đổi việc đo điểm chuẩn từ một
một-lần sự đo lường thành một có thể xác minh, có thể lặp lại khoa học quá trình (Together, these protocols transform benchmarking from a one-time measurement into a verifiable, iterable scientific process).
12.5.8 Kết quả sự diễn giải (Result interpretation)
Việc tạo ra điểm chuẩn các con số là dễ dàng phần; việc diễn giải chúng một cách chính xác là nơi hầu hết các kỹ sư
đi sai (Producing benchmark numbers is the easy part; interpreting them correctly is where most engineers go wrong). Một thô thông lượng con số hay độ chính xác điểm số là vô nghĩa mà không việc hiểu

12. Việc đo điểm chuẩn (Benchmarking)
663
các điều kiện thứ mà đã tạo ra nó, thống kê độ tin cậy (confidence) đằng sau nó, và sự triển khai ngữ cảnh thứ mà
xác định liệu con số quan trọng (conditions that produced it, the statistical confidence behind it, and the deployment context that determines whether the number matters).
Ví dụ 12.2: Việc đo điểm chuẩn một thị giác mô hình cho biên sự triển khai (Benchmarking a vision model for edge deployment)
Kịch bản (Scenario): Một nhóm xác nhận MobileNetV2 (Sandler et al. 2018) cho một động vật hoang dã máy ảnh bẫy (camera trap) đang chạy
trên một Raspberry Pi 4 (A team validates MobileNetV2 (Sandler et al. 2018) for a wildlife camera trap running on a Raspberry Pi 4).
Then chốt câu hỏi là liệu độ chính xác chi phí của INT8 là có thể chấp nhận được cho này sự triển khai—
bảng 12.6 cho thấy rằng sự lượng tử hóa đánh đổi một khiêm tốn độ chính xác sự sụt giảm cho ấn tượng độ trễ và kích thước
các sự cải thiện (The critical question is whether the accuracy cost of INT8 is acceptable for this deployment—table 12.6 shows that quantization trades a modest accuracy drop for dramatic latency and size improvements):
Bảng 12.6: MobileNetV2 INT8 sự lượng tử hóa sự đánh đổi (MobileNetV2 INT8 quantization trade-off): Độ trễ, độ chính xác, và mô hình kích thước cho FP32 và INT8 các độ chính xác
trên MobileNetV2 (Latency, accuracy, and model size for FP32 and INT8 precisions on MobileNetV2).
Độ chính xác (Precision)
Độ trễ (ms) (Latency (ms))
Độ chính xác (Top-1) (Accuracy (Top-1))
Mô hình Kích thước (Model Size)
FP32
120 ms
71.8%
14 MB
INT8
35 ms
70.9%
3.5 MB
Các hệ thống sự thấu hiểu (Systems insight): 3.4× sự tăng tốc và 4× kích thước sự giảm từ sự lượng tử hóa đến tại một chi phí
của 0.9 phần trăm các điểm của top-1 độ chính xác (The 3.4× speedup and 4× size reduction from quantization come at a cost of 0.9 percentage points of top-1 accuracy). Cho một được cấp nguồn bằng pin thời gian-thực hệ thống với này
sự dung sai (tolerance), INT8 là rõ ràng sự lựa chọn, việc kích hoạt khoảng 28.6 FPS việc xử lý so sánh với khoảng 8.3
FPS với FP32 (For a battery-powered real-time system with this tolerance, INT8 is the clear choice, enabling about 28.6 FPS processing compared to about 8.3 FPS with FP32).
Trước khi việc rút ra các kết luận từ điểm chuẩn các kết quả, áp dụng nhà cung cấp tuyên bố sự phân tích bộ khung
được giới thiệu trước đó (xem “Việc giải mã Nhà cung cấp Điểm chuẩn Các tuyên bố” danh sách kiểm tra) và mở rộng nó với
hai bổ sung các kiểm tra (Before drawing conclusions from benchmark results, apply the vendor claim analysis framework introduced earlier (see the “Decoding Vendor Benchmark Claims” checklist) and extend it with two additional checks). Đầu tiên, sự so sánh phải công bằng: việc so sánh ResNet-50 chống lại MobileNet
hợp nhất kiến trúc các sự khác biệt với sự tối ưu hóa các sự lựa chọn; độ chính xác các sự khác biệt (FP32 vs. INT8)
một mình có thể giải thích 2–4× hiệu suất các khoảng cách, và lô kích thước, phần cứng thế hệ, và phần mềm
bộ khung phải tất cả được kiểm soát (First, the comparison must be fair: comparing ResNet-50 against MobileNet conflates architecture differences with optimization choices; precision differences (FP32 vs. INT8) alone can explain 2–4× performance gaps, and batch size, hardware generation, and software framework must all be controlled). Thứ hai, các thống kê phải có ý nghĩa: đáng tin cậy các kết quả yêu cầu
nhiều các lượt chạy, được báo cáo sự biến thiên với độ tin cậy các khoảng, rõ ràng sự xử lý của các ngoại lai (outliers), và ổn-
định-trạng thái hoạt động thay vì lạnh-khởi động các hiệu ứng (Second, the statistics must be meaningful: reliable results require multiple runs, reported variance with confidence intervals, clear handling of outliers, and steady-state operation rather than cold-start effects). Việc áp dụng những các câu hỏi này tới một đại diện nhà cung cấp
tuyên bố minh họa cách nào không hoàn chỉnh các thông số kỹ thuật che khuất thực hiệu suất (Applying these questions to a representative vendor claim illustrates how incomplete specifications obscure real performance).
Vượt ra ngoài nhà cung cấp các tuyên bố, ngữ cảnh xác định cái nào các số liệu quan trọng nhất (Beyond vendor claims, context determines which metrics matter most). Một 1 phần trăm độ chính xác
sự cải thiện có thể quyết định cho y tế các sự chẩn đoán nhưng không liên quan cho một ứng dụng thứ mà ưu tiên
suy luận tốc độ (A 1 percent accuracy improvement may be decisive for medical diagnostics but irrelevant for an application that prioritizes inference speed). Các nhà thực hành nên cũng bảo vệ chống lại điểm chuẩn sự quá khớp (overfitting), nơi các mô hình được
tối ưu hóa một cách quá mức cho cụ thể điểm chuẩn các tác vụ tại chi phí của thực-thế giới sự khái quát hóa, bằng cách
việc đánh giá hiệu suất trên có liên quan nhưng khác biệt các tác vụ và việc xem xét thực tế sự triển khai các kịch bản (Practitioners should also guard against benchmark overfitting, where models are excessively optimized for specific benchmark tasks at the expense of real-world generalization, by evaluating performance on related but distinct tasks and considering practical deployment scenarios).
Các hệ thống Phối cảnh 12.6: Việc diễn giải một điểm chuẩn tuyên bố (Systems Perspective 12.6: Interpreting a benchmark claim)
Một nhà cung cấp tuyên bố “Của chúng tôi hệ thống đạt được 10,000 các suy luận/giây trên ResNet-50.” (A vendor claims “Our system achieves 10,000 inferences/second on ResNet-50.”) Được lấy một mình,
con số không thể hỗ trợ sự triển khai việc lập kế hoạch bởi vì các điều kiện thứ mà xác định của nó
ý nghĩa là không được nêu (Taken alone, the number cannot support deployment planning because the conditions that determine its meaning are unstated).
Bốn không được nêu các điều kiện xác định cái gì tuyên bố có ý nghĩa (Four unstated conditions determine what the claim means):
1. Lô kích thước (Batch size): Lớn các lô thường đạt được cao thông lượng nhưng có thể vi phạm độ trễ các mục tiêu;
lô 1 đạt được thấp độ trễ nhưng thấp hơn thông lượng (Large batches often achieve high throughput but can violate latency targets; batch 1 achieves low latency but lower throughput).
2. Độ chính xác (Precision): INT8 là 2–4× nhanh hơn hơn FP32 trên được hỗ trợ phần cứng nhưng có thể có độ chính xác
hay sự hiệu chuẩn các hàm ý (INT8 is 2–4× faster than FP32 on supported hardware but may have accuracy or calibration implications).
3. Sự đo lường ranh giới (Measurement boundary): Tuyên bố phải nêu liệu nó bao phủ thuần túy suy luận hay
bao gồm sự tiền xử lý (The claim must state whether it covers pure inference or includes preprocessing).
4. Độ chính xác (Accuracy): Tuyên bố phải nêu liệu mô hình khớp nguyên bản 76.1 phần trăm
Top-1 hay một bị suy thoái cấp độ (The claim must state whether the model matches the original 76.1 percent Top-1 or a degraded level).

664
12.5 Điểm chuẩn Các thành phần (Benchmark Components)
Một hoàn chỉnh thông số kỹ thuật: “10,000 các suy luận/giây trên ResNet-50 tại lô kích thước 32, INT8
độ chính xác, 76 phần trăm Top-1 độ chính xác, bao gồm JPEG việc giải mã, trên NVIDIA H100 tại 700 W
TDP.” (A complete specification: “10,000 inferences/second on ResNet-50 at batch size 32, INT8 precision, 76 percent Top-1 accuracy, including JPEG decoding, on NVIDIA H100 at 700 W TDP.”)
Các hệ thống sự thấu hiểu (Systems insight): Việc hiểu liệu một hiệu suất sự khác biệt là có ý nghĩa yêu cầu
cả hai thống kê sự nghiêm ngặt và thuộc về ngữ cảnh sự xác nhận (Understanding whether a performance difference is meaningful requires both statistical rigor and contextual validation). Một điểm chuẩn con số mà không có những các chi tiết này là
một tiếp thị tuyên bố, không phải một kỹ thuật thông số kỹ thuật (A benchmark number without these details is a marketing claim, not an engineering specification).
12.5.9 Ví dụ điểm chuẩn (Example benchmark)
Để thấy cách nào những các thành phần này làm việc cùng nhau trong thực tế, bước thông qua sự bất thường sự phát hiện đường ống
trong hình 12.4 một lần nữa, bây giờ việc tập trung trên đầu ra giai đoạn (To see how these components work together in practice, walk through the anomaly detection pipeline in figure 12.4 one more time, now focusing on the output stage). Điểm chuẩn tạo ra ba
bổ sung các sự đo lường: một mô hình kích thước của 270K các tham số với 10.4 ms mỗi suy luận (tính-
toán các tài nguyên), một sự phát hiện độ chính xác của 0.86 AUC trong việc phân biệt bình thường từ bất thường
âm thanh các mẫu (tác vụ tính hiệu quả), và một năng lượng sự tiêu thụ của 516 µJ mỗi suy luận (hoạt động
tính hiệu quả) (The benchmark produces three complementary measurements: a model size of 270K parameters with 10.4 ms per inference (computational resources), a detection accuracy of 0.86 AUC in distinguishing normal from anomalous audio patterns (task effectiveness), and an energy consumption of 516 µJ per inference (operational efficiency)).
Cái nào của những các số liệu này quan trọng nhất phụ thuộc hoàn toàn trên sự triển khai ngữ cảnh (Which of these metrics matters most depends entirely on the deployment context). Năng lượng sự tiêu-
thụ mỗi suy luận là then chốt cho được cấp nguồn bằng pin các thiết bị nhưng không liên quan cho luôn-bật máy chủ
các giá đỡ (racks) (Energy consumption per inference is critical for battery-powered devices but irrelevant for always-on server racks). Mô hình kích thước ràng buộc nhúng các thiết bị với bị giới hạn bộ nhớ nhưng hầu như không ghi nhận (registers) cho
đám mây các sự triển khai (Model size constrains embedded devices with limited memory but barely registers for cloud deployments). Việc xử lý tốc độ xác định liệu hệ thống có thể hoạt động trong thời gian-thực hay
phải tạo lô các đầu vào (Processing speed determines whether the system can operate in real-time or must batch inputs). Những các số liệu này cũng tiết lộ vốn có các sự đánh đổi: việc giảm mô hình kích thước từ 270K
các tham số có thể cải thiện tốc độ và năng lượng tính hiệu quả nhưng làm suy thoái 0.86 AUC sự phát hiện độ chính-
xác (These metrics also reveal inherent trade-offs: reducing model size from 270K parameters might improve speed and energy efficiency but degrade the 0.86 AUC detection accuracy). Liệu những các sự đo lường này cấu thành một “vượt qua” điểm chuẩn phụ thuộc trên sự triển khai
các sự ràng buộc—bộ khung cung cấp cấu trúc cho nhất quán sự đánh giá, nhưng sự chấp nhận các tiêu chí
phải đến từ ứng dụng các yêu cầu (Whether these measurements constitute a “passing” benchmark depends on the deployment constraints—the framework provides structure for consistent evaluation, but acceptance criteria must come from the application requirements).
Các thành phần vừa được liệt kê định nghĩa cách nào để lắp ráp bất kỳ đơn điểm chuẩn nào (The components just enumerated define how to assemble any single benchmark). Hai điểm chuẩn
các danh mục lặp lại đủ thường xuyên qua sự tối ưu hóa đường ống để đảm bảo của riêng chúng thành phần
các danh sách kiểm tra ở đây: sự nén các điểm chuẩn, thứ mà một được cắt tỉa hay được lượng tử hóa mô hình phải vượt qua trước khi
sự triển khai, và di động và biên các điểm chuẩn, thứ mà một bị ràng buộc-nhiệt và điện năng mục tiêu
áp đặt (Two benchmark categories recur often enough across the optimization pipeline to warrant their own component checklists here: compression benchmarks, which a pruned or quantized model must pass before deployment, and mobile and edge benchmarks, which a power- and thermally-constrained target imposes). Mỗi cái kết hợp (composes) tác vụ, dữ liệu, mô hình, các số liệu, khung chằng, và chạy các quy tắc vừa được định nghĩa trong khi
việc thêm các sự ràng buộc chung danh sách kiểm tra không (làm) (Each composes the task, data, model, metrics, harness, and run rules just defined while adding constraints the generic checklist does not). Cả hai là các bản xem trước của các chiều chương
phát triển đầy đủ sau này: sự nén sự xác nhận quay lại trong phần 12.11.1.3 với đầy đủ nhiều-số liệu
giao thức, và được duy trì-điện năng hành vi quay lại trong phần 12.9 (Both are previews of dimensions the chapter develops fully later: compression validation returns in section 12.11.1.3 with the full multi-metric protocol, and sustained-power behavior returns in section 12.9).
12.5.10 Sự nén các điểm chuẩn (Compression benchmarks)
Thần kinh mạng sự nén (việc cắt tỉa, sự lượng tử hóa, kiến thức sự chưng cất, và kiến trúc sự tối-
ưu hóa) yêu cầu chuyên môn hóa các điểm chuẩn bởi vì sự nén định hình lại sự đánh đổi cảnh quan:
mọi byte được tiết kiệm hay hoạt động bị loại bỏ phải được cân nhắc chống lại tiềm năng độ chính xác sự mất mát và
phần cứng tính tương thích (Neural network compression (pruning, quantization, knowledge distillation, and architecture optimization) requires specialized benchmarks because compression reshapes the trade-off landscape: every byte saved or operation eliminated must be weighed against potential accuracy loss and hardware compatibility). Cơ bản nhất sự nén số liệu là thô kích thước sự giảm: tham số số đếm,
bộ nhớ dấu chân trong các byte, và được nén lưu trữ các yêu cầu (The most basic compression metric is raw size reduction: parameter count, memory footprint in bytes, and compressed storage requirements). Kích thước một mình, tuy nhiên, là gây hiểu-
lầm (misleading) (Size alone, however, is misleading). Trên ImageNet, MobileNetV2 đạt được xấp xỉ 72 phần trăm top-1 độ chính xác với 3.5M
các tham số vs. ResNet-50’s 76 phần trăm độ chính xác với 25.6M các tham số, khoảng 7.3× ít hơn các tham số
tại có thể so sánh độ chính xác, hay đại khái 6.9× nhiều hơn độ chính xác mỗi tham số (Sandler et al. 2018; He et al.
2016a) (On ImageNet, MobileNetV2 achieves approximately 72 percent top-1 accuracy with 3.5M parameters vs. ResNet-50’s 76 percent accuracy with 25.6M parameters, about 7.3× fewer parameters at comparable accuracy, or roughly 6.9× more accuracy per parameter (Sandler et al. 2018; He et al. 2016a)).
Việc cắt tỉa các điểm chuẩn phải phân biệt giữa có cấu trúc và không có cấu trúc các cách tiếp cận, bởi vì
chúng tạo ra một cách chất lượng khác nhau các kết quả trên thực phần cứng (Pruning benchmarks must distinguish between structured and unstructured approaches, because they produce qualitatively different results on real hardware). Có cấu trúc việc cắt tỉa loại bỏ toàn bộ
các nơ-ron hay các bộ lọc, việc sinh ra nhỏ hơn dày đặc các hoạt động thứ mà thông thường các hạt nhân có thể khai thác (H. Li
et al. 2017) (Structured pruning removes entire neurons or filters, yielding smaller dense operations that conventional kernels can exploit (H. Li et al. 2017)). Không có cấu trúc việc cắt tỉa loại bỏ cá nhân các trọng số và có thể tạo ra rất thưa thớt
các mô hình, nhưng việc nhận ra thực tế các sự tăng tốc yêu cầu chuyên môn hóa thưa thớt tính toán sự hỗ trợ—việc có nghĩa là
điểm chuẩn các giao thức phải quy định phần cứng nền tảng và phần mềm sự triển khai (Han et al. 2015;
Gale et al. 2019) (Unstructured pruning eliminates individual weights and can produce very sparse models, but realizing actual speedups requires specialized sparse computation support—meaning benchmark protocols must specify hardware platform and software implementation (Han et al. 2015; Gale et al. 2019)).
Sự lượng tử hóa các điểm chuẩn đánh giá độ chính xác sự giảm qua dữ liệu các loại (Quantization benchmarks evaluate precision reduction across data types). INT8 phân phối
4× bộ nhớ sự giảm và 2–4× suy luận sự tăng tốc được định lượng cho MobileNetV2 ngọn hải đăng (lighthouse) trong
bảng 12.6, với độ chính xác-độ chính xác sự đánh đổi được phân tích trong phần 12.8.2 và năng lượng các hàm ý
trong phần 12.7.2.4 (INT8 delivers the 4× memory reduction and 2–4× inference speedup quantified for the MobileNetV2 lighthouse in table 12.6, with the precision-accuracy trade-off analyzed in section 12.8.2 and the energy implications in section 12.7.2.4). Hỗn hợp-độ chính xác các cách tiếp cận đẩy xa hơn bằng cách việc áp dụng khác nhau độ chính xác các cấp độ
tới khác nhau các lớp: then chốt các lớp giữ lại FP16 trong khi nặng-tính toán các lớp sử dụng INT8 hay INT4,
(Mixed-precision approaches push further by applying different precision levels to different layers: critical layers retain FP16 while computation-heavy layers use INT8 or INT4,)

12. Việc đo điểm chuẩn (Benchmarking)
665
việc kích hoạt mịn-hạt (fine-grained) tính hiệu quả sự tối ưu hóa (enabling fine-grained efficiency optimization). Kiến thức sự chưng cất thêm một chiều khác: một
nhỏ hơn học sinh mô hình có thể bảo tồn nhiều của một giáo viên’s hành vi trong khi việc giảm kích thước và suy luận
chi phí, nhưng việc đo điểm chuẩn phải xác minh rằng học sinh khái quát hóa thay vì đơn thuần việc ghi nhớ
giáo viên’s các đầu ra (Hinton et al. 2015) (Knowledge distillation adds another dimension: a smaller student model can preserve much of a teacher’s behavior while reducing size and inference cost, but benchmarking must verify that the student generalizes rather than merely memorizing the teacher’s outputs (Hinton et al. 2015)).
Một cách then chốt, sự gia tốc các hệ số biến đổi một cách ấn tượng qua phần cứng các nền tảng: thưa thớt các mô hình,
được giảm-độ chính xác các mô hình, và hiệu quả các kiến trúc chỉ phân phối các sự tăng tốc khi mục tiêu thời gian chạy
có các hạt nhân, bộ nhớ các bố cục, và máy gia tốc sự hỗ trợ thứ mà khai thác chúng (Critically, acceleration factors vary dramatically across hardware platforms: sparse models, reduced-precision models, and efficient architectures only deliver speedups when the target runtime has kernels, memory layouts, and accelerator support that exploit them). Hiện tại điểm chuẩn các bộ phần mềm
giống như MLPerf tập trung chủ yếu trên được chuẩn hóa tham chiếu các mô hình, trong khi sản xuất các sự triển khai thường
sử dụng được nén hoặc cụ thể-phần cứng các biến thể (Current benchmark suites like MLPerf focus primarily on standardized reference models, while production deployments often use compressed or hardware-specific variants). Này khoảng cách giữa cái gì các điểm chuẩn đo lường và
cái gì sản xuất thực tế chạy duy trì một của lĩnh vực’s mang tính hậu quả nhất điểm mù (This gap between what benchmarks measure and what production actually runs remains one of the field’s most consequential blind spots).
12.5.11 Di động và biên các điểm chuẩn (Mobile and edge benchmarks)
Di động và biên các sự triển khai đối mặt các sự ràng buộc một cách triệt để khác nhau từ đám mây các môi trường, việc yêu cầu
chuyên môn hóa việc đo điểm chuẩn các cách tiếp cận thứ mà nắm bắt duy nhất các sự đánh đổi trong bị ràng buộc-tài nguyên
các thiết lập (Mobile and edge deployments face constraints radically different from cloud environments, requiring specialized benchmarking approaches that capture the unique trade-offs in resource-constrained settings). Những các sự ràng buộc này hình thành một phụ thuộc lẫn nhau tam giác của điện năng sự tiêu thụ, suy luận độ trễ,
và mô hình độ chính xác, nơi việc cải thiện bất kỳ hai thường làm suy thoái cái thứ ba (These constraints form an interdependent triangle of power consumption, inference latency, and model accuracy, where improving any two typically degrades the third). Biên sự triển khai
yêu cầu việc điều hướng các sự đánh đổi thứ mà đám mây các sự triển khai có thể phần lớn phớt lờ, được tóm tắt trong bảng 12.7 (Edge deployment requires navigating trade-offs that cloud deployments can largely ignore, summarized in table 12.7).
Bảng 12.7: Biên so với Đám mây Sự triển khai Các sự ràng buộc (Edge vs. Cloud Deployment Constraints): Giống nhau ba các sự ràng buộc (điện năng, độ trễ, độ chính xác) mang
một cách cơ bản khác nhau các ý nghĩa qua sự triển khai các ngữ cảnh (The same three constraints (power, latency, accuracy) carry fundamentally different meanings across deployment contexts). Đám mây các hệ thống xử lý điện năng như một hoạt động chi phí và độ trễ như một
UX số liệu, việc để lại độ chính xác như chính sự tối ưu hóa mục tiêu; biên các hệ thống phải xử lý điện năng và độ trễ như cứng vật lý
các giới hạn, việc để lại độ chính xác như thặng dư (residual) biến số để tối ưu hóa (Cloud systems treat power as an operational cost and latency as a UX metric, leaving accuracy as the primary optimization target; edge systems must treat power and latency as hard physical limits, leaving accuracy as the residual variable to optimize).
Sự ràng buộc (Constraint)
Đám mây Tác động (Cloud Impact)
Biên Tác động (Edge Impact)
Điện năng (Power)
Hoạt động chi phí (~$0.10/kWh) (Operational cost (~$0.10/kWh))
Cứng giới hạn (pin dung lượng) (Hard limit (battery capacity))
Độ trễ (Latency)
Người dùng trải nghiệm số liệu (User experience metric)
An toàn-then chốt thời hạn (Safety-critical deadline)
Độ chính xác (Accuracy)
Chính sự tối ưu hóa mục tiêu (Primary optimization target)
Bị ràng buộc bởi điện năng/độ trễ (Constrained by power/latency)
Như một cụ thể ví dụ, một điện thoại thông minh máy ảnh AI cho thời gian-thực đối tượng sự phát hiện có thể cần để xử lý
tốc độ-video các đầu vào trong khi việc ở bên trong một chặt chẽ nhiệt vỏ bọc (envelope) (As a concrete example, a smartphone camera AI for real-time object detection may need to process video-rate inputs while staying inside a tight thermal envelope). Trong đó thiết lập, một họ-MobileNet
mô hình có thể là đúng điểm chuẩn mục tiêu thậm chí nếu một lớn hơn họ-ResNet mô hình báo cáo cao hơn
độ chính xác trong một đám mây thiết lập, bởi vì biên điểm chuẩn phải bao gồm được duy trì độ trễ, điện năng, và
nhiệt hành vi (In that setting, a MobileNet-family model can be the correct benchmark target even if a larger ResNet-family model reports higher accuracy in a cloud setting, because the edge benchmark must include sustained latency, power, and thermal behavior). Một được duy trì biên điểm chuẩn phơi bày những khoảng cách này giữa được tiếp thị các thông số kỹ thuật
và hoạt động hành vi (A sustained edge benchmark exposes these gaps between marketed specifications and operational behavior). Đỉnh-so với-được duy trì khoảng cách được thiết lập trong phần 12.1 trở nên cấp tính
tại biên cho một vật lý lý do vắng mặt trong dữ liệu trung tâm: một cách thụ động được làm mát thiết bị không thể rũ bỏ
nhiệt của liên tục suy luận một cách vô hạn, do đó bùng nổ-chế độ các con số có thể suy thoái dưới nhiệt
sự điều tiết (throttling) (The peak-versus-sustained gap established in section 12.1 turns acute at the edge for a physical reason absent in the data center: a passively cooled device cannot shed the heat of continuous inference indefinitely, so burst-mode numbers can degrade under thermal throttling). Đó nhiệt cơ chế, không phải sự đo lường sự cẩu thả, làm cho biên việc đo điểm chuẩn một
một cách phân loại khác nhau bài tập (exercise) hơn đám mây việc đo điểm chuẩn (That thermal mechanism, not measurement sloppiness, makes edge benchmarking a categorically different exercise than cloud benchmarking).
Ví dụ 12.3: Việc đo điểm chuẩn biên (Benchmarking the edge)
Kịch bản (Scenario): Một kỹ thuật nhóm đang chọn một thiết bị cho một thông minh chuông cửa (smart doorbell). Nhà cung cấp tuyên bố
chip chạy “AI tại 1 W.” (An engineering team is selecting a device for a smart doorbell. The vendor claims the chip runs “AI at 1 W.”)
Thiết lập (Setup): Một liên tục đối tượng sự phát hiện vòng lặp được chạy (A continuous object detection loop is run).
Sự quan sát (Observation):
1. Sớm bùng nổ (Early burst): Chip chạy một cách nhanh chóng tại được quảng cáo điện năng điểm (The chip runs quickly at the advertised power point).
2. Nhiệt sự tích tụ (Heat buildup): Được duy trì suy luận làm tăng tiếp giáp (junction) nhiệt độ (Sustained inference raises junction temperature).
3. Nhiệt sự điều tiết (Thermal throttling): Xung nhịp tốc độ giảm để ở bên trong nhiệt vỏ bọc (The clock speed drops to stay inside the thermal envelope).
4. Ổn định trạng thái (Steady state): Chip ổn định tại một thấp hơn thông lượng hơn bùng nổ kết quả (The chip stabilizes at a lower throughput than the burst result).
Các hệ thống sự thấu hiểu (Systems insight): Đỉnh kết quả là không phải sản phẩm thực tế (The peak result is not the product reality). Một người dùng trải nghiệm được thiết kế xung quanh
bùng nổ thông lượng bị phá vỡ từ bắt đầu (A user experience designed around burst throughput is broken from the start). Luôn luôn đo điểm chuẩn được duy trì hiệu suất, không chỉ
đỉnh (Always benchmark sustained performance, not just peak).

666
12.5 Điểm chuẩn Các thành phần (Benchmark Components)
bùng nổ (burst)
đầu gối (knee)
được duy trì (sustained)
Bùng nổ (Burst) điểm chuẩn FPS sụp đổ
một khi nhiệt sự điều tiết (throttling) thiết lập vào (Burst benchmark FPS collapses once thermal throttling sets in).
19
URLLC (Siêu-Đáng tin cậy
Thấp-Độ trễ
Sự giao-
tiếp (Ultra-Reliable Low-Latency Communication)):
5G dịch vụ danh mục
việc yêu cầu
99.999
phần trăm
độ tin cậy và <1 ms độ trễ (URLLC (Ultra-Reliable Low-Latency Communication): 5G service category requiring 99.999 percent reliability and <1 ms latency).
Những kép các sự ràng buộc này ép buộc
một các hệ thống sự đánh đổi: việc đẩy
tính toán
gần hơn
tới
người dùng
giảm khứ hồi (round-trip) độ trễ,
nhưng
biên
phần cứng
có sẵn
tại
đó
vị trí
có thể nhỏ hơn và nhiều
bị ràng buộc điện năng hơn hơn một
được tập trung hóa
đám mây
cụm (These dual constraints force a systems trade-off: pushing compute closer to users reduces round-trip latency, but the edge hardware available at that location may be smaller and more power constrained than a centralized cloud cluster).
URLLC
việc đo điểm chuẩn
phải do đó đo lường
toàn bộ chuỗi:
vô tuyến (radio) độ trễ
+ tính toán độ trễ + mô hình
độ chính xác tại bị ràng buộc
kích thước (URLLC benchmarking must therefore measure the entire chain: radio latency + compute latency + model accuracy at the constrained size).
Nhiệt sự điều tiết trong một bị ràng buộc thụ động-việc làm mát vỏ bọc (envelope) có thể bắt đầu trong suốt được duy trì suy luận,
việc làm cho ngắn bùng nổ các điểm chuẩn gây hiểu lầm cho luôn-bật các ứng dụng (Thermal throttling in a constrained passive-cooling envelope can begin during sustained inference, making short burst benchmarks misleading for always-on applications). Bất kỳ biên sự đánh giá nào phải
do đó tính toán cho được duy trì điện năng rút (draw) dưới nhiệt ổn định trạng thái, không phải bùng nổ-chế độ các đỉnh, và
phải đo lường đầu-tới-đầu độ trễ bao gồm dữ liệu sự chuyển giao chi phí chung (Any edge evaluation must therefore account for sustained power draw under thermal steady state, not burst-mode peaks, and must measure end-to-end latency including data transfer overhead).
Các hệ thống Phối cảnh 12.7: Biên điểm chuẩn thực tế kiểm tra (Systems Perspective 12.7: Edge benchmark reality check)
Khi việc đánh giá biên phần cứng các tuyên bố, bốn các yếu tố xác định liệu nhà cung cấp các con số
dịch thuật thành thực-thế giới hiệu suất (When evaluating edge hardware claims, four factors determine whether vendor numbers translate to real-world performance):
1. Đỉnh so với được duy trì (Peak vs. sustained): Một nhà cung cấp có thể quảng cáo 45 TOPS đỉnh thông lượng trong khi một được duy trì
nhiệt lượt chạy phân phối gần hơn tới 20 TOPS (A vendor may advertise 45 TOPS peak throughput while a sustained thermal run delivers closer to 20 TOPS). Luôn luôn đo điểm chuẩn dưới được duy trì các khối lượng công việc
dài hơn hơn 30 s (Always benchmark under sustained workloads longer than 30 s).
2. Điện năng tại nhàn rỗi so với hoạt động (Power at idle vs. active): Trong này kịch bản, một thiết bị việc tiêu thụ 50 mW nhàn rỗi và 2 W hoạt động
có thể báo cáo hoạt động rút (draw) cho tiếp thị, nhưng nếu ứng dụng chạy suy luận 1 phần trăm của
thời gian, hiệu quả điện năng rút là ~69.5 mW, không phải 2 W (In this scenario, a device consuming 50 mW idle and 2 W active could report active draw for marketing, but if the application runs inference 1 percent of the time, effective power draw is ~69.5 mW, not 2 W).
3. Nhiệt vỏ bọc (Thermal envelope): Biên các thiết bị thường hoạt động bên trong một hẹp nhiệt thiết kế điện năng
(TDP) vỏ bọc (Edge devices often operate inside a narrow thermal design power (TDP) envelope). Việc vượt quá nó kích hoạt sự điều tiết, do đó điểm chuẩn các báo cáo việc bỏ sót nhiệt
các điều kiện là không hoàn chỉnh (Exceeding it triggers throttling, so benchmark reports omitting thermal conditions are incomplete).
4. Đầu-tới-đầu so với máy gia tốc-chỉ (End-to-end vs. accelerator-only): NPU các điểm chuẩn thường loại trừ dữ liệu sự chuyển giao chi phí chung (NPU benchmarks often exclude data transfer overhead).
Việc di chuyển hình ảnh dữ liệu từ máy ảnh tới NPU và quay lại có thể vượt quá suy luận thời gian cho nhỏ
các mô hình (Moving image data from camera to NPU and back can exceed inference time for small models).
12.5.11.1 Không đồng nhất bộ xử lý sự phối hợp (Heterogeneous processor coordination)
Di động SoCs tích hợp không đồng nhất các bộ xử lý (CPU, GPU, DSP, NPU) việc yêu cầu chuyên môn hóa
việc đo điểm chuẩn thứ mà nắm bắt khối lượng công việc sự phân phối sự phức tạp trong khi việc tính toán cho nhiệt và
pin các sự ràng buộc (Mobile SoCs integrate heterogeneous processors (CPU, GPU, DSP, NPU) requiring specialized benchmarking that captures workload distribution complexity while accounting for thermal and battery constraints). Hiệu quả bộ xử lý sự phối hợp có thể phân phối lớn các khoản đạt được khi công việc được đặt
trên bộ xử lý thứ mà khớp của nó tính toán mẫu (Effective processor coordination can deliver large gains when work is placed on the processor that matches its compute pattern). Mỗi bộ xử lý xuất sắc tại khác nhau khối lượng công việc
các hồ sơ (profiles): các CPUs xử lý kiểm soát luồng, nhỏ các lô, và tuần tự việc xử lý; các GPUs gia tốc song song
dấu phẩy động các hoạt động và chung ML suy luận; các DSPs xuất sắc tại cố định-điểm tín hiệu việc xử lý và
luôn-bật sự phát hiện các tác vụ; và các NPUs nhắm mục tiêu cụ thể thần kinh mạng các kiến trúc với INT8/INT4
độ chính xác (Each processor excels at different workload profiles: CPUs handle control flow, small batches, and sequential processing; GPUs accelerate parallel floating-point operations and general ML inference; DSPs excel at fixed-point signal processing and always-on detection tasks; and NPUs target specific neural network architectures with INT8/INT4 precision).
Các điểm chuẩn phải đánh giá khối lượng công việc sự đặt (placement) các quyết định, không chỉ cá nhân bộ xử lý hiệu-
suất (Benchmarks must evaluate workload placement decisions, not just individual processor performance). Một giọng nói trợ lý, cho ví dụ, có thể sử dụng một thấp-điện năng DSP cho luôn-bật đánh-thức-từ (wake-word)
sự phát hiện, chuyển sang một NPU cho một ngắn lời nói-sự nhận dạng bùng nổ, và sử dụng CPU cho ngôn ngữ
sự hiểu (A voice assistant, for example, might use a low-power DSP for always-on wake-word detection, switch to an NPU for a short speech-recognition burst, and use the CPU for language understanding). Đơn-bộ xử lý các điểm chuẩn bỏ lỡ những sự điều phối (orchestration) các động lực học này hoàn toàn (Single-processor benchmarks miss these orchestration dynamics entirely).
12.5.11.2 Pin và nhiệt việc đo điểm chuẩn (Battery and thermal benchmarking)
Pin tác động biến đổi một cách ấn tượng bởi sử dụng trường hợp: tính toán nhiếp ảnh có thể tiêu thụ các watts
trong suốt hoạt động sự nắm bắt (capture), trong khi nền AI cho hoạt động sự nhận dạng có thể cần để ở trong một milliwatt-
quy mô ngân sách cho có thể chấp nhận được cả-ngày sức chịu đựng (endurance) (Battery impact varies dramatically by use case: computational photography can consume watts during active capture, while background AI for activity recognition may need to stay in a milliwatt-scale budget for acceptable all-day endurance). Thách thức là rằng tức thời điện năng rút (draw) trong suốt
suy luận kể chỉ một phần của câu chuyện; cái gì quan trọng cho pin tuổi thọ là tổng năng lượng ngân sách qua một
thực tế sử dụng mẫu (The challenge is that instantaneous power draw during inference tells only part of the story; what matters for battery life is the total energy budget across a realistic usage pattern).
Quan trọng nhất yếu tố là khối lượng công việc chu kỳ nhiệm vụ (duty cycle): cái gì phần nhỏ của thời gian hệ thống thực tế
chạy suy luận (The most important factor is the workload duty cycle: what fraction of time the system actually runs inference). Một chuông cửa máy ảnh thứ mà xử lý thỉnh thoảng các khung hình (frames) dành gần như tất cả của nó thời gian nhàn rỗi,
việc làm cho chờ (standby) điện năng thống trị mối quan tâm (A doorbell camera that processes occasional frames spends nearly all its time idle, making standby power the dominant concern). Một thời gian-thực video phân tích (analytics) đường ống, ngược lại, là
bị ràng buộc-suy luận gần như liên tục, việc làm cho mỗi-suy luận năng lượng then chốt số liệu (A real-time video analytics pipeline, by contrast, is inference-bound almost continuously, making per-inference energy the critical metric). Nền
điện năng, năng lượng được tiêu thụ khi mô hình được tải nhưng đang chờ đợi cho đầu vào, bắc cầu (bridges) những thái cực này
và thường vượt quá suy luận năng lượng cho ngắt quãng (intermittent) các khối lượng công việc (Background power, the energy consumed when the model is loaded but waiting for input, bridges these extremes and often exceeds inference energy for intermittent workloads). Cuối cùng, được duy trì nhiệt hành vi
phải được đặc trưng hóa qua các phút thay vì các giây, bởi vì biên các thiết bị thứ mà phân phối ấn tượng
bùng nổ hiệu suất thường xuyên điều tiết (throttle) khi tiếp giáp (junction) các nhiệt độ tăng, việc ổn định tại một cách đáng kể thấp hơn
ổn định-trạng thái thông lượng (Finally, sustained thermal behavior must be characterized over minutes rather than seconds, because edge devices that deliver impressive burst performance frequently throttle as junction temperatures rise, settling at substantially lower steady-state throughput).
12.5.11.3 Biên-đám mây sự phối hợp (Edge-cloud coordination)
Di động việc đo điểm chuẩn phải cũng đánh giá 5G/Wi-Fi biên-đám mây sự phối hợp, với URLLC19 nhấn-

12. Việc đo điểm chuẩn (Benchmarking)
667
mạnh rất thấp độ trễ và cao độ tin cậy cho then chốt các ứng dụng (sizing very low latency and high reliability for critical applications). Này sự phối hợp giới thiệu
việc đo điểm chuẩn các chiều vắng mặt từ thuần túy cục bộ sự đánh giá (This coordination introduces benchmarking dimensions absent from purely local evaluation). Mạng độ trễ sự biến thiên có nghĩa là
rằng suy luận các đường ống việc chia (splitting) công việc giữa thiết bị và đám mây đối mặt không thể dự đoán được khứ hồi các chi phí (Network latency variability means that inference pipelines splitting work between device and cloud face unpredictable round-trip costs).
Dự phòng (Fallback) hành vi xác định cái gì xảy ra khi tính kết nối thất bại hoàn toàn: liệu thiết bị
suy thoái một cách duyên dáng tới một nhỏ hơn trên-thiết bị mô hình hay xếp hàng các yêu cầu cho đến khi tính kết nối tiếp tục lại (Fallback behavior determines what happens when connectivity fails entirely: whether the device degrades gracefully to a smaller on-device model or queues requests until connectivity resumes).
Khối lượng công việc việc chia các quyết định (cái gì tính toán chạy một cách cục bộ so với một cách từ xa) và quyền riêng tư các sự ràng buộc
(cái gì dữ liệu có thể được truyền cho đám mây suy luận) xa hơn định hình điểm chuẩn thiết kế không gian (Workload splitting decisions (what computation runs locally vs. remotely) and privacy constraints (what data can be transmitted for cloud inference) further shape the benchmark design space). Mỗi
của những các chiều này phải được đo lường dưới thực tế mạng các điều kiện thay vì được lý tưởng hóa phòng thí nghiệm
tính kết nối (Each of these dimensions must be measured under realistic network conditions rather than idealized lab connectivity).
Ô tô các sự triển khai thêm ASIL sự xác nhận, nhiều-cảm biến sự dung hợp (fusion), và rộng-nhiệt độ thuộc về môi-
trường việc kiểm tra (Automotive deployments add ASIL validation, multi-sensor fusion, and wide-temperature environmental testing). Những duy nhất các yêu cầu này đòi hỏi toàn diện các bộ khung việc đánh giá
được duy trì hiệu suất dưới nhiệt các sự ràng buộc, pin tính hiệu quả qua sử dụng các mẫu, và
phụ thuộc-tính kết nối hành vi, việc mở rộng vượt ra ngoài được cô lập đỉnh các sự đo lường (These unique requirements necessitate comprehensive frameworks evaluating sustained performance under thermal constraints, battery efficiency across usage patterns, and connectivity-dependent behavior, extending beyond isolated peak measurements).
Liệu việc đo điểm chuẩn đám mây các máy chủ hay các vi điều khiển, tuy nhiên, một then chốt sự phân biệt cắt
qua tất cả sự triển khai các ngữ cảnh: giống nhau thần kinh mạng cư xử hoàn toàn khác nhau phụ thuộc trên
liệu nó đang học hay đang dự đoán (Whether benchmarking cloud servers or microcontrollers, however, a critical distinction cuts across all deployment contexts: the same neural network behaves entirely differently depending on whether it is learning or predicting). Này sự phân biệt định hình cái gì chúng ta đo lường, cách nào chúng ta đo lường nó,
và cái nào các số liệu quan trọng—và nó là quá cơ bản đến mức riêng biệt việc đo điểm chuẩn các bộ khung đã
nổi lên cho mỗi giai đoạn (This distinction shapes what we measure, how we measure it, and which metrics matter—and it is so fundamental that separate benchmarking frameworks have emerged for each phase).
12.6 Huấn luyện so với Suy luận (Training vs. Inference)
Giống nhau máy gia tốc có thể thất bại trong đối lập các cách: một huấn luyện công việc có thể lãng phí các ngày bởi vì gradient
sự đồng bộ hóa thống trị, trong khi một suy luận dịch vụ có thể bỏ lỡ của nó SLO bởi vì đuôi độ trễ tăng vọt (spikes)
dưới bùng nổ lưu lượng (The same accelerator can fail in opposite ways: a training job may waste days because gradient synchronization dominates, while an inference service may miss its SLO because tail latency spikes under bursty traffic). Huấn luyện và suy luận do đó tạo ra sự đánh giá các yêu cầu quá khác biệt
đến mức riêng biệt việc đo điểm chuẩn các bộ khung đã nổi lên cho mỗi cái: MLPerf Huấn luyện và MLPerf Suy luận
(Mattson et al. 2020; Reddi et al. 2019) (Training and inference therefore create evaluation requirements so different that separate benchmarking frameworks emerged for each: MLPerf Training and MLPerf Inference (Mattson et al. 2020; Reddi et al. 2019)). Then chốt câu hỏi là liệu lý thuyết TFLOP/s dịch thuật
tới thực tế thời gian-tới-huấn luyện hay các truy vấn-mỗi-giây (The critical question is whether theoretical TFLOP/s translate to practical time-to-train or queries-per-second). Huấn luyện tìm kiếm tối ưu các tham số thông qua mang tính lặp lại
sự tinh chỉnh (Chương 8), việc xử lý hàng tỷ của các ví dụ qua các giờ hay các ngày, việc làm căng thẳng bộ nhớ
băng thông, nhiều-GPU việc mở rộng quy mô, và được duy trì thông lượng (Training seeks optimal parameters through iterative refinement (Chapter 8), processing billions of examples over hours or days, stressing memory bandwidth, multi-GPU scaling, and sustained throughput). Suy luận áp dụng những các tham số đó tới
cá nhân các đầu vào trong việc phục vụ các hệ thống (Chương 13), thường bên trong mili giây các thời hạn, việc làm căng thẳng
độ trễ tính nhất quán, lạnh-khởi động thời gian (mô hình khởi động sự trì hoãn), và điện năng tính hiệu quả; Chương 14 kết nối
những các sự đo lường đó tới sự triển khai (rollout) và việc giám sát thực hành (Inference applies those parameters to individual inputs in serving systems (Chapter 13), often within millisecond deadlines, stressing latency consistency, cold-start time (model startup delay), and power efficiency; Chapter 14 connects those measurements to rollout and monitoring practice).
Các sự khác biệt xếp tầng (cascade) thông qua mọi khía cạnh của hệ thống thiết kế (The differences cascade through every aspect of system design). Huấn luyện liên quan hai chiều
tính toán (chuyển tiếp và ngược lại các lượt chạy), trong khi suy luận thực hiện đơn chuyển tiếp các lượt chạy với
cố định các tham số (Training involves bidirectional computation (forward and backward passes), while inference performs single forward passes with fixed parameters). Bộ nhớ sự phân bổ phân kỳ một cách sắc nét: huấn luyện yêu cầu đồng thời sự truy cập tới
các tham số, các gradients, bộ tối ưu hóa các trạng thái, và các sự kích hoạt, việc tạo ra 3–4× bộ nhớ chi phí chung so sánh
tới suy luận (Memory allocation diverges sharply: training requires simultaneous access to parameters, gradients, optimizer states, and activations, creating 3–4× memory overhead compared to inference). Huấn luyện sử dụng hỗn hợp-độ chính xác tính toán và gradient sự nén để quản lý
này chi phí chung, trong khi suy luận sử dụng tích cực hơn độ chính xác sự giảm (được chi tiết trong phần 12.8.2)
và các kỹ thuật giống như hậu-huấn luyện sự lượng tử hóa và kiến thức sự chưng cất (Training employs mixed-precision computation and gradient compression to manage this overhead, while inference uses more aggressive precision reduction (detailed in section 12.8.2) and techniques like post-training quantization and knowledge distillation). Tài nguyên sự sử dụng
các mẫu cũng tương phản: huấn luyện nhắm mục tiêu được duy trì GPU sự bão hòa, trong khi đó suy luận đương đầu (contends) với
việc biến đổi yêu cầu các mẫu thứ mà để lại phần cứng bị sử dụng dưới mức, như roofline sự phân tích trong phần 12.3.2
đã chứng minh (Resource utilization patterns also contrast: training targets sustained GPU saturation, whereas inference contends with variable request patterns that leave hardware underutilized, as the roofline analysis in section 12.3.2 demonstrated).
Năng lượng các chi phí theo sau khác nhau các mẫu (Energy costs follow different patterns). Huấn luyện năng lượng các chi phí được khấu hao qua mô hình vòng đời
và được đo lường trong tổng năng lượng mỗi được huấn luyện mô hình; các ước tính cho lớn huấn luyện các lượt chạy có thể đạt quy mô
của hàng ngàn của các megawatt-giờ (GPT-3 đã được ước tính tại đại khái 1,287 MWh) (Patterson et
al. 2021) (Training energy costs are amortized across model lifetime and measured in total energy per trained model; estimates for large training runs can reach the scale of thousands of megawatt-hours (GPT-3 has been estimated at roughly 1,287 MWh) (Patterson et al. 2021)). Suy luận năng lượng các chi phí tích lũy mỗi truy vấn và có thể trở thành một thống trị hoạt động
sự xem xét tại quy mô (Inference energy costs accumulate per query and can become a dominant operational consideration at scale). Một bền bỉ cách để lý luận về mỗi-truy vấn năng lượng là đồng nhất (identity) 𝐸total =
Power×𝑇 (A durable way to reason about per-query energy is the identity 𝐸total = Power×𝑇). Cho ví dụ, một 300 W máy gia tốc đang chạy một 10 ms suy luận tiêu thụ 300𝑊×0.01𝑠= 3𝐽,
thứ mà là khoảng 0.0008 Wh; tại 100 ms, đó trở thành khoảng 0.0083 Wh (For example, a 300 W accelerator running a 10 ms inference consumes 300𝑊×0.01𝑠= 3𝐽, which is about 0.0008 Wh; at 100 ms, that becomes about 0.0083 Wh).
Huấn luyện-so với-suy luận sự phân biệt hướng dẫn điểm chuẩn thiết kế bằng cách việc làm nổi bật cái nào các số liệu
quan trọng nhất cho mỗi giai đoạn và cách nào sự đánh giá các phương pháp luận phải khác nhau (The training-vs.-inference distinction guides benchmark design by highlighting which metrics matter most for each phase and how evaluation methodologies must differ). Huấn luyện các điểm chuẩn nhấn-
mạnh sự hội tụ thời gian và việc mở rộng quy mô tính hiệu quả; suy luận các điểm chuẩn ưu tiên độ trễ tính nhất quán
và tài nguyên tính hiệu quả qua đa dạng sự triển khai các kịch bản (Training benchmarks emphasize convergence time and scaling efficiency; inference benchmarks prioritize latency consistency and resource efficiency across diverse deployment scenarios). Chúng ta kiểm tra huấn luyện các điểm chuẩn đầu tiên,
bởi vì chất lượng của được huấn luyện mô hình thiết lập trần cho mọi thứ suy luận có thể phân phối (We examine training benchmarks first, because the quality of the trained model sets the ceiling for everything inference can deliver).

668
12.7 Huấn luyện Các điểm chuẩn (Training Benchmarks)
20
GPT-3: OpenAI’s 2020
ngôn ngữ mô hình (175B các tham-
số, 300B huấn luyện các tokens)
đã tiêu thụ một được ước tính 3,640
petaFLOP-các ngày
trên
10,000
V100 GPUs (Patterson et al.
2021) (GPT-3: OpenAI’s 2020 language model (175B parameters, 300B training tokens) consumed an estimated 3,640 petaFLOP-days on 10,000 V100 GPUs (Patterson et al. 2021)).
Này quy mô minh họa
tại sao
huấn luyện
các điểm chuẩn
là thiết yếu cho việc dự đoán
liệu một được lập kế hoạch huấn luyện
lượt chạy là về mặt hoạt động khả thi
trước khi
việc cam kết
tính-
toán (This scale illustrates why training benchmarks are essential for predicting whether a planned training run is operationally viable before committing the compute).
12.7 Huấn luyện Các điểm chuẩn (Training Benchmarks)
Trong một mang tính minh họa sự mua sắm (procurement) thất bại, một nhóm mua một lớn hơn GPU cụm việc mong đợi tỷ lệ
huấn luyện-tốc độ các khoản đạt được, chỉ để khám phá rằng giao tiếp chi phí chung và bộ nhớ các nút thắt cổ chai giới hạn
thực tế sự tăng tốc (In an illustrative procurement failure, a team purchases a larger GPU cluster expecting proportional training-speed gains, only to discover that communication overhead and memory bottlenecks limit the actual speedup). Huấn luyện các điểm chuẩn tồn tại để bắt loại này của khoảng cách trước khi sự mua sắm (Training benchmarks exist to catch this kind of gap before procurement).
Chúng chia thành ba các danh mục: sự hội tụ các số liệu thứ mà đo lường học tập tiến độ, thông lượng
các số liệu thứ mà đo lường tính toán tính hiệu quả, và khả năng mở rộng quy mô các số liệu thứ mà đo lường được phân phối
hiệu suất (They divide into three categories: convergence metrics that measure learning progress, throughput metrics that measure computational efficiency, and scalability metrics that measure distributed performance).
Huấn luyện các điểm chuẩn xác nhận liệu phần cứng sự gia tốc phân phối được hứa hẹn huấn luyện thông-
lượng (Training benchmarks validate whether hardware acceleration delivers promised training throughput). GPU các cụm, TPU pods, và được phân phối huấn luyện các chiến lược được kiểm tra trong Chương 11 tất cả tuyên bố
ấn tượng các sự tăng tốc, và huấn luyện các điểm chuẩn tiết lộ cái nào các tuyên bố giữ vững dưới thực tế các khối lượng công việc (The GPU clusters, TPU pods, and distributed training strategies examined in Chapter 11 all claim dramatic speedups, and training benchmarks reveal which claims hold under realistic workloads).
Chúng đánh giá cách nào phần cứng các cấu hình, dữ liệu việc tải các cơ chế, và được phân phối huấn luyện
các chiến lược hoạt động khi việc huấn luyện sản xuất-quy mô các mô hình (They evaluate how hardware configurations, data loading mechanisms, and distributed training strategies perform when training production-scale models). Những các điểm chuẩn này là quan trọng bởi vì
huấn luyện đại diện cho lớn nhất vốn chi tiêu (capital expenditure) trong ML các hệ thống, và chỉ nghiêm ngặt thời gian-tới-độ chính xác
sự đo lường tiết lộ liệu đó vốn phân phối tỷ lệ giá trị thay vì việc tiêu tán thành
việc mở rộng quy mô các sự kém hiệu quả, bộ nhớ các nút thắt cổ chai, hay giao tiếp chi phí chung (These benchmarks are vital because training represents the largest capital expenditure in ML systems, and only rigorous time-to-accuracy measurement reveals whether that capital delivers proportional value rather than dissipating into scaling inefficiencies, memory bottlenecks, or communication overhead).
Cho ví dụ, lớn-quy mô các mô hình giống như OpenAI’s GPT-320 (Brown et al. 2020), thứ mà bao gồm của 175B
các tham số được huấn luyện trên xấp xỉ 570 GB của được lọc CommonCrawl văn bản (từ một ~45 TB thô
tập dữ liệu, được kết hợp với khác các nguồn để hình thành 300B huấn luyện các tokens), làm nổi bật khổng lồ tính toán-
toán các đòi hỏi của hiện đại huấn luyện (For instance, large-scale models like OpenAI’s GPT-320 (Brown et al. 2020), which consists of 175B parameters trained on approximately 570 GB of filtered CommonCrawl text (from a ~45 TB raw dataset, combined with other sources to form 300B training tokens), highlight the immense computational demands of modern training). Được chuẩn hóa ML huấn luyện các điểm chuẩn cung cấp có hệ thống
sự đánh giá của bên dưới các hệ thống để đảm bảo rằng phần cứng và phần mềm các cấu hình có thể đáp ứng
những chưa từng có các đòi hỏi này một cách hiệu quả (Standardized ML training benchmarks provide systematic evaluation of the underlying systems to ensure that hardware and software configurations can meet these unprecedented demands efficiently).
Định nghĩa 12.3: ML huấn luyện các điểm chuẩn (Definition 12.3: ML training benchmarks)
ML Huấn luyện Các điểm chuẩn là máy học hệ thống các điểm chuẩn thứ mà đo lường thời gian để
đạt tới một mục tiêu chất lượng số liệu (cho ví dụ, một được quy định sự xác nhận độ chính xác hay mất mát ngưỡng) trên
một cố định tập dữ liệu và mô hình, việc định lượng tỷ lệ của sự hội tụ mỗi đơn vị của tài nguyên (ML Training Benchmarks are machine learning system benchmarks that measure the time to reach a target quality metric (for example, a specified validation accuracy or loss threshold) on a fixed dataset and model, quantifying the rate of convergence per unit of resource).
1. Ý nghĩa (Significance): Huấn luyện các điểm chuẩn tiết lộ lớn các khoảng cách vô hình tới phần cứng các thông số kỹ thuật (Training benchmarks reveal large gaps invisible to hardware specs). Việc giữ
mô hình và chất lượng mục tiêu cố định, thời gian tới sự hội tụ có thể biến đổi một cách rộng rãi qua
phần cứng-phần mềm các ngăn xếp bởi vì huấn luyện hiệu suất phụ thuộc trên đầy đủ đường ống:
dữ liệu việc tải (𝐷vol/BW), tính toán sự sử dụng (𝜂hw), gradient sự đồng bộ hóa (𝐿lat), và
lỗi phục hồi chi phí chung (Holding the model and quality target fixed, the time to convergence can vary widely across hardware-software stacks because training performance depends on the full pipeline: data loading (𝐷vol/BW), compute utilization (𝜂hw), gradient synchronization (𝐿lat), and fault recovery overhead). Một đỉnh FLOP/s thông số kỹ thuật tờ (sheet) nắm bắt không (cái nào) của những các sự tương tác này (A peak FLOP/s spec sheet captures none of these interactions).
2. Sự phân biệt (Distinction): Không giống suy luận các điểm chuẩn, thứ mà đo lường mỗi-truy vấn độ trễ và
thông lượng dưới tải, huấn luyện các điểm chuẩn đo lường thời gian-tới-độ chính xác qua đầy đủ
sự tối ưu hóa vòng lặp: dữ liệu việc tải, chuyển tiếp lượt chạy, ngược lại lượt chạy, gradient sự đồng bộ hóa,
và bộ tối ưu hóa bước (Unlike inference benchmarks, which measure per-query latency and throughput under load, training benchmarks measure time-to-accuracy across the full optimization loop: data loading, forward pass, backward pass, gradient synchronization, and optimizer step). Có tính ràng buộc sự ràng buộc chuyển dịch từ tính toán (𝑅peak) tại nhỏ quy mô tới
giao tiếp (BW) tại lớn quy mô (The binding constraint shifts from compute (𝑅peak) at small scale to communication (BW) at large scale).
3. Chung cạm bẫy (Common pitfall): Một thường xuyên quan niệm sai lầm là rằng huấn luyện các điểm chuẩn đo lường “cách nào
nhanh GPU chạy.” (A frequent misconception is that training benchmarks measure “how fast the GPU runs.”) Tại lớn quy mô, liên kết mạng (interconnect) băng thông (BW) cho gradient sự đồng bộ-
hóa và lỗi dung sai (tolerance) chi phí chung (điểm kiểm tra I/O, sự tụt hậu (straggler) sự giảm nhẹ) thường thống trị
điểm chuẩn kết quả nhiều hơn đỉnh FLOP/s (At large scale, interconnect bandwidth (BW) for gradient synchronization and fault tolerance overhead (checkpoint I/O, straggler mitigation) often dominate the benchmark result more than peak FLOP/s).
12.7.1 Huấn luyện điểm chuẩn động lực (Training benchmark motivation)
MLPerf Huấn luyện (Mattson et al. 2020; MLCommons 2024c) cung cấp được chuẩn hóa bộ khung cho
loại này của thời gian-tới-chất lượng sự đo lường, và của nó tác động là đáng chú ý: hình 12.5 chứng minh rằng
hiệu suất các sự cải thiện qua liên tiếp MLPerf Huấn luyện điểm chuẩn các phiên bản đã một cách nhất quán
vượt xa một Moore’s Định luật đường cơ sở, với một vài các khối lượng công việc việc cho thấy rất lớn nhiều-năm các sự tăng tốc
(Tschand et al. 2024) (MLPerf Training (Mattson et al. 2020; MLCommons 2024c) provides the standardized framework for this kind of time-to-quality measurement, and its impact is striking: figure 12.5 demonstrates that performance improvements across successive MLPerf Training benchmark versions have consistently outpaced a Moore’s Law baseline, with some workloads showing very large multi-year speedups (Tschand et al. 2024)). Này theo cấp số nhân sự cải thiện minh họa một cốt lõi nguyên tắc: cái gì được đo lường
được cải thiện (This exponential improvement illustrates a core principle: what gets measured gets improved). Được chuẩn hóa việc đo điểm chuẩn bộ khung tạo ra mang tính cạnh tranh áp lực thứ mà thúc đẩy
nhanh chóng sự tối ưu hóa qua toàn bộ ML tính toán ngăn xếp (The standardized benchmarking framework creates competitive pressure that drives rapid optimization across the entire ML computing stack).
Vượt ra ngoài việc lập biểu đồ đó tiến độ, huấn luyện các điểm chuẩn khám phá các sự kém hiệu quả thứ mà có hệ thống
sự đánh giá làm cho có thể nhìn thấy: chậm dữ liệu việc tải, bị sử dụng dưới mức các máy gia tốc, quá mức bộ nhớ chi phí chung,
và giao tiếp các nút thắt cổ chai thứ mà ăn mòn việc mở rộng quy mô tính hiệu quả (Beyond charting that progress, training benchmarks uncover the inefficiencies that systematic evaluation makes visible: slow data loading, underutilized accelerators, excessive memory overhead, and communication bottlenecks that erode scaling efficiency). Lý thuyết phần cứng các khả năng

12. Việc đo điểm chuẩn (Benchmarking)
669
12/18
06/19
12/19
06/20
12/20
06/21
12/21
06/22
12/22
06/23
12/23
06/24
1
2
4
8
16
32
64
Tương đối hiệu suất - Tốt nhất các kết quả - Đã đóng, có sẵn, trên cơ sở (Relative performance - Best results - Closed, available, on premises)
ResNet
Mask R-CNN
RetinaNet
3D-U-Net
BERT-large
GPT3
DLRM
DLRM-dcnv2
Stable diffusion v2
Moore's Định luật Tích lũy (Moores Law Cumulative)
Hình 12.5: MLPerf Huấn luyện Tiến độ (MLPerf Training Progress): Được chuẩn hóa các điểm chuẩn tiết lộ rằng máy học huấn luyện hiệu suất
một cách nhất quán vượt qua Moore’s Định luật, việc chỉ ra đáng kể các khoản đạt được từ cấp độ-các hệ thống các sự tối ưu hóa (Standardized benchmarks reveal that machine learning training performance consistently surpasses Moore’s Law, indicating substantial gains from systems-level optimizations). Những các xu hướng này nhấn mạnh cách nào
được tập trung sự đo lường và mang tính lặp lại sự cải thiện thúc đẩy nhanh chóng các sự tiến bộ trong ML huấn luyện tính hiệu quả và khả năng mở rộng quy mô (These trends emphasize how focused measurement and iterative improvement drive rapid advancements in ML training efficiency and scalability). Nguồn:
(Tschand et al. 2024).
21
Hỗn hợp-Độ chính xác Huấn-
luyện (Mixed-Precision Training):
Sử dụng thấp hơn độ chính xác
cho hầu hết số học trong khi
việc bảo tồn cao hơn-độ chính xác
sự tích lũy nơi được cần
(Micikevicius et al.
2017) (Uses lower precision for most arithmetic while preserving higher-precision accumulation where needed (Micikevicius et al. 2017)).
Việc đo điểm chuẩn
hệ-
quả (benchmarking consequence): hỗn hợp-độ chính xác và
đầy đủ-độ chính xác các lượt chạy là không phải
có thể so sánh một cách trực tiếp bởi vì
được giảm bộ nhớ lưu lượng và
lớn hơn khả thi lô các kích thước có thể
thay đổi sự hội tụ các động lực-
học (mixed-precision and full-precision runs are not directly comparable because reduced memory traffic and larger feasible batch sizes can change convergence dynamics).
MLPerf giải quyết này
bằng cách việc cố định độ chính xác mục tiêu,
việc làm cho
thời gian-tới-độ chính xác
có thể so sánh
đại lượng
bất kể
của
độ chính xác
chiến lược (MLPerf addresses this by fixing the accuracy target, making time-to-accuracy the comparable quantity regardless of precision strategy).
22
Thông lượng (Throughput): Từ sản-
xuất (manufacturing), nơi nó đã đo lường
các đơn vị việc đi qua một sản-
xuất dây chuyền mỗi đơn vị thời gian (From manufacturing, where it measured units passing through a production line per unit time).
Thuật ngữ đã đi vào tính toán
trong những năm 1960 lô-việc xử lý
kỷ nguyên (The term entered computing in the 1960s batch-processing era). Sản xuất nguồn-
gốc (origin) mang một các hệ thống bài học:
thông lượng và độ trễ là
vốn dĩ đối lập, bởi vì
việc tạo lô làm tăng thông-
lượng (nhiều hơn các đơn vị mỗi giờ) tại
chi phí của cá nhân mục (item)
chờ thời gian (The manufacturing origin carries a systems lesson: throughput and latency are inherently opposed, because batching increases throughput (more units per hour) at the cost of individual item wait time).
Trong ML việc phục vụ,
này biểu hiện như lô-
kích thước sự đánh đổi: lớn hơn các lô
cải thiện GPU sự sử dụng nhưng
làm tăng mỗi-yêu cầu độ trễ (In ML serving, this manifests as the batch-size trade-off: larger batches improve GPU utilization but increase per-request latency).
được thiết lập trong Chương 11 (cho ví dụ, GPU TFLOP/s, TPU tensor thông lượng) chỉ dịch thuật tới
thực tế huấn luyện các sự tăng tốc khi các điểm chuẩn xác minh chúng dưới thực tế các điều kiện (established in Chapter 11 (for example, GPU TFLOP/s, TPU tensor throughput) only translate to actual training speedups when benchmarks verify them under realistic conditions).
Huấn luyện các điểm chuẩn phục vụ bốn được kết nối với nhau các chức năng (Training benchmarks serve four interconnected functions). Đầu tiên, chúng kích hoạt phần cứng và phần-
mềm sự tối ưu hóa bằng cách việc cung cấp trung lập-nhà cung cấp các sự so sánh qua máy gia tốc các kiến trúc và
các bộ khung (TensorFlow, PyTorch) trên được chuẩn hóa các tác vụ, việc hướng dẫn phần cứng sự lựa chọn cho dữ liệu
các trung tâm và đám mây các môi trường (First, they enable hardware and software optimization by providing vendor-neutral comparisons across accelerator architectures and frameworks (TensorFlow, PyTorch) on standardized tasks, guiding hardware selection for data centers and cloud environments). Phần mềm các sự tối ưu hóa bao gồm hỗn hợp-độ chính xác huấn luyện21 và
hiệu quả-bộ nhớ dữ liệu việc tải được định lượng một cách tương tự (Software optimizations including mixed-precision training21 and memory-efficient data loading are similarly quantified). Thứ hai, chúng đánh giá khả năng mở rộng quy mô: việc thêm
các GPUs nên giảm huấn luyện thời gian một cách tỷ lệ, nhưng giao tiếp chi phí chung, sự đồng bộ hóa
độ trễ, và bộ nhớ các nút thắt cổ chai giới hạn việc mở rộng quy mô tính hiệu quả trong thực tế (Second, they evaluate scalability: adding GPUs should reduce training time proportionally, but communication overhead, synchronization latency, and memory bottlenecks limit scaling efficiency in practice). Huấn luyện các điểm chuẩn định lượng
những các sự mất mát này, việc tiết lộ liệu cơ sở hạ tầng các khoản đầu tư phân phối tỷ lệ các khoản hoàn lại (Training benchmarks quantify these losses, revealing whether infrastructure investments deliver proportional returns). Thứ ba, chúng
cung cấp chi phí và năng lượng tính trách nhiệm giải trình (accountability): với lớn-quy mô huấn luyện các lượt chạy việc tiêu thụ hàng ngàn của
các megawatt-giờ, các điểm chuẩn thứ mà theo dõi chi phí mỗi huấn luyện lượt chạy và điện năng sự tiêu thụ mỗi đơn vị của
tiến độ giúp các tổ chức cân bằng tính toán điện năng với tính bền vững các mục tiêu (Third, they provide cost and energy accountability: with large-scale training runs consuming thousands of megawatt-hours, benchmarks that track cost per training run and power consumption per unit of progress help organizations balance computational power with sustainability goals). Cuối cùng, chúng
đảm bảo công bằng, có thể tái tạo sự so sánh thông qua được chuẩn hóa sự đánh giá các tiêu chí, được kiểm soát tính ngẫu-
nhiên (randomness), và nghiêm ngặt sự đệ trình các hướng dẫn thứ mà đảm bảo hiệu suất các kết quả phản ánh chân thực hệ thống
các khả năng thay vì cụ thể-sự triển khai sự tinh chỉnh (tuning) (Finally, they ensure fair, reproducible comparison through standardized evaluation criteria, controlled randomness, and strict submission guidelines that guarantee performance results reflect genuine system capabilities rather than implementation-specific tuning).
12.7.2 Huấn luyện các số liệu (Training metrics)
Từ một các hệ thống phối cảnh, huấn luyện các điểm chuẩn đánh giá cách nào một cách hiệu quả một mô hình đạt tới một được xác định trước
độ chính xác ngưỡng (From a systems perspective, training benchmarks assess how efficiently a model reaches a predefined accuracy threshold). Các số liệu giống như thông lượng và khả năng mở rộng quy mô là chỉ có ý nghĩa tương đối tới liệu
mô hình đạt được của nó mục tiêu độ chính xác; mà không có này sự ràng buộc, việc tối ưu hóa thô tốc độ có thể là
gây hiểu lầm (Metrics like throughput and scalability are only meaningful relative to whether the model achieves its target accuracy; without this constraint, optimizing raw speed may be misleading). MLPerf Huấn luyện hệ thống hóa (codifies) này bằng cách việc định nghĩa cụ thể độ chính xác các mục tiêu mỗi tác vụ: một hệ thống
thứ mà huấn luyện một cách nhanh chóng nhưng bỏ lỡ mục tiêu là không hợp lệ, và một (hệ thống) thứ mà hội tụ một cách chính xác nhưng quá chậm
là không thực tế (MLPerf Training codifies this by defining specific accuracy targets per task: a system that trains quickly but misses the target is invalid, and one that converges accurately but too slowly is impractical). Hiệu quả việc đo điểm chuẩn cân bằng tốc độ, tính hiệu quả, và độ chính xác sự hội tụ (Effective benchmarking balances speed, efficiency, and accuracy convergence).
12.7.2.1 Thời gian và thông lượng (Time and throughput)
Một của chính các số liệu cho việc đánh giá huấn luyện tính hiệu quả là thời gian được yêu cầu để đạt tới một được xác định trước
độ chính xác ngưỡng (One of the primary metrics for evaluating training efficiency is the time required to reach a predefined accuracy threshold). Huấn luyện thời gian (𝑇train) đo lường bao lâu một mô hình lấy để hội tụ tới một
có thể chấp nhận được hiệu suất cấp độ, việc phản ánh tổng thể tính toán tính hiệu quả của hệ thống (Training time (𝑇train) measures how long a model takes to converge to an acceptable performance level, reflecting the overall computational efficiency of the system). Gọi
Accuracy(𝑡) là mô hình’s độ chính xác tại huấn luyện thời gian 𝑡, và gọi mục tiêu độ chính xác là cụ thể-điểm chuẩn
ngưỡng (cho ví dụ, 75.9 phần trăm top-1 độ chính xác cho ResNet-50 trên ImageNet trong MLPerf) (Let Accuracy(𝑡) be the model’s accuracy at training time 𝑡, and let target accuracy be the benchmark-specific threshold (for example, 75.9 percent top-1 accuracy for ResNet-50 on ImageNet in MLPerf)).
Phương trình 12.1 một cách chính thức định nghĩa này số liệu, việc giữ điểm chuẩn được tập trung trên cách nào một cách nhanh chóng một hệ thống
đạt được có ý nghĩa các kết quả (Equation 12.1 formally defines this metric, keeping the benchmark focused on how quickly a system achieves meaningful results):
𝑇train = argmin𝑡{Accuracy(𝑡) ≥target accuracy}
(12.1)

670
12.7 Huấn luyện Các điểm chuẩn (Training Benchmarks)
Thông lượng22, thường được biểu diễn như số lượng của huấn luyện các mẫu được xử lý mỗi giây, cung cấp
một bổ sung sự đo lường của hệ thống hiệu suất (Throughput22, often expressed as the number of training samples processed per second, provides an additional measure of system performance). Gọi 𝑁samples là tổng số lượng của huấn luyện các mẫu
được xử lý và 𝑇train huấn luyện thời gian từ phương trình 12.1 (Let 𝑁samples be the total number of training samples processed and 𝑇train the training time from equation 12.1). Phương trình 12.2 cho thấy (Equation 12.2 shows):
Throughput =
𝑁samples
𝑇train
(12.2)
Thông lượng một mình không đảm bảo có ý nghĩa các kết quả, vì một mô hình có thể xử lý một lớn số lượng
của các mẫu một cách nhanh chóng mà không nhất thiết việc đạt tới mong muốn độ chính xác (Throughput alone does not guarantee meaningful results, as a model may process a large number of samples quickly without necessarily reaching the desired accuracy). Cho ví dụ, MLPerf Huấn luyện
quy định cụ thể-khối lượng công việc chất lượng các mục tiêu; một ResNet-50 kết quả trên ImageNet phải đạt tới một top-1
độ chính xác mục tiêu của 75.9 phần trăm để là hợp lệ (Mattson et al. 2020; MLCommons 2024c) (For example, MLPerf Training specifies workload-specific quality targets; a ResNet-50 result on ImageNet must reach a top-1 accuracy target of 75.9 percent to be valid (Mattson et al. 2020; MLCommons 2024c)). Một mang tính giả thuyết
hệ thống thứ mà xử lý nhiều các hình ảnh mỗi giây nhưng thất bại để đạt tới mục tiêu là không phải một hợp lệ điểm chuẩn
kết quả, trong khi một chậm hơn hệ thống thứ mà hội tụ một cách hiệu quả có thể được ưa thích hơn (A hypothetical system that processes many images per second but fails to reach the target is not a valid benchmark result, while a slower system that converges efficiently can be preferable). Này làm nổi bật tại sao
thông lượng nên được đánh giá trong sự liên quan tới thời gian-tới-độ chính xác thay vì như một độc lập
hiệu suất sự đo lường (This highlights why throughput should be evaluated in relation to time-to-accuracy rather than as an independent performance measure).
12.7.2.2 Khả năng mở rộng quy mô và sự song song (Scalability and parallelism)
Khả năng mở rộng quy mô đo lường cách nào một cách hiệu quả huấn luyện hiệu suất cải thiện khi các tài nguyên được thêm vào (Scalability measures how effectively training performance improves as resources are added). Một cách lý tưởng,
việc nhân đôi GPU số đếm nên giảm một nửa huấn luyện thời gian (Ideally, doubling GPU count should halve training time). Trong thực tế, giao tiếp chi phí chung, bộ nhớ
băng thông các giới hạn, và sự song song hóa các sự kém hiệu quả ràng buộc việc mở rộng quy mô thấp hơn tốt tuyến tính (In practice, communication overhead, memory bandwidth limits, and parallelization inefficiencies constrain scaling well below linear).
Khi việc huấn luyện lớn-quy mô các mô hình chẳng hạn như GPT-3, OpenAI đã tuyển dụng một lớn cụm của NVIDIA
V100 GPUs trong một được phân phối huấn luyện thiết lập (Brown et al. 2020; Patterson et al. 2021) (When training large-scale models such as GPT-3, OpenAI employed a large cluster of NVIDIA V100 GPUs in a distributed training setup (Brown et al. 2020; Patterson et al. 2021)). Google’s
TPU v4 các hệ thống chứng minh giống nhau được phân phối-các hệ thống bài học tại dữ liệu trung tâm quy mô: việc thêm
tính toán các tài nguyên cung cấp nhiều hơn thô điện năng, nhưng hiệu suất và tính đàn hồi (resiliency) phụ thuộc trên
mạng giao tiếp, cấu trúc (topology), và hoạt động sự quản lý (Jouppi et al. 2023; Zu et al.
2024) (Google’s TPU v4 systems demonstrate the same distributed-systems lesson at data center scale: adding computational resources provides more raw power, but performance and resiliency depend on network communication, topology, and operational management (Jouppi et al. 2023; Zu et al. 2024)). Các điểm chuẩn chẳng hạn như MLPerf định lượng cách nào tốt một hệ thống mở rộng quy mô qua nhiều các máy gia tốc,
việc cung cấp các sự thấu hiểu vào nơi các sự kém hiệu quả phát sinh trong được phân phối huấn luyện (Benchmarks such as MLPerf quantify how well a system scales across multiple accelerators, providing insights into where inefficiencies arise in distributed training).
Sự song song trong huấn luyện được phân loại thành dữ liệu sự song song, mô hình sự song song, và đường ống sự song-
song (xem Chương 8), mỗi (cái) việc trình bày khác biệt các thách thức (Parallelism in training is categorized into data parallelism, model parallelism, and pipeline parallelism (see Chapter 8), each presenting distinct challenges). Dữ liệu sự song song, phổ biến nhất
được sử dụng chiến lược, liên quan việc chia huấn luyện tập dữ liệu qua nhiều tính toán các nút (Data parallelism, the most commonly used strategy, involves splitting the training dataset across multiple compute nodes). Tính hiệu quả
của này cách tiếp cận phụ thuộc trên sự đồng bộ hóa các cơ chế và gradient giao tiếp chi phí chung (The efficiency of this approach depends on synchronization mechanisms and gradient communication overhead).
Ngược lại, mô hình sự song song phân vùng thần kinh mạng chính nó, việc yêu cầu hiệu quả sự phối hợp
giữa các bộ xử lý (In contrast, model parallelism partitions the neural network itself, requiring efficient coordination between processors). Các điểm chuẩn đánh giá cách nào tốt một hệ thống quản lý những sự song song các chiến lược này
mà không làm suy thoái độ chính xác sự hội tụ (Benchmarks evaluate how well a system manages these parallelism strategies without degrading accuracy convergence). Một then chốt số liệu cho việc đánh giá sự song song là việc mở rộng quy mô tính hiệu-
quả, thứ mà định lượng bao nhiêu của được thêm vào tính toán khả năng dịch thuật thành thực tế
sự tăng tốc (A key metric for evaluating parallelism is scaling efficiency, which quantifies how much of the added computational capacity translates into actual speedup).
Khăn ăn Toán học 12.3: Việc mở rộng quy mô tính hiệu quả sự tính toán (Napkin Math 12.3: Scaling efficiency calculation)
Vấn đề (Problem): Một nhóm huấn luyện ResNet-50 trên ImageNet. Đơn-GPU huấn luyện mất 24 các giờ (Single-GPU training takes 24 hours). Với 8
GPUs, huấn luyện mất 4 các giờ (With 8 GPUs, training takes 4 hours). Là này tốt việc mở rộng quy mô (Is this good scaling)? Nơi đã tính hiệu quả đi (Where did the efficiency go)?
Bước 1: Định nghĩa việc mở rộng quy mô tính hiệu quả (Step 1: Define scaling efficiency). Cho mạnh việc mở rộng quy mô (cố định vấn đề kích thước, nhiều hơn các bộ xử lý),
gọi 𝑇(1) là huấn luyện thời gian trên một đơn GPU, 𝑇(𝑁GPU) huấn luyện thời gian trên 𝑁GPU GPUs, và
𝑁GPU GPU số đếm (For strong scaling (fixed problem size, more processors), let 𝑇(1) be the training time on a single GPU, 𝑇(𝑁GPU) the training time on 𝑁GPU GPUs, and 𝑁GPU the GPU count). Phương trình 12.3 định nghĩa tính hiệu quả (Equation 12.3 defines efficiency):
Effscaling =
𝑇(1)
𝑁GPU ×𝑇(𝑁GPU) ×100%
(12.3)
Bước 2: Tính toán tính hiệu quả (Step 2: Calculate efficiency). Effscaling(8) =
24hours
8×4hours ×100% = 24/32 = 75 percent
Với hoàn hảo việc mở rộng quy mô, 8 GPUs sẽ hoàn thành trong 3 các giờ (24 các giờ/8 GPUs) (With perfect scaling, 8 GPUs would complete in 3 hours (24 hours/8 GPUs)). Thực tế 4 các giờ
đại diện cho 75 phần trăm tính hiệu quả (The actual 4 hours represents 75 percent efficiency).
Bước 3: Tính toán cho tính hiệu quả sự mất mát (Step 3: Account for the efficiency loss). Bảng 12.8 phân rã “bị thiếu” 25 phần trăm thành
có thể đo lường chi phí chung các danh mục—gradient sự đồng bộ hóa, bộ nhớ sao chép, tải sự mất cân bằng,
và lô-kích thước các hiệu ứng—mỗi (cái) có thể đo lường thông qua một khác biệt việc lập hồ sơ (profiling) tín hiệu (Table 12.8 decomposes the “missing” 25 percent into measurable overhead categories—gradient synchronization, memory copy, load imbalance, and batch-size effects—each measurable through a distinct profiling signal).

12. Việc đo điểm chuẩn (Benchmarking)
671
Bảng 12.8: Việc mở rộng quy mô Tính hiệu quả Sự mất mát Các nguồn (Scaling Efficiency Loss Sources): Mang tính minh họa sự phân rã của bị thiếu tính hiệu quả ngân sách thành có thể đo lường
chi phí chung các danh mục và tương ứng sự đo lường tín hiệu được sử dụng để quy kết mỗi sự mất mát (Illustrative decomposition of the missing efficiency budget into measurable overhead categories and the corresponding measurement signal used to attribute each loss). Thực tế các tỷ lệ phần trăm phụ thuộc
trên mô hình, liên kết mạng (interconnect), lưu trữ, lô lịch trình, và bộ khung sự triển khai (Actual percentages depend on model, interconnect, storage, batch schedule, and framework implementation).
Nguồn (Source)
Ví dụ Sự đóng góp (Example Contribution)
Sự đo lường (Measurement)
Gradient sự đồng bộ hóa (Gradient synchronization)
10-15%
AllReduce thời gian mỗi bước (AllReduce time per step)
Bộ nhớ sao chép (CPU฀GPU) (Memory copy (CPU฀GPU))
3-5%
Dữ liệu sự chuyển giao việc lập hồ sơ (Data transfer profiling)
Tải sự mất cân bằng (Load imbalance)
2-5%
Mỗi-GPU bước thời gian sự biến thiên (Per-GPU step time variance)
Lô kích thước các hiệu ứng (Batch size effects)
2-5%
Lớn hơn các lô hội tụ khác nhau (Larger batches converge differently)
Bước 4: Các hệ thống sự thấu hiểu (Step 4: The systems insight). Việc mở rộng quy mô tính hiệu quả giảm khi 𝑁GPU tăng trưởng bởi vì giao tiếp
chi phí chung mở rộng quy mô với GPU số đếm trong khi mỗi-GPU tính toán co lại (Scaling efficiency decreases as 𝑁GPU grows because communication overhead scales with GPU count while per-GPU compute shrinks). Trong này được làm việc ví dụ,
tám GPUs đạt tới 75 phần trăm tính hiệu quả; tại lớn hơn các quy mô, giống nhau số học làm cho rõ ràng tại sao
phức tạp giao tiếp và đầu vào-đường ống sự tối ưu hóa trở nên cần thiết (In this worked example, eight GPUs reach 75 percent efficiency; at larger scales, the same arithmetic makes clear why sophisticated communication and input-pipeline optimization become necessary).
MLPerf báo cáo cả hai thô hiệu suất và việc mở rộng quy mô tính hiệu quả cho này lý do: một hệ thống việc đạt được
2× thông lượng tại 50 phần trăm tính hiệu quả có thể tồi tệ hơn hơn 1.5× thông lượng tại 90 phần trăm
tính hiệu quả, phụ thuộc trên chi phí các sự ràng buộc (MLPerf reports both raw performance and scaling efficiency for this reason: a system achieving 2× throughput at 50 percent efficiency may be worse than 1.5× throughput at 90 percent efficiency, depending on cost constraints).
12.7.2.3 Tài nguyên sự sử dụng (Resource utilization)
Tính hiệu quả của máy học huấn luyện phụ thuộc không chỉ trên tốc độ và khả năng mở rộng quy mô mà cũng trên
cách nào tốt có sẵn phần cứng các tài nguyên được sử dụng (The efficiency of machine learning training depends not only on speed and scalability but also on how well available hardware resources are used). Tính toán sự sử dụng đo lường mức độ tới thứ mà
việc xử lý các đơn vị, chẳng hạn như các GPUs hay các TPUs, được một cách tích cực tham gia trong suốt huấn luyện (Compute utilization measures the extent to which processing units, such as GPUs or TPUs, are actively engaged during training). Thấp sự sử dụng có thể
chỉ ra các nút thắt cổ chai trong dữ liệu sự di chuyển, bộ nhớ sự truy cập, hay không hiệu quả khối lượng công việc việc lập lịch trình (Low utilization may indicate bottlenecks in data movement, memory access, or inefficient workload scheduling).
Cho ví dụ, khi việc huấn luyện BERT trên một TPU cụm, đầu vào-đường ống các sự kém hiệu quả có thể giới hạn tổng thể
thông lượng thậm chí khi các máy gia tốc có cao thô tính toán điện năng (For instance, when training BERT on a TPU cluster, input-pipeline inefficiencies can limit overall throughput even when the accelerators have high raw compute power). Nếu lưu trữ sự truy xuất (retrieval) hay
sự tiền xử lý không thể theo kịp, hệ thống thất bại để giữ các TPUs hoàn toàn bận rộn (If storage retrieval or preprocessing cannot keep up, the system fails to keep the TPUs fully busy). Việc lập hồ sơ (Profiling) tài nguyên
sự sử dụng xác định nút thắt cổ chai, và các sự tối ưu hóa chẳng hạn như việc tìm nạp trước (prefetching), việc lưu vào bộ nhớ đệm, và nhiều hơn
song song đầu vào việc xử lý có thể cải thiện được duy trì hiệu suất (Profiling resource utilization identifies the bottleneck, and optimizations such as prefetching, caching, and more parallel input processing can improve sustained performance).
Bộ nhớ băng thông là một khác then chốt yếu tố, vì sâu học tập các mô hình yêu cầu thường xuyên sự truy cập tới
lớn các khối lượng của dữ liệu trong suốt huấn luyện (Memory bandwidth is another critical factor, as deep learning models require frequent access to large volumes of data during training). Nếu bộ nhớ băng thông trở thành một giới hạn yếu tố, việc làm tăng
tính toán điện năng một mình sẽ không cải thiện huấn luyện tốc độ (If memory bandwidth becomes a limiting factor, increasing compute power alone will not improve training speed). Các điểm chuẩn đánh giá cách nào tốt các mô hình sử dụng
có sẵn bộ nhớ, việc đảm bảo rằng dữ liệu sự chuyển giao các tỷ lệ giữa lưu trữ, chính bộ nhớ, và việc xử lý
các đơn vị không trở thành hiệu suất các nút thắt cổ chai (Benchmarks assess how well models use available memory, ensuring that data transfer rates between storage, main memory, and processing units do not become performance bottlenecks).
I/O hiệu suất cũng đóng một trực tiếp vai trò trong huấn luyện tính hiệu quả, đặc biệt khi làm việc với
lớn các tập dữ liệu thứ mà không thể vừa vặn hoàn toàn trong bộ nhớ (I/O performance also plays a direct role in training efficiency, particularly when working with large datasets that cannot fit entirely in memory). Các điểm chuẩn đánh giá tính hiệu quả của dữ liệu việc tải
các đường ống, bao gồm sự tiền xử lý các hoạt động, việc lưu vào bộ nhớ đệm các cơ chế, và lưu trữ sự truy xuất các tốc độ (Benchmarks evaluate the efficiency of data loading pipelines, including preprocessing operations, caching mechanisms, and storage retrieval speeds).
Các hệ thống thứ mà thất bại để tối ưu hóa dữ liệu việc tải có thể trải nghiệm lớn các sự chậm lại, bất kể của tính-
toán điện năng (Systems that fail to optimize data loading can experience large slowdowns, regardless of computational power).
12.7.2.4 Năng lượng tính hiệu quả và chi phí (Energy efficiency and cost)
Việc huấn luyện lớn-quy mô máy học các mô hình yêu cầu đáng kể tính toán các tài nguyên, việc dẫn tới
tới đáng kể năng lượng sự tiêu thụ và tài chính các chi phí (Training large-scale machine learning models requires substantial computational resources, leading to considerable energy consumption and financial costs). Năng lượng tính hiệu quả các số liệu định lượng
điện năng sự sử dụng của huấn luyện các khối lượng công việc, việc giúp xác định các hệ thống thứ mà tối ưu hóa tính toán tính hiệu quả
trong khi việc giảm thiểu năng lượng sự lãng phí (Energy efficiency metrics quantify the power usage of training workloads, helping identify systems that optimize computational efficiency while minimizing energy waste). Ngày càng tăng sự tập trung trên tính bền vững đã dẫn tới sự bao gồm của
dựa trên-năng lượng các điểm chuẩn, chẳng hạn như những (cái) trong MLPerf Huấn luyện, thứ mà đo lường điện năng sự tiêu thụ
mỗi huấn luyện lượt chạy (The increasing focus on sustainability has led to the inclusion of energy-based benchmarks, such as those in MLPerf Training, which measure power consumption per training run). Giống nhau điện năng sự kế toán chi phối suy luận, nơi độ chính xác trở thành
thống trị năng lượng đòn bẩy; phần 12.9 làm việc thông qua tại sao INT8 sự lượng tử hóa cắt mỗi-suy luận năng lượng
bằng cách việc tấn công cả hai bộ nhớ lưu lượng và số học chi phí (The same power accounting governs inference, where precision becomes the dominant energy lever; section 12.9 works through why INT8 quantization cuts per-inference energy by attacking both memory traffic and arithmetic cost).
Việc huấn luyện GPT-3 đã được ước tính để tiêu thụ 1,287 MWh của điện (Patterson et al. 2021) (Training GPT-3 was estimated to consume 1,287 MWh of electricity (Patterson et al. 2021)). Nếu
một hệ thống có thể đạt được giống nhau độ chính xác với ít hơn huấn luyện các sự lặp lại (iterations), nó một cách trực tiếp giảm năng lượng
sự tiêu thụ (If a system can achieve the same accuracy with fewer training iterations, it directly reduces energy consumption). Nhận thức-năng lượng các điểm chuẩn giúp hướng dẫn sự phát triển của phần cứng và huấn luyện
các chiến lược thứ mà tối ưu hóa điện năng tính hiệu quả trong khi việc duy trì độ chính xác các mục tiêu (Energy-aware benchmarks help guide the development of hardware and training strategies that optimize power efficiency while maintaining accuracy targets).

672
12.7 Huấn luyện Các điểm chuẩn (Training Benchmarks)
Chi phí các sự xem xét mở rộng vượt ra ngoài điện năng sự sử dụng để bao gồm phần cứng các chi phí, đám mây tính-
toán các chi phí, và cơ sở hạ tầng sự bảo trì (Cost considerations extend beyond electricity usage to include hardware expenses, cloud computing costs, and infrastructure maintenance). Huấn luyện các điểm chuẩn cung cấp các sự thấu hiểu vào chi phí-
tính hiệu quả của khác nhau phần cứng và phần mềm các cấu hình bằng cách việc đo lường huấn luyện thời gian trong
sự liên quan tới tài nguyên sự chi tiêu (Training benchmarks provide insights into the cost-effectiveness of different hardware and software configurations by measuring training time in relation to resource expenditure). Các tổ chức có thể sử dụng những các điểm chuẩn này để cân bằng hiệu suất
và ngân sách các sự ràng buộc khi việc chọn huấn luyện cơ sở hạ tầng (Organizations can use these benchmarks to balance performance and budget constraints when selecting training infrastructure).
12.7.2.5 Lỗi dung sai và tính mạnh mẽ (Fault tolerance and robustness)
Huấn luyện các khối lượng công việc thường chạy cho kéo dài các khoảng thời gian, đôi khi việc kéo dài các ngày hay các tuần, việc làm cho
lỗi dung sai một thiết yếu sự xem xét (Training workloads often run for extended periods, sometimes spanning days or weeks, making fault tolerance an essential consideration). Một kiên cường (resilient) hệ thống phải xử lý không mong đợi các thất bại
(phần cứng các trục trặc, mạng các sự gián đoạn, và bộ nhớ các lỗi) mà không làm tổn hại độ chính xác
sự hội tụ (A resilient system must handle unexpected failures (hardware malfunctions, network disruptions, and memory errors) without compromising accuracy convergence).
Trong lớn-quy mô dựa trên-đám mây huấn luyện, nút các thất bại là một hoạt động thực tế (In large-scale cloud-based training, node failures are an operational reality). Nếu một GPU nút trong một
được phân phối cụm thất bại, huấn luyện phải tiếp tục mà không làm hỏng (corrupting) mô hình (If a GPU node in a distributed cluster fails, training must continue without corrupting the model). Sản xuất huấn luyện
các hệ thống sử dụng việc kiểm tra (checkpointing) cho lỗi dung sai, nơi các mô hình một cách định kỳ lưu của chúng tiến độ để mà
các thất bại không yêu cầu việc khởi động lại toàn bộ huấn luyện quá trình (Production training systems use checkpointing for fault tolerance, where models periodically save their progress so that failures do not require restarting the entire training process). Cho lớn ngôn ngữ mô hình huấn luyện,
tuy nhiên, việc kiểm tra là chính nó một các hệ thống nút thắt cổ chai: một đơn điểm kiểm tra phải ghi mô hình các trọng số
cộng bộ tối ưu hóa các trạng thái tới mạng lưu trữ, thứ mà tại 100-tỷ-tham số quy mô có thể có nghĩa là hàng trăm
của các gigabytes được ghi trước khi huấn luyện tiếp tục lại (For large language model training, however, checkpointing is itself a systems bottleneck: a single checkpoint must write model weights plus optimizer states to network storage, which at 100-billion-parameter scale can mean hundreds of gigabytes written before training resumes). Trong suốt đó ghi, các máy gia tốc có thể đình trệ (stall), việc làm suy thoái
thời gian-tới-độ chính xác bằng cách việc kéo dài hiệu quả sự lặp lại thời gian (During that write, accelerators can stall, degrading time-to-accuracy by extending the effective iteration time). Sản xuất LLM huấn luyện các hệ thống giải quyết
này bằng cách việc chồng chéo điểm kiểm tra I/O với tiếp theo huấn luyện bước (không đồng bộ việc kiểm tra) hay bằng cách
việc sử dụng cao-băng thông song song tệp các hệ thống thứ mà giảm nhàn rỗi thời gian (Production LLM training systems address this by overlapping checkpoint I/O with the next training step (asynchronous checkpointing) or by using high-bandwidth parallel file systems that reduce idle time). MLPerf Huấn luyện chính nó chủ yếu
đo lường thời gian-tới-chất lượng dưới được chuẩn hóa các khối lượng công việc và không đo điểm chuẩn thất bại sự phục hồi
một cách trực tiếp, nhưng điểm kiểm tra chi phí chung là một vật chất (material) thành phần của bất kỳ thực được duy trì-thông lượng số nào (MLPerf Training itself primarily measures time-to-quality under standardized workloads and does not benchmark failure recovery directly, but checkpoint overhead is a material component of any real sustained-throughput number).
12.7.2.6 Khả năng tái tạo và sự chuẩn hóa (Reproducibility and standardization)
Khả năng tái tạo các nghiên cứu đã lặp đi lặp lại chỉ ra rằng khiêm tốn điểm chuẩn các khoản đạt được có thể biến mất khi
ngẫu nhiên các hạt giống (seeds), phần cứng, bộ khung các phiên bản, hay sự triển khai các chi tiết thay đổi (Henderson et al.
2018) (Reproducibility studies have repeatedly shown that modest benchmark gains can disappear when random seeds, hardware, framework versions, or implementation details change (Henderson et al. 2018)). Này thất bại chế độ minh họa một lan tỏa (pervasive) vấn đề: huấn luyện các điểm chuẩn liên quan ngẫu nhiên (stochastic)
các quá trình (trọng số sự khởi tạo, dữ liệu việc xáo trộn, dropout các mặt nạ) thứ mà tương tác với cụ thể-phần cứng
các hành vi (dấu phẩy động việc làm tròn, bộ nhớ bố cục, trình biên dịch các sự tối ưu hóa) để tạo ra các kết quả thứ mà
có thể biến đổi một cách có ý nghĩa qua các môi trường (This failure mode illustrates a pervasive problem: training benchmarks involve stochastic processes (weight initialization, data shuffling, dropout masks) that interact with hardware-specific behaviors (floating-point rounding, memory layout, compiler optimizations) to produce results that can vary meaningfully across environments).
Một sâu hơn lớp của sự không-tất định (non-determinism) đến từ song song phần cứng chính nó (A deeper layer of non-determinism comes from the parallel hardware itself). Các hoạt động chẳng hạn như
song song nguyên tử (atomic) các sự bổ sung, được sử dụng trong suốt gradient sự tích lũy cho thưa thớt các nhúng trong các mô hình
giống như Đồ thị Thần kinh Các mạng (Graph Neural Networks), thực thi trong không-tất định thứ tự qua các luồng khi đồng thời
các cập nhật nhắm mục tiêu giống nhau bộ nhớ vị trí (Operations such as parallel atomic additions, used during gradient accumulation for sparse embeddings in models like Graph Neural Networks, execute in non-deterministic order across threads when concurrent updates target the same memory location). Kết quả dấu phẩy động sự tính tổng thứ tự thay đổi
qua các lượt chạy, việc tạo ra bit-đối với-bit khác nhau các gradients thậm chí với y hệt các đầu vào và các hạt giống (The resulting floating-point summation order changes across runs, producing bit-for-bit different gradients even with identical inputs and seeds). Việc thực thi
bit-chính xác khả năng tái tạo trong những các trường hợp này yêu cầu việc vô hiệu hóa song song sự tích lũy các đường dẫn, thứ mà
giảm huấn luyện thông lượng—một trực tiếp sự đánh đổi giữa khả năng tái tạo và hiệu suất thứ mà
điểm chuẩn các giao thức phải một cách rõ ràng giải quyết (Enforcing bit-exact reproducibility in these cases requires disabling the parallel accumulation paths, which reduces training throughput—a direct trade-off between reproducibility and performance that benchmark protocols must explicitly address). Mà không có rõ ràng các sự kiểm soát cho tất cả những các nguồn này của
sự biến thiên, điểm chuẩn các con số phản ánh một cụ thể sự hội tụ của các điều kiện thay vì một hệ thống’s
chân thực khả năng (Without explicit controls for all these sources of variability, benchmark numbers reflect a specific confluence of conditions rather than a system’s genuine capability).
MLPerf Huấn luyện giải quyết này bằng cách việc thực thi nghiêm ngặt khả năng tái tạo các yêu cầu: cố định ngẫu nhiên
các hạt giống, được chuẩn hóa dữ liệu sự tiền xử lý, và sự đệ trình các quy tắc thứ mà chứng minh kết quả tính ổn định
qua được chấp nhận các lượt chạy (Mattson et al. 2020) (MLPerf Training addresses this by enforcing strict reproducibility requirements: fixed random seeds, standardized data preprocessing, and submission rules that demonstrate result stability across accepted runs (Mattson et al. 2020)). Điểm là không đơn thuần để tạo ra một nhanh lượt chạy, mà để
chỉ ra rằng được báo cáo hiệu suất phản ánh hệ thống khả năng thay vì một thuận lợi sự kết hợp
của ngẫu nhiên (stochastic) các yếu tố (The point is not merely to produce a fast run, but to show that the reported performance reflects system capability rather than a favorable combination of stochastic factors).
Cho một huấn luyện điểm chuẩn, khả năng tái tạo là do đó đầy đủ lượt chạy vỏ bọc, không chỉ ngẫu nhiên
hạt giống (For a training benchmark, reproducibility is therefore the full run envelope, not just the random seed). Một đáng tin cậy báo cáo phải bảo tồn mô hình cam kết, tập dữ liệu tổng kiểm (checksum), sự tiền xử lý đường ống,
hạt giống kế hoạch, bộ khung và trình biên dịch các phiên bản, độ chính xác chính sách, lô lịch trình, phần cứng cấu trúc,
nhiệt và điện năng các giới hạn, và điểm kiểm tra hành vi (A credible report must preserve the model commit, dataset checksum, preprocessing pipeline, seed plan, framework and compiler versions, precision policy, batch schedule, hardware topology, thermal and power limits, and checkpoint behavior). Nó phải cũng báo cáo sự phân phối của được chấp nhận
các lượt chạy thay vì một đơn tốt nhất lượt chạy (It must also report the distribution of accepted runs rather than a single best run). Chỉ sau đó có thể điểm chuẩn tách biệt một thực hệ thống sự cải thiện
từ một thuận lợi sự tương tác giữa phần mềm phiên bản, phần cứng trạng thái, và ngẫu nhiên huấn luyện đường dẫn (Only then can the benchmark separate a real system improvement from a favorable interaction among software version, hardware state, and stochastic training path).
12.7.3 Huấn luyện hiệu suất sự đánh giá (Training performance evaluation)
Một toàn diện huấn luyện điểm chuẩn xem xét nhiều các chiều của hệ thống hành vi bởi vì
mỗi chiều xác định một khác nhau cách phần cứng khoản đầu tư có thể thất bại để trở thành sự hội tụ (A comprehensive training benchmark considers multiple dimensions of system behavior because each dimension identifies a different way hardware investment can fail to become convergence).

12. Việc đo điểm chuẩn (Benchmarking)
673
23
GPU
Boost
Xung nhịp (Clock):
Động tần số việc mở rộng quy mô
tăng các xung nhịp phía trên cơ sở khi
nhiệt và điện năng khoảng không
cho phép (Dynamic frequency scaling raises clocks above base when thermal and power headroom permit).
Việc đo điểm chuẩn
cạm bẫy (trap): ngắn điểm chuẩn các lượt chạy
có thể nắm bắt tăng-xung nhịp hiệu-
suất, nhưng được duy trì ML
huấn luyện có thể ổn định tới thấp hơn
ổn định-trạng thái các tần số khi
tiếp giáp nhiệt độ tăng (The benchmarking trap: short benchmark runs can capture boost-clock performance, but sustained ML training may settle to lower steady-state frequencies as junction temperature rises).
Việc báo cáo bùng nổ-giai đoạn các kết quả
nói quá
thông lượng
một sản xuất khối lượng công việc có thể
duy trì (Reporting burst-phase results overstates the throughput a production workload can sustain).
24
Nhiệt Sự điều tiết (Thermal Throttling): Tần-
số sự giảm được kích hoạt
khi tiếp giáp nhiệt độ vượt
quá an toàn các giới hạn (Frequency reduction triggered when junction temperature exceeds safe limits).
Cho biên
các thiết bị mà không có tích cực làm-
mát, sự điều tiết có thể bắt đầu trong-
suốt được duy trì suy luận, việc có nghĩa
rằng đỉnh thông lượng các con số
từ ngắn các điểm chuẩn có thể
trình bày sai ổn định-trạng thái hiệu-
suất (For edge devices without active cooling, throttling can begin during sustained inference, meaning peak throughput numbers from short benchmarks may misrepresent steady-state performance).
Bảng 12.9 tóm tắt cốt lõi các danh mục và liên quan các số liệu một cách phổ biến được sử dụng để đo điểm chuẩn
cấp độ-hệ thống huấn luyện hiệu suất, việc cung cấp một bộ khung cho việc hiểu cách nào huấn luyện các hệ thống
cư xử dưới khác nhau các khối lượng công việc và các cấu hình (Table 12.9 summarizes the core categories and associated metrics commonly used to benchmark system-level training performance, providing a framework for understanding how training systems behave under different workloads and configurations).
Bảng 12.9: Huấn luyện Điểm chuẩn Các chiều (Training Benchmark Dimensions): Then chốt các danh mục và các số liệu cho việc đánh giá máy học huấn luyện các hệ thống
vượt ra ngoài đơn giản tốc độ, việc bao phủ tài nguyên tính hiệu quả, khả năng tái tạo, và tổng thể hiệu suất các sự đánh đổi qua khác nhau huấn luyện
các cách tiếp cận và cơ sở hạ tầng các cấu hình (Key categories and metrics for evaluating machine learning training systems beyond simple speed, covering resource efficiency, reproducibility, and overall performance trade-offs across different training approaches and infrastructure configurations).
Danh mục (Category)
Then chốt Các số liệu (Key Metrics)
Ví dụ Điểm chuẩn Sử dụng (Example Benchmark Use)
Huấn luyện Thời gian và
Thông lượng (Training Time and Throughput)
Thời gian-tới-độ chính xác (các giây, các phút, các giờ); Thông lượng
(các mẫu/giây) (Time-to-accuracy (seconds, minutes, hours); Throughput (samples/sec))
Việc so sánh huấn luyện tốc độ qua
khác nhau GPU các kiến trúc (Comparing training speed across different GPU architectures)
Khả năng mở rộng quy mô và
Sự song song (Scalability and Parallelism)
Việc mở rộng quy mô tính hiệu quả (phần trăm của lý tưởng sự tăng tốc); Giao tiếp
chi phí chung (độ trễ, băng thông) (Scaling efficiency (percent of ideal speedup); Communication overhead (latency, bandwidth))
Việc phân tích được phân phối huấn luyện
hiệu suất cho lớn các mô hình (Analyzing distributed training performance for large models)
Tài nguyên Sự sử dụng (Resource Utilization)
Tính toán sự sử dụng (phần trăm GPU/TPU sử dụng); Bộ nhớ
băng thông (GB/s); I/O tính hiệu quả (dữ liệu việc tải tốc độ) (Compute utilization (percent GPU/TPU usage); Memory bandwidth (GB/s); I/O efficiency (data loading speed))
Việc tối ưu hóa dữ liệu các đường ống để
cải thiện GPU sự sử dụng (Optimizing data pipelines to improve GPU utilization)
Năng lượng Tính hiệu quả
và Chi phí (Energy Efficiency and Cost)
Năng lượng sự tiêu thụ mỗi lượt chạy (MWh, kWh); Huấn luyện
thông lượng mỗi watt (FLOP/s/W) (Energy consumption per run (MWh, kWh); Training throughput per watt (FLOP/s/W))
Việc đánh giá hiệu quả-năng lượng
huấn luyện các chiến lược (Evaluating energy-efficient training strategies)
Lỗi Dung sai và
Tính mạnh mẽ (Fault Tolerance and Robustness)
Điểm kiểm tra chi phí chung (thời gian mỗi lần lưu); Sự phục hồi thành công tỷ lệ
(phần trăm) (Checkpoint overhead (time per save); Recovery success rate (percent))
Việc đánh giá thất bại sự phục hồi trong
dựa trên-đám mây huấn luyện các hệ thống (Assessing failure recovery in cloud-based training systems)
Khả năng tái tạo và
Sự chuẩn hóa (Reproducibility and Standardization)
Sự biến thiên qua các lượt chạy (phần trăm sự khác biệt trong độ chính xác, huấn luyện
thời gian); Bộ khung tính nhất quán (TensorFlow so với PyTorch
so với JAX) (Variance across runs (percent difference in accuracy, training time); Framework consistency (TensorFlow vs. PyTorch vs. JAX))
Việc đảm bảo tính nhất quán trong
điểm chuẩn các kết quả qua
phần cứng (Ensuring consistency in benchmark results across hardware)
Các chiều trong bảng 12.9 tương tác trong các cách thứ mà các bảng không thể nắm bắt (The dimensions in table 12.9 interact in ways that tables cannot capture). Cao hơn thông lượng từ
được giảm độ chính xác (cho ví dụ, TF32) là vô nghĩa nếu nó làm tăng các sự lặp lại được yêu cầu để đạt tới
mục tiêu độ chính xác, việc làm cho thời gian-tới-độ chính xác thiết yếu mang tính khắc phục số liệu (Higher throughput from reduced precision (for example, TF32) is meaningless if it increases the iterations required to reach target accuracy, making time-to-accuracy the essential corrective metric). Việc mở rộng quy mô tính hiệu quả có thể trông
gần như tuyến tính tại nhỏ nút các số đếm nhưng thon dần (taper) khi gradient sự đồng bộ hóa các chi phí thống trị (Scaling efficiency can look nearly linear at small node counts but taper as gradient synchronization costs dominate). Tài nguyên
sự sử dụng các số liệu tiết lộ tại sao: một BERT tiền huấn luyện tác vụ với vừa phải GPU sự sử dụng có thể bị
nút thắt cổ chai bởi của nó dữ liệu đường ống, không phải của nó các máy gia tốc (Resource utilization metrics reveal why: a BERT pretraining task with moderate GPU utilization may be bottlenecked by its data pipeline, not its accelerators). Việc kiểm tra (Checkpointing) cho lỗi dung sai giới thiệu
của riêng nó chi phí chung, việc yêu cầu sự cân bằng giữa tính đàn hồi (resilience) và hiệu suất (Checkpointing for fault tolerance introduces its own overhead, requiring balance between resilience and performance).
Qua tất cả các chiều, sự đo lường độ chính xác phụ thuộc trên việc kiểm soát cho phần cứng sự biến thiên (Across all dimensions, measurement accuracy depends on controlling for hardware variability).
GPU boost xung nhịp23 hành vi và nhiệt sự điều tiết24 có thể dịch chuyển các kết quả đủ để làm ngập lụt (swamp) nhỏ được tuyên bố
các khoản đạt được, việc làm cho lặp lại các lượt chạy và thống kê sự nghiêm ngặt (như được thiết lập trước đó) thiết yếu cho việc phân biệt
chân thực hiệu suất các sự khác biệt từ nhiễu (GPU boost clock23 behavior and thermal throttling24 can shift results enough to swamp small claimed gains, making repeated runs and statistical rigor (as established earlier) essential for distinguishing genuine performance differences from noise).
Bất chấp sự có sẵn của được định nghĩa tốt việc đo điểm chuẩn các phương pháp luận, gây hiểu lầm các kết luận
lặp lại khi các nhóm xử lý một huấn luyện số liệu như một sự thay thế cho toàn bộ sự tối ưu hóa vòng lặp (Despite the availability of well-defined benchmarking methodologies, misleading conclusions recur when teams treat one training metric as a substitute for the whole optimization loop). Các
theo sau các cạm bẫy chỉ ra nơi điểm chuẩn phải giữ tốc độ, sự hội tụ, việc mở rộng quy mô, và khả năng tái-
tạo được buộc vào nhau (The following pitfalls show where the benchmark must keep speed, convergence, scaling, and reproducibility tied together).
Huấn luyện điểm chuẩn các thất bại thường bắt đầu khi thông lượng được xử lý như mục tiêu thay vì
như một phần của học tập quá trình (Training benchmark failures usually start when throughput is treated as the objective rather than as one part of the learning process). Một hệ thống có thể tăng các ví dụ mỗi giây bằng cách việc sử dụng thấp hơn
thuộc về số (numerical) độ chính xác, việc giảm sự đồng bộ hóa, hay thậm chí việc bỏ qua (bypassing) nhất định các tính toán, nhưng những
các thay đổi đó chỉ giúp nếu sự hội tụ được bảo tồn (A system can increase examples per second by using lower numerical precision, reducing synchronization, or even bypassing certain computations, but those changes only help if convergence is preserved). Một TF32 lượt chạy có thể vượt qua FP32 mỗi bước và vẫn
thua tổng thể nếu thuộc về số tính không ổn định làm tăng số lượng của các sự lặp lại được yêu cầu để đạt tới mục tiêu
độ chính xác (A TF32 run may outpace FP32 per step and still lose overall if numerical instability increases the number of iterations required to reach the target accuracy). Điểm chuẩn do đó phải báo cáo thông lượng trong sự liên quan tới thời gian-tới-độ chính xác, việc đảm bảo
rằng tốc độ các sự tối ưu hóa không đến tại chi phí của sự hội tụ tính hiệu quả (The benchmark therefore has to report throughput in relation to time-to-accuracy, ensuring that speed optimizations do not come at the expense of convergence efficiency).
Việc mở rộng quy mô tạo ra một thứ hai cạm bẫy bởi vì một nhỏ-nút kết quả có thể trông tuyến tính cho đến khi giao tiếp
và sự đồng bộ hóa thống trị (Scaling creates a second trap because a small-node result can look linear until communication and synchronization dominate). Trước đó tám-GPU sự tính toán cho thấy tại sao nhỏ-nút các kết quả
không thể được ngoại suy (extrapolated) một cách tuyến tính một khi sự đồng bộ hóa trở thành có tính ràng buộc thuật ngữ (The earlier eight-GPU calculation shows why small-node results cannot be extrapolated linearly once synchronization becomes the binding term).
Như diễn ra trước (preceding) việc mở rộng quy mô tính hiệu quả sự tính toán đã chứng minh (nơi 8 GPUs đạt được chỉ 75
phần trăm tính hiệu quả), việc ngoại suy đơn-nút các kết quả tới các cụm là một chung lỗi (As the preceding scaling efficiency calculation demonstrated (where 8 GPUs achieved only 75 percent efficiency), extrapolating single-node results to clusters is a common error). Google’s trải-
nghiệm với 4,096-nút TPU v4 các cụm cho thấy này hiệu ứng tại cực độ quy mô, nơi sự đồng bộ hóa
các thách thức trở thành thống trị hiệu suất yếu tố (Google’s experience with 4,096-node TPU v4 clusters shows this effect at extreme scale, where synchronization challenges become the dominant performance factor). Thích hợp việc đo điểm chuẩn nên đo lường việc mở rộng quy mô
tính hiệu quả một cách rõ ràng thay vì việc giả định tuyến tính sự cải thiện (Proper benchmarking should measure scaling efficiency explicitly rather than assuming linear improvement).
Giống nhau kỷ luật áp dụng tới các thất bại và sự can thiệp (interference) (The same discipline applies to failures and interference). Nhiều các điểm chuẩn giả định được lý tưởng hóa
các điều kiện nơi phần cứng các thất bại, mạng tính không ổn định, và khối lượng công việc sự can thiệp không xảy ra,
thậm chí mặc dù những các sự kiện đó là thường lệ tại quy mô (Many benchmarks assume idealized conditions where hardware failures, network instability, and workload interference do not occur, even though those events are routine at scale). Hiệu quả việc đo điểm chuẩn tính toán cho việc kiểm tra

674
12.8 Suy luận Các điểm chuẩn (Inference Benchmarks)
25
Edge TPU: Google’s
cố định-chức năng biên AI máy gia-
tốc (fixed-function edge AI accelerator).
Nó minh họa một
việc đo điểm chuẩn sự ràng buộc cụ-
thể tới cố định-chức năng các máy gia-
tốc (accelerators): của nó tiêu đề (headline) thông-
lượng áp dụng chỉ tới được lượng-
tử hóa TensorFlow Lite các mô-
hình với được hỗ trợ toán tử
các loại, do đó các mô hình việc yêu cầu không-
được hỗ trợ các toán tử rơi trở lại
tới máy chủ CPU hay cần đồ thị
các sự viết lại trước khi máy gia tốc
kết quả là có ý nghĩa (It illustrates a benchmarking constraint specific to fixed-function accelerators: its headline throughput applies only to quantized TensorFlow Lite models with supported operator types, so models requiring unsupported operators fall back to the host CPU or need graph rewrites before the accelerator result is meaningful).
chi phí chung, thất bại sự phục hồi tính hiệu quả, và tài nguyên sự tranh chấp thay vì việc báo cáo chỉ tốt nhất-trường hợp
hiệu suất (overhead, failure recovery efficiency, and resource contention rather than reporting only best-case performance).
Khả năng tái tạo thêm một khác biệt mối đe dọa (Reproducibility adds a different threat). Các kết quả phải tái tạo qua phần cứng và phần mềm
các ngăn xếp: một TensorFlow lượt chạy với Gia tốc Tuyến tính Đại số (Accelerated Linear Algebra) (XLA) các sự tối ưu hóa có thể thể hiện khác nhau
sự hội tụ hành vi hơn giống nhau mô hình được huấn luyện trong PyTorch với Tự động Hỗn hợp Độ chính xác
(Automatic Mixed Precision) (AMP), bởi vì dấu phẩy động số học, bộ nhớ các bố cục, và sự tối ưu hóa các chiến lược có thể tất cả dịch chuyển
huấn luyện thời gian và độ chính xác (Results must reproduce across hardware and software stacks: a TensorFlow run with Accelerated Linear Algebra (XLA) optimizations may exhibit different convergence behavior than the same model trained in PyTorch with Automatic Mixed Precision (AMP), because floating-point arithmetic, memory layouts, and optimization strategies can all shift training time and accuracy).
Việc tránh những các cạm bẫy này yêu cầu việc đánh giá thông lượng trong sự liên quan tới độ chính xác sự hội tụ, việc đánh-
giá việc mở rộng quy mô tính hiệu quả một cách tổng thể, và việc tính toán cho thực-thế giới các thất bại thay vì việc giả định
được lý tưởng hóa các điều kiện (Avoiding these pitfalls requires evaluating throughput in relation to accuracy convergence, assessing scaling efficiency holistically, and accounting for real-world failures rather than assuming idealized conditions). Một mô hình được huấn luyện một cách hiệu quả, tuy nhiên, vẫn yêu cầu sự xác nhận của của nó sự triển khai
hiệu suất, thứ mà dịch chuyển sự đánh giá bộ khung hoàn toàn (A model trained efficiently, however, still requires validation of its deployment performance, which shifts the evaluation framework entirely).
12.8 Suy luận Các điểm chuẩn (Inference Benchmarks)
Huấn luyện các điểm chuẩn đo lường cách nào một cách nhanh chóng một hệ thống học; suy luận các điểm chuẩn đo lường cách nào
một cách đáng tin cậy nó phục vụ (Training benchmarks measure how quickly a system learns; inference benchmarks measure how reliably it serves). Này sự dịch chuyển thay đổi gần như mọi khía cạnh của sự đánh giá (This shift changes nearly every aspect of evaluation). Huấn luyện dung thứ (tolerates) biến đổi
sự lặp lại các thời gian miễn là sự hội tụ tiếp tục; suy luận yêu cầu nhất quán độ trễ bởi vì người dùng
trải nghiệm mỗi chậm phản hồi (Training tolerates variable iteration times as long as convergence proceeds; inference requires consistent latency because users experience every slow response). Huấn luyện tối ưu hóa cho tổng hợp thông lượng qua các giờ; suy luận
phải xử lý không thể dự đoán được yêu cầu các mẫu với cấp độ-mili giây các đảm bảo (Training optimizes for aggregate throughput across hours; inference must handle unpredictable request patterns with millisecond-level guarantees). Huấn luyện chạy trên
chuyên dụng cao-hiệu suất phần cứng; suy luận kéo dài các môi trường từ dữ liệu trung tâm GPUs tới
di động điện thoại tới các vi điều khiển (Training runs on dedicated high-performance hardware; inference spans environments from data center GPUs to mobile phones to microcontrollers).
Này là nơi sự tối ưu hóa các chương hội tụ: được gia tốc phần cứng từ Chương 11 chạy
được nén các mô hình từ Chương 10 để phân phối thời gian-thực các dự đoán (This is where the optimization chapters converge: the accelerated hardware from Chapter 11 runs compressed models from Chapter 10 to deliver real-time predictions). Suy luận các điểm chuẩn tiết lộ
liệu những lý thuyết các sự tăng tốc đó trở thành thực tế độ trễ các sự giảm dưới thực tế sự triển khai
các điều kiện (Inference benchmarks reveal whether those theoretical speedups become actual latency reductions under realistic deployment conditions).
Định nghĩa 12.4: ML suy luận các điểm chuẩn (Definition 12.4: ML inference benchmarks)
ML Suy luận Các điểm chuẩn là máy học hệ thống các điểm chuẩn thứ mà định lượng hệ thống’s
khả năng để đáp ứng độ trễ các sự ràng buộc (𝐿lat) tại được quy định thông lượng các cấp độ, việc đo lường đuôi độ trễ
(p99), thông lượng (các truy vấn mỗi giây), và điện năng tính hiệu quả qua đại diện phục vụ
các kịch bản (ML Inference Benchmarks are machine learning system benchmarks that quantify the system’s ability to meet latency constraints (𝐿lat) at specified throughput levels, measuring tail latency (p99), throughput (queries per second), and power efficiency across representative serving scenarios).
1. Ý nghĩa (Significance): Suy luận các điểm chuẩn phơi bày khoảng cách giữa không bị ràng buộc thông lượng
và thông lượng trong khi việc đáp ứng một phục vụ-cấp độ mục tiêu (SLO), chẳng hạn như một p99 độ trễ mục tiêu (Inference benchmarks expose the gap between unconstrained throughput and throughput while meeting a service-level objective (SLO), such as a p99 latency target).
Một hệ thống’s đỉnh các truy vấn mỗi giây dưới không độ trễ sự ràng buộc (ngoại tuyến chế độ) có thể là
2–3× cao hơn hơn của nó bền vững tỷ lệ dưới một p99 độ trễ SLO (máy chủ chế độ), bởi vì
việc xếp hàng các sự trì hoãn đẩy đuôi độ trễ phía trên mục tiêu tại cao tải (A system’s peak queries per second under no latency constraint (offline mode) can be 2–3× higher than its sustainable rate under a p99 latency SLO (server mode), because queuing delays push tail latency above the target at high load). Này khoảng cách là vô hình
mà không có một điểm chuẩn thứ mà thực thi độ trễ các mục tiêu tại mỗi thông lượng cấp độ (This gap is invisible without a benchmark that enforces latency targets at each throughput level).
2. Sự phân biệt (Distinction): Không giống huấn luyện các điểm chuẩn, thứ mà đo lường thời gian-tới-độ chính xác qua một cố định
tập dữ liệu, suy luận các điểm chuẩn đo lường mỗi-truy vấn phản hồi thời gian dưới thực tế tải
các mẫu, việc nắm bắt việc xếp hàng các hiệu ứng, việc tạo lô các sự đánh đổi, và lạnh-khởi động chi phí chung thứ mà
xác định thực-thế giới phục vụ kinh tế học (Unlike training benchmarks, which measure time-to-accuracy over a fixed dataset, inference benchmarks measure per-query response time under realistic load patterns, capturing queuing effects, batching trade-offs, and cold-start overhead that determine real-world serving economics).
3. Chung cạm bẫy (Common pitfall): Một thường xuyên quan niệm sai lầm là rằng trung bình độ trễ là một đủ điểm-
chuẩn (A frequent misconception is that average latency is a sufficient benchmark). Một hệ thống với thấp trung bình độ trễ nhưng một dài p99 đuôi có thể vi phạm sản xuất SLOs
cho chậm nhất 1 phần trăm của các yêu cầu; tại cao yêu cầu các tỷ lệ, đó nhỏ tỷ lệ phần trăm trở thành
một lớn số lượng của bị ảnh hưởng người dùng (A system with low average latency but a long p99 tail can violate production SLOs for the slowest 1 percent of requests; at high request rates, that small percentage becomes a large number of affected users). Đuôi độ trễ là do đó về mặt hoạt động liên quan số liệu (Tail latency is therefore the operationally relevant metric).
12.8.1 Suy luận điểm chuẩn động lực (Inference benchmark motivation)
Không giống huấn luyện, thứ mà chạy trên chuyên dụng dữ liệu trung tâm phần cứng, suy luận phải được tối ưu hóa cho
một cách ấn tượng đa dạng sự triển khai các kịch bản—từ thời gian-thực các ứng dụng giống như tự trị lái xe
và hội thoại AI tới di động các thiết bị, IoT các hệ thống, và nhúng các bộ xử lý (Unlike training, which runs on dedicated data center hardware, inference must be optimized for dramatically diverse deployment scenarios—from real-time applications like autonomous driving and conversational AI to mobile devices, IoT systems, and embedded processors). Này sự đa dạng
mở rộng tới phần cứng: trong khi các GPUs và các TPUs thống trị huấn luyện, suy luận các khối lượng công việc thường yêu cầu
chuyên môn hóa các máy gia tốc giống như NPUs, FPGAs, và chuyên dụng suy luận các chip chẳng hạn như Google’s Edge
TPU25 (This diversity extends to hardware: while GPUs and TPUs dominate training, inference workloads often require specialized accelerators like NPUs, FPGAs, and dedicated inference chips such as Google’s Edge TPU25). Suy luận các điểm chuẩn đánh giá cách nào tốt phần cứng sự lựa chọn, mô hình sự tối ưu hóa, và dữ liệu (Inference benchmarks evaluate how well hardware selection, model optimization, and data)

12. Việc đo điểm chuẩn (Benchmarking)
675
đường ống thiết kế làm việc cùng nhau qua những sự triển khai các môi trường này (pipeline design work together across these deployment environments).
Việc mở rộng quy mô suy luận các khối lượng công việc qua đám mây các máy chủ, biên các nền tảng, di động các thiết bị, và TinyML
các hệ thống giới thiệu bổ sung sự phức tạp (Scaling inference workloads across cloud servers, edge platforms, mobile devices, and TinyML systems introduces additional complexity). Hình 12.6 tiết lộ sửng sốt điện năng sự tiêu thụ
các sự chênh lệch (differentials) giữa những các hệ thống này—việc kéo dài qua mười các cấp độ của độ lớn (orders of magnitude) từ các microwatts trong
nhỏ bé nhúng các thiết bị tới hàng trăm của các kilowatts trong dữ liệu trung tâm huấn luyện các cụm (Figure 12.6 reveals the staggering power consumption differentials among these systems—spanning over ten orders of magnitude from microwatts in tiny embedded devices to hundreds of kilowatts in data center training clusters). Các phạm vi là
đại diện thay vì toàn diện (The ranges are representative rather than exhaustive). Này sự trải rộng (spread) giải thích tại sao không (có) đơn điểm chuẩn (nào) có thể phục vụ tất cả
sự triển khai các ngữ cảnh: một số liệu có ý nghĩa cho dữ liệu trung tâm sự tối ưu hóa (các kilowatts mỗi giá đỡ (rack)) trở nên
không liên quan cho được cấp nguồn bằng pin biên các thiết bị (các milliwatts mỗi suy luận) (This spread explains why no single benchmark can serve all deployment contexts: a metric meaningful for data center optimization (kilowatts per rack) becomes irrelevant for battery-powered edge devices (milliwatts per inference)). Suy luận các điểm chuẩn phải
đánh giá các sự đánh đổi giữa độ trễ, chi phí, và năng lượng tính hiệu quả bên trong mỗi quy mô để hỗ trợ
các tổ chức trong việc thực hiện được thông báo sự triển khai các quyết định (Inference benchmarks must evaluate the trade-offs between latency, cost, and energy efficiency within each scale to assist organizations in making informed deployment decisions).
Nhỏ bé (Tiny)
Biên (Edge)
Dữ liệu trung tâm (Datacenter)
Huấn luyện (Training)
Hệ thống Loại (System Type)
10
4
10
2
100
102
104
106
Điện năng Sự tiêu thụ (W, Log Quy mô) (Power Consumption (W, Log Scale))
Tối thiểu Điện năng (Minimum Power)
Tối đa Điện năng (Maximum Power)
Hình 12.6: Điện năng Sự tiêu thụ Các sự chênh lệch (Power Consumption Differentials): Điện năng sự sử dụng kéo dài qua mười các cấp độ của độ lớn qua ML hệ thống các loại, từ
các microwatts trong tinyML các thiết bị thông qua các watts tại biên tới các kilowatts trong dữ liệu trung tâm suy luận và hàng trăm của các kilowatts cho
huấn luyện các cụm (Power usage spans over ten orders of magnitude across ML system types, from microwatts in tinyML devices through watts at the edge to kilowatts in data center inference and hundreds of kilowatts for training clusters). Các phạm vi là đại diện và biến đổi bởi phần cứng và khối lượng công việc (Ranges are representative and vary by hardware and workload).
Những sự triển khai các sự khác biệt này tạo ra thực tế động lực cho suy luận các điểm chuẩn: chúng
đánh giá các nút thắt cổ chai thứ mà nổi lên khi các mô hình chuyển đổi từ sự phát triển tới sản xuất
việc phục vụ (These deployment differences create the practical motivation for inference benchmarks: they evaluate the bottlenecks that emerge when models transition from development to production serving). Động lực các yếu tố song song (parallel) những (yếu tố) cho huấn luyện (phần cứng sự tối ưu hóa, khả năng mở rộng quy mô, chi phí,
công bằng sự so sánh) nhưng khác biệt trong các chi tiết cụ thể (The motivating factors parallel those for training (hardware optimization, scalability, cost, fair comparison) but differ in specifics). Phần mềm sự tối ưu hóa các bộ khung áp dụng cụ thể-suy luận
các kỹ thuật chẳng hạn như toán tử sự kết hợp (fusion) (xem Chương 10 và Chương 11), độ chính xác sự hiệu chuẩn, và
hạt nhân sự tinh chỉnh (tuning), mà của nó tác động trên độ trễ, thông lượng, và điện năng tính hiệu quả phải được đo lường dưới
thực tế các điều kiện để xác nhận chúng phân phối thực các sự cải thiện mà không làm suy thoái độ chính xác (Software optimization frameworks apply inference-specific techniques such as operator fusion (see Chapter 10 and Chapter 11), precision calibration, and kernel tuning, whose impact on latency, throughput, and power efficiency must be measured under realistic conditions to confirm they deliver real improvements without degrading accuracy). Tự động-
việc tinh chỉnh các trình biên dịch thêm một ẩn biến số: trình biên dịch chính nó có thể yêu cầu các giờ của sự tối ưu hóa mỗi
mô hình-phần cứng cặp, việc có nghĩa (rằng) điểm chuẩn các kết quả phản ánh sự tinh chỉnh ngân sách nhiều như phần cứng
khả năng, và việc so sánh các kết quả qua các sự đệ trình yêu cầu việc chuẩn hóa cho trình biên dịch sự tối ưu hóa
thời gian (Auto-tuning compilers add a hidden variable: the compiler itself can require hours of optimization per model-hardware pair, meaning benchmark results reflect the tuning budget as much as the hardware capability, and comparing results across submissions requires normalizing for compiler optimization time).
Khả năng mở rộng quy mô các mối quan tâm cũng dịch chuyển đặc tính (Scalability concerns also shift character). Huấn luyện mở rộng quy mô bằng cách việc thêm các GPUs để giảm thời gian-tới-
độ chính xác trên một cố định khối lượng công việc, trong khi đó suy luận phải mở rộng quy mô một cách động trong phản hồi tới việc dao động (fluctuating)
người dùng nhu cầu, việc xử lý lưu lượng các sự tăng vọt (spikes) mà không vi phạm độ trễ các đảm bảo (Training scales by adding GPUs to reduce time-to-accuracy on a fixed workload, whereas inference must scale dynamically in response to fluctuating user demand, handling traffic spikes without violating latency guarantees). Lạnh-khởi động hiệu suất,
thời gian được yêu cầu cho một mô hình để tải và bắt đầu việc xử lý các truy vấn, trở thành một khác biệt suy luận
mối quan tâm với không huấn luyện (điều) tương tự (Cold-start performance, the time required for a model to load and begin processing queries, becomes a distinct inference concern with no training analog). Các ứng dụng thứ mà tải các mô hình trên nhu cầu, chẳng hạn như không máy chủ AI
các sự triển khai, là đặc biệt nhạy cảm tới này chi phí chung (Applications that load models on demand, such as serverless AI deployments, are particularly sensitive to this overhead).
Chi phí và năng lượng hồ sơ của suy luận khác biệt một cách sắc nét từ huấn luyện (The cost and energy profile of inference differs sharply from training). Huấn luyện các chi phí được gánh chịu (incurred)
một lần và được khấu hao qua mô hình’s vòng đời, trong khi suy luận các chi phí tích lũy một cách liên tục khi
các mô hình phục vụ sản xuất lưu lượng (Training costs are incurred once and amortized over the model’s lifetime, while inference costs accumulate continuously as models serve production traffic). Việc chạy một không hiệu quả mô hình tại quy mô có thể nhân lên đám mây tính-toán
các chi phí, và trên được cấp nguồn bằng pin các thiết bị, quá mức tính toán một cách trực tiếp tác động tính khả dụng (Running an inefficient model at scale can multiply cloud compute expenses, and on battery-powered devices, excessive computation directly impacts usability). Các điểm-
chuẩn thứ mà đo lường chi phí mỗi suy luận yêu cầu và tính hiệu quả mỗi watt giúp các tổ chức tối ưu hóa
cho cả hai hiệu suất và tính bền vững qua sự triển khai các nền tảng (Benchmarks that measure cost per inference request and efficiency per watt help organizations optimize for both performance and sustainability across deployment platforms).

676
12.8 Suy luận Các điểm chuẩn (Inference Benchmarks)
26
Đuôi Độ trễ (Tail Latency): Thứ 95 hay
thứ 99 phân vị phản hồi thời gian,
thứ mà xác định sản xuất
SLA sự tuân thủ (The 95th or 99th percentile response time, which determines production SLA compliance). Dean và
Barroso (2013) đã chỉ ra rằng
trong quạt-ra (fan-out) các kiến trúc (phổ-
biến trong sự giới thiệu các hệ-
thống), thậm chí 1 phần trăm chậm các phản-
hồi kết hợp (compound): một yêu cầu
việc chạm 100 phụ trợ (backend) các mảnh (shards)
có một 63 phần trăm cơ hội rằng tại
ít nhất một mảnh chạm của nó 1 phần-
trăm đuôi, việc làm cho p99 độ trễ
hiệu quả trung bình (Dean and Barroso (2013) showed that in fan-out architectures (common in recommendation systems), even 1 percent slow responses compound: a request touching 100 backend shards has a 63 percent chance that at least one shard hits its 1 percent tail, making p99 latency the effective average). Các điểm-
chuẩn việc báo cáo chỉ trung bình độ-
trễ che giấu này thất bại chế độ (Benchmarks reporting only mean latency hide this failure mode).
MLPerf Suy luận mở rộng được chuẩn hóa sự so sánh các nguyên tắc được thiết lập cho huấn luyện các điểm-
chuẩn tới sự triển khai các kịch bản, việc định nghĩa sự đánh giá các tiêu chí cho các tác vụ chẳng hạn như hình ảnh phân loại,
đối tượng sự phát hiện, và lời nói sự nhận dạng qua khác nhau phần cứng các nền tảng (MLPerf Inference extends the standardized comparison principles established for training benchmarks to deployment scenarios, defining evaluation criteria for tasks such as image classification, object detection, and speech recognition across different hardware platforms). Này đảm bảo rằng
suy luận hiệu suất các sự so sánh duy trì có ý nghĩa và có thể tái tạo trong khi việc tính toán cho
cụ thể-sự triển khai các sự ràng buộc giống như độ trễ các yêu cầu và năng lượng tính hiệu quả (Reddi et al. 2019) (This ensures that inference performance comparisons remain meaningful and reproducible while accounting for deployment-specific constraints like latency requirements and energy efficiency (Reddi et al. 2019)).
12.8.2 Suy luận các số liệu (Inference metrics)
Cho ví dụ, một giọng nói trợ lý phải phản hồi đủ nhanh (để) rằng người dùng không cảm nhận (perceive) sự trễ (lag), trong khi
một sự giới thiệu động cơ phải chấm điểm đủ các ứng viên để giữ nhịp độ (pace) với người dùng việc cuộn (scrolling) (For example, a voice assistant must respond quickly enough that users do not perceive lag, while a recommendation engine must score enough candidates to keep pace with user scrolling). Những
các sự ràng buộc này (độ trễ và thông lượng) định nghĩa hiệu suất vỏ bọc bên trong thứ mà tất cả việc phục vụ
các sự tối ưu hóa phải hoạt động (These constraints (latency and throughput) define the performance envelope within which all serving optimizations must operate). Suy luận các số liệu chính thức hóa những thực-thế giới các đòi hỏi này thành có thể đo lường
các đại lượng, và chúng khác biệt từ huấn luyện các số liệu trong loại, không chỉ mức độ, bởi vì sự tối ưu hóa
mục tiêu chuyển dịch từ “cách nào nhanh chúng ta có thể học?” tới “cách nào một cách đáng tin cậy chúng ta có thể phục vụ?” (Inference metrics formalize these real-world demands into measurable quantities, and they differ from training metrics in kind, not just degree, because the optimization target shifts from “how fast can we learn?” to “how reliably can we serve?”) Huấn luyện quan tâm về
thông lượng và thời gian-tới-độ chính xác; suy luận quan tâm về độ trễ tính nhất quán, tài nguyên tính hiệu quả, và
sự triển khai tính thực tiễn, việc kéo dài đám mây dữ liệu các trung tâm việc xử lý hàng triệu của các yêu cầu tới biên các thiết bị
việc hoạt động dưới nghiêm ngặt điện năng các sự ràng buộc (Training cares about throughput and time-to-accuracy; inference cares about latency consistency, resource efficiency, and deployment practicality, spanning cloud data centers handling millions of requests to edge devices operating under strict power constraints).
12.8.2.1 Độ trễ và đuôi độ trễ (Latency and tail latency)
Độ trễ (được giới thiệu trong Chương 2) đo lường thời gian cho một suy luận hệ thống để xử lý một đầu vào
và tạo ra một dự đoán (Latency (introduced in Chapter 2) measures the time for an inference system to process an input and produce a prediction). Trung bình độ trễ là hữu ích, nhưng nó không nắm bắt tồi tệ nhất-trường hợp các sự trì hoãn thứ mà
làm suy thoái độ tin cậy trong cao-nhu cầu các kịch bản (Average latency is useful, but it does not capture worst-case delays that degrade reliability in high-demand scenarios).
Để tính toán cho này, các điểm chuẩn thường đo lường đuôi độ trễ26, thứ mà phản ánh tồi tệ nhất-trường hợp các sự trì hoãn
trong một hệ thống (To account for this, benchmarks often measure tail latency26, which reflects the worst-case delays in a system). Những (cái) này là một cách điển hình được báo cáo như thứ 95 phân vị (p95) hay thứ 99 phân vị (p99)
độ trễ, việc có nghĩa rằng 95 phần trăm hay 99 phần trăm của các suy luận được hoàn thành bên trong một được cho thời gian (These are typically reported as the 95th percentile (p95) or 99th percentile (p99) latency, meaning that 95 percent or 99 percent of inferences are completed within a given time).
Cho các ứng dụng chẳng hạn như tự trị lái xe hay thời gian-thực giao dịch (trading), việc duy trì thấp đuôi độ trễ là
thiết yếu để tránh không thể dự đoán được các sự trì hoãn thứ mà có thể dẫn tới tới thảm khốc (catastrophic) các kết quả (For applications such as autonomous driving or real-time trading, maintaining low tail latency is essential to avoid unpredictable delays that could lead to catastrophic outcomes).
Những các sự đo lường này hình thành cơ sở cho Phục vụ Cấp độ Các mục tiêu (Service Level Objectives) (SLOs) và Phục vụ Cấp độ Các thỏa-
thuận (Service Level Agreements) (SLAs), thứ mà chính thức hóa hiệu suất các kỳ vọng (These measurements form the basis for Service Level Objectives (SLOs) and Service Level Agreements (SLAs), which formalize performance expectations).
Định nghĩa 12.5: SLOs và SLAs (Definition 12.5: SLOs and SLAs)
SLOs và SLAs là hiệu suất sự cam kết các thông số kỹ thuật cho sản xuất ML việc phục vụ các hệ thống (SLOs and SLAs are performance commitment specifications for production ML serving systems):
một Phục vụ Cấp độ Mục tiêu (SLO) là nội bộ kỹ thuật mục tiêu thứ mà nhóm tối ưu hóa hướng tới,
trong khi một Phục vụ Cấp độ Thỏa thuận (SLA) là bên ngoài thuộc về hợp đồng ngưỡng mà của nó sự vi phạm
kích hoạt tài chính các hình phạt (a Service Level Objective (SLO) is the internal engineering target that the team optimizes toward, while a Service Level Agreement (SLA) is the external contractual threshold whose breach triggers financial penalties).
1. Ý nghĩa (Significance): SLOs một cách trực tiếp ràng buộc 𝐿lat thuật ngữ trong sắt định luật bằng cách việc thiết lập một cứng
độ trễ trần (ceiling) thứ mà việc phục vụ hệ thống phải đáp ứng tại một được cho phân vị (SLOs directly constrain the 𝐿lat term in the iron law by setting a hard latency ceiling that the serving system must satisfy at a given percentile). Một đại diện
sản xuất thiết lập có thể thiết lập nội bộ SLO chặt chẽ hơn hơn bên ngoài SLA, việc để lại
khoảng không thứ mà có chức năng như một lỗi ngân sách cho thoáng qua (transient) các sự tăng vọt, sự bảo trì các cửa sổ,
và xếp tầng các thất bại (A representative production setup might set the internal SLO tighter than the external SLA, leaving headroom that functions as an error budget for transient spikes, maintenance windows, and cascading failures).
2. Sự phân biệt (Distinction): Một SLO bị vi phạm một cách nội bộ (việc kích hoạt một nhắn tin (paging) cảnh báo và một kỹ thuật
phản hồi), trong khi một SLA sự vi phạm là một hợp đồng sự vi phạm (việc kích hoạt khách hàng các khoản tín dụng hay
các hình phạt) (An SLO is violated internally (triggering a paging alert and an engineering response), while an SLA breach is a contract violation (triggering customer credits or penalties)). SLO phải chặtẽ hơn hơn SLA; việc thiết lập chúng bằng (nhau) để lại không khoảng không
cho sự đo lường sự biến thiên, triển khai các cửa sổ, hay sự cố (incident) phản hồi thời gian (The SLO must be tighter than the SLA; setting them equal leaves no headroom for measurement variance, deploy windows, or incident response time).
3. Chung cạm bẫy (Common pitfall): Một thường xuyên quan niệm sai lầm là rằng việc đáp ứng trung bình độ trễ đáp ứng một
SLO (A frequent misconception is that meeting average latency satisfies an SLO). SLOs được định nghĩa tại đuôi các phân vị (p99, p99.9), không phải các giá trị trung bình (SLOs are defined at tail percentiles (p99, p99.9), not means). Một hệ thống có thể có một
xuất sắc giá trị trung bình trong khi vẫn việc vi phạm của nó đuôi-độ trễ sự cam kết cho chậm nhất các yêu cầu (A system can have an excellent mean while still violating its tail-latency commitment for the slowest requests).
Sự phân biệt quan trọng trong thực tế: kỹ thuật các nhóm tối ưu hóa hướng tới SLOs trong khi kinh doanh
cam kết tới SLAs (The distinction matters in practice: engineering teams optimize toward SLOs while the business commits to SLAs). Việc chọn sai số liệu để tối ưu hóa lãng phí kỹ thuật nỗ lực hay vi phạm
khách hàng các đảm bảo (Choosing the wrong metric to optimize wastes engineering effort or violates customer guarantees).
Đuôi độ trễ’s sự kết nối tới người dùng trải nghiệm tại quy mô trở nên then chốt trong sản xuất các hệ thống việc phục vụ
hàng triệu của người dùng (Tail latency’s connection to user experience at scale becomes critical in production systems serving millions of users). Thậm chí nhỏ P99 độ trễ các sự suy thoái tạo ra việc kết hợp (compounding) các hiệu ứng qua lớn người dùng
các cơ sở: nếu 1 phần trăm của các yêu cầu trải nghiệm 10× độ trễ (cho ví dụ, 1000 ms thay vì 100 ms), này

12. Việc đo điểm chuẩn (Benchmarking)
677
ảnh hưởng 10,000 người dùng mỗi triệu các yêu cầu, một cách tiềm năng việc dẫn tới tới hết thời gian (timeout) các lỗi, tồi tệ người dùng trải nghiệm,
và khách hàng sự rời bỏ (churn) (affects 10,000 users per million requests, potentially leading to timeout errors, poor user experience, and customer churn). Tìm kiếm các động cơ và sự giới thiệu các hệ thống chứng minh này sự nhạy cảm:
Google’s tìm kiếm-độ trễ các thí nghiệm đã tìm thấy có thể đo lường các sự giảm trong hàng ngày các tìm kiếm mỗi người dùng sau
100–400 ms phía-máy chủ các sự trì hoãn (Brutlag 2009), thứ mà là tại sao tương tác các dịch vụ thường xử lý dưới-100
ms phản hồi các thời gian như một thực tế thiết kế mục tiêu (Search engines and recommendation systems demonstrate this sensitivity: Google’s search-latency experiments found measurable reductions in daily searches per user after 100–400 ms server-side delays (Brutlag 2009), which is why interactive services often treat sub-100 ms response times as a practical design target).
Điểm kiểm tra (Checkpoint) 12.2: Số liệu sự lựa chọn (Metric selection)
Số liệu định hình sự tối ưu hóa (The metric shapes the optimization).
Áp dụng ba các quy tắc trước khi việc hoàn thiện của bạn số liệu sự lựa chọn (Apply three rules before finalizing your metric selection):
□Thông lượng so với độ trễ (Throughput vs. latency): Quyết định liệu khối lượng công việc tối ưu hóa cho chi phí hay người dùng trải-
nghiệm, sau đó gọi tên số liệu điểm chuẩn phải giữ cố định (Decide whether the workload optimizes for cost or user experience, then name the metric the benchmark must hold fixed).
□Đuôi độ trễ (Tail latency): Nêu cái gì p99 phơi bày (mà) trung bình độ trễ che giấu (State what p99 exposes that mean latency hides).
□Đầu-tới-đầu (End-to-end): Liệt kê sự tiền xử lý, mô hình sự thực thi, và hậu xử lý các giai đoạn được bao gồm
trong được báo cáo độ trễ (List the preprocessing, model execution, and postprocessing stages included in the reported latency).
Phục vụ cấp độ các mục tiêu (SLOs) trong sản xuất các hệ thống do đó tập trung trên đuôi độ trễ thay vì
trung bình độ trễ để đảm bảo nhất quán người dùng trải nghiệm (Service level objectives (SLOs) in production systems therefore focus on tail latency rather than mean latency to ensure consistent user experience). Tương tác các dịch vụ thường định nghĩa dựa trên-
phân vị độ trễ các mục tiêu bởi vì thỉnh thoảng chậm các phản hồi có không cân xứng tác động trên người dùng
sự hài lòng (Interactive services often define percentile-based latency objectives because occasional slow responses have disproportionate impact on user satisfaction). Lớn-quy mô các hệ thống có thể theo dõi thậm chí sâu hơn các đuôi, chẳng hạn như p99.9, khi lưu lượng các sự tăng vọt (spikes) và
cơ sở hạ tầng sự biến thiên ảnh hưởng độ tin cậy (Large-scale systems may track even deeper tails, such as p99.9, when traffic spikes and infrastructure variation affect reliability).
Thách thức của việc đáp ứng những đuôi độ trễ các mục tiêu này là rằng nguồn của đuôi là thường mang tính kiến trúc,
không phải mang tính thuật toán (The challenge of meeting these tail latency targets is that the source of the tail is often architectural, not algorithmic). Một được thu gom-rác (garbage-collected) thời gian chạy, một được chia sẻ hạt nhân trình điều khiển, hay một ưu tiên-đảo ngược (priority-inversion) lỗi trong
việc phục vụ ngăn xếp có thể tiêm độ trễ các sự tăng vọt thứ mà không (có) mô hình sự tối ưu hóa (nào) sẽ loại bỏ (A garbage-collected runtime, a shared kernel driver, or a priority-inversion bug in the serving stack can inject latency spikes that no model optimization will remove).
Chiến tranh Câu chuyện (War Story) 12.1: Đuôi độ trễ cái chết (The tail latency death)
Ngữ cảnh (Context): Discord, một thời gian-thực trò chuyện nền tảng việc hỗ trợ hàng triệu của đồng thời người dùng, ban đầu
đã triển khai của nó Đọc Các trạng thái (Read States) dịch vụ trong Go (Discord, a real-time chat platform supporting millions of concurrent users, originally implemented its Read States service in Go). Dịch vụ theo dõi cái nào các kênh và các tin nhắn
mỗi người dùng đã đọc và được truy cập trên mọi kết nối, mọi tin nhắn được gửi, và mọi đọc
sự kiện, việc làm cho nó một của nền tảng’s nóng nhất dữ liệu các đường dẫn (Howarth 2020) (The service tracks which channels and messages each user has read and is accessed on every connection, every message sent, and every read event, making it one of the platform’s hottest data paths (Howarth 2020)).
Thất bại chế độ (Failure mode): Các kỹ sư đã quan sát độ trễ các sự tăng vọt mỗi hai phút thứ mà đã khớp Go’s bị ép buộc
tối thiểu rác-sự thu gom khoảng thời gian (Engineers observed latency spikes every two minutes that matched Go’s forced minimum garbage-collection interval). LRU bộ nhớ đệm đã giữ hàng chục của hàng triệu của Đọc Các trạng thái qua
hàng triệu của người dùng với hàng trăm của hàng ngàn của các cập nhật mỗi giây, do đó mọi “dừng-thế giới” (stop-the-world)
GC lượt chạy đã phải quét một khổng lồ heap (The LRU cache held tens of millions of Read States across millions of users with hundreds of thousands of updates per second, so every “stop-the-world” GC pass had to scan an enormous heap). Việc tinh chỉnh GC Phần trăm (Percent) cài đặt và việc phân vùng
bộ nhớ đệm qua các máy chủ đã tạo ra không sự khác biệt: các sự tăng vọt là mang tính cấu trúc, không phải có thể cấu hình (Tuning the GC Percent setting and partitioning the cache across servers made no difference: the spikes were structural, not configurable).
Sự giải quyết (Resolution): Trong 2019, Discord đã viết lại Đọc Các trạng thái trong Rust, thứ mà có không rác bộ thu gom (In 2019, Discord rewrote Read States in Rust, which has no garbage collector).
Trung bình phản hồi thời gian đã giảm từ các mili giây tới các micro giây, và định kỳ độ trễ
các sự tăng vọt đã biến mất (Average response time dropped from milliseconds to microseconds, and the periodic latency spikes disappeared).
Các hệ thống bài học (Systems lesson): Trung bình độ trễ là một sự phù phiếm (vanity) số liệu; đuôi độ trễ là người dùng trải nghiệm (Average latency is a vanity metric; tail latency is the user experience). Ngôn ngữ-
thời gian chạy các sự lựa chọn (được quản lý GC so với dựa trên-quyền sở hữu bộ nhớ sự quản lý) thiết lập một sàn trên
đuôi thứ mà không lượng của sự tinh chỉnh có thể hạ thấp (Language-runtime choices (managed GC vs. ownership-based memory management) set a floor on the tail that no amount of tuning can lower). Này thất bại chế độ là một cách mang tính cấu trúc được nhúng trong ML
việc phục vụ các ngăn xếp: đặc trưng các cửa hàng (feature stores) thứ mà phục vụ thời gian-thực các nhúng cho phong cách-DLRM sự giới thiệu
các mô hình là một cách phổ biến được triển khai trong Java hay Go, và của chúng rác-bộ thu gom các sự tạm dừng thổi phồng (inflate)
p99 độ trễ của mọi hạ nguồn (downstream) suy luận yêu cầu thứ mà chờ đợi cho một được truy xuất nhúng (This failure mode is structurally embedded in ML serving stacks: feature stores that serve real-time embeddings for DLRM-style recommendation models are commonly implemented in Java or Go, and their garbage-collector pauses inflate the p99 latency of every downstream inference request that waits for a retrieved embedding).
Không mô hình sự tối ưu hóa đóng khoảng cách đó, bởi vì nút thắt cổ chai là trong sự truy xuất đường dẫn, không phải
mô hình chính nó (No model optimization closes that gap, because the bottleneck is in the retrieval path, not the model itself). Discord sự cố (incident) là rõ ràng nhất được tài liệu hóa ví dụ của này cơ chế: một
được quản lý-thời gian chạy GC sự tạm dừng định nghĩa đuôi một cách quyết định cho một ML suy luận đường ống như
nó đã (làm) cho một trò chuyện dịch vụ (The Discord incident is the clearest documented example of this mechanism: a managed-runtime GC pause defines the tail just as decisively for an ML inference pipeline as it did for a chat service).
12.8.2.2 Đầu-tới-đầu so với thành phần độ trễ (End-to-end vs. component latency)
Một then chốt sự phân biệt trong suy luận việc đo điểm chuẩn là giữa thành phần độ trễ (thời gian được dành trong mô hình
tính toán) và đầu-tới-đầu độ trễ (tổng thời gian từ yêu cầu sự đến tới phản hồi sự phân phối) (A critical distinction in inference benchmarking is between component latency (time spent in model computation) and end-to-end latency (total time from request arrival to response delivery)). Nhiều

678
12.8 Suy luận Các điểm chuẩn (Inference Benchmarks)
các điểm chuẩn báo cáo chỉ mô hình suy luận thời gian, việc làm mờ đi (obscuring) phần còn lại chi phí chung thứ mà xác định
thực tế người dùng trải nghiệm (benchmarks report only model inference time, obscuring the remaining overhead that determines actual user experience). Chi phí chung là không bên lề (marginal): sự tuần tự hóa (serialization), mạng các bước nhảy (hops), và hàng đợi chờ
thời gian có thể thống trị tổng yêu cầu thời gian, việc làm cho chỉ-mô hình các sự tối ưu hóa mang lại (yield) việc giảm dần các khoản lợi nhuận (The overhead is not marginal: serialization, network hops, and queue wait time can dominate total request time, making model-only optimizations yield diminishing returns).
Ví dụ 12.4: JSON sự tuần tự hóa cạm bẫy (The JSON serialization trap)
Kịch bản (Scenario): Các nhà nghiên cứu tại Berkeley đã phát triển Clipper, một thấp-độ trễ mô hình việc phục vụ hệ thống (Researchers at Berkeley developed Clipper, a low-latency model serving system).
Của họ sự đánh giá đã làm nổi bật rằng dự đoán việc phục vụ chi phí chung có thể thống trị đơn giản các mô hình (Their evaluation highlighted that prediction serving overhead can dominate simple models).
Thất bại chế độ (Failure mode): Cho đơn giản các mô hình giống như tuyến tính hồi quy hay nhỏ tích chập thần kinh các mạng
(CNNs), API chi phí chung từ sự tuần tự hóa, sự giải tuần tự hóa, và ngôn ngữ/thời gian chạy các ranh giới
có thể tiêu thụ nhiều hơn CPU thời gian hơn thực tế suy luận (For simple models like linear regression or small convolutional neural networks (CNNs), API overhead from serialization, deserialization, and language/runtime boundaries can consume more CPU time than the actual inference). Hệ thống’s thông lượng đã bị giới hạn (capped)
không phải bởi mô hình’s toán học, mà bởi văn bản việc xử lý của đầu vào dữ liệu (The system’s throughput was capped not by the model’s math, but by the text processing of the input data). GPU đã ngồi nhàn rỗi trong khi
CPU đã phân tích cú pháp JSON các chuỗi (The GPU sat idle while the CPU parsed JSON strings).
Các hệ thống sự thấu hiểu (Systems insight): Văn bản các giao thức (JSON/HTTP) là bị giới hạn-CPU các nút thắt cổ chai cho cao-thông lượng
ML (Text protocols (JSON/HTTP) are CPU-bound bottlenecks for high-throughput ML). Nhị phân các giao thức chẳng hạn như gRPC qua Protobuf giảm việc phân tích cú pháp chi phí chung bằng cách việc gửi nhỏ gọn
được định kiểu các tin nhắn, trong khi được chia sẻ-bộ nhớ các định dạng chẳng hạn như Apache Arrow tránh lặp lại sự tuần-
tự hóa khi các quá trình chạy trên giống nhau máy chủ (Binary protocols such as gRPC over Protobuf reduce parsing overhead by sending compact typed messages, while shared-memory formats such as Apache Arrow avoid repeated serialization when processes run on the same host). Cho cao-hiệu suất việc phục vụ, “vỏ bọc” (wrapper)
thường có giá (costs) nhiều hơn hơn “món quà” (gift) (Crankshaw et al. 2017) (For high-performance serving, the “wrapper” often costs more than the “gift” (Crankshaw et al. 2017)).
Bảng 12.10 cho một có tính minh họa độ trễ sự cố (breakdown) cho một suy luận yêu cầu (Table 12.10 gives an illustrative latency breakdown for an inference request). Mô hình suy luận
giai đoạn thứ mà các nhà cung cấp báo cáo như của họ “điểm chuẩn” con số kéo dài 5 tới 100 ms, tuy nhiên hàng đợi chờ thời gian nó
ngồi đằng sau dao động từ 0 tới hơn 1,000 ms: dưới tải, đơn thành phần một điểm chuẩn đo lường
bị làm cho nhỏ bé (dwarfed) bởi một (thành phần) nó không bao giờ nhìn thấy, do đó được báo cáo con số có thể là một nhỏ lát cắt của cái mà người dùng thực tế
trải nghiệm (The model inference stage that vendors report as their “benchmark” number spans 5 to 100 ms, yet the queue wait time it sits behind ranges from 0 to over 1,000 ms: under load, the single component a benchmark measures is dwarfed by one it never sees, so the reported number can be a small slice of what the user actually experiences).
Bảng 12.10: Suy luận Độ trễ Sự cố (Inference Latency Breakdown): Khác nhau đường ống các thành phần đóng góp tới đầu-tới-đầu độ trễ, và mô hình
suy luận (con số các nhà cung cấp một cách điển hình báo cáo) có thể là chỉ một phần của tổng yêu cầu thời gian (Different pipeline components contribute to end-to-end latency, and model inference (the number vendors typically report) can be only one part of total request time). Hàng đợi chờ thời gian có thể thống trị dưới
tải, việc làm cho đầu-tới-đầu sự đo lường thiết yếu cho thực tế hiệu suất sự đánh giá (Queue wait time can dominate under load, making end-to-end measurement essential for realistic performance assessment). Các phạm vi là có tính minh họa thay vì
phổ quát (Ranges are illustrative rather than universal).
Thành phần (Component)
Ví dụ Phạm vi (Example Range)
Các ghi chú (Notes)
Mạng khứ hồi (Network round-trip)
10–100 ms
Biến đổi bởi khu vực (Varies by region)
Yêu cầu việc phân tích cú pháp (Request parsing)
0.1–1 ms
JSON/protobuf
Đầu vào sự tiền xử lý (Input preprocessing)
1–50 ms
Việc mã hóa (Tokenization), hình ảnh thay đổi kích thước (image resize)
Hàng đợi chờ thời gian (Queue wait time)
0–1000+ ms
Phụ thuộc-tải (Load-dependent)
Mô hình suy luận (Model inference)
5–100 ms
“Điểm chuẩn” (The “benchmark”)
Đầu ra hậu xử lý (Output postprocessing)
0.5–10 ms
Việc giải mã (Decoding), định dạng (format)
Phản hồi sự tuần tự hóa (Response serialization)
0.1–1 ms
JSON/protobuf
Những cấp độ-thành phần các sự đóng góp này giải thích tại sao việc tối ưu hóa bất kỳ đơn giai đoạn (nào) mang lại việc giảm dần
các khoản lợi nhuận trên đầu-tới-đầu hiệu suất, một sự tối ưu hóa trần được chính thức hóa bởi Amdahl’s Định luật (These component-level contributions explain why optimizing any single stage yields diminishing returns on end-to-end performance, an optimization ceiling formalized by Amdahl’s Law).
Khăn ăn Toán học (Napkin Math) 12.4: Amdahl’s Định luật (Amdahl’s Law): sự tối ưu hóa trần (optimization ceiling)
Vấn đề: Một thị giác đường ống dành 8 ms trên sự tiền xử lý (JPEG giải mã, thay đổi kích thước, chuẩn hóa)
và 10 ms trên suy luận (A vision pipeline spends 8 ms on preprocessing (JPEG decode, resize, normalize) and 10 ms on inference). Nếu suy luận một mình được tối ưu hóa bởi 5×, bao nhiêu thực sự
đầu-tới-đầu độ trễ cải thiện? (If inference alone is optimized by 5×, how much does end-to-end latency actually improve?)
Toán học (Math): Việc tối ưu hóa suy luận từ 10 ms tới 2 ms giảm tổng độ trễ từ 18 ms tới chỉ 10 ms,
một 1.8× sự cải thiện thay vì 5× (Optimizing inference from 10 ms to 2 ms reduces total latency from 18 ms to only 10 ms, a 1.8× improvement rather than 5×). Amdahl’s Định luật chính thức hóa này trần: nếu sự tiền xử lý
tiêu thụ phân số 𝑓của tổng độ trễ, thì thậm chí vô hạn nhanh suy luận mang lại tại nhiều nhất 1/𝑓
sự tăng tốc (Amdahl’s Law formalizes this ceiling: if preprocessing consumes fraction 𝑓 of total latency, then even infinitely fast inference yields at most 1/𝑓 speedup). Với sự tiền xử lý tại 44.4 phần trăm của độ trễ (𝑓≈0.44), tối đa có thể đạt được
sự tăng tốc là 1/𝑓≈2.25× bất chấp của mô hình sự tối ưu hóa (With preprocessing at 44.4 percent of latency (𝑓≈0.44), the maximum achievable speedup is 1/𝑓≈2.25× regardless of model optimization).

12. Việc đo điểm chuẩn (Benchmarking)
679
27
INT8 (8-Bit Số nguyên):
INT8 ngồi tại tích cực
đầu của độ chính xác hệ thống phân cấp
(FP32 cơ sở, FP16 giảm một nửa
bộ nhớ, INT8 giảm một phần tư nó),
và mỗi bước đòi hỏi ngày càng
tăng sự cẩn thận để bảo tồn độ
chính xác (INT8 sits at the aggressive end of the precision hierarchy (FP32 baseline, FP16 halves memory, INT8 quarters it), and each step demands increasing care to preserve accuracy).
Việc đo điểm chuẩn
cạm bẫy (catch):
INT8 yêu cầu hậu-
huấn luyện sự hiệu chuẩn việc sử dụng một
đại diện tập dữ liệu, và
độ chính xác sự bảo tồn (một cách điển
hình 95–99 phần trăm của FP32)
phụ thuộc trên sự hiệu chuẩn
dữ liệu’s sự tương đồng tới sự triển
khai dữ liệu (The benchmarking catch: INT8 requires post-training calibration using a representative dataset, and accuracy preservation (typically 95–99 percent of FP32) depends on the calibration data’s similarity to deployment data). INT8 các điểm chuẩn
mà không quy định sự hiệu chuẩn
tập dữ liệu và thủ tục
là không thể tái tạo (INT8 benchmarks without specifying the calibration dataset and procedure are not reproducible).
28
Mô hình Sự nén
Việc đo điểm chuẩn (Model Compression Benchmarking): Sự nén
tác động phải được đo lường
qua bốn các chiều một cách đồng
thời: độ chính xác sự suy thoái,
suy luận sự tăng tốc, bộ
nhớ sự giảm, và năng lượng các khoản tiết
kiệm (Compression impact must be measured across four dimensions simultaneously: accuracy degradation, inference speedup, memory reduction, and energy savings).
Một kỹ thuật việc đạt
được 10× kích thước sự giảm với
1 phần trăm độ chính xác sự mất mát có thể
vẫn là không phù hợp nếu độ trễ
không cải thiện một cách tỷ
lệ; không có cấu trúc việc cắt tỉa (pruning),
cho ví dụ, giảm tham số
số đếm nhưng hiếm khi cải thiện
độ trễ trên dày đặc (dense) phần cứng bởi
vì thưa thớt (sparse) các hoạt động thiếu
hiệu quả phần cứng sự hỗ trợ trên
hầu hết các GPUs (A technique achieving 10× size reduction with 1 percent accuracy loss may still be unsuitable if latency does not improve proportionally; unstructured pruning, for example, reduces parameter count but rarely improves latency on dense hardware because sparse operations lack efficient hardware support on most GPUs).
29
Không máy chủ (Serverless) AI: Sự triển-
khai hệ biến hóa (paradigm) nơi các mô hình
mở rộng quy mô từ không (zero) các phiên bản trên
nhu cầu (Deployment paradigm where models scale from zero instances on demand). Việc đo điểm chuẩn
cạm bẫy (trap): không máy chủ các nhà cung cấp báo-
cáo suy luận độ trễ ngoại-
trừ lạnh-khởi động thời gian, nhưng cho
ngắt quãng (intermittent) các khối lượng công việc, lạnh
các khởi động (100 ms cho nhỏ các mô-
hình, 10+ các giây cho lớn ngôn-
ngữ các mô hình (LLMs)) thống-
trị người dùng-được nhận thức độ-
trễ (The benchmarking trap: serverless providers report inference latency excluding cold-start time, but for intermittent workloads, cold starts (100 ms for small models, 10+ seconds for large language models (LLMs)) dominate the user-perceived latency).
Điểm chuẩn các kết quả
từ ấm (warm) các phiên bản một cách có hệ-
thống nói giảm (understate) thực-thế giới
độ trễ cho các khối lượng công việc với
thấp yêu cầu các tỷ lệ (Benchmark results from warm instances systematically understate real-world latency for workloads with low request rates).
Các hệ thống sự thấu hiểu (Systems insight): Tích cực mô hình sự tối ưu hóa mang lại đáng thất vọng đầu-tới-đầu các kết quả
bất cứ khi nào không phải mô hình phân số thống trị (Aggressive model optimization yields disappointing end-to-end results whenever the nonmodel fraction dominates). Một 3× suy luận sự tăng tốc được báo cáo trong sự cô lập
có thể chuyển đổi tới chỉ 1.5× đầu-tới-đầu sự cải thiện trong sản xuất (A 3× inference speedup reported in isolation might translate to only 1.5× end-to-end improvement in production). Toàn diện các điểm-
chuẩn phải hoặc là bao gồm sự tiền xử lý trong các sự đo lường hoặc nêu một cách rõ ràng rằng được báo cáo
các sự tăng tốc áp dụng chỉ tới suy luận thành phần (Comprehensive benchmarks must either include preprocessing in measurements or state explicitly that reported speedups apply only to the inference component).
Amdahl’s trần làm nổi bật tại sao nghiêm ngặt việc đo điểm chuẩn phương pháp luận quan trọng (Amdahl’s ceiling highlights why rigorous benchmarking methodology matters). Toàn diện
độ trễ việc báo cáo yêu cầu việc quy định cái nào các thành phần được bao gồm, việc đo lường dưới thực tế
tải các điều kiện, và việc phân biệt thành phần từ đầu-tới-đầu các số liệu (Comprehensive latency reporting requires specifying which components are included, measuring under realistic load conditions, and distinguishing component from end-to-end metrics). Trước khi việc diễn giải bất kỳ
điểm chuẩn kết quả (nào), xác minh rằng sự đo lường cách tiếp cận chính nó là hợp lý (sound) (Before interpreting any benchmark result, verify that the measurement approach itself is sound).
Điểm kiểm tra (Checkpoint) 12.3: Việc đo điểm chuẩn phương pháp luận (Benchmarking methodology)
Tồi tệ các điểm chuẩn tối ưu hóa sai các thứ (Bad benchmarks optimize the wrong things).
Ba các thực tiễn phân biệt nghiêm ngặt các điểm chuẩn từ gây hiểu lầm những cái (Three practices distinguish rigorous benchmarks from misleading ones):
□Đại diện dữ liệu (Representative data): So sánh điểm chuẩn đầu vào sự phân phối chống lại sản xuất
sự phân phối (Compare the benchmark input distribution against the production distribution).
□Làm ấm (Warm-up): Nêu bao nhiêu ban đầu các lượt chạy đã bị loại bỏ trước khi việc ghi lại các sự đo lường (State how many initial runs were discarded before recording measurements).
□Sự cô lập (Isolation): Tài liệu hóa máy, cạnh tranh các khối lượng công việc, và thời gian chạy cấu hình
được sử dụng trong suốt sự đo lường (Document the machine, competing workloads, and runtime configuration used during measurement).
Thông lượng và lô tính hiệu quả đo lường liệu một việc phục vụ hệ thống có thể sử dụng có sẵn phần cứng
mà không vi phạm độ trễ các sự ràng buộc (Throughput and batch efficiency measure whether a serving system can use available hardware without violating latency constraints). Thông lượng đếm bao nhiêu suy luận các yêu cầu một hệ thống
xử lý mỗi giây, một cách điển hình được biểu diễn như các truy vấn mỗi giây (QPS) hay các khung mỗi giây (FPS) (Throughput counts how many inference requests a system processes per second, typically expressed as queries per second (QPS) or frames per second (FPS)).
Đơn-phiên bản các hệ thống xử lý mỗi đầu vào một cách độc lập trên sự đến; lô các hệ thống xử lý nhiều
các đầu vào trong song song, việc khai thác phần cứng sự song song cho cao hơn tính hiệu quả (Single-instance systems process each input independently on arrival; batch systems process multiple inputs in parallel, exploiting hardware parallelism for higher efficiency).
Cho ví dụ, dựa trên-đám mây các dịch vụ việc xử lý hàng triệu của các truy vấn mỗi giây hưởng lợi từ lô suy-
luận, nơi lớn các nhóm của các đầu vào được xử lý cùng nhau để tối đa hóa thuộc về tính toán tính hiệu quả (For example, cloud-based services handling millions of queries per second benefit from batch inference, where large groups of inputs are processed together to maximize computational efficiency). Trong
sự tương phản, các ứng dụng giống như robot, tương tác AI, và thực tế tăng cường yêu cầu thấp-độ trễ đơn-
phiên bản suy luận, nơi hệ thống phải phản hồi ngay lập tức tới mỗi mới đầu vào (In contrast, applications like robotics, interactive AI, and augmented reality require low-latency single-instance inference, where the system must respond immediately to each new input). Các điểm chuẩn
phải xem xét cả hai đơn-phiên bản và lô thông lượng để cung cấp một toàn diện sự hiểu biết
của suy luận hiệu suất qua khác nhau sự triển khai các kịch bản (Benchmarks must consider both single-instance and batch throughput to provide a comprehensive understanding of inference performance across different deployment scenarios).
Tốc độ một mình là không đủ bởi vì suy luận các sự tối ưu hóa có thể thay đổi mô hình hành vi (Speed alone is insufficient because inference optimizations can change model behavior). Việc giảm
thuộc về số độ chính xác gia tốc sự tính toán trong khi việc cắt giảm bộ nhớ và năng lượng, 2–4× sự tăng tốc
MobileNetV2 ngọn hải đăng (lighthouse) đã đo lường (bảng 12.6), nhưng thấp hơn-độ chính xác các tính toán có thể giới thiệu
độ chính xác sự suy thoái (Reducing numerical precision accelerates computation while cutting memory and energy, the 2–4× speedup the MobileNetV2 lighthouse measured (table 12.6), but lower-precision calculations can introduce accuracy degradation). Suy luận các điểm chuẩn do đó đánh giá cách nào tốt các mô hình thực hiện dưới
khác nhau thuộc về số các cài đặt, chẳng hạn như FP32, FP16, và INT827 (Inference benchmarks therefore evaluate how well models perform under different numerical settings, such as FP32, FP16, and INT827). Nhiều hiện đại AI các máy gia tốc hỗ trợ
hỗn hợp-độ chính xác suy luận, việc cho phép các hệ thống để một cách động điều chỉnh thuộc về số sự đại diện dựa
trên khối lượng công việc các yêu cầu (Many modern AI accelerators support mixed-precision inference, allowing systems to dynamically adjust numerical representation based on workload requirements). Mô hình sự nén các kỹ thuật28 xa hơn cải thiện tính hiệu quả, nhưng của chúng
tác động trên mô hình độ chính xác biến đổi phụ thuộc trên tác vụ và tập dữ liệu (Model compression techniques28 further improve efficiency, but their impact on model accuracy varies depending on the task and dataset). Các điểm chuẩn giúp xác định
liệu những sự tối ưu hóa này là khả thi cho sự triển khai, việc đảm bảo rằng các sự cải thiện trong tính hiệu quả
không đến tại chi phí của không thể chấp nhận được độ chính xác sự mất mát (Benchmarks help determine whether these optimizations are viable for deployment, ensuring that improvements in efficiency do not come at the cost of unacceptable accuracy loss).
Bộ nhớ dấu chân và mô hình tải thời gian định nghĩa liệu mô hình có thể bắt đầu, duy trì thường trú, và
phản hồi bên trong sự triển khai vỏ bọc (Memory footprint and model load time define whether the model can start, stay resident, and respond within the deployment envelope). Không giống huấn luyện, nơi các mô hình có thể kéo dài nhiều máy gia-
tốc, suy luận thường chạy bên trong nghiêm ngặt bộ nhớ các ngân sách (Unlike training, where models can span multiple accelerators, inference often runs within strict memory budgets). Tổng mô hình kích thước xác định lưu trữ
các yêu cầu, RAM sự sử dụng phản ánh làm việc bộ nhớ trong suốt sự thực thi, và bộ nhớ băng thông có thể
nút thắt cổ chai dữ liệu sự truyền tải giữa việc xử lý các đơn vị (Total model size determines storage requirements, RAM usage reflects working memory during execution, and memory bandwidth can bottleneck data transfer between processing units). Lạnh-khởi động hiệu suất trở nên then chốt khi
các mô hình được tải trên nhu cầu thay vì được giữ thường trú trong bộ nhớ (Cold-start performance becomes critical when models are loaded on demand rather than kept resident in memory). Trong không máy chủ AI các môi trường29,
nơi các tài nguyên mở rộng quy mô một cách động với đến (incoming) các yêu cầu, thời gian từ nhàn rỗi tới tích cực sự thực thi
xác định liệu người dùng trải nghiệm có thể chấp nhận được phản hồi các thời gian (In serverless AI environments29, where resources scale dynamically with incoming requests, the time from idle to active execution determines whether users experience acceptable response times).
Mô hình tải thời gian đề cập tới khoảng thời gian được yêu cầu để tải một được huấn luyện mô hình vào bộ nhớ trước khi nó có thể
xử lý các đầu vào (Model load time refers to the duration required to load a trained model into memory before it can process inputs). Trong một số các trường hợp, đặc biệt trên bị giới hạn-tài nguyên các thiết bị, các mô hình phải được tải lại
thường xuyên để giải phóng lên bộ nhớ cho khác các ứng dụng (In some cases, particularly on resource-limited devices, models must be reloaded frequently to free up memory for other applications). Thời gian được thực hiện cho đầu tiên suy luận yêu cầu là

680
12.8 Suy luận Các điểm chuẩn (Inference Benchmarks)
cũng một quan trọng sự xem xét, vì nó phản ánh tổng sự trì hoãn người dùng trải nghiệm khi việc tương tác với
một được cấp nguồn bằng-AI dịch vụ (also an important consideration, as it reflects the total delay users experience when interacting with an AI-powered service). Các điểm chuẩn giúp định lượng những các sự trì hoãn này, việc đảm bảo rằng suy luận các hệ thống có thể
đáp ứng thực-thế giới tính đáp ứng các yêu cầu (Benchmarks help quantify these delays, ensuring that inference systems can meet real-world responsiveness requirements).
Cấp độ-sự triển khai (Deployment-scale) các số liệu mở rộng giống nhau logic từ một yêu cầu tới một khối lượng công việc (Deployment-scale metrics extend the same logic from one request to a workload). Đám mây các dịch vụ
phải xử lý hàng triệu của đồng thời người dùng một cách hiệu quả, việc phân bổ các tài nguyên một cách động khi nhu cầu
dao động mà không làm tổn hại độ trễ; di động các thiết bị phải quản lý nhiều đồng thời AI
các mô hình mà không làm quá tải hệ thống (Cloud services must handle millions of concurrent users efficiently, allocating resources dynamically as demand fluctuates without compromising latency; mobile devices must manage multiple simultaneous AI models without overloading the system). Khả năng mở rộng quy mô đo lường cách nào tốt suy luận hiệu suất
cải thiện khi bổ sung thuộc về tính toán các tài nguyên được phân bổ (Scalability measures how well inference performance improves when additional computational resources are allocated). Trong một số các trường hợp, việc thêm nhiều GPUs
hay TPUs làm tăng thông lượng một cách tỷ lệ, nhưng trong khác các kịch bản, các nút thắt cổ chai chẳng hạn như bộ nhớ
băng thông các sự giới hạn hay mạng độ trễ có thể giới hạn việc mở rộng quy mô tính hiệu quả (In some cases, adding more GPUs or TPUs increases throughput proportionally, but in other scenarios, bottlenecks such as memory bandwidth limitations or network latency may limit scaling efficiency). Các điểm chuẩn cũng đánh giá
cách nào tốt một hệ thống cân bằng nhiều đồng thời các mô hình trong thực-thế giới sự triển khai, nơi khác nhau
được cấp nguồn bằng-AI các đặc trưng có thể cần để chạy tại giống nhau thời gian mà không có sự can thiệp (Benchmarks also assess how well a system balances multiple concurrent models in real-world deployment, where different AI-powered features may need to run at the same time without interference).
Năng lượng sự tiêu thụ đóng vòng lặp bởi vì suy luận các khối lượng công việc chạy một cách liên tục trong sản xuất (Energy consumption closes the loop because inference workloads run continuously in production).
Di động và biên các thiết bị đối mặt với nhiều nhất cấp bách (acute) các sự ràng buộc, nơi pin tuổi thọ và nhiệt các giới hạn hạn chế
có sẵn thuộc về tính toán các tài nguyên (Mobile and edge devices face the most acute constraints, where battery life and thermal limits restrict available computational resources). Thậm chí trong lớn-quy mô đám mây các môi trường, điện năng tính hiệu quả một cách trực tiếp
tác động hoạt động các chi phí và tính bền vững các mục tiêu (Even in large-scale cloud environments, power efficiency directly impacts operational costs and sustainability goals). Năng lượng được yêu cầu cho một đơn suy luận là
thường được đo lường trong các joules mỗi suy luận, việc phản ánh cách nào một cách hiệu quả một hệ thống xử lý các đầu vào trong khi
việc giảm thiểu điện năng việc rút ra (The energy required for a single inference is often measured in joules per inference, reflecting how efficiently a system processes inputs while minimizing power draw). Trong dựa trên-đám mây suy luận, tính hiệu quả là một cách phổ biến được biểu diễn như các truy vấn
mỗi giây mỗi watt (QPS/W) để định lượng cách nào tốt một hệ thống cân bằng hiệu suất và năng lượng
sự tiêu thụ (In cloud-based inference, efficiency is commonly expressed as queries per second per watt (QPS/W) to quantify how well a system balances performance and energy consumption). Cho di động AI các ứng dụng, việc tối ưu hóa suy luận điện năng sự tiêu thụ kéo dài pin
tuổi thọ và cho phép các mô hình để chạy một cách hiệu quả trên bị ràng buộc-tài nguyên các thiết bị (For mobile AI applications, optimizing inference power consumption extends battery life and allows models to run efficiently on resource-constrained devices). Việc giảm năng lượng sử dụng cũng
đóng một then chốt vai trò trong việc làm lớn-quy mô AI các hệ thống nhiều hơn về mặt môi trường bền vững, việc đảm bảo rằng
thuộc về tính toán các sự tiến bộ (advancements) căn chỉnh (align) với có ý thức-năng lượng (energy-conscious) sự triển khai các chiến lược (Reducing energy use also plays a key role in making large-scale AI systems more environmentally sustainable, ensuring that computational advancements align with energy-conscious deployment strategies).
12.8.3 Suy luận hiệu suất sự đánh giá (Inference performance evaluation)
Không giống huấn luyện, suy luận các hệ thống phải xử lý các đầu vào và phân phối các dự đoán một cách hiệu quả qua
đa dạng sự triển khai các kịch bản (Unlike training, inference systems must process inputs and deliver predictions efficiently across diverse deployment scenarios). Độ trễ, thông lượng, bộ nhớ sự sử dụng, và năng lượng tính hiệu quả cung cấp
được cấu trúc các sự đo lường cho việc đánh giá này hiệu suất (Latency, throughput, memory usage, and energy efficiency provide the structured measures for evaluating this performance).
Bảng 12.11 nên được đọc như một sự triển khai bộ lọc (filter): mỗi số liệu xác định một sự ràng buộc thứ mà có thể
thống trị một khác nhau việc phục vụ môi trường (Table 12.11 should be read as a deployment filter: each metric identifies a constraint that can dominate a different serving environment). Đuôi độ trễ (p99, p99.9) là có tính ràng buộc số liệu cho một
an toàn-then chốt (safety-critical) thời gian-thực hệ thống, nơi một đơn chậm yêu cầu thất bại thời hạn (deadline), trong khi các truy vấn mỗi
giây mỗi watt chi phối một bị ràng buộc-pin (battery-bound) di động sự triển khai, nơi giống nhau mô hình được đánh giá trên
độ bền (endurance) thay vì đỉnh tốc độ (Tail latency (p99, p99.9) is the binding metric for a safety-critical real-time system, where a single slow request fails the deadline, while queries per second per watt governs a battery-bound mobile deployment, where the same model is judged on endurance rather than peak speed). Các sự đánh đổi giữa các số liệu, bao gồm tốc độ so với độ chính xác và
thông lượng so với điện năng sự tiêu thụ, là phổ biến, và việc hiểu những các sự đánh đổi này là thiết yếu
cho hiệu quả hệ thống thiết kế (Trade-offs between metrics, including speed vs. accuracy and throughput vs. power consumption, are common, and understanding these trade-offs is essential for effective system design).
Bảng 12.11: Suy luận Hiệu suất Các số liệu (Inference Performance Metrics): Độ trễ, thông lượng, và tài nguyên sự sử dụng các số liệu cung cấp một định lượng cơ sở cho
việc tối ưu hóa được triển khai máy học các hệ thống và việc chọn thích hợp phần cứng các cấu hình, việc cân bằng tốc độ, chi phí, và
độ chính xác trong sản xuất các ứng dụng (Latency, throughput, and resource usage metrics provide a quantitative basis for optimizing deployed machine learning systems and selecting appropriate hardware configurations, balancing speed, cost, and accuracy in production applications).
Danh mục (Category)
Then chốt Các số liệu (Key Metrics)
Ví dụ Điểm chuẩn Sử dụng (Example Benchmark Use)
Độ trễ và Đuôi Độ trễ (Latency and Tail Latency)
Trung bình độ trễ (ms/yêu cầu); Đuôi độ trễ (p95, p99, p99.9) (Mean latency (ms/request); Tail latency (p95, p99, p99.9))
Việc đánh giá thời gian-thực
hiệu suất cho an toàn-then chốt AI (Evaluating real-time performance for safety-critical AI)
Thông lượng và
Tính hiệu quả (Throughput and Efficiency)
Các truy vấn mỗi giây (QPS); Các khung mỗi giây (FPS); Lô
thông lượng (Queries per second (QPS); Frames per second (FPS); Batch throughput)
Việc so sánh lớn-quy mô đám mây
suy luận các hệ thống (Comparing large-scale cloud inference systems)
Thuộc về số Độ chính xác
Tác động (Numerical Precision Impact)
Độ chính xác sự suy thoái (FP32 so với INT8); Sự tăng tốc từ
được giảm độ chính xác (Accuracy degradation (FP32 vs. INT8); Speedup from reduced precision)
Việc cân bằng độ chính xác so với tính hiệu quả
trong được tối ưu hóa suy luận (Balancing accuracy vs. efficiency in optimized inference)
Bộ nhớ Dấu chân (Memory Footprint)
Mô hình kích thước (MB/GB); RAM sự sử dụng (MB); Bộ nhớ
băng thông sự sử dụng (Model size (MB/GB); RAM usage (MB); Memory bandwidth utilization)
Việc đánh giá tính khả thi cho biên và
di động các sự triển khai (Assessing feasibility for edge and mobile deployments)
Lạnh-Khởi động và Tải
Thời gian (Cold-Start and Load Time)
Mô hình tải thời gian (s); Đầu tiên suy luận độ trễ (s) (Model load time (s); First inference latency (s))
Việc đánh giá tính đáp ứng trong
không máy chủ AI (Evaluating responsiveness in serverless AI)
Khả năng mở rộng quy mô (Scalability)
Tính hiệu quả dưới tải; Đa-mô hình việc phục vụ hiệu suất (Efficiency under load; Multi-model serving performance)
Việc đo lường tính mạnh mẽ cho
động, cao-nhu cầu các hệ thống (Measuring robustness for dynamic, high-demand systems)
Điện năng và Năng lượng
Tính hiệu quả (Power and Energy Efficiency)
Điện năng sự tiêu thụ (W); Hiệu suất mỗi W (QPS/W) (Power consumption (W); Performance per W (QPS/W))
Việc tối ưu hóa năng lượng sử dụng cho
di động và bền vững AI (Optimizing energy use for mobile and sustainable AI)
Những các số liệu này tương tác thông qua không thể tránh khỏi các sự đánh đổi (These metrics interact through unavoidable trade-offs). Việc tối ưu hóa cho cao thông lượng thông qua lớn
lô các kích thước làm tăng độ trễ, việc làm cho một hệ thống không phù hợp cho thời gian-thực các ứng dụng (Optimizing for high throughput via large batch sizes increases latency, making a system unsuitable for real-time applications). Việc giảm thuộc-
về số độ chính xác cải thiện điện năng tính hiệu quả và tốc độ nhưng có thể làm suy thoái độ chính xác (Reducing numerical precision improves power efficiency and speed but may degrade accuracy). Sự triển khai

12. Việc đo điểm chuẩn (Benchmarking)
681
30
Lạnh-Khởi động Độ trễ (Cold-Start Latency):
Sự khởi tạo thời gian từ nhàn rỗi
trạng thái, bị thống trị bởi mô hình
trọng số việc tải từ lưu trữ
tới máy gia tốc bộ nhớ (The initialization time from idle state, dominated by model weight loading from storage to accelerator memory). Cho một
7B-tham số mô hình trong FP16
(~14 GB), lạnh khởi động trên PCIe
4.0 (25 GB/s hiệu quả) thực hiện
~560 ms cho trọng số sự truyền tải
một mình, cộng bộ khung sự khởi tạo
chi phí chung (For a 7B-parameter model in FP16 (~14 GB), cold start on PCIe 4.0 (25 GB/s effective) takes ~560 ms for weight transfer alone, plus framework initialization overhead). Này vật-
lý thấp hơn giới hạn có nghĩa rằng
lạnh-khởi động sự giảm nhẹ (mitigation) (mô hình
việc lưu vào bộ nhớ đệm, suy đoán việc tải)
là một các hệ thống thiết kế yêu-
cầu, không chỉ một hoạt động
sự tiện lợi (This physical lower bound means that cold-start mitigation (model caching, speculative loading) is a systems design requirement, not just an operational convenience).
31
TOPS (Tera Các hoạt động
Mỗi Giây - Tera Operations Per Second):
Một sự đo lường
của
thô (raw)
thuộc về tính toán
thông lượng
(hàng nghìn tỷ
của
các hoạt động/giây) (A measure of raw computational throughput (trillions of operations/second)).
H100 phân phối 1979 TOPS
INT8
so với
Apple
M2
Thần kinh Động cơ tại 15.8 TOPS
và Edge TPU tại 4 TOPS,
nhưng những các con số này gộp chung (conflate)
khác nhau hoạt động các loại—
nhân-tích lũy (multiply-accumulate) (MAC)
so với tích lũy so với sự kích hoạt (The H100 delivers 1979 TOPS INT8 vs. the Apple M2 Neural Engine at 15.8 TOPS and Edge TPU at 4 TOPS, but these numbers conflate different operation types—multiply-accumulate (MAC) vs. accumulate vs. activation).
TOPS
các sự so sánh
qua
các nhà cung cấp
là
có ý nghĩa
chỉ
khi
hoạt động
định nghĩa,
độ chính xác,
và
tính thưa thớt
các giả định
là
y hệt, các điều kiện hiếm khi
được đáp ứng trong nhà cung cấp các thông số kỹ thuật (TOPS comparisons across vendors are meaningful only when the operation definition, precision, and sparsity assumptions are identical, conditions rarely met in vendor specifications).
môi trường xác định cái nào các sự đánh đổi là có thể chấp nhận được: đám mây các hệ thống ưu tiên khả năng mở rộng quy mô và
thông lượng, trong khi biên các thiết bị bị thống trị bởi bộ nhớ và điện năng các sự ràng buộc (environment determines which trade-offs are acceptable: cloud systems prioritize scalability and throughput, while edge devices are dominated by memory and power constraints). Việc đánh giá
suy luận hiệu suất một cách tổng thể, thay vì việc chăm chăm (fixating) trên một đơn số liệu, đảm bảo rằng các hệ thống đáp ứng
của chúng chức năng, tài nguyên, và hiệu suất các mục tiêu trong ngữ cảnh (Evaluating inference performance holistically, rather than fixating on a single metric, ensures that systems meet their functional, resource, and performance goals in context).
Sự triển khai kịch bản xác định ưu tiên thứ tự giữa những các số liệu đó (Deployment scenario determines the priority order among those metrics). Hoạt động các sự ràng-
buộc và thành công các tiêu chí biến đổi một cách ấn tượng qua các ngữ cảnh, do đó số liệu các ưu tiên giúp các kỹ sư
tập trung việc đo điểm chuẩn nỗ lực và diễn giải các kết quả bên trong đúng quyết định bộ khung (The operational constraints and success criteria vary dramatically across contexts, so metric priorities help engineers focus benchmarking effort and interpret results within the right decision framework). Bảng 12.12
minh họa cách nào hiệu suất các ưu tiên dịch chuyển qua năm chính sự triển khai các ngữ cảnh, việc tiết lộ
có hệ thống mối quan hệ giữa hoạt động các sự ràng buộc và sự tối ưu hóa các mục tiêu (Table 12.12 illustrates how performance priorities shift across five major deployment contexts, revealing the systematic relationship between operational constraints and optimization targets).
Bảng 12.12: Hiệu suất Số liệu Các ưu tiên bởi Sự triển khai Ngữ cảnh (Performance Metric Priorities by Deployment Context): Khác nhau hoạt động các môi trường đòi hỏi khác biệt
sự tối ưu hóa các trọng tâm, việc phản ánh việc biến đổi các sự ràng buộc và thành công các tiêu chí (Different operational environments demand distinct optimization focuses, reflecting varying constraints and success criteria). Những các ưu tiên này hướng dẫn cả hai điểm chuẩn sự lựa chọn và
kết quả sự diễn giải (These priorities guide both benchmark selection and result interpretation).
Sự triển khai
Ngữ cảnh (Deployment Context)
Chính Ưu tiên (Primary Priority)
Thứ cấp Ưu tiên (Secondary Priority)
Thứ ba Ưu tiên (Tertiary Priority)
Then chốt Thiết kế Sự ràng buộc (Key Design Constraint)
Thời gian-Thực
Các ứng dụng (Real-Time Applications)
Độ trễ (Latency) (p95 < 50
ms)
Độ tin cậy (Reliability) (99.9%)
Bộ nhớ Dấu chân (Memory Footprint)
Người dùng trải nghiệm đòi hỏi
ngay lập tức phản hồi (User experience demands immediate response)
Đám mây-Quy mô
Các dịch vụ (Cloud-Scale Services)
Thông lượng
(QPS) (Throughput (QPS))
Chi phí Tính hiệu quả (Cost Efficiency)
Trung bình Độ trễ (Average Latency)
Kinh doanh tính khả thi yêu cầu
khổng lồ quy mô (Business viability requires massive scale)
Biên/Di động
Các thiết bị (Edge/Mobile Devices)
Điện năng
Sự tiêu thụ (Power Consumption)
Bộ nhớ Dấu chân (Memory Footprint)
Độ trễ (Latency)
Pin tuổi thọ và tài nguyên các giới hạn
thống trị (Battery life and resource limits dominate)
Huấn luyện
Các khối lượng công việc (Training Workloads)
Huấn luyện Thời gian (Training Time)
GPU Sự sử dụng (GPU Utilization)
Bộ nhớ Tính hiệu quả (Memory Efficiency)
Nghiên cứu vận tốc cho phép nhanh hơn
sự thử nghiệm (Research velocity enables faster experimentation)
Khoa học/Y tế (Scientific/Medical)
Độ chính xác (Accuracy)
Độ tin cậy (Reliability)
Tính có thể giải thích (Explainability)
Tính đúng đắn không thể bị
tổn hại cho hiệu suất (Correctness cannot be compromised for performance)
Then chốt sự thấu hiểu từ bảng 12.12 là rằng giống nhau số liệu có thể là chính trong một ngữ cảnh và không liên quan
trong một (ngữ cảnh) khác (The key insight from table 12.12 is that the same metric can be primary in one context and irrelevant in another). Độ trễ xếp hạng đầu tiên cho thời gian-thực các ứng dụng (tự trị các phương tiện phải xử lý cảm biến
dữ liệu bên trong nghiêm ngặt định thời gian các thời hạn) nhưng thứ ba cho đám mây các dịch vụ (thứ mà chấp nhận cao hơn độ trễ trong
sự trao đổi cho chi phí tính hiệu quả mỗi truy vấn) (Latency ranks first for real-time applications (autonomous vehicles must process sensor data within strict timing deadlines) but tertiary for cloud services (which accept higher latency in exchange for cost efficiency per query)). Một điện thoại thông minh AI trợ lý thứ mà cải thiện thông lượng bởi 50
phần trăm nhưng làm tăng điện năng sự tiêu thụ bởi 30 phần trăm đại diện cho một ròng sự thoái lui (regression) vì pin tuổi thọ
một cách trực tiếp tác động người dùng sự hài lòng (A smartphone AI assistant that improves throughput by 50 percent but increases power consumption by 30 percent represents a net regression since battery life directly impacts user satisfaction). Y tế chẩn đoán các hệ thống ưu tiên độ chính xác như không thể thương lượng—
việc đạt được 99.2 phần trăm độ chính xác tại 10 ms độ trễ cung cấp vượt trội giá trị được so sánh tới 98.8 phần trăm
tại 5 ms (Medical diagnostic systems prioritize accuracy as nonnegotiable—achieving 99.2 percent accuracy at 10 ms latency provides superior value compared to 98.8 percent at 5 ms). Này sự phụ thuộc-ngữ cảnh có nghĩa rằng một 2× thông lượng sự cải thiện đại diện cho đáng kể
giá trị cho đám mây các sự triển khai nhưng tối thiểu lợi ích cho được cấp nguồn bằng pin biên các thiết bị, nơi 20 phần trăm
điện năng sự giảm phân phối vượt trội hoạt động tác động (This context-dependence means that a 2× throughput improvement represents substantial value for cloud deployments but minimal benefit for battery-powered edge devices, where 20 percent power reduction delivers superior operational impact).
Thậm chí với được định nghĩa tốt các số liệu, suy luận các sự đánh giá thất bại khi điểm chuẩn phớt lờ
sự triển khai sự ràng buộc thứ mà thống trị việc phục vụ hệ thống (Even with well-defined metrics, inference evaluations fail when the benchmark ignores the deployment constraint that dominates the serving system). Các theo sau các cạm bẫy chỉ ra nơi trung bình
độ trễ, bộ nhớ, năng lượng, lạnh các khởi động, và việc mở rộng quy mô các giả định có thể mỗi vô hiệu hóa một mặt khác
hợp lý kết quả (The following pitfalls show where average latency, memory, energy, cold starts, and scaling assumptions can each invalidate an otherwise plausible result).
Suy luận điểm chuẩn các thất bại bắt đầu khi điểm chuẩn tính trung bình đi sự kiện người dùng thực sự
chú ý (Inference benchmark failures begin when the benchmark averages away the event users actually notice). Đuôi độ trễ (p95, p99) xác định sản xuất độ tin cậy, không phải trung bình độ trễ; một hội thoại
AI hệ thống thứ mà lỡ của nó đuôi-độ trễ mục tiêu sẽ tạo ra không thể chấp nhận được phản hồi các sự trì hoãn thậm chí nếu của nó
trung bình phản hồi thời gian trông khỏe mạnh (Tail latency (p95, p99) determines production reliability, not mean latency; a conversational AI system that misses its tail-latency target will produce unacceptable response delays even if its average response time looks healthy). Tài nguyên các sự ràng buộc tạo ra giống nhau loại của sự không khớp (Resource constraints create the same kind of mismatch). Một
mô hình với xuất sắc đám mây thông lượng có thể vẫn là không thể sử dụng trên một điện thoại hay biên thiết bị nếu của nó bộ nhớ
dấu chân hay điện năng việc rút ra vượt quá sự triển khai ngân sách, do đó thực tế suy luận các điểm chuẩn phải
bao gồm bộ nhớ và năng lượng bên cạnh độ trễ (A model with excellent cloud throughput may still be unusable on a phone or edge device if its memory footprint or power draw exceeds the deployment budget, so practical inference benchmarks must include memory and energy alongside latency).
Không máy chủ và trên-nhu cầu việc phục vụ thêm một tách biệt đầu tiên-yêu cầu sự ràng buộc (Serverless and on-demand serving add a separate first-request constraint). Lạnh-khởi động độ trễ30
đo lường thời gian được yêu cầu để khởi tạo một mô hình và xử lý đầu tiên yêu cầu, do đó việc loại trừ mô hình
tải thời gian tạo ra không thực tế các kỳ vọng cho tính đáp ứng (Cold-start latency30 measures the time required to initialize a model and process the first request, so excluding model load time creates unrealistic expectations for responsiveness). Việc đánh giá cả hai mô hình tải thời gian và
đầu tiên-suy luận độ trễ đảm bảo rằng các hệ thống được thiết kế cho các điều kiện chúng sẽ thực tế đối mặt (Evaluating both model load time and first-inference latency ensures that systems are designed for the conditions they will actually face).
Suy luận các điểm chuẩn cũng trở nên gây hiểu lầm khi một số liệu được tối ưu hóa trong sự cô lập (Inference benchmarks also become misleading when one metric is optimized in isolation). Việc tối-
đa hóa lô thông lượng có thể làm suy thoái độ trễ, trong khi tích cực độ chính xác sự giảm có thể giảm
độ chính xác (Maximizing batch throughput can degrade latency, while aggressive precision reduction can reduce accuracy). Một độ chính xác ví dụ làm cho tính có thể so sánh vấn đề cụ thể (A precision example makes the comparability problem concrete).
Thuộc về số độ chính xác sự tối ưu hóa làm ví dụ cho này thách thức một cách đặc biệt tốt (Numerical precision optimization exemplifies this challenge particularly well). Cá nhân máy gia-
tốc các điểm chuẩn chỉ ra INT8 hoạt động thông lượng31 việc đạt tới khoảng 4× FP32 dấu-phẩy-động (Individual accelerator benchmarks show INT8 operation throughput31 reaching about 4× the FP32 floating-point)

682
12.8 Suy luận Các điểm chuẩn (Inference Benchmarks)
32
MLCommons: Phi lợi nhuận
hiệp hội được ra mắt trong 2020
từ sớm hơn MLPerf nỗ-
lực, với các thành viên từ công-
nghiệp, học thuật, các công ty khởi nghiệp,
và các tổ chức phi lợi nhuận (MLCommons
2026a). MLPerf chính nó đã bắt đầu
trong 2018 (MLCommons: Nonprofit consortium launched in 2020 from the earlier MLPerf effort, with members from industry, academia, startups, and nonprofits (MLCommons 2026a). MLPerf itself began in 2018).
MLCommons giải-
quyết điểm chuẩn sự đáng tin-
cậy bằng cách việc yêu cầu mở các sự đệ-
trình với đầy đủ hệ thống các thông số kỹ-
thuật, việc ngăn chặn việc chọn-
anh đào (cherry-picking) thứ mà đã gây ra bệnh dịch (plagued) cho sớm hơn
các điểm chuẩn (MLCommons addresses benchmark credibility by requiring open submissions with full system specifications, preventing the cherry-picking that plagued earlier benchmarks).
Được xuất bản các kết-
quả tiết lộ lớn hiệu suất
các sự khác biệt giữa các nhà cung cấp
trên y hệt các khối lượng công việc, việc làm
cho MLCommons sự gần-
nhất lĩnh vực có tới phong cách-SPEC
táo-tới-táo (apples-to-apples) phần-
cứng sự so sánh (Published results reveal large performance differences between vendors on identical workloads, making MLCommons the closest the field has to SPEC-style apples-to-apples hardware comparison).
33
DLRM: Facebook’s 2019
sự giới thiệu kiến trúc
kết hợp nhúng các bảng
cho
phân loại (categorical)
các đặc trưng
với đa lớp các perceptrons (multilayer perceptrons)
(MLPs)
cho
liên tục
các đặc trưng (Naumov et al. 2019) (DLRM: Facebook’s 2019 recommendation architecture combines embedding tables for categorical features with multilayer perceptrons (MLPs) for continuous features (Naumov et al. 2019)).
DLRM làm căng thẳng (stresses) các điểm chuẩn
một cách khác biệt
hơn
thị giác
hay
ngôn ngữ
các mô hình:
của nó
nhúng
các bảng
có thể
là
đủ lớn (để) rằng bộ nhớ
dung lượng
và
băng thông
thống trị tính toán thông-
lượng (DLRM stresses benchmarks differently than vision or language models: its embedding tables can be large enough that memory capacity and bandwidth dominate compute throughput).
Đó làm cho DLRM
một
hữu ích
bị giới hạn-bộ nhớ (memory-bound)
sự giới thiệu
khối lượng công việc
trong
phong cách-MLPerf
suy luận
sự đánh giá, việc tiết lộ phần-
cứng các sự giới hạn vô hình tới
bị giới hạn-tính toán các điểm chuẩn
(Reddi et al. 2019) (That makes DLRM a useful memory-bound recommendation workload in MLPerf-style inference evaluation, revealing hardware limitations invisible to compute-bound benchmarks (Reddi et al. 2019)).
thông lượng trên giống nhau máy gia tốc, việc tạo ra hấp dẫn hiệu suất các câu chuyện (throughput on the same accelerator, creating compelling performance narratives). Những các câu chuyện đó
là chỉ hợp lệ khi điểm chuẩn cũng kiểm tra độ chính xác, được hỗ trợ toán tử độ bao phủ, và liệu
được báo cáo các hoạt động là có thể so sánh qua các thiết bị (Those narratives are only valid when the benchmark also checks accuracy, supported operator coverage, and whether the reported operations are comparable across devices).
Việc mở rộng quy mô và ứng dụng sự phù hợp (fit) yêu cầu giống nhau sự hoài nghi (Scaling and application fit require the same skepticism). Tuyến tính việc mở rộng quy mô cạm bẫy được thảo luận cho
huấn luyện các điểm chuẩn áp dụng một cách bình đẳng tới suy luận, mặc dù các nút thắt cổ chai khác biệt: huấn luyện việc mở rộng quy mô là
thường bị giới hạn bởi gradient sự đồng bộ hóa, trong khi suy luận việc mở rộng quy mô chạm trán bộ nhớ băng thông
sự bão hòa, nhiệt sự điều tiết dưới được duy trì tải, và yêu cầu-định tuyến (request-routing) chi phí chung, thêm thời gian
được dành việc gán các yêu cầu tới mô hình các bản sao (replicas) trong được phân phối việc phục vụ (The linear scaling pitfall discussed for training benchmarks applies equally to inference, though the bottlenecks differ: training scaling is often limited by gradient synchronization, while inference scaling encounters memory bandwidth saturation, thermal throttling under sustained load, and request-routing overhead, the extra time spent assigning requests to model replicas in distributed serving). Như được thảo luận trong Chương 11,
những các sự giới hạn này phát sinh từ vật lý phần cứng các sự ràng buộc và kết nối liên thông (interconnect) các kiến trúc (As discussed in Chapter 11, these limitations arise from physical hardware constraints and interconnect architectures). Một được tối ưu hóa-
đám mây điểm chuẩn có thể do đó là không liên quan cho một biên sự triển khai nơi năng lượng và bộ nhớ
thống trị, do đó điểm chuẩn sự lựa chọn phải tuân theo ứng dụng yêu cầu thay vì thuận tiện nhất
bảng xếp hạng (leaderboard) (A cloud-optimized benchmark can therefore be irrelevant for an edge deployment where energy and memory dominate, so benchmark selection has to follow the application requirement rather than the most convenient leaderboard).
Cuối cùng, suy luận các kết quả cần giống nhau thống kê kỷ luật như huấn luyện các kết quả (Finally, inference results need the same statistical discipline as training results). Việc tuân theo các
sự đánh giá phương pháp luận các nguyên tắc được thiết lập trước đó, MLPerf giải quyết sự đo lường sự biến thiên
bằng cách việc yêu cầu nhiều điểm chuẩn các lượt chạy và việc báo cáo dựa trên-phân vị các số liệu thay vì đơn
các sự đo lường (Reddi et al. 2019) (Following the evaluation methodology principles established earlier, MLPerf addresses measurement variability by requiring multiple benchmark runs and reporting percentile-based metrics rather than single measurements (Reddi et al. 2019)). MLPerf Suy luận, cho ví dụ, báo cáo thứ 99 phân vị độ trễ
bên cạnh trung bình hiệu suất, việc nắm bắt cả hai điển hình hành vi và tồi tệ nhất-trường hợp các kịch bản thứ mà đơn-
lượt chạy các sự đo lường có thể bỏ lỡ (MLPerf Inference, for instance, reports 99th percentile latency alongside mean performance, capturing both typical behavior and worst-case scenarios that single-run measurements might miss). Này cách tiếp cận nhận ra rằng hệ thống hiệu suất một cách tự nhiên biến đổi
do các yếu tố chẳng hạn như nhiệt sự điều tiết, bộ nhớ sự phân bổ các mẫu, và nền tảng các quá trình (This approach recognizes that system performance naturally varies due to factors such as thermal throttling, memory allocation patterns, and background processes).
12.8.4 MLPerf suy luận các điểm chuẩn (MLPerf inference benchmarks)
Việc tránh những các cạm bẫy này yêu cầu việc xử lý suy luận việc đo điểm chuẩn như một quá trình của việc cân bằng nhiều
các ưu tiên (độ trễ, thông lượng, bộ nhớ, năng lượng, và độ chính xác) thay vì việc tối ưu hóa cho bất kỳ đơn
số liệu (nào) trong sự cô lập; MLPerf Suy luận vận hành (operationalizes) sự cân bằng đó thông qua cụ thể-sự triển khai
các kịch bản (Avoiding these pitfalls requires treating inference benchmarking as a process of balancing multiple priorities (latency, throughput, memory, energy, and accuracy) rather than optimizing for any single metric in isolation; MLPerf Inference operationalizes that balance through deployment-specific scenarios). MLPerf Suy luận quan trọng bởi vì sự triển khai ngữ cảnh thay đổi cái gì một kết quả có nghĩa (MLPerf Inference matters because deployment context changes what a result means).
Điểm chuẩn, được phát triển bởi MLCommons32, cung cấp một được chuẩn hóa bộ khung cho việc đánh giá
máy học suy luận hiệu suất qua một phạm vi của sự triển khai các môi trường (The benchmark, developed by MLCommons32, provides a standardized framework for evaluating machine learning inference performance across a range of deployment environments). MLPerf đã bắt đầu
với huấn luyện các điểm chuẩn trong 2018; MLPerf Suy luận đã được thêm sau đó để chuẩn hóa sự đánh giá
thời gian-sự triển khai qua các kịch bản (MLPerf began with training benchmarks in 2018; MLPerf Inference was added later to standardize deployment-time evaluation across scenarios). Khi máy học các hệ thống mở rộng vào đa dạng các ứng dụng, nó
đã trở nên rõ ràng rằng một một-kích thước-phù hợp-tất cả (one-size-fits-all) suy luận điểm chuẩn đã là không đủ (As machine learning systems expanded into diverse applications, it became clear that a one-size-fits-all inference benchmark was insufficient). Kết quả gia đình của
MLPerf suy luận các điểm chuẩn ánh xạ mỗi điểm chuẩn tới một sự triển khai cài đặt, do đó một điểm số có thể được
diễn giải chống lại độ trễ, thông lượng, bộ nhớ, và điện năng các sự ràng buộc hệ thống sẽ đối mặt (The resulting family of MLPerf inference benchmarks maps each benchmark to a deployment setting, so a score can be interpreted against the latency, throughput, memory, and power constraints the system will face).
12.8.4.1 MLPerf Suy luận (MLPerf Inference)
MLPerf Suy luận (Reddi et al. 2019) phục vụ như cơ sở suy luận điểm chuẩn, việc định nghĩa được chuẩn hóa
các kịch bản cho thời gian-sự triển khai sự đánh giá qua dữ liệu-trung tâm và biên các cài đặt (MLPerf Inference (Reddi et al. 2019) serves as the baseline inference benchmark, defining standardized scenarios for deployment-time evaluation across data-center and edge settings). Nó đánh giá
hiệu suất qua sâu học tập các khối lượng công việc chẳng hạn như hình ảnh phân loại, đối tượng sự phát hiện, tự nhiên
ngôn ngữ việc xử lý, và sự giới thiệu các hệ thống (It assesses performance across deep learning workloads such as image classification, object detection, natural language processing, and recommendation systems). Này phiên bản của MLPerf là một một cách rộng rãi được sử dụng tham chiếu
điểm cho việc so sánh AI các máy gia tốc, GPUs, TPUs, và CPUs khi sự đệ trình các quy tắc và
khối lượng công việc kịch bản khớp được dự định sự triển khai môi trường (This version of MLPerf is a widely used reference point for comparing AI accelerators, GPUs, TPUs, and CPUs when the submission rules and workload scenario match the intended deployment environment).
Chính công nghệ các công ty thường xuyên tham chiếu MLPerf các kết quả cho phần cứng sự mua sắm (procurement) các quyết định (Major technology companies regularly reference MLPerf results for hardware procurement decisions). Khi việc đánh giá phần cứng cho sự giới thiệu các hệ thống cơ sở hạ tầng, MLPerf điểm chuẩn
các điểm số trên DLRM33 các khối lượng công việc có thể thông báo các sự lựa chọn giữa khác nhau máy gia tốc các thế hệ (When evaluating hardware for recommendation systems infrastructure, MLPerf benchmark scores on DLRM33 workloads can inform choices between different accelerator generations). Qua
các thế hệ, điểm chuẩn các kết quả thường cho thấy đáng kể thông lượng các sự cải thiện, mặc dù
độ lớn phụ thuộc trên khối lượng công việc, phần mềm ngăn xếp, và hệ thống cấu hình (Across generations, benchmark results often show substantial throughput improvements, although the magnitude depends on workload, software stack, and system configuration). Này minh họa cách nào
được chuẩn hóa các điểm chuẩn có thể chuyển đổi thành mang tính hậu quả cơ sở hạ tầng các quyết định (This illustrates how standardized benchmarks can translate into consequential infrastructure decisions).
Những được chuẩn hóa các sự đánh giá này cung cấp vô giá các sự so sánh, nhưng chi phí của toàn diện
việc đo điểm chuẩn giới hạn ai có thể tham gia và cách nào một cách kỹ lưỡng các hệ thống được đánh giá (These standardized evaluations provide invaluable comparisons, but the cost of comprehensive benchmarking limits who can participate and how thoroughly systems are evaluated).
Các hệ thống Quan điểm (Systems Perspective) 12.8: Chi phí của toàn diện việc đo điểm chuẩn (The cost of comprehensive benchmarking)
Việc đệ trình tới MLPerf có thể yêu cầu chuyên dụng kỹ thuật nỗ lực, phần cứng sự truy cập, sự tinh chỉnh,
sự xác nhận, và cẩn thận tài liệu hóa qua liên quan các cấu hình (Submitting to MLPerf can require dedicated engineering effort, hardware access, tuning, validation, and careful documentation across the relevant configurations). Chi phí phụ thuộc
một cách nặng nề trên khối lượng công việc và phạm vi, nhưng nó là đủ cao (để) rằng các sự đệ trình bị thống trị bởi chính
công nghệ các công ty và phần cứng các nhà cung cấp, trong khi nhỏ hơn các tổ chức dựa trên được xuất bản (The cost depends heavily on workload and scope, but it is high enough that submissions are dominated by major technology companies and hardware vendors, while smaller organizations rely on published)

12. Việc đo điểm chuẩn (Benchmarking)
683
các kết quả thay vì việc tiến hành của riêng họ toàn diện các sự đánh giá (results rather than conducting their own comprehensive evaluations). Đó rào cản thúc đẩy
nhu cầu cho nhiều hơn nhẹ cân (lightweight), nội bộ việc đo điểm chuẩn các thực tiễn thứ mà các tổ chức có thể sử dụng để
thực hiện được thông báo các quyết định mà không có chi phí của đầy đủ-quy mô được chuẩn hóa việc đo điểm chuẩn (That barrier motivates the need for more lightweight, internal benchmarking practices that organizations can use to make informed decisions without the expense of full-scale standardized benchmarking).
Phần còn lại của MLPerf suy luận gia đình thu hẹp đó cơ sở bởi sự triển khai ngữ cảnh (The rest of the MLPerf inference family narrows that baseline by deployment context). MLPerf
Di động (Mobile) (MLCommons 2024a) đánh giá liệu một mô hình có thể duy trì tính đáp ứng bên trong điện thoại thông minh
điện năng và bộ nhớ các giới hạn (Janapa Reddi et al. 2022), việc đo lường thời gian-thực AI các tác vụ chẳng hạn như dựa trên-máy ảnh
cảnh sự phát hiện, lời nói sự nhận dạng, và thực tế tăng cường (MLPerf Mobile (MLCommons 2024a) evaluates whether a model can remain responsive within smartphone power and memory limits (Janapa Reddi et al. 2022), measuring real-time AI tasks such as camera-based scene detection, speech recognition, and augmented reality). MLPerf Máy khách (Client) (MLCommons
2026b) giải quyết cục bộ-tính toán quyết định: liệu người tiêu dùng các thiết bị có thể chạy AI các khối lượng công việc
một cách trực tiếp thay vì việc dựa trên đám mây suy luận (MLPerf Client (MLCommons 2026b) addresses the local-computing decision: whether consumer devices can run AI workloads directly rather than relying on cloud inference). Của nó hiện tại sự nhấn mạnh trên cục bộ tạo sinh-AI (generative-AI) và
LLM các khối lượng công việc làm cho CPUs, rời rạc GPUs, và được tích hợp Thần kinh Việc xử lý Các đơn vị (Neural Processing Units) (NPUs) một phần
của được đo điểm chuẩn hệ thống thay vì ngẫu nhiên máy chủ phần cứng (Its current emphasis on local generative-AI and LLM workloads makes CPUs, discrete GPUs, and integrated Neural Processing Units (NPUs) part of the benchmarked system rather than incidental host hardware). MLPerf Nhỏ bé (Tiny) (C. Banbury et al.
2021) kiểm tra cực độ sự ràng buộc trường hợp: được nhúng và siêu-thấp-điện năng AI các hệ thống, chẳng hạn như IoT
các thiết bị, các thiết bị đeo (wearables), và các vi điều khiển (MLPerf Tiny (C. Banbury et al. 2021) tests the extreme constraint case: embedded and ultra-low-power AI systems, such as IoT devices, wearables, and microcontrollers). Những các biến thể này bảo tồn giống nhau điểm chuẩn kỷ luật
trong khi việc thay đổi có tính ràng buộc tài nguyên từ dữ liệu trung tâm thông lượng tới máy khách tính đáp ứng, di động
điện năng, hay vi điều khiển bộ nhớ (These variants preserve the same benchmark discipline while changing the binding resource from data center throughput to client responsiveness, mobile power, or microcontroller memory).
12.8.4.2 MLPerf sự thực thi các kịch bản (MLPerf execution scenarios)
Giống nhau phần cứng có thể báo cáo một cách ấn tượng khác nhau điểm chuẩn các con số phụ thuộc trên cách nào các yêu cầu
đến—một sự thật thứ mà giải thích tại sao nhà cung cấp các tuyên bố thường thất bại để dự đoán sản xuất hiệu suất (The same hardware can report dramatically different benchmark numbers depending on how requests arrive—a fact that explains why vendor claims often fail to predict production performance). Kinh điển
MLPerf Suy luận định nghĩa bốn sự thực thi các kịch bản thứ mà đặc trưng hóa khác biệt lưu lượng các mẫu, mỗi (kịch bản)
việc yêu cầu khác nhau sự tối ưu hóa các chiến lược (Reddi et al. 2019) (Classic MLPerf Inference defines four execution scenarios that characterize distinct traffic patterns, each requiring different optimization strategies (Reddi et al. 2019)). Hiện tại máy khách và tạo sinh-AI
điểm chuẩn các biến thể cũng bao gồm tương tác các sự đo lường cho nhạy cảm-với-độ trễ LLM các khối lượng công việc,
nơi các số liệu chẳng hạn như thời gian-tới-đầu tiên-token và thời gian-mỗi-đầu ra-token trở thành trung tâm (MLCommons
2026b) (Current client and generative-AI benchmark variants also include interactive measurements for latency-sensitive LLM workloads, where metrics such as time-to-first-token and time-per-output-token become central (MLCommons 2026b)).
ĐơnLuồng (SingleStream) ĐơnLuồng xử lý một yêu cầu tại một thời điểm, việc đo lường độ trễ cho tuần tự
suy luận (SingleStream processes one request at a time, measuring latency for sequential inference). Này kịch bản mô hình hóa di động và được nhúng các ứng dụng nơi một đơn người dùng tương tác
với thiết bị: một điện thoại thông minh máy ảnh ứng dụng việc phân loại các hình ảnh, một giọng nói trợ lý việc xử lý lời nói,
hay một thiết bị đeo việc phát hiện các cử chỉ (This scenario models mobile and embedded applications where a single user interacts with the device: a smartphone camera app classifying images, a voice assistant processing speech, or a wearable detecting gestures). Then chốt số liệu là mỗi-yêu cầu độ trễ, và việc tạo lô cung cấp không
lợi ích vì các yêu cầu đến chỉ sau khi trước đó kết quả được tiêu thụ (The key metric is per-request latency, and batching provides no benefit since requests arrive only after the previous result is consumed). Sự tối ưu hóa tập trung trên
sự tiền xử lý tính hiệu quả và điện năng sự tiêu thụ thay vì thông lượng (Optimization focuses on preprocessing efficiency and power consumption rather than throughput).
ĐaLuồng (MultiStream) ĐaLuồng xử lý nhiều được đồng bộ hóa đầu vào các luồng một cách đồng thời, việc mô hình hóa
các kịch bản giống như tự trị các phương tiện với nhiều các máy ảnh thứ mà phải được xử lý cùng nhau cho
không gian sự kết hợp (spatial fusion) (MultiStream processes multiple synchronized input streams simultaneously, modeling scenarios like autonomous vehicles with multiple cameras that must be processed together for spatial fusion). Không giống ĐơnLuồng’s tuần tự các yêu cầu, ĐaLuồng yêu cầu việc xử lý các khung
từ tất cả các cảm biến bên trong chặt chẽ video-tỷ lệ các thời hạn (Unlike SingleStream’s sequential requests, MultiStream requires processing frames from all sensors within tight video-rate deadlines). Then chốt sự phân biệt từ Máy chủ (Server) chế độ là rằng
ĐaLuồng các đầu vào đến trong bước khóa (lockstep), trong khi Máy chủ các yêu cầu đến một cách độc lập và không thể dự đoán được (The key distinction from Server mode is that MultiStream inputs arrive in lockstep, while Server requests arrive independently and unpredictably).
Then chốt sự ràng buộc là sự đồng bộ hóa: tất cả các luồng phải hoàn thành trước khi việc lập kế hoạch mô-đun có thể hành động (The key constraint is synchronization: all streams must complete before the planning module can act).
Sự tối ưu hóa tập trung trên sự bồn chồn (jitter) việc xử lý và việc đáp ứng cứng các thời hạn thay vì trung bình thông lượng (Optimization focuses on jitter handling and meeting hard deadlines rather than average throughput).
Máy chủ (Server) Máy chủ tạo ra các yêu cầu việc tuân theo một Poisson sự phân phối, việc mô phỏng đám mây API lưu lượng
nơi các yêu cầu đến một cách độc lập và không thể dự đoán được (Server generates requests following a Poisson distribution, simulating cloud API traffic where requests arrive independently and unpredictably). Này kịch bản mô hình hóa web các dịch vụ việc xử lý
hàng triệu của các truy vấn từ khác nhau người dùng (This scenario models web services handling millions of queries from different users). Không giống ĐơnLuồng’s được đảm bảo tuần tự sự đến, Máy chủ
lưu lượng tạo ra việc xếp hàng các động lực nơi nhiều các yêu cầu cạnh tranh cho các tài nguyên (Unlike SingleStream’s guaranteed sequential arrival, Server traffic creates queuing dynamics where multiple requests compete for resources). Then chốt các số liệu là
thông lượng (các truy vấn mỗi giây) và đuôi độ trễ (p99), và động việc tạo lô có thể cải thiện tính hiệu quả
bằng cách việc nhóm các yêu cầu thứ mà đến bên trong một thời gian cửa sổ (The key metrics are throughput (queries per second) and tail latency (p99), and dynamic batching can improve efficiency by grouping requests that arrive within a time window). Sự tối ưu hóa cân bằng thông lượng chống lại
độ trễ SLOs (Optimization balances throughput against latency SLOs).
Ngoại tuyến (Offline) Ngoại tuyến cung cấp tất cả các đầu vào trả trước (upfront), việc đo lường tối đa thông lượng khi độ trễ các sự ràng-
buộc bị loại bỏ (Offline provides all inputs upfront, measuring maximum throughput when latency constraints are removed). Này kịch bản mô hình hóa lô việc xử lý các đường ống: qua đêm dữ liệu việc xử lý,
khoa học tính toán, hay việc tính toán trước (precomputing) các sự giới thiệu (This scenario models batch processing pipelines: overnight data processing, scientific computing, or precomputing recommendations). Với không độ trễ yêu cầu, các hệ thống
có thể sử dụng tối đa lô các kích thước để bão hòa phần cứng sự sử dụng (With no latency requirement, systems can use maximum batch sizes to saturate hardware utilization). Then chốt số liệu là thuần túy thông lượng
(các mẫu mỗi giây), và sự tối ưu hóa tập trung hoàn toàn trên phần cứng tính hiệu quả (The key metric is pure throughput (samples per second), and optimization focuses entirely on hardware efficiency).
Bảng 12.13 ánh xạ kinh điển sự thực thi các kịch bản, cộng mới hơn Tương tác được định hướng-LLM (Interactive LLM-oriented) trường hợp, tới
của chúng sự triển khai các ngữ cảnh và sự tối ưu hóa các chiến lược (Table 12.13 maps the classic execution scenarios, plus the newer Interactive LLM-oriented case, to their deployment contexts and optimization strategies).

684
12.8 Suy luận Các điểm chuẩn (Inference Benchmarks)
Bảng 12.13: MLPerf Sự thực thi Các kịch bản (MLPerf Execution Scenarios): Kinh điển MLPerf Suy luận các kịch bản ánh xạ tới khác biệt sự triển khai các ngữ cảnh, mỗi
việc yêu cầu khác nhau sự tối ưu hóa các chiến lược, và mới hơn Tương tác các kịch bản mở rộng bộ khung tới nhạy cảm-với-độ trễ LLM
các khối lượng công việc (Classic MLPerf Inference scenarios map to distinct deployment contexts, each requiring different optimization strategies, and newer Interactive scenarios extend the framework to latency-sensitive LLM workloads). ĐơnLuồng và ĐaLuồng ưu tiên độ trễ, Máy chủ cân bằng thông lượng và độ trễ, Ngoại tuyến tối đa hóa
thông lượng, và Tương tác nhấn mạnh mức độ-token tính đáp ứng (SingleStream and MultiStream prioritize latency, Server balances throughput and latency, Offline maximizes throughput, and Interactive emphasizes token-level responsiveness). Việc khớp kịch bản tới sự triển khai ngữ cảnh xác định
cái nào điểm chuẩn các kết quả là có liên quan (Matching the scenario to deployment context determines which benchmark results are relevant).
Kịch bản (Scenario)
Ngữ cảnh (Context)
Chiến lược (Strategy)
Trọng tâm (Focus)
ĐơnLuồng (SingleStream)
Di động các ứng dụng, được nhúng các thiết bị
Không việc tạo lô (lô = 1)
Sự tiền xử lý, điện năng tính hiệu quả
ĐaLuồng (MultiStream)
Tự trị lái xe, video
phân tích (analytics)
Được đồng bộ hóa cảm biến sự kết hợp (sensor fusion)
Sự bồn chồn (Jitter) việc xử lý, thời hạn các sự đảm bảo
Máy chủ (Server)
Đám mây APIs, web các dịch vụ
Động việc tạo lô với thời gian chờ (timeout)
Thông lượng-độ trễ sự đánh đổi
sự tinh chỉnh (tuning)
Ngoại tuyến (Offline)
Lô việc xử lý, dữ liệu các đường ống
Tối đa lô kích thước
Thông lượng, phần cứng sự sử dụng
Tương tác (Interactive)
Trò chuyện, các tác nhân, cục bộ tạo sinh AI
Token việc truyền phát (streaming), KV-bộ nhớ đệm (KV-cache)
sự quản lý
Thời gian-tới-đầu tiên-token (Time-to-first-token),
thời gian-mỗi-đầu ra-token (time-per-output-token)
Các kịch bản giải thích tại sao giống nhau phần cứng có thể báo cáo một cách ấn tượng khác nhau điểm chuẩn
các con số (The scenarios explain why the same hardware can report dramatically different benchmark numbers). Trong một mang tính minh họa sự so sánh, một máy gia tốc với cao Ngoại tuyến thông lượng có thể duy trì nhiều
thấp hơn Máy chủ-chế độ thông lượng một khi p99 độ trễ các sự ràng buộc và việc xếp hàng chi phí chung được thực thi,
bởi vì Máy chủ chế độ không thể luôn luôn sử dụng tối đa lô các kích thước (In an illustrative comparison, an accelerator with high Offline throughput can sustain much lower Server-mode throughput once p99 latency constraints and queuing overhead are enforced, because Server mode cannot always use maximum batch sizes). Khi việc đánh giá phần cứng cho một
cụ thể ứng dụng, việc lựa chọn thích hợp kịch bản đảm bảo điểm chuẩn các kết quả dự đoán sản xuất
hiệu suất (When evaluating hardware for a specific application, selecting the appropriate scenario ensures benchmark results predict production performance). Để làm cho dựa trên-kịch bản sự xác nhận (trở nên) cụ thể, chúng ta quay trở lại tới MobileNetV2 ngọn hải đăng (lighthouse)
trên EdgeTPU (To make scenario-based validation concrete, we return to the MobileNetV2 lighthouse on EdgeTPU).
Ngọn hải đăng (Lighthouse) 12.2: MobileNetV2 trên EdgeTPU
Việc hoàn thành của chúng ta MobileNetV2 ngọn hải đăng ví dụ, chúng ta xác nhận phần cứng sự gia tốc
các tuyên bố từ Chương 11 việc sử dụng kịch bản kỷ luật thứ mà MLPerf áp dụng tới tập trung-vào-độ trễ
biên suy luận (Reddi et al. 2019; C. Banbury et al. 2021) (Completing our MobileNetV2 lighthouse example, we validate the hardware acceleration claims from Chapter 11 using the scenario discipline that MLPerf applies to latency-focused edge inference (Reddi et al. 2019; C. Banbury et al. 2021)).
Phần cứng sự gia tốc tuyên bố: Trong này mang tính minh họa biên-máy gia tốc kịch bản, máy gia tốc
đạt được ~2 ms suy luận cho INT8 MobileNetV2, xấp xỉ 7.5× sự tăng tốc qua một Cortex-
M-lớp CPU (~15 ms) (Hardware acceleration claim: In this illustrative edge-accelerator scenario, the accelerator achieves ~2 ms inference for INT8 MobileNetV2, approximately 7.5× speedup over a Cortex-M-class CPU (~15 ms)). Thực tế các kết quả phụ thuộc trên toán tử độ bao phủ, xung nhịp tần số, nhiệt
trạng thái, và sự triển khai (Actual results depend on operator coverage, clock frequency, thermal state, and implementation).
Bảng 12.14 báo cáo sự xác nhận giao thức dưới ĐơnLuồng kịch bản (Table 12.14 reports the validation protocol under the SingleStream scenario).
Bảng 12.14: EdgeTPU so với Cortex-M7 MobileNetV2 sự xác nhận (EdgeTPU vs. Cortex-M7 MobileNetV2 validation): ĐơnLuồng-kịch bản các sự đo lường việc so sánh
suy luận độ trễ, đầu-cuối độ trễ, điện năng, và năng lượng mỗi suy luận cho INT8 MobileNetV2, việc cho thấy cách nào
sự tiền xử lý chi phí chung làm hẹp (nổi bật) tiêu đề máy gia tốc sự tăng tốc (SingleStream-scenario measurements comparing inference latency, end-to-end latency, power, and energy per inference for INT8 MobileNetV2, showing how preprocessing overhead narrows the headline accelerator speedup).
Số liệu (Metric)
CPU (Cortex-M7)
EdgeTPU
Được tuyên bố (Claimed)
Được xác nhận? (Validated?)
Suy luận độ trễ (Inference latency)
~15 ms
~2 ms
7.5× nhanh hơn
✓
Đầu-cuối độ trễ (End-to-end latency)
~18 ms
~6 ms
—
~3× nhanh hơn
Điện năng sự tiêu thụ (Power consumption)
~120 mW
~500 mW
—
~4.2× cao hơn
Năng lượng mỗi suy luận (Energy per inference)
~1.8 mJ
~1 mJ
—
~1.8× nhiều hơn hiệu quả
Cái gì này tiết lộ: 7.5× suy luận sự tăng tốc là có thật, nhưng đầu-cuối sự cải thiện là chỉ
~3× bởi vì sự tiền xử lý (hình ảnh sự chụp, định cỡ lại, chuẩn hóa) chạy trên CPU trong cả hai các trường hợp (What this reveals: The 7.5× inference speedup is real, but end-to-end improvement is only ~3× because preprocessing (image capture, resize, normalize) runs on the CPU in both cases).
EdgeTPU tiêu thụ nhiều hơn điện năng nhưng hoàn thành nhanh hơn, việc mang lại tốt hơn năng lượng tính hiệu quả mỗi
suy luận (EdgeTPU consumes more power but completes faster, yielding better energy efficiency per inference).
Sự triển khai quyết định: Cho được cấp nguồn bằng pin các thiết bị việc chạy một cách không thường xuyên, chủ động suy luận
sự tính toán một mình thiên vị (favors) EdgeTPU, nhưng tổng số pin tác động phụ thuộc trên ngủ điện năng, thức-dậy
năng lượng, máy chủ-sự truyền tải chi phí chung, và liệu máy gia tốc có thêm nhàn rỗi sự rò rỉ (leakage) trong khi hệ thống
chờ (Deployment decision: For battery-powered devices running infrequently, the active inference calculation alone favors EdgeTPU, but total battery impact depends on sleep power, wake-up energy, host-transfer overhead, and whether the accelerator adds idle leakage while the system waits). Cho liên tục video hoạt động, EdgeTPU’s thấp hơn chủ động năng lượng mỗi suy luận là nhiều
nhiều khả năng (more likely) để thống trị (For continuous video operation, EdgeTPU’s lower active energy per inference is much more likely to dominate).

12. Việc đo điểm chuẩn (Benchmarking)
685
Sự triển khai điện năng trải dài mười bậc (orders)
của độ lớn, µW tới kW (Deployment power spans ten orders of magnitude, µW to kW).
ĐơnLuồng kết quả minh họa tại sao việc đo điểm chuẩn yêu cầu việc khớp MLPerf kịch bản tới
sự triển khai ngữ cảnh: ĐơnLuồng xác nhận di động các ứng dụng, trong khi Ngoại tuyến các điểm chuẩn
sẽ đưa ra khác nhau các kết luận được tối ưu hóa cho thông lượng thay vì độ trễ (The SingleStream result illustrates why benchmarking requires matching the MLPerf scenario to the deployment context: SingleStream validates mobile applications, while Offline benchmarks would give different conclusions optimized for throughput rather than latency).
Huấn luyện các điểm chuẩn đo lường học tập tốc độ; suy luận các điểm chuẩn đo lường việc phục vụ tốc độ (Training benchmarks measure learning speed; inference benchmarks measure serving speed).
Tuy nhiên cả hai các sự đo lường chia sẻ một chí mạng điểm mù (blind spot): chúng nói không gì cả về bao nhiêu năng lượng hệ thống
tiêu thụ để đạt được đó tốc độ (Yet both measures share a critical blind spot: they say nothing about how much energy the system consumes to achieve that speed). Một hệ thống thứ mà thiết lập thông lượng các kỷ lục trong khi việc tiêu thụ các kilowatt của
điện năng có thể là về mặt kinh tế không thể duy trì hoặc về mặt vật lý không thể để triển khai tại biên (A system that sets throughput records while consuming kilowatts of power may be economically unsustainable or physically impossible to deploy at the edge). Việc hoàn thành
sự đánh giá bức tranh yêu cầu điện năng sự đo lường: việc đo lường năng lượng chi phí của hiệu suất (Completing the evaluation picture requires power measurement: measuring the energy cost of performance).
12.9 Điện năng Sự đo lường Các kỹ thuật (Power Measurement Techniques)
Một chip nhà cung cấp quảng cáo “10 TOPS tại 0.5 W,” nhưng dưới được duy trì suy luận tải, nhiệt sự điều tiết
làm giảm thực tế thông lượng tới 3 TOPS tại 2 W (A chip vendor advertises “10 TOPS at 0.5 W,” but under sustained inference load, thermal throttling drops actual throughput to 3 TOPS at 2 W). Mà không có được chuẩn hóa điện năng sự đo lường, này 13.3×
tính hiệu quả khoảng cách giữa bảng dữ liệu (datasheet) và thực tế không bị phát hiện cho đến khi sự triển khai (Without standardized power measurement, this 13.3× efficiency gap between the datasheet and reality goes undetected until deployment).
Này thứ ba chiều (dimension) là chí mạng bởi vì Chương 11 đã thiết lập TOPS/W như một chính thiết kế
mục tiêu bên cạnh thô TOPS (This third dimension is critical because Chapter 11 established TOPS/W as a primary design objective alongside raw TOPS). Điện năng các điểm chuẩn xác nhận liệu được tối ưu hóa-tính hiệu quả các máy gia tốc
(có) phân phối của chúng được hứa hẹn năng lượng các khoản tiết kiệm (Power benchmarks validate whether efficiency-optimized accelerators deliver their promised energy savings). TOPS/W là đặc biệt dễ bị (susceptible) tới (việc) chơi game một cách chính xác
bởi vì nó là một tỷ số của hai một cách tách biệt có thể trích dẫn (quotable) các đỉnh: một nhà cung cấp có thể đọc tử số (các hoạt động)
tại lô kích thước và độ chính xác thứ mà tối đa hóa thông lượng và mẫu số (watts) tại một gần-nhàn rỗi
hoạt động điểm, do đó được quảng cáo tính hiệu quả mô tả một trạng thái chip không bao giờ chiếm giữ dưới thực tế
tải (TOPS/W is particularly susceptible to gaming precisely because it is a ratio of two separately quotable peaks: a vendor can read the numerator (operations) at the batch size and precision that maximize throughput and the denominator (watts) at a near-idle operating point, so the advertised efficiency describes a state the chip never occupies under real load). Điện năng các điểm chuẩn đóng đó lỗ hổng (loophole) bằng cách việc cố định khối lượng công việc và sự đo lường cửa sổ,
việc ép buộc tử số và mẫu số để được đọc tại giống nhau hoạt động điểm (Power benchmarks close that loophole by fixing the workload and the measurement window, forcing the numerator and denominator to be read at the same operating point).
Tuy nhiên, việc đo lường điện năng sự tiêu thụ trong máy học các hệ thống đưa ra các thách thức khác biệt
từ việc đo lường thời gian hay thông lượng (However, measuring power consumption in machine learning systems presents challenges distinct from measuring time or throughput). Điện năng biến đổi với nhiệt độ, khối lượng công việc pha (phase), và hệ thống
cấu hình theo các cách thứ mà hiệu suất các số liệu không (làm) (Power varies with temperature, workload phase, and system configuration in ways that performance metrics do not). Bảng 12.15 định lượng cách nào năng lượng các nhu cầu
của ML các mô hình biến đổi một cách ấn tượng qua sự triển khai các môi trường, việc trải dài nhiều bậc (orders)
của độ lớn từ TinyML các thiết bị việc tiêu thụ chỉ các microwatt tới dữ liệu trung tâm các giá đỡ (racks) việc yêu cầu các kilo-
watt (Table 12.15 quantifies how energy demands of ML models vary dramatically across deployment environments, spanning multiple orders of magnitude from TinyML devices consuming mere microwatts to data center racks requiring kilowatts). Này rộng quang phổ minh họa trung tâm thách thức trong việc tạo ra được chuẩn hóa việc đo điểm chuẩn
các phương pháp luận (Henderson et al. 2020) (This wide spectrum illustrates the central challenge in creating standardized benchmarking methodologies (Henderson et al. 2020)).
Việc tạo ra một được thống nhất phương pháp luận qua này mười-bậc-của-độ lớn (ten-orders-of-magnitude) phạm vi yêu cầu cẩn thận sự xem-
xét của mỗi quy mô’s độc đáo các đặc điểm: mức độ-microwatt TinyML các sự đo lường đòi hỏi
khác nhau thiết bị đo đạc (instrumentation) hơn quy mô-kilowatt máy chủ giá đỡ sự giám sát (Creating a unified methodology across this ten-orders-of-magnitude range requires careful consideration of each scale’s unique characteristics: microwatt-level TinyML measurements demand different instrumentation than kilowatt-scale server rack monitoring). Một toàn diện bộ khung
phải thích ứng những các quy mô này trong khi việc duy trì tính nhất quán, tính công bằng, và tính có thể tái tạo (A comprehensive framework must accommodate these scales while maintaining consistency, fairness, and reproducibility).
Bảng 12.15: Điện năng Sự tiêu thụ Quang phổ (Power Consumption Spectrum): Các đại diện sự triển khai các điểm được liệt kê ở đây trải dài trên bảy bậc của
độ lớn trong điện năng các nhu cầu, từ quy mô-microwatt TinyML các thiết bị (150 µW) tới quy mô-kilowatt ML máy chủ các giá đỡ (10 kW);
hình 12.6 mở rộng giống nhau bức tranh xuống tới 5.6 µW tại TinyML sàn và lên tới xấp xỉ 498 kW tại huấn luyện-cụm (The representative deployment points listed here span over seven orders of magnitude in power demands, from microwatt-scale TinyML devices (150 µW) to kilowatt-scale ML server racks (10 kW); figure 12.6 extends the same picture down to 5.6 µW at the TinyML floor and up to roughly 498 kW at the training-cluster ceiling, covering nearly eleven orders of magnitude). Này khổng lồ phạm vi giải thích tại sao không đơn sự đo lường kỹ thuật hay
tính hiệu quả số liệu áp dụng một cách phổ quát: việc đo điểm chuẩn một 150 µW thần kinh bộ xử lý yêu cầu một cách cơ bản khác nhau
thiết bị đo đạc hơn việc đo lường một 10 kW máy chủ giá đỡ (This enormous range explains why no single measurement technique or efficiency metric applies universally: benchmarking a 150 µW neural processor requires fundamentally different instrumentation than measuring a 10 kW server rack).
Thể loại (Category)
Thiết bị Loại (Device Type)
Điện năng Sự tiêu thụ (Power Consumption)
Nhỏ bé (Tiny)
Thần kinh Quyết định Bộ xử lý (NDP - Neural Decision Processor)
150 µW
Nhỏ bé (Tiny)
M7 Vi điều khiển (Microcontroller)
25 mW
Di động (Mobile)
Raspberry Pi 4
3.5 W
Di động (Mobile)
Điện thoại thông minh (Smartphone)
4 W
Biên (Edge)
Thông minh Máy ảnh (Smart Camera)
10-15 W
Biên (Edge)
Biên Máy chủ (Edge Server)
65-95 W
Đám mây (Cloud)
ML Máy chủ Nút (ML Server Node)
300-500 W
Đám mây (Cloud)
ML Máy chủ Giá đỡ (ML Server Rack)
4-10 kW
12.9.1 Điện năng sự đo lường các ranh giới (Power measurement boundaries)
Để giải quyết những sự đo lường các thách thức này, chúng ta phải hiểu cách nào điện năng sự tiêu thụ được đo-
lường tại khác nhau hệ thống các quy mô, từ TinyML các thiết bị tới đầy đủ-quy mô dữ liệu trung tâm suy luận các nút (To address these measurement challenges, we must understand how power consumption is measured at different system scales, from TinyML devices to full-scale data center inference nodes).

686
12.9 Điện năng Sự đo lường Các kỹ thuật (Power Measurement Techniques)
Hình 12.7 trình bày (lays out) các khác biệt sự đo lường các ranh giới cho mỗi kịch bản: các thành phần trong (màu) xanh lá rơi
bên trong năng lượng kế toán ranh giới, trong khi các thành phần với đỏ đứt nét (dashed) các đường viền (outlines) được một cách rõ ràng
loại trừ từ điện năng các sự đo lường (Figure 12.7 lays out the distinct measurement boundaries for each scenario: components in green fall inside the energy accounting boundary, while components with red dashed outlines are explicitly excluded from power measurements). Này sự phân biệt quan trọng bởi vì nơi ranh giới được vẽ
xác định cái gì đếm như “hiệu quả.” (This distinction matters because where the boundary is drawn determines what counts as “efficient.”)
Tính toán Đơn vị (Compute Unit)
Tính toán Đơn vị (Compute Unit)
Cơ bản (Basic)
Bộ chuyển mạch (Switch)
Trên Chip (On Chip)
SRAM
Tiny Ví dụ
Truyền thống (siêu) Thấp Điện năng SoC (Traditional (ultra) Low Power SoC)
Điện năng Sự đo lường Ranh giới (Power Measurement Boundary)
Không trong Ranh giới (Not in Boundary)
Biểu đồ Khóa (Diagram Key)
Tính toán (Compute)
Đơn vị (Unit)
Tính toán (Compute)
Đơn vị (Unit)
Trên Chip (On Chip)
SRAM
Chuyển mạch (Switching)
NoC
Tính toán (Compute)
Đơn vị (Unit)
Tính toán (Compute)
Đơn vị (Unit)
Điển hình Suy luận SoC 1 (Typical Inference SoC 1)
Ngoài-Chip DRAM (Off-Chip DRAM)
Ngoài-Chip DRAM (Off-Chip DRAM)
Điển hình Suy luận SoC n (Typical Inference SoC n)
(Các) Máy gia tốc + (Accelerator(s) +)
Cục bộ RAM (Local RAM)
(Các) Máy gia tốc + (Accelerator(s) +)
Cục bộ RAM (Local RAM)
Chủ động (Active)
Làm mát (Cooling)
NIC
Cục bộ (Local)
Lưu trữ (Storage)
Máy chủ (Host)
DRAM
(Các) Máy chủ (Host(s))
(Các) Máy chủ (Host(s))
Truyền thống Suy luận Nút 1 (Traditional Inference Node 1)
Tính toán Nút 1 (Được đo lường) (Compute Node 1 (Measured))
Tính toán Nút 2 (Được đo lường) (Compute Node 2 (Measured))
Mạng (Các) Bộ chuyển mạch (Network Switches)
(Được đo lường/Được ước tính) ((Measured/Estimated))
Lưu trữ Nút (Storage Node)
Tính toán Nút n (Được đo lường) (Compute Node n (Measured))
DC Làm mát Các thành phần (DC Cooling Components)
Huấn luyện Giá đỡ 1 (Training Rack 1)
Huấn luyện Giá đỡ n (Training Rack n)
Từ xa Lưu trữ (Remote Storage)
Từ xa Lưu trữ (Remote Storage)
Sự kết nối liên thông Các kết cấu (Interconnection Fabrics)
Suy luận Ví dụ (Inference Example)
Huấn luyện Ví dụ (Training Example)
Hình 12.7: Điện năng Sự đo lường Các ranh giới (Power Measurement Boundaries): MLPerf định nghĩa hệ thống các ranh giới cho điện năng sự đo lường, việc trải dài từ
đơn-chip các thiết bị tới đầy đủ dữ liệu trung tâm các nút, để kích hoạt công bằng các sự so sánh của năng lượng tính hiệu quả qua đa dạng phần cứng các nền tảng (MLPerf defines system boundaries for power measurement, ranging from single-chip devices to full data center nodes, to enable fair comparisons of energy efficiency across diverse hardware platforms).
Những các ranh giới này phác họa (delineate) cái nào các thành phần’ điện năng sự tiêu thụ được bao gồm trong được báo cáo các số liệu, việc tác động
sự diễn giải của hiệu suất các kết quả (These boundaries delineate which components’ power consumption is included in reported metrics, impacting the interpretation of performance results). Nguồn (Source): (Tschand et al. 2024).
Biểu đồ được tổ chức vào ba các thể loại, Nhỏ bé, Suy luận, và Huấn luyện các ví dụ, mỗi (ví dụ)
việc phản ánh khác nhau sự đo lường các phạm vi dựa trên trên hệ thống kiến trúc và sự triển khai môi trường (The diagram is organized into three categories, Tiny, Inference, and Training examples, each reflecting different measurement scopes based on system architecture and deployment environment).
Trong TinyML các hệ thống, toàn bộ thấp-điện năng SoC, bao gồm tính toán, bộ nhớ, và cơ bản các kết nối liên thông (interconnects),
điển hình rơi bên trong sự đo lường ranh giới (In TinyML systems, the entire low-power SoC, including compute, memory, and basic interconnects, typically falls within the measurement boundary). Suy luận các nút giới thiệu nhiều hơn tính phức tạp,
việc kết hợp nhiều SoCs, cục bộ lưu trữ, các máy gia tốc, và bộ nhớ, trong khi thường việc loại trừ từ xa
lưu trữ và ngoài-chip các thành phần (Inference nodes introduce more complexity, incorporating multiple SoCs, local storage, accelerators, and memory, while often excluding remote storage and off-chip components). Huấn luyện các sự triển khai trải dài nhiều các giá đỡ (racks), nơi chỉ được chọn
các yếu tố, bao gồm tính toán các nút và mạng các bộ chuyển mạch, được đo lường, trong khi lưu trữ các hệ thống,
làm mát cơ sở hạ tầng, và các phần của kết nối liên thông kết cấu thường bị loại trừ (Training deployments span multiple racks, where only selected elements, including compute nodes and network switches, are measured, while storage systems, cooling infrastructure, and parts of the interconnect fabric are often excluded).
Nơi ranh giới rơi xác định cái gì đếm như năng lượng, nhưng bên trong bất kỳ ranh giới (nào)
chiếm ưu thế số hạng (term) hiếm khi là số học (Where the boundary falls determines what counts as energy, but within any boundary the dominant term is rarely arithmetic). Việc phân rã suy luận năng lượng vào của nó vật lý các nguồn cho thấy
tại sao độ chính xác, không phải thô hoạt động số đếm, là chính năng lượng đòn bẩy, và tại sao một điện năng điểm chuẩn
thứ mà phớt lờ dữ liệu sự di chuyển đo lường sai thứ (Decomposing inference energy into its physical sources shows why precision, not raw operation count, is the primary energy lever, and why a power benchmark that ignores data movement measures the wrong thing).
Khăn ăn Toán 12.5 (Napkin Math 12.5): Tại sao INT8 tiết kiệm năng lượng
Nhớ lại từ Chương 11 rằng việc di chuyển dữ liệu tốn kém nhiều hơn năng lượng hơn việc tính toán trên nó (
năng lượng-sự di chuyển bất biến (invariant) được chính thức hóa trong Chương 4 và được định lượng bởi Horowitz’s năng lượng
các sự ước tính (Horowitz 2014)) (Recall from Chapter 11 that moving data costs far more energy than computing on it (the energy-movement invariant formalized in Chapter 4 and quantified by Horowitz’s energy estimates (Horowitz 2014))). Việc hiểu tại sao sự lượng tử hóa giảm năng lượng sự tiêu thụ
yêu cầu việc phân rã năng lượng vào của nó vật lý các nguồn (Understanding why quantization reduces energy consumption requires decomposing energy into its physical sources). Hai chiếm ưu thế các yếu tố xác định
suy luận năng lượng: tính toán các hoạt động và bộ nhớ sự truy cập (Two dominant factors determine inference energy: compute operations and memory access).
Hẹp hơn các kiểu dữ liệu (datatypes) nói chung yêu cầu ít hơn chuyển mạch và lưu trữ năng lượng mỗi hoạt động, do đó
bảng 12.16 tiết lộ một 18× khoảng cách giữa FP32 và INT8 nhân-tích lũy chi phí (Narrower datatypes generally require less switching and storage energy per operation, so table 12.16 reveals an 18× gap between FP32 and INT8 multiply-accumulate cost):
Bảng 12.16: Mỗi-hoạt động năng lượng bởi độ chính xác (Per-operation energy by precision): Năng lượng chi phí của một đơn nhân-tích lũy tại FP32, FP16, và INT8,
với tương đối chi phí được chuẩn hóa tới FP32, việc minh họa tại sao hẹp hơn các kiểu dữ liệu thống trị tính toán-năng lượng các khoản tiết kiệm (Energy cost of a single multiply-accumulate at FP32, FP16, and INT8, with relative cost normalized to FP32, illustrating why narrower datatypes dominate compute-energy savings). Các giá trị
tuân theo kinh điển năng lượng-ước tính phong cách được sử dụng trong Horowitz (2014) và phần D.1 (Values follow the canonical energy-estimate style used in Horowitz (2014) and section D.1).
Độ chính xác (Precision)
Bộ nhân Năng lượng (Multiplier Energy)
Tương đối Chi phí (Relative Cost)
FP32
~3.7 pJ/FLOP
1×
FP16
~1.1 pJ/FLOP
0.3×
INT8
~0.2 pJ/FLOP
0.05×
Một 8-bit bộ nhân sử dụng ~18× ít hơn năng lượng hơn một 32-bit dấu-phẩy-động bộ nhân trong này năng lượng
mô hình bởi vì hẹp hơn số học giảm chuyển mạch và lưu trữ công việc (Horowitz 2014) (An 8-bit multiplier uses ~18× less energy than a 32-bit floating-point multiplier in this energy model because narrower arithmetic reduces switching and storage work (Horowitz 2014)).
Phần D.1 lập danh mục kinh điển mỗi-hoạt động năng lượng các con số đằng sau những các tỷ số này và cho thấy
tại sao FP32-tới-INT8 và dữ liệu-sự di chuyển-tới-tính toán (data-movement-to-compute) các khoảng cách (gaps) giữ (stay) ổn định qua phần cứng các thế-
hệ (Section D.1 catalogs the canonical per-operation energy figures behind these ratios and shows why the FP32-to-INT8 and data-movement-to-compute gaps stay stable across hardware generations).

12. Việc đo điểm chuẩn (Benchmarking)
687
Bảng 12.17 mở rộng bức tranh tới bộ nhớ sự truy cập, với năng lượng chi phí mỗi byte qua mỗi tầng (tier) của
hệ thống phân cấp (hierarchy) (Table 12.17 extends the picture to memory access, with energy cost per byte across each tier of the hierarchy):
Bảng 12.17: Bộ nhớ truy cập năng lượng bởi tầng (Memory access energy by tier): Mỗi-byte năng lượng chi phí qua thanh ghi-tới-DRAM hệ thống phân cấp, với tương đối
chi phí được chuẩn hóa tới một thanh ghi (việc) đọc, việc phơi bày tại sao ngoài-chip bộ nhớ lưu lượng thống trị suy luận năng lượng các ngân sách (Per-byte energy cost across the register-to-DRAM hierarchy, with relative cost normalized to a register read, exposing why off-chip memory traffic dominates inference energy budgets). Các giá trị
tuân theo giống nhau kinh điển năng lượng-ước tính mô hình được sử dụng trong Horowitz (2014) và phần D.1 (Values follow the same canonical energy-estimate model used in Horowitz (2014) and section D.1).
Bộ nhớ Mức độ (Memory Level)
Năng lượng mỗi Byte (Energy per Byte)
Tương đối Chi phí (Relative Cost)
Thanh ghi (Register)
~0.01 pJ
1×
L1 Bộ nhớ đệm (L1 Cache)
~0.5 pJ
50×
L2 Bộ nhớ đệm (L2 Cache)
~2 pJ
200×
DRAM
~160 pJ/byte
16,000×
Bộ nhớ sự truy cập thống trị: việc đọc một byte từ DRAM tốn kém hơn 16,000× nhiều hơn năng lượng hơn
một thanh ghi sự truy cập (Memory access dominates: reading one byte from DRAM costs over 16,000× more energy than a register access).
Bảng 12.18 kết hợp hai các hiệu ứng cho một MobileNetV2 suy luận, việc phân rã mỗi-suy luận
năng lượng vào mô hình-tải và tính toán các số hạng (terms) tại FP32 so với INT8 (Table 12.18 combines the two effects for a MobileNetV2 inference, decomposing per-inference energy into model-load and compute terms at FP32 vs. INT8):
Bảng 12.18: MobileNetV2 INT8 năng lượng sự phá vỡ (MobileNetV2 INT8 energy breakdown): Mỗi-suy luận năng lượng được phân rã vào mô hình-tải và tính toán
các số hạng cho FP32 so với INT8, việc cho thấy rằng INT8 sự lượng tử hóa tấn công DRAM-lưu lượng năng lượng như chiếm ưu thế thành phần (Per-inference energy decomposed into model-load and compute terms for FP32 vs. INT8, showing that INT8 quantization attacks DRAM-traffic energy as the dominant component).
Thành phần (Component)
FP32 (14 MB)
INT8 (3.5 MB)
Các khoản tiết kiệm (Savings)
Mô hình tải từ DRAM (Model load from DRAM)
2243 µJ
561 µJ
4×
Tính toán (300 MFLOP) (Compute (300 MFLOP))
1,110 µJ
60 µJ
18.5×
Tổng số (Total)
3,353 µJ
621 µJ
5.4×
Các hệ thống sự thấu hiểu: Bộ nhớ sự truy cập thống trị FP32 năng lượng sự tiêu thụ (~2.2 mJ so với 1.1 mJ
tính toán) (Systems insight: Memory access dominates FP32 energy consumption (~2.2 mJ vs. 1.1 mJ compute)). INT8 sự lượng tử hóa cung cấp 4× bộ nhớ năng lượng sự giảm và ~18.5× tính toán
năng lượng sự giảm (INT8 quantization provides 4× memory energy reduction and ~18.5× compute energy reduction). Kết hợp hiệu ứng giải thích tại sao được lượng tử hóa các mô hình trên biên các thiết bị có thể
cải thiện pin tuổi thọ: chúng tấn công chiếm ưu thế bộ nhớ nút thắt cổ chai trong khi một cách đồng thời
việc gia tốc tính toán (The combined effect explains why quantized models on edge devices can improve battery life: they attack the dominant memory bottleneck while simultaneously accelerating compute).
Cấp độ-hệ thống điện năng sự đo lường cung cấp một nhiều hơn tổng thể quan điểm hơn việc đo lường cá nhân các thành-
phần trong sự cô lập (System-level power measurement offers a more holistic view than measuring individual components in isolation). Trong khi cấp độ-thành phần các số liệu (cho ví dụ, máy gia tốc hay bộ xử lý điện năng) là
có giá trị cho hiệu suất sự tinh chỉnh, thế giới-thực ML các khối lượng công việc liên quan tới phức tạp các tương tác giữa
tính toán các đơn vị, bộ nhớ các hệ thống, và hỗ trợ cơ sở hạ tầng (While component-level metrics (for example, accelerator or processor power) are valuable for performance tuning, real-world ML workloads involve intricate interactions between compute units, memory systems, and supporting infrastructure). Cho ví dụ, sự phân tích của Google’s
TensorFlow Di động các khối lượng công việc cho thấy rằng dữ liệu sự di chuyển chiếm (accounts for) 57.3 phần trăm của tổng số suy luận
năng lượng sự tiêu thụ (Boroumand et al. 2018), việc làm nổi bật cách nào bị giới hạn-bộ nhớ các hoạt động có thể
thống trị hệ thống điện năng sự sử dụng (For instance, analysis of Google’s TensorFlow Mobile workloads shows that data movement accounts for 57.3 percent of total inference energy consumption (Boroumand et al. 2018), highlighting how memory-bound operations can dominate system power usage).
Được chia sẻ cơ sở hạ tầng đưa ra bổ sung các thách thức (Shared infrastructure presents additional challenges). Trong dữ liệu các trung tâm, các tài nguyên chẳng hạn như làm mát
các hệ thống và điện năng sự phân phối được chia sẻ qua các khối lượng công việc, việc làm phức tạp sự quy gán (attribution) của năng lượng (việc) sử dụng tới
cụ thể ML các tác vụ (In data centers, resources such as cooling systems and power delivery are shared across workloads, complicating attribution of energy use to specific ML tasks). Làm mát một mình có thể chiếm 20–30 phần trăm của tổng số cơ sở điện năng sự tiêu thụ,
việc làm cho nó một chính yếu tố trong năng lượng tính hiệu quả các sự đánh giá (Barroso et al. 2019) (Cooling alone can account for 20–30 percent of total facility power consumption, making it a major factor in energy efficiency assessments (Barroso et al. 2019)). Thậm chí tại biên,
các thành phần giống như bộ nhớ và I/O các giao diện có thể phục vụ cả hai ML và phi-ML (non-ML) các chức năng, xa hơn
việc làm mờ sự đo lường các ranh giới (Even at the edge, components like memory and I/O interfaces may serve both ML and non-ML functions, further blurring measurement boundaries).
Bên trong một đơn Transformer tiến lên (forward) lượt truyền (pass), tính toán hồ sơ (profile) dịch chuyển một cách sắc nét giữa tiến-lên-nguồn-cấp (feed-forward)
các lớp—dày đặc ma trận các phép nhân thứ mà bão hòa số học thông lượng và rút ra đỉnh điện năng—
và sự chú ý các lớp, thứ mà là bị giới hạn-bộ nhớ-băng thông với thấp hơn số học cường độ và
một cách tương ứng thấp hơn điện năng (sự) rút ra (Within a single Transformer forward pass, the compute profile shifts sharply between feed-forward layers—dense matrix multiplications that saturate arithmetic throughput and draw peak power—and attention layers, which are memory-bandwidth-bound with lower arithmetic intensity and correspondingly lower power draw). Hiện đại ML các máy gia tốc phản hồi tới này sự dao động thông qua
động điện áp và tần số sự mở rộng quy mô (dynamic voltage and frequency scaling) (DVFS), thứ mà điều chỉnh bộ xử lý điện áp và xung nhịp tần số
dựa trên trên khối lượng công việc các nhu cầu (Modern ML accelerators respond to this oscillation through dynamic voltage and frequency scaling (DVFS), which adjusts processor voltage and clock frequency based on workload demands). Tiên tiến DVFS các sự triển khai việc sử dụng trên-chip chuyển mạch các bộ điều chỉnh (regulators)
có thể đạt được có ý nghĩa năng lượng các khoản tiết kiệm (Kim et al. 2008), việc gây ra điện năng sự tiêu thụ cho giống nhau
ML mô hình để biến đổi với hệ thống tải và đồng thời (concurrent) hoạt động (Advanced DVFS implementations using on-chip switching regulators can achieve meaningful energy savings (Kim et al. 2008), causing power consumption for the same ML model to vary with system load and concurrent activity). Này nhanh chóng sự chuyển đổi (toggling) giữa điện năng

688
12.9 Điện năng Sự đo lường Các kỹ thuật (Power Measurement Techniques)
các trạng thái bên trong một đơn Transformer tiến lên lượt truyền tạo ra một nhiệt và sự đo lường thách thức thứ mà
chung máy chủ các khối lượng công việc không phô bày (exhibit): thấp-tỷ lệ điện năng việc lấy mẫu có thể bí danh (alias) qua tính toán-tới-
bộ nhớ pha ranh giới, việc tạo ra một được tính trung bình sự đọc thứ mà xuyên tạc (misrepresents) cả hai đỉnh (sự) rút ra
và thấp-điện năng sự dừng (dwell) thời gian (states within a single Transformer forward pass creates a thermal and measurement challenge that generic server workloads do not exhibit: low-rate power sampling can alias across the compute-to-memory phase boundary, producing an averaged reading that misrepresents both the peak draw and the low-power dwell time). Này sự biến thiên ảnh hưởng không chỉ tính toán các thành phần nhưng cũng
hỗ trợ cơ sở hạ tầng, vì được giảm bộ xử lý hoạt động có thể hạ thấp làm mát các yêu cầu và
tổng thể cơ sở điện năng (sự) rút ra (This variability affects not only the compute components but also the supporting infrastructure, as reduced processor activity can lower cooling requirements and overall facility power draw).
Hỗ trợ cơ sở hạ tầng, đặc biệt làm mát các hệ thống, là một chính thành phần của tổng số năng lượng sự tiêu-
thụ trong quy mô lớn các sự triển khai (Support infrastructure, particularly cooling systems, is a major component of total energy consumption in large-scale deployments). Dữ liệu các trung tâm phải duy trì hoạt động các nhiệt độ, điển hình
giữa 20–25 °C, để đảm bảo hệ thống độ tin cậy (Data centers must maintain operational temperatures, typically between 20–25 °C, to ensure system reliability). Làm mát chi phí chung được nắm bắt trong Điện năng (Việc) Sử dụng
Tính hiệu quả (Power Usage Effectiveness) (PUE) số liệu, thứ mà dao động từ 1.1 trong một cách cao độ hiệu quả các cơ sở tới trên 2.0 trong kém
được tối ưu hóa (các cơ sở) (Barroso et al. 2019) (Cooling overhead is captured in the Power Usage Effectiveness (PUE) metric, which ranges from 1.1 in highly efficient facilities to over 2.0 in less optimized ones (Barroso et al. 2019)). Sự tương tác giữa tính toán các khối lượng công việc và làm mát
cơ sở hạ tầng tạo ra phức tạp các sự phụ thuộc; cho ví dụ, điện năng sự quản lý các kỹ thuật giống như DVFS
không chỉ giảm trực tiếp bộ xử lý điện năng sự tiêu thụ nhưng cũng làm giảm nhiệt sự tạo ra, việc tạo ra
xếp tầng (cascading) các hiệu ứng trên làm mát các yêu cầu (The interaction between compute workloads and cooling infrastructure creates complex dependencies; for example, power management techniques like DVFS not only reduce direct processor power consumption but also decrease heat generation, creating cascading effects on cooling requirements). Thậm chí biên các thiết bị yêu cầu cơ bản nhiệt sự quản lý (Even edge devices require basic thermal management).
12.9.2 Thuộc về tính toán tính hiệu quả so với điện năng sự tiêu thụ (Computational efficiency vs. power consumption)
Mối quan hệ giữa thuộc về tính toán hiệu suất và năng lượng tính hiệu quả là một trung tâm sự đánh đổi
trong hiện đại ML hệ thống thiết kế (The relationship between computational performance and energy efficiency is a central trade-off in modern ML system design). Khi các hệ thống thúc đẩy cho cao hơn hiệu suất, chúng thường chạm trán
việc giảm dần các lợi nhuận (diminishing returns) trong năng lượng tính hiệu quả do vật lý các sự giới hạn trong bán dẫn (semiconductor) sự mở rộng quy mô và
điện năng sự phân phối (Koomey et al. 2011) (As systems push for higher performance, they often encounter diminishing returns in energy efficiency due to physical limitations in semiconductor scaling and power delivery (Koomey et al. 2011)). Này mối quan hệ là đặc biệt rõ ràng trong bộ xử lý tần số
sự mở rộng quy mô: cao hơn tần số thường yêu cầu cao hơn điện áp, do đó động điện năng có thể tăng nhanh hơn
được phân phối thông lượng, việc phản ánh điện áp-tần số-điện năng mối quan hệ thứ mà nằm dưới (underlies) DVFS và
của nó việc giảm dần các lợi nhuận (Le Sueur and Heiser 2010) (This relationship is particularly evident in processor frequency scaling: higher frequency often requires higher voltage, so dynamic power can rise faster than delivered throughput, reflecting the voltage-frequency-power relationship that underlies DVFS and its diminishing returns (Le Sueur and Heiser 2010)).
Trong sự triển khai các kịch bản với nghiêm ngặt năng lượng các sự ràng buộc, đặc biệt được cấp nguồn bằng pin biên các thiết bị
và di động các ứng dụng, việc tối ưu hóa này hiệu suất-năng lượng sự đánh đổi trở nên thiết yếu cho thực tế
tính khả thi (In deployment scenarios with strict energy constraints, particularly battery-powered edge devices and mobile applications, optimizing this performance-energy trade-off becomes essential for practical viability). Mô hình sự tối ưu hóa các kỹ thuật cung cấp đầy hứa hẹn các cách tiếp cận để đạt được tốt hơn tính hiệu quả
mà không có vật chất độ chính xác sự suy thoái (Model optimization techniques offer promising approaches to achieve better efficiency without material accuracy degradation). Thuộc về số độ chính xác sự tối ưu hóa các kỹ thuật, thứ mà giảm
thuộc về tính toán các yêu cầu trong khi việc duy trì mô hình chất lượng, chứng minh này sự đánh đổi một cách hiệu quả (Numerical precision optimization techniques, which reduce computational requirements while maintaining model quality, demonstrate this trade-off effectively).
Số nguyên sự lượng tử hóa các nghiên cứu cho thấy rằng được giảm-độ chính xác sự tính toán có thể thường bảo tồn mô hình
chất lượng trong khi việc cải thiện suy luận tốc độ, bộ nhớ lưu lượng, và năng lượng tính hiệu quả, mặc dù được hiện thực hóa
lợi ích phụ thuộc trên mô hình, sự hiệu chuẩn phương pháp, và phần cứng sự hỗ trợ (Jacob et al. 2018; Wu et al. 2020;
Gholami et al. 2021b) (Integer quantization studies show that reduced-precision computation can often preserve model quality while improving inference speed, memory traffic, and energy efficiency, although the realized gain depends on model, calibration method, and hardware support (Jacob et al. 2018; Wu et al. 2020; Gholami et al. 2021b)).
Sự tối ưu hóa các chiến lược trải dài ba được kết nối liên thông các chiều (dimensions): độ chính xác, thuộc về tính toán hiệu-
suất, và năng lượng tính hiệu quả (Optimization strategies span three interconnected dimensions: accuracy, computational performance, and energy efficiency). Tiên tiến sự tối ưu hóa các phương pháp cho phép được tinh chỉnh sự kiểm soát (control) qua
này sự đánh đổi không gian (Advanced optimization methods enable fine-tuned control over this trade-off space). Một cách tương tự, mô hình sự tối ưu hóa và sự nén (compression) các kỹ thuật yêu cầu cẩn thận
việc cân bằng của độ chính xác các tổn thất chống lại tính hiệu quả các lợi ích (Similarly, model optimization and compression techniques require careful balancing of accuracy losses against efficiency gains). Tối ưu hoạt động điểm giữa những
các yếu tố này phụ thuộc một cách nặng nề trên sự triển khai các yêu cầu và các sự ràng buộc; di động các ứng dụng điển hình
ưu tiên năng lượng tính hiệu quả để mở rộng pin tuổi thọ, trong khi dựa trên-đám mây các dịch vụ có thể tối ưu hóa cho
độ chính xác thậm chí tại cao hơn điện năng sự tiêu thụ các chi phí, việc hưởng lợi từ các nền kinh tế của quy mô và chuyên dụng
làm mát cơ sở hạ tầng (The optimal operating point among these factors depends heavily on deployment requirements and constraints; mobile applications typically prioritize energy efficiency to extend battery life, while cloud-based services might optimize for accuracy even at higher power consumption costs, benefiting from economies of scale and dedicated cooling infrastructure).
Năng lượng tính hiệu quả các số liệu bây giờ chiếm giữ một trung tâm vị trí trong AI hệ thống sự đánh giá (Energy efficiency metrics now occupy a central position in AI system evaluation). Điện năng sự đo-
lường các tiêu chuẩn chẳng hạn như MLPerf Điện năng (Tschand et al. 2024) cung cấp được chuẩn hóa các bộ khung cho
việc so sánh năng lượng tính hiệu quả qua phần cứng các nền tảng và sự triển khai các kịch bản (Power measurement standards such as MLPerf Power (Tschand et al. 2024) provide standardized frameworks for comparing energy efficiency across hardware platforms and deployment scenarios). Những các tiêu chuẩn này
cho phép các kỹ sư để một cách có hệ thống cân bằng hiệu suất, điện năng sự tiêu thụ, và thuộc về môi trường
tác động khi việc lựa chọn phần cứng và sự tối ưu hóa các chiến lược (These standards enable engineers to systematically balance performance, power consumption, and environmental impact when selecting hardware and optimization strategies).
12.9.3 Được chuẩn hóa điện năng sự đo lường (Standardized power measurement)
Điện năng sự đo lường các kỹ thuật giống như SPEC Điện năng đã từ lâu phục vụ chung việc tính toán (Lange 2009),
nhưng ML các khối lượng công việc phơi bày một cơ bản sự khó khăn: tức thời điện năng sự tiêu thụ trong suốt một
đơn suy luận có thể dịch chuyển một cách nhanh chóng giữa chuyên sâu-tính toán ma trận phép nhân và bộ nhớ-
sự đình trệ (stall) các pha (Power measurement techniques like SPEC Power have long served general computing (Lange 2009), but ML workloads expose a fundamental difficulty: instantaneous power consumption during a single inference can shift rapidly between compute-intensive matrix multiplication and memory-stall phases). MLPerf Điện năng chính thức hóa này vấn đề cho ML các hệ thống bằng cách việc chỉ định sự đo lường
các ranh giới, thiết bị đo đạc, và việc báo cáo các quy tắc qua một rộng điện năng phạm vi (Tschand et al. 2024) (MLPerf Power formalizes this problem for ML systems by specifying measurement boundaries, instrumentation, and reporting rules across a wide power range (Tschand et al. 2024)).
Này tính dễ bay hơi (volatility) có nghĩa rằng bất kỳ đơn-điểm sự đo lường (nào) là gây hiểu lầm, và hành động của sự đo lường
chính nó (thiết bị đo đạc chi phí chung, được tạo ra-bởi-việc lấy mẫu các sự trì hoãn) có thể làm nhiễu loạn chính điện năng hồ sơ (profile) đang
được đặc trưng hóa (This volatility means that any single-point measurement is misleading, and the act of measurement itself (instrumentation overhead, sampling-induced delays) can perturb the very power profile being characterized).

12. Việc đo điểm chuẩn (Benchmarking)
689
Lõi thách thức là do đó thuộc về thời gian: việc đặc trưng hóa một đại lượng (quantity) thứ mà dao động nhanh hơn
nhiều sự đo lường các công cụ có thể lấy mẫu (The core challenge is therefore temporal: characterizing a quantity that fluctuates faster than many measurement instruments can sample). Dày đặc ma trận các hoạt động trong transformer các lớp tạo ra
ngắn, dữ dội điện năng các gai (spikes) thứ mà yêu cầu cao-tần số việc lấy mẫu để nắm bắt một cách chính xác, trong khi
CNN suy luận có xu hướng hướng tới nhiều hơn nhất quán điện năng (sự) rút ra tuân theo (amenable) tới thấp hơn việc lấy mẫu các tỷ lệ (Dense matrix operations in transformer layers create short, intense power spikes that require high-frequency sampling to capture accurately, while CNN inference tends toward more consistent power draw amenable to lower sampling rates).
Sự đo lường cửa sổ phải cũng tính đến cho ML-cụ thể làm ấm (warm-up) các khoảng thời gian, nơi ban đầu các suy luận
tiêu thụ nhiều hơn điện năng do bộ nhớ đệm sự cư trú (population) và đường ống sự khởi tạo (The measurement window must also account for ML-specific warm-up periods, where initial inferences consume more power due to cache population and pipeline initialization). Trượt-cửa sổ các trung bình
qua được lặp lại các suy luận làm trơn (smooth) những các sự dao động này vào có thể hành động tính hiệu quả các con số, nhưng
cửa sổ kích thước chính nó trở thành một thiết kế tham số thứ mà có thể che giấu hay tiết lộ khác nhau các khía cạnh của điện năng
hồ sơ (profile) (Sliding-window averages over repeated inferences smooth these fluctuations into actionable efficiency numbers, but the window size itself becomes a design parameter that can hide or reveal different aspects of the power profile).
Bộ nhớ truy cập các mẫu làm phức tạp (compound) sự đo lường vấn đề bởi vì ML các hệ thống thường tiêu tốn
nhiều hơn năng lượng (trong) việc di chuyển dữ liệu hơn việc tính toán trên nó (Memory access patterns compound the measurement problem because ML systems often spend more energy moving data than computing on it). Sự giới thiệu các mô hình giống như DLRM, cho ví dụ,
có thể tiêu thụ nhiều hơn năng lượng trên bộ nhớ sự truy cập hơn sự tính toán—một mẫu thứ mà truyền thống tập trung-
vào tính toán điện năng sự đo lường bỏ lỡ hoàn toàn (Recommendation models like DLRM, for example, can consume more energy on memory access than computation—a pattern that traditional compute-focused power measurement misses entirely). Việc nắm bắt cả hai tính toán và bộ nhớ hệ thống con (subsystem)
điện năng sự tiêu thụ yêu cầu việc trang bị (instrumenting) đầy đủ dữ liệu đường dẫn, không chỉ bộ xử lý (Capturing both compute and memory subsystem power consumption requires instrumenting the full data path, not just the processor).
Không đồng nhất máy gia tốc các cấu hình giới thiệu xa hơn tính phức tạp (Heterogeneous accelerator configurations introduce further complexity). GPUs, TPUs, và NPUs
mỗi (thiết bị) duy trì độc lập điện năng sự quản lý các cơ sở (schemes), và hiện đại SoCs một cách động chuyển mạch
giữa tính toán các tài nguyên dựa trên trên khối lượng công việc các đặc điểm (GPUs, TPUs, and NPUs each maintain independent power management schemes, and modern SoCs dynamically switch between compute resources based on workload characteristics). Chính xác cấp độ-hệ thống sự đo lường
yêu cầu được đồng bộ hóa điện năng sự nắm bắt qua tất cả chủ động tính toán các đơn vị—một thách thức thứ mà mở rộng quy mô với
hệ thống kích thước (Accurate system-level measurement requires synchronized power capture across all active compute units—a challenge that scales with system size). Đa-GPU các cấu hình phải tính đến cho gradient sự đồng bộ hóa năng lượng bên cạnh
sự tính toán, và đa-nút các sự triển khai thêm không tầm thường mạng cơ sở hạ tầng điện năng (Multi-GPU configurations must account for gradient synchronization energy alongside computation, and multi-node deployments add nontrivial network infrastructure power). Tại (phía) khác
cực đoan, biên các sự triển khai phải nắm bắt năng lượng chi phí của mô hình các bản cập nhật và dữ liệu sự tiền xử lý
bên cạnh suy luận chính nó (At the other extreme, edge deployments must capture the energy cost of model updates and data preprocessing alongside inference itself).
Lô kích thước tạo ra một phi tuyến tính mối quan hệ với điện năng sự tiêu thụ thứ mà đơn-điểm các sự đo-
lường không thể đặc trưng hóa (Batch size creates a nonlinear relationship with power consumption that single-point measurements cannot characterize). Lớn hơn các lô cải thiện tính toán tính hiệu quả (tốt hơn sự khấu hao (amortization) của
bộ nhớ các lượt tải) nhưng làm tăng bộ nhớ áp lực và đỉnh điện năng các yêu cầu, việc có nghĩa (rằng) nhất hiệu-
quả lô kích thước cho thông lượng có thể khác biệt từ nhất hiệu quả lô kích thước cho năng lượng (Larger batches improve compute efficiency (better amortization of memory loads) but increase memory pressure and peak power requirements, meaning the most efficient batch size for throughput may differ from the most efficient batch size for energy). Sự đo lường
qua nhiều lô các kích thước là thiết yếu cho một hoàn chỉnh tính hiệu quả hồ sơ (profile) (Measurement across multiple batch sizes is essential for a complete efficiency profile). Hệ thống nhàn rỗi các trạng thái xứng đáng (được)
công bằng sự chú ý, đặc biệt cho gián đoạn biên các khối lượng công việc: một đánh thức-từ (wake-word) sự phát hiện TinyML hệ thống
thứ mà một cách chủ động xử lý âm thanh cho chỉ một nhỏ phần của hoạt động thời gian có thể bị thống trị bởi
nhàn rỗi điện năng sự tiêu thụ thay vì suy luận năng lượng (System idle states deserve equal attention, particularly for intermittent edge workloads: a wake-word detection TinyML system that actively processes audio for only a small fraction of operating time may be dominated by idle power consumption rather than inference energy). Cuối cùng, được duy trì ML các khối lượng công việc có thể gây ra
nhiệt độ các sự tăng thứ mà kích hoạt nhiệt sự điều tiết và thay đổi điện năng sự tiêu thụ các mẫu—một
hiệu ứng đặc biệt cấp tính (acute) trong biên các thiết bị, nơi nhiệt các sự ràng buộc giới hạn được duy trì hiệu suất và
làm cho được mở rộng việc đo điểm chuẩn các lượt chạy (trở nên) thiết yếu cho thực tế sự đặc trưng hóa (Finally, sustained ML workloads can cause temperature increases that trigger thermal throttling and alter power consumption patterns—an effect particularly acute in edge devices, where thermal constraints limit sustained performance and make extended benchmarking runs essential for realistic characterization).
12.9.4 MLPerf điện năng trường hợp nghiên cứu (MLPerf power case study)
MLPerf Điện năng (Tschand et al. 2024) biến đổi điện năng sự đo lường từ một cụ thể-thiết bị sự đọc vào một
có thể so sánh tính hiệu quả tuyên bố: bao nhiêu hữu ích các suy luận một hệ thống phân phối mỗi watt dưới một được định nghĩa
ranh giới (MLPerf Power (Tschand et al. 2024) turns power measurement from a device-specific reading into a comparable efficiency claim: how many useful inferences a system delivers per watt under a defined boundary). Phương pháp luận áp dụng được chuẩn hóa sự đánh giá các nguyên tắc qua dữ liệu trung tâm, biên,
và nhỏ bé suy luận các cài đặt, nơi liên quan quyết định thay đổi từ giá đỡ hoạt động chi phí tới pin
tuổi thọ tới quy mô-microwatt sức chịu đựng (endurance) (The methodology applies standardized evaluation principles across data center, edge, and tiny inference settings, where the relevant decision changes from rack operating cost to battery life to microwatt-scale endurance).
Nhận thức-ranh giới (Boundary-aware) sự chuẩn hóa quan trọng bởi vì giống nhau phần cứng gia đình có thể trông hiệu quả hay
lãng phí phụ thuộc trên ranh giới và khối lượng công việc (Boundary-aware standardization matters because the same hardware family can look efficient or wasteful depending on boundary and workload). Bằng cách việc thích ứng giao thức tới CPUs, các máy gia tốc,
và không đồng nhất các hệ thống trong khi việc bảo tồn sự đo lường tính toàn vẹn, MLPerf Điện năng làm cho chéo-
nền tảng các sự so sánh (trở nên) có ý nghĩa qua khác nhau việc tính toán các quy mô (By adapting the protocol to CPUs, accelerators, and heterogeneous systems while preserving measurement integrity, MLPerf Power makes cross-platform comparisons meaningful across different computing scales).
Điểm chuẩn đã tích lũy nhiều có thể tái tạo các sự đo lường được đệ trình bởi công nghiệp các tổ-
chức, việc chứng minh được đệ trình phần cứng các khả năng và toàn-ngành-vực (sector-wide) trọng tâm trên hiệu quả-năng lượng
AI công nghệ (The benchmark has accumulated many reproducible measurements submitted by industry organizations, demonstrating submitted hardware capabilities and the sector-wide focus on energy-efficient AI technology). Dữ liệu-trung tâm bảng điều khiển trong hình 12.8 cho thấy cách nào được chuẩn hóa năng lượng tính hiệu quả đã
tiến hóa qua liên tiếp MLPerf Suy luận các phiên bản (The data-center panel in figure 12.8 shows how normalized energy efficiency has evolved across successive MLPerf Inference versions). Các lợi ích là không đồng đều (uniform) qua các khối lượng công việc:
được thiết lập thị giác, ngôn ngữ, sự giới thiệu, và lời nói các điểm chuẩn cải thiện một cách khiêm tốn sau
của chúng sớm các sự phát hành, trong khi mới hơn tạo sinh-mô hình các khối lượng công việc cho thấy lớn hơn các bước nhảy khi các hệ thống trưởng thành (The gains are not uniform across workloads: established vision, language, recommendation, and speech benchmarks improve modestly after their early releases, while newer generative-model workloads show larger jumps as systems mature).
Sự phân tích của dữ liệu-trung tâm MLPerf Điện năng các xu hướng tiết lộ hai đáng chú ý các mẫu (Analysis of the data-center MLPerf Power trends reveals two notable patterns). Đầu tiên, năng lượng
tính hiệu quả các sự cải thiện cho được thiết lập ML các khối lượng công việc, bao gồm hình ảnh phân loại, ngôn ngữ
sự hiểu biết, sự giới thiệu, và hồi quy thần kinh mạng (recurrent neural network) (RNN) dựa trên lời nói sự nhận dạng
(cụ thể ResNet, BERT, DLRM, RetinaNet, và RNN-T), đã đi ngang (plateaued) sau ban đầu các lợi ích;
thấp-treo trái cây (low-hanging fruit) của sự tối ưu hóa đã được thu hoạch (First, energy efficiency improvements for established ML workloads, including image classification, language understanding, recommendation, and recurrent neural network (RNN) based speech recognition (specifically ResNet, BERT, DLRM, RetinaNet, and RNN-T), have plateaued after initial gains; the low-hanging fruit of optimization has been harvested). Thứ hai, lớn tạo sinh-mô hình các khối lượng công việc (Second, large generative-model workloads)

690
12.10 Việc đo điểm chuẩn Tốt nhất Các thực tiễn (Benchmarking Best Practices)
Hình 12.8: Dữ liệu-Trung tâm Năng lượng Tính hiệu quả Các lợi ích (Data-Center Energy Efficiency Gains): Liên tiếp MLPerf Suy luận điểm chuẩn các phiên bản cho thấy được chuẩn hóa năng lượng
tính hiệu quả (các mẫu mỗi joule) qua dữ liệu-trung tâm các khối lượng công việc (Successive MLPerf Inference benchmark versions show normalized energy efficiency (samples per joule) across data-center workloads). Được thiết lập thị giác, ngôn ngữ, sự giới thiệu, và lời nói
các khối lượng công việc cải thiện một cách khiêm tốn sau sớm các sự phát hành, trong khi mới hơn tạo sinh-mô hình các điểm chuẩn chẳng hạn như GPT-J và Llama 2 cho thấy
lớn hơn các lợi ích khi các hệ thống trưởng thành (Established vision, language, recommendation, and speech workloads improve modestly after early releases, while newer generative-model benchmarks such as GPT-J and Llama 2 show larger gains as systems mature). Nguồn: (Tschand et al. 2024).
cho thấy nhiều lớn hơn gần đây tính hiệu quả các sự tăng, việc phản ánh nhanh chóng sự tối ưu hóa khi các nhà nghiên cứu và hệ thống
các nhà xây dựng tinh chỉnh mới hơn, lớn hơn các mô hình (Tschand et al. 2024) (show much larger recent efficiency increases, reflecting rapid optimization as researchers and system builders tune newer, larger models (Tschand et al. 2024)). Này sự phân đôi (dichotomy) gợi ý rằng được thiết lập
các khối lượng công việc có thể đạt tới sự tối ưu hóa sự trưởng thành trong khi mới hơn mô hình các lớp vẫn cung cấp đáng kể tính hiệu quả
khoảng không (headroom), một mẫu nhiều khả năng để lặp lại khi mỗi kiến trúc trưởng thành (This dichotomy suggests that established workloads can reach optimization maturity while newer model classes still offer substantial efficiency headroom, a pattern likely to repeat as each architecture matures).
Định thời gian các giao thức và điện năng thiết bị đo đạc cung cấp thô dữ liệu cho việc đo điểm chuẩn (Timing protocols and power instrumentation provide the raw data for benchmarking). Thô dữ liệu
một mình, tuy nhiên, không đảm bảo vững chắc (sound) các kết luận (Raw data alone, however, does not guarantee sound conclusions). Việc chuyển đổi các sự đo lường vào có ý nghĩa
các sự so sánh yêu cầu việc hiểu có hệ thống các nguồn của lỗi, sự thiên vị, và sự sai lệch (misalignment) thứ mà
có thể làm cho thậm chí một cách cẩn thận được thu thập điểm chuẩn các con số (trở nên) gây hiểu lầm (Converting measurements into meaningful comparisons requires understanding the systematic sources of error, bias, and misalignment that can make even carefully collected benchmark numbers misleading).
12.10 Việc đo điểm chuẩn Tốt nhất Các thực tiễn (Benchmarking Best Practices)
Một suy luận ngăn xếp thứ mà vượt qua một trạng thái-ổn định (steady-state) phòng thí nghiệm lượt chạy có thể vẫn lỡ độ trễ các mục tiêu khi sản-
xuất lưu lượng đến trong các đợt (bursts), hoặc khi đầu vào hỗn hợp dịch chuyển hướng tới đắt đỏ các ví dụ (An inference stack that passes a steady-state lab run can still miss latency targets when production traffic arrives in bursts, or when the input mix shifts toward expensive examples). Huấn luyện
thông lượng, suy luận độ trễ, và điện năng tính hiệu quả mỗi (cái) có được thiết lập sự đo lường các giao thức
được xác nhận thông qua MLPerf, nhưng việc biết cái gì để đo lường là không đủ mà không có việc hiểu
cái gì các điểm chuẩn không thể nắm bắt và tại sao này khoảng cách đã làm trật bánh (derailed) vô số các sự triển khai (Training throughput, inference latency, and power efficiency each have established measurement protocols validated through MLPerf, but knowing what to measure is insufficient without understanding what benchmarks cannot capture and why this gap has derailed countless deployments).
Mỗi điểm chuẩn thực hiện việc đơn giản hóa các giả định thứ mà kích hoạt được chuẩn hóa sự so sánh nhưng
phân kỳ (diverge) từ sản xuất thực tế (Every benchmark makes simplifying assumptions that enable standardized comparison but diverge from production reality). Huấn luyện các điểm chuẩn giả định cố định các tập dữ liệu và có thể tái tạo
ngẫu nhiên các hạt giống (seeds); sản xuất dữ liệu trôi dạt (drifts) một cách liên tục (Training benchmarks assume fixed datasets and reproducible random seeds; production data drifts continuously). Suy luận các điểm chuẩn giả định trạng thái-ổn định
hoạt động; sản xuất lưu lượng tăng vọt (spikes) một cách không thể dự đoán được (Inference benchmarks assume steady-state operation; production traffic spikes unpredictably). Điện năng các điểm chuẩn giả định được kiểm soát nhiệt
các môi trường; thực tế phần cứng điều tiết (throttles) dưới được duy trì tải (Power benchmarks assume controlled thermal environments; real hardware throttles under sustained load). Bốn các thể loại của các sự giới hạn (thuộc về thống kê,
liên quan-tới-sự triển khai, hệ thống thiết kế, và thuộc về tổ chức) xác định liệu điểm chuẩn các kết quả
chuyển dịch (translate) tới sự triển khai thành công (Four categories of limitations (statistical, deployment-related, system design, and organizational) determine whether benchmark results translate to deployment success).
12.10.1 Thuộc về thống kê và thuộc về phương pháp luận các vấn đề (Statistical and methodological issues)
Điểm chuẩn các kết quả là chỉ đáng tin cậy như các sự đo lường thứ mà tạo ra chúng (Benchmark results are only as reliable as the measurements that produce them). Ba lan tràn (pervasive)
các vấn đề làm suy yếu này độ tin cậy nếu bị bỏ lại không được giải quyết (Three pervasive issues undermine this reliability if left unaddressed).
Không hoàn chỉnh vấn đề độ bao phủ đại diện cho một trong những nhất lan tràn các sự giới hạn (Incomplete problem coverage represents one of the most pervasive limitations). Nhiều các điểm chuẩn,
trong khi hữu ích cho được kiểm soát các sự so sánh, thất bại để nắm bắt đầy đủ sự đa dạng của thế giới-thực các ứng dụng (Many benchmarks, while useful for controlled comparisons, fail to capture the full diversity of real-world applications).
Chung hình ảnh phân loại các tập dữ liệu chẳng hạn như CIFAR-10 (Krizhevsky 2009) chứa một bị giới hạn sự đa dạng
của các hình ảnh (Common image classification datasets such as CIFAR-10 (Krizhevsky 2009) contain a limited variety of images). Các mô hình thứ mà biểu diễn tốt trên những các tập dữ liệu này có thể chật vật khi được áp dụng tới nhiều hơn phức tạp,
thế giới-thực các kịch bản với lớn hơn tính biến thiên trong ánh sáng, phối cảnh (perspective), và đối tượng thành phần (composition) (Models that perform well on these datasets may struggle when applied to more complex, real-world scenarios with greater variability in lighting, perspective, and object composition). Này
khoảng cách giữa điểm chuẩn các tác vụ và thế giới-thực tính phức tạp có nghĩa (rằng) mạnh mẽ điểm chuẩn hiệu suất
cung cấp bị giới hạn các sự đảm bảo về thực tế sự triển khai thành công (This gap between benchmark tasks and real-world complexity means strong benchmark performance provides limited guarantees about practical deployment success).
Thuộc về thống kê sự không có ý nghĩa (insignificance) phát sinh khi điểm chuẩn các sự đánh giá được tiến hành trên quá ít dữ liệu các mẫu
hay các thử nghiệm, và nó là nhất cấp tính (acute) trong các cài đặt nơi sự đánh giá phương tiện (medium) chính nó giới thiệu phương sai (Statistical insignificance arises when benchmark evaluations are conducted on too few data samples or trials, and it is most acute in settings where the evaluation medium itself introduces variance).

12. Việc đo điểm chuẩn (Benchmarking)
691
34
Phần cứng
Xổ số (Lottery):
Được đặt ra (Coined) bởi Hooker (2021) để
mô tả cách nào thuộc về thuật toán thành-
công phụ thuộc trên sự căn chỉnh (alignment)
với có sẵn phần cứng (Coined by Hooker (2021) to describe how algorithmic success depends on alignment with available hardware).
transformer đã thành công một phần
bởi vì của nó dày đặc ma trận các phép-
nhân ánh xạ tốt tới GPU
Tensor Các lõi (Cores), trong khi đồ thị
thần kinh các mạng và thưa thớt
hỗn hợp-của-các chuyên gia (mixture-of-experts)
các mô hình
có thể là khó hơn để đánh giá
khi có sẵn silicon và
phần mềm các ngăn xếp thiên vị dày đặc
các hạt nhân (The transformer succeeded partly because its dense matrix multiplications map well to GPU Tensor Cores, while graph neural networks and sparse mixture-of-experts models can be harder to evaluate when available silicon and software stacks favor dense kernels).
Cho việc đo điểm chuẩn,
này có nghĩa (rằng) cụ thể-phần cứng
các bảng xếp hạng một cách có hệ thống
thiên vị
được căn chỉnh-phần cứng
các kiến trúc,
một cách tiềm năng
việc che khuất (obscuring)
các thuật toán
thứ mà
sẽ
biểu diễn
tốt hơn
dưới
khác nhau
phần cứng
các giả định (For benchmarking, this means hardware-specific leaderboards systematically favor hardware-aligned architectures, potentially obscuring algorithms that would perform better under different hardware assumptions).
Lớn ngôn ngữ mô hình sự đánh giá làm ví dụ cho này vấn đề: liệu việc chấm điểm một mới LLM chống lại
một tham chiếu việc sử dụng con người sở thích các đánh giá (ratings) hay một LLM-như-giám khảo (LLM-as-judge) giao thức, sự đánh giá tín hiệu
mang cao phương sai bởi vì các giám khảo phản hồi một cách khác biệt tới dấu nhắc (prompt) cách diễn đạt (phrasing), việc đặt hàng (ordering) các hiệu ứng, và
phản hồi độ dài (Large language model evaluation exemplifies this problem: whether scoring a new LLM against a reference using human preference ratings or an LLM-as-judge protocol, the evaluation signal carries high variance because judges respond differently to prompt phrasing, ordering effects, and response length). Một được báo cáo hai-điểm sở thích chiến thắng (win) có thể biến mất hoàn toàn qua một khác nhau
giám khảo cấu hình hay dấu nhắc mẫu (A reported two-point preference win can disappear entirely across a different judge configuration or prompt template). Nghiêm ngặt LLM việc đo điểm chuẩn do đó yêu cầu thuộc về thống-
kê các phương pháp—bootstrap độ tin cậy các khoảng hay được ghép nối (paired) ý nghĩa các bài kiểm tra—được áp dụng qua đủ
các dấu nhắc và phản hồi các sự ghép cặp (pairings) để tách biệt một đích thực khả năng sự cải thiện từ sự đánh giá tiếng ồn (Rigorous LLM benchmarking therefore requires statistical methods—bootstrap confidence intervals or paired significance tests—applied across enough prompts and response pairings to separate a genuine capability improvement from evaluation noise).
Mà không có đủ các thử nghiệm và đa dạng đầu vào các sự phân phối, việc đo điểm chuẩn các kết quả sẽ gây hiểu lầm: được báo cáo
các sự khác biệt phản ánh sự đánh giá tiếng ồn thay vì đích thực khả năng (Without sufficient trials and diverse input distributions, benchmarking results will mislead: reported differences reflect evaluation noise rather than genuine capability). Thuộc về thống kê độ tin cậy các khoảng
xung quanh điểm chuẩn các điểm số thường đi không được báo cáo, việc che khuất (obscuring) liệu được đo lường các sự khác biệt (có) đại diện cho
đích thực các sự cải thiện hay sự đo lường tiếng ồn (The statistical confidence intervals around benchmark scores often go unreported, obscuring whether measured differences represent genuine improvements or measurement noise).
Tính có thể tái tạo đại diện cho một chính đang diễn ra thách thức (Reproducibility represents a major ongoing challenge). Điểm chuẩn các kết quả có thể biến đổi một cách có thể đo lường được
phụ thuộc trên các yếu tố chẳng hạn như phần cứng các cấu hình, phần mềm các phiên bản, và hệ thống các sự phụ thuộc (Benchmark results can vary measurably depending on factors such as hardware configurations, software versions, and system dependencies).
Nhỏ các sự khác biệt trong các trình biên dịch, thuộc về số độ chính xác, hay thư viện các bản cập nhật có thể dẫn tới không nhất quán
hiệu suất các sự đo lường qua khác nhau các môi trường (Small differences in compilers, numerical precision, or library updates can lead to inconsistent performance measurements across different environments). Để giảm nhẹ này vấn đề, MLPerf giải quyết
tính có thể tái tạo bằng cách việc cung cấp tham chiếu các sự triển khai, được chuẩn hóa bài kiểm tra các môi trường, và nghiêm ngặt
sự đệ trình các hướng dẫn (To mitigate this issue, MLPerf addresses reproducibility by providing reference implementations, standardized test environments, and strict submission guidelines). Thậm chí với những các nỗ lực này, việc đạt được thực sự tính nhất quán qua đa dạng phần cứng
các nền tảng duy trì (remains) một đang diễn ra thách thức (Even with these efforts, achieving true consistency across diverse hardware platforms remains an ongoing challenge). Sự tăng sinh (proliferation) của sự tối ưu hóa các thư viện, bộ khung
các phiên bản, và trình biên dịch các cờ (flags) tạo ra một rộng lớn cấu hình không gian nơi nhẹ các sự biến thiên tạo ra
khác nhau các kết quả (The proliferation of optimization libraries, framework versions, and compiler flags creates a vast configuration space where slight variations produce different results).
12.10.2 Phòng thí nghiệm-tới-sự triển khai hiệu suất các khoảng cách (Laboratory-to-deployment performance gaps)
Thuộc về thống kê sự nghiêm ngặt đảm bảo rằng điểm chuẩn các sự đo lường là chính xác (Statistical rigor ensures that benchmark measurements are accurate). Chính xác các sự đo lường của
sai thứ, tuy nhiên, vẫn dẫn tới sự triển khai các thất bại (Accurate measurements of the wrong thing, however, still lead to deployment failures). Các điểm chuẩn phải cũng căn chỉnh với thực tế
sự triển khai các mục tiêu (Benchmarks must also align with practical deployment objectives).
Sự sai lệch (Misalignment) với thế giới-thực các mục tiêu xảy ra khi các điểm chuẩn nhấn mạnh các số liệu chẳng hạn như tốc độ,
độ chính xác, và thông lượng, trong khi thực tế AI các sự triển khai yêu cầu việc cân bằng nhiều các mục tiêu
bao gồm điện năng tính hiệu quả, chi phí, và tính mạnh mẽ (Misalignment with real-world goals occurs when benchmarks emphasize metrics such as speed, accuracy, and throughput, while practical AI deployments require balancing multiple objectives including power efficiency, cost, and robustness). Một mô hình thứ mà đạt được trên-cùng-dòng (top-line) độ chính xác trên một
điểm chuẩn có thể là không thực tế cho sự triển khai nếu nó tiêu thụ quá mức năng lượng hay yêu cầu đắt đỏ
phần cứng (A model that achieves top-line accuracy on a benchmark may be impractical for deployment if it consumes excessive energy or requires expensive hardware). Một cách tương tự, việc tối ưu hóa cho trung bình-trường hợp hiệu suất trên điểm chuẩn các tập dữ liệu có thể bỏ bê (neglect)
đuôi-độ trễ các yêu cầu thứ mà xác định người dùng trải nghiệm trong sản xuất các hệ thống (Similarly, optimizing for average-case performance on benchmark datasets may neglect tail-latency requirements that determine user experience in production systems). Đa-mục tiêu
bản chất của thực sự sự triển khai, việc bao trùm (encompassing) tài nguyên các sự ràng buộc, hoạt động các chi phí, bảo trì
tính phức tạp, và kinh doanh các yêu cầu, mở rộng xa vượt ra ngoài đơn-số liệu sự tối ưu hóa thứ mà hầu hết
các điểm chuẩn khen thưởng (The multi-objective nature of real deployment, encompassing resource constraints, operational costs, maintenance complexity, and business requirements, extends far beyond the single-metric optimization that most benchmarks reward).
12.10.3 Hệ thống thiết kế các thách thức (System design challenges)
Thuộc về thống kê phương pháp luận và sự triển khai sự căn chỉnh giải quyết cách nào chúng ta đo lường và cái gì chúng ta tối ưu hóa
cho (Statistical methodology and deployment alignment address how we measure and what we optimize for). Một thứ ba thể loại của các sự giới hạn nổi lên từ vật lý các hệ thống đang được đo lường (A third category of limitations emerges from the physical systems being measured). Phần cứng
hành vi phụ thuộc trên thuộc về môi trường các điều kiện, thuộc về kiến trúc tính tương thích, và hoạt động ngữ cảnh
theo các cách thứ mà làm phức tạp công bằng sự so sánh (Hardware behavior depends on environmental conditions, architectural compatibility, and operational context in ways that complicate fair comparison).
Thuộc về môi trường các điều kiện ảnh hưởng các điểm chuẩn theo có thể đo lường được các cách (Environmental conditions affect benchmarks in measurable ways). Điểm chuẩn các kết quả phụ thuộc trên
vật lý các điều kiện (môi trường xung quanh (ambient) nhiệt độ, độ ẩm, độ cao (altitude)) và hoạt động ngữ cảnh (nền tảng
các quá trình, mạng tải, điện năng nguồn cung cấp (supply) tính ổn định) theo tinh tế nhưng có thể đo lường được các cách (Benchmark results depend on physical conditions (ambient temperature, humidity, altitude) and operational context (background processes, network load, power supply stability) in subtle but measurable ways). Tăng cao các nhiệt-
độ kích hoạt nhiệt sự điều tiết thứ mà giảm thuộc về tính toán tốc độ; nền tảng các quá trình cạnh tranh
cho các tài nguyên và thay đổi hiệu suất các đặc điểm (Elevated temperatures trigger thermal throttling that reduces computational speed; background processes compete for resources and alter performance characteristics). Việc đảm bảo hợp lệ các điểm chuẩn yêu cầu việc kiểm soát
những các yếu tố này tới mức độ (extent) có thể (được kiểm soát-nhiệt độ các môi trường, được chuẩn hóa hệ thống
các trạng thái, được tài liệu hóa nền tảng các lượt tải) và, khi đầy đủ sự kiểm soát là không thực tế (như trong được phân phối hay
dựa trên-đám mây việc đo điểm chuẩn), chi tiết việc báo cáo của các điều kiện do đó rằng (những) người khác có thể tính đến cho tiềm năng
các sự biến thiên khi việc diễn giải các kết quả (Ensuring valid benchmarks requires controlling these factors to the extent possible (temperature-controlled environments, standardized system states, documented background loads) and, when full control is impractical (as in distributed or cloud-based benchmarking), detailed reporting of conditions so that others can account for potential variations when interpreting results).
Phần cứng xổ số34 (Hooker 2021) đưa ra một khác chí mạng vấn đề (The hardware lottery34 (Hooker 2021) presents another critical issue). Sự thành công của một máy
học mô hình là thường được ra lệnh (dictated) không chỉ bởi của nó kiến trúc và huấn luyện dữ liệu nhưng cũng bởi cách nào tốt nó
căn chỉnh với nằm dưới phần cứng (The success of a machine learning model is often dictated not only by its architecture and training data but also by how well it aligns with the underlying hardware). Một vài các mô hình biểu diễn một cách ngoại lệ tốt không phải bởi vì chúng là
vốn dĩ vượt trội nhưng bởi vì chúng ánh xạ một cách tự nhiên lên trên GPU hay TPU song song việc xử lý các khả năng (Some models perform exceptionally well not because they are inherently superior but because they map naturally onto GPU or TPU parallel processing capabilities).
Khác đầy hứa hẹn các kiến trúc có thể bị một cách có hệ thống bỏ qua (overlooked) bởi vì chúng không khớp chiếm ưu thế
phần cứng các nền tảng (Other promising architectures may be systematically overlooked because they do not fit dominant hardware platforms).

692
12.10 Việc đo điểm chuẩn Tốt nhất Các thực tiễn (Benchmarking Best Practices)
Phần cứng tính tương thích sự phụ thuộc giới thiệu tinh tế nhưng đáng kể các sự thiên vị vào việc đo điểm chuẩn
các kết quả (Hardware compatibility dependence introduces subtle but significant biases into benchmarking results). Một mô hình thứ mà là một cách cao độ hiệu quả trên một cụ thể GPU có thể biểu diễn kém trên một CPU hay một
tùy chỉnh AI máy gia tốc (A model that is highly efficient on a specific GPU may perform poorly on a CPU or a custom AI accelerator). Hình 12.9 làm cho này phần cứng sự phụ thuộc (trở nên) cụ thể bằng cách việc so sánh mô hình
hiệu suất qua khác nhau các nền tảng (Figure 12.9 makes this hardware dependence concrete by comparing model performance across different platforms). Trên CPU uint8 và GPU các cấu hình, đa-
phần cứng (multi-hardware) các mô hình theo dõi “MobileNetV3 Lớn min” cơ sở một cách chặt chẽ, việc đạt tới xấp xỉ 77 phần trăm
top-1 ImageNet độ chính xác nơi cơ sở đạt tới khoảng 75 phần trăm (On the CPU uint8 and GPU configurations, the multi-hardware models track the “MobileNetV3 Large min” baseline closely, reaching roughly 77 percent top-1 ImageNet accuracy where the baseline reaches about 75 percent). Trên EdgeTPU và DSP
phần cứng giống nhau đa-phần cứng các mô hình duy trì đó 77 phần trăm tại một cách đáng kể thấp hơn độ trễ,
trong khi một mô hình được tinh chỉnh chỉ cho CPU sẽ từ bỏ (forfeit) những các lợi ích đó (On the EdgeTPU and DSP hardware the same multi-hardware models sustain that 77 percent at substantially lower latency, while a model tuned only for the CPU would forfeit those gains). Này tiết lộ rằng “tốt nhất” mô hình
phụ thuộc hoàn toàn trên sự triển khai mục tiêu: một kết luận không thể để đạt tới từ đơn-nền tảng
các điểm chuẩn (This reveals that the “best” model depends entirely on deployment target: a conclusion impossible to reach from single-platform benchmarks).
25
50
75
100
0.70
0.72
0.74
0.76
0.78
Pixel4 CPU Float độ trễ (latency)
Top-1 ImageNet Độ chính xác (Acc)
10
20
30
0.70
0.72
0.74
0.76
0.78
Pixel4 CPU Uint8 độ trễ (latency)
Top-1 ImageNet Độ chính xác (Acc)
2.5
5.0
7.5
10.0
12.5
0.70
0.72
0.74
0.76
0.78
Pixel4 GPU Adreno 640 độ trễ (latency)
Top-1 ImageNet Độ chính xác (Acc)
2.0
2.5
3.0
3.5
0.70
0.72
0.74
0.76
0.78
Pixel4 EdgeTPU độ trễ (latency)
Top-1 ImageNet Độ chính xác (Acc)
3
4
5
6
0.70
0.72
0.74
0.76
0.78
Pixel4 DSP Qualcomm Snapdragon 855 độ trễ (latency)
Top-1 ImageNet Độ chính xác (Acc)
Mobilenet V1
Mobilenet V2
Mobilenet V3 Lớn (Large)
Mobilenet V3 Lớn min (Large min)
Mobilenet-EdgeTPU
ProxylessNAS-Di động (Mobile)
Đa-MAX (Multi-MAX)
Đa-AVG (Multi-AVG)
Hình 12.9: Phụ thuộc-Phần cứng Độ chính xác (Hardware-Dependent Accuracy): Mô hình hiệu suất biến đổi một cách đáng kể qua phần cứng các nền tảng, việc chỉ ra
rằng thuộc về kiến trúc tính hiệu quả là không duy nhất được xác định bởi thiết kế nhưng cũng bởi phần cứng tính tương thích (Model performance varies significantly across hardware platforms, indicating that architectural efficiency is not solely determined by design but also by hardware compatibility). Đa-phần cứng các mô hình
phô bày (exhibit) có thể so sánh độ chính xác tới MobileNetV3 Lớn trên CPU và GPU các cấu hình, tuy nhiên đạt được đáng kể các lợi ích trên EdgeTPU
và DSP, việc nhấn mạnh tầm quan trọng của nhận thức-phần cứng (hardware-aware) mô hình sự tối ưu hóa cho chuyên biệt việc tính toán các môi trường (Multi-hardware models exhibit comparable accuracy to MobileNetV3 Large on CPU and GPU configurations, yet achieve substantial gains on EdgeTPU and DSP, emphasizing the importance of hardware-aware model optimization for specialized computing environments). Nguồn (Source):
(Chu et al. 2021).
Mà không có cẩn thận việc đo điểm chuẩn qua đa dạng phần cứng các cấu hình, lĩnh vực có nguy cơ (risks) việc thiên vị
các kiến trúc thứ mà “chiến thắng” phần cứng xổ số thay vì việc lựa chọn các mô hình dựa trên trên của chúng nội tại (intrinsic)
các sức mạnh (Without careful benchmarking across diverse hardware configurations, the field risks favoring architectures that “win” the hardware lottery rather than selecting models based on their intrinsic strengths). Này sự thiên vị có thể định hình nghiên cứu các hướng, ảnh hưởng tài trợ (funding) sự phân bổ (allocation), và tác động
thiết kế của thế hệ-tiếp theo AI các hệ thống (This bias can shape research directions, influence funding allocation, and impact the design of next-generation AI systems). Trong cực đoan các trường hợp, nó có thể thậm chí bóp nghẹt (stifle) sự đổi mới bằng cách việc làm nản lòng
sự khám phá của thay thế các kiến trúc thứ mà không căn chỉnh với hiện tại phần cứng các xu hướng (In extreme cases, it may even stifle innovation by discouraging exploration of alternative architectures that do not align with current hardware trends).
12.10.4 Thuộc về tổ chức và thuộc về chiến lược các vấn đề (Organizational and strategic issues)
Các trước đó các sự giới hạn phát sinh từ kỹ thuật các thách thức: thuộc về thống kê tiếng ồn, sự triển khai sự sai-
lệch, thuộc về môi trường phương sai, và phần cứng tính tương thích (The preceding limitations arise from technical challenges: statistical noise, deployment misalignment, environmental variance, and hardware compatibility). Một thứ tư thể loại nổi lên từ con người
các yếu tố—và những (yếu tố) này có thể là khó nhất để giảm nhẹ bởi vì chúng liên quan tới các sự khuyến khích (incentives) thay vì
thiết bị đo đạc (A fourth category emerges from human factors—and these may be the hardest to mitigate because they involve incentives rather than instrumentation). Cạnh tranh các áp lực và nghiên cứu các sự khuyến khích tạo ra có hệ thống các sự thiên vị trong cách nào
các điểm chuẩn được sử dụng và được diễn giải (Competitive pressures and research incentives create systematic biases in how benchmarks are used and interpreted). Những thuộc về tổ chức các động lực này yêu cầu quản trị các cơ-
chế và cộng đồng các tiêu chuẩn để duy trì điểm chuẩn tính toàn vẹn (These organizational dynamics require governance mechanisms and community standards to maintain benchmark integrity).
12.10.4.1 Điểm chuẩn kỹ thuật (Benchmark engineering)
Trong khi phần cứng xổ số là một không có chủ ý (unintended) hậu quả của phần cứng các xu hướng, điểm chuẩn kỹ-
thuật là một có chủ ý (intentional) thực tiễn nơi các mô hình hay các hệ thống được một cách rõ ràng tối ưu hóa để xuất sắc trên cụ thể
điểm chuẩn các bài kiểm tra (While the hardware lottery is an unintended consequence of hardware trends, benchmark engineering is an intentional practice where models or systems are explicitly optimized to excel on specific benchmark tests). Này thực tiễn có thể dẫn tới gây hiểu lầm hiệu suất các tuyên bố và các kết quả thứ mà không
khái quát hóa vượt ra ngoài việc đo điểm chuẩn môi trường (This practice can lead to misleading performance claims and results that do not generalize beyond the benchmarking environment).

12. Việc đo điểm chuẩn (Benchmarking)
693
Điểm chuẩn kỹ thuật xảy ra khi AI các nhà phát triển tinh chỉnh các siêu tham số (hyperparameters), sự tiền xử lý
các kỹ thuật, hay mô hình các kiến trúc một cách cụ thể để tối đa hóa điểm chuẩn các điểm số thay vì cải thiện
thế giới-thực hiệu suất (Benchmark engineering occurs when AI developers fine-tune hyperparameters, preprocessing techniques, or model architectures specifically to maximize benchmark scores rather than improve real-world performance). Sự phân biệt giữa hợp pháp sự tối ưu hóa và điểm chuẩn kỹ-
thuật là thường mờ nhạt (blurry), việc ngồi tại ngưỡng (threshold) nơi việc tinh chỉnh cho một cụ thể điểm chuẩn vượt qua (crosses) vào
việc quá khớp (overfitting) tới nó (The distinction between legitimate optimization and benchmark engineering is often blurry, sitting at the threshold where tuning for a specific benchmark crosses into overfitting to it). Cho ví dụ, một đối tượng sự phát hiện mô hình có thể được một cách cẩn thận tối ưu hóa để đạt được
kỷ lục-thấp độ trễ trên một điểm chuẩn nhưng thất bại khi được triển khai trong động, thế giới-thực các môi trường
với việc biến đổi ánh sáng, chuyển động độ mờ (blur), và các sự che khuất (occlusions) (For example, an object detection model might be carefully optimized to achieve record-low latency on a benchmark but fail when deployed in dynamic, real-world environments with varying lighting, motion blur, and occlusions). Một cách tương tự, một ngôn ngữ mô hình có thể được tinh chỉnh để
xuất sắc trên điểm chuẩn các tập dữ liệu nhưng chật vật khi việc xử lý hội thoại lời nói với không chính thức
cách diễn đạt (phrasing) và mã-sự chuyển mạch (code-switching) (Similarly, a language model might be tuned to excel on benchmark datasets but struggle when processing conversational speech with informal phrasing and code-switching).
Áp lực để đạt được cao điểm chuẩn các điểm số là thường được thúc đẩy bởi sự cạnh tranh, tiếp thị, và
nghiên cứu sự công nhận (The pressure to achieve high benchmark scores is often driven by competition, marketing, and research recognition). Các điểm chuẩn được thường xuyên sử dụng để xếp hạng AI các mô hình và các hệ thống, việc tạo ra một
sự khuyến khích để tối ưu hóa một cách cụ thể cho chúng (Benchmarks are frequently used to rank AI models and systems, creating an incentive to optimize specifically for them). Trong khi này có thể thúc đẩy kỹ thuật các sự tiến bộ, nó cũng có nguy cơ
việc ưu tiên cụ thể-điểm chuẩn các sự tối ưu hóa tại chi phí của rộng hơn sự khái quát hóa—một cách chính xác
Goodhart’s Luật động lực được giới thiệu trong phần 12.1 và được minh họa với BLEU-điểm số ví dụ
trong phần 12.3.1 (While this can drive technical advancements, it also risks prioritizing benchmark-specific optimizations at the expense of broader generalization—precisely the Goodhart’s Law dynamic introduced in section 12.1 and illustrated with the BLEU-score example in section 12.3.1).
12.10.4.2 Sự thiên vị và quá-sự tối ưu hóa (Bias and over-optimization)
Người thực hành (practitioner) việc tiêu thụ một điểm chuẩn kết quả phải xác định liệu một con số phản ánh hợp-
pháp sự tối ưu hóa hay điểm chuẩn kỹ thuật (The practitioner consuming a benchmark result must determine whether a number reflects legitimate optimization or benchmark engineering). Một vài các thực tiễn làm cho đó có thể phân biệt được, và
mỗi (thực tiễn) bắt một cụ thể thất bại tại một cụ thể chi phí (Several practices make that distinguishable, and each catches a specific failure at a specific cost). Tính minh bạch là đầu tiên dòng của sự phòng thủ: một sự đệ-
trình thứ mà tài liệu hóa mọi sự tối ưu hóa được áp dụng để (lets) một người đọc tách biệt chung sự cải thiện
từ cụ thể-điểm chuẩn sự tinh chỉnh, tại chi phí của việc phơi bày các kỹ thuật một nhà cung cấp có thể thích để giữ
độc quyền (proprietary) (Transparency is the first line of defense: a submission that documents every optimization applied lets a reader separate general improvement from benchmark-specific tuning, at the cost of exposing techniques a vendor may prefer to keep proprietary). Việc báo cáo cả hai điểm chuẩn và thế giới-thực sự triển khai các kết quả đóng giống nhau khoảng cách từ
(phía) khác phía (Reporting both benchmark and real-world deployment results closes the same gap from the other side). Được đa dạng hóa sự đánh giá qua nhiều, một cách liên tục được cập nhật các điểm chuẩn nâng cao
chi phí của việc quá khớp tới bất kỳ đơn bài kiểm tra tập (nào), bởi vì một mô hình được thiết kế để chiến thắng một (bài kiểm tra) không thể dễ dàng chiến thắng
tất cả chúng; của nó chi phí là kỹ thuật nỗ lực của việc duy trì nhiều các điểm chuẩn (Diversified evaluation across multiple, continuously updated benchmarks raises the cost of overfitting to any single test set, because a model engineered to win one cannot easily win them all; its cost is the engineering effort of maintaining many benchmarks).
Sự chuẩn hóa và bên-thứ ba sự xác minh nâng cao rào cản xa hơn (Standardization and third-party verification raise the bar further). Độc lập các cuộc kiểm toán (audits) bắt các kết quả
thứ mà thất bại để tái tạo qua các cài đặt, và sự tồn tại bằng chứng cho này cơ chế xuất hiện hai
các phần sau đó trong MLPerf’s tham chiếu-so với-sự đệ trình sự xác nhận (phần 12.10.5), thứ mà loại bỏ (disqualifies)
bất kỳ sự đệ trình (nào) thứ mà không thể chạm (hit) tham chiếu độ chính xác mục tiêu (Independent audits catch results that fail to reproduce across settings, and the existence proof for this mechanism appears two sections later in MLPerf’s reference-vs-submission validation (section 12.10.5), which disqualifies any submission that cannot hit the reference accuracy target). Cụ thể-ứng dụng việc kiểm tra bắt
thất bại (mà) được kiểm soát các điểm chuẩn về mặt cấu trúc không thể (bắt): một tự trị-lái xe mô hình phải được rèn luyện (exercised)
qua thời tiết, ánh sáng, và đô thị các cài đặt nó sẽ thực tế gặp, không (được) đánh giá duy nhất trên một được tuyển chọn
tập dữ liệu (Application-specific testing catches the failure controlled benchmarks structurally cannot: an autonomous-driving model must be exercised across the weather, lighting, and urban settings it will actually meet, not judged solely on a curated dataset). Đa-phần cứng việc kiểm tra bắt cuối cùng trường hợp, hiệu suất thứ mà là thực sự phần cứng-xổ số
sự căn chỉnh thay vì mô hình chất lượng, bằng cách việc xác nhận rằng một kết quả không phụ thuộc trên tính tương thích
với một nền tảng (Multi-hardware testing catches the last case, performance that is really hardware-lottery alignment rather than model quality, by confirming that a result does not depend on compatibility with one platform).
12.10.4.3 Điểm chuẩn sự tiến hóa (Benchmark evolution)
Một dai dẳng thách thức trong việc đo điểm chuẩn là rằng các điểm chuẩn hiếm khi là tĩnh (A persistent challenge in benchmarking is that benchmarks are rarely static). Khi AI các hệ thống tiến hóa,
(do) vậy phải các điểm chuẩn thứ mà đánh giá chúng (As AI systems evolve, so must the benchmarks that evaluate them). Một hiệu suất mục tiêu thứ mà phân biệt tốt dưới
một thế hệ của các mô hình, phần cứng, và các ứng dụng có thể mất tính liên quan dưới (một thế hệ) khác (A performance target that discriminates well under one generation of models, hardware, and applications may lose relevance under another). Trong khi
các điểm chuẩn là thiết yếu cho việc theo dõi sự tiến bộ, chúng có thể cũng trở nên lỗi thời, việc dẫn tới quá-
sự tối ưu hóa cho cũ các số liệu thay vì thế giới-thực hiệu suất các sự cải thiện (While benchmarks are essential for tracking progress, they can also become outdated, leading to over-optimization for old metrics rather than real-world performance improvements).
Này sự tiến hóa là rõ ràng trong lịch sử của AI các điểm chuẩn (This evolution is evident in the history of AI benchmarks). Sớm mô hình các điểm chuẩn, cho ví dụ,
đã tập trung một cách nặng nề trên hình ảnh phân loại và đối tượng sự phát hiện, vì những (cái) này đã là một vài trong những đầu tiên một cách rộng rãi
được nghiên cứu sâu học tập các tác vụ (Early model benchmarks, for instance, focused heavily on image classification and object detection, as these were some of the first widely studied deep learning tasks). Tuy nhiên, khi AI mở rộng vào tự nhiên ngôn ngữ việc xử lý, sự giới-
thiệu các hệ thống, và tạo sinh AI, nó đã trở nên rõ ràng rằng những sớm các điểm chuẩn này không còn (no longer) phản ánh
nhất quan trọng các thách thức trong lĩnh vực (However, as AI expanded into natural language processing, recommendation systems, and generative AI, it became clear that these early benchmarks no longer reflected the most important challenges in the field). Trong sự phản hồi, mới các điểm chuẩn nổi lên để đo lường
ngôn ngữ sự hiểu biết (A. Wang et al. 2018, 2019) và tạo sinh AI (Liang et al. 2022) (In response, new benchmarks emerged to measure language understanding (A. Wang et al. 2018, 2019) and generative AI (Liang et al. 2022)).
Điểm chuẩn sự tiến hóa mở rộng vượt ra ngoài sự thêm vào của mới các tác vụ để bao trùm (encompass) mới các chiều của
hiệu suất sự đo lường (Benchmark evolution extends beyond the addition of new tasks to encompass new dimensions of performance measurement). Trong khi truyền thống AI các điểm chuẩn nhấn mạnh độ chính xác và thông lượng,
được triển khai các ứng dụng đòi hỏi sự đánh giá qua nhiều tiêu chí: tính công bằng, tính mạnh mẽ, tính có thể mở rộng quy mô,
và năng lượng tính hiệu quả (While traditional AI benchmarks emphasized accuracy and throughput, deployed applications demand evaluation across multiple criteria: fairness, robustness, scalability, and energy efficiency). Hình 12.10 làm cho những khác biệt (disparate) các yêu cầu này (trở nên) cụ thể bằng cách việc ánh xạ
khoa học các ứng dụng qua dữ liệu tỷ lệ và sự tính toán thời gian (Figure 12.10 makes these disparate requirements concrete by mapping scientific applications across data rate and computation time). Sự hình ảnh hóa tiết lộ một nổi bật
mẫu: Lớn Hadron Máy va chạm (Collider) các cảm biến phải xử lý dữ liệu tại các tỷ lệ tiếp cận 1014 bytes mỗi
giây với quy mô-nano giây (nanosecond-scale) sự tính toán các thời gian, trong khi di động các ứng dụng hoạt động tại 104 bytes (The visualization reveals a striking pattern: Large Hadron Collider sensors must process data at rates approaching 1014 bytes per second with nanosecond-scale computation times, while mobile applications operate at 104 bytes)

694
12.10 Việc đo điểm chuẩn Tốt nhất Các thực tiễn (Benchmarking Best Practices)
mỗi giây với dài hơn thuộc về tính toán các cửa sổ—một khoảng (span) của 10 bậc của độ lớn trên mỗi trục (per second with longer computational windows—a span of 10 orders of magnitude on each axis).
Này phạm vi của các yêu cầu đòi hỏi (necessitates) chuyên biệt các điểm chuẩn (This range of requirements necessitates specialized benchmarks). Cho ví dụ, biên AI các ứng dụng
hưởng lợi từ các điểm chuẩn giống như MLPerf thứ mà đánh giá hiệu suất dưới tài nguyên các sự ràng buộc, và
khoa học ứng dụng các miền cần của riêng chúng “Nhanh ML cho Khoa học (Fast ML for Science)” các điểm chuẩn (Duarte et al. 2022) (For example, edge AI applications benefit from benchmarks like MLPerf that evaluate performance under resource constraints, and scientific application domains need their own “Fast ML for Science” benchmarks (Duarte et al. 2022)).
10-9
10-7
10-5
10-3
10-1
101
103
105
102
104
106
108
1010
1012
1014
LHC cảm biến (LHC sensor)
X-quang sự nhiễu xạ (X-ray diffraction)
Internet-của-vạn vật (Internet-of-things)
Di động các thiết bị (Mobile devices)
Plasma sự kiểm soát (Plasma control)
LHC bộ kích hoạt (LHC trigger)
Chùm tia sự kiểm soát (Beam control)
DUNE sự đọc ra (DUNE readout)
EIC bộ kích hoạt (EIC trigger)
Qubit Sự đọc ra (Qubit Readout)
Thần kinh (Neuro)
Nam châm sự dập tắt (Magnet quench)
Điện tử (Electron) hiển vi (microscopy)
Nhanh ML cho Khoa học (Fast ML for Science)
điểm chuẩn các tác vụ (benchmark tasks)
Sự tính toán thời gian [s] (Computation time [s])
Dữ liệu tỷ lệ [bytes/s] (Data rate [bytes/s])
Hình 12.10: Hiệu suất Quang phổ (Performance Spectrum): Khoa học các ứng dụng và biên các thiết bị đòi hỏi một cách to lớn khác biệt thuộc về tính toán
các tài nguyên, việc trải dài nhiều bậc của độ lớn trong dữ liệu các tỷ lệ và độ trễ các yêu cầu (Scientific applications and edge devices demand vastly different computational resources, spanning multiple orders of magnitude in data rates and latency requirements). Do đó, truyền thống các điểm chuẩn
tập trung duy nhất trên độ chính xác là không đủ; chuyên biệt sự đánh giá các số liệu và các điểm chuẩn giống như MLPerf trở nên thiết yếu cho
việc tối ưu hóa AI các hệ thống qua đa dạng sự triển khai các kịch bản (Consequently, traditional benchmarks focused solely on accuracy are insufficient; specialized evaluation metrics and benchmarks like MLPerf become essential for optimizing AI systems across diverse deployment scenarios). Nguồn (Source): (Duarte et al. 2022).
Nhu cầu cho việc tiến hóa các điểm chuẩn cũng đưa ra một thách thức: tính ổn định so với tính có thể thích ứng (The need for evolving benchmarks also presents a challenge: stability vs. adaptability). Trên một
mặt, các điểm chuẩn phải duy trì ổn định cho đủ lâu để cho phép có ý nghĩa các sự so sánh qua thời gian (On the one hand, benchmarks must remain stable for long enough to allow meaningful comparisons over time).
Nếu các điểm chuẩn thay đổi quá thường xuyên, nó trở nên khó khăn để theo dõi dài-hạn sự tiến bộ và so sánh
mới các kết quả với lịch sử hiệu suất (If benchmarks change too frequently, it becomes difficult to track long-term progress and compare new results with historical performance). Trên khác mặt, việc thất bại để cập nhật các điểm chuẩn dẫn tới
sự đình trệ (stagnation), nơi các mô hình được tối ưu hóa cho lỗi thời các tác vụ thay vì việc thúc đẩy lĩnh vực (On the other hand, failing to update benchmarks leads to stagnation, where models are optimized for outdated tasks rather than advancing the field). Việc tấn công (Striking)
đúng sự cân bằng giữa điểm chuẩn tuổi thọ (longevity) và sự thích ứng là một đang diễn ra thách thức cho AI
cộng đồng (Striking the right balance between benchmark longevity and adaptation is an ongoing challenge for the AI community).
Việc tiến hóa các điểm chuẩn duy trì thiết yếu cho có ý nghĩa sự tiến bộ sự đo lường (Evolving benchmarks remains essential for meaningful progress measurement). Mà không có các bản cập nhật,
các điểm chuẩn trở nên bị tách rời (detached) từ thế giới-thực các nhu cầu, và các nhà nghiên cứu tối ưu hóa cho nhân tạo bài kiểm tra
các trường hợp thay vì thực tế các thách thức (Without updates, benchmarks become detached from real-world needs, and researchers optimize for artificial test cases rather than practical challenges). Sự chuyển đổi từ ImageNet-kỷ nguyên độ chính xác các điểm chuẩn tới
đa-chiều các sự đánh giá việc trải dài tính công bằng, tính mạnh mẽ, và năng lượng tính hiệu quả minh họa này
sự tiến hóa trong thực tiễn (The transition from ImageNet-era accuracy benchmarks to multi-dimensional evaluations spanning fairness, robustness, and energy efficiency illustrates this evolution in practice).
12.10.5 MLPerf sự tổng hợp và điểm chuẩn trò chơi (MLPerf synthesis and benchmark gaming)
Điểm chuẩn trò chơi (gaming) bắt đầu khi một trình biên dịch, thời gian chạy (runtime), hay phần cứng ngăn xếp tối ưu hóa cho điểm-
chuẩn hiện vật thay vì khối lượng công việc nó được cho là (supposed to) đại diện (Benchmark gaming begins when a compiler, runtime, or hardware stack optimizes for the benchmark artifact rather than the workload it is supposed to represent). MLPerf chống lại đó rủi ro bằng cách
việc tổng hợp các nguyên tắc được thảo luận xuyên suốt này chương vào một đơn đang tiến hóa bộ khung (MLPerf counters that risk by synthesizing the principles discussed throughout this chapter into a single evolving framework):
tham chiếu các sự triển khai và nghiêm ngặt sự đệ trình các quy tắc thực thi tính có thể tái tạo, cụ thể-sự triển khai
các bộ (suites) (Suy luận, Di động, Máy khách, Nhỏ bé) căn chỉnh với ba-chiều sự đánh giá bộ khung, và
thường xuyên tác vụ các bản cập nhật (bao gồm tạo sinh AI và hiệu quả-năng lượng việc tính toán) ngăn chặn điểm chuẩn (reference implementations and strict submission rules enforce reproducibility, deployment-specific suites (Inference, Mobile, Client, Tiny) align with the three-dimensional evaluation framework, and regular task updates (including generative AI and energy-efficient computing) prevent benchmark)

12. Việc đo điểm chuẩn (Benchmarking)
695
35
AlexNet: Tám-lớp
CNN (60M các tham số) thứ mà
cắt ImageNet top-5 lỗi từ
25.8 phần trăm tới 16.4 phần trăm
trong 2012, được huấn luyện trên hai GTX
580 GPUs với 3 GB bộ nhớ
mỗi (Krizhevsky et al.
2012) (AlexNet: The eight-layer CNN (60M parameters) that cut ImageNet top-5 error from 25.8 percent to 16.4 percent in 2012, trained on two GTX 580 GPUs with 3 GB memory each (Krizhevsky et al. 2012)). AlexNet đã thiết lập một
việc đo điểm chuẩn mô hình (paradigm) thứ mà
vẫn thông báo thị giác sự đánh-
giá:
độ chính xác trên một cố định
tập dữ liệu như chính số liệu,
với phần cứng cấu hình
như một thứ cấp sự chỉ định (AlexNet established a benchmarking paradigm that still informs vision evaluation: accuracy on a fixed dataset as the primary metric, with hardware configuration as a secondary specification).
Sau đó ImageNet các kết quả kế-
thừa (inherited) này cơ sở sự so sánh
cấu trúc (Later ImageNet results inherited this baseline comparison structure).
36
ResNet: Được giới thiệu bởi
He et al.
(2016a), nhảy (skip) các kết-
nối kích hoạt 152+ lớp
các mạng và đã đạt được 3.57
phần trăm top-5 ImageNet lỗi
(tập hợp - ensemble), việc vượt qua được ước-
tính con người lỗi tỷ lệ được báo-
cáo trong ImageNet thử-
thách ngữ cảnh (Russakovsky et
al. 2015) (ResNet: Introduced by He et al. (2016a), skip connections enabled 152+ layer networks and achieved 3.57 percent top-5 ImageNet error (ensemble), surpassing the estimated human error rate reported in the ImageNet challenge context (Russakovsky et al. 2015)). ResNet-50 đã trở thành một
chung MLPerf Huấn luyện tham-
chiếu khối lượng công việc bởi vì của nó
vừa phải kích thước (25.6M các tham-
số) và được hiểu-rõ (well-understood)
tính toán hồ sơ (4.1 GFLOP
mỗi hình ảnh) làm cho nó nhạy cảm tới
cả hai phần cứng và phần mềm
các sự tối ưu hóa mà không yêu-
cầu đa-nút các thiết lập (Matt-
son et al. 2020) (ResNet-50 became a common MLPerf Training reference workload because its moderate size (25.6M parameters) and well-understood compute profile (4.1 GFLOP per image) make it sensitive to both hardware and software optimizations without requiring multi-node setups (Mattson et al. 2020)).
sự đình trệ (stagnation). Trong Hennessy & Patterson truyền thống của định lượng các hệ thống, chúng ta phải thừa nhận
rằng các điểm chuẩn là không chỉ các sự đo lường; chúng là các mục tiêu (In the Hennessy & Patterson tradition of quantitative systems, we must acknowledge that benchmarks are not just measurements; they are targets). Goodhart động lực được giới thiệu
trong phần 12.1 áp dụng ở đây trong đầy đủ lực lượng (The Goodhart dynamic introduced in section 12.1 applies here in full force). Trong cao-tiền cược (high-stakes) thế giới của AI phần cứng, nó biểu hiện như
điểm chuẩn trò chơi (gaming): việc tối ưu hóa phần cứng hay các trình biên dịch một cách cụ thể cho điểm chuẩn’s độc đáo
các đặc điểm, thay vì cho thế giới-thực hiệu suất (In the high-stakes world of AI hardware, it manifests as benchmark gaming: optimizing hardware or compilers specifically for the benchmark’s unique characteristics, rather than for real-world performance).
Những người đệ trình (Submitters) việc theo đuổi bảng xếp hạng vị trí một cách phổ biến (commonly) với tới cho ba (việc) chơi game các kỹ thuật:
• Độ chính xác (Việc) Bỏ rơi (Precision Dropping): Các trình biên dịch có thể một cách âm thầm giảm độ chính xác (cho ví dụ, từ FP32 tới
BF16) chỉ trong suốt điểm chuẩn lượt chạy để bơm phồng (inflate) thông lượng, thậm chí nếu người dùng đã không yêu cầu nó (Precision Dropping: Compilers may silently reduce precision (for example, from FP32 to BF16) only during the benchmark run to inflate throughput, even if the user did not request it).
• Toán tử (Việc) Loại bỏ (Operator Removal): Một trình biên dịch có thể xác định rằng một điểm chuẩn chỉ quan tâm về top-1
độ chính xác và “tối ưu hóa ra (optimize out)” sự kích hoạt các hàm hay lớp các chuẩn tắc (norms) nếu chúng không ảnh hưởng đó
cụ thể số liệu, việc mang lại không thực tế các sự tăng tốc (Operator Removal: A compiler might identify that a benchmark only cares about top-1 accuracy and “optimize out” the activation functions or layer norms if they do not affect that specific metric, yielding unrealistic speedups).
• Trọng số Việc tải trước (Weight Preloading): Việc viết mã cứng (Hardcoding) điểm chuẩn mô hình’s các trọng số vào chip’s trên-chip
SRAM, việc bỏ qua “bộ nhớ bức tường (memory wall)” các nút thắt cổ chai thứ mà thực tế sản xuất các mô hình phải đối mặt (Weight Preloading: Hardcoding the benchmark model’s weights into the chip’s on-chip SRAM, bypassing the “memory wall” bottlenecks that real production models must face).
MLPerf ngăn chặn này (việc) chơi game thông qua của nó Tham chiếu so với Sự đệ trình (Reference vs. Submission) sự xác nhận (MLPerf prevents this gaming through its Reference vs. Submission validation). Mọi người đệ trình phải
chạy chính xác giống nhau mô hình cấu trúc và đạt tới một có thể xác minh độ chính xác mục tiêu (cho ví dụ, 75.9 phần trăm
trên ImageNet) để đủ điều kiện (Every submitter must run the exact same model structure and reach a verifiable accuracy target (for example, 75.9 percent on ImageNet) to qualify). Một trình biên dịch thứ mà bỏ rơi độ chính xác hay loại bỏ các toán tử thất bại độ chính xác
sự kiểm tra, và kết quả bị loại bỏ (disqualified) (A compiler that drops precision or removes operators fails the accuracy check, and the result is disqualified). Này độ chính xác lan can (guardrail) biến đổi một đơn giản tốc độ bài kiểm tra vào một
nghiêm ngặt kỹ thuật điểm chuẩn, việc ép buộc các nhà cung cấp để tối ưu hóa cho silicon hợp đồng (contract) thay vì
(việc) chơi game các con số (This accuracy guardrail transforms a simple speed test into a rigorous engineering benchmark, forcing vendors to optimize for the silicon contract rather than gaming the numbers).
Tuy nhiên thậm chí nhất nghiêm ngặt hệ thống các điểm chuẩn xác nhận chỉ một chiều của sự triển khai
sự sẵn sàng (Yet even the most rigorous system benchmarks validate only one dimension of deployment readiness). Một hệ thống việc đạt được kỷ lục thông lượng và tính hiệu quả trên MLPerf nói không gì cả về
liệu mô hình nó chạy là chính xác trên thế giới-thực các đầu vào, hoặc liệu dữ liệu nó đã được huấn luyện trên (có)
đại diện cho quần thể (population) nó sẽ phục vụ (A system achieving record throughput and efficiency on MLPerf says nothing about whether the model it runs is accurate on real-world inputs, or whether the data it was trained on represents the population it will serve). Phần cứng thứ mà phân phối được hứa hẹn TFLOP/s là cần thiết nhưng
không đủ; mô hình việc chạy trên đó phần cứng phải bảo tồn chất lượng người dùng phụ thuộc trên, và
dữ liệu thứ mà định hình đó mô hình phải đại diện thế giới nó sẽ chạm trán (Hardware that delivers promised TFLOP/s is necessary but insufficient; the model running on that hardware must preserve the quality users depend on, and the data that shaped that model must represent the world it will encounter). Việc hoàn thành sự xác nhận
ngăn xếp yêu cầu việc quay từ phần cứng tới mô hình và dữ liệu các chiều của của chúng ta ba-chiều
bộ khung (Completing the validation stack requires turning from hardware to the model and data dimensions of our three-dimensional framework).
12.11 Mô hình và Dữ liệu Sự đánh giá (Model and Data Evaluation)
Một được nén mô hình việc chạy trên được gia tốc phần cứng có thể vẫn thất bại nếu nó đã được huấn luyện trên bị thiên vị dữ liệu (A compressed model running on accelerated hardware can still fail if it was trained on biased data).
Hệ thống các điểm chuẩn có thể xác nhận rằng phần cứng phân phối được hứa hẹn huấn luyện thông lượng, suy luận
độ trễ, và điện năng tính hiệu quả, nhưng phần cứng sự xác nhận một mình không thể đảm bảo sự triển khai thành công (System benchmarks can confirm that hardware delivers promised training throughput, inference latency, and power efficiency, but hardware validation alone cannot ensure deployment success).
sự tối ưu hóa đường ống từ Phần III cũng đã bao gồm mô hình sự nén (Chương 10) và dữ liệu sự lựa chọn
(Chương 9), mỗi (cái) việc yêu cầu của riêng nó sự xác nhận (The optimization pipeline from Part III also included model compression (Chapter 10) and data selection (Chapter 9), each requiring its own validation). Phần còn lại hai các chiều của bộ khung
giải quyết này khoảng cách: mô hình các điểm chuẩn xác minh rằng sự nén đã bảo tồn độ chính xác và chí mạng mô hình
các thuộc tính, trong khi dữ liệu các điểm chuẩn xác minh rằng huấn luyện dữ liệu kích hoạt mạnh mẽ sự khái quát hóa (The remaining two dimensions of the framework address this gap: model benchmarks verify that compression preserved accuracy and critical model properties, while data benchmarks verify that data benchmarks verify that training data enables robust generalization).
12.11.1 Mô hình việc đo điểm chuẩn (Model benchmarking)
Mô hình các điểm chuẩn xác nhận liệu sự nén các kỹ thuật từ Chương 10 đã bảo tồn các thuộc-
tính thứ mà quan trọng cho sự triển khai (Model benchmarks validate whether compression techniques from Chapter 10 preserved the properties that matter for deployment). Này mở rộng vượt ra ngoài trên-cùng-dòng (top-line) độ chính xác (This extends beyond top-line accuracy). Một được cắt tỉa mô hình có thể
duy trì ImageNet độ chính xác trong khi việc mất tính mạnh mẽ tới đối kháng (adversarial) các đầu vào (A pruned model might maintain ImageNet accuracy while losing robustness to adversarial inputs). Một được lượng tử hóa mô hình
có thể bảo tồn trung bình-trường hợp hiệu suất trong khi việc suy thoái trên hiếm nhưng chí mạng biên các trường hợp (A quantized model might preserve average-case performance while degrading on rare but critical edge cases). Một được chưng cất
mô hình có thể khớp giáo viên’s độ chính xác trong khi việc mất sự hiệu chuẩn (A distilled model might match the teacher’s accuracy while losing calibration). Về mặt lịch sử, các điểm chuẩn đã tập trung
gần như độc quyền trên độ chính xác, nhưng sự nén làm cho đa-chiều sự đánh giá (trở nên) thiết yếu (Historically, benchmarks focused almost exclusively on accuracy, but compression makes multi-dimensional evaluation essential).
ImageNet liên kết mô hình việc đo điểm chuẩn tới phần cứng câu chuyện từ hình 12.1: lỗi các tỷ lệ đã rơi khi
được kích hoạt-GPU các kiến trúc trở nên thực tế (ImageNet links model benchmarking to the hardware story from figure 12.1: error rates fell as GPU-enabled architectures became practical). Hình 12.11 thêm thuộc về kiến trúc các cột mốc (milestones) tới đó
giống nhau sự tiến triển, việc theo dõi lỗi sự giảm từ 28.2 phần trăm trong 2010 tới 3.57 phần trăm trên ImageNet
Lớn Quy mô Thị giác Sự nhận dạng Thử thách (Large Scale Visual Recognition Challenge) (ILSVRC) (Russakovsky et al. 2015) (Figure 12.11 adds the architectural milestones to that same progression, tracing error reduction from 28.2 percent in 2010 to 3.57 percent on the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) (Russakovsky et al. 2015)). Sự giới thiệu của
AlexNet35 đã giảm lỗi tỷ lệ từ 25.8 phần trăm tới 16.4 phần trăm (The introduction of AlexNet35 reduced the error rate from 25.8 percent to 16.4 percent). Tiếp theo các mô hình giống như ZFNet,
VGGNet, GoogLeNet, và ResNet36 đã tiếp tục này xu hướng, với ResNet việc đạt được 3.57 phần trăm (He et
al. 2016a) (Subsequent models like ZFNet, VGGNet, GoogLeNet, and ResNet36 continued this trend, with ResNet achieving 3.57 percent (He et al. 2016a)). Này sự tiến triển đã thiết lập các cơ sở chống lại thứ mà mô hình sự nén các kỹ thuật
được đánh giá: một được cắt tỉa ResNet phải chứng minh bao nhiêu độ chính xác nó hy sinh cho một được cho
tính hiệu quả lợi ích (This progression established the baselines against which model compression techniques are evaluated: a pruned ResNet must demonstrate how much accuracy it sacrifices for a given efficiency gain).

696
12.11 Mô hình và Dữ liệu Sự đánh giá (Model and Data Evaluation)
2010
2011
2012
2013
2014
2015
Năm (Year)
0
5
10
15
20
25
30
Top-5 Lỗi (%) (Top-5 Error (%))
Cơ sở (Baseline)
Cơ sở (Baseline)
AlexNet
ZFNet
VGGNet
GoogleNet
ResNet
Hình 12.11: ImageNet Thử thách Sự tiến triển (ImageNet Challenge Progression): Thần kinh các mạng đã giảm ImageNet thử thách lỗi các tỷ lệ từ 28.2 phần trăm trong
2010 tới 3.57 phần trăm bởi 2015, việc làm nổi bật tác động của thuộc về kiến trúc các sự tiến bộ trên phân loại độ chính xác (Neural networks reduced ImageNet challenge error rates from 28.2 percent in 2010 to 3.57 percent by 2015, highlighting the impact of architectural advancements on classification accuracy). Những các cột mốc (milestones) này
thiết lập các cơ sở chống lại thứ mà sự nén các kỹ thuật được đánh giá (These milestones establish the baselines against which compression techniques are evaluated). Các nguồn: (Russakovsky et al. 2015; Krizhevsky et al.
2012; He et al. 2016a).
37
Sự hiệu chuẩn (Calibration): Từ Ả Rập (Arabic) qalib (một khuôn (mold) cho việc đúc (casting) kim loại) thông qua Latin calibrare,
ban đầu việc mô tả sự điều-
chỉnh của việc đo lường các công-
cụ chống lại được biết các tiêu-
chuẩn (From Arabic qalib (a mold for casting metal) via Latin calibrare, originally describing the adjustment of measuring instruments against known standards). Trong ML, sự hiệu chuẩn đảm-
bảo được dự đoán các xác suất
khớp thực nghiệm các tần số;
Guo et al. chính thức hóa (formalize) này mối quan-
tâm (concern) cho hiện đại thần kinh các mạng
và cho thấy rằng nhiệt-
độ (temperature) sự mở rộng quy mô là một đơn giản
hiệu quả hậu mãi (post-hoc) sự sửa chữa
(Guo et al.
2017) (In ML, calibration ensures predicted probabilities match empirical frequencies; Guo et al. formalize this concern for modern neural networks and show that temperature scaling is a simple effective post-hoc correction (Guo et al. 2017)).
Từ nguyên (etymology) là thích hợp (apt):
chỉ như
một không được hiệu chuẩn công cụ
tạo ra chính xác nhưng không chính-
xác các sự đo lường, một không được hiệu-
chuẩn mô hình tạo ra tự-
tin nhưng không đáng tin cậy các dự-
đoán, việc gây ra hạ lưu (downstream)
các hệ thống thứ mà đặt ngưỡng (threshold) trên độ tự-
tin các điểm số để đưa ra một cách có hệ thống
sai các quyết định (The etymology is apt: just as an uncalibrated instrument produces precise but inaccurate measurements, an uncalibrated model produces confident but unreliable predictions, causing downstream systems that threshold on confidence scores to make systematically wrong decisions).
12.11.1.1 Độ chính xác các số liệu và của chúng điểm mù (blind spots)
Nhất phổ biến mô hình các số liệu (độ chính xác, độ chuẩn xác (precision), độ nhớ (recall), F1) mỗi (cái) tiết lộ khác nhau các khía cạnh của
mô hình hành vi trong khi việc giấu những (khía cạnh) khác, và việc hiểu của chúng điểm mù là thiết yếu cho sự nén
sự xác nhận (The most common model metrics (accuracy, precision, recall, F1) each reveal different aspects of model behavior while hiding others, and understanding their blind spots is essential for compression validation). Top-𝑘 độ chính xác đo lường liệu đúng nhãn xuất hiện trong mô hình’s top-𝑘
các dự đoán (Top-𝑘 accuracy measures whether the correct label appears in the model’s top-𝑘 predictions). Top-1 độ chính xác là nghiêm ngặt; top-5 là khoan dung (lenient). Khoảng cách giữa chúng tiết lộ mô hình sự không chắc-
chắn (uncertainty): một mô hình với 75 phần trăm top-1 nhưng 95 phần trăm top-5 độ chính xác “biết” câu trả lời là trong số một
vài các ứng cử viên nhưng chật vật để cam kết (The gap between them reveals model uncertainty: a model with 75 percent top-1 but 95 percent top-5 accuracy “knows” the answer is among a few candidates but struggles to commit). Cho sự triển khai, có thể chấp nhận khoảng cách phụ thuộc trên liệu
hạ lưu các hệ thống có thể sử dụng được xếp hạng các dự đoán hay yêu cầu đơn các câu trả lời (For deployment, the acceptable gap depends on whether downstream systems can use ranked predictions or require single answers).
Độ chuẩn xác (Precision) và độ nhớ (recall) quan trọng khi các lớp là mất cân bằng hay các lỗi có bất đối xứng các chi phí (Sokolova
và Lapalme 2009) (Precision and recall matter when classes are imbalanced or errors have asymmetric costs (Sokolova and Lapalme 2009)). Một gian lận sự phát hiện mô hình với 99 phần trăm độ chính xác có thể có 10 phần trăm độ nhớ
trên thực tế gian lận (việc bắt chỉ một trong 10 gian lận các giao dịch), một thảm khốc thất bại mặc dù cao
độ chính xác (A fraud detection model with 99 percent accuracy might have 10 percent recall on actual fraud (catching only one in 10 fraudulent transactions), a catastrophic failure despite high accuracy). Độ chuẩn xác (của được dự đoán các (trường hợp) tích cực (positives), bao nhiêu là đúng?) và độ nhớ (của thực tế các (trường hợp) tích cực,
bao nhiêu đã được tìm thấy?) phơi bày (expose) những các thất bại này thứ mà độ chính xác giấu (Precision (of predicted positives, how many are correct?) and recall (of actual positives, how many were found?) expose these failures that accuracy hides).
Nhất xảo quyệt (insidiously), tổng hợp các số liệu giấu nhóm phụ (subgroup) các thất bại. Một mô hình việc đạt được 95 phần trăm tổng thể
độ chính xác có thể đạt được 60 phần trăm trên một chí mạng nhân khẩu học (demographic) nhóm phụ (Most insidiously, aggregate metrics hide subgroup failures. A model achieving 95 percent overall accuracy might achieve 60 percent on a critical demographic subgroup). Gender Shades dự án
(Buolamwini và Gebru 2018) đã tiết lộ thương mại giới tính-phân loại các hệ thống cho khuôn mặt sự phân tích
việc biểu diễn một cách đáng kể kém hơn trên sẫm màu hơn-da phụ nữ hơn trên sáng màu hơn-da đàn ông, một sự chênh lệch (disparity)
vô hình tới tổng hợp các điểm chuẩn (The Gender Shades project (Buolamwini and Gebru 2018) revealed commercial gender-classification systems for facial analysis performing substantially worse on darker-skinned women than on lighter-skinned men, a disparity invisible to aggregate benchmarks). Bị phân tách (Disaggregated) sự đánh giá qua liên quan-tới-sự triển khai các nhóm phụ
là thiết yếu; Chương 15 xem xét tính công bằng sự đánh giá một cách có hệ thống (Disaggregated evaluation across deployment-relevant subgroups is essential; Chapter 15 examines fairness evaluation systematically).
12.11.1.2 Sự hiệu chuẩn: Khi độ tự tin các điểm số quan trọng (Calibration: When confidence scores matter)
Cho nhiều sự triển khai các kịch bản, bao nhiêu tự tin mô hình là (thì) quan trọng như nhiều như cái gì nó dự đoán (For many deployment scenarios, how confident the model is matters as much as what it predicts). Một
được hiệu chuẩn-tốt37 mô hình’s độ tự tin các điểm số tương ứng tới thực tế tính đúng đắn xác suất: khi nó
nói “90 phần trăm tự tin,” nó nên (thì) đúng 90 phần trăm của thời gian (A well-calibrated37 model’s confidence scores correspond to actual correctness probability: when it says “90 percent confident,” it should be correct 90 percent of the time).
Sự nén có thể dịch chuyển sự hiệu chuẩn thậm chí khi việc bảo tồn độ chính xác, một chí mạng mối quan tâm khi việc xác-
nhận sự lượng tử hóa các kỹ thuật từ phần 10.4 (Compression can shift calibration even when preserving accuracy, a critical concern when validating quantization techniques from section 10.4). Một được lượng tử hóa mô hình có thể duy trì tiêu đề (headline)
độ chính xác trong khi việc trở nên quá tự tin trên các ví dụ nó (làm) sai (A quantized model might maintain headline accuracy while becoming overconfident on examples it gets wrong). Này quan trọng bởi vì hậu mãi (post-hoc)
sự hiệu chuẩn các kỹ thuật chẳng hạn như nhiệt độ sự mở rộng quy mô có thể chỉ sửa chữa vấn đề nếu sự hiệu chuẩn là
được đo lường một cách rõ ràng (Guo et al. 2017) (This matters because post-hoc calibration techniques such as temperature scaling can only correct the problem if calibration is measured explicitly (Guo et al. 2017)).
Sự hiệu chuẩn các thất bại tạo ra hạ lưu các vấn đề (Calibration failures create downstream problems). Một quá tự tin mô hình kích hoạt không cần thiết
con người sự đánh giá (được dự đoán 95 phần trăm độ tự tin nhưng sai 30 phần trăm của thời gian) (An overconfident model triggers unnecessary human review (predicted 95 percent confidence but wrong 30 percent of the time)). Một thiếu tự tin (underconfident) mô hình thất bại để tự động hóa các quyết định nó có thể xử lý (được dự đoán 70 phần trăm độ tự tin nhưng đúng
95 phần trăm của thời gian) (An underconfident model fails to automate decisions it could handle (predicted 70 percent confidence but correct 95 percent of the time)). Được kỳ vọng Sự hiệu chuẩn Lỗi (Expected Calibration Error) (ECE) đo lường khoảng cách giữa độ tự tin
và độ chính xác qua độ tự tin các thùng (bins); độ tin cậy (reliability) các sơ đồ (diagrams) hình ảnh hóa này sự tương ứng (Expected Calibration Error (ECE) measures the gap between confidence and accuracy across confidence bins; reliability diagrams visualize this correspondence).

12. Việc đo điểm chuẩn (Benchmarking)
697
38
Pareto Biên giới (Frontier): Được đặt tên
theo
nhà kinh tế học (economist)
Vilfredo
Pareto
(Pareto
1896),
biên giới
chứa
tất cả
các giải-
pháp nơi việc cải thiện một
mục tiêu yêu cầu việc suy thoái
(một mục tiêu) khác (Pareto Frontier: Named after economist Vilfredo Pareto (Pareto 1896), the frontier contains all solutions where improving one objective requires degrading another).
Trong sự nén
việc đo điểm chuẩn, biên giới’s
hình dạng
mang
chẩn đoán (diagnostic)
thông tin: một dốc (steep) khu vực
có nghĩa (rằng) tính hiệu quả các lợi ích đến
một cách rẻ mạt (cắt tỉa ở đây), trong khi
một phẳng (flat) khu vực có nghĩa (rằng) xa hơn
sự nén tốn kém không tương-
xứng (disproportionate) độ chính xác (dừng ở đây) (In compression benchmarking, the frontier’s shape carries diagnostic information: a steep region means efficiency gains come cheaply (prune here), while a flat region means further compression costs disproportionate accuracy (stop here)).
Các điểm
bên dưới
biên giới
bị một cách nghiêm ngặt thống trị và
đại diện cho bị lãng phí công suất (Points below the frontier are strictly dominated and represent wasted capacity).
Một bị thống trị (dominated) mô hình thua (loses) trên cả hai
các trục của Pareto biên giới (A dominated model loses on both axes of the Pareto frontier).
12.11.1.3 Sự nén sự xác nhận: Tính hiệu quả-chất lượng biên giới (Compression validation: The efficiency-quality frontier)
Mô hình sự nén (Chương 10) đánh đổi mô hình công suất cho tính hiệu quả (Model compression (Chapter 10) trades model capacity for efficiency). Sự xác nhận phải xác định
liệu sự nén (có) đạt được một có thể chấp nhận sự đánh đổi hay đã làm hỏng các khả năng thứ mà quan trọng (Validation must determine whether compression achieved an acceptable trade-off or damaged capabilities that matter).
Pareto biên giới38 sự đánh giá xác định liệu một được nén mô hình đại diện cho một tốt sự đánh đổi (Pareto frontier38 evaluation determines whether a compressed model represents a good trade-off).
Việc vẽ (Plotting) độ chính xác chống lại mục tiêu tính hiệu quả số liệu (độ trễ, mô hình kích thước, năng lượng) tiết lộ sự đánh-
đổi biên giới (Plotting accuracy against the target efficiency metric (latency, model size, energy) reveals the trade-off frontier). Các mô hình trên Pareto biên giới không thể cải thiện một số liệu mà không có việc suy thoái cái khác (Models on the Pareto frontier cannot improve one metric without degrading the other);
các mô hình bên dưới biên giới bị thống trị bởi tốt hơn các giải pháp thay thế (models below the frontier are dominated by better alternatives).
Khác nhau sự nén các kỹ thuật thất bại theo khác nhau các cách (Different compression techniques fail in different ways). Sự lượng tử hóa (việc giảm thuộc về số độ chính-
xác) có thể bảo tồn trung bình-trường hợp hiệu suất trong khi việc thay đổi sự hiệu chuẩn hay hành vi gần quyết định
các ranh giới (Jacob et al. 2018; Guo et al. 2017) (Quantization (reducing numerical precision) can preserve average-case performance while changing calibration or behavior near decision boundaries (Jacob et al. 2018; Guo et al. 2017)). Sự cắt tỉa (việc loại bỏ các trọng số hay các cấu trúc) có thể mất
công suất cho hiếm các tính năng, một cách tiềm năng ổn (fine) cho chung các trường hợp nhưng rủi ro cho đuôi (tail) các kịch bản (Han et al.
2015; Gale et al. 2019) (Pruning (removing weights or structures) can lose capacity for rare features, potentially fine for common cases but risky for tail scenarios (Han et al. 2015; Gale et al. 2019)). Sự chưng cất (việc huấn luyện nhỏ hơn các mô hình để bắt chước lớn hơn những cái) có thể khớp trên-cùng-dòng
độ chính xác trong khi việc thay đổi mềm hơn các thuộc tính chẳng hạn như độ tự tin và sự hiệu chuẩn (Hinton et al. 2015) (Distillation (training smaller models to mimic larger ones) can match top-line accuracy while changing softer properties such as confidence and calibration (Hinton et al. 2015)).
Sự xác nhận phải thăm dò (probe) những cụ thể thất bại các chế độ này, không chỉ đo lường tổng hợp độ chính xác (Validation must probe these specific failure modes, not just measure aggregate accuracy).
Sự hiệu chuẩn là thất bại chế độ (mà) tổng hợp độ chính xác giấu nhất một cách hoàn toàn, và được kỳ vọng sự hiệu chuẩn
lỗi (ECE) là số liệu thứ mà phơi bày nó (Calibration is the failure mode aggregate accuracy hides most completely, and expected calibration error (ECE) is the metric that exposes it). ECE đo lường liệu được dự đoán độ tự tin (có) khớp
thực tế độ chính xác (hay không): khi một mô hình báo cáo một dự đoán như 90 phần trăm tự tin, nó nên (thì) đúng
90 phần trăm của thời gian (ECE measures whether predicted confidence matches actual accuracy: when a model reports a prediction as 90 percent confident, it should be correct 90 percent of the time). Ba các ngưỡng chi phối (govern) sự diễn giải (Three thresholds govern interpretation). Một ECE < 0.05 là được hiệu chuẩn-tốt,
với độ tự tin các điểm số đáng tin cậy cho dựa trên-ngưỡng các quyết định; một ECE giữa 0.05 và 0.10 là
được hiệu chuẩn một cách vừa phải (moderately calibrated), nơi độ tự tin các điểm số nên được sử dụng với sự thận trọng; và một ECE > 0.10 là
được hiệu chuẩn kém (poorly calibrated), nơi độ tự tin các điểm số là không đáng tin cậy (An ECE < 0.05 is well-calibrated, with confidence scores reliable for threshold-based decisions; an ECE between 0.05 and 0.10 is moderately calibrated, where confidence scores should be used with caution; and an ECE > 0.10 is poorly calibrated, where confidence scores are unreliable). Sự nén có thể để lại (leave) top-1 độ chính xác
còn nguyên vẹn (intact) trong khi việc đẩy ECE qua những các ngưỡng này, thứ mà là tại sao một sự nén giao thức đo lường nó
một cách trực tiếp (Compression can leave top-1 accuracy intact while pushing ECE across these thresholds, which is why a compression protocol measures it directly).
Có thể chấp nhận sự suy thoái phụ thuộc trên sự triển khai ngữ cảnh (Acceptable degradation depends on deployment context). Một 2 phần trăm độ chính xác sự sụt giảm có thể là
có thể chấp nhận cho một sự giới thiệu hệ thống (người dùng dung thứ (tolerate) không hoàn hảo các gợi ý) nhưng không thể chấp nhận
cho y tế chẩn đoán (mỗi lỗi có đáng kể các hậu quả) (A 2 percent accuracy drop might be acceptable for a recommendation system (users tolerate imperfect suggestions) but unacceptable for medical diagnosis (each error has significant consequences)). Xác định độ chính xác các ngưỡng trước khi
sự nén, sau đó xác nhận chống lại chúng (Define accuracy thresholds before compression, then validate against them). MobileNetV2 ngọn hải đăng (lighthouse) làm cho hoàn chỉnh INT8
sự xác nhận giao thức (trở nên) cụ thể (The MobileNetV2 lighthouse makes the complete INT8 validation protocol concrete).
Ngọn hải đăng (Lighthouse) 12.3: MobileNetV2 INT8 sự nén (MobileNetV2 INT8 compression)
Việc quay trở lại (tới) của chúng ta MobileNetV2 ngọn hải đăng ví dụ, hãy xem xét một hoàn chỉnh sự xác nhận giao thức
cho INT8 sự lượng tử hóa, được làm nền tảng trong MobileNetV2’s kiến trúc (Sandler et al. 2018) và
hậu-huấn luyện (post-training) sự lượng tử hóa thực tiễn (Jacob et al. 2018) (Returning to our MobileNetV2 lighthouse example, consider a complete validation protocol for INT8 quantization, grounded in MobileNetV2’s architecture (Sandler et al. 2018) and post-training quantization practice (Jacob et al. 2018)):
Tiền-sự nén (Precompression) cơ sở: MobileNetV2 đạt được 71.8 phần trăm top-1 độ chính xác trên ImageNet tại
3.5M các tham số (14 MB FP32) (Precompression baseline: MobileNetV2 achieves 71.8 percent top-1 accuracy on ImageNet at 3.5M parameters (14 MB FP32)).
Lưu ý trong bảng 12.19 rằng tổng hợp độ chính xác hầu như không thay đổi sau INT8 sự lượng tử hóa tới 3.5 MB,
nhưng sự hiệu chuẩn lỗi và biên-trường hợp (edge-case) độ chính xác kể một khác câu chuyện (Notice in table 12.19 that aggregate accuracy barely changes after INT8 quantization to 3.5 MB, but calibration error and edge-case accuracy tell a different story). INT8 mô hình’s ECE của
0.089 hạ cánh trong đường biên (borderline) dải (band): độ tự tin các điểm số đang trở nên không đáng tin cậy cho tự động
quyết định các ngưỡng (The INT8 model’s ECE of 0.089 lands in the borderline band: confidence scores are becoming unreliable for automated decision thresholds).
Bảng 12.19: MobileNetV2 INT8 Hậu-sự nén Các số liệu (MobileNetV2 INT8 Postcompression Metrics): FP32 so với INT8 sự so sánh qua top-1 và top-5 độ chính xác,
sự hiệu chuẩn lỗi, và biên-trường hợp độ chính xác, việc tiết lộ cách nào tổng hợp độ chính xác có thể che giấu sự hiệu chuẩn và đuôi-trường hợp
sự suy thoái (FP32 vs. INT8 comparison across top-1 and top-5 accuracy, calibration error, and edge-case accuracy, revealing how aggregate accuracy can mask calibration and tail-case degradation).
Số liệu (Metric)
FP32
INT8
Có thể chấp nhận? (Acceptable?)
Top-1 độ chính xác (Top-1 accuracy)
71.8%
70.9%
✓ (0.9 pp sụt giảm; bên dưới 1 điểm phần trăm-ngưỡng (percentage-point threshold))
Top-5 độ chính xác (Top-5 accuracy)
91%
90.4%
✓
Sự hiệu chuẩn (Calibration) ECE
0.031
0.089
฀ (bị suy thoái) (degraded)
Biên-trường hợp độ chính xác (Edge-case accuracy)
68.2%
61.4%
฀ (sụt giảm của 6.8 pp) (drop of 6.8 pp)
Biên-trường hợp định nghĩa (Edge-case definition): Các hình ảnh với >50 phần trăm sự che khuất (occlusion), <100 lux ánh sáng, hoặc >30° sự xoay
từ huấn luyện sự phân phối (xấp xỉ 5 phần trăm của thế giới-thực các đầu vào) (Images with >50 percent occlusion, <100 lux lighting, or >30° rotation from training distribution (approximately 5 percent of real-world inputs)).

698
12.11 Mô hình và Dữ liệu Sự đánh giá (Model and Data Evaluation)
39
MMLU
(Khổng lồ (Massive)
Đa tác vụ (Multitask)
Ngôn ngữ (Language)
Sự hiểu biết (Un-
derstanding)):
Được giới thiệu
bởi Hendrycks et al.
(2020)
với 15,908 nhiều-lựa chọn (multiple-choice)
các câu hỏi qua năm mươi-bảy
các chủ đề (Introduced by Hendrycks et al. (2020) with 15,908 multiple-choice questions across fifty-seven subjects).
MMLU’s việc đo điểm chuẩn
sự giới hạn
là
của nó
định dạng:
nhiều-lựa chọn
sự nhận dạng là không (phải) giống nhau
tác vụ như kết thúc-mở (open-ended) sự tạo-
sinh (generation), do đó một MMLU điểm số
không nên (được) đọc như trực tiếp
bằng chứng rằng một mô hình có thể
tạo ra được làm nền tảng (grounded) hình thức-tự do (free-form)
các câu trả lời trong sản xuất (MMLU’s benchmarking limitation is its format: multiple-choice recognition is not the same task as open-ended generation, so an MMLU score should not be read as direct evidence that a model can produce grounded free-form answers in production).
40
HELM (Tổng thể (Holistic) Sự đánh giá (Eval-
uation) của Ngôn ngữ Các mô-
hình (Language Models)): Stanford’s 2022 sự đánh-
giá bộ khung đã kiểm tra một rộng
tập của các mô hình qua bảy các chiều
(độ chính xác, sự hiệu chuẩn,
tính mạnh mẽ, tính công bằng, sự thiên vị,
tính độc hại (toxicity), tính hiệu quả) (Liang et
al.
2022) (Stanford’s 2022 evaluation framework tested a broad set of models across seven dimensions (accuracy, calibration, robustness, fairness, bias, toxicity, efficiency) (Liang et al. 2022)).
HELM’s sự đóng-
góp là thuộc về phương pháp luận: bằng cách
việc đánh giá các mô hình thứ mà ghi điểm
một cách tương tự trên độ chính xác nhưng phân-
kỳ (diverge) trên sự hiệu chuẩn hay tính độc-
hại, nó chứng minh rằng đơn-
số liệu các bảng xếp hạng một cách có hệ-
thống giấu thất bại các chế độ thứ mà
quan trọng cho sản xuất sự triển-
khai (HELM’s contribution is methodological: by evaluating models that score similarly on accuracy but diverge on calibration or toxicity, it demonstrates that single-metric leaderboards systematically hide failure modes that matter for production deployment).
41
Sự bối rối (Perplexity): Từ Latin
perplexus
(bị vướng mắc - entangled);
trong
thông tin
lý thuyết,
2𝐻(𝑝)
nơi 𝐻 là entropy (From Latin perplexus (entangled); in information theory, 2𝐻(𝑝) where 𝐻 is entropy).
Một
sự bối rối của 10 có nghĩa (rằng)
mô hình là “10-chiều bối rối”
trên trung bình (A perplexity of 10 means the model is “10-way confused” on average).
Các hệ thống
hậu quả là thuộc về sự diễn giải (interpretive)
thay vì trực tiếp bộ nhớ
việc kế toán (accounting):
sự bối rối
đo lường được giữ-lại (held-out) mã thông báo-tiếp theo (next-token)
sự dự đoán trên một kho ngữ liệu (corpus), trong khi
việc phục vụ bộ nhớ áp lực là
được chi phối bởi ngữ cảnh độ dài,
lô kích thước, mô hình hình dạng, và
việc giải mã (decoding)
trạng thái;
KV-bộ nhớ đệm
sự quản lý là một riêng biệt
việc phục vụ vấn đề (Kwon et al.
2023) (The systems consequence is interpretive rather than direct memory accounting: perplexity measures held-out next-token prediction on a corpus, while serving memory pressure is governed by context length, batch size, model shape, and decoding state; KV-cache management is a separate serving problem (Kwon et al. 2023)).
Cái gì này tiết lộ: Trung bình-trường hợp độ chính xác trông (có vẻ) có thể chấp nhận (0.9 điểm phần trăm sụt giảm), nhưng
sự hiệu chuẩn bị suy thoái một cách đáng kể và biên-trường hợp độ chính xác sụt giảm 6.8 điểm phần trăm (What this reveals: Average-case accuracy looks acceptable (0.9 percentage-point drop), but calibration degraded significantly and edge-case accuracy dropped 6.8 percentage points).
Nếu sự triển khai ngữ cảnh sử dụng độ tự tin các ngưỡng (cho ví dụ, “chỉ hành động nếu độ tự tin
> 85 phần trăm”) hoặc chạm trán nhiều biên các trường hợp (bất thường ánh sáng, một phần các sự che khuất), INT8
MobileNetV2 có thể thất bại mặc dù việc vượt qua tổng hợp các điểm chuẩn (If the deployment context uses confidence thresholds (for example, “only act if confidence > 85 percent”) or encounters many edge cases (unusual lighting, partial occlusions), INT8 MobileNetV2 may fail despite passing aggregate benchmarks).
Sự sửa chữa: Áp dụng nhiệt độ sự mở rộng quy mô hậu mãi (post-hoc) để khôi phục sự hiệu chuẩn (Guo et al. 2017) (Fix: Apply temperature scaling post-hoc to restore calibration (Guo et al. 2017)). Nhiệt độ
sự mở rộng quy mô học một đơn vô hướng (scalar) 𝑇cal để chia logits trước softmax: softmax(𝑧𝑖/𝑇cal). Một cách song song,
thêm biên-trường hợp các ví dụ tới bài kiểm tra tập để theo dõi đó cụ thể thất bại chế độ một cách liên tục (In parallel, add edge-case examples to the test set to monitor that specific failure mode continuously).
Xổ số Vé Giả thuyết (Lottery Ticket Hypothesis) (phần 10.3.1.7) cung cấp cụ thể việc đo điểm chuẩn dữ liệu việc minh họa
cái gì Pareto-hiệu quả sự nén trông như thế nào (The Lottery Ticket Hypothesis (section 10.3.1.7) provides concrete benchmarking data illustrating what Pareto-efficient compression looks like). Thông qua lặp đi lặp lại sự cắt tỉa, Frankle và Carbin (2019)
đã tìm thấy thưa thớt các mạng phụ (subnetworks) (“chiến thắng các vé (winning tickets)”) trong được kết nối đầy đủ và tích chập (convolutional) các mạng thứ mà
có thể khớp nguyên bản mạng’s bài kiểm tra độ chính xác khi được huấn luyện trong sự cô lập (Through iterative pruning, Frankle and Carbin (2019) found sparse subnetworks (“winning tickets”) in fully connected and convolutional networks that could match the original network’s test accuracy when trained in isolation).
Xổ số Vé các kết quả tiết lộ hình dạng của sự nén các sự đánh đổi: tích cực sự cắt tỉa có thể
bảo tồn độ chính xác cho một vài các kiến trúc và các tác vụ, nhưng có thể chấp nhận sự thưa thớt điểm là thực nghiệm
thay vì phổ quát (The Lottery Ticket results reveal the shape of compression trade-offs: aggressive pruning can preserve accuracy for some architectures and tasks, but the acceptable sparsity point is empirical rather than universal). Sự nén sự xác nhận nên thiết lập tương tự sự đánh đổi các đường cong cho mỗi
cụ thể mô hình và tác vụ, việc xác định nơi mô hình ngồi trên Pareto biên giới và liệu xa hơn
sự nén (có) mang lại có ý nghĩa tính hiệu quả các lợi ích hay chỉ đơn thuần (merely) làm suy thoái chất lượng (Compression validation should establish similar trade-off curves for each specific model and task, identifying where the model sits on the Pareto frontier and whether further compression yields meaningful efficiency gains or merely degrades quality).
12.11.1.4 Lớn ngôn ngữ mô hình các điểm chuẩn (Large language model benchmarks)
Sự nén sự đánh giá bộ khung áp dụng một cách sạch sẽ khi tác vụ có một ổn định nhãn: phân loại
độ chính xác, sự phát hiện mAP, sự phân đoạn (segmentation) IoU (The compression evaluation framework applies cleanly when the task has a stable label: classification accuracy, detection mAP, segmentation IoU). Lớn ngôn ngữ các mô hình phá vỡ đó mẫu (Large language models break that pattern). Một đội có thể
chọn một mô hình bởi vì nó ghi điểm tốt trên một công cộng điểm chuẩn, sau đó khám phá trong sự triển khai rằng
mô hình nhận ra nhiều-lựa chọn các sự thật (facts) nhưng không thể tạo ra một được làm nền tảng câu trả lời, phản hồi quá chậm
cho một tương tác sản phẩm, hay tạo ra tự tin không an toàn văn bản thứ mà điểm chuẩn chưa bao giờ nhấn mạnh (A team can choose a model because it scores well on a public benchmark, then discover in deployment that the model recognizes multiple-choice facts but cannot generate a grounded answer, responds too slowly for an interactive product, or produces confident unsafe text that the benchmark never stressed).
LLM việc đo điểm chuẩn do đó bắt đầu bằng cách việc gọi tên sự triển khai thất bại thứ mà một điểm số được có ý định để loại
trừ (LLM benchmarking therefore starts by naming the deployment failure that a score is meant to rule out).
Hữu ích LLM số liệu phân loại học (taxonomy) trong bảng 12.20 là do đó một quyết định sự hỗ trợ, không (phải) một bảng xếp hạng (The useful LLM metric taxonomy in table 12.20 is therefore a decision aid, not a leaderboard).
Của nó các hàng sử dụng Khổng lồ Đa tác vụ Ngôn ngữ Sự hiểu biết (MMLU)39, HELM (Tổng thể Sự đánh giá
của Ngôn ngữ Các mô hình)40, và sự bối rối41 như các ví dụ của các điểm số thứ mà trả lời khác nhau sự triển khai
các câu hỏi (Its rows use Massive Multitask Language Understanding (MMLU)39, HELM (Holistic Evaluation of Language Models)40, and perplexity41 as examples of scores that answer different deployment questions):
Bảng 12.20: Hướng-tới-sự thất bại LLM điểm chuẩn phân loại học (Failure-oriented LLM benchmark taxonomy): LLM các số liệu là hữu ích khi mỗi điểm số được gắn với sự triển khai
thất bại nó được có ý định để loại trừ (LLM metrics are useful when each score is tied to the deployment failure it is meant to rule out). Sự nhận dạng, tổng thể hành vi, kho ngữ liệu sự dự đoán, và tính phản hồi phơi bày khác nhau các rủi ro, do đó không
đơn điểm số (nào) thiết lập sản xuất sự sẵn sàng (Recognition, holistic behavior, corpus prediction, and responsiveness expose different risks, so no single score establishes production readiness).
Sự triển khai
thất bại để loại trừ (Deployment failure to rule out)
Số liệu hay điểm chuẩn
gia đình (Metric or benchmark family)
Cái gì điểm số tiết lộ (What the score reveals)
Cái gì điểm số không thể chứng minh (What the score cannot prove)
Mô hình
nhận ra các sự thật
kém (The model recognizes facts poorly)
MMLU (Khổng lồ
Đa tác vụ Ngôn ngữ
Sự hiểu biết (Massive Multitask Language Understanding))
Rộng thực tế (factual) và thuộc về kỷ luật (disciplinary)
kiến thức qua năm mươi-bảy
các chủ đề, với các điểm số có thể diễn giải
chống lại mức độ-cơ hội (chance-level)
nhiều-lựa chọn hiệu suất (Broad factual and disciplinary knowledge across fifty-seven subjects, with scores interpretable against chance-level multiple-choice performance)
Liệu mô hình (có) thể tạo ra
được làm nền tảng kết thúc-mở các câu trả lời
thay vì chọn trong số
nhiều-lựa chọn các lựa chọn (Whether the model can generate grounded open-ended answers rather than choose among multiple-choice options)
Mô hình là
có khả năng nhưng không an toàn (The model is capable but unsafe)
HELM (Tổng thể
Sự đánh giá của Ngôn ngữ
Các mô hình (Holistic Evaluation of Language Models))
Độ chính xác bên cạnh sự hiệu chuẩn,
tính mạnh mẽ, tính công bằng, sự thiên vị, tính độc hại,
và tính hiệu quả (Accuracy alongside calibration, robustness, fairness, bias, toxicity, and efficiency)
Liệu một tổng hợp điểm số
(có) nắm bắt sự triển khai rủi ro; một
mô hình có thể là mạnh trên độ chính xác
và yếu trên sự hiệu chuẩn, tính an toàn, chi phí,
hay dấu nhắc tính ổn định (Whether one aggregate score captures the deployment risk; a model can be strong on accuracy and weak on calibration, safety, cost, or prompt stability)
Mô hình dự đoán
của nó kho ngữ liệu tốt (The model predicts its corpus well)
Sự bối rối (Perplexity)
Được giữ-lại mã thông báo-tiếp theo sự dự đoán trên
giống nhau kho ngữ liệu; một sự bối rối của 10
có nghĩa (rằng) mô hình là “10-chiều
bối rối” trên trung bình (Held-out next-token prediction on the same corpus; a perplexity of 10 means the model is “10-way confused” on average)
Liệu được tạo ra các câu trả lời (có) là
hữu ích, an toàn, hay được làm nền tảng bên ngoài
đó kho ngữ liệu (Whether generated answers are helpful, safe, or grounded outside that corpus)
Mô hình cảm thấy
chậm trong (việc) sử dụng (The model feels slow in use)
Đầu tiên-mã thông báo (First-token) độ trễ,
giữa-các mã thông báo (inter-token) độ trễ, và
mã thông báo thông lượng (token throughput)
Dấu nhắc-việc xử lý sự trì hoãn trước khi
sự tạo sinh bắt đầu và giải mã
tốc độ sau khi sự tạo sinh bắt đầu (Prompt-processing delay before generation starts and decode speed after generation begins)
Liệu một đơn thông lượng
con số (có) giấu kém tương tác
tính phản hồi, đặc biệt khi
việc tạo lô cải thiện thông lượng nhưng
làm tồi tệ hơn đầu tiên-mã thông báo độ trễ (Whether a single throughput number hides poor interactive responsiveness, especially when batching improves throughput but worsens first-token latency)

12. Việc đo điểm chuẩn (Benchmarking)
699
Tính phản hồi hàng xứng đáng (một) cụ thể định thời gian mỏ neo (anchor) bởi vì LLM các điểm chuẩn thường báo cáo
một đơn thông lượng con số mặc dù người dùng trải nghiệm sự tạo sinh trong các pha (The responsiveness row deserves a concrete timing anchor because LLM benchmarks often report a single throughput number even though users experience generation in phases). Một mô hình có thể trông
hiệu quả trong các mã thông báo mỗi giây trong khi vẫn cảm thấy chậm nếu đầu tiên mã thông báo đến muộn, hay nó có thể cải thiện
đầu tiên-mã thông báo độ trễ trong khi việc tạo ra phần còn lại của câu trả lời quá chậm cho một tương tác quy trình làm việc (A model can look efficient in tokens per second while still feeling slow if the first token arrives late, or it can improve first-token latency while producing the rest of the answer too slowly for an interactive workflow).
Nhỏ sự tính toán bên dưới biến những mã thông báo-tỷ lệ các số liệu đó vào có thể nhìn thấy-cho người dùng đồng hồ-treo tường (wall-clock) thời gian (The small calculation below turns those token-rate metrics into user-visible wall-clock time).
Mã thông báo thông lượng biến đó sự đánh đổi vào đồng hồ-treo tường thời gian (Token throughput turns that trade-off into wall-clock time). Cho một sự phản hồi của khoảng 750 các mã thông báo, 25
các mã thông báo/giây có nghĩa (là) 30 giây của sự tạo sinh, trong khi 100 các mã thông báo/giây có nghĩa (là) 7.5 giây (For a response of about 750 tokens, 25 tokens/s means 30 seconds of generation, while 100 tokens/s means 7.5 seconds). Thời gian-tới-đầu tiên-mã thông báo (Time-to-first-token)
và giữa-các mã thông báo độ trễ phải do đó được báo cáo cùng nhau: một (cái) nắm bắt tính phản hồi tại
bắt đầu của sự trao đổi, và (cái) khác nắm bắt tỷ lệ tại đó câu trả lời đến (Time-to-first-token and inter-token latency must therefore be reported together: one captures responsiveness at the start of the exchange, and the other captures the rate at which the answer arrives).
Cuối cùng thất bại là rằng một điểm số có thể đo lường bộ nhớ thay vì khả năng (The final failure is that a score may measure memory rather than capability). Điểm chuẩn sự ô-
nhiễm (contamination) là một độc đáo LLM rủi ro bởi vì các mô hình được huấn luyện trên web-quy mô các kho ngữ liệu có thể chạm trán
điểm chuẩn các câu hỏi trong suốt việc tiền huấn luyện, việc bơm phồng (inflating) các điểm số thông qua sự ghi nhớ thay vì kỹ năng
(Xu et al. 2024) (Benchmark contamination is a unique LLM risk because models trained on web-scale corpora may encounter benchmark questions during pretraining, inflating scores through memorization rather than skill (Xu et al. 2024)). Sự rò rỉ sự phát hiện đóng khung lại (reframes) này rủi ro như thứ gì đó điểm chuẩn các nhà thiết kế có thể kiểm tra
cho thay vì chỉ đơn thuần nghi ngờ (Leakage detection reframes this risk as something benchmark designers can test for rather than merely suspect). Thuộc về thời gian các sự giữ-lại (holdouts) sử dụng nội dung được xuất bản sau huấn luyện cắt (cutoff),
động các điểm chuẩn tạo ra mới (fresh) các trường hợp một cách liên tục, và sự ô nhiễm các bài kiểm tra hỏi liệu
mô hình (có) nhớ lại chính xác điểm chuẩn cách diễn đạt (Temporal holdouts use content published after the training cutoff, dynamic benchmarks generate fresh instances continuously, and contamination tests ask whether the model recalls exact benchmark phrasing). Những các kỹ thuật này giữ điểm chuẩn được căn chỉnh với
sự triển khai câu hỏi thay vì việc khen thưởng sự phơi bày (exposure) tới bài kiểm tra tập (These techniques keep the benchmark aligned with the deployment question instead of rewarding exposure to the test set).
12.11.2 Dữ liệu việc đo điểm chuẩn (Data benchmarking)
Mô hình các điểm chuẩn xác nhận liệu sự nén (có) đã bảo tồn mô hình chất lượng (hay không) (Model benchmarks validate whether compression preserved model quality). Mô hình chất lượng, tuy nhiên,
phụ thuộc hoàn toàn trên dữ liệu được sử dụng để huấn luyện và đánh giá nó, và này sự phụ thuộc tạo ra nhất
xảo quyệt (insidious) thất bại chế độ trong ML sự triển khai (Model quality, however, depends entirely on the data used to train and evaluate it, and this dependency creates the most insidious failure mode in ML deployment). Một một cách hoàn hảo được bảo tồn mô hình được huấn luyện trên bị thiên vị hay
không mang tính đại diện dữ liệu sẽ vẫn thất bại trong sản xuất (A perfectly preserved model trained on biased or unrepresentative data will still fail in production). Dữ liệu các điểm chuẩn xác nhận liệu tính hiệu quả
các chiến lược từ Chương 9 (chủ động học tập, chương trình học (curriculum) thiết kế, dữ liệu sự gia tăng, và tổng hợp dữ liệu
sự tạo sinh) (có) đã tạo ra huấn luyện các tập thứ mà kích hoạt đáng tin cậy sự triển khai (hay không) (Data benchmarks validate whether the efficiency strategies from Chapter 9 (active learning, curriculum design, data augmentation, and synthetic data generation) produced training sets that enable reliable deployment). Này là thường cuối cùng sự xác nhận
để thất bại và khó nhất để chẩn đoán: một mô hình việc đạt được xuất sắc độ chính xác trên được giữ-lại bài kiểm tra dữ liệu có thể
sụp đổ trên sản xuất các đầu vào thứ mà huấn luyện dữ liệu chưa bao giờ một cách đầy đủ đại diện (This is often the last validation to fail and the hardest to diagnose: a model achieving excellent accuracy on held-out test data may collapse on production inputs that the training data never adequately represented).
Đương đại (Contemporary) AI sự phát triển tiết lộ rằng dữ liệu chất lượng thường xác định hiệu suất các ranh giới
nhiều hơn mô hình kiến trúc (Contemporary AI development reveals that data quality often determines performance boundaries more than model architecture). Này sự công nhận đã nâng cao (elevated) dữ liệu việc đo điểm chuẩn từ suy nghĩ muộn màng (afterthought) tới
chí mạng kỷ luật (This recognition elevated data benchmarking from afterthought to critical discipline).
Một dữ liệu điểm chuẩn do đó bắt đầu với một giao thức trước khi nó bắt đầu với một điểm số (A data benchmark therefore starts with a protocol before it starts with a score). Xác định sự triển-
khai lát cắt (slice) mô hình phải phục vụ, dự trữ một chống rò rỉ (leakage-resistant) sự giữ-lại, xác minh bản sao (duplicate) và
gần-bản sao sự tách biệt (separation) qua các phân vùng (partitions), đặt tối thiểu độ bao phủ cho hiếm các lớp và các nhóm phụ,
kiểm toán nhãn chất lượng, và thiết lập sự trôi dạt các ngưỡng thứ mà xác định khi (nào) điểm chuẩn không còn
đại diện cho sản xuất (Define the deployment slice the model must serve, reserve a leakage-resistant holdout, verify duplicate and near-duplicate separation across partitions, set minimum coverage for rare classes and subgroups, audit label quality, and establish drift thresholds that determine when the benchmark no longer represents production). Chỉ sau khi những các cổng đó là rõ ràng (thì) tổng hợp các số liệu (mới) trở nên có thể diễn giải (được) (Only after those gates are explicit do aggregate metrics become interpretable).
Độ bao phủ các số liệu (Coverage metrics)
Đầu tiên câu hỏi dữ liệu việc đo điểm chuẩn phải trả lời là liệu huấn luyện dữ liệu (có) đại diện cho các đầu vào
mô hình sẽ chạm trán (The first question data benchmarking must answer is whether the training data represents the inputs the model will encounter). Một mô hình không thể học các mẫu nó chưa bao giờ nhìn thấy, và các cách huấn luyện
dữ liệu có thể thất bại để đại diện cho sự triển khai thực tế là thường tinh tế (A model cannot learn patterns it has never seen, and the ways training data can fail to represent deployment reality are often subtle).
Hãy xem xét lớp sự cân bằng: một gian lận sự phát hiện tập dữ liệu với 99 phần trăm hợp pháp các giao dịch và 1
phần trăm gian lận có thể tạo ra một mô hình thứ mà đạt được 99 phần trăm độ chính xác bằng cách chỉ đơn giản việc dán nhãn mọi thứ
hợp pháp (Consider class balance: a fraud detection dataset with 99 percent legitimate transactions and 1 percent fraud might produce a model that achieves 99 percent accuracy by simply labeling everything legitimate). Mô hình là vô dụng, nhưng độ chính xác số liệu trông xuất sắc (The model is useless, but the accuracy metric looks excellent). Nghiêm trọng sự mất cân bằng thường
yêu cầu sự giảm nhẹ thông qua việc lấy mẫu quá mức (oversampling), lớp việc lấy trọng số, hay ngưỡng sự điều chỉnh (Severe imbalance often requires mitigation through oversampling, class weighting, or threshold adjustment). Nhiều xảo quyệt hơn
là nhóm phụ sự mất cân bằng bên trong các lớp: một tập dữ liệu có thể có cân bằng tích cực và tiêu cực các ví dụ
tổng thể, nhưng tiêu cực các ví dụ có thể được rút ra chủ yếu từ một nhân khẩu học nhóm, việc tạo ra
các sự chênh lệch (disparities) vô hình tới tổng hợp lớp sự cân bằng các số liệu (More insidious is subgroup imbalance within classes: a dataset might have balanced positive and negative examples overall, but negative examples might be drawn predominantly from one demographic group, creating disparities invisible to aggregate class balance metrics).
Tính năng độ bao phủ đưa ra một thậm chí khó hơn thách thức bởi vì nó yêu cầu miền kiến thức về
cái gì các sự biến thiên quan trọng (Feature coverage presents an even harder challenge because it requires domain knowledge about what variations matter). Một máy tính thị giác mô hình được huấn luyện độc quyền trên ban ngày các hình ảnh sẽ
thất bại trên ban đêm các đầu vào; một tự nhiên ngôn ngữ mô hình được huấn luyện trên trang trọng văn bản sẽ thất bại trên thông tục (colloquial)
ngôn ngữ (A computer vision model trained exclusively on daytime images will fail on nighttime inputs; a natural language model trained on formal text will fail on colloquial language). Không giống như lớp sự cân bằng, thứ mà có thể được tính toán từ các nhãn một mình, tính năng độ bao phủ yêu cầu
việc hiểu sự triển khai ngữ cảnh (Unlike class balance, which can be computed from labels alone, feature coverage requires understanding the deployment context). Ánh sáng các điều kiện camera sẽ chạm trán,
các phương ngữ (dialects) người dùng sẽ nói, và biên các trường hợp thứ mà tồn tại trong sản xuất nhưng chưa bao giờ xuất hiện trong bài kiểm tra các tập
tất cả rơi ra ngoài cái gì các nhãn một mình có thể dự đoán (The lighting conditions the camera will encounter, the dialects users will speak, and the edge cases that exist in production but never appear in test sets all fall outside what labels alone can predict). Những các câu hỏi này có không thuộc về thuật toán câu trả lời; chúng
đòi hỏi sự hợp tác giữa ML các kỹ sư và miền các chuyên gia (những) người hiểu sự triển khai
môi trường (These questions have no algorithmic answer; they demand collaboration between ML engineers and domain experts who understand the deployment environment).

700
12.11 Mô hình và Dữ liệu Sự đánh giá (Model and Data Evaluation)
42
WILDS: Stanford’s 2021
điểm chuẩn của mười các tập dữ liệu
với thế giới-thực sự phân phối
các sự dịch chuyển (shifts): bệnh viện bệnh nhân quần thể
các sự thay đổi (Camelyon17),
động vật hoang dã
camera
vị trí
các sự dịch chuyển
(iWildCam),
và
vệ tinh
hình ảnh (imagery)
thuộc về thời gian
sự trôi dạt (PovertyMap) (WILDS: Stanford’s 2021 benchmark of ten datasets with real-world distribution shifts: hospital patient population changes (Camelyon17), wildlife camera location shifts (iWildCam), and satellite imagery temporal drift (PovertyMap)). WILDS
định lượng sự triển khai
khoảng cách:
các mô hình
việc đạt được
97
phần trăm
trong-sự phân phối
độ chính xác
có thể
sụt giảm
tới
70
phần trăm dưới những thực tế
các sự dịch chuyển này,
việc chứng minh
rằng
tiêu chuẩn được giữ-lại sự đánh giá
một cách có hệ thống ước tính quá cao (overestimates)
sản xuất
hiệu suất
khi i.i.d.
giả định
thất bại (WILDS quantifies the deployment gap: models achieving 97 percent in-distribution accuracy can drop to 70 percent under these realistic shifts, demonstrating that standard held-out evaluation systematically overestimates production performance when the i.i.d. assumption fails).
Cho các ứng dụng việc ảnh hưởng (tới) mọi người, nhân khẩu học sự đại diện trở thành một độ bao phủ chiều
với thuộc về đạo đức (ethical) các tác động (For applications affecting people, demographic representation becomes a coverage dimension with ethical implications). Huấn luyện dữ liệu phải đại diện sự triển khai quần thể qua liên quan
các chiều: tuổi tác, giới tính, dân tộc, địa lý, ngôn ngữ (Training data must represent the deployment population across relevant dimensions: age, gender, ethnicity, geography, language). Một khuôn mặt sự nhận dạng hệ thống được huấn luyện
chủ yếu trên một nhân khẩu học nhóm sẽ một cách có hệ thống kém hiệu quả trên những (nhóm) khác, thậm chí nếu
tổng hợp độ chính xác các số liệu trông (có vẻ) có thể chấp nhận (A facial recognition system trained predominantly on one demographic group will systematically underperform on others, even if aggregate accuracy metrics look acceptable). Thách thức là rằng nhân khẩu học siêu dữ liệu (metadata) là thường
không có sẵn hay không đáng tin cậy, việc làm cho sự đại diện các khoảng cách khó để phát hiện và đo lường (The challenge is that demographic metadata is often unavailable or unreliable, making representation gaps difficult to detect and measure).
Chất lượng các số liệu (Quality metrics)
Thậm chí khi huấn luyện dữ liệu bao phủ đúng các đầu vào, các nhãn chính chúng có thể là không đáng tin cậy (Even when training data covers the right inputs, the labels themselves may be unreliable). Các nghiên cứu
một cách nhất quán tìm thấy 3–6 phần trăm nhãn lỗi các tỷ lệ trong lớn các tập dữ liệu, bao gồm ImageNet (Northcutt et al.
2021) (Studies consistently find 3–6 percent label error rates in major datasets, including ImageNet (Northcutt et al. 2021)). Những các lỗi này là không chỉ đơn thuần (merely) tiếng ồn—chúng trở thành được học sự thật cơ bản (ground truth) (These errors are not merely noise—they become learned ground truth). Một mô hình được huấn luyện trên
dữ liệu nơi bầy sói là thỉnh thoảng được dán nhãn như bầy chó sẽ học sai quy tắc rằng một vài bầy sói là bầy chó (A model trained on data where wolves are occasionally labeled as dogs will learn the false rule that some wolves are dogs).
Điểm chuẩn sẽ báo cáo này như đúng hành vi bởi vì mô hình khớp (không chính xác) các nhãn (The benchmark will report this as correct behavior because the model matches the (incorrect) labels).
Cho nhỏ các tập dữ liệu, thủ công sự kiểm toán (audit) của một ngẫu nhiên mẫu có thể ước tính nhãn độ chính xác (For small datasets, manual audit of a random sample can estimate label accuracy). Cho lớn
các tập dữ liệu, tự tin học tập các kỹ thuật xác định nhiều khả năng bị dán nhãn sai các ví dụ bằng cách việc tìm các trường hợp nơi
mô hình các dự đoán một cách có hệ thống không đồng ý với các nhãn (For large datasets, confident learning techniques identify likely mislabeled examples by finding cases where model predictions systematically disagree with labels). Trực giác là rằng khi một mô hình một cách tự tin
dự đoán một khác nhãn hơn sự thật cơ bản, hoặc là mô hình đã học thứ gì đó không chính xác hoặc là
nhãn là sai (The intuition is that when a model confidently predicts a different label than the ground truth, either the model has learned something incorrect or the label is wrong). Sự phát hiện, tuy nhiên, là chỉ đầu tiên bước; sự sửa chữa yêu cầu con người sự đánh giá, và
việc mở rộng quy mô con người sự đánh giá tới hàng triệu của các ví dụ đưa ra của riêng nó các thách thức (Detection, however, is only the first step; correction requires human review, and scaling human review to millions of examples presents its own challenges).
Giữa các người chú thích (Inter-annotator) sự thỏa thuận (agreement) cung cấp một khác thấu kính trên nhãn chất lượng bằng cách việc đo lường tính nhất quán
qua con người những người dán nhãn (Inter-annotator agreement provides a different lens on label quality by measuring consistency across human labelers). Cohen’s kappa hay Fleiss’ kappa định lượng sự thỏa thuận vượt ra ngoài cái gì cơ hội
sẽ tạo ra (Cohen 1960; Fleiss 1971) (Cohen’s kappa or Fleiss’ kappa quantify agreement beyond what chance would produce (Cohen 1960; Fleiss 1971)). Khi sự thỏa thuận rơi bên dưới thông thường các ngưỡng cho
các tác vụ với rõ ràng sự thật cơ bản, thứ gì đó là sai: hoặc là việc dán nhãn các hướng dẫn là mơ hồ,
tác vụ là vốn dĩ chủ quan, hay người dán nhãn chất lượng biến đổi một cách đáng kể (When agreement falls below conventional thresholds for tasks with clear ground truth, something is wrong: either the labeling guidelines are ambiguous, the task is inherently subjective, or labeler quality varies significantly). Landis và Koch’s định tính
kappa các dải là một cách rộng rãi được trích dẫn như một thô thuộc về sự diễn giải hướng dẫn, mặc dù chúng không nên thay thế miền
phán đoán (Landis and Koch 1977) (Landis and Koch’s qualitative kappa bands are widely cited as a rough interpretive guide, though they should not replace domain judgment (Landis and Koch 1977)).
Sự phân biệt giữa ngẫu nhiên và có hệ thống các lỗi quan trọng một cách to lớn (enormously) cho của chúng hạ lưu
các hiệu ứng (The distinction between random and systematic errors matters enormously for their downstream effects). Ngẫu nhiên nhãn tiếng ồn một phần tính trung bình ra (averages out) trong suốt huấn luyện: nếu khác nhau các ví dụ bị dán-
nhãn sai trong khác nhau các hướng, mô hình học trung tâm xu hướng (Random label noise partially averages out during training: if different examples are mislabeled in different directions, the model learns the central tendency). Có hệ thống các lỗi (một cách nhất quán
việc dán nhãn sai một cụ thể lớp phụ (subclass)), trong sự tương phản, được học như sự thật cơ bản (Systematic errors (consistently mislabeling a particular subclass), in contrast, are learned as ground truth). Một tập dữ liệu nơi tất cả
bầy sói được chụp ảnh trong tuyết được dán nhãn “bầy chó” sẽ tạo ra một mô hình thứ mà gọi có tuyết bầy sói (là) bầy chó,
và không số lượng của bổ sung dữ liệu sửa chữa này mà không có việc sửa chữa có hệ thống lỗi tại của nó nguồn (A dataset where all wolves photographed in snow are labeled “dogs” will produce a model that calls snowy wolves dogs, and no amount of additional data fixes this without correcting the systematic error at its source).
Sự phân phối sự căn chỉnh (Distribution alignment)
Cuối cùng thể loại của dữ liệu việc đo điểm chuẩn hỏi liệu các mô hình sẽ khái quát hóa từ huấn luyện các điều-
kiện tới sự triển khai thực tế (The final category of data benchmarking asks whether models will generalize from training conditions to deployment reality). Này huấn luyện-tới-sản xuất sự căn chỉnh câu hỏi là nơi khoảng cách giữa
điểm chuẩn hiệu suất và sản xuất hiệu suất hầu hết thường xuyên nổi lên (This train-to-production alignment question is where the gap between benchmark performance and production performance most frequently emerges).
Tiêu chuẩn giả định việc nằm dưới được giữ-lại sự đánh giá, rằng bài kiểm tra dữ liệu đến từ giống nhau
sự phân phối như huấn luyện dữ liệu, bị một cách thường lệ vi phạm trong thực tiễn (The standard assumption underlying held-out evaluation, that test data comes from the same distribution as training data, is routinely violated in practice). Bài kiểm tra các tập được xây dựng các năm sau
huấn luyện dữ liệu có thể phản ánh sự phân phối sự trôi dạt (drift) khi thế giới thay đổi (Test sets constructed years after training data may reflect distribution drift as the world changes). Bài kiểm tra các tập từ khác nhau địa lý
các khu vực có thể phản ánh quần thể sự dịch chuyển (Test sets from different geographic regions may reflect population shift). Một mô hình với mạnh mẽ được giữ-lại độ chính xác có thể sụt giảm một cách sắc nét khi
được triển khai tới một khu vực hay thời gian khoảng thời gian bài kiểm tra tập đã không đại diện (A model with strong held-out accuracy can drop sharply when deployed to a region or time period the test set did not represent). Tiêu chuẩn được giữ-lại sự đánh giá
ước tính quá cao sự triển khai hiệu suất bất cứ khi nào i.i.d. (độc lập và một cách giống hệt được phân phối)
giả định thất bại (Standard held-out evaluation overestimates deployment performance whenever the i.i.d. (independent and identically distributed) assumption fails).
Thực sự bài kiểm tra là huấn luyện-tới-sản xuất sự căn chỉnh, và này là khó hơn nhiều để đo lường bởi vì sản xuất
dữ liệu khác biệt từ huấn luyện dữ liệu theo các cách thứ mà được giữ-lại bài kiểm tra các tập thường thất bại để nắm bắt (The true test is train-to-production alignment, and this is far harder to measure because production data differs from training data in ways that held-out test sets often fail to capture). Sản xuất các hình ảnh
đến từ khác nhau các camera với khác nhau các đặc điểm (Production images come from different cameras with different characteristics). Sản xuất người dùng đến từ khác nhau
các quần thể với khác nhau các hành vi (Production users come from different populations with different behaviors). Sản xuất các đầu vào bao gồm biên các trường hợp thứ mà được tuyển chọn bài kiểm tra các tập
một cách có hệ thống loại trừ (Production inputs include edge cases that curated test sets systematically exclude). WILDS42 điểm chuẩn (Koh et al. 2021) đã được thiết kế một cách cụ thể để đánh-
giá các mô hình dưới thực tế sự phân phối các sự dịch chuyển: bệnh viện các hệ thống với khác nhau bệnh nhân các quần thể,
động vật hoang dã các camera tại khác nhau các vị trí, vệ tinh hình ảnh từ khác nhau thời gian các khoảng thời gian (The WILDS42 benchmark (Koh et al. 2021) was designed specifically to evaluate models under realistic distribution shifts: hospital systems with different patient populations, wildlife cameras at different locations, satellite imagery from different time periods). Các kết quả
tiết lộ một khắc nghiệt (stark) thực tế: các mô hình việc đạt được 90 phần trăm+ độ chính xác trên trong-sự phân phối bài kiểm tra các tập có thể sụt giảm
tới 60 phần trăm dưới những thực tế các sự dịch chuyển này (The results reveal a stark reality: models achieving 90 percent+ accuracy on in-distribution test sets may drop to 60 percent under these realistic shifts).
Cho trước (Given) những các thách thức này, sự dịch chuyển sự phát hiện các phương pháp trở nên thiết yếu cho sản xuất sự giám sát (Given these challenges, shift detection methods become essential for production monitoring).
Thuộc về thống kê các bài kiểm tra giống như Kolmogorov-Smirnov bài kiểm tra (Berger và Zhou 2014) hay dựa trên-hạt nhân (kernel-based) hai-
mẫu các bài kiểm tra chẳng hạn như Tối đa Trung bình Sự khác biệt (Maximum Mean Discrepancy) (MMD) (Gretton et al. 2012) có thể phát hiện hiệp biến (covariate)

12. Việc đo điểm chuẩn (Benchmarking)
701
43
DataComp: Được giới thiệu
trong 2023, DataComp đảo ngược
tiêu chuẩn điểm chuẩn bằng cách việc cố-
định mô hình và huấn luyện
mã, việc để những người tham gia cạnh-
tranh trên tập dữ liệu sự tuyển chọn một mình (DataComp: Introduced in 2023, DataComp inverts the standard benchmark by fixing the model and training code, letting participants compete on dataset curation alone).
Các kết quả đã cho thấy rằng một một cách cẩn-
thận được lọc 30 phần trăm mạng-
con đã khớp các mô hình được huấn luyện
trên 10× lớn hơn không được lọc dữ liệu,
việc định lượng một các hệ thống sự thấu hiểu:
cho nhiều các khối lượng công việc, việc thiết-
kế dữ liệu đường ống mang lại
lớn hơn hiệu suất các lợi ích mỗi
đô la hơn việc mở rộng quy mô tính toán (Results showed that a carefully filtered 30 percent subset matched models trained on 10× larger unfiltered data, quantifying a systems insight: for many workloads, engineering the data pipeline yields greater performance gains per dollar than scaling compute).
44
Dynabench: Facebook AI
Research’s 2021 nền tảng cho
động điểm chuẩn sự tạo-
sinh, nơi con người tạo (craft) đối-
kháng các đầu vào thứ mà đánh lừa hiện-
tại tốt nhất các mô hình (Dynabench: Facebook AI Research’s 2021 platform for dynamic benchmark generation, where humans craft adversarial inputs that fool current best models). Dynabench
giải quyết sự bão hòa vấn-
đề, nơi rất cao độ chính-
xác trên tĩnh các điểm chuẩn
có thể phản ánh bài kiểm tra-tập sự quen thuộc
thay vì mạnh mẽ khả năng,
nhưng giới thiệu của riêng nó sự đánh-
đổi:
động các điểm chuẩn
là khó hơn để so sánh qua
thời gian bởi vì sự đánh giá
tập thay đổi (Dynabench addresses the saturation problem, where very high accuracy on static benchmarks may reflect test-set familiarity rather than robust capability, but introduces its own trade-off: dynamic benchmarks are harder to compare across time because the evaluation set changes).
Tĩnh và động
các điểm chuẩn phục vụ bổ-
sung (complementary) chẩn đoán các vai trò (Static and dynamic benchmarks serve complementary diagnostic roles).
sự dịch chuyển—khi sự phân phối của các đầu vào thay đổi thậm chí nếu mối quan hệ giữa các đầu vào và các đầu ra
duy trì ổn định (shift—when the distribution of inputs changes even if the relationship between inputs and outputs remains stable). Việc giám sát mô hình độ tự tin các sự phân phối có thể phát hiện khi mô hình chạm trán
các đầu vào không giống bất cứ thứ gì trong huấn luyện (Monitoring model confidence distributions can detect when the model encounters inputs unlike anything in training). Mục tiêu là sớm sự phát hiện: việc xác định sự phân phối sự dịch chuyển trước khi nó
gây ra thảm khốc hiệu suất sự suy thoái, việc kích hoạt sự can thiệp thông qua mô hình các bản cập nhật, dữ liệu
sự thu thập, hay sự triển khai các sự ràng buộc (The goal is early detection: identifying distribution shift before it causes catastrophic performance degradation, enabling intervention through model updates, data collection, or deployment constraints).
Sự phân phối sự căn chỉnh các thách thức làm nổi bật một dai dẳng sự căng thẳng (tension) trong ML sự phát triển giữa hai
các mô hình (paradigms): việc cố định dữ liệu và việc lặp (iterating) trên các mô hình, hoặc việc cố định mô hình và việc lặp trên dữ liệu (Distribution alignment challenges highlight a persistent tension in ML development between two paradigms: fixing the data and iterating on models, or fixing the model and iterating on data). Hình 12.12
đặt hai các mô hình này bên cạnh (side by side), việc tiết lộ chính xác nơi phản hồi vòng lặp khác biệt (Figure 12.12 places these two paradigms side by side, revealing exactly where the feedback loop differs). Trong
lấy-mô hình làm trung tâm (model-centric) sơ đồ, sự lặp vòng đời nhắm mục tiêu kiến trúc trong khi dữ liệu duy trì tĩnh; trong
lấy-dữ liệu làm trung tâm (data-centric) sơ đồ, kiến trúc giữ nguyên cố định trong khi vòng đời nhắm mục tiêu dữ liệu chất lượng (In the model-centric diagram, the iteration cycle targets the architecture while the data remains static; in the data-centric diagram, the architecture stays fixed while the cycle targets data quality). Nghiên cứu
ngày càng chứng minh rằng có phương pháp tập dữ liệu sự tăng cường có thể mang lại vượt trội hiệu suất
các lợi ích được so sánh với mô hình các sự tinh chỉnh một mình—việc thách thức thông thường sự nhấn mạnh trên thuộc về kiến trúc
sự đổi mới (Research increasingly demonstrates that methodical dataset enhancement can yield superior performance gains compared to model refinements alone—challenging the conventional emphasis on architectural innovation).
CPU
Mô hình (Model)
Dữ liệu (Data)
Một cách có hệ thống tăng cường mô hình (Systematically enhance the model)
Lấy-mô hình làm trung tâm AI (Model-centric AI)
CPU
Mô hình (Model)
Dữ liệu (Data)
Một cách có hệ thống tăng cường dữ liệu (Systematically enhance the data)
Lấy-dữ liệu làm trung tâm AI (Data-centric AI)
Bổ sung (Complementary)
Hình 12.12: Sự phát triển Các mô hình (Development Paradigms): Lấy-mô hình làm trung tâm AI ưu tiên thuộc về kiến trúc sự đổi mới với cố định các tập dữ liệu, trong khi
lấy-dữ liệu làm trung tâm AI một cách có hệ thống cải thiện tập dữ liệu chất lượng (các chú thích (annotations), sự đa dạng, và sự thiên vị) với nhất quán mô hình các kiến trúc để
đạt được hiệu suất các lợi ích (Model-centric AI prioritizes architectural innovation with fixed datasets, while data-centric AI systematically improves dataset quality (annotations, diversity, and bias) with consistent model architectures to achieve performance gains). Hiện đại nghiên cứu chỉ ra rằng chiến lược dữ liệu sự tăng cường thường mang lại lớn hơn các sự cải thiện hơn
duy nhất việc tinh chỉnh mô hình tính phức tạp (Modern research indicates that strategic data enhancement often yields greater improvements than solely refining model complexity).
Lấy-dữ liệu làm trung tâm AI phản ánh một quan trọng sự dịch chuyển trong việc hiểu thứ mà thách thức “nhiều hơn dữ liệu là
luôn tốt hơn” giả định: tốt hơn các tập dữ liệu, không chỉ lớn hơn những (tập dữ liệu), tạo ra nhiều hơn đáng tin cậy và có thể khái quát-
hóa AI các hệ thống (Data-centric AI reflects an important shift in understanding that challenges the “more data is always better” assumption: better datasets, not just larger ones, produce more reliable and generalizable AI systems). Các sáng kiến giống như DataPerf (Mazumder et al. 2023) và DataComp43 đã nổi lên để
một cách có hệ thống đánh giá cách nào tập dữ liệu các sự cải thiện ảnh hưởng mô hình hiệu suất (Initiatives like DataPerf (Mazumder et al. 2023) and DataComp43 have emerged to systematically evaluate how dataset improvements affect model performance). Cho ví dụ, Dat-
aComp (Gadre et al. 2023) đã chứng minh rằng các mô hình được huấn luyện trên một một cách cẩn thận được tuyển chọn 30 phần trăm
tập con của dữ liệu đã đạt được tốt hơn các kết quả hơn những (mô hình) được huấn luyện trên hoàn chỉnh tập dữ liệu, việc thách thức
giả định rằng nhiều hơn dữ liệu một cách tự động dẫn tới tốt hơn hiệu suất (For instance, DataComp (Gadre et al. 2023) demonstrated that models trained on a carefully curated 30 percent subset of data achieved better results than those trained on the complete dataset, challenging the assumption that more data automatically leads to better performance).
Một dai dẳng thách thức trong dữ liệu việc đo điểm chuẩn nổi lên từ tập dữ liệu sự bão hòa (A persistent challenge in data benchmarking emerges from dataset saturation). Khi các mô hình
đạt được gần như-hoàn hảo độ chính xác trên các điểm chuẩn giống như ImageNet, những người thực hành phải phân biệt liệu
hiệu suất các lợi ích đại diện (cho) đích thực khả năng các sự tiến bộ hay chỉ đơn thuần sự tối ưu hóa tới tồn tại bài kiểm tra các tập (When models achieve near-perfect accuracy on benchmarks like ImageNet, practitioners must distinguish whether performance gains represent genuine capability advances or merely optimization to existing test sets).
Như dòng thời gian (timeline) trong hình 12.13 minh họa, một cách rộng rãi được theo dõi AI các điểm chuẩn đã lặp đi lặp lại vượt qua
được báo cáo con người các cơ sở, việc làm cho mỗi tương ứng điểm chuẩn (trở nên) kém hữu ích như một bộ phân biệt (differentiator)
(Maslej et al. 2024) (As the timeline in figure 12.13 illustrates, widely tracked AI benchmarks have repeatedly crossed reported human baselines, making each corresponding benchmark less useful as a differentiator (Maslej et al. 2024)).
Tập dữ liệu sự bão hòa và động các điểm chuẩn (Dataset saturation and dynamic benchmarks)
Hình 12.13 đưa ra một chí mạng thuộc về phương pháp luận vấn đề: khi các mô hình vượt qua con người hiệu suất
trên các điểm chuẩn, kết quả có thể phản ánh hoặc là đích thực khả năng các sự tiến bộ hoặc là sự tối ưu hóa tới tĩnh
sự đánh giá các tập, và hai (điều này) là khó để phân biệt từ bảng xếp hạng các điểm số một mình (Figure 12.13 raises a critical methodological problem: when models surpass human performance on benchmarks, the result may reflect either genuine capability advances or optimization to static evaluation sets, and the two are difficult to distinguish from leaderboard scores alone). MNIST,
được giới thiệu thông qua kinh điển viết tay-chữ số sự nhận dạng công việc của LeCun và các đồng nghiệp (LeCun
et al. 1998), minh họa mối quan tâm: tĩnh bài kiểm tra các hình ảnh có thể chứa cụ thể-tập dữ liệu các hiện vật (artifacts) thứ mà các mô hình
học để khai thác (MNIST, introduced through the classic handwritten-digit recognition work of LeCun and colleagues (LeCun et al. 1998), illustrates the concern: static test images can contain dataset-specific artifacts that models learn to exploit). Câu hỏi “Chúng ta (có) xong với ImageNet?” (Beyer et al. 2020) khái quát hóa này
mối quan tâm (The question “Are we done with ImageNet?” (Beyer et al. 2020) generalizes this concern).
Động việc đo điểm chuẩn các cách tiếp cận giống như Dynabench44 (Kiela et al. 2021) giải quyết sự bão hòa bằng cách
một cách liên tục việc tiến hóa bài kiểm tra dữ liệu dựa trên trên mô hình hiệu suất, việc đảm bảo rằng các điểm chuẩn duy trì
thử thách khi các khả năng cải thiện (Dynamic benchmarking approaches like Dynabench44 (Kiela et al. 2021) address saturation by continuously evolving test data based on model performance, ensuring that benchmarks remain challenging as capabilities improve). Tuy nhiên, động các điểm chuẩn bổ sung thay vì thay thế
độ bao phủ, chất lượng, và sự phân phối các số liệu được mô tả trước đó: chúng ngăn chặn sự bão hòa nhưng không
chẩn đoán của nó các nguyên nhân (However, dynamic benchmarks complement rather than replace the coverage, quality, and distribution metrics described earlier: they prevent saturation but do not diagnose its causes).

702
12.11 Mô hình và Dữ liệu Sự đánh giá (Model and Data Evaluation)
2000
2005
2010
2015
2020
−100
−80
−60
−40
−20
0
+20
Viết tay sự nhận dạng (Handwriting recognition)
Giọng nói sự nhận dạng (Speech recognition)
Hình ảnh sự nhận dạng (Image recognition)
Đọc
sự hiểu (Reading comprehension)
Ngôn ngữ
sự hiểu biết (Language understanding)
Khả năng của mỗi AI hệ thống là được chuẩn hóa (normalized)
tới một ban đầu hiệu suất −100 (The capability of each AI system is normalized to an initial performance −100)
Con người hiệu suất, như điểm chuẩn, được đặt tới không (Human performance, as the benchmark, is set to zero)
AI các hệ thống hoạt động kém hơn (AI systems perform worse)
AI các hệ thống hoạt động tốt hơn
những con người (những) người đã làm những bài kiểm tra này (AI systems perform better than the humans who did these tests)
Bài kiểm tra điểm số của AI tương đối
tới con người hiệu suất (Test score of the AI relative to human performance)
Ngôn ngữ và hình ảnh sự nhận dạng các khả năng của AI các hệ thống đã cải thiện một cách nhanh chóng (Language and image recognition capabilities of AI systems have improved rapidly)
Hình 12.13: Tập dữ liệu Sự bão hòa (Dataset Saturation): AI các hệ thống đã vượt qua được báo cáo con người các cơ sở trên một vài một cách rộng rãi được theo dõi điểm chuẩn
các khả năng, bao gồm viết tay sự nhận dạng, giọng nói sự nhận dạng, hình ảnh sự nhận dạng, đọc sự hiểu, và ngôn ngữ
sự hiểu biết (AI systems have crossed reported human baselines on several widely tracked benchmark capabilities, including handwriting recognition, speech recognition, image recognition, reading comprehension, and language understanding). Này sự bão hòa nhấn mạnh (underscores) nhu cầu cho động các điểm chuẩn thứ mà duy trì thử thách khi mô hình các khả năng
cải thiện (This saturation underscores the need for dynamic benchmarks that remain challenging as model capabilities improve). Các nguồn: (Maslej et al. 2024; Kiela et al. 2021).
12.11.3 Tổng thể (Holistic) hệ thống-mô hình-dữ liệu sự đánh giá (Holistic system-model-data evaluation)
Việc vượt qua hệ thống, mô hình, và dữ liệu các điểm chuẩn một cách độc lập là không đủ (Passing system, model, and data benchmarks independently is not enough). Một hệ thống điểm chuẩn
có thể xác nhận phần cứng hiệu suất, một mô hình điểm chuẩn có thể xác minh rằng sự nén đã bảo tồn
chất lượng, và một dữ liệu điểm chuẩn có thể đánh giá huấn luyện tập tính đại diện (representativeness), tuy nhiên được triển khai hệ thống
có thể vẫn thất bại bởi vì ba các chiều tương tác (A system benchmark can validate hardware performance, a model benchmark can verify that compression preserved quality, and a data benchmark can assess training set representativeness, yet the deployed system can still fail because the three dimensions interact). Thế giới-thực AI hiệu suất nổi lên từ đó
sự tương tác, và việc tối ưu hóa một chiều có thể phơi bày các điểm yếu trong (chiều) khác (Real-world AI performance emerges from that interaction, and optimizing one dimension can expose weaknesses in another).
Hãy xem xét một cụ thể thất bại thác nước (cascade): một đội đạt được xuất sắc MLPerf Suy luận các điểm số bằng cách việc triển-
khai một INT8-được lượng tử hóa mô hình trên được tối ưu hóa phần cứng (Consider a concrete failure cascade: a team achieves excellent MLPerf Inference scores by deploying an INT8-quantized model on optimized hardware). Hệ thống các điểm chuẩn vượt qua (System benchmarks pass). Được lượng tử hóa
mô hình, tuy nhiên, đã được xác nhận chỉ trên ImageNet-được phân phối bài kiểm tra dữ liệu; sự triển khai tiết lộ độ chính xác
sự suy thoái trên nhà máy-sàn (factory-floor) các hình ảnh với khác nhau ánh sáng các đặc điểm (The quantized model, however, was validated only on ImageNet-distributed test data; deployment reveals accuracy degradation on factory-floor images with different lighting characteristics). Mô hình chất lượng các điểm-
chuẩn lẽ ra đã bắt được sự lượng tử hóa độ nhạy (Model quality benchmarks would have caught the quantization sensitivity). Xa hơn sự điều tra cho thấy huấn luyện
dữ liệu (đã) chứa không các hình ảnh với công nghiệp ánh sáng—một dữ liệu chất lượng khoảng cách thứ mà không số lượng của hệ thống hay
mô hình sự tối ưu hóa có thể giải quyết (Further investigation shows the training data contained no images with industrial lighting—a data quality gap that no amount of system or model optimization can address).
Này sự phụ thuộc lẫn nhau (interdependence) có nghĩa (rằng) điểm chuẩn các kết quả từ một chiều có thể bị làm cho mất hiệu lực (invalidated) bởi
các thất bại trong (chiều) khác (This interdependence means that benchmark results from one dimension can be invalidated by failures in another):
• Hệ thống sự thành công + Mô hình sự thất bại (System success + Model failure): Phần cứng cung cấp được hứa hẹn thông lượng, nhưng sự nén
đã làm suy thoái độ chính xác bên dưới sự triển khai các ngưỡng (Hardware delivers promised throughput, but compression degraded accuracy below deployment thresholds)
• Hệ thống sự thành công + Dữ liệu sự thất bại (System success + Data failure): Nhanh sự suy luận trên mang tính đại diện các đầu vào, nhưng huấn luyện dữ liệu sự thiên vị
gây ra các thất bại trên nhân khẩu học các nhóm phụ (Fast inference on representative inputs, but training data bias causes failures on demographic subgroups)
• Mô hình sự thành công + Hệ thống sự thất bại (Model success + System failure): Chính xác các dự đoán, nhưng độ trễ phương sai dưới tải vi phạm
SLA các yêu cầu (Accurate predictions, but latency variance under load violates SLA requirements)
• Mô hình sự thành công + Dữ liệu sự thất bại (Model success + Data failure): Cao độ chính xác trên được giữ-lại bài kiểm tra tập, nhưng sự phân phối sự dịch chuyển trong
sản xuất gây ra im lặng sự suy thoái (High accuracy on held-out test set, but distribution shift in production causes silent degradation)
Này sự phụ thuộc lẫn nhau là chính xác AI Bộ ba (Triad) được giới thiệu trong Chương 1 (hình 1.3): Hệ thống tương-
ứng (với) Máy móc (Machine), Mô hình tương ứng (với) Thuật toán (Algorithm), và Dữ liệu duy trì (là) Dữ liệu (This interdependence is precisely the AI Triad introduced in Chapter 1 (figure 1.3): System corresponds to Machine, Model corresponds to Algorithm, and Data remains Data). Tổng thể sự đánh giá
yêu cầu không chỉ việc vượt qua các điểm chuẩn trong mỗi chiều, mà (còn) việc xác minh rằng các giả định được tạo ra trong một
chiều giữ (nguyên) qua (những chiều) khác (Holistic evaluation requires not just passing benchmarks in each dimension, but verifying that assumptions made in one dimension hold across the others). Phần III sự tối ưu hóa đường ống (dữ liệu → mô hình → phần cứng)
tạo ra ngầm định các sự phụ thuộc thứ mà việc đo điểm chuẩn phải xác nhận một cách rõ ràng (The Part III optimization pipeline (data → model → hardware) creates implicit dependencies that benchmarking must validate explicitly).
D·A·M phân loại học cung cấp một chẩn đoán bộ khung cho một cách có hệ thống việc xác định chiều nào
giới hạn hiệu suất (The D·A·M taxonomy provides a diagnostic framework for systematically identifying which axis limits performance). Phần A.1 ánh xạ mỗi chiều tới của nó việc ràng buộc vật lý sự ép buộc (constraint) và
sự tối ưu hóa con đường thứ mà làm giảm (relieves) nó, việc cho đầu tiên chẩn đoán bước khi một điểm chuẩn tiết lộ

12. Việc đo điểm chuẩn (Benchmarking)
703
sự sử dụng dưới mức (underutilization). Bảng 12.21 chính thức hóa này cách tiếp cận bằng cách việc lai (crossing) mỗi D·A·M chiều với ba
cơ bản nút thắt cổ chai các loại; Phụ lục (Appendix) A cho đầy đủ chẩn đoán hướng dẫn, bao gồm việc lập hồ sơ (profiling)
các tiện ích (utilities) và tính hiệu quả việc chấm điểm (grading) các thang điểm (rubrics) (Table 12.21 formalizes this approach by crossing each D·A·M axis with the three fundamental bottleneck types; Appendix A gives the full diagnostic guide, including profiling utilities and efficiency grading rubrics).
Bảng 12.21: D·A·M Nút thắt cổ chai Chẩn đoán Ma trận (D·A·M Bottleneck Diagnostic Matrix): Mỗi ô (cell) mô tả một hiệu suất sự ép buộc (constraint) triệu chứng, và hàng
xác định nào D·A·M chiều để giải quyết (Each cell describes a performance constraint symptom, and the row identifies which D·A·M axis to address). Khi hiệu suất đình trệ (stalls), này ma trận biến đầu tiên chẩn đoán bước vào một cụ thể-chiều
kiểm tra của Dữ liệu, Thuật toán, hay Máy móc (When performance stalls, this matrix turns the first diagnostic move into an axis-specific check of Data, Algorithm, or Machine).
Thành phần (Component)
Bị giới hạn-Bởi tính toán (Compute-Bound)
Bị giới hạn-Bởi bộ nhớ (Memory-Bound)
Bị giới hạn-Bởi I/O (I/O-Bound)
Dữ liệu (Data)
Tiền xử lý quá chậm
(sự gia tăng, sự mã thông báo hóa (tokenization)) (Preprocessing too slow (augmentation, tokenization))
Tập dữ liệu vượt quá RAM (tràn (spills) ra
đĩa) (Dataset exceeds RAM (spills to disk))
Lưu trữ không thể nuôi GPU (đĩa
thông lượng giới hạn) (Storage cannot feed GPU (disk throughput limit))
Thuật toán (Algorithm)
Mô hình quá lớn cho phần cứng
(FLOPs vượt quá công suất) (Model too large for hardware (FLOPs exceed capacity))
Các kích hoạt (Activations) vượt quá bộ nhớ (lô
kích thước bị giới hạn) (Activations exceed memory (batch size limited))
Đạo hàm đồng bộ chậm hơn
tính toán (phân tán huấn luyện) (Gradient sync slower than compute (distributed training))
Máy móc (Machine)
GPU sự sử dụng bị bão hòa (cần
nhanh hơn máy gia tốc) (GPU utilization saturated (need faster accelerator))
Bộ nhớ băng thông bị bão hòa
(cần nhiều hơn HBM băng thông) (Memory bandwidth saturated (need more HBM bandwidth))
Mạng/PCIe băng thông
bị bão hòa (cần nhanh hơn các liên kết) (Network/PCIe bandwidth saturated (need faster links))
Chẩn đoán sức mạnh của này ma trận trở nên rõ ràng khi các điểm chuẩn tiết lộ không mong đợi các kết quả—
đặc biệt khi hiệu suất rơi (xuống) ngắn của các sự kỳ vọng (The diagnostic power of this matrix becomes clear when benchmarks reveal unexpected results—particularly when performance falls short of expectations). Nếu hệ thống các điểm chuẩn cho thấy thấp GPU
sự sử dụng mặc dù đầy đủ phần cứng, nút thắt cổ chai nhiều khả năng nằm (ở) nơi khác (If system benchmarks show low GPU utilization despite adequate hardware, the bottleneck likely lies elsewhere). Cho ví dụ, một đội
việc quan sát chỉ 30 phần trăm GPU sự sử dụng trong suốt huấn luyện có thể ban đầu nghi ngờ một không hiệu quả
mô hình kiến trúc (Thuật toán hàng), nhưng việc lập hồ sơ tiết lộ rằng hình ảnh sự gia tăng chạy trên CPU
và không thể theo kịp với GPU sự tiêu thụ (Dữ liệu hàng, Bị giới hạn-Bởi tính toán cột: “Tiền xử lý
quá chậm”) (For example, a team observing only 30 percent GPU utilization during training might initially suspect an inefficient model architecture (Algorithm row), but profiling reveals that image augmentation runs on CPU and cannot keep up with GPU consumption (Data row, Compute-Bound column: “Preprocessing too slow”)). Có hệ thống chẩn đoán việc sử dụng này ma trận ngăn chặn phổ biến sai lầm của việc tối ưu hóa
sai thành phần (Systematic diagnosis using this matrix prevents the common mistake of optimizing the wrong component).
Tuy nhiên (Yet) sự xác nhận dưới được kiểm soát phòng thí nghiệm các điều kiện khác biệt một cách sâu sắc từ sự xác nhận dưới
sản xuất thực tế (Yet validation under controlled laboratory conditions differs profoundly from validation under production reality). Trong phòng thí nghiệm, dữ liệu các sự phân phối giữ (nguyên) cố định, yêu cầu các mẫu duy trì đồng nhất (uniform),
và các hệ thống chạy trong sự cô lập (In the laboratory, data distributions stay fixed, request patterns remain uniform, and systems run in isolation). Trong sản xuất, tất cả ba các giả định phá vỡ một cách đồng thời—dữ liệu
trôi dạt, lưu lượng truy cập (traffic) các gai (spikes) một cách không thể đoán trước, và hệ thống các thành phần tương tác theo các cách thứ mà bị cô lập các điểm chuẩn
không thể nắm bắt (In production, all three assumptions break simultaneously—data drifts, traffic spikes unpredictably, and system components interact in ways that isolated benchmarks cannot capture). Cuối cùng chiều của việc đo điểm chuẩn hỏi liệu các hệ thống được xác nhận trong phòng thí nghiệm
(có) sống sót (sự) tiếp xúc với thế giới thực (hay không) (The final dimension of benchmarking asks whether systems validated in the lab survive contact with the real world).
12.12 Sản xuất Các sự cân nhắc (Production Considerations)
Một hệ thống thứ mà vượt qua tất cả ba điểm chuẩn các thể loại có thể vẫn thất bại trong sản xuất.
Ba-
chiều bộ khung đã xác nhận phần cứng hiệu suất, mô hình chất lượng, và dữ liệu tính đại diện
dưới được kiểm soát các điều kiện—nhưng sản xuất vi phạm những các điều kiện đó một cách liên tục (The three-dimensional framework validated hardware performance, model quality, and data representativeness under controlled conditions—but production violates those conditions continuously). Này
khoảng cách giữa điểm chuẩn sự thành công và sự triển khai sự thành công thúc đẩy một cuối cùng việc đo điểm chuẩn mối quan tâm:
việc xác nhận các hệ thống dưới các điều kiện thứ mà khớp hoạt động thực tế (This gap between benchmark success and deployment success motivates a final benchmarking concern: validating systems under conditions that match operational reality).
12.12.1 Từ phòng thí nghiệm tới sản xuất (From laboratory to production)
Phòng thí nghiệm các điểm chuẩn thiết lập cái gì một hệ thống là có khả năng của dưới lý tưởng các điều kiện (Laboratory benchmarks establish what a system is capable of under ideal conditions). Sản xuất
sự xác nhận xác định liệu đó hệ thống (có) đang hoạt động một cách chính xác ngay bây giờ, dưới thực tế các điều kiện (hay không) (Production validation determines whether that system is performing correctly right now, under real conditions).
Này sự phân biệt quan trọng bởi vì phòng thí nghiệm các điểm chuẩn giả định các điều kiện thứ mà sản xuất một cách có hệ-
thống vi phạm (This distinction matters because laboratory benchmarks assume conditions that production systematically violates). Im lặng sự suy thoái đưa ra nhất xảo quyệt thách thức: các mô hình có thể tạo ra
có vẻ hợp lý (plausible) nhưng không chính xác các đầu ra mà không có rõ ràng lỗi các tín hiệu, và một sự giới thiệu hệ thống việc trả-
về “hợp lý” nhưng dưới mức tối ưu các gợi ý có không tích hợp-sẵn (built-in) lỗi chỉ báo (Silent degradation poses the most insidious challenge: models can produce plausible but incorrect outputs without obvious error signals, and a recommendation system returning “reasonable” but suboptimal suggestions has no built-in error indicator). Động các khối lượng công việc
đưa ra một khác thất bại chế độ: một hệ thống được đo điểm chuẩn tại ổn định 1,000 QPS có thể thất bại khi chớp nhoáng (flash)
lưu lượng truy cập các sự kiện gai (spike) tới 10,000 QPS, việc tiết lộ rằng điểm chuẩn “thông lượng” đã giả định đồng nhất yêu cầu
sự đến (arrival) thay vì bùng nổ (bursty) sản xuất các mẫu (Dynamic workloads present a different failure mode: a system benchmarked at steady 1,000 QPS may fail when flash traffic events spike to 10,000 QPS, revealing that benchmark “throughput” assumed uniform request arrival rather than bursty production patterns). Dữ liệu sự phân phối sự dịch chuyển làm phức tạp (compounds) những các vấn đề này
theo (over) thời gian, khi sản xuất dữ liệu tiến hóa và phân kỳ từ huấn luyện các sự phân phối—một hình ảnh bộ phân loại
được huấn luyện trên chuyên nghiệp các bức ảnh suy thoái một cách dần dần khi người dùng nộp điện thoại thông minh các hình ảnh với khác nhau
ánh sáng, các góc độ, và sự nén các hiện vật (artifacts) (Data distribution shift compounds these problems over time, as production data evolves and diverges from training distributions—an image classifier trained on professional photos degrades gradually as users submit smartphone images with different lighting, angles, and compression artifacts). Cuối cùng, sản xuất áp đặt nhiều-mục tiêu các sự ràng buộc
thứ mà các điểm chuẩn xử lý một cách độc lập: độ chính xác, độ trễ, chi phí, và tài nguyên sự sử dụng phải tất cả được
thỏa mãn một cách đồng thời, và việc tối ưu hóa bất kỳ một (cái nào) tại chi phí của những (cái) khác dẫn tới sự triển khai
thất bại (Finally, production imposes multi-objective constraints that benchmarks treat independently: accuracy, latency, cost, and resource utilization must all be satisfied simultaneously, and optimizing any one at the expense of others leads to deployment failure).

704
12.13 Các ngụy biện và Các cạm bẫy (Fallacies and Pitfalls)
12.12.2 Việc bắc cầu điểm chuẩn tới sự triển khai (Bridging benchmark to deployment)
Trước khi sự triển khai, xác nhận việc đo điểm chuẩn các kết luận chống lại mang tính đại diện-sản xuất các điều-
kiện (Before deployment, validate benchmarking conclusions against production-representative conditions). Bảng 12.22 gọi tên điểm chuẩn giả định, sản xuất thực tế thứ mà vi phạm nó, và
sự xác nhận bước thứ mà đóng khoảng cách; điểm kiểm tra thứ mà theo (sau) biến những các hàng đó vào sự sẵn sàng-phát hành (release-readiness)
các hành động (Table 12.22 names the benchmark assumption, the production reality that violates it, and the validation step that closes the gap; the checkpoint that follows turns those rows into release-readiness actions).
Bảng 12.22: Tiền-sự triển khai (Predeployment) Điểm chuẩn Danh sách kiểm tra (Checklist): Mỗi hàng ghép nối (pairs) một giả định được nướng (baked) vào phòng thí nghiệm các điểm chuẩn với
sản xuất thực tế thứ mà vi phạm nó và sự xác nhận bước thứ mà đóng khoảng cách (Each row pairs an assumption baked into laboratory benchmarks with the production reality that violates it and the validation step that closes the gap). Một hệ thống thứ mà vượt qua mọi phòng thí nghiệm điểm chuẩn
có thể vẫn thất bại trong sản xuất trừ khi mỗi hàng của này bảng (có) đã được một cách độc lập xác minh chống lại mang tính đại diện hoạt động
các điều kiện (A system that passes every laboratory benchmark can still fail in production unless each row of this table has been independently verified against representative operational conditions).
Điểm chuẩn Giả định (Benchmark Assumption)
Sản xuất Thực tế (Production Reality)
Sự xác nhận Cách tiếp cận (Validation Approach)
Đồng nhất yêu cầu sự đến (Uniform request arrival)
Bùng nổ (Bursty) lưu lượng truy cập các mẫu (Bursty traffic patterns)
Tải bài kiểm tra với sản xuất dấu vết sự phát lại (Load test with production trace replay)
Sạch, được tiền xử lý các đầu vào (Clean, preprocessed inputs)
Có thể thay đổi chất lượng các đầu vào (Variable quality inputs)
Đánh giá trên sản xuất dữ liệu mẫu (Evaluate on production data sample)
Ấm hệ thống trạng thái (Warm system state)
Lạnh các sự khởi động, bộ nhớ đệm các sự bỏ lỡ (Cold starts, cache misses)
Đo lường lạnh-khởi động hiệu suất (Measure cold-start performance)
Bị cô lập sự thực thi (Isolated execution)
Tài nguyên sự tranh chấp (Resource contention)
Đo điểm chuẩn dưới thực tế hệ thống tải (Benchmark under realistic system load)
Cố định mô hình phiên bản (Fixed model version)
A/B việc kiểm tra, dần dần sự triển khai (A/B testing, gradual rollout)
Thiết lập cơ sở cho sự so sánh (Establish baseline for comparison)
Điểm kiểm tra (Checkpoint) 12.4: Tiền-sự triển khai điểm chuẩn danh sách kiểm tra (Predeployment benchmark checklist)
Trước khi việc triển khai một mô hình dựa trên trên điểm chuẩn các kết quả (Before deploying a model based on benchmark results):
□ Phát lại sản xuất các dấu vết: Sử dụng được ghi lại yêu cầu các mẫu để xác nhận thông lượng/độ trễ
dưới thực tế các điều kiện (Replay production traces: Use logged request patterns to validate throughput/latency under realistic conditions).
□ Kiểm tra với sản xuất dữ liệu: Mẫu gần đây sản xuất các đầu vào (việc tôn trọng quyền riêng tư) để
xác minh độ chính xác giữ (nguyên) (Test with production data: Sample recent production inputs (respecting privacy) to verify accuracy holds).
□ Căng thẳng (Stress) kiểm tra biên các trường hợp: Xác định tồi tệ nhất-trường hợp các đầu vào và xác minh tinh tế (graceful) sự suy thoái (Stress test edge cases: Identify worst-case inputs and verify graceful degradation).
□ Thiết lập việc giám sát các cơ sở: Lập tài liệu được kỳ vọng số liệu các phạm vi cho sự bất thường (anomaly) sự phát-
hiện (Establish monitoring baselines: Document expected metric ranges for anomaly detection).
□ Xác định rollback các tiêu chí: Chỉ định định lượng các ngưỡng cho việc quay lại (reverting) (tới) trước đó
mô hình phiên bản (Define rollback criteria: Specify quantitative thresholds for reverting to the previous model version).
12.12.3 Sản xuất việc giám sát như liên tục việc đo điểm chuẩn (Production monitoring as continuous benchmarking)
Sản xuất việc giám sát mở rộng việc đo điểm chuẩn từ một một-lần cổng tới một liên tục quá trình (Production monitoring extends benchmarking from a one-time gate to a continuous process).
Giống nhau các nguyên tắc áp dụng (được chuẩn hóa các số liệu, có thể tái tạo sự đo lường, thuộc về thống kê sự nghiêm ngặt (rigor)) nhưng
ngữ cảnh dịch chuyển từ “liệu này (có) hoạt động?” tới “liệu này (có) đang hoạt động?” (The same principles apply (standardized metrics, reproducible measurement, statistical rigor) but the context shifts from “will this work?” to “is this working?”)
Một khi một mô hình là trực tiếp (live), việc đo điểm chuẩn trở thành một lăn (rolling) sự so sánh chống lại các cơ sở vừa mới
được thiết lập (Once a model is live, benchmarking becomes a rolling comparison against the baselines just established). Ngay lập tức các sự kiểm tra duy trì cụ thể: liệu đầu vào sự phân phối duy trì gần tới
điểm chuẩn sự phân phối, liệu độ trễ và thông lượng ở lại bên trong được đo lường vỏ bọc (envelope), và
liệu mô hình chất lượng di chuyển ra ngoài được kỳ vọng phạm vi (The immediate checks stay concrete: whether the input distribution remains close to the benchmark distribution, whether latency and throughput stay inside the measured envelope, and whether model quality moves outside the expected range). Việc trả lời những các sự kiểm tra đó yêu cầu giống nhau
sự đo lường kỷ luật như ngoại tuyến (offline) điểm chuẩn, nhưng bây giờ các sự đo lường đến một cách liên tục
và dưới trực tiếp lưu lượng truy cập (Answering those checks requires the same measurement discipline as the offline benchmark, but now the measurements arrive continuously and under live traffic).
MLOps chương muộn hơn biến này sự đo lường vòng lặp vào sự phát hành và sự phục hồi (recovery) máy móc (machinery): được chia giai đoạn
các sự triển khai (staged rollouts), bóng (shadow) sự đánh giá [việc chạy mới mô hình bên cạnh sản xuất mà không có việc phục vụ của nó các đầu ra],
liên tục sự xác nhận, và rollback (The MLOps chapter later turns this measurement loop into release and recovery machinery: staged rollouts, shadow evaluation [running the new model beside production without serving its outputs], continuous validation, and rollback). Tại này điểm, sự bàn giao (handoff) là hẹp hơn (At this point, the handoff is narrower). Việc đo điểm chuẩn xác định
các cơ sở và thất bại các ngưỡng; (các) hoạt động (operations) tiếp tục việc đo lường chống lại chúng sau sự triển khai (Benchmarking defines the baselines and failure thresholds; operations keeps measuring against them after deployment).
Giống nhau khoảng cách giữa điểm chuẩn các điều kiện và sản xuất các điều kiện giải thích tại sao khác (otherwise)
cẩn thận các đội vẫn tạo ra có thể đoán trước các sai lầm (The same gap between benchmark conditions and production conditions explains why otherwise careful teams still make predictable mistakes). Cuối cùng phần gọi tên các quan niệm sai lầm (misconceptions) thứ mà biến
điểm chuẩn sự thành công vào sự triển khai sự thất bại (The final section names the misconceptions that turn benchmark success into deployment failure).
12.13 Các ngụy biện và Các cạm bẫy (Fallacies and Pitfalls)
Việc đo điểm chuẩn tạo ra sai độ tự tin khi được chuẩn hóa sự đo lường che khuất (obscures) sự triển khai
các thực tế (Benchmarking creates false confidence when standardized measurement obscures deployment realities). Các đội giả định được kiểm soát các sự đánh giá dự đoán sản xuất hiệu suất, nhưng thực các hệ thống (Teams assume controlled evaluations predict production performance, but real systems)

12. Việc đo điểm chuẩn (Benchmarking)
705
Trung bình (Mean) điểm chuẩn độ trễ nói giảm (understates)
sản xuất đuôi (tail) bởi một
bậc của độ lớn (order of magnitude).
bề mặt (face) tính biến đổi, tài nguyên các sự ép buộc (constraints), và nhiều-mục tiêu các sự đánh đổi thứ mà các điểm chuẩn không thể nắm bắt,
việc lãng phí kỹ thuật nỗ lực trên các hệ thống được tối ưu hóa cho sự đánh giá thay vì sự triển khai (face variability, resource constraints, and multi-objective trade-offs that benchmarks cannot capture, wasting engineering effort on systems optimized for evaluation rather than deployment).
Ngụy biện (Fallacy): Điểm chuẩn hiệu suất một cách trực tiếp dịch sang thế giới-thực ứng dụng hiệu suất (Benchmark performance directly translates to real-world application performance).
Quyến rũ (seductive) sự rõ ràng của điểm chuẩn các bảng xếp hạng dẫn dắt các đội (đến việc) chọn các hệ thống như thể bảng xếp hạng
vị trí dự đoán sản xuất hành vi (The seductive clarity of benchmark rankings leads teams to select systems as though leaderboard position predicts production behavior). Nó hiếm khi (làm) vậy (It rarely does). Như phần 12.3.1 chứng minh, ML các hệ thống
thể hiện vốn có (inherent) tính biến đổi từ dữ liệu chất lượng các vấn đề, sự phân phối các sự dịch chuyển, và tài nguyên các sự ép buộc
vắng mặt (absent) trong được kiểm soát sự đánh giá (As section 12.3.1 demonstrates, ML systems exhibit inherent variability from data quality issues, distribution shifts, and resource constraints absent in controlled evaluation). Trong một mang tính đại diện thất bại kịch bản, một ngôn ngữ mô hình việc đạt được
92 phần trăm điểm chuẩn độ chính xác sụt giảm tới 78–82 phần trăm độ chính xác trong sản xuất khi việc xử lý
được tạo-bởi-người dùng văn bản với chính tả các lỗi, không trang trọng ngôn ngữ, và cụ thể-miền thuật ngữ (In a representative failure scenario, a language model achieving 92 percent benchmark accuracy drops to 78–82 percent accuracy in production when processing user-generated text with spelling errors, informal language, and domain-specific terminology).
Một sự suy luận hệ thống với 15 ms trung bình độ trễ trên MLPerf trải nghiệm 150–200 ms p99 độ trễ trong
sản xuất (10–13.3× sự suy thoái) do đồng thời tải, rác sự thu thập (garbage collection) các sự tạm dừng, và mạng
tính biến đổi (An inference system with 15 ms mean latency on MLPerf experiences 150–200 ms p99 latency in production (10–13.3× degradation) due to concurrent load, garbage collection pauses, and network variability). Các đội việc dựa duy nhất trên điểm chuẩn các bảng xếp hạng một cách có hệ thống ước tính thấp (underestimate) sự triển khai
tính phức tạp, việc dẫn tới bị thất bại các sự ra mắt (launches) và tốn kém việc thiết kế lại (re-engineering) (Teams relying solely on benchmark rankings systematically underestimate deployment complexity, leading to failed launches and costly re-engineering).
Cạm bẫy (Pitfall): Việc tối ưu hóa một cách độc quyền cho điểm chuẩn các số liệu mà không có việc xem xét rộng hơn hệ thống các yêu cầu (Optimizing exclusively for benchmark metrics without considering broader system requirements).
Điểm chuẩn các bảng xếp hạng khuyến khích (incentivize) tích cực sự tối ưu hóa, nhưng các sự tối ưu hóa thứ mà leo lên (climb)
các bảng xếp hạng thường làm suy thoái chính (the very) các đặc điểm sản xuất đòi hỏi (Benchmark leaderboards incentivize aggressive optimization, but the optimizations that climb rankings often degrade the very characteristics production demands). Như được thảo luận trong phần 12.10.4,
này làm ví dụ (exemplifies) Goodhart’s Định luật: khi điểm chuẩn các điểm số trở thành sự tối ưu hóa các mục tiêu, chúng dừng (cease)
(việc) là có ý nghĩa các sự đo lường của hệ thống chất lượng (As discussed in section 12.10.4, this exemplifies Goodhart’s Law: when benchmark scores become optimization targets, they cease to be meaningful measures of system quality). Trong một có tính minh họa kịch bản, một đội giảm sự suy luận
độ trễ từ 12 ms tới 8 ms thông qua tích cực sự lượng tử hóa, việc cải thiện MLPerf thứ hạng bởi 15
các vị trí trong khi việc làm suy thoái sự hiệu chuẩn sao cho dự đoán độ tự tin các điểm số trở nên không đáng tin cậy cho
hạ lưu việc ra-quyết định (In one illustrative scenario, a team reduces inference latency from 12 ms to 8 ms through aggressive quantization, improving MLPerf ranking by 15 positions while degrading calibration such that prediction confidence scores become unreliable for downstream decision-making). Khác đội cải thiện ImageNet độ chính xác bởi 2.1 phần trăm thông qua
rộng rãi siêu tham số (hyperparameter) việc tinh chỉnh nhưng được tối ưu hóa mô hình tiêu thụ 40 phần trăm nhiều hơn năng lượng và
thể hiện 25 phần trăm tồi tệ hơn hiệu suất trên ngoài-sự phân phối (out-of-distribution) các hình ảnh từ sản xuất các camera (Another team improves ImageNet accuracy by 2.1 percent through extensive hyperparameter tuning but the optimized model consumes 40 percent more energy and exhibits 25 percent worse performance on out-of-distribution images from production cameras).
Các tổ chức việc khen thưởng điểm chuẩn các thứ hạng trên (over) sự triển khai sự thành công một cách có hệ thống tạo ra
các hệ thống thứ mà xuất sắc trong sự đánh giá nhưng thất bại trong sản xuất (Organizations rewarding benchmark rankings over deployment success systematically produce systems that excel in evaluation but fail in production).
Ngụy biện: Đơn-số liệu sự đánh giá cung cấp đủ sự thấu hiểu vào hệ thống hiệu suất (Single-metric evaluation provides sufficient insight into system performance).
Một đơn con số là một cách quyến rũ (seductively) đơn giản: này hệ thống là “94 phần trăm chính xác” hay “1,200 QPS nhanh.” (A single number is seductively simple: this system is “94 percent accurate” or “1,200 QPS fast.”)
Nhưng sản xuất sự thành công yêu cầu việc cân bằng nhiều cạnh tranh (competing) các mục tiêu thứ mà bất kỳ đơn số liệu (nào)
che khuất (But production success requires balancing multiple competing objectives that any single metric obscures). Như được thiết lập trong phần 12.8.2, hiện đại sự suy luận các hệ thống đòi hỏi sự đánh giá qua
độ chính xác, độ trễ, thông lượng, năng lượng, và tính mạnh mẽ các chiều (As established in section 12.8.2, modern inference systems demand evaluation across accuracy, latency, throughput, energy, and robustness dimensions). Trong một có tính minh họa sự đánh đổi, một
sự giới thiệu mô hình việc đạt được 94 phần trăm độ chính xác với 180 ms p99 độ trễ thất bại cấp độ-dịch vụ (service-level)
các mục tiêu (objectives) việc yêu cầu p99 < 100 ms mặc dù xuất sắc độ chính xác (In an illustrative trade-off, a recommendation model achieving 94 percent accuracy with 180 ms p99 latency fails service-level objectives requiring p99 < 100 ms despite excellent accuracy). Ngược lại, một hệ thống được tối ưu hóa cho
1,200 QPS thông lượng đạt được này tỷ lệ trong khi việc tiêu thụ 4.2 W so với 1.8 W cho một hơi chậm hơn hệ thống
tại 1,000 QPS (2.3× sức mạnh (power) sự khác biệt) (Conversely, a system optimized for 1,200 QPS throughput achieves this rate while consuming 4.2 W vs. 1.8 W for a slightly slower system at 1,000 QPS (2.3× power difference)). Cho được cấp nguồn bằng pin biên (edge) các thiết bị, 17 phần trăm thông lượng
sự mất mát kích hoạt 2.3× dài hơn hoạt động thời gian (For battery-powered edge devices, the 17 percent throughput loss enables 2.3× longer operation time). Khác nhau các bên liên quan (stakeholders) ưu tiên khác nhau các số liệu: ML
các kỹ sư tập trung trên độ chính xác, cơ sở hạ tầng các đội trên thông lượng và chi phí, sản phẩm những người quản lý trên
độ trễ các phân vị (percentiles) (Different stakeholders prioritize different metrics: ML engineers focus on accuracy, infrastructure teams on throughput and cost, product managers on latency percentiles). Đơn-số liệu sự tối ưu hóa một cách có hệ thống tạo ra các hệ thống thứ mà xuất sắc trên một
chiều trong khi việc thất bại sự triển khai các yêu cầu trên những (chiều) khác (Single-metric optimization systematically produces systems that excel on one dimension while failing deployment requirements on others).
Cạm bẫy: Việc sử dụng lỗi thời các điểm chuẩn thứ mà không còn phản ánh sự triển khai các thách thức và các yêu cầu (Using outdated benchmarks that no longer reflect deployment challenges and requirements).
Các điểm chuẩn có quán tính (inertia): các đội tiếp tục việc báo cáo trên được thiết lập các điểm chuẩn lâu sau khi những
các điểm chuẩn (đó) dừng việc cung cấp có ý nghĩa sự phân biệt (discrimination) (Benchmarks have inertia: teams continue reporting on established benchmarks long after those benchmarks cease to provide meaningful discrimination). Sự bão hòa xảy ra khi nhiều các cách tiếp-
cận đạt được gần như-giống hệt hiệu suất, việc loại bỏ hữu ích sự so sánh (Saturation occurs when multiple approaches achieve near-identical performance, eliminating useful comparison). ImageNet top-5
phân loại lỗi đã giảm từ 28.2 phần trăm trong 2010 tới 3.57 phần trăm bởi 2015, với cuộc thi
việc kết thúc trong 2017, tại đó điểm 29 các đội của 38 các đội đã vượt quá 95 phần trăm độ chính xác (Russakovsky
et al. 2015; Beyer et al. 2020); xa hơn sự tối ưu hóa vượt ra ngoài này ngưỡng cung cấp cận biên (marginal) giá trị
cho hầu hết các ứng dụng (ImageNet top-5 classification error decreased from 28.2 percent in 2010 to 3.57 percent by 2015, with the competition ending in 2017, at which point 29 teams of 38 teams exceeded 95 percent accuracy (Russakovsky et al. 2015; Beyer et al. 2020); further optimization beyond this threshold provides marginal value for most applications). Một cách tương tự, MNIST đã trở nên bão hòa đủ rằng các sự cải thiện tại thứ ba
số thập phân vị trí là hiếm khi liên quan-tới-sự triển khai (LeCun et al. 1998) (Similarly, MNIST became saturated enough that improvements at the third decimal place are rarely deployment-relevant (LeCun et al. 1998)). Như được thảo luận trong phần 12.10.1,
thuộc về thống kê độ tự tin các khoảng xung quanh những các sự đo lường này thường vượt quá được tuyên bố các sự cải thiện (As discussed in section 12.10.1, statistical confidence intervals around these measurements often exceed the claimed improvements).
Việc thay đổi sự triển khai các ngữ cảnh làm phức tạp vấn đề: các điểm chuẩn được thiết kế cho máy chủ phần cứng
trở nên gây hiểu lầm cho biên các thiết bị với 10× ít hơn bộ nhớ và 100× thấp hơn sức mạnh các ngân sách (Changing deployment contexts compound the problem: benchmarks designed for server hardware become misleading for edge devices with 10× less memory and 100× lower power budgets). Hiệu-
quả việc đo điểm chuẩn yêu cầu việc nghỉ hưu (retiring) bị bão hòa các điểm chuẩn và việc phát triển sự đánh giá các bộ khung
việc khớp mục tiêu sự triển khai các thực tế (Effective benchmarking requires retiring saturated benchmarks and developing evaluation frameworks matching target deployment realities).
Ngụy biện: Nghiên cứu các điểm chuẩn dự đoán sản xuất hành vi dưới thực lưu lượng truy cập (Research benchmarks predict production behavior under real traffic).
Nghiên cứu các điểm chuẩn tồn tại để so sánh các thuật toán dưới được kiểm soát các điều kiện; sản xuất các hệ-
thống tồn tại để phục vụ người dùng dưới hỗn loạn những (điều kiện) (Research benchmarks exist to compare algorithms under controlled conditions; production systems exist to serve users under chaotic ones). Việc áp dụng (cái) trước đó để đánh giá (cái) sau đó một cách có hệ thống (Applying the former to evaluate the latter systematically)

706
12.14 Tóm tắt (Summary)
ước tính quá cao hiệu suất, bởi vì nghiên cứu các điểm chuẩn thường giả định dồi dào (ample) thuộc về tính toán các tài-
nguyên, tối ưu dữ liệu chất lượng, và được lý tưởng hóa các điều kiện vắng mặt trong sản xuất (overestimates performance, because research benchmarks often assume ample computational resources, optimal data quality, and idealized conditions absent in production). Như được thiết lập trong
phần 12.10.2, sản xuất các hệ thống đối mặt đồng thời người dùng các tải, biến đổi đầu vào chất lượng, mạng
độ trễ, và hệ thống các thất bại thứ mà làm suy thoái hiệu suất (As established in section 12.10.2, production systems face concurrent user loads, varying input quality, network latency, and system failures that degrade performance). Một hệ thống việc đạt được 800 QPS thông lượng trong
bị cô lập các điểm chuẩn duy trì (sustains) chỉ 400–500 QPS dưới sản xuất tải với 90 phần trăm sự sử dụng
(37.5–50 phần trăm sự suy thoái) do hàng đợi sự tranh chấp và rác sự thu thập các sự tạm dừng (A system achieving 800 QPS throughput in isolated benchmarks sustains only 400–500 QPS under production load with 90 percent utilization (37.5–50 percent degradation) due to queue contention and garbage collection pauses). Nghiên cứu
các điểm chuẩn báo cáo mô hình sự suy luận thời gian (5–10 ms) trong khi sản xuất kết thúc-tới-kết thúc độ trễ bao gồm
sự tiền xử lý, việc xếp hàng đợi, và sự hậu xử lý chi phí hoạt động (overhead) việc tổng cộng (totaling) 50–100 ms (Research benchmarks report model inference time (5–10 ms) while production end-to-end latency includes preprocessing, queuing, and postprocessing overhead totaling 50–100 ms). Sản xuất các hệ thống
yêu cầu 99.9 phần trăm tính khả dụng (availability) (43 phút thời gian chết mỗi tháng) và tinh tế sự suy thoái dưới
các thất bại, các đặc điểm nghiên cứu các điểm chuẩn phớt lờ (Production systems require 99.9 percent availability (43 minutes downtime per month) and graceful degradation under failures, characteristics research benchmarks ignore). Hiệu quả sản xuất sự đánh giá yêu cầu hoạt động
các số liệu: được duy trì thông lượng dưới tải, sự phục hồi thời gian từ các thất bại, và hoàn chỉnh độ trễ
sự cố (breakdown) (Effective production evaluation requires operational metrics: sustained throughput under load, recovery time from failures, and complete latency breakdown).
Cạm bẫy: Việc sử dụng nghiên cứu các điểm chuẩn như sản xuất sự phát hành các cổng (Using research benchmarks as production release gates).
Các đội thỉnh thoảng thăng cấp (promote) một mô hình bởi vì nó vượt qua nghiên cứu điểm chuẩn, sau đó khám phá chỉ
sau khi sự ra mắt rằng điểm chuẩn (đã) chưa bao giờ rèn luyện (exercised) hoạt động con đường (Teams sometimes promote a model because it passes the research benchmark, then discover only after launch that the benchmark never exercised the operational path). Một sự phát hành cổng cho một việc phục vụ
hệ thống phải bao gồm tải các bài kiểm tra, đuôi-độ trễ các sự đo lường, dữ liệu-chất lượng các sự kiểm tra, thất bại các bài tập (drills), và
rollback các tiêu chí (A release gate for a serving system must include load tests, tail-latency measurements, data-quality checks, failure drills, and rollback criteria). Nghiên cứu các điểm chuẩn duy trì hữu ích cho việc so sánh các thuật toán, nhưng sản xuất
các cổng phải đo lường được triển khai hệ thống dưới lưu lượng truy cập, phần cứng, và thất bại các điều kiện nó sẽ
thực sự đối mặt (Research benchmarks remain useful for comparing algorithms, but production gates must measure the deployed system under the traffic, hardware, and failure conditions it will actually face).
12.14 Tóm tắt (Summary)
Việc đo điểm chuẩn hoàn thành Phần III’s sự tối ưu hóa đường ống bằng cách việc xác nhận liệu tính hiệu quả các lợi ích
từ dữ liệu sự lựa chọn (Chương 9), mô hình sự nén (Chương 10), và phần cứng sự gia tốc (Chương 11) cung cấp trong thực tiễn (Benchmarking completes Part III’s optimization pipeline by validating whether the efficiency gains from data selection (Chapter 9), model compression (Chapter 10), and hardware acceleration (Chapter 11) deliver in practice). Việc làm việc ngược (backward) thông qua sự tối ưu hóa ngăn xếp (phần cứng trước tiên, sau đó
mô hình chất lượng, sau đó dữ liệu tính đại diện), ba-chiều bộ khung bắt các thất bại tại
mỗi lớp trước khi chúng đổ như thác (cascade) tới sản xuất (Working backward through the optimization stack (hardware first, then model quality, then data representativeness), the three-dimensional framework catches failures at each layer before they cascade to production).
Sự xác nhận trình tự phản ánh cách các vấn đề biểu lộ (manifest): phần cứng các vấn đề bề mặt ngay lập tức
(sai thông lượng, thuộc về nhiệt sự điều chỉnh (thermal throttling)), mô hình chất lượng các vấn đề nổi lên dưới sự đánh giá (độ chính xác
sự suy thoái, sự hiệu chuẩn sự mất mát), và dữ liệu các vấn đề thường tiết lộ chính chúng chỉ trong sản xuất (sự phân phối
sự dịch chuyển, nhân khẩu học sự thiên vị) (The validation sequence reflects how problems manifest: hardware issues surface immediately (wrong throughput, thermal throttling), model quality issues emerge under evaluation (accuracy degradation, calibration loss), and data issues often reveal themselves only in production (distribution shift, demographic bias)). Hệ thống các điểm chuẩn giống như MLPerf Huấn luyện và Sự suy luận xác nhận
phần cứng các tuyên bố với được chuẩn hóa các khối lượng công việc (System benchmarks like MLPerf Training and Inference validate hardware claims with standardized workloads). Mô hình chất lượng các điểm chuẩn xác minh rằng sự nén
(đã) bảo tồn chí mạng các thuộc tính vượt ra ngoài trên-cùng-dòng độ chính xác (Model quality benchmarks verify that compression preserved critical properties beyond top-line accuracy). Dữ liệu các điểm chuẩn phơi bày tính đại diện
các khoảng cách thứ mà không số lượng của phần cứng sự tối ưu hóa có thể bù đắp cho (Data benchmarks expose representativeness gaps that no amount of hardware optimization can compensate for).
Nghiêm ngặt việc đo điểm chuẩn là cái gì phân biệt kỹ thuật các tuyên bố từ các phỏng đoán (Rigorous benchmarking is what distinguishes engineering claims from guesses). Những người thực hành (những) người
xác nhận của họ các sự tối ưu hóa một cách nghiêm ngặt, bằng cách việc đo lường đồng hồ-treo tường độ trễ thay vì việc tin tưởng FLOP
các số lượng (counts), việc lập hồ sơ đuôi các độ trễ thay vì các mức trung bình, và việc kiểm tra trên mang tính đại diện-sản xuất dữ liệu
thay vì thuận tiện các điểm chuẩn, xây dựng các hệ thống thứ mà hoạt động như mong đợi khi được triển khai (Practitioners who validate their optimizations rigorously, by measuring wall-clock latency rather than trusting FLOP counts, profiling tail latencies rather than averages, and testing on production-representative data rather than convenient benchmarks, build systems that perform as expected when deployed). Khi AI
các hệ thống trở nên ngày càng có sức ảnh hưởng trong chí mạng các ứng dụng, này sự đo lường sự nghiêm ngặt xác định
liệu sự tối ưu hóa các tuyên bố (có) dịch sang thế giới-thực tác động (hay không) (As AI systems become increasingly influential in critical applications, this measurement rigor determines whether optimization claims translate into real-world impact).
Chính Các bài học (Key Takeaways): Việc đo lường cái gì quan trọng (Measuring what matters)
• Các điểm chuẩn xác nhận đồng-thiết kế (co-design): Hệ thống, mô hình, và dữ liệu các điểm chuẩn phơi bày khác nhau
các thất bại: phần cứng sự giao-hàng dưới mức (underdelivery), sự nén chất lượng sự mất mát, và sự phân phối sự không khớp (Benchmarks validate co-design: System, model, and data benchmarks expose different failures: hardware underdelivery, compression quality loss, and distribution mismatch).
Một hệ thống thứ mà vượt qua chỉ một chiều có thể vẫn thất bại khi Dữ liệu, Thuật toán, và Máy móc
các sự ép buộc gặp dưới sản xuất tải (A system that passes only one axis can still fail when Data, Algorithm, and Machine constraints meet under production load).
• Đại diện (Proxy) các con số cần các ranh giới: Được chuẩn hóa chạy các quy tắc làm (cho) các sự so sánh (trở nên) trung thực, nhưng
cố định các khối lượng công việc là vẫn các đại diện (Proxy numbers need boundaries: Standardized run rules make comparisons honest, but fixed workloads are still proxies). Lô kích thước, thuộc về nhiệt trạng thái, đầu vào sự phân phối, tính đồng thời (concurrency),
và dịch vụ-thời hạn các cửa sổ quyết định liệu một phòng thí nghiệm kết quả (có) sống sót điểm chuẩn-
sản xuất khoảng cách (hay không) (Batch size, thermal state, input distribution, concurrency, and service-deadline windows decide whether a lab result survives the benchmark-production gap).
• Tính hạt (Granularity) đánh đổi sự chẩn đoán cho tính thực tế: Vi-điểm chuẩn (Micro-benchmarks) cô lập các hạt nhân (kernels), vĩ mô-
các điểm chuẩn (macro-benchmarks) phơi bày cấp độ-mô hình các chi phí, và kết thúc-tới-kết thúc các điểm chuẩn nắm bắt có thể nhìn thấy-với-người dùng
hành vi (Granularity trades diagnosis for realism: Micro-benchmarks isolate kernels, macro-benchmarks expose model-level costs, and end-to-end benchmarks capture user-visible behavior). Hiệu quả sự đo lường xếp chồng (stacks) tất cả ba do đó các đội có thể thấy cả hai triệu chứng và
lớp thứ mà (đã) gây ra nó (Effective measurement stacks all three so teams can see both the symptom and the layer that caused it).

12. Việc đo điểm chuẩn (Benchmarking)
707
• Đuôi độ trễ là điểm chuẩn (Tail latency is the benchmark): Tương tác các hệ thống thất bại tại p95 và p99 trước khi các mức trung bình
di chuyển (Interactive systems fail at p95 and p99 before averages move). Việc báo cáo phân vị (percentile) độ trễ dưới mang tính đại diện tải ngăn chặn một điểm chuẩn
từ việc phê duyệt (approving) một hệ thống (cái) có trung bình vượt qua trong khi của nó tồi tệ nhất-được phục vụ các yêu cầu vi phạm
SLO (Reporting percentile latency under representative load prevents a benchmark from approving a system whose mean passes while its worst-served requests violate the SLO).
• Amdahl giới hạn (caps) mọi sự tối ưu hóa tuyên bố: Một nhanh hơn mô hình không thể chạy nhanh hơn (outrun) phần còn lại của
đường ống; nếu sự tiền xử lý là 50 phần trăm của độ trễ, một vô hạn nhanh mô hình mang lại chỉ một
2× hệ thống sự cải thiện (Amdahl caps every optimization claim: A faster model cannot outrun the rest of the pipeline; if preprocessing is 50 percent of latency, an infinitely fast model yields only a 2× system improvement). Đo điểm chuẩn toàn bộ yêu cầu con đường trước khi việc ăn mừng (celebrating) hạt nhân
các sự tăng tốc (Benchmark the whole request path before celebrating kernel speedups).
• Tính hiệu quả vẫn cần chất lượng bằng chứng: INT8 có thể cắt bộ nhớ 4× và giảm MobileNet
sự suy luận năng lượng bởi khoảng 5.4×, nhưng sự hiệu chuẩn, nhóm phụ tính mạnh mẽ, và biên-trường hợp
hành vi quyết định liệu được nén mô hình là có thể triển khai (Efficiency still needs quality evidence: INT8 may cut memory 4× and reduce MobileNet inference energy by about 5.4×, but calibration, subgroup robustness, and edge-case behavior decide whether the compressed model is deployable).
Mọi chương trong này phần (đã) hứa hẹn một lợi ích của ít hơn FLOPs, một nhỏ hơn mô hình, hay cao hơn thông lượng (Every chapter in this part promised a gain of fewer FLOPs, a smaller model, or higher throughput).
Việc đo điểm chuẩn là nơi những các lời hứa đó được thực hiện để đối mặt hệ thống thứ mà sẽ giữ hay phá vỡ chúng (Benchmarking is where those promises are made to face the system that will keep or break them).
Khoảng cách giữa một được tuyên bố sự cải thiện và một được đo lường (cái) là không (phải) tiếng ồn mà (là) cấu trúc, nơi
mà Dữ liệu, Thuật toán, và Máy móc hóa ra để đã bị chỉ đơn thuần lắp ráp thay vì được khớp (The gap between a claimed improvement and a measured one is not noise but structure, the place where Data, Algorithm, and Machine turn out to have been merely assembled rather than matched):
Amdahl’s Định luật cho thấy tại sao một mô hình được làm (cho) vô hạn nhanh vẫn để lại một đường ống bị giới hạn bởi mọi thứ
bên ngoài nó, và đuôi cho thấy tại sao một mức trung bình có thể vượt qua trong khi tồi tệ nhất-được phục vụ yêu cầu thất bại (Amdahl’s Law shows why a model made infinitely fast still leaves a pipeline bounded by everything outside it, and the tail shows why an average can pass while the worst-served request fails). Này là
đồng-thiết kế được giữ để chịu trách nhiệm (held to account) (This is co-design held to account). Một ML hệ thống được thiết kế, không (phải) được khẳng định, và chỉ sự đo lường trên
thực khối lượng công việc có thể phân biệt hai (điều đó) với nhau (An ML system is engineered, not asserted, and only measurement on the real workload can tell the two apart).
Cái gì Tiếp theo: Từ phòng thí nghiệm tới trực tiếp (What’s Next: From lab to live)
Cái gì một hệ thống thứ mà vượt qua mọi điểm chuẩn thất bại để dự đoán? (What does a system that passes every benchmark fail to predict?) Sản xuất thực tế là cái gì
tĩnh các điểm chuẩn không thể nắm bắt: lưu lượng truy cập các sự bùng nổ (bursts), dữ liệu sự trôi dạt, và đổ thác (cascading) các thất bại thứ mà nổi lên
chỉ dưới (sự) tiếp xúc với trực tiếp các khối lượng công việc (Production reality is what static benchmarks cannot capture: traffic bursts, data drift, and cascading failures that emerge only under contact with live workloads). Phần IV rời khỏi được kiểm soát môi trường của
điểm chuẩn cho đó hỗn loạn thực tế, việc bắt đầu với Chương 13, nơi các hệ thống phải sống sót
sự tiếp xúc với thế giới thực (Part IV leaves the controlled environment of the benchmark for that chaotic reality, beginning with Chapter 13, where systems must survive contact with the real world).
Nghiên cứu Các câu hỏi (Research Questions): Cho xa hơn sự điều tra (For further inquiry)
• Cái gì điểm chuẩn giao thức làm (cho) các sự so sánh (trở nên) công bằng qua khác nhau phần cứng, các mô hình,
dữ liệu, và sự triển khai các giả định? (What benchmark protocol makes comparisons fair across different hardware, models, data, and deployment assumptions?)
• Khi (nào) nên vi, vĩ mô, và kết thúc-tới-kết thúc các điểm chuẩn được kết hợp, và cái gì (từng cái)
mỗi (cái) giấu? (When should micro, macro, and end-to-end benchmarks be combined, and what does each hide?)
• Nào số liệu tập ngăn chặn đơn-số liệu trò chơi hóa (gaming) qua độ trễ, đuôi độ trễ, thông lượng,
năng lượng, độ chính xác, và sự hiệu chuẩn? (Which metric set prevents single-metric gaming across latency, tail latency, throughput, energy, accuracy, and calibration?)
• Cách nào nên các đội dự đoán điểm chuẩn-sản xuất các khoảng cách từ sự trôi dạt, động tải,
thuộc về nhiệt sự điều chỉnh, và đầu vào sự biến thiên? (How should teams anticipate benchmark-production gaps from drift, dynamic load, thermal throttling, and input variation?)
IV
SỰ TRIỂN KHAI
VÀ (CÁC) HOẠT ĐỘNG (DEPLOYMENT AND OPERATIONS)
Phần IV (Part IV)
Sự triển khai Các nguyên tắc (Deployment Principles)
Mã là chính xác và các điểm chuẩn là xuất sắc, và tuy nhiên hệ thống thất bại (The code is correct and the benchmarks are excellent, and yet the system fails). Phần IV di chuyển từ
được kiểm soát các môi trường tới sự hỗn loạn của sản xuất, nơi ML các hệ thống đối mặt một mối đe dọa (threat) thứ mà truyền thống
phần mềm không (đối mặt): im lặng sự phân rã (decay) (Part IV moves from controlled environments to the chaos of production, where ML systems face a threat that traditional software does not: silent decay). Không giống như một chương trình thứ mà vỡ (crashes) khi của nó logic phá vỡ (breaks), một học
máy hệ thống tiếp tục để tạo ra các đầu ra thứ mà là tự tin, được định dạng tốt (well-formatted), và sai khi
thế giới trôi dạt xa khỏi của nó huấn luyện sự phân phối (Unlike a program that crashes when its logic breaks, a machine learning system continues to produce outputs that are confident, well-formatted, and wrong as the world drifts away from its training distribution). Tại sự triển khai, dữ liệu môi trường thoát khỏi (escapes)
kỹ sư’s sự kiểm soát, việc gây căng thẳng (stressing) được huấn luyện thuật toán và việc phục vụ máy móc theo các cách không bài kiểm tra tập (nào)
(đã) lường trước (At deployment, the data environment escapes the engineer’s control, stressing the trained algorithm and the serving machine in ways no test set anticipated). Tính đáng tin cậy là do đó một liên tục kiểm soát vòng lặp của D·A·M đồng-thiết kế thay vì một
một-lần sự phát hành cổng (Reliability is therefore a continuous control loop of D·A·M co-design rather than a one-time release gate). Các nguyên tắc ở đây xác định vật lý của đó tính đáng tin cậy (The principles here define the physics of that reliability).
Nguyên tắc (Principle) 9: Sự xác minh Khoảng cách (The Verification Gap)
Bất biến (Invariant): Trong truyền thống phần mềm, sự xác minh sử dụng đơn vị các bài kiểm tra (việc khẳng định (asserting) rằng 𝑓(𝑥) = 𝑦) (In traditional software, verification uses unit tests (asserting that 𝑓(𝑥) = 𝑦)). Trong
học máy, sự xác minh sử dụng thuộc về thống kê các giới hạn (bounds):
Pr(𝑓(𝑋) ≈ 𝑌) > 1−𝜖
Hệ quả (Implication): Sự triển khai là không (phải) một một-chiều sự chuyển giao; nó là một kiểm soát vòng lặp (Deployment is not a one-way transfer; it is a control loop). Bởi vì không bài kiểm tra bộ (suite) (nào) có thể
bao phủ mọi khả thi thế giới-thực đầu vào, sản xuất các hệ thống phải giám sát của riêng chúng sự không chắc chắn
và thất bại một cách tinh tế (gracefully) khi chúng trôi dạt ra ngoài của chúng được biết hiệu suất vỏ bọc (Because no test suite can cover every possible real-world input, production systems must monitor their own uncertainty and fail gracefully when they drift outside their known performance envelope).
Sự xác minh khoảng cách có nghĩa (rằng) tính đúng đắn không thể được chứng minh hoàn toàn (outright); nó có thể chỉ được giới hạn một cách thuộc về thống-
kê (The verification gap means correctness cannot be proven outright; it can only be bounded statistically). Những các giới hạn đó xói mòn (erode) khi sản xuất dữ liệu phân kỳ từ dữ liệu được sử dụng để thiết lập chúng (Those bounds erode as production data diverges from the data used to set them).
Nguyên tắc 10: Thuộc về thống kê Sự trôi dạt Bất biến (The Statistical Drift Invariant)
Bất biến (Invariant): Độ chính xác suy thoái khi thế giới trôi dạt từ huấn luyện sự phân phối, được chi phối bởi
sự suy thoái phương trình (Accuracy degrades as the world drifts from the training distribution, governed by the degradation equation):
Accuracy(𝑡) ≈ Accuracy0 − 𝜆⋅𝒟(𝑃𝑡‖𝑃0)
nơi Accuracy0 là mô hình’s hiệu suất tại sự triển khai, 𝒟(𝑃𝑡‖𝑃0) là thuộc về thống kê khoảng cách
giữa hiện tại dữ liệu sự phân phối và huấn luyện sự phân phối, và 𝜆 là mô hình’s
độ nhạy đối với sự phân phối sự dịch chuyển (where Accuracy0 is the model’s performance at deployment, 𝒟(𝑃𝑡‖𝑃0) is the statistical distance between the current data distribution and the training distribution, and 𝜆 is the model’s sensitivity to distributional shift). Hãy xem xét một tín dụng việc ghi điểm mô hình được huấn luyện trên 2020 người vay
hành vi (Consider a credit scoring model trained on 2020 borrower behavior). Hai các năm sau, lạm phát (inflation) tăng, lãi (interest) các suất (rates) thay đổi, và cho vay các chính sách dịch chuyển (Two years later, inflation rises, interest rates change, and lending policies shift). Hệ-
thống vẫn tạo ra các điểm số, nhưng thuộc về thống kê mối quan hệ giữa các đầu vào và các kết quả
đã di chuyển, và thực độ chính xác giảm (declines) trong khi thông thường lỗi các nhật ký duy trì im lặng (The system still produces scores, but the statistical relationship between inputs and outcomes has moved, and real accuracy declines while conventional error logs remain quiet). Không giống
nhiều truyền thống phần mềm các thất bại, thứ mà được thường xuyên phơi bày (surfaced) bởi các sự cố vỡ, các ngoại lệ, hay rõ ràng
dịch vụ-sức khỏe các tín hiệu, ML các hệ thống có thể thất bại một cách im lặng bởi vì môi trường thay đổi thậm chí khi
mã và cơ sở hạ tầng duy trì không thay đổi (Unlike many traditional software failures, which are often surfaced by crashes, exceptions, or explicit service-health signals, ML systems can fail silently because the environment changes even when the code and infrastructure remain unchanged). Này bậc-nhất sự tuyến tính hóa (linearization) nắm bắt
thống trị (dominant) hiệu ứng cho nhỏ sự phân phối các sự dịch chuyển; trong thực tiễn, mối quan hệ là phụ thuộc-vào-mô hình
và có thể là phi tuyến tính (nonlinear) cho lớn sự trôi dạt (This first-order linearization captures the dominant effect for small distributional shifts; in practice, the relationship is model-dependent and may be nonlinear for large drift).
709
710
Sự triển khai Các nguyên tắc (Deployment Principles)
Hệ quả: Khả năng quan sát (Observability) phải dịch chuyển từ hệ thống các số liệu (độ trễ, các lỗi) tới thuộc về thống kê các số liệu
(sự phân phối khoảng cách) (Observability must shift from system metrics (latency, errors) to statistical metrics (distribution distance)). Mà không có dữ liệu sự trôi dạt việc giám sát, một hệ thống có thể duy trì hoạt động trong khi
của nó các dự đoán trở nên đều đặn kém đáng tin cậy (hơn) (Without data drift monitoring, a system can remain operational while its predictions become steadily less reliable).
Bên ngoài sự trôi dạt là không (phải) duy nhất mối đe dọa (External drift is not the only threat). Thậm chí khi thế giới giữ (nguyên) đứng im (still), việc phục vụ đường ống chính nó
có thể phân kỳ từ mô hình được xác nhận ngoại tuyến (Even when the world holds still, the serving pipeline itself can diverge from the model validated offline).
Nguyên tắc 11: Huấn luyện-Việc phục vụ Sự lệch (Skew) Định luật (The Training-Serving Skew Law)
Bất biến: Nếu hàm được tính toán trong suốt việc phục vụ (𝑓serve) khác biệt từ hàm được học
trong suốt huấn luyện (𝑓train), mô hình’s hiệu quả độ chính xác suy thoái tỷ lệ thuận tới sự phân kỳ (If the function computed during serving (𝑓serve) differs from the function learned during training (𝑓train), the model’s effective accuracy degrades proportionally to the divergence):
ΔAccuracy ∝ 𝔼[|𝑓serve(𝑥)−𝑓train(𝑥)|]
Chính xác mối quan hệ phụ thuộc trên mất mát hàm, quyết định ranh giới hình học, và sản-
xuất sự phân phối, nhưng không được giải thích sự phân kỳ làm mất hiệu lực giả định rằng ngoại tuyến sự xác nhận
ước tính sản xuất hành vi và có thể gây ra im lặng độ chính xác sự mất mát (The exact relationship depends on the loss function, decision boundary geometry, and production distribution, but unexplained divergence invalidates the assumption that offline validation estimates production behavior and can cause silent accuracy loss). Này sự phân kỳ nổi lên từ
không nhất quán tiền xử lý logic, khác nhau thư viện các sự triển khai (implementations), cũ rích (stale) tính năng các giá trị, hay
môi trường trạng thái các sự thay đổi giữa hai mã các con đường (This divergence arises from inconsistent preprocessing logic, different library implementations, stale feature values, or environmental state changes between the two code paths).
Hệ quả: Tính năng tính nhất quán là một cứng thuộc về kiến trúc yêu cầu, không (phải) một thực tiễn tốt nhất (Feature consistency is a hard architectural requirement, not a best practice). Tính-
năng các cửa hàng là không (phải) các bộ nhớ đệm; chúng là tính nhất quán các động cơ thứ mà giảm sự lệch bằng cách việc tập trung hóa
tính năng các định nghĩa và sự truy xuất (Feature stores are not caches; they are consistency engines that reduce skew by centralizing feature definitions and retrieval). Các đội vẫn cần sự xác nhận cho sự mới mẻ, điểm-trong-thời gian tính đúng-
đắn, sự tiền xử lý, mô hình-thời gian chạy (runtime), và hậu xử lý tính ngang bằng (parity) (Teams still need validation for freshness, point-in-time correctness, preprocessing, model-runtime, and postprocessing parity). Thậm chí tinh tế các sự khác biệt
(PIL so với OpenCV thay đổi kích thước, FP64 so với FP32 sự chuẩn hóa) làm phức tạp để tạo ra im lặng độ chính xác
sự suy thoái thứ mà tiêu chuẩn việc giám sát sẽ không phát hiện (Even subtle differences (PIL vs. OpenCV resize, FP64 vs. FP32 normalization) compound to produce silent accuracy degradation that standard monitoring will not detect).
Bên dưới tất cả những tính đáng tin cậy các mối quan tâm này nằm (ở) một không thể thương lượng sự ép buộc: thời gian (Beneath all these reliability concerns lies a nonnegotiable constraint: time). Một y tế hình ảnh
hệ thống thứ mà phát hiện các khối u (tumors) với 99 phần trăm độ chính xác nhưng tốn 30 giây mỗi (lần) quét ép buộc những bác sĩ X quang (radiologists)
quay lại thủ công sự đánh giá (A medical imaging system that detects tumors with 99 percent accuracy but takes 30 seconds per scan forces radiologists back to manual review). Một tự trị phương tiện nhận thức (perception) mô hình thứ mà phân loại các chướng ngại vật một cách hoàn hảo
nhưng phản hồi trong 200 ms thay vì 50 ms không thể phanh (brake) trong thời gian (An autonomous vehicle perception model that classifies obstacles perfectly but responds in 200 ms instead of 50 ms cannot brake in time). Thuộc về thống kê tính đúng đắn là vô giá trị nếu nó
đến quá trễ (Statistical correctness is worthless if it arrives too late). Mọi được triển khai mô hình hoạt động dưới một độ trễ trần (ceiling), và việc vượt quá đó trần
là một cách chức năng (functionally) tương đương tới việc trả về không dự đoán (nào) cả (Every deployed model operates under a latency ceiling, and exceeding that ceiling is functionally equivalent to returning no prediction at all).
Nguyên tắc 12: Độ trễ Ngân sách Bất biến (The Latency Budget Invariant)
Bất biến: Trong nhạy cảm-độ trễ việc phục vụ, cứng sự ép buộc là một đuôi-độ trễ SLO được xác định tại
P95, P99, P99.9, hay một cụ thể-ứng dụng thời hạn; thông lượng là biến để (được) tối ưu hóa
bên trong đó sự ép buộc (In latency-sensitive serving, the hard constraint is a tail-latency SLO defined at P95, P99, P99.9, or an application-specific deadline; throughput is the variable to be optimized within that constraint). Này là được chi phối bởi độ trễ ngân sách phương trình (This is governed by the latency budget equation):
𝐿lat,total = 𝐿lat,net + 𝐿lat,pre + 𝐿lat,infer + 𝐿lat,post + 𝐿lat,queue ≤ SLO
Hệ quả: Việc phục vụ các hệ thống phải triển khai (implement) khoan dung-đuôi (tail-tolerant) các thiết kế (cho ví dụ, động
việc tạo lô, được phòng hộ (hedged) các yêu cầu) (Serving systems must implement tail-tolerant designs (for example, dynamic batching, hedged requests)). Việc phục vụ các hệ thống phải sẵn lòng (willing) để hy sinh tổng thể thông lượng để
đáp ứng độ trễ thời hạn của cũ nhất yêu cầu trong hàng đợi (Serving systems must be willing to sacrifice overall throughput to meet the latency deadline of the oldest request in the queue).
Một hệ thống có thể thỏa mãn mọi độ trễ SLO, phát hiện mọi sự phân phối sự dịch chuyển, và duy trì hoàn hảo
huấn luyện-việc phục vụ tính nhất quán trong khi vẫn gây ra có hệ thống tác hại (harm) (A system can satisfy every latency SLO, detect every distributional shift, and maintain perfect training-serving consistency while still causing systematic harm). Trước đó các nguyên tắc giải quyết
im lặng các thất bại trong tính đúng đắn và dịch vụ chất lượng; (nguyên tắc) này giải quyết một thất bại thứ mà làm suy thoái tính công bằng (equity),
thông qua giống nhau cơ chế của im lặng sự khuếch đại (amplification) (The previous principles address silent failures in correctness and service quality; this one addresses a failure that degrades equity, through the same mechanism of silent amplification).