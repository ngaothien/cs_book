# Tập 1: Phương pháp Định lượng (Quantitative Methods)
## Learning Module 2 Time Value of Money in Finance (Trang PDF 53–94)

---

# Tập 1: Phương pháp Định lượng (Volume 1: Quantitative Methods)
## Học phần 2: Giá trị Thời gian của Tiền trong Tài chính (Learning Module 2: Time Value of Money in Finance)
### Phần 1/4: Giới thiệu (Introduction) (Trang PDF 53–67)

---

<!-- PDF Page 53 -->

#### H Ọ C P H Ầ N (L E A R N I N G M O D U L E)

# **<mark>2</mark>** 

### **Giá trị Thời gian của Tiền trong Tài chính (Time Value of Money in Finance)** 

###### **<mark>MỤC TIÊU HỌC TẬP (LEARNING OUTCOMES)</mark>** 

- **_Mức độ thành thạo (Mastery) – Ứng viên cần có khả năng:_**
  - tính toán và diễn giải giá trị hiện tại (*present value – PV*) của các công cụ thu nhập cố định (*fixed-income instruments*) và công cụ vốn chủ sở hữu (*equity instruments*) dựa trên các dòng tiền dự kiến trong tương lai;
  - tính toán và diễn giải tỷ suất sinh lợi ngầm định (*implied return*) của các công cụ thu nhập cố định cùng với tỷ suất sinh lợi yêu cầu (*required return*) và tốc độ tăng trưởng ngầm định (*implied growth*) của các công cụ vốn chủ sở hữu khi biết trước giá trị hiện tại (PV) và các dòng tiền;
  - giải thích nguyên lý cộng dòng tiền (*cash flow additivity principle*), tầm quan trọng của nó đối với điều kiện không có kinh doanh chênh lệch giá (*no-arbitrage condition*), và ứng dụng của nó trong việc tính toán lãi suất kỳ hạn ngầm định (*implied forward interest rates*), tỷ giá hối đoái kỳ hạn (*forward exchange rates*) và giá trị quyền chọn (*option values*).

![](assets/Quantitative_method.pdf-0053-06.png)

<!-- Picture Text: 1<br> -->

##### **GIỚI THIỆU (INTRODUCTION)** 

Học phần này áp dụng các nguyên lý giá trị thời gian của tiền (*time value of money*) vào việc định giá các tài sản tài chính. Bài học đầu tiên tập trung vào việc giải tìm giá trị hiện tại của các dòng tiền dự kiến trong tương lai gắn liền với trái phiếu và cổ phiếu. Trong bài học thứ hai, trọng tâm chuyển sang việc giải tìm tỷ suất sinh lợi ngầm định của trái phiếu và cổ phiếu khi biết trước mức giá hiện hành. Nội dung này bao gồm việc giải tìm và diễn giải các tốc độ tăng trưởng ngầm định gắn liền với mức giá cổ phiếu đã cho. Bài học cuối cùng giới thiệu tính cộng dòng tiền (*cash flow additivity*), một nguyên lý quan trọng đảm bảo rằng giá của các tài sản tài chính không cho phép các nhà đầu tư kiếm được lợi nhuận phi rủi ro (*risk-free profits*), được minh họa bằng một số ví dụ cụ thể. Nội dung được đề cập trong học phần này cung cấp một nền tảng quan trọng giúp các ứng viên hiểu được cách thức định giá các tài sản tài chính trên thị trường.

###### **TỔNG QUAN HỌC PHẦN (LEARNING MODULE OVERVIEW)** 

- Giá của một trái phiếu bằng tổng giá trị hiện tại của các khoản thanh toán tiền lãi định kỳ (*coupon payments*) đã cam kết và mệnh giá (*par value*) của trái phiếu đó. Đối với trái phiếu chiết khấu (*discount bonds*), mức giá chỉ phản ánh giá trị hiện tại của mệnh giá trái phiếu.

- Giá trị của một cổ phiếu phải phản ánh tổng giá trị hiện tại của các khoản cổ tức dự kiến trong tương lai của cổ phiếu đó kéo dài đến vĩnh viễn (*in perpetuity*).

<!-- PDF Page 54 -->

- Các mô hình định giá cổ phiếu được phân loại theo mô hình tăng trưởng dự kiến được giả định cho cổ tức trong tương lai: (1) không tăng trưởng (*no growth*), (2) tăng trưởng không đổi (*constant growth*), hoặc (3) tăng trưởng cổ tức thay đổi (*changing dividend growth*).

- Nếu biết trước giá của một trái phiếu, tỷ suất sinh lợi ngầm định (*implied return*) của trái phiếu đó có thể được tính bằng cách sử dụng giá trái phiếu và các dòng tiền cam kết trong tương lai của nó.

- Tỷ suất sinh lợi yêu cầu (*required return*) của một cổ phiếu có thể được ước tính khi biết giá hiện hành của cổ phiếu cùng các giả định về cổ tức dự kiến và tốc độ tăng trưởng trong tương lai của nó.

- Tốc độ tăng trưởng cổ tức ngầm định (*implied dividend growth rate*) của một cổ phiếu có thể được ước tính khi biết giá hiện hành của cổ phiếu cùng các giả định về cổ tức dự kiến trong tương lai và tỷ suất sinh lợi yêu cầu của nó.

- Khi định giá hai (hoặc nhiều) chuỗi dòng tiền, nguyên lý cộng dòng tiền (*cash flow additivity principle*) cho phép so sánh các chuỗi dòng tiền với nhau (miễn là các dòng tiền phát sinh tại cùng một thời điểm).

- Việc áp dụng nguyên lý cộng dòng tiền cho phép xác nhận rằng giá tài sản là như nhau đối với các tài sản tương đương về mặt kinh tế (*economically equivalent assets*) (ngay cả khi các tài sản đó có các chuỗi dòng tiền khác nhau).

- Một số ứng dụng thực tế của nguyên lý cộng dòng tiền được sử dụng để minh họa cho việc định giá không có kinh doanh chênh lệch giá (*no-arbitrage pricing*).

## **<mark>2</mark>** 

##### **GIÁ TRỊ THỜI GIAN CỦA TIỀN TRONG CÔNG CỤ THU NHẬP CỐ ĐỊNH VÀ VỐN CHỦ SỞ HỮU (TIME VALUE OF MONEY IN FIXED INCOME AND EQUITY)** 

tính toán và diễn giải giá trị hiện tại (*present value – PV*) của các công cụ thu nhập cố định và công cụ vốn chủ sở hữu dựa trên các dòng tiền dự kiến trong tương lai

Thời điểm phát sinh của các dòng tiền gắn liền với các công cụ tài chính ảnh hưởng đến giá trị của chúng, trong đó các dòng tiền vào (*cash inflows*) được định giá càng cao khi chúng được nhận về càng sớm. Giá trị thời gian của tiền thể hiện sự đánh đổi giữa các dòng tiền nhận được ngày hôm nay so với những dòng tiền nhận được vào một ngày trong tương lai, cho phép so sánh giá trị hiện hành hay giá trị hiện tại của một hoặc nhiều dòng tiền với những dòng tiền nhận được tại các thời điểm khác nhau trong tương lai. Sự khác biệt này dựa trên một mức lãi suất chiết khấu (*discount rate*) phù hợp $r$ như đã trình bày trong học phần trước, vốn thay đổi tùy theo loại công cụ cũng như thời điểm và mức độ rủi ro của các dòng tiền dự kiến.

Tổng quát, mối quan hệ giữa giá trị hiện hành hay giá trị hiện tại ($\text{PV}$) và giá trị tương lai ($\text{FV}$) của một dòng tiền, trong đó $r$ là lãi suất chiết khấu công bố mỗi kỳ và $t$ là số kỳ ghép lãi, được biểu diễn như sau:

![](assets/Quantitative_method.pdf-0054-16.png)

$$\text{FV}_t = \text{PV}(1 + r)^t \tag{1}$$

<!-- Formula Text: FVt = PV(1 + r)t. (1) -->

Nếu số kỳ ghép lãi $t$ rất lớn, nghĩa là $t \to \infty$, chúng ta ghép lãi dòng tiền ban đầu trên cơ sở liên tục (*continuous basis*) như sau:

![](assets/Quantitative_method.pdf-0054-18.png)

$$\text{FV}_t = \text{PV}e^{rt} \tag{2}$$

<!-- Formula Text: FVt = PVer t. (2) -->

Ngược lại, giá trị hiện tại có thể được biểu diễn theo giá trị tương lai, đòi hỏi phải biến đổi lại Phương trình 1 như sau:

<!-- PDF Page 55 -->

![](assets/Quantitative_method.pdf-0055-03.png)

$$\begin{aligned}
\text{FV}_t &= \text{PV}(1 + r)^t \\
\text{PV} &= \text{FV}_t \left[\frac{1}{(1 + r)^t}\right] \\
\text{PV} &= \text{FV}_t (1 + r)^{-t} \tag{3}
\end{aligned}$$

<!-- Formula Text: FV t  =  PV (1 + r) t PV  =  FV t[ 1 _ (1 + r) t ] PV  =  FV t (1 + r) −t . (3) -->

Biểu thức tương đương theo thời gian liên tục (*continuous time equivalent expression*) của Phương trình 3 như sau:

$$\text{PV}_t = \text{FV}e^{-rt} \tag{4}$$

![](assets/Quantitative_method.pdf-0055-05.png)

<!-- Formula Text: (4) -->

###### **Các Công cụ Thu nhập Cố định và Giá trị Thời gian của Tiền (Fixed-Income Instruments and the Time Value of Money)** 

Các công cụ thu nhập cố định (*fixed-income instruments*) là các công cụ nợ, chẳng hạn như trái phiếu (*bond*) hoặc khoản vay (*loan*), đại diện cho các hợp đồng theo đó tổ chức phát hành vay tiền từ nhà đầu tư để đổi lấy lời hứa hoàn trả trong tương lai. Lãi suất chiết khấu đối với các công cụ thu nhập cố định là một mức lãi suất, và tỷ suất sinh lợi của một trái phiếu hoặc khoản vay thường được gọi là lợi suất đáo hạn (*yield-to-maturity – YTM*) của nó.

Các dòng tiền gắn liền với các công cụ thu nhập cố định thường tuân theo một trong ba mô hình tổng quát sau:

- **Chiết khấu (*Discount*):** Nhà đầu tư trả một mức giá ban đầu ($\text{PV}$) cho một trái phiếu hoặc khoản vay và nhận lại một dòng tiền nợ gốc duy nhất ($\text{FV}$) khi đáo hạn. Phần chênh lệch ($\text{FV} - \text{PV}$) đại diện cho tiền lãi kiếm được trong suốt vòng đời của công cụ.

- **Tiền lãi định kỳ (*Periodic Interest*):** Nhà đầu tư trả một mức giá ban đầu ($\text{PV}$) cho một trái phiếu hoặc khoản vay và nhận được các dòng tiền lãi ($\text{PMT}$) theo các khoảng thời gian đã định trước trong suốt vòng đời của công cụ, với khoản thanh toán tiền lãi cuối cùng và nợ gốc ($\text{FV}$) được chi trả khi đáo hạn.

- **Thanh toán đều (*Level Payments*):** Nhà đầu tư trả một mức giá ban đầu ($\text{PV}$) và nhận được các dòng tiền đồng nhất theo các khoảng thời gian đã định trước ($A$) cho đến khi đáo hạn, bao gồm cả tiền lãi và tiền trả nợ gốc.

###### **_Công cụ chiết khấu (Discount Instruments)_** 

Mô hình dòng tiền chiết khấu được thể hiện trong Bảng 1 (*Exhibit 1*):

###### **Bảng 1: Dòng tiền của Trái phiếu Chiết khấu (Exhibit 1: Discount Bond Cash Flows)** 

![](assets/Quantitative_method.pdf-0055-15.png)

<!-- Picture Text: FV<br>( FV–PV ) represents FV<br>interest over the<br>investment period<br>PV<br>Investor receives<br>final bond principal<br>payment at maturity<br>5.0 Years<br>Investor pays<br>discounted<br>value of bond<br>at inception<br>PV<br> -->
> **Chú thích hình ảnh:** Tại thời điểm khởi đầu, nhà đầu tư trả giá trị chiết khấu của trái phiếu ($\text{PV}$). Sau $5,0$ năm (khi đáo hạn), nhà đầu tư nhận được khoản thanh toán nợ gốc trái phiếu cuối cùng ($\text{FV}$). Chênh lệch ($\text{FV} - \text{PV}$) đại diện cho tiền lãi trong suốt giai đoạn đầu tư.

<!-- PDF Page 56 -->

Phép tính giá trị hiện tại ($\text{PV}$) cho một trái phiếu chiết khấu với nợ gốc ($\text{FV}$) được thanh toán tại thời điểm $t$ và lãi suất chiết khấu thị trường là $r$ mỗi kỳ như sau:

$$\text{PV}(\text{Trái phiếu chiết khấu}) = \text{FV}_t / (1 + r)^t \tag{5}$$

*(Tiếng Anh: $\text{PV}(\text{Discount Bond}) = \text{FV}_t / (1 + r)^t$)*

Nguồn sinh lợi duy nhất của nhà đầu tư là phần chênh lệch giữa mức giá đã trả ($\text{PV}$) và toàn bộ số nợ gốc ($\text{FV}$) nhận được khi đáo hạn. Loại trái phiếu này thường được gọi là **trái phiếu không trả lãi định kỳ (*zero-coupon bond*)** do không có các dòng tiền lãi trung gian — vốn thường được gọi là tiền lãi coupon (*coupons*) đối với trái phiếu.

###### **VÍ DỤ 1 (EXAMPLE 1)** 

###### **Trái phiếu chiết khấu dưới Môi trường Lãi suất Dương và Âm (Discount Bonds under Positive and Negative Interest Rates)** 

Mặc dù hầu hết các chính phủ phát hành trái phiếu có lãi suất coupon cố định với nợ gốc được thanh toán khi đáo hạn, nhưng đối với nhiều tổ chức phát hành chính phủ như Hoa Kỳ, Vương quốc Anh hoặc Ấn Độ, các nhà đầu tư mua và bán các dòng tiền lãi hoặc dòng tiền gốc riêng lẻ đã được tách rời (*separated* hay *stripped*) từ các công cụ này dưới dạng trái phiếu chiết khấu. Xét một dòng tiền nợ gốc duy nhất phải trả sau 20 năm của một trái phiếu chính phủ Cộng hòa Ấn Độ được phát hành khi lợi suất đáo hạn (YTM) là $6,70\%$. Vì mục đích của ví dụ đơn giản hóa này, chúng ta sử dụng ghép lãi hàng năm, nghĩa là $t$ trong Phương trình 5 bằng số năm cho đến khi dòng tiền phát sinh.

1. Nhà đầu tư kỳ vọng phải trả bao nhiêu cho trái phiếu chiết khấu này trên mỗi $100\text{ INR}$ nợ gốc?

###### **Lời giải (Solution):** 

$27,33\text{ INR}$

Chúng ta giải tìm $\text{PV}$ khi biết $r = 6,70\%$, $t = 20$, và $\text{FV}_{20} = 100\text{ INR}$ bằng cách sử dụng Phương trình 5:

$$\text{PV} = \text{100 INR} / (1 + 0,067)^{20} = \text{27,33 INR}$$

Chúng ta cũng có thể sử dụng hàm PV trong Microsoft Excel hoặc Google Sheets:

`=PV(rate, nper, pmt, FV, type)`

trong đó:

- _rate_ = lãi suất chiết khấu thị trường mỗi kỳ,

- _nper_ = số kỳ,

- _pmt_ = khoản thanh toán coupon định kỳ (bằng 0 đối với trái phiếu chiết khấu),

- _FV_ = giá trị tương lai hoặc mệnh giá (*face value*), và

- _type_ = các khoản thanh toán được thực hiện vào cuối kỳ (0 như trong trường hợp này) hoặc đầu kỳ (1) của mỗi kỳ.

Vì là một dòng tiền ra (hoặc mức giá phải trả), kết quả hàm PV của Excel mang dấu âm, vì vậy:

$$\text{PV} = (27,33) = \text{PV}(0.067, 20, 0, 100, 0)$$

Trong khi nợ gốc ($\text{FV}$) là một hằng số bằng $100\text{ INR}$, thì mức giá ($\text{PV}$) sẽ thay đổi khi thời gian trôi qua và khi lãi suất biến động.

<!-- PDF Page 57 -->

2. Nếu chúng ta giả định rằng lãi suất giữ nguyên không đổi, thì giá ($\text{PV}$) của trái phiếu sau ba năm nữa là bao nhiêu?

###### **Lời giải (Solution):** 

$33,21\text{ INR}$

Giải tìm $\text{PV}$ bằng cách thay $t = 17$ vào phép tính trước đó theo Phương trình 5:

$$\text{PV} = \text{100 INR} / (1 + 0,067)^{17} = \text{33,21 INR}$$

Mức tăng giá $5,88\text{ INR}$ khi $r$ không đổi đại diện cho tiền lãi ngầm định (*implied interest*) kiếm được trong ba năm đó. Nếu lãi suất là số dương, $\text{PV}$ nhìn chung sẽ tăng dần (hay tích lũy tăng – *accretes*) theo thời gian để tiến tới $\text{FV}$ khi thời gian trôi qua và $t$ tiến dần về 0.

3. Giá cũng thay đổi khi lãi suất thay đổi. Giả sử sau khi mua tại thời điểm $t = 0$, chúng ta quan sát thấy giá trái phiếu sụt giảm ngay lập tức xuống mức $22,68224\text{ INR}$ trên mỗi $100\text{ INR}$ nợ gốc. Lãi suất ngầm định (*implied interest rate*) của trái phiếu chiết khấu này là bao nhiêu?

**Lời giải (Solution):** 

$7,70\%$

Tại đây chúng ta có thể giải tìm $r$ trong Phương trình 5 như sau:

$$\text{22,68224 INR} = \text{100 INR} / (1 + r)^{20}$$

Sắp xếp lại Phương trình 5, chúng ta thu được:

$$r = 7,70\% = (100 / 22,68224)^{1/20} - 1$$

Ngoài ra, chúng ta có thể sử dụng hàm RATE trong Microsoft Excel hoặc Google Sheets:

`=RATE(nper, pmt, PV, FV, type, guess)` sử dụng các đối số giống như trên, với _guess_ là một đối số ước tính tùy chọn (phải nằm trong khoảng từ 0 đến 1 và mặc định là $0,1$), như sau:

$$7,70\% = \text{RATE}(20, 0, -22.68224, 100, 0, 0.1)$$

Điều này cho thấy mức tăng 100 điểm cơ bản ($1,00\%$) của $r$ dẫn đến mức giảm giá $4,65\text{ INR}$, nhấn mạnh mối quan hệ nghịch biến (*inverse relationship*) giữa giá trái phiếu và lợi suất đáo hạn (YTM).

4. Bây giờ hãy xét một trái phiếu được phát hành ở mức lãi suất âm. Vào tháng 7 năm 2016, Đức trở thành quốc gia đầu tiên thuộc khu vực đồng euro phát hành trái phiếu chính phủ kỳ hạn 10 năm với lợi suất âm. Nếu lợi suất đáo hạn (YTM) hàng năm của trái phiếu chính phủ Đức là $-0,05\%$ khi phát hành, hãy tính giá trị hiện tại ($\text{PV}$) của trái phiếu trên mỗi $100\text{ EUR}$ nợ gốc ($\text{FV}$) tại thời điểm phát hành.

**Lời giải (Solution):** 

$100,50\text{ EUR}$

Giải tìm $\text{PV}$ khi biết $r = -0,05\%$, $t = 10$, và $\text{FV}_{10} = 100\text{ EUR}$ bằng cách sử dụng Phương trình 5 (trong bản gốc ghi Equation 1):

$$\text{PV} = \text{100,50 EUR} = \text{100 EUR} / (1 - 0,0005)^{10}$$

hoặc:

$$\text{PV} = (100,50) = \text{PV}(-0.0005, 10, 0, 100, 0)$$

Khi phát hành, trái phiếu này được định giá ở mức **thặng dư (*premium*)** (giá cao hơn mệnh giá), nghĩa là một nhà đầu tư mua trái phiếu khi phát hành đã trả cao hơn $0,50\text{ EUR}$ so với giá trị tương lai dự kiến nhận được khi đáo hạn, tức nợ gốc.

<!-- PDF Page 58 -->

