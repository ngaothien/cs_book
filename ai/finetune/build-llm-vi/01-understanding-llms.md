# Chương 1: Hiểu về mô hình ngôn ngữ lớn

Các mô hình ngôn ngữ lớn (LLM), chẳng hạn như những mô hình được cung cấp trong ChatGPT của OpenAI, là các mô hình mạng nơ-ron sâu đã được phát triển trong vài năm qua. Chúng đã mở ra một kỷ nguyên mới cho xử lý ngôn ngữ tự nhiên (NLP). Trước sự ra đời của LLM, các phương pháp truyền thống xuất sắc trong các tác vụ phân loại như phân loại email spam và nhận dạng mẫu đơn giản có thể được nắm bắt bằng các quy tắc thủ công hoặc các mô hình đơn giản hơn. Tuy nhiên, chúng thường hoạt động kém trong các tác vụ ngôn ngữ đòi hỏi khả năng hiểu và tạo sinh phức tạp, chẳng hạn như phân tích các hướng dẫn chi tiết, tiến hành phân tích ngữ cảnh, và tạo ra văn bản gốc mạch lạc và phù hợp ngữ cảnh. Ví dụ, các thế hệ mô hình ngôn ngữ trước đó không thể viết email từ danh sách từ khóa — một tác vụ tầm thường đối với các LLM đương đại.

*Chương này bao gồm:*
- *Giải thích tổng quan về các khái niệm nền tảng đằng sau mô hình ngôn ngữ lớn (LLM)*
- *Hiểu sâu về kiến trúc transformer mà LLM được phát triển từ đó*
- *Kế hoạch xây dựng một LLM từ đầu*

---

LLM có khả năng đáng chú ý trong việc hiểu, tạo ra và diễn giải ngôn ngữ con người. Tuy nhiên, điều quan trọng cần làm rõ là khi chúng ta nói mô hình ngôn ngữ "hiểu", chúng ta có nghĩa là chúng có thể xử lý và tạo ra văn bản theo cách có vẻ mạch lạc và phù hợp ngữ cảnh, không phải là chúng sở hữu ý thức hoặc sự thấu hiểu giống con người.

Được hỗ trợ bởi những tiến bộ trong deep learning, là một tập con của machine learning và trí tuệ nhân tạo (AI) tập trung vào mạng nơ-ron, LLM được huấn luyện trên lượng dữ liệu văn bản khổng lồ. Huấn luyện quy mô lớn này cho phép LLM nắm bắt thông tin ngữ cảnh sâu hơn và các sắc thái của ngôn ngữ con người so với các phương pháp trước đây. Kết quả là, LLM đã cải thiện đáng kể hiệu suất trong nhiều tác vụ NLP, bao gồm dịch văn bản, phân tích cảm xúc, trả lời câu hỏi, và nhiều hơn nữa.

Một sự khác biệt quan trọng khác giữa LLM đương đại và các mô hình NLP trước đó là các mô hình NLP trước đó thường được thiết kế cho các tác vụ cụ thể, chẳng hạn như phân loại văn bản, dịch ngôn ngữ, v.v. Mặc dù những mô hình NLP trước đó xuất sắc trong các ứng dụng hẹp của chúng, LLM thể hiện khả năng rộng hơn qua nhiều tác vụ NLP.

Thành công đằng sau LLM có thể được quy cho kiến trúc transformer làm nền tảng cho nhiều LLM và lượng dữ liệu khổng lồ mà LLM được huấn luyện, cho phép chúng nắm bắt nhiều loại sắc thái ngôn ngữ, ngữ cảnh và mẫu mà sẽ rất khó để mã hóa thủ công.

Sự chuyển đổi sang triển khai các mô hình dựa trên kiến trúc transformer và sử dụng bộ dữ liệu huấn luyện lớn để huấn luyện LLM đã biến đổi căn bản NLP, cung cấp các công cụ có khả năng hơn để hiểu và tương tác với ngôn ngữ con người.

Cuộc thảo luận sau đây đặt nền tảng để hoàn thành mục tiêu chính của cuốn sách này: hiểu LLM bằng cách triển khai một LLM giống ChatGPT dựa trên kiến trúc transformer từng bước trong code.

## 1.1 LLM là gì?

LLM là mạng nơ-ron được thiết kế để hiểu, tạo ra và phản hồi văn bản giống con người. Những mô hình này là mạng nơ-ron sâu được huấn luyện trên lượng dữ liệu văn bản khổng lồ, đôi khi bao gồm phần lớn toàn bộ văn bản có sẵn công khai trên internet.

"Lớn" trong "mô hình ngôn ngữ lớn" đề cập đến cả kích thước mô hình về số lượng tham số (parameters) và bộ dữ liệu khổng lồ mà nó được huấn luyện. Các mô hình như thế này thường có hàng chục hoặc thậm chí hàng trăm tỷ tham số, là các trọng số (weights) có thể điều chỉnh trong mạng được tối ưu hóa trong quá trình huấn luyện để dự đoán từ tiếp theo trong một chuỗi. Dự đoán từ tiếp theo hợp lý vì nó khai thác bản chất tuần tự vốn có của ngôn ngữ để huấn luyện mô hình hiểu ngữ cảnh, cấu trúc và mối quan hệ trong văn bản. Tuy nhiên, đây là một tác vụ rất đơn giản, và vì thế nhiều nhà nghiên cứu ngạc nhiên rằng nó có thể tạo ra các mô hình có năng lực như vậy. Trong các chương sau, chúng ta sẽ thảo luận và triển khai quy trình huấn luyện dự đoán từ tiếp theo từng bước.

