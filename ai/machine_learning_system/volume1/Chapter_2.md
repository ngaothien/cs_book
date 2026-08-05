Các Ứng dụng (Applications)
Vận hành (Operations)
Phục vụ (Serving)
Huấn luyện (Training)
Mô hình (Models)
Khuôn khổ (Frameworks)
Phần cứng (Hardware)
Dữ liệu (Data)
2
Hệ thống ML (ML Systems)
2.1
Khuôn khổ Mô hình Triển khai (Deployment Paradigm Framework)
2.2
Các Ràng buộc Vật lý: Lý do Các Mô hình (Paradigms) Tồn tại
2.3
Phân tích Khối lượng Công việc (Workloads)
2.4
Cân bằng Hệ thống và Phần cứng
2.5
ML Đám mây (Cloud ML): Sức mạnh Tính toán
2.6
ML Vùng biên (Edge ML): Độ trễ và Quyền Riêng tư
2.7
ML Di động (Mobile ML): Trí tuệ Ngoại tuyến (Offline Intelligence)
2.8
TinyML: Cảm biến Phổ quát (Ubiquitous Sensing)
2.9
Lựa chọn Mô hình Triển khai (Paradigm Selection)
2.10 Kiến trúc Kết hợp (Hybrid Architectures)
2.11 Entropy của Hệ thống: Tại sao Triển khai Không phải là Kết thúc
2.12 Sự ngụy biện và Cạm bẫy (Fallacies and Pitfalls)
2.13 Tóm tắt (Summary)
Mục đích
Tại sao việc triển khai cùng một mô hình lên điện thoại so với trung tâm dữ liệu lại đòi hỏi những kỹ thuật hoàn toàn khác nhau?
Sự thấu hiểu mang tính định nghĩa của kỹ thuật hệ thống ML là các ràng buộc định hướng kiến trúc. Tốc độ ánh sáng thiết lập một giới hạn tuyệt đối (absolute floor) cho mức độ phản hồi nhanh nhạy của các máy chủ ở xa. Nhiệt động lực học giới hạn khối lượng tính toán có thể diễn ra trong một không gian thể tích nhất định trước khi nhiệt độ trở nên không thể kiểm soát. Các tính chất vật lý của bộ nhớ làm cho việc di chuyển dữ liệu thường tốn kém hơn so với việc xử lý nó. Đây không phải là những giới hạn kỹ thuật đang chờ đợi công nghệ tốt hơn; chúng là những ranh giới vật lý vĩnh viễn chia thế giới thành các chế độ vận hành hoàn toàn khác biệt. Một trung tâm dữ liệu có thể huấn luyện các mô hình tỷ tham số nhưng không thể đảm bảo phản hồi có độ trễ thấp cho người dùng cách xa hàng ngàn dặm. Một chiếc điện thoại thông minh có thể phản hồi tức thì nhưng lại có ngân sách bộ nhớ rất nhỏ so với máy chủ. Một vi điều khiển (microcontroller) có thể chạy bằng pin đồng xu trong nhiều năm nhưng chỉ có vừa đủ khả năng tính toán cho một bộ phát hiện từ khóa đơn giản. Cùng một mô hình, cùng một thuật toán áp dụng cho cùng một dữ liệu, lại đòi hỏi quá trình kỹ thuật hoàn toàn khác biệt trong từng chế độ, không phải vì những sở thích trong thiết kế mà bởi vì các định luật vật lý khác nhau chi phối từng môi trường. Các nhóm coi việc triển khai là công việc theo sau (afterthought), tiến hành huấn luyện trong một môi trường và trì hoãn (deferring) việc xem xét các ràng buộc môi trường mục tiêu cho đến lúc ra mắt, sẽ phát hiện ra quá muộn màng rằng môi trường mục tiêu làm vô hiệu hóa hàng tháng trời của những quyết định kiến trúc. Về thuật ngữ D·A·M, việc hiểu các chế độ này sẽ biến công việc triển khai từ một chi tiết vận hành trở thành một bài toán thiết kế đồng bộ (co-design) hàng đầu: vị trí (locality) dữ liệu, cấu trúc thuật toán, và ràng buộc máy móc cùng nhau quyết định những gì khả thi.
41


================ PAGE 80 ================

42
2.1 Khuôn khổ Mô hình Triển khai (Deployment Paradigm Framework)
Năng lượng trải dài khắp các mô hình từ megawatt (đám mây) cho đến milliwatt (TinyML).
Mục tiêu Học tập (Learning Objectives)
• Giải thích cách các ràng buộc vật lý tạo ra các mô hình triển khai từ đám mây đến TinyML
• Áp dụng quy luật sắt và nguyên tắc nút thắt cổ chai để phân loại các khối lượng công việc bị giới hạn bởi tính toán (compute-bound), giới hạn bởi bộ nhớ (memory-bound), và giới hạn bởi I/O
• Ánh xạ các nguyên mẫu (archetypes) khối lượng công việc sang các mô hình triển khai bằng cách sử dụng các ví dụ từ Mô hình Ngọn hải đăng
• So sánh đám mây, biên, di động, và TinyML dựa trên các ràng buộc vận hành và sự đánh đổi định lượng
• Áp dụng khuôn khổ quyết định để chọn mô hình triển khai dựa trên quyền riêng tư, độ trễ, tính toán, và giới hạn chi phí
• Phân tích các mẫu kết hợp (hybrid patterns) kết hợp các mô hình triển khai với nhau để thỏa mãn các ràng buộc hệ thống
• Đánh giá các quyết định triển khai, những cạm bẫy phổ biến, và những nguyên tắc phổ quát có thể chuyển đổi chéo giữa các quy mô
2.1 Khuôn khổ Mô hình Triển khai
Hãy xem xét hai thái cực: một bộ phát hiện từ đánh thức (wake-word) trên đồng hồ thông minh và một công cụ đề xuất trong trung tâm dữ liệu. Bộ phát hiện từ đánh thức đại diện cho một khối lượng công việc TinyML hoạt động với ngân sách năng lượng milliwatt và giới hạn bộ nhớ kilobyte; trong khi công cụ đề xuất là một ví dụ điển hình cho khối lượng công việc ML đám mây, đòi hỏi các bảng nhúng (embedding tables) quy mô terabyte và cơ sở hạ tầng quy mô megawatt. Các hệ thống này giải quyết những bài toán khác nhau dưới những ràng buộc vật lý đối nghịch nhau, và các cơ sở hạ tầng hỗ trợ chúng gần như không có điểm chung nào. Thực tế này biến việc triển khai từ một công việc bổ sung (afterthought) vào khâu vận hành thành một quyết định kỹ thuật ưu tiên, một quyết định mà hệ phân loại D·A·M thể hiện trong hình 1.3 giúp chúng ta suy luận bằng cách đặt cơ sở hạ tầng lên vị trí ưu tiên ngang hàng với dữ liệu và thuật toán.
Các ràng buộc vật lý quyết định nơi một mô hình ML có thể chạy và định hình những gì là khả thi theo những cách mà không lựa chọn thuật toán nào có thể ghi đè (override) được. Thế nhưng việc triển khai khó khăn hơn nhiều so với bề ngoài, và lý do không nằm ở bản thân mô hình. Trong các hệ thống ML sản xuất, mô hình thường chỉ là một phần nhỏ của hệ thống tổng thể (Sculley et al. 2015). Cơ sở hạ tầng xung quanh bao gồm việc thu thập dữ liệu, xử lý đặc trưng, cơ sở hạ tầng phục vụ, giám sát, và quản lý tài nguyên. Tất cả những thứ đó thay đổi đáng kể tùy thuộc vào nơi mô hình được thực thi.
Các ràng buộc vật lý chi phối từng môi trường (độ trễ, năng lượng, và bộ nhớ) buộc việc triển khai ML phải chia thành bốn mô hình triển khai biệt lập, mỗi mô hình có sự đánh đổi kỹ thuật và các mẫu thiết kế hệ thống riêng. ML Đám mây (Cloud ML) tập hợp các tài nguyên tính toán trong trung tâm dữ liệu, cung cấp sức mạnh tính toán và lưu trữ gần như không giới hạn với cái giá phải trả là độ trễ mạng. ML Vùng biên (Edge ML) chuyển tính toán lại gần nơi dữ liệu bắt nguồn, bao gồm các sàn nhà máy, cửa hàng bán lẻ, và bệnh viện, để đạt được độ trễ thấp hơn và giữ các dữ liệu nhạy cảm ở dạng cục bộ (on-premises) (Shi et al. 2016). ML Di động (Mobile ML) đưa trí tuệ trực tiếp vào điện thoại thông minh và máy tính bảng, cân bằng giữa khả năng tính toán với thời lượng pin và giới hạn nhiệt độ. TinyML đẩy trí tuệ tới các thiết bị nhỏ nhất: các vi điều khiển (microcontrollers) giá vài đô la và tiêu thụ chỉ vài milliwatt, cho phép cảm biến luôn-bật (always-on) chạy trong nhiều tháng chỉ bằng pin đồng xu (Janapa Reddi, Plancher, et al. 2022). Bốn mô hình này trải dài qua 9 cấp số nhân về tiêu thụ điện năng (từ megawatt đến milliwatt) và dung lượng bộ nhớ (từ terabyte đến kilobyte), một khoảng rộng đến mức các nguyên tắc kỹ thuật chi phối đầu này của phổ gần như không thể áp dụng cho đầu kia.
Mỗi mô hình triển khai hoạt động như một phạm vi (envelope) vận hành riêng biệt, được xác định bởi lượng điện năng, bộ nhớ, và khả năng kết nối mạng hiện có. Mọi ứng dụng ML phải nằm gọn trong ít nhất một phạm vi này, và sự phù hợp đó quyết định thuật toán, phần cứng, và sự đánh đổi kỹ thuật nào được áp dụng. Các phạm vi này trải dài trên một phổ liên tục từ cơ sở hạ tầng đám mây tập trung đến các thiết bị phân tán siêu tiêu thụ ít điện năng, và hình 2.1 lập bản đồ hiển thị nơi mỗi mô hình triển khai ngự trị dọc theo trục tập trung (centralization axis) đó.
Phổ (spectrum) này mang tính định tính (qualitative): nó cho thấy vị trí của mỗi mô hình, chứ không phải quy mô của sự đánh đổi. Bảng 2.1 làm cho những sự đánh đổi đó trở nên định lượng (quantitative) bằng cách so sánh cạnh nhau độ trễ, năng lượng, bộ nhớ, kết nối, và các ràng buộc triển khai.


================ PAGE 81 ================

2. Hệ thống ML
43
Cổng kết nối (Gateway)
Các Thiết bị và Cảm biến Năng lượng Siêu thấp (Ultra Low Powered)
Thiết bị Thông minh (Intelligent Device)
Máy chủ Cục bộ (On Premise Servers)
Đám mây (Cloud)
TinyML
Cloud AI
Edge AI
Phổ Trí tuệ Phân tán (The Distributed Intelligence Spectrum)
Hình 2.1: Phổ Trí tuệ Phân tán: Quá trình triển khai học máy trải dài từ cơ sở hạ tầng đám mây tập trung đến các thiết bị TinyML bị hạn chế tài nguyên, mỗi môi trường cân bằng giữa vị trí xử lý, khả năng của thiết bị, và sự phụ thuộc vào mạng. Sơ đồ này tổng hợp các phạm vi (envelopes) triển khai được sử dụng trong chương này.
Bảng 2.1: Phổ Triển khai (Bề mặt Khái niệm): Bốn mô hình trải dài 9 cấp số nhân về công suất (MW xuống mW) và bộ nhớ (TB xuống KB). Bảng tổng quan khái niệm này định nghĩa từng mô hình bằng chế độ vận hành (operating regime) của nó; phổ phần cứng cụ thể ở phần sau sẽ gắn các danh mục này vào những nền tảng cụ thể và các ngưỡng (thresholds) quyết định định lượng. Các thông số phần cứng và hằng số vật lý nền tảng cho những con số này được liệt kê ở Phụ lục Giả định Hệ thống.
Mô hình (Paradigm)
Vị trí (Where)
Độ trễ (Latency)
Công suất (Power)
Bộ nhớ (Memory)
Tốt nhất cho (Best For)
ML Đám mây (Cloud ML)
Các trung tâm dữ liệu
100-500 ms
MW
TB
Huấn luyện, suy luận phức tạp
ML Vùng biên (Edge ML)
Các máy chủ cục bộ
10-100 ms
100 W
GB
Suy luận thời gian thực, quyền riêng tư
ML Di động (Mobile ML)
Điện thoại thông minh
5-50 ms
3–5 W
GB
AI cá nhân, ngoại tuyến (offline)
TinyML
Vi điều khiển
1-10 ms
mW
KB
Cảm biến luôn-bật (Always-on)
Bốn mô hình này tồn tại không phải vì những lựa chọn kỹ thuật mà vì những định luật vật lý mà không mức độ tối ưu hóa nào có thể vượt qua. Khoảng cách 9 cấp số nhân trong bảng 2.1 không phải là sự tình cờ của lịch sử kỹ thuật—nó là hệ quả của ba ràng buộc nền tảng: tốc độ ánh sáng (thiết lập giới hạn dưới của độ trễ), các giới hạn nhiệt động lực học về sự tiêu tán công suất (giới hạn khả năng tính toán trên mỗi watt), và chi phí năng lượng của việc truyền tín hiệu bộ nhớ (tạo ra bức tường bộ nhớ). Đây là những ranh giới vật lý, không phải sở thích thiết kế: một chiếc xe tự hành không thể được phục vụ từ một trung tâm dữ liệu cách nó 36 ms (độ trễ), và một mô hình 1.5 tỷ tham số không thể được huấn luyện trên một bộ vi điều khiển.
2.1.1 Mỏ neo kiến trúc: Ngăn xếp nút đơn (The single-node stack)
Để điều hướng qua các chế độ vận hành này, chúng ta neo các quyết định kỹ thuật của mình vào một mô hình 4 lớp của Ngăn xếp Nút đơn (Single-Node Stack), một sự tinh chỉnh từ phía Máy móc trong hệ phân loại D·A·M dành cho một máy chủ (host), trong khi dữ liệu và thuật toán đóng vai trò qua các yêu cầu của khối lượng công việc. Ở trên cùng của ngăn xếp, ứng dụng (application) xác định nhiệm vụ (mission): các mục tiêu về thông lượng huấn luyện hoặc độ trễ suy luận, mà các cơ chế của chúng sẽ được Chương 8 và Chương 13 triển khai. Khuôn khổ ML (ML framework) biên dịch mã nguồn mô hình thành các phép toán thực thi (Chương 7). Hệ điều hành (operating system) điều phối các tài nguyên và di chuyển dữ liệu giữa bộ nhớ máy chủ (host memory) và bộ nhớ bộ tăng tốc (accelerator memory). Bản thân phần cứng, được định nghĩa bởi dung lượng bộ nhớ băng thông cao (HBM), băng thông bộ nhớ, các kết nối nội bộ nút (như NVLink), và thông lượng tính toán, sẽ thiết lập các giới hạn vật lý, với bức tường bộ nhớ (memory wall) đóng vai trò là ràng buộc chính (Chương 11).
Ngăn xếp này thiết lập hợp đồng silicon (silicon contract) của chương: một thỏa thuận hiệu suất cố định mà một đoạn silicon cụ thể cung cấp cho một mô hình, được quy định bởi băng thông bộ nhớ, tỷ lệ tính toán tối đa (peak compute rate), và các chi phí phát sinh (overhead) cố định. Mọi chương trong nửa đầu của giáo trình này đều chất vấn một hoặc nhiều lớp trong số này, bởi vì việc hiểu chúng tương tác như thế nào trong một cỗ máy đơn lẻ là điều kiện kỹ thuật tiên quyết để nắm vững các quy mô phân tán lớn hơn.
Các ràng buộc vật lý này tương tác với quy luật sắt của hệ thống ML (phần 1.7), trong đó độ trễ đầu cuối (end-to-end latency) được phân tích thành chuyển động dữ liệu, sự tính toán, và chi phí phát sinh (overhead). Các môi trường triển khai khác nhau gây áp lực lên các thành phần khác nhau của phương trình này: hệ thống đám mây thường bị giới hạn bởi tính toán (compute bound), hệ thống di động va phải bức tường năng lượng, và thiết bị TinyML bị giới hạn bởi dung lượng bộ nhớ. Bằng cách kết hợp các ràng buộc vật lý với quy luật sắt, chúng tôi phát triển một bộ từ vựng định lượng để lập luận về việc mô hình (paradigm) nào phù hợp với một khối lượng công việc nhất định và tại sao. Để neo giữ phân tích này một cách cụ thể, chương


================ PAGE 82 ================

44
2.2 Các Ràng buộc Vật lý: Lý do Các Mô hình Tồn tại
1
Mô hình Triển khai (Deployment Paradigm): Một chế độ vận hành (operating regime) riêng biệt mà ranh giới của nó được thiết lập bởi vật lý học, chứ không phải quy ước. Phổ từ Đám mây đến TinyML trải dài 9 cấp số nhân về công suất bởi vì các ràng buộc nhiệt động lực học và điện từ tạo ra những bức tường cứng rắn (hard walls) mà không sự tối ưu hóa phần mềm nào có thể vượt qua, buộc các kiến trúc hệ thống phải khác biệt về chất ở mỗi tầng (tier). Việc xác định sai ranh giới mô hình sẽ gây lãng phí nỗ lực kỹ thuật: tối ưu hóa một mô hình đám mây để đạt thông lượng cao hơn 5 phần trăm là vô nghĩa nếu ngân sách độ trễ 10 ms của ứng dụng đòi hỏi sự triển khai tại biên.
2
Độ trễ (Latency): Khoảng thời gian từ khi phát ra yêu cầu đến khi nhận được kết quả, tương ứng với 𝐿_lat trong quy luật sắt. Rào cản ánh sáng khiến mức sàn này không thể giảm bớt: tốc độ ánh sáng trong cáp quang áp đặt thời gian khứ hồi (round trip) tối thiểu là ~36 ms băng qua lục địa Mỹ, tiêu tốn toàn bộ ngân sách độ trễ của một hệ thống quan trọng về an toàn (10 ms) ngay cả trước khi bất kỳ tính toán nào bắt đầu. Mỗi một mili giây bị tiêu tốn bởi khoảng cách là một mili giây không thể dùng cho việc suy luận của mô hình, đó là lý do tại sao rào cản ánh sáng buộc phải đưa ra lựa chọn về mô hình thay vì chỉ tối ưu hóa thuần túy.
3
Tỷ lệ Dennard (Dennard Scaling): Được đặt theo tên của Dennard et al. (1974) tại IBM, người đã mô tả các mối quan hệ tỷ lệ của MOSFET, theo đó các thiết bị thu nhỏ có thể giảm điện áp và dòng điện trong khi vẫn kiểm soát xấp xỉ mật độ năng lượng. Khi khả năng mở rộng quy mô điện áp bị chậm lại và năng lượng trở thành ràng buộc kiến trúc hàng đầu, sự tăng trưởng hiệu suất chuyển hướng sang tính song song (parallelism) và tính chuyên môn hóa: bộ xử lý đa lõi (multi-core), GPU, và TPU (Hennessy and Patterson 2019; Esmaeilzadeh et al. 2011).
giới thiệu năm Mô hình Ngọn hải đăng (ResNet-50, GPT-2, DLRM cho các gợi ý sử dụng nhiều phép nhúng, MobileNetV2, và một bộ Phát hiện Từ khóa cho việc phát hiện từ đánh thức) trải dài trên phổ triển khai và cô lập các nút thắt cổ chai riêng biệt của hệ thống. Các khối lượng công việc tham chiếu này lặp đi lặp lại xuyên suốt cuốn sách, cung cấp một cơ sở nhất quán để so sánh các kỹ thuật tối ưu hóa qua các chương.
Các tính chất vật lý tạo ra những ranh giới mô hình này được trình bày trước, tiếp theo là các công cụ phân tích (quy luật sắt, nguyên tắc nút thắt cổ chai, các nguyên mẫu khối lượng công việc) để ánh xạ các khối lượng công việc tới các mục tiêu triển khai. Mỗi mô hình sau đó được phân tích chuyên sâu bao gồm cơ sở hạ tầng, sự đánh đổi, và các khối lượng công việc tiêu biểu của nó, với góc nhìn về cách chọn lựa giữa chúng khi một hệ thống có khả năng chạy được trong nhiều hơn một mô hình. Chương khép lại với khuôn khổ quyết định mang tính so sánh và các kiến trúc kết hợp (hybrid architectures) kết hợp nhiều mô hình khi không một mục tiêu triển khai đơn lẻ nào đáp ứng được tất cả các yêu cầu.
2.2 Các Ràng buộc Vật lý: Lý do Các Mô hình Tồn tại
Một hệ thống an toàn với ngân sách phản ứng 10 ms không thể chờ một vòng khứ hồi (round trip) băng qua đất nước, và một mô hình tỷ tham số không thể được nhét vào một bộ vi điều khiển chỉ bằng mã nguồn tốt hơn. Đây không phải là các lỗi triển khai; chúng là hệ quả của các định luật vật lý về tốc độ ánh sáng, nhiệt động lực học công suất, và truyền tín hiệu bộ nhớ. Nơi một hệ thống chạy sẽ định hình lại hợp đồng silicon giữa mô hình và phần cứng. Ba ràng buộc chi phối các sự đánh đổi kỹ thuật ở phía trước: rào cản ánh sáng, bức tường năng lượng, và bức tường bộ nhớ.¹
Rào cản ánh sáng (The light barrier)
Rào cản ánh sáng thiết lập mức sàn (floor) về độ trễ² tuyệt đối. Thời gian khứ hồi tối thiểu bị chi phối bởi phương trình 2.1:
𝐿_lat,min = 2 × Khoảng_cách / 𝑐_fiber ≈ 2 × Khoảng_cách / 200,000 km/s (2.1)
trong đó 𝑐_fiber ≈ 200,000 km/s là tốc độ ánh sáng trong cáp quang, xấp xỉ hai phần ba giá trị trong chân không bởi vì ánh sáng lan truyền qua thủy tinh chậm hơn qua chân không.
Khoảng cách từ California đến Virginia (~3,600 km đường chim bay) yêu cầu ~36 ms khứ hồi trước khi bất kỳ tính toán nào bắt đầu. Các dịch vụ đám mây thực tế thường bổ sung thêm 60–150 ms chi phí phát sinh phần mềm. Các ứng dụng yêu cầu phản hồi dưới 10 ms không thể sử dụng cơ sở hạ tầng đám mây ở xa—vật lý cấm điều đó. Ràng buộc này tạo ra nhu cầu về ML Vùng biên và TinyML: khi ngân sách độ trễ khắt khe, tính toán phải di chuyển lại gần nguồn dữ liệu.
Bức tường năng lượng (The power wall)
Bức tường năng lượng xuất hiện bởi vì nhiệt động lực học giới hạn khối lượng tính toán có thể diễn ra trong một thể tích nhất định. Dưới tỷ lệ Dennard cổ điển³ (duy trì cho đến khoảng năm 2006), mối quan hệ giữa công suất và tần số là quan hệ lập phương (cubic). Ở đây 𝐶 là điện dung hiệu dụng, 𝑉 là điện áp, và 𝑓 là tần số xung nhịp. Vì điện áp tỷ lệ với tần số (𝑉 ∝ 𝑓), công suất tăng theo tỷ lệ thuận với 𝑓³, như phương trình 2.2 cho thấy:
Công_suất ∝ 𝐶 × 𝑉² × 𝑓
trong đó 𝑉 ∝ 𝑓 ⟹ Công_suất ∝ 𝑓³ (2.2)
Nhân đôi tần số xung nhịp yêu cầu công suất tăng gấp khoảng 8 lần. Sự đổ vỡ của mối quan hệ tỷ lệ này đã chấm dứt kỷ nguyên tăng tốc "miễn phí" thông qua tăng tần số và buộc ngành công nghiệp chuyển hướng sang sự song song hóa (đa lõi) và chuyên môn hóa (GPU, Đơn vị Xử lý Tensor (TPU)) vốn là định nghĩa của ML hiện đại. Các thiết bị di động va phải giới hạn nhiệt khắt khe ở mức 3–5 W; vượt quá mức này gây ra hiện tượng "điều tiết" (throttling), tức là thiết bị giảm hiệu suất để ngăn chặn tình trạng quá nhiệt. Trong thực tế, điều này có nghĩa là một mô hình di động đang chạy ở tốc độ 60 FPS trong 1 phút có thể bị điều tiết xuống còn 15 FPS khi thiết bị nóng lên. Giới hạn vật lý này làm phát sinh ML di động: các thiết bị chạy bằng pin không thể chỉ đơn giản là chạy các mô hình quy mô đám mây ngay tại cục bộ.
Bức tường bộ nhớ (The memory wall)
Bức tường bộ nhớ (Wulf and McKee 1995) phản ánh khoảng trống băng thông⁴ ngày càng mở rộng. Một bản phác thảo đơn giản cấp độ sách sử dụng các hệ số tăng trưởng hàng năm tiêu biểu để chỉ ra lý do tại sao khoảng trống đó lớn dần:
Tốc độ Tăng trưởng Tính toán / Tốc độ Tăng trưởng Băng thông Bộ nhớ ≈ 1.6 / 1.2 ≈ 1.33 (2.3)


================ PAGE 83 ================

2. Hệ thống ML
45
4
Băng thông Bộ nhớ (Bức tường bộ nhớ): Thuật ngữ "bức tường bộ nhớ" (memory wall) được Wulf và McKee đặt ra vào năm 1995, những người dự đoán rằng khoảng cách hiệu suất giữa bộ xử lý và bộ nhớ cuối cùng sẽ chi phối hiệu suất hệ thống—một dự đoán đã chứng minh được tính sáng suốt của nó đối với các khối lượng công việc ML, nơi quá trình tải trọng số, chứ không phải số học, mới thường là nút thắt cổ chai. Trong quy luật sắt, băng thông (BW) xuất hiện dưới mẫu số của thành phần dữ liệu 𝐷_vol / BW, vì vậy mỗi sự tăng gấp đôi kích thước mô hình mà không đi kèm với sự tăng gấp đôi băng thông bộ nhớ sẽ trực tiếp làm tăng thời gian thực (wall-clock time). Sự bất đối xứng này, tăng trưởng với tốc độ khoảng 1.33 lần mỗi năm, là lý do tại sao các hệ thống ML hiện đại thường bị giới hạn bởi bộ nhớ (memory-bound) nhiều hơn là giới hạn bởi tính toán (compute-bound).
Năng lực tính toán vượt xa băng thông bộ nhớ; khoảng cách ngày càng nới rộng chính là bức tường bộ nhớ.
Trong phương trình 2.3, tử số và mẫu số là các hệ số tăng trưởng hàng năm không có thứ nguyên (dimensionless). Một tỷ lệ lớn hơn 1 có nghĩa là khả năng tính toán đang ngày càng kéo giãn khoảng cách so với băng thông bộ nhớ, vì vậy mỗi thế hệ phần cứng làm cho quá trình di chuyển dữ liệu trở thành một phần lớn hơn của vấn đề hiệu suất trừ phi khối lượng công việc làm tăng tính cục bộ (locality) hoặc mật độ số học (arithmetic intensity).
Phương trình 2.3 định lượng hóa sự phân kỳ này: các bộ xử lý đã nhân đôi năng lực tính toán khoảng 18 tháng một lần, nhưng băng thông bộ nhớ chỉ cải thiện khoảng 20 phần trăm mỗi năm. Khoảng cách ngày càng mở rộng này biến sự di chuyển dữ liệu trở thành nút thắt cổ chai và chi phí năng lượng chủ chốt đối với hầu hết các khối lượng công việc ML. Ràng buộc này ảnh hưởng đến tất cả các mô hình triển khai nhưng đặc biệt nghiêm trọng đối với TinyML, nơi thiết bị chỉ có vài kilobyte bộ nhớ để làm việc. Chúng ta sẽ xem xét các giải pháp kiến trúc phần cứng ứng phó với bức tường bộ nhớ, bao gồm hệ thống phân cấp HBM và SRAM trên chip (on-chip), một cách chi tiết trong phần 11.5.1.
Kiểm tra 2.1: Các ràng buộc vật lý và quá trình triển khai
Các lựa chọn triển khai bị chi phối bởi vật lý học, không chỉ là bởi các sở thích cá nhân. Hãy kiểm tra mức độ hiểu của bạn:
□ Rào cản ánh sáng: Bạn có thể giải thích tại sao tốc độ ánh sáng khiến cho ML đám mây là bất khả thi đối với các tác vụ an toàn đòi hỏi độ trễ <10 ms không?
□ Bức tường năng lượng: Bạn có hiểu tại sao nhiệt động lực học (sự tản nhiệt) ngăn các mô hình trung tâm dữ liệu chạy trên thiết bị di động không?
□ Bức tường bộ nhớ: Bạn có thể giải thích tại sao di chuyển dữ liệu thường tốn kém hơn (về thời gian và năng lượng) so với tính toán không?
Những định luật vật lý này giải thích tại sao bốn mô hình lại tồn tại. Vật lý tạo ra các ranh giới; các quy định về quyền riêng tư, các động lực kinh tế, và các yêu cầu về chủ quyền dữ liệu củng cố và làm chúng sắc nét hơn. Chúng tôi xem xét các động lực bổ sung này bên trong mỗi phần mô hình triển khai, nhưng hiểu biết cốt lõi là các mô hình này vẫn sẽ tồn tại ngay cả khi không có những mối quan ngại đó. Không một quy định nào có thể làm cho tốc độ ánh sáng nhanh hơn, và không một mô hình kinh tế nào có thể xóa bỏ nhiệt động lực học.
Chỉ việc biết rằng những rào cản này tồn tại là cần thiết nhưng chưa đủ. Đứng trước một khối lượng công việc ML cụ thể (giả sử là công cụ đề xuất hoặc bộ phát hiện từ đánh thức), chúng ta cần xác định mô hình (paradigm) nào phù hợp và khối lượng công việc sẽ va phải rào cản nào trước tiên. Câu trả lời yêu cầu các công cụ phân tích kết nối các đặc điểm của khối lượng công việc với những ràng buộc vật lý này: quy luật sắt để phân tách độ trễ, nguyên tắc nút thắt cổ chai để xác định ràng buộc chi phối, và một tập hợp các nguyên mẫu khối lượng công việc (workload archetypes) để phân loại xem mỗi mô hình rơi vào đâu trên phổ phân bổ.
2.3 Phân tích Khối lượng Công việc (Workloads)
Khi có một công cụ đề xuất hoặc bộ phát hiện từ đánh thức, câu hỏi về khối lượng công việc là thành phần nào sẽ bị giới hạn trước tiên trên phần cứng đích. Công cụ phân tích trung tâm để trả lời câu hỏi hợp đồng silicon đó là quy luật sắt của hệ thống ML, đã được thiết lập ở phần 1.7 và được nhắc lại ở đây dưới dạng phương trình 2.4:
𝑇 = 𝐷_vol / BW + 𝑂 / (𝑅_peak ⋅ 𝜂_hw) + 𝐿_lat (2.4)
Phương trình này phân tách tổng độ trễ thành ba phần: di chuyển dữ liệu (𝐷_vol/BW), tính toán (𝑂 / (𝑅_peak ⋅ 𝜂_hw)), và chi phí phát sinh cố định (𝐿_lat). Đối với một quá trình suy luận đơn lẻ, những chi phí này chỉ đơn giản là cộng lại—mỗi chi phí được thanh toán một cách tuần tự (sequentially). Tuy nhiên, trong các hệ thống sản xuất, các tác vụ được xử lý liên tục dưới dạng một luồng (stream), và quá trình phân tích chuyển từ độ trễ tác vụ đơn lẻ sang việc xác định xem thành phần nào làm giới hạn hệ thống. Câu trả lời hoàn toàn phụ thuộc vào môi trường triển khai: một mô hình bị giới hạn bởi tính toán (compute bound) trong quá trình huấn luyện có thể trở thành bị giới hạn bởi bộ nhớ (memory bound) trong quá trình suy luận; một hệ thống chạy hiệu quả trên đám mây có thể va phải các giới hạn công suất trên các thiết bị di động. Để xác định thành phần nào chiếm ưu thế, chúng ta cần một nguyên tắc đi kèm.
2.3.1 Nguyên tắc nút thắt cổ chai (The bottleneck principle)
Quy luật sắt cho chúng ta biết chi phí của từng thành phần. Nguyên tắc nút thắt cổ chai cho chúng ta biết thành phần nào quan trọng. Không giống như phần mềm truyền thống nơi việc tối ưu hóa trường hợp trung bình (average case) là hiệu quả, hệ thống ML bị chi phối bởi thành phần chậm nhất của chúng: việc xác định nút thắt cổ chai của hệ thống là quan trọng vì việc tối ưu hóa các


================ PAGE 84 ================

46
2.3 Phân tích Khối lượng Công việc
các quá trình vận hành nhanh mang lại lợi ích bằng 0 trong khi giai đoạn chậm nhất vẫn không đổi. Các bộ tăng tốc hiện đại sử dụng quá trình thực thi đường ống (pipelined execution) để chồng lấp việc di chuyển dữ liệu với quá trình tính toán: trong khi bộ tăng tốc tính toán trên lô (batch) 𝑛, hệ thống bộ nhớ đã tìm nạp trước (prefetches) lô 𝑛 + 1. Với sự chồng lấp này, quá trình nào chậm hơn sẽ quyết định thông lượng của hệ thống—quá trình nhanh hơn sẽ "ẩn" phía sau nó. Tổng trong quy luật sắt trở thành một mức tối đa (maximum), như được công thức hóa trong phương trình 2.5:
𝑇_bottleneck = max(𝐷_vol / BW, 𝑂 / (𝑅_peak ⋅ 𝜂_hw), 𝑇_network) + 𝐿_lat (2.5)
• 𝐷_vol / BW (Bộ nhớ): Thời gian di chuyển dữ liệu giữa bộ nhớ và bộ xử lý.
• 𝑂 / (𝑅_peak ⋅ 𝜂_hw) (Tính toán): Thời gian thực thi các phép tính.
• 𝑇_network: Thời gian cho giao tiếp mạng (nếu chia sẻ công việc xử lý - offloading).
• 𝐿_lat (Chi phí phát sinh - Overhead): Độ trễ cố định (việc khởi chạy kernel, chi phí phát sinh thời gian chạy - runtime overhead).
Nguyên tắc này chỉ ra rằng nếu một hệ thống bị giới hạn bởi bộ nhớ (𝐷_vol / BW > 𝑂 / (𝑅_peak ⋅ 𝜂_hw)), thì việc mua các bộ xử lý nhanh hơn (𝑅_peak) sẽ chỉ mang lại lợi ích tăng tốc (speedup) chính xác là 0 phần trăm—giống như việc mở rộng một con đường cao tốc sáu làn xe chẳng mang lại lợi ích gì khi toàn bộ lưu lượng giao thông đều phải chui qua một cây cầu chỉ có hai làn xe. Kỹ sư phải xác định thành phần chiếm ưu thế (dominant term) trước khi tối ưu hóa. Khi mạng lưới là một trong các thành phần ứng viên, điều này xảy ra mỗi khi một thiết bị có thể offload (chuyển) công việc sang một máy chủ từ xa, thì một loại chi phí thứ hai xuất hiện mà cách phân tích dựa trên thời gian (time-based analysis) thường ẩn đi: việc di chuyển dữ liệu cũng tiêu tốn năng lượng bên cạnh thời gian, vì vậy quyết định giữa cục bộ so với offload phải cân nhắc dựa trên lượng joules, chứ không chỉ milliseconds.
Tính toán Nhanh (Napkin Math) 2.1: Năng lượng cho sự truyền dẫn (transmission)
Bài toán: Một cảm biến chạy bằng pin có nên xử lý dữ liệu ngay tại thiết bị (TinyML) hay gửi nó lên đám mây khi năng lượng cho việc truyền dẫn va phải bức tường năng lượng được cung cấp bởi pin?
Cho trước:
• Dữ liệu (𝐷_vol): 1 MB (khối lượng tải trọng - payload - minh họa).
• Năng lượng truyền dẫn (𝐸_tx): 100 mJ/MB (Wi-Fi/LTE).
• Năng lượng tính toán (𝐸_op): 0.1 mJ/suy luận (MobileNetV2 trên một đơn vị xử lý thần kinh (neural processing unit), hay NPU).
Tính toán:
1. Phương pháp đám mây: 𝐸_cloud ≈ 𝐷_vol × 𝐸_tx = 1 MB × 100 mJ/MB = 100 mJ.
2. Phương pháp cục bộ: 𝐸_local ≈ Suy luận = 0.1 mJ.
Góc nhìn hệ thống: Truyền dẫn dữ liệu thô tốn kém hơn gấp 1,000 lần so với xử lý dữ liệu ở cục bộ. Ngay cả khi đám mây có tốc độ vô hạn (𝑇 ≈ 0), bức tường năng lượng cũng khiến việc offload lên đám mây là hoàn toàn bất khả thi đối với các thiết bị luôn bật chạy bằng pin. Ràng buộc máy móc (pin) quyết định sự lựa chọn thuật toán (TinyML).
Các biến số trong quy luật sắt tương tác với nhau theo những cách khác biệt giữa các kịch bản triển khai. Trước khi xem xét các nguyên mẫu khối lượng công việc cụ thể, các nhân tố xác định hiệu suất cốt lõi này cần một định nghĩa ngắn gọn.
Góc nhìn Hệ thống 2.1: Quy luật sắt như một công cụ chẩn đoán triển khai
Quy luật sắt được giới thiệu trong phần 1.7 là công cụ chẩn đoán triển khai được sử dụng xuyên suốt chương này: nó biểu diễn tổng thời gian 𝑇 cần thiết cho một khối lượng công việc dưới dạng tổng cộng của quá trình di chuyển dữ liệu, toán học (số học), và độ trễ:
𝑇 = 𝐷_vol / BW + 𝑂 / (𝑅_peak ⋅ 𝜂_hw) + 𝐿_lat


