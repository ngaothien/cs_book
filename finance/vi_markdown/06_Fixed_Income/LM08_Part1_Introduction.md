# Tập 6: Thu nhập Cố định (Fixed Income)
## Học phần 8: Các Thước đo Lợi suất và Chênh lệch Lợi suất đối với Công cụ Lãi suất Thả nổi (Yield and Yield Spread Measures for Floating-Rate Instruments)
### Phần 1/2: Giới thiệu (Trang PDF 197–206)

---

<!-- PDF Page 197 -->

#### H Ọ C P H Ầ N 

# **<mark>8</mark>** 

### **Các Thước đo Lợi suất và Chênh lệch Lợi suất đối với Công cụ Lãi suất Thả nổi (*Yield and Yield Spread Measures for Floating-Rate Instruments*)** 

###### **<mark>MỤC TIÊU HỌC TẬP (*LEARNING OUTCOMES*)</mark>** 

|**_Mức độ thành thạo_**|**_Ứng viên cần có khả năng:_**|
|---|---|
||tính toán và diễn giải các thước đo chênh lệch lợi suất (*yield spread measures*) đối với các công cụ lãi suất thả nổi (*floating-rate instruments*)|
||tính toán và diễn giải các thước đo lợi suất (*yield measures*) đối với các công cụ thị trường tiền tệ (*money market instruments*)|



##### **GIỚI THIỆU (*INTRODUCTION*)** 

## **<mark>1</mark>** 

Các bài học trước đã đề cập đến việc định giá, lợi suất và chênh lệch lợi suất (*spreads*) đối với các trái phiếu có lãi suất coupon cố định (*fixed coupon rates*) và thời gian đáo hạn từ một năm trở lên. Hai bài học tiếp theo sẽ mở rộng thảo luận sang các công cụ có lãi suất coupon biến đổi thay vì cố định, được gọi là **công cụ lãi suất thả nổi (*floating-rate instruments*)**, và những công cụ có kỳ hạn gốc từ một năm trở xuống, được gọi là **công cụ thị trường tiền tệ (*money market instruments*)**. Cả hai loại công cụ này đều quan trọng đối với các nhà đầu tư và tổ chức phát hành. Các công cụ lãi suất thả nổi, bằng cách điều chỉnh dòng tiền theo sự thay đổi của lãi suất, chịu ít rủi ro giá (*price risk*) hơn so với các công cụ lãi suất cố định và được sử dụng để phòng vệ (*hedge*) một số rủi ro nhất định cũng như để khớp dòng tiền giữa tài sản và nợ phải trả (*asset and liability cash flows*). Hầu hết các khoản vay đều là công cụ lãi suất thả nổi. Các công cụ thị trường tiền tệ là một nguồn tài trợ ngắn hạn quan trọng đối với nhiều loại tổ chức phát hành. Thời gian đáo hạn ngắn có nghĩa là các nhà đầu tư có thể tái đầu tư và các tổ chức phát hành có thể tái cấp vốn tương đối nhanh chóng, điều này làm giảm rủi ro lãi suất (*interest rate risk*). 

Hầu hết các ví dụ và bảng biểu được sử dụng xuyên suốt bài đọc có thể được tải xuống dưới dạng sổ làm việc Microsoft Excel. Mỗi trang tính trong sổ làm việc được gắn nhãn với số ví dụ hoặc số bảng biểu tương ứng trong văn bản. 

###### **TỔNG QUAN HỌC PHẦN (*LEARNING MODULE OVERVIEW*)** 

- **Công cụ lãi suất thả nổi (*floating-rate instrument*)** là một công cụ nợ có tiền lãi được xác định bởi **lãi suất tham chiếu thị trường (*market reference rate* – MRR)** quan sát được cộng với một **biên độ yết giá (*quoted margin*)**. Các khoản thanh toán lãi được đặt lại (*reset*), phản ánh bất kỳ thay đổi nào trong MRR, vào các ngày đã được xác định trước. 


<!-- PDF Page 198 -->

- **Biên độ yết giá (*quoted margin*)** là một mức chênh lệch xác định cao hơn hoặc thấp hơn lãi suất tham chiếu. **Biên độ yêu cầu (*required margin*)**, còn được gọi là **biên độ chiết khấu (*discount margin*)**, là mức chênh lệch được các nhà đầu tư yêu cầu. 

- Biên độ yêu cầu phản ánh các rủi ro “từ dưới lên” (*“bottom-up”*) hay rủi ro đặc thù của tổ chức phát hành và chứng khoán (*issuer- and security-specific risks*) và tương tự như chênh lệch lợi suất (*yield spread*) của một trái phiếu lãi suất cố định đã được thảo luận trong các bài học trước. Nếu một trái phiếu lãi suất thả nổi (*floater*) được giao dịch ngang mệnh giá (*at par*), biên độ yết giá và biên độ yêu cầu sẽ bằng nhau. 

- **Các công cụ thị trường tiền tệ (*money market instruments*)** có kỳ hạn gốc từ một năm trở xuống và được yết giá bằng các quy ước khác với các quy ước của những chứng khoán có kỳ hạn dài hơn. Báo giá được thực hiện trên cơ sở **lãi suất chiết khấu (*discount rate*)** hoặc **lãi suất cộng thêm (*add-on rate*)**. 

- **Lãi suất chiết khấu thị trường tiền tệ (*money market discount rates*)** là thu nhập tiền lãi chia cho mệnh giá (giá trị đáo hạn – *face value / maturity value*). Chúng đánh giá thấp (*understate*) tỷ suất sinh lợi của nhà đầu tư nếu giá mua thấp hơn mệnh giá và ngược lại. 

