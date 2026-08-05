4
1.1 Khoảnh khắc AI
1
GPU (Khối Xử lý Đồ họa - Graphics Processing Unit):
Ban đầu được thiết kế để kết xuất (rendering) đồ họa trò chơi điện tử, một khối lượng công việc đòi hỏi hàng nghìn phép tính pixel đơn giản, song song. Sự kết hợp giữa phần cứng và thuật toán này đã tỏ ra mang tính quyết định đối với các mạng nơ-ron, nơi mà cùng một cấu trúc số học song song khổng lồ ánh xạ trực tiếp lên phép nhân ma trận, biến GPU trở thành nhân tố vật lý hỗ trợ chính cho quy mô huấn luyện hiện đại (xem Chương 11).
2
Andrej Karpathy:
Một thành viên sáng lập của OpenAI và cựu Giám đốc AI tại Tesla, người đã tiên phong trong việc ứng dụng học sâu (deep learning) vào các đội xe tự hành. Luận điểm "Phần mềm 2.0" (Software 2.0) của ông (2017) đã làm rõ một hiểu biết sâu sắc rằng trọng số (weights) của mạng nơ-ron chính là "mã nguồn" mới, buộc phải có một thực tế kỹ thuật mới: thay vì gỡ lỗi logic rõ ràng, các kỹ sư phải giám tuyển (curate) và quản lý phiên bản cho dữ liệu định nghĩa hành vi của chương trình, bởi vì một mô hình với hàng triệu tham số không thể được vá lỗi (patched) hay suy luận một cách trực tiếp.
Mục tiêu Học tập
• Giải thích tại sao hành vi được định nghĩa bằng dữ liệu và các ràng buộc vật lý phân biệt các hệ thống ML với phần mềm truyền thống
• Áp dụng lăng kính dữ liệu-thuật toán-máy móc (data-algorithm-machine) để chẩn đoán các nút thắt cổ chai về mặt di chuyển dữ liệu, tính toán số học, và giới hạn của máy móc
• Phân tích sự chuyển dịch của AI từ các quy tắc ký hiệu (symbolic rules) sang học sâu thông qua bài học đắng cay (bitter lesson)
• Tính toán các thuật ngữ hiệu suất theo quy luật sắt để suy luận về thông lượng, độ trễ, và lợi tức trên tính toán (return on compute)
• Tổng hợp vòng đời, triển khai, suy thoái, và các góc nhìn năm trụ cột thành các phán đoán kỹ thuật hệ thống ML
1.1 Khoảnh khắc AI (AI Moment)
Các hệ thống học máy bước vào cuộc sống hàng ngày không phải như những chương trình thông thường mà như một hành vi được định hình bởi dữ liệu chạy dưới sự ràng buộc vật lý. Khi một người dùng hỏi điện thoại thông minh một câu hỏi, một hệ thống AI chuyển đổi giọng nói thành văn bản, diễn giải ý định và tạo ra câu trả lời. Khi lướt mạng xã hội, các hệ thống AI quyết định những bài đăng nào xuất hiện và theo thứ tự nào. Khi nộp đơn xin vay vốn, các hệ thống AI đánh giá mức độ tín nhiệm tín dụng. Lái một chiếc xe hơi hiện đại, các hệ thống AI theo dõi vị trí làn đường, phát hiện người đi bộ và điều chỉnh hệ thống kiểm soát hành trình. Trong mỗi trường hợp, hệ thống không chỉ đơn thuần là truy xuất thông tin mà còn đưa ra các quyết định dưới sự không chắc chắn, thường xuyên kiểm soát các kết quả vật lý ảnh hưởng đến sự an toàn, tài chính, hoặc việc tiếp cận cơ hội. Đây không phải là những khả năng của tương lai; chúng là thực tế hiện tại đang ảnh hưởng đến hàng tỷ người mỗi ngày.
Việc xây dựng những hệ thống này trở thành một thách thức kỹ thuật khác biệt với phần mềm truyền thống bởi vì một nhiệm vụ kép. Mỗi hệ thống ML phải đồng thời quản lý tính không chắc chắn của thống kê, bởi vì dự đoán của mô hình mang tính xác suất, và các ràng buộc vật lý, bởi vì việc thực thi những dự đoán đó đòi hỏi phải di chuyển hàng terabyte dữ liệu và thực hiện hàng tỷ tỷ phép toán số học, thường là trong vòng vài mili giây. Sự khác biệt trở nên rõ ràng nhất ở ranh giới của sự thất bại: một lỗi mã (code bug) gây ra sự cố (crash), một thất bại hiển nhiên (loud failure), trong khi một lỗi dữ liệu (data bug) gây ra một dự đoán sai, một thất bại thầm lặng (silent failure). Khi độ chính xác của một hệ thống ML giảm đi 5 điểm phần trăm, dữ liệu huấn luyện có thể đã bị dịch chuyển phân phối, một quy trình gán nhãn có thể đã bị thay đổi, hoặc một mô hình có thể không còn đại diện cho hành vi sản xuất nữa. Việc gỡ lỗi, kiểm thử, và thiết kế kiến trúc đều thay đổi khi hành vi của một hệ thống được định nghĩa bởi dữ liệu thay vì bởi mã.
Nhiệm vụ kép này có thể được nhìn thấy trong mọi đợt triển khai AI quy mô lớn. Các dịch vụ AI đàm thoại điều phối các nhóm GPUs khổng lồ¹ trên khắp các trung tâm dữ liệu, thực hiện số lượng phép toán khổng lồ cho mỗi truy vấn trong khi vẫn phải quản lý bộ nhớ, băng thông mạng và các ràng buộc về nhiệt. Các hệ thống hỗ trợ người lái và lái xe tự động hiện đại xử lý các luồng cảm biến tốc độ cao, thường kết hợp camera với radar, LiDAR hoặc các cảm biến khác tùy thuộc vào nền tảng của chiếc xe, và kết hợp nhận thức thành các quyết định điều khiển trong vòng vài mili giây. Google xử lý 8.5 tỷ lượt tìm kiếm mỗi ngày, mỗi lượt kích hoạt nhiều hệ thống AI cho việc xếp hạng, trích xuất kiến thức và kiểm tra chính tả, tất cả trong khi vẫn phải đáp ứng các mục tiêu độ trễ nghiêm ngặt trên một cơ sở hạ tầng phân tán toàn cầu. Những hệ thống này không chỉ đơn thuần là chạy các thuật toán. Chúng điều phối dữ liệu, tính toán và phần cứng dưới những ràng buộc vật lý chặt chẽ để mang lại các kết quả thống kê đáng tin cậy ở quy mô lớn. Bên dưới tất cả chúng là hàm ý sâu sắc hơn của nhiệm vụ kép: khi dữ liệu chứ không phải mã định nghĩa hành vi, bản chất thực sự của phần mềm sẽ thay đổi.
1.2 Sự chuyển dịch Mô hình Lấy Dữ liệu làm Trung tâm (Data-Centric Paradigm Shift)
Khi một chương trình truyền thống thất bại, kỹ sư thường có thể truy vết một nhánh (branch), kiểm tra một khung ngăn xếp (stack frame), và vá đoạn mã đó lại. Khi độ chính xác của một hệ thống ML giảm xuống mà không có sự thay đổi nào về mã, mục tiêu gỡ lỗi có thể là một phân phối dữ liệu đã bị dịch chuyển, một quy trình dán nhãn bị thay đổi, hoặc một mô hình không còn đại diện cho hành vi sản xuất. Andrej Karpathy² đã chính thức hóa sự phân biệt này thành sự chuyển dịch từ Phần mềm 1.0 sang Phần mềm 2.0 (Karpathy 2017), một bộ khung cho sự dịch chuyển mô hình lập trình từ logic được viết bằng tay sang các trọng số được học (learned weights). Bảng 1.1 lập bản đồ sự chuyển dịch này trên từng khía cạnh, và hàng thúc đẩy phần còn lại của chương này là hệ quả về mặt hệ thống: Phần mềm 1.0 thất bại một cách hiển nhiên với một sự cố sập (crash), trong khi Phần mềm 2.0 có thể


================ PAGE 43 ================

1. Giới thiệu
5
Công việc ML trong sản xuất phần lớn là
về hệ thống xung quanh, chứ không chỉ
đơn thuần là mã của mô hình.
âm thầm suy thoái thông qua việc sụt giảm chỉ số (metric degradation), vì vậy sự cố vẫn vô hình cho đến khi một hệ thống giám sát phát hiện ra nó.
Bảng 1.1: Sự chuyển dịch Mô hình từ Phần mềm 1.0 sang Phần mềm 2.0: Trong Phần mềm 2.0, "lập trình viên" không viết logic; họ giám tuyển (curate) tập dữ liệu mà quy trình tối ưu hóa sử dụng để viết ra logic. Do đó, việc gỡ lỗi sẽ chuyển ngược lên thượng nguồn từ mã sang dữ liệu. Sự so sánh với "trình biên dịch" chỉ mang tính xấp xỉ: không giống như một trình biên dịch tất định, quy trình huấn luyện mang tính ngẫu nhiên (stochastic) và có thể tạo ra các "tệp thực thi" (executables) khác nhau từ cùng một "mã nguồn."
Tính năng (Feature)
Phần mềm 1.0 (Truyền thống)
Phần mềm 2.0 (Học máy)
Mã nguồn (Source Code)
C++, Python, Java
Dữ liệu Huấn luyện + Nhãn (Training Data + Labels)
Trình biên dịch (Compiler)
GCC, LLVM
Vòng lặp huấn luyện (Giảm gradient ngẫu nhiên - stochastic gradient descent)
Logic
Rõ ràng (Viết bằng tay)
Ngầm định (Được học)
Chế độ Lỗi (Failure Mode)
Hiển nhiên (Crash, Ngoại lệ - Exception)
Thầm lặng (Suy thoái Chỉ số - Metric Degradation)
Gỡ lỗi (Debugging)
Truy vết đường dẫn thực thi
Kiểm tra phân phối dữ liệu
Quy trình làm việc lấy dữ liệu làm trung tâm tạo ra một chi phí hệ thống vốn không xuất hiện trong các dự án phần mềm thông thường: hành vi của mô hình phụ thuộc vào các đường ống, các nhãn, việc giám sát, và các vòng lặp phản hồi bao quanh đoạn mã được học. Các nhà nghiên cứu của Google đã định lượng được khoản nợ kỹ thuật tiềm ẩn (hidden technical debt) đó trong một bài báo mang tính bước ngoặt năm 2015.
Ví dụ 1.1: Khoản nợ kỹ thuật tiềm ẩn của các hệ thống ML
Bối cảnh: Các kỹ sư của Google đã xuất bản một bài báo mang tính bước ngoặt (Sculley et al. 2015) làm thay đổi cách ngành công nghiệp nhìn nhận về kỹ thuật ML.
Hiểu biết sâu sắc: Họ đã chứng minh rằng trong các hệ thống ML trưởng thành, Mã ML (bản thân mô hình) thường chỉ là một phần nhỏ của toàn bộ hệ thống. Ô "Mã ML" trong sơ đồ của bài báo của họ chỉ chiếm khoảng 5 phần trăm diện tích của sơ đồ cơ sở hạ tầng xung quanh, không phải hiểu theo nghĩa đen là kiểm đếm số dòng mã (line-count audit) mà là một trực giác hữu ích về quy mô: việc thu thập dữ liệu, xác minh, trích xuất đặc trưng, quản lý tài nguyên, giám sát, và cơ sở hạ tầng phục vụ chiếm ưu thế trên bề mặt kỹ thuật.
Góc nhìn hệ thống: "Học máy" thì dễ; "Hệ thống Học máy" mới khó. Lực cản trong việc triển khai hiếm khi chỉ đến từ phép nhân ma trận; nó đến từ giao diện giữa phép toán đó và thực tế lộn xộn của hệ thống xung quanh. Chỉ tối ưu hóa mô hình là mới chỉ tối ưu hóa trung tâm có thể nhìn thấy được của một bài toán kỹ thuật lớn hơn rất nhiều.
Gánh nặng cơ sở hạ tầng là một thuộc tính cấu trúc của hệ thống, nhưng nó mang theo một hệ quả tinh vi hơn: khi 95 phần trăm bề mặt kỹ thuật nằm ngoài mô hình, bản thân đường ống dữ liệu sẽ trở thành một nguồn gây lỗi mà không một sự tinh chỉnh mô hình nào có thể giải quyết được.
Câu chuyện Chiến tranh 1.1: Khi nhật ký tìm kiếm nhầm lẫn sự chú ý với bệnh tật
Bối cảnh: Google Flu Trends (GFT) ước tính hoạt động của bệnh cúm từ các mẫu truy vấn tìm kiếm được tổng hợp, và được coi là ví dụ điển hình về một hệ thống dự đoán giàu dữ liệu được xây dựng dựa trên các dấu vết hành vi thay vì phép đo trực tiếp (Ginsberg et al. 2009). Trong một bài báo trên tạp chí Science năm 2014, David Lazer và các đồng nghiệp tại Northeastern, Harvard, và Đại học Houston đã kiểm toán GFT so với dữ liệu thực tế (ground truth) của CDC trong khoảng thời gian hoạt động từ năm 2011 đến 2013 (Lazer et al. 2014).
Chế độ lỗi: Proxy (đại lượng đại diện) đã bị trôi dạt (drifted). Hành vi tìm kiếm phản ứng với sự chú ý của giới truyền thông, với những thay đổi về sản phẩm của chính Google (tự động điền, đề xuất tìm kiếm có liên quan), và với thói quen ngày càng phát triển của người dùng—vì vậy, một mô hình từng tỏ ra mạnh mẽ khi đối chiếu với dữ liệu bệnh cúm lịch sử nay lại thực sự đang đuổi theo một tín hiệu có ý nghĩa liên tục thay đổi. Lazer và các đồng nghiệp đã đặt ra cụm từ "sự kiêu ngạo của dữ liệu lớn" (big data hubris) để mô tả giả định ngầm định rằng khối lượng có thể thay thế cho tính hợp lệ của phép đo. Trong mùa giải 2012–2013, GFT đã dự đoán tỷ lệ số lần khám bác sĩ do các bệnh giống cúm cao gấp đôi so với báo cáo của CDC, và đã đánh giá quá cao trong gần như mỗi tuần của khoảng thời gian được kiểm tra.


================ PAGE 44 ================

6
1.2 Sự chuyển dịch Mô hình Lấy Dữ liệu làm Trung tâm
3
Giảm Gradient Ngẫu nhiên (Stochastic Gradient Descent - SGD): Thuật toán thực hiện việc "biên dịch" logic từ dữ liệu bằng cách xử lý từng mẫu dữ liệu nhỏ, ngẫu nhiên (một "lô" - batch) tại một thời điểm, thay vì toàn bộ tập dữ liệu. Sự đánh đổi này, nhiễu thống kê đổi lấy tốc độ tính toán, chính là cỗ máy cốt lõi của "trình biên dịch" huấn luyện. Sự lựa chọn kích thước lô trở thành một cờ biên dịch (compilation flag) quan trọng; một lô quá nhỏ có thể không bão hòa được các bộ xử lý song song của một bộ tăng tốc, làm lãng phí phần lớn khả năng tính toán của nó.
4
Trọng số Mô hình (Model Weights): Các tham số bằng số học được (learned numerical parameters) của một mạng nơ-ron, một giá trị cho mỗi kết nối giữa các đơn vị (units). Một mô hình quy mô GPT-3 lưu trữ 175 tỷ giá trị như vậy, tiêu tốn 350 GB ở độ chính xác FP16, một định dạng dấu phẩy động 16-bit sử dụng hai byte cho mỗi giá trị (Brown et al. 2020). Bởi vì mỗi yêu cầu suy luận phải tải các trọng số này qua phân cấp bộ nhớ, số lượng trọng số là yếu tố quyết định lớn nhất đối với cả dấu vết bộ nhớ (memory footprint) và chi phí phục vụ (xem Chương 5).
Bài học hệ thống: Khối lượng dữ liệu không phải là dữ liệu thực tế (ground truth). Các hệ thống ML được xây dựng dựa trên các proxy hành vi cần có các vòng lặp phản hồi đến các phép đo lường đáng tin cậy, các kiểm tra liên tục để đảm bảo proxy vẫn theo dõi đại lượng mà nó tuyên bố đang đo lường, và sự hoài nghi đối với các tín hiệu có ý nghĩa thay đổi dưới tác động của chính hệ thống đang tiêu thụ chúng.
Sự cố đó không nằm ở mô hình mà nằm ở dữ liệu, và nó phản ánh cách thức các hệ thống ML được xây dựng: dữ liệu, chứ không phải mã, định nghĩa những gì hệ thống thực hiện. Đây là Bất biến Dữ liệu là Mã (Data as Code Invariant). Trong phần mềm truyền thống, một lập trình viên viết logic rõ ràng (nếu x > 0 thì y). Trong học máy, lập trình viên viết siêu-logic tối ưu hóa (optimization meta-logic) (thuật toán huấn luyện), nhưng logic vận hành thực sự được "biên dịch" từ tập dữ liệu huấn luyện thông qua giảm gradient ngẫu nhiên³ và các phương pháp tối ưu hóa liên quan. Tập dữ liệu đóng vai trò là mã nguồn, đường ống huấn luyện đóng vai trò là trình biên dịch, và các trọng số của mô hình⁴ đóng vai trò là tệp thực thi nhị phân.
Từ góc độ hệ thống, điều này đại diện cho một quá trình chuyển đổi từ tính toán lấy lệnh làm trung tâm (instruction-centric) sang tính toán lấy dữ liệu làm trung tâm (data-centric) (Ng 2021). Trong mô hình lấy lệnh làm trung tâm truyền thống, các hệ thống được tối ưu hóa cho việc thực thi hiệu quả các logic được làm thủ công, và công việc của lập trình viên là viết các lệnh (instructions) chính xác. Trong mô hình lấy dữ liệu làm trung tâm của học máy, thay vào đó, các hệ thống được tối ưu hóa cho việc tiếp nhận dữ liệu hiệu quả và sự tinh chỉnh lặp đi lặp lại các tham số của mô hình, và công việc của lập trình viên là giám tuyển dữ liệu chính xác.
Do đó, việc gỡ lỗi một hệ thống ML có nghĩa là gỡ lỗi dữ liệu, chứ không phải các kịch bản (scripts) Python. Kiểm soát phiên bản phải theo dõi các tập dữ liệu, không chỉ là các lượt git commit. Kiểm thử phải xác thực các phân phối dữ liệu, chứ không chỉ các đường dẫn mã. Tuy nhiên, ngay cả việc kiểm thử kỹ lưỡng cũng không thể thu hẹp được cái gọi là khoảng trống xác minh về mặt cấu trúc (structural verification gap) giữa các tập kiểm thử hữu hạn và không gian đầu vào liên tục, rộng lớn mà các hệ thống ML phải đối mặt trong sản xuất.
Góc nhìn Hệ thống 1.1: Khoảng trống xác minh
Trong Phần mềm 1.0, logic rời rạc. Chúng ta có thể viết các kiểm thử đơn vị (unit tests) bao phủ các trường hợp biên (edge cases) bởi vì không gian đầu vào thường có thể đếm được hoặc phân vùng được.
Trong Phần mềm 2.0, không gian đầu vào có số chiều cao (ví dụ, tất cả các hình ảnh khả dĩ). Mặc dù về mặt kỹ thuật là rời rạc, nhưng nó rộng lớn đến mức thực tế là không thể lấy mẫu hết. Hãy xem xét một bộ phân loại hình ảnh: một hình ảnh RGB 224×224 có 256^(150,528) cấu hình pixel khả dĩ, một con số với 362,508 chữ số. Tập kiểm thử của Thử thách Nhận dạng Hình ảnh Quy mô lớn ImageNet (ImageNet Large Scale Visual Recognition Challenge - ILSVRC) chỉ bao phủ 50,000 trong số đó (Russakovsky et al. 2015). Gọi Tổng Không gian Đầu vào (Total Input Space) biểu thị số lượng đầu vào khả dĩ và Độ Phủ Tập Kiểm thử (Test Set Coverage) biểu thị số lượng đầu vào mà một bộ kiểm thử thực sự đánh giá. Không có bộ kiểm thử nào có thể lấy mẫu không gian này một cách có ý nghĩa. Phương trình 1.1 nắm bắt sự chênh lệch này:
Khoảng trống Xác minh (Verification Gap) = Tổng Không gian Đầu vào − Độ Phủ Tập Kiểm thử ≈ Tổng Không gian Đầu vào
(1.1)
Khoảng trống này có nghĩa là chúng ta phải dựa vào giám sát thống kê trong sản xuất (Chương 14 phát triển cơ sở hạ tầng giám sát khiến điều này khả thi) thay vì chỉ xác minh trước khi triển khai. Sự đảm bảo tính đúng đắn được đánh đổi lấy độ tin cậy thống kê.
Khoảng trống xác minh là triệu chứng của một sự chuyển dịch sâu sắc hơn: từ các hệ thống tất định (deterministic) nơi tính đúng đắn có thể được chứng minh sang các hệ thống xác suất (probabilistic) nơi tính đúng đắn chỉ có thể bị giới hạn. Trong kỹ thuật hệ thống cổ điển, sự thành công được định nghĩa bằng tính tất định: cùng một đầu vào luôn tạo ra cùng một đầu ra. Trong kỹ thuật AI, phương sai (variance) là vốn có; tính "mềm dẻo" của dữ liệu (sự nhiễu của nó, sự trôi dạt của nó, các mẫu ẩn của nó) là nguồn gốc tạo nên trí thông minh của hệ thống nhưng cũng là nguyên nhân gây ra sự khó đoán định của nó. Các hệ thống truyền thống đạt được tính mạnh mẽ (robustness) thông qua việc chống lại sự thay đổi, trong khi các hệ thống ML đạt được tính mạnh mẽ thông qua việc thích ứng với sự thay đổi. Do đó, tính mạnh mẽ thực sự trong AI đến từ kỹ thuật cho khả năng quan sát (observability) và thích ứng thay vì sự cứng nhắc.
Việc tư duy lại về ngăn xếp (stack) cũng đòi hỏi bối cảnh lịch sử. Sự chuyển dịch từ tính toán lấy lệnh làm trung tâm sang lấy dữ liệu làm trung tâm không xảy ra trong một sớm một chiều; nó nổi lên qua bảy thập kỷ chuyển tiếp mô hình, mỗi mô hình đều phải vượt qua những nút thắt cổ chai của mô hình tiền nhiệm. Mỗi kỷ nguyên của AI đều phải đối mặt với một


================ PAGE 45 ================

