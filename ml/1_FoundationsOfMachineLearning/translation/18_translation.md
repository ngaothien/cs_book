# Chương 1: Giới thiệu

Chương này trình bày phần giới thiệu sơ bộ về học máy (machine learning), bao gồm tổng quan về một số tác vụ học và ứng dụng chính, các định nghĩa và thuật ngữ cơ bản, cùng với phần thảo luận về một số kịch bản tổng quát.

## 1.1 Học máy là gì?

Học máy có thể được định nghĩa một cách rộng rãi là các phương pháp tính toán sử dụng kinh nghiệm để cải thiện hiệu suất hoặc để đưa ra các dự đoán chính xác. Ở đây, kinh nghiệm đề cập đến thông tin trong quá khứ có sẵn cho bộ học (learner), thường ở dạng dữ liệu điện tử được thu thập và cung cấp để phân tích. Dữ liệu này có thể ở dạng các tập huấn luyện được gán nhãn bởi con người dưới dạng số hóa, hoặc các loại thông tin khác thu được thông qua tương tác với môi trường. Trong mọi trường hợp, chất lượng và kích thước của dữ liệu đóng vai trò quyết định đến sự thành công của các dự đoán do bộ học tạo ra.

Một ví dụ về bài toán học máy là làm thế nào để sử dụng một mẫu hữu hạn các tài liệu được chọn ngẫu nhiên, trong đó mỗi tài liệu được gán nhãn bằng một chủ đề, để dự đoán chính xác chủ đề của các tài liệu chưa từng thấy. Rõ ràng, mẫu càng lớn thì tác vụ càng dễ dàng. Nhưng độ khó của tác vụ cũng phụ thuộc vào chất lượng của các nhãn được gán cho các tài liệu trong mẫu, vì các nhãn có thể không hoàn toàn chính xác, và phụ thuộc vào số lượng các chủ đề có thể có.

Học máy bao gồm việc thiết kế các thuật toán dự đoán hiệu quả và chính xác. Giống như trong các lĩnh vực khác của khoa học máy tính, một số thước đo quan trọng về chất lượng của các thuật toán này là độ phức tạp thời gian (time complexity) và độ phức tạp không gian (space complexity) của chúng. Nhưng trong học máy, chúng ta sẽ cần thêm một khái niệm về độ phức tạp mẫu (sample complexity) để đánh giá kích thước mẫu cần thiết để thuật toán có thể học được một họ các khái niệm. Tổng quát hơn, các đảm bảo lý thuyết về khả năng học cho một thuật toán phụ thuộc vào độ phức tạp của các lớp khái niệm được xem xét và kích thước của mẫu huấn luyện.

Vì sự thành công của một thuật toán học phụ thuộc vào dữ liệu được sử dụng, nên học máy có mối liên hệ nội tại với phân tích dữ liệu và thống kê. Tổng quát hơn, các kỹ thuật học là các phương pháp hướng dữ liệu (data-driven methods) kết hợp các khái niệm nền tảng trong khoa học máy tính với các ý tưởng từ thống kê, xác suất và tối ưu hóa.

## 1.2 Những loại bài toán nào có thể giải quyết bằng học máy?

Dự đoán nhãn của một tài liệu, còn được gọi là phân loại tài liệu (document classification), hoàn toàn không phải là tác vụ học duy nhất. Học máy cho phép ứng dụng trong một tập hợp rất rộng các bài toán thực tiễn, bao gồm những bài toán sau:

- **Phân loại văn bản hoặc tài liệu (Text or document classification).** Bao gồm các bài toán như gán một chủ đề cho một văn bản hoặc một tài liệu, hoặc tự động xác định xem nội dung của một trang web có không phù hợp hoặc quá nhạy cảm hay không; nó cũng bao gồm phát hiện thư rác (spam detection).

