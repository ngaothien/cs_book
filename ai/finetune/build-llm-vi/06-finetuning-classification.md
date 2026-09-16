# Chương 6: Tinh chỉnh cho tác vụ phân loại (Fine-tuning for classification)

Đến giờ, chúng ta đã lập trình kiến trúc LLM, tiền huấn luyện nó, và học cách nạp (import) các trọng số đã được huấn luyện trước từ một nguồn bên ngoài, chẳng hạn như OpenAI, vào mô hình của mình. Bây giờ là lúc chúng ta gặt hái thành quả bằng cách tinh chỉnh (fine-tune) LLM trên một tác vụ đích cụ thể, chẳng hạn như phân loại văn bản (text classification). Ví dụ cụ thể mà chúng ta xem xét là phân loại các tin nhắn văn bản là "spam" (thư rác) hoặc "not spam" (không phải thư rác). Hình 6.1 nhấn mạnh hai cách chính để tinh chỉnh một LLM: tinh chỉnh cho phân loại (bước 8) và tinh chỉnh để tuân theo chỉ dẫn (bước 9).

*Chương này bao gồm:*
- *Giới thiệu các phương pháp tinh chỉnh LLM khác nhau*
- *Chuẩn bị bộ dữ liệu để phân loại văn bản*
- *Sửa đổi LLM đã tiền huấn luyện để phục vụ việc tinh chỉnh*
- *Tinh chỉnh LLM để nhận diện tin nhắn rác (spam)*
- *Đánh giá độ chính xác của LLM phân loại sau khi tinh chỉnh*
- *Sử dụng LLM đã tinh chỉnh để phân loại dữ liệu mới*

[Hình 6.1: Ba giai đoạn chính trong việc lập trình một LLM. Chương này tập trung vào giai đoạn 3 (bước 8): tinh chỉnh một LLM đã được tiền huấn luyện thành một mô hình phân loại.]

## 6.1 Các danh mục tinh chỉnh khác nhau

Các cách phổ biến nhất để tinh chỉnh mô hình ngôn ngữ là tinh chỉnh chỉ dẫn (instruction fine-tuning) và tinh chỉnh phân loại (classification fine-tuning). Tinh chỉnh chỉ dẫn liên quan đến việc huấn luyện mô hình ngôn ngữ trên một tập hợp các tác vụ sử dụng những chỉ dẫn cụ thể để cải thiện khả năng hiểu và thực thi các tác vụ được mô tả trong các câu lệnh (prompt) ngôn ngữ tự nhiên, như minh họa trong hình 6.2. 

Trong tinh chỉnh phân loại, một khái niệm mà bạn có thể đã quen thuộc nếu có nền tảng về học máy (machine learning), mô hình được huấn luyện để nhận diện một tập hợp cụ thể các nhãn lớp (class label), ví dụ như "spam" (thư rác) và "not spam" (không phải thư rác). Các ví dụ về tác vụ phân loại không chỉ dừng lại ở LLM và lọc email: chúng còn bao gồm nhận dạng các loài thực vật khác nhau từ hình ảnh; phân loại tin tức thành các chủ đề như thể thao, chính trị và công nghệ; hay phân biệt giữa khối u lành tính và ác tính trong hình ảnh y tế.

[Hình 6.2: Hai kịch bản tinh chỉnh chỉ dẫn khác nhau. Ở trên cùng, mô hình được giao nhiệm vụ xác định xem một đoạn văn bản có phải là spam hay không. Ở dưới cùng, mô hình được cấp một chỉ dẫn về cách dịch một câu tiếng Anh sang tiếng Đức.]

Điểm cốt lõi là một mô hình tinh chỉnh phân loại bị giới hạn trong việc dự đoán các lớp mà nó đã tiếp xúc trong quá trình huấn luyện. Ví dụ, nó có thể xác định xem một thứ là "spam" hay "not spam", như minh họa trong hình 6.3, nhưng nó không thể nói thêm bất cứ điều gì khác về đoạn văn bản đầu vào.

Trái ngược với mô hình tinh chỉnh phân loại mô tả ở hình 6.3, một mô hình tinh chỉnh chỉ dẫn thường có thể đảm nhiệm một phạm vi tác vụ rộng hơn. Chúng ta có thể coi một mô hình tinh chỉnh phân loại là mô hình có tính chuyên biệt cao, và về cơ bản, việc phát triển một mô hình chuyên biệt (specialized model) luôn dễ dàng hơn việc phát triển một mô hình tổng quát (generalist model) hoạt động tốt trên nhiều tác vụ khác nhau.

**Chọn đúng phương pháp tiếp cận**
Tinh chỉnh chỉ dẫn cải thiện khả năng hiểu và sinh ra phản hồi dựa trên những chỉ dẫn cụ thể của người dùng. Tinh chỉnh chỉ dẫn phù hợp nhất cho các mô hình cần xử lý nhiều loại tác vụ dựa trên các chỉ dẫn phức tạp, giúp tăng tính linh hoạt và chất lượng tương tác. Tinh chỉnh phân loại là lý tưởng cho các dự án yêu cầu việc phân chia dữ liệu chính xác vào các lớp định trước, chẳng hạn như phân tích cảm xúc (sentiment analysis) hoặc phát hiện spam.

Dù tinh chỉnh chỉ dẫn linh hoạt hơn, nó lại đòi hỏi các tập dữ liệu lớn hơn và sức mạnh tính toán cao hơn để phát triển các mô hình thành thạo nhiều tác vụ. Ngược lại, tinh chỉnh phân loại cần ít dữ liệu và sức mạnh tính toán hơn, nhưng phạm vi sử dụng của nó bị giới hạn trong các lớp mà mô hình đã được huấn luyện.

[Hình 6.3: Kịch bản phân loại văn bản sử dụng một LLM. Mô hình được tinh chỉnh cho việc phân loại spam không yêu cầu thêm chỉ dẫn nào đi kèm đầu vào. Khác với mô hình tinh chỉnh chỉ dẫn, nó chỉ có thể trả lời "spam" hoặc "not spam".]

