# Tập 1: Phương pháp Định lượng (Volume 1: Quantitative Methods)
## Học phần 1: Lãi suất và Tỷ suất sinh lợi (Learning Module 1: Rates and Returns)
### Phần 2/3: Tỷ suất sinh lợi có trọng số tiền tệ và Tỷ suất sinh lợi có trọng số thời gian (Money-Weighted and Time-Weighted Return) (Trang PDF 27–40)

---

<!-- PDF Page 27 -->

$$\bar{R} = 30,0\% / 10 = 3,0\%$$

2. Tỷ suất sinh lợi trung bình nhân (*geometric mean return*) trong 10 năm _gần nhất_ với mức nào sau đây:
   - **A.** $2,94\%$.
   - **B.** $2,97\%$.
   - **C.** $3,00\%$.

   - **Lời giải (Solution):** 

B là đáp án đúng. Tỷ suất sinh lợi trung bình nhân được tính như sau:

$$\bar{R}_G = \sqrt[10]{(1 + 0,045) \times (1 + 0,06) \times \dots \times (1 + 0,055) \times (1 + 0,04)} - 1$$

$$\bar{R}_G = \sqrt[10]{1,3402338} - 1 = 2,9717\%$$

## **TỶ SUẤT SINH LỢI CÓ TRỌNG SỐ TIỀN TỆ VÀ TỶ SUẤT SINH LỢI CÓ TRỌNG SỐ THỜI GIAN (MONEY-WEIGHTED AND TIME-WEIGHTED RETURN)** 

# **<mark>4</mark>** 

so sánh tỷ suất sinh lợi có trọng số tiền tệ (*money-weighted rate of return*) và tỷ suất sinh lợi có trọng số thời gian (*time-weighted rate of return*), đồng thời đánh giá hiệu quả hoạt động của các danh mục đầu tư dựa trên các thước đo này

Các phép tính tỷ suất sinh lợi trung bình cộng và trung bình nhân không tính đến thời điểm của các dòng tiền đi vào và đi ra khỏi một danh mục đầu tư. Ví dụ, giả sử một nhà đầu tư trải qua các mức tỷ suất sinh lợi được thể hiện trong Bảng 2 (*Exhibit 2*). Thay vì chỉ đầu tư $1,0\text{ EUR}$ lúc bắt đầu (Năm 0) như trong trường hợp ở Bảng 2, giả sử nhà đầu tư đã đầu tư $10.000\text{ EUR}$ lúc bắt đầu, $1.000\text{ EUR}$ vào Năm 1, và $1.000\text{ EUR}$ vào Năm 2. Trong trường hợp đó, mức tỷ suất sinh lợi $-50\%$ vào Năm 1 gây thiệt hại đáng kể cho cô ấy do khoản đầu tư tương đối lớn ngay từ lúc bắt đầu. Ngược lại, nếu cô ấy chỉ đầu tư $100\text{ EUR}$ lúc bắt đầu, tác động tuyệt đối của mức tỷ suất sinh lợi $-50\%$ lên tổng tỷ suất sinh lợi sẽ giảm đi rất nhiều.

### **Tính Tỷ suất sinh lợi có trọng số tiền tệ (Calculating the Money Weighted Return)** 

**Tỷ suất sinh lợi có trọng số tiền tệ (*money-weighted return*)** tính đến số tiền được đầu tư và cung cấp cho nhà đầu tư thông tin về mức tỷ suất sinh lợi thực tế mà họ kiếm được trên khoản đầu tư của mình. Tỷ suất sinh lợi có trọng số tiền tệ và cách tính của nó tương tự như tỷ suất hoàn vốn nội bộ (*internal rate of return – IRR*) và lợi suất đáo hạn (*yield to maturity – YTM*) của trái phiếu. Các khoản tiền đem đi đầu tư là dòng tiền ra (*cash outflows*) dưới góc độ của nhà đầu tư, còn các khoản tiền được hoàn trả hoặc rút ra bởi nhà đầu tư, hay số tiền còn lại vào cuối một chu kỳ đầu tư, là dòng tiền vào (*cash inflow*) đối với nhà đầu tư.

Ví dụ, giả sử một nhà đầu tư đầu tư $100\text{ EUR}$ vào một quỹ tương hỗ vào đầu năm thứ nhất, nộp thêm $950\text{ EUR}$ vào đầu năm thứ hai, và rút ra $350\text{ EUR}$ vào cuối năm thứ hai. Các dòng tiền được trình bày trong Bảng 10 (*Exhibit 10*).

<!-- PDF Page 28 -->

**Bảng 10: Số dư Danh mục đầu tư qua Ba năm (Exhibit 10: Portfolio Balances across Three Years)** 

|**Năm (Year)**|**1**|**2**|**3**|
|---|---|---|---|
|Số dư từ năm trước (*Balance from previous year*)|EUR 0|EUR 50|EUR 1.000|
|Khoản đầu tư mới của nhà đầu tư (dòng tiền vào đối với quỹ tương hỗ) vào đầu năm (*New investment by the investor at the start of the year*)|100|950|0|
|Số dư ròng vào đầu năm (*Net balance at the beginning of year*)|100|1.000|1.000|
|Tỷ suất sinh lợi đầu tư trong năm (*Investment return for the year*)|−50%|35%|27%|
|Lãi (lỗ) đầu tư (*Investment gain (loss)*)|−50|350|270|
|Khoản rút tiền của nhà đầu tư (dòng tiền ra đối với quỹ tương hỗ) vào cuối năm (*Withdrawal by the investor at the end of the year*)|0|−350|0|
|Số dư vào cuối năm (*Balance at the end of year*)|EUR 50|EUR 1.000|EUR 1.270|

![](assets/Quantitative_method.pdf-0028-05.png)

Tỷ suất hoàn vốn nội bộ (*internal rate of return – IRR*) là lãi suất chiết khấu mà tại đó tổng giá trị hiện tại của các dòng tiền bằng không. Tổng quát, phương trình này có thể được biểu diễn như sau:

$$\sum_{t=0}^{T} \frac{CF_t}{(1 + \text{IRR})^t} = 0 \tag{5}$$

<!-- Formula Text: The internal rate of return is the discount rate at which the sum of present values of cash flows will equal zero. In general, the equation may be expressed as follows: ∑ t=0 T C F t _ (1 + IRR) t   =  0, (5) -->

trong đó $T$ là số kỳ, $CF_t$ là dòng tiền tại thời điểm $t$, và $\text{IRR}$ là tỷ suất hoàn vốn nội bộ hay tỷ suất sinh lợi có trọng số tiền tệ (*money-weighted rate of return*).

Một dòng tiền có thể mang giá trị dương hoặc âm; dòng tiền dương là dòng tiền vào (*inflow*) khi tiền chảy về phía nhà đầu tư, trong khi dòng tiền âm là dòng tiền ra (*outflow*) khi tiền chảy ra khỏi túi nhà đầu tư. Các dòng tiền được biểu diễn như sau, trong đó mỗi dòng tiền vào hoặc dòng tiền ra phát sinh vào cuối mỗi năm. Như vậy, $CF_0$ chỉ dòng tiền vào cuối Năm 0 hay đầu Năm 1, và $CF_3$ chỉ dòng tiền vào cuối Năm 3 hay đầu Năm 4. Bởi vì các dòng tiền đang được chiết khấu về hiện tại — tức cuối Năm 0 hay đầu Năm 1 — nên số kỳ chiết khấu của $CF_0$ bằng không.

![](assets/Quantitative_method.pdf-0028-08.png)

$$CF_0 = -100$$

<!-- Formula Text: CF 0  =  − 100 -->

![](assets/Quantitative_method.pdf-0028-09.png)

$$\begin{aligned}
CF_1 &= -950 \\
CF_2 &= +350 \\
CF_3 &= +1.270 \\
\frac{CF_0}{(1 + \text{IRR})^0} + \frac{CF_1}{(1 + \text{IRR})^1} + \frac{CF_2}{(1 + \text{IRR})^2} + \frac{CF_3}{(1 + \text{IRR})^3} &= \frac{-100}{1} + \frac{-950}{(1 + \text{IRR})^1} + \frac{+350}{(1 + \text{IRR})^2} + \frac{+1.270}{(1 + \text{IRR})^3} = 0
\end{aligned}$$

<!-- Formula Text: CF 1  =  − 950 CF 2  =  + 350 CF 3  =  + 1, 270 CF 0 _ (1 + IRR) 0  + CF 1 _ (1 + IRR) 1  + CF 2 _ (1 + IRR) 2  + CF 3 _ (1 + IRR) 3 =  − 100 _ 1   + − 950 _ (1 + IRR) 1  + + 350 _ (1 + IRR) 2  +   + 1270 _ (1 + IRR) 3   =  0 . -->

![](assets/Quantitative_method.pdf-0028-10.png)