- Các thước đo thông thường của thị trường tiền tệ có thể được chuyển đổi để tăng cường khả năng so sánh với các chứng khoán dài hạn hơn. 

###### **TỰ ĐÁNH GIÁ HỌC PHẦN (*LEARNING MODULE SELF-ASSESSMENT*)** 

Các câu hỏi ban đầu này nhằm giúp bạn tự đánh giá mức độ hiểu biết hiện tại của mình về học phần này. 

1. Thông tin sau đây liên quan đến ba trái phiếu lãi suất thả nổi (*floating-rate notes* – FRNs) được phát hành ngang mệnh giá (*at par value*) và có MRR 3 tháng làm lãi suất tham chiếu. 

|**Trái phiếu lãi suất thả nổi (*Floating-Rate Note*)**|**Biên độ yết giá (*Quoted Margin*)**|**Biên độ chiết khấu (*Discount Margin*)**|
|---|---|---|
|FRN 1|140 bps|128 bps|
|FRN 2|145 bps|145 bps|
|FRN 3|150 bps|165 bps|



Dựa trên thông tin được cung cấp, hãy xác định FRN nào sẽ được định giá chiết khấu (*at a discount*) vào ngày đặt lại lãi suất (*reset date*) tiếp theo. 

- **A.** FRN 1 

- **B.** FRN 2 

- **C.** FRN 3 

###### **Lời giải:** 

C là đáp án đúng. FRN 3 sẽ được định giá chiết khấu vào ngày đặt lại lãi suất tiếp theo vì biên độ yết giá của nó là 150 bps thấp hơn biên độ chiết khấu là 165 bps. Khoản chiết khấu là giá trị hiện tại của các khoản thanh toán tiền lãi bị thiếu hụt trong tương lai ở mức 15 bps mỗi quý (150 bps – 165 bps). 

B không đúng vì FRN 2 sẽ được định giá ngang mệnh giá vào ngày đặt lại lãi suất tiếp theo do biên độ yết giá của nó bằng với biên độ chiết khấu. 

A không đúng vì FRN 1 sẽ được định giá có phần trội (*at a premium*) bởi vì biên độ yết giá 140 bps của nó lớn hơn biên độ chiết khấu 128 bps. Khoản phần trội là giá trị hiện tại của các khoản thanh toán tiền lãi bổ sung hay “vượt trội” (*“excess”*) ở mức 12 bps mỗi quý (140 bps – 128 bps). 


<!-- PDF Page 199 -->

2. Vào ngày đặt lại lãi suất (*reset date*), nếu biên độ yêu cầu (*required margin*) giảm xuống 30 bps do sự thay đổi trong rủi ro tín dụng của tổ chức phát hành, một FRN có biên độ yết giá (*quoted margin*) là 50 bps sẽ được định giá ở mức: 

   - **A.** chiết khấu (*discount*). 

   - **B.** phần trội (*premium*). 

   - **C.** chiết khấu hoặc phần trội, tùy thuộc vào thời lượng (*duration*) của nó. 

   - **Lời giải:** 

B là đáp án đúng. Biên độ yêu cầu phản ánh rủi ro tín dụng của tổ chức phát hành. Nó đã giảm xuống, có nghĩa là rủi ro tín dụng của tổ chức phát hành đã được cải thiện; nói cách khác, thị trường đòi hỏi một mức chênh lệch thấp hơn. Biên độ yêu cầu thấp hơn biên độ yết giá, vì vậy trái phiếu lãi suất thả nổi này sẽ được định giá ở mức phần trội (*at a premium*). 

3. Một chứng chỉ tiền gửi ngân hàng (*bank certificate of deposit*) tính theo năm 365 ngày có số tiền gốc ban đầu là 96,5 triệu USD và số tiền hoàn trả đến hạn khi đáo hạn là 100 triệu USD. Số ngày giữa ngày thanh toán (*settlement*) và ngày đáo hạn (*maturity*) là 270 ngày. Lãi suất cộng thêm (*add-on rate*) của chứng chỉ tiền gửi này gần nhất với mức: 

   - **A.** 3,63%. 

   - **B.** 4,82%. 

   - **C.** 4,90%. 

**Lời giải:** 

C là đáp án đúng. Lãi suất cộng thêm gần nhất với mức 4,90%. Lãi suất cộng thêm (*AOR*) được tính như sau: 

![](assets/Fixed_Income.pdf-0199-14.png)

<!-- Formula Text: AOR  =   Year _ Days  ×  FV − PV _ PV  . AOR  =   365 _ 270  ×  100 − 96.5 _ 96.5 . -->
$$AOR = \frac{\text{Year}}{\text{Days}} \times \frac{FV - PV}{PV}$$
$$AOR = \frac{365}{270} \times \frac{100 - 96.5}{96.5}$$

$AOR = 0.04903 = 4.90\%$. 

4. Một công cụ thương phiếu (*commercial paper*) kỳ hạn 90 ngày được yết ở mức lãi suất chiết khấu (*discount rate*) là 0,120%, giả định một năm có 360 ngày. Cho biết giá của công cụ được thanh toán trên mỗi 100 đơn vị mệnh giá, lợi suất tương đương trái phiếu (*bond equivalent yield*) của nó gần nhất với mức: 

   - **A.** 0,107%. 

   - **B.** 0,120%. 

   - **C.** 0,135%. 

   - **Lời giải:** 

B là đáp án đúng. Lợi suất tương đương trái phiếu gần nhất với mức 0,120%. Trước tiên, chúng ta cần tính giá của công cụ. Sau đó, chúng ta có thể tính AOR hoặc lợi suất tương đương trái phiếu của nó. 

Giá ($PV$) của công cụ thương phiếu là: 