## 6.2 Chuẩn bị tập dữ liệu

Chúng ta sẽ sửa đổi và tinh chỉnh phân loại mô hình GPT mà chúng ta đã triển khai và tiền huấn luyện trước đó. Ta bắt đầu bằng việc tải về và chuẩn bị bộ dữ liệu, như được nêu bật trong hình 6.4. Để cung cấp một ví dụ thực tế và trực quan về tinh chỉnh phân loại, chúng ta sẽ làm việc với một tập dữ liệu tin nhắn bao gồm tin nhắn spam (rác) và non-spam (bình thường).

> **LƯU Ý**
> Các tin nhắn văn bản thường được gửi qua điện thoại, không phải email. Tuy nhiên, các bước thực hiện vẫn tương tự đối với phân loại email spam, và những độc giả quan tâm có thể tìm thấy các liên kết đến bộ dữ liệu phân loại email spam ở Phụ lục B.

[Hình 6.4: Quy trình 3 giai đoạn để tinh chỉnh phân loại một LLM. Giai đoạn 1 liên quan đến chuẩn bị dữ liệu. Giai đoạn 2 tập trung vào việc thiết lập mô hình. Giai đoạn 3 bao gồm tinh chỉnh và đánh giá mô hình.]

Bước đầu tiên là tải xuống tập dữ liệu.

**Listing 6.1: Tải xuống và giải nén bộ dữ liệu**

```python
import urllib.request
import zipfile
import os
from pathlib import Path

url = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"
zip_path = "sms_spam_collection.zip"
extracted_path = "sms_spam_collection"
data_file_path = Path(extracted_path) / "SMSSpamCollection.tsv"

def download_and_unzip_spam_data(url, zip_path, extracted_path, data_file_path):
    if data_file_path.exists():
        print(f"{data_file_path} already exists. Skipping download and extraction.")
        return
        
    with urllib.request.urlopen(url) as response:   
        with open(zip_path, "wb") as out_file:
            out_file.write(response.read())
            
    with zipfile.ZipFile(zip_path, "r") as zip_ref:   
        zip_ref.extractall(extracted_path)
        
    original_file_path = Path(extracted_path) / "SMSSpamCollection"
    os.rename(original_file_path, data_file_path)              
    print(f"File downloaded and saved as {data_file_path}")

download_and_unzip_spam_data(url, zip_path, extracted_path, data_file_path)
```

Sau khi chạy đoạn code trước, tập dữ liệu sẽ được lưu dưới dạng file văn bản phân cách bằng tab, `SMSSpamCollection.tsv`, trong thư mục `sms_spam_collection`. Chúng ta có thể nạp nó vào một pandas DataFrame như sau:

```python
import pandas as pd

df = pd.read_csv(
    data_file_path, sep="\t", header=None, names=["Label", "Text"]
)
df     
```

Hình 6.5 hiển thị kết quả khung dữ liệu (data frame) của tập dữ liệu spam.

[Hình 6.5: Xem trước tập dữ liệu SMSSpamCollection trong pandas DataFrame, hiển thị các class label ("ham" hoặc "spam") và tin nhắn tương ứng. Tập dữ liệu bao gồm 5.572 hàng (tin nhắn và nhãn).]

Hãy xem xét phân phối của các nhãn (class label):

```python
print(df["Label"].value_counts())
```

Chạy code trên, chúng ta nhận thấy rằng dữ liệu chứa "ham" (không phải spam) thường xuyên hơn rất nhiều so với "spam":

```
Label
ham     4825
spam     747
Name: count, dtype: int64
```

Để cho đơn giản, và vì chúng ta muốn một tập dữ liệu nhỏ (điều này sẽ tạo điều kiện cho LLM tinh chỉnh nhanh hơn), chúng ta chọn undersample (lấy mẫu theo thiểu số) tập dữ liệu để lấy ra 747 mẫu cho mỗi lớp.

> **LƯU Ý**
> Có nhiều phương pháp khác để xử lý việc mất cân bằng lớp (class imbalance), nhưng chúng nằm ngoài phạm vi cuốn sách này. Độc giả quan tâm khám phá thêm các phương pháp đối phó dữ liệu mất cân bằng có thể tham khảo thêm thông tin ở Phụ lục B.

Chúng ta có thể sử dụng code trong listing sau để undersample và tạo một bộ dữ liệu cân bằng (balanced dataset).

**Listing 6.2: Tạo tập dữ liệu cân bằng**

```python
def create_balanced_dataset(df):
    num_spam = df[df["Label"] == "spam"].shape[0]    
    ham_subset = df[df["Label"] == "ham"].sample(
        num_spam, random_state=123
    )                                        
    balanced_df = pd.concat([
        ham_subset, df[df["Label"] == "spam"]
    ])                              
    return balanced_df

balanced_df = create_balanced_dataset(df)
print(balanced_df["Label"].value_counts())
```

Sau khi thực thi đoạn code để cân bằng dữ liệu, chúng ta thấy rằng giờ đây số lượng tin nhắn spam và non-spam đã bằng nhau:

```
Label
ham     747
spam    747
Name: count, dtype: int64
```

Tiếp theo, chúng ta chuyển đổi chuỗi nhãn "ham" và "spam" sang số nguyên `0` và `1`:

```python
balanced_df["Label"] = balanced_df["Label"].map({"ham": 0, "spam": 1})
```

Quá trình này cũng tương tự như chuyển văn bản thành ID token. Tuy nhiên, thay vì dùng từ vựng GPT chứa hơn 50.000 từ, ta đang xử lý chỉ 2 giá trị: 0 và 1.

Tiếp theo, ta tạo hàm `random_split` để chia dữ liệu thành 3 phần: 70% huấn luyện, 10% xác thực, và 20% kiểm thử. (Tỷ lệ này là phổ biến trong máy học để huấn luyện, căn chỉnh và đánh giá mô hình).

**Listing 6.3: Phân chia tập dữ liệu**