$$\text{IRR} = 26,11\%$$

<!-- Formula Text: IRR  =  26.11% -->

Tỷ suất hoàn vốn nội bộ của nhà đầu tư, hay tỷ suất sinh lợi có trọng số tiền tệ, là $26,11\%$, cho nhà đầu tư biết mức sinh lợi mà cô ấy kiếm được trên số đồng euro thực tế đã đầu tư trong toàn bộ giai đoạn tính trên cơ sở hàng năm. Mức tỷ suất sinh lợi này lớn hơn nhiều so với tỷ suất sinh lợi trung bình cộng và trung bình nhân bởi vì chỉ có một số tiền nhỏ được đầu tư vào lúc tỷ suất sinh lợi của quỹ tương hỗ là $-50\%$.

Tất cả các phép tính trên có thể được thực hiện bằng Excel thông qua hàm `=IRR(values)`, cho kết quả IRR là $26,11\%$.

#### **_Tỷ suất sinh lợi có trọng số tiền tệ đối với cổ phiếu trả cổ tức (Money-Weighted Return for a Dividend-Paying Stock)_** 

Tiếp theo, chúng ta sẽ minh họa cách tính tỷ suất sinh lợi có trọng số tiền tệ cho một cổ phiếu trả cổ tức. Xét một khoản đầu tư trải dài trong khung thời gian hai năm. Tại thời điểm $t = 0$, một nhà đầu tư mua một cổ phiếu với giá $200\text{ USD}$. Tại thời điểm $t = 1$, ông mua thêm một cổ phiếu nữa với giá $225\text{ USD}$. Vào cuối Năm 2, $t = 2$, ông bán cả hai cổ phiếu với giá $235\text{ USD}$ mỗi cổ phiếu. Trong cả hai năm, cổ phiếu đều trả cổ tức $5\text{ USD}$ mỗi cổ phiếu. Khoản cổ tức tại $t = 1$ không được tái đầu tư. Bảng 11 (*Exhibit 11*) phác thảo tổng các dòng tiền vào và dòng tiền ra của khoản đầu tư này.

<!-- PDF Page 29 -->

**Bảng 11: Dòng tiền của Cổ phiếu trả cổ tức (Exhibit 11: Cash Flows for a Dividend-Paying Stock)** 

|**Thời điểm (Time)**|**Dòng tiền ra (Outflows)**|
|---|---|
|0|$200\text{ USD}$ để mua cổ phiếu thứ nhất|
|1|$225\text{ USD}$ để mua cổ phiếu thứ hai|
|**Thời điểm (Time)**|**Dòng tiền vào (Inflows)**|
|1|$5\text{ USD}$ cổ tức nhận được từ cổ phiếu thứ nhất (và không tái đầu tư)|
|2|$10\text{ USD}$ cổ tức ($5\text{ USD}$ mỗi cổ phiếu $\times$ 2 cổ phiếu) nhận được|
|2|$470\text{ USD}$ nhận được từ việc bán hai cổ phiếu ở mức giá $235\text{ USD}$ mỗi cổ phiếu|

Để giải tìm tỷ suất sinh lợi có trọng số tiền tệ, bước đầu tiên là nhóm các dòng tiền ròng (*net cash flows*) theo thời điểm. Đối với ví dụ này, chúng ta có $-200\text{ USD}$ cho dòng tiền ròng tại $t = 0$, $-220\text{ USD} = -225\text{ USD} + 5\text{ USD}$ cho dòng tiền ròng tại $t = 1$, và $480\text{ USD}$ cho dòng tiền ròng tại $t = 2$. Sau khi nhập các dòng tiền này, chúng ta sử dụng hàm IRR của bảng tính (chẳng hạn như Excel) hoặc của máy tính tài chính để tìm ra tỷ suất sinh lợi có trọng số tiền tệ là $9,39\%$.

$$\begin{aligned}
CF_0 &= -200 \\
CF_1 &= -220 \\
CF_2 &= +480 \\
\frac{CF_0}{(1 + \text{IRR})^0} + \frac{CF_1}{(1 + \text{IRR})^1} + \frac{CF_2}{(1 + \text{IRR})^2} &= \frac{-200}{1} + \frac{-220}{(1 + \text{IRR})^1} + \frac{480}{(1 + \text{IRR})^2} = 0 \\
\text{IRR} &= 9,39\%
\end{aligned}$$

Tất cả các phép tính này có thể được thực hiện bằng Excel thông qua hàm `=IRR(values)`, cho kết quả IRR là $9,39\%$.

Bây giờ chúng ta hãy xem xét kỹ hơn những gì đã xảy ra với danh mục đầu tư trong từng năm của giai đoạn hai năm đó.

Trong năm thứ nhất, danh mục đầu tư đã tạo ra tỷ suất sinh lợi thời kỳ nắm giữ một kỳ là $(\text{5 USD} + \text{225 USD} - \text{200 USD}) / \text{200 USD} = 15\%$. Vào đầu năm thứ hai, số tiền được đầu tư là $450\text{ USD}$, được tính bằng $225\text{ USD}$ (giá mỗi cổ phiếu) $\times$ 2 cổ phiếu, bởi vì khoản cổ tức $5\text{ USD}$ đã được đem đi chi tiêu thay vì tái đầu tư.

Vào cuối năm thứ hai, số tiền thu được từ việc thanh lý danh mục đầu tư là $470\text{ USD}$ cộng với $10\text{ USD}$ tiền cổ tức (như đã nêu trong Bảng 11). Vì vậy, trong năm thứ hai danh mục đầu tư đã tạo ra tỷ suất sinh lợi thời kỳ nắm giữ là $(\text{10 USD} + \text{470 USD} - \text{450 USD}) / \text{450 USD} = 6,67\%$. Tỷ suất sinh lợi thời kỳ nắm giữ trung bình cộng là $(15\% + 6,67\%) / 2 = 10,84\%$.

Tỷ suất sinh lợi có trọng số tiền tệ mà chúng ta đã tính được là $9,39\%$ đặt trọng số lớn hơn vào hiệu quả hoạt động tương đối kém của năm thứ hai ($6,67\%$) so với hiệu quả hoạt động tương đối tốt của năm thứ nhất ($15\%$), bởi vì có nhiều tiền hơn được đầu tư vào năm thứ hai so với năm thứ nhất. Đó chính là ý nghĩa mà theo đó tỷ suất sinh lợi trong phương pháp tính toán hiệu quả hoạt động này được gọi là “có trọng số tiền tệ” (*money weighted*).

Mặc dù tỷ suất sinh lợi có trọng số tiền tệ là một thước đo chính xác về những gì nhà đầu tư đã kiếm được trên số tiền bỏ ra đầu tư, nhưng nó lại bị hạn chế về khả năng áp dụng cho các tình huống khác. Ví dụ, nó không cho phép so sánh tỷ suất sinh lợi giữa các cá nhân khác nhau hoặc giữa các cơ hội đầu tư khác nhau. Quan trọng hơn, hai nhà đầu tư cùng đầu tư vào _một_ quỹ tương hỗ hoặc có cùng một danh mục các khoản đầu tư cơ sở có thể có tỷ suất sinh lợi có trọng số tiền tệ khác nhau bởi vì họ đã đầu tư những số tiền khác nhau vào những năm khác nhau.

<!-- PDF Page 30 -->

#### **VÍ DỤ 8 (EXAMPLE 8)** 

### **Tính toán các Tỷ suất sinh lợi (Computation of Returns)** 

Ulli Lohrmann và vợ ông, Suzanne Lohrmann, đang lập kế hoạch nghỉ hưu và muốn so sánh hiệu quả hoạt động trong quá khứ của một vài quỹ tương hỗ mà họ đang cân nhắc đầu tư. Họ tin rằng việc so sánh trong giai đoạn năm năm sẽ là phù hợp. Họ thu thập thông tin về một quỹ mà họ đang xem xét, Quỹ Rhein Valley Superior (*Rhein Valley Superior Fund*), được trình bày trong Bảng 12 (*Exhibit 12*).

#### **Bảng 12: Hiệu quả hoạt động của Quỹ Rhein Valley Superior (Exhibit 12: Rhein Valley Superior Fund Performance)** 

|**Năm (Year)**|**Tài sản thuộc quyền quản lý vào đầu năm (Assets under Management at the Beginning of Year - euro)**|**Tỷ suất sinh lợi hàng năm (Annual Return) (%)**|
|---|---|---|
|1|30 triệu|15|
|2|45 triệu|−5|
|3|20 triệu|10|
|4|25 triệu|15|
|5|35 triệu|3|

Gia đình Lohrmann quan tâm đến việc tổng hợp thông tin này để dễ dàng so sánh với các quỹ khác.

