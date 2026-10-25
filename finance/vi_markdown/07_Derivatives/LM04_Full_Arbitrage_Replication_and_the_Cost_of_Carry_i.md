# Tập 7: Công cụ Phái sinh (Derivatives)
## Learning Module 4 Arbitrage, Replication, and the Cost of Carry in Pricing Derivatives (Trang PDF 85–106)

---

# Tập 7: Công cụ Phái sinh (*Derivatives*)
## Học phần 4: Kinh doanh Chênh lệch giá, Mô phỏng và Chi phí Lưu giữ trong Định giá Công cụ Phái sinh (*Arbitrage, Replication, and the Cost of Carry in Pricing Derivatives*)
### Phần 1/2: Giới thiệu (*Introduction*) (Trang PDF 85–95)

---

<!-- PDF Page 85 -->

#### H Ọ C P H Ầ N

# **<mark>4</mark>**

### **Kinh doanh Chênh lệch giá, Mô phỏng và Chi phí Lưu giữ trong Định giá Công cụ Phái sinh (*Arbitrage, Replication, and the Cost of Carry in Pricing Derivatives*)**

###### **<mark>MỤC TIÊU HỌC TẬP (*LEARNING OUTCOMES*)</mark>**

|**_Mức độ Thành thạo (*Mastery*)_**<br>**_Ứng viên cần có khả năng:_**|
|---|
|Giải thích cách thức các khái niệm kinh doanh chênh lệch giá (*arbitrage*) và mô phỏng (*replication*) được sử dụng trong định giá các công cụ phái sinh (*pricing derivatives*).|
|Giải thích sự khác biệt giữa giá giao ngay (*spot price*) và giá kỳ vọng trong tương lai (*expected future price*) của một tài sản cơ sở cùng với chi phí lưu giữ (*cost of carry*) gắn liền với việc nắm giữ tài sản cơ sở đó.|

##### **GIỚI THIỆU (*INTRODUCTION*)**

## **<mark>1</mark>**

Các bài học về công cụ phái sinh trước đó đã thiết lập những đặc điểm của các công cụ và thị trường phái sinh, đồng thời đề cập đến cả những lợi ích lẫn rủi ro gắn liền với việc sử dụng chúng. Cam kết kỳ hạn (*forward commitments*) và quyền yêu cầu dự phòng (*contingent claims*) được phân biệt bởi cấu trúc lợi nhuận khi đáo hạn (*payoff profiles*) và các đặc điểm khác nhau của chúng. Giờ đây, chúng ta chuyển sự chú ý sang việc định giá (*pricing*) và xác định giá trị (*valuation*) của các công cụ này. Như một bước đầu tiên, chúng ta khám phá cách thức mức giá của một cam kết kỳ hạn liên hệ với giá giao ngay của một tài sản cơ sở theo cách không cho phép tồn tại các cơ hội kinh doanh chênh lệch giá (*arbitrage opportunities*). Cụ thể, chiến lược mô phỏng (*replication*) cho thấy rằng các khoản thanh toán (*payoffs*) hoàn toàn giống hệt với một cam kết kỳ hạn có thể đạt được từ các giao dịch trên thị trường giao ngay kết hợp với việc đi vay hoặc cho vay ở mức lãi suất phi rủi ro (*risk-free rate*). Cuối cùng, bài học thứ hai minh họa cách thức các chi phí hoặc lợi ích gắn liền với việc sở hữu một tài sản cơ sở tác động đến mức giá của cam kết kỳ hạn.

###### **TỔNG QUAN HỌC PHẦN (*LEARNING MODULE OVERVIEW*)**

- Cam kết kỳ hạn (*forward commitments*) là một phương thức thay thế để thiết lập vị thế mua (*long position*) hoặc vị thế bán (*short position*) đối với một tài sản cơ sở. Mối liên kết giữa giá kỳ hạn (*forward prices*) và giá giao ngay (*spot prices*) tồn tại nhằm ngăn chặn các nhà đầu tư tận dụng những cơ hội kinh doanh chênh lệch giá (*arbitrage opportunities*) giữa các công cụ trên thị trường tiền mặt (*cash instruments*) và công cụ phái sinh (*derivative instruments*).

Viện CFA (CFA Institute) xin gửi lời cảm ơn tới Tiến sĩ Don Chance, CFA, vì những đóng góp của ông cho phần này, trong đó bao gồm nội dung được trích xuất từ tài liệu xuất hiện trong phần *Thị trường và Công cụ Phái sinh* (*Derivative Markets and Instruments*), nằm trong chương trình giảng dạy CFA® Program năm 2022.


<!-- PDF Page 86 -->

- Một cam kết kỳ hạn có thể được mô phỏng (*replicated*) bằng một vị thế giao ngay mua hoặc bán đối với tài sản cơ sở kết hợp với việc đi vay hoặc cho vay ở mức lãi suất phi rủi ro. Các nhà đầu tư có thể tái tạo nhiều vị thế khác nhau bằng cách sử dụng các sự kết hợp phù hợp giữa vị thế giao ngay (*spot*), vị thế kỳ hạn (*forward*) và vị thế phi rủi ro (*risk-free positions*).

- Lãi suất phi rủi ro (*risk-free rate*) cung cấp mối liên kết nền tảng giữa giá giao ngay và giá kỳ hạn đối với các tài sản cơ sở không phát sinh thêm chi phí hay lợi ích nào từ quyền sở hữu.

- Chi phí lưu giữ (*cost of carry*) là giá trị ròng của các chi phí và lợi ích liên quan đến việc sở hữu một tài sản cơ sở trong một khoảng thời gian cụ thể và phải được tính đến trong khoản chênh lệch giữa giá giao ngay và giá kỳ hạn của một tài sản cơ sở cụ thể.

- Chi phí lưu giữ có thể bao gồm các khoản chi phí, chẳng hạn như chi phí lưu kho (*storage*) và bảo hiểm (*insurance*) đối với hàng hóa vật chất (*physical commodities*), hoặc các lợi ích của quyền sở hữu, chẳng hạn như cổ tức (*dividends*) đối với cổ phiếu và tiền lãi (*interest*) đối với trái phiếu. Ngoại hối (*foreign exchange*) đại diện cho một trường hợp đặc biệt trong đó chi phí lưu giữ là mức chênh lệch lãi suất (*interest rate differential*) giữa hai đồng tiền.

- Giá kỳ hạn có thể lớn hơn hoặc nhỏ hơn giá giao ngay của tài sản cơ sở, tùy thuộc vào chi phí lưu giữ cụ thể gắn liền với việc sở hữu tài sản cơ sở đó.

###### **TỰ ĐÁNH GIÁ HỌC PHẦN (*LEARNING MODULE SELF-ASSESSMENT*)**

Các câu hỏi ban đầu này nhằm mục đích giúp bạn tự đánh giá mức độ hiểu biết hiện tại của mình về học phần này.

1. Phát biểu nào sau đây mô tả đúng cách thức mô phỏng một vị thế mua kỳ hạn (*long forward position*)?

   - **A.** Bán một trái phiếu phi rủi ro, và mua một vị thế trên thị trường tiền mặt đối với tài sản cơ sở.

   - **B.** Mua một trái phiếu phi rủi ro, và mua một vị thế trên thị trường tiền mặt đối với tài sản cơ sở.

   - **C.** Mua một trái phiếu phi rủi ro, và bán một vị thế trên thị trường tiền mặt đối với tài sản cơ sở.

   - **Lời giải:**

A là đáp án đúng. Việc bán một trái phiếu phi rủi ro (*selling a risk-free bond* — tức là đi vay phi rủi ro) cung cấp lượng tiền mặt cần thiết để mua tài sản cơ sở trên thị trường tiền mặt (*cash market*). Khi trái phiếu đáo hạn, tài sản cơ sở được bán đi tại mức giá giao ngay trong tương lai, và số tiền thu được sẽ dùng để thanh toán dứt điểm trái phiếu đó. Lợi nhuận từ giao dịch này phụ thuộc vào mức giá giao ngay trong tương lai của tài sản cơ sở so với mức giá trên thị trường tiền mặt của tài sản cơ sở nhân với một cộng lãi suất phi rủi ro, và vị thế lợi nhuận này hoàn toàn giống hệt với vị thế mua kỳ hạn (*long forward position*) đối với tài sản cơ sở. B không đúng vì việc mua trái phiếu phi rủi ro làm phát sinh nhu cầu cần thêm tiền mặt bên cạnh việc mua tài sản cơ sở trên thị trường tiền mặt. C không đúng vì sự kết hợp này sẽ mô phỏng một vị thế bán kỳ hạn (*short forward position*).

2. Giá trị nào sau đây gần nhất với mức lợi nhuận kinh doanh chênh lệch giá (*arbitrage profit*) dành cho một nhà đầu tư có khả năng mua một tài sản với giá giao ngay là $\text{GBP}50$ tại thời điểm $t = 0$ và đồng thời bán một cam kết kỳ hạn sáu tháng trên cùng tài sản đó với mức giá kỳ hạn là $\text{GBP}52.50$? Lãi suất phi rủi ro là $4\%$, và tài sản này không có thêm chi phí hay lợi ích nào khác.

   - **A.** $\text{GBP}0.99$

   - **B.** $\text{GBP}0.48$


<!-- PDF Page 87 -->

   - **C.** $\text{GBP}1.51$

   - **Lời giải:** C là đáp án đúng. Nhà đầu tư đi vay với lãi suất $4\%$ trong sáu tháng để mua tài sản ngày hôm nay với giá $\text{GBP}50$. Sau sáu tháng, nhà đầu tư trả cho bên cho vay khoản tiền gốc và lãi là $S_0(1 + r)^T$, tương đương $\text{GBP}50.99$ [$= \text{GBP}50(1.04)^{0.5}$], đồng thời chuyển giao tài sản để thực hiện cam kết kỳ hạn bán ở mức giá $\text{GBP}52.50$. Lợi nhuận kinh doanh chênh lệch giá của nhà đầu tư là $\text{GBP}1.51$ ($= \text{GBP}52.50 - \text{GBP}50.99$). A không đúng vì đáp án này phản ánh phần chênh lệch giữa mức giá kỳ hạn không có kinh doanh chênh lệch giá (*no-arbitrage forward price*) và giá giao ngay hiện tại. B không đúng vì đáp án này phản ánh phần chênh lệch giữa giá kỳ hạn được chiết khấu ngược về một năm (thay vì sáu tháng) và giá giao ngay hiện tại.

3. Phát biểu nào sau đây mô tả đúng mối quan hệ giữa giá của một cam kết kỳ hạn so với giá giao ngay của tài sản cơ sở khi lợi ích của việc sở hữu tài sản cơ sở lớn hơn chi phí của việc sở hữu tài sản cơ sở đó (bao gồm cả chi phí lãi vay cơ hội)?
   - **A.** Giá cam kết kỳ hạn $>$ giá giao ngay.
   - **B.** Giá cam kết kỳ hạn $<$ giá giao ngay.
   - **C.** Giá cam kết kỳ hạn $=$ giá giao ngay.

   - **Lời giải:** B là đáp án đúng. Lợi ích lớn hơn gắn liền với tài sản cơ sở sẽ dẫn đến mức giá giao ngay cao hơn tương đối so với giá cam kết kỳ hạn, và nếu những lợi ích này lớn hơn các chi phí của việc sở hữu tài sản cơ sở, thì giá giao ngay sẽ lớn hơn giá cam kết kỳ hạn. A không đúng vì bất đẳng thức này sẽ đúng trong trường hợp chi phí vượt quá lợi ích. C không đúng vì sự ngang bằng giữa hai mức giá mô tả trường hợp hiếm gặp khi chi phí và lợi ích bằng nhau một cách chính xác.