```python
def random_split(df, train_frac, validation_frac):
    df = df.sample(
        frac=1, random_state=123
    ).reset_index(drop=True)              
    
    train_end = int(len(df) * train_frac)         
    validation_end = train_end + int(len(df) * validation_frac)
                                 
    train_df = df[:train_end]
    validation_df = df[train_end:validation_end]
    test_df = df[validation_end:]
    
    return train_df, validation_df, test_df

train_df, validation_df, test_df = random_split(
    balanced_df, 0.7, 0.1)                    
```

Hãy lưu dữ liệu lại dưới dạng CSV để dễ dàng gọi lại:

```python
train_df.to_csv("train.csv", index=None)
validation_df.to_csv("validation.csv", index=None)
test_df.to_csv("test.csv", index=None)
```

Từ nãy đến giờ, ta đã tải dữ liệu, cân bằng nó, và cắt nó thành tập dữ liệu đánh giá và huấn luyện. Kế đến, ta thiết lập PyTorch data loader để feed cho mô hình.

## 6.3 Tạo Data Loaders

Chúng ta sẽ phát triển các PyTorch data loader về mặt ý tưởng tương tự như lúc thao tác với dữ liệu văn bản. Trước đó, ta áp dụng cửa sổ trượt (sliding window) để chia block văn bản thành những đoạn chung độ dài, làm batch huấn luyện mô hình hiệu quả hơn. Tuy vậy, tập dữ liệu spam này có các tin nhắn dài ngắn khác nhau, ta đối mặt hai lựa chọn:
- Cắt xén (Truncate) tất cả tin nhắn bằng tin nhắn ngắn nhất.
- Chèn thêm (Pad) tin nhắn bằng tin nhắn dài nhất.

Lựa chọn thứ nhất ít hao tổn máy móc, nhưng mất thông tin vô cùng lớn. Nên ta chọn phương án số hai. Đảm bảo toàn bộ nội dung trong câu. 

Để triển khai batching, padding độ dài câu dài nhất, ta chèn thêm "padding tokens" cho các câu ngắn hơn. Mục đích này, ta dùng `<|endoftext|>` làm padding token.

Thay vì nối thẳng chuỗi `<|endoftext|>` vào chữ gốc, ta sẽ thêm mã số token ID gắn với nó vào bộ encode, được hình ảnh hóa ở Hình 6.6. `50256` là token padding của `<|endoftext|>`. Chúng ta test xem có đúng thế không:

```python
import tiktoken
tokenizer = tiktoken.get_encoding("gpt2")
print(tokenizer.encode("<|endoftext|>", allowed_special={"<|endoftext|>"}))
```
Trả về đúng là `[50256]`.

Đầu tiên, phải thiết lập Pytorch Dataset để xác định logic load/xử lý. Hàm `SpamDataset` giúp chúng ta triển khai ý đồ mô tả trong hình 6.6, nó quét từ dài nhất, token hóa, đảm bảo các dãy khác được chèn thêm pad token vào.

[Hình 6.6: Giai đoạn chuẩn bị đầu vào chữ. Token hóa. Kiểm tra tin nhắn dài nhất và pad token ID `50256` đệm vào để khớp size.]

**Listing 6.4: Thiết lập lớp Pytorch Dataset**

```python
import torch
from torch.utils.data import Dataset

class SpamDataset(Dataset):
    def __init__(self, csv_file, tokenizer, max_length=None,
                 pad_token_id=50256):
        self.data = pd.read_csv(csv_file)
                                            
        self.encoded_texts = [
            tokenizer.encode(text) for text in self.data["Text"]
        ]
        
        if max_length is None:
            self.max_length = self._longest_encoded_length()
        else:
            self.max_length = max_length
            
            # Cắt xén nếu câu dài hơn max_length
            self.encoded_texts = [
                encoded_text[:self.max_length]
                for encoded_text in self.encoded_texts
            ]
                                         
        # Pad padding token vào sau
        self.encoded_texts = [
            encoded_text + [pad_token_id] * 
            (self.max_length - len(encoded_text))
            for encoded_text in self.encoded_texts
        ]

    def __getitem__(self, index):
        encoded = self.encoded_texts[index]
        label = self.data.iloc[index]["Label"]
        return (
            torch.tensor(encoded, dtype=torch.long),
            torch.tensor(label, dtype=torch.long)
        )

    def __len__(self):
        return len(self.data)

    def _longest_encoded_length(self):
        max_length = 0
        for encoded_text in self.encoded_texts:
            encoded_length = len(encoded_text)
            if encoded_length > max_length:
                max_length = encoded_length
        return max_length
```

Tạo bộ dữ liệu thông qua DataLoader sẽ giúp ta train batch. Chạy bộ data này xem:

```python
train_dataset = SpamDataset(
    csv_file="train.csv",
    max_length=None,
    tokenizer=tokenizer
)
```

Chiều dài chuỗi lớn nhất ghim vào `max_length`. Kiểm tra token nhiều nhất:

```python
print(train_dataset.max_length)
```
Nó in ra `120`, độ dài thường thấy của các tin nhắn điện thoại. Cấu trúc mô hình ăn được 1,024 context, nhưng cho data bé này, ta dùng `120`. 

Chèn pad vô val/test dataset để khớp với số đó:

```python
val_dataset = SpamDataset(
    csv_file="validation.csv",
    max_length=train_dataset.max_length,
    tokenizer=tokenizer
)
test_dataset = SpamDataset(
    csv_file="test.csv",
    max_length=train_dataset.max_length,
    tokenizer=tokenizer
)
```

Mỗi bộ batch gồm `batch_size=8`, tức là 8 tin nhắn xếp thành cột 120 số nguyên token IDs, và 8 label theo kèm (0 hoặc 1). Minh họa tại hình 6.7.

> **Bài tập 6.1 Tăng độ dài context**
> Thử pad độ lớn đầu vào đến max số token mô hình chịu đựng xem nó tác động sao đến sức dự đoán (predictive performance).

[Hình 6.7: Mô hình 1 tập huấn luyện 8 tin nhắn, mỗi dòng chứa 120 tokens, đi kèm 1 vector label 0 1.]

**Listing 6.5: Tạo PyTorch data loaders**