================ PAGE 85 ================

2. Hệ thống ML
47
Dữ liệu, Thuật toán, và Máy móc liên kết với nhau; dịch chuyển một cái và những cái khác sẽ dịch chuyển theo.
5
Nguyên mẫu Khối lượng Công việc (Workload Archetype): Một sự phân loại các khối lượng công việc ML dựa trên nút thắt cổ chai chiếm ưu thế trong quy luật sắt thay vì dựa trên họ mô hình của chúng. Sự khác biệt này rất quan trọng vì chiến lược tối ưu hóa sẽ khác biệt hoàn toàn: một khối lượng công việc bị giới hạn bởi tính toán (compute-bound) được hưởng lợi từ số học nhanh hơn (𝑅_peak), trong khi một khối lượng công việc bị giới hạn bởi băng thông (bandwidth-bound) chỉ hưởng lợi từ các bus bộ nhớ rộng hơn (BW). Việc xác định sai nguyên mẫu gây lãng phí nỗ lực tối ưu hóa vào sai thành phần của quy luật sắt, giống như khi các nhóm bổ sung FLOP/s của bộ tăng tốc vào một đường ống suy luận bị giới hạn bởi bộ nhớ và quan sát thấy lợi ích tăng tốc bằng 0.
Sự phân rã này mang tính chẩn đoán (diagnostic): nó định lượng cách mà khối lượng dữ liệu (𝐷_vol), năng lực tính toán (𝑅_peak), và độ trễ cố định (𝐿_lat) cùng nhau thiết lập ngân sách thời gian của một khối lượng công việc. Không giống như Định luật Amdahl, tập trung vào sự tăng tốc song song, quy luật sắt gắn kết khối lượng công việc mô hình với chuyển động dữ liệu và độ trễ cố định tại ranh giới triển khai. Quan niệm sai lầm thường gặp là các thành phần này độc lập với nhau; trên thực tế, chúng là các trục đánh đổi, do đó việc tăng kích thước lô (batch size) có thể cải thiện chu kỳ làm việc (duty cycle - 𝜂_hw) đồng thời cũng làm tăng khối lượng dữ liệu (𝐷_vol) trên mỗi yêu cầu, chuyển một bài toán bị giới hạn bởi tính toán thành một bài toán bị giới hạn bởi bộ nhớ.
Quy luật sắt định lượng chi phí của từng thành phần; nguyên tắc nút thắt cổ chai xác định tốc độ của dây chuyền lắp ráp. Như một quy tắc ngón tay cái, hãy sử dụng dạng cộng trong phương trình 2.4 khi phân tích độ trễ của một tác vụ đơn lẻ, và dạng max trong phương trình 2.5 khi phân tích thông lượng của một luồng các tác vụ liên tục.
2.3.2 Các nguyên mẫu khối lượng công việc (Workload archetypes)
Nguyên tắc nút thắt cổ chai thu gọn quá trình tối ưu hóa thành một sự chẩn đoán duy nhất: xác định ràng buộc nào chiếm ưu thế đối với một khối lượng công việc nhất định. Câu trả lời phụ thuộc vào hệ phân loại D·A·M trong bảng 1.4, vốn phân tách mọi hệ thống ML thành Dữ liệu, Thuật toán, và Máy móc. Các môi trường triển khai khác nhau tạo ra những nút thắt cổ chai khác nhau dọc theo các trục này, vì vậy cùng một họ mô hình có thể yêu cầu quá trình kỹ thuật khác biệt khi nó chuyển từ một máy chủ đám mây với bộ nhớ quy mô terabyte sang một bộ vi điều khiển với quy mô kilobyte. Quy luật sắt biến công cụ chẩn đoán đó thành bốn nguyên mẫu khối lượng công việc⁵. Đây không phải là các danh mục mô hình; chúng là các nút thắt cổ chai vật lý lặp đi lặp lại xác định xem những động thái kỹ thuật nào có thể mang lại hiệu quả.
Lát cắt đầu tiên phân tách các hệ thống bị giới hạn bởi số học (arithmetic-bound) khỏi các hệ thống bị giới hạn bởi di chuyển dữ liệu (data-movement-bound). Một Quái thú Tính toán (Compute Beast) thực hiện nhiều phép tính trên mỗi byte được tải lên, vì vậy tiến bộ đạt được từ thông lượng số học cao hơn, sự tận dụng tốt hơn, và thực thi song song nhiều hơn; việc huấn luyện mạng nơ-ron lớn là một trường hợp điển hình. Ngược lại, một Kẻ ngốn Băng thông (Bandwidth Hog) lại chờ đợi sự di chuyển của các trọng số dày đặc hoặc dữ liệu kích hoạt (activations), do đó các bus bộ nhớ rộng hơn và khả năng tái sử dụng dữ liệu tốt hơn sẽ quan trọng hơn so với việc chỉ bổ sung peak FLOP/s; tạo văn bản tự hồi quy (autoregressive text generation) minh họa cho chế độ này.
Lát cắt thứ hai bao gồm các khối lượng công việc mà ràng buộc cốt lõi hoàn toàn không phải là số học dày đặc (dense arithmetic). Các khối lượng công việc Phân tán Thưa thớt (Sparse Scatter) bị chi phối bởi các quá trình tra cứu bảng không đều đặn (irregular table lookups) và tính cục bộ của bộ nhớ đệm (cache locality) kém, do đó dung lượng bộ nhớ, độ trễ truy cập, và giao tiếp sẽ định hình hiệu suất trong các hệ thống đề xuất với các bảng nhúng khổng lồ. Khối lượng công việc Ràng buộc Nhỏ bé (Tiny Constraint) đối mặt với một phạm vi (envelope) ngược lại: năng lượng cho mỗi lần suy luận và dấu vết bộ nhớ (memory footprint), chứ không phải tốc độ thô, quyết định việc cảm biến luôn-bật (always-on) có thể chạy được hay không.
Ngọn hải đăng 2.1: Năm khối lượng công việc tham chiếu
Xuyên suốt cuốn sách này, chúng tôi sử dụng năm Mô hình Ngọn hải đăng (Lighthouse Models) được tóm tắt trong bảng 2.2: các khối lượng công việc cụ thể trải dài trên phổ triển khai và cô lập các nút thắt cổ chai hệ thống khác nhau. Chương 6 cung cấp đầy đủ các chi tiết kiến trúc và tiểu sử (biographies) của mô hình.
Bảng 2.2: Năm mô hình ngọn hải đăng: Các khối lượng công việc lặp đi lặp lại được sử dụng xuyên suốt cuốn sách để kết nối quy luật sắt với thực tiễn cụ thể. Mỗi ngọn hải đăng ghép cặp một nguyên mẫu (Quái thú Tính toán, Kẻ ngốn Băng thông, Phân tán Thưa thớt, Ràng buộc Nhỏ bé) với mô hình triển khai mà nó thường chạy nhất, cô lập một nút thắt cổ chai hệ thống riêng biệt.
Ngọn hải đăng
Nguyên mẫu
Mô hình Triển khai
ResNet-50
Quái thú Tính toán
Huấn luyện đám mây, suy luận vùng biên
GPT-2/Llama
Kẻ ngốn Băng thông
Suy luận đám mây
DLRM
Phân tán Thưa thớt
Chỉ đám mây (phân tán)
MobileNetV2
Quái thú Tính toán (hiệu quả)
Di động, biên
Phát hiện Từ khóa (KWS)
Ràng buộc Nhỏ bé
TinyML, luôn-bật (always-on)


================ PAGE 86 ================

48
2.3 Phân tích Khối lượng Công việc
Các nguyên mẫu này ánh xạ một cách tự nhiên tới các mô hình triển khai. Quái thú tính toán và khối lượng công việc phân tán thưa thớt (sparse scatter) hướng về phía ML đám mây nơi tài nguyên dồi dào, những kẻ ngốn băng thông trải dài trên cả đám mây và biên tùy thuộc vào yêu cầu độ trễ, còn các khối lượng công việc bị ràng buộc nhỏ bé (tiny constraint) thuộc về TinyML. Để làm cho các khái niệm trừu tượng này trở nên cụ thể, chúng tôi neo từng nguyên mẫu vào một mô hình cụ thể lặp đi lặp lại xuyên suốt cuốn sách này dưới dạng một trong năm khối lượng công việc tham chiếu.
Để gắn kết các sự phụ thuộc trừu tượng của quy luật sắt vào thực tiễn cụ thể, chúng ta lần lượt phân tích năm Mô hình Ngọn hải đăng này. Các tóm tắt sau đây tóm tắt (recap) mỗi khối lượng công việc từ góc độ hệ thống, kết nối chúng với các nút thắt cổ chai trong quy luật sắt cụ thể mà chúng làm ví dụ minh họa.
Ngọn hải đăng đầu tiên, ResNet-50, phân loại hình ảnh vào 1,000 danh mục, xử lý mỗi hình ảnh thông qua khoảng 4.1 GFLOP sử dụng 25.6 triệu tham số (102.4 MB tại FP32) (He et al. 2016a). Được sử dụng trong các chẩn đoán hình ảnh y tế, các đường ống nhận thức của xe tự hành, và đóng vai trò như mạng lõi (backbone) cho các hệ thống kiểm duyệt nội dung, cấu trúc đều đặn (regular), mang mật độ tính toán dày đặc (compute-dense) của nó khiến nó trở thành tiêu chuẩn kinh điển (canonical benchmark) cho hiệu suất của bộ tăng tốc phần cứng.
Các mô hình ngôn ngữ GPT-2/Llama cung cấp sức mạnh cho chatbot, trợ lý mã, và các công cụ tạo nội dung (Radford et al. 2019; Touvron, Lavril, et al. 2023). Những mô hình này tạo ra văn bản theo từng token một, yêu cầu mô hình phải đọc toàn bộ tập tham số của nó (1.5 tỷ tham số cho GPT-2, 7 tỷ–70 tỷ tham số cho Llama) từ bộ nhớ đối với mỗi token đầu ra. Kiểu mẫu truy cập bộ nhớ tuần tự (sequential memory access pattern) này tạo ra nút thắt cổ chai tự hồi quy (autoregressive bottleneck) chi phối các chi phí phục vụ mô hình (Pope et al. 2023).
Ngọn hải đăng đề xuất, DLRM, đại diện cho khối lượng công việc đề xuất sử dụng nhiều phép nhúng đằng sau các hệ thống "Bạn cũng có thể thích" quy mô lớn (Naumov et al. 2019). Nó ánh xạ người dùng và các mục (items) thành các vector nhúng (embedding vectors) được lưu trữ trong các bảng có thể vượt quá 100 GB phép nhúng, khiến cho dung lượng bộ nhớ, chứ không phải sự tính toán, trở thành ràng buộc cốt lõi.
Ngọn hải đăng di động, MobileNetV2, được thiết kế cho các tác vụ thị giác di động hiệu quả như phân loại, phát hiện, và phân vùng (segmentation) (Sandler et al. 2018). Nó thực hiện cùng một tác vụ phân loại hình ảnh như ResNet nhưng sử dụng các tích chập có thể tách rời theo chiều sâu (depthwise separable convolutions), tách biệt việc lọc không gian (spatial filtering) khỏi việc trộn kênh (channel mixing), để giảm bớt tính toán đi 13.7 lần, cho phép suy luận theo thời gian thực trên điện thoại thông minh ở mức 3–5 W.
Ngọn hải đăng TinyML, Phát hiện Từ khóa (KWS), đại diện cho nguyên mẫu cảm biến luôn bật (always-on). Các hệ thống KWS phát hiện các cụm từ kích hoạt ngắn với các mô hình nhỏ gọn được xây dựng cho các vi điều khiển bị ràng buộc về tài nguyên (Y. Zhang et al. 2017); trong kịch bản Chuông cửa Thông minh (Smart Doorbell), cùng mẫu (pattern) đó trở thành một kích hoạt "Ding Dong" hoặc "Xin chào" ngay tại thiết bị. Khối lượng công việc ngọn hải đăng có khoảng 200K tham số và vừa vặn trong khoảng 800 KB, đặt nó vào chế độ TinyML với bộ nhớ kilobyte và ngân sách milliwatt.
Ngọn hải đăng KWS cũng cho thấy cách những ràng buộc như vậy được đánh giá trong thực tế như thế nào: theo cấu trúc phân cấp (hierarchically), với mức độ vừa vặn (fit) được kiểm tra trước tốc độ. Hình 2.2 chấm điểm kịch bản Chuông cửa Thông minh trên một ESP32-S3 với cả hai cấp độ. Mô hình vượt qua ngân sách bộ nhớ quy mô kilobyte, nhưng mục tiêu độ trễ 50 ms khắt khe lại thất bại, vì vậy một mô hình vừa vặn vẫn là một mô hình phải được tối ưu hóa trước khi nó đáp ứng được ngân sách tương tác của mình.
Mức độ Tận dụng Tài nguyên (Nhu cầu / Cung cấp)
Bộ nhớ (RAM)
Độ trễ (SLA)
Đánh giá Hệ thống: Chuông cửa Thông minh (Smart Doorbell)
Hình 2.2: Phân cấp của các Ràng buộc: Thẻ điểm (Scorecard) Chuông cửa Thông minh: Sự đánh giá trực quan này về kịch bản Chuông cửa Thông minh phơi bày sự đánh đổi nền tảng của hệ thống. Trong khi mô hình thành công trong việc nằm gọn trong ngân sách bộ nhớ quy mô kilobyte (Cấp độ 1: ĐẠT), độ trễ đường cơ sở 101 ms của nó vượt quá mục tiêu phản hồi thời gian thực khắt khe 50 ms trên ESP32-S3 (Cấp độ 2: KHÔNG ĐẠT). Điều này chỉ ra rằng việc tối ưu hóa thêm về mô hình và triển khai (implementation) là bắt buộc trước khi triển khai trong phạm vi ngân sách tương tác khắt khe hơn này.


================ PAGE 87 ================

2. Hệ thống ML
49
6
Đường găng (Critical Path): Chuỗi các hoạt động phụ thuộc liên tiếp dài nhất trong một đường ống. Quy tắc quyết định trong câu kích hoạt rất khắt khe: nếu một lệnh gọi mạng liên vùng (cross-region) kéo dài 200 ms xuất hiện ở bất cứ đâu trên đường găng, một hệ thống với tổng ngân sách 100 ms chắc chắn sẽ thất bại bất kể mọi giai đoạn khác chạy nhanh đến mức nào. Trong thực tế, suy luận ML hiếm khi là giai đoạn dài nhất; tiền xử lý và hậu xử lý dữ liệu thường chiếm ưu thế, khiến cho đường găng dài hơn nhiều so với chỉ riêng thời gian thực thi mô hình.
7
Phổ Chi phí Phần cứng ML (ML Hardware Cost Spectrum): Cơ sở hạ tầng AI trải dài qua 6 cấp số nhân về chi phí, từ vi điều khiển $10 đến các cụm bộ tăng tốc trị giá hàng triệu đô la. Khoảng cách gấp triệu lần này có nghĩa là việc lựa chọn mô hình triển khai đồng thời là một quyết định vật lý và quyết định kinh tế. Ngay cả trong các lựa chọn thiết bị cá nhân (individual-device choices), cùng một mục tiêu độ chính xác có thể đạt được trên một vi điều khiển chi phí thấp chỉ sau khi giảm đáng kể mô hình, hoặc trên một bộ tăng tốc đám mây đắt tiền với một ngân sách tài nguyên lớn hơn nhiều, dẫn đến các hồ sơ về độ trễ, năng lượng, và chi phí vận hành hoàn toàn khác biệt.
8
Hiệu quả Sử dụng Công suất (Power Usage Effectiveness - PUE): Số liệu này cô lập chi phí năng lượng phát sinh (ví dụ: làm mát), yếu tố quyết định khả năng khả thi về kinh tế của mô hình "đám mây MW" (MW cloud). Đối với một trung tâm dữ liệu, chi phí phát sinh 6 phần trăm còn lại của mức PUE ưu tú (elite) 1.06 vẫn tương đương với hàng megawatt cho chi phí không tính toán (noncompute). Toàn bộ danh mục chi phí này không tồn tại đối với mô hình "TinyML mW", giải thích cho một phần quan trọng của khoảng kinh tế 6 cấp số nhân.
Phạm vi trải dài trong các yêu cầu tính toán và dấu vết bộ nhớ (memory footprints) giải thích tại sao không có một mô hình triển khai đơn lẻ nào phù hợp với mọi khối lượng công việc. Một bộ phát hiện từ khóa có thể hoạt động với khoảng 20 MFLOP và 800 KB, trong khi ResNet-50 cần khoảng 4.1 GFLOP và 102.4 MB cho mỗi hình ảnh. Ví dụ DLRM tham chiếu đã đạt tới 100 GB, và các hệ thống đề xuất kiểu DLRM trong sản xuất có thể vượt quá 100 TB. Các mô hình ngôn ngữ thêm vào một chế độ bị chi phối bởi băng thông: hàng tỷ tham số được truyền tải liên tục (streamed repeatedly) từ bộ nhớ trong quá trình suy luận tự hồi quy. Năm Mô hình Ngọn hải đăng này đóng vai trò như các mỏ neo cụ thể xuyên suốt cuốn sách, mỗi mô hình cô lập một nút thắt cổ chai hệ thống riêng biệt được nhắc lại trong mọi chương.
Chỉ riêng các công cụ phân tích sẽ vẫn trừu tượng cho đến khi được neo vào silicon thực. Bước tiếp theo dịch quy luật sắt, nguyên tắc nút thắt cổ chai, và các nguyên mẫu khối lượng công việc thành các quyết định kỹ thuật định lượng bằng cách kiểm tra sự cân bằng hệ thống (sự tương tác giữa tính toán, bộ nhớ, và I/O) biến đổi ra sao giữa các nền tảng phần cứng thực tế.
2.4 Sự Cân bằng Hệ thống và Phần cứng (System Balance and Hardware)
Các ràng buộc vật lý chuyển các đánh đổi độ trễ - thông lượng thành các quyết định kỹ thuật thông qua các con số cụ thể. Bảng 2.3 cung cấp các mức độ trễ (order-of-magnitude latencies) nên làm cơ sở cho mọi quyết định triển khai—trải dài qua 8 cấp số nhân từ các phép toán tính toán nano-giây đến hàng trăm mili-giây cho các cuộc gọi mạng liên khu vực. Ràng buộc về băng thông và độ trễ phần cứng chi tiết được đề cập trong Chương 11. Quy tắc quyết định then chốt rất đơn giản: một hoạt động có độ trễ > 𝑋 không thể xuất hiện trên đường găng (critical path) của một hệ thống có ngân sách độ trễ là 𝑋 ms.⁶
Bảng 2.3: Các Con số Độ trễ cho Thiết kế Hệ thống ML: Các mức độ trễ xuyên suốt tính toán, bộ nhớ, mạng, và các hoạt động ML, quyết định tính khả thi của việc triển khai. Trải dài 8 cấp số nhân, từ các phép toán tính toán nano-giây đến hàng trăm mili-giây cho giao tiếp mạng liên vùng, những ràng buộc vật lý này định hình các quyết định kiến trúc. Để có tham chiếu nhanh toàn diện bao gồm cả các tỷ lệ năng lượng và quy tắc mở rộng quy mô, hãy xem phần D.1.
Hoạt động (Operation)
Độ trễ (Latency)
Hệ quả Triển khai (Deployment Implication)
Tính toán (Compute)
Nhân ma trận trên GPU (mỗi phép tính)
~1 ns
Tính toán hiếm khi là nút thắt cổ chai
Suy luận trên NPU (MobileNetV2)
5–20 ms
Di động có thể xử lý thị giác thời gian thực
Tạo token LLM
20–100 ms
Được cảm nhận như "tốc độ gõ phím"
Bộ nhớ (Memory)
Truy cập trúng bộ nhớ đệm L1 (L1 cache hit)
~1 ns
Giữ dữ liệu nóng (hot data) trong thanh ghi
Đọc HBM (GPU)
20–50 ns
Chậm hơn 20–50 lần so với tính toán
Đọc DRAM (di động)
50–100 ns
Bị giới hạn bởi bộ nhớ trên hầu hết thiết bị
Mạng (Network)
Cùng trung tâm dữ liệu
0.5 ms
Khả thi đối với Microservices
Cùng khu vực (region)
1–5 ms
Khả thi đối với máy chủ biên (Edge servers)
Khác khu vực (Cross-region)
50–150 ms
Chỉ dùng cho xử lý lô (Batch processing)
Hoạt động ML (ML Operations)
Phát hiện từ đánh thức (TinyML)
100 μs
Khả thi đối với luôn-bật ở mức <1 mW
Phát hiện khuôn mặt (di động)
10–30 ms
Thời gian thực ở 30 FPS
Token đầu tiên của GPT-4
200–500 ms
Người dùng nhận thấy độ trễ
Một bước huấn luyện ResNet-50
200–400 ms
Được tối ưu hóa cho thông lượng (Throughput-optimized)
Bốn mô hình triển khai có được độ chính xác khi được gắn với phần cứng cụ thể. Trong khi bảng 2.1 định nghĩa các mô hình về mặt khái niệm, bảng hệ thống tiêu biểu ở phần sau của mục này cung cấp các thiết bị, bộ xử lý cụ thể, và các ngưỡng định lượng mà người thực hành sử dụng để chọn lựa mục tiêu triển khai.⁷,⁸ Khoảng cách năng lượng 9 cấp số nhân tương tự, giờ đây được nối kết với khoảng chênh lệch chi phí từ hàng triệu USD xuống còn 10 USD, quyết định mô hình nào có thể phục vụ khối lượng công việc một cách kinh tế.
Sự khác biệt phần cứng này dịch trực tiếp thành các nút thắt cổ chai về hiệu suất. Để hiểu được ràng buộc nào chiếm ưu thế trong từng mô hình, chúng ta áp dụng nguyên tắc nút thắt cổ chai (phần 2.3.1).


================ PAGE 88 ================

50
2.4 Sự Cân bằng Hệ thống và Phần cứng
Suy luận Lô-1 (Batch-1 inference) nằm ở phía bị giới hạn bởi bộ nhớ của đường mái nhà (roofline).
Góc nhìn Hệ thống 2.2: Cân bằng hệ thống qua các mô hình
Dạng đường ống (pipelined form) của quy luật sắt của hệ thống ML từ phần 1.7 chỉ ra rằng thời gian thực thi bị giới hạn bởi nút thắt cổ chai chiếm ưu thế của hệ thống, như phương trình 2.6 công thức hóa:
𝑇 = max(𝑂 / (𝑅_peak ⋅ 𝜂_hw), 𝐷_vol / BW, 𝐷_vol / BW_IO) + 𝐿_lat (2.6)
Ở đây, 𝑂 đại diện cho tổng số phép toán, 𝑅_peak là tỷ lệ tính toán tối đa, 𝜂_hw là hiệu quả sử dụng phần cứng, 𝐷_vol là khối lượng dữ liệu, BW là băng thông bộ nhớ, BW_IO là băng thông I/O (lưu trữ hoặc mạng), và 𝐿_lat là chi phí phát sinh cố định. Phương trình xác định tài nguyên nào (tính toán, bộ nhớ, hoặc I/O) giới hạn hiệu suất. Thành phần chiếm ưu thế (dominant term) thay đổi tùy theo mô hình triển khai, và sự dịch chuyển đó vẽ lại chiến lược tối ưu hóa: huấn luyện đám mây bị ràng buộc bởi thông lượng tính toán, do đó một bộ tăng tốc nhanh hơn sẽ nâng cao hiệu suất, trong khi đó suy luận LLM và suy luận biên bị ràng buộc bởi băng thông bộ nhớ, nơi một bộ tăng tốc nhanh hơn chẳng mang lại gì và chỉ có việc di chuyển ít byte hơn mới giúp ích. Bảng 2.4 đi qua cả năm mô hình, và phần A.5.1 ánh xạ mỗi thành phần chiếm ưu thế vào những sự tối ưu hóa mang lại hiệu quả và những sự tối ưu hóa bị lãng phí, biến chẩn đoán này thành một kế hoạch hành động.
Bảng 2.4: Nút thắt cổ chai Chiếm ưu thế theo Mô hình: Thành phần nào của quy luật sắt giới hạn hiệu suất trong mỗi mô hình triển khai, lý do vật lý khiến nó chiếm ưu thế, và trọng tâm tối ưu hóa kéo theo. Thành phần chiếm ưu thế làm thay đổi hoàn toàn chiến lược tối ưu hóa: huấn luyện đám mây tối đa hóa việc tận dụng tính toán, trong khi suy luận LLM phải tấn công vào băng thông bộ nhớ.
Mô hình
Ràng buộc Chiếm ưu thế
Lý do
Trọng tâm Tối ưu hóa
Huấn luyện Đám mây
𝑂 / (𝑅_peak ⋅ 𝜂_hw) (Tính toán)
Bộ nhớ/mạng dồi dào; FLOP/s giới hạn thông lượng
Tối đa hóa tận dụng bộ tăng tốc, kích thước lô
Suy luận LLM Đám mây
𝐷_vol/BW (Băng thông bộ nhớ)
Tạo ra văn bản tuần tự liên tục di chuyển trạng thái mô hình
Tăng khả năng tái sử dụng; giảm số byte phải di chuyển
Suy luận Biên (Edge Inference)
𝐷_vol/BW (Băng thông bộ nhớ)
Băng thông cục bộ hạn chế; các mô hình thường bị giới hạn bởi bộ nhớ
Mô hình nhỏ hơn; truyền bộ nhớ ít hơn
Di động (Mobile)
Năng lượng (ngầm định - implicit)
Pin = ∫Công_suất ⋅ 𝑑𝑡; điều tiết nhiệt
Độ chính xác thấp hơn; chu kỳ làm việc (duty cycling)
TinyML
Dấu vết mô hình phải vừa khít trên chip (dung lượng)
Bộ nhớ quy mô Kilobyte; mô hình phải nằm gọn trên chip
Mô hình siêu nhỏ và số học dấu phẩy tĩnh (fixed-point)
Phân tích đường mái nhà (Roofline analysis) phân loại các nút thắt cổ chai bằng cách so sánh cường độ số học của một khối lượng công việc với điểm cân bằng của máy móc (Williams et al. 2009). Chúng ta sử dụng cấu trúc này một cách không chính thức ở đây; phần D.2.1 sẽ dẫn xuất toàn bộ mô hình, định nghĩa cường độ số học một cách chính thức và dẫn xuất điểm đỉnh (ridge point) chia tách các chế độ bị giới hạn bởi bộ nhớ và bị giới hạn bởi tính toán. Trong cấu trúc đó, cùng một mô hình ResNet-50 có thể chuyển từ hành vi huấn luyện bị giới hạn bởi tính toán ở kích thước lô cao sang suy luận ảnh đơn nhạy cảm với bộ nhớ hơn ở batch=1. Quá trình lựa chọn mô hình triển khai phải tính đến sự thay đổi này.
Sự dịch chuyển này giữa huấn luyện và suy luận là một yếu tố quan trọng cần phải hiểu. Hãy nhớ lại hệ phân loại D·A·M từ bảng 1.4: mọi hệ thống ML đều bao gồm Dữ liệu, Thuật toán, và Máy móc. Bảng 2.5 cho thấy cách mỗi thành phần hoạt động khác nhau tùy thuộc vào việc hệ thống đang huấn luyện (học các mẫu) hay phục vụ (áp dụng chúng).
Bảng 2.5: D·A·M × Giai đoạn (Phase): Cùng một mô hình áp đặt những nhu cầu hoàn toàn khác biệt lên Dữ liệu, Thuật toán, và Máy móc tùy thuộc vào việc hệ thống đang huấn luyện hay phục vụ. Khi các nút thắt cổ chai dịch chuyển một cách bất ngờ, hãy kiểm tra xem giai đoạn nào hiện đang được tối ưu hóa.
Thành phần
Huấn luyện (Có thể thay đổi - Mutable)
Suy luận (Không thay đổi - Immutable)
Dữ liệu (Data)
Thông lượng khổng lồ: các lô lớn, xáo trộn (shuffling), tăng cường (augmentation)
Độ trễ thấp: các mẫu đơn lẻ, tính mới (freshness), tốc độ
Thuật toán (Algorithm)
Giai đoạn học: cập nhật tham số mô hình từ các ví dụ
Giai đoạn dự đoán: áp dụng các trọng số cố định vào dữ liệu đầu vào mới
Máy móc (Machine)
Tối ưu hóa thông lượng: các cụm băng thông cao, bộ nhớ lớn
Tối ưu hóa độ trễ: các thiết bị biên, bộ tăng tốc suy luận


================ PAGE 89 ================

2. Hệ thống ML
51
9
Phổ Chi phí Phần cứng ML: Cơ sở hạ tầng AI trải dài sáu cấp số nhân về chi phí, từ vi điều khiển $10 đến cụm bộ tăng tốc trị giá hàng triệu đô la. Khoảng cách gấp triệu lần này có nghĩa là việc lựa chọn mô hình triển khai đồng thời là một quyết định vật lý và quyết định kinh tế. Ngay cả trong các lựa chọn thiết bị cá nhân, cùng một mục tiêu độ chính xác có thể chỉ đạt được trên vi điều khiển chi phí thấp sau khi giảm đáng kể mô hình, hoặc trên bộ tăng tốc trung tâm dữ liệu đắt tiền với ngân sách tài nguyên lớn hơn nhiều, dẫn đến các hồ sơ hoàn toàn khác biệt về độ trễ, năng lượng, và chi phí vận hành.
Một so sánh định lượng áp dụng phân tích này cho quá trình suy luận ResNet-50 trên một bộ tăng tốc trung tâm dữ liệu cao cấp và một NPU di động. Hãy coi đây là những mỏ neo phần cứng tại một thời điểm (point-in-time): tính toán số học xoay quanh tỷ lệ tính toán, băng thông bộ nhớ, và kích thước lô, trong khi Chương 11 giải thích kiến trúc bộ tăng tốc đằng sau những con số đó.
Tính toán Nhanh 2.2: ResNet-50 trên đám mây so với di động
Bài toán: Suy luận ResNet-50 bị giới hạn bởi tính toán hay giới hạn bởi bộ nhớ trên (a) bộ tăng tốc trung tâm dữ liệu cao cấp và (b) NPU di động hàng đầu (flagship)?
Cho trước (từ Mô hình Ngọn hải đăng):
• ResNet-50: 4.1 GFLOP mỗi lần suy luận, 25.6 triệu tham số (102.4 MB FP32, 51.2 MB FP16)
Phân tích:
(a) Bộ tăng tốc trung tâm dữ liệu đám mây (batch=1, FP16)
• Tối đa tính toán (Peak compute): 312 TFLOP/s (FP16)
• Băng thông bộ nhớ: 2.04 TB/s
• Thời gian tính toán: 𝑇_comp = 4.10×10^9 / (3.12×10^14) = 0.013 ms
• Thời gian bộ nhớ: 𝑇_mem = 5.12×10^7 / (2.04×10^12) = 0.025 ms
• Kết quả: Nút thắt cổ chai = Bộ nhớ (chậm hơn 1.9 lần so với tính toán)
• Phân tích: Số tính toán trên mỗi byte di chuyển = 4.10×10^9 / (5.12×10^7) = 80 FLOP/byte. Tỷ lệ này đo lường khối lượng tính toán mà khối lượng công việc thực hiện cho mỗi byte được tải lên. Khi tỷ lệ này vượt quá tỷ lệ tính toán trên băng thông (𝑅_peak/BW) của phần cứng, khối lượng công việc bị giới hạn bởi tính toán; thấp hơn mức đó, khối lượng công việc bị giới hạn bởi bộ nhớ. Đối với quá trình suy luận ảnh đơn lẻ, kích thước lô thấp mang lại sự tái sử dụng hạn chế, giải thích tại sao ngay cả các bộ tăng tốc mạnh mẽ cũng có thể bị giới hạn bởi bộ nhớ ở batch=1.
(b) Di động: NPU Hàng đầu (batch=1, INT8)
• Tối đa tính toán: ~35 TOPS (INT8)—tiêu biểu cho các NPU di động hiện đại
• Băng thông bộ nhớ: ~100 GB/s (LPDDR5)
• Kích thước mô hình: 25.6 MB (đã lượng tử hóa INT8)
• Thời gian tính toán: 𝑇_comp = 4.10×10^9 INT8 ops / (3.50×10^13 INT8 ops/s) = 0.12 ms
• Thời gian bộ nhớ: 𝑇_mem = 2.56×10^7 / (1.00×10^11) = 0.26 ms
• Kết quả: Nút thắt cổ chai = Bộ nhớ (chậm hơn 2.2 lần so với tính toán)
Góc nhìn hệ thống: Cả hai nền tảng đều bị giới hạn bởi bộ nhớ đối với suy luận ảnh đơn lẻ. Băng thông bộ nhớ nhanh hơn của A100 (2.04 TB/s so với 100 GB/s = 20.4 lần) dịch thành quá trình suy luận nhanh hơn khoảng 10.2 lần; chỉ riêng tính toán tối đa không phải là phép so sánh mang tính giới hạn. Điều này giải thích tại sao các kỹ thuật giảm byte và độ chính xác thấp hơn có thể đánh bại việc chỉ đơn giản là mua thêm peak FLOP/s cho quá trình triển khai. ResNet-50 trở thành khối lượng công việc bị giới hạn bởi tính toán khi quá trình phân lô và tái sử dụng dữ liệu đẩy lượng tính toán trên mỗi byte được di chuyển lên trên điểm cân bằng của phần cứng, 𝐼 > 𝑅_peak/BW, trong đó 𝐼 = 𝑂/𝐷_vol. Điểm giao cắt (crossover) phụ thuộc vào kiến trúc và cách triển khai, vì lưu lượng dữ liệu kích hoạt (activation traffic), quá trình di chuyển đầu vào/đầu ra, sự tái sử dụng bộ nhớ đệm, và các chi tiết thực thi thời gian chạy (runtime) đều làm thay đổi số byte hiệu quả được di chuyển trong mỗi lần suy luận.
Sự nén lại (Compression) quan trọng nhiều hơn chứ không phải ít hơn khi ngân sách phần cứng thu hẹp lại. Khi các hệ thống chuyển đổi từ Đám mây sang Vùng biên (Edge) đến TinyML, các tài nguyên sẵn có giảm xuống một cách đáng kể. Bảng 2.6 định lượng quá trình này với các ví dụ phần cứng cụ thể: bộ nhớ giảm từ 131 TB (đám mây) xuống còn 520 KB (TinyML), một sự sụt giảm gấp 250 triệu lần, đi kèm với cùng một khoảng chênh lệch công suất từ megawatt đến milliwatt⁹. Sự chênh lệch tài nguyên này đặc biệt gay gắt nhất trên các bộ vi điều khiển (microcontrollers), nền tảng phần cứng chính của TinyML, nơi dung lượng lưu trữ và bộ nhớ không đủ cho các mô hình ML thông thường.


================ PAGE 90 ================