**Bảng 13: Tỷ suất sinh lợi hàng năm và các Khoản đầu tư của Quỹ Rhein Valley Superior (triệu euro) (Exhibit 13: Rhein Valley Superior Fund Annual Returns and Investments (euro millions))** 

|**Năm (Year)**|**1**|**2**|**3**|**4**|**5**|
|---|---|---|---|---|---|
|Số dư từ năm trước (*Balance from previous year*)|0|34,50|42,75|22,00|28,75|
|Khoản đầu tư mới của nhà đầu tư (dòng tiền vào đối với quỹ Rhein) (*New investment by the investor*)|30,00|10,50|0|3,00|6,25|
|Khoản rút tiền của nhà đầu tư (dòng tiền ra đối với quỹ Rhein) (*Withdrawal by the investor*)|0|0|−22,75|0|0|
|Số dư ròng vào đầu năm (*Net balance at the beginning of year*)|30,00|45,00|20,00|25,00|35,00|
|Tỷ suất sinh lợi đầu tư trong năm (*Investment return for the year*)|15%|–5%|10%|15%|3%|
|Lãi (lỗ) đầu tư (*Investment gain (loss)*)|4,50|–2,25|2,00|3,75|1,05|
|Số dư vào cuối năm (*Balance at the end of year*)|34,50|42,75|22,00|28,75|36,05|

1. Tính tỷ suất sinh lợi thời kỳ nắm giữ của quỹ cho giai đoạn năm năm.

#### **Lời giải (Solution):** 

Tỷ suất sinh lợi thời kỳ nắm giữ năm năm được tính như sau:

$$\begin{aligned}
R &= (1 + R_1)(1 + R_2)(1 + R_3)(1 + R_4)(1 + R_5) - 1 \\
R &= (1,15)(0,95)(1,10)(1,15)(1,03) - 1 \\
R &= 0,4235 = 42,35\%
\end{aligned}$$

2. Tính tỷ suất sinh lợi hàng năm trung bình cộng của quỹ.

#### **Lời giải (Solution):** 

Tỷ suất sinh lợi hàng năm trung bình cộng được tính như sau:

<!-- PDF Page 31 -->

![](assets/Quantitative_method.pdf-0031-02.png)

$$\bar{R}_i = \frac{15\% - 5\% + 10\% + 15\% + 3\%}{5} = 7,60\%$$

<!-- Formula Text: _ R  i  =   15 %  − 5 %  + 10 %  + 15 %  + 3% ________________________ 5 =  7.60%. -->

3. Tính tỷ suất sinh lợi hàng năm trung bình nhân của quỹ. Nó so sánh như thế nào với tỷ suất sinh lợi hàng năm trung bình cộng?

#### **Lời giải (Solution):** 

Tỷ suất sinh lợi hàng năm trung bình nhân có thể được tính như sau:

$$\begin{aligned}
\bar{R}_{Gi} &= \sqrt[5]{1,15 \times 0,95 \times 1,10 \times 1,15 \times 1,03} - 1 \\
\bar{R}_{Gi} &= \sqrt[5]{1,4235} - 1 = 0,0732 = 7,32\%
\end{aligned}$$

Do đó, tỷ suất sinh lợi hàng năm trung bình nhân là $7,32\%$, thấp hơn một chút so với tỷ suất sinh lợi trung bình cộng là $7,60\%$.

4. Gia đình Lohrmann muốn kiếm được mức tỷ suất sinh lợi hàng năm tối thiểu là $5\%$. Tỷ suất sinh lợi hàng năm và số tiền đầu tư được trình bày trong Bảng 13. Tỷ suất sinh lợi hàng năm có trọng số tiền tệ có lớn hơn $5\%$ hay không?

#### **Lời giải (Solution):** 

Để tính tỷ suất sinh lợi có trọng số tiền tệ, hãy lập bảng kê tỷ suất sinh lợi hàng năm và số tiền đầu tư nhằm xác định các dòng tiền, như được thể hiện trong Bảng 13:

$$CF_0 = -30,00, \quad CF_1 = -10,50, \quad CF_2 = +22,75, \quad CF_3 = -3,00, \quad CF_4 = -6,25, \quad CF_5 = +36,05$$

Chúng ta có thể sử dụng mức tỷ suất sinh lợi $5\%$ đã cho để xem liệu giá trị hiện tại của các dòng tiền ròng có dương hay không. Nếu nó dương, thì tỷ suất sinh lợi có trọng số tiền tệ lớn hơn $5\%$, bởi vì lãi suất chiết khấu $5\%$ chưa thể làm giảm giá trị hiện tại về bằng không.

![](assets/Quantitative_method.pdf-0031-13.png)

$$\frac{-30,00}{(1,05)^0} + \frac{-10,50}{(1,05)^1} + \frac{22,75}{(1,05)^2} + \frac{-3,00}{(1,05)^3} + \frac{-6,25}{(1,05)^4} + \frac{36,05}{(1,05)^5} = 1,1476$$

<!-- Formula Text: − 30.00 _ (1.05) 0  +  − 10.50 _ (1.05) 1  +  22.75 _ (1.05) 2  +  − 3.00 _ (1.05) 3  +  − 6.25 _ (1.05) 4  +  36.05 _ (1.05) 5   =  1.1476. -->

Bởi vì giá trị này là số dương, nên tỷ suất sinh lợi có trọng số tiền tệ lớn hơn $5\%$. Tỷ suất sinh lợi có trọng số tiền tệ chính xác (được tìm bằng cách cho phương trình trên bằng không) là $5,86\%$. Các phép tính này có thể được thực hiện bằng Excel thông qua hàm `=IRR(cash flows)`, cho kết quả IRR là $5,86\%$.

#### **_Tỷ suất sinh lợi có trọng số thời gian (Time-Weighted Returns)_** 

Một thước đo đầu tư không nhạy cảm với việc nộp thêm và rút bớt vốn là tỷ suất sinh lợi có trọng số thời gian. **Tỷ suất sinh lợi có trọng số thời gian (*time-weighted rate of return*)** đo lường tốc độ tăng trưởng kép của $1\text{ USD}$ được đầu tư ban đầu vào danh mục trong một giai đoạn đo lường xác định. Để đánh giá các danh mục đầu tư gồm các chứng khoán được giao dịch công khai, tỷ suất sinh lợi có trọng số thời gian là thước đo hiệu quả hoạt động được ưu tiên vì nó trung hòa (*neutralizes*) tác động của các khoản rút tiền hoặc nộp thêm tiền vào danh mục, những hoạt động vốn nhìn chung nằm ngoài tầm kiểm soát của nhà quản lý danh mục đầu tư.

<!-- PDF Page 32 -->

#### **Tính Tỷ suất sinh lợi có trọng số thời gian (Computing Time-Weighted Returns)** 

Để tính tỷ suất sinh lợi có trọng số thời gian chính xác cho một danh mục đầu tư, hãy thực hiện ba bước sau đây:

**1.** Định giá danh mục đầu tư ngay trước bất kỳ khoản nộp thêm hoặc rút bớt vốn đáng kể nào. Chia tổng giai đoạn đánh giá thành các kỳ con (*subperiods*) dựa trên ngày phát sinh các dòng tiền vào và dòng tiền ra.

**2.** Tính tỷ suất sinh lợi thời kỳ nắm giữ của danh mục đầu tư cho từng kỳ con.

**3.** Liên kết (*link*) hoặc ghép lãi (*compound*) các tỷ suất sinh lợi thời kỳ nắm giữ để thu được tỷ suất sinh lợi hàng năm cho năm đó (tỷ suất sinh lợi có trọng số thời gian của năm). Nếu khoản đầu tư kéo dài hơn một năm, hãy lấy trung bình nhân của các tỷ suất sinh lợi hàng năm để thu được tỷ suất sinh lợi có trọng số thời gian trong giai đoạn đo lường đó.

Hãy quay lại ví dụ tính tỷ suất sinh lợi có trọng số tiền tệ cho cổ phiếu trả cổ tức trong mục “Tỷ suất sinh lợi có trọng số tiền tệ đối với cổ phiếu trả cổ tức” và tính tỷ suất sinh lợi có trọng số thời gian cho danh mục của nhà đầu tư đó dựa trên thông tin trong Bảng 11. Trong ví dụ đó, chúng ta đã tính được các tỷ suất sinh lợi thời kỳ nắm giữ của danh mục đầu tư, tức Bước 2 trong quy trình tìm tỷ suất sinh lợi có trọng số thời gian. Biết rằng danh mục đầu tư kiếm được mức sinh lợi $15\%$ trong năm thứ nhất và $6,67\%$ trong năm thứ hai, tỷ suất sinh lợi có trọng số thời gian của danh mục đầu tư trong giai đoạn đánh giá hai năm là bao nhiêu?

