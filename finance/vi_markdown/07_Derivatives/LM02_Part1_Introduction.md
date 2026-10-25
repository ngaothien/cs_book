# Tập 7: Công cụ Phái sinh (*Derivatives*)
## Học phần 2: Đặc điểm và Công cụ của Cam kết Kỳ hạn và Quyền đòi hỏi Có điều kiện (*Forward Commitment and Contingent Claim Features and Instruments*)
### Phần 1/2: Giới thiệu (Trang PDF 31–45)

---

<!-- PDF Page 31 -->

# H Ọ C P H Ầ N **<mark>2</mark>** 

### **Đặc điểm và Công cụ của Cam kết Kỳ hạn và Quyền đòi hỏi Có điều kiện (*Forward Commitment and Contingent Claim Features and Instruments*)** 

##### **<mark>MỤC TIÊU HỌC TẬP (*LEARNING OUTCOMES*)</mark>** 

|**_Mức độ thành thạo_**|**_Ứng viên cần có khả năng:_**|
|---|---|
||định nghĩa hợp đồng kỳ hạn (*forward contracts*), hợp đồng tương lai (*futures contracts*), hợp đồng hoán đổi (*swaps*), quyền chọn (*options* – quyền chọn mua *calls* và quyền chọn bán *puts*), và công cụ phái sinh tín dụng (*credit derivatives*) cũng như so sánh các đặc điểm cơ bản của chúng|
||xác định giá trị khi đáo hạn (*value at expiration*) và lợi nhuận (*profit*) từ một vị thế mua (*long position*) hoặc vị thế bán (*short position*) đối với quyền chọn mua (*call option*) hoặc quyền chọn bán (*put option*)|
||đối chiếu giữa các cam kết kỳ hạn (*forward commitments*) với các quyền đòi hỏi có điều kiện (*contingent claims*)|

#### **GIỚI THIỆU (*INTRODUCTION*)** 

## **<mark>1</mark>** 

Một bài học trước đây đã xác định công cụ phái sinh là một công cụ tài chính có hiệu quả hoạt động bắt nguồn từ một tài sản cơ sở (*underlying asset*), chỉ số (*index*), hoặc biến số tài chính khác, chẳng hạn như độ biến động giá cổ phiếu (*equity price volatility*). Các loại công cụ phái sinh chính bao gồm cam kết chắc chắn (*firm commitment* / *forward commitment*), trong đó một khoản tiền xác định trước được thỏa thuận sẽ trao đổi giữa các đối tác khi thanh toán, và quyền đòi hỏi có điều kiện (*contingent claim*), trong đó một trong các đối tác sẽ quyết định liệu giao dịch có được thanh toán hay không và vào thời điểm nào. Các bài học tiếp theo sẽ định nghĩa và so sánh các đặc điểm cơ bản của cam kết kỳ hạn và quyền đòi hỏi có điều kiện, đồng thời giải thích cách tính giá trị của chúng khi đáo hạn.

###### **TỔNG QUAN HỌC PHẦN (*LEARNING MODULE OVERVIEW*)** 

- Hợp đồng kỳ hạn (*forwards*), hợp đồng tương lai (*futures*), và hợp đồng hoán đổi (*swaps*) đại diện cho các cam kết chắc chắn (*firm commitments*), hay các hợp đồng phái sinh yêu cầu các đối tác phải trao đổi một tài sản cơ sở trong tương lai dựa trên một mức giá đã thỏa thuận.

- Hợp đồng kỳ hạn là một công cụ phái sinh phi tập trung (*over-the-counter* – OTC) linh hoạt, trong khi hợp đồng tương lai được tiêu chuẩn hóa và giao dịch trên sở giao dịch với việc thanh toán hàng ngày đối với các khoản lãi và lỗ của hợp đồng.

- Hợp đồng hoán đổi là một cam kết chắc chắn nhằm trao đổi một chuỗi các dòng tiền trong tương lai. Hợp đồng hoán đổi lãi suất (*interest rate swaps*) là loại phổ biến nhất và liên quan đến việc trao đổi các khoản thanh toán lãi cố định lấy các khoản thanh toán lãi thả nổi.

Viện CFA (*CFA Institute*) xin gửi lời cảm ơn tới Tiến sĩ Don Chance, CFA, vì những đóng góp của ông cho phần này, bao gồm tài liệu được trích xuất từ nội dung xuất hiện trong bài đọc _Derivative Markets and Instruments_ thuộc chương trình giảng dạy CFA® năm 2022.

<!-- PDF Page 32 -->

- Hợp đồng quyền chọn (*option contracts*) là các quyền đòi hỏi có điều kiện (*contingent claims*), trong đó một trong các đối tác quyết định liệu một giao dịch có được thanh toán hay không và khi nào sẽ thanh toán. Người mua quyền chọn trả một khoản phí quyền chọn (*premium*) cho người bán để có quyền giao dịch tài sản cơ sở trong tương lai tại một mức giá thực hiện (*exercise price*) đã thỏa thuận trước.

- Cấu trúc giá trị nhận được khi đáo hạn (*payoff*) và lợi nhuận (*profit*) của hợp đồng quyền chọn là phi tuyến tính (*non-linear*) khi giá tài sản cơ sở thay đổi, trái ngược với các cam kết chắc chắn như hợp đồng kỳ hạn, hợp đồng tương lai, và hợp đồng hoán đổi, vốn có tính tuyến tính (*linear*) theo các biến động giá của tài sản cơ sở.

- Những người tham gia thị trường thường tạo ra các mức độ tiếp xúc rủi ro tương tự nhau đối với một tài sản cơ sở bằng cách sử dụng các cam kết chắc chắn và các quyền đòi hỏi có điều kiện, mặc dù các loại công cụ phái sinh này có cấu trúc giá trị nhận được (*payoff*) và lợi nhuận (*profit*) khác nhau.

###### **TỰ ĐÁNH GIÁ HỌC PHẦN (*LEARNING MODULE SELF-ASSESSMENT*)** 

Những câu hỏi ban đầu này nhằm giúp bạn đánh giá mức độ hiểu biết hiện tại của mình về học phần này.

1. Phát biểu nào sau đây mô tả đúng sự khác biệt giữa hợp đồng kỳ hạn (*forward contract*) và hợp đồng tương lai (*futures contract*)?

   - **A.** Hợp đồng kỳ hạn ấn định một mức giá đã thỏa thuận cho người mua và người bán, trong khi hợp đồng tương lai thì không.

   - **B.** Hợp đồng kỳ hạn ấn định một ngày giao dịch đã thỏa thuận để người bán giao tài sản cơ sở cho người mua, trong khi hợp đồng tương lai thì không.

   - **C.** Hợp đồng kỳ hạn không yêu cầu thanh toán lãi và lỗ hàng ngày, trong khi hợp đồng tương lai có yêu cầu này.

###### **Lời giải:** 

C là đáp án đúng. Hợp đồng tương lai yêu cầu thanh toán hàng ngày (*daily settlement*) thông qua quy trình định giá theo thị trường (*mark-to-market* – MTM) của trung tâm bù trừ thuộc sở giao dịch. Hợp đồng kỳ hạn được thanh toán vào ngày đáo hạn của chúng, mặc dù hai bên tham gia hợp đồng có thể tùy chỉnh các thủ tục thanh toán thay thế khác. A không đúng vì cả hợp đồng kỳ hạn và hợp đồng tương lai đều ấn định một mức giá đã thỏa thuận cho một giao dịch trong tương lai. B không đúng vì cả hợp đồng kỳ hạn và hợp đồng tương lai đều bao gồm một ngày đáo hạn khi tài sản cơ sở sẽ được trao đổi.

2. Xác định ví dụ nào phù hợp với từng cam kết chắc chắn sau đây:

|**Bên tham gia**|**Đặc điểm mô tả**|
|---|---|
|A. Bên mua hợp đồng tương lai (*Futures contract purchaser*)|1. Đồng ý thực hiện một lần trao đổi duy nhất trong tương lai tại một mức giá thỏa thuận trước theo một hợp đồng OTC|
|B. Bên bán hợp đồng kỳ hạn (*Forward contract seller*)|2. Đồng ý thực hiện một lần trao đổi duy nhất trong tương lai dựa trên các điều khoản được tiêu chuẩn hóa do sở giao dịch quy định|
|C. Bên trả lãi suất cố định trong hợp đồng hoán đổi lãi suất (*Fixed-rate payer on an interest rate swap*)|3. Đồng ý thực hiện một chuỗi các lần trao đổi giữa các khoản thanh toán lãi cố định và lãi thả nổi|

###### **Lời giải:** 

1. B là đáp án đúng. Bên bán hợp đồng kỳ hạn đồng ý thực hiện một lần trao đổi duy nhất trong tương lai tại một mức giá thỏa thuận trước theo một hợp đồng OTC.

2. A là đáp án đúng. Bên mua hợp đồng tương lai đồng ý thực hiện một lần trao đổi duy nhất trong tương lai dựa trên các điều khoản được tiêu chuẩn hóa do một sở giao dịch quy định.

<!-- PDF Page 33 -->