52
2.5 ML Đám mây: Sức mạnh Tính toán
10
Quy mô Huấn luyện Mô hình Ngôn ngữ Lớn (LLM): GPT-3 yêu cầu khoảng 3,634.3 PFLOP-days và chi phí tính toán ước tính 4.6 triệu USD theo mức giá đám mây năm 2020. Quy mô này minh họa cho sự đánh đổi cốt lõi của ML đám mây: chỉ có cơ sở hạ tầng tập trung mới có thể tập hợp đủ 𝑅_peak cho các lần chạy huấn luyện lớn, nhưng cái giá phải trả về 𝐿_lat (100–500 ms cho một vòng khứ hồi mạng) khiến cho chính cơ sở hạ tầng đó trở nên không phù hợp cho suy luận thời gian thực.
11
Đám mây như một Điện toán Tiện ích (Utility Computing): Mô hình tiện ích cho phép các nhà cung cấp đưa ra một danh mục phần cứng chuyên dụng vốn không khả thi về mặt kinh tế đối với một tổ chức đơn lẻ nếu muốn duy trì. Điều này cung cấp khả năng truy cập trực tiếp theo yêu cầu vào các kiến trúc cụ thể cần thiết cho từng nguyên mẫu khối lượng công việc: các khoang bộ tăng tốc (accelerator pods) dày đặc cho Quái thú Tính toán, các nút được trang bị HBM cho Kẻ ngốn Băng thông, và các hệ thống bộ nhớ cao với kết nối nội bộ nhanh cho Phân tán Thưa thớt. Do đó, một nhóm có thể thuê một khoang siêu máy tính (supercomputing pod) trị giá hơn 10 triệu USD được xây dựng với mục đích cụ thể trong vài giờ thay vì phải sở hữu nó.
Phổ phần cứng biến sự chẩn đoán nút thắt cổ chai đó thành một bài kiểm tra sự phù hợp (fit test). Các nền tảng trong bảng 2.6 là sản phẩm của hàng thập kỷ tiến hóa phần cứng, từ các bộ đồng xử lý (coprocessors) dấu phẩy động trong những năm 1980 qua bộ xử lý đồ họa (graphics processors) trong những năm 2000 cho đến các bộ tăng tốc AI chuyên biệt (domain-specific AI accelerators) ngày nay. Chương 11 sẽ lần theo quá trình phát triển lịch sử này và những nguyên tắc kiến trúc thúc đẩy nó. Ở đây, hệ quả của nó là quan trọng nhất: những phần cứng khác biệt về chất xuất hiện ở những điểm khác nhau trong cơ sở hạ tầng, do đó mỗi khối lượng công việc phải được khớp (matched) với khu vực mà nó có thể thỏa mãn (satisfy) được giới hạn về tính toán, bộ nhớ, năng lượng, và chi phí.
Bảng 2.6: Phổ Phần cứng (Nền tảng Cụ thể): Các thiết bị tiêu biểu minh họa (instantiate) cho từng mô hình triển khai từ bảng 2.1. Ở nơi bảng khái niệm định nghĩa các chế độ vận hành, bảng này cung cấp các bộ xử lý cụ thể, dung lượng bộ nhớ, phạm vi công suất, và các mức giá mà những người thực hành sử dụng để khớp các khối lượng công việc vào phần cứng. DGX Spark nằm ở mức cao cấp của phổ vùng biên (edge spectrum); hầu hết các triển khai vùng biên sử dụng các thiết bị nhỏ hơn nhiều (ví dụ, Jetson Orin Nano). Chúng tôi đưa nó vào đây để minh họa mức trần của sự triển khai phi đám mây (noncloud deployment). Bản thân gia đình NVIDIA Jetson cũng trải rộng trên một phổ SKU (Stock Keeping Unit) lớn, từ Jetson Orin Nano (7–15 W) qua Jetson Orin NX (10–25 W) đến Jetson AGX Orin (15–60 W); xuyên suốt cuốn sách này, các số liệu công suất của Jetson nên được đọc kết hợp với SKU cụ thể được nhắc đến trong bối cảnh.
Danh mục
Ví dụ Thiết bị
Bộ xử lý
Bộ nhớ
Lưu trữ
Công suất
Mức giá
ML Đám mây (Cloud ML)
Google TPU v4 Pod
4,096 chip TPU v4, 1.1 EFLOP/s
131 TB HBM2
Quy mô đám mây (PB)
~3 MW
Dịch vụ đám mây (thuê)
ML Vùng biên (Edge ML)
NVIDIA DGX Spark
GB10 Grace Blackwell, 1 PFLOP/s AI
128 GB LPDDR5x
4 TB NVMe
~200 W
~$3,000–$5,000
ML Di động (Mobile ML)
Điện thoại thông minh hàng đầu
Mobile SoC (CPU + GPU + NPU)
8–16 GB
128 GB-1 TB
3–5 W
$999+
TinyML
ESP32-CAM
Lõi kép @ 240 MHz
520 KB RAM
4 MB Flash
0.05 W–1.2 W (công suất bo mạch chủ động)
$10
Mỗi mô hình chiếm giữ một khu vực riêng biệt trên phổ triển khai, bị chi phối bởi các ràng buộc vật lý (rào cản ánh sáng, bức tường năng lượng, bức tường bộ nhớ) và được định lượng bằng các công cụ phân tích (quy luật sắt, nguyên tắc nút thắt cổ chai) được giới thiệu trước đó. Các ngưỡng định lượng (quantitative thresholds) trong bảng 2.7 giúp người thực hành xác định liệu một khối lượng công việc có vừa vặn (fits) với mức giới hạn về tính toán, băng thông, năng lượng, và độ trễ của mục tiêu hay không.
Bảng 2.7: Ngưỡng Quyết định Triển khai: Các phạm vi (envelopes) thực tế mà những người thực hành sử dụng để xác định tính khả thi của việc triển khai đối với mỗi mô hình trong bảng 2.6. Những giá trị này trả lời cho câu hỏi "khối lượng công việc của tôi có thể chạy ở đây không?" bằng cách chỉ định mức (tier) tính toán, băng thông bộ nhớ, và giới hạn công suất mà mỗi mô hình cung cấp. Mỗi số liệu công suất đánh dấu một hạng mục (class) tiêu biểu của một mô hình chứ không phải là mức trần tuyệt đối; cụ thể phạm vi của vùng biên mở rộng từ các module nhúng tiêu thụ ít điện năng lên đến thiết bị cấp máy trạm (workstation-class) được hiển thị trong bảng 2.6.
Mô hình (Paradigm)
Tính toán
Băng thông bộ nhớ
Công suất
Độ trễ
ML Đám mây
> 1000 TFLOP/s
> 1000 GB/s
Hạng MW (PUE 1.1–1.3)
100-500 ms
ML Vùng biên
~1 PFLOP/s
> 270 GB/s
Hạng 100 W
10-100 ms
ML Di động
15–45 TOPS
60–100 GB/s
3–5 W
5-50 ms
TinyML
< 1 TOPS
—
< 1 mW luôn-bật mục tiêu trung bình
1-10 ms
Bảng ngưỡng hoàn tất bài kiểm tra độ phù hợp (fit test): mỗi mô hình bên dưới là một phạm vi vận hành với một tài nguyên ràng buộc (binding resource) khác nhau. Bốn phần tiếp theo đi từ đám mây đến TinyML, theo dõi dốc từ mức tài nguyên tính toán tối đa xuống mức giới hạn hiệu quả lớn nhất trong khi vẫn giữ nguyên những câu hỏi tương tự: thành phần nào bị ràng buộc, tối ưu hóa điều gì mang lại lợi ích, và những sự đánh đổi nào đi kèm.
2.5 ML Đám mây: Sức mạnh Tính toán (Computational Power)
Hãy xem xét những gì cần thiết để huấn luyện GPT-3: 3,634.3 PFLOP-ngày (PFLOP-days) tính toán, 10,000 GPU V100 chạy trong khoảng 15 ngày, tiêu tốn hàng megawatt năng lượng—với chi phí ước tính là ~$4.6 triệu¹⁰. Không một chiếc điện thoại thông minh, máy chủ biên (edge server), hay một cỗ máy đơn lẻ nào trên Trái Đất có thể thực hiện được việc tính toán này. Chỉ có trung tâm dữ liệu, với sức mạnh tính toán, bộ nhớ, và lưu trữ gần như vô hạn, mới có thể kết hợp đủ tài nguyên để làm cho điều này trở nên khả thi. Đây là mệnh đề định nghĩa (defining proposition) của ML đám mây: khi có thể chịu đựng được độ trễ, nó mang lại quy mô tính toán mà không mô hình nào khác có thể sánh kịp.


================ PAGE 91 ================

2. Hệ thống ML
53
ML Đám mây (Cloud ML) tập hợp các tài nguyên tính toán trong các trung tâm dữ liệu¹¹ để xử lý các tác vụ đòi hỏi khả năng tính toán chuyên sâu (computationally intensive): xử lý dữ liệu quy mô lớn, phát triển mô hình cộng tác, và phân tích nâng cao. Cơ sở hạ tầng này đóng vai trò là ngôi nhà tự nhiên cho ba trong số bốn nguyên mẫu khối lượng công việc: các khối lượng công việc Quái thú Tính toán (Compute Beast) như huấn luyện ResNet đòi hỏi duy trì mức TFLOP/s trên hàng ngàn bộ tăng tốc, các khối lượng công việc Kẻ ngốn Băng thông (Bandwidth Hog) như suy luận mô hình ngôn ngữ lớn (LLM) hưởng lợi từ băng thông bộ nhớ HBM mức TB/s, và các khối lượng công việc Phân tán Thưa thớt (Sparse Scatter) như hệ thống đề xuất đòi hỏi các bảng nhúng quy mô terabyte và các kết nối nội bộ băng thông cao cho các mẫu giao tiếp tất cả-với-tất cả (all-to-all communication patterns).
Việc triển khai đám mây trải dài từ các phiên bản (instances) máy đơn lẻ (máy trạm, máy chủ đa GPU, hệ thống DGX) đến các hệ thống phân tán quy mô lớn trải rộng trên nhiều trung tâm dữ liệu. Cuốn sách này tập trung vào các hệ thống đám mây máy đơn lẻ, nơi người đọc học cách xây dựng và tối ưu hóa hệ thống ML trên các cỗ máy mạnh mẽ riêng lẻ. Những nghiên cứu trong tương lai có thể giải quyết cơ sở hạ tầng đám mây phân tán, nơi các hệ thống phối hợp quá trình tính toán trên nhiều máy được kết nối mạng. Điều này tuân theo nguyên tắc thiết lập các nền tảng trước khi thêm vào những sự phức tạp.
Mọi khối lượng công việc trên đám mây đều thực hiện cùng một sự đánh đổi: khả năng tính toán co giãn (elastic compute) với cái giá phải trả là khoảng cách (distance).
Định nghĩa 2.1: ML Đám mây (Cloud ML)
Học máy Đám mây là mô hình triển khai đánh đổi độ trễ để lấy tính toán co giãn (đàn hồi) bằng cách đặt các khối lượng công việc ML trong các trung tâm dữ liệu tập trung, tách biệt năng lực tính toán khỏi vị trí vật lý của nguồn dữ liệu và người dùng.
1. Ý nghĩa: Việc triển khai đám mây chi phối thành phần 𝑅_peak: một khu vực đám mây đơn lẻ có thể cung cấp (provision) hàng nghìn bộ tăng tốc theo yêu cầu, mang lại tổng thông lượng mà không một hệ thống thiết lập cục bộ (on-premise) thông thường nào có thể sánh được về mặt kinh tế. Điểm đánh đổi là thành phần 𝐿_lat: độ trễ khứ hồi tối thiểu 10–100 ms (được thiết lập bởi tốc độ ánh sáng trên các khoảng cách lục địa) khiến đám mây trở nên bất khả thi đối với bất kỳ khối lượng công việc nào yêu cầu phản hồi dưới 10 ms.
2. Sự khác biệt: Khác với ML vùng biên, vốn ưu tiên tính tất định của độ trễ (latency determinism) và tính cục bộ của dữ liệu (data locality) ở mức 𝑅_peak cố định, ML đám mây ưu tiên 𝑅_peak co giãn với cái giá phải trả là 𝐿_lat biến thiên (variable).
3. Cạm bẫy phổ biến: Một quan niệm sai lầm thường gặp là cho rằng ML đám mây mang nghĩa "tính toán không giới hạn." Trên thực tế, hình phạt khoảng cách (𝐿_lat) và nút thắt cổ chai trong quá trình tiếp nhận (ingestion bottleneck - 𝐷_vol/BW) là những ràng buộc vật lý mà không có sự tối ưu hóa phần mềm nào có thể loại bỏ được, thiết lập một mức sàn cứng (hard floor) về thời gian phản hồi cho bất kỳ khối lượng công việc nào mà dữ liệu của nó bắt nguồn từ bên ngoài trung tâm dữ liệu.
Sự tập trung hóa là một món hời (bargain) của đám mây: nó cho phép quy mô lớn và khả năng truy cập toàn cầu, nhưng chính sự tập trung hóa đó lại tạo ra độ trễ và sự phụ thuộc vào internet (hình 2.3). Bản đồ này và ba bản đồ mô hình triển khai tiếp theo đều được đọc theo cùng một cách, vạch ra từ ràng buộc cốt lõi của từng mô hình cho đến phản hồi hệ thống mà nó buộc phải có, ranh giới thất bại (failure boundary) nơi phản hồi đó bị phá vỡ, và các khối lượng công việc phù hợp bên trong nó. Các ví dụ phát triển mạnh mẽ trong chế độ này, bao gồm trợ lý ảo, hệ thống đề xuất, và phát hiện gian lận, tất cả đều chấp nhận sự đánh đổi đó vì quy mô quan trọng hơn tính tức thì (immediacy). Thách thức cơ bản nhất, độ trễ mạng, không phải là hạn chế kỹ thuật mà là một ràng buộc vật lý. Một tính toán nhanh về hình phạt khoảng cách ngay sau hình vẽ sẽ làm rõ điều này.
Tính toán Nhanh 2.3: Hình phạt khoảng cách
Bài toán: Hãy xem xét một màn hình an toàn thời gian thực cho một cánh tay robot. Logic an toàn yêu cầu thời gian phản hồi đầu cuối (end-to-end) là 10 ms để ngăn ngừa thương tích, vì vậy hình phạt khoảng cách do rào cản ánh sáng áp đặt là một yếu tố quan trọng. Mô hình chạy trong một trung tâm dữ liệu đám mây hiệu suất cao cách đó 1,500 km. Ngân sách an toàn có thể được đáp ứng không?
Vật lý học:
1. Ánh sáng trong cáp quang: ~200,000 km/s.
2. Sự lan truyền khứ hồi (Round-trip propagation): (1,500 km × 2) / 200,000 km/s = 15 ms.
3. Kết quả: Chỉ riêng sự lan truyền khứ hồi đã đòi hỏi 15 ms, vượt quá ngân sách đầu cuối 10 ms (-5 ms khoảng trống - headroom) ngay cả trước khi mô hình thực hiện bất kỳ phép suy luận nào.


================ PAGE 92 ================

54
2.5 ML Đám mây: Sức mạnh Tính toán
12
Đơn vị Xử lý Tensor (TPU): Một bộ xử lý được thiết kế tùy chỉnh (ASIC) cung cấp thông lượng ở mức PFLOP/s bằng cách kết nối cứng (hard-wiring) kiến trúc của nó cho các hoạt động nhân ma trận, vốn là thành phần chi phối các khối lượng công việc ML. Sự chuyên môn hóa cực độ này đánh đổi tính linh hoạt đa năng (general-purpose flexibility) để lấy sự cải thiện >10 lần về hiệu suất trên mỗi watt so với bộ tăng tốc đa năng (general-purpose accelerator) trên cùng một tác vụ ML. Do đó, chi phí cao để triển khai các bộ tăng tốc này ở quy mô trung tâm dữ liệu chỉ hiệu quả về mặt kinh tế đối với quá trình tính toán ML lớn, bền bỉ (sustained).
13
Định giá Trả theo Mức Sử dụng (Pay-as-You-Go Pricing): Một mô hình kinh tế đám mây trong đó người dùng trả tiền cho số giờ bộ tăng tốc được tiêu thụ thay vì phải sở hữu phần cứng. Định giá co giãn (elastic) chuyển đổi chi phí cố định (fixed cost) của mức 𝑅_peak nhàn rỗi thành chi phí biến đổi (variable cost) tỷ lệ thuận với mức độ tận dụng (utilization) thực tế, nhưng điều ngược lại cũng đúng: các khối lượng công việc duy trì 24/7 (phục vụ suy luận liên tục) trên đám mây thường tốn kém hơn 2–3 lần so với phần cứng cục bộ (on-premises) tương đương khi được khấu hao trong ba năm, một điểm giao cắt (crossover) thúc đẩy phân tích tổng chi phí sở hữu (TCO) ở phần sau trong mục này.
Góc nhìn hệ thống: Vật lý học đã khiến cho ML đám mây trở nên bất khả thi đối với ứng dụng này. Mô hình phải di chuyển ra vùng Biên (Edge).
Ràng buộc Cốt lõi (Binding Constraint)
Phản hồi Hệ thống (System Response)
Ranh giới Thất bại (Failure Boundary)
Các Khối lượng công việc Phù hợp (Workloads That Fit)
ML Đám mây
Quy mô Vượt quá Các Máy tính Cục bộ (Scale Exceeds Local Machines)
Dữ liệu hoặc Trạng thái được Tập trung hóa (Data or State Is Centralized)
Ngân sách Độ trễ được Nới lỏng (Latency Budget Is Relaxed)
Mức Sử dụng có tính Co giãn (Usage Is Elastic)
Gộp chung Bộ tăng tốc và Lưu trữ (Pool Accelerators and Storage)
Phân mảnh Dữ liệu và Mô hình (Shard Data and Models)
Lập lịch ở Quy mô Hạm đội (Schedule at Fleet Scale)
Tập trung hóa Các hoạt động Vận hành (Centralize Operations)
Độ trễ Tốc độ Ánh sáng (Speed-of-Light Latency)
Sự phụ thuộc vào Internet (Internet Dependence)
Sự phơi nhiễm Chủ quyền Dữ liệu (Data Sovereignty Exposure)
Chi phí bị chi phối bởi Mức tận dụng (Utilization-Driven Cost)
Huấn luyện Mô hình lớn (Large-Model Training)
Hệ thống Đề xuất (Recommendation Systems)
Phát hiện Gian lận (Fraud Detection)
Giọng nói có sự Hỗ trợ của Đám mây (Cloud-Assisted Voice)
Hình 2.3: Bản đồ Ràng buộc ML Đám mây: Cơ sở hạ tầng tập trung giải quyết bài toán quy mô cho những quái thú tính toán, những kẻ ngốn băng thông, và các khối lượng công việc phân tán thưa thớt, nhưng nó giới thiệu những ràng buộc về khoảng cách, sự phụ thuộc, quyền riêng tư, và chi phí, qua đó quyết định khi nào ML đám mây không còn là mục tiêu triển khai phù hợp.
2.5.1 Cơ sở hạ tầng đám mây và quy mô
ML đám mây tập hợp các tài nguyên tính toán trong các trung tâm dữ liệu với một quy mô chưa từng có. Hình 2.4 chụp lại quy mô vật lý đằng sau sự trừu tượng hóa này: một hình ảnh trung tâm dữ liệu Google Cloud TPU¹² từ buổi công bố Gemini của Google. Các thiết kế siêu máy tính TPU tổ chức hàng nghìn chip tăng tốc chuyên dụng thành các hệ thống quy mô trung tâm dữ liệu (data-center-scale systems) nhằm cung cấp thông lượng độ-chính-xác-giảm (reduced-precision throughput) ở mức PFLOP/s đến EFLOP/s (Jouppi et al. 2023). Bảng 2.6 định lượng cách các hệ thống đám mây cung cấp năng lực tính toán và băng thông bộ nhớ lớn hơn nhiều cấp số nhân so với các thiết bị di động, ở mức công suất và chi phí vận hành cũng cao hơn tương ứng. Các cơ sở này cho phép những khối lượng công việc bất khả thi trên các thiết bị hạn chế tài nguyên, nhưng vị trí từ xa (remote) của chúng giới thiệu những sự đánh đổi khắt khe (critical trade-offs), sẽ được xem xét tiếp theo: độ trễ vòng khứ hồi mạng (network round-trip) loại trừ các ứng dụng thời gian thực, và chi phí vận hành (operational costs) tỷ lệ tuyến tính với mức độ sử dụng (usage).
Thực tế vật lý của quá trình tính toán mức PFLOP/s hiển hiện ngay trong chính cơ sở hạ tầng: một tầng cơ sở đơn lẻ chứa hàng nghìn chip tăng tốc được sắp xếp thành các hàng tủ máy (racks) được làm mát bằng chất lỏng, mỗi tủ máy tiêu thụ hàng kilowatt điện năng để duy trì tổng thông lượng mà không một thiết bị cá nhân nào có thể tiếp cận được.
ML đám mây xuất sắc trong việc xử lý khối lượng dữ liệu khổng lồ thông qua các kiến trúc được song song hóa, cho phép huấn luyện trên các bộ dữ liệu yêu cầu hàng trăm terabyte lưu trữ và hàng PFLOP tính toán, những tài nguyên vẫn là điều phi thực tế trên các thiết bị bị hạn chế (constrained devices). Các kỹ thuật huấn luyện được đề cập trong Chương 8 và phân tích phần cứng trong Chương 11 sẽ giải thích cách những người thực hành (practitioners) đạt được quy mô này.
Chính sự tập trung hóa cũng làm thay đổi cách các mô hình được chia sẻ và vận hành. Các API đám mây giúp các mô hình đã được huấn luyện có thể tiếp cận được trên toàn thế giới qua các nền tảng di động, web, và IoT. Cơ sở hạ tầng dùng chung (shared infrastructure) cho phép nhiều nhóm cộng tác đồng thời với hệ thống kiểm soát phiên bản (version control) được tích hợp, trong khi các mô hình định giá trả-theo-mức-sử-dụng¹³ loại bỏ chi tiêu vốn (capital expenditure) trả trước và mở rộng/thu hẹp linh hoạt theo nhu cầu (elastic with demand).
Một quan niệm sai lầm thường gặp cho rằng tài nguyên tính toán khổng lồ của ML đám mây giúp nó ưu việt hơn trong mọi trường hợp. Sức mạnh tính toán và khả năng lưu trữ vượt trội không tự động dịch thành những giải pháp tối ưu cho mọi ứng dụng. Bất biến trọng lực dữ liệu (data gravity invariant) trong phần B.1.1 giải thích lý do tại sao: khi khối lượng dữ liệu mở rộng, chi phí cho việc di chuyển nó tới nơi tính toán (𝐶_move(𝐷_vol) ≫ 𝐶_move(Tính_toán)) cuối cùng sẽ chiếm thế thượng phong. Những sự đánh đổi được liệt kê trong định nghĩa trước đó trở nên cụ thể khi chúng ta xem xét nơi các triển khai vùng biên và nhúng (embedded deployments) thể hiện sự xuất sắc: phản hồi thời gian thực với việc ra quyết định dưới 10 ms trong các vòng lặp điều khiển tự động, quyền riêng tư dữ liệu nghiêm ngặt đối với thiết bị y tế xử lý dữ liệu bệnh nhân, chi phí có thể dự đoán được thông qua khoản đầu tư phần cứng một lần so với các khoản phí đám mây định kỳ, hoặc việc vận hành trong các môi trường ngắt kết nối


================ PAGE 93 ================

2. Hệ thống ML
55
Hình 2.4: Quy mô Trung tâm Dữ liệu Đám mây: Các hàng tủ máy chủ (server racks) được thắp sáng bằng đèn LED xanh lam trải dài khắp sàn trung tâm dữ liệu Google Cloud TPU. Nguồn ảnh: (Google DeepMind 2024).
14
GDPR (General Data Protection Regulation - Quy định Chung về Bảo vệ Dữ liệu): Khuôn khổ quyền riêng tư của EU (2018) mà điều khoản "Quyền được Lãng quên" (Right to be Forgotten) của nó là một ràng buộc hệ thống dành riêng cho ML: việc xóa dữ liệu của người dùng có thể đòi hỏi phải huấn luyện lại bất kỳ mô hình nào đã học từ dữ liệu đó, vì các bản cập nhật trọng số (weight updates) không thể bị đảo ngược từng cái một, biến một yêu cầu pháp lý thành một chi phí tính toán (compute cost).
15
HIPAA (Health Insurance Portability and Accountability Act - Đạo luật về Tính Lưu động và Trách nhiệm Giải trình Bảo hiểm Y tế): Đạo luật này của Hoa Kỳ biến các biện pháp an ninh—mã hóa, kiểm soát truy cập, giám sát—thành chi phí hệ thống trực tiếp: tính toán bị cô lập, ghi nhật ký (logging) trên mỗi lần suy luận không thể sửa đổi (immutable), và mã hóa đầu cuối (end-to-end encryption). Các biện pháp bảo vệ này thường bổ sung thêm 15–30 phần trăm vào chi phí cơ sở hạ tầng và chi phí phát sinh vận hành đối với một hệ thống ML sản xuất.
(disconnected environments) như các thiết bị công nghiệp ở những khu vực hẻo lánh. Mô hình triển khai tối ưu phụ thuộc vào các yêu cầu ứng dụng cụ thể thay vì chỉ khả năng tính toán thô.
2.5.2 Các sự đánh đổi và ràng buộc của ML đám mây
Những lợi thế của ML đám mây mang theo những sự đánh đổi vốn có sẽ định hình các quyết định triển khai. Độ trễ là yếu tố hệ quả (consequential) nhất: độ trễ vòng khứ hồi mạng từ 100–500 ms làm cho quá trình xử lý đám mây không phù hợp với các ứng dụng thời gian thực yêu cầu phản hồi dưới 10 ms, chẳng hạn như xe tự hành và hệ thống điều khiển công nghiệp. Thời gian phản hồi không thể dự đoán làm phức tạp thêm việc giám sát hiệu suất và gỡ lỗi (debugging) trên các cơ sở hạ tầng phân tán về mặt địa lý.
Quyền riêng tư và an ninh đặt ra những thách thức nghiêm trọng cho việc triển khai đám mây. Việc truyền dữ liệu nhạy cảm đến các trung tâm dữ liệu từ xa tạo ra các lỗ hổng (vulnerabilities) và làm phức tạp việc tuân thủ quy định (regulatory compliance). Các tổ chức xử lý dữ liệu chịu sự điều chỉnh của các quy định như Quy định Chung về Bảo vệ Dữ liệu (GDPR)¹⁴ hoặc Đạo luật về Tính Lưu động và Trách nhiệm Giải trình Bảo hiểm Y tế (HIPAA)¹⁵ phải thực hiện các biện pháp an ninh toàn diện bao gồm mã hóa, kiểm soát truy cập nghiêm ngặt, và giám sát liên tục (continuous monitoring) để đáp ứng các yêu cầu xử lý dữ liệu khắt khe. Các phương pháp bảo tồn quyền riêng tư (privacy-preserving approaches) có thể làm giảm lượng dữ liệu nhạy cảm phải rời khỏi môi trường gốc của nó, nhưng chúng bổ sung cho thay vì thay thế các cơ chế kiểm soát đám mây (cloud controls) này.
Việc quản lý chi phí đem đến sự phức tạp trong khâu vận hành, đòi hỏi phải phân tích TCO¹⁶ thay vì những phép so sánh chi phí đơn vị ngây ngô. Một so sánh TCO thực tế giữa đám mây và biên (cloud vs. edge) minh họa cho khoảng cách giữa mức giá niêm yết (sticker price) và chi phí hệ thống thực sự.
Đối với so sánh thực tế, bảng 2.8 liệt kê các chi phí hàng năm về GPU, mạng, bộ cân bằng tải (load-balancer), và khả năng quan sát (observability) của một hoạt động triển khai đám mây minh họa dưới mức giá niêm yết công khai (public list pricing), và bảng 2.9 liệt kê các chi phí phần cứng, điện năng, làm mát, mạng, và nhân lực DevOps tương ứng của một hoạt động triển khai NVIDIA T4 cục bộ (on-premise).
Bảng 2.8: TCO Hàng năm của Suy luận Đám mây: Chi phí GPU, mạng, bộ cân bằng tải, và khả năng quan sát được liệt kê thành từng khoản mục cho việc triển khai khối lượng công việc thị giác quy mô ResNet-50 trên đám mây, với các tổng chi phí được sử dụng trong bài so sánh điểm hòa vốn.
Thành phần Chi phí
Công thức Tính
Chi phí Hàng năm
Suy luận GPU (A10G)
4 instances × 8760 h/năm × $0.75/h
~$26,280
Dữ liệu mạng đầu ra (Network egress)
100 GB/ngày × 365 ngày/năm × $0.09/GB
~$3,285
Bộ cân bằng tải (Load balancer)
$0.025/h + phí LCU
~$3,723
CloudWatch/logging (Ghi log)
Giám sát, cảnh báo (alerts)
~$2,000
Tổng Đám mây
~$35,288/năm


================ PAGE 94 ================

56
2.5 ML Đám mây: Sức mạnh Tính toán
Bảng 2.9: TCO Hàng năm của Suy luận Biên (Edge): Chi phí phần cứng, năng lượng, làm mát, mạng, và nhân công DevOps được liệt kê thành từng khoản cho việc triển khai thiết bị T4 tại chỗ (on-premise), cho thấy nhân công là thành phần chiếm ưu thế quyết định tính kinh tế hòa vốn (break-even economics) của hệ thống biên.
Thành phần Chi phí
Công thức Tính
Chi phí Hàng năm
Phần cứng CAPEX (Chi phí đầu tư)
$15,000 ÷ 3 năm tuổi thọ
~$5,000
Công suất (24/7)
300 W × 8760 h/năm × $0.12/kWh
~$315.4
Chi phí phát sinh Làm mát
~30% của năng lượng
~$94.6
Mạng (cáp quang)
Đường truyền cố định cho quản lý từ xa
~$1,200
Nhân công DevOps
0.1 FTE (Tương đương toàn thời gian) × Mức lương $150,000
~$15,000
Tổng Biên (Edge)
~$21,610/năm
Tính toán Nhanh 2.4: TCO Đám mây so với Biên
Bài toán: Một hệ thống thị giác phục vụ 1 triệu lần suy luận mỗi ngày ở quy mô ResNet-50 (độ trễ 10 ms, phản hồi 100 KB). Khi tính đến tất cả các chi phí (giờ sử dụng GPU, dữ liệu đầu ra mạng, năng lượng, làm mát, và nhân công, được liệt kê ở bảng 2.8 và bảng 2.9), việc triển khai đám mây hay triển khai tại biên tiết kiệm chi phí hơn trong 3 năm?
Tính toán: Phân tích hòa vốn (break-even analysis) trong phương trình 2.7 xác định khi nào việc triển khai tại biên trở nên hiệu quả về chi phí. Chi phí Cố định Biên (Edge Fixed Costs) bao gồm khấu hao phần cứng và bảo trì, Chi phí Biến đổi Đám mây trên mỗi Đơn vị (Cloud Variable Cost per Unit) là mức giá đám mây tính trên mỗi lần suy luận, và Công suất (Capacity) là tốc độ suy luận tối đa của hệ thống vùng biên:
Mức tận dụng hòa vốn = Chi phí Cố định Biên / (Chi phí Biến đổi Đám mây trên mỗi Đơn vị × Công suất) (2.7)
Trong kịch bản có công suất ổn định này, tổng chi phí vùng biên gần như hoàn toàn là chi phí cố định (fixed cost) trong khi tổng chi phí đám mây tỷ lệ với khối lượng (volume), do đó phép chia thu gọn lại thành tỷ lệ của hai mức tổng chi phí hàng năm:
~$21,610/năm ÷ ~$35,288/năm ≈ 61.24 phần trăm của điểm vận hành 1 triệu lượt/ngày, tức là khoảng 612K lượt suy luận/ngày.
Kết quả: Trên mức giao cắt (crossover) đó, thiết bị biên thắng.
Ở khối lượng tối đa (full volume), mức chênh lệch là ~$35,288/năm − ~$21,610/năm = ~$13,678/năm, khoảng 38.8 phần trăm hóa đơn đám mây; ở dưới mức giao cắt, tính co giãn (elasticity) của đám mây thường thắng.
Góc nhìn hệ thống: TCO của thiết bị biên bị chi phối bởi chi phí nhân công (~$15,000 ÷ ~$21,610/năm ≈ 69.4 phần trăm), chứ không phải phần cứng. Các tổ chức không có năng lực DevOps hiện hữu nên tính toán đến toàn bộ chi phí duy trì cơ sở hạ tầng cục bộ (on-premise infrastructure).
Các đợt triển khai đám mây cũng mang theo các ràng buộc về mặt vận hành. Những đợt tăng đột biến về mức độ sử dụng không thể đoán trước (Unpredictable usage spikes) làm phức tạp việc lập ngân sách, đòi hỏi phải có các khuôn khổ quản trị chi phí và giám sát toàn diện. Sự phụ thuộc vào mạng lưới tạo ra một ràng buộc khác: bất kỳ sự cố kết nối nào đều tác động trực tiếp đến tính khả dụng của hệ thống, đặc biệt là ở những nơi có khả năng truy cập mạng hạn chế hoặc không đáng tin cậy. Tình trạng khóa chặt vào nhà cung cấp (Vendor lock-in) làm vấn đề này trầm trọng hơn, vì sự phụ thuộc vào các công cụ và API cụ thể tạo ra những thách thức về tính di động (portability) khi chuyển đổi giữa các nhà cung cấp. Các tổ chức phải cân bằng những ràng buộc này với các lợi ích của đám mây dựa trên các yêu cầu ứng dụng cụ thể và khả năng chấp nhận rủi ro của họ. Ngay cả với những ràng buộc này, lợi thế tính toán của ML đám mây khiến nó trở nên không thể thiếu đối với các ứng dụng hướng tới người tiêu dùng (consumer applications) hoạt động ở quy mô toàn cầu.
2.5.3 Huấn luyện và suy luận quy mô lớn
Lợi thế tính toán của ML đám mây thể hiện rõ ràng nhất trong các ứng dụng hướng tới người tiêu dùng yêu cầu quy mô khổng lồ (massive scale). Các trợ lý ảo như Siri và Alexa minh họa cho các kiến trúc kết hợp (hybrid architectures) đặc trưng cho các hệ thống ML hiện đại: việc phát hiện từ đánh thức chạy trên phần cứng được thiết kế riêng có mức tiêu thụ điện năng thấp (thường dưới milliwatt) ngay trực tiếp trên thiết bị, cho phép luôn bật tính năng lắng nghe mà không làm hao pin; nhận dạng giọng nói ban đầu ngày càng chạy nhiều hơn trên thiết bị vì mục đích quyền riêng tư và khả năng phản hồi; và các tác vụ phức tạp


================ PAGE 95 ================

