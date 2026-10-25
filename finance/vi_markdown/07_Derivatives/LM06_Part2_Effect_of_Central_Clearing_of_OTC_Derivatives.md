# Tập 7: Công cụ Phái sinh (*Derivatives*)
## Học phần 6: Định giá và Xác định Giá trị của Hợp đồng Tương lai (*Pricing and Valuation of Futures Contracts*)
### Phần 2/2: Tác động của Cơ chế Bù trừ Trung tâm đối với Công cụ Phái sinh OTC (*Effect of Central Clearing of OTC Derivatives*) (Trang PDF 151–156)

---

<!-- PDF Page 151 -->

**Bảng minh họa 5: Độ lệch lồi (*Convexity Bias*)**

![](assets/Derivatives.pdf-0151-03.png)

> **Chú thích hình ảnh:**
> - **Đồ thị bên trái (Giá kỳ hạn lãi suất - *Interest rate forward price*):** Đường cong biểu diễn mối quan hệ thay đổi giá/lợi suất phi tuyến tính (*Non-linear price/yield changes*) theo Lợi suất (*Yield (%)*}).
> - **Đồ thị bên phải (Giá tương lai lãi suất - *Interest rate futures price*):** Đường thẳng biểu diễn mối quan hệ thay đổi giá/lợi suất tuyến tính (*Linear price/yield changes*) theo Lợi suất (*Yield (%)*).

Tính năng chiết khấu của hợp đồng FRA, vốn không hiện diện trong hợp đồng tương lai, dẫn đến một độ lệch lồi (*convexity bias*) càng lớn đối với các kỳ chiết khấu càng dài. Bạn sẽ nhớ lại từ bài học trước rằng hệ số chiết khấu (*discount factor*) là đại lượng tương đương về mặt *giá* của một mức lãi suất zero và là giá trị hiện tại của một đơn vị tiền tệ vào một ngày trong tương lai, mà cũng có thể được hiểu là mức giá của một dòng tiền hoặc trái phiếu không trả lãi định kỳ. Sau này chúng ta sẽ chỉ ra cách thức hệ số chiết khấu này được sử dụng để định giá các hợp đồng hoán đổi lãi suất và những công cụ phái sinh khác.

#### **TÁC ĐỘNG CỦA CƠ CHẾ BÙ TRỪ TRUNG TÂM ĐỐI VỚI CÔNG CỤ PHÁI SINH OTC (*EFFECT OF CENTRAL CLEARING OF OTC DERIVATIVES*)**

# **<mark>7</mark>**

*Giải thích tại sao giá kỳ hạn và giá tương lai lại khác nhau.*

Trong những giai đoạn căng thẳng tài chính của thị trường và/hoặc của đối tác, các biến động giá lớn kết hợp với việc một đối tác phái sinh mất khả năng đáp ứng lệnh gọi ký quỹ bổ sung (*margin call*) có thể buộc phải đóng vị thế (*closeout*) của một giao dịch hợp đồng tương lai trước khi đáo hạn. Tuy nhiên, một hợp đồng kỳ hạn OTC với các điều khoản tín dụng linh hoạt hơn vẫn có thể tiếp tục được duy trì.

Sự ra đời của cơ chế bù trừ trung tâm đối với công cụ phái sinh (*derivatives central clearing*), đã được giới thiệu trong một bài học trước, đã tạo ra những yêu cầu ký quỹ giống như hợp đồng tương lai đối với các nhà tạo lập thị trường công cụ phái sinh OTC (*OTC derivative dealers*) chuyên mua và bán hợp đồng kỳ hạn với những người sử dụng cuối cùng của công cụ phái sinh (*derivatives end users*). Các nhà tạo lập thị trường bị bắt buộc phải nộp tiền mặt hoặc các chứng khoán có tính thanh khoản cao cho một đối tác trung tâm (*central counterparty* – CCP) thường áp đặt những yêu cầu tương tự lên những người sử dụng cuối cùng của công cụ phái sinh. Những yêu cầu ký quỹ từ phía nhà tạo lập thị trường này làm giảm bớt sự khác biệt trong tác động dòng tiền giữa các công cụ phái sinh giao dịch trên sàn và công cụ phái sinh OTC. Thỏa thuận này giữa các nhà tạo lập thị trường và đối tác của họ, được thể hiện trong Bảng minh họa 6, đã được bổ sung thêm vào sơ đồ bù trừ trung tâm ban đầu từ bài học trước.