```python
from torch.utils.data import DataLoader

num_workers = 0     
batch_size = 8
torch.manual_seed(123)

train_loader = DataLoader(
    dataset=train_dataset,
    batch_size=batch_size,
    shuffle=True,
    num_workers=num_workers,
    drop_last=True,
)

val_loader = DataLoader(
    dataset=val_dataset,
    batch_size=batch_size,
    num_workers=num_workers,
    drop_last=False,
)

test_loader = DataLoader(
    dataset=test_dataset,
    batch_size=batch_size,
    num_workers=num_workers,
    drop_last=False,
)
```

Tets batch đầu:

```python
for input_batch, target_batch in train_loader:
    pass
print("Input batch dimensions:", input_batch.shape)
print("Label batch dimensions", target_batch.shape)
```
In ra `torch.Size([8, 120])` và `torch.Size([8])`. Quá chuẩn.

## 6.4 Khởi tạo mô hình với các trọng số đã huấn luyện trước

Chúng ta phải chuẩn bị mô hình cho việc tinh chỉnh phân loại để xác định tin nhắn spam. Ta bắt đầu bằng cách khởi tạo mô hình đã được tiền huấn luyện của mình, như làm nổi bật trong Hình 6.8.

Để bắt đầu quá trình chuẩn bị mô hình, chúng ta sử dụng cùng một cấu hình mà ta đã sử dụng để tiền huấn luyện dữ liệu không nhãn:

```python
CHOOSE_MODEL = "gpt2-small (124M)"
INPUT_PROMPT = "Every effort moves"

BASE_CONFIG = {
    "vocab_size": 50257,         
    "context_length": 1024,      
    "drop_rate": 0.0,            
    "qkv_bias": True             
}

model_configs = {
    "gpt2-small (124M)": {"emb_dim": 768, "n_layers": 12, "n_heads": 12},
    "gpt2-medium (355M)": {"emb_dim": 1024, "n_layers": 24, "n_heads": 16},
    "gpt2-large (774M)": {"emb_dim": 1280, "n_layers": 36, "n_heads": 20},
    "gpt2-xl (1558M)": {"emb_dim": 1600, "n_layers": 48, "n_heads": 25},
}

BASE_CONFIG.update(model_configs[CHOOSE_MODEL])
```

[Hình 6.8: Giai đoạn 2 thiết lập model. Sau phần chuẩn bị dữ liệu, tải pretrained weights vào LLM kiến trúc.]

Kế tiếp, ta nhập `download_and_load_gpt2` từ file `gpt_download.py` và lấy lại `GPTModel` cùng hàm `load_weights_into_gpt` (ở Chương 5) để gán weights GPT.

**Listing 6.6: Nạp một mô hình GPT đã huấn luyện trước**

```python
from gpt_download import download_and_load_gpt2
from chapter05 import GPTModel, load_weights_into_gpt

model_size = CHOOSE_MODEL.split(" ")[-1].lstrip("(").rstrip(")")
settings, params = download_and_load_gpt2(
    model_size=model_size, models_dir="gpt2"
)

model = GPTModel(BASE_CONFIG)
load_weights_into_gpt(model, params)
model.eval()
```

Sau khi nạp xong, ta thử xem sức sinh từ của nó với hàm tiện ích `generate_text_simple`:

```python
from chapter04 import generate_text_simple
from chapter05 import text_to_token_ids, token_ids_to_text

text_1 = "Every effort moves you"
token_ids = generate_text_simple(
    model=model,
    idx=text_to_token_ids(text_1, tokenizer),
    max_new_tokens=15,
    context_size=BASE_CONFIG["context_length"]
)
print(token_ids_to_text(token_ids, tokenizer))
```

Every effort moves you forward.
The first step is to understand the importance of your work
```

Trước khi bắt đầu tinh chỉnh mô hình như một bộ phân loại spam, hãy thử xem liệu mô hình có phân loại được tin nhắn spam không khi ta thêm các chỉ dẫn (instructions) vào câu lệnh:

```python
text_2 = (
    "Is the following text 'spam'? Answer with 'yes' or 'no':"
    " 'You are a winner you have been specially"
    " selected to receive $1000 cash or a $2000 award.'"
)

token_ids = generate_text_simple(
    model=model,
    idx=text_to_token_ids(text_2, tokenizer),
    max_new_tokens=23,
    context_size=BASE_CONFIG["context_length"]
)

