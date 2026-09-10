# Chương 2: Làm việc với dữ liệu văn bản

Cho đến nay, chúng ta đã đề cập cấu trúc tổng quát của các mô hình ngôn ngữ lớn (LLM) và biết rằng chúng được tiền huấn luyện trên lượng văn bản khổng lồ. Cụ thể, trọng tâm của chúng ta là các LLM chỉ có decoder dựa trên kiến trúc transformer, làm nền tảng cho các mô hình được sử dụng trong ChatGPT và các LLM giống GPT phổ biến khác.

Trong giai đoạn tiền huấn luyện, LLM xử lý văn bản từng từ một. Huấn luyện LLM với hàng triệu đến hàng tỷ tham số sử dụng tác vụ dự đoán từ tiếp theo tạo ra các mô hình có khả năng ấn tượng. Các mô hình này sau đó có thể được tinh chỉnh thêm để theo dõi hướng dẫn tổng quát hoặc thực hiện các tác vụ mục tiêu cụ thể. Nhưng trước khi chúng ta có thể triển khai và huấn luyện LLM, chúng ta cần chuẩn bị bộ dữ liệu huấn luyện, như minh họa trong hình 2.1.

*Chương này bao gồm:*
- *Chuẩn bị văn bản cho huấn luyện mô hình ngôn ngữ lớn*
- *Chia văn bản thành token từ và token con từ (subword)*
- *Mã hóa cặp byte (Byte pair encoding) như cách tokenize văn bản nâng cao hơn*
- *Lấy mẫu ví dụ huấn luyện với phương pháp cửa sổ trượt (sliding window)*
- *Chuyển đổi token thành vector đầu vào cho mô hình ngôn ngữ lớn*

[Hình 2.1: Ba giai đoạn chính của việc viết code một LLM. Chương này tập trung vào bước 1 của giai đoạn 1: triển khai pipeline lấy mẫu dữ liệu.]

Bạn sẽ học cách chuẩn bị văn bản đầu vào để huấn luyện LLM. Điều này bao gồm chia văn bản thành các token từ và token con từ riêng lẻ, sau đó có thể được mã hóa thành biểu diễn vector cho LLM. Bạn cũng sẽ tìm hiểu về các lược đồ tokenization nâng cao như mã hóa cặp byte, được sử dụng trong các LLM phổ biến như GPT. Cuối cùng, chúng ta sẽ triển khai chiến lược lấy mẫu và tải dữ liệu để tạo ra các cặp đầu vào-đầu ra cần thiết cho huấn luyện LLM.

## 2.1 Hiểu về word embedding

Các mô hình mạng nơ-ron sâu, bao gồm LLM, không thể xử lý trực tiếp văn bản thô. Vì văn bản là dữ liệu phân loại (categorical), nó không tương thích với các phép toán toán học được sử dụng để triển khai và huấn luyện mạng nơ-ron. Do đó, chúng ta cần một cách để biểu diễn từ dưới dạng vector có giá trị liên tục (continuous-valued vectors).

> **LƯU Ý:** Độc giả không quen thuộc với vector và tensor trong ngữ cảnh tính toán có thể tìm hiểu thêm trong phụ lục A, phần A.2.2.

Khái niệm chuyển đổi dữ liệu sang dạng vector thường được gọi là nhúng (embedding). Sử dụng một lớp mạng nơ-ron cụ thể hoặc mô hình mạng nơ-ron tiền huấn luyện khác, chúng ta có thể nhúng các loại dữ liệu khác nhau — ví dụ, video, âm thanh, và văn bản, như minh họa trong hình 2.2. Tuy nhiên, điều quan trọng cần lưu ý là các định dạng dữ liệu khác nhau yêu cầu các mô hình nhúng riêng biệt. Ví dụ, mô hình nhúng được thiết kế cho văn bản sẽ không phù hợp để nhúng dữ liệu âm thanh hoặc video.

[Hình 2.2: Các mô hình deep learning không thể xử lý trực tiếp các định dạng dữ liệu như video, âm thanh, và văn bản ở dạng thô. Do đó, chúng ta sử dụng mô hình nhúng để chuyển đổi dữ liệu thô này thành biểu diễn vector dày đặc mà kiến trúc deep learning có thể dễ dàng hiểu và xử lý. Cụ thể, hình này minh họa quá trình chuyển đổi dữ liệu thô thành vector số ba chiều.]

Về bản chất, nhúng là ánh xạ từ các đối tượng rời rạc, chẳng hạn như từ, hình ảnh, hoặc thậm chí toàn bộ tài liệu, đến các điểm trong không gian vector liên tục — mục đích chính của nhúng là chuyển đổi dữ liệu phi số thành định dạng mà mạng nơ-ron có thể xử lý.

Mặc dù nhúng từ (word embedding) là dạng nhúng văn bản phổ biến nhất, cũng có nhúng cho câu, đoạn văn, hoặc toàn bộ tài liệu. Nhúng câu hoặc đoạn văn là lựa chọn phổ biến cho tạo sinh tăng cường truy xuất (retrieval-augmented generation). Tạo sinh tăng cường truy xuất kết hợp tạo sinh (như tạo văn bản) với truy xuất (như tìm kiếm cơ sở kiến thức bên ngoài) để lấy thông tin liên quan khi tạo văn bản, đây là kỹ thuật nằm ngoài phạm vi cuốn sách này. Vì mục tiêu của chúng ta là huấn luyện LLM giống GPT, học cách tạo văn bản từng từ một, chúng ta sẽ tập trung vào nhúng từ.

Nhiều thuật toán và framework đã được phát triển để tạo nhúng từ. Một trong những ví dụ sớm nhất và phổ biến nhất là phương pháp Word2Vec. Word2Vec huấn luyện kiến trúc mạng nơ-ron để tạo nhúng từ bằng cách dự đoán ngữ cảnh của một từ cho trước từ mục tiêu hoặc ngược lại. Ý tưởng chính đằng sau Word2Vec là các từ xuất hiện trong ngữ cảnh tương tự có xu hướng có ý nghĩa tương tự. Do đó, khi chiếu vào nhúng từ hai chiều cho mục đích trực quan hóa, các thuật ngữ tương tự được nhóm lại với nhau, như hiển thị trong hình 2.3.

Nhúng từ có thể có số chiều khác nhau, từ một đến hàng nghìn. Số chiều cao hơn có thể nắm bắt các mối quan hệ tinh tế hơn nhưng với chi phí hiệu quả tính toán.

[Hình 2.3: Nếu nhúng từ là hai chiều, chúng ta có thể vẽ chúng trong biểu đồ phân tán hai chiều cho mục đích trực quan hóa như hiển thị ở đây. Khi sử dụng kỹ thuật nhúng từ, chẳng hạn như Word2Vec, các từ tương ứng với khái niệm tương tự thường xuất hiện gần nhau trong không gian nhúng. Ví dụ, các loại chim khác nhau xuất hiện gần nhau hơn trong không gian nhúng so với các quốc gia và thành phố.]

Mặc dù chúng ta có thể sử dụng các mô hình tiền huấn luyện như Word2Vec để tạo nhúng cho các mô hình machine learning, LLM thường tạo nhúng riêng của chúng là phần của lớp đầu vào và được cập nhật trong quá trình huấn luyện. Ưu điểm của việc tối ưu hóa nhúng như một phần của quá trình huấn luyện LLM thay vì sử dụng Word2Vec là nhúng được tối ưu hóa cho tác vụ và dữ liệu cụ thể. Chúng ta sẽ triển khai các lớp nhúng như vậy ở phần sau của chương này. (LLM cũng có thể tạo ra nhúng đầu ra theo ngữ cảnh, như chúng ta thảo luận trong chương 3.)

Thật không may, nhúng nhiều chiều thể hiện thách thức cho trực quan hóa vì nhận thức giác quan và biểu diễn đồ họa thông thường của chúng ta vốn bị giới hạn ở ba chiều hoặc ít hơn, đây là lý do tại sao hình 2.3 hiển thị nhúng hai chiều trong biểu đồ phân tán hai chiều. Tuy nhiên, khi làm việc với LLM, chúng ta thường sử dụng nhúng với số chiều cao hơn nhiều. Đối với cả GPT-2 và GPT-3, kích thước nhúng (thường được gọi là chiều của trạng thái ẩn — hidden states — của mô hình) thay đổi dựa trên biến thể và kích thước mô hình cụ thể. Đó là sự đánh đổi giữa hiệu suất và hiệu quả. Các mô hình GPT-2 nhỏ nhất (117M và 125M tham số) sử dụng kích thước nhúng 768 chiều để cung cấp ví dụ cụ thể. Mô hình GPT-3 lớn nhất (175B tham số) sử dụng kích thước nhúng 12.288 chiều.