4. Phát biểu nào sau đây định nghĩa đúng nhất về lợi suất tiện ích (*convenience yield*)?
   - **A.** Lợi suất tiện ích phản ánh sự ưu tiên mà những người tham gia thị trường thể hiện đối với việc mua các hợp đồng kỳ hạn nhằm tránh phải trả tiền mặt ngay từ đầu.

   - **B.** Lợi suất tiện ích phản ánh sự ưu tiên mà những người tham gia thị trường thể hiện đối với việc mua trên thị trường giao ngay nhằm tránh phải trả chi phí lưu kho.

   - **C.** Lợi suất tiện ích phản ánh sự ưu tiên mà những người tham gia thị trường thể hiện đối với việc mua trên thị trường giao ngay vì các lý do phi tiền mặt, bao gồm cả tình trạng hàng tồn kho thấp trên thị trường tiền mặt của tài sản cơ sở.

###### **Lời giải:**

C là đáp án đúng. Lợi suất tiện ích (*convenience yield*) là một lợi ích phi tiền mặt (*non-cash benefit*) gắn liền với việc sở hữu một hàng hóa vật chất cơ sở, phát sinh trong những điều kiện kinh tế nhất định, bao gồm cả tình trạng hàng tồn kho của tài sản cơ sở ở mức thấp. A không đúng vì phát biểu này ngụ ý rằng lợi suất tiện ích là một khoản chi phí của việc sở hữu tài sản cơ sở. B không đúng vì phát biểu này tự mâu thuẫn ở chỗ nó nêu rằng lợi suất tiện ích khiến những người tham gia thị trường ưu tiên thị trường giao ngay nhưng lại quy điều này một cách sai lầm cho một khoản chi phí của việc sở hữu tài sản cơ sở (mua trên thị trường giao ngay thực tế làm phát sinh chi phí lưu kho chứ không phải tránh được nó).


<!-- PDF Page 88 -->

## **<mark>2</mark>**

##### **KINH DOANH CHÊNH LỆCH GIÁ (*ARBITRAGE*)**

*Giải thích cách thức các khái niệm kinh doanh chênh lệch giá (arbitrage) và mô phỏng (replication) được sử dụng trong định giá các công cụ phái sinh.*

Một bài học trước đây về tính hiệu quả của thị trường (*market efficiency*) đã xác lập rằng giá cả thị trường không nên cho phép tồn tại khả năng thu lợi nhuận phi rủi ro (*riskless profit*) hay kinh doanh chênh lệch giá (*arbitrage*) khi không có chi phí giao dịch. Ở dạng đơn giản nhất, một cơ hội kinh doanh chênh lệch giá phát sinh nếu “quy luật một giá” (*law of one price*) không được đảm bảo, hoặc một tài sản giống hệt nhau được giao dịch cùng một lúc ở các mức giá khác nhau tại các địa điểm khác nhau.

Trong trường hợp của một hợp đồng phái sinh mà giá trị của nó bắt nguồn từ các dòng tiền trong tương lai gắn liền với giá của một tài sản cơ sở, cơ hội kinh doanh chênh lệch giá sẽ phát sinh hoặc khi hai tài sản có *dòng tiền tương lai* giống hệt nhau được giao dịch ở các mức giá khác nhau, hoặc khi một tài sản có mức giá tương lai đã biết không được giao dịch tại mức *giá trị hiện tại* (*present value*) của giá tương lai đó khi được xác định bằng một lãi suất chiết khấu phù hợp.

Trường hợp đầu tiên về các tài sản có dòng tiền tương lai giống hệt nhau nhưng giao dịch ở các mức giá khác nhau được minh họa trong Bảng minh họa 1 (*Exhibit 1*).

**Bảng minh họa 1: Các Tài sản có Dòng tiền Tương lai Giống hệt nhau Giao dịch ở các Mức giá Khác nhau (*Assets with Identical Future Cash Flows Trade at Different Prices*)**

![](assets/Derivatives.pdf-0088-11.png)

> **Chú thích hình ảnh:**
> - Tại thời điểm $0$: $\text{EUR}99 = S_0^A < S_0^B = \text{EUR}99.15$ $\rightarrow$ Mua A tại mức giá $S_0^A$, Bán B tại mức giá $S_0^B$ $\rightarrow$ Dòng tiền tại thời điểm $0$: $CF_0 = (S_0^B - S_0^A) = (\text{EUR}99.15 - \text{EUR}99) = +\text{EUR}0.15 > 0$.
> - Tại thời điểm $T$: $S_T^A = S_T^B = \text{EUR}100$ $\rightarrow$ Bán A với giá $S_T^A$, Mua B tại giá $S_T^B$ $\rightarrow$ Dòng tiền tại thời điểm $T$: $CF_T = (S_T^A - S_T^B) = (\text{EUR}100 - \text{EUR}100) = 0$.

Ví dụ, giả sử hai tài sản này là các trái phiếu không trả lãi định kỳ (*zero-coupon bonds*) có các đặc điểm giống hệt nhau và cùng một tổ chức phát hành. Cả hai trái phiếu đều đáo hạn vào cùng một ngày trong tương lai với khoản thanh toán bằng mệnh giá (*par*) và có cùng mức rủi ro vỡ nợ từ nay cho đến ngày đáo hạn.

**1.** Trái phiếu A có giá là $\text{EUR}99$ tại thời điểm $t = 0$ ($S_0^A = \text{EUR}99$).

**2.** Trái phiếu B có giá là $\text{EUR}99.15$ tại thời điểm $t = 0$ ($S_0^B = \text{EUR}99.15$).

**3.** Cả hai trái phiếu đều có mức giá kỳ vọng trong tương lai là $\text{EUR}100$ ($S_T^A = S_T^B = \text{EUR}100$). Kịch bản này đại diện cho một cơ hội kinh doanh chênh lệch giá đối với nhà đầu tư.

- Tại thời điểm $t = 0$, nhà đầu tư có thể:

   - Bán khống (*sell short*) Trái phiếu B để nhận số tiền thu về là $\text{EUR}99.15$ và mua Trái phiếu A với giá $\text{EUR}99$;

   - Hiện thực hóa một dòng tiền vào ròng (*net cash inflow*) tại thời điểm $t = 0$ là $\text{EUR}0.15$.

- Tại thời điểm $t = T$, khi cả hai trái phiếu đáo hạn, nhà đầu tư:

   - Nhận được $\text{EUR}100$ từ Trái phiếu A và sử dụng số tiền này để mua Trái phiếu B với giá $\text{EUR}100$ nhằm đóng vị thế bán khống (*cover the short position*).

   - Các dòng tiền bù trừ cho nhau tại thời điểm $T$ giúp nhà đầu tư thu được một khoản lợi nhuận phi rủi ro bằng đúng khoản chênh lệch giá $\text{EUR}0.15$ giữa Trái phiếu A và B tại thời điểm $0$.


<!-- PDF Page 89 -->

Những nhà đầu tư khác khi nhận thấy sự bất hợp lý này cũng sẽ tìm cách kiếm lợi nhuận phi rủi ro tại thời điểm $t = 0$ bằng cách bán Trái phiếu B, đẩy giá của nó giảm xuống, và mua Trái phiếu A, đẩy giá của nó tăng lên, cho đến khi hai mức giá hội tụ. Cơ hội kinh doanh chênh lệch giá sẽ biến mất một khi hai trái phiếu có cùng mức giá ($S_0^A = S_0^B$).

Loại cơ hội kinh doanh chênh lệch giá thứ hai liên quan đến công cụ phái sinh phát sinh khi một tài sản có mức giá tương lai đã biết không được giao dịch ở mức giá trị hiện tại ($\text{PV}$) của giá tương lai đó. Một bài học trước đây về giá trị thời gian của tiền tệ đã phân biệt giữa ghép lãi rời rạc (*discrete compounding*) và ghép lãi liên tục (*continuous compounding*) khi tính toán giá trị hiện tại so với giá trị tương lai. Giá trị tương lai của một dòng tiền đơn lẻ dựa trên một số lượng *rời rạc* các kỳ đồng nhất tuân theo công thức tổng quát trong Phương trình 1:

$$\text{FV}_N = \text{PV}(1 + r)^N \tag{1}$$

trong đó $r$ là lãi suất công bố trên mỗi *kỳ* và $N$ là số kỳ ghép lãi. *Ghép lãi liên tục* (*continuous compounding*) là trường hợp trong đó độ dài của các kỳ đồng nhất tiến dần về $0$, do đó số kỳ trong một năm tiến tới vô cùng và được tính toán bằng cách sử dụng cơ số logarit tự nhiên, như được thể hiện trong Phương trình 2:

$$\text{FV}_T = \text{PV}e^{rT} \tag{2}$$

Mặc dù các công cụ phái sinh có thể được định giá bằng một trong hai phương pháp, nhưng phục vụ cho mục đích của bài học này và các bài học sau, chúng ta sẽ sử dụng phương pháp ghép lãi rời rạc cho từng tài sản cơ sở riêng lẻ. Tuy nhiên, đối với các tài sản cơ sở đại diện cho một danh mục đầu tư, chẳng hạn như chỉ số cổ phiếu, thu nhập cố định, hàng hóa hoặc tín dụng, hoặc khi tài sản cơ sở liên quan đến ngoại hối nơi lãi suất được định danh bằng hai đồng tiền khác nhau, ghép lãi liên tục sẽ là phương pháp được ưu tiên sử dụng. Nếu bỏ qua các chi phí hoặc lợi ích bổ sung gắn liền với quyền sở hữu tài sản, mức lãi suất chiết khấu phù hợp, $r$, chính là lãi suất phi rủi ro, như được minh họa trong Ví dụ 1.

###### **VÍ DỤ 1 (*EXAMPLE 1*)**

###### **Giá Vàng Giao ngay so với Giá Tương lai Đã biết Được Chiết khấu (*Spot vs. Discounted Known Future Price of Gold*)**

Trong một bài học trước, Procam Investments đã tham gia vào một hợp đồng mua $100\text{ ounce}$ vàng tại mức giá thỏa thuận trước là $\text{USD}1,792.13$ mỗi ounce sau ba tháng. Trong ví dụ này, Procam thực hiện giao dịch ngược lại, khi nhận thấy có sự chênh lệch giữa giá vàng giao ngay và giá vàng tương lai đã biết sau khi chiết khấu. Giả sử giá vàng giao ngay ngày hôm nay ($S_0$) là $\text{USD}1,770$ mỗi ounce, và lãi suất phi rủi ro chuẩn hóa theo năm ($r$) là $2\%$. Phục vụ cho mục đích của ví dụ này, chúng ta giả định rằng Procam có thể đi vay ở mức lãi suất phi rủi ro và vàng có thể được lưu kho mà không tốn chi phí. Dưới các điều kiện này, chúng ta minh họa cách thức Procam có thể tạo ra một khoản lợi nhuận phi rủi ro:

- Tại thời điểm $t = 0$:

  - Procam vay $\text{USD}177,000$ với lãi suất $2.0\%$ trong ba tháng và mua $100\text{ ounce}$ vàng tại mức giá giao ngay ngày hôm nay.

  - Procam tham gia vào một hợp đồng kỳ hạn ngày hôm nay để bán $100\text{ ounce}$ vàng tại mức giá $\text{USD}1,792.13$ mỗi ounce sau ba tháng.