LLM sử dụng kiến trúc gọi là transformer, cho phép chúng tập trung có chọn lọc vào các phần khác nhau của đầu vào khi đưa ra dự đoán, làm cho chúng đặc biệt giỏi trong việc xử lý các sắc thái và độ phức tạp của ngôn ngữ con người.

Vì LLM có khả năng tạo văn bản, LLM cũng thường được gọi là một dạng trí tuệ nhân tạo tạo sinh (generative artificial intelligence), thường được viết tắt là AI tạo sinh hoặc GenAI. Như minh họa trong hình 1.1, AI bao gồm lĩnh vực rộng hơn về tạo ra các máy có thể thực hiện các tác vụ đòi hỏi trí thông minh giống con người, bao gồm hiểu ngôn ngữ, nhận dạng mẫu và đưa ra quyết định, và bao gồm các lĩnh vực con như machine learning và deep learning.

Các thuật toán được sử dụng để triển khai AI là trọng tâm của lĩnh vực machine learning. Cụ thể, machine learning bao gồm việc phát triển các thuật toán có thể học từ dữ liệu và đưa ra dự đoán hoặc quyết định dựa trên dữ liệu mà không cần được lập trình rõ ràng. Để minh họa điều này, hãy tưởng tượng bộ lọc spam như một ứng dụng thực tế của machine learning. Thay vì viết thủ công các quy tắc để nhận diện email spam, một thuật toán machine learning được cho ăn các ví dụ email được gắn nhãn là spam và email hợp lệ. Bằng cách giảm thiểu lỗi trong các dự đoán trên tập dữ liệu huấn luyện, mô hình sau đó học cách nhận ra các mẫu và đặc điểm chỉ thị spam, cho phép nó phân loại email mới là spam hoặc không spam.

[Hình 1.1: Như mô tả phân cấp này về mối quan hệ giữa các lĩnh vực khác nhau gợi ý, LLM đại diện cho một ứng dụng cụ thể của kỹ thuật deep learning, sử dụng khả năng xử lý và tạo ra văn bản giống con người. Deep learning là một nhánh chuyên biệt của machine learning tập trung vào sử dụng mạng nơ-ron nhiều lớp. Machine learning và deep learning là các lĩnh vực nhằm triển khai các thuật toán cho phép máy tính học từ dữ liệu và thực hiện các tác vụ thường đòi hỏi trí thông minh con người.]

Như minh họa trong hình 1.1, deep learning là tập con của machine learning tập trung vào sử dụng mạng nơ-ron với ba lớp trở lên (còn gọi là mạng nơ-ron sâu) để mô hình hóa các mẫu và trừu tượng phức tạp trong dữ liệu. Ngược lại với deep learning, machine learning truyền thống yêu cầu trích xuất đặc trưng thủ công (manual feature extraction). Điều này có nghĩa là các chuyên gia con người cần xác định và chọn các đặc trưng phù hợp nhất cho mô hình.

Mặc dù lĩnh vực AI hiện nay bị chi phối bởi machine learning và deep learning, nó cũng bao gồm các phương pháp khác — ví dụ, sử dụng hệ thống dựa trên quy tắc, thuật toán di truyền, hệ thống chuyên gia, logic mờ, hoặc suy luận ký hiệu.

Quay lại ví dụ phân loại spam, trong machine learning truyền thống, các chuyên gia con người có thể trích xuất thủ công các đặc trưng từ văn bản email chẳng hạn như tần suất của một số từ kích hoạt nhất định (ví dụ, "giải thưởng", "chiến thắng", "miễn phí"), số lượng dấu chấm than, sử dụng tất cả từ viết hoa, hoặc sự hiện diện của các liên kết đáng ngờ. Bộ dữ liệu này, được tạo dựa trên các đặc trưng do chuyên gia xác định, sau đó sẽ được sử dụng để huấn luyện mô hình. Ngược lại với machine learning truyền thống, deep learning không yêu cầu trích xuất đặc trưng thủ công. Điều này có nghĩa là các chuyên gia con người không cần xác định và chọn các đặc trưng phù hợp nhất cho mô hình deep learning. (Tuy nhiên, cả machine learning truyền thống và deep learning cho phân loại spam vẫn yêu cầu thu thập nhãn, chẳng hạn như spam hoặc không spam, cần được thu thập bởi chuyên gia hoặc người dùng.)

Hãy xem xét một số vấn đề mà LLM có thể giải quyết ngày nay, các thách thức mà LLM giải quyết, và kiến trúc LLM tổng quát mà chúng ta sẽ triển khai sau.

## 1.2 Ứng dụng của LLM

Nhờ khả năng tiên tiến trong việc phân tích và hiểu dữ liệu văn bản phi cấu trúc, LLM có phạm vi ứng dụng rộng rãi qua nhiều lĩnh vực. Ngày nay, LLM được sử dụng cho dịch máy, tạo văn bản mới (xem hình 1.2), phân tích cảm xúc, tóm tắt văn bản, và nhiều tác vụ khác. LLM gần đây đã được sử dụng cho sáng tạo nội dung, chẳng hạn như viết tiểu thuyết, bài viết, và thậm chí cả code máy tính.

