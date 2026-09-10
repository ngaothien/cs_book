# Chương 3: Viết code cơ chế attention

Tại thời điểm này, bạn biết cách chuẩn bị văn bản đầu vào cho huấn luyện LLM bằng cách chia văn bản thành các token từ và con từ riêng lẻ, có thể được mã hóa thành biểu diễn vector, nhúng (embedding), cho LLM.

Bây giờ, chúng ta sẽ xem xét một phần không thể thiếu của chính kiến trúc LLM, cơ chế attention, như minh họa trong hình 3.1. Chúng ta sẽ chủ yếu xem xét cơ chế attention một cách riêng biệt và tập trung vào chúng ở cấp độ cơ chế. Sau đó, chúng ta sẽ viết code các phần còn lại của LLM xung quanh cơ chế self-attention để thấy nó hoạt động và tạo mô hình sinh văn bản.

*Chương này bao gồm:*
- *Lý do sử dụng cơ chế attention trong mạng nơ-ron*
- *Một framework self-attention cơ bản, tiến tới cơ chế self-attention nâng cao*
- *Một module causal attention cho phép LLM sinh từng token một*
- *Che (mask) ngẫu nhiên các trọng số attention đã chọn bằng dropout để giảm overfitting*
- *Xếp chồng nhiều module causal attention thành module multi-head attention*

[Hình 3.1: Ba giai đoạn chính của việc viết code LLM. Chương này tập trung vào bước 2 của giai đoạn 1: triển khai cơ chế attention, là phần không thể thiếu của kiến trúc LLM.]

Chúng ta sẽ triển khai bốn biến thể khác nhau của cơ chế attention, như minh họa trong hình 3.2. Các biến thể attention khác nhau này xây dựng trên nhau, và mục tiêu là đi đến triển khai nhỏ gọn và hiệu quả của multi-head attention mà sau đó chúng ta có thể cắm vào kiến trúc LLM mà chúng ta sẽ viết code trong chương tiếp theo.

[Hình 3.2: Hình mô tả các cơ chế attention khác nhau mà chúng ta sẽ viết code trong chương này, bắt đầu với phiên bản đơn giản hóa của self-attention trước khi thêm trọng số có thể huấn luyện. Cơ chế causal attention thêm mask vào self-attention cho phép LLM sinh một từ mỗi lần. Cuối cùng, multi-head attention tổ chức cơ chế attention thành nhiều head, cho phép mô hình nắm bắt các khía cạnh khác nhau của dữ liệu đầu vào song song.]

## 3.1 Vấn đề với mô hình hóa chuỗi dài

Trước khi đi sâu vào cơ chế self-attention ở trung tâm của LLM, hãy xem xét vấn đề với các kiến trúc trước LLM không bao gồm cơ chế attention. Giả sử chúng ta muốn phát triển mô hình dịch ngôn ngữ dịch văn bản từ ngôn ngữ này sang ngôn ngữ khác. Như hiển thị trong hình 3.3, chúng ta không thể đơn giản dịch văn bản từng từ do cấu trúc ngữ pháp trong ngôn ngữ nguồn và ngôn ngữ đích.

[Hình 3.3: Khi dịch văn bản từ ngôn ngữ này sang ngôn ngữ khác, chẳng hạn từ tiếng Đức sang tiếng Anh, không thể chỉ đơn thuần dịch từng từ. Thay vào đó, quá trình dịch đòi hỏi hiểu ngữ cảnh và căn chỉnh ngữ pháp.]

Để giải quyết vấn đề này, thông thường sử dụng mạng nơ-ron sâu với hai module con, encoder và decoder. Công việc của encoder là đọc vào và xử lý toàn bộ văn bản trước, sau đó decoder tạo ra văn bản đã dịch.

Trước sự ra đời của transformer, mạng nơ-ron hồi quy (recurrent neural network — RNN) là kiến trúc encoder-decoder phổ biến nhất cho dịch ngôn ngữ. RNN là loại mạng nơ-ron trong đó đầu ra từ các bước trước được đưa làm đầu vào cho bước hiện tại, làm cho chúng phù hợp với dữ liệu tuần tự như văn bản. Nếu bạn không quen thuộc với RNN, đừng lo — bạn không cần biết chi tiết hoạt động của RNN để theo dõi thảo luận này; trọng tâm của chúng ta ở đây là khái niệm tổng quát hơn của thiết lập encoder-decoder.

Trong RNN encoder-decoder, văn bản đầu vào được đưa vào encoder, xử lý nó tuần tự. Encoder cập nhật trạng thái ẩn (hidden state) — các giá trị nội bộ tại các lớp ẩn — ở mỗi bước, cố gắng nắm bắt toàn bộ ý nghĩa của câu đầu vào trong trạng thái ẩn cuối cùng, như minh họa trong hình 3.4. Decoder sau đó lấy trạng thái ẩn cuối cùng này để bắt đầu sinh câu đã dịch, từng từ một. Nó cũng cập nhật trạng thái ẩn ở mỗi bước, được cho là mang ngữ cảnh cần thiết cho dự đoán từ tiếp theo.

[Hình 3.4: Trước sự ra đời của mô hình transformer, RNN encoder-decoder là lựa chọn phổ biến cho dịch máy. Encoder nhận chuỗi token từ ngôn ngữ nguồn làm đầu vào, nơi trạng thái ẩn (lớp mạng nơ-ron trung gian) của encoder mã hóa biểu diễn nén của toàn bộ chuỗi đầu vào. Sau đó, decoder sử dụng trạng thái ẩn hiện tại để bắt đầu dịch, token này sang token khác.]

Mặc dù chúng ta không cần biết hoạt động bên trong của các RNN encoder-decoder này, ý tưởng chính ở đây là phần encoder xử lý toàn bộ văn bản đầu vào thành trạng thái ẩn (ô nhớ — memory cell). Decoder sau đó nhận trạng thái ẩn này để tạo đầu ra. Bạn có thể nghĩ trạng thái ẩn này như một vector nhúng, khái niệm chúng ta đã thảo luận trong chương 2.

Hạn chế lớn của RNN encoder-decoder là RNN không thể trực tiếp truy cập các trạng thái ẩn trước đó từ encoder trong giai đoạn giải mã. Do đó, nó chỉ dựa vào trạng thái ẩn hiện tại, đóng gói tất cả thông tin liên quan. Điều này có thể dẫn đến mất ngữ cảnh, đặc biệt trong các câu phức tạp nơi các phụ thuộc có thể trải dài khoảng cách dài.

May mắn thay, không cần thiết phải hiểu RNN để xây dựng LLM. Chỉ cần nhớ rằng RNN encoder-decoder có nhược điểm thúc đẩy thiết kế cơ chế attention.

## 3.2 Nắm bắt các phụ thuộc dữ liệu bằng cơ chế attention

Mặc dù RNN hoạt động tốt cho dịch câu ngắn, chúng không hoạt động tốt cho văn bản dài hơn vì chúng không có quyền truy cập trực tiếp vào các từ trước trong đầu vào. Một nhược điểm lớn trong phương pháp này là RNN phải ghi nhớ toàn bộ đầu vào đã mã hóa trong một trạng thái ẩn duy nhất trước khi truyền nó đến decoder (hình 3.4).

Do đó, các nhà nghiên cứu đã phát triển cơ chế attention Bahdanau cho RNN vào năm 2014 (đặt tên theo tác giả đầu tiên của bài báo tương ứng; để biết thêm thông tin, xem phụ lục B), sửa đổi RNN encoder-decoder sao cho decoder có thể chọn lọc truy cập các phần khác nhau của chuỗi đầu vào ở mỗi bước giải mã như minh họa trong hình 3.5.

[Hình 3.5: Sử dụng cơ chế attention, phần decoder sinh văn bản của mạng có thể truy cập tất cả token đầu vào một cách chọn lọc. Điều này có nghĩa là một số token đầu vào quan trọng hơn các token khác cho việc sinh một token đầu ra nhất định. Tầm quan trọng được xác định bởi trọng số attention, mà chúng ta sẽ tính toán sau. Lưu ý rằng hình này hiển thị ý tưởng tổng quát đằng sau attention và không mô tả triển khai chính xác của cơ chế Bahdanau, là phương pháp RNN nằm ngoài phạm vi cuốn sách này.]

Thú vị thay, chỉ ba năm sau, các nhà nghiên cứu phát hiện rằng kiến trúc RNN không cần thiết để xây dựng mạng nơ-ron sâu cho xử lý ngôn ngữ tự nhiên và đề xuất kiến trúc transformer gốc (đã thảo luận trong chương 1) bao gồm cơ chế self-attention lấy cảm hứng từ cơ chế attention Bahdanau.

Self-attention là cơ chế cho phép mỗi vị trí trong chuỗi đầu vào xem xét mức độ liên quan của, hoặc "chú ý đến", tất cả các vị trí khác trong cùng chuỗi khi tính toán biểu diễn của chuỗi. Self-attention là thành phần chính của các LLM đương đại dựa trên kiến trúc transformer, chẳng hạn như dòng GPT.

Chương này tập trung vào việc viết code và hiểu cơ chế self-attention này được sử dụng trong các mô hình giống GPT, như minh họa trong hình 3.6. Trong chương tiếp theo, chúng ta sẽ viết code các phần còn lại của LLM.

[Hình 3.6: Self-attention là cơ chế trong transformer được sử dụng để tính toán biểu diễn đầu vào hiệu quả hơn bằng cách cho phép mỗi vị trí trong chuỗi tương tác với và đánh giá tầm quan trọng của tất cả các vị trí khác trong cùng chuỗi. Trong chương này, chúng ta sẽ viết code cơ chế self-attention này từ đầu trước khi viết code các phần còn lại của LLM giống GPT trong chương tiếp theo.]

## 3.3 Chú ý đến các phần khác nhau của đầu vào với self-attention

Bây giờ chúng ta sẽ đề cập đến hoạt động bên trong của cơ chế self-attention và học cách viết code nó từ đầu. Self-attention đóng vai trò là nền tảng của mọi LLM dựa trên kiến trúc transformer. Chủ đề này có thể đòi hỏi nhiều sự tập trung và chú ý (không chơi chữ), nhưng một khi bạn nắm được nền tảng, bạn sẽ chinh phục được một trong những khía cạnh khó nhất của cuốn sách này và triển khai LLM nói chung.

Vì self-attention có thể trông phức tạp, đặc biệt nếu bạn gặp nó lần đầu tiên, chúng ta sẽ bắt đầu bằng cách xem xét phiên bản đơn giản hóa của nó. Sau đó chúng ta sẽ triển khai cơ chế self-attention với trọng số có thể huấn luyện được sử dụng trong LLM.

### 3.3.1 Cơ chế self-attention đơn giản không có trọng số huấn luyện

Hãy bắt đầu bằng cách triển khai biến thể đơn giản hóa của self-attention, không có bất kỳ trọng số huấn luyện nào, như tóm tắt trong hình 3.7. Mục tiêu là minh họa một số khái niệm chính trong self-attention trước khi thêm trọng số huấn luyện.

> **"Self" trong self-attention**
>
> Trong self-attention, "self" đề cập đến khả năng của cơ chế tính toán trọng số attention bằng cách liên hệ các vị trí khác nhau trong cùng một chuỗi đầu vào duy nhất. Nó đánh giá và học các mối quan hệ và phụ thuộc giữa các phần khác nhau của chính đầu vào, chẳng hạn như các từ trong câu hoặc pixel trong ảnh.
>
> Điều này trái ngược với cơ chế attention truyền thống, nơi trọng tâm là các mối quan hệ giữa các phần tử của hai chuỗi khác nhau, chẳng hạn như trong mô hình chuỗi-sang-chuỗi nơi attention có thể nằm giữa chuỗi đầu vào và chuỗi đầu ra, chẳng hạn như ví dụ được mô tả trong hình 3.5.