5. Sáu năm sau, khi lạm phát tại Đức đạt mức cao kỷ lục trong nhiều thập kỷ và các nhà đầu tư tăng tỷ suất sinh lợi danh nghĩa yêu cầu của họ, giả sử chúng ta quan sát thấy trái phiếu chính phủ Đức ở câu hỏi 4 hiện đang giao dịch ở mức giá ($\text{PV}$) là $95,72\text{ EUR}$ trên mỗi $100\text{ EUR}$ nợ gốc. Lợi suất đáo hạn (YTM) của trái phiếu này là bao nhiêu?

**Lời giải (Solution):** 

   - $1,10\%$

   - Sử dụng Phương trình 5 để giải tìm $r$ khi biết $\text{PV} = 95,72$, $\text{FV} = 100$, và $t = 4$, chúng ta thu được:

$$\text{95,72 EUR} = \text{100 EUR} / (1 + r)^4; \quad r = 1,10\%, \quad \text{hoặc } 1,10\% = \text{RATE}(4, 0, -95.72, 100, 0, 0.1)$$

Giống như trong trường hợp trái phiếu chiết khấu của Cộng hòa Ấn Độ, lãi suất cao hơn sẽ làm giảm giá trái phiếu. Tuy nhiên, trái ngược với mức giá tích lũy tăng dần (*accreting price*) của trái phiếu chiết khấu, giá của trái phiếu thặng dư (*premium bond*) sẽ giảm dần (hay phân bổ giảm – *amortize*) theo thời gian để tiến về giá trị tương lai $100\text{ EUR}$ khi đáo hạn.

###### **_Công cụ trả lãi định kỳ (Coupon Instrument)_** 

Mô hình dòng tiền định kỳ cho các khoản thanh toán tiền lãi thu nhập cố định với nợ gốc được hoàn trả khi đáo hạn được thể hiện trong Bảng 2 (*Exhibit 2*). Trong trường hợp này, tất cả các khoản thanh toán dòng tiền định kỳ đều giống hệt nhau và diễn ra trên cơ sở nửa năm một lần (*semiannual basis*).

###### **Bảng 2: Dòng tiền của Trái phiếu trả lãi định kỳ (Exhibit 2: Coupon Bond Cash Flows)** 

![](assets/Quantitative_method.pdf-0058-12.png)

<!-- Picture Text: PMT + FV<br>FV<br>Investor receives<br>final coupon and<br>principal payment<br>at maturity<br>PMT PMT PMT PMT PMT PMT PMT PMT PMT PMT<br>0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0 Years<br>Investor pays<br>present value<br>of bond at<br>inception<br>PV<br> -->
> **Chú thích hình ảnh:** Tại thời điểm khởi đầu, nhà đầu tư trả giá trị hiện tại của trái phiếu ($\text{PV}$). Sau mỗi $0,5$ năm (từ $0,5$ đến $4,5$ năm), nhà đầu tư nhận được khoản tiền lãi coupon định kỳ ($\text{PMT}$). Tại năm $5,0$ (khi đáo hạn), nhà đầu tư nhận được khoản thanh toán coupon cuối cùng và nợ gốc ($\text{PMT} + \text{FV}$).

Việc định giá một trái phiếu trả lãi định kỳ (*coupon bond*) mở rộng phép tính dòng tiền đơn lẻ của trái phiếu chiết khấu thành một công thức tổng quát để tính giá trái phiếu ($\text{PV}$) khi biết lãi suất chiết khấu thị trường vào một ngày trả lãi coupon, như sau:

$$\text{PV}(\text{Trái phiếu coupon}) = \frac{\text{PMT}_1}{(1 + r)^1} + \frac{\text{PMT}_2}{(1 + r)^2} + \dots + \frac{\text{PMT}_N + \text{FV}_N}{(1 + r)^N} \tag{6}$$

<!-- PDF Page 59 -->

###### **VÍ DỤ 2 (EXAMPLE 2)** 

###### **Trái phiếu trả lãi hàng năm của Cộng hòa Hy Lạp (Hellenic Republic of Greece Annual Coupon Bond)** 

Vào thời điểm đỉnh dịch COVID, chính phủ Hy Lạp đã phát hành một trái phiếu trả lãi coupon hàng năm $2\%$ có kỳ hạn bảy năm.

1. Nếu lợi suất đáo hạn (YTM) quan sát được khi phát hành là $2,00\%$, thì giá phát hành ($\text{PV}$) trên mỗi $100\text{ EUR}$ nợ gốc là bao nhiêu?

###### **Lời giải (Solution):** 

$100\text{ EUR}$

Giải tìm $\text{PV}$ bằng cách sử dụng Phương trình 6 với $\text{PMT}_i = 2\text{ EUR}$, $r = 2,00\%$, và $\text{FV} = 100\text{ EUR}$:

$$\text{PV} = \text{100 EUR}$$

![](assets/Quantitative_method.pdf-0059-10.png)

$$= \frac{2}{1,02} + \frac{2}{1,02^2} + \frac{2}{1,02^3} + \frac{2}{1,02^4} + \frac{2}{1,02^5} + \frac{2}{1,02^6} + \frac{102}{1,02^7}$$

<!-- Formula Text: =   2 _ 1.02  +   2 _ 1.02 2  +   2 _ 1.02 3  +   2 _ 1.02 4  +   2 _ 1.02 5  +   2 _ 1.02 6  +  102 _ 1.02 7 . -->

Chúng ta có thể giải bài toán này bằng cách sử dụng hàm PV trong Microsoft Excel hoặc Google Sheets đã giới thiệu trước đó (`=PV(0.02, 7, 2, 100, 0)`). Giá phát hành bằng với nợ gốc ($\text{PV} = \text{FV}$). Mối quan hệ này luôn đúng vào ngày trả lãi coupon đối với bất kỳ trái phiếu nào có lãi suất coupon cố định định kỳ bằng với lãi suất chiết khấu.

Giá trị hiện tại của từng dòng tiền có thể được giải bằng Phương trình 5. Ví dụ, dòng tiền lãi và gốc cuối cùng trị giá $102\text{ EUR}$ sau bảy năm là:

$$\text{PV} = \text{88,80 EUR} = \text{102 EUR} / (1,02)^7$$

Bảng sau đây cho thấy giá trị hiện tại của tất cả các dòng tiền của trái phiếu:

|**Năm/Kỳ (Years/Periods)**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|---|---|
|FV||2|2|2|2|2|2|102|
|PV|100,00|1,96|1,92|1,88|1,85|1,81|1,78|88,80|

2. Tiếp theo, giả sử rằng đúng hai năm sau, sự gia tăng mạnh mẽ của lạm phát tại khu vực đồng Euro đã đẩy giá trái phiếu Hy Lạp xuống mức thấp hơn là $93,091\text{ EUR}$ (trên mỗi $100\text{ EUR}$ nợ gốc). Lợi suất đáo hạn (YTM) ngầm định mà các nhà đầu tư kỳ vọng trong những điều kiện thị trường mới này sẽ là bao nhiêu?

###### **Lời giải (Solution):** 

$3,532\%$

Trong trường hợp này, chúng ta phải giải tìm $r$ bằng cách sử dụng Phương trình 6, với $\text{PV}$ bằng $93,091$, như sau:

![](assets/Quantitative_method.pdf-0059-20.png)

$$\text{PV} = 93,091 = \frac{2}{(1 + r)} + \frac{2}{(1 + r)^2} + \frac{2}{(1 + r)^3} + \frac{2}{(1 + r)^4} + \frac{102}{(1 + r)^5}$$

<!-- Formula Text: PV = 93.091 = 2/(1+r) + 2/(1+r)2 + 2/(1+r)3 + 2/(1+r)4 + 102/(1+r)5. -->

Tại đây chúng ta có thể sử dụng hàm RATE trong Microsoft Excel hoặc Google Sheets (`=RATE(5, 2, -93.091, 100, 0, 0.1)`) để giải tìm $r$ bằng $3,532\%$. Các nhà đầu tư nắm giữ trái phiếu có lãi suất coupon cố định sẽ phải đối mặt với khoản lỗ vốn (*capital loss*) khi thị trường kỳ vọng một mức YTM cao hơn.

Lãi suất $r$ được sử dụng để chiết khấu tất cả các dòng tiền trong Phương trình 6 là lợi suất đáo hạn (YTM) của trái phiếu, vốn thường được niêm yết trên cơ sở hàng năm. Tuy nhiên, nhiều trái phiếu do các tổ chức vay công hoặc tư phát hành lại trả lãi trên cơ sở nửa năm một lần (*semiannual basis*). Trong Ví dụ 3, chúng ta xem xét lại trái phiếu Cộng hòa Ấn Độ mà từ đó một dòng tiền đơn lẻ đã được tách ra trong ví dụ đơn giản hóa trước đó.

<!-- PDF Page 60 -->

**VÍ DỤ 3 (EXAMPLE 3)** 

###### **Trái phiếu trả lãi nửa năm một lần của Cộng hòa Ấn Độ (Republic of India Semiannual Coupon Bond)** 

Xét trái phiếu chính phủ Cộng hòa Ấn Độ kỳ hạn 20 năm mà từ đó trái phiếu chiết khấu trong Ví dụ 1 đã được tách ra (*stripped*). Trái phiếu này được phát hành với lãi suất coupon quy đổi theo năm là $6,70\%$ và YTM là $6,70\%$, đồng thời các khoản thanh toán coupon được thực hiện nửa năm một lần.

1. Giải tìm giá của trái phiếu khi phát hành.

**Lời giải (Solution):** 

$100\text{ INR}$

Vì các kỳ coupon là nửa năm một lần, đối với nợ gốc $100\text{ INR}$, $\text{PMT} = 3,35\text{ INR}$ ($= 6,70 / 2$) và lãi suất chiết khấu định kỳ là $3,35\%$ ($= 6,70\% / 2$), như sau:

$$\text{PV} = \frac{3,35}{(1,0335)} + \frac{3,35}{(1,0335)^2} + \dots + \frac{3,35}{(1,0335)^{39}} + \frac{103,35}{(1,0335)^{40}}$$

Như đã trình bày trong Ví dụ 2, bởi vì _lãi suất coupon bằng với YTM_, chúng ta kỳ vọng trái phiếu này có $\text{PV}$ bằng $100\text{ INR}$ khi phát hành.

2. Giá của trái phiếu là bao nhiêu nếu YTM tăng ngay lập tức lên mức $7,70\%$?

###### **Lời giải (Solution):** 

$89,88\text{ INR}$

Chúng ta có thể giải tìm $\text{PV}$ bằng $89,88\text{ INR}$ bằng cách sử dụng Phương trình 6 với $r = 3,85\%$ ($= 7,70 / 2$) hoặc sử dụng hàm PV trong Microsoft Excel hoặc Google Sheets (`=PV(0.0385, 40, 3.35, 100, 0)`). Ba dòng tiền đầu tiên và ba dòng tiền cuối cùng được thể hiện dưới đây:

||**Năm (Years)**|**0**|**0,5**|**1**|**1,5**|**19**|**19,5**|**20**|
|---|---|---|---|---|---|---|---|---|
|**$r$**|**Kỳ (Periods)**|**0**|**1**|**2**|**3**|**38**|**39**|**40**|
||FV||3,35|3,35|3,35|3,35|3,35|103,35|
|6,70%|PV|100,00|3,24|3,14|3,03|0,96|0,93|27,66|
|7,70%|PV|89,88|3,23|3,11|2,99|0,80|0,77|22,81|

3. Tính lại giá trái phiếu chiết khấu cho khoản thanh toán nợ gốc duy nhất sau 20 năm từ Ví dụ 1, trong đó $\text{YTM} = 6,70\%$, và việc chiết khấu được thực hiện nửa năm một lần.

**Lời giải (Solution):** 

$26,77\text{ INR}$

Sử dụng Phương trình 5:

$$\text{PV}(\text{FV}_{40}) = \text{26,77 INR} = 100 / (1,0335)^{40}$$

Khi chiết khấu trên cơ sở nửa năm một lần cho 40 kỳ, $\text{PV}(\text{FV}_{40})$ bằng $26,77$ nhỏ hơn mức $\text{PV}$ ban đầu là $27,33$ khi sử dụng 20 kỳ hàng năm từ Ví dụ 1 (vì $1/(1 + r)^t > 1/(1 + r/2)^{2t}$ khi $r > 0$).

<!-- PDF Page 61 -->

**Trái phiếu vĩnh cửu (*perpetual bond*)** là một loại trái phiếu trả lãi định kỳ ít phổ biến hơn và không có ngày đáo hạn xác định. Hầu hết các trái phiếu vĩnh cửu được các công ty phát hành để huy động nguồn vốn tương tự vốn chủ sở hữu (*equity-like financing*) và thường bao gồm các đặc tính mua lại (*redemption features*). Khi $N \to \infty$ trong Phương trình 6, chúng ta có thể rút gọn công thức này để giải tìm giá trị hiện tại của một **niên kim vĩnh cửu (*perpetuity*)** (hay dòng tiền định kỳ cố định vĩnh viễn không có quyền mua lại trước hạn), với $r > 0$, như sau:

$$\text{PV}(\text{Trái phiếu vĩnh cửu}) = \text{PMT} / r \tag{7}$$

*(Tiếng Anh: $\text{PV}(\text{Perpetual Bond}) = \text{PMT} / r$)*

###### **VÍ DỤ 4 (EXAMPLE 4)** 

###### **Trái phiếu vĩnh cửu của KB Financial (KB Financial Perpetual Bond)** 

Vào năm 2020, KB Financial (công ty mẹ của Ngân hàng Kookmin) đã phát hành 325 tỷ KRW trái phiếu vĩnh cửu với lãi suất coupon trả hàng quý là $3,30\%$.

1. Tính lợi suất đáo hạn (YTM) của trái phiếu nếu giá thị trường là $97,03\text{ KRW}$ (trên mỗi $100\text{ KRW}$ mệnh giá).

###### **Lời giải (Solution):** 

$3,40\%$

Giải tìm $r$ trong Phương trình 7 khi biết $\text{PV}$ là $97,03\text{ KRW}$ và tiền lãi coupon định kỳ hàng quý ($\text{PMT}$) là $0,825\text{ KRW}$ ($= (3,30\% \times \text{100 KRW}) / 4$):

$$\text{97,03 KRW} = \text{0,825 KRW} / r$$

$$r = 0,85\% \text{ mỗi kỳ (quý), hay } 3,40\% (= 0,85\% \times 4) \text{ trên cơ sở quy đổi theo năm.}$$

###### **_Công cụ niên kim (Annuity Instruments)_** 

Các ví dụ về công cụ thu nhập cố định có các khoản thanh toán đều (*level payments*), kết hợp cả dòng tiền lãi và gốc cho đến khi đáo hạn, bao gồm các khoản vay trả góp khấu hao hoàn toàn (*fully amortizing loans*) như khoản vay thế chấp mua nhà (*mortgages*) và một chuỗi thu nhập cố định gồm các dòng tiền vào định kỳ trong một khoảng thời gian hữu hạn được gọi là **niên kim (*annuity*)**. Bảng 3 (*Exhibit 3*) minh họa một ví dụ về các dòng tiền đều hàng tháng dựa trên một khoản vay thế chấp.

###### **Bảng 3: Dòng tiền của Khoản vay thế chấp (Exhibit 3: Mortgage Cash Flows)** 

![](assets/Quantitative_method.pdf-0061-17.png)

<!-- Picture Text: Investor receives a fixed periodic<br>payment equal to the sum of<br>interest and principal payments<br>INT INT INT INT INT<br>INT INT INT INT INT<br>PRN PRN PRN PRN PRN<br>PRN PRN PRN PRN PRN<br>1 2 3 4 5 ... 356 357 358 359 360 Months<br>Borrower<br>receives<br>mortgage loan<br>at inception<br> -->

![](assets/Quantitative_method.pdf-0061-18.png)

<!-- Picture Text: PV<br> -->
> **Chú thích hình ảnh:** Tại thời điểm khởi đầu, người đi vay nhận khoản vay thế chấp ($\text{PV}$). Qua các tháng từ 1 đến 360, nhà đầu tư (người cho vay) nhận được một khoản thanh toán định kỳ cố định bằng tổng của tiền lãi ($\text{INT}$) và tiền trả nợ gốc ($\text{PRN}$), trong đó tỷ trọng $\text{INT}$ giảm dần và $\text{PRN}$ tăng dần theo thời gian.

<!-- PDF Page 62 -->

Chúng ta có thể tính toán dòng tiền niên kim định kỳ ($A$), phát sinh vào cuối mỗi kỳ tương ứng, như sau:

![](assets/Quantitative_method.pdf-0062-05.png)

$$A = \frac{r(\text{PV})}{1 - (1 + r)^{-t}} \tag{8}$$

<!-- Formula Text: A = r(PV) _ 1 − (1 + r) −t  , (8) -->

trong đó:

- $A =$ dòng tiền định kỳ (*periodic cash flow*),

- $r =$ lãi suất thị trường mỗi kỳ (*market interest rate per period*),

- $\text{PV} =$ giá trị hiện tại hoặc số tiền nợ gốc của khoản vay hoặc trái phiếu, và

- $t =$ số kỳ thanh toán (*number of payment periods*).

###### **VÍ DỤ 5 (EXAMPLE 5)** 

###### **Dòng tiền của Khoản vay thế chấp (Mortgage Cash Flows)** 

Một nhà đầu tư tìm kiếm một khoản vay thế chấp kỳ hạn 30 năm với lãi suất cố định để tài trợ $80\%$ giá mua $1.000.000\text{ USD}$ của một tòa nhà dân cư.

1. Tính khoản thanh toán hàng tháng của nhà đầu tư nếu lãi suất thế chấp hàng năm là $5,25\%$.

###### **Lời giải (Solution):** 

Giải tìm $A$ bằng cách sử dụng Phương trình 8 với $r = 0,4375\%$ ($= 5,25\% / 12$), $t = 360$, và $\text{PV} = 800.000\text{ USD}$ ($= 80\% \times \text{1.000.000 USD}$):

![](assets/Quantitative_method.pdf-0062-17.png)

<!-- Formula Text: 0.4375% (USD800, 000) -->

![](assets/Quantitative_method.pdf-0062-18.png)

<!-- Formula Text: A = USD4, 417.63  = 0_ -->

$$A = \text{4.417,63 USD} = \frac{0,4375\% (\text{800.000 USD})}{1 - (1 + 0,4375\%)^{-360}}$$

360 khoản thanh toán đều hàng tháng này bao gồm cả nợ gốc và tiền lãi.

2. Chi tiết phần trả nợ gốc (*principal amortization*) và tiền lãi của hai dòng tiền hàng tháng đầu tiên là bao nhiêu?

###### **Lời giải (Solution):** 

- Tháng 1: tiền lãi là $3.500\text{ USD}$ và tiền trả nợ gốc là $917,63\text{ USD}$
- Tháng 2: tiền lãi là $3.495,99\text{ USD}$ và tiền trả nợ gốc là $921,64\text{ USD}$

**Tháng 1:**

- Tiền lãi: $\text{3.500 USD} = \text{800.000 USD} \times 0,4375\%$ ($= \text{PV}_0 \times r$)
- Phần trả nợ gốc: $\text{4.417,63 USD} - \text{3.500 USD} = \text{917,63 USD}$
- Nợ gốc còn lại ($\text{PV}_1$): $\text{799.082,37 USD} = \text{800.000 USD} - \text{917,63 USD}$

**Tháng 2:**

- Tiền lãi: $\text{3.495,99 USD} = \text{799.082,37 USD} \times 0,4375\%$ ($= \text{PV}_1 \times r$)
- Phần trả nợ gốc: $\text{4.417,63 USD} - \text{3.495,99 USD} = \text{921,64 USD}$
- Nợ gốc còn lại ($\text{PV}_2$): $\text{798.160,73 USD} = \text{799.082,37 USD} - \text{921,64 USD}$

Mặc dù khoản thanh toán thế chấp định kỳ là không đổi, tỷ trọng tiền lãi trong mỗi lần thanh toán giảm dần trong khi phần trả nợ gốc tăng dần theo

<!-- PDF Page 63 -->

thời gian. Bảng tính sau đây cho thấy ba dòng tiền hàng tháng đầu tiên và ba dòng tiền hàng tháng cuối cùng.