![](assets/Derivatives.pdf-0089-15.png)

> **Chú thích hình ảnh:**
> - **Tại thời điểm $0$ ($S_0 < S_T(1 + r)^{-T}$):** Vay $S_0$ tại lãi suất $r$ và Mua $S_0$, đồng thời Thỏa thuận bán tại giá $S_T$. Cụ thể: Vay $\text{USD}1,770$ tại mức lãi suất $2\%$ và Mua vàng ($S_0$); Ký hợp đồng bán tại $S_T = \text{USD}1,792.13$ mỗi ounce. Dòng tiền $CF_0 = 0$.
> - **Tại thời điểm $T$ ($S_0(1 + r)^T < S_T$):** Bán tại giá $S_T$ và Hoàn trả khoản vay $S_0(1 + r)^T$. Cụ thể: Bán ở mức giá $\text{USD}1,792.13$ ($S_T$) và Hoàn trả $S_0(1 + r)^T = \text{USD}1,778.78$; Thu lợi nhuận phi rủi ro là $\text{USD}13.35$ mỗi ounce. Dòng tiền $CF_T = (\text{USD}1,792.13 - \text{USD}1,778.78) > 0$.

- Tại thời điểm $t = T$ (sau ba tháng):


<!-- PDF Page 90 -->

  - Procam chuyển giao $100\text{ ounce}$ vàng theo hợp đồng kỳ hạn và nhận về $\text{USD}179,213$ ($= 100 \times \text{USD}1,792.13$).

  - Procam hoàn trả nợ gốc cùng với tiền lãi:

$$\text{USD}177,878.44 = \text{USD}177,000(1.02)^{0.25}$$

  - Lợi nhuận phi rủi ro của Procam tại thời điểm $T$ bằng phần chênh lệch giữa số tiền thu được từ việc bán kỳ hạn và khoản nợ gốc cộng lãi vay: $\text{USD}1,334.56 = \text{USD}179,213 - \text{USD}177,878.44$.

Trong Ví dụ 1, giá vàng giao ngay, $S_0$, thấp hơn giá trị hiện tại của mức giá vàng tương lai đã biết sau thời gian ba tháng ($S_0 < S_T(1 + r)^{-T}$, vì $\text{USD}1,770 < \text{USD}1,783.28$). Procam kiếm được một khoản lợi nhuận phi rủi ro là $\text{USD}13.35$ mỗi ounce bằng cách đi vay và mua vàng trên thị trường tiền mặt, đồng thời bán vàng trên thị trường kỳ hạn tại mức giá đã thỏa thuận trước. Chúng ta kỳ vọng rằng khi các nhà đầu tư khác nhận ra và theo đuổi cơ hội này, giá giao ngay sẽ tăng lên (và giá kỳ hạn sẽ giảm xuống) cho đến khi giá giao ngay bằng với giá trị chiết khấu của mức giá tương lai đã biết ($S_0 = S_T(1 + r)^{-T}$) nhằm triệt tiêu cơ hội kinh doanh chênh lệch giá này.

Hai khái niệm kinh doanh chênh lệch giá cốt lõi được sử dụng để định giá công cụ phái sinh đối với một tài sản cơ sở không có dòng tiền bổ sung có thể được tóm tắt như sau:

- Các tài sản giống hệt nhau hoặc các tài sản có dòng tiền giống hệt nhau được giao dịch tại cùng một thời điểm phải có cùng một mức giá ($S_0^A = S_0^B$).

- Các tài sản có mức giá tương lai đã biết phải có giá giao ngay bằng với mức giá tương lai đó được chiết khấu theo lãi suất phi rủi ro ($S_0 = S_T(1 + r)^{-T}$).

Các điều kiện kinh doanh chênh lệch giá này thiết lập mối quan hệ giữa giá giao ngay, giá cam kết kỳ hạn và lãi suất phi rủi ro như được thể hiện trong Bảng minh họa 2.

**Bảng minh họa 2: Giá Giao ngay, Giá Cam kết Kỳ hạn và Lãi suất Phi rủi ro (*Spot Prices, Forward Commitment Prices, and the Risk-Free Rate*)**

![](assets/Derivatives.pdf-0090-13.png)

> **Chú thích hình ảnh:**
> Đồ thị biểu diễn mối quan hệ tăng dần từ Giá giao ngay $S_0$ tại thời điểm $0$ lên Giá kỳ hạn $F_0(T)$ tại thời điểm $T$ với độ dốc phụ thuộc vào lãi suất phi rủi ro $r$.

Bảng minh họa 2 thể hiện trường hợp $r > 0$ đối với một tài sản không có thu nhập hay chi phí bổ sung theo phương pháp ghép lãi rời rạc. Lưu ý rằng đối với một thời điểm $T$ nhất định, giá kỳ hạn sẽ cao hơn tương đối so với giá giao ngay khi lãi suất phi rủi ro $r$ cao hơn. Ngoài ra, đối với một mức lãi suất phi rủi ro $r$ nhất định, khi $T$ tăng lên, giá kỳ hạn sẽ tăng lên tương đối so với giá giao ngay. Điều quan trọng cần lưu ý là mức lãi suất phi rủi ro phù hợp đối với hầu hết những người tham gia thị trường chính là lãi suất mua lại (*repo rate*), đã được giới thiệu trong một bài học trước, nơi các khoản vốn vay được thế chấp bằng những chứng khoán có tính thanh khoản cao.

Hãy nhớ lại từ bài học trước rằng một cam kết kỳ hạn có cấu trúc lợi nhuận đối xứng (*symmetric payoff profile*). Nghĩa là, tại thời điểm $T$, giao dịch được thanh toán dựa trên cơ sở phần chênh lệch giữa giá kỳ hạn $F_0(T)$ và giá tài sản cơ sở $S_T$, hay $F_0(T) - S_T$ xét dưới góc độ của bên bán, như trong Bảng minh họa 3.


<!-- PDF Page 91 -->

###### **Bảng minh họa 3: Cấu trúc Lợi nhuận của Bên Bán Cam kết Kỳ hạn (*Forward Commitment Seller Payoff Profile*)**

![](assets/Derivatives.pdf-0091-04.png)

> **Chú thích hình ảnh:**
> Trục tung biểu diễn Khoản thanh toán/Lợi nhuận (*Payoff/Profit*) từ $-$ đến $+$; trục hoành biểu diễn Giá tài sản cơ sở tại ngày đáo hạn $S_T$. Đường lợi nhuận của bên bán kỳ hạn dốc xuống, cắt trục hoành tại $F_0(T)$ (khi $S_T < F_0(T)$ thì có lãi dương, khi $S_T > F_0(T)$ thì chịu lỗ âm).

Bên bán kỳ hạn hiện thực hóa một khoản lãi nếu họ có khả năng chuyển giao tài sản cơ sở tại mức giá trị thị trường ($S_T$) thấp hơn mức giá đã thỏa thuận trước, $F_0(T)$. Trong Ví dụ 1, Procam đi vay để mua tài sản cơ sở tại mức giá giao ngay thấp hơn giá trị hiện tại của $S_T$ nhằm khóa chặt một khoản lãi phi rủi ro. Cho đến nay, chúng ta vẫn coi mức giá kỳ hạn, $F_0(T)$, là cho trước. Trong phần tiếp theo, chúng ta sẽ minh họa cách thức các điều kiện không có kinh doanh chênh lệch giá (*no-arbitrage conditions*) có thể được sử dụng để thiết lập mối quan hệ giữa giá giao ngay và giá kỳ hạn thông qua việc mô phỏng (*replicating*) hoặc tái tạo một vị thế bù trừ chính xác cho một cam kết kỳ hạn.

##### **MÔ PHỎNG (*REPLICATION*)**

![](assets/Derivatives.pdf-0091-07.png)

## **<mark>3</mark>**

*Giải thích cách thức các khái niệm kinh doanh chênh lệch giá (arbitrage) và mô phỏng (replication) được sử dụng trong định giá các công cụ phái sinh.*

**Mô phỏng (*Replication*)** là một chiến lược trong đó chuỗi dòng tiền của một công cụ phái sinh có thể được tái tạo bằng cách sử dụng sự kết hợp giữa các vị thế mua (*long*) hoặc bán (*short*) đối với một tài sản cơ sở cùng với việc đi vay hoặc cho vay tiền mặt. Trái ngược với các ví dụ kinh doanh chênh lệch giá trước đó, mô phỏng thường được sử dụng để phản chiếu (*mirror*) hoặc bù trừ (*offset*) một vị thế phái sinh khi quy luật một giá được đảm bảo và không tồn tại các cơ hội kiếm lợi nhuận kinh doanh chênh lệch giá phi rủi ro. Ví dụ, Bảng minh họa 4 so sánh một cam kết mua kỳ hạn (*long forward commitment*) với phương án thay thế là đi vay vốn ở mức lãi suất phi rủi ro, $r$, để mua tài sản cơ sở tại mức giá giao ngay ngày hôm nay, $S_0$.


<!-- PDF Page 92 -->

###### **Bảng minh họa 4: Mô phỏng Cam kết Kỳ hạn (*Forward Commitment Replication*)**

![](assets/Derivatives.pdf-0092-04.png)

> **Chú thích hình ảnh:**
> - **Chiến lược Đi vay $S_0$ và mua giao ngay ($S_0$) $\rightarrow$ Hoàn trả khoản vay ($S_0(1+r)^T$) và bán giao ngay ($S_T$):**
>   - Tại $t = 0$: Vay $\text{USD}1,783.28$ ($S_0$) ngày hôm nay tại $t = 0$; Mua tại $S_0 = \text{USD}1,783.28$ $\rightarrow$ $CF_0 = (\text{USD}1,783.28 - \text{USD}1,783.28) = 0$.
>   - Tại $t = T$: Hoàn trả $\text{USD}1,792.13$ ($S_0(1+r)^T$) tại $t = T$; Bán tại giá giao ngay ($S_T$) $\rightarrow$ $CF_T = (S_T - \text{\$1,792.13})$.
> - **Chiến lược Tham gia hợp đồng mua kỳ hạn ($F_0(T)$) $\rightarrow$ Tất toán hợp đồng mua kỳ hạn ($S_T - F_0(T)$):**
>   - Tại $t = 0$: Thỏa thuận mua ở mức giá $\text{USD}1,792.13$ ($F_0(T)$) vào thời điểm $t = T$ $\rightarrow$ $CF_0 = 0$.
>   - Tại $t = T$: Tất toán hợp đồng ($S_T - F_0(T)$) tại $t = T$ $\rightarrow$ $CF_T = (S_T - \text{\$1,792.13})$.

###### **VÍ DỤ 2 (*EXAMPLE 2*)**

###### **Mô phỏng một Cam kết Kỳ hạn (*Replication of a Forward Commitment*)**

Trong Ví dụ 1, chúng ta đã giới thiệu lại Procam Investments, công ty đã đi vay và mua vàng trên thị trường giao ngay đồng thời bán vàng trên thị trường kỳ hạn để kiếm một khoản lợi nhuận phi rủi ro. Ở đây, chúng ta thay đổi giả định về giá vàng giao ngay ngày hôm nay ($S_0$). Cụ thể, giá vàng giao ngay đã tăng lên mức $\text{USD}1,783.28$ ($= \text{USD}1,792.13(1.02)^{-0.25}$) để triệt tiêu cơ hội kinh doanh chênh lệch giá trước đó khi giá giao ngay ở mức $\text{USD}1,770$. Giả sử một lần nữa rằng lãi suất phi rủi ro ($r$) là $2\%$ và vàng có thể được lưu kho mà không tốn chi phí.

