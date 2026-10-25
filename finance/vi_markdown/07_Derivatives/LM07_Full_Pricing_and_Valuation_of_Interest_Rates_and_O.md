# Tập 7: Công cụ Phái sinh (Derivatives)
## Learning Module 7 Pricing and Valuation of Interest Rates and Other Swaps (Trang PDF 157–178)

---

# Tập 7: Công cụ Phái sinh (*Derivatives*)
## Học phần 7: Định giá và Xác định giá trị của Hợp đồng Hoán đổi Lãi suất và Các Hợp đồng Hoán đổi Khác (*Pricing and Valuation of Interest Rates and Other Swaps*)
### Phần 1/2: Giới thiệu (Trang PDF 157–166)

---

<!-- PDF Page 157 -->

#### H Ọ C P H Ầ N

# **<mark>7</mark>** 

### **Định giá và Xác định giá trị của Hợp đồng Hoán đổi Lãi suất và Các Hợp đồng Hoán đổi Khác (*Pricing and Valuation of Interest Rates and Other Swaps*)** 

###### **<mark>MỤC TIÊU HỌC TẬP (*LEARNING OUTCOMES*)</mark>** 

|**_Mức độ thành thạo_**<br>**_Ứng viên cần có khả năng:_**|
|---|
|mô tả cách thức các hợp đồng hoán đổi (*swap contracts*) tương đồng nhưng cũng khác biệt so với một chuỗi các hợp đồng kỳ hạn (*series of forward contracts*)|
|đối chiếu giá trị (*value*) và mức giá (*price*) của các hợp đồng hoán đổi|

##### **GIỚI THIỆU (*INTRODUCTION*)** 

## **<mark>1</mark>** 

Hợp đồng hoán đổi (*swap contracts*) đã được giới thiệu trước đó như một cam kết chắc chắn (*firm commitment*) nhằm trao đổi một chuỗi các dòng tiền trong tương lai, trong đó hợp đồng hoán đổi lãi suất (*interest rate swaps*) – nơi các dòng tiền cố định được trao đổi lấy các khoản thanh toán thả nổi – là loại phổ biến nhất. Các bài học tiếp theo đã đề cập đến việc định giá (*pricing*) và xác định giá trị (*valuation*) của các hợp đồng kỳ hạn (*forward contracts*) và hợp đồng tương lai (*futures contracts*) dọc theo cấu trúc kỳ hạn (*term structure*), vốn tạo thành các cấu phần nền tảng cho các hợp đồng hoán đổi.

Trong bài học này, chúng ta sẽ khám phá cách thức các hợp đồng hoán đổi có liên hệ với các loại cam kết kỳ hạn (*forward commitments*) khác này. Mặc dù các định chế tài chính trung gian thường sử dụng các hợp đồng kỳ hạn lãi suất (*forward rate agreements* – FRAs) hoặc các hợp đồng tương lai lãi suất ngắn hạn để quản lý rủi ro lãi suất, các tổ chức phát hành (*issuers*) và các nhà đầu tư (*investors*) thường ưa chuộng các hợp đồng hoán đổi hơn, vì chúng khớp tốt hơn với các tài sản và nợ phải trả nhạy cảm với lãi suất có dòng tiền định kỳ, chẳng hạn như trái phiếu trả lãi cố định (*fixed-coupon bonds*), các khoản vay lãi suất biến đổi (*variable-rate loans*), hoặc các cam kết trong tương lai đã biết trước. Điều quan trọng đối với những người tham gia thị trường này không chỉ là khả năng khớp các dòng tiền dự kiến trong tương lai bằng cách sử dụng hợp đồng hoán đổi mà còn phải đảm bảo rằng sự thay đổi trong giá trị của chúng nhất quán với các mức phơi nhiễm rủi ro cơ sở hiện có hoặc mong muốn. Các bài học sau đây sẽ so sánh các hợp đồng hoán đổi với các hợp đồng kỳ hạn và đối chiếu giá trị (*value*) cũng như mức giá (*price*) của các hợp đồng hoán đổi.

###### **TỔNG QUAN HỌC PHẦN (*LEARNING MODULE OVERVIEW*)** 

- Hợp đồng hoán đổi (*swap contract*) là một thỏa thuận giữa hai đối tác (*counterparties*) nhằm trao đổi một _chuỗi_ các dòng tiền trong tương lai (*series of future cash flows*), trong khi hợp đồng kỳ hạn (*forward contract*) là một lần trao đổi giá trị _duy nhất_ (*single exchange of value*) vào một ngày sau đó. 


<!-- PDF Page 158 -->

- Hợp đồng hoán đổi lãi suất (*interest rate swaps*) tương tự như hợp đồng kỳ hạn ở chỗ cả hai hợp đồng đều là các cam kết chắc chắn (*firm commitments*) với hồ sơ kết quả thanh toán đối xứng (*symmetric payoff profiles*) và không có tiền mặt nào được trao đổi tại thời điểm khởi tạo (*at inception*), nhưng chúng khác nhau ở chỗ lãi suất hoán đổi cố định (*fixed swap rate*) là không đổi (*constant*), trong khi một chuỗi các hợp đồng kỳ hạn có các mức lãi suất kỳ hạn (*forward rates*) khác nhau tại mỗi kỳ đáo hạn. 

- Một hợp đồng hoán đổi được định giá bằng cách giải tìm lãi suất hoán đổi ngang giá (*par swap rate*), tức là mức lãi suất cố định làm cho giá trị hiện tại của tất cả các dòng tiền thả nổi dự kiến trong tương lai bằng với giá trị hiện tại của tất cả các dòng tiền cố định trong tương lai. 

- Giá trị của một hợp đồng hoán đổi tại thời điểm khởi tạo bằng không (bỏ qua chi phí giao dịch và chi phí tín dụng đối tác). Vào bất kỳ ngày thanh toán (*settlement date*) nào, giá trị của một hợp đồng hoán đổi bằng giá trị thanh toán hiện tại (*current settlement value*) cộng với giá trị hiện tại của tất cả các khoản thanh toán hoán đổi trong tương lai còn lại. 

- Giá trị của một hợp đồng hoán đổi thay đổi khi thời gian trôi qua và lãi suất thay đổi. Ví dụ, sự gia tăng của lãi suất kỳ hạn dự kiến (*expected forward rates*) làm tăng giá trị hiện tại của các khoản thanh toán thả nổi, tạo ra khoản lãi định giá theo thị trường (*mark-to-market gain* – MTM gain) cho bên trả lãi cố định / bên nhận lãi thả nổi (*fixed-rate payer / floating-rate receiver*) và khoản lỗ MTM (*MTM loss*) cho bên nhận lãi cố định / bên trả lãi thả nổi (*fixed-rate receiver / floating-rate payer*). 

###### **TỰ ĐÁNH GIÁ HỌC PHẦN (*LEARNING MODULE SELF-ASSESSMENT*)** 

Những câu hỏi ban đầu này nhằm giúp bạn tự đánh giá mức độ hiểu biết hiện tại của mình về học phần này. 

1. Xác định đặc điểm nào sau đây khớp với loại hợp đồng cam kết kỳ hạn (*forward commitment contract*) nào. 

| Đặc điểm | Hợp đồng cam kết kỳ hạn |
|---|---|
| 1. Liên quan đến các khoản thanh toán định kỳ dựa trên chênh lệch giữa một mức lãi suất cố định được thiết lập riêng cho từng kỳ và lãi suất tham chiếu thị trường (*market reference rate* – MRR) | A. Cả hợp đồng hoán đổi lãi suất (*interest rate swap*) và một chuỗi các hợp đồng kỳ hạn lãi suất (*series of forward rate agreements*) |
| 2. Có hồ sơ kết quả thanh toán đối xứng (*symmetric payoff profile*) và có giá trị bằng không đối với cả hai đối tác tại thời điểm khởi tạo | B. Một chuỗi các hợp đồng kỳ hạn lãi suất (*forward rate agreements* – FRAs) |
| 3. Liên quan đến các khoản thanh toán định kỳ dựa trên chênh lệch giữa một mức lãi suất cố định không đổi (*constant fixed rate*) và lãi suất tham chiếu thị trường (MRR) | C. Hợp đồng hoán đổi lãi suất (*interest rate swap*) |

###### **Lời giải:** 

   **1.** B là đáp án đúng. Một chuỗi các hợp đồng FRA liên quan đến các khoản thanh toán định kỳ dựa trên chênh lệch giữa một mức lãi suất cố định được thiết lập cho từng kỳ và MRR. 

   **2.** A là đáp án đúng. Cả hợp đồng hoán đổi lãi suất và một chuỗi các hợp đồng kỳ hạn lãi suất đều có hồ sơ kết quả thanh toán đối xứng và có giá trị bằng không đối với cả hai đối tác tại thời điểm khởi tạo. 

   **3.** C là đáp án đúng. Hợp đồng hoán đổi lãi suất liên quan đến các khoản thanh toán định kỳ dựa trên chênh lệch giữa một mức lãi suất cố định không đổi và MRR. 

2. Giao dịch nào sau đây sẽ cho phép một nhà quản lý danh mục đầu tư thu nhập cố định (*fixed-income portfolio manager*) thu được lợi nhuận khi lãi suất giảm? 

   - **A.** Mua một trái phiếu lãi suất thả nổi (*floating-rate bond*) 

   - **B.** Tham gia vào một <u>hợp đồng hoán đổi lãi suất nhận cố định, trả thả nổi (*receive-fixed, pay-floating interest rate swap*)</u> 


<!-- PDF Page 159 -->

   - **C.** Tham gia vào một hợp đồng hoán đổi lãi suất trả cố định, nhận thả nổi (*pay-fixed, receive-floating interest rate swap*)

###### **Lời giải:**

B là đáp án đúng. Một nhà quản lý danh mục đầu tư thu nhập cố định muốn thu lợi từ việc lãi suất giảm có thể cân nhắc tham gia vào một hợp đồng hoán đổi lãi suất _nhận_ cố định, _trả_ thả nổi thay vì mua trái phiếu. Các khoản thanh toán lãi suất cố định trở nên có giá trị hơn khi lãi suất giảm. A không đúng vì các khoản thanh toán lãi của trái phiếu lãi suất thả nổi sẽ giảm khi lãi suất giảm, do đó trái phiếu không tăng giá trị. C không đúng vì các khoản thanh toán lãi suất cố định trở nên tốn kém hơn (bất lợi hơn cho bên trả cố định) khi lãi suất giảm.

3. Phát biểu nào sau đây mô tả đúng về một vị thế hợp đồng hoán đổi lãi suất trả cố định, nhận thả nổi (*pay-fixed, receive-floating interest rate swap*)?

   - **A.** Vị thế mua (*long*) một trái phiếu lãi suất thả nổi (*floating-rate note*) được định giá theo MRR và vị thế bán (*short*) một trái phiếu lãi suất cố định (*fixed-rate bond*) có lãi suất coupon bằng với lãi suất hoán đổi cố định (*fixed swap rate*)
   - **B.** Vị thế mua (*long*) một trái phiếu lãi suất cố định có lãi suất coupon bằng với lãi suất hoán đổi cố định và vị thế bán (*short*) một trái phiếu lãi suất thả nổi được định giá theo MRR
   - **C.** Vị thế mua (*long*) một trái phiếu lãi suất thả nổi được định giá theo MRR

###### **Lời giải:**

A là đáp án đúng. Một hợp đồng hoán đổi lãi suất về mặt kinh tế tương đương với một vị thế mua (*long*) và một vị thế bán (*short*) đối với các chứng khoán nợ cơ sở. Trong trường hợp của hợp đồng hoán đổi trả cố định, nhận thả nổi, dòng tiền nhận được phản ánh vị thế mua (*long*). Trong trường hợp này, bên tham gia nhận các khoản thanh toán thả nổi, vì vậy điều này giống như việc mua một trái phiếu lãi suất thả nổi. Phần trả lãi cố định của hợp đồng hoán đổi giống như việc bán một trái phiếu lãi suất cố định và trả các khoản coupon cố định cho người mua trái phiếu. B không đúng vì đáp án này về mặt kinh tế tương đương với việc tham gia vào một hợp đồng hoán đổi nhận cố định, trả thả nổi. C không đúng vì đáp án này không phản ánh vị thế bán (*short position*).

