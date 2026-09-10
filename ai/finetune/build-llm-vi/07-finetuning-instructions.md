# Chương 7: Tinh chỉnh để tuân theo chỉ dẫn (Fine-tuning to follow instructions)

Trước đây, chúng ta đã triển khai kiến trúc LLM, thực hiện tiền huấn luyện, và nạp các trọng số đã được huấn luyện trước từ các nguồn bên ngoài vào mô hình. Sau đó, chúng ta tập trung vào việc tinh chỉnh LLM cho một tác vụ phân loại cụ thể: phân biệt giữa tin nhắn spam và non-spam. Bây giờ, chúng ta sẽ thực hiện quy trình tinh chỉnh LLM để tuân theo các chỉ dẫn của con người, như minh họa trong hình 7.1. Tinh chỉnh chỉ dẫn (instruction fine-tuning) là một trong những kỹ thuật chính đằng sau việc phát triển LLMs cho các ứng dụng chatbot, trợ lý cá nhân và các tác vụ đàm thoại khác.

*Chương này bao gồm:*
- *Quy trình tinh chỉnh chỉ dẫn của LLMs*
- *Chuẩn bị một bộ dữ liệu cho tinh chỉnh chỉ dẫn có giám sát*
- *Tổ chức dữ liệu chỉ dẫn thành các batch huấn luyện*
- *Nạp một LLM đã tiền huấn luyện và tinh chỉnh nó để tuân theo chỉ dẫn con người*
- *Trích xuất các phản hồi chỉ dẫn do LLM sinh ra để đánh giá*
- *Đánh giá một LLM đã được tinh chỉnh chỉ dẫn*

[Hình 7.1: Ba giai đoạn chính của việc lập trình một LLM. Chương này tập trung vào bước 9 của giai đoạn 3: tinh chỉnh một LLM đã tiền huấn luyện để tuân theo chỉ dẫn của con người.]

Hình 7.1 cho thấy hai cách chính để tinh chỉnh LLM: tinh chỉnh cho phân loại (bước 8) và tinh chỉnh LLM để tuân theo chỉ dẫn (bước 9). Chúng ta đã thực hiện bước 8 trong chương 6. Giờ chúng ta sẽ tinh chỉnh LLM sử dụng một tập dữ liệu chỉ dẫn.

## 7.1 Giới thiệu về tinh chỉnh chỉ dẫn

Đến giờ chúng ta đã biết rằng việc tiền huấn luyện một LLM liên quan đến một quy trình đào tạo mà trong đó nó học cách sinh ra từng từ một. LLM đã tiền huấn luyện thu được có khả năng tự hoàn thành văn bản (text completion), tức là nó có thể viết nốt câu hoặc hoàn thiện các đoạn văn khi được cung cấp một đoạn trích làm đầu vào. Tuy nhiên, các LLMs tiền huấn luyện thường gặp khó khăn với các chỉ dẫn cụ thể, chẳng hạn như "Sửa lỗi ngữ pháp trong văn bản này" hoặc "Chuyển câu này sang thể bị động". Chút nữa, chúng ta sẽ xem xét một ví dụ cụ thể, trong đó ta nạp một LLM tiền huấn luyện làm cơ sở cho tinh chỉnh chỉ dẫn, hay còn gọi là tinh chỉnh chỉ dẫn có giám sát (supervised instruction fine-tuning).

Ở đây, chúng ta tập trung cải thiện khả năng của LLM để làm theo các loại chỉ dẫn này và tạo ra phản hồi mong muốn, như được mô tả trong hình 7.2. Việc chuẩn bị tập dữ liệu là khía cạnh cốt lõi của tinh chỉnh chỉ dẫn. Sau đó, ta sẽ hoàn thành tất cả các bước trong ba giai đoạn của quá trình, bắt đầu bằng việc chuẩn bị dữ liệu, như trong hình 7.3.

[Hình 7.2: Các ví dụ về chỉ dẫn được xử lý bởi một LLM để tạo ra các phản hồi mong muốn.]

[Hình 7.3: Quy trình 3 giai đoạn để tinh chỉnh chỉ dẫn LLM. Giai đoạn 1 liên quan đến chuẩn bị bộ dữ liệu. Giai đoạn 2 tập trung vào thiết lập và tinh chỉnh mô hình. Giai đoạn 3 là quá trình đánh giá. Chúng ta sẽ bắt đầu bằng bước 1 của giai đoạn 1: tải và định dạng dataset.]

## 7.2 Chuẩn bị bộ dữ liệu cho tinh chỉnh chỉ dẫn có giám sát

Hãy tải về và định dạng tập dữ liệu chỉ dẫn để phục vụ cho việc tinh chỉnh một LLM đã tiền huấn luyện. Tập dữ liệu này bao gồm 1.100 cặp chỉ dẫn-phản hồi (instruction-response pairs) tương tự như những cặp trong hình 7.2. Tập dữ liệu này được tạo riêng cho cuốn sách này, nhưng những độc giả quan tâm có thể tìm thấy các tập dữ liệu chỉ dẫn thay thế, công khai có sẵn ở Phụ lục B.

Đoạn code sau triển khai và thực thi một hàm tải về tập dữ liệu này; nó là một file tương đối nhỏ (chỉ 204 KB) ở định dạng JSON. JSON (JavaScript Object Notation) phản ánh cấu trúc của các dictionary (từ điển) trong Python, cung cấp một cấu trúc đơn giản để trao đổi dữ liệu, vừa dễ đọc cho con người vừa thân thiện với máy móc.

**Listing 7.1: Tải về bộ dữ liệu**

```python
import json
import os
import urllib

def download_and_load_file(file_path, url):
    # Bỏ qua nếu file đã được tải xuống trước đó
    if not os.path.exists(file_path):
        with urllib.request.urlopen(url) as response:
            text_data = response.read().decode("utf-8")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_data)
    else:                                               
        with open(file_path, "r", encoding="utf-8") as file:
            text_data = file.read()
            
    with open(file_path, "r") as file:
        data = json.load(file)
        
    return data

file_path = "instruction-data.json"
url = (
    "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch"
    "/main/ch07/01_main-chapter-code/instruction-data.json"
)

data = download_and_load_file(file_path, url)
print("Number of entries:", len(data))
```

Đầu ra của việc chạy đoạn code trên là:
```
Number of entries: 1100
```

Danh sách dữ liệu ta vừa nạp từ file JSON chứa 1.100 bản ghi của tập dữ liệu chỉ dẫn. Hãy in thử một bản ghi để xem mỗi phần tử được cấu trúc như thế nào:

```python
print("Example entry:\n", data[50])
```

Nội dung của bản ghi ví dụ này là:
```
Example entry:
 {'instruction': 'Identify the correct spelling of the following word.',
  'input': 'Ocassion', 'output': "The correct spelling is 'Occasion.'"}
```

Như ta có thể thấy, các bản ghi ví dụ là các đối tượng từ điển (dictionary) của Python chứa các trường `'instruction'` (chỉ dẫn), `'input'` (đầu vào) và `'output'` (đầu ra). Hãy xem một ví dụ khác:

```python
print("Another example entry:\n", data[999])
```

Dựa trên nội dung của bản ghi này, trường `'input'` đôi khi có thể bị bỏ trống:
```
Another example entry:
 {'instruction': "What is an antonym of 'complicated'?", 
  'input': '',
  'output': "An antonym of 'complicated' is 'simple'."}
```

Tinh chỉnh chỉ dẫn liên quan đến việc đào tạo mô hình trên một tập dữ liệu nơi mà các cặp đầu vào-đầu ra được cung cấp một cách rõ ràng như ta vừa trích xuất từ tệp JSON. Có nhiều phương pháp khác nhau để định dạng những bản ghi này cho LLMs. Hình 7.4 minh họa hai định dạng ví dụ khác nhau, thường được gọi là phong cách nhắc lệnh (prompt styles), được sử dụng trong việc huấn luyện các LLM nổi tiếng như Alpaca và Phi-3.

[Hình 7.4: So sánh các kiểu viết prompt cho tinh chỉnh chỉ dẫn. Kiểu Alpaca (bên trái) dùng cấu trúc với các phần riêng cho instruction, input, và response. Kiểu Phi-3 (bên phải) dùng định dạng đơn giản hơn với các token `<|user|>` và `<|assistant|>`.]

Alpaca là một trong những LLM đầu tiên công khai chi tiết quy trình tinh chỉnh chỉ dẫn của nó. Phi-3, do Microsoft phát triển, được đưa vào để chứng minh sự đa dạng trong các phong cách prompt. Phần còn lại của chương này sử dụng định dạng prompt Alpaca vì nó là một trong những phong cách phổ biến nhất và góp công định hình cách tiếp cận ban đầu cho tinh chỉnh.