|**Tháng (Month)**|**Tổng khoản thanh toán hàng tháng (Total Monthly Payment)**|**Thanh toán tiền lãi hàng tháng (Monthly Interest Payment)**|**Hoàn trả nợ gốc hàng tháng (Monthly Principal Repayment)**|**Nợ gốc còn lại (Remaining Principal)**|
|---|---|---|---|---|
|1|$ 4.417,63|$ 3.500,00|$ 917,63|$ 799.082,37|
|2|$ 4.417,63|$ 3.495,99|$ 921,64|$ 798.160,73|
|3|$ 4.417,63|$ 3.491,95|$ 925,68|$ 797.235,05|
|…|||||
|358|$ 4.417,63|$ 57,48|$ 4.360,15|$ 8.777,61|
|359|$ 4.417,63|$ 38,40|$ 4.379,23|$ 4.398,39|
|360|$ 4.417,63|$ 19,24|$ 4.398,39|$ 0,00|

###### **Các Công cụ Vốn chủ sở hữu và Giá trị Thời gian của Tiền (Equity Instruments and the Time Value of Money)** 

Các khoản đầu tư vốn chủ sở hữu (*equity investments*), chẳng hạn như cổ phiếu ưu đãi (*preferred stock*) hoặc cổ phiếu phổ thông (*common stock*), đại diện cho các cổ phần sở hữu trong một công ty, trao quyền cho các nhà đầu tư được nhận bất kỳ dòng tiền tùy ý nào dưới hình thức cổ tức (*dividends*). Khác với các công cụ thu nhập cố định, các khoản đầu tư vốn chủ sở hữu không có ngày đáo hạn và được giả định là sẽ lưu hành vô thời hạn, hoặc cho đến khi công ty được bán, tái cơ cấu hoặc thanh lý. Một cách để định giá cổ phiếu của một công ty là chiết khấu các dòng tiền dự kiến trong tương lai bằng một mức tỷ suất sinh lợi kỳ vọng ($r$). Các dòng tiền này bao gồm bất kỳ khoản cổ tức định kỳ nào nhận được cộng với mức giá dự kiến nhận được vào cuối khung thời gian đầu tư.

Các giả định phổ biến gắn liền với việc định giá các công cụ vốn chủ sở hữu dựa trên dòng tiền cổ tức thường tuân theo một trong ba phương pháp tiếp cận tổng quát sau:

- **Cổ tức không đổi (*Constant Dividends*):** Nhà đầu tư trả một mức giá ban đầu ($\text{PV}$) cho một cổ phiếu ưu đãi hoặc cổ phiếu phổ thông và nhận được một khoản cổ tức định kỳ cố định ($D$).

- **Tốc độ tăng trưởng cổ tức không đổi (*Constant Dividend Growth Rate*):** Nhà đầu tư trả một mức giá ban đầu ($\text{PV}$) cho một cổ phiếu và nhận được khoản cổ tức ban đầu sau một kỳ ($D_{t+1}$), khoản cổ tức này được kỳ vọng sẽ tăng trưởng theo thời gian với tốc độ không đổi là $g$.

- **Tốc độ tăng trưởng cổ tức thay đổi (*Changing Dividend Growth Rate*):** Nhà đầu tư trả một mức giá ban đầu ($\text{PV}$) cho một cổ phiếu và nhận được khoản cổ tức ban đầu sau một kỳ ($D_{t+1}$). Cổ tức được kỳ vọng sẽ tăng trưởng với tốc độ thay đổi theo thời gian khi công ty chuyển từ giai đoạn tăng trưởng cao ban đầu sang tăng trưởng chậm hơn khi đạt đến độ trưởng thành (*maturity*).

Trường hợp đơn giản nhất của một cổ phiếu được giả định trả cổ tức không đổi đến vĩnh viễn được thể hiện trong Bảng 4 (*Exhibit 4*).

<!-- PDF Page 64 -->

###### **Bảng 4: Dòng tiền Vốn chủ sở hữu với Cổ tức không đổi (Exhibit 4: Equity Cash Flows with Constant Dividends)** 

![](assets/Quantitative_method.pdf-0064-04.png)

<!-- Picture Text: Constant dividend<br>D D D D D paid immediately<br>1 2 3 4 5 Years<br>Investor pays<br>share price<br>today<br>PV<br> -->
> **Chú thích hình ảnh:** Nhà đầu tư trả giá cổ phiếu ngày hôm nay ($\text{PV}$) và nhận được khoản cổ tức không đổi ($D$) định kỳ qua các năm $1, 2, 3, 4, 5, \dots$ kéo dài vô thời hạn (*indefinitely*).

Giá của một cổ phiếu ưu đãi hoặc cổ phiếu phổ thông dự kiến trả một khoản cổ tức định kỳ không đổi là một chuỗi vô hạn được rút gọn về công thức tính giá trị hiện tại của một niên kim vĩnh cửu như dưới đây và tương tự như việc định giá một trái phiếu vĩnh cửu mà chúng ta đã gặp trước đó. Cụ thể, cách định giá tương tự Phương trình 7:

![](assets/Quantitative_method.pdf-0064-06.png)

$$\text{PV}_t = \sum_{i=1}^{\infty} \frac{D_t}{(1 + r)^i} \tag{9}$$

và

$$\text{PV}_t = \frac{D_t}{r} \tag{10}$$

<!-- Formula Text: P V t = ∑ i=1 ∞ D t _ (1 + r) i , and (9) P V t  = D t _ r . (10) -->

###### **VÍ DỤ 6 (EXAMPLE 6)** 

###### **Dòng tiền Cổ tức không đổi (Constant Dividend Cash Flows)** 

Shipline PLC là một công ty trả cổ tức đều đặn ở mức $1,50\text{ GBP}$ mỗi năm, được kỳ vọng sẽ tiếp tục duy trì vô thời hạn.

1. Giá cổ phiếu dự kiến của Shipline là bao nhiêu nếu tỷ suất sinh lợi yêu cầu của các cổ đông là $15\%$?

###### **Lời giải (Solution):** 

- $10\text{ GBP}$

Giải tìm $\text{PV}$ bằng cách sử dụng Phương trình 10, trong đó $D$ là $1,50\text{ GBP}$ và tỷ suất sinh lợi mỗi kỳ $r$ là $15\%$:

$$\text{PV} = \text{10,00 GBP} = \text{1,50 GBP} / 0,15$$

Ngoài ra, một phương pháp dự báo vốn chủ sở hữu phổ biến là giả định tốc độ tăng trưởng cổ tức không đổi ($g$) đến vĩnh viễn, như được minh họa trong Bảng 5 (*Exhibit 5*).

<!-- PDF Page 65 -->

**Bảng 5: Dòng tiền Vốn chủ sở hữu với Tăng trưởng Cổ tức không đổi (Exhibit 5: Equity Cash Flows with Constant Dividend Growth)** 

![](assets/Quantitative_method.pdf-0065-03.png)

<!-- Picture Text: D ( 1 + g ) 5<br>D ( 1 + g ) 4<br>D ( 1 + g ) 3<br>D ( 1 + g ) 2<br>Dividend grows at  g<br>D ( 1 + g )<br>indefintely<br>1 2 3 4 5 Years<br>Investor pays<br>share price<br>today<br>PV<br> -->
> **Chú thích hình ảnh:** Nhà đầu tư trả giá cổ phiếu ngày hôm nay ($\text{PV}$) và nhận cổ tức tăng trưởng với tốc độ $g$ vô thời hạn: Năm 1 là $D(1+g)$, Năm 2 là $D(1+g)^2$, Năm 3 là $D(1+g)^3$, Năm 4 là $D(1+g)^4$, Năm 5 là $D(1+g)^5, \dots$

Nếu cổ tức tăng trưởng với tốc độ $g$ mỗi kỳ và được thanh toán vào cuối mỗi kỳ, thì khoản cổ tức tiếp theo (tại thời điểm $t + 1$) có thể được biểu diễn như sau:

![](assets/Quantitative_method.pdf-0065-05.png)

$$D_{t+1} = D_t(1 + g) \tag{11}$$

hoặc tổng quát sau $i$ kỳ là:

$$D_{t+i} = D_t(1 + g)^i \tag{12}$$

<!-- Formula Text: Dt +1 = Dt (1 + g), (11) or generally in i periods as: Dt +i= Dt (1 + g)i. (12) -->

Nếu các dòng tiền cổ tức tiếp tục tăng trưởng ở mức $g$ vô thời hạn, thì chúng ta có thể viết lại Phương trình 10 như sau:

![](assets/Quantitative_method.pdf-0065-07.png)

$$\text{PV}_t = \sum_{i=1}^{\infty} \frac{D_t(1 + g)^i}{(1 + r)^i} \tag{13}$$

được rút gọn thành:

$$\text{PV}_t = \frac{D_t(1 + g)}{r - g} = \frac{D_{t+1}}{r - g} \tag{14}$$

<!-- Formula Text: P V t = ∑ i=1 ∞ D t (1 + g) i _ (1 + r) i   , (13) ich simplifies to: P V t = D t(1 + g) _ r − g    = D t+1 _ r − g  , (14) -->

trong đó $r - g > 0$.

Một phương án thay thế cho tăng trưởng cổ tức không đổi là giả định tốc độ tăng trưởng thay đổi (*changing growth*). Giả định này rất phổ biến khi đánh giá giá cổ phiếu của các doanh nghiệp dự kiến sẽ trải qua sự gia tăng dòng tiền nhanh chóng ban đầu, theo sau là mức tăng trưởng chậm hơn khi công ty trưởng thành. Dạng đơn giản nhất của tăng trưởng cổ tức thay đổi là mô hình hai giai đoạn (*two-stage model*) được thể hiện trong Bảng 6 (*Exhibit 6*).

<!-- PDF Page 66 -->

**Bảng 6: Dòng tiền Vốn chủ sở hữu với Tăng trưởng Cổ tức Hai giai đoạn (Exhibit 6: Equity Cash Flows with Two-Stage Dividend Growth)** 

![](assets/Quantitative_method.pdf-0066-04.png)

<!-- Picture Text: D ( 1 + gs ) 3 ( 1 + g1 ) 2<br>D ( 1 + gs ) 3 ( 1 + g1 )<br>D ( 1 + gs ) 3<br>D ( 1 + gs ) 2<br>Dividend grows at<br>D ( 1 + gs )<br>g1  indefintely<br>1 2 3 4 5 Years<br>Investor pays<br>share price<br>today<br>PV<br>g<br>gs<br>g1<br>Years<br> -->
> **Chú thích hình ảnh:** Nhà đầu tư trả giá cổ phiếu ngày hôm nay ($\text{PV}$). Trong 3 năm đầu, cổ tức tăng trưởng ở mức cao ngắn hạn $g_s$: $D(1+g_s)$, $D(1+g_s)^2$, $D(1+g_s)^3$. Từ năm thứ 4 trở đi, cổ tức tăng trưởng ở mức dài hạn $g_l$ vô thời hạn: $D(1+g_s)^3(1+g_l)$, $D(1+g_s)^3(1+g_l)^2, \dots$

Ví dụ trong Bảng 6 cho thấy một công ty có mức tăng trưởng cổ tức ngắn hạn ban đầu cao hơn là $g_s$ trong ba năm đầu tiên, theo sau là mức tăng trưởng dài hạn thấp hơn ($g_l$, với $g_s > g_l$) vô thời hạn kể từ đó trở đi. Nếu chúng ta tổng quát hóa giai đoạn tăng trưởng ban đầu thành $n$ kỳ, theo sau là giai đoạn tăng trưởng chậm hơn vô thời hạn ở mức $g_l$, chúng ta thu được một phiên bản điều chỉnh của Phương trình 14 như sau:

![](assets/Quantitative_method.pdf-0066-06.png)

$$\text{PV}_t = \sum_{i=1}^{n} \frac{D_t(1 + g_s)^i}{(1 + r)^i} + \sum_{j=n+1}^{\infty} \frac{D_{t+n}(1 + g_l)^{j-n}}{(1 + r)^j} \tag{15}$$

<!-- Formula Text: P V t = ∑ i=1 n D t (1 + g s) i _ (1 + r) i  + ∑ j=n+1 ∞ D t+n (1 + g l) j _ (1 + r) j  . (15) -->

![](assets/Quantitative_method.pdf-0066-07.png)

Lưu ý rằng biểu thức thứ hai trong Phương trình 15 liên quan đến sự tăng trưởng không đổi bắt đầu sau $n$ kỳ, do đó chúng ta có thể thay thế bằng công thức rút gọn cấp số nhân như sau:

$$\text{PV}_t = \sum_{i=1}^{n} \frac{D_t(1 + g_s)^i}{(1 + r)^i} + \frac{E(S_{t+n})}{(1 + r)^n} \tag{16}$$

<!-- Formula Text: Note that the second expression in Equation 15 involves constant growth starting in n periods, for which we can substitute the geometric series simplification: P V t = ∑ i=1 n D t (1 + g s) i _ (1 + r) i  + E(S t+n) _ (1 + r) n  , (16) -->

trong đó giá trị của cổ phiếu sau $n$ kỳ ($E(S_{t+n})$ được gọi là **giá trị cuối kỳ (*terminal value*)**) và bằng với công thức sau:

![](assets/Quantitative_method.pdf-0066-09.png)

$$E(S_{t+n}) = \frac{D_{t+n+1}}{r - g_l} \tag{17}$$

<!-- Formula Text: E(S t+n ) = D t+n+1 _ r− g l . (17) -->

Chúng ta xem xét lại ví dụ về giá cổ phiếu của Shipline PLC để đánh giá tác động của các giả định cổ tức không đổi, tăng trưởng cổ tức không đổi và tăng trưởng cổ tức thay đổi đối với giá cổ phiếu dự kiến của một công ty.

###### **VÍ DỤ 7 (EXAMPLE 7)** 

###### **Tăng trưởng Cổ tức không đổi và Tăng trưởng Cổ tức thay đổi (Constant and Changing Dividend Growth)** 

Hãy nhớ lại rằng dựa trên mức cổ tức hàng năm không đổi là $1,50\text{ GBP}$ và tỷ suất sinh lợi yêu cầu là $15\%$, chúng ta đã chỉ ra rằng giá cổ phiếu dự kiến của Shipline PLC là $10,00\text{ GBP}$. Thay vào đó, giả sử một nhà phân tích đầu tư giả định rằng Shipline sẽ tăng cổ tức hàng năm ở mức $6\%$ mỗi năm vô thời hạn.

<!-- PDF Page 67 -->

1. Giá cổ phiếu dự kiến của Shipline thay đổi như thế nào dưới giả định tăng trưởng không đổi của nhà phân tích?

###### **Lời giải (Solution):** 

$17,67\text{ GBP}$

Sử dụng Phương trình 14, giải tìm $\text{PV}$ với $D_{t+1} = 1,59\text{ GBP}$ ($= \text{1,50 GBP} \times (1 + 0,06)$), $r = 15\%$, và $g = 6\%$:

$$\text{PV} = \text{1,59 GBP} / (15\% - 6\%) = \text{17,67 GBP}$$

Lưu ý rằng tốc độ tăng trưởng $g$ cao hơn sẽ làm tăng $\text{PV}$ bằng cách làm giảm mẫu số ($r - g$).

2. Giá cổ phiếu dự kiến của Shipline thay đổi như thế nào nếu thay vào đó chúng ta giả định mức tăng trưởng cổ tức ban đầu là $6\%$ trong giai đoạn ba năm, theo sau là mức tăng trưởng cổ tức không đổi $2\%$ kể từ đó trở đi?

**Lời giải (Solution):** 

$13,05\text{ GBP}$

Chúng ta có thể giải tìm giá cổ phiếu dự kiến ($\text{PV}$) của Shipline bằng cách sử dụng các Phương trình 15–17 với $D_t = 1,50$, $g_s = 6\%$, $n = 3$, $r = 15\%$, và $g_l = 2\%$, như sau:

![](assets/Quantitative_method.pdf-0067-11.png)

$$\text{PV}_t = \sum_{i=1}^{3} \frac{1,50(1 + 0,06)^i}{(1 + 0,15)^i} + \sum_{j=4}^{\infty} \frac{D_{t+3}(1 + 0,02)^{j-3}}{(1 + 0,15)^j}$$

<!-- Formula Text: P V t = ∑ i=1 3    1.50 (1 + 0.06) i ___________ (1 + 0.15) i  + ∑ j=4 ∞ D t+3 (1 + 0.02) j ___________ (1 + 0.15) j  . -->

Ở bước đầu tiên, chúng ta tính giá trị hiện tại của các khoản cổ tức gắn với tốc độ tăng trưởng cao hơn ($6\%$) trong ba năm đầu tiên như được thể hiện ở biểu thức thứ nhất. Ở bước thứ hai, chúng ta tính giá trị hiện tại của các khoản cổ tức tương lai ở tốc độ tăng trưởng thấp hơn ($2\%$) cho một giai đoạn vô thời hạn. Tổng của hai bước này chính là giá cổ phiếu dự kiến.

- **Bước 1:** Giải bước đầu tiên thu được $3,832\text{ GBP}$ với các dòng tiền cổ tức cho giai đoạn tăng trưởng ban đầu như được thể hiện trong bảng tính sau:

|**$t$**|**$D$**|**$\text{PV}(D)$ tại mức $r\%$**|
|---|---|---|
|0|1,500||
|1|1,590|1,383|
|2|1,685|1,274|
|3|1,787|1,175|
|$\text{PV}(\text{tăng trưởng ngắn hạn})$||3,832|

- **Bước 2:** Như đã trình bày trong Phương trình 16 và 17, biểu thức thứ hai được rút gọn như sau:

$$\frac{E(S_3)}{(1 + r)^3}; \quad \text{với } E(S_3) = \frac{D_4}{r - g_l}$$

*(Lưu ý: Bản gốc ký hiệu giá trị cuối kỳ tại $t=3$ là $E(S_4)$ nhưng chiết khấu 3 kỳ $(1+r)^3$ dựa trên cổ tức $D_4$).*

Chúng ta có thể giải tìm $D_4$ bằng $1,823\text{ GBP}$ ($= 1,787 \times 1,02 = D_3(1 + g_l)$) và giá trị của biểu thức thứ hai là $9,22\text{ GBP}$ như sau:

![](assets/Quantitative_method.pdf-0067-17.png)

$$\text{9,22 GBP} = \frac{1,823 / (0,15 - 0,02)}{(1,15)^3}$$

<!-- Formula Text: GBP9.22 = 1.823 ⧸(0.15 − 0.02) _____________ (1.15) 3 . -->

- **Bước 3:** Tổng của hai bước này mang lại cho chúng ta mức giá cổ phiếu dự kiến của Shipline là $13,05\text{ GBP}$ ($= 3,83 + 9,22$).

Trong bảng tiếp theo (ở đầu Phần 2/4), chúng tôi trình bày độ nhạy của giá cổ phiếu dự kiến ($\text{PV}$) của Shipline trước những thay đổi trong tốc độ tăng trưởng dài hạn ($g_l$) sau ba năm tăng trưởng cổ tức ở mức $6\%$:


---

# Tập 1: Phương pháp Định lượng (Volume 1: Quantitative Methods)
## Học phần 2: Giá trị Thời gian của Tiền trong Tài chính (Learning Module 2: Time Value of Money in Finance)
### Phần 2/4: Tỷ suất sinh lợi ngầm định và Tốc độ tăng trưởng ngầm định (Implied Return and Growth) (Trang PDF 68–76)

---

<!-- PDF Page 68 -->

|**Giá cổ phiếu (Share Price)**|**Tốc độ tăng trưởng dài hạn (LT Growth Rate)**|
|---|---|
|11,66|0%|
|13,05|2%|
|14,94|4%|
|17,67|6%|

# **<mark>3</mark>** 

## **TỶ SUẤT SINH LỢI NGẦM ĐỊNH VÀ TỐC ĐỘ TĂNG TRƯỞNG NGẦM ĐỊNH (IMPLIED RETURN AND GROWTH)** 

tính toán và diễn giải tỷ suất sinh lợi ngầm định (*implied return*) của các công cụ thu nhập cố định cùng với tỷ suất sinh lợi yêu cầu (*required return*) và tốc độ tăng trưởng ngầm định (*implied growth*) của các công cụ vốn chủ sở hữu khi biết trước giá trị hiện tại (PV) và các dòng tiền

Bài học 1 đã giải quyết sự đánh đổi về giá trị thời gian của tiền giữa các dòng tiền phát sinh ngày hôm nay so với những dòng tiền trong tương lai đối với một số công cụ thu nhập cố định và công cụ vốn chủ sở hữu nhất định. Những người tham gia thị trường thường đối mặt với một tình huống trong đó cả giá trị hiện tại và giá trị tương lai của các công cụ hoặc các dòng tiền đều đã được biết trước. Trong trường hợp này, hoàn toàn có thể giải tìm tỷ suất sinh lợi ngầm định hoặc tốc độ tăng trưởng ngầm định hàm chứa trong mức giá hiện hành và các đặc điểm của các dòng tiền tương lai. Theo nghĩa này, việc giải tìm tốc độ tăng trưởng hoặc tỷ suất sinh lợi ngầm định cung cấp một góc nhìn về những kỳ vọng của thị trường đang được phản ánh vào trong giá thị trường của tài sản đó.