print(token_ids_to_text(token_ids, tokenizer))
```

Đầu ra của mô hình là:

```
Is the following text 'spam'? Answer with 'yes' or 'no': 'You are a winner
you have been specially selected to receive $1000 cash 
or a $2000 award.'
The following text 'spam'? Answer with 'yes' or 'no': 'You are a winner
```

Dựa trên đầu ra này, có thể thấy rõ rằng mô hình đang gặp khó khăn trong việc làm theo chỉ dẫn. Kết quả này là dễ hiểu, vì nó chỉ mới trải qua tiền huấn luyện (pretraining) và thiếu tinh chỉnh chỉ dẫn (instruction fine-tuning). Vì vậy, hãy chuẩn bị mô hình cho quá trình tinh chỉnh phân loại.

## 6.5 Thêm một "đầu" phân loại (classification head)

Chúng ta phải sửa đổi LLM đã tiền huấn luyện để chuẩn bị cho tinh chỉnh phân loại. Để làm điều này, chúng ta thay thế lớp đầu ra gốc, vốn ánh xạ biểu diễn ẩn tới một từ vựng gồm 50.257 token, bằng một lớp đầu ra nhỏ hơn ánh xạ tới hai lớp: 0 ("not spam") và 1 ("spam"), như thể hiện ở hình 6.9. Ta giữ nguyên kiến trúc mô hình trước đó, ngoại trừ việc thay thế lớp đầu ra.

> **Số nút (node) ở lớp đầu ra**
> Về mặt kỹ thuật, chúng ta có thể sử dụng một nút đầu ra duy nhất vì ta đang giải quyết một bài toán phân loại nhị phân (binary classification). Tuy nhiên, làm vậy sẽ yêu cầu thay đổi hàm mất mát (loss function), như tôi đã thảo luận trong bài "Losses Learned—Optimizing Negative Log-Likelihood and Cross-Entropy in PyTorch" (https://mng.bz/NRZ2). Do đó, chúng ta chọn một cách tiếp cận tổng quát hơn, trong đó số lượng nút đầu ra khớp với số lượng lớp (class). Ví dụ, đối với bài toán ba lớp, chẳng hạn như phân loại các bài báo thành "Technology", "Sports", hoặc "Politics", ta sẽ sử dụng ba nút đầu ra, v.v.

[Hình 6.9: Chuyển đổi mô hình GPT cho phân loại spam bằng cách thay đổi kiến trúc của nó. Lớp tuyến tính đầu ra mapping từ 768 nút xuống 50.257, giờ đổi thành mapping từ 768 nút xuống chỉ 2 lớp.]

Trước khi thực hiện sửa đổi như hình 6.9, hãy in kiến trúc mô hình ra xem sao (`print(model)`):

```text
GPTModel(
  (tok_emb): Embedding(50257, 768)
  (pos_emb): Embedding(1024, 768)
  (drop_emb): Dropout(p=0.0, inplace=False)
  (trf_blocks): Sequential(
...
    (11): TransformerBlock(
      (att): MultiHeadAttention(
        (W_query): Linear(in_features=768, out_features=768, bias=True)
        (W_key): Linear(in_features=768, out_features=768, bias=True)
        (W_value): Linear(in_features=768, out_features=768, bias=True)
        (out_proj): Linear(in_features=768, out_features=768, bias=True)
        (dropout): Dropout(p=0.0, inplace=False)
      )
      (ff): FeedForward(
        (layers): Sequential(
          (0): Linear(in_features=768, out_features=3072, bias=True)
          (1): GELU()
          (2): Linear(in_features=3072, out_features=768, bias=True)
        )
      )
      (norm1): LayerNorm()
      (norm2): LayerNorm()
      (drop_resid): Dropout(p=0.0, inplace=False)
    )
  )
  (final_norm): LayerNorm()
  (out_head): Linear(in_features=768, out_features=50257, bias=False)
)
```

Đầu ra này sắp xếp gọn gàng kiến trúc mà ta đã thiết lập trong Chương 4. `GPTModel` chứa các lớp nhúng theo sau là 12 khối biến đổi (transformer blocks) giống hệt nhau (ở đây chỉ hiển thị khối cuối cùng cho ngắn gọn), sau đó là một LayerNorm cuối cùng và lớp đầu ra `out_head`.

Tiếp theo, ta thay thế `out_head` bằng một lớp đầu ra mới (xem hình 6.9) mà ta sẽ tinh chỉnh.

**Tinh chỉnh các lớp chọn lọc thay vì toàn bộ các lớp**
Vì ta bắt đầu với một mô hình đã tiền huấn luyện, việc tinh chỉnh toàn bộ các lớp của mô hình là không cần thiết. Trong các mô hình ngôn ngữ dựa trên mạng nơ-ron, các lớp sâu bên dưới thường nắm bắt các cấu trúc và ngữ nghĩa ngôn ngữ cơ bản, áp dụng được trên nhiều loại tác vụ và tập dữ liệu. Vì vậy, việc chỉ tinh chỉnh các lớp cuối cùng (gần đầu ra), vốn chuyên biệt hơn cho các cấu trúc ngôn ngữ và đặc trưng nhiệm vụ, thường là đủ để thích ứng mô hình với tác vụ mới. Một lợi ích phụ là điều này tiết kiệm chi phí tính toán hơn nhiều.

Để chuẩn bị mô hình cho tinh chỉnh phân loại, trước tiên chúng ta "đóng băng" (freeze) mô hình, tức là biến tất cả các lớp thành không-thể-huấn-luyện (nontrainable):

```python
for param in model.parameters():
    param.requires_grad = False
```

Sau đó, ta thay thế lớp đầu ra (`model.out_head`), lớp mà ban đầu ánh xạ các đầu vào tới 50.257 chiều (kích thước từ vựng):

**Listing 6.7: Thêm lớp phân loại**

```python
torch.manual_seed(123)
num_classes = 2
model.out_head = torch.nn.Linear(
    in_features=BASE_CONFIG["emb_dim"], 
    out_features=num_classes
)
```

Lớp đầu ra `model.out_head` mới này có thuộc tính `requires_grad` được đặt thành `True` theo mặc định, nghĩa là nó là lớp duy nhất trong mô hình sẽ được cập nhật trong quá trình huấn luyện. Về mặt kỹ thuật, huấn luyện riêng lớp này là đủ. Tuy nhiên, để tăng hiệu suất dự đoán của mô hình, ta thiết lập cho khối transformer cuối cùng và LayerNorm cuối cùng kết nối với lớp đầu ra, có thể huấn luyện (trainable), như mô tả ở hình 6.10.

Để làm cho LayerNorm cuối cùng và khối transformer cuối cùng có thể huấn luyện, ta gán `requires_grad` thành `True` cho chúng:

```python
for param in model.trf_blocks[-1].parameters():
    param.requires_grad = True

for param in model.final_norm.parameters():
    param.requires_grad = True
```

> **Bài tập 6.2: Tinh chỉnh toàn bộ mô hình (Fine-tuning the whole model)**
> Thay vì chỉ tinh chỉnh khối transformer cuối cùng và lớp phân loại đầu ra, hãy cấu hình để tinh chỉnh toàn bộ các tham số của mô hình (`requires_grad = True` cho tất cả các tầng) và đánh giá sự ảnh hưởng đến hiệu năng dự đoán cũng như thời gian huấn luyện.

Mặc dù ta vừa thay thế lớp đầu ra và làm vài lớp thành có-thể-huấn-luyện, ta vẫn có thể đưa input vào theo cách bình thường:

```python
inputs = tokenizer.encode("Do you have time")
inputs = torch.tensor(inputs).unsqueeze(0)
print("Inputs:", inputs)
print("Inputs dimensions:", inputs.shape)   
```

[Hình 6.10: Mô hình GPT bao gồm 12 block lặp lại. Cùng với layer đầu ra, ta cài LayerNorm và block Transformer cuối là trainable. Các block còn lại bị đóng băng.]

Kết quả của code trước encode câu thành 4 token input:
```
Inputs: tensor([[5211,  345,  423,  640]])
Inputs dimensions: torch.Size([1, 4])
```

Và ta feed các ID này vào mô hình:

```python
with torch.no_grad():
    outputs = model(inputs)