- **Xử lý ngôn ngữ tự nhiên (NLP).** Hầu hết các tác vụ trong lĩnh vực này, bao gồm gán nhãn từ loại (part-of-speech tagging), nhận dạng thực thể có tên (named-entity recognition), phân tích cú pháp phi ngữ cảnh (context-free parsing), hoặc phân tích cú pháp phụ thuộc (dependency parsing), đều được đặt dưới dạng các bài toán học. Trong các bài toán này, các dự đoán có một cấu trúc nhất định. Ví dụ, trong gán nhãn từ loại, dự đoán cho một câu là một chuỗi các nhãn từ loại gán cho từng từ. Trong phân tích cú pháp phi ngữ cảnh, dự đoán là một cây. Đây là những ví dụ của các bài toán học phong phú hơn, được gọi là các bài toán dự đoán có cấu trúc (structured prediction problems).

- **Các ứng dụng xử lý giọng nói (Speech processing applications).** Bao gồm nhận dạng giọng nói, tổng hợp giọng nói, xác minh người nói, nhận dạng người nói, cũng như các bài toán con như mô hình hóa ngôn ngữ (language modeling) và mô hình hóa âm học (acoustic modeling).

- **Các ứng dụng thị giác máy tính (Computer vision applications).** Bao gồm nhận dạng đối tượng, xác định đối tượng, phát hiện khuôn mặt, nhận dạng ký tự quang học (OCR), truy xuất hình ảnh dựa trên nội dung (content-based image retrieval), hoặc ước lượng tư thế (pose estimation).

- **Các ứng dụng sinh học tính toán (Computational biology applications).** Bao gồm dự đoán chức năng protein, xác định các vị trí quan trọng (key sites), hoặc phân tích các mạng lưới gen và protein.

- **Nhiều bài toán khác** như phát hiện gian lận cho các công ty thẻ tín dụng, điện thoại hoặc bảo hiểm, xâm nhập mạng (network intrusion), học chơi các trò chơi như cờ vua, cờ thỏ cáo (backgammon) hoặc cờ vây (Go), điều khiển tự động các phương tiện như robot hoặc ô tô mà không cần hỗ trợ, chẩn đoán y tế, thiết kế các hệ thống khuyến nghị (recommendation systems), các công cụ tìm kiếm (search engines), hoặc các hệ thống trích xuất thông tin (information extraction systems), đều được giải quyết bằng các kỹ thuật học máy.

Danh sách này hoàn toàn không mang tính toàn diện. Hầu hết các bài toán dự đoán được tìm thấy trong thực tiễn đều có thể được đặt dưới dạng các bài toán học, và phạm vi ứng dụng thực tế của học máy không ngừng mở rộng. Các thuật toán và kỹ thuật được thảo luận trong cuốn sách này có thể được sử dụng để rút ra các giải pháp cho tất cả các bài toán trên, mặc dù chúng tôi sẽ không thảo luận chi tiết về các ứng dụng này.

## 1.3 Một số tác vụ học tiêu chuẩn

Dưới đây là một số tác vụ học máy tiêu chuẩn đã được nghiên cứu rộng rãi:

- **Phân loại (Classification):** đây là bài toán gán một danh mục (category) cho từng mục (item). Ví dụ, phân loại tài liệu bao gồm việc gán một danh mục như chính trị, kinh doanh, thể thao hoặc thời tiết cho mỗi tài liệu, trong khi phân loại hình ảnh bao gồm việc gán cho mỗi hình ảnh một danh mục như ô tô, tàu hỏa hoặc máy bay. Số lượng các danh mục trong các tác vụ như vậy thường ít hơn vài trăm, nhưng nó có thể lớn hơn nhiều trong một số tác vụ khó và thậm chí không bị giới hạn (unbounded) như trong OCR, phân loại văn bản hoặc nhận dạng giọng nói.