4. Một nhà đầu tư tham gia vào một hợp đồng hoán đổi kỳ hạn 10 năm, trả lãi cố định (*pay-fixed*) với vốn danh nghĩa 100 triệu EUR tại mức lãi suất 1,12% đổi lấy lãi suất MRR đồng EUR kỳ hạn 6 tháng. Giả sử lãi suất MRR đồng EUR kỳ hạn 6 tháng hôm nay được ấn định ở mức 0,25%. Giá trị nào sau đây gần nhất với kết quả tính toán đúng về giá trị thanh toán định kỳ (*periodic settlement value*) của hợp đồng hoán đổi dưới góc độ của nhà đầu tư sau thời gian 6 tháng?

   - **A.** 870.000 EUR
   - **B.** –870.000 EUR
   - **C.** –435.000 EUR

###### **Lời giải:**

C là đáp án đúng. Dưới góc độ của nhà đầu tư (bên trả lãi cố định – *fixed-rate payer*), giá trị thanh toán định kỳ của hợp đồng hoán đổi bằng:

$$\text{Giá trị thanh toán định kỳ} = (\text{MRR} - s_N) \times \text{Vốn danh nghĩa (Notional amount)} \times \text{Kỳ hạn (Period)}$$

$$= -435.000\text{ EUR} = (0,25\% - 1,12\%) \times 100\text{ triệu EUR} \times 0,5\text{ năm}.$$

Vì lãi suất MRR đồng EUR được ấn định thấp hơn lãi suất hoán đổi cố định, bên trả lãi cố định phải thực hiện một khoản thanh toán ròng (*net payment*) cho bên nhận lãi cố định vào cuối kỳ tính lãi. Cả hai đáp án A và B đều bỏ qua độ dài kỳ của hợp đồng hoán đổi (0,5 năm) nên không chính xác. A cũng không chính xác vì dấu bị đảo ngược trong câu trả lời sẽ phản ánh đúng giá trị thanh toán định kỳ của phía đối tác chứ không phải của nhà đầu tư.


<!-- PDF Page 160 -->

## **<mark>2</mark>** 

##### **HỢP ĐỒNG HOÁN ĐỔI SO VỚI HỢP ĐỒNG KỲ HẠN (*SWAPS VS. FORWARDS*)** 

mô tả cách thức các hợp đồng hoán đổi (*swap contracts*) tương đồng nhưng cũng khác biệt so với một chuỗi các hợp đồng kỳ hạn (*series of forward contracts*) 

Hợp đồng hoán đổi (*swap contract*) là một thỏa thuận giữa hai bên nhằm trao đổi một _chuỗi_ các dòng tiền trong tương lai (*series of future cash flows*), trong khi hợp đồng kỳ hạn (*forward contract*) là một thỏa thuận cho một lần trao đổi giá trị _duy nhất_ (*single exchange of value*) vào một ngày sau đó. Mặc dù bài học này tập trung vào các hợp đồng hoán đổi lãi suất (*interest rate swaps*), các nguyên tắc tương tự cũng được áp dụng cho các biến số cơ sở khác nơi một chuỗi các dòng tiền được trao đổi vào một ngày trong tương lai. 

Một bài học trước đây đã chỉ ra cách thức lãi suất kỳ hạn hàm ý (*implied forward rates* – IFR) có thể được suy ra từ lãi suất giao ngay (*spot rates*). Lãi suất kỳ hạn hàm ý cho một kỳ nhất định trong tương lai tương đương với mức lãi suất cố định của hợp đồng kỳ hạn lãi suất (*forward rate agreement* – FRA) cho cùng kỳ đó mà tại đó không tồn tại cơ hội kinh doanh chênh lệch giá phi rủi ro (*no riskless profit opportunities exist*). Dòng tiền đơn lẻ của một hợp đồng FRA tương tự như một hợp đồng hoán đổi một kỳ (*single-period swap*), như được minh họa trong Bảng 1 (*Exhibit 1*). 

###### **Bảng 1: Hồ sơ Kết quả Thanh toán của Hợp đồng Hoán đổi và FRA (*Exhibit 1: Swap and FRA Payoff Profile*)** 

![](assets/Derivatives.pdf-0160-08.png)

<!-- Picture Text: Fixed-Rate<br>Payer<br>MRR × Fixed-Rate<br>Notional × × Notional<br>Period × Period<br>Floating-Rate<br>Payer<br> -->
> **Chú thích hình ảnh:** 
> - **Fixed-Rate Payer:** Bên trả lãi cố định
> - **Floating-Rate Payer:** Bên trả lãi thả nổi
> - Dòng tiền từ Bên trả lãi thả nổi sang Bên trả lãi cố định: $\text{MRR} \times \text{Vốn danh nghĩa (Notional)} \times \text{Kỳ hạn (Period)}$
> - Dòng tiền từ Bên trả lãi cố định sang Bên trả lãi thả nổi: $\text{Lãi suất cố định (Fixed-Rate)} \times \text{Vốn danh nghĩa (Notional)} \times \text{Kỳ hạn (Period)}$

Trong mỗi trường hợp, chênh lệch ròng (*net difference*) giữa mức lãi suất cố định được thỏa thuận tại thời điểm khởi tạo và mức lãi suất tham chiếu thị trường (MRR) được ấn định trong tương lai sẽ được sử dụng làm cơ sở để xác định khoản thanh toán bằng tiền mặt (*cash settlement*) tính trên một khoản vốn gốc danh nghĩa (*notional principal*) nhất định trong một khoảng thời gian cụ thể. Ví dụ, bên trả lãi cố định (*fixed-rate payer*) trong một hợp đồng hoán đổi hoặc FRA sẽ thực hiện một khoản lãi nếu MRR được ấn định ở mức cao hơn lãi suất cố định đã thỏa thuận và sẽ nhận được một khoản thanh toán ròng từ bên trả lãi thả nổi (*floating-rate payer*). Tuy nhiên, như chúng ta đã thấy trong bài học trước, hợp đồng FRA có một lần thanh toán duy nhất diễn ra vào _đầu_ kỳ tính lãi (*beginning of an interest period*), trong khi một hợp đồng hoán đổi tiêu chuẩn có các khoản thanh toán định kỳ diễn ra vào _cuối_ mỗi kỳ tương ứng (*end of each respective period*). 

Những điểm tương đồng khác giữa hợp đồng kỳ hạn lãi suất và hợp đồng hoán đổi lãi suất bao gồm hồ sơ kết quả thanh toán đối xứng (*symmetric payoff profile*) và thực tế là không có dòng tiền nào được trao đổi trả trước (*upfront*). Cả hợp đồng kỳ hạn lãi suất và hợp đồng hoán đổi lãi suất đều hàm chứa rủi ro tín dụng đối tác (*counterparty credit exposure*). 

Vì lãi suất có đặc trưng là cấu trúc kỳ hạn (*term structure*), các mức lãi suất cố định FRA khác nhau thường tồn tại cho các khoảng thời gian đáo hạn khác nhau. Ngược lại, một hợp đồng hoán đổi lãi suất tiêu chuẩn có mức lãi suất cố định _không đổi_ (*constant fixed rate*) trong suốt vòng đời của nó, bao gồm nhiều kỳ. Mối quan hệ này được thể hiện trực quan trong Bảng 2 (*Exhibit 2*) và bằng số liệu trong Ví dụ 1, vốn mở rộng từ một ví dụ về lãi suất giao ngay và lãi suất kỳ hạn trước đó. 


<!-- PDF Page 161 -->

**Bảng 2: Chuỗi các hợp đồng FRA so với Hợp đồng Hoán đổi Lãi suất Tiêu chuẩn (*Exhibit 2: Series of FRAs vs. Standard Interest Rate Swap*)** 

###### **Chuỗi các Hợp đồng Kỳ hạn Lãi suất (tại các Mức lãi suất Cố định Khác nhau) (*Series of Forward Rate Agreements (at Different Fixed Rates)*)** 

![](assets/Derivatives.pdf-0161-05.png)

<!-- Picture Text: Time<br>t  = 0 t  = 1 t  = 2 t  = 3<br>FRA Fixed- FRA Fixed- FRA Fixed- FRA Fixed-<br>Rate Payer Rate Payer Rate Payer Rate Payer<br>Contract<br>Contract<br>Contract<br>FRA Floating- FRA Floating- FRA Floating- FRA Floating-<br>Rate Payer Rate Payer Rate Payer Rate Payer<br> -->
> **Chú thích hình ảnh:** 
> - **Time ($t = 0, t = 1, t = 2, t = 3$):** Thời gian
> - **FRA Fixed-Rate Payer:** Bên trả lãi cố định FRA
> - **FRA Floating-Rate Payer:** Bên trả lãi thả nổi FRA
> - **Contract:** Từng hợp đồng FRA riêng lẻ cho mỗi kỳ với các mức lãi suất cố định khác nhau.

###### **Hợp đồng Hoán đổi Lãi suất Tiêu chuẩn (Tại Một Mức lãi suất Cố định Không đổi) (*Standard Interest Rate Swap (At A Constant Fixed Rate)*)** 

![](assets/Derivatives.pdf-0161-07.png)

<!-- Picture Text: Time<br>t  = 0 t  = 1 t  = 2 t  = 3<br>Swap Fixed- Swap Fixed- Swap Fixed- Swap Fixed-<br>Rate Payer Rate Payer Rate Payer Rate Payer<br>Contract<br>Swap Floating- Swap Floating-  Swap Floating- Swap Floating-<br>Rate Payer Rate Payer Rate Payer Rate Payer<br> -->
> **Chú thích hình ảnh:**
> - **Time ($t = 0, t = 1, t = 2, t = 3$):** Thời gian
> - **Swap Fixed-Rate Payer:** Bên trả lãi cố định của hợp đồng hoán đổi
> - **Swap Floating-Rate Payer:** Bên trả lãi thả nổi của hợp đồng hoán đổi
> - **Contract:** Một hợp đồng hoán đổi duy nhất xuyên suốt các kỳ với cùng một mức lãi suất cố định không đổi.

###### **VÍ DỤ 1 (*EXAMPLE 1*)** 

###### **Hợp đồng Hoán đổi dưới dạng Kết hợp của các Hợp đồng Kỳ hạn (*Swaps as a Combination of Forwards*)** 

Hãy nhớ lại từ bài học trước rằng ba trái phiếu chính phủ trả lãi coupon cố định hàng năm vừa mới phát hành có lãi suất coupon, giá, lợi suất đáo hạn (*yields-to-maturity* – YTM), và lãi suất zero-coupon (hay lãi suất giao ngay – *zero or spot rates*) như sau: 

|**Số năm đến khi đáo hạn**<br>**(*Years to Maturity*)**|**Lãi suất Coupon hàng năm**<br>**(*Annual Coupon*)**|**Giá trị hiện tại – PV**<br>**(trên mỗi 100 mệnh giá FV)**|**Lợi suất đáo hạn**<br>**(*YTM*)**|**Lãi suất Zero**<br>**(*Zero Rates*)**|
|---|---|---|---|---|
|1|1,50%|99,125|2,3960%|2,3960%|
|2|2,50%|98,275|3,4068%|3,4197%|
|3|3,25%|98,000|3,9703%|4,0005%|

Chúng ta giải tìm lãi suất kỳ hạn hàm ý ($\text{IFR}_{A, B-A}$), tức là mức lãi suất tái đầu tư hòa vốn (*break-even reinvestment rate*) cho một kỳ bắt đầu trong tương lai (tại thời điểm $t = A$) giữa lãi suất zero kỳ hạn ngắn hơn ($z_A$) và lãi suất zero kỳ hạn dài hơn ($z_B$) bằng công thức sau: 