$$PV = FV \times \left(1 - \frac{\text{Days}}{\text{Year}} \times DR\right)$$
$$PV = 100 \times \left(1 - \frac{90}{360} \times 0.0012\right)$$
$$PV = 99.97$$

$PV$ được sử dụng để tính lãi suất cộng thêm (*add-on rate*) hoặc lợi suất tương đương trái phiếu (*bond equivalent yield*): 


<!-- PDF Page 200 -->

![](assets/Fixed_Income.pdf-0200-02.png)

<!-- Formula Text: AOR  =   Year _ Days  ×  FV − PV _ PV  . AOR  =   360 _ 90  ×  100 − 99.97 _ 99.97 . -->
$$AOR = \frac{\text{Year}}{\text{Days}} \times \frac{FV - PV}{PV}$$
$$AOR = \frac{360}{90} \times \frac{100 - 99.97}{99.97}$$

$AOR = 0.0012 = 0.12\%$. 

5. Một chuyên viên phân tích thu nhập cố định đang đánh giá hai công cụ: 

- Một chứng chỉ tiền gửi ngân hàng (*certificate of deposit* – CD) Thái Lan kỳ hạn 180 ngày được yết ở mức lãi suất chiết khấu 5,95%, giả định một năm có 360 ngày và lợi suất tương đương trái phiếu (*bond equivalent yield*) là 6,218% 

- Một thương phiếu doanh nghiệp (*commercial paper* – CP) Thái Lan kỳ hạn 180 ngày được yết dưới dạng lãi suất cộng thêm 6,10%, giả định một năm có 365 ngày và lợi suất tương đương trái phiếu là 6,100%. 

Giả sử tín phiếu Kho bạc (*T-bill*) Thái Lan kỳ hạn 6 tháng được yết ở mức 4,36%, công cụ nào _nhiều khả năng nhất_ có rủi ro tín dụng cao hơn? 

###### **Lời giải:** 

Chứng chỉ tiền gửi (CD) của ngân hàng Thái Lan. Mức chênh lệch (*spread*) so với tín phiếu Kho bạc Thái Lan đối với CD và CP lần lượt là 186 bps và 174 bps. Chúng ta sử dụng thước đo lợi suất tương đương trái phiếu (*bond equivalent yield*) để so sánh tỷ suất sinh lợi của từng công cụ và suy ra mức chênh lệch của từng công cụ so với tín phiếu Kho bạc Thái Lan. 

CD ngân hàng Thái Lan có mức chênh lệch là: 

6,218% – 4,36% = 186 bps. 

Và CP doanh nghiệp Thái Lan có mức chênh lệch là: 

- 6,10% – 4,36% = 174 bps. 

Do đó, CD ngân hàng Thái Lan có rủi ro tín dụng cao hơn so với CP doanh nghiệp Thái Lan. 

## **<mark>2</mark>** 

##### **CÁC THƯỚC ĐO LỢI SUẤT VÀ CHÊNH LỆCH LỢI SUẤT ĐỐI VỚI TRÁI PHIẾU LÃI SUẤT THẢ NỔI (*YIELD AND YIELD SPREAD MEASURES FOR FLOATING-RATE NOTES*)** 

tính toán và diễn giải các thước đo chênh lệch lợi suất đối với các công cụ lãi suất thả nổi 

###### **Các Thước đo Lợi suất và Chênh lệch Lợi suất đối với Công cụ Lãi suất Thả nổi (*Yield and Yield Spread Measures for Floating-Rate Instruments*)** 

Các công cụ lãi suất thả nổi (*floating-rate instruments*), bao gồm trái phiếu lãi suất thả nổi (*floating-rate notes* – FRNs hoặc *floaters*) và hầu hết các khoản vay, khác với trái phiếu lãi suất cố định. Thay vì các khoản thanh toán coupon cố định, chúng thay đổi từ kỳ này sang kỳ khác tùy thuộc vào mức lãi suất tham chiếu hiện hành. Mục đích là vừa tự động điều chỉnh lãi suất cơ sở của bên đi vay theo các điều kiện thị trường, vừa mang lại cho nhà đầu tư hoặc bên cho vay ít rủi ro giá hơn khi lãi suất thị trường biến động. Về 


<!-- PDF Page 201 -->

nguyên tắc, một trái phiếu lãi suất thả nổi có mức giá ổn định ngay cả trong giai đoạn lãi suất biến động mạnh bởi vì các dòng tiền tự điều chỉnh theo những thay đổi của lãi suất. Với một chứng khoán thu nhập cố định truyền thống, các dòng tiền tương lai không đổi dẫn đến sự thay đổi giá để phản ứng lại sự biến động của lãi suất. 

Bảng 1 hiển thị bản điều khoản tóm tắt (*term sheet*) cho các FRN kỳ hạn 4 năm được phát hành bởi Antelas AG, công ty công nghệ mới nổi của Đức tập trung vào thiết kế quy trình sản xuất, đã được giới thiệu trong một bài học trước. 

**Bảng 1: Đợt phát hành Trái phiếu Lãi suất Thả nổi của Antelas AG (*Exhibit 1: Antelas AG Floating-Rate Note Issue*)** 

