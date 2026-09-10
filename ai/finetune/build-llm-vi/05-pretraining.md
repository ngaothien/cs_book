# Chương 5: Tiền huấn luyện trên dữ liệu không nhãn

Cho đến nay, chúng ta đã triển khai quá trình lấy mẫu dữ liệu và cơ chế attention, đồng thời đã viết code kiến trúc LLM. Giờ là lúc triển khai hàm huấn luyện và tiền huấn luyện (pretrain) LLM. Chúng ta sẽ tìm hiểu về các kỹ thuật đánh giá mô hình cơ bản để đo lường chất lượng văn bản được sinh ra, vốn là yêu cầu bắt buộc để tối ưu hóa LLM trong quá trình huấn luyện. Hơn nữa, chúng ta sẽ thảo luận cách nạp các trọng số đã được huấn luyện trước (pretrained weights), mang đến cho LLM một điểm khởi đầu vững chắc để tinh chỉnh (fine-tuning). Hình 5.1 phác thảo kế hoạch tổng thể của chúng ta, làm nổi bật những gì chúng ta sẽ thảo luận trong chương này.

*Chương này bao gồm:*
- *Tính toán mất mát tập huấn luyện và tập xác thực để đánh giá chất lượng văn bản LLM sinh ra trong quá trình huấn luyện*
- *Triển khai hàm huấn luyện và tiền huấn luyện LLM*
- *Lưu và nạp trọng số mô hình để tiếp tục huấn luyện LLM*
- *Nạp trọng số đã huấn luyện trước từ OpenAI*

[Hình 5.1: Ba giai đoạn chính của việc viết code LLM. Chương này tập trung vào giai đoạn 2: tiền huấn luyện LLM (bước 4), bao gồm triển khai code huấn luyện (bước 5), đánh giá hiệu suất (bước 6), và lưu cũng như nạp trọng số mô hình (bước 7).]

## 5.1 Đánh giá mô hình sinh văn bản

Sau khi nhắc lại tóm tắt về việc sinh văn bản từ chương 4, chúng ta sẽ thiết lập LLM để sinh văn bản và sau đó thảo luận về các cách cơ bản để đánh giá chất lượng văn bản được sinh ra. Tiếp đó, chúng ta sẽ tính toán độ mất mát (loss) trên tập huấn luyện và tập xác thực. Hình 5.2 hiển thị các chủ đề được đề cập trong chương này, với ba bước đầu tiên được làm nổi bật.

> **Tham số trọng số (Weight parameters)**
>
> Trong bối cảnh LLM và các mô hình deep learning khác, "trọng số" đề cập đến các tham số có thể huấn luyện mà quá trình học sẽ điều chỉnh. Các trọng số này còn được gọi là "tham số trọng số" hoặc đơn giản là "tham số". Trong các framework như PyTorch, các trọng số này được lưu trữ trong các lớp tuyến tính (linear layers); chúng ta đã sử dụng chúng để triển khai module multi-head attention trong chương 3 và `GPTModel` trong chương 4. Sau khi khởi tạo một lớp (`new_layer = torch.nn.Linear(...)`), chúng ta có thể truy cập các trọng số của nó thông qua thuộc tính `.weight`, `new_layer.weight`. Ngoài ra, để thuận tiện, PyTorch cho phép truy cập trực tiếp vào tất cả các tham số có thể huấn luyện của một mô hình, bao gồm cả trọng số và bias, thông qua phương thức `model.parameters()`, phương thức mà chúng ta sẽ sử dụng sau khi triển khai quá trình huấn luyện mô hình.

[Hình 5.2: Tổng quan về các chủ đề được đề cập trong chương này. Chúng ta bắt đầu bằng việc nhắc lại cách sinh văn bản (bước 1) trước khi chuyển sang thảo luận về các kỹ thuật đánh giá mô hình cơ bản (bước 2) và tính toán loss huấn luyện, xác thực (bước 3).]

### 5.1.1 Sử dụng GPT để sinh văn bản

Hãy thiết lập LLM và ôn lại ngắn gọn quá trình sinh văn bản mà chúng ta đã triển khai trong chương 4. Chúng ta bắt đầu bằng cách khởi tạo mô hình GPT mà chúng ta sẽ đánh giá và huấn luyện sau này, sử dụng lớp `GPTModel` và dictionary `GPT_CONFIG_124M` (xem chương 4):

```python
import torch
from chapter04 import GPTModel

GPT_CONFIG_124M = {
    "vocab_size": 50257,
    "context_length": 256,   # Chúng ta rút ngắn context length từ 1.024 xuống 256
    "emb_dim": 768,
    "n_heads": 12,
    "n_layers": 12, 
    "drop_rate": 0.1,      # Đặt dropout thành 0 là có thể và phổ biến.
    "qkv_bias": False
}

torch.manual_seed(123)
model = GPTModel(GPT_CONFIG_124M)
model.eval()
```

So với chương trước, thay đổi duy nhất trong dictionary `GPT_CONFIG_124M` là chúng ta đã giảm độ dài ngữ cảnh (`context_length`) xuống 256 token. Việc sửa đổi này làm giảm yêu cầu tính toán khi huấn luyện mô hình, giúp cho việc thực hiện huấn luyện trên một máy tính xách tay tiêu chuẩn trở nên khả thi.

Ban đầu, mô hình GPT-2 với 124 triệu tham số được cấu hình để xử lý tối đa 1.024 token. Sau quá trình huấn luyện, chúng ta sẽ cập nhật lại thiết lập kích thước ngữ cảnh và nạp các trọng số đã được huấn luyện trước để làm việc với mô hình có cấu hình độ dài ngữ cảnh 1.024 token.

Sử dụng đối tượng `GPTModel`, chúng ta sử dụng lại hàm `generate_text_simple` từ chương 4 và giới thiệu hai hàm tiện ích mới: `text_to_token_ids` và `token_ids_to_text`. Các hàm này hỗ trợ chuyển đổi qua lại giữa văn bản và biểu diễn token, một kỹ thuật chúng ta sẽ sử dụng xuyên suốt chương này.

Hình 5.3 minh họa quá trình sinh văn bản ba bước bằng mô hình GPT. Đầu tiên, tokenizer chuyển đổi văn bản đầu vào thành một chuỗi các ID token (xem chương 2). Thứ hai, mô hình nhận các ID token này và sinh ra các logit tương ứng, là các vector biểu diễn phân phối xác suất cho từng token trong từ vựng (xem chương 4). Thứ ba, các logit này được chuyển đổi trở lại thành các ID token, sau đó tokenizer sẽ giải mã chúng thành văn bản con người đọc được, hoàn tất chu trình từ đầu vào văn bản đến đầu ra văn bản.

[Hình 5.3: Việc sinh văn bản bao gồm mã hóa văn bản thành ID token để LLM xử lý thành các logit vector. Sau đó, logit vector được chuyển đổi lại thành ID token và giải mã thành văn bản.]

Chúng ta có thể triển khai quá trình sinh văn bản như trình bày trong listing sau.

**Listing 5.1: Các hàm tiện ích để chuyển đổi giữa văn bản và ID token**

```python
import tiktoken
from chapter04 import generate_text_simple

def text_to_token_ids(text, tokenizer):
    encoded = tokenizer.encode(text, allowed_special={'<|endoftext|>'})
    encoded_tensor = torch.tensor(encoded).unsqueeze(0) # .unsqueeze(0) thêm chiều batch
    return encoded_tensor

def token_ids_to_text(token_ids, tokenizer):
    flat = token_ids.squeeze(0)               # Loại bỏ chiều batch
    return tokenizer.decode(flat.tolist())

start_context = "Every effort moves you"
tokenizer = tiktoken.get_encoding("gpt2")

token_ids = generate_text_simple(
    model=model,
    idx=text_to_token_ids(start_context, tokenizer),
    max_new_tokens=10,
    context_size=GPT_CONFIG_124M["context_length"]
)

print("Output text:\n", token_ids_to_text(token_ids, tokenizer))
```

Sử dụng code này, mô hình sinh ra đoạn văn bản sau:

```
Output text:
 Every effort moves you rentingetic wasn? refres RexMeCHicular stren
```

Rõ ràng, mô hình chưa tạo ra được văn bản có nghĩa vì nó chưa được huấn luyện. Để xác định thế nào là văn bản "mạch lạc" hoặc "chất lượng cao", chúng ta phải triển khai một phương pháp toán học để đánh giá nội dung được sinh ra. Cách tiếp cận này sẽ cho phép chúng ta theo dõi và nâng cao hiệu suất của mô hình trong suốt quá trình huấn luyện.

Tiếp theo, chúng ta sẽ tính toán một metric mất mát (loss) cho các đầu ra được sinh ra. Loss này đóng vai trò như một chỉ báo về tiến độ và mức độ thành công của quá trình huấn luyện. Hơn nữa, trong các chương sau, khi tinh chỉnh LLM, chúng ta sẽ xem xét thêm các phương pháp bổ sung để đánh giá chất lượng mô hình.

### 5.1.2 Tính toán text generation loss (độ mất mát khi sinh văn bản)

Tiếp theo, hãy cùng khám phá các kỹ thuật để đánh giá bằng số học chất lượng văn bản được sinh ra trong quá trình huấn luyện bằng cách tính toán text generation loss. Chúng ta sẽ xem xét chủ đề này từng bước một với một ví dụ thực tế để làm cho các khái niệm trở nên rõ ràng và dễ áp dụng, bắt đầu bằng việc tóm tắt ngắn gọn cách dữ liệu được tải và cách văn bản được tạo ra qua hàm `generate_text_simple`.

Hình 5.4 minh họa luồng tổng thể từ văn bản đầu vào đến văn bản do LLM sinh ra bằng quy trình năm bước. Quy trình sinh văn bản này cho thấy hàm `generate_text_simple` làm gì ở bên trong. Chúng ta cần thực hiện các bước ban đầu này trước khi có thể tính toán một loss đo lường chất lượng văn bản được tạo ở phần sau.

Hình 5.4 phác thảo quá trình sinh văn bản với một từ vựng nhỏ gồm bảy token để vừa với trang in. Tuy nhiên, `GPTModel` của chúng ta làm việc với bộ từ vựng lớn hơn rất nhiều bao gồm 50.257 từ; do đó, các ID token trong đoạn code tiếp theo sẽ nằm trong khoảng từ 0 đến 50.256 thay vì từ 0 đến 6.

Ngoài ra, hình 5.4 chỉ hiển thị một ví dụ văn bản duy nhất ("every effort moves") cho đơn giản. Trong ví dụ code thực hành tiếp theo triển khai các bước trong hình, chúng ta sẽ làm việc với hai ví dụ đầu vào cho mô hình GPT ("every effort moves" và "I really like").

Hãy xem xét hai ví dụ đầu vào này, chúng đã được ánh xạ thành ID token (hình 5.4, bước 1):