print("Outputs:\n", outputs)
print("Outputs dimensions:", outputs.shape)
```

Đầu ra trông giống như sau:

```
Outputs:
 tensor([[[-1.5854,  0.9904],
          [-3.7235,  7.4548],
          [-2.2661,  6.6049],
          [-3.5983,  3.9902]]])
Outputs dimensions: torch.Size([1, 4, 2])
```

Dữ liệu đầu vào tương tự trước đây sẽ tạo ra một tensor đầu ra có kích thước `[1, 4, 50257]`. Số dòng tương ứng với số token. Số cột là 2 thay vì 50,257 vì ta đã thay thế output layer.

Hãy nhớ rằng chúng ta quan tâm đến việc tinh chỉnh mô hình này để trả về nhãn "spam" hay "not spam". Chúng ta không cần tinh chỉnh cả 4 hàng kết quả đầu ra; thay vào đó, ta tập trung vào một token đầu ra duy nhất: dòng cuối cùng (tương ứng với token cuối cùng), như ở hình 6.11.

[Hình 6.11: Tensor đầu ra bao gồm 2 cột. Chúng ta chỉ hứng thú với hàng cuối cùng để xác định bài toán phân loại spam.]

Để trích xuất token đầu ra cuối cùng, ta làm như sau:

```python
print("Last output token:", outputs[:, -1, :])
```

Sẽ in ra:
```
Last output token: tensor([[-3.5983,  3.9902]])
```

Chúng ta vẫn cần chuyển đổi các giá trị này thành dự đoán class. Tại sao ta chỉ hứng thú token cuối? Bởi vì, nhờ vào causal attention mask, mỗi token bị giới hạn không được "chú ý" (attend) tới các token trong tương lai, nên token cuối cùng tích lũy nhiều thông tin nhất vì nó có quyền truy cập vào dữ liệu từ tất cả token đi trước. Do đó, trong tác vụ phân loại, ta tập trung vào token cuối (hình 6.12).

[Hình 6.12: Cơ chế causal attention. Nhờ ma trận này, token cuối cùng là token duy nhất có attention score đến tất cả các token trước nó.]

Giờ ta sẵn sàng chuyển đổi token cuối cùng này thành dự đoán phân loại nhãn và tính toán độ chính xác khởi tạo. 

## 6.6 Tính toán hàm mất mát phân loại và độ chính xác

Chỉ còn một nhiệm vụ nhỏ trước khi tinh chỉnh: triển khai các hàm đánh giá trong khi tinh chỉnh, theo hình 6.13.

Trước khi viết hàm đánh giá, hãy bàn về cách chuyển mô hình đầu ra thành class label. Ta từng dùng softmax chuyển 50,257 đầu ra thành tỷ lệ phần trăm và argmax để lấy ra chỉ mục có số điểm cao nhất. Ở đây cũng vậy, áp dụng trực tiếp như hình 6.14.

[Hình 6.13: Giai đoạn 2 của fine-tuning classifier. Triển khai Evaluation utilities.]
[Hình 6.14: Đầu ra cuối biến đổi thành xác suất. Lấy chỉ mục chứa điểm cao nhất thành label dự đoán.]

> **Bài tập 6.3: Tinh chỉnh token đầu tiên so với token cuối cùng (Fine-tuning the first vs. last token)**
> Trong kiến trúc decoder-only với cơ chế causal attention, token cuối cùng là token duy nhất có attention weight liên kết tới tất cả các token đứng trước nó. Hãy thử nghiệm tinh chỉnh trên token đầu ra đầu tiên (`outputs[:, 0, :]`) thay vì token cuối cùng (`outputs[:, -1, :]`) và quan sát sự thay đổi về độ chính xác dự đoán.

Ví dụ, đầu ra cuối cùng:
`Last output token: tensor([[-3.5983,  3.9902]])`

Lấy nhãn lớp:

```python
probas = torch.softmax(outputs[:, -1, :], dim=-1)
label = torch.argmax(probas)
print("Class label:", label.item())
```

Trong trường hợp này in ra `1` (spam). Thực ra không dùng softmax cũng được, vì số nào to hơn thì xác suất nó to hơn:

```python
logits = outputs[:, -1, :]
label = torch.argmax(logits)
print("Class label:", label.item())
```

Tương tự ta có thể viết hàm tính độ chính xác trên toàn bộ tập dữ liệu.

**Listing 6.8: Tính độ chính xác phân loại (classification accuracy)**

```python
def calc_accuracy_loader(data_loader, model, device, num_batches=None):
    model.eval()
    correct_predictions, num_examples = 0, 0
    
    if num_batches is None:
        num_batches = len(data_loader)
    else:
        num_batches = min(num_batches, len(data_loader))
        
    for i, (input_batch, target_batch) in enumerate(data_loader):
        if i < num_batches:
            input_batch = input_batch.to(device)
            target_batch = target_batch.to(device)
            
            with torch.no_grad():
                logits = model(input_batch)[:, -1, :]    
                
            predicted_labels = torch.argmax(logits, dim=-1)
            num_examples += predicted_labels.shape[0]
            correct_predictions += (
                (predicted_labels == target_batch).sum().item()
            )
        else:
            break
            
    return correct_predictions / num_examples
