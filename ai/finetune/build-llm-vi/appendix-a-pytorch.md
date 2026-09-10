# Phụ lục A: Giới thiệu về PyTorch

Phụ lục này được thiết kế để trang bị cho bạn những kỹ năng và kiến thức cần thiết nhằm đưa học sâu (deep learning) vào thực tiễn và tự tay triển khai các mô hình ngôn ngữ lớn (LLM). PyTorch, một thư viện deep learning phổ biến trên nền tảng Python, sẽ là công cụ chính của chúng ta xuyên suốt cuốn sách này. Tôi sẽ hướng dẫn bạn cách thiết lập môi trường deep learning với PyTorch và bật hỗ trợ GPU.

Tiếp theo, bạn sẽ tìm hiểu về khái niệm trọng tâm là các "tensor" và cách sử dụng chúng trong PyTorch. Chúng ta cũng sẽ đào sâu vào cỗ máy vi phân tự động (automatic differentiation engine) của PyTorch, một tính năng cho phép chúng ta áp dụng thuật toán lan truyền ngược (backpropagation) một cách thuận tiện và hiệu quả, vốn là một thành phần then chốt trong quá trình huấn luyện mạng nơ-ron.

Phụ lục này đóng vai trò như bài vỡ lòng dành cho những ai mới tiếp cận deep learning bằng PyTorch. Dù nó giải thích PyTorch từ những nền tảng cơ bản nhất, đây không phải là một tài liệu bách khoa toàn thư che phủ mọi tính năng của PyTorch. Thay vào đó, chúng sẽ chỉ tập trung vào các khái niệm nền tảng thiết yếu để lập trình LLM. Nếu bạn đã có sẵn nền tảng về deep learning, bạn có thể mạnh dạn bỏ qua phụ lục này và đi thẳng tới chương 2.

## A.1 PyTorch là gì?