Tiếp theo, chúng ta sẽ đi qua các bước cần thiết để chuẩn bị nhúng được sử dụng bởi LLM, bao gồm chia văn bản thành từ, chuyển đổi từ thành token, và biến token thành vector nhúng.

## 2.2 Tokenization — Phân tách văn bản thành token

Hãy thảo luận cách chúng ta chia văn bản đầu vào thành các token riêng lẻ, một bước tiền xử lý cần thiết để tạo nhúng cho LLM. Các token này là các từ riêng lẻ hoặc ký tự đặc biệt, bao gồm các ký tự dấu câu, như hiển thị trong hình 2.4.

Văn bản chúng ta sẽ tokenize cho huấn luyện LLM là "The Verdict", một truyện ngắn của Edith Wharton, đã được phát hành vào phạm vi công cộng và do đó được phép sử dụng cho các tác vụ huấn luyện LLM. Văn bản có sẵn trên Wikisource tại https://en.wikisource.org/wiki/The_Verdict, và bạn có thể sao chép và dán nó vào một file văn bản, mà tôi đã sao chép vào file văn bản "the-verdict.txt".

Ngoài ra, bạn có thể tìm file "the-verdict.txt" này trong kho GitHub của cuốn sách tại https://mng.bz/Adng. Bạn có thể tải file bằng code Python sau:

[Hình 2.4: Cái nhìn về các bước xử lý văn bản trong ngữ cảnh của LLM. Ở đây, chúng ta chia văn bản đầu vào thành các token riêng lẻ, là các từ hoặc ký tự đặc biệt, chẳng hạn như ký tự dấu câu.]

```python
import urllib.request
url = ("https://raw.githubusercontent.com/rasbt/"
       "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
       "the-verdict.txt")
file_path = "the-verdict.txt"
urllib.request.urlretrieve(url, file_path)
```

Tiếp theo, chúng ta có thể tải file the-verdict.txt sử dụng các tiện ích đọc file chuẩn của Python.

**Listing 2.1: Đọc truyện ngắn làm mẫu văn bản vào Python**

```python
with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
print("Total number of character:", len(raw_text))
print(raw_text[:99])
```

Lệnh print in ra tổng số ký tự theo sau bởi 100 ký tự đầu tiên của file này cho mục đích minh họa:

```
Total number of character: 20479
I HAD always thought Jack Gisburn rather a cheap genius--though a good fellow
enough--so it was no
```

Mục tiêu của chúng ta là tokenize truyện ngắn 20.479 ký tự này thành các từ và ký tự đặc biệt riêng lẻ mà sau đó chúng ta có thể chuyển thành nhúng cho huấn luyện LLM.

> **LƯU Ý:** Thông thường khi làm việc với LLM, người ta xử lý hàng triệu bài viết và hàng trăm nghìn cuốn sách — nhiều gigabyte văn bản. Tuy nhiên, cho mục đích giáo dục, làm việc với các mẫu văn bản nhỏ hơn như một cuốn sách duy nhất là đủ để minh họa các ý tưởng chính đằng sau các bước xử lý văn bản và có thể chạy được trong thời gian hợp lý trên phần cứng tiêu dùng.

Làm thế nào chúng ta có thể chia văn bản này tốt nhất để có được danh sách token? Để làm điều này, chúng ta thực hiện một chuyến tham quan nhỏ và sử dụng thư viện biểu thức chính quy `re` của Python cho mục đích minh họa. (Bạn không cần phải học hoặc ghi nhớ bất kỳ cú pháp biểu thức chính quy nào vì sau đó chúng ta sẽ chuyển sang tokenizer được xây dựng sẵn.)

Sử dụng một số văn bản ví dụ đơn giản, chúng ta có thể sử dụng lệnh `re.split` với cú pháp sau để chia văn bản trên các ký tự khoảng trắng:

```python
import re
text = "Hello, world. This, is a test."
result = re.split(r'(\s)', text)
print(result)
```

Kết quả là danh sách các từ riêng lẻ, khoảng trắng, và ký tự dấu câu:

```
['Hello,', ' ', 'world.', ' ', 'This,', ' ', 'is', ' ', 'a', ' ', 'test.']
```

Lược đồ tokenization đơn giản này chủ yếu hoạt động để tách văn bản ví dụ thành các từ riêng lẻ; tuy nhiên, một số từ vẫn được nối với các ký tự dấu câu mà chúng ta muốn có như các mục danh sách riêng biệt. Chúng ta cũng kiềm chế không chuyển tất cả văn bản sang chữ thường vì viết hoa giúp LLM phân biệt giữa danh từ riêng và danh từ chung, hiểu cấu trúc câu, và học cách tạo văn bản với viết hoa đúng cách.

Hãy sửa đổi biểu thức chính quy để chia trên khoảng trắng (`\s`), dấu phẩy, và dấu chấm (`[,.]`):

```python
result = re.split(r'([,.]|\s)', text)
print(result)
```

Chúng ta có thể thấy rằng các từ và ký tự dấu câu giờ là các mục danh sách riêng biệt đúng như chúng ta muốn:

```
['Hello', ',', '', ' ', 'world', '.', '', ' ', 'This', ',', '', ' ', 'is',
' ', 'a', ' ', 'test', '.', '']
```

Một vấn đề nhỏ còn lại là danh sách vẫn bao gồm ký tự khoảng trắng. Tùy chọn, chúng ta có thể loại bỏ các ký tự thừa này một cách an toàn như sau:

```python
result = [item for item in result if item.strip()]
print(result)
```

Đầu ra không có khoảng trắng trông như sau:

```
['Hello', ',', 'world', '.', 'This', ',', 'is', 'a', 'test', '.']
```

> **LƯU Ý:** Khi phát triển tokenizer đơn giản, việc chúng ta nên mã hóa khoảng trắng như ký tự riêng biệt hay chỉ loại bỏ chúng phụ thuộc vào ứng dụng và yêu cầu của nó. Loại bỏ khoảng trắng giảm yêu cầu bộ nhớ và tính toán. Tuy nhiên, giữ khoảng trắng có thể hữu ích nếu chúng ta huấn luyện mô hình nhạy cảm với cấu trúc chính xác của văn bản (ví dụ, code Python, nhạy cảm với thụt lề và khoảng cách). Ở đây, chúng ta loại bỏ khoảng trắng cho đơn giản và ngắn gọn của đầu ra đã tokenize. Sau đó, chúng ta sẽ chuyển sang lược đồ tokenization bao gồm khoảng trắng.

Lược đồ tokenization mà chúng ta đã nghĩ ra ở đây hoạt động tốt trên văn bản mẫu đơn giản. Hãy sửa đổi nó thêm một chút để nó cũng có thể xử lý các loại dấu câu khác, chẳng hạn như dấu hỏi, dấu ngoặc kép, và dấu gạch ngang kép mà chúng ta đã thấy trước đó trong 100 ký tự đầu tiên của truyện ngắn Edith Wharton, cùng với các ký tự đặc biệt bổ sung:

```python
text = "Hello, world. Is this-- a test?"
result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
result = [item.strip() for item in result if item.strip()]
print(result)
```

Đầu ra kết quả là:

```
['Hello', ',', 'world', '.', 'Is', 'this', '--', 'a', 'test', '?']
```

[Hình 2.5: Lược đồ tokenization mà chúng ta đã triển khai cho đến nay chia văn bản thành các từ và ký tự dấu câu riêng lẻ. Trong ví dụ cụ thể này, văn bản mẫu được chia thành 10 token riêng lẻ.]

Như chúng ta có thể thấy dựa trên kết quả tóm tắt trong hình 2.5, lược đồ tokenization của chúng ta giờ có thể xử lý thành công các ký tự đặc biệt khác nhau trong văn bản.

Bây giờ khi chúng ta có tokenizer cơ bản hoạt động, hãy áp dụng nó cho toàn bộ truyện ngắn của Edith Wharton:

```python
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(len(preprocessed))
```

Lệnh print này xuất ra 4690, là số token trong văn bản này (không có khoảng trắng). Hãy in 30 token đầu tiên để kiểm tra trực quan nhanh:

```python
print(preprocessed[:30])
```

Đầu ra kết quả cho thấy tokenizer của chúng ta dường như xử lý văn bản tốt vì tất cả từ và ký tự đặc biệt được tách biệt gọn gàng:

```
['I', 'HAD', 'always', 'thought', 'Jack', 'Gisburn', 'rather', 'a',
'cheap', 'genius', '--', 'though', 'a', 'good', 'fellow', 'enough',
'--', 'so', 'it', 'was', 'no', 'great', 'surprise', 'to', 'me', 'to',
'hear', 'that', ',', 'in']
```

## 2.3 Chuyển đổi token thành token ID

Tiếp theo, hãy chuyển đổi các token này từ biểu diễn chuỗi Python sang biểu diễn số nguyên để tạo ra các token ID. Sự chuyển đổi này là bước trung gian trước khi chuyển đổi token ID thành vector nhúng.

Để ánh xạ các token đã tạo trước đó thành token ID, trước tiên chúng ta phải xây dựng bộ từ vựng (vocabulary). Bộ từ vựng này xác định cách chúng ta ánh xạ mỗi từ và ký tự đặc biệt duy nhất sang một số nguyên duy nhất, như hiển thị trong hình 2.6.

[Hình 2.6: Chúng ta xây dựng bộ từ vựng bằng cách tokenize toàn bộ văn bản trong tập dữ liệu huấn luyện thành các token riêng lẻ. Các token riêng lẻ này sau đó được sắp xếp theo thứ tự bảng chữ cái, và các token trùng lặp được loại bỏ. Các token duy nhất sau đó được tổng hợp vào bộ từ vựng xác định ánh xạ từ mỗi token duy nhất sang một giá trị số nguyên duy nhất. Bộ từ vựng được mô tả là có kích thước nhỏ có chủ đích và không chứa dấu câu hoặc ký tự đặc biệt cho đơn giản.]

Bây giờ khi chúng ta đã tokenize truyện ngắn của Edith Wharton và gán nó cho biến Python gọi là `preprocessed`, hãy tạo danh sách tất cả token duy nhất và sắp xếp chúng theo thứ tự bảng chữ cái để xác định kích thước bộ từ vựng:

```python
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print(vocab_size)
```

Sau khi xác định rằng kích thước bộ từ vựng là 1.130 qua code này, chúng ta tạo bộ từ vựng và in 51 mục đầu tiên cho mục đích minh họa.

**Listing 2.2: Tạo bộ từ vựng**

```python
vocab = {token:integer for integer, token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break
```

Đầu ra là:

```
('!', 0)
('"', 1)
("'", 2)
...
('Her', 49)
('Hermia', 50)
```

Như chúng ta có thể thấy, dictionary chứa các token riêng lẻ được liên kết với nhãn số nguyên duy nhất. Mục tiêu tiếp theo của chúng ta là áp dụng bộ từ vựng này để chuyển đổi văn bản mới thành token ID (hình 2.7).

Khi chúng ta muốn chuyển đổi đầu ra của LLM từ số ngược lại thành văn bản, chúng ta cần một cách để biến token ID thành văn bản. Để làm điều này, chúng ta có thể tạo phiên bản ngược của bộ từ vựng ánh xạ token ID ngược lại các token văn bản tương ứng.

[Hình 2.7: Bắt đầu với mẫu văn bản mới, chúng ta tokenize văn bản và sử dụng bộ từ vựng để chuyển đổi token văn bản thành token ID. Bộ từ vựng được xây dựng từ toàn bộ tập huấn luyện và có thể được áp dụng cho chính tập huấn luyện cũng như bất kỳ mẫu văn bản mới nào. Bộ từ vựng được mô tả không chứa dấu câu hoặc ký tự đặc biệt cho đơn giản.]

Hãy triển khai lớp tokenizer Python hoàn chỉnh với phương thức `encode` chia văn bản thành token và thực hiện ánh xạ chuỗi-sang-số-nguyên để tạo token ID qua bộ từ vựng. Ngoài ra, chúng ta sẽ triển khai phương thức `decode` thực hiện ánh xạ ngược số-nguyên-sang-chuỗi để chuyển đổi token ID ngược lại thành văn bản. Listing sau hiển thị code cho triển khai tokenizer này.

**Listing 2.3: Triển khai tokenizer văn bản đơn giản**

```python
class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab              # Lưu bộ từ vựng làm thuộc tính lớp
                                              # để truy cập trong phương thức encode và decode
        self.int_to_str = {i:s for s,i in vocab.items()}  # Tạo bộ từ vựng ngược
                                                           # ánh xạ token ID ngược lại
                                                           # token văn bản gốc

    def encode(self, text):                  # Xử lý văn bản đầu vào thành token ID
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):                   # Chuyển token ID ngược lại thành văn bản
        text = " ".join([self.int_to_str[i] for i in ids])

        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)  # Xóa khoảng trắng trước
                                                           # các dấu câu được chỉ định
        return text
```

Sử dụng lớp Python SimpleTokenizerV1, giờ chúng ta có thể khởi tạo các đối tượng tokenizer mới qua bộ từ vựng hiện có, mà sau đó chúng ta có thể sử dụng để mã hóa và giải mã văn bản, như minh họa trong hình 2.8.

Hãy khởi tạo đối tượng tokenizer mới từ lớp SimpleTokenizerV1 và tokenize một đoạn từ truyện ngắn của Edith Wharton để thử nghiệm trong thực tế:

```python
tokenizer = SimpleTokenizerV1(vocab)
text = """"It's the last he painted, you know,"
       Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)
```

Code trước in ra các token ID sau:

```
[1, 56, 2, 850, 988, 602, 533, 746, 5, 1126, 596, 5, 1, 67, 7, 38, 851,
1108, 754, 793, 7]
```

Tiếp theo, hãy xem liệu chúng ta có thể biến các token ID này ngược lại thành văn bản sử dụng phương thức decode:

```python
print(tokenizer.decode(ids))
```

[Hình 2.8: Các triển khai tokenizer chia sẻ hai phương thức chung: phương thức encode và phương thức decode. Phương thức encode nhận văn bản mẫu, chia nó thành các token riêng lẻ, và chuyển đổi token thành token ID qua bộ từ vựng. Phương thức decode nhận token ID, chuyển đổi chúng ngược lại thành token văn bản, và nối các token văn bản thành văn bản tự nhiên.]

Đầu ra là:

```
'" It\' s the last he painted, you know," Mrs. Gisburn said with
pardonable pride.'
```

Dựa trên đầu ra này, chúng ta có thể thấy rằng phương thức decode đã chuyển đổi thành công token ID ngược lại thành văn bản gốc.

Cho đến nay, mọi thứ đều tốt. Chúng ta đã triển khai tokenizer có khả năng tokenize và detokenize văn bản dựa trên đoạn trích từ tập huấn luyện. Bây giờ hãy áp dụng nó cho mẫu văn bản mới không nằm trong tập huấn luyện:

```python
text = "Hello, do you like tea?"
print(tokenizer.encode(text))
```

Thực thi code này sẽ dẫn đến lỗi sau:

```
KeyError: 'Hello'
```

Vấn đề là từ "Hello" không được sử dụng trong truyện ngắn "The Verdict". Do đó, nó không có trong bộ từ vựng. Điều này nhấn mạnh sự cần thiết phải xem xét các tập huấn luyện lớn và đa dạng để mở rộng bộ từ vựng khi làm việc với LLM.

Tiếp theo, chúng ta sẽ kiểm tra thêm tokenizer trên văn bản chứa các từ không xác định và thảo luận các token đặc biệt bổ sung có thể được sử dụng để cung cấp thêm ngữ cảnh cho LLM trong quá trình huấn luyện.

## 2.4 Thêm token ngữ cảnh đặc biệt

Chúng ta cần sửa đổi tokenizer để xử lý các từ không xác định. Chúng ta cũng cần giải quyết việc sử dụng và bổ sung các token ngữ cảnh đặc biệt có thể nâng cao khả năng hiểu ngữ cảnh hoặc thông tin liên quan khác trong văn bản của mô hình. Các token đặc biệt này có thể bao gồm các dấu hiệu cho từ không xác định và ranh giới tài liệu, ví dụ. Đặc biệt, chúng ta sẽ sửa đổi bộ từ vựng và tokenizer, SimpleTokenizerV2, để hỗ trợ hai token mới, `<|unk|>` và `<|endoftext|>`, như minh họa trong hình 2.9.