[Hình 3.7: Mục tiêu của self-attention là tính toán vector ngữ cảnh cho mỗi phần tử đầu vào kết hợp thông tin từ tất cả các phần tử đầu vào khác. Trong ví dụ này, chúng ta tính toán vector ngữ cảnh z(2). Tầm quan trọng hoặc đóng góp của mỗi phần tử đầu vào cho tính toán z(2) được xác định bởi trọng số attention α21 đến α2T. Khi tính toán z(2), trọng số attention được tính với tôn trọng phần tử đầu vào x(2) và tất cả các đầu vào khác.]

Hình 3.7 hiển thị chuỗi đầu vào, ký hiệu là x, bao gồm T phần tử được biểu diễn là x(1) đến x(T). Chuỗi này thường đại diện cho văn bản, chẳng hạn như một câu, đã được chuyển đổi thành token embedding.

Ví dụ, xem xét văn bản đầu vào như "Your journey starts with one step." Trong trường hợp này, mỗi phần tử của chuỗi, chẳng hạn như x(1), tương ứng với vector nhúng d chiều đại diện cho một token cụ thể, như "Your." Hình 3.7 hiển thị các vector đầu vào này dưới dạng nhúng ba chiều.

Trong self-attention, mục tiêu của chúng ta là tính toán vector ngữ cảnh z(i) cho mỗi phần tử x(i) trong chuỗi đầu vào. Vector ngữ cảnh có thể được hiểu như vector nhúng được làm giàu.

Để minh họa khái niệm này, hãy tập trung vào vector nhúng của phần tử đầu vào thứ hai, x(2) (tương ứng với token "journey"), và vector ngữ cảnh tương ứng, z(2), hiển thị ở phía dưới hình 3.7. Vector ngữ cảnh nâng cao này, z(2), là nhúng chứa thông tin về x(2) và tất cả các phần tử đầu vào khác, x(1) đến x(T).

Vector ngữ cảnh đóng vai trò quan trọng trong self-attention. Mục đích của chúng là tạo biểu diễn được làm giàu cho mỗi phần tử trong chuỗi đầu vào (như một câu) bằng cách kết hợp thông tin từ tất cả các phần tử khác trong chuỗi (hình 3.7). Điều này là thiết yếu trong LLM, cần hiểu mối quan hệ và mức độ liên quan của các từ trong câu với nhau. Sau đó, chúng ta sẽ thêm trọng số có thể huấn luyện giúp LLM học cách xây dựng các vector ngữ cảnh này sao cho chúng phù hợp để LLM sinh token tiếp theo. Nhưng trước tiên, hãy triển khai cơ chế self-attention đơn giản hóa để tính toán các trọng số này và vector ngữ cảnh kết quả từng bước một.

Xem xét câu đầu vào sau, đã được nhúng thành vector ba chiều (xem chương 2). Tôi đã chọn chiều nhúng nhỏ để đảm bảo nó vừa trên trang mà không xuống dòng:

```python
import torch
inputs = torch.tensor(
  [[0.43, 0.15, 0.89], # Your     (x^1)
   [0.55, 0.87, 0.66], # journey  (x^2)
   [0.57, 0.85, 0.64], # starts   (x^3)
   [0.22, 0.58, 0.33], # with     (x^4)
   [0.77, 0.25, 0.10], # one      (x^5)
   [0.05, 0.80, 0.55]] # step     (x^6)
)
```

Bước đầu tiên của triển khai self-attention là tính toán các giá trị trung gian ω, được gọi là điểm attention (attention score), như minh họa trong hình 3.8. Do giới hạn không gian, hình hiển thị các giá trị của tensor đầu vào trước ở dạng cắt ngắn; ví dụ, 0.87 được cắt thành 0.8. Trong phiên bản cắt ngắn này, nhúng của từ "journey" và "starts" có thể trông tương tự do ngẫu nhiên.

[Hình 3.8: Mục tiêu tổng thể là minh họa tính toán vector ngữ cảnh z(2) sử dụng phần tử đầu vào thứ hai, x(2) làm truy vấn. Hình này hiển thị bước trung gian đầu tiên, tính toán điểm attention ω giữa truy vấn x(2) và tất cả các phần tử đầu vào khác dưới dạng tích vô hướng (dot product). (Lưu ý rằng các số được cắt ngắn xuống một chữ số sau dấu thập phân để giảm lộn xộn trực quan.)]

Hình 3.8 minh họa cách chúng ta tính toán điểm attention trung gian giữa token truy vấn và mỗi token đầu vào. Chúng ta xác định các điểm này bằng cách tính tích vô hướng (dot product) của truy vấn, x(2), với mọi token đầu vào khác:

```python
query = inputs[1]                           # Token đầu vào thứ hai làm truy vấn
attn_scores_2 = torch.empty(inputs.shape[0])
for i, x_i in enumerate(inputs):
    attn_scores_2[i] = torch.dot(x_i, query)
print(attn_scores_2)
```

Các điểm attention được tính toán là:

```
tensor([0.9544, 1.4950, 1.4754, 0.8434, 0.7070, 1.0865])
```

> **Hiểu tích vô hướng**
>
> Tích vô hướng (dot product) về cơ bản là cách ngắn gọn để nhân hai vector theo từng phần tử và sau đó cộng các tích lại, có thể được minh họa như sau:
>
> ```python
> res = 0.
> for idx, element in enumerate(inputs[0]):
>     res += inputs[0][idx] * query[idx]
> print(res)
> print(torch.dot(inputs[0], query))
> ```
>
> Đầu ra xác nhận rằng tổng phép nhân theo phần tử cho kết quả giống tích vô hướng:
>
> ```
> tensor(0.9544)
> tensor(0.9544)
> ```
>
> Ngoài việc xem phép tích vô hướng như công cụ toán học kết hợp hai vector để tạo giá trị vô hướng, tích vô hướng là thước đo sự tương tự vì nó định lượng mức độ căn chỉnh của hai vector: tích vô hướng cao hơn chỉ ra mức độ căn chỉnh hoặc tương tự lớn hơn giữa hai vector. Trong ngữ cảnh cơ chế self-attention, tích vô hướng xác định mức độ mà mỗi phần tử trong chuỗi tập trung vào, hoặc "chú ý đến", bất kỳ phần tử nào khác: tích vô hướng càng cao, sự tương tự và điểm attention giữa hai phần tử càng cao.

Trong bước tiếp theo, như hiển thị trong hình 3.9, chúng ta chuẩn hóa mỗi điểm attention mà chúng ta đã tính toán trước đó. Mục tiêu chính đằng sau chuẩn hóa là để có được trọng số attention có tổng bằng 1. Sự chuẩn hóa này là quy ước hữu ích cho việc diễn giải và duy trì sự ổn định huấn luyện trong LLM. Đây là phương pháp đơn giản để đạt được bước chuẩn hóa này:

```python
attn_weights_2_tmp = attn_scores_2 / attn_scores_2.sum()
print("Attention weights:", attn_weights_2_tmp)
print("Sum:", attn_weights_2_tmp.sum())
```

Như đầu ra hiển thị, trọng số attention giờ có tổng bằng 1:

```
Attention weights: tensor([0.1455, 0.2278, 0.2249, 0.1285, 0.1077, 0.1656])
Sum: tensor(1.0000)
```

[Hình 3.9: Sau khi tính toán điểm attention ω21 đến ω2T với tôn trọng truy vấn đầu vào x(2), bước tiếp theo là lấy trọng số attention α21 đến α2T bằng cách chuẩn hóa điểm attention.]

Trong thực tế, phổ biến hơn và nên sử dụng hàm softmax cho chuẩn hóa. Phương pháp này tốt hơn trong việc quản lý các giá trị cực đoan và cung cấp các thuộc tính gradient thuận lợi hơn trong quá trình huấn luyện. Đây là triển khai cơ bản của hàm softmax để chuẩn hóa điểm attention:

```python
def softmax_naive(x):
    return torch.exp(x) / torch.exp(x).sum(dim=0)

attn_weights_2_naive = softmax_naive(attn_scores_2)
print("Attention weights:", attn_weights_2_naive)
print("Sum:", attn_weights_2_naive.sum())
```

Như đầu ra hiển thị, hàm softmax cũng đáp ứng mục tiêu và chuẩn hóa trọng số attention sao cho chúng có tổng bằng 1:

```
Attention weights: tensor([0.1385, 0.2379, 0.2333, 0.1240, 0.1082, 0.1581])
Sum: tensor(1.)
```

Ngoài ra, hàm softmax đảm bảo rằng trọng số attention luôn dương. Điều này làm cho đầu ra có thể diễn giải được như xác suất hoặc tầm quan trọng tương đối, nơi trọng số cao hơn chỉ ra tầm quan trọng lớn hơn.

Lưu ý rằng triển khai softmax ngây thơ này (softmax_naive) có thể gặp vấn đề bất ổn số, chẳng hạn như tràn trên (overflow) và tràn dưới (underflow), khi xử lý giá trị đầu vào lớn hoặc nhỏ. Do đó, trong thực tế, nên sử dụng triển khai softmax của PyTorch, đã được tối ưu hóa mạnh mẽ cho hiệu suất:

```python
attn_weights_2 = torch.softmax(attn_scores_2, dim=0)
print("Attention weights:", attn_weights_2)
print("Sum:", attn_weights_2.sum())
```

Trong trường hợp này, nó cho kết quả giống hàm softmax_naive trước đó:

```
Attention weights: tensor([0.1385, 0.2379, 0.2333, 0.1240, 0.1082, 0.1581])
Sum: tensor(1.)
```

Bây giờ khi chúng ta đã tính toán trọng số attention đã chuẩn hóa, chúng ta sẵn sàng cho bước cuối cùng, như hiển thị trong hình 3.10: tính toán vector ngữ cảnh z(2) bằng cách nhân các token đầu vào đã nhúng, x(i), với trọng số attention tương ứng và sau đó cộng các vector kết quả. Vì vậy, vector ngữ cảnh z(2) là tổng có trọng số của tất cả vector đầu vào, có được bằng cách nhân mỗi vector đầu vào với trọng số attention tương ứng:

```python
query = inputs[1]        # Token đầu vào thứ hai là truy vấn.
context_vec_2 = torch.zeros(query.shape)
for i, x_i in enumerate(inputs):
    context_vec_2 += attn_weights_2[i]*x_i
print(context_vec_2)
```

Kết quả tính toán này là:

```
tensor([0.4419, 0.6515, 0.5683])
```

[Hình 3.10: Bước cuối cùng, sau khi tính toán và chuẩn hóa điểm attention để có trọng số attention cho truy vấn x(2), là tính toán vector ngữ cảnh z(2). Vector ngữ cảnh này là tổ hợp của tất cả vector đầu vào x(1) đến x(T) được đánh trọng số bởi trọng số attention.]

Tiếp theo, chúng ta sẽ tổng quát hóa quy trình này để tính toán tất cả vector ngữ cảnh đồng thời.

### 3.3.2 Tính toán trọng số attention cho tất cả token đầu vào

Cho đến nay, chúng ta đã tính toán trọng số attention và vector ngữ cảnh cho đầu vào 2, như hiển thị trong hàng được đánh dấu trong hình 3.11. Bây giờ hãy mở rộng tính toán này để tính trọng số attention và vector ngữ cảnh cho tất cả đầu vào.