### **Tỷ suất sinh lợi ngầm định đối với các Công cụ Thu nhập Cố định (Implied Return for Fixed-Income Instruments)** 

Các công cụ thu nhập cố định được đặc trưng bởi các dòng tiền lãi và gốc theo hợp đồng. Nếu chúng ta quan sát được giá trị hiện tại (hay mức giá) và giả định rằng tất cả các dòng tiền tương lai đều diễn ra đúng như đã cam kết, thì lãi suất chiết khấu ($r$) hay lợi suất đáo hạn ($\text{YTM}$) là một thước đo tỷ suất sinh lợi ngầm định dưới những giả định này đối với mô hình dòng tiền đó.

Trong trường hợp của một trái phiếu chiết khấu hoặc công cụ chiết khấu, hãy nhớ lại rằng một nhà đầu tư nhận được một dòng tiền nợ gốc duy nhất ($\text{FV}$) khi đáo hạn, với ($\text{FV} - \text{PV}$) đại diện cho phần sinh lợi ngầm định, như được thể hiện trong Bảng 7 (*Exhibit 7*).

<!-- PDF Page 69 -->

#### **Bảng 7: Tỷ suất sinh lợi ngầm định của Trái phiếu Chiết khấu (Exhibit 7: Discount Bond Implied Return)** 

![](assets/Quantitative_method.pdf-0069-04.png)

<!-- Picture Text: FV<br>Bond principal<br>payment at maturity<br>5.0 Years<br>Discounted<br>bond value at<br>inception (1+r) t<br>PV<br> -->
> **Chú thích hình ảnh:** Giá trị trái phiếu chiết khấu tại thời điểm khởi đầu ($\text{PV}$) tăng trưởng theo hệ số $(1+r)^t$ qua $5,0$ năm để đạt tới khoản thanh toán nợ gốc trái phiếu khi đáo hạn ($\text{FV}$).

Chúng ta có thể sắp xếp lại Phương trình 5 ở phần trước để giải tìm tỷ suất sinh lợi định kỳ ngầm định kiếm được trong suốt vòng đời của công cụ ($t$ kỳ):

![](assets/Quantitative_method.pdf-0069-06.png)

$$r = \sqrt[t]{\frac{\text{FV}_t}{\text{PV}}} - 1 = \left(\frac{\text{FV}_t}{\text{PV}}\right)^{\frac{1}{t}} - 1 \tag{18}$$

<!-- Formula Text: r  = t √ _ F V t _ PV   − 1   =  ( F V t _ PV ) 1 _ t − 1. (18) -->

#### **VÍ DỤ 8 (EXAMPLE 8)** 

### **Tỷ suất sinh lợi ngầm định của Trái phiếu Chiết khấu (Discount Bond Implied Return)** 

Hãy nhớ lại từ Ví dụ 1 rằng vào năm 2016, các nhà đầu tư trái phiếu chính phủ Đức kỳ hạn 10 năm đã đối mặt với mức giá là $100,50\text{ EUR}$ trên mỗi $100\text{ EUR}$ nợ gốc và lợi suất đáo hạn (YTM) hàng năm là $-0,05\%$ khi phát hành. Nghĩa là, trái phiếu chính phủ Đức kỳ hạn 10 năm ban đầu được thị trường định giá để mang lại tỷ suất sinh lợi âm cho nhà đầu tư. Sáu năm sau, những trái phiếu này được giao dịch ở mức giá ($\text{PV}$) là $95,72\text{ EUR}$ trên mỗi $100\text{ EUR}$ nợ gốc.

1. Tỷ suất sinh lợi ngầm định của nhà đầu tư ban đầu đối với trái phiếu này trong thời kỳ nắm giữ sáu năm là bao nhiêu?

#### **Lời giải (Solution):** 

$-0,81\%$

Chúng ta có thể giải tìm tỷ suất sinh lợi quy đổi theo năm ($r$) của nhà đầu tư bằng cách sử dụng Phương trình 18 với $\text{PV} = 100,5$, $\text{FV} = 95,72$, và $t = 6$ như sau:

![](assets/Quantitative_method.pdf-0069-14.png)

$$r = -0,81\% = \left(\frac{95,72}{100,5}\right)^{\frac{1}{6}} - 1$$

<!-- Formula Text: r = − 0.81 %   =  ( 95.72 _ 100.5 ) 1 _ 6 − 1. -->

Lưu ý rằng một nhà đầu tư mua trái phiếu chiết khấu khi phát hành và nhận được $100\text{ EUR}$ sau 10 năm sẽ kỳ vọng mức tỷ suất sinh lợi ngầm định bằng với YTM lúc phát hành là $-0,05\%$. Tuy nhiên, mức giảm giá $4,78\text{ EUR}$ trong sáu năm đầu tiên đã chuyển thành mức tỷ suất sinh lợi quy đổi theo năm là $-0,81\%$, thấp hơn mức YTM ban đầu là $-0,05\%$. Tỷ suất sinh lợi âm này hoàn toàn nhất quán với sự sụt giảm dự kiến trong giá ($\text{PV}$) của một trái phiếu chiết khấu trong bối cảnh lạm phát tăng cao hơn.

<!-- PDF Page 70 -->

2. Tỷ suất sinh lợi kỳ vọng của một nhà đầu tư mua trái phiếu chiết khấu ở mức giá $95,72\text{ EUR}$ và nắm giữ nó trong bốn năm còn lại là bao nhiêu?

#### **Lời giải (Solution):** 

$1,10\%$

Tại đây, mức giá hiện hành $95,72$ trong Phương trình 18 bây giờ đóng vai trò là $\text{PV}$, và nợ gốc $100$ là $\text{FV}$, với $t = 4$:

![](assets/Quantitative_method.pdf-0070-07.png)

$$r = 1,10\% = \left(\frac{100}{95,72}\right)^{\frac{1}{4}} - 1$$

<!-- Formula Text: r = 1.10 %   =  ( 100 _ 95.72 ) 1 _ 4 − 1. -->

Lưu ý rằng $r = 1,10\%$ bằng với mức YTM cho bốn năm còn lại mà chúng ta đã suy ra trong Ví dụ 1. Tỷ suất sinh lợi tích lũy qua hai nhà đầu tư đúng bằng mức YTM ban đầu là $-0,05\%$, giả định không có chi phí giao dịch, như sau:

![](assets/Quantitative_method.pdf-0070-09.png)

$$-0,05\% = \left[(1 - 0,0081)^6 \times (1 + 0,011)^4\right]^{\frac{1}{10}} - 1$$

<!-- Formula Text: − 0.05 %   =  [(1 − 0.0081) 6 × (1 + 0.011) 4]  1 _ 10 − 1. -->

Các mối quan hệ này được tóm tắt trong sơ đồ sau:

![](assets/Quantitative_method.pdf-0070-11.png)

<!-- Picture Text: 100<br>95.72<br>–0.8%<br>10.0 Years<br>1.10%<br>95.72<br>100.5<br>Initial 6y Final 4y<br>Annualized Return: Annualized Return:<br>–0.8% 1.10%<br>Full 10y Annualized Return (YTM)<br>–0.05%<br> -->
> **Chú thích hình ảnh:** Trong 6 năm đầu (*Initial 6y*), giá giảm từ $100,5$ xuống $95,72$, tương ứng Tỷ suất sinh lợi quy đổi theo năm (*Annualized Return*) là $-0,81\%$ (trong hình ghi $-0,8\%$). Trong 4 năm cuối (*Final 4y*), giá tăng từ $95,72$ lên $100$, tương ứng Tỷ suất sinh lợi quy đổi theo năm là $1,10\%$. Tỷ suất sinh lợi quy đổi theo năm cho toàn bộ 10 năm (*Full 10y Annualized Return – YTM*) là $-0,05\%$.

Khác với trái phiếu chiết khấu, các công cụ thu nhập cố định trả lãi định kỳ có các dòng tiền phát sinh trong suốt vòng đời của chúng cho đến khi đáo hạn. Lãi suất chiết khấu đồng nhất (hay tỷ suất hoàn vốn nội bộ) cho tất cả các dòng tiền đã cam kết chính là lợi suất đáo hạn (YTM), một mức lãi suất chiết khấu thị trường ngầm định duy nhất áp dụng cho mọi dòng tiền bất kể thời điểm phát sinh như được thể hiện đối với trái phiếu trả lãi định kỳ trong Bảng 8 (*Exhibit 8*).

<!-- PDF Page 71 -->

#### **Bảng 8: Tỷ suất sinh lợi ngầm định của Trái phiếu trả lãi định kỳ (Exhibit 8: Coupon Bond Implied Return)** 

![](assets/Quantitative_method.pdf-0071-04.png)

<!-- Picture Text: PMT + FV<br>FV<br>Final coupon and<br>principal payment<br>at maturity<br>YTM = IRR<br>PMT PMT PMT PMT PMT PMT PMT PMT PMT PMT<br>0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0 Years<br>Present value<br>of bond at<br>inception<br>PV<br> -->
> **Chú thích hình ảnh:** Giá trị hiện tại của trái phiếu tại thời điểm khởi đầu ($\text{PV}$), các dòng tiền coupon định kỳ ($\text{PMT}$) từ năm $0,5$ đến $4,5$, và khoản thanh toán coupon cuối cùng cộng nợ gốc khi đáo hạn ($\text{PMT} + \text{FV}$) tại năm $5,0$ được liên kết với nhau qua mức lợi suất đáo hạn $\text{YTM} = \text{IRR}$.

Lợi suất đáo hạn (YTM) giả định rằng nhà đầu tư kỳ vọng sẽ nhận được tất cả các dòng tiền đã cam kết cho đến khi đáo hạn và tái đầu tư bất kỳ khoản tiền mặt nào nhận được ở cùng mức YTM đó. Đối với trái phiếu trả lãi định kỳ, điều này chỉ liên quan đến các khoản thanh toán tiền lãi định kỳ, trong khi đối với các công cụ thanh toán đều như khoản vay thế chấp, phép tính giả định cả tiền lãi và nợ gốc được hoàn trả đều có thể được tái đầu tư ở cùng một mức lãi suất. Giống như các tỷ suất hoàn vốn nội bộ khác, YTM không thể giải trực tiếp bằng một phương trình đại số đơn giản, nhưng có thể được tính bằng phương pháp lặp (*iteration*) với bảng tính hoặc máy tính tài chính — một quá trình giải tìm $r$ trong Phương trình 19 như sau:

![](assets/Quantitative_method.pdf-0071-07.png)

$$\text{PV}(\text{Trái phiếu coupon}) = \frac{\text{PMT}_1}{(1 + r)^1} + \frac{\text{PMT}_2}{(1 + r)^2} + \dots + \frac{(\text{PMT}_N + \text{FV}_N)}{(1 + r)^N} \tag{19}$$

<!-- Formula Text: = PMT1 / (1 + r)1 + PMT2 / (1 + r)2 + … + (PMTN + FVN) / (1 + r)N, (19) -->

trong đó $\text{FV}$ bằng nợ gốc của trái phiếu và $N$ là số kỳ cho đến khi đáo hạn.

Hàm YIELD trong Microsoft Excel hoặc Google Sheets có thể được sử dụng để tính YTM cho các công cụ thu nhập cố định có trả lãi định kỳ và thanh toán toàn bộ nợ gốc khi đáo hạn:

`=YIELD(settlement, maturity, rate, pr, redemption, frequency, [basis])`

trong đó:

- _settlement_ = ngày thanh toán giao dịch (*settlement date*) được nhập bằng hàm DATE;

- _maturity_ = ngày đáo hạn (*maturity date*) được nhập bằng hàm DATE;

- _rate_ = lãi suất coupon hàng năm (trả định kỳ hoặc nửa năm một lần);

- _pr_ = mức giá trên mỗi 100 đơn vị mệnh giá;

- _redemption_ = giá trị tương lai (giá trị hoàn trả) khi đáo hạn;

- _frequency_ = số lần trả coupon mỗi năm; và

- _[basis]_ = quy ước đếm ngày (*day count convention*), thông thường là 0 đối với trái phiếu Hoa Kỳ (quy ước đếm ngày 30/360).

Ví dụ 9 minh họa tỷ suất sinh lợi ngầm định đối với các công cụ thu nhập cố định có trả lãi định kỳ.

<!-- PDF Page 72 -->

#### **VÍ DỤ 9 (EXAMPLE 9)** 

### **Tỷ suất sinh lợi ngầm định của Trái phiếu trả lãi định kỳ Hy Lạp (Greek Coupon Bond Implied Return)** 

Hãy nhớ lại từ Ví dụ 2 rằng trái phiếu chính phủ Hy Lạp kỳ hạn bảy năm được phát hành vào năm 2020 với lãi suất coupon hàng năm $2,00\%$ có mức giá là $93,091\text{ EUR}$ trên mỗi $100\text{ EUR}$ nợ gốc vào hai năm sau đó.

1. Tỷ suất sinh lợi ngầm định trong hai năm đối với một nhà đầu tư có khả năng tái đầu tư tiền lãi định kỳ ở mức YTM ban đầu là $2,00\%$ là bao nhiêu?

**Lời giải (Solution):** 

$-1,445\%$

Sử dụng Phương trình 18 giống như đối với trái phiếu chiết khấu, trước tiên chúng ta phải tính giá trị tương lai ($\text{FV}$) sau hai năm bao gồm mức giá tương lai là $93,091$ và tất cả các dòng tiền được tái đầu tư tính đến ngày đó:

$$\begin{aligned}
\text{FV}_2 &= \text{PMT}_1(1 + r) + \text{PMT}_2 + \text{PV}_2 \\
\text{FV}_2 &= 97,13 = 2 \times (1,02) + 2 + 93,091
\end{aligned}$$

![](assets/Quantitative_method.pdf-0072-13.png)

$$r = -1,445\% = \left(\frac{97,13}{100}\right)^{\frac{1}{2}} - 1$$

<!-- Formula Text: r = − 1.445 %   =  ( 97.13 _ 100 ) 1 _ 2 − 1. -->

Tỷ suất sinh lợi quy đổi theo năm mang giá trị âm này là do khoản lỗ vốn $6,91\text{ EUR}$ ($= 100 - 93,091$) đã vượt quá tổng tiền lãi định kỳ cộng với tiền thu được từ tái đầu tư là $4,04\text{ EUR}$ ($= 2 \times (1,02) + 2$). Sự sụt giảm giá trái phiếu xuống mức $93,091\text{ EUR}$ vào năm 2022 là kết quả của sự gia tăng lạm phát tại khu vực đồng Euro trong giai đoạn đó.

Đối với một nhà đầu tư mua trái phiếu coupon $2\%$ vào năm 2022 ở mức giá $93,091\text{ EUR}$, hãy nhớ lại rằng chúng ta đã giải tìm được $r$ (hay YTM) là $3,532\%$. Lưu ý rằng phép tính YTM này cho năm năm còn lại giả định tất cả các dòng tiền có thể được tái đầu tư ở mức $3,532\%$ cho đến khi đáo hạn. Mức lãi suất mà tại đó tiền lãi định kỳ có thể được tái đầu tư đóng vai trò then chốt đối với phép tính tỷ suất sinh lợi ngầm định cho các trái phiếu trả lãi định kỳ như được thể hiện dưới đây. YTM được tính toán với giả định rằng trái phiếu được nắm giữ cho đến khi đáo hạn.

<!-- PDF Page 73 -->

![](assets/Quantitative_method.pdf-0073-03.png)

<!-- Picture Text: 100<br>93.091<br>–1.445%<br>2 2 2 2 2 2 2<br>Years<br>1.0 2.0 3.0 4.0 5.0 6.0 7.0<br>3.532%<br>93.091<br>100<br> -->
> **Chú thích hình ảnh:** Trái phiếu trả coupon $2$ mỗi năm từ Năm $1,0$ đến Năm $7,0$. Trong 2 năm đầu (từ Năm 0 đến Năm $2,0$), giá giảm từ $100$ xuống $93,091$, tương ứng tỷ suất sinh lợi quy đổi theo năm là $-1,445\%$. Trong 5 năm cuối (từ Năm $2,0$ đến Năm $7,0$), giá tăng từ $93,091$ lên $100$ khi đáo hạn, tương ứng lợi suất đáo hạn YTM là $3,532\%$.

### **Công cụ Vốn chủ sở hữu, Tỷ suất sinh lợi ngầm định và Tốc độ tăng trưởng ngầm định (Equity Instruments, Implied Return, and Implied Growth)** 

Như đã lưu ý trong phần thảo luận về cách tính giá trị hiện tại của một khoản đầu tư vốn chủ sở hữu, giá của một cổ phiếu phản ánh không chỉ tỷ suất sinh lợi yêu cầu mà còn cả tốc độ tăng trưởng của các dòng tiền. Nếu chúng ta bắt đầu với giả định cổ tức tăng trưởng không đổi từ Phương trình 14, chúng ta có thể sắp xếp lại công thức như sau:

![](assets/Quantitative_method.pdf-0073-06.png)

$$r - g = \frac{D_t(1 + g)}{\text{PV}_t} = \frac{D_{t+1}}{\text{PV}_t} \tag{20}$$

<!-- Formula Text: r − g = D t(1 + g) _ P V t    = D t+1 _ P V t . (20) -->

Vế trái của Phương trình 20 đơn giản phản ánh sự chênh lệch giữa tỷ suất sinh lợi yêu cầu và tốc độ tăng trưởng không đổi, còn vế phải là lợi suất cổ tức (*dividend yield*) của cổ phiếu dựa trên cổ tức dự kiến trong kỳ tiếp theo. Như vậy, tỷ suất sinh lợi ngầm định của một cổ phiếu khi biết lợi suất cổ tức dự kiến và tốc độ tăng trưởng của nó được cho bởi Phương trình 21 như sau:

![](assets/Quantitative_method.pdf-0073-08.png)

$$r = \frac{D_t(1 + g)}{\text{PV}_t} + g = \frac{D_{t+1}}{\text{PV}_t} + g \tag{21}$$

<!-- Formula Text: r = D t(1 + g) _ P V t   + g  = D t+1 _ P V t  + g. (21) -->

Nói một cách đơn giản, nếu chúng ta giả định rằng cổ tức của một cổ phiếu tăng trưởng với tốc độ không đổi đến vĩnh viễn, thì tỷ suất sinh lợi ngầm định của cổ phiếu đó bằng lợi suất cổ tức dự kiến cộng với tốc độ tăng trưởng không đổi.

Ngoài ra, chúng ta có thể quan tâm đến việc giải tìm tốc độ tăng trưởng ngầm định (*implied growth rate*) của một cổ phiếu, và mối quan hệ này được cho bởi Phương trình 22:

![](assets/Quantitative_method.pdf-0073-11.png)

$$g = \frac{r \times \text{PV}_t - D_t}{\text{PV}_t + D_t} = r - \frac{D_{t+1}}{\text{PV}_t} \tag{22}$$

<!-- Formula Text: g = r * P V t − D t _ P V t+ D t    =  r− D t+1 _ P V t . (22) -->

Nếu biết trước khoản cổ tức dự kiến tiếp theo của một cổ phiếu, thì chúng ta có thể tính tốc độ tăng trưởng ngầm định bằng cách lấy tỷ suất sinh lợi yêu cầu trừ đi lợi suất cổ tức dự kiến của nó.

<!-- PDF Page 74 -->

#### **VÍ DỤ 10 (EXAMPLE 10)** 

### **Tỷ suất sinh lợi ngầm định và Tốc độ tăng trưởng ngầm định của một Cổ phiếu (Implied Return and Growth for a Stock)** 

Cổ phiếu của Công ty Coca-Cola (*Coca-Cola Company*) đang giao dịch ở mức giá $63,00\text{ USD}$ một cổ phiếu và cổ tức dự kiến quy đổi theo năm trên mỗi cổ phiếu trong năm tới là $1,76\text{ USD}$.

1. Nếu một nhà phân tích kỳ vọng cổ tức trên mỗi cổ phiếu của Coca-Cola sẽ tăng với tốc độ không đổi $4\%$ mỗi năm vô thời hạn, hãy tính tỷ suất sinh lợi yêu cầu mà các nhà đầu tư kỳ vọng.