1. Giới thiệu
7
5
Alan Turing:
Bài báo "Trò chơi Bắt chước" (Imitation Game) năm 1950 của ông đã tái định hình trí thông minh như một bài toán đo lường đầu ra (output-measurement problem): hãy đánh giá một hệ thống bằng những gì nó làm được, chứ không phải bằng bản chất của nó. Lập trường ưu tiên kỹ thuật (engineering-first) này vẫn tồn tại trong mọi chỉ số của hệ thống ML mà chúng ta sử dụng ngày nay: độ chính xác, độ trễ, thông lượng, và FLOP/s trên mỗi watt đều là các phép đo lường đầu ra. Quy luật sắt (phần 1.7) phân rã hiệu suất thành các thành phần có thể quan sát và đo lường được thay vì các thuộc tính kiến trúc bên trong chính là vì lý do này.
6
ELIZA: Một chương trình ngôn ngữ tự nhiên năm 1966 chạy trên các máy tính lớn (mainframe) 256 KB sử dụng các quy tắc khớp mẫu (pattern-matching rules) mà không có trạng thái được học (no learned state)—sự giòn gãy (brittleness) của nó là một hệ quả hệ thống trực tiếp của việc không có bộ nhớ (zero memory) qua các lượt hội thoại. Mỗi biến thể đầu vào mới đều đòi hỏi một quy tắc viết tay mới, làm cho chi phí bảo trì tăng nhanh hơn so với năng lực và báo trước nút thắt cổ chai về tri thức đã kết liễu các hệ chuyên gia (expert systems) một thập kỷ sau đó.
7
Các Mùa đông AI dưới tư cách là Thất bại Hệ thống: Mùa đông AI đầu tiên (1974–1980) thường được gắn với việc cắt giảm tài trợ sau Báo cáo Lighthill năm 1973, trong đó chỉ trích khoảng cách giữa những lời hứa hẹn của AI và kết quả thực tế mang lại (Lighthill 1973). Mùa đông thứ hai (1987–1993) liên quan đến sự sụp đổ của thị trường và nguồn tài trợ xoay quanh các hệ chuyên gia và các máy Lisp chuyên dụng khi các máy trạm đa dụng (general-purpose workstations) làm suy yếu tính kinh tế của chúng (Hendler 2008). Từ góc độ hệ thống của cuốn sách này, cả hai giai đoạn đều phơi bày tham vọng thuật toán vượt xa cơ sở hạ tầng khả dụng, sự hỗ trợ của thị trường, và sự trưởng thành của kỹ thuật, chứ không chỉ đơn thuần là sự thiếu hụt các thuật toán thông minh.
nút thắt cổ chai, và việc hiểu được những nút thắt đó tiết lộ tại sao kỹ thuật hệ thống lại trở thành trung tâm của sự tiến bộ.
Điểm kiểm tra 1.1: Sự chuyển dịch mô hình
Trước khi theo dõi lịch sử của AI, hãy xác minh sự hiểu biết của bạn về sự chuyển dịch mô hình trong cách chúng ta xây dựng phần mềm:
□Phần mềm 1.0 vs. 2.0: Bạn có thể phân biệt Phần mềm 1.0 (các lệnh rõ ràng) với Phần mềm 2.0 (các mục tiêu tối ưu hóa) không?
□Sự chuyển dịch trong việc gỡ lỗi: Bạn có hiểu tại sao "Dữ liệu là Mã Nguồn" (Data is Source Code) lại hàm ý rằng việc gỡ lỗi phải chuyển từ kiểm tra mã sang kiểm tra tập dữ liệu không?
□Khoảng trống xác minh: Tại sao tính đúng đắn cho các hệ thống ML không thể được đảm bảo về mặt toán học theo cùng một cách mà chúng ta có thể làm cho logic truyền thống?
1.3 Sự Tiến hóa của Mô hình AI
Sự tiến hóa của AI bộc lộ một chuỗi các nút thắt cổ chai, mỗi nút thắt lại được vượt qua bởi những đổi mới về hệ thống giúp mở rộng những gì có thể tính toán được. Lĩnh vực này có nguồn gốc từ bài báo "Máy Tính toán và Trí thông minh" (Computing Machinery and Intelligence) của Turing⁵ (Turing 1950), bài báo đã đặt ra câu hỏi nền tảng: Máy móc có thể suy nghĩ không? Những hệ thống ban đầu nỗ lực trả lời câu hỏi này, chẳng hạn như Perceptron (1958) (Rosenblatt 1958) và ELIZA⁶ (Weizenbaum 1966), đã vấp phải những giới hạn của logic thủ công và phần cứng kỷ nguyên máy tính lớn (mainframe), dẫn đến sự giòn gãy (brittleness). Các kỷ nguyên tiếp theo vấp phải nút thắt cổ chai thu nhận tri thức: việc nhập liệu tri thức thủ công không thể mở rộng quy mô. Các hệ thống hiện đại phải đối mặt với một ràng buộc khác: thông lượng tính toán.
Dòng thời gian trong hình 1.1 theo dõi tần suất trí tuệ nhân tạo được nhắc đến trong các cuốn sách đã xuất bản, một thước đo đại diện cho sự chú ý thay vì là thước đo trực tiếp cho sản lượng nghiên cứu, và nó tiết lộ một mô hình lặp đi lặp lại: những giai đoạn lạc quan mãnh liệt kéo theo sau là "những mùa đông AI"⁷ khi nguồn tài trợ sụp đổ, mỗi đợt đều bị kích hoạt bởi những hạn chế về hệ thống mà chỉ riêng các thuật toán thì không thể vượt qua. Nhịp điệu bùng nổ và suy thoái (boom-and-bust) kéo dài bảy thập kỷ tuân theo một mô hình nhất quán: mỗi mùa đông đều ập đến chính xác vào lúc mô hình thống trị chạm tới giới hạn hệ thống (systems ceiling) của nó, và mỗi đợt phục hồi đều theo sau một bước đột phá về cơ sở hạ tầng kỹ thuật thay vì chỉ trong các thuật toán. Mỗi kỷ nguyên đại diện cho một sự chuyển dịch mô hình nhằm cố gắng vượt qua những hạn chế của cách tiếp cận trước đó.
1.3.1 Kỷ nguyên tiền-học máy (prelearning era): Nút thắt logic và tri thức
Trước khi học máy tồn tại như một chuyên ngành, các kỹ sư đã cố gắng xây dựng các hệ thống thông minh thông qua hai mô hình kế tiếp nhau, mỗi mô hình đều vấp phải một rào cản mở rộng quy mô (scaling barrier) cơ bản. AI Ký hiệu (Symbolic AI) mã hóa trí thông minh dưới dạng các quy tắc logic và vấp phải nút thắt cổ chai logic: các quy tắc không thể nắm bắt được sự mơ hồ của thế giới thực. Hệ chuyên gia (Expert systems) mã hóa trí thông minh dưới dạng tri thức chuyên ngành và vấp phải nút thắt cổ chai tri thức: việc thu thập và duy trì tri thức đó trở nên đắt đỏ hơn giá trị mà các hệ thống mang lại. Cùng với nhau, hai kỷ nguyên này tiết lộ một mô hình tạo động lực cho mọi thứ theo sau: các biểu diễn thủ công không thể mở rộng quy mô.
1.3.1.1 Kỷ nguyên AI Ký hiệu: Nút thắt cổ chai logic
Kỷ nguyên đầu tiên của kỹ thuật AI (những năm 1950–1970) đã cố gắng thu gọn trí thông minh thành thao tác AI Ký hiệu, một cách tiếp cận sau này được đúc kết thành giả thuyết hệ thống-ký hiệu-vật lý (physical-symbol-system hypothesis) (Newell and Simon 1976). Các nhà nghiên cứu tại Hội nghị Dartmouth năm 1956⁸ (McCarthy et al. 1955) đã giả thuyết rằng các khía cạnh của trí thông minh có thể được mô tả chính xác và được mô phỏng bởi máy móc. Thậm chí ngay cả khi đó, một số người đã nhìn thấy một con đường khác: Arthur Samuel tại IBM đã chứng minh vào năm 1959 rằng một chương trình chơi cờ đam (checkers) có thể cải thiện thông qua việc tự chơi (self-play), đặt ra chính thuật ngữ "học máy" (machine learning) (Samuel 1959), mặc dù mô hình thống trị vẫn là ký hiệu (symbolic). Hệ thống STUDENT⁹ của Daniel Bobrow là ví dụ điển hình cho cách tiếp cận này (Bobrow 1964).
Mặc dù gây ấn tượng mạnh trong các buổi trình diễn, nhưng các hệ thống này lại rất giòn gãy (brittle) trong hoạt động thực tế. Chúng dựa vào các quy tắc được mã hóa thủ công (manually coded rules) cho mọi trạng thái khả dĩ. Một biến thể nhỏ trong cách diễn đạt đầu vào (ví dụ, "số lượng khách hàng của Tom" - "Tom's client count") sẽ gây ra lỗi hệ thống. Bài học kỹ thuật: logic rõ ràng không thể


================ PAGE 46 ================

8
1.3 Sự Tiến hóa của Mô hình AI
Mùa đông AI lần 1 (1st AI Winter)
Mùa đông AI lần 2 (2nd AI Winter)
1950
Alan Turing công bố "Máy Tính toán và Trí thông minh" (Computing Machinery and Intelligence) trên tạp chí Mind.
Các Cột mốc trong AI (Milestones in AI)
Mùa hè 1956
Hội thảo Dartmouth
Một hội nghị mang tính định hình được tổ chức bởi nhà tiên phong AI John McCarthy.
1957
Nhà tâm lý học tại Cornell, Frank Rosenblatt phát minh ra perceptron, đặt nền móng cho các mạng nơ-ron hiện đại.
1966
Chatbot ELIZA
Một ví dụ ban đầu về lập trình ngôn ngữ tự nhiên được tạo ra bởi giáo sư MIT Joseph Weizenbaum.
1979
Hans Moravec chế tạo Stanford Cart, một trong những phương tiện tự hành đầu tiên.
1981
Dự án Hệ thống Máy tính Thế hệ Thứ năm của Nhật Bản bắt đầu. Sự truyền tải nguồn tài trợ nghiên cứu giúp kết thúc "mùa đông AI" đầu tiên.
1997
Deep Blue của IBM đánh bại nhà vô địch cờ vua thế giới Garry Kasparov.
2011
Watson của IBM chiến thắng tại chương trình Jeopardy!
2005
DARPA Grand Challenge
Stanford giành chiến thắng trong cuộc thi xe không người lái lần thứ hai của cơ quan này bằng cách lái 212 km trên một con đường mòn chưa được diễn tập trước.
2020
OpenAI giới thiệu GPT-3. Mô hình ngôn ngữ tự nhiên cực kỳ mạnh mẽ này sau đó đã gây ra làn sóng phản đối dữ dội khi nó bắt đầu thốt ra những lời lẽ cố chấp.
Phần trăm sách xuất bản tại Mỹ trong cơ sở dữ liệu của Google có đề cập đến trí tuệ nhân tạo (artificial intelligence).
Hình 1.1: Dòng thời gian Phát triển AI: Một đường cong proxy theo trình tự thời gian theo phong cách Google Books/Ngram theo dõi các đề cập đến trí tuệ nhân tạo trong các cuốn sách được số hóa (Michel et al. 2011), với các dải xám đánh dấu hai khoảng thời gian Mùa đông AI (1974–1980, 1987–1993). Các hộp chú ý làm nổi bật các cột mốc quan trọng bao gồm Bài kiểm tra Turing (Turing 1950), hội nghị Dartmouth (McCarthy et al. 1955), Perceptron (Rosenblatt 1958), ELIZA (Weizenbaum 1966), Deep Blue (Campbell et al. 2002), và GPT-3 (Brown et al. 2020).
8
Hội nghị Dartmouth (1956): Buổi hội thảo nơi John McCarthy đã tạo ra thuật ngữ "trí tuệ nhân tạo". Những người tham gia hội thảo đã đóng khung trí thông minh trong các khía cạnh của ngôn ngữ, sự trừu tượng, giải quyết vấn đề, và khả năng tự cải thiện, mà ít chú ý đến các ràng buộc vật lý của lưu trữ và tính toán, những thứ sau này đã trở thành trọng tâm. Cùng một giả định phớt lờ tính toán (compute-agnostic), rằng một thuật toán tốt hơn luôn có thể vượt qua một giới hạn phần cứng, chính xác là những gì cuốn sách này tồn tại để sửa đổi: mọi chương tiếp theo đều lập luận rằng các ràng buộc hệ thống là các biến số thiết kế hàng đầu (first-class design variables), chứ không phải là những suy nghĩ muộn màng.
mở rộng quy mô để xử lý sự mơ hồ của thế giới thực. Sự phức tạp của "cơ sở quy tắc" (rule base) tăng lên theo cấp số nhân cho đến khi nó không thể bảo trì được nữa. Hạn chế này mở rộng ra ngoài phạm vi ngôn ngữ: công trình của Hans Moravec¹⁰ về điều hướng tự trị (autonomous navigation) tại Stanford đã tiết lộ rằng những tác vụ con người thấy tầm thường (nhìn, đi bộ, cầm nắm) lại khó kỹ thuật hóa (engineer) hơn nhiều so với những tác vụ con người thấy khó khăn, như cờ vua hoặc đại số.
Ví dụ 1.2: STUDENT (1964)
Bối cảnh: STUDENT đã chứng minh cách AI Ký hiệu có thể giải quyết một lớp hẹp các bài toán đại số bằng lời (algebra word problems) bằng cách dịch ngôn ngữ thành cấu trúc logic được mã hóa bằng tay.
Cơ chế:
Bài toán: "Nếu số lượng khách hàng Tom nhận được gấp hai lần bình phương của 20% số lượng quảng cáo mà anh ta chạy, và số lượng quảng cáo là 45, thì số lượng khách hàng Tom nhận được là bao nhiêu?"


================ PAGE 47 ================

