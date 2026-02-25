# Chương 1: Giới Thiệu

Hiệu năng máy tính là một lĩnh vực thú vị, đa dạng và đầy thách thức. Chương này giới thiệu cho bạn về lĩnh vực hiệu năng hệ thống. Các mục tiêu học tập của chương này bao gồm:

- Hiểu về hiệu năng hệ thống, các vai trò, hoạt động và thách thức.
- Hiểu sự khác biệt giữa các công cụ quan sát (observability) và các công cụ thực nghiệm (experimental).
- Phát triển hiểu biết cơ bản về khả năng quan sát hiệu năng: thống kê, profiling, flame graph, tracing, instrumentation tĩnh và instrumentation động.
- Tìm hiểu vai trò của các phương pháp luận và danh sách kiểm tra 60 giây trên Linux.

Các tham chiếu đến những chương sau được đưa vào để chương này vừa là phần giới thiệu về hiệu năng hệ thống, vừa là phần giới thiệu về cuốn sách. Chương này kết thúc với các nghiên cứu tình huống (case study) để cho thấy hiệu năng hệ thống hoạt động như thế nào trong thực tế.

## 1.1 Hiệu Năng Hệ Thống (Systems Performance)

Hiệu năng hệ thống nghiên cứu hiệu năng của toàn bộ hệ thống máy tính, bao gồm tất cả các thành phần phần mềm và phần cứng chính. Bất kỳ thứ gì nằm trên đường dữ liệu (data path), từ thiết bị lưu trữ đến phần mềm ứng dụng, đều được bao gồm, vì chúng đều có thể ảnh hưởng đến hiệu năng. Đối với các hệ thống phân tán (distributed systems), điều này có nghĩa là nhiều máy chủ và ứng dụng. Nếu bạn chưa có sơ đồ môi trường của mình thể hiện đường dữ liệu, hãy tìm hoặc tự vẽ một sơ đồ; điều này sẽ giúp bạn hiểu mối quan hệ giữa các thành phần và đảm bảo rằng bạn không bỏ sót bất kỳ khu vực nào.

Các mục tiêu điển hình của hiệu năng hệ thống là cải thiện trải nghiệm người dùng cuối bằng cách giảm độ trễ (latency) và giảm chi phí tính toán. Giảm chi phí có thể đạt được bằng cách loại bỏ các điểm không hiệu quả, cải thiện thông lượng (throughput) hệ thống, và tinh chỉnh tổng thể (general tuning).

Hình 1.1 cho thấy một ngăn xếp phần mềm hệ thống (software stack) tổng quát trên một máy chủ đơn, bao gồm nhân hệ điều hành (OS kernel), với các tầng cơ sở dữ liệu và ứng dụng làm ví dụ. Thuật ngữ *full stack* đôi khi chỉ dùng để mô tả môi trường ứng dụng, bao gồm cơ sở dữ liệu, ứng dụng và máy chủ web. Tuy nhiên, khi nói về hiệu năng hệ thống, chúng ta sử dụng *full stack* để chỉ toàn bộ ngăn xếp phần mềm từ ứng dụng xuống đến kim loại (phần cứng), bao gồm các thư viện hệ thống, nhân (kernel) và chính phần cứng. Hiệu năng hệ thống nghiên cứu toàn bộ ngăn xếp (full stack).

*Hình 1.1: Ngăn xếp phần mềm hệ thống tổng quát*

Trình biên dịch (compiler) cũng được đưa vào Hình 1.1 vì chúng đóng vai trò trong hiệu năng hệ thống. Ngăn xếp này được thảo luận trong Chương 3, Hệ Điều Hành, và được khảo sát chi tiết hơn trong các chương sau. Các phần tiếp theo mô tả hiệu năng hệ thống chi tiết hơn.

## 1.2 Các Vai Trò (Roles)

Hiệu năng hệ thống được thực hiện bởi nhiều vai trò công việc khác nhau, bao gồm quản trị viên hệ thống, kỹ sư độ tin cậy site (SRE), nhà phát triển ứng dụng, kỹ sư mạng, quản trị viên cơ sở dữ liệu, quản trị viên web và các nhân viên hỗ trợ khác. Đối với nhiều vai trò trong số này, hiệu năng chỉ là một phần của công việc, và phân tích hiệu năng tập trung vào lĩnh vực trách nhiệm của vai trò đó: đội mạng kiểm tra mạng, đội cơ sở dữ liệu kiểm tra cơ sở dữ liệu, v.v. Đối với một số vấn đề hiệu năng, việc tìm nguyên nhân gốc rễ (root cause) hoặc các yếu tố góp phần đòi hỏi sự phối hợp từ nhiều đội.

Một số công ty tuyển dụng kỹ sư hiệu năng (performance engineers), có hoạt động chính là hiệu năng. Họ có thể làm việc với nhiều đội để thực hiện nghiên cứu toàn diện (holistic study) về môi trường, một cách tiếp cận có thể rất quan trọng trong việc giải quyết các vấn đề hiệu năng phức tạp. Họ cũng có thể đóng vai trò như nguồn lực trung tâm để tìm kiếm và phát triển các công cụ tốt hơn cho phân tích hiệu năng và hoạch định dung lượng (capacity planning) trên toàn bộ môi trường.

Ví dụ, Netflix có một đội hiệu năng đám mây (cloud performance team), mà tôi là một thành viên. Chúng tôi hỗ trợ các đội microservice và SRE trong phân tích hiệu năng và xây dựng các công cụ hiệu năng cho mọi người sử dụng.

Các công ty tuyển nhiều kỹ sư hiệu năng có thể cho phép các cá nhân chuyên sâu vào một hoặc nhiều lĩnh vực, cung cấp mức hỗ trợ sâu hơn. Ví dụ, một đội kỹ thuật hiệu năng lớn có thể bao gồm các chuyên gia về hiệu năng nhân (kernel), hiệu năng phía client, hiệu năng ngôn ngữ (ví dụ: Java), hiệu năng runtime (ví dụ: JVM), công cụ hiệu năng, và nhiều hơn nữa.

## 1.3 Các Hoạt Động (Activities)

Hiệu năng hệ thống bao gồm nhiều hoạt động khác nhau. Dưới đây là danh sách các hoạt động cũng đồng thời là các bước lý tưởng trong vòng đời của một dự án phần mềm từ khái niệm qua phát triển đến triển khai sản xuất (production deployment). Các phương pháp luận và công cụ để hỗ trợ thực hiện các hoạt động này được đề cập trong cuốn sách này.

1. Đặt mục tiêu hiệu năng và mô hình hóa hiệu năng cho sản phẩm tương lai.
2. Đánh giá đặc tính hiệu năng (performance characterization) của phần mềm và phần cứng nguyên mẫu.
3. Phân tích hiệu năng của sản phẩm đang phát triển trong môi trường thử nghiệm.
4. Kiểm thử phi hồi quy (non-regression testing) cho các phiên bản sản phẩm mới.
5. Đo hiệu năng chuẩn (benchmarking) các bản phát hành sản phẩm.
6. Kiểm thử proof-of-concept trong môi trường sản xuất mục tiêu.
7. Tinh chỉnh hiệu năng (performance tuning) trong sản xuất.
8. Giám sát phần mềm sản xuất đang chạy.
9. Phân tích hiệu năng các sự cố sản xuất.
10. Đánh giá sự cố (incident review) cho các vấn đề sản xuất.
11. Phát triển công cụ hiệu năng để nâng cao phân tích sản xuất.

Các bước 1 đến 5 bao gồm phát triển sản phẩm truyền thống, dù là sản phẩm bán cho khách hàng hay dịch vụ nội bộ công ty. Sản phẩm sau đó được ra mắt, có thể ban đầu với kiểm thử proof-of-concept trong môi trường mục tiêu (khách hàng hoặc nội bộ), hoặc có thể đi thẳng vào triển khai và cấu hình. Nếu một vấn đề gặp phải trong môi trường mục tiêu (bước 6 đến 9), điều đó có nghĩa là vấn đề không được phát hiện hoặc sửa chữa trong các giai đoạn phát triển.

Kỹ thuật hiệu năng (performance engineering) lý tưởng nên bắt đầu trước khi bất kỳ phần cứng nào được chọn hoặc phần mềm nào được viết: bước đầu tiên nên là đặt mục tiêu và tạo mô hình hiệu năng. Tuy nhiên, sản phẩm thường được phát triển mà không có bước này, trì hoãn công việc kỹ thuật hiệu năng đến thời điểm sau, sau khi một vấn đề phát sinh. Với mỗi bước của quy trình phát triển, việc sửa các vấn đề hiệu năng phát sinh do các quyết định kiến trúc được đưa ra trước đó có thể ngày càng khó khăn hơn.

