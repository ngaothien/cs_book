# Chương 1: Giới Thiệu (Introduction)

Chương này trình bày phần giới thiệu sơ bộ về học máy (machine learning), bao gồm tổng quan về một số nhiệm vụ học và ứng dụng chính, các định nghĩa và thuật ngữ cơ bản, cùng việc thảo luận một số kịch bản tổng quát.

## 1.1 Học máy là gì? (What is machine learning?)

Học máy (machine learning) có thể được định nghĩa rộng rãi là các phương pháp tính toán sử dụng kinh nghiệm để cải thiện hiệu suất hoặc đưa ra các dự đoán chính xác. Ở đây, kinh nghiệm đề cập đến thông tin quá khứ có sẵn cho bộ học (learner), thường ở dạng dữ liệu điện tử được thu thập và cung cấp để phân tích. Dữ liệu này có thể ở dạng các tập huấn luyện (training sets) được con người gán nhãn số hóa, hoặc các loại thông tin khác thu được thông qua tương tác với môi trường. Trong mọi trường hợp, chất lượng và kích thước của dữ liệu là rất quan trọng đối với sự thành công của các dự đoán do bộ học đưa ra.

Một ví dụ về bài toán học là cách sử dụng một mẫu hữu hạn các tài liệu được chọn ngẫu nhiên, mỗi tài liệu được gán nhãn một chủ đề, để dự đoán chính xác chủ đề của các tài liệu chưa thấy. Rõ ràng, mẫu càng lớn thì nhiệm vụ càng dễ. Nhưng độ khó của nhiệm vụ cũng phụ thuộc vào chất lượng của các nhãn được gán cho các tài liệu trong mẫu, vì các nhãn có thể không hoàn toàn chính xác, và vào số lượng các chủ đề có thể.

Học máy bao gồm việc thiết kế các thuật toán dự đoán hiệu quả và chính xác. Như trong các lĩnh vực khác của khoa học máy tính, một số thước đo quan trọng về chất lượng của các thuật toán này là độ phức tạp thời gian và không gian của chúng. Nhưng trong học máy, chúng ta sẽ cần thêm khái niệm **độ phức tạp mẫu** (sample complexity) để đánh giá kích thước mẫu cần thiết để thuật toán học được một họ khái niệm. Tổng quát hơn, các đảm bảo học lý thuyết cho một thuật toán phụ thuộc vào độ phức tạp của các lớp khái niệm được xem xét và kích thước của mẫu huấn luyện.

Vì sự thành công của một thuật toán học phụ thuộc vào dữ liệu được sử dụng, học máy vốn có liên quan đến phân tích dữ liệu và thống kê. Tổng quát hơn, các kỹ thuật học là các phương pháp dựa trên dữ liệu, kết hợp các khái niệm cơ bản trong khoa học máy tính với ý tưởng từ thống kê, xác suất và tối ưu hóa.

## 1.2 Có thể giải quyết vấn đề gì bằng học máy? (What kind of problems can be tackled using machine learning?)

Dự đoán nhãn của một tài liệu, hay còn gọi là phân loại tài liệu (document classification), không phải là nhiệm vụ học duy nhất. Học máy cho phép một tập hợp rất rộng các ứng dụng thực tế, bao gồm:

- **Phân loại văn bản hoặc tài liệu (Text or document classification)**. Bao gồm các bài toán như gán chủ đề cho văn bản hoặc tài liệu, hoặc tự động xác định xem nội dung của một trang web có không phù hợp hay quá rõ ràng không; cũng bao gồm phát hiện thư rác (spam detection).

- **Xử lý ngôn ngữ tự nhiên (Natural Language Processing — NLP)**. Hầu hết các tác vụ trong lĩnh vực này, bao gồm gán nhãn từ loại (part-of-speech tagging), nhận dạng thực thể có tên (named-entity recognition), phân tích cú pháp phi ngữ cảnh (context-free parsing), hoặc phân tích cú pháp phụ thuộc (dependency parsing), đều được hình thành như bài toán học. Trong các bài toán này, các dự đoán có một cấu trúc nhất định. Ví dụ, trong gán nhãn từ loại, dự đoán cho một câu là một chuỗi các thẻ từ loại gán nhãn cho mỗi từ. Trong phân tích cú pháp phi ngữ cảnh, dự đoán là một cây. Đây là các ví dụ của các bài toán học phong phú hơn gọi là **bài toán dự đoán có cấu trúc** (structured prediction problems).

