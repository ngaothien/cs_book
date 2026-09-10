# Xây dựng Mô hình Ngôn ngữ Lớn (Từ Đầu)

**MANNING**

**Sebastian Raschka**

---

[Hình bìa: Ba giai đoạn chính của việc viết code một mô hình ngôn ngữ lớn (LLM) là triển khai kiến trúc LLM và quy trình chuẩn bị dữ liệu (giai đoạn 1), tiền huấn luyện LLM để tạo mô hình nền tảng (giai đoạn 2), và tinh chỉnh mô hình nền tảng để trở thành trợ lý cá nhân hoặc bộ phân loại văn bản (giai đoạn 3). Mỗi giai đoạn này được khám phá và triển khai trong cuốn sách này.]

---

## Thông tin xuất bản

Để biết thông tin trực tuyến và đặt mua cuốn sách này cũng như các sách Manning khác, vui lòng truy cập www.manning.com. Nhà xuất bản cung cấp giảm giá cho cuốn sách này khi đặt hàng số lượng lớn. Để biết thêm thông tin, vui lòng liên hệ

Phòng Bán hàng Đặc biệt
Manning Publications Co.
20 Baldwin Road
PO Box 761
Shelter Island, NY 11964
Email: orders@manning.com

©2025 Manning Publications Co. Bảo lưu mọi quyền.

Không phần nào của ấn phẩm này được sao chép, lưu trữ trong hệ thống truy xuất, hoặc truyền tải, dưới bất kỳ hình thức hay phương tiện nào — điện tử, cơ học, sao chụp, hoặc cách khác — mà không có sự cho phép bằng văn bản trước đó của nhà xuất bản.

Nhiều ký hiệu được các nhà sản xuất và người bán sử dụng để phân biệt sản phẩm của họ được tuyên bố là nhãn hiệu thương mại. Khi những ký hiệu đó xuất hiện trong sách, và Manning Publications biết về yêu cầu nhãn hiệu thương mại, các ký hiệu đã được in với chữ cái đầu viết hoa hoặc tất cả viết hoa.

Nhận thức được tầm quan trọng của việc bảo tồn những gì đã được viết, chính sách của Manning là in các sách chúng tôi xuất bản trên giấy không chứa axit, và chúng tôi nỗ lực hết sức cho mục tiêu đó. Đồng thời nhận thức trách nhiệm bảo tồn tài nguyên hành tinh, sách Manning được in trên giấy có ít nhất 15 phần trăm tái chế và được xử lý không sử dụng clo nguyên tố.

Các tác giả và nhà xuất bản đã nỗ lực hết sức để đảm bảo thông tin trong cuốn sách này là chính xác tại thời điểm in. Các tác giả và nhà xuất bản không chịu trách nhiệm và từ chối mọi trách nhiệm pháp lý đối với bất kỳ bên nào về bất kỳ tổn thất, thiệt hại, hoặc gián đoạn nào do lỗi hoặc thiếu sót gây ra, dù các lỗi hoặc thiếu sót đó là kết quả của sự bất cẩn, tai nạn, hoặc bất kỳ nguyên nhân nào khác, hoặc từ bất kỳ việc sử dụng thông tin nào trong đây.

Manning Publications Co. | 20 Baldwin Road | PO Box 761 | Shelter Island, NY 11964

- Biên tập phát triển: Dustin Archibald
- Biên tập kỹ thuật: David Caswell
- Biên tập đánh giá: Kishor Rit
- Biên tập sản xuất: Aleksandar Dragosavljević
- Biên tập bản sao: Kari Lucke và Alisa Larson
- Người hiệu đính: Mike Beady
- Hiệu đính kỹ thuật: Jerry Kuch
- Người sắp chữ: Dennis Dalinnik
- Thiết kế bìa: Marija Tudor

ISBN: 9781633437166
In tại Hoa Kỳ

---

## Mục lục tóm tắt

1. Hiểu về mô hình ngôn ngữ lớn — trang 1
2. Làm việc với dữ liệu văn bản — trang 17
3. Lập trình cơ chế attention — trang 50
4. Triển khai mô hình GPT từ đầu để tạo văn bản — trang 92
5. Tiền huấn luyện trên dữ liệu chưa gán nhãn — trang 128
6. Tinh chỉnh cho phân loại — trang 169
7. Tinh chỉnh để theo dõi hướng dẫn — trang 204
A. Giới thiệu PyTorch — trang 251
B. Tài liệu tham khảo và đọc thêm — trang 289
C. Lời giải bài tập — trang 300
D. Thêm các tính năng nâng cao vào vòng lặp huấn luyện — trang 313
E. Tinh chỉnh hiệu quả tham số với LoRA — trang 322

