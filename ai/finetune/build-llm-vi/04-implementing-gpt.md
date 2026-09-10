# Chương 4: Triển khai mô hình GPT từ đầu để sinh văn bản

Bạn đã học và viết code cơ chế multi-head attention, một trong những thành phần cốt lõi của LLM. Bây giờ, chúng ta sẽ viết code các khối xây dựng khác của LLM và lắp ráp chúng thành mô hình giống GPT mà chúng ta sẽ huấn luyện trong chương tiếp theo để sinh văn bản giống con người.

*Chương này bao gồm:*
- *Viết code mô hình ngôn ngữ lớn (LLM) giống GPT có thể được huấn luyện để sinh văn bản giống con người*
- *Chuẩn hóa kích hoạt lớp để ổn định huấn luyện mạng nơ-ron*
- *Thêm kết nối tắt (shortcut connection) trong mạng nơ-ron sâu*
- *Triển khai khối transformer để tạo mô hình GPT với các kích thước khác nhau*
- *Tính toán số lượng tham số và yêu cầu lưu trữ của mô hình GPT*

Kiến trúc LLM được tham chiếu trong hình 4.1, bao gồm nhiều khối xây dựng. Chúng ta sẽ bắt đầu với cái nhìn từ trên xuống của kiến trúc mô hình trước khi đề cập từng thành phần riêng lẻ chi tiết hơn.

[Hình 4.1: Ba giai đoạn chính của việc viết code LLM. Chương này tập trung vào bước 3 của giai đoạn 1: triển khai kiến trúc LLM.]

## 4.1 Viết code kiến trúc LLM

LLM, chẳng hạn như GPT (viết tắt của generative pretrained transformer), là kiến trúc mạng nơ-ron sâu lớn được thiết kế để sinh văn bản mới từng từ (hoặc token) một. Tuy nhiên, mặc dù kích thước lớn, kiến trúc mô hình ít phức tạp hơn bạn có thể nghĩ, vì nhiều thành phần được lặp lại, như chúng ta sẽ thấy sau. Hình 4.2 cung cấp cái nhìn từ trên xuống của LLM giống GPT, với các thành phần chính được đánh dấu.

Chúng ta đã đề cập nhiều khía cạnh của kiến trúc LLM, chẳng hạn như tokenization và nhúng đầu vào và module masked multi-head attention. Bây giờ, chúng ta sẽ triển khai cấu trúc cốt lõi của mô hình GPT, bao gồm các khối transformer, mà sau đó chúng ta sẽ huấn luyện để sinh văn bản giống con người.

[Hình 4.2: Mô hình GPT. Ngoài lớp nhúng, nó bao gồm một hoặc nhiều khối transformer chứa module masked multi-head attention mà chúng ta đã triển khai trước đó.]