**Bảng minh họa 6: Yêu cầu Ký quỹ đối với các Công cụ Phái sinh OTC Được Bù trừ Trung tâm (*Margin Requirements for Centrally Cleared OTC Derivatives*)**

![](assets/Derivatives.pdf-0151-11.png)

> **Chú thích hình ảnh:**
> Những người sử dụng cuối cùng của công cụ phái sinh (*Derivatives end users*) nộp Ký quỹ (*Margin*) cho Định chế tài chính trung gian (*Financial intermediary*), và Định chế tài chính trung gian lại nộp Ký quỹ (*Margin*) cho Đối tác trung tâm (*Central counterparty – CCP*).


<!-- PDF Page 152 -->

Do đó, các nhà đầu tư tích cực sử dụng cả hợp đồng tương lai giao dịch trên sàn hoặc hợp đồng kỳ hạn OTC bắt buộc phải duy trì đủ lượng tiền mặt hoặc tài sản thế chấp đủ điều kiện (*eligible collateral*) để đáp ứng các yêu cầu ký quỹ hoặc thế chấp. Những người tham gia thị trường cũng phải cân nhắc đến các chi phí tài trợ (*financing*), chi phí giao dịch (*transaction*), và chi phí hành chính (*administrative costs*) của việc duy trì các vị thế này khi sử dụng công cụ phái sinh trong một danh mục đầu tư.

###### **BỘ CÂU HỎI (*QUESTION SET*)**

##### **Giá Kỳ hạn và Giá Tương lai (*Forward and Futures Prices*)**

1. Hãy xác định phát biểu sau đây là đúng hay sai và giải thích câu trả lời của bạn: Nếu giá hợp đồng tương lai có tương quan dương với lãi suất, các hợp đồng mua tương lai (*long futures contracts*) sẽ hấp dẫn hơn so với các vị thế mua kỳ hạn (*long forward positions*) đối với cùng một tài sản cơ sở và cùng kỳ hạn.

###### **Lời giải:**

Phát biểu này là đúng. Nếu giá hợp đồng tương lai tăng lên khi lãi suất tăng lên, người nắm giữ vị thế mua hợp đồng tương lai có thể tái đầu tư các khoản lợi nhuận từ hợp đồng tương lai ở các mức lãi suất cao hơn.

2. Một nhà đầu tư tìm cách phòng ngừa rủi ro lãi suất MRR kỳ hạn ba tháng trên một khoản nợ phải trả trị giá $£25,000,000$ phát sinh sau hai tháng nữa và quan sát thấy mức lãi suất kỳ hạn ngầm định ngày hôm nay ($\text{IFR}_{2\text{m},3\text{m}}$) là $2.95\%$. Hãy tính các số tiền tất toán nếu nhà đầu tư tham gia vào một vị thế mua FRA trả lãi cố định (nhận lãi thả nổi) và một vị thế bán hợp đồng tương lai (*short futures contract*), đồng thời so sánh và diễn giải kết quả nếu lãi suất $\text{MRR}_{2\text{m},3\text{m}}$ được ấn định ở mức $3.25\%$.

   - **Lời giải:**

Giải tìm giá trị Tất toán bằng tiền mặt ($\text{PV}$) của hợp đồng FRA trả lãi cố định như sau:

$$\text{Khoản thanh toán ròng} = (\text{MRR}_{B-A} - \text{IFR}_{A,B-A}) \times \text{Vốn gốc Danh nghĩa} \times \text{Kỳ hạn}$$

$$= £18,750 \quad (= [3.25\% - 2.95\%] \times £25,000,000 \times [1/4])$$

Giá trị hiện tại dựa trên lãi suất $\text{MRR}_{2\text{m},3\text{m}}$ ở mức $3.25\%$ là:

$$= £18,598.88 \quad (= £18,750 / [1 + 0.0325/4])$$

Đối với hợp đồng tương lai, giá trị BPV của hợp đồng bằng:

$$\text{BPV Hợp đồng} = £625 \quad (= £25,000,000 \times 0.01\% \times [1/4])$$

Đối với mức tăng $30\text{ điểm cơ bản}$ của lãi suất MRR ($= 3.25\% - 2.95\%$), vị thế bán hợp đồng tương lai sẽ hiện thực hóa một khoản lãi là $£18,750$ ($= £625 \times 30$). Cả hai hợp đồng đều mang lại một khoản lãi xét dưới góc độ của nhà đầu tư khi lãi suất MRR tăng lên. Tuy nhiên, khoản thanh toán của hợp đồng tương lai lớn hơn do khoản thanh toán cuối cùng của hợp đồng FRA bị chiết khấu về ngày tất toán (đầu kỳ tính lãi).