|**Antelas AG**|**Trái phiếu Lãi suất Thả nổi Kỳ hạn 4 năm (“Trái phiếu”)**<br>**Tóm tắt Bản cáo bạch (*Prospectus Summary*)**|
|---|---|
|**Tổ chức phát hành (*Issuer*):**|Antelas AG|
|**Ngày thanh toán (*Settlement Date*):**|[T + 5 Ngày làm việc]|
|**Ngày đáo hạn (*Maturity Date*):**|[Bốn năm kể từ Ngày thanh toán]|
|**Số tiền gốc (*Principal Amount*):**|250 triệu EUR|
|**Tiền lãi (*Interest*):**|MRR cộng 250 bps mỗi năm (p.a.)|
|**Thanh toán tiền lãi (*Interest Payment*):**|MRR được đặt lại hàng quý và tiền lãi được trả hàng quý<br>Bắt đầu từ ba tháng kể từ [Ngày thanh toán], được trả<br>hàng quý với khoản thanh toán cuối cùng vào [Ngày đáo hạn]|
|**Thứ tự ưu tiên (*Seniority*):**|Trái phiếu là nghĩa vụ nợ có bảo đảm và không thứ cấp (*secured and unsubordinated*) của<br>Antelas AG và sẽ xếp ngang hàng (*pari passu*) với tất cả các khoản nợ có bảo đảm và<br>không thứ cấp khác|
|**Ngày làm việc (*Business Days*):**|Frankfurt|



Hãy chú ý cách tiền lãi được ghi là “MRR cộng 250 bps mỗi năm (p.a.)”. Lãi suất tham chiếu thị trường (*market reference rate* – MRR) trên một FRN hoặc khoản vay thường là một lãi suất thị trường tiền tệ ngắn hạn. Thông thường, lãi suất tham chiếu được xác định vào đầu kỳ, và khoản thanh toán tiền lãi được thực hiện vào cuối kỳ. Cấu trúc thanh toán này được gọi là trả sau (*“in arrears”*). Các quy ước đếm ngày phổ biến nhất để tính lãi tích lũy (*accrued interest*) trên các trái phiếu lãi suất thả nổi là thực tế/360 (*actual/360*) và thực tế/365 (*actual/365*). Đối với FRN của Antelas, MRR được đặt lại hàng quý và tiền lãi được trả hàng quý. 

Đối với hầu hết các FRN và khoản vay, một mức chênh lệch xác định được cộng vào hoặc trừ đi khỏi lãi suất tham chiếu thị trường. Đối với FRN của Antelas, mức chênh lệch trên MRR là 250 bps, và đây được gọi là **biên độ yết giá (*quoted margin*)** trên FRN. Vai trò của biên độ yết giá là bù đắp cho nhà đầu tư phần chênh lệch giữa rủi ro tín dụng của tổ chức phát hành và rủi ro tín dụng hàm ý trong lãi suất tham chiếu. Các doanh nghiệp có rủi ro tín dụng rất thấp có thể đạt được mức biên độ yết giá âm. 

**Biên độ yêu cầu (*required margin*)** là mức chênh lệch lợi suất cao hơn hoặc thấp hơn lãi suất tham chiếu sao cho FRN được định giá ngang mệnh giá (*at par value*) vào ngày đặt lại lãi suất (*rate reset date*). Nó được quyết định bởi thị trường. Giả sử một trái phiếu lãi suất thả nổi được phát hành ngang mệnh giá và trả lãi MRR cộng 0,50%. Biên độ yết giá là 50 bps. Nếu không có sự thay đổi nào trong rủi ro tín dụng của tổ chức phát hành, biên độ yêu cầu vẫn giữ ở mức 50 bps. Vào mỗi ngày đặt lại lãi suất hàng quý, trái phiếu lãi suất thả nổi sẽ được định giá ngang mệnh giá. Giữa các ngày trả coupon, giá tịnh (*flat price*) của nó sẽ ở mức phần trội (*premium*) hoặc chiết khấu (*discount*) so với mệnh giá nếu MRR tương ứng giảm xuống hoặc tăng lên. Tuy nhiên, nếu biên độ yêu cầu tiếp tục bằng với biên độ yết giá, giá tịnh sẽ được “kéo về mệnh giá” (*“pulled to par”*) khi ngày đặt lại lãi suất tiếp theo đến gần. Vào ngày đặt lại lãi suất, bất kỳ thay đổi nào trong MRR đều được tính vào khoản thanh toán tiền lãi cho kỳ tiếp theo. 

Những thay đổi trong biên độ yêu cầu thường xuất phát từ những thay đổi trong rủi ro tín dụng của tổ chức phát hành. Những thay đổi về tính thanh khoản hoặc tình trạng thuế cũng có thể ảnh hưởng đến biên độ yêu cầu. Lưu ý rằng đây cũng chính là những yếu tố ảnh hưởng đến chênh lệch lợi suất (*yield spread*) đối với trái phiếu lãi suất cố định. Giả sử vào một ngày đặt lại lãi suất, biên độ yêu cầu tăng lên 75 bps do việc hạ bậc xếp hạng tín nhiệm của tổ chức phát hành. Nếu biên độ yết giá là 50 bps, tổ chức phát hành hiện đang trả cho các 


<!-- PDF Page 202 -->

nhà đầu tư của mình một khoản thanh toán tiền lãi “thiếu hụt” (*“deficient”*). FRN này sẽ được định giá chiết khấu dưới mệnh giá. Giá trị của khoản chiết khấu chính là giá trị hiện tại của các dòng tiền tương lai bị thiếu hụt đó. Chuỗi niên kim (*annuity*) đó là 25 bps mỗi kỳ trong suốt thời gian còn lại của trái phiếu. Đó là phần chênh lệch giữa biên độ yêu cầu và biên độ yết giá. Ngược lại, nếu biên độ yêu cầu giảm xuống 40 bps, có thể do sự sụt giảm rủi ro tín dụng của tổ chức phát hành, thì FRN sẽ được định giá ở mức phần trội (*at a premium*). Giá trị của khoản phần trội là giá trị hiện tại của chuỗi niên kim 10 bp từ khoản thanh toán tiền lãi “vượt trội” (*“excess”*) mỗi kỳ. 

