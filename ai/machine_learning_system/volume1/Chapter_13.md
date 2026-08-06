Sự triển khai Các nguyên tắc

Nguyên tắc 13: Sự thiên vị (Bias) Phản hồi (Feedback) Bất biến Bất biến: Khi một mô hình’s các đầu ra ảnh hưởng sự phân phối của của nó tương lai các đầu vào, dự đoán các lỗi có thể phức tạp (compound) qua quyết định các chu kỳ. Cho một được đơn giản hóa tự-củng cố (self-reinforcing) phản hồi vòng lặp, sự chênh lệch (disparity) cho nhóm 𝑔 sau 𝑘 sự triển khai các chu kỳ có thể tăng trưởng như (For a simplified self-reinforcing feedback loop, the disparity for group 𝑔 after 𝑘 deployment cycles may grow as):
Δ𝑔(𝑘) ≈ Δ𝑔(0)⋅𝛼𝑘
fb nơi Δ𝑔(0) là ban đầu hiệu suất khoảng cách giữa các nhóm và 𝛼fb là sự khuếch đại hệ số được xác định bởi cách mạnh mẽ mô hình’s các quyết định định hình lại (reshape) hạ lưu dữ liệu (where Δ𝑔(0) is the initial performance gap between groups and 𝛼fb is the amplification factor determined by how strongly the model’s decisions reshape downstream data). Hãy xem xét một khoản vay sự phê duyệt (approval) mô hình thứ mà từ chối tín dụng tại cao hơn các tỷ lệ cho những người nộp đơn (applicants) từ về mặt lịch sử không được phục vụ đầy đủ (underserved) các cộng đồng. Bị từ chối những người nộp đơn không thể xây dựng tín dụng lịch sử, thứ mà làm (cho) tương lai các đơn đăng ký (applications) yếu hơn, thứ mà tăng tương lai từ chối các tỷ lệ. Mô hình’s độ chính xác trên của nó huấn luyện sự phân phối duy trì ổn định, nhưng dân số (population) nó phục vụ đã bị định hình lại bởi của riêng nó các quyết định. Khi 𝛼fb > 1, phản hồi vòng lặp là tự-củng cố (self-reinforcing); khi 𝛼fb ≤ 1, các động lực (dynamics) là ổn định hay bị dập tắt (damped). Thực các sự triển khai có thể cũng là phi tuyến tính hay đang bão hòa. Hệ quả: Tính công bằng (Fairness) là không (phải) một hậu-sự triển khai (postdeployment) cuộc kiểm toán (audit); nó là một tính ổn định sự ép buộc trên sự triển- khai kiểm soát vòng lặp. Các hệ thống phải giám sát được phân tách (disaggregated) hiệu suất các số liệu qua nhân khẩu học các nhóm với giống nhau sự nghiêm ngặt được áp dụng tới độ trễ các phân vị, bởi vì một sự thiên vị sự thoái- lui (regression) là vô hình tới tổng hợp độ chính xác chỉ như một đuôi-độ trễ sự vi phạm là vô hình tới trung bình độ trễ. Phần IV dịch những năm các nguyên tắc này vào sản xuất các hệ thống: việc phục vụ cơ sở hạ tầng thứ mà đáp ứng độ trễ các ngân sách (độ trễ ngân sách bất biến), hoạt động các thực tiễn thứ mà phát hiện sự trôi dạt và sự lệch trước khi người dùng làm (sự xác minh khoảng cách, thuộc về thống kê sự trôi dạt, và huấn luyện-việc phục vụ sự lệch các nguyên tắc), có trách nhiệm kỹ thuật thứ mà xử lý (treats) tính công bằng như một có thể đo lường sự triển khai sự ép buộc (sự thiên vị phản hồi bất biến), operational practices that detect drift and skew before users do, responsible engineering that treats fairness as a measurable deployment constraint). Sự tổng hợp (synthesis) thứ mà kết nối những sự triển khai các thực tế này tới định lượng các bất biến được thiết lập xuyên suốt cuốn sách đóng (closes) tập (volume).
Các ứng dụng (Applications)
(Các) hoạt động (Operations)
Việc phục vụ (Serving)
Huấn luyện (Training)
Các mô hình (Models)
Các bộ khung (Frameworks)
Phần cứng (Hardware)
Dữ liệu (Data)

Mô hình Việc phục vụ (Model Serving)
13.1 Việc phục vụ Mô hình mẫu
13.2 Việc phục vụ Tải, Độ trễ, và Kiến trúc
13.3 Việc phục vụ Hệ thống
Kiến trúc
13.4 Yêu cầu Vòng đời
13.5 Xếp hàng đợi Lý thuyết (Queuing Theory)
13.6 Mô hình Vòng đời
Sự quản lý
13.7 Thông lượng
Sự tối ưu hóa
13.8 LLM Việc phục vụ (LLM Serving)
13.9 Sự suy luận Thời gian chạy Sự lựa chọn
13.10 Cấp độ-Nút (Node-Level)
Sự tối ưu hóa
13.11 Kinh tế học và Sự lập kế hoạch
13.12 Các ngụy biện và Các cạm bẫy
13.13 Tóm tắt (Summary)
Mục đích (Purpose) Tại sao (do) việc phục vụ đảo ngược mọi sự tối ưu hóa ưu tiên thứ mà (đã) làm (cho) huấn luyện (trở nên) thành công? Huấn luyện và việc phục vụ đòi hỏi đối lập vật lý. Huấn luyện tối đa hóa thông lượng (các mẫu mỗi giây): lớn các lô và dài các kỷ nguyên (epochs) nơi độ trễ các sự bùng nổ (spikes) bị (get) hấp thụ một cách vô hình: large batches and long epochs where latency spikes get absorbed invisibly). Việc phục vụ tối thiểu hóa độ trễ, được đo lường trong mili giây mỗi yêu cầu: cá nhân các yêu cầu được trả lời đủ nhanh rằng một đơn chậm phản hồi là một bị phá vỡ sản phẩm. Huấn luyện khấu hao (amortizes) phần cứng các chi phí qua hàng tỷ các ví dụ; việc phục vụ trả một thuế trên mọi yêu cầu, nơi nhỏ các sự không hiệu quả phức tạp thành hoạt động nợ. Này sự đảo ngược là tại sao các mô hình thứ mà huấn luyện một cách đẹp đẽ thường phục vụ một cách tồi tệ: nặng-lô (batch-heavy) các kiến trúc và chuyên sâu-bộ nhớ (memory-intensive) các sự tối ưu hóa được thiết kế để làm bão hòa các máy gia tốc trong suốt huấn luyện là một cách cơ bản không-phù hợp (ill-suited) cho bùng nổ (bursty), tới hạn-độ trễ (latency-critical), nhạy cảm-chi phí (cost-sensitive) thực tế của sản xuất lưu lượng truy cập. Việc phục vụ, tuy nhiên, là nhiều hơn một độ trễ vấn đề. Một việc phục vụ hệ thống phải xử lý lưu lượng truy cập thứ mà biến đổi bởi các bậc của độ lớn giữa đỉnh (peak) và đáy (trough), giới thiệu mới mô hình các phiên bản mà không có đột ngột việc di chuyển tất cả người dùng tại một (lúc), suy thoái một cách tinh tế khi thượng lưu (upstream) các sự phụ thuộc thất bại, và làm tất cả (những điều) này một cách liên tục, không (phải) cho khoảng thời gian của một huấn luyện chạy mà (là) cho vòng đời của sản phẩm. Mọi mô hình thứ mà (đã) chứng minh của nó giá trị trong suốt huấn luyện và (đã) sống sót sự nén và việc đo điểm chuẩn cuối cùng đến tại việc phục vụ lớp—sự triển khai và sự tích hợp giai đoạn của ML vòng đời—nơi câu hỏi dịch chuyển từ “liệu nó hoạt động (hay không)?” tới “liệu nó hoạt động một cách đáng tin cậy, tại quy mô, dưới sản xuất các điều kiện, mỗi giây của mỗi ngày (hay không)?” (Every model that proved its value during training and survived compression and benchmarking eventually arrives at the serving layer—the deployment and integration stage of the ML lifecycle—where the question shifts from “does it work?” to “does it work reliably, at scale, under production conditions, every second of every day?”) Việc phục vụ cơ sở hạ tầng là nơi ML các hệ thống cuối cùng gặp những người dùng, và kỹ thuật thứ mà duy trì đó cuộc gặp gỡ là một cách định tính khác biệt từ kỹ thuật thứ mà (đã) tạo ra mô hình. Nó là cũng nơi được huấn luyện thuật toán gặp trực tiếp dữ liệu bên trong máy móc’s độ trễ ngân sách: tất cả ba D·A·M các sự ép buộc hội tụ trên mọi yêu cầu.

13.1 Việc phục vụ Mô hình mẫu
Học Các mục tiêu • Giải thích việc phục vụ sự đảo ngược từ huấn luyện thông lượng tới mỗi-yêu cầu độ trễ, khoảng không (headroom), và đuôi hành vi • Phân rã (Decompose) yêu cầu độ trễ qua sự tuần tự hóa (serialization), sự tiền xử lý, sự suy luận, việc xếp hàng đợi, sự hậu- xử lý, và mạng chi phí hoạt động • Áp dụng xếp hàng đợi (queueing) các định luật và đơn giản hàng đợi các mô hình để lên kế hoạch công suất chống lại phân vị độ trễ các mục tiêu • Chẩn đoán huấn luyện-việc phục vụ sự lệch và lạnh các sự khởi động từ không khớp sự tiền xử lý, mô hình việc tải, hay bộ nhớ đệm hành vi • Lựa chọn việc tạo lô, tải sự đổ (shedding), tự động mở rộng (autoscaling), và thời gian chạy các chiến lược cho lưu lượng truy cập các mẫu và độ trễ các ngân sách • Đánh giá LLM việc phục vụ các nút thắt cổ chai bằng cách sử dụng mã thông báo độ trễ, KV-bộ nhớ đệm bộ nhớ, và liên tục việc tạo lô các sự ép buộc • Tính toán chi phí mỗi sự suy luận từ độ chính xác, phần cứng sự sử dụng, bản sao (replica) số lượng, và thời gian chạy thông lượng
13.1 Việc phục vụ Mô hình mẫu Việc phục vụ bắt đầu nơi việc đo điểm chuẩn dừng (lại): một mô hình thứ mà đã hoạt động dưới được kiểm soát sự đo- lường phải bây giờ trả lời không thể đoán trước trực tiếp các yêu cầu. Đám mây (Cloud), Biên, Di động (Mobile), và TinyML mỗi (thứ) áp đặt khác biệt việc phục vụ các thách thức, nhưng tất cả chia sẻ giống nhau sự đảo ngược từ thông lượng sự tối ưu hóa tới độ trễ sự kiểm soát. Này việc phục vụ sự đảo ngược có cụ thể kỹ thuật các hệ quả thứ mà lan tỏa (ripple) thông qua toàn bộ ngăn xếp. Sắt (iron) định luật của ML các hệ thống trải qua (undergoes) một quyết định (decisive) sự dịch chuyển: độ trễ số hạng (𝐿lat), việc đại diện cho không thể giảm thiểu (irreducible) chi phí hoạt động của yêu cầu việc lập lịch (scheduling), mạng khứ hồi (round-trips), và hệ thống sự điều phối (orchestration), trở thành thống trị (dominant) sự ép buộc thay vì một làm tròn lỗi (The iron law of ML systems undergoes a decisive shift: the latency term (𝐿lat), representing the irreducible overhead of request scheduling, network round-trips, and system orchestration, becomes the dominant constraint rather than a rounding error). Được kiểm soát các điểm chuẩn thiết lập hiệu suất dưới được biết các điều kiện; việc phục vụ đối mặt lưu lượng truy cập các mẫu không điểm chuẩn có thể hoàn toàn lường trước. Sự lượng tử hóa có thể giảm mô hình kích thước; việc phục vụ phải xác nhận rằng những các sự tối ưu hóa (như vậy) bảo tồn độ chính xác dưới thực lưu lượng truy cập các sự phân phối. Cùng với nhau những các sự tái xác nhận (revalidations) này lật (flip) các sự ưu tiên của dữ liệu, thuật toán, và máy móc một khi các yêu cầu đến từng một tại một (thời) điểm dưới một độ trễ ngân sách. D·A·M phân loại học làm (cho) sự đảo ngược (trở nên) có thể nhìn thấy. Dữ liệu sự ép buộc dịch chuyển từ khối lượng tới sự mới mẻ: hệ thống phải xử lý một trực tiếp yêu cầu ngay lập tức, không (phải) xáo trộn hàng tỷ của các ví dụ qua một huấn luyện chạy. Thuật toán sự ép buộc dịch chuyển từ có thể thay đổi (mutable) tới bị đóng băng (frozen): việc phục vụ chạy một cố định chuyển tiếp vượt qua (pass) thay vì việc cập nhật các trọng số thông qua lan truyền ngược. Máy móc sự ép buộc dịch chuyển từ sự sử dụng tới khoảng không: một máy gia tốc được giữ tại 40 tới 60 phần trăm sự sử dụng có thể hấp thụ lưu lượng truy cập các sự bùng nổ, trong khi một bị bão hòa máy gia tốc biến nhỏ tải các sự thay đổi thành đuôi-độ trễ các thất bại. Việc phục vụ do đó tối ưu hóa hữu ích được hoàn thành công việc dưới một độ trễ lời hứa thay vì hoàn toàn bị chiếm giữ (occupied) phần cứng. Đó lời hứa buộc các còn lại phần của việc phục vụ ngăn xếp cùng với nhau. Yêu cầu việc định tuyến (routing), sự tiền xử lý, mô hình sự thực thi, sự hậu xử lý, việc tạo lô, việc lưu bộ nhớ đệm, thời gian chạy sự lựa chọn, và công suất sự lập kế hoạch tất cả cạnh tranh cho giống nhau độ trễ ngân sách. Trung tâm kỹ thuật nhiệm vụ là để quyết định công việc nào thuộc về trong trực tiếp yêu cầu con đường, công việc nào có thể di chuyển ra ngoài nó, và bao nhiêu khoảng không hệ thống phải dự trữ trước khi hữu ích thông lượng trở nên mỏng manh (fragile).
13.2 Việc phục vụ Tải, Độ trễ, và Kiến trúc Một đơn lưu lượng truy cập sự bùng nổ thứ mà vượt quá này lề (margin) có thể đổ thác thành toàn-hệ thống (system-wide) thất bại; xếp hàng đợi đường cong trong hình 13.1 làm (cho) đó sự sụp đổ (collapse) (trở nên) có thể nhìn thấy. Ví dụ 13.1: ’Thứ sáu Đen (Black Friday)’ lưu lượng truy cập sự bùng nổ Kịch bản: Một thương mại điện tử (e-commerce) sự giới thiệu hệ thống chạy một cách thoải mái tại 50 ms với 1,000 QPS. Thất bại chế độ (mode): Trên Thứ sáu Đen, lưu lượng truy cập bùng nổ 10× tới 10,000 QPS. Hệ thống không chậm xuống 10×; nó sụp đổ. Độ trễ chạm 10 s, sau đó các yêu cầu bắt đầu việc tính giờ ra (timing out). Các máy chủ là 100
13. Mô hình Việc phục vụ (Model Serving)

Jevons Nghịch lý (Paradox): William
Stanley Jevons đã quan sát trong
1865 rằng tính hiệu quả các sự cải- thiện trong được cấp nguồn bằng than (coal-powered) hơi nước (steam)
các động cơ (đã) làm tăng tổng than
sự tiêu thụ
bằng cách
việc làm (cho) hơi nước năng lượng (power) về mặt kinh tế (economically)
có thể tồn tại (viable)
cho
các ứng dụng trước đó quá tốn kém. Giống nhau động lực (dynamic) có thể
áp dụng tới AI sự suy luận: mỗi
10× chi phí sự giảm thiểu mở ra
ứng dụng các lớp thứ mà (đã) là
về mặt kinh tế
không thể khả thi (infeasible)
tại
trước đó
giá điểm, việc mở rộng tổng hợp (aggregate) nhu cầu
bởi nhiều hơn (là) tính hiệu quả lợi ích.
Này là tại sao rẻ hơn sự suy luận có thể làm tăng, không (phải) làm giảm,
tổng
GPU
hạm đội (fleet)
nhu cầu—tính hiệu quả và nhu- cầu là thường xuyên các phần bù (complements) trong AI, không (phải) các vật thay thế (substitutes). phần trăm được tải, nhưng hữu ích thông lượng giảm tới gần không bởi vì hầu hết được hoàn thành các yêu cầu đã hết giờ từ khách hàng’s góc nhìn (percent loaded, but useful throughput drops to near zero because most completed requests have already timed out from the client’s perspective). Vật lý: Này xem trước (previews) xếp hàng đợi lý thuyết được chính thức hóa (formalized) muộn hơn trong phần 13.5. Khi sự sử dụng tiếp cận 100 phần trăm, hàng đợi các độ dài phân kỳ một cách phi tuyến tính thay vì một cách tuyến tính. Hệ thống dành nhiều thời gian hơn (để) quản lý hàng đợi (ngữ cảnh việc chuyển đổi (switching), thrashing) thay vì việc làm hữu ích công việc than doing useful work).
Cách sửa (Fix):
1. Tải sự đổ (shedding): Từ chối dư thừa các yêu cầu ngay lập tức để giữ hàng đợi ngắn.
2. Tự động mở rộng (Autoscaling): Sử dụng một hoạt động kiểm soát vòng lặp để quay lên (spin up) nhiều hơn việc phục vụ các bản sao trước khi sự sử dụng chạm “đầu gối (knee)” của đường cong.
3. Sự suy thoái (Degradation): Phục vụ được lưu bộ nhớ đệm/ngu ngốc hơn các sự giới thiệu để giảm tính toán chi phí mỗi truy vấn. Các hệ thống bài học: Cao trung bình thông lượng không bảo vệ một việc phục vụ hệ thống khỏi sụp đổ. Đuôi độ trễ sự kiểm soát yêu cầu việc giữ sự sử dụng bên dưới xếp hàng đợi đầu gối, việc tôn trọng máy móc sự ép buộc thậm chí nếu đó (điều đó) có nghĩa (là) việc đổ tải hay việc phục vụ một rẻ hơn mô hình.
Hình 13.1 cho thấy rằng độ trễ duy trì có thể quản lý tại vừa phải sự sử dụng và sau đó tăng (rises) một cách nhanh chóng khi hệ thống tiếp cận sự bão hòa; này là tại sao sản xuất các hệ thống dự trữ khoảng không thay vì việc lập kế hoạch cho một một cách vĩnh viễn bị bão hòa máy gia tốc (p99)). Phần B.2.1 cung cấp một toán học sự xử lý (treatment) của đuôi-dài (long-tailed) các sự phân phối và tại sao p99 độ trễ chi phối người dùng trải nghiệm tại quy mô. Đường cong là một đơn giản xếp hàng đợi sự xấp xỉ (approximation) được dự định cho trực giác (intuition) thay vì một cụ thể khối lượng công việc.
0%
20%
40%
60%
80%
100% Hệ thống Sự sử dụng (%)

Yêu cầu Độ trễ (được chuẩn hóa tới dịch vụ thời gian))
An toàn Vùng (Safe Zone)
Nguy hiểm Vùng (Danger Zone)
(Hàng đợi
Sự bùng nổ (Explosion))
Đầu gối (The Knee)
Trung bình Độ trễ (Mean Latency)
Đuôi Độ trễ (p99))
Hình 13.1: Đuôi Độ trễ Sự bùng nổ: Yêu cầu độ trễ so với việc phục vụ sự sử dụng 𝜌serv. Trong khi trung bình độ trễ (xanh dương) duy trì vừa phải, đuôi độ trễ (đỏ, p99) bùng nổ một khi sự sử dụng vượt qua đầu gối tại ~70 phần trăm remains moderate, tail latency (red, p99) explodes once utilization passes the knee at ~70 percent). Này sử dụng đơn giản M/M/1 sự xấp xỉ được giới thiệu muộn hơn trong phần 13.5 (p99 ≈ 4.6× trung bình), do đó đường cong là có tính minh họa thay vì cụ thể-khối lượng công việc (This uses the simple M/M/1 approximation introduced later in section 13.5 (p99 ≈ 4.6× mean), so the curve is illustrative rather than workload-specific). Vượt ra ngoài kỹ thuật các giới hạn của độ trễ, kinh tế học của việc phục vụ đã trải qua một triệt để (radical) sự biến- đổi (trans-formation). Khi các mô hình trở nên nhiều hơn hiệu quả và phần cứng trở nên nhiều hơn được chuyên môn hóa (specialized), chi phí của “trí thông minh” là sụp đổ1. Facebook’s kinh nghiệm tại hạm đội quy mô minh họa độ lớn của này việc phục vụ chi phí vấn đề. Chiến tranh Câu chuyện 13.1: Sự suy luận thuế tại Facebook Ngữ cảnh: Trong 2018, Kim Hazelwood và Facebook’s AI Cơ sở hạ tầng đội (đã) mô tả một sản- xuất ML khối lượng công việc thứ mà (đã) chạm gần như mọi đối mặt-người dùng (user-facing) bề mặt: Tin tức Bảng tin (Feed) xếp hạng, Quảng cáo xếp hạng, Tìm kiếm, hình ảnh sự hiểu (Lumos), khuôn mặt sự nhận dạng (Facer), sự bất thường sự phát hiện (Sigma), được tự động hóa video việc tạo phụ đề (captioning), và một Dịch (Translate) hệ thống việc phục vụ xấp xỉ 4.5 tỷ được dịch bài đăng (post) các lần hiển thị (impressions) mỗi ngày qua nhiều hơn hai nghìn ngôn ngữ các cặp (In 2018, Kim Hazelwood and Facebook’s AI Infrastructure team described a production ML workload that touched nearly every user-facing surface: News Feed ranking, Ads ranking, Search, image understanding (Lumos), face recognition (Facer), anomaly detection (Sigma), automated video captioning, and a Translate system serving roughly 4.5 billion translated post impressions per day across more than two thousand language pairs).

13.2 Việc phục vụ Tải, Độ trễ, và Kiến trúc Thất bại chế độ: Đắt tiền phần của ML (đã) di chuyển vào việc phục vụ. Sự suy luận (đã) chạy trên bậc của hàng chục (tens) của các nghìn tỷ (trillions) của các hoạt động mỗi ngày dưới nghiêm ngặt đuôi-độ trễ các mục tiêu, nơi trực tiếp yêu cầu các sự đến (arrivals) (đã) ép buộc việc tạo lô và một một-giờ-cũ (one-hour-old) xếp hạng mô hình một cách có thể đo lường (đã) làm suy thoái Tin tức
Bảng tin chất lượng—việc ép buộc tích cực việc huấn luyện lại bên cạnh tích cực việc phục vụ. Sự giải quyết (Resolution): Facebook (đã) xử lý (treated) sự suy luận như một hạng-nhất (first-class) dữ liệu-trung tâm cơ sở hạ tầng vấn đề, việc đồng-thiết kế các mô hình, các máy gia tốc, bộ nhớ các hệ thống, và việc phục vụ các nền tảng cùng với nhau thay vì việc xử lý việc phục vụ như một sự suy nghĩ lại (afterthought) tới huấn luyện. Các hệ thống bài học: Huấn luyện tạo ra mô hình; việc phục vụ trả định kỳ (recurring) hóa đơn. Tại hạm đội quy mô, một mô hình kiến trúc thứ mà là rẻ để huấn luyện có thể vẫn là quá đắt, quá bị giới hạn-bởi bộ nhớ, hay quá biến đổi trong đuôi độ trễ để phục vụ. Giống nhau việc phục vụ-kinh tế học (serving-economics) áp lực xuất hiện trong công khai API các mức giá. Để nắm bắt (grasp) tốc độ của này chi phí sự sụp đổ, (hãy) kiểm tra log-thang đo (log-scale) giá quỹ đạo (trajectory) trong hình 13.2, thứ mà theo dõi mang tính đại diện công khai API danh sách-giá (list-price) các ảnh chụp nhanh (snapshots) như một thị trường đại diện. Nhà cung cấp các mức giá thay đổi một cách thường xuyên, do đó những các điểm này nên được đọc như mang tính lịch sử nguồn gốc (provenance) cho xu hướng (trend) thay vì như hiện tại việc mua sắm (purchasing) hướng dẫn (OpenAI 2023a, 2024; OpenAI et al. 2023; OpenAI Nhà phát triển Cộng đồng 2024; Anthropic 2024; Google Các nhà phát triển Blog 2024; DeepSeek 2024)). Mỗi bậc-của-độ lớn (order-of-magnitude) sự giảm sút thay đổi ứng dụng nào là khả thi (feasible).

Năm (Year)
$100
$10
$1
$0.10
$0.01 Giá mỗi 1M (triệu) Mã thông báo ($))
GPT-3 (Davinci)
GPT-3.5 Turbo
GPT-4 (Gốc (Original))
Claude 3 Opus
Claude 3 Haiku
GPT-4o
Gemini 1.5 Flash
GPT-4o-mini
DeepSeek-V3
Xu hướng: ~5.8× Rẻ hơn Mỗi 18 Các tháng (Trend: ~5.8× Cheaper Every 18 Months)
Hình 13.2: Trí thông minh Sự giảm phát: Mang tính đại diện công khai API đầu vào-mã thông báo danh sách các mức giá mỗi 1M mã thông báo ($) theo thời gian. Các mức giá là mô hình-phiên bản các ảnh chụp nhanh được thu thập từ công khai định giá (pricing) các trang của OpenAI, Anthropic, Google, và DeepSeek giữa 2020 và 2025 và được dự định như một thị trường xu hướng chỉ báo (indicator), không (phải) một được kiểm soát hay hiện tại-giá sự so sánh. API mã thông báo-việc xử lý các mức giá đã sụp đổ bởi nhiều các bậc của độ lớn, việc biến đổi kinh tế học của được tự động hóa AI các luồng công việc. Hai các áp lực bây giờ đóng khung việc phục vụ vấn đề: đuôi độ trễ thứ mà bùng nổ một khi sự sử dụng vượt qua xếp hàng đợi đầu gối, và mỗi-sự suy luận kinh tế học thứ mà rơi (fall) bởi các bậc của độ lớn khi tính hiệu quả cải thiện. Cùng với nhau chúng ép buộc một chính thức định nghĩa của việc phục vụ được xây dựng xung quanh độ trễ thay vì thông lượng. Định nghĩa 13.1: Mô hình việc phục vụ (Model serving) Mô hình Việc phục vụ là hoạt động giai đoạn thứ mà cung cấp mô hình các dự đoán tới kết thúc-những người dùng hay hạ- lưu các hệ thống dưới nghiêm ngặt độ trễ các sự ép buộc.

13. Mô hình Việc phục vụ (Model Serving)

Dịch vụ Cấp độ Mục- tiêu so với Dịch vụ Cấp độ Thỏa thuận: Một SLO là một nội bộ mục tiêu (cho ví dụ,
“p99 độ trễ dưới 50 ms”); một SLA là một bên ngoài thuộc về hợp đồng (contractual)
cam kết với tài chính các hình phạt cho sự vi phạm (An SLO is an internal target (for example, “p99 latency under 50 ms”); an SLA is an external contractual commitment with financial penalties for violation). Các SLO được đặt chặt chẽ hơn (so với) các SLA để cung cấp một an toàn lề (safety margin). Cho
ML việc phục vụ, cả hai mô hình độ-
chính xác và sự suy luận độ trễ
đóng góp vào các SLO, việc tạo ra
nhiều-chiều sự tối ưu-
hóa các mục tiêu nơi việc cải thiện một chiều (cho ví dụ,
việc triển khai một lớn hơn mô hình cho độ chính xác) có thể vi phạm (chiều) khác (độ trễ) can violate the other (latency)).
1. Tầm quan trọng (Significance): Nó đảo ngược thông lượng ưu tiên (𝜂hw) của huấn luyện thành một độ trễ sự ép buộc (𝐿lat), việc yêu cầu một thuộc về kiến trúc ngăn xếp được thiết kế để tối thiểu hóa đuôi độ trễ (p99) của cá nhân các sự suy luận (It inverts the throughput priority (𝜂hw) of training into a latency constraint (𝐿lat), requiring an architectural stack designed to minimize the tail latency (p99) of individual inferences).
2. Sự khác biệt (Distinction): Không giống như mô hình huấn luyện, thứ mà xử lý lớn, có thể đoán trước các lô của dữ liệu, mô hình việc phục vụ phải xử lý ngẫu nhiên (stochastic) yêu cầu các mẫu và không thể đoán trước tải.
3. Phổ biến cạm bẫy: Một thường xuyên quan niệm sai lầm là rằng việc phục vụ là “chỉ (là) chuyển tiếp vượt qua.” (A frequent misconception is that serving is “just the forward pass.”) Trong thực tế, nó là một phân tán hệ thống vấn đề: mô hình sự thực thi là chỉ một thành phần của một ngăn xếp thứ mà bao gồm yêu cầu việc định tuyến, tải việc cân bằng, và dữ liệu sự biến đổi. SLO2 xác định độ trễ mục tiêu thứ mà định hình mọi thuộc về kiến trúc quyết định trong việc phục vụ ngăn xếp, bao gồm cách hệ thống lập ngân sách thời gian qua sự tiền xử lý, mô hình sự thực thi, sự hậu xử lý, và sự vận chuyển (transport). Việc phục vụ các hệ thống phải do đó thực thi một hoàn chỉnh sự suy luận đường ống dưới độ trễ các sự ép buộc, không chỉ nơ-ron mạng sự tính toán. Một phổ biến quan niệm sai lầm là rằng “sự suy luận thời gian” bằng “việc phục vụ thời gian,” nhưng nơ-ron mạng là chỉ một giai đoạn trong một dài hơn đường ống. Hình 13.3 cho thấy rằng thô các đầu vào đi qua (pass through) sự tiền xử lý (truyền thống việc tính toán), nơ-ron mạng sự suy luận (sâu học), và sự hậu xử lý (truyền thống việc tính toán) trước khi việc tạo ra cuối cùng các đầu ra, neural network inference (deep learning), and postprocessing before producing final outputs). Bất kỳ của những các giai đoạn này có thể trở thành độ trễ nút thắt cổ chai. Phần 13.4.1 định lượng một cách chính xác nơi thời gian đi (đến), việc tiết lộ một phản trực giác (counterintuitive) kết quả về (giai đoạn) nào các giai đoạn thống trị.
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
Hình 13.3: Sự suy luận Đường ống: ML việc phục vụ các hệ thống biến đổi thô các đầu vào thành cuối cùng các đầu ra thông qua tuần tự các giai đoạn: sự tiền xử lý, nơ-ron mạng sự tính toán, và sự hậu xử lý. Nơ-ron mạng đại diện chỉ một thành phần; sự tiền xử lý và sự hậu xử lý dựa trên truyền thống việc tính toán và thường thống trị tổng độ trễ trong được tối ưu hóa các hệ thống. Đường ống biến việc phục vụ thành một sự điều phối vấn đề: sự tiền xử lý, mô hình sự thực thi, sự hậu- xử lý, và sự vận chuyển tất cả cạnh tranh cho giống nhau độ trễ ngân sách. Trước khi việc tối ưu hóa bất kỳ một giai đoạn , hệ thống phải quyết định liệu các dự đoán được tính toán trước của thời gian hay theo yêu cầu (on demand).
13.2.1 Tĩnh so với động sự suy luận Trước khi việc tối ưu hóa cách để giảm sự suy luận độ trễ, hệ thống phải quyết định khi nào các dự đoán được tính toán. Đầu tiên thuộc về kiến trúc quyết định trong bất kỳ việc phục vụ hệ thống là liệu các dự đoán xảy ra trước hay trong suốt người dùng các yêu cầu (Google 2024b)). Này sự lựa chọn định hình hệ thống thiết kế, chi phí cấu trúc, và khả năng các ranh giới.
13.2.1.1 Tĩnh sự suy luận Tĩnh sự suy luận (cũng được gọi là ngoại tuyến hay lô sự suy luận) tính toán trước các dự đoán cho được lường trước các đầu vào và lưu trữ chúng cho sự truy xuất precomputes predictions for anticipated inputs and stores them for retrieval). Hãy xem xét một sự giới thiệu hệ thống thứ mà tạo ra các dự đoán cho tất cả người dùng-mặt hàng các cặp hàng đêm. Khi một người dùng yêu cầu các sự giới thiệu, hệ thống truy xuất được tính toán trước các kết quả từ một tra cứu (lookup) bảng thay vì việc chạy sự suy luận. Này cách tiếp cận di chuyển tính toán ra khỏi yêu cầu con đường, kích hoạt ngoại tuyến chất lượng các sự kiểm tra, và có thể giảm việc phục vụ các chi phí cho có thể đoán trước các đầu vào. Tuy nhiên, tĩnh sự suy luận cần hoặc một dự phòng trực tuyến con đường hoặc một được làm mới lô sự tính toán khi các yêu cầu bao gồm không lường trước các đầu vào hay mới được cập nhật các mô hình.
13.2.1.2 Động sự suy luận Động sự suy luận (cũng được gọi là trực tuyến hay thời gian-thực sự suy luận) tính toán các dự đoán theo yêu cầu khi các yêu cầu đến computes predictions on demand when requests arrive). Này xử lý bất kỳ đầu vào , bao gồm hiếm biên các trường hợp và mới mẻ (novel) các sự kết hợp, và ngay lập tức phản ánh mô hình các bản cập nhật. Chi phí là nghiêm ngặt độ trễ các yêu cầu thứ mà ép buộc mô hình tính phức tạp và đòi hỏi mạnh mẽ việc giám sát cơ sở hạ tầng.

13.2 Việc phục vụ Tải, Độ trễ, và Kiến trúc Cho của chúng ta ResNet-50 hình ảnh bộ phân loại, hãy xem xét hai sự triển khai các kịch bản. Một tĩnh cách tiếp cận phù hợp (suits) một bức ảnh (photo) sự tổ chức (organization) ứng dụng thứ mà phân loại trước tất cả các hình ảnh trong một người dùng’s thư viện qua đêm. Với 10,000 các bức ảnh và 5 ms sự suy luận mỗi , lô việc xử lý tốn ~50 s tổng cộng, và những người dùng thấy ngay lập tức sự phân loại khi việc duyệt (browsing). Một động cách tiếp cận phù hợp một nội dung sự điều độ (moderation) API thứ mà phải phân loại được tải lên-bởi-người dùng (user-uploaded) các hình ảnh trong thời gian-thực, với mỗi hình ảnh việc yêu cầu đầy đủ sự tiền xử lý→sự suy luận→sự hậu xử lý đường ống và một 100 ms độ trễ ngân sách. Hầu hết sản xuất hình ảnh sự phân loại các hệ thống sử dụng một lai cách tiếp cận: thường xuyên được yêu cầu các hình ảnh (phổ biến các sản phẩm, được biết các meme) được phân loại trước và được lưu bộ nhớ đệm, trong khi mới mẻ (novel) các lượt tải lên kích hoạt động sự suy luận are preclassified and cached, while novel uploads trigger dynamic inference). Sự lựa chọn giữa tĩnh và động việc phục vụ có trực tiếp thuộc về kinh tế các hệ quả. Chặt chẽ hơn độ trễ các yêu cầu một cách trực tiếp dịch thành cao hơn cơ sở hạ tầng các chi phí, và việc định lượng chi phí của độ trễ trong đô la các điều khoản (terms) tiết lộ bao nhiêu cơ sở hạ tầng phí bảo hiểm (premium) mỗi mili giây của độ trễ sự giảm thiểu đòi hỏi. Khăn ăn (Napkin) Toán học 13.1: Chi phí của độ trễ Độ trễ các sự ép buộc một cách trực tiếp ra lệnh cơ sở hạ tầng các chi phí. Hãy xem xét một GPU máy chủ việc thuê cho $4/giờ. Kịch bản A (thấp độ trễ): Lô kích thước 1. • Độ trễ: 5 ms. • Thông lượng: 200 req/s. • Chi phí mỗi triệu các truy vấn: $5.56. Kịch bản B (cao thông lượng): Lô kích thước 8. • Độ trễ: 10 ms (được nhân đôi do việc tạo lô chi phí hoạt động)). • Thông lượng: 800 req/s (được nhân bốn do song song tính hiệu quả)). • Chi phí mỗi triệu các truy vấn: $1.39. Các hệ thống sự thấu hiểu (insight): Việc giảm độ trễ từ 10 ms tới 5 ms làm tăng phần cứng hóa đơn bởi 300 phần trăm. Các kỹ sư phải định lượng liệu đó sự tăng tốc tạo ra đủ kinh doanh giá trị để biện minh 4× chi phí sự gia tăng (hay không). Hầu hết sản xuất các hệ thống kết hợp cả hai các cách tiếp cận. Phổ biến các truy vấn chạm một bộ nhớ đệm được điền bởi lô sự suy luận trong khi không phổ biến các yêu cầu kích hoạt động sự tính toán. Việc hiểu này phổ (spec-trum) quan trọng bởi vì nó xác định nào tiếp theo sự tối ưu hóa các chiến lược áp dụng. Tĩnh sự suy luận tối ưu hóa cho thông lượng trong suốt lô sự tính toán và lưu trữ tính hiệu quả cho việc phục vụ. Động sự suy luận tối ưu hóa cho mỗi-yêu cầu độ trễ dưới đồng thời tải, thứ mà yêu cầu việc hiểu nơi thời gian đi (đến) bên trong mỗi yêu cầu. Tĩnh-so với-động quyết định là đầu tiên của một vài thuộc về kiến trúc các sự lựa chọn thứ mà định hình việc phục vụ hệ thống thiết kế. Không kém phần quan trọng là nơi mô hình thực thi, bởi vì sự triển khai ngữ cảnh ép buộc mọi tiếp theo sự tối ưu hóa. Tất cả của chi phí sự phân tích bên trên giả định một truyền thống chuyển tiếp vượt qua: một cố định sự tính toán đồ thị thứ mà thực thi một lần mỗi yêu cầu và tạo ra một kết quả. Một mới lớp của các mô hình lật ngược (upends) đó giả định bằng cách một cách có chủ ý việc làm tăng lượng của sự tính toán được dành mỗi truy vấn, việc đánh đổi độ trễ cho câu trả lời chất lượng, và việc phục vụ chi phí các hệ quả là đáng kể. Các hệ thống Góc nhìn 13.1: Việc nhìn về phía trước (Looking ahead): Một cách có chủ ý việc dành nhiều hơn tính toán mỗi truy vấn Truyền thống việc phục vụ tối ưu hóa cho việc tối thiểu hóa độ trễ (𝐿lat → 0). Vài sự suy luận-thời gian-tính toán (inference-time-compute) các hệ thống một cách có chủ ý dành nhiều hơn tính toán các chu kỳ để cải thiện câu trả lời chất lượng. Cá nhân mã thông báo việc tạo (generation) duy trì bị giới hạn-bởi bộ nhớ-băng thông, nhưng những các hệ thống này có thể tạo ra xa nhiều hơn các mã thông báo mỗi yêu cầu, bao gồm trung gian lập luận hay tìm kiếm các mã thông báo, việc làm tăng tổng

13. Mô hình Việc phục vụ (Model Serving)

tính toán và năng lượng được dành mỗi truy vấn. Tổng hợp hiệu ứng có thể mang giống như-huấn luyện tính toán các ngân sách vào việc phục vụ giai đoạn, mặc dù mỗi mã thông báo là vẫn được chi phối bởi bộ nhớ bức tường. Liệu một hệ thống dành một chuyển tiếp vượt qua hay nhiều lập luận các bước mỗi truy vấn (hay không), sự triển khai ngữ cảnh vẫn xác định khả thi độ trễ và chi phí vỏ bọc. Đó ngữ cảnh là tiếp theo biến.
13.2.2 Phổ của việc phục vụ các kiến trúc Mặc dù “việc phục vụ” thường ngụ ý một được kết nối mạng máy chủ việc xử lý API các yêu cầu, thuộc về kiến trúc mẫu biến đổi một cách quyết liệt bởi sự triển khai môi trường. Phần 2.1 đã giới thiệu bốn sự triển khai các mô hình mẫu (Đám mây, Biên, Di động, và TinyML) và vật lý các sự ép buộc (ánh sáng rào cản, sức mạnh bức tường, và bộ nhớ bức tường) thứ mà làm (cho) nảy sinh tới chúng and the physical constraints that give rise to them). Những các sự ép buộc đó không biến mất tại việc phục vụ thời gian; chúng tăng cường (intensify), bởi vì việc phục vụ thêm độ trễ các SLO và chi phí áp lực trên đỉnh của phần cứng các giới hạn thứ mà huấn luyện có thể hấp thụ thông qua sự kiên nhẫn. Giống nhau mô hình có thể yêu cầu một cách triệt để khác biệt việc phục vụ các chiến lược tùy thuộc trên nơi nó thực thi.
13.2.2.1 Được kết nối mạng việc phục vụ (đám mây/dữ liệu trung tâm)) Trong được kết nối mạng việc phục vụ, mô hình chạy như một độc lập (standalone) dịch vụ (vi dịch vụ (microservice)), sự triển khai mô hình mẫu phần 2.5 (đã) mô tả đặc điểm (characterized) như việc đánh đổi độ trễ cho lớn hơn được gộp (pooled) tính toán, the deployment paradigm section 2.5 characterized as trading latency for larger pooled compute). Chính giao diện là mạng thông qua yêu cầu các giao thức như HTTP hay gRPC, do đó việc ràng buộc các sự ép buộc là mạng băng thông và sự tuần tự hóa chi phí trước khi yêu cầu thậm chí chạm tới máy gia tốc. Dữ liệu- trung tâm phần cứng như NVIDIA các GPU, Google Tensor Xử lý Các đơn vị, và AWS Inferentia hỗ trợ cao-thông lượng việc tạo lô và tính đồng thời, nhưng lạnh sự khởi động có thể vẫn kéo dài (stretch) từ các giây tới các phút bởi vì vùng chứa (container) sự khởi động, mô hình việc tải, và sự khởi động (warmup) ngồi bên ngoài ổn định-trạng thái (steady-state) sự suy luận con đường, Google Tensor Processing Units (TPUs), and AWS Inferentia supports high-throughput batching and concurrency, but cold start can still stretch from seconds to minutes because container startup, model loading, and warmup sit outside the steady-state inference path).
13.2.2.2 Được nhúng-ứng dụng việc phục vụ (di động/biên)) Trong được nhúng-ứng dụng việc phục vụ, mô hình chạy bên trong người dùng ứng dụng tiến trình (cho ví dụ, một điện thoại thông minh ứng dụng việc sử dụng CoreML hay TensorFlow Lite), được nhúng mô hình mẫu phần 2.6 và phần 2.7 (đã) phân tích cho của nó độ trễ, quyền riêng tư, và ngoại tuyến các lợi thế, the embedded paradigm section 2.6 and section 2.7 analyzed for its latency, privacy, and offline advantages). Có (là) không “máy chủ.” Giao diện là một hàm lệnh gọi (call), do đó sự tối ưu hóa tập trung trên năng lượng và tính đáp ứng (responsiveness) (SingleStream) thay vì được chia sẻ-máy chủ thông lượng rather than shared-server throughput). Trung tâm lợi thế là Không-Bản sao (Zero-Copy) Sự suy luận: khi dữ liệu di chuyển thông qua một hệ thống, mỗi bản sao tiêu thụ CPU các chu kỳ và bộ nhớ băng thông. Trong đám mây việc phục vụ, một camera khung hình (frame) có thể bị sao chép bốn lần: từ mạng bộ đệm tới ứng dụng bộ nhớ, sau đó tới một sự tiền xử lý bộ đệm, sau đó tới có thể truy cập-GPU bộ nhớ, và cuối cùng tới GPU VRAM. Di động các NPU có thể loại bỏ hầu hết của những các bản sao này bằng cách việc chia sẻ bộ nhớ một cách trực tiếp với camera phần cứng. Camera viết các pixel vào một bộ đệm thứ mà NPU đọc một cách trực tiếp, việc tránh CPU hoàn toàn. Này làm giảm cả hai độ trễ (không sao chép các hoạt động) và năng lượng (bộ nhớ các bản sao tiêu thụ đáng kể sức mạnh) and energy). Cơ chế yêu cầu phần cứng sự hỗ trợ: camera, CPU, và NPU phải chia sẻ một thống nhất bộ nhớ kiến trúc, như trong di động hệ thống trên chip các thiết kế như Apple’s M-series và Qualcomm Snapdragon designs such as Apple’s M-series and Qualcomm Snapdragon). Điển hình phần cứng bao gồm di động các NPU và được nhúng các GPU (Jetson) and embedded GPUs (Jetson)). Lạnh sự khởi động thường rơi (vào khoảng) trong các mili giây bởi vì mô hình là đã trong ứng dụng bộ nhớ, mặc dù đầu tiên sự suy luận có thể kích hoạt vừa-kịp-thời gian sự biên dịch (100–500 ms) compilation (100–500 ms)). Được duy trì sức mạnh ngân sách là 1–5 W, với thuộc về nhiệt sự điều chỉnh sau kéo dài (prolonged) sự suy luận.
13.2.2.3 Trần-kim loại (Bare-metal) việc phục vụ (TinyML) Trong TinyML việc phục vụ, mô hình được biên dịch vào phần sụn (firmware) của một vi điều khiển (microcontroller), cực đoan kết thúc của sự triển khai phổ phần 2.8 (đã) giới thiệu như phổ biến sự cảm biến tại vi watt (microwatt) sức mạnh các ngân sách. Có (là) không điều hành hệ thống hay động bộ nhớ bộ cấp phát (allocator). “Việc phục vụ” là một chặt chẽ (tight) vòng lặp việc đọc các cảm biến và việc gọi (invoking) trình thông dịch (interpreter) (“Serving” is a tight loop reading sensors and invoking the interpreter). Sự tối ưu hóa tập trung trên tĩnh bộ nhớ sự sử dụng (việc khớp trong SRAM) bởi vì tất cả bộ nhớ được cấp phát trước trong Tensor Đấu trường (Arena) và động việc tạo lô là không thể because all memory is preallocated in the Tensor Arena and dynamic batching is impossible). Điển hình phần cứng bao gồm ARM Cortex-M series, ESP32, và được chuyên môn hóa TinyML các máy gia tốc. Lạnh sự khởi động rơi (vào khoảng) trong các micro giây bởi vì mô hình các trọng số sống trong flash và tensor đấu trường được cấp phát trước, trong khi sức mạnh ngân sách nằm trong khoảng từ các vi watt tới các mili watt cho pin hoạt động qua các tháng hay các năm.
Bảng 13.1 tóm tắt cách những sự triển khai các ngữ cảnh này định hình việc phục vụ hệ thống thiết kế.

13.2 Việc phục vụ Tải, Độ trễ, và Kiến trúc Để làm (cho) những thuộc về kiến trúc các sự khác biệt này (trở nên) cụ thể, (hãy) xem xét cách một đơn mô hình phải thích nghi với mỗi sự triển khai ngữ cảnh. Giống nhau ResNet-50 kiến trúc yêu cầu một cách quyết liệt (dramatically) khác biệt việc phục vụ các chiến lược qua sự triển- khai các ngữ cảnh. Bảng 13.2 so sánh ba các bậc (tiers) cạnh nhau (side by side): đám mây việc phục vụ chạy đầy đủ FP16 động cơ tại mili giây độ trễ trên một dữ liệu trung tâm GPU; di động việc phục vụ nén tới INT8 và phân phối (dispatches) tới một NPU tại một phần nhỏ (fraction) của năng lượng; TinyML không thể chạy ResNet-50 hoàn toàn (at all) và thay vào đó phục vụ một được thu nhỏ (downsized) MobileNetV2 trong các kilobyte của SRAM.
Bảng 13.1: Việc phục vụ Kiến trúc Phổ: Sự triển khai mô hình mẫu được chọn trong phần 2.9 định hình mọi khía cạnh của việc phục vụ hệ thống thiết kế. Đám mây các hệ thống tối ưu hóa cho thông lượng với động việc tạo lô; di động các hệ thống tối ưu hóa cho năng lượng với cố định lô-1; TinyML các hệ thống hoạt động dưới cực đoan bộ nhớ và sức mạnh các sự ép buộc với không động sự cấp phát . Vật lý các bức tường (ánh sáng, sức mạnh, bộ nhớ) thứ mà (đã) tạo ra những các mô hình mẫu này bây giờ ra lệnh việc phục vụ các sự ép buộc mỗi phải thỏa mãn that created these paradigms now dictate the serving constraints each must satisfy).
Đặc điểm (Characteristic) Đám mây/Dữ liệu trung tâm
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
Cập nhật Cơ chế Vùng chứa (Container) sự triển khai (deploy)
Ứng dụng cửa hàng cập nhật Phần sụn (Firmware) qua-không-trung
Thất bại Chế độ (Failure Mode) Thử lại (Retry)/chuyển đổi dự phòng (failover) Tinh tế sự suy thoái
Im lặng hay đặt lại (Silent or reset)
Việc giám sát (Monitoring)
Đầy đủ đo từ xa (telemetry)
Giới hạn phân tích (analytics)
Nhịp tim (Heartbeat) chỉ (only) Các hệ thống Góc nhìn 13.2: ResNet-50 qua việc phục vụ phổ Các hệ thống sự thấu hiểu: “Giống nhau mô hình” tuyên bố là gây hiểu lầm: mỗi hàng của bảng 13.2 là một khác biệt sự tối ưu hóa, và thường một khác biệt kiến trúc hoàn toàn. Đám mây và di động các bậc chia sẻ ResNet-50 đồ thị nhưng phân kỳ trong độ chính xác, thời gian chạy, và bộ nhớ bởi ba tới bốn các bậc của độ lớn; TinyML bậc không thể chạy ResNet-50 hoàn toàn và thay thế (substitutes) một kiến trúc được thiết kế cho các sự ép buộc từ sự khởi đầu. Việc xử lý những này như một mô hình giấu công việc thứ mà làm (cho) mỗi sự triển khai (trở nên) khả thi.
Bảng 13.2: ResNet-50 Qua Việc phục vụ Phổ: Cạnh-nhau sự so sánh của đám mây, di động, và TinyML việc phục vụ cho giống nhau mục tiêu kiến trúc, việc hiển thị cách mô hình định dạng, độ trễ, thông lượng, bộ nhớ dấu chân (footprint), và năng lượng ngân sách dịch chuyển bởi ba tới bốn các bậc của độ lớn qua sự triển khai các ngữ cảnh.
Chiều (Dimension)
Đám mây
Di động
TinyML
Mô hình định dạng (Model format)
TensorRT FP16 động cơ (51.2
MB)
TensorFlow Lite INT8 (25.6
MB)
Không khả thi (25.6 MB); thay thế (alternative): MobileNetV2-0.35
INT8 (3.5 MB) Sự suy luận (lô-1))
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
13.2.3 Tải bộ cân bằng lớp Khi lưu lượng truy cập vượt quá gì một đơn máy móc có thể xử lý, đám mây và dữ liệu trung tâm các sự triển khai thứ mà chạy nhiều các bản sao của giống nhau mô hình yêu cầu một bổ sung cơ sở hạ tầng lớp: tải bộ cân bằng. Sản xuất việc phục vụ các hệ thống đặt tải các bộ cân bằng giữa các máy khách và mô hình các máy chủ, việc cung cấp ba thiết yếu các chức năng cho việc phục vụ cơ sở hạ tầng. Yêu cầu sự phân phối, đầu tiên chức năng, định tuyến đến (incoming) các yêu cầu tới có sẵn mô hình các bản sao bằng cách sử dụng các thuật toán như round-robin hay ít nhất-các kết nối (least-connections). Cho nhạy cảm-độ trễ ML việc phục vụ, các thuật toán thứ mà

13. Mô hình Việc phục vụ (Model Serving)

Một ồn ào hàng xóm làm xáo trộn (perturbs) mọi khối lượng công việc việc chia sẻ nút. định tuyến tránh xa chậm hay quá tải các bản sao cải thiện đuôi độ trễ. (Chức năng thứ) hai, sức khỏe việc giám sát, một cách liên tục xác minh rằng các bản sao là sẵn sàng để phục vụ, việc định tuyến lưu lượng truy cập tránh xa không khỏe mạnh các phiên bản. Cho ML các hệ thống, sức khỏe các sự kiểm tra phải xác minh cả hai tiến trình tính sống còn (liveness) và mô hình sự sẵn sàng, việc xác nhận rằng các trọng số được tải và sự khởi động là hoàn tất. (Chức năng thứ) ba, sự triển khai sự hỗ trợ, kích hoạt an toàn mô hình các bản cập nhật bằng cách một cách dần dần việc dịch chuyển lưu lượng truy cập giữa các phiên bản thay vì việc xử lý sự phát hành như một tất cả-tại-một-lúc công tắc. Phần 14.5.1.1 muộn hơn biến đó cơ bản lưu lượng truy cập-sự dịch chuyển (traffic-shift) ý tưởng thành đầy đủ sự triển khai và sự xác nhận các chiến lược. Cho đơn-máy móc việc phục vụ với nhiều mô hình các phiên bản (instances), như việc chạy một vài Mở Nơ-ron Mạng Trao đổi Thời gian chạy các phiên (sessions), bộ khung và hệ điều hành xử lý yêu cầu việc xếp hàng đợi Runtime sessions, the framework and operating system handle request queuing). Đầy đủ tính phức tạp của tải việc cân bằng trở nên cần thiết khi việc mở rộng tới phân tán sự suy luận các hệ thống, nơi nhiều các máy móc phục vụ giống nhau mô hình. Sự triển khai các chi tiết của yêu cầu sự phân phối các thuật toán và đa-bản sao các kiến trúc thuộc về phân tán ngữ cảnh. Khi công suất sự lập kế hoạch xem xét “máy chủ” trong này đơn-máy móc việc phục vụ sự phân tích, nó có nghĩa máy móc’s mô hình việc phục vụ công suất. Xếp hàng đợi các động lực được phân tích trong phần 13.5 áp dụng để hiểu đơn-máy móc hành vi và việc xác định khi nào việc mở rộng tới nhiều các máy móc trở nên cần thiết. Trong khi tải các bộ cân bằng phân phối các yêu cầu qua các bản sao, việc đạt được có thể đoán trước độ trễ cũng yêu cầu việc kiểm soát gì xảy ra bên trong mỗi máy móc. Hệ điều hành môi trường giới thiệu của riêng nó các nguồn của tính biến đổi.
13.2.4 Có tính quyết định (Deterministic) độ trễ và tài nguyên sự cô lập Một sự suy luận máy chủ không hoạt động trong sự cô lập. Trên một đơn máy móc, hệ điều hành quản lý nhiều cạnh tranh các tiến trình (việc ghi nhật ký các tác nhân, việc giám sát các công cụ, và hệ thống các ngắt (interrupts)) thứ mà có thể một cách gián đoạn (intermittently) đánh cắp CPU các chu kỳ từ sự suy luận đường ống that can intermittently steal CPU cycles from the inference pipeline). Những “ồn ào những người hàng xóm” này là một chính nguồn của độ trễ sự bồn chồn (jitter), nơi thời gian được yêu cầu để xử lý giống hệt các yêu cầu biến đổi một cách đáng kể, việc gây ra thứ 99 phân vị độ trễ bùng nổ thậm chí khi phần cứng bị sử dụng dưới mức (underused) (These “noisy neighbors” are a primary source of latency jitter, where the time required to process identical requests varies significantly, causing the 99th percentile (P99) latency to spike even when the hardware is underused). Các đuôi độ trễ sự bùng nổ từ hình 13.1 minh họa giống nhau sự bùng nổ, nhưng ở đây trình kích hoạt (trigger) là tài nguyên sự tranh chấp thay vì việc xếp hàng đợi. Việc đạt được có tính quyết định hiệu suất trên một đơn nút yêu cầu việc giảm thiểu sự can thiệp từ hệ điều hành’s bình thường tài nguyên-việc chia sẻ hành vi. Có thể đoán trước việc phục vụ các hệ thống như Clock- work cho thấy rằng DNN sự suy luận có thể đáp ứng chặt chẽ cấp độ-yêu cầu các SLO khi việc lập lịch và sự thực thi được kiểm soát một cách cẩn thận). CPU ái lực (affinity) (việc ghim (pinning)) là một cục bộ sự cô lập công cụ: nó hạn chế sự suy luận máy chủ’s các luồng tới cụ thể vật lý các lõi do đó nhạy cảm-độ trễ công việc là ít phơi bày (hơn) đối với luồng sự di chuyển và bộ nhớ đệm-tính cục bộ (locality) sự mất mát is one local isolation tool: it restricts the inference server’s threads to specific physical cores so latency-sensitive work is less exposed to thread migration and cache-locality loss). Việc ghim có thể giảm một nguồn của độ trễ sự bồn chồn, nhưng nó là phần của một rộng hơn tài nguyên-sự cô lập chiến lược thay vì một hoàn chỉnh giải pháp. Bộ nhớ việc khóa (mlock) giải quyết một có liên quan nhưng khác biệt nguồn của sự bồn chồn addresses a related but distinct source of jitter). Bằng mặc định, OS có thể phân trang (page) bất kỳ bộ nhớ vùng (region) tới đĩa dưới bộ nhớ áp lực. Nếu GPU’s DMA động cơ bắt đầu việc đọc mô hình các trọng số từ một vùng thứ mà (đã) bị phân trang ra (paged out), sự truyền (transfer) đình trệ (stalls) cho đến khi dữ liệu được lỗi (faulted) quay lại vào RAM, một hình phạt được đo lường trong các mili giây thay vì các micro giây. Việc khóa mô hình các trọng số và KV các bộ nhớ đệm trong vật lý RAM đảm bảo nhất quán truy cập các thời gian, mặc dù sự đánh đổi là rằng được ghim bộ nhớ không thể được đòi lại (reclaimed) bởi khác tiến trình. (Kỹ thuật thứ) ba kỹ thuật, ngắt sự che chắn (shielding), hoàn thành sự cô lập bức tranh. Mạng và lưu trữ các ngắt được định tuyến tới sự suy luận các lõi có thể chiếm quyền ưu tiên (preempt) GPU lệnh sự đệ trình (submission) tại không thể đoán trước các khoảnh khắc. Việc hướng (Steering) những các ngắt này tới phi sự suy luận các lõi đảm bảo rằng các sự bùng nổ của đến lưu lượng truy cập (do) không phá vỡ (disrupt) GPU’s lệnh luồng, thứ mà là đặc biệt quan trọng cho việc duy trì ổn định đuôi độ trễ dưới tải. Những sự cô lập các nguyên tắc này biến đổi một đơn giản “mô hình kịch bản” thành một có tính quyết định dịch vụ, một sự chuyển- tiếp (transition) thiết yếu cho tới hạn-an toàn các ứng dụng như tự trị việc lái xe hay thời gian-thực công nghiệp sự kiểm soát. Sự triển khai phổ, tải việc cân bằng, và tài nguyên sự cô lập xác định nơi các mô hình phục vụ và cái gì cơ sở hạ tầng hỗ trợ chúng. (Vấn đề) còn lại câu hỏi là cách việc phục vụ phần mềm chính nó được tổ chức, một cách cụ thể nào các thành phần bao gồm một sự suy luận máy chủ và cách chúng điều phối (coordinate) để biến không đều (irregular) người dùng lưu lượng truy cập thành hiệu quả phần cứng sự sử dụng.

13.3 Việc phục vụ Hệ thống Kiến trúc

Sự suy luận
Máy chủ:
Google’s TensorFlow Serving (Olston et al.
2017) đã giúp
thiết lập sự tách biệt của
mô hình logic từ việc phục vụ cơ sở hạ tầng (Google’s TensorFlow Serving (Olston et al. 2017) helped establish the separation of model logic from serving infrastructure); NVIDIA’s Tri-
ton (NVIDIA 2024d) mở rộng
này mẫu qua nhiều
mô hình
các bộ khung (frameworks)
và các chương trình phụ trợ (backends) (NVIDIA’s Triton (NVIDIA 2024d) extends this pattern across multiple model frameworks and backends). Chí mạng thiết kế
sự thấu hiểu là rằng một bộ lập lịch
và động bộ tạo lô biến không đều đơn-yêu cầu lưu lượng truy cập thành thân thiện-với-máy gia tốc sự thực-
thi, việc cải thiện sự sử dụng
khi độ trễ các ngân sách cho phép việc tạo lô.
Chính xác sự sử dụng
các lợi ích
phụ thuộc
trên mô hình,
phần cứng, đến tỷ lệ (arrival rate), và
được cấu hình (configured)
việc tạo lô cửa sổ (window).

NCHW và NHWC (Ten- sor Bộ nhớ Các bố cục (Tensor Memory Layouts)): Những
các từ viết tắt này mã hóa (encode) bộ-
nhớ bố cục thứ tự của 4D hình ảnh
các tensor: N (lô), C (các kênh (channels)), H (chiều cao), W (chiều rộng).
NCHW đặt tất cả các giá trị cho một kênh một cách liền kề (contiguously), việc kích- hoạt được vector hóa sự tích chập (convolution)
trên các GPU; NHWC xen kẽ (interleaves) các kênh tại mỗi không gian (spatial) vị- trí, việc căn chỉnh (aligning) tốt hơn với
CPU đơn lệnh (instruction), nhiều (mul- tiple) dữ liệu (SIMD) các lệnh.
Một định dạng sự không khớp giữa
máy khách và máy chủ có thể tạo ra
không chính xác các tensor thậm chí khi
hình dạng xuất hiện hợp lệ, do đó
việc phục vụ mã nên làm (cho) bố- cục các sự chuyển đổi (trở nên) rõ ràng.
13.3 Việc phục vụ Hệ thống Kiến trúc Người dùng các yêu cầu đến trong không thể đoán trước các sự bùng nổ, một mili giây cách nhau, sau đó năm các giây của sự im lặng, trong khi các máy gia tốc đòi hỏi ổn định, có kích thước-đồng đều (uniformly-sized) các lô. Việc thu hẹp này khoảng cách yêu cầu nhiều hơn một Python kịch bản việc gọi model.predict(); nó yêu cầu một được chuyên môn hóa phần mềm kiến trúc thứ mà hấp thụ lưu lượng truy cập tính biến đổi, hình thành (forms) hiệu quả các lô, và giữ phần cứng bị bão hòa mà không có việc vi phạm độ trễ các SLO; it requires a specialized software architecture that absorbs traffic variability, forms efficient batches, and keeps hardware saturated without violating latency SLOs).
13.3.1 Nội bộ kiến trúc và yêu cầu luồng Mô hình sự tối ưu hóa tập trung trên toán học hiện vật (artifact), trong khi mô hình việc phục vụ yêu cầu một được chuyên môn hóa phần mềm kiến trúc để quản lý cao-tần số (high-frequency) yêu cầu các luồng và phần cứng sự sử dụng. Một sự suy luận máy chủ3 (như NVIDIA Triton, TensorFlow Serving, hay TorchServe) là không (phải) một đơn giản vỏ bọc (wrapper) xung quanh một mô hình kịch bản; nó là một cao-hiệu suất bộ lập lịch thứ mà quản lý tính đồng thời, bộ nhớ, và dữ liệu sự di chuyển is not a simple wrapper around a model script; it is a high-performance scheduler that manages concurrency, memory, and data movement). Nội bộ giải phẫu học (anatomy) của những các máy chủ này tiết lộ cách chúng thu hẹp khoảng cách giữa không đều người dùng lưu lượng truy cập và cao độ (highly) đều đặn, định hướng-vào-lô (batch-oriented) các yêu cầu của các máy gia tốc. Mọi yêu cầu đi ngang qua (traverses) một nhiều-giai đoạn đường ống được thiết kế để tối đa hóa phần cứng thông lượng trong khi việc tối thiểu hóa độ trễ chi phí hoạt động.
Hình 13.4 tách biệt sáu các giai đoạn do đó mỗi thành phần’s vai trò trong việc hấp thụ lưu lượng truy cập, việc xếp hàng đợi, việc tạo lô, và máy gia tốc sự thực thi là rõ ràng.
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
Yêu cầu Việc lưu bộ đệm (Buffering) Thông lượng Sự tối ưu hóa (Throughput Opt.)
Sự thực thi
Sự tối ưu hóa (Execution Opt.)
Hình 13.4: Sự suy luận Máy chủ Giải phẫu học: Một hiện đại sự suy luận máy chủ tách rời (decouples) mạng việc xử lý khỏi máy gia tốc sự thực thi thông qua một được chia giai đoạn đường ống. Mỗi giai đoạn cô lập một mối quan tâm, từ việc hấp thụ bùng nổ lưu lượng truy cập tới việc hình thành hiệu quả các lô, do đó phần cứng máy gia tốc ở lại cao độ sử dụng mặc dù không đều đến các mẫu. Này kiến trúc phục vụ ba các chức năng. Đầu tiên, tính đồng thời sự quản lý: các máy chủ sử dụng không đồng- bộ (asynchronous) sự kiện các vòng lặp hay luồng các hồ (pools) để xử lý hàng nghìn của đồng thời máy khách các kết nối mà không có việc chặn (blocking), việc đảm bảo rằng mạng I/O chờ các thời gian không (làm) rảnh rỗi (idle) máy gia tốc. (Chức năng thứ) hai, yêu cầu sự biến- đổi: máy chủ chuyển đổi mạng các tải trọng (payloads), như JavaScript Đối tượng Ký hiệu hay Protobuf, thành cụ thể tensor các định dạng được yêu cầu bởi được tối ưu hóa mô hình thời gian chạy or Protobuf, into the specific tensor formats required by the optimized model runtime). Hình ảnh các tensor, cho ví dụ, có thể được lưu trữ như NCHW4 (lô, các kênh, chiều cao, chiều rộng) hay NHWC (lô, chiều cao, chiều rộng, các kênh) or NHWC). PyTorch và TensorRT thích NCHW bởi vì nó đặt kênh dữ liệu một cách liền kề, việc kích hoạt hiệu quả sự tích chập trên các GPU. TensorFlow mặc định (đến) NHWC, thứ mà là hiệu quả hơn trên các CPU. (Chức năng thứ) ba, mô hình sự quản lý: sự suy luận các máy chủ quản lý vòng đời của được tải mô hình các hiện vật, bao gồm việc tải các trọng số vào VRAM, việc theo dõi nào hiện vật phiên bản là hoạt động, và việc hoàn thành sự khởi động các sự suy luận trước khi việc phơi bày mô hình tới trực tiếp lưu lượng truy cập. Đầy đủ các sổ đăng ký (registries) (được tạo phiên bản hiện vật các cửa hàng),

13. Mô hình Việc phục vụ (Model Serving)

Giao thức Các bộ đệm (Proto-
buf): Protobuf sử dụng một được định- nghĩa trước (predefined) lược đồ (từ một.proto
tệp) để mã hóa có cấu trúc dữ liệu
thành một nhỏ gọn nhị phân định- dạng (Giao thức Các bộ đệm Các tác giả (Protocol Buffers Authors) 2026) to encode structured data into a compact binary format). Bởi vì lược đồ mang trường các tên và các kiểu, dây (wire) tải trọng (payload) cần không lặp lại
chúng như JSON làm. Của nó dây
định dạng là vẫn không giống hệt tới
một C++ đối tượng’s trong-bộ nhớ bố- cục, do đó nó yêu cầu một sự phân tích cú pháp (parsing)
bước và không cung cấp giống nhau trực tiếp không-bản sao truy cập
mẫu thứ mà FlatBuffers nhắm- mục tiêu.

FlatBuffers: “phẳng” trong
tên mô tả thiết kế:
nhị phân bộ đệm có thể phục vụ
như được tuần tự hóa sự biểu- diễn (representation) và dữ liệu cấu trúc
đang đọc, việc tránh một riêng- biệt sự phân tích cú pháp hay sự mở gói (unpacking) giai đoạn (phase) cho được hỗ trợ truy cập các mẫu (FlatBuffers Các tác giả (FlatBuffers Authors) 2026) (The “flat” in the name describes the design: the binary buffer can serve as the serialized representation and the data structure being read, avoiding a separate parsing or unpacking phase for supported access patterns (FlatBuffers Authors 2026)). Cho ML sự suy luận, điều này có thể kích hoạt không-bản sao truy cập tới
tensor siêu dữ liệu—việc phục vụ
hệ thống đọc tensor các hình dạng và các phần bù (offsets) một cách trực tiếp từ
bộ đệm thay vì việc cấp phát một thứ hai đối tượng sự biểu diễn.

gRPC (gRPC Từ xa Thủ tục Lệnh gọi (Remote Procedure Call)): gRPC ghép nối (pairs)
HTTP/2 sự vận chuyển với một
giao diện định nghĩa ngôn ngữ
và tin nhắn định dạng, nhất
một cách phổ biến Giao thức Các bộ đệm (gRPC Các tác giả 2026)).
(Sự)
liên quan
việc phục vụ
lợi-
thế (advantage)
là sự kết hợp của có kiểu (typed) các hợp đồng (contracts),
dai dẳng (persistent)
được ghép kênh (multiplexed) các kết nối,
sự phát trực tuyến (streaming) sự hỗ trợ,
và
nhỏ gọn
nhị phân các tin nhắn.
Kích thước và độ trễ lợi ích
so với REST/JSON phụ thuộc trên
tải trọng hình dạng, máy khách/máy chủ
sự triển khai, và liệu
sự tuần tự hóa là một có ý nghĩa
phần chia sẻ
của
đầu cuối-tới-đầu cuối (end-to-end) độ trễ ngân sách (hay không). phát hành các cổng (các sự kiểm tra trước khi phát hành), và khôi phục trạng thái cũ (rollback) sự quản trị (governance) (các quy tắc cho việc hoàn nguyên (reverting) một tồi phát hành) thuộc về Chương 14; cục bộ việc phục vụ mối quan tâm là liệu đúng hiện vật (đã) được tải và sẵn sàng (hay không), and rollback governance belong to Chapter 14; the local serving concern is whether the right artifact is loaded and ready). Trong số những các thành phần này, bộ lập lịch xứng đáng (deserves) đặc biệt sự chú ý bởi vì nó hiện thân (embodies) cốt lõi việc phục vụ sự đánh đổi giữa thông lượng và độ trễ. Bộ lập lịch là “bộ não” của sự suy luận máy chủ. Nó triển khai động việc tạo lô logic được thảo luận trong phần 13.7. Bộ lập lịch phải quyết định liệu chạy một đơn yêu cầu ngay lập tức để tối thiểu hóa của nó độ trễ hay đợi năm các mili giây cho một thứ hai yêu cầu và xử lý chúng cùng nhau để tối đa hóa thông lượng. Các hệ thống những người thiết kế sử dụng Việc tạo lô Cửa sổ tham số để điều chỉnh này sự đánh đổi. Một cửa sổ của 0 ms tối ưu hóa cho thuần túy độ trễ (không việc tạo lô), trong khi một nhỏ bị giới hạn (bounded) cửa sổ để bộ lập lịch đánh đổi một được kiểm soát lượng của việc chờ đợi cho cao hơn máy gia tốc sự sử dụng, while a small bounded window lets the scheduler trade a controlled amount of waiting for higher accelerator utilization). Này quyết định xác định (mức độ) bận rộn như thế nào máy gia tốc ở lại: liệu phần cứng dành của nó thời gian việc tính toán hay việc chờ đợi cho công việc.
13.3.2 Giao diện các giao thức và sự tuần tự hóa Cơ chế được sử dụng để vận chuyển dữ liệu giữa máy khách và máy chủ một cách trực tiếp ảnh hưởng độ trễ ngân sách. Mô hình sự suy luận là thường cao độ được tối ưu hóa, tuy nhiên chi phí của việc di chuyển dữ liệu vào mô hình (sự tuần tự hóa và mạng giao thức chi phí hoạt động) có thể trở thành thống trị nút thắt cổ chai, đặc biệt cho nhẹ (lightweight) các mô hình nơi sự suy luận thời gian là nhỏ can become the dominant bottleneck, especially for lightweight models where inference time is small).
13.3.2.1 Sự tuần tự hóa nút thắt cổ chai ML việc phục vụ các tải trọng là về cơ bản khác biệt từ điển hình web API các tải trọng: chúng bao gồm của nhiều-chiều nổi (float) các mảng (hình ảnh các tensor, sự nhúng các vector, mã thông báo ID các chuỗi (sequences)) thứ mà là dày đặc (dense), nhị phân, và lớn that are dense, binary, and large). Dựa trên-văn bản các định dạng như JSON là phổ biến nhưng về mặt tính toán tốn kém cho loại của dữ liệu này. Sự tuần tự hóa chi phí hoạt động xuất hiện khi việc phân tích cú pháp một JSON đối tượng yêu cầu việc đọc mọi byte, việc xác nhận cú pháp, và việc chuyển đổi văn bản các sự biểu diễn thành bản địa-máy móc (machine-native) các kiểu. Cho tensor các tải trọng, chi phí cộng gộp (compounds): dấu phẩy-động các giá trị phải đầu tiên được mã hóa như ASCII các chữ số (việc thổi phồng (inflating) một 4-byte nổi tới 10–15 các ký tự), và nhị phân dữ liệu như hình ảnh các byte yêu cầu Base64 sự mã hóa, thứ mà thêm 33 phần trăm kích thước chi phí hoạt động trước khi JSON sự phân tích cú pháp bắt đầu (For tensor payloads, the cost compounds: floating-point values must first be encoded as ASCII digits (inflating a 4-byte float to 10–15 characters), and binary data such as image bytes requires Base64 encoding, which adds 33 percent size overhead before JSON parsing begins). Cho cao- thông lượng các hệ thống, điều này tiêu thụ CPU các chu kỳ thứ mà có thể nói cách khác (otherwise) được sử dụng cho yêu cầu việc xử lý hay sự tiền xử lý. Nhị phân các định dạng như Giao thức Các bộ đệm5 (Protobuf) hay FlatBuffers6 giảm này sự phình to (bloat) bằng cách việc sử dụng nhận thức- lược đồ nhị phân các sự mã hóa thay vì văn bản các sự mã hóa or FlatBuffers6 reduce this bloat by using schema-aware binary encodings instead of text encodings). Bản địa nổi các mảng có thể truyền như nhỏ gọn IEEE 754 các byte với không ASCII sự chuyển đổi và không Base64 vỏ bọc. FlatBuffers có thể cũng kích hoạt không-bản sao truy cập trong được hỗ trợ các trường hợp, nơi mạng bộ đệm có thể được đọc mà không có việc cấp phát một riêng biệt đối tượng đồ thị.
13.3.2.2 REST so với gRPC Hai phổ biến các mô hình mẫu định nghĩa việc phục vụ các giao diện, mỗi với khác biệt hệ thống các đặc điểm. REST (Đại diện (Representational) Trạng thái Chuyển giao) điển hình (typically) sử dụng HTTP/1.1 và JSON typically uses HTTP/1.1 and JSON). Nó là rộng rãi được hỗ trợ, có thể đọc- bởi-con người (human-readable), và không trạng thái (stateless), việc làm nó một phổ biến sự lựa chọn cho hướng ra-công chúng (public-facing) các API. Tuy nhiên, REST’s tính không trạng thái ép buộc việc gửi lại ngữ cảnh với mọi lệnh gọi; cho LLM việc phục vụ, nơi một cuộc trò chuyện ngữ cảnh có thể vượt quá 10 KB của mã thông báo các ID, này mỗi-yêu cầu chi phí hoạt động cộng gộp tại cao QPS. Tiêu chuẩn HTTP/1.1 sử dụng dai dẳng TCP các kết nối bằng mặc định, nhưng không có HTTP/2-kiểu sự ghép kênh một máy khách thường cần nhiều các kết nối hay cẩn thận kết nối việc gộp (pooling) để tránh đầu-của-hàng (head-of-line) việc chặn và bắt tay (handshake) chi phí hoạt động sau rảnh rỗi các thời gian chờ (timeouts). JSON sự tuần tự hóa cũng thêm đáng kể độ trễ cho thuộc về số (numerical) dữ liệu như các tensor. Trong sự trái ngược, gRPC (gRPC Từ xa Thủ tục Lệnh gọi)7 sử dụng HTTP/2 và một cách phổ biến sử dụng Protobuf7 uses HTTP/2 and commonly uses Protobuf). HTTP/2 kích hoạt việc ghép kênh nhiều các yêu cầu qua một đơn dai dẳng TCP kết nối, việc giảm thiểu kết nối-sự quản lý chi phí hoạt động và việc cho phép hiệu quả nhị phân sự phát trực tuyến. Protobuf cung cấp có kiểu các lược đồ và hiệu quả nhị phân sự tuần tự hóa, việc làm gRPC một phổ biến sự lựa chọn cho nội bộ dịch vụ-tới- dịch vụ (service-to-service) sự giao tiếp nơi độ trễ và có kiểu các giao diện quan trọng. Một cụ thể tải trọng sự so sánh cho thấy cách sự tuần tự hóa sự lựa chọn thay đổi cả hai dây kích thước và sự phân tích cú pháp chi phí.

13.4 Yêu cầu Vòng đời

Đuôi Độ trễ: Không giống như trung bình, phân vị (percentile) các độ trễ tiết
lộ hiệu suất tác động của hệ thống những ngoại lệ (outliers) phổ biến trong
ML việc phục vụ, như mô hình bộ nhớ đệm các sự bỏ lỡ (misses) hay thu gom rác các sự tạm dừng (pauses). Những hiếm, cao- độ trễ các yêu cầu một cách không tương- xứng (disproportionately) làm hại người dùng sự hài lòng (satisfac- tion) và một cách trực tiếp tác động doanh- thu (revenue). Nền tảng các nghiên cứu tại
Google và Amazon (đã) định-
lượng này mối quan hệ, việc tìm thấy
rằng 100 ms của được thêm độ trễ tốn ~1 phần trăm trong các doanh số bán hàng (sales), việc thiết- lập phân vị các mục tiêu (p95,
p99) như là chí mạng các số liệu cho dịch vụ chất lượng. Khăn ăn Toán học 13.2: JSON so với Protobuf sự tuần tự hóa Hãy xem xét một yêu cầu tải trọng (chứa) đựng 1,000 dấu phẩy động các số (cho ví dụ, một sự nhúng vector). • JSON: Sử dụng ~9 KB trên dây. Yêu cầu ~50 μs để phân tích cú pháp. • Protobuf: Sử dụng ~4 KB trên dây. Yêu cầu ~5 μs để phân tích cú pháp. Toán học: Việc chuyển đổi (Switching) một yêu cầu sang nhị phân tải trọng tiết kiệm 50 μs −5 μs = 45 μs của phân tích cú pháp thời gian. Cho này mang tính minh họa hệ thống việc xử lý 10,000 các yêu cầu mỗi giây, các khoản tiết kiệm (savings) cộng gộp thành 10,000 × 45 μs = 0.45 s của CPU thời gian được đòi lại mọi bức tường-đồng hồ giây, thứ mà là 45 phần trăm của một lõi được giải phóng từ sự tuần tự hóa chi phí hoạt động một mình (alone). Các hệ thống sự thấu hiểu: Này 10× kịch bản lợi ích làm gRPC/Protobuf, FlatBuffers, hay khác nhị phân giao thức một mạnh ứng cử viên cho cao-thông lượng nội bộ các vi dịch vụ khi sự tuần tự hóa là một có thể nhìn thấy (visible) phần của độ trễ ngân sách. Hệ thống sự lựa chọn là phụ thuộc-sự ép buộc (constraint-dependent). REST/HTTP là phổ biến khi công cộng tính tương thích (compatibil-ity), việc gỡ lỗi, và hệ sinh thái phạm vi tiếp cận (reach) thống trị. gRPC/Protobuf, hay (một) khác nhị phân giao thức, được ưa chuộng (favored) khi nội bộ cao-QPS tensor lưu lượng truy cập, kết nối sự tái sử dụng, hay sự phát trực tuyến làm sự tuần tự hóa (thành) một có ý nghĩa phần chia sẻ của độ trễ và CPU ngân sách. Thuộc về kiến trúc các thành phần và các giao thức được kiểm tra cho đến nay (so far) mô tả cách việc phục vụ các hệ thống được xây dựng. Việc hiểu tại sao nhất định các cấu hình (configurations) thực hiện tốt hơn yêu cầu việc phân tích gì xảy ra đối với cá nhân các yêu cầu khi chúng đi ngang qua những các thành phần này.
13.4 Yêu cầu Vòng đời Một đơn HTTP yêu cầu (chứa) mang một 224×224 JPEG hình ảnh đến tại một sự suy luận máy chủ. Giữa khoảnh khắc (đầu) tiên byte đi vào mạng ngăn xếp và khoảnh khắc sự phân loại kết quả rời đi, đó yêu cầu đi ngang qua sáu đường ống các giai đoạn, mỗi việc tiêu thụ các mili giây thứ mà người dùng trải nghiệm như chờ thời gian. Việc hiểu nơi thời gian đi (đến) bên trong mỗi yêu cầu là thiết yếu cho hiệu quả sự tối ưu hóa: một (người) không thể cải thiện gì một (người) không (đo) lường.
13.4.1 Độ trễ ngân sách Cho động sự suy luận các hệ thống, việc phục vụ sự đảo ngược được thiết lập trong phần 13.1 tạo ra một độ trễ ngân sách thứ mà định hình hệ thống thiết kế). Một việc phục vụ hệ thống với cấp độ-giây (second-scale) mỗi- yêu cầu độ trễ có thể bỏ lỡ nhiều tương tác các SLO, thậm chí nếu nó đạt được xuất sắc thông lượng. (Sự) liên quan các số liệu dịch chuyển từ tổng hợp thông lượng tới độ trễ các sự phân phối. Trung bình (Mean) độ trễ tiết lộ ít về người dùng trải nghiệm; p50, p95, và p99 các độ trễ tiết lộ cách hệ thống thực hiện qua đầy đủ phạm vi (range) của các yêu cầu. Nếu trung bình độ trễ là 50 ms nhưng p99 là hai các giây, một trong một trăm những người dùng đợi 40× lâu hơn so với trung bình. Cho hướng đến-người tiêu dùng các ứng dụng, những đuôi các độ trễ này thường xác định người dùng sự hài lòng và sự giữ lại (retention).8 Việc quản lý những phân vị các sự ép buộc này yêu cầu việc phân rã (decomposing) tổng cho phép phản hồi thời gian thành một độ trễ ngân sách thứ mà phân bổ (allocates) thời gian qua mỗi việc xử lý giai đoạn.
Định nghĩa 13.2: Độ trễ ngân sách Độ trễ Ngân sách là thời gian vốn được phân bổ tới một ML sự suy luận yêu cầu, một cách nghiêm ngặt bị giới hạn bởi đầu cuối-tới-đầu cuối dịch vụ cấp độ mục tiêu (SLO)).
1. Tầm quan trọng: Nó hoạt động (acts) như một tổng-bằng không (zero-sum) sự ép buộc hệ thống nơi bất kỳ các mili giây được tiêu thụ bởi sự tuần tự hóa hay mạng chi phí hoạt động một cách trực tiếp giảm độ trễ ngân sách (𝐿lat) có sẵn cho mô hình sự suy luận (It acts as a zero-sum constraint system where any milliseconds consumed by serialization or network overhead directly reduce the latency budget (𝐿lat) available for model inference).
2. Sự khác biệt: Không giống như trung bình độ trễ, thứ mà giấu phương sai, một độ trễ ngân sách là một cứng ranh giới (bound) thứ mà phải được duy trì cho chậm nhất các yêu cầu (cho ví dụ, p99)).

13. Mô hình Việc phục vụ (Model Serving)

Sự suy luận là một lát cắt của độ-
trễ ngân sách; sự tiền xử lý sánh- ngang (rivals) nó.
3. Phổ biến cạm bẫy: Một thường xuyên quan niệm sai lầm là rằng “mô hình” có toàn bộ ngân sách. Trong thực tế, mô hình thường có ít hơn 50 phần trăm của tổng ngân sách; phần còn lại (remainder) là được tiêu thụ bởi yêu cầu vòng đời (DNS, TLS, tải việc cân bằng, sự tuần tự hóa)). Trước khi việc tính toán một đầy đủ ngân sách, này trạm kiểm soát thiết lập (đặt) nền tảng độ trễ-sự phân tích các kỹ năng mọi việc phục vụ kỹ sư cần. Trạm kiểm soát 13.1: ResNet-50 độ trễ sự phân tích Việc phục vụ tối ưu hóa đuôi độ trễ dưới tải. Sử dụng này trạm kiểm soát để tách biệt việc xếp hàng đợi và việc tạo lô các hiệu ứng trước khi việc chọn một sự tối ưu hóa. □Hàng đợi hành vi: Sử dụng hình 13.1 để mô tả tại sao độ trễ tăng phi tuyến tính (nonlinearly) khi sự sử dụng tiếp cận sự bão hòa. □Việc tạo lô sự đánh đổi: So sánh thông lượng lợi ích từ lớn hơn các lô đối nghịch (against) độ trễ chi phí mỗi yêu cầu. Mọi việc phục vụ yêu cầu phân rã (decomposes) thành ba các giai đoạn thứ mà mỗi tiêu thụ (một) phần của độ trễ ngân sách. Sự tiền xử lý biến đổi thô đầu vào như hình ảnh các byte hay văn bản các chuỗi (strings) thành sẵn sàng-cho-mô hình các tensor. Sự suy luận thực thi mô hình sự tính toán. Sự hậu xử lý biến đổi mô hình các đầu ra thành hướng-tới-người dùng các phản hồi. Nhanh hơn phần cứng không một cách tự động có nghĩa nhanh hơn việc phục vụ. Trong thực tế, sự tiền xử lý và sự hậu- xử lý có thể thống trị tổng độ trễ khi sự suy luận chạy trên được tối ưu hóa các máy gia tốc. Việc tối ưu hóa một cách độc quyền (exclusively) sự suy luận giai đoạn mang lại (yields) giảm dần (diminishing) các lợi tức nếu xung quanh đường ống (vẫn) duy trì bị thắt cổ chai bởi CPU các hoạt động.
13.4.2 Độ trễ sự phân phối sự phân tích Việc hiểu nơi thời gian đi (đến) yêu cầu việc trang bị (instrumenting) mỗi giai đoạn một cách độc lập. Một ResNet-50 độ trễ ngân sách sự cố (việc chia nhỏ (breakdown)) tiết lộ một cách chính xác cách mỗi mili giây được dành khi của chúng ta bộ phân loại nhận một JPEG hình ảnh. Các hệ thống Góc nhìn 13.3: ResNet-50: Độ trễ ngân sách sự cố
Bảng 13.3 chia nhỏ (breaks down) một điển hình ResNet-50 việc phục vụ yêu cầu (thành) mỗi (per) giai đoạn:
Bảng 13.3: ResNet-50 độ trễ ngân sách: Mỗi-giai đoạn sự cố của một đơn việc phục vụ yêu cầu, việc cho thấy rằng sự tiền xử lý và dữ liệu sự truyền cùng nhau sánh ngang chi phí của ResNet-50 chuyển tiếp vượt qua chính nó. Các tỷ lệ phần trăm (percentages) phơi bày nơi kỹ thuật nỗ lực thực sự được đền đáp (pays off), thứ mà là hiếm khi trong mô hình. Mỗi-giai đoạn các tỷ lệ phần trăm được làm tròn tới gần nhất nguyên số và có thể không tính tổng tới chính xác 100.
Giai đoạn
Hoạt động (Operation)
Thời gian
Tỷ lệ phần trăm
Sự tiền xử lý
JPEG sự giải mã (decode)
3 ms
30%
Sự tiền xử lý Thay đổi kích thước (Resize) tới 224×224
1 ms
10%
Sự tiền xử lý Chuẩn hóa (Normalize) (trung bình/độ lệch chuẩn (std))
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
100% Các hệ thống sự thấu hiểu: ResNet-50 việc phục vụ ngân sách cho thấy sự tiền xử lý tiêu thụ 44.6 phần trăm của độ trễ mặc dù mô hình sự suy luận là chuyên sâu-về mặt-tính toán giai đoạn. Với TensorRT sự tối ưu hóa việc giảm thiểu sự suy luận xuống 2 ms, sự tiền xử lý (sẽ) thống trị tại 63.4 phần trăm. ResNet ví dụ đại diện giới hạn-tính toán sự suy luận nơi chuyển tiếp-vượt qua số học (arithmetic) thống trị độ trễ ngân sách. Việc áp dụng giống nhau bộ khung tới một khác biệt mô hình kiến trúc thường tiết lộ rằng nút thắt cổ chai dịch chuyển từ tính toán sang bộ nhớ băng thông, việc vô hiệu hóa (invalidating) sự tối ưu hóa các chiến lược thứ mà (đã) làm việc cho thị giác các mô hình. Sự giới thiệu các hệ thống thể hiện chính xác này sự dịch chuyển. Ngọn hải đăng (Lighthouse) 13.1: Ngọn hải đăng ví dụ: DLRM việc phục vụ Kịch bản: Việc phục vụ DLRM với một 10 ms P99 độ trễ ngân sách. Sự phân tích: Trong khi ResNet-50’s mô hình giai đoạn bị thống trị bởi tích chập nơ-ron mạng (CNN) tính toán, DLRM’s thống trị mô hình-giai đoạn chi phí là sự nhúng-bảng bộ nhớ truy cập (Analysis: While ResNet-50’s model stage is dominated by convolutional neural network (CNN) compute, DLRM’s dominant model-stage cost is embedding-table memory access). Đầu cuối-tới-đầu cuối việc phục vụ các nút thắt cổ chai vẫn yêu cầu việc đo lường đầy đủ con đường: sự tiền xử lý, sự suy luận, sự hậu xử lý, và dữ liệu sự di chuyển. Bảng 13.4 chia nhỏ sự giới thiệu yêu cầu (thành) mỗi giai đoạn:
Bảng 13.4: DLRM việc phục vụ độ trễ: Mỗi-giai đoạn sự cố của một sự giới thiệu yêu cầu dưới một 10 ms p99 ngân sách, việc đối chiếu (contrasting) DLRM’s giới hạn-bộ nhớ-băng thông sự nhúng các sự tra cứu (lookups) đối nghịch ResNet-50’s giới hạn-tính toán chuyển tiếp vượt qua. Việc thêm tính toán tới sự suy luận giai đoạn không giúp một khi sự nhúng-bảng băng thông là việc ràng buộc sự ép buộc.
Giai đoạn
Hoạt động
Thời gian
Nút thắt cổ chai (Bottleneck)
Đầu vào Sự phân tích cú pháp (Parsing)
Yêu cầu sự phân tích cú pháp
0.5 ms
CPU
Sự nhúng Việc tra cứu (Look(up)) Việc lấy (Fetch) 100+ dày đặc các vector
6 ms
bộ nhớ băng thông
Sự suy luận
MLP chuyển tiếp vượt qua
1.5 ms
Tính toán
Sự hậu xử lý Xếp hạng (Ranking) & Việc lọc (Filtering)
1 ms
CPU
Tổng cộng
9 ms Các hệ thống sự thấu hiểu: Trong DLRM, “Sự suy luận” nhiều lớp perceptron giai đoạn là chỉ ~17 phần trăm của độ trễ (Systems insight: In DLRM, the “Inference” multilayer perceptron (MLP) stage is only ~17 percent of the latency). Phần lớn của thời gian được dành trong sự nhúng các sự tra cứu, việc truy xuất khổng lồ (massive) 128-chiều (dim) các vector từ quy mô-terabyte (terabyte-scale) các bảng. Đây là một bộ nhớ-băng thông và giới hạn-công suất (capacity-bound) khối lượng công việc nơi việc thêm nhiều hơn tính toán không giúp trừ khi sự nhúng các bảng có thể được phục vụ nhanh hơn. Hai ngọn hải đăng các trường hợp minh họa giống nhau chung thất bại chế độ: đơn giản (straightforward) sự tối ưu hóa các nỗ lực nhắm mục tiêu nơi ML chuyên môn áp dụng (mô hình sự lượng tử hóa, sự cắt tỉa) trong khi việc ràng buộc sự ép buộc ngồi ở nơi khác (hình ảnh sự giải mã trên CPU cho ResNet-50, sự nhúng-bảng bộ nhớ băng thông cho DLRM) while the binding constraint sits elsewhere). Mẫu khái quát hóa (generalizes): bất kỳ việc phục vụ hệ thống nơi mô hình chiếm ít hơn một nửa của tổng độ trễ (sẽ) thấy giảm dần các lợi tức từ chỉ-mô hình các sự tối ưu hóa, bất kể (mức độ) lớn như thế nào những cá nhân các sự tăng tốc (speedups) đó là. Amdahl’s Định luật định lượng trần. Việc áp dụng định lượng cách tiếp cận tới việc phục vụ phơi bày những ẩn các nút thắt cổ chai này trước khi kỹ thuật nỗ lực bị phân bổ sai (misallocated). Khăn ăn Toán học 13.3: Định lượng cách tiếp cận tới việc phục vụ Amdahl’s Định luật tại (nơi) làm việc (phần D.2.3 cung cấp chính thức sự dẫn xuất (derivation)): sự tiền xử lý (4.5 ms) và dữ liệu sự truyền (0.5 ms) tiêu thụ 49.5 phần trăm của tổng độ trễ (Amdahl’s Law at work (section D.2.3 provides the formal derivation): preprocessing (4.5 ms) and data transfer (0.5 ms) consume 49.5 percent of total latency). Việc tối ưu hóa mô hình 10× nhanh hơn (5 ms → 0.5 ms) mang lại chỉ 1.8× đầu cuối-tới-đầu cuối sự tăng tốc (từ 10.1 ms tới 5.6 ms) (Optimizing the model 10× faster (5 ms →0.5 ms) yields only 1.8× end-to-end speedup). Đây là tại sao việc tập trung một cách độc quyền trên mô hình sự tối ưu hóa (sự lượng tử hóa, sự cắt tỉa) thường gây thất vọng: nút thắt cổ chai là ở nơi khác often disappoints: the bottleneck is elsewhere). DSA tính hiệu quả: Chung-mục đích các CPU đạt được chỉ 1–2 phần trăm của đỉnh hiệu suất tại lô-1 bởi vì lệnh chi phí hoạt động thống trị. Các DSA như các TPU và Tensor Các lõi thay thế phức tạp logic với dày đặc nhân-tích lũy các mảng, việc đạt được 10–100× cao hơn số học (arithmetic) cường- độ (intensity) arrays, achieving 10–100× higher arithmetic intensity). Điều này làm phần cứng sự gia tốc (thành) một thuộc về kinh tế yêu cầu cho nhiều cao-thông lượng hay thấp-độ trễ việc phục vụ các khối lượng công việc. Các hệ thống sự thấu hiểu: Lập hồ sơ (Profile) trước khi việc tối ưu hóa. Nếu sự tiền xử lý thống trị, được gia tốc-GPU các đường ống (NVIDIA DALI) có thể vượt trội (outperform) mô hình sự lượng tử hóa may outperform model quantization). Việc di chuyển sự tiền xử lý gần hơn tới máy gia tốc có thể giảm thiểu có thể tránh (avoidable) CPU-GPU các sự truyền, nhưng đầu cuối-tới-đầu cuối lợi ích là cụ thể-đường ống (pipeline-specific). Hiệu quả sự tối ưu hóa nhắm mục tiêu lớn nhất thời gian (những người) tiêu dùng đầu tiên.

13. Mô hình Việc phục vụ (Model Serving)

13.4.2.1 Việc phục vụ thuế hóa đơn Vượt ra ngoài mô hình sự thực thi chính nó, mọi yêu cầu trả một “thuế” (tax) tới việc phục vụ cơ sở hạ tầng. Bảng 13.5 cung cấp đại diện chi phí hoạt động các phạm vi cho một cao-hiệu suất sự suy luận yêu cầu (cho ví dụ, ResNet- 50 sự phân loại)).
13.4.2.2 Kẻ giết người các micro giây vấn đề Barroso, Patterson, và các đồng nghiệp (colleagues) (đã) xác định một chí mạng khoảng trống trong cách các hệ thống xử lý độ trễ tại khác biệt thời gian các quy mô). Các hoạt động trong micro giây phạm vi là quá ngắn cho truyền thống OS sự lập lịch (thứ mà hoạt động tại mili giây độ chi tiết (granularity)) tuy nhiên quá dài để đơn giản quay-đợi (spin-wait) mà không có việc lãng phí CPU các chu kỳ yet too long to simply spin-wait without wasting CPU cycles). Này “kẻ giết người các micro giây” chế độ (regime) quan trọng trong hiện đại việc phục vụ các khối lượng công việc. Việc sử dụng đại diện các phạm vi trong bảng 13.5, sự tuần tự hóa tại 50–500 μs, sự phân phối tại 10–50 μs, và dữ liệu bản sao tại 100–500 μs là mỗi một cách cá nhân (individually) nhỏ, nhưng cho một 5 ms sự suy luận dịch vụ, những được nêu tên quy mô-micro giây (microsecond-scale) các chi phí hoạt động này một cách tập thể tiêu thụ khoảng 3.2 phần trăm tới 21 phần trăm của độ trễ ngân sách trước khi mạng và việc xếp hàng đợi các sự chậm trễ được tính. Không đơn chi phí hoạt động biện minh (cho) sự tối ưu hóa trong sự cô lập, tuy nhiên cùng nhau chúng xác định liệu hệ thống đáp ứng của nó SLO (hay không).
Bảng 13.5: Việc phục vụ Thuế Hóa đơn: Một đại diện sự cố của phi sự suy luận (noninference) độ trễ các nguồn. Trong khi cá nhân các thành phần như sự tuần tự hóa có vẻ nhỏ (< 1 ms), chúng cộng gộp, they compound). Trong một 5 ms sự suy luận dịch vụ, này “thuế” có thể dễ dàng tiêu thụ 50 phần trăm của độ trễ ngân sách. Chính kỹ thuật mục tiêu là để giảm thiểu những các chi phí này thông qua thuộc về kiến trúc các sự lựa chọn như nhị phân các giao thức, dai dẳng các kết nối, và không-bản sao dữ liệu các con đường.
Thuế Thành phần (Tax Component)
Điển hình Chi phí (Typical Cost)
Sự mở rộng Hành vi
Thuế Sự trốn tránh (Evasion) Chiến lược
Mạng I/O
1-5 ms
Tuyến tính với tải trọng Sự nén, Vùng Sự sắp xếp cùng chỗ (Colocation)
Sự tuần tự hóa
50–500 𝜇s
Tuyến tính với tải trọng
gRPC/Protobuf (so với JSON)
Việc xếp hàng đợi
0.1-10 ms
Theo cấp số nhân (Exponential) với/ tải Động Việc tạo lô, Tự động mở rộng (Autoscaling)
Sự phân phối (Dispatch)
10–50 𝜇s
Hằng số (Constant) mỗi lô Hạt nhân Sự hợp nhất (Kernel Fusion) (việc giảm thiểu các sự khởi chạy (launches))
Dữ liệu Bản sao (Data Copy)
100–500 𝜇s
Tuyến tính với tensor
Không-Bản sao/Được chia sẻ Bộ nhớ Độ trễ ngân sách bộ khung cung cấp một có hệ thống (systematic) cách tiếp cận tới này cộng gộp vấn đề. Sự đo- lường đến (trước) tiên: không có mỗi-giai đoạn sự trang bị (instrumentation), các kỹ sư không thể phân biệt (distinguish) một sự tiền xử- lý nút thắt cổ chai khỏi một sự tuần tự hóa nút thắt cổ chai, và sự tối ưu hóa nỗ lực bị phân bổ sai tới nhất có thể nhìn thấy thành phần (mô hình) thay vì đắt nhất một rather than the most expensive one). Một khi sự đo lường tiết lộ thực sự sự phân phối của thời gian, kỹ thuật nỗ lực nên chảy một cách tương ứng (proportionally)—một giai đoạn việc tiêu thụ 50 phần trăm của độ trễ xứng đáng (nhiều) hơn sự chú ý (hơn) so với một (giai đoạn) việc tiêu thụ 5 phần trăm, bất kể (giai đoạn) nào cảm thấy dễ kiểm soát (tractable) hơn. Thuộc về kiến trúc các sự thay đổi như được gia tốc-GPU sự tiền xử lý hay quyết liệt (aggressive) việc tạo lô có thể dịch chuyển công việc giữa các giai đoạn hoàn toàn, đôi khi việc loại bỏ một nút thắt cổ chai thay vì đơn thuần việc giảm thiểu nó.
13.4.3 Độ phân giải và đầu vào kích thước các sự đánh đổi Đầu vào độ phân giải ảnh hưởng cả hai sự tiền xử lý và sự suy luận độ trễ, nhưng mối quan hệ khác biệt (khác nhau) tùy thuộc (vào) việc liệu hệ thống là giới hạn-tính toán (bị giới hạn bởi số học thông lượng) hay giới hạn-bộ nhớ (memory-bound) (bị giới hạn bởi dữ liệu sự di chuyển) or memory-bound). Một giới hạn-tính toán hệ thống chậm lại một cách tương ứng (proportionally) đối với được làm tăng sự tính- toán; một giới hạn-bộ nhớ hệ thống có thể cho thấy tối thiểu sự chậm lại (slowdown) nếu kích hoạt các tensor vẫn khớp trong nhanh bộ nhớ. Đường mái nhà (roofline) sự phân tích trong phần 11.6 phát triển này sự khác biệt trong chiều sâu (depth), việc làm nó (trở nên) thiết yếu cho được cung cấp thông tin (informed) độ phân giải các quyết định. Cho giới hạn-tính toán các mô hình, phương trình 13.1 chính thức hóa cách thông lượng mở rộng một cách nghịch đảo (inversely) với
độ phân giải bình phương (squared): Thông lượng(𝑟2)/Thông lượng(𝑟1) = (𝑟1/𝑟2)^2 (13.1) Việc nhân đôi độ phân giải từ 224 tới 448 theo lý thuyết (theoretically) mang lại 4× sự chậm lại (được đo lường: 3.6× do cố định chi phí hoạt động sự khấu hao (amortization)) (Doubling resolution from 224 to 448 theoretically yields 4× slowdown (measured: 3.6× due to fixed overhead amortization)). Cao hơn độ phân giải cũng dịch chuyển tính toán-bộ nhớ cân bằng, nhưng hướng tới tính toán: mọi tích chập trọng số được tái sử dụng qua nhiều hơn không gian các vị trí, do đó các FLOP và sự kích hoạt lưu lượng truy cập cả hai phát triển theo phương trình bậc hai (quadratically) trong khi cố định trọng số lưu lượng truy cập được khấu hao, và số học cường độ tăng (rises) xa hơn bên trên đường mái nhà rãnh (ridge) điểm. Việc phục vụ các chi phí của độ phân giải là bậc hai (quadratic) độ trễ sự phát triển và bậc hai sự kích hoạt-bộ nhớ áp lực, không (phải) một băng thông nút thắt cổ chai.

13.4 Yêu cầu Vòng đời
Bảng 13.6 định lượng này sự chuyển tiếp cho ResNet-50.
Bảng 13.6: Độ phân giải và Tính toán Nút thắt cổ chai: ResNet-50 số học cường độ tăng với độ phân giải: các FLOP và sự kích hoạt lưu lượng truy cập phát triển theo phương trình bậc hai trong khi cố định trọng số lưu lượng truy cập được khấu hao trên nhiều hơn không gian các vị trí. Cho một V100 PCIe (14 TFLOP/s FP32; SXM2 biến thể chạy 15.7 TFLOP/s FP32) với 900 GB/s của HBM2 bộ nhớ băng thông, rãnh điểm là xấp xỉ
15.6 FLOP/byte; mọi hàng ngồi bên trên nó, do đó cao hơn độ phân giải lái (drives) khối lượng công việc sâu hơn vào giới hạn-tính toán chế độ (regime) with 900 GB/s of HBM2 memory bandwidth, the ridge point is approximately 15.6 FLOP/byte; every row sits above it, so higher resolution drives the workload deeper into the compute-bound regime). Việc phục vụ các chi phí của độ phân giải là bậc hai độ trễ và sự kích hoạt-bộ nhớ sự phát triển, không (phải) bộ nhớ băng thông.
Độ phân giải
Sự kích hoạt Kích thước
Số học Cường độ
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
13.4.3.1 Độ phân giải các chiến lược trong sản xuất Khác biệt sự triển khai các ngữ cảnh áp đặt khác biệt độ phân giải các yêu cầu được định hình bởi thống trị các sự ép buộc của chúng. Di động các ứng dụng thường chấp nhận thấp hơn độ phân giải (224×224) cho đối tượng sự phát hiện trong camera các kính ngắm (viewfinders), nơi độ trễ và pin tuổi thọ lớn hơn (outweigh) biên (marginal) độ chính xác các lợi ích (Mobile applications often accept lower resolution (224×224) for object detection in camera viewfinders, where latency and battery life outweigh marginal accuracy gains). Y tế việc tạo hình ảnh (imaging) ngồi tại đối diện cực đoan, việc yêu cầu 512×512 hay cao hơn cho chẩn đoán độ chính xác, với được nới lỏng độ trễ các yêu cầu thứ mà cho phép (permit) bổ sung tính toán. Tự trị các phương tiện (vehicles) chia (split) sự khác biệt bằng cách việc sử dụng nhiều các độ phân giải cho khác biệt các tác vụ: thấp độ phân giải cho nhanh chóng sự phát hiện qua rộng các trường (fields) của góc nhìn (view) và cao-độ phân giải các phần cắt (crops) cho mịn-hạt (fine-grained) sự nhận diện (recognition) của được phát hiện các đối tượng. Đám mây các API đối mặt (với) (một) thách thức khác (yet another)—chúng điển hình nhận các hình ảnh tại bất cứ độ phân giải máy khách tải lên và phải xử lý dẫn đến phạm vi một cách tinh tế (gracefully). Tính biến đổi này làm đám mây các API (trở thành) lý tưởng các ứng cử viên cho thích ứng độ phân giải các chiến lược, nơi hệ thống chọn độ phân giải một cách linh hoạt (dynamically) dựa trên nội dung các đặc điểm.
13.4.3.2 Thích ứng độ phân giải Thích ứng độ phân giải để (cho) sản xuất các hệ thống chọn độ phân giải một cách linh hoạt dựa trên nội dung. Một cách tiếp cận chạy một nhẹ bộ phân loại tại 128×128 để phân loại (categorize) nội dung kiểu, sau đó chọn tác vụ- thích hợp độ phân giải với các tài liệu tại 512×512, các phong cảnh tại 224×224, và các khuôn mặt tại 384×384. Điều này đạt được 1.4× thông lượng sự cải thiện với 99.2 phần trăm độ chính xác sự giữ lại so với cố định cao độ phân- giải. Này mẫu đánh đổi sự tiền xử lý chi phí từ việc chạy nhẹ bộ phân loại cho sự suy luận các khoản tiết kiệm trên chính (main) mô hình. Độ trễ sự phân tích cho đến nay (đã) tập trung trên tuần tự việc xử lý: một yêu cầu việc hoàn thành trước khi tiếp theo bắt đầu. Sự tiền xử lý, sự suy luận, và sự hậu xử lý các giai đoạn sử dụng khác biệt phần cứng các tài nguyên. Sự tách biệt này tạo ra một cơ hội để xử lý nhiều các yêu cầu một cách đồng thời (simultaneously).
13.4.4 Phần cứng sự sử dụng và yêu cầu việc tạo đường ống Việc tối ưu hóa mỗi yêu cầu giai đoạn trong sự cô lập bỏ lỡ một chí mạng cơ hội: các giai đoạn sử dụng khác biệt phần cứng các tài nguyên. Độ trễ ngân sách sự phân tích trong phần 13.4.1 tiết lộ rằng mô hình sự suy luận là chỉ một thành phần của yêu cầu vòng đời. Từ một phần cứng góc nhìn, chính mục tiêu của một việc phục vụ hệ thống là để tối đa hóa chu kỳ làm việc (duty cycle) của máy gia tốc, tỷ lệ phần trăm của thời gian (mà) GPU là thực hiện hữu ích sự tính toán. Trong một được tuần tự hóa việc phục vụ hệ thống, phần cứng ngồi rảnh rỗi trong suốt mạng I/O và dựa trên-CPU sự tiền- xử lý. Cao-hiệu suất việc phục vụ các hệ thống sử dụng Yêu cầu Việc tạo đường ống để chồng chéo (overlap) những các giai đoạn này, việc đảm bảo (rằng) GPU được cho ăn (fed) một liên tục luồng của các tensor.
13.4.4.1 Việc chồng chéo I/O và tính toán Hai định thời (timing) các sơ đồ trong hình 13.5 minh họa tác động của việc tạo đường ống. Trong tuần tự (serial) trường hợp (A), mỗi yêu cầu phải hoàn thành toàn bộ vòng đời của nó (Mạng → CPU Sự tiền xử lý → GPU Sự suy luận → Sự hậu xử lý) trước khi tiếp theo yêu cầu bắt đầu, và xám rảnh rỗi các khoảng trống (gaps) để GPU không được sử dụng (unused) cho nhiều hơn 50 phần trăm của thời gian, each request must complete its entire lifecycle (Network →CPU Preprocessing →GPU Inference →Postprocessing) before the next request begins, and the grey idle gaps leave the GPU unused for more than 50 percent of the time). Trong được tạo đường ống (pipelined) trường hợp (B), những các khoảng trống đó biến mất. Việc tạo đường ống được kích hoạt bởi không đồng bộ I/O và tính đồng thời các mô hình mẫu. Thay vì việc chờ đợi cho một GPU hạt nhân kết thúc (finish), máy chủ’s CPU luồng đệ trình công việc tới GPU’s lệnh hàng đợi và ngay lập tức bắt đầu việc tiền xử lý tiếp theo đến (incoming) yêu cầu.

13. Mô hình Việc phục vụ (Model Serving)

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
GPU 4 A. Tuần tự Sự thực thi (Thấp Sự sử dụng)) B. Được tạo đường ống Sự thực thi (Cao Sự sử dụng))
Hình 13.5: Yêu cầu Việc tạo đường ống: Việc tạo đường ống giấu độ trễ bằng cách việc chồng chéo độc lập các hoạt động qua khác biệt phần cứng các tài nguyên. Trong được tạo đường ống sự thực thi (B), CPU xử lý tiếp theo yêu cầu’s dữ liệu trong khi GPU thực thi hiện tại yêu cầu’s sự suy luận, the CPU processes the next request’s data while the GPU executes the current request’s inference). Điều này làm tăng GPU chu kỳ làm việc hướng tới 100 phần trăm, một cách hiệu quả việc nhân đôi hay nhân ba thông lượng trên giống nhau phần cứng mà không có việc thay đổi mô hình.
13.4.4.2 Các hệ thống số liệu: Phần cứng chu kỳ làm việc Trong “Định lượng Cách tiếp cận” tới ML các hệ thống, chúng ta định nghĩa hệ thống tính hiệu quả như là khả năng của một việc phục vụ hệ thống để bão hòa nút thắt cổ chai tài nguyên. Cho hầu hết ML các hệ thống, điều này là GPU’s tính toán các lõi hay bộ nhớ băng thông. Chúng ta định lượng điều này trong phương trình 13.2: Hệ thống Tính hiệu quả = ∑𝑇tính toán / (Bức tường Đồng hồ Thời gian × Tài nguyên Số đếm) (13.2) Nếu một ResNet-50 yêu cầu tốn 10 ms tổng cộng, một tuần tự hệ thống đạt được chỉ 50 phần trăm tính hiệu quả, a serial system achieves only 50 percent efficiency). Bằng cách việc tạo đường ống chỉ hai các yêu cầu, tính hiệu quả tiếp cận 100 phần trăm (việc giả định CPU có thể theo kịp với GPU)). Nếu CPU là quá chậm để cho GPU ăn, hệ thống trở nên giới hạn-CPU, và xa hơn (further) mô hình sự tối ưu hóa cung cấp không (zero) thông lượng lợi ích. Điều này là Amdahl’s Định luật từ phần D.2.3 được áp dụng cho việc phục vụ: nếu sự tiền xử lý tiêu thụ 50 phần trăm của độ trễ, tối đa sự tăng tốc là 2× bất kể (mức độ) nhanh như thế nào mô hình chạy. Phần cứng quỹ đạo (trajectory) làm này trần (ceiling) (trở nên) dần dần chặt chẽ hơn. Máy gia tốc tính toán thông lượng (FLOPs) (đã) phát triển xa nhanh hơn (so với) CPU đơn-luồng (single-thread) hiệu suất qua liên tiếp (successive) phần cứng các thế hệ, do đó sự suy luận phần của đường ống thu hẹp lại trong khi giới hạn-CPU sự tiền xử lý phần duy trì không bị thay đổi has grown far faster than CPU single-thread performance across successive hardware generations, so the inference portion of the pipeline shrinks while the CPU-bound preprocessing portion remains unchanged). Một hệ thống thứ mà đã (là) giới hạn-tính toán trên một cũ hơn máy gia tốc có thể trở nên giới hạn-CPU sau một phần cứng sự nâng cấp—không (phải) bởi vì sự tiền xử lý (trở nên) chậm hơn, nhưng bởi vì mô hình (trở nên) một cách quyết liệt nhanh hơn trong khi CPU (thì) không.
13.4.5 Sự hậu xử lý Yêu cầu vòng đời kết luận (concludes) với sự hậu xử lý, giai đoạn thứ mà biến đổi mô hình các đầu ra thành có thể hành động (actionable) các kết quả. Một nơ-ron mạng tạo ra thô các tensor (dấu phẩy-động các mảng thứ mà mang không vốn có (inherent) ý nghĩa đối với các ứng dụng hay những người dùng)). Một 0.95 xác suất trở thành một tự tin “con chó” (dog) nhãn chỉ sau khi sự hậu xử lý chuyển đổi nó; một chuỗi (sequence) của mã thông báo các ID trở thành có thể đọc văn bản; một hộp giới hạn (bounding box) tensor trở thành một được làm nổi bật vùng trong một hình ảnh. Sự hậu xử lý một cách đáng kể tác động cả hai độ trễ và sự hữu ích (usefulness) của các dự đoán.
13.4.5.1 Từ các logit tới các dự đoán Sự phân loại các mô hình (đưa) đầu ra các logit hay các xác suất qua các lớp. Việc chuyển đổi những thô các đầu ra này thành các dự đoán bao gồm một vài các bước. (Cái) đơn giản nhất là argmax sự lựa chọn (selection), thứ mà trả về cao nhất- xác suất lớp. Việc tạo ngưỡng (Thresholding) áp dụng một sự tự tin sự cắt đứt (cutoff), việc trả về các dự đoán chỉ khi mô hình là đủ chắc chắn. Top-𝑘 sự trích xuất trả về nhiều cao-xác suất các lớp với chúng các điểm số, hữu ích khi các ứng dụng cần được xếp hạng (ranked) các lựa chọn thay thế. Sự hiệu chuẩn (Calibration) điều chỉnh thô các xác suất để phản ánh tốt hơn thực sự các khả năng (likelihoods), một bước thứ mà thêm sự tính toán nhưng là thiết yếu khi xuôi dòng (downstream) các hệ thống đưa ra các quyết định dựa trên sự tự tin các điểm số. Cho ResNet-50 hình ảnh sự phân loại, danh sách 13.1 cho thấy đầy đủ sự hậu xử lý con đường từ thô các logit tới một sẵn sàng-API (API-ready) phản hồi, bao gồm xác suất sự chuẩn hóa (normalization), top-𝑘 sự trích xuất, nhãn sự tra cứu, và phản hồi việc định dạng. Cho này ví dụ, tổng cộng sự hậu xử lý thời gian là xấp xỉ 0.1 ms, không đáng kể (negligible) (khi được) so sánh với sự tiền xử lý và sự suy luận. Mỗi bước thêm độ trễ nhưng cải thiện phản hồi tiện ích (utility). Sự hiệu chuẩn

13. Mô hình Việc phục vụ (Model Serving)

13.5 Xếp hàng đợi Lý thuyết (Queuing Theory)

Little’s Định luật: John D. C. Little (đã) chứng minh vào năm 1961 rằng 𝑄yêu cầu (req) = 𝜆đến (arr)𝑇độ trễ (lat) đúng cho bất kỳ
ổn định hệ thống bất kể đến (arrival) sự phân phối, dịch vụ
sự phân phối, hay sự lập lịch
kỷ luật (discipline). Tính phổ- quát (universality) này là tại sao nó neo (anchors) ML
công suất việc lập kế hoạch: công-
thức không yêu cầu các giả định
về (việc) liệu các yêu cầu đến
trong các đợt (bursts), liệu sự suy-
luận các thời gian thay đổi, hay liệu
bộ lập lịch tạo lô quyết-
liệt (hay không). Duy nhất yêu cầu
là sự ổn định (𝜆arr < 𝜇), và khi đó điều kiện phá vỡ,
không lượng của sự tối ưu hóa ngăn cản hàng đợi sự phân kỳ (divergence). nói riêng có thể thêm đáng kể sự tính toán nhưng là cần thiết khi xuôi dòng các hệ thống đưa ra các quyết định dựa trên sự tự tin các điểm số.
13.4.5.2 Đầu ra việc định dạng Sản xuất các hệ thống hiếm khi trả về thô các dự đoán. Các đầu ra phải tuân thủ (conform) tới API các hợp đồng (contracts) thứ mà chỉ định JSON sự tuần tự hóa các lược đồ (schemas), sự tự tin điểm số việc định dạng, và việc tạo ngưỡng các quy tắc. Lỗi việc xử lý (handling) phải giải quyết cạnh (edge) các trường hợp: hệ thống phải định nghĩa hành vi khi không dự đoán vượt quá sự tự tin ngưỡng hay khi đầu vào xuất hiện ngoài-phân phối (out-of-distribution). Phản hồi siêu dữ liệu (mô hình phiên bản, sự suy luận thời gian, tính năng các sự quy kết (attributions)) kích hoạt xuôi dòng sự giám sát và việc gỡ lỗi enables downstream monitoring and debugging). Danh sách 13.1: ResNet-50 Sự hậu xử lý: Biến đổi thô các logit thành được hiệu chuẩn các xác suất, trích xuất top-𝑘 các dự đoán, và định dạng API phản hồi.
# Biến đổi thô các logit thành được hiệu chuẩn các xác suất
# Đầu vào: các logit tensor của hình dạng (lô_kích thước (batch_size), 1000) - một điểm số mỗi
# ImageNet lớp
các xác suất (probs) = torch.softmax(
các logit, chiều (dim)=-1
)
# Chuẩn hóa để tổng=1; ~0.05 ms trên GPU
# Trích xuất top-5 các dự đoán cho nhiều-lớp (multi-class) phản hồi
# topk trả về (các giá trị, các chỉ số) được sắp xếp bởi xác suất top5_probs, top5_indices = probs.topk(5)
# ~0.02 ms; GPU hoạt động top5_probs = top5_probs.squeeze(0).tolist() top5_indices = top5_indices.squeeze(0).tolist()
# Ánh xạ lớp các chỉ số (indices) sang có thể đọc-bởi con người các nhãn
# imagenet_labels: danh sách của 1000 lớp các tên từ synset ánh xạ
các nhãn (labels) = [ imagenet_labels[i] cho (for) i trong top5_indices
]
# ~0.01 ms; CPU sự tra cứu
# Định dạng phản hồi với các dự đoán và siêu dữ liệu cho API hợp đồng
phản hồi = {
"các dự đoán": [ {"nhãn": nhãn, "sự tự tin": float(xác suất)} cho nhãn, xác suất trong zip(các nhãn, top5_probs) ], "mô hình_phiên bản": "resnet50-v2.1",
# Phía máy khách (Client-side) phiên bản việc theo dõi "sự suy luận_thời gian_ms": 5.2,
# Khả năng quan sát (Observability) cho độ trễ sự giám sát
} Độ trễ ngân sách sự phân tích tiết lộ nơi thời gian đi (đến) bên trong một đơn yêu cầu. Sản xuất các hệ thống, tuy nhiên, không xử lý các yêu cầu trong sự cô lập: chúng phải xử lý hàng trăm hay hàng ngàn của đồng- thời các yêu cầu cạnh tranh cho hữu hạn các tài nguyên. Việc hiểu này tính đồng thời yêu cầu một khác biệt thuộc về phân tích (analytical) bộ khung.
13.5 Việc xếp hàng đợi Lý thuyết (Queuing Theory) Trong sản xuất, đồng thời các yêu cầu cạnh tranh cho hữu hạn các tài nguyên, và việc xếp hàng đợi lý thuyết dự đoán cách sự cạnh tranh này ảnh hưởng độ trễ. Những các nguyên tắc này giải thích phản trực giác (counterintuitive) hành vi gây ra được cung cấp-tốt (well-provisioned) các hệ thống vi phạm độ trễ các SLO khi tải tăng một cách khiêm tốn (modestly).
13.5.1 Little’s Định luật Việc phục vụ các kỹ sư một cách thường xuyên (routinely) đối mặt (với) một cụ thể công suất quyết định: cho một độ trễ SLO và một được mong đợi yêu cầu tỷ lệ, hệ thống phải xác định bao nhiêu đang bay (in-flight) công việc nó phải giữ trước khi việc quyết định bao nhiêu các GPU để cung cấp. Little’s Định luật (phần D.2.4) trả lời (câu) đầu tiên câu hỏi bằng cách việc liên hệ (relating) hàng đợi độ sâu (depth) tới thông lượng (Little’s Law (section D.2.4) answers the first question by relating queue depth to throughput). M/M/1 mô hình sau đó trả lời (câu) thứ hai bằng cách việc dự đoán cách độ trễ suy giảm (degrades) dưới tải. Cùng nhau, chúng cung cấp định lượng bộ khung cho công suất việc lập kế hoạch.

13. Mô hình Việc phục vụ

Việc phục vụ các kỹ sư cần một công cụ kết nối có thể quan sát (observable) các số liệu với công suất các yêu cầu. (Cái) được tán dương nhất kết quả trong việc xếp hàng đợi lý thuyết là Little’s Định luật,9 thứ mà phương trình 13.3 thể hiện như một đơn giản mối quan hệ giữa ba các đại lượng (quantities) trong bất kỳ ổn định hệ thống (The most celebrated result in queuing theory is Little’s Law,9 which equation 13.3 expresses as a simple relationship between three quantities in any stable system):
𝑄req = 𝜆arr ⋅𝑇lat (13.3) nơi 𝑄req là trung bình số lượng của các yêu cầu trong hệ thống, 𝜆arr là đến (arrival) tỷ lệ (các yêu cầu mỗi giây), và 𝑇lat là trung bình thời gian mỗi yêu cầu dành trong hệ thống (where 𝑄req is the average number of requests in the system, 𝜆arr is the arrival rate (requests per second), and 𝑇lat is the average time each request spends in the system). Một cách cụ thể, một máy chủ việc nhắm mục tiêu 1000 QPS với một 50 ms SLO có thể dịch (chuyển) đó cặp một cách trực tiếp thành số lượng của đồng thời yêu cầu các khe (slots) nó phải giữ trong bộ nhớ, cứng sàn (floor) cho sự kích hoạt lưu trữ trên đó nút; được làm việc ví dụ bên dưới thực hiện đó sự tính toán. Các hệ thống Góc nhìn 13.4: Ký hiệu cảnh báo: L so với độ trễ Trong việc xếp hàng đợi lý thuyết, 𝑇lat biểu thị phản hồi thời gian hay thời gian trong hệ thống mỗi yêu cầu; chỉ-hàng đợi (queue-only) việc chờ đợi thời gian là 𝑊𝑞. Cuốn sách này sử dụng 𝑄req cho trung bình trong-hệ thống (in-system) yêu cầu số đếm, 𝜆arr cho đến tỷ lệ, và 𝜌serv = 𝜆arr/𝜇 cho việc phục vụ sự sử dụng. Các chỉ số dưới (subscripts) phân biệt việc xếp hàng đợi ký hiệu từ sự suy giảm (degradation) phương trình’s 𝜆độ nhạy (sensitivity) tham số và giữ việc phục vụ sự sử dụng khỏi việc chiếm đóng (occupying) trần (bare) 𝜌. Trong độ trễ-ngân sách các phương trình bên dưới, mang tính mô tả 𝐿lat,* các thuật ngữ gọi tên các thành phần của ngân sách, như việc chờ đợi và tính toán. Trong việc tạo lô sự phân tích tiếp theo (phần 13.7.3), 𝐿lat,wait tương ứng với việc xếp hàng đợi chờ đợi thành phần 𝑊𝑞, và 𝐿lat,compute bao gồm sự suy luận thời gian, 𝐿lat,wait corresponds to the queueing wait component 𝑊𝑞, and 𝐿lat,compute includes inference time). Mối quan hệ này (giữ) đúng bất kể đến sự phân phối, dịch vụ thời gian sự phân phối, hay sự lập lịch chính sách. Một thực tế công suất sự tính toán cho thấy tại sao tính phổ quát này quan trọng cho việc phục vụ bộ nhớ. Khăn ăn Toán học 13.4: Little’s Định luật công suất việc xác định kích thước (Little’s Law capacity sizing) Vấn đề: Bao nhiêu đồng thời yêu cầu công suất (mà) một hệ thống cần để phục vụ 1,000 QPS? Toán học: Little’s Định luật cho 𝑄req = 𝜆arr𝑇lat, do đó tính đồng thời bằng (equals) thông lượng được nhân với độ trễ (phần D.2.4 dẫn xuất định luật) (Math: Little’s Law gives 𝑄req = 𝜆arr𝑇lat, so concurrency equals throughput multiplied by latency (section D.2.4 derives the law)).
Được cho: • Thông lượng mục tiêu (𝜆arr): 1,000 QPS. • Độ trễ mục tiêu (𝑇lat): 50 ms (0.05 s).
Toán học: 𝑄req = 1,000 QPS × 0.05 s = 50 đồng thời các yêu cầu Các hệ thống sự thấu hiểu: Máy chủ phải có đủ RAM để giữ 50 các yêu cầu một cách đồng thời qua lô và hàng đợi trạng thái. Nếu GPU hết bộ nhớ tại lô kích thước 32, hệ thống (về mặt) vật lý không thể đạt (hit) 1,000 QPS tại 50 ms độ trễ; duy nhất các tùy chọn là để giảm độ trễ (𝑇lat) hay thêm đủ bộ nhớ cho một lớn hơn thường trú (resident) 𝑄req (If the GPU runs out of memory at batch size 32, the system physically cannot hit 1,000 QPS at 50 ms latency; the only options are to reduce latency (𝑇lat) or add enough memory for a larger resident 𝑄req). Little’s Định luật có ngay lập tức thực tế các hàm ý (implications). Nếu một sự suy luận dịch vụ trung bình 10 ms mỗi yêu cầu (𝑇lat = 0.01 s) và hệ thống cho thấy 50 đồng thời các yêu cầu trên (mức) trung bình (𝑄req = 50), thì đến tỷ lệ phải là 𝜆arr = 𝑄req/𝑇lat = 5000 các yêu cầu mỗi giây (If an inference service averages 10 ms per request (𝑇lat = 0.01 s) and the system shows 50 concurrent requests on average (𝑄req = 50), then the arrival rate must be 𝜆arr = 𝑄req/𝑇lat = 5000 requests per second). Ngược lại (Conversely), nếu hệ thống phải giới hạn đồng thời các yêu cầu (xuống) 10 (có lẽ do GPU bộ nhớ các sự ép buộc) và dịch vụ thời gian là 10 ms, nó có thể duy trì (sustain) (nhiều) nhất 1000 các yêu cầu mỗi giây and the service time is 10 ms, it can sustain at most 1000 requests per second).
13.5.2 Việc tạo lô thuế: Độ trễ-thông lượng biên giới Trong khi Little’s Định luật liên hệ hàng đợi độ sâu tới thông lượng, nó không tính toán (account) cho Việc tạo lô Thuế (Batching Tax): được cố ý (deliberate) sự chậm trễ được giới thiệu để tối đa hóa phần cứng sự sử dụng. Trong truyền thống của định lượng các hệ thống, chúng ta phân tích điều này như một việc xếp hàng đợi sự chậm trễ vấn đề. Khi một sự suy luận máy chủ tạo lô các yêu cầu, nó giới thiệu hai khác biệt các nguồn của độ trễ. Lô sự hình thành (formation) sự chậm trễ (𝐿lat,form) là thời gian đầu tiên yêu cầu trong một lô đợi cho cuối cùng yêu cầu (để) đến (Batch formation delay (𝐿lat,form) is the time the first request in a batch waits for the last request to arrive).

13.5 Việc xếp hàng đợi Lý thuyết (Queuing Theory)

M/M/1 Hàng đợi: Việc xếp-
hàng đợi lý thuyết (đã) bắt nguồn với
Agner Krarup Erlang’s 1909
sự phân tích của Copenhagen
Điện thoại Tổng đài, nơi cuộc gọi các sự đến thực sự là (genuinely were) không nhớ (memoryless).
M/M/1 mô hình’s hàm mũ (exponential)
dịch vụ thời gian giả định khớp (fit) điện thoại tốt nhưng dự đoán-quá (overpre-
dicts) dịch vụ-thời gian phương sai cho
nhiều cố định-hình dạng ML sự suy- luận các khối lượng công việc. Sự không khớp
này là hữu ích cho trực giác: M/M/1 đánh giá quá cao (overestimates) đợi các thời gian bởi xấp xỉ 2× (khi được) so-
sánh với một mang tính xác định- dịch vụ (deterministic-service) mô hình như là M/D/1,
do đó công suất việc lập kế hoạch dựa
trên nó có xu hướng bảo tồn nhiều hơn khoảng không (headroom).

Siêu-Tuyến tính (Super-Linear) Độ trễ
Sự phân kỳ: Việc lập kế hoạch đầu gối (knee) thường xuất hiện tốt (ngay) trước- khi (well before) đầy đủ sự bão hòa. Trong
M/M/1 trung bình phản hồi-thời gian phương trình, 𝐸[𝑇] = (1/𝜇)/(1−𝜌serv),
nơi 𝜌serv = 𝜆arr/𝜇 là sự sử-
dụng (utilization). (1 −𝜌serv)−1
thuật ngữ phân kỳ khi 𝜌serv → 1: tại
𝜌serv = 0.7, trung bình phản hồi
thời gian đã là 3.3× (của cái) cơ sở
dịch vụ thời gian; tại 𝜌serv = 0.9, nó
là 10×. Chính xác hoạt động giới hạn là một chính sách và khối lượng công việc sự lựa chọn, nhưng việc cố gắng kéo giãn (stretch)
một nhạy cảm-độ trễ hàng đợi hướng
tới sự bão hòa tạo ra không tương- xứng độ trễ sự phát triển.

Kendall Ký hiệu: Trong
A/S/c (Đến/Dịch- vụ/các máy chủ) hệ thống,
“M”
biểu thị
một
Markovian (không nhớ)
quá trình
và
“D”
có nghĩa là mang tính xác định.
Văn bản
chọn
M/M/1
thay vì thực tế hơn
M/D/1 bởi vì M/M/1’s bảo thủ thành kiến (bias) là một tính năng
cho công suất việc lập kế hoạch:
nó
đánh giá quá cao đợi các thời gian bởi
xấp xỉ 2× khi dịch vụ các thời gian là gần như mang tính xác định,
việc bảo tồn lề (margin) chống lại
phương sai những sự ngạc nhiên. Chi phí của khiêm tốn việc cung cấp-quá (over-provisioning)
thường xa thấp hơn (so với) chi phí
của một SLA sự bỏ lỡ tại p99 đuôi
khi dịch vụ thời gian phương sai tăng vọt (spikes) một cách không mong đợi. Sự suy luận sự lạm phát (inflation) là sự phát triển trong sự suy luận thời gian 𝑇inf(𝐵) khi GPU xử lý 𝐵 các mẫu thay vì 1 (Inference inflation is the growth in inference time 𝑇inf(𝐵) when the GPU processes 𝐵 samples instead of 1). (Cái) dẫn đến độ trễ-thông lượng Pareto biên giới là tập hợp của các cấu hình nơi một (người) không thể cải thiện thông lượng mà không có việc trả một “thuế” trong được làm tăng độ trễ. Chúng ta có thể định lượng tổng được tạo lô-yêu cầu độ trễ cho một lô kích thước 𝐵 và đến tỷ lệ 𝜆arr như phương trình 13.4 (We can quantify the total batched-request latency for a batch size 𝐵 and arrival rate 𝜆arr as equation 13.4): 𝐿lat,tổng ≈ (𝐵−1)/(2𝜆arr) (Sự hình thành sự chậm trễ) + 𝑇inf(𝐵) (Sự suy luận thời gian) (13.4) Phương trình này tiết lộ “chi phí của thông lượng”. Việc tăng 𝐵 để bão hòa GPU khấu hao phần cứng chi phí, nhưng làm lạm phát mỗi-yêu cầu độ trễ. Một cách cụ thể, tại 500 QPS, việc di chuyển từ lô-1 tới lô-32 tăng đợi-thời gian từ 0 ms tới 31 ms, việc đóng góp vào một 23× tổng độ trễ hình phạt (penalty) (2 ms → 46 ms) (Concretely, at 500 QPS, moving from batch-1 to batch-32 increases wait-time from 0 ms to 31 ms, contributing to a 23× total latency penalty (2 ms → 46 ms)). Cho một các hệ thống kỹ sư, này thuế là chính bộ điều chỉnh của thuộc về kinh tế tính hiệu quả: kỹ sư chọn lô kích thước thứ mà tối đa hóa thông lượng (việc giảm thiểu chi phí mỗi truy vấn) mà không có việc vi phạm độ trễ SLO (𝐿lat) without violating the latency SLO (𝐿lat)).
13.5.3 Sự sử dụng-độ trễ mối quan hệ Little’s Định luật mô tả trung bình hệ thống hành vi, nhưng nó không tiết lộ cách độ trễ thay đổi khi tải tiếp cận công suất. Để trả lời (câu) chí mạng câu hỏi của bao nhiêu dự phòng (spare) công suất một việc phục vụ hệ thống cần, chúng ta chuyển tới M/M/1 hàng đợi mô hình).10 Cho một hệ thống với Poisson các sự đến (arrivals) và hàm mũ dịch vụ các thời gian, phương trình 13.5 cung cấp trung bình thời gian trong hệ thống: 𝑇lat = 1/(𝜇−𝜆arr) = dịch vụ thời gian/(1−𝜌serv) (13.5) nơi 𝜆arr là đến tỷ lệ, 𝜇 là dịch vụ tỷ lệ (các yêu cầu mỗi giây máy chủ có thể xử lý), và 𝜌serv = 𝜆arr/𝜇 là sự sử dụng (phần (fraction) của thời gian máy chủ là bận rộn) (where 𝜆arr is the arrival rate, 𝜇 is the service rate (requests per second the server can handle), and 𝜌serv = 𝜆arr/𝜇 is the utilization). Phương trình này tiết lộ tại sao việc phục vụ các hệ thống thể hiện phi tuyến tính hành vi: nhỏ các sự gia tăng trong tải gần công suất gây ra không tương xứng độ trễ các sự gia tăng11. Bảng 13.7 định lượng này mối quan hệ, việc cho thấy cách trung bình thời gian trong hệ thống phát triển một cách nhanh chóng khi sự sử dụng tiếp cận 100 phần trăm.
Bảng 13.7: Sự sử dụng-Độ trễ Mối quan hệ: Trung bình thời gian trong hệ thống (đợi + dịch vụ) như một bội số của dịch vụ thời gian cho một M/M/1 hàng đợi as a multiple of service time for an M/M/1 queue). Tại 50 phần trăm sự sử dụng, thời gian trong hệ thống là 2× dịch vụ thời gian; tại 90 phần trăm, nó đạt (tới) 10×. Này phi tuyến tính sự phát triển giải thích tại sao các hệ thống thứ mà thực hiện tốt tại vừa phải tải đột ngột vi phạm các SLO khi lưu lượng truy cập tăng: việc di chuyển từ 80 phần trăm tới 90 phần trăm sự sử dụng nhân đôi độ trễ.
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
100 ms M/M/1 mô hình giả định một cách theo hàm mũ được phân phối dịch vụ các thời gian, nhưng ML sự suy luận điển hình có gần-như-không-đổi (near-constant) dịch vụ thời gian cho cố định lô các kích thước, việc làm M/D/1 (mang tính xác định dịch vụ) mô hình (trở nên) chính xác hơn trong thực tế model more accurate in practice). Chúng ta sử dụng M/M/1 ở đây bởi vì nó mang lại dạng-đóng (closed-form) các giải pháp và tạo ra bảo thủ các ước tính. Cho M/D/1 các hàng đợi, trung bình đợi thời gian là xấp xỉ (một) nửa của M/M/1 tại giống nhau sự sử dụng, thứ mà quan trọng cho công suất việc lập kế hoạch: M/M/1 sự phân tích (sẽ) một cách nhẹ nhàng cung cấp-quá, việc phạm lỗi (erring) trên (về) phía của việc đáp ứng các SLO thay vì việc vi phạm chúng.12
13.5.4 Nhiều-máy chủ các sự cân nhắc (Cái) đi trước (preceding) sự phân tích tập trung trên một đơn việc phục vụ nút (một máy móc phục vụ sự suy luận các yêu cầu)). Phạm vi này (scope) căn chỉnh với cuốn sách này’s sự tập trung trên việc làm chủ (mastering) cơ bản đơn vị của ML các hệ thống. Đơn-nút việc xếp hàng đợi động lực học (dynamics) là điều kiện tiên quyết (prerequisite) tới hiệu quả sự mở rộng. Các kỹ sư không thể tối ưu hóa một được phân tán hệ thống mà không có trước tiên việc hiểu hành vi của các thành phần của nó. M/M/1 sự phân tích duy trì (là) nền tảng cho việc xác định kích thước đúng (right-sizing) cá nhân các nút, việc xác định sự mở rộng trình kích hoạt (trigger), và việc tránh non (premature) sự mở rộng-ra (scale-out). Đầu tiên, nó xác định liệu một GPU thể đáp ứng độ trễ (hay không)

13. Mô hình Việc phục vụ (Model Serving)

SLO tại được mong đợi lưu lượng truy cập. Sau đó nó cho thấy khi đến tỷ lệ vượt quá đơn-nút công suất. Cuối cùng, nó ngăn cản các nhóm (teams) khỏi việc thêm các bản sao (replicas) trước khi nút thắt cổ chai là thực sự nút công suất thay vì việc tạo lô chính sách, sự tiền xử lý, lạnh khởi động (cold start), hay thời gian chạy cấu hình. Một khi lưu lượng truy cập thực sự vượt quá đơn-nút công suất, tiếp theo động thái (move) là cấp độ-bản sao (replica-level) sự mở rộng-ra: nhiều độc lập việc phục vụ các nút ngồi đằng sau một tải bộ cân bằng (load balancer) và mỗi chạy giống nhau mô hình. M/M/c việc xếp hàng đợi mô hình mở rộng M/M/1 tới 𝑐 song song các máy chủ, việc cho thấy cách các bản sao có thể cải thiện độ trễ khi lưu lượng truy cập được cân bằng qua độc lập các máy chủ. Chính xác p99 sự cải thiện phụ thuộc vào đến quá trình, dịch vụ-thời gian phương sai, sự phân phối chính sách, và mỗi-bản sao sự sử dụng. Đó bản sao mô hình là vẫn khác từ được phân tán sự suy luận, nơi một yêu cầu được chia (split) qua các GPU thông qua mô hình sự phân mảnh (sharding), tensor tính song song, hay đường ống tính song song. Chương này thiết lập đơn-nút và bản sao nền tảng; được phân tán sự suy luận thêm sự điều phối (coordination) chi phí hoạt động và tính nhất quán các thách thức vượt ra ngoài phạm vi này.
13.5.5 Đuôi độ trễ (Tail latency) Sản xuất các SLO điển hình chỉ định phân vị các mục tiêu (p95, p99) thay vì các mức trung bình bởi vì đuôi độ trễ xác định người dùng trải nghiệm cho chậm nhất các yêu cầu (Dean và Barroso 2013) rather than averages because tail latency determines user experience for the slowest requests). Cho một M/M/1 hàng đợi, p99 độ trễ tuân theo (follows): 𝑇lat,p99 ≈ dịch vụ thời gian / (1−𝜌serv) ⋅ ln(1 / (1−0.99)) ≈ 4.6 ⋅ dịch vụ thời gian / (1−𝜌serv) (13.6) Tại 70 phần trăm sự sử dụng, M/M/1 p99 sự xấp xỉ (approximation) là xấp xỉ 15 lần dịch vụ thời gian (4.6/0.3 ≈ 15.3), trong khi trung bình độ trễ là chỉ 3.3 lần (At 70 percent utilization, the M/M/1 p99 approximation is approximately 15 times the service time (4.6/0.3 ≈ 15.3), while average latency is only 3.3 times). Cho mang tính xác định-dịch vụ các mô hình như là M/D/1, đuôi các giá trị yêu cầu cụ thể-mô hình sự tính toán thay vì một đơn giản phổ quát hệ số nhân (multiplier). Quan trọng điểm là không bị thay đổi: các hệ thống dường như khỏe mạnh với thấp trung bình độ trễ có thể có không thể chấp nhận (unacceptable) đuôi độ trễ, bởi vì mức trung bình giấu trải nghiệm của rủi ro nhất (unluckiest) các yêu cầu.
13.5.5.1 Đuôi tại quy mô vấn đề Dean và Barroso’s sự phân tích tiết lộ tại sao đuôi độ trễ trở nên chí mạng khi các hệ thống mở rộng vượt ra ngoài đơn các máy móc (Dean và Barroso 2013) (Dean and Barroso’s analysis reveals why tail latency becomes critical as systems scale beyond single machines (Dean and Barroso 2013)). Khi các yêu cầu phân nhánh ra (fan out) tới nhiều các máy chủ, xác suất của việc trải nghiệm ít nhất một chậm phản hồi phát triển một cách nhanh chóng với máy chủ số đếm. Này “đuôi tại quy mô” hiệu ứng làm cá nhân máy chủ đuôi độ trễ (trở nên) chí mạng cho tổng thể hệ thống hiệu suất. Cho đơn-máy móc việc phục vụ, nguyên tắc này có hai các hàm ý (implications). Đầu tiên, đuôi độ trễ trên cá nhân các máy móc quan trọng bởi vì nó sẽ cộng gộp khi các hệ thống cuối cùng mở rộng. Thứ hai, khoan dung-đuôi (tail-tolerant) các kỹ thuật được mô tả sau (việc rào chắn (hedging), tinh tế sự suy giảm) cung cấp giá trị thậm chí trên đơn các máy móc và trở nên không thể thiếu (indispensable) tại quy mô provide value even on single machines and become indispensable at scale). Khoan dung-đuôi các kỹ thuật như là yêu cầu việc rào chắn (hedging) gửi dư thừa (redundant) các yêu cầu sau một thời gian chờ (timeout), việc chấp nhận bất cứ phản hồi đến trước. Sao lưu các yêu cầu và tải việc cân bằng ra xa khỏi chậm các máy chủ một cách trực tiếp giải quyết độ trễ phương sai. Những các kỹ thuật này áp dụng một cách sạch sẽ tới nhiều mô hình các bản sao, và một số đơn-nút các hệ thống có thể xấp xỉ chúng với đồng thời các luồng hay các phiên bản khi sự hủy bỏ và tài nguyên sự cô lập ngữ nghĩa cho phép nó. Chúng trở nên thiết yếu khi việc mở rộng tới được phân tán sự suy luận các hệ thống. Việc xếp hàng đợi mô hình và đuôi độ trễ sự phân tích cung cấp các đầu vào cho công suất việc lập kế hoạch. Một cụ thể sự triển khai làm các sự đánh đổi (trở nên) hữu hình (tangible). Việc áp dụng Little’s Định luật tới ResNet-50 làm công suất sự ép buộc (trở nên) cụ thể. Khăn ăn Toán học 13.5: ResNet-50 công suất việc lập kế hoạch Hãy xem xét việc thiết kế một ResNet-50 việc phục vụ hệ thống với những các yêu cầu này:
• Mục tiêu p99 độ trễ: 50 ms • Đỉnh (Peak) được mong đợi lưu lượng truy cập: 5,000 QPS • Dịch vụ thời gian (TensorRT FP16): 5 ms Bước 1: Tìm an toàn sự sử dụng. Từ phương trình 13.6, 𝑇lat,p99 ≈ 4.6 × dịch vụ thời gian / (1 − 𝜌serv). Việc thiết lập 𝑇lat,p99 ≤ 50 ms với 5 ms dịch vụ thời gian cho 𝜌serv ≤ 1 − (4.6 × 5𝑚𝑠)/50𝑚𝑠 = 0.54

13.5 Việc xếp hàng đợi Lý thuyết (Queuing Theory)

Việc rào chắn (Hedging): Thuật ngữ được mượn từ tài chính, nơi một bù đắp (offsetting) vụ cá cược (bet) giảm thiểu
rủi ro; ở đây, dư thừa
yêu cầu là một vụ cá cược chống lại một chậm máy chủ. Điều này không (phải) miễn phí: cho ML các hệ thống, việc thua lỗ (losing) được rào chắn (hedged) yêu cầu có thể vẫn chiếm đóng (occupy) máy gia tốc thời gian nếu sự suy-
luận đã khởi chạy, bởi-
vì thông thường GPU các hạt nhân không một cách rẻ mạt (cheaply) bị hủy bỏ giữa- chừng-sự thực thi (mid-execution). Do đó, một việc rào chắn chính sách phải lập ngân sách (budget) trùng lặp
công việc cũng như độ trễ lợi ích (benefit).

Chim hoàng yến (Canary): Được đặt tên cho mỏ than (coal mine) thực tiễn (những năm đầu 1900–1980s) của việc sử dụng các loài chim những (con) cao trao đổi chất (metabolic) tỷ lệ
làm chúng nhạy cảm với độc
các khí trước khi các nồng độ trở nên gây tử vong cho con người. Trong ML việc phục vụ, chim hoàng yến các yêu cầu
phục vụ giống nhau cảnh báo-sớm chức năng cho phân nhánh ra (fan-out) các truy vấn: bằng cách việc kiểm tra 1–2 các phụ trợ (backends) trước- khi (before) cam kết (tới) đầy đủ phân nhánh-
ra, hệ thống phát hiện chậm hay
thất bại các bản sao trước khi một đơn kẻ đi tụt lại (straggler) làm đình trệ toàn bộ được phân-
tán sự suy luận yêu cầu—một
chí mạng sự bảo vệ khi phân nhánh-
ra chiều rộng có nghĩa (là) đuôi độ trễ
phát triển với cực đại của tất cả phụ trợ phản hồi các thời gian. (54 phần trăm tối đa sự sử dụng)). Điều này sử dụng bảo thủ M/M/1 p99 ranh giới (bound) từ được hiển thị phương trình thay vì việc áp dụng một trung bình-chờ đợi M/D/1 sự điều chỉnh tới một đuôi-độ trễ SLO. Bước 2: Tính toán được yêu cầu dịch vụ tỷ lệ. 𝜇yêu cầu (required) = 5,000𝑄𝑃𝑆/0.54 = 9259.3 𝑦ê𝑢_𝑐ầ𝑢/𝑠 Bước 3: Xác định GPU số đếm. Đơn V100 thông lượng tại 𝐵 = 16: 1,143 ℎì𝑛ℎ_ả𝑛ℎ/𝑠 (img/s) Các GPU được cần = 9259.3 𝑦ê𝑢_𝑐ầ𝑢/𝑠 / 1,143 ℎì𝑛ℎ_ả𝑛ℎ/𝑠 = 8.1 → 9 các GPU Bước 4: Thêm khoảng không cho phương sai. Sản xuất các hệ thống thêm 30 phần trăm khoảng không cho lưu lượng truy cập các sự tăng vọt (spikes) và phương sai: cuối cùng số đếm = 9 × 1.3 = 11.7, được làm tròn lên (tới) 12. Bước 5: Xác minh lỗi sự khoan dung. 30 phần trăm khoảng không giải quyết lưu lượng truy cập phương sai, nhưng sản- xuất các hệ thống cũng cần lỗi sự khoan dung. Với 12 các GPU, việc mất (đi) một để lại 11 các GPU xử lý 5,000 QPS. Sau sự thất bại (postfailure) sự sử dụng là (5,000 QPS / 1,143 ℎì𝑛ℎ_ả𝑛ℎ/𝑠) / 11 = 39.8%. Điều này duy trì tốt (nhiều) dưới 54 phần trăm an toàn sự sử dụng ngưỡng, việc xác nhận N+1 sự dư thừa được thỏa mãn. Cho nghiêm ngặt hơn lỗi sự khoan dung các yêu cầu, N+2 sự dư thừa (việc khoan dung hai đồng thời các sự thất bại) sẽ yêu cầu 11 các GPU dưới giống nhau an toàn-sự sử dụng ngưỡng, hay khoảng 14 các GPU nếu 30 phần trăm khoảng không phải duy trì sau hai đồng thời các sự thất bại would require 11 GPUs under the same safe-utilization threshold, or about 14 GPUs if the 30 percent headroom must remain after two simultaneous failures). Kết quả: Cung cấp 12 V100 các GPU để phục vụ 5,000 QPS tại 50 ms p99 độ trễ với N+1 lỗi sự khoan dung. Việc xếp hàng đợi sự phân tích giải thích công suất việc lập kế hoạch cách tiếp cận được chi tiết trong phần 13.11.3 và kết nối một cách trực tiếp tới MLPerf Máy chủ kịch bản. Phần 12.8.4.2 giải thích cách MLPerf đo lường thông lượng chỉ cho các yêu cầu đáp ứng độ trễ SLO: một hệ thống đạt được 10,000 QPS nhưng vi phạm SLO trên 5 phần trăm của các yêu cầu báo cáo chỉ 9,500 hợp lệ QPS.
13.5.6 Khoan dung-đuôi các kỹ thuật Việc loại bỏ tất cả các nguồn của độ trễ tính biến đổi (variability) là thường không thực tế (impractical). Sản xuất các hệ thống thay vào đó sử dụng các kỹ thuật thứ mà khoan dung tính biến đổi trong khi vẫn đáp ứng các SLO (Dean và Barroso 2013; Dean 2012)). Hữu ích sự tổ chức là bởi sự thất bại chế độ: một kẻ đi tụt lại (straggler) bản sao gọi cho một cuộc đua, phân nhánh ra gọi cho sớm sự phát hiện, sự quá tải gọi cho sự thu nhận kiểm soát hay tinh tế sự suy giảm, và sự thử lại (retry) sự khuếch đại (amplification) gọi cho được điều phối (coordinated) sự rụng (shedding). Cho một kẻ đi tụt lại bản sao, hệ thống có thể đua (race) chậm con đường. Dưới việc rào chắn, khi một yêu cầu (đã) không hoàn thành bên trong được mong đợi thời gian, hệ thống gửi một dư thừa yêu cầu tới một máy chủ khác.13 Máy khách sử dụng bất cứ phản hồi đến trước và hủy (bỏ) khác. Cho ML việc phục vụ, điều này có nghĩa là việc duy trì nhiều mô hình các bản sao và việc định tuyến chậm các yêu cầu tới thay thế (alternative) các bản sao. Chi phí hoạt động là khiêm tốn: nếu hệ thống rào chắn tại 95(th) phân vị, chỉ 5 phần trăm của các yêu cầu tạo ra các bản sao (duplicates), việc làm tăng tải bởi chỉ 5 phần trăm trong khi một cách quyết liệt (dramatically) việc giảm thiểu đuôi độ trễ. Thông thường được khởi chạy sự suy luận các hạt nhân không một cách rẻ mạt bị ngắt quãng giữa chừng-sự thực thi. Khi một được rào chắn yêu cầu hoàn thành, bản sao phải bị hủy (bỏ), nhưng nếu sự suy luận đã bắt đầu trên GPU, sự hủy bỏ các cách tiếp cận bao gồm việc kiểm tra một sự hủy bỏ cờ trước khi khởi chạy sự suy luận, việc chấp nhận bị lãng phí tính toán cho đang bay hạt nhân, hay việc sử dụng yêu cầu sự ưu tiên hóa (prioritization) để hạ ưu tiên (deprioritize) bản sao. Vì (Since) việc rào chắn điển hình áp dụng chỉ tới một nhỏ đuôi của các yêu cầu, chi phí hoạt động từ thỉnh thoảng (occasional) bị lãng phí tính toán có thể duy trì (có thể) chấp nhận được khi chính sách được điều chỉnh một cách cẩn thận. Bị trói (Tied) các yêu cầu làm giống nhau cuộc đua (trở nên) quyết liệt hơn bằng cách việc gửi yêu cầu tới nhiều các máy chủ một cách đồng thời, nhưng bao gồm một thẻ (tag) việc cho phép các máy chủ hủy (bỏ) sự thực thi một khi một máy chủ khác bắt đầu việc xử lý. Điều này loại bỏ sự chậm trễ của việc chờ đợi để phát hiện một chậm phản hồi trước khi việc rào chắn. Cho sự suy luận các máy chủ với đáng kể khởi nghiệp chi phí hoạt động từ mô hình việc tải và bộ nhớ sự cấp phát, bị trói các yêu cầu đảm bảo ít nhất một máy chủ bắt đầu ngay lập tức. Phân nhánh ra các hệ thống cần một khác biệt sự can thiệp (intervention) điểm bởi vì một chậm phụ trợ có thể làm đình trệ toàn bộ được phân tán yêu cầu. Chim hoàng yến các yêu cầu trước tiên gửi yêu cầu tới một nhỏ tập hợp con (subset) của một tới hai các máy chủ.14 Nếu những (máy chủ) này trả về bên trong được mong đợi thời gian, hệ thống gửi tới phần còn lại (remainder). Nếu chim hoàng yến là chậm, hệ thống có thể thử lại ở nơi khác hay sử dụng được lưu trong bộ nhớ đệm (cached) các kết quả trước khi cam kết (tới) đầy đủ phân nhánh ra. Kỹ thuật biến (turns) một tiềm năng đuôi-độ trễ sự khuếch đại vấn đề thành một sớm cảnh báo tín hiệu. Khi vấn đề là sự quá tải thay vì một đơn kẻ đi tụt lại, việc đua làm hệ thống tồi tệ hơn bằng cách việc thêm trùng lặp công việc. Hệ thống thay vào đó phải bảo vệ hướng-tới-người dùng khả năng đáp ứng (responsiveness) và

13. Mô hình Việc phục vụ (Model Serving)

được thu nhận-yêu cầu độ trễ. Tinh tế sự suy giảm trả về xấp xỉ các kết quả thay vì (việc) định thời-gian ra (timing out): sự phân loại các hệ thống có thể trả về được lưu trong bộ nhớ đệm các dự đoán cho tương tự các đầu vào, tạo sinh các mô hình có thể trả về ngắn hơn các đầu ra, và các tập hợp (ensembles) có thể trả về các dự đoán từ một tập hợp con của các mô hình. Việc giảm thiểu số lượng của hoạt động tập hợp các thành viên (members) trong suốt sự quá tải một cách trực tiếp làm ngắn (shortens) dịch vụ thời gian (𝑇svc), thứ mà làm tăng máy chủ’s dịch vụ tỷ lệ 𝜇 và mang sự sử dụng 𝜌serv = 𝜆arr/𝜇 trở lại (xuống) dưới việc xếp hàng đợi đầu gối (hình 13.1)—việc đánh đổi một được kiểm soát độ chính xác sự giảm thiểu cho SLO sự sống sót thay vì một không được kiểm soát độ trễ sự sụp đổ (collapse) (Reducing the number of active ensemble members during overload directly shortens service time (𝑇svc), which increases the server’s service rate 𝜇 and brings utilization 𝜌serv = 𝜆arr/𝜇 back below the queueing knee (figure 13.1)—trading a controlled accuracy reduction for SLO survival instead of an uncontrolled latency collapse). Sự thu nhận kiểm soát là nghiêm ngặt hơn. Khi hàng đợi độ sâu vượt quá một ngưỡng, nó chủ động từ chối (rejects) các yêu cầu với ngay lập tức 503 các phản hồi thay vì việc chấp nhận công việc nhiều khả năng (likely) để (sẽ) định thời gian ra. Điều này hy sinh (sacrifices) thông lượng để bảo vệ độ trễ cho được thu nhận các yêu cầu. Một thực tế xuất phát điểm cho việc thiết lập ngưỡng là hai tới ba lần số lượng của những người làm việc (một hàng đợi của hai tới ba dịch vụ các thời gian’ xứng đáng của công việc) (A practical starting point for setting the threshold is two to three times the number of workers (a queue of two to three service times’ worth of work)). Cho một hệ thống với bốn những người làm việc, điều này mang lại một hàng đợi độ sâu ngưỡng của 8 tới 12 các yêu cầu. Thích ứng sự thu nhận kiểm soát điều chỉnh các ngưỡng dựa trên được quan sát p99 độ trễ, việc thắt chặt (tightening) khi độ trễ tăng lên trên mục tiêu và nới lỏng (relaxing) khi độ trễ duy trì khỏe mạnh. M/D/1 đặc tính của ML sự suy luận—rằng được biên dịch (compiled) các mô hình thực thi một cố định lô kích thước có gần-như-không-đổi, mang tính xác định dịch vụ các thời gian—cung cấp (cho) ML sự thu nhận các bộ điều khiển một sự chính xác lợi thế hơn chung web máy chủ sự thu nhận các bộ điều khiển. Trong một chung web dịch vụ, dịch vụ thời gian phụ thuộc vào cơ sở dữ liệu sự nối kết (join) độ phức tạp, bộ nhớ đệm trạng thái, và truy vấn cấu trúc, việc làm nó (trở nên) cao độ ngẫu nhiên (stochastic) và khó để dự đoán. Trong ML sự suy luận, chuyển tiếp vượt qua thời gian cho một cho lô kích thước là thường được giới hạn (bởi) một cách chặt chẽ đủ rằng một sự thu nhận bộ điều khiển có thể ước tính bao nhiêu đồng thời các yêu cầu hệ thống có thể hấp thụ (absorb) trước khi hàng đợi nhiều khả năng để gây ra một SLO sự vi phạm, thay vì việc dựa (dẫm) chỉ vào thô (coarse) bảo thủ các heuristics. Một tinh tế sự thất bại chế độ xảy ra khi tất cả các bản sao bị (làm) quá tải một cách đồng thời. Nếu tải bộ cân- bằng thử lại bị từ chối yêu cầu tại khác bản sao cũng bị quá tải, thử lại lưu lượng truy cập khuếch đại (amplifies) sự quá tải. Được điều phối tải sự rụng giải quyết điều này bằng cách việc chia sẻ tải thông tin qua các bản sao, việc kích hoạt cấp độ-hệ thống các quyết định về (việc) những (nhóm) nào yêu cầu để chấp nhận. Khi toàn cục tải vượt quá công suất, các bản sao tập thể từ chối giống nhau phần của các yêu cầu thay vì mỗi từ chối một cách độc lập và việc kích hoạt (triggering) các sự thử lại. Những các kỹ thuật này trở nên thiết yếu tại quy mô khi phân nhánh ra sự khuếch đại làm cá nhân máy chủ đuôi độ trễ (trở nên) có thể nhìn thấy (với) những người dùng. Đơn-máy móc việc phục vụ các hệ thống có thể triển khai được rào chắn và bị trói các yêu cầu qua GPU các luồng (streams) hay mô hình các bản sao. Việc xếp hàng đợi sự phân tích ở đây giả định vào-trước-ra-trước việc xử lý, nhưng sản xuất các hệ thống thường triển khai sự ưu tiên sự lập lịch như là nhận thức-hạn chót (deadline-aware) hay ngắn nhất-công việc-trước (shortest-job-first) các cách tiếp cận để giảm thiểu xa hơn đuôi độ trễ cho không đồng nhất các khối lượng công việc processing, but production systems often implement priority scheduling such as deadline-aware or shortest-job-first approaches to further reduce tail latency for heterogeneous workloads). Trạm kiểm soát 13.2: Việc xếp hàng đợi và SLO khoảng không Độ trễ các SLO không thi hành bởi “nhanh sự suy luận” một mình (alone); chúng được thi hành bởi khoảng không. □Little’s Định luật: Có thể (bạn) sử dụng 𝑄req = 𝜆arr𝑇lat để giải thích tại sao việc tăng hàng đợi độ sâu ngụ ý (implies) (việc) tăng độ trễ thậm chí nếu mỗi-yêu cầu tính toán thời gian (duy trì) không bị thay đổi (hay không)? (Little’s Law: Can you use 𝑄req = 𝜆arr𝑇lat to explain why rising queue depth implies rising latency even if per-request compute time is unchanged?) □Sự sử dụng vách đá (cliff): Có thể (bạn) giải thích tại sao độ trễ phát triển phi tuyến tính khi sự sử dụng 𝜌serv tiếp cận một, và tại sao sản xuất các hệ thống nhắm mục tiêu một bảo thủ 𝜌serv thay vì “100 phần trăm bận rộn” (hay không)? (Utilization cliff: Can you explain why latency grows nonlinearly as utilization 𝜌serv approaches one, and why production systems target a conservative 𝜌serv rather than “100 percent busy”?) □Đợi so với tính toán: Được cho một đầu cuối-tới-đầu cuối độ trễ ngân sách, có thể (bạn) tách 𝐿lat,compute khỏi 𝐿lat,wait và giải thích nào (một) việc xếp hàng đợi lý thuyết một cách chủ yếu dự đoán (hay không)? (Wait vs. compute: Given an end-to-end latency budget, can you separate 𝐿lat,compute from 𝐿lat,wait and explain which one queuing theory primarily predicts?) □Công suất việc lập kế hoạch: Có thể (bạn) giải thích tại sao một thông lượng con số (number) là chỉ “thực sự” nếu các yêu cầu vẫn đáp ứng phân vị độ trễ SLO dưới tải (hay không)? (Capacity planning: Can you explain why a throughput number is only “real” if requests still meet the percentile latency SLO under load?) □Khoảng không ước tính: Để giữ p99 (ở) dưới 50 ms tại 2,000 các yêu cầu mỗi giây, (hãy) ước tính trung bình đang bay yêu cầu số đếm 𝑄req = 𝜆arr𝑇lat ngụ ý, và cách (mức độ) nhanh đó lề (margin) thu hẹp khi 𝜌serv đi qua (passes) 0.7. Khoan dung-đuôi các kỹ thuật được kiểm tra trong phần này tối ưu hóa luồng (flow) của các yêu cầu thông qua một đang hoạt động (functioning) việc phục vụ hệ thống. Việc xếp hàng đợi sự phân tích, tuy nhiên, giả định hai chí mạng các điều kiện tiên quyết (preconditions): rằng các mô hình được tải và sẵn sàng để xử lý các yêu cầu, và rằng các dự đoán khớp (với) gì đã xác nhận (validated) trong suốt sự phát triển. Trong sản xuất, giả định này thất bại một cách thường xuyên: trong suốt các sự triển khai, mới (mô hình)

13. Mô hình Việc phục vụ (Model Serving)

13.6 Mô hình Vòng đời Sự quản lý các phiên bản (instances) phải tải các mô hình từ đầu (from scratch); trong suốt sự mở rộng các sự kiện, lạnh khởi động độ trễ ảnh hưởng (tới) đầu tiên các yêu cầu (tới) mới các bản sao; và khi sự tiền xử lý các đường ống phân kỳ từ sự đào tạo, độ chính xác im lặng suy giảm (degrades). Tiếp theo phần kiểm tra những vòng đời các thách thức này phải được giải quyết trước khi việc xếp hàng đợi sự tối ưu hóa trở nên có liên quan.
13.6 Mô hình Vòng đời Sự quản lý Việc xếp hàng đợi lý thuyết và khoan dung-đuôi các kỹ thuật tối ưu hóa ổn định-trạng thái (steady-state) luồng của các yêu cầu, nhưng chúng không thể giúp nếu hệ thống không bao giờ đạt tới ổn định trạng thái. Một mới triển khai bản sao thứ mà tốn 35 các giây để biên dịch TensorRT công cụ (engine) của nó vi phạm mọi SLO trong suốt khoảng thời gian đó (đó cửa sổ). Một mô hình mà (dựa) trên-OpenCV (OpenCV-based) việc phục vụ đường ống thay đổi kích thước các hình ảnh một cách khác biệt (so với) (dựa) trên-PIL sự đào tạo đường ống im lặng đánh rơi (drops) 5 tỷ lệ phần trăm các điểm của độ chính xác—một sự suy giảm (vô hình) với độ trễ các bảng điều khiển (dashboards). Những vòng đời các sự thất bại này không (phải là) cạnh các trường hợp; chúng xảy ra tại mọi sự triển khai, mọi sự mở rộng sự kiện, và mọi bộ khung (framework) sự di chuyển (migration). Việc giải quyết chúng yêu cầu kỹ thuật kỷ luật (discipline) trong hai các lĩnh vực (areas): việc làm (cho) các mô hình sẵn sàng để phục vụ (lạnh khởi động và sự khởi tạo (initialization)) và việc giữ các dự đoán (trung thành) với gì đã xác nhận (đào tạo-phục vụ sự lệch (skew)) and keeping predictions faithful to what was validated).
13.6.1 Sự đào tạo-việc phục vụ sự lệch Một mô hình thứ mà thực hiện tốt trong suốt sự xác nhận (validation) có thể một cách im lặng suy giảm khi triển khai. Hiện- tượng này, được biết đến như (là) sự đào tạo-việc phục vụ sự lệch, đại diện một trong tinh tế nhất sự thất bại các chế độ trong sản xuất ML bởi vì nó là vô hình (invisible) đối với độ trễ sự giám sát và ngoại lệ việc theo dõi (Sculley và cộng sự 2015; Baylor và cộng sự 2017)). Định nghĩa 13.3: Sự đào tạo-việc phục vụ sự lệch Sự đào tạo-Việc phục vụ Sự lệch là thuộc về phân phối (distributional) sự phân kỳ giữa sự đào tạo và sự suy luận các môi trường được gây ra bởi không nhất quán (inconsistent) logic hay trạng thái.
1. Tầm quan trọng: Nó vi phạm tính nhất quán mệnh lệnh (imperative), việc gây ra im lặng độ chính xác sự suy giảm tương ứng (proportional) với sự khác biệt trong sự biến đổi các hàm (functions) (𝑓train(𝑥) ≠ 𝑓serve(𝑥)) (It violates the consistency imperative, causing silent accuracy degradation proportional to the difference in the transformation functions (𝑓train(𝑥) ≠𝑓serve(𝑥))).
2. Sự khác biệt: Không giống như dữ liệu sự trôi dạt (drift) (thứ mà là một bên ngoài sự dịch chuyển trong môi trường), sự đào tạo- việc phục vụ sự lệch là một nội bộ sự thất bại của kỹ thuật ngăn xếp, training-serving skew is an internal failure of the engineering stack).
3. Phổ biến cạm bẫy: Một thường xuyên quan niệm sai lầm là rằng sự lệch “tìm thấy” bằng cách việc tìm kiếm cho các lỗi. Trong thực tế, nó là vô hình đối với các ngoại lệ: hệ thống chạy một cách hoàn hảo và độ trễ là thấp, nhưng các dự đoán là (về mặt) thống kê (statistically) sai. Chương 14 cung cấp toàn diện sự phủ sóng (coverage) của sự lệch sự chẩn đoán (diagnosis), sự giám sát, và thuộc về tổ chức (organizational) sự phòng ngừa các chiến lược. Ở đây chúng ta tập trung trên cụ thể-việc phục vụ sự biểu hiện (manifestation): sự tiền xử lý sự phân kỳ. Điều này xảy ra khi thời gian thực sự suy luận đường ống xử lý thô dữ liệu một cách khác biệt (so với) lô (batch) sự đào tạo đường ống, một phổ biến sự thất bại chế độ khi sự đào tạo sử dụng Python/Pandas trong khi việc phục vụ sử dụng C++/Java hay được tối ưu hóa sự suy luận các máy chủ. Không giống như dữ liệu sự trôi dạt (thứ mà Chương 14 giải quyết thông qua sự giám sát), sự tiền xử lý sự phân kỳ là mang tính xác định và có thể phòng ngừa (preventable) thông qua cẩn thận kỹ thuật, preprocessing divergence is deterministic and preventable through careful engineering). Ví dụ 13.2: ResNet-50: Hình ảnh sự tiền xử lý sự lệch Kịch bản: Cho ResNet-50 việc phục vụ, ba sự tiền xử lý các sự lựa chọn một cách phổ biến phân kỳ giữa sự đào tạo và việc phục vụ các đường ống. • Thay đổi kích thước sự nội suy (interpolation): Sự đào tạo sử dụng PIL.BILINEAR trong khi OpenCV mặc định (tới) cv2.IN- TER_LINEAR. Những (sự nội suy) này tạo ra cấp độ-pixel (pixel-level) các sự khác biệt có thể dịch chuyển độ chính xác bởi 0.5–1 phần trăm. • Màu sắc không gian (Color space) việc xử lý: JPEG việc tải trong khác biệt các thư viện có thể tạo ra BGR so với RGB sự sắp xếp (ordering). Nếu mô hình (đã) được đào tạo trên RGB nhưng phục vụ BGR các đầu vào, các dự đoán là về cơ bản (essentially) ngẫu nhiên.

13.6 Mô hình Vòng đời Sự quản lý

CUDA (Compute (Sự tính toán) Unified (Được hợp nhất) Device (Thiết bị) Architecture (Kiến trúc)):
NVIDIA’s song song tính toán nền tảng (Nickolls và cộng sự 2008), được đặt tên cho nó mục tiêu của việc hợp nhất đa dạng GPU đổ bóng (shader) các mô hình
thành một đơn chung-mục đích kiến trúc. Trước CUDA,
GPU việc lập trình yêu cầu (đòi hỏi) việc ngụy trang (disguising) các sự tính toán như đồ họa các hoạt động.
CUDA
ngữ cảnh—dữ liệu
cấu trúc theo dõi bộ nhớ các sự cấp phát, được tải hạt nhân, và thiết bị trạng thái—là thời gian chạy’s (run- time) mỗi-tiến trình cổng (gateway) (vào) GPU các tài nguyên; trong không máy chủ (serverless)
hay nhanh chóng mở rộng việc phục vụ các hệ thống,
ngữ cảnh
sự tạo (ra) và lười biếng mô-đun (module) việc tải có thể trở thành có thể nhìn thấy phần của lạnh khởi động độ trễ.

CUDA MPS (Multi-
Process (Nhiều-Tiến trình)
Service (Dịch vụ)):
MPS tạo (ra) một điều khiển trình nền (daemon)
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
cá nhân
sử dụng dưới (mức) (underuse) máy gia tốc.
Cho
nhiều-mô hình việc phục vụ,
MPS có thể giúp các bản sao chia sẻ GPU luồng (streaming) các bộ đa xử lý (multiproces-
sors) hiệu quả. (Sự) đánh đổi
là lỗi sự cô lập: các máy khách chia sẻ được quản lý bởi-MPS GPU trạng thái, do đó phần cứng việc phân vùng (partitioning) với Nhiều-Phiên bản GPU
cung cấp mạnh hơn sự cô lập
tại chi phí của cố định phân vùng độ chi tiết (granularity).
Bảng 13.8: ResNet-50 lạnh khởi động dòng thời gian: Mỗi-giai đoạn các thời lượng cho trọng số việc tải, CUDA ngữ cảnh sự tạo, TensorRT sự biên dịch, và sự khởi động, với các tổng (số) cho được tối ưu hóa cục bộ trường hợp và đầu tiên-sự triển khai đám mây trường hợp việc cho thấy nơi thống trị chi phí sống.
Giai đoạn
Thời lượng
Các ghi chú
Trọng số việc tải (SSD)
0.5 s 98 MB FP32 các trọng số từ cục bộ lưu trữ
Trọng số việc tải (S3)
3–5 s Mạng độ trễ thống trị cho đám mây lưu trữ
CUDA ngữ cảnh
0.3–0.5 s GPU trình điều khiển (driver) sự khởi tạo và bộ nhớ thiết lập
TensorRT sự biên dịch
15–30 s Chuyển đổi PyTorch mô hình thành được tối ưu hóa công cụ
Sự khởi động (10 các sự suy luận)
0.2 s Kích hoạt còn lại lười biếng sự khởi tạo
Thời gian chạy chi phí hoạt động
0.4 s Tiến trình sự khởi nghiệp, bộ khung các móc (hooks), và thời gian chạy thiết lập
Tổng cộng (cục bộ, được tối ưu hóa)
~1.5 s Với được biên dịch trước TensorRT công cụ, ấm áp (warm) vùng chứa (container) Tổng cộng (đám mây, đầu tiên sự triển khai)
~35 s
Bao gồm sự biên dịch từ lạnh trạng thái Các hệ thống sự thấu hiểu: Việc biên dịch trước các mô hình và việc lưu trữ được tối ưu hóa công cụ loại bỏ 30- giây sự biên dịch giai đoạn trên tiếp theo các sự triển khai. CUDA ngữ cảnh16 là đầu tiên chi phí trong lạnh khởi động dòng thời gian. Trước khi bất kỳ GPU hoạt động , CUDA thời gian chạy phải thiết lập một ngữ cảnh: một dữ liệu cấu trúc thứ mà theo dõi bộ nhớ các sự cấp phát, được tải các hạt nhân, và thiết bị trạng thái. Việc tạo một ngữ cảnh yêu cầu việc giao tiếp với GPU trình điều khiển và việc cấp phát GPU bộ nhớ cho nội bộ việc ghi chép sổ sách (bookkeeping). 0.3–0.5 s giá trị trong bảng 13.8 là một kịch bản giả định cho này lạnh-khởi động ngân sách, không (phải) một phổ quát CUDA hằng số. CUDA lười biếng việc tải trì hoãn một số mô-đun và hạt nhân việc tải cho đến khi (lần) đầu tiên sử dụng, việc giảm thiểu bề ngoài (apparent) khởi nghiệp thời gian nhưng việc dịch chuyển một số chi phí (sang) đầu tiên sự suy luận (NVIDIA 2026a)). CUDA MPS (Nhiều-Tiến trình Dịch vụ)17 giải quyết GPU việc chia sẻ cho nhiều-tiến trình các sự triển khai17 addresses GPU sharing for multi-process deployments). Thông thường, mỗi tiến trình tạo ra riêng nó CUDA ngữ cảnh, và GPU có thể cắt-lát-thời-gian (time-slice) giữa các ngữ cảnh. MPS cho phép công việc từ nhiều các tiến trình (để) chồng chéo trên GPU thông qua một được chia sẻ dịch vụ, việc giảm thiểu chuyển đổi-ngữ cảnh chi phí hoạt động và việc cải thiện sự sử dụng khi cá nhân các tiến trình sử dụng dưới (mức) thiết bị (NVIDIA 2026d)). Sự đánh đổi là được giảm thiểu sự cô lập: một sự cố trong một tiến trình có thể ảnh hưởng (tới) (những tiến trình) khác chia sẻ MPS máy chủ. Không có sự khởi động, đầu tiên thực sự yêu cầu kích hoạt sự biên dịch và bộ nhớ sự cấp phát giữa-sự suy luận, thường gây ra thời gian chờ các sự thất bại. Một yêu cầu thứ mà thông thường tốn 5 ms có thể yêu cầu 500 ms trong suốt lạnh khởi động, việc vi phạm các SLO và việc làm suy giảm người dùng trải nghiệm.
13.6.3 Việc tải các chiến lược Khác biệt việc tải các chiến lược đánh đổi lạnh khởi động thời lượng đối nghịch việc phục vụ hiệu suất và bộ nhớ tính hiệu quả. Đơn giản nhất cách tiếp cận, đầy đủ việc tải, đọc toàn bộ mô hình vào bộ nhớ trước khi việc phục vụ bắt đầu. Điều này tối đa hóa sự suy luận tốc độ vì tất cả các trọng số là ngay lập tức sẵn sàng (available), nhưng kéo dài lạnh khởi động thời lượng và giới hạn mô hình kích thước (vào) sẵn sàng bộ nhớ. Cách tiếp cận là phù hợp (appropriate) khi lạnh khởi động độ trễ là (có thể) chấp nhận được và các mô hình một cách thoải mái (comfortably) khớp (vừa) trong bộ nhớ. Khi các mô hình là quá lớn cho ngay lập tức đầy đủ việc tải, bộ nhớ việc ánh xạ (mapping) cung cấp một thay thế bằng cách việc ánh xạ mô hình các tệp một cách trực tiếp vào địa chỉ không gian (address space) và việc tải các trang (pages) theo yêu cầu (on demand) khi được truy cập. Điều này giảm thiểu lạnh khởi động thời gian vì sự suy luận có thể bắt đầu trước khi đầy đủ mô hình tải, nhưng gây ra không thể đoán trước độ trễ khi các trang gặp lỗi (fault) trong (suốt) ban đầu các yêu cầu. Bộ nhớ việc ánh xạ làm việc tốt cho không thường xuyên (infrequently) được truy cập mô hình các thành phần nhưng có thể gây ra độ trễ các sự tăng vọt nếu chí mạng các trọng số không tải trước (preloaded). Một thứ ba chiến lược, lười biếng sự khởi tạo, trì hoãn sự biên dịch và sự cấp phát cho đến khi (lần) đầu tiên sử dụng. Điều này tối- thiểu hóa khởi nghiệp thời gian nhưng dịch chuyển độ trễ (sang) đầu tiên yêu cầu. Sản xuất các hệ thống thường kết hợp lười biếng sự khởi tạo với tổng hợp (synthetic) sự khởi động các yêu cầu để kích hoạt sự khởi tạo trước khi thực sự lưu lượng truy cập đến.
13.6.4 Mô hình việc lưu trong bộ nhớ đệm cơ sở hạ tầng Sản xuất các hệ thống lưu trong bộ nhớ đệm mô hình các trọng số tại cơ sở hạ tầng cấp độ để giảm thiểu lạnh khởi động cho phổ biến sự triển khai các kịch bản. Một cách tiếp cận, vùng chứa hình ảnh sự nhúng, bó (bundles) mô hình các trọng số một cách trực tiếp trong vùng chứa hình ảnh. Điều này tạo ra một đơn sự triển khai hiện vật và loại bỏ mạng các sự lấy (fetches) tại sự khởi nghiệp, nhưng tạo ra lớn các hình ảnh (thường 10–50 GB) làm chậm vùng chứa các sự kéo (pulls) và tiêu thụ sổ đăng ký (registry) lưu trữ (This produces a single deployment artifact and eliminates network fetches at startup, but creates large images (often 10–50 GB) that slow container pulls and consume registry storage). Cách tiếp cận này làm việc tốt nhất cho các mô hình hiếm khi cập nhật.

13. Mô hình Việc phục vụ (Model Serving)

MIG (Multi-Instance (Nhiều-Phiên bản)
GPU):
Được giới thiệu
với
NVIDIA’s
A100
(NVIDIA
Corporation 2020) và được tài-
liệu hóa (documented) qua được hỗ trợ dữ liệu-trung tâm (data-center) các GPU (NVIDIA 2026e),
MIG
phân vùng
một
đơn
vật lý
GPU
thành độc lập các phiên bản, mỗi với dành riêng tính toán và bộ nhớ các tài nguyên.
Không giống như
phần mềm việc chia sẻ (MPS hay
việc cắt-lát-thời-gian), MIG cung cấp
cấp độ-phần cứng
sự cô lập giữa các phân vùng.
Sự
đánh đổi
là
độ chi tiết—
các phân vùng phải tuân theo cố định các hồ sơ (profiles), do đó các tài nguyên không thể bị chia một cách tùy ý (arbitrarily).
Cho nhiều-mô hình việc phục vụ,
MIG giảm thiểu ồn ào-hàng xóm (noisy-neighbor) rủi ro
trên được chia sẻ phần cứng, trong khi
mỗi-mô hình SLO các sự đảm bảo
vẫn phụ thuộc vào bộ lập lịch
chính sách, tải, và được chọn phân vùng hồ sơ. Mô hình việc tải hạ cánh (lands) xa bên ngoài một chặt chẽ việc phục vụ SLO. Cho các tổ chức với nhiều các mô hình và thường xuyên các sự cập nhật, một được chia sẻ tệp hệ thống (EFS, GCS FUSE) chứa mô hình các trọng số cung cấp một linh hoạt hơn sự thay thế containing model weights provides a more flexible alternative). Nhiều các bản sao chia sẻ được lưu trong bộ nhớ đệm các trọng số, và các sự cập nhật lan truyền (propagate) ngay lập tức mà không có sự triển khai lại (redeployment). Sự đánh đổi là rằng mạng độ trễ ảnh hưởng (tới) lạnh khởi động, và tệp hệ thống tính có sẵn (availability) trở thành một chí mạng sự phụ thuộc. Khi lạnh khởi động độ trễ là chí mạng cho cao-lưu lượng truy cập các mô hình, nút-cục bộ (node-local) SSD việc lưu trong bộ nhớ đệm đưa (dữ liệu) vào trước (prepopulates) cục bộ các SSD trên sự suy luận các nút với thường xuyên-được sử dụng các mô hình. Cách tiếp cận này cung cấp nhanh việc tải từ Không-Bay hơi (Non-Volatile) Bộ nhớ Tốc hành (Express) (NVMe) các ổ đĩa tại 500 MB/s hay hơn mà không có mạng sự phụ thuộc, nhưng yêu cầu bộ nhớ đệm sự quản lý để xử lý mô hình các sự cập nhật và công suất các giới hạn drives at 500 MB/s or more without network dependency, but requires cache management to handle model updates and capacity limits). Sự lựa chọn giữa những các chiến lược này phụ thuộc vào mô hình cập nhật tần suất (frequency): không thường xuyên các sự cập nhật ưu ái (favor) vùng chứa sự nhúng, thường xuyên các sự cập nhật ưu ái được chia sẻ tệp hệ thống, và chí mạng-hiệu suất các sự triển khai hưởng lợi từ cục bộ việc lưu trong bộ nhớ đệm với nền (background) sự làm mới (refresh).
13.6.5 Nhiều-mô hình việc phục vụ Sản xuất các hệ thống thường phục vụ nhiều các mô hình từ một đơn máy móc, cho dù khác biệt mô hình các phiên bản (versions) cho A/B việc kiểm tra, tập hợp các thành phần, hay hoàn toàn khác biệt các mô hình chia sẻ cơ sở hạ tầng. GPU bộ nhớ trở thành giới hạn tài nguyên, việc yêu cầu cẩn thận sự quản lý các chiến lược. Ba các chiến lược giải quyết nhiều-mô hình bộ nhớ sự quản lý. Cắt ghép-thời gian (Time-multiplexing) tải một mô hình tại một thời điểm và hoán đổi (swaps) dựa trên yêu cầu việc định tuyến—đơn giản nhưng giới thiệu hoán đổi độ trễ. Bộ nhớ việc chia sẻ (Memory sharing) phân vùng GPU bộ nhớ (giữa) các mô hình, việc giới hạn đồng thời sự thực thi số đếm nhưng việc kích hoạt nhiều (hơn) các mô hình (để) duy trì thường trú (resident). Mô hình sự ảo hóa, như được triển khai bởi các bộ khung như Triton, tách biệt mô hình vòng đời khỏi ứng dụng mã thông qua mô hình kho lưu trữ và điều khiển các API cho việc tải, việc dỡ (unloading), và việc tạo phiên bản (versioning) các mô hình). Sự lựa chọn phụ thuộc vào yêu cầu các mẫu (patterns): nếu các mô hình nhận lưu lượng truy cập đồng đều, đồng thời việc tải làm việc; nếu lưu lượng truy cập là đợt (bursty) và cụ thể-mô hình, việc cắt ghép-thời gian với rõ ràng (explicit) việc tải trước (preloading) giảm thiểu trung bình độ trễ trong khi việc tối đa hóa GPU sự sử dụng.
13.6.5.1 Nhiều-luồng (Multi-stream) sự thực thi Khi nhiều các mô hình hay nhiều các phiên bản của giống nhau mô hình phải chạy đồng thời trên một đơn GPU, phần cứng phải phân vùng các tài nguyên giữa chúng. NVIDIA’s Nhiều-Phiên bản GPU18 công nghệ kích hoạt cấp độ-phần cứng sự cô lập, việc chia một A100 thành lên tới bảy độc lập GPU các phiên bản, mỗi với dành riêng bộ nhớ và tính toán các tài nguyên (NVIDIA 2026e) (NVIDIA’s Multi-Instance GPU18 technology enables hardware-level isolation, dividing an A100 into up to seven independent GPU instances, each with dedicated memory and compute resources (NVIDIA 2026e)). MIG là sẵn sàng trên A100, A30 (lên tới bốn các phiên bản), H100, H200, và mới hơn dữ liệu trung tâm các GPU, H100, H200, and newer data center GPUs). Cho cũ hơn các GPU như là V100 hay T4, CUDA luồng sự lập lịch cung cấp cắt ghép-thời gian việc chia sẻ mà không có phần cứng sự cô lập. Sự lựa chọn phụ thuộc vào liệu nhất quán độ trễ với MIG hay tối đa sự sử dụng với chia sẻ các luồng là sự ưu tiên (hay không).
13.6.5.2 Mô hình sự hoán đổi (swapping) và máy chủ bộ nhớ Khi tổng hợp (aggregate) kích thước của tất cả các mô hình vượt quá GPU bộ nhớ công suất, việc phục vụ hệ thống phải hoán đổi các mô hình giữa máy chủ bộ nhớ (DRAM) và thiết bị bộ nhớ (VRAM) theo yêu cầu and device memory (VRAM) on demand). Điều này giới thiệu một mới độ trễ thành phần xác định bởi PCIe bus băng thông. Cho một 10 GB mô hình trên PCIe Gen4 x16 (32 GB/s lý thuyết băng thông), việc tải tốn ít nhất 312.5 ms trước khi sự giải tuần tự hóa (deserialization), đồ thị thiết lập, hay sự khởi động, loading takes at least 312.5 ms before deserialization, graph setup, or warmup). Để giảm nhẹ điều này, các hệ thống sử dụng được ghim (pinned) bộ nhớ (được khóa-trang máy chủ bộ nhớ)). Theo mặc định, hoạt động hệ thống (hệ điều hành) có thể di chuyển (“phân trang” (page)) bất kỳ bộ nhớ khu vực tới đĩa khi RAM là dưới áp lực (By default, the operating system can move (“page”) any memory region to disk when RAM is under pressure). Điều này tạo ra một vấn đề cho GPU các sự truyền (transfers): nếu GPU’s DMA (Trực tiếp Bộ nhớ Truy cập) công cụ bắt đầu (việc) đọc một bộ nhớ khu vực bị (get) phân trang ra (paged out) giữa-sự truyền, sự truyền thất bại hay đình trệ (This creates a problem for GPU transfers: if the GPU’s DMA (Direct Memory Access) engine begins reading a memory region that gets paged out mid-transfer, the transfer fails or stalls). Để tránh điều này, CPU phải trước tiên sao chép dữ liệu tới một tạm thời được ghim bộ đệm trước khi GPU có thể một cách an toàn đọc nó, việc thêm cả hai độ trễ và CPU chi phí hoạt động. Việc ghim bộ nhớ hướng dẫn (instructs) HĐH (OS) (để) giữ đó khu vực vĩnh viễn (permanently) trong vật lý RAM. GPU’s DMA công cụ có thể sau đó truyền dữ liệu một cách trực tiếp từ được ghim khu vực mà không có một bổ sung (extra) (từ) có-thể-phân-trang-tới- được ghim (pageable-to-pinned) dàn dựng (staging) bản sao. Sự đánh đổi là rằng được ghim bộ nhớ giảm thiểu RAM sẵn sàng cho (các tiến trình) khác các tiến trình và không thể đòi lại (reclaimed) dưới bộ nhớ áp lực. Cho mô hình việc phục vụ, sự truyền-con đường sự cải thiện thường biện minh (cho) (justifies) việc ghim mô hình các trọng số và thường xuyên-được sử dụng đầu vào các bộ đệm, trong khi việc để lại ít chí mạng (hơn) bộ nhớ (để) có thể phân trang. Vòng đời sự quản lý các chiến lược được kiểm tra cho đến nay đảm bảo các mô hình là sẵn sàng để phục vụ: tải vào bộ nhớ, làm ấm lên (warmed up), và tạo ra các dự đoán nhất quán với sự đào tạo. Với những các điều kiện tiên quyết này

13. Mô hình Việc phục vụ (Model Serving)

13.7 Thông lượng Sự tối ưu hóa

Lô (Batch): Từ Cũ Tiếng Pháp (Old French)
bache (một số lượng được nướng tại
một thời điểm), (việc) đi vào điện- toán trong những năm 1950 cho các công việc xử- lý (processed) cùng nhau mà không có con-
người sự tương tác. ML việc phục- vụ cách sử dụng bảo tồn (preserves) ban-
đầu sự đánh đổi:
việc nhóm các yêu- cầu khấu hao (amortizes) cố định các chi phí (hạt nhân sự khởi chạy, trọng số việc tải) qua nhiều các đầu vào,
nhưng mỗi yêu cầu phải chờ đợi cho lô (để) lấp đầy (fill). Trong sự đào-
tạo, các lô của 256–4096 là thông thường (routine); trong việc phục vụ, các lô
trên 8–32 điển hình vi phạm độ trễ
các SLO, việc làm việc phục- vụ lô (trở thành) một (về mặt) cơ bản khác biệt sự tối ưu hóa mục tiêu.

Hạt nhân (Kernel) (GPU): CUDA
đã mượn
này
thuật ngữ
từ
hoạt động
các hệ thống
khoảng (circa)
2007 bởi vì GPU các hàm
đại diện thuộc về tính toán “cốt lõi” (core) của song song các thuật toán. Không giống như HĐH (OS) các hạt nhân chạy
liên tục, GPU các hạt nhân là rời rạc (discrete) các đơn vị của song song công việc khởi chạy bởi CPU.
Mỗi sự khởi chạy mang (carries) 5–20 𝜇s
của chi phí hoạt động độc lập với
lô
kích thước—không đáng kể (negligible)
cho
lớn sự đào tạo các lô nhưng thống trị tại lô-1 việc phục vụ,
nơi
một
50-lớp (layer)
mô hình
tích lũy (accumulates) 250–1000 𝜇s của thuần túy (pure) sự khởi chạy chi phí hoạt động cho mỗi sự suy luận. được thỏa mãn (satisfied), việc xếp hàng đợi động lực học từ phần 13.5 trở nên có liên quan. Tiếp theo sự tối ưu hóa cơ- hội (opportunity) nằm trong cách các yêu cầu được nhóm (lại) cho việc xử lý, thứ mà một cách trực tiếp ảnh hưởng (tới) cả thông lượng và độ trễ các thuật ngữ (terms) trong chúng ta việc xếp hàng đợi các phương trình.
13.7 Thông lượng Sự tối ưu hóa Hãy xem xét một đại diện ResNet-50 bộ phân loại kịch bản trên một V100 GPU tại lô kích thước một: GPU xử lý một hình ảnh, sau đó ngồi nhàn rỗi (idle) trong khi CPU lấy (fetches) và tiền xử lý tiếp theo—việc đạt được chỉ 15 phần trăm phần cứng sự sử dụng và 200 các hình ảnh mỗi giây. Giống nhau GPU xử lý 32 các hình ảnh tại một lúc đạt tới 95 phần trăm sự sử dụng và 1,280 các hình ảnh mỗi giây, một 6.4× thông lượng sự cải thiện trên giống hệt phần cứng bởi vì cố định các chi phí được khấu hao qua các yêu cầu. Sự khác biệt là việc tạo lô (batching), cốt lõi đòn bẩy (lever) cho việc cải thiện việc phục vụ tính kinh tế (economics). Việc tạo lô19 khác biệt sắc bén giữa sự đào tạo và việc phục vụ (Crankshaw và cộng sự 2017)). Sự đào tạo các lô tối đa hóa thông lượng bằng cách việc xử lý hàng trăm hay hàng ngàn các mẫu (samples) cùng nhau với không mối bận tâm (concern) cho cá nhân mẫu độ trễ. Việc phục vụ các lô phải cân bằng thông lượng đối nghịch cá nhân yêu cầu độ trễ, thường (việc) xử lý nhỏ các lô trong khi việc đảm bảo không yêu cầu chờ đợi quá lâu. Này thích ứng cách tiếp cận được gọi (là) động (dynamic) việc tạo lô bởi vì hệ thống điều chỉnh lô thành phần (composition) trong thực thời gian dựa trên đến các yêu cầu. Định nghĩa 13.5: Động việc tạo lô Động Việc tạo lô là ML việc phục vụ sự tối ưu hóa đánh đổi Độ trễ cho Thông lượng dưới ngẫu nhiên (stochastic) đến các mẫu.
1. Tầm quan trọng: Bằng cách việc đệm (buffering) các yêu cầu vào một việc tạo lô cửa sổ, bộ lập lịch khấu hao cố định các chi phí hoạt động (𝐿lat) qua nhiều các đầu vào, việc đẩy hệ thống ra xa khỏi bị giới hạn-bởi-bộ-nhớ chế độ (regime) (BW) hướng tới bị giới hạn-bởi-tính-toán chế độ (𝑅peak) (By buffering requests into a batching window, the scheduler amortizes fixed overheads (𝐿lat) across multiple inputs, pushing the system away from the memory-bound regime (BW) toward the compute-bound regime (𝑅peak)).
2. Sự khác biệt: Không giống như Tĩnh Việc tạo lô (Static Batching), thứ mà được cố định trong suốt sự đào tạo, Động Việc tạo lô thích ứng điều chỉnh lô kích thước tại Sự suy luận Thời gian dựa trên thực-thời gian lưu lượng truy cập khối lượng.
3. Phổ biến cạm bẫy: Một thường xuyên quan niệm sai lầm là rằng việc tạo lô “luôn luôn giúp ích”. Trong thực tế, có một độ trễ-thông lượng Pareto biên giới (frontier): nếu việc tạo lô cửa sổ là quá lớn, được làm tăng việc xếp hàng đợi sự chậm trễ có thể vi phạm hệ thống’s SLO trước khi thông lượng các lợi ích (gains) được nhận ra (realized).
13.7.1 Tại sao việc tạo lô giúp ích Hiện đại các máy gia tốc đạt được đỉnh tính hiệu quả chỉ tại đủ lô các kích thước (Shen và cộng sự 2019)). Một đơn sự suy luận yêu cầu để lại hầu hết tính toán các đơn vị (units) nhàn rỗi bởi vì các GPU được thiết kế cho song song sự thực thi qua hàng ngàn các luồng (threads). Việc tạo lô khấu hao cố định các chi phí qua nhiều các yêu cầu và kích hoạt song song sự thực thi qua lô chiều (dimension). Hai cố định các chi phí thống trị tại nhỏ lô các kích thước. Hạt nhân sự khởi chạy chi phí hoạt động20 là thời gian cho CPU để chuẩn bị và gửi (submit) công việc tới GPU. Mỗi lớp trong một nơ-ron mạng điển hình yêu cầu một riêng biệt hạt nhân sự khởi chạy: CPU phải lắp ráp hạt nhân các tham số, sao chép chúng tới có-thể-truy-cập-bởi-GPU bộ nhớ, và ra hiệu (signal) (cho) GPU để bắt đầu sự thực thi. Chi phí hoạt động này là điển hình 5–20 μs cho mỗi hạt nhân, độc lập với lô kích thước. ResNet-50 có xấp xỉ năm mươi các lớp, do đó hạt nhân sự khởi chạy một mình (nó) thêm 250–1000 μs cho mỗi sự suy luận. Tại lô kích thước một, chi phí hoạt động này có thể vượt quá thực sự tính toán thời gian; tại lô kích thước ba mươi hai, giống nhau chi phí hoạt động được khấu hao qua ba mươi hai các hình ảnh. Trọng số việc tải đọc mô hình các tham số từ GPU bộ nhớ (VRAM) tới tính toán các đơn vị to the compute units). Tại lô kích thước một, GPU đọc tất cả các trọng số để xử lý một hình ảnh; tại lô kích thước ba mươi hai, giống nhau trọng số đọc xử lý ba mươi hai các hình ảnh, (việc) đạt được 32× tốt hơn bộ nhớ tính hiệu quả. Việc đo lường việc tạo lô tính hiệu quả trên một cụ thể mô hình định lượng cách những cố định các chi phí này khấu hao trong thực tế. Khăn ăn Toán học 13.6: ResNet-50 việc tạo lô tính hiệu quả
Bảng 13.9 minh họa (illustrates) thông lượng-độ trễ sự đánh đổi cho một ResNet-50/V100 kịch bản qua lô các kích thước (từ) một đến (through) ba mươi hai. Lô các kích thước, được đo lường sự suy luận các thời gian, và GPU

13. Mô hình Việc phục vụ

sự sử dụng là kịch bản thứ được cho (givens); mỗi-hình ảnh tính toán và thông lượng các cột được bắt nguồn (derived) từ chúng. Toán học: Cho lô-8 hàng, mỗi-hình ảnh tính toán là lô độ trễ được chia (divided) bởi lô kích thước,
9.1 ms ÷ 8 các hình ảnh ≈ 1.1 ms cho mỗi hình ảnh, và thông lượng là lô kích thước được chia bởi giống nhau độ trễ, 8 các hình ảnh ÷ 9.1 ms ≈ 879 hình ảnh/s. (Cái) giống nhau hai phép chia tạo ra mọi được bắt nguồn hàng.
Bảng 13.9: ResNet-50 việc tạo lô quét (sweep): Mỗi-hình ảnh tính toán, thông lượng, và GPU sự sử dụng qua lô các kích thước (từ) một đến ba mươi hai trên một V100. Thông lượng phát triển 6.4× từ lô một tới lô ba mươi hai khi GPU sự sử dụng leo (lên) từ 15 phần trăm tới 95 phần trăm, trong khi thuần túy sự suy luận thời gian kéo dài (stretches) từ 5 ms tới 25 ms.
Lô Kích thước
Sự suy luận Thời gian
Mỗi-Hình ảnh Tính toán
Thông lượng
GPU Sự sử dụng (Util.)

5 ms
5 ms
200 hình ảnh/s
15%

7.2 ms
1.8 ms
556 hình ảnh/s
42%

9.1 ms
1.1 ms
879 hình ảnh/s
65%

14 ms
0.9 ms
1,143 hình ảnh/s
85%

25 ms
0.8 ms
1,280 hình ảnh/s
95% Các thời gian được hiển thị là thuần túy sự suy luận thời gian, việc loại trừ hàng đợi sự chờ đợi; phần 13.7.6 phân tích cách được nhận thức-bởi-người dùng độ trễ bao gồm việc tạo lô-cửa sổ sự chờ đợi. Các hệ thống sự thấu hiểu: Lô kích thước ba mươi hai đạt được 6.4× cao hơn thông lượng (so với) lô kích thước 1. Tuy nhiên, được nhận thức-bởi-người dùng độ trễ bao gồm cả hàng đợi sự chờ đợi và sự suy luận thời gian. Với một 10 ms việc tạo lô cửa sổ và 25 ms sự suy luận, tổng độ trễ đạt tới 35 ms so với 5 ms tại lô kích thước 1.
Bảng tiết lộ thông lượng-độ trễ sự đánh đổi trong khắc nghiệt (stark) các thuật ngữ: lớn hơn các lô quyết liệt cải thiện phần cứng tính hiệu quả nhưng làm tăng mỗi-yêu cầu độ trễ. Trong thực tế, tối ưu lô kích thước phụ thuộc vào cả độ trễ Dịch vụ Cấp độ Mục tiêu (SLO) và đến tỷ lệ của các yêu cầu and the arrival rate of requests). (Cái) câu hỏi đối mặt mọi việc phục vụ kỹ sư là do đó (mang tính) định lượng (quantitative): việc xác định lớn nhất lô kích thước vẫn đáp ứng một được cho độ trễ SLO. Trong kịch bản này, lô kích thước 8 với một 5 ms việc tạo lô cửa sổ có tồi tệ nhất-trường hợp người dùng độ trễ của khoảng 14 ms (5 ms đợi cộng 9 ms sự suy luận), dưới một 20 ms SLO ngân sách, below a 20 ms SLO budget). (Điều) đó kiếm gần 3× cao hơn dịch vụ thông lượng (so với) lô-1 việc phục vụ trên giống hệt phần cứng, miễn là (provided) được duy trì (sustained) tải là (đủ) cao (để) lấp đầy việc tạo lô cửa sổ. Việc vẽ (Plotting) giống nhau sự đánh đổi trong hình 13.6 tiết lộ đầu gối nơi (việc) thêm việc tạo lô dừng trả (tiền) cho nó độ trễ chi phí: thông lượng đã san phẳng (flattening) trong khi độ trễ bắt đầu (để) tăng vọt, do đó việc tạo lô vượt ra ngoài đó điểm đánh đổi khiêm tốn công suất các lợi ích cho việc xếp hàng đợi sự chậm trễ.

Lô Kích thước

Thông lượng (Các yêu cầu/sec)
Tối ưu
Điểm

Độ trễ (ms)
Hình 13.6: Thông lượng-Độ trễ Đầu gối: Lô kích thước so với thông lượng (màu xanh lam) và độ trễ (màu cam) and latency (orange)). Thông lượng tăng với lô kích thước khi phần cứng sự sử dụng cải thiện, nhưng cuối cùng bão hòa. Độ trễ duy trì tương đối bằng phẳng cho đến khi đầu gối, sau đó nó tăng vọt do (bởi) việc xếp hàng đợi. Các giá trị là (mang tính) đại diện và phụ thuộc vào mô hình/phần cứng.

13. Mô hình Việc phục vụ (Model Serving)

13.7 Thông lượng Sự tối ưu hóa “Đầu gối” trong hình 13.6 đánh dấu điểm nơi màu xanh lam thông lượng đường cong bắt đầu (để) bình nguyên (plateau) ngay khi (just as) màu cam độ trễ đường cong bắt đầu nó sắc bén hướng lên trên (upward) sự tăng vọt. Đây là tối ưu hoạt động điểm: (việc) đẩy lô kích thước vượt ra ngoài đầu gối và việc xếp hàng đợi các sự chậm trễ thống trị; (việc) ở lại (staying) dưới nó để lại phần cứng công suất trên bàn. Các con số là đại diện thay vì bị buộc (tied) vào một đơn điểm chuẩn (benchmark). Tính hiệu quả các lợi ích từ việc tạo lô đi kèm (tại) một chi phí: các yêu cầu phải chờ đợi cho lô (để) hình thành. Điều này tạo ra một trực tiếp sự căng thẳng giữa thông lượng sự tối ưu hóa (lớn hơn các lô) và độ trễ sự tối thiểu hóa (minimization) (ngay lập tức việc xử lý) and latency minimization). Khác biệt việc tạo lô các chiến lược và của chúng các sự đánh đổi chi phối (govern) cách các kỹ sư điều chỉnh (tune) này cân bằng.
13.7.2 Tĩnh so với động việc tạo lô Tĩnh việc tạo lô chờ đợi cho một cố định lô kích thước trước khi việc xử lý, thứ mà là đơn giản để triển khai nhưng mong manh (fragile) dưới có thể thay đổi (variable) lưu lượng truy cập: trong suốt thấp lưu lượng truy cập, các yêu cầu chờ đợi vô thời hạn (indefinitely) cho một đầy (full) lô, và trong suốt cao lưu lượng truy cập, lớn các lô làm tăng mỗi-yêu cầu độ trễ. Động việc tạo lô giải quyết này sự thất bại chế độ bằng cách việc thu thập các yêu cầu bên trong một được giới hạn (bounded) thời gian cửa sổ và việc xử lý bất cứ gì đã đến khi cửa sổ đóng lại (Olston và cộng sự 2017; NVIDIA 2024d)). Cửa sổ kích thước trở thành sự điều chỉnh núm (knob): ngắn hơn các cửa sổ giảm thiểu độ trễ nhưng hy sinh thông lượng, dài hơn các cửa sổ cải thiện thông lượng nhưng làm tăng độ trễ, và nhạy cảm-độ trễ các sự triển khai điều chỉnh cả thời gian cửa sổ và tối đa lô kích thước đối nghịch đến mẫu, mô hình hình dạng (shape), và SLO.
13.7.3 Động việc tạo lô độ trễ-thông lượng các sự đánh đổi Động việc tạo lô giới thiệu một có-thể-định-lượng (quantifiable) sự căng thẳng giữa thông lượng sự tối ưu hóa và độ trễ các sự ép buộc. Dưới sự quá tải, cơ chế là hàng đợi sự phát triển thay vì chậm hơn sự suy luận, thứ mà kích hoạt có hệ thống (systematic) cấu hình các quyết định thay vì thử-và-sai (trial-and-error) sự điều chỉnh. Các hệ thống Góc nhìn 13.6: Tại sao độ trễ tăng vọt dưới tải Hãy nhớ lại từ phần 13.5.1: Little’s Định luật (𝑄req = 𝜆arr𝑇lat) chi phối tất cả ổn định các hàng đợi (Recall from section 13.5.1: Little’s Law (𝑄req = 𝜆arr𝑇lat) governs all stable queues). Khi phần cứng bão hòa, dịch vụ tỷ lệ 𝜇 là phát huy tối đa (maxed out); nếu đến tỷ lệ 𝜆arr phát triển vượt ra ngoài đó công suất, hàng đợi độ sâu (𝑄req) tăng lên (When hardware is saturated, the service rate 𝜇 is maxed out; if the arrival rate 𝜆arr grows beyond that capacity, queue depth (𝑄req) increases). Vì 𝜇 không thể phát triển, độ trễ (𝑇lat) phải phát triển với hàng đợi độ sâu (Since 𝜇 cannot grow, latency (𝑇lat) must grow with queue depth). Đây là lý do tại sao sự thu nhận kiểm soát (việc từ chối các yêu cầu khi 𝑇lat vượt quá một ngưỡng) là duy nhất cách để bảo tồn độ trễ trong suốt sự quá tải (This is why admission control (rejecting requests when 𝑇lat exceeds a threshold) is the only way to preserve latency during overload). Phương trình 13.7 phân rã (decomposes) tổng được nhận thức-bởi-người dùng độ trễ cho một được tạo lô yêu cầu thành hai các thành- phần:
𝐿lat = 𝐿lat,wait + 𝐿lat,compute(𝐵)
(13.7) nơi 𝐿lat,wait là thời gian tiêu tốn (để) chờ đợi trong việc tạo lô hàng đợi (việc tương ứng (corresponding) (với) 𝐿lat,queue trong tổng thể độ trễ ngân sách) và 𝐿lat,compute(𝐵) là sự suy luận thời gian cho lô kích thước 𝐵 (việc bao trùm (encompassing) 𝐿lat,infer cộng các phần của 𝐿lat,pre và 𝐿lat,post) (where 𝐿lat,wait is the time spent waiting in the batching queue (corresponding to 𝐿lat,queue in the overall latency budget) and 𝐿lat,compute(𝐵) is the inference time for batch size 𝐵(encompassing 𝐿lat,infer plus portions of 𝐿lat,pre and 𝐿lat,post)). Việc tạo lô cửa sổ 𝑇window giới hạn sự chờ đợi thời gian (𝐿lat,wait ≤ 𝑇window), trong khi lô kích thước ảnh hưởng (tới) tính toán thời gian thông qua GPU sự sử dụng các đặc tính.
13.7.3.1 Định lượng sự phân tích của việc tạo lô Cho Poisson các sự đến với tỷ lệ 𝜆arr và việc tạo lô cửa sổ 𝑇window, các yêu cầu đến đồng đều (uniformly) bên trong cửa sổ. Một yêu cầu đến tại thời gian 𝑡 bên trong cửa sổ chờ đợi 𝑇window − 𝑡 cho lô (để) đóng lại. Phương trình 13.8 cho thấy rằng trung bình sự chờ đợi thời gian là đơn giản (bằng) một nửa cửa sổ:
𝐸[𝐿lat,wait] = 𝑇window / 2 (13.8) Này đơn giản mối quan hệ có trực tiếp các hàm ý. Một 20 ms việc tạo lô cửa sổ thêm 10 ms trung bình sự chờ đợi (lên tới 20 ms cho đầu tiên sự đến trong một cửa sổ; muộn hơn các sự đến chờ đợi ít hơn) bất kể của lô kích thước đạt được regardless of batch size achieved). Cho một 50 ms trung bình độ trễ SLO với 5 ms sự suy luận, trung bình sự chờ đợi tiêu thụ 20 phần trăm của độ trễ ngân sách trước khi bất kỳ tính toán bắt đầu; đuôi các SLO phải lập ngân sách (cho) đầy (full) cửa sổ.

13. Mô hình Việc phục vụ (Model Serving)

13.7.3.2 Lô kích thước sự phân phối Số lượng các yêu cầu thu thập trong suốt cửa sổ 𝑇window tuân theo một Poisson phân phối với mức trung bình 𝜆arr𝑇window. Phương trình 13.9 chính thức hóa (formalizes) mối quan hệ này: Pr(lô kích thước = 𝑘) = (𝜆arr𝑇window)𝑘𝑒−𝜆arr𝑇window / 𝑘!
(13.9)
Bảng 13.10 định lượng này tính biến đổi (variability), việc cho thấy cách lô kích thước dao động (fluctuates) cho khác biệt lưu lượng truy cập các cấp độ
với một cố định 10 ms cửa sổ:
Bảng 13.10: Lô Kích thước Tính biến đổi: Tại thấp lưu lượng truy cập, việc tạo lô các cửa sổ thường xuyên chứa không các yêu cầu (bị lãng phí GPU các chu kỳ)). Tại vừa phải lưu lượng truy cập, lô các kích thước dao động một cách đáng kể xung quanh mức trung bình. Cao lưu lượng truy cập cung cấp ổn định hơn việc tạo lô, và xác suất của các lô (việc) đạt tới ít nhất hai lần trung bình kích thước giảm thiểu khi lưu lượng truy cập phát triển (từ 39 phần trăm tại 50 QPS tới 0.3 phần trăm tại 1000 QPS), việc phản ánh định luật của lớn các con số, reflecting the law of large numbers).
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

1.4
14%
14%
500 QPS

2.2
0.7%
3%
1000 QPS

3.2
0.005%
0.3%
13.7.3.3 Thông lượng sự tối đa hóa chiến lược Thông lượng sự tối ưu hóa yêu cầu việc tách biệt mỗi-yêu cầu độ trễ khỏi bị bão hòa dịch vụ công suất. Một yêu cầu chờ đợi cho lô sự hình thành (formation), sau đó trả (tiền) cho dịch vụ thời gian của được hình thành lô. Dưới được duy trì tải, tuy nhiên, lô sự hình thành có thể chồng chéo với trước đó lô’s sự thực thi, do đó công suất là chi phối bởi sẵn-sàng-lô (ready-batch) dịch vụ thời gian (Under sustained load, however, batch formation can overlap with the previous batch’s execution, so capacity is governed by the ready-batch service time): 𝜇eff(𝐵) ≈ 𝐵 / 𝑇svc(𝐵),
thông lượng = min(𝜆arr, 𝜇eff(𝐵))
(13.10) Trong phương trình 13.10, 𝜆arr là được cung cấp đến tỷ lệ và 𝜇eff(𝐵) là bị bão hòa dịch vụ công suất cho lô kích thước 𝐵 (In equation 13.10, 𝜆arr is the offered arrival rate and 𝜇eff(𝐵) is the saturated service capacity for batch size 𝐵). Tử số (numerator) tăng lên một cách tuyến tính với lô kích thước trong khi dịch vụ thời gian thường tăng lên dưới-tuyến tính (sub-linearly) qua một hữu ích phạm vi bởi vì GPU tính song song là được sử dụng tốt hơn. Việc tạo lô cửa sổ vẫn xuất hiện trong yêu cầu độ trễ và trong thấp-lưu lượng truy cập các chế độ, nơi được mong đợi lô kích thước là bị giới hạn bởi các sự đến trong suốt cửa sổ, xấp xỉ 𝜆arr𝑇window. Cho ResNet-50 trên một V100 GPU, dịch vụ thời gian xấp xỉ mở rộng như 𝑇svc(𝐵) = 5 ms + 0.6𝐵 (5 ms cố định chi phí hoạt động cộng 0.6 ms cho mỗi hình ảnh trong lô) (For ResNet-50 on a V100 GPU, service time approximately scales as 𝑇svc(𝐵) = 5 ms + 0.6𝐵). Này tuyến tính sự xấp xỉ nắm bắt (captures) thống trị xu hướng (trend); thực sự dịch vụ các thời gian có thể sai lệch (deviate) một cách nhẹ (slightly) do (bởi) bộ nhớ hệ thống phân cấp (hierarchy) các hiệu ứng. Với một 𝑇window = 10 ms việc tạo lô cửa sổ, bảng 13.11 mở rộng thuần túy-sự suy luận sự quét của bảng 13.9 bằng cách việc gấp (folding) (vào) cửa sổ sự chờ đợi, do đó của nó độ trễ cột phản ánh đầu cuối-tới-đầu cuối chi phí thay vì sự suy luận thời gian một mình (nó) (With a 𝑇window = 10 ms batching window, table 13.11 extends the pure-inference sweep of table 13.9 by folding in the window wait, so its latency column reflects end-to-end cost rather than inference time alone:):
Bảng 13.11: Việc tạo lô Thông lượng Sự phân tích: Kịch bản sự phân tích cho ResNet-50 thông lượng trên V100 với 10 ms việc tạo lô cửa sổ. Thông lượng tăng lên 14.6× từ lô kích thước một tới 32 (64 hình ảnh/s tới 936 hình ảnh/s), nhưng tổng độ trễ nhiều hơn gấp đôi (15.6 ms tới
34.2 ms) (Throughput increases 14.6× from batch size one to 32 (64 img/s to 936 img/s), but total latency more than doubles). Tối ưu cấu hình phụ thuộc vào liệu độ trễ SLO hay thông lượng mục tiêu là ràng buộc (binding) sự ép buộc (hay không).
Lô Kích thước
Dịch vụ Thời gian
Tổng Độ trễ
Thông lượng
Tính hiệu quả

5.6 ms
15.6 ms
64 hình ảnh/s
Thấp

7.4 ms
17.4 ms
230 hình ảnh/s
Vừa phải

9.8 ms
19.8 ms
404 hình ảnh/s
Tốt

14.6 ms
24.6 ms
650 hình ảnh/s
Cao

24.2 ms
34.2 ms
936 hình ảnh/s
Tối đa Thông lượng các lợi ích trong bảng 13.11 theo dấu một cách trực tiếp trở lại (tới) cố định-chi phí hoạt động thuật ngữ trong sắt định luật được thiết lập trong phần 8.2, nơi việc tạo lô khấu hao công việc qua các yêu cầu.

13.7 Thông lượng Sự tối ưu hóa Khăn ăn Toán học 13.7: Sắt định luật của việc tạo lô tính hiệu quả Sắt định luật sự kết nối (connection): Trong việc phục vụ, việc tạo lô cải thiện thông lượng bằng cách việc khấu hao cố định mỗi-lô công việc như là sự lập lịch, hạt nhân sự khởi chạy, và trọng số các đọc; hàng đợi sự chờ đợi duy trì một riêng biệt độ trễ chi phí. Giống nhau sắt-định luật sự phân rã từ phương trình 13.11 cho thấy tại sao:
𝑇 = 𝑂 / (𝑅peak ⋅ 𝜂hw) + 𝐿lat
(13.11) Việc bắt nguồn (Deriving) ngọt ngào điểm (sweet spot): • Trường hợp 1 (lô 1): Chi phí hoạt động (5 ms) ฀ Tính toán (0.6 ms) (Case 1 (batch 1): Overhead (5 ms) ฀Compute (0.6 ms)). Tính hiệu quả ≈ 10 phần trăm. GPU là hầu hết chờ đợi. • Trường hợp 2 (lô 32): Chi phí hoạt động (5 ms) ฀ Tính toán (19.2 ms): Overhead (5 ms) ฀Compute (19.2 ms)). Tính hiệu quả ≈ 79 phần trăm. GPU là nhai (crunching) các con số. Vàng quy tắc: Tăng lô kích thước cho đến khi cố định chi phí hoạt động trở nên không đáng kể (< 10 phần trăm của tổng thời gian) hay độ trễ SLO chặn (chặn đứng) xa hơn sự chờ đợi or the latency SLO blocks further waiting). Vượt ra ngoài này điểm, bổ sung (additional) việc tạo lô mang lại tối thiểu thông lượng nhưng áp đặt một tuyến tính việc xếp hàng đợi hình phạt (penalty). Những ba các kết quả này soạn (compose) thành một hoạt động mô hình của động việc tạo lô: cửa sổ thiết lập trung bình sự chờ đợi tại một nửa nó chiều dài, Poisson các sự đến làm được nhận ra lô kích thước dao động xung quanh 𝜆arr𝑇window, và bị bão hòa dịch vụ công suất 𝜇eff(𝐵) leo (lên) với lô kích thước cho đến khi cố định chi phí hoạt động khấu hao hoàn toàn (away) (These three results compose into one working model of dynamic batching: the window sets the average wait at half its length, Poisson arrivals make the realized batch size fluctuate around 𝜆arr𝑇window, and the saturated service capacity 𝜇eff(𝐵) climbs with batch size until fixed overhead is amortized away). Không ai (cái nào) trong số chúng vẫn chưa thi hành độ trễ SLO. Các đường chuyền (passes) tuân theo (theo sau) thêm đó thiếu sự ép buộc, việc làm việc ngược (backward) từ một cứng phân vị ngân sách tới lớn nhất lô cửa sổ có thể một cách an toàn hình thành.
13.7.3.4 Bị ép buộc-độ trễ sự tối ưu hóa Khi độ trễ các SLO cung cấp ràng buộc sự ép buộc, sự tối ưu hóa bài toán trở thành việc tìm kiếm tối đa lô kích thước đáp ứng SLO. Cho một độ trễ mục tiêu 𝐿lat,target và trung bình sự chờ đợi thời gian 𝑇window/2, phương trình 13.12 định nghĩa tối đa có-thể-cho-phép (allowable) lô kích thước (việc) sử dụng một bậc-nhất (first-order) trung bình độ trễ sự xấp xỉ: 𝐵max = max{𝐵 ∶ 𝑇window / 2 + 𝑇svc(𝐵) ≤ 𝐿lat,target}
(13.12) Hãy xem xét một 50 ms p95 độ trễ SLO cho ResNet-50 việc phục vụ (việc sử dụng này dựa-trên-trung bình sự xấp xỉ như (là) một xuất phát điểm):): Việc so sánh một bảo thủ việc tạo lô cửa sổ đối nghịch một quyết liệt (aggressive) (cửa sổ) cô lập (isolates) cách cửa sổ sự lựa chọn đánh đổi sự chờ đợi thời gian, sự suy luận ngân sách, và thông lượng. Bảng 13.12 đặt hai các cấu hình cạnh nhau.
Bảng 13.12: Việc tạo lô cửa sổ sự đánh đổi: Cách một bảo thủ so với quyết liệt việc tạo lô cửa sổ đánh đổi trung bình sự chờ đợi, sự suy luận ngân sách, lô kích thước, và thông lượng tại cố định đến tỷ lệ.
Số liệu (Metric)
Bảo thủ (𝑇window = 5 ms)
Quyết liệt (𝑇window = 25 ms)
Trung bình sự chờ đợi
2.5 ms (tối đa đợi = 5 ms cho đầu tiên
yêu cầu trong một cửa sổ)
12.5 ms
Độ trễ ngân sách cho sự suy luận
47.5 ms (trung bình-độ trễ việc lập kế hoạch; đuôi các SLOs
nên lập ngân sách (cho) đầy cửa sổ)
37.5 ms
Lô kích thước mũ (cap)
32 các hình ảnh (điển hình lô ≈ 5.7)
48 (điển hình lô ≈ 32)
Được đạt được thông lượng
~1,140 hình ảnh/s
~1,280 hình ảnh/s Quyết liệt cửa sổ đạt được chỉ 12.3 phần trăm cao hơn thông lượng nhưng làm tăng trung bình độ trễ bởi 10 ms và p99 độ trễ bởi 20 ms. Kiểm tra bảng 13.11: cho nhạy cảm-độ trễ các ứng dụng, bảo thủ cửa sổ cung cấp tốt hơn người dùng trải nghiệm tại khiêm tốn thông lượng chi phí.

13. Mô hình Việc phục vụ

Liên tục Việc tạo lô:
Cũng được gọi (là) “cấp độ-vòng lặp việc tạo lô” (Yu và cộng sự 2022) và, trong NVIDIA TensorRT-LLM, “đang-bay (in-flight) việc tạo lô”.
Chính sự thấu hiểu là sự lập lịch độ chi tiết (granularity): truyền- thống (traditional) việc tạo lô cam kết (tới) một
cố định lô cho một toàn bộ tạo-
sinh chuỗi (tiềm năng hàng trăm các vòng lặp), trong khi
liên tục việc tạo lô lập lịch- lại (reschedules) tại mọi mã thông báo-sự tạo sinh (token-generation)
bước—tương tự (analogous) (với) sự ưu- tiên (preemp-tive) HĐH tiến trình sự lập lịch so với chạy-để-hoàn thành.
Này
mịn hơn (finer) độ chi tiết giảm thiểu sự lãng phí từ có thể thay đổi-chiều dài (variable-length) các chuỗi (se-
quences), nơi một lô khe cắm (slot) được chiếm đóng bởi một hoàn thành chuỗi ngồi nhàn rỗi cho đến khi tất cả (các chuỗi) khác các chuỗi kết thúc (finish).

vLLM (Ảo LLM (Virtual LLM)): Một
mã nguồn mở việc phục vụ hệ thống
thứ mà kích hoạt liên tục việc tạo- lô thông qua nó PagedAttention thuật- toán.
Được truyền cảm hứng bởi HĐH ảo bộ-
nhớ, kỹ thuật này giảm thiểu
nghiêm trọng KV-bộ nhớ đệm sự phân- mảnh (fragmen-tation) và sự đặt trước (reservation) sự lãng phí thứ mà ép buộc (constrains) tĩnh việc tạo lô. Bằng cách việc giữ KV-bộ nhớ đệm sự lãng phí
thấp, vLLM có thể phục vụ lớn hơn
hiệu quả các lô trên giống nhau phần cứng.
13.7.3.5 SLO sự vi phạm sự phân tích Lô kích thước tính biến đổi gây ra SLO các sự vi phạm thậm chí khi trung bình độ trễ dường như an toàn. p99 độ trễ bao gồm cả tồi tệ nhất-trường hợp sự chờ đợi thời gian (đầy cửa sổ) và tồi tệ nhất-trường hợp lô kích thước (chi phối bởi Poisson đuôi) and worst-case batch size). Phương trình 13.13 nắm bắt (captures) này mối quan hệ:
𝐿lat,p99 ≈ 𝑇window + 𝑇svc(𝐵p99)
(13.13) nơi 𝐵p99 là 99(th) phân vị lô kích thước (where 𝐵p99 is the 99th percentile batch size). Cho 𝜆arr = 500 QPS và 𝑇window = 10 ms, trung bình lô kích thước là 5 trong khi Poisson đuôi đẩy p99 lô kích thước tới 11. (Cái) đuôi đó lan truyền vào độ trễ: mức trung bình thêm 5 ms của sự chờ đợi (vào) 8 ms của dịch vụ cho 13 ms, trong khi đó (whereas) p99 thêm đầy cửa sổ của 10 ms (vào) 11.6 ms của dịch vụ cho 21.6 ms. p99 độ trễ là 1.66× mức trung bình, việc phản ánh cả sự chờ đợi thời gian phương sai và lô kích thước phương sai. Các hệ thống cung cấp (provision) (dựa) trên trung bình độ trễ sẽ trải nghiệm SLO các sự vi phạm. Các hệ thống Góc nhìn 13.7: Độ trễ-thông lượng sự đánh đổi Một đơn “sự suy luận tốc độ” con số là không được định nghĩa cho đến khi lô kích thước được đặt tên, bởi vì lô kích thước chọn chế độ nào, và nút thắt cổ chai nào, hệ thống hoạt động trong. • Lô-1 chế độ (Batch-1 regime): Bị giới hạn-độ trễ. Yêu cầu con đường thống trị bởi Python chi phí hoạt động và bộ nhớ băng thông, vì mỗi yêu cầu tải các trọng số cho một đơn đầu vào. Chế độ này chi phối thực-thời gian sự tương tác như là việc gõ phím (typing) các trình trợ giúp và rô bốt (robotics). • Lô-N chế độ (Batch-N regime): Bị giới hạn-thông lượng. Việc khấu hao trọng số tải qua một đầy lô dịch chuyển nút thắt cổ chai (sang) tính toán (FLOP/s)). Chế độ này chi phối ngoại tuyến (offline) việc xử lý và cao-lưu lượng truy cập các dịch vụ. Hai các chế độ tối ưu hóa đối nghịch (opposite) các số lượng (quantities), do đó một mô hình là “nhanh” tại lô 1 có thể (là) xa từ đỉnh thông lượng, và ngược lại. Bất kỳ độ trễ hay thông lượng số liệu (figure) phải do đó chỉ định liệu nó (đã) được đo lường tại đơn-luồng độ trễ (lô 1) hay tối đa thông lượng (lô N) (hay không) or maximum throughput (batch N)).
13.7.3.6 Thích ứng việc tạo lô các cửa sổ Giống nhau lô-kích thước sự phụ thuộc thúc đẩy cách việc phục vụ hệ thống định hình các lô của nó (ngay) trong đầu tiên nơi (ngay từ đầu). Cố định việc tạo lô các cửa sổ lãng phí độ trễ ngân sách trong suốt cao lưu lượng truy cập khi lớn các lô hình thành nhanh chóng. Danh sách 13.2 chứng minh cách thích ứng các chiến lược điều chỉnh cửa sổ dựa trên hàng đợi độ sâu.

13.7 Thông lượng Sự tối ưu hóa Danh sách 13.2: Thích ứng Việc tạo lô Cửa sổ: Động (Dynamically) điều chỉnh lô thời gian chờ dựa trên hàng đợi độ sâu và đến tỷ lệ, việc giảm thiểu trung bình độ trễ bởi 27 phần trăm so sánh với cố định các cửa sổ trong khi việc duy trì thông lượng.
```python
def adaptive_batching_window( queue_depth, arrival_rate, slo_ms, service_ms, fixed_overhead_ms
): """Tính toán tối ưu việc tạo lô cửa sổ. Dựa trên hiện tại hệ thống trạng thái.
""" target_batch_size = 16 # Tối ưu lô cho GPU sự sử dụng

# Nhanh con đường: lô (đã) sẵn sàng, đóng ngay lập tức để tối thiểu hóa độ trễ
if queue_depth >= target_batch_size:
return 0

# Tính toán tối đa có-thể-cho-phép đợi từ còn lại p99 ngân sách. max_wait_ms = max

# Ước tính thời gian để tích lũy (accumulate) mục tiêu lô tại hiện tại sự đến
# tỷ lệ.
# arrival_rate là các yêu cầu/giây, do đó chuyển đổi các giây thành
# phần nghìn giây.
if arrival_rate > 0: requests_needed = target_batch_size - queue_depth estimated_wait_ms = requests_needed / arrival_rate * 1000.0
# Trả về tối thiểu của ước tính đợi và ép buộc-SLO tối đa return min

return max_wait_ms # Thấp lưu lượng truy cập: sử dụng còn lại ngân sách để tích lũy lô
``` Cách tiếp cận này giảm thiểu trung bình sự chờ đợi thời gian trong suốt cao lưu lượng truy cập trong khi việc duy trì lô các kích thước. Cho lưu lượng truy cập thay đổi giữa 200–1000 QPS, một cố định 10 ms cửa sổ tạo ra 15 ms trung bình độ trễ tại 650 hình ảnh/s, trong khi một thích ứng cửa sổ cắt giảm trung bình độ trễ tới 11 ms (27 phần trăm sự giảm thiểu) và cải thiện thông lượng tới 680 hình ảnh/s (5 phần trăm sự cải thiện) (For traffic varying between 200–1000 QPS, a fixed 10 ms window produces 15 ms average latency at 650 img/s, while an adaptive window cuts average latency to 11 ms (27 percent reduction) and improves throughput to 680 img/s). Sự tương tác (interplay) giữa cửa sổ kích thước và lô các giới hạn tạo ra một không gian của có thể các cấu hình, mỗi (cấu hình) đại diện một khác biệt sự cân bằng giữa thông lượng và độ trễ. Việc tạo lô cấu hình không gian hình thành một Pareto biên giới nơi việc cải thiện thông lượng yêu cầu việc chấp nhận cao hơn độ trễ. Bảng 13.13 theo dấu này biên giới qua năm đại diện các cấu hình:
Bảng 13.13: Việc tạo lô Pareto Biên giới: Mỗi cấu hình đại diện một khác biệt điểm trên thông lượng-độ trễ sự đánh đổi đường cong. Việc di chuyển từ 2 ms tới 50 ms các cửa sổ cải thiện thông lượng bởi chỉ 52 phần trăm trong khi việc làm tăng p99 độ trễ bởi 5.4×. (Sự) giảm dần các lợi nhuận làm quyết liệt việc tạo lô (trở nên) đắt đỏ cho nhạy cảm-độ trễ các ứng dụng.
Cửa sổ (ms)
Tối đa Lô
Trung bình Độ trễ
p99 Độ trễ
Thông lượng
Cấu hình

8 ms
18 ms
890 hình ảnh/s
Siêu-thấp (Ultra-low) độ trễ

10 ms
22 ms
1,140 hình ảnh/s
Cân bằng

15 ms
35 ms
1,240 hình ảnh/s
Vừa phải độ trễ

23 ms
52 ms
1,310 hình ảnh/s
(Được) tối ưu hóa-thông lượng

38 ms
98 ms
1,350 hình ảnh/s
Tối đa thông lượng
13.7.3.7 Thực tế cấu hình các hướng dẫn (guidelines) Pareto biên giới trong bảng 13.13 minh họa tại sao những các hướng dẫn này quan trọng: đi qua (past) đầu gối, việc mở rộng cửa sổ mua giảm dần một cách dốc (steeply) thông lượng cho tăng lên một cách sắc bén đuôi độ trễ. Có nguyên tắc (Principled) việc tạo lô cấu hình tránh này khu vực của sự giảm dần các lợi nhuận bằng cách việc làm việc ngược từ độ trễ ngân sách. Việc cấp phát hai mươi tới 30 phần trăm của SLO (vào) việc tạo lô sự chờ đợi thời gian để lại phần còn lại cho sự suy luận và chi phí hoạt động, thứ mà giới hạn tối đa cửa sổ tại 𝑇max = 0.3 × 𝐿lat,SLO. Lưu lượng truy cập sự ước tính nạp (vào) (feeds) này sự tính toán nên sử dụng p95 đến tỷ lệ thay vì mức trung bình, bởi vì

việc tạo lô các cửa sổ điều chỉnh cho trung bình lưu lượng truy cập tạo ra quá khổ (oversized) lô trong suốt các sự tăng vọt—chính xác khi SLO khoảng không quan trọng (nhất) (batching windows tuned for average traffic produce oversized batches during spikes—precisely when SLO headroom matters most). GPU bộ nhớ áp đặt một cứng trần (ceiling) trên lô kích thước độc lập với độ trễ sự ép buộc, vì sự kích hoạt bộ nhớ mở rộng một cách tuyến tính với lô chiều. Cuối cùng, việc giám sát thực sự lô kích thước sự phân phối trong sản xuất tiết lộ liệu ban đầu lưu lượng truy cập các giả định tổ chức (hold) (hay không); cao phương sai báo hiệu (signals) rằng cửa sổ cần thích ứng sự điều chỉnh thay vì một cố định cấu hình. Cho ResNet-50 với 50 ms SLO và 500 QPS lưu lượng truy cập: Sự tính toán biến SLO và đến-tỷ lệ các giả định thành hai có-thể-triển-khai các núm (knobs): việc tạo lô cửa sổ và tối đa lô kích thước. Bảng 13.14 tóm tắt dẫn đến cấu hình và được dự đoán hoạt động điểm.
Bảng 13.14: Thực tế Việc tạo lô Cấu hình: Việc làm việc ngược từ một 50 ms SLO và 500 QPS lưu lượng truy cập sự ước tính mang lại một 12 ms việc tạo lô cửa sổ và lô-32 mũ. Được dự đoán p99 độ trễ duy trì bên trong SLO, trong khi lô mũ để lại khoảng không cho các đợt (bursts).
Số lượng
Giá trị
Kỹ thuật vai trò
Độ trễ ngân sách cho việc tạo lô
15 ms Phần của SLO sẵn sàng cho việc xếp hàng đợi sự chậm trễ.
Tối đa cửa sổ
15 ms Trên (upper) ranh giới (bound) ngụ ý (implied) bởi độ trễ ngân sách.
Được mong đợi lô kích thước

Trung bình lô dưới được tuyên bố (stated) lưu lượng truy cập.
p99 lô kích thước

Đợt kích thước dưới Poisson các sự đến.
Bị giới hạn-bởi-bộ-nhớ tối đa lô

Cứng mũ áp đặt bởi máy gia tốc bộ nhớ.
Được chọn cấu hình
𝑇window = 12 ms, 𝐵max = 32 Thực tế núm thiết lập (setting) cho sự triển khai.
Được dự đoán p99 độ trễ
24.2 ms
Xác nhận rằng cấu hình ở lại bên trong SLO.
Được dự đoán đỉnh công suất
1,176.9 hình ảnh/s Công suất nếu được chọn lô mũ bão hòa.
Được phục vụ thông lượng
500 hình ảnh/s Bị giới hạn-bởi-sự-đến tải xử lý bởi cấu hình.
13.7.4 Liên tục việc tạo lô Tự hồi quy (Autoregressive) các mô hình như ngôn ngữ các mô hình tạo sinh các đầu ra mã thông báo bởi mã thông báo—mỗi mới mã thông báo phụ thuộc vào tất cả trước đó được tạo sinh các mã thông báo, do đó sự tạo sinh là (về mặt) vốn có (inherently) tuần tự. (Cái) động việc tạo lô được kiểm tra trong phần 13.7 giả định cố định-chiều dài các đầu ra. Các LLM vi phạm giả định này: nếu một chuỗi trong một lô của tám kết thúc (finishes) sau mười các mã thông báo trong khi (các chuỗi) khác cần 100 các mã thông báo, 90 phần trăm của tính toán cho đó chuỗi khe cắm là bị lãng phí (Yu và cộng sự 2022)). Liên tục việc tạo lô21 (cũng được gọi (là) cấp độ-vòng lặp việc tạo lô) giải quyết này sự lãng phí bằng cách việc cho phép mới các yêu cầu (để) tham gia (join) một lô giữa sự tạo sinh các bước và được hoàn thành chuỗi (để) thoát (exit) (Yu và cộng sự 2022; Kwon và cộng sự 2023) addresses this waste by allowing new requests to join a batch between generation steps and completed sequences to exit). Hệ thống quản lý lô thành phần động tại mỗi việc giải mã (decoding) vòng lặp thay vì việc hình thành tĩnh các lô tồn tại (persist) cho toàn bộ tạo sinh quá trình. Cơ chế làm việc như sau: khi một chuỗi tạo sinh nó kết thúc-của-chuỗi (end-of-sequence) mã thông báo, nó khe cắm trở nên ngay lập tức sẵn sàng. Một chờ đợi yêu cầu có thể lấp đầy đó khe cắm cho tiếp theo vòng lặp thay vì việc chờ đợi cho toàn bộ lô (để) hoàn thành. (Một cách) tương tự (Similarly), hệ thống có thể thêm mới các yêu cầu (vào) sẵn sàng các khe cắm mà không có việc ngắt quãng (interrupting) diễn ra (ongoing) sự tạo sinh. Này động cách tiếp cận duy trì cao GPU sự sử dụng thậm chí khi chuỗi các chiều dài thay đổi bởi 100× hay hơn. Các hệ thống triển khai liên tục việc tạo lô, như là vLLM22 và TensorRT-LLM, cải thiện thông lượng bằng cách việc giữ giải mã các khe cắm chiếm đóng (occupied) khi các chuỗi đi vào và đi ra (Kwon và cộng sự 2023; NVIDIA 2026g)). Sarathi-Serve tinh chỉnh (refines) này bộ lập lịch với phân đoạn (chunked) việc điền trước (prefill) và không-đình-trệ (stall-free) việc tạo lô để giảm thiểu sự can thiệp (interference) giữa dấu nhắc (prompt) việc xử lý và mã thông báo việc giải mã (Agrawal và cộng sự 2024)). Sự cải- thiện đến từ hai các nguồn: việc giảm thiểu lãng phí tính toán trên được hoàn thành chuỗi và việc giảm thiểu trung bình sự chờ đợi thời gian cho mới các yêu cầu. Cho sản xuất ngôn ngữ mô hình việc phục vụ nơi phản hồi các chiều dài thay đổi từ đơn các mã thông báo tới hàng ngàn, liên tục việc tạo lô đã (trở thành) một trung tâm (central) kỹ thuật cho hiệu quả-chi phí (cost-effective) sự triển khai. Bộ nhớ sự quản lý thêm tính phức tạp (vào) liên tục việc tạo lô. Khi các chuỗi đi vào và đi ra lô, khóa-giá trị (key-value) bộ nhớ đệm lưu trữ sự chú ý (attention) ngữ cảnh phải một cách động cấp phát và giải phóng (freed). (Hãy) xem xét gì xảy ra khi các chuỗi của thay đổi các chiều dài chia sẻ GPU bộ nhớ: một 100-mã thông báo chuỗi hoàn thành và giải phóng (releases) nó bộ nhớ đệm, nhưng một mới 150-mã thông báo chuỗi không thể sử dụng đó không gian bởi vì nó cần một lớn hơn liền kề (contiguous) khối. Qua thời gian, nhỏ không thể sử dụng (unusable) các khoảng trống (gaps) tích lũy giữa

13. Mô hình Việc phục vụ (Model Serving)

13.7 Thông lượng Sự tối ưu hóa
PagedAttention thu hồi (recovers) KV- bộ nhớ đệm sự lãng phí của liền kề sự cấp- phát.

PagedAttention:
(Cái) tên một cách trực tiếp tham chiếu (tới) HĐH ảo bộ nhớ việc phân trang (paging), lần đầu tiên
được triển khai trên Atlas
máy tính
tại
Manchester
(1962)
để
giải quyết
giống nhau
lớp của sự cấp phát bài toán—
các chương trình
đã cần
nhiều (hơn)
bộ nhớ
hơn
về mặt vật lý có sẵn,
và
liền kề
sự cấp phát
đã lãng phí không gian. Được giới thiệu tại SOSP 2023,
PagedAttention áp dụng này
sáu-thập kỷ-tuổi (six-decade-old)
sự trừu tượng (abstraction)
cho GPU KV-bộ nhớ đệm bộ nhớ:
trước nó,
LLM
việc phục vụ các hệ thống đã lãng phí 60–80 phần trăm
của KV bộ nhớ đệm bộ nhớ do (bởi)
tới sự phân mảnh và quá mức- sự đặt trước (over-reservation). PagedAttention
giảm thiểu
sự lãng phí
tới
dưới 4 phần trăm,
việc kích hoạt 2–4× cao hơn thông lượng trên giống nhau phần cứng. được cấp phát các khu vực (regions), cuối cùng việc ngăn chặn mới các chuỗi khỏi việc bắt đầu thậm chí khi tổng trống bộ nhớ dường như đủ. Này bộ nhớ sự phân mảnh có thể lãng phí 40 tới 50 phần trăm của sẵn sàng bộ nhớ trong ngây thơ (naive) các sự triển khai, nghiêm trọng việc giới hạn đồng thời lô kích thước quyết định thông lượng.
13.7.4.1 PagedAttention PagedAttention,23 được giới thiệu trong vLLM, giải quyết này sự phân mảnh bài toán bằng cách việc áp dụng hoạt động hệ thống ảo bộ nhớ các khái niệm cho GPU bộ nhớ (Kwon và cộng sự 2023)). Thay vì việc cấp phát một liền kề khối (cho) mỗi chuỗi, PagedAttention chia KV bộ nhớ đệm thành cố định-kích thước các trang (điển hình 16 các mã thông báo (cho) mỗi (trang))). Một chuỗi’s bộ nhớ đệm bao gồm các con trỏ tới không liền kề các trang rải rác (scattered) qua GPU bộ nhớ. Khi một chuỗi hoàn thành, nó các trang quay trở lại một trống danh sách và có thể được tái sử dụng bởi bất kỳ mới chuỗi , bất kể của chiều dài. vLLM báo cáo rằng này việc phân trang cách tiếp cận giảm thiểu KV-bộ nhớ đệm sự lãng phí tới dưới 4 phần trăm trong khi việc cải thiện thông lượng tương đối (so với) trước đó liền kề-sự cấp phát các thiết kế. (Cái) chi phí hoạt động là một trang-bảng (page-table) tra cứu (lookup) trong suốt sự chú ý tính toán, việc làm PagedAttention (trở thành) một tiêu chuẩn tham chiếu điểm cho sản xuất LLM việc phục vụ. Việc tạo lô và bộ nhớ các kỹ thuật được bao phủ (covered) ở đây thiết lập nền tảng cho LLM việc phục vụ, nhưng một vài nâng cao (advanced) các chủ đề (topics) đảm bảo (warrant) bổ sung nghiên cứu. Các hệ thống Góc nhìn 13.8: LLM việc phục vụ: Vượt ra ngoài nguyên tắc cơ bản (fundamentals) Ngôn ngữ mô hình việc phục vụ giới thiệu các thách thức vượt ra ngoài việc tạo lô và bộ nhớ các nguyên tắc (principles) được thiết lập ở đây. Khóa-giá trị bộ nhớ đệm lưu trữ sự chú ý ngữ cảnh mở rộng với chuỗi chiều dài và lô kích thước, thường (việc) vượt quá (chính) mô hình các trọng số trong bộ nhớ sự tiêu thụ. Các kỹ- thuật như là suy đoán (speculative) việc giải mã sử dụng nhỏ nháp (draft) các mô hình để đề xuất nhiều các mã thông báo mục tiêu mô hình xác minh trong song song, việc đạt được 2–3× độ trễ sự giảm thiểu cho tương tác các ứng dụng (Leviathan và cộng sự 2023) (Techniques like speculative decoding use small draft models to propose multiple tokens that the target model verifies in parallel, achieving 2–3× latency reduction for interactive applications (Leviathan et al. 2023)). Chỉ-trọng số sự lượng tử hóa (như là INT4 các trọng số với FP16 các sự kích hoạt) là đặc biệt (especially) có liên quan cho bị giới hạn-bởi-bộ nhớ-băng thông LLM sự suy luận (Lin và cộng sự 2023) is especially relevant for memory-bandwidth-bound LLM inference (Lin et al. 2023)). Những đặc thù-LLM (LLM-specific) các sự tối ưu hóa này xây dựng một cách trực tiếp trên các nền tảng (thứ mà) chương này thiết lập: việc xếp hàng đợi lý thuyết chi phối yêu cầu sự lập lịch, việc tạo lô các sự đánh đổi quyết định thông lượng-độ trễ các đường cong, và độ chính xác sự lựa chọn tuân theo giống nhau độ chính xác-tính hiệu quả các nguyên tắc. (Các) việc phục- vụ các nguyên tắc cơ bản áp dụng phổ quát (universally); LLM việc phục vụ thêm đặc thù-miền các kỹ thuật (lên) trên (atop) này nền tảng. Nâng cao các sự xử lý (treatments) cung cấp chi tiết độ bao phủ của KV bộ nhớ đệm sự tối ưu hóa, việc bao- gồm các kỹ thuật cho nhiều-người thuê (multi-tenant) việc phục vụ, nơi một hạm đội (fleet) chia sẻ công suất qua những người dùng, và phân tán (distributed) sự suy luận, nơi một yêu cầu có thể bị chia (tách) qua các máy. Liên tục việc tạo lô là thống trị kỹ thuật cho LLM việc phục vụ, (nhưng) tuy nhiên (yet) không (phải) tất cả sự triển khai các kịch bản hưởng lợi từ việc tạo lô. Tinh vi (sophisticated) các kỹ thuật được kiểm tra cho đến nay (từ động việc tạo lô các cửa sổ tới PagedAttention) tối ưu hóa cho cao-thông lượng máy chủ (server) các khối lượng công việc optimize for high-throughput server workloads). Những kỹ thuật này giới thiệu tính phức tạp và độ trễ chi phí hoạt động có thể không được biện minh (justified) cho tất cả sự triển khai các ngữ cảnh. Thực tế câu hỏi là khi việc tạo lô làm tổn thương thay vì giúp ích. Một số các kịch bản yêu cầu đơn-yêu cầu việc xử lý. Siêu-thấp độ trễ các yêu cầu, nơi p99 độ trễ phải ở (dưới) 10 ms, làm (cho) bất kỳ việc tạo lô sự chậm trễ (trở nên) không thể chấp nhận. (Một cách) cao độ có thể thay đổi yêu cầu các kích thước tạo ra việc đệm (padding) chi phí hoạt động lãng phí tính toán, vì nhỏ nhất đầu vào trong một lô phải được đệm để khớp (với) lớn nhất. Bộ nhớ các sự ép buộc cũng trở thành ràng buộc khi các mô hình đã tiêu thụ hầu hết GPU bộ nhớ, vì lô các sự kích hoạt mở rộng tuyến tính với lô kích thước và có thể kích hoạt hết-bộ-nhớ (out-of-memory) các lỗi.
13.7.5 Phiên (Session) sự thân thiết (affinity) các sự ép buộc Khi các yêu cầu từ giống nhau người dùng hay phiên nên định tuyến tới giống nhau bản sao, việc tạo lô trở nên bị ép buộc. Phiên sự thân thiết, cũng được gọi (là) dính (sticky) các phiên, quan trọng (matters) vì ba chính (main) các lý do. Có tác động nhất (impactful) trường hợp là KV-bộ nhớ đệm sự tái sử dụng trong hội thoại AI, nơi khóa-giá trị bộ nhớ đệm từ trước đó các lượt (turns) có thể vật chất (materially) tăng tốc nhiều-lượt các cuộc hội thoại. Việc định tuyến một tiếp theo (follow-up) yêu cầu tới một khác biệt bản sao bị tước bỏ (forfeits) này được lưu trong bộ nhớ đệm ngữ cảnh, việc ép buộc hệ thống (để) tính toán lại hay tải lại tiền tố trạng thái cho dài các cuộc hội thoại. Một thứ hai trình điều khiển (driver) là đặc thù-người dùng (user-specific) các mô hình: một số hệ thống phục vụ được cá nhân hóa các mô hình hay các bộ tiếp hợp (adapters) cho mỗi người dùng, và việc định tuyến các yêu cầu tới bản sao đã tải đó người dùng’s bộ tiếp hợp tránh

13. Mô hình Việc phục vụ (Model Serving)

Poisson Tiến trình (Process): Được đặt tên
sau Pháp nhà toán học
Simeon
Denis
Poisson
(1781–1840), này ngẫu nhiên
mô hình
mô tả
các sự kiện
xảy ra liên tục và
độc lập tại một hằng số
trung bình tỷ lệ. Chính thuộc-
tính (property) cho việc phục vụ:
phương sai
bằng mức trung bình, do đó lô
các kích thước dao động đáng kể
tại
vừa phải
lưu lượng truy cập—với
𝜆arr = 200 yêu cầu/s và một 10
ms cửa sổ, được mong đợi lô
kích thước là hai nhưng xấp xỉ 14
phần trăm của các cửa sổ sẽ là trống (bị lãng phí GPU các chu kỳ). Này phương sai là lý do tại sao việc tạo lô
các cửa sổ
phải
được
điều chỉnh
theo xác suất thay vì thiết lập từ trung bình lưu lượng truy cập một mình (nó). Khi QPS tăng lên (rises), việc tạo lô cửa- sổ co lại (shrinks) trong khi lô kích thước phát triển. lặp lại việc tải chi phí hoạt động. (Một cách) tương tự, có trạng thái (stateful) việc tiền xử lý duy trì trình mã thông báo (tokenizer) các bộ nhớ đệm hay đặc thù-phiên sự chuẩn hóa (normalization) yêu cầu việc xây dựng lại trạng thái khi các yêu cầu định tuyến tới một khác biệt bản sao. Sự căng thẳng với việc tạo lô là rõ ràng vì nghiêm ngặt (strict) sự thân thiết ép buộc yêu cầu nào có thể được tạo lô cùng nhau, có khả năng (potentially) việc giảm thiểu lô các kích thước và GPU sự sử dụng. Sản xuất các hệ thống thường triển khai mềm sự thân thiết nơi các yêu cầu thích (prefer) của chúng được chỉ định bản sao nhưng có thể tràn (overflow) (sang) những (bản sao) khác khi đó bản sao bị quá tải. Điều này bảo tồn hầu hết sự thân thiết các lợi ích trong khi việc duy trì tải sự cân bằng.
13.7.6 Lưu lượng truy cập các mẫu và việc tạo lô chiến lược Tối ưu việc tạo lô chiến lược phụ thuộc tới hạn (critically) vào (cách) các yêu cầu đến. Khác biệt sự triển khai các ngữ cảnh thể hiện (exhibit) khác biệt (distinct) đến các mẫu, mỗi (ngữ cảnh) (việc) yêu cầu khác biệt việc tạo lô các cách tiếp cận. MLPerf sự suy luận điểm chuẩn mã hóa (codifies) những các mẫu này thành bốn các kịch bản trực tiếp ánh xạ tới thế giới-thực các sự triển khai, như phần 12.8.4.2 giải thích (trong) chi tiết.
13.7.6.1 Máy chủ lưu lượng truy cập (poisson các sự đến) MLPerf Máy chủ kịch bản mô hình hóa đám mây/như-API sự suy luận lưu lượng truy cập với Poisson các sự đến (Reddi và cộng sự 2019)).24 Dưới đó mô hình, các sự đến là độc lập và đồng đều phân phối qua thời gian. Phương trình 13.14 biểu diễn (expresses) được mong đợi lô kích thước cho Poisson các sự đến với tỷ lệ 𝜆arr và việc tạo lô cửa sổ 𝑇window (Equation 13.14 expresses the expected batch size for Poisson arrivals with rate 𝜆arr and batching window 𝑇window:):
𝐸[lô kích thước] = 𝜆arr ⋅ 𝑇window
(13.14) Phương sai bằng mức trung bình (một thuộc tính của Poisson các sự phân phối), do đó lô các kích thước dao động một cách đáng kể tại vừa phải lưu lượng truy cập, so batch sizes fluctuate significantly at moderate traffic). Với 𝜆arr = 200 các yêu cầu/giây và 𝑇window = 10 ms, mong đợi lô kích thước là hai, nhưng xấp xỉ 14 phần trăm của các cửa sổ sẽ có không các yêu cầu (bị lãng phí tính toán các chu kỳ) trong khi những (cửa sổ) khác có thể có bốn hay nhiều hơn (With 𝜆arr = 200 requests/second and 𝑇window = 10 ms, expected batch size is two, but roughly 14 percent of windows will have zero requests (wasted compute cycles) while others may have four or more). Một hữu ích (mang tính) khám phá (heuristic) cho việc tạo lô cửa sổ cân bằng việc chờ đợi chi phí đối nghịch thông lượng lợi ích. Phương trình 13.15 biểu diễn một như vậy quy tắc: 𝑇window ≈ min(𝐿lat,SLO − 𝑇svc, √ ( 𝑇svc / 𝜆arr ))
(13.15) nơi 𝐿lat,SLO là độ trễ SLO, 𝑇svc là dịch vụ thời gian (tính bằng giây), và 𝜆arr là đến tỷ lệ (tính bằng các yêu cầu mỗi giây), việc làm thứ hai thuật ngữ nhất quán về mặt thứ nguyên trong các giây (where 𝐿lat,SLO is the latency SLO, 𝑇svc is the service time (in seconds), and 𝜆arr is the arrival rate, making the second term dimensionally consistent in seconds). Căn-bậc hai (square-root) hình thức là một cục bộ chi phí-mô hình (mang tính) khám phá: nó cân bằng một cố định mỗi-lô lợi ích đối nghịch một sự chờ đợi chi phí thứ mà phát triển với đến khoảng (interval). Nó không (phải) (là) một đóng-hình thức (closed-form) mức tối ưu (optimum) cho ML việc phục vụ đặc thù; sản xuất các hệ thống hiệu chuẩn (calibrate) cửa sổ theo kinh nghiệm (empirically) đối nghịch quan sát lưu lượng truy cập. Một ngược lại trực giác (counterintuitive) kết quả xuất hiện (emerges) từ phương trình này: khi lưu lượng truy cập tăng lên, tối ưu cửa sổ giảm thiểu trong khi đạt được lô các kích thước vẫn phát triển. Bảng 13.15 chứng minh này hiện tượng qua bốn lưu lượng truy cập các cấp độ.
Bảng 13.15: Thích ứng-Lưu lượng truy cập Việc tạo lô: Cao hơn lưu lượng truy cập kích hoạt ngắn hơn các cửa sổ trong khi vẫn việc đạt được lớn hơn trung bình các lô. Các giá trị được tính toán từ phương trình 13.15 với một 50 ms SLO và một 25 ms dịch vụ-thời gian giả định, do đó độ trễ cột là xấp xỉ dịch vụ-cộng-cửa sổ ngân sách thay vì một đo lường sản xuất p99.
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

30 ms
5,000 QPS
2.24 ms
11.2
27.2 ms
13.7.6.2 Việc truyền phát (Streaming) lưu lượng truy cập (có tương quan các sự đến) Tự trị (Autonomous) các phương tiện, video sự phân tích (analytics), và rô bốt (robotics) các hệ thống nhận các đầu vào từ nhiều đồng bộ- hóa (synchro-nized) các cảm biến. Một sáu-máy ảnh dòng thời gian (timeline) làm (cho) sự đồng bộ hóa hạn chót (deadline) (trở nên) cụ thể (concrete). Bảng 13.16 theo dấu mỗi-sự kiện dòng thời gian cho một được đồng bộ hóa khung (frame) tập hợp trên một phương tiện với sáu các máy ảnh chụp (capturing) tại 30 FPS và việc yêu cầu không gian (spatial) sự hợp nhất (fusion).

13.7 Thông lượng Sự tối ưu hóa
Bảng 13.16: Nhiều-máy ảnh khung dòng thời gian: Mỗi-sự kiện dòng thời gian cho một đồng bộ hóa khung tập hợp qua sáu các máy ảnh tại 30 FPS. Ví dụ cho thấy một 7 ms sự đến sự lây lan (spread) giữa đầu tiên và cuối cùng máy ảnh khung, trong khi hệ thống dành riêng (reserves) 12 ms của 33 ms cứng hạn chót như (là) sự chập chờn (jitter) sự khoan dung (tolerance) trước khi lô sự suy luận phải bắt đầu.
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
Sự suy luận hoàn thành
𝑇 = 32 ms Kết quả (đã) sẵn sàng cho việc lập kế hoạch mô-đun Ví dụ 13.3: Nhiều-máy ảnh tự trị phương tiện việc phục vụ Dòng thời gian trong bảng 13.16 cố định việc phục vụ bài toán thông qua một tập hợp của cứng các sự ép buộc thay vì thống kê đến các tỷ lệ chi phối Poisson lưu lượng truy cập: • Cứng hạn chót: 33 ms (cho) mỗi khung tập hợp (thực-thời gian yêu cầu) • Lô kích thước: (Được) cố định tại sáu (một (cho) mỗi máy ảnh) • Sự đồng bộ hóa ngân sách: 12 ms của 33 ms tổng (36 phần trăm cho sự chập chờn sự khoan dung) • Hết thời gian chờ (Timeout) chính sách (policy): Nếu máy ảnh khung không nhận bởi 𝑇+20 ms, sử dụng trước đó khung Các hệ thống sự thấu hiểu: Không giống như Poisson lưu lượng truy cập nơi động việc tạo lô tối ưu hóa thông lượng, việc truyền phát lưu lượng truy cập cố định cả lô kích thước và hạn chót bên ngoài, do đó việc phục vụ hệ thống phải tiêu (tiền) nó ngân sách trên sự đồng bộ hóa các chính sách xử lý cảm biến sự chập chờn trong khi vẫn việc đáp ứng cứng hạn chót.
13.7.6.3 Đơn-người dùng lưu lượng truy cập (tuần tự các sự đến) Việc truyền phát lưu lượng truy cập tương quan các sự đến bởi cảm biến sự đồng bộ hóa, việc làm lô kích thước và hạn chót bên ngoài cố định. Tại đối nghịch (opposite) cuối (end) của quang phổ (spectrum), di động và nhúng các ứng dụng đối mặt không việc tạo lô cơ hội (tại tất cả). Sự tối ưu hóa mục tiêu dịch chuyển từ sự đồng bộ hóa ngân sách đối nghịch một cứng khung hạn chót (sang) mỗi-yêu cầu độ trễ đối nghịch năng lượng sự tiêu thụ dưới một nhiệt công suất phong bì (envelope). Di động và nhúng các ứng dụng phục vụ một người dùng tại một thời điểm; MLPerf SingleStream (Đơn Luồng) kịch bản nắm bắt này tuần tự-việc phục vụ hình dạng. Cho ResNet-50 trên một điện thoại, thống trị các chi phí dịch chuyển từ lô sự hình thành (sang) mỗi-yêu cầu độ trễ và năng lượng. Khăn ăn Toán học 13.8: ResNet-50: Di động việc phục vụ
Bảng 13.17 phân rã mỗi-giai đoạn (phase) độ trễ và năng lượng cho một đơn-người dùng di động thị giác sự suy luận:
Bảng 13.17: Di động ResNet-50 đường ống: Mỗi-giai đoạn độ trễ và năng lượng cho một đơn-người dùng di động thị giác sự suy luận, việc cho thấy rằng JPEG giải mã trên CPU thống trị năng lượng ngân sách mặc dù (even though) NPU sự suy luận giai đoạn (stage) mang (carries) mô hình’s tính toán. Sự tối ưu hóa các mục tiêu dịch chuyển từ thông lượng (sang) năng lượng-mỗi-sự suy luận tại (rìa) cạnh (edge).
Giai đoạn
Khoảng thời gian (Duration)
Năng lượng
Các ghi chú
Máy ảnh bộ đệm đọc
8 ms
0.08 mJ
Hệ thống API
JPEG giải mã (CPU)
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
Kết quả kết xuất (rendering)
Tổng
45 ms
2.98 mJ
22 FPS duy trì

13. Mô hình Việc phục vụ

Di động việc phục vụ nút (node) được chi phối bởi bốn các số liệu: • Năng lượng cho mỗi sự suy luận: 2.98 mJ kích hoạt ~12.1M các sự suy luận (cho) mỗi 10 Wh pin (điển hình điện thoại thông minh)) • Nhiệt ngân sách: Tại 2.98 mJ / 45 ms = 66 mW duy trì, vô thời hạn (indefinite) hoạt động mà không có sự điều chỉnh (throttling) • NPU so với CPU sự đánh đổi: CPU dự phòng (fallback) thay thế 12 ms, 0.8 mJ NPU sự suy luận giai đoạn với một 45 ms, 4.2 mJ CPU giai đoạn; đầy đường ống sẽ tăng từ 45 ms và 2.98 mJ tới khoảng 78 ms và 6.4 mJ trước (khi) bổ sung hệ thống chi phí hoạt động. • Bộ nhớ dấu chân (footprint): 150 MB đỉnh (mô hình + các sự kích hoạt), (việc) cạnh tranh với ứng dụng bộ nhớ, competing with app memory) Các hệ thống sự thấu hiểu: Thậm chí tại lô kích thước một, di động NPU đạt được 82 phần trăm sự sử dụng bởi vì nó tính toán công suất khớp (với) đơn-hình ảnh các khối lượng công việc. Điều này khác biệt (so) với trung tâm dữ liệu các GPU, thứ mà đạt được chỉ 15 phần trăm sự sử dụng tại lô kích thước một bởi vì của chúng đồ sộ (massive) tính song song yêu cầu lớn hơn các lô để bão hòa.
13.7.6.4 Di động việc phục vụ các sự ép buộc Không giống như đám mây việc phục vụ nơi chi phí thống trị, di động việc phục vụ đối mặt ba có liên quan các sự ép buộc định hình sự tối ưu hóa chiến lược. (Cái) đầu tiên là một năng lượng ngân sách thông lượng các mục tiêu bỏ qua, bởi vì mỗi sự suy luận làm cạn kiệt (depletes) pin. Trong mô hình hóa đường ống, 2.98 mJ tại 22 FPS rút (draws) khoảng 66 mW cho sự suy luận con đường một mình (nó), trước (khi) máy ảnh, màn hình hiển thị (display), ISP, và HĐH chi phí hoạt động thêm vào đó tổng trong một đầy ảnh ứng dụng, do đó sự tối ưu hóa mục tiêu dịch chuyển từ thông lượng (sang) năng lượng-mỗi-sự suy luận. Nhiệt sự điều chỉnh (throttling) kép (compounds) (làm trầm trọng) này giới hạn, vì duy trì cao-công suất hoạt động kích hoạt nhiệt sự quản lý: một khi SoC đạt tới nó nhiệt trần (điển hình 45 °C tiếp giáp (junction)), HĐH giảm thiểu NPU tần số bởi 30–50 phần trăm, (việc) làm suy giảm (degrading) cả độ trễ và thông lượng, là lý do tại sao bùng nổ (bursty) các khối lượng công việc cho phép sự làm mát giữa các đợt vượt trội (outperform) (so với) duy trì tối đa thông lượng (Thermal throttling compounds this limit, since sustained high-power operation triggers thermal management: once the SoC reaches its thermal ceiling (typically 45 °C junction), the OS reduces NPU frequency by 30–50 percent, degrading both latency and throughput, which is why bursty workloads that allow cooling between bursts outperform sustained maximum throughput). Bộ nhớ các sự ép buộc đóng (lại) tập hợp (lại), bởi vì di động các thiết bị chia sẻ giới hạn RAM qua các ứng dụng. Một mô hình tiêu thụ 500 MB có thể bị trục xuất (evicted) trong suốt nền (background) hoạt động, (việc) ép buộc một sự tải lại (lạnh sự khởi động) thêm 200–500 ms của độ trễ, và thậm chí một 150 MB dấu chân trở nên có vấn đề khi mô hình phải cùng tồn tại (coexist) với khác ứng dụng các thành phần that adds 200–500 ms of latency, and even a 150 MB footprint becomes problematic when the model must coexist with other app components). Hiệu quả-bộ nhớ sự lượng tử hóa cải thiện người dùng trải nghiệm thông qua nhanh hơn mô hình sự khôi phục, và được ánh xạ-bộ nhớ mô hình việc tải (phần 13.6.3) giúp ích hơn nữa (further) bằng cách việc tải các trang trên sự yêu cầu (demand) thay vì việc yêu cầu đầy mô hình trong bộ nhớ helps further by loading pages on demand rather than requiring the full model in memory). Những các sự ép buộc này làm (cho) di động việc phục vụ sự tối ưu hóa (về mặt) định tính (qualitatively) khác biệt (so) với đám mây sự tối ưu- hóa. Mục tiêu không (phải) (là) tối đa thông lượng nhưng (là) có-thể-duy-trì (sustainable) hiệu suất, việc duy trì (có thể) chấp nhận độ trễ mà không có nhiệt sự điều chỉnh hay quá mức pin rút (cạn).
13.7.6.5 Lưu lượng truy cập mẫu bản tóm tắt Thích ứng-lưu lượng truy cập việc tạo lô điều chỉnh việc tạo lô cửa sổ khi hàng đợi độ sâu và yêu cầu tỷ lệ thay đổi.
Bảng 13.18 ánh xạ bốn MLPerf các kịch bản tới của chúng sự triển khai các ngữ cảnh và tối ưu việc tạo lô các chiến lược, việc cung cấp một quyết định khuôn khổ cho việc phục vụ hệ thống thiết kế.
Bảng 13.18: Lưu lượng truy cập Các mẫu và Việc tạo lô Các chiến lược: Bốn MLPerf sự suy luận các kịch bản ánh xạ tới khác biệt sự triển khai các ngữ cảnh. Máy chủ lưu lượng truy cập (đám mây các API) sử dụng động việc tạo lô với thời gian chờ; MultiStream (tự trị việc lái xe) sử dụng đồng bộ hóa cảm biến sự hợp nhất; SingleStream (di động) xử lý các yêu cầu cá nhân; Ngoại tuyến (lô việc xử lý) tối đa hóa lô kích thước cho thông lượng uses dynamic batching with timeout; MultiStream uses synchronized sensor fusion; SingleStream (mobile) processes requests individually; Offline maximizes batch size for throughput).
Kịch bản
Ngữ cảnh
Chiến lược
Trọng tâm (Focus)
Máy chủ
Đám mây các API, web các dịch vụ
Động việc tạo lô với thời gian chờ Cửa sổ sự điều chỉnh,
sự sử dụng-độ trễ đường cong
MultiStream (Đa luồng)
Tự trị việc lái xe, video
sự phân tích
(Được) đồng bộ hóa cảm biến sự hợp nhất
Sự chập chờn (việc) xử lý, hạn chót
các sự đảm bảo (guarantees)
SingleStream (Đơn luồng) Di động các ứng dụng, nhúng các thiết bị
Không việc tạo lô (𝐵 = 1) Việc tiền xử lý, công suất tính hiệu quả
Ngoại tuyến
Lô việc xử lý, dữ liệu các đường ống
Tối đa lô kích thước
Thông lượng, phần cứng
sự sử dụng MLPerf Máy chủ kịch bản nắm bắt đám mây API lưu lượng truy cập, MultiStream nắm bắt đồng bộ hóa cảm biến các khối lượng công việc, và Ngoại tuyến sự suy luận nắm bắt lô việc xử lý nơi thông lượng thống trị độ trễ.

13.8 LLM Việc phục vụ (LLM Serving)

Tự hồi quy (Autoregressive): Từ Hy Lạp (Greek) auto- (tự) và Latinh (Latin) regressus (một sự quay trở lại)—đầu ra “hồi quy” (regresses) trên chính nó.
George Udny Yule đã giới thiệu
tự hồi quy các mô hình trong 1927 cho việc phân tích vết đen mặt trời (sunspot) các chu kỳ.
Trong ngôn ngữ việc mô hình hóa, mỗi đầu ra mã thông báo điều kiện (conditions) trên tất cả trước đó được tạo sinh các mã thông báo (to-kens), việc tạo ra một nối tiếp (serial) sự phụ thuộc
(depen-dency) ngăn chặn tính song- song khai thác (exploited) trong suốt sự đào- tạo (train-ing).
Này nối tiếp nút thắt cổ chai
giải thích tại sao LLM việc phục vụ
là bị giới hạn-bởi-bộ nhớ-băng thông
thay vì bị giới hạn-bởi-tính toán:
mô hình các trọng số phải được
đọc từ bộ nhớ một lần (cho) mỗi
mã thông báo, bất kể sẵn sàng tính toán công suất.
TTFT và TPOT sống trong khác biệt nút thắt cổ chai các chế độ. Điểm kiểm tra (Checkpoint) 13.3: Việc tạo lô và lưu lượng truy cập các mẫu Việc tạo lô là chính đòn bẩy cho việc phục vụ tính kinh tế, nhưng tối ưu chiến lược phụ thuộc vào ngữ cảnh. □ Thông lượng-độ trễ sự đánh đổi: Bạn có thể giải thích tại sao lô kích thước 32 đạt được 6× cao hơn thông lượng (so với) lô kích thước một, (nhưng) tuy nhiên (yet) một sản xuất hệ thống với một 20 ms SLO có thể vẫn chọn lô kích thước tám (hay không)? (Throughput-latency trade-off: Can you explain why batch size 32 achieves 6× higher throughput than batch size one, yet a production system with a 20 ms SLO might still choose batch size eight?) □ Động so với tĩnh việc tạo lô: Bạn có thể mô tả tại sao tĩnh việc tạo lô (việc chờ đợi cho một đầy lô) thất bại dưới có thể thay đổi lưu lượng truy cập, và cách động việc tạo lô với một thời gian cửa sổ giải quyết điều này (hay không)? fails under variable traffic, and how dynamic batching with a time window solves this?) □ Lưu lượng truy cập mẫu sự khớp (matching): Được cho một sự triển khai kịch bản (ví dụ, đám mây API, tự- trị (au-tonomous) phương tiện, di động ứng dụng), bạn có thể chọn thích hợp MLPerf kịch bản và giải thích tại sao đó việc tạo lô chiến lược phù hợp (hay không)?, can you select the appropriate MLPerf scenario and explain why that batching strategy fits?) □ Thích ứng các cửa sổ: Bạn có thể giải thích tại sao tối ưu việc tạo lô cửa sổ giảm thiểu khi lưu lượng truy cập tăng lên, mặc dù lô các kích thước phát triển (hay không)? Các việc tạo lô các chiến lược được kiểm tra cho đến nay chia sẻ một tới hạn giả định: mỗi yêu cầu tạo ra một đơn, cố định-kích thước đầu ra—một sự phân loại nhãn, một (đường) bao hộp (bounding box), một nhúng vectơ. Giả định này chi phối việc xếp hàng đợi toán học, Pareto biên giới sự phân tích, và thích ứng-lưu lượng truy cập cửa sổ sự điều chỉnh. Nhanh nhất-đang phát triển (fastest-growing) thể loại (category) của việc phục vụ các khối lượng công việc, tuy nhiên, vi phạm giả định này hoàn toàn. Lớn ngôn ngữ các mô hình tạo sinh các đầu ra mã thông báo bởi mã thông báo, với mỗi mã thông báo (việc) phụ thuộc vào mọi (mã thông báo) trước đó. Một đơn yêu cầu có thể tạo ra hàng trăm hay hàng ngàn các mã thông báo qua các giây của (đã) trôi qua (elapsed) thời gian, tuy nhiên (yet) phải cảm thấy phản hồi (nhanh) từ đầu tiên mã thông báo trở đi (onward). Này cơ bản sự dịch chuyển (shift) từ cố định-đầu ra (sang) có thể thay đổi-chiều dài, việc truyền phát-đầu ra việc phục vụ xây dựng trực tiếp trên liên tục việc tạo lô và KV-bộ nhớ đệm việc phân trang (đã) được thiết lập cho tự hồi quy sự tạo sinh. (Những) gì nó thêm là sự chia nhỏ-giai đoạn (phase-split) các số liệu cho việc điền trước và việc giải mã, việc giải mã các chiến lược đánh đổi đầu ra chất lượng đối nghịch mỗi-mã thông báo chi phí, và bộ nhớ các chiến thuật (tactics) như là tiền tố sự tái sử dụng và việc giảm tải (offloading) khai thác được chia sẻ ngữ cảnh.
13.8 LLM Việc phục vụ Lớn ngôn ngữ các mô hình giới thiệu ba các thuộc tính vắng mặt (absent) từ truyền thống việc phục vụ: tự hồi quy sự tạo sinh25 (mỗi mã thông báo phụ thuộc vào tất cả trước đó các mã thông báo, việc làm đầu ra (về mặt) vốn có (trở nên) tuần tự)), có thể thay đổi-chiều dài đầu ra (phản hồi chiều dài là không được biết tại yêu cầu thời gian, việc làm mất hiệu lực (invalidating) cố định-lô các giả định)), và có trạng thái bộ nhớ (khóa-giá trị bộ nhớ đệm phát triển với mỗi tạo sinh mã thông báo, việc tạo ra động bộ nhớ áp lực truyền thống các mô hình không bao giờ đối mặt)). Cùng nhau, những các thuộc tính này tạo ra một (về mặt) định tính khác biệt việc phục vụ thách thức. p50, p95, và p99 các số liệu chi phối sự phân loại việc phục vụ vẫn quan trọng, nhưng chúng áp dụng cho khác biệt các giai đoạn của yêu cầu—ban đầu dấu nhắc việc xử lý và sau đó (subsequent) mã thông báo sự tạo sinh. Cơ bản các nguyên tắc của việc xếp hàng đợi lý thuyết, việc tạo lô các sự đánh đổi, và độ trễ các ngân sách áp dụng phổ quát; LLM việc phục vụ thêm đặc thù-miền các kỹ thuật (lên) trên này nền tảng.
13.8.1 Hiệu suất các số liệu: TTFT và TPOT Tạo sinh các mô hình tạo ra một luồng của các mã thông báo thay vì một đơn đầu ra tensor. Này việc truyền phát bản chất yêu cầu dành riêng (dedicated) LLM hiệu suất các số liệu phản ánh nội bộ trạng thái sự chuyển đổi (transition) từ “việc điền trước” (việc xử lý đầu vào) (tới) “việc giải mã” (việc tạo sinh đầu ra) (This streaming nature requires dedicated LLM performance metrics that reflect the internal state transition from “prefill” (processing input) to “decode”). Hai chính thước đo (measures) là Thời gian tới Đầu tiên Mã thông báo và Thời gian Mỗi Đầu ra Mã thông báo, thứ mà nắm bắt phản hồi (nhanh) và (tính) trôi chảy (fluidity) tương ứng (respectively) and Time Per Output Token (TPOT), which capture responsiveness and fluidity respectively). Định nghĩa 13.6: LLM hiệu suất các số liệu LLM Hiệu suất Các số liệu là hai-chiều (two-dimensional) các phép đo (measurements) của độ trễ cho việc truyền phát tự hồi quy sự tạo sinh.

13. Mô hình Việc phục vụ

1. Tầm quan trọng: Chúng phân rã được nhận thức-bởi-người dùng độ trễ thành Thời gian tới Đầu tiên Mã thông báo (TTFT) (chi phối bởi bị giới hạn-bởi-tính-toán Việc điền trước Giai đoạn) và Thời gian Mỗi Đầu ra Mã thông báo (TPOT) (chi phối bởi bị giới hạn-bởi-bộ-nhớ-băng-thông Việc giải mã Giai đoạn) and Time Per Output Token (TPOT)).
2. Sự khác biệt: Không giống như Cố định-Đầu ra Các số liệu (ví dụ, đầu cuối-tới-đầu cuối độ trễ), LLM các số liệu đo lường Tính trôi chảy của Sự tạo sinh, việc thừa nhận (acknowledging) rằng người dùng trải nghiệm phụ thuộc vào nhịp điệu (rhythm) của mã thông báo sự đến, LLM metrics measure the Fluidity of Generation, acknowledging that the user experience depends on the rhythm of token arrival).
3. Phổ biến cạm bẫy: Một thường xuyên quan niệm sai lầm là rằng một “nhanh mô hình” có một thấp TTFT. Trong thực tế, một mô hình có thể có một nhanh TTFT nhưng một chậm chạp (sluggish) TPOT (nếu bộ nhớ bức tường (BW) là nút thắt cổ chai), việc dẫn tới một bực bội (frustrating) người dùng trải nghiệm nơi câu trả lời bắt đầu nhanh chóng nhưng “nói lắp” (stutters) sau đó (thereafter) is the bottleneck), leading to a frustrating user experience where the answer starts quickly but “stutters” thereafter). Những hai các số liệu này nắm bắt biệt người dùng trải nghiệm các khía cạnh, và sản xuất các hệ thống thiết lập riêng biệt SLO các mục tiêu cho mỗi (số liệu). Các hệ thống Góc nhìn 13.9: LLM việc phục vụ độ trễ các mục tiêu Tương tác LLM các dịch vụ thường cần riêng biệt các SLO cho sự phản hồi (nhanh), sự tạo sinh tính trôi chảy, và hạm đội thông lượng. Các giá trị bên dưới là có tính minh họa (illustrative) các mục tiêu thay vì phổ quát các yêu cầu: • TTFT: < 500 ms (cho một 1000-mã thông báo dấu nhắc) • TPOT: < 50 ms (tương đương (tới) ~20 các mã thông báo/s, nhanh hơn con người việc đọc tốc độ) • Thông lượng: > 1000 các mã thông báo/s tổng (aggregate) qua hoạt động việc phục vụ các bản sao Các hệ thống điểm là rằng một đơn “độ trễ” con số che giấu việc điền trước/việc giải mã chia nhỏ: TTFT là trống-màn hình ngân sách, TPOT là việc đọc-luồng (reading-flow) ngân sách, và tổng dịch vụ thông lượng, được đo lường như (là) các mã thông báo/s tính tổng qua hoạt động việc phục vụ các bản sao, quyết định liệu những các mục tiêu đó tổ chức (hold) dưới chia sẻ tải (hay không).
13.8.2 Việc giải mã các chiến lược Việc đáp ứng những TPOT các mục tiêu này phụ thuộc vào nhiều (thứ) hơn bộ nhớ băng thông một mình (nó): thuật toán được sử dụng để chọn mỗi mã thông báo cũng ảnh hưởng mỗi-mã thông báo độ trễ và đầu ra chất lượng. Tạo sinh các mô hình yêu cầu việc giải mã các chiến lược đánh đổi chất lượng, tính đa dạng (diversity), và độ trễ. Sự lựa chọn của việc giải mã chiến lược quyết liệt ảnh hưởng (tới) cả đầu ra chất lượng và thuộc về tính toán chi phí. (Cái) đơn giản nhất cách tiếp cận, tham lam (greedy) việc giải mã, chọn cao nhất-xác suất mã thông báo tại mỗi bước tại chi phí của một mô hình (đường) chuyền (pass) cho mỗi mã thông báo. Nó là nhanh nhưng thường tạo ra lặp đi lặp lại (repetitive) các đầu ra bởi vì nó không thể phục hồi từ sớm các sai lầm. Chùm (Beam) tìm kiếm cải thiện chất lượng bằng cách việc duy trì nhiều ứng cử viên (candidate) các chuỗi và việc chọn cao nhất-ghi điểm (scoring) hoàn thành chuỗi, nhưng nó nhân (multiplies) mỗi-mã thông báo tính toán với chùm chiều rộng. Việc lấy mẫu (Sampling) với nhiệt độ (temperature), top-𝑘, và top-𝑝 (cũng được gọi (là) hạt nhân (nucleus) việc lấy mẫu) bơm (injects) được kiểm soát tính ngẫu nhiên (randomness) cho tính đa dạng tại không đáng kể phụ (extra) tính toán (Holtzman và cộng sự 2020) (Sampling with temperature, top-𝑘, and top-𝑝(also called nucleus sampling) injects controlled randomness for diversity at negligible extra compute); nó việc phục vụ chi phí nằm (lies) ít hơn trong số học (arithmetic) (so với) trong đầu ra-chiều dài phương sai, thứ mà mở rộng lây lan của chuỗi các chiều dài liên tục việc tạo lô phải hấp thụ (absorb). Những các chi phí này ghép (compound) tại mỗi-mã thông báo cấp độ (Meister và cộng sự 2020): chùm tìm kiếm với chiều rộng năm chạy xấp xỉ 5× tính toán của tham lam việc giải mã cho mọi mã thông báo, là lý do tại sao tương tác, nhạy cảm-độ trễ các sự triển khai hiếm khi (rarely) sử dụng nó và thay vào đó (với tới) (reach for) tham lam hay việc lấy mẫu: beam search with width five runs roughly 5× the compute of greedy decoding for every token, which is why interactive, latency-sensitive deployments rarely use it and instead reach for greedy or sampling). Sản xuất LLM các hệ thống trả về các mã thông báo khi chúng được tạo ra thay vì việc chờ đợi cho hoàn thành sự tạo sinh. Này việc truyền phát phản hồi biến đổi người dùng trải nghiệm: một hai-giây tổng sự tạo sinh cảm thấy phản hồi khi các mã thông báo truyền phát liên tục, nhưng cảm thấy phá vỡ khi người dùng nhìn chằm chằm (stare) tại một trống màn hình trong hai giây. Việc truyền phát yêu cầu cơ sở hạ tầng sự hỗ trợ cho phân đoạn HTTP các phản hồi và phía-máy khách (client-side) gia tăng (incremental) kết xuất. Độ trễ hồ sơ (profile) dịch chuyển tương ứng: TTFT quyết định khi đầu ra bắt đầu (việc) xuất hiện (sự phản hồi), trong khi TPOT quyết định được nhận thức sự tạo sinh tốc độ (tính trôi chảy), while TPOT determines the perceived generation speed (fluidity)). Một khi sự tạo sinh được truyền phát mã thông báo bởi mã thông báo, việc phục vụ nút thắt cổ chai dịch chuyển từ một sự dự đoán yêu cầu tới một có trạng thái chuỗi nó bộ nhớ dấu chân phát triển trên mọi bước.

13.8 LLM Việc phục vụ

KV Bộ nhớ đệm (Key-Value
Cache): Để tránh dư thừa (redundant) công việc, hệ thống lưu trong bộ nhớ đệm
Khóa và Giá trị các vectơ từ trước đó các mã thông báo, thứ (mà) duy- trì (re-main) hợp lệ (valid) trong suốt sự tạo- sinh (gen-eration).
Này thiết kế sự lựa chọn là trực tiếp nguyên nhân (cause) của động (dy-namic)
bộ nhớ sự phát triển mô-
tả; bộ nhớ đệm’s kích thước phát triển
tuyến tính với mọi tạo sinh
mã thông báo, việc làm bộ nhớ sự quản- lý (man-agement), không (phải) tính toán, (trở thành)
chính sự ép buộc (constraint). Cho
70-tỷ-tham số-lớp (class) được nhóm-truy vấn-sự chú ý (grouped-query-attention) kích- cỡ (siz-ing) ví dụ trong phần này,
FP16 KV bộ nhớ đệm là khoảng
0.31 MB cho mỗi mã thông báo cho mỗi chuỗi (se-quence);
được nhóm-truy vấn sự chú- ý (GQA), được sử dụng trong Llama-
gia đình các mô hình như là Llama
3, chia sẻ khóa/giá trị các đầu (heads) qua nhiều truy vấn các đầu,
việc giảm thiểu bộ nhớ đệm tương đối (so với) đầy nhiều-đầu sự chú ý.
Một
lô của 32 các yêu cầu tại một
8,000-mã thông báo ngữ cảnh do đó
yêu cầu xấp xỉ 80 GB chỉ cho
KV bộ nhớ đệm, vài lần lớn hơn
vẫn mà không có được nhóm-truy vấn hay nhiều-truy vấn sự chú ý.

Suy đoán (Speculative) Việc giải mã:
Một nhỏ “nháp” mô hình tạo-
sinh 𝑘 ứng cử viên các mã thông báo tự-
hồi quy; lớn mục-
tiêu mô hình sau đó xác minh
được đề xuất khối trong song song. Khi
nháp mô hình’s các đề xuất (proposals)
được chấp nhận tại tỷ lệ 𝛼, hiệu-
quả thông lượng có thể mở rộng
với số lượng của chấp nhận các mã thông báo cho mỗi sự xác minh bước.
Điều này phá vỡ nối tiếp tự hồi- quy (autore-gressive) nút thắt cổ chai tại thời gian chạy (run-time)
lớp, không (phải) kiến trúc lớp.
13.8.3 Bộ nhớ và KV bộ nhớ đệm Tạo sinh sự suy luận yêu cầu việc quản lý KV Bộ nhớ đệm26, một có trạng thái bộ nhớ cấu trúc phát triển với chuỗi chiều dài. Không giống như truyền thống các mô hình nơi bộ nhớ cách sử dụng là hằng số (cho) mỗi lô, LLM bộ nhớ cách sử dụng là động. Mỗi tạo sinh mã thông báo thêm (vào) ngữ cảnh cửa sổ, việc tiêu thụ bổ sung GPU bộ nhớ thông qua trạng thái sự tích lũy (accumulation), và có thể thay đổi-chiều dài các chuỗi có thể dẫn tới bộ nhớ sự phân mảnh nếu không được quản lý rõ ràng.
13.8.3.1 Tiền tố việc lưu trong bộ nhớ đệm và bộ nhớ việc giảm tải Liên tục việc tạo lô và PagedAttention các kỹ thuật được bao phủ trong phần 13.7.4 giải quyết yêu cầu sự lập lịch và bộ nhớ đệm việc phân trang; còn lại bộ nhớ áp lực có thể được (làm) giảm nhẹ hơn nữa thông qua thuộc về kiến trúc các chiến lược khai thác yêu cầu các mẫu. Tiền tố Việc lưu trong bộ nhớ đệm (Prefix Caching) lưu trữ KV bộ nhớ đệm của phổ biến hướng dẫn các tiền tố (như là một 2,000-mã thông báo hệ thống dấu nhắc hay một chia sẻ truy xuất-được tăng cường sự tạo sinh (retrieval-augmented generation - RAG) ngữ cảnh), việc cho phép nhiều độc lập các yêu cầu (để) tái sử dụng giống nhau được tính toán trước (precomputed) ẩn (hidden) các trạng thái context), allowing many independent requests to reuse the same precomputed hidden states). Cho 𝑁 các yêu cầu chia sẻ một tiền tố của 𝑆prefix các mã thông báo, được lưu (saved) việc điền trước công việc là xấp xỉ (𝑁−1)𝑆prefix mã thông báo các bước, cộng được tránh (avoided) các đọc và các ghi của tiền tố KV trạng thái (For 𝑁requests sharing a prefix of 𝑆prefix tokens, the saved prefill work is roughly (𝑁−1)𝑆prefix token steps, plus the avoided reads and writes of the prefix KV state). Cho nhiều-lượt các cuộc hội thoại, điều này “lưu trong bộ nhớ đệm của quá khứ” cho phép hệ thống (để) xử lý chỉ mới các mã thông báo trong mỗi lượt. Khi tổng KV bộ nhớ đệm vượt quá GPU VRAM, các hệ thống có thể sử dụng KV Bộ nhớ đệm Việc giảm tải. Này chiến lược tràn (spills) không hoạt động hay thấp-ưu tiên (priority) ngữ cảnh các cửa sổ (sang) máy chủ CPU RAM hay NVMe SSD, việc giải phóng VRAM cho hoạt động sự tạo sinh. Việc tải lại chi phí được giới hạn (bên) dưới bởi các byte được di chuyển (chia) cho (bởi) PCIe hay NVMe băng thông, trước (khi) phần mềm chi phí hoạt động và việc xếp hàng đợi được thêm (vào). Việc giảm tải do đó ngăn chặn Hết-Bộ-nhớ (OOM) các sự thất bại và kích hoạt lớn hơn ngữ cảnh các cửa sổ, nhưng nó cũng tạo ra sự thân thiết, sự vô hiệu hóa (invalidation), và nóng-việc giải mã độ trễ các rủi ro (risks) phải được lập ngân sách rõ ràng failures and enables larger context windows, but it also creates affinity, invalidation, and hot-decode latency risks that must be budgeted explicitly). Nâng cao các kỹ thuật việc bao gồm suy đoán việc giải mã27 và phân tán tính song song, nơi một yêu cầu bị chia qua nhiều các thiết bị hay các máy, được bao phủ trong chuyên môn hóa (specialized) các sự xử lý của lớn-quy mô các hệ thống. Thuộc về tính toán cường độ (intensity) của việc quản lý KV các bộ nhớ đệm qua đồng thời các yêu cầu dấy lên (raises) một rộng hơn câu hỏi về năng lượng chi phí của mỗi mã thông báo tạo sinh. Không giống như sự phân loại các mô hình nơi năng lượng cho mỗi sự suy luận là hằng số, LLM năng lượng sự tiêu thụ mở rộng với phản hồi chiều dài—mọi tạo sinh mã thông báo yêu cầu việc đọc toàn bộ mô hình từ bộ nhớ. Năng lượng và carbon hạch toán (accounting) dịch những phần cứng các nhu cầu (demands) này thành các số liệu làm (cho) thuộc về môi trường (environmental) tác động (trở nên) cụ thể. Khăn ăn Toán học 13.9: Carbon chi phí của một cuộc trò chuyện (chat) Bài toán: Làm thế nào nhiều năng lượng (does) một hỗ trợ-bởi-H100 trò chuyện dịch vụ tiêu tốn (cho) mỗi tạo sinh mã thông báo và cho một phản hồi với 500 các mã thông báo? Khi các LLM mở rộng, các joule cho mỗi mã thông báo trở thành một hạng-nhất (first-class) hoạt động số liệu song song với (alongside) độ trễ. Cho kịch bản này việc sử dụng một H100 GPU (700 W TDP), năng lượng dấu chân tuân theo từ thông lượng và công suất (Choquette 2023), the energy footprint follows from throughput and power (Choquette 2023):):
1. Thông lượng: 114 đồng thời các yêu cầu × 8 các mã thông báo/s cho mỗi yêu cầu ≈ 912 các mã thông báo/s.
2. Công suất: 700 W (GPU) + 300 W (Máy chủ (Host)/Chi phí hoạt động) = 1000 W + 300 W (Host/Overhead) = 1000 W).
3. Năng lượng cho mỗi mã thông báo: 1000 W / 912 các mã thông báo/s ≈ 1.0965 J/mã thông báo (Energy per token: 1000 W / 912 tokens/s ≈1.0965 J/token) Các hệ thống sự thấu hiểu: Một điển hình phản hồi của 500 các mã thông báo tiêu thụ ≈ 548.2 J. • Cho sự so sánh, việc sạc một điện thoại thông minh tiêu thụ ≈ 40000 J. • Việc đun sôi (Boiling) một cốc của nước tiêu thụ ≈ 100000 J. Chính cách để giảm thiểu J/mã thông báo là để làm tăng phần cứng sự sử dụng và loại bỏ (eliminate) dư thừa tính toán. Nếu GPU ngồi tại 10 phần trăm sự sử dụng do (bởi) kém việc tạo lô, nhàn rỗi công suất là vẫn ~300 W, việc gây ra năng lượng cho mỗi mã thông báo (để) tăng tới >3.3 J/mã thông báo. Thuộc về kiến trúc các sự tối ưu hóa như tiền tố việc lưu trong bộ nhớ đệm cũng bỏ qua (skip) chuyên sâu-năng lượng (energy-intensive) việc điền trước giai đoạn cho chia sẻ ngữ cảnh, trực tiếp việc giảm thiểu năng lượng dấu chân của truy xuất-được tăng cường sự tạo sinh (RAG) và trò chuyện các ứng dụng and chat applications). Việc phục- vụ bài học là rằng tính hiệu quả không phải chỉ (là) một độ trễ hay chi phí số liệu; nó cũng quyết định (làm thế nào) nhiều năng lượng mỗi hữu ích mã thông báo tiêu thụ.

13. Mô hình Việc phục vụ

ONNX
Thời gian chạy (Runtime): Microsoft’s sự suy luận công cụ (engine) hoạt động như một phần cứng sự trừu tượng
lớp: giống nhau ONNX mô hình
chạy
trên các CPU,
NVIDIA
các GPU, AMD các GPU, hay tùy chỉnh
các bộ tăng tốc
thông qua
có thể cắm- vào (plug-gable) “sự thực thi các nhà cung cấp.”
ONNX
Thời gian chạy
áp dụng không-biết-khuôn-khổ (framework-agnostic)
đồ thị
các sự tối ưu hóa—hằng số việc gấp (folding),
dư thừa
nút sự loại bỏ (elimination), toán tử (operator) sự hợp nhất (fusion)— thứ (mà) mang lại lợi ích (cho) tất cả các mục tiêu. Này
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
thị giác các mô hình,
bù đắp (offset)
bởi khả năng (để) nhắm mục tiêu lại (retarget) giống nhau.onnx đồ tạo tác qua
CPU/GPU/NPU
mà không có
sự biên dịch lại (recompilation)—một
tính linh hoạt phần thưởng (premium) quan trọng nhất trong không đồng nhất (heterogeneous) thiết bị các hạm đội
nơi việc biên dịch lại mỗi-mục tiêu được đo lường bằng các kỹ sư-các ngày (engineer-days).

TensorRT: Nó từ bỏ (abandons)
tính di động của chung- mục đích các khuôn khổ bằng cách việc yêu-
cầu một xây dựng giai đoạn tối-
ưu hóa mô hình cho một mục tiêu GPU kiến trúc (ví dụ (for exam-ple), một H100). Này phần cứng sự khóa-vào (lock-in) cho phép
tích cực các sự tối ưu hóa như
lớp sự hợp nhất và độ chính xác sự lựa-
chọn (là) không an toàn cho một
khuôn khổ phải chạy trên bất kỳ phần cứng .
(Cái) kết quả- mang lại (result-ing) không thể di động công cụ có thể
vật chất giảm thiểu độ trễ và
do đó số lượng của các GPU
yêu cầu để đáp ứng một thông lượng mục tiêu.

OpenVINO
(Mở (Open)
Thị giác Sự suy luận và Thần kinh
Mạng lưới
Sự tối ưu hóa): Một định hướng-Intel (Intel-oriented) sự suy luận
bộ công cụ (toolkit) chuyển đổi,
tối- ưu hóa,
và chạy các mô hình
qua
Intel CPU, GPU,
và
NPU
các mục tiêu
(Intel Tập đoàn (Corporation) 2026b).
Này trực tiếp phần cứng việc nhắm mục tiêu là
một “tích cực” sự tối ưu hóa
bởi vì nó từ bỏ một số
tính di động bản địa-khuôn-khổ
các thời gian chạy (run-times)
phải đảm bảo (guarantee),
việc cho phép
nó
(để) khai thác đặc thù-mục tiêu các hạt nhân (kernels) và độ chính xác các sự lựa chọn.
(Cái) kết quả mang lại hiệu suất lợi ích (gain) là phụ thuộc-khối lượng công việc- và -phần cứng, nhưng nó có thể làm (cho) dành riêng (dedicated) CPU hay (rìa) cạnh việc phục- vụ (trở nên) (về mặt) kinh tế khả thi (viable) cho
nhỏ hơn và nhạy cảm-độ trễ các mô hình. Năng lượng tính hiệu quả phụ thuộc vào giống nhau việc tạo lô, bộ nhớ, và tiền tố-bộ nhớ đệm các cơ chế chi phối LLM độ trễ, do đó hữu ích bản tóm tắt là một sự ép buộc danh sách kiểm tra (checklist) thay vì một đơn vô hướng (scalar) số liệu. Điểm kiểm tra 13.4: LLM việc phục vụ các nguyên tắc cơ bản LLM việc phục vụ giới thiệu các sự ép buộc vắng mặt từ truyền thống mô hình việc phục vụ. □ TTFT so với TPOT: Bạn có thể giải thích tại sao hai các số liệu này nắm bắt khác biệt người dùng trải nghiệm các khía cạnh (sự phản hồi (nhanh) so với tính trôi chảy) và tại sao chúng được chi phối bởi khác biệt phần cứng các nút thắt cổ chai (tính toán so với bộ nhớ băng thông) (hay không)? and why they are governed by different hardware bottlenecks?) □ Bộ nhớ bức tường (wall): Bạn có thể giải thích tại sao việc thêm nhiều tính toán các lõi (hơn) mang lại (yields) không độ trễ sự cải thiện cho mã thông báo sự tạo sinh, và tại sao chỉ nhanh hơn bộ nhớ hay nhỏ hơn các mô hình giúp ích (hay không)? (Llama-3 tình huống (case) nghiên cứu trong phần 13.11.4 định lượng (quantifies) này mối quan hệ.)) □ Liên tục việc tạo lô: Bạn có thể giải thích tại sao truyền thống tĩnh việc tạo lô lãng phí tính toán khi chuỗi các chiều dài thay đổi, và cách mức-lặp lại (iteration-level) việc tạo lô giải quyết điều này (hay không)? □ PagedAttention: Bạn có thể giải thích bộ nhớ sự phân mảnh bài toán trong KV bộ nhớ đệm sự quản lý và cách việc mượn ảo bộ nhớ các khái niệm từ HĐH thiết kế đạt được gần-không (near-zero) sự lãng phí (hay không)? □ Tiền tố việc lưu trong bộ nhớ đệm: Bạn có thể giải thích cách việc lưu trong bộ nhớ đệm KV các trạng thái của phổ biến hướng dẫn các tiền tố giảm thiểu dư thừa tính toán và tăng tốc RAG hay nhiều-lượt các ứng dụng (hay không)?
13.9 Sự suy luận Thời gian chạy (Runtime) Sự lựa chọn Việc tạo lô các chiến lược và đặc thù-LLM các kỹ thuật quyết định cách các yêu cầu được nhóm và xử lý. Những các chiến lược này giả định một cơ bản (underlying) sự thực thi công cụ thực sự (actually) chạy mô hình các tính toán—một giả định quan trọng to lớn (enormously). Mã thông báo sự tạo sinh mối quan hệ chính- thức hóa (formalized) sau đó trong chương này và độ trễ các ngân sách được thiết lập sớm hơn (chỉ) (có thể) đạt được nếu thời gian chạy hiệu quả ánh xạ các toán tử (operations) (tới) phần cứng. Sự suy luận thời gian chạy, phần mềm lớp sắp xếp (orchestrates) tensor các toán tử và quản lý phần cứng các tài nguyên, có thể thay đổi bởi một thứ tự của độ lớn (magnitude) trong hiệu suất cho giống hệt (identical) các mô hình. Thời gian chạy công việc do đó có hai các giai đoạn: sự lựa chọn chọn sự thực thi công cụ, và cấu hình điều chỉnh (tunes) đó công cụ cho mục tiêu mô hình, phần cứng, và độ trễ sự phân phối.
13.9.1 Thời gian chạy hệ sinh thái và cấu hình Sự lựa chọn nên bắt đầu với ràng buộc sự ép buộc thay vì khuôn khổ được sử dụng trong suốt sự đào tạo. Khi sự triển khai tốc độ và tính tương thích thống trị, PyTorch và TensorFlow các mô hình có thể phục vụ trực tiếp (việc) sử dụng của chúng bản địa (native) các thời gian chạy. Này cách tiếp cận tối đa hóa tính tương thích (bất kỳ mô hình đào tạo sẽ phục vụ) và đơn giản hóa sự triển khai đường ống (không (cần) xuất hay sự chuyển đổi bước) and simplifies the deployment pipeline). Khuôn khổ các thời gian chạy bao gồm sự đào tạo tính năng (functionality) thêm (vào) chi phí hoạt động, và mặc định sự thực thi các con đường có thể không khai thác đặc thù-phần cứng các sự tối ưu hóa. TorchScript và TensorFlow SavedModel các định dạng (formats) kích hoạt biên dịch-trước (ahead-of-time) và đồ thị sự tối ưu hóa, việc cải thiện (so với) háo hức (eager) sự thực thi trong khi (vẫn) việc duy trì khuôn khổ tính tương thích. Những các định dạng này đại diện (cho) đầu tiên bước về phía sự triển khai sự tối ưu hóa mà không có việc từ bỏ quen thuộc khuôn khổ hệ sinh thái.
13.9.1.1 Chung-mục đích sự tối ưu hóa Khi tính di động qua phần cứng là ràng buộc sự ép buộc, ONNX Thời gian chạy28 cung cấp một phần cứng- không-biết sự tối ưu hóa lớp). Các mô hình xuất tới ONNX định dạng, sau đó ONNX Thời gian chạy áp dụng đồ thị các sự tối ưu hóa và chọn sự thực thi các nhà cung cấp cho mục tiêu phần cứng. Điều này kích hoạt đơn-định dạng sự triển khai qua các CPU, các GPU, và chuyên môn hóa các bộ tăng tốc.
13.9.1.2 Được chuyên môn hóa sự suy luận các công cụ Khi độ trễ hay phần cứng chi phí ràng buộc chặt chẽ (tightly) hơn (so với) tính di động, TensorRT29 (NVIDIA các GPU),

13.9 Sự suy luận Thời gian chạy Sự lựa chọn

Lớp Sự hợp nhất (Fusion):
Tương tự (Analo-gous) (với) vòng lặp sự hợp nhất trong trình biên- dịch (com-piler) sự tối ưu hóa, nơi liền kề (ad-jacent) các vòng lặp qua giống nhau mảng
(ar-ray) được kết hợp để giảm thiểu bộ nhớ lưu lượng truy cập.
Hạt nhân (Kernel) sự hợp- nhất áp dụng giống hệt (identical) nguyên- tắc (prin-ciple) cho GPU các toán tử (operations): tuần-
tự (se-quential) các hạt nhân ghi
và đọc-lại trung gian các ten-
sor từ HBM được hợp nhất
thành một đơn hạt nhân giữ dữ liệu trong các thanh ghi (registers). Các khoản tiết kiệm (savings) ghép (lại)—một điển hình ResNet-
50 có ~35 (có thể) hợp nhất toán- tử (opera-tion) các cặp (pairs), và mỗi loại- bỏ (elimi-nated) HBM chuyến khứ hồi (round-trip) tiết kiệm
1–3 𝜇s tại 3.35 TB/s băng- thông (band-width), việc chuyển đổi bị giới hạn-bởi-
bộ nhớ các chuỗi thành bị giới hạn-bởi- tính toán (compute-bound) được hợp nhất các hạt nhân. OpenVINO30 (Intel phần cứng), và tương tự các công cụ tối ưu hóa đặc thù cho của chúng mục tiêu phần cứng (NVIDIA 2024c; Intel Tập đoàn 2026b; Chen và cộng sự 2018), and similar engines optimize specifically for their target hardware). Chúng áp dụng tích cực các sự tối ưu hóa bản địa-khuôn-khổ các thời gian chạy không thể an toàn thực hiện. Lớp sự hợp nhất31 kết hợp nhiều tuần tự các toán tử thành một đơn GPU hạt nhân. Xem xét một phổ biến mẫu: tích chập (convolution) → lô chuẩn hóa → ReLU sự kích hoạt (activation) (Consider a common pattern: convolution →batch normalization →rectified linear unit (ReLU) activation). Không có sự hợp nhất, điều này yêu cầu ba hạt nhân các sự khởi chạy (launches), ba các chuyến khứ hồi tới GPU bộ nhớ (việc ghi tích chập đầu ra, việc đọc cho chuẩn hóa lô, việc ghi chuẩn hóa lô đầu ra, việc đọc cho ReLU), và ba các tập hợp của trung gian các tensor, and three sets of intermediate tensors). Sự hợp nhất kết hợp tất cả ba thành một hạt nhân đọc các đầu vào một lần, tính toán được kết hợp kết quả trong các thanh ghi, và ghi cuối cùng các đầu ra một lần. Điều này loại bỏ hạt nhân sự khởi chạy chi phí hoạt động (15–60 μs tiết kiệm (cho) mỗi sự hợp nhất) và giảm thiểu bộ nhớ lưu lượng truy cập bởi 2–3× (This eliminates kernel launch overhead (15–60 μs saved per fusion) and reduces memory traffic by 2–3×). TensorRT tự động phát hiện và hợp nhất phổ biến các mẫu; một điển hình ResNet-50 giảm thiểu từ ~50 các hạt nhân (xuống) ~15 sau sự hợp nhất. Hạt nhân tự động-điều chỉnh (auto-tuning) chọn nhanh nhất thuật toán cho mỗi toán tử trên cụ thể GPU. Một đơn tích chập có thể được triển khai (việc) sử dụng hàng chục (dozens) của các thuật toán như là trực tiếp (direct), nhanh Fourier biến đổi (FFT) dựa-trên (based), Winograd, và đa dạng (việc) xếp gạch (tiling) các chiến lược, mỗi (là) tối ưu cho khác biệt đầu vào các kích thước và GPU các kiến trúc based, Winograd, and various tiling strategies, each optimal for different input sizes and GPU architectures). Tự động-điều chỉnh (việc) chuẩn mực (benchmarks) mỗi ứng cử viên và lưu trong bộ nhớ đệm người chiến thắng (winner), việc đánh đổi biên dịch thời gian (lấy) thời gian chạy hiệu suất. Những các sự tối ưu hóa này điển hình đạt được 2–5× tăng tốc (speedup) (so với) bản địa-khuôn-khổ việc phục vụ nhưng yêu cầu rõ ràng xuất và có thể không hỗ trợ tất cả các toán tử. Một thời gian chạy sự so sánh trên một chuẩn (standard) mô hình định lượng (quantifies) những lợi ích này qua sự tối ưu hóa quang phổ (spectrum). Các hệ thống Góc nhìn 13.10: ResNet-50: Thời gian chạy sự so sánh
Bảng 13.19 so sánh ResNet-50 sự suy luận độ trễ và sự tăng tốc qua các thời gian chạy trên một V100 GPU tại lô kích thước một:
Bảng 13.19: Sự suy luận thời gian chạy sự so sánh: Độ trễ và sự tăng tốc cho ResNet-50 (lô kích thước một) qua PyTorch háo hức, TorchScript, ONNX Thời gian chạy, và TensorRT trong ba độ chính xác (precisions) trên một V100 across PyTorch eager, TorchScript, ONNX Runtime, and TensorRT in three precisions on a V100). Mỗi bước (xuống) dưới (bảng) đổi (trades) tính di động cho thô (raw) tốc độ, việc phơi bày (exposing) sự tối ưu hóa-tính tương thích sự đánh đổi định nghĩa thời gian chạy sự lựa chọn.
Thời gian chạy
Độ trễ
Sự tăng tốc
Các ghi chú
PyTorch (háo hức)
8.5 ms
1×
Cơ sở (Baseline), không sự tối ưu hóa
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
Yêu cầu sự hiệu chuẩn (calibration) Các hệ thống sự thấu hiểu: (Cái) 9.4× tăng tốc từ TensorRT INT8 đến tại chi phí của: (1) sự lượng tử hóa sự hiệu chuẩn dữ liệu, (2) tiềm năng (potential) độ chính xác (accuracy) sự mất mát (<1 phần trăm cho ResNet-50), và (3) đặc thù-NVIDIA sự triển khai (Systems insight: The 9.4× speedup from TensorRT INT8 comes at the cost of: (1) quantization calibration data, (2) potential accuracy loss, and (3) NVIDIA-specific deployment). Sự tối ưu hóa-tính tương thích sự đánh đổi là vốn có (inherent). Tích cực hơn sự tối ưu hóa mang lại tốt hơn hiệu suất tuy nhiên (làm) tăng (lên) sự triển khai tính phức tạp và có thể giới thiệu thuộc về số (numerical) các sự khác biệt từ sự đào tạo. Sự lựa chọn phụ thuộc vào độ trễ các yêu cầu, sự triển khai các sự ép buộc, và sẵn sàng kỹ thuật các tài nguyên. Sau khi thời gian chạy được chọn, cấu hình áp dụng giống nhau sự ép buộc-đầu tiên (constraint-first) logic. Luồng (Thread) hồ (pool) việc định kích thước (sizing) kiểm soát tính song song cho CPU sự suy luận: quá ít các luồng để (lại) các lõi nhàn rỗi, trong khi quá nhiều gây ra sự tranh chấp (contention). Bộ nhớ sự cấp phát các chiến lược (cấp phát trước các bộ đệm so với động sự cấp phát) đánh đổi khởi động chi phí đối nghịch tính linh hoạt trade startup cost against flexibility). Sự thực thi nhà cung cấp sự lựa chọn ưu tiên phần cứng 백엔드 (backends) xử lý mỗi toán tử, và đồ thị sự tối ưu hóa cấp độ đánh đổi sự biên dịch thời gian cho thời gian chạy hiệu suất. Những các cài đặt này là không (phải) một riêng biệt danh sách kiểm tra sau sự lựa chọn; chúng là cách được chọn thời gian chạy được làm (cho) thành thật (honest) dưới sản xuất lưu lượng truy cập. Sản xuất các sự triển khai do đó đo lường cấu hình tác động trên độ trễ các sự phân phối thay vì (việc) dựa vào mặc định.

13. Mô hình Việc phục vụ

13.9.2 Độ chính xác (Precision) sự lựa chọn cho việc phục vụ Một nhóm triển khai ResNet-50 trên V100 các GPU đối mặt một cụ thể sự ép buộc: của họ 30-GPU cụm (cluster) tốn $90/giờ, và kinh doanh sự phát triển yêu cầu 3× nhiều (hơn) thông lượng mà không (cần) việc mở rộng hạm đội. Việc chuyển đổi từ FP32 (sang) INT8 sự suy luận đạt được chính xác điều này—giống nhau mô hình trên giống nhau phần cứng phục vụ 3× nhiều (hơn) các yêu cầu mỗi giây, việc giảm thiểu hiệu quả chi phí cho mỗi sự suy luận bởi hai-phần ba, tại một chi phí của ít hơn 0.4 phần trăm điểm của độ chính xác. Ví dụ này minh họa trực tiếp mối kết nối giữa thuộc về số độ chính xác và cơ sở hạ tầng tính kinh tế. Độ chính xác sự lựa chọn kết nối tới sự lượng tử hóa các kỹ thuật được bao phủ trong phần 10.4. Phần D.4 so sánh thuộc về số các định dạng và của chúng độ chính xác-phạm vi (precision-range) các sự đánh đổi, và phần D.4.2 chi tiết cơ chế của đối xứng (symmetric) và bất đối xứng (asymmetric) số nguyên (integer) sự lượng tử hóa and their precision-range trade-offs, and section D.4.2 details the mechanics of symmetric and asymmetric integer quantization). Việc phục vụ thêm thời gian chạy các mối quan tâm như là sự hiệu chuẩn dữ liệu sẵn sàng (availability), lớp nhạy cảm (sensitivity) dưới sản xuất các đầu vào, và động độ chính xác sự lựa chọn.
13.9.2.1 Độ chính xác-thông lượng mối quan hệ Cho bị giới hạn-bởi-bộ nhớ-băng thông các toán tử, việc giảm thiểu độ chính xác tương xứng (proportionally) (làm) tăng thông lượng bằng cách việc giảm thiểu dữ liệu di chuyển. Phương trình 13.16 định lượng thuộc về lý thuyết tối đa sự tăng tốc từ độ chính xác sự giảm thiểu:
ThroughputINT8
ThroughputFP32
= 32 8 = 4× (thuộc về lý thuyết tối đa (theoretical maximum))
(13.16) Trong thực tế, GPU tính toán các đường ống và Tensor Lõi sự căn chỉnh (alignment) các hiệu ứng (effects) giới hạn đạt được tăng tốc tới 2.5–3.5× cho INT8 so với FP32. Tensor Lõi các hạt nhân là hiệu quả nhất khi ma trận các chiều (dimensions) căn chỉnh, như là INT8 các bội số (multiples) của 16 các phần tử và FP16 các bội số của 8 các phần tử trên nhiều các con đường. Hiện đại cuBLAS và cuDNN có thể vẫn sử dụng Tensor Các lõi cho nhiều khác các chiều, mặc dù thường kém hiệu quả hơn hay với nội bộ việc đệm (padding). Chương 11 cung cấp chi tiết Tensor Lõi kiến trúc giải thích những sự căn chỉnh các sự ép buộc này. Độ chính xác các sự đánh đổi cho một chuẩn thị giác mô hình minh họa cách những thuộc về lý thuyết các giới hạn này biểu hiện (manifest) trong thực tế. Các hệ thống Góc nhìn 13.11: ResNet-50: Độ chính xác các sự đánh đổi trên V100
Bảng 13.20 so sánh độ trễ, bộ nhớ, độ chính xác (accuracy), và Tensor Lõi sự sử dụng qua FP32, FP16, và hai INT8 các con đường cho ResNet-50:
Bảng 13.20: Độ chính xác các sự đánh đổi trên V100: Độ trễ, bộ nhớ dấu chân, độ chính xác, và Tensor Lõi sự sử dụng cho ResNet-50 trong FP32, FP16, và INT8 (PTQ và QAT)). FP16 là một gần-miễn phí (near-free) 2× sự tăng tốc (so với) FP32, trong khi INT8 đạt tới 3.1× (so với) FP32 (1.6× vượt qua (beyond) FP16) tại chi phí của sự hiệu chuẩn dữ liệu và một phần nhỏ của một phần trăm điểm trong độ chính xác (FP16 is a near-free 2× speedup over FP32, while INT8 reaches 3.1× over FP32 (1.6× beyond FP16) at the cost of calibration data and a fraction of a percentage point in accuracy).
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
Đầy sự đào tạo lại Các hệ thống sự thấu hiểu: INT8 đạt được 3.1× tăng tốc nhưng mất 0.33 phần trăm điểm của độ chính xác với sau-sự đào tạo sự lượng tử hóa (PTQ) (Systems insight: INT8 achieves 3.1× speedup but loses 0.33 percentage points of accuracy with post-training quantization (PTQ)). Sự lượng tử hóa-nhận thức (aware) sự đào tạo (QAT) khôi phục hầu hết độ chính xác nhưng yêu cầu sự đào tạo lại recovers most accuracy but requires retraining). FP16 cung cấp 2× tăng tốc với không độ chính xác sự mất mát cho hầu hết các mô hình.
13.9.2.2 Độ chính xác sự lựa chọn các sự ép buộc Độ chính xác sự lựa chọn bị ép buộc bởi lớp sự nhạy cảm, sự hiệu chuẩn dữ liệu, và thời gian chạy chính sách. Không phải tất cả các lớp chịu đựng (tolerate) được giảm thiểu độ chính xác ngang bằng nhau (equally). (Một cách) theo kinh nghiệm, sự lượng tử hóa lỗi (error) cho một lớp mở rộng với trọng số độ lớn (magnitude) và gradient (độ dốc) sự nhạy cảm, nắm bắt bởi sau (đây) tỷ lệ thuận (proportionality) trong phương trình 13.17:
𝜖quant ∝ 𝜅quant ⋅ ‖𝑊‖2 ⋅ 2−𝑏
(13.17)

13.10 Nút-Cấp độ Sự tối ưu hóa

nơi 𝜅quant là một đặc thù-lớp sự nhạy cảm hệ số (coefficient) (xác định theo kinh nghiệm hay thông qua Fisher thông- tin), ‖𝑊‖2 là trọng số L2 chuẩn (norm), và 𝑏 là bit độ rộng (where 𝜅quant is a layer-specific sensitivity coefficient (determined empirically or via Fisher informa-tion), ‖𝑊‖2 is the weight L2 norm, and 𝑏is the bit width). Điều này giải thích quan sát các mẫu nơi đầu tiên tích chập các lớp với cao các gradient và lớn sự nhạy cảm các hệ số là nhạy cảm-độ chính xác và thường giữ tại FP16, giữa các lớp với ổn định các gradient và thấp sự nhạy cảm các hệ số chịu đựng INT8 tốt, và cuối cùng sự phân loại các lớp với nhỏ các trọng số nhưng cao tác vụ (task) sự nhạy cảm hưởng lợi từ FP16 hay cao hơn độ chính xác. Sau-sự đào tạo sự lượng tử hóa thêm một dữ liệu sự ép buộc. Sự hiệu chuẩn tập dữ liệu quyết định tỷ lệ (scale) các hệ số (factors) sử dụng cho INT8 sự chuyển đổi, do đó nó phải đại diện (cho) thực tế việc phục vụ lưu lượng truy cập thay vì chỉ đơn thuần (merely) tái sử dụng thuận tiện (convenient) sự đào tạo hay sự xác thực (validation) dữ liệu. Một mô hình hiệu chuẩn trên ImageNet-kiểu (style) sự xác thực các hình ảnh có thể mất vài phần trăm các điểm khi phục vụ trên hoang dã (wildlife) máy ảnh các hình ảnh với khác biệt chiếu sáng và các nền (backgrounds), một sự thất bại chế độ ghé thăm lại (revisited) trong phần 13.12. Nâng cao việc phục vụ các hệ thống biến độ chính xác thành một thời gian chạy chính sách. Nếu hệ thống là đi trước (ahead of) nó độ trễ SLO, nó có thể sử dụng cao hơn độ chính xác cho tốt hơn độ chính xác (accuracy). Cho thấp-sự tự tin (confidence) INT8 các kết quả, nó có thể tính toán lại tại FP16. Khác biệt khách hàng các bậc (tiers) có thể nhận khác biệt độ chính xác các cấp độ. Này mẫu kích hoạt thích ứng chất lượng-độ trễ các sự đánh đổi trong khi tối đa hóa thông lượng trong suốt bình thường hoạt động. Độ chính xác quyết định có trực tiếp cơ sở hạ tầng các hệ quả (consequences): INT8 sự suy luận đạt được xấp xỉ 3× cao hơn thông lượng (so với) FP32, (việc) có nghĩa (là) một khối lượng công việc yêu cầu 30 các GPU tại FP32 chỉ cần 10 tại INT8. Này 3× sự giảm thiểu trong phần cứng chuyển đổi (translates) trực tiếp (thành) một 3× sự giảm thiểu trong hoạt động các chi phí. Mối kết nối giữa mức-mô hình sự tối ưu hóa và cơ sở hạ tầng tính kinh tế là lý do tại sao độ chính xác sự lựa chọn không thể được đối xử như (là) hoàn toàn một mô hình mối quan tâm. Thời gian chạy sự lựa chọn và độ chính xác sự điều chỉnh hoạt động tại mô hình cấp độ: chúng quyết định gì tính- toán chạy và tại gì thuộc về số định dạng. Giữa mô hình và silicon, tuy nhiên, nằm (lies) một khác sự tối ưu hóa lớp bao quanh (encompassing) cơ chế của đồ thị sự biên dịch (thành) các hạt nhân, byte sự di chuyển từ đĩa (tới) bộ nhớ, và CPU-GPU sự phối hợp (coordination). Những cấp độ-nút các kỹ thuật này thường mang lại cuối cùng 2–5× phân tách một có chức năng nguyên mẫu từ một cấp độ-sản xuất việc phục vụ nút.
13.10 Cấp độ-Nút Sự tối ưu hóa Xem xét một hình ảnh bộ phân loại (classifier) nó mô hình điểm chuẩn hứa hẹn (promises) mili giây sự suy luận nhưng nó sản xuất dấu vết (trace) hiển thị một chậm hơn yêu cầu con đường. Cấp độ-nút sự tối ưu hóa nhận diện ranh giới nào đang lãng phí thời gian trên đó máy. Dấu vết thường chỉ (points) (tới) một của bốn lặp lại (recurring) chẩn đoán (diagnostic) các ranh giới: • Đồ thị-tới-hạt nhân ranh giới: Tính toán đồ thị phải trở thành một nhỏ số lượng của hiệu quả các hạt nhân thay vì một dài chuỗi của sự khởi chạy các chi phí hoạt động. • CPU sự thực thi ranh giới: Phía-CPU công việc phải khai thác vectơ các đơn vị (units), tính cục bộ (locality), và thời gian chạy các thư viện thay vì vô hướng (scalar) Python. • Tải ranh giới: Mô hình các byte phải di chuyển từ đĩa vào bộ nhớ đủ nhanh (rằng) lạnh các khởi động không thống trị tăng-quy mô (scale-up) các sự kiện. • Máy chủ-bộ tăng tốc ranh giới: Máy chủ phải giữ bộ tăng tốc lên lịch mà không các khoảng trống gây ra bởi việc tiền xử lý, các sự truyền (transfers), hay sự đồng bộ hóa. Đây là không (phải) độc lập các thủ thuật (tricks). Chúng là các vị trí (places) nơi một đo lường dấu vết có thể giải thích tại sao một yêu cầu con đường là chậm hơn (so với) mô hình điểm chuẩn đã hứa.
13.10.1 Thời gian chạy đồ thị sự biên dịch Sự suy luận các công cụ như TensorRT đã được giới thiệu trong phần 13.9. Những các công cụ này đạt được 2–5× các sự tăng tốc bởi vì việc phục vụ thay đổi trình biên dịch bài toán. Sự đào tạo tính toán các đồ thị là động và có thể thay đổi (mutable), trong khi việc phục vụ các đồ thị là thường tĩnh. Một khi các hình dạng (shapes) và các toán tử (operators) cố định, trình biên dịch có thể tiêu (spend) thời gian-sự triển khai công việc để loại bỏ thời gian chạy công việc. (Cái) đầu tiên lợi ích là toán tử sự hợp nhất, giống nhau hạt nhân-sự hợp nhất sự tối ưu hóa phần 13.9.1.2 đã áp dụng (cho) TensorRT. (Những) gì tĩnh việc phục vụ đồ thị thêm (vào) là khi sự hợp nhất xảy ra: bởi vì các toán tử và các hình dạng cố định trước khi bất kỳ yêu cầu đến, trình biên dịch có thể khám phá và cam kết (commit) được hợp nhất các hạt nhân sớm (trước) thay vì (việc) khám phá lại chúng tại thời gian chạy, do đó không yêu cầu trả cho sự phân tích. (Cái) giống nhau tĩnh đồ thị cũng kích hoạt hằng số việc gấp. Nếu một biểu thức con (subexpression) phụ thuộc chỉ vào cố định các trọng số hay các hằng số, như là x * (sqrt(2) / 2), trình biên dịch thay thế nó với được tính toán trước

13. Mô hình Việc phục vụ

SIMD (Đơn Lệnh (Instruction),
Nhiều Dữ liệu (Data)): Từ
Michael Flynn’s 1966 phân loại
học (taxon-omy) của máy tính các kiến- trúc (architec-tures), SIMD kích hoạt một lệnh (in-struction) (để) hoạt động trên nhiều
dữ liệu các phần tử đồng thời (simul-taneously).
Intel’s AVX-512
xử lý 512 các bit (16 các float)
(cho) mỗi lệnh;
AMX mở- rộng (ex-tends) điều này (tới) ma trận ô (tile) các toán- tử.
Cho CPU sự suy
luận, SIMD khai thác là
chính sự tối ưu hóa đòn bẩy:
ngây thơ vô hướng ma trận phép nhân (multipli-cation) đạt được ~1 phần trăm của thuộc về lý thuyết đỉnh, trong khi SIMD-
được tối ưu hóa các hạt nhân tiếp cận
80–90 phần trăm sự sử dụng—một
khoảng trống quyết định liệu
chỉ-CPU việc phục vụ là (về mặt) kinh- tế khả thi (hay không).

NUMA (Không-Đồng đều (Non-Uniform) Bộ nhớ Truy cập (Access)): Việc truy cập
bộ nhớ cục bộ (với) một CPU socket là nhanh hơn (so với) việc truy cập bộ nhớ
đính kèm (với) một khác biệt socket. Việc ghim (Pinning) một sự suy luận
luồng (tới) một lõi là không đủ
nếu nó yêu cầu bộ nhớ cấp-
phát từ xa (remotely), việc ép buộc mọi
trọng số truy cập qua chậm hơn giữa-socket (inter-socket) liên kết. Này sự thất bại (để) cùng-định vị (co-locate) các luồng và dữ liệu áp đặt (imposes) một ~60 phần-
trăm độ trễ chi phí hoạt động, khi từ
xa truy cập tốn ~130 ns so với ~80 ns cho cục bộ.
(Cái) hình phạt (penalty) được ghép (compounded) cho ML các khối lượng công việc bởi vì mô hình các trọng số,
thứ (mà) có thể dao động
từ hàng trăm của megabyte
tới gigabyte, vượt quá L3 bộ nhớ đệm
công suất hoàn toàn—việc đảm bảo rằng chéo-socket (cross-socket) các tìm nạp (fetches) xảy ra trên mọi sự suy luận (đường) chuyền thay vì chỉ trên bộ nhớ đệm các trượt (misses). phép nhân x * 0.707.... Điều này loại bỏ công việc từ mọi yêu cầu mà không (cần) (việc) thay đổi mô hình’s toán học đầu ra. Bộ nhớ việc lập kế hoạch áp dụng giống nhau ý tưởng (cho) sự cấp phát thay vì số học. Vì tensor các vòng đời (lifetimes) biết (đến), thời gian chạy có thể tính toán trước bộ nhớ các phần bù (offsets) và tái sử dụng các bộ đệm thay vì việc cấp phát phản ứng trong suốt yêu cầu. Kết quả là không phải chỉ (là) ít hơn các toán tử, nhưng một dễ đoán hơn việc phục vụ con đường với ít hơn bộ cấp phát (allocator) (các sự) ngừng trệ (stalls) và ít hơn bộ nhớ sự phân mảnh. Những các sự tối ưu hóa này dẫn tới một sự triển khai sự lựa chọn. Đúng-lúc (Just-in-time) sự biên dịch thích ứng với các hình dạng quan sát tại thời gian chạy, nhưng đầu tiên yêu cầu trả (cho) sự biên dịch hình phạt. Biên dịch-trước (Ahead-of-time) sự biên dịch loại bỏ đó khởi động đỉnh (nhọn) (spike) bằng cách (việc) vận chuyển (shipping) một tối ưu hóa đồ tạo tác, nhưng sự triển khai phải rõ ràng bao phủ mọi hình dạng hồ sơ dịch vụ sẽ chấp nhận. Các hệ thống Góc nhìn 13.12: Sự biên dịch thời gian (timing) sự đánh đổi Đúng-lúc sự biên dịch chờ (đợi) cho đến khi đồ thị được (thực) thi (lần) đầu tiên và có thể chuyên môn hóa (specialize) (với) các hình dạng nó quan sát. Đó sự chuyên môn hóa là hữu ích cho có thể thay đổi lưu lượng truy cập, nhưng nó di chuyển trình biên dịch công việc vào việc phục vụ con đường và tạo ra một lạnh-yêu cầu độ trễ đỉnh nhọn. Biên dịch-trước sự biên dịch thực hiện trình biên dịch công việc trước (khi) sự triển khai. Nó (mang) lại (cho) dịch vụ một cố định đồ thị và tránh khởi động sự biên dịch độ trễ, tại chi phí của việc định nghĩa tất cả động các hình dạng rõ ràng hay việc biên dịch nhiều hồ sơ. Các hệ thống sự lựa chọn là ở đâu (để) trả (cho) sự biên dịch chi phí: JIT trả nó trong việc phục vụ con đường và có nguy cơ (risks) một đầu tiên-yêu cầu độ trễ đỉnh nhọn, trong khi AOT trả nó trước (khi) sự triển khai và yêu cầu chặt chẽ hơn (tự) kiểm soát đối với đầu vào các hình dạng.
13.10.2 CPU sự suy luận sự tối ưu hóa JIT so với AOT sự lựa chọn chi phối GPU sự biên dịch chiến lược; CPU sự suy luận đối mặt riêng nó sự tối ưu hóa phong cảnh (landscape), nơi sự vectơ hóa (vectorization) và sự lượng tử hóa thay thế đồ thị sự biên dịch như (là) chính các đòn bẩy. Các GPU thống trị câu chuyện (narrative), tuy nhiên (yet) các CPU vẫn (là) (con) ngựa thồ (workhorse) cho nhiều sự suy luận các khối lượng công việc, đặc biệt nhỏ các mô hình, không nhạy cảm-độ trễ lô các công việc, và bị ép buộc-chi phí các môi trường. CPU sự tối ưu hóa bắt đầu từ một khác biệt máy mô hình. Hiện đại các CPU32 chứa vectơ các đơn vị như là AVX-512 và AMX, nhưng một vô hướng Python vòng lặp không thể sử dụng chúng contain vector units such as AVX-512 and AMX, but a scalar Python loop cannot use them). (Được) chuyên môn hóa các thời gian chạy như OpenVINO hay Intel Phần mở rộng cho PyTorch (IPEX) ánh xạ thần kinh mạng lưới các toán tử trực tiếp (tới) những vectơ các lệnh này, đáng kể việc cải thiện hiệu suất (so với) ngây thơ vô hướng các sự triển khai (Intel Tập đoàn 2026b) map neural network operators directly to these vector instructions, substantially improving performance over naive scalar implementations). Tiếp theo CPU ranh giới là tính cục bộ (locality). Trên nhiều-socket các máy chủ33, việc truy cập bộ nhớ đính kèm (với) một khác biệt CPU socket (NUMA) thêm đáng kể độ trễ adds significant latency). Một sự suy luận máy chủ phải do đó (là) NUMA- nhận thức (aware): các luồng nên được ghim (tới) cụ thể các lõi, và mô hình các trọng số và đầu vào các bộ đệm luồng đó chạm (vào) nên được cấp phát trên giống nhau socket. ML mô hình các trọng số—hàng trăm của megabyte cho một tầm trung (mid-sized) mạng lưới, gigabyte cho một lớn ngôn ngữ mô hình—đồ sộ vượt quá công suất của một CPU’s L3 bộ nhớ đệm, do đó NUMA hình phạt là dai dẳng (persistent) thay vì thỉnh thoảng (occasional). Mọi sự suy luận đường chuyền phải đọc đầy trọng số tensor; đang làm việc tập hợp (working set) không bao giờ khớp (vừa) trong bộ nhớ đệm, việc tạo ra đảm bảo bộ nhớ đệm đập (thrashing) và việc ép buộc (việc) không đổi tìm nạp (fetches) từ chính RAM qua chậm hơn giữa-socket liên kết. Đây là lý do tại sao các CPU thường vượt trội (so với) các GPU tại lô kích thước một cho nhỏ các mô hình. Việc khởi chạy một GPU hạt nhân (~10 𝜇s) và việc truyền (transferring) dữ liệu (~50 𝜇s) có thể vượt quá tính toán thời gian cho một bé xíu dày đặc (dense) lớp (Launching a GPU kernel (~10 𝜇s) and transferring data (~50 𝜇s) can exceed the compute time for a tiny dense layer). Cho các mô hình (dưới) 50 MB phục vụ đơn các yêu cầu, một tối ưu hóa-tốt CPU thời gian chạy có thể cung cấp thấp hơn độ trễ (so với) một GPU bởi vì nó tránh bộ tăng tốc sự chuyển giao (handoff) hoàn toàn.
13.10.3 Mô hình sự tuần tự hóa (serialization) và nhanh việc tải (loading) Tự động mở rộng (Autoscaling) các hệ thống là hoạt động kiểm soát các vòng lặp thêm hay xóa (bỏ) việc phục vụ các bản sao dựa trên tải. Trong những hệ thống đó, thời gian để quay lên (spin up) một mới nút là tới hạn. Một chính thành phần của “Lạnh Sự khởi động” (phần 13.6.2) là đơn giản việc đọc mô hình các trọng số từ đĩa vào bộ nhớ (A major component of “Cold Start” (section 13.6.2) is simply reading the model weights from disk into memory). Sự lựa chọn của sự tuần tự hóa định dạng quyết định (như thế nào) nhanh chóng này việc tải có thể xảy ra. Tiêu chuẩn PyTorch torch.load() sử dụng Python’s pickle định dạng uses Python’s pickle format). Này cách tiếp cận là kém hiệu quả bởi vì nó yêu cầu CPU (để) hủy bỏ (unpickle) các đối tượng (từng) một (một), sao chép chúng vào bộ nhớ, và sau đó thường sao chép chúng một lần nữa (tới) GPU. (Cái) bộ nhớ việc ánh xạ giới thiệu cho trên-yêu cầu (on-demand) việc tải trong

13.10 Nút-Cấp độ Sự tối ưu hóa

Safetensors: (Cái) tên nhấn mạnh (emphasizes) an toàn (safety):
không giống như
Python’s
pickle định dạng,
safetensors không thể thực thi
tùy ý mã trong suốt sự giải-tuần tự hóa (deseri-alization), việc loại bỏ một lớp
của
bảo mật
các lỗ hổng (vulnerabilities)
nơi độc hại mô hình các tập tin có thể làm tổn hại (compromise) một việc phục vụ hệ thống.
Định dạng lưu trữ các tensor như
liền kề (raw) các byte với
một
tối thiểu
JSON tiêu đề (header),
việc kích hoạt
được ánh xạ-bộ nhớ
việc tải; trong cục bộ ví dụ
bên trên, đó con đường là 10× nhanh hơn (so với) pickle. Cho (việc) tự động mở rộng
việc phục vụ các hạm đội, này việc tải
tốc độ trực tiếp giảm thiểu lạnh
khởi động độ trễ: sự khác biệt
giữa một tải tốn
15 s và một tốn 1.5
s quyết định liệu mới các bản sao có thể hấp thụ lưu lượng truy cập
các đỉnh (nhọn)
trước khi
SLO
bị vi phạm (violated) (hay không). phần 13.6.3 cung cấp một nhanh hơn con đường ở đây cho một khác biệt lý do: nếu được tuần tự hóa các byte (đã) khớp (với) trong-bộ nhớ tensor bố cục (layout), ánh xạ tập tin cần không sự phân tích (cú pháp) (parsing) hay sao chép (tại tất cả). (Việc) xây dựng trên này không-sao chép (zero-copy) nguyên tắc, Safetensors34 là một tensor định dạng thiết kế đặc thù cho nhanh việc tải. Nó lưu trữ các tensor như (là) thô các byte với một tối thiểu JSON tiêu đề. Điều này kích hoạt không-sao chép việc tải: thô các byte trên đĩa được ánh xạ trực tiếp vào tensor bộ nhớ bộ đệm (this enables zero-copy loading: the raw bytes on disk are mapped directly into the tensor’s memory buffer). Ví dụ 13.4: Việc tải tốc độ: Safetensors so với Pickle Kịch bản: Một khởi động-lạnh bản sao phải tải một 5 GB Ổn định (Stable) Sự khuếch tán (Diffusion) v1.5 điểm kiểm tra trước khi nó có thể hấp thụ lưu lượng truy cập.
Sự phân tích: • Pickle con đường: PyTorch dựa trên-pickle bộ tải (loader) tốn 15 s trong này kịch bản bởi vì Python phải tái tạo (reconstruct) các đối tượng trước khi các tensor là (có thể) sử dụng. • Safetensors con đường: (Các) giống nhau các trọng số được lưu trữ với Safetensors tải trong 1.5 s, một 10× sự cải thiện (ment). Các hệ thống sự thấu hiểu: Với ánh xạ-bộ nhớ Safetensors các tập tin, việc tải tốc độ trở nên bị giới hạn chủ yếu bởi đĩa’s đọc tốc độ—ví dụ 3.5 GB/s trên cục bộ Gen3 NVMe—thay vì bởi CPU sự phân tích (cú pháp) chi phí hoạt động.
13.10.4 Việc lập hồ sơ (Profiling) việc phục vụ nút Sự tối ưu hóa mà không đo lường là phỏng đoán (guesswork). Hệ thống tính hiệu quả số liệu định nghĩa trong phương- trình 13.2 cung cấp mục tiêu: việc tối đa hóa phần (fraction) của đồng hồ-tường (wall-clock) thời gian bộ tăng tốc tiêu (dành) trên hữu ích tính toán. Dòng thời gian việc lập hồ sơ các công cụ như PyTorch Profiler hay NVIDIA Nsight Systems (nsys) làm (cho) đó mục tiêu (trở nên) (có thể) nhìn thấy bằng cách (việc) cho thấy chính xác chuỗi của các sự kiện trên CPU và GPU make that target visible by showing the exact sequence of events on the CPU and GPU). Một hữu ích dấu vết sự đọc (reading) là nút-thắt-cổ-chai-đầu-tiên. Trống các không gian trong GPU thanh (bar) nghĩa (là) nhàn rỗi phần cứng, thường bởi vì GPU chờ (đợi) cho CPU việc tiền xử lý hay đĩa I/O. Hàng ngàn của nhỏ xíu GPU các mảnh vụn (slivers) biểu thị (indicate) quá mức hạt nhân các sự khởi chạy và chỉ về phía toán tử sự hợp nhất hay đồ thị sự biên dịch. MemcpyHtoD các khối (blocks) phơi bày máy chủ-tới-thiết bị sự di chuyển; chẩn đoán câu hỏi là liệu những các sự truyền đó chồng chéo với tính toán hay chặn (block) nó (hay không). Dòng thời gian do đó chuyển đổi một mơ hồ (vague) lời phàn nàn (complaint) về chậm việc phục vụ thành một cụ thể ranh giới trong yêu cầu con đường.
Ví dụ 13.5: Việc lập hồ sơ vòng lặp Kịch bản: Một việc phục vụ nút có cao P99 độ trễ mặc dù (even though) trung bình bộ tăng tốc sự sử dụng trông có vẻ (có thể) chấp nhận , và một dấu vết của ấm (warm) các yêu cầu cho thấy lớn trống các khu vực (regions) trong bộ tăng tốc dòng thời gian giữa ngắn các hạt nhân.
Cách tiếp cận:
1. Thiết lập: Chạy một làm ấm (warmup), sau đó chụp mười tới năm mươi đại diện (representative) các yêu cầu trong Chrome Tracing, Nsight, hay thời gian chạy’s bộ lập hồ sơ (profiler).
2. Sự chẩn đoán: Tìm lớn nhất nhàn rỗi khoảng trống hay dài nhất chặn (blocking) sự kiện trong dấu vết.
3. Bản sửa lỗi (Fix): Áp dụng nhỏ nhất nhắm mục tiêu (targeted) bản sửa lỗi, như là sự hợp nhất cho hạt nhân-sự khởi chạy sự phân mảnh, việc ghim cho CPU tính cục bộ, không-sao chép việc tải cho sự khởi động, hay sự lập lịch các thay đổi cho máy chủ- thiết bị các sự ngừng trệ (stalls).
4. Sự xác minh (Verification): Chụp dấu vết (một lần) nữa và xác nhận rằng nhắm mục tiêu khoảng trống (đã) biến mất hay di chuyển. Các hệ thống bài học: Việc lập hồ sơ là đáng tin cậy (credible) chỉ khi tiếp theo dấu vết thay đổi trong mong đợi hướng (tion). Vòng lặp ngăn chặn sự tối ưu hóa (khỏi) (việc) trở thành một danh sách của các thủ thuật bị tách rời (detached) từ được đo lường các nút thắt cổ chai.
Bảng 13.21 là một quyết định hỗ trợ (aid) thay vì một danh sách kiểm tra: chọn kỹ thuật nó mục tiêu số liệu khớp (với) được đo lường nút thắt cổ chai, không (phải) hàng với lớn nhất điển hình lợi ích.

13. Mô hình Việc phục vụ

Bảng 13.21: Cấp độ-Nút Sự tối ưu hóa Tác động (Impact): Một quyết định ma trận cho việc lựa chọn sự tối ưu hóa các kỹ thuật. Cao-tác động các kỹ thuật như sự lượng tử hóa thường mang (theo) cao hơn sự triển khai các chi phí (sự hiệu chuẩn dữ liệu các yêu cầu), trong khi thuộc về kiến trúc các thay đổi như không-sao chép việc tải cung cấp ấn tượng (dramatic) các lợi ích cho cụ thể các số liệu (khởi động thời gian) với thấp nỗ lực, while architectural changes like zero-copy loading offer dramatic gains for specific metrics (startup time) with low effort).
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
Tới hạn-độ trễ các ứng dụng (apps) Hệ thống phân cấp (hierarchy) của tác động này hướng dẫn (nơi) nào (để) đầu tư kỹ thuật nỗ lực. Một phân lớp (layered) điểm kiểm tra giữ đó sự ưu tiên hóa (prioritization) buộc (tied) (với) việc phục vụ ngăn xếp, từ yêu cầu sự vận chuyển xuống (tới) hợp nhất các hạt nhân. Điểm kiểm tra 13.5: Sự tối ưu hóa hệ thống phân cấp Việc tối ưu hóa sự suy luận theo (sau) yêu cầu con đường từ (bên) ngoài vào (trong). Ngăn xếp có bốn các cấp độ. □Hệ thống cấp độ: (Bạn) Đã (từng) tối thiểu hóa mạng lưới vòng chuyến đi (round trips) và sự tuần tự hóa chi phí hoạt động (chưa)? (gRPC, dai dẳng các kết nối)). □Ứng dụng cấp độ: Bạn đang lập lô (batching) các yêu cầu hiệu quả? (Động việc lập lô)). □Mô hình cấp độ: (Có phải) mô hình biên dịch cho mục tiêu phần cứng? (TensorRT, ONNX Thời gian chạy)). □Hạt nhân cấp độ: (Có phải) các toán tử hợp nhất để tối thiểu hóa bộ nhớ băng thông? Sự tối ưu hóa các kỹ thuật kiểm tra (cho) đến nay (việc lập lô, thời gian chạy sự lựa chọn, độ chính xác sự điều chỉnh, đồ thị sự biên dịch) tập thể quyết định bao nhiêu hữu ích công việc một đơn việc phục vụ nút trích xuất (extracts) từ nó phần cứng collectively determine how much useful work a single serving node extracts from its hardware). (Cái) tiếp theo bước là (về mặt) kinh tế: việc quyết định bao nhiêu cơ sở hạ tầng được yêu cầu và tại gì tổng chi phí.
13.11 Tính kinh tế (Economics) và Việc lập kế hoạch Mọi sự tối ưu hóa kỹ thuật kiểm tra (cho) đến nay (việc lập lô, độ chính xác sự điều chỉnh, toán tử sự hợp nhất, đồ thị sự biên dịch) giảm thiểu một đơn con số: chi phí của một sự suy luận trên một máy reduces a single number: the cost of one inference on one machine). Sản xuất sự triển khai, tuy nhiên, yêu cầu (việc) trả lời một khác biệt câu hỏi: bao nhiêu máy, của (loại) gì, tại gì tổng chi phí. Một đội đạt được 1,200 hình ảnh/giây trên một V100 vẫn cần (để) biết liệu 8 V100 tại $3/giờ (cho) mỗi hay 24 T4 tại $0.53/giờ (cho) mỗi mang lại thấp hơn tổng chi phí của quyền sở hữu cho họ 5,000 QPS mục tiêu (hay không). Việc phục vụ các chi phí mở rộng quy mô (scale) với yêu cầu khối lượng (volume), không giống như sự đào tạo các chi phí mở rộng quy mô với tập dữ liệu kích thước và mô hình độ phức tạp). (Cái) công khai API giá cả sự nén (compression) hiển thị trong hình 13.2 minh họa này áp lực: khi mỗi-token các mức giá (prices) giảm (fall), lề (margin) trên mỗi sự suy luận co lại (shrinks), việc làm (cho) cơ sở hạ tầng tính hiệu quả (thành) một chính đòn bẩy cho (về mặt) kinh tế tính khả thi (viability).
13.11.1 Chi phí cho mỗi sự suy luận Chi phí cho mỗi sự suy luận phân rã (decomposes) thành bốn thành phần: tính toán thời gian (GPU hay CPU các chu kỳ tiêu thụ cho mỗi sự suy luận), bộ nhớ (bộ tăng tốc bộ nhớ yêu cầu để giữ mô hình các trọng số và các sự kích hoạt), dữ liệu sự truyền (mạng lưới băng thông cho yêu cầu và phản hồi các tải trọng (payloads)), và sự điều phối (orchestration) chi phí hoạt động (bộ- chứa thời gian chạy, tải việc cân bằng, và việc giám sát), memory, data transfer, and orchestration overhead). Cho GPU sự suy luận, thống trị chi phí thành phần chuyển dịch (shifts) với sự sử dụng. Tại cao sự sử dụng, tính toán thời gian thống trị bởi vì GPU luôn (stays) bận rộn việc xử lý các yêu cầu. Tại thấp sự sử dụng, bộ nhớ chi phí thống trị bởi vì GPU được dự trữ và tính tiền (billed) (thậm chí) ngay cả khi nhàn rỗi. Này sự phân biệt có ý nghĩa (matters) cho chi phí sự tối ưu hóa: việc cải thiện thông lượng giảm thiểu tính toán chi phí cho mỗi sự suy luận, trong khi việc cải thiện sự sử dụng giảm thiểu bộ nhớ sự lãng phí của nhàn rỗi phần cứng. Việc áp dụng khuôn khổ (cho) ResNet-50 cho thấy (như thế nào) hàng giờ giá (cả) và duy trì (sustained) thông lượng kết hợp thành chi phí cho mỗi sự suy luận.

13.11 Tính kinh tế và Việc lập kế hoạch Khăn ăn Toán học 13.10: ResNet-50: Chi phí sự phân tích
Bảng 13.22 so sánh hàng giờ chi phí, thông lượng, và mỗi-triệu-hình ảnh chi phí cho việc phục vụ ResNet-50 trên AWS (US-East, trên-yêu cầu việc định giá (pricing) trong 2026)):
Bảng 13.22: ResNet-50 đám mây sự suy luận chi phí sự so sánh: AWS hàng giờ chi phí, duy trì thông lượng, và kết quả chi phí cho một triệu các hình ảnh cho CPU, T4, và V100 các phiên bản (instances) trong này kịch bản, việc hiển thị (như thế nào) một cao hơn hàng giờ tỷ lệ (rate) có thể vẫn mang lại thấp hơn chi phí cho mỗi sự suy luận khi thông lượng tăng đủ.
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
$0.71 Các hệ thống sự thấu hiểu: T4 GPU phiên bản đạt được thấp nhất chi phí cho mỗi sự suy luận mặc dù cao hơn hàng giờ chi phí, bởi vì GPU thông lượng ấn tượng vượt quá CPU thông lượng. V100 là chỉ hiệu quả-chi phí tại rất cao duy trì lưu lượng truy cập nơi nó cao hơn thông lượng biện minh (cho) 5.8× giá sự gia tăng. Đám mây việc định giá dao động bởi khu vực và thay đổi qua thời gian; tham khảo hiện tại việc định giá cho sản xuất việc lập kế hoạch.
13.11.2 GPU so với CPU tính kinh tế Trong làm (worked) AWS ví dụ bên trên, GPU các phiên bản tốn nhiều hơn cho mỗi giờ nhưng cung cấp nhiều cao hơn song song thông lượng. Điểm giao nhau (crossover point) phụ thuộc vào mô hình các đặc điểm và độ trễ các yêu cầu. CPU sự suy luận có (về mặt) kinh tế ý nghĩa cho nhỏ các mô hình với ít các tham số và đơn giản các toán tử, khi độ trễ các yêu cầu là nới lỏng (hàng trăm của mili giây (có thể) chấp nhận ), khi yêu cầu khối lượng là thấp hay cao có thể thay đổi (việc làm (cho) GPU sự dự trữ lãng phí), hay khi mô hình’s các toán tử không song song hóa tốt, when request volume is low or highly variable, or when the model’s operations do not parallelize well). GPU sự suy luận là hấp dẫn khi các mô hình là lớn với thân thiện-song song các toán tử, độ trễ các yêu cầu là nghiêm ngặt (strict) (hàng chục của mili giây), yêu cầu khối lượng là cao và nhất quán đủ để duy trì sự sử dụng, và việc lập lô có thể khấu hao cho mỗi-sự suy luận chi phí hoạt động của GPU hạt nhân các sự khởi chạy, request volume is high and consistent enough to sustain utilization, and batching can amortize the per-inference overhead of GPU kernel launches). Bên ngoài ổn định-trạng thái các chi phí, khởi động thời gian ảnh hưởng (tới) (việc) mở rộng quy mô tính kinh tế. CPU các phiên bản điển hình khởi động trong 30–60 giây trong khi GPU các phiên bản tốn 2–5 phút bao gồm trình điều khiển sự khởi tạo, mô hình việc tải, và làm ấm. Cho có thể thay đổi lưu lượng truy cập các mẫu, này khởi động độ trễ có thể (là) quan trọng hơn (so với) chi phí cho mỗi sự suy luận. Nếu lưu lượng truy cập các đỉnh (nhọn) đến nhanh hơn (so với) GPU các phiên bản có thể mở rộng quy mô, độ trễ SLO sẽ bị vi phạm mặc dù (việc) có đủ cuối cùng (eventual) công suất. Này sự bất đối xứng (asymmetry) gợi ý khác biệt việc mở rộng quy mô các chiến lược nơi CPU các phiên bản kích hoạt phản ứng (việc) mở rộng quy mô bằng cách (việc) phản hồi (tới) hiện tại nhu cầu trong khi GPU các phiên bản thường yêu cầu dự đoán (việc) mở rộng quy mô bằng cách (việc) dự liệu (provision-ing) dựa trên dự đoán trước nhu cầu. Cho có tính bùng nổ (bursty) các khối lượng công việc, một lai cách tiếp cận sử dụng luôn-bật GPU công suất cho cơ sở (baseline) tải cộng CPU tràn (overflow) công suất cho các đỉnh (nhọn), (việc) đánh đổi cao hơn mỗi-sự suy luận chi phí trong suốt các đỉnh (nhọn) cho tốt hơn sự phản hồi (responsiveness). Này GPU+CPU lai là một phiên bản (instance) của rộng hơn lai kiến trúc các mẫu lập danh mục (cataloged) trong phần 2.10, nơi đào tạo-phục vụ sự chia tách và phân cấp (hierarchical) (việc) xử lý các mẫu cũng kết hợp các mô hình để cân bằng chi phí, độ trễ, và khả năng.
13.11.3 Công suất việc lập kế hoạch GPU so với CPU quyết định thiết lập chi phí cho mỗi sự suy luận, nhưng (việc) quyết định bao nhiêu cơ sở hạ- tầng để dự liệu (provision) yêu cầu (việc) kết hợp chi phí sự phân tích với hàng đợi lý thuyết các nền tảng từ phần 13.5. Công suất việc lập kế hoạch chuyển đổi (translates) ba đầu vào thành cơ sở hạ tầng các đặc tả: lưu lượng truy cập các mẫu (đỉnh yêu cầu tỷ lệ, hàng ngày/hàng tuần các chu kỳ, sự tăng trưởng các sự dự phóng (projections)), độ trễ SLO (p50, p95, p99 các mục tiêu), và mô hình các đặc điểm (sự suy luận thời gian sự phân phối tại đa dạng lô các kích thước), latency SLOs, and model characteristics). (Cái) làm ví dụ trong phần 13.5 minh họa hoàn chỉnh quy trình làm việc: (việc) bắt đầu từ một 50 ms p99 SLO và 5,000 QPS mục tiêu, (việc) suy ra (deriving) thận trọng M/M/1 an toàn sự sử dụng ngưỡng của 54 phần trăm từ phương trình 13.6, và (việc) quyết định GPU số lượng với khoảng trống (headroom) của 12 V100. Sản xuất các hệ thống điển hình dự liệu cho đỉnh tải cộng 30 phần trăm khoảng trống, (việc) sử dụng sự tự động mở rộng để giảm thiểu các chi phí trong suốt thấp-lưu lượng truy cập các khoảng thời gian (periods) trong khi (việc) đáp ứng độ trễ các mục tiêu trong suốt các đỉnh (nhọn); Chương 14 phát triển hoạt động chính sách lớp xung quanh những việc phục vụ các tính toán này. (Cái) chính sự thấu hiểu từ công suất việc lập kế hoạch là (rằng) thông lượng các con số là ý nghĩa chỉ khi ghép nối với độ trễ các sự đảm bảo: như hợp lệ-QPS việc kế toán (accounting) trong phần 13.5 (đã) thiết lập, công suất phải được định kích thước cho các yêu cầu thực sự đáp ứng SLO, không (phải) cho thô yêu cầu khối lượng.
13.11.4 Sản xuất trường hợp nghiên cứu: Việc phục vụ 8-tỷ-tham số Llama 3 (Cái) thống trị chi phí trong (việc) phục vụ một lớn ngôn ngữ mô hình là không (phải) tính toán mà (là) KV-bộ đệm bộ nhớ, và hình 13.7 cho thấy tại sao. (Được) vẽ (Plotted) tại 70-tỷ-tham số quy mô để khuếch đại hiệu ứng, bộ đệm tăng trưởng tuyến tính với ngữ cảnh độ dài và lô kích thước cho đến khi dài các ngữ cảnh đẩy (thậm chí) ngay cả một H100 vào nó Hết- Bộ nhớ (out-of-memory) vùng. (Cái) 8-tỷ-tham số Llama 3 hồ sơ phân tích trong phần còn lại của này phần tuân theo (obeys) giống nhau vật lý (physics) với nhiều hơn khoảng trống, (việc) làm nó (thành) một khối lượng công việc một kỹ sư có thể vừa vặn trên một GPU và lý luận về cuối (tới) cuối.
Hình 13.7: (Cái) KV-Bộ đệm Sự bùng nổ: Bộ nhớ sự sử dụng so với Ngữ cảnh Độ dài cho một 70-tỷ-tham số-lớp mô hình. Giả định 80 các lớp, 𝑑model = 8192, FP16 KV bộ đệm, GQA (8×) (Assumes 80 layers, 𝑑model = 8192, FP16 KV cache, GQA (8×)). (Cái) tuyến tính sự tăng trưởng của (Cái) Khóa-Giá trị bộ đệm (việc lưu trữ sự chú ý lịch sử) nhanh chóng tiêu thụ sẵn GPU bộ nhớ (đỏ nét đứt (dashed) đường) quickly consumes available GPU memory (red dashed line)). Cho lô kích thước 32 (tím), hệ thống chạm (vào) ‘OOM Vùng’ tại chỉ 8k ngữ cảnh độ dài, (việc) ép buộc một sự đánh đổi giữa lô kích thước (thông lượng) và ngữ cảnh cửa sổ (khả năng), the system hits the ‘OOM Zone’ at just 8k context length, forcing a trade-off between batch size (throughput) and context window (capability)). (Cái) tuyến tính sự tăng trưởng của KV bộ đệm với chuỗi độ dài ép buộc một cứng sự đánh đổi: để hỗ trợ dài hơn các ngữ cảnh (32k+), chúng ta phải giảm thiểu lô kích thước, (điều) mà (đến) lượt (nó) (in turn) giết chết thông lượng tính hiệu quả, we must reduce batch size, which in turn kills throughput efficiency).
13.11.4.1 Khối lượng công việc hồ sơ (Các) cố định khối lượng công việc các giả định bên dưới định nghĩa tham chiếu trường hợp sử dụng xuyên suốt độ trễ, bộ nhớ, và tính kinh tế các tính toán trong này phần; với nhau, chúng giới hạn (bound) sự phân tích theo (sau). • Mô hình: 8-tỷ-tham số Llama 3 (lượng tử hóa thành 4-bit (việc) sử dụng nhận thức-sự kích hoạt trọng số sự lượng- tử hóa (AWQ); xem Chương 10 cho sự lượng tử hóa các kỹ thuật); see Chapter 10 for quantization techniques)). • Phần cứng: 1× NVIDIA H100 SXM5 GPU (80 GB HBM3, 3.35 TB/s băng thông) (Choquette 2023) (Hardware: 1× NVIDIA H100 SXM5 GPU (80 GB HBM3, 3.35 TB/s bandwidth) (Choquette 2023)). • Yêu cầu các đặc điểm: 1,000-token đầu vào lời nhắc (Tiền điền), 256-token tạo ra phản hồi (Giải mã), 256-token generated response (Decode)). • Mục tiêu SLO: TTFT < 200 ms, TPOT < 20 ms. Những các giả định này làm (cho) trường hợp nghiên cứu hẹp đủ để tính toán trong khi (việc) bảo tồn hai việc phục vụ các sự ép buộc có ý nghĩa (matter) nhất: tiền điền ngân sách (budget) cho thời gian (tới) đầu tiên token và giải mã ngân sách cho mỗi tạo ra token.

13.11 Tính kinh tế và Việc lập kế hoạch
13.11.4.2 Độ trễ sự tháo dỡ (deconstruction) (Cái) cuối-tới-cuối yêu cầu độ trễ được chi phối bởi hai-giai đoạn sự thực thi mô hình của tự hồi quy các transformer, (việc) áp dụng TTFT và TPOT các số liệu định nghĩa trong phần 13.8.1. Tiền điền quyết định liệu người dùng thấy một lời nhắc phản hồi nhanh chóng (hay không); giải mã quyết định liệu tạo ra luồng (stream) tiếp tục (keeps) di chuyển sau khi nó bắt đầu (hay không). Tiền điền giai đoạn (thời gian tới đầu tiên token) Mô hình xử lý 1,000-token lời nhắc song song The model processes the 1,000-token prompt in parallel). Trong này kịch bản, H100 tiền điền tỷ lệ được đặt thành xấp xỉ 10,000 token/s: 𝑇prefill = 1000 token ÷ 10,000 token/s = 100 ms. (Việc) tính toán (Accounting) cho 20 ms của hệ thống chi phí hoạt động (mạng lưới xâm nhập (ingress), sự token hóa), TTFT là 120 ms, thoải mái bên trong 200 ms SLO, the TTFT is 120 ms, comfortably within the 200 ms SLO). Giải mã giai đoạn (thời gian cho mỗi đầu ra token) Mô hình tạo ra 256 các token tuần tự The model generates 256 tokens sequentially). Này giai đoạn là bị giới hạn-bộ nhớ-băng thông—giống nhau bị giới hạn-IO mẫu thấy trong DLRM nhúng các tra cứu (lookups) (phần 13.4.2), nhưng tại một lớn hơn quy mô: hệ thống phải đọc toàn bộ 3.5 GB trọng số tensor từ VRAM để tạo ra một đơn token (This phase is memory-bandwidth bound—the same IO-bound pattern seen in the DLRM embedding lookups (section 13.4.2), but at a larger scale: the system must read the entire 3.5 GB weight tensor from VRAM to generate a single token). Các hệ thống Góc nhìn 13.13: (Cái) vật lý (physics) của token sự tạo ra Nhớ lại năng lượng-sự di chuyển bất biến (invariant) định lượng (quantified) trong bảng 4.1: (việc) di chuyển một bit là 100–1,000× nhiều hơn đắt đỏ (so với) (việc) tính toán trên nó. Trong (Cái) Giải mã Giai đoạn, này định luật quyết định thuộc về vật lý “chi phí cho mỗi từ”. Vật lý: Bởi vì giải mã giai đoạn có một số học (arithmetic) cường độ của ≈1 FLOP/byte (chúng ta phải đọc mọi trọng số chỉ để tạo ra một token), hiệu suất nghiêm ngặt (strictly) giới hạn bởi bộ nhớ băng thông (BW), không (phải) tính toán (Physics: Because the decode phase has an arithmetic intensity of ≈1 FLOP/byte (we must read every weight just to generate one token), performance is strictly limited by memory bandwidth (BW), not compute). Này mối quan hệ được nắm bắt (captured) trong phương trình 13.18:
𝑇token ≈
𝐷vol
BWmemory
(13.18) Hệ quả (Implication): Mọi token sự tạo ra trả một đồ sộ (massive) “năng lượng thuế (tax)” để di chuyển mô hình’s logic từ HBM vào tính toán các thanh ghi (registers). Cho sự so sánh, trên một A100 80 GB (2.04 TB/s HBM2e), một 8-tỷ-tham số Llama 3 mô hình (4.1 GB INT4) tạo ra các token tại ≈2.0 ms cho mỗi token, an 8-billion-parameter Llama 3 model (4.1 GB INT4) generates tokens at ≈2.0 ms per token). Khi giải mã vẫn giới hạn-băng thông, (việc) thêm nhiều hơn tính toán các lõi mang lại (rất) ít độ trễ sự cải thiện; nhanh hơn bộ nhớ (Vật lý), nhỏ hơn các mô hình (Thuật toán), hay tốt hơn việc lập lô và bộ đệm quản lý thay đổi giới hạn, smaller models (Algorithm), or better batching and cache management change the bound). Việc đọc 4.1 GB trọng số tensor tại 3.35 TB/s thiết lập thuộc về lý thuyết sàn (floor): 𝑇token ≈1.2 ms. Việc tính toán cho hạt nhân sự khởi chạy chi phí hoạt động, sự chú ý tính toán, và một thận trọng (conservative) sản xuất an toàn lề (margin), hiện thực hóa (realized) 𝑇token là xấp xỉ 1.53 ms. Việc tạo ra tất cả 256 token do đó tốn 256 token ×
1.53 ms = 0.39 s, và kết quả TPOT của 1.53 ms ngồi (sits) tốt bên trong 20 ms “tính trôi chảy (fluidity)” SLO.
13.11.4.3 Bộ nhớ và thông lượng Với 4-bit các trọng số chiếm giữ (occupying) 4.1 GB, (phần) còn lại ~75 GB là có sẵn cho KV Bộ đệm, PagedAttention cấp phát với gần-không sự phân mảnh. Mỗi token yêu cầu xấp xỉ 0.033 MB của INT4 KV bộ đệm trong 8-tỷ-tham số Llama 3 cấu hình, vì (Được) Nhóm Truy vấn Sự chú ý giảm thiểu KV-đầu (head) lưu trữ so với (relative to) đầy (đủ) nhiều-đầu sự chú ý tại FP16. Việc chia 72 GB của bộ đệm bởi đó mỗi-token chi phí mang lại công suất cho ≈2.2 triệu token, do đó tại 1,256 token GPU có thể giữ một đồng thời lô kích thước của ~1749 yêu cầu.
13.11.4.4 Đơn vị tính kinh tế Xem xét một đại diện H100 SXM5 (tiền) thuê (rental) chi phí của xấp xỉ $3/giờ. Bị giới hạn-tiền điền sự tiếp- nhận (admissions) (đi) đến (come to) 10,000 token/s chia bởi 1,000 token = 10 req/s. Điều này là bên dưới KV-sự cư trú (residency) giới hạn của 1749 yêu cầu / 0.44 s ≈3931 req/s, do đó đầy-yêu cầu thông lượng là 10 req/s × 3,600 s/hr × 1,256 token ≈45.2 triệu token/giờ. Việc chia hàng giờ chi phí bởi đó thông lượng (mang) lại một chi phí cho mỗi triệu token của $3/giờ / 45.2 triệu token/giờ ≈$0.066/triệu token. Sự phân tích này làm nổi bật rằng cho các LLM, bộ nhớ công suất (kích thước của KV bộ đệm) quyết định tối đa đồng thời sự cư trú (residency), trong khi tiền điền tính toán và giải mã băng thông quyết định hiện thực hóa determines the maximum concurrent residency, while prefill compute and decode bandwidth determine realized)

13. Mô hình Việc phục vụ

token thông lượng và chi phí dưới một cụ thể lưu lượng truy cập kết hợp (mix). Bộ nhớ băng thông vẫn (là) chính yếu tố quyết định (determinant) của giải mã độ trễ. Này trường hợp nghiên cứu áp dụng cốt lõi (core) các nguyên tắc phát triển xuyên suốt này chương: độ trễ các ngân sách phân rã thành tiền điền và giải mã các giai đoạn, hàng đợi lý thuyết chi phối lô việc định kích thước và công suất việc lập kế hoạch, và phần cứng các sự ép buộc trong hình thức của bộ nhớ băng thông và công suất quyết định có thể đạt được hiệu suất và chi phí. (Cái) định lượng (quantitative) khuôn khổ thiết lập ở đây kích hoạt có nguyên tắc kỹ thuật các quyết định, nhưng chỉ khi áp dụng chính xác. Phổ biến các sự ngộ nhận (misconceptions) khiến (thậm chí) ngay cả giàu kinh nghiệm các kỹ sư (việc) áp dụng sai (misapply) những các nguyên tắc này trong thực tế.
13.12 Các ngụy biện (Fallacies) và Các cạm bẫy (Pitfalls) Việc phục vụ đảo ngược (inverts) đào tạo các sự ưu tiên trong các cách vi phạm các trực giác (intuitions) từ lô việc xử lý. (Cái) phi tuyến mối quan hệ giữa sự sử dụng và độ trễ, ẩn các chi phí của việc tiền xử lý, và im lặng sự thất bại các chế độ của đào tạo-phục vụ sự sai lệch (skew) gây ra bị vi phạm SLO, lãng phí sự tối ưu hóa nỗ lực, và độ chính xác (accuracy) sự xuống cấp (degradation) vô hình (invisible) (với) tiêu chuẩn việc giám sát. Ngụy biện: Việc giảm thiểu mô hình sự suy luận độ trễ theo tỷ lệ (proportionally) giảm thiểu người dùng-nhận thức (user-perceived) độ trễ. Các kỹ sư người tối ưu hóa mô hình sự suy luận mong đợi theo tỷ lệ sự cải thiện trong người dùng-nhận thức độ trễ, nhưng việc phục vụ các hệ thống giới thiệu độ trễ các nguồn vắng mặt từ ngoại tuyến các điểm chuẩn. Dưới tải, hàng đợi sự chậm trễ (delay) thống trị: phương trình 13.5 cho thấy rằng tại 80 phần trăm sự sử dụng với 5 ms dịch vụ thời gian, trung bình chờ (đợi) thời gian là 20 ms (thậm chí) trước khi sự suy luận bắt đầu. Việc giảm thiểu sự suy luận từ 5 ms xuống 2 ms thay đổi dịch vụ thời gian nhưng cũng dịch chuyển sự sử dụng từ 80 phần trăm xuống 32 phần trăm, (việc) giảm thiểu việc xếp hàng đợi chờ (đợi) từ 20 ms xuống 0.9 ms, một 21.2× việc xếp hàng đợi sự cải thiện làm lùn đi (dwarfs) 3 ms sự suy luận lợi ích. Này phi tuyến sự tương tác giữa sự suy luận tốc độ và việc xếp hàng đợi hành vi nghĩa (là) cấp độ-hệ thống sự tăng tốc (25 ms →2.9 ms, hay 8.5×) xa vượt qua cấp độ-mô hình sự tăng tốc (5 ms →2 ms, hay 2.5×) (This nonlinear interaction between inference speed and queuing behavior means the system-level speedup (25 ms →2.9 ms, or 8.5×) far exceeds the model-level speedup (5 ms →2 ms, or 2.5×)). Ngược lại, các đội người giảm thiểu sự suy luận bởi chỉ 20 phần trăm tại cao sự sử dụng thấy không đáng kể (negligible) đối mặt-người dùng sự cải thiện bởi vì việc xếp hàng đợi vẫn thống trị. Việc phục vụ sự tối ưu hóa yêu cầu (việc) phân tích hoàn chỉnh độ trễ ngân sách, bao gồm sự tuần tự hóa, việc xếp hàng đợi, việc tiền xử lý, và việc hậu xử lý, dưới thực tế tải các điều kiện thay vì (việc) lập hồ sơ (profiling) sự suy luận độ trễ trong cô lập (isolation). Cạm bẫy: Việc chạy việc phục vụ cơ sở hạ tầng tại cao sự sử dụng để tối đa hóa chi phí tính hiệu quả. Các đội nhắm mục tiêu (target) 90 phần trăm sự sử dụng để tối thiểu hóa nhàn rỗi công suất. Trong sản xuất, độ trễ xuống cấp (degrades) phi tuyến khi sự sử dụng tiếp cận công suất. Phương trình 13.5 cho thấy rằng tại 90 phần trăm sự sử dụng, trung bình thời gian trong hệ thống đạt (đến) 10× dịch vụ thời gian. Việc di chuyển từ 70 phần trăm (tới) 90 phần trăm sự sử dụng cắt giảm cơ sở hạ tầng các chi phí bởi 22.2 phần trăm nhưng (nhân) ba (triples) trung bình độ trễ. Cho một 5 ms sự suy luận dịch vụ, p99 độ trễ nhảy từ ~76.7 ms (tới) ~230 ms (M/M/1 mô hình)). Các hệ thống dự liệu cho trung bình tải vi phạm SLO chính xác khi lưu lượng truy cập gia tăng trong suốt tới hạn-doanh nghiệp các khoảng thời gian. Sản xuất các hệ thống nhắm mục tiêu 60 tới 70 phần trăm sự sử dụng tại đỉnh tải duy trì độ trễ khoảng trống (cần) thiết để hấp thụ lưu lượng truy cập các đỉnh (nhọn). Ngụy biện: Đào tạo độ chính xác đảm bảo (guarantees) việc phục vụ độ chính xác. Các kỹ sư giả định giống hệt (identical) mô hình các trọng số bảo tồn (preserve) (tập hợp) xác thực (set) hiệu suất. Trong sản xuất, việc tiền xử lý các sự khác biệt im lặng dịch chuyển các đầu vào (ra) ngoài đào tạo sự phân phối. Phần 13.6.1 cho thấy (như thế nào) đào tạo-phục vụ sự sai lệch (skew) gây ra độ chính xác sự xuống cấp mặc dù giống hệt các trọng số: PIL so với OpenCV đổi kích thước sự nội suy (interpolation) đơn độc có thể dịch chuyển độ chính xác bởi 0.5–1 phần trăm các điểm, FP64 so với FP32 sự chuẩn hóa sản xuất khác biệt các giá trị, hay đặc trưng tính toán thời gian thay đổi. Một mô hình đạt được 95 phần trăm sự xác thực độ chính xác rớt (drops) (xuống) 90 phần trăm trong sản xuất từ những việc tiền xử lý sự không khớp (mismatches) này, một 5 phần trăm-điểm mất mát vô hình (đối với) độ trễ việc giám sát. Tiêu chuẩn việc giám sát việc kiểm tra các ngoại lệ và độ trễ các sự vi phạm (violations) thất bại (trong việc) phát hiện này im lặng sự xuống cấp. Sản xuất các hệ thống yêu cầu (hoặc là) giống hệt việc tiền xử lý mã (code) cho sự đào tạo và việc phục vụ, hay thống kê việc giám sát việc so sánh đầu vào các sự phân phối để bắt trôi dạt (drift) trước khi độ chính xác xuống cấp. Cạm bẫy: Việc sử dụng trung bình độ trễ để đánh giá (evaluate) việc phục vụ hệ thống hiệu suất. Các kỹ sư giám sát trung bình độ trễ bởi vì nó xu hướng (trends) trơn tru và là đơn giản để tính toán. Trong sản xuất, các (số) trung bình (averages) che giấu chậm nhất các yêu cầu quyết định người dùng sự hài lòng (satisfaction). Như phần 13.5.5 minh họa, tại 70 phần trăm sự sử dụng với 5 ms dịch vụ thời gian, trung bình độ trễ là 16.7 ms nhưng p99 đạt (đến) 76.7 ms, một 4.6× khoảng trống vô hình (đối với) dựa trên-trung bình việc giám sát. Các đội tối ưu hóa trung bình độ trễ bỏ lỡ (miss) đuôi (tail) quyết định người dùng sự hài lòng: 1 phần trăm của những người dùng trải nghiệm 76.7 ms các sự chậm trễ thường tạo ra giá trị nhất các giao dịch (transactions). Sản xuất SLO chỉ định (specify) (phần) bách phân (percentile) các mục tiêu (p95, p99) chính xác bởi vì các (số) trung bình che đậy (mask) đuôi hành vi precisely because averages mask tail behavior).

13.13 Tóm tắt Ngụy biện: Lớn hơn việc phục vụ các lô luôn luôn cải thiện thông lượng mà không (làm) ảnh hưởng độ trễ SLO. Các kỹ sư tối đa hóa lô kích thước (việc) giả định GPU sự bão hòa (saturation) cải thiện chi phí tính hiệu quả dưới sản xuất tải. Trong việc phục vụ các hệ thống, tuy nhiên, việc lập lô giới thiệu một độ trễ-thông lượng sự đánh đổi chi phối bởi việc xếp hàng đợi động lực (dynamics) vắng mặt từ ngoại tuyến các điểm chuẩn. Việc tích lũy (Accumulating) các yêu cầu thành lớn hơn các lô gia tăng chờ (đợi) thời gian cho sớm người đến (arrivals): một lô cửa sổ của 10 ms có nghĩa (là) đầu tiên yêu cầu chờ (đợi) 10 ms trước khi sự suy luận bắt đầu, trực tiếp thêm vào p99 độ trễ. Trong đại diện ResNet-50/V100 kịch bản sử dụng (sớm) hơn (earlier), việc gia tăng lô kích thước từ 16 lên 32 cải thiện thông lượng chỉ 12 phần trăm nhưng gần như nhân đôi mỗi-lô sự suy luận thời gian từ 14 ms lên 25 ms, và có thể thay đổi đầu vào các kích thước bên trong một lô có thể tạo ra việc đệm (padding) chi phí hoạt động lãng phí tính toán trên (việc) đệm các token. Phần 13.7.3 cho thấy tại sao, cho chặt chẽ (tight) p99 các mục tiêu, lớn hơn lô các kích thước có thể vi phạm SLO khi lô sự hình thành sự chậm trễ cộng (việc) được gia tăng mỗi-lô sự suy luận thời gian vượt qua độ trễ ngân sách. Việc phục vụ lô sự tối ưu hóa yêu cầu chung (jointly) việc điều chỉnh lô kích thước, lô hết thời gian, và tính đồng thời chống lại độ trễ SLO dưới thực tế lưu lượng truy cập các mẫu, không (phải) (việc) tối đa hóa thông lượng trong sự cô lập. Cạm bẫy: Việc hiệu chuẩn lượng tử hóa các mô hình với đào tạo dữ liệu thay vì sản xuất lưu lượng truy cập. Các đội hiệu chuẩn với đào tạo dữ liệu bởi vì nó là dễ dàng (readily) có sẵn và (đã) tạo ra sự xác thực độ chính xác. Trong sản xuất, lưu lượng truy cập sự phân phối thường khác biệt (so) với đào tạo dữ liệu, việc làm (cho) sự hiệu chuẩn tỷ lệ hệ số (trở nên) kém tối ưu (suboptimal). Sau-sự đào tạo sự lượng tử hóa quyết định INT8 tỷ lệ hệ số bằng cách (việc) đo lường sự kích hoạt phạm vi (ranges) trên sự hiệu chuẩn dữ liệu, nhưng điều này giả định sản xuất các đầu vào khớp (với) sự hiệu chuẩn sự phân phối. Một sản xuất hệ thống đạt được 76.1 phần trăm độ chính xác trên được hiệu chuẩn-ImageNet INT8 rớt (xuống) 72.9 phần trăm, một 3.2 phần trăm-điểm sự mất mát, khi phục vụ hoang dã máy ảnh các hình ảnh với khác biệt sự chiếu sáng và các nền. Chương 10 cho thấy sự lượng tử hóa lỗi (error) tỷ lệ thuận (scales) với sự kích hoạt phạm vi: sự hiệu chuẩn sai (miscalibration) khuếch đại (amplifies) các lỗi chính xác trên ngoài-sự phân phối các đầu vào nơi các sự kích hoạt vượt quá hiệu chuẩn các phạm vi. Hiệu quả sự lượng tử hóa là dữ liệu-thuật toán cùng-thiết kế (co-design): nén mô hình phải được hiệu chuẩn chống lại đại diện các mẫu của thực tế việc phục vụ lưu lượng truy cập, không (phải) sự thuận tiện dữ liệu. Ngụy biện: Lạnh khởi động độ trễ chỉ có ý nghĩa (matters) cho đầu tiên yêu cầu. Các kỹ sư tối ưu hóa ổn định-trạng thái độ trễ (việc) giả định (phần) lớn các yêu cầu đụng (hit) ấm các phiên bản. Trong sản xuất, lạnh (các sự) khởi động cộng dồn (compound) trong suốt các sự kiện có ý nghĩa nhất: lưu lượng truy cập các đỉnh (nhọn) yêu cầu sự tăng-quy mô, các sự triển khai tung ra (rolling out) mới các phiên bản, và sự phục hồi (recovery) từ phiên bản các sự thất bại. Phần 13.6.2 (trình bày) chi tiết giải phẫu học (anatomy) của lạnh khởi động: TensorRT sự biên dịch đơn độc tốn 30 s cho mỗi phiên bản. Trong suốt một lưu lượng truy cập đỉnh (nhọn) yêu cầu 10 mới các phiên bản, tổng (aggregate) khởi động-lạnh công việc đạt (đến) 300 phiên bản-giây (instance-seconds); nếu các phiên bản ấm (lên) song song, mới công suất trở nên (trở nên) hữu ích sau khoảng 30 s. Tệ hơn, các yêu cầu đụng lạnh các phiên bản trải nghiệm 500 ms độ trễ so với 5 ms ổn định-trạng thái, một 100× sự xuống cấp vi phạm SLO chính xác khi lưu lượng truy cập là (cao) nhất. Các hệ thống phớt lờ lạnh khởi động đáp ứng SLO trong suốt ổn định trạng thái nhưng thất bại trong suốt tăng-quy mô các sự kiện và sự triển khai các cửa sổ khi (độ) tin cậy (reliability) có ý nghĩa nhất. Cạm bẫy: Việc mở rộng quy mô mà không một ấm-nhóm (warm-pool) hay theo giai đoạn-việc tải (staged-loading) ngân sách. Sự tự động mở rộng các chính sách (đếm) chỉ ổn định-trạng thái các bản sao (đánh giá) thấp (underestimate) công suất yêu cầu trong suốt lưu lượng truy cập các đỉnh (nhọn) và các sự triển khai. Việc phục vụ các hệ thống cần ấm nhóm, theo giai đoạn mô hình việc tải, hay tiếp nhận sự kiểm soát sao cho mới các bản sao trở nên (trở nên) hữu ích trước khi người dùng các yêu cầu phụ thuộc vào chúng, staged model loading, or admission control so that new replicas become useful before user requests depend on them). Ngân sách nên bao gồm sự biên dịch, trọng số việc tải, bộ đệm sự khởi tạo, và sức khỏe-việc kiểm tra thời gian, bởi vì những các bước đó quyết định liệu (việc) mở rộng quy mô (scale-out) thêm công suất hay thêm một khác nguồn của đuôi độ trễ.
13.13 Tóm tắt Việc phục vụ đánh dấu (marks) sự chuyển tiếp (transition) từ mô hình phát triển sang sản xuất sự triển khai, nơi sự tối- ưu hóa sự ưu tiên (đã) chi phối đào tạo phải đảo ngược. (Cái) sự dịch chuyển từ thông lượng sự tối đa hóa sang độ trễ sự tối thiểu hóa biến đổi mọi hệ thống thiết kế quyết định. (Cái) hàng đợi lý thuyết các nền tảng thiết lập ở đây tiết lộ (reveal) tại sao này sự đảo ngược là không (phải) (chỉ) đơn thuần một thay đổi trong các số liệu mà (là) một thay đổi trong chi phối (governing) toán học. (Cái) phi tuyến mối quan hệ giữa sự sử dụng và độ trễ có nghĩa là các hệ thống hành xử tốt tại vừa phải (moderate) tải có thể bất thình lình (suddenly) vi phạm SLO khi lưu lượng truy cập gia tăng khiêm tốn. Little’s Định luật và M/M/1 chờ (đợi) thời gian các phương trình cung cấp định lượng nền tảng cho công suất việc lập kế hoạch, (việc) thay thế dựa trên-trực giác việc dự liệu bằng kỹ thuật sự nghiêm ngặt (rigor). Hiệu quả việc phục vụ sự tối ưu hóa yêu cầu (việc) hiểu hoàn chỉnh yêu cầu con đường thay vì (việc) tập trung độc quyền vào mô hình sự suy luận. Giao diện các giao thức (protocols) như gRPC và hiệu quả sự tuần tự hóa các định dạng tối thiểu hóa “thuế” của dữ liệu sự di chuyển, trong khi việc tiền xử lý thường tiêu thụ 45 tới 70 phần trăm của tổng độ trễ khi sự suy luận chạy trên tối ưu hóa các bộ tăng tốc. (Các) quy mô-micro giây các chi phí hoạt động

13. Mô hình Việc phục vụ

nhận diện bởi Barroso, Patterson, và các đồng nghiệp giải thích tại sao việc phục vụ độ trễ thường vượt quá tổng của đo lường phần nó, và tại sao cấp độ-hệ thống sự tối ưu hóa có ý nghĩa nhiều (bằng) như mô hình sự tối ưu hóa. Đào tạo-phục vụ sự sai lệch (skew) đại diện (cho) một khác chiều (dimension) của độ phức tạp này, im lặng (việc) làm xuống cấp độ chính xác khi việc tiền xử lý logic khác biệt giữa đào tạo và sản xuất các môi trường trong các cách truyền thống việc kiểm thử không thể phát hiện. (Cái) lưu lượng truy cập mẫu sự phân tích tiết lộ (như thế nào) sự triển khai mô hình lựa chọn trong Chương 2 định hình (shapes) mọi việc phục vụ quyết định (ở) hạ nguồn (downstream). Máy chủ các khối lượng công việc với Poisson các sự đến tối ưu hóa động việc lập lô các cửa sổ, tự trị các phương tiện với truyền phát cảm biến dữ liệu yêu cầu đồng bộ hóa lô sự hình thành, và di động các ứng dụng với người dùng-đơn (single-user) các mẫu loại bỏ việc lập lô hoàn toàn. Mỗi mẫu là một trực tiếp hệ quả (consequence) của vật lý các sự ép buộc (năng lượng bức tường, bộ nhớ bức tường, ánh sáng rào cản (barrier)) (đã) tạo ra bốn các mô hình trong (lần) đầu tiên nơi that created the four paradigms in the first place). (Các) MLPerf các kịch bản mã hóa (codify) những các mẫu này cho được tiêu chuẩn hóa việc điểm chuẩn, (việc) kết nối việc phục vụ các nguyên tắc thiết lập ở đây (với) đo lường các khuôn khổ khám phá trong Chương 12. Cấp độ-nút sự tối ưu hóa các kỹ thuật (đồ thị sự biên dịch, toán tử sự hợp nhất, và hệ thống việc lập hồ- sơ (profil-ing)) làm cầu nối khoảng trống giữa cấp độ-mô hình các quyết định và phần cứng sự thực thi, thường mang lại 2–5× bổ sung sự tăng tốc thông qua tốt hơn sự sử dụng của bộ tăng tốc’s (chu) kỳ (làm) việc (duty cycle) bridge the gap between model-level decisions and hardware execution, often yielding 2–5× additional speedup through better utilization of the accelerator’s duty cycle). Độ chính xác sự lựa chọn và thời gian chạy sự tối ưu hóa mở rộng sự lượng tử hóa các kỹ thuật từ Chương 10 và Tensor Lõi các khả năng từ Chương 11 vào (trong) việc phục vụ miền (domain). (Cái) sự dịch (translation) của những (thuộc về) kỹ thuật các số liệu này thành đơn vị tính kinh tế, như hiển thị bởi Llama-3 trường hợp nghiên cứu, minh họa (như thế nào) kỹ thuật các quyết định liên quan (đến) việc lập lô, độ chính xác, và phần cứng sự lựa chọn trực tiếp quyết định (về mặt) tài chính tính khả thi của sự triển khai, một áp lực minh họa bởi công khai API giá cả sự nén trong hình 13.2. (Cái) việc phục vụ các nguyên tắc thiết lập ở đây (hàng đợi lý thuyết cho công suất việc lập kế hoạch, việc tiền xử lý sự tối- ưu hóa, việc lập lô chiến lược sự lựa chọn, và đào tạo-phục vụ sự sai lệch sự phòng ngừa) hình thành nền tảng cho (việc) xây dựng sản xuất ML các hệ thống đáp ứng thực-tế SLA form the foundation for building production ML systems that meet real-world SLAs). Cho dù triển khai một sự gợi ý hệ thống phục vụ hàng triệu của người dùng hay một y tế AI nơi mọi mili giây ảnh hưởng (tới) bệnh nhân các kết quả, những các nguyên tắc này chuyển dịch toán học thấu hiểu thành kỹ thuật các quyết định quyết định liệu các hệ thống thành công hay thất bại dưới tải. Chính Những điểm rút ra (Takeaways): Việc đảo ngược mọi đào tạo sự ưu tiên • Việc phục vụ là độ trễ tính kinh tế: Đào tạo thưởng (rewards) thông lượng (hơn) (trên) dài các chạy, nhưng việc phục vụ tiêu một cố định mỗi-yêu cầu ngân sách (xuyên) qua sự tuần tự hóa, việc tiền xử lý, việc xếp hàng đợi, sự suy luận, việc hậu xử lý, và mạng lưới. (Việc) Tối ưu hóa chỉ mô hình độ trễ bỏ lỡ giai đoạn người dùng thực sự chờ trên. • Sự sử dụng biến (turns) thành sự chờ (đợi): Hàng đợi lý thuyết làm (cho) công suất việc lập kế hoạch phi tuyến: tại 80 phần trăm sự sử dụng, trung bình thời gian trong hệ thống là 5× dịch vụ thời gian; tại 90 phần trăm, nó đạt (tới) 10×. Hiệu quả-chi phí khoảng trống giữ khiêm tốn lưu lượng truy cập các sự trào dâng (surges) khỏi (việc) trở thành SLO các sự thất bại. • Nhanh các mô hình tiết lộ đường ống các khoản thuế: Một khi sự suy luận rớt xuống xấp xỉ 5 ms, hình ảnh sự giải mã (decode), sự token hóa, và khác việc tiền xử lý có thể tiêu thụ 45–70 phần trăm của tổng độ trễ. (Cái) ràng buộc (binding) sự tối ưu hóa trở thành yêu cầu con đường, không (phải) thần kinh mạng lưới hạt nhân. • Việc lập lô theo (sau) lưu lượng truy cập, không (phải) thói quen: Poisson web các sự đến có thể sử dụng động việc lập lô, đồng bộ hóa các cảm biến cần căn chỉnh các lô, và người dùng-đơn di động các khối lượng công việc thường không thể lập lô (tại tất cả). (Cái) đúng (đắn) việc lập lô cửa sổ chuyển đổi sự chùng (xuống) (slack) thành thông lượng mà không (cần) (việc) tiêu độ trễ ngân sách. • Sự sai lệch (Skew) làm hỏng (breaks) độ chính xác mà không các lỗi: Đổi kích thước các phương pháp, sự chuẩn hóa thứ tự, sự hiệu chuẩn dữ liệu, hay đặc trưng các định nghĩa khác biệt giữa sự đào tạo và việc phục vụ dịch chuyển sống (live) các đầu vào (ra) ngoài (đã) học được sự phân phối. (Việc) Tái sử dụng giống hệt mã các con đường và (việc) giám sát sản xuất các lát cắt (slices) ngăn chặn im lặng sự xuống cấp. • LLM việc phục vụ là bộ nhớ sự quản lý: Giải mã thường đọc các trọng số từ VRAM cho mọi tạo ra token, do đó token độ trễ là bị giới hạn-băng thông trừ khi việc lập lô thay đổi sự ép buộc. KV-bộ đệm bố cục, PagedAttention, liên tục việc lập lô, độ chính xác, và thời gian chạy sự lựa chọn quyết định cả tính đồng thời và chi phí cho mỗi token.

13.13 Tóm tắt • Thời gian chạy các sự lựa chọn trở thành cơ sở hạ tầng các hóa đơn: Độ chính xác, đồ thị sự biên dịch, toán tử sự hợp nhất, và việc phục vụ thời gian chạy chuyển đổi trực tiếp thành bản sao số lượng và chi phí cho mỗi sự suy luận. Sự lượng tử hóa và chuyên môn hóa các thời gian chạy có thể đáng kể giảm thiểu yêu cầu việc phục vụ công suất khi chúng bảo tồn độ chính xác và khớp (với) mục tiêu phần cứng. Sự đào tạo được đánh giá bởi bao nhiêu công việc nó hoàn thành; việc phục vụ được đánh giá bởi liệu công việc hoàn thành đúng thời gian (hay không), và đó đơn thay đổi của câu hỏi đảo ngược (inverts) mọi thứ. Một độ trễ ngân sách được cố định từ (bên) ngoài, bởi người dùng và hợp đồng, và mọi giai đoạn của một yêu cầu chi tiêu (spends) chống lại cùng một vỏ bọc (envelope): sự tuần tự hóa, việc tiền xử lý, hàng đợi, mô hình, phản hồi. (Cái) đào tạo thuật toán, sống dữ liệu, và máy (tất cả) cùng nhau gặp (nhau) (meet) bên trong đó vỏ bọc, và hàng đợi là gì làm nó (trở nên) nguy hiểm (treacherous), bởi vì chờ (đợi) thời gian leo thang phi tuyến với tải và một hệ thống thoải mái bên trong ngân sách tại vừa phải lưu lượng truy cập có thể thổi qua (blow through) nó trên một nhỏ sự trào dâng. Không có gì trong việc phục vụ loại bỏ công việc (ra) khỏi yêu cầu; nó chỉ quyết định (như thế nào) cố định ngân sách được chia ra, đó là lý do tại sao mục tiêu là không (còn) (là) tốc độ nữa mà (là) sự đảm bảo rằng mọi yêu cầu, mọi thời điểm, đáp (lands) (vào) bên trong ranh giới (line).
(Cái) Gì Tiếp Theo: Từ nút đến nhà máy Chương này (đã) thiết kế đơn việc phục vụ nút. Theo (cách) của riêng nó (On its own), tuy nhiên, đó nút là mong manh (fragile). Các mô hình trôi dạt (drift) khi thế giới thay đổi, các bản cập nhật phải chạm tới người dùng mà không (việc) làm gián đoạn (interrupting) dịch vụ, và việc mở rộng quy mô các sự kiện yêu cầu nhiều các bản sao để hành xử như một đáng tin cậy (dependable) hệ thống. Trong Chương 14, chúng ta mở rộng quy mô chúng ta góc nhìn từ đơn yêu cầu (tới) sản xuất nhà máy: CI/CD (tự động hóa bản dựng (build), kiểm thử (test), và việc phát hành (release) các đường ống) quyết định nào mô hình đồ tạo tác thể xuất xưởng (ship), mô hình các sổ đăng ký (registries) (lập-phiên- bản (ver-sioned) mô hình đồ tạo tác các cửa hàng) và đặc trưng các cửa hàng (được chia sẻ phục vụ/đào tạo đặc trưng các kho lưu trữ (repositories)) giữ việc phục vụ căn chỉnh với sự đào tạo, tính có thể quan sát (observability) ((thuộc về) từ xa (telemetry) cho hành vi và sức khỏe) phát hiện độ trễ và độ chính xác sự trôi dạt, và quay lui (rollback) máy móc (các công cụ cho việc khôi phục (reverting) một xấu sự phát hành) giữ các sự thất bại khỏi (việc) trở thành vĩnh viễn (permanent) các sự ngừng hoạt động (outages) decides which model artifact may ship, model registries and feature stores keep serving aligned with training, observability detects latency and accuracy drift, and rollback machinery keeps failures from becoming permanent outages). Nghiên cứu Các câu hỏi: Cho sâu hơn (further) sự điều tra (inquiry) • (Như thế nào) (Việc) dịch chuyển từ đào tạo thông lượng (tới) việc phục vụ đuôi độ trễ thay đổi hệ thống kiến- trúc? • (Cái) gì độ trễ ngân sách sự phân rã nhận diện liệu mô hình, hàng đợi, việc tiền xử lý, sự tuần tự hóa, hay mạng lưới là ràng buộc (binding) (hay không)? • (Như thế nào) sự sử dụng khoảng trống nên định giá chống lại SLO-sự vi phạm rủi ro? • (Như thế nào) việc lập lô chiến lược (nên) thích ứng (với) Poisson các sự đến, truyền phát lưu lượng truy cập, người dùng-đơn các khối lượng công việc, và token sự tạo ra?