Chúng ta tìm tỷ suất sinh lợi có trọng số thời gian này bằng cách lấy trung bình nhân của hai tỷ suất sinh lợi thời kỳ nắm giữ, tức Bước 3 trong quy trình nêu trên. Phép tính trung bình nhân phản ánh chính xác phép tính tốc độ tăng trưởng kép. Tại đây, chúng ta lấy tích của 1 cộng với tỷ suất sinh lợi thời kỳ nắm giữ của mỗi kỳ để tìm giá trị cuối kỳ (*terminal value*) tại $t = 2$ của $1\text{ USD}$ được đầu tư tại $t = 0$. Sau đó chúng ta lấy căn bậc hai của tích này và trừ đi 1 để có được tỷ suất sinh lợi trung bình nhân. Chúng ta diễn giải kết quả này là tốc độ tăng trưởng kép hàng năm của $1\text{ USD}$ được đầu tư vào danh mục tại thời điểm $t = 0$. Như vậy, chúng ta có:

![](assets/Quantitative_method.pdf-0032-10.png)

$$(1 + \text{Tỷ suất sinh lợi có trọng số thời gian})^2 = (1,15)(1,0667)$$

<!-- Formula Text: (1 + Time-weighted return) 2  =  (1.15)(1.0667) -->

![](assets/Quantitative_method.pdf-0032-11.png)

$$\text{Tỷ suất sinh lợi có trọng số thời gian} = \sqrt{(1,15)(1,0667)} - 1 = 10,76\%$$

<!-- Formula Text: Time-weighted return  =  √ ____________ (1.15)(1.0667)  − 1  =  10.76%. -->

Tỷ suất sinh lợi có trọng số thời gian của danh mục đầu tư là $10,76\%$, so với tỷ suất sinh lợi có trọng số tiền tệ là $9,39\%$ vốn đặt trọng số lớn hơn vào tỷ suất sinh lợi của năm thứ hai. Chúng ta có thể thấy lý do tại sao các nhà quản lý đầu tư nhận thấy tỷ suất sinh lợi có trọng số thời gian có ý nghĩa hơn. Nếu một khách hàng giao thêm vốn cho nhà quản lý đầu tư để đầu tư vào một thời điểm bất lợi, tỷ suất sinh lợi có trọng số tiền tệ của nhà quản lý sẽ có xu hướng bị kéo giảm xuống. Nếu một khách hàng bổ sung thêm vốn vào một thời điểm thuận lợi, tỷ suất sinh lợi có trọng số tiền tệ sẽ có xu hướng được đẩy cao lên. Tỷ suất sinh lợi có trọng số thời gian loại bỏ những hiệu ứng này.

Khi xác định các bước để tính tỷ suất sinh lợi có trọng số thời gian chính xác, chúng ta đã nói rằng danh mục đầu tư cần được định giá ngay trước bất kỳ khoản nộp thêm hoặc rút bớt vốn đáng kể nào. Với khối lượng hoạt động dòng tiền lớn trong nhiều danh mục đầu tư, công việc này có thể rất tốn kém. Chúng ta thường có thể thu được một ước tính xấp xỉ hợp lý cho tỷ suất sinh lợi có trọng số thời gian bằng cách định giá danh mục đầu tư theo các khoảng thời gian đều đặn, thường xuyên, đặc biệt nếu các khoản nộp thêm và rút bớt vốn không liên quan đến biến động thị trường.

Việc định giá càng thường xuyên thì phép tính xấp xỉ càng chính xác. Định giá hàng ngày (*daily valuation*) là điều phổ biến. Giả sử một danh mục đầu tư được định giá hàng ngày trong suốt một năm. Để tính tỷ suất sinh lợi có trọng số thời gian cho năm đó, trước tiên chúng ta tính tỷ suất sinh lợi thời kỳ nắm giữ của mỗi ngày. Chúng ta tính 365 mức tỷ suất sinh lợi hàng ngày như vậy, ký hiệu là $R_1, R_2, \dots, R_{365}$. Chúng ta thu được tỷ suất sinh lợi hàng năm cho năm đó bằng cách liên kết các tỷ suất sinh lợi thời kỳ nắm giữ hàng ngày theo cách sau: $(1 + R_1) \times (1 + R_2) \times \dots \times (1 + R_{365}) - 1$. Nếu các khoản rút bớt và nộp thêm vào danh mục đầu tư chỉ diễn ra vào cuối ngày, thì tỷ suất sinh lợi hàng năm này là tỷ suất sinh lợi có trọng số thời gian chính xác cho năm đó. Ngược lại, đó là tỷ suất sinh lợi có trọng số thời gian xấp xỉ cho năm đó.

<!-- PDF Page 33 -->

Nếu có dữ liệu của nhiều năm, chúng ta có thể tính tỷ suất sinh lợi có trọng số thời gian cho từng năm riêng lẻ như trên. Nếu $R_i$ là tỷ suất sinh lợi có trọng số thời gian của năm $i$, chúng ta tính tỷ suất sinh lợi có trọng số thời gian quy đổi theo năm (*annualized time-weighted return*) bằng trung bình nhân của $N$ mức tỷ suất sinh lợi hàng năm, như sau:

![](assets/Quantitative_method.pdf-0033-04.png)

$$R_{TW} = [(1 + R_1) \times (1 + R_2) \times \dots \times (1 + R_N)]^{1/N} - 1 \tag{6}$$

<!-- Formula Text: R TW  =  [(1 + R 1) × (1 + R 2) × … × (1 + R N)] 1/N − 1. (6) -->

Ví dụ 9 minh họa phép tính tỷ suất sinh lợi có trọng số thời gian.

#### **VÍ DỤ 9 (EXAMPLE 9)** 

### **Tỷ suất sinh lợi có trọng số thời gian (Time-Weighted Rate of Return)** 

Tập đoàn Strubeck (*Strubeck Corporation*) tài trợ một quỹ hưu trí cho nhân viên của mình. Công ty tự quản lý nội bộ (*in-house*) một phần danh mục cổ phiếu và ủy thác việc quản lý phần còn lại cho Công ty Tín thác Super (*Super Trust Company*). Với tư cách là giám đốc đầu tư (*chief investment officer – CIO*) của Strubeck, bạn muốn rà soát hiệu quả hoạt động của danh mục nội bộ và danh mục Super Trust trong bốn quý vừa qua. Bạn đã sắp xếp để các dòng tiền ra và dòng tiền vào của các danh mục được thực hiện ngay vào thời điểm bắt đầu của mỗi quý. Bảng 14 (*Exhibit 14*) tóm tắt các dòng tiền vào và dòng tiền ra cũng như mức định giá của hai danh mục đầu tư. Trong Bảng 14 (bản gốc ghi nhầm là Exhibit 11), giá trị cuối kỳ là giá trị của danh mục đầu tư ngay trước khi có dòng tiền vào hoặc dòng tiền ra vào đầu quý tiếp theo. Số tiền đầu tư là số tiền mà mỗi nhà quản lý danh mục chịu trách nhiệm đầu tư.

**Bảng 14: Dòng tiền của Tài khoản Nội bộ Strubeck và Tài khoản Super Trust (đô la Mỹ) (Exhibit 14: Cash Flows for the In-House Strubeck Account and the Super Trust Account (US dollars))** 

||**Quý 1 (Quarter 1)**|**Quý 2 (Quarter 2)**|**Quý 3 (Quarter 3)**|**Quý 4 (Quarter 4)**|
|---|---|---|---|---|
|**Bảng A: Tài khoản Nội bộ (Panel A: In-House Account)**|||||
|Giá trị đầu kỳ (*Beginning value*)|4.000.000|6.000.000|5.775.000|6.720.000|
|Dòng tiền vào (dòng tiền ra) đầu kỳ (*Beginning of period inflow (outflow)*)|1.000.000|(500.000)|225.000|(600.000)|
|Số tiền đầu tư (*Amount invested*)|5.000.000|5.500.000|6.000.000|6.120.000|
|Giá trị cuối kỳ (*Ending value*)|6.000.000|5.775.000|6.720.000|5.508.000|
|**Bảng B: Tài khoản Super Trust (Panel B: Super Trust Account)**|||||
|Giá trị đầu kỳ (*Beginning value*)|10.000.000|13.200.000|12.240.000|5.659.200|
|Dòng tiền vào (dòng tiền ra) đầu kỳ (*Beginning of period inflow (outflow)*)|2.000.000|(1.200.000)|(7.000.000)|(400.000)|
|Số tiền đầu tư (*Amount invested*)|12.000.000|12.000.000|5.240.000|5.259.200|
|Giá trị cuối kỳ (*Ending value*)|13.200.000|12.240.000|5.659.200|5.469.568|

1. Tính tỷ suất sinh lợi có trọng số thời gian cho tài khoản nội bộ.

#### **Lời giải (Solution):** 