```

Áp dụng đánh giá trên 10 batch để xem thử:

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
torch.manual_seed(123)

train_accuracy = calc_accuracy_loader(train_loader, model, device, num_batches=10)
val_accuracy = calc_accuracy_loader(val_loader, model, device, num_batches=10)
test_accuracy = calc_accuracy_loader(test_loader, model, device, num_batches=10)

print(f"Training accuracy: {train_accuracy*100:.2f}%")
print(f"Validation accuracy: {val_accuracy*100:.2f}%")
print(f"Test accuracy: {test_accuracy*100:.2f}%")
```

Kết quả:
```
Training accuracy: 46.25%
Validation accuracy: 45.00%
Test accuracy: 48.75%
```
Kết quả dao động 50% giống hệt dự đoán ngẫu nhiên. Để tăng độ chính xác, ta cần tính hàm mất mát.

Độ chính xác phân loại không phải hàm khả vi (differentiable), vì thế ta dùng **cross-entropy loss** (mất mát entropy chéo). 

**Listing 6.9: Tính classification loss**

```python
def calc_loss_batch(input_batch, target_batch, model, device):
    input_batch = input_batch.to(device)
    target_batch = target_batch.to(device)
    
    logits = model(input_batch)[:, -1, :]    
    loss = torch.nn.functional.cross_entropy(logits, target_batch)
    return loss

def calc_loss_loader(data_loader, model, device, num_batches=None):
    total_loss = 0.
    if len(data_loader) == 0:
        return float("nan")
    elif num_batches is None:
        num_batches = len(data_loader)
    else:                                       
        num_batches = min(num_batches, len(data_loader))
        
    for i, (input_batch, target_batch) in enumerate(data_loader):
        if i < num_batches:
            loss = calc_loss_batch(
                input_batch, target_batch, model, device
            )
            total_loss += loss.item()
        else:
            break
            
    return total_loss / num_batches
```

Tính toán các hàm Loss khởi tạo:

```python
with torch.no_grad():                
    train_loss = calc_loss_loader(train_loader, model, device, num_batches=5)
    val_loss = calc_loss_loader(val_loader, model, device, num_batches=5)
    test_loss = calc_loss_loader(test_loader, model, device, num_batches=5)

print(f"Training loss: {train_loss:.3f}")
print(f"Validation loss: {val_loss:.3f}")
print(f"Test loss: {test_loss:.3f}")
```

```
Training loss: 2.453
Validation loss: 2.583
Test loss: 2.322
```

Mục tiêu giờ là giảm các chỉ số Mất mát (Loss) xuống thấp nhất có thể.

## 6.7 Tinh chỉnh mô hình trên dữ liệu có nhãn (Supervised Data)

Vòng lặp huấn luyện, minh họa ở hình 6.15, hoàn toàn giống với vòng lặp trong giai đoạn tiền huấn luyện; điểm khác biệt duy nhất là ta tính độ chính xác phân loại thay vì tạo văn bản mẫu.

[Hình 6.15: Một quy trình training loop cơ bản cho Mạng Nơ-ron PyTorch.]

Hàm huấn luyện này khác biệt đôi chút: ta đếm số mẫu nhìn thấy (`examples_seen`) thay vì số lượng token, và ta đánh giá accuracy qua các epoch.

**Listing 6.10: Tinh chỉnh mô hình phân loại spam**

```python
def train_classifier_simple(
        model, train_loader, val_loader, optimizer, device,
        num_epochs, eval_freq, eval_iter):
        
    train_losses, val_losses, train_accs, val_accs = [], [], [], []  
    examples_seen, global_step = 0, -1
    
    for epoch in range(num_epochs):   
        model.train()            
        for input_batch, target_batch in train_loader:
            optimizer.zero_grad()                     
            loss = calc_loss_batch(
                input_batch, target_batch, model, device
            )
            loss.backward()                         
            optimizer.step()                         
            examples_seen += input_batch.shape[0]   
            global_step += 1
              
            if global_step % eval_freq == 0:
                train_loss, val_loss = evaluate_model(
                    model, train_loader, val_loader, device, eval_iter)
                train_losses.append(train_loss)
                val_losses.append(val_loss)
                print(f"Ep {epoch+1} (Step {global_step:06d}): "
                      f"Train loss {train_loss:.3f}, "
                      f"Val loss {val_loss:.3f}"
                )
                                                  
        train_accuracy = calc_accuracy_loader(
            train_loader, model, device, num_batches=eval_iter
        )
        val_accuracy = calc_accuracy_loader(
            val_loader, model, device, num_batches=eval_iter
        )
        print(f"Training accuracy: {train_accuracy*100:.2f}% | ", end="")
        print(f"Validation accuracy: {val_accuracy*100:.2f}%")
        train_accs.append(train_accuracy)
        val_accs.append(val_accuracy)
        
    return train_losses, val_losses, train_accs, val_accs, examples_seen

def evaluate_model(model, train_loader, val_loader, device, eval_iter):
    model.eval()
    with torch.no_grad():
        train_loss = calc_loss_loader(
            train_loader, model, device, num_batches=eval_iter
        )
        val_loss = calc_loss_loader(
            val_loader, model, device, num_batches=eval_iter
        )
    model.train()
    return train_loss, val_loss
```

Huấn luyện mô hình (sẽ chạy tốn 6 phút cho laptop Macbook Air M3):

```python
import time

start_time = time.time()
torch.manual_seed(123)

optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5, weight_decay=0.1)
num_epochs = 5

train_losses, val_losses, train_accs, val_accs, examples_seen = \
    train_classifier_simple(
        model, train_loader, val_loader, optimizer, device,
        num_epochs=num_epochs, eval_freq=50,
        eval_iter=5
    )
    
end_time = time.time()
execution_time_minutes = (end_time - start_time) / 60
print(f"Training completed in {execution_time_minutes:.2f} minutes.")
```

Đầu ra của huấn luyện:

```
Ep 1 (Step 000000): Train loss 2.153, Val loss 2.392
Ep 1 (Step 000050): Train loss 0.617, Val loss 0.637
Ep 1 (Step 000100): Train loss 0.523, Val loss 0.557
Training accuracy: 70.00% | Validation accuracy: 72.50%
...
Ep 5 (Step 000550): Train loss 0.207, Val loss 0.143
Ep 5 (Step 000600): Train loss 0.083, Val loss 0.074
Training accuracy: 100.00% | Validation accuracy: 97.50%
Training completed in 5.65 minutes.
```