[Hình 3.11: Hàng được đánh dấu hiển thị trọng số attention cho phần tử đầu vào thứ hai làm truy vấn. Bây giờ chúng ta sẽ tổng quát hóa tính toán để có tất cả trọng số attention khác. (Xin lưu ý rằng các số trong hình này được cắt ngắn xuống hai chữ số sau dấu thập phân để giảm lộn xộn trực quan. Giá trị trong mỗi hàng nên cộng lại bằng 1.0 hoặc 100%.)]

Chúng ta theo ba bước giống như trước (xem hình 3.12), ngoại trừ chúng ta thực hiện vài sửa đổi trong code để tính toán tất cả vector ngữ cảnh thay vì chỉ vector thứ hai, z(2):

```python
attn_scores = torch.empty(6, 6)
for i, x_i in enumerate(inputs):
    for j, x_j in enumerate(inputs):
        attn_scores[i, j] = torch.dot(x_i, x_j)
print(attn_scores)
```

[Hình 3.12: Trong bước 1, chúng ta thêm vòng lặp for bổ sung để tính tích vô hướng cho tất cả các cặp đầu vào.]

Điểm attention kết quả là:

```
tensor([[0.9995, 0.9544, 0.9422, 0.4753, 0.4576, 0.6310],
        [0.9544, 1.4950, 1.4754, 0.8434, 0.7070, 1.0865],
        [0.9422, 1.4754, 1.4570, 0.8296, 0.7154, 1.0605],
        [0.4753, 0.8434, 0.8296, 0.4937, 0.3474, 0.6565],
        [0.4576, 0.7070, 0.7154, 0.3474, 0.6654, 0.2935],
        [0.6310, 1.0865, 1.0605, 0.6565, 0.2935, 0.9450]])
```

Mỗi phần tử trong tensor đại diện cho điểm attention giữa mỗi cặp đầu vào, như chúng ta đã thấy trong hình 3.11. Lưu ý rằng các giá trị trong hình đó đã được chuẩn hóa, đó là lý do chúng khác với điểm attention chưa chuẩn hóa trong tensor trước. Chúng ta sẽ xử lý việc chuẩn hóa sau.

Khi tính toán tensor điểm attention trước, chúng ta đã sử dụng vòng lặp for trong Python. Tuy nhiên, vòng lặp for nói chung rất chậm, và chúng ta có thể đạt được kết quả tương tự bằng phép nhân ma trận:

```python
attn_scores = inputs @ inputs.T
print(attn_scores)
```

Chúng ta có thể xác nhận trực quan rằng kết quả giống như trước:

```
tensor([[0.9995, 0.9544, 0.9422, 0.4753, 0.4576, 0.6310],
        [0.9544, 1.4950, 1.4754, 0.8434, 0.7070, 1.0865],
        [0.9422, 1.4754, 1.4570, 0.8296, 0.7154, 1.0605],
        [0.4753, 0.8434, 0.8296, 0.4937, 0.3474, 0.6565],
        [0.4576, 0.7070, 0.7154, 0.3474, 0.6654, 0.2935],
        [0.6310, 1.0865, 1.0605, 0.6565, 0.2935, 0.9450]])
```

Trong bước 2 của hình 3.12, chúng ta chuẩn hóa mỗi hàng sao cho giá trị trong mỗi hàng có tổng bằng 1:

```python
attn_weights = torch.softmax(attn_scores, dim=-1)
print(attn_weights)
```

Trả về tensor trọng số attention sau khớp với giá trị trong hình 3.10:

```
tensor([[0.2098, 0.2006, 0.1981, 0.1242, 0.1220, 0.1452],
        [0.1385, 0.2379, 0.2333, 0.1240, 0.1082, 0.1581],
        [0.1390, 0.2369, 0.2326, 0.1242, 0.1108, 0.1565],
        [0.1435, 0.2074, 0.2046, 0.1462, 0.1263, 0.1720],
        [0.1526, 0.1958, 0.1975, 0.1367, 0.1879, 0.1295],
        [0.1385, 0.2184, 0.2128, 0.1420, 0.0988, 0.1896]])
```

Trong ngữ cảnh sử dụng PyTorch, tham số `dim` trong các hàm như `torch.softmax` chỉ định chiều của tensor đầu vào mà hàm sẽ được tính toán. Bằng cách đặt `dim=-1`, chúng ta hướng dẫn hàm softmax áp dụng chuẩn hóa dọc theo chiều cuối cùng của tensor attn_scores. Nếu attn_scores là tensor hai chiều (ví dụ, với shape [hàng, cột]), nó sẽ chuẩn hóa qua các cột sao cho giá trị trong mỗi hàng (tổng qua chiều cột) có tổng bằng 1.

Chúng ta có thể xác minh rằng tất cả các hàng thực sự đều có tổng bằng 1:

```python
row_2_sum = sum([0.1385, 0.2379, 0.2333, 0.1240, 0.1082, 0.1581])
print("Row 2 sum:", row_2_sum)
print("All row sums:", attn_weights.sum(dim=-1))
```

Kết quả là:

```
Row 2 sum: 1.0
All row sums: tensor([1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000])
```

Trong bước thứ ba và cuối cùng của hình 3.12, chúng ta sử dụng trọng số attention này để tính toán tất cả vector ngữ cảnh qua phép nhân ma trận:

```python
all_context_vecs = attn_weights @ inputs
print(all_context_vecs)
```

Trong tensor đầu ra kết quả, mỗi hàng chứa vector ngữ cảnh ba chiều:

```
tensor([[0.4421, 0.5931, 0.5790],
        [0.4419, 0.6515, 0.5683],
        [0.4431, 0.6496, 0.5671],
        [0.4304, 0.6298, 0.5510],
        [0.4671, 0.5910, 0.5266],
        [0.4177, 0.6503, 0.5645]])
```

Chúng ta có thể kiểm tra lại rằng code đúng bằng cách so sánh hàng thứ hai với vector ngữ cảnh z(2) mà chúng ta đã tính toán trong phần 3.3.1:

```python
print("Previous 2nd context vector:", context_vec_2)
```

Dựa trên kết quả, chúng ta có thể thấy rằng context_vec_2 đã tính toán trước đó khớp chính xác với hàng thứ hai trong tensor trước:

```
Previous 2nd context vector: tensor([0.4419, 0.6515, 0.5683])
```

Đây kết thúc phần hướng dẫn code về cơ chế self-attention đơn giản. Tiếp theo, chúng ta sẽ thêm trọng số có thể huấn luyện, cho phép LLM học từ dữ liệu và cải thiện hiệu suất trên các tác vụ cụ thể.

## 3.4 Triển khai self-attention với trọng số huấn luyện

Bước tiếp theo của chúng ta sẽ là triển khai cơ chế self-attention được sử dụng trong kiến trúc transformer gốc, mô hình GPT, và hầu hết các LLM phổ biến khác. Cơ chế self-attention này còn được gọi là scaled dot-product attention. Hình 3.13 hiển thị cách cơ chế self-attention này phù hợp trong ngữ cảnh rộng hơn của triển khai LLM.

[Hình 3.13: Trước đó, chúng ta đã viết code cơ chế attention đơn giản hóa để hiểu cơ chế cơ bản đằng sau cơ chế attention. Bây giờ, chúng ta thêm trọng số huấn luyện vào cơ chế attention này. Sau đó, chúng ta sẽ mở rộng cơ chế self-attention này bằng cách thêm causal mask và nhiều head.]

Như minh họa trong hình 3.13, cơ chế self-attention với trọng số huấn luyện xây dựng trên các khái niệm trước: chúng ta muốn tính toán vector ngữ cảnh dưới dạng tổng có trọng số trên các vector đầu vào cụ thể cho phần tử đầu vào nhất định. Như bạn sẽ thấy, chỉ có những khác biệt nhỏ so với cơ chế self-attention cơ bản mà chúng ta đã viết code trước đó.

Sự khác biệt đáng chú ý nhất là sự giới thiệu các ma trận trọng số được cập nhật trong quá trình huấn luyện mô hình. Các ma trận trọng số có thể huấn luyện này rất quan trọng để mô hình (cụ thể, module attention bên trong mô hình) có thể học cách tạo ra vector ngữ cảnh "tốt". (Chúng ta sẽ huấn luyện LLM trong chương 5.)

Chúng ta sẽ giải quyết cơ chế self-attention này trong hai phần phụ. Đầu tiên, chúng ta sẽ viết code từng bước như trước. Thứ hai, chúng ta sẽ tổ chức code thành lớp Python nhỏ gọn có thể được nhập vào kiến trúc LLM.

### 3.4.1 Tính toán trọng số attention từng bước

Chúng ta sẽ triển khai cơ chế self-attention từng bước bằng cách giới thiệu ba ma trận trọng số huấn luyện Wq, Wk, và Wv. Ba ma trận này được sử dụng để chiếu (project) các token đầu vào đã nhúng, x(i), thành vector truy vấn (query), khóa (key), và giá trị (value), tương ứng, như minh họa trong hình 3.14.

[Hình 3.14: Trong bước đầu tiên của cơ chế self-attention với ma trận trọng số huấn luyện, chúng ta tính toán vector truy vấn (q), khóa (k), và giá trị (v) cho các phần tử đầu vào x. Tương tự các phần trước, chúng ta chỉ định đầu vào thứ hai, x(2), làm đầu vào truy vấn. Vector truy vấn q(2) được lấy qua phép nhân ma trận giữa đầu vào x(2) và ma trận trọng số Wq. Tương tự, chúng ta lấy vector khóa và giá trị qua phép nhân ma trận liên quan đến ma trận trọng số Wk và Wv.]

Trước đó, chúng ta đã định nghĩa phần tử đầu vào thứ hai x(2) làm truy vấn khi tính toán trọng số attention đơn giản hóa để tính vector ngữ cảnh z(2). Sau đó chúng ta đã tổng quát hóa điều này để tính toán tất cả vector ngữ cảnh z(1) ... z(T) cho câu đầu vào sáu từ "Your journey starts with one step."

Tương tự, chúng ta bắt đầu ở đây bằng cách chỉ tính toán một vector ngữ cảnh, z(2), cho mục đích minh họa. Chúng ta sau đó sẽ sửa đổi code này để tính toán tất cả vector ngữ cảnh.

Hãy bắt đầu bằng cách định nghĩa vài biến:

```python
x_2 = inputs[1]           # Phần tử đầu vào thứ hai
d_in = inputs.shape[1]    # Kích thước nhúng đầu vào, d=3
d_out = 2                 # Kích thước nhúng đầu ra, d_out=2
```

Lưu ý rằng trong mô hình giống GPT, chiều đầu vào và đầu ra thường giống nhau, nhưng để dễ theo dõi tính toán, chúng ta sẽ sử dụng chiều đầu vào (d_in=3) và đầu ra (d_out=2) khác nhau ở đây.

Tiếp theo, chúng ta khởi tạo ba ma trận trọng số Wq, Wk, và Wv hiển thị trong hình 3.14:

```python
torch.manual_seed(123)
W_query = torch.nn.Parameter(torch.rand(d_in, d_out), requires_grad=False)
W_key   = torch.nn.Parameter(torch.rand(d_in, d_out), requires_grad=False)
W_value = torch.nn.Parameter(torch.rand(d_in, d_out), requires_grad=False)
```