57
17
DLRM: Kiến trúc năm 2019 của Meta minh họa điển hình cho nguyên mẫu "Phân tán Thưa thớt" (Sparse Scatter). Các bảng nhúng cho các hệ thống đề xuất trong sản xuất có thể vượt quá 100 TB, khiến DLRM bị ràng buộc bởi dung lượng bộ nhớ và băng thông giao tiếp (communication BW) chứ không phải bởi 𝑅_peak thô. Sự đảo ngược này so với giả định bị giới hạn bởi tính toán (compute-bound) thông thường buộc phải có các thiết kế cụm máy (cluster designs) chuyên biệt nơi bộ nhớ, chứ không phải số học, mới là nguồn tài nguyên khan hiếm.
về hiểu biết và tạo lập ngôn ngữ tự nhiên sử dụng cơ sở hạ tầng đám mây để tiếp cận các mô hình lớn hơn và kiến thức rộng hơn.
Tính kinh tế (Economics) thúc đẩy kiến trúc này nhiều tương đương với độ trễ. Việc cố gắng xử lý các tương tác bằng giọng nói cho hàng tỷ thiết bị hoàn toàn trên đám mây sẽ va phải cả bức tường kinh tế và mức trần cơ sở hạ tầng. Việc định lượng mức trần trợ lý giọng nói (voice assistant wall) sẽ cho thấy cả hai giới hạn này cùng lúc.
Tính toán Nhanh 2.5: Mức trần trợ lý giọng nói
Bài toán: 1 tỷ thiết bị trợ lý giọng nói (điện thoại thông minh, loa thông minh, tai nghe không dây) mỗi thiết bị đưa ra 20 truy vấn/ngày dưới dạng lưu lượng từ đánh thức (wake-word traffic). Chi phí mở rộng cơ sở hạ tầng sẽ là bao nhiêu nếu tất cả các truy vấn đều được phục vụ từ ML đám mây, và tải cao điểm (peak load) sẽ cần bao nhiêu trung tâm dữ liệu chuyên dụng?
Bức tường kinh tế: Đầu tiên, chi phí phục vụ lưu lượng từ đánh thức từ đám mây.
• Chi phí đám mây: ~$0.50/thiết bị/năm → 1 tỷ thiết bị = 500,000,000 USD/năm. Không thể chấp nhận được về mặt kinh tế đối với một tính năng miễn phí.
• Lựa chọn thay thế TinyML: Phát hiện từ đánh thức cục bộ 0.1–1 mW, <$0.01/thiết bị/năm. Khả thi ở mọi quy mô.
Bức tường cơ sở hạ tầng: Thứ hai, số lượng trung tâm dữ liệu mà tải cao điểm sẽ yêu cầu.
Lập luận kinh tế thì mang tính thuyết phục, nhưng lập luận vật lý lại mang tính quyết định:
1. Khối lượng truy vấn: 1 tỷ thiết bị × 20 truy vấn/ngày = 20 tỷ truy vấn/ngày.
2. Nhu cầu GPU: Mỗi truy vấn yêu cầu ~200 ms thời gian GPU. Tổng cộng: 1,111,111 giờ/ngày.
3. Dung lượng trung tâm dữ liệu: Một trung tâm dữ liệu lớn (~10,000 GPU) cung cấp 240,000 giờ/ngày.
4. Yêu cầu trung bình: ~4.6 trung tâm dữ liệu chuyên dụng chỉ dành cho suy luận giọng nói.
5. Thực tế cao điểm: Truy vấn tập trung vào những giờ thức giấc (~4.5× tỷ lệ cao điểm so với trung bình), yêu cầu ~20.8 trung tâm dữ liệu lúc cao điểm.
Bức tường băng thông: Thứ ba, tính chất vật lý của việc di chuyển chính âm thanh đó. Nếu các thiết bị truyền âm thanh trực tiếp (streamed audio) lên đám mây (16 kHz, 16-bit), mỗi thiết bị truyền ~32 KB/s. Trên 1 tỷ thiết bị: 32 TB/s, một tỷ lệ đáng kể của tổng dung lượng mạng đường trục (internet backbone capacity) toàn cầu.
Góc nhìn hệ thống: Quá trình xử lý giọng nói chỉ dựa vào đám mây không chỉ đơn thuần là đắt đỏ; nó là bất khả thi về mặt vật lý ở quy mô toàn cầu. Phát hiện từ đánh thức cục bộ là một yêu cầu tất yếu của cơ sở hạ tầng, không phải là một sự tối ưu hóa.
Đường ống trợ lý giọng nói minh họa cho một nguyên tắc cốt lõi của hệ thống: các quyết định triển khai bị ràng buộc bởi các yêu cầu về hiệu suất, thực tế kinh tế, và tính chất vật lý của cơ sở hạ tầng. Phương pháp tiếp cận kết hợp (hybrid approach) giảm thiểu độ trễ đầu cuối so với quá trình xử lý đám mây thuần túy, trong khi vẫn duy trì được sức mạnh tính toán cần thiết để hiểu ngôn ngữ phức tạp, tất cả đều nằm trong ranh giới chi phí bền vững.
Các công cụ đề xuất được triển khai bởi Netflix và Amazon minh họa cho cùng một mức giá đám mây dưới hình thức bị giới hạn bởi dung lượng bộ nhớ. Các hệ thống này xử lý những bộ dữ liệu khổng lồ sử dụng lọc cộng tác (collaborative filtering) và các kiến trúc học sâu như DLRM¹⁷ để khám phá các mẫu hình trong sở thích của người dùng. DLRM là ví dụ điển hình cho một khối lượng công việc bị giới hạn bởi dung lượng bộ nhớ: các bảng nhúng khổng lồ của nó, đại diện cho hàng triệu người dùng và danh mục, có thể vượt quá dung lượng terabyte, yêu cầu bộ nhớ phân tán trên nhiều máy chủ chỉ để lưu trữ các tham số mô hình. Tài nguyên tính toán đám mây cho phép cập nhật và tinh chỉnh liên tục khi lượng dữ liệu người dùng tăng lên, với việc Netflix xử lý hơn 100 tỷ điểm dữ liệu hàng ngày để đưa ra các đề xuất nội dung được cá nhân hóa, giúp trực tiếp nâng cao mức độ tương tác của người dùng.
Các ứng dụng này chia sẻ một điểm chung: chúng đánh đổi độ trễ để lấy quy mô, chấp nhận hàng trăm mili-giây độ trễ vòng khứ hồi (round-trip delay) để đổi lấy khả năng truy cập vào các tài nguyên tính toán mà không một mô hình nào khác có thể cung cấp. Các hệ thống phát hiện gian lận phân tích hàng triệu giao dịch, các công cụ đề xuất xử lý quy mô terabyte của các bảng nhúng, và các mô hình ngôn ngữ tạo văn bản từng token một, tất cả đều dựa vào món hời này. Tuy nhiên, như bức tường trợ lý giọng nói đã chứng minh, có những ứng dụng mà không một lượng điện toán đám mây nào có thể bù đắp được cho quy luật vật lý của khoảng cách. Khi ngân sách độ trễ giảm xuống dưới mức tốc độ ánh sáng cho phép, hoặc khi lượng dữ liệu vượt quá khả năng truyền dẫn của mạng lưới, việc tính toán buộc phải chuyển đến gần nguồn dữ liệu hơn.


================ PAGE 96 ================

58
2.6 ML Vùng biên: Độ trễ và Quyền Riêng tư
18
IoT Công nghiệp (IIoT): Một lĩnh vực mà các ràng buộc về độ trễ được thiết lập bởi an toàn vật lý, chứ không phải do nhận thức của người dùng. Mức trễ vòng khứ hồi 100+ ms vừa đề cập là không thể chấp nhận được đối với một cánh tay robot buộc phải dừng lại trong vòng 5 ms sau khi phát hiện một con người. Điều này buộc việc tính toán phải chuyển về vùng biên (edge), đánh đổi lấy độ trễ mạng gần bằng không để chịu những ràng buộc tính toán trên thiết bị (𝑅_peak) đáng kể.
Dữ liệu vùng biên thô có thể rộng hơn đường truyền (pipe) của mạng lưới.
2.6 ML Vùng biên (Edge ML): Độ trễ và Quyền Riêng tư (Latency and Privacy)
Khi ngân sách độ trễ giảm xuống dưới 100 ms, cơ sở hạ tầng đám mây va phải một bức tường vật lý cứng rắn. Hình phạt khoảng cách có nghĩa là chỉ riêng tốc độ ánh sáng đã áp đặt mức độ trễ tối thiểu 40–150 ms đối với các yêu cầu liên vùng (cross-region)—trước cả khi bất kỳ việc tính toán nào bắt đầu. Khi một chiếc xe tự hành cần quyết định xem có nên phanh hay không, hoặc một robot công nghiệp cần phải dừng lại trước khi va vào chướng ngại vật, 100 ms là cả một khoảng thời gian dài vô tận. Phản hồi kỹ thuật hợp lý (logical engineering response) là di chuyển tính toán lại gần nguồn dữ liệu hơn.
ML Vùng biên nổi lên từ ràng buộc này, đánh đổi các tài nguyên tính toán không giới hạn để lấy độ trễ dưới 100 ms và khả năng lưu giữ dữ liệu cục bộ. Dưới khía cạnh nguyên mẫu (archetype), quá trình triển khai vùng biên biến đổi mục tiêu tối ưu hóa: một khối lượng công việc Kẻ ngốn Băng thông như suy luận LLM, vốn bị giới hạn bộ nhớ trên đám mây, sẽ trở thành bị giới hạn bởi độ trễ (latency-bound) ở biên, nơi mà mức phạt mạng 50–100 ms lấn át thời gian tính toán 10–20 ms. Phần cứng vùng biên với đủ bộ nhớ cục bộ có thể loại bỏ hoàn toàn khoản phạt này, dịch chuyển nút thắt cổ chai quay trở lại với ràng buộc băng thông bộ nhớ cơ sở (underlying memory bandwidth constraint). Nhớ lại quy luật sắt từ phương trình 2.6: bằng cách xử lý cục bộ, triển khai vùng biên loại bỏ hoàn toàn thành phần 𝐷_vol/BW_IO (I/O mạng lưới), thu gọn độ trễ thành max(𝐷_vol/BW, 𝑂 / (𝑅_peak ⋅ 𝜂_hw)) + 𝐿_lat—vẫn là sự đánh đổi giữa bộ nhớ và tính toán, nhưng không bị hình phạt mạng lưới chi phối giống như trong suy luận đám mây.
Mô hình chuyển đổi (paradigm shift) này đóng vai trò thiết yếu đối với các ứng dụng nơi mà sự chậm trễ khứ hồi từ đám mây (cloud round-trip delays) là không thể chấp nhận. Các hệ thống tự trị yêu cầu ra quyết định trong tích tắc (split-second) và các ứng dụng IoT công nghiệp¹⁸ yêu cầu phản hồi theo thời gian thực không thể chịu đựng độ trễ mạng. Tương tự, các ứng dụng chịu sự quản lý của các quy định nghiêm ngặt về chủ quyền hoặc quyền riêng tư dữ liệu (data sovereignty or privacy constraints) phải xử lý thông tin ngay tại cục bộ thay vì truyền tải nó đến các trung tâm dữ liệu ở xa. Thiết bị biên (các cổng và hub IoT) chiếm giữ vị trí trung gian trong phổ triển khai, duy trì hiệu suất ở mức có thể chấp nhận được trong khi vận hành dưới những ràng buộc tài nguyên ở mức trung bình (intermediate).
Sự đánh đổi ưu-tiên-tính-cục-bộ (locality-first trade-off) này định nghĩa mô hình vùng biên.
Định nghĩa 2.2: ML Vùng biên (Edge ML)
Học máy Vùng biên là mô hình triển khai được tối ưu hóa cho Tính tất định của Độ trễ (Latency Determinism) và Tính cục bộ của Dữ liệu (Data Locality) bằng cách định vị quy trình tính toán kế bên (physically adjacent) các nguồn dữ liệu.
1. Ý nghĩa: Nó lách qua (circumvents) Hình phạt Khoảng cách (𝐿_lat) của đám mây, đánh đổi khả năng mở rộng quy mô (elastic scale) để lấy một Năng lực Tính toán Cục bộ (𝑅_peak) cố định.
2. Sự khác biệt: Khác với ML Đám mây, vốn ưu tiên Thông lượng (Throughput), ML vùng biên ưu tiên Tính tất định (Determinism) và quyền riêng tư. Không giống như TinyML, ML vùng biên vẫn có thể sử dụng các bộ tăng tốc cấp máy trạm (workstation-class accelerators) chẳng hạn như GPU đa năng (GPGPU).
3. Cạm bẫy phổ biến: Một quan niệm sai lầm phổ biến là cho rằng ML vùng biên ám chỉ một nhóm phần cứng (hardware class) cụ thể. Trong thực tế, nó là một Mô hình Vị trí (Location Paradigm): nó trải dài từ các cổng IoT cho đến các máy chủ cục bộ, được thống nhất (unified) bởi sự gần gũi vật lý (physical proximity) đối với nguồn dữ liệu.
Xử lý phi tập trung (Decentralized processing) giúp giảm độ trễ và áp lực băng thông, nhưng nó cũng đẩy các bài toán về bảo trì và an ninh ra những phần cứng phân tán, những thứ khó bảo mật hơn so với một trung tâm dữ liệu tập trung (hình 2.5).
Lợi ích của việc sử dụng ít băng thông hơn và giảm độ trễ trở nên rõ rệt khi chúng ta kiểm tra các tốc độ dữ liệu (data rates) trong thế giới thực. Đặc điểm xác định của việc triển khai vùng biên ít liên quan đến việc quá trình xử lý diễn ra ở đâu mà liên quan đến việc vị trí đó phải xử lý khối lượng dữ liệu bao nhiêu (how much data that location must handle). Khi tốc độ dữ liệu vượt quá năng lực hiện có của mạng, nút thắt cổ chai về băng thông hệ quả (resulting bandwidth bottleneck) sẽ buộc quá trình xử lý phải chuyển ra vùng biên bất kể những cân nhắc khác.
Tính toán Nhanh 2.6: Nút thắt cổ chai băng thông
Bài toán: Xem xét một hệ thống kiểm soát chất lượng cho một xưởng nhà máy với 100 camera đang chạy ở 30 FPS cùng độ phân giải 1080p. Truyền phát video trực tiếp (video streaming) có trở thành nút thắt cổ chai băng thông không, và ML Vùng biên có giúp giảm băng thông đủ để có thể xử lý tại cục bộ không?
Vật lý học:


================ PAGE 97 ================

59
Ràng buộc Cốt lõi (Binding Constraint)
Phản hồi Hệ thống (System Response)
Ranh giới Thất bại (Failure Boundary)
Các Khối lượng công việc Phù hợp (Workloads That Fit)
ML Vùng biên
Phản hồi dưới 100 ms (Sub-100 ms Response)
Dữ liệu thô rộng hơn mạng (Raw Data Wider Than Network)
Dữ liệu Phải Giữ Cục bộ (Data Must Stay On Premises)
Trang web phải Vận hành Ngoại tuyến (Site Must Operate Offline)
Đặt Tính toán Gần Cảm biến (Place Compute Near Sensors)
Lọc Dữ liệu Trước khi Tải lên (Filter Data Before Upload)
Sử dụng Bộ tăng tốc Cục bộ (Use Local Accelerators)
Đồng bộ hóa các Bản tóm tắt (Synchronize Summaries)
Năng lực Cục bộ Cố định (Fixed Local Capacity)
Bảo mật Thiết bị Phân tán (Distributed Device Security)
Quản lý Đội xe (Fleet Management)
Điều phối Cập nhật Mô hình (Model Update Coordination)
IoT Công nghiệp (Industrial IoT)
Phân tích Video Bán lẻ (Retail Video Analytics)
Xe Tự hành (Autonomous Vehicles)
Chẩn đoán Hình ảnh Bệnh viện (Hospital Imaging)
Hình 2.5: Bản đồ Ràng buộc ML Vùng biên: Việc di chuyển tính toán lại gần dữ liệu giúp loại bỏ thành phần độ trễ mạng và giảm áp lực băng thông, nhưng nó thay thế quy mô tập trung bằng năng lực cục bộ cố định, sự phơi nhiễm bảo mật phi tập trung (distributed security exposure), và mức độ phức tạp về mặt vận hành trên nhiều trang web.
19
Bức tường Dữ liệu IoT (IoT Data Wall): McKinsey ước tính rằng các đợt triển khai IoT có thể tạo ra hàng nghìn tỷ đô la giá trị kinh tế vào năm 2030, nhưng những đợt triển khai đó phụ thuộc vào các luồng cảm biến liên tục từ những thiết bị được phân tán khắp các ngôi nhà, nhà máy, trang trại, phương tiện, và cơ sở hạ tầng (McKinsey Global Institute 2021). Ở rất nhiều nơi trong số đó, khối lượng 𝐷_vol tổng cộng từ các luồng thô áp đảo ngân sách đường truyền lên (uplink budget) hoặc ngân sách độ trễ đối với việc thu nhận dữ liệu tập trung (centralized ingestion), khiến quá trình xử lý ở biên tại cục bộ trở thành một yêu cầu mang tính kiến trúc chứ không chỉ đơn thuần là tối ưu hóa chi phí.
1. Tốc độ dữ liệu thô trên mỗi camera: 1920 × 1080 × 3 byte × 30 FPS ≈ 186.6 MB/s.
2. Tổng tốc độ dữ liệu: 100 camera × 186.6 MB/s = 18.7 GB/s.
3. Rủi ro chuyển tiếp trên đám mây (Cloud transfer exposure): Việc tải lên các luồng dữ liệu camera thô chủ yếu là một bài toán về băng thông, mức tiếp nhận (ingest), lưu trữ, và xử lý; phí dữ liệu chuyển ra (egress charges) của đám mây tính trên mỗi GB sẽ được áp dụng khi dữ liệu được truyền ngược ra khỏi đám mây. Nếu luồng dữ liệu thô sau đó được tải về (retrieved) với mức giá dữ liệu-chuyển-ra là $0.09/GB, thì riêng khoản phí truyền dẫn sẽ đạt tới 4.4 triệu USD/tháng.
4. Thực tế mạng lưới: Ngay cả một đường truyền 10 Gbps (1.25 GB/s) dành riêng (dedicated line) cũng không thể gánh được tải—khối lượng công việc đòi hỏi mức băng thông lớn hơn mức băng thông thực tế 14.9 lần.
Góc nhìn hệ thống: Vật lý học đã khiến cho việc truyền trực tiếp lên đám mây (cloud streaming) đối với ứng dụng này là bất khả thi. Việc xử lý tại vùng biên (Edge processing) không phải là một sự lựa chọn—đó là yêu cầu bắt buộc. Nếu một máy chủ vùng biên chỉ truyền siêu dữ liệu khiếm khuyết (1 KB cho mỗi lần phát hiện với mức độ khoảng 20 sự kiện/giây trên toàn nhà máy), băng thông sẽ giảm đi khoảng 933,120 lần.
Phép tính toán băng thông vừa rồi cho thấy lý do tại sao xử lý vùng biên là bắt buộc đối với các đợt triển khai cảm biến khối lượng lớn. Đối với các thiết bị vùng biên chạy bằng pin (camera không dây, thiết bị bay không người lái drone, thiết bị đeo), ràng buộc này thậm chí còn khắt khe hơn: như phần "Năng lượng cho sự Truyền dẫn" (phần 2.3.1) đã khẳng định, năng lượng để truyền dẫn vô tuyến (radio transmission) tốn kém hơn 1,000 lần so với suy luận cục bộ, khiến việc chuyển đổi sang đám mây (cloud offloading) là không thể về mặt vật lý đối với các thiết bị chạy bằng pin bất kể mức băng thông khả dụng là bao nhiêu. Hình 2.6 định lượng sự bất đối xứng này xuyên suốt các tầng (tiers) triển khai.
2.6.1 Lợi ích và thách thức triển khai của ML Vùng biên
ML Vùng biên bao phủ các thiết bị đeo (wearables), cảm biến công nghiệp, và thiết bị gia dụng thông minh chuyên xử lý dữ liệu cục bộ¹⁹ mà không phải phụ thuộc vào các máy chủ trung tâm. Khoảng trống 8 cấp số nhân về năng lượng trong hình 2.6 không phải là một khiếm khuyết kỹ thuật có thể tối ưu hóa để loại bỏ; nó phản ánh các chi phí không thể tiêu giảm cho quá trình di chuyển dữ liệu, làm mát, và chi phí phát sinh mạng lưới vốn chia rẽ các tầng triển khai.
Chính ranh giới năng lượng tương tự cũng trở thành ranh giới cho kích thước mô hình. Do các thiết bị vùng biên hoạt động trong những phạm vi công suất khắt khe, mức băng thông bộ nhớ từ 25–100 GB/s của chúng thường tương ứng với các mô hình có thể triển khai ở mức từ 100 MB–1 GB các tham số. Ràng buộc đó thúc đẩy các kỹ thuật tối ưu hóa được đề cập trong Chương 10, đạt được tốc độ tăng từ 2–4 lần bằng cách nén (compressing) các mô hình để vừa với các ngân sách phần cứng này. Phần lợi ích vươn ra ngoài phạm vi chỉ là về tính toán (compute): việc xử lý nguồn cấp camera thô cục bộ có thể giúp tránh được nhu cầu về đường truyền tốc độ cấp terabit bởi vì dữ liệu thô không bao giờ rời khỏi thiết bị, giúp giảm bớt các chi phí lưu trữ, xử lý, và chuyển đổi từ đám mây mang tính định kỳ.


================ PAGE 98 ================

60
2.6 ML Vùng biên: Độ trễ và Quyền Riêng tư
Năng lượng trên mỗi lần Suy luận (J)
TinyML: Nhận diện Từ khóa (~10 µJ)
Di động (Mobile): MobileNetV2 (NPU) (~50 mJ)
Biên (Edge): ResNet-50 (Jetson) (~500 mJ)
Đám mây (Cloud): ResNet-50 (server) (~10 J)
Đám mây (Cloud): Truy vấn GPT-4 (~1 kJ)
Chênh lệch 100,000,000 lần
Hình 2.6: Năng lượng cho Mỗi lần Suy luận Qua Các Mô hình Triển khai: Tổng năng lượng tiêu thụ của hệ thống cho mỗi lần suy luận trải dài qua 8 cấp số nhân, từ ~10 µJ cho tính năng nhận diện từ khóa của TinyML lên đến ~1 kJ cho một truy vấn LLM trên đám mây. Khoảng cách này không phải là một thiếu sót kỹ thuật—nó phản ánh tính chất vật lý của quá trình di chuyển dữ liệu, làm mát, và chi phí phát sinh về mạng, chia cắt các tầng triển khai. Sự chênh lệch 100,000,000 lần này lý giải vì sao cảm biến luôn-bật (always-on sensing) chỉ khả thi ở tầng TinyML.
2.6.2 Bất biến về tính cục bộ của dữ liệu (The data locality invariant)
Quyết định giữa xử lý ở vùng biên cục bộ hay xử lý trên đám mây từ xa được chi phối bởi sự đánh đổi giữa băng thông và độ trễ: dữ liệu bắt buộc phải giữ ở cục bộ khi thời gian để truyền dẫn nó lớn hơn tổng thời gian dành cho xử lý từ xa (bao gồm cả độ trễ mạng và tính toán từ xa).
Định nghĩa 2.3: Bất biến về tính cục bộ của dữ liệu
Bất biến về Tính cục bộ của Dữ liệu chỉ ra rằng một khối lượng công việc đòi hỏi xử lý cục bộ bất cứ khi nào thời gian truyền dẫn dữ liệu vượt quá thời gian xử lý nó từ xa:
𝐷_vol / BW_network > 𝐿_lat,network + 𝑂 / (𝑅_peak,remote ⋅ 𝜂_hw,remote)
Trong đó, BW_network là băng thông mạng khả dụng cho đường truyền chuyển giao (offload path), 𝐿_lat,network là thành phần độ trễ mạng của nó, và 𝑅_peak,remote cùng 𝜂_hw,remote là mức tính toán tối đa và hiệu suất phần cứng của bộ xử lý từ xa.
1. Ý nghĩa: Bất biến này xác định một điểm giao cắt mà nếu vượt qua đó, việc bổ sung thêm tính toán từ xa (𝑅_peak) sẽ mang lại lợi ích bằng 0 vì đường truyền mạng (BW_network) không thể cung cấp đủ nhanh khối lượng dữ liệu (𝐷_vol). Khi phía bên trái của bất đẳng thức (inequality) chiếm ưu thế, cách duy nhất để giảm độ trễ là đưa xử lý tính toán lại gần dữ liệu hơn, chứ không phải làm cho bộ xử lý từ xa tính toán nhanh hơn.
2. Sự khác biệt: Không giống như quy luật sắt phân tách thời gian thực thi thành các thành phần cộng hợp (additive terms) cho mọi khối lượng công việc, bất biến về tính cục bộ của dữ liệu là một bài kiểm tra khả thi nhị phân (binary feasibility test): nó xác định xem chuyển giao từ xa có khả thi về mặt kiến trúc hay không trước khi bắt tay vào tối ưu hóa bất kỳ thành phần đơn lẻ nào.
3. Cạm bẫy phổ biến: Một quan niệm sai lầm phổ biến là cho rằng 5G/6G có thể "giải quyết" tính cục bộ. Mặc dù các công nghệ này cải thiện BW_network, nhưng chúng không làm giảm 𝐿_lat,network xuống dưới ngưỡng sàn tốc độ ánh sáng, có nghĩa là các tác vụ đòi hỏi sự khắt khe về độ trễ (latency-critical tasks) về bản chất vẫn mang tính cục bộ (inherently local) bất kể băng thông liên kết có lớn như thế nào.
Điểm giao cắt về tính cục bộ dễ nhận thấy nhất bằng cách so sánh một khung hình cảm biến có tốc độ cao đơn lẻ với ngân sách khứ hồi cho quy trình xử lý từ xa.


================ PAGE 99 ================

61
20
Các Ràng buộc của Máy chủ Vùng biên (Edge Server Constraints): Phần cứng vùng biên thường cung cấp bộ nhớ từ 1–8 GB và công suất 5–50 W, thấp hơn khoảng 100 lần so với các máy chủ đám mây ở cả hai phương diện. Những ràng buộc này giới hạn kích thước mô hình có thể triển khai ở mức hàng triệu (không phải hàng tỷ) tham số, khiến các kỹ thuật nén trong Chương 10 trở nên cần thiết để đạt được các chu kỳ hoạt động suy luận bền vững trong phạm vi nhiệt (thermal envelope).
21
Phối hợp Đội xe Vùng biên (Edge Fleet Coordination): Việc quản lý hàng ngàn thiết bị biên phân tán đưa ra các chế độ lỗi vắng bóng trong đám mây tập trung: khả năng kết nối gián đoạn gây ra hiện tượng sai lệch phiên bản mô hình (model version drift), tính không đồng nhất của phần cứng đòi hỏi tối ưu hóa cho từng mục tiêu, và khả năng tiếp cận vật lý làm cho việc hạ cấp phần sụn (firmware rollbacks) trở nên đắt đỏ. Những mô hình vận hành này được xem xét trong Chương 14.
Tính toán Nhanh 2.7: Điểm giao cắt tính cục bộ
Bài toán: Liệu hệ thống tránh vật cản của thiết bị bay không người lái (4K, 60 FPS) có nên chuyển dữ liệu lên đám mây, hay đây trở thành điểm giao cắt tính cục bộ?
Cho trước:
• Dữ liệu (𝐷_vol): Một khung hình 4K ≈ 24.9 MB.
• Băng thông (BW_network): Băng thông rộng gia đình 100 Mb/s (tốc độ tải lên - up).
• Phản hồi từ xa (𝐿_lat,network + 𝑇_remote): 110 ms (khứ hồi + tính toán từ xa).
Tính toán:
1. Thời gian truyền dẫn: 24.9 MB × 8 bit / 100 Mb/s = 1,990.7 ms.
2. Phản hồi từ xa: 110 ms.
Góc nhìn hệ thống: Vì 1,990.7 ms ≫ 110 ms, hệ thống bị nghẽn (blocked) băng thông. Đám mây có thể có một bộ xử lý vô hạn (𝑅_peak = ∞), nhưng thiết bị bay vẫn sẽ va chạm vì nó không thể di chuyển các bit đủ nhanh. Khối lượng công việc này bắt buộc phải xử lý cục bộ.
Vật lý học ép buộc sự lựa chọn về mặt kiến trúc; các sự đánh đổi kỹ thuật cũng tuân theo nó. Lợi ích tức thời nhất là độ trễ: thời gian phản hồi giảm từ mức khứ hồi hàng trăm mili-giây của đám mây xuống còn 1–50 ms ở vùng biên, giúp các ứng dụng an toàn-tới-cùng (safety-critical) đòi hỏi phản hồi thời gian thực trở nên khả thi.
Tiết kiệm băng thông càng làm tăng thêm lợi thế này—một cửa hàng bán lẻ với 50 camera đang phát video có thể giảm yêu cầu truyền dẫn từ 100 Mbps (tốn kém 1,000–2,000 USD hàng tháng) xuống dưới 1 Mbps bằng cách xử lý cục bộ và chỉ truyền các siêu dữ liệu (metadata), giảm tới 99 phần trăm. Đổi lại, quyền riêng tư được tăng cường, vì quá trình xử lý cục bộ loại bỏ rủi ro truyền dẫn và đơn giản hóa việc tuân thủ các quy định. Đối với các triển khai trong công nghiệp, khả năng phục hồi vận hành (operational resilience) là một lợi thế quyết định: các hệ thống tiếp tục hoạt động kể cả khi mất mạng, một đặc tính thiết yếu cho các ứng dụng sản xuất, chăm sóc sức khỏe, và quản lý tòa nhà, nơi mà thời gian ngưng hoạt động (downtime) mang lại hậu quả lập tức về chi phí.
Những lợi ích này kéo theo những hạn chế tương ứng sẽ chồng chất khi quy mô triển khai tăng lên. Nguồn tài nguyên tính toán hạn chế²⁰ kìm hãm mạnh mẽ mức độ phức tạp của mô hình: các máy chủ biên thường cung cấp thông lượng xử lý kém hơn từ một cấp số nhân (an order of magnitude) trở lên so với cơ sở hạ tầng đám mây, giới hạn các mô hình có thể triển khai ở mức hàng triệu tham số thay vì hàng tỷ. Quản lý các mạng lưới phân tán giới thiệu độ phức tạp tăng phi tuyến tính (nonlinearly) theo quy mô triển khai, bởi vì việc điều phối phiên bản kiểm soát (version control) và các bản cập nhật trên hàng ngàn thiết bị đòi hỏi hệ thống điều phối tinh vi²¹, và tính không đồng nhất về phần cứng trên các nền tảng đa dạng yêu cầu những chiến lược tối ưu hóa khác nhau cho từng mục tiêu.
Một đợt triển khai bán lẻ thực tế (realistic retail deployment) cho thấy cách những ràng buộc đó chuyển đổi thành thông lượng, phần cứng, và các yêu cầu chi phí đội xe (fleet-cost requirements). Xét một chuỗi bán lẻ thông minh triển khai tính năng phát hiện người trên 500 cửa hàng, mỗi cửa hàng có 20 camera chạy ở 15 FPS. Bảng 2.10 nối cấp (cascades) tốc độ suy luận mỗi cửa hàng qua số lượng FLOP mỗi khung hình của YOLOv8-nano để đưa ra thông lượng mà mỗi cửa hàng phải duy trì.
Bảng 2.10: Yêu cầu định cỡ (sizing requirements) suy luận Biên: Mục tiêu thông lượng trên mỗi cửa hàng cho kịch bản phát hiện người trong hệ thống bán lẻ thông minh.
Số liệu đo lường (Metric)
Cách tính
Kết quả
Suy luận mỗi cửa hàng
20 camera/cửa hàng × 15 FPS
300 lượt suy luận/s
Khối lượng tính toán mô hình
YOLOv8-nano: 8.7 GFLOP/suy luận
2610 GFLOP/s
Thông lượng yêu cầu
2610 GFLOP/s × 2 (khoảng trống - headroom)
Tương đương ~5.22 TOPS
Bảng 2.11 chấm điểm ba ứng cử viên tăng tốc vùng biên (edge accelerators), bao gồm các bộ tăng tốc GPU nhúng, dựa trên mục tiêu thông lượng.
Bảng 2.11: Tùy chọn bộ tăng tốc Biên: Thông lượng, công suất, và chi phí cho ba ứng cử viên tăng tốc vùng biên ở quy mô toàn hệ thống (fleet scale).
Thiết bị Biên
INT8 TOPS
Công suất
Chi phí Đơn vị
Chi phí Hệ thống (Fleet Cost)
NVIDIA Jetson Orin NX
100 TOPS
10–25 W
$600
$300,000
Intel NUC + Movidius
1 TOPS
15 W
$400
$200,000


================ PAGE 100 ================

62
2.6 ML Vùng biên: Độ trễ và Quyền Riêng tư
22
Amazon Go: Việc sử dụng máy chủ vùng biên cục bộ của hệ thống là phản hồi trực tiếp đối với lượng dữ liệu khổng lồ từ hàng trăm camera tại cửa hàng. Kiến trúc này giúp tránh việc phải tải lên những video thô—có thể làm nghẽn một đường truyền (uplink) tải lên gigabit—đồng thời vẫn giữ được đoạn phim (footage) nhạy cảm về khách hàng ngay tại nơi đó. Thiết kế ưu tiên vùng biên (edge-first) trở thành bắt buộc bởi vì quy mô khổng lồ của dữ liệu được xử lý, có thể vượt qua 1 TB mỗi giờ tại một cửa hàng đơn lẻ.
23
Công nghiệp 4.0 (Industry 4.0): Cuộc cách mạng công nghiệp lần thứ tư tích hợp ML vào các vòng lặp phản hồi cảm biến-chấp hành (sensor-actuator feedback loop) trên nền nhà máy. Hậu quả cho hệ thống là độ trễ của vòng lặp điều khiển (𝐿_lat) phải ngắn hơn chính quy trình vật lý mà nó kiểm soát: một robot hàn phát hiện một khiếm khuyết tại mức 60 Hz có 16.7 ms để ngừng lại, một ngân sách mà chỉ suy luận vùng biên (edge inference) mới có thể đáp ứng.
24
Bảo trì Dự đoán (Predictive Maintenance): Các mô hình phân tích dữ liệu cảm biến tần số cao (ví dụ: độ rung, nhiệt độ) để dự báo hỏng hóc ở các thiết bị, qua đó cho phép theo dõi đồng thời hàng ngàn tài sản. "Mức độ phức tạp bổ sung khi triển khai" (additional deployment complexity) được nhắc tới xuất phát trực tiếp từ yêu cầu vùng biên đòi hỏi quy trình suy luận trên thiết bị hoạt động liên tục 24/7. Điều này đặt ra một ngân sách khắt khe về công suất, nơi toàn bộ cảm biến và mô hình thường phải vận hành ở dưới mức một watt, đây là một giới hạn trọng tâm thúc đẩy thiết kế kiến trúc mô hình và các quyết định nhằm thu gọn bộ nhớ byte (byte-reduction).
Thiết bị Biên
INT8 TOPS
Công suất
Chi phí Đơn vị
Chi phí Hệ thống (Fleet Cost)
Google Coral Dev (3 bảng mạch/cửa hàng)
tối đa 12 TOPS; suy giảm (derated) còn 6 TOPS
6 W
$450
$225,000
Tính toán Nhanh 2.8: Định cỡ suy luận Biên
Bài toán: Dựa vào mục tiêu thông lượng ở bảng 2.10 và các lựa chọn ở bảng 2.11, bộ tăng tốc vùng biên nào (TPU quy mô USB, GPU nhúng cấp máy trạm, hay PC mini đa năng) cung cấp đủ thông lượng yêu cầu với mức chi phí tổng thể cho ba năm thấp nhất?
Tính toán: Việc định cỡ phải bắt đầu từ khối lượng công việc mà một bảng mạch có thể duy trì được, không phải những gì ghi trên tài liệu thông số kỹ thuật tối đa. Bảng mạch Coral Dev được quảng cáo ở mức 4 TOPS tối đa nhưng thực tế phân phối chỉ khoảng 2 TOPS sau khi áp dụng tỷ lệ suy giảm (derating) 50%, do đó số lượng cho mỗi cửa hàng là: 5.22 TOPS yêu cầu ÷ 2 TOPS mỗi mạch = 2.6 mạch, sẽ làm tròn thành 3 bảng mạch/cửa hàng.
Qua 3 năm ở 500 cửa hàng, so sánh TCO (tổng chi phí sở hữu) cho cấu hình này là: Phần cứng $225,000 + Điện năng (0.006 kW × 500 × 8760 giờ/năm × 3 năm × $0.12/kWh = $9,460.8) = $234,460.8 so với quá trình suy luận đám mây là ~$9,855,000.
Kết quả: Chỉ một bảng mạch Coral thì quá thiếu công suất, nhưng cấu hình chia mảnh (sharded) gồm 3 bảng mạch/cửa hàng là lựa chọn vùng biên chi phí thấp, cung cấp 6 TOPS và tiết kiệm chi phí đầu tư (capex) phần cứng khoảng 1.3 lần so với cấu hình Jetson. Jetson vẫn là giải pháp triển khai trên thiết bị đơn nhất (single-device) đơn giản hơn nếu sự phức tạp trong việc tích hợp được coi trọng hơn là tiết kiệm chi phí phần cứng.
Góc nhìn hệ thống: Việc thiết lập kích thước vùng biên là một bài toán về công suất và chi phí, chứ không phải bài toán về thương hiệu thiết bị. Cấu hình rẻ và khả thi nhất có thể là nhiều bộ tăng tốc cỡ nhỏ lắp đặt tại mỗi địa điểm thay vì dùng một tấm bảng lớn hơn, tuy nhiên, phần cứng tiết kiệm này cũng phải được đánh giá đối trọng cùng gánh nặng trong việc vận hành bảo trì và đồng bộ với cả một hệ thống các thiết bị biên phân mảnh.
Những thách thức bảo mật ngày càng lớn do các thiết bị biên có thể dễ dàng tiếp cận được về mặt vật lý: các trang thiết bị phân phối trong những cửa hàng bán lẻ hoặc cơ sở hạ tầng công cộng gặp phải nhiều rủi ro bị thao túng (tampering) so với những trung tâm dữ liệu khép kín, yêu cầu những cơ chế bảo vệ phần cứng chặt chẽ như thiết bị khởi động bảo mật (secure boot), lưu trữ mã hóa, cùng vỏ thiết bị chống sự xâm phạm (tamper-evident enclosures). Các chi phí lắp đặt ban đầu có thể từ $500–2,000 ở mỗi máy chủ vùng biên tạo ra tích lũy chi phí trải dọc ở mọi vị trí: thiết bị hệ thống lắp đặt ở 1,000 điểm yêu cầu khoảng tiền $500,000–2,000,000 ngay lập tức, mặc dù chi phí cơ sở hạ tầng (capital) này sẽ bù đắp được chi phí cho vận hành lâu dài, giảm thiểu xuống nhiều nếu đem đi đối sánh cùng chi phí trên hệ thống dữ liệu điện toán.
2.6.3 Các hệ thống IoT và công nghiệp thời gian thực
Các phần mềm hỗ trợ vùng biên thì thay đổi thông qua từng không gian chuyên ngành khác nhau (domain), nhưng mỗi một bộ sẽ mang lý do bảo vệ sự xử lý về mặt vị trí tính toán này làm cốt yếu: các cơ cấu không thể cứ mãi mong chờ về phía thông tin qua truyền tin kỹ thuật, không thể gửi số liệu thô quá lớn, không được bỏ ngỏ tín hiệu (expose), hay chẳng được ngừng nghỉ giữa quá trình (outage). Các phương tiện có tính chủ động không người (autonomous vehicles) là tiêu biểu đại diện trong lĩnh vực những phần mềm đòi hỏi gắt gao nhất, với việc khi những nhận định được ra có thể tác động tức tốc một cách không mảy may chần chừ tới quy chuẩn bảo hộ mạng sống cần xuất hiện qua phần nghìn giây đồng hồ đặt nền bằng số liệu các thông số máy không thể gửi gắm qua một máy điện toán từ xa nọ. Các quá trình ví như quy trình Hỗ Trợ Đầy Đủ (Full Self-Driving) xử lý dữ liệu truyền lại về của rất nhiều những máy ảnh với vận tốc luồng khung lớn nhờ vào các bộ xử lý công suất thuộc vùng biên mà người kỹ sư lập trình, đưa quyết định vận hành cho đường xá có sự chậm trễ đến tận cùng rơi vào chừng các phân mảnh của mili giây thời khắc (milliseconds). Dạng dấp về mức phản hồi tốc độ này đơn giản trở thành viển vông nếu chỉ còn biết dựa qua hệ thống đám mây, do mức trễ của mạng.
Môi trường cửa tiệm mua bán cho thấy lợi điểm thực dụng từ phương pháp ML Vùng biên cho các hệ thống phần mềm tốn cao năng lượng dẫn tốc mà vẫn lưu trữ những hình ảnh không lan tỏa ngoài cá nhân (privacy-sensitive). Các khu vực như Amazon Go²² phải tự đưa thuật tính định qua những đoạn ghi video có số lượng hàng trăm những bảng máy, kiểm dò di chuyển mà mỗi người thao tác và mỗi vật dụng họ vạch tới đưa tính năng có mặt (enable) cho mô hình rời khu không kiểm tra trả hóa đơn. Quá trình xử lý mang tư tưởng ở vùng biên (edge-based) thực hiện đưa ra cả về những quan tâm thuộc lĩnh vực kỹ thuật tới đời sống. Quy trình vận chuyển truyền số liệu lớn cho video tới từ đa dạng camera yêu cầu (require) duy trì mạnh về đường lưu thông băng thông (bandwidth), khi mà sự tính giải nội dung giúp bảo đảm đoạn phân ảnh (video) cơ bản vẫn trụ bên trong khu vực đó, tháo gỡ nhiều lỗ hỗng phơi bày mà giản hóa tính tương thích phù hợp ở mức cấp độ cao.
Phần hệ thống Mạng Điện Từ Công Nghiệp (Industrial IoT²³) tận dụng nền tảng của ML Vùng biên cho các ứng dụng thực thi mà điểm mấu chốt mili-giây nhạy cảm kết dính mang hàm ảnh hưởng rất mạnh theo quy trình năng lượng với sự chuẩn tắc làm ăn trong giới kỹ sư lao động. Những không gian chế tác này vận hành toàn bộ phân khúc quy mô sử dụng vùng biên qua từng phần mềm với một mảng giám định tính theo phút giây quy củ, cùng hệ quang phổ đo được (vision systems) khả năng phát hiện ở chỗ hàn lên tốc độ hơn 60 linh kiện của mỗi một phần thời gian ngắn một phút và các dự kiến bảo trì hệ cơ cấu²⁴ tính từ quá trình theo gót của hơn 10,000 cấu kết làm ăn tại mỗi điểm khu. Ở vô số khu vực thực thi xây dựng sản xuất, hệ thống mô hình ấy đã và đang dẫn minh việc hạn chế từ 25–35 phần trăm số lỗi vô tình không lường dừng chạy máy—những đúc kết lưu trữ mà qua đó đền bù xứng hợp được cho tất cả các phần gia tăng cấu kiện lắp ráp vận hành của quá trình thiết lập.