$$(1 + z_A)^A \times (1 + \text{IFR}_{A, B-A})^{B-A} = (1 + z_B)^B \tag{1}$$

Lãi suất giao ngay tương ứng tại thời điểm $t = 0$ ($\text{IFR}_{0,1}$) và các mức lãi suất kỳ hạn hàm ý sau một năm ($\text{IFR}_{1,1}$) và sau hai năm ($\text{IFR}_{2,1}$) lần lượt như sau: 


<!-- PDF Page 162 -->

$$\text{IFR}_{0,1} = 2,3960\% = (1,023960) - 1.$$

$$\text{IFR}_{1,1} = 4,4536\% = \frac{(1,034197)^2}{1,02396} - 1.$$

$$\text{IFR}_{2,1} = 5,1719\% = \frac{(1,040005)^3}{(1,034197)^2} - 1.$$

Một cách để tạo ra một cam kết kỳ hạn cho nhiều kỳ với giá trị ban đầu bằng không là sử dụng một chuỗi các hợp đồng kỳ hạn lãi suất (FRAs), trao đổi các dòng tiền dựa trên mức lãi suất kỳ hạn hàm ý tương ứng (tức là lãi suất cố định FRA) cho từng kỳ. Tuy nhiên, mức lãi suất cố định sẽ _thay đổi_ (*vary*) cho mỗi kỳ dựa trên cấu trúc kỳ hạn của lãi suất. Thay vào đó, một hợp đồng hoán đổi lãi suất tiêu chuẩn có đặc trưng là một mức lãi suất cố định _không đổi_ (*constant*) qua nhiều kỳ. Các mức lãi suất này được trình bày cho cả hai phương án dưới đây. 

![](assets/Derivatives.pdf-0162-06.png)

<!-- Picture Text: Time<br>t  = 0 t  = 1 t  = 2 t  = 3<br>FRA fixed FRA fixed FRA fixed FRA fixed<br>rate payer rate payer rate payer rate payer<br>Contract<br>Contract<br>Contract<br>FRA floating FRA floating FRA floating FRA floating<br>rate payer rate payer rate payer rate payer<br>FRA fixed rate: FRA fixed rate: FRA fixed rate:<br>2.396% 4.4536% 5.1719%<br>Time<br>t  = 0 t  = 1 t  = 2 t  = 3<br>Swap fixed Swap fixed Swap fixed Swap fixed<br>rate payer rate payer rate payer rate payer<br>Contract<br>Swap floating Swap floating Swap floating Swap floating<br>rate payer rate payer rate payer rate payer<br>Fixed swap rate: Fixed swap rate: Fixed swap rate:<br>3.9641% 3.9641% 3.9641%<br> -->
> **Chú thích hình ảnh:**
> - **Sơ đồ trên (Chuỗi hợp đồng FRA):** Lãi suất cố định FRA (*FRA fixed rate*) thay đổi qua từng kỳ: Kỳ 1 ($t=1$) là $2,396\%$; Kỳ 2 ($t=2$) là $4,4536\%$; Kỳ 3 ($t=3$) là $5,1719\%$.
> - **Sơ đồ dưới (Hợp đồng hoán đổi):** Lãi suất hoán đổi cố định (*Fixed swap rate*) giữ nguyên không đổi qua cả ba kỳ: Kỳ 1, Kỳ 2, Kỳ 3 đều là $3,9641\%$.

Phương pháp được sử dụng để giải tìm lãi suất hoán đổi đã được giới thiệu trong một bài học về thu nhập cố định trước đó. _Lãi suất ngang giá_ (*par rate* – PMT) đã được chứng minh là mức lãi suất cố định mà tại đó một trái phiếu trả lãi coupon cố định có giá bằng mệnh giá (*par*, hay 100) khi sử dụng một chuỗi các lãi suất zero ($z_i$ cho kỳ $i$) làm thừa số chiết khấu thị trường (*market discount factors*), như sau: 

![](assets/Derivatives.pdf-0162-08.png)

<!-- Formula Text: 100  =    PMT _ (1 + z 1) 1  +   PMT _ (1 + z 2) 2  + ⋯  +  PMT + 100 _ (1 + z N) N . (2) -->
$$100 = \frac{\text{PMT}}{(1 + z_1)^1} + \frac{\text{PMT}}{(1 + z_2)^2} + \cdots + \frac{\text{PMT} + 100}{(1 + z_N)^N} \tag{2}$$

Một hợp đồng hoán đổi lãi suất tiêu chuẩn đại diện cho việc trao đổi các khoản thanh toán cố định (_không_ có khoản thanh toán nợ gốc cuối kỳ) tại một mức lãi suất không đổi để lấy một chuỗi các dòng tiền lãi suất thả nổi được kỳ vọng bằng với các mức lãi suất kỳ hạn hàm ý tương ứng tại thời điểm $t = 0$. Do đó, chúng ta phải điều chỉnh phép tính lãi suất trái phiếu ngang giá trong Phương trình 2 để giải tìm PMT dưới dạng **lãi suất hoán đổi ngang giá (*par swap rate*).** 


<!-- PDF Page 163 -->

###### **Bảng 3: Lãi suất Hoán đổi Ngang giá, Đường cong Lãi suất Giao ngay và Đường cong Lãi suất Kỳ hạn (*Exhibit 3: Par Swap Rate, Spot, and Forward Curve*)** 

![](assets/Derivatives.pdf-0163-04.png)

<!-- Picture Text: Yield (%)<br>7.00%<br>Forward curve<br>6.00%<br>IFR2,1<br>5.00%<br>IFR1,1<br>z 3<br>4.00%<br>Par swap rate ( s 3)<br>IFR0,1 =  z 1 z 2<br>3.00%<br>Spot or zero curve<br>2.00%<br>1.00% Term<br>1 2 3<br> -->
> **Chú thích hình ảnh:**
> - **Trục tung:** Lợi suất (*Yield* – %) từ $1,00\%$ đến $7,00\%$; **Trục hoành:** Kỳ hạn (*Term*) 1, 2, 3.
> - **Forward curve:** Đường cong lãi suất kỳ hạn ($\text{IFR}_{0,1} = z_1$, $\text{IFR}_{1,1}$, $\text{IFR}_{2,1}$).
> - **Spot or zero curve:** Đường cong lãi suất giao ngay hay lãi suất zero ($z_1, z_2, z_3$).
> - **Par swap rate ($s_3$):** Lãi suất hoán đổi ngang giá kỳ hạn 3 năm (đường nằm ngang ở mức $\approx 3,9641\%$).

Lãi suất hoán đổi ngang giá (*par swap rate*) là mức lãi suất cố định làm cân bằng giá trị hiện tại của tất cả các dòng tiền thả nổi dự kiến trong tương lai với giá trị hiện tại của các dòng tiền cố định. 

$$\sum \text{PV}(\text{Các khoản thanh toán thả nổi – Floating payments}) = \sum \text{PV}(\text{Các khoản thanh toán cố định – Fixed payments}), \text{ hay}$$

![](assets/Derivatives.pdf-0163-07.png)

<!-- Formula Text: ∑ i=1 N     IFR _ (1 + z i) i   =  ∑ i=1 N s i _ (1 + z i) i . (3) -->
$$\sum_{i=1}^{N} \frac{\text{IFR}}{(1 + z_i)^i} = \sum_{i=1}^{N} \frac{s_N}{(1 + z_i)^i} \tag{3}$$

Trong ví dụ ba kỳ của chúng ta, chúng ta sử dụng các mức lãi suất kỳ hạn hàm ý, $\text{IFR}$, để giải tìm $s_3$, hay lãi suất hoán đổi kỳ hạn 3 năm: 

![](assets/Derivatives.pdf-0163-09.png)

<!-- Formula Text: IFR 0, 1 _ (1 + z 1)  + IFR 1, 1 _ (1 + z 2) 2  + IFR 2, 1 _ (1 + z 3) 3   = s 3 _ (1 + z 1)  + s 3 _ (1 + z 2) 2  + s 3 _ (1 + z 3) 3 . -->
$$\frac{\text{IFR}_{0,1}}{(1 + z_1)} + \frac{\text{IFR}_{1,1}}{(1 + z_2)^2} + \frac{\text{IFR}_{2,1}}{(1 + z_3)^3} = \frac{s_3}{(1 + z_1)} + \frac{s_3}{(1 + z_2)^2} + \frac{s_3}{(1 + z_3)^3}$$

Thay thế từng cấu phần nền tảng này vào Phương trình 3 để giải tìm $s_3$: 

$$0,111017 = \frac{2,396\%}{1,02396} + \frac{4,4537\%}{(1,034197)^2} + \frac{5,1719\%}{(1,040005)^3} = \frac{s_3}{1,02396} + \frac{s_3}{(1,034197)^2} + \frac{s_3}{(1,040005)^3}$$

$$0,111017 = 2,800545 \times s_3 \implies s_3 = 3,9641\%.$$

Lãi suất hoán đổi kỳ hạn 3 năm ở mức 3,9641% có thể được hiểu là mức lãi suất hòa vốn đa kỳ (*multiperiod breakeven rate*) mà tại đó một nhà đầu tư sẽ bàng quan (*indifferent*) giữa việc: 

- _trả_ lãi suất hoán đổi cố định và _nhận_ các mức lãi suất kỳ hạn tương ứng, hoặc 

- _nhận_ lãi suất hoán đổi cố định và _trả_ các mức lãi suất kỳ hạn tương ứng. 

Vì lý do này, chúng ta có thể coi lãi suất hoán đổi cố định như một tỷ suất hoàn vốn nội bộ (*internal rate of return* – IRR) đối với các mức lãi suất kỳ hạn hàm ý cho đến khi đáo hạn hợp đồng hoán đổi tính tại thời điểm $t = 0$. Bảng 3 cũng chứng minh rằng mặc dù tổng giá trị kết hợp của các hợp đồng kỳ hạn tương đương bằng không tại thời điểm $t = 0$, một số giao dịch trao đổi kỳ hạn riêng lẻ có thể có giá trị hiện tại dương và một số sẽ có giá trị hiện tại âm. Ví dụ, bên nhận lãi cố định (bên trả lãi thả nổi) trong hợp đồng hoán đổi ở Ví dụ 1 sẽ kỳ vọng dòng tiền sau đây sau thời gian một năm: 

- _Nhận_ lãi suất hoán đổi cố định ($s_3$) là 3,9641%. 

- _Trả_ lãi suất thả nổi ban đầu ($\text{IFR}_{0,1}$) là 2,396%. 


<!-- PDF Page 164 -->

- _Nhận_ một khoản thanh toán ròng là 1,5681% ($= 3,9641\% - 2,396\%$) tính trên vốn danh nghĩa cho kỳ đó. 

Những người sử dụng cuối cùng (*end users*) đối với công cụ phái sinh, chẳng hạn như các tổ chức phát hành và các nhà đầu tư, có xu hướng sử dụng hợp đồng hoán đổi thường xuyên hơn so với các hợp đồng kỳ hạn lãi suất riêng lẻ vì một số lý do. Ví dụ, khả năng khớp các dòng tiền của tài sản hoặc nợ phải trả cơ sở cho phép các tổ chức phát hành chuyển đổi hồ sơ phơi nhiễm rủi ro của họ như trong Ví dụ 2. 

###### **VÍ DỤ 2 (*EXAMPLE 2*)** 

###### **Hợp đồng Hoán đổi sang Lãi suất Cố định của Esterr Inc. (*Esterr Inc. Swap to Fixed*)** 