```python
inputs = torch.tensor([[16833, 3626, 6100],   # ["every effort moves",
                       [40,    1107, 588]])   #  "I really like"]
```

Tương ứng với các đầu vào này, các mục tiêu (targets) chứa các ID token mà chúng ta muốn mô hình sinh ra:

```python
targets = torch.tensor([[3626, 6100, 345  ],  # [" effort moves you",
                        [1107, 588, 11311]])  #  " really like chocolate"]
```

Lưu ý rằng targets chính là inputs nhưng được dịch chuyển lên một vị trí, một khái niệm mà chúng ta đã đề cập trong chương 2 khi triển khai data loader. Chiến lược dịch chuyển này rất quan trọng để dạy mô hình dự đoán token tiếp theo trong một chuỗi.

[Hình 5.4: Với mỗi trong ba token đầu vào, chúng ta tính toán một vector chứa các điểm xác suất tương ứng với mỗi token trong từ vựng. Vị trí chỉ mục của điểm xác suất cao nhất trong mỗi vector đại diện cho ID token tiếp theo có khả năng nhất. Những ID token gắn với xác suất cao nhất sẽ được chọn và ánh xạ trở lại thành văn bản đại diện cho văn bản do mô hình tạo ra.]

Bây giờ chúng ta đưa các đầu vào vào mô hình để tính toán vector logit cho hai ví dụ đầu vào, mỗi ví dụ gồm ba token. Sau đó, chúng ta áp dụng hàm softmax để biến đổi các logit này thành điểm xác suất (probas; hình 5.4, bước 2):

```python
with torch.no_grad():    
    logits = model(inputs)
probas = torch.softmax(logits, dim=-1)    
print(probas.shape)
```

Kích thước tensor của tensor điểm xác suất (`probas`) là:

```
torch.Size([2, 3, 50257])
```

Số đầu tiên, 2, tương ứng với hai ví dụ (hàng) trong đầu vào, còn gọi là kích thước batch (batch size). Số thứ hai, 3, tương ứng với số lượng token trong mỗi đầu vào (hàng). Cuối cùng, số cuối cùng tương ứng với số chiều nhúng, được xác định bởi kích thước từ vựng. Sau khi chuyển đổi từ logit sang xác suất thông qua hàm softmax, hàm `generate_text_simple` sau đó chuyển đổi các điểm xác suất kết quả trở lại thành văn bản (hình 5.4, bước 3–5).

Chúng ta có thể hoàn thành bước 3 và 4 bằng cách áp dụng hàm `argmax` vào các điểm xác suất để lấy ID token tương ứng:

```python
token_ids = torch.argmax(probas, dim=-1, keepdim=True)
print("Token IDs:\n", token_ids)
```

Vì chúng ta có hai batch đầu vào, mỗi batch chứa ba token, việc áp dụng hàm `argmax` vào điểm xác suất (hình 5.4, bước 3) sẽ cho ra hai tập hợp đầu ra, mỗi tập gồm ba ID token được dự đoán:

```
Token IDs:
 tensor([[[16657],      
         [  339],
         [42826]],

        [[49906],       
         [29669],
         [41751]]])
```

Cuối cùng, bước 5 chuyển các ID token trở lại thành văn bản:

```python
print(f"Targets batch 1: {token_ids_to_text(targets[0], tokenizer)}")
print(f"Outputs batch 1:"
      f" {token_ids_to_text(token_ids[0].flatten(), tokenizer)}")
```

Khi giải mã các token này, chúng ta thấy rằng các token đầu ra khá khác biệt so với các token mục tiêu mà chúng ta muốn mô hình sinh ra:

```
Targets batch 1:  effort moves you
Outputs batch 1:  Armed heNetflix
```

Mô hình tạo ra văn bản ngẫu nhiên khác với văn bản mục tiêu vì nó chưa được huấn luyện. Bây giờ chúng ta muốn đánh giá hiệu suất của văn bản do mô hình tạo ra bằng số học thông qua một độ mất mát - loss (hình 5.5). Việc này không chỉ hữu ích để đo lường chất lượng của văn bản được tạo mà còn là một khối xây dựng cơ bản để triển khai hàm huấn luyện, từ đó cập nhật trọng số của mô hình nhằm cải thiện văn bản đầu ra.

Một phần của quy trình đánh giá văn bản mà chúng ta triển khai, như trong hình 5.5, là đo lường xem các token được sinh ra "cách xa" bao nhiêu so với dự đoán chính xác (targets). Hàm huấn luyện mà chúng ta triển khai sau này sẽ sử dụng thông tin này để điều chỉnh trọng số mô hình nhằm tạo ra văn bản tương tự hơn (hoặc, lý tưởng nhất là khớp hoàn toàn) với văn bản mục tiêu.

Huấn luyện mô hình nhằm mục đích tăng xác suất softmax tại các vị trí chỉ mục tương ứng với các ID token mục tiêu chính xác, như minh họa trong hình 5.6. Xác suất softmax này cũng được sử dụng trong metric đánh giá mà chúng ta sẽ triển khai tiếp theo để đánh giá bằng số học các đầu ra do mô hình tạo ra: xác suất tại các vị trí chính xác càng cao thì càng tốt.

Hãy nhớ rằng hình 5.6 hiển thị xác suất softmax cho một bộ từ vựng nhỏ gọn gồm bảy token để vừa vặn vào một hình duy nhất. Điều này có nghĩa là các giá trị ngẫu nhiên ban đầu sẽ dao động quanh mức 1/7, tức là xấp xỉ 0.14. Tuy nhiên, từ vựng mà chúng ta đang sử dụng cho mô hình GPT-2 có 50.257 token, do đó hầu hết các xác suất ban đầu sẽ dao động quanh mức 0.00002 (1/50.257).

[Hình 5.5: Tổng quan về các chủ đề trong chương này. Chúng ta đã hoàn tất bước 1 và sẵn sàng để triển khai hàm đánh giá văn bản (bước 2).]

Đối với mỗi trong hai văn bản đầu vào, chúng ta có thể in ra điểm xác suất softmax ban đầu tương ứng với các token mục tiêu bằng đoạn code sau:

```python
text_idx = 0
target_probas_1 = probas[text_idx, [0, 1, 2], targets[text_idx]]
print("Text 1:", target_probas_1)

text_idx = 1
target_probas_2 = probas[text_idx, [0, 1, 2], targets[text_idx]]
print("Text 2:", target_probas_2)
```

Xác suất của ba ID token mục tiêu cho mỗi batch là:

```
Text 1: tensor([7.4541e-05, 3.1061e-05, 1.1563e-05])
Text 2: tensor([1.0337e-05, 5.6776e-05, 4.7559e-06])
```

Mục tiêu của việc huấn luyện LLM là tối đa hóa khả năng xảy ra của token chính xác, bao gồm việc tăng xác suất của nó so với các token khác. Bằng cách này, chúng ta đảm bảo LLM luôn chọn token mục tiêu - về cơ bản là từ tiếp theo trong câu - làm token tiếp theo mà nó tạo ra.

[Hình 5.6: Trước khi huấn luyện, mô hình sinh ra các vector xác suất token ngẫu nhiên. Mục tiêu của huấn luyện mô hình là đảm bảo rằng các giá trị xác suất tương ứng với ID token mục tiêu được làm nổi bật được tối đa hóa.]

Tiếp theo, chúng ta sẽ tính toán loss cho các điểm xác suất của hai batch mẫu, `target_probas_1` và `target_probas_2`. Các bước chính được minh họa trong hình 5.7. Vì chúng ta đã áp dụng các bước 1 đến 3 để có được `target_probas_1` và `target_probas_2`, chúng ta chuyển sang bước 4, áp dụng logarithm cho các điểm xác suất:

```python
log_probas = torch.log(torch.cat((target_probas_1, target_probas_2)))
print(log_probas)
```

Điều này dẫn đến các giá trị sau:

```
tensor([ -9.5042, -10.3796, -11.3677, -11.4798,  -9.7764, -12.2561])
```

> **Lan truyền ngược (Backpropagation)**
>
> Làm thế nào để tối đa hóa các giá trị xác suất softmax tương ứng với các token mục tiêu? Bức tranh lớn là chúng ta cập nhật các trọng số mô hình sao cho mô hình xuất ra các giá trị cao hơn cho các ID token tương ứng mà chúng ta muốn tạo ra. Việc cập nhật trọng số được thực hiện thông qua một quá trình gọi là lan truyền ngược (backpropagation), một kỹ thuật tiêu chuẩn để huấn luyện các mạng thần kinh sâu (xem phần A.3 đến A.7 trong Phụ lục A để biết thêm chi tiết).
> Lan truyền ngược yêu cầu một hàm mất mát (loss function), dùng để tính toán sự khác biệt giữa đầu ra dự đoán của mô hình (ở đây là các xác suất tương ứng với ID token mục tiêu) và đầu ra mong muốn thực tế. Hàm mất mát này đo lường mức độ sai lệch giữa dự đoán của mô hình và giá trị mục tiêu.

[Hình 5.7: Việc tính toán loss bao gồm một số bước. Các bước 1 đến 3 tính toán xác suất token tương ứng với tensor mục tiêu. Những xác suất này sau đó được biến đổi bằng logarithm và lấy trung bình ở các bước 4 đến 6.]

Làm việc với logarithm của các điểm xác suất dễ quản lý hơn trong tối ưu hóa toán học so với việc xử lý các điểm số trực tiếp. Chủ đề này nằm ngoài phạm vi của cuốn sách, nhưng tôi đã trình bày chi tiết hơn trong một bài giảng có trong Phụ lục B.

Tiếp theo, chúng ta kết hợp các log probabilities (xác suất log) này thành một điểm số duy nhất bằng cách tính trung bình (bước 5 trong hình 5.7):

```python
avg_log_probas = torch.mean(log_probas)
print(avg_log_probas)
```

Điểm average log probability (xác suất log trung bình) thu được là:

```
tensor(-10.7940)
```

Mục tiêu là đưa average log probability càng gần 0 càng tốt bằng cách cập nhật các trọng số mô hình như một phần của quá trình huấn luyện. Tuy nhiên, trong deep learning, thực tiễn phổ biến không phải là đẩy average log probability lên 0 mà là đưa *negative average log probability* (xác suất log trung bình âm) xuống 0. Negative average log probability đơn giản là average log probability nhân với –1, tương ứng với bước 6 trong hình 5.7:

```python
neg_avg_log_probas = avg_log_probas * -1
print(neg_avg_log_probas)
```

Lệnh này in ra `tensor(10.7940)`. Trong deep learning, thuật ngữ để chỉ việc chuyển giá trị âm này, –10.7940, thành 10.7940, được gọi là **cross entropy loss** (mất mát chéo entropy). PyTorch rất hữu ích ở đây, vì nó đã có sẵn hàm `cross_entropy` xử lý tất cả sáu bước trong hình 5.7 cho chúng ta.