---

## Mục lục chi tiết

- Lời nói đầu — xi
- Lời cảm ơn — xiii
- Về cuốn sách này — xv
- Về tác giả — xix
- Về hình bìa — xx

**1 Hiểu về mô hình ngôn ngữ lớn — 1**
- 1.1 LLM là gì? — 2
- 1.2 Ứng dụng của LLM — 4
- 1.3 Các giai đoạn xây dựng và sử dụng LLM — 5
- 1.4 Giới thiệu kiến trúc transformer — 7
- 1.5 Sử dụng bộ dữ liệu lớn — 10
- 1.6 Nhìn kỹ hơn vào kiến trúc GPT — 12
- 1.7 Xây dựng một mô hình ngôn ngữ lớn — 14

**2 Làm việc với dữ liệu văn bản — 17**
- 2.1 Hiểu về word embedding — 18
- 2.2 Tokenization — Phân tách văn bản — 21
- 2.3 Chuyển đổi token thành token ID — 24
- 2.4 Thêm token ngữ cảnh đặc biệt — 29
- 2.5 Mã hóa cặp byte (Byte pair encoding) — 33
- 2.6 Lấy mẫu dữ liệu với cửa sổ trượt — 35
- 2.7 Tạo token embedding — 41
- 2.8 Mã hóa vị trí từ — 43

**3 Lập trình cơ chế attention — 50**
- 3.1 Vấn đề với mô hình hóa chuỗi dài — 52
- 3.2 Nắm bắt phụ thuộc dữ liệu bằng cơ chế attention — 54
- 3.3 Chú ý đến các phần khác nhau của đầu vào bằng self-attention — 55
  - Cơ chế self-attention đơn giản không có trọng số huấn luyện — 56
  - Tính trọng số attention cho tất cả token đầu vào — 61
- 3.4 Triển khai self-attention với trọng số huấn luyện — 64
  - Tính trọng số attention từng bước — 65
  - Triển khai lớp self-attention Python gọn — 70
- 3.5 Ẩn các từ tương lai bằng causal attention — 74
  - Áp dụng mặt nạ causal attention — 75
  - Che thêm trọng số attention bằng dropout — 78
  - Triển khai lớp causal attention gọn — 80
- 3.6 Mở rộng single-head attention sang multi-head attention — 82
  - Xếp chồng nhiều lớp single-head attention — 82
  - Triển khai multi-head attention với phân chia trọng số — 86

**4 Triển khai mô hình GPT từ đầu để tạo văn bản — 92**
- 4.1 Viết code kiến trúc LLM — 93
- 4.2 Chuẩn hóa kích hoạt bằng layer normalization — 99
- 4.3 Triển khai mạng feed forward với kích hoạt GELU — 105
- 4.4 Thêm kết nối tắt (shortcut connections) — 109
- 4.5 Kết nối các lớp attention và linear trong khối transformer — 113
- 4.6 Viết code mô hình GPT — 117
- 4.7 Tạo văn bản — 122

**5 Tiền huấn luyện trên dữ liệu chưa gán nhãn — 128**
- 5.1 Đánh giá mô hình tạo văn bản — 129
  - Sử dụng GPT để tạo văn bản — 130
  - Tính toán loss tạo văn bản — 132
  - Tính toán loss tập huấn luyện và tập kiểm tra — 140
- 5.2 Huấn luyện một LLM — 146
- 5.3 Chiến lược giải mã để kiểm soát tính ngẫu nhiên — 151
  - Chia tỷ lệ nhiệt độ (Temperature scaling) — 152
  - Lấy mẫu top-k — 155
  - Sửa đổi hàm tạo văn bản — 157
- 5.4 Tải và lưu trọng số mô hình trong PyTorch — 159
- 5.5 Tải trọng số tiền huấn luyện từ OpenAI — 160

**6 Tinh chỉnh cho phân loại — 169**
- 6.1 Các loại tinh chỉnh khác nhau — 170
- 6.2 Chuẩn bị bộ dữ liệu — 172
- 6.3 Tạo data loader — 175
- 6.4 Khởi tạo mô hình với trọng số tiền huấn luyện — 181
- 6.5 Thêm classification head — 183
- 6.6 Tính toán loss phân loại và độ chính xác — 190
- 6.7 Tinh chỉnh mô hình trên dữ liệu có giám sát — 195
- 6.8 Sử dụng LLM làm bộ phân loại spam — 200