Điện toán đám mây cung cấp các kỹ thuật mới cho kiểm thử proof-of-concept (bước 6) khuyến khích bỏ qua các bước trước đó (bước 1 đến 5). Một kỹ thuật như vậy là thử nghiệm phần mềm mới trên một instance duy nhất với một phần nhỏ khối lượng công việc sản xuất: đây được gọi là **canary testing**. Một kỹ thuật khác biến điều này thành bước bình thường trong triển khai phần mềm: lưu lượng được chuyển dần sang một pool instance mới trong khi giữ pool cũ trực tuyến làm bản dự phòng; đây được gọi là **blue-green deployment**.¹ Với các tùy chọn cho phép thất bại an toàn (safe-to-fail) như vậy, phần mềm mới thường được thử nghiệm trong sản xuất mà không có bất kỳ phân tích hiệu năng nào trước đó, và nhanh chóng hoàn nguyên (revert) nếu cần. Tôi khuyến nghị rằng, khi thực tế cho phép, bạn cũng nên thực hiện các hoạt động trước đó để có thể đạt được hiệu năng tốt nhất (mặc dù có thể có lý do thời gian ra thị trường để chuyển sang sản xuất sớm hơn).

> ¹ Netflix sử dụng thuật ngữ red-black deployments.

Thuật ngữ **hoạch định dung lượng** (capacity planning) có thể đề cập đến một số hoạt động nói trên. Trong giai đoạn thiết kế, nó bao gồm nghiên cứu dấu chân tài nguyên (resource footprint) của phần mềm đang phát triển để xem thiết kế có thể đáp ứng nhu cầu mục tiêu tốt như thế nào. Sau khi triển khai, nó bao gồm giám sát việc sử dụng tài nguyên để dự đoán các vấn đề trước khi chúng xảy ra.

Phân tích hiệu năng các sự cố sản xuất (bước 9) cũng có thể liên quan đến các kỹ sư độ tin cậy site (SRE); bước này được theo sau bởi các cuộc họp đánh giá sự cố (incident review meetings) (bước 10) để phân tích những gì đã xảy ra, chia sẻ kỹ thuật debug, và tìm cách tránh cùng sự cố trong tương lai. Các cuộc họp như vậy tương tự như các buổi retrospective của nhà phát triển (xem [Corry 20] về retrospective và các anti-pattern của chúng).

Các môi trường và hoạt động khác nhau giữa các công ty và sản phẩm, và trong nhiều trường hợp không phải tất cả mười bước đều được thực hiện. Công việc của bạn cũng có thể chỉ tập trung vào một số hoặc chỉ một trong các hoạt động này.

## 1.4 Các Góc Nhìn (Perspectives)

Ngoài việc tập trung vào các hoạt động khác nhau, các vai trò hiệu năng có thể được xem từ các góc nhìn khác nhau. Hai góc nhìn cho phân tích hiệu năng được ghi nhãn trong Hình 1.2: phân tích khối lượng công việc (workload analysis) và phân tích tài nguyên (resource analysis), tiếp cận ngăn xếp phần mềm từ các hướng khác nhau.

*Hình 1.2: Các góc nhìn phân tích*

Góc nhìn **phân tích tài nguyên** thường được sử dụng bởi các quản trị viên hệ thống, những người chịu trách nhiệm về các tài nguyên hệ thống. Các nhà phát triển ứng dụng, những người chịu trách nhiệm về hiệu năng được cung cấp của khối lượng công việc, thường tập trung vào góc nhìn **phân tích khối lượng công việc**. Mỗi góc nhìn có những thế mạnh riêng, được thảo luận chi tiết trong Chương 2, Phương Pháp Luận. Đối với các vấn đề khó, việc thử phân tích từ cả hai góc nhìn sẽ rất hữu ích.

## 1.5 Hiệu Năng Là Một Thách Thức (Performance Is Challenging)

Kỹ thuật hiệu năng hệ thống là một lĩnh vực đầy thách thức vì nhiều lý do, bao gồm tính chủ quan, sự phức tạp, có thể không có một nguyên nhân gốc rễ duy nhất, và thường liên quan đến nhiều vấn đề.

### 1.5.1 Tính Chủ Quan (Subjectivity)

Các ngành công nghệ có xu hướng khách quan, đến mức những người trong ngành được biết đến là thấy mọi thứ đen trắng rõ ràng. Điều này có thể đúng với việc xử lý sự cố phần mềm, khi một bug hoặc có mặt hoặc vắng mặt và hoặc được sửa hoặc chưa được sửa. Những bug như vậy thường biểu hiện dưới dạng thông báo lỗi có thể dễ dàng giải thích và hiểu là sự hiện diện của một lỗi.

Mặt khác, hiệu năng thường mang tính chủ quan. Với các vấn đề hiệu năng, có thể không rõ liệu có vấn đề ngay từ đầu hay không, và nếu có, khi nào nó được sửa. Những gì có thể được coi là hiệu năng "tệ" đối với một người dùng, và do đó là một vấn đề, có thể được coi là hiệu năng "tốt" đối với người khác.

Hãy xem xét thông tin sau:

> Thời gian phản hồi I/O đĩa trung bình là 1 ms.

Đây là "tốt" hay "tệ"? Mặc dù thời gian phản hồi, hay độ trễ (latency), là một trong những chỉ số tốt nhất có sẵn, việc giải thích thông tin độ trễ là khó khăn. Ở một mức độ nào đó, liệu một chỉ số nhất định là "tốt" hay "tệ" có thể phụ thuộc vào kỳ vọng hiệu năng của các nhà phát triển ứng dụng và người dùng cuối.

Hiệu năng chủ quan có thể được làm cho khách quan bằng cách định nghĩa các mục tiêu rõ ràng, chẳng hạn như có thời gian phản hồi trung bình mục tiêu, hoặc yêu cầu một tỷ lệ phần trăm yêu cầu nằm trong một phạm vi độ trễ nhất định. Các cách khác để xử lý tính chủ quan này được giới thiệu trong Chương 2, Phương Pháp Luận, bao gồm phân tích độ trễ.

### 1.5.2 Sự Phức Tạp (Complexity)

Ngoài tính chủ quan, hiệu năng có thể là một lĩnh vực đầy thách thức do sự phức tạp của hệ thống và thiếu điểm khởi đầu rõ ràng cho phân tích. Trong các môi trường điện toán đám mây, bạn có thể thậm chí không biết nên xem instance máy chủ nào trước. Đôi khi chúng ta bắt đầu với một giả thuyết, chẳng hạn như đổ lỗi cho mạng hoặc cơ sở dữ liệu, và nhà phân tích hiệu năng phải tìm hiểu xem đây có phải hướng đi đúng hay không.

Các vấn đề hiệu năng cũng có thể bắt nguồn từ các tương tác phức tạp giữa các hệ thống con mà vốn hoạt động tốt khi được phân tích riêng lẻ. Điều này có thể xảy ra do sự cố dây chuyền (cascading failure), khi một thành phần bị lỗi gây ra vấn đề hiệu năng cho các thành phần khác. Để hiểu vấn đề kết quả, bạn phải gỡ rối các mối quan hệ giữa các thành phần và hiểu cách chúng đóng góp.

Các nút thắt cổ chai (bottleneck) cũng có thể phức tạp và liên quan theo những cách bất ngờ; sửa một nút thắt có thể chỉ đơn giản là chuyển nút thắt sang nơi khác trong hệ thống, với hiệu năng tổng thể không cải thiện nhiều như mong đợi.

Ngoài sự phức tạp của hệ thống, các vấn đề hiệu năng cũng có thể được gây ra bởi đặc tính phức tạp của khối lượng công việc sản xuất. Những trường hợp này có thể không bao giờ tái tạo được trong môi trường phòng thí nghiệm, hoặc chỉ tái tạo được không liên tục.

Giải quyết các vấn đề hiệu năng phức tạp thường đòi hỏi cách tiếp cận toàn diện (holistic approach). Toàn bộ hệ thống — cả nội bộ và các tương tác bên ngoài — có thể cần được điều tra. Điều này đòi hỏi nhiều kỹ năng đa dạng, và có thể làm cho kỹ thuật hiệu năng trở thành một lĩnh vực công việc đa dạng và thách thức về mặt trí tuệ.