LLM cũng có thể cung cấp năng lượng cho các chatbot và trợ lý ảo tinh vi, chẳng hạn như ChatGPT của OpenAI hoặc Gemini của Google (trước đây gọi là Bard), có thể trả lời truy vấn của người dùng và bổ sung cho các công cụ tìm kiếm truyền thống như Google Search hoặc Microsoft Bing.

Hơn nữa, LLM có thể được sử dụng để truy xuất kiến thức hiệu quả từ khối lượng lớn văn bản trong các lĩnh vực chuyên biệt như y học hoặc luật. Điều này bao gồm sàng lọc tài liệu, tóm tắt các đoạn dài, và trả lời các câu hỏi kỹ thuật.

Nói ngắn gọn, LLM vô giá cho việc tự động hóa hầu hết mọi tác vụ liên quan đến phân tích và tạo văn bản. Ứng dụng của chúng gần như vô tận, và khi chúng ta tiếp tục đổi mới và khám phá các cách mới để sử dụng các mô hình này, rõ ràng rằng LLM có tiềm năng định nghĩa lại mối quan hệ của chúng ta với công nghệ, làm cho nó mang tính hội thoại, trực giác và dễ tiếp cận hơn.

Chúng ta sẽ tập trung vào việc hiểu cách LLM hoạt động từ nền tảng, viết code một LLM có thể tạo văn bản. Bạn cũng sẽ tìm hiểu về các kỹ thuật cho phép LLM thực hiện các truy vấn, từ trả lời câu hỏi đến tóm tắt văn bản, dịch văn bản sang các ngôn ngữ khác, và nhiều hơn nữa. Nói cách khác, bạn sẽ học cách các trợ lý LLM phức tạp như ChatGPT hoạt động bằng cách xây dựng một trợ lý từng bước.

[Hình 1.2: Giao diện LLM cho phép giao tiếp ngôn ngữ tự nhiên giữa người dùng và hệ thống AI. Ảnh chụp màn hình này cho thấy ChatGPT viết một bài thơ theo yêu cầu cụ thể của người dùng.]

## 1.3 Các giai đoạn xây dựng và sử dụng LLM

Tại sao chúng ta nên xây dựng LLM riêng? Viết code một LLM từ nền tảng là bài tập xuất sắc để hiểu cơ chế và hạn chế của nó. Ngoài ra, nó trang bị cho chúng ta kiến thức cần thiết để tiền huấn luyện hoặc tinh chỉnh các kiến trúc LLM mã nguồn mở hiện có cho bộ dữ liệu hoặc tác vụ thuộc lĩnh vực cụ thể của chúng ta.

> **LƯU Ý:** Hầu hết LLM ngày nay được triển khai bằng thư viện deep learning PyTorch, đây là thứ chúng ta sẽ sử dụng. Độc giả có thể tìm thấy giới thiệu toàn diện về PyTorch trong phụ lục A.

Nghiên cứu đã chỉ ra rằng khi nói đến hiệu suất mô hình hóa, các LLM được xây dựng tùy chỉnh — những LLM được thiết kế riêng cho các tác vụ hoặc lĩnh vực cụ thể — có thể vượt trội hơn các LLM đa mục đích, chẳng hạn như những LLM được cung cấp bởi ChatGPT, được thiết kế cho nhiều ứng dụng. Ví dụ bao gồm BloombergGPT (chuyên biệt cho tài chính) và các LLM được thiết kế riêng cho trả lời câu hỏi y khoa (xem phụ lục B để biết thêm chi tiết).

Sử dụng LLM xây dựng tùy chỉnh mang lại một số lợi thế, đặc biệt về quyền riêng tư dữ liệu. Ví dụ, các công ty có thể không muốn chia sẻ dữ liệu nhạy cảm với các nhà cung cấp LLM bên thứ ba như OpenAI do lo ngại về tính bảo mật. Ngoài ra, việc phát triển các LLM tùy chỉnh nhỏ hơn cho phép triển khai trực tiếp trên thiết bị khách hàng, chẳng hạn như máy tính xách tay và điện thoại thông minh, đây là điều mà các công ty như Apple đang khám phá.

Việc triển khai cục bộ này có thể giảm đáng kể độ trễ và giảm chi phí liên quan đến máy chủ. Hơn nữa, LLM tùy chỉnh cho phép nhà phát triển hoàn toàn tự chủ, cho phép họ kiểm soát các cập nhật và sửa đổi cho mô hình khi cần.

Quy trình tổng quát tạo một LLM bao gồm tiền huấn luyện (pretraining) và tinh chỉnh (fine-tuning). "Pre" trong "pretraining" đề cập đến giai đoạn ban đầu nơi một mô hình như LLM được huấn luyện trên bộ dữ liệu lớn, đa dạng để phát triển hiểu biết rộng về ngôn ngữ. Mô hình tiền huấn luyện này sau đó đóng vai trò là tài nguyên nền tảng có thể được tinh chỉnh thêm thông qua fine-tuning, một quy trình mà mô hình được huấn luyện cụ thể trên bộ dữ liệu hẹp hơn, cụ thể hơn cho các tác vụ hoặc lĩnh vực cụ thể. Phương pháp huấn luyện hai giai đoạn bao gồm tiền huấn luyện và tinh chỉnh này được mô tả trong hình 1.3.

