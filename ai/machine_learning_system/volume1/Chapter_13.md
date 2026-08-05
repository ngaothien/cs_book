Sự triển khai Các nguyên tắc (Deployment Principles)
711
Nguyên tắc 13: Sự thiên vị (Bias) Phản hồi (Feedback) Bất biến (The Bias Feedback Invariant)
Bất biến: Khi một mô hình’s các đầu ra ảnh hưởng sự phân phối của của nó tương lai các đầu vào, dự đoán
các lỗi có thể phức tạp (compound) qua quyết định các chu kỳ (When a model’s outputs influence the distribution of its future inputs, prediction errors can compound across decision cycles). Cho một được đơn giản hóa tự-củng cố (self-reinforcing) phản hồi vòng lặp,
sự chênh lệch (disparity) cho nhóm 𝑔 sau 𝑘 sự triển khai các chu kỳ có thể tăng trưởng như (For a simplified self-reinforcing feedback loop, the disparity for group 𝑔 after 𝑘 deployment cycles may grow as):
Δ𝑔(𝑘) ≈ Δ𝑔(0)⋅𝛼𝑘
fb
nơi Δ𝑔(0) là ban đầu hiệu suất khoảng cách giữa các nhóm và 𝛼fb là sự khuếch đại hệ số
được xác định bởi cách mạnh mẽ mô hình’s các quyết định định hình lại (reshape) hạ lưu dữ liệu (where Δ𝑔(0) is the initial performance gap between groups and 𝛼fb is the amplification factor determined by how strongly the model’s decisions reshape downstream data). Hãy xem xét một khoản vay
sự phê duyệt (approval) mô hình thứ mà từ chối tín dụng tại cao hơn các tỷ lệ cho những người nộp đơn (applicants) từ về mặt lịch sử không được phục vụ đầy đủ (underserved)
các cộng đồng (Consider a loan approval model that denies credit at higher rates to applicants from historically underserved communities). Bị từ chối những người nộp đơn không thể xây dựng tín dụng lịch sử, thứ mà làm (cho) tương lai các đơn đăng ký (applications)
yếu hơn, thứ mà tăng tương lai từ chối các tỷ lệ (Denied applicants cannot build credit history, which makes future applications weaker, which increases future denial rates). Mô hình’s độ chính xác trên của nó huấn luyện sự phân phối
duy trì ổn định, nhưng dân số (population) nó phục vụ đã bị định hình lại bởi của riêng nó các quyết định (The model’s accuracy on its training distribution remains stable, but the population it serves has been reshaped by its own decisions). Khi
𝛼fb > 1, phản hồi vòng lặp là tự-củng cố (self-reinforcing); khi 𝛼fb ≤ 1, các động lực (dynamics) là ổn định hay bị dập tắt (damped) (When 𝛼fb > 1, the feedback loop is self-reinforcing; when 𝛼fb ≤ 1, the dynamics are stable or damped).
Thực các sự triển khai có thể cũng là phi tuyến tính hay đang bão hòa (Real deployments may also be nonlinear or saturating).
Hệ quả: Tính công bằng (Fairness) là không (phải) một hậu-sự triển khai (postdeployment) cuộc kiểm toán (audit); nó là một tính ổn định sự ép buộc trên sự triển-
khai kiểm soát vòng lặp (Fairness is not a postdeployment audit; it is a stability constraint on the deployment control loop). Các hệ thống phải giám sát được phân tách (disaggregated) hiệu suất các số liệu qua
nhân khẩu học các nhóm với giống nhau sự nghiêm ngặt được áp dụng tới độ trễ các phân vị, bởi vì một sự thiên vị sự thoái-
lui (regression) là vô hình tới tổng hợp độ chính xác chỉ như một đuôi-độ trễ sự vi phạm là vô hình tới trung bình
độ trễ (Systems must monitor disaggregated performance metrics across demographic groups with the same rigor applied to latency percentiles, because a bias regression is invisible to aggregate accuracy just as a tail-latency violation is invisible to mean latency).
Phần IV dịch những năm các nguyên tắc này vào sản xuất các hệ thống: việc phục vụ cơ sở hạ tầng thứ mà đáp ứng
độ trễ các ngân sách (độ trễ ngân sách bất biến), hoạt động các thực tiễn thứ mà phát hiện sự trôi dạt và sự lệch trước khi
người dùng làm (sự xác minh khoảng cách, thuộc về thống kê sự trôi dạt, và huấn luyện-việc phục vụ sự lệch các nguyên tắc), có trách nhiệm
kỹ thuật thứ mà xử lý (treats) tính công bằng như một có thể đo lường sự triển khai sự ép buộc (sự thiên vị phản hồi bất biến) (Part IV translates these five principles into production systems: serving infrastructure that meets latency budgets (the latency budget invariant), operational practices that detect drift and skew before users do (the verification gap, statistical drift, and training-serving skew principles), responsible engineering that treats fairness as a measurable deployment constraint (the bias feedback invariant)).
Sự tổng hợp (synthesis) thứ mà kết nối những sự triển khai các thực tế này tới định lượng các bất biến được thiết lập
xuyên suốt cuốn sách đóng (closes) tập (volume) (The synthesis that connects these deployment realities to the quantitative invariants established throughout the book closes the volume).
Các ứng dụng (Applications)
(Các) hoạt động (Operations)
Việc phục vụ (Serving)
Huấn luyện (Training)
Các mô hình (Models)
Các bộ khung (Frameworks)
Phần cứng (Hardware)
Dữ liệu (Data)
13
Mô hình Việc phục vụ (Model Serving)
13.1 Việc phục vụ Mô hình mẫu (Serving Paradigm)
13.2 Việc phục vụ Tải, Độ trễ,
và Kiến trúc (Serving Load, Latency, and Architecture)
13.3 Việc phục vụ Hệ thống
Kiến trúc (Serving System Architecture)
13.4 Yêu cầu Vòng đời (Request Lifecycle)
13.5 Xếp hàng đợi Lý thuyết (Queuing Theory)
13.6 Mô hình Vòng đời
Sự quản lý (Model Lifecycle Management)
13.7 Thông lượng
Sự tối ưu hóa (Throughput Optimization)
13.8 LLM Việc phục vụ (LLM Serving)
13.9 Sự suy luận Thời gian chạy
Sự lựa chọn (Inference Runtime Selection)
13.10 Cấp độ-Nút (Node-Level)
Sự tối ưu hóa (Node-Level Optimization)
13.11 Kinh tế học và Sự lập kế hoạch (Economics and Planning)
13.12 Các ngụy biện và Các cạm bẫy (Fallacies and Pitfalls)
13.13 Tóm tắt (Summary)
Mục đích (Purpose)
Tại sao (do) việc phục vụ đảo ngược mọi sự tối ưu hóa ưu tiên thứ mà (đã) làm (cho) huấn luyện (trở nên) thành công? (Why does serving invert every optimization priority that made training successful?)
Huấn luyện và việc phục vụ đòi hỏi đối lập vật lý (Training and serving demand opposite physics). Huấn luyện tối đa hóa thông lượng (các mẫu mỗi
giây): lớn các lô và dài các kỷ nguyên (epochs) nơi độ trễ các sự bùng nổ (spikes) bị (get) hấp thụ một cách vô hình (Training maximizes throughput (samples per second): large batches and long epochs where latency spikes get absorbed invisibly). Việc phục vụ
tối thiểu hóa độ trễ, được đo lường trong mili giây mỗi yêu cầu: cá nhân các yêu cầu được trả lời đủ nhanh
rằng một đơn chậm phản hồi là một bị phá vỡ sản phẩm (Serving minimizes latency, measured in milliseconds per request: individual requests answered fast enough that a single slow response is a broken product). Huấn luyện khấu hao (amortizes) phần cứng các chi phí qua hàng tỷ
các ví dụ; việc phục vụ trả một thuế trên mọi yêu cầu, nơi nhỏ các sự không hiệu quả phức tạp thành hoạt động
nợ (Training amortizes hardware costs across billions of examples; serving pays a tax on every request, where small inefficiencies compound into operational debt). Này sự đảo ngược là tại sao các mô hình thứ mà huấn luyện một cách đẹp đẽ thường phục vụ một cách tồi tệ: nặng-lô (batch-heavy)
các kiến trúc và chuyên sâu-bộ nhớ (memory-intensive) các sự tối ưu hóa được thiết kế để làm bão hòa các máy gia tốc trong suốt huấn luyện
là một cách cơ bản không-phù hợp (ill-suited) cho bùng nổ (bursty), tới hạn-độ trễ (latency-critical), nhạy cảm-chi phí (cost-sensitive) thực tế của sản xuất lưu lượng truy cập (This inversion is why models that train beautifully often serve poorly: the batch-heavy architectures and memory-intensive optimizations designed to saturate accelerators during training are fundamentally ill-suited for the bursty, latency-critical, cost-sensitive reality of production traffic).
Việc phục vụ, tuy nhiên, là nhiều hơn một độ trễ vấn đề (Serving, however, is more than a latency problem). Một việc phục vụ hệ thống phải xử lý lưu lượng truy cập thứ mà biến đổi
bởi các bậc của độ lớn giữa đỉnh (peak) và đáy (trough), giới thiệu mới mô hình các phiên bản mà không có (sự) đột ngột
việc di chuyển tất cả người dùng tại một (lúc), suy thoái một cách tinh tế khi thượng lưu (upstream) các sự phụ thuộc thất bại, và làm tất cả (những điều) này
một cách liên tục, không (phải) cho khoảng thời gian của một huấn luyện chạy mà (là) cho vòng đời của sản phẩm (A serving system must handle traffic that varies by orders of magnitude between peak and trough, introduce new model versions without abruptly moving all users at once, degrade gracefully when upstream dependencies fail, and do all of this continuously, not for the duration of a training run but for the lifetime of the product). Mọi mô hình
thứ mà (đã) chứng minh của nó giá trị trong suốt huấn luyện và (đã) sống sót sự nén và việc đo điểm chuẩn cuối cùng
đến tại việc phục vụ lớp—sự triển khai và sự tích hợp giai đoạn của ML vòng đời—nơi
câu hỏi dịch chuyển từ “liệu nó (có) hoạt động (hay không)?” tới “liệu nó (có) hoạt động một cách đáng tin cậy, tại quy mô, dưới sản xuất các điều kiện,
mỗi giây của mỗi ngày (hay không)?” (Every model that proved its value during training and survived compression and benchmarking eventually arrives at the serving layer—the deployment and integration stage of the ML lifecycle—where the question shifts from “does it work?” to “does it work reliably, at scale, under production conditions, every second of every day?”) Việc phục vụ cơ sở hạ tầng là nơi ML các hệ thống cuối cùng gặp những người dùng,
và kỹ thuật (cái) thứ mà duy trì đó cuộc gặp gỡ là một cách định tính khác biệt từ kỹ thuật thứ mà
(đã) tạo ra mô hình (The serving infrastructure is where ML systems finally meet users, and the engineering that sustains that meeting is qualitatively different from the engineering that created the model). Nó là cũng nơi được huấn luyện thuật toán gặp trực tiếp dữ liệu bên trong máy móc’s
độ trễ ngân sách: tất cả ba D·A·M các sự ép buộc hội tụ trên mọi yêu cầu (It is also where the trained algorithm meets live data within the machine’s latency budget: all three D·A·M constraints converge on every request).

714
13.1 Việc phục vụ Mô hình mẫu (Serving Paradigm)
Học Các mục tiêu (Learning Objectives)
• Giải thích việc phục vụ sự đảo ngược từ huấn luyện thông lượng tới mỗi-yêu cầu độ trễ, khoảng không (headroom),
và đuôi hành vi (Explain serving inversion from training throughput to per-request latency, headroom, and tail behavior)
• Phân rã (Decompose) yêu cầu độ trễ qua sự tuần tự hóa (serialization), sự tiền xử lý, sự suy luận, việc xếp hàng đợi, sự hậu-
xử lý, và mạng chi phí hoạt động (Decompose request latency across serialization, preprocessing, inference, queuing, postprocessing, and network overhead)
• Áp dụng xếp hàng đợi (queueing) các định luật và đơn giản hàng đợi các mô hình để lên kế hoạch công suất chống lại phân vị độ trễ
các mục tiêu (Apply queueing laws and simple queue models to plan capacity against percentile latency targets)
• Chẩn đoán huấn luyện-việc phục vụ sự lệch và lạnh các sự khởi động từ không khớp sự tiền xử lý, mô hình
việc tải, hay bộ nhớ đệm hành vi (Diagnose training-serving skew and cold starts from mismatched preprocessing, model loading, or cache behavior)
• Lựa chọn việc tạo lô, tải sự đổ (shedding), tự động mở rộng (autoscaling), và thời gian chạy các chiến lược cho lưu lượng truy cập các mẫu
và độ trễ các ngân sách (Select batching, load shedding, autoscaling, and runtime strategies for traffic patterns and latency budgets)
• Đánh giá LLM việc phục vụ các nút thắt cổ chai bằng cách sử dụng mã thông báo độ trễ, KV-bộ nhớ đệm bộ nhớ, và liên tục
việc tạo lô các sự ép buộc (Evaluate LLM serving bottlenecks using token latency, KV-cache memory, and continuous batching constraints)
• Tính toán chi phí mỗi sự suy luận từ độ chính xác, phần cứng sự sử dụng, bản sao (replica) số lượng, và
thời gian chạy thông lượng (Calculate cost per inference from precision, hardware utilization, replica count, and runtime throughput)
13.1 Việc phục vụ Mô hình mẫu (Serving Paradigm)
Việc phục vụ bắt đầu nơi việc đo điểm chuẩn dừng (lại): một mô hình (cái) thứ mà đã hoạt động dưới được kiểm soát sự đo-
lường phải bây giờ trả lời không thể đoán trước trực tiếp các yêu cầu (Serving begins where benchmarking stops: a model that performed under controlled measurement must now answer unpredictable live requests). Đám mây (Cloud), Biên, Di động (Mobile), và TinyML
mỗi (thứ) áp đặt khác biệt việc phục vụ các thách thức, nhưng tất cả chia sẻ giống nhau sự đảo ngược từ thông lượng
sự tối ưu hóa tới độ trễ sự kiểm soát (Cloud, Edge, Mobile, and TinyML each impose distinct serving challenges, but all share the same inversion from throughput optimization to latency control). Này việc phục vụ sự đảo ngược có cụ thể kỹ thuật các hệ quả thứ mà
lan tỏa (ripple) thông qua toàn bộ ngăn xếp (This serving inversion has concrete engineering implications that ripple through the whole stack). Sắt (iron) định luật của ML các hệ thống trải qua (undergoes) một quyết định (decisive) sự dịch chuyển: độ trễ
số hạng (𝐿lat), việc đại diện cho không thể giảm thiểu (irreducible) chi phí hoạt động của yêu cầu việc lập lịch (scheduling), mạng khứ hồi (round-trips), và
hệ thống sự điều phối (orchestration), trở thành thống trị (dominant) sự ép buộc thay vì một làm tròn lỗi (The iron law of ML systems undergoes a decisive shift: the latency term (𝐿lat), representing the irreducible overhead of request scheduling, network round-trips, and system orchestration, becomes the dominant constraint rather than a rounding error). Được kiểm soát
các điểm chuẩn thiết lập hiệu suất dưới được biết các điều kiện; việc phục vụ đối mặt lưu lượng truy cập các mẫu không điểm chuẩn
(nào) có thể hoàn toàn lường trước (Controlled benchmarks establish performance under known conditions; serving faces traffic patterns no benchmark can fully anticipate). Sự lượng tử hóa có thể giảm mô hình kích thước; việc phục vụ phải xác nhận rằng những
các sự tối ưu hóa (như vậy) bảo tồn độ chính xác dưới thực lưu lượng truy cập các sự phân phối (Quantization can reduce model size; serving must confirm that such optimizations preserve accuracy under real traffic distributions). Cùng với nhau những các sự tái xác nhận (revalidations) này lật (flip)
các sự ưu tiên của dữ liệu, thuật toán, và máy móc một khi các yêu cầu đến từng (cái) một tại một (thời) điểm dưới một độ trễ ngân sách (Together these revalidations flip the priorities of data, algorithm, and machine once requests arrive one at a time under a latency budget).
D·A·M phân loại học làm (cho) sự đảo ngược (trở nên) có thể nhìn thấy (The D·A·M taxonomy makes the inversion visible). Dữ liệu sự ép buộc dịch chuyển từ khối lượng tới
sự mới mẻ: hệ thống phải xử lý một trực tiếp yêu cầu ngay lập tức, không (phải) xáo trộn hàng tỷ của các ví dụ qua
một huấn luyện chạy (The data constraint shifts from volume to freshness: the system must process a live request immediately, not shuffle billions of examples over a training run). Thuật toán sự ép buộc dịch chuyển từ có thể thay đổi (mutable) tới bị đóng băng (frozen): việc phục vụ chạy một cố định chuyển tiếp
vượt qua (pass) thay vì việc cập nhật các trọng số thông qua lan truyền ngược (The algorithm constraint shifts from mutable to frozen: serving runs a fixed forward pass rather than updating weights through backpropagation). Máy móc sự ép buộc dịch chuyển từ
sự sử dụng tới khoảng không: một máy gia tốc được giữ tại 40 tới 60 phần trăm sự sử dụng có thể hấp thụ lưu lượng truy cập các sự bùng nổ,
trong khi một bị bão hòa máy gia tốc biến nhỏ tải các sự thay đổi thành đuôi-độ trễ các thất bại (The machine constraint shifts from utilization to headroom: an accelerator held at 40 to 60 percent utilization can absorb traffic spikes, while a saturated accelerator turns small load changes into tail-latency failures). Việc phục vụ do đó
tối ưu hóa hữu ích được hoàn thành công việc dưới một độ trễ lời hứa thay vì hoàn toàn bị chiếm giữ (occupied) phần cứng (Serving therefore optimizes useful completed work under a latency promise rather than fully occupied hardware).
Đó lời hứa buộc các còn lại phần của việc phục vụ ngăn xếp cùng với nhau (That promise ties the remaining parts of the serving stack together). Yêu cầu việc định tuyến (routing), sự tiền xử lý,
mô hình sự thực thi, sự hậu xử lý, việc tạo lô, việc lưu bộ nhớ đệm, thời gian chạy sự lựa chọn, và công suất sự lập kế hoạch tất cả
cạnh tranh cho giống nhau độ trễ ngân sách (Request routing, preprocessing, model execution, postprocessing, batching, caching, runtime selection, and capacity planning all compete for the same latency budget). Trung tâm kỹ thuật nhiệm vụ là để quyết định (cái) công việc nào thuộc về
trong trực tiếp yêu cầu con đường, (cái) công việc nào có thể di chuyển ra ngoài nó, và bao nhiêu khoảng không hệ thống phải
dự trữ trước khi hữu ích thông lượng trở nên mỏng manh (fragile) (The central engineering task is to decide which work belongs in the live request path, which work can move outside it, and how much headroom the system must reserve before useful throughput becomes fragile).
13.2 Việc phục vụ Tải, Độ trễ, và Kiến trúc (Serving Load, Latency, and Architecture)
Một đơn lưu lượng truy cập sự bùng nổ thứ mà vượt quá này lề (margin) có thể đổ thác thành toàn-hệ thống (system-wide) thất bại; xếp hàng đợi
đường cong trong hình 13.1 làm (cho) đó sự sụp đổ (collapse) (trở nên) có thể nhìn thấy (A single traffic spike that exceeds this margin can cascade into system-wide failure; the queueing curve in figure 13.1 makes that collapse visible).
Ví dụ 13.1: ’Thứ sáu Đen (Black Friday)’ lưu lượng truy cập sự bùng nổ
Kịch bản: Một thương mại điện tử (e-commerce) sự giới thiệu hệ thống chạy một cách thoải mái tại 50 ms với 1,000 QPS.
Thất bại chế độ (mode): Trên Thứ sáu Đen, lưu lượng truy cập bùng nổ 10× tới 10,000 QPS. Hệ thống không (bị) chậm
xuống 10×; nó sụp đổ. Độ trễ chạm 10 s, sau đó các yêu cầu bắt đầu việc tính giờ ra (timing out) (The system does not slow down 10×; it collapses. Latency hits 10 s, then requests start timing out). Các máy chủ là 100
13. Mô hình Việc phục vụ (Model Serving)
715
1
Jevons Nghịch lý (Paradox): William
Stanley Jevons đã quan sát trong
1865 rằng tính hiệu quả các sự cải-
thiện trong được cấp nguồn bằng than (coal-powered) hơi nước (steam)
các động cơ (đã) làm tăng tổng than
sự tiêu thụ
bằng cách
việc làm (cho)
hơi nước năng lượng (power) về mặt kinh tế (economically)
có thể tồn tại (viable)
cho
các ứng dụng
trước đó quá tốn kém (Jevons
1865). Giống nhau động lực (dynamic) có thể
áp dụng tới AI sự suy luận: mỗi
10× chi phí sự giảm thiểu mở ra
ứng dụng các lớp thứ mà (đã) là
về mặt kinh tế
không thể khả thi (infeasible)
tại
trước đó
giá
điểm,
việc mở rộng tổng hợp (aggregate) nhu cầu
bởi nhiều hơn (là) tính hiệu quả
lợi ích (The same dynamic can apply to AI inference: each 10× cost reduction opens application classes that were economically infeasible at the previous price point, expanding aggregate demand by more than the efficiency gain).
Này là tại sao rẻ hơn
sự suy luận có thể làm tăng, không (phải)
làm giảm,
tổng
GPU
hạm đội (fleet)
nhu cầu—tính hiệu quả và nhu-
cầu là thường xuyên các phần bù (complements)
trong AI, không (phải) các vật thay thế (substitutes).
phần trăm được tải, nhưng hữu ích thông lượng giảm tới gần không bởi vì hầu hết được hoàn thành các yêu cầu
đã hết giờ từ khách hàng’s góc nhìn (percent loaded, but useful throughput drops to near zero because most completed requests have already timed out from the client’s perspective).
Vật lý: Này xem trước (previews) xếp hàng đợi lý thuyết được chính thức hóa (formalized) muộn hơn trong phần 13.5. Khi sự sử dụng
tiếp cận 100 phần trăm, hàng đợi các độ dài phân kỳ một cách phi tuyến tính thay vì một cách tuyến tính (As utilization approaches 100 percent, queue lengths diverge nonlinearly rather than linearly). Hệ thống
dành nhiều thời gian hơn (để) quản lý hàng đợi (ngữ cảnh việc chuyển đổi (switching), thrashing) thay vì việc làm hữu ích công việc (The system spends more time managing the queue (context switching, thrashing) than doing useful work).
Cách sửa (Fix):
1. Tải sự đổ (shedding): Từ chối dư thừa các yêu cầu ngay lập tức để giữ hàng đợi ngắn (Reject excess requests immediately to keep the queue short).
2. Tự động mở rộng (Autoscaling): Sử dụng một hoạt động kiểm soát vòng lặp để quay lên (spin up) nhiều hơn việc phục vụ các bản sao trước khi
sự sử dụng chạm “đầu gối (knee)” của đường cong (Use an operational control loop to spin up more serving replicas before utilization hits the “knee” of the curve).
3. Sự suy thoái (Degradation): Phục vụ được lưu bộ nhớ đệm/ngu ngốc hơn các sự giới thiệu để giảm tính toán chi phí mỗi truy vấn (Serve cached/dumber recommendations to reduce compute cost per query).
Các hệ thống bài học: Cao trung bình thông lượng không bảo vệ một việc phục vụ hệ thống khỏi (sự) sụp đổ (High average throughput does not protect a serving system from collapse). Đuôi
độ trễ sự kiểm soát yêu cầu việc giữ sự sử dụng bên dưới xếp hàng đợi đầu gối, việc tôn trọng máy móc
sự ép buộc thậm chí nếu đó (điều đó) có nghĩa (là) việc đổ tải hay việc phục vụ một rẻ hơn mô hình (Tail latency control requires keeping utilization below the queueing knee, honoring the machine constraint even if that means shedding load or serving a cheaper model).
Hình 13.1 cho thấy rằng độ trễ duy trì có thể quản lý tại vừa phải sự sử dụng và sau đó tăng (rises) một cách nhanh chóng
khi hệ thống tiếp cận sự bão hòa; này là tại sao sản xuất các hệ thống dự trữ khoảng không thay vì
việc lập kế hoạch cho một một cách vĩnh viễn bị bão hòa máy gia tốc (p99) (Figure 13.1 shows that latency remains manageable at moderate utilization and then rises rapidly as the system approaches saturation; this is why production systems reserve headroom rather than planning for a permanently saturated accelerator (p99)). Phần B.2.1 cung cấp một toán học sự xử lý (treatment)
của đuôi-dài (long-tailed) các sự phân phối và tại sao p99 độ trễ chi phối người dùng trải nghiệm tại quy mô (Section B.2.1 gives a mathematical treatment of long-tailed distributions and why p99 latency dominates the user experience at scale). Đường cong
là một đơn giản xếp hàng đợi sự xấp xỉ (approximation) được dự định cho trực giác (intuition) thay vì một cụ thể khối lượng công việc (The curve is a simple queueing approximation intended for intuition rather than a specific workload).
0%
20%
40%
60%
80%
100%
Hệ thống Sự sử dụng (System Utilization) (%)
0
10
20
30
40
50
Yêu cầu Độ trễ (được chuẩn hóa tới dịch vụ thời gian) (Request Latency (normalized to service time))
An toàn Vùng (Safe Zone)
Nguy hiểm Vùng (Danger Zone)
(Hàng đợi
Sự bùng nổ (Explosion))
Đầu gối (The Knee)
Trung bình Độ trễ (Mean Latency)
Đuôi Độ trễ (p99) (Tail Latency (p99))
Hình 13.1: Đuôi Độ trễ Sự bùng nổ (The Tail Latency Explosion): Yêu cầu độ trễ so với việc phục vụ sự sử dụng 𝜌serv (Request latency vs. serving utilization 𝜌serv). Trong khi trung bình độ trễ (xanh dương) duy trì
vừa phải, đuôi độ trễ (đỏ, p99) bùng nổ một khi sự sử dụng vượt qua đầu gối tại ~70 phần trăm (While mean latency (blue) remains moderate, tail latency (red, p99) explodes once utilization passes the knee at ~70 percent). Này sử dụng đơn giản M/M/1
sự xấp xỉ được giới thiệu muộn hơn trong phần 13.5 (p99 ≈ 4.6× trung bình), do đó đường cong là có tính minh họa thay vì cụ thể-khối lượng công việc (This uses the simple M/M/1 approximation introduced later in section 13.5 (p99 ≈ 4.6× mean), so the curve is illustrative rather than workload-specific).
Vượt ra ngoài kỹ thuật các giới hạn của độ trễ, kinh tế học của việc phục vụ đã trải qua một triệt để (radical) sự biến-
đổi (trans-formation) (Beyond the technical limits of latency, the economics of serving have undergone a radical transformation). Khi các mô hình trở nên nhiều hơn hiệu quả và phần cứng trở nên nhiều hơn được chuyên môn hóa (specialized), chi phí của
“trí thông minh” là (đang) sụp đổ1 (As models become more efficient and hardware becomes more specialized, the cost of “intelligence” is collapsing). Facebook’s kinh nghiệm tại hạm đội quy mô minh họa độ lớn của này
việc phục vụ chi phí vấn đề (Facebook’s experience at fleet scale illustrates the magnitude of this serving cost problem).
Chiến tranh Câu chuyện 13.1: Sự suy luận thuế tại Facebook
Ngữ cảnh: Trong 2018, Kim Hazelwood và Facebook’s AI Cơ sở hạ tầng đội (đã) mô tả một sản-
xuất ML khối lượng công việc thứ mà (đã) chạm gần như mọi đối mặt-người dùng (user-facing) bề mặt: Tin tức Bảng tin (Feed) xếp hạng, Quảng cáo
xếp hạng, Tìm kiếm, hình ảnh sự hiểu (Lumos), khuôn mặt sự nhận dạng (Facer), sự bất thường sự phát hiện
(Sigma), được tự động hóa video việc tạo phụ đề (captioning), và một Dịch (Translate) hệ thống việc phục vụ xấp xỉ 4.5 tỷ được dịch
bài đăng (post) các lần hiển thị (impressions) mỗi ngày qua nhiều hơn hai nghìn ngôn ngữ các cặp (Hazelwood et
al. 2018) (In 2018, Kim Hazelwood and Facebook’s AI Infrastructure team described a production ML workload that touched nearly every user-facing surface: News Feed ranking, Ads ranking, Search, image understanding (Lumos), face recognition (Facer), anomaly detection (Sigma), automated video captioning, and a Translate system serving roughly 4.5 billion translated post impressions per day across more than two thousand language pairs (Hazelwood et al. 2018)).

716
13.2 Việc phục vụ Tải, Độ trễ, và Kiến trúc
Thất bại chế độ: Đắt tiền phần của ML (đã) di chuyển vào việc phục vụ (The expensive part of ML had moved into serving). Sự suy luận (đã) chạy trên bậc
của hàng chục (tens) của các nghìn tỷ (trillions) của các hoạt động mỗi ngày dưới nghiêm ngặt đuôi-độ trễ các mục tiêu, nơi trực tiếp yêu cầu
các sự đến (arrivals) (đã) ép buộc việc tạo lô và một một-giờ-cũ (one-hour-old) xếp hạng mô hình một cách có thể đo lường (đã) làm suy thoái Tin tức
Bảng tin chất lượng—việc ép buộc tích cực việc huấn luyện lại bên cạnh tích cực việc phục vụ (Inference ran on the order of tens of trillions of operations per day under strict tail-latency targets, where live request arrivals constrained batching and a one-hour-old ranking model measurably degraded News Feed quality—forcing aggressive retraining alongside aggressive serving).
Sự giải quyết (Resolution): Facebook (đã) xử lý (treated) sự suy luận như một hạng-nhất (first-class) dữ liệu-trung tâm cơ sở hạ tầng vấn đề,
việc đồng-thiết kế các mô hình, các máy gia tốc, bộ nhớ các hệ thống, và việc phục vụ các nền tảng cùng với nhau
thay vì việc xử lý việc phục vụ như một sự suy nghĩ lại (afterthought) tới huấn luyện (Facebook treated inference as a first-class data-center infrastructure problem, co-designing models, accelerators, memory systems, and serving platforms together rather than treating serving as an afterthought to training).
Các hệ thống bài học: Huấn luyện tạo ra mô hình; việc phục vụ trả định kỳ (recurring) hóa đơn (Training creates the model; serving pays the recurring bill). Tại hạm đội quy mô, một
mô hình kiến trúc (cái) thứ mà là rẻ để huấn luyện có thể vẫn là quá đắt, quá bị giới hạn-bởi bộ nhớ, hay quá
biến đổi trong đuôi độ trễ để phục vụ (At fleet scale, a model architecture that is cheap to train can still be too expensive, too memory-bound, or too variable in tail latency to serve).
Giống nhau việc phục vụ-kinh tế học (serving-economics) áp lực xuất hiện trong công khai API các mức giá (The same serving-economics pressure appears in public API prices). Để nắm bắt (grasp) tốc độ của này
chi phí sự sụp đổ, (hãy) kiểm tra log-thang đo (log-scale) giá quỹ đạo (trajectory) trong hình 13.2, thứ mà theo dõi mang tính đại diện công khai
API danh sách-giá (list-price) các ảnh chụp nhanh (snapshots) như một thị trường đại diện (To grasp the speed of this cost collapse, examine the log-scale price trajectory in figure 13.2, which tracks representative public API list-price snapshots as a market proxy). Nhà cung cấp các mức giá thay đổi một cách thường xuyên, do đó những
các điểm này nên được đọc như mang tính lịch sử nguồn gốc (provenance) cho xu hướng (trend) thay vì như hiện tại việc mua sắm (purchasing) hướng dẫn (OpenAI
2023a, 2024; OpenAI et al. 2023; OpenAI Nhà phát triển Cộng đồng 2024; Anthropic 2024; Google
Các nhà phát triển Blog 2024; DeepSeek 2024) (Vendor prices change frequently, so these points should be read as historical provenance for the trend rather than as current purchasing guidance (OpenAI 2023a, 2024; OpenAI et al. 2023; OpenAI Developer Community 2024; Anthropic 2024; Google Developers Blog 2024; DeepSeek 2024)). Mỗi bậc-của-độ lớn (order-of-magnitude) sự giảm sút thay đổi (cái) ứng dụng nào
là khả thi (feasible) (Each order-of-magnitude drop changes which applications are feasible).
2020
2021
2022
2023
2024
2025
Năm (Year)
$100
$10
$1
$0.10
$0.01
Giá mỗi 1M (triệu) Mã thông báo ($) (Price per 1M Tokens ($))
GPT-3 (Davinci)
GPT-3.5 Turbo
GPT-4 (Gốc (Original))
Claude 3 Opus
Claude 3 Haiku
GPT-4o
Gemini 1.5 Flash
GPT-4o-mini
DeepSeek-V3
Xu hướng: ~5.8× Rẻ hơn
Mỗi 18 Các tháng (Trend: ~5.8× Cheaper Every 18 Months)
Hình 13.2: Trí thông minh Sự giảm phát (Intelligence Deflation): Mang tính đại diện công khai API đầu vào-mã thông báo danh sách các mức giá mỗi 1M mã thông báo ($) theo thời gian (Log Thang đo).
Các mức giá là mô hình-phiên bản các ảnh chụp nhanh được thu thập từ công khai định giá (pricing) các trang của OpenAI, Anthropic, Google, và DeepSeek
giữa 2020 và 2025 và được dự định như một thị trường xu hướng chỉ báo (indicator), không (phải) một được kiểm soát hay hiện tại-giá sự so sánh (Prices are model-version snapshots collected from the public pricing pages of OpenAI, Anthropic, Google, and DeepSeek between 2020 and 2025 and are intended as a market trend indicator, not a controlled or current-price comparison). API
mã thông báo-việc xử lý các mức giá đã sụp đổ bởi nhiều các bậc của độ lớn, việc biến đổi kinh tế học của được tự động hóa AI
các luồng công việc (API token-processing prices have collapsed by multiple orders of magnitude, transforming the economics of automated AI workflows).
Hai các áp lực bây giờ đóng khung việc phục vụ vấn đề: đuôi độ trễ thứ mà bùng nổ một khi sự sử dụng vượt qua
xếp hàng đợi đầu gối, và mỗi-sự suy luận kinh tế học thứ mà rơi (fall) bởi các bậc của độ lớn khi tính hiệu quả cải thiện (Two pressures now frame the serving problem: tail latency that explodes once utilization passes the queueing knee, and per-inference economics that fall by orders of magnitude as efficiency improves).
Cùng với nhau chúng ép buộc một chính thức định nghĩa của việc phục vụ được xây dựng xung quanh độ trễ thay vì thông lượng (Together they force a formal definition of serving built around latency rather than throughput).
Định nghĩa 13.1: Mô hình việc phục vụ (Model serving)
Mô hình Việc phục vụ là hoạt động giai đoạn thứ mà cung cấp mô hình các dự đoán tới kết thúc-những người dùng hay hạ-
lưu các hệ thống dưới nghiêm ngặt độ trễ các sự ép buộc (Model Serving is the operational phase that provides model predictions to end-users or downstream systems under strict latency constraints).

13. Mô hình Việc phục vụ (Model Serving)
717
2
Dịch vụ Cấp độ Mục-
tiêu (Service Level Objective - SLO) so với Dịch vụ Cấp độ
Thỏa thuận (Service Level Agreement - SLA): Một SLO là
một nội bộ mục tiêu (cho ví dụ,
“p99 độ trễ dưới 50 ms”); một
SLA là một bên ngoài thuộc về hợp đồng (contractual)
cam kết với tài chính
các hình phạt cho sự vi phạm (An SLO is an internal target (for example, “p99 latency under 50 ms”); an SLA is an external contractual commitment with financial penalties for violation). Các SLO
được đặt chặt chẽ hơn (so với) các SLA để
cung cấp một an toàn lề (safety margin) (SLOs are set tighter than SLAs to provide a safety margin). Cho
ML việc phục vụ, cả hai mô hình độ-
chính xác và sự suy luận độ trễ
đóng góp vào các SLO, việc tạo ra
nhiều-chiều sự tối ưu-
hóa các mục tiêu nơi việc cải thiện
một chiều (cho ví dụ,
việc triển khai một lớn hơn mô hình cho
độ chính xác) có thể vi phạm (chiều) khác
(độ trễ) (For ML serving, both model accuracy and inference latency contribute to SLOs, creating multi-dimensional optimization targets where improving one dimension (for example, deploying a larger model for accuracy) can violate the other (latency)).
1. Tầm quan trọng (Significance): Nó đảo ngược thông lượng ưu tiên (𝜂hw) của huấn luyện thành một độ trễ sự ép buộc
(𝐿lat), việc yêu cầu một thuộc về kiến trúc ngăn xếp được thiết kế để tối thiểu hóa đuôi độ trễ (p99) của
cá nhân các sự suy luận (It inverts the throughput priority (𝜂hw) of training into a latency constraint (𝐿lat), requiring an architectural stack designed to minimize the tail latency (p99) of individual inferences).
2. Sự khác biệt (Distinction): Không giống như mô hình huấn luyện, thứ mà xử lý lớn, có thể đoán trước các lô của dữ liệu,
mô hình việc phục vụ phải xử lý ngẫu nhiên (stochastic) yêu cầu các mẫu và không thể đoán trước tải (Unlike model training, which processes large, predictable batches of data, model serving must handle stochastic request patterns and unpredictable load).
3. Phổ biến cạm bẫy: Một thường xuyên quan niệm sai lầm là rằng việc phục vụ là “chỉ (là) chuyển tiếp vượt qua.” (A frequent misconception is that serving is “just the forward pass.”) Trong
thực tế, nó là một phân tán hệ thống vấn đề: mô hình sự thực thi là chỉ một thành phần của
một ngăn xếp thứ mà bao gồm yêu cầu việc định tuyến, tải việc cân bằng, và dữ liệu sự biến đổi (In reality, it is a distributed system problem: the model execution is only one component of a stack that includes request routing, load balancing, and data transformation).
SLO2 xác định độ trễ mục tiêu thứ mà định hình mọi thuộc về kiến trúc quyết định trong việc phục vụ ngăn xếp,
bao gồm cách hệ thống lập ngân sách thời gian qua sự tiền xử lý, mô hình sự thực thi, sự hậu xử lý,
và sự vận chuyển (transport) (The SLO2 defines the latency target that shapes every architectural decision in the serving stack, including how the system budgets time across preprocessing, model execution, postprocessing, and transport). Việc phục vụ các hệ thống phải do đó thực thi một hoàn chỉnh sự suy luận đường ống dưới độ trễ
các sự ép buộc, không chỉ nơ-ron mạng sự tính toán (Serving systems must therefore execute a complete inference pipeline under latency constraints, not just the neural network computation). Một phổ biến quan niệm sai lầm là rằng “sự suy luận
thời gian” bằng “việc phục vụ thời gian,” nhưng nơ-ron mạng là chỉ một giai đoạn trong một dài hơn đường ống (A common misconception is that “inference time” equals “serving time,” but the neural network is only one stage in a longer pipeline). Hình 13.3
cho thấy rằng thô các đầu vào đi qua (pass through) sự tiền xử lý (truyền thống việc tính toán), nơ-ron mạng sự suy luận
(sâu học), và sự hậu xử lý (truyền thống việc tính toán) trước khi việc tạo ra cuối cùng các đầu ra (Figure 13.3 shows that raw inputs pass through preprocessing (traditional computing), neural network inference (deep learning), and postprocessing (traditional computing) before producing final outputs). Bất kỳ của
những các giai đoạn này có thể trở thành độ trễ nút thắt cổ chai (Any of these stages can become the latency bottleneck). Phần 13.4.1 định lượng một cách chính xác nơi thời gian đi (đến),
việc tiết lộ một phản trực giác (counterintuitive) kết quả về (giai đoạn) nào các giai đoạn thống trị (Section 13.4.1 quantifies exactly where time goes, revealing a counterintuitive result about which stages dominate).
Thô Dữ liệu (Raw Data)
Sự tiền-
xử lý (Pre-processing)
Nơ-ron
Mạng (Neural Network)
Thô
Đầu ra (Raw Output)
Sự hậu-
xử lý (Post-processing)
Cuối cùng Đầu ra (Final Output)
Sự tiền xử lý
Sâu Học
Sự hậu xử lý
Hình 13.3: Sự suy luận Đường ống (The Inference Pipeline): ML việc phục vụ các hệ thống biến đổi thô các đầu vào thành cuối cùng các đầu ra thông qua tuần tự các giai đoạn:
sự tiền xử lý, nơ-ron mạng sự tính toán, và sự hậu xử lý (ML serving systems transform raw inputs into final outputs through sequential stages: preprocessing, neural network computation, and postprocessing). Nơ-ron mạng đại diện chỉ một thành phần;
sự tiền xử lý và sự hậu xử lý dựa trên truyền thống việc tính toán và thường thống trị tổng độ trễ trong được tối ưu hóa các hệ thống (The neural network represents just one component; preprocessing and postprocessing rely on traditional computing and often dominate total latency in optimized systems).
Đường ống biến việc phục vụ thành một sự điều phối vấn đề: sự tiền xử lý, mô hình sự thực thi, sự hậu-
xử lý, và sự vận chuyển tất cả cạnh tranh cho giống nhau độ trễ ngân sách (The pipeline turns serving into an orchestration problem: preprocessing, model execution, postprocessing, and transport all compete for the same latency budget). Trước khi việc tối ưu hóa bất kỳ một giai đoạn (nào),
hệ thống phải quyết định liệu các dự đoán được tính toán trước của thời gian hay theo yêu cầu (on demand) (Before optimizing any one stage, the system must decide whether predictions are computed ahead of time or on demand).
13.2.1 Tĩnh so với động sự suy luận (Static vs. dynamic inference)
Trước khi việc tối ưu hóa cách để giảm sự suy luận độ trễ, hệ thống phải quyết định khi nào các dự đoán được
tính toán (Before optimizing how to reduce inference latency, the system must decide when predictions are computed). Đầu tiên thuộc về kiến trúc quyết định trong bất kỳ việc phục vụ hệ thống (nào) là liệu các dự đoán xảy ra
trước hay trong suốt người dùng các yêu cầu (Google 2024b) (The first architectural decision in any serving system is whether predictions happen before or during user requests (Google 2024b)). Này sự lựa chọn định hình hệ thống thiết kế, chi phí cấu trúc,
và khả năng các ranh giới (This choice shapes system design, cost structure, and capability boundaries).
13.2.1.1 Tĩnh sự suy luận (Static inference)
Tĩnh sự suy luận (cũng được gọi là ngoại tuyến hay lô sự suy luận) tính toán trước các dự đoán cho được lường trước các đầu vào
và lưu trữ chúng cho sự truy xuất (Static inference (also called offline or batch inference) precomputes predictions for anticipated inputs and stores them for retrieval). Hãy xem xét một sự giới thiệu hệ thống thứ mà tạo ra các dự đoán cho tất cả
người dùng-mặt hàng các cặp hàng đêm (Consider a recommendation system that generates predictions for all user-item pairs nightly). Khi một người dùng yêu cầu các sự giới thiệu, hệ thống truy xuất được tính toán trước
các kết quả từ một tra cứu (lookup) bảng thay vì việc chạy sự suy luận (When a user requests recommendations, the system retrieves precomputed results from a lookup table rather than running inference). Này cách tiếp cận di chuyển tính toán ra khỏi
yêu cầu con đường, kích hoạt ngoại tuyến chất lượng các sự kiểm tra, và có thể giảm việc phục vụ các chi phí cho có thể đoán trước các đầu vào (This approach moves compute out of the request path, enables offline quality checks, and can reduce serving costs for predictable inputs).
Tuy nhiên, tĩnh sự suy luận cần hoặc một dự phòng trực tuyến con đường hoặc một được làm mới lô sự tính toán khi
các yêu cầu bao gồm không lường trước các đầu vào hay mới được cập nhật các mô hình (However, static inference needs either a fallback online path or a refreshed batch computation when requests include unanticipated inputs or newly updated models).
13.2.1.2 Động sự suy luận (Dynamic inference)
Động sự suy luận (cũng được gọi là trực tuyến hay thời gian-thực sự suy luận) tính toán các dự đoán theo yêu cầu khi
các yêu cầu đến (Dynamic inference (also called online or real-time inference) computes predictions on demand when requests arrive). Này xử lý bất kỳ đầu vào (nào), bao gồm hiếm biên các trường hợp và mới mẻ (novel) các sự kết hợp, và
ngay lập tức phản ánh mô hình các bản cập nhật (This handles any input, including rare edge cases and novel combinations, and immediately reflects model updates). Chi phí là nghiêm ngặt độ trễ các yêu cầu thứ mà ép buộc mô hình
tính phức tạp và đòi hỏi mạnh mẽ việc giám sát cơ sở hạ tầng (The cost is strict latency requirements that constrain model complexity and demand robust monitoring infrastructure).

718
13.2 Việc phục vụ Tải, Độ trễ, và Kiến trúc (Serving Load, Latency, and Architecture)
Cho của chúng ta ResNet-50 hình ảnh bộ phân loại, hãy xem xét hai sự triển khai các kịch bản (For our ResNet-50 image classifier, consider two deployment scenarios). Một tĩnh cách tiếp cận phù hợp (suits) một
bức ảnh (photo) sự tổ chức (organization) ứng dụng thứ mà phân loại trước tất cả các hình ảnh trong một người dùng’s thư viện qua đêm (A static approach suits a photo organization app that preclassifies all images in a user’s library overnight). Với 10,000 các bức ảnh
và 5 ms sự suy luận mỗi (cái), lô việc xử lý tốn ~50 s tổng cộng, và những người dùng thấy ngay lập tức sự phân loại khi
việc duyệt (browsing) (With 10,000 photos and 5 ms inference each, batch processing takes ~50 s total, and users see instant classification when browsing). Một động cách tiếp cận phù hợp một nội dung sự điều độ (moderation) API thứ mà phải phân loại được tải lên-bởi-người dùng (user-uploaded)
các hình ảnh trong thời gian-thực, với mỗi hình ảnh việc yêu cầu đầy đủ sự tiền xử lý→sự suy luận→sự hậu xử lý
đường ống và một 100 ms độ trễ ngân sách (A dynamic approach suits a content moderation API that must classify user-uploaded images in real-time, with each image requiring the full preprocessing→inference→postprocessing pipeline and a 100 ms latency budget). Hầu hết sản xuất hình ảnh sự phân loại các hệ thống sử dụng một lai
cách tiếp cận: thường xuyên được yêu cầu các hình ảnh (phổ biến các sản phẩm, được biết các meme) được phân loại trước và
được lưu bộ nhớ đệm, trong khi mới mẻ (novel) các lượt tải lên kích hoạt động sự suy luận (Most production image classification systems use a hybrid approach: frequently requested images (popular products, known memes) are preclassified and cached, while novel uploads trigger dynamic inference).
Sự lựa chọn giữa tĩnh và động việc phục vụ có trực tiếp thuộc về kinh tế các hệ quả (The choice between static and dynamic serving has direct economic implications). Chặt chẽ hơn độ trễ
các yêu cầu một cách trực tiếp dịch thành cao hơn cơ sở hạ tầng các chi phí, và việc định lượng chi phí của độ trễ
trong đô la các điều khoản (terms) tiết lộ bao nhiêu cơ sở hạ tầng phí bảo hiểm (premium) mỗi mili giây của độ trễ sự giảm thiểu
đòi hỏi (Stricter latency requirements directly translate into higher infrastructure costs, and quantifying the cost of latency in dollar terms reveals how much infrastructure premium each millisecond of latency reduction demands).
Khăn ăn (Napkin) Toán học 13.1: Chi phí của độ trễ (The cost of latency)
Độ trễ các sự ép buộc một cách trực tiếp ra lệnh cơ sở hạ tầng các chi phí (Latency constraints directly dictate infrastructure costs). Hãy xem xét một GPU máy chủ việc thuê cho
$4/giờ.
Kịch bản A (thấp độ trễ): Lô kích thước 1.
• Độ trễ: 5 ms.
• Thông lượng: 200 req/s.
• Chi phí mỗi triệu các truy vấn: $5.56.
Kịch bản B (cao thông lượng): Lô kích thước 8.
• Độ trễ: 10 ms (được nhân đôi do việc tạo lô chi phí hoạt động) (Latency: 10 ms (doubled due to batching overhead)).
• Thông lượng: 800 req/s (được nhân bốn do song song tính hiệu quả) (Throughput: 800 req/s (quadrupled due to parallel efficiency)).
• Chi phí mỗi triệu các truy vấn: $1.39.
Các hệ thống sự thấu hiểu (insight): Việc giảm độ trễ từ 10 ms tới 5 ms làm tăng phần cứng hóa đơn bởi 300
phần trăm (Systems insight: Reducing latency from 10 ms to 5 ms increases the hardware bill by 300 percent). Các kỹ sư phải định lượng liệu đó sự tăng tốc (có) tạo ra đủ kinh doanh giá trị để
biện minh 4× chi phí sự gia tăng (hay không) (Engineers must quantify whether that speedup generates enough business value to justify the 4× cost increase).
Hầu hết sản xuất các hệ thống kết hợp cả hai các cách tiếp cận (Most production systems combine both approaches). Phổ biến các truy vấn chạm một bộ nhớ đệm được điền
bởi lô sự suy luận trong khi không phổ biến các yêu cầu kích hoạt động sự tính toán (Common queries hit a cache populated by batch inference while uncommon requests trigger dynamic computation). Việc hiểu này phổ (spec-trum)
quan trọng bởi vì nó xác định (những) nào tiếp theo sự tối ưu hóa các chiến lược áp dụng (Understanding this spectrum matters because it determines which subsequent optimization strategies apply). Tĩnh sự suy luận
tối ưu hóa cho thông lượng trong suốt lô sự tính toán và lưu trữ tính hiệu quả cho việc phục vụ (Static inference optimizes for throughput during batch computation and storage efficiency for serving). Động
sự suy luận tối ưu hóa cho mỗi-yêu cầu độ trễ dưới đồng thời tải, thứ mà yêu cầu việc hiểu
nơi thời gian đi (đến) bên trong mỗi yêu cầu (Dynamic inference optimizes for per-request latency under concurrent load, which requires understanding where time goes within each request).
Tĩnh-so với-động quyết định là đầu tiên của một vài thuộc về kiến trúc các sự lựa chọn thứ mà định hình việc phục vụ
hệ thống thiết kế (The static-vs.-dynamic decision is the first of several architectural choices that shape serving system design). Không kém phần quan trọng là nơi mô hình thực thi, bởi vì sự triển khai ngữ cảnh ép buộc
mọi tiếp theo sự tối ưu hóa (Equally important is where the model executes, since deployment context constrains every subsequent optimization).
Tất cả của chi phí sự phân tích bên trên giả định một truyền thống chuyển tiếp vượt qua: một cố định sự tính toán đồ thị thứ mà
thực thi một lần mỗi yêu cầu và tạo ra một kết quả (All of the cost analysis above assumes a traditional forward pass: a fixed computation graph that executes once per request and produces a result). Một mới lớp của các mô hình lật ngược (upends) đó giả định
bằng cách một cách có chủ ý việc làm tăng lượng của sự tính toán được dành mỗi truy vấn, việc đánh đổi độ trễ cho câu trả lời
chất lượng, và việc phục vụ chi phí các hệ quả là đáng kể (A new class of models upends that assumption by deliberately increasing the amount of computation spent per query, trading latency for answer quality, and the serving cost implications are substantial).
Các hệ thống Góc nhìn 13.1: Việc nhìn về phía trước (Looking ahead): Một cách có chủ ý việc dành nhiều hơn tính toán mỗi
truy vấn (Deliberately spending more compute per query)
Truyền thống việc phục vụ tối ưu hóa cho việc tối thiểu hóa độ trễ (𝐿lat → 0). Vài sự suy luận-thời gian-tính toán (inference-time-compute)
các hệ thống một cách có chủ ý dành nhiều hơn tính toán các chu kỳ để cải thiện câu trả lời chất lượng (Some inference-time-compute systems deliberately spend more compute cycles to improve answer quality). Cá nhân mã thông báo
việc tạo (generation) duy trì bị giới hạn-bởi bộ nhớ-băng thông, nhưng những các hệ thống này có thể tạo ra xa nhiều hơn
các mã thông báo mỗi yêu cầu, bao gồm trung gian lập luận hay tìm kiếm các mã thông báo, việc làm tăng tổng

13. Mô hình Việc phục vụ (Model Serving)
719
tính toán và năng lượng được dành mỗi truy vấn (increasing the total compute and energy spent per query). Tổng hợp hiệu ứng có thể mang giống như-huấn luyện tính toán
các ngân sách vào việc phục vụ giai đoạn, mặc dù mỗi mã thông báo là vẫn được chi phối bởi bộ nhớ bức tường (The aggregate effect can bring training-like compute budgets into the serving phase, even though each token is still governed by the memory wall).
Liệu một hệ thống dành một chuyển tiếp vượt qua hay nhiều lập luận các bước mỗi truy vấn (hay không), sự triển khai
ngữ cảnh vẫn xác định khả thi độ trễ và chi phí vỏ bọc (Whether a system spends one forward pass or many reasoning steps per query, deployment context still determines the feasible latency and cost envelope). Đó ngữ cảnh là tiếp theo biến (That context is the next variable).
13.2.2 Phổ của việc phục vụ các kiến trúc (The spectrum of serving architectures)
Mặc dù “việc phục vụ” thường ngụ ý một được kết nối mạng máy chủ việc xử lý API các yêu cầu, thuộc về kiến trúc
mẫu biến đổi một cách quyết liệt bởi sự triển khai môi trường (Although “serving” often implies a networked server processing API requests, the architectural pattern varies drastically by deployment environment). Phần 2.1 đã giới thiệu bốn sự triển khai
các mô hình mẫu (Đám mây, Biên, Di động, và TinyML) và vật lý các sự ép buộc (ánh sáng rào cản,
sức mạnh bức tường, và bộ nhớ bức tường) thứ mà làm (cho) nảy sinh tới chúng (Section 2.1 introduced the four deployment paradigms (Cloud, Edge, Mobile, and TinyML) and the physical constraints (the light barrier, the power wall, and the memory wall) that give rise to them). Những các sự ép buộc đó không biến mất tại
việc phục vụ thời gian; chúng tăng cường (intensify), bởi vì việc phục vụ thêm độ trễ các SLO và chi phí áp lực trên đỉnh của
phần cứng các giới hạn thứ mà huấn luyện có thể hấp thụ thông qua sự kiên nhẫn (Those constraints do not disappear at serving time; they intensify, because serving adds latency SLOs and cost pressure on top of the hardware limits that training could absorb through patience). Giống nhau mô hình có thể yêu cầu một cách triệt để
khác biệt việc phục vụ các chiến lược tùy thuộc trên nơi nó thực thi (The same model may require radically different serving strategies depending on where it executes).
13.2.2.1 Được kết nối mạng việc phục vụ (đám mây/dữ liệu trung tâm) (Networked serving (cloud/data center))
Trong được kết nối mạng việc phục vụ, mô hình chạy như một độc lập (standalone) dịch vụ (vi dịch vụ (microservice)), sự triển khai
mô hình mẫu phần 2.5 (đã) mô tả đặc điểm (characterized) như việc đánh đổi độ trễ cho lớn hơn được gộp (pooled) tính toán (In networked serving, the model runs as a standalone service (microservice), the deployment paradigm section 2.5 characterized as trading latency for larger pooled compute). Chính
giao diện là mạng thông qua yêu cầu các giao thức như HTTP hay gRPC, do đó việc ràng buộc các sự ép buộc
là mạng băng thông và sự tuần tự hóa chi phí trước khi yêu cầu thậm chí chạm tới máy gia tốc (The primary interface is the network through request protocols such as HTTP or gRPC, so the binding constraints are network bandwidth and serialization cost before the request even reaches the accelerator). Dữ liệu-
trung tâm phần cứng như NVIDIA các GPU (V100, A100, H100), Google Tensor Xử lý Các đơn vị (Tensor Processing Units - TPUs),
và AWS Inferentia hỗ trợ cao-thông lượng việc tạo lô và tính đồng thời, nhưng lạnh sự khởi động có thể vẫn
kéo dài (stretch) từ các giây tới các phút bởi vì vùng chứa (container) sự khởi động, mô hình việc tải, và sự khởi động (warmup) ngồi bên ngoài
ổn định-trạng thái (steady-state) sự suy luận con đường (Data-center hardware such as NVIDIA GPUs (V100, A100, H100), Google Tensor Processing Units (TPUs), and AWS Inferentia supports high-throughput batching and concurrency, but cold start can still stretch from seconds to minutes because container startup, model loading, and warmup sit outside the steady-state inference path).
13.2.2.2 Được nhúng-ứng dụng việc phục vụ (di động/biên) (Application-embedded serving (mobile/edge))
Trong được nhúng-ứng dụng việc phục vụ, mô hình chạy bên trong người dùng ứng dụng tiến trình (cho ví dụ,
một điện thoại thông minh ứng dụng việc sử dụng CoreML hay TensorFlow Lite), được nhúng mô hình mẫu phần 2.6 và
phần 2.7 (đã) phân tích cho của nó độ trễ, quyền riêng tư, và ngoại tuyến các lợi thế (In application-embedded serving, the model runs within the user application process (for example, a smartphone app using CoreML or TensorFlow Lite), the embedded paradigm section 2.6 and section 2.7 analyzed for its latency, privacy, and offline advantages). Có (là) không “máy chủ.” Giao diện
là một hàm lệnh gọi (call), do đó sự tối ưu hóa tập trung trên năng lượng và tính đáp ứng (responsiveness) (SingleStream)
thay vì được chia sẻ-máy chủ thông lượng (The interface is a function call, so optimization focuses on energy and responsiveness (SingleStream) rather than shared-server throughput).
Trung tâm lợi thế là Không-Bản sao (Zero-Copy) Sự suy luận: khi dữ liệu di chuyển thông qua một hệ thống, mỗi bản sao
tiêu thụ CPU các chu kỳ và bộ nhớ băng thông (The central advantage is Zero-Copy Inference: when data moves through a system, each copy consumes CPU cycles and memory bandwidth). Trong đám mây việc phục vụ, một camera khung hình (frame) có thể bị sao chép
bốn lần: từ mạng bộ đệm tới ứng dụng bộ nhớ, sau đó tới một sự tiền xử lý bộ đệm, sau đó tới
có thể truy cập-GPU bộ nhớ, và cuối cùng tới GPU VRAM (In cloud serving, a camera frame might be copied four times: from network buffer to application memory, then to a preprocessing buffer, then to GPU-accessible memory, and finally to GPU VRAM). Di động các NPU có thể loại bỏ hầu hết của những
các bản sao này bằng cách việc chia sẻ bộ nhớ một cách trực tiếp với camera phần cứng (Mobile NPUs can eliminate most of these copies by sharing memory directly with the camera hardware). Camera viết các pixel vào một
bộ đệm thứ mà NPU đọc một cách trực tiếp, việc tránh CPU hoàn toàn (The camera writes pixels into a buffer that the NPU reads directly, avoiding the CPU entirely). Này làm giảm cả hai độ trễ (không sao chép
các hoạt động) và năng lượng (bộ nhớ các bản sao tiêu thụ đáng kể sức mạnh) (This reduces both latency (no copy operations) and energy (memory copies consume significant power)). Cơ chế yêu cầu
phần cứng sự hỗ trợ: camera, CPU, và NPU phải chia sẻ một thống nhất bộ nhớ kiến trúc, như trong
di động hệ thống trên chip (system on chip - SoC) các thiết kế như Apple’s M-series và Qualcomm Snapdragon (The mechanism requires hardware support: the camera, CPU, and NPU must share a unified memory architecture, as in mobile system on chip (SoC) designs such as Apple’s M-series and Qualcomm Snapdragon).
Điển hình phần cứng bao gồm di động các NPU (Apple Neural Engine, Qualcomm Hexagon) và được nhúng
các GPU (Jetson) (Typical hardware includes mobile NPUs (Apple Neural Engine, Qualcomm Hexagon) and embedded GPUs (Jetson)). Lạnh sự khởi động thường rơi (vào khoảng) trong các mili giây bởi vì mô hình là đã trong
ứng dụng bộ nhớ, mặc dù đầu tiên sự suy luận có thể kích hoạt vừa-kịp-thời gian (just-in-time - JIT) sự biên dịch (100–500 ms) (Cold start usually falls in milliseconds because the model is already in app memory, though first inference may trigger just-in-time (JIT) compilation (100–500 ms)).
Được duy trì sức mạnh ngân sách là 1–5 W, với thuộc về nhiệt sự điều chỉnh sau kéo dài (prolonged) sự suy luận (The sustained power budget is 1–5 W, with thermal throttling after prolonged inference).
13.2.2.3 Trần-kim loại (Bare-metal) việc phục vụ (TinyML)
Trong TinyML việc phục vụ, mô hình được biên dịch vào phần sụn (firmware) của một vi điều khiển (microcontroller), cực đoan kết thúc của
sự triển khai phổ phần 2.8 (đã) giới thiệu như phổ biến sự cảm biến tại vi watt (microwatt) sức mạnh các ngân sách (In TinyML serving, the model is compiled into the firmware of a microcontroller, the extreme end of the deployment spectrum section 2.8 introduced as ubiquitous sensing at microwatt power budgets).
Có (là) không điều hành hệ thống hay động bộ nhớ bộ cấp phát (allocator) (There is no operating system or dynamic memory allocator). “Việc phục vụ” là một chặt chẽ (tight) vòng lặp việc đọc
các cảm biến và việc gọi (invoking) trình thông dịch (interpreter) (“Serving” is a tight loop reading sensors and invoking the interpreter). Sự tối ưu hóa tập trung trên tĩnh bộ nhớ sự sử dụng (việc khớp trong SRAM)
bởi vì tất cả bộ nhớ được cấp phát trước trong Tensor Đấu trường (Arena) và động việc tạo lô là không thể (Optimization focuses on static memory usage (fitting in SRAM) because all memory is preallocated in the Tensor Arena and dynamic batching is impossible). Điển hình
phần cứng bao gồm ARM Cortex-M series, ESP32, và được chuyên môn hóa TinyML các máy gia tốc (Typical hardware includes ARM Cortex-M series, ESP32, and specialized TinyML accelerators). Lạnh sự khởi động
rơi (vào khoảng) trong các micro giây bởi vì mô hình các trọng số sống trong flash và tensor đấu trường được cấp phát trước, trong khi
sức mạnh ngân sách nằm trong khoảng từ các vi watt tới các mili watt cho pin hoạt động qua các tháng hay các năm (Cold start falls in microseconds because model weights live in flash and the tensor arena is preallocated, while the power budget ranges from microwatts to milliwatts for battery operation over months or years).
Bảng 13.1 tóm tắt cách những sự triển khai các ngữ cảnh này định hình việc phục vụ hệ thống thiết kế (Table 13.1 summarizes how these deployment contexts shape serving system design).

720
13.2 Việc phục vụ Tải, Độ trễ, và Kiến trúc
Để làm (cho) những thuộc về kiến trúc các sự khác biệt này (trở nên) cụ thể, (hãy) xem xét cách một đơn mô hình phải thích nghi với mỗi
sự triển khai ngữ cảnh (To make these architectural differences concrete, consider how a single model must adapt to each deployment context).
Giống nhau ResNet-50 kiến trúc yêu cầu một cách quyết liệt (dramatically) khác biệt việc phục vụ các chiến lược qua sự triển-
khai các ngữ cảnh (The same ResNet-50 architecture requires dramatically different serving strategies across deployment contexts). Bảng 13.2 so sánh ba các bậc (tiers) cạnh nhau (side by side): đám mây việc phục vụ chạy đầy đủ
FP16 động cơ tại mili giây độ trễ trên một dữ liệu trung tâm GPU; di động việc phục vụ nén tới INT8 và
phân phối (dispatches) tới một NPU tại một phần nhỏ (fraction) của năng lượng; TinyML không thể chạy ResNet-50 hoàn toàn (at all) và thay vào đó
phục vụ một được thu nhỏ (downsized) MobileNetV2 trong các kilobyte của SRAM (Table 13.2 compares the three tiers side by side: cloud serving runs the full FP16 engine at millisecond latency on a data center GPU; mobile serving compresses to INT8 and dispatches to an NPU at a fraction of the energy; TinyML cannot run ResNet-50 at all and instead serves a downsized MobileNetV2 in kilobytes of SRAM).
Bảng 13.1: Việc phục vụ Kiến trúc Phổ (Serving Architecture Spectrum): Sự triển khai mô hình mẫu được chọn trong phần 2.9 định hình mọi khía cạnh của việc phục vụ
hệ thống thiết kế (The deployment paradigm selected in section 2.9 shapes every aspect of serving system design). Đám mây các hệ thống tối ưu hóa cho thông lượng với động việc tạo lô; di động các hệ thống tối ưu hóa cho năng lượng với cố định
lô-1; TinyML các hệ thống hoạt động dưới cực đoan bộ nhớ và sức mạnh các sự ép buộc với không động sự cấp phát (nào) (Cloud systems optimize for throughput with dynamic batching; mobile systems optimize for energy with fixed batch-1; TinyML systems operate under extreme memory and power constraints with no dynamic allocation). Vật lý các bức tường
(ánh sáng, sức mạnh, bộ nhớ) thứ mà (đã) tạo ra những các mô hình mẫu này bây giờ ra lệnh việc phục vụ các sự ép buộc mỗi (cái) phải thỏa mãn (The physical walls (light, power, memory) that created these paradigms now dictate the serving constraints each must satisfy).
Đặc điểm (Characteristic)
Đám mây/Dữ liệu trung tâm (Cloud/Data center)
Di động/Biên (Mobile/Edge)
TinyML
Độ trễ Mục tiêu (Latency Target)
10–100 ms
20–50 ms
1–100 ms
Lô Kích thước (Batch Size)
1–128 (động)
1 (cố định)
1 (cố định)
Bộ nhớ (Memory)
16–80 GB VRAM
2–8 GB được chia sẻ (shared)
256 KB–2 MB SRAM
Sức mạnh (Power)
300–700 W
1–10 W
1–100 mW
Cập nhật Cơ chế (Update Mechanism)
Vùng chứa (Container) sự triển khai (deploy)
Ứng dụng cửa hàng cập nhật
Phần sụn (Firmware) qua-không-trung (over-the-air - OTA)
Thất bại Chế độ (Failure Mode)
Thử lại (Retry)/chuyển đổi dự phòng (failover)
Tinh tế sự suy thoái (Graceful degradation)
Im lặng hay đặt lại (Silent or reset)
Việc giám sát (Monitoring)
Đầy đủ đo từ xa (telemetry)
Giới hạn phân tích (analytics)
Nhịp tim (Heartbeat) chỉ (only)
Các hệ thống Góc nhìn 13.2: ResNet-50 qua việc phục vụ phổ (ResNet-50 across the serving spectrum)
Các hệ thống sự thấu hiểu: “Giống nhau mô hình” tuyên bố là gây hiểu lầm: mỗi hàng của bảng 13.2 là một khác biệt
sự tối ưu hóa, và thường một khác biệt kiến trúc hoàn toàn (Systems insight: The “same model” claim is misleading: each row of table 13.2 is a different optimization, and often a different architecture entirely). Đám mây và di động các bậc chia sẻ
ResNet-50 đồ thị nhưng phân kỳ trong độ chính xác, thời gian chạy, và bộ nhớ bởi ba tới bốn các bậc
của độ lớn; TinyML bậc không thể chạy ResNet-50 hoàn toàn và thay thế (substitutes) một kiến trúc
được thiết kế cho các sự ép buộc từ sự khởi đầu (The cloud and mobile tiers share the ResNet-50 graph but diverge in precision, runtime, and memory by three to four orders of magnitude; the TinyML tier cannot run ResNet-50 at all and substitutes an architecture designed for the constraints from the start). Việc xử lý những (cái) này như một mô hình giấu công việc thứ mà
làm (cho) mỗi sự triển khai (trở nên) khả thi (Treating these as one model hides the work that makes each deployment possible).
Bảng 13.2: ResNet-50 Qua Việc phục vụ Phổ (ResNet-50 Across the Serving Spectrum): Cạnh-nhau sự so sánh của đám mây, di động, và TinyML việc phục vụ cho
giống nhau mục tiêu kiến trúc, việc hiển thị cách mô hình định dạng, độ trễ, thông lượng, bộ nhớ dấu chân (footprint), và năng lượng ngân sách dịch chuyển bởi
ba tới bốn các bậc của độ lớn qua sự triển khai các ngữ cảnh (Side-by-side comparison of cloud, mobile, and TinyML serving for the same target architecture, showing how the model format, latency, throughput, memory footprint, and energy budget shift by three to four orders of magnitude across deployment contexts).
Chiều (Dimension)
Đám mây
Di động
TinyML
Mô hình định dạng (Model format)
TensorRT FP16 động cơ (51.2
MB)
TensorFlow Lite INT8 (25.6
MB)
Không khả thi (25.6 MB);
thay thế (alternative): MobileNetV2-0.35
INT8 (3.5 MB)
Sự suy luận (lô-1) (Inference (batch-1))
1.4 ms (lô-16: 14 ms)
12 ms (NPU), 45 ms (CPU)
120 ms
Thông lượng (Throughput)
1,143 img/s (được tạo lô)
~80 img/s (đơn-luồng (single-stream))
~8 img/s
Bộ nhớ
2 GB VRAM (lô-32)
150 MB đỉnh (được chia sẻ với ứng dụng)
320 KB đấu trường (khớp trong 512 KB
SRAM)
Năng lượng/sự suy luận
—
0.8 mJ (NPU), 4.2 mJ (CPU)
12 mJ
13.2.3 Tải bộ cân bằng lớp (The load balancer layer)
Khi lưu lượng truy cập vượt quá (những) gì một đơn máy móc có thể xử lý, đám mây và dữ liệu trung tâm các sự triển khai thứ mà chạy
nhiều các bản sao của giống nhau mô hình yêu cầu một bổ sung cơ sở hạ tầng lớp: tải bộ cân bằng (When traffic exceeds what a single machine can handle, cloud and data center deployments that run multiple replicas of the same model require an additional infrastructure layer: the load balancer).
Sản xuất việc phục vụ các hệ thống đặt tải các bộ cân bằng giữa các máy khách và mô hình các máy chủ, việc cung cấp ba
thiết yếu các chức năng cho việc phục vụ cơ sở hạ tầng (Production serving systems place load balancers between clients and model servers, providing three essential functions for serving infrastructure).
Yêu cầu sự phân phối, đầu tiên chức năng, định tuyến đến (incoming) các yêu cầu tới có sẵn mô hình các bản sao bằng cách sử dụng
các thuật toán như round-robin hay ít nhất-các kết nối (least-connections) (Request distribution, the first function, routes incoming requests to available model replicas using algorithms like round-robin or least-connections). Cho nhạy cảm-độ trễ ML việc phục vụ, các thuật toán thứ mà

13. Mô hình Việc phục vụ (Model Serving)
721
Một ồn ào hàng xóm làm xáo trộn (perturbs) mọi
khối lượng công việc việc chia sẻ nút (One noisy neighbor perturbs every workload sharing the node).
định tuyến tránh xa chậm hay quá tải các bản sao cải thiện đuôi độ trễ (route away from slow or overloaded replicas improve tail latency). (Chức năng thứ) hai, sức khỏe việc giám sát,
một cách liên tục xác minh rằng các bản sao là sẵn sàng để phục vụ, việc định tuyến lưu lượng truy cập tránh xa không khỏe mạnh các phiên bản (The second, health monitoring, continuously verifies that replicas are ready to serve, routing traffic away from unhealthy instances).
Cho ML các hệ thống, sức khỏe các sự kiểm tra phải xác minh cả hai tiến trình tính sống còn (liveness) và mô hình sự sẵn sàng, việc xác nhận
rằng các trọng số được tải và sự khởi động là hoàn tất (For ML systems, health checks must verify both process liveness and model readiness, confirming that weights are loaded and warmup is complete). (Chức năng thứ) ba, sự triển khai sự hỗ trợ, kích hoạt an toàn mô hình
các bản cập nhật bằng cách một cách dần dần việc dịch chuyển lưu lượng truy cập giữa các phiên bản thay vì việc xử lý sự phát hành như một tất cả-tại-một-lúc
công tắc (The third, deployment support, enables safe model updates by gradually shifting traffic between versions instead of treating release as an all-at-once switch). Phần 14.5.1.1 muộn hơn biến đó cơ bản lưu lượng truy cập-sự dịch chuyển (traffic-shift) ý tưởng thành đầy đủ sự triển khai và sự xác nhận
các chiến lược (Section 14.5.1.1 later turns that basic traffic-shift idea into full deployment and validation strategies).
Cho đơn-máy móc việc phục vụ với nhiều mô hình các phiên bản (instances), như việc chạy một vài Mở Nơ-ron
Mạng Trao đổi (Open Neural Network Exchange - ONNX) Thời gian chạy các phiên (sessions), bộ khung và hệ điều hành xử lý yêu cầu
việc xếp hàng đợi (For single-machine serving with multiple model instances, such as running several Open Neural Network Exchange (ONNX) Runtime sessions, the framework and operating system handle request queuing). Đầy đủ tính phức tạp của tải việc cân bằng trở nên cần thiết khi việc mở rộng tới phân tán
sự suy luận các hệ thống, nơi nhiều các máy móc phục vụ giống nhau mô hình (The full complexity of load balancing becomes necessary when scaling to distributed inference systems, where multiple machines serve the same model). Sự triển khai các chi tiết của
yêu cầu sự phân phối các thuật toán và đa-bản sao các kiến trúc thuộc về (đó) phân tán ngữ cảnh (The implementation details of request distribution algorithms and multi-replica architectures belong to that distributed context).
Khi công suất sự lập kế hoạch xem xét “máy chủ” trong này đơn-máy móc việc phục vụ sự phân tích, nó có nghĩa
máy móc’s mô hình việc phục vụ công suất (When capacity planning considers “the server” in this single-machine serving analysis, it means the machine’s model serving capacity). Xếp hàng đợi các động lực được phân tích trong phần 13.5 áp dụng
để hiểu đơn-máy móc hành vi và việc xác định khi nào việc mở rộng tới nhiều các máy móc
trở nên cần thiết (The queuing dynamics analyzed in section 13.5 apply to understanding single-machine behavior and determining when scaling to multiple machines becomes necessary).
Trong khi tải các bộ cân bằng phân phối các yêu cầu qua các bản sao, việc đạt được có thể đoán trước độ trễ cũng yêu cầu
việc kiểm soát (những) gì xảy ra bên trong mỗi máy móc (While load balancers distribute requests across replicas, achieving predictable latency also requires controlling what happens within each machine). Hệ điều hành môi trường giới thiệu của riêng nó
các nguồn của tính biến đổi (The operating system environment introduces its own sources of variability).
13.2.4 Có tính quyết định (Deterministic) độ trễ và tài nguyên sự cô lập (Deterministic latency and resource isolation)
Một sự suy luận máy chủ không hoạt động trong sự cô lập (An inference server does not operate in isolation). Trên một đơn máy móc, hệ điều hành quản lý
nhiều cạnh tranh các tiến trình (việc ghi nhật ký các tác nhân, việc giám sát các công cụ, và hệ thống các ngắt (interrupts)) thứ mà có thể
một cách gián đoạn (intermittently) đánh cắp CPU các chu kỳ từ sự suy luận đường ống (On a single machine, the operating system manages multiple competing processes (logging agents, monitoring tools, and system interrupts) that can intermittently steal CPU cycles from the inference pipeline). Những “ồn ào những người hàng xóm” này là một chính
nguồn của độ trễ sự bồn chồn (jitter), nơi thời gian được yêu cầu để xử lý giống hệt các yêu cầu biến đổi một cách đáng kể,
việc gây ra thứ 99 phân vị (99th percentile - P99) độ trễ bùng nổ thậm chí khi phần cứng (đang) bị sử dụng dưới mức (underused) (These “noisy neighbors” are a primary source of latency jitter, where the time required to process identical requests varies significantly, causing the 99th percentile (P99) latency to spike even when the hardware is underused). Các
đuôi độ trễ sự bùng nổ từ hình 13.1 minh họa giống nhau sự bùng nổ, nhưng ở đây trình kích hoạt (trigger) là tài nguyên
sự tranh chấp thay vì việc xếp hàng đợi (The tail latency explosion from figure 13.1 illustrates the same spike, but here the trigger is resource contention rather than queuing).
Việc đạt được có tính quyết định hiệu suất trên một đơn nút yêu cầu việc giảm thiểu sự can thiệp từ
hệ điều hành’s bình thường tài nguyên-việc chia sẻ hành vi (Achieving deterministic performance on a single node requires reducing interference from the operating system’s normal resource-sharing behavior). Có thể đoán trước việc phục vụ các hệ thống như Clock-
work cho thấy rằng DNN sự suy luận có thể đáp ứng chặt chẽ cấp độ-yêu cầu các SLO khi việc lập lịch và sự thực thi
được kiểm soát một cách cẩn thận (Gujarati et al. 2020) (Predictable serving systems such as Clockwork show that DNN inference can meet tight request-level SLOs when scheduling and execution are controlled carefully (Gujarati et al. 2020)). CPU ái lực (affinity) (việc ghim (pinning)) là một cục bộ sự cô lập công cụ: nó
hạn chế sự suy luận máy chủ’s các luồng tới cụ thể vật lý các lõi do đó nhạy cảm-độ trễ công việc là ít (bị)
phơi bày (hơn) đối với luồng sự di chuyển và bộ nhớ đệm-tính cục bộ (locality) sự mất mát (CPU affinity (pinning) is one local isolation tool: it restricts the inference server’s threads to specific physical cores so latency-sensitive work is less exposed to thread migration and cache-locality loss). Việc ghim có thể giảm một nguồn của độ trễ sự bồn chồn,
nhưng nó là phần của một rộng hơn tài nguyên-sự cô lập chiến lược thay vì một hoàn chỉnh giải pháp (Pinning can reduce one source of latency jitter, but it is part of a broader resource-isolation strategy rather than a complete solution).
Bộ nhớ việc khóa (mlock) giải quyết một có liên quan nhưng khác biệt nguồn của sự bồn chồn (Memory locking (mlock) addresses a related but distinct source of jitter). Bằng mặc định, OS có thể
phân trang (page) bất kỳ bộ nhớ vùng (region) (nào) tới đĩa dưới bộ nhớ áp lực (By default, the OS can page any memory region to disk under memory pressure). Nếu GPU’s DMA động cơ bắt đầu việc đọc
mô hình các trọng số từ một vùng thứ mà (đã) bị phân trang ra (paged out), sự truyền (transfer) đình trệ (stalls) cho đến khi dữ liệu được lỗi (faulted) quay lại
vào RAM, một hình phạt được đo lường trong các mili giây thay vì các micro giây (If the GPU’s DMA engine begins reading model weights from a region that has been paged out, the transfer stalls until the data is faulted back into RAM, a penalty measured in milliseconds rather than microseconds). Việc khóa mô hình các trọng số
và KV các bộ nhớ đệm trong vật lý RAM đảm bảo nhất quán truy cập các thời gian, mặc dù sự đánh đổi là rằng
được ghim bộ nhớ không thể được đòi lại (reclaimed) bởi (các) khác tiến trình (Locking model weights and KV caches in physical RAM guarantees consistent access times, though the trade-off is that pinned memory cannot be reclaimed by other processes).
(Kỹ thuật thứ) ba kỹ thuật, ngắt sự che chắn (shielding), hoàn thành sự cô lập bức tranh (The third technique, interrupt shielding, completes the isolation picture). Mạng và lưu trữ
các ngắt được định tuyến tới sự suy luận các lõi có thể chiếm quyền ưu tiên (preempt) GPU lệnh sự đệ trình (submission) tại không thể đoán trước
các khoảnh khắc (Network and storage interrupts routed to inference cores can preempt GPU command submission at unpredictable moments). Việc hướng (Steering) những các ngắt này tới phi sự suy luận các lõi đảm bảo rằng các sự bùng nổ của đến lưu lượng truy cập (do)
không phá vỡ (disrupt) GPU’s lệnh luồng, thứ mà là đặc biệt quan trọng cho việc duy trì ổn định đuôi
độ trễ dưới tải (Steering these interrupts to noninference cores ensures that bursts of incoming traffic do not disrupt the GPU’s command stream, which is particularly important for maintaining stable tail latency under load).
Những sự cô lập các nguyên tắc này biến đổi một đơn giản “mô hình kịch bản” thành một có tính quyết định dịch vụ, một sự chuyển-
tiếp (transition) thiết yếu cho tới hạn-an toàn các ứng dụng như tự trị việc lái xe hay thời gian-thực công nghiệp sự kiểm soát (These isolation principles transform a simple “model script” into a deterministic service, a transition essential for safety-critical applications like autonomous driving or real-time industrial control).
Sự triển khai phổ, tải việc cân bằng, và tài nguyên sự cô lập xác định nơi các mô hình phục vụ và
cái gì cơ sở hạ tầng hỗ trợ chúng (The deployment spectrum, load balancing, and resource isolation define where models serve and what infrastructure supports them). (Vấn đề) còn lại câu hỏi là cách việc phục vụ phần mềm chính nó được
tổ chức, một cách cụ thể (những) nào các thành phần bao gồm một sự suy luận máy chủ và cách chúng điều phối (coordinate) để
biến không đều (irregular) người dùng lưu lượng truy cập thành hiệu quả phần cứng sự sử dụng (The remaining question is how the serving software itself is organized, specifically what components comprise an inference server and how they coordinate to turn irregular user traffic into efficient hardware utilization).

722
13.3 Việc phục vụ Hệ thống Kiến trúc
3
Sự suy luận
Máy chủ (Inference Server):
Google’s TensorFlow Serving
(Olston et al.
2017) đã giúp
thiết lập sự tách biệt của
mô hình logic từ việc phục vụ
cơ sở hạ tầng (Google’s TensorFlow Serving (Olston et al. 2017) helped establish the separation of model logic from serving infrastructure); NVIDIA’s Tri-
ton (NVIDIA 2024d) mở rộng
này mẫu qua nhiều
mô hình
các bộ khung (frameworks)
và
các chương trình phụ trợ (backends) (NVIDIA’s Triton (NVIDIA 2024d) extends this pattern across multiple model frameworks and backends). Chí mạng thiết kế
sự thấu hiểu là rằng một bộ lập lịch
và động bộ tạo lô biến
không đều đơn-yêu cầu lưu lượng truy cập
thành thân thiện-với-máy gia tốc sự thực-
thi, việc cải thiện sự sử dụng
khi độ trễ các ngân sách cho phép
việc tạo lô (The critical design insight is that a scheduler and dynamic batcher turn irregular single-request traffic into accelerator-friendly execution, improving utilization when latency budgets allow batching).
Chính xác sự sử dụng
các lợi ích
phụ thuộc
trên
mô hình,
phần cứng, đến tỷ lệ (arrival rate), và
được cấu hình (configured)
việc tạo lô
cửa sổ (window) (Exact utilization gains depend on model, hardware, arrival rate, and the configured batching window).
4
NCHW và NHWC (Ten-
sor Bộ nhớ Các bố cục (Tensor Memory Layouts)): Những
các từ viết tắt này mã hóa (encode) bộ-
nhớ bố cục thứ tự của 4D hình ảnh
các tensor: N (lô), C (các kênh
(channels)), H (chiều cao), W (chiều rộng).
NCHW đặt tất cả các giá trị cho
một kênh một cách liền kề (contiguously), việc kích-
hoạt được vector hóa sự tích chập (convolution)
trên các GPU; NHWC xen kẽ (interleaves)
các kênh tại mỗi không gian (spatial) vị-
trí, việc căn chỉnh (aligning) tốt hơn với
CPU đơn lệnh (instruction), nhiều (mul-
tiple) dữ liệu (SIMD) các lệnh.
Một định dạng sự không khớp giữa
máy khách và máy chủ có thể tạo ra
không chính xác các tensor thậm chí khi
hình dạng xuất hiện hợp lệ, do đó
việc phục vụ mã nên làm (cho) bố-
cục các sự chuyển đổi (trở nên) rõ ràng.
13.3 Việc phục vụ Hệ thống Kiến trúc (Serving System Architecture)
Người dùng các yêu cầu đến trong không thể đoán trước các sự bùng nổ, một mili giây cách nhau, sau đó năm các giây của sự im lặng,
trong khi các máy gia tốc đòi hỏi ổn định, có kích thước-đồng đều (uniformly-sized) các lô (User requests arrive in unpredictable bursts, one millisecond apart, then five seconds of silence, while accelerators demand steady, uniformly-sized batches). Việc thu hẹp này khoảng cách yêu cầu nhiều hơn một
Python kịch bản việc gọi model.predict(); nó yêu cầu một được chuyên môn hóa phần mềm kiến trúc thứ mà hấp thụ
lưu lượng truy cập tính biến đổi, hình thành (forms) hiệu quả các lô, và giữ phần cứng bị bão hòa mà không có việc vi phạm độ trễ
các SLO (Bridging this gap requires more than a Python script calling model.predict(); it requires a specialized software architecture that absorbs traffic variability, forms efficient batches, and keeps hardware saturated without violating latency SLOs).
13.3.1 Nội bộ kiến trúc và yêu cầu luồng (Internal architecture and request flow)
Mô hình sự tối ưu hóa tập trung trên toán học hiện vật (artifact), trong khi mô hình việc phục vụ yêu cầu một được chuyên môn hóa
phần mềm kiến trúc để quản lý cao-tần số (high-frequency) yêu cầu các luồng và phần cứng sự sử dụng (Model optimization focuses on the mathematical artifact, while model serving requires a specialized software architecture to manage high-frequency request streams and hardware utilization). Một
sự suy luận máy chủ3 (như NVIDIA Triton, TensorFlow Serving, hay TorchServe) là không (phải) một đơn giản
vỏ bọc (wrapper) xung quanh một mô hình kịch bản; nó là một cao-hiệu suất bộ lập lịch thứ mà quản lý tính đồng thời,
bộ nhớ, và dữ liệu sự di chuyển (An inference server3 (such as NVIDIA Triton, TensorFlow Serving, or TorchServe) is not a simple wrapper around a model script; it is a high-performance scheduler that manages concurrency, memory, and data movement).
Nội bộ giải phẫu học (anatomy) của những các máy chủ này tiết lộ cách chúng thu hẹp khoảng cách giữa không đều người dùng
lưu lượng truy cập và cao độ (highly) đều đặn, định hướng-vào-lô (batch-oriented) các yêu cầu của các máy gia tốc (The internal anatomy of these servers reveals how they bridge the gap between irregular user traffic and the highly regular, batch-oriented requirements of accelerators). Mọi yêu cầu đi ngang qua (traverses) một
nhiều-giai đoạn đường ống được thiết kế để tối đa hóa phần cứng thông lượng trong khi việc tối thiểu hóa độ trễ chi phí hoạt động (Every request traverses a multi-stage pipeline designed to maximize hardware throughput while minimizing latency overhead).
Hình 13.4 tách biệt sáu các giai đoạn do đó mỗi thành phần’s vai trò trong việc hấp thụ lưu lượng truy cập, việc xếp hàng đợi, việc tạo lô,
và máy gia tốc sự thực thi là rõ ràng (Figure 13.4 separates the six stages so each component’s role in absorbing traffic, queueing, batching, and accelerator execution is explicit).
GPU
Máy khách
(Yêu cầu)
Mạng Sự xâm nhập (Ingress)
(HTTP/gRPC)
Yêu cầu
Hàng đợi
Động
Bộ tạo lô
Sự suy luận Trình chạy
(TensorRT/ONNX)
Máy gia tốc
(GPU/TPU)
Yêu cầu Việc lưu bộ đệm (Buffering)
Thông lượng Sự tối ưu hóa (Throughput Opt.)
Sự thực thi
Sự tối ưu hóa (Execution Opt.)
Hình 13.4: Sự suy luận Máy chủ Giải phẫu học (Inference Server Anatomy): Một hiện đại sự suy luận máy chủ tách rời (decouples) mạng việc xử lý khỏi máy gia tốc sự thực thi
thông qua một được chia giai đoạn đường ống (A modern inference server decouples network handling from accelerator execution through a staged pipeline). Mỗi giai đoạn cô lập một mối quan tâm, từ việc hấp thụ bùng nổ lưu lượng truy cập tới việc hình thành hiệu quả các lô, do đó
phần cứng máy gia tốc ở lại (được) cao độ sử dụng mặc dù không đều đến các mẫu (Each stage isolates a concern, from absorbing bursty traffic to forming efficient batches, so the hardware accelerator stays highly utilized despite irregular arrival patterns).
Này kiến trúc phục vụ ba các chức năng. Đầu tiên, tính đồng thời sự quản lý: các máy chủ sử dụng không đồng-
bộ (asynchronous) sự kiện các vòng lặp hay luồng các hồ (pools) để xử lý hàng nghìn của đồng thời máy khách các kết nối mà không có
việc chặn (blocking), việc đảm bảo rằng mạng I/O chờ các thời gian không (làm) rảnh rỗi (idle) máy gia tốc (First, concurrency management: servers use asynchronous event loops or thread pools to handle thousands of concurrent client connections without blocking, ensuring that network I/O wait times do not idle the accelerator). (Chức năng thứ) hai, yêu cầu sự biến-
đổi: máy chủ chuyển đổi mạng các tải trọng (payloads), như JavaScript Đối tượng Ký hiệu (JavaScript Object Notation - JSON) hay
Protobuf, thành cụ thể tensor các định dạng được yêu cầu bởi được tối ưu hóa mô hình thời gian chạy (Second, request transformation: the server converts network payloads, such as JavaScript Object Notation (JSON) or Protobuf, into the specific tensor formats required by the optimized model runtime). Hình ảnh các tensor,
cho ví dụ, có thể được lưu trữ như NCHW4 (lô, các kênh, chiều cao, chiều rộng) hay NHWC (lô, chiều cao,
chiều rộng, các kênh) (Image tensors, for example, can be stored as NCHW4 (batch, channels, height, width) or NHWC (batch, height, width, channels)). PyTorch và TensorRT thích NCHW bởi vì nó đặt kênh dữ liệu một cách liền kề,
việc kích hoạt hiệu quả sự tích chập trên các GPU (PyTorch and TensorRT prefer NCHW because it places channel data contiguously, enabling efficient convolution on GPUs). TensorFlow mặc định (đến) NHWC, thứ mà là hiệu quả hơn trên
các CPU.
(Chức năng thứ) ba, mô hình sự quản lý: sự suy luận các máy chủ quản lý vòng đời của được tải mô hình các hiện vật,
bao gồm việc tải các trọng số vào VRAM, việc theo dõi (cái) nào hiện vật phiên bản là hoạt động, và việc hoàn thành
sự khởi động các sự suy luận trước khi việc phơi bày mô hình tới trực tiếp lưu lượng truy cập (Third, model management: inference servers manage the lifecycle of loaded model artifacts, including loading weights into VRAM, tracking which artifact version is active, and completing warmup inferences before exposing the model to live traffic). Đầy đủ các sổ đăng ký (registries) (được tạo phiên bản hiện vật các cửa hàng),

13. Mô hình Việc phục vụ (Model Serving)
723
5
Giao thức Các bộ đệm (Proto-
buf): Protobuf sử dụng một được định-
nghĩa trước (predefined) lược đồ (từ một .proto
tệp) để mã hóa có cấu trúc dữ liệu
thành một nhỏ gọn nhị phân định-
dạng (Giao thức Các bộ đệm Các tác giả (Protocol Buffers Authors)
2026) (Protobuf uses a predefined schema (from a .proto file) to encode structured data into a compact binary format (Protocol Buffers Authors 2026)). Bởi vì lược đồ mang
trường các tên và các kiểu,
dây (wire) tải trọng (payload) cần không lặp lại
chúng như JSON làm (Because the schema carries field names and types, the wire payload need not repeat them as JSON does). Của nó dây
định dạng là vẫn không giống hệt tới
một C++ đối tượng’s trong-bộ nhớ bố-
cục, do đó nó yêu cầu một sự phân tích cú pháp (parsing)
bước và không cung cấp
giống nhau trực tiếp không-bản sao truy cập
mẫu thứ mà FlatBuffers nhắm-
mục tiêu (Its wire format is still not identical to a C++ object’s in-memory layout, so it requires a parsing step and does not provide the same direct zero-copy access pattern that FlatBuffers targets).
6
FlatBuffers: “phẳng” trong
tên mô tả thiết kế:
nhị phân bộ đệm có thể phục vụ
như được tuần tự hóa sự biểu-
diễn (representation) và dữ liệu cấu trúc
đang (được) đọc, việc tránh một riêng-
biệt sự phân tích cú pháp hay sự mở gói (unpacking)
giai đoạn (phase) cho được hỗ trợ truy cập
các mẫu (FlatBuffers Các tác giả (FlatBuffers Authors)
2026) (The “flat” in the name describes the design: the binary buffer can serve as the serialized representation and the data structure being read, avoiding a separate parsing or unpacking phase for supported access patterns (FlatBuffers Authors 2026)). Cho ML sự suy luận, điều này
có thể kích hoạt không-bản sao truy cập tới
tensor siêu dữ liệu—việc phục vụ
hệ thống đọc tensor các hình dạng
và các phần bù (offsets) một cách trực tiếp từ
bộ đệm thay vì việc cấp phát một
thứ hai đối tượng sự biểu diễn (For ML inference, this can enable zero-copy access to tensor metadata—the serving system reads tensor shapes and offsets directly from the buffer rather than allocating a second object representation).
7
gRPC (gRPC Từ xa
Thủ tục Lệnh gọi (Remote Procedure Call)): gRPC ghép nối (pairs)
HTTP/2 sự vận chuyển với một
giao diện định nghĩa ngôn ngữ
và tin nhắn định dạng, nhất
một cách phổ biến Giao thức Các bộ đệm
(gRPC Các tác giả 2026) (gRPC pairs HTTP/2 transport with an interface definition language and message format, most commonly Protocol Buffers (gRPC Authors 2026)).
(Sự)
liên quan
việc phục vụ
lợi-
thế (advantage)
là sự kết hợp của
có kiểu (typed) các hợp đồng (contracts),
dai dẳng (persistent)
được ghép kênh (multiplexed)
các kết nối,
sự phát trực tuyến (streaming)
sự hỗ trợ,
và
nhỏ gọn
nhị phân
các tin nhắn.
Kích thước và độ trễ lợi ích
so với REST/JSON phụ thuộc trên
tải trọng hình dạng, máy khách/máy chủ
sự triển khai, và liệu
sự tuần tự hóa (có) là một có ý nghĩa
phần chia sẻ
của
(cái)
đầu cuối-tới-đầu cuối (end-to-end)
độ trễ ngân sách (hay không) (The size and latency benefit over REST/JSON depends on payload shape, client/server implementation, and whether serialization is a meaningful share of the end-to-end latency budget).
phát hành các cổng (các sự kiểm tra trước khi phát hành), và khôi phục trạng thái cũ (rollback) sự quản trị (governance) (các quy tắc cho việc hoàn nguyên (reverting) một tồi phát hành)
thuộc về Chương 14; cục bộ việc phục vụ mối quan tâm là liệu đúng hiện vật (đã) được tải và sẵn sàng (hay không) (release gates (checks before release), and rollback governance (rules for reverting a bad release) belong to Chapter 14; the local serving concern is whether the right artifact is loaded and ready).
Trong số những các thành phần này, bộ lập lịch xứng đáng (deserves) đặc biệt sự chú ý bởi vì nó hiện thân (embodies) cốt lõi
việc phục vụ sự đánh đổi giữa thông lượng và độ trễ (Among these components, the scheduler deserves special attention because it embodies the core serving trade-off between throughput and latency).
Bộ lập lịch là “bộ não” của sự suy luận máy chủ (The Scheduler is the “brain” of the inference server). Nó triển khai động việc tạo lô logic
được thảo luận trong phần 13.7 (It implements the dynamic batching logic discussed in section 13.7). Bộ lập lịch phải quyết định liệu chạy một đơn yêu cầu ngay lập tức để
tối thiểu hóa của nó độ trễ hay đợi năm các mili giây cho một thứ hai yêu cầu và xử lý chúng cùng nhau để
tối đa hóa thông lượng (The scheduler must decide whether to run a single request immediately to minimize its latency or wait five milliseconds for a second request and process them together to maximize throughput).
Các hệ thống những người thiết kế sử dụng Việc tạo lô Cửa sổ tham số để điều chỉnh này sự đánh đổi (Systems designers use the Batching Window parameter to tune this trade-off). Một cửa sổ của 0 ms
tối ưu hóa cho thuần túy độ trễ (không việc tạo lô), trong khi một nhỏ bị giới hạn (bounded) cửa sổ để bộ lập lịch đánh đổi một
được kiểm soát lượng của việc chờ đợi cho cao hơn máy gia tốc sự sử dụng (A window of 0 ms optimizes for pure latency (no batching), while a small bounded window lets the scheduler trade a controlled amount of waiting for higher accelerator utilization). Này quyết định xác định (mức độ) bận rộn như thế nào
máy gia tốc ở lại: liệu phần cứng dành của nó thời gian việc tính toán hay việc chờ đợi cho công việc (This decision determines how busy the accelerator stays: whether the hardware spends its time computing or waiting for work).
13.3.2 Giao diện các giao thức và sự tuần tự hóa (Interface protocols and serialization)
Cơ chế được sử dụng để vận chuyển dữ liệu giữa máy khách và máy chủ một cách trực tiếp ảnh hưởng độ trễ ngân sách (The mechanism used to transport data between client and server directly affects the latency budget).
Mô hình sự suy luận là thường cao độ được tối ưu hóa, tuy nhiên chi phí của việc di chuyển dữ liệu vào mô hình (sự tuần tự hóa
và mạng giao thức chi phí hoạt động) có thể trở thành thống trị nút thắt cổ chai, đặc biệt cho nhẹ (lightweight)
các mô hình nơi sự suy luận thời gian là nhỏ (Model inference is often highly optimized, yet the cost of moving data into the model (serialization and network protocol overhead) can become the dominant bottleneck, especially for lightweight models where inference time is small).
13.3.2.1 Sự tuần tự hóa nút thắt cổ chai
ML việc phục vụ các tải trọng là về cơ bản khác biệt từ điển hình web API các tải trọng: chúng bao gồm
của nhiều-chiều nổi (float) các mảng (hình ảnh các tensor, sự nhúng các vector, mã thông báo ID các chuỗi (sequences)) thứ mà
là dày đặc (dense), nhị phân, và lớn (ML serving payloads are fundamentally different from typical web API payloads: they consist of multi-dimensional float arrays (image tensors, embedding vectors, token ID sequences) that are dense, binary, and large). Dựa trên-văn bản các định dạng như JSON là phổ biến nhưng về mặt tính toán
tốn kém cho loại của dữ liệu này (Text-based formats like JSON are ubiquitous but computationally expensive for this kind of data). Sự tuần tự hóa chi phí hoạt động xuất hiện khi việc phân tích cú pháp một JSON đối tượng yêu cầu
việc đọc mọi byte, việc xác nhận cú pháp, và việc chuyển đổi văn bản các sự biểu diễn thành bản địa-máy móc (machine-native) các kiểu (Serialization overhead appears when parsing a JSON object requires reading every byte, validating syntax, and converting text representations into machine-native types).
Cho tensor các tải trọng, chi phí cộng gộp (compounds): dấu phẩy-động các giá trị phải đầu tiên được mã hóa như ASCII
các chữ số (việc thổi phồng (inflating) một 4-byte nổi tới 10–15 các ký tự), và nhị phân dữ liệu như hình ảnh các byte yêu cầu
Base64 sự mã hóa, thứ mà thêm 33 phần trăm kích thước chi phí hoạt động trước khi JSON sự phân tích cú pháp bắt đầu (For tensor payloads, the cost compounds: floating-point values must first be encoded as ASCII digits (inflating a 4-byte float to 10–15 characters), and binary data such as image bytes requires Base64 encoding, which adds 33 percent size overhead before JSON parsing begins). Cho cao-
thông lượng các hệ thống, điều này tiêu thụ CPU các chu kỳ thứ mà có thể nói cách khác (otherwise) được sử dụng cho yêu cầu việc xử lý
hay sự tiền xử lý (For high-throughput systems, this consumes CPU cycles that could otherwise be used for request handling or preprocessing).
Nhị phân các định dạng như Giao thức Các bộ đệm5 (Protobuf) hay FlatBuffers6 giảm này sự phình to (bloat) bằng cách việc sử dụng nhận thức-
lược đồ nhị phân các sự mã hóa thay vì văn bản các sự mã hóa (Binary formats like Protocol Buffers5 (Protobuf) or FlatBuffers6 reduce this bloat by using schema-aware binary encodings instead of text encodings). Bản địa nổi các mảng có thể truyền như nhỏ gọn IEEE
754 các byte với không ASCII sự chuyển đổi và không Base64 vỏ bọc (Native float arrays can transmit as compact IEEE 754 bytes with no ASCII conversion and no Base64 wrapper). FlatBuffers có thể cũng kích hoạt không-bản sao
truy cập trong được hỗ trợ các trường hợp, nơi mạng bộ đệm có thể được đọc mà không có việc cấp phát một riêng biệt đối tượng
đồ thị (FlatBuffers can also enable zero-copy access in supported cases, where the network buffer can be read without allocating a separate object graph).
13.3.2.2 REST so với gRPC
Hai phổ biến các mô hình mẫu định nghĩa việc phục vụ các giao diện, mỗi (cái) với khác biệt hệ thống các đặc điểm (Two common paradigms define serving interfaces, each with distinct system characteristics). REST
(Đại diện (Representational) Trạng thái Chuyển giao) điển hình (typically) sử dụng HTTP/1.1 và JSON (REST (Representational State Transfer) typically uses HTTP/1.1 and JSON). Nó là rộng rãi được hỗ trợ, có thể đọc-
bởi-con người (human-readable), và không trạng thái (stateless), việc làm nó một phổ biến sự lựa chọn cho hướng ra-công chúng (public-facing) các API (It is widely supported, human-readable, and stateless, making it a common choice for public-facing APIs). Tuy nhiên, REST’s
tính không trạng thái ép buộc việc gửi lại ngữ cảnh với mọi lệnh gọi; cho LLM việc phục vụ, nơi một cuộc trò chuyện
ngữ cảnh có thể vượt quá 10 KB của mã thông báo các ID, này mỗi-yêu cầu chi phí hoạt động cộng gộp tại cao QPS (However, REST’s statelessness forces re-sending context with every call; for LLM serving, where a conversation context can exceed 10 KB of token IDs, this per-request overhead compounds at high QPS). Tiêu chuẩn
HTTP/1.1 sử dụng dai dẳng TCP các kết nối bằng mặc định, nhưng không có HTTP/2-kiểu sự ghép kênh một
máy khách thường cần nhiều các kết nối hay cẩn thận kết nối việc gộp (pooling) để tránh đầu-của-hàng (head-of-line) việc chặn
và bắt tay (handshake) chi phí hoạt động sau rảnh rỗi các thời gian chờ (timeouts) (Standard HTTP/1.1 uses persistent TCP connections by default, but without HTTP/2-style multiplexing a client often needs multiple connections or careful connection pooling to avoid head-of-line blocking and handshake overhead after idle timeouts). JSON sự tuần tự hóa cũng thêm đáng kể độ trễ cho
thuộc về số (numerical) dữ liệu như các tensor (JSON serialization also adds significant latency for numerical data like tensors).
Trong sự trái ngược, gRPC (gRPC Từ xa Thủ tục Lệnh gọi)7 sử dụng HTTP/2 và một cách phổ biến sử dụng Protobuf (In contrast, gRPC (gRPC Remote Procedure Call)7 uses HTTP/2 and commonly uses Protobuf).
HTTP/2 kích hoạt việc ghép kênh nhiều các yêu cầu qua một đơn dai dẳng TCP kết nối, việc giảm thiểu
kết nối-sự quản lý chi phí hoạt động và việc cho phép hiệu quả nhị phân sự phát trực tuyến (HTTP/2 enables multiplexing multiple requests over a single persistent TCP connection, reducing connection-management overhead and allowing efficient binary streaming). Protobuf cung cấp có kiểu
các lược đồ và hiệu quả nhị phân sự tuần tự hóa, việc làm gRPC một phổ biến sự lựa chọn cho nội bộ dịch vụ-tới-
dịch vụ (service-to-service) sự giao tiếp nơi độ trễ và có kiểu các giao diện quan trọng (Protobuf provides typed schemas and efficient binary serialization, making gRPC a common choice for internal service-to-service communication where latency and typed interfaces matter).
Một cụ thể tải trọng sự so sánh cho thấy cách sự tuần tự hóa sự lựa chọn thay đổi cả hai dây kích thước và
sự phân tích cú pháp chi phí (A concrete payload comparison shows how the serialization choice changes both wire size and parsing cost).

724
13.4 Yêu cầu Vòng đời (Request Lifecycle)
8
Đuôi Độ trễ: Không giống như trung
bình, phân vị (percentile) các độ trễ tiết
lộ hiệu suất tác động
của hệ thống những ngoại lệ (outliers) phổ biến trong
ML việc phục vụ, như mô hình
bộ nhớ đệm các sự bỏ lỡ (misses) hay thu gom rác (garbage collec-
tion) các sự tạm dừng (pauses). Những hiếm, cao-
độ trễ các yêu cầu (này) một cách không tương-
xứng (disproportionately) làm hại người dùng sự hài lòng (satisfac-
tion) và một cách trực tiếp tác động doanh-
thu (revenue). Nền tảng các nghiên cứu tại
Google và Amazon (đã) định-
lượng này mối quan hệ, việc tìm thấy
rằng 100 ms của được thêm độ trễ
tốn ~1 phần trăm trong các doanh số bán hàng (sales), việc thiết-
lập phân vị các mục tiêu (p95,
p99) như là chí mạng các số liệu cho
dịch vụ chất lượng.
Khăn ăn Toán học 13.2: JSON so với Protobuf sự tuần tự hóa (JSON vs. Protobuf serialization)
Hãy xem xét một yêu cầu tải trọng (chứa) đựng 1,000 dấu phẩy động các số (cho ví dụ, một sự nhúng
vector).
• JSON: Sử dụng ~9 KB trên dây. Yêu cầu ~50 μs để phân tích cú pháp.
• Protobuf: Sử dụng ~4 KB trên dây. Yêu cầu ~5 μs để phân tích cú pháp.
Toán học: Việc chuyển đổi (Switching) một yêu cầu sang nhị phân tải trọng tiết kiệm 50 μs −5 μs = 45 μs của phân tích cú pháp thời gian (Math: Switching one request to the binary payload saves 50 μs −5 μs = 45 μs of parse time).
Cho này mang tính minh họa hệ thống việc xử lý 10,000 các yêu cầu mỗi giây, các khoản tiết kiệm (savings) cộng gộp thành
10,000 × 45 μs = 0.45 s của CPU thời gian được đòi lại mọi bức tường-đồng hồ giây, thứ mà là 45 phần trăm của
một lõi được giải phóng từ sự tuần tự hóa chi phí hoạt động một mình (alone) (For this illustrative system processing 10,000 requests per second, the savings compound to 10,000 × 45 μs = 0.45 s of CPU time reclaimed every wall-clock second, which is 45 percent of one core freed from serialization overhead alone).
Các hệ thống sự thấu hiểu: Này 10× kịch bản lợi ích làm gRPC/Protobuf, FlatBuffers, hay khác nhị phân
giao thức một mạnh ứng cử viên cho cao-thông lượng nội bộ các vi dịch vụ khi sự tuần tự hóa là một
có thể nhìn thấy (visible) phần của độ trễ ngân sách (Systems insight: This 10× scenario gain makes gRPC/Protobuf, FlatBuffers, or another binary protocol a strong candidate for high-throughput internal microservices when serialization is a visible part of the latency budget).
Hệ thống sự lựa chọn là phụ thuộc-sự ép buộc (constraint-dependent). REST/HTTP là phổ biến khi công cộng tính tương thích (compatibil-ity),
việc gỡ lỗi, và hệ sinh thái phạm vi tiếp cận (reach) thống trị (REST/HTTP is common when public compatibility, debugging, and ecosystem reach dominate). gRPC/Protobuf, hay (một) khác nhị phân giao thức, được
ưa chuộng (favored) khi nội bộ cao-QPS tensor lưu lượng truy cập, kết nối sự tái sử dụng, hay sự phát trực tuyến làm sự tuần tự hóa (thành) một
có ý nghĩa phần chia sẻ của độ trễ và CPU ngân sách (gRPC/Protobuf, or another binary protocol, is favored when internal high-QPS tensor traffic, connection reuse, or streaming makes serialization a meaningful share of the latency and CPU budget).
Thuộc về kiến trúc các thành phần và các giao thức được kiểm tra cho đến nay (so far) mô tả cách việc phục vụ các hệ thống được
xây dựng (The architectural components and protocols examined so far describe how serving systems are built). Việc hiểu tại sao nhất định các cấu hình (configurations) thực hiện tốt hơn yêu cầu việc phân tích (những) gì xảy ra đối với
cá nhân các yêu cầu khi chúng đi ngang qua những các thành phần này (Understanding why certain configurations perform better requires analyzing what happens to individual requests as they traverse these components).
13.4 Yêu cầu Vòng đời
Một đơn HTTP yêu cầu (chứa) mang một 224×224 JPEG hình ảnh đến tại một sự suy luận máy chủ (A single HTTP request carrying a 224×224 JPEG image arrives at an inference server). Giữa
khoảnh khắc (đầu) tiên byte đi vào mạng ngăn xếp và khoảnh khắc sự phân loại kết quả rời đi, đó
yêu cầu đi ngang qua sáu đường ống các giai đoạn, mỗi (cái) việc tiêu thụ các mili giây thứ mà người dùng trải nghiệm như chờ
thời gian (Between the moment the first byte enters the network stack and the moment the classification result leaves, that request traverses six pipeline stages, each consuming milliseconds that the user experiences as wait time). Việc hiểu nơi thời gian đi (đến) bên trong mỗi yêu cầu là thiết yếu cho hiệu quả sự tối ưu hóa: một
(người) không thể cải thiện (những) gì một (người) không (đo) lường (Understanding where time goes within each request is essential for effective optimization: one cannot improve what one does not measure).
13.4.1 Độ trễ ngân sách (The latency budget)
Cho động sự suy luận các hệ thống, việc phục vụ sự đảo ngược được thiết lập trong phần 13.1 tạo ra một độ trễ
ngân sách thứ mà định hình hệ thống thiết kế (Gujarati et al. 2020) (For dynamic inference systems, the serving inversion established in section 13.1 creates a latency budget that shapes system design (Gujarati et al. 2020)). Một việc phục vụ hệ thống với cấp độ-giây (second-scale) mỗi-
yêu cầu độ trễ có thể bỏ lỡ nhiều tương tác các SLO, thậm chí nếu nó đạt được xuất sắc thông lượng (A serving system with second-scale per-request latency may miss many interactive SLOs, even if it achieves excellent throughput).
(Sự) liên quan các số liệu dịch chuyển từ tổng hợp thông lượng tới độ trễ các sự phân phối (Relevant metrics shift from aggregate throughput to latency distributions). Trung bình (Mean) độ trễ tiết lộ
ít về người dùng trải nghiệm; p50, p95, và p99 các độ trễ tiết lộ cách hệ thống thực hiện qua
đầy đủ phạm vi (range) của các yêu cầu (Mean latency reveals little about user experience; p50, p95, and p99 latencies reveal how the system performs across the full range of requests). Nếu trung bình độ trễ là 50 ms nhưng p99 là hai các giây, một trong một trăm những người dùng
đợi 40× lâu hơn so với trung bình (If the mean latency is 50 ms but p99 is two seconds, one in a hundred users waits 40× longer than average). Cho hướng đến-người tiêu dùng các ứng dụng, những đuôi các độ trễ này thường xác định
người dùng sự hài lòng và sự giữ lại (retention).8
Việc quản lý những phân vị các sự ép buộc này yêu cầu việc phân rã (decomposing) tổng cho phép phản hồi thời gian thành
một độ trễ ngân sách thứ mà phân bổ (allocates) thời gian qua mỗi việc xử lý giai đoạn (Managing these percentile constraints requires decomposing the total allowed response time into a latency budget that allocates time across each processing phase).
Định nghĩa 13.2: Độ trễ ngân sách
Độ trễ Ngân sách là thời gian vốn được phân bổ tới một ML sự suy luận yêu cầu, một cách nghiêm ngặt bị giới hạn bởi
(cái) đầu cuối-tới-đầu cuối dịch vụ cấp độ mục tiêu (SLO) (Latency Budget is the time capital allocated to an ML inference request, strictly bounded by the end-to-end service level objective (SLO)).
1. Tầm quan trọng: Nó hoạt động (acts) như một tổng-bằng không (zero-sum) sự ép buộc hệ thống nơi bất kỳ các mili giây (nào) được tiêu thụ
bởi sự tuần tự hóa hay mạng chi phí hoạt động một cách trực tiếp giảm độ trễ ngân sách (𝐿lat) có sẵn
cho mô hình sự suy luận (It acts as a zero-sum constraint system where any milliseconds consumed by serialization or network overhead directly reduce the latency budget (𝐿lat) available for model inference).
2. Sự khác biệt: Không giống như trung bình độ trễ, thứ mà giấu phương sai, một độ trễ ngân sách là một cứng
ranh giới (bound) thứ mà phải được duy trì cho chậm nhất các yêu cầu (cho ví dụ, p99) (Unlike average latency, which hides variance, a latency budget is a hard bound that must be maintained for the slowest requests (for example, p99)).

13. Mô hình Việc phục vụ (Model Serving)
725
Sự suy luận là một lát cắt của độ-
trễ ngân sách; sự tiền xử lý sánh-
ngang (rivals) nó.
3. Phổ biến cạm bẫy: Một thường xuyên quan niệm sai lầm là rằng “mô hình” có toàn bộ ngân sách (A frequent misconception is that the “model” has the entire budget).
Trong thực tế, mô hình thường có ít hơn 50 phần trăm của tổng ngân sách; phần còn lại (remainder) là
được tiêu thụ bởi yêu cầu vòng đời (DNS, TLS, tải việc cân bằng, sự tuần tự hóa) (In reality, the model often has less than 50 percent of the total budget; the remainder is consumed by the request lifecycle (DNS, TLS, load balancing, serialization)).
Trước khi việc tính toán một đầy đủ ngân sách, này trạm kiểm soát thiết lập (đặt) nền tảng độ trễ-sự phân tích các kỹ năng mọi
việc phục vụ kỹ sư cần (Before computing a full budget, this checkpoint sets the foundational latency-analysis skills every serving engineer needs).
Trạm kiểm soát 13.1: ResNet-50 độ trễ sự phân tích
Việc phục vụ tối ưu hóa đuôi độ trễ dưới tải. Sử dụng này trạm kiểm soát để tách biệt việc xếp hàng đợi và
việc tạo lô các hiệu ứng trước khi việc chọn một sự tối ưu hóa (Use this checkpoint to separate queueing and batching effects before choosing an optimization).
□Hàng đợi hành vi: Sử dụng hình 13.1 để mô tả tại sao độ trễ tăng phi tuyến tính (nonlinearly) khi sự sử dụng
tiếp cận sự bão hòa (Queue behavior: Use figure 13.1 to describe why latency rises nonlinearly as utilization approaches saturation).
□Việc tạo lô sự đánh đổi: So sánh thông lượng lợi ích từ lớn hơn các lô đối nghịch (against) độ trễ
chi phí mỗi yêu cầu (Batching trade-off: Compare the throughput gain from larger batches against the latency cost per request).
Mọi việc phục vụ yêu cầu phân rã (decomposes) thành ba các giai đoạn thứ mà mỗi (cái) tiêu thụ (một) phần của độ trễ ngân sách (Every serving request decomposes into three phases that each consume part of the latency budget).
Sự tiền xử lý biến đổi thô đầu vào như hình ảnh các byte hay văn bản các chuỗi (strings) thành sẵn sàng-cho-mô hình các tensor (Preprocessing transforms raw input such as image bytes or text strings into model-ready tensors).
Sự suy luận thực thi mô hình sự tính toán (Inference executes the model computation). Sự hậu xử lý biến đổi mô hình các đầu ra thành hướng-tới-người dùng
các phản hồi (Postprocessing transforms model outputs into user-facing responses).
Nhanh hơn phần cứng không một cách tự động có nghĩa nhanh hơn việc phục vụ (Faster hardware does not automatically mean faster serving). Trong thực tế, sự tiền xử lý và sự hậu-
xử lý có thể thống trị tổng độ trễ khi sự suy luận chạy trên được tối ưu hóa các máy gia tốc (In practice, preprocessing and postprocessing can dominate total latency when inference runs on optimized accelerators). Việc tối ưu hóa
một cách độc quyền (exclusively) sự suy luận giai đoạn mang lại (yields) giảm dần (diminishing) các lợi tức nếu xung quanh đường ống (vẫn) duy trì
bị thắt cổ chai bởi CPU các hoạt động (Optimizing exclusively the inference phase yields diminishing returns if the surrounding pipeline remains bottlenecked by CPU operations).
13.4.2 Độ trễ sự phân phối sự phân tích (Latency distribution analysis)
Việc hiểu nơi thời gian đi (đến) yêu cầu việc trang bị (instrumenting) mỗi giai đoạn một cách độc lập (Understanding where time goes requires instrumenting each phase independently). Một ResNet-50
độ trễ ngân sách sự cố (việc chia nhỏ (breakdown)) tiết lộ một cách chính xác cách mỗi mili giây được dành khi của chúng ta bộ phân loại nhận
một JPEG hình ảnh (A ResNet-50 latency budget breakdown reveals exactly how each millisecond is spent when our classifier receives a JPEG image).
Các hệ thống Góc nhìn 13.3: ResNet-50: Độ trễ ngân sách sự cố
Bảng 13.3 chia nhỏ (breaks down) một điển hình ResNet-50 việc phục vụ yêu cầu (thành) mỗi (per) giai đoạn:
Bảng 13.3: ResNet-50 độ trễ ngân sách: Mỗi-giai đoạn sự cố của một đơn việc phục vụ yêu cầu, việc cho thấy rằng sự tiền xử lý và
dữ liệu sự truyền cùng nhau sánh ngang chi phí của ResNet-50 chuyển tiếp vượt qua chính nó (Per-phase breakdown of a single serving request, showing that preprocessing and data transfer together rival the cost of the ResNet-50 forward pass itself). Các tỷ lệ phần trăm (percentages) phơi bày nơi kỹ thuật nỗ lực
thực sự được đền đáp (pays off), thứ mà là hiếm khi trong mô hình (The percentages expose where engineering effort actually pays off, which is rarely in the model). Mỗi-giai đoạn các tỷ lệ phần trăm được làm tròn tới gần nhất nguyên số và có thể
không tính tổng tới chính xác 100 (Per-phase percentages are rounded to the nearest whole number and may not sum to exactly 100).
Giai đoạn
Hoạt động (Operation)
Thời gian
Tỷ lệ phần trăm
Sự tiền xử lý
JPEG sự giải mã (decode)
3 ms
30%
Sự tiền xử lý
Thay đổi kích thước (Resize) tới 224×224
1 ms
10%
Sự tiền xử lý
Chuẩn hóa (Normalize) (trung bình/độ lệch chuẩn (std))
0.5 ms
5%
Dữ liệu Sự truyền
CPU→GPU bản sao
0.5 ms
5%
Sự suy luận
ResNet-50 chuyển tiếp vượt qua
5 ms
50%
Sự hậu xử lý
Softmax + top-5
0.1 ms
~1%
Tổng cộng
10.1 ms
100%
Các hệ thống sự thấu hiểu: ResNet-50 việc phục vụ ngân sách cho thấy sự tiền xử lý tiêu thụ 44.6 phần trăm
của độ trễ mặc dù mô hình sự suy luận là (cái) chuyên sâu-về mặt-tính toán (computational intensive) giai đoạn (Systems insight: The ResNet-50 serving budget shows preprocessing consumes 44.6 percent of latency despite model inference being the computationally intensive phase). Với TensorRT
sự tối ưu hóa việc giảm thiểu sự suy luận xuống 2 ms, sự tiền xử lý (sẽ) thống trị tại 63.4 phần trăm (With TensorRT optimization reducing inference to 2 ms, preprocessing would dominate at 63.4 percent).
ResNet ví dụ đại diện giới hạn-tính toán sự suy luận nơi chuyển tiếp-vượt qua số học (arithmetic)
thống trị độ trễ ngân sách (The ResNet example represents compute-bound inference where the forward-pass arithmetic dominates the latency budget). Việc áp dụng giống nhau bộ khung tới một khác biệt mô hình kiến trúc thường
tiết lộ rằng nút thắt cổ chai dịch chuyển từ tính toán sang bộ nhớ băng thông, việc vô hiệu hóa (invalidating) sự tối ưu hóa
các chiến lược thứ mà (đã) làm việc cho thị giác các mô hình (Applying the same framework to a different model architecture often reveals that the bottleneck shifts from compute to memory bandwidth, invalidating the optimization strategies that worked for vision models). Sự giới thiệu các hệ thống thể hiện chính xác này sự dịch chuyển (Recommendation systems exhibit exactly this shift).
Ngọn hải đăng (Lighthouse) 13.1: Ngọn hải đăng ví dụ: DLRM việc phục vụ
Kịch bản: Việc phục vụ DLRM với một 10 ms P99 độ trễ ngân sách.
Sự phân tích: Trong khi ResNet-50’s mô hình giai đoạn bị thống trị bởi tích chập nơ-ron mạng
(CNN) tính toán, DLRM’s thống trị mô hình-giai đoạn chi phí là sự nhúng-bảng bộ nhớ truy cập (Analysis: While ResNet-50’s model stage is dominated by convolutional neural network (CNN) compute, DLRM’s dominant model-stage cost is embedding-table memory access).
Đầu cuối-tới-đầu cuối việc phục vụ các nút thắt cổ chai vẫn yêu cầu việc đo lường đầy đủ con đường: sự tiền xử lý, sự suy luận,
sự hậu xử lý, và dữ liệu sự di chuyển (End-to-end serving bottlenecks still require measuring the full path: preprocessing, inference, postprocessing, and data movement). Bảng 13.4 chia nhỏ sự giới thiệu yêu cầu (thành) mỗi
giai đoạn (Table 13.4 breaks the recommendation request down by phase):
Bảng 13.4: DLRM việc phục vụ độ trễ: Mỗi-giai đoạn sự cố của một sự giới thiệu yêu cầu dưới một 10 ms p99 ngân sách,
việc đối chiếu (contrasting) DLRM’s giới hạn-bộ nhớ-băng thông sự nhúng các sự tra cứu (lookups) đối nghịch ResNet-50’s giới hạn-tính toán chuyển tiếp vượt qua (Per-phase breakdown of a recommendation request under a 10 ms p99 budget, contrasting DLRM’s memory-bandwidth-bound embedding lookups against ResNet-50’s compute-bound forward pass).
Việc thêm tính toán tới sự suy luận giai đoạn không giúp một khi sự nhúng-bảng băng thông là việc ràng buộc sự ép buộc (Adding compute to the inference stage does not help once embedding-table bandwidth is the binding constraint).
Giai đoạn
Hoạt động
Thời gian
Nút thắt cổ chai (Bottleneck)
Đầu vào Sự phân tích cú pháp (Parsing)
Yêu cầu sự phân tích cú pháp
0.5 ms
CPU
Sự nhúng Việc tra cứu (Look(up))
Việc lấy (Fetch) 100+ dày đặc các vector
6 ms
bộ nhớ băng thông
Sự suy luận
MLP chuyển tiếp vượt qua
1.5 ms
Tính toán
Sự hậu xử lý
Xếp hạng (Ranking) & Việc lọc (Filtering)
1 ms
CPU
Tổng cộng
9 ms
Các hệ thống sự thấu hiểu: Trong DLRM, “Sự suy luận” nhiều lớp perceptron (multilayer perceptron - MLP) giai đoạn là chỉ ~17
phần trăm của độ trễ (Systems insight: In DLRM, the “Inference” multilayer perceptron (MLP) stage is only ~17 percent of the latency). Phần lớn của thời gian được dành trong sự nhúng các sự tra cứu, việc truy xuất khổng lồ (massive)
128-chiều (dim) các vector từ quy mô-terabyte (terabyte-scale) các bảng (The majority of time is spent in embedding lookups, retrieving massive 128-dim vectors from terabyte-scale tables). Đây là một bộ nhớ-băng thông và giới hạn-công suất (capacity-bound)
khối lượng công việc nơi việc thêm nhiều hơn tính toán không giúp trừ khi sự nhúng các bảng có thể được
phục vụ nhanh hơn (This is a memory-bandwidth and capacity-bound workload where adding more compute does not help unless the embedding tables can be served faster).
Hai ngọn hải đăng các trường hợp minh họa giống nhau chung thất bại chế độ: đơn giản (straightforward) sự tối ưu hóa
các nỗ lực nhắm mục tiêu nơi ML chuyên môn áp dụng (mô hình sự lượng tử hóa, sự cắt tỉa) trong khi việc ràng buộc sự ép buộc
ngồi ở nơi khác (hình ảnh sự giải mã trên CPU cho ResNet-50, sự nhúng-bảng bộ nhớ băng thông cho
DLRM) (The two lighthouse cases illustrate the same general failure mode: straightforward optimization efforts target where ML expertise applies (model quantization, pruning) while the binding constraint sits elsewhere (image decoding on CPU for ResNet-50, embedding-table memory bandwidth for DLRM)). Mẫu khái quát hóa (generalizes): bất kỳ việc phục vụ hệ thống (nào) nơi mô hình chiếm ít hơn một nửa của
tổng độ trễ (sẽ) thấy giảm dần các lợi tức từ (những) chỉ-mô hình các sự tối ưu hóa, bất kể (của) (mức độ) lớn như thế nào
những cá nhân các sự tăng tốc (speedups) đó là (The pattern generalizes: any serving system where the model accounts for less than half of total latency will see diminishing returns from model-only optimizations, regardless of how large those individual speedups are). Amdahl’s Định luật định lượng trần (Amdahl’s Law quantifies the ceiling). Việc áp dụng định lượng
cách tiếp cận tới việc phục vụ phơi bày những ẩn các nút thắt cổ chai này trước khi kỹ thuật nỗ lực bị phân bổ sai (misallocated) (Adopting the quantitative approach to serving exposes these hidden bottlenecks before engineering effort is misallocated).
Khăn ăn Toán học 13.3: Định lượng cách tiếp cận tới việc phục vụ (The quantitative approach to serving)
Amdahl’s Định luật tại (nơi) làm việc (phần D.2.3 cung cấp chính thức sự dẫn xuất (derivation)): sự tiền xử lý (4.5 ms) và
dữ liệu sự truyền (0.5 ms) tiêu thụ 49.5 phần trăm của tổng độ trễ (Amdahl’s Law at work (section D.2.3 provides the formal derivation): preprocessing (4.5 ms) and data transfer (0.5 ms) consume 49.5 percent of total latency). Việc tối ưu hóa mô hình 10× nhanh hơn
(5 ms → 0.5 ms) mang lại chỉ 1.8× đầu cuối-tới-đầu cuối sự tăng tốc (từ 10.1 ms tới 5.6 ms) (Optimizing the model 10× faster (5 ms →0.5 ms) yields only 1.8× end-to-end speedup (from 10.1 ms to 5.6 ms)). Đây là tại sao
việc tập trung một cách độc quyền trên mô hình sự tối ưu hóa (sự lượng tử hóa, sự cắt tỉa) thường gây thất vọng:
nút thắt cổ chai là ở nơi khác (This is why focusing exclusively on model optimization (quantization, pruning) often disappoints: the bottleneck is elsewhere).
DSA tính hiệu quả: Chung-mục đích các CPU đạt được chỉ 1–2 phần trăm của đỉnh hiệu suất tại lô-1
bởi vì lệnh chi phí hoạt động thống trị (DSA efficiency: General-purpose CPUs achieve only 1–2 percent of peak performance at batch-1 because instruction overhead dominates). Các DSA như các TPU và Tensor Các lõi thay thế phức tạp
logic với dày đặc nhân-tích lũy (multiply-accumulate - MAC) các mảng, việc đạt được 10–100× cao hơn số học (arithmetic) cường-
độ (intensity) (DSAs like TPUs and Tensor Cores replace complex logic with dense multiply-accumulate (MAC) arrays, achieving 10–100× higher arithmetic intensity). Điều này làm phần cứng sự gia tốc (thành) một thuộc về kinh tế yêu cầu cho nhiều cao-thông lượng
hay thấp-độ trễ việc phục vụ các khối lượng công việc (This makes hardware acceleration an economic requirement for many high-throughput or low-latency serving workloads).
Các hệ thống sự thấu hiểu: Lập hồ sơ (Profile) trước khi việc tối ưu hóa (Systems insight: Profile before optimizing). Nếu sự tiền xử lý thống trị, được gia tốc-GPU
các đường ống (NVIDIA DALI) có thể vượt trội (outperform) mô hình sự lượng tử hóa (If preprocessing dominates, GPU-accelerated pipelines (NVIDIA DALI) may outperform model quantization).
Việc di chuyển sự tiền xử lý gần hơn tới máy gia tốc có thể giảm thiểu có thể tránh (avoidable) CPU-GPU các sự truyền, nhưng (cái)
đầu cuối-tới-đầu cuối lợi ích là cụ thể-đường ống (pipeline-specific) (Moving preprocessing closer to the accelerator can reduce avoidable CPU-GPU transfers, but the end-to-end gain is pipeline-specific). Hiệu quả sự tối ưu hóa nhắm mục tiêu lớn nhất thời gian (những người) tiêu dùng đầu tiên (Effective optimization targets the largest time consumers first).

13. Mô hình Việc phục vụ (Model Serving)
727
13.4.2.1 Việc phục vụ thuế hóa đơn (The serving tax bill)
Vượt ra ngoài mô hình sự thực thi chính nó, mọi yêu cầu trả một “thuế” (tax) tới việc phục vụ cơ sở hạ tầng (Beyond the model execution itself, every request pays a “tax” to the serving infrastructure). Bảng 13.5
cung cấp đại diện chi phí hoạt động các phạm vi cho một cao-hiệu suất sự suy luận yêu cầu (cho ví dụ, ResNet-
50 sự phân loại) (Table 13.5 gives representative overhead ranges for a high-performance inference request (for example, ResNet-50 classification)).
13.4.2.2 Kẻ giết người các micro giây vấn đề (The killer microseconds problem)
Barroso, Patterson, và các đồng nghiệp (colleagues) (đã) xác định một chí mạng khoảng trống trong cách các hệ thống xử lý độ trễ tại khác biệt
thời gian các quy mô (Barroso, Patterson, and colleagues identified a critical gap in how systems handle latency at different time scales (Barroso et al. 2017)). Các hoạt động trong micro giây phạm vi là quá ngắn cho truyền thống
OS sự lập lịch (thứ mà hoạt động tại mili giây độ chi tiết (granularity)) tuy nhiên quá dài để đơn giản quay-đợi (spin-wait) mà không có
việc lãng phí CPU các chu kỳ (Operations in the microsecond range are too short for traditional OS scheduling (which operates at millisecond granularity) yet too long to simply spin-wait without wasting CPU cycles). Này “kẻ giết người các micro giây” chế độ (regime) quan trọng trong hiện đại việc phục vụ các khối lượng công việc (This “killer microseconds” regime matters in modern serving workloads).
Việc sử dụng đại diện các phạm vi trong bảng 13.5, sự tuần tự hóa tại 50–500 μs, sự phân phối tại 10–50 μs, và
dữ liệu bản sao tại 100–500 μs là mỗi (cái) một cách cá nhân (individually) nhỏ, nhưng cho một 5 ms sự suy luận dịch vụ, những được nêu tên
quy mô-micro giây (microsecond-scale) các chi phí hoạt động này một cách tập thể tiêu thụ khoảng 3.2 phần trăm tới 21 phần trăm của độ trễ
ngân sách trước khi mạng và việc xếp hàng đợi các sự chậm trễ được tính (Using the representative ranges in table 13.5, serialization at 50–500 μs, dispatch at 10–50 μs, and data copy at 100–500 μs are each individually small, but for a 5 ms inference service, these named microsecond-scale overheads collectively consume about 3.2 percent to 21 percent of the latency budget before network and queuing delays are counted). Không đơn chi phí hoạt động (nào) biện minh (cho) sự tối ưu hóa
trong sự cô lập, tuy nhiên cùng nhau chúng xác định liệu hệ thống đáp ứng của nó SLO (hay không) (No single overhead justifies optimization in isolation, yet together they determine whether the system meets its SLO).
Bảng 13.5: Việc phục vụ Thuế Hóa đơn: Một đại diện sự cố của phi sự suy luận (noninference) độ trễ các nguồn (The Serving Tax Bill: A representative breakdown of noninference latency sources). Trong khi cá nhân các thành phần
như sự tuần tự hóa có vẻ nhỏ (< 1 ms), chúng cộng gộp (While individual components like serialization seem small (< 1 ms), they compound). Trong một 5 ms sự suy luận dịch vụ, này “thuế” có thể dễ dàng tiêu thụ 50 phần trăm của
độ trễ ngân sách (In a 5 ms inference service, this “tax” can easily consume 50 percent of the latency budget). Chính kỹ thuật mục tiêu là để giảm thiểu những các chi phí này thông qua thuộc về kiến trúc các sự lựa chọn như nhị phân các giao thức,
dai dẳng các kết nối, và không-bản sao dữ liệu các con đường (The primary engineering goal is to reduce these costs through architectural choices like binary protocols, persistent connections, and zero-copy data paths).
Thuế Thành phần (Tax Component)
Điển hình Chi phí (Typical Cost)
Sự mở rộng Hành vi (Scaling Behavior)
Thuế Sự trốn tránh (Evasion) Chiến lược
Mạng I/O
1-5 ms
Tuyến tính với tải trọng
Sự nén, Vùng Sự sắp xếp cùng chỗ (Colocation)
Sự tuần tự hóa
50–500 𝜇s
Tuyến tính với tải trọng
gRPC/Protobuf (so với JSON)
Việc xếp hàng đợi
0.1-10 ms
Theo cấp số nhân (Exponential) với/ tải
Động Việc tạo lô, Tự động mở rộng (Autoscaling)
Sự phân phối (Dispatch)
10–50 𝜇s
Hằng số (Constant) mỗi lô
Hạt nhân Sự hợp nhất (Kernel Fusion) (việc giảm thiểu các sự khởi chạy (launches))
Dữ liệu Bản sao (Data Copy)
100–500 𝜇s
Tuyến tính với tensor
Không-Bản sao/Được chia sẻ Bộ nhớ
Độ trễ ngân sách bộ khung cung cấp một có hệ thống (systematic) cách tiếp cận tới này cộng gộp vấn đề (The latency budget framework provides a systematic approach to this compound problem). Sự đo-
lường đến (trước) tiên: không có mỗi-giai đoạn sự trang bị (instrumentation), các kỹ sư không thể phân biệt (distinguish) một sự tiền xử-
lý nút thắt cổ chai khỏi một sự tuần tự hóa nút thắt cổ chai, và sự tối ưu hóa nỗ lực bị phân bổ sai tới
nhất có thể nhìn thấy thành phần (mô hình) thay vì (cái) đắt nhất một (cái) (Measurement comes first: without per-phase instrumentation, engineers cannot distinguish a preprocessing bottleneck from a serialization bottleneck, and optimization effort gets misallocated to the most visible component (the model) rather than the most expensive one). Một khi sự đo lường tiết lộ
thực sự sự phân phối của thời gian, kỹ thuật nỗ lực nên chảy một cách tương ứng (proportionally)—một giai đoạn việc tiêu thụ
50 phần trăm của độ trễ xứng đáng (nhiều) hơn sự chú ý (hơn) so với một (giai đoạn) việc tiêu thụ 5 phần trăm, bất kể (của) (giai đoạn) nào
cảm thấy dễ kiểm soát (tractable) hơn (Once measurement reveals the true distribution of time, engineering effort should flow proportionally—a phase consuming 50 percent of latency deserves more attention than one consuming 5 percent, regardless of which feels more tractable). Thuộc về kiến trúc các sự thay đổi như được gia tốc-GPU sự tiền xử lý hay quyết liệt (aggressive)
việc tạo lô có thể dịch chuyển công việc giữa các giai đoạn hoàn toàn, đôi khi việc loại bỏ một nút thắt cổ chai thay vì
đơn thuần việc giảm thiểu nó (Architectural changes such as GPU-accelerated preprocessing or aggressive batching can shift work between phases entirely, sometimes eliminating a bottleneck rather than merely reducing it).
13.4.3 Độ phân giải và đầu vào kích thước các sự đánh đổi (Resolution and input size trade-offs)
Đầu vào độ phân giải ảnh hưởng cả hai sự tiền xử lý và sự suy luận độ trễ, nhưng mối quan hệ khác biệt (khác nhau) tùy thuộc (vào)
việc liệu hệ thống là giới hạn-tính toán (bị giới hạn bởi số học thông lượng) hay giới hạn-bộ nhớ (memory-bound)
(bị giới hạn bởi dữ liệu sự di chuyển) (Input resolution affects both preprocessing and inference latency, but the relationship differs depending on whether the system is compute bound (limited by arithmetic throughput) or memory-bound (limited by data movement)). Một giới hạn-tính toán hệ thống chậm lại một cách tương ứng (proportionally) đối với được làm tăng sự tính-
toán; một giới hạn-bộ nhớ hệ thống có thể cho thấy tối thiểu sự chậm lại (slowdown) nếu kích hoạt các tensor vẫn khớp trong nhanh
bộ nhớ (A compute-bound system slows proportionally to increased computation; a memory-bound system may show minimal slowdown if activation tensors still fit in fast memory). Đường mái nhà (roofline) sự phân tích trong phần 11.6 phát triển này sự khác biệt trong chiều sâu (depth), việc làm nó (trở nên) thiết yếu
cho được cung cấp thông tin (informed) độ phân giải các quyết định (The roofline analysis in section 11.6 develops this distinction in depth, making it essential for informed resolution decisions).
Cho giới hạn-tính toán các mô hình, phương trình 13.1 chính thức hóa cách thông lượng mở rộng một cách nghịch đảo (inversely) với
độ phân giải bình phương (squared):
Thông lượng(𝑟2)/Thông lượng(𝑟1) = (𝑟1/𝑟2)^2 (13.1)
Việc nhân đôi độ phân giải từ 224 tới 448 theo lý thuyết (theoretically) mang lại 4× sự chậm lại (được đo lường: 3.6× do cố định
chi phí hoạt động sự khấu hao (amortization)) (Doubling resolution from 224 to 448 theoretically yields 4× slowdown (measured: 3.6× due to fixed overhead amortization)). Cao hơn độ phân giải cũng dịch chuyển tính toán-bộ nhớ (sự) cân bằng, nhưng hướng tới
tính toán: mọi tích chập trọng số được tái sử dụng qua nhiều hơn không gian các vị trí, do đó các FLOP và sự kích hoạt
lưu lượng truy cập cả hai phát triển theo phương trình bậc hai (quadratically) trong khi cố định trọng số lưu lượng truy cập được khấu hao, và số học cường độ
tăng (rises) xa hơn bên trên đường mái nhà rãnh (ridge) điểm (Higher resolution also shifts the compute-memory balance, but toward compute: every convolution weight is reused across more spatial positions, so FLOPs and activation traffic both grow quadratically while the fixed weight traffic is amortized, and arithmetic intensity rises further above the roofline ridge point). Việc phục vụ các chi phí của độ phân giải là bậc hai (quadratic) độ trễ
sự phát triển và bậc hai sự kích hoạt-bộ nhớ áp lực, không (phải) một băng thông nút thắt cổ chai (The serving costs of resolution are quadratic latency growth and quadratic activation-memory pressure, not a bandwidth bottleneck).

728
13.4 Yêu cầu Vòng đời (Request Lifecycle)
Bảng 13.6 định lượng này sự chuyển tiếp cho ResNet-50.
Bảng 13.6: Độ phân giải và Tính toán Nút thắt cổ chai (Resolution and Compute Bottleneck): ResNet-50 số học cường độ tăng với độ phân giải: các FLOP và sự kích hoạt
lưu lượng truy cập phát triển theo phương trình bậc hai trong khi cố định trọng số lưu lượng truy cập được khấu hao trên nhiều hơn không gian các vị trí (ResNet-50 arithmetic intensity rises with resolution: FLOPs and activation traffic grow quadratically while the fixed weight traffic is amortized over more spatial positions). Cho một V100 PCIe (14 TFLOP/s
FP32; SXM2 biến thể chạy 15.7 TFLOP/s FP32) với 900 GB/s của HBM2 bộ nhớ băng thông, rãnh điểm là xấp xỉ
15.6 FLOP/byte; mọi hàng ngồi bên trên nó, do đó cao hơn độ phân giải lái (drives) khối lượng công việc sâu hơn vào giới hạn-tính toán chế độ (regime) (For a V100 PCIe (14 TFLOP/s FP32; the SXM2 variant runs 15.7 TFLOP/s FP32) with 900 GB/s of HBM2 memory bandwidth, the ridge point is approximately 15.6 FLOP/byte; every row sits above it, so higher resolution drives the workload deeper into the compute-bound regime).
Việc phục vụ các chi phí của độ phân giải là bậc hai độ trễ và sự kích hoạt-bộ nhớ sự phát triển, không (phải) bộ nhớ băng thông (The serving costs of resolution are quadratic latency and activation-memory growth, not memory bandwidth).
Độ phân giải
Sự kích hoạt Kích thước
Số học Cường độ (Arith. Intensity)
Nút thắt cổ chai
224×224
12.5 MB
32.2 FLOP/byte
Tính toán
384×384
36.7 MB
68.5 FLOP/byte
Tính toán
512×512
65.3 MB
91.9 FLOP/byte
Tính toán
640×640
102.0 MB
109.2 FLOP/byte
Tính toán
13.4.3.1 Độ phân giải các chiến lược trong sản xuất
Khác biệt sự triển khai các ngữ cảnh áp đặt khác biệt độ phân giải các yêu cầu được định hình bởi (những) thống trị
các sự ép buộc của chúng (Different deployment contexts impose distinct resolution requirements shaped by their dominant constraints). Di động các ứng dụng thường chấp nhận thấp hơn độ phân giải (224×224) cho đối tượng sự phát hiện trong
camera các kính ngắm (viewfinders), nơi độ trễ và pin tuổi thọ lớn hơn (outweigh) biên (marginal) độ chính xác các lợi ích (Mobile applications often accept lower resolution (224×224) for object detection in camera viewfinders, where latency and battery life outweigh marginal accuracy gains). Y tế
việc tạo hình ảnh (imaging) ngồi tại (cái) đối diện cực đoan, việc yêu cầu 512×512 hay cao hơn cho chẩn đoán độ chính xác, với
được nới lỏng độ trễ các yêu cầu thứ mà cho phép (permit) bổ sung tính toán (Medical imaging sits at the opposite extreme, requiring 512×512 or higher for diagnostic accuracy, with relaxed latency requirements that permit the additional compute). Tự trị các phương tiện (vehicles) chia (split)
sự khác biệt bằng cách việc sử dụng nhiều các độ phân giải cho khác biệt các tác vụ: thấp độ phân giải cho nhanh chóng sự phát hiện qua
rộng các trường (fields) của góc nhìn (view) và cao-độ phân giải các phần cắt (crops) cho mịn-hạt (fine-grained) sự nhận diện (recognition) của được phát hiện các đối tượng (Autonomous vehicles split the difference by using multiple resolutions for different tasks: low resolution for rapid detection across wide fields of view and high-resolution crops for fine-grained recognition of detected objects). Đám mây
các API đối mặt (với) (một) thách thức khác (yet another)—chúng điển hình nhận các hình ảnh tại bất cứ độ phân giải (nào) máy khách
tải lên và phải xử lý (cái) dẫn đến phạm vi một cách tinh tế (gracefully) (Cloud APIs face yet another challenge—they typically receive images at whatever resolution the client uploads and must handle the resulting range gracefully). Tính biến đổi này làm đám mây các API (trở thành) lý tưởng
các ứng cử viên cho thích ứng độ phân giải các chiến lược, nơi hệ thống chọn độ phân giải một cách linh hoạt (dynamically) dựa
trên nội dung các đặc điểm (This variability makes cloud APIs ideal candidates for adaptive resolution strategies, where the system selects resolution dynamically based on content characteristics).
13.4.3.2 Thích ứng độ phân giải (Adaptive resolution)
Thích ứng độ phân giải để (cho) sản xuất các hệ thống chọn độ phân giải một cách linh hoạt dựa trên nội dung (Adaptive resolution lets production systems select resolution dynamically based on content). Một
cách tiếp cận chạy một nhẹ bộ phân loại tại 128×128 để phân loại (categorize) nội dung kiểu, sau đó chọn tác vụ-
thích hợp độ phân giải với các tài liệu tại 512×512, các phong cảnh tại 224×224, và các khuôn mặt tại 384×384 (One approach runs a lightweight classifier at 128×128 to categorize content type, then selects task-appropriate resolution with documents at 512×512, landscapes at 224×224, and faces at 384×384).
Điều này đạt được 1.4× thông lượng sự cải thiện với 99.2 phần trăm độ chính xác sự giữ lại so với cố định cao độ phân-
giải (This achieves 1.4× throughput improvement with 99.2 percent accuracy retention vs. fixed high resolution). Này mẫu đánh đổi sự tiền xử lý chi phí từ việc chạy nhẹ bộ phân loại cho sự suy luận
các khoản tiết kiệm trên chính (main) mô hình (This pattern trades preprocessing cost from running the lightweight classifier for inference savings on the main model).
Độ trễ sự phân tích cho đến nay (đã) tập trung trên tuần tự việc xử lý: một yêu cầu việc hoàn thành trước khi
(cái) tiếp theo bắt đầu (The latency analysis so far has focused on sequential processing: one request completing before the next begins). Sự tiền xử lý, sự suy luận, và sự hậu xử lý các giai đoạn sử dụng khác biệt phần cứng
các tài nguyên (The preprocessing, inference, and postprocessing stages use different hardware resources). Sự tách biệt này tạo ra một cơ hội để xử lý nhiều các yêu cầu một cách đồng thời (simultaneously).
13.4.4 Phần cứng sự sử dụng và yêu cầu việc tạo đường ống (Hardware utilization and request pipelining)
Việc tối ưu hóa mỗi yêu cầu giai đoạn trong sự cô lập bỏ lỡ một chí mạng cơ hội: các giai đoạn sử dụng khác biệt
phần cứng các tài nguyên (Optimizing each request stage in isolation misses a critical opportunity: the stages use different hardware resources). Độ trễ ngân sách sự phân tích trong phần 13.4.1 tiết lộ rằng mô hình sự suy luận là
chỉ một thành phần của yêu cầu vòng đời (The latency budget analysis in section 13.4.1 reveals that model inference is only one component of the request lifecycle). Từ một phần cứng góc nhìn, chính mục tiêu của một
việc phục vụ hệ thống là để tối đa hóa chu kỳ làm việc (duty cycle) của máy gia tốc, tỷ lệ phần trăm của thời gian (mà) GPU là (đang)
thực hiện hữu ích sự tính toán (From a hardware perspective, the primary goal of a serving system is to maximize the duty cycle of the accelerator, the percentage of time the GPU is performing useful computation).
Trong một được tuần tự hóa việc phục vụ hệ thống, phần cứng ngồi rảnh rỗi trong suốt mạng I/O và dựa trên-CPU sự tiền-
xử lý (In a serialized serving system, the hardware sits idle during network I/O and CPU-based preprocessing). Cao-hiệu suất việc phục vụ các hệ thống sử dụng Yêu cầu Việc tạo đường ống (Request Pipelining) để chồng chéo (overlap) những các giai đoạn này,
việc đảm bảo (rằng) GPU được cho ăn (fed) một liên tục luồng của các tensor (High-performance serving systems use Request Pipelining to overlap these stages, ensuring the GPU is fed a continuous stream of tensors).
13.4.4.1 Việc chồng chéo I/O và tính toán (Overlapping I/O and compute)
Hai định thời (timing) các sơ đồ trong hình 13.5 minh họa tác động của việc tạo đường ống (The two timing diagrams in figure 13.5 illustrate the impact of pipelining). Trong tuần tự (serial) trường hợp (A),
mỗi yêu cầu phải hoàn thành toàn bộ vòng đời của nó (Mạng → CPU Sự tiền xử lý → GPU Sự suy luận →
Sự hậu xử lý) trước khi tiếp theo yêu cầu bắt đầu, và xám rảnh rỗi các khoảng trống (gaps) để GPU không được sử dụng (unused) cho
nhiều hơn 50 phần trăm của thời gian (In the serial case (A), each request must complete its entire lifecycle (Network →CPU Preprocessing →GPU Inference →Postprocessing) before the next request begins, and the grey idle gaps leave the GPU unused for more than 50 percent of the time). Trong được tạo đường ống (pipelined) trường hợp (B), những các khoảng trống đó biến mất.
Việc tạo đường ống được kích hoạt bởi không đồng bộ I/O và tính đồng thời các mô hình mẫu (Pipelining is enabled by asynchronous I/O and concurrency models). Thay vì việc chờ đợi cho một
GPU hạt nhân kết thúc (finish), máy chủ’s CPU luồng đệ trình công việc tới GPU’s lệnh hàng đợi và
ngay lập tức bắt đầu việc tiền xử lý (cái) tiếp theo đến (incoming) yêu cầu (Instead of waiting for a GPU kernel to finish, the server’s CPU thread submits the work to the GPU’s command queue and immediately begins preprocessing the next incoming request).

13. Mô hình Việc phục vụ (Model Serving)
729
Sự tiền (xử lý) (Pre)
GPU
Rảnh rỗi
Sự tiền
GPU
Sự tiền 1
Sự tiền 2
Sự tiền 3
Sự tiền 4
GPU 1
GPU 2
GPU 3
GPU 4
A. Tuần tự Sự thực thi (Thấp Sự sử dụng) (Serial Execution (Low Utilization))
B. Được tạo đường ống Sự thực thi (Cao Sự sử dụng) (Pipelined Execution (High Utilization))
Hình 13.5: Yêu cầu Việc tạo đường ống: Việc tạo đường ống giấu độ trễ bằng cách việc chồng chéo độc lập các hoạt động qua khác biệt phần cứng
các tài nguyên (Request Pipelining: Pipelining hides latency by overlapping independent operations across different hardware resources). Trong được tạo đường ống sự thực thi (B), CPU xử lý (cái) tiếp theo yêu cầu’s dữ liệu trong khi GPU thực thi (cái) hiện tại yêu cầu’s
sự suy luận (In pipelined execution (B), the CPU processes the next request’s data while the GPU executes the current request’s inference). Điều này làm tăng GPU chu kỳ làm việc hướng tới 100 phần trăm, một cách hiệu quả việc nhân đôi hay nhân ba thông lượng trên giống nhau
phần cứng mà không có việc thay đổi mô hình (This increases the GPU duty cycle toward 100 percent, effectively doubling or tripling throughput on the same hardware without changing the model).
13.4.4.2 Các hệ thống số liệu: Phần cứng chu kỳ làm việc (The systems metric: Hardware duty cycle)
Trong “Định lượng Cách tiếp cận” tới ML các hệ thống, chúng ta định nghĩa hệ thống tính hiệu quả như là khả năng của một việc phục vụ
hệ thống để bão hòa nút thắt cổ chai tài nguyên (In the “Quantitative Approach” to ML systems, we define system efficiency as the ability of a serving system to saturate the bottleneck resource). Cho hầu hết ML các hệ thống, điều này là GPU’s tính toán các lõi hay
bộ nhớ băng thông. Chúng ta định lượng điều này trong phương trình 13.2:
Hệ thống Tính hiệu quả = ∑𝑇tính toán / (Bức tường Đồng hồ Thời gian × Tài nguyên Số đếm) (13.2)
Nếu một ResNet-50 yêu cầu tốn 10 ms tổng cộng (5 ms GPU, 5 ms CPU), một tuần tự hệ thống đạt được chỉ 50
phần trăm tính hiệu quả (If a ResNet-50 request takes 10 ms total (5 ms GPU, 5 ms CPU), a serial system achieves only 50 percent efficiency). Bằng cách việc tạo đường ống chỉ hai các yêu cầu, tính hiệu quả tiếp cận 100 phần trăm (việc giả định
CPU có thể theo kịp với GPU) (By pipelining just two requests, efficiency approaches 100 percent (assuming the CPU can keep up with the GPU)). Nếu CPU là quá chậm để cho GPU ăn, hệ thống trở nên
giới hạn-CPU, và xa hơn (further) mô hình sự tối ưu hóa cung cấp không (zero) thông lượng lợi ích (If the CPU is too slow to feed the GPU, the system becomes CPU-bound, and further model optimization provides zero throughput gain). Điều này là Amdahl’s Định luật
từ phần D.2.3 được áp dụng cho việc phục vụ: nếu sự tiền xử lý tiêu thụ 50 phần trăm của độ trễ, tối đa
sự tăng tốc là 2× bất kể (của) (mức độ) nhanh như thế nào mô hình chạy (This is Amdahl’s Law from section D.2.3 applied to serving: if preprocessing consumes 50 percent of latency, maximum speedup is 2× regardless of how fast the model runs). Phần cứng quỹ đạo (trajectory) làm này trần (ceiling)
(trở nên) dần dần chặt chẽ hơn (The hardware trajectory makes this ceiling progressively tighter). Máy gia tốc tính toán thông lượng (FLOPs) (đã) phát triển xa nhanh hơn (so với) CPU
đơn-luồng (single-thread) hiệu suất qua liên tiếp (successive) phần cứng các thế hệ, do đó sự suy luận phần của
đường ống thu hẹp lại trong khi giới hạn-CPU sự tiền xử lý phần duy trì không bị thay đổi (Accelerator compute throughput (FLOPs) has grown far faster than CPU single-thread performance across successive hardware generations, so the inference portion of the pipeline shrinks while the CPU-bound preprocessing portion remains unchanged). Một hệ thống thứ mà
đã (là) giới hạn-tính toán trên một cũ hơn máy gia tốc có thể trở nên giới hạn-CPU sau một phần cứng sự nâng cấp—không (phải)
bởi vì sự tiền xử lý (trở nên) chậm hơn, nhưng bởi vì mô hình (trở nên) một cách quyết liệt nhanh hơn trong khi CPU (thì)
không (A system that was compute-bound on an older accelerator may become CPU-bound after a hardware upgrade—not because preprocessing got slower, but because the model got dramatically faster while the CPU did not).
13.4.5 Sự hậu xử lý
Yêu cầu vòng đời kết luận (concludes) với sự hậu xử lý, giai đoạn thứ mà biến đổi mô hình các đầu ra thành
có thể hành động (actionable) các kết quả (The request lifecycle concludes with postprocessing, the phase that transforms model outputs into actionable results). Một nơ-ron mạng tạo ra thô các tensor (dấu phẩy-động các mảng thứ mà mang không
vốn có (inherent) ý nghĩa đối với các ứng dụng hay những người dùng) (A neural network produces raw tensors (floating-point arrays that carry no inherent meaning to applications or users)). Một 0.95 xác suất trở thành một tự tin “con chó” (dog) nhãn chỉ
sau khi sự hậu xử lý chuyển đổi nó; một chuỗi (sequence) của mã thông báo các ID trở thành có thể đọc văn bản; một hộp giới hạn (bounding box)
tensor trở thành một được làm nổi bật vùng trong một hình ảnh (A 0.95 probability becomes a confident “dog” label only after postprocessing converts it; a sequence of token IDs becomes readable text; a bounding box tensor becomes a highlighted region in an image). Sự hậu xử lý một cách đáng kể tác động cả hai độ trễ
và sự hữu ích (usefulness) của các dự đoán (Postprocessing significantly impacts both latency and the usefulness of predictions).
13.4.5.1 Từ các logit tới các dự đoán
Sự phân loại các mô hình (đưa) đầu ra các logit hay các xác suất qua các lớp (Classification models output logits or probabilities across classes). Việc chuyển đổi những thô các đầu ra này
thành các dự đoán bao gồm một vài các bước (Converting these raw outputs to predictions involves several steps). (Cái) đơn giản nhất là argmax sự lựa chọn (selection), thứ mà trả về (cái) cao nhất-
xác suất lớp (The simplest is argmax selection, which returns the highest-probability class). Việc tạo ngưỡng (Thresholding) áp dụng một sự tự tin sự cắt đứt (cutoff), việc trả về các dự đoán chỉ khi
mô hình là đủ chắc chắn (Thresholding applies a confidence cutoff, returning predictions only when the model is sufficiently certain). Top-𝑘 sự trích xuất trả về nhiều cao-xác suất các lớp với (của) chúng
các điểm số, hữu ích khi các ứng dụng cần được xếp hạng (ranked) các lựa chọn thay thế (Top-𝑘 extraction returns multiple high-probability classes with their scores, useful when applications need ranked alternatives). Sự hiệu chuẩn (Calibration) điều chỉnh thô các xác suất
để phản ánh tốt hơn thực sự các khả năng (likelihoods), một bước thứ mà thêm sự tính toán nhưng là thiết yếu khi xuôi dòng (downstream)
các hệ thống đưa ra các quyết định dựa trên sự tự tin các điểm số (Calibration adjusts raw probabilities to better reflect true likelihoods, a step that adds computation but is essential when downstream systems make decisions based on confidence scores). Cho ResNet-50 hình ảnh sự phân loại, danh sách 13.1
cho thấy đầy đủ sự hậu xử lý con đường từ thô các logit tới một sẵn sàng-API (API-ready) phản hồi, bao gồm xác suất
sự chuẩn hóa (normalization), top-𝑘 sự trích xuất, nhãn sự tra cứu, và phản hồi việc định dạng (For ResNet-50 image classification, listing 13.1 shows the full postprocessing path from raw logits to an API-ready response, including probability normalization, top-𝑘 extraction, label lookup, and response formatting).
Cho này ví dụ, tổng cộng sự hậu xử lý thời gian là xấp xỉ 0.1 ms, không đáng kể (negligible) (khi được) so sánh với
sự tiền xử lý và sự suy luận (For this example, total postprocessing time is approximately 0.1 ms, negligible compared to preprocessing and inference). Mỗi bước thêm độ trễ nhưng cải thiện phản hồi tiện ích (utility) (Each step adds latency but improves response utility). Sự hiệu chuẩn

13. Mô hình Việc phục vụ (Model Serving)
730
13.5 Xếp hàng đợi Lý thuyết (Queuing Theory)
9
Little’s Định luật:
John D. C. Little (đã) chứng minh vào năm 1961 rằng
𝑄yêu cầu (req) = 𝜆đến (arr)𝑇độ trễ (lat) đúng cho bất kỳ
ổn định hệ thống (nào) bất kể (của)
đến (arrival) sự phân phối, dịch vụ
sự phân phối, hay sự lập lịch
kỷ luật (discipline). Tính phổ-
quát (universality) này là tại sao nó neo (anchors) ML
công suất việc lập kế hoạch: công-
thức không yêu cầu các giả định
về (việc) liệu các yêu cầu (có) đến
trong các đợt (bursts), liệu sự suy-
luận các thời gian (có) thay đổi, hay liệu
bộ lập lịch tạo lô (một cách) quyết-
liệt (hay không). Duy nhất yêu cầu
là sự ổn định (𝜆arr < 𝜇), và
khi đó điều kiện phá vỡ,
không (có) lượng của sự tối ưu hóa (nào)
ngăn cản hàng đợi sự phân kỳ (divergence).
nói riêng có thể thêm đáng kể sự tính toán nhưng là cần thiết khi xuôi dòng các hệ thống đưa ra
các quyết định dựa trên sự tự tin các điểm số (in particular can add significant computation but is necessary when downstream systems make decisions based on confidence scores).
13.4.5.2 Đầu ra việc định dạng (Output formatting)
Sản xuất các hệ thống hiếm khi trả về thô các dự đoán (Production systems rarely return raw predictions). Các đầu ra phải tuân thủ (conform) tới API các hợp đồng (contracts) thứ mà
chỉ định JSON sự tuần tự hóa các lược đồ (schemas), sự tự tin điểm số việc định dạng, và việc tạo ngưỡng các quy tắc (Outputs must conform to API contracts that specify JSON serialization schemas, confidence score formatting, and thresholding rules). Lỗi
việc xử lý (handling) phải giải quyết cạnh (edge) các trường hợp: hệ thống phải định nghĩa hành vi khi không dự đoán (nào) vượt quá
sự tự tin ngưỡng hay khi đầu vào xuất hiện ngoài-phân phối (out-of-distribution) (Error handling must address edge cases: the system must define behavior when no prediction exceeds the confidence threshold or when the input appears out-of-distribution). Phản hồi siêu dữ liệu (mô hình
phiên bản, sự suy luận thời gian, tính năng các sự quy kết (attributions)) kích hoạt xuôi dòng sự giám sát và việc gỡ lỗi (Response metadata (model version, inference time, feature attributions) enables downstream monitoring and debugging).
Danh sách 13.1: ResNet-50 Sự hậu xử lý: Biến đổi thô các logit thành được hiệu chuẩn các xác suất, trích xuất top-𝑘 các dự đoán, và định dạng
API phản hồi (ResNet-50 Postprocessing: Transforms raw logits to calibrated probabilities, extracts top-𝑘 predictions, and formats the API response).
# Biến đổi thô các logit thành được hiệu chuẩn các xác suất
# Đầu vào: các logit tensor của hình dạng (lô_kích thước (batch_size), 1000) - một điểm số mỗi
# ImageNet lớp
các xác suất (probs) = torch.softmax(
các logit, chiều (dim)=-1
)
# Chuẩn hóa để tổng=1; ~0.05 ms trên GPU
# Trích xuất top-5 các dự đoán cho nhiều-lớp (multi-class) phản hồi
# topk trả về (các giá trị, các chỉ số) được sắp xếp bởi xác suất
top5_probs, top5_indices = probs.topk(5)
# ~0.02 ms; GPU hoạt động
top5_probs = top5_probs.squeeze(0).tolist()
top5_indices = top5_indices.squeeze(0).tolist()
# Ánh xạ lớp các chỉ số (indices) sang có thể đọc-bởi con người các nhãn
# imagenet_labels: danh sách của 1000 lớp các tên từ synset ánh xạ
các nhãn (labels) = [
imagenet_labels[i] cho (for) i trong top5_indices
]
# ~0.01 ms; CPU sự tra cứu
# Định dạng phản hồi với các dự đoán và siêu dữ liệu cho API hợp đồng
phản hồi = {
"các dự đoán": [
{"nhãn": nhãn, "sự tự tin": float(xác suất)}
cho nhãn, xác suất trong zip(các nhãn, top5_probs)
],
"mô hình_phiên bản": "resnet50-v2.1",
# Phía máy khách (Client-side) phiên bản việc theo dõi
"sự suy luận_thời gian_ms": 5.2,
# Khả năng quan sát (Observability) cho độ trễ sự giám sát
}
Độ trễ ngân sách sự phân tích tiết lộ nơi thời gian đi (đến) bên trong một đơn yêu cầu (The latency budget analysis reveals where time goes within a single request). Sản xuất các hệ thống,
tuy nhiên, không xử lý các yêu cầu trong sự cô lập: chúng phải xử lý hàng trăm hay hàng ngàn của đồng-
thời các yêu cầu (đang) cạnh tranh cho hữu hạn các tài nguyên (Production systems, however, do not process requests in isolation: they must handle hundreds or thousands of concurrent requests competing for finite resources). Việc hiểu này tính đồng thời yêu cầu một khác biệt
thuộc về phân tích (analytical) bộ khung (Understanding this concurrency requires a different analytical framework).
13.5 Việc xếp hàng đợi Lý thuyết (Queuing Theory)
Trong sản xuất, đồng thời các yêu cầu cạnh tranh cho hữu hạn các tài nguyên, và việc xếp hàng đợi lý thuyết dự đoán cách
sự cạnh tranh này ảnh hưởng độ trễ (In production, concurrent requests compete for finite resources, and queuing theory predicts how this competition affects latency). Những các nguyên tắc này giải thích phản trực giác (counterintuitive) hành vi (thứ) mà gây ra
được cung cấp-tốt (well-provisioned) các hệ thống vi phạm độ trễ các SLO khi tải tăng một cách khiêm tốn (modestly) (These principles explain the counterintuitive behavior that causes well-provisioned systems to violate latency SLOs when load increases modestly).
13.5.1 Little’s Định luật
Việc phục vụ các kỹ sư một cách thường xuyên (routinely) đối mặt (với) một cụ thể công suất quyết định: (được) cho một độ trễ SLO và một được mong đợi
yêu cầu tỷ lệ, hệ thống phải xác định bao nhiêu đang bay (in-flight) công việc nó phải giữ trước khi việc quyết định
bao nhiêu các GPU để cung cấp (Serving engineers routinely face a concrete capacity decision: given a latency SLO and an expected request rate, the system must determine how much in-flight work it has to hold before deciding how many GPUs to provision). Little’s Định luật (phần D.2.4) trả lời (câu) đầu tiên câu hỏi bằng cách việc liên hệ (relating)
hàng đợi độ sâu (depth) tới thông lượng (Little’s Law (section D.2.4) answers the first question by relating queue depth to throughput). M/M/1 mô hình sau đó trả lời (câu) thứ hai bằng cách việc dự đoán cách độ trễ
suy giảm (degrades) dưới tải (The M/M/1 model later answers the second by predicting how latency degrades under load). Cùng nhau, chúng cung cấp định lượng bộ khung cho công suất việc lập kế hoạch (Together, they provide the quantitative framework for capacity planning).

13. Mô hình Việc phục vụ
731
Việc phục vụ các kỹ sư cần một công cụ (thứ) mà kết nối có thể quan sát (observable) các số liệu với công suất các yêu cầu (Serving engineers need a tool that connects observable metrics to capacity requirements). (Cái)
được tán dương nhất kết quả trong việc xếp hàng đợi lý thuyết là Little’s Định luật,9 thứ mà phương trình 13.3 thể hiện như một đơn giản
mối quan hệ giữa ba các đại lượng (quantities) trong bất kỳ ổn định hệ thống (nào) (The most celebrated result in queuing theory is Little’s Law,9 which equation 13.3 expresses as a simple relationship between three quantities in any stable system):
𝑄req = 𝜆arr ⋅𝑇lat (13.3)
nơi 𝑄req là trung bình số lượng của các yêu cầu trong hệ thống, 𝜆arr là đến (arrival) tỷ lệ (các yêu cầu mỗi
giây), và 𝑇lat là trung bình thời gian mỗi yêu cầu dành trong hệ thống (where 𝑄req is the average number of requests in the system, 𝜆arr is the arrival rate (requests per second), and 𝑇lat is the average time each request spends in the system).
Một cách cụ thể, một máy chủ việc nhắm mục tiêu 1000 QPS với một 50 ms SLO có thể dịch (chuyển) đó cặp một cách trực tiếp thành
số lượng của đồng thời yêu cầu các khe (slots) nó phải giữ trong bộ nhớ, cứng sàn (floor) cho sự kích hoạt lưu trữ trên
đó nút; được làm việc ví dụ bên dưới thực hiện đó sự tính toán (Concretely, a server targeting 1000 QPS with a 50 ms SLO can translate that pair directly into the number of concurrent request slots it must hold in memory, the hard floor for activation storage on that node; the worked example below carries out that calculation).
Các hệ thống Góc nhìn 13.4: Ký hiệu cảnh báo: L so với độ trễ (Notation alert: L vs. latency)
Trong việc xếp hàng đợi lý thuyết, 𝑇lat biểu thị phản hồi thời gian hay thời gian trong hệ thống mỗi yêu cầu; chỉ-hàng đợi (queue-only) việc chờ đợi
thời gian là 𝑊𝑞 (In queuing theory, 𝑇lat denotes the response time or time in system per request; queue-only waiting time is 𝑊𝑞). Cuốn sách này sử dụng 𝑄req cho trung bình trong-hệ thống (in-system) yêu cầu số đếm, 𝜆arr cho đến tỷ lệ,
và 𝜌serv = 𝜆arr/𝜇 cho việc phục vụ sự sử dụng (This book uses 𝑄req for the average in-system request count, 𝜆arr for arrival rate, and 𝜌serv = 𝜆arr/𝜇 for serving utilization). Các chỉ số dưới (subscripts) phân biệt việc xếp hàng đợi ký hiệu từ
sự suy giảm (degradation) phương trình’s 𝜆độ nhạy (sensitivity) tham số và giữ việc phục vụ sự sử dụng khỏi việc chiếm đóng (occupying)
trần (bare) 𝜌 (The subscripts distinguish queueing notation from the degradation equation’s 𝜆sensitivity parameter and keep serving utilization from occupying bare 𝜌). Trong độ trễ-ngân sách các phương trình bên dưới, mang tính mô tả 𝐿lat,* các thuật ngữ gọi tên các thành phần của
ngân sách, như việc chờ đợi và tính toán (In the latency-budget equations below, descriptive 𝐿lat,* terms name components of the budget, such as waiting and compute). Trong việc tạo lô sự phân tích tiếp theo (phần 13.7.3),
𝐿lat,wait tương ứng với việc xếp hàng đợi chờ đợi thành phần 𝑊𝑞, và 𝐿lat,compute bao gồm sự suy luận
thời gian (In the batching analysis that follows (section 13.7.3), 𝐿lat,wait corresponds to the queueing wait component 𝑊𝑞, and 𝐿lat,compute includes inference time).
Mối quan hệ này (giữ) đúng bất kể đến sự phân phối, dịch vụ thời gian sự phân phối, hay sự lập lịch
chính sách (This relationship holds regardless of arrival distribution, service time distribution, or scheduling policy). Một thực tế công suất sự tính toán cho thấy tại sao tính phổ quát này quan trọng cho việc phục vụ bộ nhớ (A practical capacity calculation shows why this universality matters for serving memory).
Khăn ăn Toán học 13.4: Little’s Định luật công suất việc xác định kích thước (Little’s Law capacity sizing)
Vấn đề: Bao nhiêu đồng thời yêu cầu công suất (mà) một hệ thống cần để phục vụ 1,000 QPS? (Problem: How much concurrent request capacity does a system need to serve 1,000 QPS?)
Toán học: Little’s Định luật cho 𝑄req = 𝜆arr𝑇lat, do đó tính đồng thời bằng (equals) thông lượng được nhân với
độ trễ (phần D.2.4 dẫn xuất định luật) (Math: Little’s Law gives 𝑄req = 𝜆arr𝑇lat, so concurrency equals throughput multiplied by latency (section D.2.4 derives the law)).
Được cho:
• Thông lượng mục tiêu (𝜆arr): 1,000 QPS.
• Độ trễ mục tiêu (𝑇lat): 50 ms (0.05 s).
Toán học:
𝑄req = 1,000 QPS × 0.05 s = 50 đồng thời các yêu cầu
Các hệ thống sự thấu hiểu: Máy chủ phải có đủ RAM để giữ 50 các yêu cầu một cách đồng thời qua
lô và hàng đợi trạng thái (Systems insight: The server must have enough RAM to hold 50 requests simultaneously across batch and queue state). Nếu GPU hết bộ nhớ tại lô kích thước 32, hệ thống (về mặt) vật lý
không thể đạt (hit) 1,000 QPS tại 50 ms độ trễ; duy nhất các tùy chọn là để giảm độ trễ (𝑇lat) hay thêm đủ
bộ nhớ cho một lớn hơn thường trú (resident) 𝑄req (If the GPU runs out of memory at batch size 32, the system physically cannot hit 1,000 QPS at 50 ms latency; the only options are to reduce latency (𝑇lat) or add enough memory for a larger resident 𝑄req).
Little’s Định luật có ngay lập tức thực tế các hàm ý (implications). Nếu một sự suy luận dịch vụ trung bình 10 ms mỗi
yêu cầu (𝑇lat = 0.01 s) và hệ thống cho thấy 50 đồng thời các yêu cầu trên (mức) trung bình (𝑄req = 50), thì
đến tỷ lệ phải là 𝜆arr = 𝑄req/𝑇lat = 5000 các yêu cầu mỗi giây (If an inference service averages 10 ms per request (𝑇lat = 0.01 s) and the system shows 50 concurrent requests on average (𝑄req = 50), then the arrival rate must be 𝜆arr = 𝑄req/𝑇lat = 5000 requests per second). Ngược lại (Conversely), nếu hệ thống phải
giới hạn đồng thời các yêu cầu (xuống) 10 (có lẽ do GPU bộ nhớ các sự ép buộc) và dịch vụ thời gian là 10
ms, nó có thể duy trì (sustain) (nhiều) nhất 1000 các yêu cầu mỗi giây (Conversely, if the system must limit concurrent requests to 10 (perhaps due to GPU memory constraints) and the service time is 10 ms, it can sustain at most 1000 requests per second).
13.5.2 Việc tạo lô thuế (The batching tax): Độ trễ-thông lượng biên giới (The latency-throughput frontier)
Trong khi Little’s Định luật liên hệ hàng đợi độ sâu tới thông lượng, nó không tính toán (account) cho Việc tạo lô Thuế (Batching Tax):
được cố ý (deliberate) sự chậm trễ được giới thiệu để tối đa hóa phần cứng sự sử dụng (While Little’s Law relates queue depth to throughput, it does not account for the Batching Tax: the deliberate delay introduced to maximize hardware utilization). Trong truyền thống của định lượng
các hệ thống, chúng ta phân tích điều này như một việc xếp hàng đợi sự chậm trễ vấn đề (In the tradition of quantitative systems, we analyze this as a queuing delay problem).
Khi một sự suy luận máy chủ tạo lô các yêu cầu, nó giới thiệu hai khác biệt các nguồn của độ trễ (When an inference server batches requests, it introduces two distinct sources of latency). Lô
sự hình thành (formation) sự chậm trễ (𝐿lat,form) là thời gian (cái) đầu tiên yêu cầu trong một lô đợi cho (cái) cuối cùng yêu cầu (để) đến (Batch formation delay (𝐿lat,form) is the time the first request in a batch waits for the last request to arrive).

732
13.5 Việc xếp hàng đợi Lý thuyết (Queuing Theory)
10
M/M/1 Hàng đợi: Việc xếp-
hàng đợi lý thuyết (đã) bắt nguồn với
Agner Krarup Erlang’s 1909
sự phân tích của Copenhagen
Điện thoại Tổng đài, nơi
cuộc gọi các sự đến thực sự là (genuinely were)
không nhớ (memoryless) (Poisson).
M/M/1 mô hình’s hàm mũ (exponential)
dịch vụ thời gian giả định khớp (fit)
điện thoại tốt nhưng dự đoán-quá (overpre-
dicts) dịch vụ-thời gian phương sai cho
nhiều cố định-hình dạng ML sự suy-
luận các khối lượng công việc. Sự không khớp
này là hữu ích cho trực giác:
M/M/1 đánh giá quá cao (overestimates) đợi
các thời gian bởi xấp xỉ 2× (khi được) so-
sánh với một mang tính xác định-
dịch vụ (deterministic-service) mô hình như là M/D/1,
do đó công suất việc lập kế hoạch dựa
trên nó có xu hướng bảo tồn nhiều hơn
khoảng không (headroom).
11
Siêu-Tuyến tính (Super-Linear) Độ trễ
Sự phân kỳ: Việc lập kế hoạch
đầu gối (knee) thường xuất hiện tốt (ngay) trước-
khi (well before) đầy đủ sự bão hòa. Trong
M/M/1 trung bình phản hồi-thời gian
phương trình,
𝐸[𝑇] = (1/𝜇)/(1−𝜌serv),
nơi 𝜌serv = 𝜆arr/𝜇 là sự sử-
dụng (utilization). (1 −𝜌serv)−1
thuật ngữ phân kỳ khi 𝜌serv → 1: tại
𝜌serv = 0.7, trung bình phản hồi
thời gian đã là 3.3× (của cái) cơ sở
dịch vụ thời gian; tại 𝜌serv = 0.9, nó
là 10×. Chính xác hoạt động
giới hạn là một chính sách và khối lượng công việc
sự lựa chọn, nhưng việc cố gắng kéo giãn (stretch)
một nhạy cảm-độ trễ hàng đợi hướng
tới sự bão hòa tạo ra không tương-
xứng độ trễ sự phát triển.
12
Kendall Ký hiệu: Trong
A/S/c (Đến/Dịch-
vụ/các máy chủ) hệ thống,
“M”
biểu thị
một
Markovian (không nhớ)
quá trình
và
“D”
có nghĩa là
mang tính xác định.
Văn bản
chọn
M/M/1
thay vì (cái) thực tế hơn
M/D/1 bởi vì M/M/1’s
bảo thủ thành kiến (bias) là một tính năng
cho công suất việc lập kế hoạch:
nó
đánh giá quá cao đợi các thời gian bởi
xấp xỉ 2× khi dịch vụ
các thời gian là gần như mang tính xác định,
việc bảo tồn lề (margin) chống lại
phương sai những sự ngạc nhiên. Chi phí
của khiêm tốn việc cung cấp-quá (over-provisioning)
thường xa thấp hơn (so với) chi phí
của một SLA sự bỏ lỡ tại p99 đuôi
khi dịch vụ thời gian phương sai
tăng vọt (spikes) một cách không mong đợi.
Sự suy luận sự lạm phát (inflation) là sự phát triển trong sự suy luận thời gian 𝑇inf(𝐵) khi GPU xử lý 𝐵 các mẫu
thay vì 1 (Inference inflation is the growth in inference time 𝑇inf(𝐵) when the GPU processes 𝐵 samples instead of 1). (Cái) dẫn đến độ trễ-thông lượng Pareto biên giới là tập hợp của các cấu hình nơi một
(người) không thể cải thiện thông lượng mà không có việc trả một “thuế” trong được làm tăng độ trễ (The resulting latency-throughput Pareto frontier is the set of configurations where one cannot improve throughput without paying a “tax” in increased latency). Chúng ta có thể định lượng tổng
được tạo lô-yêu cầu độ trễ cho một lô kích thước 𝐵 và đến tỷ lệ 𝜆arr như phương trình 13.4 (We can quantify the total batched-request latency for a batch size 𝐵 and arrival rate 𝜆arr as equation 13.4):
𝐿lat,tổng ≈ (𝐵−1)/(2𝜆arr) (Sự hình thành sự chậm trễ) + 𝑇inf(𝐵) (Sự suy luận thời gian) (13.4)
Phương trình này tiết lộ “chi phí của thông lượng” (This equation reveals the “cost of throughput.”). Việc tăng 𝐵 để bão hòa GPU khấu hao
phần cứng chi phí, nhưng làm lạm phát mỗi-yêu cầu độ trễ (Increasing 𝐵 to saturate the GPU amortizes the hardware cost, but inflates the per-request latency). Một cách cụ thể, tại 500 QPS, việc di chuyển từ lô-1 tới
lô-32 tăng đợi-thời gian từ 0 ms tới 31 ms, việc đóng góp vào một 23× tổng độ trễ hình phạt (penalty) (2 ms →
46 ms) (Concretely, at 500 QPS, moving from batch-1 to batch-32 increases wait-time from 0 ms to 31 ms, contributing to a 23× total latency penalty (2 ms → 46 ms)). Cho một các hệ thống kỹ sư, này thuế là chính bộ điều chỉnh của thuộc về kinh tế tính hiệu quả: kỹ sư
chọn lô kích thước thứ mà tối đa hóa thông lượng (việc giảm thiểu chi phí mỗi truy vấn) mà không có việc vi phạm
độ trễ SLO (𝐿lat) (For a systems engineer, this tax is the primary regulator of economic efficiency: the engineer chooses the batch size that maximizes throughput (minimizing cost per query) without violating the latency SLO (𝐿lat)).
13.5.3 Sự sử dụng-độ trễ mối quan hệ (The utilization-latency relationship)
Little’s Định luật mô tả trung bình hệ thống hành vi, nhưng nó không tiết lộ cách độ trễ thay đổi khi tải
tiếp cận công suất (Little’s Law describes average system behavior, but it does not reveal how latency changes as load approaches capacity). Để trả lời (câu) chí mạng câu hỏi của bao nhiêu dự phòng (spare) công suất một việc phục vụ hệ thống
cần, chúng ta chuyển tới M/M/1 hàng đợi mô hình (Harchol-Balter 2013) (To answer the critical question of how much spare capacity a serving system needs, we turn to the M/M/1 queue model (Harchol-Balter 2013)).10 Cho một hệ thống với Poisson
các sự đến (arrivals) và hàm mũ dịch vụ các thời gian, phương trình 13.5 cung cấp trung bình thời gian trong hệ thống (For a system with Poisson arrivals and exponential service times, equation 13.5 gives the average time in system):
𝑇lat = 1/(𝜇−𝜆arr) = dịch vụ thời gian/(1−𝜌serv) (13.5)
nơi 𝜆arr là đến tỷ lệ, 𝜇 là dịch vụ tỷ lệ (các yêu cầu mỗi giây máy chủ có thể xử lý), và
𝜌serv = 𝜆arr/𝜇 là sự sử dụng (phần (fraction) của thời gian máy chủ là bận rộn) (where 𝜆arr is the arrival rate, 𝜇 is the service rate (requests per second the server can handle), and 𝜌serv = 𝜆arr/𝜇 is the utilization (fraction of time the server is busy)).
Phương trình này tiết lộ tại sao việc phục vụ các hệ thống thể hiện phi tuyến tính hành vi: nhỏ các sự gia tăng trong tải
gần công suất gây ra không tương xứng độ trễ các sự gia tăng11 (This equation reveals why serving systems exhibit nonlinear behavior: small increases in load near capacity cause disproportionate latency increases11). Bảng 13.7 định lượng này mối quan hệ,
việc cho thấy cách trung bình thời gian trong hệ thống phát triển một cách nhanh chóng khi sự sử dụng tiếp cận 100 phần trăm (Table 13.7 quantifies this relationship, showing how average time in system grows rapidly as utilization approaches 100 percent).
Bảng 13.7: Sự sử dụng-Độ trễ Mối quan hệ: Trung bình thời gian trong hệ thống (đợi + dịch vụ) như một bội số của dịch vụ thời gian cho một
M/M/1 hàng đợi (Utilization-Latency Relationship: Average time in system (wait + service) as a multiple of service time for an M/M/1 queue). Tại 50 phần trăm sự sử dụng, thời gian trong hệ thống là 2× dịch vụ thời gian; tại 90 phần trăm, nó đạt (tới) 10× (At 50 percent utilization, time in system is 2× service time; at 90 percent, it reaches 10×). Này phi tuyến tính sự phát triển
giải thích tại sao các hệ thống thứ mà thực hiện tốt tại vừa phải tải đột ngột vi phạm các SLO khi lưu lượng truy cập tăng: việc di chuyển từ 80 phần trăm
tới 90 phần trăm sự sử dụng nhân đôi độ trễ (This nonlinear growth explains why systems that perform well at moderate load suddenly violate SLOs when traffic increases: moving from 80 percent to 90 percent utilization doubles latency).
Sự sử dụng (𝜌serv)
Độ trễ Bội số
Ví dụ (5 ms dịch vụ)
50%
2×
10 ms
70%
3.3×
17 ms
80%
5×
25 ms
90%
10×
50 ms
95%
20×
100 ms
M/M/1 mô hình giả định một cách theo hàm mũ được phân phối dịch vụ các thời gian, nhưng ML sự suy luận điển hình
có gần-như-không-đổi (near-constant) dịch vụ thời gian cho cố định lô các kích thước, việc làm M/D/1 (mang tính xác định dịch vụ)
mô hình (trở nên) chính xác hơn trong thực tế (The M/M/1 model assumes exponentially distributed service times, but ML inference typically has near-constant service time for fixed batch sizes, making the M/D/1 (deterministic service) model more accurate in practice). Chúng ta sử dụng M/M/1 ở đây bởi vì nó mang lại dạng-đóng (closed-form) các giải pháp và
tạo ra bảo thủ các ước tính (We use M/M/1 here because it yields closed-form solutions and produces conservative estimates). Cho M/D/1 các hàng đợi, trung bình đợi thời gian là xấp xỉ (một) nửa của
M/M/1 tại giống nhau sự sử dụng, thứ mà quan trọng cho công suất việc lập kế hoạch: M/M/1 sự phân tích (sẽ) một cách nhẹ nhàng
cung cấp-quá, việc phạm lỗi (erring) trên (về) phía của việc đáp ứng các SLO thay vì việc vi phạm chúng (For M/D/1 queues, average wait time is approximately half of M/M/1 at the same utilization, which matters for capacity planning: M/M/1 analysis will slightly over-provision, erring on the side of meeting SLOs rather than violating them).12
13.5.4 Nhiều-máy chủ các sự cân nhắc (Multi-server considerations)
(Cái) đi trước (preceding) sự phân tích tập trung trên một đơn việc phục vụ nút (một máy móc (đang) phục vụ sự suy luận các yêu cầu) (The preceding analysis focuses on a single serving node (one machine serving inference requests)).
Phạm vi này (scope) căn chỉnh với cuốn sách này’s sự tập trung trên việc làm chủ (mastering) (cái) cơ bản đơn vị của ML các hệ thống (This scope aligns with this book’s focus on mastering the basic unit of ML systems). Đơn-nút
việc xếp hàng đợi động lực học (dynamics) là điều kiện tiên quyết (prerequisite) tới hiệu quả sự mở rộng (Single-node queuing dynamics are prerequisite to effective scaling). Các kỹ sư không thể tối ưu hóa một được phân tán
hệ thống mà không có trước tiên việc hiểu hành vi của các thành phần của nó (Engineers cannot optimize a distributed system without first understanding the behavior of its components).
M/M/1 sự phân tích duy trì (là) nền tảng cho việc xác định kích thước đúng (right-sizing) cá nhân các nút, việc xác định sự mở rộng
trình kích hoạt (trigger), và việc tránh non (premature) sự mở rộng-ra (scale-out) (M/M/1 analysis remains the foundation for right-sizing individual nodes, identifying the scaling trigger, and avoiding premature scale-out). Đầu tiên, nó xác định liệu một GPU (có) thể đáp ứng độ trễ (hay không)

13. Mô hình Việc phục vụ (Model Serving)
733
SLO tại được mong đợi lưu lượng truy cập (SLO at expected traffic). Sau đó nó cho thấy khi đến tỷ lệ vượt quá đơn-nút công suất (Then it shows when arrival rate exceeds single-node capacity). Cuối cùng, nó
ngăn cản các nhóm (teams) khỏi việc thêm các bản sao (replicas) trước khi nút thắt cổ chai là thực sự nút công suất thay vì
việc tạo lô chính sách, sự tiền xử lý, lạnh khởi động (cold start), hay thời gian chạy cấu hình (Finally, it prevents teams from adding replicas before the bottleneck is actually node capacity rather than batching policy, preprocessing, cold start, or runtime configuration).
Một khi lưu lượng truy cập thực sự vượt quá đơn-nút công suất, tiếp theo động thái (move) là cấp độ-bản sao (replica-level) sự mở rộng-ra: nhiều
độc lập việc phục vụ các nút ngồi đằng sau một tải bộ cân bằng (load balancer) và mỗi (cái) chạy giống nhau mô hình (Once traffic truly exceeds single-node capacity, the next move is replica-level scale-out: multiple independent serving nodes sit behind a load balancer and each runs the same model). M/M/c
việc xếp hàng đợi mô hình mở rộng M/M/1 tới 𝑐 song song các máy chủ, việc cho thấy cách các bản sao có thể cải thiện độ trễ
khi lưu lượng truy cập được cân bằng qua độc lập các máy chủ (The M/M/c queuing model extends M/M/1 to 𝑐 parallel servers, showing how replicas can improve latency when traffic is balanced across independent servers). Chính xác p99 sự cải thiện phụ thuộc vào đến
quá trình, dịch vụ-thời gian phương sai, sự phân phối chính sách, và mỗi-bản sao sự sử dụng (The exact p99 improvement depends on arrival process, service-time variance, dispatch policy, and per-replica utilization). Đó bản sao mô hình là
vẫn khác từ được phân tán sự suy luận, nơi một yêu cầu được chia (split) qua các GPU thông qua mô hình
sự phân mảnh (sharding), tensor tính song song, hay đường ống tính song song (That replica model is still different from distributed inference, where one request is split across GPUs through model sharding, tensor parallelism, or pipeline parallelism). Chương này thiết lập (những) đơn-nút và
bản sao nền tảng; được phân tán sự suy luận thêm sự điều phối (coordination) chi phí hoạt động và tính nhất quán các thách thức
vượt ra ngoài phạm vi này (This chapter establishes the single-node and replica foundations; distributed inference adds coordination overhead and consistency challenges beyond this scope).
13.5.5 Đuôi độ trễ (Tail latency)
Sản xuất các SLO điển hình chỉ định phân vị các mục tiêu (p95, p99) thay vì các mức trung bình bởi vì đuôi
độ trễ xác định người dùng trải nghiệm cho chậm nhất các yêu cầu (Dean và Barroso 2013) (Production SLOs typically specify percentile targets (p95, p99) rather than averages because tail latency determines user experience for the slowest requests (Dean and Barroso 2013)). Cho một M/M/1
hàng đợi, p99 độ trễ tuân theo (follows):
𝑇lat,p99 ≈ dịch vụ thời gian / (1−𝜌serv) ⋅ ln(1 / (1−0.99)) ≈ 4.6 ⋅ dịch vụ thời gian / (1−𝜌serv) (13.6)
Tại 70 phần trăm sự sử dụng, M/M/1 p99 sự xấp xỉ (approximation) là xấp xỉ 15 lần (của) dịch vụ
thời gian (4.6/0.3 ≈ 15.3), trong khi trung bình độ trễ là chỉ 3.3 lần (At 70 percent utilization, the M/M/1 p99 approximation is approximately 15 times the service time (4.6/0.3 ≈ 15.3), while average latency is only 3.3 times). Cho mang tính xác định-dịch vụ các mô hình như
là M/D/1, đuôi các giá trị yêu cầu cụ thể-mô hình sự tính toán thay vì một đơn giản phổ quát hệ số nhân (multiplier) (For deterministic-service models such as M/D/1, tail values require model-specific calculation rather than a simple universal multiplier).
Quan trọng điểm là không bị thay đổi: các hệ thống (thứ) mà dường như khỏe mạnh với thấp trung bình độ trễ có thể có
không thể chấp nhận (unacceptable) đuôi độ trễ, bởi vì mức trung bình giấu trải nghiệm của rủi ro nhất (unluckiest) các yêu cầu (The important point is unchanged: systems that seem healthy with low average latency can have unacceptable tail latency, since the average hides the experience of the unluckiest requests).
13.5.5.1 Đuôi tại quy mô vấn đề (The tail at scale problem)
Dean và Barroso’s sự phân tích tiết lộ tại sao đuôi độ trễ trở nên chí mạng khi các hệ thống mở rộng vượt ra ngoài đơn
các máy móc (Dean và Barroso 2013) (Dean and Barroso’s analysis reveals why tail latency becomes critical as systems scale beyond single machines (Dean and Barroso 2013)). Khi các yêu cầu phân nhánh ra (fan out) tới nhiều các máy chủ, xác suất của
việc trải nghiệm ít nhất một chậm phản hồi phát triển một cách nhanh chóng với máy chủ số đếm (When requests fan out to multiple servers, the probability of experiencing at least one slow response grows rapidly with server count). Này “đuôi tại quy mô” hiệu ứng
làm cá nhân máy chủ đuôi độ trễ (trở nên) chí mạng cho tổng thể hệ thống hiệu suất (This “tail at scale” effect makes individual server tail latency critical for overall system performance).
Cho đơn-máy móc việc phục vụ, nguyên tắc này có hai các hàm ý (implications). Đầu tiên, đuôi độ trễ trên cá nhân
các máy móc quan trọng bởi vì nó sẽ cộng gộp khi các hệ thống cuối cùng mở rộng (First, tail latency on individual machines matters because it will compound when systems eventually scale). Thứ hai, khoan dung-đuôi (tail-tolerant)
các kỹ thuật được mô tả sau (việc rào chắn (hedging), tinh tế sự suy giảm) cung cấp giá trị thậm chí trên đơn các máy móc
và trở nên không thể thiếu (indispensable) tại quy mô (Second, the tail-tolerant techniques described later (hedging, graceful degradation) provide value even on single machines and become indispensable at scale).
Khoan dung-đuôi các kỹ thuật như là yêu cầu việc rào chắn (hedging) gửi dư thừa (redundant) các yêu cầu sau một thời gian chờ (timeout), việc chấp nhận
bất cứ phản hồi (nào) đến trước (Tail-tolerant techniques such as request hedging send redundant requests after a timeout, accepting whichever response arrives first). Sao lưu các yêu cầu và tải việc cân bằng ra xa khỏi chậm các máy chủ một cách trực tiếp
giải quyết độ trễ phương sai (Backup requests and load balancing away from slow servers directly address latency variance). Những các kỹ thuật này áp dụng một cách sạch sẽ tới nhiều mô hình các bản sao, và một số
đơn-nút các hệ thống có thể xấp xỉ chúng với đồng thời các luồng hay các phiên bản khi sự hủy bỏ
và tài nguyên sự cô lập ngữ nghĩa cho phép nó (These techniques apply cleanly to multiple model replicas, and some single-node systems can approximate them with concurrent streams or instances when cancellation and resource isolation semantics permit it). Chúng trở nên thiết yếu khi việc mở rộng tới được phân tán
sự suy luận các hệ thống (They become essential when scaling to distributed inference systems).
Việc xếp hàng đợi mô hình và đuôi độ trễ sự phân tích cung cấp các đầu vào cho công suất việc lập kế hoạch (The queuing model and tail latency analysis provide the inputs for capacity planning). Một cụ thể
sự triển khai làm các sự đánh đổi (trở nên) hữu hình (tangible) (A concrete deployment makes the trade-offs tangible).
Việc áp dụng Little’s Định luật tới ResNet-50 làm công suất sự ép buộc (trở nên) cụ thể (Applying Little’s Law to ResNet-50 makes the capacity constraint concrete).
Khăn ăn Toán học 13.5: ResNet-50 công suất việc lập kế hoạch
Hãy xem xét việc thiết kế một ResNet-50 việc phục vụ hệ thống với những các yêu cầu này:
• Mục tiêu p99 độ trễ: 50 ms
• Đỉnh (Peak) được mong đợi lưu lượng truy cập: 5,000 QPS
• Dịch vụ thời gian (TensorRT FP16): 5 ms
Bước 1: Tìm an toàn sự sử dụng (Find safe utilization). Từ phương trình 13.6, 𝑇lat,p99 ≈ 4.6 × dịch vụ thời gian / (1 − 𝜌serv).
Việc thiết lập 𝑇lat,p99 ≤ 50 ms với 5 ms dịch vụ thời gian cho 𝜌serv ≤ 1 − (4.6 × 5𝑚𝑠)/50𝑚𝑠 = 0.54

734
13.5 Việc xếp hàng đợi Lý thuyết (Queuing Theory)
13
Việc rào chắn (Hedging): Thuật ngữ
được mượn từ tài chính,
nơi một bù đắp (offsetting) vụ cá cược (bet) giảm thiểu
rủi ro; ở đây, dư thừa
yêu cầu là một vụ cá cược chống lại một
chậm máy chủ. Điều này không (phải) miễn phí:
cho ML các hệ thống, việc thua lỗ (losing)
được rào chắn (hedged) yêu cầu có thể vẫn chiếm
đóng (occupy) máy gia tốc thời gian nếu sự suy-
luận đã (được) khởi chạy, bởi-
vì thông thường GPU các hạt nhân
không (được) một cách rẻ mạt (cheaply) bị hủy bỏ giữa-
chừng-sự thực thi (mid-execution). Do đó, một việc rào chắn
chính sách phải lập ngân sách (budget) trùng lặp
công việc cũng như độ trễ
lợi ích (benefit).
14
Chim hoàng yến (Canary): Được đặt tên cho
mỏ than (coal mine) thực tiễn (những năm đầu
1900–1980s) của việc sử dụng các loài chim
những (con) (có) cao trao đổi chất (metabolic) tỷ lệ
làm chúng nhạy cảm với độc
các khí trước khi các nồng độ
trở nên gây tử vong cho con người. Trong
ML việc phục vụ, chim hoàng yến các yêu cầu
phục vụ giống nhau cảnh báo-sớm
chức năng cho phân nhánh ra (fan-out) các truy vấn:
bằng cách việc kiểm tra 1–2 các phụ trợ (backends) trước-
khi (before) cam kết (tới) đầy đủ phân nhánh-
ra, hệ thống phát hiện chậm hay
thất bại các bản sao trước khi một đơn
kẻ đi tụt lại (straggler) làm đình trệ toàn bộ được phân-
tán sự suy luận yêu cầu—một
chí mạng sự bảo vệ khi phân nhánh-
ra chiều rộng có nghĩa (là) đuôi độ trễ
phát triển với cực đại của tất cả
phụ trợ phản hồi các thời gian.
(54 phần trăm tối đa sự sử dụng) ((54 percent maximum utilization)). Điều này sử dụng bảo thủ M/M/1 p99 ranh giới (bound) từ
được hiển thị phương trình thay vì việc áp dụng một trung bình-chờ đợi M/D/1 sự điều chỉnh tới một đuôi-độ trễ
SLO (This uses the conservative M/M/1 p99 bound from the displayed equation rather than applying an average-wait M/D/1 adjustment to a tail-latency SLO).
Bước 2: Tính toán được yêu cầu dịch vụ tỷ lệ (Calculate required service rate). 𝜇yêu cầu (required) = 5,000𝑄𝑃𝑆/0.54 = 9259.3 𝑦ê𝑢_𝑐ầ𝑢/𝑠
Bước 3: Xác định GPU số đếm. Đơn V100 thông lượng tại 𝐵 = 16: 1,143 ℎì𝑛ℎ_ả𝑛ℎ/𝑠 (img/s)
Các GPU được cần = 9259.3 𝑦ê𝑢_𝑐ầ𝑢/𝑠 / 1,143 ℎì𝑛ℎ_ả𝑛ℎ/𝑠 = 8.1 → 9 các GPU
Bước 4: Thêm khoảng không cho phương sai (Add headroom for variance). Sản xuất các hệ thống thêm 30 phần trăm khoảng không cho lưu lượng truy cập
các sự tăng vọt (spikes) và phương sai: cuối cùng số đếm = 9 × 1.3 = 11.7, được làm tròn lên (tới) 12.
Bước 5: Xác minh lỗi sự khoan dung (Verify fault tolerance). 30 phần trăm khoảng không giải quyết lưu lượng truy cập phương sai, nhưng sản-
xuất các hệ thống cũng cần lỗi sự khoan dung. Với 12 các GPU, việc mất (đi) một (cái) để lại 11 các GPU xử lý
5,000 QPS. Sau sự thất bại (postfailure) sự sử dụng là (5,000 QPS / 1,143 ℎì𝑛ℎ_ả𝑛ℎ/𝑠) / 11 = 39.8%.
Điều này duy trì tốt (nhiều) dưới 54 phần trăm an toàn sự sử dụng ngưỡng, việc xác nhận N+1 sự dư thừa
được thỏa mãn (This remains well below the 54 percent safe utilization threshold, confirming N+1 redundancy is satisfied). Cho nghiêm ngặt hơn lỗi sự khoan dung các yêu cầu, N+2 sự dư thừa (việc khoan dung hai đồng thời
các sự thất bại) sẽ yêu cầu 11 các GPU dưới giống nhau an toàn-sự sử dụng ngưỡng, hay khoảng 14
các GPU nếu 30 phần trăm khoảng không phải duy trì sau hai đồng thời các sự thất bại (For stricter fault tolerance requirements, N+2 redundancy (tolerating two simultaneous failures) would require 11 GPUs under the same safe-utilization threshold, or about 14 GPUs if the 30 percent headroom must remain after two simultaneous failures).
Kết quả: Cung cấp 12 V100 các GPU để phục vụ 5,000 QPS tại 50 ms p99 độ trễ với N+1 lỗi
sự khoan dung (Result: Provision 12 V100 GPUs to serve 5,000 QPS at 50 ms p99 latency with N+1 fault tolerance).
Việc xếp hàng đợi sự phân tích giải thích công suất việc lập kế hoạch cách tiếp cận được chi tiết trong phần 13.11.3 và
kết nối một cách trực tiếp tới MLPerf Máy chủ kịch bản (The queuing analysis explains the capacity planning approach detailed in section 13.11.3 and connects directly to the MLPerf Server scenario). Phần 12.8.4.2 giải thích cách MLPerf đo lường
thông lượng chỉ cho các yêu cầu (đang) đáp ứng độ trễ SLO: một hệ thống (đang) đạt được 10,000 QPS nhưng vi phạm
SLO trên 5 phần trăm của các yêu cầu báo cáo chỉ 9,500 hợp lệ QPS (Section 12.8.4.2 explains how MLPerf measures throughput only for requests meeting the latency SLO: a system achieving 10,000 QPS but violating the SLO on 5 percent of requests reports only 9,500 valid QPS).
13.5.6 Khoan dung-đuôi các kỹ thuật (Tail-tolerant techniques)
Việc loại bỏ tất cả các nguồn của độ trễ tính biến đổi (variability) là thường không thực tế (impractical) (Eliminating all sources of latency variability is often impractical). Sản xuất các hệ thống thay vào đó sử dụng
các kỹ thuật thứ mà khoan dung tính biến đổi trong khi vẫn đáp ứng các SLO (Dean và Barroso 2013; Dean 2012) (Production systems instead employ techniques that tolerate variability while still meeting SLOs (Dean and Barroso 2013; Dean 2012)).
Hữu ích sự tổ chức là bởi sự thất bại chế độ: một kẻ đi tụt lại (straggler) bản sao gọi cho một cuộc đua, phân nhánh ra gọi cho sớm
sự phát hiện, sự quá tải gọi cho sự thu nhận kiểm soát (admission control) hay tinh tế sự suy giảm, và sự thử lại (retry) sự khuếch đại (amplification) gọi
cho được điều phối (coordinated) sự rụng (shedding) (The useful organization is by failure mode: a straggler replica calls for a race, fan-out calls for early detection, overload calls for admission control or graceful degradation, and retry amplification calls for coordinated shedding).
Cho một kẻ đi tụt lại bản sao, hệ thống có thể đua (race) chậm con đường (For a straggler replica, the system can race the slow path). Dưới việc rào chắn, khi một yêu cầu (đã)
không hoàn thành bên trong được mong đợi thời gian, hệ thống gửi một dư thừa yêu cầu tới một máy chủ khác.13
Máy khách sử dụng bất cứ phản hồi (nào) đến trước và hủy (bỏ) (cái) khác (The client uses whichever response arrives first and cancels the other). Cho ML việc phục vụ, điều này có nghĩa là
việc duy trì nhiều mô hình các bản sao và việc định tuyến chậm các yêu cầu tới thay thế (alternative) các bản sao (For ML serving, this means maintaining multiple model replicas and routing slow requests to alternative replicas). Chi phí hoạt động
là khiêm tốn: nếu hệ thống rào chắn tại 95(th) phân vị, chỉ 5 phần trăm của các yêu cầu tạo ra các bản sao (duplicates),
việc làm tăng tải bởi chỉ 5 phần trăm trong khi một cách quyết liệt (dramatically) việc giảm thiểu đuôi độ trễ (The overhead is modest: if the system hedges at the 95th percentile, only 5 percent of requests generate duplicates, increasing load by only 5 percent while dramatically reducing tail latency).
Thông thường được khởi chạy sự suy luận các hạt nhân không (được) một cách rẻ mạt bị ngắt quãng giữa chừng-sự thực thi (Ordinary launched inference kernels are not cheaply interrupted mid-execution). Khi một được rào chắn
yêu cầu hoàn thành, (cái) bản sao phải bị hủy (bỏ), nhưng nếu sự suy luận đã (được) bắt đầu trên GPU,
sự hủy bỏ các cách tiếp cận bao gồm việc kiểm tra một sự hủy bỏ cờ trước khi khởi chạy sự suy luận, việc chấp nhận
bị lãng phí tính toán cho đang bay hạt nhân, hay việc sử dụng yêu cầu sự ưu tiên hóa (prioritization) để hạ ưu tiên (deprioritize) bản sao (When a hedged request completes, the duplicate must be cancelled, but if inference has already begun on the GPU, cancellation approaches include checking a cancellation flag before launching inference, accepting wasted compute for the in-flight kernel, or using request prioritization to deprioritize the duplicate).
Vì (Since) việc rào chắn điển hình áp dụng chỉ tới một nhỏ đuôi của các yêu cầu, chi phí hoạt động từ thỉnh thoảng (occasional) bị lãng phí
tính toán có thể duy trì (có thể) chấp nhận được khi chính sách được điều chỉnh một cách cẩn thận (Since hedging typically applies only to a small tail of requests, the overhead from occasional wasted compute can remain acceptable when the policy is tuned carefully).
Bị trói (Tied) các yêu cầu làm giống nhau cuộc đua (trở nên) quyết liệt hơn bằng cách việc gửi yêu cầu tới nhiều các máy chủ
một cách đồng thời, nhưng bao gồm một thẻ (tag) việc cho phép các máy chủ hủy (bỏ) sự thực thi một khi một máy chủ khác bắt đầu
việc xử lý (Tied requests make the same race more aggressive by sending the request to multiple servers simultaneously, but include a tag allowing servers to cancel execution once another server begins processing). Điều này loại bỏ sự chậm trễ của việc chờ đợi để phát hiện một chậm phản hồi trước khi việc rào chắn (This eliminates the delay of waiting to detect a slow response before hedging). Cho
sự suy luận các máy chủ với đáng kể khởi nghiệp chi phí hoạt động từ mô hình việc tải và bộ nhớ sự cấp phát, bị trói
các yêu cầu đảm bảo ít nhất một máy chủ bắt đầu ngay lập tức (For inference servers with significant startup overhead from model loading and memory allocation, tied requests ensure at least one server begins immediately).
Phân nhánh ra các hệ thống cần một khác biệt sự can thiệp (intervention) điểm bởi vì một chậm phụ trợ có thể làm đình trệ toàn bộ
được phân tán yêu cầu (Fan-out systems need a different intervention point because one slow backend can stall the entire distributed request). Chim hoàng yến các yêu cầu trước tiên gửi yêu cầu tới một nhỏ tập hợp con (subset) của một tới hai các máy chủ.14
Nếu những (máy chủ) này trả về bên trong được mong đợi thời gian, hệ thống gửi tới phần còn lại (remainder) (If these return within expected time, the system sends to the remainder). Nếu chim hoàng yến là chậm,
hệ thống có thể thử lại ở nơi khác hay sử dụng được lưu trong bộ nhớ đệm (cached) các kết quả trước khi cam kết (tới) đầy đủ phân nhánh ra (If the canary is slow, the system can retry elsewhere or use cached results before committing to the full fan-out). Kỹ thuật (này)
biến (turns) một tiềm năng đuôi-độ trễ sự khuếch đại vấn đề thành một sớm cảnh báo tín hiệu (The technique turns a potential tail-latency amplification problem into an early warning signal).
Khi vấn đề là sự quá tải thay vì một đơn kẻ đi tụt lại, việc đua làm hệ thống tồi tệ hơn
bằng cách việc thêm trùng lặp công việc (When the problem is overload rather than a single straggler, racing makes the system worse by adding duplicate work). Hệ thống thay vào đó phải bảo vệ hướng-tới-người dùng khả năng đáp ứng (responsiveness) và

13. Mô hình Việc phục vụ (Model Serving)
735
được thu nhận-yêu cầu độ trễ (admitted-request latency). Tinh tế sự suy giảm trả về xấp xỉ các kết quả thay vì (việc) định thời-gian
ra (timing out): sự phân loại các hệ thống có thể trả về được lưu trong bộ nhớ đệm các dự đoán cho tương tự các đầu vào, tạo sinh các mô hình có thể
trả về ngắn hơn các đầu ra, và các tập hợp (ensembles) có thể trả về các dự đoán từ một tập hợp con của các mô hình (Graceful degradation returns approximate results rather than timing out: classification systems can return cached predictions for similar inputs, generative models can return shorter outputs, and ensembles can return predictions from a subset of models). Việc giảm thiểu
số lượng của (đang) hoạt động tập hợp các thành viên (members) trong suốt sự quá tải một cách trực tiếp làm ngắn (shortens) dịch vụ thời gian (𝑇svc),
thứ mà làm tăng máy chủ’s dịch vụ tỷ lệ 𝜇 và mang sự sử dụng 𝜌serv = 𝜆arr/𝜇 trở lại (xuống) dưới
việc xếp hàng đợi đầu gối (hình 13.1)—việc đánh đổi một được kiểm soát độ chính xác sự giảm thiểu cho SLO sự sống sót thay vì một
không được kiểm soát độ trễ sự sụp đổ (collapse) (Reducing the number of active ensemble members during overload directly shortens service time (𝑇svc), which increases the server’s service rate 𝜇 and brings utilization 𝜌serv = 𝜆arr/𝜇 back below the queueing knee (figure 13.1)—trading a controlled accuracy reduction for SLO survival instead of an uncontrolled latency collapse). Sự thu nhận kiểm soát (Admission control) là nghiêm ngặt hơn (Admission control is stricter). Khi hàng đợi độ sâu vượt quá một ngưỡng,
nó (một cách) chủ động từ chối (rejects) các yêu cầu với ngay lập tức 503 các phản hồi thay vì việc chấp nhận công việc (thứ) mà (có) nhiều khả năng (likely)
để (sẽ) định thời gian ra (When queue depth exceeds a threshold, it proactively rejects requests with immediate 503 responses rather than accepting work that is likely to time out). Điều này hy sinh (sacrifices) thông lượng để bảo vệ độ trễ cho được thu nhận các yêu cầu (This sacrifices throughput to protect latency for admitted requests).
Một thực tế xuất phát điểm cho việc thiết lập ngưỡng là hai tới ba lần số lượng của những người làm việc
(một hàng đợi của hai tới ba dịch vụ các thời gian’ (sự) xứng đáng của công việc) (A practical starting point for setting the threshold is two to three times the number of workers (a queue of two to three service times’ worth of work)). Cho một hệ thống với bốn những người làm việc, điều này
mang lại một hàng đợi độ sâu ngưỡng của 8 tới 12 các yêu cầu (For a system with four workers, this yields a queue depth threshold of 8 to 12 requests). Thích ứng sự thu nhận kiểm soát điều chỉnh các ngưỡng
dựa trên được quan sát p99 độ trễ, việc thắt chặt (tightening) khi độ trễ tăng lên trên mục tiêu và nới lỏng (relaxing) khi
độ trễ duy trì (sự) khỏe mạnh (Adaptive admission control adjusts thresholds based on observed p99 latency, tightening when latency increases above target and relaxing when latency remains healthy). M/D/1 đặc tính của ML sự suy luận—rằng được biên dịch (compiled) các mô hình (đang) thực thi một
cố định lô kích thước có gần-như-không-đổi, mang tính xác định dịch vụ các thời gian—cung cấp (cho) ML sự thu nhận các bộ điều khiển
một sự chính xác lợi thế hơn chung web máy chủ sự thu nhận các bộ điều khiển (The M/D/1 property of ML inference—that compiled models executing a fixed batch size have near-constant, deterministic service times—gives ML admission controllers a precision advantage over general web server admission controllers). Trong một chung web dịch vụ,
dịch vụ thời gian phụ thuộc vào cơ sở dữ liệu sự nối kết (join) độ phức tạp, bộ nhớ đệm trạng thái, và truy vấn cấu trúc, việc làm nó (trở nên) cao độ
ngẫu nhiên (stochastic) và khó để dự đoán (In a general web service, service time depends on database join complexity, cache state, and query structure, making it highly stochastic and difficult to predict). Trong ML sự suy luận, chuyển tiếp vượt qua thời gian cho một (được) cho lô kích thước
là thường được giới hạn (bởi) một cách chặt chẽ (một cách) đủ rằng một sự thu nhận bộ điều khiển có thể ước tính bao nhiêu đồng thời
các yêu cầu hệ thống có thể hấp thụ (absorb) trước khi hàng đợi (có) nhiều khả năng để gây ra một SLO sự vi phạm, thay vì
việc dựa (dẫm) chỉ vào thô (coarse) bảo thủ các heuristics (In ML inference, the forward pass time for a given batch size is often bounded tightly enough that an admission controller can estimate how many concurrent requests the system can absorb before the queue is likely to cause an SLO violation, rather than relying only on coarse conservative heuristics).
Một tinh tế sự thất bại chế độ xảy ra khi tất cả các bản sao bị (làm) quá tải một cách đồng thời (A subtle failure mode occurs when all replicas are overloaded simultaneously). Nếu tải bộ cân-
bằng thử lại (các) bị từ chối yêu cầu tại (các) khác bản sao (thứ) mà cũng bị quá tải, thử lại lưu lượng truy cập khuếch đại (amplifies)
sự quá tải (If the load balancer retries rejected requests at other replicas that are also overloaded, retry traffic amplifies the overload). Được điều phối tải sự rụng giải quyết điều này bằng cách việc chia sẻ tải thông tin qua các bản sao,
việc kích hoạt cấp độ-hệ thống các quyết định về (việc) những (nhóm) nào yêu cầu để chấp nhận (Coordinated load shedding addresses this by sharing load information across replicas, enabling system-wide decisions about which requests to accept). Khi toàn cục tải vượt quá công suất,
các bản sao (một cách) tập thể từ chối giống nhau phần của các yêu cầu thay vì mỗi (cái) từ chối một cách độc lập
và việc kích hoạt (triggering) các sự thử lại (When global load exceeds capacity, replicas collectively reject the same fraction of requests rather than each rejecting independently and triggering retries).
Những các kỹ thuật này trở nên thiết yếu tại quy mô khi phân nhánh ra sự khuếch đại làm cá nhân máy chủ
đuôi độ trễ (trở nên) có thể nhìn thấy (với) những người dùng (These techniques become essential at scale when fan-out amplification makes individual server tail latency visible to users). Đơn-máy móc việc phục vụ các hệ thống có thể triển khai được rào chắn và bị trói các yêu cầu
qua GPU các luồng (streams) hay mô hình các bản sao (Single-machine serving systems can implement hedged and tied requests across GPU streams or model replicas). Việc xếp hàng đợi sự phân tích ở đây giả định vào-trước-ra-trước (first-in-first-out - FIFO)
việc xử lý, nhưng sản xuất các hệ thống thường triển khai sự ưu tiên sự lập lịch như là nhận thức-hạn chót (deadline-aware) hay
ngắn nhất-công việc-trước (shortest-job-first) các cách tiếp cận để giảm thiểu xa hơn đuôi độ trễ cho không đồng nhất các khối lượng công việc (Harchol-
Balter 2013) (The queuing analysis here assumes first-in-first-out (FIFO) processing, but production systems often implement priority scheduling such as deadline-aware or shortest-job-first approaches to further reduce tail latency for heterogeneous workloads (Harchol-Balter 2013)).
Trạm kiểm soát 13.2: Việc xếp hàng đợi và SLO khoảng không
Độ trễ các SLO (được) không (được) thi hành bởi “nhanh sự suy luận” một mình (alone); chúng được thi hành bởi khoảng không (Latency SLOs are not enforced by “fast inference” alone; they are enforced by headroom).
□Little’s Định luật: Có thể (bạn) sử dụng 𝑄req = 𝜆arr𝑇lat để giải thích tại sao việc tăng hàng đợi độ sâu ngụ ý (implies) (việc) tăng
độ trễ thậm chí nếu mỗi-yêu cầu tính toán thời gian (duy trì) không bị thay đổi (hay không)? (Little’s Law: Can you use 𝑄req = 𝜆arr𝑇lat to explain why rising queue depth implies rising latency even if per-request compute time is unchanged?)
□Sự sử dụng vách đá (cliff): Có thể (bạn) giải thích tại sao độ trễ phát triển phi tuyến tính khi sự sử dụng 𝜌serv
tiếp cận một, và tại sao sản xuất các hệ thống nhắm mục tiêu một bảo thủ 𝜌serv thay vì “100
phần trăm bận rộn” (hay không)? (Utilization cliff: Can you explain why latency grows nonlinearly as utilization 𝜌serv approaches one, and why production systems target a conservative 𝜌serv rather than “100 percent busy”?)
□Đợi so với tính toán: Được cho một đầu cuối-tới-đầu cuối độ trễ ngân sách, có thể (bạn) tách 𝐿lat,compute khỏi
𝐿lat,wait và giải thích (cái) nào (một) việc xếp hàng đợi lý thuyết một cách chủ yếu dự đoán (hay không)? (Wait vs. compute: Given an end-to-end latency budget, can you separate 𝐿lat,compute from 𝐿lat,wait and explain which one queuing theory primarily predicts?)
□Công suất việc lập kế hoạch: Có thể (bạn) giải thích tại sao một thông lượng con số (number) là chỉ “thực sự” nếu các yêu cầu
vẫn đáp ứng phân vị độ trễ SLO dưới tải (hay không)? (Capacity planning: Can you explain why a throughput number is only “real” if requests still meet the percentile latency SLO under load?)
□Khoảng không (sự) ước tính: Để giữ p99 (ở) dưới 50 ms tại 2,000 các yêu cầu mỗi giây, (hãy) ước tính (cái)
trung bình đang bay yêu cầu số đếm 𝑄req = 𝜆arr𝑇lat ngụ ý, và cách (mức độ) nhanh đó lề (margin) thu hẹp
khi 𝜌serv đi qua (passes) 0.7 (Headroom estimate: To hold p99 under 50 ms at 2,000 requests per second, estimate the average in-flight request count 𝑄req = 𝜆arr𝑇lat implies, and how fast that margin shrinks as 𝜌serv passes 0.7).
Khoan dung-đuôi các kỹ thuật được kiểm tra trong phần này tối ưu hóa luồng (flow) của các yêu cầu thông qua một
đang hoạt động (functioning) việc phục vụ hệ thống (The tail-tolerant techniques examined in this section optimize the flow of requests through a functioning serving system). Việc xếp hàng đợi sự phân tích, tuy nhiên, giả định hai chí mạng các điều kiện tiên quyết (preconditions): rằng
các mô hình được tải và sẵn sàng để xử lý các yêu cầu, và rằng các dự đoán khớp (với) (những) gì đã (được) xác nhận (validated)
trong suốt sự phát triển (The queuing analysis, however, assumes two critical preconditions: that models are loaded and ready to process requests, and that predictions match what was validated during development). Trong sản xuất, giả định này thất bại một cách thường xuyên: trong suốt các sự triển khai, (các) mới (mô hình)

13. Mô hình Việc phục vụ (Model Serving)
736
13.6 Mô hình Vòng đời Sự quản lý (Model Lifecycle Management)
các phiên bản (instances) phải tải các mô hình từ đầu (from scratch); trong suốt sự mở rộng các sự kiện, lạnh khởi động độ trễ ảnh hưởng (tới) (những) đầu tiên
các yêu cầu (tới) mới các bản sao; và khi sự tiền xử lý các đường ống phân kỳ từ sự đào tạo, độ chính xác (một cách) im lặng
suy giảm (degrades) (instances must load models from scratch; during scaling events, cold start latency affects the first requests to new replicas; and when preprocessing pipelines diverge from training, accuracy silently degrades). Tiếp theo phần kiểm tra những vòng đời các thách thức này (thứ) mà phải được giải quyết trước khi việc xếp hàng đợi
sự tối ưu hóa trở nên có liên quan (The next section examines these lifecycle challenges that must be solved before queuing optimization becomes relevant).
13.6 Mô hình Vòng đời Sự quản lý
Việc xếp hàng đợi lý thuyết và khoan dung-đuôi các kỹ thuật tối ưu hóa ổn định-trạng thái (steady-state) luồng của các yêu cầu, nhưng chúng
không thể giúp nếu hệ thống không bao giờ đạt tới ổn định trạng thái (Queuing theory and tail-tolerant techniques optimize the steady-state flow of requests, but they cannot help if the system never reaches steady state). Một mới (được) triển khai bản sao thứ mà tốn 35 các giây
để biên dịch TensorRT công cụ (engine) của nó vi phạm mọi SLO trong suốt khoảng thời gian đó (đó cửa sổ) (A newly deployed replica that takes 35 seconds to compile its TensorRT engine violates every SLO during that window). Một mô hình mà (có) (dựa) trên-OpenCV (OpenCV-based)
việc phục vụ đường ống thay đổi kích thước các hình ảnh một cách khác biệt (khác) (so với) (dựa) trên-PIL sự đào tạo đường ống (một cách) im lặng đánh rơi (drops)
5 tỷ lệ phần trăm các điểm của độ chính xác—một sự suy giảm (vô hình) với độ trễ các bảng điều khiển (dashboards) (A model whose OpenCV-based serving pipeline resizes images differently than the PIL-based training pipeline silently drops 5 percentage points of accuracy—a degradation invisible to latency dashboards). Những vòng đời các sự thất bại này
không (phải là) cạnh các trường hợp; chúng xảy ra tại mọi sự triển khai, mọi sự mở rộng sự kiện, và mọi bộ khung (framework) sự di chuyển (migration) (These lifecycle failures are not edge cases; they occur at every deployment, every scaling event, and every framework migration).
Việc giải quyết chúng yêu cầu kỹ thuật kỷ luật (discipline) trong hai các lĩnh vực (areas): việc làm (cho) các mô hình sẵn sàng để phục vụ (lạnh
khởi động và sự khởi tạo (initialization)) và việc giữ các dự đoán (trung thành) với (những) gì đã (được) xác nhận (đào tạo-phục vụ
sự lệch (skew)) (Addressing them requires engineering discipline in two areas: getting models ready to serve (cold start and initialization) and keeping predictions faithful to what was validated (training-serving skew)).
13.6.1 Sự đào tạo-việc phục vụ sự lệch (Training-serving skew)
Một mô hình thứ mà thực hiện tốt trong suốt sự xác nhận (validation) có thể một cách im lặng suy giảm khi (được) triển khai (A model that performed well during validation may silently degrade when deployed). Hiện-
tượng này, được biết đến như (là) sự đào tạo-việc phục vụ sự lệch, đại diện một trong (những) tinh tế nhất sự thất bại các chế độ trong
sản xuất ML bởi vì nó là vô hình (invisible) đối với độ trễ sự giám sát và ngoại lệ việc theo dõi (Sculley và cộng sự
2015; Baylor và cộng sự 2017) (This phenomenon, known as training-serving skew, represents one of the most subtle failure modes in production ML because it is invisible to latency monitoring and exception tracking (Sculley et al. 2015; Baylor et al. 2017)).
Định nghĩa 13.3: Sự đào tạo-việc phục vụ sự lệch
Sự đào tạo-Việc phục vụ Sự lệch là thuộc về phân phối (distributional) sự phân kỳ giữa sự đào tạo và sự suy luận
các môi trường được gây ra bởi không nhất quán (inconsistent) logic hay trạng thái (Training-Serving Skew is the distributional divergence between the training and inference environments caused by inconsistent logic or state).
1. Tầm quan trọng: Nó vi phạm tính nhất quán mệnh lệnh (imperative), việc gây ra im lặng độ chính xác sự suy giảm
tương ứng (proportional) với sự khác biệt trong sự biến đổi các hàm (functions) (𝑓train(𝑥) ≠ 𝑓serve(𝑥)) (It violates the consistency imperative, causing silent accuracy degradation proportional to the difference in the transformation functions (𝑓train(𝑥) ≠𝑓serve(𝑥))).
2. Sự khác biệt: Không giống như dữ liệu sự trôi dạt (drift) (thứ mà là một bên ngoài sự dịch chuyển trong môi trường), sự đào tạo-
việc phục vụ sự lệch là một nội bộ sự thất bại của kỹ thuật ngăn xếp (Unlike data drift (which is an external shift in the environment), training-serving skew is an internal failure of the engineering stack).
3. Phổ biến cạm bẫy: Một thường xuyên quan niệm sai lầm là rằng sự lệch (được) “tìm thấy” bằng cách việc tìm kiếm cho các lỗi (A frequent misconception is that skew is “found” by looking for errors).
Trong thực tế, nó là vô hình đối với các ngoại lệ: hệ thống chạy một cách hoàn hảo và độ trễ là thấp,
nhưng các dự đoán là (về mặt) thống kê (statistically) sai (In reality, it is invisible to exceptions: the system runs perfectly and the latency is low, but the predictions are statistically wrong).
Chương 14 cung cấp toàn diện sự phủ sóng (coverage) của sự lệch sự chẩn đoán (diagnosis), sự giám sát, và thuộc về tổ chức (organizational)
sự phòng ngừa các chiến lược (Chapter 14 provides comprehensive coverage of skew diagnosis, monitoring, and organizational prevention strategies). Ở đây chúng ta tập trung trên cụ thể-việc phục vụ sự biểu hiện (manifestation): sự tiền xử lý sự phân kỳ (Here we focus on the serving-specific manifestation: preprocessing divergence).
Điều này xảy ra khi thời gian thực sự suy luận đường ống xử lý thô dữ liệu một cách khác biệt (khác) (so với) lô (batch)
sự đào tạo đường ống, một phổ biến sự thất bại chế độ khi sự đào tạo sử dụng Python/Pandas trong khi việc phục vụ sử dụng
C++/Java hay được tối ưu hóa sự suy luận các máy chủ (This occurs when the real-time inference pipeline processes raw data differently than the batch training pipeline, a common failure mode when training uses Python/Pandas while serving uses C++/Java or optimized inference servers). Không giống như dữ liệu sự trôi dạt (thứ mà Chương 14 giải quyết thông qua
sự giám sát), sự tiền xử lý sự phân kỳ là mang tính xác định và có thể phòng ngừa (preventable) thông qua cẩn thận kỹ thuật (Unlike data drift (which Chapter 14 addresses through monitoring), preprocessing divergence is deterministic and preventable through careful engineering).
Ví dụ 13.2: ResNet-50: Hình ảnh sự tiền xử lý sự lệch
Kịch bản: Cho ResNet-50 việc phục vụ, ba sự tiền xử lý các sự lựa chọn một cách phổ biến phân kỳ giữa
sự đào tạo và việc phục vụ các đường ống (Scenario: For ResNet-50 serving, three preprocessing choices commonly diverge between training and serving pipelines).
• Thay đổi kích thước sự nội suy (interpolation): Sự đào tạo sử dụng PIL.BILINEAR trong khi OpenCV mặc định (tới) cv2.IN-
TER_LINEAR (Resize interpolation: Training uses PIL.BILINEAR while OpenCV defaults to cv2.INTER_LINEAR). Những (sự nội suy) này tạo ra cấp độ-pixel (pixel-level) các sự khác biệt (thứ) mà có thể dịch chuyển độ chính xác bởi 0.5–1
phần trăm (These produce pixel-level differences that can shift accuracy by 0.5–1 percent).
• Màu sắc không gian (Color space) việc xử lý: JPEG việc tải trong khác biệt các thư viện có thể tạo ra BGR so với RGB
sự sắp xếp (ordering) (Color space handling: JPEG loading in different libraries may produce BGR vs. RGB ordering). Nếu mô hình (đã) được đào tạo trên RGB nhưng phục vụ BGR các đầu vào, các dự đoán là về cơ bản (essentially)
ngẫu nhiên (If the model trained on RGB but serves BGR inputs, predictions are essentially random).

738
13.6 Mô hình Vòng đời Sự quản lý
16
CUDA (Compute (Sự tính toán)
Unified (Được hợp nhất) Device (Thiết bị) Architecture (Kiến trúc)):
NVIDIA’s song song tính toán
nền tảng (Nickolls và cộng sự 2008),
được đặt tên cho (của) nó mục tiêu của việc hợp nhất
đa dạng GPU đổ bóng (shader) các mô hình
thành một đơn chung-mục đích
kiến trúc.
Trước CUDA,
GPU việc lập trình yêu cầu (đòi hỏi)
việc ngụy trang (disguising) các sự tính toán như
đồ họa các hoạt động.
CUDA
ngữ cảnh—(cái) dữ liệu
cấu trúc (đang) theo dõi bộ nhớ
các sự cấp phát, (các) được tải hạt nhân,
và thiết bị trạng thái—là thời gian chạy’s (run-
time) mỗi-tiến trình cổng (gateway) (vào)
GPU các tài nguyên; trong không máy chủ (serverless)
hay (một cách) nhanh chóng mở rộng việc phục vụ
các hệ thống,
ngữ cảnh
sự tạo (ra)
và lười biếng mô-đun (module) việc tải có thể
trở thành có thể nhìn thấy (những) phần của lạnh
khởi động độ trễ (NVIDIA 2026a).
17
CUDA MPS (Multi-
Process (Nhiều-Tiến trình)
Service (Dịch vụ)):
MPS
tạo (ra) một điều khiển trình nền (daemon)
(thứ) mà
cho phép
CUDA
công việc
từ khác biệt các tiến trình (để)
chồng chéo trên GPU, thứ mà
có thể cải thiện sự sử dụng và
giảm thiểu
chuyển đổi-ngữ cảnh (context-switching)
chi phí hoạt động
khi
các tiến trình
(một cách) cá nhân
sử dụng dưới (mức) (underuse)
máy gia tốc (NVIDIA 2026d).
Cho
nhiều-mô hình
việc phục vụ,
MPS có thể giúp các bản sao chia sẻ
GPU luồng (streaming) các bộ đa xử lý (multiproces-
sors) (một cách) hiệu quả. (Sự) đánh đổi
là lỗi sự cô lập: các máy khách chia sẻ
được quản lý bởi-MPS GPU trạng thái, do đó
phần cứng việc phân vùng (partitioning) với
Nhiều-Phiên bản GPU (Multi-Instance GPU - MIG)
cung cấp mạnh hơn sự cô lập
tại chi phí của cố định phân vùng
độ chi tiết (granularity).
Bảng 13.8: ResNet-50 lạnh khởi động dòng thời gian: Mỗi-giai đoạn các thời lượng cho trọng số việc tải, CUDA ngữ cảnh sự tạo, TensorRT
sự biên dịch, và sự khởi động, với các tổng (số) cho (cái) được tối ưu hóa cục bộ trường hợp và (cái) đầu tiên-sự triển khai đám mây trường hợp việc cho thấy nơi
thống trị chi phí sống (ResNet-50 cold start timeline: Per-phase durations for weight loading, CUDA context creation, TensorRT compilation, and warmup, with totals for the optimized local case and the first-deploy cloud case showing where the dominant cost lives).
Giai đoạn
Thời lượng
Các ghi chú
Trọng số việc tải (SSD)
0.5 s
98 MB FP32 các trọng số từ cục bộ lưu trữ
Trọng số việc tải (S3)
3–5 s
Mạng độ trễ thống trị cho đám mây lưu trữ
CUDA ngữ cảnh
0.3–0.5 s
GPU trình điều khiển (driver) sự khởi tạo và bộ nhớ thiết lập
TensorRT sự biên dịch
15–30 s
Chuyển đổi PyTorch mô hình thành được tối ưu hóa công cụ
Sự khởi động (10 các sự suy luận)
0.2 s
Kích hoạt (cái) còn lại lười biếng sự khởi tạo
Thời gian chạy chi phí hoạt động
0.4 s
Tiến trình sự khởi nghiệp, bộ khung các móc (hooks), và thời gian chạy thiết lập
Tổng cộng (cục bộ, được tối ưu hóa)
~1.5 s
Với được biên dịch trước TensorRT công cụ, ấm áp (warm) vùng chứa (container)
Tổng cộng (đám mây, đầu tiên sự triển khai)
~35 s
Bao gồm sự biên dịch từ lạnh trạng thái
Các hệ thống sự thấu hiểu: Việc biên dịch trước các mô hình và việc lưu trữ (cái) được tối ưu hóa công cụ loại bỏ (cái) 30-
giây sự biên dịch giai đoạn trên (các) tiếp theo các sự triển khai (Systems insight: Precompiling models and storing the optimized engine eliminates the 30-second compilation phase on subsequent deployments).
CUDA ngữ cảnh16 là (cái) đầu tiên chi phí trong lạnh khởi động dòng thời gian (The CUDA context16 is the first cost in the cold start timeline). Trước khi bất kỳ GPU hoạt động (nào),
CUDA thời gian chạy phải thiết lập một ngữ cảnh: một dữ liệu cấu trúc thứ mà theo dõi bộ nhớ các sự cấp phát, (các) được tải
các hạt nhân, và thiết bị trạng thái (Before any GPU operation, the CUDA runtime must establish a context: a data structure that tracks memory allocations, loaded kernels, and device state). Việc tạo một ngữ cảnh yêu cầu việc giao tiếp với GPU trình điều khiển và
việc cấp phát GPU bộ nhớ cho nội bộ việc ghi chép sổ sách (bookkeeping) (Creating a context requires communicating with the GPU driver and allocating GPU memory for internal bookkeeping). 0.3–0.5 s giá trị trong bảng 13.8 là một kịch bản
giả định cho này lạnh-khởi động ngân sách, không (phải) một phổ quát CUDA hằng số (The 0.3–0.5 s value in table 13.8 is a scenario assumption for this cold-start budget, not a universal CUDA constant). CUDA lười biếng việc tải trì hoãn
một số mô-đun và hạt nhân việc tải cho đến khi (lần) đầu tiên sử dụng, việc giảm thiểu bề ngoài (apparent) khởi nghiệp thời gian nhưng việc dịch chuyển một số
chi phí (sang) (cái) đầu tiên sự suy luận (NVIDIA 2026a) (CUDA lazy loading defers some module and kernel loading until first use, reducing apparent startup time but shifting some cost to the first inference (NVIDIA 2026a)).
CUDA MPS (Nhiều-Tiến trình Dịch vụ)17 giải quyết GPU việc chia sẻ cho nhiều-tiến trình các sự triển khai (CUDA MPS (Multi-Process Service)17 addresses GPU sharing for multi-process deployments).
Thông thường, mỗi tiến trình tạo ra (của) riêng nó CUDA ngữ cảnh, và GPU có thể cắt-lát-thời-gian (time-slice) giữa các ngữ cảnh (Normally, each process creates its own CUDA context, and the GPU may time-slice between contexts).
MPS cho phép công việc từ nhiều các tiến trình (để) chồng chéo trên GPU thông qua một được chia sẻ dịch vụ, việc giảm thiểu
chuyển đổi-ngữ cảnh chi phí hoạt động và việc cải thiện sự sử dụng khi cá nhân các tiến trình sử dụng dưới (mức)
thiết bị (NVIDIA 2026d) (MPS allows work from multiple processes to overlap on the GPU through a shared service, reducing context-switching overhead and improving utilization when individual processes underuse the device (NVIDIA 2026d)). Sự đánh đổi là được giảm thiểu sự cô lập: một sự cố trong một tiến trình có thể ảnh hưởng (tới) (những tiến trình) khác
(đang) chia sẻ MPS máy chủ (The trade-off is reduced isolation: a crash in one process can affect others sharing the MPS server).
Không có sự khởi động, (cái) đầu tiên thực sự yêu cầu kích hoạt sự biên dịch và bộ nhớ sự cấp phát giữa-sự suy luận,
thường gây ra thời gian chờ các sự thất bại (Without warmup, the first real request triggers compilation and memory allocation mid-inference, often causing timeout failures). Một yêu cầu thứ mà thông thường tốn 5 ms có thể yêu cầu 500 ms trong suốt
lạnh khởi động, việc vi phạm các SLO và việc làm suy giảm người dùng trải nghiệm (A request that normally takes 5 ms might require 500 ms during cold start, violating SLOs and degrading user experience).
13.6.3 Việc tải các chiến lược
Khác biệt việc tải các chiến lược đánh đổi lạnh khởi động thời lượng đối nghịch việc phục vụ hiệu suất và bộ nhớ
tính hiệu quả (Different loading strategies trade off cold start duration against serving performance and memory efficiency). Đơn giản nhất cách tiếp cận, đầy đủ việc tải, đọc toàn bộ mô hình vào bộ nhớ trước khi việc phục vụ
bắt đầu (The simplest approach, full loading, reads the entire model into memory before serving begins). Điều này tối đa hóa sự suy luận tốc độ vì tất cả các trọng số là ngay lập tức (có) sẵn sàng (available), nhưng kéo dài
lạnh khởi động thời lượng và giới hạn mô hình kích thước (vào) (có) sẵn sàng bộ nhớ (This maximizes inference speed since all weights are immediately available, but extends cold start duration and limits model size to available memory). Cách tiếp cận là phù hợp (appropriate) khi
lạnh khởi động độ trễ là (có thể) chấp nhận được và các mô hình một cách thoải mái (comfortably) khớp (vừa) trong bộ nhớ (The approach is appropriate when cold start latency is acceptable and models comfortably fit in memory).
Khi các mô hình là quá lớn cho ngay lập tức đầy đủ việc tải, bộ nhớ việc ánh xạ (mapping) cung cấp một thay thế bằng cách
việc ánh xạ mô hình các tệp một cách trực tiếp vào địa chỉ không gian (address space) và việc tải các trang (pages) theo yêu cầu (on demand) khi được truy cập (When models are too large for immediate full loading, memory mapping offers an alternative by mapping model files directly into the address space and loading pages on demand as accessed). Điều này
giảm thiểu lạnh khởi động thời gian vì sự suy luận có thể bắt đầu trước khi đầy đủ mô hình (được) tải, nhưng gây ra không thể đoán trước
độ trễ khi các trang gặp lỗi (fault) trong (suốt) (những) ban đầu các yêu cầu (This reduces cold start time since inference can begin before the full model loads, but causes unpredictable latency as pages fault in during initial requests). Bộ nhớ việc ánh xạ làm việc tốt cho (một cách) không thường xuyên (infrequently)
được truy cập mô hình các thành phần nhưng có thể gây ra độ trễ các sự tăng vọt nếu chí mạng các trọng số (được) không (được) tải trước (preloaded) (Memory mapping works well for infrequently accessed model components but can cause latency spikes if critical weights are not preloaded).
Một thứ ba chiến lược, lười biếng sự khởi tạo, trì hoãn sự biên dịch và sự cấp phát cho đến khi (lần) đầu tiên sử dụng (A third strategy, lazy initialization, defers compilation and allocation until first use). Điều này tối-
thiểu hóa khởi nghiệp thời gian nhưng dịch chuyển độ trễ (sang) (cái) đầu tiên yêu cầu (This minimizes startup time but shifts latency to the first request). Sản xuất các hệ thống thường kết hợp lười biếng
sự khởi tạo với tổng hợp (synthetic) sự khởi động các yêu cầu để kích hoạt sự khởi tạo trước khi thực sự lưu lượng truy cập đến (Production systems often combine lazy initialization with synthetic warmup requests to trigger initialization before real traffic arrives).
13.6.4 Mô hình việc lưu trong bộ nhớ đệm cơ sở hạ tầng (Model caching infrastructure)
Sản xuất các hệ thống lưu trong bộ nhớ đệm mô hình các trọng số tại cơ sở hạ tầng cấp độ để giảm thiểu lạnh khởi động cho phổ biến
sự triển khai các kịch bản (Production systems cache model weights at the infrastructure level to reduce cold start for common deployment scenarios). Một cách tiếp cận, vùng chứa hình ảnh sự nhúng, bó (bundles) mô hình các trọng số một cách trực tiếp
trong vùng chứa hình ảnh (One approach, container image embedding, bundles model weights directly in the container image). Điều này tạo ra một đơn sự triển khai hiện vật và loại bỏ mạng các sự lấy (fetches)
tại sự khởi nghiệp, nhưng tạo ra lớn các hình ảnh (thường 10–50 GB) (thứ) mà làm chậm vùng chứa các sự kéo (pulls) và tiêu thụ sổ đăng ký (registry)
lưu trữ (This produces a single deployment artifact and eliminates network fetches at startup, but creates large images (often 10–50 GB) that slow container pulls and consume registry storage). Cách tiếp cận này làm việc tốt nhất cho các mô hình (thứ) mà hiếm khi cập nhật (This approach works best for models that rarely update).

13. Mô hình Việc phục vụ (Model Serving)
739
18
MIG (Multi-Instance (Nhiều-Phiên bản)
GPU):
Được giới thiệu
với
NVIDIA’s
A100
(NVIDIA
Corporation 2020) và được tài-
liệu hóa (documented) qua được hỗ trợ
dữ liệu-trung tâm (data-center) các GPU (NVIDIA
2026e),
MIG
phân vùng
một
đơn
vật lý
GPU
thành
độc lập các phiên bản, mỗi (cái)
với dành riêng tính toán và
bộ nhớ các tài nguyên.
Không giống như
phần mềm việc chia sẻ (MPS hay
việc cắt-lát-thời-gian), MIG cung cấp
cấp độ-phần cứng
sự cô lập
giữa các phân vùng.
Sự
đánh đổi
là
độ chi tiết—
các phân vùng phải tuân theo cố định
các hồ sơ (profiles), do đó các tài nguyên không thể
bị chia một cách tùy ý (arbitrarily).
Cho
nhiều-mô hình việc phục vụ,
MIG
giảm thiểu ồn ào-hàng xóm (noisy-neighbor) rủi ro
trên được chia sẻ phần cứng, trong khi
mỗi-mô hình SLO các sự đảm bảo
vẫn phụ thuộc vào bộ lập lịch
chính sách, tải, và (cái) được chọn
phân vùng hồ sơ.
Mô hình việc tải hạ cánh (lands) xa bên ngoài
một chặt chẽ việc phục vụ SLO (Model loading lands far outside a tight serving SLO).
Cho các tổ chức với nhiều các mô hình và thường xuyên các sự cập nhật, một được chia sẻ tệp hệ thống (EFS, GCS FUSE)
chứa mô hình các trọng số cung cấp một linh hoạt hơn sự thay thế (For organizations with many models and frequent updates, a shared filesystem (EFS, GCS FUSE) containing model weights provides a more flexible alternative). Nhiều các bản sao chia sẻ được lưu trong bộ nhớ đệm
các trọng số, và các sự cập nhật lan truyền (propagate) ngay lập tức mà không có sự triển khai lại (redeployment) (Multiple replicas share cached weights, and updates propagate immediately without redeployment). Sự đánh đổi là rằng mạng
độ trễ ảnh hưởng (tới) lạnh khởi động, và tệp hệ thống tính có sẵn (availability) trở thành một chí mạng sự phụ thuộc (The trade-off is that network latency affects cold start, and filesystem availability becomes a critical dependency).
Khi lạnh khởi động độ trễ là chí mạng cho cao-lưu lượng truy cập các mô hình, nút-cục bộ (node-local) SSD việc lưu trong bộ nhớ đệm đưa (dữ liệu) vào trước (prepopulates) cục bộ
các SSD trên sự suy luận các nút với thường xuyên-được sử dụng các mô hình (When cold start latency is critical for high-traffic models, node-local SSD caching prepopulates local SSDs on inference nodes with frequently-used models). Cách tiếp cận này cung cấp nhanh việc tải từ
Không-Bay hơi (Non-Volatile) Bộ nhớ Tốc hành (Express) (NVMe) các ổ đĩa tại 500 MB/s hay hơn mà không có mạng sự phụ thuộc,
nhưng yêu cầu bộ nhớ đệm sự quản lý để xử lý mô hình các sự cập nhật và công suất các giới hạn (This approach provides fast loading from Non-Volatile Memory Express (NVMe) drives at 500 MB/s or more without network dependency, but requires cache management to handle model updates and capacity limits). Sự lựa chọn giữa
những các chiến lược này phụ thuộc vào mô hình cập nhật tần suất (frequency): không thường xuyên các sự cập nhật ưu ái (favor) vùng chứa sự nhúng,
thường xuyên các sự cập nhật ưu ái được chia sẻ tệp hệ thống, và chí mạng-hiệu suất các sự triển khai hưởng lợi từ cục bộ
việc lưu trong bộ nhớ đệm với nền (background) sự làm mới (refresh) (The choice among these strategies depends on model update frequency: infrequent updates favor container embedding, frequent updates favor shared filesystem, and performance-critical deployments benefit from local caching with background refresh).
13.6.5 Nhiều-mô hình việc phục vụ (Multi-model serving)
Sản xuất các hệ thống thường phục vụ nhiều các mô hình từ một đơn máy móc, cho dù khác biệt mô hình
các phiên bản (versions) cho A/B việc kiểm tra, tập hợp các thành phần, hay hoàn toàn khác biệt các mô hình (đang) chia sẻ cơ sở hạ tầng (Production systems often serve multiple models from a single machine, whether different model versions for A/B testing, ensemble components, or entirely different models sharing infrastructure).
GPU bộ nhớ trở thành (cái) giới hạn tài nguyên, việc yêu cầu cẩn thận sự quản lý các chiến lược (GPU memory becomes the limiting resource, requiring careful management strategies).
Ba các chiến lược giải quyết nhiều-mô hình bộ nhớ sự quản lý (Three strategies address multi-model memory management). Cắt ghép-thời gian (Time-multiplexing) tải một mô hình
tại một thời điểm và hoán đổi (swaps) dựa trên yêu cầu việc định tuyến—đơn giản nhưng giới thiệu hoán đổi độ trễ (Time-multiplexing loads one model at a time and swaps based on request routing—simple but introduces swap latency). Bộ nhớ
việc chia sẻ (Memory sharing) phân vùng GPU bộ nhớ (giữa) các mô hình, việc giới hạn đồng thời sự thực thi số đếm nhưng việc kích hoạt
nhiều (hơn) các mô hình (để) duy trì thường trú (resident) (Memory sharing partitions GPU memory among models, limiting concurrent execution count but enabling more models to remain resident). Mô hình sự ảo hóa (Model virtualization), như được triển khai bởi các bộ khung như Triton,
tách biệt mô hình vòng đời khỏi ứng dụng mã thông qua mô hình kho lưu trữ và điều khiển các API cho
việc tải, việc dỡ (unloading), và việc tạo phiên bản (versioning) các mô hình (NVIDIA 2024d, 2026c, 2026b) (Model virtualization, as implemented by frameworks like Triton, separates model lifecycle from application code through model repository and control APIs for loading, unloading, and versioning models (NVIDIA 2024d, 2026c, 2026b)). Sự lựa chọn phụ thuộc
vào yêu cầu các mẫu (patterns): nếu các mô hình nhận lưu lượng truy cập (một cách) đồng đều, đồng thời việc tải làm việc; nếu lưu lượng truy cập là (có tính) đợt (bursty)
và cụ thể-mô hình, việc cắt ghép-thời gian với rõ ràng (explicit) việc tải trước (preloading) giảm thiểu trung bình độ trễ trong khi
việc tối đa hóa GPU sự sử dụng (The choice depends on request patterns: if models receive traffic evenly, concurrent loading works; if traffic is bursty and model-specific, time-multiplexing with explicit preloading reduces average latency while maximizing GPU utilization).
13.6.5.1 Nhiều-luồng (Multi-stream) sự thực thi
Khi nhiều các mô hình hay nhiều các phiên bản của giống nhau mô hình phải chạy (một cách) đồng thời trên một đơn
GPU, phần cứng phải phân vùng các tài nguyên giữa chúng (When multiple models or multiple instances of the same model must run concurrently on a single GPU, the hardware must partition resources between them). NVIDIA’s Nhiều-Phiên bản GPU18
công nghệ kích hoạt cấp độ-phần cứng sự cô lập, việc chia một A100 thành lên tới bảy độc lập GPU
các phiên bản, mỗi (cái) với dành riêng bộ nhớ và tính toán các tài nguyên (NVIDIA 2026e) (NVIDIA’s Multi-Instance GPU18 technology enables hardware-level isolation, dividing an A100 into up to seven independent GPU instances, each with dedicated memory and compute resources (NVIDIA 2026e)). MIG là (có) sẵn sàng
trên A100, A30 (lên tới bốn các phiên bản), H100, H200, và mới hơn dữ liệu trung tâm các GPU (MIG is available on A100, A30 (up to four instances), H100, H200, and newer data center GPUs). Cho cũ hơn các GPU
như là V100 hay T4, CUDA luồng sự lập lịch cung cấp (được) cắt ghép-thời gian việc chia sẻ mà không có phần cứng
sự cô lập (For older GPUs such as V100 or T4, CUDA stream scheduling provides time-multiplexed sharing without hardware isolation). Sự lựa chọn phụ thuộc vào liệu nhất quán độ trễ với MIG hay tối đa sự sử dụng với
(được) chia sẻ các luồng là sự ưu tiên (hay không) (The choice depends on whether consistent latency with MIG or maximum utilization with shared streams is the priority).
13.6.5.2 Mô hình sự hoán đổi (swapping) và máy chủ bộ nhớ
Khi tổng hợp (aggregate) kích thước của tất cả các mô hình vượt quá GPU bộ nhớ công suất, việc phục vụ hệ thống phải hoán đổi
các mô hình giữa máy chủ bộ nhớ (DRAM) và thiết bị bộ nhớ (VRAM) theo yêu cầu (When the aggregate size of all models exceeds GPU memory capacity, the serving system must swap models between host memory (DRAM) and device memory (VRAM) on demand). Điều này giới thiệu một
mới độ trễ thành phần (được) xác định bởi PCIe bus băng thông (This introduces a new latency component determined by the PCIe bus bandwidth).
Cho một 10 GB mô hình trên PCIe Gen4 x16 (32 GB/s lý thuyết băng thông), việc tải tốn ít nhất 312.5
ms trước khi sự giải tuần tự hóa (deserialization), đồ thị thiết lập, hay sự khởi động (For a 10 GB model on PCIe Gen4 x16 (32 GB/s theoretical bandwidth), loading takes at least 312.5 ms before deserialization, graph setup, or warmup).
Để giảm nhẹ điều này, các hệ thống sử dụng được ghim (pinned) bộ nhớ (được khóa-trang máy chủ bộ nhớ) (To mitigate this, systems use pinned memory (page-locked host memory)). Theo mặc định, hoạt động
hệ thống (hệ điều hành) có thể di chuyển (“phân trang” (page)) bất kỳ bộ nhớ khu vực (nào) tới đĩa khi RAM là dưới áp lực (By default, the operating system can move (“page”) any memory region to disk when RAM is under pressure). Điều này tạo ra một
vấn đề cho GPU các sự truyền (transfers): nếu GPU’s DMA (Trực tiếp Bộ nhớ Truy cập) công cụ bắt đầu (việc) đọc một
bộ nhớ khu vực (thứ) mà bị (get) phân trang ra (paged out) giữa-sự truyền, sự truyền thất bại hay (bị) đình trệ (This creates a problem for GPU transfers: if the GPU’s DMA (Direct Memory Access) engine begins reading a memory region that gets paged out mid-transfer, the transfer fails or stalls). Để tránh điều này, CPU
phải trước tiên sao chép dữ liệu tới một tạm thời được ghim bộ đệm trước khi GPU có thể một cách an toàn đọc nó, việc thêm cả hai
độ trễ và CPU chi phí hoạt động (To avoid this, the CPU must first copy data to a temporary pinned buffer before the GPU can safely read it, adding both latency and CPU overhead).
Việc ghim bộ nhớ hướng dẫn (instructs) HĐH (OS) (để) giữ đó khu vực (một cách) vĩnh viễn (permanently) trong vật lý RAM (Pinning memory instructs the OS to keep that region permanently in physical RAM). GPU’s
DMA công cụ có thể sau đó truyền dữ liệu một cách trực tiếp từ (cái) được ghim khu vực mà không có một bổ sung (extra) (từ) có-thể-phân-trang-tới-
được ghim (pageable-to-pinned) dàn dựng (staging) bản sao (The GPU’s DMA engine can then transfer data directly from the pinned region without an extra pageable-to-pinned staging copy). Sự đánh đổi là rằng được ghim bộ nhớ giảm thiểu RAM (có) sẵn sàng cho (các tiến trình) khác
các tiến trình và không thể (được) đòi lại (reclaimed) dưới bộ nhớ áp lực (The trade-off is that pinned memory reduces the RAM available for other processes and cannot be reclaimed under memory pressure). Cho mô hình việc phục vụ, sự truyền-con đường
sự cải thiện thường biện minh (cho) (justifies) việc ghim mô hình các trọng số và thường xuyên-được sử dụng đầu vào các bộ đệm, trong khi việc để lại
ít chí mạng (hơn) bộ nhớ (để) có thể phân trang (For model serving, the transfer-path improvement often justifies pinning model weights and frequently-used input buffers, while leaving less critical memory pageable).
Vòng đời sự quản lý các chiến lược được kiểm tra cho đến nay đảm bảo các mô hình là sẵn sàng để phục vụ: (được) tải vào
bộ nhớ, (được) làm ấm lên (warmed up), và (đang) tạo ra các dự đoán nhất quán với sự đào tạo (The lifecycle management strategies examined so far ensure models are ready to serve: loaded into memory, warmed up, and producing predictions consistent with training). Với những các điều kiện tiên quyết này (With these prerequisites)

13. Mô hình Việc phục vụ (Model Serving)
740
13.7 Thông lượng Sự tối ưu hóa (Throughput Optimization)
19
Lô (Batch): Từ Cũ Tiếng Pháp (Old French)
bache (một số lượng được nướng tại
một thời điểm), (việc) đi vào điện-
toán trong những năm 1950 cho các công việc (được) xử-
lý (processed) cùng nhau mà không có con-
người sự tương tác. ML việc phục-
vụ cách sử dụng bảo tồn (preserves) (cái) ban-
đầu sự đánh đổi:
việc nhóm các yêu-
cầu khấu hao (amortizes) cố định các chi phí
(hạt nhân sự khởi chạy, trọng số việc tải)
qua nhiều các đầu vào,
nhưng mỗi yêu cầu phải chờ đợi
cho lô (để) lấp đầy (fill). Trong sự đào-
tạo, các lô của 256–4096 là
thông thường (routine); trong việc phục vụ, các lô
trên 8–32 điển hình vi phạm độ trễ
các SLO, việc làm việc phục-
vụ lô (trở thành) một (về mặt) cơ bản khác biệt
sự tối ưu hóa mục tiêu.
20
Hạt nhân (Kernel) (GPU): CUDA
đã mượn
này
thuật ngữ
từ
hoạt động
các hệ thống
khoảng (circa)
2007 bởi vì GPU các hàm
đại diện (cái) thuộc về tính toán
“cốt lõi” (core) của song song các thuật toán.
Không giống như HĐH (OS) các hạt nhân (thứ) mà chạy
(một cách) liên tục, GPU các hạt nhân
là rời rạc (discrete) các đơn vị của song song
công việc (được) khởi chạy bởi CPU.
Mỗi sự khởi chạy mang (carries) 5–20 𝜇s
của chi phí hoạt động độc lập với
lô
kích thước—không đáng kể (negligible)
cho
lớn sự đào tạo các lô nhưng
thống trị tại lô-1 việc phục vụ,
nơi
một
50-lớp (layer)
mô hình
tích lũy (accumulates) 250–1000 𝜇s của
thuần túy (pure) sự khởi chạy chi phí hoạt động cho mỗi
sự suy luận.
được thỏa mãn (satisfied), việc xếp hàng đợi động lực học từ phần 13.5 trở nên có liên quan (satisfied, the queuing dynamics from section 13.5 become relevant). Tiếp theo sự tối ưu hóa cơ-
hội (opportunity) nằm trong cách các yêu cầu được nhóm (lại) cho việc xử lý, thứ mà một cách trực tiếp ảnh hưởng (tới) cả thông lượng và
độ trễ các thuật ngữ (terms) trong (của) chúng ta việc xếp hàng đợi các phương trình (The next optimization opportunity lies in how requests are grouped for processing, which directly affects both the throughput and latency terms in our queuing equations).
13.7 Thông lượng Sự tối ưu hóa
Hãy xem xét một đại diện ResNet-50 bộ phân loại kịch bản trên một V100 GPU tại lô kích thước một: GPU
xử lý một hình ảnh, sau đó ngồi nhàn rỗi (idle) trong khi CPU lấy (fetches) và tiền xử lý (cái) tiếp theo—việc đạt được chỉ
15 phần trăm phần cứng sự sử dụng và 200 các hình ảnh mỗi giây (Consider a representative ResNet-50 classifier scenario on a V100 GPU at batch size one: the GPU processes one image, then sits idle while the CPU fetches and preprocesses the next—achieving only 15 percent hardware utilization and 200 images per second). Giống nhau GPU (đang) xử lý 32 các hình ảnh tại
(cùng) một lúc đạt tới 95 phần trăm sự sử dụng và 1,280 các hình ảnh mỗi giây, một 6.4× thông lượng sự cải thiện
trên giống hệt phần cứng bởi vì cố định các chi phí được khấu hao qua các yêu cầu (The same GPU processing 32 images at once reaches 95 percent utilization and 1,280 images per second, a 6.4× throughput improvement on identical hardware because fixed costs are amortized across requests). Sự khác biệt là việc tạo lô (batching),
cốt lõi đòn bẩy (lever) cho việc cải thiện việc phục vụ tính kinh tế (economics) (The difference is batching, the core lever for improving serving economics). Việc tạo lô19 khác biệt (một cách) sắc bén giữa sự đào tạo và
việc phục vụ (Crankshaw và cộng sự 2017) (Batching19 differs sharply between training and serving (Crankshaw et al. 2017)). Sự đào tạo các lô tối đa hóa thông lượng bằng cách việc xử lý hàng trăm
hay hàng ngàn (của) các mẫu (samples) cùng nhau với không (có) mối bận tâm (concern) cho cá nhân mẫu độ trễ (Training batches maximize throughput by processing hundreds or thousands of samples together with no concern for individual sample latency). Việc phục vụ các lô
phải cân bằng thông lượng đối nghịch cá nhân yêu cầu độ trễ, thường (việc) xử lý nhỏ các lô trong khi
việc đảm bảo không yêu cầu (nào) chờ đợi quá lâu (Serving batches must balance throughput against individual request latency, often processing small batches while ensuring no request waits too long). Này thích ứng cách tiếp cận được gọi (là) động (dynamic) việc tạo lô bởi vì
hệ thống điều chỉnh lô thành phần (composition) trong thực thời gian dựa trên (đang) đến các yêu cầu (This adaptive approach is called dynamic batching because the system adjusts batch composition in real time based on arriving requests).
Định nghĩa 13.5: Động việc tạo lô (Dynamic batching)
Động Việc tạo lô là ML việc phục vụ sự tối ưu hóa (thứ) mà đánh đổi Độ trễ cho Thông lượng dưới
ngẫu nhiên (stochastic) đến các mẫu (Dynamic Batching is the ML serving optimization that trades Latency for Throughput under stochastic arrival patterns).
1. Tầm quan trọng: Bằng cách việc đệm (buffering) các yêu cầu vào một việc tạo lô cửa sổ, bộ lập lịch khấu hao
cố định các chi phí hoạt động (𝐿lat) qua nhiều các đầu vào, việc đẩy hệ thống ra xa khỏi bị giới hạn-bởi-bộ-nhớ
chế độ (regime) (BW) hướng tới bị giới hạn-bởi-tính-toán chế độ (𝑅peak) (By buffering requests into a batching window, the scheduler amortizes fixed overheads (𝐿lat) across multiple inputs, pushing the system away from the memory-bound regime (BW) toward the compute-bound regime (𝑅peak)).
2. Sự khác biệt: Không giống như Tĩnh Việc tạo lô (Static Batching), thứ mà được cố định trong suốt sự đào tạo, Động Việc tạo lô
(một cách) thích ứng điều chỉnh lô kích thước tại Sự suy luận Thời gian dựa trên thực-thời gian lưu lượng truy cập khối lượng (Unlike Static Batching, which is fixed during training, Dynamic Batching adaptively adjusts the batch size at Inference Time based on real-time traffic volume).
3. Phổ biến cạm bẫy: Một thường xuyên quan niệm sai lầm là rằng việc tạo lô “luôn luôn giúp ích” (A frequent misconception is that batching “always helps.”). Trong thực tế,
có một độ trễ-thông lượng Pareto biên giới (frontier): nếu việc tạo lô cửa sổ là quá lớn, (cái)
được làm tăng việc xếp hàng đợi sự chậm trễ có thể vi phạm hệ thống’s SLO trước khi thông lượng các lợi ích (gains) được
nhận ra (realized) (In reality, there is a latency-throughput Pareto frontier: if the batching window is too large, the increased queuing delay may violate the system’s SLO before the throughput gains are realized).
13.7.1 Tại sao việc tạo lô giúp ích
Hiện đại các máy gia tốc đạt được đỉnh tính hiệu quả chỉ tại đủ lô các kích thước (Shen và cộng sự 2019) (Modern accelerators achieve peak efficiency only at sufficient batch sizes (Shen et al. 2019)). Một đơn
sự suy luận yêu cầu để lại hầu hết tính toán các đơn vị (units) nhàn rỗi bởi vì các GPU được thiết kế cho song song sự thực thi
qua hàng ngàn (của) các luồng (threads) (A single inference request leaves most compute units idle because GPUs are designed for parallel execution across thousands of threads). Việc tạo lô khấu hao cố định các chi phí qua nhiều các yêu cầu và kích hoạt
song song sự thực thi qua lô chiều (dimension) (Batching amortizes fixed costs across multiple requests and enables parallel execution across the batch dimension).
Hai cố định các chi phí thống trị tại nhỏ lô các kích thước (Two fixed costs dominate at small batch sizes). Hạt nhân sự khởi chạy chi phí hoạt động20 là thời gian cho CPU
để chuẩn bị và gửi (submit) công việc tới GPU (Kernel launch overhead20 is the time for the CPU to prepare and submit work to the GPU). Mỗi lớp trong một nơ-ron mạng điển hình yêu cầu một riêng biệt
hạt nhân sự khởi chạy: CPU phải lắp ráp hạt nhân các tham số, sao chép chúng tới có-thể-truy-cập-bởi-GPU bộ nhớ,
và ra hiệu (signal) (cho) GPU để bắt đầu sự thực thi (Each layer in a neural network typically requires a separate kernel launch: the CPU must assemble kernel parameters, copy them to GPU-accessible memory, and signal the GPU to begin execution). Chi phí hoạt động này là điển hình 5–20 μs cho mỗi hạt nhân, độc lập
với lô kích thước (This overhead is typically 5–20 μs per kernel, independent of batch size). ResNet-50 có xấp xỉ năm mươi các lớp, do đó hạt nhân sự khởi chạy một mình (nó) thêm 250–1000 μs
cho mỗi sự suy luận (ResNet-50 has approximately fifty layers, so kernel launch alone adds 250–1000 μs per inference). Tại lô kích thước một, chi phí hoạt động này có thể vượt quá (cái) thực sự tính toán thời gian; tại lô kích thước
ba mươi hai, giống nhau chi phí hoạt động được khấu hao qua ba mươi hai các hình ảnh (At batch size one, this overhead may exceed the actual compute time; at batch size thirty-two, the same overhead is amortized across thirty-two images). Trọng số việc tải đọc mô hình
các tham số từ GPU bộ nhớ (VRAM) tới tính toán các đơn vị (Weight loading reads model parameters from GPU memory (VRAM) to the compute units). Tại lô kích thước một, GPU đọc tất cả
các trọng số để xử lý một hình ảnh; tại lô kích thước ba mươi hai, giống nhau trọng số (sự) đọc xử lý ba mươi hai
các hình ảnh, (việc) đạt được 32× tốt hơn bộ nhớ tính hiệu quả (At batch size one, the GPU reads all weights to process one image; at batch size thirty-two, the same weight read processes thirty-two images, achieving 32× better memory efficiency). Việc đo lường việc tạo lô tính hiệu quả trên một cụ thể mô hình
định lượng cách những cố định các chi phí này khấu hao trong thực tế (Measuring batching efficiency on a concrete model quantifies how these fixed costs amortize in practice).
Khăn ăn Toán học 13.6: ResNet-50 việc tạo lô tính hiệu quả
Bảng 13.9 minh họa (illustrates) thông lượng-độ trễ sự đánh đổi cho một ResNet-50/V100 kịch bản qua
lô các kích thước (từ) một đến (through) ba mươi hai (Table 13.9 illustrates the throughput-latency trade-off for a ResNet-50/V100 scenario across batch sizes one through thirty-two). Lô các kích thước, được đo lường sự suy luận các thời gian, và GPU

13. Mô hình Việc phục vụ
741
sự sử dụng là kịch bản (những) thứ được cho (givens); mỗi-hình ảnh tính toán và thông lượng các cột được bắt nguồn (derived)
từ chúng (utilization are the scenario givens; the per-image compute and throughput columns are derived from them).
Toán học: Cho (cái) lô-8 hàng, mỗi-hình ảnh tính toán là lô độ trễ được chia (divided) bởi lô kích thước,
9.1 ms ÷ 8 các hình ảnh ≈ 1.1 ms cho mỗi hình ảnh, và thông lượng là lô kích thước được chia bởi (cái) giống nhau
độ trễ, 8 các hình ảnh ÷ 9.1 ms ≈ 879 hình ảnh/s (Math: For the batch-8 row, per-image compute is the batch latency divided by the batch size, 9.1 ms ÷ 8 images ≈1.1 ms per image, and throughput is the batch size divided by the same latency, 8 images ÷ 9.1 ms ≈879 img/s). (Cái) giống nhau hai phép chia tạo ra mọi được bắt nguồn hàng (The same two divisions produce every derived row).
Bảng 13.9: ResNet-50 việc tạo lô (sự) quét (sweep): Mỗi-hình ảnh tính toán, thông lượng, và GPU sự sử dụng qua lô các kích thước (từ) một
đến ba mươi hai trên một V100 (Table 13.9: ResNet-50 batching sweep: Per-image compute, throughput, and GPU utilization across batch sizes one through thirty-two on a V100). Thông lượng phát triển 6.4× từ lô một tới lô ba mươi hai khi GPU sự sử dụng leo (lên) từ
15 phần trăm tới 95 phần trăm, trong khi thuần túy sự suy luận thời gian kéo dài (stretches) từ 5 ms tới 25 ms (Throughput grows 6.4× from batch one to batch thirty-two as GPU utilization climbs from 15 percent to 95 percent, while pure inference time stretches from 5 ms to 25 ms).
Lô Kích thước
Sự suy luận Thời gian
Mỗi-Hình ảnh Tính toán
Thông lượng
GPU Sự sử dụng (Util.)
1
5 ms
5 ms
200 hình ảnh/s
15%
4
7.2 ms
1.8 ms
556 hình ảnh/s
42%
8
9.1 ms
1.1 ms
879 hình ảnh/s
65%
16
14 ms
0.9 ms
1,143 hình ảnh/s
85%
32
25 ms
0.8 ms
1,280 hình ảnh/s
95%
Các thời gian được hiển thị là thuần túy sự suy luận thời gian, việc loại trừ hàng đợi sự chờ đợi; phần 13.7.6 phân tích cách
được nhận thức-bởi-người dùng độ trễ bao gồm việc tạo lô-cửa sổ sự chờ đợi (The times shown are pure inference time, excluding queue wait; section 13.7.6 analyzes how user-perceived latency includes batching-window wait).
Các hệ thống sự thấu hiểu: Lô kích thước ba mươi hai đạt được 6.4× cao hơn thông lượng (so với) lô kích thước 1 (Systems insight: Batch size thirty-two achieves 6.4× higher throughput than batch size 1).
Tuy nhiên, được nhận thức-bởi-người dùng độ trễ bao gồm cả hàng đợi sự chờ đợi và sự suy luận thời gian (However, user-perceived latency includes both queue wait and inference time). Với một 10 ms
việc tạo lô cửa sổ và 25 ms sự suy luận, tổng độ trễ đạt tới 35 ms so với 5 ms tại lô kích thước 1 (With a 10 ms batching window and 25 ms inference, total latency reaches 35 ms vs. 5 ms at batch size 1).
Bảng (này) tiết lộ thông lượng-độ trễ sự đánh đổi trong khắc nghiệt (stark) các thuật ngữ: lớn hơn các lô (một cách) quyết liệt
cải thiện phần cứng tính hiệu quả nhưng làm tăng mỗi-yêu cầu độ trễ (The table reveals the throughput-latency trade-off in stark terms: larger batches dramatically improve hardware efficiency but increase per-request latency). Trong thực tế, tối ưu lô kích thước
phụ thuộc vào cả độ trễ Dịch vụ Cấp độ Mục tiêu (SLO) và (cái) đến tỷ lệ của các yêu cầu (In practice, the optimal batch size depends on both the latency Service Level Objective (SLO) and the arrival rate of requests). (Cái)
câu hỏi (đang) đối mặt mọi việc phục vụ kỹ sư là do đó (mang tính) định lượng (quantitative): việc xác định (cái) lớn nhất lô kích thước
(thứ) mà vẫn đáp ứng một được cho độ trễ SLO (The question facing every serving engineer is therefore quantitative: determining the largest batch size that still meets a given latency SLO). Trong kịch bản này, lô kích thước 8 với một 5 ms việc tạo lô cửa sổ
có tồi tệ nhất-trường hợp người dùng độ trễ của khoảng 14 ms (5 ms đợi cộng 9 ms sự suy luận), dưới một 20 ms SLO
ngân sách (In this scenario, batch size 8 with a 5 ms batching window has worst-case user latency of about 14 ms (5 ms wait plus 9 ms inference), below a 20 ms SLO budget). (Điều) đó kiếm (được) gần 3× cao hơn dịch vụ thông lượng (so với) lô-1 việc phục vụ trên giống hệt phần cứng,
miễn là (provided) được duy trì (sustained) tải là (đủ) cao (để) lấp đầy việc tạo lô cửa sổ (That earns nearly 3× higher service throughput than batch-1 serving on the same hardware, provided sustained load is high enough to fill the batching window). Việc vẽ (Plotting) giống nhau sự đánh đổi
trong hình 13.6 tiết lộ đầu gối nơi (việc) thêm việc tạo lô dừng trả (tiền) cho (của) nó độ trễ chi phí: thông lượng
đã (đang) san phẳng (flattening) trong khi độ trễ bắt đầu (để) tăng vọt, do đó việc tạo lô vượt ra ngoài đó điểm đánh đổi khiêm tốn
công suất các lợi ích cho việc xếp hàng đợi sự chậm trễ (Plotting the same trade-off in figure 13.6 reveals the knee where extra batching stops paying for its latency cost: throughput is already flattening while latency begins to spike, so batching beyond that point trades modest capacity gains for queueing delay).
20
21
22
23
24
25
26
27
28
Lô Kích thước
200
400
600
800
1000
1200
Thông lượng (Các yêu cầu/sec)
Tối ưu
Điểm
50
100
150
200
250
300
Độ trễ (ms)
Hình 13.6: Thông lượng-Độ trễ Đầu gối: Lô kích thước so với thông lượng (màu xanh lam) và độ trễ (màu cam) (Figure 13.6: The Throughput-Latency Knee: Batch size vs. throughput (blue) and latency (orange)). Thông lượng tăng với
lô kích thước khi phần cứng sự sử dụng cải thiện, nhưng cuối cùng bão hòa (Throughput increases with batch size as hardware utilization improves, but eventually saturates). Độ trễ duy trì tương đối bằng phẳng cho đến khi đầu gối, sau (cái) đó
nó tăng vọt do (bởi) việc xếp hàng đợi (Latency remains relatively flat until the knee, after which it spikes due to queuing). Các giá trị là (mang tính) đại diện và phụ thuộc vào mô hình/phần cứng (Values are representative and depend on model/hardware).

13. Mô hình Việc phục vụ (Model Serving)
742
13.7 Thông lượng Sự tối ưu hóa
“Đầu gối” trong hình 13.6 đánh dấu điểm nơi màu xanh lam thông lượng đường cong bắt đầu (để) bình nguyên (plateau) ngay
khi (just as) màu cam độ trễ đường cong bắt đầu (của) nó (sự) sắc bén hướng lên trên (upward) sự tăng vọt (The “knee” in figure 13.6 marks the point where the blue throughput curve begins to plateau just as the orange latency curve starts its sharp upward spike). Đây là tối ưu hoạt động điểm: (việc) đẩy
lô kích thước vượt ra ngoài đầu gối và việc xếp hàng đợi các sự chậm trễ thống trị; (việc) ở lại (staying) dưới nó để lại phần cứng công suất
trên bàn (This is the optimal operating point: push batch size beyond the knee and queuing delays dominate; staying below it leaves hardware capacity on the table). Các con số là đại diện thay vì bị buộc (tied) vào một đơn điểm chuẩn (benchmark) (The numbers are representative rather than tied to a single benchmark).
Tính hiệu quả các lợi ích từ việc tạo lô đi kèm (tại) một chi phí: các yêu cầu phải chờ đợi cho lô (để) hình thành (The efficiency gains from batching come at a cost: requests must wait for the batch to form). Điều này
tạo ra một trực tiếp sự căng thẳng giữa thông lượng sự tối ưu hóa (lớn hơn các lô) và độ trễ sự tối thiểu hóa (minimization)
(ngay lập tức việc xử lý) (This creates a direct tension between throughput optimization (larger batches) and latency minimization (immediate processing)). Khác biệt việc tạo lô các chiến lược và của chúng các sự đánh đổi chi phối (govern) cách các kỹ sư
điều chỉnh (tune) này (sự) cân bằng (The different batching strategies and their trade-offs govern how engineers tune this balance).
13.7.2 Tĩnh so với động việc tạo lô
Tĩnh việc tạo lô chờ đợi cho một cố định lô kích thước trước khi việc xử lý, thứ mà là đơn giản để triển khai nhưng mong manh (fragile)
dưới có thể thay đổi (variable) lưu lượng truy cập: trong suốt thấp lưu lượng truy cập, các yêu cầu chờ đợi (một cách) vô thời hạn (indefinitely) cho một đầy (full) lô, và trong suốt cao
lưu lượng truy cập, lớn các lô làm tăng mỗi-yêu cầu độ trễ (Static batching waits for a fixed batch size before processing, which is simple to implement but fragile under variable traffic: during low traffic, requests wait indefinitely for a full batch, and during high traffic, large batches increase per-request latency). Động việc tạo lô giải quyết này sự thất bại chế độ
bằng cách việc thu thập các yêu cầu bên trong một được giới hạn (bounded) thời gian cửa sổ và việc xử lý bất cứ (những) gì đã đến khi
cửa sổ đóng lại (Olston và cộng sự 2017; NVIDIA 2024d) (Dynamic batching addresses this failure mode by collecting requests within a bounded time window and processing whatever has arrived when the window closes (Olston et al. 2017; NVIDIA 2024d)). Cửa sổ kích thước trở thành sự điều chỉnh núm (knob):
ngắn hơn các cửa sổ giảm thiểu độ trễ nhưng hy sinh thông lượng, dài hơn các cửa sổ cải thiện thông lượng
nhưng làm tăng độ trễ, và nhạy cảm-độ trễ các sự triển khai điều chỉnh cả thời gian cửa sổ và tối đa
lô kích thước đối nghịch đến mẫu, mô hình hình dạng (shape), và SLO (The window size becomes the tuning knob: shorter windows reduce latency but sacrifice throughput, longer windows improve throughput but increase latency, and latency-sensitive deployments tune both the time window and maximum batch size against arrival pattern, model shape, and SLO).
13.7.3 Động việc tạo lô độ trễ-thông lượng các sự đánh đổi
Động việc tạo lô giới thiệu một có-thể-định-lượng (quantifiable) sự căng thẳng giữa thông lượng sự tối ưu hóa và độ trễ
các sự ép buộc (Dynamic batching introduces a quantifiable tension between throughput optimization and latency constraints). Dưới sự quá tải, cơ chế là hàng đợi sự phát triển thay vì chậm hơn sự suy luận, thứ mà
kích hoạt có hệ thống (systematic) cấu hình các quyết định thay vì thử-và-sai (trial-and-error) sự điều chỉnh (Under overload, the mechanism is queue growth rather than slower inference, which enables systematic configuration decisions instead of trial-and-error tuning).
Các hệ thống Góc nhìn 13.6: Tại sao độ trễ tăng vọt dưới tải
Hãy nhớ lại từ phần 13.5.1: Little’s Định luật (𝑄req = 𝜆arr𝑇lat) chi phối tất cả ổn định các hàng đợi (Recall from section 13.5.1: Little’s Law (𝑄req = 𝜆arr𝑇lat) governs all stable queues). Khi
phần cứng (bị) bão hòa, dịch vụ tỷ lệ 𝜇 là (được) phát huy tối đa (maxed out); nếu đến tỷ lệ 𝜆arr phát triển vượt ra ngoài đó
công suất, hàng đợi độ sâu (𝑄req) tăng lên (When hardware is saturated, the service rate 𝜇 is maxed out; if the arrival rate 𝜆arr grows beyond that capacity, queue depth (𝑄req) increases). Vì 𝜇 không thể phát triển, độ trễ (𝑇lat) phải phát triển với hàng đợi
độ sâu (Since 𝜇 cannot grow, latency (𝑇lat) must grow with queue depth). Đây là lý do tại sao sự thu nhận kiểm soát (việc từ chối các yêu cầu khi 𝑇lat vượt quá một ngưỡng) là (cái)
duy nhất cách để bảo tồn độ trễ trong suốt sự quá tải (This is why admission control (rejecting requests when 𝑇lat exceeds a threshold) is the only way to preserve latency during overload).
Phương trình 13.7 phân rã (decomposes) tổng được nhận thức-bởi-người dùng độ trễ cho một được tạo lô yêu cầu thành hai các thành-
phần (Equation 13.7 decomposes the total user-perceived latency for a batched request into two components:):
𝐿lat = 𝐿lat,wait + 𝐿lat,compute(𝐵)
(13.7)
nơi 𝐿lat,wait là thời gian (được) tiêu tốn (để) chờ đợi trong việc tạo lô hàng đợi (việc tương ứng (corresponding) (với) 𝐿lat,queue trong tổng thể
độ trễ ngân sách) và 𝐿lat,compute(𝐵) là sự suy luận thời gian cho lô kích thước 𝐵 (việc bao trùm (encompassing) 𝐿lat,infer cộng
các phần của 𝐿lat,pre và 𝐿lat,post) (where 𝐿lat,wait is the time spent waiting in the batching queue (corresponding to 𝐿lat,queue in the overall latency budget) and 𝐿lat,compute(𝐵) is the inference time for batch size 𝐵(encompassing 𝐿lat,infer plus portions of 𝐿lat,pre and 𝐿lat,post)). Việc tạo lô cửa sổ 𝑇window giới hạn sự chờ đợi thời gian (𝐿lat,wait ≤ 𝑇window),
trong khi lô kích thước ảnh hưởng (tới) tính toán thời gian thông qua GPU sự sử dụng các đặc tính (while batch size affects compute time through GPU utilization characteristics).
13.7.3.1 Định lượng sự phân tích của việc tạo lô
Cho Poisson các sự đến với tỷ lệ 𝜆arr và việc tạo lô cửa sổ 𝑇window, các yêu cầu đến (một cách) đồng đều (uniformly) bên trong
cửa sổ (For Poisson arrivals with rate 𝜆arr and batching window 𝑇window, requests arrive uniformly within the window). Một yêu cầu (đang) đến tại thời gian 𝑡 bên trong cửa sổ chờ đợi 𝑇window − 𝑡 cho lô (để) đóng lại (A request arriving at time 𝑡 within the window waits 𝑇window −𝑡 for the batch to close).
Phương trình 13.8 cho thấy rằng trung bình sự chờ đợi thời gian là đơn giản (bằng) một nửa (của) cửa sổ (Equation 13.8 shows that the average wait time is simply half the window:):
𝐸[𝐿lat,wait] = 𝑇window / 2 (13.8)
Này đơn giản mối quan hệ có trực tiếp các hàm ý (This simple relationship has direct implications). Một 20 ms việc tạo lô cửa sổ thêm 10 ms trung bình
sự chờ đợi (lên tới 20 ms cho (cái) đầu tiên sự đến trong một cửa sổ; muộn hơn các sự đến chờ đợi ít hơn) bất kể của lô kích thước
(được) đạt được (A 20 ms batching window adds 10 ms average wait (up to 20 ms for the first arrival in a window; later arrivals wait less) regardless of batch size achieved). Cho một 50 ms trung bình độ trễ SLO với 5 ms sự suy luận, trung bình sự chờ đợi tiêu thụ 20 phần trăm
của độ trễ ngân sách trước khi bất kỳ tính toán (nào) bắt đầu; đuôi các SLO phải lập ngân sách (cho) (cái) đầy (full) cửa sổ (For a 50 ms mean latency SLO with 5 ms inference, the average wait consumes 20 percent of the latency budget before any computation begins; tail SLOs must budget the full window).

13. Mô hình Việc phục vụ (Model Serving)
743
13.7.3.2 Lô kích thước sự phân phối
Số lượng các yêu cầu (được) thu thập trong suốt cửa sổ 𝑇window tuân theo một Poisson phân phối với mức trung bình
𝜆arr𝑇window. Phương trình 13.9 chính thức hóa (formalizes) mối quan hệ này:
Pr(lô kích thước = 𝑘) = (𝜆arr𝑇window)𝑘𝑒−𝜆arr𝑇window / 𝑘!
(13.9)
Bảng 13.10 định lượng này tính biến đổi (variability), việc cho thấy cách lô kích thước dao động (fluctuates) cho khác biệt lưu lượng truy cập các cấp độ
với một cố định 10 ms cửa sổ:
Bảng 13.10: Lô Kích thước Tính biến đổi: Tại thấp lưu lượng truy cập, việc tạo lô các cửa sổ (một cách) thường xuyên chứa không các yêu cầu (bị lãng phí GPU các chu kỳ) (Table 13.10: Batch Size Variability: At low traffic, batching windows frequently contain zero requests (wasted GPU cycles)). Tại
vừa phải lưu lượng truy cập, lô các kích thước dao động một cách đáng kể xung quanh mức trung bình (At moderate traffic, batch sizes fluctuate significantly around the mean). Cao lưu lượng truy cập cung cấp ổn định hơn việc tạo lô, và
xác suất của các lô (việc) đạt tới ít nhất hai lần (cái) trung bình kích thước giảm thiểu khi lưu lượng truy cập phát triển (từ 39 phần trăm tại 50 QPS tới 0.3 phần trăm tại
1000 QPS), việc phản ánh định luật của lớn các con số (High traffic provides more stable batching, and the probability of batches reaching at least twice the mean size decreases as traffic grows (from 39 percent at 50 QPS to 0.3 percent at 1000 QPS), reflecting the law of large numbers).
Đến Tỷ lệ
Trung bình Lô
Độ lệch Chuẩn (Std Dev)
Pr(lô = 0)
Pr(lô ≥ 2×trung bình)
50 QPS
0.5
0.7
61%
39%
200 QPS
2
1.4
14%
14%
500 QPS
5
2.2
0.7%
3%
1000 QPS
10
3.2
0.005%
0.3%
13.7.3.3 Thông lượng sự tối đa hóa chiến lược
Thông lượng sự tối ưu hóa yêu cầu việc tách biệt mỗi-yêu cầu độ trễ khỏi bị bão hòa dịch vụ công suất (Throughput optimization requires separating per-request latency from saturated service capacity). Một
yêu cầu chờ đợi cho lô sự hình thành (formation), sau đó trả (tiền) cho dịch vụ thời gian của (cái) được hình thành lô (A request waits for batch formation, then pays the service time of the formed batch). Dưới được duy trì
tải, tuy nhiên, lô sự hình thành có thể chồng chéo với (cái) trước đó lô’s sự thực thi, do đó công suất là
(được) chi phối bởi (cái) sẵn-sàng-lô (ready-batch) dịch vụ thời gian (Under sustained load, however, batch formation can overlap with the previous batch’s execution, so capacity is governed by the ready-batch service time):
𝜇eff(𝐵) ≈ 𝐵 / 𝑇svc(𝐵),
thông lượng = min(𝜆arr, 𝜇eff(𝐵))
(13.10)
Trong phương trình 13.10, 𝜆arr là (cái) được cung cấp đến tỷ lệ và 𝜇eff(𝐵) là bị bão hòa dịch vụ công suất cho
lô kích thước 𝐵 (In equation 13.10, 𝜆arr is the offered arrival rate and 𝜇eff(𝐵) is the saturated service capacity for batch size 𝐵). Tử số (numerator) tăng lên một cách tuyến tính với lô kích thước trong khi dịch vụ thời gian thường tăng lên
dưới-tuyến tính (sub-linearly) qua một hữu ích phạm vi bởi vì GPU tính song song là được sử dụng tốt hơn (The numerator increases linearly with batch size while service time often increases sub-linearly over a useful range because GPU parallelism is better utilized). Việc tạo lô cửa sổ
vẫn xuất hiện trong yêu cầu độ trễ và trong thấp-lưu lượng truy cập các chế độ, nơi (cái) được mong đợi lô kích thước là bị giới hạn
bởi các sự đến trong suốt cửa sổ, xấp xỉ 𝜆arr𝑇window (The batching window still appears in request latency and in low-traffic regimes, where the expected batch size is limited by arrivals during the window, roughly 𝜆arr𝑇window).
Cho ResNet-50 trên một V100 GPU, dịch vụ thời gian (một cách) xấp xỉ mở rộng như 𝑇svc(𝐵) = 5 ms + 0.6𝐵 (5
ms cố định chi phí hoạt động cộng 0.6 ms cho mỗi hình ảnh trong lô) (For ResNet-50 on a V100 GPU, service time approximately scales as 𝑇svc(𝐵) = 5 ms + 0.6𝐵(5 ms fixed overhead plus 0.6 ms per image in the batch)). Này tuyến tính sự xấp xỉ nắm bắt (captures)
thống trị xu hướng (trend); thực sự dịch vụ các thời gian có thể sai lệch (deviate) một cách nhẹ (slightly) do (bởi) bộ nhớ hệ thống phân cấp (hierarchy) các hiệu ứng (This linear approximation captures the dominant trend; actual service times may deviate slightly due to memory hierarchy effects). Với
một 𝑇window = 10 ms việc tạo lô cửa sổ, bảng 13.11 mở rộng (cái) thuần túy-sự suy luận sự quét của bảng 13.9 bằng cách
việc gấp (folding) (vào) cửa sổ sự chờ đợi, do đó của nó độ trễ cột phản ánh đầu cuối-tới-đầu cuối chi phí thay vì sự suy luận thời gian
một mình (nó) (With a 𝑇window = 10 ms batching window, table 13.11 extends the pure-inference sweep of table 13.9 by folding in the window wait, so its latency column reflects end-to-end cost rather than inference time alone:):
Bảng 13.11: Việc tạo lô Thông lượng Sự phân tích: Kịch bản sự phân tích cho ResNet-50 thông lượng trên V100 với 10 ms việc tạo lô cửa sổ (Table 13.11: Batching Throughput Analysis: Scenario analysis for ResNet-50 throughput on V100 with 10 ms batching window).
Thông lượng tăng lên 14.6× từ lô kích thước một tới 32 (64 hình ảnh/s tới 936 hình ảnh/s), nhưng tổng độ trễ nhiều hơn gấp đôi (15.6 ms tới
34.2 ms) (Throughput increases 14.6× from batch size one to 32 (64 img/s to 936 img/s), but total latency more than doubles (15.6 ms to 34.2 ms)). Tối ưu cấu hình phụ thuộc vào liệu độ trễ SLO hay thông lượng mục tiêu là (cái) ràng buộc (binding) sự ép buộc (hay không) (The optimal configuration depends on whether the latency SLO or throughput target is the binding constraint).
Lô Kích thước
Dịch vụ Thời gian
Tổng Độ trễ
Thông lượng
Tính hiệu quả
1
5.6 ms
15.6 ms
64 hình ảnh/s
Thấp
4
7.4 ms
17.4 ms
230 hình ảnh/s
Vừa phải
8
9.8 ms
19.8 ms
404 hình ảnh/s
Tốt
16
14.6 ms
24.6 ms
650 hình ảnh/s
Cao
32
24.2 ms
34.2 ms
936 hình ảnh/s
Tối đa
Thông lượng các lợi ích trong bảng 13.11 theo dấu một cách trực tiếp trở lại (tới) cố định-chi phí hoạt động thuật ngữ trong sắt định luật
được thiết lập trong phần 8.2, nơi việc tạo lô khấu hao công việc qua các yêu cầu (The throughput gains in table 13.11 trace directly back to the fixed-overhead term in the iron law established in section 8.2, where batching amortizes work across requests).

744
13.7 Thông lượng Sự tối ưu hóa
Khăn ăn Toán học 13.7: Sắt định luật của việc tạo lô tính hiệu quả
Sắt định luật sự kết nối (connection): Trong việc phục vụ, việc tạo lô cải thiện thông lượng bằng cách việc khấu hao cố định mỗi-lô
công việc như là sự lập lịch, hạt nhân sự khởi chạy, và trọng số các (sự) đọc; hàng đợi sự chờ đợi duy trì một riêng biệt
độ trễ chi phí (Iron law connection: In serving, batching improves throughput by amortizing fixed per-batch work such as scheduling, kernel launch, and weight reads; queue wait remains a separate latency cost). Giống nhau sắt-định luật sự phân rã từ phương trình 13.11 cho thấy tại sao (The same iron-law decomposition from equation 13.11 shows why:):
𝑇 = 𝑂 / (𝑅peak ⋅ 𝜂hw) + 𝐿lat
(13.11)
Việc bắt nguồn (Deriving) (cái) ngọt ngào điểm (sweet spot):
• Trường hợp 1 (lô 1): Chi phí hoạt động (5 ms) ฀ Tính toán (0.6 ms) (Case 1 (batch 1): Overhead (5 ms) ฀Compute (0.6 ms)). Tính hiệu quả ≈ 10 phần trăm (Efficiency ≈10 percent). GPU
là hầu hết (đang) chờ đợi (The GPU is mostly waiting).
• Trường hợp 2 (lô 32): Chi phí hoạt động (5 ms) ฀ Tính toán (19.2 ms) (Case 2 (batch 32): Overhead (5 ms) ฀Compute (19.2 ms)). Tính hiệu quả ≈ 79 phần trăm (Efficiency ≈79 percent). GPU
là (đang) nhai (crunching) các con số (The GPU is crunching numbers).
Vàng quy tắc: Tăng lô kích thước cho đến khi cố định chi phí hoạt động trở nên không đáng kể (< 10 phần trăm của tổng
thời gian) hay độ trễ SLO chặn (chặn đứng) xa hơn sự chờ đợi (Golden rule: Increase batch size until fixed overhead becomes negligible (< 10 percent of total time) or the latency SLO blocks further waiting). Vượt ra ngoài này điểm, bổ sung (additional) việc tạo lô mang lại
tối thiểu thông lượng nhưng áp đặt một tuyến tính việc xếp hàng đợi hình phạt (penalty) (Beyond this point, additional batching yields minimal throughput but imposes a linear queueing penalty).
Những ba các kết quả này soạn (compose) thành một hoạt động mô hình của động việc tạo lô: cửa sổ thiết lập
trung bình sự chờ đợi tại một nửa (của) (của) nó chiều dài, Poisson các sự đến làm (cái) được nhận ra lô kích thước dao động xung quanh
𝜆arr𝑇window, và bị bão hòa dịch vụ công suất 𝜇eff(𝐵) leo (lên) với lô kích thước cho đến khi cố định chi phí hoạt động (được)
khấu hao (một cách) hoàn toàn (away) (These three results compose into one working model of dynamic batching: the window sets the average wait at half its length, Poisson arrivals make the realized batch size fluctuate around 𝜆arr𝑇window, and the saturated service capacity 𝜇eff(𝐵) climbs with batch size until fixed overhead is amortized away). Không ai (cái nào) trong số chúng vẫn chưa thi hành độ trễ SLO (None of them yet enforces the latency SLO). Các đường chuyền (passes) (thứ) mà tuân theo (theo sau) thêm đó (sự) thiếu
sự ép buộc, việc làm việc ngược (backward) từ một cứng phân vị ngân sách tới (cái) lớn nhất lô (thứ) mà cửa sổ có thể
một cách an toàn hình thành (The passes that follow add that missing constraint, working backward from a hard percentile budget to the largest batch the window may safely form).
13.7.3.4 Bị ép buộc-độ trễ sự tối ưu hóa
Khi độ trễ các SLO cung cấp ràng buộc sự ép buộc, sự tối ưu hóa bài toán trở thành việc tìm kiếm
tối đa lô kích thước (thứ) mà đáp ứng SLO (When latency SLOs provide the binding constraint, the optimization problem becomes finding the maximum batch size that meets the SLO). Cho một độ trễ mục tiêu 𝐿lat,target và trung bình sự chờ đợi thời gian
𝑇window/2, phương trình 13.12 định nghĩa tối đa có-thể-cho-phép (allowable) lô kích thước (việc) sử dụng một bậc-nhất (first-order) trung bình
độ trễ sự xấp xỉ (Equation 13.12 defines the maximum allowable batch size using a first-order average latency approximation:):
𝐵max = max{𝐵 ∶ 𝑇window / 2 + 𝑇svc(𝐵) ≤ 𝐿lat,target}
(13.12)
Hãy xem xét một 50 ms p95 độ trễ SLO cho ResNet-50 việc phục vụ (việc sử dụng này dựa-trên-trung bình sự xấp xỉ
như (là) một xuất phát điểm) (Consider a 50 ms p95 latency SLO for ResNet-50 serving (using this mean-based approximation as a starting point):):
Việc so sánh một bảo thủ việc tạo lô cửa sổ đối nghịch một quyết liệt (aggressive) (cửa sổ) cô lập (isolates) cách cửa sổ
sự lựa chọn đánh đổi sự chờ đợi thời gian, sự suy luận ngân sách, và thông lượng (Comparing a conservative batching window against an aggressive one isolates how the window choice trades wait time, inference budget, and throughput). Bảng 13.12 đặt hai các cấu hình
cạnh nhau (Table 13.12 lays the two configurations side by side).
Bảng 13.12: Việc tạo lô cửa sổ sự đánh đổi: Cách một bảo thủ so với quyết liệt việc tạo lô cửa sổ đánh đổi trung bình sự chờ đợi, sự suy luận
ngân sách, lô kích thước, và thông lượng tại cố định đến tỷ lệ (Table 13.12: Batching window trade-off: How a conservative versus aggressive batching window trades average wait, inference budget, batch size, and throughput at fixed arrival rate).
Số liệu (Metric)
Bảo thủ (𝑇window = 5 ms)
Quyết liệt (𝑇window = 25 ms)
Trung bình sự chờ đợi
2.5 ms (tối đa đợi = 5 ms cho (cái) đầu tiên
yêu cầu trong một cửa sổ)
12.5 ms
Độ trễ ngân sách cho sự suy luận
47.5 ms (trung bình-độ trễ việc lập kế hoạch; đuôi các SLOs
nên lập ngân sách (cho) (cái) đầy cửa sổ)
37.5 ms
Lô kích thước mũ (cap)
32 các hình ảnh (điển hình lô ≈ 5.7)
48 (điển hình lô ≈ 32)
Được đạt được thông lượng
~1,140 hình ảnh/s
~1,280 hình ảnh/s
Quyết liệt cửa sổ đạt được chỉ 12.3 phần trăm cao hơn thông lượng nhưng làm tăng trung bình
độ trễ bởi 10 ms và p99 độ trễ bởi 20 ms (The aggressive window achieves only 12.3 percent higher throughput but increases average latency by 10 ms and p99 latency by 20 ms). Kiểm tra bảng 13.11: cho nhạy cảm-độ trễ các ứng dụng,
bảo thủ cửa sổ cung cấp tốt hơn người dùng trải nghiệm tại khiêm tốn thông lượng chi phí (Examine table 13.11: for latency-sensitive applications, the conservative window provides better user experience at modest throughput cost).

13. Mô hình Việc phục vụ
747
21
Liên tục Việc tạo lô (Continuous Batching):
Cũng được gọi (là) “cấp độ-vòng lặp
việc tạo lô” (Yu và cộng sự 2022) và,
trong NVIDIA TensorRT-LLM,
“đang-bay (in-flight) việc tạo lô” (NVIDIA
2026g).
Chính sự thấu hiểu là
sự lập lịch độ chi tiết (granularity): truyền-
thống (traditional) việc tạo lô cam kết (tới) một
cố định lô cho một toàn bộ tạo-
sinh chuỗi (tiềm năng
hàng trăm (của) các vòng lặp), trong khi
liên tục việc tạo lô lập lịch-
lại (reschedules) tại mọi mã thông báo-sự tạo sinh (token-generation)
bước—tương tự (analogous) (với) sự ưu-
tiên (preemp-tive) HĐH tiến trình sự lập lịch
so với chạy-để-hoàn thành.
Này
mịn hơn (finer) độ chi tiết giảm thiểu
sự lãng phí từ có thể thay đổi-chiều dài (variable-length) các chuỗi (se-
quences), nơi một lô khe cắm (slot)
được chiếm đóng bởi một (được) hoàn thành chuỗi
ngồi nhàn rỗi cho đến khi tất cả (các chuỗi) khác
các chuỗi kết thúc (finish).
22
vLLM (Ảo LLM (Virtual LLM)): Một
mã nguồn mở việc phục vụ hệ thống
thứ mà kích hoạt liên tục việc tạo-
lô thông qua (của) nó PagedAttention thuật-
toán (Kwon và cộng sự 2023).
Được truyền cảm hứng bởi HĐH ảo bộ-
nhớ, kỹ thuật này giảm thiểu
nghiêm trọng KV-bộ nhớ đệm sự phân-
mảnh (fragmen-tation) và sự đặt trước (reservation) sự lãng phí
thứ mà ép buộc (constrains) tĩnh việc tạo lô.
Bằng cách việc giữ KV-bộ nhớ đệm sự lãng phí
thấp, vLLM có thể phục vụ lớn hơn
hiệu quả các lô trên (cái) giống nhau
phần cứng.
13.7.3.5 SLO sự vi phạm sự phân tích
Lô kích thước tính biến đổi gây ra SLO các sự vi phạm thậm chí khi trung bình độ trễ dường như an toàn (Batch size variability causes SLO violations even when mean latency appears safe). p99 độ trễ
bao gồm cả tồi tệ nhất-trường hợp sự chờ đợi thời gian (đầy cửa sổ) và tồi tệ nhất-trường hợp lô kích thước ((được) chi phối bởi Poisson
đuôi) (The p99 latency includes both worst-case wait time (full window) and worst-case batch size (governed by Poisson tail)). Phương trình 13.13 nắm bắt (captures) này mối quan hệ (Equation 13.13 captures this relationship:):
𝐿lat,p99 ≈ 𝑇window + 𝑇svc(𝐵p99)
(13.13)
nơi 𝐵p99 là 99(th) phân vị lô kích thước (where 𝐵p99 is the 99th percentile batch size). Cho 𝜆arr = 500 QPS và 𝑇window = 10 ms, trung bình lô
kích thước là 5 trong khi Poisson đuôi đẩy p99 lô kích thước tới 11 (For 𝜆arr = 500 QPS and 𝑇window = 10 ms, the mean batch size is 5 while the Poisson tail pushes the p99 batch size to 11). (Cái) đuôi đó lan truyền vào độ trễ:
mức trung bình thêm 5 ms của sự chờ đợi (vào) 8 ms của dịch vụ cho 13 ms, trong khi đó (whereas) p99 thêm (cái) đầy cửa sổ của 10 ms
(vào) 11.6 ms của dịch vụ cho 21.6 ms (That tail propagates into latency: the mean adds 5 ms of wait to 8 ms of service for 13 ms, whereas the p99 adds the full window of 10 ms to 11.6 ms of service for 21.6 ms).
p99 độ trễ là 1.66× mức trung bình, việc phản ánh cả sự chờ đợi thời gian phương sai và lô kích thước phương sai (The p99 latency is 1.66× the mean, reflecting both wait time variance and batch size variance).
Các hệ thống (thứ) mà cung cấp (provision) (dựa) trên trung bình độ trễ sẽ trải nghiệm SLO các sự vi phạm (Systems that provision based on mean latency will experience SLO violations).
Các hệ thống Góc nhìn 13.7: Độ trễ-thông lượng sự đánh đổi
Một đơn “sự suy luận tốc độ” con số là không được định nghĩa cho đến khi lô kích thước được đặt tên, bởi vì lô
kích thước chọn chế độ nào, và nút thắt cổ chai nào, hệ thống hoạt động trong (đó) (A single “inference speed” number is undefined until the batch size is named, because batch size selects which regime, and which bottleneck, the system operates in).
• Lô-1 chế độ (Batch-1 regime): Bị giới hạn-độ trễ (Latency-bound). Yêu cầu con đường (bị) thống trị bởi Python chi phí hoạt động và
bộ nhớ băng thông, vì mỗi yêu cầu tải các trọng số cho một đơn đầu vào (The request path is dominated by Python overhead and memory bandwidth, since each request loads the weights for a single input). Chế độ này
chi phối thực-thời gian sự tương tác như là việc gõ phím (typing) các trình trợ giúp và rô bốt (robotics) (This regime governs real-time interaction such as typing helpers and robotics).
• Lô-N chế độ (Batch-N regime): Bị giới hạn-thông lượng (Throughput-bound). Việc khấu hao trọng số tải qua một đầy lô
dịch chuyển nút thắt cổ chai (sang) tính toán (FLOP/s) (Amortizing the weight load across a full batch shifts the bottleneck to compute (FLOP/s)). Chế độ này chi phối ngoại tuyến (offline) việc xử lý và
cao-lưu lượng truy cập các dịch vụ (This regime governs offline processing and high-traffic services).
Hai các chế độ tối ưu hóa đối nghịch (opposite) các số lượng (quantities), do đó một mô hình (thứ) mà là “nhanh” tại lô 1 có thể (là) xa
từ đỉnh thông lượng, và ngược lại (The two regimes optimize opposite quantities, so a model that is “fast” at batch 1 may be far from peak throughput, and vice versa). Bất kỳ độ trễ hay thông lượng số liệu (figure) (nào) phải do đó chỉ định
liệu nó (đã) được đo lường tại đơn-luồng độ trễ (lô 1) hay tối đa thông lượng (lô N) (hay không) (Any latency or throughput figure must therefore specify whether it was measured at single-stream latency (batch 1) or maximum throughput (batch N)).
13.7.3.6 Thích ứng việc tạo lô các cửa sổ
Giống nhau lô-kích thước sự phụ thuộc thúc đẩy cách việc phục vụ hệ thống định hình các lô của nó (ngay) trong đầu tiên nơi (ngay từ đầu) (The same batch-size dependence drives how the serving system shapes its batches in the first place).
Cố định việc tạo lô các cửa sổ lãng phí độ trễ ngân sách trong suốt cao lưu lượng truy cập khi lớn các lô hình thành (một cách) nhanh chóng (Fixed batching windows waste latency budget during high traffic when large batches form quickly).
Danh sách 13.2 chứng minh cách thích ứng các chiến lược điều chỉnh cửa sổ dựa trên hàng đợi độ sâu (Listing 13.2 demonstrates how adaptive strategies adjust the window based on queue depth).

746
13.7 Thông lượng Sự tối ưu hóa
Danh sách 13.2: Thích ứng Việc tạo lô Cửa sổ: Động (Dynamically) điều chỉnh lô thời gian chờ dựa trên hàng đợi độ sâu và đến tỷ lệ, việc giảm thiểu
trung bình độ trễ bởi 27 phần trăm (được) so sánh với cố định các cửa sổ trong khi việc duy trì thông lượng (Listing 13.2: Adaptive Batching Window: Dynamically adjusts batch timeout based on queue depth and arrival rate, reducing average latency by 27 percent compared to fixed windows while maintaining throughput).
```python
def adaptive_batching_window(
    queue_depth, arrival_rate, slo_ms, service_ms, fixed_overhead_ms
):
    """Tính toán tối ưu việc tạo lô cửa sổ.
    Dựa trên hiện tại hệ thống trạng thái.
    """
    target_batch_size = 16  # Tối ưu lô cho GPU sự sử dụng

    # Nhanh con đường: lô (đã) sẵn sàng, đóng ngay lập tức để tối thiểu hóa độ trễ
    if queue_depth >= target_batch_size:
        return 0

    # Tính toán tối đa có-thể-cho-phép đợi từ (cái) còn lại p99 ngân sách.
    max_wait_ms = max(0, slo_ms - service_ms - fixed_overhead_ms)

    # Ước tính thời gian để tích lũy (accumulate) mục tiêu lô tại hiện tại sự đến
    # tỷ lệ.
    # arrival_rate là các yêu cầu/giây, do đó chuyển đổi các giây thành
    # phần nghìn giây.
    if arrival_rate > 0:
        requests_needed = target_batch_size - queue_depth
        estimated_wait_ms = requests_needed / arrival_rate * 1000.0
        # Trả về tối thiểu của (được) ước tính đợi và (được) ép buộc-SLO tối đa
        return min(estimated_wait_ms, max_wait_ms)

    return max_wait_ms  # Thấp lưu lượng truy cập: sử dụng còn lại ngân sách để tích lũy lô
```
Cách tiếp cận này giảm thiểu trung bình sự chờ đợi thời gian trong suốt cao lưu lượng truy cập trong khi việc duy trì lô các kích thước (This approach reduces average wait time during high traffic while maintaining batch sizes). Cho
lưu lượng truy cập (đang) thay đổi giữa 200–1000 QPS, một cố định 10 ms cửa sổ tạo ra 15 ms trung bình độ trễ tại
650 hình ảnh/s, trong khi một thích ứng cửa sổ cắt giảm trung bình độ trễ tới 11 ms (27 phần trăm sự giảm thiểu) và
cải thiện thông lượng tới 680 hình ảnh/s (5 phần trăm sự cải thiện) (For traffic varying between 200–1000 QPS, a fixed 10 ms window produces 15 ms average latency at 650 img/s, while an adaptive window cuts average latency to 11 ms (27 percent reduction) and improves throughput to 680 img/s (5 percent improvement)). Sự tương tác (interplay) giữa cửa sổ kích thước
và lô các giới hạn tạo ra một không gian của có thể (có) các cấu hình, mỗi (cấu hình) đại diện một khác biệt sự cân bằng
giữa thông lượng và độ trễ (The interplay between window size and batch limits creates a space of possible configurations, each representing a different balance between throughput and latency).
Việc tạo lô cấu hình không gian hình thành một Pareto biên giới nơi việc cải thiện thông lượng yêu cầu
việc chấp nhận cao hơn độ trễ (The batching configuration space forms a Pareto frontier where improving throughput requires accepting higher latency). Bảng 13.13 theo dấu này biên giới qua năm đại diện các cấu hình (Table 13.13 traces this frontier across five representative configurations:):
Bảng 13.13: Việc tạo lô Pareto Biên giới: Mỗi cấu hình đại diện một khác biệt điểm trên thông lượng-độ trễ sự đánh đổi đường cong (Table 13.13: Batching Pareto Frontier: Each configuration represents a different point on the throughput-latency trade-off curve).
Việc di chuyển từ 2 ms tới 50 ms các cửa sổ cải thiện thông lượng bởi chỉ 52 phần trăm trong khi việc làm tăng p99 độ trễ bởi 5.4× (Moving from 2 ms to 50 ms windows improves throughput by only 52 percent while increasing p99 latency by 5.4×).
(Sự) giảm dần các lợi nhuận (Diminishing returns) làm quyết liệt việc tạo lô (trở nên) đắt đỏ cho nhạy cảm-độ trễ các ứng dụng (Diminishing returns make aggressive batching costly for latency-sensitive applications).
Cửa sổ (ms)
Tối đa Lô
Trung bình Độ trễ
p99 Độ trễ
Thông lượng
Cấu hình
2
16
8 ms
18 ms
890 hình ảnh/s
Siêu-thấp (Ultra-low) độ trễ
5
32
10 ms
22 ms
1,140 hình ảnh/s
Cân bằng
10
32
15 ms
35 ms
1,240 hình ảnh/s
Vừa phải độ trễ
20
64
23 ms
52 ms
1,310 hình ảnh/s
(Được) tối ưu hóa-thông lượng
50
128
38 ms
98 ms
1,350 hình ảnh/s
Tối đa thông lượng
13.7.3.7 Thực tế cấu hình các hướng dẫn (guidelines)
Pareto biên giới trong bảng 13.13 minh họa tại sao những các hướng dẫn này quan trọng: đi qua (past) đầu gối, việc mở rộng
cửa sổ mua (sự) giảm dần một cách dốc (steeply) thông lượng cho (sự) tăng lên một cách sắc bén đuôi độ trễ (The Pareto frontier in table 13.13 illustrates why these guidelines matter: past the knee, widening the window buys steeply diminishing throughput for sharply rising tail latency). Có nguyên tắc (Principled) việc tạo lô
cấu hình tránh này khu vực của sự giảm dần các lợi nhuận bằng cách việc làm việc ngược từ độ trễ
ngân sách (Principled batching configuration avoids this region of diminishing returns by working backward from the latency budget). Việc cấp phát hai mươi tới 30 phần trăm của SLO (vào) việc tạo lô sự chờ đợi thời gian để lại (cái) phần còn lại cho
sự suy luận và chi phí hoạt động, thứ mà giới hạn tối đa cửa sổ tại 𝑇max = 0.3 × 𝐿lat,SLO (Allocating twenty to 30 percent of the SLO to batching wait time leaves the remainder for inference and overhead, which bounds the maximum window at 𝑇max = 0.3×𝐿lat,SLO). Lưu lượng truy cập
sự ước tính (thứ) mà nạp (vào) (feeds) này sự tính toán nên sử dụng p95 đến tỷ lệ thay vì mức trung bình, bởi vì

việc tạo lô các cửa sổ (được) điều chỉnh cho trung bình lưu lượng truy cập tạo ra (các) quá khổ (oversized) lô trong suốt các sự tăng vọt—chính xác
khi SLO khoảng không quan trọng (nhất) (batching windows tuned for average traffic produce oversized batches during spikes—precisely when SLO headroom matters most). GPU bộ nhớ áp đặt một cứng trần (ceiling) trên lô kích thước độc lập
với độ trễ sự ép buộc, vì sự kích hoạt bộ nhớ mở rộng một cách tuyến tính với lô chiều (GPU memory imposes a hard ceiling on batch size independent of the latency constraint, since activation memory scales linearly with the batch dimension). Cuối cùng,
việc giám sát (cái) thực sự lô kích thước sự phân phối trong sản xuất tiết lộ liệu ban đầu lưu lượng truy cập các giả định
tổ chức (hold) (hay không); cao phương sai báo hiệu (signals) rằng cửa sổ cần thích ứng sự điều chỉnh thay vì một cố định cấu hình (Finally, monitoring the actual batch size distribution in production reveals whether initial traffic assumptions hold; high variance signals that the window needs adaptive tuning rather than a fixed configuration).
Cho ResNet-50 với 50 ms SLO và 500 QPS lưu lượng truy cập (For ResNet-50 with 50 ms SLO and 500 QPS traffic:):
Sự tính toán biến SLO và đến-tỷ lệ các giả định thành hai có-thể-triển-khai các núm (knobs): (cái)
việc tạo lô cửa sổ và tối đa lô kích thước (The calculation turns the SLO and arrival-rate assumptions into two deployable knobs: the batching window and maximum batch size). Bảng 13.14 tóm tắt (cái) dẫn đến cấu hình
và (cái) được dự đoán hoạt động điểm (Table 13.14 summarizes the resulting configuration and the predicted operating point).
Bảng 13.14: Thực tế Việc tạo lô Cấu hình: Việc làm việc ngược từ một 50 ms SLO và 500 QPS lưu lượng truy cập sự ước tính mang lại một 12 ms
việc tạo lô cửa sổ và lô-32 mũ (Table 13.14: Practical Batching Configuration: Working backward from a 50 ms SLO and 500 QPS traffic estimate yields a 12 ms batching window and batch-32 cap). Được dự đoán p99 độ trễ duy trì bên trong SLO, trong khi lô mũ để lại khoảng không cho
các đợt (bursts) (The predicted p99 latency remains within the SLO, while the batch cap leaves headroom for bursts).
Số lượng
Giá trị
Kỹ thuật vai trò
Độ trễ ngân sách cho việc tạo lô
15 ms
Phần của SLO (có) sẵn sàng cho việc xếp hàng đợi sự chậm trễ.
Tối đa cửa sổ
15 ms
Trên (upper) ranh giới (bound) (được) ngụ ý (implied) bởi độ trễ ngân sách.
Được mong đợi lô kích thước
6
Trung bình lô dưới (cái) được tuyên bố (stated) lưu lượng truy cập.
p99 lô kích thước
12
Đợt kích thước dưới Poisson các sự đến.
Bị giới hạn-bởi-bộ-nhớ tối đa lô
32
Cứng mũ (được) áp đặt bởi máy gia tốc bộ nhớ.
Được chọn cấu hình
𝑇window = 12 ms, 𝐵max = 32
Thực tế núm thiết lập (setting) cho sự triển khai.
Được dự đoán p99 độ trễ
24.2 ms
Xác nhận rằng cấu hình ở lại bên trong
SLO.
Được dự đoán đỉnh công suất
1,176.9 hình ảnh/s
Công suất nếu (cái) được chọn lô mũ (bị) bão hòa.
Được phục vụ thông lượng
500 hình ảnh/s
Bị giới hạn-bởi-sự-đến tải (được) xử lý bởi cấu hình.
13.7.4 Liên tục việc tạo lô
Tự hồi quy (Autoregressive) các mô hình như ngôn ngữ các mô hình tạo sinh các đầu ra mã thông báo bởi mã thông báo—mỗi mới mã thông báo
phụ thuộc vào tất cả trước đó được tạo sinh các mã thông báo, do đó sự tạo sinh là (về mặt) vốn có (inherently) tuần tự (Autoregressive models like language models generate outputs token by token—each new token depends on all previously generated tokens, so generation is inherently sequential). (Cái) động
việc tạo lô được kiểm tra trong phần 13.7 giả định cố định-chiều dài các đầu ra (The dynamic batching examined in section 13.7 assumes fixed-length outputs). Các LLM vi phạm giả định này: nếu
một chuỗi trong một lô của tám kết thúc (finishes) sau mười các mã thông báo trong khi (các chuỗi) khác cần 100 các mã thông báo, 90 phần trăm của
tính toán cho đó chuỗi khe cắm là bị lãng phí (Yu và cộng sự 2022) (LLMs violate this assumption: if one sequence in a batch of eight finishes after ten tokens while others need 100 tokens, 90 percent of the compute for that sequence slot is wasted (Yu et al. 2022)).
Liên tục việc tạo lô21 (cũng được gọi (là) cấp độ-vòng lặp việc tạo lô) giải quyết này sự lãng phí bằng cách việc cho phép mới
các yêu cầu (để) tham gia (join) một lô giữa sự tạo sinh các bước và (các) được hoàn thành chuỗi (để) thoát (exit) (Yu và cộng sự 2022;
Kwon và cộng sự 2023) (Continuous batching21 (also called iteration-level batching) addresses this waste by allowing new requests to join a batch between generation steps and completed sequences to exit (Yu et al. 2022; Kwon et al. 2023)). Hệ thống quản lý lô thành phần (một cách) động tại mỗi việc giải mã (decoding) vòng lặp
thay vì việc hình thành tĩnh các lô (thứ) mà tồn tại (persist) cho (cái) toàn bộ tạo sinh quá trình (The system manages batch composition dynamically at each decoding iteration rather than forming static batches that persist for the entire generation process).
Cơ chế làm việc như sau: khi một chuỗi tạo sinh (của) nó kết thúc-của-chuỗi (end-of-sequence) mã thông báo, (của) nó khe cắm
trở nên ngay lập tức (có) sẵn sàng (The mechanism works as follows: when a sequence generates its end-of-sequence token, its slot becomes immediately available). Một (đang) chờ đợi yêu cầu có thể lấp đầy đó khe cắm cho (cái) tiếp theo vòng lặp thay vì
việc chờ đợi cho (cái) toàn bộ lô (để) hoàn thành (A waiting request can fill that slot for the next iteration rather than waiting for the entire batch to complete). (Một cách) tương tự (Similarly), hệ thống có thể thêm mới các yêu cầu (vào) (có) sẵn sàng các khe cắm
mà không có việc ngắt quãng (interrupting) (đang) diễn ra (ongoing) sự tạo sinh (Similarly, the system can add new requests to available slots without interrupting ongoing generation). Này động cách tiếp cận duy trì cao GPU sự sử dụng
thậm chí khi chuỗi các chiều dài thay đổi bởi 100× hay hơn (This dynamic approach maintains high GPU utilization even when sequence lengths vary by 100× or more).
Các hệ thống (đang) triển khai liên tục việc tạo lô, như là vLLM22 và TensorRT-LLM, cải thiện
thông lượng bằng cách việc giữ giải mã các khe cắm (được) chiếm đóng (occupied) khi các chuỗi đi vào và đi ra (Kwon và cộng sự 2023; NVIDIA
2026g) (Systems implementing continuous batching, such as vLLM22 and TensorRT-LLM, improve throughput by keeping decode slots occupied as sequences enter and exit (Kwon et al. 2023; NVIDIA 2026g)). Sarathi-Serve tinh chỉnh (refines) này bộ lập lịch với (được) phân đoạn (chunked) việc điền trước (prefill) và không-đình-trệ (stall-free) việc tạo lô để giảm thiểu
sự can thiệp (interference) giữa dấu nhắc (prompt) việc xử lý và mã thông báo việc giải mã (Agrawal và cộng sự 2024) (Sarathi-Serve refines this scheduler with chunked prefill and stall-free batching to reduce interference between prompt processing and token decoding (Agrawal et al. 2024)). Sự cải-
thiện đến từ hai các nguồn: việc giảm thiểu (bị) lãng phí tính toán trên (các) được hoàn thành chuỗi và việc giảm thiểu
trung bình sự chờ đợi thời gian cho mới các yêu cầu (The improvement comes from two sources: reducing wasted compute on completed sequences and reducing average wait time for new requests). Cho sản xuất ngôn ngữ mô hình việc phục vụ nơi phản hồi các chiều dài
thay đổi từ đơn các mã thông báo tới hàng ngàn, liên tục việc tạo lô đã (trở thành) một trung tâm (central) kỹ thuật cho
hiệu quả-chi phí (cost-effective) sự triển khai (For production language model serving where response lengths vary from single tokens to thousands, continuous batching has become a central technique for cost-effective deployment).
Bộ nhớ sự quản lý thêm tính phức tạp (vào) liên tục việc tạo lô (Memory management adds complexity to continuous batching). Khi các chuỗi đi vào và đi ra
lô, khóa-giá trị (key-value) bộ nhớ đệm (thứ) mà lưu trữ sự chú ý (attention) ngữ cảnh phải (được) một cách động (được) cấp phát và
(được) giải phóng (freed) (As sequences enter and exit the batch, the key-value cache that stores attention context must be dynamically allocated and freed). (Hãy) xem xét (những) gì xảy ra khi các chuỗi của (đang) thay đổi các chiều dài chia sẻ GPU bộ nhớ: một 100-mã thông báo
chuỗi hoàn thành và giải phóng (releases) (của) nó bộ nhớ đệm, nhưng một mới 150-mã thông báo chuỗi không thể sử dụng đó không gian
bởi vì nó cần một lớn hơn liền kề (contiguous) khối (Consider what happens when sequences of varying lengths share GPU memory: a 100-token sequence completes and releases its cache, but a new 150-token sequence cannot use that space because it needs a larger contiguous block). Qua thời gian, nhỏ không thể sử dụng (unusable) các khoảng trống (gaps) tích lũy giữa

13. Mô hình Việc phục vụ (Model Serving)
748
13.7 Thông lượng Sự tối ưu hóa
PagedAttention thu hồi (recovers) KV-
bộ nhớ đệm sự lãng phí của liền kề sự cấp-
phát (PagedAttention recovers the KV-cache waste of contiguous alloca-tion).
23
PagedAttention:
(Cái)
tên một cách trực tiếp tham chiếu (tới) HĐH
ảo bộ nhớ việc phân trang (paging), lần đầu tiên
được triển khai trên Atlas
máy tính
tại
Manchester
(1962)
để
giải quyết
(cái)
giống nhau
lớp của sự cấp phát bài toán—
các chương trình
đã cần
nhiều (hơn)
bộ nhớ
hơn
về mặt vật lý
có sẵn,
và
liền kề
sự cấp phát
đã lãng phí
không gian.
Được giới thiệu tại SOSP 2023,
PagedAttention áp dụng này
sáu-thập kỷ-tuổi (six-decade-old)
sự trừu tượng (abstraction)
cho GPU KV-bộ nhớ đệm bộ nhớ:
trước
nó,
LLM
việc phục vụ
các hệ thống đã lãng phí 60–80 phần trăm
của KV bộ nhớ đệm bộ nhớ do (bởi)
tới sự phân mảnh và quá mức-
sự đặt trước (over-reservation). PagedAttention
giảm thiểu
sự lãng phí
tới
dưới
4 phần trăm,
việc kích hoạt 2–4×
cao hơn thông lượng trên (cái)
giống nhau phần cứng (Kwon và cộng sự
2023).
(các) được cấp phát các khu vực (regions), cuối cùng việc ngăn chặn mới các chuỗi khỏi việc bắt đầu thậm chí khi tổng trống bộ nhớ
dường như đủ (allocated regions, eventually preventing new sequences from starting even when total free memory appears sufficient). Này bộ nhớ sự phân mảnh có thể lãng phí 40 tới 50 phần trăm của (có) sẵn sàng bộ nhớ trong
ngây thơ (naive) các sự triển khai, (một cách) nghiêm trọng việc giới hạn đồng thời lô kích thước (thứ) mà quyết định thông lượng (This memory fragmentation can waste 40 to 50 percent of available memory in naive implementations, severely limiting the concurrent batch size that determines throughput).
13.7.4.1 PagedAttention
PagedAttention,23 được giới thiệu trong vLLM, giải quyết này sự phân mảnh bài toán bằng cách việc áp dụng hoạt động
hệ thống ảo bộ nhớ các khái niệm cho GPU bộ nhớ (Kwon và cộng sự 2023) (PagedAttention,23 introduced in vLLM, solves this fragmentation problem by applying operating system virtual memory concepts to GPU memory (Kwon et al. 2023)). Thay vì việc cấp phát một
liền kề khối (cho) mỗi chuỗi, PagedAttention chia KV bộ nhớ đệm thành cố định-kích thước các trang (điển hình
16 các mã thông báo (cho) mỗi (trang)) (Instead of allocating one contiguous block per sequence, PagedAttention divides the KV cache into fixed-size pages (typically 16 tokens each)). Một chuỗi’s bộ nhớ đệm bao gồm các con trỏ tới không liền kề các trang (được) rải rác (scattered) qua
GPU bộ nhớ (A sequence’s cache consists of pointers to noncontiguous pages scattered across GPU memory). Khi một chuỗi hoàn thành, (của) nó các trang quay trở lại một trống danh sách và có thể được tái sử dụng bởi bất kỳ
mới chuỗi (nào), bất kể của chiều dài (When a sequence completes, its pages return to a free list and can be reused by any new sequence, regardless of length). vLLM báo cáo rằng này việc phân trang cách tiếp cận giảm thiểu KV-bộ nhớ đệm sự lãng phí
tới dưới 4 phần trăm trong khi việc cải thiện thông lượng tương đối (so với) (các) trước đó liền kề-sự cấp phát các thiết kế (vLLM reports that this paging approach reduces KV-cache waste to below 4 percent while improving throughput relative to prior contiguous-allocation designs). (Cái)
chi phí hoạt động là một trang-bảng (page-table) (sự) tra cứu (lookup) trong suốt sự chú ý tính toán, việc làm PagedAttention (trở thành) một tiêu chuẩn
tham chiếu điểm cho sản xuất LLM việc phục vụ (The overhead is a page-table lookup during attention computation, making PagedAttention a standard reference point for production LLM serving).
Việc tạo lô và bộ nhớ các kỹ thuật được bao phủ (covered) ở đây thiết lập nền tảng cho LLM việc phục vụ, nhưng
một vài nâng cao (advanced) các chủ đề (topics) đảm bảo (warrant) bổ sung (sự) nghiên cứu (The batching and memory techniques covered here establish the foundation for LLM serving, but several advanced topics warrant additional study).
Các hệ thống Góc nhìn 13.8: LLM việc phục vụ: Vượt ra ngoài (các) nguyên tắc cơ bản (fundamentals)
Ngôn ngữ mô hình việc phục vụ giới thiệu các thách thức vượt ra ngoài việc tạo lô và bộ nhớ các nguyên tắc (principles)
được thiết lập ở đây (Language model serving introduces challenges beyond the batching and memory principles established here). Khóa-giá trị bộ nhớ đệm (thứ) mà lưu trữ sự chú ý ngữ cảnh mở rộng với chuỗi chiều dài
và lô kích thước, thường (việc) vượt quá (chính) mô hình các trọng số (chúng) trong bộ nhớ sự tiêu thụ (The key-value cache that stores attention context scales with sequence length and batch size, often exceeding the model weights themselves in memory consumption). Các kỹ-
thuật như là suy đoán (speculative) việc giải mã sử dụng nhỏ nháp (draft) các mô hình để đề xuất nhiều các mã thông báo (thứ) mà
mục tiêu mô hình xác minh trong song song, việc đạt được 2–3× độ trễ sự giảm thiểu cho tương tác các ứng dụng
(Leviathan và cộng sự 2023) (Techniques like speculative decoding use small draft models to propose multiple tokens that the target model verifies in parallel, achieving 2–3× latency reduction for interactive applications (Leviathan et al. 2023)). Chỉ-trọng số sự lượng tử hóa (như là INT4 các trọng số với FP16 các sự kích hoạt)
là đặc biệt (especially) có liên quan cho bị giới hạn-bởi-bộ nhớ-băng thông LLM sự suy luận (Lin và cộng sự 2023) (Weight-only quantization (such as INT4 weights with FP16 activations) is especially relevant for memory-bandwidth-bound LLM inference (Lin et al. 2023)).
Những đặc thù-LLM (LLM-specific) các sự tối ưu hóa này xây dựng một cách trực tiếp trên các nền tảng (thứ mà) chương này thiết lập (These LLM-specific optimizations build directly on the foundations this chapter establishes:):
việc xếp hàng đợi lý thuyết chi phối yêu cầu sự lập lịch, việc tạo lô các sự đánh đổi quyết định thông lượng-độ trễ
các đường cong, và độ chính xác sự lựa chọn tuân theo giống nhau độ chính xác-tính hiệu quả các nguyên tắc (queuing theory governs request scheduling, batching trade-offs determine throughput-latency curves, and precision selection follows the same accuracy-efficiency principles). (Các) việc phục-
vụ các nguyên tắc cơ bản áp dụng (một cách) phổ quát (universally); LLM việc phục vụ thêm đặc thù-miền các kỹ thuật (lên) trên (atop) này
nền tảng (The serving fundamentals apply universally; LLM serving adds domain-specific techniques atop this foundation). Nâng cao các sự xử lý (treatments) cung cấp chi tiết độ bao phủ của KV bộ nhớ đệm sự tối ưu hóa, việc bao-
gồm các kỹ thuật cho nhiều-người thuê (multi-tenant) việc phục vụ, nơi một hạm đội (fleet) chia sẻ công suất qua những người dùng, và
phân tán (distributed) sự suy luận, nơi một yêu cầu có thể bị chia (tách) qua các máy (Advanced treatments provide detailed coverage of KV cache optimization, including techniques for multi-tenant serving, where one fleet shares capacity across users, and distributed inference, where one request may be split across machines).
Liên tục việc tạo lô là thống trị kỹ thuật cho LLM việc phục vụ, (nhưng) tuy nhiên (yet) không (phải) tất cả sự triển khai các kịch bản
hưởng lợi từ việc tạo lô (Continuous batching is the dominant technique for LLM serving, yet not all deployment scenarios benefit from batching). Tinh vi (sophisticated) các kỹ thuật được kiểm tra cho đến nay (từ động việc tạo lô
các cửa sổ tới PagedAttention) tối ưu hóa cho cao-thông lượng máy chủ (server) các khối lượng công việc (The sophisticated techniques examined so far (from dynamic batching windows to PagedAttention) optimize for high-throughput server workloads). Những kỹ thuật này
giới thiệu tính phức tạp và độ trễ chi phí hoạt động (thứ) mà có thể không được biện minh (justified) cho tất cả sự triển khai các ngữ cảnh (These techniques introduce complexity and latency overhead that may not be justified for all deployment contexts).
Thực tế câu hỏi là khi (nào) việc tạo lô làm tổn thương thay vì giúp ích (The practical question is when batching hurts rather than helps).
Một số các kịch bản yêu cầu đơn-yêu cầu việc xử lý (Some scenarios require single-request processing). Siêu-thấp độ trễ các yêu cầu, nơi p99
độ trễ phải ở (dưới) 10 ms, làm (cho) bất kỳ việc tạo lô sự chậm trễ (nào) (trở nên) không thể chấp nhận (được) (Ultra-low latency requirements, where p99 latency must stay under 10 ms, make any batching delay unacceptable). (Một cách) cao độ có thể thay đổi yêu cầu các kích thước
tạo ra việc đệm (padding) chi phí hoạt động (thứ) mà lãng phí tính toán, vì nhỏ nhất đầu vào trong một lô phải được đệm để
khớp (với) (cái) lớn nhất (Highly variable request sizes create padding overhead that wastes compute, since the smallest input in a batch must be padded to match the largest). Bộ nhớ các sự ép buộc cũng trở thành ràng buộc khi các mô hình đã tiêu thụ hầu hết
GPU bộ nhớ, vì lô các sự kích hoạt mở rộng (một cách) tuyến tính với lô kích thước và có thể kích hoạt hết-bộ-nhớ (out-of-memory)
các lỗi (Memory constraints also become binding when models already consume most GPU memory, since batch activations scale linearly with batch size and can trigger out-of-memory errors).
13.7.5 Phiên (Session) sự thân thiết (affinity) các sự ép buộc
Khi các yêu cầu từ giống nhau người dùng hay phiên nên định tuyến tới giống nhau bản sao, việc tạo lô trở nên
bị ép buộc (When requests from the same user or session should route to the same replica, batching becomes constrained). Phiên sự thân thiết, cũng được gọi (là) dính (sticky) các phiên, quan trọng (matters) vì ba chính (main) các lý do (Session affinity, also called sticky sessions, matters for three main reasons).
Có tác động nhất (impactful) trường hợp là KV-bộ nhớ đệm sự tái sử dụng trong hội thoại AI, nơi khóa-giá trị bộ nhớ đệm từ
trước đó các lượt (turns) có thể (một cách) vật chất (materially) tăng tốc nhiều-lượt các cuộc hội thoại (The most impactful case is KV-cache reuse in conversational AI, where the key-value cache from previous turns can materially speed up multi-turn conversations). Việc định tuyến một tiếp theo (follow-up) yêu cầu tới một
khác biệt bản sao bị tước bỏ (forfeits) này được lưu trong bộ nhớ đệm ngữ cảnh, việc ép buộc hệ thống (để) tính toán lại hay tải lại tiền tố trạng thái
cho dài các cuộc hội thoại (Routing a follow-up request to a different replica forfeits this cached context, forcing the system to recompute or reload prefix state for long conversations).
Một thứ hai trình điều khiển (driver) là đặc thù-người dùng (user-specific) các mô hình: một số hệ thống phục vụ được cá nhân hóa các mô hình hay các bộ tiếp hợp (adapters)
cho mỗi người dùng, và việc định tuyến các yêu cầu tới bản sao (thứ) mà đã tải đó người dùng’s bộ tiếp hợp tránh

13. Mô hình Việc phục vụ (Model Serving)
749
24
Poisson Tiến trình (Process): Được đặt tên
sau Pháp nhà toán học
Simeon
Denis
Poisson
(1781–1840), này ngẫu nhiên
mô hình
mô tả
các sự kiện
(đang) xảy ra (một cách) liên tục và
(một cách) độc lập tại một hằng số
trung bình tỷ lệ. Chính thuộc-
tính (property) cho việc phục vụ:
phương sai
bằng mức trung bình, do đó lô
các kích thước dao động (một cách) đáng kể
tại
vừa phải
lưu lượng truy cập—với
𝜆arr = 200 yêu cầu/s và một 10
ms cửa sổ, được mong đợi lô
kích thước là hai nhưng xấp xỉ 14
phần trăm của các cửa sổ sẽ là
trống (bị lãng phí GPU các chu kỳ).
Này phương sai là lý do tại sao việc tạo lô
các cửa sổ
phải
được
điều chỉnh
(một cách) theo xác suất thay vì
(được) thiết lập từ trung bình lưu lượng truy cập một mình (nó).
Khi QPS tăng lên (rises), việc tạo lô cửa-
sổ co lại (shrinks) trong khi lô kích thước
phát triển.
(sự) lặp lại việc tải chi phí hoạt động (repeated loading overhead). (Một cách) tương tự, có trạng thái (stateful) việc tiền xử lý (thứ) mà duy trì trình mã thông báo (tokenizer) các bộ nhớ đệm hay
đặc thù-phiên sự chuẩn hóa (normalization) yêu cầu việc xây dựng lại trạng thái khi các yêu cầu định tuyến tới một khác biệt bản sao (Similarly, stateful preprocessing that maintains tokenizer caches or session-specific normalization requires rebuilding state when requests route to a different replica).
Sự căng thẳng với việc tạo lô là rõ ràng vì nghiêm ngặt (strict) sự thân thiết ép buộc (những) yêu cầu nào có thể được tạo lô
cùng nhau, có khả năng (potentially) việc giảm thiểu lô các kích thước và GPU sự sử dụng (The tension with batching is clear since strict affinity constrains which requests can be batched together, potentially reducing batch sizes and GPU utilization). Sản xuất các hệ thống thường triển khai
mềm sự thân thiết nơi các yêu cầu thích (prefer) của chúng được chỉ định bản sao nhưng có thể tràn (overflow) (sang) những (bản sao) khác khi đó bản sao
bị quá tải (Production systems often implement soft affinity where requests prefer their assigned replica but can overflow to others when that replica is overloaded). Điều này bảo tồn hầu hết sự thân thiết các lợi ích trong khi việc duy trì tải sự cân bằng (This preserves most affinity benefits while maintaining load balance).
13.7.6 Lưu lượng truy cập các mẫu và việc tạo lô chiến lược
Tối ưu việc tạo lô chiến lược phụ thuộc (một cách) tới hạn (critically) vào (cách) các yêu cầu đến (The optimal batching strategy depends critically on how requests arrive). Khác biệt sự triển khai
các ngữ cảnh thể hiện (exhibit) khác biệt (distinct) đến các mẫu, mỗi (ngữ cảnh) (việc) yêu cầu khác biệt việc tạo lô các cách tiếp cận (Different deployment contexts exhibit distinct arrival patterns, each requiring different batching approaches). MLPerf
sự suy luận điểm chuẩn mã hóa (codifies) những các mẫu này thành bốn các kịch bản (thứ) mà (một cách) trực tiếp ánh xạ tới thế giới-thực
các sự triển khai, như phần 12.8.4.2 giải thích (trong) chi tiết (The MLPerf inference benchmark codifies these patterns into four scenarios that directly map to real-world deployments, as section 12.8.4.2 explains in detail).
13.7.6.1 Máy chủ lưu lượng truy cập (poisson các sự đến)
MLPerf Máy chủ kịch bản mô hình hóa đám mây/như-API sự suy luận lưu lượng truy cập với Poisson các sự đến (Reddi
và cộng sự 2019) (The MLPerf Server scenario models cloud/API-like inference traffic with Poisson arrivals (Reddi et al. 2019)).24 Dưới đó mô hình, các sự đến là độc lập và (được) đồng đều phân phối qua thời gian (Under that model, arrivals are independent and uniformly distributed over time).
Phương trình 13.14 biểu diễn (expresses) (cái) được mong đợi lô kích thước cho Poisson các sự đến với tỷ lệ 𝜆arr và việc tạo lô
cửa sổ 𝑇window (Equation 13.14 expresses the expected batch size for Poisson arrivals with rate 𝜆arr and batching window 𝑇window:):
𝐸[lô kích thước] = 𝜆arr ⋅ 𝑇window
(13.14)
Phương sai bằng mức trung bình (một thuộc tính của Poisson các sự phân phối), do đó lô các kích thước dao động
một cách đáng kể tại vừa phải lưu lượng truy cập (The variance equals the mean (a property of Poisson distributions), so batch sizes fluctuate significantly at moderate traffic). Với 𝜆arr = 200 các yêu cầu/giây và 𝑇window = 10 ms, (được) mong đợi
lô kích thước là hai, nhưng xấp xỉ 14 phần trăm của các cửa sổ sẽ có không các yêu cầu (bị lãng phí tính toán các chu kỳ)
trong khi những (cửa sổ) khác có thể có bốn hay nhiều hơn (With 𝜆arr = 200 requests/second and 𝑇window = 10 ms, expected batch size is two, but roughly 14 percent of windows will have zero requests (wasted compute cycles) while others may have four or more).
Một hữu ích (mang tính) khám phá (heuristic) cho việc tạo lô cửa sổ cân bằng việc chờ đợi chi phí đối nghịch thông lượng lợi ích (A useful heuristic for the batching window balances waiting cost against throughput benefit).
Phương trình 13.15 biểu diễn một như vậy quy tắc (Equation 13.15 expresses one such rule:):
𝑇window ≈ min(𝐿lat,SLO − 𝑇svc, √ ( 𝑇svc / 𝜆arr ))
(13.15)
nơi 𝐿lat,SLO là độ trễ SLO, 𝑇svc là dịch vụ thời gian (tính bằng giây), và 𝜆arr là đến tỷ lệ (tính bằng
các yêu cầu mỗi giây), việc làm (cái) thứ hai thuật ngữ nhất quán về mặt thứ nguyên (dimensionally consistent) trong các giây (where 𝐿lat,SLO is the latency SLO, 𝑇svc is the service time (in seconds), and 𝜆arr is the arrival rate (in requests per second), making the second term dimensionally consistent in seconds). Căn-bậc hai (square-root)
hình thức là một cục bộ chi phí-mô hình (mang tính) khám phá: nó cân bằng một cố định mỗi-lô lợi ích đối nghịch một sự chờ đợi chi phí
thứ mà phát triển với đến khoảng (interval) (The square-root form is a local cost-model heuristic: it balances a fixed per-batch benefit against a waiting cost that grows with the arrival interval). Nó không (phải) (là) một đóng-hình thức (closed-form) mức tối ưu (optimum) cho ML việc phục vụ (một cách) đặc thù;
sản xuất các hệ thống hiệu chuẩn (calibrate) cửa sổ (một cách) theo kinh nghiệm (empirically) đối nghịch (được) quan sát lưu lượng truy cập (It is not a closed-form optimum for ML serving specifically; production systems calibrate the window empirically against observed traffic). Một ngược lại trực giác (counterintuitive)
kết quả xuất hiện (emerges) từ phương trình này: khi lưu lượng truy cập tăng lên, tối ưu cửa sổ giảm thiểu trong khi (được) đạt được
lô các kích thước vẫn phát triển (A counterintuitive result emerges from this equation: as traffic increases, the optimal window decreases while achieved batch sizes still grow). Bảng 13.15 chứng minh này hiện tượng qua bốn lưu lượng truy cập các cấp độ (Table 13.15 demonstrates this phenomenon across four traffic levels).
Bảng 13.15: Thích ứng-Lưu lượng truy cập Việc tạo lô: Cao hơn lưu lượng truy cập kích hoạt ngắn hơn các cửa sổ trong khi vẫn việc đạt được lớn hơn trung bình các lô (Table 13.15: Traffic-Adaptive Batching: Higher traffic enables shorter windows while still achieving larger average batches).
Các giá trị được tính toán từ phương trình 13.15 với một 50 ms SLO và một 25 ms dịch vụ-thời gian giả định, do đó độ trễ cột là (cái)
xấp xỉ dịch vụ-cộng-cửa sổ ngân sách thay vì một (được) đo lường sản xuất p99 (Values are computed from equation 13.15 with a 50 ms SLO and a 25 ms service-time assumption, so the latency column is the approximate service-plus-window budget rather than a measured production p99).
Đến Tỷ lệ
Tối ưu Cửa sổ
Trung bình Lô Kích thước
Xấp xỉ Độ trễ
100 QPS
15.8 ms
1.6
40.8 ms
500 QPS
7.1 ms
3.5
32.1 ms
1,000 QPS
5 ms
5
30 ms
5,000 QPS
2.24 ms
11.2
27.2 ms
13.7.6.2 Việc truyền phát (Streaming) lưu lượng truy cập (có tương quan các sự đến)
Tự trị (Autonomous) các phương tiện, video sự phân tích (analytics), và rô bốt (robotics) các hệ thống nhận các đầu vào từ nhiều (được) đồng bộ-
hóa (synchro-nized) các cảm biến (Autonomous vehicles, video analytics, and robotics systems receive inputs from multiple synchro-nized sensors). Một sáu-máy ảnh dòng thời gian (timeline) làm (cho) sự đồng bộ hóa hạn chót (deadline) (trở nên) cụ thể (concrete) (A six-camera timeline makes the synchronization deadline concrete). Bảng 13.16
theo dấu mỗi-sự kiện dòng thời gian cho một được đồng bộ hóa khung (frame) tập hợp trên một phương tiện với sáu các máy ảnh (đang) chụp (capturing)
tại 30 FPS và việc yêu cầu không gian (spatial) sự hợp nhất (fusion) (Table 13.16 traces the per-event timeline for one synchronized frame set on a vehicle with six cameras capturing at 30 FPS and requiring spatial fusion).

750
13.7 Thông lượng Sự tối ưu hóa
Bảng 13.16: Nhiều-máy ảnh khung dòng thời gian: Mỗi-sự kiện dòng thời gian cho một (được) đồng bộ hóa khung tập hợp qua sáu các máy ảnh tại 30 FPS (Table 13.16: Multi-camera frame timeline: Event-by-event timeline for one synchronized frame set across six cameras at 30 FPS).
Ví dụ cho thấy một 7 ms sự đến sự lây lan (spread) giữa (cái) đầu tiên và cuối cùng máy ảnh khung, trong khi hệ thống dành riêng (reserves) 12 ms của 33 ms
cứng hạn chót như (là) sự chập chờn (jitter) sự khoan dung (tolerance) trước khi lô sự suy luận phải bắt đầu (The example shows a 7 ms arrival spread between the first and last camera frame, while the system reserves 12 ms of the 33 ms hard deadline as jitter tolerance before batch inference must begin).
Thời gian
Sự kiện
𝑇 = 0 ms
Các máy ảnh bắt đầu (việc) chụp khung N
𝑇 = 8 ms
Máy ảnh 1 khung đến
𝑇 = 10 ms
Các máy ảnh 2-5 các khung đến
𝑇 = 15 ms
Máy ảnh 6 đến (sự chập chờn)
𝑇 = 15 ms
Lô sự suy luận bắt đầu (6 các hình ảnh)
𝑇 = 25 ms
Sự suy luận (được) hoàn thành
𝑇 = 32 ms
Kết quả (đã) sẵn sàng cho việc lập kế hoạch mô-đun
Ví dụ 13.3: Nhiều-máy ảnh tự trị phương tiện việc phục vụ
Dòng thời gian trong bảng 13.16 cố định việc phục vụ bài toán thông qua một tập hợp của cứng các sự ép buộc thay
vì (các) thống kê đến các tỷ lệ (thứ) mà chi phối Poisson lưu lượng truy cập (The timeline in table 13.16 fixes the serving problem through a set of hard constraints rather than the statistical arrival rates that govern Poisson traffic:):
• Cứng hạn chót: 33 ms (cho) mỗi khung tập hợp (thực-thời gian yêu cầu)
• Lô kích thước: (Được) cố định tại sáu (một (cho) mỗi máy ảnh)
• Sự đồng bộ hóa ngân sách: 12 ms của 33 ms tổng (36 phần trăm cho sự chập chờn sự khoan dung)
• Hết thời gian chờ (Timeout) chính sách (policy): Nếu máy ảnh khung không (được) nhận bởi 𝑇+20 ms, sử dụng trước đó khung
Các hệ thống sự thấu hiểu: Không giống như Poisson lưu lượng truy cập nơi động việc tạo lô tối ưu hóa thông lượng, việc truyền phát
lưu lượng truy cập cố định cả lô kích thước và hạn chót (một cách) bên ngoài, do đó việc phục vụ hệ thống phải tiêu (tiền)
(của) nó ngân sách trên sự đồng bộ hóa các chính sách (thứ) mà xử lý cảm biến sự chập chờn trong khi vẫn việc đáp ứng cứng
hạn chót (Systems insight: Unlike Poisson traffic where dynamic batching optimizes throughput, stream-ing traffic fixes both batch size and deadline externally, so the serving system must spend its budget on synchronization policies that handle sensor jitter while still meeting the hard deadline).
13.7.6.3 Đơn-người dùng lưu lượng truy cập (tuần tự các sự đến)
Việc truyền phát lưu lượng truy cập tương quan các sự đến bởi cảm biến sự đồng bộ hóa, việc làm lô kích thước và hạn chót
bên ngoài (được) cố định (Streaming traffic correlates arrivals by sensor synchronization, making batch size and deadline externally fixed). Tại (cái) đối nghịch (opposite) cuối (end) của quang phổ (spectrum), di động và nhúng các ứng dụng đối mặt không
việc tạo lô cơ hội (nào) (tại tất cả) (At the opposite end of the spectrum, mobile and embedded applications face no batching opportunity at all). Sự tối ưu hóa mục tiêu dịch chuyển từ sự đồng bộ hóa ngân sách đối nghịch
một cứng khung hạn chót (sang) mỗi-yêu cầu độ trễ đối nghịch năng lượng sự tiêu thụ dưới một nhiệt công suất
phong bì (envelope) (The optimization target shifts from synchronization budget against a hard frame deadline to per-request latency against energy consumption under a thermal power envelope).
Di động và nhúng các ứng dụng phục vụ một người dùng tại một thời điểm; MLPerf SingleStream (Đơn Luồng) kịch bản
nắm bắt này tuần tự-việc phục vụ hình dạng (Mobile and embedded applications serve one user at a time; the MLPerf SingleStream scenario captures this sequential-serving shape). Cho ResNet-50 trên một điện thoại, thống trị các chi phí dịch chuyển từ
lô sự hình thành (sang) mỗi-yêu cầu độ trễ và năng lượng (For ResNet-50 on a phone, the dominant costs shift from batch formation to per-request latency and energy).
Khăn ăn Toán học 13.8: ResNet-50: Di động việc phục vụ
Bảng 13.17 phân rã mỗi-giai đoạn (phase) độ trễ và năng lượng cho một đơn-người dùng di động thị giác sự suy luận (Table 13.17 decomposes per-phase latency and energy for a single-user mobile vision inference:):
Bảng 13.17: Di động ResNet-50 đường ống: Mỗi-giai đoạn độ trễ và năng lượng cho một đơn-người dùng di động thị giác sự suy luận,
việc cho thấy rằng JPEG (sự) giải mã trên CPU thống trị năng lượng ngân sách mặc dù (even though) NPU sự suy luận giai đoạn (stage) mang (carries)
mô hình’s (sự) tính toán (Table 13.17: Mobile ResNet-50 pipeline: Per-phase latency and energy for a single-user mobile vision inference, showing that JPEG decode on the CPU dominates the energy budget even though the NPU inference stage carries the model’s compute). Sự tối ưu hóa các mục tiêu dịch chuyển từ thông lượng (sang) năng lượng-mỗi-sự suy luận tại (rìa) cạnh (edge) (Optimization targets shift from throughput to energy-per-inference at the edge).
Giai đoạn
Khoảng thời gian (Duration)
Năng lượng
Các ghi chú
Máy ảnh bộ đệm (sự) đọc
8 ms
0.08 mJ
Hệ thống API
JPEG (sự) giải mã (CPU)
15 ms
1.5 mJ
Đơn-luồng (Single-threaded)
Thay đổi kích thước + Chuẩn hóa
5 ms
0.4 mJ
CPU (việc) tiền xử lý
NPU sự suy luận
12 ms
0.8 mJ
82% sự sử dụng
(Việc) hậu xử lý + UI
5 ms
0.2 mJ
Kết quả (sự) kết xuất (rendering)
Tổng
45 ms
2.98 mJ
22 FPS (được) duy trì

13. Mô hình Việc phục vụ
751
Di động việc phục vụ nút (node) được chi phối bởi bốn các số liệu (The mobile serving node is governed by four metrics:):
• Năng lượng cho mỗi sự suy luận: 2.98 mJ kích hoạt ~12.1M các sự suy luận (cho) mỗi 10 Wh pin (điển hình
điện thoại thông minh) (Energy per inference: 2.98 mJ enables ~12.1M inferences per 10 Wh battery (typical smartphone))
• Nhiệt ngân sách: Tại 2.98 mJ / 45 ms = 66 mW (được) duy trì, vô thời hạn (indefinite) hoạt động mà không có
sự điều chỉnh (throttling) (Thermal budget: At 2.98 mJ / 45 ms = 66 mW sustained, indefinite operation without throttling)
• NPU so với CPU sự đánh đổi: CPU (sự) dự phòng (fallback) thay thế 12 ms, 0.8 mJ NPU sự suy luận giai đoạn
với một 45 ms, 4.2 mJ CPU giai đoạn; (cái) đầy đường ống sẽ tăng từ 45 ms và 2.98 mJ tới
khoảng 78 ms và 6.4 mJ trước (khi) bổ sung hệ thống chi phí hoạt động (NPU vs. CPU trade-off: CPU fallback replaces the 12 ms, 0.8 mJ NPU inference stage with a 45 ms, 4.2 mJ CPU stage; the full pipeline would rise from 45 ms and 2.98 mJ to about 78 ms and 6.4 mJ before additional system overhead).
• Bộ nhớ dấu chân (footprint): 150 MB đỉnh (mô hình + các sự kích hoạt), (việc) cạnh tranh với ứng dụng bộ nhớ (Memory footprint: 150 MB peak (model + activations), competing with app memory)
Các hệ thống sự thấu hiểu: Thậm chí tại lô kích thước một, di động NPU đạt được 82 phần trăm sự sử dụng bởi vì
(của) nó tính toán công suất khớp (với) đơn-hình ảnh các khối lượng công việc (Systems insight: Even at batch size one, the mobile NPU achieves 82 percent utilization because its compute capacity matches single-image workloads). Điều này khác biệt (so) với trung tâm dữ liệu các GPU,
(những) thứ mà đạt được chỉ 15 phần trăm sự sử dụng tại lô kích thước một bởi vì của chúng đồ sộ (massive) tính song song
yêu cầu lớn hơn các lô để bão hòa (This differs from data center GPUs, which achieve only 15 percent utilization at batch size one because their massive parallelism requires larger batches to saturate).
13.7.6.4 Di động việc phục vụ các sự ép buộc
Không giống như đám mây việc phục vụ nơi chi phí thống trị, di động việc phục vụ đối mặt ba có liên quan các sự ép buộc (thứ) mà định hình
sự tối ưu hóa chiến lược (Unlike cloud serving where cost dominates, mobile serving faces three related constraints that shape optimization strategy). (Cái) đầu tiên là một năng lượng ngân sách (thứ) mà thông lượng các mục tiêu bỏ qua, bởi vì mỗi
sự suy luận làm cạn kiệt (depletes) pin (The first is an energy budget that throughput targets ignore, because each inference depletes battery). Trong (được) mô hình hóa đường ống, 2.98 mJ tại 22 FPS rút (draws) khoảng 66 mW cho
sự suy luận con đường một mình (nó), trước (khi) máy ảnh, màn hình hiển thị (display), ISP, và HĐH chi phí hoạt động thêm vào đó tổng trong một đầy ảnh
ứng dụng, do đó sự tối ưu hóa mục tiêu dịch chuyển từ thông lượng (sang) năng lượng-mỗi-sự suy luận (In the modeled pipeline, 2.98 mJ at 22 FPS draws about 66 mW for the inference path alone, before camera, display, ISP, and OS overhead add to that total in a full photo app, so the optimization target shifts from throughput to energy-per-inference). Nhiệt sự điều chỉnh (throttling)
kép (compounds) (làm trầm trọng) này giới hạn, vì (được) duy trì cao-công suất hoạt động kích hoạt nhiệt sự quản lý: một khi
SoC đạt tới (của) nó nhiệt trần (điển hình 45 °C tiếp giáp (junction)), HĐH giảm thiểu NPU tần số bởi
30–50 phần trăm, (việc) làm suy giảm (degrading) cả độ trễ và thông lượng, (đó) là lý do tại sao bùng nổ (bursty) các khối lượng công việc (thứ) mà cho phép
sự làm mát giữa các đợt vượt trội (outperform) (so với) (được) duy trì tối đa thông lượng (Thermal throttling compounds this limit, since sustained high-power operation triggers thermal management: once the SoC reaches its thermal ceiling (typically 45 °C junction), the OS reduces NPU frequency by 30–50 percent, degrading both latency and throughput, which is why bursty workloads that allow cooling between bursts outperform sustained maximum throughput). Bộ nhớ các sự ép buộc đóng (lại)
tập hợp (lại), bởi vì di động các thiết bị chia sẻ (bị) giới hạn RAM qua các ứng dụng (Memory constraints close the set, because mobile devices share limited RAM across applications). Một mô hình (đang) tiêu thụ 500 MB
có thể bị trục xuất (evicted) trong suốt nền (background) hoạt động, (việc) ép buộc một sự tải lại (lạnh sự khởi động) (thứ) mà thêm 200–500 ms của
độ trễ, và thậm chí một 150 MB dấu chân trở nên có vấn đề khi mô hình phải cùng tồn tại (coexist) với (những) khác
ứng dụng các thành phần (A model consuming 500 MB may be evicted during background operation, forcing a reload (cold start) that adds 200–500 ms of latency, and even a 150 MB footprint becomes problematic when the model must coexist with other app components). Hiệu quả-bộ nhớ sự lượng tử hóa cải thiện người dùng trải nghiệm thông qua nhanh hơn mô hình
sự khôi phục, và được ánh xạ-bộ nhớ mô hình việc tải (phần 13.6.3) giúp ích hơn nữa (further) bằng cách việc tải các trang trên
sự yêu cầu (demand) thay vì việc yêu cầu (cái) đầy mô hình trong bộ nhớ (Memory-efficient quantization improves user experience through faster model restoration, and memory-mapped model loading (section 13.6.3) helps further by loading pages on demand rather than requiring the full model in memory).
Những các sự ép buộc này làm (cho) di động việc phục vụ sự tối ưu hóa (về mặt) định tính (qualitatively) khác biệt (so) với đám mây sự tối ưu-
hóa (These constraints make mobile serving optimization qualitatively different from cloud optimiza-tion). Mục tiêu không (phải) (là) tối đa thông lượng nhưng (là) có-thể-duy-trì (sustainable) hiệu suất, việc duy trì (có thể) chấp nhận (được)
độ trễ mà không có nhiệt sự điều chỉnh hay quá mức pin (sự) rút (cạn) (The goal is not maximum throughput but sustainable performance, maintaining acceptable latency without thermal throttling or excessive battery drain).
13.7.6.5 Lưu lượng truy cập mẫu bản tóm tắt
Thích ứng-lưu lượng truy cập việc tạo lô điều chỉnh việc tạo lô cửa sổ khi hàng đợi độ sâu và yêu cầu tỷ lệ thay đổi (Traffic-adaptive batching adjusts the batching window as queue depth and request rate change).
Bảng 13.18 ánh xạ bốn MLPerf các kịch bản tới của chúng sự triển khai các ngữ cảnh và tối ưu việc tạo lô
các chiến lược, việc cung cấp một quyết định khuôn khổ cho việc phục vụ hệ thống thiết kế (Table 13.18 maps the four MLPerf scenarios to their deployment contexts and optimal batching strategies, providing a decision framework for serving system design).
Bảng 13.18: Lưu lượng truy cập Các mẫu và Việc tạo lô Các chiến lược: Bốn MLPerf sự suy luận các kịch bản ánh xạ tới khác biệt sự triển khai các ngữ cảnh (Table 13.18: Traffic Patterns and Batching Strategies: The four MLPerf inference scenarios map to distinct deployment contexts).
Máy chủ lưu lượng truy cập (đám mây các API) sử dụng động việc tạo lô với thời gian chờ; MultiStream (tự trị việc lái xe) sử dụng (được) đồng bộ hóa cảm biến
sự hợp nhất; SingleStream (di động) xử lý các yêu cầu (một cách) cá nhân; Ngoại tuyến (lô việc xử lý) tối đa hóa lô kích thước cho thông lượng (Server traffic (cloud APIs) uses dynamic batching with timeout; MultiStream (autonomous driving) uses synchronized sensor fusion; SingleStream (mobile) processes requests individually; Offline (batch processing) maximizes batch size for throughput).
Kịch bản
Ngữ cảnh
Chiến lược
Trọng tâm (Focus)
Máy chủ
Đám mây các API, web các dịch vụ
Động việc tạo lô với thời gian chờ
Cửa sổ sự điều chỉnh,
sự sử dụng-độ trễ đường cong
MultiStream (Đa luồng)
Tự trị việc lái xe, video
sự phân tích
(Được) đồng bộ hóa cảm biến sự hợp nhất
Sự chập chờn (việc) xử lý, hạn chót
các sự đảm bảo (guarantees)
SingleStream (Đơn luồng)
Di động các ứng dụng, nhúng các thiết bị
Không việc tạo lô (𝐵 = 1)
Việc tiền xử lý, công suất tính hiệu quả
Ngoại tuyến
Lô việc xử lý, dữ liệu các đường ống
Tối đa lô kích thước
Thông lượng, phần cứng
sự sử dụng
MLPerf Máy chủ kịch bản nắm bắt đám mây API lưu lượng truy cập, MultiStream nắm bắt (được) đồng bộ hóa cảm biến
các khối lượng công việc, và Ngoại tuyến sự suy luận nắm bắt lô việc xử lý nơi thông lượng thống trị độ trễ (The MLPerf Server scenario captures cloud API traffic, MultiStream captures synchronized sensor workloads, and Offline inference captures batch processing where throughput dominates latency).

13.8 LLM Việc phục vụ (LLM Serving)
752
25
Tự hồi quy (Autoregressive): Từ
Hy Lạp (Greek) auto- (tự) và Latinh (Latin)
regressus (một sự quay trở lại)—(cái)
đầu ra “hồi quy” (regresses) trên chính nó.
George Udny Yule đã giới thiệu
tự hồi quy các mô hình trong 1927
cho việc phân tích vết đen mặt trời (sunspot) các chu kỳ.
Trong ngôn ngữ việc mô hình hóa, mỗi
đầu ra mã thông báo điều kiện (conditions) trên
tất cả trước đó được tạo sinh các mã thông
báo (to-kens), việc tạo ra một nối tiếp (serial) sự phụ thuộc
(depen-dency) (thứ) mà ngăn chặn (cái) tính song-
song (được) khai thác (exploited) trong suốt sự đào-
tạo (train-ing).
Này nối tiếp nút thắt cổ chai
giải thích tại sao LLM việc phục vụ
là bị giới hạn-bởi-bộ nhớ-băng thông
thay vì bị giới hạn-bởi-tính toán:
mô hình các trọng số phải được
đọc từ bộ nhớ một lần (cho) mỗi
mã thông báo, bất kể (của) (có) sẵn sàng
tính toán công suất.
TTFT và TPOT sống trong khác biệt
nút thắt cổ chai các chế độ.
Điểm kiểm tra (Checkpoint) 13.3: Việc tạo lô và lưu lượng truy cập các mẫu
Việc tạo lô là chính đòn bẩy cho việc phục vụ tính kinh tế, nhưng tối ưu chiến lược phụ thuộc vào
ngữ cảnh (Batching is the primary lever for serving economics, but the optimal strategy depends on context).
□ Thông lượng-độ trễ sự đánh đổi: Bạn có thể giải thích tại sao lô kích thước 32 đạt được 6× cao hơn
thông lượng (so với) lô kích thước một, (nhưng) tuy nhiên (yet) một sản xuất hệ thống với một 20 ms SLO có thể vẫn
chọn lô kích thước tám (hay không)? (Throughput-latency trade-off: Can you explain why batch size 32 achieves 6× higher throughput than batch size one, yet a production system with a 20 ms SLO might still choose batch size eight?)
□ Động so với tĩnh việc tạo lô: Bạn có thể mô tả tại sao tĩnh việc tạo lô (việc chờ đợi cho một đầy
lô) thất bại dưới có thể thay đổi lưu lượng truy cập, và cách động việc tạo lô với một thời gian cửa sổ giải quyết
điều này (hay không)? (Dynamic vs. static batching: Can you describe why static batching (waiting for a full batch) fails under variable traffic, and how dynamic batching with a time window solves this?)
□ Lưu lượng truy cập mẫu sự khớp (matching): Được cho một sự triển khai kịch bản (ví dụ, đám mây API, tự-
trị (au-tonomous) phương tiện, di động ứng dụng), bạn có thể chọn (cái) thích hợp MLPerf kịch bản và
giải thích tại sao đó việc tạo lô chiến lược phù hợp (hay không)? (Traffic pattern matching: Given a deployment scenario (for example, cloud API, au-tonomous vehicle, mobile app), can you select the appropriate MLPerf scenario and explain why that batching strategy fits?)
□ Thích ứng các cửa sổ: Bạn có thể giải thích tại sao tối ưu việc tạo lô cửa sổ giảm thiểu khi
lưu lượng truy cập tăng lên, mặc dù lô các kích thước phát triển (hay không)? (Adaptive windows: Can you explain why the optimal batching window decreases as traffic increases, even though batch sizes grow?)
Các việc tạo lô các chiến lược được kiểm tra cho đến nay chia sẻ một tới hạn giả định: mỗi yêu cầu tạo ra một
đơn, cố định-kích thước đầu ra—một sự phân loại nhãn, một (đường) bao hộp (bounding box), một nhúng vectơ (The batching strategies examined so far share a critical assumption: each request produces a single, fixed-size output—one classification label, one bounding box, one embedding vector). Giả định
này chi phối việc xếp hàng đợi toán học, Pareto biên giới sự phân tích, và thích ứng-lưu lượng truy cập cửa sổ
sự điều chỉnh (This assumption governs the queuing math, the Pareto frontier analysis, and the traffic-adaptive window tuning). Nhanh nhất-đang phát triển (fastest-growing) thể loại (category) của việc phục vụ các khối lượng công việc, tuy nhiên, vi phạm giả định này
(một cách) hoàn toàn (The fastest-growing category of serving workloads, however, violates this assumption entirely). Lớn ngôn ngữ các mô hình tạo sinh các đầu ra mã thông báo bởi mã thông báo, với mỗi mã thông báo (việc) phụ thuộc vào
mọi (mã thông báo) trước đó (Large language models generate outputs token by token, with each token depending on every previous one). Một đơn yêu cầu có thể tạo ra hàng trăm hay hàng ngàn (của) các mã thông báo qua các giây
của (đã) trôi qua (elapsed) thời gian, tuy nhiên (yet) phải cảm thấy phản hồi (nhanh) từ (cái) đầu tiên mã thông báo trở đi (onward) (A single request may produce hundreds or thousands of tokens over seconds of elapsed time, yet must feel responsive from the first token onward). Này cơ bản sự dịch chuyển (shift) từ
cố định-đầu ra (sang) có thể thay đổi-chiều dài, việc truyền phát-đầu ra việc phục vụ xây dựng (một cách) trực tiếp trên liên tục việc tạo lô
và KV-bộ nhớ đệm việc phân trang (đã) được thiết lập cho tự hồi quy sự tạo sinh (This fundamental shift from fixed-output to variable-length, streaming-output serving builds directly on the continuous batching and KV-cache paging already established for autoregressive generation). (Những) gì nó thêm là sự chia nhỏ-giai đoạn (phase-split)
các số liệu cho việc điền trước và việc giải mã, việc giải mã các chiến lược (thứ) mà đánh đổi đầu ra chất lượng đối nghịch mỗi-mã thông báo chi phí,
và bộ nhớ các chiến thuật (tactics) như là tiền tố sự tái sử dụng và việc giảm tải (offloading) (thứ) mà khai thác được chia sẻ ngữ cảnh (What it adds are phase-split metrics for prefill and decode, decoding strategies that trade output quality against per-token cost, and memory tactics such as prefix reuse and offloading that exploit shared context).
13.8 LLM Việc phục vụ
Lớn ngôn ngữ các mô hình giới thiệu ba các thuộc tính vắng mặt (absent) từ truyền thống việc phục vụ: tự hồi quy
sự tạo sinh25 (mỗi mã thông báo phụ thuộc vào tất cả trước đó các mã thông báo, việc làm đầu ra (về mặt) vốn có (trở nên) tuần tự) (Large language models introduce three properties absent from traditional serving: autoregressive generation25 (each token depends on all previous tokens, making output inherently sequential)),
có thể thay đổi-chiều dài đầu ra (phản hồi chiều dài là không được biết tại yêu cầu thời gian, việc làm mất hiệu lực (invalidating) cố định-lô các giả định) (variable-length output (response length is unknown at request time, invalidating fixed-batch assump-tions)), và có trạng thái bộ nhớ (khóa-giá trị bộ nhớ đệm phát triển với mỗi (được) tạo sinh mã thông báo, việc tạo ra động
bộ nhớ áp lực (thứ) mà truyền thống các mô hình không bao giờ đối mặt) (and stateful memory (the key-value cache grows with each generated token, creating dynamic memory pressure that traditional models never face)). Cùng nhau, những các thuộc tính này tạo ra một (về mặt) định tính
khác biệt việc phục vụ thách thức (Together, these properties create a qualitatively different serving challenge). p50, p95, và p99 các số liệu (thứ) mà chi phối sự phân loại việc phục vụ vẫn
quan trọng, nhưng chúng áp dụng cho khác biệt các giai đoạn của yêu cầu—(cái) ban đầu dấu nhắc việc xử lý và (cái)
sau đó (subsequent) mã thông báo sự tạo sinh (The p50, p95, and p99 metrics that govern classification serving still matter, but they apply to different phases of the request—the initial prompt processing and the subsequent token generation). Cơ bản các nguyên tắc của việc xếp hàng đợi lý thuyết, việc tạo lô các sự đánh đổi,
và độ trễ các ngân sách áp dụng (một cách) phổ quát; LLM việc phục vụ thêm đặc thù-miền các kỹ thuật (lên) trên này
nền tảng (The foundational principles of queuing theory, batching trade-offs, and latency budgets apply universally; LLM serving adds domain-specific techniques atop this foundation).
13.8.1 Hiệu suất các số liệu: TTFT và TPOT
Tạo sinh các mô hình tạo ra một luồng của các mã thông báo thay vì một đơn đầu ra tensor (Generative models produce a stream of tokens rather than a single output tensor). Này việc truyền phát
bản chất yêu cầu dành riêng (dedicated) LLM hiệu suất các số liệu (thứ) mà phản ánh nội bộ trạng thái sự chuyển đổi (transition) từ
“việc điền trước” (việc xử lý đầu vào) (tới) “việc giải mã” (việc tạo sinh đầu ra) (This streaming nature requires dedicated LLM performance metrics that reflect the internal state transition from “prefill” (processing input) to “decode” (generating output)). Hai chính thước đo (measures) là Thời gian tới Đầu tiên
Mã thông báo (Time to First Token - TTFT) và Thời gian Mỗi Đầu ra Mã thông báo (Time Per Output Token - TPOT), (những) thứ mà nắm bắt (sự) phản hồi (nhanh) và (tính) trôi chảy (fluidity)
(một cách) tương ứng (respectively) (The two key measures are Time to First Token (TTFT) and Time Per Output Token (TPOT), which capture responsiveness and fluidity respectively).
Định nghĩa 13.6: LLM hiệu suất các số liệu
LLM Hiệu suất Các số liệu là hai-chiều (two-dimensional) các phép đo (measurements) của độ trễ cho việc truyền phát
tự hồi quy sự tạo sinh (LLM Performance Metrics are the two-dimensional measurements of latency for streaming autoregressive generation).

13. Mô hình Việc phục vụ
753
1. Tầm quan trọng: Chúng phân rã được nhận thức-bởi-người dùng độ trễ thành Thời gian tới Đầu tiên Mã thông báo (TTFT)
((được) chi phối bởi bị giới hạn-bởi-tính-toán Việc điền trước Giai đoạn) và Thời gian Mỗi Đầu ra Mã thông báo (TPOT)
((được) chi phối bởi bị giới hạn-bởi-bộ-nhớ-băng-thông Việc giải mã Giai đoạn) (Significance: They decompose user-perceived latency into Time to First Token (TTFT) (governed by the compute-bound Prefill Phase) and Time Per Output Token (TPOT) (governed by the memory-bandwidth-bound Decode Phase)).
2. Sự khác biệt: Không giống như Cố định-Đầu ra Các số liệu (ví dụ, đầu cuối-tới-đầu cuối độ trễ), LLM các số liệu
đo lường Tính trôi chảy của Sự tạo sinh, việc thừa nhận (acknowledging) rằng người dùng trải nghiệm phụ thuộc vào
nhịp điệu (rhythm) của mã thông báo sự đến (Distinction: Unlike Fixed-Output Metrics (for example, end-to-end latency), LLM metrics measure the Fluidity of Generation, acknowledging that the user experience depends on the rhythm of token arrival).
3. Phổ biến cạm bẫy: Một thường xuyên quan niệm sai lầm là rằng một “nhanh mô hình” có một thấp TTFT (A frequent misconception is that a “fast model” has a low TTFT). Trong
thực tế, một mô hình có thể có một nhanh TTFT nhưng một chậm chạp (sluggish) TPOT (nếu bộ nhớ bức tường (BW) là
nút thắt cổ chai), việc dẫn tới một bực bội (frustrating) người dùng trải nghiệm nơi câu trả lời bắt đầu (một cách) nhanh chóng
nhưng “nói lắp” (stutters) sau đó (thereafter) (In reality, a model can have a fast TTFT but a sluggish TPOT (if the memory wall (BW) is the bottleneck), leading to a frustrating user experience where the answer starts quickly but “stutters” thereafter).
Những hai các số liệu này nắm bắt (khác) biệt người dùng trải nghiệm các khía cạnh, và sản xuất các hệ thống thiết lập riêng biệt
SLO các mục tiêu cho mỗi (số liệu) (These two metrics capture distinct user experience aspects, and production systems set separate SLO targets for each).
Các hệ thống Góc nhìn 13.9: LLM việc phục vụ độ trễ các mục tiêu
Tương tác LLM các dịch vụ thường cần riêng biệt các SLO cho sự phản hồi (nhanh), sự tạo sinh tính trôi chảy, và
hạm đội thông lượng (Interactive LLM services usually need separate SLOs for responsiveness, generation fluidity, and fleet throughput). Các giá trị bên dưới là có tính minh họa (illustrative) các mục tiêu thay vì phổ quát các yêu cầu (The values below are illustrative targets rather than universal requirements:):
• TTFT: < 500 ms (cho một 1000-mã thông báo dấu nhắc)
• TPOT: < 50 ms ((sự) tương đương (tới) ~20 các mã thông báo/s, nhanh hơn con người việc đọc tốc độ)
• Thông lượng: > 1000 các mã thông báo/s tổng (aggregate) qua (đang) hoạt động việc phục vụ các bản sao
Các hệ thống điểm là rằng một đơn “độ trễ” con số che giấu việc điền trước/việc giải mã (sự) chia nhỏ: TTFT là
trống-màn hình ngân sách, TPOT là việc đọc-luồng (reading-flow) ngân sách, và tổng dịch vụ thông lượng,
được đo lường như (là) các mã thông báo/s (được) tính tổng qua (đang) hoạt động việc phục vụ các bản sao, quyết định liệu những các mục tiêu đó
tổ chức (hold) dưới (được) chia sẻ tải (hay không) (The systems point is that a single “latency” number hides the prefill/decode split: TTFT is the blank-screen budget, TPOT is the reading-flow budget, and aggregate service throughput, measured as tokens/s summed across active serving replicas, determines whether those targets hold under shared load).
13.8.2 Việc giải mã các chiến lược
Việc đáp ứng những TPOT các mục tiêu này phụ thuộc vào nhiều (thứ) hơn bộ nhớ băng thông một mình (nó): thuật toán được sử dụng
để chọn mỗi mã thông báo cũng ảnh hưởng mỗi-mã thông báo độ trễ và đầu ra chất lượng (Meeting these TPOT targets depends on more than memory bandwidth alone: the algorithm used to select each token also affects per-token latency and output quality). Tạo sinh các mô hình yêu cầu
việc giải mã các chiến lược (thứ) mà đánh đổi chất lượng, tính đa dạng (diversity), và độ trễ (Generative models require decoding strategies that trade off quality, diversity, and latency). Sự lựa chọn của việc giải mã chiến lược
(một cách) quyết liệt ảnh hưởng (tới) cả đầu ra chất lượng và thuộc về tính toán chi phí (The choice of decoding strategy dramatically affects both output quality and computational cost).
(Cái) đơn giản nhất cách tiếp cận, tham lam (greedy) việc giải mã, chọn (cái) cao nhất-xác suất mã thông báo tại mỗi bước tại
chi phí của một mô hình (đường) chuyền (pass) cho mỗi mã thông báo (The simplest approach, greedy decoding, selects the highest-probability token at each step at the cost of one model pass per token). Nó là nhanh nhưng thường tạo ra lặp đi lặp lại (repetitive) các đầu ra bởi vì nó không thể
phục hồi từ sớm các sai lầm (It is fast but often produces repetitive outputs because it cannot recover from early mistakes). Chùm (Beam) (sự) tìm kiếm cải thiện chất lượng bằng cách việc duy trì nhiều ứng cử viên (candidate)
các chuỗi và việc chọn (cái) cao nhất-ghi điểm (scoring) (được) hoàn thành chuỗi, nhưng nó nhân (multiplies) mỗi-mã thông báo tính toán
với chùm chiều rộng (Beam search improves quality by maintaining multiple candidate sequences and selecting the highest-scoring complete sequence, but it multiplies per-token compute by the beam width). Việc lấy mẫu (Sampling) với nhiệt độ (temperature), top-𝑘, và top-𝑝 (cũng được gọi (là) hạt nhân (nucleus) việc lấy mẫu)
bơm (injects) được kiểm soát tính ngẫu nhiên (randomness) cho tính đa dạng tại không đáng kể phụ (extra) tính toán (Holtzman và cộng sự 2020) (Sampling with temperature, top-𝑘, and top-𝑝(also called nucleus sampling) injects controlled randomness for diversity at negligible extra compute (Holtzman et al. 2020));
(của) nó việc phục vụ chi phí nằm (lies) ít hơn trong số học (arithmetic) (so với) trong đầu ra-chiều dài phương sai, thứ mà mở rộng (sự) lây lan của
chuỗi các chiều dài (thứ) mà liên tục việc tạo lô phải hấp thụ (absorb) (its serving cost lies less in arithmetic than in output-length variance, which widens the spread of sequence lengths that continuous batching must absorb). Những các chi phí này ghép (compound) tại mỗi-mã thông báo
cấp độ (Meister và cộng sự 2020): chùm (sự) tìm kiếm với chiều rộng năm chạy xấp xỉ 5× tính toán của tham lam
việc giải mã cho mọi mã thông báo, (đó) là lý do tại sao tương tác, nhạy cảm-độ trễ các sự triển khai hiếm khi (rarely) sử dụng nó và
thay vào đó (với tới) (reach for) tham lam hay việc lấy mẫu (These costs compound at the per-token level (Meister et al. 2020): beam search with width five runs roughly 5× the compute of greedy decoding for every token, which is why interactive, latency-sensitive deployments rarely use it and instead reach for greedy or sampling).
Sản xuất LLM các hệ thống trả về các mã thông báo khi chúng được tạo ra thay vì việc chờ đợi cho (được) hoàn thành
sự tạo sinh (Production LLM systems return tokens as they are produced rather than waiting for complete generation). Này việc truyền phát phản hồi biến đổi người dùng trải nghiệm: một hai-giây tổng sự tạo sinh
cảm thấy phản hồi khi các mã thông báo truyền phát (một cách) liên tục, nhưng cảm thấy (bị) phá vỡ khi người dùng nhìn chằm chằm (stare) tại một trống
màn hình trong hai giây (This streaming response transforms the user experience: a two-second total generation feels responsive when tokens stream continuously, but feels broken when users stare at a blank screen for two seconds). Việc truyền phát yêu cầu cơ sở hạ tầng sự hỗ trợ cho (được) phân đoạn HTTP các phản hồi
và phía-máy khách (client-side) gia tăng (incremental) (sự) kết xuất (Streaming requires infrastructure support for chunked HTTP responses and client-side incremental rendering). Độ trễ hồ sơ (profile) dịch chuyển (một cách) tương ứng: TTFT quyết định
khi (nào) đầu ra bắt đầu (việc) xuất hiện (sự phản hồi), trong khi TPOT quyết định (cái) được nhận thức sự tạo sinh
tốc độ (tính trôi chảy) (The latency profile shifts accordingly: TTFT determines when output starts appearing (responsiveness), while TPOT determines the perceived generation speed (fluidity)). Một khi sự tạo sinh được truyền phát mã thông báo bởi mã thông báo, việc phục vụ nút thắt cổ chai dịch chuyển từ một
sự dự đoán yêu cầu tới một có trạng thái chuỗi (thứ) mà (của) nó bộ nhớ dấu chân phát triển trên mọi bước (Once generation is streamed token by token, the serving bottleneck shifts from one prediction request to a stateful sequence whose memory footprint grows on every step).

754
13.8 LLM Việc phục vụ
26
KV Bộ nhớ đệm (Key-Value
Cache): Để tránh dư thừa (redundant)
công việc, hệ thống lưu trong bộ nhớ đệm
Khóa và Giá trị các vectơ từ
trước đó các mã thông báo, (những) thứ (mà) duy-
trì (re-main) hợp lệ (valid) trong suốt sự tạo-
sinh (gen-eration).
Này thiết kế sự lựa chọn
là trực tiếp nguyên nhân (cause) của động (dy-namic)
bộ nhớ sự phát triển (được) mô-
tả; bộ nhớ đệm’s kích thước phát triển
(một cách) tuyến tính với mọi (được) tạo sinh
mã thông báo, việc làm bộ nhớ sự quản-
lý (man-agement), không (phải) tính toán, (trở thành)
chính sự ép buộc (constraint). Cho
70-tỷ-tham số-lớp (class)
được nhóm-truy vấn-sự chú ý (grouped-query-attention) kích-
cỡ (siz-ing) ví dụ trong phần này,
FP16 KV bộ nhớ đệm là khoảng
0.31 MB cho mỗi mã thông báo cho mỗi chuỗi (se-quence);
được nhóm-truy vấn sự chú-
ý (grouped-query atten-tion) (GQA), được sử dụng trong Llama-
gia đình các mô hình như là Llama
3, chia sẻ khóa/giá trị các đầu (heads)
qua nhiều truy vấn các đầu,
việc giảm thiểu bộ nhớ đệm (một cách) tương đối
(so với) đầy nhiều-đầu sự chú ý
(Dubey và cộng sự
2024).
Một
lô của 32 các yêu cầu tại một
8,000-mã thông báo ngữ cảnh do đó
yêu cầu xấp xỉ 80 GB chỉ cho
KV bộ nhớ đệm, vài lần lớn hơn
vẫn mà không có được nhóm-truy vấn
hay nhiều-truy vấn sự chú ý.
27
Suy đoán (Speculative) Việc giải mã:
Một nhỏ “nháp” mô hình tạo-
sinh 𝑘 ứng cử viên các mã thông báo tự-
hồi quy; lớn mục-
tiêu mô hình sau đó xác minh
(cái) được đề xuất khối trong song song
(Leviathan và cộng sự 2023). Khi
nháp mô hình’s các đề xuất (proposals)
được chấp nhận tại tỷ lệ 𝛼, hiệu-
quả thông lượng có thể mở rộng
với số lượng của (được) chấp nhận
các mã thông báo cho mỗi sự xác minh bước.
Điều này phá vỡ nối tiếp tự hồi-
quy (autore-gressive) nút thắt cổ chai tại thời gian chạy (run-time)
lớp, không (phải) kiến trúc
lớp.
13.8.3 Bộ nhớ và KV bộ nhớ đệm
Tạo sinh sự suy luận yêu cầu việc quản lý KV Bộ nhớ đệm26, một có trạng thái bộ nhớ cấu trúc (thứ) mà phát triển
với chuỗi chiều dài (Generative inference requires managing the KV Cache26, a stateful memory structure that grows with sequence length). Không giống như truyền thống các mô hình nơi bộ nhớ cách sử dụng là hằng số (cho) mỗi lô, LLM
bộ nhớ cách sử dụng là động (Unlike traditional models where memory usage is constant per batch, LLM memory usage is dynamic). Mỗi (được) tạo sinh mã thông báo thêm (vào) ngữ cảnh cửa sổ, việc tiêu thụ bổ sung
GPU bộ nhớ thông qua trạng thái sự tích lũy (accumulation), và có thể thay đổi-chiều dài các chuỗi có thể dẫn tới bộ nhớ
sự phân mảnh nếu không được quản lý (một cách) rõ ràng (Each generated token adds to the context window, consuming additional GPU memory through state accumulation, and variable-length sequences can lead to memory fragmentation if not managed explicitly).
13.8.3.1 Tiền tố việc lưu trong bộ nhớ đệm và bộ nhớ việc giảm tải
Liên tục việc tạo lô và PagedAttention các kỹ thuật được bao phủ trong phần 13.7.4 giải quyết yêu cầu
sự lập lịch và bộ nhớ đệm việc phân trang; (cái) còn lại bộ nhớ áp lực có thể được (làm) giảm nhẹ hơn nữa (further mitigated) thông qua
thuộc về kiến trúc các chiến lược (thứ) mà khai thác yêu cầu các mẫu (The continuous batching and PagedAttention techniques covered in section 13.7.4 address request scheduling and cache paging; the remaining memory pressure can be further mitigated through architectural strategies that exploit request patterns). Tiền tố Việc lưu trong bộ nhớ đệm (Prefix Caching) lưu trữ KV bộ nhớ đệm của phổ biến
hướng dẫn các tiền tố (như là một 2,000-mã thông báo hệ thống dấu nhắc hay một (được) chia sẻ truy xuất-được tăng cường sự tạo sinh
(retrieval-augmented generation - RAG) ngữ cảnh), việc cho phép nhiều độc lập các yêu cầu (để) tái sử dụng giống nhau được tính toán trước (precomputed) ẩn (hidden) các trạng thái (Prefix Caching stores the KV cache of common instruction prefixes (such as a 2,000-token system prompt or a shared retrieval-augmented generation (RAG) context), allowing many independent requests to reuse the same precomputed hidden states).
Cho 𝑁 các yêu cầu (đang) chia sẻ một tiền tố của 𝑆prefix các mã thông báo, (cái) được lưu (saved) việc điền trước công việc là xấp xỉ (𝑁−1)𝑆prefix
mã thông báo các bước, cộng (các) được tránh (avoided) các (sự) đọc và các (sự) ghi của tiền tố KV trạng thái (For 𝑁requests sharing a prefix of 𝑆prefix tokens, the saved prefill work is roughly (𝑁−1)𝑆prefix token steps, plus the avoided reads and writes of the prefix KV state). Cho nhiều-lượt các cuộc hội thoại,
điều này “(sự) lưu trong bộ nhớ đệm của (cái) quá khứ” cho phép hệ thống (để) xử lý chỉ (những) mới các mã thông báo trong mỗi lượt (For multi-turn conversations, this “caching of the past” allows the system to process only the new tokens in each turn).
Khi tổng KV bộ nhớ đệm vượt quá GPU VRAM, các hệ thống có thể sử dụng KV Bộ nhớ đệm Việc giảm tải (KV Cache Offloading).
Này chiến lược tràn (spills) không hoạt động hay thấp-ưu tiên (priority) ngữ cảnh các cửa sổ (sang) máy chủ CPU RAM hay NVMe SSD,
việc giải phóng VRAM cho (đang) hoạt động sự tạo sinh (This strategy spills inactive or low-priority context windows to host CPU RAM or NVMe SSD, freeing VRAM for active generation). Việc tải lại chi phí được giới hạn (bên) dưới bởi các byte được di chuyển (chia) cho (bởi)
PCIe hay NVMe băng thông, trước (khi) phần mềm chi phí hoạt động và việc xếp hàng đợi được thêm (vào) (The reload cost is bounded below by bytes moved divided by PCIe or NVMe bandwidth, before software overhead and queueing are added). Việc giảm tải do đó
ngăn chặn Hết-Bộ-nhớ (OOM) các sự thất bại và kích hoạt lớn hơn ngữ cảnh các cửa sổ, nhưng nó cũng tạo ra
sự thân thiết, sự vô hiệu hóa (invalidation), và nóng-việc giải mã độ trễ các rủi ro (risks) (thứ) mà phải được lập ngân sách (một cách) rõ ràng (Offloading therefore prevents Out-of-Memory (OOM) failures and enables larger context windows, but it also creates affinity, invalidation, and hot-decode latency risks that must be budgeted explicitly). Nâng cao
các kỹ thuật việc bao gồm suy đoán việc giải mã27 và phân tán tính song song, nơi một yêu cầu bị chia
qua nhiều các thiết bị hay các máy, được bao phủ trong (được) chuyên môn hóa (specialized) các sự xử lý của lớn-quy mô các hệ thống (Advanced techniques including speculative decoding27 and distributed parallelism, where one request is split across multiple devices or machines, are covered in specialized treatments of large-scale systems).
Thuộc về tính toán cường độ (intensity) của việc quản lý KV các bộ nhớ đệm qua đồng thời các yêu cầu dấy lên (raises) một rộng hơn
câu hỏi về năng lượng chi phí của mỗi mã thông báo (được) tạo sinh (The computational intensity of managing KV caches across concurrent requests raises a broader question about the energy cost of each token generated). Không giống như sự phân loại các mô hình nơi năng lượng
cho mỗi sự suy luận là hằng số, LLM năng lượng sự tiêu thụ mở rộng với phản hồi chiều dài—mọi (được) tạo sinh
mã thông báo yêu cầu việc đọc (cái) toàn bộ mô hình từ bộ nhớ (Unlike classification models where energy per inference is constant, LLM energy consumption scales with response length—every generated token requires reading the entire model from memory). Năng lượng và carbon (sự) hạch toán (accounting) dịch
những phần cứng các nhu cầu (demands) này thành các số liệu (thứ) mà làm (cho) (cái) thuộc về môi trường (environmental) tác động (trở nên) cụ thể (Energy and carbon accounting translate these hardware demands into metrics that make the environmental impact concrete).
Khăn ăn Toán học 13.9: Carbon chi phí của một cuộc trò chuyện (chat)
Bài toán: Làm thế nào nhiều năng lượng (does) một (được) hỗ trợ-bởi-H100 trò chuyện dịch vụ tiêu tốn (cho) mỗi (được) tạo sinh mã thông báo và
cho một phản hồi với 500 các mã thông báo? (Problem: How much energy does an H100-backed chat service spend per generated token and for a response with 500 tokens?)
Khi các LLM mở rộng, các joule cho mỗi mã thông báo trở thành một hạng-nhất (first-class) hoạt động số liệu song song với (alongside) độ trễ (As LLMs scale, joules per token becomes a first-class operational metric alongside latency). Cho
kịch bản này việc sử dụng một H100 GPU (700 W TDP), năng lượng dấu chân tuân theo từ thông lượng
và công suất (Choquette 2023) (For this scenario using an H100 GPU (700 W TDP), the energy footprint follows from throughput and power (Choquette 2023):):
1. Thông lượng: 114 đồng thời các yêu cầu × 8 các mã thông báo/s cho mỗi yêu cầu ≈ 912 các mã thông báo/s (Throughput: 114 concurrent requests × 8 tokens/s per request ≈912 tokens/s).
2. Công suất: 700 W (GPU) + 300 W (Máy chủ (Host)/Chi phí hoạt động) = 1000 W (Power: 700 W (GPU) + 300 W (Host/Overhead) = 1000 W).
3. Năng lượng cho mỗi mã thông báo: 1000 W / 912 các mã thông báo/s ≈ 1.0965 J/mã thông báo (Energy per token: 1000 W / 912 tokens/s ≈1.0965 J/token)
Các hệ thống sự thấu hiểu: Một điển hình phản hồi của 500 các mã thông báo tiêu thụ ≈ 548.2 J (Systems insight: A typical response of 500 tokens consumes ≈548.2 J.).
• Cho sự so sánh, việc sạc một điện thoại thông minh tiêu thụ ≈ 40000 J (For comparison, charging a smartphone consumes ≈40000 J).
• Việc đun sôi (Boiling) một cốc của nước tiêu thụ ≈ 100000 J (Boiling a cup of water consumes ≈100000 J).
Chính cách để giảm thiểu J/mã thông báo là để làm tăng phần cứng sự sử dụng và loại bỏ (eliminate) dư thừa
tính toán (The primary way to reduce J/token is to increase hardware utilization and eliminate redundant compute). Nếu GPU ngồi tại 10 phần trăm sự sử dụng do (bởi) kém việc tạo lô, (cái) nhàn rỗi công suất là vẫn
~300 W, việc gây ra năng lượng cho mỗi mã thông báo (để) tăng tới >3.3 J/mã thông báo (If the GPU sits at 10 percent utilization due to poor batching, the idle power is still ~300 W, causing the energy per token to rise to >3.3 J/token). Thuộc về kiến trúc các sự tối ưu hóa như
tiền tố việc lưu trong bộ nhớ đệm cũng bỏ qua (skip) chuyên sâu-năng lượng (energy-intensive) việc điền trước giai đoạn cho (được) chia sẻ ngữ cảnh, (một cách) trực tiếp việc giảm thiểu
năng lượng dấu chân của truy xuất-được tăng cường sự tạo sinh (RAG) và trò chuyện các ứng dụng (Architectural optimizations like prefix caching also skip the energy-intensive prefill phase for shared context, directly reducing the energy footprint of retrieval-augmented generation (RAG) and chat applications). Việc phục-
vụ bài học là rằng tính hiệu quả không phải chỉ (là) một độ trễ hay chi phí số liệu; nó cũng quyết định (làm thế nào)
nhiều năng lượng mỗi hữu ích mã thông báo tiêu thụ (The serving lesson is that efficiency is not only a latency or cost metric; it also determines how much energy each useful token consumes).

13. Mô hình Việc phục vụ
755
28
ONNX
Thời gian chạy (Runtime):
Microsoft’s sự suy luận công cụ (engine)
hoạt động như một phần cứng sự trừu tượng
lớp: (cái) giống nhau ONNX mô hình
chạy
trên
các CPU,
NVIDIA
các GPU, AMD các GPU, hay tùy chỉnh
các bộ tăng tốc
thông qua
có thể cắm-
vào (plug-gable) “sự thực thi các nhà cung cấp.”
ONNX
Thời gian chạy
áp dụng
không-biết-khuôn-khổ (framework-agnostic)
đồ thị
các sự tối ưu hóa—hằng số
việc gấp (folding),
dư thừa
nút
sự loại bỏ (elimination), toán tử (operator) sự hợp nhất (fusion)—
(những) thứ (mà) mang lại lợi ích (cho) tất cả các mục tiêu. Này
chéo-nền tảng (cross-platform)
khả năng
tránh việc duy trì riêng biệt
sự tối ưu hóa các đường ống (cho) mỗi
phần cứng mục tiêu, việc chấp nhận
một
5–15
phần trăm
thông-
lượng sự mất mát so với TensorRT cho
thị giác
các mô hình,
(được) bù đắp (offset)
bởi
khả năng (để) nhắm mục tiêu lại (retarget) (cái)
giống nhau .onnx đồ tạo tác qua
CPU/GPU/NPU
mà không có
sự biên dịch lại (recompilation)—một
tính linh hoạt
phần thưởng (premium) (thứ) mà quan trọng nhất trong
không đồng nhất (heterogeneous) thiết bị các hạm đội
nơi việc biên dịch lại mỗi-mục tiêu
được đo lường bằng các kỹ sư-các ngày (engineer-days).
29
TensorRT: Nó từ bỏ (abandons)
tính di động của chung-
mục đích các khuôn khổ bằng cách việc yêu-
cầu một xây dựng giai đoạn (thứ) mà tối-
ưu hóa mô hình cho một mục tiêu
GPU kiến trúc (ví dụ (for exam-ple), một H100) (NVIDIA 2024c).
Này phần cứng sự khóa-vào (lock-in) cho phép
tích cực các sự tối ưu hóa như
lớp sự hợp nhất và độ chính xác sự lựa-
chọn (thứ) mà (là) không an toàn cho một
khuôn khổ (thứ) mà phải chạy trên
bất kỳ phần cứng (nào).
(Cái) kết quả-
mang lại (result-ing) không thể di động công cụ có thể
(một cách) vật chất giảm thiểu độ trễ và
do đó số lượng của các GPU
(được) yêu cầu để đáp ứng một thông lượng
mục tiêu.
30
OpenVINO
(Mở (Open)
Thị giác Sự suy luận và Thần kinh
Mạng lưới
Sự tối ưu hóa):
Một định hướng-Intel (Intel-oriented) sự suy luận
bộ công cụ (toolkit)
(thứ) mà
chuyển đổi,
tối-
ưu hóa,
và chạy các mô hình
qua
Intel
CPU,
GPU,
và
NPU
các mục tiêu
(Intel
Tập đoàn (Corporation) 2026b).
Này
trực tiếp phần cứng việc nhắm mục tiêu là
một “tích cực” sự tối ưu hóa
bởi vì nó từ bỏ một số
tính di động (thứ) mà bản địa-khuôn-khổ
các thời gian chạy (run-times)
phải
đảm bảo (guarantee),
việc cho phép
nó
(để)
khai thác đặc thù-mục tiêu các hạt nhân (kernels)
và độ chính xác các sự lựa chọn.
(Cái)
kết quả mang lại hiệu suất lợi ích (gain)
là phụ thuộc-khối lượng công việc- và -phần cứng (workload- and hardware-dependent), nhưng nó có thể làm (cho)
dành riêng (dedicated) CPU hay (rìa) cạnh việc phục-
vụ (trở nên) (về mặt) kinh tế khả thi (viable) cho
nhỏ hơn và nhạy cảm-độ trễ
các mô hình.
Năng lượng tính hiệu quả phụ thuộc vào (những) giống nhau việc tạo lô, bộ nhớ, và tiền tố-bộ nhớ đệm các cơ chế (thứ) mà
chi phối LLM độ trễ, do đó (cái) hữu ích bản tóm tắt là một sự ép buộc danh sách kiểm tra (checklist) thay vì một đơn vô hướng (scalar)
số liệu (Energy efficiency depends on the same batching, memory, and prefix-cache mechanisms that govern LLM latency, so the useful summary is a constraint checklist rather than a single scalar metric).
Điểm kiểm tra 13.4: LLM việc phục vụ các nguyên tắc cơ bản
LLM việc phục vụ giới thiệu các sự ép buộc vắng mặt từ truyền thống mô hình việc phục vụ (LLM serving introduces constraints absent from traditional model serving).
□ TTFT so với TPOT: Bạn có thể giải thích tại sao hai các số liệu này nắm bắt khác biệt người dùng trải nghiệm
các khía cạnh (sự phản hồi (nhanh) so với tính trôi chảy) và tại sao chúng được chi phối bởi khác biệt phần cứng
các nút thắt cổ chai (tính toán so với bộ nhớ băng thông) (hay không)? (TTFT vs. TPOT: Can you explain why these two metrics capture different user experience aspects (responsiveness vs. fluidity) and why they are governed by different hardware bottlenecks (compute vs. memory bandwidth)?)
□ Bộ nhớ bức tường (wall): Bạn có thể giải thích tại sao việc thêm nhiều tính toán các lõi (hơn) mang lại (yields) không độ trễ
sự cải thiện cho mã thông báo sự tạo sinh, và tại sao chỉ nhanh hơn bộ nhớ hay nhỏ hơn các mô hình giúp ích (hay không)?
(Llama-3 tình huống (case) nghiên cứu trong phần 13.11.4 định lượng (quantifies) này mối quan hệ.) (Memory wall: Can you explain why adding more compute cores yields zero latency improvement for token generation, and why only faster memory or smaller models help? (The Llama-3 case study in section 13.11.4 quantifies this relationship.))
□ Liên tục việc tạo lô: Bạn có thể giải thích tại sao truyền thống tĩnh việc tạo lô lãng phí tính toán
khi chuỗi các chiều dài thay đổi, và cách mức-lặp lại (iteration-level) việc tạo lô giải quyết điều này (hay không)? (Continuous batching: Can you explain why traditional static batching wastes compute when sequence lengths vary, and how iteration-level batching solves this?)
□ PagedAttention: Bạn có thể giải thích bộ nhớ sự phân mảnh bài toán trong KV bộ nhớ đệm
sự quản lý và cách việc mượn ảo bộ nhớ các khái niệm từ HĐH thiết kế đạt được
gần-không (near-zero) sự lãng phí (hay không)? (PagedAttention: Can you explain the memory fragmentation problem in KV cache management and how borrowing virtual memory concepts from OS design achieves near-zero waste?)
□ Tiền tố việc lưu trong bộ nhớ đệm: Bạn có thể giải thích cách việc lưu trong bộ nhớ đệm KV các trạng thái của phổ biến hướng dẫn
các tiền tố giảm thiểu dư thừa tính toán và tăng tốc RAG hay nhiều-lượt các ứng dụng (hay không)? (Prefix caching: Can you explain how caching the KV states of common instruction prefixes reduces redundant computation and speeds up RAG or multi-turn applications?)
13.9 Sự suy luận Thời gian chạy (Runtime) Sự lựa chọn
Việc tạo lô các chiến lược và đặc thù-LLM các kỹ thuật quyết định cách các yêu cầu được nhóm và
(được) xử lý (The batching strategies and LLM-specific techniques determine how requests are grouped and processed). Những các chiến lược này giả định một cơ bản (underlying) sự thực thi công cụ (thứ) mà thực sự (actually) chạy mô hình
các tính toán—một giả định (thứ) mà quan trọng (một cách) to lớn (enormously) (These strategies assume an underlying execution engine that actually runs the model computations—an assumption that matters enormously). Mã thông báo sự tạo sinh mối quan hệ (được) chính-
thức hóa (formalized) sau đó trong chương này và độ trễ các ngân sách được thiết lập sớm hơn (chỉ) (có thể) đạt được nếu
thời gian chạy (một cách) hiệu quả ánh xạ các toán tử (operations) (tới) phần cứng (The token generation relationship for-malized later in this chapter and the latency budgets established earlier are achievable only if the runtime efficiently maps operations to hardware). Sự suy luận thời gian chạy, phần mềm lớp (thứ) mà
sắp xếp (orchestrates) tensor các toán tử và quản lý phần cứng các tài nguyên, có thể thay đổi bởi một thứ tự của độ lớn (magnitude)
trong hiệu suất cho giống hệt (identical) các mô hình (The inference runtime, the software layer that orchestrates tensor operations and manages hardware resources, can vary by an order of magnitude in performance for identical models). Thời gian chạy công việc do đó có hai các giai đoạn: sự lựa chọn chọn
sự thực thi công cụ, và cấu hình điều chỉnh (tunes) đó công cụ cho (cái) mục tiêu mô hình, phần cứng, và độ trễ
sự phân phối (Runtime work therefore has two phases: selection chooses the execution engine, and configuration tunes that engine for the target model, hardware, and latency distribution).
13.9.1 Thời gian chạy hệ sinh thái và cấu hình
Sự lựa chọn nên bắt đầu với (đang) ràng buộc sự ép buộc thay vì (cái) khuôn khổ được sử dụng trong suốt sự đào tạo (Selection should start with the binding constraint rather than the framework used during training).
Khi sự triển khai tốc độ và tính tương thích thống trị, PyTorch và TensorFlow các mô hình có thể phục vụ
(một cách) trực tiếp (việc) sử dụng của chúng bản địa (native) các thời gian chạy (When deployment speed and compatibility dominate, PyTorch and TensorFlow models can serve directly using their native runtimes). Này cách tiếp cận tối đa hóa tính tương thích (bất kỳ mô hình (nào) (thứ) mà đào tạo
sẽ phục vụ) và đơn giản hóa sự triển khai đường ống (không (cần) xuất hay sự chuyển đổi bước) (This approach maximizes compatibility (any model that trains will serve) and simplifies the deployment pipeline (no export or conversion step)). Khuôn khổ
các thời gian chạy bao gồm sự đào tạo tính năng (functionality) (thứ) mà thêm (vào) chi phí hoạt động, và mặc định sự thực thi các con đường có thể không
khai thác đặc thù-phần cứng các sự tối ưu hóa (Framework runtimes include training functionality that adds overhead, and default execution paths may not exploit hardware-specific optimizations).
TorchScript và TensorFlow SavedModel các định dạng (formats) kích hoạt biên dịch-trước (ahead-of-time) và đồ thị
sự tối ưu hóa, việc cải thiện (so với) háo hức (eager) sự thực thi trong khi (vẫn) việc duy trì khuôn khổ tính tương thích (TorchScript and TensorFlow SavedModel formats enable ahead-of-time compilation and graph optimization, improving over eager execution while maintaining framework compatibility). Những
các định dạng này đại diện (cho) (cái) đầu tiên bước về phía sự triển khai sự tối ưu hóa mà không có việc từ bỏ (cái) quen thuộc
khuôn khổ hệ sinh thái (These formats represent the first step toward deployment optimization without abandoning the familiar framework ecosystem).
13.9.1.1 Chung-mục đích sự tối ưu hóa
Khi tính di động qua phần cứng là (cái) (đang) ràng buộc sự ép buộc, ONNX Thời gian chạy28 cung cấp một phần cứng-
không-biết sự tối ưu hóa lớp (When portability across hardware is the binding constraint, ONNX Runtime28 provides a hardware-agnostic optimization layer (Microsoft 2024b)). Các mô hình (được) xuất tới ONNX định dạng, sau đó ONNX Thời gian chạy
áp dụng đồ thị các sự tối ưu hóa và chọn sự thực thi các nhà cung cấp cho (cái) mục tiêu phần cứng (Models export to ONNX format, then ONNX Runtime applies graph optimizations and selects execution providers for the target hardware). Điều này kích hoạt
đơn-định dạng sự triển khai qua các CPU, các GPU, và (được) chuyên môn hóa các bộ tăng tốc (This enables single-format deployment across CPUs, GPUs, and specialized accelerators).
13.9.1.2 Được chuyên môn hóa sự suy luận các công cụ
Khi độ trễ hay phần cứng chi phí ràng buộc (một cách) chặt chẽ (tightly) hơn (so với) tính di động, TensorRT29 (NVIDIA các GPU),

756
13.9 Sự suy luận Thời gian chạy Sự lựa chọn
31
Lớp Sự hợp nhất (Fusion):
Tương tự (Analo-gous)
(với) vòng lặp sự hợp nhất trong trình biên-
dịch (com-piler) sự tối ưu hóa, nơi liền kề
(ad-jacent) các vòng lặp qua giống nhau mảng
(ar-ray) được kết hợp để giảm thiểu
bộ nhớ lưu lượng truy cập.
Hạt nhân (Kernel) sự hợp-
nhất áp dụng (cái) giống hệt (identical) nguyên-
tắc (prin-ciple) cho GPU các toán tử (operations): tuần-
tự (se-quential) các hạt nhân (thứ) mà ghi
và đọc-lại trung gian các ten-
sor từ HBM được hợp nhất
thành một đơn hạt nhân (thứ) mà giữ
dữ liệu trong các thanh ghi (registers). Các khoản tiết kiệm
(savings) ghép (lại)—một điển hình ResNet-
50 có ~35 (có thể) hợp nhất toán-
tử (opera-tion) các cặp (pairs), và mỗi (được) loại-
bỏ (elimi-nated) HBM chuyến khứ hồi (round-trip) tiết kiệm
1–3 𝜇s tại 3.35 TB/s băng-
thông (band-width), việc chuyển đổi (các) bị giới hạn-bởi-
bộ nhớ các chuỗi thành bị giới hạn-bởi-
tính toán (compute-bound) được hợp nhất các hạt nhân.
OpenVINO30 (Intel phần cứng), và tương tự các công cụ tối ưu hóa (một cách) đặc thù cho của chúng mục tiêu phần cứng
(NVIDIA 2024c; Intel Tập đoàn 2026b; Chen và cộng sự 2018) (OpenVINO30 (Intel hardware), and similar engines optimize specifically for their target hardware (NVIDIA 2024c; Intel Corporation 2026b; Chen et al. 2018)). Chúng áp dụng tích cực các sự tối ưu hóa
(thứ) mà bản địa-khuôn-khổ các thời gian chạy không thể (một cách) an toàn thực hiện (They apply aggressive optimizations that framework-native runtimes cannot safely perform).
Lớp sự hợp nhất31 kết hợp nhiều tuần tự các toán tử thành một đơn GPU hạt nhân (Layer fusion31 combines multiple sequential operations into a single GPU kernel). Xem xét một
phổ biến mẫu: tích chập (convolution) → lô chuẩn hóa (batch normalization) → ReLU (rectified linear unit) sự kích hoạt (activation) (Consider a common pattern: convolution →batch normalization →rectified linear unit (ReLU) activation).
Không có sự hợp nhất, điều này yêu cầu ba hạt nhân các sự khởi chạy (launches), ba các chuyến khứ hồi tới GPU bộ nhớ (việc ghi tích chập
đầu ra, việc đọc cho chuẩn hóa lô, việc ghi chuẩn hóa lô đầu ra, việc đọc cho ReLU), và ba các tập hợp của trung gian
các tensor (Without fusion, this requires three kernel launches, three round-trips to GPU memory (write conv output, read for batchnorm, write batchnorm output, read for ReLU), and three sets of intermediate tensors). Sự hợp nhất kết hợp tất cả ba thành một hạt nhân (thứ) mà đọc các đầu vào một lần, tính toán (cái) được kết hợp
kết quả trong các thanh ghi, và ghi cuối cùng các đầu ra một lần (Fusion combines all three into one kernel that reads inputs once, computes the combined result in registers, and writes final outputs once). Điều này loại bỏ hạt nhân sự khởi chạy chi phí hoạt động (15–60 μs
(được) tiết kiệm (cho) mỗi sự hợp nhất) và giảm thiểu bộ nhớ lưu lượng truy cập bởi 2–3× (This eliminates kernel launch overhead (15–60 μs saved per fusion) and reduces memory traffic by 2–3×). TensorRT (một cách) tự động phát hiện và hợp nhất
phổ biến các mẫu; một điển hình ResNet-50 giảm thiểu từ ~50 các hạt nhân (xuống) ~15 sau sự hợp nhất (TensorRT automatically detects and fuses common patterns; a typical ResNet-50 reduces from ~50 kernels to ~15 after fusion).
Hạt nhân tự động-điều chỉnh (auto-tuning) chọn (cái) nhanh nhất thuật toán cho mỗi toán tử trên (cái) cụ thể GPU (Kernel auto-tuning selects the fastest algorithm for each operation on the specific GPU). Một đơn
tích chập có thể được triển khai (việc) sử dụng hàng chục (dozens) của các thuật toán như là trực tiếp (direct), nhanh Fourier biến đổi
(FFT) dựa-trên (based), Winograd, và đa dạng (việc) xếp gạch (tiling) các chiến lược, mỗi (cái) (là) tối ưu cho khác biệt đầu vào các kích thước và GPU
các kiến trúc (A single convolution can be implemented using dozens of algorithms such as direct, fast Fourier transform (FFT) based, Winograd, and various tiling strategies, each optimal for different input sizes and GPU architectures). Tự động-điều chỉnh (việc) chuẩn mực (benchmarks) mỗi ứng cử viên và lưu trong bộ nhớ đệm (cái) người chiến thắng (winner), việc đánh đổi biên dịch
thời gian (lấy) thời gian chạy hiệu suất (Auto-tuning benchmarks each candidate and caches the winner, trading compilation time for runtime performance).
Những các sự tối ưu hóa này điển hình đạt được 2–5× (sự) tăng tốc (speedup) (so với) bản địa-khuôn-khổ việc phục vụ nhưng yêu cầu
rõ ràng (sự) xuất và có thể không hỗ trợ tất cả các toán tử (These optimizations typically achieve 2–5× speedup over framework-native serving but require explicit export and may not support all operations). Một thời gian chạy sự so sánh trên một chuẩn (standard) mô hình
định lượng (quantifies) những lợi ích này qua (cái) sự tối ưu hóa quang phổ (spectrum) (A runtime comparison on a standard model quantifies these gains across the optimization spectrum).
Các hệ thống Góc nhìn 13.10: ResNet-50: Thời gian chạy sự so sánh
Bảng 13.19 so sánh ResNet-50 sự suy luận độ trễ và sự tăng tốc qua các thời gian chạy trên một V100 GPU
tại lô kích thước một (Table 13.19 compares ResNet-50 inference latency and speedup across runtimes on a V100 GPU at batch size one:):
Bảng 13.19: Sự suy luận thời gian chạy sự so sánh: Độ trễ và sự tăng tốc cho ResNet-50 (lô kích thước một) qua PyTorch háo hức,
TorchScript, ONNX Thời gian chạy, và TensorRT trong ba độ chính xác (precisions) trên một V100 (Table 13.19: Inference runtime comparison: Latency and speedup for ResNet-50 (batch size one) across PyTorch eager, TorchScript, ONNX Runtime, and TensorRT in three precisions on a V100). Mỗi bước (xuống) dưới (bảng) đổi (trades) tính di động cho
thô (raw) tốc độ, việc phơi bày (exposing) sự tối ưu hóa-tính tương thích sự đánh đổi (thứ) mà định nghĩa thời gian chạy sự lựa chọn (Each step down the table trades portability for raw speed, exposing the optimization-compatibility trade-off that defines runtime selection).
Thời gian chạy
Độ trễ
Sự tăng tốc
Các ghi chú
PyTorch (háo hức)
8.5 ms
1×
Cơ sở (Baseline), không (có) sự tối ưu hóa
TorchScript
6.2 ms
1.4×
JIT sự biên dịch
ONNX Thời gian chạy
5.1 ms
1.7×
Chéo-nền tảng
TensorRT FP32
2.8 ms
3×
Đặc thù-NVIDIA
TensorRT FP16
1.4 ms
6.1×
Tensor Lõi (Core) sự tăng tốc
TensorRT INT8
0.9 ms
9.4×
Yêu cầu sự hiệu chuẩn (calibration)
Các hệ thống sự thấu hiểu: (Cái) 9.4× (sự) tăng tốc từ TensorRT INT8 đến tại chi phí của: (1) sự lượng tử hóa
sự hiệu chuẩn dữ liệu, (2) tiềm năng (potential) độ chính xác (accuracy) sự mất mát (<1 phần trăm cho ResNet-50), và (3) đặc thù-NVIDIA
sự triển khai (Systems insight: The 9.4× speedup from TensorRT INT8 comes at the cost of: (1) quantization calibration data, (2) potential accuracy loss (<1 percent for ResNet-50), and (3) NVIDIA-specific deployment).
Sự tối ưu hóa-tính tương thích sự đánh đổi là vốn có (inherent). Tích cực hơn sự tối ưu hóa mang lại tốt hơn
hiệu suất tuy nhiên (làm) tăng (lên) sự triển khai tính phức tạp và có thể giới thiệu thuộc về số (numerical) các sự khác biệt từ
sự đào tạo (More aggressive optimization yields better performance yet increases deployment complexity and may introduce numerical differences from training). Sự lựa chọn phụ thuộc vào độ trễ các yêu cầu, sự triển khai các sự ép buộc, và (có) sẵn sàng
kỹ thuật các tài nguyên (The choice depends on latency requirements, deployment constraints, and available engineering resources).
Sau khi thời gian chạy được chọn, cấu hình áp dụng (cái) giống nhau sự ép buộc-đầu tiên (constraint-first) logic (After the runtime is chosen, configuration applies the same constraint-first logic). Luồng (Thread) hồ (pool)
việc định kích thước (sizing) kiểm soát tính song song cho CPU sự suy luận: quá ít các luồng để (lại) các lõi nhàn rỗi, trong khi quá nhiều gây ra
sự tranh chấp (contention) (Thread pool sizing controls parallelism for CPU inference: too few threads leave cores idle, while too many cause contention). Bộ nhớ sự cấp phát các chiến lược ((được) cấp phát trước các bộ đệm so với động sự cấp phát) đánh đổi khởi động
chi phí đối nghịch tính linh hoạt (Memory allocation strategies (preallocated buffers vs. dynamic allocation) trade startup cost against flexibility). Sự thực thi nhà cung cấp sự lựa chọn ưu tiên (những) phần cứng 백엔드 (backends) (nào) xử lý
mỗi toán tử, và đồ thị sự tối ưu hóa cấp độ đánh đổi sự biên dịch thời gian cho thời gian chạy hiệu suất (Execution provider selection prioritizes which hardware backends handle each operation, and graph optimization level trades compilation time for runtime performance).
Những các cài đặt này là không (phải) một riêng biệt danh sách kiểm tra sau sự lựa chọn; chúng là cách (cái) được chọn thời gian chạy được làm (cho)
thành thật (honest) dưới sản xuất lưu lượng truy cập (These settings are not a separate checklist after selection; they are how the selected runtime is made honest under production traffic). Sản xuất các sự triển khai do đó đo lường cấu hình tác động
trên độ trễ các sự phân phối thay vì (việc) dựa vào (các) mặc định (Production deployments therefore measure configuration impact on latency distributions rather than relying on defaults).

13. Mô hình Việc phục vụ
757
13.9.2 Độ chính xác (Precision) sự lựa chọn cho việc phục vụ
Một nhóm (đang) triển khai ResNet-50 trên V100 các GPU đối mặt một cụ thể sự ép buộc: của họ 30-GPU cụm (cluster) tốn
$90/giờ, và kinh doanh sự phát triển yêu cầu 3× nhiều (hơn) thông lượng mà không (cần) việc mở rộng hạm đội (A team deploying ResNet-50 on V100 GPUs faces a concrete constraint: their 30-GPU cluster costs $90/hour, and business growth requires 3× more throughput without expanding the fleet). Việc chuyển đổi
từ FP32 (sang) INT8 sự suy luận đạt được chính xác điều này—(cái) giống nhau mô hình trên (cái) giống nhau phần cứng phục vụ
3× nhiều (hơn) các yêu cầu mỗi giây, việc giảm thiểu hiệu quả chi phí cho mỗi sự suy luận bởi hai-phần ba, tại một chi phí của
ít hơn 0.4 phần trăm điểm của độ chính xác (Switching from FP32 to INT8 inference achieves exactly this—the same model on the same hardware serves 3× more requests per second, reducing the effective cost per inference by two-thirds, at a cost of less than 0.4 percentage points of accuracy). Ví dụ này minh họa (cái) trực tiếp mối kết nối giữa
thuộc về số độ chính xác và cơ sở hạ tầng tính kinh tế (This example illustrates the direct connection between numerical precision and infrastructure economics). Độ chính xác sự lựa chọn kết nối tới sự lượng tử hóa
các kỹ thuật được bao phủ trong phần 10.4 (Precision selection connects to the quantization techniques covered in section 10.4). Phần D.4 so sánh thuộc về số các định dạng (FP32, FP16, BF16,
FP8, INT8) và của chúng độ chính xác-phạm vi (precision-range) các sự đánh đổi, và phần D.4.2 chi tiết cơ chế của đối xứng (symmetric)
và bất đối xứng (asymmetric) số nguyên (integer) sự lượng tử hóa (Section D.4 compares the numerical formats (FP32, FP16, BF16, FP8, INT8) and their precision-range trade-offs, and section D.4.2 details the mechanics of symmetric and asymmetric integer quantization). Việc phục vụ thêm thời gian chạy các mối quan tâm như là sự hiệu chuẩn dữ liệu
(có) sẵn sàng (availability), lớp (sự) nhạy cảm (sensitivity) dưới sản xuất các đầu vào, và động độ chính xác sự lựa chọn (Serving adds runtime concerns such as calibration data availability, layer sensitivity under production inputs, and dynamic precision selection).
13.9.2.1 Độ chính xác-thông lượng mối quan hệ
Cho bị giới hạn-bởi-bộ nhớ-băng thông các toán tử, việc giảm thiểu độ chính xác (một cách) tương xứng (proportionally) (làm) tăng thông lượng
bằng cách việc giảm thiểu dữ liệu (sự) di chuyển (For memory-bandwidth-bound operations, reducing precision proportionally increases throughput by reducing data movement). Phương trình 13.16 định lượng (cái) thuộc về lý thuyết tối đa sự tăng tốc từ
độ chính xác sự giảm thiểu (Equation 13.16 quantifies the theoretical maximum speedup from precision reduction:):
ThroughputINT8
ThroughputFP32
= 32
8 = 4× (thuộc về lý thuyết tối đa (theoretical maximum))
(13.16)
Trong thực tế, GPU tính toán các đường ống và Tensor Lõi sự căn chỉnh (alignment) các hiệu ứng (effects) giới hạn (được) đạt được (sự) tăng tốc
tới 2.5–3.5× cho INT8 so với FP32 (In practice, GPU compute pipelines and Tensor Core alignment effects limit achieved speedup to 2.5–3.5× for INT8 vs. FP32). Tensor Lõi các hạt nhân là hiệu quả nhất khi ma trận các chiều (dimensions) (được)
căn chỉnh, như là INT8 các bội số (multiples) của 16 các phần tử và FP16 các bội số của 8 các phần tử trên nhiều các con đường (Tensor Core kernels are most efficient when matrix dimensions are aligned, such as INT8 multiples of 16 elements and FP16 multiples of 8 elements on many paths).
Hiện đại cuBLAS và cuDNN có thể vẫn sử dụng Tensor Các lõi cho nhiều khác các chiều, mặc dù thường
kém hiệu quả hơn hay với nội bộ việc đệm (padding) (Modern cuBLAS and cuDNN can still use Tensor Cores for many other dimensions, though often less efficiently or with internal padding). Chương 11 cung cấp (cái) chi tiết Tensor Lõi kiến trúc
(thứ) mà giải thích những sự căn chỉnh các sự ép buộc này (Chapter 11 provides the detailed Tensor Core architecture that explains these alignment constraints). Độ chính xác các sự đánh đổi cho một chuẩn thị giác mô hình
minh họa cách những thuộc về lý thuyết các giới hạn này biểu hiện (manifest) trong thực tế (The precision trade-offs for a standard vision model illustrate how these theoretical limits manifest in practice).
Các hệ thống Góc nhìn 13.11: ResNet-50: Độ chính xác các sự đánh đổi trên V100
Bảng 13.20 so sánh độ trễ, bộ nhớ, độ chính xác (accuracy), và Tensor Lõi sự sử dụng qua FP32, FP16,
và hai INT8 các con đường cho ResNet-50 (Table 13.20 compares latency, memory, accuracy, and Tensor Core utilization across FP32, FP16, and two INT8 paths for ResNet-50:):
Bảng 13.20: Độ chính xác các sự đánh đổi trên V100: Độ trễ, bộ nhớ dấu chân, độ chính xác, và Tensor Lõi sự sử dụng cho
ResNet-50 trong FP32, FP16, và INT8 (PTQ và QAT) (Table 13.20: Precision trade-offs on V100: Latency, memory footprint, accuracy, and Tensor Core utilization for ResNet-50 in FP32, FP16, and INT8 (PTQ and QAT)). FP16 là một gần-miễn phí (near-free) 2× sự tăng tốc (so với) FP32, trong khi INT8 đạt tới 3.1×
(so với) FP32 (1.6× vượt qua (beyond) FP16) tại chi phí của sự hiệu chuẩn dữ liệu và một phần nhỏ của một phần trăm điểm trong độ chính xác (FP16 is a near-free 2× speedup over FP32, while INT8 reaches 3.1× over FP32 (1.6× beyond FP16) at the cost of calibration data and a fraction of a percentage point in accuracy).
Độ chính xác
Độ trễ
Bộ nhớ
Độ chính xác (Accuracy)
Tensor Lõi Sử dụng. (Util.)
Sự hiệu chuẩn
FP32
2.8 ms
98 MB
76.13%
0%
Không
FP16
1.4 ms
49 MB
76.13%
85%
Không
INT8 (PTQ)
0.9 ms
25 MB
75.80%
92%
1,000 các mẫu (samples)
INT8 (QAT)
0.9 ms
25 MB
76.05%
92%
Đầy sự đào tạo lại
Các hệ thống sự thấu hiểu: INT8 đạt được 3.1× (sự) tăng tốc nhưng mất 0.33 phần trăm điểm của độ chính xác với
sau-sự đào tạo sự lượng tử hóa (PTQ) (Systems insight: INT8 achieves 3.1× speedup but loses 0.33 percentage points of accuracy with post-training quantization (PTQ)). Sự lượng tử hóa-nhận thức (aware) sự đào tạo (QAT) khôi phục hầu hết độ chính xác
nhưng yêu cầu sự đào tạo lại (Quantization-aware training (QAT) recovers most accuracy but requires retraining). FP16 cung cấp 2× (sự) tăng tốc với không độ chính xác sự mất mát cho hầu hết các mô hình (FP16 provides 2× speedup with no accuracy loss for most models).
13.9.2.2 Độ chính xác sự lựa chọn các sự ép buộc
Độ chính xác sự lựa chọn bị ép buộc bởi lớp sự nhạy cảm, sự hiệu chuẩn dữ liệu, và thời gian chạy chính sách (Precision selection is constrained by layer sensitivity, calibration data, and runtime policy). Không phải tất cả
các lớp chịu đựng (tolerate) được giảm thiểu độ chính xác (một cách) ngang bằng nhau (equally) (Not all layers tolerate reduced precision equally). (Một cách) theo kinh nghiệm, sự lượng tử hóa lỗi (error) cho một lớp mở rộng với trọng số
độ lớn (magnitude) và gradient (độ dốc) sự nhạy cảm, (được) nắm bắt bởi (cái) sau (đây) (sự) tỷ lệ thuận (proportionality) trong phương trình 13.17 (Empirically, quantization error for a layer scales with weight magnitude and gradient sensitivity, captured by the following proportionality in equation 13.17:):
𝜖quant ∝ 𝜅quant ⋅ ‖𝑊‖2 ⋅ 2−𝑏
(13.17)

13.10 Nút-Cấp độ Sự tối ưu hóa (Node-Level Optimization)
758
nơi 𝜅quant là một đặc thù-lớp sự nhạy cảm hệ số (coefficient) ((được) xác định (một cách) theo kinh nghiệm hay thông qua Fisher thông-
tin), ‖𝑊‖2 là trọng số L2 chuẩn (norm), và 𝑏 là bit độ rộng (where 𝜅quant is a layer-specific sensitivity coefficient (determined empirically or via Fisher informa-tion), ‖𝑊‖2 is the weight L2 norm, and 𝑏is the bit width). Điều này giải thích (được) quan sát các mẫu nơi
đầu tiên tích chập các lớp với cao các gradient và lớn sự nhạy cảm các hệ số là nhạy cảm-độ chính xác
và thường (được) giữ tại FP16, giữa các lớp với ổn định các gradient và thấp sự nhạy cảm các hệ số chịu đựng
INT8 (một cách) tốt, và cuối cùng sự phân loại các lớp với nhỏ các trọng số nhưng cao tác vụ (task) sự nhạy cảm hưởng lợi từ
FP16 hay cao hơn độ chính xác (This explains observed patterns where first convolutional layers with high gradients and large sensitivity coefficients are precision-sensitive and often kept at FP16, middle layers with stable gradients and low sensitivity coefficients tolerate INT8 well, and final classification layers with small weights but high task sensitivity benefit from FP16 or higher precision).
Sau-sự đào tạo sự lượng tử hóa thêm một dữ liệu sự ép buộc (Post-training quantization adds a data constraint). Sự hiệu chuẩn tập dữ liệu quyết định (các) tỷ lệ (scale)
các hệ số (factors) (được) sử dụng cho INT8 sự chuyển đổi, do đó nó phải đại diện (cho) thực tế việc phục vụ lưu lượng truy cập thay vì chỉ đơn thuần (merely) tái sử dụng
thuận tiện (convenient) sự đào tạo hay sự xác thực (validation) dữ liệu (The calibration dataset determines the scale factors used for INT8 conversion, so it must represent actual serving traffic rather than merely reuse convenient training or validation data). Một mô hình (được) hiệu chuẩn trên ImageNet-kiểu (style) sự xác thực các hình ảnh có thể
mất vài phần trăm các điểm khi (được) phục vụ trên hoang dã (wildlife) máy ảnh các hình ảnh với khác biệt (sự) chiếu sáng và
các nền (backgrounds), một sự thất bại chế độ (được) ghé thăm lại (revisited) trong phần 13.12 (A model calibrated on ImageNet-style validation images can lose several percentage points when served on wildlife camera images with different lighting and backgrounds, a failure mode revisited in section 13.12).
Nâng cao việc phục vụ các hệ thống biến độ chính xác thành một thời gian chạy chính sách (Advanced serving systems turn precision into a runtime policy). Nếu hệ thống là đi trước (ahead of) (của) nó
độ trễ SLO, nó có thể sử dụng cao hơn độ chính xác cho tốt hơn độ chính xác (accuracy) (If the system is ahead of its latency SLO, it can use higher precision for better accuracy). Cho thấp-sự tự tin (confidence) INT8 các kết quả, nó có thể
tính toán lại tại FP16 (For low-confidence INT8 results, it can recompute at FP16). Khác biệt khách hàng các bậc (tiers) có thể nhận khác biệt độ chính xác các cấp độ (Different customer tiers may receive different precision levels). Này mẫu
kích hoạt thích ứng chất lượng-độ trễ các sự đánh đổi trong khi tối đa hóa thông lượng trong suốt bình thường hoạt động (This pattern enables adaptive quality-latency trade-offs while maximizing throughput during normal operation).
Độ chính xác quyết định có trực tiếp cơ sở hạ tầng các hệ quả (consequences): INT8 sự suy luận đạt được xấp xỉ
3× cao hơn thông lượng (so với) FP32, (việc) có nghĩa (là) một khối lượng công việc (đang) yêu cầu 30 các GPU tại FP32 chỉ cần 10
tại INT8 (The precision decision has direct infrastructure consequences: INT8 inference achieves roughly 3× higher throughput than FP32, meaning a workload requiring 30 GPUs at FP32 needs only 10 at INT8). Này 3× sự giảm thiểu trong phần cứng chuyển đổi (translates) (một cách) trực tiếp (thành) một 3× sự giảm thiểu trong (đang) hoạt động các chi phí (This 3× reduction in hardware translates directly to a 3× reduction in operating costs).
Mối kết nối giữa mức-mô hình sự tối ưu hóa và cơ sở hạ tầng tính kinh tế là lý do tại sao độ chính xác
sự lựa chọn không thể được đối xử như (là) (một cách) hoàn toàn một mô hình mối quan tâm (The connection between model-level optimization and infrastructure economics is why precision selection cannot be treated as purely a model concern).
Thời gian chạy sự lựa chọn và độ chính xác sự điều chỉnh hoạt động tại mô hình cấp độ: chúng quyết định (những) gì tính-
toán chạy và tại (cái) gì thuộc về số định dạng (Runtime selection and precision tuning operate at the model level: they determine what computa-tion runs and at what numerical format). Giữa mô hình và silicon, tuy nhiên, nằm (lies) một khác
sự tối ưu hóa lớp bao quanh (encompassing) cơ chế của đồ thị sự biên dịch (thành) các hạt nhân, byte sự di chuyển
từ đĩa (tới) bộ nhớ, và CPU-GPU sự phối hợp (coordination) (Between the model and the silicon, however, lies another optimization layer encompassing the mechanics of graph compilation to kernels, byte movement from disk to memory, and CPU-GPU coordination). Những cấp độ-nút các kỹ thuật này thường mang lại (cái) cuối cùng
2–5× (thứ) mà phân tách một có chức năng nguyên mẫu từ một cấp độ-sản xuất việc phục vụ nút (These node-level techniques often yield the final 2–5× that separates a functional prototype from a production-grade serving node).
13.10 Cấp độ-Nút Sự tối ưu hóa
Xem xét một hình ảnh bộ phân loại (classifier) (thứ) mà (của) nó mô hình điểm chuẩn hứa hẹn (promises) mili giây sự suy luận nhưng (thứ) mà (của) nó
sản xuất dấu vết (trace) hiển thị một chậm hơn yêu cầu con đường (Consider an image classifier whose model benchmark promises millisecond inference but whose production trace shows a slower request path). Cấp độ-nút sự tối ưu hóa nhận diện (những) ranh giới nào
đang lãng phí thời gian trên đó máy (Node-level optimization identifies which boundary is wasting time on that machine). Dấu vết thường chỉ (points) (tới) một của bốn (đang) lặp lại (recurring) chẩn đoán (diagnostic)
các ranh giới (The trace usually points to one of four recurring diagnostic boundaries:):
• Đồ thị-tới-hạt nhân ranh giới: Tính toán đồ thị phải trở thành một nhỏ số lượng của hiệu quả
các hạt nhân thay vì một dài chuỗi của sự khởi chạy các chi phí hoạt động (Graph-to-kernel boundary: The computation graph has to become a small number of efficient kernels rather than a long sequence of launch overheads).
• CPU sự thực thi ranh giới: Phía-CPU công việc phải khai thác vectơ các đơn vị (units), tính cục bộ (locality), và thời gian chạy
các thư viện thay vì vô hướng (scalar) Python (CPU execution boundary: CPU-side work has to exploit vector units, locality, and runtime libraries rather than scalar Python).
• Tải ranh giới: Mô hình các byte phải di chuyển từ đĩa vào bộ nhớ đủ nhanh (rằng) lạnh các (sự) khởi động
không thống trị tăng-quy mô (scale-up) các sự kiện (Load boundary: Model bytes have to move from disk into memory fast enough that cold starts do not dominate scale-up events).
• Máy chủ-bộ tăng tốc ranh giới: Máy chủ phải giữ bộ tăng tốc (được) lên lịch mà không (có) các khoảng trống
(được) gây ra bởi việc tiền xử lý, các sự truyền (transfers), hay sự đồng bộ hóa (Host-accelerator boundary: The host has to keep the accelerator scheduled without gaps caused by preprocessing, transfers, or synchronization).
Đây là không (phải) độc lập các thủ thuật (tricks) (These are not independent tricks). Chúng là các vị trí (places) nơi một (được) đo lường dấu vết có thể giải thích tại sao một
yêu cầu con đường là chậm hơn (so với) mô hình điểm chuẩn đã hứa (They are places where a measured trace can explain why a request path is slower than the model benchmark promised).
13.10.1 Thời gian chạy đồ thị sự biên dịch
Sự suy luận các công cụ như TensorRT đã được giới thiệu trong phần 13.9 (Inference engines like TensorRT were introduced in section 13.9). Những các công cụ này đạt được 2–5×
các sự tăng tốc bởi vì việc phục vụ thay đổi trình biên dịch bài toán (These engines achieve 2–5× speedups because serving changes the compiler problem). Sự đào tạo tính toán các đồ thị là động
và có thể thay đổi (mutable), trong khi việc phục vụ các đồ thị là thường tĩnh (Training computation graphs are dynamic and mutable, whereas serving graphs are usually static). Một khi các hình dạng (shapes) và các toán tử (operators) (được) cố định,
trình biên dịch có thể tiêu (spend) thời gian-sự triển khai công việc để loại bỏ thời gian chạy công việc (Once shapes and operators are fixed, the compiler can spend deployment-time work to remove runtime work).
(Cái) đầu tiên lợi ích là toán tử sự hợp nhất, (cái) giống nhau hạt nhân-sự hợp nhất sự tối ưu hóa phần 13.9.1.2 đã áp dụng (cho)
TensorRT (The first gain is operator fusion, the same kernel-merging optimization section 13.9.1.2 applied to TensorRT). (Những) gì tĩnh việc phục vụ đồ thị thêm (vào) là khi (nào) sự hợp nhất xảy ra: bởi vì các toán tử và
các hình dạng (được) cố định trước khi bất kỳ yêu cầu (nào) đến, trình biên dịch có thể khám phá và cam kết (commit) (các) được hợp nhất các hạt nhân
sớm (trước) thay vì (việc) khám phá lại chúng tại thời gian chạy, do đó không yêu cầu (nào) trả cho sự phân tích (What the static serving graph adds is when the fusion happens: because operators and shapes are fixed before any request arrives, the compiler can discover and commit the fused kernels ahead of time rather than rediscovering them at runtime, so no request pays for the analysis).
(Cái) giống nhau tĩnh đồ thị cũng kích hoạt hằng số việc gấp (The same static graph also enables constant folding). Nếu một biểu thức con (subexpression) phụ thuộc chỉ vào (được) cố định
các trọng số hay các hằng số, như là x * (sqrt(2) / 2), trình biên dịch thay thế nó với (cái) được tính toán trước

13. Mô hình Việc phục vụ
759
32
SIMD (Đơn Lệnh (Instruction),
Nhiều Dữ liệu (Data)): Từ
Michael Flynn’s 1966 phân loại
học (taxon-omy) của máy tính các kiến-
trúc (architec-tures), SIMD kích hoạt một lệnh
(in-struction) (để) hoạt động trên nhiều
dữ liệu các phần tử (một cách) đồng
thời (simul-taneously).
Intel’s AVX-512
xử lý 512 các bit (16 các float)
(cho) mỗi lệnh;
AMX mở-
rộng (ex-tends) điều này (tới) ma trận ô (tile) các toán-
tử.
Cho CPU sự suy
luận, SIMD (sự) khai thác là
chính sự tối ưu hóa đòn bẩy:
ngây thơ vô hướng ma trận phép nhân
(multipli-cation) đạt được ~1 phần trăm của
thuộc về lý thuyết đỉnh, trong khi SIMD-
được tối ưu hóa các hạt nhân tiếp cận
80–90 phần trăm sự sử dụng—một
khoảng trống (thứ) mà quyết định liệu
chỉ-CPU việc phục vụ là (về mặt) kinh-
tế khả thi (hay không).
33
NUMA (Không-Đồng đều (Non-Uniform)
Bộ nhớ Truy cập (Access)): Việc truy cập
bộ nhớ cục bộ (với) một CPU socket
là nhanh hơn (so với) việc truy cập bộ nhớ
(được) đính kèm (với) một khác biệt
socket. Việc ghim (Pinning) một sự suy luận
luồng (tới) một lõi là không đủ
nếu (của) nó (được) yêu cầu bộ nhớ (được) cấp-
phát (một cách) từ xa (remotely), việc ép buộc mọi
trọng số truy cập qua
chậm hơn giữa-socket (inter-socket) liên kết. Này
sự thất bại (để) cùng-định vị (co-locate) các luồng
và dữ liệu áp đặt (imposes) một ~60 phần-
trăm độ trễ chi phí hoạt động, khi từ
xa truy cập tốn ~130 ns
so với ~80 ns cho cục bộ.
(Cái)
hình phạt (penalty) được ghép (compounded) cho
ML các khối lượng công việc bởi vì mô hình
các trọng số,
(những) thứ (mà) có thể dao động
từ hàng trăm của megabyte
tới gigabyte, vượt quá L3 bộ nhớ đệm
công suất (một cách) hoàn toàn—việc đảm bảo
rằng chéo-socket (cross-socket) các (sự) tìm nạp (fetches) xảy ra
trên mọi sự suy luận (đường) chuyền thay
vì chỉ trên bộ nhớ đệm các (sự) trượt (misses).
phép nhân x * 0.707.... (multiplication x * 0.707....) Điều này loại bỏ công việc từ mọi yêu cầu mà không (cần) (việc) thay đổi mô hình’s
toán học đầu ra (This removes work from every request without changing the model’s mathematical output).
Bộ nhớ việc lập kế hoạch áp dụng (cái) giống nhau ý tưởng (cho) sự cấp phát thay vì số học (Memory planning applies the same idea to allocation rather than arithmetic). Vì tensor
các vòng đời (lifetimes) (được) biết (đến), thời gian chạy có thể tính toán trước bộ nhớ các phần bù (offsets) và tái sử dụng các bộ đệm thay vì
việc cấp phát (một cách) phản ứng trong suốt yêu cầu (Since the tensor lifetimes are known, the runtime can precalculate memory offsets and reuse buffers instead of allocating reactively during the request). Kết quả là không phải chỉ (là) ít hơn các toán tử, nhưng một dễ đoán hơn
việc phục vụ con đường với ít hơn bộ cấp phát (allocator) (các sự) ngừng trệ (stalls) và ít hơn bộ nhớ sự phân mảnh (The result is not just fewer operations, but a more predictable serving path with fewer allocator stalls and less memory fragmentation).
Những các sự tối ưu hóa này dẫn tới một sự triển khai sự lựa chọn (These optimizations lead to a deployment choice). Đúng-lúc (Just-in-time) sự biên dịch thích ứng với các hình dạng
(được) quan sát tại thời gian chạy, nhưng (cái) đầu tiên yêu cầu trả (cho) sự biên dịch hình phạt (Just-in-time compilation adapts to the shapes observed at runtime, but the first request pays the compilation penalty). Biên dịch-trước (Ahead-of-time) sự biên dịch
loại bỏ đó khởi động đỉnh (nhọn) (spike) bằng cách (việc) vận chuyển (shipping) một (được) tối ưu hóa đồ tạo tác, nhưng sự triển khai phải (một cách) rõ ràng
bao phủ mọi hình dạng hồ sơ (thứ) mà dịch vụ sẽ chấp nhận (Ahead-of-time compilation removes that startup spike by shipping an optimized artifact, but the deployment must explicitly cover every shape profile the service will accept).
Các hệ thống Góc nhìn 13.12: Sự biên dịch thời gian (timing) sự đánh đổi
Đúng-lúc sự biên dịch chờ (đợi) cho đến khi đồ thị được (thực) thi (lần) đầu tiên và có thể chuyên môn hóa (specialize) (với) các hình dạng
nó quan sát (Just-in-time compilation waits until the graph is first executed and can specialize to the shapes it observes). Đó sự chuyên môn hóa là hữu ích cho có thể thay đổi lưu lượng truy cập, nhưng nó di chuyển trình biên dịch công việc vào
việc phục vụ con đường và tạo ra một lạnh-yêu cầu độ trễ đỉnh nhọn (That specialization is useful for variable traffic, but it moves compiler work into the serving path and creates a cold-request latency spike).
Biên dịch-trước sự biên dịch thực hiện trình biên dịch công việc trước (khi) sự triển khai (Ahead-of-time compilation performs the compiler work before deployment). Nó (mang) lại (cho) dịch vụ
một (được) cố định đồ thị và tránh khởi động sự biên dịch độ trễ, tại chi phí của việc định nghĩa tất cả động các hình dạng
(một cách) rõ ràng hay việc biên dịch nhiều hồ sơ (It gives the service a fixed graph and avoids startup compilation latency, at the cost of defining all dynamic shapes explicitly or compiling multiple profiles).
Các hệ thống sự lựa chọn là ở đâu (để) trả (cho) sự biên dịch chi phí: JIT trả nó trong việc phục vụ con đường và có nguy cơ (risks) một
đầu tiên-yêu cầu độ trễ đỉnh nhọn, trong khi AOT trả nó trước (khi) sự triển khai và yêu cầu chặt chẽ hơn (tự) kiểm soát
đối với đầu vào các hình dạng (The systems choice is where to pay compilation cost: JIT pays it in the serving path and risks a first-request latency spike, while AOT pays it before deployment and requires tighter control over input shapes).
13.10.2 CPU sự suy luận sự tối ưu hóa
JIT so với AOT sự lựa chọn chi phối GPU sự biên dịch chiến lược; CPU sự suy luận đối mặt (của) riêng nó sự tối ưu hóa
phong cảnh (landscape), nơi sự vectơ hóa (vectorization) và sự lượng tử hóa thay thế đồ thị sự biên dịch như (là) chính các đòn bẩy (The JIT vs. AOT choice governs GPU compilation strategy; CPU inference faces its own optimization landscape, where vectorization and quantization replace graph compilation as the primary levers).
Các GPU thống trị câu chuyện (narrative), tuy nhiên (yet) các CPU vẫn (là) (con) ngựa thồ (workhorse) cho nhiều sự suy luận các khối lượng công việc,
đặc biệt nhỏ các mô hình, không nhạy cảm-độ trễ lô các công việc, và bị ép buộc-chi phí các môi trường (GPUs dominate the narrative, yet CPUs remain the workhorse for many inference workloads, especially small models, latency-insensitive batch jobs, and cost-constrained environments). CPU
sự tối ưu hóa bắt đầu từ một khác biệt máy mô hình (CPU optimization starts from a different machine model). Hiện đại các CPU32 (Intel Xeon, AMD EPYC) chứa
vectơ các đơn vị như là AVX-512 và AMX, nhưng một vô hướng Python vòng lặp không thể sử dụng chúng (Modern CPUs32 (Intel Xeon, AMD EPYC) contain vector units such as AVX-512 and AMX, but a scalar Python loop cannot use them). (Được) chuyên môn hóa
các thời gian chạy như OpenVINO hay Intel Phần mở rộng cho PyTorch (IPEX) ánh xạ thần kinh mạng lưới các toán tử (một cách) trực tiếp
(tới) những vectơ các lệnh này, (một cách) đáng kể việc cải thiện hiệu suất (so với) ngây thơ vô hướng các sự triển khai
(Intel Tập đoàn 2026b) (Specialized runtimes like OpenVINO or Intel Extension for PyTorch (IPEX) map neural network operators directly to these vector instructions, substantially improving performance over naive scalar implementations (Intel Corporation 2026b)).
Tiếp theo CPU ranh giới là tính cục bộ (locality). Trên nhiều-socket các máy chủ33, việc truy cập bộ nhớ (được) đính kèm (với) một
khác biệt CPU socket (NUMA) thêm đáng kể độ trễ (The next CPU boundary is locality. On multi-socket servers33, accessing memory attached to a different CPU socket (NUMA) adds significant latency). Một sự suy luận máy chủ phải do đó (là) NUMA-
nhận thức (aware): các luồng nên được ghim (tới) cụ thể các lõi, và mô hình các trọng số và đầu vào các bộ đệm (những)
luồng đó chạm (vào) nên được cấp phát trên (cái) giống nhau socket (An inference server must therefore be NUMA-aware: threads should be pinned to specific cores, and the model weights and input buffers those threads touch should be allocated on the same socket). ML mô hình các trọng số—hàng trăm của megabyte
cho một tầm trung (mid-sized) mạng lưới, gigabyte cho một lớn ngôn ngữ mô hình—(một cách) đồ sộ vượt quá công suất của một
CPU’s L3 bộ nhớ đệm, do đó NUMA hình phạt là dai dẳng (persistent) thay vì thỉnh thoảng (occasional) (ML model weights—hundreds of megabytes for a mid-sized network, gigabytes for a large language model—massively exceed the capacity of a CPU’s L3 cache, so the NUMA penalty is persistent rather than occasional). Mọi sự suy luận đường chuyền
phải đọc (cái) đầy trọng số tensor; đang làm việc tập hợp (working set) không bao giờ khớp (vừa) trong bộ nhớ đệm, việc tạo ra (được) đảm bảo bộ nhớ đệm
(sự) đập (thrashing) và việc ép buộc (việc) không đổi tìm nạp (fetches) từ chính RAM qua chậm hơn giữa-socket liên kết (Every inference pass must read the full weight tensor; the working set never fits in cache, producing guaranteed cache thrashing and forcing constant fetches from main RAM across the slower inter-socket link).
Đây là lý do tại sao các CPU thường vượt trội (so với) các GPU tại lô kích thước một cho nhỏ các mô hình (This is why CPUs often outperform GPUs at batch size one for small models). Việc khởi chạy một GPU
hạt nhân (~10 𝜇s) và việc truyền (transferring) dữ liệu (~50 𝜇s) có thể vượt quá tính toán thời gian cho một bé xíu dày đặc (dense) lớp (Launching a GPU kernel (~10 𝜇s) and transferring data (~50 𝜇s) can exceed the compute time for a tiny dense layer).
Cho các mô hình (dưới) 50 MB (đang) phục vụ đơn các yêu cầu, một (được) tối ưu hóa-tốt CPU thời gian chạy có thể cung cấp thấp hơn
độ trễ (so với) một GPU bởi vì nó tránh (cái) bộ tăng tốc sự chuyển giao (handoff) (một cách) hoàn toàn (For models under 50 MB serving single requests, a well-optimized CPU runtime can deliver lower latency than a GPU because it avoids the accelerator handoff entirely).
13.10.3 Mô hình sự tuần tự hóa (serialization) và nhanh việc tải (loading)
Tự động mở rộng (Autoscaling) các hệ thống là (đang) hoạt động kiểm soát các vòng lặp (thứ) mà thêm hay xóa (bỏ) việc phục vụ các bản sao (được) dựa trên
tải (Autoscaling systems are operational control loops that add or remove serving replicas based on load). Trong những hệ thống đó, thời gian để quay lên (spin up) một mới nút là tới hạn (In those systems, the time to spin up a new node is critical). Một chính thành phần của “Lạnh
Sự khởi động” (phần 13.6.2) là (một cách) đơn giản việc đọc mô hình các trọng số từ đĩa vào bộ nhớ (A major component of “Cold Start” (section 13.6.2) is simply reading the model weights from disk into memory). Sự lựa chọn của
sự tuần tự hóa định dạng quyết định (như thế nào) (một cách) nhanh chóng này việc tải có thể xảy ra (The choice of serialization format determines how quickly this loading can occur).
Tiêu chuẩn PyTorch torch.load() sử dụng Python’s pickle định dạng (The standard PyTorch torch.load() uses Python’s pickle format). Này cách tiếp cận là kém hiệu quả
bởi vì nó yêu cầu CPU (để) hủy bỏ (unpickle) các đối tượng (từng) một (một), sao chép chúng vào bộ nhớ, và sau đó
thường sao chép chúng một lần nữa (tới) GPU (This approach is inefficient because it requires the CPU to unpickle objects one by one, copy them into memory, and then often copy them again to the GPU). (Cái) bộ nhớ việc ánh xạ (được) giới thiệu cho trên-yêu cầu (on-demand) việc tải trong

760
13.10 Nút-Cấp độ Sự tối ưu hóa
34
Safetensors: (Cái) tên
nhấn mạnh (emphasizes) an toàn (safety):
không giống như
Python’s
pickle
định dạng,
safetensors không thể thực thi
tùy ý mã trong suốt sự giải-tuần tự hóa
(deseri-alization), việc loại bỏ một lớp
của
bảo mật
các lỗ hổng (vulnerabilities)
nơi độc hại mô hình các tập tin
có thể làm tổn hại (compromise) một việc phục vụ
hệ thống (Hugging Face 2026).
Định dạng lưu trữ các tensor như
liền kề (raw) các byte với
một
tối thiểu
JSON
tiêu đề (header),
việc kích hoạt
được ánh xạ-bộ nhớ
việc tải; trong (cái) cục bộ ví dụ
bên trên, đó con đường là 10× nhanh hơn
(so với) pickle. Cho (việc) tự động mở rộng
việc phục vụ các hạm đội, này việc tải
tốc độ (một cách) trực tiếp giảm thiểu lạnh
(sự) khởi động độ trễ: sự khác biệt
giữa một tải (thứ) mà tốn
15 s và một (thứ) mà tốn 1.5
s quyết định liệu mới
các bản sao có thể hấp thụ lưu lượng truy cập
các đỉnh (nhọn)
trước khi
(các) SLO
bị
vi phạm (violated) (hay không).
phần 13.6.3 cung cấp một nhanh hơn con đường ở đây cho một khác biệt lý do: nếu (các) được tuần tự hóa các byte (đã) khớp (với) (cái)
trong-bộ nhớ tensor bố cục (layout), (được) ánh xạ tập tin cần không sự phân tích (cú pháp) (parsing) hay (sự) sao chép (nào) (tại tất cả) (section 13.6.3 offers a faster path here for a different reason: if the serialized bytes already match the in-memory tensor layout, the mapped file needs no parsing or copying at all).
(Việc) xây dựng trên này không-sao chép (zero-copy) nguyên tắc, Safetensors34 là một tensor định dạng (được) thiết kế (một cách) đặc thù cho nhanh
việc tải (Building on this zero-copy principle, Safetensors34 is a tensor format designed specifically for fast loading). Nó lưu trữ các tensor như (là) (các) thô các byte với một tối thiểu JSON tiêu đề (It stores tensors as raw bytes with a minimal JSON header). Điều này kích hoạt không-sao chép việc tải:
thô các byte trên đĩa được ánh xạ (một cách) trực tiếp vào (của) tensor bộ nhớ bộ đệm (this enables zero-copy loading: the raw bytes on disk are mapped directly into the tensor’s memory buffer).
Ví dụ 13.4: Việc tải tốc độ: Safetensors so với Pickle
Kịch bản: Một khởi động-lạnh bản sao phải tải một 5 GB Ổn định (Stable) Sự khuếch tán (Diffusion) v1.5 điểm kiểm tra trước khi nó có thể
hấp thụ lưu lượng truy cập (Scenario: A cold-start replica has to load a 5 GB Stable Diffusion v1.5 checkpoint before it can absorb traffic).
Sự phân tích:
• Pickle con đường: PyTorch dựa trên-pickle bộ tải (loader) tốn 15 s trong này kịch bản bởi vì Python
phải tái tạo (reconstruct) các đối tượng trước khi các tensor là (có thể) sử dụng (được) (Pickle path: The PyTorch pickle-based loader takes 15 s in this scenario because Python has to reconstruct objects before tensors are usable).
• Safetensors con đường: (Các) giống nhau các trọng số được lưu trữ với Safetensors tải trong 1.5 s, một 10× sự cải thiện
(ment) (Safetensors path: The same weights stored with Safetensors load in 1.5 s, a 10× improve-ment).
Các hệ thống sự thấu hiểu: Với (được) ánh xạ-bộ nhớ Safetensors các tập tin, việc tải tốc độ trở nên bị giới hạn
chủ yếu bởi đĩa’s (sự) đọc tốc độ—ví dụ 3.5 GB/s trên cục bộ Gen3 NVMe—thay vì bởi
CPU sự phân tích (cú pháp) chi phí hoạt động (Systems insight: With memory-mapped Safetensors files, loading speed becomes limited mainly by the disk’s read speed—for example 3.5 GB/s on local Gen3 NVMe—rather than by CPU parsing overhead).
13.10.4 Việc lập hồ sơ (Profiling) việc phục vụ nút
Sự tối ưu hóa mà không (có) (sự) đo lường là phỏng đoán (guesswork) (Optimization without measurement is guesswork). Hệ thống tính hiệu quả số liệu (được) định nghĩa trong phương-
trình 13.2 cung cấp mục tiêu: việc tối đa hóa (cái) phần (fraction) của đồng hồ-tường (wall-clock) thời gian bộ tăng tốc tiêu (dành) trên
hữu ích tính toán (The system efficiency metric defined in equa-tion 13.2 provides the target: maximizing the fraction of wall-clock time the accelerator spends on useful computation). Dòng thời gian việc lập hồ sơ các công cụ như PyTorch Profiler hay NVIDIA Nsight Systems (nsys)
làm (cho) đó mục tiêu (trở nên) (có thể) nhìn thấy (được) bằng cách (việc) cho thấy (cái) chính xác chuỗi của các sự kiện trên CPU và GPU (Timeline profiling tools like PyTorch Profiler or NVIDIA Nsight Systems (nsys) make that target visible by showing the exact sequence of events on the CPU and GPU).
Một hữu ích dấu vết sự đọc (reading) là nút-thắt-cổ-chai-đầu-tiên (A useful trace reading is bottleneck-first). Trống các không gian trong GPU thanh (bar) (có) nghĩa (là) nhàn rỗi phần cứng,
thường bởi vì GPU (đang) chờ (đợi) cho CPU việc tiền xử lý hay đĩa I/O (Empty spaces in the GPU bar mean idle hardware, usually because the GPU is waiting for CPU preprocessing or disk I/O). Hàng ngàn của nhỏ xíu GPU
các mảnh vụn (slivers) biểu thị (indicate) quá mức hạt nhân các sự khởi chạy và chỉ về phía toán tử sự hợp nhất hay đồ thị sự biên dịch (Thousands of tiny GPU slivers indicate excessive kernel launches and point toward operator fusion or graph compilation).
MemcpyHtoD các khối (blocks) phơi bày máy chủ-tới-thiết bị sự di chuyển; (cái) chẩn đoán câu hỏi là liệu những
các sự truyền đó (có) chồng chéo với tính toán hay (có) chặn (block) nó (hay không) (MemcpyHtoD blocks expose host-to-device movement; the diagnostic question is whether those transfers overlap with computation or block it). Dòng thời gian do đó chuyển đổi một mơ hồ (vague) lời phàn nàn (complaint)
về chậm việc phục vụ thành một cụ thể ranh giới trong yêu cầu con đường (The timeline therefore converts a vague complaint about slow serving into a concrete boundary in the request path).
Ví dụ 13.5: Việc lập hồ sơ vòng lặp
Kịch bản: Một việc phục vụ nút có cao P99 độ trễ mặc dù (even though) trung bình bộ tăng tốc sự sử dụng
trông có vẻ (có thể) chấp nhận (được), và một dấu vết của ấm (warm) các yêu cầu cho thấy lớn trống các khu vực (regions) trong (cái) bộ tăng tốc
dòng thời gian giữa ngắn các hạt nhân (Scenario: A serving node has high P99 latency even though average accelerator utilization looks acceptable, and a trace of warm requests shows large blank regions in the accelerator timeline between short kernels).
Cách tiếp cận:
1. Thiết lập: Chạy một (sự) làm ấm (warmup), sau đó chụp mười tới năm mươi (có tính) đại diện (representative) các yêu cầu trong Chrome Tracing,
Nsight, hay (cái) thời gian chạy’s bộ lập hồ sơ (profiler) (Setup: Run a warmup, then capture ten to fifty representative requests in Chrome Tracing, Nsight, or the runtime’s profiler).
2. Sự chẩn đoán: Tìm (cái) lớn nhất nhàn rỗi khoảng trống hay dài nhất (đang) chặn (blocking) sự kiện trong dấu vết (Diagnosis: Find the largest idle gap or longest blocking event in the trace).
3. Bản sửa lỗi (Fix): Áp dụng (cái) nhỏ nhất (được) nhắm mục tiêu (targeted) bản sửa lỗi, như là sự hợp nhất cho hạt nhân-sự khởi chạy sự phân mảnh,
việc ghim cho CPU tính cục bộ, không-sao chép việc tải cho sự khởi động, hay sự lập lịch các thay đổi cho máy chủ-
thiết bị các sự ngừng trệ (stalls) (Fix: Apply the smallest targeted fix, such as fusion for kernel-launch fragmentation, pinning for CPU locality, zero-copy loading for startup, or scheduling changes for host-device stalls).
4. Sự xác minh (Verification): Chụp dấu vết (một lần) nữa và xác nhận rằng (cái) (được) nhắm mục tiêu khoảng trống (đã) biến mất hay
di chuyển (Verification: Capture the trace again and confirm that the targeted gap disappeared or moved).
Các hệ thống bài học: Việc lập hồ sơ là đáng tin cậy (credible) chỉ khi (cái) tiếp theo dấu vết thay đổi trong (cái) (được) mong đợi hướng
(tion) (Systems lesson: Profiling is credible only when the next trace changes in the expected direc-tion). Vòng lặp ngăn chặn sự tối ưu hóa (khỏi) (việc) trở thành một danh sách của các thủ thuật bị tách rời (detached) từ (các) được đo lường
các nút thắt cổ chai (The loop prevents optimization from becoming a list of tricks detached from measured bottlenecks).
Bảng 13.21 là một quyết định (sự) hỗ trợ (aid) thay vì một danh sách kiểm tra: chọn kỹ thuật (thứ) mà (của) nó mục tiêu số liệu
khớp (với) (cái) được đo lường nút thắt cổ chai, không (phải) hàng với (cái) lớn nhất điển hình lợi ích (Table 13.21 is a decision aid rather than a checklist: choose the technique whose target metric matches the measured bottleneck, not the row with the largest typical gain).

13. Mô hình Việc phục vụ
761
Bảng 13.21: Cấp độ-Nút Sự tối ưu hóa Tác động (Impact): Một quyết định ma trận cho việc lựa chọn sự tối ưu hóa các kỹ thuật (Table 13.21: Node-Level Optimization Impact: A decision matrix for selecting optimization techniques). Cao-tác động
các kỹ thuật như sự lượng tử hóa thường mang (theo) cao hơn sự triển khai các chi phí (sự hiệu chuẩn dữ liệu các yêu cầu), trong khi thuộc về kiến trúc
các thay đổi như không-sao chép việc tải cung cấp ấn tượng (dramatic) các lợi ích cho cụ thể các số liệu (khởi động thời gian) với thấp nỗ lực (High-impact techniques like quantization often carry higher implementation costs (calibration data requirements), while architectural changes like zero-copy loading offer dramatic gains for specific metrics (startup time) with low effort).
Kỹ thuật
Mục tiêu Số liệu
Điển hình Lợi ích (Gain)
Sự triển khai Chi phí
Tốt nhất Cho
Toán tử Sự hợp nhất
Độ trễ & Thông lượng
2–5×
Trung bình (Trình biên dịch)
Bị giới hạn-bộ nhớ các lớp
INT8 Sự lượng tử hóa
Thông lượng
3–4×
Cao (Sự hiệu chuẩn)
Nặng-sự suy luận các nút
Đồ thị Sự biên dịch
Độ trễ
1.5–3×
Thấp (Một-dòng)
Tĩnh đồ thị các mô hình
Không-Sao chép Việc tải
Khởi động Thời gian
10–50×
Thấp (Tập tin định dạng)
Tự động mở rộng/Lạnh Sự khởi động
CPU Việc ghim (Pinning)
Đuôi Độ trễ (P99)
20-50% sự giảm thiểu
Thấp (Cấu hình)
Tới hạn-độ trễ các ứng dụng (apps)
Hệ thống phân cấp (hierarchy) của tác động này hướng dẫn (nơi) nào (để) đầu tư kỹ thuật nỗ lực (This hierarchy of impact guides where to invest engineering effort). Một (được) phân lớp (layered) điểm kiểm tra giữ
đó sự ưu tiên hóa (prioritization) (được) buộc (tied) (với) (cái) việc phục vụ ngăn xếp, từ yêu cầu sự vận chuyển xuống (tới) (được) hợp nhất các hạt nhân (A layered checkpoint keeps that prioritization tied to the serving stack, from request transport down to fused kernels).
Điểm kiểm tra 13.5: Sự tối ưu hóa hệ thống phân cấp
Việc tối ưu hóa sự suy luận theo (sau) (cái) yêu cầu con đường từ (bên) ngoài vào (trong) (Optimizing inference follows the request path from the outside in).
Ngăn xếp có bốn các cấp độ (The stack has four levels).
□Hệ thống cấp độ: (Bạn) Đã (từng) tối thiểu hóa mạng lưới vòng chuyến đi (round trips) và sự tuần tự hóa chi phí hoạt động (chưa)?
(gRPC, dai dẳng các kết nối) (System level: Have you minimized network round trips and serialization overhead? (gRPC, persistent connections)).
□Ứng dụng cấp độ: Bạn (có) đang lập lô (batching) các yêu cầu (một cách) hiệu quả? (Động việc lập lô) (Application level: Are you batching requests effectively? (Dynamic batching)).
□Mô hình cấp độ: (Có phải) mô hình (được) biên dịch cho mục tiêu phần cứng? (TensorRT, ONNX Thời gian chạy) (Model level: Is the model compiled for the target hardware? (TensorRT, ONNX Runtime)).
□Hạt nhân cấp độ: (Có phải) các toán tử (được) hợp nhất để tối thiểu hóa bộ nhớ băng thông? (Kernel level: Are operations fused to minimize memory bandwidth?)
Sự tối ưu hóa các kỹ thuật (được) kiểm tra (cho) đến nay (việc lập lô, thời gian chạy sự lựa chọn, độ chính xác sự điều chỉnh, đồ thị
sự biên dịch) (một cách) tập thể quyết định bao nhiêu hữu ích công việc một đơn việc phục vụ nút trích xuất (extracts) từ (của) nó
phần cứng (The optimization techniques examined so far (batching, runtime selection, precision tuning, graph compilation) collectively determine how much useful work a single serving node extracts from its hardware). (Cái) tiếp theo bước là (về mặt) kinh tế: việc quyết định bao nhiêu cơ sở hạ tầng được yêu cầu và tại (cái) gì
tổng chi phí (The next step is economic: determining how much infrastructure is required and at what total cost).
13.11 Tính kinh tế (Economics) và Việc lập kế hoạch
Mọi sự tối ưu hóa kỹ thuật (được) kiểm tra (cho) đến nay (việc lập lô, độ chính xác sự điều chỉnh, toán tử sự hợp nhất, đồ thị
sự biên dịch) giảm thiểu một đơn con số: chi phí của một sự suy luận trên một máy (Every optimization technique examined so far (batching, precision tuning, operator fusion, graph compilation) reduces a single number: the cost of one inference on one machine). Sản xuất
sự triển khai, tuy nhiên, yêu cầu (việc) trả lời một khác biệt câu hỏi: bao nhiêu (các) máy, của (loại) gì,
tại (cái) gì tổng chi phí (Production deployment, however, requires answering a different question: how many machines, of what type, at what total cost). Một đội (thứ) mà đạt được 1,200 (các) hình ảnh/giây trên một V100 vẫn cần (để) biết liệu
8 (các) V100 tại $3/giờ (cho) mỗi (cái) hay 24 (các) T4 tại $0.53/giờ (cho) mỗi (cái) mang lại thấp hơn tổng chi phí của quyền sở hữu cho (của) họ
5,000 QPS mục tiêu (hay không) (A team that achieves 1,200 images/second on a V100 still needs to know whether 8 V100s at $3/hour each or 24 T4s at $0.53/hour each yields lower total cost of ownership for their 5,000 QPS target). Việc phục vụ các chi phí mở rộng quy mô (scale) với yêu cầu khối lượng (volume), không giống như sự đào tạo các chi phí (thứ) mà mở rộng quy mô với
tập dữ liệu kích thước và mô hình độ phức tạp (Zhang et al. 2019) (Serving costs scale with request volume, unlike training costs that scale with dataset size and model complexity (Zhang et al. 2019)). (Cái) công khai API giá cả sự nén (compression) (được) hiển thị trong
hình 13.2 minh họa này áp lực: khi mỗi-token các mức giá (prices) giảm (fall), (cái) lề (margin) trên mỗi sự suy luận co lại (shrinks),
việc làm (cho) cơ sở hạ tầng tính hiệu quả (thành) một chính đòn bẩy cho (về mặt) kinh tế tính khả thi (viability) (The public API price compression shown in figure 13.2 illustrates this pressure: as per-token prices fall, the margin on each inference shrinks, making infrastructure efficiency a primary lever for economic viability).
13.11.1 Chi phí cho mỗi sự suy luận
Chi phí cho mỗi sự suy luận phân rã (decomposes) thành bốn thành phần: tính toán thời gian (GPU hay CPU các chu kỳ (được) tiêu thụ
cho mỗi sự suy luận), bộ nhớ (bộ tăng tốc bộ nhớ (được) yêu cầu để giữ mô hình các trọng số và các sự kích hoạt), dữ liệu
sự truyền (mạng lưới băng thông cho yêu cầu và phản hồi các tải trọng (payloads)), và sự điều phối (orchestration) chi phí hoạt động (bộ-
chứa thời gian chạy, tải việc cân bằng, và việc giám sát) (Cost per inference decomposes into four components: compute time (GPU or CPU cycles consumed per inference), memory (accelerator memory required to hold model weights and activations), data transfer (network bandwidth for request and response payloads), and orchestration overhead (con-tainer runtime, load balancing, and monitoring)). Cho GPU sự suy luận, (cái) thống trị chi phí thành phần
chuyển dịch (shifts) với sự sử dụng (For GPU inference, the dominant cost component shifts with utilization). Tại cao sự sử dụng, tính toán thời gian thống trị bởi vì GPU luôn (stays) bận rộn
việc xử lý các yêu cầu (At high utilization, compute time dominates because the GPU stays busy processing requests). Tại thấp sự sử dụng, bộ nhớ chi phí thống trị bởi vì GPU được dự trữ và
tính tiền (billed) (thậm chí) ngay cả khi nhàn rỗi (At low utilization, memory cost dominates because the GPU is reserved and billed even while idle). Này sự phân biệt có ý nghĩa (matters) cho chi phí sự tối ưu hóa: việc cải thiện thông lượng giảm thiểu
tính toán chi phí cho mỗi sự suy luận, trong khi việc cải thiện sự sử dụng giảm thiểu (cái) bộ nhớ sự lãng phí của nhàn rỗi phần cứng (This distinction matters for cost optimization: improving throughput reduces compute cost per inference, while improving utilization reduces the memory waste of idle hardware).
Việc áp dụng khuôn khổ (cho) ResNet-50 cho thấy (như thế nào) hàng giờ giá (cả) và (được) duy trì (sustained) thông lượng kết hợp
thành chi phí cho mỗi sự suy luận (Applying the framework to ResNet-50 shows how hourly price and sustained throughput combine into cost per inference).

762
13.11 Tính kinh tế và Việc lập kế hoạch
Khăn ăn Toán học 13.10: ResNet-50: Chi phí sự phân tích
Bảng 13.22 so sánh hàng giờ chi phí, thông lượng, và mỗi-triệu-hình ảnh chi phí cho việc phục vụ ResNet-50
trên AWS (US-East, trên-yêu cầu việc định giá (pricing) trong 2026) (Table 13.22 compares hourly cost, throughput, and per-million-image cost for serving ResNet-50 on AWS (US-East, on-demand pricing in 2026)):
Bảng 13.22: ResNet-50 đám mây sự suy luận chi phí sự so sánh: AWS hàng giờ chi phí, (được) duy trì thông lượng, và (cái) kết quả chi phí cho
một triệu các hình ảnh cho CPU, T4, và V100 các phiên bản (instances) trong này kịch bản, việc hiển thị (như thế nào) một cao hơn hàng giờ tỷ lệ (rate) có thể vẫn mang lại
thấp hơn chi phí cho mỗi sự suy luận khi thông lượng tăng đủ (Table 13.22: ResNet-50 cloud inference cost comparison: AWS hourly cost, sustained throughput, and resulting cost per one million images for CPU, T4, and V100 instances in this scenario, showing how a higher hourly rate can still yield lower cost per inference when throughput rises enough).
Phiên bản Loại
Chi phí/Giờ
Thông lượng
Chi phí cho mỗi 1M Các hình ảnh
c5.xlarge (CPU)
$0.17
50 img/s
$0.94
g4dn.xlarge (T4 GPU)
$0.53
400 img/s
$0.37
p3.2xlarge (V100 GPU)
$3.06
1,200 img/s
$0.71
Các hệ thống sự thấu hiểu: T4 GPU phiên bản đạt được (cái) thấp nhất chi phí cho mỗi sự suy luận mặc dù cao hơn
hàng giờ chi phí, bởi vì GPU thông lượng (một cách) ấn tượng vượt quá CPU thông lượng (Systems insight: The T4 GPU instance achieves the lowest cost per inference despite higher hourly cost, because GPU throughput dramatically exceeds CPU throughput). V100 là chỉ
hiệu quả-chi phí tại rất cao (được) duy trì lưu lượng truy cập nơi (của) nó cao hơn thông lượng biện minh (cho) 5.8× giá
sự gia tăng (The V100 is only cost-effective at very high sustained traffic where its higher throughput justifies the 5.8× price increase). Đám mây việc định giá dao động bởi khu vực và thay đổi qua thời gian; tham khảo hiện tại việc định giá cho
sản xuất việc lập kế hoạch (Cloud pricing varies by region and changes over time; consult current pricing for production planning).
13.11.2 GPU so với CPU tính kinh tế
Trong (được) làm (worked) AWS ví dụ bên trên, GPU các phiên bản tốn nhiều hơn cho mỗi giờ nhưng cung cấp nhiều cao hơn
song song thông lượng (In the worked AWS example above, GPU instances cost more per hour but deliver much higher parallel throughput). Điểm giao nhau (crossover point) phụ thuộc vào mô hình các đặc điểm và độ trễ các yêu cầu (The crossover point depends on model characteristics and latency requirements).
CPU sự suy luận có (về mặt) kinh tế ý nghĩa cho nhỏ các mô hình với ít các tham số và đơn giản các toán tử,
khi độ trễ các yêu cầu là (được) nới lỏng (hàng trăm của mili giây (có thể) chấp nhận (được)), khi yêu cầu khối lượng
là thấp hay (một cách) cao có thể thay đổi (việc làm (cho) GPU sự dự trữ lãng phí), hay khi mô hình’s các toán tử không
song song hóa tốt (CPU inference makes economic sense for small models with few parameters and simple operations, when latency requirements are relaxed (hundreds of milliseconds acceptable), when request volume is low or highly variable (making GPU reservation wasteful), or when the model’s operations do not parallelize well). GPU sự suy luận là hấp dẫn khi các mô hình là lớn với thân thiện-song song các toán tử,
độ trễ các yêu cầu là nghiêm ngặt (strict) (hàng chục của mili giây), yêu cầu khối lượng là cao và nhất quán đủ
để duy trì sự sử dụng, và việc lập lô có thể khấu hao (cái) cho mỗi-sự suy luận chi phí hoạt động của GPU hạt nhân các sự khởi chạy (GPU inference is attractive when models are large with parallel-friendly operations, latency requirements are strict (tens of milliseconds), request volume is high and consistent enough to sustain utilization, and batching can amortize the per-inference overhead of GPU kernel launches).
Bên ngoài ổn định-trạng thái các chi phí, khởi động thời gian ảnh hưởng (tới) (việc) mở rộng quy mô tính kinh tế (Beyond steady-state costs, startup time affects scaling economics). CPU các phiên bản (một cách) điển hình khởi động trong
30–60 giây trong khi GPU các phiên bản tốn 2–5 phút bao gồm trình điều khiển sự khởi tạo, mô hình việc tải,
và (sự) làm ấm (CPU instances typically start in 30–60 seconds while GPU instances take 2–5 minutes including driver initialization, model loading, and warmup). Cho có thể thay đổi lưu lượng truy cập các mẫu, này khởi động độ trễ có thể (là) quan trọng hơn (so với) chi phí cho mỗi
sự suy luận (For variable traffic patterns, this startup latency can be more important than cost per inference). Nếu lưu lượng truy cập các đỉnh (nhọn) đến nhanh hơn (so với) GPU các phiên bản có thể mở rộng quy mô, độ trễ (các) SLO sẽ bị vi phạm
mặc dù (việc) có đủ cuối cùng (eventual) công suất (If traffic spikes arrive faster than GPU instances can scale, latency SLOs will be violated despite having sufficient eventual capacity).
Này sự bất đối xứng (asymmetry) gợi ý khác biệt việc mở rộng quy mô các chiến lược nơi CPU các phiên bản kích hoạt (có tính) phản ứng (việc) mở rộng quy mô
bằng cách (việc) phản hồi (tới) hiện tại nhu cầu trong khi GPU các phiên bản thường yêu cầu (có tính) dự đoán (việc) mở rộng quy mô bằng cách (việc) dự liệu (provision-ing) (được) dựa trên (được) dự đoán trước nhu cầu (This asymmetry suggests different scaling strategies where CPU instances enable reactive scaling by responding to current demand while GPU instances often require predictive scaling by provision-ing based on anticipated demand). Cho có tính bùng nổ (bursty) các khối lượng công việc, một lai cách tiếp cận sử dụng luôn-bật GPU
công suất cho cơ sở (baseline) tải cộng CPU tràn (overflow) công suất cho các đỉnh (nhọn), (việc) đánh đổi cao hơn mỗi-sự suy luận chi phí
trong suốt các đỉnh (nhọn) cho tốt hơn sự phản hồi (responsiveness) (For bursty workloads, a hybrid approach uses always-on GPU capacity for baseline load plus CPU overflow capacity for spikes, trading higher per-inference cost during spikes for better responsiveness). Này GPU+CPU lai là một phiên bản (instance) của (cái) rộng hơn lai
kiến trúc các mẫu (được) lập danh mục (cataloged) trong phần 2.10, nơi đào tạo-phục vụ sự chia tách và (có tính) phân cấp (hierarchical) (việc) xử lý
các mẫu cũng kết hợp các mô hình để cân bằng chi phí, độ trễ, và khả năng (This GPU+CPU hybrid is one instance of the broader hybrid architecture patterns cataloged in section 2.10, where the train-serve split and hierarchical processing patterns also combine paradigms to balance cost, latency, and capability).
13.11.3 Công suất việc lập kế hoạch
GPU so với CPU quyết định thiết lập (cái) chi phí cho mỗi sự suy luận, nhưng (việc) quyết định bao nhiêu cơ sở hạ-
tầng để dự liệu (provision) yêu cầu (việc) kết hợp chi phí sự phân tích với hàng đợi lý thuyết các nền tảng từ
phần 13.5 (The GPU vs. CPU decision establishes the cost per inference, but determining how much infras-tructure to provision requires combining cost analysis with the queuing theory foundations from section 13.5). Công suất việc lập kế hoạch chuyển đổi (translates) ba (các) đầu vào thành cơ sở hạ tầng các đặc tả: lưu lượng truy cập
các mẫu (đỉnh yêu cầu tỷ lệ, hàng ngày/hàng tuần các chu kỳ, sự tăng trưởng các sự dự phóng (projections)), độ trễ (các) SLO (p50, p95, p99
các mục tiêu), và mô hình các đặc điểm (sự suy luận thời gian sự phân phối tại đa dạng lô các kích thước) (Harchol-Balter
2013) (Capacity planning translates three inputs into infrastructure specifications: traffic patterns (peak request rate, daily/weekly cycles, growth projections), latency SLOs (p50, p95, p99 targets), and model characteristics (inference time distribution at various batch sizes) (Harchol-Balter 2013)).
(Cái) (được) làm ví dụ trong phần 13.5 minh họa (cái) hoàn chỉnh quy trình làm việc: (việc) bắt đầu từ một 50 ms
p99 SLO và 5,000 QPS mục tiêu, (việc) suy ra (deriving) (cái) thận trọng M/M/1 an toàn sự sử dụng ngưỡng của 54
phần trăm từ phương trình 13.6, và (việc) quyết định GPU số lượng với khoảng trống (headroom) của 12 (các) V100 (The worked example in section 13.5 demonstrates the complete workflow: starting from a 50 ms p99 SLO and 5,000 QPS target, deriving the conservative M/M/1 safe utilization threshold of 54 percent from equation 13.6, and determining GPU count with headroom of 12 V100s). Sản xuất
các hệ thống (một cách) điển hình dự liệu cho đỉnh tải cộng 30 phần trăm khoảng trống, (việc) sử dụng sự tự động mở rộng để giảm thiểu các chi phí
trong suốt thấp-lưu lượng truy cập các khoảng thời gian (periods) trong khi (việc) đáp ứng độ trễ các mục tiêu trong suốt các đỉnh (nhọn); Chương 14 phát triển (cái)
(đang) hoạt động chính sách lớp xung quanh những việc phục vụ các tính toán này (Production systems typically provision for peak load plus 30 percent headroom, using autoscaling to reduce costs during low-traffic periods while meeting latency objectives during peaks; Chapter 14 develops the operational policy layer around these serving calculations). (Cái) chính sự thấu hiểu từ công suất việc lập kế hoạch
là (rằng) thông lượng các con số là (có) ý nghĩa chỉ khi (được) ghép nối với độ trễ các sự đảm bảo: như
hợp lệ-QPS việc kế toán (accounting) trong phần 13.5 (đã) thiết lập, công suất phải được định kích thước cho các yêu cầu (thứ) mà (một cách) thực sự
đáp ứng (cái) SLO, không (phải) cho thô yêu cầu khối lượng (The key insight from capacity planning is that throughput numbers are meaningful only when coupled with latency guarantees: as the valid-QPS accounting in section 13.5 established, capacity must be sized for requests that actually meet the SLO, not for raw request volume).
13.11.4 Sản xuất trường hợp nghiên cứu: Việc phục vụ 8-tỷ-tham số Llama 3
(Cái) thống trị chi phí trong (việc) phục vụ một lớn ngôn ngữ mô hình là không (phải) tính toán mà (là) KV-bộ đệm bộ nhớ, và
hình 13.7 cho thấy tại sao (The dominant cost in serving a large language model is not compute but KV-cache memory, and figure 13.7 shows why). (Được) vẽ (Plotted) tại 70-tỷ-tham số quy mô để khuếch đại (cái) hiệu ứng, (cái) bộ đệm tăng trưởng
(một cách) tuyến tính với ngữ cảnh độ dài và lô kích thước cho đến khi dài các ngữ cảnh đẩy (thậm chí) ngay cả một H100 vào (của) nó Hết-
Bộ nhớ (out-of-memory) vùng (Plotted at 70-billion-parameter scale to amplify the effect, the cache grows linearly with context length and batch size until long contexts push even an H100 into its out-of-memory zone). (Cái) 8-tỷ-tham số Llama 3 hồ sơ (được) phân tích trong (cái) phần còn lại của này phần tuân theo (obeys)
(cái) giống nhau vật lý (physics) với nhiều hơn khoảng trống, (việc) làm nó (thành) một khối lượng công việc một kỹ sư có thể vừa vặn trên một GPU và
lý luận về cuối (tới) cuối (The 8-billion-parameter Llama 3 profile analyzed in the rest of this section obeys the same physics with more headroom, making it a workload an engineer can fit on one GPU and reason about end to end).
Hình 13.7: (Cái) KV-Bộ đệm Sự bùng nổ: Bộ nhớ sự sử dụng so với Ngữ cảnh Độ dài cho một 70-tỷ-tham số-lớp mô hình (Figure 13.7: The KV-Cache Explosion: Memory usage vs. Context Length for a 70-billion-parameter-class model). Giả định 80
các lớp, 𝑑model = 8192, FP16 KV bộ đệm, GQA (8×) (Assumes 80 layers, 𝑑model = 8192, FP16 KV cache, GQA (8×)). (Cái) tuyến tính sự tăng trưởng của (Cái) Khóa-Giá trị bộ đệm (việc lưu trữ sự chú ý lịch sử) (một cách) nhanh chóng
tiêu thụ (có) sẵn GPU bộ nhớ (đỏ nét đứt (dashed) đường) (The linear growth of the Key-Value cache (storing attention history) quickly consumes available GPU memory (red dashed line)). Cho lô kích thước 32 (tím), hệ thống chạm (vào) ‘OOM Vùng’ tại chỉ 8k ngữ cảnh
độ dài, (việc) ép buộc một sự đánh đổi giữa lô kích thước (thông lượng) và ngữ cảnh cửa sổ (khả năng) (For batch size 32 (purple), the system hits the ‘OOM Zone’ at just 8k context length, forcing a trade-off between batch size (throughput) and context window (capability)).
(Cái) tuyến tính sự tăng trưởng của (cái) KV bộ đệm với chuỗi độ dài ép buộc một cứng sự đánh đổi: để hỗ trợ dài hơn
các ngữ cảnh (32k+), chúng ta phải giảm thiểu lô kích thước, (điều) mà (đến) lượt (nó) (in turn) giết chết thông lượng tính hiệu quả (The linear growth of the KV cache with sequence length forces a hard trade-off: to support longer contexts (32k+), we must reduce batch size, which in turn kills throughput efficiency).
13.11.4.1 Khối lượng công việc hồ sơ
(Các) (được) cố định khối lượng công việc các giả định bên dưới định nghĩa (cái) tham chiếu trường hợp (được) sử dụng xuyên suốt độ trễ,
bộ nhớ, và tính kinh tế các tính toán trong này phần; (cùng) với nhau, chúng giới hạn (bound) (các) sự phân tích (thứ) mà theo (sau) (The fixed workload assumptions below define the reference case used throughout the latency, memory, and economics calculations in this section; together, they bound the analyses that follow).
• Mô hình: 8-tỷ-tham số Llama 3 ((được) lượng tử hóa thành 4-bit (việc) sử dụng nhận thức-sự kích hoạt trọng số sự lượng-
tử hóa (AWQ); xem Chương 10 cho sự lượng tử hóa các kỹ thuật) (Dubey et al. 2024; Lin et al.
2023) (Model: 8-billion-parameter Llama 3 (quantized to 4-bit using activation-aware weight quan-tization (AWQ); see Chapter 10 for quantization techniques) (Dubey et al. 2024; Lin et al. 2023)).
• Phần cứng: 1× NVIDIA H100 SXM5 GPU (80 GB HBM3, 3.35 TB/s băng thông) (Choquette
2023) (Hardware: 1× NVIDIA H100 SXM5 GPU (80 GB HBM3, 3.35 TB/s bandwidth) (Choquette 2023)).
• Yêu cầu các đặc điểm: 1,000-token đầu vào lời nhắc (Tiền điền), 256-token (được) tạo ra phản hồi
(Giải mã) (Request characteristics: 1,000-token input prompt (Prefill), 256-token generated response (Decode)).
• Mục tiêu (các) SLO: TTFT < 200 ms, TPOT < 20 ms.
Những các giả định này làm (cho) (cái) trường hợp nghiên cứu hẹp đủ để tính toán trong khi (việc) bảo tồn hai
việc phục vụ các sự ép buộc (thứ) mà có ý nghĩa (matter) nhất: (cái) tiền điền ngân sách (budget) cho thời gian (tới) (cái) đầu tiên token và (cái) giải mã ngân sách
cho mỗi (được) tạo ra token (These assumptions make the case study narrow enough to calculate while preserving the two serving constraints that matter most: the prefill budget for time to first token and the decode budget for each generated token).

764
13.11 Tính kinh tế và Việc lập kế hoạch
13.11.4.2 Độ trễ sự tháo dỡ (deconstruction)
(Cái) cuối-tới-cuối yêu cầu độ trễ được chi phối bởi (cái) hai-giai đoạn sự thực thi mô hình của (có tính) tự hồi quy
các transformer, (việc) áp dụng TTFT và TPOT các số liệu (được) định nghĩa trong phần 13.8.1 (The end-to-end request latency is governed by the two-phase execution model of autoregressive transformers, applying the TTFT and TPOT metrics defined in section 13.8.1). Tiền điền quyết định
liệu người dùng thấy một lời nhắc phản hồi (một cách) nhanh chóng (hay không); giải mã quyết định liệu (cái) (được) tạo ra luồng (stream)
tiếp tục (keeps) di chuyển sau khi nó bắt đầu (hay không) (Prefill determines whether the user sees a prompt response quickly; decode determines whether the generated stream keeps moving after it starts).
Tiền điền giai đoạn (thời gian tới đầu tiên token) Mô hình xử lý (cái) 1,000-token lời nhắc (một cách) song song (Prefill phase (time to first token) The model processes the 1,000-token prompt in parallel). Trong này
kịch bản, (cái) H100 tiền điền tỷ lệ được đặt thành xấp xỉ 10,000 (các) token/s: 𝑇prefill = 1000 (các) token ÷ 10,000
(các) token/s = 100 ms (In this scenario, the H100 prefill rate is set to approximately 10,000 tokens/s: 𝑇prefill = 1000 tokens ÷ 10,000 tokens/s = 100 ms). (Việc) tính toán (Accounting) cho 20 ms của hệ thống chi phí hoạt động (mạng lưới (sự) xâm nhập (ingress), sự token hóa), (cái)
TTFT là 120 ms, (một cách) thoải mái bên trong (cái) 200 ms SLO (Accounting for 20 ms of system overhead (network ingress, tokenization), the TTFT is 120 ms, comfortably within the 200 ms SLO).
Giải mã giai đoạn (thời gian cho mỗi đầu ra token) Mô hình tạo ra 256 các token (một cách) tuần tự (Decode phase (time per output token) The model generates 256 tokens sequentially). Này giai đoạn là
bị giới hạn-bộ nhớ-băng thông—(cái) giống nhau bị giới hạn-IO mẫu (được) thấy trong (cái) DLRM nhúng các (sự) tra cứu (lookups)
(phần 13.4.2), nhưng tại một lớn hơn quy mô: hệ thống phải đọc (cái) toàn bộ 3.5 GB trọng số tensor từ
VRAM để tạo ra một đơn token (This phase is memory-bandwidth bound—the same IO-bound pattern seen in the DLRM embedding lookups (section 13.4.2), but at a larger scale: the system must read the entire 3.5 GB weight tensor from VRAM to generate a single token).
Các hệ thống Góc nhìn 13.13: (Cái) vật lý (physics) của token sự tạo ra
Nhớ lại (cái) năng lượng-sự di chuyển bất biến (invariant) (được) định lượng (quantified) trong bảng 4.1: (việc) di chuyển một bit là 100–1,000× nhiều hơn
đắt đỏ (so với) (việc) tính toán trên nó (Recall the energy-movement invariant quantified in table 4.1: moving a bit is 100–1,000× more expensive than computing on it). Trong (Cái) Giải mã Giai đoạn, này định luật quyết định (cái) thuộc về vật lý “chi phí cho mỗi
từ” (In the Decode Phase, this law determines the physical “cost per word”).
Vật lý: Bởi vì (cái) giải mã giai đoạn có một số học (arithmetic) cường độ của ≈1 FLOP/byte (chúng ta phải đọc
mọi trọng số chỉ để tạo ra một token), hiệu suất (bị) (một cách) nghiêm ngặt (strictly) giới hạn bởi bộ nhớ băng thông
(BW), không (phải) tính toán (Physics: Because the decode phase has an arithmetic intensity of ≈1 FLOP/byte (we must read every weight just to generate one token), performance is strictly limited by memory bandwidth (BW), not compute). Này mối quan hệ được nắm bắt (captured) trong phương trình 13.18 (This relationship is captured in equation 13.18):
𝑇token ≈
𝐷vol
BWmemory
(13.18)
Hệ quả (Implication): Mọi token sự tạo ra trả một đồ sộ (massive) “năng lượng thuế (tax)” để di chuyển mô hình’s logic
từ HBM vào tính toán các thanh ghi (registers) (Implication: Every token generation pays a massive “energy tax” to move the model’s logic from HBM into compute registers). Cho sự so sánh, trên một A100 80 GB (2.04 TB/s HBM2e), một
8-tỷ-tham số Llama 3 mô hình (4.1 GB INT4) tạo ra các token tại ≈2.0 ms cho mỗi token (For comparison, on an A100 80 GB (2.04 TB/s HBM2e), an 8-billion-parameter Llama 3 model (4.1 GB INT4) generates tokens at ≈2.0 ms per token). Khi
giải mã vẫn (bị) giới hạn-băng thông, (việc) thêm nhiều hơn tính toán các lõi mang lại (rất) ít độ trễ sự cải thiện;
nhanh hơn bộ nhớ (Vật lý), nhỏ hơn các mô hình (Thuật toán), hay tốt hơn việc lập lô và bộ đệm (sự) quản lý
thay đổi (cái) giới hạn (When decode remains bandwidth-bound, adding more compute cores yields little latency improvement; faster memory (Physics), smaller models (Algorithm), or better batching and cache management change the bound).
Việc đọc (cái) 4.1 GB trọng số tensor tại 3.35 TB/s thiết lập (cái) thuộc về lý thuyết sàn (floor): 𝑇token ≈1.2 ms (Reading the 4.1 GB weight tensor at 3.35 TB/s sets the theoretical floor: 𝑇token ≈1.2 ms). Việc tính toán
cho hạt nhân sự khởi chạy chi phí hoạt động, sự chú ý tính toán, và một thận trọng (conservative) sản xuất an toàn lề (margin),
(cái) (được) hiện thực hóa (realized) 𝑇token là xấp xỉ 1.53 ms (Accounting for kernel launch overhead, attention computation, and a conservative production safety margin, the realized 𝑇token is approximately 1.53 ms). Việc tạo ra tất cả 256 (các) token do đó tốn 256 (các) token ×
1.53 ms = 0.39 s, và (cái) kết quả TPOT của 1.53 ms ngồi (sits) tốt bên trong (cái) 20 ms “tính trôi chảy (fluidity)” SLO (Generating all 256 tokens therefore takes 256 tokens × 1.53 ms = 0.39 s, and the resulting TPOT of 1.53 ms sits well within the 20 ms “fluidity” SLO).
13.11.4.3 Bộ nhớ và thông lượng
Với 4-bit các trọng số (đang) chiếm giữ (occupying) 4.1 GB, (cái) (phần) còn lại ~75 GB là có sẵn cho (cái) KV Bộ đệm, (thứ) mà
PagedAttention cấp phát với gần-không sự phân mảnh (With 4-bit weights occupying 4.1 GB, the remaining ~75 GB is available for the KV Cache, which PagedAttention allocates with near-zero fragmentation). Mỗi token yêu cầu xấp xỉ 0.033 MB
của INT4 KV bộ đệm trong (cái) 8-tỷ-tham số Llama 3 cấu hình, vì (Được) Nhóm Truy vấn Sự chú ý (Grouped Query Attention)
giảm thiểu KV-đầu (head) lưu trữ so với (relative to) đầy (đủ) nhiều-đầu sự chú ý tại FP16 (Each token requires approximately 0.033 MB of INT4 KV cache in the 8-billion-parameter Llama 3 configuration, since Grouped Query Attention reduces KV-head storage relative to full multi-head attention at FP16). Việc chia (cái) 72 GB của bộ đệm
bởi đó mỗi-token chi phí mang lại công suất cho ≈2.2 triệu (các) token, do đó tại 1,256 (các) token GPU có thể giữ một
đồng thời lô kích thước của ~1749 (các) yêu cầu (Dividing the 72 GB of cache by that per-token cost yields capacity for ≈2.2 million tokens, so at 1,256 tokens the GPU can hold a concurrent batch size of ~1749 requests).
13.11.4.4 Đơn vị tính kinh tế
Xem xét một (có tính) đại diện H100 SXM5 (tiền) thuê (rental) chi phí của xấp xỉ $3/giờ (Consider a representative H100 SXM5 rental cost of approximately $3/hour). Bị giới hạn-tiền điền (các) sự tiếp-
nhận (admissions) (đi) đến (come to) 10,000 (các) token/s (được) chia bởi 1,000 (các) token = 10 req/s (Prefill-limited admissions come to 10,000 tokens/s divided by 1,000 tokens = 10 req/s). Điều này là bên dưới (cái) KV-sự cư trú (residency)
giới hạn của 1749 (các) yêu cầu / 0.44 s ≈3931 req/s, do đó đầy-yêu cầu thông lượng là 10 req/s × 3,600 s/hr ×
1,256 (các) token ≈45.2 triệu (các) token/giờ (This is below the KV-residency limit of 1749 requests / 0.44 s ≈3931 req/s, so full-request throughput is 10 req/s × 3,600 s/hr × 1,256 tokens ≈45.2 million tokens/hour). Việc chia (cái) hàng giờ chi phí bởi đó thông lượng (mang) lại một chi phí
cho mỗi triệu (các) token của $3/giờ / 45.2 triệu (các) token/giờ ≈$0.066/triệu (các) token (Dividing the hourly cost by that throughput gives a cost per million tokens of $3/hour / 45.2 million tokens/hour ≈$0.066/million tokens).
Sự phân tích này làm nổi bật rằng cho các LLM, bộ nhớ công suất (kích thước của KV bộ đệm) quyết định (cái)
tối đa đồng thời sự cư trú (residency), trong khi tiền điền tính toán và giải mã băng thông quyết định (cái) (được) hiện thực hóa (This analysis highlights that for LLMs, memory capacity (the size of the KV cache) determines the maximum concurrent residency, while prefill compute and decode bandwidth determine realized)

13. Mô hình Việc phục vụ
765
token thông lượng và chi phí dưới một cụ thể lưu lượng truy cập (sự) kết hợp (mix) (token throughput and cost under a specific traffic mix). Bộ nhớ băng thông vẫn (là) (cái) chính
yếu tố quyết định (determinant) của giải mã độ trễ (Memory bandwidth remains the primary determinant of decode latency).
Này trường hợp nghiên cứu áp dụng (các) cốt lõi (core) các nguyên tắc (được) phát triển xuyên suốt này chương: độ trễ các ngân sách
phân rã thành tiền điền và giải mã các giai đoạn, hàng đợi lý thuyết chi phối lô việc định kích thước và công suất
việc lập kế hoạch, và phần cứng các sự ép buộc trong (cái) hình thức của bộ nhớ băng thông và công suất quyết định
có thể đạt được hiệu suất và chi phí (This case study applies the core principles developed throughout this chapter: latency budgets decompose into prefill and decode phases, queuing theory governs batch sizing and capacity planning, and hardware constraints in the form of memory bandwidth and capacity determine achievable performance and cost). (Cái) định lượng (quantitative) khuôn khổ (được) thiết lập ở đây kích hoạt có nguyên tắc
kỹ thuật các quyết định, nhưng chỉ khi (được) áp dụng (một cách) chính xác (The quantitative framework established here enables principled engineering decisions, but only when applied correctly). Phổ biến các sự ngộ nhận (misconceptions) khiến (thậm chí) ngay cả
giàu kinh nghiệm các kỹ sư (việc) áp dụng sai (misapply) những các nguyên tắc này trong thực tế (Common misconceptions cause even experienced engineers to misapply these principles in practice).
13.12 Các ngụy biện (Fallacies) và Các cạm bẫy (Pitfalls)
Việc phục vụ đảo ngược (inverts) đào tạo các sự ưu tiên trong các cách (thứ) mà vi phạm các trực giác (intuitions) từ lô việc xử lý (Serving inverts training priorities in ways that violate intuitions from batch processing). (Cái) phi tuyến
mối quan hệ giữa sự sử dụng và độ trễ, (những) ẩn các chi phí của việc tiền xử lý, và (các) im lặng sự thất bại
các chế độ của đào tạo-phục vụ sự sai lệch (skew) gây ra (các) bị vi phạm (các) SLO, lãng phí sự tối ưu hóa nỗ lực, và độ chính xác (accuracy)
sự xuống cấp (degradation) vô hình (invisible) (với) tiêu chuẩn việc giám sát (The nonlinear relationship between utilization and latency, the hidden costs of preprocessing, and the silent failure modes of training-serving skew cause violated SLOs, wasted optimization effort, and accuracy degradation invisible to standard monitoring).
Ngụy biện: Việc giảm thiểu mô hình sự suy luận độ trễ (một cách) theo tỷ lệ (proportionally) giảm thiểu người dùng-nhận thức (user-perceived) độ trễ (Fallacy: Reducing model inference latency proportionally reduces user-perceived latency).
Các kỹ sư (những) người tối ưu hóa mô hình sự suy luận mong đợi (sự) theo tỷ lệ sự cải thiện trong người dùng-nhận thức
độ trễ, nhưng việc phục vụ các hệ thống giới thiệu độ trễ các nguồn vắng mặt từ ngoại tuyến các điểm chuẩn (Engineers who optimize model inference expect proportional improvement in user-perceived latency, but serving systems introduce latency sources absent from offline benchmarks). Dưới tải,
hàng đợi sự chậm trễ (delay) thống trị: phương trình 13.5 cho thấy rằng tại 80 phần trăm sự sử dụng với 5 ms dịch vụ thời gian,
trung bình chờ (đợi) thời gian là 20 ms (thậm chí) trước khi sự suy luận bắt đầu (Under load, queuing delay dominates: equation 13.5 shows that at 80 percent utilization with 5 ms service time, average wait time is 20 ms before inference even begins). Việc giảm thiểu sự suy luận từ 5 ms xuống 2 ms
thay đổi dịch vụ thời gian nhưng cũng dịch chuyển sự sử dụng từ 80 phần trăm xuống 32 phần trăm, (việc) giảm thiểu việc xếp hàng đợi
chờ (đợi) từ 20 ms xuống 0.9 ms, một 21.2× việc xếp hàng đợi sự cải thiện (thứ) mà làm lùn đi (dwarfs) (cái) 3 ms sự suy luận lợi ích (Reducing inference from 5 ms to 2 ms changes service time but also shifts utilization from 80 percent to 32 percent, reducing queuing wait from 20 ms to 0.9 ms, a 21.2× queuing improvement that dwarfs the 3 ms inference gain). Này
phi tuyến sự tương tác giữa sự suy luận tốc độ và việc xếp hàng đợi hành vi (có) nghĩa (là) (cái) cấp độ-hệ thống sự tăng tốc
(25 ms →2.9 ms, hay 8.5×) (một cách) xa vượt qua (cái) cấp độ-mô hình sự tăng tốc (5 ms →2 ms, hay 2.5×) (This nonlinear interaction between inference speed and queuing behavior means the system-level speedup (25 ms →2.9 ms, or 8.5×) far exceeds the model-level speedup (5 ms →2 ms, or 2.5×)). Ngược lại, các đội
(những) người giảm thiểu sự suy luận bởi chỉ 20 phần trăm tại cao sự sử dụng thấy không đáng kể (negligible) đối mặt-người dùng sự cải thiện
bởi vì việc xếp hàng đợi vẫn thống trị (Conversely, teams that reduce inference by only 20 percent at high utilization see negligible user-facing improvement because queuing still dominates). Việc phục vụ sự tối ưu hóa yêu cầu (việc) phân tích (cái) hoàn chỉnh độ trễ
ngân sách, bao gồm sự tuần tự hóa, việc xếp hàng đợi, việc tiền xử lý, và việc hậu xử lý, dưới thực tế tải
các điều kiện thay vì (việc) lập hồ sơ (profiling) sự suy luận độ trễ trong (sự) cô lập (isolation) (Serving optimization requires analyzing the complete latency budget, including serialization, queuing, preprocessing, and postprocessing, under realistic load conditions rather than profiling inference latency in isolation).
Cạm bẫy: Việc chạy việc phục vụ cơ sở hạ tầng tại cao sự sử dụng để tối đa hóa chi phí tính hiệu quả (Pitfall: Running serving infrastructure at high utilization to maximize cost efficiency).
Các đội nhắm mục tiêu (target) 90 phần trăm sự sử dụng để tối thiểu hóa nhàn rỗi công suất (Teams target 90 percent utilization to minimize idle capacity). Trong sản xuất, độ trễ xuống cấp (degrades)
(một cách) phi tuyến khi sự sử dụng tiếp cận công suất (In production, latency degrades nonlinearly as utilization approaches capacity). Phương trình 13.5 cho thấy rằng tại 90 phần trăm sự sử dụng,
trung bình thời gian trong hệ thống đạt (đến) 10× dịch vụ thời gian (Equation 13.5 shows that at 90 percent utilization, average time in system reaches 10× service time). Việc di chuyển từ 70 phần trăm (tới) 90 phần trăm sự sử dụng
cắt giảm cơ sở hạ tầng các chi phí bởi 22.2 phần trăm nhưng (nhân) ba (triples) trung bình độ trễ (Moving from 70 percent to 90 percent utilization cuts infrastructure costs by 22.2 percent but triples average latency). Cho một 5 ms sự suy luận dịch vụ, p99
độ trễ nhảy từ ~76.7 ms (tới) ~230 ms (M/M/1 mô hình) (For a 5 ms inference service, p99 latency jumps from ~76.7 ms to ~230 ms (M/M/1 model)). Các hệ thống (được) dự liệu cho trung bình tải
vi phạm (các) SLO (một cách) chính xác khi lưu lượng truy cập gia tăng trong suốt tới hạn-doanh nghiệp các khoảng thời gian (Systems provisioned for average load violate SLOs precisely when traffic increases during business-critical periods). Sản xuất các hệ thống
nhắm mục tiêu 60 tới 70 phần trăm sự sử dụng tại đỉnh tải duy trì (cái) độ trễ khoảng trống (cần) thiết để hấp thụ
lưu lượng truy cập các đỉnh (nhọn) (Production systems targeting 60 to 70 percent utilization at peak load maintain the latency headroom needed to absorb traffic spikes).
Ngụy biện: Đào tạo độ chính xác đảm bảo (guarantees) việc phục vụ độ chính xác (Fallacy: Training accuracy guarantees serving accuracy).
Các kỹ sư giả định (các) giống hệt (identical) mô hình các trọng số bảo tồn (preserve) (tập hợp) xác thực (set) hiệu suất (Engineers assume identical model weights preserve validation set performance). Trong sản xuất,
việc tiền xử lý các sự khác biệt (một cách) im lặng dịch chuyển các đầu vào (ra) ngoài đào tạo sự phân phối (In production, preprocessing differences silently shift inputs outside the training distribution). Phần 13.6.1 cho thấy
(như thế nào) đào tạo-phục vụ sự sai lệch (skew) gây ra độ chính xác sự xuống cấp mặc dù giống hệt các trọng số: PIL so với OpenCV
đổi kích thước sự nội suy (interpolation) đơn độc có thể dịch chuyển độ chính xác bởi 0.5–1 phần trăm các điểm, FP64 so với FP32 sự chuẩn hóa
sản xuất khác biệt các giá trị, hay đặc trưng tính toán thời gian thay đổi (Section 13.6.1 shows how training-serving skew causes accuracy degradation despite identical weights: PIL vs. OpenCV resize interpolation alone can shift accuracy by 0.5–1 percentage points, FP64 vs. FP32 normalization produces different values, or feature computation timing changes). Một mô hình (đang) đạt được 95 phần trăm
sự xác thực độ chính xác rớt (drops) (xuống) 90 phần trăm trong sản xuất từ những việc tiền xử lý (các) sự không khớp (mismatches) này, một 5
phần trăm-điểm (sự) mất mát vô hình (đối với) độ trễ việc giám sát (A model achieving 95 percent validation accuracy drops to 90 percent in production from these preprocessing mismatches, a 5 percentage-point loss invisible to latency monitoring). Tiêu chuẩn việc giám sát việc kiểm tra các ngoại lệ và
độ trễ các sự vi phạm (violations) thất bại (trong việc) phát hiện này im lặng sự xuống cấp (Standard monitoring checking exceptions and latency violations fails to detect this silent degradation). Sản xuất các hệ thống yêu cầu (hoặc là) giống hệt
việc tiền xử lý mã (code) cho sự đào tạo và việc phục vụ, hay (có tính) thống kê việc giám sát việc so sánh đầu vào các sự phân phối
để bắt (sự) trôi dạt (drift) trước khi độ chính xác xuống cấp (Production systems require either identical preprocessing code for training and serving, or statistical monitoring comparing input distributions to catch drift before accuracy degrades).
Cạm bẫy: Việc sử dụng trung bình độ trễ để đánh giá (evaluate) việc phục vụ hệ thống hiệu suất (Pitfall: Using average latency to evaluate serving system performance).
Các kỹ sư giám sát trung bình độ trễ bởi vì nó (có) xu hướng (trends) trơn tru và là đơn giản để tính toán (Engineers monitor average latency because it trends smoothly and is simple to compute). Trong
sản xuất, các (số) trung bình (averages) che giấu chậm nhất các yêu cầu (thứ) mà quyết định người dùng sự hài lòng (satisfaction) (In production, averages hide the slowest requests that determine user satisfaction). Như phần 13.5.5
minh họa, tại 70 phần trăm sự sử dụng với 5 ms dịch vụ thời gian, trung bình độ trễ là 16.7 ms nhưng p99
đạt (đến) 76.7 ms, một 4.6× khoảng trống vô hình (đối với) dựa trên-trung bình việc giám sát (As section 13.5.5 demonstrates, at 70 percent utilization with 5 ms service time, average latency is 16.7 ms but p99 reaches 76.7 ms, a 4.6× gap invisible to mean-based monitoring). Các đội (đang) tối ưu hóa trung bình độ trễ
bỏ lỡ (miss) (cái) đuôi (tail) (thứ) mà quyết định người dùng sự hài lòng: (cái) 1 phần trăm của những người dùng (đang) trải nghiệm 76.7 ms các sự chậm trễ
thường tạo ra (những) (có) giá trị nhất các giao dịch (transactions) (Teams optimizing average latency miss the tail that determines user satisfaction: the 1 percent of users experiencing 76.7 ms delays often generate the most valuable transactions). Sản xuất (các) SLO chỉ định (specify) (phần) bách phân (percentile) các mục tiêu (p95, p99)
(một cách) chính xác bởi vì các (số) trung bình che đậy (mask) đuôi hành vi (Production SLOs specify percentile targets (p95, p99) precisely because averages mask tail behavior).

766
13.13 Tóm tắt
Ngụy biện: Lớn hơn việc phục vụ các lô luôn luôn cải thiện thông lượng mà không (làm) ảnh hưởng độ trễ (các) SLO (Fallacy: Larger serving batches always improve throughput without affecting latency SLOs).
Các kỹ sư tối đa hóa lô kích thước (việc) giả định GPU sự bão hòa (saturation) cải thiện chi phí tính hiệu quả dưới sản xuất
tải (Engineers maximize batch size assuming GPU saturation improves cost efficiency under produc-tion load). Trong việc phục vụ các hệ thống, tuy nhiên, việc lập lô giới thiệu một độ trễ-thông lượng sự đánh đổi (được) chi phối
bởi việc xếp hàng đợi (các) động lực (dynamics) vắng mặt từ ngoại tuyến các điểm chuẩn (In serving systems, however, batching introduces a latency-throughput trade-off governed by queuing dynamics absent from offline benchmarks). Việc tích lũy (Accumulating) các yêu cầu thành lớn hơn các lô
gia tăng chờ (đợi) thời gian cho (những) sớm (những) người đến (arrivals): một lô cửa sổ của 10 ms có nghĩa (là) (cái) đầu tiên yêu cầu chờ (đợi) 10
ms trước khi sự suy luận bắt đầu, (một cách) trực tiếp thêm vào p99 độ trễ (Accumulating requests into larger batches increases wait time for early arrivals: a batch window of 10 ms means the first request waits 10 ms before inference begins, directly adding to p99 latency). Trong (cái) (có tính) đại diện ResNet-50/V100
kịch bản (được) sử dụng (sớm) hơn (earlier), việc gia tăng lô kích thước từ 16 lên 32 cải thiện thông lượng chỉ 12 phần trăm nhưng
gần như nhân đôi mỗi-lô sự suy luận thời gian từ 14 ms lên 25 ms, và có thể thay đổi đầu vào các kích thước bên trong một
lô có thể tạo ra việc đệm (padding) chi phí hoạt động (thứ) mà lãng phí tính toán trên (việc) đệm các token (In the representative ResNet-50/V100 scenario used earlier, increasing batch size from 16 to 32 improves throughput only 12 percent but nearly doubles per-batch inference time from 14 ms to 25 ms, and variable input sizes within a batch can create padding overhead that wastes compute on padding tokens). Phần 13.7.3 cho thấy
tại sao, cho chặt chẽ (tight) p99 các mục tiêu, lớn hơn lô các kích thước có thể vi phạm (các) SLO khi lô sự hình thành sự chậm trễ cộng
(việc) được gia tăng mỗi-lô sự suy luận thời gian vượt qua (cái) độ trễ ngân sách (Section 13.7.3 shows why, for tight p99 targets, larger batch sizes can violate SLOs when batch formation delay plus increased per-batch inference time exceeds the latency budget). Việc phục vụ lô sự tối ưu hóa yêu cầu
(một cách) chung (jointly) việc điều chỉnh lô kích thước, lô (sự) hết thời gian, và tính đồng thời chống lại độ trễ (các) SLO dưới thực tế lưu lượng truy cập
các mẫu, không (phải) (việc) tối đa hóa thông lượng trong sự cô lập (Serving batch optimization requires jointly tuning batch size, batch timeout, and concurrency against latency SLOs under realistic traffic patterns, not maximizing throughput in isolation).
Cạm bẫy: Việc hiệu chuẩn (được) lượng tử hóa các mô hình với đào tạo dữ liệu thay vì sản xuất lưu lượng truy cập (Pitfall: Calibrating quantized models with training data rather than production traffic).
Các đội hiệu chuẩn với đào tạo dữ liệu bởi vì nó là (một cách) dễ dàng (readily) có sẵn và (đã) tạo ra sự xác thực độ chính xác (Teams calibrate with training data because it is readily available and produced validation accuracy).
Trong sản xuất, lưu lượng truy cập sự phân phối thường khác biệt (so) với đào tạo dữ liệu, việc làm (cho) sự hiệu chuẩn (các) tỷ lệ (các) hệ số
(trở nên) kém tối ưu (suboptimal) (In production, traffic distribution often differs from training data, making calibration scale factors suboptimal). Sau-sự đào tạo sự lượng tử hóa quyết định INT8 (các) tỷ lệ (các) hệ số bằng cách (việc) đo lường (các) sự kích hoạt (các) phạm vi (ranges)
trên sự hiệu chuẩn dữ liệu, nhưng điều này giả định sản xuất các đầu vào khớp (với) sự hiệu chuẩn sự phân phối (Post-training quantization determines INT8 scale factors by measuring activation ranges on calibration data, but this assumes production inputs match the calibration distribution). Một
sản xuất hệ thống (đang) đạt được 76.1 phần trăm độ chính xác trên được hiệu chuẩn-ImageNet INT8 rớt (xuống) 72.9
phần trăm, một 3.2 phần trăm-điểm sự mất mát, khi (đang) phục vụ hoang dã máy ảnh các hình ảnh với khác biệt sự chiếu sáng
và các nền (One production system achieving 76.1 percent accuracy on ImageNet-calibrated INT8 dropped to 72.9 percent, a 3.2 percentage-point loss, when serving wildlife camera images with different lighting and backgrounds). Chương 10 cho thấy sự lượng tử hóa lỗi (error) tỷ lệ thuận (scales) với sự kích hoạt phạm vi: sự hiệu chuẩn sai (miscalibration)
khuếch đại (amplifies) các lỗi (một cách) chính xác trên ngoài-sự phân phối các đầu vào nơi các sự kích hoạt vượt quá (được) hiệu chuẩn các phạm vi (Chapter 10 shows quantization error scales with activation range: miscalibration amplifies errors precisely on out-of-distribution inputs where activations exceed calibrated ranges).
Hiệu quả sự lượng tử hóa là dữ liệu-thuật toán (sự) cùng-thiết kế (co-design): (cái) (được) nén mô hình phải được hiệu chuẩn chống lại
(có tính) đại diện các mẫu của thực tế việc phục vụ lưu lượng truy cập, không (phải) sự thuận tiện dữ liệu (Effective quantization is data-algorithm co-design: the compressed model must be calibrated against representative samples of actual serving traffic, not convenience data).
Ngụy biện: Lạnh (sự) khởi động độ trễ chỉ có ý nghĩa (matters) cho (cái) đầu tiên yêu cầu (Fallacy: Cold start latency only matters for the first request).
Các kỹ sư tối ưu hóa ổn định-trạng thái độ trễ (việc) giả định (phần) lớn các yêu cầu đụng (hit) ấm các phiên bản (Engineers optimize steady-state latency assuming most requests hit warm instances). Trong sản
xuất, lạnh (các sự) khởi động cộng dồn (compound) trong suốt các sự kiện (thứ) mà có ý nghĩa nhất: lưu lượng truy cập các đỉnh (nhọn) (đang) yêu cầu sự tăng-quy mô,
các sự triển khai (đang) tung ra (rolling out) mới các phiên bản, và sự phục hồi (recovery) từ phiên bản các sự thất bại (In produc-tion, cold starts compound during the events that matter most: traffic spikes requiring scale-up, deployments rolling out new versions, and recovery from instance failures). Phần 13.6.2 (trình bày) chi tiết
giải phẫu học (anatomy) của lạnh (sự) khởi động: TensorRT sự biên dịch đơn độc tốn 30 s cho mỗi phiên bản (Section 13.6.2 details the anatomy of cold start: TensorRT compilation alone takes 30 s per instance). Trong suốt một lưu lượng truy cập
đỉnh (nhọn) (đang) yêu cầu 10 mới các phiên bản, tổng (aggregate) khởi động-lạnh công việc đạt (đến) 300 (các) phiên bản-giây (instance-seconds); nếu (các)
các phiên bản ấm (lên) (một cách) song song, mới công suất trở nên (trở nên) hữu ích sau khoảng 30 s (During a traffic spike requiring 10 new instances, aggregate cold-start work reaches 300 instance-seconds; if the instances warm in parallel, new capacity becomes useful after about 30 s). Tệ hơn, các yêu cầu đụng
lạnh các phiên bản trải nghiệm 500 ms độ trễ so với 5 ms ổn định-trạng thái, một 100× sự xuống cấp (thứ) mà vi phạm
(các) SLO (một cách) chính xác khi lưu lượng truy cập là (cao) nhất (Worse, requests hitting cold instances experience 500 ms latency vs. 5 ms steady-state, a 100× degradation that violates SLOs precisely when traffic is highest). Các hệ thống (đang) phớt lờ lạnh (sự) khởi động đáp ứng (các) SLO trong suốt ổn định trạng thái
nhưng thất bại trong suốt tăng-quy mô các sự kiện và sự triển khai các cửa sổ khi (độ) tin cậy (reliability) có ý nghĩa nhất (Systems ignoring cold start meet SLOs during steady state but fail during scale-up events and deployment windows when reliability matters most).
Cạm bẫy: Việc mở rộng quy mô mà không (có) một ấm-nhóm (warm-pool) hay (được) theo giai đoạn-việc tải (staged-loading) ngân sách (Pitfall: Scaling without a warm-pool or staged-loading budget).
Sự tự động mở rộng các chính sách (thứ) mà (đếm) chỉ ổn định-trạng thái các bản sao (đánh giá) thấp (underestimate) (cái) công suất (được) yêu cầu
trong suốt lưu lượng truy cập các đỉnh (nhọn) và các sự triển khai (Autoscaling policies that count only steady-state replicas underestimate the capacity needed during traffic spikes and deployments). Việc phục vụ các hệ thống cần ấm (các) nhóm (pre-initialized spare replicas), (được) theo giai đoạn mô hình việc tải, hay (sự) tiếp nhận sự kiểm soát sao cho mới các bản sao trở nên (trở nên) hữu ích trước khi
người dùng các yêu cầu phụ thuộc vào chúng (Serving systems need warm pools (pre-initialized spare replicas), staged model loading, or admission control so that new replicas become useful before user requests depend on them). Ngân sách nên bao gồm sự biên dịch, trọng số việc tải, bộ đệm
sự khởi tạo, và sức khỏe-việc kiểm tra thời gian, bởi vì những các bước đó quyết định liệu (việc) mở rộng quy mô (scale-out) thêm công suất
hay thêm một khác nguồn của đuôi độ trễ (The budget should include compilation, weight loading, cache initialization, and health-check time, because those steps determine whether scale-out adds capacity or adds another source of tail latency).
13.13 Tóm tắt
Việc phục vụ đánh dấu (marks) (cái) sự chuyển tiếp (transition) từ mô hình (sự) phát triển sang sản xuất sự triển khai, nơi (cái) sự tối-
ưu hóa (các) sự ưu tiên (thứ) mà (đã) chi phối (sự) đào tạo phải (bị) đảo ngược (Serving marks the transition from model development to production deployment, where the opti-mization priorities that governed training must be inverted). (Cái) sự dịch chuyển từ thông lượng sự tối đa hóa
sang độ trễ sự tối thiểu hóa biến đổi mọi hệ thống thiết kế quyết định (The shift from throughput maximization to latency minimization transforms every system design decision). (Cái) hàng đợi lý thuyết các nền tảng
(được) thiết lập ở đây tiết lộ (reveal) tại sao này sự đảo ngược là không (phải) (chỉ) đơn thuần một (sự) thay đổi trong các số liệu mà (là) một (sự) thay đổi trong (cái)
(đang) chi phối (governing) toán học (The queuing theory foundations established here reveal why this inversion is not merely a change in metrics but a change in the governing mathematics). (Cái) phi tuyến mối quan hệ giữa sự sử dụng và độ trễ có nghĩa là
các hệ thống (đang) hành xử tốt tại vừa phải (moderate) tải có thể (một cách) bất thình lình (suddenly) vi phạm (các) SLO khi lưu lượng truy cập gia tăng (một cách) khiêm tốn (The nonlinear relationship between utilization and latency means that systems behaving well at moderate load can suddenly violate SLOs when traffic increases modestly).
Little’s Định luật và (cái) M/M/1 chờ (đợi) thời gian các phương trình cung cấp (cái) định lượng nền tảng cho công suất
việc lập kế hoạch, (việc) thay thế dựa trên-trực giác việc dự liệu bằng kỹ thuật sự nghiêm ngặt (rigor) (Little’s Law and the M/M/1 wait time equations provide the quantitative foundation for capacity planning, replacing intuition-based provisioning with engineering rigor).
Hiệu quả việc phục vụ sự tối ưu hóa yêu cầu (việc) hiểu (cái) hoàn chỉnh yêu cầu con đường thay vì
(việc) tập trung (một cách) độc quyền vào mô hình sự suy luận (Effective serving optimization requires understanding the complete request path rather than focusing exclusively on model inference). Giao diện các giao thức (protocols) như gRPC và hiệu quả sự tuần tự hóa
các định dạng tối thiểu hóa (cái) “thuế” của dữ liệu sự di chuyển, trong khi việc tiền xử lý thường tiêu thụ 45 tới 70 phần trăm
của tổng độ trễ khi sự suy luận chạy trên (được) tối ưu hóa các bộ tăng tốc (Interface protocols like gRPC and efficient serialization formats minimize the “tax” of data movement, while preprocessing often consumes 45 to 70 percent of total latency when inference runs on optimized accelerators). (Các) quy mô-micro giây các chi phí hoạt động

13. Mô hình Việc phục vụ
767
(được) nhận diện bởi Barroso, Patterson, và các đồng nghiệp giải thích tại sao việc phục vụ độ trễ thường vượt quá (cái) tổng
của (những) (được) đo lường (các) phần (của) nó, và tại sao cấp độ-hệ thống sự tối ưu hóa có ý nghĩa nhiều (bằng) như mô hình sự tối ưu hóa (identified by Barroso, Patterson, and colleagues explain why serving latency often exceeds the sum of its measured parts, and why system-level optimization matters as much as model optimization).
Đào tạo-phục vụ sự sai lệch (skew) đại diện (cho) một khác chiều (dimension) của (cái) độ phức tạp này, (một cách) im lặng (việc) làm xuống cấp độ chính xác
khi việc tiền xử lý logic khác biệt giữa đào tạo và sản xuất các môi trường trong các cách (thứ) mà
truyền thống việc kiểm thử không thể phát hiện (Training-serving skew represents another dimension of this complexity, silently degrading accuracy when preprocessing logic differs between training and production environments in ways that traditional testing cannot detect).
(Cái) lưu lượng truy cập mẫu sự phân tích tiết lộ (như thế nào) (cái) sự triển khai mô hình (được) lựa chọn trong Chương 2 định hình (shapes)
mọi việc phục vụ quyết định (ở) hạ nguồn (downstream) (The traffic pattern analysis reveals how the deployment paradigm selected in Chapter 2 shapes every serving decision downstream). Máy chủ các khối lượng công việc với Poisson các sự đến tối ưu hóa động
việc lập lô các cửa sổ, tự trị các phương tiện với (đang) truyền phát cảm biến dữ liệu yêu cầu (được) đồng bộ hóa lô
sự hình thành, và di động các ứng dụng với người dùng-đơn (single-user) các mẫu loại bỏ việc lập lô (một cách) hoàn toàn (Server workloads with Poisson arrivals optimize dynamic batching windows, autonomous vehicles with streaming sensor data require synchronized batch formation, and mobile applications with single-user patterns eliminate batching entirely). Mỗi
mẫu là một trực tiếp hệ quả (consequence) của (cái) vật lý các sự ép buộc (năng lượng bức tường, bộ nhớ bức tường, ánh sáng rào cản (barrier))
(thứ) mà (đã) tạo ra (cái) bốn các mô hình trong (cái) (lần) đầu tiên nơi (Each pattern is a direct consequence of the physical constraints (power wall, memory wall, light barrier) that created the four paradigms in the first place). (Các) MLPerf các kịch bản mã hóa (codify) những các mẫu này cho
được tiêu chuẩn hóa việc điểm chuẩn, (việc) kết nối (cái) việc phục vụ các nguyên tắc (được) thiết lập ở đây (với) (cái) (sự) đo lường
các khuôn khổ (được) khám phá trong Chương 12 (The MLPerf scenarios codify these patterns for standardized benchmarking, connecting the serving principles established here to the measurement frameworks explored in Chapter 12).
Cấp độ-nút sự tối ưu hóa các kỹ thuật (đồ thị sự biên dịch, toán tử sự hợp nhất, và (có tính) hệ thống việc lập hồ-
sơ (profil-ing)) làm cầu nối (cái) khoảng trống giữa cấp độ-mô hình các quyết định và phần cứng sự thực thi, thường mang lại 2–5×
bổ sung sự tăng tốc thông qua tốt hơn sự sử dụng của (cái) bộ tăng tốc’s (chu) kỳ (làm) việc (duty cycle) (Node-level optimization techniques (graph compilation, operator fusion, and systematic profil-ing) bridge the gap between model-level decisions and hardware execution, often yielding 2–5× additional speedup through better utilization of the accelerator’s duty cycle). Độ chính xác sự lựa chọn
và thời gian chạy sự tối ưu hóa mở rộng (cái) sự lượng tử hóa các kỹ thuật từ Chương 10 và Tensor Lõi
các khả năng từ Chương 11 vào (trong) (cái) việc phục vụ miền (domain) (Precision selection and runtime optimization extend the quantization techniques from Chapter 10 and Tensor Core capabilities from Chapter 11 into the serving domain). (Cái) sự dịch (translation) của những (thuộc về) kỹ thuật các số liệu này
thành đơn vị tính kinh tế, như (được) hiển thị bởi (cái) Llama-3 trường hợp nghiên cứu, minh họa (như thế nào) kỹ thuật các quyết định
liên quan (đến) việc lập lô, độ chính xác, và phần cứng sự lựa chọn (một cách) trực tiếp quyết định (cái) (về mặt) tài chính tính khả thi của
sự triển khai, một áp lực (được) minh họa bởi (cái) công khai API giá cả sự nén trong hình 13.2 (The translation of these technical metrics into unit economics, as shown by the Llama-3 case study, demonstrates how engineering decisions regarding batching, precision, and hardware selection directly determine the financial viability of deployment, a pressure illustrated by the public API price compression in figure 13.2).
(Cái) việc phục vụ các nguyên tắc (được) thiết lập ở đây (hàng đợi lý thuyết cho công suất việc lập kế hoạch, việc tiền xử lý sự tối-
ưu hóa, việc lập lô chiến lược sự lựa chọn, và đào tạo-phục vụ sự sai lệch sự phòng ngừa) hình thành (cái) nền tảng cho
(việc) xây dựng sản xuất ML các hệ thống (thứ) mà đáp ứng thực-tế (các) SLA (The serving principles established here (queuing theory for capacity planning, preprocessing opti-mization, batching strategy selection, and training-serving skew prevention) form the foundation for building production ML systems that meet real-world SLAs). Cho dù (đang) triển khai một sự gợi ý
hệ thống (đang) phục vụ hàng triệu của người dùng hay một y tế AI nơi mọi mili giây ảnh hưởng (tới) bệnh nhân các kết quả,
những các nguyên tắc này chuyển dịch toán học (sự) thấu hiểu thành kỹ thuật các quyết định (thứ) mà quyết định
liệu các hệ thống thành công hay thất bại dưới tải (Whether deploying a recommendation system serving millions of users or a medical AI where every millisecond affects patient outcomes, these principles translate mathematical understanding into engineering decisions that determine whether systems succeed or fail under load).
Chính Những điểm rút ra (Takeaways): Việc đảo ngược mọi đào tạo sự ưu tiên
• Việc phục vụ là độ trễ tính kinh tế (Serving is latency economics): Đào tạo thưởng (rewards) thông lượng (hơn) (trên) dài các (sự) chạy, nhưng việc phục vụ
tiêu một (được) cố định mỗi-yêu cầu ngân sách (xuyên) qua sự tuần tự hóa, việc tiền xử lý, việc xếp hàng đợi, sự suy luận,
việc hậu xử lý, và (cái) mạng lưới (Training rewards throughput over long runs, but serving spends a fixed per-request budget across serialization, preprocessing, queuing, inference, postprocessing, and the network). (Việc) Tối ưu hóa chỉ mô hình độ trễ bỏ lỡ (các) giai đoạn người dùng
thực sự chờ trên (đó) (Optimizing only model latency misses the stages users actually wait on).
• Sự sử dụng biến (turns) thành sự chờ (đợi) (Utilization turns into waiting): Hàng đợi lý thuyết làm (cho) công suất việc lập kế hoạch phi tuyến: tại
80 phần trăm sự sử dụng, trung bình thời gian trong hệ thống là 5× dịch vụ thời gian; tại 90 phần trăm, nó đạt (tới)
10× (Queuing theory makes capacity planning nonlinear: at 80 percent utilization, average time in system is 5× service time; at 90 percent, it reaches 10×). Hiệu quả-chi phí khoảng trống giữ khiêm tốn lưu lượng truy cập các sự trào dâng (surges) khỏi (việc) trở thành SLO các sự thất bại (Cost-efficient headroom keeps modest traffic surges from becoming SLO failures).
• Nhanh các mô hình tiết lộ đường ống các khoản thuế (Fast models reveal pipeline taxes): Một khi sự suy luận rớt xuống xấp xỉ 5 ms, hình ảnh sự giải mã (decode),
sự token hóa, và khác việc tiền xử lý có thể tiêu thụ 45–70 phần trăm của tổng độ trễ (Once inference falls to roughly 5 ms, image decode, tokenization, and other preprocessing can consume 45–70 percent of total latency). (Cái)
(đang) ràng buộc (binding) sự tối ưu hóa trở thành (cái) yêu cầu con đường, không (phải) (cái) thần kinh mạng lưới hạt nhân (The binding optimization becomes the request path, not the neural network kernel).
• Việc lập lô theo (sau) lưu lượng truy cập, không (phải) thói quen (Batching follows traffic, not habit): Poisson web các sự đến có thể sử dụng động việc lập lô,
(được) đồng bộ hóa các cảm biến cần (được) căn chỉnh các lô, và người dùng-đơn di động các khối lượng công việc thường
không thể lập lô (tại tất cả) (Poisson web arrivals can use dynamic batching, synchronized sensors need aligned batches, and single-user mobile workloads often cannot batch at all). (Cái) đúng (đắn) việc lập lô cửa sổ chuyển đổi sự chùng (xuống) (slack) thành thông lượng mà không (cần)
(việc) tiêu (cái) độ trễ ngân sách (The right batching window converts slack into throughput without spending the latency budget).
• Sự sai lệch (Skew) làm hỏng (breaks) độ chính xác mà không (có) các lỗi (Skew breaks accuracy without errors): Đổi kích thước các phương pháp, sự chuẩn hóa thứ tự, sự hiệu chuẩn
dữ liệu, hay đặc trưng các định nghĩa (thứ) mà khác biệt giữa sự đào tạo và việc phục vụ dịch chuyển sống (live) các đầu vào
(ra) ngoài (cái) (đã) học được sự phân phối (Resize methods, normalization order, calibration data, or feature definitions that differ between training and serving shift live inputs outside the learned distribution). (Việc) Tái sử dụng giống hệt mã các con đường và (việc) giám sát sản xuất
các lát cắt (slices) ngăn chặn im lặng sự xuống cấp (Reusing identical code paths and monitoring production slices prevents silent degradation).
• LLM việc phục vụ là bộ nhớ sự quản lý (LLM serving is memory management): Giải mã thường đọc các trọng số từ VRAM cho
mọi (được) tạo ra token, do đó token độ trễ là bị giới hạn-băng thông trừ khi việc lập lô thay đổi
(cái) sự ép buộc (Decode often reads weights from VRAM for every generated token, so token latency is bandwidth-bound unless batching changes the constraint). KV-bộ đệm bố cục, PagedAttention, liên tục việc lập lô, độ chính xác, và
thời gian chạy sự lựa chọn quyết định cả tính đồng thời và chi phí cho mỗi token (KV-cache layout, PagedAttention, continuous batching, precision, and runtime choice determine both concurrency and cost per token).

768
13.13 Tóm tắt
• Thời gian chạy các sự lựa chọn trở thành cơ sở hạ tầng các hóa đơn (Runtime choices become infrastructure bills): Độ chính xác, đồ thị sự biên dịch, toán tử
sự hợp nhất, và việc phục vụ thời gian chạy chuyển đổi (một cách) trực tiếp thành bản sao số lượng và chi phí cho mỗi sự suy luận (Precision, graph compilation, operator fusion, and serving runtime translate directly into replica count and cost per inference).
Sự lượng tử hóa và (được) chuyên môn hóa các thời gian chạy có thể (một cách) đáng kể giảm thiểu (cái) (được) yêu cầu việc phục vụ công suất
khi chúng bảo tồn độ chính xác và khớp (với) (cái) mục tiêu phần cứng (Quantization and specialized runtimes can materially reduce required serving capacity when they preserve accuracy and fit the target hardware).
Sự đào tạo được đánh giá bởi bao nhiêu công việc nó hoàn thành; việc phục vụ được đánh giá bởi liệu công việc hoàn thành
đúng thời gian (hay không), và đó đơn (sự) thay đổi của câu hỏi đảo ngược (inverts) mọi thứ (Training is judged by how much work it completes; serving is judged by whether the work finishes in time, and that single change of question inverts everything). Một độ trễ ngân sách được cố định từ (bên)
ngoài, bởi (cái) người dùng và (cái) hợp đồng, và mọi giai đoạn của một yêu cầu chi tiêu (spends) chống lại (cái) cùng một vỏ bọc (envelope):
sự tuần tự hóa, việc tiền xử lý, (cái) hàng đợi, (cái) mô hình, (cái) phản hồi (A latency budget is fixed from the outside, by the user and the contract, and every stage of a request spends against the same envelope: serialization, preprocessing, the queue, the model, the response). (Cái) (được) đào tạo thuật toán, (cái) sống dữ liệu,
và (cái) máy (tất cả) cùng nhau gặp (nhau) (meet) bên trong đó vỏ bọc, và (cái) hàng đợi là (những) gì làm nó (trở nên) nguy hiểm (treacherous), bởi vì
chờ (đợi) thời gian leo thang (một cách) phi tuyến với tải và một hệ thống (một cách) thoải mái bên trong ngân sách tại vừa phải
lưu lượng truy cập có thể thổi qua (blow through) nó trên một nhỏ sự trào dâng (The trained algorithm, the live data, and the machine all meet inside that envelope, and the queue is what makes it treacherous, because waiting time climbs nonlinearly with load and a system comfortably within budget at moderate traffic can blow through it on a small surge). Không có gì trong việc phục vụ loại bỏ công việc (ra) khỏi (cái) yêu cầu;
nó chỉ quyết định (như thế nào) (cái) (được) cố định ngân sách được chia ra, đó là lý do tại sao (cái) mục tiêu là không (còn) (là) tốc độ nữa mà (là) (cái)
sự đảm bảo rằng mọi yêu cầu, mọi thời điểm, đáp (lands) (vào) bên trong (cái) ranh giới (line) (Nothing in serving removes work from the request; it only decides how the fixed budget is divided, which is why the goal is no longer speed but the guarantee that every request, every time, lands inside the line).
(Cái) Gì Tiếp Theo: Từ nút đến nhà máy
Chương này (đã) thiết kế (cái) đơn việc phục vụ nút (This chapter engineered the single serving node). Theo (cách) của riêng nó (On its own), tuy nhiên, đó nút là mong manh (fragile).
Các mô hình trôi dạt (drift) khi (cái) thế giới thay đổi, các bản cập nhật phải chạm tới người dùng mà không (việc) làm gián đoạn (interrupting) dịch vụ, và
việc mở rộng quy mô các sự kiện yêu cầu nhiều các bản sao để hành xử như một đáng tin cậy (dependable) hệ thống (Models drift as the world changes, updates must reach users without interrupting service, and scaling events require many replicas to behave like one dependable system). Trong Chương 14, chúng ta
mở rộng quy mô (của) chúng ta góc nhìn từ (cái) đơn yêu cầu (tới) (cái) sản xuất nhà máy: CI/CD ((được) tự động hóa
bản dựng (build), kiểm thử (test), và việc phát hành (release) các đường ống) quyết định (cái) nào mô hình đồ tạo tác (có) thể xuất xưởng (ship), mô hình các sổ đăng ký (registries) ((được) lập-phiên-
bản (ver-sioned) mô hình đồ tạo tác các cửa hàng) và đặc trưng các cửa hàng (được chia sẻ phục vụ/đào tạo đặc trưng các kho lưu trữ (repositories))
giữ việc phục vụ (được) căn chỉnh với sự đào tạo, tính có thể quan sát (observability) ((thuộc về) từ xa (telemetry) cho hành vi và sức khỏe) phát hiện
độ trễ và độ chính xác sự trôi dạt, và quay lui (rollback) máy móc (các công cụ cho việc khôi phục (reverting) một xấu sự phát hành) giữ
các sự thất bại khỏi (việc) trở thành vĩnh viễn (permanent) các sự ngừng hoạt động (outages) (In Chapter 14, we scale our perspective from the single request to the production factory: CI/CD (automated build, test, and release pipelines) decides which model artifact may ship, model registries (ver-sioned model artifact stores) and feature stores (shared serving/training feature repositories) keep serving aligned with training, observability (telemetry for behavior and health) detects latency and accuracy drift, and rollback machinery (tools for reverting a bad release) keeps failures from becoming permanent outages).
Nghiên cứu Các câu hỏi: Cho sâu hơn (further) sự điều tra (inquiry)
• (Như thế nào) (Việc) dịch chuyển từ đào tạo thông lượng (tới) việc phục vụ đuôi độ trễ thay đổi hệ thống kiến-
trúc? (How does shifting from training throughput to serving tail latency change system archi-tecture?)
• (Cái) gì độ trễ ngân sách sự phân rã nhận diện liệu (cái) mô hình, hàng đợi, việc tiền xử lý,
sự tuần tự hóa, hay mạng lưới là (đang) ràng buộc (binding) (hay không)? (What latency budget decomposition identifies whether the model, queue, preprocessing, serialization, or network is binding?)
• (Như thế nào) sự sử dụng khoảng trống nên (được) định giá chống lại SLO-sự vi phạm rủi ro? (How should utilization headroom be priced against SLO-violation risk?)
• (Như thế nào) việc lập lô chiến lược (nên) thích ứng (với) Poisson các sự đến, (đang) truyền phát lưu lượng truy cập, người dùng-đơn
các khối lượng công việc, và token sự tạo ra? (How should batching strategy adapt to Poisson arrivals, streaming traffic, single-user workloads, and token generation?)