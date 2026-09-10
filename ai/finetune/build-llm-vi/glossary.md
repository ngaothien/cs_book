# Bảng thuật ngữ (Glossary)

Bảng thuật ngữ này tổng hợp các khái niệm Khoa học Máy tính, Trí tuệ Nhân tạo (AI), Học máy (Machine Learning), và Học sâu (Deep Learning) được sử dụng trong cuốn sách, kèm theo bản dịch tiếng Việt tương ứng nhằm đảm bảo tính nhất quán.

| Thuật ngữ tiếng Anh | Thuật ngữ tiếng Việt | Giải thích ngắn gọn |
| :--- | :--- | :--- |
| **Artificial Intelligence (AI)** | Trí tuệ nhân tạo | Ngành khoa học máy tính nhằm tạo ra máy móc có khả năng bắt chước trí thông minh con người. |
| **Attention Mechanism** | Cơ chế chú ý | Cơ chế cho phép mạng nơ-ron tập trung vào các phần quan trọng của dữ liệu đầu vào. |
| **Autograd** | Cỗ máy vi phân tự động | Hệ thống của PyTorch tự động tính toán đạo hàm (gradient) cho các mạng nơ-ron. |
| **Backpropagation** | Lan truyền ngược | Thuật toán dùng để huấn luyện mạng nơ-ron bằng cách truyền ngược sai số từ đầu ra về đầu vào nhằm điều chỉnh trọng số. |
| **Batch** | Lô / Cụm dữ liệu | Một tập hợp con của dữ liệu huấn luyện được xử lý cùng lúc trong một vòng lặp. |
| **Batch Normalization** | Chuẩn hóa theo lô | Kỹ thuật chuẩn hóa đầu vào của từng lớp mạng nhằm tăng tốc độ huấn luyện và ổn định mô hình. |
| **Chain Rule** | Quy tắc chuỗi / Hàm phức | Quy tắc tính đạo hàm của hàm hợp trong giải tích, cốt lõi của thuật toán backpropagation. |
| **Class Label** | Nhãn phân lớp | Thẻ phân loại hoặc danh mục gán cho một dữ liệu đầu vào trong học có giám sát. |
| **Computation Graph** | Đồ thị tính toán | Một đồ thị có hướng thể hiện chuỗi các phép toán toán học trong mô hình mạng nơ-ron. |
| **Data Loader** | Bộ tải dữ liệu | Công cụ nạp, xáo trộn và đóng gói dữ liệu thành các lô (batch) để huấn luyện mô hình. |
| **Dataset** | Tập dữ liệu | Một tập hợp các dữ liệu dùng để huấn luyện, kiểm thử hoặc xác thực mô hình. |
| **Deep Learning** | Học sâu | Một nhánh của Machine Learning chuyên sử dụng các mạng nơ-ron sâu (nhiều lớp). |
| **Deep Neural Network** | Mạng nơ-ron sâu | Mạng nơ-ron nhân tạo có nhiều lớp ẩn ở giữa lớp đầu vào và lớp đầu ra. |
| **Dropout** | Lớp rơi rụng / Kỹ thuật Dropout | Kỹ thuật chuẩn hóa vô hiệu hóa ngẫu nhiên một số nơ-ron trong quá trình huấn luyện để chống overfit. |
| **Epoch** | Kỷ nguyên / Vòng lặp huấn luyện toàn bộ | Một chu kỳ huấn luyện khi toàn bộ tập dữ liệu đã được đưa qua mô hình mạng nơ-ron một lần. |
| **Finetuning** | Tinh chỉnh | Quá trình huấn luyện tiếp một mô hình đã được pre-trained trên một tập dữ liệu cụ thể để làm tốt một tác vụ. |
| **Forward Pass** | Phép lan truyền xuôi / Nhồi dữ liệu | Quá trình tính toán kết quả dự đoán của mô hình bằng cách đẩy dữ liệu từ đầu vào đến đầu ra. |
| **Fully Connected Layer** | Lớp liên kết toàn phần | Lớp nơ-ron mà trong đó mọi nơ-ron đều được kết nối với tất cả các nơ-ron ở lớp trước nó. |
| **Gradient** | Đạo hàm (theo hướng) / Gradient | Vectơ đạo hàm riêng phần, chỉ hướng dốc nhất của hàm mất mát. |
| **Gradient Descent** | Giảm chênh lệch / Giảm gradient | Thuật toán tối ưu hóa nhằm cực tiểu hóa hàm mất mát bằng cách cập nhật thông số ngược hướng gradient. |
| **Hyperparameter** | Siêu tham số | Các thông số không được mô hình học từ dữ liệu mà do người dùng thiết lập trước (vd: learning rate, số epoch). |
| **Inference** | Suy luận / Dự đoán | Quá trình đưa dữ liệu mới vào mô hình đã huấn luyện xong để lấy kết quả dự đoán. |
| **Large Language Model (LLM)** | Mô hình ngôn ngữ lớn | Mô hình AI xử lý ngôn ngữ tự nhiên, chứa hàng tỷ tham số và được huấn luyện trên lượng văn bản khổng lồ. |
| **Learning Rate** | Tốc độ học thuật | Siêu tham số quyết định kích thước bước tiến trong mỗi lần cập nhật trọng số của thuật toán tối ưu. |
| **Logits** | Logits / Giá trị ngõ ra thô | Kết quả đầu ra của lớp cuối cùng trong mạng nơ-ron, trước khi qua hàm kích hoạt (như softmax). |
| **Loss Function** | Hàm mất mát / Hàm suy hao | Hàm đánh giá độ chênh lệch giữa kết quả dự đoán của mô hình và kết quả thực tế. |
| **Machine Learning** | Học máy | Nhánh của AI nghiên cứu thuật toán cho phép hệ thống tự học tập và rút kinh nghiệm từ dữ liệu. |
| **Matrix** | Ma trận | Một mảng số liệu 2 chiều (2D tensor). |
| **Multilayer Perceptron (MLP)** | Mạng nơ-ron đa cực | Kiến trúc mạng nơ-ron tiến (feedforward) cơ bản gồm ít nhất ba lớp: input, hidden, và output. |
| **Optimizer** | Bộ tối ưu hóa (Optimizer) | Thuật toán hoặc phương pháp dùng để thay đổi các thuộc tính của mạng (như weights và learning rate) nhằm giảm loss. |
| **Overfitting** | Quá khớp / Học vẹt | Tình trạng mô hình học quá tốt trên tập huấn luyện nhưng dự đoán kém trên tập kiểm thử (dữ liệu mới). |
| **Parameter** | Tham số / Trọng số | Các biến số nội bộ của mô hình được máy tự động điều chỉnh trong quá trình học. |
| **Pretraining** | Tiền huấn luyện | Giai đoạn huấn luyện sơ khởi mô hình trên dữ liệu lớn, tổng quát trước khi tinh chỉnh cho tác vụ cụ thể. |
| **Prompt** | Câu lệnh điều hướng / Yêu cầu đầu vào | Dữ liệu đầu vào hoặc câu hỏi người dùng cung cấp cho LLM để nó sinh ra câu trả lời. |
| **Scalar** | Vô hướng | Một giá trị số đơn lẻ (0D tensor). |
| **Stochastic Gradient Descent (SGD)** | Thuật toán SGD | Biến thể của Gradient Descent thực hiện cập nhật thông số sau mỗi tập lô dữ liệu ngẫu nhiên. |
| **Supervised Learning** | Học có giám sát | Phương pháp học máy mà trong đó mô hình được huấn luyện bằng tập dữ liệu có dán nhãn sẵn. |
| **Tensor** | Tensor (Khối mảng) | Cấu trúc toán học dạng mảng nhiều chiều để chứa dữ liệu (tổng quát hóa của ma trận). |
| **Test Dataset** | Tập dữ liệu kiểm thử | Tập dữ liệu độc lập dùng để đánh giá độ chính xác cuối cùng của mô hình sau khi huấn luyện xong. |
| **Training Dataset** | Tập dữ liệu huấn luyện | Bộ dữ liệu được sử dụng để dạy cho mô hình cách đưa ra dự đoán. |
| **Unstructured Data** | Dữ liệu phi cấu trúc | Dữ liệu không có định dạng tổ chức cụ thể, ví dụ như hình ảnh, âm thanh, văn bản. |
| **Validation Dataset** | Tập kiểm thử chéo / Tập xác thực | Tập dữ liệu dùng để tinh chỉnh siêu tham số và ngăn chặn overfitting trong quá trình huấn luyện. |
| **Vector** | Vectơ | Một mảng số liệu 1 chiều (1D tensor). |
| **Weights** | Trọng số (Weights) | Các tham số có thể huấn luyện nằm trên các kết nối giữa các nơ-ron, quy định độ mạnh yếu của liên kết. |

*Bảng thuật ngữ này được duy trì và cập nhật xuyên suốt quá trình dịch.*