Bước đầu tiên trong việc tạo LLM là huấn luyện nó trên một tập dữ liệu văn bản lớn, đôi khi được gọi là văn bản thô (raw text). Ở đây, "thô" đề cập đến thực tế rằng dữ liệu này chỉ là văn bản thông thường không có thông tin gắn nhãn nào. (Có thể áp dụng lọc, chẳng hạn như loại bỏ ký tự định dạng hoặc tài liệu bằng ngôn ngữ không xác định.)

> **LƯU Ý:** Độc giả có nền tảng machine learning có thể lưu ý rằng thông tin gắn nhãn thường được yêu cầu cho các mô hình machine learning truyền thống và mạng nơ-ron sâu được huấn luyện qua mô hình học có giám sát thông thường. Tuy nhiên, đây không phải trường hợp cho giai đoạn tiền huấn luyện LLM. Trong giai đoạn này, LLM sử dụng học tự giám sát (self-supervised learning), nơi mô hình tự tạo nhãn của mình từ dữ liệu đầu vào.

[Hình 1.3: Tiền huấn luyện LLM bao gồm dự đoán từ tiếp theo trên các bộ dữ liệu văn bản lớn. Một LLM tiền huấn luyện sau đó có thể được tinh chỉnh bằng cách sử dụng bộ dữ liệu có nhãn nhỏ hơn.]

Giai đoạn huấn luyện đầu tiên này của LLM cũng được gọi là tiền huấn luyện, tạo ra một LLM tiền huấn luyện ban đầu, thường được gọi là mô hình cơ sở hoặc mô hình nền tảng (base hoặc foundation model). Một ví dụ điển hình của mô hình như vậy là mô hình GPT-3 (tiền thân của mô hình gốc được cung cấp trong ChatGPT). Mô hình này có khả năng hoàn thành văn bản — tức là hoàn thiện nửa câu do người dùng cung cấp. Nó cũng có khả năng few-shot hạn chế, nghĩa là nó có thể học cách thực hiện các tác vụ mới dựa trên chỉ một vài ví dụ thay vì cần dữ liệu huấn luyện rộng rãi.

Sau khi có được LLM tiền huấn luyện từ việc huấn luyện trên các bộ dữ liệu văn bản lớn, nơi LLM được huấn luyện để dự đoán từ tiếp theo trong văn bản, chúng ta có thể huấn luyện thêm LLM trên dữ liệu có nhãn, còn được gọi là tinh chỉnh.

Hai loại tinh chỉnh LLM phổ biến nhất là tinh chỉnh theo hướng dẫn (instruction fine-tuning) và tinh chỉnh cho phân loại (classification fine-tuning). Trong tinh chỉnh theo hướng dẫn, bộ dữ liệu có nhãn bao gồm các cặp hướng dẫn và câu trả lời, chẳng hạn như truy vấn dịch văn bản kèm theo văn bản đã dịch chính xác. Trong tinh chỉnh cho phân loại, bộ dữ liệu có nhãn bao gồm các văn bản và nhãn lớp liên quan — ví dụ, email được liên kết với nhãn "spam" và "không spam".

Chúng ta sẽ bao gồm các triển khai code cho tiền huấn luyện và tinh chỉnh LLM, và chúng ta sẽ đi sâu hơn vào chi tiết cụ thể của cả tinh chỉnh theo hướng dẫn và phân loại sau khi tiền huấn luyện một LLM cơ sở.

## 1.4 Giới thiệu kiến trúc transformer