Hãy nhớ lại từ một bài học trước rằng Esterr Inc. có một khoản vay có kỳ hạn lãi suất thả nổi (*floating-rate term loan*) trị giá 250 triệu CAD với lãi suất bằng MRR đồng Canada kỳ hạn 3 tháng cộng 150 điểm cơ bản (*basis points* – bps), còn 3,5 năm nữa là đáo hạn và trả lãi hàng quý. Esterr tham gia vào một hợp đồng hoán đổi lãi suất trị giá 250 triệu CAD để trả lãi suất hoán đổi cố định hàng quý là 2,05% và nhận lãi suất MRR thả nổi kỳ hạn 3 tháng trên vốn gốc danh nghĩa 250 triệu CAD dựa trên các ngày thanh toán khớp với khoản vay có kỳ hạn. Mức phơi nhiễm rủi ro kết hợp của khoản vay và hợp đồng hoán đổi có thể được thể hiện như sau: 

![](assets/Derivatives.pdf-0164-08.png)

<!-- Picture Text: Loan market<br>3-month MRR<br>+ 150 bps p.a.<br>Esterr Inc.<br>Fixed swap 3-month<br>rate 2.05% MRR<br>Financial<br>intermediary<br> -->
> **Chú thích hình ảnh:**
> - **Loan market:** Thị trường cho vay (Esterr Inc. trả lãi suất $\text{MRR 3 tháng} + 150\text{ bps/năm}$).
> - **Esterr Inc.:** Tổ chức phát hành / Bên đi vay.
> - **Financial intermediary:** Định chế tài chính trung gian (Esterr Inc. trả lãi suất hoán đổi cố định $2,05\%$ và nhận $\text{MRR 3 tháng}$).

Theo thỏa thuận hoán đổi này, Esterr có thể cố định chi phí lãi vay (*interest expense*) cho khoản vay có kỳ hạn của mình và tránh được gánh nặng hành chính của việc quản lý nhiều hợp đồng kỳ hạn tại các mức lãi suất kỳ hạn khác nhau. Hãy xem xét các kịch bản dòng tiền sau đây đối với hợp đồng hoán đổi lãi suất và khoản vay có kỳ hạn (giả sử mỗi kỳ tính lãi là 0,25 năm): 

###### **Kịch bản 1 (*Scenario 1*):** 

Lãi suất MRR đồng CAD được ấn định ở mức 3,75%. Với tư cách là bên trả lãi cố định (*fixed-rate payer*), Esterr: 

- trả lãi suất hoán đổi cố định 2,05% và nhận MRR đồng CAD ở mức 3,75%, 

- _nhận_ một khoản thanh toán hoán đổi _ròng_ là 1,70% cho quý đó, và 

- thực hiện khoản thanh toán lãi vay có kỳ hạn là 5,25% ($= 3,75\% + 1,50\%$). 

Chi phí lãi vay của Esterr là 3,55% ($= 5,25\%\text{ trả đi} - 1,70\%\text{ nhận về}$). 

###### **Kịch bản 2 (*Scenario 2*):** 

Lãi suất MRR đồng CAD được ấn định ở mức 1,25%. Với tư cách là bên trả lãi cố định, Esterr: 

- trả lãi suất hoán đổi cố định 2,05% và nhận MRR đồng CAD ở mức 1,25%, 

- _trả_ một khoản thanh toán hoán đổi _ròng_ là 0,80% cho quý đó, và 


<!-- PDF Page 165 -->

- thực hiện khoản thanh toán lãi vay có kỳ hạn là 2,75% ($= 1,25\% + 1,50\%$). 

Chi phí lãi vay của Esterr là 3,55% ($= 2,75\%\text{ trả đi} + 0,80\%\text{ trả đi}$). Bất kể lãi suất MRR đồng CAD được ấn định ở mức nào trong mỗi kỳ, chi phí lãi vay của Esterr cho mỗi kỳ tính lãi hàng quý đều xấp xỉ 2.218.750 CAD ($= 3,55\%$ [bằng lãi suất hoán đổi 2,05% + mức chênh lệch khoản vay 1,50%] $\times 250\text{ triệu CAD} \times 0,25\text{ năm}$). 

Là một công cụ thu nhập cố định có các dòng tiền cố định định kỳ cho đến khi đáo hạn, một hợp đồng hoán đổi lãi suất được kỳ vọng sẽ có các đặc điểm rủi ro và tỷ suất sinh lợi tương tự như một trái phiếu trả lãi coupon cố định có kỳ hạn tương đương. Đặc điểm này làm cho các hợp đồng hoán đổi lãi suất trở thành một lựa chọn thay thế hấp dẫn hơn so với các hợp đồng kỳ hạn lãi suất (FRAs) đối với các nhà đầu tư trong việc quản lý mức phơi nhiễm rủi ro thu nhập cố định. Hãy xem xét bảng so sánh sau đây giữa một vị thế trái phiếu tiền mặt (*cash bond position*) với việc trả hoặc nhận lãi suất hoán đổi cố định: 

**Bảng 4: Sử dụng Hợp đồng Hoán đổi để Quản lý Phơi nhiễm Rủi ro Thu nhập Cố định (*Exhibit 4: Using Swaps to Manage Fixed-Income Exposure*)** 

![](assets/Derivatives.pdf-0165-07.png)

<!-- Picture Text: Fixed-Rate<br>Payer ( Short<br>Bond Position )<br>Fixed Swap<br>MRR<br>Rate<br>Floating-Rate<br>Payer ( Long<br>Bond Position )<br> -->
> **Chú thích hình ảnh:**
> - **Fixed-Rate Payer (Short Bond Position):** Bên trả lãi cố định (tương đương Vị thế bán trái phiếu cố định).
> - **Floating-Rate Payer (Long Bond Position):** Bên trả lãi thả nổi / nhận lãi cố định (tương đương Vị thế mua trái phiếu cố định).
> - Dòng tiền trao đổi gồm **MRR** (Lãi suất tham chiếu thị trường) và **Fixed Swap Rate** (Lãi suất hoán đổi cố định).

|**Công cụ (*Instrument*)**|**Vị thế (*Position*)**|**Lãi suất cao hơn (*Higher interest rates*)**|**Lãi suất thấp hơn (*Lower interest rates*)**|
|---|---|---|---|
|**Trái phiếu tiền mặt (*Cash bond*)**|- Mua trái phiếu cố định (*Long fixed bond*)<br>- Bán trái phiếu lãi suất thả nổi (*Short floating-rate note*)|Lỗ (*Loss*)|Lãi (*Gain*)|
|**Hợp đồng hoán đổi lãi suất (*Interest rate swap*)**|- Nhận cố định (*Receive fixed*)<br>- Trả thả nổi (*Pay floating*)|Lỗ (*Loss*)|Lãi (*Gain*)|
|**Trái phiếu tiền mặt (*Cash bond*)**|- Bán trái phiếu cố định (*Short fixed bond*)<br>- Mua trái phiếu lãi suất thả nổi (*Long floating-rate note*)|Lãi (*Gain*)|Lỗ (*Loss*)|
|**Hợp đồng hoán đổi lãi suất (*Interest rate swap*)**|- Trả cố định (*Pay fixed*)<br>- Nhận thả nổi (*Receive floating*)|Lãi (*Gain*)|Lỗ (*Loss*)|

Mặc dù bài học tiếp theo sẽ khám phá giá trị và mức giá của hợp đồng hoán đổi lãi suất một cách chi tiết hơn, Bảng 4 chứng minh sự tương đồng giữa vị thế mua (bán) trái phiếu và hợp đồng hoán đổi lãi suất nhận (trả) lãi cố định. Nhờ tính thanh khoản cao hơn và hồ sơ phơi nhiễm rủi ro chuẩn (*benchmark exposure profile*) tương tự như các vị thế trái phiếu riêng lẻ, các nhà quản lý danh mục đầu tư thu nhập cố định chủ động (*active fixed-income portfolio managers*) thường sử dụng các hợp đồng hoán đổi thay vì các chứng khoán cơ sở để điều chỉnh mức phơi nhiễm rủi ro lãi suất của họ. Ví dụ, nếu lãi suất được dự báo sẽ giảm, một nhà quản lý danh mục đầu tư có thể chọn nhận lãi cố định trên một hợp đồng hoán đổi thay vì mua các trái phiếu cơ sở để hiện thực hóa khoản lợi nhuận trong môi trường lãi suất thấp hơn. 


<!-- PDF Page 166 -->

Như đã đề cập trước đó, hợp đồng FRA chủ yếu được sử dụng bởi các định chế tài chính trung gian để quản lý các vị thế nhạy cảm với lãi suất của họ theo từng kỳ một (*period-by-period basis*). Các tổ chức phát hành và các nhà đầu tư thường lựa chọn hiệu quả cao hơn của các hợp đồng hoán đổi lãi suất để quản lý mức phơi nhiễm rủi ro lãi suất của mình. Như chúng ta sẽ thấy trong các bài học sau, tính thanh khoản cao hơn của các hợp đồng hoán đổi lãi suất cũng đã dẫn đến việc chúng được sử dụng vừa làm chuẩn mực định giá trái phiếu (*bond pricing benchmark*) vừa làm biến số cơ sở (*underlying variable*) cho các công cụ phái sinh khác. 

###### **BỘ CÂU HỎI (*QUESTION SET*)** 

###### **Hợp đồng Hoán đổi Lãi suất so với Hợp đồng Kỳ hạn (*Interest Rate Swaps vs. Forward Contracts*)** 

1. Xác định các câu trả lời đúng để điền vào chỗ trống: Bên trả lãi cố định (*fixed-rate payer*) trong một hợp đồng hoán đổi hoặc FRA sẽ thực hiện một khoản ______ nếu MRR được ấn định ở mức cao hơn lãi suất cố định đã thỏa thuận và sẽ ______ một khoản thanh toán ròng ______ bên trả lãi thả nổi (*floating-rate payer*). 

###### **Lời giải:** 

Bên trả lãi cố định trong một hợp đồng hoán đổi hoặc FRA sẽ thực hiện một khoản _lãi (gain)_ nếu MRR được ấn định ở mức cao hơn lãi suất cố định đã thỏa thuận và sẽ _nhận (receive)_ một khoản thanh toán ròng _từ (from)_ bên trả lãi thả nổi. 

2. Xác định đặc điểm nào sau đây khớp với loại hợp đồng cam kết kỳ hạn nào. 

| Đặc điểm | Hợp đồng cam kết kỳ hạn |
|---|---|
| 1. Giá của hợp đồng này là lãi suất kỳ hạn hàm ý (*implied forward rate*), hay lãi suất tái đầu tư hòa vốn (*breakeven reinvestment rate*), cho một kỳ bắt đầu trong tương lai. | A. Hợp đồng hoán đổi lãi suất (*Interest rate swap*) |
| 2. Hàm chứa rủi ro tín dụng đối tác (*counterparty credit risk*) | B. Hợp đồng kỳ hạn lãi suất (*Forward rate agreement*) |
| 3. Có một mức lãi suất cố định không đổi mà tại đó giá trị hiện tại của các giao dịch trao đổi dòng tiền cố định so với thả nổi trong tương lai bằng không | C. Cả hợp đồng hoán đổi lãi suất và hợp đồng kỳ hạn lãi suất |

###### **Lời giải:** 

**1.** B là đáp án đúng. Lãi suất tái đầu tư hòa vốn, hay lãi suất kỳ hạn hàm ý, là mức lãi suất cố định FRA không có kinh doanh chênh lệch giá (*no-arbitrage FRA fixed rate*). 

**2.** C là đáp án đúng. Cả hợp đồng hoán đổi lãi suất và hợp đồng kỳ hạn lãi suất đều hàm chứa rủi ro tín dụng đối tác. 

**3.** A là đáp án đúng. Hợp đồng hoán đổi lãi suất có một mức lãi suất cố định không đổi mà tại đó giá trị hiện tại của các giao dịch trao đổi dòng tiền cố định so với thả nổi bằng không. 


---

# Tập 7: Công cụ Phái sinh (*Derivatives*)
## Học phần 7: Định giá và Xác định giá trị của Hợp đồng Hoán đổi Lãi suất và Các Hợp đồng Hoán đổi Khác (*Pricing and Valuation of Interest Rates and Other Swaps*)
### Phần 2/2: Giá trị và Mức giá của Hợp đồng Hoán đổi (Trang PDF 167–178)