================ PAGE 101 ================

63
25
Nhiếp ảnh Tính toán (Computational Photography): Sử dụng các thuật toán ML (ví dụ: kết hợp nhiều khung hình - multi-frame fusion, khử nhiễu nơ-ron - neural denoising) để vượt qua những giới hạn vật lý của cảm biến camera nhỏ trên thiết bị di động. Điều này minh họa cho sự đánh đổi trong điện toán di động, khi một đường ống gồm 10–15 mô hình phải thực thi trong khoảng thời gian trễ màn trập (shutter delay) mà người dùng có thể cảm nhận được (~200 ms) trong khi phải tuân thủ một ngân sách nhiệt dùng chung khắt khe 3–5 W.
26
Thu giảm Mô hình Thị giác Di động (Mobile Vision Model Reduction): Các kiến trúc kiểu MobileNet giảm bớt khối lượng tính toán trong các lớp thị giác thông thường trong khi vẫn duy trì được độ chính xác hữu ích cho các tác vụ di động. Các chi tiết kiến trúc sẽ xuất hiện trong Chương 6; điểm hệ thống ở đây là việc triển khai trên thiết bị di động thường đòi hỏi phải thay đổi họ mô hình (model family), chứ không đơn thuần chỉ là chuyển cùng một mô hình lên điện thoại.
Các tòa nhà thông minh sử dụng ML vùng biên để tối ưu hóa việc tiêu thụ năng lượng trong khi vẫn duy trì tính liên tục của hoạt động trong suốt những thời gian mất mạng (network outages). Các tòa nhà thương mại được trang bị hệ thống quản lý tòa nhà dựa trên biên xử lý dữ liệu từ hàng nghìn cảm biến giám sát nhiệt độ, mật độ người, chất lượng không khí, và việc sử dụng năng lượng. Điều này làm giảm yêu cầu truyền dẫn lên đám mây xuống một cấp số nhân (order of magnitude) hoặc hơn trong khi vẫn cho phép thời gian phản hồi dưới một giây. Tương tự, các ứng dụng chăm sóc sức khỏe sử dụng ML vùng biên để theo dõi bệnh nhân và hỗ trợ phẫu thuật, duy trì sự tuân thủ HIPAA thông qua quá trình xử lý cục bộ trong khi vẫn hỗ trợ các luồng công việc (workflows) có độ trễ thấp phục vụ cho việc hướng dẫn theo thời gian thực (real-time guidance).
Các ứng dụng này đều chia sẻ một giả định chung: thiết bị biên nằm cố định và được cắm vào nguồn điện (wall power). Nhớ lại quy luật sắt trong phương trình 2.6: triển khai vùng biên đã loại bỏ thành phần mạng 𝐷_vol/BW_IO vốn chi phối quá trình suy luận đám mây, nhưng nó vẫn giả định năng lượng là không giới hạn. Việc một máy chủ vùng biên trong nhà máy tiêu thụ hàng trăm watt suốt ngày đêm không có gì đáng nói khi nó được kết nối với nguồn điện lưới (mains power).
Tuy nhiên, hàng tỷ người dùng lại mang theo các thiết bị điện toán của họ di chuyển khắp nơi, và những thiết bị đó chạy bằng ngân sách pin cố định. Khi chúng ta chuyển từ cơ sở hạ tầng biên cố định sang chiếc điện thoại thông minh nằm trong túi người dùng, một thành phần mới tham gia vào quá trình tối ưu hóa: Năng lượng (Energy) = Công suất (Power) × 𝑇. Ràng buộc chiếm ưu thế sẽ chuyển từ độ trễ sang năng lượng cho mỗi lần suy luận, và cùng với đó là toàn bộ bài toán kỹ thuật (engineering calculus) thay đổi.
2.7 ML Di động (Mobile ML): Trí tuệ Ngoại tuyến (Offline Intelligence)
ML Vùng biên giải quyết vấn đề khoảng cách vốn hạn chế các đợt triển khai đám mây, đạt được độ trễ dưới 100 ms thông qua quá trình xử lý cục bộ. Tuy nhiên, các thiết bị biên vẫn bị trói buộc với cơ sở hạ tầng cố định—các cổng (gateways), máy chủ nhà máy, hệ thống biên cửa hàng bán lẻ. Người dùng không đứng yên một chỗ, vì vậy AI của họ cũng vậy.
Để mang khả năng ML tới những người dùng đang di chuyển, chúng ta phải giải quyết một ràng buộc khác: pin. Khác với các máy chủ biên cắm điện có thể liên tục tiêu thụ hàng trăm watt, các thiết bị di động phải hoạt động trong nhiều giờ hoặc nhiều ngày dựa trên các ngân sách năng lượng cố định.
ML Di động giải quyết thách thức này bằng cách tích hợp máy học trực tiếp vào các thiết bị di động (portable devices) như điện thoại thông minh và máy tính bảng, cung cấp cho người dùng các khả năng được cá nhân hóa theo thời gian thực. Mô hình này xuất sắc khi tính riêng tư của người dùng, hoạt động ngoại tuyến, và khả năng phản hồi tức thời trở nên quan trọng hơn sự tinh vi trong tính toán (computational sophistication), hỗ trợ các ứng dụng như nhận dạng giọng nói, nhiếp ảnh tính toán²⁵, và theo dõi sức khỏe trong khi vẫn duy trì sự riêng tư của dữ liệu thông qua quá trình tính toán trên thiết bị (on-device computation). Các thiết bị chạy bằng pin này phải cân bằng giữa hiệu suất với hiệu quả sử dụng năng lượng và quản lý nhiệt độ (thermal management), khiến chúng phù hợp với các tác vụ AI có thời lượng ngắn (short-duration) nhưng xảy ra thường xuyên.
Môi trường di động mang tới một ràng buộc khắt khe không tồn tại trong các hoạt động triển khai cố định: năng lượng cho mỗi lần suy luận trở thành một tham số thiết kế hàng đầu. Theo quy luật sắt ở phương trình 2.6, hệ thống đám mây và biên tối ưu hóa nhằm cực tiểu hóa 𝑇, tổng độ trễ. Các hệ thống di động phải đối mặt với một ràng buộc bổ sung: Năng lượng = Công suất × 𝑇, và bức tường năng lượng được mô tả bởi phương trình 2.2 giới hạn công suất duy trì ở mức 3–5 W. Theo thuật ngữ nguyên mẫu, một khối lượng công việc Quái thú Tính toán như phân loại hình ảnh phải được chuyển đổi thành một mô hình thị giác nhỏ gọn hơn²⁶, giảm bớt FLOP đi 13.7 lần trong khi vẫn bảo tồn đủ độ chính xác cho ứng dụng. Đây không chỉ đơn thuần là tối ưu hóa; nó đại diện cho sự thay đổi về mặt bản chất (qualitative shift) trong sự đánh đổi giữa tính toán trên mỗi byte, chấp nhận mức thông lượng (peak throughput) thấp hơn để đổi lấy khả năng vận hành bền vững trong phạm vi nhiệt 3–5 W.
Ranh giới về nhiệt độ và pin này định hình hình thức đặc trưng của mô hình di động.
Định nghĩa 2.4: ML Di động (Mobile ML)
Học máy Di động là mô hình triển khai bị giới hạn bởi Công suất Thiết kế Nhiệt (Thermal Design Power - TDP) và năng lượng pin.
1. Ý nghĩa: Nó bị ràng buộc bởi khả năng tản nhiệt mức độ vài watt của công nghệ làm mát thụ động (passive cooling), đòi hỏi các kiến trúc ưu tiên hiệu suất năng lượng duy trì ổn định thay vì thông lượng tối đa (𝑅_peak).
2. Sự khác biệt: Khác với ML Vùng biên, vốn có thể có tính năng làm mát chủ động (active cooling), ML di động phải hoạt động trong phạm vi Ngân sách Năng lượng Cá nhân (Personal Energy Budget). Khác với TinyML, nó vẫn cung cấp một Hệ điều hành phong phú và năng lực tính toán cấp đa watt (multi-watt).
3. Cạm bẫy phổ biến: Một quan niệm sai lầm thường gặp là cho rằng hiệu suất của ML di động là một giá trị cố định. Trên thực tế, nó là một Ràng buộc Biến đổi theo Thời gian (Time-Varying Constraint): hiệu suất thường giảm xuống khi thiết bị va phải giới hạn nhiệt của nó, kích hoạt sự điều tiết (throttling) làm giảm chu kỳ hoạt động (𝜂_hw).


================ PAGE 102 ================

64
2.7 ML Di động: Trí tuệ Ngoại tuyến
Hiệu suất nhiệt duy trì (sustained thermal performance) thường thấp hơn nhiều so với các đỉnh bùng nổ (burst peaks).
Sự tích hợp cảm biến và quá trình xử lý trên thiết bị mang lại khả năng phản hồi thời gian thực và những thuộc tính riêng tư mạnh mẽ hơn, nhưng thời lượng pin và khả năng tính toán hạn chế buộc các kỹ sư phải ưu tiên hiệu quả duy trì (sustained efficiency) hơn là hiệu suất tối đa (raw performance) (hình 2.7).
Những ràng buộc về nguồn tài nguyên và thời lượng pin được liệt kê trước đó chuyển trực tiếp thành các yêu cầu kỹ thuật. Các tính năng ML luôn-bật (always-on) phải chịu một khoản mà chúng tôi gọi là thuế pin (battery tax), bởi vì quá trình suy luận liên tục tiêu tốn ngân sách năng lượng hữu hạn của chiếc điện thoại ngay cả trước khi phần còn lại của hệ thống chạy.
Tính toán Nhanh 2.9: Thuế pin
Bài toán: Hãy xem xét việc triển khai một bộ phát hiện vật thể nền (background object detector) "thời gian thực" trên một chiếc điện thoại thông minh. Mô hình này tiêu thụ 2 W điện năng liên tục khi hoạt động. Chiếc điện thoại có một viên pin 15 Wh tiêu chuẩn. Tính năng này có thể bật cả ngày được không? Đây chính là thuế pin vốn biến thời lượng pin thành một ràng buộc về ngân sách năng lượng của ML di động.
Vật lý học:
1. Thời gian chạy lý tưởng: 15 Wh / 2 W = 7.5 giờ
2. Thực tế: Một người dùng kỳ vọng điện thoại của họ sẽ tồn tại được 24 giờ. Việc chạy liên tục một tính năng đơn lẻ này trong một ngày sẽ đòi hỏi 320 phần trăm ngân sách năng lượng hàng ngày của điện thoại.
Góc nhìn hệ thống: Mô hình không thể chỉ đơn giản là được "triển khai". Các kỹ thuật trong Chương 10 phải giảm thiểu cả khối lượng công việc mô hình và chu kỳ làm việc (duty cycle) để tính năng này có thể hoạt động cả ngày.
Ràng buộc Cốt lõi (Binding Constraint)
Phản hồi Hệ thống (System Response)
Ranh giới Thất bại (Failure Boundary)
Các Khối lượng công việc Phù hợp (Workloads That Fit)
ML Di động
Ngân sách Pin Dùng chung (Shared Battery Budget)
Phạm vi Nhiệt Thụ động (Passive Thermal Envelope)
Dữ liệu Cảm biến Riêng tư (Private Sensor Data)
Người dùng Ngoại tuyến hoặc Đang di chuyển (User Is Offline or Moving)
Chạy Suy luận trên Thiết bị (Run Inference on Device)
Sử dụng NPU và Các Kernel Tích hợp (Use NPU and Fused Kernels)
Nén Mô hình và Các kích hoạt (Compress Model and Activations)
Điều tiết theo Trạng thái Nhiệt (Throttle by Thermal State)
Thuế Pin (Battery Tax)
Điều tiết Nhiệt (Thermal Throttling)
Giới hạn Lưu trữ và Bộ nhớ (Storage and Memory Limits)
Phân mảnh Cập nhật Nền tảng (Platform Update Fragmentation)
Nhiếp ảnh Tính toán (Computational Photography)
Giọng nói và Dịch thuật (Speech and Translation)
Theo dõi Sức khỏe (Health Monitoring)
Cá nhân hóa (Personalization)
Hình 2.7: Bản đồ Ràng buộc ML Di động: Quá trình xử lý trên thiết bị đem lại sự phản hồi nhanh chóng, tính riêng tư, hoạt động ngoại tuyến, và sự cá nhân hóa, nhưng pin dùng chung và phạm vi nhiệt thụ động của điện thoại làm cho hiệu quả năng lượng duy trì trở thành ràng buộc thiết kế chi phối.
Ràng buộc pin giới hạn tổng mức tiêu thụ năng lượng theo thời gian. Tuy nhiên, ngay cả khi chúng ta có thể phớt lờ thời lượng pin (chẳng hạn, đối với một máy tính bảng đang cắm điện hoặc một bản demo ngắn), một định luật vật lý thứ hai sẽ can thiệp: nhiệt động lực học. Mỗi watt tính toán biến thành một watt nhiệt cần phải được tản đi. Trong một trung tâm dữ liệu, các hệ thống làm mát khổng lồ loại bỏ lượng nhiệt này. Trong một thiết bị di động mỏng, kín và không có quạt, đường dẫn nhiệt duy nhất là xuyên qua lớp vỏ kính và kim loại ra không khí xung quanh. Điều này tạo ra bức tường nhiệt, một mức trần cứng cản trở mức tiêu thụ điện năng duy trì tồn tại độc lập với dung lượng pin.
Sự phân biệt này quan trọng đối với các quyết định kỹ thuật: thuế pin là một vấn đề về ngân sách, về nguyên tắc có thể giải quyết được bằng cách giảm bớt tần suất hoạt động của mô hình hoặc tăng dung lượng pin. Bức tường nhiệt lại là một mức trần vật lý. Không có một chu kỳ làm việc nào, không có một viên pin lớn hơn nào, và không có một sự tối ưu hóa phần mềm nào có thể nâng giới hạn công suất (watt) duy trì tối đa mà một bộ khung tản nhiệt thụ động (passive chassis) có thể tỏa đi. Một mô hình vượt quá phạm vi nhiệt sẽ kích hoạt sự điều tiết (throttling) phần cứng chỉ trong vài giây, bất kể pin còn lại bao nhiêu năng lượng. Do đó, hai ràng buộc này tấn công vào những điểm khác nhau trong quy luật sắt: pin giới hạn tổng số phép toán trên mỗi lần sạc (𝑂 tích lũy theo thời gian), trong khi bức tường nhiệt giới hạn mức thông lượng tức thời (instantaneous rate - 𝑅_peak ⋅ 𝜂_hw) mà silicon có thể duy trì.


================ PAGE 103 ================

2. Hệ thống ML
65
27
Đơn vị Xử lý Nơ-ron (NPU): Một khối phần cứng chuyên dụng trên một Hệ thống-trên-Chip (System-on-Chip) di động mà các mạch của nó được thiết kế độc quyền cho phép nhân ma trận độ chính xác thấp. Sự chuyên môn hóa này giúp tránh được logic lệnh tiêu tốn nhiều điện năng của CPU, mang lại mức hiệu suất năng lượng (TOPS/W) tăng 10–100 lần, cho phép thông lượng AI cao nằm gọn trong ngân sách công suất duy trì <500 mW vô cùng khắt khe của một thiết bị di động.
28
Hệ thống-trên-Chip (System-on-Chip - SoC): Bằng cách tích hợp các lõi CPU, GPU, và NPU với bộ nhớ dùng chung trên một die đơn nhất, chi phí năng lượng vật lý cho việc di chuyển dữ liệu được tối thiểu hóa. Sự tích hợp chặt chẽ này đặt ra ràng buộc về băng thông bộ nhớ, qua đó giới hạn các mô hình di động ở quy mô 10–100 MB. Thiết kế này là bắt buộc đối với thời lượng pin bởi vì việc truy cập bộ nhớ ngoài-chip (off-chip) tiêu tốn năng lượng nhiều hơn >100 lần so với truy cập trên-chip (on-chip).
29
Face ID: Hệ thống sinh trắc học của Apple chiếu 30,000 chấm hồng ngoại để lập bản đồ khuôn mặt 3D, được xử lý hoàn toàn bên trong Secure Enclave, một bộ đồng xử lý mật mã (cryptographic coprocessor) bị cô lập mà hệ điều hành (OS) chính thậm chí cũng không thể truy cập bộ nhớ của nó. Các mẫu sinh trắc học không bao giờ rời khỏi thiết bị. Kiến trúc này đạt được tỷ lệ chấp nhận sai 1:1,000,000 trong khi loại bỏ được hoạt động truyền qua mạng—thứ vốn có thể tạo ra cả hình phạt độ trễ lẫn bề mặt phơi nhiễm (surface) vi phạm dữ liệu, minh họa rằng các ràng buộc trên-thiết-bị có thể đồng thời củng cố quyền riêng tư và cải thiện độ chính xác.
30
Đường ống Chế độ Chân dung (Portrait Mode Pipeline): Đây không phải là một mô hình đơn lẻ mà là một chuỗi (sequence) các mô hình thời gian thực để ước lượng chiều sâu, phân vùng (segmentation), và kết xuất (rendering). Vấn đề kỹ thuật cốt lõi là quản lý tổng độ trễ và điện năng của đường ống, chứ không phải hiệu suất của bất kỳ một mô hình riêng lẻ nào. Toàn bộ ngăn xếp (stack) 10–15 mô hình này phải được thực thi trong thời gian trễ màn trập mà người dùng cảm nhận được và cùng chia sẻ ngân sách nhiệt 3–5 W của điện thoại, buộc phải có những sự đánh đổi về mặt lập lịch (scheduling trade-offs) giữa CPU, GPU, và NPU để tránh bị điều tiết nhiệt.
Tính toán Nhanh 2.10: Bức tường nhiệt
Bài toán: Một mô hình thị giác chưa được tối ưu hóa yêu cầu thông lượng tính toán cao nhất 12 W. Liệu nó có thể được triển khai trên thiết bị di động, hay nó sẽ đụng phải bức tường nhiệt và bức tường năng lượng di động?
Kịch bản: Một hệ thống trên chip (SoC) di động cho phép làm mát thụ động ở mức khoảng 3 W. Giả sử mô hình chưa được tối ưu hóa vẫn được xuất xưởng (ships); một quá trình dò tìm điều tiết (throttling trace) tiêu biểu cho một thiết bị làm mát thụ động như vậy sẽ chạy qua ba bước:
1. Nhiệt độ tăng (Temperature rise): Ở mức 12 W, nhiệt độ thiết bị tăng khoảng 1 °C/s.
2. Điểm kích hoạt nhiệt (Thermal trip): Trong vòng 60 giây, phần cứng đạt đến Điểm Kích hoạt Nhiệt (Thermal Trip Point - 80 °C), kích hoạt tính năng điều tiết của HĐH.
3. Thông lượng bị điều tiết (Throttled throughput): Mô hình 100 FPS đột ngột giảm xuống còn 30 FPS để duy trì bên trong phạm vi nhiệt (thermal envelope).
Tính toán: Lượng tử hóa (Quantization) từ FP32 xuống INT8 (giảm độ chính xác số học xuống còn ít bit hơn cho mỗi trọng số; xem Chương 10) giúp cắt giảm khoảng 4 lần điện năng: 12 W ÷ 4 = 3 W, mức này vừa đúng với ngưỡng làm mát thụ động 3 W mà không còn bất kỳ khoảng trống (headroom) nào.
Góc nhìn hệ thống: Ngay cả khi đã giảm 4 lần điện năng cũng không tạo ra được khoảng trống nhiệt; nó mới chỉ vừa chạm đến giới hạn bền vững. Vật lý học đã thiết lập một ngưỡng sàn (trần) cứng mà không sự tối ưu hóa nào có thể vượt qua.
2.7.1 Lợi ích và các ràng buộc tài nguyên của ML Di động
Các thiết bị di động làm ví dụ điển hình cho những ràng buộc trung gian: 8–16 GB RAM (thay đổi từ tầm trung đến cao cấp), 128 GB–1 TB dung lượng lưu trữ, 15–45 TOPS khả năng tính toán AI thông qua các Đơn vị Xử lý Nơ-ron²⁷ tiêu thụ 3–5 W điện năng. Các kiến trúc Hệ-thống-trên-Chip²⁸ tích hợp tính toán và bộ nhớ nhằm tối thiểu hóa chi phí năng lượng. Băng thông bộ nhớ 60–100 GB/s giới hạn các mô hình trong khoảng 10–100 MB tham số, đòi hỏi các kỹ thuật tối ưu hóa quyết liệt (aggressive optimization techniques) mà Chương 10 trình bày chi tiết. Ràng buộc về pin (dung lượng 15 Wh–22 Wh) khiến việc tối ưu hóa năng lượng trở nên cực kỳ quan trọng: thêm 1 W quá trình xử lý ML liên tục vào một chiếc điện thoại vốn có thời lượng 24 giờ sẽ làm giảm thời gian chạy xuống còn khoảng 9.2 giờ–11.5 giờ, tùy thuộc vào dung lượng pin. Các khuôn khổ ML trên thiết bị (on-device) chuyên biệt cung cấp quá trình suy luận tối ưu hóa theo phần cứng cho phép thời gian phản hồi giao diện người dùng (UI) <5–50 ms.
ML Di động tỏ ra xuất sắc trong việc mang lại những trải nghiệm người dùng nhanh nhạy, bảo vệ quyền riêng tư. Quá trình xử lý thời gian thực có thể đạt độ trễ dưới 10 ms đối với một số tác vụ nhất định, cho phép thời gian phản hồi giao diện 5–50 ms trong các ứng dụng tương tác. Các thuộc tính quyền riêng tư mạnh mẽ hơn xuất hiện khi những thông tin đầu vào nhạy cảm được xử lý cục bộ, giảm thiểu sự truyền tải dữ liệu và việc lưu trữ tập trung, đồng thời các vùng an toàn (enclaves) trên thiết bị như Secure Enclave của Apple có thể bảo vệ thêm các quá trình tính toán nhạy cảm như xử lý sinh trắc học²⁹, dù sức mạnh của những bảo đảm về quyền riêng tư cuối cùng phụ thuộc vào thiết kế hệ thống tổng thể và mô hình rủi ro (threat model). Chức năng ngoại tuyến (Offline functionality) càng làm phân biệt di động so với đám mây: tính năng điều hướng (navigation), dịch thuật, và xử lý phương tiện đều chạy cục bộ trong phạm vi ngân sách tài nguyên di động, loại bỏ sự phụ thuộc vào mạng lưới. Sự cá nhân hóa (Personalization) hoàn thiện những lợi thế này, vì các mô hình có thể khai thác các tín hiệu trên thiết bị và ngữ cảnh của người dùng trong khi vẫn giữ dữ liệu thô cục bộ.
Những lợi ích này đòi hỏi việc phải chấp nhận các ràng buộc tài nguyên khắt khe. So với các đợt triển khai đám mây, các ứng dụng di động thường hoạt động trong các ngân sách chặt chẽ hơn nhiều về bộ nhớ, dung lượng lưu trữ, và độ trễ, điều này làm hạn chế kích thước mô hình và hành vi của lô (batch behavior). Thời lượng pin thể hiện tác động lên người dùng một cách rõ ràng, và việc điều tiết nhiệt (thermal throttling) có thể giới hạn đáng kể hiệu suất duy trì: thông lượng NPU tối đa thường cao hơn đáng kể so với mức có thể duy trì dưới các khối lượng công việc kéo dài (prolonged workloads). Sự phức tạp trong quá trình phát triển (Development complexity) nhân lên trên các nền tảng, đòi hỏi những bản triển khai riêng biệt và phải tinh chỉnh hiệu suất (performance tuning) một cách cẩn thận, trong khi sự không đồng nhất về thiết bị (device heterogeneity) yêu cầu phải có nhiều biến thể mô hình (model variants). Sự cản trở khi triển khai (Deployment friction) làm tăng thêm các thách thức: quy trình đánh giá ứng dụng của các cửa hàng ứng dụng (app store review processes) có thể mất vài ngày, làm chậm tốc độ lặp lại (iteration) so với các luồng công việc đám mây.
2.7.2 Trợ lý cá nhân và xử lý đa phương tiện
Qua các ứng dụng di động, vấn đề cốt lõi của hệ thống là việc nhiều đường ống (pipelines) ngắn phải cùng chia sẻ ngân sách năng lượng và nhiệt độ. Nhiếp ảnh tính toán minh họa cho thách thức của việc chạy nhiều đường ống ML trong một phạm vi nhiệt độ nhất định. Các mẫu điện thoại cao cấp hiện đại xử lý từng bức ảnh qua mười đến mười lăm mô hình ML riêng biệt trong thời gian thực: chế độ chân dung³⁰ sử dụng công cụ ước tính độ sâu (depth estimation) và


================ PAGE 104 ================

66
2.8 TinyML: Cảm biến Phổ quát (Ubiquitous Sensing)
31
Ngưỡng 1 mW: Dưới mức xấp xỉ một milliwatt, một thiết bị có thể được cấp nguồn vô thời hạn (indefinitely) bằng cách thu thập năng lượng xung quanh (ambient energy)—pin mặt trời có kích thước bằng ngón tay cái (~10 mW ngoài trời, ~10 µW trong nhà), máy phát nhiệt điện (thermoelectric generators) trên các đường ống ấm (~100 µW), hoặc năng lượng RF từ các máy phát sóng gần đó (~10 µW). Điểm giao cắt này biến đổi mô hình triển khai từ "thời gian sống bị giới hạn bởi pin" sang "triển khai và lãng quên", đó là lý do tại sao 1 mW không phải là một con số ngẫu nhiên mà là một ranh giới vật lý biến TinyML trở thành một mô hình khác biệt chứ không chỉ đơn thuần là một thiết bị biên được thu nhỏ (scaled-down).
32
Điện toán Phổ quát (Ubiquitous Computing): Tầm nhìn điện toán phổ quát của Mark Weiser tưởng tượng ra sự tính toán được đan xen vào các môi trường thường ngày cho đến khi nó rút lui khỏi sự chú ý trực tiếp của con người (Weiser 1991). TinyML là một con đường hiện đại tiến tới tầm nhìn đó: khi chi phí và điện năng của một cảm biến thông minh trở nên đủ thấp cho việc triển khai đại trà, mục tiêu tối ưu hóa sẽ chuyển từ hiệu suất (thông lượng) sang công suất (năng lượng cho mỗi lần suy luận), sự đánh đổi trọng tâm của nguyên mẫu Ràng buộc Nhỏ bé (Tiny Constraint archetype).
phân đoạn (segmentation), chụp chế độ ban đêm chụp và căn chỉnh chín đến mười lăm khung hình với bộ khử nhiễu dựa trên ML (ML-based denoising), cùng việc hợp nhất (merging) HDR, siêu phân giải, và tối ưu hóa cảnh chạy nối tiếp nhau (in sequence). Thách thức kỹ thuật không nằm ở bất kỳ mô hình riêng lẻ nào mà nằm ở đường ống: các mô hình này phải chia sẻ ngân sách công suất 3–5 W và hoàn thành trong thời gian trễ màn trập mà người dùng có thể nhận thấy, đòi hỏi việc lập lịch (scheduling) cẩn thận trên CPU, GPU, và NPU để tránh hiện tượng điều tiết nhiệt (thermal throttling).
Các tương tác bằng giọng nói thể hiện kiến trúc phân lớp (layered architecture) của ML di động. Tính năng phát hiện từ đánh thức chạy liên tục ở mức dưới 1 mW trên một lõi công suất thấp chuyên dụng, tính năng nhận dạng giọng nói hoạt động trên NPU ở mức độ trễ dưới 10 ms, và tính năng dự đoán bàn phím sử dụng các mô hình nơ-ron nhận thức-ngữ-cảnh (context-aware) để giảm thiểu nỗ lực gõ phím từ 30–40 phần trăm. Mỗi lớp hoạt động ở một mức công suất (power tier) khác nhau, minh họa cách ML di động phân vùng các khối lượng công việc qua các đơn vị xử lý không đồng nhất bên trong một SoC duy nhất.
Theo dõi sức khỏe và thực tế tăng cường (AR) thúc đẩy ML di động đến những giới hạn hiệu suất duy trì của nó. Các thiết bị đeo (Wearables) như Apple Watch xử lý toàn bộ dữ liệu điện tâm đồ (ECG) và gia tốc kế (accelerometer) ngay trên thiết bị để duy trì sự tuân thủ HIPAA, trong khi các khuôn khổ AR (AR frameworks) đòi hỏi thời gian khung hình duy trì ổn định dưới 16 ms ở 60 FPS cho việc định vị đồng thời (simultaneous localization), theo dõi bàn tay, và nhận thức bối cảnh (scene understanding). Những ứng dụng này đại diện cho mức trần mà các thiết bị chạy bằng pin, làm mát thụ động có thể duy trì, và chúng vạch ra ranh giới (boundary) mà vượt qua mức đó thì chỉ tối ưu hóa nền tảng di động thôi là không đủ.
Những thành công này có thể tạo ra một cảm giác dễ dàng gây hiểu lầm. Một cạm bẫy phổ biến liên quan đến việc cố gắng triển khai trực tiếp các mô hình được huấn luyện trên máy tính để bàn (desktop) sang các thiết bị di động hoặc thiết bị biên mà không thay đổi kiến trúc. Các mô hình được phát triển trên máy trạm mạnh mẽ thường thất bại khi được triển khai vào các thiết bị bị hạn chế tài nguyên. Một đường ống ResNet-50 trên máy tính để bàn có thể cần đến mức gigabyte một khi các mức kích hoạt (activations), các lô, bộ đệm tiền xử lý (preprocessing buffers), và chi phí thời gian chạy (runtime overhead) được tính đến, mặc dù chỉ riêng các trọng số FP32 đã vào khoảng 102.4 MB. Một đường ống như vậy, yêu cầu 4.1 GFLOP mỗi lần suy luận, không thể chạy mà không cần thay đổi trên một mục tiêu thiết bị biên cấp thấp tiêu biểu (representative low-end edge target) chỉ với 512 MB RAM và một bộ xử lý 1 GFLOP/s. Vượt lên trên những vi phạm nguồn tài nguyên đơn giản (simple resource violations), các mô hình được tối ưu hóa cho máy tính để bàn có thể sử dụng các phép toán không được phần cứng di động hỗ trợ, giả định các định dạng số không có sẵn trên hệ thống nhúng, hoặc yêu cầu xử lý lô vốn không tương thích với suy luận ảnh đơn (single-sample inference). Việc triển khai thành công đòi hỏi thiết kế kiến-trúc-nhận-thức (architecture-aware design) ngay từ đầu: các họ mô hình, định dạng số học, và lựa chọn thực hiện (implementation choices) tất cả đều phải khớp (match) với thiết bị mục tiêu.
ML Di động chứng minh rằng trí thông minh hữu ích có thể hoạt động trong một phạm vi nhiệt 3–5 W nhờ nguồn năng lượng pin. Tuy nhiên, điện thoại thông minh vẫn có giá hàng trăm đô la, cần hàng gigabyte bộ nhớ, và đòi hỏi sự chú ý của người dùng để sạc hàng ngày. Những yêu cầu này khiến chúng không phù hợp với một lượng lớn (vast class) các ứng dụng: theo dõi độ ẩm đất trên một trang trại rộng hàng ngàn mẫu Anh, phát hiện ứng suất (stress) cấu trúc trên các dây cáp cầu, hoặc lắng nghe âm thanh của các loài có nguy cơ tuyệt chủng trong một khu rừng xa xôi. Các kịch bản này đòi hỏi không chỉ công suất thấp hơn mà còn là một chế độ kỹ thuật hoàn toàn khác biệt về mặt định tính (qualitatively different engineering regime), nơi thiết bị chỉ có giá vài đô la thay vì hàng trăm, bộ nhớ được đo bằng kilobyte thay vì gigabyte, và hệ thống chạy tự động (unattended) trong nhiều tháng hoặc nhiều năm. Các phương pháp tối ưu hóa di động sẽ giúp ích, nhưng chúng không thể thu hẹp khoảng cách 10,000 lần về bộ nhớ sẵn có. Điều cần thiết không phải là một chiếc điện thoại thông minh được thu nhỏ (scaled-down smartphone) mà là một loại (class) phần cứng và thuật toán hoàn toàn khác biệt.
2.8 TinyML: Cảm biến Phổ quát (Ubiquitous Sensing)
Hãy tưởng tượng việc trang bị thiết bị cho (instrumenting) từng tấm pallet trong một nhà kho, từng dây cáp trên một cây cầu treo, từng tổ ong trong một khu nuôi ong. Để gắn "tai mắt" lên rất nhiều vật thể như vậy, từ hàng chục ngàn đến hàng triệu cái, thiết bị phải có giá tính bằng đơn vị đô la, chứ không phải hàng trăm đô la, và đo lường bằng milimet, chứ không phải centimet. Điện thoại thông minh thì quá đắt đỏ và cồng kềnh; thứ cần thiết là khả năng cảm biến phổ quát với kích thước bằng một con tem (postage stamp) và giá trị bằng một tách cà phê.
TinyML hoàn thiện phổ triển khai bằng cách đẩy trí tuệ đến giới hạn vật lý của nó: ML công suất thấp, chi phí thấp (low-cost, low-power ML) trên các thiết bị nhúng bị hạn chế sâu sắc (deeply constrained embedded devices) (Janapa Reddi, Plancher, et al. 2022). Trong phạm vi vận hành của cuốn sách này, các thiết bị có giá dưới 10 đô la và tiêu thụ dưới một milliwatt³¹ năng lượng sẽ làm cho cảm biến phổ quát³² trở nên khả thi về mặt kinh tế ở quy mô lớn; MLPerf Tiny và MCUNet chỉ ra cách các ràng buộc này được đánh giá và tối ưu hóa trong thực tế như thế nào (C. Banbury et al. 2021; Lin et al. 2020). Đây là lĩnh vực độc quyền (exclusive domain) của nguyên mẫu Ràng buộc Nhỏ bé (Tiny Constraint archetype), nơi mục tiêu tối ưu hóa dịch chuyển từ việc tối đa hóa thông lượng (throughput) sang việc tối thiểu hóa năng lượng cho mỗi lần suy luận. Theo các giả định về chu kỳ làm việc được sử dụng trong chương này, một mô hình nhận diện từ khóa (keyword spotting) tiêu thụ 10 µJ cho mỗi lần suy luận có thể hoạt động nhiều năm trên một cục pin đồng xu (coin-cell battery), đạt được mức cải thiện hiệu suất năng lượng lên tới hàng triệu lần bằng cách đánh đổi năng lực mô hình để lấy tuổi thọ vận hành (operational longevity).