#### **Lời giải (Solution):** 

$6,79\%$

Sử dụng Phương trình 21:

![](assets/Quantitative_method.pdf-0074-09.png)

$$r = \frac{1,76}{63} + 0,04 = 0,0679$$

<!-- Formula Text: r  =   1.76 _ 63  + 0.04  =  0.0679. -->

Tỷ suất sinh lợi yêu cầu được kỳ vọng đối với cổ phiếu Coca-Cola là $6,79\%$ khi biết giá hiện hành, cổ tức dự kiến và tốc độ tăng trưởng cổ tức dự kiến của nó. Kỳ vọng của nhà đầu tư về tỷ suất sinh lợi cổ phiếu trong tương lai được suy ra từ sự kết hợp giữa mức giá hiện hành, các dòng tiền dự kiến trong tương lai và tốc độ tăng trưởng dòng tiền. Giả sử rằng, thay vì cố gắng ước tính tỷ suất sinh lợi yêu cầu, một nhà đầu tư lại muốn xác định tốc độ tăng trưởng cổ tức ngầm định. Trong trường hợp này, nhà đầu tư phải giả định một mức tỷ suất sinh lợi cổ phiếu trong tương lai, như trong câu hỏi 2.

2. Nếu nhà phân tích tin rằng các nhà đầu tư cổ phiếu Coca-Cola nên kỳ vọng một mức tỷ suất sinh lợi là $7\%$, hãy tính tốc độ tăng trưởng cổ tức ngầm định cho Coca-Cola.

#### **Lời giải (Solution):** 

$4,21\%$

Sử dụng Phương trình 22:

![](assets/Quantitative_method.pdf-0074-14.png)

$$g = 0,07 - \frac{1,76}{63} = 0,0421$$

<!-- Formula Text: g  =  0.07−  1.76 _ 63  = 0.0421. -->

Tốc độ tăng trưởng cổ tức ngầm định của cổ phiếu Coca-Cola là $4,21\%$ khi biết tỷ suất sinh lợi kỳ vọng, mức giá và cổ tức dự kiến của nó. Do một mức tỷ suất sinh lợi kỳ vọng cao hơn được giả định trong câu hỏi này so với trường hợp ở câu hỏi 1, nên kết quả dẫn đến một tốc độ tăng trưởng cổ tức ngầm định cao hơn để biện minh cho mức giá cổ phiếu $63,00\text{ USD}$ của Coca-Cola.

Thay vì so sánh trực tiếp giá cổ phiếu tính theo đơn vị tiền tệ, một thông lệ phổ biến là so sánh tỷ số giữa giá cổ phiếu trên thu nhập mỗi cổ phiếu, hay **hệ số giá trên thu nhập (*price-to-earnings ratio – P/E*)**.

#### **HỆ SỐ GIÁ TRÊN THU NHẬP (PRICE-TO-EARNINGS RATIO)** 

Hệ số giá trên thu nhập (*price-to-earnings ratio*) là một thước đo định giá tương đối (*relative valuation metric*) giúp cải thiện khả năng so sánh bằng cách kiểm soát một yếu tố dẫn dắt giá trị đã biết (thu nhập trên mỗi cổ phiếu – *earnings per share*) cũng như đơn vị tiền tệ. Nó tương tự như việc biểu thị giá bất động sản bằng đơn giá trên mỗi mét vuông.

Một cổ phiếu đang giao dịch ở hệ số giá trên thu nhập (P/E) bằng 20 hàm ý rằng giá cổ phiếu của nó gấp 20 lần thu nhập trên mỗi cổ phiếu và các nhà đầu tư sẵn sàng trả gấp 20 lần thu nhập trên mỗi cổ phiếu cho mỗi cổ phiếu được giao dịch, tức là đắt hơn so với một cổ phiếu đang giao dịch ở hệ số giá trên thu nhập bằng 10.

<!-- PDF Page 75 -->

Hệ số giá trên thu nhập không chỉ được sử dụng cho các cổ phiếu riêng lẻ mà còn là một thước đo định giá cho các chỉ số chứng khoán, chẳng hạn như S&P 500, FTSE 100, hoặc Nikkei 225. Tại đây, giá trị chỉ số chứng khoán được chia cho tổng có trọng số của thu nhập trên mỗi cổ phiếu của các công ty thành phần trong chỉ số. Nội dung này sẽ được khám phá sâu hơn ở phần sau của chương trình học, nhưng chúng ta có thể liên hệ hệ số giá trên thu nhập với phần thảo luận trước đó về việc gắn kết giá cổ phiếu ($\text{PV}$) với các dòng tiền dự kiến trong tương lai để rút ra một số nhận xét hữu ích. Trước hết, hãy nhớ lại Phương trình 14:

![](assets/Quantitative_method.pdf-0075-04.png)

$$\text{PV}_t = \frac{D_t(1 + g)}{r - g}$$

<!-- Formula Text: P V t = D t(1 + g) _ r − g  . -->

Chúng ta có thể chia cả hai vế cho $E_t$, thu nhập trên mỗi cổ phiếu (*earnings per share*) của kỳ $t$, để thu được:

![](assets/Quantitative_method.pdf-0075-06.png)

$$\frac{\text{PV}_t}{E_t} = \frac{D_t}{E_t} \times \frac{(1 + g)}{r - g} \tag{23}$$

<!-- Formula Text: P V t _ E t  = D t _ E t  × (1 + g) _ r− g . (23) -->

Vế trái của Phương trình 23 là hệ số giá trên thu nhập (P/E hiện tại – *trailing P/E*), trong khi thừa số đầu tiên ở tử số bên vế phải là tỷ trọng thu nhập được phân phối cho các cổ đông dưới dạng cổ tức, được gọi là **tỷ lệ chi trả cổ tức (*dividend payout ratio*)**.

Khi biết hệ số giá trên thu nhập và tỷ lệ chi trả cổ tức, chúng ta có thể giải tìm tỷ suất sinh lợi yêu cầu hoặc tốc độ tăng trưởng cổ tức ngầm định (khi có giả định về đại lượng còn lại). Tỷ suất sinh lợi yêu cầu rất hữu ích trong việc tìm hiểu kỳ vọng sinh lợi của nhà đầu tư trên cơ sở hướng tới tương lai (*forward-looking basis*). Tốc độ tăng trưởng không đổi ngầm định lại hữu ích để so sánh với tốc độ tăng trưởng dự kiến và tốc độ tăng trưởng lịch sử của công ty. Ví dụ, nếu tốc độ tăng trưởng không đổi ngầm định là $10\%$ nhưng nhà phân tích ước tính rằng công ty chỉ có thể tăng trưởng ở mức $5\%$, nhà phân tích có thể đánh giá rằng cổ phiếu đó đang bị định giá quá cao (*overvalued*).

Trên thực tế, **hệ số giá trên thu nhập dự phóng (*forward price-to-earnings ratio – forward P/E*)**, hay tỷ số giữa giá cổ phiếu trên mức ước tính thu nhập mỗi cổ phiếu của kỳ tiếp theo ($t + 1$), thường được sử dụng phổ biến. Với hệ số này, chúng ta có thể rút gọn phương trình trước đó như sau:

![](assets/Quantitative_method.pdf-0075-10.png)

$$\frac{\text{PV}_t}{E_{t+1}} = \frac{D_{t+1} / E_{t+1}}{r - g} \tag{24}$$

<!-- Formula Text: P V t _ E t+1  = D t+1 _ E t+1 _ r− g . (24) -->

Từ Phương trình 24, chúng ta có thể thấy rằng hệ số giá trên thu nhập dự phóng có mối quan hệ đồng biến (*positively related*) với tỷ lệ chi trả cổ tức dự kiến cao hơn và tốc độ tăng trưởng dự kiến cao hơn, nhưng có mối quan hệ nghịch biến (*negatively related*) với tỷ suất sinh lợi yêu cầu.

#### **VÍ DỤ 11 (EXAMPLE 11)** 

### **Tỷ suất sinh lợi ngầm định và Tốc độ tăng trưởng ngầm định từ Hệ số Giá trên Thu nhập (Implied Return and Growth from Price to Earnings Ratio)** 

1. Giả sử cổ phiếu Coca-Cola giao dịch ở hệ số giá trên thu nhập dự phóng (*forward P/E*) là 28, tỷ lệ chi trả cổ tức dự kiến của nó là $70\%$, và các nhà phân tích tin rằng cổ tức của công ty sẽ tăng trưởng với tốc độ không đổi là $4\%$ mỗi năm. Hãy tính tỷ suất sinh lợi yêu cầu của Coca-Cola.

**Lời giải (Solution):** 

$6,50\%$

Sử dụng Phương trình 24:

![](assets/Quantitative_method.pdf-0075-17.png)

$$28 = \frac{0,7}{r - 0,04}$$

<!-- Formula Text: 28 =   0.7 _ r − 0.04 . -->

Giải phương trình này để tìm $r$, tỷ suất sinh lợi yêu cầu của Coca-Cola là $6,50\%$. Từ kết quả trên cho tỷ suất sinh lợi yêu cầu của Coca-Cola, không có gì đáng ngạc nhiên khi nếu thay vào đó chúng ta giả định rằng tỷ suất sinh lợi yêu cầu đối với cổ phiếu Coca-Cola là $6,50\%$, thì chúng ta sẽ tìm ra tốc độ tăng trưởng ngầm định của Coca-Cola là $4\%$, và kết quả này được xác nhận trong câu hỏi 2.

<!-- PDF Page 76 -->

2. Giả sử cổ phiếu Coca-Cola giao dịch ở hệ số giá trên thu nhập dự phóng là 28, tỷ lệ chi trả cổ tức dự kiến của nó là $70\%$, và các nhà phân tích tin rằng tỷ suất sinh lợi yêu cầu của nó là $6,50\%$. Hãy tính tốc độ tăng trưởng ngầm định của Coca-Cola.

#### **Lời giải (Solution):** 

$4,00\%$

Sử dụng Phương trình 24:

$$28 = \frac{0,70}{0,065 - g}$$

Giải phương trình này để tìm $g$, tốc độ tăng trưởng ngầm định của Coca-Cola là $4,00\%$. Cụ thể, tỷ suất sinh lợi của Coca-Cola được kỳ vọng sẽ cao hơn $2,5\%$ so với tốc độ tăng trưởng cổ tức của nó (tức là $6,50\% - 4,00\%$).

Như đã thảo luận trước đó, các nguyên lý tương tự cũng được áp dụng để tìm hiểu tỷ suất sinh lợi yêu cầu và tốc độ tăng trưởng của các chỉ số chứng khoán.

3. Một chỉ số chứng khoán đang giao dịch ở hệ số giá trên thu nhập dự phóng là 19. Nếu tỷ lệ chi trả cổ tức dự kiến của chỉ số là $60\%$, và các nhà đầu tư cổ phiếu kỳ vọng mức tỷ suất sinh lợi của chỉ số là $8\%$, hãy tính tốc độ tăng trưởng không đổi ngầm định cho chỉ số này.

**Lời giải (Solution):** 

$4,84\%$

Sử dụng Phương trình 24:

![](assets/Quantitative_method.pdf-0076-13.png)

$$19 = \frac{0,60}{0,08 - g}$$

<!-- Formula Text: 19 =   0.60 _ 0.08− g . -->

Giải tìm $g$, chúng ta thấy rằng các nhà đầu tư kỳ vọng tốc độ tăng trưởng cổ tức của chỉ số sẽ là $4,84\%$ trong tương lai. Ngược lại, chúng ta có thể giả định rằng các nhà đầu tư kỳ vọng tốc độ tăng trưởng là $4,84\%$ và giải tìm $r$ để tính ra mức tỷ suất sinh lợi yêu cầu là $8\%$. Do đó, hệ số giá trên thu nhập dự phóng của chỉ số là 19 và tỷ lệ chi trả cổ tức dự kiến là $60\%$ kết hợp lại để phản ánh kỳ vọng về mức tỷ suất sinh lợi $8\%$ và tốc độ tăng trưởng $4,84\%$. Cụ thể, tỷ suất sinh lợi yêu cầu vượt quá tốc độ tăng trưởng cổ tức ngầm định một mức là $3,16\%$ (tức là $8\% - 4,84\%$).

Một điểm quan trọng rút ra từ các kết quả trước là giá cổ phiếu, cho dù được biểu thị đơn giản dưới dạng mức giá hay dưới dạng hệ số giá trên thu nhập, đều phản ánh những kỳ vọng kết hợp về tỷ suất sinh lợi và tốc độ tăng trưởng trong tương lai. Kỳ vọng về tỷ suất sinh lợi và tốc độ tăng trưởng được liên kết chặt chẽ với nhau thông qua mức chênh lệch giữa $r$ và $g$. Ví dụ, trường hợp của Coca-Cola sử dụng hệ số giá trên thu nhập bằng 28 mô tả một tình huống trong đó các nhà đầu tư phải tin rằng tỷ suất sinh lợi yêu cầu đối với cổ phiếu Coca-Cola cao hơn $2,5\%$ so với tốc độ tăng trưởng của nó.

4. Giả sử cổ phiếu Coca-Cola giao dịch ở hệ số giá trên thu nhập dự phóng là 28 và tỷ lệ chi trả cổ tức dự kiến của nó là $70\%$. Các nhà phân tích tin rằng cổ phiếu Coca-Cola cần phải mang lại mức tỷ suất sinh lợi $9\%$ và cổ tức của nó sẽ tăng trưởng $4,50\%$ mỗi năm vô thời hạn. Hãy khuyến nghị một phương án hành động cho một nhà đầu tư đang quan tâm đến việc mở vị thế đối với cổ phiếu Coca-Cola.

#### **Lời giải (Solution):** 

Mở vị thế bán khống (*short position*) đối với cổ phiếu Coca-Cola. Nếu chúng ta đánh giá các tham số trên bằng cách sử dụng Phương trình 24, chúng ta có thể thấy rằng điều này dẫn đến một bất đẳng thức:
*(Xem tiếp phần lời giải ở đầu Phần 3/4)*


---

# Tập 1: Phương pháp Định lượng (Volume 1: Quantitative Methods)
## Học phần 2: Giá trị Thời gian của Tiền trong Tài chính (Learning Module 2: Time Value of Money in Finance)
### Phần 3/4: Tính cộng Dòng tiền (Cash Flow Additivity) (Trang PDF 77–91)

---

<!-- PDF Page 77 -->

$$28 > \frac{0,70}{0,09 - 0,045} = 15,56$$

Hệ số giá trên thu nhập dự phóng (*forward price-to-earnings ratio*) của Coca-Cola ở mức 28 lớn hơn nhiều so với con số $15,56$ được tính ra từ phương trình. Kỳ vọng của nhà đầu tư về tốc độ tăng trưởng dòng tiền và tỷ suất sinh lợi không nhất quán với hệ số giá trên thu nhập dự phóng của Coca-Cola. Cụ thể, nhà đầu tư nên cân nhắc mở một vị thế bán khống (*short position*) đối với cổ phiếu Coca-Cola với niềm tin rằng giá của nó sẽ giảm xuống bởi vì hệ số giá trên thu nhập hiện hành của nó cao hơn nhiều so với những gì các yếu tố cơ bản (*fundamentals*) hàm ý. Như đã trình bày trong kết quả của câu hỏi 1 và 2 ở ví dụ này, kỳ vọng về tỷ suất sinh lợi yêu cầu và tốc độ tăng trưởng phải sao cho $r - g = 2,50\%$ thì mới biện minh được cho hệ số giá trên thu nhập dự phóng bằng 28 khi tỷ lệ chi trả cổ tức dự kiến là $70\%$.

## **TÍNH CỘNG DÒNG TIỀN (CASH FLOW ADDITIVITY)** 

**<mark>4</mark>** 

giải thích nguyên lý cộng dòng tiền (*cash flow additivity principle*), tầm quan trọng của nó đối với điều kiện không có kinh doanh chênh lệch giá (*no-arbitrage condition*), và ứng dụng của nó trong việc tính toán lãi suất kỳ hạn ngầm định (*implied forward interest rates*), tỷ giá hối đoái kỳ hạn (*forward exchange rates*) và giá trị quyền chọn (*option values*)

Sự đánh đổi về giá trị thời gian của tiền giữa các dòng tiền phát sinh ngày hôm nay so với những dòng tiền trong tương lai có thể được mở rộng vượt ra ngoài việc định giá các dòng tiền tương lai ở thời điểm hiện tại hoặc tính toán tỷ suất sinh lợi ngầm định trên một công cụ đơn lẻ bằng cách sử dụng **nguyên lý cộng dòng tiền (*cash flow additivity principle*)**. Theo nguyên lý cộng dòng tiền, giá trị hiện tại của bất kỳ chuỗi dòng tiền tương lai nào được đánh chỉ số tại cùng một thời điểm đều bằng tổng giá trị hiện tại của từng dòng tiền thành phần. Nguyên lý này rất quan trọng trong việc đảm bảo rằng giá thị trường phản ánh điều kiện không có kinh doanh chênh lệch giá (*no arbitrage*), hay nói cách khác là không tồn tại khả năng kiếm được lợi nhuận phi rủi ro (*riskless profit*) khi không có chi phí giao dịch. Hãy bắt đầu với một ví dụ cơ bản để minh họa nguyên lý cộng dòng tiền.

#### **VÍ DỤ 12 (EXAMPLE 12)** 

### **Tính cộng Dòng tiền Cơ bản (Basic Cash Flow Additivity)** 

Giả sử bạn có $100\text{ GBP}$ để đầu tư và có hai chiến lược để lựa chọn với các chuỗi dòng tiền tương ứng như được thể hiện trong Bảng 9 (*Exhibit 9*).

<!-- PDF Page 78 -->

#### **Bảng 9: Hai Chiến lược Đầu tư (Exhibit 9: Two Investment Strategies)** 

![](assets/Quantitative_method.pdf-0078-04.png)

<!-- Picture Text: Time<br>t =0 t =1 t =2 t =3<br>Strategy 1.)<br>GBP100 CF(1)1: GBP45 CF(1)2: GBP45 CF(1)3: GBP45<br>Strategy 2.)<br>GBP100 CF(2)1: GBP60 CF(2)2: GBP40 CF(2)3: GBP32.35<br> -->
> **Chú thích hình ảnh:**
> - **Chiến lược 1 (*Strategy 1*):** Đầu tư $100\text{ GBP}$ tại $t=0$; nhận các dòng tiền $CF(1)_1 = 45\text{ GBP}$ tại $t=1$, $CF(1)_2 = 45\text{ GBP}$ tại $t=2$, $CF(1)_3 = 45\text{ GBP}$ tại $t=3$.
> - **Chiến lược 2 (*Strategy 2*):** Đầu tư $100\text{ GBP}$ tại $t=0$; nhận các dòng tiền $CF(2)_1 = 60\text{ GBP}$ tại $t=1$, $CF(2)_2 = 40\text{ GBP}$ tại $t=2$, $CF(2)_3 = 32,35\text{ GBP}$ tại $t=3$.

Tỷ suất sinh lợi yêu cầu của bạn đối với cả hai chiến lược đầu tư là $10\%$ mỗi kỳ.

1. Khuyến nghị nên lựa chọn chiến lược đầu tư nào.

#### **Lời giải (Solution):** 

Để đưa ra khuyến nghị giữa hai chiến lược này, chúng ta cần xác định xem chiến lược nào có giá trị hiện tại cao hơn cũng như liệu có chiến lược nào mang lại giá trị hiện tại ròng dương hay không. Để đạt được các mục tiêu này, trước tiên chúng ta có thể tính giá trị hiện tại của cả hai chiến lược và đảm bảo rằng ít nhất một chiến lược có giá trị hiện tại dương bên cạnh việc so sánh giá trị hiện tại của hai chiến lược với nhau. Ngoài ra, chúng ta có thể tính mức chênh lệch giữa các dòng tiền tại mỗi kỳ để tạo ra một tập hợp các dòng tiền mới. Cả hai quy trình giải đều phải cho ra một kết quả số học tương đương khi so sánh hai chiến lược, và sự tương đương về mặt số học này thể hiện nguyên lý cộng dòng tiền. Trước hết, hãy tạo tập hợp các dòng tiền từ hiệu số của hai chiến lược như được thể hiện trong sơ đồ sau:

![](assets/Quantitative_method.pdf-0078-09.png)