---

<!-- PDF Page 167 -->

3. Xác định lợi ích nào sau đây của việc sử dụng hợp đồng hoán đổi thay vì hợp đồng kỳ hạn được áp dụng phù hợp nhất cho đối tượng người sử dụng cuối cùng (*derivative end users*) nào. 

| Lợi ích của hợp đồng hoán đổi | Người sử dụng cuối cùng |
|---|---|
| 1. Hợp đồng hoán đổi cho phép những người sử dụng cuối cùng này khớp các dòng tiền định kỳ của một khoản nợ phải trả cụ thể trên bảng cân đối kế toán để chuyển đổi hồ sơ phơi nhiễm rủi ro lãi suất của họ. | A. Cả tổ chức phát hành (*issuers*) và nhà đầu tư (*investors*) |
| 2. Hợp đồng hoán đổi cho phép những người sử dụng cuối cùng này chủ động điều chỉnh hồ sơ phơi nhiễm rủi ro lãi suất của họ mà không cần mua hoặc bán các chứng khoán cơ sở. | B. Tổ chức phát hành (*Issuers*) |
| 3. Hợp đồng hoán đổi liên quan đến một chuỗi các dòng tiền giúp những người sử dụng cuối cùng này tránh được gánh nặng hành chính của việc tham gia và quản lý nhiều hợp đồng kỳ hạn. | C. Nhà đầu tư (*Investors*) |

###### **Lời giải:** 

**1.** B là đáp án đúng. Hợp đồng hoán đổi cho phép các tổ chức phát hành khớp các dòng tiền định kỳ của một khoản nợ phải trả cụ thể trên bảng cân đối kế toán để chuyển đổi hồ sơ phơi nhiễm rủi ro lãi suất của họ, như đã trình bày trong Ví dụ 2. 

**2.** C là đáp án đúng. Hợp đồng hoán đổi cho phép các nhà đầu tư chủ động điều chỉnh hồ sơ phơi nhiễm rủi ro lãi suất của họ mà không cần mua hoặc bán các chứng khoán cơ sở. 

**3.** A là đáp án đúng. Cả các tổ chức phát hành và các nhà đầu tư đều hưởng lợi từ việc giảm bớt gánh nặng hành chính khi chỉ tham gia một hợp đồng hoán đổi lãi suất cho một chuỗi các dòng tiền thay vì nhiều hợp đồng kỳ hạn riêng lẻ. 

4. Xác định phát biểu sau đây là đúng hay sai, và giải thích câu trả lời của bạn: Lãi suất tham chiếu thị trường (*market reference rate* – MRR) là tỷ suất hoàn vốn nội bộ (*internal rate of return* – IRR) đối với các mức lãi suất kỳ hạn hàm ý trong suốt vòng đời của một hợp đồng hoán đổi lãi suất. 

###### **Lời giải:** 

Sai. Lãi suất hoán đổi cố định (*fixed swap rate*) mới là tỷ suất hoàn vốn nội bộ đối với các mức lãi suất kỳ hạn hàm ý trong suốt vòng đời của một hợp đồng hoán đổi lãi suất. 

5. Giải thích cách thức một nhà quản lý danh mục đầu tư thu nhập cố định chủ động (*active fixed-income portfolio manager*) có thể sử dụng hợp đồng hoán đổi lãi suất thay vì các trái phiếu cơ sở để hiện thực hóa khoản lãi trong môi trường lãi suất thấp hơn, và giải thích lý do cho câu trả lời của bạn. 

###### **Lời giải:** 

Một nhà quản lý có thể chọn vị thế nhận lãi cố định, trả lãi thả nổi (*receive fixed, pay floating*) trong một hợp đồng hoán đổi lãi suất, với luồng dòng tiền cố định tương tự như việc sở hữu một trái phiếu trả lãi coupon cố định. Nếu lãi suất được dự báo sẽ giảm, nhà quản lý sẽ thực hiện được một khoản lãi định giá theo thị trường (*MTM gain*) trong môi trường lãi suất thấp hơn. 

#### **GIÁ TRỊ VÀ MỨC GIÁ CỦA HỢP ĐỒNG HOÁN ĐỔI (*SWAP VALUES AND PRICES*)** 

# **<mark>3</mark>** 

đối chiếu giá trị (*value*) và mức giá (*price*) của các hợp đồng hoán đổi 

Trong bài học trước, chúng ta đã chỉ ra rằng mức giá của một hợp đồng hoán đổi (*swap price*, hay lãi suất hoán đổi ngang giá – *par swap rate*) là một mức lãi suất cố định định kỳ làm cân bằng giá trị hiện tại của tất cả các dòng tiền thả nổi dự kiến trong tương lai với giá trị hiện tại của các dòng tiền cố định. Lãi suất hoán đổi ($s_N$ cho $N$ kỳ) tương đương với một 


<!-- PDF Page 168 -->

mức lãi suất kỳ hạn, $F_0(T)$, thỏa mãn điều kiện không có kinh doanh chênh lệch giá (*no-arbitrage condition*). Tương tự như các hợp đồng kỳ hạn khác, giá trị hợp đồng ban đầu (bỏ qua chi phí giao dịch và chi phí tín dụng đối tác) bằng không ($V_0(T) = 0$). 

Trái ngược với các cam kết kỳ hạn khác vốn chỉ liên quan đến một lần thanh toán _duy nhất_ (*single settlement*) khi đáo hạn, một hợp đồng hoán đổi liên quan đến một _chuỗi_ các khoản thanh toán định kỳ (*series of periodic settlements*) cùng với một lần thanh toán cuối cùng khi hợp đồng đáo hạn. Hãy nhớ lại từ bài học trước rằng giá trị của một hợp đồng kỳ hạn khi đáo hạn dưới góc độ của bên mua kỳ hạn (*long forward*) là $V_T(T) = S_T - F_0(T)$, trong đó $S_T$ là giá giao ngay khi đáo hạn và $F_0(T)$ là giá kỳ hạn. Đối với một hợp đồng hoán đổi có các lần trao đổi định kỳ, lãi suất MRR hiện hành đóng vai trò là mức giá “giao ngay” (*“spot” price*) và lãi suất hoán đổi cố định, $s_N$, là mức giá kỳ hạn (*forward price*). Phát biểu lại kết quả này cho bên trả lãi cố định (*fixed-rate payer*) trong một hợp đồng hoán đổi, giá trị thanh toán định kỳ (*periodic settlement value*) là: 

$$\text{Giá trị thanh toán định kỳ (Periodic settlement value)} = (\text{MRR} - s_N) \times \text{Vốn danh nghĩa (Notional amount)} \times \text{Kỳ hạn (Period)} \tag{4}$$

Giá trị của một hợp đồng hoán đổi vào bất kỳ ngày thanh toán nào bằng giá trị thanh toán hiện tại trong Phương trình 4 _cộng với_ giá trị hiện tại của tất cả các khoản thanh toán hoán đổi trong tương lai còn lại. Mặc dù thông lệ thị trường hoán đổi có sự khác nhau, cho mục đích của bài học này, chúng ta sẽ giả định rằng MRR được ấn định vào đầu mỗi kỳ tính lãi, với cùng tần suất kỳ hạn (*periodicity*) và quy ước đếm ngày (*day count convention*) như lãi suất hoán đổi. Khoản chênh lệch giữa lãi cố định và lãi thả nổi được trao đổi vào cuối mỗi kỳ. 

###### **VÍ DỤ 3 (*EXAMPLE 3*)** 

##### **Giá trị và Mức giá Hợp đồng Hoán đổi của Esterr Inc. (*Esterr Inc. Swap Value and Price*)** 

Esterr đã tham gia vào một hợp đồng hoán đổi lãi suất kỳ hạn 3,5 năm trị giá 250 triệu CAD, theo đó công ty trả lãi suất hoán đổi cố định hàng quý là 2,05% và nhận lãi suất MRR đồng CAD kỳ hạn 3 tháng. _Mức giá_ hoán đổi cố định (*fixed swap price*) 2,05% do Esterr trả giữ nguyên không đổi trong suốt vòng đời của hợp đồng. Trong khi lãi suất MRR đồng CAD kỳ hạn 3 tháng đầu tiên _đã được biết_ tại thời điểm $t = 0$, 13 lần ấn định MRR còn lại vẫn _chưa được biết_ nhưng được _kỳ vọng_ sẽ bằng với các mức lãi suất kỳ hạn hàm ý (*implied forward rates* – IFRs) tương ứng cho mỗi kỳ cho đến khi đáo hạn. Một bài học trước đã chỉ ra cách thức các mức IFR được suy ra từ lãi suất zero, sau đó được sử dụng để giải tìm lãi suất hoán đổi cố định bằng cách đặt giá trị hiện tại của các khoản thanh toán cố định bằng với giá trị hiện tại của các khoản thanh toán thả nổi. 

_Giá trị_ (*value*) hợp đồng hoán đổi của Esterr sẽ thay đổi khi thời gian trôi qua và lãi suất thay đổi. Trước tiên, chúng ta xem xét sự trôi qua của thời gian mà không có sự thay đổi nào đối với lãi suất kỳ vọng. Nghĩa là, MRR được ấn định trong mỗi kỳ dựa đúng theo các mức lãi suất kỳ hạn hàm ý tại thời điểm khởi tạo giao dịch. Giả sử các mức lãi suất kỳ hạn hàm ý sau đây được áp dụng cho hợp đồng hoán đổi của Esterr tại thời điểm $t = 0$: 

|**Kỳ (*Period*)**|**Lãi suất kỳ hạn hàm ý (*IFR*)**|**Mức lãi suất (*Rate*)**|
|---|---|---|
|1|$\text{IFR}_{0,3m}$|0,50%|
|2|$\text{IFR}_{3m,3m}$|0,74%|
|3|$\text{IFR}_{6m,3m}$|0,98%|
|4|$\text{IFR}_{9m,3m}$|1,22%|
|5|$\text{IFR}_{12m,3m}$|1,46%|
|6|$\text{IFR}_{15m,3m}$|1,70%|
|7|$\text{IFR}_{18m,3m}$|1,94%|
|8|$\text{IFR}_{21m,3m}$|2,18%|
|9|$\text{IFR}_{24m,3m}$|2,43%|
|10|$\text{IFR}_{27m,3m}$|2,67%|
|11|$\text{IFR}_{30m,3m}$|2,91%|
|12|$\text{IFR}_{33m,3m}$|3,15%|


<!-- PDF Page 169 -->

|**Kỳ (*Period*)**|**Lãi suất kỳ hạn hàm ý (*IFR*)**|**Mức lãi suất (*Rate*)**|
|---|---|---|
|13|$\text{IFR}_{36m,3m}$|3,39%|
|14|$\text{IFR}_{39m,3m}$|3,78%|

Dựa trên các mức lãi suất kỳ hạn này, Esterr kỳ vọng sẽ _thực hiện (chi trả)_ một khoản thanh toán hoán đổi ròng mỗi quý cho đến hết kỳ thứ bảy—vì $(\text{MRR} - s_N) = (1,94\% - 2,05\%) < 0$—và _nhận_ một khoản thanh toán hoán đổi ròng hàng quý bắt đầu từ kỳ thứ tám, nơi $(\text{MRR} - s_N) = (2,18\% - 2,05\%) > 0$. Sử dụng Phương trình 4 (trong nguyên bản ghi Equation 1), hãy xem xét các giá trị thanh toán định kỳ cho hai kỳ đầu tiên dưới góc độ của Esterr là bên trả lãi cố định: 

- **Kỳ 1:** $-968.750\text{ CAD} = (0,5\% - 2,05\%) \times 250\text{ triệu CAD} \times 0,25$. 

- **Kỳ 2:** $-818.750\text{ CAD} = (0,74\% - 2,05\%) \times 250\text{ triệu CAD} \times 0,25$. 