================ PAGE 105 ================

67
33
Vi điều khiển (Microcontroller - MCU): Một máy tính trên một chip đơn (single-chip computer) mà thiết kế của nó ưu tiên tối thiểu hóa chi phí và điện năng hơn là hiệu suất, tạo ra "ràng buộc tận gốc" (radical constraint) đã được đề cập. Ràng buộc này là một mức trần bộ nhớ cứng (hard memory ceiling): các mô hình ML phải nằm trọn vẹn bên trong phạm vi kilobyte của SRAM trên-chip (ví dụ, 32–512 KB), do không có bộ nhớ ảo hay DRAM giống như trong các thiết bị di động. Ngưỡng tài nguyên sàn (resource floor) này, thường thấp hơn 1,000 lần so với của điện thoại thông minh, buộc phải phát triển các kiến trúc ML hoàn toàn mới, lấy bộ nhớ làm trung tâm (memory-centric).
34
Khoảng trống Năng lượng TinyML: Sự chênh lệch này bắt nguồn từ triết lý thiết kế phần cứng; các GPU đám mây được tối ưu hóa cho thông lượng (throughput) thô, tiêu thụ hàng trăm watt, trong khi vi điều khiển TinyML được thiết kế cho các trạng thái ngủ (sleep states) tiêu thụ năng lượng gần như bằng không. Đối với một tác vụ suy luận đám mây thông thường, một yêu cầu (request) có thể tiêu thụ ~1 joule, trong khi một thiết bị TinyML chuyên dụng sử dụng dưới một microjoule, tức là khoảng cách 1,000,000 lần. Các truy vấn LLM trên đám mây có thể đẩy sự so sánh này đi xa hơn nữa, như đã định lượng trong bảng 2.12.
35
Triển khai Pin Đồng xu (Coin-Cell Deployment): Một cục pin CR2032 (225 mAh ở 3 V, ~675 mWh) cấp nguồn cho một mô hình TinyML tiêu thụ 10–50 µW hoạt động trong 1–10 năm. Mô hình hoạt động "triển khai và lãng quên" này hạn chế các mô hình ở mức <100 KB (vừa vặn trên SRAM trên-chip) và thúc đẩy đổi mới trong điện toán ngắt quãng (intermittent computing), nơi thiết bị ngủ giữa các lần suy luận để kéo giãn ngân sách năng lượng qua nhiều năm vận hành tự động không cần giám sát.
Nơi ML di động yêu cầu phần cứng tinh vi với hàng gigabyte bộ nhớ và bộ xử lý đa lõi (multi-core processors), TinyML lại hoạt động trên các vi điều khiển³³ với hàng kilobyte RAM và mức giá trị giá chỉ vài đô la (C. Banbury et al. 2021; Lin et al. 2020). Ràng buộc cực đoan này buộc người ta phải có một cách tiếp cận hoàn toàn khác biệt đối với việc triển khai máy học, ưu tiên mức tiêu thụ năng lượng cực thấp (ultra-low power consumption) và chi phí tối thiểu so với mức độ tinh vi tính toán. Các hệ thống TinyML tiếp sức cho các ứng dụng như bảo trì dự đoán, giám sát môi trường, và nhận dạng cử chỉ đơn giản. Khoảng trống năng lượng giữa TinyML và suy luận đám mây (hình 2.6) kéo dài qua ít nhất sáu cấp số nhân³⁴ và đạt tới tám cấp số nhân cho các truy vấn LLM đám mây, thúc đẩy những kiến trúc hệ thống và mô hình triển khai hoàn toàn khác biệt. Hiệu năng vượt trội này cho phép hoạt động trong nhiều tháng hoặc nhiều năm trên các nguồn năng lượng hạn chế như pin đồng xu³⁵, như được minh họa bởi các bộ thiết bị trong hình 2.8. Những hệ thống này cung cấp thông tin chuyên sâu có thể hành động được (actionable insights) trong những môi trường xa xôi hoặc không được kết nối, nơi mà việc cấp nguồn điện, khả năng kết nối mạng, và quyền tiếp cận bảo trì là không khả thi.
Hình 2.8: Quy mô của Hệ thống TinyML: Các bảng mạch phát triển vi điều khiển cỡ nhỏ với những con chip xử lý hiển hiện và hệ thống cổng cắm (pin connectors) cho phép gắn kết (integration) cùng những cảm biến phục vụ quá trình suy luận ML luôn-bật bên trong những ngân sách eo hẹp về công suất cũng như bộ nhớ.
Quy mô của những ràng buộc này trở nên hữu hình khi chúng ta tận mắt chứng kiến phần cứng. Hình 2.8 trình bày các bo mạch phát triển vi điều khiển tiêu biểu, mỗi bảng được xây dựng xoay quanh hệ thống SRAM quy mô kilobyte (kilobyte-scale) cùng mức cung cấp điện năng quy mô milliwatt. Toàn bộ đường ống thực thi quy trình suy luận ML, từ cảm biến nhận đầu vào cho tới việc phân loại trả kết quả đầu ra, đều bắt buộc giới hạn trong khuôn khổ vật lý cùng những định mức điện năng này. Ở điểm cuối này, mục tiêu triển khai được xác định bởi cảm biến luôn-bật dưới ngân sách đo bằng kilobyte và milliwatt.
Định nghĩa 2.5: TinyML
TinyML là miền máy học (domain of machine learning) của Cảm biến Luôn-bật bị giới hạn bởi Bộ nhớ Quy mô Kilobyte và Năng lượng Quy mô Milliwatt.
1. Ý nghĩa: Nó đòi hỏi các mô hình đủ nhỏ để cư trú (reside) hoàn toàn trong SRAM Trên-Chip, tránh được chi phí năng lượng cao (gấp 100 lần) của việc truy cập DRAM nhằm cho phép suy luận liên tục trong ngân sách năng lượng milliwatt.
2. Sự khác biệt: Khác với ML Di động, sử dụng các bộ xử lý nhiều watt (multi-watt) và một hệ điều hành (OS) đầy đủ, TinyML chạy trên Các vi điều khiển (MCU) không hề có sự trừu tượng hóa của hệ điều hành.
3. Cạm bẫy phổ biến: Một quan niệm sai lầm thường thấy là cho rằng TinyML chỉ là "các mô hình nhỏ". Trên thực tế, nó là một Nguyên mẫu Bị Ràng buộc Bằng Năng lượng (Energy-Bound Paradigm): số liệu đo lường cốt lõi là Năng lượng Cho mỗi Lần Suy luận (tính bằng microjoule), chứ không đơn thuần chỉ là số lượng tham số (parameter count).
Mức tiêu thụ năng lượng đo bằng milliwatt của TinyML đại diện cho sự giảm thiểu sáu cấp số nhân so với việc suy luận đám mây, một khoảng cách mang theo những hệ quả (implications) sâu rộng đối với hệ thống thiết kế. Trong phương trình quy luật sắt 2.6, TinyML thuộc về dạng (regime) mà quy chuẩn khắt khe chiếm hữu ưu thế (dominant constraint) chẳng phải là 𝑂/(𝑅_peak ⋅ 𝜂_hw) hay 𝐷_vol/BW, mà nó nghiêng về ràng buộc giới hạn độ vừa vặn bộ nhớ (memory-fit) vốn không được mô tả tường tận trong dạng công thức kia: diện tích của mô hình (footprint) 𝑀_model và diện tích của chuỗi các kích hoạt buộc phải tương thích và nằm khép trong khối dung tích bộ nhớ trên-chip 𝐶_mem. Khi mà tất cả không gian ghi nhớ đều chỉ đo được qua những đơn vị kilobyte, các thông số mô hình phải gói trọn hoàn hảo phía trên chip, và một byte cho vận chuyển cấu trúc


================ PAGE 106 ================

68
2.8 TinyML: Cảm biến Phổ quát (Ubiquitous Sensing)
tiêu thụ mức năng lượng (energy) được đếm bằng picojoule. Tôn chỉ cho sự ưu tiên hoàn thiện dịch chuyển xa hẳn với việc làm thấp nhất độ trễ đi tới định dạng làm nhỏ phần năng lượng với mỗi một thực tính chạy—là tính hiệu năng hữu dụng (efficiency), không phải do vận tốc.
Góc nhìn Hệ thống (Systems Perspective) 2.3: Đọc các con số năng lượng-mỗi-lần-suy luận
Những con số năng lượng trong bảng 2.12 đại diện cho tổng mức năng lượng của toàn hệ thống (full-system energy), bao gồm cả những CPU trên máy chủ, khả năng bộ nhớ, hệ thống mạng lưới kết nối, và chi phí phần chung (overhead) thuộc về công đoạn làm mát, chứ không đơn thuần là mức tiêu hao nhiệt lượng biệt lập (isolated) trên bộ phận tính toán gia tốc. Một chiếc thẻ GPU A100 có thể một mình giải quyết bài toán suy luận của kiến trúc mô hình ResNet-50 ở khoảng mức nhỏ hơn 1 ms (~0.3 J), tuy nhiên một bộ cụm máy chủ hoàn chỉnh lại có thể tiêu thụ công suất ~1 kW một khi đã hòa chung (amortized) để chi phối hàng đợi chờ, tác vụ cấu hình hệ đệm trước, và nguồn điện nghỉ chờ khi tĩnh tại (idle power). Phần tính cột (query counts) xuất hiện đằng sau chót bảng giúp giải mã ý tưởng dưới hệ ngôn ngữ số của thông tin thực dụng đời thường: một hệ dung lượng pin ở chiếc điện thoại tay cấu thành độ chống đỡ tương xứng cấp hoạt động lên tới tận mức cường độ gấp 100,000,000 lần tính trên một bộ ứng dụng dò-từ-thức (wake-word detector) TinyML so với lượt yêu cầu lên hệ dữ liệu bộ LLM đám mây (cloud LLM).
Khảo qua về khoảng không xa của hệ hiệu quả (energy-efficiency) nơi TinyML giải minh điều vì sao cảm ứng không tắt mới trở thành khả năng làm ăn được trên riêng tầng mô hình TinyML này (TinyML tier). Điện thoại trên bàn tay con người phải kéo cày một loạt câu cầu hệ thống trên đám mây sẽ sớm cạn nguồn điện ở thời lượng quy tính bằng vài chục phút, trong lúc nguồn dự trữ cùng loại như vậy đủ để hậu thuẫn những đo lường dò tín hiệu địa phương ở quy mô các chu kỳ cả tháng trời.
Lỗ hổng năng lượng giữa những khung hình tư duy triển khai hệ không chỉ rơi vào số khoảng lớn nhỏ trong phạm trù đo mức (degree), thay vào đó chính là do các quy luật thuộc vấn đề hệ thống (scale), dàn rộng đến tất thảy tám phần lớn theo bậc lũy thừa được vạch ra trong sơ đồ 2.6. Bản đối số liệu 2.12 bám rễ những khoảng dài trên thông qua nhiều thông tin rõ ràng chi tiết, phiên dịch các định hình dạng quy luật năng lượng hao tổn trở về dưới hình thái độ đáp trả yêu cầu (inferences) của khả năng lưu sức máy ở chỉ có độc chiếc điện thoại đơn.
Bảng 2.12: Năng lượng cho mỗi lần suy luận qua các nguyên mẫu (paradigms): Mức tiêu thụ điện năng cho cả một hệ thống tiêu biểu ở mỗi thao tác thực hành suy luận, cũng như con số lượng tác vụ giải mã qua được (query counts) nhờ viên pin từ thiết bị, mô phỏng ra sự kiện dàn cảnh lên tới tám số hạng lũy thừa định mức rằng bộ cảm biến chạy vĩnh viễn (always-on sensing) bắt buộc giới hạn trong khung hình TinyML.
Nguyên mẫu
Ví dụ Khối lượng công việc
Năng lượng/Lần Suy luận
Thời lượng Pin (3.7 V, 3000 mAh)
Đám mây
Truy vấn GPT-4
~1 kJ
40 lượt truy vấn
Đám mây
ResNet-50 (máy chủ tăng tốc)
68.8 mJ
580,864 lượt truy vấn
Biên (Edge)
ResNet-50 (Jetson)
12.3 mJ
3,259,067 lượt truy vấn
Di động (Mobile)
MobileNet (NPU)
2.46 mJ
16,272,606 lượt truy vấn
TinyML
Nhận dạng Từ khóa
10 µJ
3996 triệu lượt truy vấn
TinyML ngự trị ở điểm tận cùng trong khoảng đường giới hạn (resource envelope): những dòng điện (power) hệ tính milliwatt (milliwatt power) cùng độ lưu đệm hệ kilobyte (kilobyte memory) (hình 2.9). Nhờ các vùng không gian (limits) hẹp ấy thiết lập lên những quy chế dò chạy luồng không đứt gãy vốn chẳng thể được trụ nổi (sustain) do ở những mô hình xây dựng khác, song buộc (force) kiến trúc sư phát triển cần mẫn rào gọn mức cô đọng rất khủng (extreme model compression) trước chặng xuất định hình phần mềm ra ngoài.
Ràng buộc Cốt lõi
Phản hồi Hệ thống
Ranh giới Thất bại
Các Khối lượng công việc Phù hợp
TinyML
Ngân sách Công suất Milliwatt
Phạm vi Bộ nhớ Kilobyte
Chu kỳ Làm việc Luôn-Bật (Always-On Duty Cycle)
Truy cập Mạng Thưa thớt (Sparse Network Access)
Gói gọn Mô hình và Các kích hoạt trên Chip
Sử dụng Số học Số nguyên (Integer) và Nhị phân
Ngủ (Sleep) Giữa các Lần Phát hiện
Tóm tắt Trước khi Truyền đi
Suy giảm Độ chính xác do Nén
Rủi ro Cập nhật Phần sụn (Firmware Update Risk)
Phân mảnh Chuỗi công cụ (Toolchain Fragmentation)
Không có Huấn luyện Hoàn chỉnh (Full Training) Cục bộ
Phát hiện Từ Đánh thức (Wake-Word)
Theo dõi Động vật hoang dã
Thiết bị đeo Y tế
Cảm biến Nhà máy
Hình 2.9: Bản đồ Ràng buộc TinyML: Công suất milliwatt và bộ nhớ kilobyte khiến cho cảm biến luôn-bật khả thi về mặt kinh tế, nhưng chính những giới hạn đó buộc mô hình, các kích hoạt, thời gian chạy, và con đường cập nhật phải vừa vặn với một phạm vi kỹ thuật (engineering envelope) nhỏ hơn rất nhiều.


================ PAGE 107 ================

69
36
Ràng buộc của Huấn luyện Trên-thiết-bị (On-Device Training Constraints): Huấn luyện hoàn chỉnh (Full training) trên thiết bị phải giữ lại các kết quả đầu ra của lớp trung gian (intermediate layer outputs) để các bản cập nhật trọng số sau này có thể tái sử dụng chúng, tiêu thụ một lượng bộ nhớ tỷ lệ thuận với độ sâu của mô hình. Trong quá trình suy luận, các giá trị tạm thời của mỗi lớp thường có thể bị hủy bỏ sau khi lớp tiếp theo sử dụng chúng; còn trong quá trình huấn luyện, nhiều giá trị trong số đó phải giữ nguyên khả dụng để bước cập nhật (update step) có thể quyết định các trọng số nên thay đổi như thế nào. Với chỉ từ 256 KB–2 MB RAM, các vi điều khiển không thể hỗ trợ đường ống này; các phương pháp thích ứng chuyên biệt như TinyTL chỉ tinh chỉnh (fine-tune) các lớp cuối cùng bằng cách sử dụng <50 KB bộ nhớ làm việc. Ràng buộc bộ nhớ này là lý do giải thích vì sao các thiết bị TinyML chủ yếu chỉ dành cho quá trình suy luận (inference-only), với các bản cập nhật mô hình được đẩy lên thông qua phần sụn (firmware) chứ không phải được học tại chỗ (in situ).
37
Dải thiết bị TinyML (TinyML Device Range): Dải thiết bị vật lý này phản ánh sự đánh đổi trực tiếp giữa ngữ cảnh triển khai và khả năng tính toán. Các hệ thống quy mô milimet (Millimeter-scale) ưu tiên công suất tối thiểu (~140 µW) cho các tác vụ chức năng đơn lẻ, thời lượng dài (single-function, long-duration tasks), trong khi các bảng mạch có kích thước bằng lòng bàn tay đánh đổi kích thước lớn hơn và công suất cao hơn để lấy khả năng xử lý nhiều luồng cảm biến phức tạp (multiple complex sensor streams). Sự lựa chọn thiết kế chung (co-design choice) này tạo ra sự chênh lệch lớn hơn >10,000 lần về công suất và ~100 lần về diện tích (area) trên toàn bộ phổ vận hành của các thiết bị TinyML.
38
Phân mảnh Hệ sinh thái TinyML (TinyML Ecosystem Fragmentation): Không giống như ML trên đám mây hay di động, nơi PyTorch hoặc TensorFlow Lite cung cấp một con đường tối ưu hóa thống nhất, TinyML trải dài trên hàng chục họ vi điều khiển không tương thích (incompatible microcontroller families) (chẳng hạn như ARM Cortex-M, RISC-V, Xtensa), mỗi họ đều có các tập lệnh (instruction sets), cách bố trí bộ nhớ (memory layouts), và chuỗi công cụ (toolchains) đặc thù của nhà cung cấp. Một mô hình được tối ưu hóa cho một thiết bị mục tiêu thường đòi hỏi phải điều chỉnh (retuning) và thẩm định lại (re-validation) cho một mục tiêu khác, làm nhân lên các chi phí kỹ thuật (engineering cost) cho quá trình triển khai trên đa thiết bị và tạo ra rào cản tính khả chuyển (portability barriers) vốn vắng bóng trong các mô hình có nguồn tài nguyên dồi dào hơn.
2.8.1 Ưu điểm và các đánh đổi trong hoạt động của TinyML
TinyML hoạt động ở những điều kiện phần cứng khắc nghiệt (hardware extremes). So với các hệ thống đám mây, các triển khai TinyML thường cung cấp bộ nhớ ít hơn khoảng từ 10⁶ đến 10⁹ lần, tùy thuộc vào ngân sách của vi điều khiển nằm ở mức vài megabyte hay kilobyte thấp, với ngân sách điện năng ở ngưỡng milliwatt. Những giới hạn nghiêm ngặt này cho phép thiết bị vận hành tự động trong nhiều tháng hoặc nhiều năm³⁶ nhưng đổi lại đòi hỏi các thuật toán chuyên biệt, việc nén mô hình (model compression), và quá trình đồng-thiết-kế (co-design) hệ thống cẩn thận. Các thiết bị trải dài từ bộ công cụ phát triển kích cỡ bằng bàn tay (palm-sized) tới cả các con chip kích thước milimet³⁷, qua đó cho phép khả năng cảm biến phổ quát tại những nơi mà kết nối mạng, nguồn điện, hay việc bảo trì mang chi phí quá đắt đỏ. Những bộ kit cho nhà phát triển (developer kits) phổ biến bao gồm Arduino Nano 33 BLE Sense (256 KB RAM, 1 MB bộ nhớ flash, 20–40 mW) cùng ESP32-CAM (520 KB RAM, 4 MB flash, 50–250 mW).
Sự giới hạn nguồn tài nguyên cực độ của TinyML một cách nghịch lý lại mang tới các lợi ích độc nhất (unique advantages). Bằng cách né tránh truyền tải qua hệ thống mạng hoàn toàn, thiết bị sử dụng kiến trúc TinyML tạo lập được ngưỡng trễ cho hệ khép kín (end-to-end latency) mức ngắn bậc nhất của bộ mô hình làm việc (deployment spectrum), đẩy tốc độ phản hồi nhanh chóng (rapid local responses) phục vụ hệ điều tra cảm biến và các vòng kiểm soát (control loops) mà xóa nhòa phụ thuộc thời gian trao đổi bên ngoài (communication overhead). Phương pháp tính tự cung tự cấp này cũng tác động ngược trở lại nền tảng của quy trình tài chính đầu tư từ dự án rộng: vì hệ phí tính bình quân rớt xuống dưới một vài đô la cho một cảm biến đơn (node), việc trang bị hệ đo kiểm vào tất cả phần mảng công nghiệp, nông hộ, hoặc cả toà cao ốc chuyển dạng kinh tế (economically viable) trên góc độ khả năng thay thế mà mô hình biên (edge) hay bộ dữ liệu điện toán không cách nào cân xứng. Sự tính chuẩn xác qua nguồn duy trì bổ trợ vào những đánh giá tiền chi, khiến cho tiến trình vận hành kéo liên tục hơn cả vài năm nhờ những bình pin nhỏ nhoi, có thể kể cả quá trình tự xoay trở thu nhặt năng lượng vĩnh viễn không tắt ngủ. Tính ẩn danh cá nhân (Privacy) tuôn trào liền như chuyện mặc định qua tính bản lề giới hạn không gian (locality), khi mà tín hiệu sơ khai chưa qua nhào nặn tuyệt nhiên chưa một lần đi khỏi máy phát, hất tung phần hiểm hoạ đánh cắp đường gửi (transmission risks) và cho phép việc qua cửa thông qua (compliance). Nhưng việc hệ thống định biên giải nghĩa trên thân (On-device processing) lại chưa mặc định cấp một thẻ bài miễn hoàn toàn an toàn từ chuẩn riêng tư (formal privacy guarantees) nếu chưa tính có các bộ cấu trúc quy chuẩn đi kèm bảo hộ.
Các khả năng kể trên (capabilities) đòi hỏi sự nhân nhượng lớn (substantial trade-offs). Rào cản phần mềm tính ra các định dạng chặn khe khắt (severe limits): những vi xử lý loại nhỏ thường sẽ mở cổng tính khoảng mức dung sai chứa đựng 10⁵ đến tầm 10⁶ byte của tính toán RAM, đẩy sức chạy ở các chuỗi kết nối và điểm nạp nhịp (intermediate activations) xuống khu giới hạn vỏn vẹn chục kilobyte cho chạm đến khoảng ít megabyte (low-megabytes) hoàn toàn tính vào áp lực vận hành thực sự tại thời điểm (workload). Bộ phức tạp kiến trúc phát triển đẩy đòi hỏi chuyên tu xuyên mảng trên toàn mảng làm gọn độ phủ khối kết nối mô hình học sâu, công đoạn rải bố trí bộ nhớ cấp độ hệ cơ tĩnh (hardware-level memory management), cùng cả cấu trúc đồ nghề nhúng (embedded toolchains) mà việc gỡ rầy các vấn đề cho từng kiến trúc điều khiển riêng (debugging across diverse microcontroller architectures).
Vượt lên cao của sự bức bối mặt kiến trúc, các vấn đề của hoạt động còn chất dày lên tính khó cho bài giải. Khối lượng và chất lượng hoạt động từ kết tinh mô hình bị tổn thất sau màn gói gọn dung sai nặng trĩu cùng làm hụt mức chuẩn (reduced precision), bó thắt tính hiệu chuẩn vào bài toán công cụ làm việc thực chiến ở đòi hỏi điểm chính xác (high accuracy) cũng độ dày kinh cường (robustness). Màn thử nghiệm có thể bộc lộ cứng ngắc: thiết bị chạy định tính vài mẫu kết tinh quy chuẩn cho sẵn không chuyển xoay, rồi màn làm thay đổi dữ liệu đè phải dùng qua luồng đường công đoạn (firmware workflows) thường sẽ rớt chậm chạp mà chứa đầy hiểm hoạ gấp bao lần (slower and riskier) quy trình trên đám mây mang lại (cloud rollouts). Tính xé lẻ và khó trộn hợp³⁸ ở khắp không gian hãng chế tạo hệ máy điều khiển và không gian khuôn mô ML cũng đưa cho sự tăng thêm tải nặng đè lên chi phí và vấn đề làm mềm hoá linh kiện di tản (portability challenges).
2.8.2 Giám sát môi trường và sức khỏe
Các ứng dụng TinyML thuộc về đây khi mức tiêu thụ điện năng cực thấp (ultra-low power), chi phí thấp trên mỗi điểm nút (per-node cost), và quá trình xử lý cục bộ làm cho một đợt triển khai trở nên khả thi trong khi không một mô hình nào khác có thể chống đỡ nổi (sustain). Nhận diện từ đánh thức (Wake-word detection) là ví dụ người tiêu dùng quen thuộc nhất: thiết bị lắng nghe liên tục với mức tiêu thụ năng lượng dưới milliwatt, xử lý âm thanh tại cục bộ, và chỉ kích hoạt các thành phần tiêu thụ năng lượng cao hơn khi một cụm từ thức tỉnh được phát hiện, qua đó giảm đáng kể lượng năng lượng tiêu thụ trung bình³⁹. Nông nghiệp chính xác (Precision agriculture) khai thác cùng áp lực cục bộ đó (locality pressure) từ một hướng khác: Dự án FarmBeats sử dụng các cảm biến, camera, thiết bị bay không người lái (drone), và quá trình xử lý qua cổng kết nối (gateway processing) cục bộ để hạn chế việc di chuyển dữ liệu thô ở những nơi mà khả năng kết nối của trang trại quá đắt đỏ (Vasisht et al. 2017). TinyML đẩy logic cục bộ đó đi xa hơn khi bản thân nút cảm biến (sensing node) phải hoạt động dưới những ngân sách đo bằng milliwatt.
Bảo tồn động vật hoang dã sử dụng TinyML cho việc giám sát môi trường từ xa, nơi các nhà nghiên cứu triển khai các cảm biến âm thanh chạy bằng năng lượng mặt trời tiêu thụ 100–500 mW, xử lý các luồng âm thanh liên tục (continuous audio streams) nhằm nhận dạng loài. Bằng cách thực hiện quá trình phân tích cục bộ, những hệ thống này giảm bớt các yêu cầu truyền dữ liệu qua vệ tinh từ 4.3 GB/ngày đối với âm thanh thô xuống còn 400 KB/ngày cho các bản tóm tắt nhận diện (detection summaries), một sự sụt giảm 10,750 lần, giúp các đợt triển khai quy mô lớn gồm 100–1,000 cảm biến trở nên khả thi về mặt kinh tế. Các thiết bị đeo y tế (Medical wearables) áp dụng cùng logic xử lý cục bộ đó (local-processing logic) vào lĩnh vực sức khỏe, nơi mà khả năng giám sát luôn-bật (always-on monitoring) và tính riêng tư trên-thiết-bị mang lại giá trị to lớn khi kết hợp cùng nhau: các máy theo dõi nhịp tim được FDA phê duyệt đạt được độ nhạy (sensitivity) 95–98 phần trăm trong khi xử lý 250–500 mẫu điện tâm đồ (ECG) mỗi giây với mức tiêu thụ năng lượng chưa tới 5 mW, cho phép theo dõi liên tục suốt cả tuần so với chỉ vài giờ của các giải pháp thay thế dựa trên điện thoại thông minh, và giảm thiểu chi phí chẩn đoán từ 2,000–5,000 USD cho các nghiên cứu tại phòng thí nghiệm truyền thống xuống dưới 100 USD khi thực hiện kiểm tra tại nhà.


================ PAGE 108 ================

70
2.9 Lựa chọn Nguyên mẫu (Paradigm Selection)
39
Phát hiện Từ-Đánh thức (Wake-Word) Luôn-bật: Mục tiêu công suất dưới milliwatt (sub-milliwatt) này được đáp ứng bởi một mô hình đơn giản, chuyên dụng không làm gì khác ngoài việc lắng nghe dấu hiệu âm thanh (acoustic signature) của cụm từ đánh thức. Mô hình này hoạt động như một cổng năng lượng quyết liệt (aggressive power gate), ngăn chặn việc kích hoạt không cần thiết của bộ xử lý ứng dụng chính vốn tiêu thụ điện năng lớn hơn từ 100–1,000 lần. Toàn bộ kiến trúc tiết kiệm năng lượng sẽ sụp đổ nếu thành phần luôn-bật này vượt quá ngân sách công suất khắt khe của nó ở mức xấp xỉ một milliwatt.
Bốn mô hình triển khai giờ đây trải dài toàn bộ từ các trung tâm dữ liệu megawatt cho đến các vi điều khiển milliwatt. Mỗi mô hình (paradigm) nổi lên như một giải pháp đáp trả các ràng buộc vật lý cụ thể, và mỗi cái đều tỏ ra xuất sắc bên trong giới hạn vận hành của nó. Câu hỏi về việc một kỹ sư nên lựa chọn giữa chúng như thế nào, và phải làm gì khi không một mô hình đơn lẻ nào thỏa mãn được mọi yêu cầu, là động lực thúc đẩy phần phân tích so sánh tiếp theo đây.
2.9 Lựa chọn Nguyên mẫu (Paradigm Selection)
Một kiến trúc sư (architect) khi lựa chọn nơi để chạy một tính năng ML hiếm khi chỉ tối ưu hóa ở một phương diện (dimension). Một quy tắc về quyền riêng tư có thể cấm quá trình xử lý trên đám mây, một ngân sách độ trễ có thể cấm việc suy luận từ xa, một khoảng trống bộ nhớ có thể vượt quá khả năng của thiết bị di động, và một mục tiêu chi phí có thể loại trừ phần cứng luôn-bật (always-on) ở vùng biên. Đám mây, vùng biên, thiết bị di động, và TinyML đóng vai trò là những giới hạn vận hành (operating envelopes) cho những xung đột đó, vì vậy việc lựa chọn giữa chúng đòi hỏi một khuôn khổ so sánh thống nhất và một quy trình ra quyết định có cấu trúc.
2.9.1 Phân tích so sánh các sự đánh đổi
Các quyết định triển khai yêu cầu phải xem xét các sự đánh đổi (trade-offs) giữa độ trễ và thông lượng (latency-vs-throughput) của các mô hình một cách trực diện (side by side) trên tất cả những phương diện quan trọng. Một kiến trúc sư hệ thống khi lựa chọn giữa triển khai ở biên và trên thiết bị di động phải đồng thời so sánh độ trễ, công suất, chi phí, quyền riêng tư, và độ phức tạp của quá trình phát triển. Bảng 2.13 cung cấp sự so sánh này trên mười bốn phương diện (dimensions), từ sức mạnh tính toán và độ trễ cho tới chi phí và tốc độ triển khai.
Bảng 2.13: So sánh Mười bốn Phương diện Mô hình (Fourteen-Dimension Paradigm Comparison): Một sự so sánh trực tiếp, toàn diện trên mười bốn khía cạnh (dimensions) có tính chất quyết định đối với các lựa chọn triển khai. Cần lưu ý mối quan hệ nghịch đảo giữa khả năng sức mạnh tính toán và quyền riêng tư: ML Đám mây cung cấp sức mạnh tính toán mạnh nhất nhưng các đảm bảo về quyền riêng tư lại yếu hơn, trong khi TinyML mang lại quyền riêng tư cao nhất nhưng lại có sức mạnh tính toán kém nhất. Bảng này đóng vai trò như tài liệu tham khảo chính dành cho các kỹ sư kiến trúc hệ thống khi đánh giá các tùy chọn triển khai.
Khía cạnh
ML Đám mây
ML Vùng biên
ML Di động
TinyML
Vị trí Xử lý
Các máy chủ đám mây tập trung (Trung tâm dữ liệu)
Các thiết bị biên cục bộ (cổng kết nối, máy chủ)
Điện thoại thông minh và máy tính bảng
Vi điều khiển siêu tiết kiệm điện và hệ thống nhúng
Độ trễ
100 ms–1000 ms+
10–100 ms
5–50 ms
1–10 ms
Sức mạnh Tính toán
Rất Cao (Nhiều GPU/TPU)
Cao (GPU Biên)
Trung bình (NPU/GPU Di động)
Rất Thấp (MCU/bộ vi xử lý cực nhỏ)
Dung lượng Lưu trữ
Không giới hạn (petabyte+)
Lớn (terabyte)
Trung bình (gigabyte)
Rất Hạn chế (kilobyte–megabyte)
Mức Tiêu thụ Năng lượng
Rất Cao (Khoảng kW–MW)
Cao (Hàng trăm watt)
Trung bình (1–10 W)
Rất Thấp (Khoảng mW)
Khả năng Mở rộng Quy mô
Xuất sắc (gần như không giới hạn)
Tốt (bị giới hạn bởi phần cứng biên)
Trung bình (mở rộng theo từng thiết bị)
Hạn chế (phần cứng cố định)
Quyền Riêng tư Dữ liệu
Cơ bản-Trung bình (Dữ liệu rời khỏi thiết bị)
Cao (Dữ liệu ở lại trong mạng nội bộ)
Cao (Dữ liệu ở lại trên điện thoại)
Rất Cao (Dữ liệu thô có thể duy trì cục bộ)
Yêu cầu Kết nối mạng
Cần băng thông cao liên tục
Ngắt quãng (Intermittent)
Tùy chọn
Không
Khả năng Ngoại tuyến
Không
Tốt
Xuất sắc
Hoàn toàn
Xử lý Thời gian thực
Phụ thuộc vào mạng
Tốt
Rất Tốt
Xuất sắc
Chi phí
Cao ($1000+/tháng)
Trung bình ($100–$1000)
Trung bình ($200–$1000+/thiết bị)
Rất Thấp ($1–$10)
Yêu cầu Phần cứng
Cơ sở hạ tầng đám mây
Máy chủ/cổng kết nối biên
Điện thoại thông minh hiện đại
MCU/hệ thống nhúng
Độ Phức tạp Phát triển
Cao (cần chuyên môn về đám mây)
Trung bình-Cao (biên + kết nối mạng)
Trung bình (SDK di động)
Cao (chuyên môn về hệ thống nhúng)
Tốc độ Triển khai
Nhanh
Trung bình
Nhanh
Chậm


================ PAGE 109 ================