3. C là đáp án đúng. Bên trả lãi suất cố định trong một hợp đồng hoán đổi lãi suất đồng ý thực hiện một chuỗi các lần trao đổi giữa các khoản thanh toán lãi cố định và lãi thả nổi.

3. Xác định ví dụ nào phù hợp với từng quyền đòi hỏi có điều kiện sau đây:

|**Bên tham gia**|**Đặc điểm mô tả**|
|---|---|
|A. Bên mua quyền chọn bán (*Put option purchaser*)|1. Tìm cách thu lợi từ sự gia tăng trong giá của tài sản cơ sở|
|B. Bên mua quyền chọn mua (*Call option purchaser*)|2. Để cho quyền chọn hết hạn vào ngày đáo hạn nếu giá tài sản cơ sở cao hơn giá thực hiện (*exercise price*)|
|C. Cả bên mua quyền chọn bán và bên mua quyền chọn mua|3. Trả một khoản phí quyền chọn (*option premium*) cho người bán quyền chọn khi hợp đồng được thỏa thuận|

###### **Lời giải:** 

1. B là đáp án đúng. Bên mua quyền chọn mua tìm cách thu lợi từ sự gia tăng trong giá của tài sản cơ sở.

2. A là đáp án đúng. Bên mua quyền chọn bán sẽ để quyền chọn hết hạn vào ngày đáo hạn mà không thực hiện quyền nếu giá tài sản cơ sở cao hơn giá thực hiện.

3. C là đáp án đúng. Cả bên mua quyền chọn bán và bên mua quyền chọn mua đều sẽ trả một khoản phí quyền chọn cho người bán quyền chọn khi hợp đồng quyền chọn được ký kết.

4. Một quyền chọn để mua một chứng khoán cơ sở tại mức giá thực hiện là 45 USD sau ba tháng được giao dịch với mức phí quyền chọn là 6 USD. Sau ba tháng, tài sản cơ sở được giao dịch ở mức 50 USD. Câu trả lời nào sau đây mô tả đúng vị thế lãi/lỗ (*profit/loss position*) của người mua và người bán quyền chọn?

   - **A.** Người mua quyền chọn thu được khoản lợi nhuận 5 USD, và người bán quyền chọn chịu khoản lỗ 5 USD.

   - **B.** Người mua quyền chọn chịu khoản lỗ 1 USD, và người bán quyền chọn thu được khoản lợi nhuận 1 USD.

   - **C.** Người mua quyền chọn thu được khoản lợi nhuận 5 USD, và người bán quyền chọn thu được 0 USD.

###### **Lời giải:** 

B là đáp án đúng. Vị thế của người mua quyền chọn tạo ra một giá trị nhận được khi đáo hạn (*payoff*) là 5 USD, bằng $\max(0, 50 - 45)$. Người mua quyền chọn đã trả 6 USD để mua vị thế quyền chọn này, và dòng tiền chi ra này lớn hơn phần giá trị nhận được dương. Do đó, tổng lợi nhuận của người mua quyền chọn là một khoản lỗ 1 USD (tức là $5 - 6 = -1$). Đối với người bán quyền chọn, vị thế quyền chọn tạo ra một dòng tiền thanh toán âm là $-5$ USD, bằng $-\max(0, 50 - 45)$. Tuy nhiên, người bán quyền chọn đã nhận được phí quyền chọn là 6 USD, vì vậy tổng lợi nhuận là 1 USD (tức là $6 - 5 = 1$). A không đúng vì số tiền 5 USD chỉ phản ánh giá trị nhận được khi đáo hạn (*payoff*) của quyền chọn chứ chưa phải là lợi nhuận và thua lỗ có tính đến phí quyền chọn. C không đúng vì lợi nhuận của người mua chỉ nêu sai thành giá trị nhận được của vị thế quyền chọn chứ không phải lợi nhuận ròng, còn lợi nhuận của người bán sẽ chỉ bằng 0 nếu tài sản cơ sở giao dịch ở mức 51 chứ không phải 50.

5. Người mua quyền chọn bán (*put option buyer*) kiếm được lợi nhuận dương trong điều kiện nào sau đây?

   - **A.** Giá của tài sản cơ sở khi quyền chọn đáo hạn thấp hơn giá thực hiện của quyền chọn.

   - **B.** Giá của tài sản cơ sở khi quyền chọn đáo hạn lớn hơn giá thực hiện của quyền chọn.

<!-- PDF Page 34 -->

   - **C.** Giá của tài sản cơ sở thấp hơn mức giá thực hiện của quyền chọn trừ đi phí quyền chọn.

###### **Lời giải:** 

C là đáp án đúng. Để người mua quyền chọn bán kiếm được lợi nhuận dương, giá tài sản cơ sở phải thấp hơn đủ sâu so với giá thực hiện của quyền chọn bán sao cho (1) quyền chọn bán có thể được thực hiện với giá trị nhận được (*payoff*) dương và (2) giá trị nhận được dương đó phải lớn hơn khoản phí quyền chọn đã trả. Do đó, điều này chỉ có thể xảy ra nếu giá tài sản cơ sở giảm xuống thấp hơn mức giá thực hiện trừ đi phí quyền chọn ($S_T < X - p_0$). A không đúng vì điều kiện này chỉ hàm ý một giá trị nhận được dương trên quyền chọn nhưng vẫn bao gồm cả những mức giá mà tại đó giá trị nhận được không lớn hơn phí quyền chọn. B không đúng vì khi đó quyền chọn bán sẽ ở trạng thái kiệt giá (*out of the money*) và tạo ra giá trị nhận được bằng không.

6. Những vị thế nào sau đây trên cùng một tài sản cơ sở sẽ hưởng lợi từ các biến động giá ngược chiều nhau của tài sản cơ sở đó?

   - **A.** Vị thế mua hợp đồng kỳ hạn (*long forward contract*), vị thế bán quyền chọn bán (*short put option*)

   - **B.** Vị thế bán hợp đồng kỳ hạn (*short forward contract*), vị thế mua quyền chọn bán (*long put option*)

   - **C.** Vị thế bán hợp đồng kỳ hạn (*short forward contract*), vị thế bán quyền chọn bán (*short put option*)

###### **Lời giải:** 

C là đáp án đúng. Vị thế bán hợp đồng kỳ hạn (*short forward*) hưởng lợi khi giá tài sản cơ sở giảm, trong khi vị thế bán quyền chọn bán (*short put*) chỉ hưởng lợi khi giá tài sản cơ sở tăng (hoặc giữ nguyên trên giá thực hiện). A không đúng vì cả vị thế mua hợp đồng kỳ hạn và vị thế bán quyền chọn bán đều hưởng lợi khi giá tài sản cơ sở tăng. B không đúng vì cả vị thế bán hợp đồng kỳ hạn và vị thế mua quyền chọn bán đều hưởng lợi khi giá tài sản cơ sở giảm.

## **<mark>2</mark>** 

#### **HỢP ĐỒNG KỲ HẠN, HỢP ĐỒNG TƯƠNG LAI VÀ HỢP ĐỒNG HOÁN ĐỔI (*FORWARDS, FUTURES, AND SWAPS*)** 

định nghĩa hợp đồng kỳ hạn, hợp đồng tương lai, hợp đồng hoán đổi, quyền chọn (quyền chọn mua và quyền chọn bán), và công cụ phái sinh tín dụng cũng như so sánh các đặc điểm cơ bản của chúng

Hợp đồng kỳ hạn (*forwards*), hợp đồng tương lai (*futures*), và hợp đồng hoán đổi (*swaps*) là những hợp đồng phái sinh phổ biến nhất đại diện cho một cam kết chắc chắn (*firm commitment*). Cam kết chắc chắn này là nghĩa vụ của cả hai đối tác phải thực hiện theo các điều khoản của hợp đồng phái sinh. Các đặc điểm chung chính của loại công cụ phái sinh này bao gồm:

- Một quy mô hợp đồng cụ thể (*specific contract size*)

- Một tài sản cơ sở cụ thể (*specific underlying*)

- Một hoặc nhiều lần trao đổi dòng tiền hoặc tài sản cơ sở vào một ngày hoặc các ngày cụ thể trong tương lai

- (Các) lần trao đổi dựa trên một mức giá đã thỏa thuận trước (*pre-agreed price*)

Mặc dù có những điểm tương đồng, hợp đồng kỳ hạn, hợp đồng tương lai, và hợp đồng hoán đổi đều có những đặc điểm khác nhau, và đó là chủ đề của bài học này.

Hợp đồng kỳ hạn (*forward contract*) là một công cụ phái sinh phi tập trung (*over-the-counter* – OTC) trong đó hai đối tác thỏa thuận rằng một đối tác (người mua – *buyer*) sẽ mua một tài sản cơ sở từ đối tác kia (người bán – *seller*) trong tương lai tại một mức giá cố định đã thỏa thuận trước. Như đã lưu ý trước đó, các công cụ phái sinh OTC mang lại sự linh hoạt và khả năng tùy chỉnh cao hơn so với các công cụ phái sinh giao dịch trên sở giao dịch (ETD), nhưng thường cũng liên quan đến nhiều rủi ro đối tác hơn. Hợp đồng kỳ hạn