Hãy định nghĩa một hàm `format_input` mà ta có thể dùng để chuyển các bản ghi dữ liệu thành định dạng đầu vào kiểu Alpaca.

**Listing 7.2: Triển khai hàm định dạng prompt**

```python
def format_input(entry):
    instruction_text = (
        f"Below is an instruction that describes a task. "
        f"Write a response that appropriately completes the request."
        f"\n\n### Instruction:\n{entry['instruction']}"
    )
    
    input_text = (
        f"\n\n### Input:\n{entry['input']}" if entry["input"] else ""
    )
    
    return instruction_text + input_text
```

Hàm `format_input` này nhận đầu vào là một từ điển (dictionary) và cấu trúc lại nó thành chuỗi định dạng sẵn. Thử chạy hàm với bản ghi `data[50]` lúc nãy:

```python
model_input = format_input(data[50])
desired_response = f"\n\n### Response:\n{data[50]['output']}"
print(model_input + desired_response)
```

Chuỗi đầu vào được định dạng sẽ trông như thế này:
```
Below is an instruction that describes a task. Write a response that 
appropriately completes the request.

### Instruction:
Identify the correct spelling of the following word.

### Input:
Ocassion

### Response:
The correct spelling is 'Occasion.'
```

> **Bài tập 7.1 Thay đổi phong cách prompt**
> Sau khi bạn hoàn tất tinh chỉnh mô hình bằng phong cách prompt Alpaca, hãy thử phong cách prompt Phi-3 (hiển thị ở hình 7.4) và xem thử nó có tác động đến chất lượng trả lời của mô hình không.

Lưu ý rằng hàm `format_input` sẽ tự động bỏ qua phần `### Input:` nếu trường `'input'` bị trống. Ta có thể test hàm này với giá trị `data[999]` ta đã kiểm tra trước đó:

```python
model_input = format_input(data[999])
desired_response = f"\n\n### Response:\n{data[999]['output']}"
print(model_input + desired_response)
```

Đầu ra chứng tỏ rằng những bản ghi có `'input'` bị trống sẽ không chứa phần `### Input:` trong chuỗi định dạng:
```
Below is an instruction that describes a task. Write a response that 
appropriately completes the request.

### Instruction:
What is an antonym of 'complicated'?

### Response:
An antonym of 'complicated' is 'simple'.
```

Trước khi chuyển sang việc thiết lập PyTorch data loader ở phần tiếp theo, ta hãy chia tập dữ liệu thành các tập huấn luyện (training), xác thực (validation), và kiểm thử (test) tương tự như lúc ta làm với dataset phân loại thư rác (spam) ở chương trước. Đoạn code dưới đây cho thấy cách tính toán các phần này.

**Listing 7.3: Phân chia bộ dữ liệu**

```python
# Sử dụng 85% data cho training
train_portion = int(len(data) * 0.85)   
# Sử dụng 10% data cho testing
test_portion = int(len(data) * 0.1)           
# Phần 5% còn lại cho validation
val_portion = len(data) - train_portion - test_portion   

train_data = data[:train_portion]
test_data = data[train_portion:train_portion + test_portion]
val_data = data[train_portion + test_portion:]

print("Training set length:", len(train_data))
print("Validation set length:", len(val_data))
print("Test set length:", len(test_data))
```

Phép chia này dẫn tới kích cỡ cụ thể của các tập dữ liệu như sau:
```
Training set length: 935
Validation set length: 55
Test set length: 110
```

## 7.3 Tổ chức dữ liệu thành các batch huấn luyện

Quá trình triển khai tinh chỉnh chỉ dẫn tiếp tục với bước thiết lập batch huấn luyện, được mô tả trong hình 7.5. Điều này liên quan đến việc định nghĩa một quy trình đưa dữ liệu định dạng sẵn vào mô hình theo batch để tính toán hiệu quả hơn.

[Hình 7.5: Quy trình 3 bước tinh chỉnh chỉ dẫn. Tập trung vào Bước 2 của Giai đoạn 1: Lập các batch dữ liệu.]

Trong chương trước, các batch dữ liệu được lớp `DataLoader` của PyTorch tạo tự động với hàm `collate` mặc định để hợp nhất (merge) các mẫu rời rạc thành một batch. Tuy nhiên, quy trình batching cho tinh chỉnh chỉ dẫn phức tạp hơn một chút và đòi hỏi chúng ta phải tự tạo một hàm `collate` tùy biến (custom collate function).

Hãy tiếp cận vấn đề theo nhiều bước nhỏ, như hình 7.6. Để thực hiện các bước 2.1 và 2.2, ta lập trình lớp `InstructionDataset` nhằm gọi `format_input` và mã hóa toàn bộ dữ liệu, tương tự như `SpamDataset`. Tiến trình 2 bước này được thể hiện ở hình 7.7, thực thi bên trong hàm dựng `__init__` của `InstructionDataset`.

[Hình 7.6: Năm bước phụ trong việc khởi tạo batch. (2.1) Format data prompt. (2.2) Tokenize nó. (2.3) Chèn thêm pad để có cùng độ dài. (2.4) Lập token chỉ tiêu (target) (dịch 1 đơn vị sang phải so với input). (2.5) Thay pad của target bằng biến placeholder -100 để loại nó ra khỏi tính toán loss.]

**Listing 7.4: Triển khai lớp instruction dataset**

```python
import torch
from torch.utils.data import Dataset

class InstructionDataset(Dataset):
    def __init__(self, data, tokenizer):
        self.data = data
        self.encoded_texts = []
        for entry in data:        
            instruction_plus_input = format_input(entry)
            response_text = f"\n\n### Response:\n{entry['output']}"
            full_text = instruction_plus_input + response_text
            
            # Tiền token hóa (Pretokenize) text
            self.encoded_texts.append(
                tokenizer.encode(full_text)
            )
            
    def __getitem__(self, index):
        return self.encoded_texts[index]
        
    def __len__(self):
        return len(self.data)
```

[Hình 7.7: Hai bước đầu tiên trong quá trình thiết lập batch. Các entry được gắn prompt format (2.1) rồi được tokenize (2.2).]

Giống như tinh chỉnh phân loại, ta muốn đẩy nhanh quá trình bằng cách gom các mẫu vào một batch, tức là ta phải đệm (pad) các đầu vào để chúng có cùng độ dài. Giống lúc làm phân loại, token padding sẽ là `<|endoftext|>`.

```python
import tiktoken
tokenizer = tiktoken.get_encoding("gpt2")
print(tokenizer.encode("<|endoftext|>", allowed_special={"<|endoftext|>"}))
```
ID trả về là `50256`.

Đến bước 2.3 (hình 7.6), ta vận dụng cách tiếp cận tinh tế hơn bằng việc thiết kế một custom collate function. Hàm này chỉ đệm chiều dài của các ví dụ (example) cho bằng chiều dài của câu dài nhất trong batch đó, chứ không lấy câu dài nhất của toàn dataset. Cách này giúp tránh padding thừa thãi. (Hình 7.8 minh họa ý tưởng này).

[Hình 7.8: Đệm các token ID 50256 sao cho các mẫu có chiều dài bằng với mẫu dài nhất trong cái batch đó. Mỗi batch có chiều dài khác nhau.]

Chúng ta triển khai quy trình padding này bằng một hàm collate tuỳ biến như sau:

```python
def custom_collate_draft_1(
    batch,
    pad_token_id=50256,
    device="cpu"
):
    # Tìm chuỗi dài nhất trong batch
    batch_max_length = max(len(item)+1 for item in batch)  
    inputs_lst = []
    
    for item in batch:    
        new_item = item.copy()
        new_item += [pad_token_id]
        
        # Đệm thêm cho đủ độ dài
        padded = (
            new_item + [pad_token_id] * 
            (batch_max_length - len(new_item))
        )
        
        # Cắt bớt phần pad thừa đã nối thêm ở đầu
        inputs = torch.tensor(padded[:-1])   
        inputs_lst.append(inputs)
        
    # Chuyển list input thành một tensor và bắn vào thiết bị đích
    inputs_tensor = torch.stack(inputs_lst).to(device)    
    return inputs_tensor
```

Hàm `custom_collate_draft_1` được thiết kế để nhét vào `DataLoader`, nhưng ta cũng có thể gọi nó trực tiếp. Thử nghiệm với 3 input:

```python
inputs_1 = [0, 1, 2, 3, 4]
inputs_2 = [5, 6]
inputs_3 = [7, 8, 9]

batch = (
    inputs_1,
    inputs_2,
    inputs_3
)
print(custom_collate_draft_1(batch))
```

Đầu ra trông sẽ như thế này:
```
tensor([[    0,     1,     2,     3,     4],  
        [    5,     6, 50256, 50256, 50256],
        [    7,     8,     9, 50256, 50256]])
```
Như mong đợi, 3 input đã được đệm sao cho bằng độ dài của `inputs_1` (có 5 token IDs).