Chúng ta đặt `requires_grad=False` để giảm lộn xộn trong đầu ra, nhưng nếu chúng ta sử dụng ma trận trọng số cho huấn luyện mô hình, chúng ta sẽ đặt `requires_grad=True` để cập nhật các ma trận này trong quá trình huấn luyện mô hình.

Tiếp theo, chúng ta tính toán vector truy vấn, khóa, và giá trị:

```python
query_2 = x_2 @ W_query
key_2 = x_2 @ W_key
value_2 = x_2 @ W_value
print(query_2)
```

Đầu ra cho kết quả truy vấn là vector hai chiều vì chúng ta đặt số cột của ma trận trọng số tương ứng, qua d_out, là 2:

```
tensor([0.4306, 1.4551])
```

> **Tham số trọng số so với trọng số attention**
>
> Trong ma trận trọng số W, thuật ngữ "trọng số" (weight) viết tắt cho "tham số trọng số" (weight parameters), các giá trị của mạng nơ-ron được tối ưu hóa trong quá trình huấn luyện. Điều này không nên nhầm lẫn với trọng số attention. Như chúng ta đã thấy, trọng số attention xác định mức độ mà vector ngữ cảnh phụ thuộc vào các phần khác nhau của đầu vào (nghĩa là, mức độ mạng tập trung vào các phần khác nhau của đầu vào).
>
> Tóm lại, tham số trọng số là các hệ số cơ bản, được học xác định kết nối của mạng, trong khi trọng số attention là các giá trị động, cụ thể theo ngữ cảnh.

Mặc dù mục tiêu tạm thời của chúng ta chỉ là tính toán một vector ngữ cảnh, z(2), chúng ta vẫn cần vector khóa và giá trị cho tất cả phần tử đầu vào vì chúng tham gia vào tính toán trọng số attention đối với truy vấn q(2) (xem hình 3.14).

Chúng ta có thể lấy tất cả khóa và giá trị qua phép nhân ma trận:

```python
keys = inputs @ W_key
values = inputs @ W_value
print("keys.shape:", keys.shape)
print("values.shape:", values.shape)
```

Như chúng ta có thể thấy từ đầu ra, chúng ta đã chiếu thành công sáu token đầu vào từ không gian nhúng ba chiều sang hai chiều:

```
keys.shape: torch.Size([6, 2])
values.shape: torch.Size([6, 2])
```

Bước thứ hai là tính toán điểm attention, như hiển thị trong hình 3.15.

[Hình 3.15: Tính toán điểm attention là phép tích vô hướng tương tự như chúng ta đã sử dụng trong cơ chế self-attention đơn giản hóa trong phần 3.3. Khía cạnh mới ở đây là chúng ta không trực tiếp tính tích vô hướng giữa các phần tử đầu vào mà sử dụng truy vấn và khóa được lấy bằng cách biến đổi đầu vào qua các ma trận trọng số tương ứng.]

Đầu tiên, hãy tính điểm attention ω22:

```python
keys_2 = keys[1]            # Nhớ rằng Python bắt đầu đánh chỉ mục từ 0
attn_score_22 = query_2.dot(keys_2)
print(attn_score_22)
```

Kết quả cho điểm attention chưa chuẩn hóa là:

```
tensor(1.8524)
```

Lại lần nữa, chúng ta có thể tổng quát hóa tính toán này cho tất cả điểm attention qua phép nhân ma trận:

```python
attn_scores_2 = query_2 @ keys.T      # Tất cả điểm attention cho truy vấn cho trước
print(attn_scores_2)
```

Như chúng ta có thể thấy, để kiểm tra nhanh, phần tử thứ hai trong đầu ra khớp với attn_score_22 mà chúng ta đã tính toán trước đó:

```
tensor([1.2705, 1.8524, 1.8111, 1.0795, 0.5577, 1.5440])
```

Bây giờ, chúng ta muốn đi từ điểm attention đến trọng số attention, như minh họa trong hình 3.16. Chúng ta tính toán trọng số attention bằng cách chia tỷ lệ (scaling) điểm attention và sử dụng hàm softmax. Tuy nhiên, bây giờ chúng ta chia tỷ lệ điểm attention bằng cách chia chúng cho căn bậc hai của chiều nhúng của khóa (lấy căn bậc hai về mặt toán học giống với lũy thừa 0.5):

```python
d_k = keys.shape[-1]
attn_weights_2 = torch.softmax(attn_scores_2 / d_k**0.5, dim=-1)
print(attn_weights_2)
```

[Hình 3.16: Sau khi tính toán điểm attention ω, bước tiếp theo là chuẩn hóa các điểm này sử dụng hàm softmax để có trọng số attention α.]

> **Lý do đằng sau scaled-dot product attention**
>
> Lý do chuẩn hóa bằng kích thước chiều nhúng là để cải thiện hiệu suất huấn luyện bằng cách tránh gradient nhỏ. Ví dụ, khi tăng chiều nhúng, thường lớn hơn 1.000 cho LLM giống GPT, tích vô hướng lớn có thể dẫn đến gradient rất nhỏ trong quá trình lan truyền ngược do hàm softmax được áp dụng cho chúng. Khi tích vô hướng tăng, hàm softmax hoạt động giống hàm bước (step function) hơn, dẫn đến gradient tiệm cận zero. Các gradient nhỏ này có thể làm chậm đáng kể việc học hoặc khiến huấn luyện bị đình trệ.
>
> Việc chia tỷ lệ bằng căn bậc hai của chiều nhúng là lý do tại sao cơ chế self-attention này còn được gọi là scaled-dot product attention.

Trọng số attention kết quả là:

```
tensor([0.1500, 0.2264, 0.2199, 0.1311, 0.0906, 0.1820])
```

Bây giờ, bước cuối cùng là tính toán vector ngữ cảnh, như minh họa trong hình 3.17. Tương tự khi chúng ta tính toán vector ngữ cảnh dưới dạng tổng có trọng số trên vector đầu vào (xem phần 3.3), giờ chúng ta tính toán vector ngữ cảnh dưới dạng tổng có trọng số trên vector giá trị. Ở đây, trọng số attention đóng vai trò là hệ số đánh trọng số cân nhắc tầm quan trọng tương ứng của mỗi vector giá trị. Cũng như trước, chúng ta có thể sử dụng phép nhân ma trận để lấy đầu ra trong một bước:

```python
context_vec_2 = attn_weights_2 @ values
print(context_vec_2)
```

[Hình 3.17: Trong bước cuối cùng của tính toán self-attention, chúng ta tính toán vector ngữ cảnh bằng cách kết hợp tất cả vector giá trị qua trọng số attention.]

Nội dung vector kết quả là:

```
tensor([0.3061, 0.8210])
```

Cho đến nay, chúng ta chỉ tính toán một vector ngữ cảnh đơn, z(2). Tiếp theo, chúng ta sẽ tổng quát hóa code để tính toán tất cả vector ngữ cảnh trong chuỗi đầu vào, z(1) đến z(T).

### 3.4.2 Triển khai lớp Python self-attention nhỏ gọn

Tại thời điểm này, chúng ta đã đi qua rất nhiều bước để tính toán đầu ra self-attention. Chúng ta làm điều đó chủ yếu cho mục đích minh họa để có thể đi qua từng bước một. Trong thực tế, với triển khai LLM trong chương tiếp theo trong đầu, việc tổ chức code này thành lớp Python là hữu ích, như hiển thị trong listing sau.

> **Tại sao query, key, và value?**
>
> Các thuật ngữ "khóa" (key), "truy vấn" (query), và "giá trị" (value) trong ngữ cảnh cơ chế attention được mượn từ lĩnh vực truy xuất thông tin và cơ sở dữ liệu, nơi các khái niệm tương tự được sử dụng để lưu trữ, tìm kiếm, và truy xuất thông tin.
>
> Truy vấn (query) tương tự như truy vấn tìm kiếm trong cơ sở dữ liệu. Nó đại diện cho mục hiện tại (ví dụ, từ hoặc token trong câu) mà mô hình tập trung vào hoặc cố gắng hiểu. Truy vấn được sử dụng để thăm dò các phần khác của chuỗi đầu vào để xác định mức attention cần dành cho chúng.
>
> Khóa (key) giống như khóa cơ sở dữ liệu được sử dụng cho đánh chỉ mục và tìm kiếm. Trong cơ chế attention, mỗi mục trong chuỗi đầu vào (ví dụ, mỗi từ trong câu) có khóa liên kết. Các khóa này được sử dụng để khớp với truy vấn.
>
> Giá trị (value) trong ngữ cảnh này tương tự giá trị trong cặp khóa-giá trị trong cơ sở dữ liệu. Nó đại diện cho nội dung hoặc biểu diễn thực tế của các mục đầu vào. Khi mô hình xác định được khóa nào (và do đó phần nào của đầu vào) phù hợp nhất với truy vấn (mục tập trung hiện tại), nó truy xuất giá trị tương ứng.

**Listing 3.1: Lớp self-attention nhỏ gọn**

```python
import torch.nn as nn

class SelfAttention_v1(nn.Module):
    def __init__(self, d_in, d_out):
        super().__init__()
        self.W_query = nn.Parameter(torch.rand(d_in, d_out))
        self.W_key   = nn.Parameter(torch.rand(d_in, d_out))
        self.W_value = nn.Parameter(torch.rand(d_in, d_out))

    def forward(self, x):
        keys = x @ self.W_key
        queries = x @ self.W_query
        values = x @ self.W_value
        attn_scores = queries @ keys.T  # omega
        attn_weights = torch.softmax(
            attn_scores / keys.shape[-1]**0.5, dim=-1
        )
        context_vec = attn_weights @ values
        return context_vec
```

Trong code PyTorch này, SelfAttention_v1 là lớp được dẫn xuất từ nn.Module, là khối xây dựng cơ bản của mô hình PyTorch cung cấp các chức năng cần thiết cho tạo và quản lý lớp mô hình.

Phương thức `__init__` khởi tạo ma trận trọng số huấn luyện (W_query, W_key, và W_value) cho truy vấn, khóa, và giá trị, mỗi cái chuyển đổi chiều đầu vào d_in sang chiều đầu ra d_out.

Trong lượt truyền xuôi (forward pass), sử dụng phương thức forward, chúng ta tính toán điểm attention (attn_scores) bằng cách nhân truy vấn và khóa, chuẩn hóa các điểm này sử dụng softmax. Cuối cùng, chúng ta tạo vector ngữ cảnh bằng cách đánh trọng số giá trị với các trọng số attention đã chuẩn hóa.

Chúng ta có thể sử dụng lớp này như sau:

```python
torch.manual_seed(123)
sa_v1 = SelfAttention_v1(d_in, d_out)
print(sa_v1(inputs))
```

Vì inputs chứa sáu vector nhúng, kết quả là ma trận lưu sáu vector ngữ cảnh:

```
tensor([[0.2996, 0.8053],
        [0.3061, 0.8210],
        [0.3058, 0.8203],
```

```
tensor([[0.2996, 0.8053],
        [0.3061, 0.8210],
        [0.3058, 0.8203],
        [0.2948, 0.7939],
        [0.2927, 0.7891],
        [0.2990, 0.8040]], grad_fn=<MmBackward0>)
```

Để kiểm tra nhanh, lưu ý rằng hàng thứ hai ([0.3061, 0.8210]) khớp với nội dung của context_vec_2 trong phần trước. Hình 3.18 tóm tắt cơ chế self-attention chúng ta vừa triển khai.