- **Hồi quy (Regression):** đây là bài toán dự đoán một giá trị thực cho mỗi mục. Các ví dụ về hồi quy bao gồm dự đoán giá trị cổ phiếu hoặc dự đoán sự biến động của các biến số kinh tế. Trong hồi quy, hình phạt cho một dự đoán sai phụ thuộc vào độ lớn của sự khác biệt giữa giá trị thực và giá trị dự đoán, trái ngược với bài toán phân loại, trong đó thường không có khái niệm về sự gần gũi giữa các danh mục khác nhau.

- **Xếp hạng (Ranking):** đây là bài toán học cách sắp xếp các mục theo một tiêu chí nào đó. Tìm kiếm web, ví dụ: trả về các trang web liên quan đến một truy vấn tìm kiếm, là ví dụ xếp hạng điển hình nhất. Nhiều bài toán xếp hạng tương tự khác cũng xuất hiện trong bối cảnh thiết kế các hệ thống trích xuất thông tin hoặc hệ thống xử lý ngôn ngữ tự nhiên.

- **Phân cụm (Clustering):** đây là bài toán phân chia một tập hợp các mục thành các tập con đồng nhất (homogeneous subsets). Phân cụm thường được sử dụng để phân tích các tập dữ liệu rất lớn. Ví dụ, trong bối cảnh phân tích mạng xã hội, các thuật toán phân cụm cố gắng xác định các cộng đồng tự nhiên trong các nhóm lớn người dùng.

- **Giảm chiều dữ liệu hoặc học đa tạp (Dimensionality reduction or manifold learning):** bài toán này bao gồm việc chuyển đổi một biểu diễn ban đầu của các mục thành một biểu diễn có số chiều thấp hơn trong khi vẫn bảo toàn một số tính chất của biểu diễn ban đầu. Một ví dụ phổ biến liên quan đến việc tiền xử lý các hình ảnh kỹ thuật số trong các tác vụ thị giác máy tính.

Các mục tiêu thực tiễn chính của học máy bao gồm việc tạo ra các dự đoán chính xác cho các mục chưa từng thấy và thiết kế các thuật toán hiệu quả và bền vững để tạo ra các dự đoán này, ngay cả đối với các bài toán quy mô lớn. Để làm được điều đó, một số câu hỏi về thuật toán và lý thuyết được đặt ra. Một số câu hỏi cơ bản bao gồm: Những họ khái niệm nào thực sự có thể được học, và trong những điều kiện nào? Các khái niệm này có thể được học tốt đến mức nào về mặt tính toán?

## 1.4 Các giai đoạn học

Ở đây, chúng ta sẽ sử dụng bài toán phát hiện thư rác (spam detection) làm ví dụ xuyên suốt để minh họa một số định nghĩa cơ bản và mô tả cách sử dụng cũng như đánh giá các thuật toán học máy trong thực tế, bao gồm các giai đoạn khác nhau của chúng.

Phát hiện thư rác là bài toán học cách tự động phân loại các thư điện tử thành thư rác (spam) hoặc không phải thư rác (non-spam). Dưới đây là danh sách các định nghĩa và thuật ngữ thường dùng trong học máy:

- **Ví dụ / Điểm dữ liệu (Examples):** Các mục hoặc thực thể dữ liệu được sử dụng cho quá trình học hoặc đánh giá. Trong bài toán thư rác của chúng ta, các ví dụ này tương ứng với tập hợp các thư điện tử mà chúng ta sẽ sử dụng để học và kiểm thử.

- **Đặc trưng (Features):** Tập hợp các thuộc tính, thường được biểu diễn dưới dạng một vectơ, gắn liền với một ví dụ. Trong trường hợp thư điện tử, một số đặc trưng liên quan có thể bao gồm độ dài của thư, tên người gửi, các đặc điểm khác nhau của tiêu đề thư (header), sự xuất hiện của một số từ khóa nhất định trong phần thân thư (body), v.v.