Ta đã triển khai hàm custom collate đầu tiên. Nhưng ta cũng cần tạo ra batch chứa chuỗi token mục tiêu (target) tương ứng. Những chỉ số target này, như mô tả ở hình 7.9, cực kỳ quan trọng vì nó quyết định những gì mô hình sinh ra và quyết định tính toán suy hao (loss).

Giống tiền huấn luyện LLM, các ID của token đích (target) trùng với ID đầu vào nhưng lệch sang phải 1 đơn vị. Setup này giúp mô hình học cách dự đoán token nối tiếp (Hình 7.10).

[Hình 7.9: Trọng tâm của Batch bước 2.4 - Lập token đích (target IDs) để hỗ trợ tính năng sinh từ.]
[Hình 7.10: Đối chiếu Input và Target. Mỗi chuỗi Target bị dịch đi 1 index, bỏ token đầu và chèn thêm padding ở token cuối.]

Đoạn code cập nhật sau sẽ sinh target từ input:

```python
def custom_collate_draft_2(
    batch,
    pad_token_id=50256,
    device="cpu"
):
    batch_max_length = max(len(item)+1 for item in batch)
    inputs_lst, targets_lst = [], []
    
    for item in batch:
        new_item = item.copy()
        new_item += [pad_token_id]
        padded = (
            new_item + [pad_token_id] * 
            (batch_max_length - len(new_item))
        )
        
        # Cắt bớt token cuối của inputs
        inputs = torch.tensor(padded[:-1])    
        # Dịch chuyển +1 sang phải cho targets
        targets = torch.tensor(padded[1:])   
        
        inputs_lst.append(inputs)
        targets_lst.append(targets)
        
    inputs_tensor = torch.stack(inputs_lst).to(device)
    targets_tensor = torch.stack(targets_lst).to(device)
    return inputs_tensor, targets_tensor

inputs, targets = custom_collate_draft_2(batch)
print(inputs)
print(targets)
```

Chạy đoạn code này, kết quả nhận được (tensor đầu là inputs, tensor sau là targets):

```
tensor([[    0,     1,     2,     3,     4],   
        [    5,     6, 50256, 50256, 50256],
        [    7,     8,     9, 50256, 50256]])
tensor([[    1,     2,     3,     4, 50256],  
        [    6, 50256, 50256, 50256, 50256],
        [    8,     9, 50256, 50256, 50256]])
```

Ở bước tiếp theo, ta gán biến đánh dấu `-100` cho tất cả pad token (hình 7.11). Đây là con số đặc biệt dùng để bỏ qua những ô bị độn thêm (padding) lúc tính loss, giúp ta đào tạo trên những token mang ý nghĩa thật sự (nhớ lại khi phân loại, ta không bận tâm lắm vì chỉ cần token xuất kết quả ở cuối cùng).

Tuy nhiên, ta sẽ phải giữ lại một `50256` token trong danh sách target (hình 7.12). Giữ lại nó giúp mô hình học cách sinh ra một tín hiệu ngắt dòng để báo nó đã hoàn thành câu lệnh.

Listing 7.5 sau đây sẽ đổi token 50256 trong target list thành `-100`. Đồng thời giới hạn độ dài `allowed_max_length` để cắt những câu lệnh vượt mức kích thước ngữ cảnh cho phép (context size).

[Hình 7.11: Đổi padding token thành placeholder `-100`.]
[Hình 7.12: Token `50256` đầu tiên thì giữ nguyên, nhưng các padding phía sau thì chuyển hết sang `-100`.]

**Listing 7.5: Triển khai hàm custom batch collate**

```python
def custom_collate_fn(
    batch,
    pad_token_id=50256,
    ignore_index=-100,
    allowed_max_length=None,
    device="cpu"
):
    batch_max_length = max(len(item)+1 for item in batch)
    inputs_lst, targets_lst = [], []
    
    for item in batch:
        new_item = item.copy()
        new_item += [pad_token_id]
        
        padded = (                              
            new_item + [pad_token_id] *         
            (batch_max_length - len(new_item))  
        )
        inputs = torch.tensor(padded[:-1])     
        targets = torch.tensor(padded[1:])    
        
        # Trích lọc tất cả các pad ngoại trừ pad đứng đầu
        mask = targets == pad_token_id             
        indices = torch.nonzero(mask).squeeze()    
        if indices.numel() > 1:                    
            targets[indices[1:]] = ignore_index    
            
        # Truncate nếu dữ liệu dài quá max
        if allowed_max_length is not None:
            inputs = inputs[:allowed_max_length]      
            targets = targets[:allowed_max_length]    
            
        inputs_lst.append(inputs)
        targets_lst.append(targets)
        
    inputs_tensor = torch.stack(inputs_lst).to(device)
    targets_tensor = torch.stack(targets_lst).to(device)
    return inputs_tensor, targets_tensor
```

Kiểm tra lại hàm:

```python
inputs, targets = custom_collate_fn(batch)
print(inputs)
print(targets)
```

Kết quả in ra chứng tỏ hàm đã đổi pad phụ thành `-100`:
```
tensor([[    0,     1,     2,     3,     4],
        [    5,     6, 50256, 50256, 50256],
        [    7,     8,     9, 50256, 50256]])
tensor([[    1,     2,     3,     4, 50256],
        [    6, 50256,  -100,  -100,  -100],
        [    8,     9, 50256,  -100,  -100]])
```

Tại sao lại là -100? Thử một ví dụ nhỏ tính cross-entropy.
```python
logits_1 = torch.tensor(
    [[-1.0, 1.0],    
     [-0.5, 1.5]]     
)
targets_1 = torch.tensor([0, 1]) 
loss_1 = torch.nn.functional.cross_entropy(logits_1, targets_1)
print(loss_1)
```
Hệ số sinh ra là `tensor(1.1269)`.

Thêm token ID thứ ba:
```python
logits_2 = torch.tensor(
    [[-1.0, 1.0],
     [-0.5, 1.5],
     [-0.5, 1.5]]     
)
targets_2 = torch.tensor([0, 1, 1])
loss_2 = torch.nn.functional.cross_entropy(logits_2, targets_2)
print(loss_2)
```
Hệ số là `tensor(0.7936)`.

Nhưng nếu ta thêm `-100` thay vì `1`:
```python
targets_3 = torch.tensor([0, 1, -100])
loss_3 = torch.nn.functional.cross_entropy(logits_2, targets_3)
print(loss_3)
print("loss_1 == loss_3:", loss_1 == loss_3)
```
Kết quả ra y chang `tensor(1.1269)`. `loss_1 == loss_3: tensor(True)`.

Nói cách khác, hàm cross entropy loss bỏ qua token có ID `-100`. Đó là vì tham số mặc định của cross entropy PyTorch có chứa tuỳ chọn `ignore_index=-100`.

Bên cạnh việc giấu đi padding, một kỹ thuật khác cũng rất được phổ biến là mask luôn cả những token thuộc phần chỉ dẫn (instruction) ở trong bộ dữ liệu (hình 7.13). Việc này khiến mô hình không học hỏi phần instruction (nhằm giảm overfitting) mà chỉ tập trung tối ưu quá trình sinh response.

[Hình 7.13: Masking (giấu) instruction bằng cách thay instruction thành các token ID `-100`.]

Tại thời điểm cuốn sách này đang soạn, giới nghiên cứu vẫn còn tranh cãi liệu masking instruction có thật sự tạo lợi thế hay không. Báo cáo 2024 "Instruction Tuning With Loss Over Instructions" lại chứng minh **không** masking có lợi hơn. Nên chúng ta không mask instruction, chỉ để lại đây như bài tập phụ cho ai muốn vọc.

> **Bài tập 7.2 Instruction and input masking**
> Sau khi tinh chỉnh mô hình xong ở cuối chương, bạn thử dùng `ignore_index` thay thế các token thuộc Instruction và đánh giá xem model có hoạt động tốt hơn không.

## 7.4 Khởi tạo các data loader cho bộ dữ liệu chỉ dẫn

Chúng ta đã hoàn thành một số giai đoạn để triển khai lớp `InstructionDataset` và hàm `custom_collate_fn`. Như trình bày trong hình 7.14, giờ ta đã sẵn sàng gặt hái thành quả bằng cách nhét `InstructionDataset` và hàm `custom_collate_fn` vào các data loader của PyTorch. Những data loader này sẽ tự động xáo trộn và xếp batch để tinh chỉnh LLM.

[Hình 7.14: Quy trình 3 bước tinh chỉnh chỉ dẫn. Ở bước 3, chúng ta lập Data loader cho các tập huấn luyện, xác thực và kiểm thử.]