**1.** Cam kết mua kỳ hạn (thỏa thuận mua tại giá $F_0(T)$ vào thời điểm $t = T$):

   - Procam tham gia một cam kết kỳ hạn để mua $100\text{ ounce}$ vàng sau ba tháng tại mức giá kỳ hạn, $F_0(T)$, là $\text{USD}1,792.13$ mỗi ounce.

   - Nếu $S_T = \text{USD}1,900$ mỗi ounce:
     - Lợi nhuận $= \text{USD}10,787 = 100 \times (\text{USD}1,900 - \text{USD}1,792.13)$.

   - Nếu $S_T = \text{USD}1,700$ mỗi ounce:
     - Lợi nhuận $= -\text{USD}9,213 = 100 \times (\text{USD}1,700 - \text{USD}1,792.13)$.

**2.** Đi vay và mua tài sản (vay $S_0$ và mua tài sản tại giá $S_0$ vào thời điểm $t = 0$):

   - Procam vay $\text{USD}178,328$ với lãi suất $2\%$ và mua $100\text{ ounce}$ vàng tại mức giá giao ngay ngày hôm nay, $S_0$.

   - Procam bán số vàng đó sau ba tháng tại mức giá giao ngay $S_T$.

   - Procam hoàn trả nợ gốc và lãi vay: $\text{USD}179,213 = \text{USD}178,328(1.02)^{0.25}$.

   - Nếu $S_T = \text{USD}1,900$:
     - Lợi nhuận $= \text{USD}10,787 = 100 \times (\text{USD}1,900 - \text{USD}1,792.13)$.

   - Nếu $S_T = \text{USD}1,700$:
     - Lợi nhuận $= -\text{USD}9,213 = 100 \times (\text{USD}1,700 - \text{USD}1,792.13)$.


<!-- PDF Page 93 -->

Lưu ý rằng các mức lợi nhuận hoàn toàn giống nhau được quan sát thấy dưới cả Kịch bản 1 và Kịch bản 2, đều bằng $S_T - F_0(T)$. Nếu chúng ta đặt mức giá kỳ hạn, $F_0(T)$, bằng với giá trị tương lai của giá giao ngay tính theo lãi suất phi rủi ro ($F_0(T) = S_0(1 + r)^T$), điều kiện không có kinh doanh chênh lệch giá chứng minh rằng Procam tạo ra cùng một dòng tiền tại thời điểm $T$ bất kể chiều hướng biến động của giá vàng, cho dù công ty:

**1.** tham gia vào một cam kết mua kỳ hạn được tất toán tại thời điểm $T$, hay

**2.** đi vay ở mức lãi suất phi rủi ro, mua tài sản cơ sở và nắm giữ nó cho đến thời điểm $T$.

Một hình thức mô phỏng riêng biệt nhưng có liên quan, kết hợp một vị thế mua tài sản (*long asset*) với một vị thế bán kỳ hạn (*short forward*), được thể hiện trong Bảng minh họa 5. Nửa trên thể hiện cấu trúc lãi/lỗ của vị thế mua tài sản, và nửa dưới thể hiện cấu trúc lãi/lỗ của vị thế bán kỳ hạn. Vị thế mua tài sản tạo ra một khoản lãi (lỗ) khi $S_T > S_0$ ($S_T < S_0$). Vị thế bán kỳ hạn tạo ra một khoản lãi (lỗ) khi $S_T < F_0$ ($S_T > F_0$).

**Bảng minh họa 5: Khoản thanh toán cho Vị thế Mua Tài sản và Vị thế Bán Kỳ hạn (*Payoffs for Long Asset and Short Forward Positions*)**

![](assets/Derivatives.pdf-0093-08.png)

> **Chú thích hình ảnh:**
> - **Đồ thị trên (Vị thế mua trên thị trường tiền mặt - *Long cash position*):** Đường lợi nhuận (*Payoff/Profit*) dốc lên, cắt trục hoành $S_T$ tại $S_0$.
> - **Đồ thị dưới (Vị thế bán kỳ hạn - *Short forward position*):** Đường lợi nhuận (*Payoff/Profit*) dốc xuống, cắt trục hoành $S_T$ tại $F_0(T)$.

Trái ngược với Ví dụ 2, các vị thế này dường như bù trừ lẫn nhau. Ví dụ sau đây đánh giá tỷ suất sinh lợi được tạo ra bởi sự kết hợp của các vị thế này.


<!-- PDF Page 94 -->

###### **VÍ DỤ 3 (*EXAMPLE 3*)**

###### **Mô phỏng Giao dịch Phi Rủi ro: Mua Tài sản, Bán Kỳ hạn (*Risk-Free Trade Replication: Long Asset, Short Forward*)**

Procam Investments mua $100\text{ ounce}$ vàng tại mức giá giao ngay ngày hôm nay ($S_0$) là $\text{USD}1,783.28$ và đồng thời tham gia một cam kết kỳ hạn để bán vàng tại mức giá kỳ hạn, $F_0(T)$, là $\text{USD}1,792.13$. Một lần nữa, chúng ta giả định rằng vàng có thể được lưu kho mà không tốn chi phí, và ở đây chúng ta giải tìm tỷ suất sinh lợi của Procam.

- Tại thời điểm $t = 0$, dòng tiền của Procam là $-S_0 = -\text{USD}178,328$.

- Tại thời điểm $t = T$, dòng tiền của Procam là $F_0(T) = \text{USD}179,213$.

- Giải tìm tỷ suất sinh lợi đối với chiến lược của Procam như sau:

  - $\text{USD}179,213 = \text{USD}178,328(1 + r)^{0.25}$.

  - $r = 2.0\%$, bằng đúng mức lãi suất phi rủi ro.

Ví dụ này chứng minh rằng Procam có thể phòng ngừa rủi ro (*hedge*) cho vị thế mua vàng trên thị trường tiền mặt của mình bằng một vị thế bán công cụ phái sinh (tức là bán hợp đồng kỳ hạn) và kiếm được tỷ suất sinh lợi phi rủi ro miễn là điều kiện không có kinh doanh chênh lệch giá ($F_0(T) = S_0(1 + r)^T$) được đảm bảo. Lợi nhuận kết hợp được thể hiện trong Bảng minh họa 6. Lưu ý rằng nếu Procam đi vay ở mức lãi suất phi rủi ro để mua tài sản cơ sở tại giá $S_0$, công ty sẽ kiếm được lợi nhuận bằng không.

**Bảng minh họa 6: Lợi nhuận Kết hợp của Vị thế Mua Tài sản và Bán Kỳ hạn (*Combined Long Asset and Short Forward Profit*)**

![](assets/Derivatives.pdf-0094-13.png)

> **Chú thích hình ảnh:**
> Trục tung biểu diễn Khoản thanh toán/Lợi nhuận (*Payoff/Profit*), trục hoành biểu diễn $S_T$. Đường lợi nhuận là một đường thẳng nằm ngang ở phần dương: $\text{Profit} = F_0(T) - S_0$ không đổi bất kể giá trị của $S_T$.

Bởi vì giá kỳ hạn được giả định là lớn hơn giá giao ngay trong ví dụ này và $r$ mang giá trị dương, nên khoản lợi nhuận phi rủi ro là một số tiền dương và giữ nguyên không đổi (tức là phi rủi ro) bất kể mức giá của tài sản cơ sở ($S_T$) là bao nhiêu. Như chúng ta sẽ thấy trong bài học tiếp theo, có thể tồn tại những lợi ích hoặc chi phí gắn liền với việc sở hữu một tài sản cơ sở khiến cho mức sinh lợi phi rủi ro trong Bảng minh họa 6 khác biệt so với $F_0(T) - S_0$ và thậm chí có khả năng mang giá trị âm.


<!-- PDF Page 95 -->

##### **BỘ CÂU HỎI (*QUESTION SET*): Kinh doanh Chênh lệch giá và Mô phỏng (*Arbitrage and Replication*)**

1. Xác định các từ đúng để điền vào chỗ trống: Nếu quy luật một giá không được đảm bảo, một tài sản \_\_\_\_\_\_\_\_\_ được giao dịch cùng một lúc ở các mức giá \_\_\_\_\_\_\_\_\_ tại các địa điểm khác nhau.

   **Lời giải:**
   Nếu quy luật một giá không được đảm bảo, một tài sản *giống hệt nhau* (*identical*) được giao dịch cùng một lúc ở các mức giá *khác nhau* (*different*) tại các địa điểm khác nhau.

2. Một nhà đầu tư quan sát thấy rằng giá giao ngay, $S_0$, của một tài sản cơ sở không có chi phí hay lợi ích bổ sung vượt quá mức giá tương lai đã biết của nó sau khi được chiết khấu theo lãi suất phi rủi ro, $S_T(1 + r)^{-T}$. Hãy mô tả và giải thích một chiến lược kinh doanh chênh lệch giá giúp tạo ra lợi nhuận phi rủi ro cho nhà đầu tư.

   **Lời giải:**
   Vì giá giao ngay của tài sản cơ sở vượt quá mức giá tương lai đã biết được chiết khấu theo lãi suất phi rủi ro ($S_0 > F_0(T)(1 + r)^{-T}$), nên tại thời điểm $t = 0$, nhà đầu tư:
   - Bán khống tài sản cơ sở trên thị trường giao ngay tại mức giá $S_0$
   - Đồng thời tham gia một hợp đồng mua kỳ hạn (*long forward contract*) tại mức giá $F_0(T)$
   - Cho vay khoản tiền $S_0$ ở mức lãi suất phi rủi ro $r$ để nhận về $S_0(1 + r)^T$ tại thời điểm $T$.

   Tại thời điểm $t = T$, nhà đầu tư:
   - Tất toán vị thế mua kỳ hạn và nhận được $S_T - F_0(T)$
   - Đóng vị thế bán khống tài sản cơ sở tại mức giá $S_T$, và
   - Giữ lại khoản $S_0(1 + r)^T - F_0(T)$ như một khoản lợi nhuận phi rủi ro bất kể giá giao ngay của tài sản cơ sở tại thời điểm $T$ là bao nhiêu.

3. Hãy thiết lập một chiến lược mô phỏng (*replication strategy*) cho một cam kết bán kỳ hạn (*short forward commitment*) kỳ hạn ba tháng đối với $1,000$ cổ phiếu của một mã cổ phiếu không trả cổ tức.

   **Lời giải:**
   Chiến lược mô phỏng cho một cam kết bán kỳ hạn ba tháng đối với một cổ phiếu không trả cổ tức bao gồm việc bán khống $1,000$ cổ phiếu tại thời điểm $t = 0$ và đầu tư số tiền thu được ở mức lãi suất phi rủi ro, $r$. Tại thời điểm $t = T$, giao dịch bán khống được đóng lại (*covered*) tại mức giá $S_T$, và dưới điều kiện không có kinh doanh chênh lệch giá $F_0(T) = S_0(1 + r)^T$, mức sinh lợi sẽ bằng $F_0(T) - S_T$ đối với cả vị thế bán kỳ hạn lẫn chiến lược mô phỏng.