3. Hãy giải thích tại sao các hợp đồng bán tương lai (*short futures contracts*) lại hấp dẫn hơn so với các vị thế bán kỳ hạn (*short forward positions*) nếu giá hợp đồng tương lai có tương quan âm với lãi suất đối với các vị thế có cùng tài sản cơ sở và cùng kỳ hạn.

###### **Lời giải:**

Lý do khiến các hợp đồng bán tương lai hấp dẫn hơn so với các vị thế bán kỳ hạn nếu giá hợp đồng tương lai có tương quan âm với lãi suất là bởi vì mức giá giảm xuống dẫn đến các khoản lợi nhuận từ vị thế bán hợp đồng tương lai được đem đi tái đầu tư trong những giai đoạn lãi suất đang tăng cao, và mức giá tăng lên dẫn đến các khoản lỗ phát sinh trong những giai đoạn lãi suất đang giảm thấp (chi phí tài trợ thấp).


<!-- PDF Page 153 -->

4. Hãy xác định phát biểu sau đây là đúng hay sai và giải thích câu trả lời của bạn: Độ lệch lồi (*convexity bias*) giữa hợp đồng tương lai lãi suất và hợp đồng kỳ hạn lãi suất khiến cho mức thay đổi giá tính theo phần trăm (xét theo giá trị tuyệt đối) khi lãi suất MRR tăng lên thì lớn hơn so với khi nó giảm xuống đối với một hợp đồng kỳ hạn so với một hợp đồng tương lai.

###### **Lời giải:**

Phát biểu này là sai. Độ lệch lồi giữa hợp đồng tương lai lãi suất và hợp đồng kỳ hạn lãi suất khiến cho mức thay đổi giá tính theo phần trăm (xét theo giá trị tuyệt đối) khi lãi suất MRR *giảm xuống* thì lớn hơn so với khi nó *tăng lên* đối với một hợp đồng kỳ hạn, trái ngược với mối quan hệ tuyến tính của một hợp đồng tương lai.

5. Hãy giải thích cách thức mà cơ chế bù trừ trung tâm của các công cụ phái sinh làm giảm bớt sự khác biệt giữa giá tương lai và giá kỳ hạn đối với cùng một tài sản cơ sở và cùng kỳ hạn đáo hạn.

###### **Lời giải:**

Cơ chế bù trừ trung tâm của các công cụ phái sinh đã tạo ra những yêu cầu ký quỹ giống như hợp đồng tương lai đối với các nhà tạo lập thị trường công cụ phái sinh OTC chuyên mua và bán hợp đồng kỳ hạn với những người sử dụng cuối cùng của công cụ phái sinh. Các nhà tạo lập thị trường bị bắt buộc phải nộp tiền mặt hoặc các chứng khoán có tính thanh khoản cao cho một đối tác trung tâm thường áp đặt những yêu cầu tương tự lên những người sử dụng cuối cùng của công cụ phái sinh. Thỏa thuận này giữa các nhà tạo lập thị trường phái sinh và đối tác của họ sẽ làm giảm bớt sự khác biệt trong tác động dòng tiền của các công cụ phái sinh ETD và OTC. Do đó, bất kỳ sự chênh lệch giá nào giữa hợp đồng tương lai ETD và hợp đồng kỳ hạn OTC đều sẽ được thu hẹp lại.


<!-- PDF Page 154 -->

## **BÀI TẬP THỰC HÀNH (*PRACTICE PROBLEMS*)**

### **Thông tin sau đây liên quan đến các câu hỏi từ 1 đến 4**

Ace Limited là một định chế tài chính trung gian hoạt động tích cực trên cả thị trường hợp đồng tương lai lẫn thị trường hợp đồng kỳ hạn. Bạn đã được thuê làm chuyên gia tư vấn đầu tư và được yêu cầu rà soát các hoạt động của Ace cũng như trả lời những câu hỏi sau đây.