_Giá trị_ định giá theo thị trường (*MTM value*) của hợp đồng hoán đổi dưới góc độ của Esterr ngay sau lần thanh toán định kỳ thứ hai là bao nhiêu nếu lãi suất kỳ hạn không thay đổi? Lưu ý rằng _mức giá_ của hợp đồng hoán đổi (lãi suất hoán đổi cố định 2,05%) đã được thiết lập tại thời điểm khởi tạo để làm cân bằng giá trị hiện tại của các khoản thanh toán cố định so với thả nổi. 

![](assets/Derivatives.pdf-0169-08.png)

<!-- Picture Text: Rate<br>4.00%<br>Forward curve<br>3.50%<br>3.00%<br>2.50%<br>2.00% Swap  rate<br>1.50%<br>1.00%<br>0.50%<br>0.00%<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14<br>Quarterly period<br> -->
> **Chú thích hình ảnh:**
> - **Trục tung:** Lãi suất (*Rate*) từ $0,00\%$ đến $4,00\%$; **Trục hoành:** Kỳ hàng quý (*Quarterly period*) từ 1 đến 14.
> - **Forward curve:** Đường cong lãi suất kỳ hạn dốc lên.
> - **Swap rate:** Lãi suất hoán đổi cố định ban đầu ($2,05\%$).

Khi chúng ta tiến về phía trước theo thời gian mà _không_ có sự thay đổi nào đối với kỳ vọng lãi suất, giá trị hiện tại của các khoản thanh toán thả nổi còn lại sẽ tăng lên cao hơn giá trị hiện tại của các khoản thanh toán cố định ở mức 2,05%, bởi vì Esterr đã thực hiện chi trả khoản thanh toán ròng trong hai kỳ đầu tiên. 

![](assets/Derivatives.pdf-0169-10.png)

<!-- Picture Text: Rate<br>4.00%<br>Forward curve<br>3.50%<br>3.00%<br>2.50% New swap rate (3y)<br>2.00% Original swap rate<br>1.50%<br>1.00%<br>0.50%<br>0.00%<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14<br> -->
> **Chú thích hình ảnh:**
> - **New swap rate (3y):** Lãi suất hoán đổi mới cho 3 năm còn lại (từ kỳ 3 đến kỳ 14), nằm cao hơn **Original swap rate** (Lãi suất hoán đổi ban đầu $2,05\%$).

###### **Kỳ hàng quý (*Quarterly period*)** 

Như sơ đồ cho thấy, khi thời gian trôi qua, Esterr thực hiện được một khoản lãi định giá theo thị trường (*MTM gain*) trên hợp đồng hoán đổi, bởi vì: 


<!-- PDF Page 170 -->

$$\sum \text{PV}(\text{Các khoản thanh toán thả nổi nhận được – Floating payments received}) > \sum \text{PV}(\text{Các khoản thanh toán cố định phải trả – Fixed payments paid}).$$

Lưu ý rằng kết quả này phụ thuộc vào mức độ tương đối của các mức IFR và hình dạng của đường cong lãi suất kỳ hạn (*forward curve*), mà trong trường hợp này là dốc lên (*upward sloping*). 

Nếu thay vào đó chúng ta chỉ xem xét những thay đổi về lãi suất, dưới góc độ của Esterr là bên trả lãi cố định (và là bên nhận lãi thả nổi), chúng ta có thể chỉ ra các điều kiện mà theo đó Esterr có khoản lãi hoặc lỗ MTM trên hợp đồng hoán đổi: 

- Esterr thực hiện được một khoản _lãi_ MTM (*MTM gain*) trên hợp đồng hoán đổi với tư cách là bên trả lãi cố định nếu: 

  $$\sum \text{PV}(\text{Các khoản thanh toán thả nổi nhận được}) > \sum \text{PV}(\text{Các khoản thanh toán cố định phải trả}).$$

- Esterr thực hiện một khoản _lỗ_ MTM (*MTM loss*) trên hợp đồng hoán đổi với tư cách là bên trả lãi cố định nếu: 

  $$\sum \text{PV}(\text{Các khoản thanh toán thả nổi nhận được}) < \sum \text{PV}(\text{Các khoản thanh toán cố định phải trả}).$$

Sự gia tăng của các mức lãi suất kỳ hạn dự kiến sau khi khởi tạo sẽ làm tăng giá trị hiện tại của các khoản thanh toán thả nổi, trong khi lãi suất hoán đổi cố định vẫn giữ nguyên như cũ. Chúng ta thể hiện tác động của một sự thay đổi tức thời trong lãi suất ngay sau khi khởi tạo giao dịch trong sơ đồ dưới đây: 

![](assets/Derivatives.pdf-0170-11.png)

<!-- Picture Text: Rate New forward curve<br>4.00%<br>Original forward curve<br>3.50%<br>3.00% New swap rate<br>2.50%<br>2.00% Original swap rate<br>1.50%<br>1.00%<br>0.50%<br>0.00%<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14<br>Quarterly period<br> -->
> **Chú thích hình ảnh:**
> - **New forward curve:** Đường cong lãi suất kỳ hạn mới (dịch chuyển lên trên **Original forward curve** – Đường cong lãi suất kỳ hạn ban đầu).
> - **New swap rate:** Lãi suất hoán đổi mới (cao hơn **Original swap rate** – Lãi suất hoán đổi ban đầu).

Đường cong lãi suất kỳ hạn mới trong sơ đồ này bao gồm các mức IFR cao hơn. Nếu bây giờ chúng ta giải tìm một mức lãi suất hoán đổi cố định bằng cách sử dụng các mức IFR cao hơn này thông qua việc đặt các dòng tiền thả nổi và cố định bằng nhau, thì lãi suất hoán đổi mới sẽ nằm trên mức lãi suất hoán đổi ban đầu. Tuy nhiên, vì Esterr đã khóa chặt (*locked in*) các khoản thanh toán cố định trong tương lai ở mức lãi suất hoán đổi ban đầu _thấp hơn_ trong khi lại nhận được các mức MRR dự kiến trong tương lai cao hơn, nên hợp đồng hoán đổi có giá trị MTM dương đối với Esterr. 

Một cách diễn giải khác về hợp đồng hoán đổi lãi suất là bên trả lãi cố định (bên nhận lãi thả nổi) đang giữ vị thế _mua (long)_ một trái phiếu lãi suất thả nổi (*floating-rate note* – FRN) được định giá theo MRR và vị thế _bán (short)_ một trái phiếu lãi suất cố định có lãi suất coupon bằng với lãi suất hoán đổi cố định. Lưu ý rằng sự kết hợp của vị thế mua và bán trái phiếu làm cho cả giá mua và giá bán của hai trái phiếu tại thời điểm khởi tạo cũng như việc hoàn trả vốn gốc khi đáo hạn triệt tiêu lẫn nhau, và chỉ còn lại các khoản thanh toán coupon cố định so với biến đổi. Ví dụ sau đây cho thấy sự thay đổi trong giá trị của một hợp đồng hoán đổi lãi suất tương tự như sự thay đổi của một chứng khoán thu nhập cố định như thế nào bằng cách sử dụng một ví dụ về hợp đồng hoán đổi của nhà đầu tư trước đó. 

###### **VÍ DỤ 4 (*EXAMPLE 4*)** 

##### **Fyleton Investments** 

Trong một ví dụ ở bài học trước, Fyleton Investments đã tham gia vào một hợp đồng hoán đổi lãi suất kỳ hạn 5 năm, nhận lãi cố định (*receive-fixed*) trị giá 200 triệu GBP nhằm làm tăng thời lượng (*duration*) cho danh mục đầu tư thu nhập cố định của mình. Giả sử trong trường hợp này, Fyleton nhận lãi suất hoán đổi cố định 


<!-- PDF Page 171 -->

ở mức 2,38% trên cơ sở nửa năm một lần (*semiannual basis*) đổi lấy lãi suất MRR đồng GBP kỳ hạn 6 tháng. Giả sử thêm rằng lãi suất MRR đồng GBP kỳ hạn 6 tháng ban đầu được ấn định ở mức 0,71% và, giống như trong trường hợp của Esterr, đường cong lãi suất kỳ hạn MRR có hình dạng dốc lên (*upward sloping*). Giá trị hợp đồng hoán đổi của Fyleton sẽ thay đổi như thế nào khi thời gian trôi qua và lãi suất thay đổi? 

Trước tiên, hãy xem xét sự trôi qua của thời gian mà không có sự thay đổi nào về lãi suất. Giá trị thanh toán hợp đồng hoán đổi kỳ đầu tiên (sau 6 tháng) dưới góc độ của Fyleton là bên nhận lãi cố định (*fixed-rate receiver*) là: 

$$1.670.000\text{ GBP} = (2,38\% - 0,71\%) \times 200\text{ triệu GBP} \times 0,5.$$

Giá trị MTM dưới góc độ của Fyleton ngay sau lần thanh toán đầu tiên là bao nhiêu nếu các mức lãi suất kỳ hạn hàm ý vẫn giữ nguyên như tại thời điểm khởi tạo giao dịch? 

Với tư cách là bên _nhận_ lãi cố định, Fyleton sẽ thực hiện một khoản _lỗ_ MTM (*MTM loss*) trên hợp đồng hoán đổi, bởi vì: 

$$\sum \text{PV}(\text{Các khoản thanh toán thả nổi phải trả – Floating payments paid}) > \sum \text{PV}(\text{Các khoản thanh toán cố định nhận được – Fixed payments received}).$$

Thứ hai, hãy xem xét sự thay đổi trong lãi suất kỳ hạn. Sự _sụt giảm_ của các mức lãi suất kỳ hạn dự kiến ngay sau khi khởi tạo giao dịch sẽ _làm giảm_ giá trị hiện tại của các khoản thanh toán thả nổi, trong khi lãi suất hoán đổi cố định vẫn giữ nguyên. Fyleton sẽ thực hiện được một khoản lãi MTM (*MTM gain*) với tư cách là bên nhận lãi cố định, bởi vì: 

$$\sum \text{PV}(\text{Các khoản thanh toán cố định nhận được}) > \sum \text{PV}(\text{Các khoản thanh toán thả nổi phải trả}).$$

Khoản lãi MTM này được thể hiện qua kích thước khác nhau của các vùng được tô bóng dưới mức lãi suất hoán đổi ban đầu khi sử dụng đường cong lãi suất kỳ hạn mới trong sơ đồ dưới đây. 

![](assets/Derivatives.pdf-0171-12.png)

<!-- Picture Text: Rate<br>4.00% PV(Fixed)  >  PV(Floating)<br>Original forward curve<br>3.50%<br>3.00% New forward curve<br>2.50%<br>Original swap rate<br>2.00%<br>New swap rate<br>1.50%<br>1.00%<br>0.50%<br>0.00% Time<br> -->
> **Chú thích hình ảnh:**
> - **PV(Fixed) > PV(Floating):** Giá trị hiện tại của dòng tiền cố định lớn hơn Giá trị hiện tại của dòng tiền thả nổi.
> - **Original forward curve:** Đường cong lãi suất kỳ hạn ban đầu; **New forward curve:** Đường cong lãi suất kỳ hạn mới (dịch chuyển xuống dưới).
> - **Original swap rate:** Lãi suất hoán đổi ban đầu (cao hơn **New swap rate** – Lãi suất hoán đổi mới).