**7 Tinh chỉnh để theo dõi hướng dẫn — 204**
- 7.1 Giới thiệu về instruction fine-tuning — 205
- 7.2 Chuẩn bị bộ dữ liệu cho supervised instruction fine-tuning — 207
- 7.3 Tổ chức dữ liệu thành batch huấn luyện — 211
- 7.4 Tạo data loader cho bộ dữ liệu hướng dẫn — 223
- 7.5 Tải LLM tiền huấn luyện — 226
- 7.6 Tinh chỉnh LLM trên dữ liệu hướng dẫn — 229
- 7.7 Trích xuất và lưu phản hồi — 233
- 7.8 Đánh giá LLM đã tinh chỉnh — 238
- 7.9 Kết luận — 247
  - Tiếp theo là gì? — 247
  - Cập nhật trong lĩnh vực phát triển nhanh — 248
  - Lời cuối — 248

---

## Lời nói đầu

Mô hình ngôn ngữ lớn (Large Language Model - LLM) đã cách mạng hóa lĩnh vực xử lý ngôn ngữ tự nhiên (Natural Language Processing - NLP) và mang trí tuệ nhân tạo (AI) đến gần hơn với khả năng hiểu và tạo ra ngôn ngữ giống con người. Bằng cách xây dựng một LLM từ đầu, cuốn sách này cho phép bạn hiểu sâu cách thức hoạt động của LLM ở cấp nền tảng. Kiến thức nền tảng này sẽ giúp bạn tự tin hơn khi làm việc với các framework và công cụ LLM hiện có, cũng như khi tinh chỉnh hoặc phát triển LLM cho nhu cầu riêng của bạn.

Trong cuốn sách này, chúng ta sẽ từng bước xây dựng một LLM, bao gồm lập trình kiến trúc nền tảng, tiền huấn luyện trên dữ liệu văn bản, và tinh chỉnh mô hình để theo dõi hướng dẫn cũng như phân loại văn bản. Phương pháp thực hành này đảm bảo rằng bạn không chỉ hiểu lý thuyết mà còn có kinh nghiệm thực tế trong việc tạo ra các mô hình ngôn ngữ mạnh mẽ.

Mặc dù các mô hình bạn sẽ tạo ra có quy mô nhỏ hơn so với các mô hình nền tảng lớn, chúng sử dụng cùng các khái niệm và đóng vai trò là công cụ giáo dục mạnh mẽ để nắm bắt các cơ chế và kỹ thuật cốt lõi được sử dụng trong việc xây dựng các LLM tiên tiến nhất.

Bạn có thể nghĩ về LLM như một loại AI mới hơn — nhưng trên thực tế, chúng chỉ là các mô hình deep learning cực kỳ lớn (ví dụ, GPT-3 có hơn 175 tỷ tham số — đó là 175.000.000.000 tham số. Để so sánh, trong machine learning truyền thống hoặc phương pháp thống kê, bộ dữ liệu hoa Iris có thể được phân loại với hơn 90% độ chính xác bằng một mô hình nhỏ chỉ với hai tham số.) Tuy nhiên, bất chấp kích thước lớn của LLM so với các phương pháp truyền thống hơn, LLM không nhất thiết phải là hộp đen.

Trong cuốn sách này, bạn sẽ học cách xây dựng một LLM từng bước một. Đến cuối, bạn sẽ có hiểu biết vững chắc về cách một LLM, giống như các LLM được sử dụng trong ChatGPT, hoạt động ở cấp nền tảng. Tôi tin rằng việc phát triển sự tự tin với từng phần của các khái niệm nền tảng và code cơ bản là cực kỳ quan trọng cho thành công. Điều này không chỉ giúp sửa lỗi và cải thiện hiệu suất mà còn cho phép thử nghiệm với các ý tưởng mới.

Một vài năm trước, khi tôi bắt đầu làm việc với LLM, tôi phải học cách triển khai chúng theo cách khó khăn, sàng lọc qua nhiều bài báo nghiên cứu và các kho code không hoàn chỉnh để phát triển hiểu biết tổng quát. Với cuốn sách này, tôi hy vọng làm cho LLM dễ tiếp cận hơn bằng cách phát triển và chia sẻ hướng dẫn triển khai từng bước, trình bày chi tiết tất cả các thành phần chính và giai đoạn phát triển của một LLM.