Các phương pháp luận khác nhau có thể được sử dụng để hướng dẫn chúng ta vượt qua những phức tạp này, như được giới thiệu trong Chương 2; Chương 6 đến 10 bao gồm các phương pháp luận cụ thể cho các tài nguyên hệ thống cụ thể: CPU, Bộ nhớ, Hệ thống File, Đĩa và Mạng. (Phân tích các hệ thống phức tạp nói chung, bao gồm tràn dầu và sụp đổ hệ thống tài chính, đã được nghiên cứu bởi [Dekker 18].)

Trong một số trường hợp, vấn đề hiệu năng có thể được gây ra bởi sự tương tác của các tài nguyên này.

### 1.5.3 Nhiều Nguyên Nhân (Multiple Causes)

Một số vấn đề hiệu năng không có một nguyên nhân gốc rễ duy nhất, mà thay vào đó có nhiều yếu tố góp phần. Hãy tưởng tượng một kịch bản trong đó ba sự kiện bình thường xảy ra đồng thời và kết hợp để gây ra vấn đề hiệu năng: mỗi sự kiện là một sự kiện bình thường mà khi xảy ra riêng lẻ không phải là nguyên nhân gốc rễ.

Ngoài nhiều nguyên nhân, cũng có thể có nhiều vấn đề hiệu năng.

### 1.5.4 Nhiều Vấn Đề Hiệu Năng (Multiple Performance Issues)

Tìm ra một vấn đề hiệu năng thường không phải là vấn đề; trong phần mềm phức tạp thường có rất nhiều. Để minh họa điều này, hãy thử tìm cơ sở dữ liệu bug cho hệ điều hành hoặc ứng dụng của bạn và tìm kiếm từ *performance*. Bạn có thể ngạc nhiên! Thông thường, sẽ có một số vấn đề hiệu năng đã biết nhưng chưa được sửa, ngay cả trong phần mềm hoàn thiện được coi là có hiệu năng cao. Điều này đặt ra thêm một khó khăn khi phân tích hiệu năng: nhiệm vụ thực sự không phải là tìm một vấn đề; mà là xác định vấn đề hoặc các vấn đề nào quan trọng nhất.

Để làm điều này, nhà phân tích hiệu năng phải định lượng mức độ nghiêm trọng của các vấn đề. Một số vấn đề hiệu năng có thể không áp dụng cho khối lượng công việc của bạn, hoặc chỉ áp dụng ở mức rất nhỏ. Lý tưởng nhất, bạn sẽ không chỉ định lượng các vấn đề mà còn ước tính tốc độ cải thiện tiềm năng (potential speedup) cho mỗi vấn đề. Thông tin này có thể có giá trị khi ban quản lý tìm kiếm lý do chính đáng để chi tiêu nguồn lực kỹ thuật hoặc vận hành.

Một chỉ số phù hợp cho việc định lượng hiệu năng, khi có sẵn, là độ trễ (latency).

## 1.6 Độ Trễ (Latency)

Độ trễ là thước đo thời gian chờ đợi, và là một chỉ số hiệu năng thiết yếu. Được sử dụng rộng rãi, nó có thể có nghĩa là thời gian để bất kỳ thao tác nào hoàn thành, chẳng hạn như một yêu cầu ứng dụng, một truy vấn cơ sở dữ liệu, một thao tác hệ thống file, v.v. Ví dụ, độ trễ có thể biểu thị thời gian để một trang web tải hoàn toàn, từ khi nhấp liên kết đến khi hiển thị trên màn hình. Đây là một chỉ số quan trọng cho cả khách hàng và nhà cung cấp trang web: độ trễ cao có thể gây ra sự thất vọng, và khách hàng có thể chuyển sang nơi khác.

Là một chỉ số, độ trễ cho phép ước tính tốc độ cải thiện tối đa. Ví dụ, Hình 1.3 mô tả một truy vấn cơ sở dữ liệu mất 100 ms (đó là độ trễ) trong đó nó dành 80 ms bị chặn chờ đọc đĩa. Cải thiện hiệu năng tối đa bằng cách loại bỏ đọc đĩa (ví dụ: bằng cache) có thể được tính toán: từ 100 ms xuống 20 ms (100 – 80) là nhanh hơn năm lần (5x). Đây là tốc độ cải thiện ước tính, và phép tính cũng đã định lượng vấn đề hiệu năng: đọc đĩa đang khiến truy vấn chạy chậm hơn tới 5 lần.

*Hình 1.3: Ví dụ về độ trễ I/O đĩa*

Phép tính như vậy không thể thực hiện được khi sử dụng các chỉ số khác. Số thao tác I/O mỗi giây (IOPS), ví dụ, phụ thuộc vào loại I/O và thường không thể so sánh trực tiếp. Nếu một thay đổi giảm tốc độ IOPS 80%, khó có thể biết tác động hiệu năng sẽ là gì. Có thể ít hơn 5 lần IOPS, nhưng nếu mỗi I/O tăng kích thước (byte) lên 10 lần thì sao?

Độ trễ cũng có thể mơ hồ nếu không có các thuật ngữ xác định. Ví dụ, trong mạng, độ trễ có thể có nghĩa là thời gian để thiết lập kết nối nhưng không phải thời gian truyền dữ liệu; hoặc nó có thể có nghĩa là tổng thời gian của kết nối, bao gồm cả truyền dữ liệu (ví dụ: độ trễ DNS thường được đo theo cách này). Xuyên suốt cuốn sách này, tôi sẽ sử dụng các thuật ngữ làm rõ khi có thể: những ví dụ đó sẽ được mô tả tốt hơn là *connection latency* (độ trễ kết nối) và *request latency* (độ trễ yêu cầu). Thuật ngữ độ trễ cũng được tóm tắt ở đầu mỗi chương.

Mặc dù độ trễ là một chỉ số hữu ích, nó không phải lúc nào cũng có sẵn khi và ở đâu cần thiết. Một số khu vực hệ thống chỉ cung cấp độ trễ trung bình; một số không cung cấp phép đo độ trễ nào cả. Với sự sẵn có của các công cụ quan sát dựa trên BPF² mới, độ trễ giờ đây có thể được đo từ các điểm quan tâm tùy ý tùy chỉnh và có thể cung cấp dữ liệu hiển thị toàn bộ phân phối của độ trễ.

> ² BPF giờ đây là một tên và không còn là viết tắt (ban đầu là Berkeley Packet Filter).

## 1.7 Khả Năng Quan Sát (Observability)

Khả năng quan sát đề cập đến việc hiểu một hệ thống thông qua quan sát, và phân loại các công cụ thực hiện điều này. Điều này bao gồm các công cụ sử dụng bộ đếm (counter), profiling và tracing. Nó không bao gồm các công cụ benchmark, vốn thay đổi trạng thái của hệ thống bằng cách thực hiện một thí nghiệm khối lượng công việc. Đối với môi trường sản xuất, các công cụ quan sát nên được thử trước bất cứ khi nào có thể, vì các công cụ thực nghiệm có thể gây nhiễu khối lượng công việc sản xuất thông qua tranh chấp tài nguyên. Đối với môi trường thử nghiệm đang nhàn rỗi, bạn có thể muốn bắt đầu với các công cụ benchmark để xác định hiệu năng phần cứng.

Trong phần này tôi sẽ giới thiệu bộ đếm, chỉ số, profiling và tracing. Tôi sẽ giải thích khả năng quan sát chi tiết hơn trong Chương 4, bao gồm khả năng quan sát toàn hệ thống so với từng tiến trình, các công cụ quan sát Linux và nội bộ của chúng. Chương 5 đến 11 bao gồm các phần đặc thù cho từng chương về khả năng quan sát, ví dụ, Phần 6.6 cho các công cụ quan sát CPU.

### 1.7.1 Bộ Đếm, Thống Kê và Chỉ Số (Counters, Statistics, and Metrics)

Ứng dụng và nhân (kernel) thường cung cấp dữ liệu về trạng thái và hoạt động của chúng: số lượng thao tác, số byte, phép đo độ trễ, mức sử dụng tài nguyên và tỷ lệ lỗi. Chúng thường được triển khai dưới dạng các biến số nguyên gọi là bộ đếm (counter) được mã hóa cứng trong phần mềm, một số trong đó là tích lũy (cumulative) và luôn tăng. Các bộ đếm tích lũy này có thể được đọc tại các thời điểm khác nhau bởi các công cụ hiệu năng để tính toán thống kê: tốc độ thay đổi theo thời gian, giá trị trung bình, phân vị (percentile), v.v.