- **Nhãn (Labels):** Các giá trị hoặc danh mục được gán cho các ví dụ. Trong các bài toán phân loại, các ví dụ được gán các danh mục cụ thể, chẳng hạn các danh mục thư rác và không phải thư rác trong bài toán phân loại nhị phân của chúng ta. Trong hồi quy, các mục được gán nhãn có giá trị thực.

- **Siêu tham số (Hyperparameters):** Các tham số tự do không được xác định bởi thuật toán học, mà được chỉ định như là các đầu vào cho thuật toán học.

- **Tập huấn luyện (Training sample):** Các ví dụ được sử dụng để huấn luyện một thuật toán học. Trong bài toán thư rác của chúng ta, tập huấn luyện bao gồm một tập hợp các ví dụ thư điện tử cùng với các nhãn tương ứng của chúng. Tập huấn luyện thay đổi tùy theo các kịch bản học khác nhau, như được mô tả trong mục 1.5.

- **Tập xác thực (Validation sample):** Các ví dụ được sử dụng để tinh chỉnh các tham số của thuật toán học khi làm việc với dữ liệu có nhãn. Tập xác thực được sử dụng để chọn các giá trị phù hợp cho các tham số tự do (siêu tham số) của thuật toán học.

- **Tập kiểm thử (Test sample):** Các ví dụ được sử dụng để đánh giá hiệu suất của thuật toán học. Tập kiểm thử được tách biệt khỏi dữ liệu huấn luyện và xác thực, và không được cung cấp trong giai đoạn học. Trong bài toán thư rác, tập kiểm thử bao gồm một tập hợp các ví dụ thư điện tử mà thuật toán học phải dự đoán nhãn dựa trên các đặc trưng. Các dự đoán này sau đó được so sánh với các nhãn của tập kiểm thử để đo lường hiệu suất của thuật toán.

- **Hàm mất mát (Loss function):** Một hàm đo lường sự khác biệt, hay mất mát, giữa một nhãn dự đoán và một nhãn thực. Ký hiệu tập tất cả các nhãn là $\mathcal{Y}$ và tập các dự đoán có thể có là $\mathcal{Y}'$, hàm mất mát $L$ là một ánh xạ $L: \mathcal{Y} \times \mathcal{Y}' \to \mathbb{R}_+$. Trong hầu hết các trường hợp, $\mathcal{Y}' = \mathcal{Y}$ và hàm mất mát bị chặn (bounded), nhưng các điều kiện này không phải lúc nào cũng đúng. Các ví dụ phổ biến của hàm mất mát bao gồm hàm mất mát zero-one (hay mất mát phân loại sai) được định nghĩa trên $\{-1, +1\} \times \{-1, +1\}$ bởi $L(y, y') = \mathbf{1}_{y' \neq y}$ và hàm mất mát bình phương (squared loss) được định nghĩa trên $I \times I$ bởi $L(y, y') = (y' - y)^2$, trong đó $I \subseteq \mathbb{R}$ thường là một khoảng bị chặn.

- **Lớp giả thuyết (Hypothesis set):** Một tập hợp các hàm ánh xạ từ các đặc trưng (vectơ đặc trưng) tới tập các nhãn $\mathcal{Y}$. Trong ví dụ của chúng ta, đây có thể là một tập hợp các hàm ánh xạ các đặc trưng thư điện tử tới $\mathcal{Y} = \{\text{spam}, \text{non-spam}\}$. Tổng quát hơn, các giả thuyết có thể là các hàm ánh xạ các đặc trưng tới một tập khác $\mathcal{Y}'$. Chúng có thể là các hàm tuyến tính ánh xạ các vectơ đặc trưng thư điện tử tới các số thực được hiểu như điểm số ($\mathcal{Y}' = \mathbb{R}$), trong đó các giá trị điểm số cao hơn cho thấy khả năng là thư rác cao hơn so với các giá trị thấp hơn.

> **Hình 1.1:** Minh họa các giai đoạn điển hình của một quá trình học.