Trước khi áp dụng hàm `cross_entropy`, hãy xem xét lại shape của tensor logit và tensor mục tiêu:

```python
print("Logits shape:", logits.shape)
print("Targets shape:", targets.shape)
```

> **Cross entropy loss**
>
> Về cốt lõi, cross entropy loss là một phép đo phổ biến trong machine learning và deep learning dùng để đo lường sự khác biệt giữa hai phân phối xác suất—thường là phân phối thực của nhãn (ở đây là token trong tập dữ liệu) và phân phối dự đoán từ mô hình (ví dụ: xác suất token do LLM sinh ra).
> Trong bối cảnh machine learning và cụ thể là trong các framework như PyTorch, hàm `cross_entropy` tính toán phép đo này cho các kết quả rời rạc, tương tự như negative average log probability của các token mục tiêu dựa trên xác suất token do mô hình sinh ra, làm cho các thuật ngữ "cross entropy" và "negative average log probability" liên quan mật thiết và thường được sử dụng thay thế cho nhau trong thực tế.

Kết quả các shape là:

```
Logits shape: torch.Size([2, 3, 50257])
Targets shape: torch.Size([2, 3])
```

Như chúng ta thấy, tensor logit có ba chiều: kích thước batch, số token và kích thước từ vựng. Tensor mục tiêu có hai chiều: kích thước batch và số token.

Đối với hàm `cross_entropy` trong PyTorch, chúng ta muốn làm phẳng (flatten) các tensor này bằng cách kết hợp chúng dọc theo chiều batch:

```python
logits_flat = logits.flatten(0, 1)
targets_flat = targets.flatten()

print("Flattened logits:", logits_flat.shape)
print("Flattened targets:", targets_flat.shape)
```

Kết quả chiều tensor là:

```
Flattened logits: torch.Size([6, 50257])
Flattened targets: torch.Size([6])
```

Hãy nhớ rằng target là các ID token chúng ta muốn LLM sinh ra, và logit chứa các đầu ra mô hình chưa chia tỷ lệ (unscaled) trước khi chúng đi vào hàm softmax để có được điểm xác suất.

Trước đó, chúng ta đã áp dụng hàm softmax, chọn các điểm xác suất tương ứng với ID mục tiêu và tính toán negative average log probabilities. Hàm `cross_entropy` của PyTorch sẽ đảm nhiệm tất cả các bước này cho chúng ta:

```python
loss = torch.nn.functional.cross_entropy(logits_flat, targets_flat)
print(loss)
```

Loss thu được giống với loss mà chúng ta đã tính toán trước đó khi áp dụng thủ công các bước riêng lẻ trong hình 5.7:

```
tensor(10.7940)
```

> **Perplexity (Độ bối rối)**
>
> Perplexity là một phép đo thường được sử dụng cùng với cross entropy loss để đánh giá hiệu suất của mô hình trong các tác vụ như mô hình hóa ngôn ngữ. Nó cung cấp một cách dễ giải thích hơn để hiểu mức độ không chắc chắn của mô hình trong việc dự đoán token tiếp theo trong chuỗi.
> Perplexity đo lường mức độ khớp giữa phân phối xác suất do mô hình dự đoán và phân phối thực tế của các từ trong tập dữ liệu. Tương tự như loss, perplexity thấp hơn cho thấy dự đoán của mô hình gần hơn với phân phối thực tế.
> Có thể tính Perplexity bằng `perplexity = torch.exp(loss)`, lệnh này trả về `tensor(48725.8203)` khi áp dụng cho loss đã tính ở trên.
> Perplexity thường được coi là dễ diễn giải hơn giá trị loss thô vì nó biểu thị kích thước từ vựng có hiệu lực mà mô hình không chắc chắn ở mỗi bước. Trong ví dụ đã cho, điều này có nghĩa là mô hình không chắc chắn nên chọn token nào trong số 48.725 token trong từ vựng để tạo thành token tiếp theo.

Bây giờ chúng ta đã tính toán được loss cho hai đầu vào văn bản nhỏ nhằm mục đích minh họa. Tiếp theo, chúng ta sẽ áp dụng việc tính toán loss cho toàn bộ tập huấn luyện và tập xác thực.

### 5.1.3 Tính toán độ mất mát trên tập huấn luyện và tập xác thực

Trước tiên, chúng ta phải chuẩn bị tập huấn luyện và tập xác thực để huấn luyện LLM. Sau đó, như được làm nổi bật trong hình 5.8, chúng ta sẽ tính cross entropy cho tập huấn luyện và tập xác thực, một thành phần quan trọng của quá trình huấn luyện mô hình.

Để tính loss trên tập dữ liệu huấn luyện và xác thực, chúng ta sử dụng một tập dữ liệu văn bản rất nhỏ, truyện ngắn "The Verdict" của Edith Wharton, mà chúng ta đã làm việc trong chương 2. Bằng cách chọn một văn bản thuộc miền công cộng (public domain), chúng ta tránh được bất kỳ lo ngại nào liên quan đến quyền sử dụng. Ngoài ra, việc sử dụng tập dữ liệu nhỏ như vậy cho phép thực thi các ví dụ code trên máy tính xách tay tiêu chuẩn chỉ trong vài phút, ngay cả khi không có GPU mạnh, điều này đặc biệt thuận lợi cho mục đích giáo dục.

> **LƯU Ý**
> Độc giả quan tâm cũng có thể sử dụng source code đi kèm cuốn sách này để chuẩn bị một bộ dữ liệu quy mô lớn hơn gồm hơn 60.000 cuốn sách miền công cộng từ Project Gutenberg và huấn luyện LLM trên đó (xem Phụ lục D để biết chi tiết).

[Hình 5.8: Sau khi hoàn tất các bước 1 và 2, bao gồm tính toán cross entropy loss, giờ đây chúng ta có thể áp dụng phép tính loss này cho toàn bộ bộ dữ liệu văn bản sẽ dùng để huấn luyện mô hình.]

Đoạn mã sau tải truyện ngắn "The Verdict":

```python
file_path = "the-verdict.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text_data = file.read()
```

Sau khi tải tập dữ liệu, chúng ta có thể kiểm tra số lượng ký tự và token trong tập dữ liệu:

```python
total_characters = len(text_data)
total_tokens = len(tokenizer.encode(text_data))

print("Characters:", total_characters)
print("Tokens:", total_tokens)
```

Kết quả là:

```
Characters: 20479
Tokens: 5145
```

Với chỉ 5.145 token, văn bản này có vẻ quá nhỏ để huấn luyện một LLM, nhưng như đã đề cập trước đó, việc này dành cho mục đích giáo dục để chúng ta có thể chạy code trong vài phút thay vì vài tuần. Thêm vào đó, sau này chúng ta sẽ nạp các trọng số đã huấn luyện trước từ OpenAI vào code `GPTModel`.

Tiếp theo, chúng ta chia tập dữ liệu thành tập huấn luyện (training set) và tập xác thực (validation set) và sử dụng data loader từ chương 2 để chuẩn bị các batch cho việc huấn luyện LLM. Quá trình này được trực quan hóa trong hình 5.9. Do hạn chế về không gian, chúng ta sử dụng `max_length=6`. Tuy nhiên, đối với data loader thực tế, chúng ta đặt `max_length` bằng độ dài ngữ cảnh 256 token mà LLM hỗ trợ để LLM nhìn thấy văn bản dài hơn trong quá trình huấn luyện.

> **Chi phí tiền huấn luyện LLM**
>
> Để hình dung quy mô dự án của chúng ta, hãy xem xét việc huấn luyện mô hình Llama 2 có 7 tỷ tham số, một LLM khá phổ biến hiện có sẵn. Mô hình này cần 184.320 giờ GPU trên các GPU A100 đắt tiền, xử lý 2 nghìn tỷ token. Tại thời điểm viết bài, việc chạy một máy chủ cloud 8 × A100 trên AWS có giá khoảng 30 đô la một giờ. Ước tính sơ bộ cho thấy tổng chi phí huấn luyện LLM như vậy vào khoảng 690.000 đô la (tính bằng 184.320 giờ chia cho 8, sau đó nhân với 30 đô la).

> **LƯU Ý**
> Chúng ta đang huấn luyện mô hình với dữ liệu huấn luyện được trình bày thành các đoạn có kích thước tương đương nhau cho đơn giản và hiệu quả. Tuy nhiên, trong thực tế, cũng có thể hữu ích khi huấn luyện LLM với đầu vào có độ dài thay đổi để giúp LLM khái quát hóa tốt hơn với nhiều loại đầu vào khác nhau khi được sử dụng.

Để triển khai việc chia nhỏ và tải dữ liệu, đầu tiên chúng ta định nghĩa `train_ratio` để sử dụng 90% dữ liệu cho huấn luyện và 10% dữ liệu còn lại để làm dữ liệu xác thực cho đánh giá mô hình trong quá trình huấn luyện:

```python
train_ratio = 0.90
split_idx = int(train_ratio * len(text_data))
train_data = text_data[:split_idx]
val_data = text_data[split_idx:]
```

[Hình 5.9: Khi chuẩn bị data loader, chúng ta chia văn bản đầu vào thành các phần của tập huấn luyện và tập xác thực. Sau đó, chúng ta token hóa văn bản và chia văn bản đã token hóa thành các đoạn (chunk) với độ dài do người dùng chỉ định (ở đây là 6). Cuối cùng, chúng ta xáo trộn (shuffle) các hàng và tổ chức các đoạn văn bản thành các batch (batch size 2) để dùng cho việc huấn luyện mô hình.]

Sử dụng tập con `train_data` và `val_data`, bây giờ chúng ta có thể tạo data loader tương ứng bằng cách tái sử dụng code `create_dataloader_v1` từ chương 2:

```python
from chapter02 import create_dataloader_v1

torch.manual_seed(123)

train_loader = create_dataloader_v1(
    train_data,
    batch_size=2,
    max_length=GPT_CONFIG_124M["context_length"],
    stride=GPT_CONFIG_124M["context_length"],
    drop_last=True,
    shuffle=True,
    num_workers=0
)

val_loader = create_dataloader_v1(
    val_data,
    batch_size=2,
    max_length=GPT_CONFIG_124M["context_length"],
    stride=GPT_CONFIG_124M["context_length"],
    drop_last=False,
    shuffle=False,
    num_workers=0
)
```

Chúng ta sử dụng kích thước batch tương đối nhỏ để giảm yêu cầu tài nguyên tính toán vì chúng ta làm việc với bộ dữ liệu rất nhỏ. Trong thực tế, huấn luyện LLM với batch size 1.024 hoặc lớn hơn là rất phổ biến.

Như một bước kiểm tra tùy chọn, chúng ta có thể lặp qua các data loader để đảm bảo rằng chúng đã được tạo đúng cách:

```python
print("Train loader:")
for x, y in train_loader:
    print(x.shape, y.shape)

print("\nValidation loader:")
for x, y in val_loader:
    print(x.shape, y.shape)
```

Chúng ta sẽ thấy kết quả đầu ra sau:

```
Train loader:
torch.Size([2, 256]) torch.Size([2, 256])
torch.Size([2, 256]) torch.Size([2, 256])
torch.Size([2, 256]) torch.Size([2, 256])
torch.Size([2, 256]) torch.Size([2, 256])
torch.Size([2, 256]) torch.Size([2, 256])
torch.Size([2, 256]) torch.Size([2, 256])
torch.Size([2, 256]) torch.Size([2, 256])
torch.Size([2, 256]) torch.Size([2, 256])
torch.Size([2, 256]) torch.Size([2, 256])

Validation loader:
torch.Size([2, 256]) torch.Size([2, 256])
```

Dựa trên kết quả in ra của đoạn code trước, chúng ta có 9 batch cho tập huấn luyện, mỗi batch gồm hai mẫu, mỗi mẫu dài 256 token. Vì chúng ta chỉ phân bổ 10% dữ liệu cho việc xác thực, chỉ có một batch xác thực gồm hai ví dụ đầu vào. Đúng như mong đợi, dữ liệu đầu vào (`x`) và dữ liệu mục tiêu (`y`) có cùng kích thước (kích thước batch nhân số lượng token trong mỗi batch) vì mục tiêu chính là các đầu vào được dịch sang một vị trí, như đã thảo luận trong chương 2.

Tiếp theo, chúng ta sẽ viết một hàm tiện ích để tính toán cross entropy loss của một batch nhất định do loader huấn luyện hoặc xác thực trả về:

```python
def calc_loss_batch(input_batch, target_batch, model, device):
    input_batch = input_batch.to(device)        # Chuyển data sang thiết bị
    target_batch = target_batch.to(device)      # (ví dụ GPU)
    logits = model(input_batch)
    loss = torch.nn.functional.cross_entropy(
        logits.flatten(0, 1), target_batch.flatten()
    )
    return loss
```

Chúng ta có thể sử dụng hàm tiện ích `calc_loss_batch` (tính loss cho một batch duy nhất) này để triển khai hàm `calc_loss_loader` sau đây nhằm tính toán loss trên tất cả các batch được một data loader cung cấp.

**Listing 5.2: Hàm tính toán loss huấn luyện và xác thực**

```python
def calc_loss_loader(data_loader, model, device, num_batches=None):
    total_loss = 0.
    if len(data_loader) == 0:
        return float("nan")
    elif num_batches is None:
        num_batches = len(data_loader)    # Lặp qua toàn bộ nếu không khai báo
    else:
        # Giảm số lượng batch nếu num_batches lớn hơn
        num_batches = min(num_batches, len(data_loader))  
    for i, (input_batch, target_batch) in enumerate(data_loader):
        if i < num_batches:
            loss = calc_loss_batch(
                input_batch, target_batch, model, device
            )
            total_loss += loss.item()     # Cộng dồn loss
        else:
            break
    return total_loss / num_batches       # Lấy trung bình loss
```

Mặc định, hàm `calc_loss_loader` lặp qua toàn bộ batch trong data loader, cộng dồn loss vào biến `total_loss`, rồi chia trung bình loss trên tổng số lượng batch. Ngoài ra, chúng ta có thể xác định một số lượng batch nhỏ hơn thông qua tham số `num_batches` để tăng tốc độ đánh giá trong quá trình huấn luyện mô hình.

Hãy cùng xem hàm `calc_loss_loader` này hoạt động, áp dụng nó cho các loader tập huấn luyện và xác thực:

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)  # Đưa model lên device tương ứng với data

with torch.no_grad(): # Tắt tracking gradient để tăng hiệu suất
    train_loss = calc_loss_loader(train_loader, model, device)   
    val_loss = calc_loss_loader(val_loader, model, device)

print("Training loss:", train_loss)
print("Validation loss:", val_loss)
```

*(Nếu bạn có máy tính hỗ trợ GPU CUDA, LLM sẽ được huấn luyện trên GPU mà không cần thay đổi code).*

Kết quả giá trị loss là:

```
Training loss: 10.98758347829183
Validation loss: 10.98110580444336
```

Các giá trị loss tương đối cao vì mô hình chưa được huấn luyện. Để so sánh, loss sẽ tiến về 0 nếu mô hình học được cách sinh ra các token tiếp theo chính xác như cách chúng xuất hiện trong tập huấn luyện và tập xác thực.

Bây giờ khi đã có cách đo lường chất lượng văn bản sinh ra, chúng ta sẽ tiến hành huấn luyện LLM để giảm loss này, giúp mô hình cải thiện khả năng sinh văn bản, như minh họa trong hình 5.10.

[Hình 5.10: Chúng ta đã ôn lại quá trình sinh văn bản (bước 1) và triển khai các kỹ thuật đánh giá mô hình cơ bản (bước 2) để tính toán loss trên tập huấn luyện và tập xác thực (bước 3). Tiếp theo, chúng ta sẽ đi đến các hàm huấn luyện và tiền huấn luyện LLM (bước 4).]

Tiếp theo, chúng ta sẽ tập trung vào việc tiền huấn luyện LLM. Sau quá trình huấn luyện mô hình, chúng ta sẽ triển khai các chiến lược sinh văn bản thay thế và lưu cũng như nạp lại các trọng số mô hình đã được huấn luyện trước.

## 5.2 Huấn luyện một LLM

Cuối cùng cũng đến lúc triển khai code để tiền huấn luyện LLM, tức là `GPTModel` của chúng ta. Để làm điều này, chúng ta tập trung vào một vòng lặp huấn luyện đơn giản để giữ cho code ngắn gọn và dễ đọc.

> **LƯU Ý**
> Độc giả quan tâm có thể tìm hiểu về các kỹ thuật nâng cao hơn, bao gồm khởi động tốc độ học (learning rate warmup), cosine annealing, và cắt xén gradient (gradient clipping), trong Phụ lục D.

Lưu đồ trong hình 5.11 mô tả quy trình làm việc chuẩn khi huấn luyện mạng nơ-ron bằng PyTorch, quy trình này cũng được áp dụng cho việc huấn luyện một LLM. Nó phác thảo tám bước, bắt đầu bằng việc lặp qua từng epoch, xử lý các batch, đặt lại (reset) gradient, tính toán loss và gradient mới, cập nhật trọng số và kết thúc bằng các bước giám sát như in ra loss và sinh các mẫu văn bản.

> **LƯU Ý**
> Nếu bạn tương đối mới với việc huấn luyện mạng nơ-ron sâu bằng PyTorch và thấy bất kỳ bước nào trong số này xa lạ, hãy xem xét đọc các phần A.5 đến A.8 trong Phụ lục A.

[Hình 5.11: Một vòng lặp huấn luyện điển hình cho mạng nơ-ron sâu trong PyTorch bao gồm nhiều bước, lặp qua các batch trong tập huấn luyện trong một số epoch. Trong mỗi vòng lặp, chúng ta tính toán loss cho từng batch để xác định gradient, từ đó cập nhật trọng số mô hình sao cho loss giảm thiểu.]

Chúng ta có thể triển khai luồng huấn luyện này qua hàm `train_model_simple`:

**Listing 5.3: Hàm chính để tiền huấn luyện LLM**

```python
def train_model_simple(model, train_loader, val_loader,
                       optimizer, device, num_epochs,
                       eval_freq, eval_iter, start_context, tokenizer):
    
    # Khởi tạo các list để theo dõi loss và số token đã thấy
    train_losses, val_losses, track_tokens_seen = [], [], []   
    tokens_seen, global_step = 0, -1
    
    # Bắt đầu vòng lặp huấn luyện chính
    for epoch in range(num_epochs):   
        model.train()
        for input_batch, target_batch in train_loader:
            optimizer.zero_grad() # Đặt lại gradient từ batch trước 
            loss = calc_loss_batch(
                input_batch, target_batch, model, device
            )
            loss.backward()       # Tính toán gradient             
            optimizer.step()      # Cập nhật trọng số mô hình             
            tokens_seen += input_batch.numel()
            global_step += 1
            
            # Bước đánh giá tùy chọn
            if global_step % eval_freq == 0:   
                train_loss, val_loss = evaluate_model(
                    model, train_loader, val_loader, device, eval_iter)
                train_losses.append(train_loss)
                val_losses.append(val_loss)
                track_tokens_seen.append(tokens_seen)
                print(f"Ep {epoch+1} (Step {global_step:06d}): "
                      f"Train loss {train_loss:.3f}, "
                      f"Val loss {val_loss:.3f}"
                )
        
        # In văn bản mẫu sau mỗi epoch
        generate_and_print_sample(                     
            model, tokenizer, device, start_context
        )
    return train_losses, val_losses, track_tokens_seen
```

Lưu ý rằng hàm `train_model_simple` mà chúng ta vừa tạo sử dụng hai hàm chưa được định nghĩa: `evaluate_model` và `generate_and_print_sample`.

Hàm `evaluate_model` tương ứng với bước 7 trong hình 5.11. Nó in ra loss của tập huấn luyện và tập xác thực sau mỗi lần cập nhật mô hình để chúng ta có thể đánh giá xem việc huấn luyện có cải thiện mô hình hay không. Cụ thể hơn, hàm `evaluate_model` tính toán loss trên tập huấn luyện và tập xác thực đồng thời đảm bảo mô hình đang ở chế độ đánh giá (`eval mode`) bằng cách vô hiệu hóa dropout và theo dõi gradient:

```python
def evaluate_model(model, train_loader, val_loader, device, eval_iter):
    model.eval() # Vô hiệu hóa dropout để có kết quả ổn định
    with torch.no_grad(): # Tắt tính toán gradient để giảm chi phí tính toán                            
        train_loss = calc_loss_loader(
            train_loader, model, device, num_batches=eval_iter
        )
        val_loss = calc_loss_loader(
            val_loader, model, device, num_batches=eval_iter
        )
    model.train()
    return train_loss, val_loss
```

Tương tự như `evaluate_model`, `generate_and_print_sample` là một hàm tiện ích mà chúng ta sử dụng để theo dõi xem mô hình có cải thiện trong quá trình huấn luyện hay không. Cụ thể, hàm `generate_and_print_sample` nhận một đoạn văn bản (`start_context`) làm đầu vào, chuyển đổi nó thành ID token, và đưa vào LLM để sinh ra một mẫu văn bản bằng cách sử dụng hàm `generate_text_simple` đã viết trước đó:

```python
def generate_and_print_sample(model, tokenizer, device, start_context):
    model.eval()
    context_size = model.pos_emb.weight.shape[0]
    encoded = text_to_token_ids(start_context, tokenizer).to(device)
    with torch.no_grad():
        token_ids = generate_text_simple(
            model=model, idx=encoded,
            max_new_tokens=50, context_size=context_size
        )
    decoded_text = token_ids_to_text(token_ids, tokenizer)
    print(decoded_text.replace("\n", " ")) # Định dạng in gọn gàng hơn
    model.train()