PyTorch (https://pytorch.org/) là một thư viện deep learning mã nguồn mở dựa trên Python. Theo tổ chức Papers With Code (https://paperswithcode.com/trends), một nền tảng chuyên theo dõi và phân tích các bài báo nghiên cứu, PyTorch đã trở thành thư viện deep learning được sử dụng rộng rãi nhất cho nghiên cứu với khoảng cách áp đảo kể từ năm 2019. Và theo Khảo sát về Khoa học Dữ liệu và Học Máy của Kaggle năm 2022 (https://www.kaggle.com/c/kaggle-survey-2022), số lượng người tham gia khảo sát sử dụng PyTorch xấp xỉ 40% và vẫn đang tăng lên hàng năm.

Một trong những lý do khiến PyTorch phổ biến đến vậy là giao diện thân thiện với người dùng và hiệu suất của nó. Bất chấp sự dễ dùng, nó không hề thỏa hiệp về tính linh hoạt, cho phép người dùng chuyên sâu tinh chỉnh các khía cạnh cấp thấp nhất của mô hình để tùy biến và tối ưu hóa. Tóm lại, đối với nhiều kỹ sư và nhà nghiên cứu, PyTorch mang lại sự cân bằng hoàn hảo giữa tính dễ dùng (usability) và các tính năng mạnh mẽ.

### A.1.1 Ba thành phần cốt lõi của PyTorch

PyTorch là một thư viện tương đối toàn diện, và một cách để tiếp cận nó là tập trung vào ba thành phần cốt lõi của nó, được tóm tắt trong hình A.1.

Đầu tiên, PyTorch là một thư viện tensor mở rộng từ mô hình lập trình mảng (array-oriented) của thư viện NumPy, cộng thêm tính năng tăng tốc tính toán trên các phần cứng GPU, từ đó cung cấp sự chuyển đổi mượt mà giữa CPU và GPU. Thứ hai, PyTorch là một cỗ máy vi phân tự động, hay còn gọi là autograd, cho phép tính toán tự động đạo hàm (gradient) cho các phép tính trên tensor, làm đơn giản hóa thuật toán backpropagation và tối ưu mô hình. Cuối cùng, PyTorch là một thư viện deep learning thực thụ. Nó cung cấp các khối (building blocks) lập trình dạng module linh hoạt và hiệu quả, bao gồm các mô hình được huấn luyện sẵn (pretrained models), các hàm mất mát (loss functions) và các bộ tối ưu hóa (optimizers), để thiết kế và huấn luyện đủ mọi loại mô hình deep learning cho giới nghiên cứu và lập trình viên.

[Hình A.1: Ba thành phần cốt lõi của PyTorch bao gồm thư viện tensor như khối hình khối nền tảng tính toán, cỗ máy vi phân tự động cho việc tối ưu mô hình, và các hàm công cụ deep learning, làm cho việc cài đặt và huấn luyện mạng nơ-ron dễ dàng hơn.]

### A.1.2 Định nghĩa về Deep learning

Trên báo chí, các mô hình LLM thường được gọi là mô hình AI (trí tuệ nhân tạo). Tuy nhiên, LLM cũng là một loại deep neural network (mạng nơ-ron sâu), và PyTorch lại là thư viện deep learning (học sâu). Nghe có vẻ rối rắm? Hãy dành một phút tóm tắt mối quan hệ giữa các thuật ngữ này trước khi đi tiếp.

AI về cơ bản là việc tạo ra các hệ thống máy tính có khả năng thực hiện các tác vụ vốn yêu cầu trí tuệ con người. Các tác vụ này bao gồm hiểu ngôn ngữ tự nhiên, nhận dạng hình mẫu và ra quyết định. (Mặc dù đã có những tiến bộ đáng kể, AI vẫn còn lâu mới đạt được cấp độ trí tuệ tổng quát như con người).

Machine learning (Học máy) là một nhánh con của AI, như minh họa ở hình A.2, tập trung vào việc phát triển và cải tiến các thuật toán học tập. Ý tưởng trọng tâm đằng sau machine learning là cho phép máy tính tự học từ dữ liệu và đưa ra các dự đoán hoặc quyết định mà không cần lập trình rõ ràng (hard-code) từng nguyên tắc một. Quá trình này bao gồm các thuật toán có khả năng nhận dạng khuôn mẫu (pattern), học từ dữ liệu lịch sử và cải thiện hiệu suất theo thời gian khi được tiếp nạp nhiều dữ liệu và phản hồi (feedback) hơn.

Machine learning không thể thiếu trong sự tiến hóa của AI, tạo động lực cho nhiều tiến bộ mà chúng ta đang thấy ngày nay, bao gồm cả các LLM. Machine learning cũng đứng sau các công nghệ như hệ thống đề xuất (recommendation) của các nền tảng bán lẻ và dịch vụ phát trực tuyến, bộ lọc thư rác, nhận diện giọng nói trong các trợ lý ảo, và cả xe tự lái. Sự ra đời và tiến bộ của machine learning đã nâng cao đáng kể các năng lực của AI, giúp nó vượt khỏi các hệ thống dùng quy tắc cứng nhắc (rule-based) để thích ứng với dữ liệu đầu vào mới hoặc những môi trường luôn thay đổi.

Deep learning (Học sâu) lại là một nhánh con của machine learning, chuyên tập trung vào việc huấn luyện và ứng dụng các deep neural network. Các deep neural network vốn dĩ được truyền cảm hứng từ cách bộ não con người làm việc, đặc biệt là sự liên kết giữa vô số nơ-ron. Chữ "deep" (sâu) trong deep learning ngụ ý có nhiều lớp ẩn (hidden layers) bao gồm các nơ-ron nhân tạo hoặc các nút cho phép chúng mô hình hóa được các mối quan hệ phi tuyến tính phức tạp trong dữ liệu. Khác với các kỹ thuật machine learning truyền thống chỉ làm tốt ở các tác vụ nhận dạng khuôn mẫu đơn giản, deep learning cực kỳ xuất sắc trong việc xử lý dữ liệu phi cấu trúc (unstructured data) như hình ảnh, âm thanh hay văn bản, nên nó đặc biệt hoàn hảo cho mô hình ngôn ngữ lớn (LLM).

Quy trình (workflow) lập mô hình dự đoán điển hình (cũng được biết đến là học có giám sát - supervised learning) trong machine learning và deep learning được tóm tắt ở hình A.3.

Bằng một thuật toán học tập, mô hình sẽ được huấn luyện trên một bộ dữ liệu (dataset) bao gồm các ví dụ (examples) và các nhãn (labels) tương ứng. Lấy ví dụ ở bài toán phân loại email rác, bộ training dataset sẽ bao gồm các email và các nhãn "spam" và "not spam" do một người phân loại. Sau đó, mô hình đã được huấn luyện có thể đem ra sử dụng cho các quan sát mới (tức các email mới) để dự đoán nhãn chưa biết ("spam" hay "not spam"). Dĩ nhiên, ta sẽ luôn thêm bước đánh giá hiệu năng (model evaluation) chen giữa giai đoạn huấn luyện (training) và suy luận (inference) để đảm bảo mô hình thỏa mãn các tiêu chí đặt ra trước khi mang vào sử dụng ở môi trường thực tế.

[Hình A.2: Deep learning là phân ngành con của machine learning, tập trung xây dựng mạng deep neural network. Machine learning lại là phân ngành con của AI chuyên thiết kế thuật toán học từ dữ liệu. AI là khái niệm rộng nhất đại diện cho những cái máy sở hữu năng lực trí tuệ con người.]

[Hình A.3: Quy trình học có giám sát (supervised learning) cho mô hình dự đoán (predictive modeling). Ở giai đoạn huấn luyện, ta huấn luyện mô hình dựa trên các cặp nhãn. Khi huấn luyện xong, mô hình được dùng để dự đoán nhãn (label) cho dữ liệu mới.]

Nếu chúng ta huấn luyện LLM để phân loại văn bản, quy trình huấn luyện LLM sẽ tương tự như quy trình được mô tả ở hình A.3. Nhưng ngay cả khi ta muốn huấn luyện LLM để "sinh" ra văn bản đi nữa - mục tiêu chính của chúng ta - thì hình A.3 vẫn đúng. Trong trường hợp này, các "nhãn" trong giai đoạn tiền huấn luyện chính là văn bản (task dự đoán từ tiếp theo như ở chương 1). Dựa trên yêu cầu đầu vào (prompt), LLM sẽ sinh ra một câu hoàn toàn mới (thay vì dự đoán nhãn).

### A.1.3 Cài đặt PyTorch

PyTorch có thể được cài đặt dễ dàng như bất kỳ thư viện hoặc gói (package) Python nào khác. Tuy nhiên, vì PyTorch là một bộ thư viện đồ sộ có khả năng tối ưu hóa cho CPU lẫn GPU, nên quá trình cài đặt cần có thêm lời giải thích.

> **Phiên bản Python**
> Rất nhiều thư viện tính toán khoa học không hỗ trợ ngay lập tức các phiên bản mới nhất của Python. Do đó, khi cài đặt PyTorch, lời khuyên là hãy sử dụng một phiên bản Python lùi lại một hoặc hai đợt. Ví dụ, nếu phiên bản Python mới nhất đang là 3.13, bạn nên sử dụng Python 3.11 hoặc 3.12.

Ví dụ, hiện có hai phiên bản PyTorch: một phiên bản rút gọn chỉ hỗ trợ tính toán bằng CPU và một phiên bản đầy đủ có hỗ trợ CPU và GPU. Nếu máy bạn có card GPU chuẩn CUDA (lý tưởng nhất là NVIDIA T4, RTX 2080 Ti trở lên), tôi khuyên bạn nên cài phiên bản GPU. Bất luận thế nào, câu lệnh cài đặt mặc định của PyTorch trong terminal là:

```bash
pip install torch
```

Giả sử máy tính của bạn hỗ trợ GPU chuẩn CUDA, nó sẽ tự động nhận diện và cài đặt phiên bản PyTorch có hỗ trợ tăng tốc GPU thông qua CUDA, với điều kiện môi trường Python của bạn đã cài đặt các thành phần phụ thuộc (như pip).

> **LƯU Ý**
> Tại thời điểm cuốn sách này được viết, PyTorch đã bắt đầu thử nghiệm hỗ trợ các GPU của AMD qua ROCm. Hãy truy cập trang chủ https://pytorch.org để xem hướng dẫn bổ sung.

Để chỉ định cài đặt phiên bản hỗ trợ CUDA một cách minh bạch, cách tốt nhất là chọn đúng phiên bản CUDA mà PyTorch tương thích. Website chính thức của PyTorch (https://pytorch.org) sẽ cung cấp cú pháp (commands) chuẩn để cài PyTorch cho từng hệ điều hành. Hình A.4 hiển thị một đoạn mã không chỉ tải PyTorch mà còn tải `torchvision` và `torchaudio` (hai thư viện này là tùy chọn với nội dung sách).

Tôi sử dụng PyTorch 2.4.0 cho các ví dụ trong sách, vì vậy tôi khuyến cáo bạn dùng lệnh sau để cài đặt chính xác phiên bản này nhằm đảm bảo tính tương thích:

```bash
pip install torch==2.4.0
```

[Hình A.4: Truy cập trang đề xuất cài đặt PyTorch trên https://pytorch.org để tùy chỉnh và chọn cấu hình cài đặt phù hợp với hệ thống máy tính của bạn.]

Tuy nhiên, tùy theo hệ điều hành, lệnh cài đặt có thể khác đôi chút so với lệnh trên. Do đó, tôi khuyên bạn vào trang https://pytorch.org và sử dụng menu cài đặt (xem hình A.4) để chọn lệnh cài đặt chuẩn. Nhớ thay thế `torch` thành `torch==2.4.0` trong câu lệnh của bạn.

Để kiểm tra phiên bản của PyTorch, thực thi đoạn code sau trong Python:

```python
import torch
torch.__version__
```
Đầu ra sẽ in ra:
```
'2.4.0'
```

Nếu bạn tìm kiếm các chỉ dẫn phụ để cài đặt môi trường lập trình Python hoặc các thư viện khác, bạn có thể tham khảo mục tài liệu hỗ trợ của sách (supplementary) tại https://github.com/rasbt/LLMs-from-scratch.

Sau khi cài đặt PyTorch, bạn có thể kiểm tra xem máy tính của bạn có nhận diện GPU NVIDIA nội trú hay không bằng cách chạy mã sau trong Python:

```python
import torch
torch.cuda.is_available()
```
Đầu ra sẽ là:
```
True
```

Nếu kết quả trả về `True`, bạn đã sẵn sàng. Còn nếu về `False`, máy tính của bạn có thể không có một GPU tương thích, hoặc PyTorch chưa nhận ra được nó. Dù các GPU không quá bắt buộc ở những chương đầu, nó sẽ mang lại tốc độ xử lý nhanh hơn đáng kể khi tính toán.

> **PyTorch và Torch**
> Thư viện Python được đặt tên là PyTorch chủ yếu vì nó là sự kế thừa của thư viện Torch nhưng được điều chỉnh cho Python (do đó có tên "PyTorch"). Cái tên "Torch" vinh danh nguồn gốc của thư viện này trong Torch, một nền tảng lập trình máy tính dành cho khoa học với sự hỗ trợ rộng rãi cho các thuật toán học máy, vốn ban đầu được viết bằng ngôn ngữ lập trình Lua.

Nếu không sở hữu GPU, trên thị trường có vài nhà cung cấp dịch vụ cloud cho thuê GPU theo giờ với giá phải chăng. Môi trường phổ biến có hình thái giống Jupyter notebook là Google Colab (https://colab.research.google.com), cung cấp quyền truy cập giới hạn thời gian vào GPU. Dùng thanh menu Runtime, bạn có thể lựa chọn GPU theo hướng dẫn ở hình A.5.

> **PyTorch trên Apple Silicon**
> Nếu bạn sở hữu máy Mac dùng chip Apple Silicon (như M1, M2, M3 hoặc cao hơn), bạn có thể khai thác nó để tăng tốc cho PyTorch. Đầu tiên bạn cứ cài PyTorch như bình thường. Rồi kiểm tra tính năng bằng đoạn code sau:
> ```python
> print(torch.backends.mps.is_available())
> ```
> Nếu kết quả về `True`, Mac của bạn hoàn toàn đủ tính năng dùng Apple Silicon để boot tốc độ cho PyTorch.

> **Bài tập A.1**
> Cài đặt và set-up PyTorch vào trong máy tính.
> 
> **Bài tập A.2**
> Chạy code mẫu trong phần tài liệu bổ sung (https://mng.bz/o05v) để kiểm chứng xem cài đặt đã chuẩn chỉnh chưa.

[Hình A.5: Chọn thiết bị GPU cho môi trường Google Colab ở tab Runtime/Change Runtime Type.]

## A.2 Hiểu về tensor

Tensor là một khái niệm toán học tổng quát từ các véc-tơ (vector) và ma trận (matrix) lên các chiều (dimension) cao hơn. Nói cách khác, tensor là các đối tượng toán học được đặc trưng bởi thứ hạng (order hay rank) của chúng - quy định số lượng chiều. Ví dụ, một vô hướng (scalar - bản chất chỉ là một số) là một tensor có thứ hạng 0 (rank 0), véc-tơ là tensor có thứ hạng 1, ma trận là tensor có thứ hạng 2, được minh họa ở hình A.6.

Ở khía cạnh lập trình máy tính, tensor đóng vai trò như các container trữ dữ liệu. Ví dụ, chúng trữ mảng dữ liệu nhiều chiều (multidimensional), nơi mà mỗi chiều biểu thị một tính năng (feature) riêng biệt. Các thư viện tensor như PyTorch có khả năng nhào nặn và tính toán với các mảng số liệu trên với tốc độ bàn thờ. Trong bối cảnh đó, thư viện tensor chính là array library (thư viện mảng).

Tensor của PyTorch có nhiều nét tương đồng với các array (mảng) trong thư viện NumPy, nhưng PyTorch cung cấp vài tính năng phụ thêm vốn không thể thiếu đối với lập trình deep learning. Đơn cử, PyTorch có thêm công cụ lấy vi phân (đạo hàm) tự động, giúp việc tính toán gradient vô cùng nhẹ nhàng (xem mục A.4). Tensor PyTorch cũng hỗ trợ tính toán trên GPU để đẩy nhanh tốc độ training (xem mục A.8).

### A.2.1 Vô hướng (scalar), véc-tơ, ma trận và tensor

Như đã đề cập trước đó, PyTorch tensor là vùng chứa dữ liệu cho các cấu trúc giống như array (mảng). Vô hướng (scalar) là một tensor không có chiều (chỉ là một số), véc-tơ là tensor một chiều (1D) và ma trận là tensor hai chiều (2D). Không có các thuật ngữ chuyên biệt cho tensor có thứ nguyên cao hơn nên chúng ta thường quy ước gọi chung tensor ba chiều là tensor 3D, v.v. Để tạo mới đối tượng cho lớp Tensor, dùng hàm `torch.tensor` như Listing A.1.

> **PyTorch với API mang phong cách NumPy**
> PyTorch áp dụng hầu hết hàm API và cú pháp về xử lý array của NumPy cho các phương thức trên tensor của mình. Nếu bạn chưa rành về NumPy, bạn có thể đọc tham khảo về các tính năng cần thiết tại "Scientific Computing in Python: Introduction to NumPy and Matplotlib" tại https://sebastianraschka.com/blog/2020/numpy-intro.html.

[Hình A.6: Các loại Tensor với từng bậc (rank) tương ứng. 0D là hạng 0, 1D là hạng 1, và 2D là hạng 2. Một vector ba chiều chứa ba phần tử, nhưng nó vẫn là tensor hạng 1.]

**Listing A.1: Khởi tạo các PyTorch tensor**

```python
import torch

# Khởi tạo một tensor 0 chiều (scalar) từ một số integer
tensor0d = torch.tensor(1)    

# Khởi tạo một tensor 1 chiều (vector) từ list Python
tensor1d = torch.tensor([1, 2, 3])   

# Khởi tạo một tensor 2 chiều từ list lồng nhau
tensor2d = torch.tensor([[1, 2], 
                         [3, 4]])    

# Khởi tạo một tensor 3 chiều từ list lồng nhau
tensor3d = torch.tensor([[[1, 2], [3, 4]], 
                         [[5, 6], [7, 8]]])   
```

### A.2.2 Kiểu dữ liệu tensor

PyTorch mặc định kế thừa loại dữ liệu (data type) kiểu số nguyên 64-bit từ Python. Dùng thẻ `.dtype` của tensor sẽ truy xuất được nó:

```python
tensor1d = torch.tensor([1, 2, 3])
print(tensor1d.dtype)
```
In ra:
```
torch.int64
```

Nhưng nếu ta tạo tensor bằng số thập phân (float), PyTorch sẽ mặc định hạ chuẩn 32-bit (chứ không phải 64-bit của Python).

```python
floatvec = torch.tensor([1.0, 2.0, 3.0])
print(floatvec.dtype)
```
Kết quả in ra là:
```
torch.float32
```

Sự lựa chọn này chủ yếu đến từ việc cân bằng giữa mức độ tính toán chính xác và hiệu suất. Khai báo mảng float 32-bit cung cấp độ chính xác vừa đủ cho hầu hết các nhiệm vụ deep learning nhưng tiêu tốn ít bộ nhớ và tài nguyên hơn so với float 64-bit. Thêm vào đó, kiến trúc GPU hiện đại vốn được tối ưu hóa cho các phép tính 32-bit, sử dụng kiểu dữ liệu này đẩy nhanh tốc độ đào tạo và suy luận vô cùng đáng kể.

Thêm nữa, ta có thể đổi dung lượng dữ liệu bằng hàm `.to`. Code sau sẽ biến số nguyên 64-bit về số lẻ 32-bit:

```python
floatvec = tensor1d.to(torch.float32)
print(floatvec.dtype)
```
Đầu ra là:
```
torch.float32
```

Để tìm hiểu thêm về các data types khả dụng của Tensor, hãy tham khảo tài liệu chính thức tại: https://pytorch.org/docs/stable/tensors.html.

### A.2.3 Các lệnh thực thi tensor phổ biến

Tuy cuốn sách này sẽ không thể nhồi nhét mọi thư mục lệnh của thư viện PyTorch, nhưng tôi sẽ mô tả ngắn gọn một vài lệnh phổ biến thường gặp trong cuốn sách.

Chúng ta đã được giới thiệu về `torch.tensor()` để tạo một tensor mới:
```python
tensor2d = torch.tensor([[1, 2, 3], 
                         [4, 5, 6]])
print(tensor2d)
```
Nó sẽ in ra ma trận:
```
tensor([[1, 2, 3],
        [4, 5, 6]])
```

Bên cạnh đó, thẻ thuộc tính `.shape` giúp soi khung kích cỡ của tensor:
```python
print(tensor2d.shape)
```
Nó sẽ in ra:
```
torch.Size([2, 3])
```
Kết quả báo về `[2, 3]`, tức tensor bao gồm hai hàng (row) và ba cột (column). Để nhào nặn lại tensor thành ma trận 3 × 2, dùng hàm `.reshape`:
```python
print(tensor2d.reshape(3, 2))
```
Nó in ra:
```
tensor([[1, 2],
        [3, 4],
        [5, 6]])
```

Tuy nhiên, lưu ý rằng cú pháp phổ biến hơn của thao tác này trong PyTorch lại là dùng hàm `.view()`:
```python
print(tensor2d.view(3, 2))
```
Kết quả in ra cũng là:
```
tensor([[1, 2],
        [3, 4],
        [5, 6]])
```

Giống như với `.reshape` và `.view`, ở một số tình huống PyTorch có vô vàn các biến thể cho cùng một tác vụ. Nguyên nhân là do PyTorch từ ban đầu được xây dựng để kế thừa ngôn ngữ Lua, nhưng về sau theo thị hiếu người dùng mà cập nhật thêm để các cú pháp giống hệt NumPy. (Sự khác biệt tinh tế giữa `.view()` và `.reshape()` trong PyTorch nằm ở cách chúng xử lý mảng layout của bộ nhớ: `.view()` yêu cầu bộ dữ liệu gốc (original data) phải liền kề với nhau và sẽ báo lỗi nếu không đáp ứng, trong khi `.reshape()` vẫn sẽ hoạt động bất kể mọi thứ và sẵn sàng sao chép dữ liệu để định hình tensor theo cách người dùng muốn).

Kế tiếp, hàm `.T` dùng để dịch chuyển hoán đổi chéo trục tọa độ ngang dọc (transpose). Thao tác này khá giống như bóp nặn khung matrix `reshape`, ví dụ:
```python
print(tensor2d.T)
```
Kết quả:
```
tensor([[1, 4],
        [2, 5],
        [3, 6]])
```

Cuối cùng, hàm `.matmul` dùng để thực hiện phép nhân ma trận đa chiều với nhau:
```python
print(tensor2d.matmul(tensor2d.T))
```
Kết quả in ra ma trận:
```
tensor([[14, 32],
        [32, 77]])
```

Tuy nhiên, thay vì gõ dài dòng như vậy, ta có thể dùng biểu tượng toán tử `@` thay thế:
```python
print(tensor2d @ tensor2d.T)
```
Phép nhân trả về đáp án i xì:
```
tensor([[14, 32],
        [32, 77]])
```

Như đã nói, trong chương này tôi sẽ dùng hàm tới đâu giới thiệu tới đó, nhưng nếu bạn muốn tìm hiểu kho tàng các lệnh tensor mà PyTorch hỗ trợ, mời đọc tài liệu tại: https://pytorch.org/docs/stable/tensors.html.

## A.3 Mô phỏng Model qua các đồ thị (Graph) tính toán

Bây giờ ta hãy cùng mổ xẻ cỗ máy (engine) vi phân tự động của PyTorch, còn gọi là autograd. Hệ thống autograd của PyTorch cung cấp các hàm để tự động tính toán gradient trong các đồ thị (graph) đa chiều và sinh động.

Khái niệm "computational graph" là một đồ thị có hướng cho phép chúng ta thể hiện và hình dung các phương trình toán học phức tạp. Trong bối cảnh học sâu (deep learning), một computational graph sẽ trải ra sơ đồ một chuỗi các bước nhằm đo đếm đầu ra của neural network. Từ đó ta sẽ dựa trên con số này để tiến hành tính toán các thông số gradient cho hàm backpropagation (hàm backpropagation là một dạng giải thuật huấn luyện mạng neural).

Hãy nhìn vào ví dụ cụ thể này để làm rõ khái niệm computation graph. Phép xử lý ở listing dưới đây thực hiện một hàm nhồi dữ liệu tuần tự (forward pass) của hàm logistic regression, có thể xem như một mạng nơ-ron chỉ có duy nhất một lớp. Nó trả về kết quả dự đoán với điểm số từ 0 đến 1, sau đó so sánh với nhãn thực tế true class label (0 hoặc 1) khi đưa vào hàm suy hao (loss function).

**Listing A.2: Phép nhồi logistic regression tuyến tính (forward pass)**

```python
# Lệnh import thu gọn gõ tắt này rất phổ biến ở PyTorch
import torch.nn.functional as F    

y = torch.tensor([1.0])         # Nhãn thực tế (True label)
x1 = torch.tensor([1.1])        # Các thuộc tính (Input feature)
w1 = torch.tensor([2.2])        # Tham số trọng lượng (Weight parameter)
b = torch.tensor([0.0])         # Biến số thiên vị (Bias unit)

z = x1 * w1 + b                 # Hàm tuyến tính nhập (Net input)
a = torch.sigmoid(z)            # Kích hoạt ra kết quả 
loss = F.binary_cross_entropy(a, y)  # Chạy hàm cross_entropy
```

Nếu bạn không thể nắm bắt tường tận từng dòng, đừng lo lắng. Ở đây mục đích của ta không phải là cài đặt logistic regression, mà là phác họa cách chuỗi các sự kiện đó kết hợp với nhau ra làm sao tạo thành một đồ thị toán học như hình A.7.

Trên thực tế, PyTorch sẽ ngầm xây dựng đồ thị tương tự chạy dưới hệ thống nền, để rồi khi có được tham số suy hao (loss parameter), nó sẽ tính ngược trở lại giá trị gradient để đem qua cho các chỉ số trọng lượng ($w_1$, $b$) để thực hiện việc tối ưu.

[Hình A.7: Một mô phỏng (forward pass) tính tuyến tính của đồ thị computation graph. Chỉ số đầu vào x1 nhân với trọng lượng w1 và cho lọt qua hàm kích hoạt (activation function) kết hợp với bias. Các con số hàm suy hao loss parameter a được xử lý cùng với dữ liệu nhãn mác y.]

## A.4 Lấy vi phân tự động trở nên vô cùng dễ dàng

Khi ta nhập liệu và tính toán bằng PyTorch, nó sẽ tự động dựng một sơ đồ thuật toán đồ thị trong hệ thống ngầm định nếu như tham số `.requires_grad=True` được kích hoạt ở một nút mạng bất kỳ. Autograd hữu ích vô cùng với việc tự tính đạo hàm gradient. (Và gradient là tài sản vô giá với cái thuật toán huấn luyện vĩ đại mang tên backpropagation (lan truyền ngược)). Tính backpropagation vốn có thể coi là phép khai triển hàm phức quy tắc chuỗi (chain rule) đối với các mạng neural network (xem hình A.8).

> **ĐẠO HÀM RIÊNG PHẦN VÀ GRADIENT**
> Hình A.8 biểu diễn một dạng hàm lấy đạo hàm riêng phần (partial derivatives), nơi mà nó đo đạc tốc độ tăng giảm của hàm số so với những biến số riêng lẻ tương ứng. Còn "gradient" là véc-tơ tổng hợp quy tụ toàn bộ chuỗi các đạo hàm riêng phần của một đa hàm (multivariate function - hàm có trên 2 ẩn số) vào làm một mảng thông tin.
>
> Nếu bạn đã quên sạch sành sanh mấy khái niệm đạo hàm, vi phân riêng phần, gradient, hay chain rule từ cấp 3 thì đừng hoảng hốt. Ở trên bình diện tổng quan cho cuốn sách này, tất cả những gì bạn cần biết đó là "chain rule" chính là công thức cốt lõi dùng để tính gradient đối với một đồ thị hàm loss. Có thông số này chúng ta mới mang đi điều chỉnh được cho từng biến số nhỏ nhặt, sao cho tổng thể giảm được hàm mất mát (loss function - một kiểu phép đo điểm kém của mô hình), nhằm mục tiêu tối ưu hiệu năng của mô hình thông qua gradient descent. Chúng ta sẽ đào sâu khái niệm vòng lặp này ở mục A.7.

Thế cái này liên quan gì tới động cơ vi phân (autograd) là cái thành phần thứ 2 của PyTorch? Động cơ này lập trình sơ đồ toán học bằng cách tracking mọi tham số và thông tin mỗi khi tensor có biến động. Sau đó nhờ gọi hàm `grad` mà ta tóm được giá trị gradient của quá trình (Ví dụ ở model thông số parameter w1) (Listing A.3).

[Hình A.8: Phương pháp thông dụng nhất để tính hàm gradient của đồ thị là lấy theo chain rule từ phải qua trái (lan truyền ngược autograd). Chúng ta xuất phát từ lớp output cho tới input layer để dò thông số. Công việc nặng nhọc này nhằm cung cấp dữ liệu định hướng cho quá trình trau dồi model ở mục A.7.]

**Listing A.3: Tính Gradient bằng autograd**

```python
import torch.nn.functional as F
from torch.autograd import grad

y = torch.tensor([1.0])
x1 = torch.tensor([1.1])
w1 = torch.tensor([2.2], requires_grad=True)
b = torch.tensor([0.0], requires_grad=True)

z = x1 * w1 + b 
a = torch.sigmoid(z)
loss = F.binary_cross_entropy(a, y)

# Theo cài đặt chuẩn, Pytorch sẽ xóa sổ Computation Graph ngay khi xử 
# lý xong gradients để dọn sạch bộ nhớ. Tuy nhiên, nếu muốn tận dụng
# lại sơ đồ này ngay sau đó, phải đặt thuộc tính retain_graph=True
grad_L_w1 = grad(loss, w1, retain_graph=True)  
grad_L_b = grad(loss, b, retain_graph=True)
```

Kết quả của bộ hàm suy hao so với parameter w1 và b in ra là:
```python
print(grad_L_w1)
print(grad_L_b)
```
Kết quả hiển thị:
```
(tensor([-0.0898]),)
(tensor([-0.0817]),)
```

Ở ví dụ trên, chúng ta dùng phương thức thủ công đối với hàm `grad`, điều vốn được khuyến nghị cho các công đoạn thí nghiệm, dò lỗi bugs hay thử chức năng. Tuy nhiên trong thực tiễn, PyTorch cung cấp một thư viện nâng cao để làm điều này. Tỉ dụ, bằng việc gọi thẳng hàm `.backward` (lan truyền ngược) cắm vào biến hàm mất mát loss, PyTorch sẽ chạy hết và tóm trọn bộ thuộc tính của đồ thị, trữ trong giá trị `.grad`:

```python
loss.backward()
print(w1.grad)
print(b.grad)
```
Cho ra kết quả hoàn toàn tương tự:
```
(tensor([-0.0898]),)
(tensor([-0.0817]),)
```

Tuy là nãy giờ tôi nhồi sọ bạn quá nhiều thuật ngữ hàn lâm với phép tính, nhưng cũng đừng vội nản. Vì đằng sau mớ ma trận thuật ngữ lằng nhằng đó, PyTorch tự động ôm trọn hết tất thảy các phép giải mã này thông qua cụm API `.backward` duy nhất, chúng ta sẽ không bao giờ cần phải ngồi nháp vẽ lại đạo hàm bằng tay như thời thi đại học đâu.

## A.5 Triển khai mạng neural nhiều lớp (Multilayer neural networks)

Tiếp đến ta hãy để mắt tới PyTorch dưới hình hài của một thư viện đồ sộ có khả năng cung cấp nền tảng tính toán triển khai cấu trúc mạng deep neural networks. Để lấy ví dụ minh họa, ta xem mô hình phân lớp nơ-ron đa cực (multilayer perceptron) dưới dạng fully connected theo hình A.9.

Để ứng dụng cấu trúc này cho lập trình, ta tạo một lớp mạng (class) kế thừa từ lớp cha `torch.nn.Module`. Lớp Module base class này được trang bị sẵn vô số phương thức hỗ trợ tối ưu việc tạo lập hệ thống. Ví dụ: đóng gói các hàm vận hành cấu trúc mạng với nhau và theo dấu thông số trọng lượng của chúng.

Trong bản thể mới vừa được tạo lập, ta định nghĩa một mạng thông qua phương thức `__init__` constructor và trình bày sự tương tác của chúng bằng phương thức `forward`. Phương thức `forward` thể hiện quá trình dữ liệu đi từ cửa vào cho tới ngõ ra theo cách vẽ ở hàm graph. Chiều ngược lại (lấy đạo hàm của tham số weights bằng suy hao), hàm `backward` không đòi hỏi ta phải tự viết code thủ công (xem A.7). 

Dưới đây (Listing A.4), chúng ta biểu diễn cấu trúc của hệ thống phân tầng perceptron điển hình có 2 tầng ẩn, thể hiện đầy đủ cho công thức viết code với base class `Module`.

[Hình A.9: Ví dụ minh họa một mô hình phân tầng nơ-ron (multilayer perceptron) hai tầng ẩn. Mỗi điểm nút tròn biểu diễn cho một phần tử ở trong một layer. Do để minh họa nên số nút ở đây rất ít.]

**Listing A.4: Mạng multilayer perceptron với hai lớp ẩn**

```python
class NeuralNetwork(torch.nn.Module):
    # Khai báo thông số nạp input/output qua tham số truyền biến
    # Cách code này giúp hệ thống ứng dụng được cho đa dạng các loại
    # dataset khác biệt.
    def __init__(self, num_inputs, num_outputs):   
        super().__init__()
        self.layers = torch.nn.Sequential(
                
            # Hàm Linear nhận dữ liệu cho ngõ vô và ngõ ra.
            # Lớp ẩn thứ 1
            torch.nn.Linear(num_inputs, 30),
            # Hàm phi tuyến hàm kích hoạt chen giữa
            torch.nn.ReLU(),              
            
            # Lớp ẩn thứ 2
            # Bắt buộc input lớp trong phải khớp với output lớp bên ngoài.
            torch.nn.Linear(30, 20),   
            torch.nn.ReLU(),
            
            # Tầng xuất dữ liệu output. Đầu ra được gọi chung là các 'logits'
            torch.nn.Linear(20, num_outputs),
        )

    def forward(self, x):
        logits = self.layers(x)
        return logits          
```

Sau khi lập trình xong, ta khởi tạo (instantiate) một bản thể neural network của lớp này:
```python
model = NeuralNetwork(50, 3)
```

Trước khi cho chạy, ta dùng hàm in `print` trên model này để xem lướt bảng hệ thống kiến trúc của nó:
```python
print(model)
```
Kết quả in ra cấu trúc:
```
NeuralNetwork(
  (layers): Sequential(
    (0): Linear(in_features=50, out_features=30, bias=True)
    (1): ReLU()
    (2): Linear(in_features=30, out_features=20, bias=True)
    (3): ReLU()
    (4): Linear(in_features=20, out_features=3, bias=True)
  )
)
```

Lưu ý rằng chúng ta dùng lớp đối tượng `Sequential` lúc viết chương trình trên. Dùng cấu trúc mảng Sequential tuy không bắt buộc, nhưng lại tỏ ra cực kì mượt mà hữu hiệu nếu hệ thống đòi hỏi thiết lập một hàng dài các tầng layer nối tiếp nhau. Lợi thế là ở chỗ thay vì chúng ta phải lập trình truy cập vào từng layer độc lập, biến `self.layers` bọc trong `Sequential` cho phép kích hoạt toàn chuỗi liên hoàn chỉ với dòng lệnh `self.layers` đơn giản thông qua hàm `forward`.

Bây giờ ta tính xem cái model còm này có bao nhiêu tham số:
```python
num_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
print("Total number of trainable model parameters:", num_params)
```
Kết quả:
```
Total number of trainable model parameters: 2213
```

Mỗi biến parameter có nhãn cờ hiệu `requires_grad=True` được đếm và gọi chung là 1 parameter được huấn luyện trong mạng nơ-ron (xem mục A.7).

Với mạng mô hình chứa hai tầng ẩn như trên, mọi trọng số đào tạo được lèn vào bên trong các đối tượng thuộc `torch.nn.Linear`. Đối tượng lớp mạng Linear biến hóa tham số bằng phép toán ma trận cùng hằng số thiên hướng (bias). Lớp xử lý dữ liệu này mang tên "feedforward" (truyền thẳng/nhồi qua) hoặc "fully connected" (liên kết toàn phần).

Theo như những gì hàm in `print(model)` gọi báo ở phía trên, ta phát hiện ở vị trí thứ [0] ngay đầu chuỗi hàm truy cập là một khối xử lý Linear. Chúng ta bóc tách trọng số bằng code sau:
```python
print(model.layers[0].weight)
```
In ra kết quả tham số:
```
Parameter containing:
tensor([[ 0.1174, -0.1350, -0.1227,  ...,  0.0275, -0.0520, -0.0192],
        [-0.0169,  0.1265,  0.0255,  ..., -0.1247,  0.1191, -0.0698],
        [-0.0973, -0.0974, -0.0739,  ..., -0.0068, -0.0892,  0.1070],
        ...,
        [-0.0681,  0.1058, -0.0315,  ..., -0.1081, -0.0290, -0.1374],
        [-0.0159,  0.0587, -0.0916,  ..., -0.1153,  0.0700,  0.0770],
        [-0.1019,  0.1345, -0.0176,  ...,  0.0114, -0.0559, -0.0088]],
       requires_grad=True)
```
Đống ma trận này quá đồ sộ để theo dõi trên màn hình, thay vào đó ta xài hàm soi góc chiếu `.shape`:
```python
print(model.layers[0].weight.shape)
```
Trả về dạng ma trận 30 × 50:
```
torch.Size([30, 50])
```
(Tương tự như cách trên, bạn có thể soi mảng thiên vị (bias vector) dùng `model.layers[0].bias`.)

Thêm nữa, biến `requires_grad` được gán vào thẻ True, mang ý nghĩa rằng các giá trị bên trong hoàn toàn có thể hiệu chỉnh được (hay còn gọi là train) (đây là thiết lập mặc định của lệnh hàm `torch.nn.Linear`).

Dĩ nhiên ma trận của bạn tạo sẽ ra số random khác biệt. Những con số cực nhỏ ngẫu nhiên lúc ban đầu mang nhiệm vụ phá vỡ thế đối xứng lúc mới đào tạo. Nếu không, các điểm nút sẽ tính toán giống hệt nhau rồi dồn ứ cho thuật toán autograd backpropagation, làm mạng nơ ron bị chết đứng và tịt đường học cái cấu trúc phức tạp.

Tuy vậy, nếu ta vẫn muốn làm ngẫu nhiên cho thuật toán mà vẫn bảo toàn được sự nhất quán ở các lần thử thì hãy áp dụng seed random cố định cho hàm `manual_seed`:
```python
torch.manual_seed(123)
model = NeuralNetwork(50, 3)
print(model.layers[0].weight)
```
Kết quả hiển thị luôn cố định cho mọi máy:
```
Parameter containing:
tensor([[-0.0577,  0.0047, -0.0702,  ...,  0.0222,  0.1260,  0.0865],
        [ 0.0502,  0.0307,  0.0333,  ...,  0.0951,  0.1134, -0.0297],
        [ 0.1077, -0.1108,  0.0122,  ...,  0.0108, -0.1049, -0.1063],
        ...,
        [-0.0787,  0.1259,  0.0803,  ...,  0.1218,  0.1303, -0.1351],
        [ 0.1359,  0.0175, -0.0673,  ...,  0.0674,  0.0676,  0.1058],
        [ 0.0790,  0.1343, -0.0293,  ...,  0.0344, -0.0971, -0.0509]],
       requires_grad=True)
```

Giờ là lúc ta test cho cái mạng model rỗng này thử chạy forward pass:
```python
torch.manual_seed(123)
X = torch.rand((1, 50))
out = model(X)
print(out)
```
Kết quả 3 số âm dương bất kỳ:
```
tensor([[-0.1262,  0.1080, -0.1792]], grad_fn=<AddmmBackward0>)
```

Trong dòng lệnh trên, tôi đã tự khởi tạo một mẫu biến x rỗng đầu tiên (với input cần là hệ 50 phần tử) và truyền vào `model`. Lúc ấy cái hàm forward tự chạy.

Phép truyền dữ liệu theo phương forward pass là thực hiện đi qua từ điểm cửa (input) dọc theo các lớp tầng ẩn (hidden layer) và lọt tới điểm ngõ (output layer).

Thứ trả về sau hàng loạt đợt nhào lộn chính là bộ 3 con số, điểm giá trị ngõ ra. Chú ý rằng ở đuôi của dòng kết quả kèm theo thông số hàm tính `grad_fn`.

Thuộc tính này mang chức danh là hàm truy vấn gradient tính toán lùi của đồ thị, đánh mã số `AddmmBackward0`. Cụm từ `AddmmBackward0` mang ý nghĩa chỉ thị báo cáo thao tác ma trận nhân cộng ở khâu truy quét lùi, `Add` (Cộng) và `mm` (matrix multiplication). PyTorch nhờ thuộc tính đó mà dễ bề đi tính đạo hàm.

Còn nếu, sau khi ta huấn luyện thành thục và hoàn thành, ta không muốn đi cập nhật các giá trị trọng lượng trong mạng model này thêm một bước nào nữa — chẳng hạn khi ta lấy kết quả dự đoán (prediction inference) — mà thuật toán cỗ máy vi phân lại cứ nạp thông tin gradient đằng sau chạy tốn cả bộ nhớ ram, ta lập tức bóp tính năng ngốn RAM vô thưởng vô phạt đó đi bằng cụm `torch.no_grad()`:
```python
with torch.no_grad():
    out = model(X)
print(out)
```
Dòng kết quả trả về trở nên cực kì tinh giản (gradient tracking đã tắt):
```
tensor([[-0.1262,  0.1080, -0.1792]])
```

Ở môi trường đồ thị PyTorch, việc lấy mảng đồ thị `logits` xuất ngõ (điểm giá trị cuối) lúc kết thúc một tầng mà bỏ qua hẳn một bộ lọc giới hạn hàm phi tuyến là rất bình thường. Điều đó có lợi về mặt đo lường sự khác biệt về sai số, tiết kiệm được thuật toán. Nếu chúng ta thích lấy ra hệ thập phân cho hệ thống thành tỉ lệ xác suất, chúng ta dùng bộ hàm `softmax` bao ngoài ngõ ra `model(X)`:
```python
with torch.no_grad():
    out = torch.softmax(model(X), dim=1)
print(out)
```
Kết quả hiển thị:
```
tensor([[0.3113, 0.3934, 0.2952]])
```
Lúc này 3 hệ số đầu ra đã bọc thêm giá trị tỉ lệ tổng bằng 1. Đây cũng là một thứ hệ số cân bằng và bất định dành cho bất cứ mô hình khởi tạo random rỗng não.

## A.6 Cài đặt bộ tải dữ liệu (data loaders) hiệu quả

Trước khi bước vào huấn luyện mô hình, chúng ta phải bàn ngắn gọn về cách tạo ra một bộ tải dữ liệu (data loaders) tối ưu, thứ sẽ được cỗ máy lặp qua lặp lại vô vàn vòng trong quá trình huấn luyện. Ý tưởng tổng quan đằng sau cơ chế nhồi dữ liệu trong PyTorch được mô tả ở hình A.10.

Tuân theo mô tả ở hình A.10, ta sẽ triển khai một lớp tùy biến `Dataset` để sinh ra hai tệp dữ liệu training dataset (dữ liệu huấn luyện) và test dataset (dữ liệu kiểm tra). Sau đó, hai tệp này sẽ được bơm vào cho hệ thống phân phối data loaders. Hãy bắt đầu bằng một dữ liệu đồ chơi mini chỉ gồm năm mẫu dữ liệu huấn luyện, mỗi mẫu gồm hai thông số feature. Đồng hành với các dữ liệu training này, ta sẽ nặn ra một bộ tensor chuyên chứa dữ liệu nhãn phân lớp (class labels) đi kèm tương ứng: 3 mẫu dữ liệu thuộc về class 0, và 2 mẫu dữ liệu thuộc về class 1. Bổ sung thêm, ta nặn nốt một bộ test set gồm vỏn vẹn 2 mẫu. Cấu trúc để tạo ra cái nồi thập cẩm này được biểu diễn ở Listing A.5.

**Listing A.5: Tạo một đồ chơi dữ liệu siêu tí hon**

```python
X_train = torch.tensor([
    [-1.2, 3.1],
    [-0.9, 2.9],
    [-0.5, 2.6],
    [2.3, -1.1],
    [2.7, -1.5]
])
y_train = torch.tensor([0, 0, 0, 1, 1])

X_test = torch.tensor([
    [-0.8, 2.8],
    [2.6, -1.6],
])
y_test = torch.tensor([0, 1])
```

[Hình A.10: PyTorch cài đặt lớp `Dataset` và `DataLoader`. Lớp `Dataset` được dùng để khởi tạo từng bản ghi độc lập. Đối tượng `DataLoader` nắm quyền quản lý sự tráo đổi và lèn dữ liệu thành các cục batch dữ liệu khổng lồ.]

> **LƯU Ý**
> PyTorch yêu cầu các nhãn dữ liệu (class labels) phải được đánh số thứ tự khởi đầu là 0, và cái mác phân loại lớn nhất không được vượt quá số nút ngõ ra trừ đi 1 (bởi index trong Python đếm từ số không). Vậy nếu chúng ta có các dòng mác nhãn lớp 0, 1, 2, 3, và 4, thì số lượng nơ-ron output phải thiết lập là 5 nơ-ron.

Kế đến, ta nặn một lớp dữ liệu chuyên biệt có tên `ToyDataset` kế thừa mọi thứ tinh hoa từ lớp cha `Dataset` của PyTorch (Listing A.6).

**Listing A.6: Khai báo một lớp Dataset chuyên biệt**

```python
from torch.utils.data import Dataset

class ToyDataset(Dataset):
    def __init__(self, X, y):
        self.features = X
        self.labels = y

    # Chỉ thị này nhặt đúng một cặp đối tượng dựa vào số dòng
    def __getitem__(self, index):       
        one_x = self.features[index]    
        one_y = self.labels[index]      
        return one_x, one_y             

    # Chỉ thị báo cáo chiều dài dữ liệu
    def def __len__(self):
        return self.labels.shape[0]     

train_ds = ToyDataset(X_train, y_train)
test_ds = ToyDataset(X_test, y_test)
```

Mục đích tạo ra cái `ToyDataset` dị biệt này là để cấp nhiên liệu vận hành cỗ máy `DataLoader` của PyTorch. Nhưng khoan vội vã, ta hãy ngắm nghía sơ qua cái cấu trúc chung của đoạn code `ToyDataset`.

Trong môi trường PyTorch, ba trụ cột cơ bản của mọi file lớp `Dataset` là `__init__`, `__getitem__`, và `__len__` (xem Listing A.6). Ở hàm `__init__`, chúng ta thiết lập biến thuộc tính cho việc gọi lại ở các khâu `__getitem__` và `__len__`. Các thông số đó có thể là tệp văn bản, vật chứa, tài khoản database, v.v. Do ta tự dùng hệ thống biến lưu vào RAM bộ nhớ bằng tensor, ta chỉ đơn giản là gắn hai nhãn mác X và y cho hai đối tượng này.

Ở hàm `__getitem__`, ta đặt nguyên tắc nhặt đúng và nhặt chuẩn chỉ một đơn vị (item) ra khỏi bộ hồ sơ bằng chỉ số mục lục index. Việc này hướng thẳng tới thông số tính năng và cái mác thuộc tính của dữ liệu train hoặc test đó. (Bộ điều phối DataLoader tự cung cấp cho ta tham số index này, ta sẽ bàn sau).

Ở khâu cuối `__len__`, nơi này chứa cái khai báo chiều dài bộ khung chứa. Bằng thẻ `shape` của bộ tensor, hệ thống trả về con số chiều dài các dòng. Với cái file dataset mẫu, nó báo là 5 hàng.

```python
print(len(train_ds))
```
Kết quả in ra:
```
5
```

Giờ khi đã lên khuôn xong cái lớp hồ sơ cho hệ thống bằng PyTorch, ta lấy module điều phối `DataLoader` ra để lấy dữ liệu. Xem listing A.7.

**Listing A.7: Khởi tạo băng chuyền data loaders**

```python
from torch.utils.data import DataLoader

torch.manual_seed(123)

train_loader = DataLoader(
    # Băng chuyền truyền thẳng đối tượng ToyDataset được nặn nãy giờ vào đây 
    dataset=train_ds,    
    batch_size=2,

    # Khai báo có cho phép trộn mớ hỗn độn này lên hay không
    shuffle=True,         

    # Thiết lập số lượng process hệ thống vận hành
    num_workers=0    
)

test_loader = DataLoader(
    dataset=test_ds,
    batch_size=2,
    
    # Không cần phải xáo trộn bộ dữ liệu Test (Kiểm tra)
    shuffle=False,    
    num_workers=0
)
```

Một khi đúc được cái khuôn data loader rồi, giờ ta rải đinh nó. Lặp ở khâu test cũng giống thế nên ta rút ngắn lại:

```python
for idx, (x, y) in enumerate(train_loader):
    print(f"Batch {idx+1}:", x, y)
```
Kết quả hiển thị:
```
Batch 1: tensor([[-1.2000,  3.1000],
                 [-0.5000,  2.6000]]) tensor([0, 0])
Batch 2: tensor([[ 2.3000, -1.1000],
                 [-0.9000,  2.9000]]) tensor([1, 0])
Batch 3: tensor([[ 2.7000, -1.5000]]) tensor([1])
```

Dựa trên thứ in ra ở bảng hiển thị, ta thấy cỗ máy vòng lặp train_loader chạy một nháy xuyên thủng bộ danh sách đồ chơi dataset, điểm mặt không chừa một khuôn mẫu train nào (nó thăm viếng đúng 1 lần). Cuộc càn quét vô biên này được định danh là một `kỷ nguyên huấn luyện` (training epoch). Hơn nữa do thuật gán số seed ngẫu nhiên bằng `torch.manual_seed(123)` ở khâu tạo dựng ban đầu, cỗ máy sẽ in ra thứ tự tráo đổi vị trí hệt như ở màn hình của bạn. Chứ nếu bạn thử chạy lại vòng hai xem, thứ tự trộn bị đảo lộn không nhận ra ngay. Lý do là để cỗ máy deep neural network không bao giờ bị ù lì vướng vào một con hẻm lặp đi lặp lại nhạt nhẽo đâm ra phán đoán sai lệch rập khuôn sáo rỗng.

Trong ví dụ ở trên, ta yêu cầu mỗi nhóm là 2 mẫu, nhưng ở mâm thứ ba chỉ có duy nhất một đối tượng mẫu mã. Lý do là có tổng 5 phần tử mẫu, 5 làm sao chia hết cho 2!
Trong thực tiễn môi trường lớn, một nhóm batch bé xíu bị lẻ còi cọc đu bám ở đuôi nhóm sẽ cản trở quá trình mượt mà của hệ thống đào tạo. Cách thanh trừng tốt nhất là tiễn nó ra rìa bằng nhãn `drop_last=True` ở khâu khai báo, như ở Listing A.8.

**Listing A.8: Một băng chuyền train vứt bỏ cụm bị mẻ ở đít nhóm**

```python
train_loader = DataLoader(
    dataset=train_ds,
    batch_size=2,
    shuffle=True,
    num_workers=0,
    drop_last=True
)
```
Giờ hãy ngắm băng chuyền chạy xem cái cụm cuối bị tiễn đi đâu nào:
```python
for idx, (x, y) in enumerate(train_loader):
    print(f"Batch {idx+1}:", x, y)
```
Kết quả hiển thị:
```
Batch 1: tensor([[-0.9000,  2.9000],
        [ 2.3000, -1.1000]]) tensor([0, 1])
Batch 2: tensor([[ 2.7000, -1.5000],
        [-0.5000,  2.6000]]) tensor([1, 0])
```

Vấn đề cuối cùng, tôi và bạn hãy bàn nốt về tham số `num_workers=0` trong hàm DataLoader. Thông số này thực sự giữ vị thế sống còn cho quá trình ép xử lý đồng loạt đa quy trình giữa nạp file và phân tách nén file. Việc khai báo bằng 0 báo cho hệ thống ngưng làm trò tải file bằng các quy trình luồng độc lập, mà tập trung sức mạnh dồn lực xử lý trên hệ thống trung tâm. Nghe có vẻ hoàn toàn chẳng dính lỗi logic tẹo nào phải không? Tuy nhiên nó sẽ làm ngẽn đường băng hệ thống huấn luyện đối với mô hình khổng lồ dùng sức cày GPU. Chẳng những tài nguyên GPU không tập trung vào cái công việc vĩ đại học hỏi hệ thống của mô hình mạng nơ ron, mà CPU còn làm trì trệ quá trình bằng cách tranh thủ lúc rảnh rỗi dọn dẹp nhồi và nạp data. CPU lúc ấy làm kẹt hệ thống GPU ở chế độ nghỉ đông. 
Ngược lại, khi nhích `num_workers` lên một hệ số lớn hơn 0, một loạt đàn lính thợ phân chia nhau ôm luồng quy trình (process) dọn nạp vào bộ nhớ RAM ở background. Việc đó nhường ngõ và không gian để cái CPU dồn hết sức mạnh lo cho chuyện học hành mô hình (hình A.11).

Tuy nhiên, với mớ bộ đồ chơi nhỏ lặt vặt như mẫu trên, cái tham số chỉnh lên cao không có quá nhiều ý nghĩa do thời lượng train chưa bằng một phần nghìn giây đồng hồ. Vì thế nếu test trên hệ Jupyter notebook hay các bộ mini, tăng thông số không giúp cải tiến thêm tẹo nào mà còn gây hệ lụy. Hệ lụy to nhất chính là gánh nặng khởi động đàn kiến thợ quy trình quá đông cho công việc không xứng tầm. Một khi thời gian kêu gọi lính thợ lấp đầy lâu hơn cả thời gian tải của dữ liệu thì lúc đó hệ thống bị ì ạch cực kì phiền phức.

Thêm vào đó, ở môi trường Jupyter notebooks, chỉnh số `num_workers` vượt biên số 0 lắm khi phá nát hệ sinh thái vì xung đột tài nguyên giữa các tiến trình hệ thống, dẫn đến hiện tượng văng màn hình xanh crash hoặc ngưng báo lỗi rầm rộ. Khôn ngoan nhất chính là phải nắm bắt cán cân thỏa hiệp trong thông số thiết lập `num_workers`. Đặt giá trị đúng, chạy nhẹ tựa lông hồng. Nhưng bắt buộc phải ước lượng dựa theo lượng dung lượng và phần cứng máy móc của từng bên.

Với tư cách là một kẻ lăn lộn chiến trường, tôi hay đặt biến cờ `num_workers=4`. Số 4 thường tỏ ra là hệ số bùa hộ mệnh phù hợp nhất cho mọi bộ máy, nhưng quyết định cuối cùng vẫn thuộc quyền định đoạt vào phần cứng của bạn và tính chất khối lượng mẫu nạp của file Dataset.

[Hình A.11: Tải dữ liệu mà không bật chạy đa luồng thợ (num_workers=0) sẽ tạo thành cục nghẽn tải kẹt cổ chai dữ liệu nơi mà model cứ ngồi không ăn bám chờ nạp batch kế tiếp. Nhưng khi phân luồng, lính thợ tải data loader chuẩn bị nhét đầy các cụm kế tiếp ngay ở hàng đợi (bên phải).]

## A.7 Một vòng lặp đào tạo (training loop) điển hình

Tới giờ nạp dữ liệu train cho mô hình thần thánh rồi. Dưới đây liệt kê bộ khung source code.

**Listing A.9: Huấn luyện Neural network trên PyTorch**

```python
import torch.nn.functional as F

torch.manual_seed(123)

# Do mẫu có 2 tính năng input và 2 ngõ ra phân lớp
model = NeuralNetwork(num_inputs=2, num_outputs=2)   

# Cỗ máy nén (Optimizer) cần phải ngắm xem bộ nào bị đào tạo để điều 
# hướng (tinh chỉnh tốc độ bằng lr)
optimizer = torch.optim.SGD(
    model.parameters(), lr=0.5
)           

num_epochs = 3

for epoch in range(num_epochs): 
    
    model.train()
    for batch_idx, (features, labels) in enumerate(train_loader):
        logits = model(features)
       
        loss = F.cross_entropy(logits, labels)
        
        # Bắt buộc xóa bộ đếm gradient của hệ đợt trước về 0 để tránh cặn dồn cục 
        optimizer.zero_grad()           
        
        # Thiết bị cỗ máy ngầm kích hoạt tính gradient cho các mảng
        loss.backward()        
        
        # Cỗ máy Optimizer nhận số liệu và chà lướt model parameters
        optimizer.step()       
    
        ### LOGGING IN KẾT QUẢ ĐÀO TẠO
        print(f"Epoch: {epoch+1:03d}/{num_epochs:03d}"
              f" | Batch {batch_idx:03d}/{len(train_loader):03d}"
              f" | Train Loss: {loss:.2f}")

    model.eval()
    # Khu vực nhét thêm code đánh giá hiệu suất mô hình (tùy ý)
```

Chạy cái bọc nilon đó sẽ in ra nguyên si thành quả sau:
```
Epoch: 001/003 | Batch 000/002 | Train Loss: 0.75
Epoch: 001/003 | Batch 001/002 | Train Loss: 0.65
Epoch: 002/003 | Batch 000/002 | Train Loss: 0.44
Epoch: 002/003 | Batch 001/002 | Trainl Loss: 0.13
Epoch: 003/003 | Batch 000/002 | Train Loss: 0.03
Epoch: 003/003 | Batch 001/002 | Train Loss: 0.00
```

Như ta ngắm nhìn từ bảng số, độ sai số tụt tuốt về số 0 chẵn tròn ở kỷ nguyên thứ 3, một điềm báo tốt lành là mô hình đã hội tụ và đạt cảnh giới thấu hiểu tập train. Ở đây, ta dựng model gồm có hai luồng ngõ vô và hai đầu ngõ xuất. Ta sử dụng bộ cỗ máy tối ưu hóa số đạo hàm chập cheng mang tên stochastic gradient descent (SGD) nạp thêm tỉ lệ số tốc độ học thuật (lr - learning rate) đặt ở mức 0.5. Siêu tham số (hyperparameter - biến cài đặt ngoài model) có khả năng định độ dốc hội tụ ở mức tinh chỉnh tùy hứng khi ta thấy loss có biểu hiện trồi sụt. Ta rất khát khao ước ao mỏi mòn dò tìm con số thần chú cho tỉ lệ tốc độ học thuật để sai số vọt tụt xuống ở một chặng đường đào tạo epoch hợp lý — số epoch cũng lại là một thứ siêu tham số. 

Thực tế sương gió cho thấy, ta thường cần chi viện từ viện binh bộ tập dữ liệu thứ 3, cái tên giang hồ phong cho là "tập kiểm thử chéo xác thực" (validation dataset), hòng moi ra giá trị tốt đẹp của cái bầy thông số hyperparameter mệt mỏi này. Cái cục kiểm thử chéo này sinh đôi với cục test set, nhưng do mâm đồ cúng "test set" chỉ được giở nắp đúng 1 lần phòng bệnh ảo tưởng ăn gian trong hệ thống, cái tập kiểm thử này có thể mượn đi xài lại băm vằm hàng trăm lần đặng nặn chỉnh ra các setting siêu ngầu cho model.

Chúng ta cũng chèn thử các lệnh chỉ thị `model.train()` và `model.eval()`. Như lời kêu réo trong câu lệnh, những lệnh này chỉ nhằm ném cái mô hình model vào chế độ học sinh hoặc chế độ nhà phê bình đánh giá. Đây lại là đòi hỏi sinh tử với những cấu thành bộ phận hành vi thay đổi lúc train hoặc lúc soi như là các lớp rơi rụng (dropout layer) hoặc các lớp hàm điều biến theo cụm batch (batch normalization). Mạng nơ ron của chúng ta vốn làm bằng nilon chẳng bao giờ có mấy bộ áo xịn xò phức tạp ấy nên thật thừa thãi và chẳng làm gì, nhưng nếp sống gia giáo lập trình buộc ta vẫn phải cấy sẵn vào trước phòng trừ khi rảnh tay thay cái mạng xương quai xanh kiến trúc mô hình to tướng hoặc tải mã về chèn mô hình đồ cổ đem tái sử dụng thì đỡ bị hành.

Và như đàm phán sương sương từ trước đó, chúng ta bơm bộ đồ thị số `logits` phi thẳng luôn vào hàm phán quyết lỗi đạo hàm `cross_entropy`, để cái thuật hàm softmax tự thân vận động làm âm ỉ bên trong nội tạng máy đo vì lý trí năng suất và ổn định độ tính toán. Kế đó, hò nốt cái hàm `loss.backward()` tính giùm hệ số dốc số lượng ở cái mạng sơ đồ ẩn mà thằng PyTorch âm thầm đóng phía hậu đài. Cái chiêu `optimizer.step()` mượn đà xài tiếp mấy thông số này sửa cái đống tham số trọng lượng với hy vọng diệt gọn hệ số lỗi suy hao. Xét về bộ phận tối ưu hóa SGD của PyTorch, nó chỉ là con toán lấy tốc độ học (learning rate) nhân đạo hàm dốc trừ âm vào thông số trọng lượng mà thôi.

> **LƯU Ý**
> Để phòng cái họa gradient của kiếp luân hồi trước lưu manh cộng dồn với kiếp luân hồi sau tạo ra cục nghiệp chướng sai số rác rưởi, người dùng bắt buộc gài hàm `optimizer.zero_grad()` ở cuối lặp khai sinh mỗi đợt diệt dọn luân chuyển. Còn nếu không dọn rác, đống đạo hàm sẽ tích lũy sình ứ và mọi chuyện sẽ chẳng có gì để bàn sau đó.

Sau một đợt tu luyện đẫm máu cho cái mô hình chập choạng này, ta lôi nó ra xem trò phán đoán:
```python
model.eval()
with torch.no_grad():
    outputs = model(X_train)

print(outputs)
```
Kết quả trào ra là: 
```
tensor([[ 2.8569, -4.1618],
        [ 2.5382, -3.7548],
        [ 2.0944, -3.1820],
        [-1.4814,  1.4816],
        [-1.7176,  1.7342]])
```

Nhằm moi ra bằng được tỉ lệ trăm phần trăm định dạng thuộc tính mác hạng, ta gọi nốt lão già hàm `softmax` thuộc thư viện PyTorch ra:
```python
torch.set_printoptions(sci_mode=False)
probas = torch.softmax(outputs, dim=1)
print(probas)
```
Cái này ói ra:
```
tensor([[    0.9991,     0.0009],
        [    0.9982,     0.0018],
        [    0.9949,     0.0051],
        [    0.0491,     0.9509],
        [    0.0307,     0.9693]])
```

Hé mắt dòm hàng đầu tiên của bộ số này coi. Cột đầu tiên ám chỉ đối tượng 0 có 99,91% khả năng đúng dòng họ class 0, và chỉ ngắc ngoải 0.09% cơ hội nhập dòng họ class 1. (Lệnh `set_printoptions` chỉ nhằm khóa mồm hệ máy tính phun toán học hàn lâm giúp người đọc cho bớt lác mắt).

Còn có trò đùn cái bảng chỉ số lên chức thành con mác chính thống thông qua lệnh `argmax`, lệnh này trả về giá trị chỉ số dòng tối đa trên trục dòng `dim=1` (nếu đặt `dim=0` sẽ tìm dòng lớn nhất ở mỗi cột).
```python
predictions = torch.argmax(probas, dim=1)
print(predictions)
```
Băng in cho kết quả:
```
tensor([0, 0, 0, 1, 1])
```
Khổ, việc chạy softmax vốn cũng chả cần thiết cho lắm khi chỉ muốn lấy nhãn label. Đắp nốt con `argmax` dập lên hàm `outputs` (tức là cái `logits` nãy ấy) vẫn ra đúng bài.
```python
predictions = torch.argmax(outputs, dim=1)
print(predictions)
```
In i chang rứa:
```
tensor([0, 0, 0, 1, 1])
```

Vậy là chúng ta đã đoạt được nhãn dự đoán cho kho dữ liệu đào tạo. Do cái file train này có bé bằng mắt muỗi nên có thể đem lên soi đối chiếu mắt bằng tay cũng nhận ra lão mô hình máy tính đánh đúng 100%. Xác minh chuẩn nốt qua lệnh so trùng `==`:
```python
predictions == y_train
```
Cho cái vé:
```
tensor([True, True, True, True, True])
```
Giờ gọi nốt toán tổng `torch.sum` là đếm ra số lượng phán đoán bách phát bách trúng.
```python
torch.sum(predictions == y_train)
```
Lão về là:
```
5
```
Vì cái mâm dataset có vỏn vẹn 5 mẫu tập tành, mà trúng xổ số cả 5, suy ra: 5/5 x 100% = 100% độ chính xác cho bài học làm quen (prediction accuracy).

Để rập khuôn công thức tính ra cái bài toán tỉ lệ % này vô chương trình cho nó đa dụng tiện lợi, hãy ráp lại vào một mô tơ hàm lệnh `compute_accuracy`, mà nó sẽ được vẽ ra ở phần listing tiếp sau đây.