Trước đó, chúng ta đã sử dụng chiều nhúng nhỏ hơn cho đơn giản, đảm bảo rằng các khái niệm và ví dụ có thể vừa trên một trang. Bây giờ, chúng ta đang mở rộng lên kích thước mô hình GPT-2 nhỏ, cụ thể là phiên bản nhỏ nhất với 124 triệu tham số, như mô tả trong "Language Models Are Unsupervised Multitask Learners" của Radford et al. (https://mng.bz/yoBq). Lưu ý rằng mặc dù báo cáo gốc đề cập 117 triệu tham số, điều này sau đó đã được chỉnh sửa. Trong chương 6, chúng ta sẽ tập trung vào việc nạp trọng số đã huấn luyện trước vào triển khai của chúng ta và điều chỉnh nó cho mô hình GPT-2 lớn hơn với 345, 762, và 1.542 triệu tham số.

Trong ngữ cảnh deep learning và LLM như GPT, thuật ngữ "tham số" (parameter) đề cập đến trọng số huấn luyện của mô hình. Các trọng số này thực chất là biến nội bộ của mô hình được điều chỉnh và tối ưu hóa trong quá trình huấn luyện để tối thiểu hóa hàm mất mát cụ thể. Sự tối ưu hóa này cho phép mô hình học từ dữ liệu huấn luyện.

> **GPT-2 so với GPT-3**
>
> Lưu ý rằng chúng ta tập trung vào GPT-2 vì OpenAI đã công khai trọng số của mô hình đã huấn luyện trước, mà chúng ta sẽ nạp vào triển khai của mình trong chương 6. GPT-3 về cơ bản giống nhau về kiến trúc mô hình, ngoại trừ nó được mở rộng từ 1.5 tỷ tham số trong GPT-2 lên 175 tỷ tham số trong GPT-3, và được huấn luyện trên nhiều dữ liệu hơn. Tại thời điểm viết, trọng số GPT-3 không được công khai. GPT-2 cũng là lựa chọn tốt hơn để học cách triển khai LLM, vì nó có thể chạy trên một máy tính xách tay, trong khi GPT-3 yêu cầu cụm GPU để huấn luyện và suy luận. Theo Lambda Labs (https://lambdalabs.com/), sẽ mất 355 năm để huấn luyện GPT-3 trên một GPU V100 datacenter và 665 năm trên GPU tiêu dùng RTX 8000.

Ví dụ, trong lớp mạng nơ-ron được biểu diễn bằng ma trận (hoặc tensor) trọng số 2.048 × 2.048 chiều, mỗi phần tử của ma trận này là một tham số. Vì có 2.048 hàng và 2.048 cột, tổng số tham số trong lớp này là 2.048 nhân 2.048, bằng 4.194.304 tham số.

Chúng ta chỉ định cấu hình mô hình GPT-2 nhỏ qua dictionary Python sau, mà chúng ta sẽ sử dụng trong các ví dụ code sau:

```python
GPT_CONFIG_124M = {
    "vocab_size": 50257,     # Kích thước từ vựng
    "context_length": 1024,  # Độ dài ngữ cảnh
    "emb_dim": 768,          # Chiều nhúng
    "n_heads": 12,           # Số attention head
    "n_layers": 12,          # Số lớp
    "drop_rate": 0.1,        # Tỷ lệ dropout
    "qkv_bias": False        # Bias Query-Key-Value
}
```

Trong dictionary GPT_CONFIG_124M, chúng ta sử dụng tên biến ngắn gọn cho rõ ràng và để tránh dòng code dài:

- `vocab_size` đề cập đến từ vựng 50.257 từ, như được sử dụng bởi tokenizer BPE (xem chương 2).
- `context_length` ký hiệu số lượng token đầu vào tối đa mà mô hình có thể xử lý qua nhúng vị trí (positional embedding) (xem chương 2).
- `emb_dim` đại diện cho kích thước nhúng, biến đổi mỗi token thành vector 768 chiều.
- `n_heads` chỉ số lượng attention head trong cơ chế multi-head attention (xem chương 3).
- `n_layers` chỉ định số khối transformer trong mô hình, mà chúng ta sẽ đề cập trong phần thảo luận sắp tới.
- `drop_rate` chỉ cường độ của cơ chế dropout (0.1 ngụ ý 10% loại bỏ ngẫu nhiên đơn vị ẩn) để ngăn overfitting (xem chương 3).
- `qkv_bias` xác định có bao gồm vector bias trong lớp Linear của multi-head attention cho tính toán truy vấn, khóa, và giá trị hay không. Chúng ta ban đầu sẽ tắt điều này, theo chuẩn của LLM hiện đại, nhưng sẽ xem lại trong chương 6 khi nạp trọng số GPT-2 đã huấn luyện trước từ OpenAI vào mô hình (xem chương 6).

Sử dụng cấu hình này, chúng ta sẽ triển khai kiến trúc GPT placeholder (DummyGPTModel), như hiển thị trong hình 4.3. Điều này sẽ cung cấp cho chúng ta cái nhìn tổng quan về cách mọi thứ khớp với nhau và những thành phần nào khác chúng ta cần viết code để lắp ráp kiến trúc GPT đầy đủ.

[Hình 4.3: Thứ tự chúng ta viết code kiến trúc GPT. Chúng ta bắt đầu với khung GPT, kiến trúc placeholder, trước khi đến các phần cốt lõi riêng lẻ và cuối cùng lắp ráp chúng trong khối transformer cho kiến trúc GPT cuối cùng.]

**Listing 4.1: Lớp kiến trúc mô hình GPT placeholder**

```python
import torch
import torch.nn as nn

class DummyGPTModel(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.tok_emb = nn.Embedding(cfg["vocab_size"], cfg["emb_dim"])
        self.pos_emb = nn.Embedding(cfg["context_length"], cfg["emb_dim"])
        self.drop_emb = nn.Dropout(cfg["drop_rate"])
        self.trf_blocks = nn.Sequential(              # Sử dụng placeholder
            *[DummyTransformerBlock(cfg)               # cho TransformerBlock
              for _ in range(cfg["n_layers"])]
        )
        self.final_norm = DummyLayerNorm(cfg["emb_dim"])    # Sử dụng placeholder
                                                             # cho LayerNorm
        self.out_head = nn.Linear(
            cfg["emb_dim"], cfg["vocab_size"], bias=False
        )

    def forward(self, in_idx):
        batch_size, seq_len = in_idx.shape
        tok_embeds = self.tok_emb(in_idx)
        pos_embeds = self.pos_emb(
            torch.arange(seq_len, device=in_idx.device)
        )
        x = tok_embeds + pos_embeds
        x = self.drop_emb(x)
        x = self.trf_blocks(x)
        x = self.final_norm(x)
        logits = self.out_head(x)
        return logits

class DummyTransformerBlock(nn.Module):   # Lớp placeholder đơn giản sẽ được
    def __init__(self, cfg):              # thay thế bằng TransformerBlock thật sau
        super().__init__()
    def forward(self, x):                 # Khối này không làm gì
        return x                          # và chỉ trả về đầu vào

class DummyLayerNorm(nn.Module):          # Lớp placeholder đơn giản sẽ được
    def __init__(self, normalized_shape, eps=1e-5):  # thay thế bằng LayerNorm thật sau
        super().__init__()                # Tham số ở đây chỉ để bắt chước
    def forward(self, x):                 # giao diện LayerNorm
        return x
```

Lớp DummyGPTModel trong code này định nghĩa phiên bản đơn giản hóa của mô hình giống GPT sử dụng module mạng nơ-ron của PyTorch (nn.Module). Kiến trúc mô hình trong lớp DummyGPTModel bao gồm nhúng token và vị trí, dropout, chuỗi khối transformer (DummyTransformerBlock), chuẩn hóa lớp cuối cùng (DummyLayerNorm), và lớp đầu ra tuyến tính (out_head). Cấu hình được truyền vào qua dictionary Python, ví dụ, dictionary GPT_CONFIG_124M chúng ta đã tạo trước đó.

Phương thức forward mô tả luồng dữ liệu qua mô hình: nó tính toán nhúng token và vị trí cho chỉ mục đầu vào, áp dụng dropout, xử lý dữ liệu qua các khối transformer, áp dụng chuẩn hóa, và cuối cùng tạo logit với lớp đầu ra tuyến tính.

Code trong listing 4.1 đã hoạt động được. Tuy nhiên, lưu ý rằng chúng ta sử dụng placeholder (DummyLayerNorm và DummyTransformerBlock) cho khối transformer và chuẩn hóa lớp, mà chúng ta sẽ phát triển sau.

Tiếp theo, chúng ta sẽ chuẩn bị dữ liệu đầu vào và khởi tạo mô hình GPT mới để minh họa cách sử dụng. Xây dựng trên phần viết code tokenizer (xem chương 2), hãy xem xét tổng quan cấp cao về cách dữ liệu chảy vào và ra khỏi mô hình GPT, như hiển thị trong hình 4.4.

[Hình 4.4: Tổng quan cấp cao cho thấy cách dữ liệu đầu vào được token hóa, nhúng, và đưa vào mô hình GPT. Lưu ý rằng trong DummyGPTClass đã viết code trước đó, nhúng token được xử lý bên trong mô hình GPT. Trong LLM, chiều nhúng token đầu vào thường khớp với chiều đầu ra. Nhúng đầu ra ở đây đại diện cho vector ngữ cảnh (xem chương 3).]

Để triển khai các bước này, chúng ta token hóa batch gồm hai văn bản đầu vào cho mô hình GPT sử dụng tokenizer tiktoken từ chương 2:

```python
import tiktoken
tokenizer = tiktoken.get_encoding("gpt2")
batch = []
txt1 = "Every effort moves you"
txt2 = "Every day holds a"
batch.append(torch.tensor(tokenizer.encode(txt1)))
batch.append(torch.tensor(tokenizer.encode(txt2)))
batch = torch.stack(batch, dim=0)
print(batch)
```

Các token ID kết quả cho hai văn bản là:

```
tensor([[6109,  3626,  6100,   345],   # Hàng đầu tiên tương ứng với văn bản đầu tiên
        [6109,  1110,  6622,   257]])   # hàng thứ hai tương ứng với văn bản thứ hai
```

Tiếp theo, chúng ta khởi tạo instance DummyGPTModel 124 triệu tham số mới và đưa batch đã token hóa vào:

```python
torch.manual_seed(123)
model = DummyGPTModel(GPT_CONFIG_124M)
logits = model(batch)
print("Output shape:", logits.shape)
print(logits)
```

Đầu ra mô hình, thường được gọi là logit, là:

```
Output shape: torch.Size([2, 4, 50257])
tensor([[[-1.2034,  0.3201, -0.7130,  ..., -1.5548, -0.2390, -0.4667],
         [-0.1192,  0.4539, -0.4432,  ...,  0.2392,  1.3469,  1.2430],
         [ 0.5307,  1.6720, -0.4695,  ...,  1.1966,  0.0111,  0.5835],
         [ 0.0139,  1.6755, -0.3388,  ...,  1.1586, -0.0435, -1.0400]],
        [[-1.0908,  0.1798, -0.9484,  ..., -1.6047,  0.2439, -0.4530],
         [-0.7860,  0.5581, -0.0610,  ...,  0.4835, -0.0077,  1.6621],
         [ 0.3567,  1.2698, -0.6398,  ..., -0.0162, -0.1296,  0.3717],
         [-0.2407, -0.7349, -0.5102,  ...,  2.0057, -0.3694,  0.1814]]],
       grad_fn=<UnsafeViewBackward0>)
```

Tensor đầu ra có hai hàng tương ứng với hai mẫu văn bản. Mỗi mẫu văn bản gồm bốn token; mỗi token là vector 50.257 chiều, khớp với kích thước từ vựng của tokenizer.

Nhúng có 50.257 chiều vì mỗi chiều này đề cập đến một token duy nhất trong từ vựng. Khi chúng ta triển khai code hậu xử lý, chúng ta sẽ chuyển đổi các vector 50.257 chiều này trở lại thành token ID, mà sau đó chúng ta có thể giải mã thành từ.

Bây giờ khi chúng ta đã xem xét kiến trúc GPT từ trên xuống và đầu vào đầu ra, chúng ta sẽ viết code các placeholder riêng lẻ, bắt đầu với lớp chuẩn hóa lớp thật sẽ thay thế DummyLayerNorm trong code trước.

## 4.2 Chuẩn hóa kích hoạt với layer normalization

Huấn luyện mạng nơ-ron sâu với nhiều lớp đôi khi có thể khó khăn do các vấn đề như gradient biến mất (vanishing gradient) hoặc gradient bùng nổ (exploding gradient). Các vấn đề này dẫn đến động lực huấn luyện không ổn định và gây khó khăn cho mạng trong việc điều chỉnh trọng số hiệu quả, nghĩa là quá trình học gặp khó khăn trong việc tìm bộ tham số (trọng số) cho mạng nơ-ron tối thiểu hóa hàm mất mát. Nói cách khác, mạng gặp khó khăn trong việc học các mẫu cơ bản trong dữ liệu đến mức cho phép đưa ra dự đoán hoặc quyết định chính xác.

> **LƯU Ý:** Nếu bạn mới với huấn luyện mạng nơ-ron và khái niệm gradient, giới thiệu ngắn gọn về các khái niệm này có thể tìm thấy trong phần A.4 trong phụ lục A. Tuy nhiên, hiểu biết toán học sâu về gradient không bắt buộc để theo dõi nội dung cuốn sách này.

Bây giờ hãy triển khai layer normalization để cải thiện sự ổn định và hiệu quả của huấn luyện mạng nơ-ron. Ý tưởng chính đằng sau layer normalization là điều chỉnh kích hoạt (activation) — đầu ra — của lớp mạng nơ-ron để có trung bình 0 và phương sai 1, còn gọi là phương sai đơn vị (unit variance). Sự điều chỉnh này tăng tốc hội tụ đến trọng số hiệu quả và đảm bảo huấn luyện nhất quán, đáng tin cậy. Trong GPT-2 và các kiến trúc transformer hiện đại, layer normalization thường được áp dụng trước và sau module multi-head attention, và, như chúng ta đã thấy với placeholder DummyLayerNorm, trước lớp đầu ra cuối cùng. Hình 4.5 cung cấp tổng quan trực quan về cách layer normalization hoạt động.

[Hình 4.5: Minh họa layer normalization nơi sáu đầu ra của lớp, còn gọi là kích hoạt, được chuẩn hóa sao cho chúng có trung bình 0 và phương sai 1.]

Chúng ta có thể tái tạo ví dụ hiển thị trong hình 4.5 qua code sau, nơi chúng ta triển khai lớp mạng nơ-ron với năm đầu vào và sáu đầu ra mà chúng ta áp dụng cho hai ví dụ đầu vào:

```python
torch.manual_seed(123)
batch_example = torch.randn(2, 5)    # Tạo hai ví dụ huấn luyện
                                      # với năm chiều (đặc trưng) mỗi cái
layer = nn.Sequential(nn.Linear(5, 6), nn.ReLU())
out = layer(batch_example)
print(out)
```

In ra tensor sau, nơi hàng đầu tiên liệt kê đầu ra lớp cho đầu vào đầu tiên và hàng thứ hai liệt kê đầu ra lớp cho hàng thứ hai:

```
tensor([[0.2260, 0.3470, 0.0000, 0.2216, 0.0000, 0.0000],
        [0.2133, 0.2394, 0.0000, 0.5198, 0.3297, 0.0000]],
       grad_fn=<ReluBackward0>)
```

Lớp mạng nơ-ron chúng ta đã viết code bao gồm lớp Linear theo sau bởi hàm kích hoạt phi tuyến, ReLU (viết tắt của rectified linear unit), là hàm kích hoạt tiêu chuẩn trong mạng nơ-ron. Nếu bạn không quen thuộc với ReLU, nó đơn giản đặt ngưỡng các đầu vào âm về 0, đảm bảo lớp chỉ xuất giá trị dương, giải thích tại sao đầu ra lớp kết quả không chứa giá trị âm nào. Sau đó, chúng ta sẽ sử dụng hàm kích hoạt phức tạp hơn trong GPT.

Trước khi áp dụng layer normalization cho các đầu ra này, hãy kiểm tra trung bình và phương sai:

```python
mean = out.mean(dim=-1, keepdim=True)
var = out.var(dim=-1, keepdim=True)
print("Mean:\n", mean)
print("Variance:\n", var)
```

Đầu ra là:

```
Mean:
  tensor([[0.1324],
          [0.2170]], grad_fn=<MeanBackward1>)
Variance:
  tensor([[0.0231],
          [0.0398]], grad_fn=<VarBackward0>)
```

Hàng đầu tiên trong tensor trung bình ở đây chứa giá trị trung bình cho hàng đầu vào đầu tiên, và hàng đầu ra thứ hai chứa trung bình cho hàng đầu vào thứ hai.

Sử dụng `keepdim=True` trong các phép toán như tính trung bình hoặc phương sai đảm bảo rằng tensor đầu ra giữ cùng số chiều với tensor đầu vào, mặc dù phép toán giảm tensor dọc theo chiều được chỉ định qua `dim`. Ví dụ, không có `keepdim=True`, tensor trung bình trả về sẽ là vector hai chiều [0.1324, 0.2170] thay vì ma trận 2 × 1 [[0.1324], [0.2170]].

Tham số `dim` chỉ định chiều mà tính toán thống kê (ở đây, trung bình hoặc phương sai) nên được thực hiện trong tensor. Như hình 4.6 giải thích, cho tensor hai chiều (như ma trận), sử dụng `dim=-1` cho các phép toán như tính trung bình hoặc phương sai giống với sử dụng `dim=1`. Điều này là vì -1 đề cập đến chiều cuối cùng của tensor, tương ứng với cột trong tensor hai chiều. Sau đó, khi thêm layer normalization vào mô hình GPT, tạo tensor ba chiều với shape [batch_size, num_tokens, embedding_size], chúng ta vẫn có thể sử dụng `dim=-1` cho chuẩn hóa qua chiều cuối cùng, tránh thay đổi từ `dim=1` sang `dim=2`.

[Hình 4.6: Minh họa tham số dim khi tính trung bình của tensor. Ví dụ, nếu chúng ta có tensor hai chiều (ma trận) với các chiều [hàng, cột], sử dụng dim=0 sẽ thực hiện phép toán qua hàng (theo chiều dọc), kết quả là đầu ra tổng hợp dữ liệu cho mỗi cột. Sử dụng dim=1 hoặc dim=-1 sẽ thực hiện phép toán qua cột (theo chiều ngang), kết quả là đầu ra tổng hợp dữ liệu cho mỗi hàng.]

Tiếp theo, hãy áp dụng layer normalization cho đầu ra lớp mà chúng ta nhận được trước đó. Phép toán bao gồm trừ trung bình và chia cho căn bậc hai của phương sai (còn gọi là độ lệch chuẩn):

```python
out_norm = (out - mean) / torch.sqrt(var)
mean = out_norm.mean(dim=-1, keepdim=True)
var = out_norm.var(dim=-1, keepdim=True)
print("Normalized layer outputs:\n", out_norm)
print("Mean:\n", mean)
print("Variance:\n", var)
```

Như chúng ta có thể thấy dựa trên kết quả, đầu ra lớp đã chuẩn hóa, giờ cũng chứa giá trị âm, có trung bình 0 và phương sai 1:

```
Normalized layer outputs:
 tensor([[ 0.6159,  1.4126, -0.8719,  0.5872, -0.8719, -0.8719],
        [-0.0189,  0.1121, -1.0876,  1.5173,  0.5647, -1.0876]],
       grad_fn=<DivBackward0>)
Mean:
 tensor([[-5.9605e-08],
        [1.9868e-08]], grad_fn=<MeanBackward1>)
Variance:
 tensor([[1.],
        [1.]], grad_fn=<VarBackward0>)
```

Lưu ý rằng giá trị –5.9605e-08 trong tensor đầu ra là ký hiệu khoa học cho –5.9605 × 10⁻⁸, là –0.000000059605 ở dạng thập phân. Giá trị này rất gần 0, nhưng không chính xác bằng 0 do lỗi số nhỏ có thể tích lũy vì độ chính xác hữu hạn mà máy tính biểu diễn số.

Để cải thiện khả năng đọc, chúng ta cũng có thể tắt ký hiệu khoa học khi in giá trị tensor bằng cách đặt sci_mode thành False:

```python
torch.set_printoptions(sci_mode=False)
print("Mean:\n", mean)
print("Variance:\n", var)
```

Đầu ra là:

```
Mean:
 tensor([[    0.0000],
        [    0.0000]], grad_fn=<MeanBackward1>)
Variance:
 tensor([[1.],
        [1.]], grad_fn=<VarBackward0>)
```

Cho đến nay, chúng ta đã viết code và áp dụng layer normalization trong quy trình từng bước. Bây giờ hãy đóng gói quy trình này trong module PyTorch mà chúng ta có thể sử dụng trong mô hình GPT sau.

**Listing 4.2: Lớp layer normalization**

```python
class LayerNorm(nn.Module):
    def __init__(self, emb_dim):
        super().__init__()
        self.eps = 1e-5
        self.scale = nn.Parameter(torch.ones(emb_dim))
        self.shift = nn.Parameter(torch.zeros(emb_dim))

    def forward(self, x):
        mean = x.mean(dim=-1, keepdim=True)
        var = x.var(dim=-1, keepdim=True, unbiased=False)
        norm_x = (x - mean) / torch.sqrt(var + self.eps)
        return self.scale * norm_x + self.shift
```

Triển khai cụ thể này của layer normalization hoạt động trên chiều cuối cùng của tensor đầu vào x, đại diện cho chiều nhúng (emb_dim). Biến eps là hằng số nhỏ (epsilon) được thêm vào phương sai để ngăn chia cho zero trong quá trình chuẩn hóa. scale và shift là hai tham số huấn luyện (cùng chiều với đầu vào) mà LLM tự động điều chỉnh trong quá trình huấn luyện nếu xác định rằng làm như vậy sẽ cải thiện hiệu suất mô hình trên tác vụ huấn luyện. Điều này cho phép mô hình học chia tỷ lệ và dịch chuyển phù hợp nhất với dữ liệu đang xử lý.

> **Phương sai thiên lệch**
>
> Trong phương pháp tính phương sai, chúng ta sử dụng chi tiết triển khai bằng cách đặt `unbiased=False`. Cho những ai tò mò điều này có nghĩa gì, trong tính toán phương sai, chúng ta chia cho số đầu vào n trong công thức phương sai. Phương pháp này không áp dụng hiệu chỉnh Bessel, thường sử dụng n – 1 thay vì n trong mẫu số để điều chỉnh thiên lệch trong ước lượng phương sai mẫu. Quyết định này dẫn đến cái gọi là ước lượng thiên lệch của phương sai. Cho LLM, nơi chiều nhúng n đủ lớn, sự khác biệt giữa sử dụng n và n – 1 là không đáng kể. Tôi chọn phương pháp này để đảm bảo tương thích với lớp chuẩn hóa của mô hình GPT-2 và vì nó phản ánh hành vi mặc định của TensorFlow, được sử dụng để triển khai mô hình GPT-2 gốc. Sử dụng cài đặt tương tự đảm bảo phương pháp của chúng ta tương thích với trọng số đã huấn luyện trước mà chúng ta sẽ nạp trong chương 6.

Bây giờ hãy thử module LayerNorm trong thực tế và áp dụng cho batch đầu vào:

```python
ln = LayerNorm(emb_dim=5)
out_ln = ln(batch_example)
mean = out_ln.mean(dim=-1, keepdim=True)
var = out_ln.var(dim=-1, unbiased=False, keepdim=True)
print("Mean:\n", mean)
print("Variance:\n", var)
```

Kết quả cho thấy code layer normalization hoạt động như mong đợi và chuẩn hóa giá trị của mỗi trong hai đầu vào sao cho chúng có trung bình 0 và phương sai 1:

```
Mean:
 tensor([[    -0.0000],
        [     0.0000]], grad_fn=<MeanBackward1>)
Variance:
 tensor([[1.0000],
        [1.0000]], grad_fn=<VarBackward0>)
```

> **Layer normalization so với batch normalization**
>
> Nếu bạn quen thuộc với batch normalization, phương pháp chuẩn hóa phổ biến và truyền thống cho mạng nơ-ron, bạn có thể tự hỏi nó so sánh thế nào với layer normalization. Không giống batch normalization chuẩn hóa qua chiều batch, layer normalization chuẩn hóa qua chiều đặc trưng. LLM thường yêu cầu tài nguyên tính toán đáng kể, và phần cứng có sẵn hoặc trường hợp sử dụng cụ thể có thể quyết định kích thước batch trong quá trình huấn luyện hoặc suy luận. Vì layer normalization chuẩn hóa mỗi đầu vào độc lập với kích thước batch, nó cung cấp linh hoạt và ổn định hơn trong các tình huống này. Điều này đặc biệt có lợi cho huấn luyện phân tán hoặc khi triển khai mô hình trong môi trường tài nguyên hạn chế.

Chúng ta đã hoàn thành hai trong số các khối xây dựng cần thiết để triển khai kiến trúc GPT, như hiển thị trong hình 4.7. Tiếp theo, chúng ta sẽ xem xét hàm kích hoạt GELU, là một trong những hàm kích hoạt được sử dụng trong LLM, thay vì hàm ReLU truyền thống mà chúng ta đã sử dụng trước đó.

[Hình 4.7: Các khối xây dựng cần thiết để xây dựng kiến trúc GPT. Cho đến nay, chúng ta đã hoàn thành khung GPT và layer normalization. Tiếp theo, chúng ta sẽ tập trung vào kích hoạt GELU và mạng feed forward.]

## 4.3 Triển khai mạng feed forward với kích hoạt GELU

Tiếp theo, chúng ta sẽ triển khai module mạng nơ-ron nhỏ được sử dụng như phần của khối transformer trong LLM. Chúng ta bắt đầu bằng cách triển khai hàm kích hoạt GELU, đóng vai trò quan trọng trong module mạng nơ-ron nhỏ này.

> **LƯU Ý:** Để biết thêm thông tin về triển khai mạng nơ-ron trong PyTorch, xem phần A.5 trong phụ lục A.

Trong lịch sử, hàm kích hoạt ReLU đã được sử dụng phổ biến trong deep learning do tính đơn giản và hiệu quả qua các kiến trúc mạng nơ-ron khác nhau. Tuy nhiên, trong LLM, nhiều hàm kích hoạt khác được sử dụng ngoài ReLU truyền thống. Hai ví dụ đáng chú ý là GELU (Gaussian error linear unit) và SwiGLU (Swish-gated linear unit).

GELU và SwiGLU là các hàm kích hoạt phức tạp và mượt mà hơn, kết hợp đơn vị Gaussian và đơn vị tuyến tính có cổng sigmoid, tương ứng. Chúng cung cấp hiệu suất được cải thiện cho mô hình deep learning, không giống ReLU đơn giản hơn.

Hàm kích hoạt GELU có thể được triển khai theo nhiều cách; phiên bản chính xác được định nghĩa là GELU(x) = x⋅Φ(x), nơi Φ(x) là hàm phân phối tích lũy của phân phối Gaussian chuẩn. Tuy nhiên, trong thực tế, thường triển khai xấp xỉ rẻ hơn về tính toán (mô hình GPT-2 gốc cũng được huấn luyện với xấp xỉ này, được tìm qua khớp đường cong):

**Listing 4.3: Triển khai hàm kích hoạt GELU**

```python
class GELU(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return 0.5 * x * (1 + torch.tanh(
            torch.sqrt(torch.tensor(2.0 / torch.pi)) *
            (x + 0.044715 * torch.pow(x, 3))
        ))
```

Tiếp theo, để có ý tưởng hàm GELU này trông như thế nào và so sánh với hàm ReLU, hãy vẽ biểu đồ hai hàm này cạnh nhau:

```python
import matplotlib.pyplot as plt

gelu, relu = GELU(), nn.ReLU()
x = torch.linspace(-3, 3, 100)    # Tạo 100 điểm dữ liệu mẫu trong khoảng -3 đến 3
y_gelu, y_relu = gelu(x), relu(x)
plt.figure(figsize=(8, 3))
for i, (y, label) in enumerate(zip([y_gelu, y_relu], ["GELU", "ReLU"]), 1):
    plt.subplot(1, 2, i)
    plt.plot(x, y)
    plt.title(f"{label} activation function")
    plt.xlabel("x")
    plt.ylabel(f"{label}(x)")
    plt.grid(True)
plt.tight_layout()
plt.show()
```

[Hình 4.8: Đầu ra đồ thị GELU và ReLU sử dụng matplotlib. Trục x hiển thị đầu vào hàm và trục y hiển thị đầu ra hàm.]

Như chúng ta có thể thấy trong đồ thị kết quả trong hình 4.8, ReLU (phải) là hàm tuyến tính từng phần xuất đầu vào trực tiếp nếu dương; ngược lại, xuất zero. GELU (trái) là hàm mượt, phi tuyến xấp xỉ ReLU nhưng với gradient khác zero cho hầu hết tất cả giá trị âm (ngoại trừ xấp xỉ tại x = –0.75).

Sự mượt mà của GELU có thể dẫn đến thuộc tính tối ưu hóa tốt hơn trong quá trình huấn luyện, vì nó cho phép điều chỉnh tinh tế hơn cho tham số mô hình. Ngược lại, ReLU có góc nhọn tại zero (hình 4.8, phải), đôi khi có thể gây khó khăn cho tối ưu hóa, đặc biệt trong mạng rất sâu hoặc có kiến trúc phức tạp. Hơn nữa, không giống ReLU xuất zero cho bất kỳ đầu vào âm nào, GELU cho phép đầu ra nhỏ, khác zero cho giá trị âm. Đặc tính này có nghĩa là trong quá trình huấn luyện, các nơ-ron nhận đầu vào âm vẫn có thể đóng góp cho quá trình học, mặc dù ở mức độ thấp hơn đầu vào dương.

Tiếp theo, hãy sử dụng hàm GELU để triển khai module mạng nơ-ron nhỏ, FeedForward, mà chúng ta sẽ sử dụng trong khối transformer của LLM sau.

**Listing 4.4: Module mạng nơ-ron feed forward**

```python
class FeedForward(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(cfg["emb_dim"], 4 * cfg["emb_dim"]),
            GELU(),
            nn.Linear(4 * cfg["emb_dim"], cfg["emb_dim"]),
        )

    def forward(self, x):
        return self.layers(x)
```

Như chúng ta có thể thấy, module FeedForward là mạng nơ-ron nhỏ gồm hai lớp Linear và hàm kích hoạt GELU. Trong mô hình GPT 124 triệu tham số, nó nhận batch đầu vào với token có kích thước nhúng 768 mỗi cái qua dictionary GPT_CONFIG_124M nơi GPT_CONFIG_124M["emb_dim"] = 768. Hình 4.9 cho thấy kích thước nhúng được thao tác như thế nào bên trong mạng nơ-ron feed forward nhỏ này khi chúng ta truyền đầu vào.

[Hình 4.9: Tổng quan về kết nối giữa các lớp của mạng nơ-ron feed forward. Mạng nơ-ron này có thể chứa kích thước batch và số token thay đổi trong đầu vào. Tuy nhiên, kích thước nhúng cho mỗi token được xác định và cố định khi khởi tạo trọng số.]

Theo ví dụ trong hình 4.9, hãy khởi tạo module FeedForward mới với kích thước nhúng token 768 và đưa đầu vào batch với hai mẫu và ba token mỗi cái:

```python
ffn = FeedForward(GPT_CONFIG_124M)
x = torch.rand(2, 3, 768)         # Tạo đầu vào mẫu với chiều batch 2
out = ffn(x)
print(out.shape)
```

Như chúng ta có thể thấy, shape của tensor đầu ra giống với tensor đầu vào:

```
torch.Size([2, 3, 768])
```

Module FeedForward đóng vai trò quan trọng trong việc nâng cao khả năng học từ và tổng quát hóa dữ liệu của mô hình. Mặc dù chiều đầu vào và đầu ra của module này giống nhau, nó mở rộng nội bộ chiều nhúng vào không gian chiều cao hơn qua lớp tuyến tính đầu tiên, như minh họa trong hình 4.10. Sự mở rộng này được theo sau bởi kích hoạt GELU phi tuyến rồi co lại về chiều gốc với phép biến đổi tuyến tính thứ hai. Thiết kế như vậy cho phép khám phá không gian biểu diễn phong phú hơn.

[Hình 4.10: Minh họa sự mở rộng và co lại đầu ra lớp trong mạng nơ-ron feed forward. Đầu tiên, đầu vào mở rộng bằng hệ số 4 từ 768 lên 3.072 giá trị. Sau đó, lớp thứ hai nén 3.072 giá trị trở lại biểu diễn 768 chiều.]

Hơn nữa, sự đồng nhất trong chiều đầu vào và đầu ra đơn giản hóa kiến trúc bằng cách cho phép xếp chồng nhiều lớp, như chúng ta sẽ làm sau, mà không cần điều chỉnh chiều giữa chúng, do đó làm cho mô hình dễ mở rộng hơn.

## 4.4 Thêm kết nối tắt

Hãy thảo luận khái niệm đằng sau kết nối tắt (shortcut connection), còn được gọi là kết nối bỏ qua (skip connection) hoặc kết nối dư (residual connection). Ban đầu, kết nối tắt được đề xuất cho mạng sâu trong thị giác máy tính (cụ thể, trong mạng dư — residual network) để giảm thiểu thách thức gradient biến mất. Vấn đề gradient biến mất đề cập đến vấn đề nơi gradient (hướng dẫn cập nhật trọng số trong quá trình huấn luyện) trở nên nhỏ dần khi chúng lan truyền ngược qua các lớp, gây khó khăn cho việc huấn luyện hiệu quả các lớp trước đó.

[Hình 4.12: So sánh mạng nơ-ron sâu gồm năm lớp không có (trái) và có kết nối tắt (phải). Kết nối tắt liên quan đến việc cộng đầu vào của lớp với đầu ra, hiệu quả tạo đường dẫn thay thế bỏ qua các lớp nhất định. Gradient biểu thị gradient trung bình tuyệt đối tại mỗi lớp, mà chúng ta tính toán trong listing 4.5.]

Hình 4.12 cho thấy kết nối tắt tạo đường dẫn thay thế, ngắn hơn cho gradient chảy qua mạng bằng cách bỏ qua một hoặc nhiều lớp, đạt được bằng cách cộng đầu ra của lớp này với đầu ra của lớp sau. Đây là lý do các kết nối này còn được gọi là kết nối bỏ qua. Chúng đóng vai trò quan trọng trong việc bảo toàn luồng gradient trong lượt truyền ngược khi huấn luyện.

**Listing 4.5: Mạng nơ-ron để minh họa kết nối tắt**

```python
class ExampleDeepNeuralNetwork(nn.Module):
    def __init__(self, layer_sizes, use_shortcut):
        super().__init__()
        self.use_shortcut = use_shortcut
        self.layers = nn.ModuleList([      # Triển khai năm lớp
            nn.Sequential(nn.Linear(layer_sizes[0], layer_sizes[1]),
                          GELU()),
            nn.Sequential(nn.Linear(layer_sizes[1], layer_sizes[2]),
                          GELU()),
            nn.Sequential(nn.Linear(layer_sizes[2], layer_sizes[3]),
                          GELU()),
            nn.Sequential(nn.Linear(layer_sizes[3], layer_sizes[4]),
                          GELU()),
            nn.Sequential(nn.Linear(layer_sizes[4], layer_sizes[5]),
                          GELU())
        ])

    def forward(self, x):
        for layer in self.layers:
            layer_output = layer(x)        # Tính đầu ra của lớp hiện tại
            if self.use_shortcut and x.shape == layer_output.shape:   # Kiểm tra
                x = x + layer_output       # có thể áp dụng shortcut không
            else:
                x = layer_output
        return x
```

Code triển khai mạng nơ-ron sâu với năm lớp, mỗi lớp gồm lớp Linear và hàm kích hoạt GELU. Trong lượt truyền xuôi, chúng ta lặp truyền đầu vào qua các lớp và tùy chọn thêm kết nối tắt nếu thuộc tính self.use_shortcut được đặt True.

Hãy sử dụng code này để khởi tạo mạng nơ-ron không có kết nối tắt. Mỗi lớp sẽ được khởi tạo sao cho nó nhận ví dụ với ba giá trị đầu vào và trả về ba giá trị đầu ra. Lớp cuối cùng trả về một giá trị đầu ra duy nhất:

```python
layer_sizes = [3, 3, 3, 3, 3, 1]
sample_input = torch.tensor([[1., 0., -1.]])
torch.manual_seed(123)                           # Chỉ định random seed cho trọng số
model_without_shortcut = ExampleDeepNeuralNetwork(  # khởi tạo cho tính tái tạo
    layer_sizes, use_shortcut=False
)
```

Tiếp theo, chúng ta triển khai hàm tính gradient trong lượt truyền ngược của mô hình:

```python
def print_gradients(model, x):
    output = model(x)            # Truyền xuôi
    target = torch.tensor([[0.]])
    loss = nn.MSELoss()
    loss = loss(output, target)   # Tính loss dựa trên mức gần
                                  # giữa target và output
    loss.backward()               # Truyền ngược để tính gradient

    for name, param in model.named_parameters():
        if 'weight' in name:
            print(f"{name} has gradient mean of "
                  f"{param.grad.abs().mean().item()}")
```

Code này chỉ định hàm mất mát tính toán mức gần giữa đầu ra mô hình và mục tiêu do người dùng chỉ định (ở đây, cho đơn giản, giá trị 0). Sau đó, khi gọi `loss.backward()`, PyTorch tính toán gradient mất mát cho mỗi lớp trong mô hình. Chúng ta có thể lặp qua tham số trọng số qua `model.named_parameters()`. Giả sử chúng ta có ma trận tham số trọng số 3 × 3 cho lớp cho trước. Trong trường hợp đó, lớp này sẽ có 3 × 3 giá trị gradient, và chúng ta in gradient trung bình tuyệt đối của 3 × 3 giá trị gradient này để có một giá trị gradient đơn cho mỗi lớp nhằm so sánh gradient giữa các lớp dễ dàng hơn.

Nói ngắn gọn, phương thức `.backward()` là phương thức tiện lợi trong PyTorch tính toán gradient mất mát, cần thiết trong huấn luyện mô hình, mà không cần triển khai toán học cho tính toán gradient, do đó làm cho làm việc với mạng nơ-ron sâu dễ tiếp cận hơn nhiều.

> **LƯU Ý:** Nếu bạn không quen thuộc với khái niệm gradient và huấn luyện mạng nơ-ron, tôi khuyến nghị đọc phần A.4 và A.7 trong phụ lục A.

Bây giờ hãy sử dụng hàm print_gradients và áp dụng cho mô hình không có kết nối bỏ qua:

```python
print_gradients(model_without_shortcut, sample_input)
```

Đầu ra là:

```
layers.0.0.weight has gradient mean of 0.00020173587836325169
layers.1.0.weight has gradient mean of 0.0001201116101583466
layers.2.0.weight has gradient mean of 0.0007152041653171182
layers.3.0.weight has gradient mean of 0.001398873864673078
layers.4.0.weight has gradient mean of 0.005049646366387606
```

Đầu ra của hàm print_gradients cho thấy, gradient trở nên nhỏ hơn khi chúng ta tiến từ lớp cuối (layers.4) đến lớp đầu (layers.0), là hiện tượng gọi là vấn đề gradient biến mất.

Bây giờ hãy khởi tạo mô hình với kết nối bỏ qua và xem so sánh thế nào:

```python
torch.manual_seed(123)
model_with_shortcut = ExampleDeepNeuralNetwork(
    layer_sizes, use_shortcut=True
)
print_gradients(model_with_shortcut, sample_input)
```

Đầu ra là:

```
layers.0.0.weight has gradient mean of 0.22169792652130127
layers.1.0.weight has gradient mean of 0.20694105327129364
layers.2.0.weight has gradient mean of 0.32896995544433594
layers.3.0.weight has gradient mean of 0.2665732502937317
layers.4.0.weight has gradient mean of 1.3258541822433472
```

Lớp cuối (layers.4) vẫn có gradient lớn hơn các lớp khác. Tuy nhiên, giá trị gradient ổn định khi chúng ta tiến về lớp đầu (layers.0) và không co lại xuống giá trị nhỏ biến mất.

Tóm lại, kết nối tắt rất quan trọng để vượt qua các hạn chế do vấn đề gradient biến mất gây ra trong mạng sâu. Kết nối tắt rất quan trọng cho huấn luyện mô hình sâu hơn hiệu quả, và chúng ta sẽ sử dụng chúng trong kiến trúc GPT mà chúng ta sẽ triển khai trong phần tiếp theo khi kết hợp tất cả khái niệm trong khối transformer.

## 4.5 Kết nối các lớp attention và tuyến tính trong khối transformer

Bây giờ, hãy triển khai khối transformer, khối xây dựng cơ bản của GPT và các kiến trúc LLM khác. Khối này, được lặp lại hàng chục lần trong kiến trúc GPT-2 124 triệu tham số, kết hợp một số khái niệm chúng ta đã đề cập trước đó: multi-head attention, layer normalization, dropout, feed forward layers, và kích hoạt GELU. Sau đó, chúng ta sẽ kết nối khối transformer này với các phần còn lại của kiến trúc GPT.

Hình 4.13 cho thấy khối transformer kết hợp một số thành phần, bao gồm module masked multi-head attention (xem chương 3) và module FeedForward chúng ta đã triển khai trước đó (xem phần 4.3). Khi khối transformer xử lý chuỗi đầu vào, mỗi phần tử trong chuỗi (ví dụ, một từ hoặc token phụ) được đại diện bởi vector kích thước cố định (trong trường hợp này, 768 chiều). Các phép toán bên trong khối transformer, bao gồm multi-head attention và các lớp feed forward, được thiết kế để biến đổi các vector này theo cách bảo toàn số chiều của chúng.

Ý tưởng là cơ chế self-attention trong khối multi-head attention xác định và phân tích mối quan hệ giữa các phần tử trong chuỗi đầu vào. Ngược lại, mạng feed forward sửa đổi dữ liệu riêng lẻ tại mỗi vị trí. Sự kết hợp này không chỉ cho phép hiểu và xử lý chi tiết hơn về đầu vào mà còn nâng cao khả năng tổng thể của mô hình trong việc xử lý các mẫu dữ liệu phức tạp.

[Hình 4.13: Minh họa khối transformer. Các token đầu vào đã được nhúng thành vector 768 chiều. Mỗi hàng tương ứng với biểu diễn vector của một token. Đầu ra của khối transformer là các vector cùng chiều với đầu vào, sau đó có thể được đưa vào các lớp tiếp theo trong LLM.]

Chúng ta có thể tạo TransformerBlock trong code.

**Listing 4.6: Thành phần khối transformer của GPT**

```python
from chapter03 import MultiHeadAttention

class TransformerBlock(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.att = MultiHeadAttention(
            d_in=cfg["emb_dim"],
            d_out=cfg["emb_dim"],
            context_length=cfg["context_length"],
            num_heads=cfg["n_heads"], 
            dropout=cfg["drop_rate"],
            qkv_bias=cfg["qkv_bias"])
        self.ff = FeedForward(cfg)
        self.norm1 = LayerNorm(cfg["emb_dim"])
        self.norm2 = LayerNorm(cfg["emb_dim"])
        self.drop_shortcut = nn.Dropout(cfg["drop_rate"])

    def forward(self, x):
        # Kết nối tắt cho khối attention
        shortcut = x
        x = self.norm1(x)
        x = self.att(x)
        x = self.drop_shortcut(x)
        x = x + shortcut     # Cộng lại đầu vào gốc

        # Kết nối tắt cho khối feed forward
        shortcut = x
        x = self.norm2(x)
        x = self.ff(x)
        x = self.drop_shortcut(x)
        x = x + shortcut     # Cộng lại đầu vào gốc
        return x
```

Code được cung cấp định nghĩa lớp TransformerBlock trong PyTorch bao gồm cơ chế multi-head attention (MultiHeadAttention) và mạng feed forward (FeedForward), cả hai được cấu hình dựa trên dictionary cấu hình được cung cấp (cfg), chẳng hạn như GPT_CONFIG_124M.

Layer normalization (LayerNorm) được áp dụng trước mỗi thành phần này, và dropout được áp dụng sau chúng để điều chuẩn mô hình và ngăn overfitting. Điều này còn được gọi là Pre-LayerNorm. Các kiến trúc cũ hơn, chẳng hạn như mô hình transformer gốc, thay vào đó áp dụng layer normalization sau self-attention và mạng feed forward, được gọi là Post-LayerNorm, điều thường dẫn đến động lực huấn luyện kém hơn.

Lớp này cũng triển khai lượt truyền xuôi, nơi mỗi thành phần được theo sau bởi kết nối tắt cộng đầu vào của khối với đầu ra. Tính năng quan trọng này giúp gradient chảy qua mạng trong quá trình huấn luyện và cải thiện việc học của các mô hình sâu (xem phần 4.4).

Sử dụng dictionary GPT_CONFIG_124M mà chúng ta đã định nghĩa trước đó, hãy khởi tạo khối transformer và truyền cho nó một số dữ liệu mẫu:

```python
torch.manual_seed(123)
x = torch.rand(2, 4, 768)     # Tạo đầu vào mẫu với shape 
                               # [batch_size, num_tokens, emb_dim]
block = TransformerBlock(GPT_CONFIG_124M)
output = block(x)

print("Input shape:", x.shape)
print("Output shape:", output.shape)
```

Đầu ra là:

```
Input shape: torch.Size([2, 4, 768])
Output shape: torch.Size([2, 4, 768])
```

Như chúng ta có thể thấy, khối transformer duy trì chiều đầu vào trong đầu ra của nó, chỉ ra rằng kiến trúc transformer xử lý các chuỗi dữ liệu mà không làm thay đổi shape của chúng trong suốt mạng.

Việc bảo toàn shape trong suốt kiến trúc khối transformer không phải ngẫu nhiên mà là một khía cạnh quan trọng của thiết kế. Thiết kế này cho phép ứng dụng hiệu quả qua nhiều tác vụ sequence-to-sequence, nơi mỗi vector đầu ra tương ứng trực tiếp với vector đầu vào, duy trì mối quan hệ một-một. Tuy nhiên, đầu ra là vector ngữ cảnh gói gọn thông tin từ toàn bộ chuỗi đầu vào (xem chương 3). Điều này có nghĩa là trong khi các chiều vật lý của chuỗi (chiều dài và kích thước đặc trưng) không thay đổi khi đi qua khối transformer, nội dung của mỗi vector đầu ra được mã hóa lại để tích hợp thông tin ngữ cảnh từ toàn bộ chuỗi đầu vào.

Với khối transformer được triển khai, giờ chúng ta đã có tất cả các khối xây dựng cần thiết để triển khai kiến trúc GPT. Như minh họa trong hình 4.14, khối transformer kết hợp layer normalization, mạng feed forward, kích hoạt GELU, và kết nối tắt. Như cuối cùng chúng ta sẽ thấy, khối transformer này sẽ tạo nên thành phần chính của kiến trúc GPT.

[Hình 4.14: Các khối xây dựng cần thiết để xây dựng kiến trúc GPT. Các dấu check đen chỉ các khối chúng ta đã hoàn thành.]

## 4.6 Viết code mô hình GPT

Chúng ta đã bắt đầu chương này với tổng quan từ trên xuống của kiến trúc GPT mà chúng ta gọi là DummyGPTModel. Trong triển khai code DummyGPTModel này, chúng ta đã hiển thị đầu vào và đầu ra cho mô hình GPT, nhưng các khối xây dựng của nó vẫn là hộp đen sử dụng lớp DummyTransformerBlock và DummyLayerNorm làm placeholder.

Bây giờ hãy thay thế placeholder DummyTransformerBlock và DummyLayerNorm bằng các lớp TransformerBlock và LayerNorm thực mà chúng ta đã viết code trước đó để lắp ráp phiên bản hoạt động đầy đủ của phiên bản GPT-2 124 triệu tham số gốc. Trong chương 5, chúng ta sẽ huấn luyện trước mô hình GPT-2, và trong chương 6, chúng ta sẽ nạp trọng số đã huấn luyện trước từ OpenAI.

Trước khi chúng ta lắp ráp mô hình GPT-2 trong code, hãy xem cấu trúc tổng thể của nó, như hiển thị trong hình 4.15, bao gồm tất cả các khái niệm chúng ta đã đề cập cho đến nay. Như chúng ta có thể thấy, khối transformer được lặp lại nhiều lần trong suốt kiến trúc mô hình GPT. Trong trường hợp mô hình GPT-2 124 triệu tham số, nó được lặp lại 12 lần, điều mà chúng ta chỉ định qua mục n_layers trong dictionary GPT_CONFIG_124M. Khối transformer này được lặp lại 48 lần trong mô hình GPT-2 lớn nhất với 1.542 triệu tham số.

Đầu ra từ khối transformer cuối cùng sau đó đi qua bước chuẩn hóa lớp cuối cùng trước khi đến lớp đầu ra tuyến tính. Lớp này ánh xạ đầu ra của transformer vào không gian chiều cao (trong trường hợp này, 50.257 chiều, tương ứng với kích thước từ vựng của mô hình) để dự đoán token tiếp theo trong chuỗi.

Bây giờ hãy viết code kiến trúc trong hình 4.15.

[Hình 4.15: Tổng quan về kiến trúc mô hình GPT cho thấy luồng dữ liệu qua mô hình GPT. Bắt đầu từ dưới cùng, văn bản đã token hóa trước tiên được chuyển thành nhúng token, sau đó được bổ sung bằng nhúng vị trí. Thông tin kết hợp này tạo thành tensor được truyền qua chuỗi khối transformer hiển thị ở giữa (mỗi khối chứa multi-head attention và các lớp mạng nơ-ron feed forward với dropout và layer normalization), được xếp chồng lên nhau và lặp lại 12 lần.]

**Listing 4.7: Triển khai kiến trúc mô hình GPT**

```python
class GPTModel(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.tok_emb = nn.Embedding(cfg["vocab_size"], cfg["emb_dim"])
        self.pos_emb = nn.Embedding(cfg["context_length"], cfg["emb_dim"])
        self.drop_emb = nn.Dropout(cfg["drop_rate"])
        
        self.trf_blocks = nn.Sequential(
            *[TransformerBlock(cfg) for _ in range(cfg["n_layers"])])
        
        self.final_norm = LayerNorm(cfg["emb_dim"])
        self.out_head = nn.Linear(
            cfg["emb_dim"], cfg["vocab_size"], bias=False
        )

    def forward(self, in_idx):
        batch_size, seq_len = in_idx.shape
        tok_embeds = self.tok_emb(in_idx)

        # Cài đặt device sẽ cho phép chúng ta huấn luyện
        # mô hình trên CPU hoặc GPU, tùy thuộc vào 
        # thiết bị mà dữ liệu đầu vào đang ở. 
        pos_embeds = self.pos_emb(
            torch.arange(seq_len, device=in_idx.device)
        )
        x = tok_embeds + pos_embeds
        x = self.drop_emb(x)
        x = self.trf_blocks(x)
        x = self.final_norm(x)
        logits = self.out_head(x)
        return logits
```

Nhờ lớp TransformerBlock, lớp GPTModel tương đối nhỏ và gọn.

Hàm khởi tạo `__init__` của lớp GPTModel này khởi tạo các lớp nhúng token và vị trí sử dụng cấu hình được truyền qua dictionary Python, cfg. Các lớp nhúng này chịu trách nhiệm chuyển đổi chỉ mục token đầu vào thành vector dày đặc và thêm thông tin vị trí (xem chương 2).

Tiếp theo, phương thức `__init__` tạo chuỗi ngăn xếp các module TransformerBlock bằng với số lớp được chỉ định trong cfg. Tiếp theo các khối transformer, lớp LayerNorm được áp dụng, chuẩn hóa đầu ra từ các khối transformer để ổn định quá trình học. Cuối cùng, một đầu ra tuyến tính (out_head) không có bias được định nghĩa, chiếu đầu ra của transformer vào không gian từ vựng của tokenizer để sinh ra các logit cho mỗi token trong từ vựng.

Phương thức forward nhận batch các chỉ mục token đầu vào, tính toán nhúng của chúng, áp dụng nhúng vị trí, truyền chuỗi qua các khối transformer, chuẩn hóa đầu ra cuối cùng, và sau đó tính toán logit, đại diện cho xác suất chưa chuẩn hóa của token tiếp theo. Chúng ta sẽ chuyển đổi các logit này thành token và văn bản đầu ra trong phần tiếp theo.

Bây giờ hãy khởi tạo mô hình GPT 124 triệu tham số sử dụng dictionary GPT_CONFIG_124M chúng ta truyền vào tham số cfg và cung cấp cho nó batch văn bản đầu vào chúng ta đã tạo trước đó:

```python
torch.manual_seed(123)
model = GPTModel(GPT_CONFIG_124M)
out = model(batch)

print("Input batch:\n", batch)
print("\nOutput shape:", out.shape)
print(out)
```

Code này in nội dung của batch đầu vào theo sau là tensor đầu ra:

```
Input batch:
 tensor([[6109,  3626,  6100,   345],     # Token IDs của văn bản 1
         [6109,  1110,  6622,   257]])    # Token IDs của văn bản 2

Output shape: torch.Size([2, 4, 50257])
tensor([[[ 0.3613,  0.4222, -0.0711,  ...,  0.3483,  0.4661, -0.2838],
         [-0.1792, -0.5660, -0.9485,  ...,  0.0477,  0.5181, -0.3168],
         [ 0.7120,  0.0332,  0.1085,  ...,  0.1018, -0.4327, -0.2553],
         [-1.0076,  0.3418, -0.1190,  ...,  0.7195,  0.4023,  0.0532]],

        [[-0.2564,  0.0900,  0.0335,  ...,  0.2659,  0.4454, -0.6806],
         [ 0.1230,  0.3653, -0.2074,  ...,  0.7705,  0.2710,  0.2246],
         [ 1.0558,  1.0318, -0.2800,  ...,  0.6936,  0.3205, -0.3178],
         [-0.1565,  0.3926,  0.3288,  ...,  1.2630, -0.1858,  0.0388]]],
       grad_fn=<UnsafeViewBackward0>)
```

Như chúng ta có thể thấy, tensor đầu ra có shape [2, 4, 50257], vì chúng ta đã truyền vào hai văn bản đầu vào với bốn token mỗi văn bản. Chiều cuối cùng, 50257, tương ứng với kích thước từ vựng của tokenizer. Sau đó, chúng ta sẽ xem cách chuyển đổi từng vector đầu ra 50.257 chiều này trở lại thành token.

Trước khi chuyển sang viết code hàm chuyển đổi đầu ra mô hình thành văn bản, hãy dành một chút thời gian với chính kiến trúc mô hình và phân tích kích thước của nó. Sử dụng phương thức `numel()`, viết tắt của "number of elements" (số phần tử), chúng ta có thể thu thập tổng số tham số trong các tensor tham số của mô hình:

```python
total_params = sum(p.numel() for p in model.parameters())
print(f"Total number of parameters: {total_params:,}")
```

Kết quả là:

```
Total number of parameters: 163,009,536
```

Bây giờ, một độc giả tò mò có thể nhận thấy sự khác biệt. Trước đó, chúng ta nói về việc khởi tạo mô hình GPT 124 triệu tham số, vậy tại sao số lượng tham số thực tế lại là 163 triệu?

Lý do là một khái niệm gọi là weight tying (ràng buộc trọng số), được sử dụng trong kiến trúc GPT-2 gốc. Điều này có nghĩa là kiến trúc GPT-2 gốc tái sử dụng trọng số từ lớp nhúng token trong lớp đầu ra của nó. Để hiểu rõ hơn, hãy xem xét shape của lớp nhúng token và lớp đầu ra tuyến tính mà chúng ta đã khởi tạo trên mô hình qua GPTModel trước đó:

```python
print("Token embedding layer shape:", model.tok_emb.weight.shape)
print("Output layer shape:", model.out_head.weight.shape)
```

Như chúng ta có thể thấy từ các đầu ra in, tensor trọng số cho cả hai lớp này có cùng shape:

```
Token embedding layer shape: torch.Size([50257, 768])
Output layer shape: torch.Size([50257, 768])
```

Lớp nhúng token và lớp đầu ra rất lớn do số lượng hàng 50.257 trong từ vựng của tokenizer. Hãy loại bỏ số lượng tham số lớp đầu ra khỏi tổng số mô hình GPT-2 theo khái niệm weight tying:

```python
total_params_gpt2 = (
    total_params - sum(p.numel() for p in model.out_head.parameters())
)
print(f"Number of trainable parameters "
      f"considering weight tying: {total_params_gpt2:,}"
)
```

Đầu ra là:

```
Number of trainable parameters considering weight tying: 124,412,160
```

Như chúng ta có thể thấy, mô hình giờ chỉ còn 124 triệu tham số, khớp với kích thước gốc của mô hình GPT-2.

Weight tying giảm tổng lượng bộ nhớ và độ phức tạp tính toán của mô hình. Tuy nhiên, theo kinh nghiệm của tôi, sử dụng lớp nhúng token và lớp đầu ra riêng biệt dẫn đến huấn luyện và hiệu suất mô hình tốt hơn; do đó, chúng ta sử dụng các lớp riêng biệt trong triển khai GPTModel của mình. Điều tương tự cũng đúng với các LLM hiện đại. Tuy nhiên, chúng ta sẽ xem lại và triển khai khái niệm weight tying sau trong chương 6 khi chúng ta nạp trọng số đã huấn luyện trước từ OpenAI.

> **Bài tập 4.1: Số lượng tham số trong feed forward và attention module**
>
> Tính toán và so sánh số lượng tham số có trong module feed forward và các tham số có trong module multi-head attention.

Cuối cùng, hãy tính toán yêu cầu bộ nhớ của 163 triệu tham số trong đối tượng GPTModel của chúng ta:

```python
total_size_bytes = total_params * 4      # Tính tổng kích thước theo byte (giả sử
                                          # float32, 4 byte cho mỗi tham số)
total_size_mb = total_size_bytes / (1024 * 1024)    # Chuyển đổi sang megabyte
print(f"Total size of the model: {total_size_mb:.2f} MB")
```

Kết quả là:

```
Total size of the model: 621.83 MB
```

Tóm lại, bằng cách tính toán yêu cầu bộ nhớ cho 163 triệu tham số trong đối tượng GPTModel của chúng ta và giả định mỗi tham số là số float 32-bit chiếm 4 byte, chúng ta thấy rằng tổng kích thước của mô hình lên tới 621.83 MB, minh họa dung lượng lưu trữ tương đối lớn cần thiết để chứa ngay cả các LLM tương đối nhỏ.

Bây giờ chúng ta đã triển khai kiến trúc GPTModel và thấy rằng nó xuất ra các tensor số có shape `[batch_size, num_tokens, vocab_size]`, hãy viết code để chuyển đổi các tensor đầu ra này thành văn bản.

> **Bài tập 4.2: Khởi tạo các mô hình GPT lớn hơn**
>
> Chúng ta đã khởi tạo mô hình GPT 124 triệu tham số, được gọi là "GPT-2 small". Không thực hiện bất kỳ sửa đổi code nào ngoài việc cập nhật tệp cấu hình, hãy sử dụng lớp GPTModel để triển khai GPT-2 medium (sử dụng nhúng 1.024 chiều, 24 khối transformer, 16 head multi-head attention), GPT-2 large (nhúng 1.280 chiều, 36 khối transformer, 20 head multi-head attention), và GPT-2 XL (nhúng 1.600 chiều, 48 khối transformer, 25 head multi-head attention). Như một phần thưởng, hãy tính tổng số tham số trong mỗi mô hình GPT.

## 4.7 Sinh văn bản

Bây giờ chúng ta sẽ triển khai code chuyển đổi các đầu ra tensor của mô hình GPT trở lại thành văn bản. Trước khi bắt đầu, hãy xem xét ngắn gọn cách một mô hình tạo sinh (generative model) như LLM sinh văn bản từng từ (hoặc token) một.

Hình 4.16 minh họa quá trình từng bước trong đó mô hình GPT sinh văn bản khi có ngữ cảnh đầu vào, chẳng hạn như "Hello, I am". Với mỗi lần lặp, ngữ cảnh đầu vào tăng lên, cho phép mô hình sinh văn bản mạch lạc và phù hợp với ngữ cảnh. Đến lần lặp thứ sáu, mô hình đã xây dựng một câu hoàn chỉnh: "Hello, I am a model ready to help". Chúng ta đã thấy rằng triển khai GPTModel hiện tại của chúng ta xuất ra các tensor với shape `[batch_size, num_token, vocab_size]`. Bây giờ câu hỏi là: Làm thế nào mô hình GPT đi từ các tensor đầu ra này đến văn bản được sinh ra?

Quá trình mô hình GPT đi từ tensor đầu ra đến văn bản được sinh ra bao gồm một số bước, như minh họa trong hình 4.17. Các bước này bao gồm giải mã tensor đầu ra, chọn token dựa trên phân phối xác suất, và chuyển đổi các token này thành văn bản con người có thể đọc được.

[Hình 4.16: Quá trình từng bước qua đó LLM sinh văn bản, mỗi lần một token. Bắt đầu với ngữ cảnh đầu vào ban đầu ("Hello, I am"), mô hình dự đoán token tiếp theo trong mỗi lần lặp, nối nó vào ngữ cảnh đầu vào cho vòng dự đoán tiếp theo. Như đã thấy, lần lặp thứ nhất thêm "a", thứ hai "model", và thứ ba "ready", xây dựng câu dần dần.]

Quá trình sinh token tiếp theo được trình bày chi tiết trong hình 4.17 minh họa một bước đơn lẻ trong đó mô hình GPT sinh token tiếp theo dựa trên đầu vào của nó. Trong mỗi bước, mô hình xuất một ma trận với các vector đại diện cho các token tiếp theo tiềm năng. Vector tương ứng với token tiếp theo được trích xuất và chuyển đổi thành phân phối xác suất thông qua hàm softmax. Trong vector chứa các điểm xác suất kết quả, vị trí của chỉ mục có giá trị cao nhất được định vị, và chuyển thành ID token. ID token này sau đó được giải mã trở lại thành văn bản, tạo ra token tiếp theo trong chuỗi. Cuối cùng, token này được nối vào các đầu vào trước đó, tạo thành chuỗi đầu vào mới cho lần lặp tiếp theo. Quá trình từng bước này cho phép mô hình sinh văn bản tuần tự, xây dựng các cụm từ và câu mạch lạc từ ngữ cảnh đầu vào ban đầu.

[Hình 4.17: Cơ chế sinh văn bản trong mô hình GPT bằng cách hiển thị một lần lặp duy nhất trong quy trình sinh token. Quá trình bắt đầu bằng việc mã hóa văn bản đầu vào thành các ID token, sau đó được cung cấp cho mô hình GPT. Các đầu ra của mô hình sau đó được chuyển đổi lại thành văn bản và được thêm vào văn bản đầu vào ban đầu.]

Trong thực tế, chúng ta lặp lại quá trình này qua nhiều lần lặp, như hiển thị trong hình 4.16, cho đến khi chúng ta đạt được số lượng token sinh ra do người dùng chỉ định. Trong code, chúng ta có thể triển khai quy trình sinh token như được hiển thị trong listing sau.

**Listing 4.8: Hàm cho mô hình GPT để sinh văn bản**

```python
def generate_text_simple(model, idx,                
                         max_new_tokens, context_size): 
    # idx là mảng index có shape (batch, n_tokens)
    # trong ngữ cảnh hiện tại.
    for _ in range(max_new_tokens):
        # Cắt xén ngữ cảnh hiện tại nếu nó vượt quá 
        # kích thước ngữ cảnh được hỗ trợ. Ví dụ, nếu LLM chỉ 
        # hỗ trợ 5 token, và ngữ cảnh là 10, thì chỉ 
        # 5 token cuối được sử dụng làm ngữ cảnh.
        idx_cond = idx[:, -context_size:]   

        with torch.no_grad():
            logits = model(idx_cond)
       
        # Chỉ lấy bước thời gian cuối cùng, 
        # sao cho shape (batch, n_token, vocab_size) 
        # trở thành (batch, vocab_size)
        logits = logits[:, -1, :]                   
        
        # probas có shape (batch, vocab_size).
        probas = torch.softmax(logits, dim=-1)          
        
        # idx_next có shape (batch, 1).
        idx_next = torch.argmax(probas, dim=-1, keepdim=True)   

        # Nối sample index vào chuỗi đang chạy, nơi 
        # idx có shape (batch, n_tokens+1)
        idx = torch.cat((idx, idx_next), dim=1)    
    return idx
```

Code này trình bày một triển khai đơn giản của vòng lặp sinh tự động (generative loop) cho mô hình ngôn ngữ bằng PyTorch. Nó lặp cho số lượng token mới được chỉ định để tạo, cắt xén ngữ cảnh hiện tại cho vừa với kích thước ngữ cảnh tối đa của mô hình, tính toán dự đoán, và sau đó chọn token tiếp theo dựa trên dự đoán xác suất cao nhất.

Để viết code hàm `generate_text_simple`, chúng ta sử dụng hàm softmax để chuyển đổi các logit thành phân phối xác suất từ đó chúng ta xác định vị trí có giá trị cao nhất qua `torch.argmax`. Hàm softmax là hàm đơn điệu, nghĩa là nó bảo toàn thứ tự đầu vào khi chuyển thành đầu ra. Vì vậy, trong thực tế, bước softmax là dư thừa vì vị trí có điểm cao nhất trong tensor đầu ra softmax chính là vị trí đó trong tensor logit. Nói cách khác, chúng ta có thể áp dụng trực tiếp hàm `torch.argmax` vào tensor logit và nhận được kết quả tương tự. Tuy nhiên, tôi cung cấp code cho quá trình chuyển đổi để minh họa đầy đủ quy trình chuyển logit thành xác suất, điều này có thể giúp hiểu trực quan hơn để mô hình sinh ra token tiếp theo có khả năng cao nhất, quá trình này được gọi là giải mã tham lam (greedy decoding).

Khi chúng ta triển khai code huấn luyện GPT trong chương tiếp theo, chúng ta sẽ sử dụng các kỹ thuật lấy mẫu bổ sung để sửa đổi đầu ra softmax sao cho mô hình không phải lúc nào cũng chọn token có khả năng xảy ra cao nhất. Điều này tạo ra sự đa dạng và sáng tạo trong văn bản được tạo ra.

Quá trình sinh từng ID token một và nối nó vào ngữ cảnh bằng cách sử dụng hàm `generate_text_simple` được minh họa chi tiết hơn trong hình 4.18. (Quy trình sinh ID token cho mỗi lần lặp được trình bày chi tiết trong hình 4.17). Chúng ta sinh các ID token theo cách lặp đi lặp lại. Ví dụ, trong lần lặp 1, mô hình được cung cấp các token tương ứng với "Hello, I am", dự đoán token tiếp theo (với ID 257, tương ứng với "a") và nối nó vào đầu vào. Quá trình này được lặp lại cho đến khi mô hình tạo ra câu hoàn chỉnh "Hello, I am a model ready to help" sau sáu lần lặp.

[Hình 4.18: Sáu lần lặp của chu trình dự đoán token, trong đó mô hình nhận chuỗi ID token ban đầu làm đầu vào, dự đoán token tiếp theo, và thêm token này vào chuỗi đầu vào cho lần lặp kế tiếp. (Các ID token cũng được dịch thành văn bản tương ứng để dễ hiểu hơn.)]

Bây giờ, hãy dùng thử hàm `generate_text_simple` với ngữ cảnh đầu vào "Hello, I am". Trước tiên, chúng ta mã hóa ngữ cảnh đầu vào thành ID token:

```python
start_context = "Hello, I am"
encoded = tokenizer.encode(start_context)
print("encoded:", encoded)

encoded_tensor = torch.tensor(encoded).unsqueeze(0)  # Thêm chiều batch
print("encoded_tensor.shape:", encoded_tensor.shape)
```

Các ID được mã hóa là:

```
encoded: [15496, 11, 314, 716]
encoded_tensor.shape: torch.Size([1, 4])
```

Tiếp theo, chúng ta đặt mô hình vào chế độ `.eval()`. Chế độ này vô hiệu hóa các thành phần ngẫu nhiên như dropout (vốn chỉ được dùng trong quá trình huấn luyện) và sử dụng hàm `generate_text_simple` trên tensor đầu vào đã mã hóa:

```python
model.eval()   # Vô hiệu hóa dropout vì chúng ta 
                # không đang huấn luyện mô hình
out = generate_text_simple(
    model=model,
    idx=encoded_tensor, 
    max_new_tokens=6, 
    context_size=GPT_CONFIG_124M["context_length"]
)

print("Output:", out)
print("Output length:", len(out[0]))
```

ID token đầu ra kết quả là:

```
Output: tensor([[15496,    11,   314,   716, 27018, 24086, 47843,
30961, 42348,  7267]])
Output length: 10
```

Sử dụng phương thức `.decode` của tokenizer, chúng ta có thể chuyển các ID này trở lại thành văn bản:

```python
decoded_text = tokenizer.decode(out.squeeze(0).tolist())
print(decoded_text)
```

Đầu ra mô hình định dạng văn bản là:

```
Hello, I am Featureiman Byeswickattribute argue
```

Như chúng ta thấy, mô hình sinh ra một mớ vô nghĩa, không hề giống đoạn văn bản hoàn chỉnh "Hello, I am a model ready to help." Điều gì đã xảy ra? Lý do khiến mô hình không thể tạo ra văn bản mạch lạc là do chúng ta chưa huấn luyện nó. Từ trước tới giờ, chúng ta mới chỉ triển khai kiến trúc GPT và khởi tạo một mô hình GPT bằng các trọng số ngẫu nhiên ban đầu. Huấn luyện mô hình tự nó là một chủ đề lớn và chúng ta sẽ giải quyết trong chương tiếp theo.

## Tóm tắt

- Layer normalization (chuẩn hóa lớp) làm ổn định quá trình huấn luyện bằng cách đảm bảo rằng các đầu ra của mỗi lớp có trung bình và phương sai nhất quán.
- Shortcut connections (kết nối tắt) là những kết nối bỏ qua một hoặc nhiều lớp bằng cách cấp đầu ra của lớp trước trực tiếp vào lớp sâu hơn, giúp giảm thiểu vấn đề vanishing gradient (gradient biến mất) khi huấn luyện các mạng thần kinh sâu, như LLM.
- Khối transformer là cấu trúc cốt lõi của các mô hình GPT, kết hợp module masked multi-head attention với mạng feed forward được kết nối đầy đủ (fully connected) sử dụng hàm kích hoạt GELU.
- Các mô hình GPT là LLM với nhiều khối transformer được lặp lại, chứa hàng triệu đến hàng tỷ tham số.
- Các mô hình GPT có nhiều kích cỡ khác nhau, ví dụ: 124, 345, 762 và 1.542 triệu tham số, và ta có thể triển khai chúng với cùng một lớp Python là `GPTModel`.
- Khả năng sinh văn bản của một LLM kiểu GPT bao gồm việc giải mã các tensor đầu ra thành văn bản con người đọc được bằng cách dự đoán tuần tự từng token dựa trên một ngữ cảnh đầu vào có sẵn.
- Nếu không được huấn luyện, mô hình GPT sinh ra văn bản vô nghĩa, điều này nhấn mạnh tầm quan trọng của việc huấn luyện mô hình để nó có khả năng sinh văn bản mạch lạc.

> **Bài tập 4.3 Sử dụng tham số dropout riêng biệt**
>
> Ở phần đầu chương này, chúng ta đã định nghĩa cài đặt `drop_rate` chung trong biến `GPT_CONFIG_124M` để thiết lập tỷ lệ dropout ở nhiều nơi trong toàn bộ kiến trúc `GPTModel`. Hãy thay đổi code để chỉ định một giá trị dropout riêng cho các lớp dropout khác nhau trên toàn bộ kiến trúc mô hình. (Gợi ý: có ba vị trí phân biệt nơi chúng ta sử dụng các lớp dropout: lớp embedding, lớp shortcut và module multi-head attention.)