Ví dụ, tiện ích vmstat(8) in ra tóm tắt toàn hệ thống về thống kê bộ nhớ ảo và nhiều hơn nữa, dựa trên các bộ đếm nhân trong hệ thống file /proc. Đầu ra vmstat(8) ví dụ này là từ một máy chủ API sản xuất 48-CPU:

```
$ vmstat 1 5
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r   b   swpd    free     buff   cache     si       so       bi       bo       in     cs us sy id wa st
19   0       0 6531592    42656 1672040         0        0        1        7     21     33 51   4 46   0   0
26   0       0 6533412    42656 1672064         0        0        0        0 81262 188942 54       4 43    0   0
62   0       0 6533856    42656 1672088         0        0        0        8 80865 180514 53       4 43    0   0
34   0       0 6532972    42656 1672088         0        0        0        0 81250 180651 53       4 43    0   0
31   0       0 6534876    42656 1672088         0        0        0        0 74389 168210 46       3 51    0   0
```

Kết quả này cho thấy mức sử dụng CPU toàn hệ thống khoảng 57% (cột cpu us + sy). Các cột được giải thích chi tiết trong Chương 6 và 7.

Một **chỉ số** (metric) là một thống kê đã được chọn để đánh giá hoặc giám sát một mục tiêu. Hầu hết các công ty sử dụng agent giám sát để ghi lại các thống kê được chọn (chỉ số) theo khoảng thời gian đều đặn, và biểu đồ hóa chúng trong giao diện đồ họa để xem các thay đổi theo thời gian. Phần mềm giám sát cũng có thể hỗ trợ tạo cảnh báo tùy chỉnh từ các chỉ số này, chẳng hạn như gửi email để thông báo nhân viên khi phát hiện vấn đề.

Thứ bậc từ bộ đếm đến cảnh báo được mô tả trong Hình 1.4. Hình 1.4 được cung cấp như một hướng dẫn để giúp bạn hiểu các thuật ngữ này, nhưng việc sử dụng chúng trong ngành không cứng nhắc. Các thuật ngữ bộ đếm, thống kê và chỉ số thường được sử dụng thay thế cho nhau. Ngoài ra, cảnh báo có thể được tạo ra bởi bất kỳ lớp nào, không chỉ một hệ thống cảnh báo chuyên dụng.

*Hình 1.4: Thuật ngữ đo lường hiệu năng*

Như một ví dụ về việc biểu đồ hóa chỉ số, Hình 1.5 là ảnh chụp màn hình của một công cụ dựa trên Grafana quan sát cùng máy chủ với đầu ra vmstat(8) trước đó.

*Hình 1.5: Giao diện GUI chỉ số hệ thống (Grafana)*

Các biểu đồ đường này hữu ích cho hoạch định dung lượng, giúp bạn dự đoán khi nào tài nguyên sẽ cạn kiệt.

Khả năng giải thích thống kê hiệu năng của bạn sẽ cải thiện với sự hiểu biết về cách chúng được tính toán. Thống kê, bao gồm giá trị trung bình, phân phối, mode và các giá trị ngoại lai (outlier), được tóm tắt trong Chương 2, Phương Pháp Luận, Phần 2.8, Thống Kê.

Đôi khi, các chỉ số chuỗi thời gian (time-series metrics) là tất cả những gì cần thiết để giải quyết một vấn đề hiệu năng. Biết chính xác thời điểm vấn đề bắt đầu có thể tương quan với một thay đổi phần mềm hoặc cấu hình đã biết, có thể được hoàn nguyên. Lần khác, chỉ số chỉ chỉ ra một hướng, gợi ý rằng có vấn đề CPU hoặc đĩa, nhưng không giải thích tại sao. Các công cụ profiling hoặc tracing là cần thiết để đào sâu hơn và tìm nguyên nhân.

### 1.7.2 Profiling

Trong hiệu năng hệ thống, thuật ngữ profiling thường đề cập đến việc sử dụng các công cụ thực hiện lấy mẫu (sampling): lấy một tập con (một mẫu) các phép đo để vẽ lên bức tranh tổng thể của mục tiêu. CPU là mục tiêu profiling phổ biến. Phương pháp thường được sử dụng để profile CPU bao gồm lấy mẫu theo khoảng thời gian định kỳ các đường dẫn mã (code path) đang chạy trên CPU.

Một cách trực quan hóa hiệu quả của CPU profile là **flame graph**. CPU flame graph có thể giúp bạn tìm được nhiều cải thiện hiệu năng hơn bất kỳ công cụ nào khác, sau các chỉ số. Chúng không chỉ tiết lộ các vấn đề CPU, mà còn các loại vấn đề khác, được tìm thấy bởi dấu chân CPU mà chúng để lại. Các vấn đề tranh chấp khóa (lock contention) có thể được tìm thấy bằng cách tìm kiếm thời gian CPU trong các đường dẫn spin; các vấn đề bộ nhớ có thể được phân tích bằng cách tìm thời gian CPU quá mức trong các hàm cấp phát bộ nhớ (malloc()), cùng với các đường dẫn mã dẫn đến chúng; các vấn đề hiệu năng liên quan đến cấu hình mạng sai có thể được phát hiện bằng cách thấy thời gian CPU trong các đường dẫn mã chậm hoặc cũ; v.v.

Hình 1.6 là một ví dụ CPU flame graph thể hiện các chu kỳ CPU được sử dụng bởi công cụ micro-benchmark mạng iperf(1).

*Hình 1.6: Profiling CPU sử dụng flame graph*

Flame graph này cho thấy bao nhiêu thời gian CPU được dành cho việc sao chép byte (đường dẫn kết thúc bằng copy_user_enhanced_fast_string()) so với truyền TCP (cột bên trái bao gồm tcp_write_xmit()). Độ rộng tỷ lệ thuận với thời gian CPU đã sử dụng, và trục dọc hiển thị đường dẫn mã.

Profiler được giải thích trong Chương 4, 5 và 6, và trực quan hóa flame graph được giải thích trong Chương 6, CPU, Phần 6.7.3, Flame Graph.

### 1.7.3 Tracing

Tracing là ghi lại dựa trên sự kiện, trong đó dữ liệu sự kiện được thu thập và lưu để phân tích sau hoặc được sử dụng ngay lập tức (on-the-fly) cho các tóm tắt tùy chỉnh và các hành động khác. Có các công cụ tracing chuyên dụng cho system call (ví dụ: Linux strace(1)) và gói mạng (ví dụ: Linux tcpdump(8)); và các công cụ tracing đa năng có thể phân tích việc thực thi của tất cả các sự kiện phần mềm và phần cứng (ví dụ: Linux Ftrace, BCC và bpftrace). Các tracer toàn diện này sử dụng nhiều nguồn sự kiện khác nhau, đặc biệt là instrumentation tĩnh và động, và BPF cho khả năng lập trình.

**Instrumentation Tĩnh (Static Instrumentation)**

Instrumentation tĩnh mô tả các điểm đo lường phần mềm được mã hóa cứng được thêm vào mã nguồn. Có hàng trăm điểm như vậy trong nhân Linux để đo lường I/O đĩa, sự kiện bộ lập lịch (scheduler), system call và nhiều hơn nữa. Công nghệ Linux cho instrumentation tĩnh nhân được gọi là **tracepoint**. Cũng có một công nghệ instrumentation tĩnh cho phần mềm không gian người dùng (user-space) gọi là **user statically defined tracing (USDT)**. USDT được sử dụng bởi các thư viện (ví dụ: libc) để đo lường các lời gọi thư viện và bởi nhiều ứng dụng để đo lường yêu cầu dịch vụ.

Như một ví dụ công cụ sử dụng instrumentation tĩnh, execsnoop(8) in ra các tiến trình mới được tạo trong khi nó đang tracing (chạy) bằng cách đo lường một tracepoint cho system call execve(2). Ví dụ sau cho thấy execsnoop(8) tracing một phiên đăng nhập SSH:

```
# execsnoop
PCOMM               PID     PPID    RET ARGS
ssh                 30656   20063      0 /usr/bin/ssh 0
sshd                30657   1401       0 /usr/sbin/sshd -D -R
sh                  30660   30657      0
env                 30661   30660      0 /usr/bin/env -i PATH=/usr/local/sbin:/usr/local...
run-parts           30661   30660      0 /bin/run-parts --lsbsysinit /etc/update-motd.d
00-header           30662   30661      0 /etc/update-motd.d/00-header
uname               30663   30662      0 /bin/uname -o
uname               30664   30662      0 /bin/uname -r
uname               30665   30662      0 /bin/uname -m
10-help-text        30666   30661      0 /etc/update-motd.d/10-help-text
50-motd-news        30667   30661      0 /etc/update-motd.d/50-motd-news
cat                 30668   30667      0 /bin/cat /var/cache/motd-news
cut                 30671   30667      0 /usr/bin/cut -c -80
tr                  30670   30667      0 /usr/bin/tr -d \000-\011\013\014\016-\037
head                30669   30667      0 /usr/bin/head -n 10
80-esm              30672   30661      0 /etc/update-motd.d/80-esm
lsb_release         30673   30672      0 /usr/bin/lsb_release -cs
[...]
```

Điều này đặc biệt hữu ích để phát hiện các tiến trình tồn tại ngắn (short-lived processes) có thể bị bỏ sót bởi các công cụ quan sát khác như top(1). Các tiến trình tồn tại ngắn này có thể là nguồn gây ra vấn đề hiệu năng.

Xem Chương 4 để biết thêm thông tin về tracepoint và USDT probe.

**Instrumentation Động (Dynamic Instrumentation)**

Instrumentation động tạo các điểm đo lường sau khi phần mềm đã chạy, bằng cách sửa đổi các lệnh trong bộ nhớ để chèn các routine đo lường. Điều này tương tự như cách debugger có thể chèn một breakpoint vào bất kỳ hàm nào trong phần mềm đang chạy. Debugger chuyển luồng thực thi sang debugger tương tác khi breakpoint được chạm, trong khi instrumentation động chạy một routine và sau đó tiếp tục phần mềm mục tiêu. Khả năng này cho phép tạo các thống kê hiệu năng tùy chỉnh từ bất kỳ phần mềm đang chạy nào. Các vấn đề mà trước đây không thể hoặc cực kỳ khó giải quyết do thiếu khả năng quan sát giờ đây có thể được sửa chữa.

Instrumentation động khác biệt đến mức so với quan sát truyền thống rằng ban đầu có thể khó nắm bắt vai trò của nó. Hãy xem xét một nhân hệ điều hành: phân tích nội bộ nhân có thể giống như mạo hiểm vào một căn phòng tối, với các ngọn nến (bộ đếm hệ thống) được đặt ở nơi mà các kỹ sư nhân nghĩ rằng chúng cần thiết. Instrumentation động giống như có một chiếc đèn pin mà bạn có thể chiếu đến bất kỳ đâu.

Instrumentation động lần đầu được tạo ra vào những năm 1990 [Hollingsworth 94], cùng với các công cụ sử dụng nó gọi là dynamic tracer (ví dụ: kerninst [Tamches 99]). Đối với Linux, instrumentation động lần đầu được phát triển vào năm 2000 [Kleen 08] và bắt đầu được merge vào nhân năm 2004 (kprobes). Tuy nhiên, các công nghệ này không được biết đến rộng rãi và khó sử dụng. Điều này thay đổi khi Sun Microsystems ra mắt phiên bản riêng của họ vào năm 2005, DTrace, dễ sử dụng và an toàn cho sản xuất. Tôi đã phát triển nhiều công cụ dựa trên DTrace cho thấy tầm quan trọng của nó đối với hiệu năng hệ thống, các công cụ được sử dụng rộng rãi và giúp DTrace cũng như instrumentation động trở nên nổi tiếng.

**BPF**

BPF, ban đầu viết tắt của Berkeley Packet Filter, đang cung cấp năng lượng cho các công cụ dynamic tracing mới nhất cho Linux. BPF bắt nguồn như một máy ảo nhỏ trong nhân (mini in-kernel virtual machine) để tăng tốc việc thực thi các biểu thức tcpdump(8). Từ năm 2013, nó đã được mở rộng (do đó đôi khi được gọi là eBPF³) để trở thành một môi trường thực thi tổng quát trong nhân, cung cấp tính an toàn và truy cập nhanh đến các tài nguyên. Trong số nhiều ứng dụng mới của nó có các công cụ tracing, nơi nó cung cấp khả năng lập trình cho các giao diện BPF Compiler Collection (BCC) và bpftrace. execsnoop(8), đã trình bày trước đó, là một công cụ BCC.⁴

> ³ eBPF ban đầu được sử dụng để mô tả BPF mở rộng này; tuy nhiên, công nghệ này hiện được gọi đơn giản là BPF.

> ⁴ Tôi đã phát triển nó lần đầu cho DTrace, và sau đó tôi đã phát triển nó cho các tracer khác bao gồm BCC và bpftrace.

Chương 3 giải thích BPF, và Chương 15 giới thiệu các giao diện tracing BPF: BCC và bpftrace. Các chương khác giới thiệu nhiều công cụ tracing dựa trên BPF trong các phần quan sát của chúng; ví dụ, các công cụ tracing CPU được bao gồm trong Chương 6, CPU, Phần 6.6, Công Cụ Quan Sát. Tôi cũng đã xuất bản các cuốn sách trước đó về công cụ tracing (cho DTrace [Gregg 11a] và BPF [Gregg 19]).

Cả perf(1) và Ftrace cũng là tracer với một số khả năng tương tự các giao diện BPF. perf(1) và Ftrace được đề cập trong Chương 13 và 14.

## 1.8 Thực Nghiệm (Experimentation)

Ngoài các công cụ quan sát, còn có các công cụ thực nghiệm, hầu hết trong số đó là công cụ benchmark. Các công cụ này thực hiện một thí nghiệm bằng cách áp dụng một khối lượng công việc tổng hợp (synthetic workload) lên hệ thống và đo hiệu năng của nó. Điều này phải được thực hiện cẩn thận, vì các công cụ thực nghiệm có thể gây nhiễu hiệu năng của các hệ thống đang được thử nghiệm.

Có các công cụ **macro-benchmark** mô phỏng khối lượng công việc thực tế như client gửi yêu cầu ứng dụng; và có các công cụ **micro-benchmark** thử nghiệm một thành phần cụ thể, chẳng hạn như CPU, đĩa hoặc mạng. Như một phép so sánh: thời gian chạy vòng đua tại Laguna Seca Raceway của một chiếc xe có thể được coi là macro-benchmark, trong khi tốc độ tối đa và thời gian 0 đến 60mph có thể được coi là micro-benchmark. Cả hai loại benchmark đều quan trọng, mặc dù micro-benchmark thường dễ debug, lặp lại và hiểu hơn, và ổn định hơn.

Ví dụ sau sử dụng iperf(1) trên một máy chủ nhàn rỗi để thực hiện micro-benchmark thông lượng mạng TCP với một máy chủ nhàn rỗi từ xa. Benchmark này chạy trong mười giây (-t 10) và tạo giá trị trung bình mỗi giây (-i 1):

```
# iperf -c 100.65.33.90 -i 1 -t 10
------------------------------------------------------------
Client connecting to 100.65.33.90, TCP port 5001
TCP window size: 12.0 MByte (default)
------------------------------------------------------------
[   3] local 100.65.170.28 port 39570 connected with 100.65.33.90 port 5001
[ ID] Interval          Transfer       Bandwidth
[   3]   0.0- 1.0 sec    582 MBytes    4.88 Gbits/sec
[   3]   1.0- 2.0 sec    568 MBytes    4.77 Gbits/sec
[   3]   2.0- 3.0 sec    574 MBytes    4.82 Gbits/sec
[   3]   3.0- 4.0 sec    571 MBytes    4.79 Gbits/sec
[   3]   4.0- 5.0 sec    571 MBytes    4.79 Gbits/sec
[   3]   5.0- 6.0 sec    432 MBytes    3.63 Gbits/sec
[   3]   6.0- 7.0 sec    383 MBytes    3.21 Gbits/sec
[   3]   7.0- 8.0 sec    388 MBytes    3.26 Gbits/sec
[   3]   8.0- 9.0 sec    390 MBytes    3.28 Gbits/sec
[   3]   9.0-10.0 sec    383 MBytes    3.22 Gbits/sec
[   3]   0.0-10.0 sec   4.73 GBytes    4.06 Gbits/sec
```

Đầu ra cho thấy thông lượng⁵ khoảng 4.8 Gbits cho năm giây đầu tiên, sau đó giảm xuống khoảng 3.2 Gbits/sec. Đây là một kết quả thú vị cho thấy thông lượng hai chế độ (bi-modal). Để cải thiện hiệu năng, người ta có thể tập trung vào chế độ 3.2 Gbits/sec, và tìm kiếm các chỉ số khác có thể giải thích nó.