Self-attention liên quan đến ma trận trọng số huấn luyện Wq, Wk, và Wv. Các ma trận này biến đổi dữ liệu đầu vào thành truy vấn, khóa, và giá trị, tương ứng, là các thành phần quan trọng của cơ chế attention. Khi mô hình tiếp xúc với nhiều dữ liệu hơn trong quá trình huấn luyện, nó điều chỉnh các trọng số huấn luyện này, như chúng ta sẽ thấy trong các chương tiếp theo.

[Hình 3.18: Trong self-attention, chúng ta biến đổi vector đầu vào trong ma trận đầu vào X với ba ma trận trọng số, Wq, Wk, và Wv. Chúng ta tính toán ma trận trọng số attention dựa trên truy vấn (Q) và khóa (K) kết quả. Sử dụng trọng số attention và giá trị (V), chúng ta sau đó tính toán vector ngữ cảnh (Z). Để rõ ràng trực quan, chúng ta tập trung vào một văn bản đầu vào đơn với n token, không phải batch gồm nhiều đầu vào. Do đó, tensor đầu vào ba chiều được đơn giản hóa thành ma trận hai chiều trong ngữ cảnh này. Phương pháp này cho phép trực quan hóa và hiểu các quy trình liên quan dễ dàng hơn. Để nhất quán với các hình sau, các giá trị trong ma trận attention không mô tả trọng số attention thực tế. (Các số trong hình này được cắt ngắn xuống hai chữ số sau dấu thập phân để giảm lộn xộn trực quan. Giá trị trong mỗi hàng nên cộng lại bằng 1.0 hoặc 100%.)]

Chúng ta có thể cải thiện triển khai SelfAttention_v1 hơn nữa bằng cách sử dụng lớp nn.Linear của PyTorch, thực hiện phép nhân ma trận hiệu quả khi đơn vị bias bị tắt. Ngoài ra, một lợi thế đáng kể của việc sử dụng nn.Linear thay vì triển khai thủ công nn.Parameter(torch.rand(...)) là nn.Linear có sơ đồ khởi tạo trọng số tối ưu hóa, góp phần huấn luyện mô hình ổn định và hiệu quả hơn.

**Listing 3.2: Lớp self-attention sử dụng lớp Linear của PyTorch**

```python
class SelfAttention_v2(nn.Module):
    def __init__(self, d_in, d_out, qkv_bias=False):
        super().__init__()
        self.W_query = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.W_key   = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.W_value = nn.Linear(d_in, d_out, bias=qkv_bias)

    def forward(self, x):
        keys = self.W_key(x)
        queries = self.W_query(x)
        values = self.W_value(x)
        attn_scores = queries @ keys.T
        attn_weights = torch.softmax(
            attn_scores / keys.shape[-1]**0.5, dim=-1
        )
        context_vec = attn_weights @ values
        return context_vec
```

Bạn có thể sử dụng SelfAttention_v2 tương tự SelfAttention_v1:

```python
torch.manual_seed(789)
sa_v2 = SelfAttention_v2(d_in, d_out)
print(sa_v2(inputs))
```

Đầu ra là:

```
tensor([[-0.0739,  0.0713],
        [-0.0748,  0.0703],
        [-0.0749,  0.0702],
        [-0.0760,  0.0685],
        [-0.0763,  0.0679],
        [-0.0754,  0.0693]], grad_fn=<MmBackward0>)
```

Lưu ý rằng SelfAttention_v1 và SelfAttention_v2 cho đầu ra khác nhau vì chúng sử dụng trọng số khởi tạo khác nhau cho ma trận trọng số vì nn.Linear sử dụng sơ đồ khởi tạo trọng số phức tạp hơn.

> **Bài tập 3.1: So sánh SelfAttention_v1 và SelfAttention_v2**
>
> Lưu ý rằng nn.Linear trong SelfAttention_v2 sử dụng sơ đồ khởi tạo trọng số khác với nn.Parameter(torch.rand(d_in, d_out)) được sử dụng trong SelfAttention_v1, gây ra hai cơ chế cho kết quả khác nhau. Để kiểm tra rằng hai triển khai, SelfAttention_v1 và SelfAttention_v2, nói cách khác là tương tự, chúng ta có thể chuyển ma trận trọng số từ đối tượng SelfAttention_v2 sang SelfAttention_v1, sao cho cả hai đối tượng sau đó cho kết quả giống nhau.
>
> Nhiệm vụ của bạn là gán đúng trọng số từ instance của SelfAttention_v2 cho instance của SelfAttention_v1. Để làm điều này, bạn cần hiểu mối quan hệ giữa trọng số trong cả hai phiên bản. (Gợi ý: nn.Linear lưu ma trận trọng số ở dạng chuyển vị.) Sau khi gán, bạn sẽ thấy cả hai instance cho đầu ra giống nhau.

Tiếp theo, chúng ta sẽ thực hiện các cải tiến cho cơ chế self-attention, tập trung cụ thể vào việc kết hợp các yếu tố causal và multi-head. Khía cạnh causal liên quan đến việc sửa đổi cơ chế attention để ngăn mô hình truy cập thông tin tương lai trong chuỗi, điều rất quan trọng cho các tác vụ như mô hình hóa ngôn ngữ, nơi mỗi dự đoán từ chỉ nên phụ thuộc vào các từ trước đó.

Thành phần multi-head liên quan đến việc chia cơ chế attention thành nhiều "head." Mỗi head học các khía cạnh khác nhau của dữ liệu, cho phép mô hình đồng thời chú ý đến thông tin từ các không gian con biểu diễn khác nhau ở các vị trí khác nhau. Điều này cải thiện hiệu suất mô hình trong các tác vụ phức tạp.

## 3.5 Ẩn các từ tương lai với causal attention

Với nhiều tác vụ LLM, bạn sẽ muốn cơ chế self-attention chỉ xem xét các token xuất hiện trước vị trí hiện tại khi dự đoán token tiếp theo trong chuỗi. Causal attention, còn được gọi là masked attention, là dạng chuyên biệt của self-attention. Nó giới hạn mô hình chỉ xem xét đầu vào trước và hiện tại trong chuỗi khi xử lý bất kỳ token nào cho trước khi tính toán điểm attention. Điều này trái ngược với cơ chế self-attention tiêu chuẩn, cho phép truy cập toàn bộ chuỗi đầu vào cùng lúc.

Bây giờ, chúng ta sẽ sửa đổi cơ chế self-attention tiêu chuẩn để tạo cơ chế causal attention, điều thiết yếu cho việc phát triển LLM trong các chương tiếp theo. Để đạt được điều này trong LLM giống GPT, cho mỗi token được xử lý, chúng ta che (mask) các token tương lai, đến sau token hiện tại trong văn bản đầu vào, như minh họa trong hình 3.19. Chúng ta che trọng số attention phía trên đường chéo, và chuẩn hóa trọng số attention không bị che sao cho trọng số attention có tổng bằng 1 trong mỗi hàng. Sau đó, chúng ta sẽ triển khai quy trình che và chuẩn hóa này trong code.

[Hình 3.19: Trong causal attention, chúng ta che trọng số attention phía trên đường chéo sao cho cho đầu vào cho trước, LLM không thể truy cập token tương lai khi tính toán vector ngữ cảnh sử dụng trọng số attention. Ví dụ, cho từ "journey" ở hàng thứ hai, chúng ta chỉ giữ trọng số attention cho các từ trước ("Your") và ở vị trí hiện tại ("journey").]

### 3.5.1 Áp dụng causal attention mask

Bước tiếp theo của chúng ta là triển khai causal attention mask trong code. Để triển khai các bước áp dụng causal attention mask để có trọng số attention đã che, như tóm tắt trong hình 3.20, hãy làm việc với điểm attention và trọng số từ phần trước để viết code cơ chế causal attention.

[Hình 3.20: Một cách để có ma trận trọng số attention đã che trong causal attention là áp dụng hàm softmax cho điểm attention, đặt zero các phần tử phía trên đường chéo và chuẩn hóa ma trận kết quả.]

Trong bước đầu tiên, chúng ta tính toán trọng số attention sử dụng hàm softmax như chúng ta đã làm trước đó:

```python
queries = sa_v2.W_query(inputs)    # Sử dụng lại ma trận trọng số truy vấn và khóa
keys = sa_v2.W_key(inputs)         # của đối tượng SelfAttention_v2 từ phần trước
attn_scores = queries @ keys.T     # cho tiện
attn_weights = torch.softmax(attn_scores / keys.shape[-1]**0.5, dim=-1)
print(attn_weights)
```

Kết quả là trọng số attention sau:

```
tensor([[0.1921, 0.1646, 0.1652, 0.1550, 0.1721, 0.1510],
        [0.2041, 0.1659, 0.1662, 0.1496, 0.1665, 0.1477],
        [0.2036, 0.1659, 0.1662, 0.1498, 0.1664, 0.1480],
        [0.1869, 0.1667, 0.1668, 0.1571, 0.1661, 0.1564],
        [0.1830, 0.1669, 0.1670, 0.1588, 0.1658, 0.1585],
        [0.1935, 0.1663, 0.1666, 0.1542, 0.1666, 0.1529]],
       grad_fn=<SoftmaxBackward0>)
```

Chúng ta có thể triển khai bước thứ hai sử dụng hàm tril của PyTorch để tạo mask nơi các giá trị phía trên đường chéo bằng zero:

```python
context_length = attn_scores.shape[0]
mask_simple = torch.tril(torch.ones(context_length, context_length))
print(mask_simple)
```

Mask kết quả là:

```
tensor([[1., 0., 0., 0., 0., 0.],
        [1., 1., 0., 0., 0., 0.],
        [1., 1., 1., 0., 0., 0.],
        [1., 1., 1., 1., 0., 0.],
        [1., 1., 1., 1., 1., 0.],
        [1., 1., 1., 1., 1., 1.]])
```

Bây giờ, chúng ta có thể nhân mask này với trọng số attention để đặt zero các giá trị phía trên đường chéo:

```python
masked_simple = attn_weights*mask_simple
print(masked_simple)
```

Như chúng ta có thể thấy, các phần tử phía trên đường chéo đã được đặt zero thành công:

```
tensor([[0.1921, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
        [0.2041, 0.1659, 0.0000, 0.0000, 0.0000, 0.0000],
        [0.2036, 0.1659, 0.1662, 0.0000, 0.0000, 0.0000],
        [0.1869, 0.1667, 0.1668, 0.1571, 0.0000, 0.0000],
        [0.1830, 0.1669, 0.1670, 0.1588, 0.1658, 0.0000],
        [0.1935, 0.1663, 0.1666, 0.1542, 0.1666, 0.1529]],
       grad_fn=<MulBackward0>)
```

Bước thứ ba là tái chuẩn hóa trọng số attention để lại có tổng bằng 1 trong mỗi hàng. Chúng ta có thể đạt được điều này bằng cách chia mỗi phần tử trong mỗi hàng cho tổng trong mỗi hàng:

```python
row_sums = masked_simple.sum(dim=-1, keepdim=True)
masked_simple_norm = masked_simple / row_sums
print(masked_simple_norm)
```

Kết quả là ma trận trọng số attention nơi trọng số attention phía trên đường chéo bị đặt zero, và các hàng có tổng bằng 1:

```
tensor([[1.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
        [0.5517, 0.4483, 0.0000, 0.0000, 0.0000, 0.0000],
        [0.3800, 0.3097, 0.3103, 0.0000, 0.0000, 0.0000],
        [0.2758, 0.2460, 0.2462, 0.2319, 0.0000, 0.0000],
        [0.2175, 0.1983, 0.1984, 0.1888, 0.1971, 0.0000],
        [0.1935, 0.1663, 0.1666, 0.1542, 0.1666, 0.1529]],
       grad_fn=<DivBackward0>)
```