4. Tính toán lợi nhuận kinh doanh chênh lệch giá nếu một tài sản giao ngay không có chi phí hay lợi ích bổ sung được giao dịch tại mức giá giao ngay là $100$, giá kỳ hạn ba tháng của tài sản cơ sở đó là $102$, và lãi suất phi rủi ro là $5\%$.

   **Lời giải:**
   Mức giá kỳ hạn, $F_0(T) = S_0(1 + r)^T$, tại đó không tồn tại cơ hội kinh doanh chênh lệch giá là $101.23$ ($= 100(1.05)^{0.25}$). Với mức giá kỳ hạn quan sát được trên thị trường là $102$, cơ hội kinh doanh chênh lệch giá sẽ là bán hợp đồng kỳ hạn và mua tài sản cơ sở, đồng thời đi vay ở mức lãi suất phi rủi ro để tài trợ cho giao dịch mua đó. Lợi nhuận kinh doanh chênh lệch giá tại thời điểm đáo hạn là phần chênh lệch giữa giá kỳ hạn quan sát được và giá kỳ hạn không có kinh doanh chênh lệch giá, bằng $0.77$ ($= 102 - 101.23$).


---

# Tập 7: Công cụ Phái sinh (*Derivatives*)
## Học phần 4: Kinh doanh Chênh lệch giá, Mô phỏng và Chi phí Lưu giữ trong Định giá Công cụ Phái sinh (*Arbitrage, Replication, and the Cost of Carry in Pricing Derivatives*)
### Phần 2/2: Chi phí và Lợi ích Gắn liền với Việc Sở hữu Tài sản Cơ sở (*Costs and Benefits Associated with Owning the Underlying*) (Trang PDF 96–106)

---

<!-- PDF Page 96 -->

5. Hãy mô tả mối quan hệ giữa giá giao ngay và giá kỳ hạn đối với một tài sản cơ sở nếu lãi suất phi rủi ro mang giá trị âm.

   - **Lời giải:**

Mối quan hệ giữa giá giao ngay và giá kỳ hạn đối với một tài sản không có thêm chi phí hay lợi ích nào từ quyền sở hữu ngoài chi phí cơ hội (lãi suất phi rủi ro) được xác định bởi công thức $F_0(T) = S_0(1 + r)^T$. Trong trường hợp $r < 0$, ta có $(1 + r)^T < 1$ và do đó giá kỳ hạn, $F_0(T)$, sẽ thấp hơn giá giao ngay, $S_0$, nếu lãi suất phi rủi ro là số âm.

# **<mark>4</mark>**

## **CHI PHÍ VÀ LỢI ÍCH GẮN LIỀN VỚI VIỆC SỞ HỮU TÀI SẢN CƠ SỞ (*COSTS AND BENEFITS ASSOCIATED WITH OWNING THE UNDERLYING*)**

*Giải thích sự khác biệt giữa giá giao ngay và giá kỳ vọng trong tương lai của một tài sản cơ sở cùng với chi phí lưu giữ gắn liền với việc nắm giữ tài sản cơ sở đó.*

Trong bài học trước, phương pháp mô phỏng (*replication*) đã được sử dụng để minh họa mối quan hệ cơ bản giữa việc tham gia vào một giao dịch giao ngay so với một cam kết kỳ hạn. Mối liên kết giữa giá giao ngay của một tài sản không có các dòng tiền đi kèm và một cam kết kỳ hạn trên cùng tài sản đó đã được chứng minh chính là lãi suất phi rủi ro, $r$. Trong bài học này, chúng ta thảo luận về **chi phí lưu giữ (*cost of carry*)** với tư cách là giá trị ròng của các chi phí và lợi ích liên quan đến việc sở hữu một tài sản cơ sở trong một khoảng thời gian cụ thể.

Trong ví dụ về cam kết kỳ hạn từ bài học trước, nơi không có chi phí hay lợi ích nào gắn liền với tài sản cơ sở, mối quan hệ sau đây giữa giá giao ngay và giá kỳ hạn đã được thiết lập:

![](assets/Derivatives.pdf-0096-11.png)

$$F_0(T) = S_0(1 + r)^T \tag{3}$$

Mối quan hệ này được biểu diễn dưới dạng ghép lãi liên tục trong Phương trình 4:

$$F_0(T) = S_0 e^{rT} \tag{4}$$

Lãi suất phi rủi ro, $r$, biểu thị **chi phí cơ hội (*opportunity cost*)** của việc nắm giữ (“**lưu giữ**” – *carrying*) tài sản, bất kể nhà đầu tư nắm giữ vị thế mua có đi vay để tài trợ cho việc mua tài sản đó hay không. Chi phí cơ hội này hiện diện đối với tất cả các loại tài sản được thảo luận dưới đây.

Phương trình 3 và 4 đại diện cho trường hợp đặc biệt của một tài sản cơ sở không có thêm các dòng tiền đi kèm. Tuy nhiên, nhiều tài sản có thêm các chi phí hoặc lợi ích từ quyền sở hữu mà bắt buộc phải được phản ánh vào mức giá cam kết kỳ hạn nhằm ngăn chặn các cơ hội kinh doanh chênh lệch giá phi rủi ro phát sinh giữa giá giao ngay của tài sản cơ sở và giá công cụ phái sinh. Bảng minh họa 7 minh họa tác động của các chi phí và lợi ích (thường là thu nhập cổ tức hoặc tiền lãi) lên mối quan hệ giữa giá giao ngay, giá cam kết kỳ hạn và lãi suất phi rủi ro.


<!-- PDF Page 97 -->

#### **Bảng minh họa 7: Giá Giao ngay, Giá Cam kết Kỳ hạn và Lãi suất Phi rủi ro khi Tài sản Cơ sở có Chi phí và Lợi ích (*Spot Prices, Forward Commitment Prices, and the Risk-Free Rate with Underlying Asset Costs and Benefits*)**

![](assets/Derivatives.pdf-0097-03.png)

> **Chú thích hình ảnh:**
> Xuất phát từ mức giá giao ngay $S_0$ tại thời điểm $0$ đến thời điểm $T$:
> - Đường cơ sở (chỉ có lãi suất phi rủi ro $r$): tiến tới $F_0(T)$.
> - Khi Chi phí $>$ Lợi ích (*Cost > Benefit*): đường giá kỳ hạn dịch chuyển lên cao hơn tới mức $F_0^+(T)$.
> - Khi Lợi ích $>$ Chi phí (*Benefit > Cost*): đường giá kỳ hạn dịch chuyển xuống thấp hơn tới mức $F_0^-(T)$.

Nếu người sở hữu tài sản cơ sở phải chịu thêm các khoản chi phí ngoài chi phí cơ hội, người đó sẽ kỳ vọng được đền bù cho những chi phí tăng thêm này thông qua một mức giá kỳ hạn cao hơn, $F_0^+(T)$. Thu nhập hoặc các lợi ích khác thuộc về người sở hữu tài sản cơ sở và do đó sẽ làm giảm mức giá kỳ hạn xuống còn $F_0^-(T)$.

Đối với các tài sản cơ sở có lợi ích hoặc thu nhập từ quyền sở hữu ($I$) hoặc chi phí ($C$) được biểu thị dưới dạng một *số tiền đã biết tính theo giá trị hiện tại tại thời điểm $t = 0$* — ký hiệu là $\text{PV}_0()$ — mối quan hệ giữa giá giao ngay và giá kỳ hạn theo phương pháp ghép lãi rời rạc có thể được biểu diễn như sau:

$$F_0(T) = [S_0 - \text{PV}_0(I) + \text{PV}_0(C)](1 + r)^T \tag{5}$$

Trong các trường hợp khác, những chi phí hoặc lợi ích bổ sung được biểu thị dưới dạng một *tỷ suất sinh lợi* (*rate of return*) trong suốt vòng đời của hợp đồng. Đối với tỷ suất thu nhập ($i$) và tỷ suất chi phí ($c$) được biểu thị dưới dạng tỷ lệ phần trăm, mối quan hệ giữa giá giao ngay và giá kỳ hạn theo phương pháp ghép lãi liên tục là:

$$F_0(T) = S_0 e^{(r + c - i)T} \tag{6}$$

Cho dù được biểu thị dưới dạng một số tiền đã biết tính theo giá trị hiện tại hay dưới dạng một tỷ suất sinh lợi, giá kỳ hạn bắt buộc phải kết hợp tác động ròng của tất cả các chi phí và lợi ích gắn liền với việc sở hữu tài sản cơ sở, bao gồm những yếu tố sau đây:

- **Chi phí cơ hội (lãi suất phi rủi ro, $r$):** Một mức lãi suất phi rủi ro dương làm cho giá kỳ hạn lớn hơn giá giao ngay của tài sản cơ sở, khi các yếu tố khác không đổi (*all else equal*), và lãi suất phi rủi ro càng cao thì khoản chênh lệch dương giữa hai mức giá càng lớn. Chi phí cơ hội này áp dụng cho bất kỳ tài sản nào.

- **Các chi phí sở hữu khác ($C$, $c$):** Người sở hữu một số tài sản cơ sở, chẳng hạn như hàng hóa vật chất, phải gánh chịu các chi phí lưu kho (*storage*), vận chuyển (*transportation*), bảo hiểm (*insurance*), và/hoặc hư hỏng (*spoilage*). Một người sở hữu tham gia vào hợp đồng giao hàng trong tương lai sẽ kỳ vọng được đền bù cho những chi phí này, dẫn đến một mức giá kỳ hạn lớn hơn giá giao ngay của tài sản cơ sở, khi các yếu tố khác không đổi.

- **Lợi ích của quyền sở hữu ($I$, $i$):** Ngược lại, người sở hữu một số tài sản cơ sở được hưởng dòng tiền hoặc các lợi ích khác gắn liền với việc trực tiếp sở hữu tài sản cơ sở đó so với việc nắm giữ một công cụ phái sinh trên tài sản đó. Một đối tác tham gia vào hợp đồng phái sinh để nhận giao hàng tài sản cơ sở trong tương lai sẽ từ bỏ những lợi ích này và do đó sẽ giảm mức giá kỳ hạn đi một lượng tương ứng. Cổ tức cổ phiếu (*stock dividends*) hoặc lãi trái phiếu định kỳ (*bond coupons*) là những ví dụ về lợi ích dòng tiền.

Bảng minh họa 8 minh họa mối quan hệ giữa giá kỳ hạn và giá giao ngay khi có sự hiện diện của các chi phí và lợi ích. Ví dụ, khi chi phí cơ hội và các chi phí sở hữu khác vượt quá lợi ích, giá kỳ hạn sẽ nằm trên mức giá giao ngay của tài sản cơ sở.


<!-- PDF Page 98 -->

**Bảng minh họa 8: Giá Kỳ hạn so với Giá Giao ngay (*Forward vs. Spot Price*)**

|**Chi phí so với Lợi ích (*Cost vs. Benefit*)**|**Giá Kỳ hạn so với Giá Giao ngay (*Forward vs. Spot Price*)**|
|---|---|
|Chi phí Cơ hội và Chi phí Khác $>$ Lợi ích|$F_0(T) > S_0$|
|Chi phí Cơ hội và Chi phí Khác $<$ Lợi ích|$F_0(T) < S_0$|
|Chi phí Cơ hội và Chi phí Khác $=$ Lợi ích|$F_0(T) = S_0$|

Mỗi loại tài sản cơ sở có những chi phí và lợi ích khác nhau, có thể thay đổi theo thời gian và giữa các thị trường. Ví dụ, người sở hữu một số chứng khoán vốn cổ phần riêng lẻ nhận được lợi ích từ cổ tức cổ phiếu định kỳ, như trong Ví dụ 4, trong khi những cổ phiếu khác thì không. Đối với các chỉ số cổ phiếu (*equity indexes*), lợi ích thường được biểu thị dưới dạng một tỷ suất sinh lợi (tỷ suất cổ tức), như được thể hiện trong Ví dụ 5.