> ⁵ Đầu ra sử dụng thuật ngữ "Bandwidth," một cách sử dụng sai phổ biến. Bandwidth đề cập đến thông lượng tối đa có thể, điều mà iperf(1) không đo. iperf(1) đang đo tốc độ hiện tại của khối lượng công việc mạng: thông lượng (throughput) của nó.

Hãy xem xét những hạn chế của việc debug vấn đề hiệu năng này trên máy chủ sản xuất chỉ sử dụng các công cụ quan sát. Thông lượng mạng có thể thay đổi từ giây sang giây vì phương sai tự nhiên trong khối lượng công việc client, và hành vi hai chế độ cơ bản của mạng có thể không rõ ràng. Bằng cách sử dụng iperf(1) với khối lượng công việc cố định, bạn loại bỏ phương sai client, làm lộ phương sai do các yếu tố khác (ví dụ: điều tiết mạng bên ngoài, sử dụng bộ đệm, v.v.).

Như tôi đã khuyến nghị trước đó, trên các hệ thống sản xuất, bạn nên thử các công cụ quan sát trước. Tuy nhiên, có quá nhiều công cụ quan sát đến mức bạn có thể dành hàng giờ làm việc qua chúng khi một công cụ thực nghiệm sẽ dẫn đến kết quả nhanh hơn. Một phép ẩn dụ được dạy cho tôi bởi một kỹ sư hiệu năng cấp cao (Roch Bourbonnais) nhiều năm trước là: bạn có hai bàn tay, quan sát và thực nghiệm. Chỉ sử dụng một loại công cụ giống như cố gắng giải quyết vấn đề bằng một tay.

Chương 6 đến 10 bao gồm các phần về công cụ thực nghiệm; ví dụ, công cụ thực nghiệm CPU được đề cập trong Chương 6, CPU, Phần 6.8, Thực Nghiệm.

## 1.9 Điện Toán Đám Mây (Cloud Computing)

Điện toán đám mây, một cách triển khai tài nguyên tính toán theo nhu cầu, đã cho phép mở rộng quy mô nhanh chóng các ứng dụng bằng cách hỗ trợ triển khai chúng trên số lượng ngày càng tăng các hệ thống ảo nhỏ gọi là instance. Điều này đã giảm nhu cầu hoạch định dung lượng nghiêm ngặt, vì có thể thêm dung lượng từ đám mây trong thời gian ngắn. Trong một số trường hợp, nó cũng đã tăng mong muốn phân tích hiệu năng, vì sử dụng ít tài nguyên hơn có thể có nghĩa là ít hệ thống hơn. Vì việc sử dụng đám mây thường được tính phí theo phút hoặc giờ, một cải thiện hiệu năng dẫn đến ít hệ thống hơn có thể có nghĩa là tiết kiệm chi phí ngay lập tức. So sánh kịch bản này với một trung tâm dữ liệu doanh nghiệp, nơi bạn có thể bị ràng buộc vào một hợp đồng hỗ trợ cố định trong nhiều năm, không thể thực hiện tiết kiệm chi phí cho đến khi hợp đồng kết thúc.

Những khó khăn mới do điện toán đám mây và ảo hóa gây ra bao gồm quản lý các ảnh hưởng hiệu năng từ các tenant khác (đôi khi gọi là cách ly hiệu năng - performance isolation) và khả năng quan sát hệ thống vật lý từ mỗi tenant. Ví dụ, trừ khi được quản lý đúng cách bởi hệ thống, hiệu năng I/O đĩa có thể kém do tranh chấp với một neighbor. Trong một số môi trường, việc sử dụng thực sự của các đĩa vật lý có thể không thể quan sát được bởi mỗi tenant, làm cho việc xác định vấn đề này trở nên khó khăn.

Các chủ đề này được đề cập trong Chương 11, Điện Toán Đám Mây.

## 1.10 Phương Pháp Luận (Methodologies)

Phương pháp luận là cách ghi lại các bước được khuyến nghị để thực hiện các nhiệm vụ khác nhau trong hiệu năng hệ thống. Nếu không có phương pháp luận, một cuộc điều tra hiệu năng có thể biến thành chuyến đi câu cá: thử những thứ ngẫu nhiên với hy vọng bắt được một chiến thắng. Điều này có thể tốn thời gian và không hiệu quả, đồng thời cho phép các khu vực quan trọng bị bỏ qua. Chương 2, Phương Pháp Luận, bao gồm một thư viện các phương pháp luận cho hiệu năng hệ thống. Phần sau đây là phương pháp đầu tiên tôi sử dụng cho bất kỳ vấn đề hiệu năng nào: danh sách kiểm tra dựa trên công cụ.

### 1.10.1 Phân Tích Hiệu Năng Linux trong 60 Giây

Đây là danh sách kiểm tra dựa trên công cụ Linux có thể được thực hiện trong 60 giây đầu tiên của cuộc điều tra vấn đề hiệu năng, sử dụng các công cụ truyền thống nên có sẵn cho hầu hết các bản phân phối Linux [Gregg 15a]. Bảng 1.1 cho thấy các lệnh, cần kiểm tra gì, và phần trong cuốn sách này đề cập chi tiết lệnh đó.

**Bảng 1.1: Danh sách kiểm tra phân tích 60 giây trên Linux**

| #  | Công cụ | Kiểm tra | Phần |
|----|---------|----------|------|
| 1  | `uptime` | Load average để xác định tải đang tăng hay giảm (so sánh trung bình 1, 5 và 15 phút). | 6.6.1 |
| 2  | `dmesg -T \| tail` | Lỗi nhân bao gồm sự kiện OOM. | 7.5.11 |
| 3  | `vmstat -SM 1` | Thống kê toàn hệ thống: độ dài hàng đợi chạy, swapping, mức sử dụng CPU tổng thể. | 7.5.1 |
| 4  | `mpstat -P ALL 1` | Cân bằng từng CPU: một CPU bận có thể chỉ ra khả năng mở rộng luồng kém. | 6.6.3 |
| 5  | `pidstat 1` | Mức sử dụng CPU từng tiến trình: xác định các trình tiêu thụ CPU bất thường, và thời gian CPU user/system cho mỗi tiến trình. | 6.6.7 |
| 6  | `iostat -sxz 1` | Thống kê I/O đĩa: IOPS và thông lượng, thời gian chờ trung bình, phần trăm bận. | 9.6.1 |
| 7  | `free -m` | Mức sử dụng bộ nhớ bao gồm bộ nhớ đệm hệ thống file. | 8.6.2 |
| 8  | `sar -n DEV 1` | I/O thiết bị mạng: gói tin và thông lượng. | 10.6.6 |
| 9  | `sar -n TCP,ETCP 1` | Thống kê TCP: tỷ lệ kết nối, retransmit. | 10.6.6 |
| 10 | `top` | Kiểm tra tổng quan. | 6.6.6 |

Danh sách kiểm tra này cũng có thể được thực hiện bằng GUI giám sát, miễn là cùng các chỉ số có sẵn.⁶

> ⁶ Bạn thậm chí có thể tạo dashboard tùy chỉnh cho danh sách kiểm tra này; tuy nhiên, hãy lưu ý rằng danh sách kiểm tra này được thiết kế để tận dụng tối đa các công cụ CLI sẵn có, và các sản phẩm giám sát có thể có nhiều (và tốt hơn) chỉ số. Tôi có xu hướng tạo dashboard tùy chỉnh cho phương pháp USE và các phương pháp luận khác.

Chương 2, Phương Pháp Luận, cũng như các chương sau, chứa nhiều phương pháp luận hơn cho phân tích hiệu năng, bao gồm phương pháp USE, đặc trưng hóa khối lượng công việc, phân tích độ trễ, và nhiều hơn nữa.

## 1.11 Nghiên Cứu Tình Huống (Case Studies)

Nếu bạn mới bắt đầu với hiệu năng hệ thống, các nghiên cứu tình huống cho thấy khi nào và tại sao các hoạt động khác nhau được thực hiện có thể giúp bạn liên hệ chúng với môi trường hiện tại của mình. Hai ví dụ giả định được tóm tắt ở đây; một là vấn đề hiệu năng liên quan đến I/O đĩa, và một là kiểm thử hiệu năng của một thay đổi phần mềm.

Các nghiên cứu tình huống này mô tả các hoạt động được giải thích trong các chương khác của cuốn sách. Các cách tiếp cận được mô tả ở đây cũng nhằm cho thấy không phải cách đúng hay cách duy nhất, mà là một cách mà các hoạt động hiệu năng này có thể được thực hiện, để bạn xem xét một cách phê phán.