1. Giới thiệu
9
9
STUDENT: Hệ thống năm 1964 của Daniel Bobrow tại MIT đã phơi bày chế độ lỗi (failure mode) cốt lõi của AI ký hiệu: độ phức tạp tăng nhanh hơn năng lực. Mỗi loại bài toán mới đều yêu cầu các quy tắc phân tích cú pháp (parsing rules) viết tay mới, do đó gánh nặng bảo trì của hệ thống mở rộng theo tỷ lệ siêu tuyến tính (superlinearly) với phạm vi bao phủ (coverage). Các cách tiếp cận hướng dữ liệu (data-driven) phá vỡ cái bẫy này bằng cách học ánh xạ từ các ví dụ thay vì mã hóa nó thành các quy tắc, đó là lý do tại sao sự chuyển dịch sang ML thống kê trong những năm 1980–90 về cơ bản là một bước đột phá trong việc mở rộng quy mô, chứ không chỉ đơn thuần là sự cải thiện độ chính xác.
10
Nghịch lý Moravec (Moravec's Paradox): Nhà nghiên cứu robot của Đại học Carnegie Mellon, Hans Moravec, đã quan sát thấy rằng suy luận cấp cao (cờ vua) đòi hỏi ít tính toán trong khi nhận thức cấp thấp (đi bộ) lại đòi hỏi tính toán song song quy mô lớn (Moravec 1988). Nghịch lý này giải thích một thực tế cốt lõi của kỹ thuật hệ thống ML: những tác vụ có vẻ "dễ dàng" đối với con người (thị giác, giọng nói, điều khiển vận động) lại là những tác vụ đòi hỏi FLOP/s, băng thông bộ nhớ và phần cứng chuyên dụng cao nhất, thúc đẩy cuộc cách mạng bộ tăng tốc (accelerator revolution) vốn định hình nên cơ sở hạ tầng ML hiện đại.
11
Nút thắt cổ chai Thu nhận Tri thức (Knowledge Acquisition Bottleneck): Công trình kỹ thuật tri thức của Feigenbaum đã đóng khung AI ứng dụng xoay quanh khó khăn thực tế trong việc trích xuất, biểu diễn và duy trì tri thức của chuyên gia (Feigenbaum 1984). Xét về thuật ngữ hệ thống, nút thắt này là một vấn đề về thông lượng: việc khơi gợi tri thức (knowledge elicitation) và duy trì quy tắc bị giới hạn bởi băng thông nối tiếp (serial bandwidth) của các chuyên gia con người. Không giống như các nút thắt tính toán có thể được giải quyết bằng phần cứng nhanh hơn, đây là ràng buộc "không thể mở rộng quy mô" nguyên bản trong AI và là động lực trực tiếp cho mô hình hướng dữ liệu xuất hiện sau đó.
STUDENT sẽ làm như sau:
1. Phân tích cú pháp văn bản tiếng Anh
2. Chuyển đổi văn bản thành các phương trình đại số
3. Giải phương trình: n = 2(0.2 × 45)²
4. Đưa ra câu trả lời: 162 khách hàng
Bài học hệ thống: Quá trình chứng minh (demonstration) hoạt động được là do bài toán phù hợp với các quy tắc mà hệ thống đã biết. Khi cách diễn đạt, miền (domain), hoặc cấu trúc bài toán thay đổi, gánh nặng kỹ thuật sẽ quay trở lại với việc duy trì thủ công trình phân tích cú pháp (parser) và cơ sở quy tắc.
1.3.1.2 Kỷ nguyên Hệ chuyên gia: Nút thắt cổ chai tri thức
Trong kỷ nguyên hệ chuyên gia, các kỹ sư đã chuyển hướng từ logic tổng quát sang việc nắm bắt kiến thức chuyên môn sâu sắc. MYCIN, được thiết kế để chẩn đoán nhiễm trùng máu, bao gồm các khả năng thu nhận quy tắc cho phép các chuyên gia về lĩnh vực đó bổ sung trực tiếp tri thức (Shortliffe et al. 1975).
Ví dụ 1.3: MYCIN (1976)
Bối cảnh: MYCIN đã mã hóa chuyên môn y tế dưới dạng các quy tắc sản xuất rõ ràng (explicit production rules) với các trọng số không chắc chắn (uncertainty weights).
Cơ chế:
Ví dụ về Quy tắc từ MYCIN:
NẾU (IF)
Tình trạng nhiễm trùng là vãng khuẩn huyết nguyên phát (primary-bacteremia)
Vị trí lấy mẫu cấy là một trong các vị trí vô trùng
Cửa ngõ xâm nhập nghi ngờ là đường tiêu hóa
THÌ (THEN)
Tìm thấy bằng chứng gợi ý (0.7) rằng nhiễm trùng do vi khuẩn Bacteroides
Bài học hệ thống: Các hệ chuyên gia có thể nắm bắt logic của chuyên gia, nhưng mỗi căn bệnh mới, nguồn bằng chứng mới và ngoại lệ mới lại mở rộng thêm gánh nặng về thu nhận và duy trì tri thức.
MYCIN hoạt động tốt hơn các bác sĩ thực tập trong các bài kiểm tra cụ thể nhưng lại bộc lộ nút thắt cổ chai thu nhận tri thức¹¹. Việc trích xuất trực giác ngầm định từ các chuyên gia con người và chính thức hóa nó thành các quy tắc IF-THEN đã tỏ ra chậm chạp, dễ xảy ra lỗi và mâu thuẫn.
Việc duy trì một hệ thống với hàng ngàn quy tắc mâu thuẫn nhau đã trở thành một vấn đề kỹ thuật hệ thống không thể giải quyết được. Thất bại này đã chứng minh rằng AI có thể mở rộng quy mô (scalable AI) đòi hỏi các hệ thống phải học các quy tắc từ dữ liệu, thay vì được các kỹ sư đưa vào một cách thủ công.
1.3.2 Kỷ nguyên học thống kê: Nút thắt cổ chai kỹ thuật đặc trưng (feature engineering bottleneck)
Những năm 1990 đánh dấu sự chuyển dịch sang học thống kê và các hệ thống xác suất. Thay vì các logic được mã hóa cứng (hard-coded logic), các hệ thống ước tính xác suất từ dữ liệu (𝑝(𝑦∣𝑥)). Quá trình chuyển đổi này được thúc đẩy bởi sự sẵn có của dữ liệu kỹ thuật số và "tính hiệu quả phi lý" (unreasonable effectiveness)¹² của các tập dữ liệu lớn.
Việc lọc thư rác minh họa rõ nét sự chuyển dịch này. Thay vì duy trì danh sách các từ cấm, các bộ lọc thống kê học xác suất để một từ ngụ ý đó là thư rác dựa trên hàng triệu ví dụ.
Ví dụ 1.4: Các hệ thống phát hiện thư rác đời đầu
Dựa trên quy tắc (Những năm 1980): NẾU chứa("viagra") HOẶC chứa("người chiến thắng") THÌ là thư rác
Thống kê (Những năm 1990):
𝑝(thư rác ∣ từ) = tần suất xuất hiện trong thư rác / tổng tần suất xuất hiện


================ PAGE 48 ================

1. Giới thiệu
11
các đặc trưng và các lớp kết nối đầy đủ tạo ra phân loại cuối cùng, tất cả sẽ được phát triển trong các chương sau; điều quan trọng ở đây là kiến trúc tách thành hai luồng xử lý song song. Sự phân tách đó phản ánh giới hạn bộ nhớ của một GPU GTX 580 duy nhất, khiến một phần cấu trúc của mạng trở thành sản phẩm từ các ràng buộc phần cứng của nó.
Hình 1.2: Kiến trúc AlexNet: Mạng nơ-ron đã khởi động cuộc cách mạng học sâu tại ImageNet 2012 (Krizhevsky et al. 2012). Hai luồng GPU song song xử lý các hình ảnh đầu vào 224×224 thông qua các lớp tích chập (convolutional layers - các khối màu xanh lá) trích xuất các đặc trưng không gian ở độ phân giải giảm dần, hội tụ qua ba lớp kết nối đầy đủ để đưa ra 1.000 lớp (classes) đầu ra. Với 60 triệu tham số được huấn luyện trên hai GPU GTX 580, AlexNet đạt được tỷ lệ lỗi top-5 là 15,3 phần trăm, một sự cải thiện tương đối 41,6 phần trăm so với mục dự thi đứng thứ hai.
Học sâu thực chất đã đánh đổi nút thắt cổ chai về kỹ thuật đặc trưng lấy một nút thắt cổ chai tính toán mới. Các mô hình như GPT-3 (Brown et al. 2020) (175 tỷ tham số) minh họa quy mô của thách thức mới này. Brown và các cộng sự báo cáo việc huấn luyện trên khoảng 300 tỷ token từ văn bản web đã được lọc, sách, và Wikipedia. Sử dụng phép xấp xỉ huấn luyện dày đặc (dense-training approximation) của cuốn sách, quy mô tham số-token đó ngụ ý khoảng 314 zettaFLOPs tính toán; bởi vì bài báo GPT-3 không chỉ định chính xác cấu hình phần cứng, bất kỳ sự chuyển đổi sang GPU-year V100 nào đều là một ước tính mang tính minh họa nội bộ chứ không phải là một thực tế được báo cáo. (Một zettaFLOP bằng 10²¹ phép toán dấu phẩy động; kho ngữ liệu huấn luyện bao gồm khoảng 420 GB văn bản.) Thách thức kỹ thuật chính đã chuyển từ "làm thế nào để chúng ta mô tả tai của một con mèo?" sang "làm thế nào để chúng ta điều phối quá trình huấn luyện phân tán quy mô lớn mà không bị lỗi?"
Với việc theo dõi bốn quá trình chuyển đổi mô hình này, mô hình (pattern) trở nên hiển nhiên trong Bảng 1.2: bước đột phá của mỗi kỷ nguyên không đến từ các thuật toán thông minh hơn mà từ việc loại bỏ một nút thắt cổ chai hệ thống vốn ngăn cản các thuật toán hiện tại sử dụng nhiều dữ liệu và tính toán hơn. AI Ký hiệu có các thuật toán logic nhưng thiếu dữ liệu; hệ chuyên gia có tri thức lĩnh vực nhưng không thể mở rộng quy mô; học thống kê có dữ liệu nhưng đòi hỏi kỹ thuật đặc trưng thủ công; học sâu tự động hóa việc học đặc trưng nhưng đòi hỏi cơ sở hạ tầng chưa từng tồn tại. Chủ đề lặp đi lặp lại là những đổi mới về hệ thống, chứ không phải đổi mới về thuật toán, đã kích hoạt mỗi sự chuyển đổi, và nó đặt ra một tình thế tiến thoái lưỡng nan trong thực tế: với các nguồn lực hạn chế, các tổ chức phải quyết định xem nên đầu tư vào các thuật toán tốt hơn, các tập dữ liệu lớn hơn hay phần cứng có thông lượng cao hơn. Một trong những nhà nghiên cứu hàng đầu về AI đã kiểm tra hồ sơ lịch sử một cách có hệ thống và đưa ra một kết luận thách thức những trực giác sâu sắc nhất của chúng ta về việc trí thông minh nên được xây dựng như thế nào.
Bảng 1.2: Sự Tiến hóa của Mô hình AI: Mỗi kỷ nguyên được định nghĩa bởi nút thắt cổ chai hệ thống đã kìm hãm nó. Học sâu (ngoài cùng bên phải) đã vượt qua nút thắt cổ chai Kỹ thuật Đặc trưng nhưng lại đưa ra những thách thức cơ sở hạ tầng mới, đòi hỏi kỹ thuật hệ thống ML hiện đại.
Khía cạnh (Aspect)
AI Ký hiệu (Symbolic AI)
Hệ Chuyên gia (Expert Systems)
Học Thống kê (Statistical Learning)
Học Sâu (Deep Learning)
Điểm mạnh Cốt lõi
Suy luận logic
Chuyên môn lĩnh vực (Domain expertise)
Tính linh hoạt
Nhận dạng mẫu (Pattern recognition)
Nút thắt cổ chai (Bottleneck)
Sự giòn gãy (Brittleness - Quy tắc bị phá vỡ)
Nhập liệu Tri thức (Knowledge Entry - Chuyên gia khan hiếm)
Kỹ thuật Đặc trưng (Manual preprocessing)
Quy mô Tính toán & Dữ liệu (Chi phí cơ sở hạ tầng)
Xử lý Dữ liệu
Cần tối thiểu dữ liệu
Dựa trên tri thức lĩnh vực
Cần một lượng dữ liệu vừa phải
Xử lý dữ liệu quy mô lớn (Massive)
1.4 Bài học Đắng cay (Bitter Lesson)
Các hệ chuyên gia đầu tư nỗ lực kỹ thuật vào việc mã hóa tri thức lĩnh vực; các hệ thống học sâu đầu tư nỗ lực đó vào việc hấp thụ nhiều dữ liệu và tính toán hơn. "Bài học Đắng cay" thâu tóm lịch sử


================ PAGE 50 ================

12
1.4 Bài học Đắng cay
14
Richard Sutton: Một nhà tiên phong về học tăng cường (reinforcement learning), người có bài luận năm 2019 đã kết tinh mô hình được theo dõi trong các phần trước: từ AI ký hiệu qua các hệ chuyên gia đến học sâu, các phương pháp tổng quát (general methods) sử dụng tính toán liên tục vượt trội so với chuyên môn được kỹ thuật hóa thủ công (hand-engineered expertise). Bài học này "đắng cay" bởi vì nó ngụ ý rằng logic đặc thù cho một lĩnh vực cụ thể (domain-specific logic) là một tài sản ngày càng giảm giá trị, trong khi lợi thế bền vững thuộc về kỹ thuật hệ thống có khả năng hấp thụ sự gia tăng gấp hàng tỷ lần của tính toán thô kể từ những năm 1970.
15
Deep Blue: Hệ thống chơi cờ vua của IBM (Campbell et al. 2002) đã đánh bại Nhà vô địch Thế giới Garry Kasparov vào năm 1997 thông qua sự kết hợp hệ thống: tìm kiếm với tốc độ khoảng 200 triệu nước đi mỗi giây trên 480 bộ vi xử lý cờ vua tùy chỉnh, cộng với đánh giá và kiến thức chuyên biệt về cờ vua. Deep Blue là một trong những minh chứng công khai đầu tiên cho thấy silicon được chế tạo chuyên dụng có thể khuếch đại việc tìm kiếm và tri thức miền (domain knowledge) được mã hóa, báo trước chiến lược bộ tăng tốc chuyên biệt theo miền định hình nên phần cứng ML hiện đại.
16
AlphaGo: Lần đầu tiên AlphaGo học từ các trận đấu của con người, sau đó được cải tiến thông qua việc học tăng cường từ việc tự chơi (self-play), đánh đổi chiến lược cờ vây (Go) được mã hóa thủ công để lấy một đường ống dữ liệu-và-tính toán có thể khám phá không gian vấn đề (problem space) ở quy mô tính toán lớn. Hệ thống kế nhiệm, AlphaGo Zero, sử dụng độc quyền nguyên tắc này: nó đã vượt qua phiên bản gốc chỉ sau 3 ngày chạy trên 4 TPU, giành chiến thắng 100 ván với tỷ số 100-0. Việc phân bổ bộ tăng tốc được nêu đó tương ứng với 288 giờ TPU (TPU-hours), biến ngân sách cơ sở hạ tầng, chứ không phải là chuyên môn mã hóa thủ công, trở thành ràng buộc cốt yếu (binding constraint).
mô hình này: các phương pháp tổng quát tận dụng việc gia tăng tính toán luôn vượt trội so với các cách tiếp cận mã hóa chuyên môn của con người. Richard Sutton¹⁴ đã đúc kết nhận định này trong bài luận năm 2019 "Bài học Đắng cay" (Sutton 2019), viết: "Bài học lớn nhất có thể rút ra từ 70 năm nghiên cứu AI là các phương pháp tổng quát tận dụng tính toán xét cho cùng là hiệu quả nhất, và với một khoảng cách lớn."
Bảng 1.3 định lượng sự dịch chuyển từ các hệ chuyên gia sang học thống kê và đến học sâu: hiệu suất của tác vụ đại diện được cải thiện khi mỗi quá trình chuyển đổi mở khóa thêm nhiều quy mô tính toán thay vì phải thiết kế nhiều biểu diễn tri thức con người phức tạp hơn. Cột ngoài cùng bên phải chỉ ra mô hình hệ thống: khi nguồn tài nguyên tính toán phát triển từ việc đánh giá các quy tắc đến các đường ống đặc trưng thời đại CPU, đến huấn luyện đa GPU (multi-GPU), và cuối cùng là huấn luyện phân tán quy mô lớn, hiệu suất đã được cải thiện từ mức nghiệp dư đến mức siêu phàm. Cấu hình huấn luyện chính xác của GPT-4 không được tiết lộ, vì vậy bảng sử dụng neo tham chiếu mlsysim minh họa thay vì tiết lộ huấn luyện chính thức: 2.5 triệu ngày-GPU tham chiếu, cùng một cường độ quy mô như 25,000 GPU tham chiếu trong khoảng 90 ngày (SemiAnalysis 2023).
Bảng 1.3: Sự Tiến hóa Hiệu suất AI qua các Mô hình: Mỗi lần chuyển đổi mô hình (paradigm transition) có tương quan với việc tăng quy mô tính toán thay vì sự phức tạp tinh vi của thuật toán. Hiệu suất được cải thiện từ các hệ chuyên gia cấp nghiệp dư (2000 Elo) thông qua việc học thống kê độ chính xác cao trên các điểm chuẩn có ràng buộc cho đến các mô hình nền tảng cấp siêu phàm (siêu phàm - superhuman) (86.4% ở bộ kiểm tra Hiểu Ngôn ngữ Đa nhiệm Khổng lồ - Massive Multitask Language Understanding (MMLU)), trong khi các yêu cầu tính toán tăng trưởng từ các đường ống đặc trưng kỷ nguyên CPU đến huấn luyện phân tán quy mô lớn. Các chi tiết huấn luyện GPT-4 không phải là công bố chính thức, do đó, giá trị ngoài cùng bên phải là một mỏ neo minh họa quy mô thay vì là kết quả chuẩn.
Kỷ nguyên (Era)
Cách tiếp cận (Approach)
Tác vụ Đại diện
Hiệu suất (Performance)
Nguồn lực Tính toán
Hệ Chuyên gia (Expert Systems) (1980s)
Các quy tắc thủ công
Cờ vua (hệ số Elo)
~2000 Elo (nghiệp dư)
Tối thiểu (đánh giá quy tắc)
Học Thống kê (Statistical ML) (1990s–2000s)
Kỹ thuật đặc trưng + học
Nhận dạng chữ số viết tay
khoảng 98–99% trên các điểm chuẩn kỷ nguyên MNIST
Đường ống đặc trưng kỷ nguyên CPU; nguồn lực thay đổi tùy theo việc triển khai
Học Sâu (Deep Learning) (2012)
Mạng nơ-ron từ-đầu-đến-cuối (End-to-end)
Độ chính xác top-5 ImageNet
84.7% (AlexNet)
6 ngày trên 2 GPUs
Học Sâu Hiện đại (2020+)
Transformer quy mô lớn
Độ chính xác top-5 ImageNet
90%+ (ViT) (Dosovitskiy et al. 2021)
Vài giờ trên các hệ thống phân tán
Học Sâu Hiện đại (2023)
Mô hình nền tảng (Foundation models)
Điểm chuẩn MMLU
86.4% (GPT-4) (OpenAI et al. 2023)
Không tiết lộ; neo minh họa mlsysim khoảng 2.5 triệu ngày-GPU tham chiếu (cùng quy mô với 25,000 GPU tham chiếu trong 90 ngày) (SemiAnalysis 2023)
Bảng biểu tiết lộ thêm hai hiểu biết sâu sắc. MMLU (Hiểu Ngôn ngữ Đa nhiệm Khổng lồ), một điểm chuẩn (benchmark) đánh giá kiến thức rộng lớn qua nhiều chủ đề, đóng vai trò mỏ neo cho hàng mô hình nền tảng; Chương 12 sẽ chính thức hóa cách diễn giải các điểm chuẩn như vậy. Đối với các tác vụ chuẩn cố định như ImageNet, việc huấn luyện phân tán đã đẩy lùi thời gian huấn luyện từ các đợt chạy AlexNet kéo dài nhiều ngày trở lại mức vài giờ; các đợt chạy mô hình nền tảng hàng đầu vẫn mất vài ngày đến vài tháng bởi vì các đội ngũ tái đầu tư sự song song hóa vào việc gia tăng quy mô lớn hơn nữa. Những cải tiến ấn tượng nhất đã xảy ra tại các quá trình chuyển đổi mô hình (hệ chuyên gia sang học thống kê, học thống kê sang học sâu) khi các cách tiếp cận mới mở khóa khả năng sử dụng tính toán hiệu quả hơn. Mô hình này xác nhận quan sát của Sutton: tiến bộ đến từ việc tìm cách sử dụng nhiều tính toán hơn, chứ không phải từ việc mã hóa thêm nhiều tri thức con người.
Nguyên tắc này tìm thấy sự xác nhận sâu sắc hơn trên khắp các bước đột phá của AI. Trong cờ vua, Deep Blue của IBM đã đánh bại nhà vô địch thế giới Garry Kasparov¹⁵ vào năm 1997 bằng cách kết hợp phần cứng cờ vua tùy chỉnh, tìm kiếm quy mô lớn và tri thức đánh giá chuyên biệt về cờ vua. Hàm đánh giá của nó mã hóa các kinh nghiệm đánh cờ (heuristics) của con người, nhưng quy mô tìm kiếm được hỗ trợ bởi silicon tùy chỉnh mới là yếu tố trung tâm để biến tri thức đó thành một lối chơi đẳng cấp thế giới. Trong cờ vây (Go), AlphaGo của DeepMind¹⁶ (Silver et al. 2016) đã đạt được hiệu suất siêu phàm bằng cách kết hợp học có giám sát từ các trận đấu của chuyên gia với học tăng cường thông qua quá trình tự chơi và tìm kiếm cây (tree search) có sự chỉ dẫn của mạng nơ-ron, thay vì dựa dẫm vào các chiến lược cờ vây được mã hóa thủ công.


================ PAGE 51 ================

1. Giới thiệu
13
17
Năng lượng Huấn luyện GPT-3: Patterson và cộng sự (2021) ước tính một lần huấn luyện duy nhất của GPT-3 tiêu tốn khoảng 1.287 MWh và thải ra 552 tấn lượng CO2 tương đương, gần bằng lượng điện năng sử dụng hàng năm của 120 hộ gia đình trung bình ở Hoa Kỳ dựa trên mức cơ sở 10,7 MWh/hộ gia đình-năm. Chi phí năng lượng được định hình không chỉ bởi số học mà còn bởi sự di chuyển dữ liệu qua phân cấp bộ nhớ; việc di chuyển dữ liệu qua các tầng bộ nhớ có thể tiêu tốn nhiều năng lượng hơn so với số học cục bộ theo mức độ nhiều cấp số nhân (orders of magnitude) (Horowitz 2014).
18
Băng thông Bộ nhớ (Memory Bandwidth): Tốc độ mà các tham số của mô hình di chuyển từ bộ nhớ sang bộ vi xử lý. Năng lượng tính bằng gigawatt-giờ tiêu thụ bởi quá trình huấn luyện ở quy mô GPT không chỉ được định hình bởi quá trình tính toán mà còn bởi quá trình vật lý đắt đỏ của việc tìm nạp (fetching) hàng tỷ trọng số thông qua phân cấp bộ nhớ. Việc di chuyển dữ liệu từ bộ nhớ ngoài chip (off-chip memory) có thể tốn nhiều năng lượng hơn từ một đến vài bậc so với số học cục bộ, tùy thuộc vào độ chính xác và cấp độ bộ nhớ, điều này khiến băng thông, chứ không chỉ riêng tốc độ bộ vi xử lý, trở thành động lực trực tiếp tạo ra sức hút năng lượng khổng lồ của trung tâm dữ liệu.
Bài học này "đắng cay" bởi vì trực giác của chúng ta đang đánh lừa chúng ta. Chúng ta tự nhiên giả định rằng việc mã hóa chuyên môn của con người phải là con đường dẫn đến trí tuệ nhân tạo. Tuy nhiên, liên tục hết lần này đến lần khác, các hệ thống sử dụng sức mạnh tính toán để học từ dữ liệu luôn vượt trội so với các hệ thống dựa vào tri thức con người, khi chúng có đủ quy mô (scale). Quy luật (pattern) này đã được giữ nguyên qua các kỷ nguyên AI ký hiệu, học thống kê, và học sâu.
Các mô hình ngôn ngữ hiện đại như GPT-4 và các hệ thống tạo hình ảnh như DALL-E minh họa nguyên tắc này một cách trực tiếp. Các khả năng của chúng nổi lên không phải từ các lý thuyết ngôn ngữ hay nghệ thuật được mã hóa bởi con người, mà từ việc huấn luyện các mạng nơ-ron đa năng trên một lượng lớn dữ liệu sử dụng nguồn tài nguyên tính toán khổng lồ. Các ước tính cho các mô hình ở quy mô của GPT-3 đề xuất khoảng 1.3 GWh năng lượng¹⁷ (Patterson et al. 2021), và việc phục vụ những mô hình này cho hàng triệu người dùng biến việc suy luận (inference) thành một vấn đề liên tục về điện năng, làm mát và hoạch định năng lực (capacity-planning) cho trung tâm dữ liệu.
Ý nghĩa (implication) là việc hiện thực hóa lời hứa của "Bài học Đắng cay" đòi hỏi kiến thức chuyên môn về kỹ thuật dữ liệu, tối ưu hóa phần cứng, và điều phối hệ thống¹⁸ vượt xa sự đổi mới thuật toán. Chúng ta sẽ khám phá những ràng buộc phần cứng này một cách định lượng trong Chương 11, nơi sinh viên sẽ có đủ nền tảng kiến thức tiên quyết để phân tích những hạn chế về băng thông bộ nhớ và ý nghĩa của chúng đối với thiết kế hệ thống.
Bài học đắng cay của Sutton giải thích động lực đằng sau kỹ thuật hệ thống ML. Nếu sự tiến bộ của AI phụ thuộc vào khả năng mở rộng quy mô tính toán một cách hiệu quả của chúng ta, thì việc hiểu cách xây dựng, triển khai, và duy trì những hệ thống tính toán này là điều thiết yếu đối với những người thực hành AI. Thế nhưng, sự thấu hiểu này đòi hỏi nhiều hơn sự quen thuộc với bất kỳ lĩnh vực kỹ thuật đơn lẻ nào. Khoa học Máy tính thúc đẩy các thuật toán ML, và Kỹ thuật Điện phát triển phần cứng AI chuyên dụng, nhưng không kỷ luật nào trong số đó tự nó cung cấp đủ các nguyên tắc kỹ thuật cần thiết để triển khai, tối ưu hóa, và duy trì các hệ thống ML ở quy mô lớn. Sự hội tụ giữa quản lý dữ liệu, thiết kế thuật toán, và tối ưu hóa cơ sở hạ tầng vào thành một thách thức kỹ thuật duy nhất đã tạo ra một chuyên ngành mới, thứ mà chúng tôi sẽ định nghĩa chính thức ở phần sau trong chương này và phát triển nó xuyên suốt toàn bộ cuốn sách.
Bài học đắng cay cho chúng ta biết lý do tại sao quy mô lại quan trọng. Câu hỏi tiếp theo một cách tự nhiên là loại hệ thống nào sẽ khiến cho quy mô đó trở nên khả thi trong thực tế. Một mô tả đặc tính (characterization) chính xác bắt đầu bằng một ví dụ cụ thể.
1.5 Định nghĩa Hệ thống ML
Thay vì bắt đầu với một định nghĩa trừu tượng, hãy xem xét một hệ thống mà hầu hết mọi người tương tác hàng ngày: lọc thư rác email. Một bộ lọc thư rác bảo vệ một hộp thư đến điển hình hoạt động chống lại lưu lượng email toàn cầu được tính bằng hàng trăm tỷ tin nhắn gửi và nhận mỗi ngày (Bộ phận Nghiên cứu Statista 2024), và các nhà cung cấp lớn phải đưa ra quyết định trong vài mili giây để xem tin nhắn nào đáng được chú ý và tin nhắn nào nên bị cách ly (quarantined).
Tác vụ tưởng chừng đơn giản này tiết lộ điều tạo nên sự khác biệt giữa các hệ thống học máy so với phần mềm truyền thống. Thử thách bắt đầu từ dữ liệu: bộ lọc được huấn luyện trên hàng triệu ví dụ có nhãn và phải tiếp tục thích ứng khi những kẻ gửi thư rác liên tục phát triển chiến thuật của chúng, thay vì dựa vào các lập trình viên để mã hóa thủ công từng mẫu thư rác. Sau đó, nó trở thành một vấn đề thuật toán, bởi vì mô hình phải khái quát hóa (generalize) từ những ví dụ đó sang các thông điệp mà nó chưa bao giờ gặp trước đây trong khi cân bằng giữa độ chuẩn xác (precision) và độ phủ (recall) để email hợp pháp không bị ẩn đi. Cuối cùng, cùng một quyết định đó trở thành một vấn đề cơ sở hạ tầng: các nhà cung cấp phải xử lý hàng tỷ email mỗi ngày, lưu trữ và cập nhật các mô hình khi thư rác phát triển, và phục vụ các dự đoán với độ trễ dưới 100 ms trên khắp các trung tâm dữ liệu được mở rộng quy mô theo chiều ngang (horizontally scaled data centers).
Ba mối quan tâm đan xen lẫn nhau này, thu thập và quản lý dữ liệu huấn luyện ở quy mô lớn, triển khai các thuật toán để học hỏi và khái quát hóa một cách hiệu quả, và xây dựng cơ sở hạ tầng hỗ trợ cả việc huấn luyện lẫn dự đoán trong thời gian thực, xuất hiện ở mọi hệ thống học máy. Không một hệ thống phần mềm truyền thống nào có thể hiện cả ba điều này cùng một lúc.
Định nghĩa 1.1: Hệ thống học máy (Machine learning systems)
Các Hệ thống Học máy là những hệ thống phần mềm có hành vi cốt lõi được quyết định bởi các tham số học được từ dữ liệu thay vì các quy tắc lập trình rõ ràng, làm cho hiệu suất trở thành một hàm số (function) phụ thuộc vào chất lượng dữ liệu, lựa chọn thuật toán, và công suất phần cứng cùng một lúc.
1. Ý nghĩa: Mọi ngân sách về hiệu suất (performance budget) đều có thể được truy xuất về ba chi phí vật lý: số byte được di chuyển, khối lượng công việc tính toán được thực hiện, và thời gian chi phí trễ cố định (fixed latency overhead). Trong một hệ thống gợi ý (recommendation system) sản xuất (production) xử lý 10 triệu yêu cầu mỗi ngày, việc giảm bớt lượng byte được di chuyển trên mỗi yêu cầu sẽ cắt giảm tổng


================ PAGE 52 ================

14
1.5 Định nghĩa Hệ thống ML
giảm lượng di chuyển dữ liệu một cách tương ứng, trong khi việc nâng cấp bộ vi xử lý chỉ hỗ trợ cho phần tính toán của yêu cầu. Ràng buộc cốt yếu phải được xác định trước khi bất kỳ khoản đầu tư tối ưu hóa nào mang lại lợi nhuận.
2. Sự Khác biệt (Distinction): Không giống như phần mềm truyền thống, nơi tính đúng đắn chỉ bị suy giảm khi mã nguồn thay đổi, độ chính xác của một hệ thống ML suy giảm khi thế giới thay đổi. Các trọng số của mô hình được cố định sau khi triển khai, nhưng sự phân bố của các đầu vào so với những gì mô hình đã học sẽ liên tục thay đổi, âm thầm làm xói mòn độ chính xác mà không có bất kỳ thông báo lỗi hay ngoại lệ nào.
3. Cạm bẫy Phổ biến (Common pitfall): Một quan niệm sai lầm thường gặp là cho rằng một hệ thống ML chính là mô hình. Phân tích của Google về khoản nợ kỹ thuật (technical debt) trong các hệ thống ML sản xuất (production) đã sử dụng một sơ đồ trong đó mã của mô hình là một hộp nhỏ ở trung tâm, chỉ chiếm khoảng 5 phần trăm sơ đồ, được bao quanh bởi một cơ sở hạ tầng hỗ trợ lớn hơn nhiều; các đường ống dữ liệu, cơ sở hạ tầng phục vụ (serving infrastructure), giám sát, và các mã hỗ trợ khác thường chiếm ưu thế trong gánh nặng kỹ thuật (Sculley et al. 2015).
Định nghĩa này tạo động lực cho Hệ phân loại D·A·M (D·A·M taxonomy), thứ mà giờ đây chúng ta chính thức hóa thành một công cụ chẩn đoán: khi hiệu suất bị đình trệ hoặc hành vi bị suy thoái, bước chẩn đoán đầu tiên là xác định trục ràng buộc (binding axis).
Định nghĩa 1.2: Hệ phân loại D·A·M (D·A·M taxonomy)
Hệ phân loại D·A·M là một khuôn khổ chẩn đoán (diagnostic framework) dùng để phân loại nút thắt cổ chai về hiệu suất của bất kỳ hệ thống học máy nào theo ba trục: Dữ liệu (Data), xác định các ví dụ và byte nào mà hệ thống phải xử lý; Thuật toán (Algorithm), xác định cấu trúc mô hình và khối lượng công việc cần thiết để học hoặc dự đoán; và Máy móc (Machine), xác định công suất phần cứng khả dụng để thực thi công việc đó. Mục tiêu là xác định trục nào là ràng buộc cốt yếu.
1. Ý nghĩa: Sức mạnh chẩn đoán rất cụ thể ngay cả trước khi các phép toán phần cứng chi tiết xuất hiện trong câu chuyện. Nếu bộ lọc thư rác bỏ sót một chiến dịch lừa đảo (phishing) mới vì tập huấn luyện chưa bao giờ chứa chiến thuật đó, trục ràng buộc là Dữ liệu. Nếu các ví dụ huấn luyện là đủ nhưng mô hình không thể biểu diễn khuôn mẫu đó, trục ràng buộc là Thuật toán. Nếu cả hai đều đủ nhưng dịch vụ không thể phân loại tin nhắn đủ nhanh trong thời điểm lưu lượng truy cập tăng vọt, trục ràng buộc là Máy móc. Chẩn đoán định lượng bắt đầu bằng cách hỏi trục nào đang giới hạn hệ thống.
2. Sự Khác biệt: Không giống như phân tích hiệu suất phần mềm truyền thống, nơi coi mã và dữ liệu là những mối quan tâm riêng biệt, hệ phân loại D·A·M nhận ra rằng việc lựa chọn thuật toán trực tiếp quyết định cả quy mô tập dữ liệu huấn luyện cần thiết (một transformer cần dữ liệu nhiều hơn theo cấp số nhân so với một mô hình tuyến tính để có thể khái quát hóa) và cấu hình máy móc cần thiết để chạy nó.
3. Cạm bẫy Phổ biến: Một quan niệm sai lầm thường gặp là ba trục này độc lập với nhau. Việc chuyển từ một bộ phân loại đơn giản sang một mô hình lớn hơn có thể yêu cầu nhiều bộ nhớ hơn, cơ sở hạ tầng phục vụ khác, và phân phối dữ liệu rộng hơn. Các trục này luôn dịch chuyển cùng nhau.
Ba thành phần này có thể được khái niệm hóa thành Dữ liệu (nhiên liệu), Thuật toán (bản thiết kế) và Máy móc (động cơ). Nếu thiếu bất kỳ thành phần nào, các thành phần còn lại chỉ mang tính lý thuyết. Hệ phân loại D·A·M nắm bắt sự phụ thuộc lẫn nhau này một cách trực tiếp; Hình 1.3 cho thấy lý do tại sao ba yếu tố này không thể được thiết kế, hay thậm chí là suy luận, một cách cô lập.
Các mũi tên hai chiều giữa Dữ liệu, Thuật toán, và Máy móc nhấn mạnh rằng không có trục nào có thể được tối ưu hóa một cách riêng biệt. Mỗi yếu tố đều định hình các khả năng của những yếu tố khác. Thuật toán quyết định cả những nhu cầu tính toán cho việc huấn luyện và suy luận lẫn khối lượng và cấu trúc dữ liệu cần thiết để học tập hiệu quả. Quy mô và độ phức tạp của dữ liệu ảnh hưởng đến loại máy móc nào cần thiết để lưu trữ và xử lý, đồng thời quyết định thuật toán nào là khả thi. Năng lực của máy móc thiết lập những giới hạn thực tế cho cả quy mô mô hình và khả năng xử lý dữ liệu, tạo ra một ranh giới mà trong đó các trục khác phải hoạt động.


================ PAGE 53 ================

1. Giới thiệu
15
Thuật toán (Algorithm)
Máy móc (Machine)
Dữ liệu (Data)
Hình 1.3: Hệ phân loại D·A·M: Mối quan hệ phụ thuộc lẫn nhau giữa Dữ liệu, Thuật toán, và Máy móc. Mỗi nút (tập dữ liệu, mô hình, và cơ sở hạ tầng) đều ràng buộc khả năng của các nút khác. Kỹ thuật hệ thống ML là kỷ luật cân bằng ba trục này; việc tối ưu hóa một trục một cách riêng lẻ thường chỉ chuyển dời nút thắt cổ chai hệ thống sang trục khác thay vì loại bỏ nó hoàn toàn.
Kỹ thuật hệ thống ML là kỷ luật giữ cho cả ba trục luôn ở trạng thái cân bằng. Bảng 1.4 chính thức hóa vai trò của từng trục.
Bảng 1.4: Hệ phân loại D·A·M: Mỗi hệ thống ML đều bao gồm ba trục phụ thuộc lẫn nhau này, và việc tối ưu hóa một trục một cách riêng biệt thường chỉ dịch chuyển nút thắt cổ chai sang trục khác chứ không loại bỏ nó. Bước chẩn đoán lặp đi lặp lại trong suốt cuốn sách này là xác định xem trục nào đang là giới hạn trước khi chọn phương pháp tối ưu hóa.
Trục (Axis)
Định nghĩa
Vai trò trong Hệ thống
Dữ liệu (Data)
Thông tin chỉ đạo hành vi
Nhiên liệu: Xác định những gì hệ thống học được
Thuật toán (Algorithm)
Các cấu trúc toán học dùng để học
Bản thiết kế: Xác định cách nắm bắt các mẫu (patterns)
Máy móc (Machine)
Cơ sở hạ tầng phần cứng và phần mềm
Động cơ: Xác định tốc độ và vị trí tính toán
Hệ phân loại D·A·M cung cấp lăng kính chẩn đoán, nhưng để xây dựng các hệ thống, chúng ta phải tổ chức các trục này thành một hệ thống phân cấp có thể tái tạo (reproducible hierarchy): một ngăn xếp (stack) bốn lớp biến đổi các ràng buộc vật lý thô sơ thành các ứng dụng chức năng cho người dùng.
1.5.1 Từ silicon đến sứ mệnh (mission): Hệ thống phân cấp bốn lớp
Mọi hệ thống học máy được phân tích trong cuốn sách này đều được xây dựng từ bốn lớp phân cấp, đảm bảo rằng một quyết định được đưa ra ở cấp độ silicon có thể được truy xuất về tác động của nó đối với sứ mệnh cuối cùng.
1. Phần cứng (The Silicon): Nền tảng vật lý (Động cơ). Lớp này xác định các năng lực thô: thông lượng tính toán đỉnh (𝑅peak), băng thông bộ nhớ (BW), và dung lượng bộ nhớ; các bản sao phần cứng cụ thể (concrete hardware twins) sẽ khởi tạo các đại lượng đó khi các kịch bản triển khai cần đến những ràng buộc bằng số (numeric constraints).
2. Hệ thống (The Platforms): Đơn vị triển khai tích hợp (Chiếc xe). Lớp này xác định "Phạm vi" (Envelope) mà phần cứng hoạt động trong đó: ngân sách điện năng, giới hạn nhiệt, và các kết nối cấp độ nút (node-level interconnects). Các ví dụ bao gồm Nút Cụm Huấn luyện (Training Cluster Node) hoặc Nút Cảm biến Dưới Watt (Sub-Watt Sensor Node).
3. Khối lượng công việc (The Models): Nhu cầu thuật toán (Tuyến đường). Lớp này xác định khối lượng công việc toán học: số lượng phép toán (𝑂), khối lượng dữ liệu được di chuyển (𝐷vol), và bố cục dữ liệu (data layout). Khối lượng công việc đặc thù theo kịch bản (Scenario-specific workloads), chẳng hạn như GPT-4 và Wake Vision, khởi tạo các nhu cầu này cho các nhiệm vụ cụ thể.
4. Sứ mệnh (The Scenarios): Bối cảnh ứng dụng (Đích đến). Đây là đỉnh của ngăn xếp, nơi một hệ thống được triển khai để giải quyết một vấn đề cụ thể. Một sứ mệnh đưa ra các yêu cầu cấp cao, chẳng hạn như thời lượng pin, độ trễ an toàn (safety latency), hoặc trần chi phí đám mây, quy định cấu hình của mọi lớp bên dưới.
Hệ thống phân cấp này đảm bảo rằng khi chúng ta xây dựng một phòng thí nghiệm hoặc một nghiên cứu tình huống (case study), các kỹ sư không bắt đầu từ con số không, mà kế thừa các ràng buộc của một mô hình triển khai và áp dụng một khối lượng công việc tình huống vào một nhiệm vụ cụ thể. Cuộc thảo luận về vòng đời ở phần sau trong chương này ghép nối mỗi nhiệm vụ lặp đi lặp lại với khối lượng công việc và ràng buộc cốt yếu của nó. Cách tiếp cận có cấu trúc này cho phép chúng ta lý luận về "Vật lý của ML" trên bất kỳ lĩnh vực ứng dụng nào.


================ PAGE 54 ================
16
1.5 Định nghĩa Hệ thống ML
Hệ phân loại D·A·M đóng vai trò như một lăng kính chẩn đoán xuyên suốt văn bản này. Mở rộng quy mô (Scale) trong các hệ thống ML là việc không ngừng theo đuổi nút thắt cổ chai liên tục dịch chuyển. Việc giảm bớt một ràng buộc dọc theo một trục thường sẽ chuyển giới hạn sang một trục khác. Việc nâng cấp lên các GPU nhanh hơn (Máy móc) có thể tiết lộ rằng lưu trữ không thể cung cấp dữ liệu đủ nhanh (Dữ liệu). Việc thu thập một tập dữ liệu khổng lồ (Dữ liệu) có thể tiết lộ rằng mô hình thiếu công suất để học từ nó (Thuật toán). Việc chuyển sang một mô hình lớn hơn (Thuật toán) có thể vượt quá bộ nhớ khả dụng (Máy móc). Hiểu được những động lực này là trọng tâm của kỹ thuật hệ thống ML. Phần III chính thức hóa phương pháp chẩn đoán này, và phần A.1 ánh xạ từng trục với ràng buộc vật lý cốt yếu của nó và lộ trình tối ưu hóa đòn bẩy cao (high-leverage optimization pathway), cung cấp cho người đọc một điểm tham chiếu để biết nên can thiệp ở đâu một khi trục thống trị đã được xác định.
Góc nhìn Hệ thống 1.2: Bối cảnh hệ thống ML: Bốn mô hình triển khai
Bối cảnh các hệ thống học máy trải dài khoảng 10⁶ về sức mạnh tính toán và 10⁵ về dung lượng bộ nhớ. Bảng 1.5 đối chiếu các giới hạn (envelopes) về bộ nhớ, tính toán, và điện năng trên Bốn Mô hình Triển khai (Four Deployment Paradigms) định hình các ràng buộc cho mọi chương tiếp theo.
Bảng 1.5: Bốn Mô hình Triển khai: Đại diện cho các phạm vi về bộ nhớ, tính toán, và điện năng cho đám mây (cloud), biên (edge), di động (mobile), và TinyML, cho thấy khoảng cách nhiều bậc (multi-order-of-magnitude span) ngăn cản việc sử dụng lại mô hình đơn giản trên các phân tầng này. Các bản sao phần cứng chính xác và các tính toán tỷ lệ đỉnh sẽ xuất hiện trong các chương về phần cứng.
Mô hình (Paradigm)
Hệ thống Đại diện
Phạm vi Bộ nhớ
Phạm vi Tính toán
Phạm vi Điện năng
Đám mây (Cloud)
Nút bộ tăng tốc trung tâm dữ liệu
Bộ nhớ thiết bị lớn cộng với lưu trữ (≈10¹¹ B)
Phân tầng thông lượng cao nhất (≈10¹⁵ ops/s)
Điện năng do cơ sở vật lý quản lý
Biên (Edge)
Cổng kết nối công nghiệp hoặc Robotics
Bộ nhớ cục bộ theo giới hạn triển khai (≈10¹¹ B)
Ngân sách bộ tăng tốc hoặc CPU cục bộ (≈10¹⁴ ops/s)
Điện năng từ tường, phương tiện, hoặc địa điểm
Di động (Mobile)
Điện thoại thông minh hoặc SoC lớp thiết bị đeo (wearable)
Bộ nhớ ứng dụng chia sẻ (≈10¹⁰ B)
Động cơ nơ-ron, GPU, và CPU cấp điện thoại (≈10¹³ ops/s)
Pin và giới hạn nhiệt
TinyML
Nút vi điều khiển (Microcontroller node)
Bộ nhớ quy mô Kilobyte (≈10⁶ B)
Tính toán cảm biến luôn bật (≈10⁹ ops/s)
Ngân sách pin cấp Milliwatt
Quan sát: Đọc các cột bộ nhớ và tính toán từ Đám mây (Cloud) đến TinyML, các điểm cuối khác biệt nhau 10⁵ về bộ nhớ và 10⁶ về tính toán. Sự phân kỳ này chính là lý do tại sao chúng ta không thể đơn giản là "thu nhỏ" một mô hình đám mây để chạy ở vùng biên (edge); mỗi cấp độ đòi hỏi một sự tái thiết kế cơ bản các trục D·A·M.
Khoảng cách nhiều bậc này trên bốn mô hình triển khai không chỉ đơn thuần là sự hiếu kỳ về mặt kỹ thuật; nó chuyển đổi trực tiếp thành chi phí. Một mô hình vừa vặn thoải mái trong bộ nhớ của bộ tăng tốc trung tâm dữ liệu không thể chạy y nguyên trên một thiết bị vi điều khiển, và việc thu hẹp khoảng cách đó đòi hỏi sự đánh đổi về mặt kỹ thuật ở mọi tầng của hệ phân loại D·A·M. Chất lượng dữ liệu, hiệu quả thuật toán, và khả năng phần cứng tương tác thông qua một ràng buộc kinh tế duy nhất: số lượng mẫu trên mỗi đô la (samples per dollar).
Góc nhìn Hệ thống 1.3: Số lượng mẫu trên mỗi đô la
Hiểu biết sâu sắc về hệ thống: Trong khi các nhà nghiên cứu tối ưu hóa để đạt được độ chính xác, các kỹ sư hệ thống lại tối ưu hóa để đạt được số lượng mẫu trên mỗi đô la. Gọi kích thước mô hình là số lượng tham số, kích thước tập dữ liệu là số lượng mẫu huấn luyện, và hiệu suất phần cứng là thông lượng tính toán trên mỗi đô la (FLOP/s trên mỗi đô la, với FLOP/s được chính thức hóa trong quy luật sắt ở dưới). Chỉ số này hợp nhất ba trục của hệ phân loại D·A·M thành một phương trình ràng buộc duy nhất, được thể hiện trong phương trình 1.2:
Chi phí ∝ Kích thước Mô hình × Kích thước Tập dữ liệu / Hiệu suất Phần cứng
(1.2)


================ PAGE 55 ================

1. Giới thiệu
17
19
Suy luận (Inference): Bắt nguồn từ tiếng Latin inferre ("mang vào" - "to bring in" hoặc "kết luận" - "to conclude"). Trong kỹ thuật ML, suy luận đề cập đến giai đoạn triển khai nơi một mô hình đã được huấn luyện áp dụng các mẫu đã học vào các đầu vào mới (novel inputs). Sự phân biệt về mặt hệ thống rất quan trọng: việc huấn luyện được tối ưu hóa về thông lượng (throughput-optimized - tối đa hóa số mẫu/giây), trong khi suy luận được tối ưu hóa về độ trễ (latency-optimized - tối thiểu hóa số mili giây/dự đoán), và các mục tiêu đối lập này đòi hỏi các cấu hình phần cứng và ngăn xếp phần mềm (software stacks) khác biệt căn bản (xem Chương 13).
• Dữ liệu (Thông tin - Information): Việc cải thiện chất lượng dữ liệu (làm sạch, lọc) làm tăng "giá trị học hỏi" (learning value) của mỗi mẫu, giúp làm giảm tử số một cách hiệu quả.
• Thuật toán (Logic): Cấu trúc mô hình hiệu quả hơn làm giảm thời gian tính toán cho mỗi mẫu, giúp làm giảm tử số.
• Máy móc (Vật lý - Physics): Phần cứng chuyên dụng làm tăng mẫu số, cho phép tính toán được nhiều hơn trên mỗi đô la.
Kỹ thuật hệ thống là nghệ thuật cân bằng phương trình này. Việc tăng 10 phần trăm hiệu suất phần cứng có thể cung cấp thêm khoảng 10 phần trăm dữ liệu hoặc hỗ trợ một mô hình lớn hơn với cùng mức ngân sách, nhưng sự đền đáp về độ chính xác phụ thuộc vào độ co giãn (elasticity) của đường cong học tập (learning-curve) của khối lượng công việc. Nếu lỗi (error) tỷ lệ xấp xỉ 𝐷^(-𝛼) đối với kích thước tập dữ liệu 𝐷, thì lợi ích từ việc có thêm dữ liệu được chi phối bởi 𝛼log(1.1) thay vì bởi một tỷ lệ phần trăm chung (universal percentage). Công việc của kỹ sư là ước tính độ co giãn đó cho hệ thống trong tầm tay và đưa ra quyết định liệu sự đánh đổi đó có khả thi về mặt kinh tế hay không.
Góc nhìn kinh tế này giải thích tại sao các thất bại của ML hiếm khi thuộc về một thành phần: một sự rút ngắn quy trình với dữ liệu, thay đổi mô hình, hoặc nút thắt phần cứng đều có thể biểu hiện thành hành vi bị suy thoái sau khi triển khai.
1.6 ML so với Phần mềm Truyền thống
Hệ phân loại D·A·M tiết lộ những gì hệ thống ML bao gồm: dữ liệu định hướng hành vi, thuật toán trích xuất các mẫu, và máy móc cho phép học tập và suy luận¹⁹. Sự khác biệt quan trọng giữa kỹ thuật hệ thống ML và kỹ thuật phần mềm truyền thống không nằm ở chính các thành phần này mà nằm ở cách các hệ thống kết quả thất bại.
Phần mềm truyền thống biểu hiện các chế độ lỗi rõ ràng (explicit failure modes). Khi mã nguồn bị lỗi, các ứng dụng gặp sự cố (crash), thông báo lỗi được lan truyền, và các hệ thống giám sát sẽ kích hoạt cảnh báo. Phản hồi ngay lập tức này cho phép chẩn đoán và khắc phục nhanh chóng: hệ thống hoạt động đúng hoặc gặp lỗi một cách có thể quan sát được (observably). Các hệ thống học máy hoạt động dưới sự suy thoái thầm lặng (silent degradation): chúng có thể tiếp tục hoạt động trong khi hiệu suất của chúng suy giảm một cách âm thầm, mà không kích hoạt các cơ chế phát hiện lỗi thông thường. Các thuật toán tiếp tục thực thi và các máy móc duy trì việc phục vụ các dự đoán, tuy nhiên hành vi học được ngày càng trở nên kém chính xác hoặc kém phù hợp với bối cảnh hơn.
Hệ thống nhận thức của xe tự hành minh họa sự khác biệt này một cách cụ thể. Phần mềm ô tô truyền thống thể hiện các trạng thái vận hành nhị phân: bộ điều khiển động cơ quản lý quá trình phun nhiên liệu chính xác hoặc kích hoạt các cảnh báo chẩn đoán. Chế độ lỗi vẫn có thể quan sát được thông qua giám sát tiêu chuẩn. Một hệ thống nhận thức dựa trên ML đưa ra một thách thức khác. Độ chính xác của hệ thống trong việc phát hiện người đi bộ có thể giảm từ 95 phần trăm xuống 85 phần trăm trong nhiều tháng do những thay đổi theo mùa, khi các điều kiện ánh sáng khác nhau, kiểu quần áo, hoặc các hiện tượng thời tiết chưa được đại diện đầy đủ trong dữ liệu huấn luyện ảnh hưởng đến hiệu suất của mô hình. Xe vẫn tiếp tục hoạt động, phát hiện thành công phần lớn người đi bộ, tuy nhiên hiệu suất giảm sút tạo ra các rủi ro an toàn chỉ bộc lộ thông qua việc giám sát hệ thống các trường hợp biên (edge cases) và đánh giá toàn diện. Các cơ chế cảnh báo và ghi nhật ký lỗi thông thường vẫn im lặng trong khi hệ thống rõ ràng trở nên kém an toàn hơn.
Mức độ nghiêm trọng của sự suy thoái này mang ý nghĩa quan trọng trong các bối cảnh quan trọng về an toàn (safety-critical contexts). Một mô hình nhận thức chạy ở tần số 10 Hz xử lý 36.000 khung hình trong một giờ. Ngay cả tỷ lệ âm tính giả 0,1 phần trăm cũng sẽ tạo ra hàng chục lần phát hiện bị bỏ sót trước khi cơ chế lọc theo thời gian (temporal filtering), hợp nhất cảm biến (sensor fusion), và các giới hạn phạm vi thiết kế hoạt động làm giảm thiểu rủi ro. Do đó, việc suy giảm 10 điểm phần trăm từ 95 phần trăm xuống 85 phần trăm không chỉ đơn thuần là sự thay đổi về độ chính xác; nó làm thay đổi tỷ lệ phơi nhiễm rủi ro (exposure rate) của logic điều khiển các hệ thống hạ nguồn (downstream) chính xác ở những trường hợp biên nơi mà việc phát hiện vốn dĩ đã có tính giới hạn (marginal).
Sự suy thoái thầm lặng này biểu hiện trên cả ba trục D·A·M. Phân phối dữ liệu dịch chuyển khi thế giới thay đổi: hành vi người dùng tiến hóa, các mẫu (patterns) theo mùa xuất hiện, và các trường hợp biên mới xuất hiện (Gama et al. 2014; Quiñonero-Candela et al. 2009). Trong khi đó, các thuật toán tiếp tục đưa ra dự đoán dựa trên các mẫu học được đã lỗi thời, không nhận thức được rằng phân phối huấn luyện của chúng không còn khớp với thực tế vận hành. Các máy móc trung thành phục vụ những dự đoán ngày càng kém chính xác này trên quy mô lớn, khuếch đại vấn đề đối với từng người dùng và từng truy vấn.
Bởi vì chế độ lỗi này là thầm lặng, không thể dựa vào nhật ký sự cố (crash logs) để phát hiện; các phương pháp tiếp cận toán học phải được sử dụng. Khi các lỗi không tự thông báo, các tín hiệu định lượng


================ PAGE 56 ================

18
1.6 ML so với Phần mềm Truyền thống
Độ chính xác suy giảm thầm lặng dưới tác động của sự trôi dạt.
cần phải kết nối sự dịch chuyển phân phối (distribution shift) có thể đo lường được với sự sụt giảm hiệu suất dự kiến. Bằng cách loại suy với sự phân rã hiệu suất bộ xử lý được giới thiệu ở bên dưới, chúng ta có thể phân rã sự suy thoái của hệ thống ML thành các yếu tố cấu thành. Phương trình suy thoái trong phương trình 1.3 là một xấp xỉ chẩn đoán bậc một (first-order diagnostic approximation), không phải là một định luật dự đoán phổ quát (universal prediction law): nó nắm bắt trường hợp phổ biến khi sự dịch chuyển phân phối càng lớn thì khả năng hiệu suất sụt giảm dự kiến theo thời gian càng cao.
Độ_chính_xác(𝑡) ≈ Độ_chính_xác_0 − 𝜆 ⋅ 𝒟(𝑃_𝑡 ‖ 𝑃_0)
(1.3)
trong đó:
• Độ_chính_xác_0: Độ chính xác ban đầu tại thời điểm triển khai
• 𝒟(𝑃_𝑡 ‖ 𝑃_0): Độ phân kỳ thống kê (Statistical divergence) giữa phân phối dữ liệu hiện tại 𝑃_𝑡 và phân phối huấn luyện 𝑃_0
• 𝜆: Độ nhạy của mô hình với sự dịch chuyển phân phối (phụ thuộc vào kiến trúc)
Phép tuyến tính hóa bậc một (first-order linearization) này nắm bắt xu hướng chủ đạo: độ chính xác bị xói mòn gần như tỷ lệ thuận với mức độ mà phân phối dữ liệu hiện tại đã trôi dạt (drifted) khỏi phân phối huấn luyện. Sự phân kỳ dần dần đó chính là Sự Trôi dạt Dữ liệu (Data Drift): phân phối sản xuất dịch chuyển ra khỏi phân phối mà mô hình đã học, do đó các dự đoán có thể trở nên không đáng tin cậy ngay cả khi mã nguồn không hề thay đổi. Mô hình bị phá vỡ đối với các thay đổi lớn (nơi mối quan hệ trở nên phi tuyến tính) và số đo độ phân kỳ cụ thể 𝒟(⋅‖⋅) được cố ý để ở dạng tổng quát (các lựa chọn phổ biến bao gồm phân kỳ KL, khoảng cách tổng biến thiên - total variation distance, hoặc khoảng cách Wasserstein, mỗi cái có cấu hình độ nhạy khác nhau). Bất chấp những sự đơn giản hóa này, phương trình đã bộc lộ ba đòn bẩy kỹ thuật để quản lý sự suy thoái:
1. Cải thiện độ chính xác ban đầu (Độ_chính_xác_0): Huấn luyện tốt hơn, dữ liệu nhiều hơn, các kiến trúc vượt trội. Điều này làm dịch chuyển đường cong (shifts the curve) nhưng không thay đổi độ dốc của nó.
2. Giảm độ nhạy phân phối (𝜆): Các kỹ thuật huấn luyện mạnh mẽ (robust), thích ứng miền (domain adaptation), các phân phối huấn luyện rộng hơn. Những điều này làm phẳng đường cong suy thoái.
3. Giám sát và phản ứng với sự trôi dạt (𝒟(𝑃_𝑡 ‖ 𝑃_0)): Việc đo lường liên tục độ phân kỳ phân phối cho phép huấn luyện lại chủ động (proactive retraining) trước khi độ chính xác giảm xuống dưới các ngưỡng có thể chấp nhận được.
Ý nghĩa thực tiễn: biết khi nào cần huấn luyện lại cũng quan trọng như việc biết cách huấn luyện. Một hệ thống thực hiện huấn luyện lại khi 𝒟(𝑃_𝑡 ‖ 𝑃_0) > 𝜏 đối với một ngưỡng 𝜏 nào đó sẽ duy trì độ chính xác trong các giới hạn. Một hệ thống không có sự giám sát trôi dạt hoạt động mù quáng (blind) trước sự suy thoái của chính nó. Chúng ta sẽ phát triển cơ sở hạ tầng giám sát và các chiến lược cảnh báo triển khai nguyên tắc này trong Chương 14.
Khuôn khổ này phân biệt kỹ thuật hệ thống ML với kỹ thuật phần mềm truyền thống ở mức độ sâu sắc nhất. Các hệ thống truyền thống không có phương trình tương đương bởi vì chúng không bị trôi dạt: một hàm số tính toán đúng vào ngày hôm qua thì cũng sẽ tính toán đúng vào ngày hôm nay. Các hệ thống ML yêu cầu sự đầu tư liên tục vào cơ sở hạ tầng giám sát mà phần mềm truyền thống chưa bao giờ cần đến, và phương trình suy thoái định lượng được lý do tại sao. Đây là phản hồi kỹ thuật đối với khoảng trống xác minh được xác định trong phương trình 1.1: vì chúng ta không thể kiểm thử triệt để, chúng ta phải giám sát liên tục.
Một hệ thống gợi ý minh họa cho quy luật này: nó có thể mất vài điểm phần trăm dưới sự trôi dạt theo mùa nhẹ hoặc hàng chục điểm dưới sự sai lệch (skew) giữa quá trình huấn luyện-phục vụ nghiêm trọng, với tốc độ phụ thuộc vào độ dịch chuyển phân phối đo được và độ nhạy của mô hình với sự thay đổi đó. Sự suy thoái này thường bắt nguồn từ sự sai lệch huấn luyện-phục vụ (training-serving skew), trong đó các đặc trưng được tính toán khác nhau giữa các đường ống huấn luyện và phục vụ khiến hiệu suất mô hình suy giảm bất chấp việc mã nguồn không bị thay đổi. Đây là một vấn đề của máy móc (machine issue) biểu hiện ra như một thất bại về thuật toán (algorithmic failure).
Sự khác biệt trong các chế độ lỗi đòi hỏi những thực tiễn kỹ thuật (engineering practices) mới. Quá trình phát triển phần mềm truyền thống tập trung vào việc loại bỏ lỗi (bugs) và đảm bảo hành vi tất định, nhưng kỹ thuật hệ thống ML phải bổ sung việc giải quyết các hành vi xác suất, các phân phối dữ liệu không ngừng tiến hóa, và sự suy thoái hiệu suất xảy ra không do những thay đổi về mã. Các hệ thống giám sát phải theo dõi tình trạng sức khỏe cơ sở hạ tầng, hiệu suất mô hình, chất lượng dữ liệu, và phân phối dự đoán một cách đồng thời. Các thực tiễn triển khai phải cho phép cập nhật mô hình liên tục khi các phân phối dữ liệu thay đổi. Toàn bộ vòng đời của hệ thống, từ việc thu thập dữ liệu qua việc huấn luyện mô hình cho đến phục vụ suy luận, đều phải được thiết kế dựa trên tư duy đối phó với sự suy thoái thầm lặng.
Phương trình suy thoái tiết lộ điều gì xảy ra đối với các hệ thống ML: sự suy giảm độ tin cậy thầm lặng vốn không có trong phần mềm truyền thống. Biết rằng một hệ thống sẽ bị suy thoái không giống với việc biết lý do tại sao nó suy thoái hoặc nơi nào cần can thiệp. Để làm được điều đó, chúng ta cần phân rã bản thân hiệu suất thành các đặc điểm vật lý của nó.


================ PAGE 57 ================

1. Giới thiệu
19
20
"Mọi mô hình đều sai, nhưng một số thì hữu ích": Câu châm ngôn của nhà thống kê George Box áp dụng trực tiếp cho quy luật sắt: sự phân rã cộng gộp (additive decomposition) bỏ qua việc tạo đường ống (pipelining), các hiệu ứng phân cấp bộ nhớ, và chi phí liên lạc chìm (communication overhead). Thế nhưng, sự đơn giản hóa có chủ ý này lại chính xác là những gì làm cho nó mang tính chẩn đoán. Những kỹ sư cố gắng lập mô hình cho mọi tương tác trước khi lập hồ sơ (profiling) sẽ không bao giờ ra mắt được sản phẩm (never ship); những kỹ sư xác định được yếu tố nào trong ba yếu tố chiếm ưu thế sẽ ra mắt được các hệ thống hoạt động thực tế.
yếu tố cấu thành. Bài học đắng cay đã thiết lập rằng quy mô tính toán là động lực thúc đẩy sự tiến bộ của AI; câu hỏi bây giờ trở thành làm thế nào để lý luận định lượng về quá trình di chuyển dữ liệu, quá trình tính toán, và những chi phí chìm (overhead) cấu thành nên quy mô đó.
1.7 Quy luật Sắt của các Hệ thống ML (Iron Law of ML Systems)
Một công việc huấn luyện bị đình trệ khi không gian lưu trữ không thể cung cấp đủ cho bộ tăng tốc; một đường dẫn suy luận trễ thời hạn khi trạng thái mô hình (model state) di chuyển quá chậm qua bộ nhớ hoặc qua mạng. Các chế độ lỗi này trông có vẻ khác nhau, nhưng chúng cùng chia sẻ một cấu trúc hiệu suất chung. Hiệu suất của hệ thống học máy bị chi phối bởi Quy luật Sắt của các Hệ thống ML, được chính thức hóa trong phương trình 1.4:
𝑇 = 𝐷_vol / BW + 𝑂 / (𝑅_peak ⋅ 𝜂_hw) + 𝐿_lat
(1.4)
trong đó:
• 𝐷_vol / BW: Yếu tố dữ liệu
• 𝑂 / (𝑅_peak ⋅ 𝜂_hw): Yếu tố tính toán
• 𝐿_lat: Yếu tố độ trễ
Phương trình này là xương sống toán học của cuốn sách này. Nó phân rã tổng thời gian cần thiết cho bất kỳ tác vụ ML nào, dù là huấn luyện một mô hình trong nhiều tuần hay phục vụ một suy luận trong vài mili giây, thành ba yếu tố tương ứng trực tiếp với các ràng buộc vật lý của Nhiệm vụ Kép (Dual Mandate) đã được giới thiệu trước đó:
1. Yếu tố dữ liệu (𝐷_vol / BW): Chi phí vật lý của việc di chuyển các bit. 𝐷_vol là khối lượng dữ liệu được di chuyển (tính bằng byte), và BW là băng thông bộ nhớ hoặc mạng (byte/s). Bất kể là tải hàng terabyte từ bộ nhớ đám mây hay tìm nạp các trọng số từ bộ nhớ băng thông cao, hiệu suất thường bị giới hạn bởi tính chất vật lý của I/O (Input/Output). Vấn đề này được đề cập trong Phần I: Nền tảng (Foundations).
2. Yếu tố tính toán (𝑂 / (𝑅_peak ⋅ 𝜂_hw)): Chi phí của các phép toán số học. 𝑂 là số lượng các phép toán dấu phẩy động (floating-point operations). 𝑅_peak là thông lượng đỉnh theo lý thuyết của phần cứng (FLOP/s). 𝜂_hw là hệ số tận dụng phần cứng (hardware utilization factor) (0 ≤ 𝜂_hw ≤ 1), đại diện cho hiệu suất thực tế. Chúng tôi giải quyết vấn đề này trong Phần II: Xây dựng (Build) và Phần III: Tối ưu hóa (Optimize).
3. Yếu tố độ trễ (𝐿_lat): "Loại thuế" (tax) không thể cắt giảm của quá trình điều phối hệ thống, mạng lưới, và quá trình tuần tự hóa (serialization). Độ trễ cố định này chiếm ưu thế trong quá trình triển khai thời gian thực (real-time deployment). Chúng tôi giải quyết vấn đề này trong Phần IV: Triển khai (Deploy).
Góc nhìn Hệ thống 1.4: Sự tương đồng của quy luật sắt
Chúng ta gọi đây là "quy luật sắt" theo phép so sánh với Quy luật Sắt về Hiệu suất Bộ xử lý của Patterson & Hennessy (Patterson and Hennessy 2017). Tuy nhiên, có những khác biệt quan trọng. Quy luật của P&H là một sự phân rã nhân (multiplicative decomposition) (một điều hiển nhiên phân tích thời gian CPU), trong khi phương trình của chúng ta là một mô hình bậc một cộng gộp (additive first-order model) mô phỏng hiệu suất theo các giả định đơn giản hóa. Dạng cộng giả định việc thực thi tuần tự (sequential execution); trong thực tế, các hệ thống có thể cho các yếu tố này chồng lấp lên nhau, biến tổng (sum) thành tối đa (max) như phương trình 1.5 cho thấy:
𝑇_pipelined = max(𝐷_vol / BW, 𝑂 / (𝑅_peak ⋅ 𝜂_hw)) + 𝐿_lat
(1.5)
Chúng tôi giữ lại "quy luật sắt" bởi vì, giống như Định luật Amdahl (Amdahl 1967), giá trị của nó nằm ở sức mạnh chẩn đoán: xác định ràng buộc vật lý nào đang chiếm ưu thế trước khi tiến hành tối ưu hóa. Quy luật sắt rất hữu ích chính xác vì nó đơn giản hóa sự phức tạp của toàn bộ ngăn xếp thành ba yếu tố có thể quản lý được. Phụ lục A trình bày cách xử lý tinh chỉnh hơn, bao gồm các kỹ thuật tạo đường ống và chồng lấp biến mô hình cộng (additive model) thành dạng công thức dựa trên hàm max (max-based formulation) được sử dụng trong thực tế.
Như George Box đã nói một câu nổi tiếng: "Mọi mô hình đều sai, nhưng một số thì hữu ích" (Box 1976).²⁰ Phần D.2.1 phát triển cách xử lý toán học sâu sắc hơn, bao gồm điểm gợn (ridge point) giúp sự đánh đổi giữa dữ liệu/tính toán có thể đo lường được: bên dưới điểm gợn, sự di chuyển dữ liệu chiếm ưu thế; bên trên nó, thông lượng số học chiếm ưu thế. Xuyên suốt cuốn sách này, mọi kỹ thuật tối ưu hóa mà chúng ta nghiên cứu đều là một phương pháp để thao tác một trong những biến số này: di chuyển ít dữ liệu hơn, làm ít công việc hơn, sử dụng máy móc hiệu quả hơn, hoặc giảm độ trễ của quá trình điều phối. Một ước tính huấn luyện đẳng cấp GPT-3 làm cho sự thao tác đó trở nên cụ thể bằng cách chỉ ra một sự thay đổi về hiệu suất truyền (propagates) qua quy luật sắt như thế nào.


================ PAGE 58 ================

20
1.7 Quy luật Sắt của các Hệ thống ML
Việc di chuyển một byte tiêu tốn năng lượng gấp khoảng 145 lần so với một phép toán FP16, một khoản thuế di chuyển dữ liệu (data-movement tax).
Toán học Khái lược (Napkin Math) 1.1: Huấn luyện GPT-3
Vấn đề: Thời gian huấn luyện cho một mô hình thuộc lớp GPT-3 trên một cụm gồm 1024 bộ tăng tốc được xây dựng từ các bộ tăng tốc tham chiếu là bao lâu?
Cho trước:
• Các phép toán (𝑂): ≈ 3.14 × 10²³ FLOPs
• Đỉnh (𝑅_peak): 312 TFLOP/s
• Hiệu suất (𝜂_hw): ≈ 45 phần trăm (điển hình cho huấn luyện phân tán quy mô lớn)
• Quy mô (𝑁_accel): 1024 bộ tăng tốc
Toán học:
• 𝑇_train ≈ 𝑂 / (𝑁_accel ⋅ 𝑅_peak ⋅ 𝜂_hw) ≈ 3.14 × 10²³ / (1024 × 312 × 10¹² × 0.45) ≈ 25 ngày
Kết quả: 25 ngày.
Hiểu biết sâu sắc về hệ thống: Nếu chúng ta cải thiện việc tận dụng phần cứng (𝜂_hw) từ 45 phần trăm lên 60 phần trăm thông qua việc lập lịch biểu tốt hơn (better scheduling) và thực thi hiệu quả hơn, thời gian huấn luyện sẽ giảm xuống còn 19 ngày, tiết kiệm được gần 6 ngày cho thời gian tính toán đắt đỏ.
Phương trình này nhất quán về mặt thứ nguyên (dimensionally consistent): mỗi thành phần (term) đều được giải quyết thành số giây. Một người không thể cộng thêm số lượng FLOP vào số byte cũng như không thể cộng thêm số mét vào số kilogam; quy luật sắt cộng thời gian với thời gian và với thời gian. Phần D.2.2 cung cấp một phân tích thứ nguyên chính thức xác minh tính nhất quán này và chứng minh cách việc theo dõi đơn vị (unit tracking) ngăn chặn các lỗi mô hình hóa phổ biến.
Quy luật sắt chi phối thời gian, nhưng thời gian không phải là ràng buộc duy nhất. Đối với các thiết bị di động, hệ thống biên (edge systems), và các cụm huấn luyện quy mô lớn, năng lượng thường quan trọng hơn tốc độ thô.
Cũng giống như thời gian bị chi phối bởi vật lý, năng lượng cũng vậy. Chúng ta phải thêm một yếu tố thứ tư vào mô hình tư duy của mình: thuế năng lượng (energy tax). Trong nhiều hệ thống hiện đại (di động, biên, và huấn luyện quy mô lớn), năng lượng, chứ không phải thời gian, mới là giới hạn cứng (hard constraint). Gọi 𝐷_vol là tổng lượng dữ liệu di chuyển (bytes), 𝐸_move là năng lượng trên mỗi byte được di chuyển, 𝑂 là tổng số lượng phép toán, và 𝐸_compute là năng lượng trên mỗi phép toán. Phương trình 1.6 chính thức hóa mối quan hệ này, tuân theo quan sát năng lượng-phần cứng rằng việc di chuyển dữ liệu có thể lấn át năng lượng tính toán (Horowitz 2014):
𝐸_total ≈ 𝐷_vol × 𝐸_move (Thành phần chủ đạo) + 𝑂 × 𝐸_compute (Thành phần phụ)
(1.6)
Thành phần chủ đạo là sự di chuyển dữ liệu: 𝐸_move ≫ 𝐸_compute. Dưới các hằng số năng lượng được sử dụng trong tài liệu này, việc di chuyển một byte từ DRAM ngoài chip (off-chip DRAM) tiêu tốn gấp khoảng 145.5 lần một phép toán FP16 và gấp khoảng 800 lần một phép toán INT8 (Horowitz 2014). Tỷ lệ chính xác phụ thuộc vào độ chính xác và mức độ phân cấp của bộ nhớ, nhưng kết luận vẫn ổn định: di chuyển dữ liệu qua các tầng bậc của bộ nhớ tốn năng lượng nhiều hơn gấp nhiều cấp số nhân (orders of magnitude) so với các phép toán số học. Nguyên nhân vật lý là do sự di chuyển dữ liệu đòi hỏi việc nạp và xả (charging and discharging) các dây dẫn trên một khoảng cách vĩ mô (macroscopic distances), trong khi tính toán số học được thực hiện cục bộ trong các mạch điện của đơn vị xử lý. Do đó, giảm thiểu sự di chuyển dữ liệu (𝐷_vol) là đòn bẩy chính cho cả tốc độ và hiệu suất năng lượng.
Điểm kiểm tra 1.2: Quy luật sắt
Quy luật sắt (𝑇 ≈ 𝐷_vol / BW + 𝑂 / (𝑅_peak ⋅ 𝜂_hw) + 𝐿_lat) là xương sống phân tích của cuốn sách này. Trước khi tiếp tục, hãy xác minh bạn có thể thao tác các yếu tố của nó:
□Yếu tố dữ liệu (𝐷_vol / BW): Xác định tài nguyên vật lý giới hạn yếu tố này và gọi tên một chế độ khối lượng công việc (workload regime) mà tại đó yếu tố này chiếm ưu thế.
□Yếu tố tính toán (𝑂 / (𝑅_peak ⋅ 𝜂_hw)): Xác định đại lượng phần cứng và hệ số tận dụng giới hạn yếu tố này.


================ PAGE 59 ================

1. Giới thiệu
21
□Yếu tố độ trễ (𝐿_lat): Xác định những chi phí nào còn lại sau khi sự di chuyển dữ liệu và số học đã được tối ưu hóa.
Tự kiểm tra (Self-test): Nếu bạn tăng gấp đôi tốc độ bộ xử lý (𝑅_peak), yếu tố nào được cải thiện?
Những thành phần quyết định thời gian và năng lượng cũng chính là những thành phần quyết định chi phí: mỗi byte được di chuyển, mỗi phép toán được thực thi, và mỗi mili giây độ trễ đều tiêu tốn ngân sách cơ sở hạ tầng. Do đó, bài kiểm tra tiếp theo mang tính kinh tế, đặt câu hỏi liệu việc bổ sung tính toán có đem lại đủ sự cải thiện cho mô hình để biện minh cho các nguồn lực mà nó tiêu thụ hay không.
1.7.1 Bất biến kinh tế: Lợi tức trên tính toán (Return on compute - RoC)
Sự phân rã thời gian cũng là một ràng buộc kinh tế. Theo truyền thống của Hennessy & Patterson về lập luận định lượng, lợi tức trên tính toán (RoC) được định nghĩa là mức tăng độ chính xác biên (marginal accuracy gain) trên mỗi đô la đầu tư vào cơ sở hạ tầng.
RoC = ΔĐộ_chính_xác / ΔChi_phí_tính_toán
Bất biến này phơi bày một ranh giới kinh tế: việc đạt được 1 phần trăm lợi ích về độ chính xác có thể thất bại trong bài kiểm tra RoC nếu nó yêu cầu tăng gấp 10 lần 𝑂 (Tổng số phép toán). Mọi tối ưu hóa trong các chương tiếp theo đều nhắm vào tử số (trích xuất nhiều tín hiệu hơn từ cùng một dữ liệu) hoặc mẫu số (giảm chi phí thực thi toán học). Nếu RoC bằng 0 hoặc âm, hệ thống đang bị thiết kế quá mức (over-engineered), bất kể sự tinh vi về mặt kỹ thuật của nó. Lăng kính kinh tế này biến "độ chính xác" từ một mục tiêu nghiên cứu thành một ngân sách kỹ thuật.
Nếu quy mô là đòn bẩy tối thượng cho hiệu suất, nó cũng là kẻ tiêu thụ tài nguyên tối thượng. Bài học đắng cay dạy rằng quy mô hoạt động hiệu quả, nhưng quy luật sắt dạy chúng ta làm thế nào để chi trả cho nó. Sự căng thẳng giữa việc mở rộng quy mô (scaling) và tính bền vững (sustainability) định hình các nguyên tắc kỹ thuật tiếp theo.
1.7.2 Các mô hình ngọn hải đăng (Lighthouse models): Quy luật sắt trong thực tiễn
Quy luật sắt làm được nhiều việc hơn là chẩn đoán các nút thắt cổ chai; nó tổ chức toàn bộ chuyên ngành. Mỗi thành phần trong phương trình tương ứng với một mệnh lệnh kỹ thuật cốt lõi. Yếu tố dữ liệu đòi hỏi chúng ta phải xây dựng các đường ống dữ liệu (data pipelines) và cơ sở hạ tầng mạnh mẽ (Chương 4). Yếu tố tính toán yêu cầu chúng ta phải tối ưu hóa thuật toán và việc sử dụng phần cứng để đạt hiệu suất cao (Phần III). Yếu tố độ trễ đòi hỏi chúng ta phải triển khai và vận hành các hệ thống một cách đáng tin cậy trong môi trường sản xuất (Chương 13, Chương 14). Ba mệnh lệnh này cấu trúc nên cuốn giáo trình này: Phần I và II đề cập đến việc xây dựng, Phần III đề cập đến việc tối ưu hóa, và Phần IV đề cập đến việc triển khai và vận hành.
Các phương trình trừu tượng trở nên cụ thể thông qua các khối lượng công việc cụ thể. Cuốn giáo trình này sử dụng năm Mô hình Ngọn hải đăng lặp đi lặp lại như là các công cụ chẩn đoán cho quy luật sắt. Các khối lượng công việc kinh điển này xuất hiện trở lại ở các chương để kiểm tra xem cùng một ràng buộc vật lý có tác động như thế nào đến các mô hình kiến trúc khác nhau.
Mỗi mô hình ngọn hải đăng đại diện cho một trường hợp ứng suất (stress case) riêng biệt đối với quy luật sắt. Ví dụ, ResNet-50 cho phép chúng ta khảo sát thông lượng tính toán khi một hệ thống liên tục tái sử dụng (reuses) các tham số đã học được giống nhau, trong khi GPT-2/Llama hoạt động như một công cụ thăm dò chính của chúng ta về áp lực băng thông bộ nhớ trong quá trình tạo ngôn ngữ (language generation). Đối với các mô hình ngôn ngữ, giải mã tự hồi quy (autoregressive decode) có nghĩa là tạo ra từng token một; bộ đệm KV (KV cache) là trạng thái chú ý (attention state) được lưu lại từ các token trước đó (Chương 6 giới thiệu toàn bộ cơ chế chú ý), và quá trình làm đầy trước (prefill) là lượt (pass) ban đầu xử lý câu lệnh (prompt) trước khi việc tạo ra từng token bắt đầu. Chẩn đoán đó là đặc thù theo chế độ (regime-specific): việc giải mã lô nhỏ (small-batch decode) thường truyền (streams) các trọng số và trạng thái bộ đệm KV đủ nhanh để làm phơi bày băng thông bộ nhớ, trong khi quá trình làm đầy trước (prefill) và phục vụ lô lớn (high-batch serving) có thể làm dịch chuyển nút thắt cổ chai về phía số học hoặc giao tiếp. Bằng cách theo dõi những khối lượng công việc giống nhau này từ kỹ thuật dữ liệu cho đến triển khai tại biên (edge deployment), mỗi chương trình bày cách thức một lựa chọn kiến trúc đơn lẻ lan truyền (propagates) các ràng buộc vật lý và kinh tế trên toàn bộ hệ thống.
Quy luật sắt làm cho những khác biệt này trở nên chính xác. ResNet-50 áp dụng cùng các bộ lọc trọng số nhỏ trên nhiều vị trí không gian (spatial positions) và, dưới việc phân lô (batching), trên nhiều đầu vào; việc tái sử dụng đó có thể khiến 𝑂 / (𝑅_peak ⋅ 𝜂_hw) trở thành yếu tố chiếm ưu thế bởi vì bộ xử lý phải duy trì một thông lượng số học khổng lồ trong khi dấu vết dữ liệu (data footprint) vẫn ở mức khiêm tốn. Ngược lại, GPT-2 tải hàng tỷ tham số trọng số duy nhất cho


================ PAGE 60 ================

22
1.8 Khuôn khổ Hiệu quả (Efficiency Framework)
Giải mã GPT-2 bị giới hạn băng thông: yếu tố dữ liệu chiếm ưu thế.
21
ImageNet: Tập dữ liệu năm 2009 chứng minh rằng quy mô dữ liệu là thành phần còn thiếu trong thị giác máy tính. Fei-Fei Li đã điều động 49.000 công nhân trên Mechanical Turk để gán nhãn cho 14,2 triệu hình ảnh thuộc 21.841 danh mục; tập huấn luyện phân chia của cuộc thi năm 2012 mà AlexNet sử dụng chứa khoảng 1,3 triệu hình ảnh được gán nhãn. Hoạt động kỹ thuật dữ liệu này đã làm lu mờ sự mới lạ về thuật toán của mọi thứ mà nó cho phép sau đó, bao gồm cả bước đột phá năm 2012 của AlexNet (xem Chương 4).
mỗi token mà nó tạo ra, và mỗi trọng số chỉ được sử dụng một lần trước khi trọng số tiếp theo phải được tìm nạp (fetched); thành phần 𝐷_vol / BW của nó chiếm ưu thế bởi vì băng thông bộ nhớ, chứ không phải toán học, là ràng buộc cốt yếu.
Cùng một phương trình đó, khi áp dụng cho hai khối lượng công việc khác nhau, lại mang đến các chẩn đoán khác nhau và do đó các chiến lược tối ưu hóa cũng khác nhau: việc tăng gấp đôi 𝑅_peak sẽ giúp ích cho mô hình ResNet-50 được phân lô một khi sự tái sử dụng (reuse) làm tăng khối lượng tính toán trên mỗi byte được di chuyển, nhưng gần như không ảnh hưởng gì đến quá trình giải mã của GPT-2; việc tăng gấp đôi BW lại có tác dụng ngược lại đối với quá trình giải mã bị giới hạn băng thông (bandwidth-bound decode). Bảng 1.6 tóm tắt lý do tại sao mỗi mô hình ngọn hải đăng đóng vai trò như một công cụ chẩn đoán cho một nút thắt cổ chai cụ thể.
Bảng 1.6: Các Mô hình Ngọn hải đăng dưới dạng Khối lượng Công việc Tham chiếu: Mỗi khối lượng công việc cô lập một nút thắt cổ chai riêng biệt, cho phép khảo sát có hệ thống về cách thức các ràng buộc của hệ thống ảnh hưởng đến các mô hình kiến trúc khác nhau. Các thông số định lượng và chi tiết kiến trúc xuất hiện trong Chương 6.
Mô hình Ngọn hải đăng
Nút thắt cổ chai Hệ thống
Những gì nó tiết lộ
Các Câu hỏi Kỹ thuật Chính
ResNet-50
Thông lượng tính toán dưới sự tái sử dụng
Tận dụng GPU, phân lô
Phần cứng của tôi đang thực hiện tính toán hay đang chờ dữ liệu?
GPT-2/Llama
Băng thông bộ nhớ
Sự di chuyển trọng số và trạng thái chuỗi (sequence-state)
Tôi có thể di chuyển trạng thái mô hình đến bộ xử lý nhanh đến mức nào?
Mô hình Khuyến nghị Học Sâu (DLRM)
Dung lượng bộ nhớ
Bảng nhúng (Embedding tables), mở rộng quy mô (scale-out)
Làm thế nào để tôi vừa khít các mô hình quy mô terabyte vào bộ nhớ?
MobileNetV2
Độ trễ và điện năng
Thiết kế toán tử (operator) hiệu quả
Tôi có thể đáp ứng các ràng buộc thời gian thực trên pin không?
Nhận diện Từ khóa (Keyword Spotting)
Phạm vi điện năng (Power envelope)
Bộ nhớ nhỏ bé và ngân sách năng lượng
Tôi có thể chạy suy luận luôn-bật (always-on) trên milliwatt không?
Mỗi mô hình ngọn hải đăng bộc lộ những ràng buộc khác nhau dọc theo các trục D·A·M, đảm bảo rằng các nguyên tắc được phát triển xuyên suốt văn bản này được thử nghiệm với sự đa dạng của các thách thức kỹ thuật hệ thống thế giới thực. Việc phân công lao động giữa các ví dụ lặp đi lặp lại của cuốn sách là có chủ đích: bốn mô hình triển khai ấn định giới hạn (envelope) mà một hệ thống phải hoạt động bên trong, năm Mô hình Ngọn hải đăng cung cấp khối lượng công việc gây áp lực cho giới hạn đó, và sau đó trong chương này, bốn nhiệm vụ kỹ thuật và ba nghiên cứu tình huống sản xuất (Waymo, FarmBeats, và AlphaFold) ghép nối giới hạn với khối lượng công việc dưới các ràng buộc của thế giới thực.
Cách đọc chẩn đoán tương tự cũng áp dụng hồi cứu cho bước đột phá đã khởi động kỷ nguyên học sâu. Sự chiến thắng của AlexNet được theo dõi trong phần 1.3.3 là một sự điều chỉnh (alignment) D·A·M: việc giảm thiểu lỗi đến không chỉ từ sự mới lạ về thuật toán mà từ các phép toán ma trận song song của mạng nơ-ron tích chập khớp với các khả năng của GPU, được huấn luyện trên kho ngữ liệu được gán nhãn chưa từng có của ImageNet²¹ (Deng et al. 2009).
Sự phụ thuộc lẫn nhau này có nghĩa là việc tối ưu hóa một thành phần thường đẩy áp lực sang thành phần khác. Thành công trong quá trình thiết kế đồng bộ (co-design) của AlexNet có mức giá phải chăng vào năm 2012 (hai GPU tiêu dùng trong một tuần), nhưng các mô hình hiện đại lại đòi hỏi tài nguyên lớn hơn khoảng 7 cấp số nhân. Nếu quy luật sắt chi phối việc một hệ thống chạy nhanh như thế nào, chúng ta vẫn cần một khuôn khổ để lý luận về việc nó sử dụng những tài nguyên đó hiệu quả ra sao.
1.8 Khuôn khổ Hiệu quả (Efficiency Framework)
Bài học đắng cay thiết lập rằng quy mô thúc đẩy tiến bộ AI, nhưng nó cũng tạo ra một nghịch lý: nếu việc thúc đẩy AI đòi hỏi những tập dữ liệu và ngân sách tính toán ngày càng lớn, sự tham gia sẽ thu hẹp lại chỉ còn những tổ chức giàu tài nguyên nhất. Ngay cả những tổ chức đó cũng phải đối mặt với các giới hạn vật lý về ràng buộc năng lượng của trung tâm dữ liệu, nút thắt băng thông bộ nhớ, và lợi suất giảm dần của việc thêm nhiều tham số.
Những ước tính công khai phổ biến cho quá trình huấn luyện mô hình cấp độ GPT-4 đặt ngân sách tính toán vào khoảng 2.5 triệu ngày-bộ tăng tốc (accelerator-days), tương đương hàng triệu đô la chi phí tính toán và tác động đáng kể đến môi trường. Nhiều viện nghiên cứu và công ty không có đủ khả năng cạnh tranh thông qua mở rộng quy mô bằng vũ lực (brute-force scaling). Thực tế thúc đẩy một cách tiếp cận bổ sung: thay vì chỉ tập trung vào việc áp dụng nhiều tính toán hơn, lĩnh vực này cũng phải giải quyết việc tận dụng các sức mạnh tính toán hiện tại sao cho hiệu quả.
Hiệu quả (Efficiency) là một chẩn đoán nút thắt cổ chai, không phải là một kỹ thuật duy nhất. Ba chiều hướng bổ sung ánh xạ trực tiếp tới hệ phân loại D·A·M của chúng ta (bảng 1.4), và mỗi chiều hướng làm thay đổi một thành phần khác nhau trong ngân sách tài nguyên.
Hiệu quả thuật toán (Algorithmic efficiency), giới hạn sớm nhất, làm giảm các yêu cầu tính toán thông qua quy trình huấn luyện và thiết kế mô hình tốt hơn. Mục tiêu của nó là tạo ra hành vi hữu ích hơn trên mỗi phép tính,


================ PAGE 61 ================

1. Giới thiệu
23
22
Định luật Moore: Quan sát năm 1965 của Gordon Moore đã mô tả sự gia tăng nhanh chóng số lượng linh kiện có thể được tích hợp một cách kinh tế trên một con chip (Moore 1998); các bản tóm tắt ngành sau này thường thể hiện nhịp độ này như một sự nhân đôi khoảng hai năm một lần. Qua cùng khung thời gian 2012–2019, nhịp độ nhân đôi hai năm tạo ra khả năng mở rộng bóng bán dẫn (transistor scaling) gấp khoảng 11.3 lần, nghĩa là sự đổi mới thuật toán đã thu hẹp khoảng trống hiệu suất nhiều hơn so với chỉ riêng phần cứng. Đồng thời, nhu cầu về khả năng tính toán huấn luyện tăng gấp đôi mỗi 3.4 tháng, nhanh hơn khoảng 7.1 lần so với nhịp độ hai năm của phần cứng, buộc phải chuyển sang các bộ tăng tốc chuyên biệt theo lĩnh vực (domain-specific accelerators).
để khả năng năng lực (capability) tăng lên mà không cần phải gia tăng tỷ lệ thuận mọi tài nguyên. Khi các thuật toán đòi hỏi ngày càng nhiều tính toán, hiệu quả tính toán (compute efficiency) trở thành chiều hướng quan trọng thứ hai. Nó tối đa hóa sự tận dụng phần cứng bằng cách căn chỉnh (aligning) logic thuật toán với tính chất vật lý của máy móc, biến năng lực bộ xử lý theo lý thuyết thành khối lượng công việc hữu ích. Gần đây nhất, việc lựa chọn dữ liệu (data selection) nổi lên như chiều hướng thứ ba, trích xuất nhiều tín hiệu học tập (learning signal) hơn từ các ví dụ hạn chế, và qua đó giảm thiểu thành phần tổng số phép toán 𝑂 của quy luật sắt. Dòng thời gian trong hình 1.4 đặt ba chiều hướng này trên cùng một trục để thứ tự lịch sử của các nút thắt cổ chai được hiển thị trước khi chuỗi các chương giới thiệu chúng theo trình tự xây dựng. Cùng với nhau, ba chiều hướng này cung cấp các công cụ kỹ thuật để vượt qua các bức tường Dữ liệu, Thuật toán, và Máy móc mà việc chỉ mở rộng quy mô đơn thuần không thể giải quyết được.
1980
Kỷ nguyên Tiền-Học máy
Hiệu suất Thuật toán (Algorithmic Efficiency)
Kỷ nguyên Học Sâu
2010
Hiệu suất Thuật toán Hiện đại
2023
Tương lai
Tính toán Đa dụng
1980
Hiệu suất Tính toán (Compute Efficiency)
Tính toán Tăng tốc (Accelerated Computing)
2010
2022
Tính toán Bền vững
Tương lai
Sự Khan hiếm Dữ liệu
Lựa chọn Dữ liệu (Data Selection)
Kỷ nguyên Dữ liệu Lớn (Big Data)
1980
2010
2022
AI Lấy Dữ liệu Làm Trung tâm (Data-Centric AI)
Tương lai
Hình 1.4: Các Xu hướng Hiệu suất Lịch sử: Một dòng thời gian được nhóm lại từ 1980 đến 2023 tóm tắt tiến trình về Hiệu suất Thuật toán (màu xanh lam), Hiệu suất Tính toán (màu vàng), và Lựa chọn Dữ liệu (màu xanh lá). Mỗi nhóm tiến triển qua các kỷ nguyên riêng biệt: các thuật toán tiến lên từ các phương pháp ban đầu qua học sâu đến các kỹ thuật hiệu suất hiện đại; sức mạnh tính toán phát triển từ CPU đa dụng qua phần cứng tăng tốc đến tính toán bền vững; thực tiễn dữ liệu chuyển từ sự khan hiếm qua dữ liệu lớn sang AI lấy dữ liệu làm trung tâm.
Ba chiều hướng này không nổi lên cùng một lúc; mỗi chiều hướng tiến triển qua các kỷ nguyên khác nhau với những tốc độ khác nhau. Hiệu suất thuật toán đi tiên phong, hiệu suất tính toán theo sau khi nhu cầu tăng trưởng, và các phương pháp lấy dữ liệu làm trung tâm trưởng thành gần đây nhất. Mặc dù lịch sử đã đi từ các bước đột phá về thuật toán đến tăng tốc phần cứng, và sau đó đến các phương pháp tiếp cận lấy dữ liệu làm trung tâm, Phần III của cuốn sách này đảo ngược trình tự đó: chúng ta bắt đầu với việc lựa chọn dữ liệu, sau đó là nén mô hình, và cuối cùng là tăng tốc phần cứng. Thứ tự sư phạm (pedagogical order) này phản ánh cách thức những người thực hành (practitioners) thực sự xây dựng các hệ thống: dữ liệu chất lượng là điều kiện tiên quyết để tối ưu hóa mô hình một cách hiệu quả, và việc hiểu mô hình là điều kiện tiên quyết để ánh xạ nó một cách hiệu quả lên phần cứng.
Quỹ đạo cấp độ kiến trúc trong hình 1.5 làm cho khía cạnh thuật toán của khoảng trống này bộc lộ rõ qua từng mô hình (model by model), chứ không chỉ là một tuyên bố mở rộng quy mô tổng hợp (aggregate scaling claim).
Độ lớn của những cải thiện về hiệu suất có thể đo lường được. Từ năm 2012 đến 2019, nguồn lực tính toán cần thiết để huấn luyện một mạng nơ-ron nhằm đạt được hiệu suất cấp độ AlexNet trên hệ thống phân loại ImageNet đã giảm khoảng 44.5 lần (Hernandez and Brown 2020). Sự cải thiện này, giảm một nửa cứ sau khoảng 15 tháng, đã vượt xa tốc độ cải thiện hiệu suất phần cứng mà Định luật Moore²² dự đoán, chứng minh rằng sự đổi mới thuật toán thúc đẩy hiệu suất nhiều không kém gì những tiến bộ về phần cứng. Đồng thời, sức mạnh tính toán huấn luyện tổng hợp trong các đợt chạy hàng đầu được công bố đã đi theo một nhịp độ dốc hơn nhiều so với Định luật Moore, với thời gian nhân đôi phù hợp là khoảng 3.4 tháng (Amodei and Hernandez 2018b). Xu hướng công bố tổng hợp đó không cùng số lượng với tỷ lệ điểm cuối (endpoint ratio) giữa hai mô hình cột mốc, nhưng nó giải thích tại sao tối ưu hóa hiệu quả không phải là một lựa chọn (optional). Nếu không có nó, chỉ những tổ chức giàu tài nguyên nhất mới có thể tham gia vào phát triển AI.
Những phép đo này xuất hiện từ phương pháp luận thực nghiệm (empirical methodology) nghiêm ngặt đã theo dõi sức mạnh tính toán huấn luyện trên hàng trăm mô hình được công bố; Chương 12 phát triển các khuôn khổ đo lường (measurement frameworks) cho phép sự phân tích có hệ thống như vậy đối với hiệu suất của hệ thống ML. Hai nhịp độ vừa được so sánh định nghĩa khoảng trống hệ thống (systems gap): khoảng cách ngày càng nới rộng giữa những gì mô hình yêu cầu (tính toán tăng gấp đôi mỗi 3.4 tháng) và những gì phần cứng cung cấp (mật độ bóng bán dẫn tăng gấp đôi khoảng hai năm một lần). Thu hẹp khoảng trống đó là mục tiêu chính của cuốn giáo trình này, đòi hỏi kiến thức chuyên môn tích hợp (integrated expertise) trên toàn bộ ngăn xếp phần mềm và phần cứng; Chương 11 sẽ định lượng điều này một cách trực tiếp.
Hình 1.5 theo dõi quỹ đạo này theo từng kiến trúc: VGG, ResNet, MobileNet, và EfficientNet, mỗi cái đều đạt được độ chính xác tương đương với tài nguyên tính toán giảm dần. Các kiến trúc ImageNet ra đời sau được hiển thị nhằm cung cấp bối cảnh trực quan cho điểm chuẩn hoàn thiện (mature benchmark), nhưng tuyên bố hiệu suất thực nghiệm được trích dẫn là quỹ đạo từ năm 2012–2019.


================ PAGE 62 ================

24
1.8 Khuôn khổ Hiệu quả
Hệ số Hiệu suất (Tương đối so với AlexNet)
AlexNet
Xu hướng hàm mũ (~Nhân đôi mỗi 16 tháng)
Hình 1.5: Quỹ đạo Hiệu suất Thuật toán: Hệ số hiệu suất huấn luyện tương đối so với AlexNet (đường cơ sở năm 2012) cho phân loại ImageNet. Hầu hết các kiến trúc sau này đạt được độ chính xác tương đương với ít tài nguyên tính toán hơn, mặc dù các điểm cá biệt có sự biến đổi. Quỹ đạo từ AlexNet (1×) qua VGG, ResNet, MobileNet, và ShuffleNet đến EfficientNet (44×) chứng minh sự sụt giảm 44 lần lượng tính toán cần thiết trong suốt 7 năm, độc lập với những cải tiến về phần cứng (Hernandez and Brown 2020). Các điểm vào đầu những năm 2020 được tác giả đưa vào để cung cấp thêm bối cảnh thay vì dùng làm bằng chứng để kéo dài xu hướng Hernandez-Brown.
Tuy nhiên, mức tăng hiệu quả mới chỉ kể được một nửa câu chuyện. Hình 1.6 so sánh các ước tính điểm cuối (endpoint estimates) minh họa cho quá trình huấn luyện ở kỷ nguyên AlexNet và lớp GPT-4—một hình ảnh trực quan về quy mô, khác biệt với xu hướng nhân đôi tổng hợp sau mỗi 3.4 tháng được trích dẫn ở trên—thế nhưng khoảng cách đó vẫn tiếp tục phát triển theo cấp số nhân, khiến việc tối ưu hóa hiệu quả không còn là một sự xa xỉ mà là một điều kiện tất yếu (necessity) để tiếp tục tiến bộ.
10²⁶
10²⁵
10²⁴
10²³
10²²
10²¹
10²⁰
10¹⁹
10¹⁸
2012
2014
2016
2018
Năm (Year)
2020
2022
2024
Tính toán Huấn luyện (FLOPs)
AlexNet
AlphaGoZero
GPT-3
PaLM
GPT-4-class
Grok-3
Học Sâu (Deep Learning)
Quy mô Lớn (Large Scale)
Xu hướng (~Nhân đôi mỗi 6 tháng)
Hình 1.6: Kỷ nguyên Quy mô: Các ước tính sức mạnh tính toán huấn luyện minh họa (FLOPs) so với năm trên thang logarit. Trong khi học sâu thời kỳ đầu (màu xanh lam) cho thấy sự tăng trưởng nhanh chóng, kỷ nguyên transformer (màu đỏ) đã đẩy nhanh xu hướng này một cách đáng kể. Từ AlexNet (2012) đến các điểm neo quy mô huấn luyện lớp GPT-4 mang tính minh họa (2023), yêu cầu về tính toán đã tăng lên khoảng 7 cấp số nhân (gấp 16.7 triệu lần), vượt xa Định luật Moore. Phép so sánh điểm cuối này khác biệt với các nghiên cứu về xu hướng tổng hợp tính toán huấn luyện (Amodei and Hernandez 2018b; Sevilla et al. 2022) và được sử dụng ở đây để tạo động lực cho các cơ sở hạ tầng chuyên biệt được mô tả trong cuốn sách này.
Khi xem xét cùng nhau, hai hình ảnh này tiết lộ một mâu thuẫn hiển nhiên định hình kinh tế học của việc phát triển AI hiện đại: hình 1.5 cho thấy hiệu quả được cải thiện 44.5 lần trong khi hình 1.6 cho thấy nhu cầu tính toán tăng trưởng khoảng 7 cấp số nhân. Giải pháp (resolution) nằm ở việc hiểu cách thức hiệu quả và quy mô đồng tiến hóa (co-evolve).


================ PAGE 63 ================

1. Giới thiệu
25
23
Kỹ thuật Máy tính (Computer Engineering): Được chính thức hóa như một chuyên ngành học thuật khi Đại học Case Western Reserve ra mắt chương trình được công nhận đầu tiên vào năm 1971, thừa nhận rằng cả kỹ thuật điện hay khoa học máy tính đơn thuần đều không thể giải quyết việc xây dựng các máy tính đáng tin cậy từ các thành phần không đáng tin cậy. Kỹ thuật hệ thống ML tóm tắt lại sự hội tụ này: ràng buộc cốt lõi không nằm ở thuật toán hay phần cứng một cách riêng lẻ, mà nằm ở sự tích hợp cả hai dưới các ngân sách về độ trễ, năng lượng, và chất lượng dữ liệu mà chương trình giảng dạy của không chuyên ngành nào giải quyết đầy đủ.
Góc nhìn Hệ thống 1.5: Nghịch lý hiệu suất (The efficiency paradox)
Nghịch lý hiệu suất này định hình kinh tế học của kỹ thuật hệ thống ML. Những lợi ích về hiệu quả cho phép thực hiện các thí nghiệm lớn hơn, vốn đòi hỏi sức mạnh tính toán cao hơn, từ đó lại tạo động lực cho các nghiên cứu về hiệu quả xa hơn nữa. Hãy xem xét: nếu EfficientNet cần khối lượng tính toán ít hơn 44.5 lần so với AlexNet để đạt cùng độ chính xác, các tổ chức sẽ không đầu tư phần tiết kiệm đó vào việc giảm chi phí mà đưa vào việc huấn luyện các mô hình lớn hơn trên dữ liệu nhiều hơn, đó chính xác là lý do tại sao GPT-3 cuối cùng lại đòi hỏi tính toán nhiều hơn theo nhiều cấp số nhân (orders of magnitude) so với AlexNet, bất chấp những khoản lợi ích to lớn về hiệu suất tính trên mỗi FLOP (per-FLOP efficiency gains). Vòng lặp phản hồi này, nơi hiệu suất cho phép mở rộng quy mô và quy mô lại đòi hỏi hiệu suất, xác định bức tranh toàn cảnh về kỹ thuật AI hiện đại. Việc hiểu được động lực học (dynamic) này là điều cần thiết để đưa ra những quyết định sáng suốt về nơi cần đầu tư nỗ lực tối ưu hóa.
Các phương pháp cụ thể để đạt được những lợi ích này được phát triển một cách có hệ thống trong Chương 10 (các kỹ thuật thuật toán) và Chương 11 (nền tảng phần cứng). Chương 9 đề cập đến lựa chọn dữ liệu như một kỹ thuật nâng cao hiệu quả, trong khi Chương 4 bao quát thiết kế đường ống (pipeline design) và cơ sở hạ tầng chất lượng để làm cho dữ liệu được chọn có thể sử dụng được.
Bối cảnh triển khai quyết định những chiều hướng hiệu suất nào cần ưu tiên: các hệ thống đám mây tối ưu hóa cho thông lượng (throughput) trong khi các thiết bị biên tối ưu hóa cho điện năng (power). Lưu ý những gì các phần trước vừa yêu cầu đối với người kỹ sư: quy luật sắt yêu cầu lý luận đồng thời về sự di chuyển dữ liệu và quá trình tính toán, phương trình suy thoái yêu cầu việc giám sát sự trôi dạt thống kê (statistical drift) trong môi trường sản xuất, và khuôn khổ hiệu quả yêu cầu cân bằng giữa việc cải thiện thuật toán, sức mạnh tính toán, và dữ liệu so với nhau. Không một chuyên ngành hiện tại nào giảng dạy tất cả các kỹ năng này. Khoa học máy tính giải quyết các thuật toán; kỹ thuật điện giải quyết phần cứng. Không ngành nào giải quyết được thách thức tích hợp (integrated challenge) của việc xây dựng các hệ thống ML đồng thời hiệu quả, đáng tin cậy, và có khả năng mở rộng quy mô. Khoảng trống này tạo động lực cho một định nghĩa chính thức về chuyên ngành bao quát chúng: Kỹ thuật AI (AI Engineering).
1.9 Định nghĩa Kỹ thuật AI
Định nghĩa 1.3: Kỹ thuật AI (AI engineering)
Kỹ thuật AI là chuyên ngành kỹ thuật thiết kế, triển khai, và bảo trì các hệ thống có các đầu ra vốn có tính xác suất (ngẫu nhiên - stochastic) để đáp ứng các mục tiêu về độ tin cậy tất định (deterministic reliability targets) thông qua việc thỏa mãn đồng thời các ràng buộc trên cả ba trục D·A·M (Chất lượng dữ liệu - Data quality, Tính đúng đắn của thuật toán - Algorithm correctness, Hiệu suất của máy móc - Machine efficiency) trong môi trường sản xuất.
1. Ý nghĩa: Nghiên cứu ML thường chỉ tối ưu hóa trục thuật toán (𝑂 và sự hội tụ). Kỹ thuật AI tối ưu hóa chung cả ba: nó giới hạn 𝐷_vol bằng các yêu cầu quản trị dữ liệu (data governance requirements), giới hạn 𝑂 / (𝑅_peak ⋅ 𝜂_hw) bằng các yêu cầu độ trễ sản xuất, và giới hạn tổng mức tiêu thụ điện năng bằng các ngân sách về năng lượng và chi phí. Một hệ thống sản xuất đạt độ chính xác 95 phần trăm trong nghiên cứu nhưng vi phạm yêu cầu độ trễ 100 ms trong sản xuất là một hệ thống thất bại, bất kể điểm số thuật toán của nó là bao nhiêu.
2. Sự Khác biệt: Không giống như nghiên cứu học máy, vốn nhắm vào một mục tiêu đơn lẻ (sự mất mát đánh giá - validation loss) trên một tập dữ liệu tĩnh, kỹ thuật AI nhắm vào một bề mặt ràng buộc đa mục tiêu (multi-objective constraint surface) (độ trễ, thông lượng, độ chính xác, chi phí, tính công bằng, và tính mạnh mẽ - robustness) trên một phân phối thay đổi liên tục sau khi triển khai.
3. Cạm bẫy Phổ biến: Một quan niệm sai lầm thường gặp là cho rằng kỹ thuật AI chỉ là "kỹ thuật phần mềm cho ML." Sự khác biệt quan trọng là đặc điểm kỹ thuật (specification) của hệ thống mang tính xác suất: đầu ra của một hệ thống ML là hợp lệ (valid) hay không hợp lệ về mặt thống kê đối với một phân phối liên tục thay đổi, chứ không phải đúng hay sai đối với một hợp đồng (contract) tất định cố định. Điều này làm cho việc giám sát liên tục (continuous monitoring) trở thành một yêu cầu cấu trúc, chứ không phải là một lựa chọn vận hành.
Cụm từ "các hệ thống ngẫu nhiên có độ tin cậy tất định" (stochastic systems with deterministic reliability) nắm bắt một phả hệ sâu sắc. Sự nổi lên của kỹ thuật AI như một chuyên ngành học biệt lập phản ánh cách kỹ thuật máy tính (computer engineering) nổi lên vào cuối những năm 1960 và đầu những năm 1970.²³ Khi các hệ thống máy tính ngày càng trở nên phức tạp, cả kỹ thuật điện lẫn khoa học máy tính đứng độc lập đều không thể giải quyết được những thách thức tích hợp trong việc xây dựng một hệ thống đáng tin cậy


================ PAGE 64 ================

26
1.10 Vòng đời của Hệ thống ML
từ các linh kiện. Kỹ thuật máy tính nổi lên như một chuyên ngành bắc cầu giữa cả hai lĩnh vực. Ngày nay, kỹ thuật AI đối mặt với những thách thức tương tự ở điểm giao thoa giữa thuật toán, cơ sở hạ tầng, và thực tiễn vận hành.
Kỹ thuật AI bao gồm toàn bộ vòng đời của các hệ thống thông minh (intelligent systems) sản xuất. Một thuật toán đột phá đòi hỏi việc thu thập và xử lý dữ liệu hiệu quả, tính toán phân tán (distributed computation) trên hàng trăm hoặc hàng nghìn máy móc, dịch vụ đáng tin cậy tới người dùng với những yêu cầu nghiêm ngặt về độ trễ, và việc giám sát và cập nhật liên tục dựa trên hiệu suất ở thế giới thực. Xuyên suốt văn bản này, chúng tôi sử dụng cụm từ "kỹ thuật hệ thống ML" (ML systems engineering) để mô tả hoạt động thực tiễn này: công việc thiết kế, triển khai, và bảo trì các hệ thống học máy cấu thành nên AI hiện đại.
Định nghĩa một chuyên ngành là một chuyện; thực hành nó lại là chuyện khác. Định nghĩa cho chúng ta biết kỹ thuật AI là gì, nhưng các kỹ sư cần biết nó diễn ra như thế nào trong thực tiễn. Phần mềm truyền thống đi theo một vòng đời đã được hiểu rõ: thiết kế, triển khai (implement), kiểm thử (test), đưa vào sử dụng (deploy), bảo trì (maintain). Các hệ thống ML đi theo một mô hình khác, một mô hình được định hình bởi hành vi phụ thuộc vào dữ liệu và các chế độ suy thoái thầm lặng mà chúng ta đã xác định. Việc hiểu được vòng đời này, và cách bối cảnh triển khai định hình lại nó ra sao, là chiếc cầu nối giữa các nguyên tắc trừu tượng và công việc kỹ thuật hằng ngày.
1.10 Vòng đời của Hệ thống ML
Vòng đời rất quan trọng bởi vì đối tượng kỹ thuật không còn chỉ là mã nguồn; nó là mã nguồn, dữ liệu, hành vi mô hình, bối cảnh triển khai, và bằng chứng giám sát (monitoring evidence) cùng tiến hóa với nhau. Các vòng lặp phản hồi sản xuất có thể đẩy một hệ thống đã triển khai quay trở lại việc thu thập và huấn luyện dữ liệu, uốn cong quỹ đạo tuyến tính quen thuộc thành một chu kỳ.
1.10.1 Vòng đời phát triển ML
Sự khác biệt về mặt cấu trúc được thể hiện đầu tiên qua các công cụ (tooling). Hàng chục năm thực tiễn đã được thiết lập giúp hỗ trợ hành vi được xác định bởi mã (code-defined behavior): kiểm soát phiên bản (version control) duy trì các lịch sử chính xác, các đường ống tích hợp liên tục (continuous integration pipelines) tự động hóa việc kiểm thử, và các công cụ phân tích tĩnh (static analysis tools) đo lường chất lượng. Hành vi học được từ dữ liệu bị trượt ra ngoài những công cụ này, bởi vì tạo tác (artifact) đang bị thay đổi không còn là một khác biệt mã (diff) do một nhà phát triển viết ra. Chúng tôi sẽ giải quyết những thách thức này và quy trình công việc chuyên biệt (specialized workflows) mà chúng đòi hỏi ở Chương 3.
Sự khác biệt sâu sắc hơn là hình dáng của bản thân quy trình: Các hệ thống ML hoạt động theo những chu kỳ liên tục (continuous cycles) thay vì một tiến trình tuyến tính (linear progression) từ lúc thiết kế đến lúc triển khai. Các vòng lặp phản hồi trong hình 1.7 cho thấy lý do tại sao: khi việc giám sát phát hiện ra sự suy thoái hiệu suất, hệ thống không chỉ đơn giản là nhận được một bản vá (patch). Nó quay ngược trở lại các chu trình thu thập dữ liệu, chuẩn bị dữ liệu, huấn luyện, và đánh giá trước khi tái triển khai, tạo ra một vòng lặp không bao giờ kết thúc vốn không có bản sao tương ứng trong kỹ thuật phần mềm truyền thống.
Thu thập Dữ liệu (Data Collection)
Chuẩn bị Dữ liệu (Data Preparation)
Huấn luyện Mô hình (Model Training)
Đánh giá Mô hình (Model Evaluation)
Triển khai Mô hình (Model Deployment)
Giám sát Mô hình (Model Monitoring)
Cần Cải thiện
Đáp ứng Yêu cầu
Hiệu suất Suy thoái
Hình 1.7: Vòng đời Hệ thống ML: Một sơ đồ quy trình sáu ô mô tả Thu thập Dữ liệu, Chuẩn bị, Huấn luyện Mô hình, Đánh giá, Triển khai, và Giám sát. Hai vòng lặp phản hồi phân biệt chu kỳ này với quy trình phát triển phần mềm tuyến tính: bước đánh giá sẽ quay lại bước chuẩn bị khi kết quả không đủ tốt, và giám sát sẽ kích hoạt thu thập dữ liệu mới khi hiệu suất bị suy thoái.
Bản chất phụ thuộc vào dữ liệu của các hệ thống ML tạo ra các vòng đời động (dynamic lifecycles) yêu cầu sự giám sát và thích ứng liên tục. Không giống như mã nguồn chỉ thay đổi thông qua sự chỉnh sửa của các nhà phát triển, dữ liệu phản ánh những thay đổi động (dynamics) trong thế giới thực: những sự dịch chuyển phân phối có thể thay đổi âm thầm hành vi của hệ thống mà không cần bất kỳ thay đổi mã nào. Khoảng trống về công cụ được xác định ở trên cũng đi theo hệ thống vào quá trình sản xuất: việc kiểm soát phiên bản vốn được xây dựng cho các thay đổi mã rời rạc (discrete code changes) nay phải vật lộn với những tập dữ liệu đang không ngừng phát triển, và các khuôn khổ kiểm thử (testing frameworks) được xây dựng cho các kết quả đầu ra tất định đòi hỏi sự thích ứng với các dự đoán theo xác suất (probabilistic predictions). Chúng ta sẽ giải quyết việc lập phiên bản dữ liệu (data versioning) và quản lý chất lượng ở Chương 4 và các cách tiếp cận giám sát (monitoring approaches) xử lý các hành vi xác suất ở Chương 14.


================ PAGE 65 ================

28
1.10 Vòng đời của Hệ thống ML
26
Nén Mô hình (Model Compression): Một hệ quả tất yếu của lựa chọn kiến trúc nhằm triển khai tại vùng biên, đánh đổi trực tiếp độ chính xác dự đoán của mô hình để đáp ứng ngân sách tài nguyên cố định của một thiết bị. Điều này cho phép một mô hình ban đầu được thiết kế cho trung tâm dữ liệu có thể chạy trong phạm vi bộ nhớ quy mô kilobyte và điện năng milliwatt của một hệ thống nhúng, thường giảm kích thước của nó đi hơn 90 phần trăm.
tập trung vào các tác vụ cụ thể trong khi tích hợp với cơ sở hạ tầng hiện có. Một số tổ chức sử dụng các cách tiếp cận kết hợp (hybrid approaches), phân phối các khả năng ML trên nhiều phân tầng (tiers) để cân bằng giữa độ trễ, quyền riêng tư, băng thông, và việc kiểm soát cập nhật.
Mỗi vị trí trên phổ triển khai này tạo ra những nút thắt cổ chai riêng biệt quyết định chiều hướng hiệu quả nào là quan trọng nhất, như được tóm tắt trong bảng 1.8:
Bảng 1.8: Các Ưu tiên Hiệu quả theo Bối cảnh Triển khai: Mỗi môi trường triển khai tạo ra những nút thắt cổ chai riêng biệt, đòi hỏi các chiến lược tối ưu hóa được tinh chỉnh phù hợp. Các hệ thống đám mây tối ưu hóa cho thông lượng và chi phí; các hệ thống biên tối ưu hóa cho bộ nhớ và điện năng; các hệ thống TinyML đòi hỏi hiệu quả cực độ trên mọi chiều hướng.
Môi trường (Environment)
Ràng buộc Chính (Primary Constraint)
Trọng tâm Hiệu quả (Efficiency Focus)
Huấn luyện đám mây
Chi phí, thông lượng
Hiệu quả phân tán, sự tận dụng phần cứng
Suy luận đám mây
Độ trễ, chi phí mỗi truy vấn
Phân lô, tối ưu hóa quá trình phục vụ mô hình
Thiết bị biên
Bộ nhớ, điện năng
Các mô hình nhỏ hơn và sự di chuyển dữ liệu thấp hơn
Di động (Mobile)
Pin, nhiệt độ (thermal)
Suy luận tiết kiệm năng lượng
TinyML
Bộ nhớ quy mô kilobyte, năng lượng mW
Nén cực độ, các kiến trúc chuyên biệt
1.10.3 Việc triển khai định hình vòng đời như thế nào
Phổ triển khai (deployment spectrum) đại diện cho nhiều thứ hơn là các cấu hình phần cứng khác nhau. Mỗi môi trường triển khai định hình lại mọi giai đoạn của vòng đời ML, từ lúc thu thập dữ liệu ban đầu cho đến quá trình hoạt động liên tục và phát triển, tạo ra một sự tương tác của các ràng buộc mà phần mềm truyền thống hiếm khi gặp phải.
Hãy xem xét việc một quyết định triển khai đơn lẻ gây hiệu ứng lan truyền (cascades) qua toàn bộ hệ thống như thế nào. Các ứng dụng nhạy cảm với độ trễ như xe tự hành hoặc phát hiện gian lận thời gian thực yêu cầu các kiến trúc biên hoặc nhúng bất chấp các ràng buộc về tài nguyên của chúng, trong khi các mô hình ngôn ngữ lớn lại tự nhiên hướng về cơ sở hạ tầng đám mây tập trung. Tuy nhiên, lựa chọn kiến trúc ban đầu này quyết định nhiều thứ hơn là chỉ nơi quá trình tính toán diễn ra. Các hệ thống đám mây phải tối ưu hóa cho hiệu quả chi phí ở quy mô lớn, cân bằng giữa các cụm GPU, bộ nhớ lưu trữ, và băng thông mạng đắt đỏ, điều này đến lượt nó lại định hình tần suất các mô hình được huấn luyện lại, những dữ liệu lịch sử nào được giữ lại, và cách tải suy luận được phân phối. Các hệ thống biên và di động đối mặt với những giới hạn tài nguyên cố định ràng buộc sự phức tạp của mô hình và tần suất cập nhật, buộc phải nén mô hình một cách tích cực²⁶ và lên lịch trình cẩn thận. Những ràng buộc khắt khe nhất nảy sinh trong các môi trường nhúng và TinyML, nơi mỗi byte bộ nhớ và milliwatt năng lượng đều quan trọng.
Độ phức tạp trong vận hành tăng lên khi các hệ thống ngày càng trở nên phân tán hơn. Các kiến trúc đám mây tập trung được hưởng lợi từ các công cụ triển khai trưởng thành và các dịch vụ được quản lý, trong khi các hệ thống biên và kết hợp (hybrid) phải điều phối việc thu thập dữ liệu trên các cảm biến có khả năng kết nối khác nhau, theo dõi các mô hình được triển khai trên hàng nghìn thiết bị, xử lý việc triển khai theo từng giai đoạn (staged rollouts) cùng với các khả năng khôi phục (rollback), và tổng hợp các tín hiệu giám sát từ các điểm cuối (endpoints) phân tán về mặt địa lý (Chương 14). Những vấn đề cân nhắc về dữ liệu tạo ra những áp lực cạnh tranh: yêu cầu về quyền riêng tư hoặc quy định về chủ quyền dữ liệu có thể đẩy quá trình tính toán về phía vùng biên, trong khi nhu cầu về dữ liệu huấn luyện quy mô lớn lại kéo về phía tổng hợp trên đám mây tập trung. Ngay cả việc cập nhật mô hình cũng hoạt động khác nhau trên toàn bộ phổ: kiến trúc đám mây cho phép lặp lại (iteration) nhanh chóng thông qua việc kiểm soát lưu lượng tập trung, trong khi việc triển khai tại biên yêu cầu cập nhật từ xa với khả năng khôi phục và quản lý băng thông cẩn thận.
Trong thực tế, những sự đánh đổi này hiếm khi là những lựa chọn nhị phân đơn giản. Các hệ thống ML hiện đại thường áp dụng các cách tiếp cận kết hợp (hybrid approaches) trải dài trên phổ triển khai. Một chiếc xe tự hành thực hiện nhận thức và kiểm soát theo thời gian thực tại vùng biên vì lý do độ trễ, tải dữ liệu lái xe lên đám mây để cải thiện mô hình, và định kỳ tải xuống các mô hình đã được cập nhật. Một trợ lý giọng nói chạy quá trình phát hiện từ đánh thức (wake-word) ngay trên thiết bị để bảo vệ quyền riêng tư và giảm độ trễ, nhưng gửi toàn bộ giọng nói lên đám mây để xử lý ngôn ngữ tự nhiên phức tạp. Hiểu biết cốt lõi là một lựa chọn triển khai trên các thiết bị nhúng không chỉ ràng buộc kích thước mô hình; nó ảnh hưởng đến các chiến lược thu thập dữ liệu, các cách tiếp cận huấn luyện, các số đo (metrics) đánh giá, các cơ chế triển khai, và các khả năng giám sát. Những quyết định liên kết chặt chẽ với nhau này minh chứng cho hệ phân loại D·A·M trong thực tế, nơi mà các ràng buộc dọc theo một trục tạo ra các hiệu ứng lan truyền xuyên suốt toàn bộ hệ thống.


================ PAGE 67 ================

1. Giới thiệu
29
27
Waymo: Quy trình làm việc lái xe tự hành kết hợp (hybrid) rủi ro cao buộc phải đối mặt với một thách thức về đồng bộ hóa vốn không có trong các hệ thống thuần đám mây hay thuần biên: mô hình trên xe phải được kiểm soát và kiểm thử hồi quy (regression-tested) trước khi triển khai, trong khi cơ sở hạ tầng đám mây có thể huấn luyện và đánh giá các phiên bản được cải thiện dựa trên dữ liệu lái xe mới thu thập. Điều này tạo ra một khoảng trống quản lý phiên bản giữa các mô hình đã được triển khai và các mô hình mới được huấn luyện, đòi hỏi quá trình xác thực nghiêm ngặt trước khi bất kỳ bản cập nhật mô hình từ xa nào có thể được đẩy (pushed) xuống các phương tiện có tính an toàn quan trọng.
28
FarmBeats: Hệ thống chứng minh rằng ràng buộc cốt yếu đối với ML vùng biên thường là băng thông (BW) mạng chứ không phải tính toán hay chất lượng mô hình. Bằng cách sử dụng mạng lưới không gian trắng (white-space) của TV và xử lý tại biên, FarmBeats biến tính mới mẻ của mô hình và sự đồng bộ hóa dữ liệu thành các vấn đề kỹ thuật hạng nhất (first-class) trong các đợt triển khai bị giới hạn về kết nối (Vasisht et al. 2017).
29
LiDAR (Tính toán Khoảng cách và Phát hiện bằng Ánh sáng): Cảm biến này là lý do chính khiến chiếc xe trở thành một "trung tâm dữ liệu lưu động" (roving data center), khi các tia laser xung của nó tạo ra một đám mây điểm 3D dày đặc của môi trường. Luồng dữ liệu thô từ một thiết bị duy nhất có thể vượt quá 100 megabyte mỗi giây, tạo ra cả thách thức về khối lượng quy mô terabyte và thách thức về chất lượng như đã đề cập, vì tín hiệu dễ dàng bị suy giảm do nhiễu cảm biến từ mưa hoặc sương mù.
30
Radar (Tính toán Khoảng cách và Phát hiện bằng Vô tuyến): Radar phát ra sóng vô tuyến phần lớn không bị ảnh hưởng bởi mưa và sương mù, những thứ làm mù các cảm biến quang học như máy ảnh. Tính chất vật lý này cung cấp lớp mạnh mẽ (robustness layer) cốt yếu trong một hệ thống hợp nhất cảm biến như của Waymo, cho phép nó bù đắp cho chế độ lỗi đã biết của các máy ảnh trong thời tiết xấu. Độ tin cậy trong mọi thời tiết của radar ô tô bắt nguồn từ hoạt động tần số cao của nó (~77 GHz), cung cấp khả năng phát hiện đối tượng liên tục ngay cả khi các cảm biến độ phân giải cao hơn bị suy giảm hiệu suất.
Để làm cho những sự đánh đổi trừu tượng này trở nên cụ thể, chúng ta xem xét ba hệ thống sản xuất đại diện cho các thái cực của phổ triển khai. Mỗi hệ thống đối mặt với cùng những thách thức cốt lõi (chất lượng dữ liệu, độ phức tạp của mô hình, và quy mô máy móc), nhưng các ràng buộc từ môi trường triển khai của chúng buộc phải có những giải pháp kỹ thuật hoàn toàn khác biệt.
1.11 Nghiên cứu Tình huống Triển khai (Deployment Case Studies)
Một nghiên cứu tình huống triển khai trở thành một công cụ kỹ thuật khi nó phơi bày ràng buộc cốt yếu đằng sau một thiết kế. Ba hệ thống sản xuất dưới đây nằm ở các thái cực khác nhau của phổ triển khai, do đó cùng những câu hỏi D·A·M lại buộc phải có những phản hồi kỹ thuật khác nhau:
• Waymo²⁷ (Sun et al. 2020) bị ràng buộc về độ trễ an toàn quan trọng (safety-critical latency) và tính mới (freshness) của dữ liệu. Ngăn xếp (stack) nhận thức lái xe tự hành của nó minh họa một mô hình triển khai kết hợp đầy rủi ro: các mô hình nhận thức trên xe (on-vehicle perception models) chạy ở vùng biên dưới các yêu cầu nghiêm ngặt về độ trễ, trong khi cơ sở hạ tầng đám mây hỗ trợ việc huấn luyện và đánh giá trên dữ liệu lái xe đa phương thức (multimodal) quy mô lớn.
• FarmBeats²⁸ (Vasisht et al. 2017) bị ràng buộc về kết nối và tính mới của mô hình. Nền tảng nông nghiệp chính xác của Microsoft triển khai các mô hình ML tới các trang trại có kết nối hạn chế. FarmBeats đại diện cho mô hình triển khai vùng biên bị hạn chế tài nguyên: các mô hình nhỏ gọn chạy suy luận trên các thiết bị năng lượng thấp trong khi các liên kết mạng giới hạn tốc độ di chuyển của dữ liệu và các bản cập nhật.
• AlphaFold (Jumper et al. 2021) bị ràng buộc bởi việc tìm kiếm cần nhiều tính toán (compute-intensive) và dữ liệu khoa học được giám tuyển (curated). Hệ thống dự đoán cấu trúc protein của DeepMind đã giải quyết một thách thức lớn kéo dài 50 năm trong sinh học. AlphaFold đại diện cho mô hình triển khai đám mây tính toán chuyên sâu: việc huấn luyện yêu cầu 128 lõi TPUv3 chạy trong nhiều tuần và sử dụng Ngân hàng Dữ liệu Protein (Protein Data Bank) gồm các cấu trúc được xác định qua thực nghiệm.
Các hệ thống này bổ sung cho các Mô hình Ngọn hải đăng bằng cách minh họa cách thức cùng một thách thức cốt lõi (chất lượng dữ liệu, độ phức tạp mô hình, và quy mô cơ sở hạ tầng) biểu hiện dưới các ràng buộc hoàn toàn khác biệt. Thay vì xem xét mỗi hệ thống một cách cô lập, chúng được phân tích qua lăng kính của hệ phân loại D·A·M. Hiện tượng trôi dạt dữ liệu tương tự ảnh hưởng đến các mô hình nhận thức của Waymo khi thời tiết thay đổi cũng ảnh hưởng đến quá trình phát hiện bệnh cây trồng của FarmBeats qua các mùa vụ, mặc dù các giải pháp kỹ thuật khác nhau dựa trên các ràng buộc về máy móc.
Sự phụ thuộc lẫn nhau giữa các trục D·A·M tạo ra những loại thách thức cụ thể xác định công việc hàng ngày của một kỹ sư hệ thống ML. Bằng cách kiểm tra các thái cực triển khai của chúng ta, chúng ta có thể thấy những thách thức này ở những dạng khắc nghiệt nhất của chúng.
Dữ liệu trong thế giới thực thường nhiễu và không nhất quán, bộc lộ nhóm thách thức đầu tiên. Các phương tiện tự hành của Waymo hoạt động như các trung tâm dữ liệu lưu động, xử lý các luồng cảm biến đa phương thức khổng lồ trên LiDAR²⁹, radar³⁰, và máy ảnh (Sun et al. 2020). Các kỹ sư phải giải quyết tình trạng nhiễu cảm biến, chẳng hạn như mưa làm mờ máy ảnh, và sự lệch pha thời gian (temporal misalignment) giữa các luồng dữ liệu không đồng bộ. Quy mô làm phức tạp thêm những vấn đề về chất lượng này: FarmBeats nằm ở một thái cực, với các mô hình dưới megabyte bị nhồi nhét qua các liên kết băng thông cấp kilobit được mô tả trước đó, trong khi AlphaFold nằm ở thái cực ngược lại, yêu cầu quyền truy cập vào các cấu trúc được xác định bằng thực nghiệm của Ngân hàng Dữ liệu Protein trong suốt quá trình huấn luyện.
Trôi dạt dữ liệu tạo ra một gánh nặng vận hành liên tục nằm trên cả chất lượng và quy mô. Các đặc tính thống kê của dữ liệu đầu vào thay đổi theo thời gian, và các mô hình chỉ đáng tin cậy nếu chúng phù hợp với phân phối hiện tại (Gama et al. 2014; Quiñonero-Candela et al. 2009; Koh et al. 2021). Các mô hình của Waymo được huấn luyện trên những con đường ngập nắng của Phoenix có thể gặp trục trặc trong bão tuyết ở New York do sự dịch chuyển phân phối³¹; việc phát hiện những sự dịch chuyển này đòi hỏi phải giám sát liên tục các số liệu thống kê đầu vào trước khi chúng biểu hiện thành lỗi hệ thống.
Ngoài dữ liệu, độ phức tạp của mô hình và khả năng khái quát hóa tạo thành nhóm thách thức thứ hai. Cường độ tính toán (Computational intensity) định nghĩa giới hạn trên của năng lực: các mô hình nền tảng ở quy mô GPT-3 (phần 1.3.3) đòi hỏi tính toán lên đến zettaFLOP, và ngay cả các mô hình khoa học nhỏ hơn như AlphaFold cũng yêu cầu hàng tuần lễ huấn luyện bằng các bộ tăng tốc chuyên dụng. Kỹ sư hệ thống phải tối ưu hóa cho "FLOP/s trên mỗi watt" để làm cho những mô hình này khả thi về mặt kinh tế và môi trường. Thế nhưng chỉ riêng quy mô thô là chưa đủ. Khoảng trống khái quát hóa (generalization gap) vẫn là rủi ro cốt lõi của thuật toán: một mô hình có thể đạt độ chính xác 99 phần trăm trên các điểm chuẩn (benchmarks) nhưng chỉ đạt 75 phần trăm trong thế giới thực. Đối với các hệ thống lái xe tự hành có tính an toàn then chốt của Waymo, việc giảm thiểu khoảng trống này là một yêu cầu sống còn, đòi hỏi các phương pháp đảm bảo tính mạnh mẽ có thể bao phủ được một dải dài (long tail) các trường hợp biên.


================ PAGE 68 ================

30
1.12 Khuôn khổ Năm Trụ cột
31
Trôi dạt Dữ liệu (Data Drift): Sự phân kỳ (divergence) dần dần giữa phân phối dữ liệu huấn luyện (𝑃_0) và phân phối sản xuất trong thế giới thực (𝑃_𝑡). Sự trôi dạt là "entropy" của các hệ thống ML: độ chính xác bị xói mòn thầm lặng theo thời gian khi môi trường thay đổi, và nếu không được giám sát liên tục, sự suy thoái này sẽ trở nên vô hình cho đến khi nó biểu hiện thành lỗi hệ thống (xem Chương 14).
32
Tấn công Suy luận (Inference Attack): Một mối đe dọa bảo mật trong đó kẻ thù truy vấn một mô hình để suy luận thông tin nhạy cảm về tập huấn luyện. Những cuộc tấn công này khai thác xu hướng ghi nhớ các mẫu (patterns) duy nhất trong dữ liệu huấn luyện của các mô hình bị tham số hóa quá mức (overparameterized models), tạo ra một sự đánh đổi trực tiếp giữa năng lực mô hình và rủi ro quyền riêng tư vốn là động lực cho các kỹ thuật phòng thủ như quyền riêng tư khác biệt (differential privacy) và nhiễu loạn đầu ra (output perturbation).
Nhóm thách thức thứ ba bao gồm các khó khăn ở cấp độ hệ thống trong việc khiến các mô hình hoạt động đáng tin cậy trong môi trường sản xuất. Sự phân chia huấn luyện-phục vụ mô tả khoảng cách giữa môi trường linh hoạt nơi các mô hình ra đời và môi trường cứng nhắc nơi chúng hoạt động. Sự đánh đổi giữa độ trễ và thông lượng quyết định kiến trúc: các hệ thống nhận thức kiểu Waymo yêu cầu các quyết định an toàn có độ trễ thấp tại vùng biên, trong khi AlphaFold ưu tiên thông lượng, chạy nhiều ngày trên đám mây để khám phá các không gian cấu hình protein rộng lớn. Sự điều phối kết hợp (Hybrid coordination) làm tăng thêm độ phức tạp, khi các hệ thống hiện đại ngày càng áp dụng các kiến trúc phân tầng (tiered architectures). Ví dụ, một trợ lý giọng nói thực hiện việc phát hiện từ đánh thức cục bộ (TinyML) để bảo vệ quyền riêng tư và giảm độ trễ, nhưng lại chuyển các quá trình xử lý ngôn ngữ tự nhiên phức tạp sang các cụm GPU khổng lồ trên đám mây.
Cuối cùng, khi các hệ thống mở rộng quy mô, tác động của chúng đối với xã hội trở thành mối quan tâm kỹ thuật hàng đầu cắt ngang qua cả ba trục D·A·M. Sự công bằng và thiên vị phải được quản lý một cách chủ động, vì các mô hình có thể vô tình học phải những thiên vị (biases) của xã hội hiện diện trong dữ liệu huấn luyện của chúng. Thực hành kỹ thuật có trách nhiệm (Responsible engineering) đòi hỏi phải kiểm toán hệ thống về mặt hiệu suất trên các nhóm nhân khẩu học để đảm bảo kết quả công bằng. Yêu cầu về tính minh bạch và quyền riêng tư càng ràng buộc hơn về mặt thiết kế: nhiều mạng sâu hoạt động như "hộp đen", thế nhưng trong các lĩnh vực như chăm sóc sức khỏe hay tài chính, các bên liên quan yêu cầu khả năng diễn giải (interpretability). Hệ thống cũng phải có khả năng phục hồi trước các cuộc tấn công suy luận³² nhằm cố gắng trích xuất dữ liệu huấn luyện nhạy cảm từ các dự đoán của mô hình.
Bốn nhóm thách thức này—dữ liệu, mô hình, hệ thống, và đạo đức—không tồn tại độc lập. Sự trôi dạt dữ liệu làm suy giảm độ chính xác của mô hình, gây áp lực lên cơ sở hạ tầng, và có thể khuếch đại rủi ro đạo đức. Vấn đề chưa được giải quyết là quyền sở hữu: mỗi danh mục đòi hỏi kỹ thuật chuyên sâu, nhưng chuỗi lỗi (failure chain) lại vắt ngang tất cả chúng.
1.12 Khuôn khổ Năm Trụ cột
Khoảng trống giữa việc phát triển và triển khai mô hình không chỉ nằm ở thuật toán: nó bao gồm chất lượng dữ liệu, hành vi mô hình, cơ sở hạ tầng vận hành, và quy trình làm việc của tổ chức (Paleyes et al. 2022). Sự suy giảm hiệu suất thầm lặng, sự trôi dạt dữ liệu, độ phức tạp của mô hình, và những quan ngại về đạo đức, mỗi thứ đều đòi hỏi một kỹ thuật chuyên sâu, thế nhưng chúng lại tương tác với nhau: sự thất bại về chất lượng dữ liệu làm suy giảm mô hình, gây áp lực lên cơ sở hạ tầng phục vụ, và có thể khuếch đại rủi ro đạo đức. Thực tiễn kỹ thuật phần mềm truyền thống không thể giải quyết được các hệ thống suy thoái âm thầm thay vì hỏng hóc có thể nhìn thấy, do đó khuôn khổ phải phân công trách nhiệm rõ ràng cho mỗi loại thách thức trong khi vẫn duy trì sự điều phối trên toàn bộ hệ thống.
Cuốn sách này tổ chức kỹ thuật hệ thống ML xung quanh năm chuyên ngành liên kết với nhau, trực tiếp giải quyết các nhóm thách thức mà chúng ta đã xác định. Hình 1.8 trình bày cấu trúc tổ chức này: năm trụ cột kỹ thuật, mỗi trụ cột nhắm mục tiêu vào một danh mục thách thức riêng biệt, nằm trên một nền tảng chung phản ánh các ràng buộc vật lý và kinh tế mà mọi trụ cột phải tôn trọng. Cùng với nhau, chúng đại diện cho các năng lực kỹ thuật cốt lõi cần thiết để thu hẹp khoảng cách giữa các nguyên mẫu nghiên cứu và các hệ thống sản xuất có khả năng hoạt động đáng tin cậy ở quy mô lớn. Mặc dù các trụ cột này tổ chức việc thực hành kỹ thuật ML, chúng được hỗ trợ bởi các mệnh lệnh kỹ thuật nền tảng là Tối ưu hóa Hiệu suất và Tăng tốc Phần cứng (được đề cập trong Phần III), cung cấp hiệu suất cần thiết để làm cho việc triển khai và huấn luyện quy mô lớn khả thi về mặt vật lý và kinh tế.
1.12.1 Năm chuyên ngành kỹ thuật
Các trụ cột dễ hiểu nhất là thông qua một chuỗi lỗi (failure chain). Giả sử một mô hình từ đánh thức ngừng hoạt động một cách đáng tin cậy đối với người dùng trong một tòa nhà chung cư ồn ào sau một lần cập nhật mô hình. Câu hỏi đầu tiên là liệu dữ liệu huấn luyện có nắm bắt được môi trường âm thanh đó hay không, nhãn dán có đáng tin cậy hay không, và đường ống (pipeline) có thể theo dõi ví dụ nào đã đến được với mô hình hay không. Đó là trụ cột Kỹ thuật Dữ liệu (Data Engineering) (Chương 4): nó quản lý chất lượng dữ liệu, quy mô, quyền riêng tư, sự trôi dạt, và các vấn đề về phả hệ (lineage) quyết định những gì mô hình có thể học được.
Nếu dữ liệu hợp lý, câu hỏi tiếp theo là liệu quá trình huấn luyện có chuyển đổi nó thành một mô hình phù hợp với nhiệm vụ và ngân sách hay không. Trụ cột Hệ thống Huấn luyện (Training Systems) (Chương 8) làm chủ ranh giới đó: điều phối các tập dữ liệu, các khuôn khổ (frameworks), thuật toán tối ưu hóa, siêu tham số, các công việc phân tán, khởi động lại, và sự đánh đổi chi phí-chất lượng do quy mô mô hình tạo ra. Một mô hình được huấn luyện thành công vẫn chưa phải là một hệ thống. Trụ cột Cơ sở hạ tầng Triển khai (Deployment Infrastructure) làm chủ ranh giới huấn luyện-phục vụ: đóng gói mô hình, hiệu suất suy luận, độ trễ, thông lượng, ràng buộc thiết bị, và phương pháp đo lường (benchmarking methods) cho biết liệu cấu phần được triển khai có còn đáp ứng yêu cầu hay không.


================ PAGE 69 ================

1. Giới thiệu
31
Hình 1.8: Khuôn khổ Năm Trụ cột: Một mô-típ đền thờ Hy Lạp thể hiện năm trụ cột của kỹ thuật hệ thống ML: Kỹ thuật Dữ liệu, Hệ thống Huấn luyện, Cơ sở hạ tầng Triển khai, Vận hành và Giám sát, và Đạo đức và Quản trị. Một trụ cột chi tiết ở bên trái phân tích các nền tảng kỹ thuật chạy xuyên suốt mọi chuyên ngành: Nền tảng Kỹ thuật, Hiệu suất & Tối ưu hóa, Đo lường & Đánh giá, Tính Mạnh mẽ & Độ Tin cậy, và Kỹ thuật Có trách nhiệm & Đạo đức.
Một khi mô hình đang được phục vụ, lỗi sẽ trở thành vấn đề về thời gian (temporal). Trụ cột Vận hành và Giám sát (Operations and Monitoring) quản lý câu hỏi về việc liệu hành vi có duy trì được mức độ chấp nhận được sau khi ra mắt hay không, khi các phân phối dữ liệu thay đổi, lưu lượng truy cập thay đổi, và chất lượng mô hình có thể bị suy giảm trong khi các bảng điều khiển (dashboards) cơ sở hạ tầng vẫn hiển thị màu xanh (bình thường). Nó kết nối quá trình giám sát, cảnh báo, chiến lược triển khai (rollout strategy), phản ứng sự cố, và đánh giá liên tục. Cuối cùng, lỗi từ đánh thức có thể không ảnh hưởng đến tất cả người dùng như nhau, và đường ống âm thanh có thể làm phát sinh các nghĩa vụ về quyền riêng tư hoặc sự đồng ý. Trụ cột Đạo đức và Quản trị (Ethics and Governance) (Chương 15) quản lý các ràng buộc đó: tính công bằng, tính minh bạch, quyền riêng tư, sự an toàn, tài liệu hóa, và trách nhiệm giải trình trong suốt vòng đời.
Các khuôn khổ tổ chức thay thế có thể nhóm những mối quan tâm này theo thành phần hoặc theo giai đoạn của vòng đời. Cấu trúc năm trụ cột được chọn vì nó khớp với ranh giới quyền sở hữu xuất hiện trong các nhóm kỹ thuật thực tế trong khi vẫn làm rõ sự phụ thuộc lẫn nhau của chúng. Lựa chọn về dữ liệu định hình kết quả huấn luyện; lựa chọn về huấn luyện ràng buộc việc triển khai; lựa chọn về triển khai xác định những gì hoạt động vận hành có thể quan sát được; và các yêu cầu quản trị có thể thay đổi cả bốn yếu tố trên. Việc coi kỹ thuật có trách nhiệm là một trụ cột riêng biệt sẽ ngăn chặn việc nó trở thành một ý nghĩ muộn màng ngầm định dưới áp lực thời hạn (deadline).
Năm trụ cột không hoạt động một cách cô lập; chúng nổi lên từ hệ phân loại D·A·M và các giai đoạn vòng đời được thiết lập ở phần trước, với mỗi trụ cột chịu trách nhiệm cho các trục cụ thể và sự tương tác của chúng trên toàn bộ vòng đời hệ thống. Cấu trúc này phản ánh cách AI tiến hóa từ nghiên cứu lấy thuật toán làm trung tâm sang kỹ thuật lấy hệ thống làm trung tâm, chuyển trọng tâm từ việc làm cho các thuật toán riêng lẻ hoạt động sang việc xây dựng các hệ thống có thể triển khai, vận hành, và bảo trì các thuật toán đó một cách đáng tin cậy ở quy mô lớn. Năm trụ cột đại diện cho các năng lực kỹ thuật cần thiết cho quá trình chuyển đổi đó.
Những trụ cột này cũng cung cấp bộ khung tổ chức cho cuốn giáo trình này. Mỗi phần của cuốn sách phát triển kiến thức và kỹ năng cần thiết cho một hoặc nhiều trụ cột, đi theo một tiến trình phản ánh cách các kỹ sư xây dựng hệ thống trong thực tế: nền tảng trước tiên, tiếp đến là xây dựng mô hình, sau đó là tối ưu hóa, và cuối cùng là triển khai sản xuất.
1.13 Tổ chức Cuốn sách
Năm trụ cột ánh xạ trực tiếp lên cấu trúc gồm bốn phần của cuốn giáo trình này, tiến triển từ các khái niệm nền tảng qua việc phát triển mô hình đến triển khai trong sản xuất. Nguyên tắc tổ chức là bối cảnh trước lý thuyết: bối cảnh (landscape) và từ vựng được thiết lập (Phần I) trước khi xây dựng mô hình (Phần II), tối ưu hóa những mô hình đó (Phần III), và triển khai chúng một cách đáng tin cậy (Phần IV). Bảng 1.9 phác thảo cách tổ chức này.
Phần I thiết lập bộ từ vựng về các ràng buộc trước khi hệ thống máy móc của mô hình xuất hiện. Chương 1 phát triển cuộc cách mạng kỹ thuật trong AI và các khuôn khổ tổ chức chuyên ngành này. Chương 2 khám phá phổ triển khai từ Đám mây đến TinyML, khảo sát cách các ràng buộc vật lý (các phạm vi điện năng, hệ thống phân cấp bộ nhớ, và các ngân sách độ trễ) chi phối mỗi phân tầng. Chương 3 trình bày


================ PAGE 70 ================

32
1.14 Sự ngụy biện và Cạm bẫy
quy trình từ đầu đến cuối, từ việc định hình bài toán đến triển khai, cung cấp bản đồ khái niệm định hướng cho việc học tập tiếp theo. Chương 4 đề cập đến việc thu thập, xử lý, và quản lý dữ liệu, xác lập rằng cơ sở hạ tầng dữ liệu đi trước và làm nền tảng (enables) cho sự phát triển mô hình.
Bảng 1.9: Tổ chức Cuốn sách: Bốn phần tuân theo một trình tự sư phạm từ bối cảnh (Nền tảng) qua lý thuyết (Xây dựng) đến thực hành (Tối ưu hóa, Triển khai). Mỗi phần được xây dựng dựa trên từ vựng và các khuôn khổ của các phần trước, vì vậy các kỹ thuật tối ưu hóa của Phần III giả định sự quen thuộc với các kiến trúc mô hình của Phần II, và các thực tiễn triển khai của Phần IV giả định sự thành thạo với Phần II và Phần III.
Phần (Part)
Chủ đề (Theme)
Các Chương Chính (Key Chapters)
I: Nền tảng (Foundations)
Bối cảnh: Toàn cảnh hệ thống ML
Chương 1, Chương 2, Chương 3, Chương 4
II: Xây dựng (Build)
Lý thuyết: Nền tảng mô hình
Chương 5, Chương 6, Chương 7, Chương 8
III: Tối ưu hóa (Optimize)
Hiệu suất: Tinh chỉnh hiệu năng (Performance tuning)
Chương 9, Chương 10, Chương 11, Chương 12
IV: Triển khai (Deploy)
Sản xuất: Các hệ thống thế giới thực
Chương 13, Chương 14, Chương 15, Chương 16
Phần II biến bộ từ vựng đó thành các kỹ năng xây dựng mô hình. Chương 5 cung cấp các nền tảng thuật toán, trong khi Chương 6 mở rộng chúng sang các thiết kế mạng cụ thể. Cả hai chương đều tham chiếu đến năm Mô hình Ngọn hải đăng được giới thiệu ở phần trước (ResNet-50, GPT-2/Llama, MobileNetV2, DLRM, và Phát hiện Từ đánh thức) để gắn kết các khái niệm trừu tượng vào những khối lượng công việc cụ thể. Chương 7 khảo sát cơ sở hạ tầng phần mềm từ TensorFlow và PyTorch đến các công cụ chuyên biệt. Chương 8 phát triển các hệ thống huấn luyện cho các mô hình phức tạp và các tập dữ liệu lớn.
Phần III đặt câu hỏi làm thế nào để thay đổi các thành phần trong quy luật sắt mà không làm mất đi chất lượng. Chương 9 giới thiệu các kỹ thuật nhằm giảm thiểu các yêu cầu tính toán trong khi vẫn duy trì chất lượng. Chương 10 đề cập đến các kỹ thuật nén mô hình làm cho việc triển khai trở nên rẻ hơn. Chương 11 xem xét phần cứng chuyên dụng, từ GPU đến các ASIC tùy chỉnh. Chương 12 thiết lập các phương pháp luận để đo lường và so sánh hiệu suất hệ thống.
Phần IV đưa các hệ thống đã tối ưu hóa trở lại quá trình sản xuất, nơi mà sự suy thoái và bối cảnh triển khai đóng vai trò chủ đạo. Chương 13 bao quát cơ sở hạ tầng phục vụ việc đưa ra các dự đoán với độ trễ thấp. Chương 14 bao gồm các hoạt động từ giám sát và triển khai đến phản ứng sự cố. Chương 15 giải quyết các vấn đề cân nhắc về đạo đức và quản trị. Chương 16 tổng hợp toàn bộ phương pháp luận và chuẩn bị cho người đọc bước chuyển đổi từ sự làm chủ nút đơn (single-node mastery) sang việc điều phối quy mô đội nhóm máy móc (fleet-scale orchestration).
Cuốn sách này bao quát chế độ nút đơn (single-node regime): 1–8 bộ tăng tốc kết nối thông qua bộ nhớ dùng chung, nơi nút thắt cổ chai cốt lõi là bức tường bộ nhớ (memory wall), tốc độ mà dữ liệu di chuyển từ HBM (bộ nhớ băng thông cao cục bộ trên bộ tăng tốc) đến các đơn vị tính toán. Ở quy mô đội nhóm máy móc (fleet scale), hàng nghìn nút phối hợp xuyên suốt các kết cấu mạng (network fabrics) và nút thắt cổ chai chuyển dịch sang băng thông chia đôi (bisection bandwidth), tức tổng công suất xuyên suốt một lát cắt qua mạng lưới cụm (cluster network). Để có hướng dẫn chi tiết về lộ trình đọc, kết quả học tập, các yêu cầu tiên quyết, và cách tận dụng tối đa giáo trình này, chương Về Cuốn sách Này ở phần đầu sách sẽ cung cấp những định hướng đó.
Trước khi tiến về phía trước, chúng tôi xem xét những giả định thường làm vấp ngã những người mới thực hành hệ thống ML. Các khuôn khổ trước đó cung cấp những mô hình tư duy (mental models) đúng đắn, nhưng chỉ khi chúng ta cũng rũ bỏ được những mô hình sai lầm được mang sang từ các lĩnh vực liền kề. Mọi chuyên ngành đều tích lũy những trực giác (intuitions) phát huy tác dụng tốt trong giới hạn của nó nhưng lại thất bại khi áp dụng sang nơi khác. Kỹ thuật hệ thống ML đặc biệt dễ bị ảnh hưởng bởi những giả định vay mượn như vậy vì nó đồng thời lấy từ kỹ thuật phần mềm, thống kê, và thiết kế phần cứng, mỗi ngành nuôi dưỡng những trực giác hơi khác nhau về cách thức một hệ thống nên hoạt động.
1.14 Sự ngụy biện và Cạm bẫy (Fallacies and Pitfalls)
Những giả định đúng trong phần mềm truyền thống, nghiên cứu học thuật, hoặc toán học thuần túy sẽ thất bại khi áp dụng cho các hệ thống có hành vi nảy sinh từ dữ liệu. Những sự ngụy biện và cạm bẫy sau đây ghi nhận những sai lầm làm lãng phí nỗ lực kỹ thuật, trì hoãn việc triển khai, và gây ra những sự cố sản xuất thầm lặng.
Ngụy biện: Thuật toán tốt hơn tự động tạo ra hệ thống tốt hơn.
Các kỹ sư cho rằng sự tinh vi của thuật toán sẽ thúc đẩy hiệu suất hệ thống, nhưng điều này bỏ qua quy luật sắt (phần 1.7). Các mô hình vision transformers chứng minh rằng kiến trúc và tiền huấn luyện quy mô lớn (large-scale pretraining) có thể tạo ra kết quả nhận dạng hình ảnh mạnh mẽ (Dosovitskiy et al. 2021), nhưng tính tiện ích trong sản xuất vẫn


================ PAGE 71 ================

1. Giới thiệu
33
Việc chỉ tối ưu hóa suy luận sẽ để nguyên phần lớn độ trễ đầu cuối (end-to-end latency).
phụ thuộc vào các ngân sách về tính toán, di chuyển dữ liệu, và độ trễ. Trong môi trường sản xuất, một mô hình có độ chính xác cao hơn 1 phần trăm nhưng lại vi phạm các yêu cầu về độ trễ về cơ bản không có tiện ích nào. Ví dụ về nợ kỹ thuật tiềm ẩn (hidden-technical-debt) ở phần trước của chương này cho thấy tại sao mã mô hình (model code) chỉ là phần trung tâm có thể nhìn thấy được của một hệ thống sản xuất lớn hơn rất nhiều. Một hệ thống được thiết kế kỹ thuật tốt (well-engineered) với một mô hình đơn giản hơn có thể vượt trội hơn một kiến trúc phức tạp nhưng lại thiếu cơ sở hạ tầng mạnh mẽ.
Cạm bẫy: Đối xử với hệ thống ML như phần mềm truyền thống tình cờ chứa một mô hình.
Các kỹ sư áp dụng các hoạt động kiểm thử và triển khai truyền thống cho các hệ thống ML, nhưng các hệ thống này thường thất bại theo những cách khác biệt về chất (section 1.6). Các lỗi truyền thống (Traditional bugs) thường tạo ra những hỏng hóc ngay lập tức; các hệ thống ML có thể suy thoái thầm lặng trong nhiều tuần hoặc nhiều tháng trước khi ai đó nhận ra. Các thử nghiệm A/B trong phần mềm thông thường có thể cho thấy các tín hiệu rõ ràng nhanh chóng, trong khi so sánh ML có thể yêu cầu những khoảng quan sát dài hơn để phát hiện những khác biệt nhỏ về độ chính xác giữa các nhóm người dùng (subpopulations). Kiểm thử đơn vị (Unit tests) xác minh các đường dẫn mang tính tất định; các hệ thống ML yêu cầu cơ sở hạ tầng giám sát để bắt những dự đoán không đáng tin cậy, sự trôi dạt dữ liệu, và các lỗi hiệu chuẩn (calibration failures). Các nhóm triển khai ML chỉ với các đường ống CI/CD có nguy cơ gặp phải những thất bại thầm lặng, vốn chỉ bộc lộ sau khi hành vi hiển thị cho người dùng đã bị suy thoái.
Ngụy biện: Độ chính xác cao trên tập dữ liệu chuẩn (benchmark datasets) cho thấy hệ thống đã sẵn sàng cho sản xuất.
Các kỹ sư giả định hiệu suất điểm chuẩn sẽ dự đoán được độ chính xác trong quá trình sản xuất, nhưng sự dịch chuyển phân phối (distribution shift) và các khác biệt trong vận hành có thể gây ra sự sụt giảm đáng kể khi triển khai. Một mô hình phân tích cảm xúc hoạt động tốt trên dữ liệu kiểm thử được giám tuyển có thể sụt giảm độ chính xác nghiêm trọng trong sản xuất khi người dùng sử dụng tiếng lóng, biểu tượng cảm xúc (emojis), và bối cảnh (context) không có trong các điểm chuẩn. Phổ triển khai (section 1.10.2) cho thấy rằng các môi trường đám mây, biên, và di động đều mang đến những ràng buộc riêng biệt: độ trễ mạng làm tăng chi phí phát sinh (overhead), độ chính xác số học hạn chế của thiết bị di động có thể làm thay đổi độ chính xác của mô hình, và thiết bị biên có thể thiếu bộ nhớ cho các chiến lược đa mô hình (multi-model strategies) vốn làm tăng điểm số điểm chuẩn. Các hệ thống sản xuất yêu cầu phân tích các chế độ lỗi (failure mode analysis) trên các nhóm nhân khẩu học, cơ sở hạ tầng giám sát để phát hiện sự trôi dạt, và các giao thức xác thực (validation protocols) phù hợp với điều kiện vận hành thực tế thay vì các tập kiểm thử lý tưởng hóa.
Cạm bẫy: Tối ưu hóa các thành phần riêng lẻ mà không xem xét sự tương tác của hệ thống.
Các kỹ sư tối ưu hóa độ trễ suy luận một cách độc lập, nhưng Định luật Amdahl chi phối hiệu suất đầu cuối (end-to-end performance). Một nhóm làm giảm thời gian suy luận mô hình từ 45 ms xuống 15 ms, kỳ vọng sự cải thiện theo tỷ lệ tương ứng. Thế nhưng tiền xử lý chiếm 60 ms và hậu xử lý cộng thêm 25 ms, do đó tổng độ trễ chỉ giảm từ 130 ms xuống 100 ms: cải thiện 23 phần trăm thay vì 67 phần trăm như kỳ vọng. Hệ phân loại D·A·M (bảng 1.4) cho thấy các trục Dữ liệu, Thuật toán, và Máy móc tạo thành một hệ thống phụ thuộc lẫn nhau, nơi mà việc tối ưu hóa một thành phần chỉ làm dịch chuyển nút thắt cổ chai thay vì loại bỏ chúng. Một mô hình đòi hỏi tiền xử lý nhiều hơn 3 lần có thể làm tăng tổng chi phí lên 40 phần trăm trong khi chỉ cải thiện độ chính xác được 2 phần trăm. Các nhóm tối ưu hóa thành phần độc lập thường phát hiện ra rằng 50–70 phần trăm nỗ lực kỹ thuật của họ không mang lại cải thiện cho các số đo đầu cuối.
Ngụy biện: Hệ thống ML có thể được triển khai một lần và để hoạt động vô thời hạn.
Các kỹ sư cho rằng hệ thống đã triển khai sẽ duy trì hiệu suất vô thời hạn, nhưng phương trình suy thoái ở phương trình 1.3 định lượng lý do tại sao hệ thống ML lại bị xói mòn. Một hệ thống đề xuất được triển khai ở độ chính xác 85 phần trăm sẽ giảm xuống còn 80.2 phần trăm trong vòng 6 tháng khi các mô hình mua hàng thay đổi, đánh mất 4.8 điểm phần trăm mà không có bất kỳ thay đổi nào trong mã nguồn. Vòng đời phát triển ML (phần 1.10.1) cho thấy việc giám sát và huấn luyện lại liên tục là những yêu cầu vận hành. Các hệ thống phát hiện gian lận và NLP đối mặt với quy luật tương tự: những kẻ tấn công thích ứng, vốn từ vựng thay đổi, và hành vi của người dùng cũng thay đổi, trong khi mã nguồn thì giữ nguyên. Nếu không có giám sát, hệ thống có thể trông có vẻ khỏe mạnh trong khi chất lượng dự đoán dần xói mòn. Các tổ chức coi triển khai là công việc thực hiện một lần thường chỉ phát hiện hỏng hóc sau những khiếu nại của khách hàng hoặc khi các số liệu (metrics) ở hạ nguồn bộc lộ sự suy giảm hiệu suất.
Cạm bẫy: Cho rằng chuyên môn ML đơn thuần là đủ cho kỹ thuật hệ thống ML.
Các tổ chức tuyển dụng các nhà nghiên cứu ML và kỳ vọng sẽ có những hệ thống sẵn sàng cho sản xuất, nhưng năm chuyên ngành kỹ thuật (phần 1.12.1) yêu cầu kiến thức chuyên môn tích hợp (integrated expertise) qua cả thuật toán, phần mềm, hệ thống, và vận hành. Các nhóm có kỹ năng ML mạnh nhưng lại ít kinh nghiệm về hệ thống có thể lỡ mất mục tiêu về thông lượng (throughput) bởi vì thiết kế API, cấu trúc lưu trữ (storage layout), và cơ sở hạ tầng phục vụ sẽ định hình hiệu suất thực tế đạt được. Ngược lại, cơ sở hạ tầng phần mềm được xây dựng thiếu nhận thức về ML có thể tạo ra các lỗi (bugs) trong đặc trưng (feature) hoặc quá trình tiền xử lý, làm suy giảm hành vi của mô hình mà không có dấu hiệu hỏng hóc hệ thống rõ ràng. Các nghiên cứu tình huống triển khai cho thấy ML sản xuất cần có sự chú ý phối hợp đến cả dữ liệu, mô hình, cơ sở hạ tầng, và luồng công việc tổ chức, chứ không chỉ là chất lượng thuật toán đơn thuần (Paleyes et al. 2022). Các nhóm hiệu quả sẽ kết hợp các nhà nghiên cứu ML, kỹ sư phần mềm, và chuyên gia vận hành thay vì kỳ vọng một vai trò có thể làm chủ tất cả các kỹ năng.
Phần tóm tắt kéo những sai lầm này trở lại khẳng định trọng tâm của chương: ML


================ PAGE 72 ================

34
1.15 Tóm tắt (Summary)
kỹ thuật hệ thống tồn tại bởi vì hành vi học được (learned behavior), cơ sở hạ tầng vật lý, và quy trình làm việc tổ chức phải được thiết kế cùng nhau.
1.15 Tóm tắt (Summary)
Phần giới thiệu này đã thiết lập nền tảng khái niệm cho mọi thứ sẽ theo sau. Chương đã bắt đầu với khoảnh khắc AI (AI moment) và sự chuyển dịch Phần mềm 2.0 (Software 2.0): các hệ thống ML khác với phần mềm truyền thống bởi vì hành vi của chúng được học từ dữ liệu và có thể suy thoái thầm lặng khi các phân phối thay đổi. Sau đó, nó lần theo lịch sử mô hình của AI và bài học đắng cay (the bitter lesson), cho thấy lý do tại sao tiến bộ liên tục đến từ các hệ thống có thể tận dụng nhiều tính toán hơn thay vì từ chuyên môn được mã hóa thủ công (hand-coded expertise). Chương này đã chính thức hóa các hệ thống ML thông qua hệ phân loại D·A·M, sau đó giới thiệu phương trình suy thoái, quy luật sắt, và các khuôn khổ năng lượng và hiệu suất như những lăng kính định lượng để chẩn đoán.
Với các công cụ đó, chương này đã định nghĩa kỹ thuật AI như một chuyên ngành kỹ thuật xây dựng các hệ thống ngẫu nhiên (stochastic) đạt độ tin cậy tất định (deterministic reliability targets), thỏa mãn đồng thời ba ràng buộc D·A·M trên khắp các nền tảng tính toán. Sau đó, nó ánh xạ vòng đời phát triển ML, phổ triển khai, và các nghiên cứu tình huống sản xuất từ huấn luyện đám mây đến TinyML, cho thấy lý do tại sao sự lặp lại liên tục và thiết kế nhận thức bối cảnh (context-aware design) là yêu cầu bắt buộc chứ không phải là sự lựa chọn. Năm Mô hình Ngọn hải đăng được giới thiệu tại đây (ResNet-50, GPT-2/Llama, MobileNetV2, DLRM, và Phát hiện Từ đánh thức, được trình bày chi tiết trong Chương 6) đóng vai trò như những chuẩn mực (touchstones) lặp đi lặp lại trong các chương tiếp theo, gắn các nguyên tắc trừu tượng vào các thách thức kỹ thuật cụ thể của những khối lượng công việc thực tế.
Các nguyên tắc và khuôn khổ được thiết lập trong phần giới thiệu này cung cấp từ vựng khái niệm cho mọi thứ tiếp theo. Chúng cũng trả lời cho câu hỏi được đặt ra ngay từ đầu: việc xây dựng các hệ thống học máy đòi hỏi những nguyên tắc kỹ thuật khác biệt bởi vì những hệ thống này lấy hành vi của chúng từ dữ liệu thay vì từ mã nguồn, suy thoái thầm lặng thay vì hỏng hóc rõ ràng, và đòi hỏi sự thiết kế đồng bộ (co-design) giữa thuật toán, phần mềm, và phần cứng ở mọi giai đoạn. Đó là nhiệm vụ của kỹ thuật AI: thuần hóa hành vi ngẫu nhiên này bằng độ tin cậy tất định. Hệ phân loại D·A·M cung cấp một lăng kính có hệ thống để phân tích bất kỳ thách thức nào của hệ thống ML, trong khi năm Mô hình Ngọn hải đăng đưa những khái niệm trừu tượng này vào các vấn đề kỹ thuật cụ thể thường gặp trong suốt sự nghiệp của một người thực hành.
Những Điểm Chính rút ra: Các ràng buộc định hướng kiến trúc
• Nút thắt cổ chai D·A·M dịch chuyển, không biến mất: Ràng buộc Dữ liệu, Thuật toán, và Máy móc tương tác với nhau, vì vậy việc cải thiện một trục thường phơi bày nút thắt ở một trục khác. Thói quen của kỹ thuật hệ thống là hỏi xem trục nào hiện đang bị ràng buộc (binds), sau đó chọn sự can thiệp làm giảm ràng buộc đó mà không tạo ra một lỗi lớn hơn ở hạ nguồn.
• Hành vi học được sẽ bị suy thoái thầm lặng: Phần mềm truyền thống thường bị hỏng khi mã nguồn thay đổi; hệ thống ML có thể bị xói mòn trong khi mã nguồn và cơ sở hạ tầng vẫn cố định bởi vì thế giới thay đổi làm lệch so với phân phối huấn luyện. Phương trình suy thoái biến sự trôi dạt đó thành các kích hoạt huấn luyện lại (retraining triggers) thay vì để độ chính xác giảm bất ngờ.
• Quy luật sắt làm cho độ trễ có tính chẩn đoán (diagnostic): Quá trình di chuyển dữ liệu, tính toán, và những chi phí phát sinh (overhead) đều tiêu tốn từ cùng một ngân sách thời gian. Việc giảm suy luận từ 45 ms xuống 15 ms chỉ mang lại 23 phần trăm cải thiện khi tiền xử lý (60 ms) và hậu xử lý (25 ms) đang chiếm ưu thế, do đó hãy tối ưu hóa yếu tố đang ràng buộc hành vi đầu cuối.
• Quy mô sẽ chiến thắng bên trong các giới hạn vật lý: Bài học đắng cay giải thích tại sao các phương pháp tổng quát hóa sử dụng nhiều tính toán hơn lại đánh bật các hệ thống được tạo thủ công, nhưng quy mô chỉ phát huy tác dụng khi dữ liệu, kiến trúc, và máy móc có thể hỗ trợ nó. Những cải tiến hiệu suất gấp 44.5 lần đã cùng tồn tại với khoảng 7 cấp số nhân về tăng trưởng tính toán.
• Kỹ thuật AI là thiết kế đồng bộ liên tục: Bối cảnh triển khai, giám sát vòng đời, và năm trụ cột kỹ thuật không phải là những tiện ích bổ sung (add-ons) về sau; chúng là cách để hành vi học được ngẫu nhiên duy trì được các mục tiêu độ tin cậy tất định, từ huấn luyện đám mây cho đến hoạt động TinyML.
Mọi thứ chương này đã giới thiệu đều hướng tới một khẳng định mà phần còn lại của cuốn sách sẽ bám sát: một hệ thống học máy bị chi phối bởi tính chất vật lý, không phải bởi ý định. Phần mềm truyền thống thực hiện những gì nó được viết ra; một hệ thống học máy thực hiện những gì dữ liệu, số học, và phần cứng của nó


================ PAGE 73 ================

1. Giới thiệu
35
cho phép, và ba yếu tố đó hiếm khi đồng ý với những hy vọng của lập trình viên. Bài học đắng cay, quy luật sắt, phương trình suy thoái, và hệ phân loại D·A·M không phải là những dữ kiện tách rời để ghi nhớ, mà là một từ vựng duy nhất cho sự chuyển đổi đó, một cách để lý luận về hành vi được phát triển (grown) chứ không phải được mã hóa (coded), và sẽ bị xói mòn trừ phi nó được bảo trì. Kỹ thuật một hệ thống như vậy là coi các ràng buộc của nó như đặc tả thực sự (real specification), và đó là điều biến một tập hợp các kỹ thuật trở thành một chuyên ngành học.
Tiếp theo là gì: Từ tầm nhìn (vision) đến kiến trúc
Một mô hình ML thực sự nên chạy ở đâu? Các định luật vật lý quyết định những gì khả thi. Tốc độ ánh sáng làm cho các máy chủ đám mây xa xôi trở nên vô dụng đối với việc phanh khẩn cấp. Nhiệt động lực học ngăn cản các mô hình quy mô trung tâm dữ liệu chạy trên một thiết bị di động. Các tính chất vật lý của bộ nhớ tạo ra những giới hạn băng thông (bandwidth ceilings) mà các con chip nhanh hơn không thể vượt qua. Bốn mô hình triển khai (deployment paradigms) chính là nơi các định luật đó thể hiện: Chương 2 xuất phát (derives) phạm vi hoạt động (operating envelope) của từng mô hình từ các tính chất vật lý và phát triển khuôn khổ quyết định (decision framework) cho việc lựa chọn giữa chúng khi các yêu cầu xung đột nhau.
Câu hỏi Nghiên cứu: Dành cho sự tìm hiểu sâu hơn
• Làm thế nào một kỹ sư chẩn đoán được liệu một lỗi của hệ thống ML đến từ Dữ liệu, Thuật toán, Máy móc, hay từ sự tương tác của chúng?
• Khi nào bài học đắng cay không còn là một hướng dẫn đủ tốt vì các ràng buộc về tính toán, năng lượng, dữ liệu, hoặc triển khai chiếm ưu thế?
• Các mục tiêu độ tin cậy nên được đặc tả (specified) như thế nào đối với các hệ thống có hành vi học được từ dữ liệu và có thể trôi dạt sau khi triển khai?
• Khi nào thì một mô hình đơn giản hơn, kém chính xác hơn lại là một hệ thống sản xuất tốt hơn một khi đã xem xét đến độ trễ, năng lượng, và vòng lặp phản hồi vòng đời?


================ PAGE 74 ================



================ PAGE 75 ================

I
NỀN TẢNG CỦA CÁC HỆ THỐNG ML
Phần I


================ PAGE 76 ================



================ PAGE 77 ================

Các Nguyên tắc Nền tảng (Foundation Principles)
Các hệ thống học máy tuân theo một định luật bảo toàn tưởng chừng đơn giản: độ phức tạp không thể bị triệt tiêu, mà chỉ có thể bị di chuyển. Độ phức tạp luân chuyển qua lại giữa ba miền của hệ phân loại D·A·M: Dữ liệu (Data) với tư cách là thông tin, Thuật toán (Algorithm) với tư cách là logic, và Máy móc (Machine) với tư cách là tính chất vật lý. Việc đơn giản hóa một miền tất yếu sẽ tạo thêm gánh nặng cho các miền khác. Một đường ống đặc trưng (feature pipeline) được xây dựng thủ công làm giảm độ phức tạp của thuật toán nhưng lại đòi hỏi nhiều nỗ lực kỹ thuật dữ liệu hơn. Một mô hình lớn hơn sẽ hấp thụ được dữ liệu lộn xộn nhưng lại chuyển gánh nặng độ phức tạp sang phần cứng dùng để huấn luyện và phục vụ nó. Định luật Bảo toàn Độ phức tạp (Conservation of Complexity) này chính là siêu nguyên tắc (meta-principle) thúc đẩy mọi thứ trong cuốn sách này. Các bất biến định lượng (quantitative invariants) được giới thiệu xuyên suốt cuốn sách là những biểu hiện cụ thể có thể đo lường được của nó: mỗi bất biến định lượng hóa một ràng buộc nảy sinh từ nơi mà độ phức tạp hiện đang cư trú.
Các kiến trúc, khuôn khổ, và kỹ thuật tối ưu hóa chỉ thành công khi chúng tôn trọng các ràng buộc bất biến do phần cứng, toán học, và lý thuyết thông tin áp đặt. Giống như các kỹ sư xây dựng không thể phớt lờ trọng lực, các kỹ sư ML không thể phớt lờ các định luật vật lý chi phối dữ liệu, tính toán, và thông lượng hệ thống. Phần I thiết lập những ràng buộc bất biến này: không phải là các phương pháp thực hành tốt nhất (best practices) vốn thay đổi theo các khuôn khổ (frameworks) hay những quan điểm khác biệt giữa các nhóm, mà là các tính chất vật lý của kỹ thuật ML. Ràng buộc đầu tiên bắt đầu từ chính dữ liệu, nơi ranh giới quen thuộc giữa chương trình và dữ liệu đầu vào bắt đầu biến mất.
Nguyên tắc 1: Bất biến Dữ liệu dưới dạng Mã nguồn (Data as Code Invariant)
Bất biến: Dữ liệu là mã nguồn của hệ thống ML. Sự thay đổi đối với tập dữ liệu huấn luyện tương đương về mặt chức năng với sự thay đổi trong logic thực thi (ΔProgram).
Hành_vi_Hệ_thống ≈ 𝑓(Dữ_liệu)
Hệ quả: Kỹ thuật dữ liệu đòi hỏi sự nghiêm ngặt tương tự như kỹ thuật phần mềm. Các tập dữ liệu phải được lập phiên bản (như Git), kiểm thử đơn vị (kiểm tra chất lượng dữ liệu), và gỡ lỗi (debugged). Xóa một hàng dữ liệu huấn luyện tương đương với việc xóa một dòng mã nguồn; huấn luyện lại (retraining) sẽ xây dựng lại cấu phần đã học (learned artifact) từ tài liệu nguồn đã bị thay đổi.
Nếu dữ liệu là mã nguồn, thì nó không chỉ thuần túy là một tạo tác logic (logical artifact)—nó còn mang những thuộc tính vật lý ràng buộc kiến trúc hệ thống. Không giống như mã nguồn, vốn có thể được sao chép và phân phối tự do, dữ liệu kháng cự lại sự di chuyển, và quy mô của nó làm thay đổi vị trí nơi việc tính toán nên diễn ra.
Nguyên tắc 2: Bất biến Trọng lực Dữ liệu (Data Gravity Invariant)
Bất biến: Dữ liệu có khối lượng. Khi khối lượng dữ liệu (𝐷_vol) tăng lên, chi phí (độ trễ, băng thông, năng lượng) cho việc di chuyển dữ liệu vượt xa chi phí di chuyển sự tính toán.
𝐶_move(𝐷_vol) ≫ 𝐶_move(Tính_toán)
Hệ quả: Các tập dữ liệu lớn trở thành tâm hấp dẫn (gravitational center) của kiến trúc. Các hệ thống ngày càng chuyển việc tính toán về phía dữ liệu bằng cách gửi (shipping) các truy vấn hoặc mã nguồn tới lớp lưu trữ, thay vì chuyển dữ liệu về phía tính toán bằng cách liên tục tải xuống các tập dữ liệu lớn.
39


================ PAGE 78 ================

40
Các Nguyên tắc Nền tảng
Cùng với nhau, hai bất biến này xác lập rằng dữ liệu vừa là chương trình logic vừa là mỏ neo vật lý của mọi hệ thống ML. Với những nền tảng đã được thiết lập, Phần I xây dựng nên một bộ khung khái niệm: từ nguồn gốc của chuyên ngành và các số đo (metrics) cốt lõi, qua các ràng buộc vật lý định hình nên phổ triển khai, đến vòng đời quản lý sự phức tạp qua các giai đoạn, và cuối cùng là các thực tiễn kỹ thuật đối xử với dữ liệu bằng sự nghiêm ngặt mà nó đòi hỏi.


================ PAGE 79 ================