#### **VÍ DỤ 4 (*EXAMPLE 4*)**

### **Hợp đồng Kỳ hạn Cổ phiếu có Cổ tức của Hightest (*Hightest Equity Forward with Dividend*)**

Giả sử Hightest Capital đồng ý chuyển giao $1,000$ cổ phiếu Unilever (UL) tại một mức giá thỏa thuận trước cho một định chế tài chính trung gian sau sáu tháng theo một hợp đồng kỳ hạn. Giả sử UL có giá giao ngay ($S_0$) là $\text{EUR}50$ và không trả cổ tức ($I = 0$), đồng thời giả sử lãi suất phi rủi ro ($r$) là $5\%$. Chúng ta có thể sử dụng Phương trình 3 để giải tìm giá kỳ hạn, $F_0(T)$, sau sáu tháng:

$$F_0(T) = S_0(1 + r)^T$$

$$\text{EUR}51.23 = \text{EUR}50(1.05)^{0.5}$$

Bây giờ, giả sử thay vào đó Unilever trả cổ tức hàng quý là $\text{EUR}0.30$, diễn ra sau đúng ba tháng nữa và một lần nữa tại thời điểm $T$, với các thông tin chi tiết khác giữ nguyên không đổi. Sử dụng Phương trình 5 với $\text{PV}_0(C) = 0$ để giải tìm $F_0(T)$ sau sáu tháng:

$$F_0(T) = [S_0 - \text{PV}_0(I)](1 + r)^T$$

Trước tiên, giải tìm giá trị hiện tại của cổ tức trên mỗi cổ phiếu, $\text{PV}_0(I)$, như sau:

$$\text{PV}_0(I) = \text{EUR}0.30(1.05)^{-0.25} + \text{EUR}0.30(1.05)^{-0.5}$$

$$\text{EUR}0.5892 = 0.2964 + 0.2928$$

Thay $\text{PV}_0(I) = \text{EUR}0.5892$ vào Phương trình 5 để giải tìm $F_0(T)$:

$$F_0(T) = (\text{EUR}50 - \text{EUR}0.5892)(1.05)^{0.5}$$

$$= \text{EUR}50.6310$$

Do đó, hợp đồng kỳ hạn của Hightest đối với $1,000$ cổ phiếu UL sẽ được định giá ở mức $\text{EUR}50,631.00$ ($= 1,000 \times \text{EUR}50.6310$). Chi phí cơ hội của việc đi vay ở mức lãi suất phi rủi ro là $\text{EUR}1.23$ trên mỗi cổ phiếu trong sáu tháng và bằng $F_0(T) - S_0$ khi Unilever không trả cổ tức. Khoản cổ tức hàng quý $\text{EUR}0.30$ làm giảm mức chênh lệch giữa giá kỳ hạn và giá giao ngay xuống còn xấp xỉ $\text{EUR}0.63$.


<!-- PDF Page 99 -->

#### **VÍ DỤ 5 (*EXAMPLE 5*)**

### **Hợp đồng Tương lai Chỉ số Cổ phiếu có Tỷ suất Cổ tức (*Stock Index Futures with Dividend Yield*)**

Văn phòng Quản lý Tài sản Gia đình Viswan (VFO) muốn tham gia vào một hợp đồng cam kết kỳ hạn ba tháng để mua chỉ số thị trường chứng khoán Ấn Độ chuẩn NIFTY 50 được giao dịch trên Sở Giao dịch Chứng khoán Quốc gia (*National Stock Exchange*). Mức giá giao ngay của chỉ số NIFTY 50 là $\text{INR}15,200$, tỷ suất cổ tức của chỉ số (*index dividend yield*) là $2.2\%$, và lãi suất phi rủi ro của đồng rupee Ấn Độ là $4\%$. Sử dụng Phương trình 6 (với $c = 0$) để giải tìm mức giá kỳ hạn:

$$F_0(T) = S_0 e^{(r + c - i)T} = 15,200 e^{(0.04 - 0.022) \times 0.25} = \text{INR}15,268.55$$

Ngoại hối (*foreign exchange* – FX) đòi hỏi một số điều chỉnh để thiết lập điều kiện không có kinh doanh chênh lệch giá giữa giá giao ngay và giá kỳ hạn, như đã trình bày trong bài học trước. Trước hết, điều quan trọng là phải phân biệt “mức giá” của tài sản cơ sở: đối với cổ phiếu, thu nhập cố định hoặc hàng hóa, giá đề cập đến số đơn vị tiền tệ cho mỗi tài sản — ví dụ, một cổ phiếu hoặc số tiền gốc của một trái phiếu. Ngược lại, tỷ giá hối đoái được biểu thị dưới dạng một tỷ giá giao ngay ($S_{0,f/d}$) quy định số đơn vị của *đồng tiền định giá* (*price currency* — ở đây ký hiệu là $f$ hay đồng ngoại tệ) ở tử số trên *một* đơn vị của *đồng tiền yết giá / đồng tiền cơ sở* (*base currency* — ở đây ký hiệu là $d$ hay đồng nội tệ) ở mẫu số. Ví dụ, đối với tỷ giá giao ngay USD/EUR ($S_{0,f/d}$) là $1.20$, đồng đô la Mỹ là đồng tiền định giá ($f$), và đồng euro là đồng tiền cơ sở ($d$), với $\text{USD}1.20$ đổi được $\text{EUR}1$.

Một hợp đồng kỳ hạn ngoại hối (*FX forward contract*) bao gồm việc bán một đồng tiền này và mua một đồng tiền khác vào một ngày trong tương lai tại mức giá kỳ hạn ($F_{0,f/d}$) được thỏa thuận ngay từ khi khởi tạo. Một vị thế *mua* kỳ hạn ngoại hối (*long FX forward position*) bao gồm việc *mua* đồng tiền cơ sở (*base currency*) và *bán* đồng tiền định giá (*price currency*). Ví dụ, một vị thế mua kỳ hạn ngoại hối USD/EUR là việc bán đô la Mỹ và mua đồng euro tại một mức tỷ giá kỳ hạn.

Trong ví dụ mô phỏng trước đó, chuỗi dòng tiền của công cụ phái sinh được tái tạo bằng cách kết hợp một vị thế mua hoặc bán đối với một tài sản cơ sở cùng với việc đi vay hoặc cho vay tiền mặt. Ở đây, *mỗi* đồng ngoại tệ và đồng nội tệ đều có một chi phí cơ hội riêng — cụ thể là lãi suất phi rủi ro của đồng ngoại tệ ($r_f$) và lãi suất phi rủi ro của đồng nội tệ ($r_d$) tương ứng.

#### **VÍ DỤ 6 (*EXAMPLE 6*)**

### **Mô phỏng Hợp đồng Kỳ hạn Ngoại hối AUD/USD (*AUD/USD Foreign Exchange Forward Replication*)**

Để mô phỏng mức sinh lợi của một đồng tiền tính theo đồng tiền kia đối với một mức giá giao ngay cho trước ngày hôm nay là $S_{0,f/d}$, chúng ta có thể giải tìm tỷ giá kỳ hạn $F_{0,f/d}(T)$ bằng cách sử dụng khái niệm kinh doanh chênh lệch giá trước đó rằng các tài sản có mức giá tương lai đã biết phải có giá giao ngay ($S_{0,f/d}$) bằng với mức giá tương lai được chiết khấu theo lãi suất phi rủi ro.

Giả sử tỷ giá giao ngay AUD/USD hiện tại là $1.3335$. Đồng đô la Úc (AUD) là đồng tiền định giá hay ngoại tệ ($f$), và đồng đô la Mỹ (USD) là đồng tiền cơ sở hay nội tệ ($d$) ($\text{AUD}1.3335 = \text{USD}1$). Lãi suất phi rủi ro sáu tháng của đồng đô la Úc là $0.05\%$, và lãi suất phi rủi ro sáu tháng của đồng đô la Mỹ là $0.20\%$.

- Tại thời điểm $t = 0$:

   **1.** Vay $\text{USD}1,000$ tại mức lãi suất phi rủi ro của đồng đô la Mỹ là $0.20\%$ trong sáu tháng.

   **2.** Mua $\text{AUD}1,333.50$ tại mức tỷ giá giao ngay AUD/USD ($S_{0,f/d} = 1.3335$).

   **3.** Cho vay số tiền $\text{AUD}1,333.50$ nhận được tại mức lãi suất phi rủi ro của đồng đô la Úc là $0.05\%$ trong sáu tháng.


<!-- PDF Page 100 -->

- Tại thời điểm $t = T$ sau sáu tháng:

   **4.** Nhận số tiền thu hồi từ khoản cho vay bằng đô la Úc là $1,333.83$ ($= 1,333.50 e^{(0.0005 \times 0.5)}$).

   **5.** Đổi số tiền đô la Úc thu được sang đô la Mỹ tại mức tỷ giá $S_{T,f/d}$ để hoàn trả khoản vay đô la Mỹ.

   **6.** Hoàn trả khoản vay đô la Mỹ (kèm tiền lãi) là $1,001$ ($= 1,000 e^{(0.002 \times 0.5)}$).

Nếu giao dịch chuyển đổi ở Bước 5 tại thời điểm $T$ diễn ra ở một mức giá giao ngay, $S_{T,f/d}$, mà tại đó số tiền thu được từ khoản cho vay đô la Úc (Bước 4) bù trừ chính xác cho khoản vay đô la Mỹ (Bước 6), thì sẽ không tồn tại cơ hội kinh doanh chênh lệch giá phi rủi ro. Giải tìm $S_{T,f/d}$ bằng cách lấy số đô la Úc ở Bước 4 chia cho số đô la Mỹ ở Bước 6:

$$S_{T,f/d} = 1.3325 \quad (= \text{AUD}1,333.83 / \text{USD}1,001)$$

Sơ đồ dưới đây tóm tắt các dòng tiền tại thời điểm $t = 0$ và thời điểm $T$:

![](assets/Derivatives.pdf-0100-10.png)

> **Chú thích hình ảnh:**
> - **Thời điểm $t = 0$:**
>   - Bán USD ($\text{USD}1,000$): Đi vay theo lãi suất $r_{\text{USD}} = r_d = 0.20\%$.
>   - Tỷ giá giao ngay $S_{0,(f/d)} = 1.3335$.
>   - Mua AUD ($\text{AUD}1,333.50$): Cho vay $\text{AUD}1,333.50$ theo lãi suất $r_{\text{AUD}} = r_f = 0.05\%$.
> - **Thời điểm $t = T$:**
>   - Hoàn trả khoản vay USD: $\text{USD}1,000 e^{r_d T} = 1,000 e^{(0.002 \times 0.5)} = \text{USD}1,001$.
>   - Thu về khoản cho vay AUD: $\text{AUD}1,333.50 e^{r_f T} = 1,333.50 e^{(0.0005 \times 0.5)} = \text{AUD}1,333.83$.
>   - Tỷ giá kỳ hạn: $F_{0,(f/d)}(T) = 1.3325 = \frac{\text{AUD}1,333.83}{\text{USD}1,001}$, tức là $F_{0,f/d}(T) = S_{0,f/d} e^{(r_f - r_d)T} = 1.3335 e^{(-0.0015 \times 0.5)} = 1.3325$.