Tôi tin tưởng mạnh mẽ rằng cách tốt nhất để hiểu LLM là viết code một LLM từ đầu — và bạn sẽ thấy rằng điều này cũng có thể rất thú vị!

Chúc bạn đọc và viết code vui vẻ!

---

## Lời cảm ơn

Viết một cuốn sách là một công việc đáng kể, và tôi muốn bày tỏ lòng biết ơn chân thành đến vợ tôi, Liza, vì sự kiên nhẫn và ủng hộ của cô ấy trong suốt quá trình này. Tình yêu vô điều kiện và sự khuyến khích liên tục của cô ấy là hoàn toàn cần thiết.

Tôi vô cùng biết ơn Daniel Kleine, người mà phản hồi vô giá của anh ấy về các chương đang viết và code đã vượt xa mong đợi. Với con mắt tinh tường về chi tiết và những gợi ý sâu sắc, những đóng góp của Daniel chắc chắn đã làm cho cuốn sách này trở thành trải nghiệm đọc mượt mà và thú vị hơn.

Tôi cũng muốn cảm ơn đội ngũ tuyệt vời tại Manning Publications, bao gồm Michael Stephens, vì nhiều cuộc thảo luận hiệu quả đã giúp định hình hướng đi của cuốn sách này, và Dustin Archibald, người mà phản hồi mang tính xây dựng và hướng dẫn tuân thủ các quy chuẩn Manning đã rất quan trọng. Tôi cũng đánh giá cao sự linh hoạt của các bạn trong việc đáp ứng các yêu cầu đặc biệt của phương pháp xây dựng từ đầu không theo quy ước này. Lời cảm ơn đặc biệt gửi đến Aleksandar Dragosavljević, Kari Lucke, và Mike Beady vì công việc của họ trên các bố cục chuyên nghiệp và đến Susan Honeywell cùng đội ngũ của cô ấy vì đã tinh chỉnh và hoàn thiện đồ họa.

Tôi muốn bày tỏ lòng biết ơn sâu sắc đến Robin Campbell và đội ngũ marketing xuất sắc của cô ấy vì sự hỗ trợ vô giá trong suốt quá trình viết.

Cuối cùng, tôi gửi lời cảm ơn đến các reviewer: Anandaganesh Balakrishnan, Anto Aravinth, Ayush Bihani, Bassam Ismail, Benjamin Muskalla, Bruno Sonnino, Christian Prokopp, Daniel Kleine, David Curran, Dibyendu Roy Chowdhury, Gary Pass, Georg Sommer, Giovanni Alzetta, Guillermo Alcántara, Jonathan Reeves, Kunal Ghosh, Nicolas Modrzyk, Paul Silisteanu, Raul Ciotescu, Scott Ling, Sriram Macharla, Sumit Pal, Vahid Mirjalili, Vaijanath Rao, và Walter Reade vì phản hồi kỹ lưỡng của họ về các bản nháp. Con mắt tinh tường và bình luận sâu sắc của các bạn đã rất cần thiết trong việc cải thiện chất lượng cuốn sách này.

Gửi đến tất cả mọi người đã đóng góp vào hành trình này, tôi chân thành biết ơn. Sự hỗ trợ, chuyên môn, và sự tận tâm của các bạn đã đóng vai trò then chốt trong việc đưa cuốn sách này đến thành quả. Cảm ơn các bạn!

---

## Về cuốn sách này

*Xây dựng Mô hình Ngôn ngữ Lớn (Từ Đầu)* được viết để giúp bạn hiểu và tạo ra các mô hình ngôn ngữ lớn (LLM) giống GPT của riêng bạn từ nền tảng. Cuốn sách bắt đầu bằng việc tập trung vào các kiến thức cơ bản về làm việc với dữ liệu văn bản và viết code cơ chế attention, sau đó hướng dẫn bạn triển khai một mô hình GPT hoàn chỉnh từ đầu. Cuốn sách sau đó bao gồm cơ chế tiền huấn luyện cũng như tinh chỉnh cho các tác vụ cụ thể như phân loại văn bản và theo dõi hướng dẫn. Đến cuối cuốn sách này, bạn sẽ có hiểu biết sâu về cách LLM hoạt động và kỹ năng để xây dựng mô hình của riêng bạn. Mặc dù các mô hình bạn sẽ tạo ra có quy mô nhỏ hơn so với các mô hình nền tảng lớn, chúng sử dụng cùng các khái niệm và đóng vai trò là công cụ giáo dục mạnh mẽ để nắm bắt các cơ chế và kỹ thuật cốt lõi được sử dụng trong việc xây dựng các LLM tiên tiến nhất.