```

Trong khi hàm `evaluate_model` cung cấp ước tính bằng số về tiến độ huấn luyện của mô hình, hàm `generate_and_print_sample` này cung cấp một ví dụ văn bản cụ thể do mô hình tạo ra để chúng ta đánh giá khả năng của nó trong suốt quá trình huấn luyện.

> **AdamW**
>
> Các optimizer (trình tối ưu hóa) thuộc họ Adam là lựa chọn phổ biến để huấn luyện mạng nơ-ron sâu. Tuy nhiên, trong vòng lặp huấn luyện của mình, chúng ta chọn optimizer AdamW. AdamW là một biến thể của Adam cải tiến cách tiếp cận suy giảm trọng số (weight decay), nhằm giảm thiểu độ phức tạp của mô hình và ngăn ngừa overfitting bằng cách phạt các trọng số lớn. Việc điều chỉnh này cho phép AdamW đạt được regularization (điều chuẩn) hiệu quả hơn và khả năng tổng quát hóa tốt hơn; do đó, AdamW thường được sử dụng trong việc huấn luyện LLM.

Hãy cùng xem mọi thứ hoạt động thực tế bằng cách huấn luyện đối tượng `GPTModel` trong 10 epoch bằng optimizer AdamW và hàm `train_model_simple` mà chúng ta đã định nghĩa:

```python
torch.manual_seed(123)
model = GPTModel(GPT_CONFIG_124M)
model.to(device)
optimizer = torch.optim.AdamW(
    model.parameters(), # model.parameters() trả về toàn bộ trọng số có thể huấn luyện của model         
    lr=0.0004, weight_decay=0.1
)

num_epochs = 10
train_losses, val_losses, tokens_seen = train_model_simple(
    model, train_loader, val_loader, optimizer, device,
    num_epochs=num_epochs, eval_freq=5, eval_iter=5,
    start_context="Every effort moves you", tokenizer=tokenizer
)
```

Việc thực thi hàm `train_model_simple` khởi động quá trình huấn luyện, mất khoảng 5 phút để hoàn thành trên MacBook Air hoặc laptop tương tự. Kết quả in ra trong quá trình thực thi như sau:

```
Ep 1 (Step 000000): Train loss 9.781, Val loss 9.933
Ep 1 (Step 000005): Train loss 8.111, Val loss 8.339
Every effort moves you,,,,,,,,,,,,.                                     
Ep 2 (Step 000010): Train loss 6.661, Val loss 7.048
Ep 2 (Step 000015): Train loss 5.961, Val loss 6.616
Every effort moves you, and, and, and, and, and, and, and, and, and, and,
 and, and, and, and, and, and, and, and, and, and, and, and,, and, and,
[...]                                                  
Ep 9 (Step 000080): Train loss 0.541, Val loss 6.393
Every effort moves you?"  "Yes--quite insensible to the irony. She wanted
him vindicated--and by me!"  He laughed again, and threw back the 
window-curtains, I had the donkey. "There were days when I
Ep 10 (Step 000085): Train loss 0.391, Val loss 6.452
Every effort moves you know," was one of the axioms he laid down across the
Sevres and silver of an exquisitely appointed luncheon-table, when, on a
later day, I had again run over from Monte Carlo; and Mrs. Gis
```

Như chúng ta thấy, loss huấn luyện (training loss) cải thiện đáng kể, bắt đầu từ giá trị 9.781 và hội tụ về 0.391. Kỹ năng ngôn ngữ của mô hình đã cải thiện khá nhiều. Lúc đầu, mô hình chỉ có thể nối thêm dấu phẩy vào ngữ cảnh ban đầu (`Every effort moves you,,,,,,,,,,,,`) hoặc lặp lại từ `and`. Đến cuối quá trình huấn luyện, nó có thể tạo ra các câu đúng ngữ pháp.

Tương tự như loss của tập huấn luyện, chúng ta có thể thấy rằng loss xác thực (validation loss) bắt đầu khá cao (9.933) và giảm trong suốt quá trình huấn luyện. Tuy nhiên, nó không bao giờ nhỏ như training loss và giữ ở mức 6.452 sau epoch thứ 10.

Trước khi thảo luận chi tiết hơn về validation loss, hãy vẽ một biểu đồ đơn giản hiển thị loss huấn luyện và xác thực cạnh nhau:

```python
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def plot_losses(epochs_seen, tokens_seen, train_losses, val_losses):
    fig, ax1 = plt.subplots(figsize=(5, 3))
    
    ax1.plot(epochs_seen, train_losses, label="Training loss")
    ax1.plot(
        epochs_seen, val_losses, linestyle="-.", label="Validation loss"
    )
    ax1.set_xlabel("Epochs")
    ax1.set_ylabel("Loss")
    ax1.legend(loc="upper right")
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
    
    # Tạo trục X thứ hai dùng chung trục Y
    ax2 = ax1.twiny()                  
    ax2.plot(tokens_seen, train_losses, alpha=0) # Plot vô hình để gióng hàng tick   
    ax2.set_xlabel("Tokens seen")
    
    fig.tight_layout()
    plt.show()

epochs_tensor = torch.linspace(0, num_epochs, len(train_losses))
plot_losses(epochs_tensor, tokens_seen, train_losses, val_losses)
```

[Hình 5.12: Ở giai đoạn đầu của huấn luyện, cả training loss và validation loss đều giảm mạnh, dấu hiệu cho thấy mô hình đang học. Tuy nhiên, training loss tiếp tục giảm sau epoch thứ 2, trong khi validation loss bị đình trệ. Đây là dấu hiệu mô hình vẫn đang học nhưng bắt đầu overfitting (quá khớp) với tập huấn luyện kể từ sau epoch 2.]

Biểu đồ loss huấn luyện và xác thực kết quả được hiển thị trong hình 5.12. Như chúng ta thấy, cả hai loss đều bắt đầu cải thiện trong epoch đầu tiên. Tuy nhiên, các đường loss bắt đầu phân kỳ sau epoch thứ hai. Sự phân kỳ này và thực tế là validation loss lớn hơn nhiều so với training loss chỉ ra rằng mô hình đang quá khớp (overfitting) với dữ liệu huấn luyện. Chúng ta có thể xác nhận rằng mô hình đang ghi nhớ thuộc lòng (memorize) dữ liệu huấn luyện bằng cách tìm kiếm các đoạn văn bản được tạo, ví dụ như "quite insensible to the irony", trong file văn bản "The Verdict".

Sự ghi nhớ này là có thể đoán trước vì chúng ta đang làm việc với một tập dữ liệu huấn luyện rất nhỏ và huấn luyện mô hình trong nhiều epoch. Thông thường, thực tế phổ biến là huấn luyện mô hình trên một tập dữ liệu lớn hơn nhiều và chỉ lặp qua một epoch duy nhất.

> **LƯU Ý**
> Như đã đề cập trước đó, độc giả quan tâm có thể thử huấn luyện mô hình trên 60.000 cuốn sách thuộc miền công cộng từ Project Gutenberg, nơi hiện tượng overfitting này không xảy ra; xem Phụ lục B để biết chi tiết.

Như được minh họa trong hình 5.13, chúng ta đã hoàn thành bốn mục tiêu cho chương này. Tiếp theo, chúng ta sẽ đề cập đến các chiến lược sinh văn bản cho LLM để giảm thiểu việc ghi nhớ dữ liệu huấn luyện và tăng tính sáng tạo của văn bản do LLM sinh ra, trước khi chúng ta đề cập đến việc lưu/nạp trọng số và nạp trọng số đã tiền huấn luyện từ mô hình GPT của OpenAI.

[Hình 5.13: Mô hình của chúng ta có thể sinh ra văn bản mạch lạc sau khi triển khai hàm huấn luyện. Tuy nhiên, nó thường ghi nhớ các đoạn văn từ tập huấn luyện nguyên văn. Tiếp theo, chúng ta sẽ thảo luận các chiến lược để tạo ra các văn bản đầu ra đa dạng hơn.]

## 5.3 Các chiến lược giải mã (decoding strategies) để kiểm soát tính ngẫu nhiên

Hãy xem xét các chiến lược sinh văn bản (còn gọi là các chiến lược giải mã) để sinh ra văn bản sáng tạo hơn. Đầu tiên, chúng ta sẽ ôn lại nhanh hàm `generate_text_simple` mà chúng ta đã dùng trong `generate_and_print_sample` trước đó. Sau đó, chúng ta sẽ trình bày hai kỹ thuật, bù nhiệt độ (temperature scaling) và lấy mẫu top-k (top-k sampling), để cải thiện hàm này.

Chúng ta bắt đầu bằng cách chuyển mô hình từ GPU về CPU vì việc suy luận (inference) với một mô hình tương đối nhỏ không yêu cầu GPU. Đồng thời, sau khi huấn luyện, chúng ta chuyển mô hình sang chế độ đánh giá (`eval`) để tắt các thành phần ngẫu nhiên như dropout:

```python
model.to("cpu")
model.eval()
```

Tiếp theo, chúng ta đưa đối tượng `GPTModel` (`model`) vào hàm `generate_text_simple`, hàm này sử dụng LLM để sinh mỗi lần một token:

```python
tokenizer = tiktoken.get_encoding("gpt2")
token_ids = generate_text_simple(
    model=model,
    idx=text_to_token_ids("Every effort moves you", tokenizer),
    max_new_tokens=25,
    context_size=GPT_CONFIG_124M["context_length"]
)

print("Output text:\n", token_ids_to_text(token_ids, tokenizer))
```

Văn bản sinh ra là:

```
Output text:
 Every effort moves you know," was one of the axioms he laid down across the