<!-- Picture Text: Time<br>t =0 t =1 t =2 t =3<br>Strategy 2.)  –  Strategy 1.)<br>CF(2-1)1: GBP0<br>CF(2-1)1: GBP15<br>CF(2-1)2: (GBP5)<br>CF(2-1)3: (GBP12.65)<br>GBP100<br> -->
> **Chú thích hình ảnh (Chiến lược 2 – Chiến lược 1):** Dòng tiền chênh lệch tại $t=0$ là $0\text{ GBP}$; tại $t=1$ là $+15\text{ GBP}$; tại $t=2$ là $-5\text{ GBP}$; tại $t=3$ là $-12,65\text{ GBP}$.

![](assets/Quantitative_method.pdf-0078-10.png)

Giá trị hiện tại của các dòng tiền ròng chênh lệch này bằng không, cho thấy sự tương đương nhau, như sau:

$$\text{PV} = 0 + \frac{15}{1,10} + \frac{-5}{(1,10)^2} + \frac{-12,65}{(1,10)^3} = 0$$

<!-- Formula Text: The present value of these net cash flows is zero, indicating equivalence, as follows: PV = 0+  15 _ 1.10 +   − 5 _ (1.10) 2 +  − 12, 65 _ (1.10) 3   =  0. -->

Kết luận rút ra từ phân tích này là hai chiến lược tương đương nhau về mặt kinh tế (*economically equivalent*); do đó bạn không nên có sự ưu tiên nào cho chiến lược này hơn chiến lược kia. Chúng ta cũng phải xác định xem liệu các chiến lược này có mang lại giá trị kinh tế hay không. Để làm điều đó, hãy tính giá trị hiện tại ròng của từng chiến lược riêng lẻ.

<!-- PDF Page 79 -->

![](assets/Quantitative_method.pdf-0079-03.png)

Đối với chiến lược đầu tư 1, giá trị hiện tại ròng là $11,91\text{ GBP}$, như sau:

$$\text{PV} = -100 + \frac{45}{1,10} + \frac{45}{(1,10)^2} + \frac{45}{(1,10)^3} = 11,91$$

Đối với chiến lược đầu tư 2, giá trị hiện tại ròng cũng là $11,91\text{ GBP}$, như sau:

$$\text{PV} = -100 + \frac{60}{1,10} + \frac{40}{(1,10)^2} + \frac{32,35}{(1,10)^3} = 11,91$$

<!-- Formula Text: For investment strategy 1, the present value is GBP11.91, as follows: PV = − 100+  45 _ 1.10 +   45 _ (1.10) 2 +   45 _ (1.10) 3   =  11.91. For investment strategy 2, the present value is also GBP11.91, as follows: PV = − 100+  60 _ 1.10 +   40 _ (1.10) 2 +  32.35 _ (1.10) 3   =  11.91. -->

Cả hai chiến lược đầu tư đều có giá trị ở chỗ giá trị hiện tại của tổng các dòng tiền của chúng đều mang dấu dương. Vì các giá trị hiện tại giống hệt nhau, nên việc lấy giá trị hiện tại của chiến lược 2 trừ đi giá trị hiện tại của chiến lược 1 sẽ bằng không (tức là $11,91 - 11,91$). Khuyến nghị có thể chọn bất kỳ chiến lược nào vì cả hai đều mang lại giá trị kinh tế và có giá trị hiện tại bằng nhau.

Trong các mục tiếp theo, chúng ta áp dụng nguyên lý cộng dòng tiền vào ba tình huống kinh tế khác nhau và minh họa sâu hơn về nguyên lý không có kinh doanh chênh lệch giá (*no arbitrage*) bằng cách so sánh hai chiến lược tương đương nhau về mặt kinh tế trong từng tình huống.

### **Lãi suất kỳ hạn ngầm định sử dụng Tính cộng Dòng tiền (Implied Forward Rates Using Cash Flow Additivity)** 

Xét hai trái phiếu chiết khấu phi rủi ro có kỳ hạn khác nhau như sau:

- Trái phiếu kỳ hạn một năm: $r_1 = 2,50\%$

- Trái phiếu kỳ hạn hai năm: $r_2 = 3,50\%$

Một nhà đầu tư trung lập với rủi ro (*risk-neutral investor*) đang tìm cách kiếm tỷ suất sinh lợi trên $100\text{ GBP}$ trong khung thời gian đầu tư hai năm có hai chiến lược khả thi:

- _Chiến lược đầu tư 1:_ Đầu tư ngay hôm nay trong hai năm ở mức lợi suất quy đổi theo năm đã biết là $3,50\%$. Sử dụng Phương trình 5, chúng ta có thể giải tìm giá trị tương lai sau hai năm ($\text{FV}_2$) như sau:

$$\begin{aligned}
\text{100 GBP} &= \text{FV}_2 / (1 + r_2)^2 \\
\text{FV}_2 &= \text{107,12 GBP}
\end{aligned}$$

- _Chiến lược đầu tư 2:_ Đầu tư ngay hôm nay trong một năm ở mức lợi suất đã biết là $2,50\%$ và tái đầu tư vào thời điểm một năm sau cho kỳ hạn một năm tiếp theo ở mức lãi suất $F_{1,1}$ (lãi suất kỳ hạn một năm bắt đầu sau một năm – *one-year forward rate starting in one year*).

Hai chiến lược này được tóm tắt trong Bảng 10 (*Exhibit 10*):

<!-- PDF Page 80 -->

#### **Bảng 10: Ví dụ về Lãi suất kỳ hạn ngầm định (Exhibit 10: Implied Forward Rate Example)** 

![](assets/Quantitative_method.pdf-0080-04.png)

<!-- Picture Text: Time<br>t =0 t =1 t =2<br>Strategy 1.)<br>1-year rate Implied forward rate F1,1<br>GBP100<br>GBP102.5 GBP102.5(1+ F 1,1)<br>GBP100(1+r1)<br>Strategy 2.)<br>2-year rate<br>GBP100<br>GBP107.12<br>GBP100(1+r2) 2<br> -->
> **Chú thích hình ảnh:**
> - Nhánh trên: Đầu tư $100\text{ GBP}$ tại $t=0$ theo lãi suất 1 năm ($r_1$) để có $100(1+r_1) = 102,5\text{ GBP}$ tại $t=1$, sau đó tái đầu tư theo lãi suất kỳ hạn ngầm định $F_{1,1}$ để nhận $102,5(1+F_{1,1})$ tại $t=2$.
> - Nhánh dưới: Đầu tư $100\text{ GBP}$ tại $t=0$ theo lãi suất 2 năm ($r_2$) để nhận $100(1+r_2)^2 = 107,12\text{ GBP}$ tại $t=2$.

Theo nguyên lý cộng dòng tiền, một nhà đầu tư trung lập với rủi ro sẽ bàng quan (*indifferent*) giữa chiến lược 1 và chiến lược 2 dưới điều kiện sau đây:

$$\text{FV}_2 = \text{PV}_0 \times (1 + r_2)^2 = \text{PV}_0 \times (1 + r_1)(1 + F_{1,1}) \tag{25}$$

$$\text{107,12 GBP} = \text{100 GBP}(1,025)(1 + F_{1,1})$$

và

$$F_{1,1} = 4,51\%$$

Chúng ta có thể sắp xếp lại Phương trình 25 để giải tìm $F_{1,1}$ một cách tổng quát như sau:

$$F_{1,1} = \frac{(1 + r_2)^2}{(1 + r_1)} - 1$$

Để minh họa lý do tại sao lãi suất kỳ hạn một năm phải bằng $4,51\%$, hãy giả sử một nhà đầu tư có thể khóa chặt (*lock in*) mức lãi suất một năm là $5\%$ bắt đầu sau một năm. Chiến lược kinh doanh chênh lệch giá (*arbitrage strategy*) sau đây sẽ tạo ra một khoản lợi nhuận phi rủi ro:

**1.** Vay $100\text{ GBP}$ trong hai năm với lãi suất $3,50\%$ và đồng ý trả $107,12\text{ GBP}$ sau hai năm.

**2.** Đầu tư $100\text{ GBP}$ trong năm thứ nhất với lãi suất $2,50\%$ và trong năm thứ hai với lãi suất $5\%$, nhờ đó nhận được $107,63\text{ GBP}$ sau hai năm.

**3.** Sự kết hợp của hai chiến lược trên mang lại khoản lợi nhuận phi rủi ro là $0,51\text{ GBP}$ sau hai năm với số vốn đầu tư ban đầu bằng không.

Tập hợp các chiến lược này minh họa rằng lãi suất kỳ hạn phải được thiết lập sao cho các nhà đầu tư không thể kiếm được lợi nhuận kinh doanh chênh lệch giá phi rủi ro trên các thị trường tài chính. Điều này được chứng minh bằng cách so sánh hai chiến lược tương đương nhau về mặt kinh tế (tức là vay trong hai năm ở mức lãi suất hai năm so với vay qua hai kỳ hạn một năm liên tiếp ở hai mức lãi suất khác nhau). Lãi suất kỳ hạn $F_{1,1}$ có thể được diễn giải là lãi suất tái đầu tư hòa vốn kỳ hạn một năm (*breakeven one-year reinvestment rate*) vào thời điểm một năm sau.

<!-- PDF Page 81 -->

#### **VÍ DỤ 13 (EXAMPLE 13)** 

### **Những thay đổi trong Lãi suất kỳ hạn (Forward Interest Rate Changes)** 

Tại cuộc họp tháng 6 năm 2022, Cục Dự trữ Liên bang Hoa Kỳ (Fed) đã gây bất ngờ cho thị trường khi nâng lãi suất mục tiêu thêm 75 điểm cơ bản (bps) — cao hơn mức dự kiến — và gợi ý về các đợt tăng lãi suất tiếp theo trong tương lai nhằm ứng phó với mức lạm phát tăng vọt. Bảng 11 (*Exhibit 11*) cho thấy giá trái phiếu Kho bạc Hoa Kỳ tách lãi (*US Treasury strip*) kỳ hạn một năm và hai năm trên mỗi $100\text{ USD}$ mệnh giá vào cuối tháng 5 năm 2022 và sau quyết định của Fed vào tháng 6:

**Bảng 11: Giá Trái phiếu Kho bạc Hoa Kỳ Tách lãi Kỳ hạn Một năm và Hai năm (Exhibit 11: One- and Two-Year US Treasury Strip Prices)** 

|**Ngày (Date)**|**$\text{PV}(1y)$**|**$\text{PV}(2y)$**|
|---|---|---|
|31 tháng 5 năm 2022|98,028|95,109|
|15 tháng 6 năm 2022|97,402|93,937|

1. Sử dụng thông tin trong Bảng 11, hãy tính mức thay đổi trong lãi suất tái đầu tư hòa vốn kỳ hạn một năm bắt đầu sau một năm ($F_{1,1}$).

#### **Lời giải (Solution):** 

62 bps hay $0,62\%$

Trước hết, chúng ta sử dụng Phương trình 18 để giải tìm từng mức lãi suất chiết khấu thị trường $r$. Ví dụ, trong trường hợp trái phiếu chiết khấu kỳ hạn hai năm vào ngày 15 tháng 6:

![](assets/Quantitative_method.pdf-0081-12.png)

$$r = 3,177\% = \left(\frac{100}{93,937}\right)^{\frac{1}{2}} - 1$$

<!-- Formula Text: r = 3.177 percent  =  (  100 _ 93.937 ) 1 _ 2 − 1. -->

Bảng sau đây tóm tắt các mức lãi suất trái phiếu chiết khấu tương ứng:

|**Ngày (Date)**|**$r_1$**|**$r_2$**|
|---|---|---|
|31 tháng 5 năm 2022|2,012%|2,539%|
|15 tháng 6 năm 2022|2,667%|3,177%|

Giải tìm các mức lãi suất kỳ hạn tương ứng ($F_{1,1}$) bằng cách sắp xếp lại Phương trình 25: $F_{1,1} = (1 + r_2)^2 / (1 + r_1) - 1$.

- **$\underline{F_{1,1}\text{ (31 tháng 5):}}$** $F_{1,1} = 3,069\% = (1 + 2,539\%)^2 / (1 + 2,012\%) - 1$.
- **$\underline{F_{1,1}\text{ (15 tháng 6):}}$** $F_{1,1} = 3,689\% = (1 + 3,177\%)^2 / (1 + 2,667\%) - 1$.

Trong khi mức $r_1$ và $r_2$ cao hơn vào giữa tháng 6 cho thấy các nhà đầu tư đã phản ánh đợt tăng 75 bps tức thời vào lãi suất chiết khấu danh nghĩa của họ, thì mức tăng 62 bps ($0,62\% = 3,689\% - 3,069\%$) của $F_{1,1}$ là thước đo phản ánh các đợt tăng lãi suất dự kiến trong tương lai do lãi suất danh nghĩa kỳ hạn một năm này bắt đầu sau một năm nữa. Cũng cần lưu ý rằng trong môi trường lãi suất đang tăng lên, $F_{1,1} > r_2$, như được thể hiện trong sơ đồ sau đây so sánh $r_1$, $r_2$ và $F_{1,1}$ vào ngày 31 tháng 5 (lãi suất thấp hơn) với ngày 15 tháng 6 (lãi suất cao hơn).

<!-- PDF Page 82 -->

![](assets/Quantitative_method.pdf-0082-03.png)

<!-- Picture Text: Yield (%)<br>4.00%<br>F1,1<br>r2<br>3.00%<br>r1 F1,1<br>r2<br>2.00%<br>r1<br>1.00% Term<br>1 2 3<br> -->
> **Chú thích hình ảnh:** Trục tung biểu diễn Lợi suất (*Yield (%)*) từ $1,00\%$ đến $4,00\%$; trục hoành biểu diễn Kỳ hạn (*Term*). Đường thấp hơn (ngày 31/5) và đường cao hơn (ngày 15/6) đều dốc lên với $r_1 < r_2 < F_{1,1}$.

### **Tỷ giá hối đoái kỳ hạn sử dụng Nguyên lý Không có Kinh doanh Chênh lệch giá (Forward Exchange Rates Using No Arbitrage)** 

Bây giờ chúng ta mở rộng nguyên lý cộng dòng tiền sang một kịch bản kinh tế liên quan đến các đồng tiền khác nhau.

Giả sử bạn có $1.000\text{ USD}$ để đầu tư trong sáu tháng. Bạn đang cân nhắc một khoản đầu tư phi rủi ro vào nợ chính phủ kỳ hạn sáu tháng của Hoa Kỳ hoặc của Nhật Bản. Giả sử tỷ giá hối đoái hiện hành (tỷ giá giao ngay – *spot exchange rate*) giữa đồng yên Nhật (JPY) và đồng đô la Mỹ (USD) là $134,40$ (tức là $134,40\text{ JPY} = 1\text{ USD}$). Lãi suất phi rủi ro kỳ hạn sáu tháng của đồng yên Nhật được giả định là $0,05\%$ (quy đổi theo năm), và lãi suất phi rủi ro kỳ hạn sáu tháng của đồng đô la Mỹ là $2,00\%$ (quy đổi theo năm). Ví dụ này giả định ghép lãi liên tục (*continuous compounding*).

- _Chiến lược đầu tư 1:_ Đầu tư $1.000\text{ USD}$ vào tín phiếu Kho bạc Hoa Kỳ kỳ hạn sáu tháng.
  - Tại thời điểm $t = 0$: Đầu tư $1.000\text{ USD}$ ở mức lãi suất phi rủi ro đồng đô la Mỹ là $2,00\%$ trong sáu tháng.
  - Tại thời điểm $t = T$ sau sáu tháng: Nhận về $1.010,05\text{ USD}$ ($= 1.000e^{(0,02 \times 0,5)}$).

- _Chiến lược đầu tư 2:_ Chuyển đổi $1.000\text{ USD}$ sang đồng yên Nhật theo tỷ giá hối đoái hiện hành là $134,40$, đầu tư vào tín phiếu Kho bạc Nhật Bản kỳ hạn sáu tháng, và chuyển đổi số tiền đã biết trước này trở lại sang đồng đô la Mỹ sau sáu tháng theo tỷ giá hối đoái kỳ hạn sáu tháng (*six-month forward exchange rate*) được thiết lập ngay hôm nay là $133,096$.
  - Tại thời điểm $t = 0$: Chuyển đổi $1.000\text{ USD}$ thành $134.400\text{ JPY}$. Cho vay $134.400\text{ JPY}$ ở mức lãi suất phi rủi ro đồng JPY là $0,05\%$ trong sáu tháng.
  - Tại thời điểm $t = T$ sau sáu tháng: Nhận về số tiền thu hồi khoản vay bằng đồng JPY là $134.433,60\text{ JPY}$ ($= 134.400e^{(0,0005 \times 0,5)}$). Đổi số tiền thu hồi khoản vay bằng đồng JPY sang đô la Mỹ theo tỷ giá kỳ hạn là $133,096$ để nhận về $1.010,05\text{ USD}$ ($= 134.433,60 / 133,096$).

Hai chiến lược này tương đương nhau về mặt kinh tế ở chỗ cả hai đều liên quan đến việc đầu tư $1.000\text{ USD}$ tại $t = 0$ và nhận về $1.010,05\text{ USD}$ sau sáu tháng. Yếu tố liên kết hai chiến lược này lại với nhau chính là tỷ giá hối đoái kỳ hạn sáu tháng ở mức $133,096\text{ JPY/USD}$. Nếu tỷ giá kỳ hạn này được thiết lập cao hơn hoặc thấp hơn mức $133,096$, một cơ hội kinh doanh chênh lệch giá sẽ xuất hiện cho các nhà đầu tư thực hiện chuyển đổi qua lại giữa đồng yên Nhật và đồng đô la Mỹ. Bảng 12 (*Exhibit 12*) cung cấp sơ đồ trực quan của hai chiến lược này.

<!-- PDF Page 83 -->

#### **Bảng 12: Điều kiện Không có Kinh doanh Chênh lệch giá trên Thị trường Ngoại hối (Exhibit 12: No-Arbitrage Condition in the Foreign Exchange Market)** 

![](assets/Quantitative_method.pdf-0083-04.png)

<!-- Picture Text: Investment Lend USD1,000 at<br>Strategy 1 USD1,000 rusd  = rd =2.00% Receive USD1,000e USD1,010.05 r d T<br>=1,000e (0.02 × 0.5)<br>Begin with<br>Time<br>USD1,000<br>t =0 t = 6 months<br>Investment Sell USD Receive<br>Strategy 2 USD1,000 USD[134,433.60 × 1/ F o,( f /d) ( T )]<br>which must = USD1,010.05<br>S o,( f /d) = 134.400 F o,( f /d) ( T ) = JPY134,433.60 = 133.096<br>USD1,010.05<br>Lend JPY134,400 at<br>Receive JPY134,400 rJPY  =  rf  = 0.05% Earn JPY134,400e JPY134,433.60 r f T<br>= 134,400e (0.0005 × 0.5)<br> -->
> **Chú thích hình ảnh:**
> - **Chiến lược đầu tư 1 (*Investment Strategy 1*):** Bắt đầu với $1.000\text{ USD}$ tại $t=0$, cho vay ở mức $r_{\text{USD}} = r_d = 2,00\%$, nhận về $1.000e^{r_d T} = 1.000e^{(0,02 \times 0,5)} = 1.010,05\text{ USD}$ tại $t = 6\text{ tháng}$.
> - **Chiến lược đầu tư 2 (*Investment Strategy 2*):** Bán $1.000\text{ USD}$ theo tỷ giá giao ngay $S_{0,(f/d)} = 134,400$ để nhận $134.400\text{ JPY}$; cho vay $134.400\text{ JPY}$ ở mức $r_{\text{JPY}} = r_f = 0,05\%$ để thu được $134.400e^{r_f T} = 134.433,60\text{ JPY}$ sau 6 tháng; chuyển đổi lại sang USD theo tỷ giá kỳ hạn $F_{0,(f/d)}(T) = \frac{134.433,60\text{ JPY}}{1.010,05\text{ USD}} = 133,096$.

#### **VÍ DỤ 14 (EXAMPLE 14)** 

### **Tỷ giá hối đoái kỳ hạn trong Môi trường Lãi suất Thay đổi (Foreign Exchange Forward Rates in a Changing Interest Rate Environment)** 

Các ngân hàng trung ương đã phản ứng khác nhau trước sự gia tăng đột biến của lạm phát trong năm 2022. Ví dụ, trong khi Fed nâng lãi suất thêm 75 bps lên mức $1,75\%$ vào giữa tháng 6, Ngân hàng Trung ương Anh (*Bank of England*) lại chọn cách tiếp cận từ từ hơn, chỉ nâng lãi suất chuẩn thêm 25 bps lên mức $1,25\%$. Bảng 13 (*Exhibit 13*) so sánh lãi suất trái phiếu Kho bạc Hoa Kỳ tách lãi kỳ hạn một năm ($r_{\text{USD}}$) từ ví dụ trước với lãi suất trái phiếu chính phủ Anh tách lãi (*UK gilt strip rates* – $r_{\text{GBP}}$) trong cùng khung thời gian:

#### **Bảng 13: So sánh Lãi suất Trái phiếu Chính phủ Tách lãi của Hoa Kỳ và Anh (Exhibit 13: Comparison of US Treasury Strip Rates)** 

|**Ngày (Date)**|**$r_{\text{USD}}$**|**$r_{\text{GBP}}$**|
|---|---|---|
|31 tháng 5 năm 2022|2,012%|1,291%|
|15 tháng 6 năm 2022|2,667%|1,562%|

1. Nếu chúng ta giả định tỷ giá giao ngay USD/GBP ở mức $1,2602$ (hay $1,2602\text{ USD}$ trên mỗi $1,00\text{ GBP}$) từ ngày 31 tháng 5 giữ nguyên không đổi, sự thay đổi trong lãi suất phi rủi ro của đồng đô la Mỹ so với đồng bảng Anh ảnh hưởng như thế nào đến tỷ giá kỳ hạn một năm USD/GBP?

#### **Lời giải (Solution):** 

Tỷ giá kỳ hạn không có kinh doanh chênh lệch giá USD/GBP tăng từ $1,2693$ lên $1,2742$. Giả sử một nhà đầu tư có $1.000\text{ GBP}$ để đầu tư trong một năm vào trái phiếu chiết khấu phi rủi ro bằng đồng bảng Anh hoặc bằng đồng đô la Mỹ. Số đô la Mỹ cần thiết để mua $1\text{ GBP}$ sau một năm phải có mức giá giao ngay bằng với giá trị tương lai đã chiết khấu.

**Tính đến ngày 31 tháng 5:**

<!-- PDF Page 84 -->

- _Chiến lược nội địa (Domestic Strategy):_ Đầu tư $1.000\text{ GBP}$ ở mức lãi suất phi rủi ro một năm của đồng bảng Anh là $1,291\%$ để nhận về $1.012,99\text{ GBP}$ ($= 1.000e^{(0,01291)}$) sau một năm.

- _Chiến lược nước ngoài (Foreign Strategy):_ Chuyển đổi $1.000\text{ GBP}$ theo tỷ giá $\text{USD/GBP} = 1,2602$ để nhận được $1.260,20\text{ USD}$, số tiền này được đầu tư ở mức lãi suất phi rủi ro một năm của đồng đô la Mỹ là $2,012\%$ sẽ tạo ra số tiền thu về là $1.285,81\text{ USD}$ ($= 1.260,20e^{(0,02012)}$) sau một năm.

Do đó, tỷ giá kỳ hạn không có kinh doanh chênh lệch giá USD/GBP tính đến ngày 31 tháng 5 bằng $1,2693$ ($= \text{1.285,81 USD} / \text{1.012,99 GBP}$).

**Tính đến ngày 15 tháng 6:**

- _Chiến lược nội địa (Domestic Strategy):_ Đầu tư $1.000\text{ GBP}$ ở mức lãi suất phi rủi ro một năm của đồng bảng Anh là $1,562\%$ để nhận về $1.015,74\text{ GBP}$ ($= 1.000e^{(0,01562)}$) sau một năm.

- _Chiến lược nước ngoài (Foreign Strategy):_ Chuyển đổi $1.000\text{ GBP}$ theo tỷ giá $1,2602$ để nhận được $1.260,20\text{ USD}$, số tiền này được đầu tư ở mức lãi suất phi rủi ro một năm của đồng đô la Mỹ là $2,667\%$ sẽ mang lại $1.294,26\text{ USD}$ ($= 1.260,20e^{(0,02667)}$) sau một năm.

Tỷ giá kỳ hạn không có kinh doanh chênh lệch giá USD/GBP tính đến ngày 15 tháng 6 bằng $1,2742$ ($= \text{1.294,26 USD} / \text{1.015,74 GBP}$).

Tính đến giữa tháng 6, một nhà đầu tư đồng ý đổi đô la Mỹ lấy bảng Anh sau một năm phải giao nhiều đô la Mỹ hơn ($1,2742$ so với $1,2693$) để đổi lấy $1\text{ GBP}$ so với trường hợp cùng hợp đồng đó được ký kết vào cuối tháng 5. Mức tăng lớn hơn của $r_{\text{USD}}$ làm nới rộng mức chênh lệch lãi suất ($r_{\text{USD}} - r_{\text{GBP}}$), khiến đồng đô la Mỹ giảm giá trên cơ sở kỳ hạn (*depreciate on a forward basis*) so với đồng bảng Anh trong giai đoạn đó. Nói cách khác, kỳ vọng về sự giảm giá của đồng đô la Mỹ trên cơ sở kỳ hạn so với đồng bảng Anh sẽ đòi hỏi mức lãi suất đồng đô la Mỹ cao hơn để thu hút các nhà đầu tư nắm giữ đồng đô la Mỹ so với đồng bảng Anh.

### **Định giá Quyền chọn sử dụng Tính cộng Dòng tiền (Option Pricing Using Cash Flow Additivity)** 

Giả sử một tài sản có mức giá hiện hành là 40 nhân dân tệ Trung Quốc (tức $40\text{ CNY}$). Tài sản này có rủi ro ở chỗ giá của nó có thể tăng $40\%$ lên mức $56\text{ CNY}$ trong kỳ tiếp theo hoặc có thể giảm $20\%$ xuống mức $32\text{ CNY}$ trong kỳ tiếp theo.

Một nhà đầu tư muốn bán một hợp đồng dựa trên tài sản đó, trong đó người mua hợp đồng có quyền, nhưng không có nghĩa vụ (*the right, but not obligation*), được mua tài sản nêu trên với giá $50\text{ CNY}$ vào cuối kỳ tiếp theo. Chúng ta có thể áp dụng nguyên lý cộng dòng tiền để thiết lập mức giá không có kinh doanh chênh lệch giá (*no-arbitrage pricing*) cho hợp đồng này.

Cây nhị thức (*binomial tree*) trong Bảng 14 (*Exhibit 14*) tóm tắt hai kết quả có thể xảy ra trong tương lai của tài sản:

<!-- PDF Page 85 -->

#### **Bảng 14: Cây nhị thức Một kỳ cho Giá của Tài sản (Exhibit 14: One-Period Binomial Tree for the Asset’s Price)** 

![](assets/Quantitative_method.pdf-0085-04.png)

<!-- Picture Text: S 1 u  = CNY56<br>S 0 = CNY40<br>S 1 d  = CNY32<br>0 time T  = 1<br> -->
> **Chú thích hình ảnh:** Tại thời điểm $0$, giá tài sản là $S_0 = 40\text{ CNY}$. Tại thời điểm $T = 1$, giá tăng lên $S_1^u = 56\text{ CNY}$ hoặc giảm xuống $S_1^d = 32\text{ CNY}$.

Giá trị hợp đồng dưới hai kịch bản như sau (được thể hiện trực quan trong Bảng 15):

- **Giá tăng (*Price Increase*):** Mức tăng $40\%$ dẫn đến giá trị hợp đồng là $6\text{ CNY}$ ($= \text{56 CNY} - \text{50 CNY}$), bởi vì người sở hữu hợp đồng sẽ chọn mua tài sản ở mức giá $50\text{ CNY}$ và có thể bán nó ở mức giá thị trường là $56\text{ CNY}$.

- **Giá giảm (*Price Decrease*):** Mức giảm $20\%$ dẫn đến giá trị hợp đồng bằng không ($0\text{ CNY}$), bởi vì người sở hữu hợp đồng sẽ chọn không mua tài sản ở mức giá $50\text{ CNY}$ khi giá thị trường chỉ là $32\text{ CNY}$.

#### **Bảng 15: Cây nhị thức Một kỳ cho Giá của Hợp đồng (Exhibit 15: One-Period Binomial Tree for the Contract’s Price)** 

![](assets/Quantitative_method.pdf-0085-09.png)

<!-- Picture Text: c 1 u  =  CNY6<br>c 0 = ?<br>c 1 d  =  CNY0<br>0 time T  = 1<br> -->
> **Chú thích hình ảnh:** Tại thời điểm $0$, giá hợp đồng là $c_0 = ?$. Tại thời điểm $T = 1$, giá trị hợp đồng là $c_1^u = 6\text{ CNY}$ (nếu giá tài sản tăng) hoặc $c_1^d = 0\text{ CNY}$ (nếu giá tài sản giảm).

Hãy xét vị thế của người bán hợp đồng như sau:

- Tại $t = 0$, giá trị hợp đồng là $c_0$.

- Tại $t = 1$, giá trị hợp đồng là $6\text{ CNY}$ (nếu tài sản cơ sở tăng lên $56\text{ CNY}$) hoặc $0\text{ CNY}$ (nếu cổ phiếu cơ sở giảm xuống $32\text{ CNY}$).

Giá trị hợp đồng ban đầu $c_0$ là chưa biết và có thể được xác định bằng cách sử dụng nguyên lý cộng dòng tiền và định giá không có kinh doanh chênh lệch giá. Nghĩa là, giá trị của hợp đồng và tài sản cơ sở trong từng kịch bản tương lai có thể được sử dụng để xây dựng một danh mục đầu tư phi rủi ro (*risk-free portfolio*), hay một danh mục đầu tư mà giá trị của nó là như nhau trong cả hai kịch bản. Ví dụ, giả sử tại $t = 0$, một nhà đầu tư tạo ra một danh mục trong đó bán một hợp đồng ở mức giá $c_0$ và mua $0,25$ đơn vị tài sản cơ sở. Danh mục này được gọi là danh mục mô phỏng (*replicating portfolio*) ở chỗ nó được thiết kế đặc biệt để tạo ra một chuỗi dòng tiền tương lai khớp với chuỗi dòng tiền của một tài sản phi rủi ro. Ký hiệu giá trị của danh mục là $V$ tại $t = 0$ và tại $t = 1$ dưới cả hai kịch bản tăng giá và giảm giá, chúng ta có:

- $V_0 = 0,25 \times 40 - c_0$,

- $V_1^u = 0,25 \times 56 - 6 = 8$, và

- $V_1^d = 0,25 \times 32 - 0 = 8$.

<!-- PDF Page 86 -->

Như có thể thấy, giá trị của danh mục mô phỏng bằng $8\text{ CNY}$ bất kể giá của tài sản tăng hay giảm. Chính vì điều này, danh mục đầu tư là phi rủi ro và có thể được chiết khấu như một tài sản phi rủi ro. Giá trị nhận về (*payoffs*) cho hai kịch bản này được thể hiện trong Bảng 16 (*Exhibit 16*).

#### **Bảng 16: Mô phỏng Quyền chọn Mua (Exhibit 16: Call Option Replication)** 

![](assets/Quantitative_method.pdf-0086-06.png)

<!-- Picture Text: 0.25S 1 u  –  c1 u<br>0.25S 0 –  c 0<br>0.25S 1 d  –  c1 d<br>0 time T  = 1<br> -->
> **Chú thích hình ảnh:** Tại thời điểm $0$, giá trị danh mục là $0,25S_0 - c_0$. Tại thời điểm $T = 1$, giá trị danh mục là $0,25S_1^u - c_1^u$ (nhánh trên) hoặc $0,25S_1^d - c_1^d$ (nhánh dưới).

Để giải tìm $c_0$, chúng ta cho giá trị hiện tại của danh mục mô phỏng ($0,25 \times 40 - c_0$) bằng với giá trị tương lai đã chiết khấu của khoản thu nhập phi rủi ro $8\text{ CNY}$ dưới mỗi kết quả giống như trong Phương trình 5. Giả sử lãi suất phi rủi ro $r$ là $5\%$:

![](assets/Quantitative_method.pdf-0086-08.png)

$$V_0 = 0,25S_0 - c_0$$

<!-- Formula Text: V0 = 0.25S0 − c0, -->

![](assets/Quantitative_method.pdf-0086-09.png)

$$V_0 = \frac{V_1^u}{1 + r} = \frac{V_1^d}{1 + r}, \quad \text{và} \quad 0,25 \times 40 - c_0 = \frac{\text{8 CNY}}{1,05}$$

<!-- Formula Text: V 0 = V 1 u _ 1 + r  = V 1 d _ 1 + r , and 0.25 × 40 − c 0 =  CNY8 _ 1.05  . -->

Chúng ta giải tìm được $c_0$ bằng $2,38\text{ CNY}$. Như vậy, $2,38\text{ CNY}$ là mức giá hợp lý (*fair price*) để người bán hợp đồng nhận về từ người mua hợp đồng.

Là một phần của ví dụ trên, chúng ta đã giả định rằng nhà đầu tư mua $0,25$ đơn vị tài sản như một phần của danh mục. Tỷ trọng này của tài sản cơ sở được gọi là **tỷ số phòng vệ (*hedge ratio*)** trong định giá quyền chọn. Trên thực tế, ví dụ vừa hoàn thành là một quy trình đơn giản hóa để giải tìm giá trị của một quyền chọn mua (*call option*) (nội dung này sẽ được đề cập chi tiết hơn ở phần sau của chương trình học). Giống như trong các ví dụ trước của chúng ta, chúng ta so sánh các chiến lược khác nhau bằng cách sử dụng nguyên lý cộng dòng tiền để giúp giải tìm mức giá không có kinh doanh chênh lệch giá cho một công cụ tài chính.

#### **VÍ DỤ 15 (EXAMPLE 15)** 

### **Quyền chọn Bán (Put Option)** 

Một quyền chọn bán (*put option*) trao cho người sở hữu quyền, nhưng không phải nghĩa vụ, được bán một cổ phiếu ở mức giá thực hiện (*exercise price*) đã định trước $X$. Nếu chúng ta giả định $X = 50\text{ CNY}$, thì giá trị quyền chọn bán sau một kỳ ($p_1$) bằng $\text{Max}(0, \text{50 CNY} - S_1)$.

1. Sử dụng mô hình cây nhị thức một kỳ với cùng các mức giá sau một năm, giá cổ phiếu ban đầu ($S_0$) là $40\text{ CNY}$, và lãi suất chiết khấu là $5\%$, hãy tạo một danh mục phi rủi ro mô phỏng quyền chọn bán với $0,75$ đơn vị tài sản cơ sở và giải tìm giá quyền chọn bán ($p_0$).

#### **Lời giải (Solution):** 

Mô hình nhị thức một kỳ như sau:

<!-- PDF Page 87 -->

![](assets/Quantitative_method.pdf-0087-03.png)

<!-- Picture Text: S 1 u  = CNY56<br>S 0 = CNY40<br>S 1 d  = CNY32<br>0 time T  = 1<br> -->
> **Chú thích hình ảnh:** Tại thời điểm $0$, $S_0 = 40\text{ CNY}$. Tại thời điểm $T = 1$, $S_1^u = 56\text{ CNY}$ hoặc $S_1^d = 32\text{ CNY}$.

Giá trị của quyền chọn bán dưới hai kịch bản như sau:

- **Giá tăng ($p_1^u$):** Mức tăng $40\%$ dẫn đến giá trị quyền chọn bán bằng $0\text{ CNY}$, bởi vì người sở hữu quyền chọn sẽ chọn không bán cổ phiếu ở mức giá thực hiện.

- **Giá giảm ($p_1^d$):** Mức giảm $20\%$ dẫn đến giá trị quyền chọn bán bằng $18\text{ CNY}$ ($\text{50 CNY} - \text{32 CNY}$), bởi vì người sở hữu quyền chọn bán sẽ chọn bán cổ phiếu đang có giá thị trường $32\text{ CNY}$ ở mức giá thực hiện là $50\text{ CNY}$.

![](assets/Quantitative_method.pdf-0087-07.png)

<!-- Picture Text: P 1 u  = CNY0<br>P 0 = ?<br>P 1 d  = CNY18<br>0 time T  = 1<br> -->
> **Chú thích hình ảnh:** Tại thời điểm $0$, giá quyền chọn bán là $p_0 = ?$. Tại thời điểm $T = 1$, giá trị quyền chọn bán là $p_1^u = 0\text{ CNY}$ hoặc $p_1^d = 18\text{ CNY}$.

Khác với quyền chọn mua, quyền chọn bán tăng giá trị khi giá cổ phiếu giảm xuống, vì vậy một danh mục đầu tư phi rủi ro sẽ kết hợp việc mua cổ phiếu với một quyền chọn bán được mua vào (*purchased put option*). Cụ thể, giả sử tại $t = 0$, chúng ta nắm giữ (mua) một quyền chọn bán ở mức giá $p_0$ và mua $0,75$ đơn vị cổ phiếu cơ sở. *(Lưu ý: Trong bản gốc tiếng Anh ghi "sell a put option" ở câu văn nhưng trong phương trình dùng dấu cộng $+p_0$, tức là mua quyền chọn bán kết hợp mua $0,75$ cổ phiếu).* Giá trị danh mục đầu tư tại $t = 0$ và $t = 1$ như sau:

- $V_0 = 0,75S_0 + p_0$,
  - $V_1^u = 0,75S_1^u + p_1^u$, và
  - $V_1^d = 0,75S_1^d + p_1^d$,

trong đó $V_1^u = V_1^d$.

Giá trị của danh mục đầu tư phi rủi ro sau một kỳ ($V_1 = 0,75S_1 + p_1$) dưới hai kịch bản là:

- **Giá tăng ($V_1^u$):** Giá trị danh mục là $42\text{ CNY}$ ($= (0,75 \times \text{56 CNY}) + \text{0 CNY}$).

- **Giá giảm ($V_1^d$):** Giá trị danh mục là $42\text{ CNY}$ ($= (0,75 \times \text{32 CNY}) + \text{18 CNY}$).

Giải tìm $p_0$ bằng cách cho giá trị hiện tại của danh mục mô phỏng ($0,75S_0 + p_0$) bằng với giá trị tương lai đã chiết khấu của khoản thu nhập cuối kỳ, với $S_0$ là $40\text{ CNY}$ và $r$ là $5\%$:

$$V_0 = 0,75S_0 + p_0$$

![](assets/Quantitative_method.pdf-0087-17.png)

$$V_0 = \frac{V_1^u}{1 + r} = \frac{V_1^d}{1 + r}, \quad \text{và}$$

<!-- Formula Text: V 0 = V 1 u _ 1 + r  = V 1 d _ 1 + r , and -->

<!-- PDF Page 88 -->

$$p_0 = \frac{\text{42 CNY}}{1,05} - 0,75(\text{40 CNY})$$

Giải tìm $p_0$ thu được kết quả bằng $10\text{ CNY}$. Mức giá quyền chọn bán cao hơn này là kết quả từ khoản thu nhập cuối kỳ (*payoff*) lớn hơn của quyền chọn bán so với quyền chọn mua dưới các tham số đã cho của mô hình nhị thức. Các yếu tố ảnh hưởng đến giá quyền chọn sẽ được trình bày chi tiết ở phần sau của chương trình học.

<!-- PDF Page 89 -->

# **BÀI TẬP THỰC HÀNH (PRACTICE PROBLEMS)** 

**1.** Grupo Ignacia đã phát hành trái phiếu doanh nghiệp kỳ hạn 10 năm cách đây hai năm. Trái phiếu trả lãi coupon quy đổi theo năm là $10,7\%$ trên cơ sở nửa năm một lần, và lợi suất đáo hạn (YTM) quy đổi theo năm hiện hành là $11,6\%$. Mức giá hiện tại của trái phiếu Grupo Ignacia (trên mỗi $100\text{ MXN}$ mệnh giá) _gần nhất_ với mức nào sau đây:

   - **A.** $95,47\text{ MXN}$.

   - **B.** $97,18\text{ MXN}$.

   - **C.** $95,39\text{ MXN}$.

**2.** Grey Pebble Real Estate tìm kiếm một khoản vay thế chấp kỳ hạn năm năm với lãi suất cố định, trả góp khấu hao hoàn toàn (*fully amortizing*) để tài trợ $75\%$ giá mua một tòa nhà dân cư có chi phí là $5\text{ triệu NZD}$. Lãi suất thế chấp hàng năm là $4,8\%$. Khoản thanh toán hàng tháng cho khoản vay thế chấp này sẽ _gần nhất_ với mức nào sau đây:

   - **A.** $70.424\text{ NZD}$.

   - **B.** $93.899\text{ NZD}$.

   - **C.** $71.781\text{ NZD}$.