Bây giờ chúng ta định nghĩa các giai đoạn học của bài toán thư rác (xem Hình 1.1). Chúng ta bắt đầu với một tập hợp các ví dụ có nhãn cho trước. Đầu tiên, chúng ta phân chia ngẫu nhiên dữ liệu thành một tập huấn luyện, một tập xác thực và một tập kiểm thử. Kích thước của mỗi tập mẫu này phụ thuộc vào một số cân nhắc khác nhau. Ví dụ, lượng dữ liệu dành cho xác thực phụ thuộc vào số lượng siêu tham số của thuật toán, được biểu diễn ở đây bởi vectơ $\Theta$. Ngoài ra, khi mẫu có nhãn tương đối nhỏ, lượng dữ liệu huấn luyện thường được chọn lớn hơn lượng dữ liệu kiểm thử vì hiệu suất học trực tiếp phụ thuộc vào tập huấn luyện.

Tiếp theo, chúng ta gắn kết các đặc trưng liên quan cho các ví dụ. Đây là một bước quan trọng trong việc thiết kế các giải pháp học máy. Các đặc trưng hữu ích có thể hướng dẫn hiệu quả thuật toán học, trong khi các đặc trưng kém hoặc không mang thông tin có thể gây nhầm lẫn. Mặc dù rất quan trọng, nhưng phần lớn việc lựa chọn các đặc trưng được để cho người dùng quyết định. Sự lựa chọn này phản ánh kiến thức tiên nghiệm (prior knowledge) của người dùng về tác vụ học, mà trong thực tế có thể có ảnh hưởng đáng kể đến kết quả hiệu suất.

Bây giờ, chúng ta sử dụng các đặc trưng đã chọn để huấn luyện thuật toán học $A$ bằng cách tinh chỉnh các giá trị của các tham số tự do $\Theta$ (còn gọi là siêu tham số). Với mỗi giá trị của các tham số này, thuật toán chọn ra một giả thuyết khác nhau từ tập giả thuyết. Chúng ta chọn giả thuyết cho kết quả tốt nhất trên tập xác thực ($\Theta_0$). Cuối cùng, sử dụng giả thuyết đó, chúng ta dự đoán nhãn cho các ví dụ trong tập kiểm thử. Hiệu suất của thuật toán được đánh giá bằng cách sử dụng hàm mất mát gắn liền với tác vụ, ví dụ: hàm mất mát zero-one trong tác vụ phát hiện thư rác của chúng ta, để so sánh các nhãn dự đoán và nhãn thực. Do đó, hiệu suất của một thuật toán tất nhiên được đánh giá dựa trên sai số kiểm thử (test error) chứ không phải sai số trên tập huấn luyện.

## 1.5 Các kịch bản học

Tiếp theo, chúng ta mô tả ngắn gọn một số kịch bản học máy phổ biến. Các kịch bản này khác nhau về các loại dữ liệu huấn luyện có sẵn cho bộ học, thứ tự và phương pháp mà dữ liệu huấn luyện được nhận, cũng như dữ liệu kiểm thử được sử dụng để đánh giá thuật toán học.

- **Học có giám sát (Supervised learning):** Bộ học nhận một tập hợp các ví dụ có nhãn làm dữ liệu huấn luyện và đưa ra dự đoán cho tất cả các điểm chưa được quan sát. Đây là kịch bản phổ biến nhất liên quan đến các bài toán phân loại, hồi quy và xếp hạng. Bài toán phát hiện thư rác thảo luận ở phần trước là một ví dụ của học có giám sát.

- **Học không giám sát (Unsupervised learning):** Bộ học chỉ nhận dữ liệu huấn luyện không có nhãn, và đưa ra dự đoán cho tất cả các điểm chưa được quan sát. Vì nói chung không có ví dụ có nhãn nào có sẵn trong thiết lập này, nên việc đánh giá định lượng hiệu suất của bộ học có thể khó khăn. Phân cụm và giảm chiều dữ liệu là các ví dụ của các bài toán học không giám sát.