<!-- PDF Page 35 -->

có lợi thế đối với những người sử dụng cuối cùng của công cụ phái sinh đang tìm cách phòng vệ một mức độ tiếp xúc rủi ro cơ sở hiện có hoặc được dự báo dựa trên các điều khoản cụ thể. Ví dụ, một nhà nhập khẩu có thể tham gia vào một hợp đồng kỳ hạn để mua số ngoại tệ cần thiết nhằm đáp ứng các điều khoản thương mại của một hợp đồng giao nhận hàng hóa trong tương lai. Hợp đồng kỳ hạn linh hoạt hơn về quy mô, chi tiết tài sản cơ sở, kỳ hạn, và/hoặc các điều khoản tín dụng so với một hợp đồng ETD tương tự. Người mua hợp đồng kỳ hạn có vị thế mua (*long position*) và do đó sẽ hưởng lợi từ sự tăng giá của tài sản cơ sở trong suốt vòng đời của hợp đồng.

Để hiểu rõ hơn về hợp đồng kỳ hạn, chúng ta phải xem xét cấu trúc giá trị nhận được khi đáo hạn (*payoff profile*) của chúng. Giả sử một hợp đồng kỳ hạn được thỏa thuận tại thời điểm $t = 0$ và đáo hạn tại thời điểm $T$. Tại thời điểm $t = 0$, các đối tác không trao đổi bất kỳ khoản thanh toán trả trước nào mà thay vào đó, đồng ý về việc giao tài sản cơ sở tại thời điểm $T$ với một mức **giá kỳ hạn (*forward price*)** là $F_0(T)$. Chỉ số dưới $0$ đề cập đến ngày mà mức giá tài sản cơ sở trong tương lai được ấn định ($t = 0$), và chữ $T$ trong ngoặc đơn đề cập đến ngày trao đổi ($t = T$). Giá giao ngay của tài sản cơ sở tại thời điểm $T$ là $S_T$. Bảng minh họa 1 cho thấy giá trị nhận được khi đáo hạn từ góc độ của người mua kỳ hạn, tức là một vị thế mua kỳ hạn (*long forward position*). Lưu ý rằng giá trị nhận được khi đáo hạn (*payoff*) bằng đúng với lợi nhuận (*profit*), vì không có khoản thanh toán trả trước nào được thực hiện.

**Bảng minh họa 1: Cấu trúc Giá trị nhận được của Vị thế Mua Kỳ hạn (*Exhibit 1: Long Forward (Forward Buyer) Payoff Profile*)** 

![](assets/Derivatives.pdf-0035-06.png)

<!-- Picture Text: Payoff/<br>Profit<br>Profit<br>+<br>0 ST<br>F0(T)<br>–<br> -->

> **Chú thích hình ảnh:**
> - **Trục tung:** Giá trị nhận được / Lợi nhuận (*Payoff / Profit*) từ miền âm ($-$) qua $0$ lên miền dương ($+$).
> - **Trục hoành:** Giá giao ngay khi đáo hạn $S_T$, cắt đường biểu diễn lợi nhuận (*Profit*) tại điểm hòa vốn $F_0(T)$.

|**Kết quả (*Outcome*)**|**Giá trị nhận được của Người mua (*Buyer Payoff*)**|**Giá trị nhận được của Người bán (*Seller Payoff*)**|
|---|---|---|
|$S_T > F_0(T)$|$[S_T - F_0(T)] > 0$|$[F_0(T) - S_T] < 0$|
|$S_T < F_0(T)$|$[S_T - F_0(T)] < 0$|$[F_0(T) - S_T] > 0$|

Cấu trúc giá trị nhận được đối xứng (*symmetric payoff profile*) thể hiện trong Bảng minh họa 1 là một đặc điểm chung của các cam kết chắc chắn. Vì giá của công cụ phái sinh là một hàm tuyến tính của tài sản cơ sở, các cam kết chắc chắn còn được gọi là **công cụ phái sinh tuyến tính (*linear derivatives*)**. Tại thời điểm $T$, giao dịch được thanh toán dựa trên mức chênh lệch giữa giá kỳ hạn $F_0(T)$ và giá tài sản cơ sở $S_T$, hay $[S_T - F_0(T)]$ xét từ góc độ của người mua. Nghĩa là, người mua thực hiện được một khoản lãi nếu bà có thể nhận giao tài sản cơ sở đang có giá trị thị trường $S_T$ vượt quá mức giá đã thỏa thuận trước $F_0(T)$. Nếu giá kỳ hạn vượt quá giá trị thị trường hiện hành $[F_0(T) > S_T]$, người mua sẽ chịu một khoản lỗ và phải nhận giao một tài sản với mức lỗ là $[F_0(T) - S_T]$ hoặc trả cho người bán số tiền này bằng tiền mặt. Hợp đồng kỳ hạn thường liên quan đến một lần trao đổi duy nhất trong tương lai, như trong Ví dụ 1.

<!-- PDF Page 36 -->

###### **VÍ DỤ 1 (*EXAMPLE 1*)** 

##### **Giao dịch Mua Vàng Kỳ hạn (*Forward Gold Purchase*)** 

Một nhà đầu tư, Procam Investments, tham gia vào một hợp đồng kỳ hạn thanh toán bằng tiền mặt (*cash-settled forward contract*) với một định chế tài chính trung gian để mua 100 ounce vàng tại mức giá kỳ hạn $F_0(T)$ là $\$1.792,13$ mỗi ounce sau ba tháng.

**1.** Giá vàng giao ngay hôm nay ($S_0$) là $\$1.770$ mỗi ounce.

**2.** Khi hợp đồng đáo hạn, giá vàng ($S_T$) là $\$1.780,50$ mỗi ounce.

**3.** Giá trị nhận được khi đáo hạn (*payoff*), $S_T - F_0(T)$, là $-\$11,63 = \$1.780,50 - \$1.792,13$ mỗi ounce.

**4.** Procam (người mua) phải trả cho định chế tài chính trung gian (người bán) $\$1.163$ ($= 100 \times \$11,63$) để thanh toán hợp đồng kỳ hạn khi đáo hạn.

![](assets/Derivatives.pdf-0036-10.png)

<!-- Picture Text: Agree at  t  = 0 to At time  t  =  T ,<br>exchange underlying for underlying is delivered<br>F0 ( T ) at time  t  =  T at a price of  F0 ( T )<br>Time<br>t  = 0 t  =  T<br>Procam Procam<br>investments investments<br>100 ounces of<br>gold Contract 100 ounces of gold<br>F0 ( T ) × 100 ounces<br>ST  × 100 ounces = $179,213<br>$1,792.13 per = $178,050<br>ounce  F0 ( T )<br>Financial Financial<br>intermediary intermediary<br> -->

> **Chú thích hình ảnh:**
> - **Tại thời điểm $t = 0$:** Thỏa thuận tại $t = 0$ để trao đổi tài sản cơ sở lấy mức giá $F_0(T)$ tại thời điểm $t = T$. Procam Investments ký hợp đồng (*Contract*) với Định chế tài chính trung gian cho 100 ounce vàng tại mức giá $F_0(T) = \$1.792,13/\text{ounce}$.
> - **Tại thời điểm $t = T$:** Tài sản cơ sở được giao (hoặc định giá thanh toán) tại mức giá $F_0(T)$. Procam Investments nhận giá trị 100 ounce vàng theo giá giao ngay $S_T \times 100\text{ ounce} = \$178.050$ và trả $F_0(T) \times 100\text{ ounce} = \$179.213$ cho Định chế tài chính trung gian (thanh toán ròng bằng tiền mặt là $\$1.163$).

Hợp đồng có thể quy định việc giao nhận thực tế tài sản cơ sở hoặc thanh toán bằng tiền mặt (*cash settlement*). Số tiền thanh toán bằng $[S_T - F_0(T)]$ từ góc độ của người mua và bằng $-[S_T - F_0(T)] = [F_0(T) - S_T]$ từ góc độ của người bán. Lưu ý rằng người mua sẽ phải trả $S_0$ tại thời điểm $t = 0$ và thực hiện được mức sinh lợi $(S_T - S_0)$ tại thời điểm $T$ để tạo ra một mức độ tiếp xúc rủi ro trên thị trường giao ngay tương tự như vị thế mua kỳ hạn.

###### **BỘ CÂU HỎI (*QUESTION SET*)** 

##### **Hợp đồng Kỳ hạn (*Forwards*)** 

1. Mô tả một kịch bản trong đó một hợp đồng kỳ hạn có giá trị thanh toán bằng tiền mặt bằng không khi đáo hạn và không có đối tác nào bị vỡ nợ.

###### **Lời giải:** 

   - Một hợp đồng kỳ hạn sẽ có giá trị thanh toán bằng tiền mặt bằng không khi đáo hạn nếu $S_T = F_0(T)$ hay giá trị nhận được từ góc độ của người mua là $[S_T - F_0(T)] = 0$. Điểm này thường được gọi là **điểm hòa vốn (*breakeven point*)** đối với hợp đồng kỳ hạn cho cả người mua và người bán trong trường hợp không có chi phí giao dịch, và được biểu diễn trực quan bằng giao điểm với trục hoành ($x$-axis) của đường lợi nhuận trong Bảng minh họa 1.