> **Rò rỉ thông tin**
>
> Khi chúng ta áp dụng mask rồi tái chuẩn hóa trọng số attention, ban đầu có vẻ như thông tin từ token tương lai (mà chúng ta dự định che) vẫn có thể ảnh hưởng đến token hiện tại vì giá trị của chúng là phần của phép tính softmax. Tuy nhiên, nhận định quan trọng là khi chúng ta tái chuẩn hóa trọng số attention sau khi che, điều chúng ta thực sự làm là tính lại softmax trên tập con nhỏ hơn (vì vị trí bị che không đóng góp vào giá trị softmax).
>
> Sự thanh lịch toán học của softmax là mặc dù ban đầu bao gồm tất cả vị trí trong mẫu số, sau khi che và tái chuẩn hóa, hiệu ứng của các vị trí bị che bị triệt tiêu — chúng không đóng góp vào điểm softmax theo bất kỳ cách có ý nghĩa nào. Nói đơn giản hơn, sau khi che và tái chuẩn hóa, phân phối trọng số attention giống như được tính chỉ giữa các vị trí không bị che từ đầu. Điều này đảm bảo không có rò rỉ thông tin từ token tương lai (hoặc bị che khác) như chúng ta dự định.

Mặc dù chúng ta có thể kết thúc triển khai causal attention tại thời điểm này, chúng ta vẫn có thể cải thiện nó. Hãy tận dụng thuộc tính toán học của hàm softmax và triển khai tính toán trọng số attention đã che hiệu quả hơn trong ít bước hơn, như hiển thị trong hình 3.21.

[Hình 3.21: Cách hiệu quả hơn để có ma trận trọng số attention đã che trong causal attention là che điểm attention bằng giá trị âm vô cùng trước khi áp dụng hàm softmax.]

Hàm softmax chuyển đổi đầu vào thành phân phối xác suất. Khi giá trị âm vô cùng (-∞) có mặt trong hàng, hàm softmax coi chúng là xác suất zero. (Về mặt toán học, điều này là vì e^(-∞) tiệm cận 0.)

Chúng ta có thể triển khai "thủ thuật" che hiệu quả hơn này bằng cách tạo mask với 1 phía trên đường chéo rồi thay các 1 này bằng giá trị âm vô cùng (-inf):

```python
mask = torch.triu(torch.ones(context_length, context_length), diagonal=1)
masked = attn_scores.masked_fill(mask.bool(), -torch.inf)
print(masked)
```

Kết quả là mask sau:

```
tensor([[0.2899,   -inf,   -inf,   -inf,   -inf,   -inf],
        [0.4656, 0.1723,   -inf,   -inf,   -inf,   -inf],
        [0.4594, 0.1703, 0.1731,   -inf,   -inf,   -inf],
        [0.2642, 0.1024, 0.1036, 0.0186,   -inf,   -inf],
        [0.2183, 0.0874, 0.0882, 0.0177, 0.0786,   -inf],
        [0.3408, 0.1270, 0.1290, 0.0198, 0.1290, 0.0078]],
       grad_fn=<MaskedFillBackward0>)
```

Bây giờ tất cả những gì chúng ta cần làm là áp dụng hàm softmax cho các kết quả đã che này, và chúng ta hoàn thành:

```python
attn_weights = torch.softmax(masked / keys.shape[-1]**0.5, dim=1)
print(attn_weights)
```

Như chúng ta có thể thấy dựa trên đầu ra, giá trị trong mỗi hàng có tổng bằng 1, và không cần chuẩn hóa thêm:

```
tensor([[1.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
        [0.5517, 0.4483, 0.0000, 0.0000, 0.0000, 0.0000],
        [0.3800, 0.3097, 0.3103, 0.0000, 0.0000, 0.0000],
        [0.2758, 0.2460, 0.2462, 0.2319, 0.0000, 0.0000],
        [0.2175, 0.1983, 0.1984, 0.1888, 0.1971, 0.0000],
        [0.1935, 0.1663, 0.1666, 0.1542, 0.1666, 0.1529]],
       grad_fn=<SoftmaxBackward0>)
```

Giờ chúng ta có thể sử dụng trọng số attention đã sửa đổi để tính toán vector ngữ cảnh qua `context_vec = attn_weights @ values`, như trong phần 3.4. Tuy nhiên, trước tiên chúng ta sẽ đề cập một chỉnh sửa nhỏ khác cho cơ chế causal attention hữu ích để giảm overfitting khi huấn luyện LLM.

### 3.5.2 Che thêm trọng số attention bằng dropout

Dropout trong deep learning là kỹ thuật nơi các đơn vị lớp ẩn được chọn ngẫu nhiên bị bỏ qua trong quá trình huấn luyện, hiệu quả là "loại bỏ" chúng. Phương pháp này giúp ngăn overfitting bằng cách đảm bảo mô hình không trở nên quá phụ thuộc vào bất kỳ tập hợp đơn vị lớp ẩn cụ thể nào. Điều quan trọng cần nhấn mạnh là dropout chỉ được sử dụng trong quá trình huấn luyện và bị vô hiệu hóa sau đó.

Trong kiến trúc transformer, bao gồm các mô hình như GPT, dropout trong cơ chế attention thường được áp dụng tại hai thời điểm cụ thể: sau khi tính toán trọng số attention hoặc sau khi áp dụng trọng số attention cho vector giá trị. Ở đây chúng ta sẽ áp dụng dropout mask sau khi tính toán trọng số attention, như minh họa trong hình 3.22, vì đó là biến thể phổ biến hơn trong thực tế.

[Hình 3.22: Sử dụng causal attention mask (trên trái), chúng ta áp dụng dropout mask bổ sung (trên phải) để đặt zero các trọng số attention bổ sung nhằm giảm overfitting trong quá trình huấn luyện.]

Trong ví dụ code sau, chúng ta sử dụng tỷ lệ dropout 50%, nghĩa là che một nửa trọng số attention. (Khi chúng ta huấn luyện mô hình GPT trong các chương sau, chúng ta sẽ sử dụng tỷ lệ dropout thấp hơn, chẳng hạn 0.1 hoặc 0.2.) Chúng ta áp dụng triển khai dropout của PyTorch trước tiên cho tensor 6 × 6 gồm các số 1 cho đơn giản:

```python
torch.manual_seed(123)
dropout = torch.nn.Dropout(0.5)   # Chúng ta chọn tỷ lệ dropout 50%.
example = torch.ones(6, 6)        # Ở đây, chúng ta tạo ma trận toàn 1.
print(dropout(example))
```

Như chúng ta có thể thấy, khoảng một nửa giá trị bị đặt zero:

```
tensor([[2., 2., 0., 2., 2., 0.],
        [0., 0., 0., 2., 0., 2.],
        [2., 2., 2., 2., 0., 2.],
        [0., 2., 2., 0., 0., 2.],
        [0., 2., 0., 2., 0., 2.],
        [0., 2., 2., 2., 2., 0.]])
```

Khi áp dụng dropout cho ma trận trọng số attention với tỷ lệ 50%, một nửa phần tử trong ma trận được đặt zero ngẫu nhiên. Để bù đắp cho sự giảm phần tử hoạt động, giá trị của các phần tử còn lại trong ma trận được tăng lên bằng hệ số 1/0.5 = 2. Sự chia tỷ lệ này rất quan trọng để duy trì sự cân bằng tổng thể của trọng số attention, đảm bảo rằng ảnh hưởng trung bình của cơ chế attention vẫn nhất quán trong cả giai đoạn huấn luyện và suy luận.

Bây giờ hãy áp dụng dropout cho chính ma trận trọng số attention:

```python
torch.manual_seed(123)
print(dropout(attn_weights))
```

Ma trận trọng số attention kết quả giờ có thêm các phần tử bị đặt zero và các số 1 còn lại được chia tỷ lệ lại:

```
tensor([[2.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
        [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
        [0.7599, 0.6194, 0.6206, 0.0000, 0.0000, 0.0000],
        [0.0000, 0.4921, 0.4925, 0.0000, 0.0000, 0.0000],
        [0.0000, 0.3966, 0.0000, 0.3775, 0.0000, 0.0000],
        [0.0000, 0.3327, 0.3331, 0.3084, 0.3331, 0.0000]],
       grad_fn=<MulBackward0>)
```

Lưu ý rằng đầu ra dropout kết quả có thể trông khác tùy thuộc vào hệ điều hành của bạn; bạn có thể đọc thêm về sự không nhất quán này trên trình theo dõi lỗi PyTorch tại https://github.com/pytorch/pytorch/issues/121595.

Sau khi hiểu về causal attention và dropout masking, giờ chúng ta có thể phát triển lớp Python ngắn gọn. Lớp này được thiết kế để tạo điều kiện cho việc áp dụng hiệu quả hai kỹ thuật này.

### 3.5.3 Triển khai lớp causal attention nhỏ gọn

Bây giờ chúng ta sẽ kết hợp các sửa đổi causal attention và dropout vào lớp Python SelfAttention mà chúng ta đã phát triển trong phần 3.4. Lớp này sau đó sẽ đóng vai trò mẫu cho phát triển multi-head attention, là lớp attention cuối cùng chúng ta sẽ triển khai.

Nhưng trước khi bắt đầu, hãy đảm bảo rằng code có thể xử lý batch gồm nhiều hơn một đầu vào sao cho lớp CausalAttention hỗ trợ đầu ra batch được tạo bởi data loader chúng ta đã triển khai trong chương 2.

Cho đơn giản, để mô phỏng đầu vào batch như vậy, chúng ta nhân đôi ví dụ văn bản đầu vào:

```python
batch = torch.stack((inputs, inputs), dim=0)
print(batch.shape)               # Hai đầu vào với sáu token mỗi cái;
                                  # mỗi token có chiều nhúng 3.
```

Kết quả là tensor ba chiều gồm hai văn bản đầu vào với sáu token mỗi cái, nơi mỗi token là vector nhúng ba chiều:

```
torch.Size([2, 6, 3])
```

Lớp CausalAttention sau đây tương tự lớp SelfAttention chúng ta đã triển khai trước đó, ngoại trừ chúng ta thêm các thành phần dropout và causal mask.

**Listing 3.3: Lớp causal attention nhỏ gọn**

```python
class CausalAttention(nn.Module):
    def __init__(self, d_in, d_out, context_length,
                dropout, qkv_bias=False):
        super().__init__()
        self.d_out = d_out
        self.W_query = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.W_key   = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.W_value = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.dropout = nn.Dropout(dropout)           # Thêm lớp dropout
        self.register_buffer(                        # register_buffer cũng là bổ sung mới
           'mask',
           torch.triu(torch.ones(context_length, context_length),
           diagonal=1)
        )

    def forward(self, x):
        b, num_tokens, d_in = x.shape
        keys = self.W_key(x)
        queries = self.W_query(x)
        values = self.W_value(x)
        attn_scores = queries @ keys.transpose(1, 2)   # Chuyển vị chiều 1 và 2,
                                                         # giữ chiều batch ở vị trí đầu (0)
        attn_scores.masked_fill_(                       # Phép toán với dấu _ ở cuối
            self.mask.bool()[:num_tokens, :num_tokens], -torch.inf)  # được thực hiện in-place
        attn_weights = torch.softmax(
            attn_scores / keys.shape[-1]**0.5, dim=-1
        )
        attn_weights = self.dropout(attn_weights)
        context_vec = attn_weights @ values
        return context_vec
```