- **Học bán giám sát (Semi-supervised learning):** Bộ học nhận một tập huấn luyện bao gồm cả dữ liệu có nhãn và không có nhãn, và đưa ra dự đoán cho tất cả các điểm chưa được quan sát. Học bán giám sát phổ biến trong các môi trường mà dữ liệu không có nhãn dễ dàng truy cập nhưng việc thu thập nhãn rất tốn kém. Nhiều loại bài toán phát sinh trong ứng dụng, bao gồm các tác vụ phân loại, hồi quy hoặc xếp hạng, có thể được đặt dưới dạng các trường hợp của học bán giám sát. Kỳ vọng là phân phối của dữ liệu không có nhãn mà bộ học có thể truy cập sẽ giúp bộ học đạt được hiệu suất tốt hơn so với trong thiết lập có giám sát. Việc phân tích các điều kiện mà điều này thực sự có thể đạt được là chủ đề của nhiều nghiên cứu lý thuyết và ứng dụng học máy hiện đại.

- **Suy diễn chuyển nạp (Transductive inference):** Giống như trong kịch bản bán giám sát, bộ học nhận một tập huấn luyện có nhãn cùng với một tập các điểm kiểm thử không có nhãn. Tuy nhiên, mục tiêu của suy diễn chuyển nạp là chỉ dự đoán nhãn cho chính các điểm kiểm thử cụ thể này. Suy diễn chuyển nạp dường như là một tác vụ dễ hơn và phù hợp với kịch bản gặp phải trong nhiều ứng dụng hiện đại. Tuy nhiên, giống như trong thiết lập bán giám sát, các giả định mà theo đó hiệu suất tốt hơn có thể đạt được trong thiết lập này là các câu hỏi nghiên cứu chưa được giải quyết hoàn toàn.

- **Học trực tuyến (On-line learning):** Trái ngược với các kịch bản trước đó, kịch bản trực tuyến bao gồm nhiều vòng (rounds) trong đó các giai đoạn huấn luyện và kiểm thử được xen kẽ. Tại mỗi vòng, bộ học nhận một điểm huấn luyện không có nhãn, đưa ra dự đoán, nhận nhãn thực, và chịu một mất mát. Mục tiêu trong thiết lập trực tuyến là tối thiểu hóa mất mát tích lũy qua tất cả các vòng hoặc tối thiểu hóa sự hối tiếc (regret), tức là sự khác biệt giữa mất mát tích lũy phải chịu và mất mát của chuyên gia tốt nhất khi nhìn lại (best expert in hindsight). Không giống như các thiết lập trước đó, không có giả định phân phối nào được đưa ra trong học trực tuyến. Thực tế, các thực thể và nhãn của chúng có thể được chọn theo hướng đối kháng (adversarially) trong kịch bản này.

- **Học tăng cường (Reinforcement learning):** Các giai đoạn huấn luyện và kiểm thử cũng được xen kẽ trong học tăng cường. Để thu thập thông tin, bộ học tương tác chủ động với môi trường và trong một số trường hợp tác động đến môi trường, và nhận một phần thưởng (reward) tức thì cho mỗi hành động. Mục tiêu của bộ học là tối đa hóa phần thưởng của mình qua một chuỗi các hành động và lần tương tác với môi trường. Tuy nhiên, môi trường không cung cấp phản hồi phần thưởng dài hạn, và bộ học phải đối mặt với bài toán tiến thoái lưỡng nan giữa khám phá và khai thác (exploration versus exploitation dilemma), vì bộ học phải lựa chọn giữa việc khám phá các hành động chưa biết để thu thập thêm thông tin và việc khai thác thông tin đã thu thập.