- **Ứng dụng xử lý tiếng nói (Speech processing)**. Bao gồm nhận dạng tiếng nói (speech recognition), tổng hợp tiếng nói (speech synthesis), xác minh người nói (speaker verification), nhận dạng người nói (speaker identification), cũng như các bài toán con như mô hình hóa ngôn ngữ (language modeling) và mô hình hóa âm học (acoustic modeling).

- **Ứng dụng thị giác máy tính (Computer vision)**. Bao gồm nhận dạng đối tượng (object recognition), nhận dạng danh tính đối tượng (object identification), phát hiện khuôn mặt (face detection), nhận dạng ký tự quang học (OCR), truy xuất hình ảnh dựa trên nội dung (content-based image retrieval), hoặc ước lượng tư thế (pose estimation).

- **Ứng dụng sinh học tính toán (Computational biology)**. Bao gồm dự đoán chức năng protein (protein function prediction), xác định các vị trí quan trọng, hoặc phân tích mạng gen và protein.

- **Nhiều bài toán khác** như phát hiện gian lận (fraud detection) cho thẻ tín dụng, điện thoại hoặc công ty bảo hiểm, xâm nhập mạng (network intrusion), học chơi các trò chơi như cờ vua, cờ backgammon, hoặc cờ vây, điều khiển tự động phương tiện (unassisted control of vehicles) như robot hoặc ô tô, chẩn đoán y tế, thiết kế hệ thống gợi ý (recommendation systems), công cụ tìm kiếm hoặc hệ thống trích xuất thông tin, đều được giải quyết bằng các kỹ thuật học máy.

Danh sách này không hề toàn diện. Hầu hết các bài toán dự đoán gặp trong thực tế đều có thể được hình thành dưới dạng bài toán học, và lĩnh vực ứng dụng thực tế của học máy tiếp tục mở rộng. Các thuật toán và kỹ thuật được thảo luận trong cuốn sách này có thể được sử dụng để suy ra giải pháp cho tất cả các bài toán này, mặc dù chúng tôi sẽ không thảo luận chi tiết các ứng dụng này.

## 1.3 Một số tác vụ học tiêu chuẩn (Some standard learning tasks)

Sau đây là một số tác vụ học máy tiêu chuẩn đã được nghiên cứu sâu rộng:

- **Phân loại (Classification)**: đây là bài toán gán một danh mục cho mỗi mục. Ví dụ, phân loại tài liệu bao gồm gán danh mục như chính trị, kinh doanh, thể thao hoặc thời tiết cho mỗi tài liệu, trong khi phân loại hình ảnh bao gồm gán cho mỗi hình ảnh một danh mục như ô tô, tàu hỏa hoặc máy bay. Số lượng danh mục trong các tác vụ như vậy thường ít hơn vài trăm, nhưng có thể lớn hơn nhiều trong một số tác vụ khó và thậm chí không giới hạn như trong OCR, phân loại văn bản hoặc nhận dạng tiếng nói.

- **Hồi quy (Regression)**: đây là bài toán dự đoán một giá trị thực cho mỗi mục. Ví dụ về hồi quy bao gồm dự đoán giá trị cổ phiếu hoặc dự đoán biến động của các biến kinh tế. Trong hồi quy, hình phạt cho dự đoán không chính xác phụ thuộc vào biên độ của sự khác biệt giữa giá trị thực và giá trị dự đoán, trái ngược với bài toán phân loại, nơi thường không có khái niệm về sự gần gũi giữa các danh mục khác nhau.

- **Xếp hạng (Ranking)**: đây là bài toán học cách sắp xếp các mục theo một tiêu chí nào đó. Tìm kiếm web, ví dụ, trả về các trang web liên quan đến một truy vấn tìm kiếm, là ví dụ xếp hạng kinh điển. Nhiều bài toán xếp hạng tương tự khác xuất hiện trong bối cảnh thiết kế các hệ thống trích xuất thông tin hoặc xử lý ngôn ngữ tự nhiên.

- **Phân cụm (Clustering)**: đây là bài toán phân chia một tập hợp các mục thành các tập con đồng nhất. Phân cụm thường được sử dụng để phân tích các tập dữ liệu rất lớn. Ví dụ, trong bối cảnh phân tích mạng xã hội, các thuật toán phân cụm cố gắng xác định các cộng đồng tự nhiên trong các nhóm người lớn.