Trái phiếu lãi suất cố định và trái phiếu lãi suất thả nổi về cơ bản là giống nhau xét trên khía cạnh thay đổi rủi ro tín dụng. Với trái phiếu lãi suất cố định, phần trội hoặc chiết khấu phát sinh từ sự chênh lệch giữa lãi suất coupon cố định và lợi suất đáo hạn yêu cầu (*required yield-to-maturity*). Với trái phiếu lãi suất thả nổi, phần trội hoặc chiết khấu phát sinh từ sự chênh lệch giữa biên độ yết giá cố định và biên độ yêu cầu. Tuy nhiên, trái phiếu lãi suất cố định và trái phiếu lãi suất thả nổi lại rất khác nhau xét trên khía cạnh thay đổi lãi suất chuẩn (*benchmark interest rates*). 

![](assets/Fixed_Income.pdf-0202-04.png)

<!-- Formula Text: The valuation of a floating-rate note requires a pricing model. Recall that the price for a fixed-rate bond given a market discount rate r and a coupon per period PMT is PV  =    PMT _ (1 + r) 1  +   PMT _ (1 + r) 2  + ... +  PMT + FV _ (1 + r) N  . -->
Việc định giá một trái phiếu lãi suất thả nổi đòi hỏi một mô hình định giá. Hãy nhớ lại rằng giá của một trái phiếu lãi suất cố định với lãi suất chiết khấu thị trường $r$ và khoản coupon mỗi kỳ $PMT$ là:

$$PV = \frac{PMT}{(1 + r)^1} + \frac{PMT}{(1 + r)^2} + \dots + \frac{PMT + FV}{(1 + r)^N}$$

Đối với một FRN, $PMT$ là một hàm của MRR và biên độ yết giá (*quoted margin*), còn $r$ là một hàm của MRR và biên độ chiết khấu (*discount margin*). Chúng ta có thể sử dụng trực giác này để suy ra Phương trình 1, một mô hình định giá FRN giản lược. 

![](assets/Fixed_Income.pdf-0202-06.png)

<!-- Formula Text: PV  =    (MRR + QM ) × FV ______________ m ____________ (1 +  MRR + DM _ m ) 1 +   (MRR + QM ) × FV ______________ m ____________ (1 +  MRR + DM _ m ) 2 + ... +   (MRR + QM ) × FV ______________ m + FV ________________ (1 +  MRR + DM _ m ) N , (1) -->
$$PV = \frac{\frac{(MRR + QM) \times FV}{m}}{\left(1 + \frac{MRR + DM}{m}\right)^1} + \frac{\frac{(MRR + QM) \times FV}{m}}{\left(1 + \frac{MRR + DM}{m}\right)^2} + \dots + \frac{\frac{(MRR + QM) \times FV}{m} + FV}{\left(1 + \frac{MRR + DM}{m}\right)^N} \tag{1}$$

trong đó: 

- $PV$ = giá trị hiện tại (*present value*), hay giá của trái phiếu lãi suất thả nổi 

- $MRR$ = lãi suất tham chiếu thị trường (*market reference rate*), được biểu thị dưới dạng lãi suất phần trăm năm (đôi khi được gọi chung là Chỉ số – *Index*) 

- $QM$ = biên độ yết giá (*quoted margin*), được biểu thị dưới dạng lãi suất phần trăm năm 

- $FV$ = giá trị tương lai (*future value*) được trả khi đáo hạn, hay mệnh giá (*par value*) của trái phiếu 

- $m$ = định kỳ (*periodicity*) của trái phiếu lãi suất thả nổi, tức số kỳ thanh toán mỗi năm 

- $DM$ = biên độ chiết khấu (*discount margin*) = biên độ yêu cầu (*required margin*) được biểu thị dưới dạng lãi suất phần trăm năm 

- $N$ = số kỳ cách đều nhau cho đến khi đáo hạn 

Lưu ý rằng trong Phương trình 1, bởi vì chúng ta đang sử dụng lãi suất hàng năm cho $MRR$, $QM$, và $DM$, chúng ta phải chia cho $m$ kỳ trong năm. 

Đây là một mô hình giản lược vì một số lý do. Thứ nhất, $PV$ được tính tại một ngày đặt lại lãi suất (*rate reset date*) khi có $N$ kỳ cách đều nhau cho đến khi đáo hạn. Không có lãi tích lũy (*accrued interest*), vì vậy giá tịnh (*flat price*) cũng chính là giá toàn phần (*full price*). Thứ hai, mô hình giả định quy ước đếm ngày 30/360, nhằm đảm bảo rằng định kỳ $m$ là một số nguyên. Tuy nhiên, trên thực tế, hầu hết các trái phiếu lãi suất thả nổi sử dụng quy ước đếm ngày thực tế/360 (*actual/360*). Thứ ba, và quan trọng nhất, cùng một mức $MRR$ được sử dụng cho tất cả các dòng tiền. Các mô hình định giá FRN phức tạp hơn sử dụng lãi suất dự phóng trong tương lai ở tử số và lãi suất giao ngay (*spot rates*) ở mẫu số. Do đó, phép tính cho $DM$ phụ thuộc vào các giả định giản lược trong mô hình định giá. 


<!-- PDF Page 203 -->

Giả sử chúng ta đang định giá một FRN trả lãi nửa năm một lần, kỳ hạn 2 năm, trả lãi bằng MRR cộng 0,50%. Giả sử MRR là 1,25% và mức chênh lệch lợi suất được các nhà đầu tư yêu cầu là 40 bps. Đối với Phương trình 1, chúng ta có các thông số đầu vào sau: 

$MRR = 0.0125$, 

$QM = 0.0050$, $FV = 100$, $m = 2$, 

$DM = 0.0040$, và 

$N = 4$. 