Để tính tỷ suất sinh lợi có trọng số thời gian cho tài khoản nội bộ, chúng ta tính tỷ suất sinh lợi thời kỳ nắm giữ hàng quý cho tài khoản đó và liên kết chúng lại thành tỷ suất sinh lợi hàng năm. Tỷ suất sinh lợi có trọng số thời gian của tài khoản nội bộ là $27,01\%$, được tính như sau:

<!-- PDF Page 34 -->

$$\begin{aligned}
\text{HPR Quý 1: } r_1 &= (\text{6.000.000 USD} - \text{5.000.000 USD}) / \text{5.000.000 USD} = 0,20 \\
\text{HPR Quý 2: } r_2 &= (\text{5.775.000 USD} - \text{5.500.000 USD}) / \text{5.500.000 USD} = 0,05 \\
\text{HPR Quý 3: } r_3 &= (\text{6.720.000 USD} - \text{6.000.000 USD}) / \text{6.000.000 USD} = 0,12 \\
\text{HPR Quý 4: } r_4 &= (\text{5.508.000 USD} - \text{6.120.000 USD}) / \text{6.120.000 USD} = -0,10
\end{aligned}$$

$$R_{TW} = (1 + r_1)(1 + r_2)(1 + r_3)(1 + r_4) - 1$$

$$R_{TW} = (1,20)(1,05)(1,12)(0,90) - 1 = 0,2701 \text{ hay } 27,01\%$$

2. Tính tỷ suất sinh lợi có trọng số thời gian cho tài khoản Super Trust.

#### **Lời giải (Solution):** 

Tài khoản do Super Trust quản lý có tỷ suất sinh lợi có trọng số thời gian là $26,02\%$, được tính như sau:

$$\begin{aligned}
\text{HPR Quý 1: } r_1 &= (\text{13.200.000 USD} - \text{12.000.000 USD}) / \text{12.000.000 USD} = 0,10 \\
\text{HPR Quý 2: } r_2 &= (\text{12.240.000 USD} - \text{12.000.000 USD}) / \text{12.000.000 USD} = 0,02 \\
\text{HPR Quý 3: } r_3 &= (\text{5.659.200 USD} - \text{5.240.000 USD}) / \text{5.240.000 USD} = 0,08 \\
\text{HPR Quý 4: } r_4 &= (\text{5.469.568 USD} - \text{5.259.200 USD}) / \text{5.259.200 USD} = 0,04
\end{aligned}$$

$$R_{TW} = (1 + r_1)(1 + r_2)(1 + r_3)(1 + r_4) - 1$$

$$R_{TW} = (1,10)(1,02)(1,08)(1,04) - 1 = 0,2602 \text{ hay } 26,02\%$$

Tỷ suất sinh lợi có trọng số thời gian của danh mục nội bộ cao hơn danh mục Super Trust là 99 điểm cơ bản (*basis points – bps*). Lưu ý rằng $27,01\%$ và $26,02\%$ có thể được làm tròn thành $27\%$ và $26\%$ tương ứng. Tác động của việc làm tròn chênh lệch hiệu quả hoạt động (100 bps so với 99 bps) có vẻ không đáng kể, nhưng tác động của nó trên một danh mục đầu tư quy mô lớn có thể rất đáng kể.

Sau khi hoàn thành bài tập này, chúng ta đã sẵn sàng xem xét một tình huống chi tiết hơn.

#### **VÍ DỤ 10 (EXAMPLE 10)** 

### **So sánh song song Tỷ suất sinh lợi có trọng số thời gian và Tỷ suất sinh lợi có trọng số tiền tệ (Time-Weighted and Money-Weighted Rates of Return Side by Side)** 

Nhiệm vụ của bạn là tính toán hiệu quả đầu tư của Quỹ Walbright (*Walbright Fund*) cho năm gần nhất. Các dữ kiện thực tế như sau:

- Vào ngày 1 tháng 1, Quỹ Walbright có giá trị thị trường là $100\text{ triệu USD}$.

- Trong giai đoạn từ ngày 1 tháng 1 đến ngày 30 tháng 4, các cổ phiếu trong quỹ đã tạo ra khoản lãi vốn (*capital gain*) là $10\text{ triệu USD}$.

- Vào ngày 1 tháng 5, các cổ phiếu trong quỹ đã trả tổng cộng $2\text{ triệu USD}$ tiền cổ tức. Toàn bộ cổ tức đã được tái đầu tư vào việc mua thêm cổ phiếu.

- Bởi vì hiệu quả hoạt động của quỹ rất xuất sắc, các tổ chức đã đầu tư thêm $20\text{ triệu USD}$ vào Walbright vào ngày 1 tháng 5, nâng tổng tài sản thuộc quyền quản lý (*assets under management – AUM*) lên mức $132\text{ triệu USD}$ ($\text{100 USD} + \text{10 USD} + \text{2 USD} + \text{20 USD}$).

- Vào ngày 31 tháng 12, Walbright nhận được tổng cổ tức là $2,64\text{ triệu USD}$. Giá trị thị trường của quỹ vào ngày 31 tháng 12, chưa tính $2,64\text{ triệu USD}$ tiền cổ tức, là $140\text{ triệu USD}$.

- Quỹ không thực hiện bất kỳ khoản thanh toán tiền mặt giữa kỳ (*interim cash payments*) nào khác trong năm.

<!-- PDF Page 35 -->

1. Tính tỷ suất sinh lợi có trọng số thời gian của Quỹ Walbright.

#### **Lời giải (Solution):** 

Bởi vì có các dòng tiền giữa kỳ phát sinh vào ngày 1 tháng 5, chúng ta phải tính hai mức tổng tỷ suất sinh lợi giữa kỳ và sau đó liên kết chúng lại để thu được tỷ suất sinh lợi hàng năm. Bảng 15 (*Exhibit 15*) liệt kê các giá trị thị trường có liên quan vào ngày 1 tháng 1, ngày 1 tháng 5 và ngày 31 tháng 12, cũng như tỷ suất sinh lợi thời kỳ nắm giữ giữa kỳ tương ứng của giai đoạn bốn tháng (1 tháng 1 đến 1 tháng 5) và giai đoạn tám tháng (1 tháng 5 đến 31 tháng 12).

#### **Bảng 15: Dòng tiền của Quỹ Walbright (Exhibit 15: Cash Flows for the Walbright Fund)** 

- **Ngày 1 tháng 1:**
  - Giá trị danh mục đầu kỳ $= 100\text{ triệu USD}$
- **Ngày 1 tháng 5:**
  - Cổ tức nhận được trước khi có khoản đầu tư bổ sung $= 2\text{ triệu USD}$
  - Giá trị danh mục cuối kỳ $= 110\text{ triệu USD}$
  - Tỷ suất sinh lợi thời kỳ nắm giữ bốn tháng:
    $$R = \frac{\text{2 USD} + \text{10 USD}}{\text{100 USD}} = 12\%$$
  - Khoản đầu tư mới $= 20\text{ triệu USD}$
  - Giá trị thị trường đầu kỳ cho hai phần ba năm cuối $= 132\text{ triệu USD}$
- **Ngày 31 tháng 12:**
  - Cổ tức nhận được $= 2,64\text{ triệu USD}$
  - Giá trị danh mục cuối kỳ $= 140\text{ triệu USD}$
  - Tỷ suất sinh lợi thời kỳ nắm giữ tám tháng:
    $$R = \frac{\text{2,64 USD} + \text{140 USD} - \text{132 USD}}{\text{132 USD}} = 8,06\%$$

Bây giờ chúng ta phải liên kết theo cấp số nhân (*geometrically link*) các tỷ suất sinh lợi thời kỳ nắm giữ bốn tháng và tám tháng để tính tỷ suất sinh lợi hàng năm. Chúng ta tính tỷ suất sinh lợi có trọng số thời gian như sau:

$$R_{TW} = 1,12 \times 1,0806 - 1 = 0,2103$$

Trong trường hợp này, chúng ta tính được tỷ suất sinh lợi có trọng số thời gian là $21,03\%$ cho một năm. Khoảng thời gian bốn tháng và tám tháng cộng lại đúng bằng một năm. (Lưu ý: Việc lấy căn bậc hai của tích $1,12 \times 1,0806$ sẽ chỉ phù hợp nếu mỗi con số $1,12$ và $1,0806$ áp dụng cho một năm trọn vẹn.)

2. Tính tỷ suất sinh lợi có trọng số tiền tệ của Quỹ Walbright.

   - **Lời giải (Solution):** 