### Ai nên đọc cuốn sách này

*Xây dựng Mô hình Ngôn ngữ Lớn (Từ Đầu)* dành cho những người đam mê machine learning, kỹ sư, nhà nghiên cứu, sinh viên, và những người thực hành muốn có hiểu biết sâu về cách LLM hoạt động và học cách xây dựng mô hình của riêng mình từ đầu. Cả người mới bắt đầu và nhà phát triển có kinh nghiệm đều có thể sử dụng các kỹ năng và kiến thức hiện có của mình để nắm bắt các khái niệm và kỹ thuật được sử dụng trong việc tạo ra LLM.

Điều làm cuốn sách này khác biệt là phạm vi bao quát toàn diện về toàn bộ quy trình xây dựng LLM, từ làm việc với bộ dữ liệu đến triển khai kiến trúc mô hình, tiền huấn luyện trên dữ liệu chưa gán nhãn, và tinh chỉnh cho các tác vụ cụ thể. Tại thời điểm viết, không có tài nguyên nào khác cung cấp phương pháp tiếp cận hoàn chỉnh và thực hành như vậy để xây dựng LLM từ nền tảng.

Để hiểu các ví dụ code trong cuốn sách này, bạn nên có nắm vững lập trình Python. Mặc dù có một số quen thuộc với machine learning, deep learning, và trí tuệ nhân tạo có thể có lợi, nhưng không cần có nền tảng sâu rộng trong các lĩnh vực này. LLM là một tập con độc đáo của AI, vì vậy ngay cả khi bạn tương đối mới trong lĩnh vực này, bạn vẫn có thể theo dõi được.

Nếu bạn có một số kinh nghiệm với mạng nơ-ron sâu, bạn có thể thấy một số khái niệm quen thuộc hơn, vì LLM được xây dựng dựa trên các kiến trúc này. Tuy nhiên, thành thạo PyTorch không phải là điều kiện tiên quyết. Phụ lục A cung cấp giới thiệu ngắn gọn về PyTorch, trang bị cho bạn các kỹ năng cần thiết để hiểu các ví dụ code trong suốt cuốn sách.

Hiểu biết toán học ở cấp trung học, đặc biệt là làm việc với vector và ma trận, có thể hữu ích khi chúng ta khám phá cách hoạt động bên trong của LLM. Tuy nhiên, kiến thức toán học nâng cao không cần thiết để nắm bắt các khái niệm và ý tưởng chính được trình bày trong cuốn sách này.

Điều kiện tiên quyết quan trọng nhất là nền tảng vững chắc về lập trình Python. Với kiến thức này, bạn sẽ sẵn sàng khám phá thế giới hấp dẫn của LLM và hiểu các khái niệm cũng như ví dụ code được trình bày trong cuốn sách này.

### Cuốn sách được tổ chức như thế nào: Lộ trình

Cuốn sách được thiết kế để đọc tuần tự, vì mỗi chương xây dựng dựa trên các khái niệm và kỹ thuật được giới thiệu ở các chương trước. Cuốn sách được chia thành bảy chương bao gồm các khía cạnh thiết yếu của LLM và cách triển khai chúng.

Chương 1 cung cấp giới thiệu tổng quan về các khái niệm cơ bản đằng sau LLM. Nó khám phá kiến trúc transformer, nền tảng cho các LLM như những mô hình được sử dụng trên nền tảng ChatGPT.

Chương 2 trình bày kế hoạch xây dựng LLM từ đầu. Nó bao gồm quá trình chuẩn bị văn bản cho huấn luyện LLM, bao gồm chia văn bản thành token từ và token con từ, sử dụng mã hóa cặp byte cho tokenization nâng cao, lấy mẫu ví dụ huấn luyện với phương pháp cửa sổ trượt, và chuyển đổi token thành vector đầu vào cho LLM.