### 1.11.1 Đĩa Chậm (Slow Disks)

Sumit là quản trị viên hệ thống tại một công ty cỡ trung. Đội cơ sở dữ liệu đã gửi một ticket hỗ trợ phàn nàn về "đĩa chậm" trên một trong các máy chủ cơ sở dữ liệu.

Nhiệm vụ đầu tiên của Sumit là tìm hiểu thêm về vấn đề, thu thập chi tiết để hình thành mô tả vấn đề (problem statement). Ticket tuyên bố rằng đĩa chậm, nhưng không giải thích liệu điều này có gây ra vấn đề cơ sở dữ liệu hay không. Sumit phản hồi bằng cách hỏi những câu hỏi sau:

- Hiện tại có vấn đề hiệu năng cơ sở dữ liệu không? Nó được đo như thế nào?
- Vấn đề này đã xuất hiện được bao lâu?
- Gần đây có gì thay đổi với cơ sở dữ liệu không?
- Tại sao nghi ngờ đĩa?

Đội cơ sở dữ liệu trả lời: "Chúng tôi có log cho các truy vấn chậm hơn 1.000 millisecond. Những truy vấn này thường không xảy ra, nhưng trong tuần qua chúng đã tăng lên hàng chục mỗi giờ. AcmeMon cho thấy đĩa đang bận."

Điều này xác nhận rằng có vấn đề cơ sở dữ liệu thực sự, nhưng cũng cho thấy giả thuyết về đĩa có lẽ chỉ là phỏng đoán. Sumit muốn kiểm tra đĩa, nhưng anh cũng muốn kiểm tra nhanh các tài nguyên khác trong trường hợp phỏng đoán đó sai.

AcmeMon là hệ thống giám sát máy chủ cơ bản của công ty, cung cấp các biểu đồ hiệu năng lịch sử dựa trên các chỉ số hệ điều hành tiêu chuẩn, cùng các chỉ số được in bởi mpstat(1), iostat(1) và các tiện ích hệ thống. Sumit đăng nhập vào AcmeMon để tự mình xem.

Sumit bắt đầu với một phương pháp luận gọi là **phương pháp USE** (định nghĩa trong Chương 2, Phương Pháp Luận, Phần 2.5.9) để nhanh chóng kiểm tra các nút thắt tài nguyên. Như đội cơ sở dữ liệu đã báo cáo, mức sử dụng đĩa cao, khoảng 80%, trong khi đối với các tài nguyên khác (CPU, mạng) mức sử dụng thấp hơn nhiều. Dữ liệu lịch sử cho thấy mức sử dụng đĩa đã tăng đều đặn trong tuần qua, trong khi mức sử dụng CPU ổn định. AcmeMon không cung cấp thống kê bão hòa (saturation) hoặc lỗi cho đĩa, nên để hoàn thành phương pháp USE, Sumit phải đăng nhập vào máy chủ và chạy một số lệnh.

Anh kiểm tra bộ đếm lỗi đĩa từ /sys; chúng bằng không. Anh chạy iostat(1) với khoảng thời gian một giây và quan sát các chỉ số sử dụng và bão hòa theo thời gian. AcmeMon báo cáo 80% sử dụng nhưng dùng khoảng thời gian một phút. Ở độ chi tiết một giây, Sumit có thể thấy mức sử dụng đĩa dao động, thường đạt 100% và gây ra các mức bão hòa và tăng độ trễ I/O đĩa.

Để xác nhận thêm rằng điều này đang chặn cơ sở dữ liệu — và không phải bất đồng bộ đối với các truy vấn cơ sở dữ liệu — anh sử dụng một công cụ tracing BCC/BPF gọi là offcputime(8) để thu thập stack trace mỗi khi cơ sở dữ liệu bị nhân loại khỏi lịch trình (descheduled), cùng với thời gian dành ngoài CPU. Các stack trace cho thấy cơ sở dữ liệu thường bị chặn trong khi đọc hệ thống file, trong một truy vấn. Đây là đủ bằng chứng cho Sumit.

Câu hỏi tiếp theo là tại sao. Thống kê hiệu năng đĩa có vẻ nhất quán với tải cao. Sumit thực hiện đặc trưng hóa khối lượng công việc (workload characterization) để hiểu thêm, sử dụng iostat(1) để đo IOPS, thông lượng, độ trễ I/O đĩa trung bình và tỷ lệ đọc/ghi. Để biết thêm chi tiết, Sumit có thể sử dụng tracing I/O đĩa; tuy nhiên, anh hài lòng rằng điều này đã chỉ ra trường hợp tải đĩa cao, và không phải vấn đề với bản thân đĩa.

Sumit thêm chi tiết vào ticket, nêu rõ những gì anh đã kiểm tra và bao gồm ảnh chụp màn hình các lệnh được sử dụng để nghiên cứu đĩa. Tóm tắt của anh cho đến nay là đĩa đang chịu tải cao, điều này làm tăng độ trễ I/O và làm chậm các truy vấn. Tuy nhiên, đĩa có vẻ hoạt động bình thường cho mức tải đó. Anh hỏi liệu có giải thích đơn giản không: tải cơ sở dữ liệu có tăng không?

Đội cơ sở dữ liệu trả lời rằng không, và tỷ lệ truy vấn (không được AcmeMon báo cáo) đã ổn định. Điều này có vẻ nhất quán với phát hiện trước đó rằng mức sử dụng CPU cũng ổn định.

Sumit nghĩ về những gì khác có thể gây ra tải I/O đĩa cao hơn mà không có sự tăng đáng kể về CPU và nhanh chóng trao đổi với đồng nghiệp về điều đó. Một trong số họ gợi ý phân mảnh hệ thống file (file system fragmentation), điều được mong đợi khi hệ thống file tiến gần 100% dung lượng. Sumit phát hiện rằng nó chỉ ở mức 30%.

Sumit biết rằng anh có thể thực hiện phân tích đào sâu (drill-down analysis)⁷ để hiểu nguyên nhân chính xác của I/O đĩa, nhưng điều này có thể tốn thời gian. Anh cố gắng nghĩ về các giải thích dễ dàng khác mà anh có thể kiểm tra nhanh trước, dựa trên kiến thức của mình về ngăn xếp I/O nhân. Anh nhớ rằng I/O đĩa này chủ yếu được gây ra bởi cache miss của bộ nhớ đệm hệ thống file (page cache).

> ⁷ Điều này được đề cập trong Chương 2, Phương Pháp Luận, Phần 2.5.12, Phân Tích Đào Sâu.

Sumit kiểm tra tỷ lệ trúng cache hệ thống file (file system cache hit ratio) sử dụng cachestat(8)⁸ và thấy nó hiện ở mức 91%. Điều này nghe có vẻ cao (tốt), nhưng anh không có dữ liệu lịch sử để so sánh. Anh đăng nhập vào các máy chủ cơ sở dữ liệu khác phục vụ khối lượng công việc tương tự và thấy tỷ lệ trúng cache của chúng là trên 98%. Anh cũng thấy kích thước bộ nhớ đệm hệ thống file lớn hơn nhiều trên các máy chủ khác.

> ⁸ Một công cụ tracing BCC được đề cập trong Chương 8, Hệ Thống File, Phần 8.6.12, cachestat.

Chuyển sự chú ý sang kích thước bộ nhớ đệm hệ thống file và mức sử dụng bộ nhớ máy chủ, anh tìm thấy điều đã bị bỏ qua: một dự án phát triển có một ứng dụng nguyên mẫu đang tiêu thụ lượng bộ nhớ ngày càng tăng, ngay cả khi nó chưa chịu tải sản xuất. Bộ nhớ này được lấy từ phần có sẵn cho bộ nhớ đệm hệ thống file, giảm tỷ lệ trúng cache và khiến nhiều lần đọc hệ thống file trở thành đọc đĩa.

Sumit liên hệ đội phát triển ứng dụng và yêu cầu họ tắt ứng dụng và chuyển nó sang máy chủ khác, tham chiếu đến vấn đề cơ sở dữ liệu. Sau khi họ làm điều này, Sumit quan sát mức sử dụng đĩa giảm dần trong AcmeMon khi bộ nhớ đệm hệ thống file phục hồi về kích thước ban đầu. Các truy vấn chậm trở về không, và anh đóng ticket là đã giải quyết.

### 1.11.2 Thay Đổi Phần Mềm (Software Change)

