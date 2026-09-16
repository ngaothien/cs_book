# Bảng thuật ngữ (Glossary)

Bảng thuật ngữ này tổng hợp các khái niệm Khoa học Máy tính, Trí tuệ Nhân tạo (AI), Học máy (Machine Learning), và Học sâu (Deep Learning) được sử dụng trong cuốn sách, kèm theo bản dịch tiếng Việt tương ứng nhằm đảm bảo tính nhất quán.

| Thuật ngữ tiếng Anh | Thuật ngữ tiếng Việt | Giải thích ngắn gọn |
| :--- | :--- | :--- |
| **Artificial Intelligence (AI)** | Trí tuệ nhân tạo | Ngành khoa học máy tính nhằm tạo ra máy móc có khả năng bắt chước trí thông minh con người. |
| **Attention Mechanism** | Cơ chế chú ý | Cơ chế cho phép mạng nơ-ron tập trung vào các phần quan trọng của dữ liệu đầu vào. |
| **Autograd** | Cơ chế tự động tính đạo hàm (Autograd) | Hệ thống cốt lõi của PyTorch tự động tính toán đạo hàm (gradient) cho các mạng nơ-ron thông qua đồ thị tính toán. |
| **Backpropagation** | Lan truyền ngược | Thuật toán dùng để huấn luyện mạng nơ-ron bằng cách truyền ngược sai số từ đầu ra về đầu vào nhằm điều chỉnh trọng số. |
| **Batch** | Lô dữ liệu / Batch | Một tập hợp con của dữ liệu huấn luyện được xử lý đồng thời trong một bước lặp (iteration). |
| **Batch Normalization** | Chuẩn hóa theo lô | Kỹ thuật chuẩn hóa đầu vào của từng lớp mạng nhằm tăng tốc độ huấn luyện và ổn định mô hình. |
| **Chain Rule** | Quy tắc chuỗi (Đạo hàm hàm hợp) | Quy tắc tính đạo hàm của hàm hợp trong giải tích, nền tảng toán học cốt lõi của thuật toán backpropagation. |
| **Class Label** | Nhãn phân lớp | Thẻ phân loại hoặc danh mục gán cho một dữ liệu đầu vào trong học có giám sát. |
| **Computation Graph** | Đồ thị tính toán | Một đồ thị có hướng thể hiện chuỗi các phép toán toán học trong mô hình mạng nơ-ron. |
| **Data Loader** | Bộ tải dữ liệu (DataLoader) | Công cụ nạp, xáo trộn và đóng gói dữ liệu thành các lô (batch) để huấn luyện mô hình hiệu quả. |
| **Dataset** | Tập dữ liệu | Một tập hợp các dữ liệu dùng để huấn luyện, kiểm thử hoặc xác thực mô hình. |
| **Deep Learning** | Học sâu | Một nhánh của Machine Learning chuyên sử dụng các mạng nơ-ron sâu (nhiều lớp ẩn). |
| **Deep Neural Network** | Mạng nơ-ron sâu | Mạng nơ-ron nhân tạo có nhiều lớp ẩn ở giữa lớp đầu vào và lớp đầu ra. |
| **Dropout** | Dropout (Kỹ thuật ngắt kết nối ngẫu nhiên) | Kỹ thuật chuẩn hóa vô hiệu hóa ngẫu nhiên một tỷ lệ nơ-ron trong quá trình huấn luyện để chống quá khớp (overfitting). |
| **Epoch** | Epoch (Chu kỳ huấn luyện) | Một chu kỳ huấn luyện khi toàn bộ tập dữ liệu huấn luyện đã được đưa qua mô hình mạng nơ-ron một lần. |
| **Finetuning** | Tinh chỉnh (Fine-tuning) | Quá trình huấn luyện tiếp một mô hình đã được tiền huấn luyện trên một tập dữ liệu cụ thể để tối ưu cho một tác vụ mục tiêu. |
| **Forward Pass** | Lan truyền tiến / Lan truyền xuôi | Quá trình tính toán kết quả đầu ra của mô hình bằng cách truyền dữ liệu từ lớp đầu vào qua các lớp ẩn đến lớp đầu ra. |
| **Fully Connected Layer** | Lớp liên kết toàn phần (Dense/Linear layer) | Lớp nơ-ron mà trong đó mọi nơ-ron đều được kết nối với tất cả các nơ-ron ở lớp trước nó. |
| **Gradient** | Đạo hàm (Gradient) | Vectơ đạo hàm riêng phần, chỉ hướng dốc nhất làm tăng giá trị của hàm mất mát. |
| **Gradient Descent** | Giảm độ dốc (Gradient Descent) | Thuật toán tối ưu hóa nhằm cực tiểu hóa hàm mất mát bằng cách cập nhật tham số ngược hướng gradient. |
| **Hyperparameter** | Siêu tham số | Các thông số không được mô hình học từ dữ liệu mà do người thiết kế thiết lập trước (vd: learning rate, batch size, số epoch). |
| **Inference** | Suy luận / Dự đoán | Quá trình đưa dữ liệu mới vào mô hình đã huấn luyện xong để lấy kết quả dự đoán (không tính gradient). |
| **Large Language Model (LLM)** | Mô hình ngôn ngữ lớn | Mô hình AI xử lý ngôn ngữ tự nhiên dựa trên Transformer, chứa hàng triệu đến hàng trăm tỷ tham số và được huấn luyện trên lượng văn bản khổng lồ. |
| **Learning Rate** | Tốc độ học (Learning rate) | Siêu tham số quyết định kích thước bước tiến trong mỗi lần cập nhật trọng số của thuật toán tối ưu. |
| **Logits** | Logits (Giá trị đầu ra thô) | Kết quả đầu ra của lớp cuối cùng trong mạng nơ-ron, trước khi qua hàm kích hoạt xác suất (như softmax). |
| **Loss Function** | Hàm mất mát (Loss function) | Hàm đánh giá độ chênh lệch giữa kết quả dự đoán của mô hình và nhãn thực tế. |
| **Machine Learning** | Học máy | Phân ngành của AI nghiên cứu các thuật toán cho phép máy tính tự học tập và cải thiện hiệu suất từ dữ liệu. |
| **Matrix** | Ma trận | Một mảng số liệu 2 chiều (2D tensor). |
| **Multilayer Perceptron (MLP)** | Perceptron đa tầng / Mạng nơ-ron truyền thẳng đa tầng | Kiến trúc mạng nơ-ron tiến (feedforward) gồm ít nhất ba lớp: input, hidden, và output kết nối toàn phần. |
| **Optimizer** | Bộ tối ưu hóa (Optimizer) | Thuật toán (như SGD, AdamW) dùng để cập nhật các trọng số của mạng dựa trên gradient nhằm giảm thiểu hàm mất mát. |
| **Overfitting** | Quá khớp (Overfitting) | Tình trạng mô hình học thuộc lòng dữ liệu huấn luyện (kể cả nhiễu) dẫn đến khả năng tổng quát hóa kém trên dữ liệu mới. |
| **Parameter** | Tham số / Trọng số | Các biến số nội bộ (weights và biases) của mô hình được tối ưu tự động trong quá trình học từ dữ liệu. |
| **Pretraining** | Tiền huấn luyện (Pre-training) | Giai đoạn huấn luyện sơ khởi mô hình trên dữ liệu lớn, chưa gán nhãn để nắm bắt cấu trúc ngôn ngữ trước khi tinh chỉnh. |
| **Prompt** | Câu lệnh điều hướng (Prompt) | Đoạn văn bản đầu vào do người dùng cung cấp để hướng dẫn LLM sinh ra nội dung mong muốn. |
| **Scalar** | Đại lượng vô hướng | Một giá trị số đơn lẻ (0D tensor). |
| **Stochastic Gradient Descent (SGD)** | Hạ độ dốc ngẫu nhiên (SGD) | Biến thể của Gradient Descent thực hiện tính gradient và cập nhật tham số sau mỗi lô (mini-batch) ngẫu nhiên. |
| **Supervised Learning** | Học có giám sát | Phương pháp học máy mà trong đó mô hình được huấn luyện trên tập dữ liệu có các cặp (đầu vào, nhãn mục tiêu). |
| **Tensor** | Tensor | Cấu trúc dữ liệu mảng đa chiều tổng quát hóa của scalar (0D), vector (1D), ma trận (2D) và các chiều cao hơn. |
| **Test Dataset** | Tập kiểm thử (Test set) | Tập dữ liệu độc lập chỉ dùng để đánh giá khách quan độ chính xác cuối cùng của mô hình sau khi huấn luyện xong. |
| **Training Dataset** | Tập huấn luyện (Training set) | Bộ dữ liệu được sử dụng trực tiếp để tối ưu hóa trọng số mô hình. |
| **Unstructured Data** | Dữ liệu phi cấu trúc | Dữ liệu không theo cấu trúc bảng cố định, ví dụ như văn bản tự nhiên, hình ảnh, âm thanh. |
| **Validation Dataset** | Tập xác thực (Validation set) | Tập dữ liệu dùng để theo dõi quá trình huấn luyện, tinh chỉnh siêu tham số và phát hiện quá khớp. |
| **Vector** | Vectơ | Một mảng số liệu 1 chiều (1D tensor). |
| **Weights** | Trọng số (Weights) | Các tham số có thể huấn luyện nằm trên các kết nối giữa các nơ-ron, quy định cường độ liên kết và truyền tín hiệu. |

*Bảng thuật ngữ này được duy trì và cập nhật xuyên suốt quá trình dịch.*