Chúng ta có thể sửa đổi tokenizer để sử dụng token `<|unk|>` nếu nó gặp từ không thuộc bộ từ vựng. Hơn nữa, chúng ta thêm token giữa các văn bản không liên quan. Ví dụ, khi huấn luyện LLM giống GPT trên nhiều tài liệu hoặc sách độc lập, thông thường sẽ chèn token trước mỗi tài liệu hoặc sách tiếp theo sau nguồn văn bản trước đó, như minh họa trong hình 2.10. Điều này giúp LLM hiểu rằng mặc dù các nguồn văn bản này được nối lại để huấn luyện, chúng thực tế không liên quan.

[Hình 2.9: Chúng ta thêm token đặc biệt vào bộ từ vựng để xử lý một số ngữ cảnh nhất định. Ví dụ, chúng ta thêm token `<|unk|>` để đại diện cho các từ mới và không xác định không thuộc dữ liệu huấn luyện và do đó không thuộc bộ từ vựng hiện có. Hơn nữa, chúng ta thêm token `<|endoftext|>` mà chúng ta có thể sử dụng để phân tách hai nguồn văn bản không liên quan.]

[Hình 2.10: Khi làm việc với nhiều nguồn văn bản độc lập, chúng ta thêm token `<|endoftext|>` giữa các văn bản này. Các token `<|endoftext|>` này hoạt động như các dấu hiệu, báo hiệu điểm bắt đầu hoặc kết thúc của một phân đoạn cụ thể, cho phép xử lý và hiểu hiệu quả hơn bởi LLM.]

Bây giờ hãy sửa đổi bộ từ vựng để bao gồm hai token đặc biệt này, `<unk>` và `<|endoftext|>`, bằng cách thêm chúng vào danh sách tất cả từ duy nhất:

```python
all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])
vocab = {token:integer for integer, token in enumerate(all_tokens)}
print(len(vocab.items()))
```

Dựa trên đầu ra của lệnh print này, kích thước bộ từ vựng mới là 1.132 (kích thước bộ từ vựng trước đó là 1.130).

Như kiểm tra nhanh bổ sung, hãy in năm mục cuối cùng của bộ từ vựng đã cập nhật:

```python
for i, item in enumerate(list(vocab.items())[-5:]):
    print(item)
```

Code in ra:

```
('younger', 1127)
('your', 1128)
('yourself', 1129)
('<|endoftext|>', 1130)
('<|unk|>', 1131)
```

Dựa trên đầu ra code, chúng ta có thể xác nhận rằng hai token đặc biệt mới đã thực sự được kết hợp thành công vào bộ từ vựng. Tiếp theo, chúng ta điều chỉnh tokenizer từ code listing 2.3 tương ứng như hiển thị trong listing sau.

**Listing 2.4: Tokenizer văn bản đơn giản xử lý từ không xác định**

```python
class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = { i:s for s,i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        preprocessed = [item if item in self.str_to_int      # Thay thế từ không
                        else "<|unk|>" for item in preprocessed]  # xác định bằng
                                                                   # token <|unk|>
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)  # Xóa khoảng trắng trước
                                                              # các dấu câu được chỉ định
        return text
```

So với SimpleTokenizerV1 mà chúng ta đã triển khai trong listing 2.3, SimpleTokenizerV2 mới thay thế các từ không xác định bằng token `<|unk|>`.

Bây giờ hãy thử tokenizer mới này trong thực tế. Để làm điều này, chúng ta sẽ sử dụng mẫu văn bản đơn giản mà chúng ta nối từ hai câu độc lập và không liên quan:

```python
text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((text1, text2))
print(text)
```

Đầu ra là:

```
Hello, do you like tea? <|endoftext|> In the sunlit terraces of the palace.
```

Tiếp theo, hãy tokenize văn bản mẫu sử dụng SimpleTokenizerV2 trên vocab mà chúng ta đã tạo trước đó trong listing 2.2:

```python
tokenizer = SimpleTokenizerV2(vocab)
print(tokenizer.encode(text))
```

Đầu ra in ra các token ID sau:

```
[1131, 5, 355, 1126, 628, 975, 10, 1130, 55, 988, 956, 984, 722, 988, 1131, 7]
```

Chúng ta có thể thấy danh sách token ID chứa 1130 cho token phân tách `<|endoftext|>` cũng như hai token 1131, được sử dụng cho các từ không xác định.

Hãy detokenize văn bản để kiểm tra nhanh:

```python
print(tokenizer.decode(tokenizer.encode(text)))
```

Đầu ra là:

```
<|unk|>, do you like tea? <|endoftext|> In the sunlit terraces of the <|unk|>.
```

Dựa trên so sánh văn bản detokenize này với văn bản đầu vào gốc, chúng ta biết rằng tập dữ liệu huấn luyện, truyện ngắn "The Verdict" của Edith Wharton, không chứa các từ "Hello" và "palace."

Tùy thuộc vào LLM, một số nhà nghiên cứu cũng xem xét các token đặc biệt bổ sung như sau:

- **[BOS]** (beginning of sequence — đầu chuỗi) — Token này đánh dấu điểm bắt đầu của văn bản. Nó báo hiệu cho LLM nơi nội dung bắt đầu.

- **[EOS]** (end of sequence — cuối chuỗi) — Token này được đặt ở cuối văn bản và đặc biệt hữu ích khi nối nhiều văn bản không liên quan, tương tự như `<|endoftext|>`. Ví dụ, khi kết hợp hai bài viết Wikipedia hoặc sách khác nhau, token [EOS] chỉ ra nơi một bài kết thúc và bài tiếp theo bắt đầu.

- **[PAD]** (padding — đệm) — Khi huấn luyện LLM với batch size lớn hơn một, batch có thể chứa các văn bản có độ dài khác nhau. Để đảm bảo tất cả văn bản có cùng độ dài, các văn bản ngắn hơn được mở rộng hoặc "đệm" sử dụng token [PAD], lên đến độ dài của văn bản dài nhất trong batch.

Tokenizer được sử dụng cho mô hình GPT không cần bất kỳ token nào trong số này; nó chỉ sử dụng token `<|endoftext|>` cho đơn giản. `<|endoftext|>` tương tự với token [EOS]. `<|endoftext|>` cũng được sử dụng cho padding. Tuy nhiên, như chúng ta sẽ khám phá trong các chương tiếp theo, khi huấn luyện trên đầu vào theo batch, chúng ta thường sử dụng mask, nghĩa là chúng ta không chú ý đến các token padding. Do đó, token cụ thể được chọn cho padding trở nên không quan trọng.

Hơn nữa, tokenizer được sử dụng cho mô hình GPT cũng không sử dụng token `<|unk|>` cho các từ ngoài bộ từ vựng. Thay vào đó, mô hình GPT sử dụng tokenizer mã hóa cặp byte (byte pair encoding), phân tách các từ thành các đơn vị con từ (subword units), mà chúng ta sẽ thảo luận tiếp theo.

## 2.5 Mã hóa cặp byte (Byte pair encoding)

Hãy xem xét một lược đồ tokenization tinh vi hơn dựa trên khái niệm gọi là mã hóa cặp byte (BPE). Tokenizer BPE đã được sử dụng để huấn luyện các LLM như GPT-2, GPT-3, và mô hình gốc được sử dụng trong ChatGPT.