Tiếp theo, ta vẽ biểu đồ Training/Validation loss bằng matplotlib.

**Listing 6.11: Vẽ đồ thị độ mất mát của tập phân loại**

```python
import matplotlib.pyplot as plt

def plot_values(
        epochs_seen, examples_seen, train_values, val_values,
        label="loss"):
        
    fig, ax1 = plt.subplots(figsize=(5, 3))
                                     
    ax1.plot(epochs_seen, train_values, label=f"Training {label}")
    ax1.plot(
        epochs_seen, val_values, linestyle="-.",
        label=f"Validation {label}"
    )
    ax1.set_xlabel("Epochs")
    ax1.set_ylabel(label.capitalize())
    ax1.legend()
                                  
    ax2 = ax1.twiny()
    ax2.plot(examples_seen, train_values, alpha=0)   
    ax2.set_xlabel("Examples seen")
    
    fig.tight_layout()            
    plt.savefig(f"{label}-plot.pdf")
    plt.show()

epochs_tensor = torch.linspace(0, num_epochs, len(train_losses))
examples_seen_tensor = torch.linspace(0, examples_seen, len(train_losses))
plot_values(epochs_tensor, examples_seen_tensor, train_losses, val_losses)
```

Hình 6.16 hiển thị các đường cong tổn thất. Sự dốc xuống mạnh mẽ ở kỷ nguyên đầu chứng tỏ tiến trình huấn luyện nhanh. Chênh lệch giữa loss training và validation vô cùng nhỏ (ít xảy ra hiện tượng overfitting). Tương tự, gọi hàm đồ thị cho Accuracy (Hình 6.17).

[Hình 6.16: Loss quá trình huấn luyện và tập kiểm định trên 5 epoch. Hàm mất mát giảm mạnh xuống gần mức 0 sau vòng 5.]
[Hình 6.17: Độ chính xác accuracy của quá trình training và validation tịnh tiến về mức 1 (100%).]

Tính toán tổng cho tất cả bộ dữ liệu, ta thấy:

```python
train_accuracy = calc_accuracy_loader(train_loader, model, device)
val_accuracy = calc_accuracy_loader(val_loader, model, device)
test_accuracy = calc_accuracy_loader(test_loader, model, device)

print(f"Training accuracy: {train_accuracy*100:.2f}%")
print(f"Validation accuracy: {val_accuracy*100:.2f}%")
print(f"Test accuracy: {test_accuracy*100:.2f}%")
```

Kết quả:
```
Training accuracy: 97.21%
Validation accuracy: 97.32%
Test accuracy: 95.67%
```
Hiệu suất huấn luyện và tập validation xấp xỉ nhau, overfitting thấp. Thường validation accuracy sẽ cao hơn chút xíu vì nó được tùy chỉnh siêu tham số trên đó. Có thể điều chỉnh `drop_rate` hay `weight_decay` nếu sự chênh lệch (gap) là quá lớn.

## 6.8 Sử dụng LLM với vai trò Mô hình phân loại rác (Spam)

Chúng ta có thể thử dùng mô hình bằng 1 script code mới.

[Hình 6.18: Giai đoạn cuối của Fine-tuning: Bước 10 Sử dụng Model trên Data mới để phân loại]

**Listing 6.12: Dùng model classfy câu mới**

```python
def classify_review(
        text, model, tokenizer, device, max_length=None,
        pad_token_id=50256):
        
    model.eval()
    input_ids = tokenizer.encode(text)         
    supported_context_length = model.pos_emb.weight.shape[1]
    
    input_ids = input_ids[:min(             
        max_length, supported_context_length
    )]
    
    input_ids += [pad_token_id] * (max_length - len(input_ids))   
    
    input_tensor = torch.tensor(
        input_ids, device=device
    ).unsqueeze(0)             
    
    with torch.no_grad():                               
        logits = model(input_tensor)[:, -1, :]    
        
    predicted_label = torch.argmax(logits, dim=-1).item()
    return "spam" if predicted_label == 1 else "not spam"    
```

Chạy code với 1 ví dụ:

```python
text_1 = (
    "You are a winner you have been specially"
    " selected to receive $1000 cash or a $2000 award."
)
print(classify_review(
    text_1, model, tokenizer, device, max_length=train_dataset.max_length
))
```
Kết quả trả về chính xác: `"spam"`. Ví dụ 2:

```python
text_2 = (
    "Hey, just wanted to check if we're still on"
    " for dinner tonight? Let me know!"
)
print(classify_review(
    text_2, model, tokenizer, device, max_length=train_dataset.max_length
))
```
Trả về đúng là `"not spam"`. Lưu mô hình nếu cần:

```python
torch.save(model.state_dict(), "review_classifier.pth")

# Load model lại
# model_state_dict = torch.load("review_classifier.pth", map_location=device)
# model.load_state_dict(model_state_dict)
```

## Tóm tắt
- Có những chiến lược tinh chỉnh LLMs khác nhau, bao gồm tinh chỉnh phân loại (classification) và tinh chỉnh chỉ dẫn (instruction).
- Tinh chỉnh phân loại bao gồm việc thay thế lớp đầu ra (output layer) bằng một lớp phân loại (classification layer) nhỏ.
- Trong tác vụ phân loại thư rác (spam) với "not spam", layer mới này bao gồm 2 đầu ra node. (Thay vì 50.257 đầu ra như trước)
- Thay vì dự đoán token tiếp theo, nó huấn luyện model phân loại chính xác nhãn "spam" và "not spam".
- Đầu vào model là một dãy token ID được mã hóa, y hệt như tiền huấn luyện (pretraining).
- Trước khi tinh chỉnh, nạp model weight gốc.
- Đánh giá phân loại bao gồm tính Accuracy (độ chính xác dự đoán).
- Tinh chỉnh phân loại cũng sử dụng chung hàm mất mát (Cross entropy loss) giống như giai đoạn tiền huấn luyện.