Trước khi khởi tạo data loader, ta cần thiết lập cấu hình thiết bị phần cứng (device). Cụ thể, hàm `custom_collate_fn` có kèm sẵn phương thức để tải các tensor đầu vào và đầu ra sang biến thiết bị được chỉ định (bằng hàm `to(device)`). Các thiết bị khả dụng có thể là `"cpu"`, `"cuda"` (cho NVIDIA GPU) hoặc `"mps"` (cho các máy Mac có chip Apple Silicon).

> **LƯU Ý**
> Sử dụng `"mps"` có thể dẫn đến một chút khác biệt sai số so với kết quả trong sách, do tính năng hỗ trợ Apple Silicon trong PyTorch vẫn đang ở giai đoạn thử nghiệm.

Trước đây, ta di chuyển dữ liệu vào thẻ nhớ GPU (ví dụ, khi `device="cuda"`) trực tiếp trong vòng lặp huấn luyện chính. Nay việc đẩy tác vụ này sang hàm collate cho phép chạy việc tải tensor lên bộ nhớ đích dưới dạng tiến trình nền (background process), không làm gián đoạn GPU trong khi model đang training.

Đoạn mã sau khởi tạo biến `device`:

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Nếu dùng Apple Silicon Mac, hãy bỏ comment 2 dòng này
# if torch.backends.mps.is_available():  
#     device = torch.device("mps")"      

print("Device:", device)
```

Nó sẽ in ra `"Device: cpu"` hoặc `"Device: cuda"` tùy thuộc vào máy tính của bạn.

Tiếp theo, để tái sử dụng biến `device` này bên trong `custom_collate_fn` khi nạp nó vào lớp DataLoader của PyTorch, ta dùng hàm `partial` từ thư viện tiêu chuẩn `functools` của Python. Hàm này tạo một phiên bản mới của `custom_collate_fn` mà ở đó tham số `device` được gán sẵn. Ta cũng gán luôn thông số `allowed_max_length=1024` (chiều dài ngữ cảnh tối đa của GPT-2).

```python
from functools import partial

customized_collate_fn = partial(
    custom_collate_fn,
    device=device,
    allowed_max_length=1024
)
```

Bây giờ chúng ta thiết lập data loaders giống y cách đã làm ở các chương trước, nhưng lần này sẽ dùng hàm collate tùy biến ở trên.

**Listing 7.6: Khởi tạo các data loader**

```python
from torch.utils.data import DataLoader

# Bạn có thể tăng số này nếu HĐH hỗ trợ chạy song song
num_workers = 0     
batch_size = 8

torch.manual_seed(123)

train_dataset = InstructionDataset(train_data, tokenizer)
train_loader = DataLoader(
    train_dataset,
    batch_size=batch_size,
    collate_fn=customized_collate_fn,
    shuffle=True,
    drop_last=True,
    num_workers=num_workers
)

val_dataset = InstructionDataset(val_data, tokenizer)
val_loader = DataLoader(
    val_dataset,
    batch_size=batch_size,
    collate_fn=customized_collate_fn,
    shuffle=False,
    drop_last=False,
    num_workers=num_workers
)

test_dataset = InstructionDataset(test_data, tokenizer)
test_loader = DataLoader(
    test_dataset,
    batch_size=batch_size,
    collate_fn=customized_collate_fn,
    shuffle=False,
    drop_last=False,
    num_workers=num_workers
)
```

Kiểm tra kích thước của các tensor (chiều dọc và ngang) mà `train_loader` xuất ra:

```python
print("Train loader:")
for inputs, targets in train_loader:
    print(inputs.shape, targets.shape)
```

Đầu ra trông sẽ như sau:
```
Train loader:
torch.Size([8, 61]) torch.Size([8, 61])
torch.Size([8, 76]) torch.Size([8, 76])
torch.Size([8, 73]) torch.Size([8, 73])
...
torch.Size([8, 74]) torch.Size([8, 74])
torch.Size([8, 69]) torch.Size([8, 69])
```

Đầu ra này chứng minh batch thứ nhất có kích thước `8 × 61`, trong đó `8` là kích thước batch (số câu lệnh trong batch) và `61` là chiều dài theo token của câu lệnh dài nhất trong batch đó. Ở batch thứ hai, chiều dài này đổi thành `76`. Nhờ `custom_collate_fn`, data loader của chúng ta có khả năng tự động tạo ra những batch có độ dài uyển chuyển.

Ở phần sau, ta sẽ tải bộ trọng số của LLM đã được huấn luyện vào và bắt đầu tinh chỉnh.

## 7.5 Nạp bộ LLM đã tiền huấn luyện

Chúng ta đã dành rất nhiều thời gian chuẩn bị tập dữ liệu cho tinh chỉnh chỉ dẫn. Nhiều khía cạnh khác thì giống như trong quá trình tiền huấn luyện, do đó ta có thể tái sử dụng phần lớn code từ các chương trước.

Trước khi tinh chỉnh, trước hết ta phải tải mô hình GPT đã được tiền huấn luyện lên (xem hình 7.15). Lần này ta không sử dụng mô hình cỡ nhỏ `124 triệu tham số` (124M) nữa, thay vào đó ta dùng bản trung bình `355 triệu tham số` (355M). Sở dĩ đổi loại là vì model 124M không có đủ năng lực để đưa ra kết quả tinh chỉnh lệnh (instruction fine-tuning) thỏa đáng. Cụ thể, các model quá nhỏ không đủ nhạy bén để ghi nhớ các khuôn mẫu phức tạp và hành vi tinh tế cần thiết để tuân theo chỉ dẫn của người dùng.

[Hình 7.15: Tải bộ LLM đã tiền huấn luyện vào nền tảng. Đây là mô hình nền tảng làm xuất phát điểm cho các thao tác kế tiếp.]

Đoạn code nạp bộ trọng số giống y hệt ở mục 5.5 và 6.4, ngoại trừ chuỗi chỉ định giờ là `"gpt2-medium (355M)"`.

> **LƯU Ý**
> Khi chạy lệnh dưới đây, mô hình GPT cỡ trung sẽ được tải về ổ cứng (chiếm tầm 1.42 GB, tức gấp 3 lần so với loại small).

**Listing 7.7: Nạp mô hình đã tiền huấn luyện**

```python
from gpt_download import download_and_load_gpt2
from chapter04 import GPTModel
from chapter05 import load_weights_into_gpt

BASE_CONFIG = {
    "vocab_size": 50257,     # Vocabulary size
    "context_length": 1024,  # Context length
    "drop_rate": 0.0,        # Dropout rate
    "qkv_bias": True         # Query-key-value bias
}

model_configs = {
    "gpt2-small (124M)": {"emb_dim": 768, "n_layers": 12, "n_heads": 12},
    "gpt2-medium (355M)": {"emb_dim": 1024, "n_layers": 24, "n_heads": 16},
    "gpt2-large (774M)": {"emb_dim": 1280, "n_layers": 36, "n_heads": 20},
    "gpt2-xl (1558M)": {"emb_dim": 1600, "n_layers": 48, "n_heads": 25},
}

CHOOSE_MODEL = "gpt2-medium (355M)"

BASE_CONFIG.update(model_configs[CHOOSE_MODEL])

model_size = CHOOSE_MODEL.split(" ")[-1].lstrip("(").rstrip(")")
settings, params = download_and_load_gpt2(
    model_size=model_size, 
    models_dir="gpt2"
)

model = GPTModel(BASE_CONFIG)
load_weights_into_gpt(model, params)
model.eval()
```

Đầu ra khi chạy code báo hiệu một loạt các file liên quan đã được tải về:
```
checkpoint: 100%|██████████| 77.0/77.0 [00:00<00:00, 156kiB/s]
...
model.ckpt.data-00000-of-00001: 100%|██████████| 1.42G/1.42G 
```

Bây giờ ta hãy giành chút thời gian để kiểm tra xem cái mô hình tiền huấn luyện này xử lý chỉ dẫn "nguyên bản" tệ đến đâu. Lấy mẫu đầu tiên ở tập validation (xác thực) ra để mổ xẻ:

```python
torch.manual_seed(123)
input_text = format_input(val_data[0])
print(input_text)
```

Nội dung chuỗi chỉ dẫn (instruction) là:
```
Below is an instruction that describes a task. Write a response that 
appropriately completes the request.

### Instruction:
Convert the active sentence to passive: 'The chef cooks the meal every day.'
```

Sử dụng hàm `generate` (lấy từ chương 5) để sinh câu trả lời:

```python
from chapter05 import generate, text_to_token_ids, token_ids_to_text

token_ids = generate(
    model=model,
    idx=text_to_token_ids(input_text, tokenizer),
    max_new_tokens=35,
    context_size=BASE_CONFIG["context_length"],
    eos_id=50256,
)

