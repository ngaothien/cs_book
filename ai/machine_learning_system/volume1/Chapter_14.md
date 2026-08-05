Các ứng dụng (Applications)
> _
Các hoạt động (Operations)
Việc phục vụ (Serving)
Sự đào tạo (Training)
∇
Các mô hình (Models)
Các khuôn khổ (Frameworks)
Phần cứng (Hardware)
Dữ liệu (Data)
14
ML Các hoạt động (Operations)
14.1 MLOps Tổng quan
14.2 Các nguyên tắc và
Các nền tảng (Foundations)
14.3 Kỹ thuật Nợ (Technical Debt)
14.4 Sự phát triển
Cơ sở hạ tầng
14.5 Sản xuất Các hoạt động
14.6 Thiết kế và Sự trưởng thành (Maturity)
Khuôn khổ
14.7 Trường hợp Các nghiên cứu
14.8 Các ngụy biện và Các cạm bẫy
14.9 Tóm tắt
Mục đích
Tại sao một ML hệ thống (có) thể hoàn toàn có sẵn và hoàn toàn sai (cùng) lúc (đó) (Why can an ML system be perfectly available and perfectly wrong at the same time)?
Truyền thống phần mềm thất bại (một cách) ồn ào: một rỗng (null) con trỏ ngoại lệ (exception) làm sập (cái) máy chủ, việc giám sát các bảng
điều khiển (dash-boards) chuyển sang đỏ, và các kỹ sư bị gọi (paged) trong vòng (vài) phút (Traditional software fails loudly: a null pointer exception crashes the server, monitoring dash-boards turn red, and engineers are paged within minutes). Máy học các hệ thống thất bại (một cách) im lặng (Machine learning systems fail silently). Một
mô hình (đang) trải nghiệm dữ liệu sự trôi dạt tiếp tục phục vụ các dự đoán với đầy đủ sự tự tin trong khi độ chính xác
xuống cấp tuần (này) qua (by) tuần (khác), không kích hoạt cảnh báo (nào) bởi vì mọi sức khỏe (sự) kiểm tra (độ trễ, thông lượng, thời gian
hoạt động (up-time)) vẫn (có màu) xanh lá cây (A model experiencing data drift continues serving predictions with full confidence while accuracy degrades week by week, triggering no alerts because every health check (latency, throughput, up-time) remains green). (Cái) việc phục vụ cơ sở hạ tầng đưa (gets) các mô hình vào sản xuất; các hoạt động giữ chúng
chính xác một khi chúng (đã) ở đó, và tính chính xác là (cái) khó hơn bài toán (The serving infrastructure gets models into production; operations keeps them correct once they are there, and correctness is the harder problem). Không giống như mã (code), (thứ) mà xuống cấp chỉ
khi (có) ai đó chỉnh sửa nó, các mô hình xuống cấp (một cách) đơn giản bởi vì (cái) thế giới thay đổi: khách hàng hành vi
dịch chuyển, mới sản phẩm các danh mục (categories) xuất hiện, (có tính) mùa vụ các mẫu (patterns) tiến hóa, và (cái) sự phân phối (cái) mô hình
(đã) học từ (đó) (một cách) chậm chạp phân kỳ (diverges) khỏi (cái) sự phân phối nó hiện đối mặt (Unlike code, which degrades only when someone modifies it, models degrade simply because the world changes: customer behavior shifts, new product categories appear, seasonal patterns evolve, and the distribution the model learned from slowly diverges from the distribution it now faces). Điều này không (phải) (là) một thỉnh thoảng sự thất bại
chế độ mà (là) (cái) mặc định quỹ đạo (trajectory) của mọi (được) triển khai mô hình (This is not an occasional failure mode but the default trajectory of every deployed model). Entropy không (phải) (là) một rủi ro (để) được giảm nhẹ (mitigated) mà (là)
một sự chắc chắn (certainty) (để) được quản lý (Entropy is not a risk to be mitigated but a certainty to be managed). Việc quản lý nó yêu cầu một (một cách) cơ bản khác biệt (thuộc về) hoạt động kỷ luật (discipline):
liên tục việc giám sát (thứ) mà theo dõi (tracks) dự đoán chất lượng bên cạnh hệ thống sức khỏe, (được) tự động hóa (sự) đào-tạo-lại
các đường ống (thứ) mà phát hiện sự trôi dạt và phản hồi trước khi độ chính xác xuống cấp tới (các) không thể chấp nhận các mức độ, và
sự triển khai các chiến lược (thứ) mà xác thực (validate) mới mô hình các phiên bản chống lại sản xuất lưu lượng truy cập trước khi đầy (đủ) (sự) tung ra (rollout) (Managing it requires a fundamentally different operational discipline: continuous monitoring that tracks prediction quality alongside system health, automated retrain-ing pipelines that detect drift and respond before accuracy degrades to unacceptable levels, and deployment strategies that validate new model versions against production traffic before full rollout).
Khoảng trống giữa sự phát triển và sản xuất không (phải) (là) một rào cản (hurdle) (để) được vượt qua một lần mà (là) một điều kiện (để)
được quản lý (một cách) vô thời hạn (indefinitely) (The gap between development and production is not a hurdle to be cleared once but a condition to be managed indefinitely). Máy học các hoạt động tồn tại bởi vì thời gian hoạt động mà không (có) độ chính xác là một
hệ thống (thứ) mà (một cách) tự tin cung cấp sai các câu trả lời tại quy mô (Machine learning operations exists because uptime without accuracy is a system that confidently delivers wrong answers at scale). Nó là D·A·M (sự) cùng-thiết kế được làm (cho) liên tục: (cái)
dữ liệu môi trường vẫn (là) một (đang) di chuyển mục tiêu lâu sau khi (cái) ban đầu mô hình được triển khai, do đó (cái) sự căn chỉnh
công việc không bao giờ kết thúc (It is D·A·M co-design made continuous: the data environment remains a moving target long after the initial model is deployed, so the alignment work never ends).
769

770
14.1 MLOps Tổng quan
Học tập Các mục tiêu (Objectives)
• Giải thích tại sao ML các hệ thống có thể duy trì (có) sẵn trong khi dự đoán chất lượng (một cách) im lặng xuống cấp
dưới sự phân phối (sự) dịch chuyển (Explain why ML systems can remain available while prediction quality silently degrades under distribution shift)
• Chẩn đoán (Diagnose) kỹ thuật nợ (xuyên) qua dữ liệu-mô hình, mô hình-cơ sở hạ tầng, và sản xuất-
việc giám sát giao diện các ranh giới (Diagnose technical debt across data-model, model-infrastructure, and production-monitoring interface boundaries)
• Thiết kế đặc trưng các cửa hàng, các sổ đăng ký, và CI/CD các đường ống (thứ) mà bảo tồn đào tạo-phục vụ
sự nhất quán (consistency) và (có thể) tái tạo (reproducible) sự quay lui (Design feature stores, registries, and CI/CD pipelines that preserve training-serving consistency and reproducible rollback)
• Áp dụng (cái) (sự) đào tạo lại sự cũ kỹ (staleness) mô hình để chọn nhận thức-chi phí (cost-aware) (sự) đào tạo lại (các) bộ kích hoạt và các khoảng thời gian (Apply the retraining staleness model to choose cost-aware retraining triggers and intervals)
• Triển khai (được) phân lớp (layered) việc giám sát cho sự trôi dạt, sự sai lệch, sự xuống cấp, doanh nghiệp các số liệu, và dữ liệu
sự tươi mới (freshness) (Implement layered monitoring for drift, skew, degradation, business metrics, and data freshness)
• So sánh canary, xanh-lục (blue-green), bóng (shadow), và quay lui các chiến lược cho sản xuất mô hình
phát hành rủi ro (Compare canary, blue-green, shadow, and rollback strategies for production model release risk)
• Đánh giá (thuộc về) hoạt động sự trưởng thành (maturity) và (sự) đầu tư (việc) sử dụng mô hình tính tới hạn (criticality), (thuộc về) hoạt động rủi ro,
và (thuộc về) tổ chức (sự) sẵn sàng (Evaluate operational maturity and investment using model criticality, operational risk, and organizational readiness)
14.1 MLOps Tổng quan
Sau khi một mô hình được xây dựng, (được) tối ưu hóa, (được) điểm chuẩn, và (được) phục vụ, (cái) hệ thống vẫn phải duy trì
chính xác (After a model is built, optimized, benchmarked, and served, the system still has to remain correct). Một điểm chuẩn thiết lập hiệu suất tại một thời điểm (a point in time); việc phục vụ cơ sở hạ tầng
trả lời các yêu cầu trong (các) mili giây (A benchmark establishes performance at a point in time; serving infrastructure answers requests in milliseconds). (Cái) đội triển khai (vào) sản xuất, và tuần một trông (có vẻ)
xuất sắc (The team deploys to production, and week one looks excellent). (Cái) thử thách bắt đầu trong tuần hai (The challenge begins in week two).
Dữ liệu các sự phân phối dịch chuyển, người dùng hành vi thay đổi, và (cái) thế giới di chuyển (tiếp) (moves on) khỏi (các) điều kiện dưới
(đó) (cái) mô hình đã được đào tạo (Data distributions shift, user behavior changes, and the world moves on from the conditions under which the model was trained). Một lớn phần (fraction) của ML các mô hình (thứ) mà thành công trong (sự) phát triển không bao giờ
tiếp cận (được) duy trì sản xuất (sự) sử dụng, không (phải) bởi vì chúng đã được xây dựng (một cách) không chính xác, mà bởi vì không ai theo dõi
chúng sau khi sự triển khai (A large fraction of ML models that succeed in development never reach sustained production use, not because they were built incorrectly, but because no one watched them after deployment). (Cái) gốc rễ nguyên nhân là một (thuộc về) hoạt động sự không khớp (mismatch): thông thường (conventional) việc giám sát theo dõi
(có tính) tất định (deterministic) hệ thống sức khỏe, bao gồm máy chủ thời gian hoạt động, yêu cầu độ trễ, và yêu cầu thành công các tỷ lệ,
trong khi ML việc giám sát phải theo dõi (có tính) thống kê sức khỏe, bao gồm độ chính xác qua thời gian, đầu vào-sự phân phối
(sự) dịch chuyển, và mỗi-phân đoạn (segment) dự đoán chất lượng (The root cause is an operational mismatch: conventional monitoring tracks deterministic system health, including server uptime, request latency, and request success rates, while ML monitoring must track statistical health, including accuracy over time, input-distribution shift, and per-segment prediction quality). Một mô hình có thể xuống cấp từ 94 phần trăm độ chính xác xuống 81
phần trăm trong khi (không) ném (không có) ngoại lệ (nào), (không) kích hoạt (không có) cơ sở hạ tầng (các) báo động (nào), và (đang) duy trì hoàn hảo
thời gian hoạt động (A model can degrade from 94 percent accuracy to 81 percent while throwing no exceptions, triggering no infrastructure alarms, and maintaining perfect uptime).
(Cái) kỷ luật (thứ) mà làm những vô hình các sự thất bại này (trở nên) có thể nhìn thấy được là Máy Học Các hoạt động
(MLOps) (The discipline that makes these invisible failures visible is Machine Learning Operations (MLOps)). MLOps tổng hợp (synthesizes) việc giám sát, sự tự động hóa, và sự quản trị (governance) thành sản xuất các kiến-
trúc (architec-tures) (thứ) mà phát hiện sự xuống cấp, kích hoạt (sự) đào tạo lại, và duy trì hệ thống sức khỏe xuyên suốt một mô hình’s
(thuộc về) hoạt động vòng đời (lifetime) (MLOps synthesizes monitoring, automation, and governance into production architec-tures that detect degradation, trigger retraining, and maintain system health throughout a model’s operational lifetime). Nó thừa kế (inherits) (cái) sự tự động hóa và các hoạt động dòng dõi (lineage) của DevOps (Debois 2009),
nhưng (cái) sự thất bại chế độ là khác biệt: thông thường các dịch vụ có thể thường được kiểm thử chống lại (có tính) tất định
mã các con đường, trong khi ML các hệ thống phụ thuộc vào đào tạo dữ liệu các sự phân phối, (đã) học (được) các tham số, và
(thuộc về) môi trường (environmental) các điều kiện (thứ) mà dịch chuyển (một cách) liên tục (It inherits the automation and operations lineage of DevOps (Debois 2009), but the failure mode is different: conventional services can often be tested against deterministic code paths, while ML systems depend on training data distributions, learned parameters, and environmental conditions that shift continuously).
(Cái) tuần-hai bài toán khoác (takes) (lên) (có tính) cụ thể hình dạng trong một cụ thể sự triển khai (The week-two problem takes concrete shape in a specific deployment). Xem xét một nhu cầu
(sự) dự đoán hệ thống cho một chia sẻ chuyến đi (ridesharing) dịch vụ (Consider a demand prediction system for a ridesharing service). Ban đầu (các) sự đo lường cho thấy 94 phần trăm độ chính xác, 15 ms
P99 độ trễ, và mạnh (mẽ) hiệu suất (xuyên) qua (các) kiểm thử các phân đoạn (Initial measurements show 94 percent accuracy, 15 ms P99 latency, and strong performance across test segments). Đến (By) tuần bốn, độ chính xác đã rớt xuống
88 phần trăm, nhưng (cái) cơ sở hạ tầng các số liệu hiển thị không có gì sai (By week four, accuracy has dropped to 88 percent, but the infrastructure metrics show nothing wrong). Đến tuần tám, một sản phẩm người quản lý
chú ý (thấy) tài xế (sự) điều phối (dispatch) là kém hiệu quả; (sự) điều tra tiết lộ (cái) mô hình đã không thích ứng (với) một đối thủ cạnh tranh’s
mới sự khuyến mãi (promotion) (thứ) mà (đã) dịch chuyển người dùng hành vi (By week eight, a product manager notices driver dispatch is inefficient; investigation reveals the model has not adapted to a competitor’s new promotion that shifted user behavior). (Cái) mô hình (đã) cần (sự) đào tạo lại sáu tuần trước, nhưng không
hệ thống (nào) đang theo dõi (watching for) này sự xuống cấp (The model needed retraining six weeks ago, but no system was watching for this degradation). MLOps cung cấp (cái) khuôn khổ để phát hiện (kiểu) (such) sự trôi dạt (drift) (như vậy),
kích hoạt (sự) đào tạo lại, và xác thực mới các mô hình trước khi (những) người dùng trải nghiệm (cái) tác động (impact) (MLOps provides the framework to detect such drift, trigger retraining, and validate new models before users experience the impact).
(Cái) (thuộc về) hoạt động sự không khớp kết nối (một cách) trực tiếp (tới) (cái) cuốn sách’s (thuộc về) phân tích các nền tảng (The operational mismatch connects directly to the book’s analytical foundations). Nếu việc điểm chuẩn
cung cấp (các) cảm biến cho (của) chúng ta hệ thống, MLOps là (cái) hoàn chỉnh kiểm soát hệ thống (If benchmarking provides the sensors for our system, MLOps is the complete control system). Nó đóng (closes) (cái) sự xác minh khoảng trống
từ phương trình 1.1 bằng cách (việc) (một cách) liên tục hiệu chuẩn lại (recalibrating) chống lại một (đang) thay đổi thế giới (It closes the verification gap from equation 1.1 by continuously recalibrating against a changing world). MLOps vận hành hóa (operationalizes)
(cái) sự xuống cấp phương trình trong phương trình 1.3: độ chính xác (sự) phân rã (decay) là không (phải) một sự thất bại của (cái) mã, mà (là) một (điều) không thể tránh khỏi (inevitable)
hệ quả (consequence) của (cái) (thuộc về) sự phân phối (distributional) sự phân kỳ (divergence) giữa (cái) thế giới chúng ta (đã) đào tạo trên (đó) và (cái) thế giới chúng ta
phục vụ (MLOps operationalizes the degradation equation in equation 1.3: accuracy decay is not a failure of the code, but an inevitable consequence of the distributional divergence between the world we trained on and the world we serve). Nó cũng chính thức hóa (formalizes) các giao diện và các trách nhiệm (xuyên) qua (một cách) truyền thống (được) cô lập các miền
(dữ liệu khoa học, máy học kỹ thuật, và các hệ thống các hoạt động (Amershi et al. 2019)) thông qua
1
Việc đo từ xa (Telemetry):
(Cái) duy nhất
phản hồi con đường (thứ) mà làm
mô hình sự xuống cấp có thể nhìn thấy được
trước khi nó trở thành một doanh nghiệp sự thất-
bại. Không giống như truyền thống phần-
mềm, nơi các sự cố (crashes) và lỗi (er-
ror) các mã (codes) nổi lên (surface) các bài toán
(một cách) ngay lập tức, ML các hệ thống xuống
cấp (một cách) im lặng:
sự phân phối
sự dịch chuyển có thể đi không bị phát hiện cho
(các) tuần hay (các) tháng mà không (có) (thuộc về) thống-
kê (sta-tistical) việc đo từ xa (đặc trưng các sự phân-
phối (tributions), dự đoán (sự) tự-
tin, (sự) trôi dạt các chỉ báo (indicators)).
Đến
(By) đó thời điểm (cái) mô hình đã (và đang) (been)
đang tạo ra (đang) bị xuống cấp các dự đoán
tại đầy (đủ) (sự) tự động hóa tỷ lệ (rate), (việc) tích-
lũy (ac-cumulating) (đang) ghép (compounding) các lỗi (er-
rors) trong (thuộc về) hạ nguồn các hệ thống
(thứ) mà không cơ sở hạ tầng số liệu (nào)
sẽ (có thể) đã gắn cờ (flagged).

772
14.2 Các nguyên tắc và Các nền tảng
(một cách) liên tục (sự) đào tạo lại, A/B sự đánh giá, (được) tốt nghiệp (graduated) sự tung ra, và (được) tiêu chuẩn hóa đồ tạo tác việc theo dõi (tracking) (thứ) mà
làm mọi (được) triển khai mô hình (có thể) tái tạo (reproducible) và (có thể) kiểm toán (auditable) (continuous retraining, A/B evaluation, graduated rollout, and standardized artifact tracking that makes every deployed model reproducible and auditable).
Việc triển khai, việc giám sát, và việc duy trì một đơn ML hệ thống trong sản xuất cấu thành (những) gì chúng
tôi gọi là đơn-mô hình các hoạt động, (cái) (thuộc về) hoạt động đơn vị cho (cái) sự phân tích (thứ) mà theo (sau) (Deploying, monitoring, and maintaining a single ML system in production constitutes what we term single-model operations, the operational unit for the analysis that follows). Này (thuộc về) hoạt động đơn vị
yêu cầu một (được) dành riêng (dedicated) thuật ngữ (term) (This operational unit requires a dedicated term). Chúng tôi định nghĩa (cái) ML nút, một hoàn chỉnh hệ thống (đang) bao gồm (comprising) dữ liệu các đường ống,
đặc trưng tính toán, mô hình (sự) đào tạo, việc phục vụ cơ sở hạ tầng, và việc giám sát cho một đơn máy
học ứng dụng (We define the ML node, a complete system comprising data pipelines, feature computation, model training, serving infrastructure, and monitoring for a single machine learning application). Nền tảng các hoạt động tại lớn hơn quy mô (việc quản lý hàng trăm của các mô hình, chéo-
mô hình các sự phụ thuộc, nhiều-khu vực (multi-region) sự phối hợp, và toàn-tổ chức (organization-wide) ML nền tảng kỹ thuật)
cấu thành nâng cao các chủ đề (thứ) mà xây dựng trên những đơn-mô hình các nền tảng này (Platform operations at larger scale (managing hundreds of models, cross-model dependencies, multi-region coordination, and organization-wide ML platform engineering) constitute advanced topics that build on these single-model foundations).
(Cái) vòng đời của một sản xuất ML nút bắt đầu với (cái) tuần-hai (sự) kiểm soát bài toán và theo (sau) (các)
giao diện (thứ) mà làm nó (có thể) quan sát (được) (The lifecycle of one production ML node starts with the week-two control problem and follows the interfaces that make it observable). Kỹ thuật nợ giải thích tại sao sản xuất ML trở nên đắt đỏ
sau (cái) (lần) đầu tiên (có) thành công sự triển khai; đặc trưng các cửa hàng, CI/CD các đường ống, và thí nghiệm việc theo dõi sau đó
định nghĩa (cái) cơ sở hạ tầng (được) yêu cầu để tái tạo dữ liệu, mã, các tham số, và cấu hình (Technical debt explains why production ML becomes expensive after the first successful deployment; feature stores, CI/CD pipelines, and experiment tracking then define the infrastructure needed to reproduce data, code, parameters, and configuration). Một khi những
đồ tạo tác đó có thể được tái tạo, việc giám sát, sự trôi dạt sự phát hiện, sự triển khai chiến lược, và sự cố (incident) (sự) phản hồi
giữ (cái) mô hình khỏe mạnh qua thời gian (Once those artifacts can be reproduced, monitoring, drift detection, deployment strategy, and incident response keep the model healthy over time). Sự đầu tư các quyết định và trường hợp các nghiên cứu sau đó cho thấy (như thế nào) (các) giống nhau
các nguyên tắc trông (có vẻ) khác biệt trong một thiết bị đeo (wearable) biên (edge) và trong lâm sàng (clinical) AI các hoạt động (Investment decisions and case studies then show how the same principles look different in an edge wearable and in clinical AI operations).
(Cái) đơn-mô hình (thuộc về) hoạt động thử thách phân rã thành ba khác biệt các giao diện (The single-model operational challenge decomposes into three distinct interfaces). (Cái) Dữ liệu-Mô hình
Giao diện là (cái) sự chuyển giao (handoff) giữa dữ liệu cơ sở hạ tầng và mô hình (sự) đào tạo; (của) nó mục tiêu là đặc trưng sự nhất quán,
sao cho đào tạo và phục vụ các đường ống tính toán (các) đặc trưng (cùng) (cái) giống nhau cách (The Data-Model Interface is the handoff between data infrastructure and model training; its goal is feature consistency, so training and serving pipelines compute features the same way). (Cái) Mô hình-Cơ sở hạ tầng
Giao diện là (cái) sự chuyển tiếp (transition) từ (được) đào tạo các trọng số sang (có thể) mở rộng quy mô dịch vụ; (của) nó thử thách là môi trường
sự ngang bằng (parity), bởi vì một mô hình (thứ) mà hoạt động trong một sổ tay có thể thất bại trong sản xuất do phiên bản, sự phụ thuộc,
hay thời gian chạy các sự không khớp (The Model-Infrastructure Interface is the transition from trained weights to scalable service; its challenge is environment parity, because a model that works in a notebook may fail in production due to version, dependency, or runtime mismatches). (Cái) Sản xuất-Việc giám sát Giao diện là (cái) phản hồi vòng lặp (thứ) mà kích hoạt
tự-sự sửa chữa (self-correction), (việc) trả về (thuộc về) thống kê việc đo từ xa từ sản xuất (về) đào tạo bởi vì ML các hệ thống thất bại
(một cách) im lặng thông qua sự trôi dạt thay vì các sự cố (crashes) (The Production-Monitoring Interface is the feedback loop that enables self-correction, returning statistical telemetry from production to training because ML systems fail silently through drift rather than crashes).
Những các giao diện đó quyết định (nơi) nào (cái) chương’s cơ sở hạ tầng (các) mảnh (pieces) thuộc về (Those interfaces determine where the chapter’s infrastructure pieces belong). Đặc trưng các cửa hàng ổn (định)-
hóa (stabi-lize) đặc trưng tính toán tại (cái) dữ liệu-mô hình ranh giới (Feature stores stabi-lize feature computation at the data-model boundary). Mô hình các sổ đăng ký và sự triển khai các đường ống
bảo tồn (cái) mô hình-cơ sở hạ tầng sự chuyển giao (Model registries and deployment pipelines preserve the model-infrastructure handoff). Sự trôi dạt các màn hình (monitors), (sự) đào tạo lại (các) bộ kích hoạt, và sự quản trị
các chính sách đóng (closes) (cái) sản xuất-việc giám sát vòng lặp trước khi im lặng sự xuống cấp trở thành một doanh nghiệp sự thất bại (Drift monitors, retraining triggers, and governance policies close the production-monitoring loop before silent degradation becomes a business failure).
(Cái) việc đo từ xa1 (đang) chảy (flowing) qua những các giao diện này cung cấp (cái) dữ liệu (được) yêu cầu cho (được) thông báo (informed) (thuộc về) hoạt động
các quyết định (The telemetry1 flowing through these interfaces provides the data needed for informed operational decisions). Đó (thuộc về) hoạt động phạm vi (scope) làm (cho) (cái) tiếp theo tác vụ (trở nên) chính xác: phân biệt (distinguish) MLOps từ truyền thống
DevOps, nhận diện (các) nền tảng (foundational) các nguyên tắc (thứ) mà chi phối sản xuất các quyết định, và phơi bày (expose) (các) khoản nợ
các mẫu (thứ) mà tích lũy khi những các nguyên tắc đó bị phớt lờ (That operational scope makes the next task precise: distinguish MLOps from traditional DevOps, identify the foundational principles that govern production decisions, and expose the debt patterns that accumulate when those principles are ignored).
14.2 Các nguyên tắc và Các nền tảng
Một sản xuất ML sự phát hành là không (còn) (là) chỉ một mã (sự) khác biệt (diff) (nữa): dữ liệu các sự phân phối, (đã) học (được) các tham số,
sự đánh giá các lát cắt (slices), và việc giám sát phản hồi các vòng lặp tất cả trở thành phát hành các đối tượng (thứ) mà có thể thay đổi
(cái) hệ thống’s hành vi (A production ML release is no longer just a code diff: data distributions, learned parameters, evaluation slices, and monitoring feedback loops all become release objects that can change the system’s behavior). MLOps xây dựng trên DevOps nhưng giải quyết (addresses) những cụ thể các nhu cầu này của ML hệ thống
sự phát triển và sự triển khai (Kreuzberger et al. 2023; Amershi et al. 2019) (MLOps builds on DevOps but addresses these specific demands of ML system development and deployment (Kreuzberger et al. 2023; Amershi et al. 2019)). Truyền thống CI/CD có thể
thường lý luận về mã, cấu hình, các bài kiểm tra, và cơ sở hạ tầng như (là) (các) chính phát hành các đối tượng;
ML các hoạt động cũng phải quản lý các đồ tạo tác (thứ) mà (của) chúng tính hợp lệ (validity) phụ thuộc vào (cái) dữ liệu và môi trường
(thứ) mà (đã) tạo ra chúng (Traditional CI/CD can usually reason about code, configuration, tests, and infrastructure as the primary release objects; ML operations must also manage artifacts whose validity depends on the data and environment that produced them).
DevOps tích hợp và phân phối (có tính) tất định phần mềm (DevOps integrates and delivers deterministic software). MLOps phải quản lý (có tính) không tất định (nondeterministic),
phụ thuộc-dữ liệu các quy trình làm việc (spanning) sự thu thập (acquisition), việc tiền xử lý, mô hình sự đào tạo, sự đánh giá,
sự triển khai, và liên tục việc giám sát thông qua một (có tính) lặp lại (iterative) chu kỳ (đang) kết nối thiết kế, mô hình sự phát-
triển (devel-opment), và các hoạt động (MLOps must manage nondeterministic, data-dependent workflows spanning data acquisition, preprocessing, model training, evaluation, deployment, and continuous monitoring through an iterative cycle connecting design, model devel-opment, and operations). Theo dõi (Trace) (cái) vô cực-vòng lặp (infinity-loop) cấu trúc trong hình 14.1 để xem (như thế nào) những các pha (phases) này phản
hồi (feed back) vào một (cái) (khác) (another) (một cách) liên tục; (cái) vòng lặp (mang) lại (cái) kỷ luật (của) nó (đang) hoạt động hình dạng (Trace the infinity-loop structure in figure 14.1 to see how these phases feed back into one another continuously; the loop gives the discipline its operating shape).
Định nghĩa 14.1: MLOps
Máy Học Các hoạt động (MLOps) là (cái) kỹ thuật kỷ luật (thứ) mà đóng (closes) (cái) phản hồi
vòng lặp giữa mô hình hành vi và dữ liệu thực tế bằng cách (việc) tự động hóa (sự) đào tạo lại, sự xác thực, và
sự triển khai để (in) phản hồi (response) (với) (có thể) đo lường (được) sản xuất sự trôi dạt (Kreuzberger et al. 2023) (Machine Learning Operations (MLOps) is the engineering discipline that closes the feedback loop between model behavior and data reality by automating retraining, validation, and deployment in response to measurable production drift (Kreuzberger et al. 2023)).
1. Tầm quan trọng (Significance): (Cái) chi phí của (việc) không đóng này vòng lặp xuất hiện như (là) cũ (stale) các dự đoán, (được) trì hoãn
sự phát hiện, và (có thể) tránh (được) sự phục hồi (recovery) công việc (The cost of not closing this loop appears as stale predictions, delayed detection, and avoidable recovery work). Sự trôi dạt các ngưỡng, (sự) đào tạo lại các bộ kích hoạt, và trung bình
thời gian để (phục) hồi (recovery) (MTTR) các mục tiêu là đặc thù-sự triển khai các đại lượng (quantities) (được) hiệu chuẩn từ
(cái) doanh nghiệp giá trị của các dự đoán, nhãn sự chậm trễ (delay), sự xác thực rủi ro, và đào tạo lại chi phí (Drift thresholds, retraining triggers, and mean time to recovery (MTTR) targets are deployment-specific quantities calibrated from the business value of predictions, label delay, validation risk, and retraining cost). (Cái)
quan trọng định lượng thói quen là không (phải) một phổ quát (universal) ngưỡng mà (là) (cái) sự kiểm soát vòng lặp: đo lường
sự phân phối sự dịch chuyển, ước lượng (cái) chi phí của sự cũ kỹ (staleness), kích hoạt (sự) đào tạo lại chỉ khi (được) mong đợi
lợi ích vượt quá sự xác thực và (sự) tung ra rủi ro, và xác minh (cái) sự thay thế mô hình trước khi
sự thăng cấp (promotion) (The important quantitative habit is not a universal threshold but the control loop: measure distribution shift, estimate the cost of staleness, trigger retraining only when expected benefit exceeds validation and rollout risk, and verify the replacement model before promotion).
2. Sự khác biệt (Distinction): Không giống như DevOps ((thứ) mà giám sát hệ thống tính khả dụng (availability): thời gian hoạt động, lỗi các tỷ lệ,
độ trễ, và thành công miễn là (as long as) (cái) dịch vụ phản hồi), MLOps phải giám sát (thuộc về) dự đoán
tính chính xác, (thứ) mà có thể (một cách) im lặng xuống cấp (về) (số) không trong khi mọi cơ sở hạ tầng sức khỏe sự kiểm tra
vẫn (có màu) xanh lá cây (Unlike DevOps (which monitors system availability: uptime, error rates, latency, and succeeds as long as the service responds), MLOps must monitor predictive correctness, which can silently degrade to zero while every infrastructure health check stays green).
3. Phổ biến cạm bẫy: Một thường xuyên (frequent) sự ngộ nhận là (rằng) (việc) đào tạo lại trên mới dữ liệu giải quyết (solves) (sự) phân phối
sự dịch chuyển (A frequent misconception is that retraining on new data solves distribu-tion shift). Trong thực tế, (việc) đào tạo lại trên (được) dịch chuyển dữ liệu mà không (cần) (việc) đầu tiên chẩn đoán (cái) nào sự phân phối
(đã) thay đổi (đầu vào các đặc trưng (𝑝(𝑥)), nhãn các mối quan hệ (𝑝(𝑦∣𝑥)), hay cả hai) có thể cố thủ (entrench) (cái)
sự dịch chuyển thay vì sửa chữa nó (In reality, retraining on shifted data without first diagnosing which distribution changed (input features (𝑝(𝑥)), label relationships (𝑝(𝑦∣𝑥)), or both) can entrench the shift rather than correct it). Dữ liệu sự trôi dạt và khái niệm sự trôi dạt yêu cầu khác biệt các sự can thiệp (interventions):
mới (fresh) (việc) lấy mẫu sửa (cái) (trước) (former); (việc) dán nhãn lại dưới hiện tại sự thật-cơ bản (ground-truth) các tiêu chí (criteria) được yêu cầu
cho (cái) (sau) (latter) (Data drift and concept drift require different interventions: fresh sampling fixes the former; relabeling under current ground-truth criteria is required for the latter).
THIẾT KẾ (DESIGN)
MÔ HÌNH (MODEL)
SỰ PHÁT TRIỂN (DEVELOPMENT)
CÁC HOẠT ĐỘNG (OPERATIONS)
• Các yêu cầu Kỹ thuật (Requirements Engineering)
• ML (Các) Trường hợp sử dụng Sự ưu tiên hóa (ML Use-Cases Prioritization)
• Dữ liệu Tính khả dụng Sự kiểm tra (Data Availability Check)
• Dữ liệu Kỹ thuật (Data Engineering)
• ML Mô hình Kỹ thuật (ML Model Engineering)
• Mô hình Việc kiểm thử & Sự xác thực (Model Testing & Validation)
• ML Mô hình Sự triển khai (ML Model Deployment)
• CI/CD Đường ống (CI/CD Pipeline)
• Việc giám sát & Sự kích hoạt (Monitoring & Triggering)
Hình 14.1: (Có tính) lặp lại MLOps Vòng lặp: MLOps mở rộng DevOps các nguyên tắc để quản lý (cái) độc nhất (unique) các thử thách của máy học
các hệ thống, bao gồm dữ liệu việc lập phiên bản, mô hình (sự) đào tạo lại, và liên tục việc giám sát (Figure 14.1: Iterative MLOps Loop: MLOps extends DevOps principles to manage the unique challenges of machine learning systems, including data versioning, model retraining, and continuous monitoring). (Cái) (có tính) lặp lại quy trình làm việc bao quanh (encompasses) dữ liệu
kỹ thuật, mô hình sự phát triển, và đáng tin cậy (reliable) sự triển khai cho (được) duy trì hiệu suất trong sản xuất (The iterative workflow encompasses data engineering, model development, and reliable deployment for sustained performance in production).
(Cái) (thuộc về) hoạt động độ phức tạp và doanh nghiệp rủi ro của (việc) triển khai máy học mà không (có) (có tính) hệ thống
kỹ thuật các thực hành trở nên (trở nên) rõ ràng khi (việc) kiểm tra thế giới-thực sự thất bại các mẫu (The operational complexity and business risk of deploying machine learning without systematic engineering practices becomes clear when examining real-world failure patterns). Xem xét một
(có tính) minh họa (illustrative) bán lẻ sự triển khai trong (đó) (which) một sự gợi ý mô hình ban đầu (initially) thúc đẩy (boosts) doanh số bởi xấp xỉ 15
phần trăm (Consider an illustrative retail deployment in which a recommendation model initially boosts sales by roughly 15 percent). Do (tới) im lặng dữ liệu sự trôi dạt, (cái) mô hình’s độ chính xác xuống cấp qua sáu (các) tháng, (một cách) cuối cùng (việc) giảm thiểu
doanh số bởi vài phần trăm (so) với (so với) (cái) nguyên bản hệ thống (Due to silent data drift, the model’s accuracy degrades over six months, eventually reducing sales by several percent compared to the original system). (Cái) bài toán đi (mà) không bị phát hiện bởi vì
việc giám sát tập trung vào hệ thống thời gian hoạt động thay vì mô hình hiệu suất các số liệu (The problem goes undetected because monitoring focuses on system uptime rather than model performance metrics). Đến (cái) thời điểm (cái) vấn đề
được khám phá trong suốt thường lệ (routine) hàng quý (quarterly) sự phân tích, (cái) (có tính) tích lũy (cumulative) doanh thu tác động trên một cỡ-trung (mid-size) nhà bán lẻ (retailer)
có thể (một cách) có lý (plausibly) đạt (đến) hàng chục của hàng triệu của đô la (By the time the issue is discovered during routine quarterly analysis, the cumulative revenue impact on a mid-size retailer can plausibly reach tens of millions of dollars). Này kịch bản minh họa tại sao MLOps là một doanh nghiệp
sự cần thiết (necessity), không (phải) một (có tính) tùy chọn (optional) tốt nhất thực hành, cho các tổ chức (đang) phụ thuộc vào máy học các hệ thống
cho tới hạn (critical) các hoạt động (This scenario illustrates why MLOps is a business necessity, not an optional best practice, for organizations depending on machine learning systems for critical operations).
14.2.1 (Thuộc về) Nền tảng (Foundational) các nguyên tắc
Đó bán lẻ sự triển khai minh họa một mẫu: mà không (có) (có tính) hệ thống (thuộc về) hoạt động các thực hành, (thậm chí) ngay cả chính xác
các mô hình thất bại trong sản xuất (That retail deployment illustrates a pattern: without systematic operational practices, even accurate models fail in production). Đọc (cái) sự cố (incident) như (là) một gỡ lỗi (debugging) chuỗi (Read the incident as a debugging sequence). Khi doanh thu rớt xuống, (cái) đầu tiên
câu hỏi là liệu (cái) đội (có thể) tái tạo (cái) (được) triển khai mô hình (hay không), (điều) (mà) yêu cầu tính có thể tái tạo (The first question is whether the team can reconstruct the deployed model, which requires reproducibility).
(Cái) tiếp theo câu hỏi là liệu (cái) dữ liệu đường ống, đào tạo công việc, phục vụ con đường, và việc giám sát hệ thống
có các ranh giới rõ ràng đủ để cô lập (isolate) (cái) lỗi (hay không), (điều) (mà) yêu cầu sự phân tách của các mối quan tâm (The next question is whether the data pipeline, training job, serving path, and monitoring system have boundaries clear enough to isolate the fault, which requires separation of concerns). Nếu (các)
phục vụ các đặc trưng không (còn) (nữa) khớp (với) (các) đào tạo các đặc trưng, sự nhất quán trở thành (cái) sự kiểm soát (thứ) mà ngăn chặn
(cái) giống nhau sự cố (khỏi) (việc) trở lại (If the serving features no longer match the training features, consistency becomes the control that prevents the same incident from returning). Nếu sự trôi dạt bắt đầu trước khi người dùng phàn nàn (complain), (có thể) quan sát (được) sự xuống cấp
là (cái) sự kiểm soát (thứ) mà biến (turns) im lặng sự thất bại thành một cảnh báo (If drift begins before users complain, observable degradation is the control that turns silent failure into an alert). Cuối cùng, nếu sự đào tạo lại là (có) thể nhưng đắt đỏ,
nhận thức-chi phí sự tự động hóa quyết định khi (nào) sự can thiệp là (có) giá trị (đáng) (worth) (cái) (thuộc về) hoạt động rủi ro và tính toán chi phí (Finally, if retraining is possible but expensive, cost-aware automation decides when intervention is worth the operational risk and compute cost).
(Các) lâu dài (enduring) các nguyên tắc bên dưới đặt tên (name) những (các) sự kiểm soát đó trong (cái) thứ tự (order) một các hoạt động đội cần chúng (The enduring principles below name those controls in the order an operations team needs them).

14. ML Các hoạt động
773
2
Đồ tạo tác (Artifact):
Một mô hình’s
các trọng số là (cái) (có tính) tất định
đầu ra của một hàm (thứ) mà (của) nó
các đầu vào (mã, dữ liệu, cấu-
hình (config-uration)) không thể được (đảo ngược)-
kỹ thuật lại (reverse-engineered) từ (cái) (đang) kết quả
các tham số (A model’s weights are the deterministic output of a function whose inputs (code, data, config-uration) cannot be reverse-engineered from the resulting parameters).
Hệ quả là (Consequently),
(việc) lập phiên bản chỉ (cái) mã là
một tới hạn sự thất bại chế độ, vì (as) một
đơn-byte (sự) thay đổi trong (cái) đầu-
vào (in-put) dữ liệu có thể (một cách) im lặng thay đổi hàng triệu
của các tham số trong (cái) cuối-
cùng (fi-nal) mô hình (Consequently, versioning only the code is a critical failure mode, as a single-byte change in the in-put data can silently alter mil-lions of parameters in the fi-nal model). Mà không (có) (việc) lập phiên-
bản (version-ing) tất cả bốn đồ tạo tác (các) lớp (classes)
(mã, dữ liệu, cấu hình, và môi-
trường (envi-ronment)), thực sự tính có thể tái tạo (reproducibil-ity)
là không thể (Without version-ing all four artifact classes (code, data, config, and envi-ronment), true reproducibil-ity is impossible).
14.2.1.1 Tính có thể tái tạo (Reproducibility)
Mọi đồ tạo tác2 (thứ) mà ảnh hưởng (đến) mô hình hành vi phải được lập phiên bản và (có thể) theo dõi (traceable) (Every artifact2 that influences model behavior must be versioned and traceable). Này nguyên tắc
mở rộng vượt ra ngoài mã việc lập phiên bản để bao quanh (encompass) dữ liệu, các cấu hình, và các môi trường (This principle extends beyond code versioning to encompass data, configurations, and environments). Phương trình 14.1
biểu diễn (expresses) này sự phụ thuộc (một cách) chính thức (formally):
Mô hình Đầu ra (Output) = 𝑓(Mã𝑣, Dữ liệu𝑣, Cấu hình𝑣, Môi trường𝑣)
(14.1)
nơi mỗi chỉ số dưới 𝑣 biểu thị một cụ thể phiên bản (where each subscript 𝑣denotes a specific version). Một mô hình không thể được tái tạo trừ khi tất cả bốn
các thành phần (components) được nắm bắt (captured) (A model cannot be reproduced unless all four components are captured). Các công cụ (thứ) mà triển khai này nguyên tắc khác nhau trong sự triển khai nhưng chia sẻ (cái)
chung mục tiêu của (việc) kích hoạt hoàn chỉnh tính có thể tái tạo (Tools that implement this principle vary in implementation but share the common goal of enabling complete reproducibility). Chúng bao gồm phiên bản (sự) kiểm soát các hệ thống, dữ liệu
việc lập phiên bản các nền tảng, và cấu hình các nhà quản lý (These include version control systems, data versioning platforms, and configuration managers).
14.2.1.2 Sự phân tách của các mối quan tâm (Separation of concerns)
Sự phân tách của các mối quan tâm phân rã (decomposes) MLOps các hệ thống thành khác biệt (thuộc về) chức năng các lớp (thứ) mà có thể tiến hóa
(một cách) độc lập, như bảng 14.1 cho thấy (Separation of concerns decomposes MLOps systems into distinct functional layers that can evolve independently, as table 14.1 shows):
Bảng 14.1: MLOps Sự phân tách của Các mối quan tâm: Mỗi lớp giải quyết một khác biệt trách nhiệm và tiến hóa tại khác biệt các tốc độ (rates), từ
ổn định phần cứng các nền tảng xuyên qua cấp độ-mô hình các thành phần (thứ) mà thay đổi với mỗi thí nghiệm (Table 14.1: MLOps Separation of Concerns: Each layer addresses a distinct responsibility and evolves at different rates, from stable hardware foundations through model-level components that change with each experiment). Này sự phân tách kích hoạt
độc lập (việc) mở rộng quy mô và các bản cập nhật, (việc) giảm thiểu vụ nổ bán kính (blast radius) khi các sự thay đổi được yêu cầu (This separation enables independent scaling and updates, reducing blast radius when changes are required).
Lớp
Trách nhiệm
Tính ổn định (Stability)
Dữ liệu Lớp
Đặc trưng tính toán, lưu trữ, việc phục vụ
Thay đổi với dữ liệu lược đồ (schema) sự tiến hóa
Đào tạo Lớp
Mô hình sự phát triển, siêu tham số sự tối ưu hóa
Thay đổi với thuật toán nghiên cứu
Việc phục vụ Lớp
Sự suy luận, việc mở rộng quy mô, độ trễ sự quản lý
Thay đổi với lưu lượng truy cập các mẫu
Việc giám sát Lớp
Sự trôi dạt sự phát hiện, hiệu suất việc theo dõi
Thay đổi với doanh nghiệp các yêu cầu
14.2.1.3 Sự nhất quán mệnh lệnh (Consistency imperative)
(Cái) sự phân tách trong bảng 14.1 kích hoạt các đội để cập nhật việc phục vụ cơ sở hạ tầng mà không (cần) (việc) đào tạo lại các mô hình,
sửa đổi việc giám sát các ngưỡng mà không (cần) (việc) tái triển khai, và tiến hóa dữ liệu các đường ống trong khi (đang) duy trì
mô hình tính tương thích (compatibility) (The separation in table 14.1 enables teams to update serving infrastructure without retraining models, modify monitoring thresholds without redeploying, and evolve data pipelines while maintaining model compatibility). Đó sự độc lập là an toàn chỉ khi đào tạo và phục vụ các môi trường
xử lý dữ liệu (một cách) giống hệt nhau (identically), (việc) làm (cho) đào tạo-phục vụ sự ngang bằng một sự nhất quán mệnh lệnh (That independence is safe only when training and serving environments process data identically, making training-serving parity a consistency imperative). (Cái) (thuộc về) tài chính
tác động của này sự không nhất quán (inconsistency) được nắm bắt trong phương trình 14.2 (The financial impact of this inconsistency is captured in equation 14.2):
Sự sai lệch (Skew) Chi phí = Cơ sở (Base) Lỗi Tỷ lệ × Truy vấn Khối lượng × Lỗi Tác động
(14.2)
nơi Cơ sở Lỗi Tỷ lệ là (cái) phần (fraction) của các truy vấn bị ảnh hưởng bởi đào tạo-phục vụ sự sai lệch, Truy vấn Khối lượng là
(cái) số lượng của các truy vấn mỗi thời gian chu kỳ (period), và Lỗi Tác động là (cái) chi phí cho mỗi bị lỗi (erroneous) dự đoán (where Base Error Rate is the fraction of queries affected by training-serving skew, Query Volume is the number of queries per time period, and Error Impact is the cost per erroneous prediction).
Cho một hệ thống (đang) phục vụ 1,000,000 các truy vấn/ngày với 1 phần trăm (do) sự sai lệch-gây ra (skew-induced) các lỗi (đang) có giá $0.10 mỗi (cái),
hàng năm sự sai lệch chi phí đạt (đến) $365,000 (For a system serving 1,000,000 queries/day with 1 percent skew-induced errors costing $0.10 each, annual skew cost reaches $365,000). Điều này định lượng (quantifies) tại sao sự nhất quán các cơ chế đại diện (cho) các sự đầu-
tư (invest-ments) với (có thể) đo lường (được) các lợi nhuận (returns) (This quantifies why consistency mechanisms represent invest-ments with measurable returns). Những các cơ chế này bao gồm đặc trưng các cửa hàng, (được) chia sẻ việc tiền xử lý
mã, và sự xác thực các sự kiểm tra (checks) (These mechanisms include feature stores, shared preprocessing code, and validation checks).
14.2.1.4 (Có thể) quan sát (được) sự xuống cấp
ML các hệ thống phải làm im lặng các sự thất bại (trở nên) có thể nhìn thấy được thông qua liên tục sự đo lường (ML systems must make silent failures visible through continuous measurement). Mô hình hiệu suất
xuống cấp dọc theo một thể liên tục (continuum) thay vì thất bại (một cách) rời rạc (discretely), và mỗi sự thất bại chế độ có một khác biệt
thời gian chữ ký (signature) (thứ) mà quyết định cả (như thế nào) nó được phát hiện (như thế nào) và (như thế nào) (cái) hệ thống nên phản hồi (Model performance degrades along a continuum rather than failing discretely, and each failure mode has a distinct time signature that dictates both how it is detected and how the system should respond). Bảng 14.2
ghép cặp (pairs) mỗi sự xuống cấp loại với (cái) bộ phát hiện (detector) (thứ) mà bắt (catches) nó trên (của) riêng nó thời gian quy mô (timescale) và (cái) (đang) khớp
sự phản hồi: ngưỡng các cảnh báo bắt một đột ngột (sudden) sự rớt (xuống) và kích hoạt quay lui, trong khi chậm xu hướng sự phân tích
bắt (sự) dần dần sự trôi dạt và lên lịch (sự) đào tạo lại (Table 14.2 pairs each degradation type with the detector that catches it on its own timescale and the matching response: threshold alerts catch a sudden drop and trigger rollback, while slow trend analysis catches gradual drift and schedules retraining).
14.2.1.5 Nhận thức-chi phí sự tự động hóa
Nhận thức-chi phí sự tự động hóa nên cân bằng (thuộc về) tính toán các chi phí chống lại độ chính xác các sự cải thiện (Cost-aware automation should balance computational costs against accuracy improvements). Phương-
trình (Equa-tion) 14.3 mô hình hóa này sự đánh đổi (Equation 14.3 models this trade-off):
Đào tạo lại nếu (Retrain if): ΔĐộ chính xác × Giá trị cho mỗi Điểm > Đào tạo Chi phí + Sự triển khai Rủi ro
(14.3)

774
14.2 Các nguyên tắc và Các nền tảng
Bảng 14.2: Sự xuống cấp Sự phát hiện Các chiến lược: Khác biệt sự thất bại các chế độ yêu cầu khác biệt việc giám sát các cách tiếp cận và sự phản hồi
các chiến lược (Table 14.2: Degradation Detection Strategies: Different failure modes require different monitoring approaches and response strategies). (Thuộc về) Thống kê các bài kiểm tra phát hiện sự phân phối các sự dịch chuyển trước khi hiệu suất xuống cấp (một cách) có thể nhìn thấy được, trong khi hiệu suất việc giám sát bắt
các vấn đề (thứ) mà lảng tránh (evade) (thuộc về) thống kê sự phát hiện (Statistical tests detect distribution shifts before performance degrades visibly, while performance monitoring catches issues that evade statistical detection). (Có tính) thích ứng các ngưỡng ngăn chặn sai (false) các báo động trong khi (đang) duy trì độ nhạy (sensitivity) đối với (tới) đích thực (genuine)
sự xuống cấp (Adaptive thresholds prevent false alarms while maintaining sensitivity to genuine degradation).
Sự xuống cấp Loại
Sự phát hiện Cơ chế
Sự phản hồi Chiến lược
Đột ngột độ chính xác sự rớt (xuống)
Ngưỡng các cảnh báo
Ngay lập tức sự quay lui
Dần dần sự trôi dạt
Xu hướng sự phân tích
Được lên lịch sự đào tạo lại
Phân nhóm (Subgroup) sự xuống cấp
Đoàn hệ (Cohort) việc giám sát
Được nhắm mục tiêu dữ liệu sự thu thập
Độ trễ sự gia tăng
Phần trăm (Percentile) việc theo dõi
Cơ sở hạ tầng việc mở rộng quy mô
Này nguyên tắc hướng dẫn (cái) thiết kế của (sự) đào tạo lại các bộ kích hoạt, sự xác thực các ngưỡng, và sự triển khai
các chiến lược (được) kiểm tra xuyên suốt này chương (This principle guides the design of retraining triggers, validation thresholds, and deployment strategies examined throughout this chapter). (Các) cụ thể các giá trị khác nhau tùy (by) miền, nhưng (cái) khuôn khổ
cho (việc) đưa ra (making) có nguyên tắc sự đánh đổi các quyết định vẫn không đổi (The specific values vary by domain, but the framework for making principled trade-off decisions remains constant). Phần 11 dẫn xuất (derives) (cái) hoàn chỉnh (thuộc về) kinh tế
mô hình với (đã) được giải (worked) các ví dụ (đang) cho thấy (như thế nào) để tính toán tối ưu (sự) đào tạo lại các khoảng thời gian (Section 11 derives the complete economic model with worked examples showing how to calculate optimal retraining intervals). Một khi (cái) (thuộc về) nhân quả (causal)
chuỗi là rõ ràng, (cái) năm các nguyên tắc có thể phục vụ như (là) một nhỏ gọn sự đánh giá khuôn khổ cho các công cụ và các thực hành (Once the causal chain is clear, the five principles can serve as a compact evaluation framework for tools and practices).
(Cái) (đang) tổ chức tuyên bố (claim) của bảng 14.3 là (rằng) mỗi nguyên tắc là chỉ (có tính) hoạt động (operational) một khi nó được gắn (tied) (với) một cụ thể
(có thể) đo lường (được) số liệu: (việc) ghép cặp mọi nguyên tắc với (của) nó chính số liệu, từ đồ tạo tác băm (hash) (tới) ròng (net) (sự) đào tạo lại
giá trị, là (những) gì làm (cái) khuôn khổ (trở nên) có thể kiểm toán thay vì mang tính khát vọng (aspirational) (The organizing claim of table 14.3 is that each principle is only operational once it is tied to a concrete measurable metric: pairing every principle with its key metric, from artifact hash to net retraining value, is what makes the framework auditable rather than aspirational).
Bảng 14.3: MLOps Các nguyên tắc Tóm tắt: Nhanh tham khảo (reference) cho (cái) năm (thuộc về) nền tảng các nguyên tắc (thứ) mà hướng dẫn tất cả MLOps (thuộc về) công cụ (tooling) và
thực hành các quyết định (Table 14.3: MLOps Principles Summary: Quick reference for the five foundational principles that guide all MLOps tooling and practice decisions).
Nguyên tắc
Cốt lõi Sự thấu hiểu (Insight)
Chính Số liệu
Tính có thể tái tạo
Lập phiên bản tất cả các đồ tạo tác
Hoàn chỉnh đồ tạo tác băm (hash)
Sự phân tách của các mối quan tâm
Độc lập lớp sự tiến hóa
Lớp (sự) ghép nối (coupling) điểm số
Sự nhất quán
Đào tạo bằng (equals) Phục vụ
Đặc trưng sự sai lệch tỷ lệ
(Có thể) quan sát (được) sự xuống cấp
Làm các sự thất bại có thể nhìn thấy được
Thời gian để (tới) sự phát hiện
Nhận thức-chi phí sự tự động hóa
Tối ưu hóa tổng chi phí
Ròng (Net) (sự) đào tạo lại giá trị
(Như thế nào) những các nguyên tắc này biểu hiện (manifest) trong thực tế phụ thuộc vào (cái) khối lượng công việc (How these principles manifest in practice depends on the workload). Một sự gợi ý hệ thống
trôi dạt hàng ngày khi người dùng các sở thích (preferences) dịch chuyển; một TinyML mô hình (được) triển khai trên nhúng (embedded) phần cứng có thể chạy
không bị thay đổi (unchanged) cho (các) tháng (A recommendation system drifts daily as user preferences shift; a TinyML model deployed on embedded hardware may run unchanged for months). (Cái) việc giám sát chiến lược phải khớp (với) (cái) nguyên mẫu (archetype) (The monitoring strategy must match the archetype).
Ngọn hải đăng 14.1: Việc giám sát chiến lược bởi nguyên mẫu
(Các) chủ đạo sự thất bại các chế độ và việc giám sát các ưu tiên khác nhau (xuyên) qua khối lượng công việc các nguyên mẫu (The dominant failure modes and monitoring priorities differ across workload archetypes).
Bảng 14.4 so sánh bốn (có tính) đại diện các nguyên mẫu theo sự trôi dạt mẫu, việc giám sát số liệu, và
ví dụ (sự) đào tạo lại bộ kích hoạt (Table 14.4 compares four representative archetypes by drift pattern, monitoring metric, and example retraining trigger):
Bảng 14.4: Việc giám sát chiến lược bởi khối lượng công việc nguyên mẫu: (Có tính) minh họa bắt đầu các điểm cho việc giám sát chiến lược (Table 14.4: Monitoring strategy by workload archetype: Illustrative starting points for monitoring strategy). Thực tế
các ngưỡng phải được hiệu chuẩn với (cái) (sự) triển khai’s nhãn sự chậm trễ, lưu lượng truy cập khối lượng, doanh nghiệp rủi ro, và cảnh báo-sự mệt mỏi (alert-fatigue) ngân sách (Real thresholds must be calibrated to the deployment’s label delay, traffic volume, business risk, and alert-fatigue budget).
Nguyên mẫu
Chủ đạo Sự trôi dạt Mẫu
Chính Việc giám sát
Số liệu
Ví dụ (Sự) Đào tạo lại Bộ kích hoạt
ResNet-50
(Tính toán Quái thú (Beast))
(Thuộc về) thị giác (Visual) sự phân phối sự dịch chuyển
(ánh sáng, máy ảnh, mới đối tượng
các lớp)
Độ chính xác trên (được) giữ lại (holdout) tập hợp
(sự thật cơ bản (có) sẵn)
Độ chính xác rớt (xuống) > 2% từ đường cơ sở
(∼hàng tháng cho ổn định các miền)
GPT-2
(Băng thông
Con heo (Hog))
Từ vựng sự trôi dạt, chủ đề sự dịch chuyển,
(đang) nổi lên (emerging) các thực thể
Độ bối rối (Perplexity) trên sống (live) lưu lượng truy cập
(không (cần) sự thật cơ bản
(được) yêu cầu (needed))
Độ bối rối gia tăng > 10%; mới
từ vựng (được) phát hiện (∼hàng tuần cho
tin tức các miền)
DLRM (Thưa thớt
Sự phân tán (Scatter))
Người dùng hành vi sự dịch chuyển, mục (item)
danh mục (catalog) sự xáo trộn (churn), lạnh-khởi động các mục
CTR/CVR delta
so với (vs.) (thuộc về) lịch sử các đoàn hệ
Sự tương tác (Engagement) rớt (xuống) > 5%; danh mục
(sự) làm mới (refresh) (∼hàng ngày cho thương mại điện tử)
DS-CNN (Tí hon
Sự ép buộc)
(Thuộc về) âm thanh môi trường (sự) thay đổi
(tiếng ồn sàn (floor) sự dịch chuyển)
(Chu) kỳ (Làm) việc (Duty cycle)
(các sự thức dậy (wakeups)/giờ) + sai
tích cực (positive) tỷ lệ
Sai thức (dậy) tỷ lệ > 1%; pin (sự) cạn kiệt (drain)
vượt quá thông số kỹ thuật (spec) (∼hàng quý OTA
cập nhật)

14. ML Các hoạt động
775
3
Dữ liệu Sự trôi dạt (Drift):
Khái niệm-
sự trôi dạt và dữ liệu-luồng nghiên cứu
(đã) chính thức hóa (formalized) (cái) bài toán rằng
một mô hình’s mục tiêu mối quan hệ
có thể thay đổi sau (khi) sự triển khai
(Widmer và Kubat 1996;
Gama và cộng sự.
2014).
Trong (có tính) đối-
kháng (ad-versarial) các miền như
thư rác, gian lận, và (sự) lạm dụng (abuse) sự phát-
hiện (de-tection), (cái) sự phân phối có thể
(một cách) chủ động (actively) thích ứng để (in) phản hồi
(với) (cái) mô hình, (việc) làm (cho) liên tục-
tục việc giám sát và (sự) đào tạo-
lại một (thuộc về) cấu trúc yêu cầu
thay vì một (thuộc về) hoạt động sự xa-
xỉ (lux-ury).
4
DVC (Dữ liệu Phiên bản Sự kiểm-
soát (Con-trol)): DVC mang (đến) Giống-như-Git (Git-like) việc lập phiên-
bản (ver-sioning) cho các tập dữ liệu và mô hình
các đồ tạo tác (Iterative 2024), (việc) giải-
quyết (solv-ing) (cái) đồ tạo tác khoảng trống (thứ) mà phương-
trình 14.1 chính thức hóa: mà không (có)
dữ liệu việc lập phiên bản, (cái) Dữ liệu𝑣
số hạng (term) là không thể phục hồi (unrecoverable), và không
(có) (sự) kết hợp của mã các (sự) cam kết (commits)
(có thể) tái cấu trúc (reconstruct) (cái) mô hình (thứ) mà
đã được triển khai.
Các hệ thống sự thấu hiểu: Sự thật cơ bản tính khả dụng quyết định việc giám sát chiến lược (Systems insight: Ground truth availability determines monitoring strategy). ResNet-50 (hình ảnh
sự phân loại) có thể sử dụng (mang tính) rõ ràng (explicit) các nhãn; GPT-2 phụ thuộc vào (có tính) đại diện (proxy) các số liệu (độ bối rối); DLRM sử dụng
(mang tính) ngầm hiểu (implicit) phản hồi (các cú nhấp chuột (clicks)); DS-CNN, một (theo) chiều sâu-có thể tách rời (depthwise-separable) (thuộc về) tích chập (convolutional) thần kinh mạng lưới
(CNN), giám sát (thuộc về) hoạt động các số liệu (năng lượng, sai (các) tích cực (positives)) (ResNet-50 (image classification) can use explicit labels; GPT-2 relies on proxy metrics (perplexity); DLRM uses implicit feedback (clicks); DS-CNN, a depthwise-separable convolutional neural network (CNN), monitors operational metrics (energy, false positives)). (Cái) (có tính) minh họa (sự) đào tạo lại nhịp điệu (cadence)
trải rộng (spans) xấp xỉ hai các bậc của độ lớn, từ hàng ngày sự gợi ý các bản cập nhật đến (những) (bản cập nhật) chậm hơn nhiều
(thuộc về) (được) nhúng-thiết bị các bản cập nhật (The illustrative retraining cadence spans roughly two orders of magnitude, from daily recommendation updates to much slower embedded-device updates).
Những các nguyên tắc này phản hồi (đối với) (các) (đang) lặp lại các thử thách: dữ liệu sự trôi dạt3, tính có thể tái tạo các sự thất bại (Schelter và
cộng sự. 2018), và im lặng sau sự triển khai sự xuống cấp (These principles respond to recurring challenges: data drift3, reproducibility failures (Schelter et al. 2018), and silent postdeployment degradation). Những (điều này) (một cách) tập thể (collectively) thúc đẩy (motivate) (các) (được) chuyên môn hóa các công cụ
và các quy trình làm việc (đang) phân biệt MLOps (với) truyền thống DevOps (These collectively motivate the specialized tools and workflows distinguishing MLOps from traditional DevOps). (Cái) sự phân kỳ (divergence) được thúc đẩy bởi (cái)
im lặng sự thất bại bài toán (được) giới thiệu tại (cái) chương’s (sự) mở đầu: hệ thống sức khỏe không thể được đo lường bằng
thời gian hoạt động hay độ trễ đơn độc (alone) (The divergence is driven by the silent failure problem introduced at the chapter’s opening: system health cannot be measured by uptime or latency alone). (Thuộc về) Hoạt động kỷ luật trong ML yêu cầu (việc) giám sát (các) (thuộc về) thống kê (các) thuộc tính
của dữ liệu các sự phân phối và mô hình các đầu ra, (việc) dịch chuyển (cái) sự tập trung từ “liệu (is) (cái) máy chủ (đang) chạy?” sang “liệu
(cái) hệ thống vẫn thông minh?” (Operational discipline in ML requires monitoring the statistical properties of data distributions and model outputs, shifting the focus from “is the server running?” to “is the system still intelligent?”)
Bảng 14.5 đối chiếu (contrasts) (các) mục tiêu, (các) phương pháp luận (methodologies), (các) chính công cụ, và (các) điển hình kết quả của DevOps
và MLOps, (việc) minh họa (như thế nào) những ML-đặc thù (ML-specific) các yêu cầu này đòi hỏi (demand) khác biệt (thuộc về) hoạt động các thực hành (Table 14.5 contrasts the objectives, methodologies, primary tools, and typical outcomes of DevOps and MLOps, illustrating how these ML-specific requirements demand distinct operational practices).
MLOps phối hợp (coordinates) một rộng hơn (các) bên liên quan hệ sinh thái và giới thiệu (được) chuyên môn hóa các thực hành như
dữ liệu việc lập phiên bản4, mô hình việc lập phiên bản, và mô hình việc giám sát (thứ) mà mở rộng vượt ra ngoài truyền thống DevOps
phạm vi (MLOps coordinates a broader stakeholder ecosystem and introduces specialized practices such as data versioning4, model versioning, and model monitoring that extend beyond traditional DevOps scope).
Bảng 14.5: MLOps so với DevOps: MLOps mở rộng DevOps các nguyên tắc để giải quyết (cái) độc nhất các yêu cầu của máy học
các hệ thống, bao gồm dữ liệu và mô hình việc lập phiên bản, và liên tục việc giám sát cho mô hình hiệu suất và dữ liệu sự trôi dạt (Table 14.5: MLOps vs. DevOps: MLOps extends DevOps principles to address the unique requirements of machine learning systems, including data and model versioning, and continuous monitoring for model performance and data drift). MLOps
phối hợp một rộng hơn (khoảng) phạm vi của các bên liên quan và nhấn mạnh tính có thể tái tạo và tính có thể mở rộng quy mô vượt ra ngoài truyền thống phần mềm
sự phát triển các quy trình làm việc (MLOps coordinates a broader range of stakeholders and emphasizes reproducibility and scalability beyond traditional software development workflows).
Khía cạnh (Aspect)
DevOps
MLOps
Mục tiêu
(Việc) Hợp lý hóa (Streamlining) phần mềm sự phát triển và
các hoạt động các quy trình
(Việc) Tối ưu hóa (cái) vòng đời của máy học các mô hình
Phương pháp luận
Liên tục Sự Tích hợp và Liên tục Sự Phân phối
(CI/CD) cho phần mềm sự phát triển
Tương tự như CI/CD nhưng tập trung vào máy học
các quy trình làm việc
Chính
Các công cụ
Phiên bản sự kiểm soát (Git), CI/CD các công cụ (Jenkins, Travis
CI), Cấu hình sự quản lý (Ansible, Puppet)
Dữ liệu việc lập phiên bản các công cụ, Mô hình (sự) đào tạo và sự triển khai
các công cụ, CI/CD các đường ống (được) điều chỉnh (tailored) cho ML
Chính
Các mối quan tâm
Mã sự tích hợp, Việc kiểm thử, Phát hành sự quản lý,
Sự tự động hóa, Cơ sở hạ tầng như (là) mã
Dữ liệu sự quản lý, Mô hình việc lập phiên bản, Thí nghiệm
việc theo dõi, Mô hình sự triển khai, Tính có thể mở rộng quy mô của ML
các quy trình làm việc
Điển hình
Các kết quả
Nhanh hơn và nhiều đáng tin cậy hơn phần mềm các sự phát hành,
(Được) Cải thiện sự cộng tác giữa sự phát triển và
các hoạt động các đội
Hiệu quả sự quản lý và sự triển khai của máy
học các mô hình, (Được) Tăng cường sự cộng tác giữa dữ liệu
các nhà khoa học và các kỹ sư
Này (được) mở rộng phạm vi biến (turns) mô hình (sự) hoạt động (operation) thành một phản hồi vòng lặp thay vì một sự phát hành đường ống (This expanded scope turns model operation into a feedback loop rather than a release pipeline).
Điểm kiểm tra 14.1: (Cái) MLOps vòng lặp
MLOps không (phải) (là) tuyến tính; nó là (có tính) vòng tròn (circular).
(Cái) Phản hồi Chu kỳ
□(Việc) Đóng (cái) vòng lặp: (Như thế nào) sản xuất các số liệu (ví dụ, sự trôi dạt các cảnh báo) kích hoạt mới
đào tạo các chu kỳ (như thế nào)?
□(Được) Tự động hóa sự đào tạo lại: Liệu (is) (của) bạn đường ống mạnh mẽ (robust) đủ để đào tạo lại và triển khai một mô hình
mà không (có) con người sự can thiệp (intervention) (hay không)?
Các Đồ tạo tác
□Việc lập phiên bản: Liệu (are) bạn (có đang) lập phiên bản Dữ liệu + Mã + Mô hình + Môi trường (cùng) với nhau (hay không)?
(Cái) sự tiến hóa từ DevOps sang MLOps phản ánh (reflects) một cốt lõi sự thật: máy học các hệ thống thất bại (một cách) khác-
biệt (differ-ently) (so) với truyền thống phần mềm (The evolution from DevOps to MLOps reflects a core truth: machine learning systems fail differ-ently than traditional software). Nơi DevOps giải quyết sự triển khai và việc mở rộng quy mô các thử thách cho

776
14.3 Kỹ thuật Nợ
5
Kỹ thuật Nợ: Ward
Cunningham’s 1992 WyCash
kinh nghiệm báo cáo (đã) giới thiệu
(cái) nợ phép ẩn dụ (metaphor) cho thiết-
thực (ex-pedient) mã và (được) trì hoãn
sự hợp nhất (consolidation) (Cunningham
1992). Trong ML, (cái) nợ cộng-
dồn (com-pounds) (một cách) im lặng thông qua dữ liệu
và mô hình các sự phụ thuộc (thứ) mà
thông thường đơn vị các bài kiểm tra và
mã (các) sự đánh giá (reviews) không thể phát hiện:
một hoàn hảo đường ống xuống cấp
không (phải) bởi vì mã (đã) thay đổi mà
bởi vì (cái) thế giới (đã thay đổi) (did). (Cái)
ML Bài kiểm tra Điểm số (Test Score) bảng đánh giá (rubric) (Breck và
cộng sự. 2017) làm điều này nợ (trở nên) rõ-
ràng (ex-plicit) thông qua 28 sản xuất-
sự sẵn sàng (readiness) các bài kiểm tra (được) nhóm thành
dữ liệu, mô hình, cơ sở hạ tầng,
và việc giám sát các phần.
sự tự động hóa (automation)
thủ công (manual)
20 tuần (20w)
Tích lũy thủ công công việc vượt-
qua (over-takes) (cái) một-lần sự tự động hóa sự đầu-
tư (in-vestment) gần tuần 20.
(có tính) tất định mã, MLOps phải đương đầu (contend) với các hệ thống (thứ) mà tích lũy (những) ẩn độ phức tạp thông qua
dữ liệu các sự phụ thuộc, mô hình các sự tương tác, và (đang) tiến hóa các yêu cầu (deterministic code, MLOps must contend with systems that accumulate hidden complexity through data dependencies, model interactions, and evolving requirements). Những (cái) độc nhất sự thất bại (các) chế độ này,
(một cách) tập thể (được) gọi (termed) (là) kỹ thuật nợ, hình thành một (thuộc về) chẩn đoán (diagnostic) từ vựng (thứ) mà giải thích tại sao MLOps yêu cầu
(được) chuyên môn hóa cơ sở hạ tầng (These unique failure modes, collectively termed technical debt, form a diagnostic vocabulary that explains why MLOps requires specialized infrastructure). Việc hiểu ranh giới (sự) xói mòn (erosion) tiết lộ tại sao (có tính) mô đun (modular) đường ống thiết kế
là cần thiết (Understanding boundary erosion reveals why modular pipeline design is necessary). (Việc) Nhận ra sự sửa chữa (correction) các thác (cascades) làm rõ tại sao việc lập phiên bản và quay lui là (thiết) yếu (Recognizing correction cascades clarifies why versioning and rollback are essential).
(Việc) Nhận diện (những) chưa được khai báo (undeclared) (những) người tiêu dùng (consumers) biện minh (justifies) (cho) nghiêm ngặt (strict) giao diện các hợp đồng (Identifying undeclared consumers justifies strict interface contracts). Những các mẫu này là (những) (có tính) cụ thể
sự thất bại các chế độ thúc đẩy mọi cơ sở hạ tầng thành phần chúng ta kiểm tra (về) sau (These patterns are the concrete failure modes motivating every infrastructure component we examine later).
Mỗi (sự) lặp (iteration) qua (cái) vòng lặp có thể giới thiệu dữ liệu các sự phụ thuộc, mô hình các sự tương tác, và cấu-
hình (config-uration) sự trôi dạt vô hình (đối với) tiêu chuẩn phần mềm việc kiểm thử (Each iteration through the loop can introduce data dependencies, model interactions, and config-uration drift invisible to standard software testing). Những (đang) tích lũy (accumulating) các chi phí đó là kỹ thuật nợ: một
khuôn khổ cho (việc) chuyển đổi im lặng ML sự thất bại (các) chế độ thành (có thể) định lượng (được) (quantifiable) (thuộc về) kỹ thuật các khoản nợ (liabilities) (Those accumulating costs are technical debt: a framework for converting silent ML failure modes into quantifiable engineering liabilities).
14.3 Kỹ thuật Nợ
(Các) im lặng sự thất bại các chế độ (được) thiết lập (sớm) hơn (earlier) biểu hiện (một cách) cụ thể như (là) kỹ thuật nợ (Sculley và cộng sự.
2015): dữ liệu các sự thay đổi, mô hình các sự tương tác, và (đang) tiến hóa các yêu cầu gây ra (sự) dần dần sự xuống cấp (thứ) mà
cộng dồn (compounds) qua thời gian (The silent failure modes established earlier manifest concretely as technical debt (Sculley et al. 2015): data changes, model interactions, and evolving requirements cause gradual degradation that compounds over time). Không giống như mã các lỗi (bugs) (thứ) mà kích hoạt ngăn xếp (stack) (các) dấu vết (traces), những các sự thất bại này tích lũy (một cách) vô hình
(xuyên) qua nhiều hệ thống các thành phần, (việc) đòi hỏi (thuộc về) kỹ thuật các cách tiếp cận (được) thiết kế (một cách) đặc thù cho
(thuộc về) xác suất (probabilistic) các hệ thống (Unlike code bugs that trigger stack traces, these failures accumulate invisibly across multiple system components, demanding engineering approaches designed specifically for probabilistic systems). (Được) đề xuất (một cách) nguyên bản (Originally) trong phần mềm kỹ thuật vào (các) năm 19905, (cái) kỹ thuật nợ
phép ẩn dụ so sánh các lối tắt (shortcuts) trong sự triển khai (với) (thuộc về) tài chính nợ, (việc) đánh đổi ngắn-hạn vận tốc (velocity) cho
(đang) diễn ra (ongoing) lãi (interest) các khoản thanh toán (payments) trong (sự) bảo trì (maintenance), (sự) tái cấu trúc (refactoring), và (thuộc về) hệ thống rủi ro (Cunningham 1992) (Originally proposed in software engineering in the 1990s5, the technical debt metaphor compares shortcuts in implementation to financial debt, trading short-term velocity for ongoing interest payments in maintenance, refactoring, and systemic risk (Cunningham 1992)). Trong
ML, này nợ mở rộng vượt ra ngoài mã để bao gồm “ẩn” các chi phí độc nhất đối với (tới) (thuộc về) thống kê việc lập mô hình và dữ liệu
các sự phụ thuộc (In ML, this debt extends beyond code to include “hidden” costs unique to statistical modeling and data dependencies). (Có tính) hệ thống sự đánh giá các bảng đánh giá (rubrics), (chẳng) hạn như (cái) ML Bài kiểm tra Điểm số (Breck và cộng sự. 2017), cung cấp
các khuôn khổ cho (việc) định lượng này nợ và (việc) đánh giá sản xuất sự sẵn sàng (xuyên) qua dữ liệu, mô hình, và
cơ sở hạ tầng các thành phần (Systematic evaluation rubrics, such as the ML Test Score (Breck et al. 2017), provide frameworks for quantifying this debt and assessing production readiness across data, model, and infrastructure components).
Định nghĩa 14.2: Kỹ thuật nợ trong ML
Kỹ thuật Nợ trong Máy Học là (cái) (đang) tích lũy bảo trì chi phí (được) tạo ra bởi ngầm (hiểu)
dữ liệu các sự phụ thuộc, (bị) vướng víu (entangled) các đặc trưng, và chưa được khai báo (những) người tiêu dùng trong ML các hệ thống, nơi (cái)
“lãi” cộng dồn như (là) im lặng độ chính xác sự xuống cấp thay vì chậm hơn sự phát triển vận tốc (Technical Debt in Machine Learning is the accumulating maintenance cost created by implicit data dependencies, entangled features, and undeclared consumers in ML systems, where the “interest” compounds as silent accuracy degradation rather than slower development velocity).
1. Tầm quan trọng: Google’s sự phân tích của sản xuất ML các hệ thống lập luận (argues) rằng mô hình mã là
chỉ một nhỏ phần (fraction) của (cái) (đang) bao quanh (surrounding) hệ thống; (cái) lớn hơn (thuộc về) hoạt động bề mặt bao gồm
dữ liệu sự thu thập (collection), đặc trưng sự trích xuất (extraction), cấu hình, việc phục vụ cơ sở hạ tầng, việc giám sát, và
quy trình (process) sự quản lý (Sculley và cộng sự. 2015) (Google’s analysis of production ML systems argues that model code is only a small fraction of the surrounding system; the larger operational surface includes data collection, feature extraction, configuration, serving infrastructure, monitoring, and process management (Sculley et al. 2015)). ML-đặc thù nợ (những) người thúc đẩy (drivers) cộng dồn điều này:
(việc) thay đổi một đầu vào đặc trưng có thể (một cách) im lặng dịch chuyển (cái) (đã) học được sự biểu diễn (representation) của mọi (đặc trưng) khác
đặc trưng (sự vướng víu (entanglement)), một mô hình (được) đào tạo để sửa (correct) (cái) mô hình khác’s các lỗi tạo ra một mong manh
sự phụ thuộc chuỗi (sự sửa chữa (correction) các thác (cascades)), và hạ nguồn các hệ thống (đang) tiêu thụ mô hình
các đầu ra mà không (có) (mang tính) rõ ràng các hợp đồng trở thành chưa được khai báo (những) người tiêu dùng (thứ) mà hỏng (một cách) im lặng
khi (cái) mô hình được cập nhật (ML-specific debt drivers compound this: changing one input feature can silently shift the learned representation of every other feature (entanglement), a model trained to correct another model’s errors creates a fragile dependency chain (correction cascades), and downstream systems consuming model outputs without explicit contracts become undeclared consumers that break silently when the model is updated).
2. Sự khác biệt: Không giống như phần mềm kỹ thuật nợ ((thứ) mà biểu hiện như (là) chậm hơn sự phát triển
vận tốc và là có thể nhìn thấy được trong mã (sự) đánh giá), ML kỹ thuật nợ biểu hiện như (là) im lặng độ chính xác
sự xuống cấp (thứ) mà là vô hình đối với đơn vị các bài kiểm tra, sự tích hợp các bài kiểm tra, và hệ thống sức khỏe (các) màn hình (monitors) (Unlike software technical debt (which manifests as slower development velocity and is visible in code review), ML technical debt manifests as silent accuracy degradation that is invisible to unit tests, integration tests, and system health monitors).
(Cái) hệ thống tiếp tục (để) chạy và phản hồi (một cách) chính xác bởi mọi cơ sở hạ tầng số liệu trong khi
các dự đoán (một cách) lặng lẽ tồi tệ đi (The system continues to run and respond correctly by every infrastructure metric while predictions quietly worsen).
3. Phổ biến cạm bẫy: Một thường xuyên sự ngộ nhận là (rằng) “tốt hơn mã” giải quyết kỹ thuật nợ
trong ML (A frequent misconception is that “better code” solves technical debt in ML). Trong thực tế, nó là một các hệ thống kiến trúc bài toán: (cái) nợ tích lũy khi (các)
các giả định (assumptions) của (cái) đào tạo sự phân phối (đặc trưng các phạm vi (ranges), nhãn các ý nghĩa (meanings), dữ liệu sự tươi mới)
(được) không (được) thực thi (enforced) như (là) thời gian chạy các hợp đồng tại (cái) hệ thống ranh giới (In reality, it is a systems architecture problem: the debt accumulates when the assumptions of the training distribution (feature ranges, label meanings, data freshness) are not enforced as runtime contracts at the system boundary).
(Cái) (mang tính) trừu tượng (abstract) khái niệm của kỹ thuật nợ trở nên (trở nên) cụ thể khi chúng ta kiểm tra chi phí các động lực (dynamics) (The abstract notion of technical debt becomes concrete when we examine cost dynamics). Các đội
thường (hay) chống lại (resist) sự tự động hóa sự đầu tư bởi vì thủ công các quy trình có vẻ nhanh hơn trong (cái) ngắn hạn, nhưng điều này
trực giác là (một cách) có hệ thống (systematically) sai (Teams often resist automation investment because manual processes seem faster in the short term, but this intuition is systematically wrong). Một điểm hòa vốn (break-even) sự tính toán làm điều đó (sự) cộng dồn (trở nên) cụ thể (A break-even calculation makes that compounding concrete).
Hình 14.2 tiết lộ (cái) (không) thoải mái (uncomfortable) sự thật: (cái) ML mã (tự) bản thân (nó) đại diện (cho) chỉ một nhỏ phần (fraction) của
một sản xuất ML hệ thống’s độ phức tạp (Figure 14.2 reveals the uncomfortable truth: the ML code itself represents only a small fraction of a production ML system’s complexity).

14. ML Các hoạt động
777
Khăn ăn Toán 14.1: (Cái) cộng dồn chi phí của thủ công các hoạt động
Bài toán: Tại sao xây dựng (được) tự động hóa các đường ống khi thủ công sự đào tạo lại là nhanh hơn?
Vật lý: Thủ công công việc tích lũy (lãi suất) cộng dồn (compound interest).
• Thủ công (sự) đào tạo lại: 4 giờ của kỹ thuật mỗi tuần.
• Đường ống (sự) xây dựng: 80 kỹ thuật (các) giờ (một-lần).
Toán:
• Hòa-vốn điểm: 20 các tuần.
• Bẫy (Trap): Điều này giả định (cái) mô hình không bao giờ thay đổi.
• Thực tế: Mọi mới đặc trưng thêm (vào) thủ công độ phức tạp. Nếu đặc trưng số lượng (count) nhân đôi, thủ công
thời gian nhân đôi.
• Kết quả: Sau 1 năm, thủ công các đội vẫn tiêu (spend) 4 (các) giờ mỗi tuần cho (sự) bảo trì (maintenance). Đường ống
các đội tiêu 0 (đang) lặp lại (recurring) (các) giờ.
Bối cảnh (Context): Một trung tâm (central) định luật (law) của các hệ thống kỹ thuật là (rằng) (cái) chi phí của (việc) bảo trì một hệ thống (xuyên) qua
(của) nó vòng đời có thể thống trị (cái) chi phí của (việc) xây dựng nó. Trong ML, kỹ thuật nợ là (một cách) đặc biệt (especially) nguy hiểm
bởi vì nó thường là (được) thúc đẩy bởi dữ liệu thay vì (được) thúc đẩy bởi mã: một hoàn hảo đoạn của mã vẫn (có thể) thất bại nếu (cái)
dữ liệu nó xử lý dịch chuyển. Sự đo lường là (cái) sự quản lý ranh giới: mà không (có) việc đo từ xa (telemetry), (cái)
đội không thể phân biệt (tell) liệu bảo trì công việc (có đang) giảm thiểu nợ hay (chỉ) đơn thuần che giấu nó.
Các hệ thống sự thấu hiểu: Sự tự động hóa là (một cách) cơ bản về công suất trần (ceiling), không (phải) (chỉ) tốc độ đơn độc. Một
thủ công đội đụng (hit) một trần nơi họ không thể triển khai mới các mô hình bởi vì họ đang chìm (drowning)
trong (cái) sự bảo trì của cũ (các) (mô hình). MLOps là (cái) kỹ thuật sự phản hồi: nó thay thế (cái) thủ công
“nghề thủ công (craft)” của mô hình sự bảo trì bằng một (có tính) hệ thống “nhà máy” của tính có thể quan sát và sự tự động hóa.
Mà không (có) việc giám sát cơ sở hạ tầng để làm (cho) im lặng các sự thất bại (trở nên) có thể nhìn thấy được, (cái) đội đang tích lũy
nợ và (đang) xây dựng một hệ thống (thứ) mà (là) không thể quản lý (được) (unmanageable) bởi thiết kế.
ML hệ thống
Máy
Tài nguyên
Sự quản lý
Cấu hình
Dữ liệu
Sự thu thập
Dữ liệu
Sự xác minh
Việc phục vụ
Cơ sở hạ tầng
Việc giám sát
Đặc trưng
Sự trích xuất
ML Mã
Sự phân tích Các công cụ
Quy trình
Sự quản lý
Các công cụ
Hình 14.2: Ẩn Cơ sở hạ tầng của ML Các hệ thống: (Phần) lớn kỹ thuật nỗ lực trong một điển hình máy học hệ thống tập trung (concentrates)
trên các thành phần (đang) bao quanh (cái) mô hình (tự) bản thân (nó): dữ liệu sự thu thập, đặc trưng kỹ thuật, và hệ thống cấu hình thay vì (cái)
mô hình mã (Figure 14.2: Hidden Infrastructure of ML Systems: Most engineering effort in a typical machine learning system concentrates on components surrounding the model itself: data collection, feature engineering, and system configuration rather than the model code). (Cái) sự phân phối tiết lộ (các) (thuộc về) hoạt động các thử thách và tiềm năng (potential) cho kỹ thuật nợ (đang) phát sinh (arising) từ những
thường-bị bỏ qua (often-overlooked) (đang) bao quanh các thành phần (này) (The distribution reveals the operational challenges and potential for technical debt arising from these often-overlooked surrounding components). Nguồn: (Sculley và cộng sự. 2015).
Thủ công các hoạt động đụng một công suất trần, nhưng (cái) chi phí bài toán mở rộng vượt ra ngoài kỹ thuật thời gian (Manual operations hit a capacity ceiling, but the cost problem extends beyond engineering time).
ML các hệ thống tích lũy (những) ẩn độ phức tạp thông qua (mang tính) đặc thù nợ các mẫu, mỗi (mẫu) (đang) nổi lên (emerging) từ
ML’s (có tính) đặc biệt (distinctive) sự phụ thuộc (reliance) vào dữ liệu thay vì (có tính) tất định logic, (có tính) thống kê thay vì chính xác hành vi,
và ngầm các sự phụ thuộc thông qua dữ liệu các luồng (flows) thay vì (mang tính) rõ ràng các giao diện (ML systems accumulate hidden complexity through specific debt patterns, each emerging from ML’s distinctive reliance on data rather than deterministic logic, statistical rather than exact behavior, and implicit dependencies through data flows rather than explicit interfaces).
778
14.3 Kỹ thuật Nợ
Hình 14.3 ánh xạ (maps) những các mẫu này thành sáu (các) danh mục (Figure 14.3 maps these patterns into six categories). Chú ý (như thế nào) chúng bao quanh (span) dữ liệu các mối quan tâm (chất lượng
các vấn đề (issues), sự tươi mới), mô hình các mối quan tâm (phản hồi các vòng lặp, sự sửa chữa các thác), và cơ sở hạ tầng các mối quan tâm
(cấu hình sự bành trướng (sprawl), đường ống sự phân mảnh (fragmentation)) (Notice how they span data concerns (quality issues, freshness), model concerns (feedback loops, correction cascades), and infrastructure concerns (configuration sprawl, pipeline fragmentation)). Chúng ta kiểm tra (có tính) đại diện các ví dụ (thứ) mà minh họa
(cái) kỹ thuật các phản hồi mỗi mẫu đòi hỏi (demand) (We examine representative examples that illustrate the engineering responses each pattern demands).
Ẩn
Kỹ thuật Nợ
Cấu hình
Nợ
Phản hồi
Các vòng lặp
Dữ liệu Nợ
Đường ống Nợ
Sự sửa chữa
Các thác (Cascades)
Ranh giới
Sự xói mòn
Chưa được khai báo
(Những) người tiêu dùng: Ẩn
mô hình các sự phụ thuộc
Tham số Sự bành trướng (Sprawl):
Ad hoc các thiết lập và
được mã hóa-cứng (hard-coded) các giá trị
Mong manh Các quy trình làm việc:
(Bị) ghép nối chặt chẽ
Tuần tự (Sequential)
Các sự phụ thuộc:
Thượng nguồn (Upstream) các sửa chữa (fixes) (làm) hỏng
hạ nguồn các hệ thống
Chất lượng Các vấn đề:
Không nhất quán (Inconsistent) các định dạng (formats)
và các sự phân phối
CACHE Nguyên tắc:
Thay đổi Bất cứ điều gì
Thay đổi Mọi thứ
Hình 14.3: ML Kỹ thuật Nợ Phân loại học (Taxonomy): Máy học các hệ thống tích lũy khác biệt các dạng của kỹ thuật nợ từ dữ liệu
các sự phụ thuộc, mô hình các sự tương tác, và (đang) tiến hóa các yêu cầu (Figure 14.3: ML Technical Debt Taxonomy: Machine learning systems accumulate distinct forms of technical debt from data dependencies, model interactions, and evolving requirements). Sáu chính nợ các mẫu tỏa ra (radiate) từ một trung tâm (central) trung tâm (hub): ranh giới
sự xói mòn phá ngầm (undermines) tính có thể mô đun hóa (modularity), sự sửa chữa các thác lan truyền (propagate) các sửa chữa thông qua các sự phụ thuộc, phản hồi các vòng lặp tạo ra (những) ẩn
sự ghép nối (coupling), trong khi dữ liệu các sự phụ thuộc, cấu hình nợ, và đường ống (những) khu rừng rậm (jungles) phản ánh (được) kém quản lý các đồ tạo tác và các quy trình làm việc (Six primary debt patterns radiate from a central hub: boundary erosion undermines modularity, correction cascades propagate fixes through dependencies, feedback loops create hidden coupling, while data dependencies, configuration debt, and pipeline jungles reflect poorly managed artifacts and workflows).
14.3.1 Ranh giới sự xói mòn
(Cái) đầu tiên và thường (là) (mang tính) xảo quyệt (insidious) nhất nợ mẫu liên quan (đến) (cái) sự giải tán (dissolution) của hệ thống các ranh giới (The first and often most insidious debt pattern involves the dissolution of system boundaries). Trong
truyền thống phần mềm, tính có thể mô đun hóa và sự trừu tượng hóa (abstraction) cung cấp rõ ràng các ranh giới giữa các thành phần,
(việc) cho phép các sự thay đổi để được cô lập và hành vi (để) duy trì (có thể) dự đoán (được) (In traditional software, modularity and abstraction provide clear boundaries between components, allowing changes to be isolated and behavior to remain predictable). Máy học các hệ thống
làm mờ (blur) những các ranh giới này cho một (thuộc về) cấu trúc lý do: mô hình hành vi phụ thuộc vào (thuộc về) thống kê các thuộc tính
của dữ liệu (đang) chảy (flowing) qua (cái) hệ thống thay vì (dựa) trên (mang tính) rõ ràng các giao diện (Machine learning systems blur these boundaries for a structural reason: model behavior depends on statistical properties of data flowing through the system rather than on explicit interfaces). Một (sự) thay đổi đối với (tới) thượng nguồn dữ liệu
việc định dạng có thể vượt qua (pass) tất cả đơn vị các bài kiểm tra trong khi (một cách) im lặng (việc) làm xuống cấp hạ nguồn mô hình độ chính xác (A change to upstream data formatting might pass all unit tests while silently degrading downstream model accuracy). Này
ngầm (sự) ghép nối (coupling) thông qua dữ liệu, thay vì mã, tạo ra (được) ghép nối chặt chẽ các sự tương tác giữa dữ liệu
các đường ống, đặc trưng kỹ thuật, mô hình sự đào tạo, và hạ nguồn sự tiêu thụ (This implicit coupling through data, rather than code, creates tightly coupled interactions between data pipelines, feature engineering, model training, and downstream consumption).
Này sự xói mòn tạo ra sự vướng víu: các sự phụ thuộc giữa các thành phần trở nên (trở nên) quá đan xen (intertwined)
rằng (địa) phương (local) các sự sửa đổi (modifications) yêu cầu toàn cầu sự thấu hiểu và sự phối hợp (This erosion produces entanglement: dependencies between components become so intertwined that local modifications require global understanding and coordination). (Cái) kết quả được nắm bắt bởi
(cái) CACHE nguyên tắc: Thay đổi Bất cứ điều gì Thay đổi Mọi thứ (The result is captured by the CACHE principle: Change Anything Changes Everything). Khi các hệ thống thiếu mạnh các ranh giới,
(việc) điều chỉnh một đặc trưng (sự) mã hóa (encoding), mô hình siêu tham số, hay dữ liệu (sự) lựa chọn tiêu chí có thể ảnh hưởng hạ-
nguồn hành vi trong (những) không thể dự đoán các cách (When systems lack strong boundaries, adjusting a feature encoding, model hyperparameter, or data selection criterion can affect down-stream behavior in unpredictable ways). Lấy ví dụ, (việc) thay đổi (cái) (việc) chia thùng (binning) chiến lược của một (thuộc về) số (numerical)
đặc trưng có thể gây ra một (được) (trước) đó tinh chỉnh (tuned) mô hình (để) giảm hiệu suất (underperform), (việc) kích hoạt sự đào tạo lại và hạ nguồn
sự đánh giá các sự thay đổi (thứ) mà gợn sóng (ripple) xa vượt ra ngoài (cái) ban đầu (original) sự sửa đổi (For example, changing the binning strategy of a numerical feature may cause a previously tuned model to underperform, triggering retraining and downstream evaluation changes that ripple far beyond the original modification).
(Cái) chính (sự) phòng thủ (defense) chống lại ranh giới sự xói mòn là (thuộc về) kiến trúc: tính có thể mô đun hóa và sự đóng gói (encapsulation) tại
(cái) thiết kế cấp độ (The primary defense against boundary erosion is architectural: modularity and encapsulation at the design level). Các thành phần với được xác định-tốt các giao diện cho phép các kỹ sư (để) cô lập các lỗi, lý luận
về các sự thay đổi, và giảm thiểu (cái) rủi ro của toàn-hệ thống (system-wide) các sự hồi quy (regressions) (Components with well-defined interfaces allow engineers to isolate faults, reason about changes, and reduce the risk of system-wide regressions). (Mang tính) Rõ ràng (sự) phân tách giữa dữ liệu
sự ăn (vào) (ingestion), đặc trưng kỹ thuật, và việc lập mô hình logic giới thiệu các lớp (thứ) mà có thể (được) (một cách) độc lập
(được) xác thực, (được) giám sát, và (được) duy trì (Explicit separation between data ingestion, feature engineering, and modeling logic introduces layers that can be independently validated, monitored, and maintained). Ranh giới sự xói mòn là thường vô hình trong sớm sự phát triển
bởi vì (cái) chặt (chẽ) (sự) ghép nối chỉ trở nên rõ ràng khi một có vẻ như (địa) phương sự thay đổi kích hoạt một xa xôi (distant)
sự thất bại (Boundary erosion is often invisible in early development because the tight coupling only becomes apparent when a seemingly local change triggers a distant failure). (Có tính) Chủ động (Proactive) thiết kế các quyết định (thứ) mà bảo tồn sự trừu tượng hóa, (có tính) hệ thống việc kiểm thử, và giao diện
tài liệu hóa cung cấp (các) (mang tính) thực tế nhất (các) sự phòng thủ chống lại này (đang) leo trèo (creeping) độ phức tạp (Proactive design decisions that preserve abstraction, systematic testing, and interface documentation provide the most practical defenses against this creeping complexity).
14.3.2 Sự sửa chữa các thác (cascades)
Nếu ranh giới sự xói mòn mô tả (như thế nào) ML các hệ thống mất (của) chúng (thuộc về) cấu trúc tính toàn vẹn (integrity), sự sửa chữa các thác
mô tả (những) gì xảy ra khi các đội cố gắng (thực hiện) các sự sửa chữa (repairs) (If boundary erosion describes how ML systems lose their structural integrity, correction cascades describe what happens when teams attempt repairs). Một sự sửa chữa thác xảy ra khi (việc) sửa
một thành phần giới thiệu các bài toán (ở) nơi khác, (việc) yêu cầu bổ sung các sửa chữa (fixes) (thứ) mà chính chúng gây ra
thêm nữa (further) các bài toán (A correction cascade occurs when fixing one component introduces problems elsewhere, requiring additional fixes that themselves cause further problems). Trong ML các hệ thống, những các thác này là (một cách) đặc biệt nghiêm trọng (severe) bởi vì các sự thay đổi lan truyền
thông qua (thuộc về) thống kê các sự phụ thuộc thay vì (mang tính) rõ ràng mã các con đường (In ML systems, these cascades are particularly severe because changes propagate through statistical dependencies rather than explicit code paths). (Việc) Đào tạo lại một mô hình để sửa một sự thất bại
chế độ có thể (làm) xuống cấp hiệu suất trên (được) (trước) đó (đang) hoạt động các trường hợp (Retraining a model to fix one failure mode may degrade performance on previously working cases). (Việc) Điều chỉnh các ngưỡng để giảm thiểu

14. ML Các hoạt động
779
sai các tích cực có thể gia tăng sai các tiêu cực (Adjusting thresholds to reduce false positives may increase false negatives). (Việc) Thêm (vào) các đặc trưng để giải quyết (các) góc-cạnh (edge) (các) trường hợp có thể giới thiệu
các sự tương quan (correlations) (thứ) mà (làm) mất ổn định (destabilize) (cái) toàn bộ hệ thống (Adding features to address edge cases may introduce correlations that destabilize the entire system). Mỗi sự sửa chữa kích hoạt (cái) nhu cầu cho nhiều sự sửa chữa (hơn),
(việc) tạo ra một thác (thứ) mà có thể tiêu thụ kỹ thuật tài nguyên xa vượt qua (cái) ban đầu (sự) sửa chữa (fix) (Each correction triggers the need for more corrections, creating a cascade that can consume engineering resources far exceeding the original fix).
Hình 14.4 làm (cho) (cái) thác cấu trúc (trở nên) có thể nhìn thấy được như (là) một dòng thời gian từ bài toán tuyên bố xuyên qua
sự triển khai (Figure 14.4 makes the cascade structure visible as a timeline from problem statement through deployment). Một dự án bắt đầu với một bài toán tuyên bố, tiến hành (proceeds) qua dữ liệu sự thu thập, và
nâng cao (advances) hướng tới sự triển khai (A project begins with a problem statement, proceeds through data collection, and advances toward deployment). (Các) (Được) tô màu (colored) các vòng cung (arcs) đại diện (cho) (sự) sửa chữa (các) hành động (được) kích hoạt bởi khác biệt
các nguồn của sự bất ổn định (instability): (màu) xanh lam (các) vòng cung cho thế giới-thực sự giòn tan (brittleness), đỏ cho miền chuyên môn các khoảng trống, (màu) xanh lá cây cho
(đang) xung đột (conflicting) phần thưởng các hệ thống, và (màu) cam cho sự tài liệu hóa các sự thất bại (The colored arcs represent correction actions triggered by different sources of instability: blue arcs for real-world brittleness, red for domain expertise gaps, green for conflicting reward systems, and orange for documentation failures). Các sự sửa chữa (được) khởi xướng (initiated) sớm trong
(cái) đường ống, (một cách) đặc biệt trong suốt dữ liệu sự thu thập, tạo ra (các) dài nhất các vòng cung bởi vì chúng ảnh hưởng (tới) nhiều
(thuộc về) hạ nguồn các giai đoạn (Corrections initiated early in the pipeline, especially during data collection, create the longest arcs because they affect multiple downstream stages). (Các) (Được) nét đứt (dashed) các mũi tên phía trên (cái) dòng thời gian chỉ ra (cái) tồi tệ nhất kết quả: (việc) từ bỏ
(cái) hiện tại cách tiếp cận (một cách) hoàn toàn và (việc) khởi động lại (cái) quy trình (The dashed arrows above the timeline indicate the worst outcome: abandoning the current approach entirely and restarting the process).
Bài toán
Tuyên bố
Dữ liệu sự thu thập
và (sự) dán nhãn
Dữ liệu sự phân tích
và (sự) làm sạch
Mô hình
sự lựa chọn
Mô hình
sự đào tạo
Mô hình
sự đánh giá
Mô hình
sự triển khai
(Việc) Tương tác với (thuộc về) vật lý
thế giới sự giòn tan
Không đủ (Inadequate)
ứng dụng-miền chuyên môn
Đang xung đột (Conflicting) phần thưởng
các hệ thống
Kém chéo-tổ chức
sự tài liệu hóa
Các tác động của các thác
Từ bỏ/khởi động lại quy trình
Hình 14.4: Sự sửa chữa Các thác: (Có tính) Lặp lại các sự tinh chỉnh (refinements) trong ML các hệ thống thường kích hoạt phụ thuộc các sửa chữa (fixes) (xuyên) qua (cái) quy trình làm việc,
(đang) lan truyền từ ban đầu các sự điều chỉnh (adjustments) xuyên qua dữ liệu, mô hình, và sự triển khai các giai đoạn (Figure 14.4: Correction Cascades: Iterative refinements in ML systems often trigger dependent fixes across the workflow, propagating from initial adjustments through data, model, and deployment stages). Được mã hóa-màu các vòng cung đại diện (cho) (thuộc về) sửa chữa (corrective) các hành động
(đang) bắt nguồn (stemming) từ các nguồn của sự bất ổn định, trong khi (được) nét đứt (màu) đỏ các mũi tên chỉ ra (đang) leo thang (escalating) các bản sửa đổi (revisions) (thứ) mà yêu cầu một đầy (đủ) hệ thống khởi động lại (Color-coded arcs represent corrective actions stemming from sources of instability, while dashed red arrows indicate escalating revisions that require a full system restart).
Những dài các vòng cung đó có ý nghĩa (matter) bởi vì chúng biến (địa) phương các sự sửa chữa (repairs) thành toàn-vòng đời (lifecycle-wide) các sự phụ thuộc (Those long arcs matter because they turn local repairs into lifecycle-wide dependencies). (Mang tính) Tuần tự (Sequential)
mô hình sự phát triển là một phổ biến nguồn: (việc) tái sử dụng (reusing) hay (việc) tinh chỉnh (fine-tuning) (đang) tồn tại các mô hình tăng tốc
sự phát triển cho mới các tác vụ, nhưng nó cũng tạo ra (những) ẩn các giả định (thứ) mà (là) khó để (gỡ) rối (unwind) (về) sau (Sequential model development is one common source: reusing or fine-tuning existing models accelerates development for new tasks, but it also creates hidden assumptions that are difficult to unwind later).
Các giả định (được) nhúng trong sớm hơn các mô hình trở thành ngầm các sự ép buộc cho tương lai các mô hình, (việc) giới hạn
tính linh hoạt (flexibility) và (việc) gia tăng (cái) chi phí của hạ nguồn các sự sửa chữa (Assumptions embedded in earlier models become implicit constraints for future models, limiting flexibility and increasing the cost of downstream corrections).
Xem xét một đội (những) người tinh chỉnh một khách hàng sự rời bỏ (churn) dự đoán mô hình cho một mới sản phẩm (Consider a team that fine-tunes a customer churn prediction model for a new product). (Cái)
ban đầu mô hình có thể nhúng đặc thù-sản phẩm (product-specific) các hành vi hay đặc trưng các sự mã hóa (thứ) mà không chuyển giao (transfer)
sang (cái) mới bối cảnh (The original model may embed product-specific behaviors or feature encodings that do not transfer to the new setting). Khi hiệu suất các vấn đề (issues) xuất hiện, các đội có thể cố gắng để vá (patch) (cái) mô hình, chỉ
để khám phá rằng (cái) thật bài toán nằm (nhiều) vài (several) các lớp (ở) thượng nguồn trong (cái) nguyên bản đặc trưng sự lựa chọn hay
(sự) dán nhãn các tiêu chí (As performance issues emerge, teams may attempt to patch the model, only to discover that the true problem lies several layers upstream in the original feature selection or labeling criteria).
Để giảm nhẹ sự sửa chữa các thác, các đội phải cân bằng sự tái sử dụng chống lại sự thiết kế lại (To mitigate correction cascades, teams must balance reuse against redesign). Cho nhỏ, tĩnh (static)
các tập dữ liệu, (sự) tinh chỉnh có thể là (có tính) thích hợp (appropriate); cho lớn hay (một cách) nhanh chóng (đang) tiến hóa các tập dữ liệu, (việc) đào tạo lại từ
đầu (scratch) cung cấp lớn hơn (sự) kiểm soát (For small, static datasets, fine-tuning may be appropriate; for large or rapidly evolving datasets, retraining from scratch provides greater control). (Sự) Tinh chỉnh yêu cầu ít hơn (thuộc về) tính toán tài nguyên nhưng (việc) sửa đổi
(thuộc về) nền tảng (foundational) các thành phần (về) sau trở nên cực kỳ đắt đỏ do (thuộc về) thác (cascading) các hiệu ứng (Fine-tuning requires fewer computational resources but modifying foundational components later becomes extremely costly due to cascading effects).
(Cái) (đang) làm nền tảng (underlying) cơ chế là (rằng) khi mô hình A’s các đầu ra ảnh hưởng (tới) mô hình B’s đào tạo dữ liệu,
ngầm các sự phụ thuộc xuất hiện (emerge) thông qua dữ liệu các luồng (flows) thay vì (mang tính) rõ ràng mã các giao diện (The underlying mechanism is that when model A’s outputs influence model B’s training data, implicit dependencies emerge through data flows rather than explicit code interfaces). Những các sự-
phụ-thuộc (de-pendencies) này là vô hình đối với truyền thống sự phụ thuộc sự phân tích các công cụ (These de-pendencies are invisible to traditional dependency analysis tools). Việc ngăn chặn các thác yêu cầu
(thuộc về) kiến trúc các quyết định (thứ) mà bảo tồn hệ thống tính có thể mô đun hóa (modularity): (việc) giữ các mô hình (được) ghép nối lỏng lẻo, (việc) duy-
trì (main-taining) rõ ràng phiên bản các ranh giới, và (việc) thiết kế cho (tính) độc lập sự tiến hóa (thậm chí) ngay cả khi (đang) tái sử dụng
các thành phần (Preventing cascades requires architectural decisions that preserve system modularity: keeping models loosely coupled, main-taining clear version boundaries, and designing for independent evolution even when reusing components).
14.3.3 Giao diện và sự phụ thuộc các thử thách
Ranh giới sự xói mòn và sự sửa chữa các thác chia sẻ một gốc rễ nguyên nhân: ML các hệ thống phát triển giao diện các sự-
phụ-thuộc (thứ) mà đi vòng qua (bằng đường vòng) (bypass) (mang tính) rõ ràng các giao diện (Boundary erosion and correction cascades share a root cause: ML systems develop interface de-pendencies that bypass explicit interfaces). Truyền thống phần mềm các sự phụ thuộc là có thể nhìn thấy được (nhập (import)
các câu lệnh, API các lệnh gọi (calls), cấu hình các tệp) và có thể (được) phân tích bởi các công cụ (Traditional software dependencies are visible (import statements, API calls, configuration files) and can be analyzed by tools). ML các sự phụ thuộc trốn (hide)
trong dữ liệu (ML dependencies hide in data). Khi mô hình A’s các dự đoán trở thành các đặc trưng cho mô hình B, (cái) sự phụ thuộc tồn tại chỉ trong
(cái) dữ liệu đường ống, vô hình đối với mã sự phân tích (When model A’s predictions become features for model B, the dependency exists only in the data pipeline, invisible to code analysis). Khi một bảng điều khiển tiêu thụ mô hình các đầu ra để dẫn dắt (drive)
doanh nghiệp các quyết định, không giao diện hợp đồng (nào) chi phối (cái) mối quan hệ (When a dashboard consumes model outputs to drive business decisions, no interface contract governs the relationship).

780
14.3 Kỹ thuật Nợ
Hai tới hạn các mẫu minh họa những các thử thách này (Two critical patterns illustrate these challenges). Chưa được khai báo (những) người tiêu dùng xuất hiện (arise) khi mô hình các đầu ra
phục vụ hạ nguồn các thành phần mà không (có) (mang tính) chính thức việc theo dõi hay giao diện các hợp đồng (Undeclared consumers arise when model outputs serve downstream components without formal tracking or interface contracts). Khi các mô hình tiến hóa,
những ẩn các sự phụ thuộc này hỏng (một cách) im lặng (When models evolve, these hidden dependencies break silently). Một tín dụng (việc) chấm điểm (scoring) mô hình’s các đầu ra có thể cho ăn (feed) một tính đủ điều kiện (eligibility)
động cơ (engine) (thứ) mà ảnh hưởng (đến) tương lai (người) nộp đơn (applicant) các nhóm (pools) và đào tạo dữ liệu, (việc) tạo ra không được theo dõi (untracked) phản hồi các vòng lặp
(thứ) mà (làm) thiên lệch (bias) mô hình hành vi qua thời gian (A credit scoring model’s outputs might feed an eligibility engine that influences future applicant pools and training data, creating untracked feedback loops that bias model behavior over time). Dữ liệu sự phụ thuộc nợ cộng dồn này bài toán như (khi) ML các đường ống
tích lũy không ổn định và (bị) sử dụng dưới mức (underutilized) dữ liệu các sự phụ thuộc (thứ) mà trở nên khó để theo dõi hay xác thực (Data dependency debt compounds this problem as ML pipelines accumulate unstable and underutilized data dependencies that become difficult to trace or validate).
Đặc trưng kỹ thuật các tập lệnh, dữ liệu các sự kết nối (joins), và (sự) dán nhãn các quy ước (conventions) thiếu (cái) sự phụ thuộc sự phân tích các công cụ
có sẵn trong truyền thống phần mềm sự phát triển (Feature engineering scripts, data joins, and labeling conventions lack the dependency analysis tools available in traditional software development). Khi dữ liệu các nguồn thay đổi cấu trúc hay sự phân phối,
hạ nguồn các mô hình thất bại (một cách) không mong đợi (When data sources change structure or distribution, downstream models fail unexpectedly).
Việc giảm nhẹ những giao diện các thử thách này yêu cầu (có tính) hệ thống các cách tiếp cận: nghiêm ngặt quyền truy cập các sự kiểm soát cho
mô hình các đầu ra, (mang tính) chính thức giao diện các hợp đồng với (được) tài liệu hóa các lược đồ (schemas), dữ liệu việc lập phiên bản và dòng dõi (lineage)
việc theo dõi các hệ thống, và liên tục việc giám sát của (sự) dự đoán (việc) sử dụng các mẫu (Mitigating these interface challenges requires systematic approaches: strict access controls for model outputs, formal interface contracts with documented schemas, data versioning and lineage tracking systems, and continuous monitoring of prediction usage patterns). (Cái) MLOps cơ sở hạ tầng
các mẫu (được) trình bày trong (những) tiếp theo (subsequent) các phần cung cấp (có tính) cụ thể các sự triển khai của những các giải pháp này (The MLOps infrastructure patterns presented in subsequent sections provide concrete implementations of these solutions).
14.3.4 Hệ thống sự tiến hóa các thử thách
Các (phần) đi trước (preceding) các mẫu mô tả nợ từ kém thiết kế (The preceding patterns describe debt from poor design). Thậm chí được thiết kế-tốt ML các hệ thống đối mặt (với)
sự tiến hóa các thử thách (thứ) mà khác biệt (một cách) sắc bén (sharply) từ truyền thống phần mềm (Even well-designed ML systems face evolution challenges that differ sharply from traditional software).
Phản hồi các vòng lặp đại diện (cho) (cái) tinh vi (subtle) nhất sự tiến hóa thử thách: các mô hình ảnh hưởng (tới) (của) chính chúng tương lai
hành vi thông qua (cái) dữ liệu chúng tạo ra (Feedback loops represent the most subtle evolution challenge: models influence their own future behavior through the data they generate). Sự gợi ý các hệ thống làm ví dụ (exemplify) này động lực: được gợi-
ý (sug-gested) các mục định hình (shape) người dùng các cú nhấp chuột (clicks), thứ (mà) trở thành đào tạo dữ liệu, (một cách) có tiềm năng (việc) tạo ra tự-củng cố (self-reinforcing)
các sự thiên lệch (biases) (Recommendation systems exemplify this dynamic: sug-gested items shape user clicks, which become training data, potentially creating self-reinforcing biases). (Về mặt) Hoạt động (Operationally), (cái) cảnh báo dấu hiệu là một phân nhóm (subgroup) lỗi khoảng trống (gap) (thứ) mà mở rộng (widens) (xuyên) qua (sự) đào tạo lại các chu kỳ:
một đoàn hệ nhận (các) tồi tệ hơn các dự đoán, những các dự đoán đó định hình lại (reshape) tương lai hành vi hay các nhãn, và (cái)
tiếp theo tập dữ liệu khuếch đại (amplifies) (cái) khoảng trống (Operationally, the warning sign is a subgroup error gap that widens across retraining cycles: one cohort receives worse predictions, those predictions reshape future behavior or labels, and the next dataset amplifies the gap). (Cái) MLOps bài học là để giám sát các đoàn hệ trước khi (mang tính) tổng hợp (aggregate) các số liệu
che giấu (hide) (cái) vòng lặp (The MLOps lesson is to monitor cohorts before aggregate metrics hide the loop). Những các vòng lặp này phá ngầm (undermine) dữ liệu (sự) độc lập các giả định và có thể che giấu (mask) hiệu suất
sự xuống cấp cho (các) tháng (These loops undermine data independence assumptions and can mask performance degradation for months).
Đường ống và cấu hình nợ tích lũy như (khi) ML các quy trình làm việc tiến hóa thành “đường ống những khu rừng rậm” của ad hoc
các tập lệnh và (bị) phân mảnh (fragmented) các cấu hình (Pipeline and configuration debt accumulates as ML workflows evolve into “pipeline jungles” of ad hoc scripts and fragmented configurations). Mà không (có) (có tính) mô đun các giao diện, các đội xây dựng (những) trùng lặp (duplicate) các đường ống
thay vì tái cấu trúc (những) mong manh (đường ống) (ones), (việc) dẫn đến (tới) không nhất quán (sự) xử lý và (đang) phát triển bảo trì gánh nặng (burden) (Without modular interfaces, teams build duplicate pipelines rather than refactor brittle ones, leading to inconsistent processing and growing maintenance burden).
(Đang) Cộng dồn (Compounding) điều này, nhanh (chóng) việc tạo nguyên mẫu (prototyping) khuyến khích (việc) nhúng doanh nghiệp logic trong đào tạo mã và
không được tài liệu hóa (undocumented) cấu hình các sự thay đổi (Compounding this, rapid prototyping encourages embedding business logic in training code and undocumented configuration changes). Trong khi những sớm-giai đoạn (early-stage) (các) lối tắt này là cần thiết cho sự đổi mới (innovation),
chúng trở thành các khoản nợ (liabilities) khi các hệ thống mở rộng quy mô (xuyên) qua các đội (While these early-stage shortcuts are necessary for innovation, they become liabilities as systems scale across teams). Việc quản lý sự tiến hóa yêu cầu (thuộc về) kiến trúc
kỷ luật: dựa trên-đoàn hệ (cohort-based) việc giám sát cho vòng lặp sự phát hiện, (có tính) mô đun đường ống thiết kế với quy trình làm việc
sự điều phối (orchestration) các công cụ, và (việc) đối xử (với) cấu hình như (là) một hạng-nhất (first-class) hệ thống thành phần với việc lập phiên bản
và sự xác thực (Managing evolution requires architectural discipline: cohort-based monitoring for loop detection, modular pipeline design with workflow orchestration tools, and treating configuration as a first-class system component with versioning and validation).
14.3.5 Mã và kiến trúc nợ
Dữ liệu các sự phụ thuộc và hệ thống sự tiến hóa tạo ra nợ thông qua ngầm sự ghép nối (Data dependencies and system evolution create debt through implicit coupling). ML các hệ thống cũng
tích lũy cấp độ-mã (code-level) nợ các mẫu (thứ) mà khác biệt từ truyền thống phần mềm (ML systems also accumulate code-level debt patterns that differ from traditional software). Sculley và cộng sự. (2015)
nhận diện (identify) (nhiều) vài (mẫu) (thứ) mà xứng đáng (deserve) (mang tính) rõ ràng sự chú ý (attention) (Sculley et al. (2015) identify several that deserve explicit attention).
Keo (Glue) mã thống trị (dominates) ML các cơ sở mã (codebases): các hệ thống thường yêu cầu đáng kể (substantial) sự tích hợp mã để kết nối
đa-mục đích (general-purpose) ML các gói (packages) (tới) (mang tính) đặc thù dữ liệu các đường ống và việc phục vụ các hệ thống, với (cái) keo (đang) cấu-
thành (consti-tuting) lên đến (up to) 95 phần trăm của (cái) cơ sở mã trong khi (cái) thực tế ML mã đại diện (cho) chỉ 5 phần trăm (Glue code dominates ML codebases: systems often require substantial integration code to connect general-purpose ML packages to specific data pipelines and serving systems, with the glue consti-tuting up to 95 percent of the codebase while the actual ML code represents only 5 percent). Này
keo tạo ra chặt (chẽ) sự ghép nối giữa gói các API và (cái) (đang) bao quanh hệ thống, (việc) có nghĩa (là) rằng khi
các gói cập nhật (của) chúng các giao diện, tất cả keo mã phải được viết lại (This glue creates tight coupling between package APIs and the surrounding system, meaning that when packages update their interfaces, all glue code must be rewritten). Sự giảm nhẹ yêu cầu việc bọc (wrapping) ML
các gói trong ổn định nội bộ các API và (việc) đối xử (với) bên ngoài các sự phụ thuộc như (là) (có thể) thay thế (được) (substitutable) các thành phần (Mitigation requires wrapping ML packages in stable internal APIs and treating external dependencies as substitutable components).
Chết (Dead) (thuộc về) thí nghiệm mã các con đường (codepaths) tích lũy khi ML sự phát triển bao gồm sâu rộng (extensive) sự thử nghiệm (experimentation),
(việc) để lại đằng sau (behind) (có tính) điều kiện (conditional) các nhánh (branches) cho (đã) bị từ bỏ (abandoned) các cách tiếp cận (Dead experimental codepaths accumulate as ML development involves extensive experimentation, leaving behind conditional branches for abandoned approaches). Không giống như truyền thống chết mã (thứ) mà
có thể (được) phát hiện (một cách) tĩnh (statically), (thuộc về) thí nghiệm ML mã các con đường thường duy trì “sống (live)” bởi vì chúng được kiểm soát
bởi cấu hình các cờ (flags) thay vì thời gian-biên dịch (compile-time) các điều kiện (Unlike traditional dead code that can be detected statically, experimental ML codepaths often remain “live” because they are controlled by configuration flags rather than compile-time conditions). Qua thời gian, những các con đường này gia tăng (việc) kiểm thử
gánh nặng và tạo ra sự nhầm lẫn (confusion) về việc nào mã thực sự chạy trong sản xuất (Over time, these paths increase testing burden and create confusion about which code actually runs in production). Thường xuyên mã (các) sự kiểm toán (audits)
với (mang tính) rõ ràng sự phản đối (deprecation) các dòng thời gian (timelines) và đặc trưng cờ vệ sinh (hygiene) giúp quản lý này nợ (Regular code audits with explicit deprecation timelines and feature flag hygiene help manage this debt).
Sự trừu tượng hóa nợ xuất hiện bởi vì truyền thống phần mềm kỹ thuật phụ thuộc vào được xác định-tốt các sự trừu tượng hóa
giống như các hàm, các lớp, và các mô đun, nhưng ML các hệ thống thiếu trưởng thành (mature) các sự trừu tượng hóa cho chính các khái niệm (chẳng)
hạn như (cái) đúng (right) giao diện cho một “đặc trưng” hay (cái) đúng sự đóng gói (encapsulation) cho “mô hình hành vi” (Abstraction debt arises because traditional software engineering relies on well-defined abstractions like functions, classes, and modules, but ML systems lack mature abstractions for key concepts such as the right interface for a “feature” or the right encapsulation for “model behavior”). Sự vắng mặt (absence) (này)
ép buộc các đội (để) phát minh lại (reinvent) các sự trừu tượng hóa hay, tệ hơn, tránh sự trừu tượng hóa (một cách) hoàn toàn (This absence forces teams to reinvent abstractions or, worse, avoid abstraction entirely). Phổ biến các mẫu (chẳng) hạn như

14. ML Các hoạt động
781
6
Zillow iBuying (Sự) Thất bại:
Zillow (đã) báo cáo một kế hoạch để
thu hẹp (wind down) Zillow Offers vào
Tháng 11 năm 2021, bao gồm một
Q3 hàng tồn kho (việc) giảm-giá trị (write-down) và
lực lượng lao động (các) sự cắt giảm (reductions) (Zillow
Group 2021). (Cái) sự thất bại minh-
họa (illus-trates) sự sửa chữa thác nợ
tại quy mô: việc định giá (pricing) các lỗi, việc mua (pur-chasing) các quyết định, và hàng tồn-kho phản hồi có thể củng cố (reinforce)
lẫn nhau (one another), (việc) tạo ra một vòng lặp
(thứ) mà không một (nào) (sự) đào tạo lại chu kỳ
có thể phá vỡ (break).
đặc trưng các cửa hàng (stores) ((việc) trừu tượng hóa đặc trưng sự tính toán), mô hình các cơ quan đăng ký (registries) ((việc) trừu tượng hóa mô hình việc lập phiên bản),
và sự dự đoán các dịch vụ ((việc) trừu tượng hóa sự suy luận) giảm (thiểu) trên-mỗi-dự án (per-project) sự trừu tượng hóa nợ khi chúng phù hợp (với) (cái)
đội’s quy trình làm việc (feature stores (abstracting feature computation), model registries (abstracting model versioning), and prediction services (abstracting inference) reduce per-project abstraction debt when they fit the team’s workflow).
Vượt ra ngoài những các mẫu này, Sculley và cộng sự. (2015) nhận diện cảnh báo các dấu hiệu, hay phổ biến (những) mùi (smells), (thứ) mà chỉ ra
(đang) tích lũy nợ: (cái) Đơn Thuần-Cũ-Dữ Liệu (Plain-Old-Data) Loại Mùi (sử dụng (mang tính) chung (generic) các loại giống như các chuỗi và số thực (floats) thay vì
của (thuộc về) ngữ nghĩa (semantic) các loại (thứ) mà mã hóa ý nghĩa và các sự ép buộc (constraints)), (cái) Nhiều-Ngôn Ngữ Mùi (các hệ thống
(đang) trải rộng (spanning) Python, SQL, C++, và shell các tập lệnh với không nhất quán các quy ước), và (cái) Nguyên Mẫu Mùi
(“tạm thời” nghiên cứu mã (thứ) mà trở thành (mang tính) cố định (permanent) cơ sở hạ tầng mà không (có) (sự) tái cấu trúc) (Beyond these patterns, Sculley et al. (2015) identify warning signs, or common smells, that indicate accumulating debt: the Plain-Old-Data Type Smell (using generic types like strings and floats instead of semantic types that encode meaning and constraints), the Multiple-Language Smell (systems spanning Python, SQL, C++, and shell scripts with inconsistent conventions), and the Prototype Smell (“temporary” research code that becomes permanent infrastructure without refactoring)). Có hiệu quả
các tổ chức theo dõi những các mùi này trong mã (các) sự đánh giá và phân bổ (allocate) (mang tính) rõ ràng thời gian cho nợ sự giảm thiểu, (việc) đối xử (với)
kỹ thuật nợ (việc) trả dần (paydown) như (là) một hạng-nhất (thuộc về) kỹ thuật hoạt động thay vì một ý nghĩ muộn màng (afterthought) (Effective organizations track these smells in code reviews and allocate explicit time for debt reduction, treating technical debt paydown as a first-class engineering activity rather than an afterthought).
14.3.6 Kỹ thuật nợ trong thực tế
(Các) nợ các mẫu (được) mô tả sớm hơn không phải (là) (thuộc về) lý thuyết các cấu trúc (constructs) (The debt patterns described earlier are not theoretical constructs). Chúng đã đóng một tới hạn vai trò trong
(việc) định hình (shaping) thế giới-thực máy học các hệ thống (They have played a critical role in shaping real-world machine learning systems). Trong thực tế, không nhìn thấy (unseen) các sự phụ thuộc và bị sai lệch (misaligned)
các giả định có thể tích lũy (một cách) lặng lẽ, chỉ để trở thành chính các khoản nợ (liabilities) qua thời gian (In practice, unseen dependencies and misaligned assumptions can accumulate quietly, only to become major liabilities over time).
14.3.6.1 Sản xuất nợ các mẫu
(Cái) đầu tiên cặp phơi bày (exposes) sự ghép nối (coupling) thông qua mô hình hành vi (The first pair exposes coupling through model behavior). YouTube’s sự gợi ý hệ thống minh-
họa (illus-trates) (cái) phản hồi-vòng lặp phiên bản của bài toán này: lớn (các) hệ thống gợi ý (recommenders) học từ (cái) hành vi chúng
đã giúp (để) định hình, vì thế (việc) xếp hạng (ranking) các mục tiêu, (bị) trì hoãn các nhãn, và dựa trên-đoàn hệ sự đánh giá trở thành phần của (cái)
hệ thống thiết kế thay vì ngoại tuyến (offline) sự đánh giá các chi tiết (Covington và cộng sự. 2016) (YouTube’s recommendation system illus-trates the feedback-loop version of this problem: large recommenders learn from the behavior they helped shape, so ranking objectives, delayed labels, and cohort-based evaluation become part of the system design rather than offline evaluation details (Covington et al. 2016)). Zillow’s nhà (việc) định-
giá (valua-tion) và (việc) mua quy trình làm việc (đã) phơi bày (cái) sự sửa chữa-thác phiên bản trong suốt (của) nó iBuying liên doanh (venture)6 (Zillow’s home valua-tion and purchasing workflow exposed the correction-cascade version during its iBuying venture6).
Việc định giá và hàng tồn kho các giả định (đã) lan truyền vào việc mua các quyết định; (về) sau các sự sửa chữa (corrections) sau đó
(đã) làm mất ổn định hàng tồn kho và việc định giá các quyết định, (việc) ép buộc sự tái xác thực (revalidation) và cuối cùng (eventually) một (sự) quay lui hoàn toàn
khi (cái) công ty đóng cửa (shut down) (cái) iBuying nhánh (arm) vào (năm) 2021 (Valuation and inventory assumptions propagated into purchasing decisions; later corrections then destabilized inventory and pricing decisions, forcing revalidation and eventually a full rollback when the company shut down the iBuying arm in 2021).
(Cái) thứ hai cặp phơi bày sự ghép nối thông qua quyền sở hữu và cấu hình (The second pair exposes coupling through ownership and configuration). An toàn-tới hạn (Safety-critical) việc lái xe
sự tự động hóa minh họa (cái) chưa được khai báo-người tiêu dùng rủi ro từ một khác hướng: khi được tự động-
hóa-kiểm soát (automated-control) các đầu ra, (người) lái xe các kỳ vọng (expectations), và hệ thống con (subsystem) các trách nhiệm (được) không (được) chỉ định đủ rõ ràng,
(thuộc về) hoạt động các sự thất bại có thể vượt qua (cross) thành phần các ranh giới thay vì duy trì (tại) (địa) phương (Quốc gia Giao-
thông (Trans-portation) An toàn Ủy ban (Board) 2017) (Safety-critical driving automation illustrates the undeclared-consumer risk from a different direction: when automated-control outputs, driver expectations, and subsystem responsibilities are not specified clearly enough, operational failures can cross component boundaries rather than staying local (National Trans-portation Safety Board 2017)). Facebook’s Bảng Tin (News Feed) các sự lặp lại (iterations) cho thấy (cái) cấu hình phiên bản
của (cái) cùng quản trị (governance) bài toán (Facebook’s News Feed iterations show the configuration version of the same governance problem). Nhanh sự thử nghiệm và (việc) xếp hạng các sự thay đổi yêu cầu (có thể) theo dõi (được) (traceable)
các thiết lập (settings) và (mang tính) rõ ràng các mục tiêu; (nếu) không (otherwise) (thuộc về) hành vi (behavioral) các sự thay đổi trở nên khó (để) kiểm toán (audit) sau sự triển khai
(Engineering 2016; Mosseri 2018) (Rapid experimentation and ranking changes require traceable settings and explicit objectives; otherwise behavioral changes become hard to audit after deployment (Engineering 2016; Mosseri 2018)).
Những các ví dụ này không phải (là) cảnh báo (cautionary) các câu chuyện từ bất cẩn (careless) các tổ chức (These examples are not cautionary tales from careless organizations). Chúng là (có thể) dự đoán (được) (predictable) các hậu-
quả (con-sequences) của (việc) triển khai (thuộc về) xác suất (probabilistic) hay (được) tự động hóa (automated) quyết định các hệ thống mà không (có) cơ sở hạ tầng (thứ) mà
làm (cho) sự ghép nối (trở nên) có thể nhìn thấy được (They are predictable con-sequences of deploying probabilistic or automated decision systems without infrastructure that makes coupling visible). YouTube, Zillow, an toàn-tới hạn việc lái xe sự tự động hóa, và Facebook mỗi
phơi bày một khác biệt nợ mẫu: phản hồi các vòng lặp, sự sửa chữa các thác, chưa được khai báo (những) người tiêu dùng, và
cấu hình sự bành trướng (YouTube, Zillow, safety-critical driving automation, and Facebook each expose a different debt pattern: feedback loops, correction cascades, undeclared consumers, and configuration sprawl).
Mỗi nợ mẫu có một (đang) tương ứng cơ sở hạ tầng giải pháp: đặc trưng các cửa hàng cho dữ liệu sự phụ thuộc
nợ, việc lập phiên bản các hệ thống cho cấu hình nợ, CI/CD các đường ống cho đường ống nợ, việc giám sát
các hệ thống cho phản hồi các vòng lặp (Each debt pattern has a corresponding infrastructure solution: feature stores for data dependency debt, versioning systems for configuration debt, CI/CD pipelines for pipeline debt, monitoring systems for feedback loops). Những (cái) này không phải (là) (mang tính) tùy ý (arbitrary) công cụ (tooling) các sự lựa chọn mà (là) (thuộc về) kỹ thuật các sự phản hồi (đối với)
sự thất bại các chế độ (được) chẩn đoán sớm hơn (These are not arbitrary tooling choices but engineering responses to the failure modes diagnosed earlier).
Việc nhận ra nợ các mẫu, tuy nhiên, là chỉ (một) nửa (cái) trận chiến (Recognizing debt patterns, however, is only half the battle). Các tổ chức trong những tình huống
(nghiên cứu) (case studies) này (đã) không thiếu tài năng (talented) các kỹ sư; họ (đã) thiếu (cái) (có tính) hệ thống cơ sở hạ tầng để bắt các bài toán
trước khi chúng cộng dồn (compounded) (The organizations in these case studies did not lack talented engineers; they lacked the systematic infrastructure to catch problems before they compounded). (Cái) sự chuyển đổi từ (sự) chẩn đoán sang (sự) phòng ngừa (prevention) yêu cầu (việc) kiểm tra (examining) mỗi
cơ sở hạ tầng thành phần (một cách) chi tiết: (việc) hiểu (những) gì nó làm và, (một cách) tới hạn (critically) hơn, (như thế nào) nó giải quyết
(cái) (mang tính) đặc thù sự thất bại chế độ (thứ) mà thúc đẩy (motivated) (của) nó sự tạo ra (The transition from diagnosis to prevention requires examining each infrastructure component in detail: understanding what it does and, more critically, how it addresses the specific failure mode that motivated its creation).
14.4 Sự phát triển Cơ sở hạ tầng
Sự phát triển cơ sở hạ tầng biến (cái) nợ các mẫu (được) chẩn đoán sớm hơn thành sự thực thi (enforcement) các điểm (Development infrastructure turns the debt patterns diagnosed earlier into enforcement points). Một
đặc trưng lược đồ (schema) (thứ) mà trôi dạt thượng nguồn không thể được sửa chữa bởi một bảng điều khiển đơn độc; nó cần một (được) chia sẻ
hợp đồng, một (được) lập phiên bản đồ tạo tác, và một sự triển khai đường dẫn (path) (thứ) mà từ chối (rejects) không tương thích các sự thay đổi trước khi chúng
chạm (tới) (reach) sản xuất (A feature schema that drifts upstream cannot be repaired by a dashboard alone; it needs a shared contract, a versioned artifact, and a deployment path that rejects incompatible changes before they reach production). (Cái) sự ánh xạ (mapping) trong bảng 14.6 là trực tiếp: mỗi thành phần triển khai một (thuộc về) nền tảng
nguyên tắc (phần 14.2.1) và giải quyết một cụ thể sự thất bại chế độ (The mapping in table 14.6 is direct: each component implements a foundational principle (section 14.2.1) and addresses a specific failure mode).

782
14.4 Sự phát triển Cơ sở hạ tầng
Bảng 14.6: MLOps Cơ sở hạ tầng như (là) Nợ Sự khắc phục (Remediation): Mỗi cơ sở hạ tầng thành phần là (cái) (thuộc về) kỹ thuật (sự) phản hồi cho một
cụ thể lớp (class) của kỹ thuật nợ (được) quan sát trong sản xuất ML các hệ thống (Table 14.6: MLOps Infrastructure as Debt Remediation: Each infrastructure component is the engineering response to a specific class of technical debt observed in production ML systems). Đặc trưng các cửa hàng thực thi (cái) sự nhất quán mệnh lệnh (thứ) mà
loại bỏ (eliminates) đào tạo-phục vụ sự sai lệch; việc lập phiên bản các hệ thống bảo tồn tính có thể tái tạo chống lại sự sửa chữa các thác; CI/CD các đường ống
tự động hóa (cái) (sự) ra mắt (rollout) kỷ luật (thứ) mà ngăn chặn ranh giới sự xói mòn; việc giám sát các hệ thống làm nổi lên (surface) im lặng sự xuống cấp trước khi người dùng (làm điều đó) (do) (Feature stores enforce the consistency imperative that eliminates training-serving skew; versioning systems preserve reproducibility against correction cascades; CI/CD pipelines automate the rollout discipline that prevents boundary erosion; monitoring systems surface silent degradation before users do).
Cơ sở hạ tầng Thành phần
Nguyên tắc Được triển khai (Implemented)
Nợ Mẫu Được giải quyết (Addressed)
Đặc trưng các cửa hàng
Sự nhất quán Mệnh lệnh
Dữ liệu sự phụ thuộc nợ, đào tạo-phục vụ sự sai lệch
Việc lập phiên bản các hệ thống
Tính có thể tái tạo Thông qua Việc lập phiên bản
Cấu hình nợ, sự sửa chữa các thác
CI/CD các đường ống
Nhận thức-Chi phí Sự Tự động hóa
Đường ống nợ, ranh giới sự xói mòn
Việc giám sát các hệ thống
(Có thể) Quan sát (được) Sự xuống cấp
Phản hồi các vòng lặp, im lặng các sự thất bại
Hình 14.5 tổ chức những các thành phần này (xuyên) qua ML các mô hình, các khuôn khổ, sự điều phối (orchestration), cơ-sở-
hạ-tầng (infras-tructure), và phần cứng (Figure 14.5 organizes these components across ML models, frameworks, orchestration, infras-tructure, and hardware). (Việc) Hiểu (như thế nào) những các lớp này tương tác kích hoạt (cho phép) những người thực hành (practitioners) thiết kế
các hệ thống (thứ) mà (một cách) có hệ thống giải quyết (cái) kỹ thuật nợ các mẫu (được) nhận diện sớm hơn trong khi (đang) duy trì
(thuộc về) hoạt động tính bền vững (sustainability) (Understanding how these layers interact enables practitioners to design systems that systematically address the technical debt patterns identified earlier while maintaining operational sustainability).
ML Các mô hình/Các ứng dụng
(ví dụ, BERT)
ML Các khuôn khổ/Các nền tảng
(ví dụ, PyTorch)
Mô hình Sự điều phối
(ví dụ, Ray)
Cơ sở hạ tầng
(ví dụ, Kubernetes)
Phần cứng
(ví dụ, một GPU cụm (cluster))
Dữ liệu Sự quản lý
CI/CD
Mô hình Sự đào tạo
Mô hình Sự đánh giá (Eval)
Sự triển khai
Mô hình Việc phục vụ
Công việc (Job) Việc lên lịch (Scheduling)
Tài nguyên Sự quản lý
Công suất Sự quản lý
Việc giám sát
MLOps
• • •
Hình 14.5: MLOps Ngăn xếp Các lớp: Năm tầng (tiers) tổ chức (cái) ML hệ thống ngăn xếp: ML Các mô hình tại (cái) đỉnh, (được) theo sau bởi Các khuôn khổ,
Sự điều phối, Cơ sở hạ tầng, và Phần cứng (Figure 14.5: MLOps Stack Layers: Five tiers organize the ML system stack: ML Models at the top, followed by Frameworks, Orchestration, Infrastructure, and Hardware). MLOps trải rộng (spans) sự điều phối các tác vụ (dữ liệu sự quản lý xuyên qua mô hình việc phục vụ) và
cơ sở hạ tầng các tác vụ (công việc việc lên lịch xuyên qua việc giám sát), (việc) kích hoạt sự tự động hóa, tính có thể tái tạo, và (có thể) mở rộng quy mô sự triển khai (MLOps spans orchestration tasks (data management through model serving) and infrastructure tasks (job scheduling through monitoring), enabling automation, reproducibility, and scalable deployment).
14.4.1 Dữ liệu cơ sở hạ tầng và sự chuẩn bị
Đáng tin cậy máy học các hệ thống phụ thuộc vào (được) cấu trúc, (có thể) mở rộng quy mô, và (có thể) lặp lại dữ liệu (sự) xử lý (handling) (Reliable machine learning systems depend on structured, scalable, and repeatable data handling).
Từ sự ăn (vào) (ingestion) đến sự suy luận, mỗi giai đoạn phải bảo tồn chất lượng, sự nhất quán, và tính có thể theo dõi (traceability) (xuyên) qua
ban đầu sự phát triển, liên tục (continual) sự đào tạo lại, (sự) kiểm toán, và (việc) phục vụ giống nhau (alike) (From ingestion to inference, each stage must preserve quality, consistency, and traceability across initial development, continual retraining, auditing, and serving alike). Những các yêu cầu này đòi hỏi
các hệ thống (thứ) mà chính thức hóa (formalize) dữ liệu sự chuyển đổi (transformation) và việc lập phiên bản xuyên suốt (cái) ML vòng đời (These requirements demand systems that formalize data transformation and versioning throughout the ML lifecycle).
14.4.1.1 Dữ liệu sự quản lý
(Các) kỹ thuật nợ các mẫu chúng ta (đã) kiểm tra bắt nguồn (stem) (phần) lớn từ kém dữ liệu sự quản lý: không được lập phiên bản
các tập dữ liệu tạo ra ranh giới sự xói mòn, không nhất quán đặc trưng sự tính toán gây ra sự sửa chữa các thác,
và không được tài liệu hóa dữ liệu các sự phụ thuộc sinh ra (breed) ẩn (những) người tiêu dùng (The technical debt patterns we examined stem largely from poor data management: unversioned datasets create boundary erosion, inconsistent feature computation causes correction cascades, and undocumented data dependencies breed hidden consumers). Dữ liệu sự quản lý cơ sở hạ tầng
(một cách) trực tiếp giải quyết những gốc rễ nguyên nhân này (Data management infrastructure directly addresses these root causes). Xây dựng trên (cái) dữ liệu kỹ thuật các nền tảng (foundations) từ Chương 4,
dữ liệu sự thu thập, việc tiền xử lý, và đặc trưng sự chuyển đổi trở thành (được) chính thức hóa (thuộc về) hoạt động các quy trình (Building on the data engineering foundations from Chapter 4, data collection, preprocessing, and feature transformation become formalized operational processes).
Nơi dữ liệu kỹ thuật tập trung vào đơn-đường ống (single-pipeline) tính đúng đắn (correctness), MLOps dữ liệu sự quản lý nhấn-
mạnh (empha-sizes) chéo-đường ống sự nhất quán, (việc) đảm bảo rằng (việc) đào tạo và (việc) phục vụ tính toán (những) giống hệt nhau các đặc trưng (Where data engineering focuses on single-pipeline correctness, MLOps data management empha-sizes cross-pipeline consistency, ensuring that training and serving compute identical features). Dữ liệu
sự quản lý do vậy mở rộng vượt ra ngoài ban đầu sự chuẩn bị để bao quanh (encompass) (cái) liên tục (sự) xử lý (handling) của dữ liệu
các đồ tạo tác xuyên suốt (cái) ML hệ thống vòng đời (Data management thus extends beyond initial preparation to encompass the continuous handling of data artifacts throughout the ML system lifecycle).

14. ML Các hoạt động
783
7
Đặc trưng Cửa hàng (Store):
Uber’s
Michelangelo nền tảng đã-
mô tả một (được) tập trung (centralized) đặc trưng
cửa hàng cho (việc) chia sẻ và (việc) phục-
vụ (serv-ing) các đặc trưng (xuyên) qua sản-
xuất (produc-tion) các mô hình (Hermann và
Del Balso 2017a).
Tại đó
quy mô, (cái) sự nhất quán (sự) đảm bảo (guaran-tee)
phải giữ (hold) dưới một trực tuyến (online)
độ trễ ngân sách: (những) gì phân-
biệt (distin-guishes) một đặc trưng cửa hàng khỏi một
được chia sẻ thư viện của đặc trưng mã
là rằng (cái) được chia sẻ đặc trưng con đường
cũng phải phục vụ (sự) tươi mới các đặc trưng
nhanh đủ cho thời gian-thực (real-time) sự suy-
luận (infer-ence).
Ba các nguyên tắc tổ chức (cái) cơ sở hạ tầng (thứ) mà giải quyết những gốc rễ nguyên nhân này: sự nhất quán, sự tươi mới,
và chất lượng (Three principles organize the infrastructure that addresses these root causes: consistency, freshness, and quality). Mỗi nguyên tắc thúc đẩy (mang tính) đặc thù công cụ (tooling) thay vì (cái) ngược lại (reverse) (Each principle motivates specific tooling rather than the reverse).
(Cái) đầu tiên yêu cầu là dữ liệu sự nhất quán: mọi đồ tạo tác (đang) ảnh hưởng (tới) mô hình hành vi, từ thô (raw)
các tập dữ liệu đến (được) làm kỹ thuật (engineered) các đặc trưng, phải được lập phiên bản và (có thể) tái tạo (được) (The first requirement is data consistency: every artifact influencing model behavior, from raw datasets to engineered features, must be versioned and reproducible). Mà không (có) việc lập phiên bản, các đội
không thể theo dõi (trace) cái nào dữ liệu (đã) sản xuất cái nào mô hình, (việc) làm (cho) việc gỡ lỗi (debugging) và sự quay lui (trở nên) không thể (Without versioning, teams cannot trace which data produced which model, making debugging and rollback impossible). (Cái)
sự triển khai thường kết hợp mã việc lập phiên bản, tập dữ liệu việc lập phiên bản, và bền (durable) đối tượng lưu trữ (The implementation usually combines code versioning, dataset versioning, and durable object storage).
DVC (Dữ liệu Phiên bản Sự kiểm soát) (Iterative 2024), Git (Torvalds và Hamano 2024), Amazon S3 (Amazon
Web Services 2024b), và Google Đám mây (Cloud) Lưu trữ (Google Cloud 2024b) là các ví dụ của đó mẫu,
nhưng (cái) bất biến (invariant) là (cái) quan trọng phần: thô và (được) xử lý các đồ tạo tác phải duy trì (có thể) đánh địa chỉ (được) (addressable) bởi
phiên bản (DVC (Data Version Control) (Iterative 2024), Git (Torvalds and Hamano 2024), Amazon S3 (Amazon Web Services 2024b), and Google Cloud Storage (Google Cloud 2024b) are examples of that pattern, but the invariant is the important part: raw and processed artifacts must remain addressable by version). Phần 14.4.1.3 kiểm tra sự triển khai các chi tiết bao gồm Git sự tích hợp, siêu dữ liệu
việc theo dõi, và dòng dõi sự bảo tồn (preservation) (Section 14.4.1.3 examines implementation details including Git integration, metadata tracking, and lineage preservation). Tại (cái) đặc trưng cấp độ, (cái) đặc trưng cửa hàng thực thi sự nhất quán bằng (cách)
(việc) tính toán các đặc trưng một lần và (việc) phục vụ chúng (một cách) giống hệt nhau (tới) cả đào tạo và phục vụ các đường ống (At the feature level, the feature store enforces consistency by computing features once and serving them identically to both training and serving pipelines). Uber’s
Michelangelo nền tảng (đã) phổ biến (popularized) này mẫu bên trong một lớn sản xuất ML nền tảng, và Feast
(về) sau (đã) làm (cho) (cái) mẫu (có) sẵn như (là) nguồn-mở (open-source) đặc trưng-cửa hàng cơ sở hạ tầng (Hermann và Del Balso
2017a; Gojek và Google 2019) (Uber’s Michelangelo platform popularized this pattern inside a large production ML platform, and Feast later made the pattern available as open-source feature-store infrastructure (Hermann and Del Balso 2017a; Gojek and Google 2019)). Phần 14.4.1.2 chi tiết (details) sự triển khai các mẫu cho đào tạo-phục vụ
sự nhất quán (Section 14.4.1.2 details implementation patterns for training-serving consistency).
Sự nhất quán đơn độc (alone) là không đủ nếu (cái) (đang) làm nền tảng (underlying) dữ liệu là cũ (stale) (Consistency alone is insufficient if the underlying data is stale). Dữ liệu sự tươi mới đảm bảo rằng các mô hình
đào tạo và phục vụ trên hiện tại dữ liệu thay vì (đã) lỗi thời (outdated) các ảnh chụp nhanh (snapshots) (Data freshness ensures that models train and serve on current data rather than outdated snapshots). (Được) Tự động hóa dữ liệu các đường ống duy trì
sự tươi mới bằng (cách) (một cách) liên tục (việc) chuyển đổi thô dữ liệu thành sẵn sàng-để-phân tích (analysis-ready) các định dạng thông qua (được) cấu trúc
các giai đoạn: sự ăn (vào), lược đồ sự xác thực, sự khử trùng lặp (deduplication), sự chuyển đổi, và (việc) tải (loading) (Automated data pipelines maintain freshness by continuously transforming raw data into analysis-ready formats through structured stages: ingestion, schema validation, deduplication, transformation, and loading). Sự điều phối (Orchestration)
các hệ thống (chẳng) hạn như Apache Airflow (Apache Phần mềm (Software) Tổ chức (Foundation) 2024), Prefect (Prefect Các công nghệ (Technologies),
Inc. 2024), và dbt (dbt Các phòng thí nghiệm (Labs) 2024) có ý nghĩa (matter) bởi vì chúng làm (cho) những các giai đoạn đó (trở nên) rõ ràng, (được) lên lịch, và
có thể đánh giá (reviewable) như (là) mã (Orchestration systems such as Apache Airflow (Apache Software Foundation 2024), Prefect (Prefect Technologies, Inc. 2024), and dbt (dbt Labs 2024) matter because they make those stages explicit, scheduled, and reviewable as code). Một khi (cái) đường ống được quản lý theo cách này, dữ liệu các luồng có thể tiến hóa cùng (với) mô hình
các yêu cầu mà không (cần) mất (đi) việc lập phiên bản, tính có thể mô đun hóa, hay CI/CD sự tích hợp (Once the pipeline is managed this way, data flows can evolve with model requirements without losing versioning, modularity, or CI/CD integration).
(Cái) thứ ba trụ cột (pillar), dữ liệu chất lượng, chi phối liệu (cái) dữ liệu (đang) chạm (tới) các mô hình là (có tính) chính xác, hoàn chỉnh, và
(được) dán nhãn (một cách) nhất quán (hay không) (The third pillar, data quality, governs whether the data reaching models is accurate, complete, and consistently labeled). Trong (được) giám sát (supervised) học tập các đường ống, (việc) dán nhãn chất lượng (một cách) trực tiếp quyết định mô hình
các trần (ceilings) (In supervised learning pipelines, labeling quality directly determines model ceilings). Việc dán nhãn các công cụ (chẳng) hạn như Label Studio (HumanSignal 2024) hỗ trợ (có thể) mở rộng quy mô, dựa trên-đội (team-based)
sự chú thích (annotation) với (được) tích hợp kiểm toán (các) dấu vết (trails) và phiên bản các lịch sử (histories), các khả năng (thứ) mà trở nên thiết yếu khi
việc dán nhãn các quy ước tiến hóa qua thời gian hay yêu cầu sự tinh chỉnh (refinement) (xuyên) qua nhiều dự án các sự lặp lại (Labeling tools such as Label Studio (HumanSignal 2024) support scalable, team-based annotation with integrated audit trails and version histories, capabilities that become essential when labeling conventions evolve over time or require refinement across multiple project iterations).
Để minh họa (như thế nào) ba các nguyên tắc này củng cố lẫn nhau trong thực tế (như thế nào), xem xét một (thuộc về) dự đoán
bảo trì ứng dụng trong một (thuộc về) công nghiệp bối cảnh (setting) (To illustrate how these three principles reinforce each other in practice, consider a predictive maintenance application in an industrial setting). Một liên tục luồng của cảm biến dữ liệu được ăn (vào)
và (được) kết nối (joined) với (thuộc về) lịch sử bảo trì các nhật ký thông qua một (được) lên lịch đường ống (được) quản lý trong Airflow
(sự tươi mới) (A continuous stream of sensor data is ingested and joined with historical maintenance logs through a scheduled pipeline managed in Airflow (freshness)). Các (đang) kết quả các đặc trưng, bao gồm (đang) lăn (rolling) các số trung bình và (thuộc về) thống kê (các) (sự) tổng hợp (aggregates), được lưu trữ
trong một đặc trưng cửa hàng cho cả sự đào tạo lại và thấp-độ trễ sự suy luận (sự nhất quán) (The resulting features, including rolling averages and statistical aggregates, are stored in a feature store for both retraining and low-latency inference (consistency)). Lược đồ sự xác thực,
cảm biến-phạm vi (sensor-range) các sự kiểm tra (checks), sự thiếu vắng (missingness) các bài kiểm tra, và nhãn các sự kiểm toán bắt (bị) dị dạng (malformed) hay không đáng tin cậy bảo trì
các bản ghi trước khi chúng chạm (tới) (sự) đào tạo (chất lượng), trong khi việc lập phiên bản và mô hình-cơ quan đăng ký sự tích hợp bảo tồn
tính có thể theo dõi từ dữ liệu đến (được) triển khai mô hình các dự đoán (Schema validation, sensor-range checks, missingness tests, and label audits catch malformed or unreliable maintenance records before they reach training (quality), while versioning and model-registry integration preserve traceability from data to deployed model predictions). Dữ liệu sự quản lý, (được) tổ chức xoay quanh (around) những
ba các nguyên tắc này, thiết lập (cái) (thuộc về) hoạt động xương sống (backbone) cho mô hình tính có thể tái tạo, tính có thể kiểm toán (auditability), và
(được) duy trì (sustained) sự triển khai tại quy mô (Data management, organized around these three principles, establishes the operational backbone for model reproducibility, auditability, and sustained deployment at scale).
14.4.1.2 Đặc trưng các cửa hàng
(Cái) dữ liệu sự phụ thuộc nợ và đào tạo-phục vụ sự sai lệch các mẫu (được) mô tả trong phần 14.3 chia sẻ một
chung gốc rễ nguyên nhân: không nhất quán đặc trưng sự tính toán (xuyên) qua đường ống các giai đoạn (The data dependency debt and training-serving skew patterns described in section 14.3 share a common root cause: inconsistent feature computation across pipeline stages). Xem xét (những) gì (một cách) điển hình
xảy ra (khi) không (có) một đặc trưng cửa hàng: một dữ liệu nhà khoa học tính toán user_session_length (người dùng_phiên_độ dài) trong Python cho
(sự) đào tạo, trong khi một kỹ sư triển khai lại cùng (cái) (sự) tính toán bằng Java cho (việc) phục vụ (Consider what typically happens without a feature store: a data scientist computes user_session_length in Python for training, while an engineer reimplements the same calculation in Java for serving). (Mang tính) Tinh vi các sự khác biệt
xuất hiện: (cái) một sử dụng tường-đồng hồ (wall-clock) thời gian, (cái) khác (sử dụng) (việc) xử lý thời gian; (cái) một bao gồm nhàn rỗi (idle) các (sự) hết thời gian chờ (timeouts), (cái) khác
(thì) không (Subtle differences emerge: one uses wall-clock time, the other processing time; one includes idle timeouts, the other does not). (Cái) mô hình đào tạo trên một định nghĩa nhưng phục vụ (đang) sử dụng (cái) khác, và độ chính xác xuống cấp (một cách) im lặng (The model trains on one definition but serves using another, and accuracy degrades silently).
Đặc trưng các cửa hàng7 giải quyết này thử thách bằng (cách) cung cấp một sự trừu tượng hóa lớp giữa dữ liệu kỹ thuật
và máy học, (việc) triển khai (cái) sự nhất quán mệnh lệnh thông qua một đơn (single) nguồn của sự thật cho
đặc trưng các giá trị (Feature stores7 address this challenge by providing an abstraction layer between data engineering and machine learning, implementing the consistency imperative through a single source of truth for feature values). Trong (mang tính) thông thường (conventional) các đường ống, đặc trưng kỹ thuật logic (bị) trùng lặp (duplicated) hay phân kỳ (xuyên) qua
các môi trường, (việc) giới thiệu các rủi ro của đào tạo-phục vụ sự sai lệch, dữ liệu (sự) rò rỉ (leakage), và mô hình sự trôi dạt (In conventional pipelines, feature engineering logic is duplicated or diverges across environments, introducing risks of training-serving skew, data leakage, and model drift).
Đặc trưng các cửa hàng quản lý cả ngoại tuyến (lô (batch)) và trực tuyến (thời gian-thực) đặc trưng quyền truy cập thông qua một (được) tập trung-
hóa kho lưu trữ (repository) (Feature stores manage both offline (batch) and online (real-time) feature access through a central-ized repository). Trong suốt (sự) đào tạo, các đặc trưng được tính toán và (được) lưu trữ trong một lô môi trường cùng với
(thuộc về) lịch sử các nhãn (During training, features are computed and stored in a batch environment alongside historical labels). Tại suy luận thời gian, (cái) cùng sự chuyển đổi logic được áp dụng cho tươi (fresh) dữ liệu trong một
trực tuyến (đang) phục vụ hệ thống (At inference time, the same transformation logic is applied to fresh data in an online serving system). Này kiến trúc đảm bảo các mô hình tiêu thụ (những) giống hệt nhau các đặc trưng trong cả hai các bối cảnh,
một thuộc tính (thứ) mà trở nên tới hạn khi (đang) triển khai (các) (được) tối ưu hóa các mô hình (được) thảo luận trong Chương 10 (This architecture ensures models consume identical features in both contexts, a property that becomes critical when deploying the optimized models discussed in Chapter 10).

784
14.4 Sự phát triển Cơ sở hạ tầng
(Cái) đặc trưng cửa hàng là, (về mặt) các hệ thống các thuật ngữ, (cái) kỹ thuật cơ chế (thứ) mà thực thi (cái) đào tạo-phục vụ
sự sai lệch định luật: bằng (cách) (việc) tập trung hóa đặc trưng các định nghĩa và (việc) phục vụ chúng thông qua một (được) chia sẻ con đường, nó giảm thiểu
(cái) đường ống sự phân kỳ (thứ) mà (nếu) không (otherwise) gây ra im lặng sản xuất độ chính xác (sự) mất (mát) (The feature store is, in systems terms, the engineering mechanism that enforces the training-serving skew law: by centralizing feature definitions and serving them through a shared path, it reduces the pipeline divergence that otherwise causes silent production accuracy loss).
Vượt ra ngoài sự nhất quán, đặc trưng các cửa hàng hỗ trợ việc lập phiên bản, siêu dữ liệu sự quản lý, và đặc trưng sự tái sử dụng
(xuyên) qua các đội (Beyond consistency, feature stores support versioning, metadata management, and feature reuse across teams). Một gian lận sự phát hiện mô hình và một tín dụng (việc) chấm điểm mô hình có thể phụ thuộc vào (đang) chồng chéo (overlapping) giao-
dịch (transac-tion) các đặc trưng (thứ) mà có thể (được) (một cách) tập trung (được) duy trì, (được) xác thực, và (được) chia sẻ (A fraud detection model and a credit scoring model may rely on overlapping transac-tion features that can be centrally maintained, validated, and shared). Sự tích hợp với dữ liệu các đường ống
và mô hình các cơ quan đăng ký kích hoạt dòng dõi việc theo dõi: khi một đặc trưng được cập nhật hay (bị) phản đối, (các) phụ thuộc
các mô hình được nhận diện và (được) đào tạo lại (một cách) tương ứng (Integration with data pipelines and model registries enables lineage tracking: when a feature is updated or deprecated, dependent models are identified and retrained accordingly).
Đào tạo-phục vụ sự sai lệch: Sự chẩn đoán và sự phòng ngừa Đào tạo-phục vụ sự sai lệch ((được) định nghĩa (một cách) chính thức trong
phần 13.6.1) biểu hiện (về mặt) hoạt động thông qua đặc trưng cửa hàng các sự không nhất quán (inconsistencies) và đường ống sự phân kỳ (Training-serving skew: Diagnosis and prevention Training-serving skew (defined formally in section 13.6.1) manifests operationally through feature store inconsistencies and pipeline divergence).
Bảng 14.7 tóm tắt (summarizes) phổ biến các nguyên nhân và (của) chúng sự phát hiện các phương pháp (Table 14.7 summarizes common causes and their detection methods):
Bảng 14.7: Đào tạo-Phục vụ Sự sai lệch Các danh mục: Mỗi danh mục yêu cầu khác biệt sự phát hiện và sự phòng ngừa các chiến lược (Table 14.7: Training-Serving Skew Categories: Each category requires different detection and prevention strategies). Lược đồ
và việc tiền xử lý sự sai lệch xuất hiện từ mã sự phân kỳ và yêu cầu đặc trưng cửa hàng sự hợp nhất (unification), trong khi dữ liệu sự phân phối sự sai lệch
yêu cầu (thuộc về) thống kê việc giám sát so với (against) đào tạo các đường cơ sở (Schema and preprocessing skew emerge from code divergence and require feature store unification, while data distribution skew requires statistical monitoring against training baselines). Thời gian sự sai lệch đòi hỏi (demand) cẩn thận sự phân tích của đặc trưng sự tươi mới giữa
đào tạo và phục vụ các bối cảnh (Timing skew demands careful analysis of feature freshness between training and serving contexts).
Sự sai lệch Loại
Ví dụ
Sự phát hiện Phương pháp
Đặc trưng việc tiền xử lý
Sự chuẩn hóa (Normalization) sử dụng khác (thuộc về) thống kê
(Thuộc về) Thống kê sự so sánh của đặc trưng các sự phân phối
Thiếu dữ liệu sự xử lý
Đào tạo điền (fills) NaN với (số) trung bình; phục vụ sử dụng 0
Lược đồ sự xác thực với (mang tính) rõ ràng null sự xử lý
Phụ thuộc-thời gian các đặc trưng
Các đặc trưng (được) tính toán với khác thời gian các ngưỡng cắt (cutoffs)
Dấu thời gian (Timestamp) sự xác thực trong đặc trưng các đường ống
Thư viện phiên bản sự trôi dạt
NumPy hay Pandas phiên bản các sự khác biệt
Môi trường băm sự so sánh
Đào tạo-phục vụ sự sai lệch tình huống (nghiên cứu) Một (mang tính) thực tế ví dụ minh họa (như thế nào) đào tạo-phục vụ sự sai lệch biểu-
hiện (man-ifests) trong sản xuất các hệ thống (như thế nào) (Training-serving skew case study A practical example illustrates how training-serving skew man-ifests in production systems). Xem xét một sự gợi ý hệ thống (thứ) mà cho thấy 8 phần trăm độ chính xác
sự xuống cấp một tháng sau sự triển khai với không mô hình-mã các sự thay đổi (Consider a recommendation system that shows 8 percent accuracy degradation one month after deployment with no model-code changes). Đặc trưng sự phân phối sự so-
sánh (com-parison) tiết lộ rằng user_session_length có một (số) trung bình của 45 (các) phút trong đào tạo nhưng 12 (các) phút trong
phục vụ (Feature distribution com-parison reveals that user_session_length has a mean of 45 minutes in training but 12 minutes in serving). (Cái) gốc rễ nguyên nhân là đặc trưng-định nghĩa sự sai lệch: (cái) ngoại tuyến đào tạo đường ống tính toán tường-đồng hồ
khoảng thời gian (duration) từ (cái) đầu tiên sự kiện đến (cái) cuối cùng sự kiện trong một phiên (session), trong khi (cái) trực tuyến phục vụ con đường đếm (counts) chỉ
tiền cảnh-hoạt động (foreground-active) thời gian sau (khi) nhàn rỗi các khoảng trống được loại bỏ (The root cause is feature-definition skew: the offline training pipeline computes wall-clock duration from the first event to the last event in a session, while the online serving path counts only foreground-active time after idle gaps are removed). Như (là) một kết quả, (cái) mô hình (đã) học các ngưỡng (được) gắn (tied)
với một đặc trưng định nghĩa (thứ) mà sản xuất không bao giờ thực sự phục vụ (As a result, the model learned thresholds tied to a feature definition that production never actually serves).
Đặc trưng các cửa hàng ((đang) xây dựng trên (cái) dữ liệu các đường ống từ Chương 4) giải quyết này bài toán bằng (cách) (việc) tính toán
các đặc trưng một lần và (việc) phục vụ chúng (một cách) nhất quán (tới) cả đào tạo và phục vụ các đường ống (Feature stores (building on the data pipelines from Chapter 4) address this problem by computing features once and serving them consistently to both training and serving pipelines). (Mã) Liệt kê 14.1
chứng minh (demonstrates) (cái) bất biến (invariant): (việc) đào tạo truy xuất (retrieves) thời điểm-trong-thời gian (point-in-time) (thuộc về) lịch sử các đặc trưng, (việc) phục vụ truy xuất
hiện tại trực tuyến các đặc trưng, và cả hai các lệnh gọi phân giải (resolve) (tới) (cái) cùng (được) lập phiên bản đặc trưng định nghĩa thay vì
(bị) trùng lặp mã các con đường (Listing 14.1 demonstrates the invariant: training retrieves point-in-time historical features, serving retrieves current online features, and both calls resolve to the same versioned feature definition rather than duplicated code paths).
(Mã) Liệt kê 14.1: Đặc trưng Cửa hàng Sự nhất quán: (Được) Hợp nhất (Unified) đặc trưng sự truy xuất giảm (thiểu) đào tạo-phục vụ sự sai lệch bằng (cách) (việc) đảm bảo cả hai các đường ống
truy cập (những) giống hệt nhau đặc trưng các sự tính toán (Listing 14.1: Feature Store Consistency: Unified feature retrieval reduces training-serving skew by ensuring both pipelines access identical feature computations).
feature_definitions = registry.load(version="2026-06-01")
training_features = feature_definitions.materialize_historical(
entities=training_entities,
at_event_time=True,
names=["user.session_length", "user.purchase_history"],
)
serving_features = feature_definitions.lookup_online(
entities=[{"user_id": 12345}],
names=["user.session_length", "user.purchase_history"],
)
assert training_features.schema == serving_features.schema
assert (
training_features.definition_hash
== serving_features.definition_hash
)
14. ML Các hoạt động
785
8
Mô hình Cơ quan đăng ký: Ngăn chặn
“cơ quan đăng ký đường vòng (bypass),” (cái) sự thất bại
chế độ nơi (cái) không được tài-
liệu-hóa sản xuất mô hình
phân kỳ từ (cái) (được) đào tạo
đồ tạo tác thông qua khác việc tiền-
xử lý, cũ (sự) tuần tự hóa
các định dạng, hay thủ công các bản sửa lỗi nóng (hotfixes)
(được) áp dụng (một cách) trực tiếp (tới) (cái)
(đang) phục vụ điểm cuối (endpoint). Mà không (có) một
cơ quan đăng ký (đang) thực thi (được) lập phiên bản,
bất biến (immutable) các đồ tạo tác với
(có thể) truy vấn (được) siêu dữ liệu và trạng thái,
các sự quay lui yêu cầu (việc) định-
vị (locating)
(cái) chính xác các trọng số từ một
ad-hoc đồ tạo tác cửa hàng dưới
sự cố (incident) áp lực (pressure).
Bằng (cách) (việc) tính toán session_length (phiên_độ dài) một lần trong (cái) đặc trưng đường ống, đào tạo và phục vụ thấy (những) giống hệt nhau
các giá trị (By computing session_length once in the feature pipeline, training and serving see identical values). (Được) Tập trung hóa đặc trưng các cửa hàng cũng hỗ trợ đặc trưng sự tái sử dụng và siêu dữ liệu việc theo dõi, thứ (mà) làm (cho)
sự sai lệch dễ (dàng) (hơn) để phát hiện và sửa (correct) khi một đặc trưng định nghĩa thay đổi (Hermann và Del Balso 2017a;
Gojek và Google 2019) (Centralized feature stores also support feature reuse and metadata tracking, which makes skew easier to detect and correct when a feature definition changes (Hermann and Del Balso 2017a; Gojek and Google 2019)).
Như (khi) (cái) sự nhất quán mệnh lệnh định lượng (phần 14.2.1.3), do-sự sai lệch-gây ra các lỗi tại sản xuất
quy mô chuyển đổi (translate) thành (hàng) trăm của (hàng) ngàn của đô la trong hàng năm chi phí (As the consistency imperative quantified (section 14.2.1.3), skew-induced errors at production scale translate to hundreds of thousands of dollars in annual cost). Đặc trưng các cửa hàng biến đổi (transform) này
liên tục (sự) rò rỉ thành một một-lần cơ sở hạ tầng sự đầu tư với (có thể) đo lường (được) các lợi nhuận (returns) (Feature stores transform this continuous leakage into a one-time infrastructure investment with measurable returns). Uber’s
Michelangelo nền tảng cho thấy (như thế nào) những tính kinh tế (economics) đó diễn ra (play out) (như thế nào) tại quy mô (Uber’s Michelangelo platform shows how those economics play out at scale).
Ví dụ 14.1: Uber Michelangelo đặc trưng cửa hàng
Bối cảnh: Uber’s Michelangelo nền tảng đã giúp thiết lập (cái) sản xuất đặc trưng-cửa hàng mẫu
(Hermann và Del Balso 2017a), (việc) giải quyết đào tạo-phục vụ sự sai lệch và sự tái sử dụng (xuyên) qua nhiều
các mô hình và các đội (đang) cung cấp năng lượng (powering) chuyến đi (ride) việc định giá, ETA sự dự đoán, và gian lận sự phát hiện.
Sự thấu hiểu: Các dữ liệu (nhà) khoa học tính toán các đặc trưng trong Spark cho đào tạo, trong khi các kỹ sư triển khai lại
(cái) cùng logic bằng Java cho phục vụ. Michelangelo’s đặc trưng cửa hàng (đã) di chuyển đặc trưng sự tính toán
vào một (được) chia sẻ hệ thống (thứ) mà phục vụ đào tạo thông qua Hive và sản xuất thông qua Cassandra,
với đặc trưng các định nghĩa (được) viết một lần và (được) biên dịch (compiled) thành lô và trực tuyến các sự triển khai.
Các hệ thống bài học: Đặc trưng các cửa hàng biến (turn) sự nhất quán từ một đội quy ước thành cơ sở hạ tầng.
Thời điểm-trong-thời gian (Point-in-time) tính đúng đắn ngăn chặn (sự) rò rỉ, đặc trưng việc lập phiên bản kích hoạt an toàn (sự) lặp (iteration), và một
(được) tập trung hóa danh mục (catalog) hỗ trợ (sự) tái sử dụng (xuyên) qua lớn mô hình các danh mục (đầu tư) (portfolios).
Sự sai lệch sự phát hiện trong CI/CD (Được) Tự động hóa các đường ống nên xác thực đặc trưng sự nhất quán trước khi sự triển-
khai (Skew detection in CI/CD Automated pipelines should validate feature consistency before deploy-ment). (Mã) Liệt kê 14.2 cho thấy một hàm (thứ) mà so sánh đào tạo và phục vụ đặc trưng các sự phân phối (đang) sử dụng
(cái) Kolmogorov-Smirnov bài kiểm tra, (việc) từ chối sự triển khai khi bất kỳ đặc trưng (nào) phân kỳ vượt ra ngoài một ngưỡng (Listing 14.2 shows a function that compares training and serving feature distributions using the Kolmogorov-Smirnov test, rejecting deployment when any feature diverges beyond a threshold).
(Mã) Liệt kê 14.2: Đặc trưng Sự sai lệch Sự xác thực: Này hàm so sánh đào tạo và phục vụ đặc trưng các sự phân phối (đang) sử dụng (cái) Kolmogorov-
Smirnov bài kiểm tra, (việc) từ chối sự triển khai khi bất kỳ đặc trưng (nào) phân kỳ vượt ra ngoài một (có thể) cấu hình (được) ngưỡng (Listing 14.2: Feature Skew Validation: This function compares training and serving feature distributions using the Kolmogorov-Smirnov test, rejecting deployment when any feature diverges beyond a configurable threshold).
def validate_no_skew(
training_features, serving_features, threshold=0.1
):
"""Reject deployment if feature distributions diverge."""
for feature in training_features.columns:
ks_stat = ks_2samp(
training_features[feature], serving_features[feature]
)
if ks_stat.statistic > threshold:
raise SkewDetectedError(
f"{feature}: KS={ks_stat.statistic:.3f}"
)
14.4.1.3 Việc lập phiên bản và dòng dõi
Dòng dõi việc theo dõi và việc lập phiên bản triển khai tính có thể tái tạo (phần 14.2.1), thứ (mà) yêu cầu tất cả
các đồ tạo tác (đang) ảnh hưởng (tới) mô hình hành vi (để) được lập phiên bản (Lineage tracking and versioning implement reproducibility (section 14.2.1), which requires all artifacts influencing model behavior to be versioned). Không giống như truyền thống phần mềm, ML các mô hình
phụ thuộc vào nhiều (đang) thay đổi các đồ tạo tác: đào tạo dữ liệu, đặc trưng kỹ thuật logic, (được) đào tạo mô hình
các tham số, và cấu hình các thiết lập (Unlike traditional software, ML models depend on multiple changing artifacts: training data, feature engineering logic, trained model parameters, and configuration settings). MLOps các thực hành thực thi (việc) theo dõi của các phiên bản (xuyên) qua tất cả
đường ống các thành phần để quản lý này độ phức tạp (MLOps practices enforce tracking of versions across all pipeline components to manage this complexity).
Dữ liệu việc lập phiên bản cho phép các đội (để) chụp ảnh nhanh các tập dữ liệu tại cụ thể các điểm trong thời gian và liên kết (associate) chúng
với cụ thể mô hình (các) lần chạy (runs), bao gồm cả thô dữ liệu và (được) xử lý các đồ tạo tác (Data versioning allows teams to snapshot datasets at specific points in time and associate them with particular model runs, including both raw data and processed artifacts). Mô hình việc lập phiên bản
đăng ký (registers) (được) đào tạo các mô hình như (là) bất biến các đồ tạo tác cùng với siêu dữ liệu (chẳng) hạn như đào tạo các tham số,
sự đánh giá các số liệu, và môi trường các thông số kỹ thuật (specifications) (Model versioning registers trained models as immutable artifacts alongside metadata such as training parameters, evaluation metrics, and environment specifications). Mô hình các cơ quan đăng ký8 cung cấp (được) cấu trúc các giao diện
cho (việc) thăng cấp (promoting), (việc) triển khai, và (việc) quay lui (rolling back) mô hình các phiên bản, với một số hỗ trợ dòng dõi (sự) trực quan-
hóa (visualiza-tion) (đang) theo dõi (tracing) (cái) đầy (đủ) sự phụ thuộc đồ thị từ thô dữ liệu đến (được) triển khai dự đoán (MLflow Dự án 2026;
Cloud 2024b) (Model registries8 provide structured interfaces for promoting, deploying, and rolling back model versions, with some supporting lineage visualiza-tion tracing the full dependency graph from raw data to deployed prediction (MLflow Project 2026; Cloud 2024b)).

786
14.4 Sự phát triển Cơ sở hạ tầng
9
Tính lũy đẳng (Idempotency): Này thuộc-
tính (prop-erty) đảm bảo rằng (việc) chạy lại một
đường ống giai đoạn mang lại (yields) một (giống) hệt-
nhau (iden-tical) kết quả, nhưng (cái) đào tạo
giai đoạn vi phạm điều này (theo) mặc-
định (de-fault) do (các) nguồn của (tính) ngẫu-
nhiên (ran-domness) giống như (tuyển) tập (weight) (sự) khởi tạo-
tạo (initial-ization).
Mà không (có) (tính) lũy đẳng (idempo-tency), một đường ống (sự) chạy lại sau
một (sự) xác thực hay triển khai (sự) thất-
bại (fail-ure) sẽ sản xuất một (một cách) hơi (slightly)
khác mô hình, (việc) làm mất hiệu lực (invalidating)
(cái) ban đầu hiệu suất (các) số-
liệu (met-rics) và (việc) làm (cho) việc gỡ lỗi
không đáng tin cậy.
Sản xuất các hệ-
thống (sys-tems) do đó thực thi (tính) tất-
định (deter-minism) bằng (cách) (việc) cố định tất cả ngẫu nhiên
các hạt giống (seeds), thường thành một đơn số nguyên
giống như 42, như (là) một trong vài (các) sự kiểm-
soát (con-trols) (cùng với (có tính) tất định
các hạt nhân (kernels), (được) cố định thư viện các phiên bản,
và (được) kiểm soát dữ liệu (sự) sắp xếp (ordering))
(được) cần (needed) cho tính có thể tái tạo.
Những (mang tính) bổ sung (complementary) các thực hành này hình thành (cái) dòng dõi lớp của một ML hệ thống (These complementary practices form the lineage layer of an ML system). (Cái) dòng dõi lớp kích hoạt
sự tự xem xét (introspection), sự thử nghiệm, và quản trị (governance) bằng (cách) (việc) bảo tồn (cái) chuỗi của chứng cứ (evidence) (được) cần để
chẩn đoán một (bị) xuống cấp mô hình: liệu (cái) đầu vào sự phân phối (có) khớp (với) đào tạo dữ liệu, liệu đặc trưng
các định nghĩa (có) thay đổi, và liệu (cái) (được) triển khai mô hình phiên bản (có) khớp (với) (cái) (đang) phục vụ cơ sở hạ tầng (hay không) (The lineage layer enables introspection, experimentation, and governance by preserving the chain of evidence needed to diagnose a degraded model: whether the input distribution matched training data, whether feature definitions changed, and whether the deployed model version matched the serving infrastructure).
Bằng (cách) (việc) nâng tầm (elevating) việc lập phiên bản và dòng dõi thành hạng-nhất (first-class) (những) công dân trong (cái) hệ thống thiết kế, MLOps kích hoạt các đội
để xây dựng và duy trì (đáng) tin cậy, (có thể) kiểm toán (được), và (có thể) tiến hóa (được) (evolvable) ML các quy trình làm việc tại quy mô (By elevating versioning and lineage to first-class citizens in the system design, MLOps enables teams to build and maintain reliable, auditable, and evolvable ML workflows at scale).
14.4.2 (Mang tính) Liên tục các đường ống và sự tự động hóa
Đặc trưng các cửa hàng và việc lập phiên bản các hệ thống giải quyết dữ liệu sự nhất quán (một cách) tĩnh: chúng đảm bảo rằng các đặc trưng
được tính toán (một cách) chính xác tại một điểm trong thời gian (Feature stores and versioning systems address data consistency statically: they ensure that features are computed correctly at a point in time). Sự tự động hóa kích hoạt những các hệ thống này để tiến hóa (một cách) liên tục,
(việc) đồng bộ hóa (synchronizing) dữ liệu việc tiền xử lý, sự đào tạo, sự đánh giá, và sự phát hành thành (được) tích hợp các quy trình làm việc (thứ) mà
phản hồi (tới) mới dữ liệu, (đang) dịch chuyển các mục tiêu, và (thuộc về) hoạt động các sự ép buộc (Orr và cộng sự. 2021) (Automation enables these systems to evolve continuously, synchronizing data preprocessing, training, evaluation, and release into integrated workflows that respond to new data, shifting objectives, and operational constraints (Orr et al. 2021)).
14.4.2.1 CI/CD các đường ống
Đặc trưng các cửa hàng và việc lập phiên bản các hệ thống giải quyết (cái) dữ liệu mặt (side) của sự nhất quán; CI/CD các đường ống giải quyết
(cái) quy trình mặt, (việc) đảm bảo rằng các sự thay đổi chảy qua (được) xác thực các giai đoạn thay vì ad hoc các sự triển khai (Feature stores and versioning systems address the data side of consistency; CI/CD pipelines address the process side, ensuring that changes flow through validated stages rather than ad hoc deployments).
ML CI/CD các đường ống phải xử lý độ phức tạp vắng mặt (absent) từ truyền thống phần mềm: dữ liệu các sự phụ thuộc,
mô hình đào tạo các quy trình làm việc, và đồ tạo tác việc lập phiên bản (thứ) mà ghép nối (couple) mã các sự thay đổi với (thuộc về) thống kê hành vi
các sự thay đổi (ML CI/CD pipelines must handle complexity absent from traditional software: data dependencies, model training workflows, and artifact versioning that couple code changes to statistical behavior changes).
Một điển hình ML CI/CD đường ống bao gồm của (được) phối hợp các giai đoạn: kiểm tra (checking out) (được) cập nhật mã, (việc) tiền-
xử lý (pre-processing) đầu vào dữ liệu, (việc) đào tạo một ứng cử viên mô hình, (việc) xác thực hiệu suất, (việc) đóng gói (cái) mô hình,
và (việc) triển khai (tới) một (đang) phục vụ môi trường (A typical ML CI/CD pipeline consists of coordinated stages: checking out updated code, pre-processing input data, training a candidate model, validating performance, packaging the model, and deploying to a serving environment). Trong một số các trường hợp, các đường ống cũng bao gồm các bộ kích hoạt cho (tính) tự-
động (auto-matic) sự đào tạo lại dựa trên dữ liệu sự trôi dạt hay hiệu suất sự xuống cấp (In some cases, pipelines also include triggers for auto-matic retraining based on data drift or performance degradation). Bằng (cách) (việc) hệ thống hóa (codifying) những các bước này, CI/CD
các đường ống9 giảm thiểu thủ công sự can thiệp, thực thi chất lượng các sự kiểm tra, và hỗ trợ liên tục sự cải thiện
của (được) triển khai các hệ thống (By codifying these steps, CI/CD pipelines9 reduce manual intervention, enforce quality checks, and support continuous improvement of deployed systems).
ML-tập trung (ML-focused) CI/CD xếp lớp hai (các) tầng (tiers) của công cụ cho một lý do (ML-focused CI/CD layers two tiers of tooling for one reason). Một đa-mục đích CI/CD bộ-điều-
phối (orches-trator) (Jenkins, CircleCI (2024), hay GitHub Actions (GitHub, Inc. 2024b)) quản lý phiên bản-kiểm soát
các sự kiện và sự thực thi logic, nhưng (cái) ML lớp phải (một cách) bổ sung lập phiên bản dữ liệu, chặn (gate) (dựa) trên mô hình các số liệu,
và kích hoạt sự đào tạo lại (A general-purpose CI/CD orches-trator (Jenkins, CircleCI (2024), or GitHub Actions (GitHub, Inc. 2024b)) manages version-control events and execution logic, but the ML layer must additionally version data, gate on model metrics, and trigger retraining). Các đội do đó thêm (vào) một đặc thù-miền (domain-specific) nền tảng (Kubeflow (Authors 2024),
Metaflow (Netflix 2024), hay Prefect (Prefect Các công nghệ, Inc. 2024)) (thứ) mà cung cấp (supplies) cao-cấp-hơn
các sự trừu tượng hóa cho những (mang tính) ML-đặc thù các tác vụ đó (Teams therefore add a domain-specific platform (Kubeflow (Authors 2024), Metaflow (Netflix 2024), or Prefect (Prefect Technologies, Inc. 2024)) that supplies higher-level abstractions for those ML-specific tasks).
Mà không (có) này sự tự động hóa, mô hình sự triển khai xuống cấp thành một thủ công, dễ-gây-lỗi (error-prone) quy trình: một
kỹ sư đào tạo lại (ở) (địa) phương, sao chép các đồ tạo tác sang một chạy thử (staging) máy chủ, và thăng cấp (promotes) (lên) sản xuất với không
đảm bảo (nào) (rằng) (cái) dữ liệu, mã, hay các siêu tham số khớp (với) (những) gì đã được xác thực (Without this automation, model deployment degrades into a manual, error-prone process: an engineer retrains locally, copies artifacts to a staging server, and promotes to production with no guarantee that the data, code, or hyperparameters match what was validated). (Cái) chi phí của (những) như vậy ad
hoc các quy trình làm việc cộng dồn với đội quy mô và sự triển khai tần suất, (việc) sản xuất cấu hình sự trôi dạt
và im lặng các sự hồi quy (thứ) mà làm nổi lên (surface) chỉ sau (khi) (cái) mô hình đã phục vụ không chính xác các dự đoán (The cost of such ad hoc workflows compounds with team size and deployment frequency, producing configuration drift and silent regressions that surface only after the model has served incorrect predictions).
Hình 14.6 cho thấy (như thế nào) một (có tính) đại diện CI/CD đường ống giải quyết những các rủi ro này (như thế nào), (đang) bắt đầu với một
tập dữ liệu và đặc trưng kho lưu trữ từ (đó) dữ liệu được ăn (vào) và (được) xác thực (Figure 14.6 shows how a representative CI/CD pipeline addresses these risks, beginning with a dataset and feature repository from which data is ingested and validated). (Được) Xác thực dữ liệu (được) sau đó
(được) chuyển đổi cho mô hình sự đào tạo (Validated data is then transformed for model training). Một (sự) đào tạo lại bộ kích hoạt, (chẳng) hạn như một (được) lên lịch công việc hay hiệu suất (thuộc về) ngưỡng-
(thresh-old), khởi xướng quy trình này (một cách) tự động (A retraining trigger, such as a scheduled job or performance thresh-old, initiates this process automatically). Một khi sự đào tạo và siêu tham số sự tinh chỉnh (tuning) là hoàn tất, (cái)
(đang) kết quả mô hình trải qua (undergoes) sự đánh giá so với (against) (được) xác định trước các tiêu chí (Once training and hyperparameter tuning are complete, the resulting model undergoes evaluation against predefined criteria). Nếu (cái) mô hình thỏa mãn (cái) (được) yêu cầu
các ngưỡng, nó được đăng ký trong một mô hình kho lưu trữ cùng với siêu dữ liệu, hiệu suất các số liệu, và
dòng dõi thông tin (If the model satisfies the required thresholds, it is registered in a model repository along with metadata, performance metrics, and lineage information). Cuối cùng, (cái) mô hình được triển khai lại vào (cái) sản xuất hệ thống, (việc) đóng (cái)
vòng lặp và (việc) kích hoạt (mang tính) liên tục sự phân phối của (được) cập nhật các mô hình (Finally, the model is deployed back into the production system, closing the loop and enabling continuous delivery of updated models).
Để minh họa những các khái niệm này trong thực tế, xem xét một hình ảnh sự phân loại mô hình (đang) dưới (sự) (mang tính) chủ động (active)
sự phát triển (To illustrate these concepts in practice, consider an image classification model under active development). Khi một dữ liệu nhà khoa học cam kết (commits) các sự thay đổi (tới) một GitHub (GitHub, Inc. 2024a) kho lưu trữ,
một Jenkins đường ống được kích hoạt (When a data scientist commits changes to a GitHub (GitHub, Inc. 2024a) repository, a Jenkins pipeline is triggered). (Cái) đường ống nạp (fetches) (được) cập nhật dữ liệu, thực hiện việc tiền xử lý, và
khởi xướng mô hình sự đào tạo (The pipeline fetches updated data, performs preprocessing, and initiates model training). Các sự thử nghiệm được theo dõi (đang) sử dụng MLflow (Databricks 2024) thứ (mà) ghi nhật ký các số liệu
và lưu trữ mô hình các đồ tạo tác (Experiments are tracked using MLflow (Databricks 2024) which logs metrics and stores model artifacts). Sau (khi) vượt qua (được) tự động hóa sự đánh giá các bài kiểm tra, (cái) mô hình được đóng gói (containerized) và
(được) triển khai (tới) một chạy thử môi trường (đang) sử dụng Kubernetes (Đám mây Nguyên bản (Native) Máy tính Tổ chức 2024a) (After passing automated evaluation tests, the model is containerized and deployed to a staging environment using Kubernetes (Cloud Native Computing Foundation 2024a)).
Nếu (cái) mô hình đáp ứng sự xác thực các tiêu chí trong chạy thử, (cái) đường ống điều phối (được) kiểm soát sự triển khai
các chiến lược (chẳng) hạn như chim yến (canary) việc kiểm thử ((được) chi tiết trong phần 14.4.2.3), (một cách) dần dần (việc) định tuyến (routing) sản xuất lưu lượng truy cập (tới)
(cái) mới mô hình trong khi (đang) giám sát chính các số liệu cho (các) sự bất thường (anomalies) (If the model meets validation criteria in staging, the pipeline orchestrates controlled deployment strategies such as canary testing (detailed in section 14.4.2.3), gradually routing production traffic to the new model while monitoring key metrics for anomalies). Trong trường hợp của hiệu suất các sự hồi quy, (cái)
hệ thống có thể (một cách) tự động khôi phục (revert) (về) một (trước) đó mô hình phiên bản (In case of performance regressions, the system can automatically revert to a previous model version).
CI/CD các đường ống đóng một trung tâm vai trò trong (việc) kích hoạt (có thể) mở rộng quy mô, (có thể) lặp lại, và an toàn ML sự triển khai (CI/CD pipelines play a central role in enabling scalable, repeatable, and safe ML deployment).
Trong trưởng thành MLOps các môi trường, CI/CD không phải (là) (có tính) tùy chọn mà (là) (thuộc về) nền tảng, (việc) biến đổi ad hoc

787
Dữ liệu sự xác thực
Dữ liệu
sự chuyển đổi
Mô hình
sự xác thực
Mô hình
sự đăng ký
Tập dữ liệu
sự ăn (vào)
Mô hình
sự đào tạo/sự tinh chỉnh (tuning)
Mô hình
sự đánh giá
Liên tục đào tạo đường ống
Tập dữ liệu &
đặc trưng
kho lưu trữ
Mô hình
kho lưu trữ
ML siêu dữ liệu
& đồ tạo tác
kho lưu trữ
Tập dữ liệu
<\>
(Được) Đào tạo
Mô hình
<\>
(Được) Đào tạo đường ống
siêu dữ liệu & các đồ tạo tác <\>
Sự đào tạo lại
bộ kích hoạt
Mô hình
đào tạo công cụ (engine)
Mô hình xử lý
công cụ
Mô hình đánh giá
công cụ
Hình 14.6: ML CI/CD Đường ống: (Cái) đường ống bắt đầu với tập dữ liệu và đặc trưng các kho lưu trữ, chảy qua dữ liệu sự xác thực,
sự chuyển đổi, sự đào tạo, sự đánh giá, và mô hình sự đăng ký các giai đoạn, (sau) đó triển khai (tới) sản xuất (Figure 14.6: ML CI/CD Pipeline: The pipeline begins with dataset and feature repositories, flows through data validation, transformation, training, evaluation, and model registration stages, then deploys to production). Sự đào tạo lại các bộ kích hoạt khởi xướng (cái)
chu kỳ (một cách) tự động, trong khi siêu dữ liệu và đồ tạo tác các kho lưu trữ đảm bảo tính có thể tái tạo và quản trị (Retraining triggers initiate the cycle automatically, while metadata and artifact repositories ensure reproducibility and governance). (Được) Thích ứng từ Google
Cloud’s MLOps liên tục sự phân phối và sự tự động hóa đường ống sự hướng dẫn (Google Cloud 2026b) (Adapted from Google Cloud’s MLOps continuous delivery and automation pipeline guidance (Google Cloud 2026b)).
sự thử nghiệm thành (được) cấu trúc, (về mặt) hoạt động vững chắc (sound) sự phát triển (experimentation into structured, operationally sound development). Google’s TFX (TensorFlow
Extended) nền tảng làm ví dụ (minh họa) (exemplifies) (như thế nào) những CI/CD các nguyên tắc này mở rộng quy mô (tới) sản xuất (như thế nào) (Google’s TFX (TensorFlow Extended) platform exemplifies how these CI/CD principles scale to production).
Ví dụ 14.2: Google TFX sản xuất ML các đường ống
Bối cảnh: TensorFlow (Được) Mở rộng (Extended) (TFX) (đã) xuất hiện từ Google’s sản xuất ML cơ sở hạ tầng,
(việc) cung cấp (có thể) tái sử dụng (được) các thành phần cho dữ liệu sự xác thực, sự chuyển đổi, sự đào tạo, mô hình sự phân tích,
và sự triển khai (Baylor và cộng sự. 2017).
Sự thấu hiểu: Trước TFX, các đội (đã) xây dựng (được) thiết kế riêng (bespoke) các đường ống cho mỗi ML dự án, (một cách) lặp đi lặp lại (việc) giải quyết
dữ liệu sự xác thực, lược đồ sự thực thi (enforcement), mô hình sự xác thực, và sự triển khai (việc) chặn (gating). TFX (đã) chuẩn-
hóa những các bước đó thông qua các thành phần (chẳng) hạn như ExampleGen, StatisticsGen, SchemaGen,
ExampleValidator, Transform, Trainer, Evaluator, và Pusher.
Các hệ thống bài học: Sản xuất ML các đường ống cần đồ tạo tác kỷ luật, không (phải) chỉ tác vụ sự điều phối.
TFX làm (cho) mỗi bước sản xuất (được) lập phiên bản các đồ tạo tác với siêu dữ liệu, vì vậy sản xuất các vấn đề có thể được
theo dõi ngược lại thông qua (cái) chính xác dữ liệu, mã, và cấu hình (thứ) mà (đã) sản xuất (cái) (được) triển khai mô hình.
14.4.2.2 Đào tạo các đường ống
CI/CD các đường ống điều phối (cái) tổng thể quy trình làm việc, nhưng sự đào tạo chính nó yêu cầu (được) chuyên môn hóa cơ sở hạ-
tầng (CI/CD pipelines orchestrate the overall workflow, but training itself requires specialized infras-tructure). Mô hình sự đào tạo, nơi các thuật toán được tối ưu hóa để học các mẫu từ dữ liệu, xây dựng trên
(cái) (được) phân tán đào tạo các khái niệm (được) bao phủ trong Chương 8 (Model training, where algorithms are optimized to learn patterns from data, builds on the distributed training concepts covered in Chapter 8). Trong (phạm vi) MLOps, đào tạo các hoạt động trở thành
phần của một (có thể) tái tạo (được), (có thể) mở rộng quy mô, và (được) tự động hóa đường ống (đang) hỗ trợ liên tục sự thử nghiệm và
(đáng) tin cậy sản xuất sự triển khai (Within MLOps, training activities become part of a reproducible, scalable, and automated pipeline supporting continual experimentation and reliable production deployment).
Các khuôn khổ (chẳng) hạn như TensorFlow (Abadi và cộng sự. 2016), PyTorch (Paszke và cộng sự. 2019), và Keras
(Chollet và cộng sự. 2024) cung cấp (cái) (có tính) mô đun các thành phần cho (việc) xây dựng và (việc) đào tạo các mô hình, và (các)
khuôn khổ-sự lựa chọn các nguyên tắc từ Chương 7 mang vào sản xuất (mà) không thay đổi (Frameworks such as TensorFlow (Abadi et al. 2016), PyTorch (Paszke et al. 2019), and Keras (Chollet et al. 2024) supply the modular components for building and training models, and the framework-selection principles from Chapter 7 carry into production unchanged). (Cái) (thuộc về) hoạt động
câu hỏi (mà) này phần trả lời là khác: cái nào (mang tính) khám phá đào tạo logic tốt nghiệp (graduates) thành một (được) lập phiên bản,
(được) kiểm thử sự đào tạo lại công việc, và khi nào (The operational question this section answers is different: which exploratory training logic graduates into a versioned, tested retraining job, and when).
Vượt ra ngoài khả năng mở rộng, tính có thể tái tạo là một chính mục tiêu (Beyond scalability, reproducibility is a key objective). Đào tạo các kịch bản (scripts) và các cấu hình được
phiên bản-(được) kiểm soát (đang) sử dụng các công cụ giống như Git (Torvalds và Hamano 2024) và (được) lưu trữ (hosted) trên các nền tảng (chẳng)
hạn như GitHub (GitHub, Inc. 2024a) (Training scripts and configurations are version-controlled using tools like Git (Torvalds and Hamano 2024) and hosted on platforms such as GitHub (GitHub, Inc. 2024a)). (Mang tính) Tương tác sự phát triển các môi trường, bao gồm Jupyter (Project
Jupyter 2024) các sổ tay (notebooks), gói gọn (encapsulate) dữ liệu sự ăn (vào), đặc trưng kỹ thuật, đào tạo các thói quen (routines), và
sự đánh giá logic trong một (được) hợp nhất định dạng (Interactive development environments, including Jupyter (Project Jupyter 2024) notebooks, encapsulate data ingestion, feature engineering, training routines, and evaluation logic in a unified format). Trong sản xuất, các sổ tay nên được đối xử như (là) (sự) khám phá
các bộ khung (harnesses): (được) xác thực các sự chuyển đổi, đào tạo mã, và sự đánh giá các sự kiểm tra phải được trích xuất (extracted) thành
(được) lập phiên bản, (được) kiểm thử các mô-đun trước khi chúng trở thành (được) lên lịch sự đào tạo lại các công việc (In production, notebooks should be treated as exploration harnesses: validated transformations, training code, and evaluation checks must be extracted into versioned, tested modules before they become scheduled retraining jobs).

789
10
Đám mây ML Sự đào tạo
Các tính kinh tế (Economics): GPT-3 đào tạo
chi phí đã được ước tính trong
(hàng) các triệu của đô la khi
(được) định giá bằng V100 GPU-các giờ
(Li 2020). Tinh-chỉnh các chi phí
khác nhau (vary) theo mô hình kích thước, nhà cung cấp,
tập dữ liệu, và số lượng của đào tạo
các bước.
Đốm (Spot) các 인스턴스 (instances)
và Đốm các VM có thể giảm (thiểu) phiên-
bản (in-stance) các giá nhưng giới thiệu một
sự đánh đổi (trade-off): AWS Spot Instances
và Google Cloud Spot VMs
có thể bị (bị) gián đoạn hay bị ưu-
tiên (pre-empted), (việc) yêu cầu điểm kiểm tra-
và-tiếp tục (checkpoint-and-resume) cơ sở hạ tầng cho
chịu-lỗi (fault-tolerant) đào tạo khối lượng công-
việc (work-loads) (Amazon Web Services
2026; Google Cloud 2026c).
đào tạo các quy trình (xuyên) qua (được) phân tán các hệ thống (training processes across distributed systems). Đám mây các nhà cung cấp cung cấp (được) quản lý các dịch vụ (thứ) mà (cung cấp) (provision)
hiệu-suất-cao (high-performance) (việc) tính toán các tài nguyên, bao gồm GPU và Tensor Xử lý Đơn vị (TPU) (các) bộ tăng-
tốc (accelera-tors), theo yêu cầu (on demand)10 (Cloud providers offer managed services that provision high-performance computing resources, including GPU and Tensor Processing Unit (TPU) accelera-tors, on demand10). Phụ thuộc vào (cái) nền tảng, các đội cấu trúc của riêng họ đào tạo các quy trình làm việc hay dựa
vào hoàn toàn (được) quản lý các dịch vụ (chẳng) hạn như Vertex AI Fine Tuning (Cloud 2024a), thứ (mà) hỗ trợ (được) tự động hóa
sự thích ứng của nền tảng các mô hình với mới các tác vụ (Depending on the platform, teams construct their own workflows or rely on fully managed services such as Vertex AI Fine Tuning (Cloud 2024a), which support automated adaptation of foundation models to new tasks). Phần cứng tính có sẵn (availability), (thuộc về) khu vực (regional) (sự) truy cập các giới hạn,
và chi phí các sự ép buộc duy trì (những) quan trọng các sự xem xét khi (đang) thiết kế dựa trên-đám mây đào tạo các hệ thống
(OECD.AI 2021) (Hardware availability, regional access restrictions, and cost constraints remain important considerations when designing cloud-based training systems (OECD.AI 2021)).
Những các thực hành này hội tụ (converge) tại một đơn (thuộc về) hoạt động ranh giới (These practices converge on a single operational boundary). (Mang tính) Khám phá đào tạo logic (thứ) mà chứng minh (proves)
(hiệu quả) (out) trong một sổ tay, một khi nó sản xuất một (được) xác thực mô hình, (thì) (được) phiên bản-kiểm soát và (được) trích xuất thành một
(được) lên lịch sự đào tạo lại công việc (được) kích hoạt bởi dữ liệu các bản cập nhật hay hiệu suất việc giám sát (Exploratory training logic that proves out in a notebook, once it produces a validated model, is version-controlled and extracted into a scheduled retraining job triggered by data updates or performance monitoring). (Cái) sự khám phá
bộ khung (thứ) mà (đã) làm (cho) (sự) lặp (iteration) nhanh không phải (là) (những) gì chạy trong sản xuất; (cái) (được) kiểm thử, (được) lập phiên bản mô-đun là (như vậy), và
(cái) kỷ luật của đó sự bàn giao (hand-off) là (những) gì tách biệt (separates) một (có thể) tái tạo (được) đường ống khỏi một mỏng manh (một) (The exploration harness that made iteration fast is not what runs in production; the tested, versioned module is, and the discipline of that hand-off is what separates a reproducible pipeline from a fragile one). Thông qua
(được) chuẩn hóa các quy trình làm việc, (được) lập phiên bản các môi trường, và (được) tự động hóa sự điều phối, MLOps chuyển tiếp (transitions)
mô hình sự đào tạo từ ad hoc sự thử nghiệm sang mạnh mẽ (robust), (có thể) lặp lại (được) các hệ thống (đang) đáp ứng sản xuất
các tiêu chuẩn cho độ tin cậy, tính có thể theo dõi, và hiệu suất (Through standardized workflows, versioned environments, and automated orchestration, MLOps transitions model training from ad hoc experimentation to robust, repeatable systems meeting production standards for reliability, traceability, and performance).
Sự đào tạo lại quyết định bộ khung (được) Tự động hóa đào tạo các đường ống giới thiệu một tới hạn quyết định liên-
quan (re-garding) của chúng sự thực thi tần suất (Retraining decision framework Automated training pipelines introduce a critical decision re-garding their execution frequency). (Việc) Quyết định khi nào để đào tạo lại một mô hình yêu cầu (việc) cân bằng độ chính xác
sự bảo trì so với (against) (thuộc về) tính toán các chi phí (Deciding when to retrain a model requires balancing accuracy maintenance against computational costs). Ba phổ biến các chiến lược tồn tại, mỗi (chiến lược) với khác biệt các sự đánh-
đổi (Three common strategies exist, each with distinct trade-offs). Bảng 14.8 cung cấp (các) điển hình các lịch trình (xuyên) qua các miền, từ hàng ngày sự đào tạo lại cho (một cách) nhanh chóng (đang) dịch chuyển
quảng cáo nhấp chuột sự dự đoán đến hàng quý các bản cập nhật cho ổn định (thuộc về) y tế hình ảnh (imaging) các ứng dụng (Table 14.8 provides typical schedules across domains, from daily retraining for rapidly shifting ad click prediction to quarterly updates for stable medical imaging applications):
Bảng 14.8: (Các) Điển hình Sự đào tạo lại Các lịch trình Theo Miền: Những (cái này) đại diện (cho) (các) bắt đầu các điểm; (mang tính) thực tế các nhịp độ (cadences) phụ thuộc vào (được) quan sát
sự trôi dạt các tỷ lệ và (thuộc về) kinh doanh tác động, và các tổ chức (một cách) điển hình hiệu chuẩn (calibrate) chúng thông qua (thuộc về) hoạt động kinh nghiệm (Table 14.8: Typical Retraining Schedules by Domain: These represent starting points; actual cadences depend on observed drift rates and business impact, and organizations typically calibrate them through operational experience).
Miền
Điển hình Lịch trình
Lý do (Rationale)
Quảng cáo nhấp chuột sự dự đoán
Hàng ngày
Người dùng các sự quan tâm (interests) dịch chuyển (một cách) nhanh chóng
Gian lận sự phát hiện
Hàng tuần
Tấn công các mẫu tiến hóa (một cách) liên tục
Nhu cầu (Demand) sự dự báo
Hàng tháng
(Thuộc về) Mùa vụ (Seasonal) các mẫu thay đổi (một cách) chậm chạp
(Thuộc về) Y tế hình ảnh
Hàng quý
Bệnh (Disease) các sự trình bày (presentations) là ổn định
Những các lịch trình đó là (các) bắt đầu các điểm, không phải (các) quy tắc (Those schedules are starting points, not rules). (Được) Lên lịch sự đào tạo lại chạy trên một (được) cố định nhịp độ (cadence),
(chẳng) hạn như hàng ngày, hàng tuần, hay hàng tháng, bất kể của hiệu suất các số liệu (Scheduled retraining runs on a fixed cadence, such as daily, weekly, or monthly, regardless of performance metrics). Nó là đơn giản để triển khai
và đảm bảo rằng gần đây dữ liệu cuối cùng đi vào (cái) mô hình, nhưng nó có thể lãng phí (việc) tính toán khi (cái)
sự phân phối là ổn định hay phản hồi quá chậm khi một sự dịch chuyển xảy ra giữa (thuộc về) lịch (calendar) các lần chạy (It is simple to implement and guarantees that recent data eventually enters the model, but it can waste compute when the distribution is stable or respond too slowly when a shift happens between calendar runs).
(Được) Kích hoạt sự đào tạo lại buộc (cái) sự đào tạo lại quyết định vào (được) quan sát sự xuống cấp (Triggered retraining ties the retraining decision to observed degradation). Nó tối ưu hóa (việc) tính toán
chi phí bằng (cách) (việc) đào tạo lại chỉ khi (việc) giám sát phát hiện hiệu suất (sự) mất (mát) hay sự trôi dạt vượt ra ngoài các ngưỡng, nhưng
nó yêu cầu mạnh mẽ từ xa (đo lường) (telemetry) và cẩn thận sự hiệu chuẩn để tránh (các) dương tính giả hay (bị) bỏ lỡ sự xuống cấp (It optimizes compute cost by retraining only when monitoring detects performance loss or drift beyond thresholds, but it requires robust telemetry and careful calibration to avoid false positives or missed degradation).
(Mã) Liệt kê 14.3 thể hiện (cái) bộ kích hoạt như (là) một quyết định hàm thay vì một đặc thù-sự triển khai cấu-
hình (configura-tion) tệp: đào tạo lại khi (cái) (được) đo lường (sự) mất (mát) từ tính cũ (staleness) vượt quá (cái) chi phí và rủi ro của một mới đào tạo
lần chạy (Listing 14.3 expresses the trigger as a decision function rather than a deployment-specific configura-tion file: retrain when the measured loss from staleness exceeds the cost and risk of a new training run). Trong (cái) gian lận-sự phát hiện tình huống (được) sử dụng ở đây, một 2 phần trăm hàng ngày suy tàn (decay) tỷ lệ làm (cho) hàng ngày sự đào tạo lại
(thành) (cái) hòa vốn (break-even) điểm nơi sự đào tạo lại chi phí khớp (với) (cái) (sự) mất (mát) từ cũ các dự đoán (In the fraud-detection scenario used here, a 2 percent daily decay rate makes daily retraining the break-even point where retraining cost matches the loss from stale predictions).
Liên tục sự đào tạo lại cập nhật (cái) mô hình (một cách) tăng dần (incrementally) khi (được) dán nhãn dữ liệu đến (arrives), hoặc thông qua
trực tuyến học tập hoặc (mang tính) định kỳ vi-các bản cập nhật (Continuous retraining updates the model incrementally as labeled data arrives, either through online learning or periodic micro-updates). Điều này giữ (cho) (cái) mô hình (ở trạng thái) hiện tại với tối thiểu độ trễ, nhưng
nó nâng cao (cái) sự xác thực gánh nặng (burden) bởi vì ồn ào các nhãn hay (mang tính) đối kháng (adversarial) dữ liệu có thể được kết hợp (incorporated) trước khi
(các) con người đã đánh giá (reviewed) (cái) sự dịch chuyển (This keeps the model current with minimal latency, but it raises the validation burden because noisy labels or adversarial data can be incorporated before humans have reviewed the shift).
(Cái) (thuộc về) hoạt động sự lựa chọn do đó phụ thuộc vào bốn các sự ép buộc: sự đào tạo lại chi phí, sự xác thực cơ sở hạ-
tầng, sự quay lui khả năng, và nhãn tính có sẵn (The operating choice therefore depends on four constraints: retraining cost, validation infrastruc-ture, rollback capability, and label availability). Lớn các mô hình có thể tốn (hàng) (các) chục của (hàng) ngàn của đô la
mỗi lần chạy; (được) kích hoạt sự đào tạo lại yêu cầu mặt đất (sự) thật (ground truth) hay (đáng) tin cậy đại diện (proxy) các nhãn; và mọi (được) tự động hóa
(sự) cập nhật con đường cần đủ sự xác thực và sự quay lui sức chứa (capacity) để chứng minh rằng (cái) mới mô hình vượt trội (outperforms)
(cái) đường cơ sở (Large models may cost tens of thousands of dollars per run; triggered retraining requires ground truth or reliable proxy labels; and every automated update path needs enough validation and rollback capacity to prove that the new model outperforms the baseline). (Được) Lên lịch sự đào tạo lại phù hợp (suits) ổn định các miền, (được) kích hoạt sự đào tạo lại giải quyết (mang tính) dần dần sự trôi dạt,
và liên tục sự đào tạo lại thuộc về (một cách) nhanh chóng (đang) tiến hóa các sự phân phối nơi (việc) chờ đợi cho một (thuộc về) lịch
khoảng (interval) sẽ mất quá nhiều giá trị (Scheduled retraining suits stable domains, triggered retraining addresses gradual drift, and continuous retraining belongs to rapidly evolving distributions where waiting for a calendar interval would lose too much value).

790
14.4 Sự phát triển Cơ sở hạ tầng
11
Hệ thống Entropy: (Cái)
suy tàn tỷ lệ 𝛾khác nhau theo (các) bậc
của độ lớn (xuyên) qua các miền.
(Chuyển động) Nhanh-chóng (Fast-moving) các miền (xã hội
phương tiện (media) các sự gợi ý, (thuộc về) tài-
chính gian lận) thể hiện (các) nửa-
đời (half-lives) của (các) ngày đến (các) tuần; (chuyển động) chậm hơn
các miền ((thuộc về) y tế hình ảnh,
(thuộc về) công nghiệp sự kiểm tra) suy tàn
qua (các) tháng đến (các) năm.
Này
phạm vi quyết định (cái) tối-
thiểu cơ sở hạ tầng sự đầu-
tư: một mô hình với một ba-
ngày nửa-đời yêu cầu (mang tính) liên-
tục đào tạo cơ sở hạ tầng,
không (phải) một (được) lên lịch lô công việc,
trong khi một mô hình với một sáu-
tháng nửa-đời có thể đào tạo lại
hàng tuần tại một phần (fraction) của (cái) chi phí.
12
Nửa-Đời (từ (thuộc về) hạt nhân
vật lý, nơi nó đo lường
(cái) thời gian cho một nửa của một (có tính) phóng-
xạ (radioac-tive) mẫu để suy tàn): Trong ML
các hoạt động, (cái) phép ẩn dụ là
một (về mặt) toán học (có tính) thuận tiện
sự xấp xỉ, không (phải) một (có tính) phổ-
quát (univer-sal) định luật. Khi (thuộc về) lịch sử hiệu-
suất hỗ trợ một (có tính) mũ
suy tàn (sự) khớp (fit), (cái) (được) khớp
nửa-đời biến “khi nào nên
chúng ta đào tạo lại?” từ một (sự) phán đoán
lệnh gọi (call) thành một sự tính toán; khi
sự suy tàn là (thuộc về) mùa vụ, đột ngột, hay
(mang tính) đối kháng, (cái) mô hình phải
được thay thế bởi một (phong) phú hơn sự trôi dạt
quy trình.
(Mã) Liệt kê 14.3: (Được) Kích hoạt Sự đào tạo lại Quyết định: (Cái) quyết định kết hợp chất lượng (sự) mất (mát), đặc trưng sự trôi dạt, dự đoán sự dịch chuyển, và sự đào tạo lại
chi phí vì vậy (mang tính) tự động sự đào tạo lại kích hoạt (fires) chỉ khi (cái) (được) kỳ vọng lợi ích vượt quá (cái) (thuộc về) hoạt động rủi ro (Listing 14.3: Triggered Retraining Decision: The decision combines quality loss, feature drift, prediction shift, and retraining cost so automatic retraining fires only when the expected benefit exceeds the operational risk).
quality_loss = baseline_accuracy - current_accuracy
feature_drift = max(population_stability_index(features))
prediction_shift = distribution_distance(
baseline_predictions, live_predictions
)
benefit = estimate_value_recovered(
quality_loss=quality_loss,
feature_drift=feature_drift,
prediction_shift=prediction_shift,
)
risk = retraining_cost + validation_cost + rollout_risk
if benefit > risk and validation_data_is_fresh():
schedule_retraining_run()
(Mang tính) Định lượng sự đào tạo lại (các tính) kinh tế (Cái) quyết định để đào tạo lại một mô hình không phải là một vấn đề của trực giác mà
(là) một kỹ thuật sự tối ưu hóa (thứ) mà cân bằng (cái) chi phí của Hệ thống Entropy11 (độ chính xác sự suy tàn) so với (against) (cái)
chi phí của cơ sở hạ tầng (sự đào tạo lại (sự) chi tiêu) (Quantitative retraining economics The decision to retrain a model is not a matter of intuition but an engineering optimization that balances the cost of System Entropy11 (accuracy decay) against the cost of infrastructure (retraining expense)). Chúng ta có thể nghĩ về mô hình độ chính xác như (là) một (đang) suy tàn đại lượng (quantity),
tương tự với (có tính) phóng xạ sự suy tàn, với một (có thể) đo lường (được) tỷ lệ của sự suy giảm (decline) (We can think of model accuracy as a decaying quantity, analogous to radioactive decay, with a measurable rate of decline). Trong sản xuất, một mô hình cư xử
giống như một (có tính) phóng xạ đồng vị (isotope): nó có một (có thể) đo lường (được) Nửa-Đời12 sau (đó) của nó (thuộc về) dự đoán giá trị trở nên
độc hại (toxic) đối với (cái) (hoạt động) kinh doanh (In production, a model behaves like a radioactive isotope: it has a measurable Half-Life12 after which its predictive value becomes toxic to the business).
Một đơn giản nửa-đời sự tính toán biến sự đào tạo lại tần suất thành một (có thể) đo lường (được) khoảng (A simple half-life calculation turns retraining frequency into a measurable interval).
Khăn ăn Toán học 14.3: (Cái) nửa-đời của một mô hình
Bài toán: (Như thế nào) thường xuyên nên (cái) đội đào tạo lại (cái) mô hình để tối đa hóa lợi nhuận (như thế nào)?
Vật lý: Mô hình độ chính xác Độ chính xác(𝑡) suy tàn tại tỷ lệ 𝛾do dữ liệu sự trôi dạt.
• 𝑄: Hàng ngày Truy vấn Khối lượng (Lưu lượng truy cập).
• 𝑉: (Thuộc về) Tài chính giá trị mỗi truy vấn cho một đơn vị sự thay đổi trong độ chính xác phần (fraction). Với này quy ước,
𝑉= $0.50 có nghĩa (là) 1 phần trăm điểm của độ chính xác là (đáng) giá $0.005 mỗi truy vấn.
• 𝐶: (Được) Cố định chi phí của một sự đào tạo lại lần chạy, bao gồm (việc) tính toán và (thuộc về) hoạt động chi phí chung.
Công thức: (Cái) sự xấp xỉ trong phương trình 14.4 cho (cái) tối ưu sự đào tạo lại khoảng (𝑇∗) (thứ) mà
tối thiểu hóa (cái) tổng của (tính) cũ các sự mất (mát) và đào tạo các chi phí:
𝑇∗≈√
2⋅𝐶
𝑄⋅𝑉⋅Độ chính xác0 ⋅𝛾
(14.4)
Toán học: Xem xét một ngọn hải đăng gian lận mô hình (Độ chính xác0 = 0.95):
• Lưu lượng truy cập (𝑄): 1,000,000 (các) giao dịch/ngày.
• Tiện ích (𝑉): $0.50/truy vấn cho một đơn vị độ chính xác sự thay đổi.
• Sự đào tạo lại Chi phí (𝐶): $5,000.
• Sự trôi dạt Tỷ lệ (𝛾): 2 phần trăm mỗi ngày.
𝑇∗≈√
2×5,000
1,000,000×0.50×0.95×0.02 ≈1 Ngày
Các hệ thống sự thấu hiểu: Nếu lưu lượng truy cập là cao và độ chính xác là (có) giá trị, (cái) đội không thể đủ khả năng để chờ đợi. (Cái)
đường ống phải được tự động hóa. Nếu 𝑇∗là nhỏ hơn (cái) của đội thủ công sự triển khai thời gian, (cái) hệ thống
ở trong một trạng thái của (mang tính) vĩnh viễn (thuộc về) kỹ thuật nợ.
14. ML Các hoạt động
791
Kéo dài (Stretch) sự đào tạo lại quá xa và tính cũ
chi phí chạy (mất) đi.
(Cái) cùng sự dẫn xuất (derivation) có thể được chính thức hóa thành một bộ khung cho (việc) hiệu chuẩn việc giám sát các ngưỡng
(được) dựa trên (có thể) đo lường (được) (thuộc về) kinh doanh tác động (The same derivation can be formalized into a framework for calibrating monitoring thresholds based on measurable business impact). Này (mang tính) định lượng bộ khung biến đổi sự đào tạo lại từ một ad
hoc quyết định thành một kỹ thuật sự tối ưu hóa, (việc) triển khai nhận thức-chi phí sự tự động hóa (phần 14.2.1) (This quantitative framework transforms retraining from an ad hoc decision into an engineering optimization, implementing cost-aware automation (section 14.2.1)).
(Cái) (tính) cũ chi phí hàm Mô hình độ chính xác (một cách) điển hình xuống cấp qua thời gian do (sự) phân phối sự trôi dạt,
(việc) tạo ra một (tính) cũ chi phí (The staleness cost function Model accuracy typically degrades over time due to distribution drift, creating a staleness cost). Trong khi (cái) cơ chế của này sự xuống cấp là (cái) (thuộc về) sự phân phối sự phân kỳ
𝒟(𝑃𝑡‖𝑃0) (được) mô tả bởi phương trình 1.3, cho (thuộc về) kinh tế việc lập kế hoạch chúng ta có thể mô hình hóa (cái) (có thể) quan sát (được) tác động
qua thời gian như (là) một (có tính) mũ suy tàn quy trình (While the mechanism of this degradation is the distributional divergence 𝒟(𝑃𝑡‖𝑃0) described by equation 1.3, for economic planning we can model the observable impact over time as an exponential decay process). Trong (cái) (thuộc về) kinh điển (canonical) sự xuống cấp phương trình, 𝜆đại diện (cho)
độ nhạy với (thuộc về) sự phân phối sự phân kỳ; ở đây chúng ta sử dụng 𝛾như (là) một (thuộc về) thời gian suy tàn tỷ lệ, (đang) giả định (sự) trôi dạt
tích lũy (accumulates) (một cách) đều đặn (steadily) qua thời gian (In the canonical degradation equation, 𝜆represents sensitivity to distributional divergence; here we use 𝛾as a temporal decay rate, assuming drift accumulates steadily over time). (Cái) (có tính) mũ mô hình là một sự đơn giản hóa (thứ) mà kích hoạt dạng-đóng (closed-form)
(thuộc về) kinh tế sự phân tích (The exponential model is a simplification that enables closed-form economic analysis). Cho (phép) Độ chính xác(𝑡) đại diện (cho) độ chính xác tại thời gian 𝑡kể từ (lần) cuối sự đào tạo, và Độ chính xác0
đại diện (cho) ban đầu độ chính xác (Let Accuracy(𝑡) represent accuracy at time 𝑡since last training, and Accuracy0 represent initial accuracy). Phương trình 14.5 nắm bắt này sự xuống cấp, nơi (cái) tỷ lệ 𝛾phụ thuộc vào
miền tính dễ bay hơi (volatility):
Độ chính xác(𝑡) = Độ chính xác0 ⋅𝑒−𝛾𝑡
(14.5)
(Cái) chi phí của (tính) cũ tích lũy (được) dựa trên truy vấn khối lượng 𝑄mỗi thời gian khoảng (period) và (cái) giá trị tác động
𝑉của một đơn vị sự thay đổi trong độ chính xác phần (The cost of staleness accumulates based on query volume 𝑄per time period and the value impact 𝑉of a unit change in accuracy fraction). (Việc) Tích phân (Integrating) (cái) (mang tính) tức thời (instantaneous) độ chính xác (sự) mất (mát) (Độ chính xác0 −
Độ chính xác(𝑡)) qua (cái) sự đào tạo lại khoảng 𝑇mang lại (yields) phương trình 14.6:
(Tính) Cũ Chi phí(𝑇) = ∫
𝑇
0
𝑄⋅𝑉⋅(Độ chính xác0 −Độ chính xác(𝑡))𝑑𝑡=
𝑄⋅𝑉⋅Độ chính xác0 ⋅(𝑇−1−𝑒−𝛾𝑇
𝛾
)
(14.6)
(Cái) tích phân tích lũy chi phí qua thời gian 𝑡từ 0 đến 𝑇, và (cái) dạng-đóng tuân theo (follows) từ (việc) thay thế (substituting)
phương trình 14.5 cho Độ chính xác(𝑡) (The integral accumulates cost over time 𝑡from 0 to 𝑇, and the closed form follows from substituting equation 14.5 for Accuracy(𝑡)).
(Cái) sự đào tạo lại chi phí hàm Mỗi (sự) đào tạo lại gánh chịu (incurs) (được) cố định các chi phí bao gồm (việc) tính toán, sự xác thực, và
sự triển khai chi phí chung (The retraining cost function Each retraining incurs fixed costs including compute, validation, and deployment overhead). Phương trình 14.7 phân rã (decomposes) những (cái này):
Sự đào tạo lại Chi phí = 𝐶tính toán +𝐶xác thực +𝐶triển khai +𝐶rủi ro
(14.7)
nơi 𝐶tính toán là (cái) chi phí của (cái) đào tạo lần chạy chính nó, 𝐶xác thực là (cái) chi phí của (việc) đánh giá (cái) mới mô hình
trước khi (sự) phát hành, 𝐶triển khai là (cái) chi phí của (việc) cuộn (rolling) nó vào sản xuất, và 𝐶rủi ro là (cái) (được) kỳ vọng chi phí của
(mang tính) tiềm năng sự hồi quy từ (cái) mới mô hình (where 𝐶compute is the cost of the training run itself, 𝐶validation is the cost of evaluating the new model before release, 𝐶deployment is the cost of rolling it into production, and 𝐶risk is the expected cost of potential regression from the new model).
Tối ưu sự đào tạo lại khoảng (Cái) tối ưu sự đào tạo lại khoảng 𝑇∗tối thiểu hóa tổng chi phí mỗi đơn vị thời gian, như
phương trình 14.8 cho thấy (Optimal retraining interval The optimal retraining interval 𝑇∗minimizes total cost per unit time, as equation 14.8 shows):
𝑇∗= argmin𝑇
(Tính) Cũ Chi phí(𝑇)+Sự đào tạo lại Chi phí
𝑇
(14.8)
Cho (có tính) mũ sự suy tàn, điều này mang lại (cái) căn-bậc hai định luật (được) sử dụng trong (của) chúng ta (trước) đó khăn ăn toán học sự tính toán (For exponential decay, this yields the square-root law used in our earlier napkin math calculation).
Trong gian lận sự phát hiện, những các công thức này chuyển đổi (một cách) trực tiếp thành một sự đào tạo lại lịch trình: với các tham số
trong bảng 14.9, hàng ngày sự đào tạo lại là (về mặt) kinh tế (có tính) tối ưu bởi vì (tính) cũ chi phí tích lũy nhanh hơn
sự đào tạo lại chi phí (In fraud detection, these formulas translate directly into a retraining schedule: with the parameters in table 14.9, daily retraining is economically optimal because staleness cost accumulates faster than retraining cost).
Bảng 14.9: Sự đào tạo lại Quyết định Các tham số: Ví dụ các giá trị cho một gian lận sự phát hiện hệ thống (đang) xử lý 1,000,000 các giao dịch
hàng ngày (Table 14.9: Retraining Decision Parameters: Example values for a fraud detection system processing 1,000,000 transactions daily).
Tham số
Giá trị
Sự mô tả
𝑄
1,000,000
Các giao dịch mỗi ngày
𝑉
$0.50/truy vấn
Giá trị mỗi truy vấn cho một đơn vị độ chính xác sự thay đổi
Độ chính xác0
0.95
Ban đầu độ chính xác
𝛾
0.02
Hàng ngày suy tàn tỷ lệ (2% mỗi ngày)
Sự đào tạo lại Chi phí
$5,000
Tổng sự đào tạo lại (sự) chi tiêu
Độ nhạy sự phân tích Bởi vì 𝑇∗mở rộng quy mô với (cái) căn bậc hai của những các tham số này, lớn đầu vào các sự dao động (swings)
sản xuất chỉ khiêm tốn (modest) khoảng các sự thay đổi (Sensitivity analysis Because 𝑇∗scales with the square root of these parameters, large input swings produce only modest interval changes). Bảng 14.10 làm (cho) (cái) sự giảm xóc (damping) (trở nên) cụ thể: một gấp bốn (fourfold) sự thay đổi
trong sự đào tạo lại chi phí, truy vấn khối lượng, hay suy tàn tỷ lệ di chuyển (cái) tối ưu khoảng chỉ gấp đôi (twofold), vì vậy sự đào tạo lại
nhịp độ duy trì (sự) mạnh mẽ đối với (có tính) vừa phải (moderate) sự không chắc chắn (uncertainty) trong bất kỳ đơn tham số (nào) (Table 14.10 makes the damping concrete: a fourfold change in retraining cost, query volume, or decay rate moves the optimal interval only twofold, so retraining cadence stays robust to moderate uncertainty in any single parameter).

792
14.4 Sự phát triển Cơ sở hạ tầng
Mô hình các hạn chế (limitations) Này bộ khung cung cấp một bậc-một (first-order) sự xấp xỉ (thứ) mà kích hoạt có nguyên tắc (principled)
việc ra quyết định (decision-making), nhưng những người thực hành (practitioners) nên được nhận thức của (những) của nó các giả định:
• (Có thể) Dự đoán (được) sự trôi dạt: (Cái) có tính mũ suy tàn mô hình giả định sự trôi dạt xảy ra (một cách) dần dần tại một (đã) biết tỷ lệ.
Đột ngột (sự) phân phối các sự dịch chuyển (khái niệm sự trôi dạt) yêu cầu khác biệt sự phát hiện và phản hồi các cơ chế.
• (Đã) Biết giá trị hàm: (Cái) mô hình giả định mỗi độ chính xác điểm có một (có thể) định lượng (được) (thuộc về) kinh doanh
giá trị. Trong thực tế, này giá trị có thể là phi tuyến tính hay phụ thuộc-bối cảnh.
• Độc lập sự đào tạo lại các chu kỳ: (Cái) mô hình đối xử (với) mỗi sự đào tạo lại quyết định (một cách) độc lập,
(việc) phớt lờ (ignoring) (mang tính) tiềm năng các lợi ích từ liên tục học tập hay sự chuyển giao (xuyên) qua sự đào tạo lại các chu kỳ.
• Tuyến tính chi phí việc mở rộng quy mô: Sự đào tạo lại các chi phí được giả định (là) (được) cố định. Trong thực tế, cơ sở hạ tầng các chi phí có thể
khác nhau với tính toán tính có sẵn và việc định giá (các) động lực (dynamics).
Bảng 14.10: Sự đào tạo lại Khoảng Sự nhạy cảm: (Như thế nào) tham số các sự thay đổi ảnh hưởng (đến) tối ưu sự đào tạo lại tần suất (như thế nào). (Việc) Tăng gấp bốn lần (Quadrupling) truy vấn
khối lượng giảm đi một nửa (halves) (cái) tối ưu khoảng bởi vì sự xuống cấp các chi phí mở rộng quy mô (một cách) tuyến tính với lưu lượng truy cập. (Việc) Giảm xuống còn một phần tư (Quartering) sự đào tạo lại chi phí (một cách) tương tự
giảm đi một nửa (cái) khoảng, trong khi thấp hơn suy tàn các tỷ lệ kéo dài nó. Các hệ thống với cao lưu lượng truy cập và cao mỗi-truy vấn giá trị hưởng lợi (nhiều) nhất từ
thường xuyên sự đào tạo lại sự tự động hóa.
Sự thay đổi
Tác động lên 𝑇∗
4× sự đào tạo lại chi phí
2× dài hơn khoảng
4× truy vấn khối lượng
2× ngắn hơn khoảng
4× suy tàn tỷ lệ
2× ngắn hơn khoảng
Mặc dù những các hạn chế này, (cái) bộ khung cung cấp một có nguyên tắc bắt đầu điểm cho sự đào tạo lại các quyết-
định (deci-sions). Các tham số cải thiện với sự hiệu chuẩn so với (thuộc về) lịch sử dữ liệu và sự tinh chỉnh (refinement) như (khi) (thuộc về) hoạt động
kinh nghiệm tích lũy. Bằng (cách) (việc) làm (cho) chi phí-lợi ích các sự đánh đổi (trở nên) rõ ràng và (có thể) định lượng (được), này bộ khung
triển khai nhận thức-chi phí sự tự động hóa (phần 14.2.1), (việc) kích hoạt (được) biện minh (justified) cơ sở hạ tầng các sự đầu tư
và việc giám sát các ngưỡng (được) dựa (grounded) trên (có thể) đo lường (được) (thuộc về) kinh doanh tác động.
14.4.2.3 Mô hình sự xác thực
Đào tạo các đường ống sản xuất mô hình các ứng cử viên; mô hình sự xác thực quyết định (cái) nào (các) ứng cử viên xứng đáng (merit)
sản xuất sự triển khai. Không giống như (thuộc về) nghiên cứu sự đánh giá, nơi một mô hình (thứ) mà đánh bại (beats) một điểm chuẩn (benchmark) trên
một tĩnh kiểm thử tập được xem xét (là) thành công, sản xuất sự xác thực phải xác minh (verify) (thuộc về) hoạt động tính sẵn sàng (readiness):
liệu (cái) mô hình (có) biểu diễn (một cách) (đáng) tin cậy dưới (mang tính) động thực-thế giới các điều kiện (hay không) và tiếp tục để làm (như) vậy
khi (as) dữ liệu các sự phân phối dịch chuyển.
(Cái) sự đánh giá quy trình bắt đầu với hiệu suất việc kiểm thử so với một (được) giữ lại (holdout) kiểm thử tập (được) lấy mẫu từ
(cái) cùng sự phân phối như (là) sản xuất dữ liệu. Cốt lõi (Core) các số liệu (chẳng) hạn như độ chính xác, diện tích dưới (cái) đường cong (AUC),
độ chụm (precision), (độ) thu hồi (recall), và F1 điểm (Rainio và cộng sự. 2024) được tính toán và (được) theo dõi (một cách) dọc (longitudinally) để phát hiện
sự xuống cấp từ dữ liệu sự trôi dạt (IBM 2024). Ba (được) căn chỉnh các bảng (panels) trong hình 14.7 cho thấy này sự xuống cấp
mẫu (một cách) cụ thể (concretely). (Cái) trên cùng bảng trình bày (đang) đến (incoming) dữ liệu các mẫu qua thời gian, (được) mã hóa-màu (color-coded) theo loại.
(Cái) (ở) giữa bảng tiết lộ (cái) (đang) làm nền tảng nguyên nhân: một đặc trưng sự phân phối (sales_channel (bán hàng_kênh)) (một cách) dần dần
(đang) dịch chuyển từ chủ yếu (predominantly) trực tuyến sang chủ yếu ngoại tuyến các giao dịch. (Cái) dưới cùng bảng cho thấy
(cái) hệ quả (consequence): mô hình độ chính xác (đang) suy giảm (declining) (theo) từng bước đồng bộ (in lockstep) với (cái) sự phân phối sự dịch chuyển. Này sự trực quan hóa
nắm bắt (cái) cốt lõi thử thách của mô hình sự xác thực: (cái) nhu cầu để giám sát các đầu vào cùng với các đầu ra để
hiểu tại sao hiệu suất thay đổi.
Vượt ra ngoài tĩnh sự đánh giá, MLOps khuyến khích (encourages) (được) kiểm soát sự triển khai các chiến lược (thứ) mà mô phỏng (simulate)
sản xuất các điều kiện trong khi (đang) giảm thiểu rủi ro. Một (một cách) rộng rãi (được) áp dụng phương pháp là chim yến việc kiểm thử (Fowler
2014), trong đó một mới mô hình được triển khai (tới) một nhỏ phần của người dùng hay các truy vấn. Trong suốt này (được) giới hạn
sự cuộn ra (rollout), trực tiếp hiệu suất các số liệu được giám sát để đánh giá (assess) hệ thống độ ổn định và người dùng tác động. Cho
ví dụ (instance), một thương mại điện tử nền tảng triển khai một mới sự gợi ý mô hình (tới) 5 phần trăm của web lưu lượng truy cập
và quan sát các số liệu (chẳng) hạn như nhấp chuột-xuyên qua (click-through) tỷ lệ, độ trễ, và dự đoán độ chính xác. Chỉ sau (khi) (cái)
mô hình chứng minh (một cách) nhất quán và (đáng) tin cậy hiệu suất (thì) (is) nó (được) thăng cấp (lên) đầy (đủ) sản xuất.
(Việc) Đánh giá các ứng cử viên dưới (những) giống hệt nhau các điều kiện là (cái) điều kiện tiên quyết (prerequisite) cho một vững chắc (sound) sự thăng cấp
quyết định, bởi vì một ứng cử viên (thứ) mà chiến thắng chỉ bởi vì nó đã được đo lường so với khác lưu lượng truy cập, các đặc trưng,
hay thời gian các cửa sổ không nói (với) (cái) đội (điều) gì (cả). Đám mây ML các nền tảng hỗ trợ điều này thông qua sự thử nghiệm
việc ghi nhật ký, yêu cầu sự phát lại (replay), và (mang tính) tổng hợp kiểm thử-trường hợp (test-case) sự tạo (ra), và công cụ (chẳng) hạn như Trọng số & Các độ lệch (Biases)

793
(Đang) Đến dữ liệu
Thời gian
Đặc trưng sự phân phối: bán hàng_kênh
Trực tuyến cửa hàng
Ngoại tuyến cửa hàng
Mô hình chất lượng: độ chính xác qua thời gian
Hình 14.7: Dữ liệu Sự trôi dạt Tác động: (Đang) Suy giảm (Declining) mô hình hiệu suất qua thời gian (là) kết quả (results) từ dữ liệu sự trôi dạt, nơi các đặc điểm (characteristics) của
sản xuất dữ liệu phân kỳ từ (cái) đào tạo tập dữ liệu (Figure 14.7: Data Drift Impact: Declining model performance over time results from data drift, where the characteristics of production data diverge from the training dataset). (Việc) Giám sát chính các số liệu (một cách) dọc (longitudinally) cho phép MLOps các kỹ sư để phát hiện này
sự trôi dạt và kích hoạt mô hình sự đào tạo lại hay dữ liệu đường ống các sự điều chỉnh (adjustments) để duy trì độ chính xác (Monitoring key metrics longitudinally allows MLOps engineers to detect this drift and trigger model retraining or data pipeline adjustments to maintain accuracy).
(Weights & Biases, Inc. 2024) nắm bắt (cái) đào tạo các đồ tạo tác, siêu tham số các cấu hình, và
các số liệu (thứ) mà làm (cho) những các sự so sánh đó (có thể) tái tạo (được) và (có thể) theo dõi (được) (xuyên) qua (cái) đào tạo và sự triển khai
đường ống (Weights & Biases, Inc. 2024) captures the training artifacts, hyperparameter configurations, and metrics that make those comparisons reproducible and traceable across the training and deployment pipeline).
Trong khi sự tự động hóa là (trung) tâm đối với MLOps sự đánh giá, (con) người sự giám sát (oversight) duy trì (tính) thiết yếu (While automation is central to MLOps evaluation, human oversight remains essential). (Được) Tự-
động hóa (Auto-mated) các bài kiểm tra có thể thất bại (trong việc) nắm bắt (mang tính) nhiều sắc thái (nuanced) hiệu suất các vấn đề (chẳng) hạn như kém tính tổng quát hóa trên hiếm
(các) quần thể phụ (subpopulations) hay các sự dịch chuyển trong người dùng hành vi ((Được) Tự-động hóa (Auto-mated) các bài kiểm tra có thể thất bại (trong việc) nắm bắt (mang tính) nhiều sắc thái (nuanced) hiệu suất các vấn đề (chẳng) hạn như kém tính tổng quát hóa trên hiếm (các) quần thể phụ (subpopulations) hay các sự dịch chuyển trong người dùng hành vi). Các đội kết hợp (mang tính) định lượng sự đánh giá với (mang tính) định tính
sự đánh giá, (một cách) đặc biệt cho các mô hình (được) triển khai trong rủi ro-cao (high-stakes) hay (được) quản lý (regulated) các môi trường (Teams combine quantitative evaluation with qualitative review, particularly for models deployed in high-stakes or regulated environments). Này đa-giai đoạn
sự đánh giá quy trình kết nối (bridges) ngoại tuyến việc kiểm thử và trực tiếp hệ thống việc giám sát, (việc) đảm bảo các mô hình cư xử
(một cách) (có thể) dự đoán (được) dưới thực-thế giới các điều kiện và (việc) hoàn tất (cái) sự phát triển cơ sở hạ tầng nền tảng
(được) cần thiết cho sản xuất sự triển khai (This multi-stage evaluation process bridges offline testing and live system monitoring, ensuring models behave predictably under real-world conditions and completing the development infrastructure foundation necessary for production deployment).
14.4.3 Cơ sở hạ tầng sự tích hợp
(Cái) sự phát triển cơ sở hạ tầng (được) kiểm tra sớm hơn giải quyết hai của (cái) ba tới hạn các giao diện
(được) giới thiệu tại (cái) chương (sự) mở (đầu) (The development infrastructure examined earlier addresses two of the three critical interfaces introduced at the chapter’s opening). Đặc trưng các cửa hàng và dữ liệu việc lập phiên bản giải quyết (cái) Dữ liệu-Mô hình
Giao diện bằng (cách) (việc) đảm bảo (có tính) nhất quán, (được) theo dõi đặc trưng quyền truy cập (xuyên) qua đào tạo và phục vụ (Feature stores and data versioning solve the Data-Model Interface by ensuring consistent, tracked feature access across training and serving). CI/CD các đường ống,
mô hình các cơ quan đăng ký, và sự xác thực các cổng (gates) giải quyết (cái) Mô hình-Cơ sở hạ tầng Giao diện bằng (cách) (việc) tự động hóa (cái)
sự chuyển tiếp từ (được) đào tạo các trọng số sang (được) đóng gói (thành container) các dịch vụ với sự quay lui khả năng (CI/CD pipelines, model registries, and validation gates address the Model-Infrastructure Interface by automating the transition from trained weights to containerized services with rollback capability).
Những (cái này) đại diện (cho) chỉ hai-phần ba của (cái) (thuộc về) hoạt động thử thách, tuy nhiên (These represent only two-thirds of the operational challenge, however). Một mô hình (thứ) mà vượt qua tất cả
sự xác thực các cổng và triển khai (một cách) thành công có thể vẫn thất bại (một cách) im lặng trong sản xuất khi (as) (cái) thế giới thay đổi
xung quanh nó (A model that passes all validation gates and deploys successfully can still fail silently in production as the world changes around it). (Cái) thứ ba tới hạn giao diện, Sản xuất-Việc giám sát, yêu cầu một khác tập của các thực hành
(được) tập trung không (phải) vào (việc) xây dựng các mô hình mà (là) vào (việc) giữ chúng khỏe mạnh qua thời gian (The third critical interface, Production-Monitoring, requires a different set of practices focused not on building models but on keeping them healthy over time).
14.5 Sản xuất Các hoạt động
Một mô hình (thứ) mà vượt qua mọi sự xác thực cổng vẫn có một nửa-đời (A model that passes every validation gate still has a half-life). Từ (cái) khoảnh khắc của sự triển khai, (cái)
thế giới bắt đầu (để) phân kỳ từ (cái) đào tạo sự phân phối: các khách hàng thay đổi hành vi, các đối thủ cạnh tranh
ra mắt (launch) các sản phẩm, (các) mùa thay đổi (shift), và mới biên các trường hợp xuất hiện (thứ) mà không kiểm thử tập (nào) (đã) lường trước (anticipated) (From the moment of deployment, the world begins to diverge from the training distribution: customers change behavior, competitors launch products, seasons shift, and new edge cases emerge that no test set anticipated). Sản xuất
các hoạt động tồn tại để làm (cho) này (không thể) tránh khỏi sự suy tàn (trở nên) (có thể) nhìn thấy (được) và (có thể) quản lý (được), (việc) triển khai (cái) Sản xuất-
Việc giám sát Giao diện thông qua sự triển khai các chiến lược, việc giám sát, sự cố (incident) sự phản hồi, và quản trị (Production operations exist to make this inevitable decay visible and manageable, implementing the Production-Monitoring Interface through deployment strategies, monitoring, incident response, and governance).
Các yêu cầu là khắt khe (demanding): xử lý (có thể) biến đổi các tải, duy trì (có tính) nhất quán độ trễ, phục hồi
(một cách) êm ái (gracefully) từ các sự thất bại, và thích ứng với (đang) tiến hóa dữ liệu các sự phân phối, tất cả (mà) không làm gián đoạn (disrupting) dịch vụ (The requirements are demanding: handle variable loads, maintain consistent latency, recover gracefully from failures, and adapt to evolving data distributions, all without disrupting service).
Những các thực hành này triển khai (có thể) quan sát (được) sự xuống cấp tại thời gian chạy (runtime), (việc) biến đổi im lặng mô hình sự trôi dạt thành
(có thể) hành động (được) các cảnh báo trước khi (các) người dùng trải nghiệm sự xuống cấp (These practices implement observable degradation at runtime, transforming silent model drift into actionable alerts before users experience degradation).
14.5.1 Mô hình sự triển khai và (việc) phục vụ
Một khi (được) đào tạo và (được) xác thực, một mô hình phải được tích hợp vào một sản xuất môi trường (thứ) mà phân phối
các dự đoán tại quy mô (Once trained and validated, a model must be integrated into a production environment that delivers predictions at scale). Sự triển khai biến đổi một tĩnh đồ tạo tác thành một trực tiếp hệ thống thành phần, và

794
14.5 Sản xuất Các hoạt động
13
Việc đóng gói (thành container) cho ML
Sự triển khai: Docker (Merkel
2014) đóng gói mã với
các sự phụ thuộc vào (có thể) mang theo (được) (portable)
các đơn vị; Kubernetes (Burns và cộng sự.
2016) điều phối những các đơn vị đó
(xuyên) qua các cụm. Cho ML các hệ-
thống (sys-tems), việc đóng gói (thành container) giải quyết
(cái) Môi trường𝑣thuật ngữ (term) trong
phương trình 14.1: một mô hình (thứ) mà
hoạt động trong sự phát triển nhưng
thất bại trong sản xuất do một thư-
viện phiên bản sự không khớp (mismatch) không phải (là)
một mã lỗi (bug) mà (là) một môi-
trường (tính) chẵn lẻ (parity) sự thất bại. (Các) Container
làm (cho) (cái) môi trường (thành) một
(được) lập phiên bản, (có thể) triển khai (được) đồ tạo tác.
14
Chạy thử (Staging) Sự xác thực: (Cái)
chính sự khác biệt từ (mang tính) thông-
thường (conven-tional) phần mềm chạy thử: (mang tính) thông-
thường chạy thử xác thực (mang tính) tất-
định (de-terministic) tính đúng đắn (làm
(cái) mã sản xuất (cái) đúng
đầu ra (không)?), trong khi ML chạy thử
xác thực (mang tính) xác suất sự đầy-
đủ (ade-quacy) (có phải (cái) của mô hình (độ) chính-
xác (accu-racy) sự phân phối (là) (có thể) chấp nhận (được)
(được) cho hiện tại dữ liệu (không)?).
Điều này
làm (cho) ML chạy thử (về mặt) cơ-
bản (fundamen-tally) khó hơn: một mô hình có thể vượt qua
tất cả đơn vị các bài kiểm tra và vẫn thất bại trong
sản xuất bởi vì (cái) kiểm thử
dữ liệu không phản ánh (reflect) (cái) sự triển-
khai (de-ployment) sự phân phối, vì vậy (sự) cuộn-
ra các cổng phải so sánh dự-
đoán các số liệu thống kê, sự đánh giá
các lát (cắt) (slices), và (thuộc về) kinh doanh các lan can (guardrails)
so với (against) (được) hiệu chuẩn các ngưỡng
thay vì dựa vào đơn vị các bài kiểm tra
đơn độc (alone).
15
Bóng (Shadow) Sự triển khai:
(Về mặt) Kinh tế (được) biện minh (justified) khi
(cái) chi phí của một tồi (bad) sự cuộn ra (đối mặt-người dùng
các lỗi × người dùng số đếm (count)
× (thuộc về) kinh doanh tác động mỗi lỗi) vượt quá (cái) chi phí của (việc) chạy
bóng cơ sở hạ tầng
cho (bị) trùng lặp sự suy luận (mà) không-
phục vụ các kết quả. (Cái) chính
sự thấu hiểu là (rằng) bóng sự triển-
khai’s giá trị là bất đối xứng (asymmetric): nó
giảm thiểu (có tính) thảm họa (catastrophic) đuôi rủi ro,
không phải (là) trung bình-trường hợp lỗi, (việc) làm
nó hữu ích cho rủi ro-cao (high-stakes)
các mô hình nơi một đơn tồi
sự cuộn ra có thể gây ra (không thể) đảo ngược (irreversible)
sự thiệt hại (damage).
16
Chim yến (Canary) Sự triển khai:
Định tuyến (Routes) một nhỏ phần của trực tiếp
lưu lượng truy cập (tới) một ứng cử viên mô hình,
(đang) sử dụng nó như (là) một người lính gác (sentinel) cho sản-
xuất sức khỏe.
(Cái) ML-
đặc thù thử thách là (rằng) một
“sự thất bại” là (thuộc về) thống kê sự xuống-
cấp (degrada-tion), không phải (là) một (mang tính) tất định sự cố (crash):
(việc) phát hiện một nhỏ độ chính xác (sự) khác-
biệt (dif-ference) với cao sự tự tin
có thể yêu cầu (hàng) ngàn của các (sự) suy-
luận (in-ferences), (việc) tạo ra một sự căng thẳng (tension) giữa-
quyết định tốc độ và (thuộc về) thống-
kê (sta-tistical) sức mạnh (power) (thứ) mà quyết định
tối thiểu chim yến khoảng thời gian (duration).
(việc) phục vụ đảm bảo tính có khả năng truy cập (accessibility), độ tin cậy, và tính hiệu quả trong (việc) phản hồi (tới) sự suy luận các yêu cầu (serving ensures accessibility, reliability, and efficiency in responding to inference requests). Cùng nhau,
những các thành phần này kết nối (bridge) mô hình sự phát triển và thực-thế giới tác động (Together, these components bridge model development and real-world impact).
14.5.1.1 Mô hình sự triển khai
Xem xét một gian lận sự phát hiện mô hình (thứ) mà đạt được 99.2 phần trăm độ chụm trong (cái) sự phát triển môi-
trường (environ-ment) (Consider a fraud detection model that achieves 99.2 percent precision in the development environ-ment). Một kỹ sư xuất khẩu (exports) các trọng số, sao chép chúng sang một sản xuất máy chủ, và khám phá (rằng) (cái) mô hình
d dự đoán mọi giao dịch như (là) hợp pháp (legitimate)—(cái) sản xuất máy chủ chạy một khác phiên bản của (cái) đặc trưng
sự trích xuất (extraction) thư viện, (việc) sản xuất các đầu vào (mà) (cái) mô hình (đã) không bao giờ thấy (An engineer exports the weights, copies them to a production server, and discovers the model predicts every transaction as legitimate—the production server runs a different version of the feature extraction library, producing inputs the model has never seen). Này tình huống, (một cách) gây thất vọng (frustratingly) (là) phổ biến,
minh họa tại sao sự triển khai không phải (là) một tệp (sự) chuyển giao (transfer) mà (là) một (thuộc về) các hệ thống (thuộc về) kỹ thuật bài toán (This scenario, frustratingly common, illustrates why deployment is not a file transfer but a systems engineering problem). (Việc) Đóng gói (Packaging),
(việc) kiểm thử, và (việc) theo dõi ML các mô hình cho (đáng) tin cậy sản xuất sự triển khai yêu cầu (việc) đối xử (với) (cái) mô hình, của nó
các sự phụ thuộc, và của nó cấu hình như (là) một đơn (có thể) triển khai (được) đơn vị (Packaging, testing, and tracking ML models for reliable production deployment requires treating the model, its dependencies, and its configuration as a single deployable unit). Một phổ biến cách tiếp cận bao gồm
(việc) đóng gói (thành container) các mô hình (đang) sử dụng container các công nghệ13, (việc) đảm bảo tính có thể mang theo (được) (xuyên) qua các môi trường (One common approach involves containerizing models using container technologies13, ensuring portability across environments).
Sản xuất sự triển khai yêu cầu các khuôn khổ (thứ) mà xử lý mô hình việc đóng gói, việc lập phiên bản, và
sự tích hợp với (đang) phục vụ cơ sở hạ tầng (Production deployment requires frameworks that handle model packaging, versioning, and integration with serving infrastructure). Các công cụ giống như MLflow và mô hình các cơ quan đăng ký quản lý những
sự triển khai các đồ tạo tác này (A. Chen và cộng sự. 2020), trong khi phục vụ-đặc thù các khuôn khổ ((được) chi tiết trong Chương 13)
xử lý (cái) thời gian chạy sự tối ưu hóa và (việc) mở rộng quy mô các yêu cầu (Tools like MLflow and model registries manage these deployment artifacts (A. Chen et al. 2020), while serving-specific frameworks (detailed in Chapter 13) handle the runtime optimization and scaling requirements). Trước (khi) đầy-quy mô (full-scale) sự cuộn ra (rollout), các đội triển khai
(được) cập nhật các mô hình (tới) chạy thử (staging) hay QA các môi trường14 để (một cách) nghiêm ngặt (rigorously) kiểm thử hiệu suất (Before full-scale rollout, teams deploy updated models to staging or QA environments14 to rigorously test performance).
Các kỹ thuật (chẳng) hạn như bóng (shadow) các sự triển khai15, chim yến (canary) việc kiểm thử16, và xanh dương-xanh lá cây (blue-green) sự triển khai17 xác thực
mới các mô hình (một cách) tăng dần (incrementally) (Techniques such as shadow deployments15, canary testing16, and blue-green deployment17 validate new models incrementally). Những (được) kiểm soát sự triển khai các chiến lược này kích hoạt an toàn mô hình sự xác thực trong
sản xuất (These controlled deployment strategies enable safe model validation in production). Mạnh mẽ sự quay lui các quy trình là thiết yếu để xử lý (không được) mong đợi các vấn đề, (việc) khôi phục (reverting) các hệ thống
về (cái) (trước) đó ổn định mô hình phiên bản để đảm bảo tối thiểu sự gián đoạn (Robust rollback procedures are essential to handle unexpected issues, reverting systems to the previous stable model version to ensure minimal disruption).
Chiến tranh Câu chuyện 14.1: (Cái) Knight Capital lỗi (2012)
Bối cảnh: Knight Capital Tập đoàn (Group) (đã) là một lớn thị trường (nhà) tạo lập (maker) trong Mỹ (US) các cổ phiếu (equities). Vào (năm) 2012, họ
(đã) triển khai mới phần mềm (tới) bảy trong tám các máy chủ nhưng (đã) bỏ lỡ (cái) thứ 8 (U.S. Chứng khoán và (Sự) Trao đổi
Ủy ban 2013).
Sự thất bại chế độ: (Cái) mới mã (đã) tái sử dụng mục đích (repurposed) một cũ cờ (flag) (SMARS). Trên (cái) bảy (được) cập nhật các máy chủ,
điều này (đã) hoạt động (một cách) chính xác. Trên (cái) thứ 8 máy chủ (đang) chạy cũ mã, (việc) kích hoạt SMARS (đã) kích hoạt (triggered) một (đang) ngủ đông (dormant)
kiểm thử hàm (được) gọi (là) “Power Peg” (được) thiết kế (nhiều) năm sớm hơn để mua cổ phiếu (một cách) quyết liệt cho việc kiểm thử. Trong
bốn mươi lăm phút, (cái) (bị) khiếm khuyết (defective) bộ định tuyến (router) (đã) tạo ra (hàng) triệu của (mang tính) sai sót (erroneous) các đơn hàng (orders), (đã) tích lũy một
không lường trước (unintended) nhiều-tỷ-đô la danh mục (đầu tư), và cuối cùng làm tốn (cost) Knight nhiều hơn $460 triệu.
(Cái) công ty (đã) cần (mang tính) khẩn cấp sự tài trợ (financing) trong (vòng) (các) ngày.
Các hệ thống bài học: Sự triển khai là một (các) hệ thống bài toán (thứ) mà mở rộng (extends) tốt (nhiều) vượt ra ngoài mã. (Việc) Cấu-
hình (Config-uration) sự trôi dạt và một phần các sự cuộn ra là (có tính) thảm họa (catastrophic) sự thất bại các chế độ trong (được) tự động hóa các hệ thống. ML
các sự triển khai kế thừa (inherit) (cái) cùng rủi ro bề mặt (surface): một mô hình cơ quan đăng ký (đang) trỏ (pointing) vào (cái) sai phiên bản, một
đặc trưng lược đồ (đang) trôi dạt giữa đào tạo và phục vụ, hay một một phần chim yến (canary) (thứ) mà chèn ép (wedges) một nửa
(cái) hạm đội (fleet) trên một cũ định tuyến quy tắc (tất cả) đều tái tạo (reproduce) (cái) Knight Capital hình dạng với (cái) mô hình (nằm) ở vị trí
của (cái) (đang) giao dịch công cụ (engine).
(Việc) Tránh (cái) Knight Capital sự thất bại chế độ (chính) xác là tại sao ML các sự triển khai chạy thử (stage) (sự) cuộn ra thay
vì lật (flip) một (công) tắc, nhưng (được) chạy thử (sự) cuộn ra tạo ra của riêng nó bài toán (Avoiding the Knight Capital failure mode is exactly why ML deployments stage rollout rather than flip a switch, but staged rollout creates its own problem). Khi chim yến các sự triển khai tiết lộ
các bài toán tại một phần lưu lượng truy cập các cấp độ (các vấn đề (đang) xuất hiện tại 30 phần trăm lưu lượng truy cập nhưng không (phải) tại 5 phần trăm), các đội
cần (có tính) hệ thống việc gỡ lỗi các chiến lược (When canary deployments reveal problems at partial traffic levels (issues appearing at 30 percent traffic but not at 5 percent), teams need systematic debugging strategies). (Có tính) Hiệu quả sự chẩn đoán yêu cầu (việc) tương quan hóa (correlating) nhiều (các) tín hiệu: hiệu-
suất (per-formance) các số liệu từ Chương 12, dữ liệu sự phân phối sự phân tích để phát hiện sự trôi dạt, và đặc trưng (sự) quan trọng
các sự dịch chuyển (thứ) mà có thể giải thích sự xuống cấp (Effective diagnosis requires correlating multiple signals: performance metrics from Chapter 12, data distribution analysis to detect drift, and feature importance shifts that might explain degradation). Các đội duy trì (việc) gỡ lỗi các bộ công cụ (toolkits) bao gồm A/B kiểm thử sự phân tích
các khuôn khổ, đặc trưng (sự) quy kết (attribution) các công cụ, và dữ liệu lát (cắt) (các) bộ phân tích (thứ) mà nhận diện cái nào (các) quần thể phụ
đang trải qua (đang bị) xuống cấp hiệu suất (Teams maintain debug toolkits including A/B test analysis frameworks, feature attribution tools, and data slice analyzers that identify which subpopulations are experiencing degraded performance).
Đó sự chẩn đoán vòng lặp phải kết nối (một cách) trực tiếp (tới) (cái) (sự) phát hành đường ống (That diagnosis loop must connect directly to the release pipeline). CI/CD sự tích hợp tự động hóa
sự triển khai và sự quay lui, nhưng chỉ khi sự quay lui được thiết kế như (là) phần của (cái) sự cuộn ra cơ chế
thay vì (được) đối xử như (là) một (mang tính) khẩn cấp kịch bản (CI/CD integration automates deployment and rollback, but only when rollback is designed as part of the rollout mechanism rather than treated as an emergency script).
Sự quay lui các chiến lược và an toàn các cơ chế Sự quay lui18 khả năng là (cái) an toàn lưới (thứ) mà kích hoạt
(sự) tự tin sự triển khai (Rollback strategies and safety mechanisms Rollback18 capability is the safety net that enables confident deployment). Mà không (có) (đáng) tin cậy sự quay lui, các đội trở nên (sự) e ngại-triển khai (deployment-averse) và làm chậm (lại) (của) họ
(sự) lặp vận tốc (Without reliable rollback, teams become deployment-averse and slow their iteration velocity). (Có tính) Hiệu quả sự quay lui yêu cầu (việc) lập kế hoạch cho ba khác biệt các tình huống (Effective rollback requires planning for three distinct scenarios):

795
17
Xanh dương-Xanh lá cây (Blue-Green) Sự triển-
khai (Deploy-ment):
Duy trì hai có thể so-
sánh (com-parable) sản xuất các môi-
trường (environ-ments), “xanh dương” ((đang) phục vụ hiện-
tại (cur-rent) lưu lượng truy cập) và “xanh lá cây” ((đang) chạy
(cái) ứng cử viên),
(sau) đó
chuyển đổi (switches) lưu lượng truy cập trong một định tuyến
sự thay đổi một khi (cái) xanh lá cây môi-
trường vượt qua sự xác thực.
Bởi vì sự quay lui là một lưu lượng truy cập
(sự) lật (flip) thay vì một (được) chạy thử sự tháo nước (drain),
sự phục hồi (recovery) có thể (là) nhanh hơn một
(mang tính) dần dần chim yến (canary) cho không trạng thái
các dịch vụ. (Cái) sự đánh đổi là bổ-
sung (ex-tra) cơ sở hạ tầng trong suốt
(cái) (sự) chuyển đổi, vì vậy xanh dương-xanh lá cây chiến thắng
hơn (over) chim yến khi ngắn (brief) (bị) trùng-
lặp (dupli-cate) sức chứa là (có thể) chấp nhận (được) và
mỗi-phân đoạn (per-segment) (thuộc về) thống kê sự xác-
thực (valida-tion) là đắt đỏ.
18
Sự quay lui (từ Cơ sở dữ liệu
Giao dịch
Sự quản lý):
Này
“hoàn tác” (undo)
hành động
cho
các sự triển khai (được) phức tạp hóa
trong ML bởi phụ thuộc-mô hình
trạng thái (cho ví dụ, (được) lưu trữ đệm (cached)
các (sự) nhúng (embeddings)) thứ (mà) (là) thường
không tương thích (incompatible) giữa mô hình
các phiên bản.
(Cái) rủi ro của này
trạng thái-phiên bản
sự không khớp (mismatch)
(thứ (mà) có thể gây ra (các) giờ của
thời gian chết (downtime) (so) với (các) giây cho một
không trạng thái dịch vụ) là (cái) (mang tính) trực tiếp
nguyên nhân
của
(cái)
sự triển khai
sự e ngại (aversion) và chậm (sự) lặp
vận tốc (được) đề cập.
(Cái) nhanh nhất tầng, (mang tính) ngay lập tức sự quay lui, giải quyết (mang tính) tới hạn các sự thất bại (được) phát hiện ngay sau sự triển khai:
phục vụ các lỗi, độ trễ các gai (spikes), hay rõ ràng dự đoán các sự thất bại (The fastest tier, immediate rollback, addresses critical failures detected right after deployment: serving errors, latency spikes, or obvious prediction failures). Nó yêu cầu (việc) giữ (cái) (trước) đó mô hình
phiên bản (được) tải và ấm vì vậy lưu lượng truy cập có thể chuyển đổi (mà) không (có) lạnh-khởi động độ trễ (It requires keeping the previous model version loaded and warm so traffic can switch without cold-start delay). Nhanh chóng sự quay lui xử lý hiệu-
suất (per-formance) sự xuống cấp (được) phát hiện thông qua chim yến các số liệu trong (vòng) (cái) đầu tiên giờ, thứ (mà) yêu cầu mô hình
cơ quan đăng ký sự tích hợp (thứ) mà giữ (trước) đó các phiên bản (có thể) triển khai (được) với tối thiểu cấu hình các sự thay đổi (Rapid rollback handles per-formance degradation detected through canary metrics within the first hour, which requires model registry integration that keeps previous versions deployable with minimal configuration changes).
(Bị) Trì hoãn sự quay lui giải quyết (mang tính) tinh vi các vấn đề (được) phát hiện thông qua (thuộc về) kinh doanh các số liệu hay người dùng phản hồi sau đầy (đủ)
sự triển khai, nơi sự quay lui phải tính đến (account for) phụ thuộc-mô hình dữ liệu (chẳng) hạn như sự cá nhân hóa trạng thái
hay (được) lưu trữ đệm các (sự) nhúng (được) tích lũy trong suốt (cái) mới mô hình’s hoạt động (Delayed rollback addresses subtle issues detected through business metrics or user feedback after full deployment, where rollback must account for model-dependent data such as personalization state or cached embeddings accumulated during the new model’s operation).
Bảng 14.11 tóm tắt sự triển khai các mẫu cho mỗi sự quay lui loại (Table 14.11 summarizes implementation patterns for each rollback type):
Bảng 14.11: Sự quay lui Các mẫu Theo Tình huống: Mỗi sự quay lui loại yêu cầu khác biệt cơ sở hạ tầng sự hỗ trợ và trạng thái sự xử lý
các chiến lược (Table 14.11: Rollback Patterns by Scenario: Each rollback type requires different infrastructure support and state handling strategies). (Mang tính) Ngay lập tức sự quay lui đòi hỏi (demands) luôn-ấm (always-warm) (các chế độ) dự phòng (standbys); (bị) trì hoãn sự quay lui có thể yêu cầu dữ liệu di cư (migration) các quy trình (Immediate rollback demands always-warm standbys; delayed rollback may require data migration procedures).
Sự quay lui Loại
Bộ kích hoạt
Sự triển khai
Trạng thái Sự xử lý
Ngay lập tức
Phục vụ các lỗi, các sự cố
Nóng (chế độ) dự phòng với (mang tính) tức thời (sự) chuyển đổi
Không trạng thái—không (có) đặc biệt sự xử lý
Nhanh chóng
Chim yến số liệu sự xuống cấp
Dựa trên-cơ quan đăng ký sự triển khai lại
Xóa các bộ nhớ cache, khởi động lại các phiên
Trì hoãn
(Thuộc về) Kinh doanh số liệu sự suy giảm
Đầy (đủ) sự triển khai lại với sự di cư
Di cư trạng thái, phát lại nếu (được) cần
Sự quay lui việc kiểm thử Sự quay lui các quy trình (thứ) mà (đã) chưa bao giờ được kiểm thử sẽ thất bại khi (được) cần, và (cái) sự thất bại
chế độ là (một cách) đặc biệt quỷ quyệt (insidious): (cái) đội khám phá (cái) khoảng trống tại 3:00 AM trong suốt một (mang tính) chủ động sự cố,
khi (thuộc về) nhận thức (cognitive) tải là cao nhất và thời gian áp lực là lớn nhất (Rollback testing Rollback procedures that have never been tested will fail when needed, and the failure mode is particularly insidious: the team discovers the gap at 3:00 AM during an active incident, when cognitive load is highest and time pressure is greatest). (Không được) Kiểm thử các sự quay lui thất bại cho bốn khác biệt
các lý do, mỗi (lý do) tương ứng với một khác cơ sở hạ tầng khoảng trống (Untested rollbacks fail for four distinct reasons, each corresponding to a different infrastructure gap). Đầu tiên, các cơ học (mechanics) của (việc) chuyển đổi
mô hình các phiên bản thường bao gồm (mang tính) tinh vi cấu hình các sự phụ thuộc (môi trường các biến, đặc trưng
cờ các trạng thái, định tuyến các quy tắc) (thứ) mà hoạt động (một cách) khác biệt dưới sự căng thẳng so với trong tài liệu (First, the mechanics of switching model versions often involve subtle configuration dependencies (environment variables, feature flag states, routing rules) that work differently under stress than in documentation). Hàng tháng “cứu hỏa
các cuộc diễn tập (drills)” nơi các đội thực hành (việc) cuộn lại (tới) (trước) đó các phiên bản phơi bày (expose) những các khoảng trống này trước khi chúng quan trọng (matter) (Monthly “fire drills” where teams practice rolling back to previous versions expose these gaps before they matter).
Thứ hai, thủ công sự quay lui các quyết định giới thiệu (mang tính) nguy hiểm độ trễ; (việc) xác định (được) tự động hóa các ngưỡng
(cho ví dụ, “nếu P99 độ trễ vượt quá 2× đường cơ sở trong 5 phút, kích hoạt sự quay lui”) loại bỏ (con) người
phản ứng thời gian từ (cái) tới hạn con đường (Second, manual rollback decisions introduce dangerous latency; defining automated thresholds (for example, “if P99 latency exceeds 2× baseline for 5 minutes, trigger rollback”) removes human reaction time from the critical path). Thứ ba, (cái) (được) cuộn-lại (rolled-back) mô hình phải sản xuất (có tính) nhất quán hành vi
thay vì (bị) làm hỏng (corrupted) các dự đoán từ cũ (stale) các bộ nhớ cache hay (đã) lỗi thời đặc trưng các giá trị—một sự xác thực bước
(thứ) mà (là) tầm thường (trivial) để bỏ qua trong việc kiểm thử nhưng (là) (có tính) thảm họa để bỏ lỡ trong sản xuất (Third, the rolled-back model must produce consistent behavior rather than corrupted predictions from stale caches or outdated feature values—a validation step that is trivial to skip in testing but catastrophic to miss in production). Cuối cùng, từng-bước cẩm nang (runbook)
tài liệu đảm bảo rằng (cái) người (đang) thực thi (cái) sự quay lui cần (không) (phải) (là) (cái) người (đã) thiết kế
nó, một thuộc tính (thứ) mà trở nên thiết yếu khi (as) đội các quy mô phát triển và trực ban (on-call) các (sự) luân phiên (rotations) mở rộng (widen) (Finally, step-by-step runbook documentation ensures that the person executing the rollback need not be the person who designed it, a property that becomes essential as team sizes grow and on-call rotations widen).
Có trạng thái (Stateful) vs. không trạng thái sự quay lui ML các hệ thống khác nhau (vary) (về) tính có trạng thái (statefulness), (việc) ảnh hưởng (đến) sự quay lui độ phức tạp (Stateful vs. stateless rollback ML systems vary in statefulness, affecting rollback complexity):
• Không trạng thái các mô hình: Sự phân loại và sự hồi quy sự quay lui bao gồm chỉ (việc) chuyển đổi mô hình các trọng số,
bởi vì mỗi dự đoán là độc lập (Stateless models: Classification and regression rollback involves only switching model weights, because each prediction is independent).
• Có trạng thái các mô hình: (Có tính) Tuần tự sự gợi ý và (thuộc về) hội thoại các hệ thống phải xem xét
(được) tích lũy người dùng trạng thái, và sự quay lui có thể yêu cầu phiên các (sự) thiết lập lại hay trạng thái sự di cư (Stateful models: Sequential recommendation and conversational systems must consider accumulated user state, and rollback may require session resets or state migration).
• Các mô hình với phản hồi các vòng lặp: Phản hồi-được thúc đẩy (driven) các mô hình có thể không khôi phục (trước) đó hành vi nếu
đào tạo dữ liệu đã bị (bị) ô nhiễm (contaminated) trong suốt (cái) (có) vấn đề (problematic) sự triển khai cửa sổ (Models with feedback loops: Feedback-driven models may not restore previous behavior if training data was contaminated during the problematic deployment window).
Cho có trạng thái các hệ thống, triển khai “sự quay lui các điểm kiểm tra” (thứ) mà nắm bắt (có tính) nhất quán trạng thái các ảnh chụp nhanh tại
sự triển khai các ranh giới, (việc) kích hoạt sạch sự khôi phục (restoration) (mà) không (có) (có thể) nhìn thấy-(đối với)-người dùng sự gián đoạn (For stateful systems, implement “rollback checkpoints” that capture consistent state snapshots at deployment boundaries, enabling clean restoration without user-visible disruption).
A/B việc kiểm thử cho mô hình sự xác thực A/B việc kiểm thử cung cấp (cái) (thuộc về) thống kê nền tảng cho sự triển khai
các quyết định bằng (cách) (việc) so sánh mô hình các phiên bản dưới (được) kiểm soát các điều kiện (A/B testing for model validation A/B testing provides the statistical foundation for deployment decisions by comparing model versions under controlled conditions). Không giống như chim yến các sự triển khai
((thứ) mà xác thực (thuộc về) hoạt động độ ổn định), A/B các bài kiểm tra đo lường liệu một mới mô hình (có) cải thiện (thuộc về) kinh doanh
các kết cục (outcomes) với (thuộc về) thống kê sự tự tin (hay không) (Unlike canary deployments (which validate operational stability), A/B tests measure whether a new model improves business outcomes with statistical confidence).
Sự thử nghiệm (sự) thiết lập (setup) và quyết định các quy tắc Một hợp lệ (valid) A/B bài kiểm tra bắt đầu với bốn các sự kiểm soát (thứ) mà làm (cho) (cái) (sau) đó
sự triển khai quyết định (về mặt) thống kê (có) ý nghĩa (Experiment setup and decision rules A valid A/B test starts with four controls that make the later deployment decision statistically meaningful). (Cái) Sự ngẫu nhiên hóa (Randomization) Đơn vị xác định (những) gì (được) ngẫu nhiên
(được) gán cho (sự) điều trị (treatment) vs. (sự) kiểm soát (The Randomization Unit defines what gets randomly assigned to treatment vs. control). Người dùng-cấp độ sự ngẫu nhiên hóa đảm bảo (có tính) nhất quán trải nghiệm nhưng
yêu cầu lớn hơn mẫu các quy mô (User-level randomization ensures consistent experience but requires larger sample sizes). Yêu cầu-cấp độ sự ngẫu nhiên hóa kích hoạt nhanh hơn các sự thử nghiệm nhưng có thể
gây nhầm lẫn (cho) (các) người dùng (đang) thấy khác các kết quả (Request-level randomization enables faster experiments but can confuse users seeing different results).
Mẫu quy mô sự tính toán: Xác định (được) yêu cầu lưu lượng truy cập trước khi ra mắt (đang) sử dụng phương trình 14.9 (Sample size calculation: Determine required traffic before launch using equation 14.9):
𝑛=
2(𝑧𝛼/2 +𝑧𝛽)2𝜎2
𝛿2
(14.9)

796
14.5 Sản xuất Các hoạt động
19
Phi máy chủ (Serverless) ML Sự suy-
luận (Infer-ence): (Cái) chi phí-tính hiệu quả của
này tùy chọn xuất phát (stems) từ (việc) cung-
cấp (provi-sioning) (việc) tính toán chỉ khi (upon)
yêu cầu và (việc) mở rộng quy mô (về) không
khi nhàn rỗi, (việc) loại bỏ (eliminating) (cái)
chi phí của một (mang tính) bền bỉ điểm cuối.
Điều này tạo ra một (mang tính) trực tiếp sự căng thẳng
với hiệu suất các mục tiêu, khi (as)
(cái) đầu tiên yêu cầu sau một nhàn rỗi
khoảng thời gian gánh chịu một “lạnh khởi động” độ-
trễ (la-tency) hình phạt (penalty) trong khi (cái) mô hình
được tải vào bộ nhớ. Cho
lớn các mô hình, đó sự trì hoãn có thể
(đủ) dài để vi phạm thời gian-thực (real-time)
độ trễ các ngân sách trừ khi
(cái) dịch vụ giữ ấm sức-
chứa (capac-ity) hay sử dụng một thời gian chạy (được) thiết kế
cho nhanh (việc) tải.
nơi 𝛿là (cái) tối thiểu (có thể) phát hiện (được) tác động, 𝜎là kết cục (outcome) tiêu chuẩn độ lệch, và 𝑧các giá trị phụ thuộc vào
(được) mong muốn sự tự tin ((một cách) điển hình 95 phần trăm) và sức mạnh (power) ((một cách) điển hình 80 phần trăm) (where 𝛿is the minimum detectable effect, 𝜎is outcome standard deviation, and 𝑧values depend on desired confidence (typically 95 percent) and power (typically 80 percent)). Cho một 2 phần trăm (có tính) tương đối
(sự) nâng lên (lift) trên một 5 phần trăm đường cơ sở chuyển đổi tỷ lệ (5 phần trăm lên 5.1 phần trăm) và 80 phần trăm sức mạnh, kỳ vọng
(một cách) xấp xỉ (roughly) 745,644 các người dùng mỗi biến thể (variant); 25,000 các người dùng mỗi biến thể sẽ chỉ phát hiện một lớn (hơn) (nhiều) (sự) nâng lên,
khoảng 0.5 phần trăm các điểm (một cách) tuyệt đối (For a 2 percent relative lift on a 5 percent baseline conversion rate (5 percent to 5.1 percent) and 80 percent power, expect roughly 745,644 users per variant; 25,000 users per variant would only detect a much larger lift, about 0.5 percentage points absolute).
Lan can Các số liệu: Xác định các số liệu (thứ) mà phải không (xuống cấp) ngay cả nếu chính số liệu cải thiện (Guardrail Metrics: Define metrics that must not degrade even if primary metric improves). Một
sự gợi ý mô hình (đang) cải thiện nhấp chuột-xuyên qua tỷ lệ bởi 10 phần trăm trong khi (đang) tăng trang tải thời gian
bởi 500 ms có thể thất bại lan can các sự kiểm tra (A recommendation model improving click-through rate by 10 percent while increasing page load time by 500 ms may fail guardrail checks).
Thời gian chạy (Runtime): Chạy các bài kiểm tra cho đến khi đạt (được) (thuộc về) thống kê tính có ý nghĩa, (một cách) điển hình 1–2 (các) tuần tối thiểu để nắm bắt
hàng tuần các mẫu (Runtime: Run tests until reaching statistical significance, typically 1–2 weeks minimum to capture weekly patterns). Tránh “việc nhìn trộm (peeking)” vào các kết quả và (việc) dừng (lại) sớm, vì điều này làm thổi phồng (inflates) dương tính giả các tỷ lệ (Avoid “peeking” at results and stopping early, as this inflates false positive rates).
Những các sự kiểm soát đó thiết lập (cái) (thuộc về) thống kê bao thư (envelope), nhưng ML các hệ thống thêm (vào) sự thất bại các chế độ (thứ) mà thông thường
web các sự thử nghiệm có thể che giấu (hide) (Those controls establish the statistical envelope, but ML systems add failure modes that ordinary web experiments can hide). Chuyển đổi các sự kiện có thể đến (nhiều) ngày sau (khi) dự đoán, (việc) tạo ra (bị) trì hoãn
phản hồi: một sự gợi ý (được) cho thấy Thứ Hai có thể thúc đẩy một (sự) mua hàng Thứ Sáu, vì vậy (cái) (sự) quy kết cửa sổ
phải là phần của (cái) bài kiểm tra thiết kế (Conversion events may arrive days after prediction, creating delayed feedback: a recommendation shown Monday can drive a purchase Friday, so the attribution window must be part of the test design). Tính mới mẻ (Novelty) các hiệu ứng (effects) có thể cũng thổi phồng sớm hiệu suất khi (as) (các) người dùng tương tác
với tươi mới các sự gợi ý, (đó) là tại sao trưởng thành các sự thử nghiệm bao gồm một sự cháy-trong (burn-in) khoảng thời gian trước khi
sự đo lường (Novelty effects can also inflate early performance as users engage with fresh recommendations, which is why mature experiments include a burn-in period before measurement).
Sự gợi ý và việc xếp hạng các hệ thống thêm (vào) sự can thiệp (interference) các tác động bởi vì (việc) cho thấy một mặt hàng (tới) một
người dùng có thể ảnh hưởng (tới) (những) gì duy trì (có) sẵn hay nổi bật (salient) đối với (một) (người) khác, (việc) vi phạm (cái) (tính) độc lập giả định
đằng sau tiêu chuẩn A/B sự phân tích (Recommendation and ranking systems add interference effects because showing an item to one user can affect what remains available or salient for another, violating the independence assumption behind standard A/B analysis). Phân đoạn tính không đồng nhất (heterogeneity) tạo ra một thứ hai sự phân tích bài toán: một (mang tính) tổng thể
trung lập kết quả có thể che giấu mạnh mẽ (mang tính) tích cực các tác động cho một thuần tập (cohort) và (mang tính) tiêu cực các tác động cho (một) (thuần tập) khác (Segment heterogeneity creates a second analysis problem: an overall neutral result may hide strong positive effects for one cohort and negative effects for another). Những
các sự phức tạp (complications) này không làm mất hiệu lực A/B việc kiểm thử, nhưng chúng làm (cho) các lan can, phân đoạn sự phân tích, và
(được) đăng ký trước (preregistered) các quyết định (thành) phần của (cái) sự thử nghiệm thay vì sau-(cái)-thực tế (after-the-fact) sự diễn giải (These complications do not invalidate A/B testing, but they make guardrails, segment analysis, and preregistered decisions part of the experiment rather than after-the-fact interpretation).
Bảng 14.12 biến những các sự ép buộc đó thành một sự triển khai quyết định (Table 14.12 turns those constraints into a deployment decision):
Bảng 14.12: A/B Bài kiểm tra Quyết định Ma trận: Sự triển khai các quyết định nên xem xét cả chính các số liệu và các lan can (Table 14.12: A/B Test Decision Matrix: Deployment decisions should consider both primary metrics and guardrails).
Các sự cải thiện (thứ) mà đến tại (cái) chi phí của lan can các sự vi phạm yêu cầu cẩn thận sự đánh đổi sự phân tích thay vì (mang tính) tự động sự triển khai (Improvements that come at the cost of guardrail violations require careful trade-off analysis rather than automatic deployment).
Chính Số liệu
Các lan can
Quyết định
(Đáng) Kể sự cải thiện
Tất cả vượt qua
Phát hành (Ship) mới mô hình
(Đáng) Kể sự cải thiện
Một số thất bại
Điều tra các sự đánh đổi, có thể cần mô hình (sự) lặp (iteration)
Không (có) (đáng) kể sự thay đổi
Tất cả vượt qua
Mới mô hình thêm không (có) giá trị; giữ hiện tại trừ khi (đang) đơn giản hóa (simplifying)
(Đáng) Kể sự xuống cấp
N/A
Không phát hành; điều tra gốc rễ nguyên nhân
(Cái) bảng (thì) chỉ (đáng) tin cậy khi (cái) sự phân tích quy trình là (có) kỷ luật trước khi ra mắt (The table is only reliable when the analysis process is disciplined before launch). Các đội nên
đăng ký trước (preregister) (được) kỳ vọng các tác động trước khi (cái) bài kiểm tra bắt đầu và chọn (cái) sự ngẫu nhiên hóa đơn vị, (sự) quy kết
cửa sổ, các lan can, và tối thiểu thời gian chạy trước khi (việc) quan sát các kết cục (Teams should preregister expected effects before the test begins and choose the randomization unit, attribution window, guardrails, and minimum runtime before observing outcomes).
(Cái) cùng kỷ luật phải tiếp tục trong suốt sự phân tích (The same discipline has to continue during analysis). (Có tính) Tuần tự việc kiểm thử hỗ trợ hợp lệ (thuộc về) tạm thời (interim)
các quyết định bằng (cách) (việc) xác định trước khi nào (việc) dừng (lại) sớm (được) (về mặt) thống kê (được) cho phép, và phương sai-sự giảm (reduction) các kỹ-
thuật (tech-niques) (chẳng) hạn như CUPED ((Được) Kiểm soát-sự thử nghiệm (Sử dụng) Trước-Sự thử nghiệm Dữ liệu) giảm thiểu số liệu (tiếng) ồn
bằng (cách) (việc) điều chỉnh các kết cục với trước-sự thử nghiệm (các) hiệp biến (covariates) (Sequential testing supports valid interim decisions by predefining when early stopping is statistically allowed, and variance-reduction tech-niques such as CUPED (Controlled-experiment Using Pre-Experiment Data) reduce metric noise by adjusting outcomes with pre-experiment covariates). (Bị) Thất bại các sự thử nghiệm nên được lưu trữ (archived)
bởi vì chúng mã hóa (encode) (mang tính) tiêu cực chứng cứ, và (cái) sự phân tích đường ống nên được tự động hóa vì vậy thủ công
bảng tính công việc không trở thành một mới nguồn của sự triển khai lỗi (Failed experiments should be archived because they encode negative evidence, and the analysis pipeline should be automated so manual spreadsheet work does not become a new source of deployment error).
Một A/B quyết định chỉ quan trọng nếu (cái) sự phát hành máy móc (machinery) có thể thăng cấp, giữ, hay cuộn lại (cái) chính xác
đồ tạo tác (thứ) mà đã được kiểm thử (An A/B decision only matters if the release machinery can promote, hold, or roll back the exact artifact that was tested). Mô hình các cơ quan đăng ký, (chẳng) hạn như Vertex AI’s mô hình cơ quan đăng ký (Cloud 2024b), hành động như
(được) tập trung hóa các kho lưu trữ cho (việc) lưu trữ và (việc) quản lý (được) đào tạo các mô hình và các phiên bản (Model registries, such as Vertex AI’s model registry (Cloud 2024b), act as centralized repositories for storing and managing trained models and versions). Mô hình các danh mục (catalogs)
phục vụ một khác vai trò: Vertex AI Model Garden giúp các đội khám phá, kiểm thử, tùy chỉnh, và triển khai
Google, đối tác, và (được) chọn nguồn-mở các mô hình (Google Cloud 2026a) (Model catalogs serve a different role: Vertex AI Model Garden helps teams discover, test, customize, and deploy Google, partner, and selected open-source models (Google Cloud 2026a)). Llama thuộc về (trong) đó
mô hình-gia đình và mô hình-danh mục bối cảnh, không (phải) trong (cái) cơ quan đăng ký vòng đời (sự) tuyên bố (claim) (Touvron, Martin, và cộng sự.
2023) (Llama belongs in that model-family and model-catalog context, not in the registry lifecycle claim (Touvron, Martin, et al. 2023)).
Sự suy luận các điểm cuối mang đó (được) kiểm thử đồ tạo tác vào trực tiếp lưu lượng truy cập (Inference endpoints carry that tested artifact into live traffic). Chúng (một cách) điển hình phơi bày (expose) (cái) (được) triển khai
mô hình thông qua REST các API cho thời gian-thực các dự đoán (They typically expose the deployed model via REST APIs for real-time predictions). Phụ thuộc vào hiệu suất các yêu cầu, các đội
có thể cấu hình các tài nguyên, (chẳng) hạn như GPU các bộ tăng tốc, để đáp ứng độ trễ và thông lượng các mục tiêu (Depending on performance requirements, teams can configure resources, such as GPU accelerators, to meet latency and throughput targets). Một số
các nhà cung cấp cũng cung cấp (có tính) linh hoạt các tùy chọn giống như phi máy chủ19 hay lô sự suy luận, (việc) loại bỏ (cái) nhu cầu cho
(mang tính) bền bỉ các điểm cuối và (việc) kích hoạt chi phí-hiệu quả, (có thể) mở rộng quy mô các sự triển khai (Some providers also offer flexible options like serverless19 or batch inference, eliminating the need for persistent endpoints and enabling cost-efficient, scalable deployments).

797
20
MLflow:
(Được) Tạo ra bởi
Databricks sau (khi) (việc) quan sát
rằng các dữ liệu (nhà) khoa học (đã) đang theo-
dõi (track-ing) mô hình các kết quả trong (các) bảng-
tính (spread-sheets) và (đã) có thể không bao giờ tái-
tạo (repro-duce) (những) (của) họ tốt nhất các sự thử nghiệm.
(Cái) “mô hình cơ quan đăng ký” khái niệm
nó (đã) phổ biến giải quyết (cái)
(thuộc về) tổ hợp (combinatorial) (sự) bùng nổ bài-
toán: với 𝑁các siêu tham số (hyperparame-ters), 𝑀dữ liệu các phiên bản, và 𝐾
mã các nhánh, thủ công (việc) theo-
dõi trở nên khó giải quyết (intractable), và
(cái) tính không thể (inability) (để) tái tạo một (được) triển-
khai (de-ployed) mô hình trở thành một quản-
trị (gov-ernance) và (việc) gỡ lỗi (khoản) nợ (liabil-ity).
21
Ray:
Một (được) phân tán
(việc) tính toán khuôn khổ từ
UC Berkeley (Moritz và cộng sự.
2018) thứ (mà) cung cấp một (được) hợp-
nhất (uni-fied) tác vụ và tác nhân (actor) giao-
diện (inter-face), (được) chống lưng (backed) bởi một (được) phân tán
(bộ) lên lịch và chịu-lỗi
cửa hàng.
(Cái) rộng hơn MLOps
bài học là (rằng) (bị) phân mảnh (fragmented) cơ-
sở hạ tầng (in-frastructure) tạo ra (sự) biên-dịch (transla-tion) các điểm nơi việc tiền xử-
lý (preprocess-ing) logic, (sự) chuẩn hóa các hằng-
số (con-stants), bộ mã hóa (tokenizer) các phiên bản, hay
đồ tạo tác các định dạng có thể phân kỳ
(một cách) im lặng.
(Được) Chia sẻ sự thực thi
các sự trừu tượng hóa có thể giảm (thiểu) đó
sự phân mảnh, nhưng đào tạo-
phục vụ sự sai lệch vẫn yêu cầu
(mang tính) rõ ràng sự nhất quán các sự kiểm tra
(xuyên) qua dữ liệu, các đặc trưng, và phục-
vụ mã.
Để duy trì dòng dõi và tính có thể kiểm toán, các đội theo dõi mô hình các đồ tạo tác, bao gồm các kịch bản, các trọng số, các nhật ký,
và các số liệu, (đang) sử dụng các công cụ giống như MLflow20 (Databricks 2024) (To maintain lineage and auditability, teams track model artifacts, including scripts, weights, logs, and metrics, using tools like MLflow20 (Databricks 2024)). Cùng nhau, các cơ quan đăng ký, các điểm cuối, dòng dõi
việc theo dõi, và (được) phân tán sự điều phối các khuôn khổ giống như Ray21 biến A/B các kết cục thành (được) kiểm soát
sản xuất các sự thay đổi: (cái) (được) kiểm thử mô hình có thể (được) (được) thăng cấp, (được) quan sát, và (được) đảo ngược (mà) không (bị) mất
nguồn gốc (provenance) (Together, registries, endpoints, lineage tracking, and distributed orchestration frameworks like Ray21 turn A/B outcomes into controlled production changes: the tested model can be promoted, observed, and reversed without losing provenance).
14.5.1.2 Mô hình định dạng sự tối ưu hóa
Một PyTorch mô hình (thứ) mà đạt được cao nhất độ chính xác trên một điểm chuẩn có thể phục vụ các dự đoán tại 200 ms độ trễ
trong sản xuất, mười lần chậm hơn (cái) SLO yêu cầu (A PyTorch model that achieves top accuracy on a benchmark may serve predictions at 200 ms latency in production, ten times slower than the SLO requires). (Cái) khoảng trống giữa nghiên cứu các khuôn khổ và
sản xuất (việc) phục vụ thường là (đáng) kể, và định dạng sự tối ưu hóa kết nối (bridges) nó (The gap between research frameworks and production serving is often substantial, and format optimization bridges it). (Được) Tối ưu hóa các định dạng
có thể cải thiện độ trễ bằng (cách) (việc) chuyển đổi các mô hình thành các sự biểu diễn (được) thiết kế riêng (tailored) cho (mang tính) đặc thù phần cứng, nhưng
(cái) (sự) tăng thêm (gain) (thì) (là) phụ thuộc-khối lượng công việc và -thời gian chạy (Optimized formats can improve latency by converting models into representations tailored for specific hardware, but the gain is workload- and runtime-dependent). (Cái) sự suy luận các thời gian chạy và độ chụm các chiến lược
(được) chi tiết trong phần 13.9 và phần 13.9.2 cung cấp (các) (thuộc về) kỹ thuật các nền tảng; này phần tập trung vào
(cái) (thuộc về) hoạt động quy trình làm việc (The inference runtimes and precision strategies detailed in section 13.9 and section 13.9.2 provide the technical foundations; this section focuses on the operational workflow).
(Cái) đầu tiên (thuộc về) hoạt động ranh giới là sự biểu diễn (The first operational boundary is representation). ONNX (Mở Thần kinh Mạng (Sự) Trao đổi (Exchange)) là một
(một cách) rộng rãi (được) sử dụng (sự) trao đổi định dạng cho mô hình tính có thể mang theo (được) (portability), nhưng (cái) sự lựa chọn của sự tối ưu hóa khuôn khổ
quyết định cả (các) phần cứng các mục tiêu (có) sẵn và (cái) hiệu suất trần (có thể) tiếp cận (được) (ONNX (Open Neural Network Exchange) is a widely used interchange format for model portability, but the choice of optimization framework determines both the hardware targets available and the performance ceiling reachable). Rộng hơn
sự tương thích thông qua ONNX Thời gian chạy (Runtime) đến tại (cái) chi phí của đỉnh hiệu suất, trong khi tối đa
thông lượng thông qua TensorRT khóa sự triển khai (tới) một đơn nhà cung cấp (vendor), như bảng 14.13 tóm tắt (Broader compatibility through ONNX Runtime comes at the cost of peak performance, while maximum throughput through TensorRT locks deployment to a single vendor, as table 14.13 summarizes). Một
điển hình quy trình làm việc xuất khẩu một PyTorch mô hình sang ONNX, chạy cấp-đồ-thị dọn dẹp (hằng số (sự) gấp (folding),
mã-chết sự loại bỏ (elimination)), áp dụng toán tử (operator) sự dung hợp (fusion) ((chẳng) hạn như Conv+BN+ReLU (được) thu gọn (collapsed) thành một đơn op),
và lượng tử hóa các trọng số (FP32 sang INT8) trước khi triển khai (tới) (cái) mục tiêu thời gian chạy (A typical workflow exports a PyTorch model to ONNX, runs graph-level cleanup (constant folding, dead-code elimination), applies operator fusion (such as Conv+BN+ReLU collapsed into a single op), and quantizes weights (FP32 to INT8) before deploying to the target runtime). (Thuộc về) Số sự tương đương (equivalence)
đối với (cái) nguồn mô hình phải được xác thực tại mỗi bước (Numerical equivalence to the source model must be validated at each step).
Bảng 14.13: Mô hình Sự tối ưu hóa Các khuôn khổ: Khác nhau sự tối ưu hóa các công cụ nhắm mục tiêu (đến) khác nhau sự triển khai các tình huống (Table 14.13: Model Optimization Frameworks: Different optimization tools target different deployment scenarios). TensorRT
cung cấp tối đa hiệu suất trên NVIDIA (các) GPU nhưng khóa các sự triển khai vào đó phần cứng (TensorRT provides maximum performance on NVIDIA GPUs but locks deployments into that hardware). ONNX Runtime cung cấp rộng hơn
sự tương thích (xuyên) qua phần cứng các mục tiêu (ONNX Runtime offers broader compatibility across hardware targets). OpenVINO tối ưu hóa cho Intel phần cứng các hệ sinh thái (OpenVINO optimizes for Intel hardware ecosystems).
Khuôn khổ
Nguồn Các định dạng
Mục tiêu Phần cứng
Chính Các sự tối ưu hóa
ONNX Runtime
PyTorch, TF, Keras, scikit
CPU, GPU, NPU
Đồ thị sự tối ưu hóa, toán tử sự dung hợp,
sự lượng tử hóa
TensorRT
ONNX, TF, PyTorch
NVIDIA GPU chỉ
Hạt nhân (tính) tự động-tinh chỉnh, độ chụm
sự hiệu chuẩn, lớp sự dung hợp
OpenVINO
ONNX, TF, PyTorch, Caffe,
MXNet
Intel CPU, GPU, VPU, FPGA
Mô hình sự nén (compression), không đồng bộ (async) sự thực thi,
(việc) lưu trữ đệm (caching)
TF-TRT
TensorFlow
NVIDIA GPU
TensorRT sự tích hợp bên trong
TensorFlow đồ thị
Core ML
ONNX, TF, PyTorch
Apple Thần kinh Công cụ (Engine), GPU, CPU
(Được) Hợp nhất định dạng cho Apple các thiết bị,
trên-thiết bị sự suy luận
TFLite
TensorFlow, Keras
Di động CPU, GPU, Rìa (Edge) TPU
Sự lượng tử hóa, người đại diện (delegate) sự hỗ trợ,
mô hình sự nén
(Cái) bền mẫu không phải (là) (cái) sản phẩm danh sách mà (là) (cái) sự trao đổi (mà) nó phơi bày (exposes): mọi (sự) tăng thêm trong đỉnh
thông lượng được mua với một số mức độ của phần cứng hay thời gian chạy (sự) cam kết, vì vậy khuôn khổ
sự lựa chọn là một tính có thể mang theo (được) so với đỉnh-hiệu suất quyết định trước khi nó là một đặc trưng sự so sánh (The durable pattern is not the product list but the exchange it exposes: every gain in peak throughput is purchased with some degree of hardware or runtime commitment, so framework choice is a portability versus peak-performance decision before it is a feature comparison). Độ chụm
là (cái) thứ hai ranh giới (Precision is the second boundary). Sự lượng tử hóa giảm (thiểu) mô hình kích thước và tăng thông lượng bằng (cách) (việc) sử dụng
thấp hơn-độ chụm số học (arithmetic), nhưng từ một (thuộc về) hoạt động góc nhìn (cái) chính sự triển khai câu hỏi không phải (là)
liệu INT8 (có) (là) nhanh hơn (hay không) (Quantization reduces model size and increases throughput by using lower-precision arithmetic, but from an operational perspective the key deployment question is not whether INT8 is faster). Nó là liệu (cái) (được) lượng tử hóa mô hình duy trì độ chính xác dưới sản xuất lưu lượng truy cập
các sự phân phối (hay không), không chỉ (merely) sự hiệu chuẩn các tập dữ liệu (It is whether the quantized model maintains accuracy under production traffic distributions, not merely calibration datasets). Các cơ học của PTQ, QAT, và hỗn hợp-độ chụm
các chiến lược được bao phủ trong Chương 10, với phục vụ-đặc thù độ chụm sự lựa chọn (bao gồm (mang tính) động
mỗi-yêu cầu độ chụm) (được) chi tiết trong phần 13.9.2 (The mechanics of PTQ, QAT, and mixed-precision strategies are covered in Chapter 10, with serving-specific precision selection (including dynamic per-request precision) detailed in section 13.9.2).
Sản xuất sự triển khai của (được) tối ưu hóa các mô hình do đó yêu cầu sự xác thực (thứ) mà nhắm mục tiêu (đến) (cái) sự thất bại
các chế độ (mà) sự tối ưu hóa có thể giới thiệu (một cách) im lặng (Production deployment of optimized models therefore requires validation that targets the failure modes optimization can introduce silently). Xem xét một đội (thứ) mà triển khai một INT8-(được) lượng tử hóa mô hình
sau (khi) (việc) xác minh chỉ thông lượng sự cải thiện: sự phân loại độ chính xác giảm (drops) trên hiếm nhưng cao-giá trị
biên các trường hợp, và (cái) sự xuống cấp trôi (goes) (mà) không bị phát hiện trong (các) tuần bởi vì (được) tổng hợp các số liệu duy trì
bên trong SLO các ranh giới (bounds) (Consider a team that deploys an INT8-quantized model after verifying only throughput improvement: classification accuracy drops on rare but high-value edge cases, and the degradation goes undetected for weeks because aggregate metrics remain within SLO bounds). (Cái) đầu tiên sự xác thực lớp là (thuộc về) số sự tương đương, (việc) so sánh (được) tối ưu hóa
các đầu ra so với (cái) ban đầu mô hình trên một (có tính) đại diện kiểm thử tập với ứng dụng-đặc thù sự phân kỳ (The first validation layer is numerical equivalence, comparing optimized outputs against the original model on a representative test set with application-specific divergence)

798
14.5 Vận hành trên môi trường sản xuất (Production Operations)
ngưỡng (thresholds). Sự kiểm tra đó là cần thiết nhưng không đủ vì các đầu vào hiếm, các ví dụ ngoài phân phối (out-of-distribution examples),
và các trường hợp cụ thể của phân nhóm (subgroup-specific cases) có thể bộc lộ các hiện tượng giả lượng tử hóa (quantization artifacts) mà các số liệu kiểm tra tổng hợp che giấu.
Lớp thứ hai là sự xác thực hoạt động (operational validation). Dấu chân bộ nhớ (Memory footprint) phải được đo lường tại mức sử dụng (utilization) 
thời gian chạy (runtime) đỉnh, bao gồm các cấp phát động (dynamic allocations) trong quá trình suy luận, vì một số tối ưu hóa đánh đổi việc tăng
bộ nhớ thời gian chạy để lấy tốc độ tính toán. Các yêu cầu khởi động (Warm-up requirements) rất quan trọng vì nhiều thời gian chạy (runtimes) 
được tối ưu hóa, bao gồm TensorRT và Accelerated Linear Algebra (XLA), yêu cầu các lần chạy suy luận ban đầu
để biên dịch các hạt nhân (kernels), tạo ra một sự tăng vọt độ trễ khởi động lạnh (cold-start latency spike) mà các thủ tục triển khai và các
kiểm tra sức khỏe (health checks) phải hấp thụ. Tính tương thích phiên bản thời gian chạy (Runtime version compatibility) sau đó đóng vòng lặp: các cấu hình triển khai
cần việc ghim phiên bản (version pinning) rõ ràng vì ngay cả những thay đổi thời gian chạy nhỏ cũng có thể ảnh hưởng đến cả các đặc điểm
hiệu suất và tính chính xác số học (numerical correctness).

14.5.1.3 Phục vụ suy luận (Inference serving)
Một mô hình được tối ưu hóa nằm trên đĩa không tạo ra giá trị nào. Nó cần cơ sở hạ tầng thời gian chạy (runtime infrastructure) để chấp nhận
các yêu cầu, thực thi suy luận, và trả về các dự đoán ở quy mô lớn (at scale). Các kiến trúc phục vụ (serving architectures) và các khuôn khổ 
thỏa thuận mức dịch vụ (service level agreement - SLA) và mục tiêu mức dịch vụ (service level objective - SLO) được trình bày chi tiết trong Chương 13 cung cấp
nền tảng kỹ thuật; phần này tập trung vào các xem xét hoạt động (operational considerations) cho việc lựa chọn và
quản lý cơ sở hạ tầng đó. Trong các thiết lập quy mô lớn (large-scale settings), các hệ thống phục vụ (serving systems) xử lý hàng chục nghìn tỷ
truy vấn suy luận (inference queries) mỗi ngày (C.-J. Wu và cộng sự, 2019), và khoảng cách giữa một hệ thống phục vụ đang hoạt động và một
hệ thống được vận hành tốt quyết định liệu các SLO có được đáp ứng một cách nhất quán qua các tháng và các năm hay không.
Các khuôn khổ phục vụ cấp độ sản xuất (Production-grade serving frameworks) như TensorFlow Serving (Olston và cộng sự, 2017), NVIDIA
Triton Inference Server (NVIDIA 2024d), và KServe (KServe Community 2024) cung cấp các cơ chế 
chuẩn hóa (standardized mechanisms) để triển khai, phiên bản hóa, và mở rộng quy mô (scaling) các mô hình. Từ góc độ vận hành,
quyết định quan trọng là khuôn khổ nào phù hợp nhất với ngữ cảnh triển khai: TensorFlow Serving cho
các quy trình làm việc (workflows) dựa trên TensorFlow, Triton cho việc phục vụ GPU đa khuôn khổ, và KServe cho các môi trường dựa trên Kubernetes
yêu cầu khả năng mở rộng xuống không (scale-to-zero).
Bất kể mô hình phục vụ (serving paradigm) nào được sử dụng (trực tuyến, ngoại tuyến, hoặc gần trực tuyến, như được trình bày chi tiết trong
phần 13.2.2), một hiểu biết vận hành (operational insight) quan trọng là thời gian suy luận mô hình (model inference time) thường là một phần nhỏ của
độ trễ đầu cuối (end-to-end latency). Việc phân rã ngân sách độ trễ (latency budget) tiết lộ nơi mà các điểm nghẽn hoạt động (operational bottlenecks) thực sự
nằm ở đâu.

Góc nhìn Hệ thống 14.1 (Systems Perspective 14.1): Ngân sách độ trễ (The latency budget)
Một dịch vụ có SLO 100 ms P99, và ngân sách suy luận mô hình là 45 ms; 55 ms còn lại
phải bao phủ mọi giai đoạn khác của đường dẫn yêu cầu (request path). Bảng 14.14 phân bổ ngân sách trên
toàn bộ vòng đời yêu cầu (request lifecycle).

Bảng 14.14: Các Thành phần của Ngân sách Độ trễ (Latency Budget Components): Việc phân bổ tiêu biểu của SLO 100 ms P99 trên toàn bộ vòng đời yêu cầu.
Suy luận mô hình chiếm 45 phần trăm tổng độ trễ, phần lớn còn lại dành cho mạng, việc trích xuất đặc trưng (feature retrieval), phân tích cú pháp (parsing),
hậu xử lý (postprocessing), và tuần tự hóa (serialization). Cột đòn bẩy tối ưu hóa (optimization-lever) cho thấy nơi mỗi thành phần có thể được giảm bớt.

Thành phần (Component) | Thị phần Ngân sách (Budget Share) | Ngân sách P99 (P99 Budget) | Đòn bẩy Tối ưu hóa (Optimization Lever)
Mạng RTT (Network RTT) | 15% | 15 ms | Triển khai biên (Edge deployment), gộp kết nối (connection pooling)
Trích xuất đặc trưng (Feature retrieval) | 25% | 25 ms | Bộ nhớ đệm đặc trưng (Feature caching), tính toán trước (precomputation)
Phân tích yêu cầu (Request parsing) | 5% | 5 ms | Giao thức nhị phân (gRPC), tối ưu hóa lược đồ (schema optimization)
Suy luận mô hình (Model inference) | 45% | 45 ms | Lượng tử hóa (Quantization), xử lý hàng loạt (batching), chưng cất mô hình (model distillation)
Hậu xử lý (Postprocessing) | 5% | 5 ms | Xử lý bất đồng bộ (Async processing), bộ nhớ đệm kết quả (result caching)
Tuần tự hóa phản hồi (Response serialization) | 5% | 5 ms | Định dạng hiệu quả (Protobuf, MessagePack)

Hiểu biết hệ thống (Systems insight): Việc tối ưu hóa mô hình đơn thuần thường chỉ nắm bắt được chưa tới 50 phần trăm cơ hội giảm
độ trễ. Một mô hình chạy nhanh hơn 2 lần làm giảm ví dụ này từ 100 ms xuống 77.5 ms, chỉ là sự
cải thiện đầu cuối 1.3 lần, bởi vì suy luận là 45 phần trăm của tổng độ trễ.
Tư duy hệ thống (Systems thinking) đòi hỏi sự phân tích từ đầu đến cuối (end-to-end analysis). Áp dụng phân loại D·A·M để chẩn đoán
nguyên nhân gốc rễ (root cause) trên Dữ liệu (chi phí trích xuất đặc trưng, chi phí tuần tự hóa), Thuật toán (quá nhiều

================ PAGE 837 ================

14. Vận hành ML (ML Operations)
799
Ngân sách năng lượng biên (Edge power budgets) trải dài trên các cảm biến,
các cổng kết nối (gateways), và các phương tiện giao thông trên
nhiều cấp độ lớn (orders of magnitude).

lớp, đồ thị chưa được tối ưu hóa), và Máy móc (Machine) (sự bão hòa băng thông bộ nhớ, điều tiết nhiệt độ (thermal throttling)).
Nguyên tắc của Dave Patterson được áp dụng: "Đo lường mọi thứ, tối ưu hóa điểm nghẽn." Nếu việc trích xuất
đặc trưng vượt quá ngân sách của nó, không có khối lượng tối ưu hóa mô hình nào sẽ đạt được SLO.
Vượt ra ngoài ngân sách độ trễ, việc vận hành (operationalizing) sự phục vụ đòi hỏi phải chọn lựa các kỹ thuật cơ sở hạ tầng
cho ràng buộc mà ngân sách bộc lộ. Bảng 14.15 tóm tắt các chiến lược tiêu biểu cho cơ sở hạ tầng ML-như-
một-dịch vụ (ML-as-a-service); câu hỏi tổ chức (organizing question) là liệu điểm nghẽn nằm ở độ trễ xếp hàng (queueing delay),
công suất (capacity), việc định tuyến (routing), chi phí điều phối (orchestration overhead), hay dự đoán độ trễ (latency prediction).

Bảng 14.15: Kỹ thuật Hệ thống Phục vụ (Serving System Techniques): Cơ sở hạ tầng phục vụ ML có thể mở rộng (Scalable ML-as-a-service infrastructure) dựa trên các kỹ thuật như lập lịch yêu cầu (request scheduling)
và lựa chọn phiên bản (instance selection) để tối ưu hóa việc sử dụng tài nguyên và giảm độ trễ dưới tải trọng cao (high load). Đối với lý thuyết hàng đợi (queuing theory) cơ bản
và các chiến lược tạo lô (batching strategies), hãy xem Chương 13.

Kỹ thuật (Technique) | Mô tả (Description) | Hệ thống ví dụ (Example System)
Lập lịch Yêu cầu & Tạo lô (Request Scheduling & Batching) | Nhóm các yêu cầu suy luận để cải thiện thông lượng (throughput) và giảm chi phí | Clipper (Crankshaw và cộng sự, 2017)
Lựa chọn Phiên bản & Định tuyến (Instance Selection & Routing) | Phân công động (Dynamically assigns) các yêu cầu tới các biến thể mô hình dựa trên các ràng buộc | INFaaS (Romero và cộng sự, 2021)
Tự động mở rộng Dự đoán (Predictive Autoscaling) | Thêm công suất trước những đợt tăng vọt nhu cầu để đáp ứng các SLO độ trễ | MArk (Zhang và cộng sự, 2019)
Tự động mở rộng (Autoscaling) | Điều chỉnh các phiên bản mô hình để phù hợp với các nhu cầu của khối lượng công việc (workload demands) | INFaaS
Điều phối Mô hình (Model Orchestration) | Phối hợp thực thi trên các thành phần mô hình hoặc các đường ống | AlpaServe (Li và cộng sự, 2023)
Dự đoán Thời gian Thực thi (Execution Time Prediction) | Dự báo độ trễ để tối ưu hóa việc lập lịch yêu cầu | Clockwork (Gujarati và cộng sự, 2020)

Các chiến lược này tạo thành nền tảng phục vụ trên đám mây (cloud-serving foundation). Triển khai ở biên (Edge deployment) giữ nguyên mục tiêu
hoạt động nhưng thay đổi các ràng buộc: việc quay lui (rollback), đo từ xa (telemetry), và kiểm soát cập nhật phải hoạt động trên các thiết bị với
sức mạnh, bộ nhớ và khả năng kết nối bị giới hạn.

14.5.1.4 Triển khai AI ở biên (Edge AI deployment)
Xem xét một máy dò khói với một mô hình ML để phân biệt khói nấu ăn với lửa. Khi
mô hình này suy giảm chất lượng, một kỹ sư không thể đơn giản là SSH vào thiết bị, quay lui về phiên bản trước đó,
và khởi động lại. Thiết bị đó nằm trên trần nhà của ai đó với Wi-Fi chập chờn, pin đồng xu (coin-cell battery), và
256 KB bộ nhớ. Mọi giả định hoạt động từ MLOps trên đám mây (quay lui tức thì, ghi nhật ký tập trung, giám sát thời gian thực) phải được hình dung lại.
AI ở biên (Edge AI) đại diện cho sự dịch chuyển này: suy luận học máy xảy ra tại hoặc gần nguồn dữ liệu thay
vì ở cơ sở hạ tầng đám mây tập trung (Reddi và cộng sự, 2019). Các khối lượng công việc đòi hỏi độ trễ thấp,
xử lý cục bộ bảo vệ quyền riêng tư, kết nối chập chờn, hoặc các ngân sách năng lượng chặt chẽ khiến các mẫu
triển khai ở biên (edge deployment patterns) trở thành kiến thức thiết yếu cho những người thực hành MLOps. Sự thay đổi này giới thiệu ba
danh mục liên quan với nhau của các thách thức hoạt động: giới hạn tài nguyên (resource constraints), phân cấp triển khai (deployment hierarchy), và
các cơ chế cập nhật (update mechanisms).
Giới hạn tài nguyên thống trị các quyết định triển khai ở biên. Các thiết bị biên đòi hỏi các kỹ thuật tối ưu hóa
mô hình tích cực được thiết lập trong Chương 10 (lượng tử hóa, cắt tỉa (pruning), chưng cất tri thức (knowledge distillation)) để đáp ứng các ranh giới bộ nhớ và năng lượng của các đợt triển khai lớp vi điều khiển (microcontroller-class deployments) (Warden và
Situnayake 2020; David và cộng sự, 2021). Ngân sách năng lượng trải dài trên bốn cấp độ lớn, từ vài miliwatt
cho các cảm biến IoT đến hàng chục watt trong các hệ thống ô tô, đòi hỏi việc lập lịch suy luận nhận biết năng lượng (power-aware inference scheduling)
và quản lý nhiệt độ (thermal management). Các ứng dụng quan trọng về an toàn (Safety-critical applications) áp đặt các mục tiêu thời gian xác định đòi hỏi
phân tích thời gian thực thi tình huống xấu nhất (worst-case execution time - WCET) dưới các điều kiện bất lợi bao gồm điều tiết nhiệt độ
và sự tranh chấp bộ nhớ (memory contention).
Những giới hạn này định hình một phân cấp triển khai tự nhiên trên ba tầng (tiers). Quá trình xử lý ở cấp độ cảm biến
xử lý việc lọc dữ liệu tức thời và trích xuất đặc trưng trên các thiết bị lớp vi điều khiển tiêu thụ
1–100 mW. Xử lý cổng biên (Edge gateway processing) thực hiện suy luận trung gian trên các bộ xử lý ứng dụng với
ngân sách điện 1–10 W. Sự phối hợp đám mây (Cloud coordination) quản lý việc phân phối mô hình, học tập tổng hợp (aggregated learning), và

================ PAGE 838 ================

800
14.5 Vận hành trên môi trường sản xuất (Production Operations)
suy luận phức tạp (complex reasoning) đòi hỏi các tài nguyên lớp GPU (GPU-class resources). Sự phân cấp này cho phép sự tối ưu hóa toàn hệ thống (system-wide optimization):
các thao tác tốn kém về mặt tính toán di chuyển lên trên trong khi các quyết định quan trọng về độ trễ (latency-critical) vẫn ở cục bộ.
Hai bối cảnh triển khai đáng chú ý cụ thể. TinyML nhắm mục tiêu vào suy luận dựa trên vi điều khiển dưới các giới hạn bộ nhớ chặt chẽ và
năng lượng lớp miliwatt, đòi hỏi các công cụ chuyên dụng như
TensorFlow Lite Micro và CMSIS-NN (David và cộng sự, 2021; Lai và cộng sự, 2018). Các kiến trúc mô hình
phải được đồng thiết kế (co-designed) với các giới hạn phần cứng, ưu tiên các toán tử nhỏ gọn (compact operators), lượng tử hóa, và
các chiến lược cắt tỉa mà mức độ quyết liệt của nó phụ thuộc vào thiết bị và mục tiêu độ chính xác. Mobile AI
mở rộng việc triển khai ở biên đến các điện thoại thông minh với mức độ tính toán vừa phải, sử dụng NPU và GPU compute
shaders để đáp ứng độ trễ tương tác (interactive latency) và các giới hạn về tuổi thọ pin thông qua việc lập lịch nhận biết năng lượng.
Các bản cập nhật và việc giám sát hoàn thiện bức tranh vận hành ở biên. Các bản cập nhật mô hình qua không gian (Over-the-air - OTA)
cho phép bảo trì các hệ thống không thể tiếp cận về mặt vật lý. Các đường ống OTA phải triển khai việc phân phối mô hình an toàn
với các chữ ký mật mã (cryptographic signatures) và cơ chế quay lui, sử dụng tính năng nén chênh lệch (differential compression)
để chỉ truyền đi các thay đổi tham số thay vì toàn bộ cấu phần mô hình. Việc lập lịch cập nhật phải
tính đến các mẫu kết nối của thiết bị, sự khả dụng về năng lượng, và tầm quan trọng của hoạt động (operational criticality).
Việc giám sát đòi hỏi sự thích ứng với các môi trường bị giới hạn tài nguyên: các hệ thống đo lường từ xa (telemetry) nhẹ
ghi lại các số liệu cần thiết (độ trễ suy luận, tiêu thụ năng lượng, các chỉ số độ chính xác) trong khi
giảm thiểu chi phí phát sinh. Việc giám sát sức khỏe theo dõi các điều kiện ở cấp độ thiết bị (trạng thái nhiệt độ, mức pin, 
chất lượng kết nối) để dự đoán các nhu cầu bảo trì. Các mô hình phối hợp biên-đám mây (Edge-cloud coordination patterns) cho phép
việc giảm tải thích ứng (adaptive offloading) giữa các tầng (tiers) dựa trên tải hiện tại, các điều kiện mạng, và các yêu cầu về
độ trễ. Việc bộ nhớ đệm đặc trưng tại các cổng biên (edge gateways) giúp giảm việc tính toán dư thừa, trong khi học liên kết (federated learning)
cho phép các thiết bị biên đóng góp vào việc cải thiện mô hình mà không cần truyền dữ liệu thô.
Sự suy giảm nhẹ nhàng (Graceful degradation) là mẫu thiết kế vận hành định hình cho AI ở biên. Khi các tài nguyên trở nên
bị hạn chế, các hệ thống phải duy trì chức năng cốt lõi bằng cách giảm bớt độ phức tạp của mô hình, tần suất suy luận,
hoặc tính hoàn chỉnh của đặc trưng. Triết lý thiết kế này phải được tích hợp (built in) ngay từ đầu, chứ không phải
được chắp vá như một suy nghĩ muộn màng.
Việc đưa các mô hình vào sản xuất chỉ là một nửa thách thức. Một mô hình được triển khai thành công có thể
bị suy giảm chất lượng qua sự trôi dạt (drift) hoặc các vấn đề về chất lượng dữ liệu mà không kích hoạt bất kỳ cảnh báo nào, chính xác là các chế độ lỗi tĩnh lặng (silent failure modes)
đã thúc đẩy toàn bộ chương này. Các thực hành giám sát, phản hồi sự cố (incident response), và trực ban (on-call practices)
tiếp sau đây sẽ đóng lại vòng lặp này.

14.5.2 Quản lý tài nguyên và giám sát (Resource management and monitoring)
Việc triển khai và phục vụ đưa các mô hình vào sản xuất. Việc giữ chúng hoạt động ổn định yêu cầu hai kỷ luật
bổ trợ cho nhau: quản lý tài nguyên (cung cấp và mở rộng quy mô điện toán, lưu trữ, và
mạng) và giám sát (quan sát hành vi hệ thống và phát hiện sự suy giảm chất lượng trước khi người dùng
nhận ra).

14.5.2.1 Quản lý cơ sở hạ tầng (Infrastructure management)
Một mô hình hoạt động trong môi trường staging (môi trường dàn dựng) nhưng thất bại ở production (môi trường sản xuất) bởi vì ai đó đã cấp phát thủ công (manually provisioned) một
loại GPU khác. Một công việc huấn luyện (training job) bị sập vì một thí nghiệm của đồng nghiệp đã tiêu thụ toàn bộ
bộ nhớ khả dụng. Một dịch vụ suy luận không thể mở rộng quy mô (cannot scale) bởi vì các hạn mức tài nguyên (resource quotas) của nó đã được đặt thông qua một
tin nhắn Slack cách đây sáu tháng. Những sự cố này chia sẻ một nguyên nhân cốt lõi (root cause): cơ sở hạ tầng được quản lý thông qua
các quy trình thủ công (manual processes) thay vì mã nguồn (code).
Cơ sở hạ tầng (Infrastructure) có thể mở rộng, linh hoạt là nền tảng cho việc vận hành hóa các hệ thống ML, và Cơ sở hạ tầng dưới dạng Mã nguồn (Infrastructure as Code - IaC) là thực hành làm cho nó trở nên đáng tin cậy. IaC xem cấu hình cơ sở hạ tầng như
phần mềm (được kiểm soát phiên bản, được xem xét, kiểm tra, và thực thi tự động) thay vì cấu hình
thủ công thông qua các giao diện đồ họa (graphical interfaces) hoặc công cụ dòng lệnh (command-line tools). Cách tiếp cận này mang lại tính kỷ luật của kỹ thuật
phần mềm cho việc quản lý tài nguyên: các thay đổi được theo dõi, các cấu hình có thể được kiểm tra
trước khi triển khai, và các môi trường có thể được tái tạo một cách đáng tin cậy.
Công cụ cơ sở hạ tầng cụ thể ít quan trọng hơn hợp đồng mà nó bắt buộc thi hành. Terraform (HashiCorp
2014), AWS CloudFormation (Amazon Web Services 2024e), và Ansible (Hatcher 2024) đại diện
cho các cách thức phổ biến để định nghĩa các phiên bản cơ sở hạ tầng song song với mã nguồn ứng dụng. Trong các thiết lập MLOps,
định nghĩa được phiên bản hóa đó là thứ cho phép một nhóm (team) tái tạo loại GPU, chính sách mạng, các quyền truy cập lưu trữ,
và các giới hạn mở rộng quy mô được sử dụng bởi một môi trường huấn luyện hoặc phục vụ trên AWS (Amazon
Web Services 2024c), Google Cloud Platform (Google Cloud 2024a), Microsoft Azure (Microsoft
2024a), hoặc cơ sở hạ tầng tại chỗ (on-premises infrastructure).

================ PAGE 839 ================

801
22
ML
Tự động mở rộng quy mô (Autoscaling):
Tự động mở rộng quy mô điều chỉnh sức chứa
dựa trên nhu cầu các tín hiệu
(Amazon
Web
Các dịch vụ
2024d),
nhưng
ML
(việc) phục vụ
thêm (vào)
các sự ép buộc
vắng mặt (absent)
từ không trạng thái web các dịch vụ.
Tự động mở rộng quy mô các quyết định phải
tính đến (cho) mô hình (việc) tải
thời gian
(lạnh-khởi động
chi phí),
GPU bộ nhớ sự phân mảnh,
và (việc) gộp lô hành vi ngoài
(việc) thêm (vào) CPU sự sử dụng.
(Việc) Mở rộng quy mô lên quá chậm vi phạm
độ trễ các SLO; (việc) mở rộng quy mô xuống
quá
quyết liệt
buộc
(được) lặp lại
lạnh
các sự khởi động
(thứ) mà
làm xuống cấp P99 độ trễ.
Cơ sở hạ tầng sự quản lý bao phủ (cái) đầy đủ ML vòng đời. Trong suốt (quá trình) đào tạo, IaC các kịch bản phân bổ
tính toán các cá thể với GPU hay TPU các bộ tăng tốc, cấu hình (được) phân tán lưu trữ, và triển khai vùng chứa (container)
các cụm. Bởi vì cơ sở hạ tầng các định nghĩa được lưu trữ như (là) mã, chúng có thể được kiểm toán, (được) tái sử dụng, và
(được) tích hợp vào CI/CD các đường ống (việc) đảm bảo sự nhất quán (xuyên) qua các môi trường.
Việc chứa trong vùng chứa (Containerization) cung cấp (cái) cùng khả năng tái tạo ranh giới cho thời gian chạy các sự phụ thuộc. Docker
(Merkel 2014) đóng gói (cái) mô hình, các thư viện, và phục vụ mã vào một (bị) cô lập đơn vị, trong khi sự điều phối
các hệ thống (chẳng) hạn như Kubernetes (Đám mây Bản địa Máy tính Quỹ (Foundation) 2024a) quản lý những các đơn vị đó
(xuyên) qua các cụm. (Cái) (thuộc về) hoạt động giá trị không phải (là) (cái) vùng chứa tên; nó là (cái) khả năng để triển khai (cái) cùng
đồ tạo tác (một cách) lặp đi lặp lại trong khi tài nguyên sự phân bổ, (việc) mở rộng quy mô, và sức khỏe sự quản lý duy trì (mang tính) rõ ràng.
Để xử lý các sự thay đổi trong khối lượng công việc cường độ, bao gồm các gai (spikes) trong suốt siêu tham số (việc) tinh chỉnh và
các sự dâng trào (surges) trong dự đoán lưu lượng truy cập, các đội dựa vào đám mây tính đàn hồi (elasticity) và tự động mở rộng quy mô22. Đám mây các nền tảng
hỗ trợ theo-yêu cầu (on-demand) (việc) cung cấp và (thuộc về) chiều ngang (việc) mở rộng quy mô của cơ sở hạ tầng các tài nguyên. Tự động mở rộng quy mô
các cơ chế (Amazon Web Các dịch vụ 2024d) (một cách) tự động điều chỉnh tính toán sức chứa dựa trên sự sử dụng
các số liệu, (việc) kích hoạt các đội để tối ưu hóa cho cả hiệu suất và chi phí-tính hiệu quả.
Cơ sở hạ tầng trong MLOps (thì) không (bị) giới hạn (tới) (cái) đám mây. Nhiều các sự triển khai bao phủ trên-cơ sở, đám mây,
và rìa các môi trường, phụ thuộc vào độ trễ, quyền riêng tư, hay (mang tính) quy định (regulatory) các sự ép buộc. Một mạnh mẽ cơ sở hạ-
tầng sự quản lý chiến lược phải chứa (accommodate) này sự đa dạng bằng (cách) (việc) cung cấp (có tính) linh hoạt sự triển khai
các mục tiêu và (có tính) nhất quán cấu hình sự quản lý (xuyên) qua các môi trường.
Để minh họa, xem xét một tình huống trong đó một đội sử dụng Terraform để cung cấp một GPU phục vụ
nút trên Google Đám mây Nền tảng. (Cái) nút lưu trữ một (được) chứa-trong-vùng-chứa TensorFlow mô hình (thứ) mà phục vụ
các dự đoán thông qua HTTP các API, và một tự động mở rộng quy mô nhóm thêm hay xóa (các) giống hệt các bản sao khi (as) yêu cầu
tải thay đổi. Trong khi đó, CI/CD các đường ống cập nhật (cái) mô hình vùng chứa dựa trên (việc) đào tạo lại các chu kỳ,
và việc giám sát các công cụ theo dõi độ trễ và tài nguyên sự sử dụng. Tất cả cơ sở hạ tầng các thành phần, (trải dài) từ
mạng cấu hình đến tính toán các hạn ngạch, được quản lý như (là) (được) lập phiên bản-kiểm soát mã, (việc) đảm bảo
khả năng tái tạo và tính có thể kiểm toán. Bằng (cách) (việc) áp dụng Cơ sở hạ tầng như (là) Mã, đám mây-bản địa sự điều phối,
và (được) tự động hóa (việc) mở rộng quy mô, MLOps các đội có thể cung cấp và duy trì các tài nguyên (được) yêu cầu cho máy
học tại sản xuất quy mô.
Cơ sở hạ tầng như (là) Mã giải quyết (cách) làm thế nào để cung cấp các tài nguyên; (cái) thử thách duy trì (việc) quyết định khi nào
và bao nhiêu. ML các khối lượng công việc thể hiện (về mặt) chất lượng khác nhau tài nguyên sự tiêu thụ các mẫu so với
không trạng thái web các ứng dụng: đào tạo các công việc (jobs) bùng nổ (burst) từ không (lên) (hàng) tá của các GPU (sau) đó quay trở lại (tới) tối thiểu
sự tiêu thụ, trong khi sự suy luận duy trì (có tính) ổn định sự sử dụng dưới (có thể) thay đổi lưu lượng truy cập. Đào tạo các khối lượng công việc
chứng minh (mang tính) bùng thực các yêu cầu (thứ) mà tạo ra sự căng thẳng giữa tài nguyên sự sử dụng tính hiệu quả và
thời gian-(đến)-sự thấu hiểu. Sự suy luận các khối lượng công việc hiện diện (có tính) ổn định hơn sự tiêu thụ các mẫu nhưng với nghiêm ngặt độ trễ
các yêu cầu dưới (có thể) thay đổi lưu lượng truy cập.
Phần cứng sự sử dụng các mẫu (Việc) Cung cấp các tài nguyên (thì) chỉ (là) (cái) đầu tiên (một) nửa của (cái) bài toán; (việc) sử dụng
chúng (một cách) hiệu quả có nghĩa là (việc) thiết lập sự sử dụng các mục tiêu (thứ) mà cân bằng chi phí (so) với tính đáng tin cậy, và những các mục tiêu đó
phụ thuộc vào (việc) đọc phần cứng các số liệu (một cách) chính xác thay vì (việc) lấy chúng tại mệnh giá (face value). (Việc) Hiểu
phần cứng sự sử dụng các mẫu là thiết yếu cho chi phí-hiệu quả ML các hoạt động. Không giống như (mang tính) truyền thống web
các dịch vụ nơi CPU sự sử dụng (một cách) trực tiếp có tương quan với thông lượng, ML sự suy luận thể hiện phức tạp
các mối quan hệ giữa phần cứng các số liệu và thực tế hiệu suất.
GPU sự sử dụng các số liệu có thể đánh lừa (mislead) các toán tử (operators). Một cao sự sử dụng (việc) đọc có thể (là) tính toán-
giới hạn (chủ động (đang) thực thi tensor các hoạt động, (cái) (mang tính) lý tưởng trường hợp), bộ nhớ-giới hạn ((đang) chờ dữ liệu
các (sự) chuyển giao từ GPU bộ nhớ), hay I/O-giới hạn ((bị) đình trệ (stalled) (đang) chờ cho đầu vào dữ liệu từ CPU hay mạng).
Bảng 14.16 phân biệt những các mẫu này và của chúng sự tối ưu hóa các chiến lược:
Bảng 14.16: GPU Sự sử dụng Các mẫu: Khác nhau sự sử dụng các chữ ký yêu cầu khác nhau các sự tối ưu hóa. Cao GPU sự sử dụng
với thấp bộ nhớ băng thông gợi ý tính toán-giới hạn các khối lượng công việc (thứ) mà hưởng lợi từ tính song song. Cao bộ nhớ băng thông với
(mức độ) vừa phải GPU sự sử dụng chỉ ra bộ nhớ-giới hạn các khối lượng công việc (đang) yêu cầu mô hình sự tối ưu hóa.
Mẫu
GPU Util
Bộ nhớ băng thông util.
Sự tối ưu hóa Chiến lược
Tính toán-giới hạn
>85%
<70%
Lớn hơn lô các quy mô, tensor tính song song bên trong nút
Bộ nhớ-giới hạn
50–85%
>85%
Giảm (thiểu) mô hình kích thước, lượng tử hóa, tối ưu hóa bộ nhớ truy cập
I/O-giới hạn
<50%
<50%
Cải thiện dữ liệu đường ống, tìm nạp trước (prefetch) các đầu vào, sử dụng các SSD
Lô-bị đói (starved)
(Có thể) Thay đổi ((mang tính) gai)
(Có thể) Thay đổi
(Mang tính) Động (việc) gộp lô, yêu cầu (việc) xếp hàng trên đơn máy chủ

802
14.5 Sản xuất Các hoạt động
Sự sử dụng các mục tiêu theo khối lượng công việc (Có tính) Đại diện sự sử dụng các mục tiêu thay đổi theo khối lượng công việc các đặc điểm,
(việc) phản ánh (cái) khác nhau độ trễ các sự chịu đựng (tolerances) và chi phí các tính nhạy cảm của mỗi (thuộc về) hoạt động chế độ:
• Lô (việc) đào tạo: Mục tiêu >80 phần trăm GPU sự sử dụng. Thấp hơn sự sử dụng chỉ ra dữ liệu đường ống
các nút thắt cổ chai hay (dưới) mức tối ưu (suboptimal) lô các quy mô. Giám sát gpu_util, memory_bandwidth_util, và
data_load_time.
• Trực tuyến sự suy luận: Mục tiêu 50–70 phần trăm GPU sự sử dụng tại P50 tải. Dự trữ (Reserve) khoảng không gian (headroom) (30–50
phần trăm) cho lưu lượng truy cập các gai. Cao hơn (được) duy trì sự sử dụng (gây) rủi ro độ trễ SLA các sự vi phạm trong suốt
các sự bùng nổ (bursts).
• Lô sự suy luận: Mục tiêu >85 phần trăm sự sử dụng. Không giống như trực tuyến (việc) phục vụ, lô các công việc có thể chịu đựng
việc xếp hàng các sự trì hoãn, (việc) kích hoạt tối đa phần cứng tính hiệu quả.
Sự sử dụng các mục tiêu là (mang tính) chẩn đoán (diagnostic) bắt đầu các điểm, không (phải) (mang tính) phổ quát (universal) các ngưỡng. (Cái) cùng sự sử dụng
số có thể chỉ ra một khác nút thắt cổ chai phụ thuộc vào (việc) liệu (cái) khối lượng công việc (có) là nhạy cảm-độ trễ
(việc) phục vụ, hướng-tới-thông lượng lô sự suy luận, hay (việc) đào tạo (hay không).
Bộ nhớ hệ thống phân cấp các hiệu ứng Mô hình phục vụ hiệu suất phụ thuộc (một cách) tới hạn vào bộ nhớ hệ thống phân cấp
sự sử dụng. Dữ liệu phải chảy qua nhiều bộ nhớ các cấp độ với vô cùng (vastly) khác nhau các băng thông
(phần D.3.3 lập bản đồ (cái) đầy đủ độ trễ hệ thống phân cấp (xuyên) qua (cái) lưu trữ phổ), như bảng 14.17 định lượng.
(Cái) (một cách) xấp xỉ 400-lần băng thông khoảng trống giữa L2 bộ nhớ cache và NVMe là (cái) (mang tính) ràng buộc sự ép buộc trên
nơi mỗi phục vụ đồ tạo tác phải sống: nóng các trọng số thuộc về (trong) L2 và (cái) đầy đủ mô hình trong HBM (một cách) chính xác
bởi vì chúng được chạm vào trên mỗi token, trong khi bất cứ thứ gì (mà) tràn (spills) (sang) NVMe trả một (sự) hoán đổi (swap) hình phạt
(thứ) mà thống trị sự suy luận độ trễ. Phần D.1 lập bảng (cái) hiện tại bộ tăng tốc các thông số kỹ thuật (specifications) và
HBM các băng thông (mà) những phục vụ các con số này dựa vào (draw on), vì vậy các giá trị bên dưới truy vết trở lại (tới) (được) lập tài liệu
mỗi-thế hệ bộ nhớ các số liệu thay vì (mang tính) minh họa các ước tính:
Bảng 14.17: GPU Bộ nhớ Hệ thống phân cấp và Băng thông: Mỗi cấp độ trong (cái) bộ nhớ hệ thống phân cấp đánh đổi sức chứa cho tốc độ. Hiệu quả
mô hình (việc) phục vụ yêu cầu (việc) giữ nóng các trọng số trong L2 bộ nhớ cache và đầy đủ mô hình các tham số trong HBM, trong khi (được) gộp lô các đầu vào xếp hàng trong
hệ thống RAM. Khi mô hình kích thước vượt quá GPU bộ nhớ, NVMe (sự) hoán đổi giới thiệu các bậc-của-cường độ độ trễ các hình phạt (thứ) mà
thống trị sự suy luận thời gian.
Bộ nhớ Cấp độ
Băng thông
Điển hình Các nội dung
L2 Bộ nhớ cache (40 MB trên A100)
~3 TB/s
Nóng các trọng số
HBM2e GPU Bộ nhớ (80 GB)
~2 TB/s
Mô hình
PCIe Gen4 x16 tới CPU
~32 GB/s
Các sự kích hoạt
Hệ thống RAM (512 GB)
~200 GB/s
(Được) Gộp lô các đầu vào
NVMe SSD
~7 GB/s
Mô hình (sự) hoán đổi
Cho lớn ngôn ngữ mô hình (LLM) (việc) phục vụ trên một đơn GPU hay máy chủ, (cái) KV-cache ((đang) lưu trữ sự chú ý
các khóa và các giá trị cho mỗi token) thường trở thành (cái) bộ nhớ nút thắt cổ chai; vLLM’s PagedAttention
thiết kế đã được thúc đẩy bởi này phục vụ áp lực (Kwon và cộng sự. 2023). Cho một Llama 2 70-tỷ-tham số-
kiểu nhóm-truy vấn sự chú ý mô hình (Touvron, Martin, và cộng sự. 2023) với 80 các lớp, 8 KV các đầu (heads), một 4,096-
token ngữ cảnh, và FP16 bộ nhớ cache các mục (entries), mỗi chủ động chuỗi lưu trữ khoảng 1.3 GB của KV cache. Tám
đồng thời các chuỗi do đó tiêu thụ khoảng 10.7 GB trước (khi) bộ lên lịch khoảng không gian, sự phân mảnh,
hay các sự kích hoạt, (việc) giới hạn bao nhiêu các yêu cầu một đơn nút có thể gộp lô (lại) với nhau. (Việc) Giám sát KV-cache
sự sử dụng trên mỗi phục vụ nút kích hoạt sức chứa (việc) lập kế hoạch: khi KV-cache tiếp cận GPU
bộ nhớ các giới hạn, bổ sung các yêu cầu xếp hàng thay vì gộp lô, (việc) làm xuống cấp độ trễ.
Chi phí-mỗi-sự suy luận việc theo dõi Biên dịch phần cứng các số liệu thành (có) liên quan-tới-kinh doanh chi phí-mỗi-sự suy luận
các số liệu (đang) sử dụng phương trình 14.10:
Chi phí mỗi 1K các sự suy luận = Hàng giờ GPU chi phí×1000
Các sự suy luận mỗi giờ
(14.10)
Cho một $3/giờ A100 cá thể (đang) xử lý 50,000 các sự suy luận/giờ, chi phí là $0.06/1K các sự suy luận. Theo dõi
này số liệu (xuyên) qua thời gian; các sự gia tăng chỉ ra tính hiệu quả sự xuống cấp (đang) yêu cầu sự điều tra.

803
23
Khả năng quan sát (từ (sự) kiểm-
soát lý thuyết (Kalman 1960)):
Đo lường (cách) tốt như thế nào một hệ thống’s
bên trong các trạng thái có thể được suy luận
từ (những) của nó bên ngoài các đầu ra. Trong
MLOps, việc giám sát trả lời
“là (cái) hệ thống (bị) hỏng (broken)?” (cao
lỗi tỷ lệ) trong khi khả năng quan sát
trả lời “tại sao nó hỏng?”
bằng (cách) (việc) kích hoạt sự suy luận của bên trong
trạng thái (đặc trưng các sự phân phối,
dự đoán sự tự tin, (thuộc về) thần-
kinh (neu-ron) các sự kích hoạt) từ các đầu ra
đơn độc.
(Mà) Không (có) khả năng quan-
sát (observabil-ity), một (đang) trôi dạt mô hình sản xuất
(cái) cùng (mang tính) chẩn đoán tín hiệu như
một khỏe mạnh (cái): xanh lá cây các bảng điều-
khiển (dash-boards) và (được) thỏa mãn các SLO.
Sự trôi dạt sự phát hiện tốc độ (thì) (bị) giới hạn
bởi (cái) mẫu tỷ lệ.
24
Sự trôi dạt Sự phát hiện (Sự) Trễ (Lag): Đặc-
trưng sự trôi dạt (hiệp biến (sự) dịch chuyển trên
𝑝(𝑥)) là (có thể) phát hiện (được) (một cách) ngay lập
tức từ đầu vào các sự phân phối,
với không (có) các nhãn (được) cần. Khái-
niệm sự trôi dạt (𝑝(𝑦∣𝑥) (đang) thay đổi)
(thì) (là) vô hình cho đến khi sự thật cơ sở (ground truth)
đến, thứ (mà) trong cao-rủi ro (stakes)
các miền (miền (y tế) chẩn đoán,
sự gian lận sự phát hiện, (thuộc về) pháp lý các quyết-
định) có thể mất (các) ngày, (các) tuần,
hay (các) tháng. Này sự bất đối xứng
có nghĩa là (cái) nguy hiểm nhất
sự trôi dạt (cũng) là (cái) chậm nhất để phát-
hiện, (đang) yêu cầu người đại diện (proxy) các số liệu
(dự đoán sự tự tin các sự phân-
phối, đầu ra entropy) như (là)
không hoàn hảo sớm (sự) cảnh báo các hệ-
thống (thứ) mà đánh đổi (trade) báo động giả
tỷ lệ cho sự phát hiện tốc độ.
25
COVID-19 ML Tác động:
COVID-kỷ nguyên hành vi các sự thay đổi
cung cấp một (mang tính) kinh điển ví dụ
về
đột ngột
khái niệm
sự trôi dạt:
nhu cầu các mẫu và người dùng
hành vi (đã) dịch chuyển nhanh hơn
bất kỳ
(sự) đào tạo lại
đường ống
(nào) có thể
phản hồi.
Nhiều
sự gợi ý và (việc) định giá
các hệ thống (đã) yêu cầu (thuộc về) khẩn cấp
thủ công sự can thiệp bởi vì
(những) (được) lên lịch
(sự) đào tạo lại
các nhịp điệu (cadences) (của) chúng (đã) giả định (mang tính) dần dần
sự trôi dạt,
không (phải)
(mang tính) rời rạc (discontinuous)
sự phân phối các sự dịch chuyển, (việc) phơi bày một
khoảng trống trong nhận thức-chi phí tự động hóa
(việc) lập kế hoạch.
14.5.2.2 Mô hình và cơ sở hạ tầng việc giám sát
Cơ sở hạ tầng sự quản lý cung cấp các tài nguyên; việc giám sát quan sát (những) của chúng hành vi. Này sự phân-
biệt (dis-tinction) quan trọng bởi vì (cái) sự xác minh khoảng trống có nghĩa là ML các hệ thống không thể (được) chứng minh (là) đúng thông qua
đơn vị các bài kiểm tra—chúng chỉ có thể (được) (bị) giới hạn (về mặt) thống kê. Việc giám sát triển khai (có thể) quan sát (được) sự xuống cấp
(phần 14.2.1), (việc) biến đổi này (thuộc về) lý thuyết sự hạn chế thành (thuộc về) hoạt động thực hành. Một khi việc giám sát
nổi lên (surfaces) một triệu chứng—một độ trễ SLA (sự) lỡ (miss), thông lượng bên dưới mục tiêu, hay bộ nhớ (sự) leo lên (creep)—phần A.5.1
lập bản đồ đó triệu chứng (tới) của nó (mang tính) thống trị D·A·M thuật ngữ và nói (với) (cái) người vận hành (những) sự tối ưu hóa nào sẽ
di chuyển (cái) (mang tính) ràng buộc sự ép buộc và (những) (cái) nào sẽ (bị) lãng phí trên (việc) phục vụ cơ sở hạ tầng. (Mà) Không (có) (mang tính) liên tục
việc giám sát, và (cái) sâu hơn khả năng quan sát23 (mà) nó kích hoạt, một (được) triển khai mô hình là một đen hộp (một cách) chậm chạp (đang) trôi dạt
hướng tới tính không liên quan (irrelevance).
Hiệu quả việc giám sát bao phủ cả mô hình hành vi và cơ sở hạ tầng hiệu suất. Trên (cái) mô hình
(cái) mặt (side), các đội theo dõi các số liệu (chẳng) hạn như độ chính xác (accuracy), độ chụm (precision), độ thu hồi (recall), và (cái) sự nhầm lẫn ma trận (scikit-learn
các nhà phát triển 2024b) (đang) sử dụng trực tiếp hay (được) lấy mẫu các dự đoán để phát hiện liệu hiệu suất duy trì (có tính) ổn định (hay không)
hay bắt đầu (để) trôi dạt. Một tới hạn sự ép buộc là (cái) sự trôi dạt sự phát hiện sự trì hoãn, thứ (mà) quyết định (cách) nhanh như thế nào
(thuộc về) thống kê việc giám sát có thể xác nhận rằng sự xuống cấp đã xảy ra. (Cái) tốc độ của sự phát hiện phụ thuộc vào
lưu lượng truy cập khối lượng. Một ngắn mẫu-tỷ lệ sự tính toán làm (cho) đó sự ép buộc (có thể) nhìn thấy (được).
(Cái) mẫu-tỷ lệ sự tính toán bên dưới phơi bày một (mang tính) cơ bản sự bất đối xứng: (thuộc về) thống kê các bài kiểm tra yêu cầu
đủ (được) dán nhãn các mẫu để đạt được sức mạnh (power), và thấp-lưu lượng truy cập các hệ thống có thể chờ (các) ngày hay (các) tuần trước khi
(việc) tích lũy đủ chứng cứ. Này độ trễ khoảng trống không phải (là) một kỹ thuật lối tắt (shortcut) (thứ) mà tốt hơn bộ công cụ (tooling)
có thể đóng (lại); nó là một hệ quả (consequence) của hữu hạn mẫu các tỷ lệ (đang) va chạm với (cái) (thuộc về) thống kê sức mạnh các yêu cầu
của (sự) giả thuyết việc kiểm thử. (Cái) (mang tính) thực tiễn hàm ý (implication) là (rằng) việc giám sát các hệ thống phải phân biệt giữa
sự trôi dạt (thứ) mà làm thay đổi (cái) đầu vào sự phân phối ((có thể) phát hiện (được) (mà) không (có) các nhãn) và sự trôi dạt (thứ) mà thay đổi (cái) quyết định
ranh giới chính nó ((có thể) phát hiện (được) chỉ sau (khi) sự thật cơ sở đến).
Giấy ăn (Napkin) Toán 14.4: (Cái) sự trôi dạt sự phát hiện sự trì hoãn
Bài toán: Một mô hình có 95 phần trăm đường cơ sở độ chính xác. (Cái) mục tiêu là để phát hiện một 5 phần trăm-điểm (point)
sự sụt giảm (drop) (xuống 90 phần trăm) với 95 phần trăm (thuộc về) thống kê sự tự tin. (Cái) hệ thống xử lý 1 QPS. (Bao) Lâu
(sẽ) (nó) mất để “chứng minh” (cái) mô hình đã trôi dạt?
Toán:
1. (Được) Yêu cầu các mẫu: Để phân biệt 95 phần trăm khỏi 90 phần trăm với cao sự tự tin,
sự phát hiện yêu cầu ≈1,000 (được) dán nhãn các mẫu.
2. Sự phát hiện độ trễ: 1,000 các mẫu / 1 QPS = 1,000 (các) giây ≈16.7 phút.
3. Thấp-lưu lượng truy cập trường hợp: Nếu (cái) mô hình chỉ xử lý 100 các yêu cầu/ngày, (việc) phát hiện (cái) cùng 5
phần trăm-điểm sự trôi dạt mất 10 ngày.
Các hệ thống sự thấu hiểu: (Cái) mẫu tỷ lệ của việc giám sát (thì) (bị) (về mặt) vật lý (bị) giới hạn bởi lưu lượng truy cập khối lượng. Cho
thấp-lưu lượng truy cập, cao-rủi ro (stakes) các mô hình (giống như (miền) y tế chẩn đoán), sự trôi dạt sự phát hiện có thể mất (các) ngày hay (các) tuần,
(việc) để lại (cái) hệ thống trong một dài-hạn (term) im lặng-sự thất bại trạng thái. Đây là (lý do) tại sao cao-rủi ro các hệ thống phải
bổ sung (thuộc về) thống kê việc giám sát với (mang tính) chủ động mô hình các cuộc kiểm toán (audits).
Sản xuất ML các hệ thống đối mặt (với) hai khác biệt (các) hình thức của mô hình sự trôi dạt24 (thứ) mà việc giám sát phải phân biệt.
Khái niệm sự trôi dạt25 xảy ra khi (cái) làm nền tảng (underlying) mối quan hệ giữa các đặc trưng và các mục tiêu tiến hóa: (cái)
hàm 𝑝(𝑦∣𝑥) thay đổi ngay cả mặc dù (cái) các đầu vào trông tương tự. Trong suốt (cái) COVID-19 đại dịch (pandemic),
cho ví dụ, (việc) mua hàng hành vi (đã) dịch chuyển (một cách) đáng kể (dramatically), (việc) làm mất hiệu lực (invalidating) nhiều (trước) đó (đã) chính xác
sự gợi ý các mô hình. Dữ liệu sự trôi dạt26, bằng sự tương phản (contrast), đề cập đến các sự dịch chuyển trong (cái) đầu vào sự phân phối 𝑝(𝑥) chính nó.
Trong các ứng dụng (chẳng) hạn như tự-lái ô tô, điều này có thể (là) kết quả từ (thuộc về) mùa vụ (seasonal) các sự thay đổi trong thời tiết, (sự) chiếu sáng (lighting),
hay đường sá các điều kiện, tất cả (những thứ) của (nào) làm thay đổi (cái) mô hình’s các đầu vào (mà) không (có) (việc) thay đổi (các) làm nền tảng (các) vật lý (physics) của
(việc) lái xe.
Cả hai (các) hình thức của sự trôi dạt thúc đẩy một (mang tính) hình thức định nghĩa:

804
14.5 Sản xuất Các hoạt động
26
Hiệp biến (Covariate) Sự dịch chuyển:
Shi-
modaira’s (sự) quan trọng việc đánh trọng số (weight-
ing) (sự) điều chỉnh (2000) giả định
(cái) sự hỗ trợ (support) của (cái) (việc) đào tạo
sự phân phối bao phủ (cái) sự triển-
khai sự phân phối:
mọi (ev-ery) sự triển khai đầu vào (đã) có thể
đã xuất hiện trong (việc) đào tạo,
chỉ với khác xác suất.
Khi sự triển khai chứa
(một cách) thực sự ngoài-phân-phối
các đầu vào (mới sản phẩm các danh-
mục, mới nhân khẩu học (demographics),
(mang tính) đối kháng (adversarial) các đầu vào), (cái) sự điều-
chỉnh thất bại (một cách) hoàn toàn và (cái)
mô hình sản xuất (một cách) tự tin
sai các đầu ra với không (có) (sự) cảnh-
báo tín hiệu, (việc) làm (cho) sự hỗ trợ
sự bao phủ (coverage) (thành) (cái) (bị) ẩn giả-
định (thứ) mà quyết định liệu
sự trôi dạt sự điều chỉnh hay đầy đủ sự đào tạo lại (retrain-ing) (có) được yêu cầu (hay không).
Định nghĩa 14.3: Dữ liệu sự trôi dạt
Dữ liệu sự trôi dạt là (cái) cụ thể kiểu phụ (subtype) của sự phân phối sự dịch chuyển trong đó (cái) đầu vào sự phân phối 𝑝(𝑥)
thay đổi trong khi (cái) quyết định ranh giới 𝑝(𝑦∣𝑥) duy trì (có tính) ổn định. (Cái) rộng hơn sự trôi dạt hệ thống phân loại từ
phần 4.5.3 cũng bao gồm khái niệm sự trôi dạt, trong đó 𝑝(𝑦∣𝑥) chính nó dịch chuyển.
1. Ý nghĩa (Significance): Nó đại diện (cho) một sự vi phạm của (cái) i.i.d. giả định ((mang tính) độc lập và (một cách) giống-
hệt (được) phân phối), (việc) gây ra độ chính xác (để) xói mòn (erode) (một cách) đơn điệu (monotonically) với (cái) (thuộc về) sự phân phối
sự phân kỳ (divergence) (𝒟(𝑃𝑡‖𝑃0)), (về mặt) thực nghiệm (được) mô hình hóa như (là) Độ chính xác(𝑡) ≈Độ chính xác0 −𝜆⋅𝒟(𝑃𝑡‖𝑃0)
với 𝜆 (được) khớp (fit) cho mỗi sự triển khai. Bởi vì 𝑝(𝑦∣𝑥) (thì) không thay đổi, (việc) đào tạo lại trên tươi mới 𝑝(𝑥) dữ liệu
có thể phục hồi hiệu suất (khi (cái) mới đầu vào sự phân phối chồng lấn (overlaps) (cái) nguyên bản sự hỗ trợ),
không giống như khái niệm sự trôi dạt, nơi (cái) nhãn mối quan hệ cũng phải được học-lại.
2. Sự phân biệt (Distinction): Không giống như mô hình sự phân rã (decay) (thứ (mà) hàm ý bên trong sự thất bại, nơi (cái) thuật toán hay
mã (đã) xuống cấp), dữ liệu sự trôi dạt là một bên ngoài lực (thị trường các sự dịch chuyển, cảm biến (sự) lão hóa (aging), người dùng hành vi
sự thay đổi) (thứ) mà làm mất hiệu lực (cái) mô hình’s (đã) được học sự ánh xạ (mà) không (có) bất kỳ kỹ thuật lỗi (nào).
3. Phổ biến cạm bẫy (pitfall): Một thường xuyên sự quan niệm sai lầm (misconception) là (rằng) sự trôi dạt là (có thể) phát hiện (được) bằng (cách) (việc) giám sát
mô hình các đầu ra. Vào (cái) lúc đầu ra sự trôi dạt (có thể) nhìn thấy (được), (cái) hệ thống (đã) thường (đã) (đang) phục vụ
(bị) xuống cấp các dự đoán trong (các) tuần. (Việc) Giám sát đầu vào đặc trưng các số liệu thống kê (𝒟(𝑃𝑡‖𝑃0)
thông qua PSI hay KL sự phân kỳ) cung cấp sớm hơn (sự) cảnh báo bởi vì đầu vào sự dịch chuyển đi trước (precedes) đầu ra
sự dịch chuyển bởi (cái) độ dài của (cái) sự thật cơ sở phản hồi vòng lặp.
Bởi vì (của) sự trôi dạt, một (được) triển khai mô hình cư xử (behaves) ít (giống) như phần mềm (thứ (mà) không hỏng trừ khi (được) thay đổi)
và nhiều (giống) như hàng tồn kho (inventory) (thứ (mà) phân rã qua thời gian). Đây là (cái) (thuộc về) thống kê sự trôi dạt bất biến (invariant) (đang) hoạt động: (cái)
sự xuống cấp phương trình (Độ chính xác(𝑡) ≈Độ chính xác0 −𝜆⋅𝒟(𝑃𝑡‖𝑃0)) dự đoán rằng độ chính xác xói mòn trong
tỷ lệ với (cái) (thuộc về) sự phân phối sự phân kỳ 𝒟(𝑃𝑡‖𝑃0), bất kể (của) mã chất lượng. Mọi việc giám sát
chiến lược trong chương này tồn tại để phát hiện này sự phân kỳ trước khi nó kết hợp (compounds) thành kinh doanh tác động.
(Cái) Đang thối rữa (Rotting) Tài sản (Asset) Đường cong biểu đồ (hình 14.8) đưa (puts) này entropy vào góc nhìn bằng (cách) (việc) đối chiếu (contrasting) hai
bảo trì các chiến lược. (Cái) màu cam răng cưa (sawtooth) mẫu đại diện (cho) (được) lên lịch (sự) đào tạo lại: độ chính xác
thiết lập lại tại một cố định khoảng (thời gian), liệu (cái) mô hình (có) vẫn khỏe mạnh hay (đã) rơi (xuống) bên dưới (cái) sự trôi dạt
ngưỡng (hay không). Này cách tiếp cận (thì) đơn giản nhưng có thể (là) cả lãng phí và trễ bởi vì (cái) lịch, không (phải) (sự) được quan-
sát sự xuống cấp, thúc đẩy (cái) bản cập nhật. (Cái) màu xanh lá cây đường (line) đại diện (cho) dựa trên-trình kích hoạt (trigger-based) (việc) đào tạo lại: độ chính xác
được (một cách) liên tục (được) giám sát, và (việc) đào tạo lại kích hoạt (fires) khi sự trôi dạt sự phát hiện báo hiệu rằng (cái) ngưỡng đã
bị vượt qua. (Cái) sự phân rã tỷ lệ và các khoảng (thời gian) là (mang tính) minh họa, nhưng (cái) (thuộc về) chất lượng hành vi (thì) mạnh mẽ.
0
50
100
150
200
250
300
350
Các ngày Kể từ Sự triển khai
0.750
0.775
0.800
0.825
0.850
0.875
0.900
0.925
0.950
Mô hình Độ chính xác
Sự trôi dạt Ngưỡng
(Được) Lên lịch Sự đào tạo lại
Dựa trên-trình kích hoạt Sự đào tạo lại
Hình 14.8: (Cái) Đang thối rữa Tài sản Đường cong: Mô hình độ chính xác so với (vs.) thời gian (các ngày) (đang) cho thấy (cái) tác động của (thuộc về) thống kê sự trôi dạt. Không giống như (mang tính) truyền thống
phần mềm (thứ) mà duy trì (có tính) tĩnh (static) trừ khi (được) sửa đổi, ML các mô hình phân rã khi (cái) thế giới thay đổi. (Mang tính) Định kỳ (sự) đào tạo lại (răng cưa) và
(được) kích hoạt (sự) đào tạo lại (xanh lá cây) là (những) (cái) chính các sự phản hồi để ngăn chặn im lặng sự thất bại. Sự phân rã các tỷ lệ và (sự) đào tạo lại các khoảng (thời gian) là
(mang tính) minh họa.

805
27
Prometheus:
Của nó
dựa trên-kéo (pull-based) mô hình, nơi một
trung tâm máy chủ cạo (scrapes) các số liệu
từ mục tiêu các hệ thống, là (những) gì
kích hoạt
(cái)
(được) tổng hợp
(thuộc về) hoạt động bảng điều khiển góc nhìn
(được) mô tả. Cho (cái) nhận thức-
nhiệt (sự) lên lịch (được) đề cập,
(cái) tới hạn sự đánh đổi là số liệu
tính hạt (granularity);
(việc) giám sát
mỗi-bộ tăng tốc
các (thông số) nhiệt
cho phép
(có tính) chính xác
khối lượng công việc
(việc) định tuyến nhưng tại cao dữ liệu chi phí,
trong khi
rẻ hơn
cấp độ-máy chủ
các (tập hợp) tổng hợp
có thể
che giấu
(cái)
cấp độ-thành phần
(sự) chèn ép (throttling)
(thứ) mà vi phạm độ trễ các SLO.
Một điển hình cạo (scrape) khoảng của
15–60 (các) giây ra lệnh (dictates) (cái)
hệ thống’s phản ứng thời gian đối với một
(thuộc về) nhiệt sự kiện (event).
(Cái) hai (các) đường cong biến sự trôi dạt từ một (mang tính) trừu tượng (thuộc về) thống kê bài toán thành một (các) hoạt động chính sách (sự) lựa chọn.
(Được) Lên lịch (sự) đào tạo lại (thì) dễ để lập kế hoạch nhưng có thể đào tạo lại quá sớm hay quá trễ; dựa trên-trình kích hoạt (sự) đào tạo lại
yêu cầu mạnh hơn từ xa (telemetry) nhưng căn chỉnh (aligns) sự can thiệp với (sự) được quan sát sự xuống cấp.
14.5.3 (Được) Phân lớp việc giám sát và sự trôi dạt sự định lượng (quantification)
(Cái) (thuộc về) thống kê sự trôi dạt bất biến (được) thiết lập trước đó nói (với) chúng ta rằng độ chính xác phân rã trong tỷ lệ với (thuộc về) sự phân-
phối sự phân kỳ. (Việc) Định lượng đó sự phân rã yêu cầu hai (các) lớp của từ xa: cơ sở hạ tầng các số liệu
(thứ) mà tiết lộ liệu (cái) phục vụ hệ thống chính nó (có) là (cái) nút thắt cổ chai (hay không), và sự phân phối các số liệu (chẳng) hạn như PSI
(thứ) mà tiết lộ liệu (cái) dữ liệu (đã) di chuyển (hay không). (Mang tính) Dần dần dài-hạn sự xuống cấp là (một cách) đặc biệt (mang tính) quỷ quyệt (insidious)
bởi vì nó có thể lảng tránh (evade) thô (coarse) sự phát hiện các ngưỡng: nhỏ (từ) ngày-sang-ngày các sự thay đổi trong một chất lượng số liệu có thể
kết hợp (compound) thành (về mặt) vật chất sự xuống cấp qua một năm (mà) không (có) (việc) vấp phải (tripping) (hàng) tháng các cảnh báo. (Thuộc về) Mùa vụ các mẫu
làm phức tạp (compound) này độ phức tạp. Một mô hình (được) đào tạo vào (mùa) hè có thể hoạt động tốt (xuyên) qua (mùa) thu nhưng thất bại
trong (mùa) đông các điều kiện (mà) nó (chưa) bao giờ quan sát (thấy). (Việc) Phát hiện (sự) như vậy (mang tính) dần dần sự xuống cấp yêu cầu đa-thang thời gian
việc giám sát: hiệu suất các đường cơ sở (xuyên) qua nhiều thời gian các chân trời (horizons) ((hàng) ngày, (hàng) tuần, (hàng) quý), (đang) trượt (sliding)
cửa sổ các sự so sánh (thứ) mà phát hiện chậm các xu hướng, và (thuộc về) mùa vụ hiệu suất các hồ sơ (profiles) (thứ) mà tính đến (cho)
(mang tính) chu kỳ (cyclical) các mẫu.
(Cái) đầu tiên lớp là cấp độ-cơ sở hạ tầng việc giám sát, thứ (mà) theo dõi các chỉ báo (chẳng) hạn như CPU và GPU
sự sử dụng, bộ nhớ và đĩa sự tiêu thụ, mạng độ trễ, và dịch vụ tính có sẵn. Thô sự sử dụng
đơn độc (thì) (một cách) dối trá (deceptively) không cung cấp thông tin (uninformative): như bảng 14.16 (đã) cho thấy, giống hệt 90 phần trăm GPU-sự sử dụng
các (việc) đọc có thể chỉ ra tính toán-giới hạn, bộ nhớ-giới hạn, hay I/O-giới hạn hành vi, vì vậy một sản xuất
bảng điều khiển phải tương quan GPU sự sử dụng với bộ nhớ-băng thông sự sử dụng để tách biệt (có tính) hiệu quả
tensor sự tính toán khỏi một dữ liệu-chuyển động (sự) đình trệ. Nguồn điện-tính hiệu quả các số liệu (cho ví dụ, các sự suy luận
mỗi joule hay FLOP/s/W, phụ thuộc vào khối lượng công việc) thêm (vào) một (được) chuẩn hóa-chi phí góc nhìn (thứ) mà kích hoạt hỗn hợp-
khối lượng công việc việc lên lịch cho cả (thuộc về) kinh tế và (thuộc về) môi trường tác động.
Các hệ thống Góc nhìn 14.2: Sắt (Iron) định luật trong sản xuất việc giám sát
Những sự sử dụng các mẫu này lập bản đồ (một cách) trực tiếp (tới) (cái) sắt định luật của ML các hệ thống (phần 1.7). Việc giám sát
tiết lộ (cái) nào thuật ngữ thống trị:
• Tính toán-giới hạn (cao GPU sự sử dụng, thấp bộ nhớ băng thông sự sử dụng): (Bị) Giới hạn bởi
𝑂/(𝑅peak ⋅𝜂hw). Tối ưu hóa các hạt nhân, sử dụng Tensor Các lõi (Cores), hay nâng cấp phần cứng.
• Bộ nhớ-giới hạn ((mức độ) vừa phải GPU sự sử dụng, cao bộ nhớ băng thông sự sử dụng): (Bị) Giới-
hạn bởi 𝐷vol/BW. Tối ưu hóa với sự lượng tử hóa, (việc) cắt tỉa, hay (việc) gộp lô.
• I/O-giới hạn (thấp GPU sự sử dụng, thấp bộ nhớ băng thông sự sử dụng): (Bị) Giới hạn bởi dữ liệu
đường ống độ trễ. Sửa (cái) DataLoader, không (phải) (cái) mô hình.
(Cái) sắt định luật tăng gấp đôi (doubles) như một (mang tính) chẩn đoán khuôn khổ cho sản xuất các hệ thống. Khi độ trễ các SLA (bị)
vi phạm, (cái) việc giám sát bảng điều khiển chỉ ra (cái) nào thuật ngữ để điều tra.
(Thuộc về) Nhiệt việc giám sát tích hợp vào (thuộc về) hoạt động việc lên lịch các quyết định, (một cách) đặc biệt cho (được) duy trì
cao-sự sử dụng các sự triển khai nơi (thuộc về) nhiệt (sự) chèn ép có thể làm xuống cấp hiệu suất (một cách) không thể dự đoán.
Hiện đại MLOps việc giám sát các bảng điều khiển kết hợp (thuộc về) nhiệt khoảng không gian các số liệu (thứ) mà hướng dẫn khối-
lượng công việc sự phân phối (xuyên) qua (có) sẵn phần cứng, (việc) ngăn chặn (bị) gây ra (bởi)-nhiệt hiệu suất sự xuống cấp
(thứ) mà có thể vi phạm sự suy luận độ trễ các SLA. Các công cụ (chẳng) hạn như Prometheus27 (Đám mây Bản địa Máy tính
Quỹ 2024b), Grafana (Labs 2024), và Elastic (Elastic NV 2024) được (một cách) rộng rãi sử dụng để thu thập,
tổng hợp, và trực quan hóa những (thuộc về) hoạt động các số liệu này. Những các công cụ này thường tích hợp vào các bảng điều khiển (thứ) mà
cung cấp thời gian-thực và (thuộc về) lịch sử các góc nhìn của hệ thống hành vi.
(Việc) Thu thập tất cả của những các tín hiệu này tại sản xuất quy mô giới thiệu của riêng nó chi phí các sự ép buộc. Những
các sự ép buộc (đó) buộc kỹ thuật các đội phải thực hiện (có) chủ ý (deliberate) các sự đánh đổi giữa việc giám sát tính hạt
và cơ sở hạ tầng (sự) chi tiêu.

806
14.5 Sản xuất Các hoạt động
Giấy ăn Toán 14.5: (Cái) tính kinh tế (economics) của khả năng quan sát
Sự đánh đổi: “Đo lường mọi thứ” là (về mặt) vật lý không thể tại quy mô. Phương trình 14.11 cho thấy rằng
khả năng quan sát chi phí mở rộng quy mô (một cách) tuyến tính với (việc) lấy mẫu tần suất và số liệu tính bản số (cardinality):
Chi phí ≈Tần suất×Các số liệu×((Việc) Hấp thụ Chi phí+Lưu trữ Chi phí)
(14.11)
Tần suất được đo bằng các mẫu mỗi đơn vị thời gian, Các số liệu là (cái) (sự) đếm của (được) phát ra số liệu các chuỗi
sau (khi) các nhãn và tính bản số sự mở rộng, và (cái) chi phí các thuật ngữ là đơn vị các mức giá mỗi (được) hấp thụ hay (được) giữ lại
dữ liệu điểm. (Cái) sản phẩm là một (đang) hoạt động chi phí tỷ lệ, không (phải) một một-lần thiết lập chi phí.
Cả hai dữ liệu các khối lượng (đi) theo từ (cái) cùng hai-bước số học. Tại đầy đủ tính trung thực (fidelity) (1 s việc lấy mẫu),
mọi yêu cầu’s từ xa bước vào (cái) luồng (stream): 1M req/s × 1 KB của từ xa mỗi yêu cầu = 1
GB/s. (Việc) Kéo dài (Stretching) (cái) khoảng (thời gian) tới 60 s trải ra (spreads) đó cùng luồng qua một cửa sổ 60× dài hơn, vì vậy
(cái) (được) lấy mẫu khối lượng là 1 GB/s ÷ 60 ≈16.7 MB/s. Bảng 14.18 đặt (cái) hai (các) chế độ (regimes) cạnh (bởi)
cạnh với (những) của chúng chi phí tác động.
Bảng 14.18: Việc lấy mẫu tần suất so với khả năng quan sát chi phí: (Một cách) Xấp xỉ 60× dữ liệu-khối lượng sự dao động (swing) giữa 1 s và 60 s việc lấy mẫu
tại 1M req/s, (đang) giả định khoảng 1 KB của từ xa mỗi yêu cầu.
Việc lấy mẫu
Tính hạt
Dữ liệu Khối lượng (1M req/s)
Chi phí Tác động
1 s
Vi-bùng nổ (Micro-bursts)
~1 GB/s
Cao (Yêu cầu dành riêng cụm)
60 s
Các xu hướng
~16.7 MB/s
Thấp (Tiêu chuẩn sidecar)
Sự khuyến nghị: Sử dụng (mang tính) động (việc) lấy mẫu. Lấy mẫu 1 phần trăm của thành công các yêu cầu nhưng 100
phần trăm của các lỗi. Sử dụng cao-tần suất (1 s) việc giám sát chỉ cho (được) tổng hợp các bộ đếm (counters) (giống như lỗi
tỷ lệ), nhưng thấp-tần suất (60 s) cho cao-tính bản số dữ liệu (giống như cấp độ-người dùng sự phân phối các phác thảo (sketches)).
Phần 30 cung cấp (được) thực hiện các ví dụ cho (việc) lập ngân sách việc giám sát cơ sở hạ tầng.
(Cái) còn lại câu hỏi là (cách) làm thế nào (đang) cảnh báo các cơ chế chuyển đổi (thuộc về) thống kê các tín hiệu thành (có thể) hành động
các phản hồi trước khi (cái) chi phí của im lặng sự thất bại vượt quá (cái) chi phí của sự can thiệp. (Mang tính) Chủ động (việc) cảnh báo các cơ-
chế thông báo (cho) các đội khi các sự bất thường hay ngưỡng các sự vi phạm xảy ra. Một (được) duy trì (sự) sụt giảm (drop) trong mô hình
độ chính xác có thể kích hoạt sự trôi dạt sự điều tra; cơ sở hạ tầng các cảnh báo có thể báo hiệu bộ nhớ sự bão hòa hay
(bị) xuống cấp mạng hiệu suất. (Cái) thiết kế của những các cảnh báo này quyết định (cái) khoảng trống giữa khi nào
sự xuống cấp bắt đầu và khi nào một kỹ sư hành động trên nó, và đó khoảng trống biên dịch (một cách) trực tiếp thành kinh doanh
tác động tại quy mô.
Ví dụ 14.3: Sự gợi ý việc giám sát tại quy mô
Bối cảnh: Một lớn (đang) phát trực tuyến (streaming) sự gợi ý dịch vụ phải giám sát (việc) xếp hạng chất lượng trong khi
(việc) xem các mẫu, nội dung các danh mục (catalogs), và (thuộc về) khu vực các thuần tập (cohorts) tiến hóa.
Sự thấu hiểu: (Mang tính) Truyền thống cơ sở hạ tầng việc giám sát có thể bỏ lỡ ML-cụ thể sự xuống cấp khi (việc) xem
các mẫu dịch chuyển, nội dung các thư viện thay đổi, và người dùng các thuần tập tiến hóa (xuyên) qua các khu vực. Một mạnh hơn
việc giám sát hệ thống kết hợp (thuộc về) thống kê quy trình sự kiểm soát (kiểm soát các biểu đồ để phát hiện số liệu
các chuyến du ngoạn (excursions)), dựa trên-thuần tập việc giám sát ((việc) theo dõi các nhóm phụ (một cách) riêng biệt), phản sự thực (counterfactual)
sự đánh giá ((việc) ước tính (những) gì (đã) có thể đã xảy ra dưới một khác người xếp hạng hay chính sách), và
(đang) xen kẽ (interleaving) các cuộc thử nghiệm ((việc) trộn hai (những) người xếp hạng trong một người dùng trải nghiệm để so sánh (sự) ưu tiên
các tín hiệu) để bắt (được) chất lượng (sự) mất (mát) (thứ) mà tổng hợp các số liệu che giấu.
Các hệ thống bài học: (Việc) Cảnh báo (thì) chỉ (là) hữu ích khi (cái) (được) giám sát tín hiệu khớp (với) (cái) sự thất bại chế độ.
Sự gợi ý các hệ thống cần thuần tập và phản sự thực các tín hiệu bởi vì toàn cầu các (mức) trung bình có thể
duy trì (có tính) ổn định trong khi cụ thể người dùng các nhóm hay nội dung các khu vực xuống cấp.
14.5.3.1 Dữ liệu chất lượng việc giám sát
Mô hình và cơ sở hạ tầng việc giám sát theo dõi các đầu ra. Vào (cái) lúc đầu ra các số liệu xuống cấp, tuy nhiên,
(cái) làm nền tảng bài toán có thể đã tồn tại trong (các) ngày hay (các) tuần. Dữ liệu chất lượng việc giám sát bắt các vấn đề

807
28
Lược đồ Sự xác thực: (Các)
quy tắc trong danh sách 14.4 ngăn chặn
im lặng dữ liệu hợp đồng các sự vi phạm,
(chẳng) hạn như một đặc trưng cột
(đang) thay đổi từ một số nguyên sang
một số thực (float) hay một mới danh mục xuất-
hiện (thứ) mà (đã) vắng mặt trong
suốt (việc) đào tạo.
(Mà) Không (có) này
cấp độ-đầu vào lan can, phía dưới-
dòng (downstream) mô hình việc giám sát không
thể phân biệt một dữ liệu chất lượng
lỗi khỏi một thực sự hiệu suất
sự hồi quy, (việc) che giấu (cái) gốc rễ
nguyên nhân. Một lược đồ sự không khớp (mismatch) trong
một tới hạn đặc trưng có thể làm mất hiệu lực
một (nếu) không (thì) (được) hình-thành-tốt dự-
đoán lô.
29
Quần thể (Population) Tính ổn định Chỉ-
số (In-dex) (PSI): PSI được (một cách) rộng rãi sử dụng
trong tín dụng-rủi ro bảng điểm (scorecard) việc giám-
sát để so sánh (được) kỳ vọng
và (được) quan sát (được) gộp (binned) các quần-
thể; Yurdakul và Naranjo
phân tích (những) của nó (thuộc về) thống kê các đặc-
tính (Yurdakul và Naranjo
2020). (Cái) phổ biến 0.1 và
0.2 (các) dải (bands) là hữu ích (thuộc về) hoạt-
động các quy ước (conventions), không (phải) (mang tính) phổ-
quát (thuộc về) thống kê các định luật.
ML các hoạt-
động (đã) áp dụng PSI bởi vì
nó hoạt động trên (được) gộp (mang tính) phân loại (categori-cal) hay (mang tính) liên tục các đặc trưng và
cung cấp một (có thể) diễn giải (được) sự trôi dạt
điểm số (thứ) mà không-(phải)-chuyên gia (non-specialists) có thể
đánh giá.
trước khi chúng lan truyền qua (cái) hệ thống. Trong sản xuất ML, (việc) giám sát các đầu vào (thì) thường
quan trọng (hơn) so với (việc) giám sát các đầu ra bởi vì dữ liệu các vấn đề là một phổ biến nguồn của mô hình sự xuống cấp.
(Cái) đầu tiên lan can là (có thể) thực thi đầu vào sự xác thực, như danh sách 14.4 cho thấy: lược đồ các sự kỳ vọng từ chối
(bị) dị dạng (malformed) các lô trước khi sự suy luận, (việc) biến đổi một (thuộc về) chất lượng-dữ liệu giả định thành một (có thể) kiểm thử hợp đồng.
Danh sách 14.4: Đầu vào Dữ liệu Sự xác thực: Lược đồ sự xác thực các quy tắc kiểm tra cột sự tồn tại, dữ liệu các kiểu, null các giá trị, và (thuộc về) thống kê
các ranh giới (bounds) để bắt dữ liệu chất lượng các vấn đề trước khi chúng lan truyền tới mô hình sự suy luận.
schema.require_column("user_id")
schema.require_type("timestamp", "datetime")
schema.require_non_null("feature_a")
schema.require_range("age", min_value=0, max_value=120)
schema.require_mean_between(
"purchase_amount", min_value=10, max_value=1000
)
Đầu vào dữ liệu sự xác thực Lược đồ28 sự xác thực bắt (mang tính) cấu trúc các vấn đề trước khi chúng tiếp cận (cái) mô hình.
(Cái) phổ biến quy tắc các danh mục là cột sự tồn tại các (cuộc) kiểm tra, kiểu (sự) thực thi (enforcement), null sự phát hiện, và
(thuộc về) thống kê các ranh giới.
Đặc trưng sự phân phối việc giám sát Lược đồ sự xác thực bắt (mang tính) cấu trúc sự tham nhũng (corruption) ((bị) thiếu các cột,
sai các kiểu, null các giá trị) nhưng không thể phát hiện (cái) tinh vi hơn (subtler) sự thất bại chế độ nơi dữ liệu đến trong (cái) chính xác
định dạng nhưng từ một (bị) dịch chuyển sự phân phối. Một đặc trưng (đang) đại diện (cho) người dùng tuổi có thể vượt qua mọi lược đồ (cuộc) kiểm tra
trong khi (cái) (mức) trung bình (của) nó (một cách) im lặng di cư (migrates) từ 32 (lên) 45 qua ba tháng khi một (thuộc về) tiếp thị chiến dịch thu hút một
lớn tuổi hơn nhân khẩu học (demographic). Này (thuộc về) sự phân phối sự dịch chuyển làm xuống cấp mô hình các dự đoán (từ) lâu trước khi bất kỳ (mang tính) cấu trúc
sự bất thường (anomaly) (nào) xuất hiện. (Thuộc về) Thống kê khoảng cách các thước đo (measures) định lượng này sự phân kỳ bằng (cách) (việc) so sánh (cái) hiện tại
đặc trưng các sự phân phối (so) với (việc) đào tạo các đường cơ sở. Bảng 14.19 chỉ định (có tính) đại diện cảnh báo các ngưỡng
cho ba phổ biến các số liệu, với PSI phù hợp cho (mang tính) phân loại các đặc trưng, KS các số liệu thống kê cho (mang tính) liên tục
các sự phân phối, và Jensen-Shannon sự phân kỳ cho (việc) so sánh đầy đủ xác suất các sự phân phối với một
(mang tính) đối xứng (symmetric), (bị) giới hạn (được) dẫn xuất (từ)-KL thước đo (measure).
Bảng 14.19: Đặc trưng Sự phân phối Các ngưỡng: Bắt đầu các điểm cho sự trôi dạt sự phát hiện, (được) hiệu chuẩn (calibrated) trong thực tiễn đối với mỗi đặc trưng’s
tính nhạy cảm và kinh doanh tác động. PSI các ngưỡng (chẳng) hạn như 0.1 và 0.2 là phổ biến bảng điểm-(việc) giám sát các quy ước, trong khi KS và
JS các ngưỡng phải được hiệu chuẩn với (cái) đặc trưng, mẫu kích thước, và chi phí của (bị) bỏ lỡ sự trôi dạt. Cao hơn các ngưỡng giảm (thiểu) cảnh báo sự mệt mỏi nhưng
(gây) rủi ro (việc) bỏ lỡ (mang tính) dần dần sự trôi dạt.
Số liệu
Cảnh báo Ngưỡng
Sử dụng Trường hợp (Use Case)
Quần thể Tính ổn định Chỉ số (PSI)
PSI > 0.2
(Mang tính) Phân loại và (được) gộp (binned) các đặc trưng
Kolmogorov-Smirnov số liệu thống kê
KS > 0.1
(Mang tính) Liên tục đặc trưng các sự phân phối
Jensen-Shannon sự phân kỳ
JS > 0.1
Xác suất các sự phân phối
(Việc) Hiểu tại sao chúng ta sử dụng những các ngưỡng này yêu cầu (việc) nhìn vào (cái) toán (học). (Cái) Quần thể Tính ổn định
Chỉ số (PSI)29 định lượng (thuộc về) sự phân phối sự dịch chuyển bằng (cách) (việc) so sánh (được) kỳ vọng ((việc) đào tạo) so với (vs.) thực tế ((việc) phục vụ)
các tần suất (xuyên) qua các thùng (bins) (phần B.2.2 phát triển (cái) (thuộc về) toán học các nền tảng của KL sự phân kỳ, PSI,
và thông tin lý thuyết cho các hệ thống việc giám sát). Phương trình 14.12 hình thức hóa điều này:
PSI =
𝑛
∑
𝑖=1
(thực tế𝑖−kỳ vọng𝑖)×ln( thực tế𝑖
kỳ vọng𝑖
)
(14.12)
Cho (mang tính) liên tục các sự phân phối, Kullback-Leibler (KL) sự phân kỳ cung cấp một nhạy cảm hơn sự thay thế,
mặc dù PSI’s (mang tính) đối xứng các đặc tính thường làm (cho) nó (được) ưu tiên cho sự trôi dạt (việc) cảnh báo. Phương trình 14.13 định nghĩa
(cái) cục bộ cụ thể-KL ký hiệu 𝒟KL; (ở) nơi khác trong tập này, 𝒟(𝑃𝑡‖𝑃0) biểu thị (denotes) một (mang tính) chung (thuộc về) thống kê
sự phân kỳ trong (cái) sự xuống cấp phương trình:
𝒟KL(𝑝‖𝑞) = ∑
𝑥
𝑝(𝑥)log(𝑝(𝑥)
𝑞(𝑥))
(14.13)

808
14.5 Sản xuất Các hoạt động
Để nhìn thấy điều này trong thực tiễn, xem xét một sự gợi ý hệ thống (đang) giám sát người dùng tuổi. Một sự dịch chuyển từ
“trẻ hơn” sang “lớn tuổi hơn” nhân khẩu học (demographics) có thể trông (mang tính) tinh vi trên một biểu đồ tần suất (histogram) nhưng tạo ra một rõ ràng PSI
tín hiệu, (được) phân rã (decomposed) thùng (bin) theo (by) thùng trong bảng 14.20:
Bảng 14.20: PSI (Được) Làm việc Ví dụ: Người dùng tuổi sự phân phối sự trôi dạt từ (việc) đào tạo sang (việc) phục vụ, (được) phân rã (xuyên) qua sáu tuổi các thùng. (Cái)
tổng số PSI là 0.029, (ở) tốt (well) bên dưới (cái) 0.1 (sự) cảnh báo ngưỡng, ngay cả mặc dù một vài các thùng (đã) dịch chuyển đi (by) 3 phần trăm các điểm. (Cái)
sự đóng góp cột cho thấy tại sao (được) tổng hợp PSI là (có tính) đáng tin cậy hơn (so) với mỗi-thùng (sự) kiểm tra (inspection): (mang tính) cá nhân thùng chuyển động có thể trông
đáng chú ý (noticeable) trong khi (cái) (được) tính tổng (summed) chứng cứ duy trì bên dưới (cái) cảnh báo ngưỡng.
Tuổi Thùng
Đào tạo
Phục vụ
Sự khác biệt
ln(Phục vụ/Đào tạo)
Sự đóng góp
18–25
15%
12%
-0.03
-0.223
0.0067
26–35
25%
22%
-0.03
-0.128
0.0038
36–45
20%
18%
-0.02
-0.105
0.0021
46–55
18%
20%
+0.02
+0.105
0.0021
56–65
12%
15%
+0.03
+0.223
0.0067
66+
10%
13%
+0.03
+0.262
0.0079
(Cái) tổng số PSI là 0.029 (Ổn định). (Cái) đào tạo và phục vụ các cột được cho thấy như (là) các tỷ lệ phần trăm, trong khi
(cái) sự khác biệt cột được thể hiện trong tỷ lệ các đơn vị, vì vậy một 3 phần trăm-điểm sự dịch chuyển xuất hiện như (là)
±0.03. Ngay cả mặc dù (các) cụ thể các thùng (đã) dịch chuyển đi 3 phần trăm các điểm, (cái) (được) tổng hợp sự trôi dạt (nằm) tốt bên dưới
(cái) 0.1 (sự) cảnh báo ngưỡng. Này sự tính toán ngăn chặn báo động giả khỏi nhỏ các sự dao động (fluctuations) trong khi
duy trì nhạy cảm (với) (mang tính) hệ thống các sự dịch chuyển.
Dữ liệu tính tươi mới (freshness) việc giám sát Đặc trưng các cửa hàng và dữ liệu các đường ống có thể trở nên cũ (stale) (mà) không (có) (việc) kích hoạt
(mang tính) rõ ràng các lỗi. Dữ liệu tính tươi mới việc giám sát bắt đó sự thất bại chế độ, và danh sách 14.5 cho thấy một
cấu hình (thứ) mà giám sát đặc trưng tính tươi mới và kích hoạt dự phòng (fallback) hành vi khi dữ liệu trở nên
cũ.
Danh sách 14.5: Dữ liệu Tính tươi mới Cảnh báo Cấu hình: Này cấu hình giám sát (cái) user_purchase_history đặc trưng cho tính cũ (staleness),
(đang) cảnh báo (các) hoạt động các đội thông qua PagerDuty và Slack và (đang) rơi (falling) trở lại (tới) mặc định các giá trị khi (cái) đặc trưng vượt quá (cái) tối đa
(được) cho phép tuổi.
# Ví dụ tính tươi mới cảnh báo cấu hình
feature: user_purchase_history
max_staleness: 6h
alert_channels: [pagerduty, slack]
on_stale:
action: fallback_to_default
default_value: []
Các sự thất bại tại khác nhau các lớp tạo ra khác nhau các triệu chứng và đòi hỏi khác nhau các phản hồi.
Điểm kiểm tra 14.2: (Cái) việc giám sát ngăn xếp
ML việc giám sát (thì) (được) phân lớp, không (phải) (mang tính) nguyên khối. (Bạn) Có thể (bạn) chẩn đoán (cái) nào lớp giải thích mỗi triệu
chứng (hay không)?
□Cơ sở hạ tầng sự sử dụng: (Bạn) Có thể (bạn) phân biệt một 0 phần trăm GPU sự sử dụng sự thất bại khỏi
một 100 phần trăm việc xếp hàng sự thất bại (hay không)?
□Lưu lượng truy cập thông lượng: (Bạn) Có thể (bạn) nói (việc) liệu một đột ngột QPS (sự) sụt giảm chỉ ra ngược dòng (upstream) (việc) định tuyến
sự thất bại hay (phía)-máy khách (client-side) nhu cầu sự thay đổi (hay không)?
□Dữ liệu tính tươi mới: (Bạn) Có thể (bạn) phát hiện cũ các đặc trưng trước khi (trông có vẻ) hợp lý (plausible-looking) các dự đoán phản ánh
hôm qua’s thế giới (hay không)?
□Dữ liệu sự trôi dạt: (Bạn) Có thể (bạn) sử dụng PSI hay KL sự phân kỳ để quyết định liệu sản xuất dữ liệu (có) vẫn
giống (với) (cái) (việc) đào tạo sự phân phối (hay không)?
□Mô hình độ chính xác: (Bạn) Có thể (bạn) tính đến (cho) (bị) trì hoãn sự thật cơ sở các nhãn khi (đang) diễn giải
độ chính xác các cảnh báo (hay không)?
□Thuần tập sự thiên vị: (Bạn) Có thể (bạn) sử dụng thuần tập sự phân tích để bắt nhóm phụ các sự thất bại (thứ) mà tổng hợp
độ chính xác che giấu (hay không)?
(Cái) cùng ngăn xếp phải quan sát (cái) dữ liệu các nguồn (thứ) mà cho (ăn) (cái) ML hệ thống: cơ sở dữ liệu sự sao chép độ trễ,
API điểm cuối tính có sẵn, và trích xuất, biến đổi, tải (ETL) công việc (sự) hoàn thành trạng thái. Trong một (có tính) đại diện
sự cố (incident) mẫu, một sự gợi ý hệ thống phát hiện một (về mặt) vật chất sự dịch chuyển trong user_lifetime_value
sự phân phối trong vòng hai ngày và truy vết (cái) vấn đề (tới) một cơ sở dữ liệu sự di cư (migration) (thứ) mà (đã) thay đổi (việc) tổng hợp
logic. (Mà) Không (có) dữ liệu chất lượng việc giám sát, này (cái) kiểu (của) vấn đề có thể làm xuống cấp các sự gợi ý trong (các) tuần
trước khi độ chính xác các số liệu phát hiện (cái) bài toán.
(Việc) Giám sát chi phí mô hình Khả năng quan sát cơ sở hạ tầng gánh chịu (incurs) các chi phí (thứ) mà mở rộng quy mô với việc giám sát tính hạt
(granularity). (Việc) Hiểu những các chi phí này kích hoạt hợp lý các quyết định về việc giám sát chiều sâu so với (vs.) ngân sách
các sự ép buộc.
Chi phí các thành phần Việc giám sát các chi phí vỡ (break) xuống thành bốn các danh mục, như phương trình 14.14 phân rã:
Việc giám sát Chi phí = 𝐶hấp_thụ +𝐶lưu_trữ +𝐶tính_toán +𝐶cảnh_báo
(14.14)
(Cái) bốn 𝐶∗thuật ngữ là chi phí các thành phần qua (cái) cùng (việc) kế toán cửa sổ: dữ liệu sự hấp thụ (ingestion), (được) giữ lại
lưu trữ, truy vấn hay bảng điều khiển tính toán, và cảnh báo-quy tắc sự đánh giá. (Việc) Tách biệt chúng quan trọng bởi vì
mỗi (thành phần) mở rộng quy mô với một khác kiểm soát núm (knob).
Bảng 14.21 cung cấp (có tính) đại diện đơn vị-chi phí các giả định cho mỗi thành phần:
Bảng 14.21: Việc giám sát Chi phí Các thành phần: Tình huống đơn vị các chi phí (được) sử dụng cho (cái) (được) thực hiện ví dụ. Các chi phí mở rộng quy mô (một cách) khác nhau (xuyên) qua
các thành phần: số liệu sự hấp thụ mở rộng quy mô với tính bản số (cardinality) (số của độc nhất số liệu các chuỗi), lưu trữ mở rộng quy mô với sự giữ lại, và truy vấn
các chi phí mở rộng quy mô với bảng điều khiển sự sử dụng các mẫu.
Thành phần
Điển hình Đơn vị Chi phí
Mở rộng quy mô Yếu tố (Factor)
Số liệu Sự hấp thụ
$0.10–0.50 mỗi triệu dữ liệu (các) điểm
Số của các số liệu×mẫu tỷ lệ
Nhật ký Lưu trữ
$0.50–2.00 mỗi GB/tháng
Nhật ký tính dài dòng (verbosity)×sự giữ lại khoảng (thời gian)
Truy vấn Tính toán
$0.01–0.05 mỗi truy vấn
Bảng điều khiển làm mới tỷ lệ×(các) người dùng
Cảnh báo Sự đánh giá
$0.001–0.01 mỗi sự đánh giá
Số của cảnh báo các quy tắc×kiểm tra tần suất
(Việc) Biên dịch những đơn vị các chi phí này thành một cụ thể ngân sách (sự) ước tính làm rõ (cái) thực sự chi phí của (việc) giám sát
ngay cả một đơn sản xuất mô hình.
Ví dụ 14.4: Đơn-mô hình việc giám sát ngân sách
Tình huống: Xem xét (việc) giám sát một đơn ML nút (một sản xuất mô hình) với:
• một mô hình với 3 sự triển khai các biến thể (sản xuất, canary, staging), mỗi (biến thể) (đang) phát ra 50
các số liệu
• Các số liệu (được) lấy mẫu mỗi 15 giây
• Sự giữ lại yêu cầu: 30 ngày
• 2 các bảng điều khiển (mô hình sức khỏe, cơ sở hạ tầng), 3 đội các thành viên, năm-phút (sự) làm mới
Số liệu sự hấp thụ:
• Dữ liệu các điểm mỗi tháng: 3 × 50 × (4 các mẫu/phút × 60 × 24 × 30 ngày) = 25.9M
• Chi phí tại $0.30/triệu: $7.8/tháng
Lưu trữ:
• Tại 8 byte/điểm (được) nén: 25.9M × 8 byte = 0.2 GB
• Chi phí tại $1/GB: $0.21/tháng
Truy vấn tính toán:

810
14.5 Sản xuất Các hoạt động
30
Mạch Cầu dao (Breaker) Mẫu:
(Mang tính) Tự động sự thất bại sự phát hiện
thứ (mà) “mở” khi lỗi các tỷ lệ
vượt quá (được) cấu hình các ngưỡng,
(việc) định tuyến lưu lượng truy cập ra xa khỏi (đang) thất-
bại các dịch vụ. Trong ML các hệ thống,
(cái) mẫu yêu cầu một tới-
hạn sự thích ứng (adaptation): dự đoán độ-
chính xác sự xuống cấp đòi hỏi
khác các ngưỡng so với dịch-
vụ tính có sẵn các sự thất bại, bởi-
vì một mô hình (đang) trả về (trông có vẻ) hợp-
lý nhưng không chính xác các dự đoán
kích hoạt không (có) lỗi tín hiệu, (việc) để-
lại (cái) mạch cầu dao (bị) mù
đối với (cái) nguy hiểm nhất sự thất bại
chế độ.
• Các truy vấn mỗi tháng: 2 các bảng điều khiển × 3 người dùng × (12 các truy vấn/giờ × 8 giờ/ngày × 22
ngày) = 12,672 các truy vấn/tháng
• Chi phí tại $0.02/truy vấn: $253/tháng
Tổng số: ~$261.4/tháng cho một đơn ML nút
Các hệ thống sự thấu hiểu: Điều này mở rộng quy mô (một cách) tuyến tính. Nền tảng các đội (đang) quản lý năm mươi-cộng (thêm) các mô hình đối mặt bổ-
sung các sự ép buộc nơi truy vấn chi phí sự tối ưu hóa trở nên tới hạn.
Chi phí sự tối ưu hóa các chiến lược (Cái) (mang tính) thống trị chi phí trình điều khiển trong việc giám sát cơ sở hạ tầng là số liệu tính bản số:
cao-tính bản số các nhãn (chẳng) hạn như user_id hay request_id tạo ra một (thuộc về) tổ hợp sự bùng nổ trong lưu trữ
các yêu cầu (thứ) mà có thể làm lùn (dwarf) tính toán các chi phí. (Việc) Giải quyết tính bản số thông qua (việc) lấy mẫu hay (việc) tổng hợp
cho cao-tính bản số các chiều (dimensions) (một cách) điển hình mang lại (yields) (cái) lớn nhất ngay lập tức các sự tiết kiệm. (Cái) thứ hai chính
chi phí trình điều khiển là (thuộc về) thời gian độ phân giải: (việc) lưu trữ tất cả các số liệu tại 15-giây tính hạt cho 30 ngày (thì) hiếm khi
(được) cần thiết, nhưng (yet) nó là (cái) mặc định trong nhiều việc giám sát các hệ thống. Một (được) phân tầng (tiered) sự giữ lại chính sách (cao-độ phân giải
cho gần đây các sự cố, (được) lấy mẫu xuống dữ liệu cho dài hơn lịch sử) bảo tồn (việc) gỡ lỗi tính trung thực trong khi
(việc) giảm (thiểu) lưu trữ. Bảng điều khiển truy vấn các chi phí tích lũy (một cách) tinh vi hơn: mỗi (sự) làm mới kích hoạt các truy vấn
(chống) lại (cái) các số liệu phụ trợ (backend), và mặc định tự động-làm mới các khoảng (thời gian) (xuyên) qua (hàng) tá (của) các bảng điều khiển và
(các) người dùng tạo ra (mang tính) liên tục truy vấn tải ngay cả khi không (có) ai (đang) (một cách) chủ động (đang) xem. (Việc) Thiết lập chậm hơn làm mới
các khoảng (thời gian) cho không tới hạn (noncritical) các bảng điều khiển và tự động-tạm dừng (không) hoạt động các tab có thể giảm (thiểu) truy vấn các chi phí. Cuối cùng,
cảnh báo cấu hình ảnh hưởng cả tính toán các chi phí và (thuộc về) hoạt động tính hiệu quả: (việc) củng cố (có) liên quan
các cảnh báo thành đa-điều kiện các quy tắc giảm (thiểu) sự đánh giá chi phí phi công (overhead) trong khi cũng giảm (thiểu) cảnh báo sự mệt mỏi,
(việc) căn chỉnh chi phí sự tối ưu hóa với (thuộc về) hoạt động chất lượng.
Chi phí-lợi ích khuôn khổ Biện minh (cho) việc giám sát các khoản đầu tư (chống) lại sự cố các chi phí (đang) sử dụng (cái) việc giám sát
ROI công thức trong phương trình 14.15:
Việc giám sát ROI = Các sự cố (Được) Ngăn chặn×Trung bình Sự cố Chi phí
Hàng năm Việc giám sát Chi phí
(14.15)
Nếu (mức) trung bình sự cố có chi phí $50,000 (thời gian ngừng hoạt động + kỹ thuật thời gian + danh tiếng (reputation)) và việc giám sát
ngăn chặn 5 các sự cố (hàng) năm tại $50,000 việc giám sát chi phí:
ROI = 5×$50,000
$50,000
= 5×
Này khuôn khổ giúp biện minh (cho) việc giám sát các khoản đầu tư và ưu tiên (những) số liệu nào xứng đáng mịn-
hạt sự quan sát so với (vs.) thô (việc) lấy mẫu. (Cái) Việc giám sát các hệ thống chính chúng yêu cầu sự phục hồi (resilience) việc lập kế-
hoạch để ngăn chặn (thuộc về) hoạt động mù các điểm (spots). Khi (mang tính) chính việc giám sát cơ sở hạ tầng thất bại (Prometheus
(đang) trải qua thời gian ngừng hoạt động hay Grafana trở nên không có sẵn), các đội (gây) rủi ro (việc) hoạt động mù trong suốt tới hạn
các khoảng thời gian. (Cấp độ) Sản xuất-lớp MLOps các sự triển khai do đó duy trì dư thừa (redundant) việc giám sát
các con đường: (mang tính) phụ số liệu các (bộ) thu thập (thứ) mà kích hoạt trong suốt chính hệ thống các sự thất bại, (mang tính) cục bộ (việc) ghi nhật ký
(thứ) mà tồn tại (persists) khi (được) tập trung hóa các hệ thống thất bại, và nhịp tim (heartbeat) các (cuộc) kiểm tra (thứ) mà phát hiện việc giám sát hệ thống
các (sự) mất điện (outages).
Một số các tổ chức triển khai chéo-việc giám sát nơi (mang tính) riêng biệt cơ sở hạ tầng giám sát (cái)
việc giám sát các hệ thống chính chúng, (việc) đảm bảo rằng sự quan sát các sự thất bại kích hoạt ngay lập tức các cảnh báo thông qua
(mang tính) thay thế các kênh (chẳng) hạn như PagerDuty hay (mang tính) trực tiếp các thông báo. Này phòng thủ-theo-chiều sâu (defense-in-depth) cách tiếp cận ngăn-
chặn (cái) (mang tính) thảm họa (catastrophic) tình huống nơi cả (hai) các mô hình và của chúng việc giám sát các hệ thống thất bại (một cách) đồng thời
(mà) không (có) sự phát hiện. Một mạch cầu dao30 thêm (vào) một xa hơn (further) sự bảo vệ (safeguard), (một cách) tự động (đang) định tuyến lưu lượng truy cập ra xa
khỏi một (đang) thất bại dịch vụ khi (cái) lỗi tỷ lệ (của) nó vượt quá một ngưỡng. (Việc) Điều phối những các sự bảo vệ này (xuyên) qua
nhiều (được) sao chép các dịch vụ, với dựa trên-sự đồng thuận (việc) cảnh báo và chéo-khu vực số liệu sự tổng hợp, là
một cấp độ-hạm đội (fleet-scale) mối quan tâm (thứ) mà phát sinh (arises) một khi một mô hình được sao chép (xuyên) qua các khu vực, (vượt) ra ngoài (cái) đơn-nút
phạm vi (ở) đây.
14.5.4 Sự cố phản hồi và (thuộc về) hoạt động các thực tiễn
Việc giám sát và sự trôi dạt sự phát hiện xác định các vấn đề; (cái) các thực tiễn trong phần này giải quyết chúng và
duy trì (thuộc về) hoạt động sức khỏe qua thời gian. Sự cố phản hồi, (việc) gỡ lỗi, và trực-ban (on-call) các sự luân phiên hình thành (cái)
con người mặt (side) của (cái) Sản xuất-Việc giám sát Giao diện, (việc) đảm bảo rằng (thuộc về) thống kê các tín hiệu biên dịch thành
kịp thời kỹ thuật hành động.

811
Sản xuất (việc) gỡ lỗi bắt đầu trên
(cái) dữ liệu trục (axis) của D·A·M.
14.5.4.1 Sự cố phản hồi cho ML các hệ thống
Tại 2:00 AM, một trực-ban kỹ sư nhận một cảnh báo: sự gợi ý nhấp-chuột-qua (click-through) tỷ lệ đã sụt giảm 12
phần trăm qua (cái) (đã) qua giờ (hour). Có không (có) ngăn xếp dấu vết (stack trace), không (có) lỗi nhật ký, không (có) (bị) sự cố quy trình, chỉ một (thuộc về) thống kê
tín hiệu rằng (một) thứ gì đó đã thay đổi. (Cái) người phản hồi phải phân biệt giữa bốn ứng cử viên gốc rễ
các nguyên nhân: một ngược dòng dữ liệu-đường ống sự thất bại, mô hình sự trôi dạt, một (thuộc về) mùa vụ lưu lượng truy cập mẫu, hay (thuộc về) thống kê nhiễu (noise).
Này sự mơ hồ (ambiguity) phân biệt ML các sự cố khỏi (mang tính) truyền thống phần mềm các sự cố: các triệu chứng biểu hiện (manifest)
như (là) độ chính xác sự xuống cấp thay vì (mang tính) tường minh các lỗi, và sự cố phản hồi phải tính đến (cho) (cái)
(mang tính) xác suất bản chất của (cái) hệ thống.
Độ nghiêm trọng (Severity) sự phân loại cung cấp (cái) nền tảng cho (việc) ưu tiên (sự) phản hồi trong này (mang tính) mơ hồ cảnh-
quan. Bảng 14.22 định nghĩa bốn ưu tiên các mức độ với (được) liên kết phản hồi các thời gian, từ P0 (mang tính) hoàn toàn
các sự thất bại (đang) yêu cầu 15-phút phản hồi tới P3 nhỏ các sự bất thường (đang) cho phép 24-giờ sự điều tra.
Một khi độ nghiêm trọng được chỉ định, (cái) sự cố phản hồi quy trình tuân theo một (được) cấu trúc danh sách kiểm tra (thứ) có
thứ tự thu hẹp (cái) (cuộc) tìm kiếm tại mỗi bước:
1. Sự phát hiện quyết định (cái) nào việc giám sát tín hiệu (đã) kích hoạt (cái) cảnh báo.
2. Tác động sự đánh giá (assessment) định lượng (cái) nào tỷ lệ phần trăm của lưu lượng truy cập (bị) ảnh hưởng.
3. Những người phản hồi xem xét (đã) gần đây các sự thay đổi để xác định liệu bất kỳ các mô hình, các đặc trưng, hay dữ liệu các đường ống
(nào) đã được triển khai (hay không).
4. Sự giảm nhẹ (Mitigation) các tùy chọn được đánh giá, bao gồm (việc) quay lui, dự phòng sự kích hoạt (enablement), hay lưu lượng truy cập sự giảm (thiểu).
5. Gốc rễ nguyên nhân sự phân tích quyết định liệu (cái) vấn đề xuất phát (stems) từ (cái) mô hình, dữ liệu, hay cơ sở hạ tầng (hay không).
Bảng 14.22: Sự cố Độ nghiêm trọng Sự phân loại cho ML Các hệ thống: Phản hồi các thời gian phản ánh (cái) tính khẩn cấp (urgency) và (có) tiềm năng kinh doanh
tác động của mỗi độ nghiêm trọng mức độ.
Mức độ
Các tiêu chí (Criteria)
Phản hồi Thời gian
Ví dụ
P0
Hoàn toàn mô hình sự thất bại, (việc) phục vụ các lỗi
15 phút
Mô hình trả về null các dự đoán
P1
Đáng kể độ chính xác sự xuống cấp (>10%)
1 giờ
Sự gợi ý CTR sụt giảm 15%
P2
(Mức độ) Vừa phải sự trôi dạt, (được) cục bộ hóa tác động
4 giờ
Một đặc trưng cho thấy PSI > 0.3
P3
Nhỏ các sự bất thường, không (có) người dùng tác động
24 giờ
Đào tạo đường ống sự trì hoãn (delay)
Cho P0 và P1 các sự cố, khám nghiệm tử thi (postmortem) tài liệu được yêu cầu. Những các khám nghiệm tử thi này phải bao gồm
dòng thời gian, gốc rễ nguyên nhân, người dùng tác động, và (mang tính) phòng ngừa các biện pháp. ML-cụ thể các yếu tố bao gồm (việc) xác định
(cái) nào việc giám sát khoảng trống (đã) cho phép (cái) vấn đề (để) tiếp cận (môi trường) sản xuất và (cái) gì sự xác thực (đã) có thể đã bắt (được)
nó sớm hơn.
14.5.4.2 Mô hình (việc) gỡ lỗi: Từ sự phát hiện tới sự chẩn đoán
Sự cố phản hồi phân loại (triages) và giảm nhẹ; mô hình (việc) gỡ lỗi xác định gốc rễ các nguyên nhân. Việc giám sát phát hiện
rằng (một) thứ gì đó (thì) sai; (việc) gỡ lỗi quyết định tại sao. ML (việc) gỡ lỗi khác (với) (mang tính) truyền thống phần mềm
(việc) gỡ lỗi bởi vì các sự thất bại là (mang tính) xác suất thay vì (mang tính) tất định (deterministic). Một mô hình (đang) tạo ra không chính xác
các dự đoán (thì) không ném (ra) các ngoại lệ (exceptions) hay tạo ra ngăn xếp các dấu vết, (việc) làm (cho) (mang tính) hệ thống (việc) gỡ lỗi
các cách tiếp cận (trở nên) thiết yếu cho (việc) giải quyết ML các sự cố (một cách) hiệu quả.
(Cái) (việc) gỡ lỗi quyết định cây Khi mô hình hiệu suất xuống cấp, làm việc qua những (mang tính) chẩn đoán
các câu hỏi này theo thứ tự. Cho một (mang tính) hệ thống chẩn đoán ma trận (thứ) mà lập bản đồ các triệu chứng tới D·A·M (Dữ liệu ·
Thuật toán · Máy móc) các trục, xem phần A.8 trong (cái) D·A·M phụ lục.
1. Nó có phải (là) (cái) dữ liệu (không)? Kiểm tra (cho) ngược dòng dữ liệu đường ống các sự thất bại, lược đồ các sự thay đổi, (bị) thiếu các giá trị, hay
sự phân phối các sự dịch chuyển. Dữ liệu (thì) thường (là) (cái) đầu tiên nơi để tìm kiếm bởi vì nhiều sản xuất ML các sự thất bại
bắt nguồn trong (đang) thay đổi các đầu vào, các nhãn, hay đặc trưng các đường ống.
2. Nó có phải (là) (việc) đào tạo-(việc) phục vụ sự xiên lệch (không)? So sánh đặc trưng các sự phân phối giữa (việc) đào tạo và (môi trường) sản xuất.
Sử dụng (cái) KS số liệu thống kê hay PSI để xác định (đang) phân kỳ các đặc trưng.
3. Nó có phải (là) một cụ thể quần thể phụ (subpopulation) (không)? Cắt lát (Slice) hiệu suất bởi chính các chiều (địa lý, thiết bị kiểu,
người dùng phân đoạn). Sự xuống cấp (được) cục bộ hóa (vào) một lát cắt gợi ý một dữ liệu sự bao phủ hay (việc) dán nhãn vấn đề.

812
14.5 Sản xuất Các hoạt động
4. Nó có phải (là) (thuộc về) thời gian (không)? Vẽ biểu đồ hiệu suất qua thời gian. Đột ngột các (sự) sụt giảm chỉ ra sự triển khai hay dữ liệu các vấn đề;
(mang tính) dần dần sự suy giảm (decline) gợi ý khái niệm sự trôi dạt.
5. Nó có phải (là) (cái) mô hình (không)? Chỉ sau khi (đã) loại bỏ dữ liệu các vấn đề, (hãy) kiểm tra mô hình hành vi thông qua dự đoán
sự phân tích và đặc trưng sự quy gán (attribution).
Này chuỗi làm (cho) lát cắt sự phân tích (thành) (cái) đầu tiên (sự) làm sâu sắc thêm (deepening) bước một khi một (mang tính) toàn cầu sự xuống cấp đã
được phát hiện, bởi vì nó kiểm thử liệu (cái) (trông có vẻ) hiển nhiên (apparent) (mang tính) toàn-hệ thống vấn đề có (phải) thực sự (được) tập trung trong một
quần thể phụ (hay không).
Lát cắt sự phân tích Hiệu suất các số liệu (được) tổng hợp (xuyên) qua tất cả lưu lượng truy cập có thể che giấu đáng kể các bài toán trong
các quần thể phụ. Lát cắt sự phân tích phơi bày đó sự che giấu, và bảng 14.23 minh họa (cách) làm thế nào tổng thể độ chính xác
có thể che giấu (mang tính) nghiêm trọng sự xuống cấp trong (các) cụ thể các phân đoạn.
Đặc trưng sự quy gán cho (việc) gỡ lỗi Khi lát cắt sự phân tích xác định một (có tính) vấn đề (problematic) phân đoạn, đặc trưng
sự quy gán các kỹ thuật giúp xác định (những) đặc trưng nào thúc đẩy không chính xác các dự đoán. Danh sách 14.6 chứng-
minh một quy trình làm việc (thứ) mà sử dụng SHAP các giá trị, đặc trưng-sự quy gán các điểm số (thứ) mà ước tính (cách) làm thế nào nhiều mỗi
đầu vào đặc trưng (đã) đóng góp (tới) một (mang tính) cá nhân dự đoán, để phân tích các (sự) dự đoán sai trong một cụ thể
lát cắt.
Bảng 14.23: Lát cắt Sự phân tích Ví dụ: Tổng thể độ chính xác của 91 phần trăm xuất hiện (có thể) chấp nhận (được), nhưng máy tính bảng (những) người dùng (5 phần trăm của lưu lượng truy cập)
trải nghiệm 62 phần trăm độ chính xác, một nghiêm trọng sự xuống cấp (bị) che giấu bởi sự tổng hợp. (Có tính) Hiệu quả (việc) gỡ lỗi yêu cầu (mang tính) hệ thống lát cắt
sự phân tích (xuyên) qua chính các chiều.
Người dùng Phân đoạn
Lưu lượng truy cập %
Độ chính xác
Tác động
Máy tính để bàn những người dùng
45%
94%
(Mang tính) Danh nghĩa (Nominal)
Di động (iOS)
30%
92%
(Mang tính) Danh nghĩa
Di động (Android)
20%
88%
Nhỏ sự xuống cấp
Máy tính bảng những người dùng
5%
62%
Nghiêm trọng—điều tra
Tổng thể
100%
91%
Che giấu máy tính bảng bài toán
Danh sách 14.6: Dựa trên-SHAP (Việc) Gỡ lỗi Quy trình làm việc: Này mã lọc (bị) dự đoán sai các ví dụ từ một (có tính) vấn đề lát cắt (máy tính bảng
những người dùng), tính toán SHAP các giá trị để giải thích mô hình các quyết định, và tạo ra một tóm tắt biểu đồ (đang) tiết lộ (những) đặc trưng nào đóng góp
nhiều nhất tới (cái) các lỗi.
# Dựa trên-SHAP (việc) gỡ lỗi quy trình làm việc
import shap
# Lựa chọn (bị) dự đoán sai các ví dụ từ (có tính) vấn đề lát cắt
errors = predictions[
(predictions.actual != predictions.predicted)
& (predictions.device_type == "tablet")
]
# Tính toán SHAP các giá trị cho lỗi các trường hợp
explainer = shap.Explainer(model)
shap_values = explainer(errors[feature_columns])
# Xác định các đặc trưng với cao sự quy gán cho các lỗi
shap.summary_plot(shap_values, errors[feature_columns])
Phổ biến các phát hiện từ đặc trưng sự quy gán (việc) gỡ lỗi bao gồm: cũ các đặc trưng (đặc trưng cửa hàng không
(đang) cập nhật cho (các) cụ thể các phân đoạn), (bị) thiếu đặc trưng sự bao phủ (các đặc trưng (không) được định nghĩa cho rìa (edge) các trường hợp), và
đặc trưng sự phân phối sự dịch chuyển (đặc trưng ngữ nghĩa (đã) thay đổi trong (môi trường) sản xuất).
Các hệ thống Góc nhìn 14.3: Zombie (xác sống) các đặc trưng
(Sống)-lâu (Long-lived) sản xuất các mô hình thường tích lũy các đặc trưng (những thứ) mà (những) nguyên bản những người chủ, (cái) ngữ nghĩa, hay
(được) dự định (sự) sử dụng (đã) phai mờ (faded). Một đặc trưng có thể bị phản đối (deprecated) trong ứng dụng mã trong khi vẫn (đang) chảy
qua một đặc trưng cửa hàng, đào tạo tập dữ liệu, hay (được) tuần tự hóa mô hình đầu vào hợp đồng. (Cái) mô hình có thể
học để bỏ qua nó, chia tách tín hiệu (xuyên) qua một (cái) (bản) sao, hay phụ thuộc (vào) một (việc) tiền xử lý tạo tác (thứ) mà
không (còn) ai vẫn (đang) sở hữu. (Việc) Loại bỏ một (cái) như vậy đặc trưng là do đó không còn một cục bộ (việc) dọn dẹp (cleanup): nó trở thành một
khả năng tương thích sự thay đổi (thứ) mà có thể ảnh hưởng (việc) đào tạo lại, (việc) phục vụ, (việc) giám sát, và phía dưới dòng sự phân tích.
Các đặc trưng trong ML các hệ thống không biến mất chỉ bởi vì mã những người chủ dừng suy nghĩ về chúng.
(Mà) Không (có) (mang tính) tường minh (sự) phản đối các chính sách và đặc trưng-cửa hàng (sự) quản trị (governance), các mô hình tích lũy “chết
mã” (thứ) mà tiêu thụ các tài nguyên và làm phức tạp (việc) gỡ lỗi (Sculley et al. 2015).
Zombie các đặc trưng cho thấy rằng sự quy gán có thể tiết lộ (những) gì một mô hình nên không còn phụ thuộc (vào).
Cho (mang tính) cá nhân các (sự) dự đoán sai, phản sự thực sự phân tích thêm (vào) (cái) (mang tính) bổ sung góc nhìn: (cái) tối thiểu
sự thay đổi (thứ) mà sẽ lật (flip) một đơn quyết định.
Phản sự thực sự phân tích Cho (mang tính) cá nhân các (sự) dự đoán sai, phản sự thực sự phân tích xác định (cái) tối-
thiểu sự thay đổi (thứ) mà sẽ lật (cái) dự đoán: nếu session_duration là 45 giây thay vì 12
giây, (cái) mô hình sẽ dự đoán “tham gia” (engaged) thay vì “rời bỏ” (churned). Điều này tiết lộ (những) đặc trưng nào
các ranh giới thúc đẩy các quyết định và liệu những các ranh giới đó (có) làm (cho) (thuộc về) ngữ nghĩa ý nghĩa (hay không). Phản sự thực
(những thứ) mà yêu cầu không thể tin được (implausible) các sự thay đổi (“người dùng tuổi sẽ cần phải là -5 tuổi”) thường chỉ ra đặc trưng
kỹ thuật các bài toán.
Những các kỹ thuật này (quyết định các cây, lát cắt sự phân tích, đặc trưng sự quy gán, và các phản sự thực) hình thành một
(việc) gỡ lỗi bộ công cụ (toolkit). Để áp dụng chúng (một cách) nhất quán, các đội hệ thống hóa (codify) (cái) quy trình.
(Việc) Gỡ lỗi danh sách kiểm tra (Mang tính) Hệ thống (việc) gỡ lỗi tuân theo một sáu-giai đoạn (việc) gỡ lỗi danh sách kiểm tra (thứ) mà phản chiếu
(cái) (thuộc về) khoa học phương pháp: quan sát, cách ly (isolate), đưa ra giả thuyết, kiểm thử, xác nhận, và khái quát hóa (generalize). (Cái) (sự) sắp xếp
thì (có) chủ ý bởi vì mỗi giai đoạn thu hẹp (cái) (cuộc) tìm kiếm không gian cho (cái) (giai đoạn) tiếp theo. Sự tái tạo (Reproduction) đến đầu tiên
bởi vì một ML sự thất bại (thứ) mà không thể được tái tạo trên (được) giữ-ra (held-out) dữ liệu là thường (phụ thuộc vào)-dữ liệu, một
sự thấu hiểu (thứ) mà chuyển hướng (redirects) sự điều tra hướng tới (cái) D·A·M hệ thống phân loại’s dữ liệu lớp. Một khi (được) tái tạo,
sự cách ly xác định (cái) tối thiểu đầu vào tập hợp (thứ) mà kích hoạt (cái) sự thất bại, (việc) biến đổi một (mang tính) khuếch tán (diffuse) “cái mô hình
thì sai” lời phàn nàn thành một (mang tính) cụ thể, (có thể) kiểm thử điều kiện.
Sự chia đôi (Bisection) sau đó khai thác (exploits) phiên bản lịch sử: nếu (cái) sự thất bại tương quan với một gần đây sự triển khai, (việc) so-
sánh mô hình các phiên bản chỉ ra (pinpoints) (cái) nào sự thay đổi (đã) giới thiệu (cái) sự hồi quy. Đặc trưng sự quy gán áp dụng
(cái) tính (có thể) diễn giải các kỹ thuật từ (cái) (đứng) trước các phần để xác định (những) nào đầu vào các yếu tố thúc đẩy
(cái) (có tính) sai sót (erroneous) hành vi. Sự xác thực đóng (cái) (mang tính) nhân quả vòng lặp bằng (cách) (việc) xác nhận rằng (cái) (được) giả thuyết gốc rễ
nguyên nhân, khi (được) sửa chữa, (một cách) thực sự giải quyết (cái) sự thất bại, (việc) phân biệt (mang tính) chân thực (genuine) các (bản) sửa lỗi (fixes) khỏi (mang tính) trùng hợp (coincidental)
các sự cải tiến.
(Cái) cuối cùng giai đoạn, sự phòng ngừa, chuyển đổi mỗi (được) giải quyết sự cố thành một (việc) giám sát quy tắc hay (việc) xác thực
(cuộc) kiểm tra, (một cách) có hệ thống (đang) đóng (cái) khoảng trống giữa sự phát hiện và sự tái phát (recurrence). Này (mang tính) tích lũy (sự) làm cứng (hardening)
giải thích tại sao (mang tính) trưởng thành ML các hệ thống trải nghiệm ít hơn (những) mới sự thất bại các chế độ qua thời gian: mỗi sự cố
(một cách) vĩnh viễn tăng cường (strengthens) (cái) khả năng quan sát cơ sở hạ tầng.
(Việc) Gỡ lỗi ML các hệ thống yêu cầu cả (hai) (mang tính) hệ thống phương pháp luận và miền chuyên môn. (Cái) nhiều
hiệu quả nhất (việc) gỡ lỗi thường đến từ các kỹ sư (những người) mà hiểu cả (hai) (cái) mô hình kiến trúc và
(cái) kinh doanh bối cảnh của (cái) các dự đoán.
14.5.4.3 Trực ban các thực tiễn cho ML các hệ thống
(Cái) (đứng) trước (việc) gỡ lỗi các kỹ thuật hoạt động khi một kỹ sư (đang) (một cách) chủ động điều tra một vấn đề
trong (suốt) (giờ) làm việc (business hours). Sản xuất các hệ thống, tuy nhiên, thất bại tại 3:00 AM vào cuối tuần, và (cái) người
(đang) phản hồi có thể không là (cái) người (đã) xây dựng (cái) mô hình. (Việc) Gỡ lỗi giải quyết (mang tính) cá nhân các sự cố;
trực-ban các thực tiễn duy trì (thuộc về) hoạt động sức khỏe qua thời gian bằng (cách) (việc) đảm bảo rằng (một) ai đó với (mang tính) phù hợp
chuyên môn là luôn luôn có sẵn và (được) trang bị để phản hồi. Trực-ban sự luân phiên cho ML các hệ thống yêu cầu
(được) chuyên môn hóa các thực tiễn (vượt) ra ngoài (mang tính) truyền thống phần mềm các hoạt động bởi vì ML các sự cố thường biểu hiện
như (là) (mang tính) dần dần sự xuống cấp thay vì cứng (hard) các sự thất bại. Một (mang tính) truyền thống phần mềm kỹ sư (đang) phản hồi (đối với)
một cảnh báo có thể (một cách) điển hình truy vết một ngăn xếp dấu vết tới một gốc rễ nguyên nhân trong vòng (các) phút. Một ML kỹ sư (đang) đối mặt
một 3 phần trăm độ chính xác (sự) sụt giảm phải đầu tiên quyết định liệu (cái) sự thay đổi đại diện (cho) (thuộc về) thống kê nhiễu,
(mang tính) hợp pháp khái niệm sự trôi dạt, hay một tới hạn sự thất bại (đang) yêu cầu ngay lập tức sự quay lui (hay không). Này sự phân biệt đòi hỏi
(thuộc về) thống kê bối cảnh thay vì đơn giản nhật ký sự phân tích.
Này sự mơ hồ kết hợp với (bị) trì hoãn tác động tính (có thể) nhìn thấy (visibility). Không giống như độ trễ các (sự) tăng vọt (spikes) (thứ) mà nổi lên
ngay lập tức trong các bảng điều khiển, ML sự xuống cấp có thể mất (các) giờ hay (các) ngày để biểu hiện trong kinh doanh các số liệu.
Một sự gợi ý mô hình (thứ) mà (đã) bắt đầu phục vụ (nhẹ) kém (hơn) (slightly worse) các gợi ý vào (thứ) Hai có thể không

814
14.5 Sản xuất Các hoạt động
tạo ra (có thể) đo lường (được) doanh thu tác động cho đến (thứ) Sáu, (vào) lúc (mà) (cái) cửa sổ cho dễ dàng (sự) chẩn đoán
đã đóng. Chéo-hệ thống các sự phụ thuộc (càng) làm phức tạp thêm sự phản hồi: ML các vấn đề thường bắt nguồn
trong ngược dòng dữ liệu các hệ thống (được) sở hữu bởi khác nhau các đội, (đang) yêu cầu sự điều phối (xuyên) qua (thuộc về) tổ chức
các ranh giới trong suốt sự cố (việc) phản hồi. (Cái) sâu nhất thách thức là (rằng) (có tính) hiệu quả sự phản hồi đòi hỏi
(việc) hiểu mô hình hành vi, không (phải) cơ sở hạ tầng sức khỏe (sự) đơn độc. Một cơ sở dữ liệu (người) quản trị có thể khởi động lại
một (đã bị) sự cố (crashed) dịch vụ (mà) không (cần) hiểu (những) của nó kinh doanh logic, nhưng một ML kỹ sư không thể (một cách) (có) ý nghĩa (meaningfully)
gỡ lỗi độ chính xác sự xuống cấp (mà) không (cần) hiểu (cái) mô hình’s đặc trưng các sự phụ thuộc và (được) kỳ vọng
hành vi các mẫu.
Những các thách thức này thúc đẩy (được) phân tầng (tiered) (sự) leo thang (escalation) các cấu trúc (thứ) mà khớp chuyên môn (với) sự cố độ phức tạp.
Bảng 14.24 minh họa một (được) khuyến nghị trực-ban cấu trúc cho ML các đội, nơi (mang tính) chính những người phản hồi
xử lý (mang tính) thường lệ (routine) các vấn đề (đang) sử dụng (được) tiêu chuẩn hóa các sổ tay điều hành (runbooks) trong khi (sự) leo thang các con đường kết nối tới các chuyên gia
có khả năng của sâu hơn (sự) điều tra. (Cái) song song dữ liệu trực-ban vai trò xứng đáng (sự) đặc biệt chú ý. Bởi vì
dữ liệu các vấn đề gây ra (cái) đa số của ML các sự cố, (việc) có một dữ liệu kỹ sư (có) sẵn (ở) bên cạnh (cái)
ML trực-ban (một cách) đáng kể giảm (thiểu) thời gian-để-giải quyết cho ngược dòng các bài toán. (Mà) Không (có) này song song
cấu trúc, ML các kỹ sư lãng phí (các) giờ (đang) điều tra mô hình hành vi chỉ để khám phá rằng (cái) gốc rễ
nguyên nhân nằm (lies) trong một dữ liệu đường ống (mà) họ không thể truy cập hay sửa đổi.
Bảng 14.24: ML Trực Ban Cấu trúc: (Được) Phân tầng sự leo thang với song song dữ liệu trực-ban kích hoạt (có tính) hiệu quả sự cố phản hồi. Tầng 1
xử lý (mang tính) thường lệ các vấn đề (đang) sử dụng các sổ tay điều hành; Tầng 2 giải quyết (mang tính) phức tạp (việc) gỡ lỗi; Tầng 3 quản lý (mang tính) tới hạn các sự cố (đang) yêu cầu
kiến trúc các quyết định.
Tầng
Người phản hồi
Trách nhiệm
Tầng 1 (Chính)
ML Kỹ sư
Ban đầu sự phân loại, tiêu chuẩn các sổ tay điều hành, sự leo thang
các quyết định
Tầng 2 (Leo thang)
Cấp cao ML Kỹ sư/Dữ liệu Nhà khoa học
Phức tạp (việc) gỡ lỗi, chéo-hệ thống sự điều tra,
cụ thể-mô hình các vấn đề
Tầng 3 (Tới hạn)
ML Nền tảng (Người) Dẫn dắt
Kiến trúc các quyết định, chính các sự cố, nhà cung cấp (vendor)
sự leo thang
Dữ liệu Trực Ban (Song song)
Dữ liệu Kỹ sư
Dữ liệu đường ống các vấn đề, đặc trưng cửa hàng các bài toán,
ngược dòng các sự phụ thuộc
(Có tính) Hiệu quả trực-ban phụ thuộc (một cách) nặng nề vào sổ tay điều hành chất lượng. Mọi sản xuất ML mô hình nên có
tài liệu (đang) bao phủ (cái) mô hình’s mục đích, (sự) sở hữu, và kinh doanh tính tới hạn (criticality) cùng với (những) của nó (mang tính) bình-
thường (đang) hoạt động các thông số—(được) kỳ vọng độ trễ, thông lượng, và độ chính xác các phạm vi (thứ) mà định nghĩa (có tính) khỏe mạnh
hành vi. (Thuộc về) Lịch sử các sự cố và của chúng các (sự) giải quyết cung cấp các mẫu cho phổ biến sự thất bại các mẫu,
trong khi (mang tính) chẩn đoán các lệnh kích hoạt nhanh (chóng) sức khỏe sự đánh giá: (cách) làm thế nào để kiểm tra (đã) gần đây các dự đoán, đặc trưng
các sự phân phối, và mô hình độ tự tin các điểm số. (Một cách) Tới hạn, các sổ tay điều hành phải chỉ định (sự) leo thang các tiêu chí
(khi nào để đánh thức dậy Tầng 2 so với (vs.) khi nào để quay lui (mà) không (có) sự phê duyệt) và quay lui các thủ tục với
từng-bước-một các (sự) hướng dẫn và (được) kỳ vọng phục hồi các thời gian. Các sổ tay điều hành (được) viết trong suốt bình tĩnh các khoảng thời gian tiết kiệm
(mang tính) tới hạn (các) phút trong suốt 3:00 AM các sự cố.
Ngay cả (được) thiết kế-tốt việc giám sát có thể tạo ra quá mức các cảnh báo (thứ) mà làm xói mòn trực-ban tính hiệu quả.
Cảnh báo sự mệt mỏi, (cái) xu hướng để bỏ qua hay gạt đi (dismiss) các cảnh báo sau khi (đang) trải nghiệm quá nhiều báo động giả (false positives),
đại diện (cho) một đáng kể (thuộc về) hoạt động rủi ro. Các đội chống lại sự mệt mỏi thông qua sự củng cố, (việc) nhóm
(có) liên quan các cảnh báo sao cho nhiều các đặc trưng (đang) trôi dạt (một cách) đồng thời tạo ra một đơn thông báo thay
vì (hàng) tá. (Mang tính) Thích ứng các ngưỡng (thứ) mà tính đến (cho) (hàng) tuần và (thuộc về) mùa vụ các mẫu ngăn chặn (có thể) dự đoán
các sự thay đổi (khỏi) (việc) kích hoạt không cần thiết các trang (tiếng bíp). (Việc) Đo lường cảnh báo tính (có thể) hành động cung cấp (thuộc về) thực nghiệm
sự hướng dẫn: các cảnh báo (được) hành động trên ít hơn 10 phần trăm của (cái) thời gian nên được nghỉ hưu hay (được) hiệu chuẩn lại. Khi
tạm thời (sự) tắt tiếng là (cần) thiết, trách nhiệm giải trình (accountability) các cơ chế ((việc) yêu cầu một theo-dõi phiếu (ticket) trước khi
báo thức (snoozing)) ngăn chặn các cảnh báo khỏi (việc) bị (một cách) vĩnh viễn bỏ qua.
Ca (làm việc) (Shift) các (sự) bàn giao (handoffs) đại diện (cho) một khác tới hạn thực tiễn (thứ) mà phân biệt (mang tính) trưởng thành các hoạt động. (Đang) Đi vào
trực-ban các kỹ sư cần bối cảnh về (đang) hoạt động các sự cố và của chúng hiện tại trạng thái, (đã) gần đây các sự triển khai
(thứ) mà có thể gây ra (bị) trì hoãn các vấn đề, sắp tới (được) lên lịch các sự thay đổi (chẳng) hạn như dữ liệu các sự di cư hay mô hình
các bản cập nhật, và bất kỳ các cảnh báo (nào) (thứ) mà (đã) bị (đàn) áp (suppressed) cùng với (cái) sự lý luận. (Mà) Không (có) (được) cấu trúc các (sự) bàn giao,
bối cảnh (bị) mất giữa các ca, và (đang) đi vào các kỹ sư lãng phí thời gian (đang) khám phá lại (những) thông tin (mà) của họ
(những) người tiền nhiệm (predecessors) (đã) thu thập (rồi).

815
(Mang tính) Bền vững (Sustainable) trực-ban các thực tiễn cũng phải giải quyết sự kiệt sức (burnout). ML trực-ban mang (theo) đặc biệt căng thẳng do
bởi sự cố sự mơ hồ: (cái) sự không chắc chắn của (việc) không biết liệu một cảnh báo (có) đại diện (cho) một thực vấn đề (hay không)
đòi hỏi liên tục sự cảnh giác (vigilance). Các tổ chức giảm nhẹ sự kiệt sức bằng (cách) giới hạn liên tiếp trực-ban các ngày,
(việc) cung cấp (có tính) đền bù (compensatory) thời gian nghỉ (time off) sau cao-độ nghiêm trọng các sự cố, (việc) tiến hành thường xuyên sự luân phiên các (cuộc) đánh giá (reviews)
để cân bằng tải (xuyên) qua đội các thành viên, và (việc) đầu tư vào sự tự động hóa (thứ) mà giảm (thiểu) sự khó nhọc (toil). (Cái) Mục tiêu là để
làm (cho) trực-ban các sự luân phiên (trở nên) bền vững qua (nhiều) năm của (việc) hoạt động, không (phải) để bố trí nhân sự (staff) (cho) chúng như (là) một (sự) suy nghĩ muộn màng (afterthought).
Kỹ thuật (việc) giám sát các khả năng (chỉ) một mình (thì) không đảm bảo (thuộc về) hoạt động sự thành công. (Cái) nhiều tinh vi nhất
các bảng điều khiển thất bại nếu không ai chịu trách nhiệm cho (việc) hành động trên các cảnh báo, và (cái) nhiều chi tiết nhất các sổ tay điều hành tàn lụi (languish)
nếu đội các cấu trúc không hỗ trợ (sự) sử dụng (của) chúng. Sản xuất ML các hoạt động yêu cầu (thuộc về) tổ chức
cơ sở hạ tầng (đang) song song (với) (cái) kỹ thuật: rõ ràng (sự) quản trị (governance), (được) xác định các vai trò, và giao tiếp các mẫu
(thứ) mà kích hoạt chéo-chức năng sự điều phối.
14.5.5 Sự quản trị và đội sự điều phối
Trực-ban các thực tiễn giải quyết (thuộc về) hoạt động các (trường hợp) khẩn cấp, nhưng sản xuất ML cũng yêu cầu (mang tính) chủ động sự quản-
trị và chéo-chức năng sự cộng tác (collaboration). Sự quản trị bao trùm (encompasses) (cái) các chính sách và các thực tiễn
(đang) đảm bảo rằng ML các mô hình hoạt động (một cách) minh bạch, (một cách) công bằng, và trong sự tuân thủ (compliance) với (thuộc về) đạo đức và (thuộc về) quy-
định (regulatory) các tiêu chuẩn. (Mà) Không (có) nó, (đã) được triển khai các mô hình có thể tạo ra (bị) thiên vị (biased) hay mờ đục (opaque) các quyết định, (đang) tạo ra
(thuộc về) pháp lý, (thuộc về) danh tiếng (reputational), và (thuộc về) xã hội các rủi ro. Sự quản trị tập trung vào ba cốt lõi các mục tiêu: tính minh bạch
((có thể) diễn giải (được), (có thể) kiểm toán (được) (auditable) các mô hình), tính công bằng ((mang tính) công bằng (equitable) sự đối xử (xuyên) qua người dùng các nhóm), và sự tuân thủ
(sự liên kết (alignment) với (thuộc về) pháp lý và (thuộc về) tổ chức các chính sách). (Cái) (Mang tính) cụ thể tính (có thể) diễn giải các phương pháp, tính công bằng
các số liệu, và sự thiên vị sự phát hiện các kỹ thuật (thứ) mà vận hành hóa (operationalize) những các mục tiêu này được kiểm tra trong Chương-
15; MLOps cung cấp (cái) cơ sở hạ tầng để thực thi (enforce) những các (cuộc) kiểm tra này (một cách) liên tục xuyên suốt (cái)
sự triển khai vòng đời.
(Cái) Gì làm (cho) ML sự quản trị (trở nên) (một cách) độc đáo (mang tính) thách thức là của nó vòng đời phạm vi. Không giống (như) (mang tính) truyền thống phần mềm
sự tuân thủ, (thứ) mà có thể được xác thực tại (sự) phát hành thời gian, ML sự quản trị phải kéo dài (span) sự phát triển, sự triển-
khai, và (việc) hoạt động. Trong suốt sự phát triển, các đội phải tài liệu hóa mô hình các giả định và đào tạo
dữ liệu nguồn gốc (provenance). Tại sự triển khai, (sự) trước-phát hành (prerelease) các (cuộc) kiểm toán (audits) đánh giá tính công bằng và tính mạnh mẽ (robustness). (Sự) Sau-triển-
khai (Postdeployment), (cái) (việc) giám sát các hệ thống (đã) được thảo luận trong (cái) (đứng) trước phần phải theo dõi không chỉ hiệu suất
sự xuống cấp mà cũng (cả) tính công bằng sự trôi dạt, nơi khái niệm sự trôi dạt (một cách) không cân xứng (disproportionately) ảnh hưởng (đến) cụ thể người dùng
các nhóm phụ (subgroups). Sự quản trị các chính sách (được) mã hóa vào (được) tự động hóa các đường ống đảm bảo rằng những các (cuộc) kiểm tra này được
áp dụng (một cách) nhất quán thay vì (việc) dựa vào (sự) đặc biệt (ad hoc) con người (sự) xem xét.
(Một cách) Cụ thể, một mô hình (sự) đăng ký sự thăng cấp (promotion) cổng có thể yêu cầu một (đã được) ký đặc trưng hợp đồng, một (đã được) ghi lại
đào tạo-dữ liệu dòng dõi (lineage) băm (hash), nhóm phụ các số liệu (ở) trên chính sách các ngưỡng, một canary SLO với quay lui
các tiêu chí, và một (được) đặt tên tạo tác (người) chủ trước khi (cái) mô hình có thể di chuyển từ (việc) dàn dựng tới (môi trường) sản xuất. Đó (cái) cổng
chuyển sự quản trị từ một (cuộc) họp thành một (sự) phát hành bất biến (được) thực thi bởi (cái) cùng CI/CD bộ máy (machinery)
(thứ) mà triển khai (cái) mô hình.
Sự quản trị thiết lập các chính sách, nhưng chéo-chức năng sự cộng tác thực hiện chúng. Máy
học các hệ thống được phát triển và (được) bảo trì bởi đa-ngành (multidisciplinary) các đội, và (cái) các ranh giới
giữa các vai trò tạo ra (cái) (nhiều) dễ-thất bại (failure-prone) nhất các điểm trong (cái) toàn bộ vòng đời. (Được) Chia sẻ thử nghiệm (việc) theo dõi,
mô hình (các sự) đăng ký, và (được) tiêu chuẩn hóa tài liệu cung cấp (cái) (mang tính) kết nối mô (tissue) (thứ) mà kích hoạt tính (có thể) tái-
tạo và nới lỏng (eases) (sự) bàn giao giữa các chuyên gia. Tương đương (Một cách) quan trọng là (được) chia sẻ sự hiểu biết của dữ liệu
ngữ nghĩa: các bảng chú giải thuật ngữ (glossaries), lược đồ các (sự) tham chiếu, và dòng dõi tài liệu đảm bảo rằng tất cả các bên liên quan
diễn giải các đặc trưng, các nhãn, và các thống kê (một cách) nhất quán.
Trong khi các chức danh thay đổi (xuyên) qua các tổ chức, năm cốt lõi ML đội các vai trò nổi lên (một cách) nhất quán. Bảng 14.25
lập bản đồ những các vai trò này tới (những) của chúng chính các trách nhiệm:
Bảng 14.25: ML Đội Các Vai Trò Ma trận: Rõ ràng vai trò các ranh giới ngăn chặn các khoảng trống và các sự chồng chéo (overlaps). Dữ liệu Các nhà khoa học tập trung vào mô hình chất lượng
trong khi ML Các kỹ sư xử lý sự sản xuất hóa (productionization). Dữ liệu Các kỹ sư sở hữu dữ liệu các đường ống trong khi Nền tảng Các kỹ sư sở hữu MLOps
(việc) làm công cụ (tooling). SREs đảm bảo tổng thể hệ thống độ tin cậy.
Vai trò
Chính Trọng tâm
Chính Các sản phẩm giao (Deliverables)
Sự cộng tác Các điểm
Dữ liệu
Nhà khoa học
Mô hình sự phát triển,
(sự) thử nghiệm, thuật toán
sự lựa chọn
(Đã được) Đào tạo các mô hình, thử nghiệm
các kết quả, hiệu suất
các điểm chuẩn (benchmarks)
Bàn giao (Hands off) cho ML Kỹ sư để
sản xuất hóa

816
14.5 Sản xuất Các hoạt động
Vai trò
Chính Trọng tâm
Chính Các sản phẩm giao (Deliverables)
Sự cộng tác Các điểm
ML
Kỹ sư
Sản xuất ML các hệ thống, (việc) đào tạo
các đường ống, (việc) phục vụ cơ sở hạ tầng
(Đã được) Triển khai các mô hình, (việc) đào tạo
các đường ống, (việc) phục vụ các hệ thống
Nhận từ Dữ liệu Nhà khoa học; làm việc
với Nền tảng Kỹ sư về
cơ sở hạ tầng
Dữ liệu
Kỹ sư
Dữ liệu các đường ống, đặc trưng
kỹ thuật, dữ liệu chất lượng
Đặc trưng các đường ống, dữ liệu chất lượng
các hệ thống, đặc trưng các cửa hàng
Cung cấp dữ liệu cho Dữ liệu Nhà khoa học;
bảo trì đặc trưng cửa hàng cho ML
Kỹ sư
Nền tảng
Kỹ sư
MLOps cơ sở hạ tầng, (việc) làm công cụ,
sự tự động hóa
CI/CD các đường ống, (việc) giám sát
các hệ thống, (việc) tính toán (compute)
cơ sở hạ tầng
Kích hoạt ML Kỹ sư; bảo trì
(được) chia sẻ cơ sở hạ tầng
De-
vOps/SRE
Độ tin cậy, sự cố phản hồi,
hệ thống sức khỏe
SLOs/SLAs, trực-ban
các thủ tục, các sổ tay điều hành
Hỗ trợ tất cả các vai trò; sở hữu sản xuất
sức khỏe
Rõ ràng vai trò các định nghĩa (là) quan trọng nhất tại (sự) bàn giao các điểm, nơi công việc chuyển tiếp (transitions) giữa các chuyên gia.
(Cái) (Nhiều) Dễ-thất bại nhất (sự) bàn giao xảy ra giữa Dữ liệu Các nhà khoa học và ML Các kỹ sư: một mô hình (thứ) mà
hoạt động tốt trong một Jupyter sổ tay có thể thất bại trong (môi trường) sản xuất do bởi (không) được tài liệu hóa (việc) tiền xử lý
các bước, (được) mã hóa cứng (hardcoded) tập tin các đường dẫn, hay môi trường các sự phụ thuộc. Tương tự (như vậy), (cái) (sự) bàn giao từ ML Các kỹ-
sư cho SREs (Beyer et al. 2016) yêu cầu (đã được) xác thực (việc) giám sát các bảng điều khiển, (đã được) cấu hình (việc) cảnh báo các quy tắc,
(đã được) tài liệu hóa các sổ tay điều hành, và (đã được) kiểm thử quay lui các thủ tục. Dữ liệu Các kỹ sư bàn giao cho (cái) rộng hơn ML
đội thông qua đặc trưng các hợp đồng, (mang tính) hình thức các đặc tả (specifications) của lược đồ, sự mới mẻ SLOs, và chất lượng các (sự) đảm-
bảo (guarantees) (những thứ) mà ngăn chặn thầm lặng (silent) đường ống các sự thay đổi (khỏi) (việc) nổi lên (surfacing) như (là) (mang tính) bí ẩn mô hình sự xuống cấp (nhiều) tuần
sau đó. Các tổ chức giảm nhẹ những (sự) bàn giao các rủi ro này thông qua (được) tiêu chuẩn hóa mô hình các giao diện, (được) yêu cầu
tài liệu, và tính (có thể) tái tạo các yêu cầu (những thứ) mà phải được xác thực trước mỗi sự chuyển tiếp.
14.5.5.1 (Các) Bên liên quan (Stakeholder) sự giao tiếp
(Có tính) Hiệu quả MLOps mở rộng (vượt) ra ngoài nội bộ đội sự điều phối tới (cái) (mang tính) rộng hơn sự giao tiếp các (sự) thách-
thức (thứ) mà nảy sinh (arise) khi (thuộc về) kỹ thuật các đội giao tiếp (interface) với (thuộc về) kinh doanh các bên liên quan. Chéo-chức năng
sự cộng tác giải quyết sự điều phối bên trong (thuộc về) kỹ thuật các đội; (các) bên liên quan sự giao tiếp kết nối
(thuộc về) kỹ thuật và (thuộc về) kinh doanh các miền. (Có tính) Hiệu quả MLOps kết nối những các miền này bằng (cách) (việc) dịch (các) máy
học (sự) thực tế thành các thuật ngữ (mà) các bên liên quan có thể hành động trên (chúng). Không giống như (mang tính) tất định phần mềm, máy học
các hệ thống thể hiện (exhibit) (mang tính) xác suất hiệu suất, dữ liệu các sự phụ thuộc, và sự xuống cấp các mẫu (những thứ) mà
các bên liên quan thường cảm thấy (phản) trực giác (counterintuitive).
(Cái) Phổ biến nhất sự giao tiếp thách thức nổi lên từ (bị) đơn giản hóa quá mức (oversimplified) sự cải tiến các yêu cầu.
Sản phẩm những người quản lý thường xuyên đề xuất “làm (cho) (cái) mô hình (trở nên) chính xác hơn” (mà) không (cần) hiểu
(nằm bên) dưới (underlying) các sự đánh đổi (trade-offs). (Có tính) Hiệu quả sự giao tiếp đóng khung lại (reframes) (những) yêu cầu như vậy bằng (cách) (việc) trình bày (mang tính) cụ thể
các tùy chọn: (việc) cải thiện độ chính xác từ 85 phần trăm tới 87 phần trăm có thể yêu cầu (một cách) đáng kể nhiều hơn (đã được) dán nhãn
dữ liệu và một chậm hơn mô hình (thứ) mà vi phạm (cái) độ trễ ngân sách. (Việc) Trình bày (Articulating) (mang tính) cụ thể các ràng buộc biến đổi
(mang tính) mơ hồ các yêu cầu thành (đã được) thông báo kinh doanh các quyết định.
(Việc) Dịch (thuộc về) kỹ thuật các số liệu thành kinh doanh tác động yêu cầu (mang tính) nhất quán các khuôn khổ (đang) kết nối
mô hình hiệu suất (tới) (thuộc về) hoạt động các kết quả. Một 5 phần trăm độ chính xác sự cải tiến xuất hiện khiêm tốn trong
sự cô lập (isolation), nhưng (việc) bối cảnh hóa (contextualizing) điều này như (là) “(việc) giảm báo động giả (về) gian lận từ 1,000 xuống 800 (hàng) ngày khách hàng
sự ma sát (friction) các sự cố” cung cấp (có thể) hành động kinh doanh bối cảnh.
Này sự kết nối thì không (mang tính) tuyến tính. Hình 14.9 phơi bày này (sự) phi tuyến tính: (cái) (mang tính) tối ưu (đang) hoạt động điểm
cho một mô hình (thì) hiếm khi (là) (cái) điểm của cao nhất độ chính xác. Nó là (cái) điểm nơi (cái) (được) kết hợp chi phí của Báo động
Giả (ví dụ, (việc) chặn một (mang tính) hợp pháp người dùng) và Âm tính Giả (ví dụ, (việc) bỏ lỡ gian lận)
được giảm thiểu.
Sự cố sự giao tiếp trình bày (presents) một khác tới hạn thách thức. Khi các mô hình xuống cấp hoặc yêu cầu
các (sự) quay lui, (việc) duy trì (các) bên liên quan sự tin tưởng phụ thuộc vào rõ ràng sự phân loại: (mang tính) tạm thời hiệu suất
các sự biến động (fluctuations) như (là) bình thường sự biến đổi (variation), dữ liệu sự trôi dạt như (là) (được) lên kế hoạch (sự) bảo trì các yêu cầu, và hệ thống
các sự thất bại (đang) đòi hỏi ngay lập tức sự quay lui. (Mang tính) Thường xuyên hiệu suất (việc) báo cáo các nhịp độ (cadences) (một cách) ưu tiên (preemptively)
giải quyết độ tin cậy các mối quan tâm.
Tài nguyên (sự) biện minh (justification) yêu cầu (việc) dịch (thuộc về) kỹ thuật các yêu cầu thành kinh doanh giá trị. Thay vì
(việc) yêu cầu “tám A100 GPUs cho mô hình (việc) đào tạo,” (có tính) hiệu quả sự giao tiếp đóng khung (frames) các (sự) đầu tư như
(là) “cơ sở hạ tầng để giảm thử nghiệm chu kỳ thời gian từ (các) tuần xuống (các) ngày, (đang) kích hoạt nhanh hơn đặc trưng sự lặp lại.”
Dòng thời gian sự ước lượng phải tính đến (cho) (mang tính) thực tế các tỷ lệ: dữ liệu sự chuẩn bị và sự triển khai
sự tích hợp thường chi phối (dominate) (cái) lịch trình, trong khi mô hình sự phát triển (thì) chỉ (là) một phần của (cái) công việc.

817
0.0
0.2
0.4
0.6
0.8
1.0
Phân loại Ngưỡng (Threshold)
0
100
200
300
400
(Được) Kỳ vọng Chi phí ($)
Tối ưu ngưỡng = 0.34
FP Chi phí ($100/(bị) chặn người dùng)
FN Chi phí ($500/(bị) bỏ lỡ gian lận)
Tổng Chi phí
Hình 14.9: (Cái) Kinh doanh Chi phí Đường cong: (Được) Kỳ vọng chi phí so với phân loại ngưỡng. (Thuộc về) Kỹ thuật các số liệu giống (như) ROC các đường cong che giấu (cái)
(thuộc về) kinh tế (sự) thực tế: các lỗi có khác nhau các chi phí. Trong này gian lận (sự) phát hiện kịch bản, một âm tính giả ((bị) bỏ lỡ gian lận) tốn $500, trong khi một
báo động giả ((bị) chặn người dùng) tốn $100. (Cái) hệ thống gắn cờ một giao dịch như (là) gian lận khi của nó điểm số vượt quá (cái) ngưỡng, vậy nên một thấp hơn
ngưỡng gắn cờ nhiều hơn các giao dịch. Bởi vì (việc) bỏ lỡ gian lận (thì) gấp 5 lần (5x) (nhiều) tốn kém hơn, (cái) tối ưu ngưỡng dịch chuyển (sang) trái của trung tâm, (việc) làm (cho)
(cái) hệ thống (trở nên) (mang tính) tấn công (aggresive) hơn tại (việc) gắn cờ (có tính) đáng ngờ các giao dịch và (việc) chấp nhận nhiều hơn các báo động giả để giảm thiểu đắt đỏ các (sự) bỏ lỡ.
Với ngang bằng (equal) các chi phí (cái) (mức) tối ưu (optimum) sẽ nằm tại ngưỡng = 0.50; (cái) sự bất đối xứng (asymmetry) kéo nó hướng tới ngưỡng ≈0.34. MLOps là (cái)
kỷ luật (discipline) của (việc) tinh chỉnh này ngưỡng (một cách) động (dynamically) khi các chi phí thay đổi.
Hãy xem xét một gian lận (sự) phát hiện đội (đang) thực hiện mô hình các sự cải tiến. Khi các bên liên quan yêu cầu
(được) nâng cao độ chính xác, (cái) đội phản hồi với một (được) cấu trúc (sự) đề xuất (proposal): (việc) tăng (sự) phát hiện các tỷ lệ từ
92 phần trăm tới 94 phần trăm yêu cầu (việc) tích hợp bên ngoài dữ liệu các nguồn, (việc) kéo dài đào tạo khoảng thời gian (duration) thêm
hai tuần, và (việc) chấp nhận 30 phần trăm cao hơn cơ sở hạ tầng các chi phí, nhưng sẽ ngăn chặn một (được) ước tính
$1 triệu trong (hàng) năm gian lận các (sự) tổn thất trong khi (đang) giảm báo động giả (các) cảnh báo (đang) ảnh hưởng 50,000 (các) khách hàng
(hàng) tháng.
Thông qua (có) kỷ luật (các) bên liên quan sự giao tiếp, MLOps (những) người thực hành duy trì (thuộc về) tổ chức
sự hỗ trợ trong khi (đang) thiết lập (mang tính) thực tế các (sự) kỳ vọng về hệ thống các khả năng. Này sự giao tiếp
năng lực (competency) (thì) (mang tính) thiết yếu như (là) (thuộc về) kỹ thuật chuyên môn cho (việc) duy trì (mang tính) thành công ML các hoạt động.
14.5.6 ML kiểm thử điểm số
Một sự phát hành-sự sẵn sàng (readiness) (sự) đánh giá cần một (được) chia sẻ (bản) kiểm kê (inventory) của (cái) (khoản) nợ các mẫu (thứ) mà có thể làm (cho) một mô hình
(không) an toàn để triển khai ngay cả khi (những) của nó ngoại tuyến các số liệu trông (có thể) chấp nhận (được). Bảng 14.26 củng cố (consolidates) (cái) các mẫu
(đã) được thảo luận xuyên suốt này chương, (đang) cung cấp (cái) (sự) tham chiếu (thứ) mà (cái) sự đánh giá phiếu đánh giá (rubric) bên dưới xây dựng
trên.
Bảng 14.26: (Thuộc về) Kỹ thuật Nợ Các mẫu: Máy học các hệ thống tích lũy (mang tính) riêng biệt (distinct) các hình thức của (thuộc về) kỹ thuật nợ từ dữ liệu
các sự phụ thuộc, mô hình các sự tương tác, và (đang) tiến hóa (thuộc về) hoạt động các bối cảnh. (Thuộc về) Cấp một nợ các mẫu, của chúng các nguyên nhân, các triệu chứng, và
(được) khuyến nghị sự giảm nhẹ các chiến lược hướng dẫn những người thực hành trong (việc) nhận ra và (việc) giải quyết những các thách thức này (một cách) có hệ thống.
Nợ Mẫu
Chính Nguyên nhân
Chính Các triệu chứng
Sự giảm nhẹ Các chiến lược
Ranh giới Sự xói mòn (Erosion)
(Một cách) Chặt chẽ (được) ghép cặp (coupled)
các thành phần, (không) rõ ràng
các giao diện
Các sự thay đổi xếp tầng (cascade) (một cách) (không thể) dự đoán,
CACHE nguyên tắc các sự vi phạm
Thực thi (mang tính) mô-đun (modular) các giao diện,
thiết kế cho sự đóng gói (encapsulation)
Sự sửa chữa Các (sự) xếp tầng
(Mang tính) Tuần tự mô hình
các sự phụ thuộc, (được) kế thừa
các giả định
Ngược dòng các (bản) sửa lỗi làm hỏng
phía dưới dòng các hệ thống, (đang) leo thang
các sự sửa đổi (revisions)
Cẩn thận sự tái sử dụng so với (vs.) sự thiết kế lại
các sự đánh đổi, rõ ràng (việc) lập phiên bản
(Không) Được khai báo Những người tiêu dùng
(Không) Chính thức đầu ra sự chia sẻ,
(không) được theo dõi các sự phụ thuộc
Thầm lặng sự hỏng hóc (breakage) từ mô hình
các bản cập nhật, (bị) ẩn phản hồi các vòng lặp
Nghiêm ngặt truy cập các kiểm soát, (mang tính) hình thức
giao diện các hợp đồng, (sự) sử dụng
(việc) giám sát
Dữ liệu Sự phụ thuộc Nợ
(Không) Ổn định (Unstable) hay
(bị) sử dụng (dưới mức) dữ liệu các đầu vào
Mô hình các sự thất bại từ dữ liệu
các sự thay đổi, giòn (brittle) đặc trưng các đường ống
Dữ liệu (việc) lập phiên bản, dòng dõi (việc) theo dõi,
để-lại-một-cái-ra sự phân tích
818
14.5 Sản xuất Các hoạt động
Nợ Mẫu
Chính Nguyên nhân
Chính Các triệu chứng
Sự giảm nhẹ Các chiến lược
Phản hồi Các vòng lặp
Mô hình các đầu ra ảnh hưởng
(tới) tương lai đào tạo dữ liệu
Tự-củng cố hành vi,
(bị) ẩn hiệu suất
sự xuống cấp
Dựa trên-đoàn hệ (Cohort) (việc) giám sát, canary
các sự triển khai, (thuộc về) kiến trúc
sự cách ly
Đường ống Nợ
(Sự) Đặc biệt các quy trình làm việc, (sự) thiếu
của tiêu chuẩn các giao diện
(Có tính) Mỏng manh (Fragile) sự thực thi, sự trùng lặp (duplication),
sự bảo trì gánh nặng
(Mang tính) Mô-đun thiết kế, quy trình làm việc
sự điều phối (orchestration) các công cụ, (được) chia sẻ
các thư viện
Cấu hình Nợ
(Bị) Phân mảnh (Fragmented) các cài đặt,
tồi (việc) lập phiên bản
(Không thể) Tái tạo các kết quả, thầm lặng
các sự thất bại, (việc) tinh chỉnh sự mờ đục (opacity)
Phiên bản (việc) kiểm soát, sự xác thực,
(được) cấu trúc các định dạng, sự tự động hóa
Nguyên mẫu Nợ
Nhanh (chóng) (việc) tạo nguyên mẫu (prototyping)
các (sự) phím tắt, chặt chẽ
mã-logic (sự) ghép cặp
Tính (không thể) linh hoạt (Inflexibility) khi các hệ thống mở rộng (quy mô),
(mang tính) khó khăn đội sự cộng tác
(Có tính) Linh hoạt các nền tảng, (có) chủ ý (intentional)
nợ (việc) theo dõi, (được) lên kế hoạch
sự tái cấu trúc (refactoring)
Với những (cái) (khoản) nợ các mẫu (đó) (ở) trong một nơi, nhận thức (chỉ) một mình (thì) (không) đủ (insufficient); các đội cần một (mang tính) hệ thống
(thuộc về) kỹ thuật nợ sự đánh giá phiếu đánh giá (thứ) mà chuyển đổi (mang tính) chủ quan “(liệu) này hệ thống (có) sẵn sàng (không)?” các cuộc trò chuyện
thành (có thể) định lượng (được) các (sự) đánh giá (evaluations). (Cái) ML Kiểm thử Điểm số (Breck et al. 2017) cung cấp một (mang tính) hệ thống phiếu đánh giá cho
(việc) đánh giá sản xuất sự sẵn sàng (xuyên) qua bốn hạng mục: dữ liệu các (cuộc) kiểm thử, mô hình các (cuộc) kiểm thử, ML cơ sở hạ tầng
các (cuộc) kiểm thử, và (việc) giám sát các (cuộc) kiểm thử. (Cái) bài báo (paper) định nghĩa 28 các (cuộc) kiểm thử (vào) trong tổng số, bảy (cái) (trên) mỗi phần, với một phần hay toàn bộ
tín dụng (credit) cho mỗi (cuộc) kiểm thử. Sự sẵn sàng được theo dõi bởi phần thay vì bởi một đơn giản tổng-cộng (grand-total) (sự) trưởng thành
dải (band): một hệ thống với mạnh (mẽ) mô hình các (cuộc) kiểm thử nhưng yếu (việc) giám sát vẫn mang sản xuất rủi ro. Bảng 14.27
tóm tắt (mang tính) đại diện các (cuộc) kiểm thử (mà) những người thực hành nên thực hiện:
• Dữ liệu phần: Xác thực đặc trưng các (sự) kỳ vọng, quyền riêng tư (privacy) các kiểm soát, và liệu mỗi đặc trưng (có)
có lợi so với (relative) (những) của nó (thuộc về) hoạt động chi phí (hay không).
• Mô hình phần: Xác thực (đã được) xem xét mô hình các đặc tả, siêu tham số (hyperparameter) kỷ luật (discipline), sự cũ rích (staleness)
các giới hạn, và ngoại tuyến-trực tuyến số liệu sự liên kết.
• Cơ sở hạ tầng phần: Xác thực (có thể) tái tạo (việc) đào tạo, sự quay lui, (việc) đào tạo-(việc) phục vụ tính nhất quán,
và sự triển khai các cổng (gates).
• (Việc) Giám sát phần: Xác thực các cảnh báo cho sự phụ thuộc các sự thay đổi, dữ liệu các bất biến (invariants), sự xiên lệch, và
mô hình sự cũ rích.
Bảng 14.27: ML Kiểm thử Điểm số Danh sách kiểm tra: (Mang tính) Đại diện sản xuất-sự sẵn sàng các (cuộc) kiểm thử từ (cái) ML Kiểm thử Điểm số phiếu đánh giá. (Cái) Nguyên bản
phiếu đánh giá chứa 28 các (cuộc) kiểm thử (được) nhóm thành bốn phần của bảy các (cuộc) kiểm thử (cho) mỗi (phần); phần các điểm số phơi bày liệu sản xuất rủi ro đến từ
dữ liệu sự xác thực, mô hình sự xác thực, cơ sở hạ tầng, hay (việc) giám sát (hay không) thay vì (việc) che giấu (cái) điểm yếu trong một đơn tổng số. Dựa trên Breck
et al. (2017).
Hạng mục
(Cuộc) Kiểm thử
Sự thực hiện Ví dụ
Dữ liệu Các (cuộc) kiểm thử
Đặc trưng các (sự) kỳ vọng được ghi nhận trong lược đồ
Great Expectations, TFX Data Validation
Tất cả các đặc trưng là (có) lợi (không (có) (bị) sử dụng các đặc trưng)
Đặc trưng tầm quan trọng sự phân tích, (sự) cắt bỏ (ablation)
các (cuộc) nghiên cứu
Không (có) đặc trưng’s chi phí vượt quá (cái) của nó lợi ích
Độ trễ/độ chính xác sự đánh đổi sự phân tích
Dữ liệu đường ống có (mang tính) phù hợp quyền riêng tư các kiểm soát
PII sự phát hiện, truy cập (việc) ghi nhật ký
Mô hình Các (cuộc) kiểm thử
Mô hình đặc tả được xem xét và (được) kiểm tra vào phiên bản
(việc) kiểm soát
(Được) Git-theo dõi mô hình các cấu hình (configs)
Ngoại tuyến và trực tuyến các số liệu được tương quan
A/B kiểm thử sự xác thực của ngoại tuyến các sự cải tiến
Tất cả siêu tham số được tinh chỉnh
(Được) Tự động hóa HPO với (đã được) theo dõi các kết quả
Mô hình sự cũ rích được đo lường và (được) giới hạn (bounded)
Hiệu suất sự suy giảm (decay) (việc) giám sát
Cơ sở hạ tầng Các (cuộc) kiểm thử
(Việc) Đào tạo là (có thể) tái tạo
(Được) Cố định (Fixed) các hạt giống (seeds), (đã được) lập phiên bản dữ liệu, (đã bị) khóa
các sự phụ thuộc
Mô hình có thể được quay lui tới (đứng) trước phiên bản
Mô hình (sự) đăng ký với (việc) lập phiên bản
(Việc) Đào tạo và (việc) phục vụ mã các con đường được kiểm thử cho
tính nhất quán
Đặc trưng cửa hàng sự tích hợp các (cuộc) kiểm thử
Mô hình chất lượng được xác thực trước khi (việc) phục vụ
(Được) Tự động hóa sự xác thực các cổng trong CI/CD
(Việc) Giám sát Các (cuộc) kiểm thử
Sự phụ thuộc các sự thay đổi dẫn đến (các) cảnh báo
Dữ liệu lược đồ (việc) giám sát

14. ML Operations
819
Category (Hạng mục)
Test (Kiểm thử)
Implementation Example (Ví dụ triển khai)
Data invariants hold in training and serving (Các bất biến dữ liệu được giữ nguyên trong quá trình huấn luyện và phục vụ)
Distribution comparison tests (Các kiểm thử so sánh phân phối)
Training and serving features are not skewed (Các đặc trưng huấn luyện và phục vụ không bị lệch)
Training-serving skew detection (Phát hiện sự lệch giữa huấn luyện-phục vụ)
Model staleness triggers retraining (Sự cũ kỹ của mô hình kích hoạt việc huấn luyện lại)
Automated retraining pipelines (Các đường ống huấn luyện lại tự động)

Quarterly audits against this rubric, prioritizing tests that address the most frequent incident (Các cuộc kiểm toán hàng quý dựa trên bảng tiêu chí này, ưu tiên các kiểm thử giải quyết sự cố thường xuyên nhất)
types, reveal where operational investments will yield the highest reliability gains. Checking boxes (các loại, tiết lộ nơi mà các khoản đầu tư vận hành sẽ mang lại những lợi ích về độ tin cậy cao nhất. Việc đánh dấu vào các hộp kiểm)
is necessary but not sufficient. Production readiness requires understanding how practices integrate (là cần thiết nhưng không đủ. Sự sẵn sàng cho môi trường sản xuất đòi hỏi việc hiểu cách các thực tiễn tích hợp)
into a coherent system and how organizations evolve their capabilities over time. (vào một hệ thống mạch lạc và cách các tổ chức phát triển các khả năng của họ theo thời gian.)

14.6 Design and Maturity Framework (14.6 Khung thiết kế và sự trưởng thành)
An organization deploying its initial ML model might rely on a hand-run Jupyter notebook, a (Một tổ chức triển khai mô hình ML ban đầu của họ có thể dựa vào một sổ tay Jupyter chạy bằng tay, một)
scheduled cron job, and minimal monitoring. A mature enterprise runs thousands of models (cron job được lập lịch, và việc giám sát tối thiểu. Một doanh nghiệp trưởng thành chạy hàng ngàn mô hình)
through automated pipelines with drift detection, canary deployments, and continuous validation. (thông qua các đường ống tự động với sự phát hiện độ trôi, các đợt triển khai canary, và việc xác thực liên tục.)
Both are doing “MLOps,” yet the gap between them spans orders of magnitude in reliability, cost (Cả hai đều đang làm “MLOps,” nhưng khoảng cách giữa họ kéo dài các cấp bậc độ lớn về độ tin cậy, sự hiệu quả)
efficiency, and engineering velocity. Deployment case studies show that practical challenges appear (về chi phí, và tốc độ kỹ thuật. Các nghiên cứu tình huống triển khai cho thấy rằng các thách thức thực tế xuất hiện)
across the ML deployment workflow (Paleyes et al. 2022). This chapter uses operational maturity as (xuyên suốt quy trình triển khai ML (Paleyes và cộng sự 2022). Chương này sử dụng sự trưởng thành vận hành như)
a systems lens for that progression: organizations evolve from ad hoc experimentation toward fully (một lăng kính hệ thống cho tiến trình đó: các tổ chức tiến hóa từ việc thử nghiệm đặc biệt (ad hoc) hướng tới)
automated operations, and understanding where a team stands on this continuum is as important (các hoạt động hoàn toàn tự động, và việc hiểu một nhóm đứng ở đâu trên sự liên tục này quan trọng như)
as knowing the technical components themselves. Identifying what investments yield the highest (việc biết các thành phần kỹ thuật đó. Việc xác định các khoản đầu tư nào mang lại kết quả cao nhất)
returns at each stage guides resource allocation more effectively than adopting tools indiscriminately. (ở mỗi giai đoạn sẽ hướng dẫn việc phân bổ tài nguyên hiệu quả hơn so với việc áp dụng các công cụ một cách bừa bãi.)

14.6.1 Maturity levels (14.6.1 Các mức độ trưởng thành)
The ML Test Score assesses individual practices. Operational maturity captures something broader: (Điểm kiểm thử ML đánh giá các thực tiễn cá nhân. Sự trưởng thành vận hành nắm bắt một cái gì đó rộng hơn:)
the systemic integration of those practices into a coherent whole. The key distinction is not which (sự tích hợp hệ thống của các thực tiễn đó vào một tổng thể mạch lạc. Sự khác biệt chính không phải là)
tools a team has adopted but how well infrastructure, automation, monitoring, governance, and (những công cụ nào một nhóm đã áp dụng mà là cơ sở hạ tầng, tự động hóa, giám sát, quản trị, và)
collaboration work together across the ML lifecycle. Lifecycle tools such as MLflow address parts of (sự cộng tác hoạt động cùng nhau tốt như thế nào xuyên suốt vòng đời ML. Các công cụ vòng đời như MLflow giải quyết các phần của)
that workflow (Zaharia et al. 2018), but maturity is the organizational ability to make the pieces work (quy trình làm việc đó (Zaharia và cộng sự 2018), nhưng sự trưởng thành là khả năng tổ chức để làm cho các mảnh ghép hoạt động)
together. Although operational maturity exists on a continuum, distinguishing broad maturity levels (cùng nhau. Mặc dù sự trưởng thành vận hành tồn tại trên một sự liên tục, việc phân biệt các mức độ trưởng thành rộng)
helps illustrate how ML systems evolve from research prototypes to production-grade infrastructure. (giúp minh họa cách các hệ thống ML tiến hóa từ các nguyên mẫu nghiên cứu sang cơ sở hạ tầng cấp độ sản xuất.)

At the lowest level, ML workflows are ad hoc: experiments run manually, models train on local (Ở mức độ thấp nhất, các quy trình ML là đặc biệt (ad hoc): các thí nghiệm chạy thủ công, các mô hình huấn luyện trên)
machines, and deployment involves hand-crafted scripts. As maturity increases, workflows become (các máy cục bộ, và việc triển khai liên quan đến các kịch bản được tạo bằng tay. Khi sự trưởng thành tăng lên, các quy trình làm việc trở nên)
structured: teams adopt version control, automated training pipelines, and centralized model (có cấu trúc: các nhóm áp dụng kiểm soát phiên bản, các đường ống huấn luyện tự động, và sự lưu trữ mô hình)
storage. At the highest levels, systems are fully integrated with infrastructure-as-code, continuous (tập trung. Ở các mức độ cao nhất, các hệ thống được tích hợp đầy đủ với cơ sở hạ tầng dưới dạng mã (infrastructure-as-code), các đường ống phân phối)
delivery pipelines, and automated monitoring that support large-scale deployment and rapid (liên tục (continuous delivery), và sự giám sát tự động cái mà hỗ trợ sự triển khai quy mô lớn và sự)
experimentation. (thử nghiệm nhanh chóng.)

The distinguishing marker at each stage is not which tools a team adopts but how tightly infras- (Dấu hiệu phân biệt ở mỗi giai đoạn không phải là một nhóm áp dụng công cụ nào mà là mức độ chặt chẽ của)
tructure, automation, and monitoring integrate across the lifecycle—table 14.28 shows that the leap (cơ sở hạ tầng, tự động hóa, và giám sát tích hợp xuyên suốt vòng đời—bảng 14.28 cho thấy bước nhảy vọt)
from ad hoc to scalable is primarily an architectural shift from isolated scripts to a cohesive system. (từ ad hoc sang có thể mở rộng (scalable) chủ yếu là một sự thay đổi kiến trúc từ các kịch bản bị cô lập sang một hệ thống gắn kết.)

Table 14.28: Maturity Progression: Machine learning operational practices evolve from manual, fragile workflows toward fully (Bảng 14.28: Tiến trình trưởng thành: Các thực tiễn vận hành học máy tiến hóa từ các quy trình làm việc thủ công, dễ vỡ hướng tới)
integrated, automated systems, impacting reproducibility and scalability. Key characteristics and outcomes at each maturity (các hệ thống tự động, được tích hợp đầy đủ, tác động đến khả năng tái tạo và khả năng mở rộng. Các đặc điểm chính và kết quả ở mỗi mức độ trưởng thành)
level emphasize architectural cohesion and lifecycle integration for building maintainable learning systems. (nhấn mạnh sự gắn kết kiến trúc và sự tích hợp vòng đời cho việc xây dựng các hệ thống học máy có thể bảo trì.)

Maturity Level (Mức độ trưởng thành)
System Characteristics (Đặc điểm hệ thống)
Typical Outcomes (Kết quả điển hình)
Ad Hoc (Đặc biệt)
Manual data processing, local training, no version (Xử lý dữ liệu thủ công, huấn luyện cục bộ, không có kiểm soát)
control, unclear ownership (phiên bản, quyền sở hữu không rõ ràng)
Fragile workflows, difficult to (Các quy trình dễ vỡ, khó khăn để)
reproduce or debug (tái tạo hoặc gỡ lỗi)
Repeatable (Có thể lặp lại)
Automated training pipelines, basic CI/CD, (Các đường ống huấn luyện tự động, CI/CD cơ bản,)
centralized model storage, some monitoring (lưu trữ mô hình tập trung, một số giám sát)
Improved reproducibility, limited (Cải thiện khả năng tái tạo, hạn chế)
scalability (khả năng mở rộng)
Scalable (Có thể mở rộng)
Fully automated workflows, integrated (Các quy trình hoàn toàn tự động, tích hợp)
observability, infrastructure-as-code, governance (khả năng quan sát (observability), cơ sở hạ tầng dưới dạng mã, quản trị)
High reliability, rapid iteration, (Độ tin cậy cao, lặp lại nhanh chóng,)
production-grade ML (ML cấp độ sản xuất)

Consider how a fraud detection system evolves across these maturity levels: (Hãy xem xét cách một hệ thống phát hiện gian lận tiến hóa xuyên suốt các mức độ trưởng thành này:)

820
14.6 Design and Maturity Framework (14.6 Khung thiết kế và sự trưởng thành)
• Ad hoc: A data scientist trains a model in a Jupyter notebook, exports it as a pickle file, and (• Ad hoc (Đặc biệt): Một nhà khoa học dữ liệu huấn luyện một mô hình trong một sổ tay Jupyter, xuất nó như một tệp pickle, và)
hands it to an engineer who deploys it to a single server. When accuracy drops, the data (giao nó cho một kỹ sư người mà triển khai nó tới một máy chủ đơn lẻ. Khi độ chính xác giảm, nhà khoa học)
scientist retrains manually by running the notebook again with fresh data. Debugging requires (dữ liệu huấn luyện lại thủ công bằng cách chạy sổ tay lại với dữ liệu mới. Việc gỡ lỗi đòi hỏi)
the original data scientist because no one else understands the preprocessing steps. (nhà khoa học dữ liệu gốc vì không ai khác hiểu các bước tiền xử lý.)
• Repeatable: The training script is version-controlled, with a scheduled Jenkins job that retrains (• Có thể lặp lại: Kịch bản huấn luyện được kiểm soát phiên bản, với một công việc Jenkins được lập lịch cái mà huấn luyện lại)
monthly. Features are computed in a SQL script that engineering maintains separately. The (hàng tháng. Các đặc trưng được tính toán trong một kịch bản SQL mà bộ phận kỹ thuật duy trì riêng biệt. Mô hình)
model is deployed via container, with basic accuracy monitoring. When the feature SQL (được triển khai thông qua container, với sự giám sát độ chính xác cơ bản. Khi kịch bản SQL đặc trưng)
changes, the data scientist must manually verify the model still works. (thay đổi, nhà khoa học dữ liệu phải xác minh thủ công mô hình vẫn hoạt động.)
• Scalable: Training and serving use the same feature store, eliminating skew. A CI/CD pipeline (• Có thể mở rộng: Quá trình huấn luyện và phục vụ sử dụng cùng một cửa hàng đặc trưng (feature store), loại bỏ sự lệch. Một đường ống CI/CD)
automatically retrains when drift exceeds PSI > 0.2, validates the new model against the (tự động huấn luyện lại khi độ trôi vượt quá PSI > 0.2, xác thực mô hình mới chống lại)
baseline, and deploys via canary release. Monitoring tracks per-merchant accuracy, triggering (đường cơ sở (baseline), và triển khai thông qua phát hành canary. Việc giám sát theo dõi độ chính xác theo từng người bán, kích hoạt)
investigation when specific segments degrade. The entire lineage from raw data to production (sự điều tra khi các phân khúc cụ thể suy thoái. Toàn bộ dòng dõi (lineage) từ dữ liệu thô đến dự đoán trên môi trường sản xuất)
prediction is auditable. (là có thể kiểm toán được.)

The investment required to move between levels is substantial and often spans months of engi- (Sự đầu tư yêu cầu để di chuyển giữa các mức độ là đáng kể và thường kéo dài nhiều tháng nỗ lực)
neering effort, but the reduction in incident frequency and debugging time can justify the cost for (kỹ thuật, nhưng sự giảm thiểu tần suất sự cố và thời gian gỡ lỗi có thể biện minh cho chi phí đối với)
production-critical systems. (các hệ thống quan trọng trong môi trường sản xuất.)

These maturity levels provide a systems lens through which to evaluate ML operations, not (Các mức độ trưởng thành này cung cấp một lăng kính hệ thống thông qua đó để đánh giá các hoạt động ML, không)
in terms of specific tools adopted, but in how reliably and cohesively a system supports the full (về mặt các công cụ cụ thể được áp dụng, mà là ở cách một hệ thống hỗ trợ toàn bộ)
machine learning lifecycle. Understanding this progression prepares practitioners to identify design (vòng đời học máy một cách đáng tin cậy và gắn kết như thế nào. Việc hiểu tiến trình này chuẩn bị cho các người thực hành để xác định các)
bottlenecks and prioritize investments that support long-term system sustainability. (điểm nghẽn (bottlenecks) thiết kế và ưu tiên các khoản đầu tư hỗ trợ sự bền vững lâu dài của hệ thống.)

14.6.2 System design implications (14.6.2 Những hàm ý thiết kế hệ thống)
Maturity levels describe organizational stages; system design implications describe the architectural (Các mức độ trưởng thành mô tả các giai đoạn của tổ chức; các hàm ý thiết kế hệ thống mô tả các hệ quả)
consequences. At each level, the system architecture evolves in response to new expectations around (kiến trúc. Ở mỗi mức độ, kiến trúc hệ thống tiến hóa để phản ứng với những kỳ vọng mới xoay quanh)
modularity, automation, monitoring, and fault tolerance. (tính mô-đun hóa, tự động hóa, giám sát, và khả năng chịu lỗi.)

In low-maturity environments, ML systems are monolithic: data processing logic embedded (Trong các môi trường có mức độ trưởng thành thấp, các hệ thống ML mang tính nguyên khối (monolithic): logic xử lý dữ liệu được nhúng)
in model code, configurations managed informally, and deployments handled through ad hoc (vào mã mô hình, các cấu hình được quản lý một cách không chính thức, và các đợt triển khai được xử lý thông qua các kịch bản)
scripts. These architectures enable rapid experimentation but lack the separation of concerns needed (ad hoc. Những kiến trúc này cho phép sự thử nghiệm nhanh chóng nhưng thiếu sự phân tách các mối quan tâm cần thiết)
for maintainability or safe iteration. As maturity increases, modular abstractions emerge: feature (cho khả năng bảo trì hoặc sự lặp lại an toàn. Khi sự trưởng thành tăng lên, các sự trừu tượng hóa mô-đun xuất hiện: kỹ thuật)
engineering decouples from model logic, pipelines become declarative, and system boundaries are (đặc trưng (feature engineering) tách rời khỏi logic mô hình, các đường ống trở nên mang tính khai báo, và ranh giới hệ thống được)
enforced through APIs. At high maturity, ML systems exhibit properties of production-grade soft- (thực thi thông qua các API. Ở sự trưởng thành cao, các hệ thống ML thể hiện các thuộc tính của phần mềm cấp độ sản xuất)
ware (stateless services, contract-driven interfaces, environment isolation, and observable execution) ((các dịch vụ phi trạng thái, các giao diện dựa trên hợp đồng, sự cô lập môi trường, và quá trình thực thi có thể quan sát được))
where data, models, and infrastructure co-evolve through closed feedback loops. (nơi dữ liệu, mô hình, và cơ sở hạ tầng cùng tiến hóa thông qua các vòng lặp phản hồi kín.)

Figure 14.10 captures this architectural reality as an iceberg. What stakeholders see (uptime, the (Hình 14.10 nắm bắt thực tế kiến trúc này như một tảng băng trôi. Những gì các bên liên quan (stakeholders) nhìn thấy (thời gian hoạt động (uptime), phần)
visible tip) represents only a fraction of what must work correctly beneath the surface. The hidden (đỉnh có thể nhìn thấy) đại diện chỉ cho một phần nhỏ của những gì phải hoạt động chính xác bên dưới bề mặt. Khối lượng ẩn)
mass below the waterline shows the threats that can sink a system even when it appears healthy: data (bên dưới mực nước cho thấy các mối đe dọa có thể đánh chìm một hệ thống ngay cả khi nó có vẻ khỏe mạnh: độ trôi dữ liệu,)
drift, concept drift, broken pipelines, schema changes, model bias, and underperforming segments. (độ trôi khái niệm, đường ống bị hỏng, các thay đổi lược đồ, độ chệch mô hình (model bias), và các phân khúc hoạt động kém hiệu quả.)
Operational maturity must address all three domains (data health, model health, service health) (Sự trưởng thành vận hành phải giải quyết cả ba miền (sức khỏe dữ liệu, sức khỏe mô hình, sức khỏe dịch vụ))
simultaneously. (một cách đồng thời.)

The three threat categories in the iceberg map to distinct failure mechanisms. Data health threats (Ba loại mối đe dọa trong tảng băng trôi ánh xạ tới các cơ chế thất bại riêng biệt. Các mối đe dọa sức khỏe dữ liệu)
(drift, staleness, and schema changes) erode the statistical assumptions a model was trained on, ((độ trôi, sự cũ kỹ, và sự thay đổi lược đồ) xói mòn các giả định thống kê mà một mô hình đã được huấn luyện dựa vào,)
often without any change to the model itself. Model health threats (accuracy degradation, bias (thường mà không có bất kỳ thay đổi nào đối với chính mô hình. Các mối đe dọa sức khỏe mô hình (sự suy thoái độ chính xác, sự khuếch đại)
amplification, and feedback loops) compound silently because the model continues to produce (độ chệch, và các vòng lặp phản hồi) kết hợp lại một cách âm thầm bởi vì mô hình tiếp tục tạo ra)
outputs that appear well-formed even as their quality decays. Infrastructure health threats (config- (các đầu ra có vẻ định dạng tốt ngay cả khi chất lượng của chúng suy giảm. Các mối đe dọa sức khỏe cơ sở hạ tầng (sự mở rộng)
uration sprawl, pipeline fragmentation, and stale dependencies) undermine reproducibility and (cấu trúc, sự phân mảnh đường ống, và các phụ thuộc cũ kỹ) làm suy yếu khả năng tái tạo và)
recoverability. None of these categories triggers a traditional server-down alert, which is precisely (khả năng phục hồi. Không có thể loại nào trong số này kích hoạt một cảnh báo máy chủ bị sập truyền thống, điều đó chính xác là)
why they persist undetected in low-maturity environments. (lý do tại sao chúng tồn tại mà không bị phát hiện trong các môi trường có sự trưởng thành thấp.)

14.6.3 Design patterns and anti-patterns (14.6.3 Các mẫu thiết kế và các mẫu phản tác dụng (anti-patterns))
The most sophisticated infrastructure fails without the organizational patterns to operate it effec- (Cơ sở hạ tầng tinh vi nhất thất bại nếu không có các mẫu tổ chức để vận hành nó một cách)
tively. A feature store cannot prevent training-serving skew if no one owns the feature definitions; (hiệu quả. Một cửa hàng đặc trưng không thể ngăn chặn sự lệch huấn luyện-phục vụ nếu không ai sở hữu các định nghĩa đặc trưng;)
automated monitoring cannot catch drift if alerts route to the wrong team. As ML systems grow in (việc giám sát tự động không thể bắt được độ trôi nếu các cảnh báo định tuyến đến sai nhóm. Khi các hệ thống ML phát triển về)
complexity, organizational patterns must evolve to match. (sự phức tạp, các mẫu tổ chức phải tiến hóa để phù hợp.)

In mature environments, organizational design emphasizes clear ownership and interface disci- (Trong các môi trường trưởng thành, thiết kế tổ chức nhấn mạnh quyền sở hữu rõ ràng và kỷ luật)
pline. Platform teams may take responsibility for shared infrastructure and CI/CD pipelines while (giao diện. Các nhóm nền tảng có thể chịu trách nhiệm cho cơ sở hạ tầng được chia sẻ và các đường ống CI/CD trong khi)

14. ML Operations
821
UPTIME (THỜI GIAN HOẠT ĐỘNG)
MODEL ACCURACY (ĐỘ CHÍNH XÁC MÔ HÌNH)
DATA DRIFT (SỰ TRÔI DỮ LIỆU)
CONCEPT DRIFT (SỰ TRÔI KHÁI NIỆM)
BROKEN PIPELINES (CÁC ĐƯỜNG ỐNG BỊ HỎNG)
SCHEMA CHANGE (THAY ĐỔI LƯỢC ĐỒ)
MODEL BIAS (ĐỘ CHỆCH MÔ HÌNH)
DATA OUTAGE (SỰ CỐ DỮ LIỆU)
UNDERPERFORMING SEGMENTS (CÁC PHÂN KHÚC HOẠT ĐỘNG KÉM HIỆU QUẢ)
Data health (Sức khỏe dữ liệu)
Model health (Sức khỏe mô hình)
Service health (Sức khỏe dịch vụ)

Figure 14.10: Uptime Dependency Stack: An iceberg visualization where visible service uptime floats above the waterline, (Hình 14.10: Ngăn xếp phụ thuộc thời gian hoạt động: Một hình ảnh minh họa tảng băng trôi nơi thời gian hoạt động của dịch vụ có thể nhìn thấy nổi trên mực nước,)
supported by hidden threats below: model accuracy degradation, data drift, concept drift, broken pipelines, schema changes, (được hỗ trợ bởi các mối đe dọa ẩn bên dưới: sự suy thoái độ chính xác mô hình, sự trôi dữ liệu, sự trôi khái niệm, các đường ống bị hỏng, những thay đổi lược đồ,)
model bias, data outages, and underperforming segments. Labels group these threats into data health, model health, and (độ chệch mô hình, các sự cố dữ liệu, và các phân khúc hoạt động kém hiệu quả. Các nhãn nhóm các mối đe dọa này vào các danh mục sức khỏe dữ liệu, sức khỏe mô hình, và)
service health categories. (sức khỏe dịch vụ.)

31 Bulkhead Pattern: This (31 Mẫu Vách ngăn (Bulkhead Pattern): Mẫu)
pattern partitions system re- (này phân vùng các tài nguyên)
sources to contain failures (hệ thống để chứa đựng các lỗi)
within isolated zones. For iso- (trong các vùng bị cô lập. Đối với việc)
lating experimental models, (cô lập các mô hình thử nghiệm,)
a bulkhead dedicates a fixed (một vách ngăn dành riêng một ngân sách)
compute and memory budget (tính toán và bộ nhớ cố định)
to the new version. This re- (cho phiên bản mới. Sự)
source partition ensures that (phân vùng tài nguyên này đảm bảo rằng)
a catastrophic failure in the ex- (một lỗi thảm khốc trong)
periment, such as a memory (thử nghiệm, chẳng hạn như rò rỉ)
leak, cannot exhaust all avail- (bộ nhớ, không thể làm cạn kiệt tất cả các)
able resources and cause a (tài nguyên có sẵn và gây ra một)
system-wide production out- (sự cố sản xuất)
age. (toàn hệ thống.)

32 Byzantine Fault Toler- (32 Khả năng chịu lỗi Byzantine:)
ance: In ML systems, the clas- (Trong các hệ thống ML, mô hình)
sic Byzantine failure model (lỗi Byzantine cổ điển)
shifts from arbitrary node fail- (chuyển đổi từ các lỗi nút)
ures to “semantic failures,” (tùy ý sang "các lỗi ngữ nghĩa",)
where models produce plau- (nơi mà các mô hình tạo ra các dự đoán)
sible but incorrect predictions (có vẻ hợp lý nhưng không chính xác)
that pass health checks. Un- (những cái vượt qua các cuộc kiểm tra sức khỏe. Không)
like a system crash, these se- (giống như một sự cố hệ thống, những)
mantic failures do not trig- (lỗi ngữ nghĩa này không kích hoạt)
ger availability-focused cir- (các bộ ngắt mạch tập trung vào tính)
cuit breakers, silently cor- (sẵn sàng, ngấm ngầm làm)
rupting application outcomes. (hỏng các kết quả của ứng dụng.)
The strict Byzantine fault- (Kết quả chịu lỗi)
tolerance result requires 3𝑓+ (Byzantine nghiêm ngặt đòi hỏi 3𝑓+)
1 replicas to tolerate 𝑓arbi- (1 bản sao để chịu được 𝑓 lỗi)
trary faults (Lamport et al. (tùy ý (Lamport và cộng sự)
1982); ML ensembles are only (1982); các tập hợp ML (ML ensembles) chỉ là)
an analogy because model er- (một sự tương tự vì các lỗi)
rors can be correlated rather (mô hình có thể tương quan với nhau hơn là)
than independent. (độc lập.)

domain teams focus on model development and business alignment. Interfaces between teams (các nhóm lĩnh vực (domain teams) tập trung vào việc phát triển mô hình và sự liên kết kinh doanh. Các giao diện giữa các nhóm)
(feature definitions, data schemas, and deployment targets) are well-defined and versioned. ((định nghĩa đặc trưng, lược đồ dữ liệu, và các mục tiêu triển khai) được định nghĩa rõ ràng và đánh phiên bản.)

One effective pattern is a centralized MLOps team providing shared services to multiple model (Một mẫu hiệu quả là một nhóm MLOps tập trung cung cấp các dịch vụ được chia sẻ cho nhiều nhóm phát triển)
development groups. Such structures promote consistency and reduce duplicated effort. Alterna- (mô hình. Các cấu trúc như vậy thúc đẩy sự nhất quán và giảm thiểu nỗ lực bị trùng lặp. Thay)
tively, some organizations adopt a federated model, embedding MLOps engineers within product (vào đó, một số tổ chức áp dụng một mô hình liên kết (federated model), nhúng các kỹ sư MLOps vào trong các nhóm)
teams while maintaining a central architectural function for system-wide integration. (sản phẩm trong khi vẫn duy trì một chức năng kiến trúc trung tâm cho sự tích hợp toàn hệ thống.)

Anti-patterns emerge when responsibilities are fragmented. The tool-first approach (adopting (Các mẫu phản tác dụng (anti-patterns) nổi lên khi các trách nhiệm bị phân mảnh. Cách tiếp cận ưu tiên công cụ (áp dụng)
infrastructure tools without first defining processes and roles) results in fragile pipelines and (các công cụ cơ sở hạ tầng mà không định nghĩa trước các quy trình và vai trò) dẫn đến các đường ống dễ vỡ và)
unclear handoffs. Siloed experimentation, where data scientists operate in isolation from production (sự chuyển giao không rõ ràng. Sự thử nghiệm bị cô lập (siloed experimentation), nơi các nhà khoa học dữ liệu hoạt động tách biệt khỏi)
engineers, leads to models that are difficult to deploy or retrain effectively. (các kỹ sư sản xuất, dẫn đến các mô hình khó triển khai hoặc huấn luyện lại một cách hiệu quả.)

Organizational drift presents another challenge: as teams scale, undocumented workflows become (Sự trôi dạt tổ chức (organizational drift) đưa ra một thách thức khác: khi các nhóm mở rộng quy mô, các quy trình làm việc không được ghi chép trở nên)
entrenched and coordination costs increase. Organizational maturity must co-evolve with system (bám rễ và chi phí điều phối tăng lên. Sự trưởng thành của tổ chức phải cùng tiến hóa với sự phức tạp của)
complexity through communication patterns, role definitions, and accountability structures that (hệ thống thông qua các mẫu giao tiếp, định nghĩa vai trò, và các cấu trúc trách nhiệm giải trình cái mà)
reinforce modularity, automation, and observability. (củng cố tính mô-đun hóa, tự động hóa, và khả năng quan sát.)

These organizational patterns must be supported by technical architectures handling the unique (Các mẫu tổ chức này phải được hỗ trợ bởi các kiến trúc kỹ thuật xử lý các thách thức)
reliability challenges of ML systems. MLOps inherits distributed systems challenges but adds com- (về độ tin cậy độc đáo của các hệ thống ML. MLOps thừa hưởng các thách thức của hệ thống phân tán nhưng bổ sung thêm những)
plications through learning components requiring adaptations for probabilistic behavior. Traditional (sự phức tạp thông qua các thành phần học tập đòi hỏi những sự thích ứng cho các hành vi mang tính xác suất. Khả năng chịu)
fault tolerance assumes failures are obvious: a service either responds or it does not. ML systems (lỗi truyền thống giả định rằng các thất bại là hiển nhiên: một dịch vụ hoặc phản hồi hoặc không. Các hệ thống ML)
introduce a third state: responding incorrectly, with no error signal to distinguish bad predictions (giới thiệu một trạng thái thứ ba: phản hồi không chính xác, không có tín hiệu lỗi nào để phân biệt các dự đoán tồi tệ)
from good ones. (khỏi những dự đoán tốt.)

Circuit breaker patterns must account for model-specific failure modes, where prediction accuracy (Các mẫu bộ ngắt mạch phải tính đến các chế độ thất bại cụ thể của mô hình, nơi sự suy thoái độ chính xác)
degradation requires different thresholds than service availability failures. Bulkhead patterns31 (dự đoán đòi hỏi các ngưỡng khác với các lỗi về tính sẵn sàng của dịch vụ. Các mẫu vách ngăn31)
become critical when isolating experimental model versions from production traffic. These patterns (trở nên quan trọng khi cô lập các phiên bản mô hình thử nghiệm khỏi lưu lượng sản xuất. Các mẫu này)
require resource partitioning strategies that prevent resource exhaustion in one model from affecting (đòi hỏi các chiến lược phân vùng tài nguyên ngăn chặn sự cạn kiệt tài nguyên trong một mô hình ảnh hưởng)
others. The Byzantine fault tolerance32 problem takes on new characteristics in MLOps environments, (tới các mô hình khác. Vấn đề khả năng chịu lỗi Byzantine32 mang những đặc điểm mới trong các môi trường MLOps,)
where “Byzantine” behavior includes models producing plausible but incorrect outputs rather than (nơi hành vi "Byzantine" bao gồm các mô hình tạo ra các đầu ra có vẻ hợp lý nhưng không chính xác thay vì)
obvious failures. (những lỗi hiển nhiên.)

Traditional consensus algorithms focus on agreement among correct nodes, but ML systems (Các thuật toán đồng thuận truyền thống tập trung vào sự đồng thuận giữa các nút chính xác, nhưng các hệ thống ML)
require consensus about model correctness when ground truth may be delayed or unavailable. These (yêu cầu sự đồng thuận về tính đúng đắn của mô hình khi sự thật cơ sở (ground truth) có thể bị trì hoãn hoặc không có sẵn. Các)
reliability patterns form the theoretical foundation distinguishing robust MLOps implementations (mẫu độ tin cậy này hình thành nền tảng lý thuyết phân biệt các triển khai MLOps mạnh mẽ)
from fragile ones. (khỏi những cái dễ vỡ.)

14.6.4 Contextualizing MLOps (14.6.4 Bối cảnh hóa MLOps)
Best practices are rarely deployed in pristine environments. Every ML system operates within a (Các thực tiễn tốt nhất hiếm khi được triển khai trong các môi trường nguyên sơ. Mỗi hệ thống ML hoạt động trong một)
specific context that shapes how practices are implemented: physical constraints (edge compute, (bối cảnh cụ thể định hình cách các thực tiễn được triển khai: các ràng buộc vật lý (tính toán ranh giới (edge compute),)

14.6 Design and Maturity Framework (14.6 Khung Thiết kế và Sự Trưởng thành)
power budgets), regulatory requirements (healthcare, finance), or organizational realities (team size, skill distribution). (ngân sách năng lượng), các yêu cầu quy định (chăm sóc sức khỏe, tài chính), hoặc các thực tế tổ chức (quy mô nhóm, phân bổ kỹ năng).)
A standard CI/CD pipeline may be infeasible without direct host access; (Một đường ống CI/CD tiêu chuẩn có thể không khả thi nếu không có quyền truy cập máy chủ trực tiếp;)
monitoring may require indirect signals or on-device anomaly detection; (việc giám sát có thể yêu cầu các tín hiệu gián tiếp hoặc phát hiện bất thường trên thiết bị;)
data collection may be limited by privacy regulations. (việc thu thập dữ liệu có thể bị giới hạn bởi các quy định về quyền riêng tư.)
These adaptations are expressions of maturity under constraint, not departures from the principles. (Những sự thích ứng này là biểu hiện của sự trưởng thành dưới các ràng buộc, không phải là sự xa rời các nguyên tắc.)

At the highest levels of operational maturity, the single-model practices established here become building blocks for larger organizational capabilities. (Ở các mức độ cao nhất của sự trưởng thành vận hành, các thực tiễn cho một mô hình đơn lẻ được thiết lập ở đây trở thành các khối xây dựng cho các khả năng tổ chức lớn hơn.)
Organizations operating many ML nodes simultaneously often consolidate into platform architectures that provide shared infrastructure, centralized governance, and economies of scale. (Các tổ chức vận hành nhiều nút ML đồng thời thường củng cố thành các kiến trúc nền tảng cung cấp cơ sở hạ tầng được chia sẻ, quản trị tập trung, và lợi thế nhờ quy mô.)
The transition from individual ML nodes to platform-scale infrastructure introduces qualitatively different challenges (cross-model resource allocation, system-level observability, fault tolerance for interdependent AI systems) that extend beyond our single-model scope. (Sự chuyển đổi từ các nút ML riêng lẻ sang cơ sở hạ tầng quy mô nền tảng giới thiệu những thách thức khác biệt về chất (phân bổ tài nguyên xuyên mô hình, khả năng quan sát cấp hệ thống, khả năng chịu lỗi cho các hệ thống AI phụ thuộc lẫn nhau) mở rộng vượt ra ngoài phạm vi mô hình đơn lẻ của chúng ta.)
The key insight is that solid ML node practices are prerequisite to platform success: every gap in single-model monitoring, testing, or deployment becomes multiplied across the model portfolio. (Sự hiểu biết sâu sắc then chốt là các thực tiễn vững chắc cho nút ML là điều kiện tiên quyết cho sự thành công của nền tảng: mọi khoảng trống trong việc giám sát, kiểm thử, hoặc triển khai mô hình đơn lẻ đều bị nhân lên trên toàn bộ danh mục mô hình.)

14.6.5 MLOps investment economics (14.6.5 Kinh tế học đầu tư MLOps)
The operational benefits of MLOps become persuasive only when the investment matches the model’s production value. (Các lợi ích hoạt động của MLOps chỉ trở nên thuyết phục khi khoản đầu tư tương xứng với giá trị sản xuất của mô hình.)
For a single ML node, the decision is whether deployment speed, incident reduction, and monitoring coverage justify the operational spend; (Đối với một nút ML đơn lẻ, quyết định là liệu tốc độ triển khai, giảm thiểu sự cố, và phạm vi giám sát có biện minh cho chi tiêu hoạt động hay không;)
for a portfolio, the same economics compound into platform investment. (đối với một danh mục đầu tư, cũng tính kinh tế đó được gộp vào khoản đầu tư nền tảng.)

14.6.5.1 Single-model MLOps investment (14.6.5.1 Đầu tư MLOps cho mô hình đơn lẻ)
For a single production ML system, the first threshold is the annual cost of making the node observable, deployable, and recoverable. (Đối với một hệ thống ML sản xuất đơn lẻ, ngưỡng đầu tiên là chi phí hàng năm để làm cho nút đó có thể quan sát được, có thể triển khai được, và có thể phục hồi được.)
Table 14.29 summarizes the main cost categories: (Bảng 14.29 tóm tắt các danh mục chi phí chính:)

Table 14.29: Single-Model MLOps Investment: Costs for operationalizing one production ML system. (Bảng 14.29: Đầu tư MLOps cho Mô hình Đơn lẻ: Các chi phí cho việc vận hành một hệ thống ML sản xuất.)
Open-source tooling (MLflow, Feast) can reduce software costs; cloud-managed services trade higher unit costs for reduced engineering overhead. (Các công cụ mã nguồn mở (MLflow, Feast) có thể giảm chi phí phần mềm; các dịch vụ được quản lý trên nền tảng đám mây đánh đổi chi phí đơn vị cao hơn để giảm chi phí kỹ thuật (overhead).)

| Component (Thành phần) | Typical Cost (Chi phí Điển hình) | Justification (Lý do) |
|---|---|---|
| CI/CD pipeline setup (Thiết lập đường ống CI/CD) | $10–30K one-time ($10–30K trả một lần) | Reduces deployment time from days to hours (Giảm thời gian triển khai từ nhiều ngày xuống nhiều giờ) |
| Monitoring and alerting (Giám sát và cảnh báo) | $2–10K/year ($2–10K/năm) | Catches degradation before user impact (Phát hiện sự suy thoái trước khi ảnh hưởng đến người dùng) |
| Feature store (basic) (Cửa hàng đặc trưng (cơ bản)) | $5–20K/year ($5–20K/năm) | Eliminates training-serving skew (Loại bỏ độ lệch huấn luyện-phục vụ) |
| Model registry (Sổ đăng ký mô hình) | $0–5K/year ($0–5K/năm) | Enables rollback, audit trails (Cho phép khôi phục, nhật ký kiểm toán) |
| Engineering time (Thời gian Kỹ thuật) | 1–2 FTE-months setup (1–2 tháng nhân lực thiết lập) | Initial automation and integration (Tự động hóa và tích hợp ban đầu) |

14.6.5.2 Single-model ROI calculation (14.6.5.2 Tính toán ROI cho mô hình đơn lẻ)
The return threshold then depends on model criticality: a revenue-facing model can justify more operational spend because avoided incidents and deployment-time savings have measurable value. (Ngưỡng hoàn vốn sau đó phụ thuộc vào mức độ quan trọng của mô hình: một mô hình hướng tới doanh thu có thể biện minh cho chi tiêu hoạt động nhiều hơn bởi vì các sự cố được tránh và tiết kiệm thời gian triển khai có giá trị có thể đo lường được.)
Equation 14.16 formalizes that single-node calculation: (Phương trình 14.16 chính thức hóa tính toán nút đơn lẻ đó:)

Annual ROI = (Incidents Avoided × Avg Incident Cost + Time Savings × Hourly Cost) / Annual MLOps Investment (ROI Hàng năm = (Các sự cố được tránh × Chi phí sự cố trung bình + Tiết kiệm thời gian × Chi phí hàng giờ) / Đầu tư MLOps Hàng năm)
(14.16)

where Incidents Avoided is the count of production failures the tooling prevents per year and Avg Incident Cost is the loss per failure, so their product is the value of avoided incidents; (trong đó Các sự cố được tránh là số lượng các lỗi sản xuất mà bộ công cụ ngăn chặn mỗi năm và Chi phí sự cố trung bình là tổn thất cho mỗi lỗi, do đó tích của chúng là giá trị của các sự cố được tránh;)
Time Savings is the engineer-hours that automation reclaims per year and Hourly Cost is the loaded labor rate, so their product is the value of recovered labor; (Tiết kiệm thời gian là số giờ kỹ sư mà tự động hóa lấy lại mỗi năm và Chi phí hàng giờ là tỷ lệ lao động đã tải, do đó tích của chúng là giá trị của lao động được phục hồi;)
the denominator is the annual cost of the tooling itself. (mẫu số là chi phí hàng năm của chính bộ công cụ đó.)
The ratio expresses every dollar of investment in dollars returned. (Tỷ lệ này biểu thị mỗi đô la đầu tư bằng số đô la thu lại được.)

For a model generating $1M annual revenue with: (Đối với một mô hình tạo ra doanh thu hàng năm 1 triệu đô la với:)
• 4 incidents/year avoided (at $25K each) = $100K saved (4 sự cố/năm được ngăn chặn (mỗi sự cố trị giá 25 nghìn đô la) = tiết kiệm được 100 nghìn đô la)
• 20 hours/month deployment time saved (at $150/hr) = $36K saved (Tiết kiệm 20 giờ/tháng thời gian triển khai (với mức 150 đô la/giờ) = tiết kiệm được 36 nghìn đô la)
• MLOps investment of $30K/year (Đầu tư MLOps là 30 nghìn đô la/năm)

ROI = ($100K + $36K) / $30K = 4.5×

================ PAGE 861 ================

14. ML Operations (14. Vận hành ML)
823

14.6.5.3 When to invest more (14.6.5.3 Khi nào cần đầu tư thêm)
The 4.5× return means the investment is not justified by tooling elegance; it is justified because the model is expensive enough that preventing incidents and shortening deployments outweigh the annual platform spend. (Tỷ suất lợi nhuận 4.5× có nghĩa là khoản đầu tư không được biện minh bởi sự thanh lịch của công cụ; nó được biện minh vì mô hình đủ đắt giá để việc ngăn chặn các sự cố và rút ngắn thời gian triển khai vượt xa chi tiêu nền tảng hàng năm.)
The returns from single-model MLOps practices compound when teams add additional models. (Lợi nhuận từ các thực tiễn MLOps cho một mô hình đơn lẻ cộng gộp lại khi các nhóm bổ sung thêm các mô hình mới.)
The transition from operating several independent ML nodes to building a centralized platform involves different economics entirely, including shared infrastructure amortization, platform team overhead, and cross-model coordination costs. (Sự chuyển đổi từ việc vận hành một số nút ML độc lập sang xây dựng một nền tảng tập trung liên quan đến các tính toán kinh tế hoàn toàn khác biệt, bao gồm khấu hao cơ sở hạ tầng được chia sẻ, chi phí chung của nhóm nền tảng, và chi phí điều phối xuyên mô hình.)

For single-model operations, the key insight is: invest in MLOps proportional to model criticality. (Đối với các hoạt động của mô hình đơn lẻ, sự hiểu biết sâu sắc then chốt là: đầu tư vào MLOps tỷ lệ thuận với mức độ quan trọng của mô hình.)
A model driving $10M in annual revenue justifies more operational rigor than an internal analytics model. (Một mô hình mang lại 10 triệu đô la doanh thu hàng năm biện minh cho sự chặt chẽ trong vận hành nhiều hơn so với một mô hình phân tích nội bộ.)
Start with monitoring and CI/CD (highest ROI), then add feature stores and automated retraining as the model matures. (Bắt đầu với việc giám sát và CI/CD (ROI cao nhất), sau đó thêm các cửa hàng đặc trưng (feature stores) và huấn luyện lại tự động khi mô hình trưởng thành.)

The preceding technical infrastructure and economic framework provide the foundation; the case studies that follow demonstrate how these elements combine in production systems. (Cơ sở hạ tầng kỹ thuật và khuôn khổ kinh tế trước đó cung cấp nền tảng; các nghiên cứu tình huống tiếp theo chứng minh cách các yếu tố này kết hợp với nhau trong các hệ thống sản xuất.)
Each case demonstrates specific implementations of the five foundational principles, identifying where reproducibility appears, how observable degradation is achieved, and what triggers automation. (Mỗi tình huống chứng minh các triển khai cụ thể của năm nguyên tắc nền tảng, xác định vị trí mà khả năng tái lập xuất hiện, cách thức đạt được sự suy thoái có thể quan sát được, và điều gì kích hoạt tự động hóa.)

14.7 Case Studies (14.7 Nghiên cứu Tình huống)
A battery-powered sleep-tracking ring and AI/ML-based medical software governed by FDA lifecycle expectations (U.S. Food and Drug Administration 2021) face different operational constraints. (Một chiếc nhẫn theo dõi giấc ngủ chạy bằng pin và phần mềm y tế dựa trên AI/ML được quản lý bởi các kỳ vọng về vòng đời của FDA (Cục Quản lý Thực phẩm và Dược phẩm Hoa Kỳ 2021) đối mặt với các ràng buộc vận hành khác nhau.)
The principles, patterns, and infrastructure examined throughout this chapter converge differently depending on the deployment context. (Các nguyên tắc, mẫu hình, và cơ sở hạ tầng được xem xét trong suốt chương này hội tụ khác nhau tùy thuộc vào bối cảnh triển khai.)
We examine two cases: the Oura Ring, where pipeline debt and configuration management challenge resource-constrained edge environments, and ClinAIOps, where feedback loops and governance requirements drive specialized healthcare operations. (Chúng ta xem xét hai trường hợp: Oura Ring, nơi nợ đường ống (pipeline debt) và quản lý cấu hình thách thức các môi trường ranh giới (edge) bị hạn chế về tài nguyên, và ClinAIOps, nơi các vòng phản hồi và yêu cầu quản trị thúc đẩy các hoạt động chăm sóc sức khỏe chuyên biệt.)
The comparison starts with the shared principles, because the domains differ most in how those principles are implemented. (Sự so sánh bắt đầu bằng các nguyên tắc chung, bởi vì các lĩnh vực khác biệt nhất ở cách các nguyên tắc đó được triển khai.)

Table 14.30 lays out how the two environments implement the five foundational MLOps principles. (Bảng 14.30 trình bày cách hai môi trường triển khai năm nguyên tắc MLOps nền tảng.)
Domain constraints (edge hardware, clinical regulation) reshape how each principle is realized without changing which principles matter. (Các ràng buộc của lĩnh vực (phần cứng ranh giới, quy định lâm sàng) định hình lại cách mỗi nguyên tắc được hiện thực hóa mà không thay đổi những nguyên tắc nào là quan trọng.)
In the Oura case, polysomnography (PSG) refers to the clinical sleep-study measurements used as the reference labels. (Trong trường hợp Oura, polysomnography (PSG) hay đa ký giấc ngủ đề cập đến các phép đo nghiên cứu giấc ngủ lâm sàng được sử dụng làm các nhãn tham chiếu.)

Table 14.30: MLOps principles by case study: Side-by-side implementation of the five foundational MLOps principles in the Oura Ring and ClinAIOps deployments, showing how domain constraints reshape how each principle is realized without changing which principles apply. (Bảng 14.30: Các nguyên tắc MLOps theo nghiên cứu tình huống: Việc triển khai song song năm nguyên tắc MLOps nền tảng trong các triển khai Oura Ring và ClinAIOps, cho thấy cách các ràng buộc của lĩnh vực định hình lại cách hiện thực hóa mỗi nguyên tắc mà không làm thay đổi các nguyên tắc được áp dụng.)

| Principle (Nguyên tắc) | Oura Ring | ClinAIOps |
|---|---|---|
| Reproducibility (Khả năng tái lập) | Versioned synchronized wearable and PSG datasets (Các bộ dữ liệu đồng bộ thiết bị đeo và PSG được đánh phiên bản) | Audit trails, decision provenance (Nhật ký kiểm toán, nguồn gốc quyết định) |
| Separation of concerns (Tách biệt các mối quan tâm) | Independent data, training, and serving layers with edge-specific deployment pipeline (Các tầng dữ liệu, huấn luyện, và phục vụ độc lập với đường ống triển khai dành riêng cho thiết bị ranh giới) | Distinct clinical validation and deployment stages with regulatory compliance isolation (Các giai đoạn xác thực và triển khai lâm sàng riêng biệt với sự cô lập tuân thủ quy định) |
| Consistency (Tính nhất quán) | PSG-aligned preprocessing across training and on-device inference (Tiền xử lý căn chỉnh theo PSG xuyên suốt quá trình huấn luyện và suy luận trên thiết bị) | Standardized clinical data pipelines ensuring training-serving parity (Các đường ống dữ liệu lâm sàng được tiêu chuẩn hóa đảm bảo tính ngang giá giữa huấn luyện-phục vụ) |
| Observable degradation (Sự suy thoái có thể quan sát được) | On-device anomaly detection, limited telemetry (Phát hiện bất thường trên thiết bị, đo từ xa hạn chế) | Cohort-specific monitoring, outcome tracking (Giám sát đặc thù theo thuần tập (cohort), theo dõi kết quả) |
| Cost-aware automation (Tự động hóa nhận thức chi phí) | Battery-aware retraining triggers, CI/CD for edge balancing accuracy and resource cost (Các trình kích hoạt huấn luyện lại nhận thức về pin, CI/CD cho thiết bị ranh giới cân bằng độ chính xác và chi phí tài nguyên) | Automated model updates with human-in-loop gates balancing update cost and patient risk (Các cập nhật mô hình tự động với các cổng con-người-trong-vòng-lặp cân bằng chi phí cập nhật và rủi ro cho bệnh nhân) |

The principles stay stable, but their implementation changes with the deployment regime. (Các nguyên tắc vẫn ổn định, nhưng việc triển khai chúng thay đổi theo chế độ triển khai.)
Edge systems spend the automation budget on battery, telemetry, and constrained updates; (Các hệ thống ranh giới dành ngân sách tự động hóa cho pin, đo lường từ xa, và các bản cập nhật bị hạn chế;)
clinical systems spend it on auditability, validation gates, and accountable human control. (các hệ thống lâm sàng dành ngân sách cho khả năng kiểm toán, các cổng xác thực, và sự kiểm soát có trách nhiệm của con người.)
The two case studies that follow trace how each environment earns those entries. (Hai nghiên cứu tình huống sau đây theo dõi cách mỗi môi trường đạt được các khoản mục đó.)

14.7.1 Oura Ring case study (14.7.1 Nghiên cứu tình huống Oura Ring)
The Oura Ring exemplifies MLOps practices applied to consumer wearable devices, where embedded ML must operate under strict resource constraints while delivering accurate health insights. (Oura Ring minh họa các thực tiễn MLOps được áp dụng cho các thiết bị đeo của người tiêu dùng, nơi ML nhúng phải hoạt động dưới các ràng buộc tài nguyên nghiêm ngặt trong khi cung cấp các thông tin chi tiết chính xác về sức khỏe.)
This case study traces the full operational lifecycle—from the clinical data collection that established (Nghiên cứu tình huống này theo dõi toàn bộ vòng đời vận hành—từ việc thu thập dữ liệu lâm sàng để thiết lập)

================ PAGE 862 ================

824
14.7 Case Studies (14.7 Nghiên cứu Tình huống)
33 Polysomnography (PSG): A multi-parameter sleep study that provides the clinical ground truth data for this classification task. (33 Polysomnography (PSG) (Đa ký giấc ngủ): Một nghiên cứu giấc ngủ đa thông số cung cấp dữ liệu sự thật cơ sở lâm sàng cho tác vụ phân loại này.)
This ‘truth’ is inherently noisy; expert human scorers interpreting the same PSG recordings agree with each other at about 82 percent–83 percent reliability. (Sự 'thật' này về bản chất là nhiễu; các chuyên gia chấm điểm con người diễn giải cùng một bản ghi PSG đồng ý với nhau ở độ tin cậy khoảng 82%–83%.)
This inter-rater agreement establishes a practical accuracy ceiling, framing the Oura study’s 57 percent accelerometer-only baseline and 79 percent enhanced model as a meaningful but still imperfect approach to clinical sleep staging. (Sự đồng thuận giữa những người đánh giá này thiết lập một mức trần độ chính xác thực tế, định hình đường cơ sở 57% chỉ dùng gia tốc kế của nghiên cứu Oura và 79% cho mô hình nâng cao như một phương pháp tiếp cận có ý nghĩa nhưng vẫn chưa hoàn hảo đối với việc phân giai đoạn giấc ngủ lâm sàng.)
34 Over-the-Air (OTA) Updates: The mechanism used to deploy optimized models to devices already in the field, bypassing the need for physical access. (34 Cập nhật Qua không trung (Over-the-Air - OTA): Cơ chế được sử dụng để triển khai các mô hình được tối ưu hóa tới các thiết bị đã hoạt động thực tế, bỏ qua nhu cầu truy cập vật lý.)
The small footprint from quantization and pruning matters because constrained edge networks may need to transmit only changed model artifacts rather than complete application bundles. (Dấu chân nhỏ từ việc lượng tử hóa và cắt tỉa (pruning) rất quan trọng bởi vì các mạng ranh giới bị ràng buộc có thể chỉ cần truyền đi các hiện vật (artifacts) mô hình đã bị thay đổi thay vì toàn bộ các gói ứng dụng hoàn chỉnh.)
This process makes consistency a critical concern; a failed update can corrupt the on-device model, breaking the ML pipeline until a future connectivity window allows for a fix. (Quá trình này biến tính nhất quán thành một mối quan tâm quan trọng; một bản cập nhật thất bại có thể làm hỏng mô hình trên thiết bị, phá vỡ đường ống ML cho đến khi một cửa sổ kết nối trong tương lai cho phép sửa chữa.)

ground truth, through the model development process that improved sleep stage classification, to the over-the-air deployment pipeline and iterative refinement cycle that sustains the system in production. (sự thật cơ sở, thông qua quá trình phát triển mô hình nhằm cải thiện việc phân loại giai đoạn giấc ngủ, tới đường ống triển khai qua không trung và chu trình tinh chỉnh lặp đi lặp lại nhằm duy trì hệ thống trong sản xuất.)
The constraints imposed by a battery-powered ring with limited compute make every MLOps decision visible in a way that cloud-scale systems can obscure. (Các ràng buộc bị áp đặt bởi một chiếc nhẫn chạy bằng pin với khả năng tính toán hạn chế làm cho mọi quyết định MLOps trở nên rõ ràng theo cách mà các hệ thống quy mô đám mây có thể che khuất.)

14.7.1.1 Context and motivation (14.7.1.1 Bối cảnh và động lực)
The Oura Ring is a consumer-grade wearable monitoring sleep, activity, and physiological recovery through embedded sensing and computation. (Oura Ring là một thiết bị đeo cấp độ tiêu dùng theo dõi giấc ngủ, hoạt động, và sự phục hồi sinh lý thông qua cảm biến và tính toán nhúng.)
By measuring motion, heart rate, and body temperature, the device estimates sleep stages and delivers personalized feedback. (Bằng cách đo chuyển động, nhịp tim, và nhiệt độ cơ thể, thiết bị ước tính các giai đoạn giấc ngủ và cung cấp phản hồi cá nhân hóa.)
Unlike traditional cloud-based systems, much of the data processing and inference occurs directly on the device. (Không giống như các hệ thống dựa trên đám mây truyền thống, phần lớn quá trình xử lý dữ liệu và suy luận diễn ra trực tiếp trên thiết bị.)

The central objective was improving sleep stage classification accuracy to align more closely with polysomnography (PSG)33, the clinical gold standard. (Mục tiêu trung tâm là cải thiện độ chính xác phân loại giai đoạn giấc ngủ để phù hợp chặt chẽ hơn với polysomnography (PSG)33, tiêu chuẩn vàng lâm sàng.)
Initial evaluations showed 57 percent four-stage sleep classification accuracy for an accelerometer-only model, compared with 79 percent for models that included autonomic nervous system and circadian features. (Các đánh giá ban đầu cho thấy 57% độ chính xác phân loại giấc ngủ bốn giai đoạn cho một mô hình chỉ dùng gia tốc kế, so với 79% cho các mô hình bao gồm hệ thần kinh tự chủ và các đặc trưng nhịp sinh học.)
Published human PSG inter-scorer reliability is about 82 percent to 83 percent, framing the remaining gap between wearable inference and expert clinical scoring. (Độ tin cậy giữa những người chấm điểm PSG con người được công bố là khoảng 82% đến 83%, định khung khoảng cách còn lại giữa suy luận trên thiết bị đeo và đánh giá lâm sàng chuyên gia.)
The 22 percentage-point gain closes roughly 84.6–88 percent of the baseline-to-human-agreement gap, so the remaining improvement target is real but bounded by the noisiness of the clinical reference itself. (Mức tăng 22 điểm phần trăm thu hẹp khoảng 84.6–88% khoảng cách từ đường cơ sở đến thỏa thuận của con người, do đó mục tiêu cải thiện còn lại là có thực nhưng bị giới hạn bởi tính nhiễu của chính tham chiếu lâm sàng.)
This discrepancy prompted an effort to re-evaluate data collection, preprocessing, and model development workflows. (Sự khác biệt này đã thúc đẩy nỗ lực đánh giá lại quy trình thu thập dữ liệu, tiền xử lý và phát triển mô hình.)

To overcome performance limitations, the Oura team constructed a diverse dataset grounded in clinical standards through a study involving 106 participants from three continents (Altini and Kinnunen 2021). (Để vượt qua những hạn chế về hiệu suất, nhóm Oura đã xây dựng một bộ dữ liệu đa dạng dựa trên các tiêu chuẩn lâm sàng thông qua một nghiên cứu bao gồm 106 người tham gia từ ba lục địa (Altini và Kinnunen 2021).)
Each participant wore the Oura Ring while simultaneously undergoing PSG, yielding 440 nights of data and 3,444 hours of time-synchronized recordings that aligned wearable sensor data with validated sleep annotations. (Mỗi người tham gia đeo Oura Ring đồng thời trải qua PSG, tạo ra 440 đêm dữ liệu và 3,444 giờ bản ghi được đồng bộ thời gian căn chỉnh dữ liệu cảm biến trên thiết bị đeo với các chú thích giấc ngủ đã được xác thực.)
The scale and diversity of the collection captured physiological variation as well as environmental and behavioral factors critical for generalizing across a real-world user base. (Quy mô và sự đa dạng của bộ thu thập đã nắm bắt sự biến đổi sinh lý cũng như các yếu tố môi trường và hành vi quan trọng để tổng quát hóa trên một cơ sở người dùng trong thế giới thực.)

The study consolidated synchronized accelerometer, temperature, heart-rate, heart-rate-variability, and PSG data from research Oura rings, then resolved temporal alignment and preprocessing requirements for downstream model development. (Nghiên cứu đã củng cố các dữ liệu gia tốc kế, nhiệt độ, nhịp tim, sự thay đổi nhịp tim và PSG được đồng bộ hóa từ các vòng Oura nghiên cứu, sau đó giải quyết việc căn chỉnh thời gian và các yêu cầu tiền xử lý cho việc phát triển mô hình hạ nguồn (downstream).)
These workflows address data dependency debt patterns by emphasizing robust versioning and lineage tracking, avoiding unstable dependencies that commonly plague embedded ML systems. (Các quy trình làm việc này giải quyết các mẫu nợ phụ thuộc dữ liệu bằng cách nhấn mạnh việc quản lý phiên bản (versioning) mạnh mẽ và theo dõi nguồn gốc (lineage tracking), tránh các phụ thuộc không ổn định thường gây rắc rối cho các hệ thống ML nhúng.)

With high-quality data in place, the next operational question was whether extra sensing justified its cost on the device. (Với dữ liệu chất lượng cao đã có sẵn, câu hỏi vận hành tiếp theo là liệu việc cảm biến bổ sung có biện minh cho chi phí của nó trên thiết bị hay không.)
The team developed models classifying sleep stages under the ring’s limited memory and compute budget, so model design had to prioritize efficiency alongside predictive accuracy. (Nhóm đã phát triển các mô hình phân loại các giai đoạn giấc ngủ dưới ngân sách bộ nhớ và tính toán hạn chế của chiếc nhẫn, do đó thiết kế mô hình phải ưu tiên hiệu quả bên cạnh độ chính xác dự đoán.)
The team explored two configurations: one using only accelerometer data for minimal energy consumption, and another incorporating heart rate variability and body temperature to capture autonomic nervous system activity and circadian rhythms. (Nhóm đã khám phá hai cấu hình: một cấu hình chỉ sử dụng dữ liệu gia tốc kế để tiêu thụ năng lượng tối thiểu, và một cấu hình khác kết hợp sự thay đổi nhịp tim và nhiệt độ cơ thể để nắm bắt hoạt động của hệ thần kinh tự chủ và nhịp sinh học.)
Through 5-fold cross-validation against PSG annotations and iterative tuning, the enhanced models achieved 79 percent four-stage classification accuracy, a significant improvement from the 57 percent accelerometer-only baseline toward the clinical benchmark. (Thông qua kiểm chứng chéo 5 lần đối với các chú thích PSG và tinh chỉnh lặp đi lặp lại, các mô hình nâng cao đã đạt được độ chính xác phân loại bốn giai đoạn là 79%, một sự cải thiện đáng kể so với mức cơ sở 57% chỉ dành cho gia tốc kế hướng tới điểm chuẩn lâm sàng.)
These gains reflect the broader impact of an MLOps approach integrating data collection, reproducible training pipelines, and disciplined evaluation: (Những mức tăng này phản ánh tác động rộng lớn hơn của phương pháp tiếp cận MLOps tích hợp thu thập dữ liệu, các đường ống huấn luyện có thể tái lập và đánh giá có kỷ luật:)
structured documentation and version control of model parameters avoided the fragmented settings that often undermine embedded ML deployments, while requiring close collaboration among data scientists, ML engineers, and DevOps engineers. (tài liệu có cấu trúc và kiểm soát phiên bản của các tham số mô hình đã tránh được các cài đặt bị phân mảnh thường làm suy yếu các đợt triển khai ML nhúng, đồng thời đòi hỏi sự hợp tác chặt chẽ giữa các nhà khoa học dữ liệu, kỹ sư ML và kỹ sư DevOps.)

Following validation, deployment shifted the problem from model quality to update safety. (Sau khi xác thực, quá trình triển khai đã chuyển vấn đề từ chất lượng mô hình sang sự an toàn của bản cập nhật.)
An Oura-like edge deployment must decide which parts of the model run continuously on-device, which richer signals can be used under looser memory and battery budgets, and how model updates reach devices already in the field. (Một bản triển khai ranh giới (edge) giống Oura phải quyết định phần nào của mô hình chạy liên tục trên thiết bị, tín hiệu phong phú hơn nào có thể được sử dụng dưới ngân sách bộ nhớ và pin lỏng lẻo hơn, và cách cập nhật mô hình đến các thiết bị đã có mặt trên thị trường.)
To keep that split maintainable, the operational toolchain needs reproducible model conversion, versioned artifacts, and over-the-air (OTA)34 update procedures that preserve consistency across devices in the field. (Để giữ cho sự phân chia đó có thể duy trì được, chuỗi công cụ vận hành cần khả năng chuyển đổi mô hình có thể tái lập, các hiện vật (artifacts) được đánh phiên bản, và các thủ tục cập nhật qua không trung (OTA)34 duy trì tính nhất quán trên các thiết bị trên thị trường.)

The operational lesson is that edge MLOps is not governed by accuracy alone; it is governed by accuracy under battery, privacy, telemetry, and weak ground truth constraints. (Bài học vận hành là MLOps ranh giới không chỉ được chi phối bởi độ chính xác; nó được chi phối bởi độ chính xác dưới các ràng buộc về pin, quyền riêng tư, đo lường từ xa và sự thật cơ sở yếu.)
Consider the DS-CNN (Tiny Constraint) archetype from table 14.4, where monitoring relies on operational metrics such as duty cycle and false positive rate rather than continuous ground-truth labels, and retraining occurs quarterly through OTA updates. (Hãy xem xét nguyên mẫu DS-CNN (Ràng buộc Nhỏ - Tiny Constraint) từ Bảng 14.4, nơi việc giám sát phụ thuộc vào các số liệu vận hành như chu kỳ hoạt động và tỷ lệ dương tính giả hơn là các nhãn sự thật cơ sở liên tục, và việc huấn luyện lại diễn ra hàng quý thông qua các bản cập nhật OTA.)
The transition from 57 percent accelerometer-only accuracy (Sự chuyển đổi từ độ chính xác 57% chỉ dành cho gia tốc kế)

================ PAGE 863 ================

14. ML Operations (14. Vận hành ML)
825

35 Continuous Therapeutic Monitoring (CTM): Healthcare approach using wearable sensors for real-time physiological data collection and personalized treatment adjustments. (35 Giám sát Trị liệu Liên tục (CTM): Cách tiếp cận chăm sóc sức khỏe sử dụng cảm biến đeo trên người để thu thập dữ liệu sinh lý theo thời gian thực và điều chỉnh phương pháp điều trị cá nhân hóa.)
CTM forces MLOps to confront constraints absent in typical deployments: (CTM buộc MLOps phải đối mặt với các ràng buộc vắng mặt trong các triển khai điển hình:)
feedback loops must include human-in-the-loop approval for safety-critical decisions, (các vòng phản hồi phải bao gồm sự phê duyệt của con-người-trong-vòng-lặp cho các quyết định an toàn quan trọng,)
retraining requires clinician-validated labels rather than implicit signals, and model updates must satisfy regulatory compliance before deployment. (việc huấn luyện lại đòi hỏi các nhãn được bác sĩ lâm sàng xác thực hơn là các tín hiệu ngầm hiểu, và cập nhật mô hình phải đáp ứng sự tuân thủ quy định trước khi triển khai.)
These constraints reshape every MLOps principle, making CTM a stress test for operational maturity. (Những ràng buộc này định hình lại mọi nguyên tắc MLOps, khiến CTM trở thành một bài kiểm tra áp lực đối với mức độ trưởng thành hoạt động.)

to 79 percent multi-sensor accuracy required systematic configuration management across data collection, feature sets, model architectures, and deployment targets. (lên 79% độ chính xác đa cảm biến đòi hỏi quản lý cấu hình có hệ thống xuyên suốt việc thu thập dữ liệu, các tập đặc trưng, kiến trúc mô hình và các mục tiêu triển khai.)

Those constraints explain how the foundational principles appear without repeating them as a checklist. (Những ràng buộc đó giải thích cách thức các nguyên tắc nền tảng xuất hiện mà không cần lặp lại chúng như một danh sách kiểm tra.)
Versioned wearable and PSG datasets make each model traceable to the evidence used to train it. (Các bộ dữ liệu PSG và thiết bị đeo được quản lý phiên bản làm cho mỗi mô hình có thể truy xuất nguồn gốc đến bằng chứng được sử dụng để huấn luyện nó.)
Modular tiered architectures keep data collection, model training, and on-device serving separate enough that quantization, pruning, and fallback policies can change without destabilizing the whole pipeline. (Các kiến trúc phân tầng dạng mô-đun giữ cho việc thu thập dữ liệu, huấn luyện mô hình và phục vụ trên thiết bị đủ tách biệt để lượng tử hóa, cắt tỉa (pruning) và các chính sách dự phòng có thể thay đổi mà không làm mất ổn định toàn bộ đường ống.)
PSG-aligned preprocessing preserves consistency between training and on-device inference, while privacy-preserving telemetry makes degradation observable through duty cycle, battery impact, inference failures, confidence, anomaly rates, and periodic labeled studies. (Quá trình tiền xử lý được căn chỉnh theo PSG duy trì tính nhất quán giữa việc huấn luyện và suy luận trên thiết bị, trong khi phép đo từ xa bảo vệ quyền riêng tư giúp cho sự suy thoái có thể quan sát được thông qua chu kỳ hoạt động, tác động đến pin, lỗi suy luận, độ tin cậy, tỷ lệ bất thường và các nghiên cứu có nhãn định kỳ.)
OTA deployment then becomes the cost-aware automation boundary: updates must justify their accuracy gain against battery impact, validation burden, and the risk of changing software on a device worn continuously by users. (Triển khai OTA sau đó trở thành ranh giới tự động hóa nhận thức về chi phí: các bản cập nhật phải chứng minh được mức tăng độ chính xác của chúng so với tác động đến pin, gánh nặng xác thực và rủi ro thay đổi phần mềm trên một thiết bị được người dùng đeo liên tục.)

This case exemplifies how MLOps principles adapt to domain-specific constraints. (Trường hợp này minh họa cách thức các nguyên tắc MLOps thích ứng với các ràng buộc theo từng lĩnh vực cụ thể.)
When machine learning moves into clinical applications, additional complexity emerges, requiring frameworks that address regulatory compliance, patient safety, and clinical decision-making. (Khi học máy chuyển sang các ứng dụng lâm sàng, sự phức tạp bổ sung sẽ xuất hiện, đòi hỏi các khuôn khổ giải quyết sự tuân thủ các quy định, an toàn cho bệnh nhân và ra quyết định lâm sàng.)

14.7.2 ClinAIOps case study (14.7.2 Nghiên cứu tình huống ClinAIOps)
Healthcare ML deployment presents challenges extending beyond resource constraints. (Việc triển khai ML trong chăm sóc sức khỏe đưa ra những thách thức vượt ra ngoài các hạn chế về tài nguyên.)
Traditional MLOps frameworks often fall short in domains requiring extensive human oversight, domain-specific evaluation, and ethical governance. (Các khuôn khổ MLOps truyền thống thường thiếu sót trong các lĩnh vực yêu cầu sự giám sát rộng rãi của con người, đánh giá theo lĩnh vực cụ thể và quản trị đạo đức.)
Continuous therapeutic monitoring (CTM)35 exemplifies a domain where MLOps must evolve to meet clinical integration demands. (Giám sát Trị liệu Liên tục (CTM)35 là một ví dụ điển hình về một lĩnh vực nơi MLOps phải phát triển để đáp ứng các nhu cầu tích hợp lâm sàng.)

CTM uses wearable sensors to collect real-time physiological and behavioral data from patients. (CTM sử dụng cảm biến đeo trên người để thu thập dữ liệu sinh lý và hành vi theo thời gian thực từ bệnh nhân.)
AI systems must be integrated into clinical workflows, aligned with regulatory requirements, and designed to augment rather than replace human decision-making. (Các hệ thống AI phải được tích hợp vào các quy trình lâm sàng, phù hợp với các yêu cầu quy định và được thiết kế để gia tăng cường chứ không phải thay thế việc ra quyết định của con người.)
The traditional MLOps paradigm does not adequately account for patient safety, clinician judgment, and ethical constraints. (Mô hình MLOps truyền thống không tính đến đầy đủ sự an toàn của bệnh nhân, phán đoán của bác sĩ lâm sàng và các rào cản đạo đức.)

ClinAIOps (Chen et al. 2023), a framework for operationalizing AI in clinical environments, shows how MLOps principles must evolve for regulatory and human-centered requirements. (ClinAIOps (Chen và cộng sự. 2023), một khuôn khổ để vận hành AI trong môi trường lâm sàng, cho thấy các nguyên tắc MLOps phải phát triển như thế nào đối với các yêu cầu quy định và lấy con người làm trung tâm.)
Unlike conventional MLOps, ClinAIOps directly addresses feedback loop challenges by designing them into the system architecture. (Không giống như MLOps thông thường, ClinAIOps giải quyết trực tiếp các thách thức về vòng phản hồi bằng cách thiết kế chúng vào kiến trúc hệ thống.)
The framework’s structured coordination between patients, clinicians, and AI developers represents practical implementation of governance and collaboration principles. (Sự điều phối có cấu trúc của khuôn khổ giữa bệnh nhân, bác sĩ lâm sàng và nhà phát triển AI thể hiện việc thực hiện thực tế các nguyên tắc quản trị và hợp tác.)

Standard MLOps falls short in clinical environments because healthcare requires coordination among diverse human actors, clinical decision-making hinges on personalized care and shared accountability, and health data must comply with strict privacy regulations. (MLOps tiêu chuẩn bị thiếu sót trong môi trường lâm sàng bởi vì chăm sóc sức khỏe đòi hỏi sự phối hợp giữa nhiều tác nhân con người đa dạng, việc ra quyết định lâm sàng xoay quanh chăm sóc cá nhân hóa và trách nhiệm chung, đồng thời dữ liệu sức khỏe phải tuân thủ các quy định nghiêm ngặt về quyền riêng tư.)
ClinAIOps presents a framework that balances technical rigor with clinical utility and operational reliability with ethical responsibility. (ClinAIOps trình bày một khuôn khổ cân bằng sự nghiêm ngặt về kỹ thuật với tiện ích lâm sàng và độ tin cậy vận hành với trách nhiệm đạo đức.)

14.7.2.1 Feedback loops (14.7.2.1 Các vòng phản hồi)
Three interlocking feedback loops enable safe, adaptive integration of machine learning into clinical practice. (Ba vòng phản hồi đan xen vào nhau cho phép tích hợp an toàn, thích ứng học máy vào thực hành lâm sàng.)
Figure 14.11 maps these loops as a circular flow among three stakeholders. (Hình 14.11 lập bản đồ các vòng lặp này dưới dạng luồng tuần hoàn giữa ba bên liên quan.)
Patients contribute continuous monitoring data from wearable sensors and receive bounded AI-assisted guidance. (Bệnh nhân đóng góp dữ liệu giám sát liên tục từ các cảm biến đeo trên người và nhận hướng dẫn được AI hỗ trợ có giới hạn.)
Clinicians receive AI-generated summaries, alerts, and recommendations, then apply clinical judgment by setting therapy regimens and approval limits. (Bác sĩ lâm sàng nhận các tóm tắt, cảnh báo và khuyến nghị do AI tạo ra, sau đó áp dụng đánh giá lâm sàng bằng cách thiết lập phác đồ điều trị và giới hạn phê duyệt.)
AI developers receive continuous feedback from patients and clinicians, using real-world performance and workflow signals to improve models and deployment processes. (Các nhà phát triển AI nhận phản hồi liên tục từ bệnh nhân và bác sĩ lâm sàng, sử dụng hiệu suất thực tế và các tín hiệu quy trình làm việc để cải thiện các mô hình và quy trình triển khai.)
The outer loop connecting all three stakeholders represents the full governance cycle. (Vòng lặp bên ngoài kết nối cả ba bên liên quan đại diện cho toàn bộ chu kỳ quản trị.)

Each feedback loop plays a distinct yet interconnected role: (Mỗi vòng phản hồi đóng một vai trò riêng biệt nhưng có liên kết với nhau:)
• The patient treatment loop captures real-time physiological data and uses bounded AI outputs to support patient self-management. (Vòng điều trị bệnh nhân nắm bắt dữ liệu sinh lý theo thời gian thực và sử dụng các đầu ra AI có giới hạn để hỗ trợ bệnh nhân tự quản lý.)
• The clinician oversight loop ensures AI-assisted recommendations are reviewed, limited, and refined under professional supervision. (Vòng giám sát bác sĩ lâm sàng đảm bảo các khuyến nghị được hỗ trợ bởi AI được xem xét, giới hạn và tinh chỉnh dưới sự giám sát chuyên môn.)
• The developer feedback loop gives AI developers continuous feedback from patients and clinicians so models, interfaces, and monitoring workflows can improve. (Vòng phản hồi nhà phát triển cung cấp cho nhà phát triển AI phản hồi liên tục từ bệnh nhân và bác sĩ lâm sàng để các mô hình, giao diện và quy trình giám sát có thể được cải thiện.)

Together, these loops enable adaptive personalization, maintain clinician control, and promote continuous model improvement based on real-world feedback. (Cùng nhau, các vòng lặp này kích hoạt quá trình cá nhân hóa có khả năng thích ứng, duy trì sự kiểm soát của bác sĩ lâm sàng, và thúc đẩy cải tiến mô hình liên tục dựa trên các phản hồi từ thế giới thực.)

================ PAGE 864 ================

826
14.7 Case Studies (14.7 Nghiên cứu Tình huống)

Figure 14.11: ClinAIOps Feedback Loops: The cyclical framework coordinates patients, clinicians, and AI developers to support continuous model improvement and safe clinical integration. (Hình 14.11: Các Vòng phản hồi ClinAIOps: Khuôn khổ theo chu kỳ phối hợp bệnh nhân, bác sĩ lâm sàng và các nhà phát triển AI để hỗ trợ cải tiến mô hình liên tục và tích hợp lâm sàng an toàn.)
Patients and clinicians use AI outputs in care workflows, while AI developers receive feedback from both groups to refine models and operations. Source: (Chen et al. 2023). (Bệnh nhân và bác sĩ lâm sàng sử dụng kết quả đầu ra của AI trong quy trình chăm sóc, trong khi các nhà phát triển AI nhận phản hồi từ cả hai nhóm để tinh chỉnh mô hình và hoạt động. Nguồn: (Chen và cộng sự. 2023).)

Patient treatment loop (Vòng điều trị bệnh nhân) The patient treatment loop enables personalized therapy optimization through continuous physiological data from wearable devices. (Vòng điều trị bệnh nhân cho phép tối ưu hóa liệu pháp cá nhân hóa thông qua dữ liệu sinh lý liên tục từ các thiết bị đeo.)
Patients wear sensors such as continuous glucose monitors or ECG-enabled wearables that passively capture health signals. (Bệnh nhân đeo các cảm biến như màn hình theo dõi lượng đường huyết liên tục hoặc thiết bị đeo có hỗ trợ điện tâm đồ (ECG) ghi lại tín hiệu sức khỏe một cách thụ động.)
The AI system analyzes these data streams alongside clinical context from electronic medical records, generating individualized recommendations for treatment adjustments. (Hệ thống AI phân tích các luồng dữ liệu này cùng với bối cảnh lâm sàng từ hồ sơ y tế điện tử, tạo ra các đề xuất cá nhân hóa để điều chỉnh phương pháp điều trị.)
Treatment suggestions are tiered: minor adjustments within clinician-defined safety thresholds may be acted upon directly by the patient, while significant changes require clinician approval. (Các đề xuất điều trị được phân tầng: những điều chỉnh nhỏ trong ngưỡng an toàn do bác sĩ lâm sàng xác định có thể được bệnh nhân thực hiện trực tiếp, trong khi những thay đổi đáng kể cần sự chấp thuận của bác sĩ lâm sàng.)
This structure maintains human oversight while enabling high-frequency, data-driven adaptation. (Cấu trúc này duy trì sự giám sát của con người trong khi vẫn cho phép sự thích ứng dựa trên dữ liệu, với tần suất cao.)

Clinician oversight loop (Vòng giám sát bác sĩ lâm sàng) The clinician oversight loop introduces human oversight into AI-assisted decision-making. (Vòng giám sát bác sĩ lâm sàng đưa sự giám sát của con người vào việc ra quyết định do AI hỗ trợ.)
The AI generates treatment recommendations with interpretable summaries of patient data including longitudinal trends and sensor-derived metrics. (AI tạo ra các đề xuất điều trị với các bản tóm tắt có thể diễn giải được về dữ liệu của bệnh nhân bao gồm các xu hướng dọc và số liệu có nguồn gốc từ cảm biến.)
For example, an AI model might recommend reducing antihypertensive medication for a patient with consistently below-target blood pressure. (Ví dụ, một mô hình AI có thể đề xuất giảm thuốc điều trị tăng huyết áp cho bệnh nhân có huyết áp liên tục dưới mức mục tiêu.)
The clinician reviews the recommendation in context and may accept, reject, or modify it, and this feedback refines model alignment with clinical practice. (Bác sĩ lâm sàng xem xét khuyến nghị theo ngữ cảnh và có thể chấp nhận, từ chối hoặc sửa đổi nó, và phản hồi này tinh chỉnh sự liên kết của mô hình với thực hành lâm sàng.)
Clinicians also define operational boundaries that ensure only low-risk adjustments are automated, preserving clinical accountability while integrating machine intelligence. (Các bác sĩ lâm sàng cũng xác định các ranh giới hoạt động đảm bảo chỉ có các điều chỉnh rủi ro thấp mới được tự động hóa, giữ gìn trách nhiệm lâm sàng trong khi tích hợp trí tuệ máy móc.)

Developer feedback and patient-clinician coordination (Phản hồi của nhà phát triển và sự phối hợp giữa bệnh nhân-bác sĩ lâm sàng) Developer feedback and patient-clinician coordination shift clinical interactions from routine data collection to higher-level interpretation, shared decision-making, and model improvement. (Phản hồi của nhà phát triển và sự phối hợp giữa bệnh nhân-bác sĩ lâm sàng chuyển các tương tác lâm sàng từ việc thu thập dữ liệu thường quy sang giải thích ở mức độ cao hơn, chia sẻ quá trình ra quyết định và cải tiến mô hình.)
With AI handling data aggregation and trend analysis, clinicians engage more meaningfully: reviewing patterns, contextualizing insights, and setting personalized health goals. (Với việc AI xử lý tổng hợp dữ liệu và phân tích xu hướng, các bác sĩ lâm sàng tham gia một cách có ý nghĩa hơn: xem xét các mẫu, ngữ cảnh hóa thông tin chi tiết và thiết lập các mục tiêu sức khỏe được cá nhân hóa.)
For example, in diabetes management, a clinician may use AI-summarized data to guide discussions on dietary habits and physical activity. (Ví dụ, trong quản lý bệnh tiểu đường, bác sĩ lâm sàng có thể sử dụng dữ liệu do AI tóm tắt để hướng dẫn các cuộc thảo luận về thói quen ăn uống và hoạt động thể chất.)
Visit frequency adjusts dynamically based on patient progress rather than fixed intervals. (Tần suất thăm khám điều chỉnh linh hoạt dựa trên tiến trình của bệnh nhân thay vì các khoảng thời gian cố định.)
This positions the clinician as coach and advisor, interpreting data through the lens of patient preferences and clinical judgment. (Điều này định vị bác sĩ lâm sàng với vai trò như huấn luyện viên và cố vấn, diễn giải dữ liệu qua lăng kính sở thích của bệnh nhân và đánh giá lâm sàng.)
Feedback from these interactions gives AI developers evidence about model behavior, interface usability, and workflow fit. (Phản hồi từ các tương tác này cung cấp cho các nhà phát triển AI bằng chứng về hành vi mô hình, khả năng sử dụng giao diện và sự phù hợp với quy trình làm việc.)

14.7.2.2 Hypertension case example (14.7.2.2 Ví dụ trường hợp tăng huyết áp)
Hypertension management illustrates how the three ClinAIOps loops work in practice. (Quản lý tăng huyết áp minh họa cách thức hoạt động trong thực tế của ba vòng lặp ClinAIOps.)
Because it affects a large share of adults and requires individualized, ongoing therapy adjustments, it is an ideal candidate for continuous therapeutic monitoring. (Vì nó ảnh hưởng đến một tỷ lệ lớn người trưởng thành và đòi hỏi các điều chỉnh liệu pháp được cá nhân hóa, liên tục, nó là một ứng cử viên lý tưởng cho việc theo dõi điều trị liên tục.)

================ PAGE 865 ================

14. ML Operations (14. Vận hành ML)
827

36 Photoplethysmography (PPG): Optical technique detecting blood volume changes by measuring light absorption variations through green LEDs. (36 Photoplethysmography (PPG) (Đo thể tích đồ quang học): Kỹ thuật quang học phát hiện sự thay đổi thể tích máu bằng cách đo các biến thiên hấp thụ ánh sáng thông qua đèn LED xanh lục.)
For ML operations, PPG introduces a data quality challenge absent in controlled environments: (Đối với các hoạt động ML, PPG đưa ra một thách thức về chất lượng dữ liệu vắng mặt trong các môi trường được kiểm soát:)
motion artifacts from wrist movement corrupt the signal, creating a data drift pattern where the same physiological state produces different input distributions depending on user activity. (các nhiễu chuyển động (artifacts) từ chuyển động của cổ tay làm hỏng tín hiệu, tạo ra một mẫu trôi dạt dữ liệu trong đó cùng một trạng thái sinh lý tạo ra các phân phối đầu vào khác nhau tùy thuộc vào hoạt động của người dùng.)
Models must either filter corrupted windows before inference or learn to be robust to motion noise, and monitoring must distinguish genuine physiological changes from artifact-induced distribution shift. (Các mô hình hoặc phải lọc các cửa sổ bị hỏng trước khi suy luận hoặc phải học cách mạnh mẽ đối với nhiễu chuyển động, và việc giám sát phải phân biệt được những thay đổi sinh lý thực sự khỏi sự dịch chuyển phân phối do nhiễu (artifact) gây ra.)

Data infrastructure (Cơ sở hạ tầng dữ liệu) Research systems estimate systolic blood pressure indirectly from ECG, photoplethysmography (PPG)36, pulse-transit-time, and heart-rate features (Q. Zhang et al. 2017). (Các hệ thống nghiên cứu ước tính huyết áp tâm thu gián tiếp từ điện tâm đồ (ECG), đo thể tích đồ quang học (PPG)36, thời gian truyền xung (pulse-transit-time), và các đặc trưng nhịp tim (Q. Zhang và cộng sự. 2017).)
In a deployed hypertension workflow, those signals may be augmented by accelerometer data for activity context and self-reported medication adherence logs. (Trong một quy trình làm việc tăng huyết áp được triển khai, các tín hiệu đó có thể được tăng cường bởi dữ liệu gia tốc kế để lấy bối cảnh hoạt động và nhật ký tuân thủ thuốc do người bệnh tự báo cáo.)
Accuracy depends on validation, calibration, and regulatory authorization; consumer wrist or ring claims should not be treated as clinically reliable without such evidence. (Độ chính xác phụ thuộc vào việc xác thực, hiệu chuẩn, và sự cho phép của cơ quan quản lý; các công bố về đồng hồ đeo tay hay nhẫn tiêu dùng không nên được coi là đáng tin cậy về mặt lâm sàng nếu không có bằng chứng như vậy.)
When validated for the intended population and setting, this multimodal data stream, integrated with electronic health records, can form the foundation for personalized AI recommendations. (Khi được xác thực cho đối tượng và bối cảnh dự định, luồng dữ liệu đa phương thức này, được tích hợp với hồ sơ sức khỏe điện tử, có thể tạo thành nền tảng cho các đề xuất AI được cá nhân hóa.)

Loop implementation (Triển khai Vòng lặp) Figure 14.12 shows how two of the three feedback loops manifest in hypertension management, with each panel highlighting one loop. (Hình 14.12 cho thấy cách hai trong ba vòng phản hồi thể hiện trong việc quản lý tăng huyết áp, với mỗi bảng điểm nhấn mạnh vào một vòng lặp.)
The left panel illustrates the patient treatment loop, where the patient monitors blood pressure and receives bounded titration recommendations that the AI system can issue within clinician-defined safety thresholds; (Bảng điều khiển bên trái minh họa vòng điều trị bệnh nhân, trong đó bệnh nhân theo dõi huyết áp và nhận được các khuyến nghị chuẩn độ (titration) có giới hạn mà hệ thống AI có thể ban hành trong các ngưỡng an toàn do bác sĩ lâm sàng xác định;)
significant changes require explicit approval. (những thay đổi đáng kể cần có sự phê duyệt rõ ràng.)
The center panel depicts the clinician oversight loop, where longitudinal trend summaries flow from the AI system to the clinician, and the clinician sets approval limits and receives alerts for clinical risk events such as persistent hypotension or hypertensive crisis. (Bảng điều khiển trung tâm mô tả vòng giám sát bác sĩ lâm sàng, nơi các tóm tắt xu hướng dọc truyền từ hệ thống AI đến bác sĩ lâm sàng, và bác sĩ thiết lập các giới hạn phê duyệt cũng như nhận cảnh báo cho các sự kiện rủi ro lâm sàng chẳng hạn như hạ huyết áp dai dẳng hoặc khủng hợp tăng huyết áp.)
The right panel captures the patient-clinician coordination that emerges once routine data collection moves to the AI loop: appointments shift to higher-level discussions of lifestyle factors and shared decision-making. (Bảng điều khiển bên phải nắm bắt sự phối hợp giữa bệnh nhân-bác sĩ lâm sàng xuất hiện khi việc thu thập dữ liệu thường quy chuyển sang vòng lặp AI: các cuộc hẹn chuyển sang các cuộc thảo luận cấp cao hơn về các yếu tố lối sống và cùng ra quyết định.)
The third loop (developer feedback) is not depicted in the figure; it is described in the prose above as the channel by which real-world workflow signals from both patients and clinicians inform model and interface improvements. (Vòng lặp thứ ba (phản hồi của nhà phát triển) không được mô tả trong hình vẽ; nó được mô tả trong đoạn văn trên như là kênh thông qua đó các tín hiệu quy trình làm việc thực tế từ cả bệnh nhân và bác sĩ lâm sàng cung cấp thông tin cho những cải tiến mô hình và giao diện.)

Figure 14.12: Hypertension Management Loops: Two of the three feedback loops shown side by side, with patient-clinician coordination as the third panel. (Hình 14.12: Các Vòng Quản lý Tăng huyết áp: Hai trong số ba vòng phản hồi được hiển thị cạnh nhau, với sự phối hợp bệnh nhân-bác sĩ lâm sàng là bảng thứ ba.)
The patient treatment loop (left) enables bounded self-management through blood pressure monitoring and titration recommendations; (Vòng điều trị bệnh nhân (trái) cho phép tự quản lý có giới hạn thông qua việc theo dõi huyết áp và các đề xuất chuẩn độ;)
the clinician oversight loop (center) provides review via trend summaries and clinical risk alerts; (vòng giám sát bác sĩ lâm sàng (giữa) cung cấp sự xem xét thông qua các bản tóm tắt xu hướng và cảnh báo rủi ro lâm sàng;)
the patient-clinician coordination panel (right) shows how appointment content shifts to higher-level discussion once the AI carries routine monitoring. (bảng phối hợp bệnh nhân-bác sĩ lâm sàng (phải) cho thấy nội dung cuộc hẹn thay đổi như thế nào sang cuộc thảo luận ở cấp độ cao hơn một khi AI đảm nhận việc theo dõi thường quy.)
The developer feedback loop is discussed in the prose. Source: (Chen et al. 2023). (Vòng phản hồi của nhà phát triển được thảo luận trong đoạn văn. Nguồn: (Chen và cộng sự. 2023).)

The three panels make the accountability boundary explicit: routine monitoring can be automated only inside clinician-defined limits, while escalation, adverse-event review, and treatment trade-offs remain human responsibilities. (Ba bảng làm cho ranh giới trách nhiệm giải trình trở nên rõ ràng: việc theo dõi thường quy chỉ có thể được tự động hóa bên trong các giới hạn do bác sĩ lâm sàng xác định, trong khi việc chuyển cấp, xem xét sự cố bất lợi, và những đánh đổi điều trị vẫn là trách nhiệm của con người.)
That boundary is the point where ordinary MLOps practices need the additional clinical coordination summarized next. (Ranh giới đó là điểm mà các thực tiễn MLOps thông thường cần thêm sự điều phối lâm sàng được tóm tắt tiếp theo.)

14.7.2.3 MLOps vs. ClinAIOps comparison (14.7.2.3 So sánh MLOps và ClinAIOps)
The hypertension case illustrates the ClinAIOps-MLOps comparison: traditional MLOps frameworks are often insufficient for high-stakes clinical domains. (Trường hợp tăng huyết áp minh họa cho sự so sánh giữa ClinAIOps-MLOps: các khuôn khổ MLOps truyền thống thường không đủ cho các lĩnh vực lâm sàng có tính rủi ro cao.)
Conventional MLOps excels at technical lifecycle management but lacks constructs for coordinating human decision-making and ensuring ethical accountability. (MLOps thông thường vượt trội trong quản lý vòng đời kỹ thuật nhưng thiếu các cấu trúc để điều phối việc ra quyết định của con người và đảm bảo trách nhiệm đạo đức.)

ClinAIOps extends beyond technical infrastructure to support complex sociotechnical systems, embedding machine learning into contexts where clinicians, patients, and stakeholders collaboratively shape treatment decisions. (ClinAIOps vươn ra ngoài cơ sở hạ tầng kỹ thuật để hỗ trợ các hệ thống kỹ thuật xã hội phức tạp, nhúng học máy vào các ngữ cảnh mà ở đó các bác sĩ lâm sàng, bệnh nhân và các bên liên quan cùng phối hợp định hình các quyết định điều trị.)
Table 14.31 contrasts these approaches across eight dimensions. (Bảng 14.31 so sánh đối chiếu các phương pháp tiếp cận này trên tám phương diện.)

================ PAGE 866 ================

828
14.8 Fallacies and Pitfalls (14.8 Những lầm tưởng và cạm bẫy)
Table 14.31: Clinical AI Operations: Traditional MLOps focuses on model performance, while ClinAIOps integrates technical systems with clinical workflows, ethical considerations, and ongoing feedback loops to ensure safe, trustworthy AI assistance in healthcare settings. (Bảng 14.31: Hoạt động AI lâm sàng: MLOps truyền thống tập trung vào hiệu suất mô hình, trong khi ClinAIOps tích hợp các hệ thống kỹ thuật với quy trình làm việc lâm sàng, các cân nhắc về đạo đức và các vòng phản hồi liên tục để đảm bảo sự hỗ trợ của AI an toàn, đáng tin cậy trong các cơ sở chăm sóc sức khỏe.)
ClinAIOps prioritizes human oversight and accountability alongside automation, addressing unique challenges in clinical decision-making that standard MLOps pipelines often overlook. (ClinAIOps ưu tiên sự giám sát và trách nhiệm giải trình của con người cùng với quá trình tự động hóa, giải quyết những thách thức đặc biệt trong việc ra quyết định lâm sàng mà các đường ống MLOps tiêu chuẩn thường bỏ qua.)

| | Traditional MLOps (MLOps truyền thống) | ClinAIOps |
|---|---|---|
| Focus (Trọng tâm) | ML model development and deployment (Phát triển và triển khai mô hình ML) | Coordinating human and AI decision-making (Điều phối việc ra quyết định của con người và AI) |
| Stakeholders (Các bên liên quan) | Data scientists, IT engineers (Nhà khoa học dữ liệu, kỹ sư CNTT) | Patients, clinicians, AI developers (Bệnh nhân, bác sĩ lâm sàng, nhà phát triển AI) |
| Feedback loops (Các vòng phản hồi) | Model retraining, monitoring (Huấn luyện lại mô hình, giám sát) | Patient treatment, clinician oversight, developer feedback (Điều trị bệnh nhân, giám sát của bác sĩ lâm sàng, phản hồi của nhà phát triển) |
| Objective (Mục tiêu) | Operationalize ML deployments (Vận hành các triển khai ML) | Optimize patient health outcomes (Tối ưu hóa kết quả sức khỏe bệnh nhân) |
| Processes (Quy trình) | Automated pipelines and infrastructure (Các đường ống và cơ sở hạ tầng tự động) | Integrates clinical workflows and oversight (Tích hợp quy trình làm việc lâm sàng và giám sát) |
| Data considerations (Cân nhắc về dữ liệu) | Building training datasets (Xây dựng các bộ dữ liệu huấn luyện) | Privacy, ethics, protected health information (Quyền riêng tư, đạo đức, thông tin sức khỏe được bảo vệ) |
| Model validation (Xác thực mô hình) | Testing model performance metrics (Kiểm thử các số liệu hiệu suất mô hình) | Clinical evaluation of recommendations (Đánh giá lâm sàng các khuyến nghị) |
| Implementation (Triển khai) | Focuses on technical integration (Tập trung vào tích hợp kỹ thuật) | Aligns incentives of human stakeholders (Gắn kết các động lực của các bên liên quan là con người) |

The table’s central distinction is that clinical deployment changes who owns the risk. (Điểm khác biệt trung tâm của bảng là việc triển khai lâm sàng thay đổi người gánh chịu rủi ro.)
Technical performance remains necessary, but it is not sufficient when a recommendation affects care decisions. (Hiệu suất kỹ thuật vẫn là cần thiết, nhưng nó không đủ khi một khuyến nghị ảnh hưởng đến các quyết định chăm sóc.)
The ClinAIOps framework therefore changes the governing constraint from device efficiency to clinical accountability. (Do đó, khuôn khổ ClinAIOps thay đổi ràng buộc chi phối từ hiệu suất thiết bị sang trách nhiệm giải trình lâm sàng.)
The model participates in care, but it cannot own the clinical decision. (Mô hình tham gia vào việc chăm sóc, nhưng nó không thể sở hữu quyết định lâm sàng.)
Every recommendation must be reproducible from input data, model version, confidence score, and clinician action; otherwise the system cannot support audit, review, or outcome analysis. (Mọi khuyến nghị phải có thể tái lập từ dữ liệu đầu vào, phiên bản mô hình, điểm độ tin cậy và hành động của bác sĩ lâm sàng; nếu không, hệ thống không thể hỗ trợ phân tích kết quả, xem xét hoặc kiểm toán.)
Separation of concerns becomes a safety mechanism rather than only a software design preference: (Sự tách biệt các mối quan tâm trở thành một cơ chế an toàn hơn là chỉ là một sở thích thiết kế phần mềm:)
automated data collection from wearables, AI recommendations, clinician diagnosis, treatment decisions, and developer workflow improvement each need explicit boundaries and human gates at critical decision points. (việc thu thập dữ liệu tự động từ các thiết bị đeo, các đề xuất của AI, chẩn đoán của bác sĩ lâm sàng, các quyết định điều trị và cải tiến quy trình làm việc của nhà phát triển đều cần có ranh giới rõ ràng và các cổng kiểm duyệt của con người tại các điểm ra quyết định quan trọng.)

The same accountability requirement changes monitoring. (Cùng một yêu cầu trách nhiệm giải trình làm thay đổi việc giám sát.)
Standardized clinical data pipelines preserve training-serving parity, but clinical validation also has to compare recommendations against standard-of-care outcomes, prospective evidence, and cohort-specific effects. (Các đường ống dữ liệu lâm sàng được chuẩn hóa duy trì sự cân bằng giữa huấn luyện-phục vụ, nhưng việc xác thực lâm sàng cũng phải so sánh các khuyến nghị với các kết quả tiêu chuẩn chăm sóc, bằng chứng tiến cứu và các tác động đặc thù theo nhóm thuần tập (cohort).)
Observable degradation is measured through blood pressure control, adverse events, clinician overrides, and subgroup outcomes, not just model metrics. (Sự suy thoái có thể quan sát được đo lường thông qua việc kiểm soát huyết áp, các biến cố bất lợi, những lần ghi đè (override) của bác sĩ lâm sàng, và kết quả của nhóm phụ, chứ không chỉ các số liệu mô hình.)
Feedback loops are therefore not technical debt in this setting; patient treatment, clinician oversight, and developer feedback loops are intentional mechanisms that improve care while keeping authority with humans. (Do đó, các vòng phản hồi không phải là khoản nợ kỹ thuật trong bối cảnh này; các vòng lặp điều trị bệnh nhân, giám sát của bác sĩ lâm sàng và phản hồi của nhà phát triển là những cơ chế có chủ ý nhằm cải thiện việc chăm sóc trong khi vẫn giữ quyền hạn cho con người.)
Cost-aware automation operates inside those gates: updates can be automated only when their expected benefit justifies validation cost and patient risk, and conservative recommendations or uncertainty flags must route low-confidence cases back to clinical review. (Tự động hóa nhận thức về chi phí hoạt động bên trong các cổng đó: các bản cập nhật chỉ có thể được tự động hóa khi lợi ích mong đợi của chúng biện minh cho chi phí xác thực và rủi ro của bệnh nhân, và các đề xuất thận trọng hoặc cờ báo hiệu sự không chắc chắn phải định tuyến lại các trường hợp có độ tin cậy thấp trở về sự đánh giá lâm sàng.)

14.7.3 Case study synthesis (14.7.3 Tổng hợp nghiên cứu tình huống)
The Oura Ring and ClinAIOps cases separate stable MLOps principles from the deployment constraints that reshape their implementation. (Các trường hợp Oura Ring và ClinAIOps phân tách các nguyên tắc MLOps ổn định khỏi các ràng buộc triển khai định hình lại cách thức hiện thực hóa chúng.)
Oura is a resource-envelope case: the operational system must preserve reproducibility, consistency, and observable degradation while battery, telemetry, and weak ground truth limit what can be measured and updated on the device. (Oura là một trường hợp phong bì tài nguyên (resource-envelope): hệ thống vận hành phải duy trì tính tái lập, tính nhất quán và sự suy thoái có thể quan sát được trong khi pin, phép đo từ xa và sự thật cơ sở yếu hạn chế những gì có thể được đo lường và cập nhật trên thiết bị.)
ClinAIOps is an accountability-envelope case: the same principles apply, but validation, audit trails, and human gates dominate because the model influences clinical action. (ClinAIOps là một trường hợp phong bì trách nhiệm giải trình (accountability-envelope): các nguyên tắc tương tự vẫn được áp dụng, nhưng việc xác thực, nhật ký kiểm toán và các cổng kiểm duyệt của con người chiếm ưu thế vì mô hình ảnh hưởng đến hành động lâm sàng.)

The shared engineering lesson is that MLOps maturity is not tool accumulation. (Bài học kỹ thuật chung là sự trưởng thành của MLOps không phải là sự tích lũy công cụ.)
It is the ability to identify the governing constraint, choose the operational controls that match it, and preserve evidence when the model changes. (Đó là khả năng xác định ràng buộc chi phối, chọn các biện pháp kiểm soát vận hành phù hợp với nó, và lưu giữ bằng chứng khi mô hình thay đổi.)
Production ML systems more commonly fail when teams import intuitions from deterministic software into probabilistic systems, which is why the chapter closes by naming the fallacies and pitfalls that these two case studies help expose. (Các hệ thống ML sản xuất thường gặp thất bại hơn khi các nhóm nhập khẩu trực giác từ phần mềm tất định vào các hệ thống xác suất, đó là lý do tại sao chương này khép lại bằng cách gọi tên các lầm tưởng và cạm bẫy mà hai nghiên cứu tình huống này giúp phơi bày.)

14.8 Fallacies and Pitfalls (14.8 Những lầm tưởng và Cạm bẫy)
These fallacies and pitfalls capture common errors that waste engineering resources, trigger production incidents, and cause silent accuracy degradation. (Những lầm tưởng và cạm bẫy này nắm bắt những lỗi phổ biến gây lãng phí tài nguyên kỹ thuật, kích hoạt các sự cố sản xuất, và gây ra sự suy giảm độ chính xác một cách âm thầm.)
Each connects to specific sections detailing the underlying mechanisms and solutions. (Mỗi điểm kết nối tới các phần cụ thể trình bày chi tiết các cơ chế nền tảng và các giải pháp.)

================ PAGE 867 ================

14. ML Operations (14. Vận hành ML)
829

Fallacy: MLOps is just applying traditional DevOps practices to machine learning models. (Lầm tưởng: MLOps chỉ đơn thuần là việc áp dụng các thực tiễn DevOps truyền thống cho các mô hình học máy.)
Engineers assume standard CI/CD pipelines transfer directly to ML, but production ML requires specialized infrastructure. (Các kỹ sư cho rằng các đường ống CI/CD tiêu chuẩn có thể chuyển trực tiếp sang ML, nhưng ML sản xuất yêu cầu cơ sở hạ tầng chuyên biệt.)
As section 14.4.2.1 showed, ML pipelines add data validation, model training, performance evaluation, artifact registration, and deployment gates that make them slower and more stateful than conventional software pipelines. (Như phần 14.4.2.1 đã chỉ ra, các đường ống ML bổ sung thêm việc xác thực dữ liệu, huấn luyện mô hình, đánh giá hiệu suất, đăng ký hiện vật (artifact) và các cổng triển khai khiến chúng chậm hơn và lưu trạng thái (stateful) nhiều hơn so với các đường ống phần mềm thông thường.)
Traditional DevOps can release deterministic services frequently; ML systems without specialized tooling often slow down because retraining and validation are stateful. (DevOps truyền thống có thể phát hành các dịch vụ tất định một cách thường xuyên; các hệ thống ML nếu không có công cụ chuyên biệt thường bị chậm lại do việc huấn luyện lại và xác thực mang tính lưu trạng thái.)
Standard CI/CD tools do not by themselves handle feature stores, model registries, or drift detection. (Bản thân các công cụ CI/CD tiêu chuẩn không tự xử lý các cửa hàng đặc trưng (feature stores), các sổ đăng ký mô hình (model registries) hoặc phát hiện sự trôi dạt (drift detection).)
A recommendation system deployed using conventional DevOps can lose accuracy because the pipeline lacks training-serving consistency checks. (Một hệ thống gợi ý được triển khai bằng DevOps thông thường có thể mất đi độ chính xác do đường ống thiếu các kiểm tra tính nhất quán giữa huấn luyện-phục vụ.)
Organizations that adopt DevOps without ML adaptations optimize the computational reliability of their infrastructure while neglecting the statistical behavior of their models, encountering silent model degradation, training-serving skew, and data quality failures that evade conventional testing. (Các tổ chức áp dụng DevOps mà không có sự điều chỉnh cho ML thường tối ưu hóa độ tin cậy điện toán của cơ sở hạ tầng nhưng lại bỏ qua hành vi thống kê của các mô hình của họ, dẫn đến gặp phải sự suy giảm mô hình âm thầm, độ lệch huấn luyện-phục vụ, và các lỗi chất lượng dữ liệu vượt qua khỏi các bài kiểm thử thông thường.)

Pitfall: Treating model deployment as a one-time event rather than an ongoing process. (Cạm bẫy: Coi việc triển khai mô hình là một sự kiện xảy ra một lần thay vì là một quá trình liên tục.)
Teams view deployment as a terminal milestone analogous to shipping software releases, but models degrade continuously due to data drift and distribution shift. (Các nhóm xem việc triển khai như một cột mốc cuối cùng tương tự như việc phát hành các bản phần mềm, nhưng các mô hình suy giảm liên tục do sự trôi dạt dữ liệu và dịch chuyển phân phối.)
Section 14.5.3.1 establishes PSI as one useful distribution-shift signal whose thresholds must be calibrated to the feature and business risk. (Phần 14.5.3.1 thiết lập PSI như một tín hiệu dịch chuyển phân phối hữu ích mà ngưỡng của nó phải được hiệu chuẩn với đặc trưng và rủi ro nghiệp vụ.)
A fraud detection model can move from below the warning threshold to above the review threshold within months, turning initially acceptable accuracy into material degradation. (Một mô hình phát hiện gian lận có thể di chuyển từ dưới ngưỡng cảnh báo lên trên ngưỡng xem xét chỉ trong vòng vài tháng, biến độ chính xác ban đầu có thể chấp nhận được thành sự suy giảm nghiêm trọng.)
The optimal retraining interval follows 𝑇∗≈√2𝐶/(𝑄⋅𝑉⋅Accuracy0⋅𝛾) from section 11, where high-volume systems require more frequent retraining than low-drift domains. (Khoảng thời gian huấn luyện lại tối ưu tuân theo 𝑇∗≈√2𝐶/(𝑄⋅𝑉⋅Accuracy0⋅𝛾) từ chương 11, trong đó các hệ thống khối lượng cao yêu cầu huấn luyện lại thường xuyên hơn so với các lĩnh vực có độ trôi dạt thấp.)
Production ML requires continuous monitoring of feature distributions, performance metrics, and automated retraining triggers throughout the operational lifecycle. (ML sản xuất yêu cầu phải giám sát liên tục các phân phối đặc trưng, các số liệu hiệu suất, và các bộ kích hoạt huấn luyện lại tự động trong suốt vòng đời vận hành.)

Fallacy: Automated retraining ensures optimal model performance without human oversight. (Lầm tưởng: Huấn luyện lại tự động đảm bảo hiệu suất mô hình tối ưu mà không cần sự giám sát của con người.)
Engineers assume automated pipelines handle all maintenance scenarios, yet automation cannot detect all failure modes. (Các kỹ sư cho rằng các đường ống tự động có thể xử lý tất cả các kịch bản bảo trì, tuy nhiên quá trình tự động hóa không thể phát hiện ra mọi chế độ thất bại.)
Automated retraining can perpetuate biases in corrupted training data, trigger updates during peak traffic, or deploy models that pass aggregate validation but degrade edge cases. (Huấn luyện lại tự động có thể duy trì các thành kiến trong dữ liệu huấn luyện bị hỏng, kích hoạt các bản cập nhật trong thời gian lưu lượng truy cập cao điểm, hoặc triển khai các mô hình vượt qua quá trình xác thực tổng hợp nhưng lại làm suy giảm các trường hợp ranh giới (edge cases).)
A news recommendation system retrained on weekend data might exhibit lower weekday engagement because user behavior differs sharply across weekday vs. weekend contexts. (Một hệ thống gợi ý tin tức được huấn luyện lại trên dữ liệu cuối tuần có thể thể hiện sự tương tác vào ngày thường thấp hơn do hành vi người dùng khác biệt rõ rệt giữa bối cảnh ngày thường và cuối tuần.)
Effective MLOps requires escalation protocols for anomalous validation results, manual approval for unusual metric patterns, and override capabilities when automation produces questionable outcomes. (MLOps hiệu quả yêu cầu các giao thức chuyển cấp (escalation protocols) cho các kết quả xác thực bất thường, phê duyệt thủ công cho các mẫu số liệu lạ, và khả năng ghi đè (override) khi quá trình tự động hóa tạo ra những kết quả đáng ngờ.)

Pitfall: Focusing on technical infrastructure while neglecting organizational and process alignment. (Cạm bẫy: Tập trung vào cơ sở hạ tầng kỹ thuật trong khi bỏ qua sự liên kết giữa tổ chức và quy trình.)
Organizations invest in MLOps platforms expecting tooling to solve deployment problems, but sophisticated infrastructure fails without cultural transformation. (Các tổ chức đầu tư vào các nền tảng MLOps với kỳ vọng rằng bộ công cụ sẽ giải quyết được các vấn đề về triển khai, nhưng cơ sở hạ tầng tinh vi sẽ thất bại nếu không có sự chuyển đổi về mặt văn hóa.)
MLOps demands coordination between data scientists optimizing for accuracy, engineers prioritizing latency, and business stakeholders focused on impact. (MLOps đòi hỏi sự phối hợp giữa các nhà khoa học dữ liệu đang tối ưu hóa độ chính xác, các kỹ sư ưu tiên độ trễ (latency), và các bên liên quan của doanh nghiệp tập trung vào tác động.)
A retail company may deploy feature stores and model registries yet maintain a slow deployment cadence because data scientists and engineers operate in isolation. (Một công ty bán lẻ có thể triển khai các cửa hàng đặc trưng và sổ đăng ký mô hình nhưng vẫn duy trì nhịp độ triển khai chậm chạp do các nhà khoa học dữ liệu và kỹ sư hoạt động tách biệt.)
Successful MLOps requires cross-functional teams with unified objectives, shared on-call rotations building empathy across roles, and incentive structures rewarding production reliability alongside model performance. (MLOps thành công yêu cầu các nhóm đa chức năng với mục tiêu thống nhất, chia sẻ lịch trực chéo (on-call rotations) nhằm xây dựng sự đồng cảm giữa các vai trò, và các cấu trúc khen thưởng cho độ tin cậy sản xuất bên cạnh hiệu suất mô hình.)

Fallacy: Training and serving environments automatically remain consistent once pipelines are established. (Lầm tưởng: Môi trường huấn luyện và phục vụ sẽ tự động duy trì tính nhất quán khi các đường ống được thiết lập.)
Teams assume that feature computation produces identical values across training and serving after initial pipeline setup, but training-serving skew emerges from subtle inconsistencies in preprocessing logic, timezone handling, or dependency versions. (Các nhóm cho rằng quá trình tính toán đặc trưng tạo ra các giá trị giống hệt nhau ở cả khâu huấn luyện và phục vụ sau khi thiết lập đường ống ban đầu, nhưng độ lệch huấn luyện-phục vụ phát sinh từ những sự không nhất quán tinh vi trong logic tiền xử lý, xử lý múi giờ, hoặc các phiên bản phụ thuộc.)
Section 14.4.1.2 demonstrates how a feature store reduces this risk by centralizing feature definitions and comparing feature distributions across environments. (Phần 14.4.1.2 chứng minh cách một cửa hàng đặc trưng làm giảm rủi ro này bằng cách tập trung hóa các định nghĩa đặc trưng và so sánh các phân phối đặc trưng giữa các môi trường.)
An e-commerce ranking model that computes session_length using wall-clock time in training but processing time in serving can suffer material accuracy loss that persists until someone compares feature distributions directly. (Một mô hình xếp hạng thương mại điện tử tính toán session_length bằng cách sử dụng thời gian thực tế (wall-clock time) trong khâu huấn luyện nhưng sử dụng thời gian xử lý (processing time) trong khâu phục vụ có thể bị mất độ chính xác đáng kể và kéo dài cho đến khi ai đó so sánh trực tiếp các phân phối đặc trưng.)
Without centralized feature stores and automated consistency validation, skew detection can take weeks as degradation gradually becomes visible in aggregate metrics. (Nếu không có các cửa hàng đặc trưng tập trung và khả năng xác thực tính nhất quán tự động, việc phát hiện độ lệch có thể mất hàng tuần khi sự suy giảm dần trở nên rõ ràng trong các số liệu tổng hợp.)

Pitfall: Assuming comprehensive monitoring prevents all production incidents. (Cạm bẫy: Cho rằng giám sát toàn diện sẽ ngăn chặn mọi sự cố sản xuất.)
Engineers believe sufficient metrics and dashboards eliminate surprise failures, but monitoring creates blind spots when teams track outputs without validating inputs. (Các kỹ sư tin rằng số lượng đủ các số liệu và bảng điều khiển (dashboards) sẽ loại bỏ các thất bại bất ngờ, nhưng việc giám sát sẽ tạo ra các điểm mù khi các nhóm chỉ theo dõi các đầu ra mà không xác thực các đầu vào.)
Section 14.5.3.1 establishes that input validation detects issues before they degrade predictions, yet many ML systems in practice monitor only accuracy and latency. (Phần 14.5.3.1 thiết lập rằng việc xác thực đầu vào phát hiện ra các vấn đề trước khi chúng làm suy giảm các dự đoán, tuy nhiên nhiều hệ thống ML trong thực tế chỉ giám sát độ chính xác và độ trễ.)
A recommendation system can track click-through rate while ignoring feature staleness, missing embeddings that are hours out of date due to database replication (Một hệ thống gợi ý có thể theo dõi tỷ lệ nhấp chuột trong khi bỏ qua tính cũ nát (staleness) của đặc trưng, bỏ sót các nhúng (embeddings) bị trễ hàng giờ do nhân bản cơ sở dữ liệu)

================ PAGE 868 ================

830
14.9 Summary (14.9 Tóm tắt)
lag. This can create engagement degradation before accuracy monitoring triggers alerts. (độ trễ. Điều này có thể tạo ra sự suy giảm tương tác trước khi việc giám sát độ chính xác kích hoạt cảnh báo.)
Systems monitoring only outputs can detect failures late; adding data quality monitoring can reduce time to detection. (Các hệ thống chỉ giám sát đầu ra có thể phát hiện lỗi chậm; việc bổ sung giám sát chất lượng dữ liệu có thể làm giảm thời gian phát hiện.)
Production ML requires layered monitoring with explicit SLAs for data freshness, schema validation, feature distributions, model outputs, and business metrics. (ML sản xuất yêu cầu khả năng giám sát theo lớp với các Thỏa thuận mức dịch vụ (SLA) rõ ràng cho độ mới của dữ liệu, xác thực lược đồ, phân phối đặc trưng, kết quả đầu ra của mô hình và số liệu nghiệp vụ.)
Monitoring infrastructure itself needs redundancy to prevent blind operation during platform failures. (Bản thân cơ sở hạ tầng giám sát cũng cần tính dự phòng để ngăn chặn tình trạng vận hành "mù" trong khi nền tảng bị lỗi.)

Fallacy: Accuracy is the first production signal to monitor. (Lầm tưởng: Độ chính xác là tín hiệu sản xuất đầu tiên cần theo dõi.)
Teams instrument production with accuracy dashboards and assume degradation will appear there first. (Các nhóm trang bị cho quá trình sản xuất các bảng điều khiển độ chính xác và cho rằng sự suy giảm sẽ xuất hiện ở đó đầu tiên.)
Accuracy is a lagging indicator. (Độ chính xác là một chỉ báo có độ trễ.)
A model’s accuracy can remain stable even as the input distribution drifts, because the model continues to memorize enough of the old distribution to maintain aggregate metrics on the slice it has seen before. (Độ chính xác của một mô hình có thể duy trì sự ổn định ngay cả khi phân phối đầu vào bị trôi dạt, bởi vì mô hình tiếp tục ghi nhớ đủ lượng phân phối cũ để duy trì các số liệu tổng hợp trên phần dữ liệu mà nó đã thấy trước đó.)
By the time accuracy visibly degrades, the drift may have been accumulating for weeks. (Vào thời điểm độ chính xác suy giảm rõ rệt, sự trôi dạt có thể đã tích tụ trong nhiều tuần.)
Monitoring input distributions with PSI or KL divergence (section 14.5.3.1) catches drift earlier and allows proactive retraining before accuracy crosses the SLO. (Việc giám sát các phân phối đầu vào bằng PSI hoặc phân kỳ KL (phần 14.5.3.1) giúp nắm bắt sự trôi dạt sớm hơn và cho phép huấn luyện lại một cách chủ động trước khi độ chính xác vượt qua mục tiêu cấp độ dịch vụ (SLO).)

Pitfall: Routing leading-indicator alerts to a different channel than accuracy alerts. (Cạm bẫy: Định tuyến các cảnh báo về chỉ báo đi trước (leading-indicator) sang một kênh khác với các cảnh báo về độ chính xác.)
Teams that do instrument drift and freshness signals often wire them to a dashboard or a low-priority queue separate from the on-call path that handles accuracy regressions, so the early warning fires but no one is paged. (Các nhóm có trang bị các tín hiệu trôi dạt và độ mới thường kết nối chúng vào một bảng điều khiển hoặc một hàng đợi có mức độ ưu tiên thấp tách biệt khỏi đường dẫn trực (on-call path) chuyên xử lý các hồi quy độ chính xác, do đó cảnh báo sớm được kích hoạt nhưng không có ai được gọi.)
A leading indicator only buys time if it reaches the same response machinery, with the same severity classification and runbooks, that an accuracy drop would trigger; (Một chỉ báo đi trước chỉ giúp câu giờ nếu nó chạm tới cùng một bộ máy phản hồi, với cùng một phân loại mức độ nghiêm trọng và sổ tay vận hành (runbooks), mà một sự sụt giảm độ chính xác sẽ kích hoạt;)
otherwise detection improves while time-to-response does not. (nếu không, khả năng phát hiện được cải thiện trong khi thời gian phản hồi thì không.)
The operational goal is to make accuracy the confirmation signal rather than the first sign of trouble, which holds only when the earlier signals are acted on with equal urgency. (Mục tiêu vận hành là biến độ chính xác thành tín hiệu xác nhận thay vì là dấu hiệu rắc rối đầu tiên, điều này chỉ đúng khi các tín hiệu sớm hơn được hành động với mức độ khẩn cấp tương đương.)

14.9 Summary (14.9 Tóm tắt)
MLOps exists because machine learning systems fail differently than traditional software. (MLOps tồn tại vì các hệ thống học máy gặp lỗi khác với phần mềm truyền thống.)
Where a crashed server throws exceptions and turns dashboards red, a degrading model continues serving predictions with full confidence while accuracy erodes invisibly. (Trong khi một máy chủ bị treo sẽ ném ra các ngoại lệ và làm cho bảng điều khiển chuyển sang màu đỏ, một mô hình đang suy giảm vẫn tiếp tục phục vụ các dự đoán với độ tin cậy đầy đủ trong khi độ chính xác bị xói mòn một cách vô hình.)
This fundamental difference (probabilistic systems that decay rather than crash) explains why the operational practices developed for deterministic software prove insufficient for ML, and why the discipline of machine learning operations emerged to close this observability gap. (Sự khác biệt cơ bản này (các hệ thống xác suất bị suy tàn thay vì gặp sự cố treo) giải thích tại sao các thực tiễn vận hành được phát triển cho phần mềm tất định lại được chứng minh là không đủ cho ML, và tại sao kỷ luật vận hành học máy lại nổi lên để lấp đầy khoảng trống về khả năng quan sát này.)

The five foundational principles introduced at the chapter’s opening (section 14.2.1) provide an evaluation framework that applies regardless of scale or domain. (Năm nguyên tắc nền tảng được giới thiệu ở phần mở đầu chương (phần 14.2.1) cung cấp một khuôn khổ đánh giá áp dụng bất kể quy mô hay lĩnh vực.)
Reproducibility through versioning addresses the root cause of many production incidents: untracked artifacts including data versions, configuration changes, and environment drift that make debugging impossible and rollbacks unreliable. (Khả năng tái lập thông qua quản lý phiên bản giải quyết nguyên nhân gốc rễ của nhiều sự cố sản xuất: các hiện vật (artifacts) không được theo dõi bao gồm các phiên bản dữ liệu, các thay đổi cấu hình và trôi dạt môi trường khiến cho việc gỡ lỗi trở nên bất khả thi và việc khôi phục trở nên không đáng tin cậy.)
Separation of concerns contains the blast radius when changes are required, preventing the boundary erosion and correction cascades that transform local fixes into system-wide regressions. (Sự tách biệt các mối quan tâm kiềm chế bán kính ảnh hưởng (blast radius) khi cần có sự thay đổi, ngăn chặn sự xói mòn ranh giới và các đợt hiệu chỉnh dây chuyền có thể biến các bản sửa lỗi cục bộ thành những hồi quy trên toàn hệ thống.)
The consistency imperative targets training-serving skew, the silent accuracy killer that appears when feature computation diverges between pipelines; feature stores implement this principle by computing features once and serving them everywhere. (Mệnh lệnh về tính nhất quán nhắm mục tiêu vào độ lệch huấn luyện-phục vụ, kẻ giết chết độ chính xác thầm lặng xuất hiện khi quá trình tính toán đặc trưng bị phân kỳ giữa các đường ống; các cửa hàng đặc trưng triển khai nguyên tắc này bằng cách tính toán các đặc trưng một lần và phục vụ chúng ở mọi nơi.)
Observable degradation transforms the abstract “silent failure” problem into actionable alerts through layered monitoring that tracks data freshness, feature distributions, model outputs, and business metrics. (Sự suy thoái có thể quan sát được biến vấn đề “lỗi thầm lặng” trừu tượng thành các cảnh báo có thể hành động thông qua khả năng giám sát theo lớp theo dõi độ mới của dữ liệu, phân phối đặc trưng, kết quả đầu ra của mô hình và số liệu nghiệp vụ.)
Cost-aware automation replaces arbitrary retraining schedules with principled economics, using the staleness cost function (𝑇∗≈√2𝐶/(𝑄⋅𝑉⋅Accuracy0⋅𝛾)) to quantify when accuracy decay justifies retraining expense. (Tự động hóa nhận thức về chi phí thay thế các lịch trình huấn luyện lại tùy tiện bằng tính kinh tế có nguyên tắc, sử dụng hàm chi phí độ cũ nát (𝑇∗≈√2𝐶/(𝑄⋅𝑉⋅Accuracy0⋅𝛾)) để định lượng xem khi nào sự suy giảm độ chính xác biện minh cho chi phí huấn luyện lại.)

The infrastructure components examined throughout the chapter directly implement these principles across the three critical interfaces introduced at the chapter’s opening. (Các thành phần cơ sở hạ tầng được kiểm tra xuyên suốt chương triển khai trực tiếp các nguyên tắc này qua ba giao diện quan trọng được giới thiệu ở phần mở đầu của chương.)
Feature stores and data versioning address the Data-Model Interface by ensuring training-serving consistency. (Các cửa hàng đặc trưng và quản lý phiên bản dữ liệu giải quyết Giao diện Dữ liệu-Mô hình bằng cách đảm bảo tính nhất quán giữa huấn luyện và phục vụ.)
CI/CD pipelines and model registries address the Model-Infrastructure Interface by enforcing reproducibility and enabling rollback. (Các đường ống CI/CD và sổ đăng ký mô hình giải quyết Giao diện Mô hình-Cơ sở hạ tầng bằng cách thực thi khả năng tái lập và cho phép khôi phục (rollback).)
Monitoring systems, incident response frameworks, and on-call practices address the Production-Monitoring Interface by making degradation observable and actionable. (Hệ thống giám sát, khuôn khổ phản ứng sự cố và thực tiễn trực ca (on-call) giải quyết Giao diện Sản xuất-Giám sát bằng cách biến sự suy thoái thành có thể quan sát được và có thể hành động.)
The retraining decision framework enables cost-aware automation by connecting drift detection to economic thresholds. (Khuôn khổ ra quyết định huấn luyện lại cho phép tự động hóa nhận thức về chi phí bằng cách kết nối việc phát hiện trôi dạt với các ngưỡng kinh tế.)
The case studies demonstrated that domain constraints reshape how principles are implemented without changing which principles matter: (Các nghiên cứu tình huống đã chứng minh rằng các ràng buộc của lĩnh vực định hình lại cách thức các nguyên tắc được thực hiện mà không làm thay đổi những nguyên tắc nào là quan trọng:)
Oura Ring showed how edge constraints force proactive graceful degradation design, with the 57 percent to 79 percent accuracy improvement coming from systematic data management and feature integration rather than algorithmic innovation alone. (Oura Ring cho thấy cách các ràng buộc ranh giới (edge) buộc phải thiết kế sự suy giảm nhẹ nhàng một cách chủ động, với sự cải thiện độ chính xác từ 57% lên 79% đến từ việc quản lý dữ liệu có hệ thống và tích hợp đặc trưng thay vì chỉ là sự đổi mới thuật toán.)
ClinAIOps showed how regulatory requirements transform graceful degradation from optional to mandatory, with human-in-the-loop governance serving as the primary safety mechanism and the three feedback loops (patient treatment, clinician oversight, developer feedback) functioning as architectural patterns rather than operational overhead. (ClinAIOps cho thấy cách các yêu cầu quản lý biến sự suy giảm nhẹ nhàng từ tùy chọn thành bắt buộc, với sự quản trị của con-người-trong-vòng-lặp đóng vai trò là cơ chế an toàn chính và ba vòng phản hồi (điều trị bệnh nhân, giám sát bác sĩ lâm sàng, phản hồi nhà phát triển) hoạt động như các mẫu hình kiến trúc thay vì là chi phí hoạt động (overhead).)

================ PAGE 869 ================

14. ML Operations (14. Vận hành ML)
831

mechanism and the three feedback loops (patient treatment, clinician oversight, developer feedback) functioning as architectural patterns rather than operational overhead. (cơ chế và ba vòng phản hồi (điều trị bệnh nhân, giám sát bác sĩ lâm sàng, phản hồi nhà phát triển) hoạt động như các mẫu hình kiến trúc thay vì là chi phí hoạt động (overhead).)

Key Takeaways: Perfectly available, perfectly wrong (Bài học chính: Sẵn sàng hoàn hảo, sai lầm hoàn hảo)
• ML systems fail silently, and the degradation equation quantifies why: Unlike software that crashes, ML degrades gradually as the distributional divergence 𝒟(𝑃𝑡‖𝑃0) grows. (Các hệ thống ML gặp lỗi trong im lặng, và phương trình suy thoái định lượng lý do tại sao: Không giống như phần mềm bị sự cố treo, ML suy giảm dần dần khi phân kỳ phân phối 𝒟(𝑃𝑡‖𝑃0) gia tăng.)
A model can maintain perfect uptime while accuracy falls. Outcome monitoring is essential, not uptime tracking alone. (Một mô hình có thể duy trì thời gian hoạt động (uptime) hoàn hảo trong khi độ chính xác giảm sút. Việc giám sát kết quả là rất cần thiết, chứ không chỉ là theo dõi thời gian hoạt động.)

• Training-serving skew is a silent accuracy killer: Feature stores reduce skew by computing features once and serving them to both training and production, transforming continuous accuracy leakage into a one-time infrastructure investment. (Độ lệch huấn luyện-phục vụ là kẻ giết chết độ chính xác thầm lặng: Các cửa hàng đặc trưng làm giảm độ lệch bằng cách tính toán các đặc trưng một lần và phục vụ chúng cho cả quá trình huấn luyện lẫn sản xuất, biến sự rò rỉ độ chính xác liên tục thành một khoản đầu tư cơ sở hạ tầng diễn ra một lần.)

• Retraining is an engineering optimization, not a guess: The staleness cost function (𝑇∗≈√2𝐶/(𝑄⋅𝑉⋅Accuracy0 ⋅𝛾)) transforms retraining frequency from intuition into quantitative economics. (Việc huấn luyện lại là một sự tối ưu hóa kỹ thuật, không phải là một sự phỏng đoán: Hàm chi phí độ cũ nát (𝑇∗≈√2𝐶/(𝑄⋅𝑉⋅Accuracy0 ⋅𝛾)) biến đổi tần suất huấn luyện lại từ trực giác thành tính kinh tế định lượng.)
High-volume systems may require daily retraining; stable domains sustain monthly intervals. (Các hệ thống khối lượng cao có thể yêu cầu huấn luyện lại hàng ngày; các lĩnh vực ổn định duy trì khoảng thời gian hàng tháng.)

• Deploy through graduated rollout with pretested rollback: Canary, blue-green, and shadow deployments match risk profiles, with tiered rollback strategies that must be tested regularly through fire drills. (Triển khai thông qua việc phát hành theo từng giai đoạn với khả năng khôi phục (rollback) đã được kiểm thử trước: Triển khai Canary, xanh-lục (blue-green) và bóng tối (shadow) phù hợp với các hồ sơ rủi ro, với các chiến lược khôi phục phân tầng phải được kiểm tra thường xuyên thông qua các cuộc diễn tập phòng cháy chữa cháy (fire drills).)

• Stage the investment: Monitoring and continuous integration/deployment typically provide the highest return on investment. (Đầu tư theo từng giai đoạn: Việc giám sát và tích hợp/triển khai liên tục (CI/CD) thường mang lại lợi tức đầu tư (ROI) cao nhất.)
A $10M model justifies more rigor than internal analytics. (Một mô hình 10 triệu đô la biện minh cho sự nghiêm ngặt hơn so với một hệ thống phân tích nội bộ.)
Add feature stores when training-serving skew becomes measurable; add automated retraining as the model matures. (Bổ sung các cửa hàng đặc trưng khi độ lệch huấn luyện-phục vụ trở nên có thể đo lường được; bổ sung huấn luyện lại tự động khi mô hình trưởng thành.)

• The five principles apply universally: Reproducibility (version everything), Separation of Concerns (modular layers), Consistency (feature stores), Observable Degradation (layered monitoring), and Cost-Aware Automation (retraining economics). (Năm nguyên tắc áp dụng phổ biến: Tính tái lập (đánh phiên bản mọi thứ), Tách biệt các Mối quan tâm (các lớp mô-đun), Tính nhất quán (cửa hàng đặc trưng), Sự suy thoái có thể quan sát (giám sát theo lớp), và Tự động hóa Nhận thức Chi phí (kinh tế học huấn luyện lại).)
Domain constraints change how each principle is implemented, not whether it is required. (Các ràng buộc của lĩnh vực thay đổi cách mỗi nguyên tắc được triển khai, chứ không phải việc liệu nó có cần thiết hay không.)

• Operational maturity is staged and organizational: Managing one model differs qualitatively from managing many. (Sự trưởng thành hoạt động mang tính từng giai đoạn và tổ chức: Quản lý một mô hình khác biệt về mặt định tính so với việc quản lý nhiều mô hình.)
The principles scale, but complexity grows superlinearly with fleet size, and shared on-call rotations and unified incentives are as critical as tooling. (Các nguyên tắc này có thể mở rộng (scale), nhưng độ phức tạp tăng lên theo cấp số nhân (superlinearly) so với quy mô nhóm, và các ca trực chung cũng như các động lực thống nhất cũng quan trọng không kém gì công cụ.)

The operational discipline examined in this chapter distinguishes production ML systems from development prototypes. (Tính kỷ luật trong vận hành được xem xét trong chương này phân biệt các hệ thống ML sản xuất với các nguyên mẫu phát triển.)
The practitioners who internalize these principles can diagnose a degrading model and immediately identify whether the problem is data drift (check feature distributions), training-serving skew (compare preprocessing paths), configuration debt (audit recent changes), or feedback loop contamination (analyze temporal patterns). (Các chuyên gia thực hành thấm nhuần các nguyên tắc này có thể chẩn đoán một mô hình đang suy giảm và ngay lập tức xác định xem vấn đề là do trôi dạt dữ liệu (kiểm tra phân phối đặc trưng), độ lệch huấn luyện-phục vụ (so sánh các đường dẫn tiền xử lý), nợ cấu hình (kiểm toán các thay đổi gần đây), hay ô nhiễm vòng phản hồi (phân tích các mẫu thời gian).)
Those who treat production ML as “deploy and forget” discover their models have been silently wrong for months, eroding user trust and business value while dashboards showed green. (Những người đối xử với ML sản xuất như kiểu “triển khai rồi quên” sẽ phát hiện ra rằng các mô hình của họ đã sai trong im lặng suốt nhiều tháng, làm xói mòn lòng tin của người dùng và giá trị doanh nghiệp trong khi các bảng điều khiển vẫn hiển thị màu xanh lá cây.)
As ML systems become critical infrastructure powering decisions from loan approvals to medical diagnoses, this operational discipline determines whether organizations can deploy AI responsibly at scale. (Khi các hệ thống ML trở thành cơ sở hạ tầng quan trọng hỗ trợ cho các quyết định từ phê duyệt khoản vay đến chẩn đoán y tế, tính kỷ luật trong vận hành này xác định liệu các tổ chức có thể triển khai AI một cách có trách nhiệm ở quy mô lớn hay không.)

A traditional system can be perfectly available and therefore correct, because it breaks against its own code, and code does not move. (Một hệ thống truyền thống có thể hoàn toàn sẵn sàng và do đó là chính xác, bởi vì nó gặp lỗi do chính mã lệnh của nó, và mã lệnh thì không thay đổi (không di chuyển).)
A model breaks against the world. (Một mô hình gặp lỗi với thế giới thực.)
Its code can stay byte-for-byte identical while the data it was trained on drifts out from under it, so a system at full uptime can be confidently, silently wrong. (Mã lệnh của nó có thể giữ nguyên không đổi từng byte trong khi dữ liệu mà nó được huấn luyện đang trôi dạt dần ra khỏi nó, vì vậy một hệ thống hoạt động toàn thời gian vẫn có thể sai lầm một cách tự tin và thầm lặng.)
That is why operations for ML cannot be inherited from software: the match between model and world is not a state reached once but a cost paid continuously, the data axis of D·A·M never holding still. (Đó là lý do tại sao các hoạt động cho ML không thể được thừa hưởng từ phần mềm: sự khớp nối giữa mô hình và thế giới không phải là một trạng thái chỉ đạt được một lần mà là một khoản chi phí được trả liên tục, trục dữ liệu của D·A·M không bao giờ đứng yên.)
Reliability here is measured in outcomes, not uptime, and the most dangerous state an ML system can occupy is a green dashboard resting on a drifting model. (Độ tin cậy ở đây được đo lường bằng kết quả đầu ra chứ không phải thời gian hoạt động, và trạng thái nguy hiểm nhất mà một hệ thống ML có thể chiếm giữ là một bảng điều khiển màu xanh lá cây nằm trên một mô hình đang bị trôi dạt.)

================ PAGE 870 ================

832
14.9 Summary (14.9 Tóm tắt)
What’s Next: From reliability to responsibility (Tiếp theo là gì: Từ độ tin cậy đến trách nhiệm)
We have built a system that is efficient, scalable, and reliable. (Chúng ta đã xây dựng một hệ thống hiệu quả, có thể mở rộng và đáng tin cậy.)
A system can achieve 99.9 percent uptime and sub-10 ms latency, however, while still causing harm by amplifying bias or leaking data. (Tuy nhiên, một hệ thống có thể đạt được 99,9% thời gian hoạt động và độ trễ dưới 10 mili giây trong khi vẫn gây ra tác hại bằng cách khuếch đại sự thiên vị hoặc làm rò rỉ dữ liệu.)
In Chapter 15, we face the final and most difficult constraint: aligning our technical optimization with human values, ensuring that what we build serves the world we want to live in. (Trong Chương 15, chúng ta phải đối mặt với ràng buộc cuối cùng và khó khăn nhất: điều chỉnh sự tối ưu hóa kỹ thuật của chúng ta với các giá trị con người, đảm bảo rằng những gì chúng ta xây dựng phục vụ cho thế giới mà chúng ta muốn sống.)

Research Questions: For further inquiry (Câu hỏi Nghiên cứu: Dành cho những tìm hiểu sâu hơn)
• How should an organization detect a model that is fully available but silently wrong? (Một tổ chức nên làm thế nào để phát hiện ra một mô hình hoàn toàn có sẵn nhưng lại sai sót trong im lặng?)
• Where should boundaries be drawn to limit correction cascades across data, model, infrastructure, and monitoring? (Nên vẽ ranh giới ở đâu để hạn chế các đợt hiệu chỉnh dây chuyền trên dữ liệu, mô hình, cơ sở hạ tầng và giám sát?)
• How should retraining triggers balance staleness cost, retraining cost, traffic value, and human oversight? (Các bộ kích hoạt huấn luyện lại nên cân bằng như thế nào giữa chi phí độ cũ nát, chi phí huấn luyện lại, giá trị lưu lượng truy cập và sự giám sát của con người?)
• When do feature stores, registries, and CI/CD pipelines become justified infrastructure rather than premature process? (Khi nào các cửa hàng đặc trưng, sổ đăng ký và đường ống CI/CD trở thành cơ sở hạ tầng chính đáng thay vì là một quy trình quá sớm?)

================ PAGE 871 ================

Applications
> _
Operations
Serving
Training
∇
Models
Frameworks
Hardware
Data
15
Responsible Engineering (Kỹ thuật có trách nhiệm)
15.1 Responsibility as Systems Engineering (Trách nhiệm như một Kỹ thuật Hệ thống)
15.2 Engineering Responsibility Gap (Khoảng trống Trách nhiệm Kỹ thuật)
15.3 Responsible Engineering Checklist (Danh sách kiểm tra Kỹ thuật có trách nhiệm)
15.4 Environmental and Cost Awareness (Nhận thức về Môi trường và Chi phí)
15.5 Data Governance and Compliance (Quản trị Dữ liệu và Tuân thủ)
15.6 Fallacies and Pitfalls (Những lầm tưởng và Cạm bẫy)
15.7 Summary (Tóm tắt)

Purpose (Mục đích)
Why is a system that does exactly what it was told to do often the most dangerous? (Tại sao một hệ thống làm chính xác những gì nó được yêu cầu làm thường là hệ thống nguy hiểm nhất?)
Operations ensures the system runs reliably: low latency, high availability, accurate predictions. (Hoạt động (Operations) đảm bảo hệ thống chạy một cách đáng tin cậy: độ trễ thấp, tính sẵn sàng cao, dự đoán chính xác.)
Responsible engineering asks who that reliability serves. (Kỹ thuật có trách nhiệm đặt câu hỏi sự đáng tin cậy đó phục vụ ai.)
An ML system can meet every technical specification (latency, throughput, accuracy) while actively amplifying harm. (Một hệ thống ML có thể đáp ứng mọi thông số kỹ thuật (độ trễ, thông lượng, độ chính xác) trong khi chủ động khuếch đại tác hại.)
The failure occurs not because the system is broken but because it is working efficiently to optimize a flawed specification. (Lỗi xảy ra không phải vì hệ thống bị hỏng mà vì nó đang hoạt động hiệu quả để tối ưu hóa một thông số kỹ thuật có nhiều thiếu sót.)

A loan approval system that correctly predicts default risk can encode historical discrimination, denying credit to qualified applicants from historically marginalized communities. (Một hệ thống phê duyệt khoản vay dự đoán chính xác rủi ro vỡ nợ có thể mã hóa sự phân biệt đối xử trong lịch sử, từ chối cấp tín dụng cho những người nộp đơn đủ điều kiện từ các cộng đồng bị thiệt thòi trong lịch sử.)
A content recommendation system that accurately predicts engagement may amplify harmful content because outrage generates more clicks than nuance. (Một hệ thống gợi ý nội dung dự đoán chính xác mức độ tương tác có thể khuếch đại nội dung có hại bởi vì sự phẫn nộ tạo ra nhiều lượt nhấp chuột hơn so với những sắc thái tinh tế.)
A hiring algorithm that reliably identifies candidates similar to past hires may perpetuate workforce homogeneity, screening out the diversity that drives innovation. (Một thuật toán tuyển dụng xác định một cách đáng tin cậy các ứng viên tương tự như những người đã được tuyển dụng trước đây có thể duy trì sự đồng nhất của lực lượng lao động, sàng lọc đi sự đa dạng vốn là động lực cho sự đổi mới.)
In each case the system is performing exactly as designed. (Trong từng trường hợp, hệ thống đều đang hoạt động chính xác như thiết kế.)
The failure is in what was designed for. (Thất bại nằm ở việc nó được thiết kế cho cái gì.)
When mathematical optimization is confused with value alignment, the result is a system that is technically robust but socially fragile. (Khi sự tối ưu hóa toán học bị nhầm lẫn với sự liên kết giá trị, kết quả là một hệ thống mạnh mẽ về mặt kỹ thuật nhưng lại mong manh về mặt xã hội.)
The model faithfully reproduces whatever patterns exist in its training data, including historical injustice no one intended to encode. (Mô hình tái tạo lại một cách trung thực bất kỳ khuôn mẫu nào tồn tại trong dữ liệu huấn luyện của nó, bao gồm cả những bất công lịch sử mà không ai có ý định mã hóa.)
Building systems that work is an engineering achievement. (Việc xây dựng các hệ thống hoạt động được là một thành tựu kỹ thuật.)
Building systems that work for everyone requires treating unintended consequences not as edge cases but as system bugs: diagnosed, measured, and fixed with the rigor applied to latency or accuracy regressions. (Việc xây dựng các hệ thống phục vụ cho tất cả mọi người đòi hỏi phải coi những hậu quả không lường trước được không phải là các trường hợp ngoại lệ (edge cases) mà là các lỗi hệ thống (system bugs): được chẩn đoán, đo lường và khắc phục với sự nghiêm ngặt được áp dụng cho độ trễ hoặc độ suy giảm chính xác.)
Responsible engineering is D·A·M co-design under a constraint the specification omits: data must be interrogated for the harms it encodes, algorithms must be bounded so they do not optimize those harms, and machine infrastructure must monitor, document, and enforce those boundaries in production. (Kỹ thuật có trách nhiệm là việc đồng thiết kế D·A·M dưới một ràng buộc mà thông số kỹ thuật bỏ qua: dữ liệu phải được thẩm vấn về các tác hại mà nó mã hóa, các thuật toán phải được giới hạn để chúng không tối ưu hóa các tác hại đó, và cơ sở hạ tầng máy móc phải giám sát, lập tài liệu và thực thi các ranh giới đó trong môi trường sản xuất.)
833

================ PAGE 872 ================