Sevres and silver of an exquisitely appointed lun
```

Như đã giải thích trước đó, token được sinh ra sẽ được chọn ở mỗi bước sao cho tương ứng với điểm xác suất lớn nhất trong số tất cả token trong từ vựng. Điều này có nghĩa là LLM sẽ luôn sinh ra cùng một đầu ra ngay cả khi chúng ta chạy hàm `generate_text_simple` nhiều lần trên cùng một ngữ cảnh ban đầu ("Every effort moves you").

### 5.3.1 Bù nhiệt độ (Temperature scaling)

Hãy cùng xem xét temperature scaling, một kỹ thuật bổ sung một quy trình chọn ngẫu nhiên vào tác vụ sinh token tiếp theo. Trước đây, trong hàm `generate_text_simple`, chúng ta luôn lấy mẫu token có xác suất cao nhất bằng `torch.argmax`, hay còn gọi là greedy decoding (giải mã tham lam). Để sinh ra văn bản đa dạng hơn, chúng ta có thể thay thế `argmax` bằng một hàm lấy mẫu từ một phân phối xác suất (ở đây là các điểm xác suất mà LLM sinh ra cho mỗi mục từ vựng ở mỗi bước sinh token).

Để minh họa việc lấy mẫu xác suất bằng một ví dụ cụ thể, hãy cùng thảo luận ngắn gọn quá trình sinh token tiếp theo sử dụng một bộ từ vựng rất nhỏ:

```python
vocab = { 
    "closer": 0,
    "every": 1, 
    "effort": 2, 
    "forward": 3,
    "inches": 4,
    "moves": 5, 
    "pizza": 6,
    "toward": 7,
    "you": 8,
} 
inverse_vocab = {v: k for k, v in vocab.items()}
```

Tiếp theo, giả sử LLM được cấp ngữ cảnh khởi đầu là "every effort moves you" và nó sinh ra các logit cho token tiếp theo như sau:

```python
next_token_logits = torch.tensor(
    [4.51, 0.89, -1.90, 6.75, 1.63, -1.62, -1.89, 6.28, 1.79]
)
```

Như đã thảo luận ở chương 4, bên trong `generate_text_simple`, chúng ta biến đổi logit thành xác suất qua hàm softmax và lấy ID token tương ứng bằng hàm `argmax`, sau đó ta có thể ánh xạ lại thành văn bản thông qua từ vựng ngược (inverse vocabulary):

```python
probas = torch.softmax(next_token_logits, dim=0)
next_token_id = torch.argmax(probas).item()
print(inverse_vocab[next_token_id])
```

Vì giá trị logit lớn nhất và, tương ứng, điểm xác suất softmax lớn nhất nằm ở vị trí thứ tư (index 3 vì Python đếm từ 0), từ được sinh ra là "forward".

Để triển khai một quá trình chọn mẫu xác suất, chúng ta có thể thay thế `argmax` bằng hàm `multinomial` trong PyTorch:

```python
torch.manual_seed(123) 
next_token_id = torch.multinomial(probas, num_samples=1).item()
print(inverse_vocab[next_token_id])
```

Đầu ra in ra vẫn là "forward" giống như trước. Có chuyện gì vậy? Hàm `multinomial` lấy mẫu token tiếp theo tỷ lệ thuận với điểm xác suất của nó. Nói cách khác, "forward" vẫn là token có khả năng xuất hiện cao nhất và sẽ được chọn bởi `multinomial` hầu hết các lần, nhưng không phải mọi lúc. Để minh họa điều này, hãy triển khai một hàm lặp lại quá trình lấy mẫu này 1.000 lần:

```python
def print_sampled_tokens(probas):
    torch.manual_seed(123)
    sample = [torch.multinomial(probas, num_samples=1).item()
             for i in range(1_000)]
    sampled_ids = torch.bincount(torch.tensor(sample))
    for i, freq in enumerate(sampled_ids):
        print(f"{freq} x {inverse_vocab[i]}")

print_sampled_tokens(probas)
```

Kết quả lấy mẫu là:

```
73 x closer
0 x every
0 x effort
582 x forward
2 x inches
0 x moves
0 x pizza
343 x toward
```

Như chúng ta thấy, từ "forward" được lấy mẫu hầu hết thời gian (582 trên 1.000 lần), nhưng các token khác như "closer", "inches", và "toward" cũng sẽ được lấy mẫu vài lần. Điều này có nghĩa là nếu chúng ta thay thế hàm `argmax` bằng hàm `multinomial` bên trong hàm `generate_and_print_sample`, LLM đôi khi sẽ sinh ra các văn bản như "every effort moves you toward", "every effort moves you inches", và "every effort moves you closer" thay vì chỉ toàn "every effort moves you forward".

Chúng ta có thể kiểm soát sâu hơn phân phối và quá trình chọn mẫu bằng một khái niệm gọi là temperature scaling (bù nhiệt độ). Temperature scaling thực chất chỉ là cách gọi mỹ miều cho việc chia các logit cho một số lớn hơn 0:

```python
def softmax_with_temperature(logits, temperature):
    scaled_logits = logits / temperature
    return torch.softmax(scaled_logits, dim=0)
```

Nhiệt độ (temperature) lớn hơn 1 dẫn đến các xác suất token được phân phối đồng đều hơn, và nhiệt độ nhỏ hơn 1 sẽ dẫn đến các phân phối tự tin hơn (sắc nhọn hơn, có đỉnh rõ hơn). Hãy cùng minh họa điều này bằng cách vẽ sơ đồ các xác suất gốc cùng với các xác suất được scale bằng nhiều giá trị nhiệt độ khác nhau:

```python
temperatures = [1, 0.1, 5]                                    
scaled_probas = [softmax_with_temperature(next_token_logits, T)
                for T in temperatures]

x = torch.arange(len(vocab))
bar_width = 0.15
fig, ax = plt.subplots(figsize=(5, 3))

for i, T in enumerate(temperatures):
    rects = ax.bar(x + i * bar_width, scaled_probas[i], 
                   bar_width, label=f'Temperature = {T}')

ax.set_ylabel('Probability')
ax.set_xticks(x)
ax.set_xticklabels(vocab.keys(), rotation=90)
ax.legend()
plt.tight_layout()
plt.show()
```

Biểu đồ kết quả được hiển thị trong hình 5.14.

Nhiệt độ bằng 1 sẽ chia logit cho 1 trước khi đưa vào hàm softmax. Nói cách khác, việc sử dụng nhiệt độ bằng 1 cũng giống như không sử dụng bù nhiệt độ nào. Trong trường hợp này, các token được chọn với xác suất bằng với điểm xác suất softmax gốc thông qua hàm lấy mẫu `multinomial` trong PyTorch. Ví dụ, với thiết lập nhiệt độ là 1, token tương ứng với "forward" sẽ được chọn khoảng 60% số lần, như chúng ta có thể thấy trong hình 5.14.

[Hình 5.14: Nhiệt độ 1 đại diện cho điểm xác suất không bị điều chỉnh (unscaled). Giảm nhiệt độ xuống 0.1 làm sắc nhọn phân phối, khiến cho token có khả năng nhất ("forward") sẽ có điểm xác suất còn cao hơn nữa. Ngược lại, tăng nhiệt độ lên 5 khiến cho phân phối trở nên đồng đều (uniform) hơn.]

Ngoài ra, như trong hình 5.14, áp dụng nhiệt độ rất nhỏ, chẳng hạn như 0.1, sẽ làm cho phân phối nhọn hơn, dẫn đến hành vi của hàm `multinomial` sẽ chọn token có khả năng xuất hiện cao nhất (ở đây là "forward") gần 100% thời gian, tiến gần đến hành vi của hàm `argmax`. Tương tự, nhiệt độ 5 tạo ra phân phối đều hơn nơi các token khác được chọn thường xuyên hơn. Việc này có thể bổ sung thêm tính đa dạng cho các văn bản sinh ra nhưng đồng thời cũng thường xuyên tạo ra những văn bản vô nghĩa hơn. Ví dụ, sử dụng nhiệt độ 5 sinh ra văn bản như "every effort moves you pizza" khoảng 4% thời gian.

> **Bài tập 5.1**
> Sử dụng hàm `print_sampled_tokens` để in ra các tần suất lấy mẫu của các xác suất softmax được scale với các nhiệt độ như hình 5.14. Tần suất từ "pizza" được chọn trong mỗi trường hợp là bao nhiêu? Bạn có thể nghĩ ra cách nhanh hơn và chính xác hơn để xác định xem từ "pizza" được chọn tần suất ra sao không?

### 5.3.2 Lấy mẫu Top-k (Top-k sampling)

Chúng ta đã triển khai phương pháp lấy mẫu xác suất kết hợp với bù nhiệt độ để tăng tính đa dạng của các đầu ra. Chúng ta đã thấy rằng các giá trị nhiệt độ cao hơn mang đến các phân phối xác suất token tiếp theo đồng đều hơn, từ đó tạo ra đầu ra đa dạng hơn vì nó giảm thiểu khả năng mô hình liên tục chọn token có xác suất cao nhất. Phương pháp này cho phép khám phá các nhánh kém khả năng hơn nhưng tiềm năng thú vị và sáng tạo hơn trong quá trình sinh văn bản. Tuy nhiên, một nhược điểm của phương pháp này là thỉnh thoảng nó dẫn đến các đầu ra sai ngữ pháp hoặc hoàn toàn vô nghĩa như "every effort moves you pizza".

Lấy mẫu Top-k, khi kết hợp cùng lấy mẫu xác suất và bù nhiệt độ, có thể cải thiện kết quả sinh văn bản. Trong lấy mẫu top-k, chúng ta có thể hạn chế các token được lấy mẫu trong top k token có khả năng xuất hiện cao nhất và loại trừ tất cả các token khác bằng cách gán cho xác suất của chúng giá trị ẩn (mask), như minh họa ở Hình 5.15.

Phương pháp top-k thay thế tất cả logit không được chọn thành giá trị âm vô cực (`-inf`), để khi tính giá trị softmax, các xác suất của các token không thuộc top-k sẽ là 0, và các xác suất còn lại sẽ cộng tổng bằng 1. (Độc giả tinh ý có thể nhớ lại kỹ thuật mask này từ module causal attention mà chúng ta đã triển khai ở chương 3, mục 3.5.1).

[Hình 5.15: Sử dụng lấy mẫu top-k với k = 3, chúng ta tập trung vào 3 token có logit cao nhất và mask tất cả token khác bằng âm vô cực (`-inf`) trước khi áp dụng hàm softmax. Kết quả là tạo ra phân phối xác suất với xác suất 0 gán cho tất cả các token không thuộc top-k.]

Trong code, chúng ta có thể triển khai tiến trình top-k ở hình 5.15 như sau, bắt đầu với việc chọn các token có logit lớn nhất:

```python
top_k = 3
top_logits, top_pos = torch.topk(next_token_logits, top_k)

print("Top logits:", top_logits)
print("Top positions:", top_pos)
```

Các giá trị logit và ID của top 3 token (theo thứ tự giảm dần) là:

```
Top logits: tensor([6.7500, 6.2800, 4.5100])
Top positions: tensor([3, 7, 0])
```

Kế tiếp, chúng ta sử dụng hàm `where` của PyTorch để thiết lập các logit thấp hơn logit thấp nhất trong nhóm top-3 thành âm vô cực (`-inf`):

```python
new_logits = torch.where(
    condition=next_token_logits < top_logits[-1],   
    input=torch.tensor(float('-inf')),    
    other=next_token_logits    
)
print(new_logits)
```

Các logit kết quả cho token kế tiếp trong nhóm từ vựng (9 token) là:

```
tensor([4.5100,   -inf,   -inf, 6.7500,   -inf,   -inf,   -inf, 6.2800,
     -inf])