Để điều kiện không có kinh doanh chênh lệch giá được đảm bảo giữa giá giao ngay và giá kỳ hạn ngoại hối, số lượng đô la Úc cần thiết để mua $\text{USD}1$ tại thời điểm $T$ ($F_{0,f/d}(T)$) phải có mức giá giao ngay ($S_{0,f/d}$) bằng với mức giá tương lai đã chiết khấu. Lãi suất chiết khấu phù hợp ở đây liên quan đến *mức chênh lệch* giữa lãi suất phi rủi ro của đồng ngoại tệ và đồng nội tệ, như được thể hiện trong phiên bản điều chỉnh sau đây của Phương trình 4:

![](assets/Derivatives.pdf-0100-12.png)

$$F_{0,f/d}(T) = S_{0,f/d} e^{(r_f - r_d)T} \tag{7}$$

Giải tìm $F_{0,\text{AUD/USD}}(T)$ trong Ví dụ 6 như sau: $F_{0,f/d}(T) = 1.3325$ ($= 1.3335 e^{(-0.0015 \times 0.5)}$).

Từ Phương trình 7, chúng ta thấy rằng chính *mức chênh lệch* lãi suất phi rủi ro ($r_f - r_d$), chứ không phải mức lãi suất tuyệt đối, mới là yếu tố quyết định mối quan hệ giữa giá ngoại hối giao ngay và kỳ hạn. Ví dụ, trong Ví dụ 6, lãi suất phi rủi ro của đồng đô la Úc thấp hơn $0.15\%$ so với lãi suất của đồng đô la Mỹ ($r_f - r_d < 0$). Việc đi vay ở mức lãi suất đô la Mỹ cao hơn và cho vay ở mức lãi suất đô la Úc thấp hơn dẫn đến một mức giá kỳ hạn không có kinh doanh chênh lệch giá mà tại đó cần *ít* đô la Úc hơn để mua $\text{USD}1$ trong tương lai, vì vậy đồng đô la Úc được gọi là giao dịch ở mức *gia tăng* (*at a premium* — thặng dư/cao giá kỳ hạn) trên thị trường kỳ hạn so với đồng đô la Mỹ. Bảng minh họa 9 tóm tắt mối quan hệ giữa giá ngoại hối kỳ hạn và giao ngay.


<!-- PDF Page 101 -->

**Bảng minh họa 9: Mối quan hệ giữa Giá Kỳ hạn và Giá Giao ngay Ngoại hối (*FX Forward vs. Spot Price Relationship*)**

|**Chênh lệch Lãi suất (*Interest Rate Differential*)**|**Giá Kỳ hạn so với Giá Giao ngay (*Forward vs. Spot Price*)**|**Kỳ hạn Đồng Ngoại tệ / Đồng Định giá (*Foreign Currency Forward*)**|**Phần bù / Chiết khấu Kỳ hạn FX (của Đồng Cơ sở) (*FX Forward Premium/Discount*)**|
|---|---|---|---|
|$(r_f - r_d) > 0$|$F_{0,f/d}(T) > S_{0,f/d}$|Chiết khấu (*Discount*)|Phần bù / Gia tăng (*Premium*)|
|$(r_f - r_d) < 0$|$F_{0,f/d}(T) < S_{0,f/d}$|Phần bù / Gia tăng (*Premium*)|Chiết khấu (*Discount*)|
|$(r_f - r_d) = 0$|$F_{0,f/d}(T) = S_{0,f/d}$|Không gia tăng cũng không chiết khấu (*Neither a premium nor a discount*)|Không gia tăng cũng không chiết khấu (*Neither a premium nor a discount*)|

Bây giờ chúng ta xem xét mối quan hệ giữa giá giao ngay và giá kỳ hạn ngoại hối này trong trường hợp ví dụ về công ty Montau AG từ bài học trước.

#### **VÍ DỤ 7 (*EXAMPLE 7*)**

### **Tỷ giá Kỳ hạn Ngoại hối của Montau AG (*Montau AG’s FX Forward Rate*)**

Một bài học trước đã giới thiệu Montau AG, một nhà sản xuất tư liệu sản xuất của Đức. Montau ký một hợp đồng thương mại với Jeon, Inc., một nhà sản xuất Hàn Quốc, để giao một máy cắt laser với mức giá $\text{KRW}650\text{ triệu}$ sau $75\text{ ngày}$. Montau phải đối mặt với sự lệch pha về mặt thời gian giữa các chi phí phát sinh bằng đồng nội tệ euro và doanh thu bằng đồng euro được hiện thực hóa khi bàn giao máy và bán số đồng won Hàn Quốc nhận được để đổi lấy đồng euro trên thị trường ngoại hối giao ngay. Montau tham gia vào một hợp đồng mua kỳ hạn ngoại hối KRW/EUR (*long KRW/EUR FX forward contract*). Nghĩa là, Montau đồng ý bán đồng won Hàn Quốc và mua đồng euro tại một mức giá cố định, $F_0(T)$, sau $75\text{ ngày}$ nhằm loại bỏ sự lệch pha tỷ giá hối đoái KRW/EUR phát sinh từ hợp đồng xuất khẩu.

Trong phiên bản này của ví dụ về Montau AG, chúng ta sử dụng tỷ giá hối đoái giao ngay ngày hôm nay cùng với lãi suất phi rủi ro của đồng nội tệ ($r_d$) và đồng ngoại tệ ($r_f$) để giải tìm tỷ giá kỳ hạn KRW/EUR. Như đã thấy trong Phương trình 7, sự khác biệt giữa tỷ giá ngoại hối giao ngay và kỳ hạn liên quan đến *mức chênh lệch* trong lãi suất phi rủi ro. Trong trường hợp KRW/EUR, đồng won Hàn Quốc là đồng tiền định giá hay ngoại tệ và do đó $r_f$ là lãi suất đồng won Hàn Quốc. Đồng euro là đồng tiền cơ sở hay nội tệ. Do đó, chúng ta có thể viết lại Phương trình 7 như sau:

$$F_{0,\text{KRW/EUR}}(T) = S_{0,\text{KRW/EUR}} e^{(r_{\text{KRW}} - r_{\text{EUR}})T}$$

Giả sử tỷ giá giao ngay KRW/EUR ($S_0$) là $1,300$ (tức là $\text{KRW}1,300 = \text{EUR}1$), lãi suất phi rủi ro của đồng won Hàn Quốc là $0.75\%$, và lãi suất phi rủi ro của đồng euro là $-0.25\%$ ($r_d$). Hãy tính tỷ giá kỳ hạn KRW/EUR sau $75\text{ ngày}$ nhất quán với điều kiện không có kinh doanh chênh lệch giá.

$$F_{0,\text{KRW/EUR}}(T) = 1,300 \times e^{(0.0075 - (-0.0025)) \times (75/365)} = 1,300 \times e^{(0.0075 + 0.0025) \times (75/365)}$$

Giải tìm tỷ giá kỳ hạn KRW/EUR cho chúng ta kết quả $F_0(T) = 1,302.67$. Hãy chú ý rằng mức chênh lệch $1\%$ giữa lãi suất đồng won Hàn Quốc và đồng euro dẫn đến một mức giá kỳ hạn cao hơn giá giao ngay ($F_{0,f/d}(T) > S_{0,f/d}$). Nghĩa là, trong thời gian tới, sẽ cần nhiều đồng won Hàn Quốc hơn để mua một đồng euro, và đồng won Hàn Quốc được gọi là giao dịch ở mức chiết khấu kỳ hạn (*forward discount*) so với đồng euro.

Để chứng minh điều kiện không có kinh doanh chênh lệch giá giữa tỷ giá kỳ hạn và tỷ giá giao ngay, giả sử rằng Montau chuyển đổi $\text{KRW}650\text{ triệu}$ sang đồng euro tại mức tỷ giá giao ngay KRW/EUR là $1,300$ để nhận về $\text{EUR}500,000$ ($= \text{KRW}650,000,000 / 1,300$) và đầu tư số tiền này trong $75\text{ ngày}$ ở mức lãi suất ghép lãi liên tục $r_{\text{EUR}} = -0.25\%$:

$$\text{EUR}499,743.22 = \text{EUR}500,000 \times e^{[-0.0025 \times (75/365)]}$$

Giả sử rằng Jeon Inc. đầu tư $\text{KRW}650\text{ triệu}$ ở mức lãi suất phi rủi ro của đồng won Hàn Quốc ($r_{\text{KRW}} = 0.75\%$) trong $75\text{ ngày}$ để nhận về:

$$\text{KRW}651,002,484.59 = \text{KRW}650,000,000 \times e^{[0.0075 \times (75/365)]}$$


<!-- PDF Page 102 -->

Do đó, một mức giá cam kết kỳ hạn không có kinh doanh chênh lệch giá phải cho phép Montau chuyển đổi $\text{KRW}651,002,484.59$ thành $\text{EUR}499,743.22$ sau $75\text{ ngày}$:

$$F_0(T) = 651,002,484.59 / 499,743.22 = 1,302.67$$

Điều này xác nhận rằng hai mức giá (tỷ giá hối đoái giao ngay và kỳ hạn) hoàn toàn nhất quán với mức chênh lệch lãi suất phi rủi ro giữa hai đồng tiền khác nhau.

Trái ngược với chứng khoán hoặc tiền mặt được lưu trữ dưới dạng điện tử, hàng hóa (*commodities*) thường liên quan đến các khoản chi phí đã biết gắn liền với việc lưu kho (*storage*), bảo hiểm (*insurance*), vận chuyển (*transportation*), và khả năng hư hỏng (*spoilage* — trong trường hợp hàng hóa nông sản/mềm (*soft commodities*)) của những tài sản vật chất này. Một lợi ích phi tiền mặt của việc nắm giữ một hàng hóa vật chất so với một công cụ phái sinh được gọi là **lợi suất tiện ích (*convenience yield*)**. Trên các thị trường hàng hóa vật chất, những điều kiện kinh tế có thể phát sinh khiến cho những người tham gia thị trường ưu tiên việc trực tiếp sở hữu hàng hóa vật chất hơn. Lấy một ví dụ đơn giản, nếu lượng tồn kho dầu thô ở mức rất thấp, các nhà máy lọc dầu có thể trả giá đẩy giá dầu giao ngay lên cao đến mức giá kỳ hạn không còn phản ánh đầy đủ chi phí lưu kho và lãi suất. Ví dụ sau đây minh họa tác động của những chi phí lưu giữ này lên mối quan hệ giữa giá giao ngay và giá cam kết kỳ hạn đối với một hàng hóa, cũng như khả năng xuất hiện của lợi suất tiện ích.

#### **VÍ DỤ 8 (*EXAMPLE 8*)**

### **Hợp đồng Kỳ hạn Vàng của Procam khi có Chi phí Lưu kho (*Procam’s Gold Forward Contract with Storage Costs*)**

Hãy nhớ lại từ các ví dụ trước rằng Procam đã đi vay và mua vàng trên thị trường giao ngay đồng thời bán vàng trên thị trường kỳ hạn ba tháng để kiếm một khoản lợi nhuận phi rủi ro. Dưới giả định lãi suất phi rủi ro là $2\%$, chúng ta đã chứng minh rằng giá vàng giao ngay ($S_0$) sẽ cần phải tăng lên mức $\text{USD}1,783.28$ ($= \text{USD}1,792.13(1.02)^{-0.25}$) để triệt tiêu cơ hội kinh doanh chênh lệch giá trước đó đối với một mức giá kỳ hạn cho trước là $\text{USD}1,792.13$ khi vàng có thể được lưu kho mà không tốn chi phí.