Hầu hết LLM hiện đại dựa trên kiến trúc transformer, là kiến trúc mạng nơ-ron sâu được giới thiệu trong bài báo năm 2017 "Attention Is All You Need" (https://arxiv.org/abs/1706.03762). Để hiểu LLM, chúng ta phải hiểu transformer gốc, được phát triển cho dịch máy, dịch văn bản tiếng Anh sang tiếng Đức và tiếng Pháp. Phiên bản đơn giản hóa của kiến trúc transformer được mô tả trong hình 1.4.

Kiến trúc transformer bao gồm hai module con: encoder và decoder. Module encoder xử lý văn bản đầu vào và mã hóa nó thành một loạt các biểu diễn số (numerical representations) hoặc vector nắm bắt thông tin ngữ cảnh của đầu vào. Sau đó, module decoder lấy các vector được mã hóa này và tạo ra văn bản đầu ra. Trong tác vụ dịch thuật, ví dụ, encoder sẽ mã hóa văn bản từ ngôn ngữ nguồn thành vector, và decoder sẽ giải mã các vector này để tạo văn bản ở ngôn ngữ đích. Cả encoder và decoder đều bao gồm nhiều lớp được kết nối bởi cơ chế gọi là self-attention. Bạn có thể có nhiều câu hỏi về cách đầu vào được tiền xử lý và mã hóa. Những câu hỏi này sẽ được giải quyết trong triển khai từng bước ở các chương tiếp theo.

Thành phần chính của transformer và LLM là cơ chế self-attention (không được hiển thị), cho phép mô hình đánh giá mức độ quan trọng của các từ hoặc token khác nhau trong một chuỗi tương đối với nhau. Cơ chế này cho phép mô hình nắm bắt các phụ thuộc tầm xa (long-range dependencies) và mối quan hệ ngữ cảnh trong dữ liệu đầu vào, nâng cao khả năng tạo ra đầu ra mạch lạc và phù hợp ngữ cảnh. Tuy nhiên, do độ phức tạp của nó, chúng ta sẽ hoãn giải thích thêm đến chương 3, nơi chúng ta sẽ thảo luận và triển khai nó từng bước.

[Hình 1.4: Mô tả đơn giản hóa kiến trúc transformer gốc, là mô hình deep learning cho dịch ngôn ngữ. Transformer bao gồm hai phần: (a) encoder xử lý văn bản đầu vào và tạo ra biểu diễn embedding (biểu diễn số nắm bắt nhiều yếu tố khác nhau trong các chiều khác nhau) của văn bản mà (b) decoder có thể sử dụng để tạo văn bản đã dịch từng từ một. Hình này hiển thị giai đoạn cuối của quá trình dịch thuật nơi decoder chỉ phải tạo từ cuối cùng ("Beispiel"), cho trước văn bản đầu vào gốc ("This is an example") và câu đã dịch một phần ("Das ist ein"), để hoàn thành bản dịch.]

Các biến thể sau của kiến trúc transformer, chẳng hạn như BERT (viết tắt của bidirectional encoder representations from transformers - biểu diễn encoder hai chiều từ transformer) và các mô hình GPT khác nhau (viết tắt của generative pretrained transformers - transformer tiền huấn luyện tạo sinh), đã xây dựng dựa trên khái niệm này để thích ứng kiến trúc này cho các tác vụ khác nhau. Nếu quan tâm, hãy tham khảo phụ lục B để có thêm gợi ý đọc.

BERT, được xây dựng dựa trên module con encoder của transformer gốc, khác biệt trong phương pháp huấn luyện so với GPT. Trong khi GPT được thiết kế cho các tác vụ tạo sinh, BERT và các biến thể của nó chuyên về dự đoán từ bị che (masked word prediction), nơi mô hình dự đoán các từ bị che hoặc ẩn trong một câu cho trước, như hiển thị trong hình 1.5. Chiến lược huấn luyện độc đáo này trang bị cho BERT thế mạnh trong các tác vụ phân loại văn bản, bao gồm dự đoán cảm xúc và phân loại tài liệu. Như một ứng dụng của khả năng này, tại thời điểm viết, X (trước đây là Twitter) sử dụng BERT để phát hiện nội dung độc hại.

[Hình 1.5: Biểu diễn trực quan của các module con encoder và decoder của transformer. Bên trái, phân đoạn encoder minh họa các LLM giống BERT, tập trung vào dự đoán từ bị che và chủ yếu được sử dụng cho các tác vụ như phân loại văn bản. Bên phải, phân đoạn decoder giới thiệu các LLM giống GPT, được thiết kế cho các tác vụ tạo sinh và tạo ra chuỗi văn bản mạch lạc.]

GPT, mặt khác, tập trung vào phần decoder của kiến trúc transformer gốc và được thiết kế cho các tác vụ yêu cầu tạo văn bản. Điều này bao gồm dịch máy, tóm tắt văn bản, viết tiểu thuyết, viết code máy tính, và nhiều hơn nữa.

Các mô hình GPT, được thiết kế và huấn luyện chủ yếu để thực hiện các tác vụ hoàn thành văn bản, cũng cho thấy tính linh hoạt đáng chú ý trong khả năng của chúng. Các mô hình này giỏi trong việc thực hiện cả tác vụ học zero-shot và few-shot. Học zero-shot đề cập đến khả năng tổng quát hóa cho các tác vụ hoàn toàn chưa từng thấy mà không có bất kỳ ví dụ cụ thể nào trước đó. Mặt khác, học few-shot liên quan đến việc học từ số lượng tối thiểu các ví dụ mà người dùng cung cấp làm đầu vào, như hiển thị trong hình 1.6.

[Hình 1.6: Ngoài hoàn thành văn bản, các LLM giống GPT có thể giải quyết nhiều tác vụ khác nhau dựa trên đầu vào mà không cần huấn luyện lại, tinh chỉnh, hoặc thay đổi kiến trúc mô hình theo tác vụ cụ thể. Đôi khi việc cung cấp ví dụ về mục tiêu trong đầu vào rất hữu ích, được gọi là thiết lập few-shot. Tuy nhiên, các LLM giống GPT cũng có khả năng thực hiện các tác vụ mà không có ví dụ cụ thể, được gọi là thiết lập zero-shot.]

## 1.5 Sử dụng bộ dữ liệu lớn

Các bộ dữ liệu huấn luyện lớn cho các mô hình giống GPT và BERT phổ biến đại diện cho các tập văn bản đa dạng và toàn diện bao gồm hàng tỷ từ, gồm nhiều chủ đề và ngôn ngữ tự nhiên cũng như ngôn ngữ máy tính. Để cung cấp ví dụ cụ thể, bảng 1.1 tóm tắt bộ dữ liệu được sử dụng cho tiền huấn luyện GPT-3, đóng vai trò là mô hình cơ sở cho phiên bản đầu tiên của ChatGPT.

> **Transformer so với LLM**
>
> Các LLM ngày nay dựa trên kiến trúc transformer. Do đó, transformer và LLM là các thuật ngữ thường được sử dụng đồng nghĩa trong tài liệu. Tuy nhiên, lưu ý rằng không phải tất cả transformer đều là LLM vì transformer cũng có thể được sử dụng cho thị giác máy tính. Ngoài ra, không phải tất cả LLM đều là transformer, vì có các LLM dựa trên kiến trúc hồi quy và tích chập. Động lực chính đằng sau các phương pháp thay thế này là cải thiện hiệu quả tính toán của LLM. Liệu các kiến trúc LLM thay thế này có thể cạnh tranh với khả năng của LLM dựa trên transformer và liệu chúng có được áp dụng trong thực tế hay không vẫn còn phải chờ xem. Để đơn giản, tôi sử dụng thuật ngữ "LLM" để chỉ các LLM dựa trên transformer tương tự GPT. (Độc giả quan tâm có thể tìm tài liệu tham khảo mô tả các kiến trúc này trong phụ lục B.)

Bảng 1.1 báo cáo số lượng token, trong đó token là đơn vị văn bản mà mô hình đọc và số token trong bộ dữ liệu xấp xỉ tương đương với số từ và ký tự dấu câu trong văn bản. Chương 2 đề cập đến tokenization, quá trình chuyển đổi văn bản thành token.

Điểm chính cần rút ra là quy mô và sự đa dạng của bộ dữ liệu huấn luyện này cho phép các mô hình này hoạt động tốt trên các tác vụ đa dạng, bao gồm cú pháp ngôn ngữ, ngữ nghĩa, và ngữ cảnh — thậm chí một số yêu cầu kiến thức tổng quát.

Bản chất tiền huấn luyện của các mô hình này làm cho chúng cực kỳ linh hoạt cho tinh chỉnh thêm trên các tác vụ hạ nguồn (downstream tasks), đây là lý do tại sao chúng cũng được gọi là mô hình cơ sở hoặc mô hình nền tảng. Tiền huấn luyện LLM yêu cầu truy cập vào tài nguyên đáng kể và rất tốn kém. Ví dụ, chi phí tiền huấn luyện GPT-3 được ước tính là 4,6 triệu USD về tín dụng điện toán đám mây (https://mng.bz/VxEW).

**Bảng 1.1: Bộ dữ liệu tiền huấn luyện của LLM GPT-3 phổ biến**

| Tên bộ dữ liệu | Mô tả bộ dữ liệu | Số token | Tỷ trọng trong dữ liệu huấn luyện |
|---|---|---|---|
| CommonCrawl (đã lọc) | Dữ liệu thu thập web | 410 tỷ | 60% |
| WebText2 | Dữ liệu thu thập web | 19 tỷ | 22% |
| Books1 | Kho sách dựa trên internet | 12 tỷ | 8% |
| Books2 | Kho sách dựa trên internet | 55 tỷ | 8% |
| Wikipedia | Văn bản chất lượng cao | 3 tỷ | 3% |

> **Chi tiết bộ dữ liệu GPT-3**
>
> Bảng 1.1 hiển thị bộ dữ liệu được sử dụng cho GPT-3. Cột tỷ trọng trong bảng tổng cộng lên 100% dữ liệu được lấy mẫu, đã điều chỉnh cho sai số làm tròn. Mặc dù các tập con trong cột Số Token tổng cộng 499 tỷ, mô hình chỉ được huấn luyện trên 300 tỷ token. Các tác giả của bài báo GPT-3 không nêu rõ tại sao mô hình không được huấn luyện trên tất cả 499 tỷ token.
>
> Để có ngữ cảnh, hãy xem xét kích thước của bộ dữ liệu CommonCrawl, chỉ riêng nó đã bao gồm 410 tỷ token và yêu cầu khoảng 570 GB lưu trữ. Để so sánh, các lần lặp sau của mô hình như GPT-3, chẳng hạn như LLaMA của Meta, đã mở rộng phạm vi huấn luyện để bao gồm các nguồn dữ liệu bổ sung như bài báo nghiên cứu Arxiv (92 GB) và Q&A liên quan đến code của StackExchange (78 GB).
>
> Các tác giả của bài báo GPT-3 không chia sẻ bộ dữ liệu huấn luyện, nhưng một bộ dữ liệu có thể so sánh được và có sẵn công khai là Dolma: An Open Corpus of Three Trillion Tokens for LLM Pretraining Research của Soldaini et al. 2024 (https://arxiv.org/abs/2402.00159). Tuy nhiên, bộ sưu tập có thể chứa các tác phẩm có bản quyền, và các điều khoản sử dụng chính xác có thể phụ thuộc vào mục đích sử dụng và quốc gia.

Tin tốt là nhiều LLM tiền huấn luyện, có sẵn dưới dạng mô hình mã nguồn mở, có thể được sử dụng làm công cụ đa mục đích để viết, trích xuất và chỉnh sửa các văn bản không thuộc dữ liệu huấn luyện. Ngoài ra, LLM có thể được tinh chỉnh trên các tác vụ cụ thể với bộ dữ liệu tương đối nhỏ hơn, giảm tài nguyên tính toán cần thiết và cải thiện hiệu suất.

Chúng ta sẽ triển khai code cho tiền huấn luyện và sử dụng nó để tiền huấn luyện một LLM cho mục đích giáo dục. Tất cả phép tính đều có thể thực thi trên phần cứng tiêu dùng. Sau khi triển khai code tiền huấn luyện, chúng ta sẽ học cách tái sử dụng trọng số mô hình có sẵn công khai và tải chúng vào kiến trúc mà chúng ta sẽ triển khai, cho phép chúng ta bỏ qua giai đoạn tiền huấn luyện tốn kém khi tinh chỉnh LLM.

## 1.6 Nhìn kỹ hơn vào kiến trúc GPT

GPT ban đầu được giới thiệu trong bài báo "Improving Language Understanding by Generative Pre-Training" (https://mng.bz/x2qg) của Radford et al. từ OpenAI. GPT-3 là phiên bản mở rộng quy mô của mô hình này với nhiều tham số hơn và được huấn luyện trên bộ dữ liệu lớn hơn. Ngoài ra, mô hình gốc được cung cấp trong ChatGPT được tạo ra bằng cách tinh chỉnh GPT-3 trên bộ dữ liệu hướng dẫn lớn sử dụng phương pháp từ bài báo InstructGPT của OpenAI (https://arxiv.org/abs/2203.02155). Như hình 1.6 cho thấy, các mô hình này là các mô hình hoàn thành văn bản có năng lực và có thể thực hiện các tác vụ khác như sửa lỗi chính tả, phân loại, hoặc dịch ngôn ngữ. Điều này thực sự rất đáng chú ý vì các mô hình GPT được tiền huấn luyện trên tác vụ dự đoán từ tiếp theo tương đối đơn giản, như được mô tả trong hình 1.7.

Tác vụ dự đoán từ tiếp theo là một dạng học tự giám sát (self-supervised learning), là một dạng tự gắn nhãn (self-labeling). Điều này có nghĩa là chúng ta không cần thu thập nhãn cho dữ liệu huấn luyện một cách rõ ràng mà có thể sử dụng cấu trúc của chính dữ liệu: chúng ta có thể sử dụng từ tiếp theo trong câu hoặc tài liệu làm nhãn mà mô hình cần dự đoán. Vì tác vụ dự đoán từ tiếp theo này cho phép chúng ta tạo nhãn "nhanh chóng", nên có thể sử dụng các bộ dữ liệu văn bản chưa gán nhãn khổng lồ để huấn luyện LLM.

[Hình 1.7: Trong tác vụ tiền huấn luyện dự đoán từ tiếp theo cho các mô hình GPT, hệ thống học cách dự đoán từ sắp tới trong câu bằng cách nhìn vào các từ đã đến trước nó. Phương pháp này giúp mô hình hiểu cách các từ và cụm từ thường kết hợp với nhau trong ngôn ngữ, tạo nền tảng có thể được áp dụng cho nhiều tác vụ khác nhau.]

So với kiến trúc transformer gốc mà chúng ta đã đề cập trong phần 1.4, kiến trúc GPT tổng quát tương đối đơn giản. Về cơ bản, nó chỉ là phần decoder mà không có encoder (hình 1.8). Vì các mô hình kiểu decoder như GPT tạo văn bản bằng cách dự đoán văn bản từng từ một, chúng được coi là một loại mô hình tự hồi quy (autoregressive model). Mô hình tự hồi quy kết hợp đầu ra trước đó của chúng làm đầu vào cho các dự đoán trong tương lai. Do đó, trong GPT, mỗi từ mới được chọn dựa trên chuỗi đứng trước nó, cải thiện tính mạch lạc của văn bản kết quả.

[Hình 1.8: Kiến trúc GPT chỉ sử dụng phần decoder của transformer gốc. Nó được thiết kế cho xử lý một chiều, từ trái sang phải, làm cho nó phù hợp cho các tác vụ tạo văn bản và dự đoán từ tiếp theo để tạo văn bản theo cách lặp đi lặp lại, từng từ một.]

Các kiến trúc như GPT-3 cũng lớn hơn đáng kể so với mô hình transformer gốc. Ví dụ, transformer gốc lặp lại các khối encoder và decoder sáu lần. GPT-3 có 96 lớp transformer và 175 tỷ tham số tổng cộng.

GPT-3 được giới thiệu vào năm 2020, mà theo tiêu chuẩn của deep learning và phát triển mô hình ngôn ngữ lớn, được coi là khá lâu. Tuy nhiên, các kiến trúc gần đây hơn, chẳng hạn như các mô hình Llama của Meta, vẫn dựa trên cùng các khái niệm nền tảng, chỉ đưa ra các sửa đổi nhỏ. Do đó, việc hiểu GPT vẫn còn phù hợp hơn bao giờ hết, vì vậy tôi tập trung vào triển khai kiến trúc nổi bật đằng sau GPT trong khi cung cấp các chỉ dẫn đến các điều chỉnh cụ thể được sử dụng bởi các LLM thay thế.

Mặc dù mô hình transformer gốc, bao gồm các khối encoder và decoder, được thiết kế rõ ràng cho dịch ngôn ngữ, các mô hình GPT — bất chấp kiến trúc lớn hơn nhưng đơn giản hơn chỉ với decoder nhắm vào dự đoán từ tiếp theo — cũng có khả năng thực hiện các tác vụ dịch thuật. Khả năng này ban đầu gây bất ngờ cho các nhà nghiên cứu, vì nó xuất hiện từ một mô hình chủ yếu được huấn luyện trên tác vụ dự đoán từ tiếp theo, một tác vụ không nhắm cụ thể vào dịch thuật.

Khả năng thực hiện các tác vụ mà mô hình không được huấn luyện rõ ràng để thực hiện được gọi là hành vi nổi trội (emergent behavior). Khả năng này không được dạy rõ ràng trong quá trình huấn luyện mà xuất hiện như hệ quả tự nhiên của việc mô hình được tiếp xúc với lượng dữ liệu đa ngôn ngữ khổng lồ trong các ngữ cảnh đa dạng. Thực tế rằng các mô hình GPT có thể "học" các mẫu dịch thuật giữa các ngôn ngữ và thực hiện các tác vụ dịch thuật mặc dù chúng không được huấn luyện cụ thể cho điều đó chứng minh lợi ích và khả năng của các mô hình ngôn ngữ tạo sinh quy mô lớn này. Chúng ta có thể thực hiện các tác vụ đa dạng mà không cần sử dụng các mô hình đa dạng cho mỗi tác vụ.

## 1.7 Xây dựng một mô hình ngôn ngữ lớn

Bây giờ khi chúng ta đã đặt nền tảng cho việc hiểu LLM, hãy viết code một LLM từ đầu. Chúng ta sẽ lấy ý tưởng cơ bản đằng sau GPT làm bản thiết kế và giải quyết điều này trong ba giai đoạn, như được phác thảo trong hình 1.9.

[Hình 1.9: Ba giai đoạn chính của việc viết code một LLM là triển khai kiến trúc LLM và quy trình chuẩn bị dữ liệu (giai đoạn 1), tiền huấn luyện LLM để tạo mô hình nền tảng (giai đoạn 2), và tinh chỉnh mô hình nền tảng để trở thành trợ lý cá nhân hoặc bộ phân loại văn bản (giai đoạn 3).]

Trong giai đoạn 1, chúng ta sẽ tìm hiểu về các bước tiền xử lý dữ liệu cơ bản và viết code cơ chế attention ở trung tâm của mọi LLM. Tiếp theo, trong giai đoạn 2, chúng ta sẽ học cách viết code và tiền huấn luyện một LLM giống GPT có khả năng tạo văn bản mới. Chúng ta cũng sẽ xem qua các nguyên tắc cơ bản về đánh giá LLM, điều cần thiết cho việc phát triển các hệ thống NLP có năng lực.

Tiền huấn luyện một LLM từ đầu là một nỗ lực đáng kể, đòi hỏi hàng nghìn đến hàng triệu USD chi phí tính toán cho các mô hình giống GPT. Do đó, trọng tâm của giai đoạn 2 là triển khai huấn luyện cho mục đích giáo dục sử dụng bộ dữ liệu nhỏ. Ngoài ra, tôi cũng cung cấp ví dụ code để tải trọng số mô hình có sẵn công khai.

Cuối cùng, trong giai đoạn 3, chúng ta sẽ lấy một LLM tiền huấn luyện và tinh chỉnh nó để theo dõi hướng dẫn như trả lời truy vấn hoặc phân loại văn bản — các tác vụ phổ biến nhất trong nhiều ứng dụng thực tế và nghiên cứu.

Tôi hy vọng bạn mong chờ bắt đầu hành trình thú vị này!

## Tóm tắt

- LLM đã biến đổi lĩnh vực xử lý ngôn ngữ tự nhiên, trước đây chủ yếu dựa vào các hệ thống dựa trên quy tắc rõ ràng và các phương pháp thống kê đơn giản hơn. Sự ra đời của LLM giới thiệu các phương pháp tiếp cận mới dựa trên deep learning dẫn đến những tiến bộ trong việc hiểu, tạo ra và dịch ngôn ngữ con người.

- LLM hiện đại được huấn luyện theo hai bước chính:
  - Đầu tiên, chúng được tiền huấn luyện trên tập dữ liệu văn bản lớn chưa gán nhãn bằng cách sử dụng dự đoán từ tiếp theo trong câu làm nhãn.
  - Sau đó, chúng được tinh chỉnh trên bộ dữ liệu có nhãn, nhỏ hơn, cho tác vụ mục tiêu để theo dõi hướng dẫn hoặc thực hiện các tác vụ phân loại.

- LLM dựa trên kiến trúc transformer. Ý tưởng chính của kiến trúc transformer là cơ chế attention cho phép LLM truy cập có chọn lọc vào toàn bộ chuỗi đầu vào khi tạo đầu ra từng từ một.

- Kiến trúc transformer gốc bao gồm encoder để phân tích văn bản và decoder để tạo văn bản.

- LLM cho tạo văn bản và theo dõi hướng dẫn, chẳng hạn như GPT-3 và ChatGPT, chỉ triển khai module decoder, đơn giản hóa kiến trúc.

- Bộ dữ liệu lớn bao gồm hàng tỷ từ là cần thiết cho tiền huấn luyện LLM.

- Mặc dù tác vụ tiền huấn luyện tổng quát cho mô hình giống GPT là dự đoán từ tiếp theo trong câu, các LLM này thể hiện các thuộc tính nổi trội (emergent properties), chẳng hạn như khả năng phân loại, dịch thuật, hoặc tóm tắt văn bản.

- Sau khi LLM được tiền huấn luyện, mô hình nền tảng thu được có thể được tinh chỉnh hiệu quả hơn cho các tác vụ hạ nguồn khác nhau.

- LLM được tinh chỉnh trên bộ dữ liệu tùy chỉnh có thể vượt trội hơn LLM tổng quát trên các tác vụ cụ thể.