```

Cuối cùng, chúng ta áp dụng hàm softmax để biến chúng thành xác suất token tiếp theo:

```python
topk_probas = torch.softmax(new_logits, dim=0)
print(topk_probas)
```

Như chúng ta thấy, kết quả của top-3 approach là ba xác suất khác 0:

```
tensor([0.0615, 0.0000, 0.0000, 0.5775, 0.0000, 0.0000, 0.0000, 0.3610,
        0.0000])
```

Bây giờ chúng ta có thể kết hợp bù nhiệt độ (temperature scaling) và lấy mẫu `multinomial` để chọn token tiếp theo từ các điểm xác suất khác không. Tiếp theo, chúng ta sẽ điều chỉnh hàm `generate` cho phù hợp.

### 5.3.3 Chỉnh sửa hàm sinh văn bản

Bây giờ, hãy kết hợp bù nhiệt độ và top-k sampling để điều chỉnh hàm `generate_text_simple` lúc nãy, tạo ra một hàm `generate` mới:

**Listing 5.4: Hàm sinh văn bản mới được chỉnh sửa với nhiều tính đa dạng hơn**

```python
def generate(model, idx, max_new_tokens, context_size,
             temperature=0.0, top_k=None, eos_id=None):
    for _ in range(max_new_tokens):           
        idx_cond = idx[:, -context_size:]
        with torch.no_grad():
            logits = model(idx_cond)
        logits = logits[:, -1, :] # Chỉ lấy time step cuối
        
        if top_k is not None:               
            # Lọc logit với top_k
            top_logits, _ = torch.topk(logits, top_k)
            min_val = top_logits[:, -1]
            logits = torch.where(
                logits < min_val,
                torch.tensor(float('-inf')).to(logits.device),
                logits
            )
            
        if temperature > 0.0:                 
            # Áp dụng bù nhiệt độ
            logits = logits / temperature
            probs = torch.softmax(logits, dim=-1)
            idx_next = torch.multinomial(probs, num_samples=1)
        else:   
            # Dùng greedy như trước nếu temperature là 0
            idx_next = torch.argmax(logits, dim=-1, keepdim=True)
            
        if idx_next == eos_id: # Dừng sinh nếu chạm token kết thúc             
            break
        idx = torch.cat((idx, idx_next), dim=1)
    return idx
```

Cùng xem hàm `generate` này chạy thực tế:

```python
torch.manual_seed(123)
token_ids = generate(
    model=model,
    idx=text_to_token_ids("Every effort moves you", tokenizer),
    max_new_tokens=15,
    context_size=GPT_CONFIG_124M["context_length"],
    top_k=25,
    temperature=1.4
)

print("Output text:\n", token_ids_to_text(token_ids, tokenizer))
```

Văn bản kết quả là:

```
Output text:
 Every effort moves you stand to work on surprise, a one of us had gone
 with random-
```

Như chúng ta thấy, văn bản sinh ra rất khác so với thứ được sinh ra từ `generate_text_simple` trong phần 5.3 ("Every effort moves you know," was one of the axioms he laid...!), vốn là một đoạn học thuộc từ tập huấn luyện.

> **Bài tập 5.2**
> Thử với các thiết lập temperature và top-k khác nhau. Dựa trên quan sát, bạn có thể nghĩ đến ứng dụng nào phù hợp với thiết lập nhiệt độ và top-k thấp hơn? Ngược lại, trường hợp nào thì thiết lập cao hơn được ưa chuộng? (Khuyến nghị là quay lại bài tập này ở cuối chương sau khi tải trọng số GPT của OpenAI).

## 5.4 Lưu và nạp trọng số mô hình trong PyTorch

Đến lúc này, chúng ta đã thảo luận cách đo lường bằng số học về hiệu suất huấn luyện và cách huấn luyện LLM từ đầu. Dù mô hình và tập dữ liệu còn nhỏ, nhưng bài thực hành này chứng minh rằng việc tiền huấn luyện LLM tốn kém rất nhiều tài nguyên tính toán. Do đó, việc biết cách lưu trữ LLM để không phải chạy lại cả mô hình mỗi lần sử dụng trong một session mới là rất quan trọng.

Vậy hãy cùng tìm hiểu cách lưu và nạp (load) một mô hình đã tiền huấn luyện, như minh họa ở Hình 5.16. Lát nữa, chúng ta sẽ nạp mô hình tiền huấn luyện GPT mạnh hơn từ OpenAI vào `GPTModel`.

[Hình 5.16: Sau khi huấn luyện và kiểm tra mô hình, việc lưu lại mô hình để tái sử dụng hay huấn luyện tiếp sau này là rất hữu ích (bước 6).]

May mắn thay, lưu một mô hình PyTorch khá thẳng thắn. Cách được khuyến nghị là lưu `state_dict` của mô hình, đó là một dictionary ánh xạ từng layer với tham số của nó, dùng `torch.save`:

```python
torch.save(model.state_dict(), "model.pth")
```

`model.pth` là file lưu `state_dict`. Đuôi `.pth` là định dạng quy ước cho file PyTorch, dù kỹ thuật có thể dùng bất cứ phần mở rộng nào.

Sau khi lưu các tham số trọng số qua `state_dict`, chúng ta có thể nạp chúng vào một đối tượng `GPTModel` mới:

```python
model = GPTModel(GPT_CONFIG_124M)
model.load_state_dict(torch.load("model.pth", map_location=device))
model.eval()
```

Như đã thảo luận trong chương 4, dropout hỗ trợ chống overfitting. Nhưng khi sử dụng (inference), ta không muốn layer bị "drop out" ngẫu nhiên các nơ-ron thông tin. Dùng lệnh `model.eval()` chuyển mô hình sang chế độ inference, tắt các dropout. Nếu muốn tiếp tục pretrain về sau (dùng hàm `train_model_simple`), việc lưu trạng thái `optimizer` cũng rất được khuyến khích.

Optimizer như AdamW lưu các tham số bổ sung cho từng trọng số. Nó dùng lịch sử dữ liệu để tự động điều chỉnh tốc độ học cho từng thông số. Nếu thiếu nó, optimizer bị reset, và mô hình có thể gặp vấn đề về hội tụ và bị mất chức năng sinh câu mạch lạc. Dùng `torch.save`, ta có thể lưu cả model và optimizer `state_dict`:

```python
torch.save({
    "model_state_dict": model.state_dict(),
    "optimizer_state_dict": optimizer.state_dict(),
    }, 
    "model_and_optimizer.pth"
)
```

Sau đó phục hồi trạng thái bằng cách:

```python
checkpoint = torch.load("model_and_optimizer.pth", map_location=device)

model = GPTModel(GPT_CONFIG_124M)
model.load_state_dict(checkpoint["model_state_dict"])

optimizer = torch.optim.AdamW(model.parameters(), lr=5e-4, weight_decay=0.1)
optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
model.train();
```

> **Bài tập 5.3**
> Đâu là cách chỉnh các thiết lập trong `generate` để ép tính tất định (deterministic), tức là loại bỏ lấy mẫu ngẫu nhiên để mô hình sinh ra một output giống y hệt mọi lần như `generate_simple`?

> **Bài tập 5.4**
> Sau khi lưu trọng số, nạp lại model và optimizer ở session mới hoặc notebook, tiếp tục pretrain mô hình đó bằng hàm `train_model_simple` thêm 1 epoch nữa.

## 5.5 Nạp trọng số tiền huấn luyện từ OpenAI

Vừa rồi, chúng ta đã huấn luyện một mô hình GPT-2 nhỏ qua một tập truyện ngắn. Nó giúp ta tập trung nắm kiến thức cơ bản mà không yêu cầu cao tài nguyên tính toán.

May mắn thay, OpenAI công khai chia sẻ các trọng số GPT-2 của họ, tránh việc chúng ta tốn bộn tiền vào việc tái huấn luyện một model trên tập văn bản lớn. Vậy nên ta hãy thử nạp các trọng số này vào lớp `GPTModel` để chạy sinh văn bản. Từ "trọng số" ở đây là các tham số trọng số trong thuộc tính `.weight` của Linear và Embedding PyTorch. Ta từng tiếp xúc với nó qua hàm `model.parameters()`. Trong Chương 6, ta sẽ tận dụng lại các tham số này để tinh chỉnh cho tác vụ phân loại và giúp mô hình tuân theo mệnh lệnh như ChatGPT.

Lưu ý rằng trọng số OpenAI gốc lưu trên TensorFlow, ta phải cài TensorFlow để tải trong Python. Đoạn mã dưới đây sử dụng công cụ `tqdm` để thanh tiến trình. Ta cần cài hai thư viện này thông qua terminal:

```bash
pip install tensorflow>=2.15.0  tqdm>=4.66
```

Đoạn code tải dài và đa phần là template lặp lại. Nên thay vì tốn trang giấy giải thích đoạn tải file từ internet, ta download hẳn module `gpt_download.py` từ GitHub sách:

```python
import urllib.request

url = (
    "https://raw.githubusercontent.com/rasbt/"
    "LLMs-from-scratch/main/ch05/"
    "01_main-chapter-code/gpt_download.py"
)
filename = url.split('/')[-1]
urllib.request.urlretrieve(url, filename)
```

Sau khi tải, nên kiểm tra lướt file xem tải thành công code Python chưa.

Sau đó, ta nhập khẩu hàm `download_and_load_gpt2` từ file này. Nó sẽ tải thông số cài đặt kiến trúc GPT-2 (`settings`) và tham số trọng số (`params`) vào session Python:

```python
from gpt_download import download_and_load_gpt2

settings, params = download_and_load_gpt2(
    model_size="124M", models_dir="gpt2"
)
```

Quá trình thực thi sẽ tải 7 file liên đới với GPT-2 cỡ 124M:

```
checkpoint: 100%|███████████████████████████| 77.0/77.0 [00:00<00:00, 
                                                         63.9kiB/s]
encoder.json: 100%|█████████████████████████| 1.04M/1.04M [00:00<00:00,
                                                           2.20MiB/s]
hprams.json: 100%|██████████████████████████| 90.0/90.0 [00:00<00:00,
                                                         78.3kiB/s]
model.ckpt.data-00000-of-00001: 100%|███████| 498M/498M [01:09<00:00,
                                                         7.16MiB/s]
...
```

> **LƯU Ý**
> Nếu lệnh tải không chạy, nó có thể là lỗi kết nối, mạng, hay OpenAI đổi link chia sẻ. Trong trường hợp đó hãy ghé repo github cuốn sách để cập nhật.

Mặc định chạy thành công, giờ kiểm tra `settings` và `params`:

```python
print("Settings:", settings)
print("Parameter dictionary keys:", params.keys())
```

Nội dung:

```
Settings: {'n_vocab': 50257, 'n_ctx': 1024, 'n_embd': 768, 'n_head': 12,
           'n_layer': 12}