Để tính tỷ suất sinh lợi có trọng số tiền tệ, chúng ta cần tìm lãi suất chiết khấu làm cho tổng giá trị hiện tại của các dòng tiền vào và dòng tiền ra bằng không. Giá trị thị trường ban đầu của quỹ và tất cả các khoản bổ sung thêm vào quỹ được xem là dòng tiền ra. (Hãy nghĩ về chúng như những khoản chi tiêu.) Các khoản rút vốn, khoản thu nhận về, và giá trị thị trường cuối kỳ của quỹ được tính là dòng tiền vào. (Giá trị thị trường cuối kỳ là số tiền mà các nhà đầu tư nhận được khi thanh lý quỹ.) Bởi vì các dòng tiền giữa kỳ đã phát sinh theo các khoảng thời gian bốn tháng, chúng ta phải giải tìm tỷ suất hoàn vốn nội bộ bốn tháng (*four-month internal rate of return*). Bảng 15 nêu chi tiết các dòng tiền và thời điểm phát sinh của chúng.

$$\begin{aligned}
CF_0 &= -100 \\
CF_1 &= -20 \\
CF_2 &= 0
\end{aligned}$$

<!-- PDF Page 36 -->

$$CF_3 = 142,64$$

$CF_0$ chỉ khoản đầu tư ban đầu trị giá $100\text{ triệu USD}$ được thực hiện vào đầu khoảng thời gian bốn tháng thứ nhất vào ngày 1 tháng 1. $CF_1$ chỉ các dòng tiền phát sinh vào cuối khoảng thời gian bốn tháng thứ nhất hay đầu khoảng thời gian bốn tháng thứ hai vào ngày 1 tháng 5. Các dòng tiền đó bao gồm một dòng tiền vào trị giá $2\text{ triệu USD}$ cho khoản cổ tức nhận được và các dòng tiền ra trị giá $22\text{ triệu USD}$ cho khoản cổ tức tái đầu tư và khoản đầu tư bổ sung tương ứng (tức dòng tiền ròng là $+2 - 22 = -20\text{ triệu USD}$). Khoảng thời gian bốn tháng thứ hai không có dòng tiền nào nên $CF_2$ bằng không. $CF_3$ chỉ các dòng tiền vào tại thời điểm cuối của khoảng thời gian bốn tháng thứ ba. Các dòng tiền vào đó bao gồm khoản cổ tức nhận được là $2,64\text{ triệu USD}$ và giá trị thị trường cuối kỳ của quỹ là $140\text{ triệu USD}$.

Sử dụng bảng tính hoặc máy tính tài chính có chức năng IRR, chúng ta nhập $-100$, $-20$, $0$, và $142,64\text{ USD}$ cho các dòng tiền ròng tại $t = 0$, $t = 1$, $t = 2$, và $t = 3$ tương ứng. Sử dụng một trong hai công cụ, chúng ta thu được IRR bốn tháng là $6,28\%$.

![](assets/Quantitative_method.pdf-0036-07.png)

$$\begin{aligned}
\frac{CF_0}{(1 + \text{IRR})^0} + \frac{CF_1}{(1 + \text{IRR})^1} + \frac{CF_2}{(1 + \text{IRR})^2} + \frac{CF_3}{(1 + \text{IRR})^3} &= 0 \\
\frac{-100}{1} + \frac{-20}{(1 + \text{IRR})^1} + \frac{0}{(1 + \text{IRR})^2} + \frac{142,64}{(1 + \text{IRR})^3} &= 0 \\
\text{IRR} &= 6,28\%
\end{aligned}$$

<!-- Formula Text: CF 0 _ (1 + IRR) 0  + CF 1 _ (1 + IRR) 1  + CF 2 _ (1 + IRR) 2  + CF 3 _ (1 + IRR) 3   =  0 − 100 _ 1   + − 20 _ (1 + IRR) 1  + 0 _ (1 + IRR) 2  +   142.64 _ (1 + IRR) 3   =  0 IRR  =  6.28% . -->

Cách nhanh chóng để quy đổi tỷ suất sinh lợi bốn tháng này theo năm (*annualize*) là nhân nó với 3. Một cách chính xác hơn là tính nó trên cơ sở ghép lãi như sau: $(1,0628)^3 - 1 = 0,2005$ hay $20,05\%$.

Các phép tính này cũng có thể được thực hiện bằng Excel thông qua hàm `=IRR(cash flows)`, cho kết quả IRR bốn tháng là $6,28\%$.

3. Diễn giải sự khác biệt giữa tỷ suất sinh lợi có trọng số thời gian và tỷ suất sinh lợi có trọng số tiền tệ của Quỹ.

#### **Lời giải (Solution):** 

Trong ví dụ này, tỷ suất sinh lợi có trọng số thời gian ($21,03\%$) lớn hơn tỷ suất sinh lợi có trọng số tiền tệ ($20,05\%$). Hiệu quả hoạt động của Quỹ Walbright tương đối kém hơn trong giai đoạn tám tháng, thời điểm mà quỹ có nhiều tiền được đầu tư hơn, so với hiệu quả hoạt động tổng thể. Thực tế này được phản ánh qua mức tỷ suất sinh lợi có trọng số tiền tệ thấp hơn so với tỷ suất sinh lợi có trọng số thời gian, bởi vì tỷ suất sinh lợi có trọng số tiền tệ nhạy cảm với thời điểm và quy mô của các khoản rút bớt và nộp thêm vốn vào danh mục đầu tư.

Việc đo lường chính xác tỷ suất sinh lợi danh mục đầu tư có ý nghĩa quan trọng đối với quá trình đánh giá các nhà quản lý danh mục đầu tư. Tuy nhiên, bên cạnh việc xem xét tỷ suất sinh lợi, các nhà phân tích cũng phải cân nhắc đến rủi ro. Khi giải quyết Ví dụ 9, chúng ta đã dừng lại trước khi đưa ra kết luận rằng bộ phận quản lý nội bộ vượt trội hơn Super Trust chỉ vì họ kiếm được tỷ suất sinh lợi có trọng số thời gian cao hơn. Một nhận định đánh giá xem hiệu quả hoạt động là “tốt hơn” hay “kém hơn” phải bao gồm cả chiều hướng rủi ro, nội dung sẽ được đề cập ở phần sau trong tài liệu học tập của bạn.

# **<mark>5</mark>** 

## **TỶ SUẤT SINH LỢI QUY ĐỔI THEO NĂM (ANNUALIZED RETURN)** 

tính toán và diễn giải các thước đo tỷ suất sinh lợi quy đổi theo năm (*annualized return measures*) và tỷ suất sinh lợi ghép lãi liên tục (*continuously compounded returns*), cũng như mô tả các trường hợp sử dụng phù hợp của chúng

<!-- PDF Page 37 -->

Khoảng thời gian mà một tỷ suất sinh lợi được tạo ra hoặc được tính toán có thể khác nhau, và thường thì chúng ta phải quy đổi theo năm (*annualize*) một mức tỷ suất sinh lợi vốn được tính cho một khoảng thời gian ngắn hơn (hoặc dài hơn) một năm. Bạn có thể mua một tín phiếu Kho bạc ngắn hạn có kỳ hạn ba tháng, hoặc bạn có thể nắm giữ một vị thế trong hợp đồng tương lai sẽ đáo hạn vào cuối quý tới. Làm thế nào chúng ta có thể so sánh các mức tỷ suất sinh lợi này?

Trong nhiều trường hợp, thuận tiện nhất là quy đổi tất cả các tỷ suất sinh lợi hiện có sang cơ sở hàng năm để tạo điều kiện so sánh. Do đó, các tỷ suất sinh lợi hàng ngày, hàng tuần, hàng tháng và hàng quý được chuyển đổi thành tỷ suất sinh lợi quy đổi theo năm (*annualized returns*). Nhiều công thức được sử dụng để tính toán một số giá trị hoặc mức giá nhất định cũng đòi hỏi tất cả các tỷ suất sinh lợi và kỳ hạn phải được biểu thị dưới dạng tỷ suất sinh lợi quy đổi theo năm. Ví dụ, phiên bản phổ biến nhất của mô hình định giá quyền chọn Black–Scholes (*Black–Scholes option-pricing model*) đòi hỏi tỷ suất sinh lợi phải được quy đổi theo năm và thời gian phải được tính bằng đơn vị năm.

### **Ghép lãi không theo năm (Non-annual Compounding)** 

Hãy nhớ lại rằng tiền lãi có thể được thanh toán nửa năm một lần (*semiannually*), hàng quý (*quarterly*), hàng tháng (*monthly*), hoặc thậm chí hàng ngày (*daily*). Để xử lý các khoản thanh toán tiền lãi được thực hiện nhiều hơn một lần trong năm, chúng ta có thể điều chỉnh công thức giá trị hiện tại như sau. Tại đây, $R_s$ là lãi suất niêm yết (*quoted interest rate*) và bằng lãi suất định kỳ (*periodic interest rate*) nhân với số kỳ ghép lãi trong mỗi năm. Tổng quát, khi có nhiều hơn một kỳ ghép lãi trong một năm, chúng ta có thể biểu diễn công thức tính giá trị hiện tại như sau:

![](assets/Quantitative_method.pdf-0037-07.png)

$$\text{PV} = \text{FV}_N \left(1 + \frac{R_s}{m}\right)^{-mN} \tag{7}$$

<!-- Formula Text: PV  =  FV N (1 + R s _ m ) −mN , (7) -->

trong đó:

- $m =$ số kỳ ghép lãi mỗi năm (*number of compounding periods per year*),

- $R_s =$ lãi suất niêm yết hàng năm (*quoted annual interest rate*), và

- $N =$ số năm (*number of years*).

Công thức trong Phương trình 7 khá giống với công thức giá trị hiện tại đơn giản. Như chúng ta đã lưu ý, thừa số giá trị hiện tại (*present value factor*) và thừa số giá trị tương lai (*future value factor*) là hai số nghịch đảo của nhau. Việc thay đổi tần suất ghép lãi không làm thay đổi kết quả này. Sự khác biệt duy nhất là việc sử dụng lãi suất định kỳ và số kỳ ghép lãi tương ứng. Ví dụ sau đây trình bày một ứng dụng của ghép lãi hàng tháng.

#### **VÍ DỤ 11 (EXAMPLE 11)** 

### **Giá trị hiện tại của một Khoản tiền trả một lần với Ghép lãi hàng tháng (The Present Value of a Lump Sum with Monthly Compounding)** 

Nhà quản lý của một quỹ hưu trí Canada biết rằng quỹ phải thực hiện một khoản thanh toán trả một lần (*lump-sum payment*) trị giá $5\text{ triệu CAD}$ vào thời điểm 10 năm kể từ ngày hôm nay. Cô ấy muốn đầu tư một số tiền ngay hôm nay vào một hợp đồng đầu tư đảm bảo (*guaranteed investment contract – GIC*) để số tiền đó tăng trưởng thành số tiền yêu cầu. Lãi suất hiện hành của các hợp đồng GIC là $6\%$ một năm, ghép lãi hàng tháng (*compounded monthly*).

1. Hôm nay cô ấy nên đầu tư bao nhiêu vào hợp đồng GIC?

**Lời giải (Solution):** 

Bằng cách áp dụng Phương trình 7, giá trị hiện tại yêu cầu được tính như sau:

<!-- PDF Page 38 -->

$$\begin{aligned}
\text{FV}_N &= \text{5.000.000 CAD} \\
R_s &= 6\% = 0,06 \\
m &= 12 \\
R_s / m &= 0,06 / 12 = 0,005 \\
N &= 10 \\
mN &= 12(10) = 120 \\
\text{PV} &= \text{FV}_N \left(1 + \frac{R_s}{m}\right)^{-mN} \\
&= \text{5.000.000 CAD}(1,005)^{-120} \\
&= \text{5.000.000 CAD}(0,549633) = \text{2.748.163,67 CAD}
\end{aligned}$$

Khi áp dụng Phương trình 7, chúng ta sử dụng lãi suất định kỳ (trong trường hợp này là lãi suất hàng tháng) và số kỳ phù hợp với việc ghép lãi hàng tháng (trong trường hợp này là 10 năm ghép lãi hàng tháng, hay 120 tháng).

### **Quy đổi Tỷ suất sinh lợi theo năm (Annualizing Returns)** 

Để quy đổi bất kỳ tỷ suất sinh lợi nào của một giai đoạn ngắn hơn một năm sang cơ sở hàng năm, tỷ suất sinh lợi của giai đoạn đó phải được ghép lãi theo số kỳ trong một năm. Tỷ suất sinh lợi hàng tháng được ghép lãi 12 lần, tỷ suất sinh lợi hàng tuần được ghép lãi 52 lần, và tỷ suất sinh lợi hàng quý được ghép lãi 4 lần. Tỷ suất sinh lợi hàng ngày thông thường được ghép lãi 365 lần. Đối với một số lượng ngày không phổ biến, chúng ta ghép lãi theo tỷ số giữa 365 chia cho số ngày đó.

Nếu tỷ suất sinh lợi hàng tuần là $0,2\%$, thì tỷ suất sinh lợi kép hàng năm là $10,95\%$ (có 52 tuần trong một năm):

![](assets/Quantitative_method.pdf-0038-09.png)

$$R_{\text{annual}} = (1 + R_{\text{weekly}})^{52} - 1 = (1 + 0,2\%)^{52} - 1 = (1,002)^{52} - 1 = 0,1095 = 10,95\%$$

<!-- Formula Text: R annual  =  (1 + R weekly) 52 − 1  =  (1 + 0.2%) 52 − 1 = (1.002) 52 − 1  =  0.1095  =  10.95% . -->

Nếu tỷ suất sinh lợi trong 15 ngày là $0,4\%$, thì tỷ suất sinh lợi quy đổi theo năm là $10,20\%$, giả định có 365 ngày trong một năm:

![](assets/Quantitative_method.pdf-0038-11.png)

$$R_{\text{annual}} = (1 + R_{15})^{365/15} - 1 = (1 + 0,4\%)^{365/15} - 1 = (1,004)^{365/15} - 1 = 0,1020 = 10,20\%$$

<!-- Formula Text: R annual  =  (1 + R 15) 365/15 − 1  =  (1 + 0.4%) 365/15 − 1 = (1.004) 365/15 − 1  =  0.1020  =  10.20% . -->

Phương trình tổng quát để quy đổi tỷ suất sinh lợi theo năm được cho dưới đây, trong đó $c$ là số kỳ trong một năm. Đối với một quý, $c = 4$ và đối với một tháng, $c = 12$:

![](assets/Quantitative_method.pdf-0038-13.png)

$$R_{\text{annual}} = (1 + R_{\text{period}})^c - 1 \tag{8}$$

<!-- Formula Text: R annual  =    (1  + R period) c − 1. (8) -->

Làm thế nào chúng ta có thể quy đổi một tỷ suất sinh lợi theo năm khi tỷ suất sinh lợi thời kỳ nắm giữ dài hơn một năm? Ví dụ, làm thế nào chúng ta quy đổi tỷ suất sinh lợi thời kỳ nắm giữ 18 tháng sang cơ sở hàng năm? Bởi vì một năm chứa hai phần ba của giai đoạn 18 tháng, nên $c = 2/3$ trong phương trình trên. Ví dụ, mức tỷ suất sinh lợi 18 tháng là $20\%$ có thể được quy đổi theo năm như sau:

![](assets/Quantitative_method.pdf-0038-15.png)

$$R_{\text{annual}} = (1 + R_{\text{18month}})^{2/3} - 1 = (1 + 0,20)^{2/3} - 1 = 0,1292 = 12,92\%$$

<!-- Formula Text: R annual  =  (1 + R 18month) 2/3 − 1  =  (1 + 0.20) 2/3 − 1  =  0.1292  =  12.92%. -->

Các biểu thức tương tự có thể được xây dựng khi cần sử dụng tỷ suất sinh lợi hàng quý hoặc hàng tuần để so sánh thay vì tỷ suất sinh lợi hàng năm. Trong những trường hợp như vậy, $c$ bằng số thời kỳ nắm giữ trong một quý hoặc trong một tuần. Ví dụ, giả sử bạn muốn chuyển đổi tỷ suất sinh lợi hàng ngày sang tỷ suất sinh lợi hàng tuần hoặc từ tỷ suất sinh lợi hàng năm sang tỷ suất sinh lợi hàng tuần để so sánh giữa các tỷ suất sinh lợi hàng tuần với nhau. Để chuyển đổi tỷ suất sinh lợi hàng ngày sang tỷ suất sinh lợi hàng tuần, $c = 5$, giả định rằng có năm ngày giao dịch (*trading days*) trong một tuần. Tuy nhiên, các phép tính tỷ suất sinh lợi hàng ngày có thể được quy đổi theo năm theo cách khác nhau. Ví dụ, có thể dùng 5 ngày mỗi tuần cho các phép tính dựa trên ngày giao dịch, tương ứng khoảng 250 ngày giao dịch một năm; hoặc có thể dùng 7 ngày mỗi tuần cho các phép tính dựa trên ngày lịch (*calendar-day-based calculations*). Các phương pháp cụ thể được sử dụng sẽ tuân theo các thông lệ kinh doanh, quy ước thị trường

<!-- PDF Page 39 -->

và các chuẩn mực cụ thể. Để chuyển đổi tỷ suất sinh lợi hàng năm sang tỷ suất sinh lợi hàng tuần, $c = 1/52$. Các biểu thức cho tỷ suất sinh lợi hàng năm khi đó có thể được viết lại thành các biểu thức cho tỷ suất sinh lợi hàng tuần như sau:

![](assets/Quantitative_method.pdf-0039-04.png)