2. Xác định các câu trả lời đúng để điền vào chỗ trống: Một nhà sản xuất dầu mỏ ký một hợp đồng phái sinh với một nhà đầu tư để bán 1.000 thùng dầu sau hai tháng tại mức giá kỳ hạn là $\$64$ mỗi thùng. Nếu giá dầu giao ngay khi đáo hạn

<!-- PDF Page 37 -->

là $\$58,50$ mỗi thùng, nhà đầu tư sẽ thực hiện một __________ khi đáo hạn bằng __________.

###### **Lời giải:** 

Một nhà sản xuất dầu mỏ ký một hợp đồng phái sinh với một nhà đầu tư để bán 1.000 thùng dầu sau hai tháng tại mức giá kỳ hạn là $\$64$ mỗi thùng. Nếu giá dầu giao ngay khi đáo hạn là $\$58,50$ mỗi thùng, nhà đầu tư sẽ thực hiện một _khoản lỗ (loss)_ khi đáo hạn bằng _$\$5.500$_.

Giá dầu kỳ hạn, $F_0(T)$, theo hợp đồng bằng $\$64$ mỗi thùng. Khi hợp đồng đáo hạn, giá dầu giao ngay ($S_T$) là $\$58,50$ mỗi thùng.

- Giá trị nhận được của nhà đầu tư trên mỗi thùng dầu:

  $$[S_T - F_0(T)] = \$58,50 - \$64,00 = -\$5,50\text{ mỗi thùng}$$

- Tổng số tiền nhà đầu tư phải trả cho nhà sản xuất dầu mỏ để thanh toán hợp đồng kỳ hạn 1.000 thùng dầu khi đáo hạn:

  $$1.000 \times \$5,50 = \$5.500$$

3. Xác định những bên tham gia hợp đồng kỳ hạn có khả năng phù hợp nhất với các phát biểu sau đây:

|**Bên tham gia**|**Đặc điểm mô tả**|
|---|---|
|A. Bên mua hợp đồng kỳ hạn (*Forward contract purchaser*)|1. Tìm cách hưởng lợi từ sự giảm giá của tài sản cơ sở|
|B. Bên bán hợp đồng kỳ hạn (*Forward contract seller*)|2. Thực hiện được một khoản lãi nếu giá giao ngay ban đầu của tài sản cơ sở, $S_0$, vượt quá giá kỳ hạn $F_0(T)$|
|C. Không phải bên mua cũng không phải bên bán hợp đồng kỳ hạn|3. Nhận được giá trị đáo hạn (*payoff*) dương khi đáo hạn nếu giá giao ngay, $S_T$, vượt quá giá kỳ hạn $F_0(T)$|

###### **Lời giải:** 

1. Đáp án đúng là B. Bên bán kỳ hạn nhận $[F_0(T) - S_T]$ (hoặc trả $[S_T - F_0(T)]$) với bên mua hợp đồng kỳ hạn khi đáo hạn và do đó được hưởng lợi khi giá giao ngay của tài sản cơ sở $S_T$ giảm xuống theo thời gian.

2. Đáp án đúng là C. Cả người mua lẫn người bán hợp đồng kỳ hạn đều không thực hiện được khoản lãi nào nếu giá giao ngay ban đầu, $S_0$, vượt quá giá kỳ hạn $F_0(T)$, bởi vì việc thanh toán được dựa trên giá giao ngay trong tương lai, $S_T$.

3. Đáp án đúng là A. Bên mua hợp đồng kỳ hạn thực hiện được một khoản lãi khi đáo hạn nếu $S_T > F_0(T)$.

#### **HỢP ĐỒNG TƯƠNG LAI (*FUTURES*)** 

![](assets/Derivatives.pdf-0037-19.png)

<!-- Picture Text: 3<br> -->

định nghĩa hợp đồng kỳ hạn, hợp đồng tương lai, hợp đồng hoán đổi, quyền chọn (quyền chọn mua và quyền chọn bán), và công cụ phái sinh tín dụng cũng như so sánh các đặc điểm cơ bản của chúng

**Hợp đồng tương lai (*Futures contracts*)** là các hợp đồng kỳ hạn có quy mô, ngày tháng, và tài sản cơ sở được tiêu chuẩn hóa được giao dịch trên các sở giao dịch hợp đồng tương lai (*futures exchanges*). Thị trường hợp đồng tương lai mang lại cả tính thanh khoản cao hơn lẫn sự bảo vệ chống lại tổn thất do vỡ nợ bằng cách kết hợp tính đồng nhất của hợp đồng với một thị trường có tổ chức gồm các quy tắc, quy định, và một cơ chế bù trừ tập trung.

<!-- PDF Page 38 -->

###### **Đặc điểm và Công cụ của Cam kết Kỳ hạn và Quyền đòi hỏi Có điều kiện (*Forward Commitment and Contingent Claim Features and Instruments*)** 

Người mua hợp đồng tương lai tạo ra một vị thế tiếp xúc mua (*long exposure*) đối với tài sản cơ sở bằng cách đồng ý mua tài sản cơ sở vào một ngày sau đó tại một mức giá đã thỏa thuận trước. Người bán thực hiện cam kết ngược lại, tạo ra một vị thế tiếp xúc bán (*short exposure*) đối với tài sản cơ sở bằng cách đồng ý bán tài sản cơ sở trong tương lai tại một mức giá đã thỏa thuận. Mức giá đã thỏa thuận này được gọi là **giá tương lai (*futures price*)**, $f_0(T)$. Tần suất các kỳ đáo hạn của hợp đồng tương lai, quy mô hợp đồng, và các chi tiết khác được sở giao dịch thiết lập dựa trên mối quan tâm của người mua và người bán.

Đặc điểm quan trọng nhất của hợp đồng tương lai là việc thanh toán hàng ngày (*daily settlement*) đối với các khoản lãi và lỗ cùng sự bảo lãnh tín dụng đi kèm được cung cấp bởi sở giao dịch thông qua trung tâm bù trừ (*clearinghouse*) của mình. Vào cuối mỗi ngày, trung tâm bù trừ thực hiện một nghiệp vụ gọi là **định giá theo thị trường (*mark to market* – MTM)**, còn được gọi là **thanh toán hàng ngày (*daily settlement*)**. Trung tâm bù trừ xác định một mức trung bình của các mức giá giao dịch hợp đồng tương lai cuối cùng trong ngày và chỉ định mức giá đó làm **giá thanh toán (*settlement price*)** cuối ngày. Khi đó, tất cả các hợp đồng được gọi là được định giá lại theo mức giá thanh toán cuối ngày.

Giống như hợp đồng kỳ hạn, không có khoản tiền mặt nào được trao đổi giữa hai bên khi một hợp đồng tương lai được khởi tạo bởi người mua hoặc người bán. Tuy nhiên, mỗi đối tác phải ký quỹ một khoản tiền tối thiểu bắt buộc (hay **ký quỹ ban đầu – *initial margin***) vào một **tài khoản ký quỹ hợp đồng tương lai (*futures margin account*)** được giữ tại sở giao dịch để trung tâm bù trừ sử dụng nhằm thanh toán khoản chênh lệch định giá theo thị trường (MTM) hàng ngày. Các hợp đồng tương lai phải được thực hiện thông qua các định chế tài chính trung gian chuyên biệt, những đơn vị đứng ra bù trừ và thanh toán các khoản chi trả tại sở giao dịch thay mặt cho các đối tác, như được thể hiện trong Ví dụ 2.

###### **VÍ DỤ 2 (*EXAMPLE 2*)** 

##### **Giao dịch Mua một Hợp đồng Tương lai Vàng (*Purchase of a Gold Futures Contract*)** 

![](assets/Derivatives.pdf-0038-08.png)

<!-- Picture Text: Trade initiation:<br>100 ounces of gold 100 ounces of gold<br>Procam Financial London metals<br>investments intermediary exchange (LME)<br>$1,792.13 per ounce $1,792.13 per ounce<br>Initial margin Initial margin<br> -->

> **Chú thích hình ảnh:**
> - **Khởi tạo giao dịch (*Trade initiation*):** **Procam Investments** ký hợp đồng tương lai 100 ounce vàng tại mức giá $\$1.792,13/\text{ounce}$ và nộp **Ký quỹ ban đầu (*Initial margin*)** cho **Định chế tài chính trung gian (*Financial intermediary*)**, đơn vị này tiếp tục chuyển giao lệnh 100 ounce vàng tại mức giá $\$1.792,13/\text{ounce}$ và **Ký quỹ ban đầu (*Initial margin*)** tới **Sở Giao dịch Kim loại Luân Đôn (*London Metals Exchange* – LME)**.