Sử dụng Phương trình 1 với $N = 4$, FRN được định giá ở mức 100,196 trên mỗi 100 đơn vị mệnh giá. Trái phiếu lãi suất thả nổi này được định giá ở mức phần trội (*at a premium*) cao hơn mệnh giá bởi vì biên độ yết giá lớn hơn biên độ chiết khấu. 

![](assets/Fixed_Income.pdf-0203-08.png)

<!-- Formula Text: PV  =    (MRR + QM ) × FV ______________ m ____________ (1 +  MRR + DM _ m ) 1 +   (MRR + QM ) × FV ______________ m ____________ (1 +  MRR + DM _ m ) 2 + ... +   (MRR + QM ) × FV ______________ m + FV ________________ (1 +  MRR + DM _ m ) N . PV  = (0.0125 + 0.0050 ) × 100 _________________ 2 _______________ (1 +  0.0125 + 0.0040 ____________ 2 ) 1 + (0.0125 + 0.0050 ) × 100 _________________ 2 _______________ (1 +  0.0125 + 0.0040 ____________ 2 ) 2 + (0.0125 + 0.0050 ) × 100 _________________ 2 _______________ (1 +  0.0125 + 0.0040 ____________ 2 ) 3 + (0.0125 + 0.0050 ) × 100 _________________ 2 + 100 ____________________ (1 +  0.0125 + 0.0040 ____________ 2 ) 4 -->
$$PV = \frac{\frac{(MRR + QM) \times FV}{m}}{\left(1 + \frac{MRR + DM}{m}\right)^1} + \frac{\frac{(MRR + QM) \times FV}{m}}{\left(1 + \frac{MRR + DM}{m}\right)^2} + \dots + \frac{\frac{(MRR + QM) \times FV}{m} + FV}{\left(1 + \frac{MRR + DM}{m}\right)^N}$$
$$PV = \frac{\frac{(0.0125 + 0.0050) \times 100}{2}}{\left(1 + \frac{0.0125 + 0.0040}{2}\right)^1} + \frac{\frac{(0.0125 + 0.0050) \times 100}{2}}{\left(1 + \frac{0.0125 + 0.0040}{2}\right)^2} + \frac{\frac{(0.0125 + 0.0050) \times 100}{2}}{\left(1 + \frac{0.0125 + 0.0040}{2}\right)^3} + \frac{\frac{(0.0125 + 0.0050) \times 100}{2} + 100}{\left(1 + \frac{0.0125 + 0.0040}{2}\right)^4}$$

$PV = 100.196$ 

Nếu chúng ta có giá thị trường của một FRN, chúng ta cũng có thể sử dụng Phương trình 1 để ước tính biên độ chiết khấu (*discount margin*). Giả sử một FRN kỳ hạn 2 năm trả lãi MRR cộng 0,75% trên cơ sở nửa năm một lần. Hiện tại, MRR là 1,10% và giá của trái phiếu lãi suất thả nổi này là 95,50 trên mỗi 100 đơn vị mệnh giá, tức chiết khấu so với mệnh giá, do rủi ro tín dụng xấu đi. Đối với Phương trình 1, chúng ta có các thông số đầu vào sau: 

$PV = 95.50$, 

$MRR = 0.0110$, 

$QM = 0.0075$, 

$FV = 100$, 

$m = 2$, và 

$N = 4$. 

Sử dụng công cụ bổ trợ Solver cho Microsoft Excel, chúng ta tìm được $DM = 3.12\%$, hay 312 bps, bằng cách đặt mức giá (tổng giá trị hiện tại của các dòng tiền) bằng 95,50 làm mục tiêu (*objective*) và $DM$ làm biến thay đổi (*change variable*). Vui lòng xem hệ sinh thái học tập dành cho ứng viên trực tuyến để biết bảng tính minh họa phép tính trong sổ làm việc Excel có thể tải xuống. 

Nếu FRN này được phát hành ngang mệnh giá, các nhà đầu tư vào thời điểm đó chỉ yêu cầu mức chênh lệch 75 bps trên MRR. Giờ đây, sau khi bị hạ bậc tín nhiệm, các nhà đầu tư yêu cầu một biên độ chiết khấu _ước tính_ là 312 bps. Trái phiếu lãi suất thả nổi giao dịch ở mức chiết khấu bởi vì biên độ yết giá vẫn giữ cố định ở mức 75 bps, nên bị “thiếu hụt” 237 bps (312 – 75) mỗi kỳ. Biên độ chiết khấu chỉ là một con số ước tính bởi vì nó dựa trên một mô hình định giá FRN giản lược. 

Mô hình định giá FRN trong Phương trình 1 cũng áp dụng tương tự cho các khoản vay có lãi suất điều chỉnh (*adjustable-rate loans*) do các ngân hàng cấp và các công cụ thu nhập cố định khác dựa trên MRR. Bởi vì một phần đáng kể nguồn vốn của ngân hàng đến từ tiền gửi ngắn hạn và các nguồn lãi suất thả nổi 


<!-- PDF Page 204 -->

khác, các ngân hàng ưu tiên cấp các khoản vay lãi suất thả nổi cho các doanh nghiệp và cá nhân, thay vì các khoản vay lãi suất cố định, để giúp duy trì sự cân xứng giữa tài sản và nợ phải trả trên bảng cân đối kế toán. 

###### **VÍ DỤ 1** 

###### **Tính toán Biên độ Chiết khấu cho một Trái phiếu Lãi suất Thả nổi (*Calculating the Discount Margin for a Floating-Rate Note*)** 