generated_text = token_ids_to_text(token_ids, tokenizer)
```

Vì hàm `generate` sẽ trả về văn bản đầu ra nối tiếp ngay sau đầu vào, nên ta cần phải loại bỏ đoạn input khỏi kết quả `generated_text` bằng cách gọt bớt:

```python
response_text = generated_text[len(input_text):].strip()
print(response_text)
```

Đoạn code trên cắt phần input text ở đầu ra khỏi chuỗi kết quả `generated_text`, và dùng `.strip()` xóa bỏ các ký tự khoảng trắng thừa. Kết quả in ra là:

```
### Response:
The chef cooks the meal every day.

### Instruction:
Convert the active sentence to passive: 'The chef cooks the
```

Ta có thể thấy rõ ràng một mô hình vừa được tiền huấn luyện hoàn toàn vô dụng trong việc hoàn thành một chỉ dẫn cụ thể (ở đây là biến câu chủ động thành bị động). Nó chỉ lặp lại cái câu chủ động, sau đó lại viết tiếp một cái mác `### Instruction:` nữa như kiểu bị rối loạn chức năng. Nên bây giờ ta bắt tay vào tinh chỉnh để nó hành xử giống như một chatbot đàng hoàng.

## 7.6 Tinh chỉnh LLM với dữ liệu chỉ dẫn

Đã đến lúc tinh chỉnh LLM trên tập dữ liệu chỉ dẫn (hình 7.16). Chúng ta sẽ lấy mô hình tiền huấn luyện vừa nạp ở trên và đào tạo nó (fine-tune) bằng dataset ở đầu chương. Mọi công việc nặng nhọc như tính loss hay vòng lặp đào tạo đều có thể lấy trực tiếp từ chương 5 qua:

[Hình 7.16: Tinh chỉnh mô hình dựa trên tập dữ liệu chỉ dẫn.]

```python
from chapter05 import (
    calc_loss_loader,
    train_model_simple
)
```

Trước khi đào tạo, ta chạy hàm để biết điểm khởi đầu của độ đo suy hao (loss):

```python
model.to(device)
torch.manual_seed(123)

with torch.no_grad():
    train_loss = calc_loss_loader(
        train_loader, model, device, num_batches=5
    )
    val_loss = calc_loss_loader(
        val_loader, model, device, num_batches=5
    )

print("Training loss:", train_loss)
print("Validation loss:", val_loss)
```

Điểm hao hụt (loss) khởi đầu của mô hình là:
```
Training loss: 3.825908660888672
Validation loss: 3.7619335651397705
```