Pamela là kỹ sư hiệu năng và khả năng mở rộng tại một công ty nhỏ nơi cô làm việc trên tất cả các hoạt động liên quan đến hiệu năng. Các nhà phát triển ứng dụng đã phát triển một tính năng cốt lõi mới và không chắc liệu việc giới thiệu nó có ảnh hưởng đến hiệu năng hay không. Pamela quyết định thực hiện kiểm thử phi hồi quy (non-regression testing)⁹ phiên bản ứng dụng mới, trước khi nó được triển khai trong sản xuất.

> ⁹ Một số gọi đó là regression testing, nhưng đây là hoạt động nhằm xác nhận rằng một thay đổi phần mềm hoặc phần cứng không gây ra hồi quy hiệu năng, do đó, non-regression testing.

Pamela mua một máy chủ nhàn rỗi cho mục đích thử nghiệm và tìm kiếm một trình mô phỏng khối lượng công việc client. Đội ứng dụng đã viết một trình mô phỏng cách đây một thời gian, mặc dù nó có nhiều hạn chế và bug đã biết. Cô quyết định thử nó nhưng muốn xác nhận rằng nó giống đủ với khối lượng công việc sản xuất hiện tại.

Cô cấu hình máy chủ để phù hợp với cấu hình triển khai hiện tại và chạy trình mô phỏng khối lượng công việc client từ một hệ thống khác đến máy chủ. Khối lượng công việc client có thể được đặc trưng hóa bằng cách nghiên cứu access log, và đã có sẵn một công cụ công ty để làm điều này, mà cô sử dụng. Cô cũng chạy công cụ trên log máy chủ sản xuất cho các thời điểm khác nhau trong ngày và so sánh khối lượng công việc. Có vẻ như trình mô phỏng client áp dụng khối lượng công việc sản xuất trung bình nhưng không tính đến phương sai. Cô ghi nhận điều này và tiếp tục phân tích.

Pamela biết một số cách tiếp cận để sử dụng tại thời điểm này. Cô chọn cách dễ nhất: tăng tải từ trình mô phỏng client cho đến khi đạt giới hạn (đôi khi gọi là stress testing). Trình mô phỏng client có thể được cấu hình để thực hiện số lượng yêu cầu client mục tiêu mỗi giây, với mặc định là 1.000 mà cô đã sử dụng trước đó. Cô quyết định tăng tải bắt đầu từ 100 và thêm các bước tăng 100 cho đến khi đạt giới hạn, mỗi mức được thử nghiệm trong một phút. Cô viết một shell script để thực hiện kiểm thử, thu thập kết quả vào file để vẽ biểu đồ bởi các công cụ khác.

Với tải đang chạy, cô thực hiện benchmarking chủ động để xác định các yếu tố giới hạn là gì. Tài nguyên máy chủ và luồng máy chủ có vẻ phần lớn nhàn rỗi. Trình mô phỏng client cho thấy thông lượng yêu cầu ổn định ở khoảng 700 mỗi giây.

Cô chuyển sang phiên bản phần mềm mới và lặp lại kiểm thử. Phiên bản này cũng đạt mốc 700 và ổn định. Cô cũng phân tích máy chủ để tìm các yếu tố giới hạn nhưng một lần nữa không thể thấy bất kỳ yếu tố nào.

Cô vẽ biểu đồ kết quả, hiển thị tỷ lệ yêu cầu hoàn thành so với tải, để nhận diện trực quan hồ sơ khả năng mở rộng (scalability profile). Cả hai đều có vẻ đạt trần đột ngột.

Mặc dù có vẻ như các phiên bản phần mềm có đặc tính hiệu năng tương tự, Pamela thất vọng vì cô không thể xác định yếu tố giới hạn gây ra trần khả năng mở rộng. Cô biết mình chỉ kiểm tra tài nguyên máy chủ, và yếu tố giới hạn có thể là vấn đề logic ứng dụng. Nó cũng có thể ở nơi khác: mạng hoặc trình mô phỏng client.

Pamela tự hỏi liệu có cần một cách tiếp cận khác hay không, chẳng hạn như chạy tỷ lệ thao tác cố định và sau đó đặc trưng hóa việc sử dụng tài nguyên (CPU, I/O đĩa, I/O mạng), để có thể biểu thị dưới dạng một yêu cầu client đơn lẻ. Cô chạy trình mô phỏng ở tỷ lệ 700 mỗi giây cho phần mềm hiện tại và mới, và đo mức tiêu thụ tài nguyên. Phần mềm hiện tại đưa 32 CPU đến mức sử dụng trung bình 20% cho tải đã cho. Phần mềm mới đưa cùng CPU đến 30% sử dụng, cho cùng tải. Có vẻ như đây thực sự là một hồi quy (regression), tiêu thụ nhiều tài nguyên CPU hơn.

Tò mò muốn hiểu giới hạn 700, Pamela khởi chạy tải cao hơn và sau đó điều tra tất cả các thành phần trong đường dữ liệu, bao gồm mạng, hệ thống client và trình tạo khối lượng công việc client. Cô cũng thực hiện phân tích đào sâu (drill-down analysis) phần mềm máy chủ và client. Cô ghi lại những gì đã kiểm tra, bao gồm ảnh chụp màn hình, để tham khảo.

Để điều tra phần mềm client, cô thực hiện phân tích trạng thái luồng (thread state analysis) và phát hiện rằng nó chỉ có một luồng (single-threaded)! Một luồng đó đang dành 100% thời gian thực thi trên CPU. Điều này thuyết phục cô rằng đây là yếu tố giới hạn của kiểm thử.

Như một thí nghiệm, cô khởi chạy phần mềm client song song trên các hệ thống client khác nhau. Bằng cách này, cô đưa máy chủ đến 100% sử dụng CPU cho cả phần mềm hiện tại và mới. Phiên bản hiện tại đạt 3.500 yêu cầu/giây, và phiên bản mới đạt 2.300 yêu cầu/giây, nhất quán với các phát hiện trước đó về tiêu thụ tài nguyên.

Pamela thông báo cho các nhà phát triển ứng dụng rằng có hồi quy với phiên bản phần mềm mới, và cô bắt đầu profiling mức sử dụng CPU bằng CPU flame graph để hiểu tại sao: đường dẫn mã nào đang đóng góp. Cô ghi nhận rằng khối lượng công việc sản xuất trung bình đã được thử nghiệm và các khối lượng công việc đa dạng thì chưa. Cô cũng gửi một bug để ghi nhận rằng trình tạo khối lượng công việc client chỉ có một luồng, có thể trở thành nút thắt cổ chai.

### 1.11.3 Đọc Thêm (More Reading)

Một nghiên cứu tình huống chi tiết hơn được cung cấp dưới dạng Chương 16, Nghiên Cứu Tình Huống, ghi lại cách tôi giải quyết một vấn đề hiệu năng đám mây cụ thể. Chương tiếp theo giới thiệu các phương pháp luận được sử dụng cho phân tích hiệu năng, và các chương còn lại đề cập đến nền tảng và chi tiết cần thiết.

## 1.12 Tài Liệu Tham Khảo (References)

- [Hollingsworth 94] Hollingsworth, J., Miller, B., and Cargille, J., "Dynamic Program Instrumentation for Scalable Performance Tools," Scalable High-Performance Computing Conference (SHPCC), May 1994.

- [Tamches 99] Tamches, A., and Miller, B., "Fine-Grained Dynamic Instrumentation of Commodity Operating System Kernels," Proceedings of the 3rd Symposium on Operating Systems Design and Implementation, February 1999.

- [Kleen 08] Kleen, A., "On Submitting Kernel Patches," Intel Open Source Technology Center, http://halobates.de/on-submitting-patches.pdf, 2008.

- [Gregg 11a] Gregg, B., and Mauro, J., DTrace: Dynamic Tracing in Oracle Solaris, Mac OS X and FreeBSD, Prentice Hall, 2011.

- [Gregg 15a] Gregg, B., "Linux Performance Analysis in 60,000 Milliseconds," Netflix Technology Blog, http://techblog.netflix.com/2015/11/linux-performance-analysis-in-60s.html, 2015.

- [Dekker 18] Dekker, S., Drift into Failure: From Hunting Broken Components to Understanding Complex Systems, CRC Press, 2018.

- [Gregg 19] Gregg, B., BPF Performance Tools: Linux System and Application Observability, Addison-Wesley, 2019.

- [Corry 20] Corry, A., Retrospectives Antipatterns, Addison-Wesley, 2020.