71
Mối quan hệ nghịch đảo giữa quyền riêng tư và sức mạnh tính toán này không phải là ngẫu nhiên—nó phản ánh sự đánh đổi vốn có (inherent trade-off) giữa tính cục bộ của dữ liệu (data locality) và quy mô tính toán. Dữ liệu giữ lại ở cục bộ thì không thể được xử lý với quy mô trung tâm dữ liệu, và dữ liệu di chuyển lên đám mây thì không thể duy trì sự riêng tư hoàn toàn. Việc ánh xạ các nguyên mẫu-mô hình (archetype-paradigm mapping) được thiết lập trong phần 2.3 kết nối những đặc tính này với các yêu cầu khối lượng công việc cụ thể, với mỗi một nguyên mẫu sẽ hướng tới (gravitating toward) các mô hình giải quyết được ràng buộc cốt lõi của nó.
Hình 2.10 biểu diễn (plots) những sự đánh đổi này dưới dạng biểu đồ radar, nơi mỗi mô hình tạo thành một đa giác và các diện tích lớn hơn chỉ ra hiệu suất mạnh mẽ hơn trên trục đó. Điểm số (scores) của các trục là các đánh giá thứ tự (ordinal judgments) trên thang điểm 0–10, những xếp hạng phù hợp với các ranh giới (envelopes) đã đo lường trong chương này chứ không phải bản thân các giá trị thực tế. Biểu đồ a) đối chiếu sức mạnh tính toán và khả năng mở rộng, nơi ML đám mây thể hiện xuất sắc, với độ trễ và hiệu suất năng lượng, nơi TinyML chiếm ưu thế tuyệt đối. Biểu đồ b) đối chiếu tính tự chủ (autonomy) trong vận hành: tính độc lập với kết nối mạng, quyền riêng tư, khả năng xử lý thời gian thực, và hoạt động ngoại tuyến, những khía cạnh mà quá trình triển khai cục bộ (local deployment) thể hiện lợi thế mạnh mẽ nhất.
Sức mạnh Tính toán
Độ trễ
Khả năng Mở rộng
Hiệu suất Năng lượng
1
3
5
7
9
ML Đám mây
ML Vùng biên
ML Di động
TinyML
a)
Sự Độc lập với Mạng
Quyền Riêng tư Dữ liệu
Xử lý Thời gian thực
Khả năng Ngoại tuyến
1
3
5
7
9
b)
Hình 2.10: Biểu đồ Radar So sánh Các Mô hình (Paradigm Comparison Radar Plots): Hai biểu đồ radar so sánh hiệu suất và các đặc tính vận hành (operational characteristics) giữa các mô hình đám mây, vùng biên, di động, và TinyML sử dụng thang điểm thứ tự (ordinal) 0–10. Biểu đồ bên trái đối chiếu sức mạnh tính toán, độ trễ, khả năng mở rộng, và hiệu suất năng lượng; biểu đồ bên phải đối chiếu tính độc lập với mạng lưới, quyền riêng tư, khả năng thời gian thực, và hoạt động ngoại tuyến. Trong cả hai biểu đồ, đa giác lớn hơn thể hiện hiệu suất mạnh hơn, với ML đám mây đạt đỉnh ở khả năng tính toán cùng khả năng mở rộng, còn TinyML vươn lên chiếm thế thượng phong về hiệu suất năng lượng, quyền riêng tư, và khả năng ngoại tuyến.
Những biểu đồ radar đã làm cho các quyết định triển khai trở nên rõ ràng: không có mô hình (paradigm) nào chiếm ưu thế trên toàn bộ các trục (axes). Mức độ phức tạp trong việc phát triển có quan hệ tỷ lệ nghịch (varies inversely) với năng lực phần cứng: Đám mây và TinyML đều yêu cầu chuyên môn sâu (cloud infrastructure and embedded systems chuyên ngành đám mây và hệ thống nhúng, tương ứng), trong lúc nhóm hệ thống Mobile (Di động) với Edge (Biên) sử dụng những SDK (bộ phát triển ứng dụng) cùng loạt công cụ dễ tiếp cận hơn. Cơ cấu giá cả (cost structures) đi theo dạng khuôn mẫu tương tự (similar pattern): Đám mây (Cloud) mắc phải các chi phí hoạt động liên tục ($1,000s+/tháng), Vùng biên (Edge) đòi hỏi phần quỹ rót sẵn lớn cho đoạn ban đầu ($100s-$1,000s), hệ Di động vận dụng thiết bị cá nhân (user-provided devices) của người dùng để kéo phẳng giá cơ sở hạ tầng ($0-$10s), và TinyML làm rẻ mạt tiền nguyên vật liệu ($1-$10s) trong khi cần đến đầu tư rất mạnh cho bước kiến thiết, tạo lập (development investment).
Một sai sót (pitfall) đầy tính chí mạng cho quy trình quyết định cách triển khai đó là chỉ rập khuôn lựa mô hình (paradigms) đo theo mức độ đúng đắn (model accuracy) bỏ qua những rào cản xét về mảng thiết kế (system-level constraints). Một mô hình đưa lên mạng tính dữ liệu đám mây sở hữu 99 phần trăm chuẩn chỉnh có khi biến thành không thể sử dụng vào chức năng phanh khẩn nguy tự động (autonomous emergency braking) nếu quãng thời gian kết nối mạng trễ (network latency) vượt ngoài độ chớp mắt yêu cầu (reaction time requirements); một mô hình vùng biên đạt mức trúng đích hoàn hảo tới đâu nếu bòn rút (drains) nguồn pin thiết bị tay (mobile) vài tích tắc thì vẫn bị gọi là sản phẩm vứt đi dẫu độ chính xác xuất chúng (superior accuracy). Triển khai đạt kỳ vọng đỏi hỏi tiến hành dò kiểm gắt gao với các yêu cầu trễ nhịp (latency requirements), định phí điện, duy trì tín hiệu liên tục, khung luật pháp quyền tư cá nhân (data privacy regulations), và mức tổng phí tổn (total cost of ownership) vận hành đồng nhất. Những bức tường (constraints) đó nên đặt làm hệ trụ móng định hình (established) phía trước đoạn nhen nhóm xây mô hình (model development) để ngừa những thay đổi phương án ngốn kinh phí diễn ra khúc đuôi (late) trong dự án.
2.9.2 Khuôn khổ ra quyết định (Decision framework)
Tiến hành lựa ra phương thức (deployment paradigm) phù hợp đòi hỏi cần khung quy chiếu làm khuôn đúc định đoạt bắt nhịp theo định mức rào cản ứng dụng (application constraints) thay vì thói thiên lệch tập thể (organizational biases) hay một xu hướng về kỹ thuật công nghệ. Các cánh cổng (gates) được lần lượt dựng lên bằng cấp độ cản phá mà mỗi yếu điểm tạo ra để gạt bỏ một dự án (invalidate an architecture): sự riêng tư (privacy) có thể sẽ tước đoạt thẳng quyền gửi truyền tính toán bên ngoài, quy luật trễ nải (latency) hoàn toàn tước quyền xử lý về đặc tính vật lý hiện tại, tham số đòi năng lượng xử lý có thể loại phần thiết bị gốc khỏi danh mục ứng viên, và


================ PAGE 110 ================
72
2.9 Lựa chọn Mô hình
suy ra giá thành cho phép kết luận ứng viên (feasible option) còn sót sống đủ làm một thiết chế cơ cấu làm ăn. Phỏng rập quyết định đưa theo hình khối 2.11, nó tiến hành việc lọc sạch toàn phương hướng qua cơ sở tháp phân hóa nhu cầu tiên quyết trên.
Lớp: Quyền riêng tư (Privacy)
Lớp: Hiệu suất (Performance)
Lớp: Nhu cầu Tính toán (Compute Needs)
Lớp: Chi phí (Cost)
Lớp: Tùy chọn Triển khai (Deployment Options)
Bắt đầu
Quyền riêng tư có mang tính sống còn? (Is privacy critical?)
Cho phép Xử lý Đám mây (Cloud Processing Allowed)
Ưu tiên Xử lý Cục bộ (Local Processing Preferred)
Có yêu cầu độ trễ thấp (<10 ms) không?
Chấp nhận Độ trễ (Latency Tolerant)
Tiny hoặc Edge ML
Mô hình có đòi hỏi lượng tính toán lớn không?
Tính toán Nặng (Heavy Compute)
Xử lý Nhẹ nhàng (Lightweight Processing)
Có những ràng buộc khắt khe về chi phí không?
Ngân sách Linh hoạt (Flexible Budget)
Tùy chọn Chi phí Thấp (Low-Cost Options)
Edge ML
Tiny ML
Cloud ML
Mobile ML
Không (No)
Có (Yes)
Không
Có
Có
Không
Không
Có
Hình 2.11: Logic Quyết định Triển khai: Sơ đồ luồng (flowchart) này hướng dẫn việc lựa chọn một mô hình triển khai máy học phù hợp bằng cách đánh giá có hệ thống (systematically evaluating) các yêu cầu về quyền riêng tư và các ràng buộc xử lý, cuối cùng cân bằng giữa hiệu suất, chi phí, và bảo mật dữ liệu. Việc điều hướng (Navigating) qua cây quyết định giúp các chuyên viên (practitioners) xác định xem điện toán đám mây, vùng biên, thiết bị di động hay máy học cỡ nhỏ (tiny) phù hợp nhất với một ứng dụng cụ thể.
Khuôn khổ này đánh giá bốn lớp quyết định quan trọng một cách tuần tự (sequentially). Các ràng buộc về quyền riêng tư đóng vai trò là bộ lọc đầu tiên, xác định xem dữ liệu có thể được truyền ra bên ngoài hay không. Các ứng dụng xử lý dữ liệu nhạy cảm theo các quy định nghiêm ngặt của GDPR, HIPAA, hoặc giới hạn quyền sở hữu (proprietary restrictions) bắt buộc (mandate) phải xử lý cục bộ, ngay lập tức loại bỏ các hình thức triển khai chỉ sử dụng đám mây (cloud-only deployments). Yêu cầu về độ trễ thiết lập ràng buộc thứ hai thông qua ngân sách thời gian phản hồi (response time budgets): các ứng dụng đòi hỏi thời gian phản hồi dưới 10 ms không thể sử dụng quá trình xử lý đám mây, vì bản thân sự chậm trễ mạng lưới do yếu tố vật lý tạo ra (physics-imposed network delays) đã vượt quá ngưỡng này. Yêu cầu tính toán hình thành nên lớp đánh giá thứ ba, xem xét (assessing) xem các ứng dụng cần một hệ cơ sở hạ tầng đạt năng lực sức mạnh tối đa (high-performance infrastructure) mà chỉ đám mây hoặc vùng biên mới thỏa mãn, hay liệu các phần mềm có thể kham được sức làm bên dưới những định mức khắc nghiệt dành cho tài nguyên ở mảng di động hoặc siêu nhỏ (tiny devices). Điểm cuối tính toán về kinh phí (Cost considerations) khép lại bộ khuôn mẫu khi dàn trải đối trọng giữa phí đầu tư ban đầu (capital expenditure), quỹ chạy định kỳ (operational expenses), cùng tiêu hao năng suất trong dòng đời được trù định của hệ thống cài đặt.
Bài toán ví dụ về tình huống thắng gấp xe bảo vệ tính mạng (safety-critical) phơi bày quá trình xếp thứ tự một cách dễ hình dung hơn, bởi độ nghẽn mạch sẽ triệt tiêu cửa cài trên mây (cloud deployment) ngay tắp lự trước khi ta màng đo đếm khả năng sức chạy hay bài toán giá cả tiền chi.


================ PAGE 111 ================

73
Ví dụ 2.1: Phanh khẩn cấp cho xe tự hành (Autonomous vehicle emergency braking)
Kịch bản: Phát hiện người đi bộ dựa trên thị giác máy tính cho hệ thống phanh khẩn cấp.
Phân tích:
1. Quyền riêng tư: Dữ liệu camera của xe không được truyền cho bên thứ ba → Không có ràng buộc quyền riêng tư mạnh mẽ. Có thể sử dụng đám mây.
2. Độ trễ: Phanh khẩn cấp yêu cầu tổng thời gian phản hồi <100 ms. Ở tốc độ 100 km/h, một chiếc xe di chuyển 2.8 m trong 100 ms.
• Độ trễ mạng tới đám mây: 50–150 ms (biến đổi) → Không đạt yêu cầu
• Xử lý biên (Edge processing): 10–30 ms → Đạt
• Quyết định: Đám mây bị loại trừ bởi yếu tố vật lý.
3. Tính toán: Việc phát hiện người đi bộ đòi hỏi khoảng ~10 GFLOP ở 30 FPS = 300 GFLOP/s duy trì (sustained).
• Năng lực tính toán cấp TinyML: Không kham nổi khối lượng công việc này.
• Khả năng tăng tốc nơ-ron (neural acceleration) cấp điện thoại: Có thể thực hiện sau khi lượng tử hóa số nguyên (integer quantization), nhưng các giới hạn nhiệt (thermal limits) duy trì vẫn là một vấn đề.
• Bộ tăng tốc biên (Edge accelerator) trên ô tô: Dư sức vượt qua.
• Quyết định: Biên (Edge) hoặc Di động cao cấp (high-end Mobile).
4. Chi phí: Ứng dụng an toàn-tới-cùng, sản xuất khối lượng lớn (high-volume production) (hàng triệu xe).
• GPU Biên: $500-1000 mỗi xe, được khấu hao (amortized) trong hơn 10 năm tuổi thọ của xe = $50–100/năm
• Quyết định: GPU Biên hoàn toàn hợp lý đối với một ứng dụng an toàn-tới-cùng.
Kết quả: Edge ML với một bộ tăng tốc ô tô (automotive accelerator) cục bộ. Các tài nguyên đám mây hỗ trợ việc huấn luyện, cập nhật mô hình, và phân tích toàn đội xe (fleet-wide analytics), chứ không phải để phục vụ suy luận thời gian thực (real-time inference).
Góc nhìn hệ thống: Độ trễ đã loại bỏ tùy chọn đám mây trước cả khi khả năng tính toán hay chi phí được cân nhắc; trình tự quyền riêng tư-độ trễ-khả năng tính toán một cách trọn vẹn đã thu hẹp bốn mô hình triển khai xuống chỉ còn lại vùng biên.
Khuôn khổ quyết định (decision framework) vừa rồi nhận diện được các lựa chọn khả thi (feasible options) về mặt kỹ thuật, tuy nhiên sự khả thi không có gì để bảo đảm thành công. Mảng quá trình xây dựng hệ thống chạy thực (production deployment) còn ăn theo nhóm kỹ năng của hội tổ chức tạo lập để đi tới quyết định rằng một bước đi tuy chắc tay rạch ròi kỹ thuật thì có thể được cài đặt hoàn thiện (implemented) và nuôi nấng bảo trì hiệu quả hay chăng (maintained effectively). Thực thi mĩ mãn (Successful deployment) bám lấy các xét nét bao quanh chứ không hẳn nằm kẹt trong riêng phần cứng tính kỹ sư (pure engineering constraints). Nền kỹ năng sâu của đội (Team expertise) phải ăn khớp cùng đòi hỏi đặc trưng từ cách dựng: quy chuẩn điện toán đám mây cho ML cần đầu kỹ năng thấu hiểu kiến trúc (distributed systems knowledge), vùng Biên đòi mảng mổ xẻ rành rẽ đường hệ thống làm việc với thiết bị (device management capabilities), bộ ML Mobile ngỏ cần tay có kinh nghiệm cặn kẽ trên khâu thiết kế tối ưu hệ từng mẫu đặc trưng (platform-specific optimization skills), trong lúc khuôn định hình siêu bé TinyML (TinyML) réo gọi vốn kĩ thuật mảng cấu kiện nhúng (embedded systems expertise). Khung tổ chức thiếu hụt các khả năng kể ra tất nhiên nhận lại việc kéo nhão thời khóa biểu (extended development timelines) tới mức ném đi toàn bộ những ích lợi đáng tự hào về góc độ kiến trúc đã giành lấy (undermine even the strongest technical advantages).
Khả năng kiểm soát điều phối hệ thống (monitoring and maintenance capabilities) theo dòng khuôn cũ thiết lập sự sống còn (viability) khi xét ở hệ quy trình nhân rộng (at scale): hệ vùng Biên (edge deployments) buộc phải thao túng mạng lưới kết nối của nhiều con chip riêng biệt (distributed device orchestration), trong khi mẫu nhỏ TinyML lại gọi ra cả sự đòi hỏi tinh gọn khâu chuyên biệt hóa hệ mạch in (firmware management) – cái sự khuyết vắng rất thường thấy trong vô số mảng hội. Kết nối tài chính tính phí (Cost structures) đưa vô hẳn khía cạnh đánh giá thêm vào, khi mức mẫu hoa văn chạy dài mặt chi tiền (temporal pattern of expenses) có chiều thay phiên chuyển hoán rất rõ xuyên thấu (dramatically) cùng những mô hình định triển khai. Hệ cơ điện mây kéo mảng chạy phí quy trình quay trở (recurring operational costs) tiện lợi (favorable) hơn trên những lượng nhu cầu chẳng lường chước (unpredictable workloads); Edge vòi tiền to đập sẵn ban sơ (upfront investment) gỡ gạc bằng dòng bảo trì hậu thuẫn đi theo ở giá dễ thở hơn; Di động (Mobile) nương tay cho người kiến thiết (users-provided devices) khi đánh tan tiền mớ (minimize infrastructure expenses); và mảng vi hạt (TinyML) tước sạch giá nguyên phụ liệu kĩ thuật (hardware costs) bù lại phải cắn chặt nguồn vốn đầu não tư duy khai phá (significant development investment).
Các phương diện thực tế (organizational realities) của một tổ chức mở ra sự lo ngại (broader concern) không nhỏ: hướng đi ML không mặc nhiên cho điểm đánh trúng 10 trên 10 (not always the right choice). Khởi sự nào vắt ML vào (deployment carries) cũng gánh hệ chi thêm (operational overhead)—vòi hút dữ liệu, kiểm ứng, bảo dưỡng phần rèn thuật—mà vô vàn cách thức sơ khởi thông minh không phải đau đầu trúng, thành ra cục nợ nặng túi đó phải đem đắp trả sòng phẳng (paid back) qua giá trị đánh giá được cao hơn rất rõ của phần thành phẩm.


================ PAGE 112 ================
74
2.10 Kiến trúc Kết hợp (Hybrid Architectures)
Góc nhìn Hệ thống 2.4: Thuế phức tạp (The complexity tax)
Trước khi cam kết triển khai bất kỳ hệ thống ML nào, hãy cân nhắc (weigh) gánh nặng vận hành so với các giải pháp thay thế đơn giản hơn.
Hãy xem xét một bài toán phân loại (classification problem) có thể giải quyết bằng một phương pháp suy nghiệm (heuristic - các quy tắc if-then) hoặc một đường ống học sâu (deep learning pipeline). Phương pháp suy nghiệm có thể là năm mươi dòng mã với chi phí tính toán gần như bằng không, mất khoảng một giờ mỗi tháng để cập nhật các quy tắc, và không có hiện tượng trôi dạt mô hình (model drift). Hệ thống ML cũng có thể chỉ có năm mươi dòng mã mô hình, nhưng nó lại mang theo khoảng 2,000 dòng mã cơ sở hạ tầng (infrastructure) cho các đường ống dữ liệu, hệ thống giám sát, và trình điều khiển (drivers) GPU, cộng thêm khoảng 40 giờ mỗi tháng để gỡ lỗi trôi dạt (debugging drift) và quản lý cơ sở hạ tầng.
Một hệ thống ML giúp cải thiện độ chính xác từ 90 phần trăm lên 95 phần trăm vẫn có thể là một lựa chọn kỹ thuật tồi nếu nó làm tăng độ phức tạp lên 40 lần. Kỹ thuật hệ thống ML là nghệ thuật tối thiểu hóa khoản thuế này thông qua các kiến trúc vững chắc (robust architecture). Nếu chi phí vận hành để duy trì chất lượng mô hình theo thời gian là quá đắt đỏ (unaffordable), phương pháp suy nghiệm đơn giản hơn có thể là một lựa chọn hệ thống ưu việt (superior systems choice).
Mỗi quyết định triển khai đều bị ràng buộc (constrained) đồng thời bởi yếu tố vật lý, chi phí cơ sở hạ tầng, và gánh nặng liên tục của việc giữ cho hệ thống luôn chính xác. Khi thuế phức tạp (complexity tax) vượt quá mức tăng độ chính xác, một phương pháp suy nghiệm đơn giản hơn sẽ là sự lựa chọn hệ thống ưu việt.
Điểm kiểm tra 2.2: Thiết kế hệ thống
Sự đánh đổi cốt lõi thường là giữa độ chính xác (accuracy) và độ phức tạp (complexity).
Cổng Quyết định (Decision Gates)
□ Đường cơ sở (The baseline): Bạn đã đo lường độ chính xác của một phương pháp suy nghiệm đơn giản (regex, hồi quy logistic) trước khi bắt tay vào huấn luyện một Mạng Sâu (Deep Network) chưa?
□ Chi phí cơ sở hạ tầng (The infrastructure cost): Liệu mức tăng độ chính xác 2 phần trăm từ một kiến trúc transformer có xứng đáng (worth) với mức tăng chi phí suy luận gấp 10 lần cùng gánh nặng bảo trì so với một mô hình nhỏ hơn hay không?
Việc triển khai thành công cần phải cân bằng giữa tối ưu hóa kỹ thuật (technical optimization) và năng lực tổ chức (organizational capability). Lựa chọn mô hình không chỉ giới hạn ở các yêu cầu kỹ thuật mà còn bao trùm (encompass) các kỹ năng của đội ngũ, khả năng vận hành, và ràng buộc kinh tế, tất cả đều bị chi phối bởi các quy luật vật lý về mở rộng quy mô (physical scaling laws) mà chúng ta đã xem xét. Các khía cạnh vận hành (Operational aspects) được trình bày chi tiết trong Chương 14 và các phương pháp chấm điểm (benchmarking approaches) nằm ở Chương 12. Tuy nhiên, trên thực tế, khuôn khổ ra quyết định (decision framework) hiếm khi chỉ ra một thiết kế duy nhất chiến thắng. Hầu hết các hệ thống sản xuất (production systems) kết hợp nhiều mô hình, chẳng hạn như huấn luyện trên đám mây, phục vụ tại vùng biên, và tiền xử lý trên thiết bị di động, nhằm thỏa mãn các ràng buộc mà không một mục tiêu triển khai đơn lẻ nào có thể đáp ứng được.
2.10 Kiến trúc Kết hợp (Hybrid Architectures)
Khuôn khổ ra quyết định (hình 2.11) giúp lựa chọn mô hình đơn lẻ (single paradigm) tốt nhất cho một ứng dụng nhất định. Tuy nhiên, trong thực tế, các hệ thống sản xuất hiếm khi chỉ sử dụng một mô hình. Trợ lý giọng nói kết hợp tính năng phát hiện từ đánh thức của TinyML với khả năng nhận diện giọng nói trên di động (mobile speech recognition) và sự thấu hiểu ngôn ngữ tự nhiên trên đám mây (cloud natural language understanding). Xe tự hành ghép cặp quá trình suy luận vùng biên cho tính năng nhận thức thời gian thực (real-time perception) với hoạt động huấn luyện trên đám mây phục vụ cho các bản cập nhật mô hình. Những kiến trúc kết hợp (hybrid architectures) này khai thác thế mạnh của nhiều mô hình trong khi giảm thiểu (mitigating) điểm yếu của từng cái. Ba chiến lược tích hợp (integration strategies) sẽ định hình (formalize) cách các sự kết hợp đó hoạt động trong thực tế như thế nào.
Định nghĩa 2.6: ML Kết hợp (Hybrid ML)
Học máy Kết hợp là chiến lược triển khai phân tách (splits) một đường ống ML thành các tầng (tiers) đám mây và biên, chỉ định (assigning) các giai đoạn quan trọng về độ trễ (latency-critical stages) cho phần cứng cục bộ và các giai đoạn đòi hỏi nhiều tính toán (compute-intensive stages) cho các trung tâm dữ liệu từ xa.


================ PAGE 113 ================

75
40
Bất đối xứng Chi phí Huấn luyện-Phục vụ (Train-Serve Cost Asymmetry): Quá trình huấn luyện là một cuộc tìm kiếm tham số mô hình đòi hỏi nhiều tính toán và chỉ thực hiện một lần, trong khi suy luận (inference) là một bước truyền xuôi (forward pass) đơn lẻ, rẻ tiền sử dụng các tham số đó. Điều này tạo ra cơ sở lý luận kinh tế (economic rationale) cho việc phân tách, vì chi phí cố định khổng lồ cho việc huấn luyện sẽ được khấu hao (amortized) qua hàng tỷ truy vấn suy luận chi phí thấp tiếp theo. Khoảng cách chi phí sinh ra giữa một đợt chạy huấn luyện trị giá hàng triệu đô la với một lần suy luận giá chưa tới một xu (sub-cent) có thể vượt quá ngưỡng gấp 1,000,000 lần.
1. Ý nghĩa: Kiến trúc kết hợp khai thác cấu trúc cộng hợp (additive structure) của quy luật sắt: tầng vùng biên tối thiểu hóa 𝐿_lat cho các khâu tiền xử lý và suy luận nhạy cảm về thời gian, trong khi tầng đám mây cung cấp 𝑅_peak cần thiết cho việc huấn luyện, huấn luyện lại, và suy luận theo lô khối lượng lớn. Việc phân tách bị chi phối bởi bất biến tính cục bộ dữ liệu (data locality invariant): các giai đoạn mà ở đó 𝐷_vol/BW_network vượt qua lợi ích của việc tính toán từ xa sẽ được chạy cục bộ; các giai đoạn nơi 𝑅_peak của đám mây chiếm ưu thế sẽ chạy từ xa.
2. Sự khác biệt: Khác với triển khai chỉ-trên-đám-mây (vốn chấp nhận hình phạt khoảng cách cho tất cả các giai đoạn) hoặc triển khai chỉ-tại-biên (chấp nhận 𝑅_peak giới hạn cho tất cả các giai đoạn), ML kết hợp phân bổ động (dynamically assigns) mỗi giai đoạn của đường ống vào tầng nào mà ở đó thành phần quy luật sắt chi phối (binding iron law term) của nó được cực tiểu hóa.
3. Cạm bẫy phổ biến: Một quan niệm sai lầm phổ biến là cho rằng ML kết hợp chỉ đơn giản là "chạy hai mô hình". Trong thực tế, hai tầng (tiers) này phải chia sẻ trạng thái đồng bộ (synchronized state)—các định nghĩa đặc trưng (feature definitions), phiên bản mô hình, và logic tiền xử lý—sao cho các đường dẫn vùng biên và đám mây tạo ra kết quả nhất quán. Nếu không có sự đồng bộ hóa này, sự sai lệch giữa huấn luyện-phục vụ (training-serving skew) sẽ xuất hiện tại ranh giới giữa các tầng.
2.10.1 Các mẫu tích hợp (Integration patterns)
Ba mẫu ML kết hợp (hybrid ML) thiết yếu có sự khác biệt bởi việc ranh giới nào tạo ra ràng buộc: phân tách huấn luyện-phục vụ (train-serve split), xử lý phân cấp (hierarchical processing), hoặc triển khai lũy tiến (progressive deployment). Việc lựa chọn chúng là một quyết định mang tính quy luật sắt: mỗi giai đoạn nên chạy ở nơi mà thành phần chi phối của nó (cho dù là tính toán huấn luyện, độ trễ cục bộ, hay kích thước mô hình) dễ dàng thỏa mãn nhất với chi phí rẻ nhất.
Phân tách Huấn luyện-Phục vụ (Train-Serve Split) đặt quá trình huấn luyện trên đám mây trong khi quá trình suy luận (inference) diễn ra trên vùng biên, thiết bị di động, hoặc thiết bị tiny. Mẫu thiết kế (pattern) này khai thác quy mô đám mây cho việc huấn luyện đồng thời hưởng lợi từ độ trễ suy luận cục bộ cùng với quyền riêng tư. Chi phí huấn luyện có thể lên tới hàng triệu đô la cho các mô hình lớn, trong khi chi phí suy luận chỉ tính bằng xu (cents) cho mỗi truy vấn khi được triển khai hiệu quả.⁴⁰
Trong Xử lý Phân cấp (Hierarchical Processing), dữ liệu và trí tuệ lưu chuyển giữa các tầng (tiers) điện toán. Các cảm biến TinyML thực hiện phát hiện bất thường (anomaly detection) cơ bản, các thiết bị biên tổng hợp và phân tích dữ liệu từ nhiều cảm biến, còn hệ thống đám mây xử lý các phân tích phức tạp và các bản cập nhật mô hình. Mỗi tầng xử lý các tác vụ phù hợp với năng lực của mình.
Mẫu thứ ba, Triển khai Lũy tiến (Progressive Deployment), nén các mô hình một cách có hệ thống để triển khai trên các tầng. Một mô hình đám mây khổng lồ dần trở thành các phiên bản được tối ưu hóa cho máy chủ biên, thiết bị di động, và cảm biến nhỏ (tiny sensors). Trợ lý giọng nói chính là một ví dụ điển hình cho mẫu này: tính năng phát hiện từ đánh thức sử dụng các mô hình nhỏ, luôn-bật (always-on), thường chỉ tốn vài chục kilobyte cho mạng lưới nơ-ron TinyML theo tiêu chuẩn (benchmark) và sử dụng mức năng lượng chưa tới một milliwatt đến một milliwatt trên phần cứng chuyên dụng tiêu thụ năng lượng thấp, trong khi tính năng hiểu ngôn ngữ tự nhiên (natural language understanding) phức tạp lại cần những mô hình lớn hơn rất nhiều nằm trên cơ sở hạ tầng đám mây.
Khi đã có sẵn ba mẫu tích hợp, việc chọn lựa trở thành một bài toán ghép khớp ràng buộc (constraint-matching problem): hãy chọn mẫu thiết kế có hồ sơ đánh đổi (trade-off profile) ăn khớp với nút thắt cổ chai chi phối (dominant bottleneck) của hệ thống. Bảng 2.14 sẽ tóm lược sự đánh đổi, những điều kiện ưu tiên (favoring) từng mẫu, cũng như các điều kiện bác bỏ (argue against) nó.
Bảng 2.14: Hướng dẫn Lựa chọn Mẫu (Pattern) Kết hợp: Các sự đánh đổi, điều kiện ưu tiên và điều kiện loại trừ cho từng mẫu trong số ba mẫu tích hợp kết hợp (hybrid integration patterns). Quá trình lựa chọn diễn ra bằng cách khớp (matches) cấu hình đánh đổi của mẫu này với điểm nghẽn cổ chai lớn nhất chi phối toàn bộ hệ thống.
Mẫu Thiết kế (Pattern)
Sự Đánh đổi
Lựa chọn khi
Tránh khi
Phân tách Huấn luyện-Phục vụ
Chi phí huấn luyện so với (vs.) độ trễ suy luận
Quá trình huấn luyện yêu cầu quy mô mà suy luận không cần tới; quyền riêng tư quan trọng đối với suy luận nhưng không quan trọng đối với huấn luyện
Mô hình cần liên tục học hỏi từ dữ liệu triển khai
Xử lý Phân cấp
Quyền tự chủ cục bộ so với quá trình tối ưu hóa tổng thể
Lượng dữ liệu vượt quá khả năng truyền dẫn (transmission capacity); cần các quyết định tại nhiều khoảng thời gian (timescales)
Toàn bộ quy trình xử lý có thể diễn ra ở một tầng; mạng lưới luôn ổn định, tin cậy và đạt tốc độ cao
Triển khai Lũy tiến
Chất lượng mô hình so với phạm vi triển khai
Cần cùng một mô hình ở nhiều cấp độ (levels) khả năng khác nhau; yêu cầu quá trình suy giảm nhẹ nhàng, dần dần (graceful degradation)
Mô hình không có cách nào được nén lại đáng kể; chỉ có một mục tiêu triển khai duy nhất
Các trợ lý giọng nói (Voice assistants) kết hợp (combine) cả Phân tách Huấn luyện-Phục vụ, Triển khai Lũy tiến, và Xử lý Phân cấp; xe tự hành lại kết hợp Xử lý Phân cấp với Triển khai Lũy tiến nhằm mục đích khởi chạy các


================ PAGE 114 ================

76
2.10 Kiến trúc Kết hợp
mô hình đã được tối ưu hóa ở mỗi tầng. Các phương pháp tiếp cận huấn luyện phân tán bảo vệ quyền riêng tư (Privacy-preserving distributed training) sẽ mở rộng thêm danh mục này khi mà dữ liệu cần phải nằm lại gần các thiết bị tạo ra nó.
2.10.2 Tích hợp hệ thống sản xuất (Production system integration)
Các hệ thống ML kết hợp trong sản xuất tích hợp nhiều mẫu thiết kế vào các giải pháp gắn kết (cohesive solutions). Hình 2.12 làm rõ các tương tác này thông qua các loại kết nối cụ thể trong một đường ống dữ liệu kết hợp. Tính năng cốt lõi là luồng hai chiều (bidirectional flow): Các luồng "Triển khai" (Deploy paths) chỉ ra cách các mô hình chảy xuống từ quá trình huấn luyện đám mây đến nhiều thiết bị khác nhau, trong khi "Dữ liệu" (Data) và "Kết quả" (Results) lại di chuyển từ cảm biến lên trên qua các giai đoạn xử lý cho đến công đoạn phân tích đám mây (cloud analytics). Các kết nối "Đồng bộ hóa" (Sync) minh họa quá trình điều phối thiết bị xuyên suốt các tầng. Kiến trúc hai chiều này, với mô hình đi xuống và dữ liệu đi lên, là đặc điểm làm nên sự khác biệt (defining characteristic) của các hệ thống sản xuất kết hợp (production hybrid systems).
Huấn luyện
Suy luận
Suy luận
Suy luận
Xử lý
Xử lý
Phân tích
Cảm biến
TinyML
Cloud ML (ML Đám mây)
Dữ liệu
Triển khai
Kết quả
Kết quả
Hỗ trợ (Assist)
Đồng bộ (Sync)
Kết quả
Dữ liệu
Kết quả
Edge ML (ML Vùng biên)
Mobile ML (ML Di động)
Hình 2.12: Các Tương tác trong Hệ thống Kết hợp (Hybrid System Interactions): Dữ liệu chảy ngược lên (upward) từ các thiết bị cảm biến thông qua những tầng (layers) xử lý phân lớp tới nhánh phân tích (analytics) trên không gian dữ liệu đám mây (cloud), còn phần mô hình đã hoàn thành khâu huấn luyện lại đi rải xuống khu vực biên, thiết bị trong tay người dùng, cùng các địa điểm truy suất trên TinyML. Hình hài đa điểm chia mảng (distributed architecture) tạo bởi hệ thống tập hợp năm mối dây nối (kể cả triển khai - deploy, dữ liệu - data, thành phẩm nhận lại - results, trợ sức - assist, và đồng bộ trơn tru - sync), mà qua đó mỗi nguyên mẫu đem tặng một bộ tính năng độc quyền chưa từng có.
Các hệ thống sản xuất (Production systems) biểu diễn những khuôn mẫu hợp chung (integration patterns) dưới định hình rạch ròi qua hành động áp đặt ranh giới các mảng (tier boundary) nơi mỗi nút tắt tạo áp lực. Quá trình phát giác phần hư hỏng lỗi kĩ thuật trên hàng công nghiệp (Industrial defect detection) chính là ví dụ bóc tách rất chuẩn của dạng Phân tách Huấn luyện-Truy vấn (Train-Serve Split): cơ sở mây chịu trọng trách đưa bài huấn luyện trên các nhóm kết cấu học nhìn hình (vision models) với mảng đai lượng gom từ đủ mặt cơ sở, để rồi rải đi cấu trúc tối ưu sang máy chạy điện toán biên quán xuyến mặt xưởng, hệ chạy máy tính bảng ở kho khâu thanh tra (quality inspectors), cùng chuỗi thu nhận hình gắn chết trên đai lắp. Công tác kiểm chuẩn cây cấy công nghiệp đem lại biểu mẫu minh chứng việc Quản lý Hệ Phân lớp (Hierarchical Processing): các thiết bị cắm đo đất chạy giám định bất bình thường khu mảng (local anomaly detection) theo chuẩn bộ vi hình TinyML, sau đó bộ vi xử lý biên ôm nạp thu lại dữ liệu báo cáo đi theo ở mỗi cụm chục loại đo kiểm tạo hình đường đi dạng đặc thù của mảng làm ăn điền canh, đẩy lại trọng trách công việc về khối liệu số toàn trạng cùng phác họa cấu trúc vụ gặt năm cho bộ đồ thị mây cao. Các máy đeo ghi chép thể dục chính là hình dạng mẫu cho mô hình Triển khai Phân lớp (Progressive Deployment) theo mẫu cổng chia (gateway patterns): hệ vòng đeo giám sát chạy ngầm sức vận động sử dụng liên tục quy chế chuyên dụng (optimized algorithms) trên vi xử lý có mốc tốn điện năng <1 mW, truyền mớ sơ lược gọn ghẽ này tới các cỗ máy thông minh kết hợp hệ lượng đong chung mọi nơi (multiple sources), kế tiếp trả kết xuất thời đoạn về hệ máy mây hòng đúc nên bảng theo dõi tình hình thể lực theo lộ trình sống.
2.10.3 Tại sao các phương pháp tiếp cận kết hợp (hybrid) mang lại hiệu quả
Kiến trúc kết hợp đem tới thành công vì mảng phân kì điểm khác biệt lại quy vào sự định khối kho nguyên (resource budgets), không dính đòn nơi phần gốc sâu nguyên lí hệ thống làm đòn. Tôn chỉ dồn hướng hội tụ (convergence principles) phác rõ bên hình 2.13: khâu tạo lắp nối thông đi theo khoảng từ mây tới siêu nhỏ gặp nhau (meet) nơi lõi gốc các khó khăn nền móng kiểm định đường ống truyền nhận liệu, phân dòng áp lực tạo biên, cùng định tính các khối cấu trúc chạy chuẩn tin (reliable architectures). Cái gốc móng tạo nề vững trãi (shared foundations) truyền tải (raise) lại lên chính hàng tá suy tính mổ xẻ ngang hàng ở vạn hướng qua mọi dạng nguyên mẫu (paradigm), cốt ở chuyện tối ưu khả năng sinh năng lượng, hệ đặc thù của khâu chạy định hình, và dòng học sâu có lòng tín cậy.
Sự tề tựu này diễn giải tính nguyên lí khi luân phiên tính chất chuyển giao giữa đủ kích thước của chuỗi cản trở ngầm cùng chôn dấu (shared bottleneck). Tổ chức học xây trên hệ mây (cloud-trained models) triển chạy nốt qua tới miền mép (edge) là do thành phần bộ xương tạo lập số nặng (learned weights) cùng dạng đồ hoạ thực thi (operator graph) có quyền làm vật xoay dùng đi lại, song đổi phần thiết bị tới sẽ làm biến hình số ghi, tính cực sắc bén (precision), nhịp trễ, cũng với nguồn điện dung cho mảng đai khối. Các loại định tính nén (representations) không sắc bén quá (lower-precision) đắp rèn riêng do biên độ giúp chi trả nhỏ nhẹ lại khoản bòn vốn để nạp trả cấu trúc trên nền đám mây (cloud serving); Chương 10 đắp quy tắc quy đổi trên bằng định dạng lấy tính lượng tử hóa (quantization). Chiến đồ tháo bỏ khối việc để rải