Hãy lưu ý sự tương đồng giữa hồ sơ phơi nhiễm rủi ro của hợp đồng hoán đổi nhận lãi cố định (*receive-fixed swap*) và hồ sơ của một vị thế mua trái phiếu tiền mặt lãi suất cố định (*long cash fixed-rate bond position*). Trong trường hợp thứ nhất, chúng ta kỳ vọng một trái phiếu ngang giá lãi suất cố định sẽ được định giá ở mức _chiết khấu_ (*discount*) khi thời gian trôi qua nếu lãi suất tăng lên theo đường cong lãi suất kỳ hạn dốc lên, trong khi một trái phiếu FRN được định giá theo MRR sẽ vẫn giữ ở mức ngang giá (*par*). Trong trường hợp thứ hai, sự sụt giảm của lãi suất kỳ hạn hàm ý (hay sự dịch chuyển xuống dưới của đường cong lãi suất kỳ hạn) sẽ làm cho một trái phiếu ngang giá lãi suất cố định được định giá ở mức _thặng dư_ (*premium*), trong khi giá trái phiếu FRN sẽ không thay đổi. Chúng ta sẽ khám phá cách thức những thay đổi của cấu trúc kỳ hạn và đường cong lợi suất ảnh hưởng đến giá trị hợp đồng hoán đổi và giá trái phiếu một cách chi tiết hơn ở phần sau của chương trình học. 


<!-- PDF Page 172 -->

###### **BỘ CÂU HỎI (*QUESTION SET*)** 

##### **Mức giá và Giá trị của Hợp đồng Hoán đổi (*Swap Prices and Values*)** 

1. Xác định các câu trả lời đúng để điền vào chỗ trống: Sự gia tăng của các mức lãi suất kỳ hạn dự kiến sau khi khởi tạo sẽ ______ giá trị hiện tại của các khoản thanh toán thả nổi, làm cho bên nhận lãi cố định (*fixed-rate receiver*) thực hiện một sự ______ trong giá trị MTM của hợp đồng hoán đổi. 

###### **Lời giải:** 

Sự gia tăng của các mức lãi suất kỳ hạn dự kiến sau khi khởi tạo sẽ _làm tăng (increase)_ giá trị hiện tại của các khoản thanh toán thả nổi, làm cho bên nhận lãi cố định thực hiện một sự _sụt giảm (decline)_ trong giá trị MTM của hợp đồng hoán đổi. 

2. Xác định phát biểu sau đây là đúng hay sai, và giải thích câu trả lời của bạn: Lãi suất cố định trong một hợp đồng hoán đổi lãi suất được định giá sao cho giá trị hiện tại của các khoản thanh toán thả nổi (dựa trên các mức lãi suất kỳ hạn hàm ý tương ứng cho mỗi kỳ) bằng với giá trị hiện tại của các khoản thanh toán cố định tại thời điểm $t = 0$. 

###### **Lời giải:** 

Phát biểu này là đúng. Lãi suất cố định trong một hợp đồng hoán đổi lãi suất có thể được giải tìm bằng cách đặt giá trị hiện tại của các khoản thanh toán thả nổi bằng với giá trị hiện tại của các khoản thanh toán cố định. Chúng ta sử dụng lãi suất zero (*zero rates*) để suy ra lãi suất kỳ hạn hàm ý (*implied forward rates* – IFRs), hay lãi suất tái đầu tư hòa vốn, giữa một mức lãi suất zero ngắn hạn hơn và một mức lãi suất zero dài hạn hơn. Các mức IFR này đại diện cho các mức lãi suất thả nổi tương ứng được kỳ vọng sẽ áp dụng cho từng kỳ tương lai tính tại thời điểm $t = 0$. 

3. Xác định phát biểu nào sau đây gắn liền với vị thế nào trong một hợp đồng hoán đổi lãi suất. 

| Phát biểu | Vị thế trong hợp đồng hoán đổi lãi suất |
|---|---|
| 1. Thiết lập một tập hợp các dòng tiền tương lai ròng chắc chắn (*certain net future cash flows*) trên một hợp đồng hoán đổi tại thời điểm khởi tạo | A. Bên trả lãi cố định (Bên nhận lãi thả nổi) (*Fixed-rate payer / Floating-rate receiver*) |
| 2. Thực hiện được một khoản lãi MTM trên hợp đồng hoán đổi nếu các khoản thanh toán lãi suất thả nổi dự kiến trong tương lai tăng lên | B. Bên nhận lãi cố định (Bên trả lãi thả nổi) (*Fixed-rate receiver / Floating-rate payer*) |
| 3. Một nhà đầu tư có thể làm tăng thời lượng (*duration*) của danh mục đầu tư bằng cách tham gia vị thế này trong một hợp đồng hoán đổi | C. Không phải bên trả lãi cố định cũng không phải bên nhận lãi cố định (*Neither a fixed-rate payer nor a fixed-rate receiver*) |

###### **Lời giải:** 

**1.** C là đáp án đúng. Một hợp đồng hoán đổi thiết lập một tập hợp các dòng tiền tương lai cố định _chắc chắn_ (*certain*) được đem trao đổi lấy một tập hợp các dòng tiền tương lai thả nổi _dự kiến_ (_không chắc chắn_ – *uncertain*). Do đó, _không_ bên nào (cả bên trả lãi cố định lẫn bên nhận lãi cố định) biết trước được các dòng tiền tương lai _ròng_ (*net future cash flows*) của hợp đồng hoán đổi tại thời điểm khởi tạo. 

**2.** A là đáp án đúng. Bên trả lãi cố định thực hiện được một khoản lãi MTM trên hợp đồng hoán đổi nếu các khoản thanh toán lãi suất thả nổi dự kiến trong tương lai tăng lên. 

**3.** B là đáp án đúng. Bên nhận lãi cố định có thể làm tăng thời lượng (*duration*) của danh mục đầu tư bằng cách tham gia vị thế này trong hợp đồng hoán đổi, bởi vì việc nhận lãi cố định tương tự như một vị thế mua trái phiếu (*long bond position*). 


<!-- PDF Page 173 -->

4. Xác định các câu trả lời đúng để điền vào chỗ trống: Giá trị của một hợp đồng hoán đổi vào bất kỳ ngày thanh toán nào bằng giá trị thanh toán ______ cộng với giá trị hiện tại của tất cả các khoản thanh toán hoán đổi ______ còn lại. 

###### **Lời giải:** 

Giá trị của một hợp đồng hoán đổi vào bất kỳ ngày thanh toán nào bằng giá trị thanh toán _hiện tại (current)_ cộng với giá trị hiện tại của tất cả các khoản thanh toán hoán đổi _tương lai (future)_ còn lại. 

5. Mô tả cách thức một nhà đầu tư có thể sử dụng hợp đồng hoán đổi lãi suất để làm giảm thời lượng (*duration*) của một danh mục đầu tư thu nhập cố định, và giải thích lý do cho câu trả lời của bạn. 

###### **Lời giải:** 

Một hợp đồng hoán đổi trả lãi cố định (*pay-fixed swap*) tương tự như một vị thế bán trái phiếu (*short bond position*) giúp làm giảm thời lượng (*duration*), bởi vì bên trả lãi cố định (bên nhận lãi thả nổi) về thực chất đang giữ vị thế mua (*long*) một trái phiếu lãi suất thả nổi được định giá theo MRR và giữ vị thế bán (*short*) một trái phiếu lãi suất cố định có lãi suất coupon bằng với lãi suất hoán đổi cố định. 


<!-- PDF Page 174 -->

## **BÀI TẬP THỰC HÀNH (*PRACTICE PROBLEMS*)** 

### **Thông tin sau đây liên quan đến các câu hỏi từ 1 đến 6** 

Ace Limited là một định chế tài chính trung gian hoạt động tích cực trên thị trường kỳ hạn và hoán đổi với các khách hàng là tổ chức phát hành và nhà đầu tư. Bạn được yêu cầu tư vấn về một số tình huống của khách hàng để xác định hướng hành động tốt nhất. 

**1.** Xác định phát biểu nào sau đây gắn liền với vị thế hoán đổi nào của đối tác giao dịch với Ace. 

| Phát biểu | Vị thế hoán đổi của đối tác |
|---|---|
| 1. Đối tác của Ace giữ vị thế hoán đổi này sẽ thực hiện được một khoản lãi MTM nếu các mức lãi suất kỳ hạn hàm ý tăng lên. | A. Hợp đồng hoán đổi lãi suất nhận cố định (*A receive-fixed interest rate swap*) |
| 2. Đối tác của Ace giữ vị thế hoán đổi này sẽ phải thực hiện một khoản thanh toán ròng nếu lãi suất tham chiếu thị trường (MRR) ban đầu được ấn định cao hơn lãi suất hoán đổi cố định. | B. Hợp đồng hoán đổi lãi suất trả cố định (*A pay-fixed interest rate swap*) |
| 3. Đối tác của Ace giữ vị thế này sẽ có giá trị hợp đồng hoán đổi ban đầu (bỏ qua chi phí giao dịch và chi phí tín dụng đối tác) bằng không. | C. Cả hợp đồng hoán đổi lãi suất nhận cố định và trả cố định (*Both a receive-fixed and a pay-fixed interest rate swap*) |

**2.** Khách hàng của Ace là một công ty quản lý tài sản có một phần đáng kể danh mục đầu tư trái phiếu lãi suất cố định sắp đáo hạn. Khách hàng của Ace dự định tái đầu tư số tiền thu được vào các trái phiếu có kỳ hạn 5 năm. Phương án nào sau đây mô tả hướng hành động _tốt nhất_ trên thị trường công cụ phái sinh để khách hàng của Ace giải quyết rủi ro tái đầu tư trái phiếu (*bond reinvestment risk*) của mình? 

   - **A.** Khách hàng của Ace nên cân nhắc việc _nhận_ lãi cố định trong một hợp đồng hoán đổi kỳ hạn 5 năm bắt đầu trong tương lai (*forward-starting swap*) được thanh toán bằng tiền mặt, bắt đầu và thanh toán sau 3 tháng nữa nhằm giải quyết tốt nhất rủi ro tái đầu tư trái phiếu của mình. 

   - **B.** Khách hàng của Ace nên cân nhắc việc _trả_ lãi cố định trong một hợp đồng hoán đổi kỳ hạn 5 năm bắt đầu trong tương lai được thanh toán bằng tiền mặt, bắt đầu sau 3 tháng nữa nhằm giải quyết tốt nhất rủi ro tái đầu tư trái phiếu của mình. 

   - **C.** Khách hàng của Ace nên cân nhắc việc tham gia vào một _chuỗi_ các hợp đồng kỳ hạn lãi suất (FRAs) từ hôm nay cho đến 5 năm sau, theo đó họ trả lãi suất cố định và nhận lãi suất thả nổi mỗi kỳ kết thúc sau 5 năm để giải quyết rủi ro tái đầu tư trái phiếu của mình. 

**3.** Ace tham gia vào một hợp đồng hoán đổi lãi suất đồng GBP kỳ hạn 10 năm với một khách hàng, trong đó Ace nhận lãi suất MRR đồng GBP kỳ hạn 6 tháng ban đầu là 1,75% và trả lãi suất hoán đổi cố định đồng GBP là 3,10% cho kỳ nửa năm đầu tiên. Phát biểu nào sau đây mô tả đúng nhất giá trị của hợp đồng hoán đổi dưới góc độ của Ace vào thời điểm 3 tháng sau khi khởi tạo giao dịch? 

   - **A.** Ace có một khoản _lỗ_ MTM trên hợp đồng hoán đổi, bởi vì công ty nợ đối tác một khoản thanh toán ròng bằng 1,35% nhân với vốn danh nghĩa và kỳ hạn. 


<!-- PDF Page 175 -->

   - **B.** Ace có một khoản _lãi_ MTM trên hợp đồng hoán đổi, bởi vì một khi công ty thực hiện khoản thanh toán ròng đầu tiên đã biết cho đối tác của mình, phần còn lại của các dòng tiền cố định so với thả nổi ròng trong tương lai phải có giá trị hiện tại dương dưới góc độ của Ace. 

   - **C.** Mặc dù giá trị hiện tại của các dòng tiền cố định và tương lai đã được thiết lập bằng không thông qua việc giải tìm lãi suất hoán đổi tại thời điểm khởi tạo, chúng ta không có đủ thông tin để xác định liệu hợp đồng hoán đổi hiện đang có giá trị dương hay âm dưới góc độ của Ace sau khi khởi tạo. 