**1.** Ace đóng vai trò là một tổ chức môi giới hoa hồng hợp đồng tương lai (*futures commission merchant* – FCM) nhằm hỗ trợ một số khách hàng là các nhà tư vấn giao dịch hàng hóa (*commodity trading advisers* – CTAs) của mình trong việc bù trừ và tất toán các vị thế ký quỹ hợp đồng tương lai của họ với sở giao dịch hợp đồng tương lai. Ace đang rà soát thị trường hợp đồng tương lai đồng (*copper futures*) cho một khách hàng CTA đang cân nhắc thiết lập vị thế mua hợp đồng tương lai đồng lần đầu tiên. Thông tin chi tiết về thị trường hợp đồng tương lai đồng như sau:

|**Hợp đồng Tương lai Đồng CME (*CME Copper Futures*)**|**Đặc điểm Kỹ thuật của Hợp đồng (*Contract Specifications*)**|
|---|---|
|**Kỳ hạn Hợp đồng (*Contract Maturities*):**|Hàng tháng [từ 1 tháng đến 15 tháng]|
|**Quy mô Hợp đồng (*Contract Size*):**|$25,000\text{ pound}$|
|**Loại hình Giao hàng (*Delivery Type*):**|Tất toán bằng tiền mặt (*Cash settled*)|
|**Yết giá (*Price Quotation*):**|\$ trên mỗi pound|
|**Ký quỹ Ban đầu (*Initial Margin*):**|$\$10,000$ cho mỗi hợp đồng|
|**Ký quỹ Duy trì (*Maintenance Margin*):**|$\$6,000$ cho mỗi hợp đồng|
|**Đáo hạn Cuối cùng (*Final Maturity*):**|Ngày làm việc cuối cùng của CME trong tháng hợp đồng|
|**Tất toán Hàng ngày (*Daily Settlement*):**|Bộ phận Vận hành Giao dịch CME tính toán các giá trị thanh toán hàng ngày dựa trên quy trình đã công bố của sở|

Giá đồng giao ngay ngày hôm nay là $\$4.25$ mỗi pound, và lãi suất phi rủi ro không đổi là $1.875\%$. Mỗi hợp đồng có chi phí lưu kho là $\$10$ phải trả vào cuối tháng. Phát biểu nào sau đây mô tả đúng nhất cấu trúc rủi ro ký quỹ của khách hàng CTA của Ace nếu khách hàng này tham gia vào một hợp đồng tương lai đồng kỳ hạn một tháng?

   - **A.** Khách hàng CTA sẽ được kỳ vọng phải nộp $\$10,000$ tiền ký quỹ ban đầu và sẽ nhận được lệnh gọi ký quỹ bổ sung (*margin call*) nếu giá hợp đồng tương lai đồng lập tức giảm xuống dưới mức $\$4.10$ mỗi pound hoặc dưới mức giá $\$102,425$ cho mỗi hợp đồng.

   - **B.** Khách hàng CTA sẽ được kỳ vọng phải nộp $\$10,000$ tiền ký quỹ ban đầu và sẽ nhận được lệnh gọi ký quỹ bổ sung tại bất kỳ thời điểm nào trong suốt vòng đời của hợp đồng nếu giá hợp đồng tương lai đồng lập tức giảm xuống dưới mức $\$3.86$ mỗi pound hoặc dưới mức giá $\$96,425$ cho mỗi hợp đồng.

   - **C.** Khách hàng CTA sẽ được kỳ vọng phải nộp $\$10,000$ tiền ký quỹ ban đầu, nhưng chúng ta không thể xác định được mức giá hợp đồng tương lai chính xác mà tại đó lệnh gọi ký quỹ bổ sung sẽ xảy ra vì giá trị MTM của hợp đồng tương lai được tất toán mỗi ngày và giá trị hợp đồng được thiết lập lại về bằng không.

**2.** Một trong những khách hàng đầu tư của Ace đã tham gia vào một giao dịch mua kỳ hạn sáu tháng với Ace đối với $100$ cổ phiếu của Xenaliya (XLYA), một cổ phiếu công nghệ không trả cổ tức. Giá giao ngay trên mỗi cổ phiếu của mã này, $S_0$, là $€85$, và lãi suất phi rủi ro là hằng số $1\%$ cho mọi kỳ hạn. Ace đã phòng ngừa rủi ro cho giao dịch khách hàng này bằng một vị thế mua


<!-- PDF Page 155 -->