- **Giảm chiều hoặc học đa tạp (Dimensionality reduction or manifold learning)**: bài toán này bao gồm chuyển đổi biểu diễn ban đầu của các mục thành biểu diễn có số chiều thấp hơn trong khi bảo toàn một số tính chất của biểu diễn ban đầu. Một ví dụ phổ biến bao gồm tiền xử lý hình ảnh số trong các tác vụ thị giác máy tính.

Các mục tiêu thực tế chính của học máy bao gồm tạo ra các dự đoán chính xác cho các mục chưa thấy và thiết kế các thuật toán hiệu quả, mạnh mẽ để tạo ra các dự đoán này, ngay cả đối với các bài toán quy mô lớn. Để làm được điều đó, một số câu hỏi thuật toán và lý thuyết xuất hiện. Một số câu hỏi cơ bản bao gồm: Những họ khái niệm nào thực sự có thể được học, và trong điều kiện nào? Các khái niệm này có thể được học tốt đến mức nào về mặt tính toán?

## 1.4 Các giai đoạn học (Learning stages)

Ở đây, chúng tôi sẽ sử dụng bài toán kinh điển về phát hiện thư rác làm ví dụ minh họa để trình bày một số định nghĩa cơ bản và mô tả việc sử dụng và đánh giá các thuật toán học máy trong thực tế, bao gồm các giai đoạn khác nhau của chúng.

Phát hiện thư rác (spam detection) là bài toán học cách tự động phân loại các tin nhắn email thành thư rác hoặc không phải thư rác. Sau đây là danh sách các định nghĩa và thuật ngữ thường được sử dụng trong học máy:

- **Ví dụ / Mẫu (Examples)**: Các mục hoặc thực thể dữ liệu được sử dụng cho việc học hoặc đánh giá. Trong bài toán thư rác, các ví dụ này tương ứng với bộ sưu tập các tin nhắn email mà chúng ta sẽ sử dụng để học và kiểm thử.

- **Đặc trưng (Features)**: Tập hợp các thuộc tính, thường được biểu diễn dưới dạng vectơ, liên kết với một ví dụ. Trong trường hợp tin nhắn email, một số đặc trưng liên quan có thể bao gồm độ dài tin nhắn, tên người gửi, các đặc điểm khác nhau của phần đầu thư (header), sự hiện diện của một số từ khóa nhất định trong nội dung tin nhắn, v.v.

- **Nhãn (Labels)**: Các giá trị hoặc danh mục được gán cho các ví dụ. Trong các bài toán phân loại, các ví dụ được gán các danh mục cụ thể, ví dụ, danh mục thư rác và không phải thư rác trong bài toán phân loại nhị phân. Trong hồi quy, các mục được gán nhãn có giá trị thực.

- **Siêu tham số (Hyperparameters)**: Các tham số tự do không được xác định bởi thuật toán học, mà được chỉ định như đầu vào cho thuật toán học.

- **Mẫu huấn luyện (Training sample)**: Các ví dụ được sử dụng để huấn luyện thuật toán học. Trong bài toán thư rác, mẫu huấn luyện bao gồm một tập hợp các ví dụ email cùng với các nhãn liên quan. Mẫu huấn luyện thay đổi cho các kịch bản học khác nhau, như được mô tả trong mục 1.5.

- **Mẫu xác thực (Validation sample)**: Các ví dụ được sử dụng để điều chỉnh các tham số của thuật toán học khi làm việc với dữ liệu có nhãn. Mẫu xác thực được sử dụng để chọn các giá trị phù hợp cho các tham số tự do (siêu tham số) của thuật toán học.

- **Mẫu kiểm thử (Test sample)**: Các ví dụ được sử dụng để đánh giá hiệu suất của thuật toán học. Mẫu kiểm thử tách biệt khỏi dữ liệu huấn luyện và xác thực và không được cung cấp trong giai đoạn học. Trong bài toán thư rác, mẫu kiểm thử bao gồm một bộ sưu tập các ví dụ email mà thuật toán học phải dự đoán nhãn dựa trên đặc trưng. Các dự đoán này sau đó được so sánh với nhãn của mẫu kiểm thử để đo lường hiệu suất của thuật toán.

