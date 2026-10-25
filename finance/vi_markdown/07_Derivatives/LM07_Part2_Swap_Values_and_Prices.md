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