Giống như trong Ví dụ 1, Procam Investments tham gia vào một hợp đồng thanh toán bằng tiền mặt để mua 100 ounce vàng tại mức giá $\$1.792,13$ mỗi ounce sau ba tháng. Thay vì hợp đồng kỳ hạn như trong Ví dụ 1, Procam mua một hợp đồng tương lai $[f_0(T) = \$1.792,13]$ trên sở giao dịch thông qua một định chế tài chính trung gian. Quy tắc của Sở Giao dịch Kim loại Luân Đôn (LME) yêu cầu mức ký quỹ ban đầu bằng tiền mặt là $\$4.950$ cho mỗi hợp đồng vàng (100 ounce) được bán hoặc mua:

- Procam nộp $\$4.950$ tiền ký quỹ ban đầu bắt buộc tại sở giao dịch.

- Giá vàng giao ngay hôm nay ($S_0$) là $\$1.770$ mỗi ounce, và giá mở cửa hợp đồng tương lai vàng, $f_0(T)$, là $\$1.792,13$ mỗi ounce.

- Khi đóng cửa phiên hôm nay, giá hợp đồng tương lai vàng, $f_1(T)$, chốt thanh toán ở mức $\$1.797,13$ mỗi ounce.

- Procam thực hiện được một khoản lãi MTM là $\$500$, hay $\$5\text{ mỗi ounce} \times 100\text{ ounce}$. Công ty nhận được một khoản tiền cộng thêm $\$500$ vào tài khoản ký quỹ hợp đồng tương lai từ trung tâm bù trừ.

- Tài khoản ký quỹ hợp đồng tương lai của Procam có số dư cuối ngày là $\$5.450$, bằng $\$4.950$ ký quỹ ban đầu cộng với khoản lãi MTM $\$500$.

Mỗi hợp đồng tương lai quy định một mức **ký quỹ duy trì (*maintenance margin*)**, hay số dư tối thiểu được ấn định thấp hơn mức ký quỹ ban đầu, mà mỗi người mua và người bán hợp đồng phải duy trì trong tài khoản ký quỹ hợp đồng tương lai kể từ khi khởi tạo giao dịch cho đến khi thanh toán cuối cùng lúc đáo hạn.

<!-- PDF Page 39 -->

Trung tâm bù trừ luân chuyển tiền hàng ngày giữa các tài khoản ký quỹ của người mua và người bán, ghi có (*crediting*) vào tài khoản của những bên có lãi định giá theo thị trường (MTM) và ghi nợ (*charging*) vào tài khoản của những bên bị lỗ định giá theo thị trường.

Ví dụ, quy tắc của Sở Giao dịch Kim loại Luân Đôn yêu cầu mức ký quỹ duy trì là $\$4.500$ cho mỗi hợp đồng vàng 100 ounce được bán hoặc mua. Bây giờ hãy xét _người bán (seller)_ một hợp đồng tương lai có vị thế đối ứng với vị thế của Procam trong Ví dụ 2.

- Người bán nộp $\$4.950$ tiền ký quỹ ban đầu bắt buộc tại sở giao dịch.

- Giá mở cửa hợp đồng tương lai vàng hôm nay, $f_0(T)$, là $\$1.792,13$ mỗi ounce.

- Khi đóng cửa phiên, giá hợp đồng tương lai vàng, $f_1(T)$, chốt thanh toán ở mức $\$1.797,13$ mỗi ounce.

- Người bán chịu một khoản lỗ MTM là $\$500$, hay $\$5\text{ mỗi ounce} \times 100\text{ ounce}$; số tiền $\$500$ bị trung tâm bù trừ khấu trừ khỏi tài khoản ký quỹ hợp đồng tương lai của người bán.

- Tài khoản ký quỹ hợp đồng tương lai của người bán có số dư cuối ngày là $\$4.450$, bằng $\$4.950$ ký quỹ ban đầu trừ đi khoản lỗ MTM $\$500$.

- Tài khoản ký quỹ của người bán bị thấp hơn $\$50$ so với mức ký quỹ duy trì bắt buộc $(\$4.450 - \$4.500 = -\$50)$.

Người bán nhận được một **lệnh gọi ký quỹ (*margin call*)**, hay yêu cầu phải nộp tiền ngay lập tức để đưa số dư tài khoản quay trở lại mức _ký quỹ ban đầu (initial margin)_. Người bán phải nộp thêm $\$500$ để đưa tài khoản ký quỹ trở lại mức ký quỹ ban đầu $\$4.950$. Số tiền cần thiết để bổ sung vào tài khoản ký quỹ hợp đồng tương lai đôi khi được gọi là **ký quỹ biến đổi (*variation margin*)**. Nếu một đối tác không đáp ứng được lệnh gọi ký quỹ, bên đó phải đóng hợp đồng càng sớm càng tốt và bù đắp mọi khoản lỗ phát sinh thêm. Nếu đối tác không thể đáp ứng các nghĩa vụ của mình, trung tâm bù trừ cung cấp bảo lãnh rằng chính trung tâm sẽ tự bù đắp khoản lỗ đó bằng cách duy trì một quỹ bảo hiểm (*insurance fund*). Bảng minh họa 2 cho thấy quy trình ký quỹ và thanh toán hợp đồng tương lai, trong đó $f_0(T)$ là giá tương lai khi khởi tạo và $f_t(T)$ đại diện cho giá tương lai vào ngày $t$.

**Bảng minh họa 2: Quy trình Ký quỹ và Thanh toán Hợp đồng Tương lai (*Exhibit 2: Futures Margin and Settlement Process*)** 

![](assets/Derivatives.pdf-0039-13.png)

<!-- Picture Text: Time<br>t  = 0 Daily ( t ) t  =  T<br>Long Long Long<br>futures futures futures<br>position position position<br>Post initial Margin Settlement<br>margin movement due totals<br>to MTM change fT ( T ) –  f0 ( T ) =<br>ft ( T ) –  ft –1( T )   ST –  f0 ( T )<br>Financial Financial Financial<br>intermediary/ intermediary/ intermediary/<br>Exchange Exchange Exchange<br> -->

> **Chú thích hình ảnh:**
> - **Tại thời điểm $t = 0$:** Bên nắm giữ **Vị thế mua hợp đồng tương lai (*Long futures position*)** nộp ký quỹ ban đầu (*Post initial margin*) cho **Định chế tài chính trung gian / Sở giao dịch (*Financial intermediary / Exchange*)**.
> - **Hàng ngày (*Daily* – $t$):** Biến động số dư ký quỹ do thay đổi định giá theo thị trường (MTM): $f_t(T) - f_{t-1}(T)$.
> - **Tại thời điểm $t = T$:** Tổng thanh toán lũy kế: $f_T(T) - f_0(T) = S_T - f_0(T)$.

Các sở giao dịch bảo lưu quyền áp đặt các yêu cầu nghiêm ngặt hơn so với các quy tắc tài khoản ký quỹ hợp đồng tương lai tiêu chuẩn nhằm hạn chế những tổn thất tiềm tàng từ việc vỡ nợ của đối tác. Ví dụ, đối với các vị thế lớn hoặc khi có sự gia tăng đáng kể về độ biến động giá của tài sản cơ sở, sở giao dịch có thể tăng mức ký quỹ bắt buộc và/hoặc đưa ra các lệnh gọi ký quỹ ngay trong ngày giao dịch (*intraday basis*). Một số hợp đồng tương lai cũng giới hạn mức biến động giá hàng ngày. Các quy tắc này, được gọi là **biên độ dao động giá (*price limits*)**,

<!-- PDF Page 40 -->

thiết lập một dải biên độ so với giá thanh toán của ngày hôm trước mà tất cả các giao dịch phải diễn ra bên trong đó. Nếu những người tham gia thị trường muốn giao dịch ở một mức giá nằm ngoài các biên độ này, giao dịch sẽ tạm dừng cho đến khi hai bên đồng ý thực hiện một giao dịch tại một mức giá nằm trong phạm vi quy định. Trong các trường hợp khác, các sở giao dịch sử dụng cơ chế gọi là **ngắt mạch tự động (*circuit breaker*)** để tạm dừng giao dịch trong ngày trong một khoảng thời gian ngắn nếu chạm đến giới hạn giá.

Tương tự như hợp đồng kỳ hạn, việc thanh toán cuối cùng khi đáo hạn đối với hợp đồng tương lai được dựa trên mức chênh lệch giữa giá tương lai, $f_0(T)$, và giá tài sản cơ sở $S_T$, hay $[S_T - f_0(T)]$ xét từ góc độ của người mua. Bởi vì Procam đã đồng ý mua vàng hiện đang (tại $t = T$) được định giá ở mức $\$1.780,50$ mỗi ounce với mức giá mua là $\$1.792,13$ mỗi ounce, công ty nợ $\$11,63$ mỗi ounce, hay $\$1.163$ $[(\$1.780,50 - \$1.792,13) \times 100\text{ oz.}]$ theo cả hợp đồng kỳ hạn ở Ví dụ 1 lẫn hợp đồng tương lai này. Cấu trúc giá trị nhận được _ròng (net payoff profile)_ thể hiện trong Bảng minh họa 1 là giống hệt nhau đối với hợp đồng tương lai và hợp đồng kỳ hạn với giả định chúng có cùng ngày đáo hạn, điểm khác biệt duy nhất là _thời điểm (timing)_ của các dòng tiền do việc thanh toán định giá theo thị trường (MTM) hàng ngày của hợp đồng tương lai, như được thể hiện trong Ví dụ 3.