Mặc dù tất cả dòng code được thêm lẽ ra nên quen thuộc tại thời điểm này, giờ chúng ta đã thêm lời gọi `self.register_buffer()` trong phương thức `__init__`. Việc sử dụng `register_buffer` trong PyTorch không bắt buộc nghiêm ngặt cho tất cả trường hợp sử dụng nhưng cung cấp nhiều lợi thế ở đây. Ví dụ, khi chúng ta sử dụng lớp CausalAttention trong LLM, buffer tự động được chuyển đến thiết bị phù hợp (CPU hoặc GPU) cùng với mô hình, điều sẽ liên quan khi huấn luyện LLM. Điều này có nghĩa chúng ta không cần đảm bảo thủ công rằng các tensor này ở cùng thiết bị với tham số mô hình, tránh lỗi không khớp thiết bị.

Chúng ta có thể sử dụng lớp CausalAttention như sau, tương tự SelfAttention trước đó:

```python
torch.manual_seed(123)
context_length = batch.shape[1]
ca = CausalAttention(d_in, d_out, context_length, 0.0)
context_vecs = ca(batch)
print("context_vecs.shape:", context_vecs.shape)
```

Tensor ngữ cảnh kết quả là tensor ba chiều nơi mỗi token giờ được biểu diễn bằng nhúng hai chiều:

```
context_vecs.shape: torch.Size([2, 6, 2])
```

[Hình 3.23: Đây là những gì chúng ta đã làm cho đến nay. Chúng ta bắt đầu với cơ chế attention đơn giản hóa, thêm trọng số huấn luyện, rồi thêm causal attention mask. Tiếp theo, chúng ta sẽ mở rộng cơ chế causal attention và viết code multi-head attention, mà chúng ta sẽ sử dụng trong LLM.]

## 3.6 Mở rộng single-head attention thành multi-head attention

Bước cuối cùng của chúng ta sẽ là mở rộng lớp causal attention đã triển khai trước đó qua nhiều head. Điều này còn được gọi là multi-head attention.

Thuật ngữ "multi-head" đề cập đến việc chia cơ chế attention thành nhiều "head," mỗi cái hoạt động độc lập. Trong ngữ cảnh này, một module causal attention đơn có thể được coi là single-head attention, nơi chỉ có một bộ trọng số attention xử lý đầu vào tuần tự.

Chúng ta sẽ xử lý sự mở rộng này từ causal attention thành multi-head attention. Đầu tiên, chúng ta sẽ xây dựng trực quan module multi-head attention bằng cách xếp chồng nhiều module CausalAttention. Sau đó chúng ta sẽ triển khai cùng module multi-head attention theo cách phức tạp hơn nhưng hiệu quả hơn về mặt tính toán.

### 3.6.1 Xếp chồng nhiều lớp single-head attention

Về mặt thực tế, triển khai multi-head attention liên quan đến việc tạo nhiều instance của cơ chế self-attention (xem hình 3.18), mỗi cái với trọng số riêng, rồi kết hợp đầu ra. Sử dụng nhiều instance của cơ chế self-attention có thể tốn kém về tính toán, nhưng nó rất quan trọng cho loại nhận dạng mẫu phức tạp mà các mô hình như LLM dựa trên transformer nổi tiếng.

[Hình 3.24: Module multi-head attention bao gồm hai module single-head attention xếp chồng lên nhau. Vì vậy, thay vì sử dụng một ma trận Wv đơn để tính ma trận giá trị, trong module multi-head attention với hai head, giờ chúng ta có hai ma trận trọng số giá trị: Wv1 và Wv2. Tương tự áp dụng cho các ma trận trọng số khác, WQ và Wk. Chúng ta có hai bộ vector ngữ cảnh Z1 và Z2 mà chúng ta có thể kết hợp thành một ma trận vector ngữ cảnh đơn Z.]

Như đã đề cập trước, ý tưởng chính đằng sau multi-head attention là chạy cơ chế attention nhiều lần (song song) với các phép chiếu tuyến tính (linear projection) khác nhau, đã học — kết quả nhân dữ liệu đầu vào (như vector truy vấn, khóa, và giá trị trong cơ chế attention) với ma trận trọng số. Trong code, chúng ta có thể đạt được điều này bằng cách triển khai lớp MultiHeadAttentionWrapper đơn giản xếp chồng nhiều instance của lớp CausalAttention đã triển khai trước đó.

**Listing 3.4: Lớp wrapper để triển khai multi-head attention**

```python
class MultiHeadAttentionWrapper(nn.Module):
    def __init__(self, d_in, d_out, context_length,
                 dropout, num_heads, qkv_bias=False):
        super().__init__()
        self.heads = nn.ModuleList(
            [CausalAttention(
                 d_in, d_out, context_length, dropout, qkv_bias
             )
             for _ in range(num_heads)]
        )

    def forward(self, x):
        return torch.cat([head(x) for head in self.heads], dim=-1)
```

Ví dụ, nếu chúng ta sử dụng lớp MultiHeadAttentionWrapper này với hai attention head (qua num_heads=2) và chiều đầu ra CausalAttention d_out=2, chúng ta nhận được vector ngữ cảnh bốn chiều (d_out*num_heads=4), như mô tả trong hình 3.25.

[Hình 3.25: Sử dụng MultiHeadAttentionWrapper, chúng ta chỉ định số attention head (num_heads). Nếu chúng ta đặt num_heads=2, như trong ví dụ này, chúng ta nhận tensor với hai bộ ma trận vector ngữ cảnh. Trong mỗi ma trận vector ngữ cảnh, các hàng đại diện cho vector ngữ cảnh tương ứng với token, và các cột tương ứng với chiều nhúng được chỉ định qua d_out=4. Chúng ta nối các ma trận vector ngữ cảnh này dọc theo chiều cột. Vì chúng ta có hai attention head và chiều nhúng là 2, chiều nhúng cuối cùng là 2 × 2 = 4.]

Để minh họa thêm bằng ví dụ cụ thể, chúng ta có thể sử dụng lớp MultiHeadAttentionWrapper tương tự lớp CausalAttention trước:

```python
torch.manual_seed(123)
context_length = batch.shape[1]  # Đây là số token
d_in, d_out = 3, 2
mha = MultiHeadAttentionWrapper(
    d_in, d_out, context_length, 0.0, num_heads=2
)
context_vecs = mha(batch)
print(context_vecs)
print("context_vecs.shape:", context_vecs.shape)
```

Kết quả là tensor sau đại diện cho vector ngữ cảnh:

```
tensor([[[-0.4519,  0.2216,  0.4772,  0.1063],
         [-0.5874,  0.0058,  0.5891,  0.3257],
         [-0.6300, -0.0632,  0.6202,  0.3860],
         [-0.5675, -0.0843,  0.5478,  0.3589],
         [-0.5526, -0.0981,  0.5321,  0.3428],
         [-0.5299, -0.1081,  0.5077,  0.3493]],
        [[-0.4519,  0.2216,  0.4772,  0.1063],
         [-0.5874,  0.0058,  0.5891,  0.3257],
         [-0.6300, -0.0632,  0.6202,  0.3860],
         [-0.5675, -0.0843,  0.5478,  0.3589],
         [-0.5526, -0.0981,  0.5321,  0.3428],
         [-0.5299, -0.1081,  0.5077,  0.3493]]], grad_fn=<CatBackward0>)
context_vecs.shape: torch.Size([2, 6, 4])
```

Chiều đầu tiên của tensor context_vecs kết quả là 2 vì chúng ta có hai văn bản đầu vào (các văn bản đầu vào được nhân đôi, đó là lý do vector ngữ cảnh hoàn toàn giống nhau cho chúng). Chiều thứ hai đề cập đến 6 token trong mỗi đầu vào. Chiều thứ ba đề cập đến nhúng bốn chiều của mỗi token.

Cho đến nay, chúng ta đã triển khai MultiHeadAttentionWrapper kết hợp nhiều module single-head attention. Tuy nhiên, chúng được xử lý tuần tự qua `[head(x) for head in self.heads]` trong phương thức forward. Chúng ta có thể cải thiện triển khai này bằng cách xử lý các head song song. Một cách để đạt được điều này là tính toán đầu ra cho tất cả attention head đồng thời qua phép nhân ma trận.

> **Bài tập 3.2: Trả về vector nhúng hai chiều**
>
> Thay đổi đối số đầu vào cho lời gọi MultiHeadAttentionWrapper(..., num_heads=2) sao cho vector ngữ cảnh đầu ra là hai chiều thay vì bốn chiều trong khi giữ setting num_heads=2. Gợi ý: Bạn không cần sửa đổi triển khai lớp; bạn chỉ cần thay đổi một trong các đối số đầu vào khác.

### 3.6.2 Triển khai multi-head attention với chia tách trọng số

Cho đến nay, chúng ta đã tạo MultiHeadAttentionWrapper để triển khai multi-head attention bằng cách xếp chồng nhiều module single-head attention. Điều này được thực hiện bằng cách khởi tạo và kết hợp nhiều đối tượng CausalAttention.

Thay vì duy trì hai lớp riêng biệt, MultiHeadAttentionWrapper và CausalAttention, chúng ta có thể kết hợp các khái niệm này thành một lớp MultiHeadAttention duy nhất. Ngoài ra, ngoài việc hợp nhất MultiHeadAttentionWrapper với code CausalAttention, chúng ta sẽ thực hiện một số sửa đổi khác để triển khai multi-head attention hiệu quả hơn.

Trong MultiHeadAttentionWrapper, nhiều head được triển khai bằng cách tạo danh sách các đối tượng CausalAttention (self.heads), mỗi cái đại diện cho một attention head riêng biệt. Lớp CausalAttention thực hiện cơ chế attention độc lập, và kết quả từ mỗi head được nối lại. Ngược lại, lớp MultiHeadAttention sau đây tích hợp chức năng multi-head trong một lớp duy nhất. Nó chia đầu vào thành nhiều head bằng cách reshape tensor truy vấn, khóa, và giá trị đã chiếu rồi kết hợp kết quả từ các head này sau khi tính toán attention.

Hãy xem xét lớp MultiHeadAttention trước khi thảo luận thêm.

[Hình 3.26: Trong lớp MultiHeadAttentionWrapper với hai attention head, chúng ta khởi tạo hai ma trận trọng số, Wq1 và Wq2, và tính toán hai ma trận truy vấn, Q1 và Q2 (trên). Trong lớp MultiHeadAttention, chúng ta khởi tạo một ma trận trọng số lớn hơn Wq, chỉ thực hiện một phép nhân ma trận với đầu vào để có ma trận truy vấn Q, rồi chia ma trận truy vấn thành Q1 và Q2 (dưới). Chúng ta làm tương tự cho khóa và giá trị, không hiển thị để giảm lộn xộn trực quan.]