Giả sử MRR cho trái phiếu lãi suất thả nổi kỳ hạn 4 năm của Antelas AG được tính trên cơ sở 3 tháng và biên độ yết giá là 250 bps. Trái phiếu lãi suất thả nổi này được định giá ở mức 97 trên mỗi 100 đơn vị mệnh giá. Hãy tính biên độ chiết khấu cho trái phiếu lãi suất thả nổi này với giả định rằng MRR 3 tháng không đổi ở mức –0,55%. Giả định quy ước đếm ngày 30/360 và các kỳ cách đều nhau. 

###### **Lời giải:** 

Chúng ta có thể sử dụng công cụ bổ trợ Solver trong Microsoft Excel để giải nhanh ra $DM = 3.29\%$, hay 329 bps, theo cùng cách thức như trong ví dụ trước. Vui lòng xem hệ sinh thái học tập dành cho ứng viên trực tuyến để biết bảng tính minh họa phép tính trong sổ làm việc Excel có thể tải xuống. 

Ngoài ra, chúng ta có thể sử dụng hàm RATE trong Microsoft Excel, Google Sheets, hoặc máy tính tài chính bằng cách trước tiên giải tìm $PMT$, tức các tử số trong Phương trình 1. 

![](assets/Fixed_Income.pdf-0204-10.png)

<!-- Formula Text: PMT  =   (MRR + QM ) × FV ______________ m . PMT  =   (− 0.0055 + 0.0250 ) × 100 ___________________ 4 . PMT  =  0.4875. -->
$$PMT = \frac{(MRR + QM) \times FV}{m}$$
$$PMT = \frac{(-0.0055 + 0.0250) \times 100}{4}$$
$$PMT = 0.4875$$

Sau đó, sử dụng $PV = -97$, $FV = 100$, $PMT = 0.4875$, và $N = 16$, chúng ta có thể giải tìm lãi suất chiết khấu mỗi kỳ là 0,686122%. Chúng ta sử dụng con số này để giải tìm $DM$:

$$r = \frac{MRR + DM}{m}$$

![](assets/Fixed_Income.pdf-0204-12.png)

<!-- Formula Text: 0.00686122  =   − 0.0055 + DM ___________ 4 . -->
$$0.00686122 = \frac{-0.0055 + DM}{4}$$

![](assets/Fixed_Income.pdf-0204-13.png)

<!-- Formula Text: DM  =  0.0329  =  3.29 % . -->
$$DM = 0.0329 = 3.29\%$$

Biên độ yết giá là 250 bps trên lãi suất tham chiếu. Sử dụng mô hình định giá FRN giản lược, biên độ chiết khấu (mức chênh lệch mà các nhà đầu tư yêu cầu để trái phiếu lãi suất thả nổi được định giá ngang mệnh giá) là 329 bps. 

###### **BỘ CÂU HỎI (*QUESTION SET*)** 

![](assets/Fixed_Income.pdf-0204-16.png)

<!-- Formula Text: 1.	 Fill in the blanks using one of the words in each set of parentheses: -->
1. Điền vào chỗ trống bằng cách sử dụng một trong các từ trong mỗi cặp ngoặc đơn:

Các trái phiếu lãi suất thả nổi có kỳ đặt lại lãi suất (*reset periods*) dài hơn có thể chịu __________ (nhiều hơn, ít hơn) rủi ro biến động lãi suất và biến động giá. 


<!-- PDF Page 205 -->

Kỳ đặt lại lãi suất càng __________ (ngắn hơn, dài hơn), trái phiếu lãi suất thả nổi sẽ càng hoạt động giống với một chứng khoán lãi suất cố định ngắn hạn và giá của nó sẽ có khả năng biến động __________ (ít hơn, nhiều hơn). **Lời giải:** Các trái phiếu lãi suất thả nổi có kỳ đặt lại lãi suất dài hơn có thể chịu _<u>nhiều hơn</u>_ (*more*) rủi ro biến động lãi suất và biến động giá. Kỳ đặt lại lãi suất càng _<u>dài hơn</u>_ (*longer*), trái phiếu lãi suất thả nổi sẽ càng hoạt động giống với một chứng khoán lãi suất cố định ngắn hạn và giá của nó sẽ có khả năng biến động _<u>nhiều hơn</u>_ (*more*). 

|2. Đối với một chứng khoán lãi suất thả nổi kỳ hạn 5 năm, nếu lãi suất thị trường thay đổi 0,5%,<br>thay đổi trong giá của chứng khoán đó nhiều khả năng nhất sẽ:|
|---|
|**A.** bằng không.|
|**B.** giống như một chứng khoán lãi suất cố định tương tự về mọi mặt khác.<br>**C.** liên quan đến tần suất đặt lại coupon (*coupon reset frequency*) của chứng khoán đó.<br>**Lời giải:**<br>C là đáp án đúng. Độ nhạy cảm với lãi suất của một chứng khoán lãi suất thả nổi<br>thường xuất phát từ thời gian còn lại cho đến ngày đặt lại coupon tiếp theo của nó.<br>A không đúng: khi lãi suất thay đổi, lãi suất chiết khấu của<br>chứng khoán lãi suất thả nổi cũng thay đổi, làm thay đổi giá trị hiện tại của chứng khoán<br>khi chiết khấu các dòng tiền.<br>B không đúng: với một chứng khoán lãi suất cố định, những thay đổi về lãi suất ảnh hưởng đến<br>giá nhiều hơn so với một chứng khoán lãi suất thả nổi tương tự (cùng kỳ hạn), do<br>các khoản thanh toán coupon cố định và thời lượng (*duration*) cao hơn của nó.|
|3. Xác định mối quan hệ giữa biên độ yêu cầu (*required margin*) và giá của một trái phiếu lãi suất thả nổi vào<br>ngày đặt lại lãi suất (*reset date*):|
|1. Biên độ yêu cầu > Biên độ yết giá (*Required margin > Quoted margin*)<br>A. Trái phiếu lãi suất thả nổi được định giá ngang mệnh giá (*at par*)|
|2. Biên độ yêu cầu = Biên độ yết giá (*Required margin = Quoted margin*)<br>B. Trái phiếu lãi suất thả nổi được định giá chiết khấu (*at a discount*)|
|3. Biên độ yêu cầu < Biên độ yết giá (*Required margin < Quoted margin*)<br>C. Trái phiếu lãi suất thả nổi được định giá ở mức phần trội (*at a premium*)|
|**Lời giải:**|
|1. Biên độ yêu cầu > Biên độ yết giá (*Required margin > Quoted margin*)<br>B. Trái phiếu lãi suất thả nổi được định giá chiết khấu (*at a discount*)|
|2. Biên độ yêu cầu = Biên độ yết giá (*Required margin = Quoted margin*)<br>A. Trái phiếu lãi suất thả nổi được định giá ngang mệnh giá (*at par*)|
|3. Biên độ yêu cầu < Biên độ yết giá (*Required margin < Quoted margin*)<br>C. Trái phiếu lãi suất thả nổi được định giá ở mức phần trội (*at a premium*)|