Vì việc triển khai BPE có thể khá phức tạp, chúng ta sẽ sử dụng thư viện Python mã nguồn mở có sẵn gọi là tiktoken (https://github.com/openai/tiktoken), triển khai thuật toán BPE rất hiệu quả dựa trên mã nguồn Rust. Tương tự các thư viện Python khác, chúng ta có thể cài đặt thư viện tiktoken qua trình cài đặt pip của Python từ terminal:

```
pip install tiktoken
```

Code chúng ta sẽ sử dụng dựa trên tiktoken 0.7.0. Bạn có thể sử dụng code sau để kiểm tra phiên bản bạn hiện đã cài đặt:

```python
from importlib.metadata import version
import tiktoken
print("tiktoken version:", version("tiktoken"))
```

Sau khi cài đặt, chúng ta có thể khởi tạo tokenizer BPE từ tiktoken như sau:

```python
tokenizer = tiktoken.get_encoding("gpt2")
```

Cách sử dụng tokenizer này tương tự SimpleTokenizerV2 mà chúng ta đã triển khai trước đó qua phương thức encode:

```python
text = (
    "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
     "of someunknownPlace."
)
integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
print(integers)
```

Code in ra các token ID sau:

```
[15496, 11, 466, 345, 588, 8887, 30, 220, 50256, 554, 262, 4252, 18250,
 8812, 2114, 286, 617, 34680, 27271, 13]
```

Sau đó chúng ta có thể chuyển đổi token ID ngược lại thành văn bản sử dụng phương thức decode, tương tự SimpleTokenizerV2:

```python
strings = tokenizer.decode(integers)
print(strings)
```

Code in ra:

```
Hello, do you like tea? <|endoftext|> In the sunlit terraces of someunknownPlace.
```

Chúng ta có thể đưa ra hai quan sát đáng chú ý dựa trên token ID và văn bản được giải mã. Đầu tiên, token `<|endoftext|>` được gán token ID tương đối lớn, cụ thể là 50256. Thực tế, tokenizer BPE, được sử dụng để huấn luyện các mô hình như GPT-2, GPT-3, và mô hình gốc được sử dụng trong ChatGPT, có tổng kích thước bộ từ vựng là 50.257, với `<|endoftext|>` được gán token ID lớn nhất.

Thứ hai, tokenizer BPE mã hóa và giải mã các từ không xác định, chẳng hạn như someunknownPlace, một cách chính xác. Tokenizer BPE có thể xử lý bất kỳ từ không xác định nào. Nó đạt được điều này như thế nào mà không sử dụng token `<|unk|>`?

Thuật toán nền tảng của BPE phân tách các từ không có trong bộ từ vựng được xác định trước thành các đơn vị con từ nhỏ hơn hoặc thậm chí các ký tự riêng lẻ, cho phép nó xử lý các từ ngoài bộ từ vựng. Vì vậy, nhờ thuật toán BPE, nếu tokenizer gặp một từ không quen thuộc trong quá trình tokenization, nó có thể biểu diễn nó như một chuỗi token con từ hoặc ký tự, như minh họa trong hình 2.11.

Khả năng phân tách các từ không xác định thành ký tự riêng lẻ đảm bảo rằng tokenizer và do đó LLM được huấn luyện với nó có thể xử lý bất kỳ văn bản nào, ngay cả khi nó chứa các từ không có trong dữ liệu huấn luyện.

[Hình 2.11: Tokenizer BPE phân tách các từ không xác định thành token con từ và ký tự riêng lẻ. Bằng cách này, tokenizer BPE có thể phân tích bất kỳ từ nào và không cần thay thế các từ không xác định bằng token đặc biệt, chẳng hạn như `<|unk|>`.]

Thảo luận chi tiết và triển khai BPE nằm ngoài phạm vi cuốn sách này, nhưng nói ngắn gọn, nó xây dựng bộ từ vựng bằng cách lặp đi lặp lại việc hợp nhất các ký tự thường xuyên thành con từ và các con từ thường xuyên thành từ. Ví dụ, BPE bắt đầu bằng cách thêm tất cả ký tự đơn riêng lẻ vào bộ từ vựng ("a", "b", v.v.). Trong giai đoạn tiếp theo, nó hợp nhất các tổ hợp ký tự xuất hiện thường xuyên cùng nhau thành con từ. Ví dụ, "d" và "e" có thể được hợp nhất thành con từ "de", phổ biến trong nhiều từ tiếng Anh như "define", "depend", "made", và "hidden". Các hợp nhất được xác định bởi ngưỡng tần suất.

> **Bài tập 2.1: Mã hóa cặp byte của từ không xác định**
>
> Thử tokenizer BPE từ thư viện tiktoken trên các từ không xác định "Akwirw ier" và in các token ID riêng lẻ. Sau đó, gọi hàm decode trên mỗi số nguyên kết quả trong danh sách này để tái tạo ánh xạ hiển thị trong hình 2.11. Cuối cùng, gọi phương thức decode trên token ID để kiểm tra xem nó có thể tái tạo đầu vào gốc, "Akwirw ier" hay không.

## 2.6 Lấy mẫu dữ liệu với cửa sổ trượt

Bước tiếp theo trong việc tạo nhúng cho LLM là tạo các cặp đầu vào-mục tiêu cần thiết cho huấn luyện LLM. Các cặp đầu vào-mục tiêu này trông như thế nào? Như chúng ta đã học, LLM được tiền huấn luyện bằng cách dự đoán từ tiếp theo trong văn bản, như mô tả trong hình 2.12.

[Hình 2.12: Cho trước mẫu văn bản, trích xuất các khối đầu vào dưới dạng mẫu con đóng vai trò là đầu vào cho LLM, và tác vụ dự đoán của LLM trong quá trình huấn luyện là dự đoán từ tiếp theo theo sau khối đầu vào. Trong quá trình huấn luyện, chúng ta che tất cả các từ vượt quá mục tiêu. Lưu ý rằng văn bản hiển thị trong hình này phải trải qua tokenization trước khi LLM có thể xử lý nó; tuy nhiên, hình này bỏ qua bước tokenization cho rõ ràng.]

Hãy triển khai data loader lấy các cặp đầu vào-mục tiêu trong hình 2.12 từ tập dữ liệu huấn luyện sử dụng phương pháp cửa sổ trượt. Để bắt đầu, chúng ta sẽ tokenize toàn bộ truyện ngắn "The Verdict" sử dụng tokenizer BPE:

```python
with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
enc_text = tokenizer.encode(raw_text)
print(len(enc_text))
```

Thực thi code này sẽ trả về 5145, tổng số token trong tập huấn luyện, sau khi áp dụng tokenizer BPE.

Tiếp theo, chúng ta loại bỏ 50 token đầu tiên khỏi tập dữ liệu cho mục đích trình diễn, vì nó tạo ra đoạn văn bản thú vị hơn một chút trong các bước tiếp theo:

```python
enc_sample = enc_text[50:]
```

Một trong những cách dễ nhất và trực quan nhất để tạo các cặp đầu vào-mục tiêu cho tác vụ dự đoán từ tiếp theo là tạo hai biến, x và y, trong đó x chứa các token đầu vào và y chứa các mục tiêu, là đầu vào được dịch chuyển 1 vị trí:

```python
context_size = 4        # Kích thước ngữ cảnh xác định có bao nhiêu
                        # token được bao gồm trong đầu vào.
x = enc_sample[:context_size]
y = enc_sample[1:context_size+1]
print(f"x: {x}")
print(f"y:      {y}")
```

Chạy code trước đó in ra đầu ra sau:

```
x: [290, 4920, 2241, 287]
y:      [4920, 2241, 287, 257]
```

Bằng cách xử lý đầu vào cùng với mục tiêu, là đầu vào được dịch chuyển một vị trí, chúng ta có thể tạo các tác vụ dự đoán từ tiếp theo (xem hình 2.12), như sau:

```python
for i in range(1, context_size+1):
    context = enc_sample[:i]
    desired = enc_sample[i]
    print(context, "---->", desired)
```

Code in ra:

```
[290] ----> 4920
[290, 4920] ----> 2241
[290, 4920, 2241] ----> 287
[290, 4920, 2241, 287] ----> 257
```

Mọi thứ bên trái mũi tên (---->) đề cập đến đầu vào mà LLM sẽ nhận, và token ID bên phải mũi tên đại diện cho token ID mục tiêu mà LLM cần dự đoán. Hãy lặp lại code trước nhưng chuyển đổi token ID thành văn bản:

```python
for i in range(1, context_size+1):
    context = enc_sample[:i]
    desired = enc_sample[i]
    print(tokenizer.decode(context), "---->", tokenizer.decode([desired]))
```

Đầu ra sau cho thấy đầu vào và đầu ra trông như thế nào ở dạng văn bản:

```
 and ---->  established
 and established ---->  himself
 and established himself ---->  in
 and established himself in ---->  a
```

Chúng ta đã tạo các cặp đầu vào-mục tiêu mà chúng ta có thể sử dụng cho huấn luyện LLM.

Chỉ còn một tác vụ nữa trước khi chúng ta có thể biến token thành nhúng: triển khai data loader hiệu quả lặp qua tập dữ liệu đầu vào và trả về đầu vào và mục tiêu dưới dạng tensor PyTorch, có thể được coi là mảng đa chiều. Đặc biệt, chúng ta quan tâm đến việc trả về hai tensor: tensor đầu vào chứa văn bản mà LLM thấy và tensor mục tiêu chứa các mục tiêu để LLM dự đoán, như mô tả trong hình 2.13. Mặc dù hình hiển thị token ở dạng chuỗi cho mục đích minh họa, triển khai code sẽ hoạt động trực tiếp trên token ID vì phương thức encode của tokenizer BPE thực hiện cả tokenization và chuyển đổi thành token ID trong một bước duy nhất.

[Hình 2.13: Để triển khai data loader hiệu quả, chúng ta thu thập đầu vào trong tensor x, nơi mỗi hàng đại diện cho một ngữ cảnh đầu vào. Tensor thứ hai, y, chứa các mục tiêu dự đoán tương ứng (từ tiếp theo), được tạo bằng cách dịch chuyển đầu vào một vị trí.]

> **LƯU Ý:** Để triển khai data loader hiệu quả, chúng ta sẽ sử dụng các lớp Dataset và DataLoader tích hợp của PyTorch. Để biết thêm thông tin và hướng dẫn cài đặt PyTorch, vui lòng xem phần A.2.1.3 trong phụ lục A.

Code cho lớp dataset được hiển thị trong listing sau.

**Listing 2.5: Dataset cho đầu vào và mục tiêu theo batch**

```python
import torch
from torch.utils.data import Dataset, DataLoader

class GPTDatasetV1(Dataset):
    def __init__(self, txt, tokenizer, max_length, stride):
        self.input_ids = []
        self.target_ids = []
        token_ids = tokenizer.encode(txt)   # Tokenize toàn bộ văn bản

        for i in range(0, len(token_ids) - max_length, stride):  # Sử dụng cửa sổ trượt
            input_chunk = token_ids[i:i + max_length]              # để chia sách thành
            target_chunk = token_ids[i + 1: i + max_length + 1]    # các chuỗi chồng lấp
            self.input_ids.append(torch.tensor(input_chunk))        # có độ dài max_length
            self.target_ids.append(torch.tensor(target_chunk))

    def __len__(self):             # Trả về tổng số hàng trong dataset
        return len(self.input_ids)

    def __getitem__(self, idx):    # Trả về một hàng đơn từ dataset
        return self.input_ids[idx], self.target_ids[idx]
```

Lớp GPTDatasetV1 dựa trên lớp Dataset của PyTorch và xác định cách các hàng riêng lẻ được lấy từ dataset, nơi mỗi hàng bao gồm một số token ID (dựa trên max_length) được gán cho tensor input_chunk. Tensor target_chunk chứa các mục tiêu tương ứng. Tôi khuyên bạn nên đọc tiếp để xem dữ liệu trả về từ dataset này trông như thế nào khi chúng ta kết hợp dataset với PyTorch DataLoader — điều này sẽ mang lại trực giác và sự rõ ràng bổ sung.

> **LƯU Ý:** Nếu bạn mới làm quen với cấu trúc lớp Dataset PyTorch, như hiển thị trong listing 2.5, tham khảo phần A.6 trong phụ lục A, giải thích cấu trúc và cách sử dụng tổng quát của lớp Dataset và DataLoader PyTorch.

Code sau sử dụng GPTDatasetV1 để tải đầu vào theo batch qua PyTorch DataLoader.

**Listing 2.6: Data loader để tạo batch với cặp đầu vào-mục tiêu**

```python
def create_dataloader_v1(txt, batch_size=4, max_length=256,
                         stride=128, shuffle=True, drop_last=True,
                         num_workers=0):
    tokenizer = tiktoken.get_encoding("gpt2")           # Khởi tạo tokenizer
    dataset = GPTDatasetV1(txt, tokenizer, max_length, stride)  # Tạo dataset
    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        drop_last=drop_last,    # drop_last=True bỏ batch cuối nếu ngắn hơn
                                # batch_size được chỉ định để ngăn đột biến
                                # loss trong quá trình huấn luyện.
        num_workers=num_workers  # Số tiến trình CPU sử dụng cho tiền xử lý
    )
    return dataloader
```

Hãy thử dataloader với batch size là 1 cho LLM với context size là 4 để phát triển trực giác về cách lớp GPTDatasetV1 từ listing 2.5 và hàm create_dataloader_v1 từ listing 2.6 hoạt động cùng nhau:

```python
with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
dataloader = create_dataloader_v1(
    raw_text, batch_size=1, max_length=4, stride=1, shuffle=False)
data_iter = iter(dataloader)     # Chuyển dataloader thành Python iterator
                                  # để lấy mục tiếp theo qua hàm next() tích hợp
first_batch = next(data_iter)
print(first_batch)
```

Thực thi code trước in ra:

```
[tensor([[  40,  367, 2885, 1464]]), tensor([[ 367, 2885, 1464, 1807]])]
```

Biến first_batch chứa hai tensor: tensor đầu tiên lưu token ID đầu vào, và tensor thứ hai lưu token ID mục tiêu. Vì max_length được đặt thành 4, mỗi trong hai tensor chứa bốn token ID. Lưu ý rằng kích thước đầu vào là 4 khá nhỏ và chỉ được chọn cho đơn giản. Thông thường huấn luyện LLM với kích thước đầu vào ít nhất 256.

Để hiểu ý nghĩa của stride=1, hãy lấy một batch khác từ dataset này:

```python
second_batch = next(data_iter)
print(second_batch)
```

Batch thứ hai có nội dung sau:

```
[tensor([[ 367, 2885, 1464, 1807]]), tensor([[2885, 1464, 1807, 3619]])]
```

Nếu chúng ta so sánh batch thứ nhất và thứ hai, chúng ta có thể thấy rằng token ID của batch thứ hai được dịch chuyển một vị trí (ví dụ, ID thứ hai trong đầu vào batch đầu tiên là 367, đây là ID đầu tiên của đầu vào batch thứ hai). Thiết lập stride quy định số vị trí mà đầu vào dịch chuyển qua các batch, mô phỏng phương pháp cửa sổ trượt, như trình diễn trong hình 2.14.

[Hình 2.14: Khi tạo nhiều batch từ tập dữ liệu đầu vào, chúng ta trượt cửa sổ đầu vào qua văn bản. Nếu stride được đặt thành 1, chúng ta dịch chuyển cửa sổ đầu vào một vị trí khi tạo batch tiếp theo. Nếu chúng ta đặt stride bằng kích thước cửa sổ đầu vào, chúng ta có thể ngăn chồng lấp giữa các batch.]

> **Bài tập 2.2: Data loader với stride và context size khác nhau**
>
> Để phát triển trực giác hơn về cách data loader hoạt động, hãy thử chạy nó với các thiết lập khác nhau như max_length=2 và stride=2, và max_length=8 và stride=2.

Batch size 1, như chúng ta đã lấy mẫu từ data loader cho đến nay, hữu ích cho mục đích minh họa. Nếu bạn có kinh nghiệm trước với deep learning, bạn có thể biết rằng batch size nhỏ yêu cầu ít bộ nhớ hơn trong quá trình huấn luyện nhưng dẫn đến cập nhật mô hình nhiễu hơn. Giống như trong deep learning thông thường, batch size là sự đánh đổi và là siêu tham số (hyperparameter) cần thử nghiệm khi huấn luyện LLM.

Hãy xem nhanh cách chúng ta có thể sử dụng data loader để lấy mẫu với batch size lớn hơn 1:

```python
dataloader = create_dataloader_v1(
    raw_text, batch_size=8, max_length=4, stride=4,
    shuffle=False
)
data_iter = iter(dataloader)
inputs, targets = next(data_iter)
print("Inputs:\n", inputs)
print("\nTargets:\n", targets)
```

Đầu ra:

```
Inputs:
 tensor([[   40,   367,  2885,  1464],
        [ 1807,  3619,   402,   271],
        [10899,  2138,   257,  7026],
        [15632,   438,  2016,   257],
        [  922,  5891,  1576,   438],
        [  568,   340,   373,   645],
        [ 1049,  5975,   284,   502],
        [  284,  3285,   326,    11]])

Targets:
 tensor([[  367,  2885,  1464,  1807],
        [ 3619,   402,   271, 10899],
        [ 2138,   257,  7026, 15632],
        [  438,  2016,   257,   922],
        [ 5891,  1576,   438,   568],
        [  340,   373,   645,  1049],
        [ 5975,   284,   502,   284],
        [ 3285,   326,    11,   287]])
```

Lưu ý rằng chúng ta tăng stride lên 4 để sử dụng đầy đủ tập dữ liệu (chúng ta không bỏ qua một từ nào). Điều này tránh bất kỳ chồng lấp nào giữa các batch vì nhiều chồng lấp hơn có thể dẫn đến tăng overfitting.

## 2.7 Tạo token embedding

Bước cuối cùng trong việc chuẩn bị văn bản đầu vào cho huấn luyện LLM là chuyển đổi token ID thành vector nhúng, như hiển thị trong hình 2.15. Là bước sơ bộ, chúng ta phải khởi tạo các trọng số nhúng này với giá trị ngẫu nhiên. Quá trình khởi tạo này đóng vai trò là điểm bắt đầu cho quá trình học của LLM. Trong chương 5, chúng ta sẽ tối ưu hóa trọng số nhúng như một phần của quá trình huấn luyện LLM.

[Hình 2.15: Việc chuẩn bị bao gồm tokenize văn bản, chuyển đổi token văn bản thành token ID, và chuyển đổi token ID thành vector nhúng. Ở đây, chúng ta xem xét token ID đã tạo trước đó để tạo vector nhúng token.]

Biểu diễn vector liên tục, hoặc nhúng, là cần thiết vì LLM giống GPT là mạng nơ-ron sâu được huấn luyện bằng thuật toán lan truyền ngược (backpropagation).

> **LƯU Ý:** Nếu bạn không quen với cách mạng nơ-ron được huấn luyện bằng lan truyền ngược, vui lòng đọc phần B.4 trong phụ lục A.

Hãy xem cách chuyển đổi token ID sang vector nhúng hoạt động với ví dụ thực hành. Giả sử chúng ta có bốn token đầu vào sau với ID 2, 3, 5, và 1:

```python
input_ids = torch.tensor([2, 3, 5, 1])
```

Vì lý do đơn giản, giả sử chúng ta có bộ từ vựng nhỏ chỉ gồm 6 từ (thay vì 50.257 từ trong bộ từ vựng tokenizer BPE), và chúng ta muốn tạo nhúng kích thước 3 (trong GPT-3, kích thước nhúng là 12.288 chiều):

```python
vocab_size = 6
output_dim = 3
```

Sử dụng vocab_size và output_dim, chúng ta có thể khởi tạo lớp nhúng trong PyTorch, đặt seed ngẫu nhiên là 123 cho mục đích tái tạo:

```python
torch.manual_seed(123)
embedding_layer = torch.nn.Embedding(vocab_size, output_dim)
print(embedding_layer.weight)
```

Lệnh print in ra ma trận trọng số nền tảng của lớp nhúng:

```
Parameter containing:
tensor([[ 0.3374, -0.1778, -0.1690],
        [ 0.9178,  1.5810,  1.3010],
        [ 1.2753, -0.2010, -0.1606],
        [-0.4015,  0.9666, -1.1481],
        [-1.1589,  0.3255, -0.6315],
        [-2.8400, -0.7849, -1.4096]], requires_grad=True)
```

Ma trận trọng số của lớp nhúng chứa các giá trị nhỏ, ngẫu nhiên. Các giá trị này được tối ưu hóa trong quá trình huấn luyện LLM như một phần của việc tối ưu hóa chính LLM. Hơn nữa, chúng ta có thể thấy rằng ma trận trọng số có sáu hàng và ba cột. Có một hàng cho mỗi trong sáu token có thể trong bộ từ vựng, và có một cột cho mỗi trong ba chiều nhúng.

Bây giờ, hãy áp dụng nó cho một token ID để lấy vector nhúng:

```python
print(embedding_layer(torch.tensor([3])))
```

Vector nhúng trả về là:

```
tensor([[-0.4015,  0.9666, -1.1481]], grad_fn=<EmbeddingBackward0>)
```

Nếu chúng ta so sánh vector nhúng cho token ID 3 với ma trận nhúng trước đó, chúng ta thấy nó giống hệt hàng thứ tư (Python bắt đầu với chỉ mục zero, vì vậy đó là hàng tương ứng với chỉ mục 3). Nói cách khác, lớp nhúng về cơ bản là phép tra cứu (lookup operation) truy xuất các hàng từ ma trận trọng số của lớp nhúng qua token ID.

> **LƯU Ý:** Đối với những ai quen thuộc với mã hóa one-hot, phương pháp lớp nhúng được mô tả ở đây về cơ bản chỉ là cách triển khai hiệu quả hơn của mã hóa one-hot theo sau bằng phép nhân ma trận trong lớp kết nối đầy đủ, được minh họa trong code bổ sung trên GitHub tại https://mng.bz/ZEB5. Bởi vì lớp nhúng chỉ là triển khai hiệu quả hơn tương đương với phương pháp mã hóa one-hot và nhân ma trận, nó có thể được coi là lớp mạng nơ-ron có thể được tối ưu hóa qua lan truyền ngược.

[Hình 2.16: Lớp nhúng thực hiện phép tra cứu, truy xuất vector nhúng tương ứng với token ID từ ma trận trọng số của lớp nhúng. Ví dụ, vector nhúng của token ID 5 là hàng thứ sáu của ma trận trọng số lớp nhúng (đó là hàng thứ sáu thay vì thứ năm vì Python bắt đầu đếm từ 0). Chúng ta giả sử rằng token ID được tạo bởi bộ từ vựng nhỏ từ phần 2.3.]

Chúng ta đã thấy cách chuyển đổi một token ID đơn thành vector nhúng ba chiều. Bây giờ hãy áp dụng điều đó cho tất cả bốn ID đầu vào (torch.tensor([2, 3, 5, 1])):

```python
print(embedding_layer(input_ids))
```

Đầu ra print cho thấy kết quả là ma trận 4 × 3:

```
tensor([[ 1.2753, -0.2010, -0.1606],
        [-0.4015,  0.9666, -1.1481],
        [-2.8400, -0.7849, -1.4096],
        [ 0.9178,  1.5810,  1.3010]], grad_fn=<EmbeddingBackward0>)
```

Mỗi hàng trong ma trận đầu ra này được lấy qua phép tra cứu từ ma trận trọng số nhúng, như minh họa trong hình 2.16.

Sau khi tạo vector nhúng từ token ID, tiếp theo chúng ta sẽ thêm một sửa đổi nhỏ vào các vector nhúng này để mã hóa thông tin vị trí về token trong văn bản.

## 2.8 Mã hóa vị trí từ

Về nguyên tắc, nhúng token là đầu vào phù hợp cho LLM. Tuy nhiên, một nhược điểm nhỏ của LLM là cơ chế self-attention của chúng (xem chương 3) không có khái niệm về vị trí hoặc thứ tự cho các token trong chuỗi. Cách lớp nhúng đã giới thiệu trước đó hoạt động là cùng token ID luôn được ánh xạ sang cùng biểu diễn vector, bất kể token ID nằm ở đâu trong chuỗi đầu vào, như hiển thị trong hình 2.17.

[Hình 2.17: Lớp nhúng chuyển đổi token ID thành cùng biểu diễn vector bất kể nó nằm ở đâu trong chuỗi đầu vào. Ví dụ, token ID 5, dù ở vị trí đầu tiên hay thứ tư trong vector token ID đầu vào, sẽ cho ra cùng vector nhúng.]

Về nguyên tắc, nhúng xác định, không phụ thuộc vị trí của token ID là tốt cho mục đích tái tạo. Tuy nhiên, vì cơ chế self-attention của LLM tự nó cũng không nhận biết vị trí, việc đưa thêm thông tin vị trí vào LLM là hữu ích.

Để đạt được điều này, chúng ta có thể sử dụng hai loại nhúng nhận biết vị trí: nhúng vị trí tương đối (relative positional embeddings) và nhúng vị trí tuyệt đối (absolute positional embeddings). Nhúng vị trí tuyệt đối được liên kết trực tiếp với các vị trí cụ thể trong chuỗi. Cho mỗi vị trí trong chuỗi đầu vào, một nhúng duy nhất được thêm vào nhúng của token để truyền đạt vị trí chính xác của nó. Ví dụ, token đầu tiên sẽ có nhúng vị trí cụ thể, token thứ hai có nhúng khác biệt khác, và cứ thế, như minh họa trong hình 2.18.

[Hình 2.18: Nhúng vị trí được thêm vào vector nhúng token để tạo nhúng đầu vào cho LLM. Vector vị trí có cùng chiều với nhúng token gốc. Nhúng token được hiển thị với giá trị 1 cho đơn giản.]

Thay vì tập trung vào vị trí tuyệt đối của token, trọng tâm của nhúng vị trí tương đối là vị trí hoặc khoảng cách tương đối giữa các token. Điều này có nghĩa là mô hình học các mối quan hệ về "cách xa bao nhiêu" thay vì "ở vị trí chính xác nào". Ưu điểm ở đây là mô hình có thể tổng quát hóa tốt hơn cho các chuỗi có độ dài khác nhau, ngay cả khi nó chưa thấy các độ dài như vậy trong quá trình huấn luyện.

Cả hai loại nhúng vị trí đều nhằm tăng cường khả năng của LLM trong việc hiểu thứ tự và mối quan hệ giữa các token, đảm bảo dự đoán chính xác hơn và nhận biết ngữ cảnh hơn. Sự lựa chọn giữa chúng thường phụ thuộc vào ứng dụng cụ thể và bản chất của dữ liệu được xử lý.

Mô hình GPT của OpenAI sử dụng nhúng vị trí tuyệt đối được tối ưu hóa trong quá trình huấn luyện thay vì cố định hoặc được xác định trước như mã hóa vị trí trong mô hình transformer gốc. Quá trình tối ưu hóa này là một phần của quá trình huấn luyện mô hình. Bây giờ, hãy tạo nhúng vị trí ban đầu để tạo đầu vào LLM.

Trước đây, chúng ta tập trung vào kích thước nhúng rất nhỏ cho đơn giản. Bây giờ, hãy xem xét kích thước nhúng thực tế và hữu ích hơn và mã hóa token đầu vào thành biểu diễn vector 256 chiều, nhỏ hơn mô hình GPT-3 gốc sử dụng (trong GPT-3, kích thước nhúng là 12.288 chiều) nhưng vẫn hợp lý cho thử nghiệm. Hơn nữa, chúng ta giả sử rằng token ID được tạo bởi tokenizer BPE mà chúng ta đã triển khai trước đó, có kích thước bộ từ vựng 50.257:

```python
vocab_size = 50257
output_dim = 256
token_embedding_layer = torch.nn.Embedding(vocab_size, output_dim)
```

Sử dụng token_embedding_layer trước đó, nếu chúng ta lấy mẫu dữ liệu từ data loader, chúng ta nhúng mỗi token trong mỗi batch thành vector 256 chiều. Nếu chúng ta có batch size là 8 với bốn token mỗi batch, kết quả sẽ là tensor 8 × 4 × 256.

Hãy khởi tạo data loader (xem phần 2.6) trước:

```python
max_length = 4
dataloader = create_dataloader_v1(
    raw_text, batch_size=8, max_length=max_length,
    stride=max_length, shuffle=False
)
data_iter = iter(dataloader)
inputs, targets = next(data_iter)
print("Token IDs:\n", inputs)
print("\nInputs shape:\n", inputs.shape)
```

Code in ra:

```
Token IDs:
 tensor([[   40,   367,  2885,  1464],
        [ 1807,  3619,   402,   271],
        [10899,  2138,   257,  7026],
        [15632,   438,  2016,   257],
        [  922,  5891,  1576,   438],
        [  568,   340,   373,   645],
        [ 1049,  5975,   284,   502],
        [  284,  3285,   326,    11]])

Inputs shape:
 torch.Size([8, 4])
```

Như chúng ta có thể thấy, tensor token ID có chiều 8 × 4, nghĩa là batch dữ liệu gồm tám mẫu văn bản với bốn token mỗi mẫu.

Bây giờ hãy sử dụng lớp nhúng để nhúng các token ID này thành vector 256 chiều:

```python
token_embeddings = token_embedding_layer(inputs)
print(token_embeddings.shape)
```

Lệnh gọi hàm print trả về:

```
torch.Size([8, 4, 256])
```

Tensor đầu ra 8 × 4 × 256 chiều cho thấy mỗi token ID giờ đã được nhúng thành vector 256 chiều.

Đối với phương pháp nhúng tuyệt đối của mô hình GPT, chúng ta chỉ cần tạo một lớp nhúng khác có cùng chiều nhúng như token_embedding_layer:

```python
context_length = max_length
pos_embedding_layer = torch.nn.Embedding(context_length, output_dim)
pos_embeddings = pos_embedding_layer(torch.arange(context_length))
print(pos_embeddings.shape)
```

Đầu vào cho pos_embeddings thường là vector placeholder torch.arange(context_length), chứa chuỗi số 0, 1, ..., đến kích thước đầu vào tối đa −1. context_length là biến đại diện cho kích thước đầu vào được hỗ trợ của LLM. Ở đây, chúng ta chọn nó tương tự như độ dài tối đa của văn bản đầu vào. Trong thực tế, văn bản đầu vào có thể dài hơn kích thước ngữ cảnh được hỗ trợ, trong trường hợp đó chúng ta phải cắt ngắn văn bản.

Đầu ra của lệnh print là:

```
torch.Size([4, 256])
```

Như chúng ta có thể thấy, tensor nhúng vị trí bao gồm bốn vector 256 chiều. Giờ chúng ta có thể thêm trực tiếp chúng vào nhúng token, nơi PyTorch sẽ cộng tensor pos_embeddings 4 × 256 chiều vào mỗi tensor nhúng token 4 × 256 chiều trong mỗi batch trong tám batch:

```python
input_embeddings = token_embeddings + pos_embeddings
print(input_embeddings.shape)
```

Đầu ra print là:

```
torch.Size([8, 4, 256])
```

[Hình 2.19: Là một phần của pipeline xử lý đầu vào, văn bản đầu vào trước tiên được chia thành các token riêng lẻ. Các token này được chuyển đổi thành token ID sử dụng bộ từ vựng. Token ID được chuyển đổi thành vector nhúng mà nhúng vị trí có kích thước tương tự được thêm vào, tạo ra nhúng đầu vào được sử dụng làm đầu vào cho các lớp LLM chính.]

input_embeddings mà chúng ta đã tạo, như tóm tắt trong hình 2.19, là các ví dụ đầu vào đã nhúng có thể được xử lý bởi các module LLM chính, mà chúng ta sẽ bắt đầu triển khai trong chương tiếp theo.

## Tóm tắt

- LLM yêu cầu dữ liệu văn bản được chuyển đổi thành vector số, gọi là nhúng (embedding), vì chúng không thể xử lý văn bản thô. Nhúng chuyển đổi dữ liệu rời rạc (như từ hoặc hình ảnh) thành không gian vector liên tục, làm cho chúng tương thích với các phép toán mạng nơ-ron.

- Là bước đầu tiên, văn bản thô được chia thành token, có thể là từ hoặc ký tự. Sau đó, token được chuyển đổi thành biểu diễn số nguyên, gọi là token ID.

- Các token đặc biệt, chẳng hạn như `<|unk|>` và `<|endoftext|>`, có thể được thêm vào để nâng cao khả năng hiểu của mô hình và xử lý các ngữ cảnh khác nhau, chẳng hạn như từ không xác định hoặc đánh dấu ranh giới giữa các văn bản không liên quan.

- Tokenizer mã hóa cặp byte (BPE) được sử dụng cho LLM như GPT-2 và GPT-3 có thể xử lý hiệu quả các từ không xác định bằng cách phân tách chúng thành đơn vị con từ hoặc ký tự riêng lẻ.

- Chúng ta sử dụng phương pháp cửa sổ trượt trên dữ liệu đã tokenize để tạo cặp đầu vào-mục tiêu cho huấn luyện LLM.

- Lớp nhúng trong PyTorch hoạt động như phép tra cứu, truy xuất vector tương ứng với token ID. Các vector nhúng kết quả cung cấp biểu diễn liên tục của token, điều cực kỳ quan trọng cho huấn luyện các mô hình deep learning như LLM.

- Mặc dù nhúng token cung cấp biểu diễn vector nhất quán cho mỗi token, chúng thiếu ý thức về vị trí của token trong chuỗi. Để khắc phục điều này, có hai loại nhúng vị trí chính: tuyệt đối và tương đối. Mô hình GPT của OpenAI sử dụng nhúng vị trí tuyệt đối, được thêm vào vector nhúng token và được tối ưu hóa trong quá trình huấn luyện mô hình.