**4.** Ace tham gia vào một hợp đồng hoán đổi lãi suất đồng GBP kỳ hạn 10 năm với một khách hàng, trong đó Ace nhận lãi suất MRR đồng GBP kỳ hạn 6 tháng ban đầu là 1,75% và trả lãi suất hoán đổi cố định đồng GBP là 3,10% cho kỳ nửa năm đầu tiên. Sáu tháng sau, Ace và đối tác của mình thanh toán khoản tiền hoán đổi đầu tiên, và không có sự thay đổi nào xảy ra đối với kỳ vọng lãi suất trong tương lai. Phát biểu nào sau đây mô tả đúng nhất giá trị của hợp đồng hoán đổi dưới góc độ của Ace? 

   - **A.** Ace có một khoản lãi MTM trên hợp đồng hoán đổi, bởi vì một khi công ty thực hiện khoản thanh toán ròng đầu tiên đã biết cho đối tác của mình, phần còn lại của các dòng tiền cố định so với thả nổi ròng trong tương lai phải có giá trị hiện tại dương dưới góc độ của Ace. 

   - **B.** Ace có một khoản lỗ MTM trên hợp đồng hoán đổi, bởi vì một khi công ty nhận được khoản thanh toán đầu tiên đã biết từ đối tác của mình, phần còn lại của các dòng tiền cố định so với thả nổi ròng trong tương lai phải có giá trị hiện tại âm dưới góc độ của Ace. 

   - **C.** Mặc dù giá trị hiện tại của các dòng tiền cố định và tương lai đã được thiết lập bằng không thông qua việc giải tìm lãi suất hoán đổi tại thời điểm khởi tạo, chúng ta không có đủ thông tin để xác định liệu hợp đồng hoán đổi hiện đang có giá trị dương hay âm dưới góc độ của Ace sau khi khởi tạo. 

**5.** Tại thời điểm $t = 0$, Ace quan sát thấy các mức lãi suất zero sau đây qua ba kỳ: 

|**Kỳ (*Periods*)**|**Lãi suất Zero (*Zero Rates*)**|
|---|---|
|1|2,2727%|
|2|3,0323%|
|3|3,6355%|

Phương án nào sau đây mô tả đúng nhất cách thức Ace tính ra lãi suất hoán đổi ngang giá ba kỳ ($s_3$)? 

- **A.** Vì lãi suất hoán đổi ngang giá đại diện cho mức lãi suất cố định mà tại đó giá trị hiện tại của các dòng tiền cố định và tương lai bằng nhau, chúng ta chiết khấu từng mức lãi suất zero về hiện tại bằng cách sử dụng các mức lãi suất zero và giải tìm $s_3$ để có được 2,961%. 

- **B.** Vì lãi suất hoán đổi ngang giá đại diện cho mức lãi suất cố định mà tại đó giá trị hiện tại của các dòng tiền cố định và tương lai bằng nhau, trước tiên chúng ta giải tìm lãi suất kỳ hạn hàm ý cho mỗi kỳ bằng cách sử dụng các mức lãi suất zero, sau đó chiết khấu từng mức lãi suất kỳ hạn hàm ý về hiện tại bằng cách sử dụng các mức lãi suất zero, và giải tìm $s_3$ để có được 3,605%. 


<!-- PDF Page 176 -->

   - **C.** Vì lãi suất hoán đổi ngang giá đại diện cho mức lãi suất cố định mà tại đó giá trị hiện tại của các dòng tiền cố định và tương lai bằng nhau, trước tiên chúng ta giải tìm lãi suất kỳ hạn hàm ý cho mỗi kỳ bằng cách sử dụng các mức lãi suất zero, sau đó chiết khấu từng mức lãi suất zero về hiện tại bằng cách sử dụng các mức lãi suất kỳ hạn hàm ý, và giải tìm $s_3$ để có được 3,009%. 

**6.** Khách hàng tổ chức phát hành của Ace đã hoán đổi khoản nợ lãi suất cố định đang lưu hành của mình sang lãi suất thả nổi để khớp với các dòng tiền từ danh mục tài sản vốn tạo ra tỷ suất sinh lợi dựa trên MRR. Phát biểu nào sau đây mô tả _đúng nhất_ mức phơi nhiễm rủi ro tín dụng MTM (*MTM credit exposure*) của Ace đối với tổ chức phát hành thay đổi như thế nào nếu lãi suất tăng lên ngay sau khi khởi tạo giao dịch? 

   - **A.** Vì khách hàng nhận lãi cố định và trả lãi thả nổi trên hợp đồng hoán đổi, khách hàng phải đối mặt với một khoản lỗ MTM trên giao dịch khi lãi suất tăng lên, làm _tăng_ mức phơi nhiễm rủi ro MTM của Ace đối với khách hàng. 

   - **B.** Vì khách hàng nhận lãi cố định và trả lãi thả nổi trên hợp đồng hoán đổi, khách hàng có được một khoản lãi MTM trên giao dịch khi lãi suất tăng lên, làm _giảm_ mức phơi nhiễm rủi ro MTM của Ace đối với khách hàng. 

   - **C.** Vì giá trị của hợp đồng hoán đổi bằng khoản thanh toán hiện tại cộng với các khoản thanh toán dự kiến trong tương lai, chúng ta không có đủ thông tin để xác định liệu mức phơi nhiễm rủi ro MTM của Ace đối với khách hàng tăng hay giảm. 


<!-- PDF Page 177 -->

## **LỜI GIẢI (*SOLUTIONS*)** 

1. 1. B là đáp án đúng. Một đối tác tham gia hợp đồng hoán đổi trả lãi cố định (*pay-fixed swap*) sẽ thực hiện được một khoản lãi MTM nếu các mức lãi suất kỳ hạn hàm ý tăng lên. 

   2. A là đáp án đúng. Một đối tác tham gia hợp đồng hoán đổi nhận lãi cố định (*receive-fixed swap*) sẽ phải thực hiện một khoản thanh toán ròng nếu lãi suất tham chiếu thị trường (MRR) ban đầu được ấn định cao hơn lãi suất hoán đổi cố định. 

   3. C là đáp án đúng. Cả đối tác tham gia hợp đồng hoán đổi nhận lãi cố định và trả lãi cố định đều sẽ đứng trước giá trị hợp đồng hoán đổi ban đầu (bỏ qua chi phí giao dịch và chi phí tín dụng đối tác) bằng không. 

2. A là đáp án đúng. Khách hàng của Ace nên cân nhắc việc _nhận_ lãi cố định trên một hợp đồng hoán đổi kỳ hạn 5 năm. Một hợp đồng hoán đổi nhận lãi cố định có hồ sơ rủi ro và tỷ suất sinh lợi tương tự như một vị thế _mua_ trái phiếu lãi suất cố định (*long fixed-rate bond position*). Do đó, khách hàng của Ace sẽ kỳ vọng có được một khoản lãi hoặc lỗ MTM tương tự trên vị thế hoán đổi giống như thể họ đã mua một trái phiếu kỳ hạn 5 năm tại thời điểm khởi tạo. 

3. C là đáp án đúng. Tại thời điểm $t = 0$, giá trị hiện tại của các dòng tiền cố định và tương lai đã được thiết lập bằng không thông qua việc giải tìm lãi suất hoán đổi tại thời điểm khởi tạo. Mặc dù giá trị thanh toán hiện tại đã được biết, chúng ta không thể xác định liệu hợp đồng hoán đổi có giá trị dương hay âm dưới góc độ của Ace vào thời điểm 3 tháng sau nếu không có thêm thông tin—cụ thể là mức lãi suất kỳ hạn tương lai hiện hành. 

4. A là đáp án đúng. Ace thực hiện chi trả khoản thanh toán ròng đầu tiên bởi vì khoản thanh toán lãi suất cố định lớn hơn mức lãi suất thả nổi nhận được. Với giả định không có sự thay đổi nào trong lãi suất kỳ hạn tương lai, điều này hàm ý rằng các dòng tiền ròng còn lại phải có giá trị hiện tại dương đối với Ace. B không đúng vì câu trả lời này phát biểu ngược lại so với câu trả lời trước. C không đúng vì chúng ta đã có thông tin về kỳ vọng lãi suất kỳ hạn. 

5. B là đáp án đúng. Vì các dòng tiền thả nổi dự kiến trên hợp đồng hoán đổi là các mức lãi suất kỳ hạn hàm ý (IFRs), trước tiên chúng ta sử dụng lãi suất zero để giải tìm các mức IFR bằng Phương trình 1: 

$$(1 + z_A)^A \times (1 + \text{IFR}_{A, B-A})^{B-A} = (1 + z_B)^B.$$

Chúng ta có thể giải tìm các mức lãi suất này lần lượt là $\text{IFR}_{0,1} = 2,2727\%$, $\text{IFR}_{1,1} = 3,7975\%$, và $\text{IFR}_{2,1} = 4,8525\%$. Sau đó, chúng ta thay thế các mức IFR tương ứng được chiết khấu bằng lãi suất zero vào phương trình sau đây để giải tìm $s_3$: 

![](assets/Derivatives.pdf-0177-13.png)

<!-- Formula Text: IF R 0, 1 _ (1 + z 1)  + IF R 1, 1 _ (1 + z 2) 2  + IF R 2, 1 _ (1 + z 3) 3   = s 3 _ (1 + z 1)  + s 3 _ (1 + z 2) 2  + s 3 _ (1 + z 3) 3 . -->
$$\frac{\text{IFR}_{0,1}}{(1 + z_1)} + \frac{\text{IFR}_{1,1}}{(1 + z_2)^2} + \frac{\text{IFR}_{2,1}}{(1 + z_3)^3} = \frac{s_3}{(1 + z_1)} + \frac{s_3}{(1 + z_2)^2} + \frac{s_3}{(1 + z_3)^3}$$

Giải vế trái của phương trình, chúng ta có được: 

![](assets/Derivatives.pdf-0177-15.png)

<!-- Formula Text: 0.10159  =   2.2727% _ 1.022727  +   3.7975% _ (1.030323) 2  +   4.8525% _ (1.036355) 3 =   2.2727% _ 1.022727  +   3.7975% _ (1.030323) 2  +   4.8525% _ (1.036355) 3 -->
$$0,10159 = \frac{2,2727\%}{1,022727} + \frac{3,7975\%}{(1,030323)^2} + \frac{4,8525\%}{(1,036355)^3}$$

Giải vế phải, chúng ta có được: 

![](assets/Derivatives.pdf-0177-17.png)

<!-- Formula Text: 2.81819 s 3  =  [ 1 _ 1.022727  + 1 _ (1.030323) 2  + 1 _ (1.036355) 3 ] × s 3. -->
$$2,81819 s_3 = \left[ \frac{1}{1,022727} + \frac{1}{(1,030323)^2} + \frac{1}{(1,036355)^3} \right] \times s_3$$

$$s_3 = 3,605\% = 0,10159 \div 2,81819.$$

A không đúng vì phương án này chiết khấu lãi suất zero chứ không phải các mức IFR về hiện tại bằng lãi suất zero, trong khi C chiết khấu sai các mức lãi suất zero bằng các mức IFR tương ứng. 

6. A là đáp án đúng. Vì khách hàng nhận lãi cố định và trả lãi thả nổi trên hợp đồng hoán đổi, trong môi trường lãi suất tăng lên, $\sum \text{PV}(\text{Các khoản thanh toán thả nổi}) > \sum \text{PV}(\text{Các khoản thanh toán cố định})$, và do đó khách hàng sẽ 


<!-- PDF Page 178 -->

nợ nhiều hơn trong các khoản thanh toán lãi suất thả nổi tương lai so với số tiền họ sẽ nhận được trong các khoản thanh toán lãi suất cố định, dẫn đến một khoản lỗ MTM cho khách hàng và làm _tăng_ mức phơi nhiễm rủi ro tín dụng MTM của Ace (vì hợp đồng có giá trị dương đối với Ace). 