Chương 3 tập trung vào cơ chế attention được sử dụng trong LLM. Nó giới thiệu framework self-attention cơ bản và tiến tới cơ chế self-attention nâng cao. Chương cũng bao gồm triển khai module causal attention cho phép LLM tạo text từng token một, che (masking) ngẫu nhiên các trọng số attention được chọn với dropout để giảm overfitting và xếp chồng nhiều module causal attention thành module multi-head attention.

Chương 4 tập trung vào viết code mô hình LLM giống GPT có thể được huấn luyện để tạo văn bản giống con người. Nó bao gồm các kỹ thuật như chuẩn hóa kích hoạt lớp (layer normalization) để ổn định quá trình huấn luyện mạng nơ-ron, thêm kết nối tắt (shortcut connections) trong mạng nơ-ron sâu để huấn luyện mô hình hiệu quả hơn, triển khai các khối transformer để tạo mô hình GPT có kích thước khác nhau, và tính toán số tham số cũng như yêu cầu lưu trữ của mô hình GPT.

Chương 5 triển khai quá trình tiền huấn luyện LLM. Nó bao gồm tính toán loss trên tập huấn luyện và tập kiểm tra (validation set) để đánh giá chất lượng văn bản do LLM tạo ra, triển khai hàm huấn luyện và tiền huấn luyện LLM, lưu và tải trọng số mô hình để tiếp tục huấn luyện LLM, và tải trọng số tiền huấn luyện từ OpenAI.

Chương 6 giới thiệu các phương pháp tinh chỉnh LLM khác nhau. Nó bao gồm chuẩn bị bộ dữ liệu cho phân loại văn bản, sửa đổi LLM tiền huấn luyện cho tinh chỉnh, tinh chỉnh LLM để nhận diện tin nhắn spam, và đánh giá độ chính xác của bộ phân loại LLM đã tinh chỉnh.

Chương 7 khám phá quá trình tinh chỉnh theo hướng dẫn (instruction fine-tuning) của LLM. Nó bao gồm chuẩn bị bộ dữ liệu cho tinh chỉnh theo hướng dẫn có giám sát, tổ chức dữ liệu hướng dẫn trong các batch huấn luyện, tải LLM tiền huấn luyện và tinh chỉnh nó để theo dõi hướng dẫn của con người, trích xuất phản hồi hướng dẫn do LLM tạo ra để đánh giá, và đánh giá LLM đã tinh chỉnh theo hướng dẫn.

### Về code

Để giúp bạn dễ dàng theo dõi nhất có thể, tất cả ví dụ code trong cuốn sách này đều có sẵn trên trang web Manning tại https://www.manning.com/books/build-a-large-language-model-from-scratch, cũng như ở định dạng Jupyter notebook trên GitHub tại https://github.com/rasbt/LLMs-from-scratch. Và đừng lo lắng nếu bạn gặp khó khăn — lời giải cho tất cả bài tập code có thể được tìm thấy trong phụ lục C.

Cuốn sách này chứa nhiều ví dụ mã nguồn cả trong các listing được đánh số và trong dòng với văn bản bình thường. Trong cả hai trường hợp, mã nguồn được định dạng bằng phông chữ có chiều rộng cố định `như thế này` để phân biệt với văn bản thông thường.

Trong nhiều trường hợp, mã nguồn gốc đã được định dạng lại; chúng tôi đã thêm ngắt dòng và chỉnh lại thụt lề để phù hợp với không gian trang có sẵn trong sách. Trong các trường hợp hiếm, ngay cả điều này cũng không đủ, và các listing bao gồm dấu tiếp tục dòng (➥). Ngoài ra, các comment trong mã nguồn thường đã được loại bỏ khỏi các listing khi code được mô tả trong văn bản. Chú thích code đi kèm nhiều listing, làm nổi bật các khái niệm quan trọng.

Một trong những mục tiêu chính của cuốn sách này là khả năng tiếp cận, vì vậy các ví dụ code đã được thiết kế cẩn thận để chạy hiệu quả trên máy tính xách tay thông thường, không cần phần cứng đặc biệt nào. Nhưng nếu bạn có quyền truy cập GPU, một số phần cung cấp mẹo hữu ích về việc mở rộng bộ dữ liệu và mô hình để tận dụng sức mạnh bổ sung đó.

Trong suốt cuốn sách, chúng ta sẽ sử dụng PyTorch làm thư viện tensor và deep learning chính để triển khai LLM từ nền tảng. Nếu PyTorch là mới với bạn, tôi khuyên bạn nên bắt đầu với phụ lục A, cung cấp giới thiệu chuyên sâu, kèm theo các khuyến nghị cài đặt.