**Listing 3.5: Lớp multi-head attention hiệu quả**

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d_in, d_out,
                 context_length, dropout, num_heads, qkv_bias=False):
        super().__init__()
        assert (d_out % num_heads == 0), \
            "d_out must be divisible by num_heads"

        self.d_out = d_out
        self.num_heads = num_heads
        self.head_dim = d_out // num_heads   # Giảm chiều chiếu để khớp
                                              # chiều đầu ra mong muốn

        self.W_query = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.W_key = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.W_value = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.out_proj = nn.Linear(d_out, d_out)   # Sử dụng lớp Linear
                                                   # để kết hợp đầu ra head
        self.dropout = nn.Dropout(dropout)
        self.register_buffer(
            "mask",
            torch.triu(torch.ones(context_length, context_length),
                       diagonal=1)
        )

    def forward(self, x):
        b, num_tokens, d_in = x.shape

        keys = self.W_key(x)        # Shape: (b, num_tokens, d_out)
        queries = self.W_query(x)   # Shape: (b, num_tokens, d_out)
        values = self.W_value(x)    # Shape: (b, num_tokens, d_out)

        # Chúng ta ngầm chia ma trận bằng cách thêm chiều num_heads.
        # Sau đó unroll chiều cuối:
        # (b, num_tokens, d_out) -> (b, num_tokens, num_heads, head_dim)
        keys = keys.view(b, num_tokens, self.num_heads, self.head_dim)
        values = values.view(b, num_tokens, self.num_heads, self.head_dim)
        queries = queries.view(
            b, num_tokens, self.num_heads, self.head_dim
        )

        # Chuyển vị từ shape (b, num_tokens, num_heads, head_dim)
        # sang (b, num_heads, num_tokens, head_dim)
        keys = keys.transpose(1, 2)
        queries = queries.transpose(1, 2)
        values = values.transpose(1, 2)

        # Tính tích vô hướng cho mỗi head
        attn_scores = queries @ keys.transpose(2, 3)

        # Mask cắt ngắn xuống số token
        mask_bool = self.mask.bool()[:num_tokens, :num_tokens]

        # Sử dụng mask để điền điểm attention
        attn_scores.masked_fill_(mask_bool, -torch.inf)

        attn_weights = torch.softmax(
            attn_scores / keys.shape[-1]**0.5, dim=-1)
        attn_weights = self.dropout(attn_weights)

        # Shape: (b, num_tokens, num_heads, head_dim)
        context_vec = (attn_weights @ values).transpose(1, 2)

        # Kết hợp head, nơi self.d_out = self.num_heads * self.head_dim
        context_vec = context_vec.contiguous().view(
            b, num_tokens, self.d_out
        )

        # Thêm phép chiếu tuyến tính tùy chọn
        context_vec = self.out_proj(context_vec)
        return context_vec
```

Mặc dù reshape (.view) và chuyển vị (.transpose) của tensor bên trong lớp MultiHeadAttention trông rất phức tạp về mặt toán học, lớp MultiHeadAttention triển khai cùng khái niệm như MultiHeadAttentionWrapper trước đó.

Ở cấp độ tổng quan, trong MultiHeadAttentionWrapper trước đó, chúng ta xếp chồng nhiều lớp single-head attention mà chúng ta kết hợp thành lớp multi-head attention. MultiHeadAttention sử dụng phương pháp tích hợp. Nó bắt đầu với lớp multi-head rồi nội bộ chia lớp này thành các attention head riêng lẻ, như minh họa trong hình 3.26.

Sự chia tách tensor truy vấn, khóa, và giá trị đạt được thông qua các phép toán reshape và chuyển vị tensor sử dụng phương thức .view và .transpose của PyTorch. Đầu vào trước tiên được biến đổi (qua lớp linear cho truy vấn, khóa, và giá trị) rồi được reshape để đại diện cho nhiều head.

Phép toán chính là chia chiều d_out thành num_heads và head_dim, nơi head_dim = d_out / num_heads. Sự chia tách này sau đó đạt được sử dụng phương thức .view: tensor với các chiều (b, num_tokens, d_out) được reshape thành chiều (b, num_tokens, num_heads, head_dim).

Các tensor sau đó được chuyển vị để đưa chiều num_heads trước chiều num_tokens, kết quả là shape (b, num_heads, num_tokens, head_dim). Sự chuyển vị này rất quan trọng để căn chỉnh đúng truy vấn, khóa, và giá trị qua các head khác nhau và thực hiện phép nhân ma trận batch hiệu quả.

Để minh họa phép nhân ma trận batch này, giả sử chúng ta có tensor sau:

```python
a = torch.tensor([[[[0.2745, 0.6584, 0.2775, 0.8573],   # Shape tensor này là
                    [0.8993, 0.0390, 0.9268, 0.7388],    # (b, num_heads, num_tokens, head_dim)
                    [0.7179, 0.7058, 0.9156, 0.4340]],   # = (1, 2, 3, 4)
                   [[0.0772, 0.3565, 0.1479, 0.5331],
                    [0.4066, 0.2318, 0.4545, 0.9737],
                    [0.4606, 0.5159, 0.4220, 0.5786]]]])
```

Bây giờ chúng ta thực hiện phép nhân ma trận batch giữa tensor với chính nó nơi chúng ta chuyển vị hai chiều cuối, num_tokens và head_dim:

```python
print(a @ a.transpose(2, 3))
```

Kết quả là:

```
tensor([[[[1.3208, 1.1631, 1.2879],
          [1.1631, 2.2150, 1.8424],
          [1.2879, 1.8424, 2.0402]],
         [[0.4391, 0.7003, 0.5903],
          [0.7003, 1.3737, 1.0620],
          [0.5903, 1.0620, 0.9912]]]])
```

Trong trường hợp này, triển khai phép nhân ma trận trong PyTorch xử lý tensor đầu vào bốn chiều sao cho phép nhân ma trận được thực hiện giữa hai chiều cuối (num_tokens, head_dim) rồi lặp lại cho từng head riêng lẻ.

Ví dụ, phần trước trở thành cách nhỏ gọn hơn để tính phép nhân ma trận cho mỗi head riêng biệt:

```python
first_head = a[0, 0, :, :]
first_res = first_head @ first_head.T
print("First head:\n", first_res)

second_head = a[0, 1, :, :]
second_res = second_head @ second_head.T
print("\nSecond head:\n", second_res)
```

Kết quả hoàn toàn giống với kết quả chúng ta nhận được khi sử dụng phép nhân ma trận batch `print(a @ a.transpose(2, 3))`:

```
First head:
 tensor([[1.3208, 1.1631, 1.2879],
        [1.1631, 2.2150, 1.8424],
        [1.2879, 1.8424, 2.0402]])

Second head:
 tensor([[0.4391, 0.7003, 0.5903],
        [0.7003, 1.3737, 1.0620],
        [0.5903, 1.0620, 0.9912]])
```

Tiếp tục với MultiHeadAttention, sau khi tính toán trọng số attention và vector ngữ cảnh, vector ngữ cảnh từ tất cả head được chuyển vị lại thành shape (b, num_tokens, num_heads, head_dim). Các vector này sau đó được reshape (flatten) thành shape (b, num_tokens, d_out), hiệu quả kết hợp đầu ra từ tất cả head.

Ngoài ra, chúng ta đã thêm lớp chiếu đầu ra (self.out_proj) vào MultiHeadAttention sau khi kết hợp các head, không có trong lớp CausalAttention. Lớp chiếu đầu ra này không bắt buộc nghiêm ngặt (xem phụ lục B để biết thêm chi tiết), nhưng nó thường được sử dụng trong nhiều kiến trúc LLM, đó là lý do tôi thêm nó ở đây cho đầy đủ.

Mặc dù lớp MultiHeadAttention trông phức tạp hơn MultiHeadAttentionWrapper do reshape và chuyển vị tensor bổ sung, nó hiệu quả hơn. Lý do là chúng ta chỉ cần một phép nhân ma trận để tính toán khóa, ví dụ, `keys = self.W_key(x)` (tương tự đúng cho truy vấn và giá trị). Trong MultiHeadAttentionWrapper, chúng ta cần lặp lại phép nhân ma trận này, là một trong những bước tốn kém nhất về tính toán, cho mỗi attention head.

Lớp MultiHeadAttention có thể được sử dụng tương tự các lớp SelfAttention và CausalAttention chúng ta đã triển khai trước đó:

```python
torch.manual_seed(123)
batch_size, context_length, d_in = batch.shape
d_out = 2
mha = MultiHeadAttention(d_in, d_out, context_length, 0.0, num_heads=2)
context_vecs = mha(batch)
print(context_vecs)
print("context_vecs.shape:", context_vecs.shape)
```

Kết quả cho thấy chiều đầu ra được kiểm soát trực tiếp bởi đối số d_out:

```
tensor([[[0.3190, 0.4858],
         [0.2943, 0.3897],
         [0.2856, 0.3593],
         [0.2693, 0.3873],
         [0.2639, 0.3928],
         [0.2575, 0.4028]],
        [[0.3190, 0.4858],
         [0.2943, 0.3897],
         [0.2856, 0.3593],
         [0.2693, 0.3873],
         [0.2639, 0.3928],
         [0.2575, 0.4028]]], grad_fn=<ViewBackward0>)
context_vecs.shape: torch.Size([2, 6, 2])
```

Giờ chúng ta đã triển khai lớp MultiHeadAttention mà chúng ta sẽ sử dụng khi triển khai và huấn luyện LLM. Lưu ý rằng mặc dù code hoàn toàn hoạt động được, tôi đã sử dụng kích thước nhúng và số attention head tương đối nhỏ để giữ đầu ra dễ đọc.

Để so sánh, mô hình GPT-2 nhỏ nhất (117 triệu tham số) có 12 attention head và kích thước nhúng vector ngữ cảnh là 768. Mô hình GPT-2 lớn nhất (1.5 tỷ tham số) có 25 attention head và kích thước nhúng vector ngữ cảnh là 1.600. Kích thước nhúng của token đầu vào và nhúng ngữ cảnh giống nhau trong mô hình GPT (d_in = d_out).

> **Bài tập 3.3: Khởi tạo module attention kích thước GPT-2**
>
> Sử dụng lớp MultiHeadAttention, khởi tạo module multi-head attention có cùng số attention head như mô hình GPT-2 nhỏ nhất (12 attention head). Cũng đảm bảo bạn sử dụng kích thước nhúng đầu vào và đầu ra tương ứng tương tự GPT-2 (768 chiều). Lưu ý rằng mô hình GPT-2 nhỏ nhất hỗ trợ độ dài ngữ cảnh 1.024 token.

## Tóm tắt

- Cơ chế attention biến đổi các phần tử đầu vào thành biểu diễn vector ngữ cảnh nâng cao kết hợp thông tin về tất cả đầu vào.
- Cơ chế self-attention tính toán biểu diễn vector ngữ cảnh dưới dạng tổng có trọng số trên đầu vào.
- Trong cơ chế attention đơn giản hóa, trọng số attention được tính toán qua tích vô hướng.
- Tích vô hướng là cách ngắn gọn để nhân hai vector theo từng phần tử rồi cộng các tích.
- Phép nhân ma trận, mặc dù không bắt buộc nghiêm ngặt, giúp chúng ta triển khai tính toán hiệu quả và nhỏ gọn hơn bằng cách thay thế vòng lặp for lồng nhau.
- Trong cơ chế self-attention được sử dụng trong LLM, còn gọi là scaled-dot product attention, chúng ta bao gồm ma trận trọng số huấn luyện để tính toán các biến đổi trung gian của đầu vào: truy vấn, giá trị, và khóa.
- Khi làm việc với LLM đọc và sinh văn bản từ trái sang phải, chúng ta thêm causal attention mask để ngăn LLM truy cập token tương lai.
- Ngoài causal attention mask để đặt zero trọng số attention, chúng ta có thể thêm dropout mask để giảm overfitting trong LLM.
- Các module attention trong LLM dựa trên transformer liên quan đến nhiều instance của causal attention, được gọi là multi-head attention.
- Chúng ta có thể tạo module multi-head attention bằng cách xếp chồng nhiều instance của module causal attention.
- Cách hiệu quả hơn để tạo module multi-head attention liên quan đến phép nhân ma trận batch.