$$R_{\text{weekly}} = (1 + R_{\text{daily}})^5 - 1; \quad R_{\text{weekly}} = (1 + R_{\text{annual}})^{1/52} - 1 \tag{9}$$

<!-- Formula Text: R weekly  =  (1 + R daily) 5 − 1;  R weekly  =  (1 + R annual) 1/52 − 1. (9) -->

Một hạn chế lớn của việc quy đổi tỷ suất sinh lợi theo năm là giả định ngầm định (*implicit assumption*) rằng các tỷ suất sinh lợi có thể được lặp lại một cách chính xác, nghĩa là tiền có thể được tái đầu tư lặp đi lặp lại trong khi vẫn kiếm được một mức tỷ suất sinh lợi tương tự. Loại tỷ suất sinh lợi này không phải lúc nào cũng khả thi. Một nhà đầu tư có thể kiếm được mức tỷ suất sinh lợi $5\%$ trong một tuần bởi vì thị trường tăng mạnh vào tuần đó, nhưng rất khó có khả năng ông ấy sẽ kiếm được mức tỷ suất sinh lợi $5\%$ mỗi tuần trong suốt 51 tuần tiếp theo để tạo ra mức tỷ suất sinh lợi quy đổi theo năm lên tới $1.164,3\%$ ($= 1,05^{52} - 1$). Do đó, điều quan trọng là khi quy đổi các tỷ suất sinh lợi ngắn hạn theo năm, cần phải luôn ghi nhớ hạn chế này.

#### **VÍ DỤ 12 (EXAMPLE 12)** 

### **Tỷ suất sinh lợi quy đổi theo năm (Annualized Returns)** 

Một nhà phân tích muốn đánh giá ba chứng khoán mà cô đã nắm giữ trong danh mục đầu tư của mình trong các khoảng thời gian khác nhau.

   - Trong 100 ngày qua, Chứng khoán A đã kiếm được mức tỷ suất sinh lợi là $6,2\%$.

   - Chứng khoán B đã kiếm được $2\%$ trong bốn tuần qua.

   - Chứng khoán C đã kiếm được mức tỷ suất sinh lợi là $5\%$ trong ba tháng qua.

1. So sánh hiệu quả hoạt động tương đối của ba chứng khoán này.

#### **Lời giải (Solution):** 

Để thuận tiện cho việc so sánh, tỷ suất sinh lợi của ba chứng khoán cần được quy đổi theo năm:

- Tỷ suất sinh lợi quy đổi theo năm của Chứng khoán A: $R_{SA} = (1 + 0,062)^{365/100} - 1 = 0,2455 = 24,55\%$

- Tỷ suất sinh lợi quy đổi theo năm của Chứng khoán B: $R_{SB} = (1 + 0,02)^{52/4} - 1 = 0,2936 = 29,36\%$

- Tỷ suất sinh lợi quy đổi theo năm của Chứng khoán C: $R_{SC} = (1 + 0,05)^4 - 1 = 0,2155 = 21,55\%$

Chứng khoán B đã tạo ra mức tỷ suất sinh lợi quy đổi theo năm cao nhất.

#### **VÍ DỤ 13 (EXAMPLE 13)** 

### **Hiệu quả hoạt động của Quỹ hoán đổi danh mục (Exchange-Traded Fund Performance)** 

Một nhà đầu tư đang đánh giá tỷ suất sinh lợi của ba quỹ hoán đổi danh mục (*exchange-traded funds – ETFs*) mới được thành lập gần đây. Thông tin chọn lọc về tỷ suất sinh lợi của các quỹ ETF được trình bày trong Bảng 16 (*Exhibit 16*).

<!-- PDF Page 40 -->

#### **Bảng 16: Thông tin Hiệu quả hoạt động của các Quỹ ETF (Exhibit 16: ETF Performance Information)** 

|**ETF**|**Thời gian kể từ khi thành lập (Time Since Inception)**|**Tỷ suất sinh lợi kể từ khi thành lập (Return Since Inception) (%)**|
|---|---|---|
|1|146 ngày|4,61|
|2|5 tuần|1,10|
|3|15 tháng|14,35|

1. Quỹ ETF nào có tỷ suất sinh lợi quy đổi theo năm cao nhất?

   - **A.** ETF 1
   - **B.** ETF 2
   - **C.** ETF 3

   - **Lời giải (Solution):** 

- B là đáp án đúng. Tỷ suất sinh lợi quy đổi theo năm của ba quỹ ETF như sau:
  - Tỷ suất sinh lợi quy đổi theo năm của ETF 1 $= (1,0461^{365/146}) - 1 = 11,93\%$
  - Tỷ suất sinh lợi quy đổi theo năm của ETF 2 $= (1,0110^{52/5}) - 1 = 12,05\%$
  - Tỷ suất sinh lợi quy đổi theo năm của ETF 3 $= (1,1435^{12/15}) - 1 = 11,32\%$

Mặc dù có giá trị tỷ suất sinh lợi định kỳ thấp nhất, ETF 2 lại có tỷ suất sinh lợi quy đổi theo năm cao nhất do giả định lãi suất tái đầu tư và việc ghép lãi của mức sinh lợi định kỳ.

### **Tỷ suất sinh lợi ghép lãi liên tục (Continuously Compounded Returns)** 

Một khái niệm quan trọng là tỷ suất sinh lợi ghép lãi liên tục gắn với một tỷ suất sinh lợi thời kỳ nắm giữ, chẳng hạn như $R_1$. **Tỷ suất sinh lợi ghép lãi liên tục (*continuously compounded return*)** gắn với một tỷ suất sinh lợi thời kỳ nắm giữ là logarit tự nhiên (*natural logarithm*) của 1 cộng với tỷ suất sinh lợi thời kỳ nắm giữ đó, hoặc tương đương, là logarit tự nhiên của giá cuối kỳ chia cho giá đầu kỳ (tỷ số giá tương đối – *price relative*). Lưu ý rằng tại đây chúng ta đang sử dụng ký hiệu $r$ để chỉ riêng các tỷ suất sinh lợi ghép lãi liên tục, nhưng các giáo trình và nguồn tài liệu khác có thể sử dụng một ký hiệu khác.

Nếu chúng ta quan sát thấy tỷ suất sinh lợi thời kỳ nắm giữ một tuần là $0,04$, thì tỷ suất sinh lợi ghép lãi liên tục tương đương, được gọi là tỷ suất sinh lợi ghép lãi liên tục một tuần, là $\ln(1,04) = 0,039221$; $1,00\text{ EUR}$ được đầu tư trong một tuần ở mức lãi suất $0,039221$ ghép lãi liên tục sẽ mang lại $1,04\text{ EUR}$, tương đương với mức tỷ suất sinh lợi thời kỳ nắm giữ một tuần là $4\%$.

Tỷ suất sinh lợi ghép lãi liên tục từ thời điểm $t$ đến $t + 1$ là:

![](assets/Quantitative_method.pdf-0040-15.png)

$$r_{t,t+1} = \ln(P_{t+1} / P_t) = \ln(1 + R_{t,t+1}) \tag{10}$$

<!-- Formula Text: rt,t+1 = ln(Pt+1/Pt) = ln(1 + Rt,t+1). (10) -->

Đối với ví dụ của chúng ta, một tài sản được mua tại thời điểm $t$ với mức giá $P_0$ là $30\text{ USD}$ và cùng tài sản đó một kỳ sau, tại $t + 1$, có giá trị $P_1$ là $34,50\text{ USD}$ sẽ có tỷ suất sinh lợi ghép lãi liên tục được cho bởi $r_{0,1} = \ln(P_1 / P_0) = \ln(1 + R_{0,1}) = \ln(\text{34,50 USD} / \text{30 USD}) = \ln(1,15) = 0,139762$.

Như vậy, $13,98\%$ là tỷ suất sinh lợi ghép lãi liên tục từ $t = 0$ đến $t = 1$. Tỷ suất sinh lợi ghép lãi liên tục nhỏ hơn tỷ suất sinh lợi thời kỳ nắm giữ tương ứng. Nếu khung thời gian đầu tư của chúng ta kéo dài từ $t = 0$ đến $t = T$, thì tỷ suất sinh lợi ghép lãi liên tục đến thời điểm $T$ là:

![](assets/Quantitative_method.pdf-0040-18.png)

$$r_{0,T} = \ln(P_T / P_0) \tag{11}$$

<!-- Formula Text: r0,T = ln(PT/P0). (11) -->

Áp dụng hàm mũ (*exponential function*) cho cả hai vế của phương trình, chúng ta có $\exp(r_{0,T}) = \exp[\ln(P_T / P_0)] = P_T / P_0$, vì vậy:

![](assets/Quantitative_method.pdf-0040-20.png)

$$P_T = P_0 \exp(r_{0,T})$$

<!-- Formula Text: PT = P0exp(r0,T). -->