### Diễn đàn thảo luận liveBook

Việc mua cuốn sách *Xây dựng Mô hình Ngôn ngữ Lớn (Từ Đầu)* bao gồm quyền truy cập miễn phí vào liveBook, nền tảng đọc trực tuyến của Manning. Sử dụng các tính năng thảo luận độc quyền của liveBook, bạn có thể đính kèm bình luận vào cuốn sách một cách tổng thể hoặc vào các phần hoặc đoạn cụ thể. Rất dễ dàng để ghi chú cho bản thân, hỏi và trả lời các câu hỏi kỹ thuật, và nhận trợ giúp từ tác giả cùng người dùng khác. Để truy cập diễn đàn, hãy truy cập https://livebook.manning.com/book/build-a-large-language-model-from-scratch/discussion. Bạn cũng có thể tìm hiểu thêm về diễn đàn Manning và quy tắc ứng xử tại https://livebook.manning.com/discussion.

Cam kết của Manning với độc giả là cung cấp một nơi mà cuộc đối thoại có ý nghĩa giữa các độc giả cá nhân và giữa độc giả với tác giả có thể diễn ra. Đây không phải là cam kết về bất kỳ lượng tham gia cụ thể nào từ phía tác giả, người mà đóng góp cho diễn đàn vẫn là tự nguyện (và không được trả thù lao). Chúng tôi gợi ý bạn hãy thử đặt cho tác giả một số câu hỏi thách thức kẻo sự quan tâm của ông ấy lạc hướng! Diễn đàn và kho lưu trữ các cuộc thảo luận trước đó sẽ có thể truy cập được từ trang web của nhà xuất bản miễn là cuốn sách vẫn còn in.

### Tài nguyên trực tuyến khác

Quan tâm đến xu hướng nghiên cứu AI và LLM mới nhất?
Hãy xem blog của tôi tại https://magazine.sebastianraschka.com, nơi tôi thường xuyên thảo luận về nghiên cứu AI mới nhất với trọng tâm là LLM.

Cần trợ giúp để bắt kịp tốc độ với deep learning và PyTorch?
Tôi cung cấp một số khóa học miễn phí trên trang web của mình tại https://sebastianraschka.com/teaching. Các tài nguyên này có thể giúp bạn nhanh chóng bắt kịp các kỹ thuật mới nhất.

Tìm kiếm tài liệu bổ sung liên quan đến cuốn sách?
Truy cập kho GitHub của cuốn sách tại https://github.com/rasbt/LLMs-from-scratch để tìm các tài nguyên và ví dụ bổ sung để hỗ trợ việc học tập của bạn.

---

## Về tác giả

SEBASTIAN RASCHKA, Tiến sĩ, đã làm việc trong lĩnh vực machine learning và AI hơn một thập kỷ. Ngoài vai trò nhà nghiên cứu, Sebastian có niềm đam mê mạnh mẽ với giáo dục. Ông được biết đến với các cuốn sách bán chạy nhất về machine learning với Python và những đóng góp cho mã nguồn mở.

Sebastian là kỹ sư nghiên cứu cấp cao (staff research engineer) tại Lightning AI, tập trung vào triển khai và đào tạo LLM. Trước kinh nghiệm trong ngành, Sebastian là phó giáo sư tại Khoa Thống kê, Đại học Wisconsin-Madison, nơi ông tập trung nghiên cứu deep learning. Bạn có thể tìm hiểu thêm về Sebastian tại https://sebastianraschka.com.

---

## Về hình bìa

Hình trên bìa cuốn *Xây dựng Mô hình Ngôn ngữ Lớn (Từ Đầu)*, có tiêu đề "Le duchesse" hay "Nữ công tước", được lấy từ một cuốn sách của Louis Curmer xuất bản năm 1841. Mỗi hình minh họa đều được vẽ tinh xảo và tô màu bằng tay.

Vào thời đó, dễ dàng nhận biết nơi sinh sống và nghề nghiệp hay địa vị xã hội của mọi người chỉ bằng trang phục của họ. Manning tôn vinh sự sáng tạo và tinh thần tiên phong của ngành công nghiệp máy tính bằng bìa sách dựa trên sự đa dạng phong phú của văn hóa vùng miền hàng thế kỷ trước, được hồi sinh bằng những bức tranh từ các bộ sưu tập như thế này.