###### **VÍ DỤ 3 (*EXAMPLE 3*)** 

![](assets/Derivatives.pdf-0040-06.png)

<!-- Picture Text: Final Settlement of a Gold Futures Contract<br> -->

##### **Thanh toán Cuối cùng của một Hợp đồng Tương lai Vàng (*Final Settlement of a Gold Futures Contract*)**

![](assets/Derivatives.pdf-0040-07.png)

<!-- Picture Text: Final settlement:<br>Return of Margin Return of Margin<br>Plus/Minus: Plus/Minus:<br>Final daily settlement Final daily settlement<br>fT ( T ) –  fT –1( T ) fT ( T ) –  fT –1( T )<br>Procam Financial London Metals<br>Investments Intermediary Exchange (LME)<br> -->

> **Chú thích hình ảnh:**
> - **Thanh toán cuối cùng (*Final settlement*):** Hoàn trả tiền ký quỹ (*Return of Margin*) Cộng/Trừ (*Plus/Minus*) Khoản thanh toán hàng ngày cuối cùng $f_T(T) - f_{T-1}(T)$ từ **Sở Giao dịch Kim loại Luân Đôn (LME)** qua **Định chế tài chính trung gian** về cho **Procam Investments**.

Để thuận tiện cho việc trình bày, chúng ta nén ba tháng biến động giá hợp đồng tương lai vàng từ Ví dụ 2 thành sáu ngày giao dịch trong bảng tính sau đây:

###### **Bảng minh họa 3 (*Exhibit 3*)** 

###### **Tài khoản Ký quỹ Hợp đồng Tương lai của Procam (*Procam’s Futures Margin Account*)** 