- **Học chủ động (Active learning):** Bộ học thu thập các ví dụ huấn luyện một cách thích ứng hoặc tương tác, thường bằng cách truy vấn một bộ trả lời (oracle) để yêu cầu nhãn cho các điểm mới. Mục tiêu trong học chủ động là đạt được hiệu suất tương đương với kịch bản học có giám sát tiêu chuẩn (hoặc kịch bản học thụ động), nhưng với ít ví dụ có nhãn hơn. Học chủ động thường được sử dụng trong các ứng dụng mà việc thu thập nhãn rất tốn kém, ví dụ các ứng dụng sinh học tính toán.

Trong thực tế, nhiều kịch bản học trung gian và phức tạp hơn khác cũng có thể gặp phải.

## 1.6 Khái quát hóa (Generalization)

Học máy về cơ bản là nói về khái quát hóa. Ví dụ, kịch bản học có giám sát tiêu chuẩn bao gồm việc sử dụng một mẫu hữu hạn các ví dụ có nhãn để đưa ra các dự đoán chính xác về các ví dụ chưa từng thấy. Bài toán thường được phát biểu dưới dạng chọn một hàm từ một tập giả thuyết (hypothesis set), là một tập con của họ tất cả các hàm. Hàm được chọn sau đó được sử dụng để gán nhãn cho tất cả các thực thể, bao gồm cả các ví dụ chưa từng thấy.

Tập giả thuyết nên được chọn như thế nào? Với một tập giả thuyết phong phú hoặc phức tạp, bộ học có thể chọn một hàm hoặc bộ dự đoán nhất quán (consistent) với tập huấn luyện, tức là hàm không mắc lỗi nào trên tập huấn luyện. Với một họ ít phức tạp hơn, việc mắc một số lỗi trên tập huấn luyện có thể là không thể tránh khỏi. Nhưng, cách nào sẽ dẫn đến khả năng khái quát hóa tốt hơn? Chúng ta nên định nghĩa độ phức tạp của một tập giả thuyết như thế nào?

> **Hình 1.2:** Đường ngoằn ngoèo (zig-zag) ở bảng bên trái nhất quán trên tập huấn luyện gồm các điểm xanh và đỏ, nhưng nó là một bề mặt phân tách phức tạp và không có khả năng khái quát hóa tốt cho dữ liệu chưa thấy. Ngược lại, bề mặt quyết định ở bảng bên phải đơn giản hơn và có thể khái quát hóa tốt hơn mặc dù nó phân loại sai một vài điểm của tập huấn luyện.

Hình 1.2 minh họa hai loại lời giải: một là đường ngoằn ngoèo phân tách hoàn hảo hai tập điểm xanh và đỏ, được chọn từ một họ phức tạp; loại còn lại là một đường mượt hơn được chọn từ một họ đơn giản hơn, chỉ phân biệt không hoàn hảo giữa hai tập. Chúng ta sẽ thấy rằng, nói chung, bộ dự đoán tốt nhất trên tập huấn luyện có thể không phải là bộ dự đoán tốt nhất tổng thể. Một bộ dự đoán được chọn từ một họ rất phức tạp về cơ bản có thể ghi nhớ (memorize) dữ liệu, nhưng khái quát hóa khác biệt với việc ghi nhớ các nhãn huấn luyện.

Chúng ta sẽ thấy rằng sự đánh đổi (trade-off) giữa kích thước mẫu và độ phức tạp đóng vai trò then chốt trong khái quát hóa. Khi kích thước mẫu tương đối nhỏ, việc chọn từ một họ quá phức tạp có thể dẫn đến khái quát hóa kém, hiện tượng này còn được gọi là quá khớp (overfitting). Mặt khác, với một họ quá đơn giản, có thể không đạt được độ chính xác đủ tốt, hiện tượng này được gọi là dưới khớp (underfitting).

Trong các chương tiếp theo, chúng ta sẽ phân tích chi tiết hơn bài toán khái quát hóa và sẽ tìm cách rút ra các đảm bảo lý thuyết cho việc học. Điều này sẽ phụ thuộc vào các khái niệm khác nhau về độ phức tạp mà chúng ta sẽ thảo luận kỹ lưỡng.