**3.** Tập đoàn Mylandia (*Mylandia Corporation*) trả cổ tức hàng năm cho các cổ đông của mình, và khoản thanh toán gần đây nhất là $2,40\text{ CAD}$. Các nhà phân tích theo dõi Mylandia kỳ vọng cổ tức của công ty sẽ tăng trưởng với tốc độ không đổi là $3\%$ mỗi năm đến vĩnh viễn. Các cổ đông của Mylandia yêu cầu mức tỷ suất sinh lợi là $8\%$ mỗi năm. Giá cổ phiếu dự kiến của Mylandia _gần nhất_ với mức nào sau đây:

   - **A.** $48,00\text{ CAD}$.

   - **B.** $49,44\text{ CAD}$.

   - **C.** $51,84\text{ CAD}$.

**4.** Giả sử Mylandia thông báo rằng công ty kỳ vọng dòng tiền sẽ tăng trưởng mạnh trong ba năm tới, và hiện có kế hoạch tăng mức cổ tức $2,40\text{ CAD}$ gần đây thêm $10\%$ trong mỗi năm của ba năm tới. Sau giai đoạn tăng trưởng $10\%$, Mylandia dự kiến sẽ tăng cổ tức hàng năm ở mức không đổi $3\%$ vô thời hạn. Tỷ suất sinh lợi yêu cầu của Mylandia là $8\%$. Dựa trên những kỳ vọng đã điều chỉnh này, giá cổ phiếu dự kiến của cổ phiếu Mylandia là:

   - **A.** $49,98\text{ CAD}$.

   - **B.** $55,84\text{ CAD}$.

   - **C.** $59,71\text{ CAD}$.

**5.** Xét một trái phiếu không trả lãi định kỳ (*zero-coupon bond*) của Liên bang Thụy Sĩ có mệnh giá $100\text{ CHF}$, thời gian còn lại cho đến khi đáo hạn là 12 năm và mức giá hiện tại là $89\text{ CHF}$. Sau ba năm nữa, trái phiếu được kỳ vọng sẽ có mức giá là $95,25\text{ CHF}$. Nếu được mua ngay hôm nay (và bán sau ba năm), tỷ suất sinh lợi quy đổi theo năm kỳ vọng của trái phiếu _gần nhất_ với mức nào sau đây:

   - **A.** $0,58\%$.

   - **B.** $1,64\%$.

<!-- PDF Page 90 -->

   - **C.** $2,29\%$.

**6.** Grupo Ignacia đã phát hành trái phiếu doanh nghiệp kỳ hạn 10 năm cách đây bốn năm. Trái phiếu trả lãi coupon quy đổi theo năm là $10,7\%$ trên cơ sở nửa năm một lần, và mức giá hiện tại của trái phiếu là $97,50\text{ MXN}$ trên mỗi $100\text{ MXN}$ mệnh giá. Lợi suất đáo hạn (YTM) của trái phiếu _gần nhất_ với mức nào sau đây:

   - **A.** $11,28\%$.

   - **B.** $11,50\%$.

   - **C.** $11,71\%$.

**7.** Cổ phiếu của Tập đoàn Mylandia đang giao dịch ở mức giá $60,00\text{ CAD}$. Công ty trả cổ tức hàng năm cho các cổ đông của mình, và khoản thanh toán gần đây nhất trị giá $2,40\text{ CAD}$ vừa diễn ra vào ngày hôm qua. Các nhà phân tích theo dõi Mylandia kỳ vọng cổ tức của công ty sẽ tăng trưởng với tốc độ không đổi là $3\%$ mỗi năm. Tỷ suất sinh lợi yêu cầu của Mylandia là:

   - **A.** $8,00\%$.

   - **B.** $7,00\%$.

   - **C.** $7,12\%$.

**8.** Một nhà phân tích quan sát thấy chỉ số chứng khoán chuẩn NIFTY 50 của Ấn Độ đang giao dịch ở hệ số giá trên thu nhập dự phóng (*forward P/E*) là 15. Tỷ lệ chi trả cổ tức dự kiến của chỉ số trong năm tới là $50\%$, và tỷ suất sinh lợi yêu cầu của chỉ số là $7,50\%$. Nếu nhà phân tích tin rằng cổ tức của chỉ số NIFTY 50 sẽ tăng trưởng với tốc độ không đổi là $4,50\%$ trong tương lai, phát biểu nào sau đây là đúng?

   - **A.** Nhà phân tích nên xem NIFTY 50 là đang bị định giá quá cao (*overpriced*).

   - **B.** Nhà phân tích nên xem NIFTY 50 là đang bị định giá quá thấp (*underpriced*).

   - **C.** Nhà phân tích nên xem NIFTY 50 là đang được định giá hợp lý (*fairly priced*).

**9.** Nếu bạn yêu cầu mức tỷ suất sinh lợi là $8\%$ và phải đầu tư $500.000\text{ USD}$, bạn nên ưu tiên cơ hội đầu tư nào trong Bảng 1?

**Bảng 1: Các Cơ hội Đầu tư (Exhibit 1: Investment Opportunities)** 

|**Dòng tiền (tính bằng nghìn USD)**|**$t = 0$**|**$t = 1$**|**$t = 2$**|**$t = 3$**|
|---|---|---|---|---|
|Cơ hội 1 (*Opportunity 1*)|−500|195|195|195|
|Cơ hội 2 (*Opportunity 2*)|−500|225|195|160,008|

   - **A.** Cơ hội 1

   - **B.** Cơ hội 2

   - **C.** Bàng quan (*Indifferent*) giữa hai cơ hội đầu tư.

**10.** Nợ chính phủ Ý kỳ hạn một năm có lãi suất là $0,73\%$; nợ chính phủ Ý kỳ hạn hai năm có lãi suất là $1,29\%$. Lãi suất tái đầu tư hòa vốn kỳ hạn một năm, bắt đầu sau một năm kể từ bây giờ, _gần nhất_ với mức nào sau đây:

   - **A.** $1,01\%$.

<!-- PDF Page 91 -->

   - **B.** $1,11\%$.

   - **C.** $1,85\%$.

**11.** Tỷ giá hối đoái hiện hành giữa đồng euro và đồng đô la Mỹ là $1,025\text{ USD/EUR}$. Lãi suất phi rủi ro kỳ hạn một năm là $0,75\%$ đối với đồng euro và $3,25\%$ đối với đồng đô la Mỹ (ghép lãi liên tục). Tỷ giá kỳ hạn một năm USD/EUR giúp ngăn chặn _tốt nhất_ các cơ hội kinh doanh chênh lệch giá là:

   - **A.** $1,051\text{ USD/EUR}$.

   - **B.** $1,025\text{ USD/EUR}$.

   - **C.** $0,975\text{ USD/EUR}$.

**12.** Một cổ phiếu hiện đang giao dịch ở mức giá $25\text{ USD}$. Sau một năm, giá trị của nó sẽ tăng lên $35\text{ USD}$ hoặc giảm xuống $15\text{ USD}$. Một nhà đầu tư bán một quyền chọn mua (*call option*) trên cổ phiếu này, trao cho người mua quyền, nhưng không phải nghĩa vụ, được mua cổ phiếu ở mức giá $25\text{ USD}$ sau một năm. Cùng lúc đó, nhà đầu tư mua $0,5$ đơn vị cổ phiếu. Phát biểu nào sau đây về giá trị danh mục đầu tư của nhà đầu tư vào cuối năm thứ nhất là đúng?

   - **A.** Danh mục đầu tư có giá trị là $7,50\text{ USD}$ trong cả hai kịch bản.

   - **B.** Danh mục đầu tư có giá trị là $25\text{ USD}$ trong cả hai kịch bản.

   - **C.** Danh mục đầu tư có giá trị là $17,50\text{ USD}$ nếu cổ phiếu tăng giá và $7,50\text{ USD}$ nếu cổ phiếu giảm giá.


---

# Tập 1: Phương pháp Định lượng (Volume 1: Quantitative Methods)
## Học phần 2: Giá trị Thời gian của Tiền trong Tài chính (Learning Module 2: Time Value of Money in Finance)
### Phần 4/4: Lời giải Bài tập Thực hành (Solutions) (Trang PDF 92–94)

---

<!-- PDF Page 92 -->

# **LỜI GIẢI (SOLUTIONS)** 

1. C là đáp án đúng. Các khoản thanh toán coupon là $5,35$ ($= 10,7 / 2$), lãi suất chiết khấu là $5,8\%$ ($= 11,6\% / 2$) mỗi kỳ, và số kỳ là $16$ ($= 8 \times 2$). Sử dụng Phương trình 6, phép tính được thực hiện như sau:

![](assets/Quantitative_method.pdf-0092-05.png)

$$95,39 = \frac{5,35}{1,058} + \frac{5,35}{1,058^2} + \frac{5,35}{1,058^3} + \frac{5,35}{1,058^4} + \dots + \frac{5,35}{1,058^{14}} + \frac{5,35}{1,058^{15}} + \frac{105,35}{1,058^{16}}$$

<!-- Formula Text: 95.39  =   5.35 _ 1.058  +   5.35 _ 1.058 2  +   5.35 _ 1.058 3  +   5.35 _ 1.058 4  + … +   5.35 _ 1.058 14  +   5.35 _ 1.058 15  +  105.35 _ 1.058 16 . -->

Ngoài ra, việc sử dụng hàm PV trong Microsoft Excel hoặc Google Sheets (`=PV(0.058, 16, 5.35, 100, 0)`) cũng cho kết quả là $95,39\text{ MXN}$.
A không đúng. $95,47\text{ MXN}$ là kết quả khi sử dụng sai các khoản thanh toán coupon là $10,7$, lãi suất chiết khấu là $11,6\%$, và số kỳ là 8.
B không đúng. $97,18\text{ MXN}$ là kết quả khi sử dụng đúng tiền lãi coupon nửa năm và lãi suất chiết khấu nửa năm, nhưng lại sử dụng sai số kỳ là 8.

2. A là đáp án đúng. Giá trị hiện tại của khoản vay thế chấp là $3,75\text{ triệu NZD}$ ($= 0,75 \times 5.000.000$), lãi suất chiết khấu định kỳ là $0,004$ ($= 0,048 / 12$), và số kỳ là $60$ ($= 5 \times 12$). Sử dụng Phương trình 8:

![](assets/Quantitative_method.pdf-0092-09.png)

<!-- Formula Text: A = $70, 424  = 0_ -->

![](assets/Quantitative_method.pdf-0092-10.png)

<!-- Formula Text: 1 − (1 + 0.4%) −60  . -->

$$A = \text{70.424 NZD} = \frac{0,4\% (\text{3.750.000 NZD})}{1 - (1 + 0,4\%)^{-60}}$$

Ngoài ra, hàm PMT trên bảng tính có thể được sử dụng với các thông số đầu vào đã nêu ở trên.

B không đúng. $93.899\text{ NZD}$ là kết quả nếu sử dụng sai $5\text{ triệu NZD}$ làm giá trị hiện tại.

C không đúng. $71.781\text{ NZD}$ là kết quả nếu phép tính được thực hiện bằng cách sử dụng $4,8\%$ làm lãi suất và 5 làm số kỳ, sau đó lấy đáp số chia cho 12.

3. B là đáp án đúng. Cổ tức dự kiến tiếp theo của Mylandia là $2,472\text{ CAD}$ ($= 2,40 \times 1,03$), và sử dụng Phương trình 14:

![](assets/Quantitative_method.pdf-0092-15.png)

$$\text{PV}_t = \frac{2,40(1 + 0,03)}{0,08 - 0,03} = \frac{2,472}{0,05} = 49,44$$

<!-- Formula Text: P V t =  2.40(1 + 0.03) _ 0.08 − 0.03   =  2.472 _ 0.05   =  49.44. -->

4. C là đáp án đúng. Thực hiện theo bước đầu tiên, chúng ta quan sát thấy các khoản cổ tức dự kiến của Mylandia trong ba năm tới như sau:

- Sau 1 năm: $D_1 = \text{2,64 CAD}$ ($= 2,40 \times 1,10$)
- Sau 2 năm: $D_2 = \text{2,90 CAD}$ ($= 2,40 \times 1,10^2$)
- Sau 3 năm: $D_3 = \text{3,19 CAD}$ ($= 2,40 \times 1,10^3$)

Bước thứ hai liên quan đến tốc độ tăng trưởng thấp hơn ở mức $3\%$. Vào cuối năm thứ tư, cổ tức của Mylandia ($D_4$) dự kiến là $3,29\text{ CAD}$ ($= 2,40 \times 1,10^3 \times 1,03$). Tại thời điểm này, giá trị cuối kỳ dự kiến (*expected terminal value*) của Mylandia vào cuối năm thứ ba là $65,80\text{ CAD}$ khi sử dụng Phương trình 17, như sau:

![](assets/Quantitative_method.pdf-0092-20.png)

$$E(S_{t+n}) = \frac{3,29}{0,08 - 0,03} = 65,80$$

<!-- Formula Text: E(S t+n ) = 3.29 _ 0.08− 0.03   =  65.80. -->

![](assets/Quantitative_method.pdf-0092-21.png)

Thứ ba, chúng ta tính tổng giá trị hiện tại của các khoản cổ tức dự kiến này bằng cách sử dụng Phương trình 16:

$$\text{PV}_t = \frac{2,64}{1,08} + \frac{2,90}{1,08^2} + \frac{3,19}{1,08^3} + \frac{65,80}{1,08^3} = 59,71$$

<!-- Formula Text: Third, we calculate the sum of the present values of these expected dividends using Equation 16: P V t =  2.64 _ 1.08 +  2.90 _ 1.08 2 +  3.19 _ 1.08 3  +  65.80 _ 1.08 3   =  59.71. -->

5. C là đáp án đúng. $\text{FV}$ của trái phiếu là $95,25\text{ CHF}$, $\text{PV}$ là $89\text{ CHF}$, và số kỳ hàng năm ($t$) là 3. Sử dụng Phương trình 18:

<!-- PDF Page 93 -->

$$2,29\% = (95,25 / 89)^{(1/3)} - 1$$

*(Lưu ý: Trong bản gốc tiếng Anh ghi nhầm số hiển thị là `92.25/89` nhưng kết quả tính từ `95.25/89` đúng bằng $2,29\%$.).*

A không đúng vì kết quả này được suy ra khi sử dụng $t = 12$.
B không đúng vì kết quả này được suy ra khi sử dụng $\text{PV}$ là $95,25\text{ CHF}$ và $\text{FV}$ là 100 (cho 9 năm còn lại).

6. A là đáp án đúng. YTM được tính bằng cách giải hàm RATE trên bảng tính với các thông số đầu vào sau: số kỳ là $12$ ($= 6 \times 2$), khoản thanh toán coupon là $5,35$ ($= 10,7 / 2$), $\text{PV}$ là $-97,50$, và $\text{FV}$ là $100$. Kết quả giải hàm RATE là $5,64\%$ tính theo kỳ nửa năm, vì vậy nhân với 2 để tính ra YTM quy đổi theo năm là $11,28\%$.

B không đúng, vì $11,50\%$ là kết quả nếu số kỳ sử dụng là 8 thay vì 12.
C không đúng, vì $11,71\%$ là kết quả nếu số kỳ sử dụng là 6 thay vì 12.

7. C là đáp án đúng. Chúng ta có thể giải tìm tỷ suất sinh lợi yêu cầu dựa trên giả định cổ tức tăng trưởng không đổi bằng cách sử dụng Phương trình 21:

$$r = \frac{2,40(1,03)}{60} + 0,03 = 0,0712 \text{ hay } 7,12\%$$

B không đúng vì $7,00\%$ là kết quả nếu chúng ta sử dụng khoản cổ tức trước đó là $2,40\text{ CAD}$ thay vì khoản cổ tức dự kiến tiếp theo.
A không đúng vì $8,00\%$ đơn giản là tỷ suất sinh lợi yêu cầu được giả định từ một trong các ví dụ trước của Mylandia trong đó mức giá giải ra có giá trị thấp hơn.

8. B là đáp án đúng. Sử dụng Phương trình 24, các thông số đầu vào trên dẫn đến bất đẳng thức sau:

$$15 < \frac{0,50}{0,075 - 0,045} = 16,67$$

Bất đẳng thức trên hàm ý rằng nhà phân tích nên xem chỉ số NIFTY 50 là đang được định giá quá thấp (*underpriced*). Các thông số cơ bản đưa vào phương trình hàm ý một hệ số giá trên thu nhập dự phóng là $16,67$ thay vì $15$. Một cách tiếp cận khác để trả lời câu hỏi này là giải tìm tốc độ tăng trưởng ngầm định bằng cách sử dụng hệ số giá trên thu nhập dự phóng quan sát được là 15 và so sánh con số này với kỳ vọng tăng trưởng của nhà phân tích:

$$15 = \frac{0,50}{0,075 - g}$$

Giải tìm $g$ cho kết quả là $4,1667\%$. Vì nhà phân tích kỳ vọng tốc độ tăng trưởng cổ tức của NIFTY 50 cao hơn ở mức $4,50\%$, nên chỉ số này được xem là đang bị định giá thấp (*underpriced*).

9. C là đáp án đúng. Sử dụng nguyên lý cộng dòng tiền (*cash flow additivity*), hãy so sánh hai cơ hội đầu tư bằng cách lấy Cơ hội 1 trừ đi Cơ hội 2, thu được các dòng tiền sau:

|**Dòng tiền (nghìn USD)**|**$t = 0$**|**$t = 1$**|**$t = 2$**|**$t = 3$**|
|---|---|---|---|---|
|Cơ hội 1 – Cơ hội 2|0|−30|0|34,992|

Việc tìm giá trị hiện tại của các dòng tiền trên ở mức lãi suất chiết khấu $8\%$ cho thấy cả hai cơ hội đầu tư có cùng giá trị hiện tại (vì $-30/1,08 + 34,992/1,08^3 = 0$). Do đó, hai cơ hội này hoàn toàn giống hệt nhau về mặt kinh tế, và không có sự ưu tiên rõ ràng nào cho cơ hội này hơn cơ hội kia.

10. C là đáp án đúng. Lãi suất kỳ hạn một năm (*one-year forward rate*) phản ánh lãi suất tái đầu tư hòa vốn kỳ hạn một năm bắt đầu sau một năm kể từ bây giờ, được tính như sau:

$$\begin{aligned}
F_{1,1} &= (1 + r_2)^2 / (1 + r_1) - 1 \\
F_{1,1} &= (1,0129)^2 / (1,0073) - 1 = 0,0185 \text{ hay } 1,85\%
\end{aligned}$$

11. A là đáp án đúng. Để tránh các cơ hội kinh doanh chênh lệch giá khi chuyển đổi giữa đồng euro và đồng đô la Mỹ, các nhà đầu tư phải có khả năng khóa chặt một mức tỷ giá hối đoái kỳ hạn một năm là $1,051\text{ USD/EUR}$ ngay hôm nay. Phương pháp giải được trình bày dưới đây:

<!-- PDF Page 94 -->

- Sau một năm, một đơn vị đồng euro được đầu tư phi rủi ro có giá trị là $1,0075\text{ EUR}$ ($= e^{0,0075}$).
- Sau một năm, một đơn vị đồng euro được chuyển đổi sang đô la Mỹ và sau đó được đầu tư phi rủi ro có giá trị là $1,0589\text{ USD}$ ($= 1,025 \times e^{0,0325}$).

Để chuyển đổi $1,0589\text{ USD}$ thành $1,0075\text{ EUR}$ đòi hỏi một tỷ giá hối đoái kỳ hạn là $1,051\text{ USD/EUR}$ ($= 1,0589 / 1,0075$).

12. A là đáp án đúng. Bất kể giá cổ phiếu tăng hay giảm, danh mục đầu tư của nhà đầu tư đều có giá trị là $7,50\text{ USD}$ như sau:

- Nếu giá cổ phiếu tăng lên $35\text{ USD}$, giá trị danh mục $= 0,5 \times 35 - 10 = 7,50\text{ USD}$.
- Nếu giá cổ phiếu giảm xuống $15\text{ USD}$, giá trị danh mục $= 0,5 \times 15 - 0 = 7,50\text{ USD}$.

Nếu giá cổ phiếu tăng lên $35\text{ USD}$, quyền chọn mua đã bán ở mức giá thực hiện $25\text{ USD}$ sẽ có giá trị đối với người mua quyền chọn là $10\text{ USD}$ (do đó là khoản nghĩa vụ $-10\text{ USD}$ đối với người bán quyền chọn), bù trừ với mức tăng của giá cổ phiếu.