Với mức giá giao ngay là $\text{USD}1,783.28$, giá vàng kỳ hạn sẽ thay đổi như thế nào để thỏa mãn điều kiện không có kinh doanh chênh lệch giá nếu chúng ta đưa thêm vào khoản chi phí lưu kho và bảo hiểm vàng là $\text{USD}2$ mỗi ounce, thanh toán vào thời điểm kết thúc hợp đồng?

Mức giá cam kết kỳ hạn đối với một hàng hóa có số tiền chi phí lưu kho đã biết có thể được xác định bằng cách sử dụng Phương trình 5, trong đó $\text{PV}_0(I) = 0$:

$$F_0(T) = [S_0 + \text{PV}_0(C)](1 + r)^T$$

Trước tiên, giải tìm giá trị hiện tại của chi phí lưu kho trên mỗi ounce $\text{PV}_0(C)$ như sau:

$$\text{PV}_0(C) = \text{USD}2(1.02)^{-0.25} = \text{USD}1.99$$

Thay $\text{PV}_0(C) = \text{USD}1.99$ vào Phương trình 5 để giải tìm $F_0(T)$:

$$F_0(T) = (\text{USD}1,783.28 + \text{USD}1.99)(1.02)^{0.25} = \text{USD}1,794.13$$

Lưu ý rằng việc bổ sung thêm chi phí lưu kho và bảo hiểm làm gia tăng khoản chênh lệch giữa giá giao ngay và giá kỳ hạn. Cuối cùng, lưu ý rằng một mức giá kỳ hạn, $F_0(T)$, thấp hơn đáng kể so với mức giá không có kinh doanh chênh lệch giá có thể là dấu hiệu cho thấy sự hiện diện của lợi suất tiện ích (*convenience yield*).

Các chi phí và lợi ích bổ sung của việc sở hữu tài sản cơ sở được tóm tắt trong Bảng minh họa 10.


<!-- PDF Page 103 -->

**Bảng minh họa 10: Chi phí Lưu giữ đối với các Tài sản Cơ sở (*Cost of Carry for Underlying Assets*)**

|**Loại Tài sản (*Asset Class*)**|**Ví dụ (*Examples*)**|**Lợi ích (*Benefits* – $i$)**|**Chi phí (*Costs* – $r, c$)**|
|---|---|---|---|
|Tài sản không có Dòng tiền (*Asset without Cash Flows*)|Cổ phiếu không trả cổ tức (*Non-dividend-paying stock*)|Không có (*None*)|Lãi suất phi rủi ro (*Risk-free rate*)|
|Cổ phiếu (*Equities*)|Cổ phiếu có trả cổ tức (*Dividend-paying stocks*)<br>Chỉ số cổ phiếu (*Equity indexes*)|Cổ tức (*Dividend*)<br>Tỷ suất cổ tức (*Dividend yield*)|Lãi suất phi rủi ro (*Risk-free rate*)|
|Ngoại hối (*Foreign Exchange*)|Trái phiếu chính phủ nước ngoài (*Sovereign bonds - foreign*)<br>Tỷ giá hối đoái thị trường (*Market exchange rates*)|Không có (*None*)|Chênh lệch giữa lãi suất phi rủi ro ngoại tệ và nội tệ ($r_f - r_d$)|
|Hàng hóa (*Commodities*)|Hàng hóa mềm và cứng (*Soft and hard commodities*)<br>Chỉ số hàng hóa (*Commodity indexes*)|Lợi suất tiện ích (*Convenience yield*)|Lãi suất phi rủi ro (*Risk-free rate*)<br>Chi phí lưu kho (*Storage cost*)|
|Lãi suất (*Interest Rates*)|Trái phiếu chính phủ trong nước (*Sovereign bonds - domestic*)<br>Lãi suất tham chiếu thị trường (*Market reference rates*)|Thu nhập tiền lãi (*Interest income*)|Lãi suất phi rủi ro (*Risk-free rate*)|
|Tín dụng (*Credit*)|Thực thể tham chiếu đơn lẻ (*Single reference entity*)<br>Chỉ số tín dụng (*Credit indexes*)|Chênh lệch tín dụng (*Credit spread*)|Lãi suất phi rủi ro (*Risk-free rate*)|

Lãi suất và tín dụng có cấu trúc kỳ hạn (*term structure*) — nghĩa là các mức giá hoặc lãi suất khác nhau cho các kỳ hạn khác nhau. Những hợp đồng kỳ hạn này sẽ được đề cập trong một bài học sau.

#### **BỘ CÂU HỎI (*QUESTION SET*)**

### **Chi phí Lưu giữ (*Cost of Carry*)**

1. Hãy mô tả mối quan hệ giữa giá giao ngay và giá kỳ hạn đối với một tài sản cơ sở mà lợi ích của nó vượt quá chi phí cơ hội và các chi phí sở hữu khác.

#### **Lời giải:**

Nếu những lợi ích dành cho người sở hữu một tài sản cơ sở vượt quá chi phí cơ hội và các chi phí khác của việc sở hữu tài sản cơ sở đó, thì giá giao ngay sẽ lớn hơn giá kỳ hạn ($S_0 > F_0(T)$).

2. Hãy xác định ví dụ nào tương ứng với từng mối quan hệ sau đây giữa giá giao ngay và giá kỳ hạn:

|Mối quan hệ|Ví dụ|
|---|---|
|1. $F_0(T) > S_0$|A. Một trái phiếu trả lãi cố định được định giá ngang mệnh giá (*at par*) có lãi suất coupon cao hơn lãi suất phi rủi ro|
|2. $F_0(T) < S_0$|B. Một hợp đồng kỳ hạn ngoại tệ nơi lãi suất phi rủi ro của đồng ngoại tệ lớn hơn lãi suất phi rủi ro của đồng nội tệ|
|3. Không đủ thông tin để xác định mối quan hệ giữa $F_0(T)$ và $S_0$|C. Một hàng hóa có lợi suất tiện ích cũng như các chi phí lưu kho và bảo hiểm|

#### **Lời giải:**

1. B là đáp án đúng. Tỷ giá kỳ hạn ngoại hối lớn hơn tỷ giá giao ngay nếu lãi suất phi rủi ro của đồng ngoại tệ lớn hơn lãi suất phi rủi ro của đồng nội tệ ($r_f > r_d \Rightarrow F_{0,f/d}(T) > S_{0,f/d}$).


<!-- PDF Page 104 -->

2. A là đáp án đúng. Một trái phiếu trả lãi cố định được định giá ngang mệnh giá có khoản thu nhập vượt quá chi phí cơ hội của lãi suất phi rủi ro, vì vậy $F_0(T) < S_0$.

3. C là đáp án đúng. Chúng ta không có đủ thông tin để đánh giá đầy đủ phần lợi ích (lợi suất tiện ích) so với phần chi phí (lãi suất phi rủi ro, chi phí lưu kho và bảo hiểm) của việc nắm giữ tài sản hàng hóa vật chất trong ví dụ này.

3. Xác định các từ đúng để điền vào chỗ trống: Một mức lãi suất phi rủi ro dương khiến cho giá kỳ hạn \_\_\_\_\_\_\_ hơn giá giao ngay của tài sản cơ sở, khi các yếu tố khác không đổi, và lãi suất phi rủi ro càng cao thì mức chênh lệch giữa hai mức giá càng \_\_\_\_\_\_\_.

#### **Lời giải:**

Một mức lãi suất phi rủi ro dương khiến cho giá kỳ hạn *lớn* (*greater*) hơn giá giao ngay của tài sản cơ sở, khi các yếu tố khác không đổi, và lãi suất phi rủi ro càng cao thì mức chênh lệch giữa hai mức giá càng *lớn* (*greater*).

4. Một nhà phân tích quan sát thấy tỷ giá hối đoái giao ngay MXN/USD hiện tại là $19.50$, lãi suất phi rủi ro sáu tháng của đồng peso Mexico (MXN) là $4\%$, và lãi suất phi rủi ro sáu tháng của đồng đô la Mỹ (USD) là $0.25\%$. Hãy mô tả mối quan hệ giữa tỷ giá giao ngay và tỷ giá kỳ hạn sáu tháng của cặp MXN/USD, đồng thời giải thích câu trả lời của bạn.

#### **Lời giải:**

Mối quan hệ giữa giá giao ngay và giá kỳ hạn ngoại hối MXN/USD phụ thuộc vào mức chênh lệch lãi suất phi rủi ro giữa đồng peso Mexico và đồng đô la Mỹ ($r_f - r_d > 0$, vì $3.75\% = 4.0\% - 0.25\%$). Vì lãi suất đồng peso Mexico cao hơn $3.75\%$ so với lãi suất đồng đô la Mỹ, chúng ta kỳ vọng rằng việc đi vay ở mức lãi suất đồng peso Mexico cao hơn và cho vay ở mức lãi suất đồng đô la Mỹ thấp hơn sẽ dẫn đến một mức giá kỳ hạn không có kinh doanh chênh lệch giá mà tại đó cần nhiều đồng peso Mexico hơn để mua $\text{USD}1$ trong tương lai, vì vậy đồng peso Mexico được gọi là giao dịch ở mức chiết khấu (*at a discount*) trên thị trường kỳ hạn so với đồng đô la Mỹ ($F_{0,\text{MXN/USD}}(T) > S_{0,\text{MXN/USD}}$).

Chúng ta có thể chứng minh điều này bằng cách sử dụng Phương trình 7 cho trường hợp MXN/USD như sau:

$$F_{0,\text{MXN/USD}}(T) = S_{0,\text{MXN/USD}} e^{(r_{\text{MXN}} - r_{\text{USD}})T}$$

Dựa trên mức tỷ giá hiện tại $S_{0,f/d}$ là $19.50$, $r_f = 4\%$, $r_d = 0.25\%$, và $T = 0.5$, chúng ta có thể giải tìm mức giá kỳ hạn không có kinh doanh chênh lệch giá, $F_{0,f/d}$, như sau:

$$F_{0,\text{MXN/USD}}(T) = 19.50 e^{[(0.04 - 0.0025) \times 0.5]} = 19.8691$$

5. Giả sử các quy định môi trường mới, nghiêm ngặt hơn gắn liền với việc lưu kho và bảo hiểm dầu mỏ khiến cho chi phí của các dịch vụ này tăng vọt. Hãy mô tả tác động dự kiến của những chi phí gia tăng này lên mối quan hệ giữa giá dầu giao ngay và giá cam kết kỳ hạn.

#### **Lời giải:**

Những người sở hữu hàng hóa vật chất phải gánh chịu chi phí lưu kho và bảo hiểm theo thời gian luôn kỳ vọng sẽ được đền bù bằng mức giá cam kết kỳ hạn cao hơn cho việc giao hàng tài sản cơ sở trong tương lai. Giả sử các yếu tố khác không đổi, chi phí lưu kho và bảo hiểm cao hơn do đó sẽ dẫn đến mức giá cam kết kỳ hạn cao hơn và làm tăng khoản chênh lệch giữa giá giao ngay và giá kỳ hạn. Như được thể hiện trong Phương trình 5, sự gia tăng trong $C$ sẽ làm tăng $F_0(T)$ đối với một mức giá $S_0$ cho trước:


<!-- PDF Page 105 -->

$$F_0(T) = [S_0 - \text{PV}_0(I) + \text{PV}_0(C)](1 + r)^T \tag{8}$$


<!-- PDF Page 106 -->