|Thông số hợp đồng|Giá trị|Đơn vị|
|---|---|---|
|Hợp đồng Vàng (*Gold Contract*)|100|ounce|
|Số lượng hợp đồng (*# of Contracts*)|1||
|Giá tương lai ban đầu $f_0(T)$ (*Initial Futures Price*)|$\$1.792,13$|mỗi ounce|
|Giá trị vị thế ban đầu (*Initial Position Value*)|$\$179.213$||
|Ký quỹ ban đầu (*Initial Margin*)|$\$4.950$||
|Ký quỹ duy trì (*Maintenance Margin*)|$\$4.500$||

|**Ngày (*Day*)**|**Giá tương lai (*Futures Price*)**|**Lãi (Lỗ) trong ngày (*Day Gain/Loss*)**|**Tổng Lãi (Lỗ) (*Total Gain/Loss*)**|**Số dư ký quỹ (*Margin Balance*)**|**Lệnh gọi ký quỹ (*Margin Call*)**|
|---|---|---|---|---|---|
|$T - 6$|$\$1.792,13$|||$\$4.950$||
|$T - 5$|$\$1.797,13$|$\$500$|$\$500$|$\$5.450$|—|
|$T - 4$|$\$1.786,25$|$(\$1.088)$|$(\$588)$|$\$4.362$|$\$588$|
|$T - 3$|$\$1.782,19$|$(\$406)$|$(\$994)$|$\$4.544$|—|
|$T - 2$|$\$1.777,45$|$(\$474)$|$(\$1.468)$|$\$4.070$|$\$880$|
|$T - 1$|$\$1.779,50$|$\$205$|$(\$1.263)$|$\$5.155$|—|
|$T$|$\$1.780,50$|$\$100$|**$(\$1.163)$**|$\$5.255$|$\$1.468$|

<!-- PDF Page 41 -->

|**Kết quả của Procam từ Hợp đồng Tương lai (*Procam’s Results from the Futures Contract*)**|**Giá trị**|
|---|---|
|Hợp đồng Vàng (*Gold Contract*)|100|
|Số lượng hợp đồng (*# of Contracts*)|1|
|Giá tương lai ban đầu $f_0(T)$ (*Initial Futures Price*)|$\$1.792,13$|
|Giá trị vị thế ban đầu (*Initial Position Value*)|$\$179.213$|
|Tổng Lãi (Lỗ) (*Total Gain (Loss)*)|$(\$1.163)$|
|Giá tương lai cuối cùng $F_T(T)$ (*Final Futures Price*)|$\$1.780,50$|
|Giá trị vị thế cuối cùng (*Final Position Value*)|$\$178.050$|
|Tổng các lệnh gọi ký quỹ (*Sum of Margin Calls*)|$\$1.468$|
|Số dư ký quỹ đầu kỳ trừ cuối kỳ (*Beginning less Ending Margin Balance*)|$(\$305)$|
|Tổng các khoản thanh toán ròng vào Tài khoản Ký quỹ (*Total Payments to Margin Account*)|$\$1.163$|

Khi giá hợp đồng tương lai vàng, $f_0(t)$, sụt giảm và số dư ký quỹ giảm xuống dưới mức tối thiểu của ký quỹ duy trì là $\$4.500$ theo thời gian, Procam phải ngay lập tức nộp bổ sung số dư của mình về lại mức ký quỹ ban đầu $\$4.950$ mỗi khi điều này xảy ra:

- Vào Ngày $T - 4$, hợp đồng tương lai vàng giảm $\$10,88$ mỗi ounce $(\$1.797,13 - \$1.786,25)$. Số dư của Procam giảm $\$1.088$ $(100 \times \$10,88)$ xuống còn $\$4.362$ $(\$5.450 - \$1.088)$. Procam phải đối mặt với một lệnh gọi ký quỹ là $\$588$ $(\$4.950 - \$4.362)$.

- Vào Ngày $T - 2$, hợp đồng tương lai vàng giảm $\$4,74$ mỗi ounce $(\$1.782,19 - \$1.777,45)$. Số dư của Procam giảm $\$474$ $(100 \times \$4,74)$ xuống còn $\$4.070$ $(\$4.544 - \$474)$. Procam phải đối mặt với một lệnh gọi ký quỹ là $\$880$ $(\$4.950 - \$4.070)$.

Vào ngày giao dịch cuối cùng, Procam đã nộp tổng cộng $\$1.468$ $(\$588 + \$880)$ theo các lệnh gọi ký quỹ và số dư tài khoản ký quỹ hợp đồng tương lai của công ty là $\$5.155$, hay cao hơn $\$205$ so với mức ký quỹ ban đầu $\$4.950$. Procam có mức lỗ MTM lũy kế là $\$1.263$ $(\$1.468 - \$205)$ vào đầu ngày giao dịch cuối cùng.

- Giá thanh toán hợp đồng tương lai vàng của ngày hôm trước, $f_{T-1}(T)$, là $\$1.779,50$.

- Hợp đồng tương lai vàng tăng $\$1$ mỗi ounce vào ngày giao dịch cuối cùng để chốt thanh toán ở mức $f_T(T) = \$1.780,50$ mỗi ounce, bằng đúng mức giá đối với hợp đồng kỳ hạn trong Ví dụ 1.

- Mức thay đổi hàng ngày trong tài khoản ký quỹ của Procam là một khoản tăng thêm $\$100$ $(\$1\text{ mỗi ounce} \times 100\text{ ounce})$, đưa tài khoản ký quỹ lên mức $\$5.255$.

- Số dư ký quỹ hợp đồng tương lai của Procam là $\$5.255$ được hoàn trả khi thanh toán, mang lại khoản thu hồi ròng về ký quỹ là $\$305$ $(\$5.255 - \$4.950)$.

- Procam nhận được khoản thu hồi ròng $\$305$ tiền ký quỹ khi thanh toán, tương ứng với mức lỗ lũy kế khi thanh toán là $\$1.163$ $(\$305 - \$1.468 = -\$1.163$).

Cả hợp đồng kỳ hạn và hợp đồng tương lai đều dẫn đến một khoản lỗ thanh toán là $\$1.163$, nhưng hợp đồng kỳ hạn được thanh toán toàn bộ một lần khi đáo hạn trong khi hợp đồng tương lai được thanh toán dựa trên định giá theo thị trường (MTM) hàng ngày. Nguyên lý giá trị thời gian của tiền tệ (*time value of money*) cho thấy rằng các khoản thanh toán của hợp đồng kỳ hạn và hợp đồng tương lai này không phải là những số tiền tương đương nhau hoàn toàn, nhưng sự khác biệt là rất nhỏ đối với các kỳ hạn ngắn và môi trường lãi suất thấp. Cũng cần lưu ý rằng theo hợp đồng kỳ hạn trong Ví dụ 1, định chế tài chính trung gian phải gánh chịu rủi ro đối tác đối với Procam cho khoản thanh toán kỳ hạn. Trên thực tế, các định chế tài chính trung gian thường sử dụng các thỏa thuận tài sản thế chấp (*collateral arrangements*) tương tự như cơ chế ký quỹ hợp đồng tương lai cho các hợp đồng kỳ hạn hoặc các công cụ phái sinh khác nhằm giảm thiểu rủi ro tín dụng đối tác.

Khi đáo hạn, số lượng các hợp đồng đang lưu hành, hay **khối lượng mở (*open interest*)**, được thanh toán thông qua tiền mặt hoặc giao hàng vật chất. Thay vào đó, một đối tác có thể lựa chọn tham gia vào một hợp đồng tương lai đối ứng (*offsetting futures contract*) trước khi hết hạn để đóng vị thế; ví dụ, một người mua hợp đồng tương lai

<!-- PDF Page 42 -->

có thể đơn giản là bán hợp đồng đang mở đó đi. Trung tâm bù trừ sẽ định giá lại hợp đồng theo mức giá hiện hành so với giá thanh toán trước đó và đóng vị thế của người tham gia.

Các hợp đồng tương lai quy định cụ thể liệu việc giao hàng vật chất đối với tài sản cơ sở hay thanh toán bằng tiền mặt sẽ diễn ra khi đáo hạn. Ví dụ, một hợp đồng tương lai hàng hóa có giao hàng vật chất bắt buộc người bán phải giao một tài sản cơ sở có chủng loại, số lượng, và chất lượng cụ thể tới một địa điểm được chỉ định. Người mua phải chấp nhận và trả tiền cho việc giao hàng đó, điều này đảm bảo rằng giá hợp đồng tương lai sẽ hội tụ (*converges*) về giá giao ngay khi đáo hạn.

###### **BỘ CÂU HỎI (*QUESTION SET*)** 

##### **Hợp đồng Tương lai (*Futures*)** 

1. Xác định các câu trả lời đúng để điền vào chỗ trống: Nếu tài khoản ký quỹ của người mua hợp đồng tương lai giảm xuống dưới mức __________ __________, hay số dư tối thiểu mà mỗi người mua và người bán hợp đồng phải duy trì trong tài khoản kể từ khi khởi tạo giao dịch cho đến khi thanh toán cuối cùng, người mua phải ngay lập tức nộp tiền vào để đưa số dư tài khoản quay trở lại mức __________ __________.

###### **Lời giải:** 

Nếu tài khoản ký quỹ của người mua hợp đồng tương lai giảm xuống dưới mức _ký quỹ duy trì (maintenance margin)_, hay số dư tối thiểu mà mỗi người mua và người bán hợp đồng phải duy trì trong tài khoản kể từ khi khởi tạo giao dịch cho đến khi thanh toán cuối cùng, người mua phải ngay lập tức nộp tiền vào để đưa số dư tài khoản quay trở lại mức _ký quỹ ban đầu (initial margin)_.

2. Mô tả quy trình định giá theo thị trường (*mark-to-market*) đối với một hợp đồng tương lai.

###### **Lời giải:** 

Trung tâm bù trừ của sở giao dịch xác định một mức trung bình của các mức giá hợp đồng tương lai cuối cùng trong ngày và chỉ định mức giá đó làm giá thanh toán cuối ngày (*end-of-day settlement price*). Việc thanh toán hàng ngày đối với các khoản lãi và lỗ diễn ra thông qua tài khoản ký quỹ hợp đồng tương lai của mỗi đối tác.

3. Xác định những bên tham gia hợp đồng tương lai tương ứng với các phát biểu sau đây:

|**Bên tham gia**|**Đặc điểm mô tả**|
|---|---|
|A. Bên mua hợp đồng tương lai (*Futures contract purchaser*)|1. Phải nộp một khoản tiền ký quỹ khi khởi tạo hợp đồng và duy trì một số dư tối thiểu cho đến khi đáo hạn|
|B. Bên bán hợp đồng tương lai (*Futures contract seller*)|2. Nhận được một khoản tiền cộng vào tài khoản ký quỹ nếu giá hợp đồng tương lai tăng lên vào bất kỳ ngày giao dịch nào|
|C. Cả bên mua và bên bán hợp đồng tương lai|3. Nhận được một giá trị đáo hạn (*payoff*) dương nếu giá giao ngay $S_T$ thấp hơn giá tương lai, $f_0(T)$, khi đáo hạn|

###### **Lời giải:** 

1. Đáp án đúng là C. Cả người mua và người bán hợp đồng tương lai đều phải nộp tiền ký quỹ và duy trì một số dư ký quỹ tối thiểu (ký quỹ duy trì) trong suốt vòng đời của hợp đồng.

2. Đáp án đúng là A. Người mua hợp đồng tương lai thực hiện được một khoản lãi định giá theo thị trường (MTM) vào bất kỳ ngày giao dịch nào khi giá hợp đồng tương lai tăng lên và nhận được một khoản tiền cộng thêm tương ứng vào tài khoản ký quỹ.

<!-- PDF Page 43 -->

3. Đáp án đúng là B. Người bán hợp đồng tương lai thực hiện được một giá trị đáo hạn dương khi đáo hạn nếu $S_T < f_0(T)$.

#### **HỢP ĐỒNG HOÁN ĐỔI (*SWAPS*)** 

## **<mark>4</mark>** 

định nghĩa hợp đồng kỳ hạn, hợp đồng tương lai, hợp đồng hoán đổi, quyền chọn (quyền chọn mua và quyền chọn bán), và công cụ phái sinh tín dụng cũng như so sánh các đặc điểm cơ bản của chúng

Hợp đồng hoán đổi (*swap*) là một cam kết chắc chắn theo đó hai đối tác trao đổi một chuỗi các dòng tiền trong tương lai. Một luồng dòng tiền thường biến đổi, hay thả nổi (*variable, or floating*), và được xác định bởi một lãi suất tham chiếu thị trường (*market reference rate*) được thiết lập lại (*resets*) vào mỗi kỳ. Luồng dòng tiền còn lại thường cố định (*fixed*) hoặc có thể thay đổi dựa trên một tài sản cơ sở hoặc một mức lãi suất khác. Trong trường hợp này, chúng ta gọi đối tác chi trả các dòng tiền biến đổi là **bên trả lãi suất thả nổi (*floating-rate payer*)** (hoặc bên nhận lãi suất cố định – *fixed-rate receiver*) và đối tác chi trả các dòng tiền cố định là **bên trả lãi suất cố định (*fixed-rate payer*)** (hoặc bên nhận lãi suất thả nổi – *floating-rate receiver*), như được thể hiện trong Bảng minh họa 4.

**Bảng minh họa 4: Cơ chế Hoạt động của Hợp đồng Hoán đổi (*Exhibit 4: Swap Mechanics*)** 

![](assets/Derivatives.pdf-0043-09.png)

<!-- Picture Text: Floating Market<br>Reference Rate<br>Fixed-Rate Payer Floating-Rate Payer<br>(Floating-Rate Receiver) (Fixed-Rate Receiver)<br>Fixed Rate<br> -->

> **Chú thích hình ảnh:**
> - **Bên trả lãi suất cố định / Bên nhận lãi suất thả nổi (*Fixed-Rate Payer / Floating-Rate Receiver*)** trả **Lãi suất cố định (*Fixed Rate*)** cho **Bên trả lãi suất thả nổi / Bên nhận lãi suất cố định (*Floating-Rate Payer / Fixed-Rate Receiver*)**, và nhận lại **Lãi suất tham chiếu thị trường thả nổi (*Floating Market Reference Rate*)**.

Hợp đồng hoán đổi và hợp đồng kỳ hạn có các đặc điểm tương tự nhau, chẳng hạn như ngày bắt đầu, ngày đáo hạn, và một tài sản/biến số cơ sở được đàm phán giữa các đối tác và được quy định cụ thể trong hợp đồng. Hợp đồng hoán đổi lãi suất (*interest rate swaps*), trong đó một mức lãi suất cố định được trao đổi lấy một mức lãi suất thả nổi, là loại hợp đồng hoán đổi phổ biến nhất. Đối với mỗi kỳ trong tương lai, lãi suất tham chiếu thị trường (MRR) do bên trả lãi suất thả nổi chi trả sẽ được thiết lập lại, trong khi lãi suất cố định (được gọi là **lãi suất hoán đổi – *swap rate***) giữ nguyên không đổi, như được thể hiện trong Bảng minh họa 5.

<!-- PDF Page 44 -->

**Bảng minh họa 5: Hợp đồng Hoán đổi như một Chuỗi các Giao dịch Trao đổi Kỳ hạn (*Exhibit 5: Swap as a Series of Forward Exchanges*)** 

![](assets/Derivatives.pdf-0044-04.png)

<!-- Picture Text: Time<br>t  = 1 t  = 2 t  =  T<br>Fixed-Rate Fixed-Rate Fixed-Rate<br>Payer Payer Payer<br>MRR1 × Fixed rate MRR2 × Fixed rate MRR T  × Fixed rate<br>Notional × × Notional Notional × × Notional Notional × × Notional<br>Period × Period Period × Period Period × Period<br>Floating-Rate Floating-Rate Floating-Rate<br>Payer Payer Payer<br> -->

> **Chú thích hình ảnh:**
> - Tại mỗi kỳ thanh toán $t = 1, t = 2, \dots, t = T$:
>   - **Bên trả lãi suất cố định (*Fixed-Rate Payer*)** trả cho **Bên trả lãi suất thả nổi (*Floating-Rate Payer*)** khoản tiền: $\text{Lãi suất cố định (Fixed rate)} \times \text{Vốn gốc danh nghĩa (Notional)} \times \text{Kỳ hạn (Period)}$.
>   - **Bên trả lãi suất thả nổi (*Floating-Rate Payer*)** trả cho **Bên trả lãi suất cố định (*Fixed-Rate Payer*)** khoản tiền: $\text{MRR}_t \times \text{Vốn gốc danh nghĩa (Notional)} \times \text{Kỳ hạn (Period)}$.

Các đối tác thường trao đổi một khoản thanh toán bù trừ ròng (*net payment*) giữa các khoản thanh toán lãi suất cố định và lãi suất thả nổi trên hợp đồng hoán đổi như trong Ví dụ 4.

###### **VÍ DỤ 4 (*EXAMPLE 4*)** 

##### **Hợp đồng Hoán đổi của Fyleton Investments (*Fyleton Investments Swap*)** 

Fyleton Investments đã tham gia vào một hợp đồng hoán đổi lãi suất nhận lãi cố định (*receive-fixed*) kỳ hạn năm năm trị giá 200 triệu GBP với một định chế tài chính trung gian nhằm làm tăng thời lượng (*duration*) cho danh mục đầu tư thu nhập cố định của mình. Theo các điều khoản của hợp đồng hoán đổi, Fyleton đã đồng ý nhận mức lãi suất cố định GBP bán niên là 2,25% và trả lãi suất MRR kỳ hạn sáu tháng.

![](assets/Derivatives.pdf-0044-09.png)

<!-- Picture Text: 6-Month MRR<br>Fyleton Financial<br>Investments Intermediary<br>2.25% Semiannual<br> -->

> **Chú thích hình ảnh:**
> - **Fyleton Investments** trả **Lãi suất MRR kỳ hạn 6 tháng (*6-Month MRR*)** cho **Định chế tài chính trung gian (*Financial Intermediary*)**, và nhận lại mức lãi cố định **2,25% bán niên (*2.25% Semiannual*)**.

Hãy tính toán lần trao đổi dòng tiền hoán đổi đầu tiên nếu lãi suất MRR kỳ hạn sáu tháng được ấn định ở mức 1,95%.

- Định chế tài chính trung gian nợ Fyleton một khoản thanh toán dòng tiền cố định là:

  $$\text{GBP } 2.250.000 = \text{GBP } 200\text{ triệu} \times \frac{0,0225}{2}$$

- Fyleton nợ định chế tài chính trung gian một khoản thanh toán dòng tiền thả nổi là:

  $$\text{GBP } 1.950.000 = \text{GBP } 200\text{ triệu} \times \frac{0,0195}{2}$$

- Các khoản thanh toán cố định và thả nổi được bù trừ ròng với nhau, và kết quả ròng là định chế tài chính trung gian trả cho Fyleton:

  $$\text{GBP } 300.000 = \text{GBP } 2.250.000 - \text{GBP } 1.950.000$$

Vốn gốc danh nghĩa (*notional principal*) thường không được trao đổi mà thay vào đó được sử dụng để tính toán các khoản thanh toán lãi cố định và thả nổi, như trong Ví dụ 4. Ví dụ này minh họa cách một nhà quản lý đầu tư có thể sử dụng hợp đồng hoán đổi lãi suất để thay đổi thời lượng (*duration*) của danh mục đầu tư mà không cần giao dịch trái phiếu. Các tổ chức phát hành thường sử dụng hợp đồng hoán đổi để thay đổi cấu trúc tiếp xúc rủi ro của một khoản nợ phải trả, chẳng hạn như một khoản vay có kỳ hạn.

Giống như hợp đồng tương lai và hợp đồng kỳ hạn, không có khoản tiền nào được trao đổi khi một hợp đồng hoán đổi được khởi tạo. Do đó, giá trị của một hợp đồng hoán đổi khi khởi tạo trên thực tế bằng không, nếu bỏ qua chi phí giao dịch. Trong một bài học về thu nhập cố định trước đây, chúng ta đã thấy rằng lãi suất kỳ hạn hàm ý (*implied forward rates*) có thể được suy ra từ lãi suất giao ngay (*spot rates*). Các mức lãi suất MRR kỳ hạn (*forward MRRs*) có thể được sử dụng để xác định các dòng tiền tương lai kỳ vọng cho nhánh thả nổi (*floating leg*) của một hợp đồng hoán đổi lãi suất. Lãi suất hoán đổi (*swap rate*) cho các khoản thanh toán của nhánh cố định (*fixed leg*) được xác định bằng cách giải tìm một mức lợi suất cố định không đổi giúp cân bằng giá trị hiện tại của các khoản thanh toán nhánh cố định và nhánh thả nổi.

<!-- PDF Page 45 -->

Khi điều kiện thị trường thay đổi và thời gian trôi qua, giá trị định giá theo thị trường (*mark-to-market value*) của một hợp đồng hoán đổi sẽ lệch khỏi mức không ($0$), dẫn đến một giá trị MTM dương cho một đối tác và một giá trị MTM âm đối ứng cho đối tác kia. Các điều khoản tín dụng của hợp đồng hoán đổi được đàm phán riêng tư giữa các đối tác trong một thỏa thuận phi tập trung (OTC) và có thể dao động từ việc tiếp xúc rủi ro không có tài sản thế chấp (*uncollateralized exposure*) — nơi mỗi đối tác chịu toàn bộ rủi ro vỡ nợ của bên kia — cho đến các điều khoản tương tự như cơ chế ký quỹ hợp đồng tương lai cho một hoặc cả hai đối tác. Một sự kiện vỡ nợ của đối tác thường kích hoạt việc chấm dứt hợp đồng hoán đổi (*swap termination*) và thanh toán theo giá trị MTM giống như bất kỳ khoản đòi nợ nào khác. Các hợp đồng hoán đổi được bù trừ tập trung giữa các định chế tài chính trung gian và một đối tác trung tâm (CCP) bao gồm các điều khoản ký quỹ tương tự như hợp đồng tương lai nhằm tiêu chuẩn hóa và giảm thiểu rủi ro đối tác.

###### **BỘ CÂU HỎI (*QUESTION SET*)** 

##### **Hợp đồng Hoán đổi (*Swaps*)** 

1. Mô tả một điểm tương đồng và một điểm khác biệt giữa hợp đồng kỳ hạn và hợp đồng hoán đổi.

###### **Lời giải:** 

**Điểm tương đồng:** Cả hợp đồng kỳ hạn và hợp đồng hoán đổi đều đại diện cho các cam kết chắc chắn có giá trị ban đầu bằng không, trong đó các dòng tiền được trao đổi trong tương lai tại một mức giá đã thỏa thuận trước.

**Điểm khác biệt:** Hợp đồng kỳ hạn thường liên quan đến một lần trao đổi dòng tiền duy nhất trong tương lai, trong khi một hợp đồng hoán đổi liên quan đến nhiều hơn một lần trao đổi các dòng tiền trong tương lai.

2. Xác định các câu trả lời đúng để điền vào chỗ trống: Theo một hợp đồng hoán đổi, chúng ta gọi đối tác chi trả các dòng tiền biến đổi là _______________ và đối tác chi trả các dòng tiền cố định là _______________.

###### **Lời giải:** 

Theo một hợp đồng hoán đổi, chúng ta gọi đối tác chi trả các dòng tiền biến đổi là _bên trả lãi suất thả nổi (floating-rate payer)_ (hoặc _bên nhận lãi suất cố định – fixed-rate receiver_) và đối tác chi trả các dòng tiền cố định là _bên trả lãi suất cố định (fixed-rate payer)_ (hoặc _bên nhận lãi suất thả nổi – floating-rate receiver_).

3. Xác định những bên tham gia hợp đồng hoán đổi lãi suất tương ứng với các phát biểu sau đây:

|**Bên tham gia**|**Đặc điểm mô tả**|
|---|---|
|A. Bên trả lãi suất cố định (*Fixed-rate payer*)|1. Thực hiện một khoản thanh toán vào mỗi kỳ tính lãi dựa trên một lãi suất tham chiếu thị trường|
|B. Bên trả lãi suất thả nổi (*Floating-rate payer*)|2. Có thể đối mặt với giá trị định giá theo thị trường (MTM) dương hoặc âm trong suốt vòng đời của một hợp đồng hoán đổi lãi suất|
|C. Cả bên trả lãi suất cố định và bên trả lãi suất thả nổi|3. Nhận được một khoản thanh toán ròng trên hợp đồng hoán đổi cho bất kỳ kỳ tính lãi nào mà lãi suất tham chiếu thị trường vượt quá lãi suất cố định|

###### **Lời giải:** 

1. Đáp án đúng là B. Bên trả lãi suất thả nổi trên một hợp đồng hoán đổi thực hiện một khoản thanh toán vào mỗi kỳ dựa trên một lãi suất tham chiếu thị trường.

2. Đáp án đúng là C. Cả bên trả lãi suất cố định và bên trả lãi suất thả nổi đều có thể đối mặt với giá trị MTM dương hoặc MTM âm trên một hợp đồng hoán đổi.