Parameter dictionary keys: dict_keys(['blocks', 'b', 'g', 'wpe', 'wte'])
```

Cả hai đối tượng là các từ điển Python. Từ điển `settings` thiết lập kiến trúc LLM y như cách ta đã thủ công với `GPT_CONFIG_124M`. Dictionary `params` chứa các tensor weight gốc. Để xem logit nhúng (embedding), ví dụ:

```python
print(params["wte"])
print("Token embedding weight tensor dimensions:", params["wte"].shape)
```

Kết quả của trọng số token embedding:

```
[[-0.11010301 ... -0.1363697   0.01506208   0.04531523]
 [ 0.04034033 ...  0.08605453  0.00253983   0.04318958]
 [-0.12746179  ...  0.08991534 -0.12972379 -0.08785918]
 ...
 [-0.04453601 ...   0.10435229  0.09783269 -0.06952604]
 [ 0.1860082  ...  -0.09625227  0.07847701 -0.02245961]
 [ 0.05135201 ...   0.00704835  0.15519823  0.12067825]]
Token embedding weight tensor dimensions: (50257, 768)
```

Ta đã dùng mô hình nhỏ nhất (gpt2-small "124M"). OpenAI cũng chia sẻ các mẫu 355M, 774M, và 1558M. Nhìn chung kiến trúc LLM cho các dòng máy to hay nhỏ này đều giống hệt nhau ở các nền tảng căn bản (Hình 5.17), chỉ khác ở hệ số nhân độ lớn và độ sâu khối Transformer và vector nhúng. Vì vậy đoạn mã từ giờ tương thích với mọi kích cỡ máy.

[Hình 5.17: Khái quát các hệ máy GPT-2, thay đổi hệ số vector nhúng (embd) và số lượng lần nhân bản Transformer Block/Attention heads]

Sau khi nạp xong GPT-2 về bộ nhớ, bước tiếp theo là đẩy nội dung `settings` và `params` lên class `GPTModel`. Bước 1, thiết lập thay đổi giữa các size mô hình:

```python
model_configs = {
    "gpt2-small (124M)": {"emb_dim": 768, "n_layers": 12, "n_heads": 12},
    "gpt2-medium (355M)": {"emb_dim": 1024, "n_layers": 24, "n_heads": 16},
    "gpt2-large (774M)": {"emb_dim": 1280, "n_layers": 36, "n_heads": 20},
    "gpt2-xl (1558M)": {"emb_dim": 1600, "n_layers": 48, "n_heads": 25},
}
```

Giả sử ta dùng "gpt2-small (124M)", ta cập nhật thông số `NEW_CONFIG` từ config `GPT_CONFIG_124M` đầu chương:

```python
model_name = "gpt2-small (124M)"
NEW_CONFIG = GPT_CONFIG_124M.copy()
NEW_CONFIG.update(model_configs[model_name])
```

Vì `context_length` ta dùng lúc đầu là 256, còn bản chính của GPT là 1024 nên ta cũng update nó:

```python
NEW_CONFIG.update({"context_length": 1024})
```

Tương tự, OpenAI dùng vector `bias` cho query, key, value matrix, cái mà chúng ta đặt False từ trước vì không thấy cải thiện độ ưu việt LLM. Nhưng để xài bộ pretrain OpenAI, ta bắt buộc bật lên vì cần cấu trúc tương ứng 1-1 với weight array:

```python
NEW_CONFIG.update({"qkv_bias": True})
```

Xong, giờ khởi tạo cái mới:

```python
gpt = GPTModel(NEW_CONFIG)
gpt.eval()
```

Lúc này, nó sở hữu số lượng weight vector random. Công đoạn cuối cùng, hãy ghi đè mớ random bằng các array chính gốc từ biến `params`. Trước đó, hãy code 1 hàm gán thông minh (check shape) giữa hai array (`left` và `right`):

```python
def assign(left, right):
    if left.shape != right.shape:
        raise ValueError(f"Shape mismatch. Left: {left.shape}, "
                          "Right: {right.shape}"
        )
    return torch.nn.Parameter(torch.tensor(right))
```

Bây giờ ta ánh xạ tất cả:

**Listing 5.5: Nạp trọng số OpenAI vào code model của ta**

```python
import numpy as np

def load_weights_into_gpt(gpt, params):          
    gpt.pos_emb.weight = assign(gpt.pos_emb.weight, params['wpe'])
    gpt.tok_emb.weight = assign(gpt.tok_emb.weight, params['wte'])
    
    for b in range(len(params["blocks"])):    
        q_w, k_w, v_w = np.split(                           
            (params["blocks"][b]["attn"]["c_attn"])["w"], 3, axis=-1)
        gpt.trf_blocks[b].att.W_query.weight = assign(
            gpt.trf_blocks[b].att.W_query.weight, q_w.T)
        gpt.trf_blocks[b].att.W_key.weight = assign(
            gpt.trf_blocks[b].att.W_key.weight, k_w.T)
        gpt.trf_blocks[b].att.W_value.weight = assign(
            gpt.trf_blocks[b].att.W_value.weight, v_w.T)
            
        q_b, k_b, v_b = np.split(
            (params["blocks"][b]["attn"]["c_attn"])["b"], 3, axis=-1)
        gpt.trf_blocks[b].att.W_query.bias = assign(
            gpt.trf_blocks[b].att.W_query.bias, q_b)
        gpt.trf_blocks[b].att.W_key.bias = assign(
            gpt.trf_blocks[b].att.W_key.bias, k_b)
        gpt.trf_blocks[b].att.W_value.bias = assign(
            gpt.trf_blocks[b].att.W_value.bias, v_b)
            
        gpt.trf_blocks[b].att.out_proj.weight = assign(
            gpt.trf_blocks[b].att.out_proj.weight, 
            params["blocks"][b]["attn"]["c_proj"]["w"].T)
        gpt.trf_blocks[b].att.out_proj.bias = assign(
            gpt.trf_blocks[b].att.out_proj.bias, 
            params["blocks"][b]["attn"]["c_proj"]["b"])
            
        gpt.trf_blocks[b].ff.layers[0].weight = assign(
            gpt.trf_blocks[b].ff.layers[0].weight, 
            params["blocks"][b]["mlp"]["c_fc"]["w"].T)
        gpt.trf_blocks[b].ff.layers[0].bias = assign(
            gpt.trf_blocks[b].ff.layers[0].bias, 
            params["blocks"][b]["mlp"]["c_fc"]["b"])
        gpt.trf_blocks[b].ff.layers[2].weight = assign(
            gpt.trf_blocks[b].ff.layers[2].weight, 
            params["blocks"][b]["mlp"]["c_proj"]["w"].T)
        gpt.trf_blocks[b].ff.layers[2].bias = assign(
            gpt.trf_blocks[b].ff.layers[2].bias, 
            params["blocks"][b]["mlp"]["c_proj"]["b"])
            
        gpt.trf_blocks[b].norm1.scale = assign(
            gpt.trf_blocks[b].norm1.scale, 
            params["blocks"][b]["ln_1"]["g"])
        gpt.trf_blocks[b].norm1.shift = assign(
            gpt.trf_blocks[b].norm1.shift, 
            params["blocks"][b]["ln_1"]["b"])
        gpt.trf_blocks[b].norm2.scale = assign(
            gpt.trf_blocks[b].norm2.scale, 
            params["blocks"][b]["ln_2"]["g"])
        gpt.trf_blocks[b].norm2.shift = assign(
            gpt.trf_blocks[b].norm2.shift, 
            params["blocks"][b]["ln_2"]["b"])
            
    gpt.final_norm.scale = assign(gpt.final_norm.scale, params["g"])
    gpt.final_norm.shift = assign(gpt.final_norm.shift, params["b"])
    gpt.out_head.weight = assign(gpt.out_head.weight, params["wte"])   
```

> **LƯU Ý:** Mô hình GPT-2 nguyên gốc của OpenAI tái sử dụng trọng số embedding token cho lớp output để làm giảm số lượng tham số, đây là một kỹ thuật được biết đến với tên gọi "cột trọng số" (weight tying).

Quá trình map tên file vào đúng cấu trúc được dò tìm cẩn thận từ các class. `assign` sẽ rào lỗi cho ta. Hãy đưa nó vào hoạt động:

```python
load_weights_into_gpt(gpt, params)
gpt.to(device)
```

Giờ hãy chạy mô hình pretrain gốc với text generator mới nhất của ta để tận hưởng thành quả:

```python
torch.manual_seed(123)
token_ids = generate(
    model=gpt,
    idx=text_to_token_ids("Every effort moves you", tokenizer).to(device),
    max_new_tokens=25,
    context_size=NEW_CONFIG["context_length"],
    top_k=50,
    temperature=1.5
)

print("Output text:\n", token_ids_to_text(token_ids, tokenizer))
```

Dữ liệu đưa ra là:

```
Output text:
 Every effort moves you toward finding an ideal new way to practice 
something!
What makes us want to be on top of that?
```

Sự tự tin của mô hình qua kết quả ngôn ngữ tốt và rõ nghĩa là minh chứng việc gán load layer đã thành công mỹ mãn. Bước nhỏ xíu thôi cũng phá tan toàn bộ. Sau chương này, chúng ta sẽ làm việc sát sườn với `gpt` và tiếp tục tinh chỉnh (fine-tune) để xếp loại cảm xúc (classify) và tuân lệnh hướng dẫn (follow instruction).

## Tóm tắt chương 5
- Khi sinh ra chữ, LLM chỉ khạc ra một chữ duy nhất (1 token) một lần.
- Mặc định, tham số giải mã tham lam `greedy decoding` sẽ khiến máy móc chọn kết quả cao nhất mỗi lần khạc chữ.
- Ta có thể tăng tính nghệ thuật, tính thú vị qua sự đa dạng cho đầu ra nhờ `top-k` và bù độ nhiễu/nhiệt độ (`temperature scaling`).
- Tổn thất / Mất mát huấn luyện (Loss) đánh giá chất lượng từ.
- Tiền huấn luyện LLM liên quan đến việc thay đổi trọng số nhằm giảm sai số loss tập huấn luyện.
- Vòng lặp tiền huấn luyện cho LLM áp dụng cơ chế Cross entropy chuẩn và dùng AdamW như Deep Learning cơ bản.
- Train tự chủ trên kho dữ liệu siêu khủng vô cùng nhọc sức và đòi siêu server tính toán, thế nên nạp mô hình có sẵn tải từ Internet là kế pháp vẹn toàn, tối ưu so với mọi thứ.

> **Bài tập 5.5**
> Tính loss huấn luyện và xác thực của `GPTModel` với các trọng số từ OpenAI khi đưa cho nó đọc tập ngắn "The Verdict".

> **Bài tập 5.6**
> Thử nghiệm GPT-2 các độ lớn (VD: mẫu 1558 triệu) - sinh thử văn và so sánh với cỡ gốc (124M).