hợp đồng tương lai XLYA kỳ hạn sáu tháng tại mức giá $f_0(T)$ là $€85.42$ và đã nộp khoản ký quỹ ban đầu là $€1,000$. Ba tháng sau khi hợp đồng kỳ hạn và hợp đồng tương lai được khởi tạo, XLYA công bố mối quan hệ đối tác chiến lược với một tập đoàn công nghệ toàn cầu lớn, và giá cổ phiếu giao ngay của hãng tăng vọt thêm $€15$ trong ngày giao dịch đó để đóng cửa ở mức $€123$. Phát biểu nào sau đây mô tả đúng nhất tác động của phiên giao dịch ngày hôm đó lên giá trị MTM của hợp đồng kỳ hạn so với hợp đồng tương lai?

- **A.** Khách hàng của Ace hiện thực hóa một khoản lãi MTM xấp xỉ $€1,500$ ($= €15 \times 100$) trên tài khoản ký quỹ của mình, mà Ace bắt buộc phải nộp vào cuối ngày để đáp ứng lệnh gọi ký quỹ bổ sung.

- **B.** Khách hàng của Ace được hưởng lợi từ một khoản lãi MTM chưa thực hiện (*MTM unrealized gain*) trên hợp đồng kỳ hạn của mình với Ace, và Ace có một khoản lãi MTM tương ứng xấp xỉ $€1,500$ ($= €15 \times 100$) được sở giao dịch chuyển vào tài khoản ký quỹ của mình.

- **C.** Bởi vì Ace đã thiết lập một giao dịch phòng ngừa rủi ro cho vị thế mua kỳ hạn của khách hàng đối với cổ phiếu XLYA bằng cách thực hiện một hợp đồng tương lai có các điều khoản khác hoàn toàn giống hệt nhau, nên hai giá trị MTM của hợp đồng bù trừ chính xác cho nhau và không có khoản tiền mặt nào được trao đổi trên cả hai giao dịch.

**3.** Hãy xác định vị thế nào sau đây tương ứng với mô tả nào.

|Vị thế|Mô tả|
|---|---|
|1. Vị thế mua hợp đồng tương lai lãi suất (*Long interest rate futures position*)|A. Dẫn đến một khoản lãi khi lãi suất MRR được ấn định cao hơn mức lãi suất cam kết kỳ hạn ban đầu vào ngày đáo hạn|
|2. Hợp đồng FRA trả lãi cố định (nhận lãi thả nổi) (*Pay fixed (receive floating) FRA contract*)|B. Dẫn đến một khoản lỗ khi lãi suất MRR được ấn định cao hơn mức lãi suất cam kết kỳ hạn ban đầu vào ngày đáo hạn|
|3. Hợp đồng FRA nhận lãi cố định (trả lãi thả nổi) (*Receive fixed (pay floating) FRA contract*)|C. Có một mức giá cam kết kỳ hạn sẽ tăng lên khi lãi suất ngắn hạn giảm xuống|

**4.** Các khách hàng đầu tư của Ace thường sử dụng các giao dịch kỳ hạn OTC mà Ace bắt buộc phải bù trừ thông qua một đối tác trung tâm (*central counterparty*). Phát biểu nào sau đây liên quan đến tác động lên Ace từ việc bù trừ những vị thế này là chính xác nhất?

   - **A.** Nếu các đối tác của Ace tham gia vào các hợp đồng mua kỳ hạn mà giá của chúng có tương quan dương với lãi suất, Ace sẽ phải nộp nhiều tài sản thế chấp hơn cho các đối tác trung tâm so với các hợp đồng tương lai tương tự khác, vì mức giá tăng lên sẽ dẫn đến các khoản lãi MTM của đối tác được tái đầu tư ở mức lãi suất cao hơn.

   - **B.** Nếu các đối tác của Ace tham gia vào các hợp đồng bán kỳ hạn mà giá của chúng có tương quan âm với lãi suất, Ace sẽ phải nộp ít tài sản thế chấp hơn cho các đối tác trung tâm so với các hợp đồng tương lai tương tự khác, vì mức giá giảm xuống sẽ dẫn đến các khoản lãi MTM của đối tác được tái đầu tư ở mức lãi suất cao hơn.

   - **C.** Vì Ace bị bắt buộc phải nộp tài sản thế chấp (tiền mặt hoặc các chứng khoán có tính thanh khoản cao) cho đối tác trung tâm để bù trừ các giao dịch kỳ hạn của khách hàng, nên Ace sẽ phải đối mặt với các yêu cầu ký quỹ tương tự như những yêu cầu của các thị trường hợp đồng tương lai được chuẩn hóa giao dịch trên sàn.


<!-- PDF Page 156 -->

## **LỜI GIẢI (*SOLUTIONS*)**