> **Cách đối phó với giới hạn phần cứng**
> Việc đào tạo một model cỡ vừa (355 triệu tham số) yêu cầu năng lực điện toán cao hơn loại model 124M. Nếu gặp lỗi thiếu phần cứng, hãy chuyển biến `CHOOSE_MODEL = "gpt2-medium (355M)"` thành `CHOOSE_MODEL = "gpt2-small (124M)"`.
> Hoặc để đẩy tốc độ nhanh hơn, hãy sử dụng GPU đám mây. Bạn có thể tham khảo một vài nền tảng GPU đám mây ở mục phụ lục (https://mng.bz/EOEq).
> Bảng sau hiển thị tốc độ đào tạo trung bình cho 2 epoch:
> - `gpt2-medium (355M)` trên CPU (M3 MacBook Air): 15.78 phút
> - `gpt2-medium (355M)` trên GPU (NVIDIA L4): 1.83 phút
> - `gpt2-medium (355M)` trên GPU (NVIDIA A100): 0.86 phút
> - `gpt2-small (124M)` trên CPU (M3 MacBook Air): 5.74 phút
> - `gpt2-small (124M)` trên GPU (NVIDIA L4): 0.69 phút
> - `gpt2-small (124M)` trên GPU (NVIDIA A100): 0.39 phút

Đoạn code trong listing 7.8 khởi tạo bộ cấu hình huấn luyện (ví dụ gán optimizer, learning rate, số epoch là 2). Ta cũng sẽ in mẫu đầu tiên ở tập validation (xác thực) ra màn hình sau mỗi chặng để theo dõi chất lượng trả lời.

**Listing 7.8: Tiến hành tinh chỉnh chỉ dẫn LLM**

```python
import time

start_time = time.time()
torch.manual_seed(123)

optimizer = torch.optim.AdamW(
    model.parameters(), lr=0.00005, weight_decay=0.1
)

num_epochs = 2

train_losses, val_losses, tokens_seen = train_model_simple(
    model, train_loader, val_loader, optimizer, device,
    num_epochs=num_epochs, eval_freq=5, eval_iter=5,
    start_context=format_input(val_data[0]), tokenizer=tokenizer
)

end_time = time.time()
execution_time_minutes = (end_time - start_time) / 60
print(f"Training completed in {execution_time_minutes:.2f} minutes.")
```

Đầu ra phản ánh tiến trình tập luyện:

```
Ep 1 (Step 000000): Train loss 2.637, Val loss 2.626
Ep 1 (Step 000005): Train loss 1.174, Val loss 1.103
Ep 1 (Step 000010): Train loss 0.872, Val loss 0.944
Ep 1 (Step 000015): Train loss 0.857, Val loss 0.906
...
Ep 1 (Step 000115): Train loss 0.520, Val loss 0.665

Below is an instruction that describes a task. Write a response that 
appropriately completes the request.  ### Instruction: Convert the 
active sentence to passive: 'The chef cooks the meal every day.' 
### Response: The meal is prepared every day by the chef.<|endoftext|>
The following is an instruction that describes a task. 
Write a response that appropriately completes the request.  
### Instruction: Convert the active sentence to passive:

Ep 2 (Step 000120): Train loss 0.438, Val loss 0.670
...
Ep 2 (Step 000230): Train loss 0.300, Val loss 0.657

Below is an instruction that describes a task. Write a response 
that appropriately completes the request.  ### Instruction: 
Convert the active sentence to passive: 'The chef cooks the meal 
every day.'  ### Response: The meal is cooked every day by the 
chef.<|endoftext|>The following is an instruction that describes 
a task. Write a response that appropriately completes the request.  
### Instruction: What is the capital of the United Kingdom

Training completed in 0.87 minutes.
```

Đầu ra chứng tỏ mô hình học hỏi rất hiệu quả, khi mà điểm hao hụt (loss) của quá trình train và validation liên tục tụt dốc sau 2 vòng học (epoch). Điều này cho thấy mô hình đang cải thiện năng lực nhận thức và tuân thủ lệnh của người dùng. (Vì mô hình hoạt động hiệu quả qua 2 epoch nên không cần thiết cho học tới epoch thứ 3, vì có thể dẫn tới overfitting - tức học vẹt).

Ngoài ra, câu trả lời sinh ra ở cuối mỗi epoch cho thấy mô hình hoàn thành xuất sắc câu lệnh "chuyển sang bị động" ở trong tập dữ liệu thử. Thay vì trả lời ngớ ngẩn như mục 7.5, thì ở đây LLM đã đổi mẫu câu "The chef cooks the meal every day." (Đầu bếp nấu ăn mỗi ngày) thành "The meal is cooked every day by the chef" (Bữa ăn được nấu mỗi ngày bởi người đầu bếp). 

Hãy trực quan hóa đường cong thể hiện giá trị giảm dần của validation loss bằng thư viện pyplot:

```python
from chapter05 import plot_losses

epochs_tensor = torch.linspace(0, num_epochs, len(train_losses))
plot_losses(epochs_tensor, tokens_seen, train_losses, val_losses)
```

Biểu đồ hình 7.17 biểu thị tốc độ tiếp thu siêu đẳng của model ở đầu kỳ, giảm dần gia tốc ở cuối kỳ - biểu hiện của mô hình dần bước tới trạng thái hội tụ (stable solution).

[Hình 7.17: Biểu đồ đường cong validation loss so với train loss sau hai chu kì học.]

Mặc dù biểu đồ hình 7.17 cho thấy mô hình được học hiệu quả, nhưng điều quan trọng nhất vẫn là năng lực hiểu câu hỏi. Bước kế tiếp ta sẽ phải xuất hệ thống lưu trữ kết quả đầu ra của mô hình rồi đi đánh giá.

## 7.7 Trích xuất và lưu trữ các phản hồi

Sau khi đã tinh chỉnh mô hình LLM trên tập huấn luyện của dataset chỉ dẫn, giờ đây ta sẽ đánh giá khả năng của nó trên tập kiểm thử (test set) chưa từng được thấy trước đó. Trước tiên, ta cần trích xuất các câu trả lời mà mô hình sinh ra tương ứng với mỗi đầu vào trong test set. Sau đó ta có thể đọc và phân tích thủ công, cuối cùng đánh giá LLM để đưa ra điểm số định lượng cho chất lượng trả lời (theo quy trình ở hình 7.18).

> **Bài tập 7.3 Tinh chỉnh trên tập Alpaca nguyên bản**
> Tập dữ liệu Alpaca, do các nhà nghiên cứu tại Stanford tạo ra, là một trong những tập dữ liệu chỉ dẫn mã nguồn mở sớm nhất và phổ biến nhất, với 52.002 bản ghi. Thay cho file `instruction-data.json`, hãy thử tinh chỉnh LLM bằng tập dữ liệu này. File dữ liệu có tại https://mng.bz/NBnE.
> Do kích thước lớn hơn gấp 50 lần so với tập chúng ta dùng, phần lớn các câu lại rất dài, tác giả khuyến nghị bạn nên dùng GPU để huấn luyện nhằm tăng tốc quá trình. Nếu gặp lỗi hết bộ nhớ (out-of-memory), hãy giảm `batch_size` từ 8 xuống 4, 2 hoặc 1. Giảm `allowed_max_length` từ 1024 xuống 512 hoặc 256 cũng giúp giải quyết lỗi bộ nhớ.

[Hình 7.18: Quy trình 3 bước tinh chỉnh chỉ dẫn. Ở bước 7 và 8, ta trích xuất câu trả lời của mô hình sinh ra từ test set để làm nguyên liệu, sau đó đem đi đánh giá.]

Để hoàn thành bước trích xuất phản hồi, ta sẽ sử dụng lại hàm `generate`. Dưới đây, ta in phản hồi của mô hình song song với câu trả lời dự kiến của test set đối với ba bản ghi đầu tiên, đặt chúng cạnh nhau để dễ bề so sánh:

```python
torch.manual_seed(123)

for entry in test_data[:3]:     
    input_text = format_input(entry)
    
    token_ids = generate(              
        model=model,
        idx=text_to_token_ids(input_text, tokenizer).to(device),
        max_new_tokens=256,
        context_size=BASE_CONFIG["context_length"],
        eos_id=50256
    )
    generated_text = token_ids_to_text(token_ids, tokenizer)
    
    response_text = (
        generated_text[len(input_text):]
        .replace("### Response:", "")
        .strip()
    )
    
    print(input_text)
    print(f"\nCorrect response:\n>> {entry['output']}")
    print(f"\nModel response:\n>> {response_text.strip()}")
    print("-------------------------------------")
```

Như đã đề cập trước đó, hàm `generate` trả về chuỗi nối ghép cả đầu vào và đầu ra, vì vậy ta dùng kỹ thuật cắt chuỗi (slicing) và phương thức `.replace()` trên chuỗi `generated_text` để lấy phần trả lời của mô hình. Các chỉ dẫn, theo sau bởi kết quả mẫu trong test set và phản hồi thực tế của model, được hiển thị như sau.

```
Below is an instruction that describes a task. Write a response that appropriately
completes the request.
### Instruction:
Rewrite the sentence using a simile.
### Input:
The car is very fast.

Correct response:
>> The car is as fast as lightning.

Model response:
>> The car is as fast as a bullet.
-------------------------------------
Below is an instruction that describes a task. Write a response that appropriately
completes the request.
### Instruction:
What type of cloud is typically associated with thunderstorms?

Correct response:
>> The type of cloud typically associated with thunderstorms is cumulonimbus.

Model response:
>> The type of cloud associated with thunderstorms is a cumulus cloud.
-------------------------------------
Below is an instruction that describes a task. Write a response that appropriately
completes the request.
### Instruction:
Name the author of ‘Pride and Prejudice.’

Correct response:
>> Jane Austen.

Model response:
>> The author of ‘Pride and Prejudice’ is Jane Austen.
-------------------------------------
```

Như chúng ta có thể thấy dựa trên các chỉ dẫn của test set, đáp án gợi ý và phản hồi của mô hình, mô hình hoạt động tương đối tốt. Các câu trả lời cho câu lệnh thứ nhất và thứ ba rõ ràng là đúng, trong khi câu trả lời thứ hai gần đúng nhưng không hoàn toàn chính xác. Mô hình trả lời bằng "cumulus cloud" (mây tích) thay vì "cumulonimbus" (mây vũ tích), mặc dù cần lưu ý rằng đám mây tích có thể phát triển thành đám mây vũ tích để tạo ra giông bão.

Quan trọng nhất, việc đánh giá mô hình không hề đơn giản như trong nhiệm vụ phân loại (khi mà ta chỉ cần tính phần trăm nhãn spam/non-spam đúng để ra độ chính xác). Trong thực tế, các LLM tuân thủ lệnh như chatbot được đánh giá thông qua nhiều cách tiếp cận:
- Các benchmark dạng trắc nghiệm hoặc câu hỏi ngắn, như MMLU, dùng để kiểm tra kiến thức tổng quát của mô hình.
- So sánh sự ưu tiên bởi con người (Human preference) với các LLM khác, chẳng hạn như LMSYS chatbot arena.
- Các benchmark đàm thoại tự động (Automated conversational benchmarks), nơi một LLM ưu việt hơn như GPT-4 được chỉ định làm giám khảo chấm điểm các câu trả lời, điển hình là phương pháp của AlpacaEval.

Trong thực tế, việc kết hợp cả ba phương pháp đánh giá (trả lời trắc nghiệm, đánh giá bởi người, và thang đo tự động) là rất hữu ích. Tuy nhiên, vì mục tiêu chính của chúng ta là xem xét hiệu suất đàm thoại thay vì giải trắc nghiệm, phương pháp đánh giá của người dùng và hệ thống điểm tự động sẽ phù hợp hơn cả.

Đánh giá bởi con người, dù mang lại những góc nhìn giá trị, có thể tốn khá nhiều công sức và thời gian, đặc biệt khi phải đối phó với số lượng phản hồi lớn. Ví dụ, việc đọc và chấm điểm tất cả 1.100 phản hồi sẽ đòi hỏi một lượng công sức đáng kể.

Vì vậy, cân nhắc tới quy mô tác vụ, chúng ta sẽ áp dụng phương pháp tự động hóa bằng cách sử dụng một LLM khác để chấm điểm. Phương pháp này cho phép đánh giá chất lượng phản hồi một cách nhanh chóng mà không cần tốn quá nhiều sức người, giúp tiết kiệm thời gian và tài nguyên mà vẫn thu được các thông số đánh giá hợp lý.

Hãy lấy cảm hứng từ AlpacaEval, sử dụng một LLM khác để làm giám khảo. Tuy nhiên, thay vì phụ thuộc vào một bộ dataset benchmark có sẵn trên mạng, ta tự dùng bộ test set tùy biến của chính mình (chính là file dữ liệu 1.100 câu). Điều này giúp nhắm thẳng vào các tính năng mà người dùng muốn hướng tới.

Để chuẩn bị, ta ghép phản hồi do mô hình sinh ra vào dictionary `test_set` rồi lưu dưới tên `"instruction-data-with-response.json"`. File này giúp dễ dàng phân tích phản hồi ở các phiên Python khác nhau.

Đoạn code Listing 7.9 dưới đây dùng hàm `generate` tương tự như trước, nhưng giờ lặp qua toàn bộ `test_set`. Thay vì in, nó chèn kết quả trực tiếp vào biến dictionary.

**Listing 7.9: Khởi tạo các câu trả lời test set**

```python
from tqdm import tqdm

for i, entry in tqdm(enumerate(test_data), total=len(test_data)):
    input_text = format_input(entry)
    token_ids = generate(
        model=model,
        idx=text_to_token_ids(input_text, tokenizer).to(device),
        max_new_tokens=256,
        context_size=BASE_CONFIG["context_length"],
        eos_id=50256
    )
    generated_text = token_ids_to_text(token_ids, tokenizer)
    
    response_text = (
        generated_text[len(input_text):]
        .replace("### Response:", "")
        .strip()
    )
    test_data[i]["model_response"] = response_text

with open("instruction-data-with-response.json", "w") as file:
    # indent cho dễ đọc
    json.dump(test_data, file, indent=4)        
```

Xử lý toàn bộ dataset mất tầm 1 phút trên A100 GPU và 6 phút trên M3 MacBook Air. Cột tiến độ hiển thị như sau:
```
100%|██████████| 110/110 [01:05<00:00,  1.68it/s]
```

Chúng ta cùng kiểm tra lại xem các phản hồi đã được nhét vào trong dictionary của `test_set` chưa:
```python
print(test_data[0])
```

Đầu ra chứng tỏ trường `model_response` đã được lưu chính xác:
```
{'instruction': 'Rewrite the sentence using a simile.', 
 'input': 'The car is very fast.', 
 'output': 'The car is as fast as lightning.', 
 'model_response': 'The car is as fast as a bullet.'}
```

Cuối cùng, chúng ta lưu model thành file `gpt2-medium355M-sft.pth` để tiện sử dụng lại trong tương lai:
```python
import re

# Xóa khoảng trắng và dấu ngoặc khỏi tên file
file_name = f"{re.sub(r'[ ()]', '', CHOOSE_MODEL) }-sft.pth"     
torch.save(model.state_dict(), file_name)
print(f"Model saved as {file_name}")
```

Mô hình đã lưu này sau đó có thể tải lên qua phương thức `model.load_state_dict(torch.load("gpt2-medium355M-sft.pth"))`.

## 7.8 Đánh giá tự động LLM đã tinh chỉnh

Trước đó, chúng ta đánh giá hiệu năng của mô hình LLM qua ba ví dụ nhỏ ở đầu test set. Mặc dù nó cho một góc nhìn tổng quan, nhưng phương thức này không mở rộng hiệu quả khi số lượng dữ liệu test phình to. Vì vậy, ta sẽ xây dựng hệ thống để một "ông lớn" LLM đứng ra tự động chấm điểm cho mô hình nhỏ (theo hình 7.19).

Để tự động chấm điểm, ta nhờ tới sức mạnh của mô hình 8-tỉ tham số Llama 3 do Meta AI thiết kế (phiên bản đã tinh chỉnh theo lệnh). Ta có thể kích hoạt Llama 3 cục bộ qua nền tảng mã nguồn mở Ollama (https://ollama.com).

> **LƯU Ý**
> Ollama là một phần mềm hỗ trợ chạy LLMs gọn nhẹ trên máy tính cá nhân. Nó bao bọc thư viện `llama.cpp`, vận hành mã C/C++ nhằm tối đa hóa tốc độ tải (inference). Ollama không có tính năng huấn luyện hay tinh chỉnh LLM, nó chỉ nhận lệnh và sinh đáp án.

Để chạy được đoạn code phía dưới, bạn cần cài đặt Ollama từ website gốc (chọn Yes nếu được hỏi cài đặt cho giao diện dòng lệnh cmd).

Trước khi tiến hành chấm điểm bằng code Python, ta nên tải Llama 3 và chạy một phiên ở giao diện lệnh terminal cho chắc (Hình 7.20).

> **Dùng API của các LLM khổng lồ**
> Phiên bản Llama 3 8 tỉ tham số là một mô hình rất mạnh mẽ có khả năng chạy local. Tuy nhiên, nó vẫn chưa sánh bằng các model khổng lồ thương mại (proprietary LLMs) như GPT-4 của OpenAI. Nếu bạn muốn tận dụng GPT-4 thông qua REST API để chấm điểm, tôi đã để sẵn một notebook trong tài liệu phụ lục (https://mng.bz/BgEv).

[Hình 7.19: Sử dụng một LLM khác để chấm điểm bộ phản hồi của mô hình mà ta vừa huấn luyện.]
[Hình 7.20: Các phương pháp khởi chạy hệ thống Ollama bằng terminal, sau đó nạp Llama3 bằng lệnh `ollama run llama3`.]

Khi Ollama đã được khởi tạo qua terminal (hoặc ứng dụng Ollama), ta gõ dòng lệnh sau ở tab lệnh mới:
```bash
ollama run llama3
```

Ở lần chạy đầu tiên, Ollama sẽ phải tải một lượng lớn file với dung lượng 4.7 GB. Quá trình hiển thị như sau:
```
pulling manifest
pulling 6a0746a1ec1a... 100% |████████████████| 4.7 GB
...
success
```

Khi download hoàn tất, Ollama mở ra một giao diện đàm thoại (chat) ở terminal, bạn có thể thử hỏi nó bằng tiếng Anh như "What do llamas eat?" (Llama ăn gì?):
```
>>> What do llamas eat?
Llamas are ruminant animals, which means they have a four-chambered
stomach and eat plants that are high in fiber. In the wild, 
llamas typically feed on:
1. Grasses: They love to graze on various types of grasses, including tall
grasses, wheat, oats, and barley.
```

(Chú ý rằng câu trả lời của bạn có thể khác biệt vì Llama không đưa ra các câu trả lời tất định - deterministic). Bạn có thể kết thúc phiên hỏi đáp bằng lệnh `/bye`. Tuy nhiên, bạn phải đảm bảo hệ thống Ollama vẫn đang hoạt động ẩn (chạy ứng dụng nền hoặc giữ lệnh `ollama serve`) cho phần còn lại của chương này.

Đoạn mã sau kiểm tra xem ứng dụng Ollama đã được bật đúng cách hay chưa:

```python
import psutil

def check_if_running(process_name):
    running = False
    for proc in psutil.process_iter(["name"]):
        if process_name in proc.info["name"]:
            running = True
            break
    return running

ollama_running = check_if_running("ollama")

if not ollama_running:
    raise RuntimeError(
        "Ollama not running. Launch ollama before proceeding."
)
print("Ollama running:", check_if_running("ollama"))
```

> **Các LLM cỡ nhỏ khác trên Ollama**
> Khai báo lệnh `llama3` trong `ollama run` tức là gọi bản Llama 3 - 8 tỉ tham số. Model này tốn tầm 16 GB bộ nhớ RAM để vận hành. Nếu máy tính bạn yếu, bạn có thể gọi model cỡ nhỏ `phi3` với 3.8 tỉ tham số, chỉ yêu cầu vỏn vẹn 8 GB RAM. Ngược lại, nếu máy bạn cực trâu, hãy gọi bản 70-tỉ bằng thẻ `llama3:70b`.

Đảm bảo đầu ra in ra `Ollama running: True`. Nếu là False, tức là hệ thống đang tắt, bạn phải kiểm tra lại xem Ollama đã chạy ở chế độ nền chưa.

Thay vì gõ lệnh trên terminal, ta có thể dùng code Python để gọi model thông qua REST API do Ollama mở sẵn. Hàm `query_model` dưới đây mô phỏng phương pháp này.

**Listing 7.10: Truy vấn (Querying) mô hình local của Ollama**

```python
import urllib.request
import json

def query_model(
    prompt, 
    model="llama3", 
    url="http://localhost:11434/api/chat"
):
    # Tạo danh sách các cấu hình 
    data = {            
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "options": {        
            "seed": 123,
            "temperature": 0,
            "num_ctx": 2048
        }
    }
    
    # Chuyển từ điển dictionary sang chuỗi JSON và giải nén byte 
    payload = json.dumps(data).encode("utf-8")   
    
    # Thiết lập request dưới dạng POST
    request = urllib.request.Request(                      
        url,                                               
        data=payload,                                      
        method="POST"                                      
    )
    
    request.add_header("Content-Type", "application/json")  
    
    response_data = ""
    # Mở liên kết API và hứng response
    with urllib.request.urlopen(request) as response:  
        while True:
            line = response.readline().decode("utf-8")
            if not line:
                break
            response_json = json.loads(line)
            response_data += response_json["message"]["content"]
            
    return response_data
```

*(Ghi chú: Nếu bạn muốn chạy các đoạn code tiếp theo trong một phiên Python hoàn toàn mới, hãy tự tạo hàm `format_input` cũng như biến `test_data` từ file json mới tải).*

Thử chạy hàm `query_model` để hỏi LLM Llama3:
```python
model = "llama3"
result = query_model("What do Llamas eat?", model)
print(result)
```
Kết quả in ra sẽ trông như sau:
```
Llamas are ruminant animals, which means they have a four-chambered 
stomach that allows them to digest plant-based foods. Their diet 
typically consists of:
1. Grasses: Llamas love to graze on grasses, including tall grasses, 
short grasses, and even weeds.
...
```

Dựa vào hàm truy vấn này, ta có thể nhồi một đoạn Prompt vào để nhờ Llama 3 chấm điểm câu trả lời của mô hình GPT tự trồng, theo thang từ 0-100 với căn cứ là lời giải có trong dataset. Thử nghiệm ngay với 3 ví dụ ban nãy:

```python
for entry in test_data[:3]:
    prompt = (
        f"Given the input `{format_input(entry)}` "
        f"and correct output `{entry['output']}`, "
        f"score the model response `{entry['model_response']}`"
        f" on a scale from 0 to 100, where 100 is the best score. "
    )
    print("\nDataset response:")
    print(">>", entry['output'])
    print("\nModel response:")
    print(">>", entry["model_response"])
    print("\nScore:")
    print(">>", query_model(prompt))
    print("\n-------------------------")
```

Kết quả sẽ na ná như thế này (Ollama không có tính tất định 100% nên câu văn sẽ bị khác nhau ở mỗi lần chạy):
```
Dataset response:
>> The car is as fast as lightning.
Model response:
>> The car is as fast as a bullet.
Score:
>> I’d rate the model response “The car is as fast as a bullet.” an 85 out of 100.
Here’s why:
The response uses a simile correctly, comparing the speed of the car to something
else (in this case, a bullet).
The comparison is relevant and makes sense, as bullets are known for their high
velocity.
The phrase “as fast as” is used correctly to introduce the simile.
The only reason I wouldn’t give it a perfect score is that some people might find the
comparison slightly less vivid or evocative than others. For example, comparing
something to lightning (as in the original response) can be more dramatic and atten-
tion grabbing. However, “as fast as a bullet” is still a strong and effective simile that
effectively conveys the idea of the car’s speed.
Overall, I think the model did a great job!
-------------------------
Dataset response:
>> The type of cloud typically associated with thunderstorms is cumulonimbus.
Model response:
>> The type of cloud associated with thunderstorms is a cumulus cloud.
Score:
>> I’d score this model response as 40 out of 100.
Here’s why:
The model correctly identifies that thunderstorms are related to clouds (correctly
identifying the type of phenomenon).
However, it incorrectly specifies the type of cloud associated with thunderstorms.
Cumulus clouds are not typically associated with thunderstorms; cumulonimbus
clouds are.
The response lacks precision and accuracy in its description.
Overall, while the model attempts to address the instruction, it provides an incorrect
answer, which is a significant error.
-------------------------
Dataset response:
>> Jane Austen.
Model response:
>> The author of ‘Pride and Prejudice’ is Jane Austen.
Score:
>> I’d rate my own response as 95 out of 100. Here’s why:
The response accurately answers the question by naming the author of Pride and Prej-
udice as Jane Austen.
The response is concise and clear, making it easy to understand.
There are no grammatical errors or ambiguities that could lead to confusion.
The only reason I wouldn’t give myself a perfect score is that the response is slightly
redundant—it’s not necessary to rephrase the question in the answer. A more con-
cise response would be simply “Jane Austen.”
```

Các kết quả trên cho thấy Llama 3 cung cấp những đánh giá rất hợp lý và biết phân chia điểm số hợp tình hợp lý khi mô hình đưa ra một câu trả lời gần đúng nhưng không trúng (như ví dụ thứ hai "cumulus cloud").

Bên cạnh con số hiển thị điểm, Prompt hiện tại xuất ra những bài đánh giá phân tích dài dòng. Chúng ta nên sửa lại câu nhắc để yêu cầu trả về giá trị số (integer scores) từ 0 đến 100 nhằm mục đích tính điểm trung bình (average score). Hàm `generate_model_scores` dưới đây chỉnh lại prompt bằng câu chốt "Respond with the integer number only."

**Listing 7.11: Đánh giá mô hình LLM đã tinh chỉnh chỉ dẫn**

```python
def generate_model_scores(json_data, json_key, model="llama3"):
    scores = []
    for entry in tqdm(json_data, desc="Scoring entries"):
        prompt = (
            f"Given the input `{format_input(entry)}` "
            f"and correct output `{entry['output']}`, "
            f"score the model response `{entry[json_key]}`"
            f" on a scale from 0 to 100, where 100 is the best score. "
            f"Respond with the integer number only."  
        )
        
        score = query_model(prompt, model)
        try:
            scores.append(int(score))
        except ValueError:
            print(f"Could not convert score: {score}")
            continue
            
    return scores
```

Áp dụng hàm `generate_model_scores` vào mảng `test_data`, mất khoảng 1 phút trên máy M3 Macbook Air:

```python
scores = generate_model_scores(test_data, "model_response")
print(f"Number of scores: {len(scores)} of {len(test_data)}")
print(f"Average score: {sum(scores)/len(scores):.2f}\n")
```

Kết quả nhận được:
```
Scoring entries: 100%|████████████████████████| 110/110 
[01:10<00:00,  1.56it/s]
Number of scores: 110 of 110
Average score: 50.32
```

Kết quả trả về cho thấy mô hình của chúng ta đạt điểm trung bình 50 (rất xuất sắc). Đây là một cột mốc để chúng ta đem đi so sánh với các loại mô hình tiên tiến khác, hoặc để thử nghiệm những cấu hình (hyper-parameters) đào tạo đa dạng nhằm đẩy cao giới hạn.

(Ghi chú: Llama chạy Ollama hiện vẫn chưa có tính chất tất định, nên mỗi lần bạn chấm nó sẽ đưa ra một con số khác nhau. Để kết quả chính xác và chặt chẽ, ta nên quét lại vài lần rồi tính trung bình).

Có vô vàn cách để đẩy cao thông số của LLM:
- Chỉnh các hệ số hyper-parameters trong lúc huấn luyện, tỉ như learning rate, batch size, số lượng epochs.
- Nâng dung lượng tập huấn luyện (training dataset), lấy nhiều mẫu đa dạng trải đều các lĩnh vực học thuật khác nhau.
- Thử nghiệm với các dạng format prompt khác nhau (như Phi-3 đã làm) để điều tiết phản hồi.
- Tải bộ trọng số mô hình lớn hơn (ví dụ cỡ GPT Large), đem tới một năng lực tư duy, biểu thị và giải đáp tốt hơn.

> **LƯU Ý**
> Để làm một vài phép so sánh, mô hình cơ sở Llama 3 8B nguyên bản (bản chưa tinh chỉnh qua dataset), khi đem vào chấm sẽ lấy trung bình 58.51 điểm trên test set. Bản Llama 3 8B instruct thì đạt 82.6 điểm.

## 7.9 Kết luận

Chương này đánh dấu cột mốc quan trọng trong lộ trình phát triển LLM. Chúng ta đã bao phủ hết mọi bước đi tinh hoa nhất, từ mã hóa kiến trúc LLM, cho tới việc tiền huấn luyện và tinh chỉnh cho từng tác vụ riêng rẽ.

[Hình 7.21: Sơ đồ bao quát ba giai đoạn phát triển LLM.]

### 7.9.1 Bạn có thể học gì tiếp theo?

Mặc dù khóa huấn luyện đã phủ kín các mảng cốt lõi, vẫn còn một nước đi ẩn mà người ta gọi là **tinh chỉnh ưu tiên** (preference fine-tuning). Nước đi này hướng model trở nên "chăm sóc khách hàng" và nhã nhặn với người dùng hơn. Nếu hứng thú, bạn hãy ghé repo github có thư mục tên `04_preference-tuning-with-dpo` tại https://mng.bz/dZwD.

> **Bài tập 7.4 Tinh chỉnh với hệ số thông minh LoRA**
> Để thực hiện quá trình đào tạo tinh chỉnh nhẹ nhàng hơn, thay đổi code trong chương bằng kĩ thuật Low-Rank Adaptation (LoRA) ở Phụ lục E. Sau đó đối chiếu lại với tốc độ train của chúng ta hôm nay xem có gì khác biệt.

Một rổ tính năng bonus của khóa học được tác giả đặt tại mục "Bonus Material" tại https://mng.bz/r12g.

### 7.9.2 Bắt kịp xu hướng trong kỉ nguyên biến động

AI/LLM đang chạy đua quá nhanh. Cách tốt nhất để không bị tụt lại là theo dõi các diễn đàn khoa học như https://arxiv.org/list/cs.LG/recent. Hoặc tham gia mạng xã hội X hay subreddit cộng đồng `r/LocalLLaMA`. Tôi (tác giả) cũng thường xuyên phổ cập kiến thức tại blog https://magazine.sebastianraschka.com và https://sebastianraschka.com/blog/.

### 7.9.3 Đôi lời muốn nói

Tôi hi vọng bạn đã tận hưởng chuyến xe dài hạn này, tự tay xây dựng mô hình LLM khổng lồ từ hai bàn tay trắng bằng những dòng mã. Xây mọi thứ từ đầu là phương pháp luận hiệu quả nhất để nhét kiến thức nền tảng vô trong vỏ não. Tôi cũng hi vọng nó mang tới nền tảng cho sự nghiệp và giá trị của bạn.

Dù cuốn sách nhắm vào việc giáo dục, bạn hoàn toàn có thể vươn xa hơn, vận hành các tool quyền lực hơn như Axolotl hoặc LitGPT (những thứ mà tôi đang tích cực tham gia cống hiến).

Cảm ơn bạn đã gắn bó với chuyến xe này. Tôi chúc bạn những điều tuyệt vời nhất trong tương lai ở một kỉ nguyên bùng nổ LLMs và trí tuệ nhân tạo (AI)!

## Tóm tắt

- Quy trình tinh chỉnh chỉ dẫn giúp uốn nắn một LLM đã qua tiền huấn luyện theo đúng mệnh lệnh của con người.
- Việc chuẩn bị dữ liệu xoay quanh bộ data instruction-response, định dạng (format) và chia tách (train, val, test).
- Tập hợp Batch bằng hàm custom_collate_fn (gắn pad, dịch tọa độ, dùng mặt nạ masking `-100`).
- Ta nạp model tầm trung GPT-2 (355 triệu thông số) làm nền móng (foundation).
- Vòng lặp tinh chỉnh lấy y hệt vòng lặp tiền huấn luyện.
- Đánh giá thông qua một máy chấm (một LLM khác).
- Ollama với bản Llama 8-tỉ thông số là môt giám khảo tuyệt vời tự động đánh giá kết quả, thu thập điểm trung bình để đo đếm năng lực của model.