- **Hàm mất mát (Loss function)**: Một hàm đo sự khác biệt, hay mất mát, giữa nhãn dự đoán và nhãn thực. Ký hiệu tập hợp tất cả các nhãn là $Y$ và tập hợp các dự đoán có thể là $Y'$, một hàm mất mát $L$ là một ánh xạ $L: Y \times Y' \to \mathbb{R}_+$. Trong hầu hết các trường hợp, $Y' = Y$ và hàm mất mát bị chặn, nhưng các điều kiện này không phải lúc nào cũng đúng. Các ví dụ phổ biến về hàm mất mát bao gồm mất mát zero-one (hoặc phân loại sai) được định nghĩa trên $\{-1, +1\} \times \{-1, +1\}$ bởi $L(y, y') = \mathbf{1}_{y' \neq y}$ và mất mát bình phương được định nghĩa trên $I \times I$ bởi $L(y, y') = (y' - y)^2$, trong đó $I \subseteq \mathbb{R}$ thường là một khoảng.

![Hình 1.1: Minh họa các giai đoạn điển hình của quá trình học](images/fig1_1.png)

*Hình 1.1: Minh họa các giai đoạn điển hình của quá trình học. Dữ liệu có nhãn → đặc trưng → mẫu huấn luyện → thuật toán $A(\Theta)$ → chọn tham số (sử dụng dữ liệu xác thực) → $A(\Theta_0)$ → đánh giá (trên mẫu kiểm thử).*

Hình 1.1 minh họa các giai đoạn khác nhau của quá trình học. Đầu tiên, chúng ta chia dữ liệu có nhãn thành mẫu huấn luyện và mẫu kiểm thử (cùng với mẫu xác thực). Mẫu có nhãn thường được phân chia ngẫu nhiên. Mặc dù không có quy tắc tuyệt đối liên quan đến tỷ lệ dữ liệu được sử dụng cho mỗi mục đích, nhưng do kích thước mẫu có nhãn thường tương đối nhỏ, lượng dữ liệu huấn luyện thường được chọn lớn hơn dữ liệu kiểm thử vì hiệu suất học trực tiếp phụ thuộc vào mẫu huấn luyện.

Tiếp theo, chúng ta liên kết các đặc trưng phù hợp với các ví dụ. Đây là bước quan trọng trong thiết kế giải pháp học máy. Các đặc trưng hữu ích có thể hướng dẫn thuật toán học một cách hiệu quả, trong khi các đặc trưng kém hoặc không mang thông tin có thể gây sai lệch. Mặc dù rất quan trọng, phần lớn việc lựa chọn đặc trưng được để lại cho người dùng. Sự lựa chọn này phản ánh kiến thức tiên nghiệm (prior knowledge) của người dùng về tác vụ học, mà trong thực tế có thể có ảnh hưởng đáng kể đến kết quả hiệu suất.

Bây giờ, chúng ta sử dụng các đặc trưng đã chọn để huấn luyện thuật toán học $A$ bằng cách điều chỉnh các giá trị của các tham số tự do $\Theta$ (còn gọi là siêu tham số). Đối với mỗi giá trị của các tham số này, thuật toán chọn một giả thuyết khác từ tập giả thuyết. Chúng ta chọn giả thuyết cho kết quả hiệu suất tốt nhất trên mẫu xác thực ($\Theta_0$). Cuối cùng, sử dụng giả thuyết đó, chúng ta dự đoán nhãn của các ví dụ trong mẫu kiểm thử. Hiệu suất của thuật toán được đánh giá bằng cách sử dụng hàm mất mát liên quan đến tác vụ, ví dụ, mất mát zero-one trong tác vụ phát hiện thư rác, để so sánh nhãn dự đoán và nhãn thực. Do đó, hiệu suất của thuật toán tất nhiên được đánh giá dựa trên lỗi kiểm thử (test error) chứ không phải lỗi trên mẫu huấn luyện.

## 1.5 Các kịch bản học (Learning scenarios)

Tiếp theo, chúng tôi mô tả ngắn gọn một số kịch bản học máy phổ biến. Các kịch bản này khác nhau ở loại dữ liệu huấn luyện có sẵn cho bộ học, thứ tự và phương pháp nhận dữ liệu huấn luyện, cũng như dữ liệu kiểm thử được sử dụng để đánh giá thuật toán học.

- **Học có giám sát (Supervised learning)**: Bộ học nhận một tập hợp các ví dụ có nhãn làm dữ liệu huấn luyện và đưa ra dự đoán cho tất cả các điểm chưa thấy. Đây là kịch bản phổ biến nhất liên quan đến các bài toán phân loại, hồi quy và xếp hạng. Bài toán phát hiện thư rác được thảo luận trong phần trước là một ví dụ về học có giám sát.

- **Học không giám sát (Unsupervised learning)**: Bộ học chỉ nhận dữ liệu huấn luyện không có nhãn và đưa ra dự đoán cho tất cả các điểm chưa thấy. Vì nói chung không có ví dụ nào được gán nhãn trong thiết lập này, có thể khó đánh giá định lượng hiệu suất của bộ học. Phân cụm (clustering) và giảm chiều (dimensionality reduction) là ví dụ về các bài toán học không giám sát.

- **Học bán giám sát (Semi-supervised learning)**: Bộ học nhận mẫu huấn luyện bao gồm cả dữ liệu có nhãn và không có nhãn, và đưa ra dự đoán cho tất cả các điểm chưa thấy. Học bán giám sát phổ biến trong các thiết lập mà dữ liệu không nhãn dễ tiếp cận nhưng nhãn tốn kém để có được. Các loại bài toán khác nhau phát sinh trong ứng dụng, bao gồm các tác vụ phân loại, hồi quy hoặc xếp hạng, có thể được hình thành dưới dạng các trường hợp của học bán giám sát. Hy vọng là phân phối của dữ liệu không nhãn có thể giúp bộ học đạt hiệu suất tốt hơn so với thiết lập giám sát. Phân tích các điều kiện mà điều này thực sự có thể đạt được là chủ đề của nhiều nghiên cứu học máy lý thuyết và ứng dụng hiện đại.

- **Suy luận truyền dẫn (Transductive inference)**: Như trong kịch bản bán giám sát, bộ học nhận mẫu huấn luyện có nhãn cùng với một tập hợp các điểm kiểm thử không nhãn. Tuy nhiên, mục tiêu của suy luận truyền dẫn là chỉ dự đoán nhãn cho các điểm kiểm thử cụ thể này. Suy luận truyền dẫn dường như là một tác vụ dễ hơn và phù hợp với kịch bản gặp trong nhiều ứng dụng hiện đại. Tuy nhiên, như trong thiết lập bán giám sát, các giả định mà hiệu suất tốt hơn có thể đạt được vẫn là câu hỏi nghiên cứu chưa được giải quyết hoàn toàn.

- **Học trực tuyến (On-line learning)**: Trái ngược với các kịch bản trước, kịch bản trực tuyến bao gồm nhiều vòng lặp trong đó các giai đoạn huấn luyện và kiểm thử được xen kẽ. Tại mỗi vòng, bộ học nhận một điểm huấn luyện không nhãn, đưa ra dự đoán, nhận nhãn thực, và chịu một mất mát. Mục tiêu trong thiết lập trực tuyến là tối thiểu hóa mất mát tích lũy qua tất cả các vòng hoặc tối thiểu hóa độ hối tiếc (regret) — tức sự khác biệt giữa mất mát tích lũy phải chịu và mất mát của chuyên gia tốt nhất nhìn lại (best expert in hindsight). Không giống như các thiết lập đã thảo luận trước đó, không có giả định phân phối nào được đặt ra trong học trực tuyến. Trên thực tế, các thực thể và nhãn của chúng có thể được chọn theo hướng đối nghịch (adversarially) trong kịch bản này.

- **Học tăng cường (Reinforcement learning)**: Các giai đoạn huấn luyện và kiểm thử cũng được xen kẽ trong học tăng cường. Để thu thập thông tin, bộ học chủ động tương tác với môi trường và trong một số trường hợp ảnh hưởng đến môi trường, và nhận phần thưởng tức thời (immediate reward) cho mỗi hành động. Mục tiêu của bộ học là tối đa hóa phần thưởng qua một chuỗi hành động và lần lặp với môi trường. Tuy nhiên, không có phản hồi phần thưởng dài hạn nào được cung cấp bởi môi trường, và bộ học đối mặt với **thế lưỡng nan khám phá–khai thác** (exploration versus exploitation dilemma), vì phải chọn giữa khám phá các hành động chưa biết để thu thêm thông tin và khai thác thông tin đã thu thập được.

- **Học chủ động (Active learning)**: Bộ học thu thập các ví dụ huấn luyện một cách thích ứng hoặc tương tác, thường bằng cách truy vấn một bộ tiên tri (oracle) để yêu cầu nhãn cho các điểm mới. Mục tiêu trong học chủ động là đạt hiệu suất tương đương với kịch bản học có giám sát tiêu chuẩn (hoặc kịch bản học thụ động), nhưng với ít ví dụ có nhãn hơn. Học chủ động thường được sử dụng trong các ứng dụng mà nhãn tốn kém để có được, ví dụ các ứng dụng sinh học tính toán.

Trong thực tế, nhiều kịch bản học trung gian và phức tạp hơn khác có thể được gặp.

## 1.6 Khái quát hóa (Generalization)

Học máy về cơ bản là về **khái quát hóa** (generalization). Ví dụ, kịch bản học có giám sát tiêu chuẩn bao gồm sử dụng một mẫu hữu hạn các ví dụ có nhãn để đưa ra các dự đoán chính xác về các ví dụ chưa thấy. Bài toán thường được hình thành dưới dạng chọn một hàm từ một **tập giả thuyết** (hypothesis set), là một tập con của họ tất cả các hàm. Hàm được chọn sau đó được sử dụng để gán nhãn cho tất cả các thực thể, bao gồm cả các ví dụ chưa thấy.

Nên chọn tập giả thuyết như thế nào? Với tập giả thuyết phong phú hoặc phức tạp, bộ học có thể chọn một hàm hoặc bộ dự đoán **nhất quán** (consistent) với mẫu huấn luyện, tức là không mắc lỗi trên mẫu huấn luyện. Với họ ít phức tạp hơn, việc mắc một số lỗi trên mẫu huấn luyện có thể là không tránh khỏi. Nhưng cái nào sẽ dẫn đến khái quát hóa tốt hơn? Chúng ta nên định nghĩa độ phức tạp của tập giả thuyết như thế nào?

![Hình 1.2: So sánh hai mặt phân tách](images/fig1_2.png)

*Hình 1.2: Đường zig-zag trên bảng bên trái nhất quán trên mẫu huấn luyện xanh dương và đỏ, nhưng nó là một mặt phân tách phức tạp không có khả năng khái quát hóa tốt cho dữ liệu chưa thấy. Ngược lại, mặt quyết định trên bảng bên phải đơn giản hơn và có thể khái quát hóa tốt hơn mặc dù phân loại sai một vài điểm trong mẫu huấn luyện.*

Hình 1.2 minh họa hai loại giải pháp: một là đường zig-zag phân tách hoàn hảo hai quần thể điểm xanh dương và đỏ, được chọn từ một họ phức tạp; cái còn lại là đường mượt hơn được chọn từ họ đơn giản hơn, chỉ phân biệt không hoàn hảo giữa hai tập. Chúng ta sẽ thấy rằng, nói chung, bộ dự đoán tốt nhất trên mẫu huấn luyện có thể không phải là bộ dự đoán tốt nhất tổng thể. Một bộ dự đoán được chọn từ một họ rất phức tạp về cơ bản có thể **ghi nhớ** (memorize) dữ liệu, nhưng khái quát hóa khác với việc ghi nhớ nhãn huấn luyện.

Chúng ta sẽ thấy rằng sự đánh đổi giữa kích thước mẫu và độ phức tạp đóng vai trò quan trọng trong khái quát hóa. Khi kích thước mẫu tương đối nhỏ, việc chọn từ một họ quá phức tạp có thể dẫn đến khái quát hóa kém, còn được gọi là **quá khớp** (overfitting). Mặt khác, với họ quá đơn giản, có thể không đạt được độ chính xác đủ, được gọi là **dưới khớp** (underfitting).

Trong các chương tiếp theo, chúng ta sẽ phân tích chi tiết hơn bài toán khái quát hóa và sẽ tìm cách suy ra các đảm bảo lý thuyết cho việc học. Điều này sẽ phụ thuộc vào các khái niệm khác nhau về độ phức tạp mà chúng ta sẽ thảo luận kỹ lưỡng.