1. **A là đáp án đúng.** Khách hàng CTA sẽ phải đối mặt với lệnh gọi ký quỹ bổ sung (*margin call*) nếu giá hợp đồng đồng giảm quá $\$4,000$ ($= \$10,000 - \$6,000$), hay $\$0.16$ ($= \$4,000 / 25,000$) trên mỗi pound. Chúng ta có thể giải tìm mức giá mà tại đó CTA nhận được lệnh gọi ký quỹ bổ sung bằng cách trước tiên giải tìm mức giá hợp đồng tương lai ban đầu, $f_0(T)$, khi khởi tạo hợp đồng như sau:

   $$f_0(T) = [S_0 + \text{PV}_0(C)](1 + r)^T$$

   Giải tìm $\text{PV}_0(C)$ cho cả hợp đồng như sau:

   $$\text{PV}_0(C) = \$9.98 \quad (= \$10[1.01875^{-(1/12)}])$$

   Thay $\text{PV}_0(C) = \$9.98$ vào Phương trình 4 để giải tìm $f_0(T)$:

   $$f_0(T) = [(\$4.25 \times 25,000) + \$9.98](1.01875^{1/12})$$

   $$f_0(T) = \$106,425 \text{ cho mỗi hợp đồng } (\approx \$4.257 \text{ mỗi pound})$$

   Vì vậy, $\$106,425 - \$4,000 = \$102,425$ cho mỗi hợp đồng, và $\$4.257 - \$0.16 = \$4.10$ mỗi pound.

   B không đúng vì nó giả định rằng không có mức ký quỹ duy trì (chỉ gọi ký quỹ khi mất hết toàn bộ $\$10,000$), và mặc dù C có thể đúng trong một số hoàn cảnh khi thời gian đã trôi qua nhiều ngày, nhưng sự thay đổi được nêu trong câu A là diễn ra tức thời (*immediately* — xảy ra ngay khi khởi tạo giao dịch).

2. **B là đáp án đúng.** Vị thế mua kỳ hạn của khách hàng đầu tư với Ace được hưởng lợi từ một khoản lãi MTM trên hợp đồng kỳ hạn với Ace, nhưng không có khoản tiền mặt nào được trao đổi cho đến khi đáo hạn. Ace nhận được một khoản tiền chuyển vào tài khoản ký quỹ hợp đồng tương lai của mình bằng đúng khoản lãi MTM hàng ngày của hợp đồng tương lai, mà nếu giá giao ngay và giá tương lai thay đổi một lượng xấp xỉ bằng nhau thì sẽ bằng $€1,500$ ($€15 \times 100$).

3. **1. C là đáp án đúng.** Giá hợp đồng tương lai lãi suất thay đổi hàng ngày dựa trên quy ước yết giá $(100 - \text{lợi suất})$, vì vậy mức giá của nó sẽ tăng lên khi lợi suất giảm xuống và ngược lại. Mức lãi suất cố định trên một hợp đồng FRA không thay đổi trong suốt vòng đời của hợp đồng.
   **2. A là đáp án đúng.** Một bên trả lãi suất cố định (nhận lãi suất thả nổi) trong hợp đồng FRA sẽ hiện thực hóa một khoản lãi trên hợp đồng khi tất toán (bằng giá trị hiện tại của phần chênh lệch giữa lãi suất MRR và lãi suất cố định nhân với vốn gốc danh nghĩa của hợp đồng trong kỳ tính lãi quy định) nếu lãi suất MRR được ấn định cao hơn mức lãi suất cố định ban đầu trên hợp đồng.
   **3. B là đáp án đúng.** Nếu lãi suất MRR được ấn định cao hơn mức lãi suất cam kết kỳ hạn ban đầu vào ngày đáo hạn, bên nhận lãi suất cố định (trả lãi suất thả nổi) trong hợp đồng FRA sẽ chịu một khoản lỗ MTM trên hợp đồng.

4. **C là đáp án đúng.** Các yêu cầu bù trừ trung tâm bắt buộc áp đặt những yêu cầu ký quỹ lên các định chế tài chính trung gian tương tự như những yêu cầu của các thị trường hợp đồng tương lai được chuẩn hóa giao dịch trên sàn, và các định chế này thường chuyển tiếp những chi phí và/hoặc yêu cầu này sang cho khách hàng của họ. Đáp án A và B không đúng, vì các khoản lãi MTM trên hợp đồng kỳ hạn truyền thống không được hiện thực hóa cho đến khi đáo hạn.