================ PAGE 115 ================

2. Hệ thống ML
77
Các Bản Triển khai Hệ thống ML
Nguyên tắc Hệ thống Cốt lõi
Các Cân nhắc Hệ thống
Cloud ML
Cloud ML
Huấn luyện ở Quy mô Lớn
Edge ML
Edge ML
Suy luận Trên-thiết-bị
AI
Mobile ML
Các Thiết bị Cá nhân
Các Ứng dụng Người dùng
Tiny ML
Các Thiết bị Bị Hạn chế
Tài nguyên
Đường ống Dữ liệu
Thu thập Xử lý
Triển khai
Kiến trúc Hệ thống
Mô hình Phần cứng
Phần mềm
Quản lý Tài nguyên
Tính toán Bộ nhớ
Năng lượng Mạng
Tối ưu hóa & Hiệu suất
Mô hình Phần cứng
Năng lượng
Các Khía cạnh Vận hành
Triển khai Giám sát
Cập nhật
AI
AI Đáng tin cậy
Bảo mật Quyền riêng tư
Độ tin cậy
Hình 2.13: Sự Hội tụ của các Hệ thống ML (Convergence of ML Systems): Cấu trúc ba lớp thể hiện cách mà các mô hình triển khai đa dạng hội tụ lại với nhau. Lớp trên cùng liệt kê bốn nguyên mẫu (Đám mây, Vùng biên, Di động, TinyML); lớp giữa xác định các nền tảng dùng chung (các đường ống dữ liệu, quản lý tài nguyên, mô hình, phần cứng, và việc triển khai); và lớp dưới cùng trình bày ba sự cân nhắc hệ thống (system considerations) (tối ưu hóa và hiệu suất, các khía cạnh vận hành, và AI đáng tin cậy) vốn được áp dụng cho tất cả các nguyên mẫu (paradigms).
trên nhiều thiết bị cũng tương tự thông báo cho các đợt triển khai vùng biên trong việc phân vùng một mô hình (partition one model) trên nhiều bộ xử lý; Chương 8 sẽ chính thức hóa họ phương pháp này dưới tên gọi tính song song mô hình (model parallelism).
Các kiến thức tối ưu hóa (optimization insights) di động thông báo cho sự hiệu quả của đám mây bởi vì các giới hạn về băng thông bộ nhớ luôn xuất hiện ở mọi quy mô. Các phương pháp làm giảm lưu lượng bộ nhớ trên điện thoại cũng có thể làm giảm chi phí suy luận đám mây khi áp dụng vào việc phục vụ theo lô (batch serving). Những đổi mới trong TinyML định hướng những tiến bộ xuyên suốt các mô hình bởi vì các giới hạn khắc nghiệt bắt buộc phải có những đột phá thực sự mới lạ (genuinely novel) về mặt thuật toán: việc thể hiện (representations) mô hình một cách nhỏ gọn gọn phát triển cho các vi điều khiển (microcontrollers) sau này cũng có thể thông báo lại (inform) cho các hệ thống quy mô lớn hơn với cùng một áp lực bộ nhớ (memory pressure) tương tự.
Định dạng phân lớp chia đều này lại nối qua Chương 4 ở hệ ống tải lượng dữ liệu (data pipelines), theo về Chương 10 cho khâu làm thắt tối ưu (optimization), rồi qua Chương 14 để luận mặt chạy hoạt động. Toàn cảnh thẩy thảy cũng y chang hệt đối với bộ Pod TPU (TPU Pod) đến cả ESP32 nhỏ lẻ. Cho dù vậy, hệ móng nề làm khung chịu tải (shared principles) lại đồng thời mở hướng nhược điểm chôn giấu (shared vulnerabilities) phải đỡ đạn theo mảng chung: loại gian khó đường đi vấp (operational challenges) như nhau (rời hình dạng trôi data - data drift, mục cấu tạo - model decay, quy định xét rà - monitoring) hiện nguyên hình lên mâm ở đủ mảng hạ tầng lại mời gọi sức lo toan đặt mắt bám tâm trước tiên khi ta vươn tính lấy kho lượng lời huấn thị sót (remaining lessons) nằm bên cuối chương luận.
Điểm kiểm tra 2.3: Các mẫu (patterns) ML Kết hợp
Kiến trúc kết hợp phát huy hiệu quả khi bạn phân bổ khối lượng công việc trên các tầng (tiers)—chứ không phải khi bạn sao chép (copy) cùng một đường ống duy nhất đến mọi nơi.
Các Mẫu Tích hợp (Integration Patterns)
□ Phân tách huấn luyện-phục vụ (Train-serve split): Bạn có thể giải thích tại sao quá trình huấn luyện trên đám mây và phục vụ tại biên/thiết bị di động thường mang lại lợi ích tối ưu về mặt kinh tế, ngay cả khi mô hình được chạy cục bộ không?


================ PAGE 116 ================

79
Một giai đoạn mô hình nhanh hơn không giúp tăng tốc độ tuyến tính (linearly speed up) của một đường ống (pipeline) máy ảnh.
41
Định luật Amdahl (Amdahl’s Law): Được Amdahl (1967) chính thức hóa cho khả năng mở rộng (scaling) của đa bộ xử lý (multiprocessor), nguyên tắc này áp dụng trực tiếp cho các đường ống triển khai ML, nơi mà mô hình chỉ là một giai đoạn trong số rất nhiều giai đoạn. Trong đường ống máy ảnh được minh họa ở trên, quá trình suy luận ML chiếm 60 ms trong tổng số 200 ms; ngay cả khi tăng tốc độ mô hình lên 100 lần thì sự cải thiện tổng thể (end-to-end) cũng chỉ đạt khoảng 1.4–2 lần bởi vì phần còn lại của đường ống không hề thay đổi. Các nhóm thực hiện việc chấm điểm (benchmark) độ trễ mô hình một cách độc lập thường đánh giá quá cao (overestimate) những lợi ích khi triển khai.
thách thức những trực giác (intuitions) từ kỹ thuật phần mềm truyền thống. Những sự nguỵ biện (fallacies) và cạm bẫy (pitfalls) này nắm bắt các sai lầm kiến trúc (architectural mistakes) làm lãng phí tài nguyên phát triển, bỏ lỡ mục tiêu hiệu suất, hoặc triển khai các hệ thống hoàn toàn không phù hợp (critically mismatched) với những ràng buộc vận hành của chúng.
Nguỵ biện: Một mô hình triển khai duy nhất (One deployment paradigm) có thể giải quyết được tất cả các vấn đề về ML.
Các ràng buộc vật lý tạo ra những ranh giới cứng (hard boundaries) mà không một mô hình đơn lẻ nào có thể trải dài qua hết. Thảo luận về bức tường bộ nhớ trong phần 2.4 cho thấy băng thông, dung lượng bộ nhớ, và độ trễ có khả năng mở rộng (scale) khác biệt so với khả năng tính toán thô, từ đó tạo ra những điểm nghẽn cổ chai (bottlenecks) mang tính khác biệt về chất (qualitatively different) ở các mô hình triển khai khác nhau. Bảng 2.13 định lượng điều này: ML đám mây đạt độ trễ 100–1000 ms trong khi TinyML mang lại mức 1–10 ms, sự chênh lệch gấp 100 lần này bắt nguồn từ các giới hạn của tốc độ ánh sáng, chứ không phải chất lượng triển khai (implementation quality). Một hệ thống robot thời gian thực (real-time robotics system) yêu cầu phản hồi dưới 10 ms không thể sử dụng quá trình suy luận đám mây bất kể khả năng tối ưu hóa, và một mô hình ngôn ngữ tỷ-tham-số (billion-parameter) không thể nằm vừa trên một vi điều khiển với 256 KB RAM bất kể kích thước mô hình được thu giảm (reduction) tới đâu. Kiến trúc tối ưu nhất thường kết hợp nhiều mô hình (paradigms) với nhau, chẳng hạn như quá trình huấn luyện đám mây đi kèm quá trình suy luận ở vùng biên, hoặc tiền xử lý trên thiết bị di động (mobile preprocessing) cùng với quá trình phân tích trên đám mây.
Một quan niệm sai lầm có liên quan là cho rằng việc di chuyển quá trình tính toán lại gần người dùng hơn thì luôn luôn làm giảm độ trễ, phớt lờ chi phí xử lý phụ (processing overhead) bị sinh ra do phần cứng biên yếu hơn—một sự đánh đổi được khám phá trong các phép thử suy luận (inference benchmarks) (phần 12.8).
Cạm bẫy: Chỉ dựa vào quá trình tối ưu hóa mô hình để vượt qua các giới hạn về năng lượng và nhiệt trên thiết bị di động.
Các kỹ thuật nén (Compression techniques) không thể mở rộng vô hạn nhằm chống lại các định luật vật lý. Hãy xem xét một chiếc điện thoại thông minh với viên pin 15 Wh. Một khối lượng công việc suy luận nhẹ ngốn 1 W chạy được trong 15 Wh / 1 W = 15 h, nhưng một khối lượng công việc nặng tiêu tốn 5 W, phổ biến đối với các mô hình lớn trên thiết bị, sẽ làm cạn kiệt cùng viên pin đó chỉ trong 15 Wh / 5 W = 3 h.
Khối lượng công việc 5 W đó còn kích hoạt sự điều tiết nhiệt (thermal throttling) làm giảm hiệu suất một cách đáng kể. Như phần 2.7.1 đã thiết lập, quá trình suy luận di động được duy trì không thể vượt quá ngưỡng xấp xỉ 3 W nếu không có khả năng làm mát chủ động (active cooling). Việc lượng tử hóa (Quantization) giúp giảm công suất đi khoảng 4 lần, nhưng sự thu giảm độ chính xác một cách mạnh mẽ (aggressive precision reduction) thường dẫn đến tổn thất tính chuẩn xác (accuracy loss). Các ứng dụng yêu cầu quá trình suy luận liên tục vượt quá phạm vi nhiệt độ di động sẽ vẫn không thể thực hiện được về mặt vật lý bất kể các cải tiến mang tính thuật toán.
Nguỵ biện: TinyML đại diện cho phiên bản thu nhỏ của ML di động (scaled-down mobile ML).
Sự khác biệt là về mặt định tính (qualitative), chứ không đơn thuần chỉ là định lượng. Như phần 2.8.1 đã thiết lập, các vi điều khiển TinyML cung cấp bộ nhớ từ 256 KB đến 1 MB so với các thiết bị di động là từ 4–12 GB, mức chênh lệch 10,000 lần đòi hỏi những thuật toán hoàn toàn khác biệt. ML di động sử dụng phép toán độ-chính-xác-giảm (reduced-precision arithmetic) với tổn thất độ chính xác cực nhỏ; TinyML yêu cầu khả năng giảm độ chính xác cực độ (extreme precision reduction) hy sinh từ 10–15 phần trăm tính chính xác để đổi lấy sự suy giảm bộ nhớ gấp 32 lần. Thiết bị di động chạy các mô hình với hàng triệu tham số; mô hình TinyML chứa 10,000–100,000 tham số, đòi hỏi các lựa chọn kiến trúc riêng biệt (distinct architectural choices) như các phép tính trọng lượng-nhẹ chuyên dụng (specialized lightweight operations) thiết kế nhằm tối thiểu hóa số lượng phép nhân-tích lũy (multiply-accumulate counts). Ngân sách công suất cho thấy các sự đứt gãy tương tự: suy luận di động tiêu thụ 1–5 W, trong khi TinyML nhắm tới mục tiêu 1–10 mW phục vụ cho hoạt động thu thập năng lượng không cần pin (battery-free energy harvesting). Những khoảng cách nghìn lần này biến TinyML thành một lớp bài toán (problem class) hoàn toàn khác, không phải là phiên bản nhỏ hơn của ML di động. Những nhóm áp dụng trực tiếp các kỹ thuật tối ưu hóa thiết bị di động vào các dự án TinyML sẽ phát hiện ra rằng việc lượng tử hóa từ FP32 xuống INT8 là chưa đủ khi mà các mô hình phải vừa vặn trong 64 KB, buộc phải có sự tái thiết kế kiến trúc hoàn chỉnh.
Cạm bẫy: Tối thiểu hóa nguồn tài nguyên tính toán cũng đồng nghĩa tối thiểu hóa tổng chi phí.
Nhiều nhóm chuyên tối ưu hóa mức tiêu thụ tài nguyên trên mỗi thiết bị (per-unit) trong khi lờ đi các chi phí vận hành chung (operational overhead) cũng như tốc độ phát triển (development velocity). Như khuôn khổ ra quyết định ở phần 2.9.2 đã nhấn mạnh, lựa chọn mô hình triển khai đòi hỏi việc đánh giá tổng chi phí sở hữu (total cost of ownership), không phải chỉ chi phí máy tính đơn thuần. Khâu chạy dịch vụ phân tích dữ liệu mạng tốn kém ($2,000/tháng tiền xử lý máy) nhìn đắt hơn giá hao mòn đầu tư máy biên cục bộ tại chỗ ($500/tháng), song cài ráp mạng biên nảy thêm chi phí quản lý vận mạng ($3,000/tháng), giá sửa chữa tu sửa linh kiện vật lý ($500/tháng), và phí chuyên viên bảo kê độ tin cậy ($2,000/tháng), gom góp thành $6,000/tháng—chênh 3 lần. Nhịp sống công việc đẩy vút hố ngăn cách: máy hệ mạng (cloud deployments) lao mình cập bờ đưa vô chạy thực tế tầm hai tháng đối lại sáu tháng đối với hạ tầng cơ sở biên (edge infrastructure) tạo riêng tương ứng khoảng bốn tháng doanh thu không cánh bay mất (delayed revenue). Điểm cắt phí tối đa cho ra đáp số (optimal cost solution) muốn giải cần mổ xẻ rạch ròi tổng chi phí sở hữu ôm trọn toàn bộ thời gian lên hình sản phẩm, chằng chịt tính vận hành (operational complexity), và giá đánh đổi cơ hội (opportunity costs), chẳng mảy may chỉ dừng lại cực tiểu hoá số tiền vận điện toán.
Nguỵ biện: Tối ưu hóa mô hình tương đương với tỷ lệ tăng tốc tuyến tính về mặt hệ thống (linear to system speedup).
Định luật Amdahl (Amdahl’s Law)⁴¹ vạch trần hàng biên chặn thẳng (hard limits) mà cơ chế thắt cổ chai đem ra chạy ứng dụng thực chiến được, ở nơi mục D.2.3.1 bóc tách mô hình giới hạn cực cường độ sức chạy (strong-scaling form) và trình bày dẫn chứng (works a speedup example) quy chiếu bằng tám máy chạy xử lí song hành: Điểm_nhanh_tổng_cuộc =
1
(1−𝑝)+ 𝑝
𝑠trong đó 𝑝đại diện mảng công việc khả dụng khả năng được tăng hiệu suất lên (improved) và 𝑠là
tỷ lệ nhanh hơn của phần đó (speedup of that fraction). Thử búng thao tác chụp nơi máy ảnh chiếc smartphone thông thường coi sao. Hình nhận vào trượt mình xuyên 100 ms thời gian lọc luồng kĩ thuật thông tin ban đầu (độ mở máy, cân màu), qua 60 ms luồng ML phân tính màn


================ PAGE 118 ================

80
2.13 Tóm tắt (Summary)
phân loại (classification), rồi chốt hậu kỳ 40 ms định màu (ánh định, quy nén HDR)—toàn thời gian ngót 200 ms. Ưu biến quá trình mô hình ML phân nhánh đánh lướt 10× vút qua tốc độ (còn 6 ms thay thế 60 ms cũ) tước mẻ tổng nhịp tính (total time) tụt đi hẵng từ 200 ms sang 146
ms—tổng kết được độ 1.37× nhanh vượt, chẳng đời nào là 10×. Kể cả trừ tuyệt mô hình thông minh đó đi luôn (𝑠= ∞) đem ra sức chạy tốc độ 1.43×,
vì khoảng 70 phần trăm quãng ống quy trình đằng sau ngó lơ chẳng dính dấp. Hiệu năng tính mĩ mãn vòi đòi đo mảng (profiling) cả chu trình toàn khối mà gỡ từng cọc nghẽn cho đồng quy nhất quán (systematically), vì hiệu năng hệ chung lệ thuộc rập tại chóp nghẽn nải nhịp (slowest unoptimized stage).
Cạm bẫy: Cứ cho là đút thêm dữ kiện huấn luyện (training data) vô chừng nào chắc chắn tâng bốc điểm năng lực của cấu kiện khi chạy vận ngoài thực (deployed model performance) bấy nhiêu.
Ba vách chặn ngăn lại sức đem giá trị từ bộ tâng scale (scaling benefits) với dữ liệu, y chang như khối hình mẫu hệ thống tại bộ phần 2.3 phác ra (illustrate). Điều đầu, vỏ sức (model size) giật lại ranh định tính nạp có thể thâu nạp (learned): khối lượng thiết kế lọc dạng từ (keyword spotting model) cầm trong tay 250K thành tố vớt điểm độ 95 phần trăm chạy trơn với 50K dạng nguồn thông tin (samples) mà trượt dốc thành 96.5 phần trăm (1.5 % nhỉnh dẫu 20× nạp lượng data đè vô) khi ôm vào thân độ 1M nguồn nạp, cộng đội tiền dung nạp (storage), cùng sức khoán (labeling cost). Thiết kế ấy nói thẳng (simply) là không đủ tay phác lại mạng đường khối nạp siêu lắt léo đa tạp hơn. Điều thứ hai, chuẩn mực lượng dữ liệu (data quality) uy phong hất cẳng quy mô độ nhiều (quantity): 1M mẫu phân tinh giản tốt nhất (curated samples) nện cái đè đầu được mảng 100M nạp rối tạp moi tìm mảng (web-scraped samples), với nguyên do phần gán thông sai (mislabeled examples) cùng dòng mảng sai tính (misleading patterns) đâm ngược gậy hủy hao tính hiệu dụng song hành độ bung bự mảng lượng. Điều số ba, mặt trải dữ kiện mảng nạp phân chia (deployment distribution) định đoạn sống chết nặng hơn quy mô tập (training scale): nguyên mẫu ráp xây nạp một tỉ vạn ảnh lướt từ web có chiều vận hành kém hơn nạp đánh (medical imaging) ở mảng cấu trúc máy y tế nhiều so đo với cái nạp riêng chuyên biệt độ 100K mẫu ngách. Nhóm hội chúi chọc nhồi mảng nguồn to khủng bố trốn bẵng đi bước xét năng lực ôm đòn (model capacity) hao phí tháng trời mồ hôi cho điểm tính nhích tí teo vứt ra bã (negligible accuracy gains).
Nguỵ biện: Cứ một cục khối hình nén chuẩn (model binary) rải thầu ngon ơ cho toàn vạn ngách chạy thực (every edge hardware target).
Những khối độ nhóm nhào tạc thiết chế đặc hữu ráp sẵn đem ném rải mọi bãi đáp đích y xì đúc, nhìn phần tung vãi triển khai giống y khâu gói bọc thay vì điểm cắt hở cho điểm tính toán hiệu chỉnh. Ở ngoài đời, hệ quy tắc theo riêng rẽ hệ thiết bị vật lí nhỉnh (yield) độ tốt lên 3–5× chênh lệch mà một cục nhị phân thường thường chẳng kham được. Mã tính nguyên INT8 (INT8 model) nạp trơn ở trên bo mạch NPU chuyên phục vụ đong khối nơ-ron hốt tới điểm định xử 3–4× cho từng watt nếu đọ ngang cái mã đó mà bắt xài định nổi FP32 ở nền máy chung định vị CPU (general-purpose CPU), chính vì con đường dẫn xử mảng quy mô INT8 cài ngầm trên NPU tước đoạt lượng tốn dư ở luồng đánh điểm động nổi (floating-point arithmetic). Đồng điệu, cơ cấu nén phép (operator fusion) (gập nhập mảng tính cạnh kề để đường đệm khối nháp không bận bung trở (written back) về ô cắm) cùng điểm chuẩn bố cục vùng (memory layout tuning) nện vô bộ máy đặc thù ở khối chờ nhỏ (cache hierarchy) đủ gọt một nửa cái ngưng nghẽn truyền nhận khi suy đoán (halve inference latency) dẫu cho cái mảng mạng độ tĩnh của thiết kế nọ (model's weights) đứng im. Як (Như) màn chia tách đánh ranh cho hệ dàn (deployment paradigm analysis) ở vùng 2.1 móc rễ (establishes), từng một điểm nạp chia mảng đều gắn theo tính kìm cứng phần vật chất riêng rẽ; khối nhị phân nhào trọn gói ưu vào máy tính lõi Arm Cortex-A78 chạy chểnh mảng bộ gia tính (matrix acceleration units) thuộc con cắm NPU Arm Ethos-U. Đám chạy ngó lơ độ sửa nắn đặc cho điểm cuối hoặc ăn tốn điện hao sài vào bộ cầm tay, hoặc chẳng thể đạt chuẩn giao kết đo chờ trễ mạng (latency service level agreements - SLAs) của vùng máy cắm biên, tạo áp buộc bồi hồi xử lôi ngược đắt đỏ (postdeployment remediation).
Cạm bẫy: Cung cấp (Shipping) các tạo tác (artifacts) chung chung mà không lập hồ sơ từng mục tiêu (per-target profiling).
Một bản cài ráp đơn vẫn còn công năng như đường phân ngưỡng (portability baseline), tuy vậy nó chẳng đáng chọn như bộ giấy mực kết hợp chung kết (final performance contract). Từng một mục tiêu đưa ra chạy màng dò vạch kiểm trọn ở khu cắm thật sự vào luồng đường hệ (runtime, delegate, memory hierarchy, thermal envelope) chuẩn bị cho đoạn đời chạy làm việc nạp thật ngoài nhà máy. Thiếu rà (per-target check), khối người chế sẽ đứng chết trân không tường được tệp mẫu (generic binary) đó qua môn (acceptable), cạn vốn vô duyên (merely inefficient), hay ngay nền gốc đã tự chống đá nhau với hệ máy (fundamentally mismatched to the device).
2.13 Tóm tắt (Summary)
Khung biên cương vật lý lý giải được sao ở tại sao riêng cấu trúc một dạng máy bắt định quy đổi toàn rạch ròi mặt nền kĩ nghệ bên máy tính di động so bì mảng ở nơi trạm phân trung bộ dữ liệu (data center). Ba trụ kiềm khóa bất dịch (immutable constraints) (tốc năng quang truyền, vách chắn dòng diện áp, vách hố hệ nhớ) khắc xé khối vạn dạng dàn hệ sinh hình về hẳn bốn hướng định rõ trượt nhau ước tám chín lớp nhân độ (nine orders of magnitude) tại mặt lượng điện năng với không bộ lưu tính. Không cái khối hệ nào chăn dắt đủ tất cõi mảng chạy (production systems); định tính ráp đan (hybrid architectures) cái nào băm phân khối tại vùng Mây (Cloud), Biên (Edge), Điện tay (Mobile), TinyML đắp lên cấu trúc sản phẩm sinh nhai lúc một phân cấp không vỗ về vừa bụng mọi cái đe.
Những hệ tính công cụ nhãn qua được tạo hình sẵn (iron law, bottleneck principle, workload archetypes, and lighthouse models) vòng quay tới lui khắp chặng trang của chương sách kế. Tất thảy mẩu phần theo, đi từ bộ dữ liệu thiết kế đến tạo hình mô tính nén lại rồi phân truyền cắm cổng (serving), sống cùng vách trần bọc lại ở chương nãy (established here). Khuôn hướng giải vấn (decision framework) (hình 2.11) và bộ đong đếm kĩ quy phân (table 2.13) trao cung mấu móc dẫn mảng cày nháp ở những điểm thảo luận (discussions).


================ PAGE 119 ================

2. Hệ thống ML
81
Những Bài học Cốt lõi (Key Takeaways): Cùng một mô hình, kỹ thuật khác nhau
• Những ràng buộc vật lý định nghĩa tính khả thi (feasibility): Tốc độ ánh sáng (~36 ms vòng khứ hồi xuyên quốc gia), bức tường năng lượng, bức tường bộ nhớ, và các ngân sách độ trễ tạo ra những ranh giới cứng mà kỹ thuật không thể vượt qua, chỉ có thể điều hướng (navigate).
• Xác định điểm nghẽn cổ chai (bottlenecks) trước khi tối ưu hóa: Cùng một mô hình nhưng bị giới hạn bởi tính toán (compute bound) trong quá trình huấn luyện và bị giới hạn bởi bộ nhớ trong quá trình suy luận. Quy luật sắt và Nguyên lý Nút thắt Cổ chai sẽ chỉ ra chính xác ràng buộc nào đang chi phối; việc tối ưu hóa sai yếu tố (term) không mang lại bất kỳ sự tăng tốc nào.
• Nguyên mẫu khối lượng công việc quyết định tính khả thi của đợt triển khai: Một "Quái thú Tính toán" (Huấn luyện ResNet-50) yêu cầu quy mô đám mây; một "Ràng buộc Nhỏ bé" (Nhận diện từ khóa) đòi hỏi hiệu suất của vi điều khiển. Không thể sử dụng cùng một chiến lược tối ưu hóa cho cả hai—hãy khớp nguyên mẫu khối lượng công việc vào đúng mô hình triển khai.
• Công suất triển khai trải dài qua chín cấp số nhân (orders): Cơ sở hạ tầng trung tâm dữ liệu đám mây hoạt động ở quy mô megawatt, trong khi các hệ thống TinyML nhắm tới mục tiêu milliwatt. Khoảng cách này mở ra hoàn toàn các phân lớp ứng dụng khác nhau chứ không hẳn chỉ thể hiện một sự hạn chế.
• Những kiến trúc kết hợp rất phổ biến trong các hệ thống sản xuất (production systems): Trợ lý giọng nói bao phủ từ TinyML (từ đánh thức), Di động (speech-to-text), đến Đám mây (hiểu ngôn ngữ). Hiếm khi một mô hình triển khai duy nhất có thể đáp ứng đủ; các mẫu (patterns) tích hợp (Phân tách Huấn luyện-Phục vụ, Xử lý Phân cấp, Triển khai Lũy tiến) định hình (formalize) cách thức các mô hình kết hợp với nhau.
• Tốc độ toàn hệ thống (System-level speedup) tuân theo Định luật Amdahl, chứ không phải hiệu suất mô hình: Một mô hình chạy nhanh hơn 10 lần chỉ mang lại 1.37 lần tốc độ cho toàn hệ thống nếu ML chỉ chiếm 30 phần trăm đường ống (pipeline). Hãy phân tích cấu hình (Profile) toàn bộ hệ thống trước khi bắt tay vào tối ưu bất kỳ thành phần nào.
• Các nguyên tắc hệ thống phổ quát có thể chuyển đổi giữa các mô hình (paradigms): Các đường ống dữ liệu, quản lý tài nguyên, và kiến trúc hệ thống lặp lại (recur) ở mọi quy mô, đó là lý do tại sao những ý tưởng tối ưu hóa có thể di chuyển từ đám mây xuống vùng biên và ngược lại.
Bốn mô hình (paradigms) có vẻ giống như một thực đơn lựa chọn, nhưng chương này đã lập luận hoàn toàn ngược lại: chúng không phải là những phương án để người thiết kế tự do chọn, chúng là những vùng không gian được khoanh vùng (carves out) bởi các quy luật vật lý. Ba giới hạn thực hiện việc khoanh vùng, bao gồm tốc độ ánh sáng, bức tường năng lượng, và bức tường bộ nhớ, và nơi hệ thống phải chạy sẽ cố định (fixes) điều kiện nào trong số chúng sẽ chiếm vai trò chi phối (binds) trước. Đó là lý do tại sao cùng một mô hình lại trở thành một bài toán kỹ thuật (engineering problem) khác biệt giữa điện thoại và trung tâm dữ liệu, dù phần toán học không hề thay đổi. Do đó, mục tiêu triển khai (deployment target) không phải là một chi tiết được chốt hạ (settle) vào phút chót; nó là ràng buộc đầu tiên cần đọc vị (read), bởi vì nó quyết định quy luật vật lý nào sẽ chi phối mọi thứ diễn ra sau đó.
Điều gì Tiếp theo: Từ lý thuyết đến quy trình (From theory to process)
Việc lựa chọn nơi hệ thống vận hành đã quyết định (settles) tính chất vật lý của nó; song không bảo vệ nó khỏi dòng thời gian. Khoản ghi giảm (write-down) trị giá 304 triệu USD của Zillow không phải là một thất bại về độ chính xác của mô hình mà là sự thất bại của hệ thống tư duy lập luận (systems reasoning): không có quy trình nào theo dõi cách sự trôi dạt thị trường (drifting market) truyền tải qua mô hình định giá để chuyển hóa thành những cam kết không thể vãn hồi (irreversible commitments). Chương 3 sẽ thiết lập quy trình đó, nguyên tắc phát triển có hệ thống (systematic development discipline) dẫn dắt hệ thống ML từ khi hình thành khái niệm (conception) xuyên suốt tới khâu triển khai, đồng thời được xây dựng chuyên biệt nhằm kìm hãm ngay đúng lớp (class) lỗi kỹ thuật chết người kia trước thời điểm mọi thứ tự cộng dồn lại rồi hóa ung nhọt nguy hại.
Câu hỏi Nghiên cứu: Dành cho việc tìm hiểu sâu hơn (For further inquiry)
• Làm thế nào để các ràng buộc vật lý có thể xác định mô hình (paradigm) triển khai trước khi quá trình phát triển mô hình bắt đầu?
• Khi nào thì một hệ thống sản xuất nên kết hợp đám mây, vùng biên, thiết bị di động, hoặc TinyML thay vì chỉ chọn một mô hình duy nhất?


================ PAGE 120 ================
82
2.13 Tóm tắt
• Quy luật sắt (iron law) nên hướng dẫn việc tối ưu hóa như thế nào khi cùng một khối lượng công việc liên tục dịch chuyển (shifts) điểm nghẽn cổ chai giữa quá trình huấn luyện và suy luận?
• Bằng chứng nào sẽ chứng minh rằng tổng chi phí sở hữu (total cost of ownership), chứ không phải chi phí tính toán thô (raw compute cost), mới là yếu tố quyết định khả năng triển khai khả thi (feasible deployment)?


================ PAGE 121 ================

Ứng dụng
> _
Vận hành
Phục vụ (Serving)
Huấn luyện
∇
Các Mô hình
Các Khuôn khổ (Frameworks)
Phần cứng
Dữ liệu
3
Quy trình Công việc ML (ML Workflow)
3.1
Vòng đời ML (ML Lifecycle)
3.2
Các Giai đoạn Vòng đời
3.3
Định nghĩa Vấn đề
3.4
Thu thập Dữ liệu
3.5
Phát triển Mô hình
3.6
Đánh giá và Thẩm định (Evaluation and Validation)
3.7
Triển khai và Tích hợp
3.8
Giám sát và Bảo trì
3.9
Tư duy Hệ thống (Systems Thinking)
3.10 Nguỵ biện và Cạm bẫy
3.11 Tóm tắt
Mục đích
Tại sao việc nhìn thấy toàn bộ bản đồ trước khi bước đi trên bất kỳ một con đường đơn lẻ nào lại cần thiết?
Hệ thống phân loại D·A·M (D·A·M taxonomy) định danh (names) tất cả thành phần của mọi hệ thống ML, và vị trí triển khai sẽ quyết định (determines) các giới hạn (constraints) vật lý mà mỗi thành phần phải đáp ứng (satisfy). Các nhóm thường coi những thành phần này như những mối quan tâm riêng biệt (separate concerns): một nhóm thu thập dữ liệu, một nhóm khác thiết kế mô hình, và một nhóm thứ ba chuẩn bị (provisions) phần cứng. Thế nhưng bài học sâu sắc nhất của hệ thống phân loại là sự thật rằng những thành phần này luôn tương tác lẫn nhau. Dữ liệu được thu thập chi phối việc thuật toán nào là khả thi. Thuật toán được chọn quy định (dictates) loại phần cứng nào có thể chạy nó. Phần cứng mục tiêu lại tái định hình (reshapes) những gì dữ liệu có thể được xử lý. Chỉ cần kéo căng (Pull on) bất kỳ một sợi chỉ (thread) nào và toàn bộ hệ thống sẽ dịch chuyển.
Những tương tác này bộc lộ (play out) qua lại giữa các thành phần và theo thời gian: một mô hình biểu diễn tốt tại thời điểm ra mắt (launch) sẽ bắt đầu suy thoái (degrades) khi phân phối dữ liệu trôi dạt (drifts), buộc quá trình phải huấn luyện lại (retraining) vốn có thể đòi hỏi các phần cứng khác biệt hoặc đường ống dữ liệu được tinh chỉnh (revised). Việc tối ưu hóa biệt lập (isolation) mỗi thành phần chính là cách mà các nhóm kiến tạo ra các mô hình mang tính chính xác (accurate) vốn chẳng cách nào có thể đem ra triển khai cũng như các đường ống (pipelines) nhạy bén mang nguồn nguyên liệu số liệu (data) không đúng đi để nạp. Người lo phần dữ liệu (data engineer) thấu được quy trình biến đổi nguồn (preprocessing choices) đè lực chặn đứng phần phát kiến mô hình (downstream architectures) thế nào sẽ đúc nặn một bộ cung dẫn (pipelines) có phần không giống như kẻ chỉ coi thao tác xử nguồn ban đầu ngang hàng như ván bài không đụng độ liên đới; nhà soạn mô hình thấu đoạt được mức trần ngốn chứa cho không gian (memory budget) từ hệ máy mục tiêu cắm (deployment target) tận ngày đầu dựng hình sẽ đưa tay trỏ cách xếp loại khung (architecture decisions) trơn tru, không giống một gã chỉ nhăm nhe ngó số đo tốt đỉnh (accuracy) cõi sương mơ hồ chẳng tưởng (in a vacuum). Bước khi tính li ti của (details) mảng phần không tên bộc bạch tỏ thông, bộ bản đồ vẹn nguyên buộc trổ mặt: bằng cách định (built) tạo, nghiệm quy (evaluated), cùng neo giữ một bộ hệ ML làm mảng gạch nối đặc xệt tính vẹn liền (coherent whole). Khung chạy vận hành ML (ML workflow) ví bằng tấm sơ đồ chạy động (map set in motion): quá trình lặp gỡ hòa liên hoàn (iterative) của nhóm D·A·M xoáy qua nguồn khối liệu số, cấu hình phần cứng nhét tay cùng hệ thuật tính (algorithm) đến kỳ bung nở công lực cho kì bằng chạm chuẩn (requirements) nơi đời thường.
83


================ PAGE 122 ================