Đối với Biên độ yêu cầu > Biên độ yết giá, B là đáp án đúng. Những thay đổi trong biên độ yêu cầu thường xuất phát từ những thay đổi trong rủi ro tín dụng của tổ chức phát hành. Nếu biên độ yêu cầu tăng lên và cao hơn biên độ yết giá vào ngày đặt lại lãi suất, trái phiếu lãi suất thả nổi sẽ trả một khoản thanh toán tiền lãi “thiếu hụt”. Trái phiếu lãi suất thả nổi sẽ được định giá chiết khấu dưới mệnh giá. 

Đối với Biên độ yêu cầu = Biên độ yết giá, A là đáp án đúng. Nếu biên độ yêu cầu tiếp tục bằng với biên độ yết giá, giá tịnh sẽ được “kéo về <u>mệnh giá” khi ngày đặt lại lãi suất tiếp theo đến gần.</u> 


<!-- PDF Page 206 -->

Đối với Biên độ yêu cầu < Biên độ yết giá, C là đáp án đúng. Nếu biên độ yêu cầu giảm xuống và thấp hơn biên độ yết giá, trái phiếu lãi suất thả nổi sẽ được định giá ở mức phần trội. 

4. Một trái phiếu lãi suất thả nổi của Ý kỳ hạn 2 năm trả lãi Euribor 3 tháng ở mức –0,50% cộng 250 bp. Trái phiếu lãi suất thả nổi này được định giá ở mức 99 trên mỗi 100 đơn vị mệnh giá. Giả định quy ước đếm ngày 30/360 và các kỳ cách đều nhau, biên độ chiết khấu (*discount margin*) của trái phiếu lãi suất thả nổi này gần nhất với mức: 

- **A.** 201 bps. 

- **B.** 251 bps. 

- **C.** 300 bps. 

###### **Lời giải:** 

C là đáp án đúng. Biên độ chiết khấu của trái phiếu lãi suất thả nổi gần nhất với mức 300 bps. Sử dụng thông tin được cung cấp, khoản thanh toán định kỳ $PMT$ bằng: 

![](assets/Fixed_Income.pdf-0206-09.png)

<!-- Formula Text: (MRR + QM ) × FV ______________ m =   (− 0.005 + 0.0025 ) × 100 __________________ 4 =  0.5. -->
$$\frac{(MRR + QM) \times FV}{m} = \frac{(-0.005 + 0.025) \times 100}{4} = 0.5$$

Sử dụng hàm RATE trong Microsoft Excel, Google Sheets, hoặc máy tính tài chính với $PV = -99$, $FV = 100$, $PMT = 0.5$, và $N = 8$, chúng ta giải tìm lãi suất chiết khấu mỗi kỳ là 0,628562%. Biên độ chiết khấu có thể được ước tính bằng cách giải tìm $DM$: 

![](assets/Fixed_Income.pdf-0206-11.png)

<!-- Formula Text: r  =   MRR + DM _ m . -->
$$r = \frac{MRR + DM}{m}$$

$$0.00628562 = \frac{-0.005 + DM}{4}$$

   - $DM = 0.03014 = 3.014\%$. 

5. Trái phiếu lãi suất thả nổi kỳ hạn 4 năm của Antelas AG trả lãi MRR 3 tháng ở mức –0,55% cộng 250 bps. Trái phiếu lãi suất thả nổi này được định giá ở mức 102 trên mỗi 100 đơn vị mệnh giá. Giả định quy ước đếm ngày 30/360 và các kỳ cách đều nhau, hãy tính biên độ chiết khấu cho trái phiếu lãi suất thả nổi này. 

###### **Lời giải:** 

Biên độ chiết khấu ước tính là 199 bps. 

Sử dụng thông tin được cung cấp, khoản thanh toán định kỳ $PMT$ bằng: 

- $$\frac{(MRR + QM) \times FV}{m} = \frac{(-0.0055 + 0.025) \times 100}{4} = 0.4875$$

Sử dụng hàm RATE trong Microsoft Excel, Google Sheets, hoặc máy tính tài chính với $PV = -102$, $FV = 100$, $PMT = 0.4875$, và $N = 16$, chúng ta giải tìm lãi suất chiết khấu mỗi kỳ là 0,358655%. Biên độ chiết khấu sau đó có thể được ước tính bằng cách giải tìm $DM$: 

$$r = \frac{MRR + DM}{m}$$

$$0.00358655 = \frac{-0.0055 + DM}{4}$$

- $DM = 0.019846 = 1.99\%$. 
