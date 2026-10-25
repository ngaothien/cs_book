# Tập 1: Phương pháp Định lượng (Volume 1: Quantitative Methods)
## Học phần 1: Lãi suất và Tỷ suất sinh lợi (Learning Module 1: Rates and Returns)
### Phần 1/3: Giới thiệu (Introduction) (Trang PDF 11–26)

---

<!-- PDF Page 11 -->

#### H Ọ C P H Ầ N (L E A R N I N G M O D U L E)

# **<mark>1</mark>** 

### **Lãi suất và Tỷ suất sinh lợi (Rates and Returns)** 

**Biên soạn bởi: Richard A. DeFusco, PhD, CFA, Dennis W. McLeavey, DBA, CFA, Jerald E. Pinto, PhD, CFA, David E. Runkle, PhD, CFA, và Vijay Singal, PhD, CFA.** 

_Richard A. DeFusco, PhD, CFA, công tác tại Đại học Nebraska-Lincoln (Hoa Kỳ). Dennis W. McLeavey, DBA, CFA, công tác tại Đại học Rhode Island (Hoa Kỳ). Jerald E. Pinto, PhD, CFA, công tác tại Viện CFA (Hoa Kỳ). David E. Runkle, PhD, CFA, công tác tại Jacobs Levy Equity Management (Hoa Kỳ). Vijay Singal, PhD, CFA, công tác tại Virginia Tech (Hoa Kỳ)._ 

###### **<mark>MỤC TIÊU HỌC TẬP (LEARNING OUTCOMES)</mark>** 

- **_Mức độ thành thạo (Mastery) – Ứng viên cần có khả năng:_**
  - diễn giải lãi suất (*interest rates*) dưới góc độ tỷ suất sinh lợi yêu cầu (*required rates of return*), lãi suất chiết khấu (*discount rates*), hoặc chi phí cơ hội (*opportunity costs*) và giải thích lãi suất như là tổng của lãi suất phi rủi ro thực (*real risk-free rate*) và các phần bù (*premiums*) nhằm đền bù cho nhà đầu tư khi gánh chịu các loại rủi ro riêng biệt;
  - tính toán và diễn giải các phương pháp đo lường tỷ suất sinh lợi khác nhau theo thời gian và mô tả các trường hợp sử dụng phù hợp của chúng;
  - so sánh tỷ suất sinh lợi có trọng số tiền tệ (*money-weighted rate of return*) và tỷ suất sinh lợi có trọng số thời gian (*time-weighted rate of return*), đồng thời đánh giá hiệu quả hoạt động của các danh mục đầu tư dựa trên các thước đo này;
  - tính toán và diễn giải các thước đo tỷ suất sinh lợi quy đổi theo năm (*annualized return measures*) và tỷ suất sinh lợi ghép lãi liên tục (*continuously compounded returns*), cũng như mô tả các trường hợp sử dụng phù hợp của chúng;
  - tính toán và diễn giải các thước đo tỷ suất sinh lợi chính yếu khác và mô tả các trường hợp sử dụng phù hợp của chúng.

![](assets/Quantitative_method.pdf-0011-08.png)

<!-- Picture Text: 1<br> -->

##### **GIỚI THIỆU (INTRODUCTION)** 

Lãi suất (*interest rates*) là một khái niệm cốt lõi trong tài chính. Trong một số trường hợp, chúng ta giả định một mức lãi suất cụ thể và trong những trường hợp khác, lãi suất lại là ẩn số cần phải xác định. Mặc dù tài liệu đọc trước (*pre-reads*) đã đề cập đến cơ chế giải quyết các bài toán giá trị thời gian của tiền (*time value of money*), tại đây trước hết chúng tôi sẽ minh họa các khái niệm kinh tế nền tảng bằng cách giải thích ý nghĩa và cách diễn giải của lãi suất, sau đó tiến hành tính toán, diễn giải và so sánh các thước đo tỷ suất sinh lợi khác nhau.

<!-- PDF Page 12 -->

###### **TỔNG QUAN HỌC PHẦN (LEARNING MODULE OVERVIEW)** 

- Lãi suất (*interest rate*), ký hiệu là $r$, có thể mang ba cách diễn giải: (1) tỷ suất sinh lợi yêu cầu (*required rate of return*), (2) lãi suất chiết khấu (*discount rate*), hoặc (3) chi phí cơ hội (*opportunity cost*). Lãi suất phản ánh mối quan hệ giữa các dòng tiền phát sinh ở các thời điểm khác nhau.

- Lãi suất có thể được xem là tổng của lãi suất phi rủi ro thực (*real risk-free interest rate*) và một tập hợp các phần bù (*premiums*) đền bù cho người cho vay vì đã gánh chịu các loại rủi ro riêng biệt: phần bù lạm phát (*inflation premium*), phần bù rủi ro vỡ nợ (*default risk premium*), phần bù thanh khoản (*liquidity premium*), và phần bù kỳ hạn (*maturity premium*).

- Lãi suất phi rủi ro danh nghĩa (*nominal risk-free interest rate*) được tính xấp xỉ bằng tổng của lãi suất phi rủi ro thực và phần bù lạm phát.

- Tổng tỷ suất sinh lợi (*total return*) của một tài sản tài chính bao gồm hai thành phần: lợi suất thu nhập (*income yield*) bao gồm cổ tức tiền mặt hoặc các khoản thanh toán tiền lãi, và tỷ suất sinh lợi phản ánh lãi vốn hoặc lỗ vốn (*capital gain or loss*) phát sinh từ những thay đổi trong giá của tài sản tài chính đó.

- Tỷ suất sinh lợi thời kỳ nắm giữ (*holding period return*), ký hiệu là $R$, là mức sinh lợi mà nhà đầu tư kiếm được trong một khoảng thời gian xác định duy nhất (ví dụ: một ngày, một tháng, năm năm).

- Tỷ suất sinh lợi nhiều kỳ (*multiperiod returns*) có thể được tính toán qua nhiều thời kỳ nắm giữ bằng cách sử dụng các thước đo tỷ suất sinh lợi khác nhau (ví dụ: trung bình cộng – *arithmetic mean*, trung bình nhân – *geometric mean*, trung bình điều hòa – *harmonic mean*, trung bình cắt bỏ ngoại lai – *trimmed mean*, trung bình làm mượt ngoại lai – *winsorized mean*). Mỗi phép tính tỷ suất sinh lợi có những ứng dụng đặc thù để đánh giá các khoản đầu tư.

- Việc lựa chọn sử dụng thước đo giá trị trung bình nào trong số các phương án thay thế cho một tập dữ liệu nhất định phụ thuộc vào các yếu tố cân nhắc như sự hiện diện của các giá trị ngoại lai cực đoan (*extreme outliers*), các giá trị ngoại lai mà chúng ta muốn đưa vào tính toán, liệu phân phối có đối xứng hay không, và hiệu ứng ghép lãi (*compounding*).

- Tỷ suất sinh lợi có trọng số tiền tệ (*money-weighted return*) phản ánh mức sinh lợi thực tế kiếm được từ một khoản đầu tư sau khi đã tính đến giá trị và thời điểm của các dòng tiền liên quan đến khoản đầu tư đó.

- Tỷ suất sinh lợi có trọng số thời gian (*time-weighted return*) đo lường tốc độ tăng trưởng kép (*compound rate of growth*) của một đơn vị tiền tệ được đầu tư vào danh mục trong một giai đoạn đo lường xác định. Khác với tỷ suất sinh lợi có trọng số tiền tệ, tỷ suất sinh lợi có trọng số thời gian không nhạy cảm với thời điểm và quy mô của các dòng tiền, do đó đây là thước đo hiệu quả hoạt động được ưu tiên để đánh giá các nhà quản lý danh mục đầu tư vì việc rút tiền hoặc nộp thêm tiền vào danh mục nhìn chung nằm ngoài tầm kiểm soát của nhà quản lý danh mục.

- Tiền lãi có thể được thanh toán hoặc nhận về thường xuyên hơn mức hàng năm. Lãi suất định kỳ (*periodic interest rate*) và số kỳ ghép lãi tương ứng (ví dụ: hàng quý, hàng tháng, hàng ngày) cần được điều chỉnh để tính toán giá trị hiện tại (*present value*) và giá trị tương lai (*future value*).

- Việc quy đổi tỷ suất sinh lợi định kỳ theo năm (*annualizing periodic returns*) cho phép các nhà đầu tư so sánh các khoản đầu tư khác nhau qua các thời kỳ nắm giữ khác nhau nhằm đánh giá và so sánh hiệu quả tương đối của chúng tốt hơn. Khi số kỳ ghép lãi mỗi năm tiến tới vô cùng, tiền lãi được gọi là ghép lãi liên tục (*compounded continuously*).

- Tỷ suất sinh lợi gộp (*gross return*), tức tỷ suất sinh lợi trước khi khấu trừ các chi phí quản lý và hành chính (những chi phí không liên quan trực tiếp đến việc tạo ra lợi nhuận), là thước đo phù hợp để đánh giá và so sánh năng lực của một nhà quản lý tài sản.

<!-- PDF Page 13 -->

- Tỷ suất sinh lợi ròng (*net return*), bằng tỷ suất sinh lợi gộp trừ đi các chi phí quản lý và hành chính, là thước đo phản ánh tốt hơn những gì nhà đầu tư thực sự kiếm được.

- Tỷ suất sinh lợi danh nghĩa sau thuế (*after-tax nominal return*) được tính bằng tổng tỷ suất sinh lợi trừ đi bất kỳ khoản dự phòng thuế nào đánh trên cổ tức, tiền lãi và lãi vốn đã thực hiện (*realized gains*).

- Tỷ suất sinh lợi thực (*real returns*) đặc biệt hữu ích khi so sánh tỷ suất sinh lợi qua các giai đoạn thời gian khác nhau vì tỷ lệ lạm phát có thể biến động theo thời gian, đồng thời cũng đặc biệt hữu ích để so sánh các khoản đầu tư qua nhiều thời kỳ và hiệu quả hoạt động giữa các loại tài sản (*asset classes*) khác nhau có cơ chế chịu thuế khác nhau.

- Việc sử dụng đòn bẩy (*leveraging*) cho danh mục đầu tư, thông qua vay nợ hoặc hợp đồng tương lai (*futures*), có thể khuếch đại các khoản lãi hoặc lỗ của danh mục đó.

##### **LÃI SUẤT VÀ GIÁ TRỊ THỜI GIAN CỦA TIỀN (INTEREST RATES AND TIME VALUE OF MONEY)** 

## **<mark>2</mark>** 

diễn giải lãi suất dưới góc độ tỷ suất sinh lợi yêu cầu, lãi suất chiết khấu, hoặc chi phí cơ hội và giải thích lãi suất như là tổng của lãi suất phi rủi ro thực và các phần bù nhằm đền bù cho nhà đầu tư khi gánh chịu các loại rủi ro riêng biệt

Giá trị thời gian của tiền (*time value of money*) thiết lập sự tương đương giữa các dòng tiền phát sinh vào những ngày khác nhau. Vì tiền mặt nhận được ngày hôm nay được ưa thích hơn tiền mặt hứa hẹn trong tương lai, chúng ta phải thiết lập một cơ sở nhất quán cho sự đánh đổi này để so sánh các công cụ tài chính trong những trường hợp mà tiền mặt được chi trả hoặc nhận về ở các thời điểm khác nhau. **Lãi suất (*interest rate*)** (hay lợi suất – *yield*), ký hiệu là $r$, là một tỷ suất sinh lợi phản ánh mối quan hệ giữa các dòng tiền ở các thời điểm (ngày tháng) khác nhau. Nếu 9.500 USD ngày hôm nay và 10.000 USD sau một năm có giá trị tương đương nhau, thì $\text{10.000 USD} - \text{9.500 USD} = \text{500 USD}$ là khoản đền bù yêu cầu cho việc nhận 10.000 USD sau một năm thay vì nhận ngay bây giờ. Lãi suất (tức là khoản đền bù yêu cầu được biểu thị dưới dạng tỷ suất sinh lợi) là $\text{500 USD} / \text{9.500 USD} = 0,0526$ hay $5,26\%$.

Lãi suất có thể được hiểu theo ba cách:

- Thứ nhất, chúng có thể được xem là _tỷ suất sinh lợi yêu cầu (required rates of return)_ — tức là mức tỷ suất sinh lợi tối thiểu mà một nhà đầu tư phải nhận được để chấp nhận một khoản đầu tư.

- Thứ hai, lãi suất có thể được xem là _lãi suất chiết khấu (discount rates)_. Trong ví dụ trước, $5,26\%$ là lãi suất chiết khấu mà tại đó 10.000 USD sau một năm tương đương với 9.500 USD ngày hôm nay. Do đó, chúng ta sử dụng thuật ngữ “lãi suất” và “lãi suất chiết khấu” gần như thay thế cho nhau.

- Thứ ba, lãi suất có thể được xem là _chi phí cơ hội (opportunity costs)_. **Chi phí cơ hội (*opportunity cost*)** là giá trị mà các nhà đầu tư từ bỏ khi lựa chọn một phương án hành động. Trong ví dụ trên, nếu bên cung cấp 9.500 USD quyết định chi tiêu số tiền đó ngay hôm nay, họ sẽ từ bỏ việc kiếm được mức sinh lợi $5,26\%$ do chọn tiêu dùng thay vì tiết kiệm. Vì vậy, chúng ta có thể xem $5,26\%$ là chi phí cơ hội của việc tiêu dùng hiện tại.

<!-- PDF Page 14 -->

###### **Các yếu tố quyết định lãi suất (Determinants of Interest Rates)** 

Kinh tế học cho chúng ta biết rằng lãi suất được thiết lập bởi các lực lượng cung và cầu, nơi các nhà đầu tư cung cấp vốn và người đi vay có nhu cầu sử dụng vốn đó. Đứng trên góc độ của các nhà đầu tư khi phân tích lãi suất do thị trường quyết định, chúng ta có thể xem lãi suất $r$ được cấu thành từ lãi suất phi rủi ro thực cộng với một tập hợp các phần bù đóng vai trò là tỷ suất sinh lợi yêu cầu hoặc khoản đền bù cho việc gánh chịu các loại rủi ro riêng biệt:

$$r = \text{Lãi suất phi rủi ro thực} + \text{Phần bù lạm phát} + \text{Phần bù rủi ro vỡ nợ} + \text{Phần bù thanh khoản} + \text{Phần bù kỳ hạn} \tag{1}$$

*(Tiếng Anh: $r = \text{Real risk-free interest rate} + \text{Inflation premium} + \text{Default risk premium} + \text{Liquidity premium} + \text{Maturity premium}$)*

- **Lãi suất phi rủi ro thực (*real risk-free interest rate*)** là lãi suất một kỳ của một chứng khoán hoàn toàn phi rủi ro nếu không có lạm phát dự kiến. Trong lý thuyết kinh tế, lãi suất phi rủi ro thực phản ánh sự ưa thích theo thời gian của các cá nhân đối với việc tiêu dùng thực ở hiện tại so với tương lai.

- **Phần bù lạm phát (*inflation premium*)** đền bù cho các nhà đầu tư đối với lạm phát dự kiến và phản ánh tỷ lệ lạm phát trung bình được kỳ vọng trong suốt kỳ hạn của khoản nợ. Lạm phát làm giảm sức mua của một đơn vị tiền tệ — tức số lượng hàng hóa và dịch vụ mà một người có thể mua được bằng đơn vị tiền tệ đó.

- **Phần bù rủi ro vỡ nợ (*default risk premium*)** đền bù cho các nhà đầu tư đối với khả năng người đi vay không thực hiện được khoản thanh toán đã cam kết vào đúng thời điểm và đủ số tiền theo hợp đồng.

- **Phần bù thanh khoản (*liquidity premium*)** đền bù cho các nhà đầu tư đối với rủi ro thua lỗ so với giá trị hợp lý (*fair value*) của khoản đầu tư nếu khoản đầu tư đó cần được chuyển đổi thành tiền mặt một cách nhanh chóng. Ví dụ, tín phiếu Kho bạc Hoa Kỳ (*US Treasury bills – T-bills*) không chịu phần bù thanh khoản vì một lượng lớn tín phiếu này có thể được mua và bán mà không làm ảnh hưởng đến giá thị trường của chúng. Ngược lại, nhiều trái phiếu của các tổ chức phát hành nhỏ lại giao dịch không thường xuyên sau khi phát hành; lãi suất của những trái phiếu như vậy bao gồm một phần bù thanh khoản phản ánh chi phí tương đối cao (bao gồm cả tác động lên giá) của việc bán đi một vị thế.

- **Phần bù kỳ hạn (*maturity premium*)** đền bù cho các nhà đầu tư đối với sự gia tăng độ nhạy cảm của giá trị thị trường của khoản nợ trước sự thay đổi của lãi suất thị trường khi kỳ hạn được kéo dài, nhìn chung là vậy (giữ các yếu tố khác không đổi – *holding all else equal*). Chênh lệch giữa lãi suất của trái phiếu Kho bạc có tính thanh khoản cao, kỳ hạn dài hơn và lãi suất của trái phiếu Kho bạc ngắn hạn thường phản ánh một phần bù kỳ hạn dương cho khoản nợ dài hạn hơn (và có thể bao gồm cả các phần bù lạm phát khác nhau).

Tổng của lãi suất phi rủi ro thực và phần bù lạm phát là lãi suất phi rủi ro danh nghĩa (*nominal risk-free interest rate*):

Lãi suất phi rủi ro danh nghĩa phản ánh sự kết hợp của lãi suất phi rủi ro thực cộng với phần bù lạm phát:

$$(1 + \text{Lãi suất phi rủi ro danh nghĩa}) = (1 + \text{Lãi suất phi rủi ro thực})(1 + \text{Phần bù lạm phát})$$

Tuy nhiên, trên thực tế, lãi suất danh nghĩa thường được tính xấp xỉ bằng tổng của lãi suất phi rủi ro thực cộng với phần bù lạm phát:

$$\text{Lãi suất phi rủi ro danh nghĩa} = \text{Lãi suất phi rủi ro thực} + \text{Phần bù lạm phát}$$

Nhiều quốc gia có các khoản nợ chính phủ ngắn hạn mà lãi suất của chúng có thể được xem là đại diện cho lãi suất phi rủi ro danh nghĩa trong khung thời gian đó tại quốc gia tương ứng. Chính phủ Pháp phát hành BTF, hay tín phiếu Kho bạc chiết khấu lãi suất cố định có thể chuyển nhượng (*Bons du Trésor à taux fixe et à intérêts précomptés*), với kỳ hạn lên đến một năm. Chính phủ Nhật Bản phát hành tín phiếu Kho bạc ngắn hạn với kỳ hạn 6 và 12 tháng. Chẳng hạn, lãi suất của tín phiếu Kho bạc Hoa Kỳ (T-bill) kỳ hạn 90 ngày đại diện cho lãi suất phi rủi ro danh nghĩa của Hoa Kỳ trong ba

<!-- PDF Page 15 -->

tháng tới. Thông thường, lãi suất được yết theo năm (*quoted in annual terms*), vì vậy lãi suất của một chứng khoán nợ chính phủ kỳ hạn 90 ngày được yết ở mức $3\%$ là lãi suất đã quy đổi theo năm (*annualized rate*) chứ không phải lãi suất thực tế kiếm được trong giai đoạn 90 ngày đó.

Cho dù lãi suất chúng ta sử dụng là tỷ suất sinh lợi yêu cầu, lãi suất chiết khấu hay chi phí cơ hội, mức lãi suất đó đều bao hàm lãi suất phi rủi ro thực và một tập hợp các phần bù rủi ro (*risk premia*) phụ thuộc vào đặc điểm của các dòng tiền. Tập hợp các phần bù nền tảng bao gồm lạm phát, rủi ro vỡ nợ, rủi ro thanh khoản và rủi ro kỳ hạn. Tất cả các phần bù này đều thay đổi theo thời gian và biến động liên tục, cũng giống như lãi suất phi rủi ro thực. Do đó, mọi mức lãi suất đều biến động, nhưng mức độ thay đổi nhiều hay ít phụ thuộc vào các yếu tố kinh tế cơ bản khác nhau — và vào kỳ vọng về việc các yếu tố kinh tế cơ bản này có thể thay đổi như thế nào trong tương lai.

###### **VÍ DỤ 1 (EXAMPLE 1)** 

###### **Xác định lãi suất (Determining Interest Rates)** 

Bảng 1 (*Exhibit 1*) trình bày thông tin chọn lọc của năm chứng khoán nợ. Cả năm khoản đầu tư đều chỉ hứa hẹn một khoản thanh toán duy nhất khi đáo hạn. Giả định rằng các phần bù liên quan đến lạm phát, thanh khoản và rủi ro vỡ nợ là không đổi qua mọi khung thời gian.

**Bảng 1: Các phương án đầu tư và đặc điểm của chúng (Exhibit 1: Investments Alternatives and Their Characteristics)** 

|**Khoản đầu tư (Investment)**|**Kỳ hạn (Maturity - năm)**|**Tính thanh khoản (Liquidity)**|**Rủi ro vỡ nợ (Default Risk)**|**Lãi suất (Interest Rate) (%)**|
|---|---|---|---|---|
|1|2|Cao (High)|Thấp (Low)|2,0|
|2|2|Thấp (Low)|Thấp (Low)|2,5|
|3|7|Thấp (Low)|Thấp (Low)|$r_3$|
|4|8|Cao (High)|Thấp (Low)|4,0|
|5|8|Thấp (Low)|Cao (High)|6,5|

Dựa trên thông tin trong Bảng 1, hãy giải quyết các yêu cầu sau:

1. Giải thích sự khác biệt giữa lãi suất của Khoản đầu tư 1 và Khoản đầu tư 2.

###### **Lời giải (Solution):** 

Khoản đầu tư 2 giống hệt Khoản đầu tư 1 ngoại trừ việc Khoản đầu tư 2 có tính thanh khoản thấp. Chênh lệch giữa lãi suất của Khoản đầu tư 2 và Khoản đầu tư 1 là $0,5\%$. Khoản chênh lệch giữa hai mức lãi suất này đại diện cho phần bù thanh khoản (*liquidity premium*), tức khoản đền bù cho tính thanh khoản thấp hơn của Khoản đầu tư 2 (rủi ro thua lỗ so với giá trị hợp lý của khoản đầu tư nếu khoản đầu tư cần được chuyển đổi thành tiền mặt một cách nhanh chóng).

2. Ước tính phần bù rủi ro vỡ nợ (*default risk premium*) ảnh hưởng đến tất cả các chứng khoán.

###### **Lời giải (Solution):** 

Để ước tính phần bù rủi ro vỡ nợ, hãy xác định hai khoản đầu tư có cùng kỳ hạn nhưng có mức độ rủi ro vỡ nợ khác nhau. Khoản đầu tư 4 và 5 đều có kỳ hạn là tám năm nhưng có mức độ rủi ro vỡ nợ khác nhau. Tuy nhiên, Khoản đầu tư 5 có tính thanh khoản thấp và do đó chịu thêm phần bù thanh khoản so với Khoản đầu tư 4. Từ Phần 1, chúng ta biết phần bù thanh khoản là $0,5\%$. Chênh lệch giữa lãi suất của Khoản đầu tư 5 và 4 là $2,5\%$ ($6,5\% - 4,0\%$), trong đó $0,5\%$ là phần bù thanh khoản. Điều này

<!-- PDF Page 16 -->

hàm ý rằng $2,0\%$ ($2,5\% - 0,5\%$) phải đại diện cho phần bù rủi ro vỡ nợ phản ánh mức rủi ro vỡ nợ cao hơn tương đối của Khoản đầu tư 5.

3. Tính giới hạn trên và giới hạn dưới cho mức lãi suất chưa biết của Khoản đầu tư 3, $r_3$.

###### **Lời giải (Solution):** 

Khoản đầu tư 3 có rủi ro thanh khoản và rủi ro vỡ nợ tương đương với Khoản đầu tư 2, nhưng với thời gian đáo hạn dài hơn, Khoản đầu tư 3 sẽ có phần bù kỳ hạn cao hơn và mang lại mức lãi suất cao hơn Khoản đầu tư 2. Do đó, lãi suất của Khoản đầu tư 3, $r_3$, phải cao hơn $2,5\%$ (lãi suất của Khoản đầu tư 2).

Nếu tính thanh khoản của Khoản đầu tư 3 là cao, Khoản đầu tư 3 sẽ giống với Khoản đầu tư 4 ngoại trừ việc Khoản đầu tư 3 có kỳ hạn ngắn hơn. Khi đó chúng ta sẽ kết luận rằng lãi suất của Khoản đầu tư 3 phải thấp hơn lãi suất của Khoản đầu tư 4, tức là $4\%$. Tuy nhiên, trái ngược với Khoản đầu tư 4, Khoản đầu tư 3 có tính thanh khoản thấp. Có khả năng lãi suất của Khoản đầu tư 3 vượt quá lãi suất của Khoản đầu tư 4 mặc dù Khoản đầu tư 3 có kỳ hạn ngắn hơn, tùy thuộc vào quy mô tương đối của phần bù thanh khoản và phần bù kỳ hạn. Tuy nhiên, chúng ta kỳ vọng $r_3$ sẽ thấp hơn $4,5\%$, là mức lãi suất dự kiến của Khoản đầu tư 4 nếu nó có tính thanh khoản thấp ($4\% + 0,5\%$, phần bù thanh khoản). Do đó, chúng ta kỳ vọng lãi suất của Khoản đầu tư 3 sẽ nằm trong khoảng từ $2,5\%$ đến $4,5\%$.

## **<mark>3</mark>** 

##### **TỶ SUẤT SINH LỢI (RATES OF RETURN)** 

tính toán và diễn giải các phương pháp đo lường tỷ suất sinh lợi khác nhau theo thời gian và mô tả các trường hợp sử dụng phù hợp của chúng

Các tài sản tài chính thường được xác định dựa trên các đặc điểm về tỷ suất sinh lợi (*return*) và rủi ro (*risk*) của chúng. Việc so sánh theo hai chiều hướng này giúp đơn giản hóa quá trình xây dựng một danh mục đầu tư từ tất cả các tài sản hiện có. Trong bài học này, chúng ta sẽ tính toán, đánh giá và so sánh các thước đo tỷ suất sinh lợi khác nhau.

Các tài sản tài chính thông thường tạo ra hai loại tỷ suất sinh lợi cho nhà đầu tư. Thứ nhất, chúng có thể mang lại thu nhập định kỳ (*periodic income*) thông qua cổ tức tiền mặt hoặc các khoản thanh toán tiền lãi. Thứ hai, giá của một tài sản tài chính có thể tăng hoặc giảm, dẫn đến lãi vốn (*capital gain*) hoặc lỗ vốn (*capital loss*).

Một số tài sản tài chính chỉ mang lại tỷ suất sinh lợi thông qua một trong hai cơ chế này. Ví dụ, các nhà đầu tư vào cổ phiếu không trả cổ tức chỉ thu được tỷ suất sinh lợi từ biến động giá. Các tài sản khác lại chỉ tạo ra thu nhập định kỳ. Ví dụ, các quỹ hưu trí phúc lợi xác định (*defined benefit pension plans*) và niên kim hưu trí (*retirement annuities*) thực hiện các khoản thanh toán thu nhập trong suốt cuộc đời của người thụ hưởng.

###### **Tỷ suất sinh lợi thời kỳ nắm giữ (Holding Period Return)** 

Tỷ suất sinh lợi có thể được đo lường trong một kỳ duy nhất (*single period*) hoặc qua nhiều kỳ (*multiple periods*). Tỷ suất sinh lợi một kỳ rất đơn giản vì chỉ có một cách duy nhất để tính toán chúng. Tuy nhiên, tỷ suất sinh lợi nhiều kỳ có thể được tính theo nhiều cách khác nhau và điều quan trọng là phải nhận thức được những sự khác biệt này để tránh nhầm lẫn.

<!-- PDF Page 17 -->

**Tỷ suất sinh lợi thời kỳ nắm giữ (*holding period return*)**, ký hiệu là $R$, là tỷ suất sinh lợi kiếm được từ việc nắm giữ một tài sản trong một khoảng thời gian xác định duy nhất. Khoảng thời gian này có thể là một ngày, một tuần, một tháng, năm năm, hoặc bất kỳ thời kỳ xác định nào. Nếu tài sản (ví dụ: trái phiếu, cổ phiếu) được mua ngày hôm nay, tại thời điểm ($t = 0$), với giá 100 và được bán sau đó, giả sử tại thời điểm ($t = 1$), với giá 105 mà không có cổ tức hay thu nhập nào khác, thì tỷ suất sinh lợi thời kỳ nắm giữ là $5\%$ $[(105 - 100)/100]$. Nếu tài sản đó đồng thời trả một khoản thu nhập là 2 đơn vị tại thời điểm ($t = 1$), thì tổng tỷ suất sinh lợi là $7\%$. Tỷ suất sinh lợi này có thể được tổng quát hóa và biểu diễn dưới dạng biểu thức toán học trong đó $P$ là giá và $I$ là thu nhập, như sau:

![](assets/Quantitative_method.pdf-0017-04.png)

$$R = \frac{(P_1 - P_0) + I_1}{P_0} \tag{1}$$

<!-- Formula Text: R  = (P 1 − P 0) + I 1 _ P 0 , (1) -->

trong đó chỉ số dưới (*subscript*) cho biết thời điểm của giá hoặc thu nhập; ($t = 0$) là thời điểm đầu kỳ; và ($t = 1$) là thời điểm cuối kỳ. Hai nhận xét sau đây là rất quan trọng:

- Chúng ta đã tính được mức lãi vốn là $5\%$ và lợi suất thu nhập (*income yield*) là $2\%$ trong ví dụ này. Để dễ minh họa, chúng ta đã giả định rằng thu nhập được thanh toán tại thời điểm $t = 1$. Nếu thu nhập được nhận trước thời điểm $t = 1$, tỷ suất sinh lợi thời kỳ nắm giữ của chúng ta có thể đã cao hơn nếu chúng ta tái đầu tư khoản thu nhập đó trong khoảng thời gian còn lại của kỳ.

- Tỷ suất sinh lợi có thể được biểu thị dưới dạng số thập phân ($0,07$), phân số ($7/100$), hoặc phần trăm ($7\%$). Tất cả đều tương đương nhau.

Tỷ suất sinh lợi thời kỳ nắm giữ có thể được tính cho một giai đoạn dài hơn một năm. Ví dụ, một nhà phân tích có thể cần tính tỷ suất sinh lợi thời kỳ nắm giữ ba năm từ ba mức tỷ suất sinh lợi hàng năm. Trong trường hợp đó, tỷ suất sinh lợi thời kỳ nắm giữ ba năm được tính bằng cách ghép lãi ba mức tỷ suất sinh lợi hàng năm đó:

$$R = [(1 + R_1) \times (1 + R_2) \times (1 + R_3)] - 1$$

trong đó $R_1$, $R_2$, và $R_3$ là ba mức tỷ suất sinh lợi hàng năm.

###### **Tỷ suất sinh lợi trung bình cộng (Arithmetic or Mean Return)** 

Hầu hết các tỷ suất sinh lợi thời kỳ nắm giữ được báo cáo dưới dạng tỷ suất sinh lợi hàng ngày, hàng tháng hoặc hàng năm. Khi các tài sản có tỷ suất sinh lợi qua nhiều thời kỳ nắm giữ, cần phải chuẩn hóa (*normalize*) các tỷ suất sinh lợi về một thời kỳ chung để dễ dàng so sánh và thấu hiểu. Có nhiều phương pháp khác nhau để tổng hợp tỷ suất sinh lợi qua nhiều thời kỳ nắm giữ. Phần còn lại của mục này trình bày các cách tính tỷ suất sinh lợi trung bình khác nhau và thảo luận về khả năng áp dụng của chúng.

Cách đơn giản nhất để tính một thước đo tóm tắt cho tỷ suất sinh lợi qua nhiều kỳ là lấy trung bình cộng đơn giản (*simple arithmetic average*) của các tỷ suất sinh lợi thời kỳ nắm giữ. Do đó, ba mức tỷ suất sinh lợi hàng năm là $-50\%$, $35\%$, và $27\%$ sẽ cho chúng ta mức trung bình là $4\%$ mỗi năm $= \left(\frac{-50\% + 35\% + 27\%}{3}\right)$. Tỷ suất sinh lợi trung bình cộng rất dễ tính toán và có các tính chất thống kê đã biết rõ.

Tổng quát, tỷ suất sinh lợi trung bình cộng (*arithmetic or mean return*) được ký hiệu là $\bar{R}_i$ và được cho bởi phương trình sau đây đối với tài sản $i$, trong đó $R_{it}$ là tỷ suất sinh lợi trong kỳ $t$ và $T$ là tổng số kỳ:

![](assets/Quantitative_method.pdf-0017-15.png)

$$\bar{R}_i = \frac{R_{i1} + R_{i2} + \dots + R_{i,T-1} + R_{iT}}{T} = \frac{1}{T} \sum_{t=1}^{T} R_{it} \tag{2}$$

<!-- Formula Text: _ R  i  = R i1 + R i2 + … + R i,T−1 + R iT ____________________ T =   1 _ T  ∑ t=1 T   R it. (2) -->

<!-- PDF Page 18 -->

###### **Tỷ suất sinh lợi trung bình nhân (Geometric Mean Return)** 

Tỷ suất sinh lợi trung bình cộng giả định rằng số tiền đầu tư vào đầu mỗi kỳ là như nhau. Tuy nhiên, trong một danh mục đầu tư, ngay cả khi không có dòng tiền đi vào hoặc đi ra khỏi danh mục thì số vốn gốc cũng thay đổi qua mỗi năm. Khoản thu nhập của năm trước phải được cộng vào giá trị đầu kỳ của khoản đầu tư trong năm tiếp theo — những khoản thu nhập này sẽ được “ghép lãi” (*compounded*) theo mức tỷ suất sinh lợi kiếm được trong năm tiếp theo đó. Chúng ta có thể sử dụng tỷ suất sinh lợi trung bình nhân (*geometric mean return*) để tính đến hiệu ứng ghép lãi của tỷ suất sinh lợi.

Tỷ suất sinh lợi trung bình nhân cung cấp một sự biểu diễn chính xác hơn về mức tăng trưởng giá trị danh mục đầu tư trong một khoảng thời gian nhất định so với tỷ suất sinh lợi trung bình cộng. Tổng quát, tỷ suất sinh lợi trung bình nhân được ký hiệu là $\bar{R}_{Gi}$ và được cho bởi phương trình sau đây đối với tài sản $i$:

![](assets/Quantitative_method.pdf-0018-07.png)

$$\bar{R}_{Gi} = \sqrt[T]{(1 + R_{i1}) \times (1 + R_{i2}) \times \dots \times (1 + R_{i,T-1}) \times (1 + R_{iT})} - 1 \tag{3}$$

<!-- Formula Text: _ R  Gi  = T √ _________________________________________ (1 + R i1) × (1 + R i2) × … × (1 + R i,T−1) × (1 + R iT)  − 1 (3) -->

![](assets/Quantitative_method.pdf-0018-08.png)

$$= \sqrt[T]{\prod_{t=1}^{T} (1 + R_{it})} - 1$$

<!-- Formula Text: = T √ ____________ ∏ t=1 T   (1 + R t)  − 1 , -->

trong đó $R_{it}$ là tỷ suất sinh lợi trong kỳ $t$ và $T$ là tổng số kỳ.

Trong ví dụ ở mục trước, chúng ta đã tính được trung bình cộng là $4,00\%$. Sử dụng Phương trình 3, chúng ta có thể tính tỷ suất sinh lợi trung bình nhân từ cùng ba mức tỷ suất sinh lợi hàng năm đó:

$$\bar{R}_{Gi} = \sqrt[3]{(1 - 0,50) \times (1 + 0,35) \times (1 + 0,27)} - 1 = -0,0500$$

Bảng 2 (*Exhibit 2*) cho thấy tỷ suất sinh lợi thực tế của mỗi năm và số dư vào cuối mỗi năm khi sử dụng tỷ suất sinh lợi thực tế.

**Bảng 2: Giá trị và Hiệu quả hoạt động của Danh mục đầu tư (Exhibit 2: Portfolio Value and Performance)** 

||**Tỷ suất sinh lợi thực tế trong năm (Actual Return for the Year) (%)**|**Số tiền cuối năm (Year-End Amount)**|**Số tiền cuối năm sử dụng TSSL trung bình cộng 4% (Year-End Amount Using Arithmetic Return of 4%)**|**Số tiền cuối năm sử dụng TSSL trung bình nhân −5% (Year-End Amount Using Geometric Return of −5%)**|
|---|---|---|---|---|
|Năm 0 (Year 0)||EUR 1,0000|EUR 1,0000|EUR 1,0000|
|Năm 1 (Year 1)|−50|0,5000|1,0400|0,9500|
|Năm 2 (Year 2)|35|0,6750|1,0816|0,9025|
|Năm 3 (Year 3)|27|0,8573|1,1249|0,8574|

Bắt đầu với khoản đầu tư ban đầu là $1,0000\text{ EUR}$, chúng ta sẽ có số dư là $0,8574\text{ EUR}$ vào cuối giai đoạn ba năm như được thể hiện ở cột thứ năm của Bảng 2. Lưu ý rằng chúng ta đã ghép lãi các tỷ suất sinh lợi bởi vì, trừ khi có quy định khác, chúng ta kiếm được tỷ suất sinh lợi dựa trên số dư tính đến cuối năm trước đó. Nghĩa là, chúng ta sẽ nhận được mức sinh lợi $35\%$ trong năm thứ hai dựa trên số dư vào cuối năm thứ nhất, vốn chỉ còn $0,5000\text{ EUR}$, chứ không phải số dư ban đầu là $1,0000\text{ EUR}$. Hãy so sánh số dư vào cuối giai đoạn ba năm được tính bằng tỷ suất sinh lợi trung bình nhân với số dư mà chúng ta sẽ tính được nếu sử dụng tỷ suất sinh lợi trung bình cộng hàng năm $4\%$ từ ví dụ trước đó. Giá trị cuối kỳ khi sử dụng tỷ suất sinh lợi trung bình cộng là $1,1249\text{ EUR}$ ($= 1,0000 \times 1,04^3$). Con số này lớn hơn nhiều so với số dư thực tế vào cuối Năm 3 là $0,8573\text{ EUR}$.

Nhìn chung, tỷ suất sinh lợi trung bình cộng bị chệch lên trên (*biased upward*) trừ khi từng mức tỷ suất sinh lợi thời kỳ nắm giữ cơ sở đều bằng nhau. Độ chệch trong tỷ suất sinh lợi trung bình cộng đặc biệt nghiêm trọng nếu các tỷ suất sinh lợi thời kỳ nắm giữ là sự pha trộn của cả mức sinh lợi dương và âm, như trong ví dụ này.

Bây giờ chúng ta sẽ xem xét ba ví dụ tính toán tỷ suất sinh lợi thời kỳ nắm giữ qua các khung thời gian khác nhau.

<!-- PDF Page 19 -->

###### **VÍ DỤ 2 (EXAMPLE 2)** 

###### **Tỷ suất sinh lợi thời kỳ nắm giữ (Holding Period Return)** 

1. Một nhà đầu tư đã mua 100 cổ phiếu của một công ty với giá $34,50\text{ USD}$ mỗi cổ phiếu vào đầu quý. Nếu nhà đầu tư bán toàn bộ số cổ phiếu đó với giá $30,50\text{ USD}$ mỗi cổ phiếu sau khi nhận được khoản thanh toán cổ tức trị giá $51,55\text{ USD}$ vào cuối quý, tỷ suất sinh lợi thời kỳ nắm giữ của nhà đầu tư _gần nhất_ với mức nào sau đây:

   - **A.** $-13,0\%$.

   - **B.** $-11,6\%$.

   - **C.** $-10,1\%$.

###### **Lời giải (Solution):** 

C là đáp án đúng. Áp dụng Phương trình 1 (trong văn bản gốc ghi Equation 2), tỷ suất sinh lợi thời kỳ nắm giữ là $-10,1\%$, được tính như sau:

$$R = \frac{3.050 - 3.450 + 51,55}{3.450} = -10,1\%$$

Tỷ suất sinh lợi thời kỳ nắm giữ bao gồm lợi suất cổ tức (*dividend yield*) là $1,49\%$ ($= 51,55 / 3.450$) và khoản lỗ vốn (*capital loss*) là $-11,59\%$ ($= -400 / 3.450$).

###### **VÍ DỤ 3 (EXAMPLE 3)** 

###### **Tỷ suất sinh lợi thời kỳ nắm giữ (Holding Period Return)** 

1. Một nhà phân tích thu thập được các mức tỷ suất sinh lợi hàng năm sau đây của một quỹ tương hỗ (*mutual fund*), được trình bày trong Bảng 3 (*Exhibit 3*).

###### **Bảng 3: Hiệu quả hoạt động của Quỹ tương hỗ, 20X8–20X0 (Exhibit 3: Mutual Fund Performance, 20X8–20X0)** 

|**Năm (Year)**|**Tỷ suất sinh lợi (Return) (%)**|
|---|---|
|20X8|14|
|20X9|−10|
|20X0|−2|

Tỷ suất sinh lợi thời kỳ nắm giữ của quỹ trong giai đoạn ba năm _gần nhất_ với mức nào sau đây:

- **A.** $0,18\%$.

- **B.** $0,55\%$.

- **C.** $0,67\%$.

###### **Lời giải (Solution):** 

B là đáp án đúng. Tỷ suất sinh lợi thời kỳ nắm giữ ba năm của quỹ là $0,55\%$, được tính như sau:

$$R = [(1 + R_1) \times (1 + R_2) \times (1 + R_3)] - 1$$

$$R = [(1 + 0,14)(1 - 0,10)(1 - 0,02)] - 1 = 0,0055 = 0,55\%$$

<!-- PDF Page 20 -->

###### **VÍ DỤ 4 (EXAMPLE 4)** 

###### **Tỷ suất sinh lợi trung bình nhân (Geometric Mean Return)** 

1. Một nhà phân tích quan sát thấy các mức tỷ suất sinh lợi hàng năm sau đây của một quỹ phòng hộ (*hedge fund*), được trình bày trong Bảng 4 (*Exhibit 4*).

**Bảng 4: Hiệu quả hoạt động của Quỹ phòng hộ, 20X8–20X0 (Exhibit 4: Hedge Fund Performance, 20X8–20X0)** 

|**Năm (Year)**|**Tỷ suất sinh lợi (Return) (%)**|
|---|---|
|20X8|22|
|20X9|−25|
|20X0|11|

Tỷ suất sinh lợi trung bình nhân của quỹ trong giai đoạn ba năm _gần nhất_ với mức nào sau đây:

- **A.** $0,52\%$.

- **B.** $1,02\%$.

- **C.** $2,67\%$.

**Lời giải (Solution):** 

A là đáp án đúng. Áp dụng công thức tỷ suất sinh lợi trung bình nhân, tỷ suất sinh lợi trung bình nhân của quỹ trong giai đoạn ba năm là $0,52\%$, được tính như sau:

$$\bar{R}_G = [(1 + 0,22)(1 - 0,25)(1 + 0,11)]^{(1/3)} - 1 = 1,0157^{(1/3)} - 1 = 0,0052 = 0,52\%$$

###### **VÍ DỤ 5 (EXAMPLE 5)** 

###### **Tỷ suất sinh lợi trung bình nhân và trung bình cộng (Geometric and Arithmetic Mean Returns)** 

1. Xét dữ liệu tỷ suất sinh lợi hàng năm của nhóm các quốc gia trong Bảng 5 (*Exhibit 5*).

**Bảng 5: Tỷ suất sinh lợi hàng năm từ Năm 1 đến Năm 3 của các Chỉ số Chứng khoán tại một số Quốc gia được chọn (Exhibit 5: Annual Returns for Years 1 to 3 for Selected Countries’ Stock Indexes)** 

||**Tỷ suất sinh lợi 52 tuần (52-Week Return) (%)**|||**Tỷ suất sinh lợi trung bình 3 năm (Average 3-Year Return) (%)**||
|---|---|---|---|---|---|
|**Chỉ số (Index)**|**Năm 1 (Year 1)**|**Năm 2 (Year 2)**|**Năm 3 (Year 3)**|**Trung bình cộng (Arithmetic)**|**Trung bình nhân (Geometric)**|
|Quốc gia A (Country A)|−15,6|−5,4|6,1|−4,97|−5,38|
|Quốc gia B (Country B)|7,8|6,3|−1,5|4,20|4,12|
|Quốc gia C (Country C)|5,3|1,2|3,5|3,33|3,32|
|Quốc gia D (Country D)|−2,4|−3,1|6,2|0,23|0,15|
|Quốc gia E (Country E)|−4,0|−3,0|3,0|−1,33|−1,38|
|Quốc gia F (Country F)|5,4|5,2|−1,0|3,20|3,16|
|Quốc gia G (Country G)|12,7|6,7|−1,2|6,07|5,91|
|Quốc gia H (Country H)|3,5|4,3|3,4|3,73|3,73|
|Quốc gia I (Country I)|6,2|7,8|3,2|5,73|5,72|

<!-- PDF Page 21 -->

||**Tỷ suất sinh lợi 52 tuần (52-Week Return) (%)**|||**Tỷ suất sinh lợi trung bình 3 năm (Average 3-Year Return) (%)**||
|---|---|---|---|---|---|
|**Chỉ số (Index)**|**Năm 1 (Year 1)**|**Năm 2 (Year 2)**|**Năm 3 (Year 3)**|**Trung bình cộng (Arithmetic)**|**Trung bình nhân (Geometric)**|
|Quốc gia J (Country J)|8,1|4,1|−0,9|3,77|3,70|
|Quốc gia K (Country K)|11,5|3,4|1,2|5,37|5,28|

Hãy tính tỷ suất sinh lợi trung bình cộng và trung bình nhân trong ba năm cho ba chỉ số chứng khoán sau đây: Quốc gia D, Quốc gia E, và Quốc gia F.

**Lời giải (Solution):** 

Tỷ suất sinh lợi trung bình cộng như sau:

||**Tỷ suất sinh lợi hàng năm (Annual Return) (%)**|||**Tổng (Sum)**|**Tỷ suất sinh lợi trung bình cộng (Arithmetic Mean Return) (%)**|
|---|---|---|---|---|---|
||**Năm 1 (Year 1)**|**Năm 2 (Year 2)**|**Năm 3 (Year 3)**|$\sum_{i=1}^{3} R_i$||
|Quốc gia D (Country D)|−2,4|−3,1|6,2|0,7|0,233|
|Quốc gia E (Country E)|−4,0|−3,0|3,0|−4,0|−1,333|
|Quốc gia F (Country F)|5,4|5,2|−1,0|9,6|3,200|

Tỷ suất sinh lợi trung bình nhân như sau:

||**1 + TSSL dưới dạng thập phân $(1 + R_t)$**|||**Tích (Product)**|**Căn bậc 3 (3rd Root)**|**Tỷ suất sinh lợi trung bình nhân (Geometric mean return) (%)**|
|---|---|---|---|---|---|---|
||**Năm 1 (Year 1)**|**Năm 2 (Year 2)**|**Năm 3 (Year 3)**|$\prod_{t=1}^{T} (1 + R_t)$|$\left[\prod_{t=1}^{T} (1 + R_t)\right]^{1/3}$||
|Quốc gia D (Country D)|0,976|0,969|1,062|1,00438|1,00146|0,146|
|Quốc gia E (Country E)|0,960|0,970|1,030|0,95914|0,98619|−1,381|
|Quốc gia F (Country F)|1,054|1,052|0,990|1,09772|1,03157|3,157|

Trong Ví dụ 5, tỷ suất sinh lợi trung bình nhân nhỏ hơn tỷ suất sinh lợi trung bình cộng đối với tỷ suất sinh lợi chỉ số của từng quốc gia. Trên thực tế, trung bình nhân luôn nhỏ hơn hoặc bằng trung bình cộng với một ngoại lệ duy nhất: hai số trung bình này sẽ bằng nhau khi không có sự biến thiên (*variability*) giữa các quan sát — nghĩa là khi tất cả các quan sát trong chuỗi đều có giá trị như nhau.

Nhìn chung, sự chênh lệch giữa trung bình cộng và trung bình nhân tăng lên cùng với mức độ biến thiên trong mẫu; các quan sát càng phân tán thì chênh lệch giữa trung bình cộng và trung bình nhân càng lớn. Quan sát sơ bộ các tỷ suất sinh lợi trong Bảng 5 và biểu đồ các giá trị trung bình tương ứng trong Bảng 6 (*Exhibit 6*) cho thấy mức độ biến thiên lớn hơn ở chỉ số của Quốc gia A so với các chỉ số khác, và điều này được xác nhận qua độ lệch lớn hơn của tỷ suất sinh lợi trung bình nhân ($-5,38\%$) so với tỷ suất sinh lợi trung bình cộng ($-4,97\%$). Nhà phân tích nên diễn giải những kết quả này như thế nào?

<!-- PDF Page 22 -->

**Bảng 6: Tỷ suất sinh lợi trung bình cộng và trung bình nhân của Chỉ số Chứng khoán các Quốc gia, Năm 1 đến Năm 3 (Exhibit 6: Arithmetic and Geometric Mean Returns for Country Stock Indexes, Years 1 to 3)** 

![](assets/Quantitative_method.pdf-0022-04.png)

<!-- Picture Text: Country<br>A<br>B<br>C<br>D<br>E<br>F<br>G<br>H<br>I<br>J<br>K<br>6 –4 –2 0 2 4 6 8<br>Mean Return (%)<br>Geometric Mean Arithmetic Average<br> -->
> **Chú thích hình ảnh:** Trục tung hiển thị các Quốc gia (*Country*) từ A đến K; trục hoành hiển thị Tỷ suất sinh lợi trung bình (*Mean Return (%)*) từ $-6\%$ đến $8\%$; các thanh biểu diễn Trung bình nhân (*Geometric Mean*) và Trung bình cộng (*Arithmetic Average*).

Tỷ suất sinh lợi trung bình nhân đại diện cho tốc độ tăng trưởng (*growth rate*) hay tỷ suất sinh lợi kép (*compound rate of return*) của một khoản đầu tư. Một đơn vị tiền tệ được đầu tư vào một quỹ mô phỏng chỉ số của Quốc gia B vào đầu Năm 1 sẽ tăng trưởng thành $(1,078)(1,063)(0,985) = 1,128725$ đơn vị tiền tệ, bằng với 1 cộng với tỷ suất sinh lợi trung bình nhân của Quốc gia B là $4,1189\%$ được ghép lãi qua ba kỳ: $[1 + 0,041189]^3 = 1,128725$. Phép toán này xác nhận rằng trung bình nhân chính là tỷ suất sinh lợi kép. Với trọng tâm là tỷ suất sinh lợi thực tế của một khoản đầu tư qua khung thời gian nhiều kỳ, trung bình nhân là mối quan tâm hàng đầu của các nhà đầu tư. Tỷ suất sinh lợi trung bình cộng, tập trung vào hiệu quả hoạt động trung bình của một kỳ đơn lẻ, cũng được quan tâm. Cả trung bình cộng và trung bình nhân đều đóng vai trò nhất định trong quản lý đầu tư, và cả hai thường được báo cáo cho các chuỗi tỷ suất sinh lợi.

Để báo cáo tỷ suất sinh lợi lịch sử, trung bình nhân có sức hấp dẫn đáng kể bởi vì nó là tốc độ tăng trưởng hay tỷ suất sinh lợi mà chúng ta phải kiếm được mỗi năm để khớp với hiệu quả đầu tư tích lũy thực tế. Giả sử chúng ta mua một cổ phiếu với giá $100\text{ EUR}$ và hai năm sau nó có giá trị là $100\text{ EUR}$, với năm ở giữa đạt mức giá $200\text{ EUR}$. Trung bình nhân bằng $0\%$ rõ ràng là tốc độ tăng trưởng kép trong suốt hai năm đó, điều mà chúng ta có thể xác nhận bằng cách ghép lãi các tỷ suất sinh lợi: $[(1 + 1,00)(1 - 0,50)]^{1/2} - 1 = 0\%$. Cụ thể, số tiền cuối kỳ bằng số tiền đầu kỳ nhân với $(1 + \bar{R}_G)^2$.

Tuy nhiên, trung bình cộng, bằng $[100\% + (-50\%)]/2 = 25\%$ trong ví dụ trước, có thể làm sai lệch đánh giá của chúng ta về hiệu quả hoạt động lịch sử. Như chúng ta đã lưu ý, trung bình cộng luôn lớn hơn hoặc bằng trung bình nhân. Nếu chúng ta muốn ước tính tỷ suất sinh lợi trung bình cho khung thời gian một kỳ (*one-period horizon*), chúng ta nên sử dụng trung bình cộng bởi vì trung bình cộng là mức trung bình của các tỷ suất sinh lợi một kỳ. Tuy nhiên, nếu chúng ta muốn ước tính tỷ suất sinh lợi trung bình qua nhiều hơn một kỳ, chúng ta nên sử dụng trung bình nhân của các tỷ suất sinh lợi bởi vì trung bình nhân nắm bắt được cách thức mà tổng tỷ suất sinh lợi được liên kết với nhau theo thời gian.

###### **Trung bình điều hòa (The Harmonic Mean)** 

**Trung bình điều hòa (*harmonic mean*)**, ký hiệu là $\bar{X}_H$, là một thước đo xu hướng trung tâm (*measure of central tendency*) khác. Trung bình điều hòa phù hợp trong những trường hợp mà biến số là một tốc độ (*rate*) hoặc một tỷ số (*ratio*). Thuật ngữ “điều hòa” (*harmonic*) xuất phát từ việc sử dụng một dạng chuỗi bao gồm các số nghịch đảo được gọi là chuỗi điều hòa (*harmonic series*).

<!-- PDF Page 23 -->

**Công thức Trung bình điều hòa (Harmonic Mean Formula).** Trung bình điều hòa của một tập hợp các quan sát $X_1, X_2, \dots, X_n$ là:

![](assets/Quantitative_method.pdf-0023-04.png)

$$\bar{X}_H = \frac{n}{\sum_{i=1}^{n} (1 / X_i)} \tag{4}$$

<!-- Formula Text: _ X  H  = n _ ∑ i=1 n (1 / X i) , (4) -->

với $X_i > 0$ cho $i = 1, 2, \dots, n$.

Trung bình điều hòa là giá trị thu được bằng cách tính tổng các số nghịch đảo của các quan sát,

![](assets/Quantitative_method.pdf-0023-07.png)

$$\sum_{i=1}^{n} (1 / X_i)$$

<!-- Formula Text: ∑ i=1 n (1 / X i), -->

tức các số hạng có dạng $1/X_i$, sau đó lấy trung bình của tổng đó bằng cách chia cho số lượng quan sát, $n$, và cuối cùng là lấy số nghịch đảo của mức trung bình đó,

![](assets/Quantitative_method.pdf-0023-09.png)

<!-- Formula Text: n -->

![](assets/Quantitative_method.pdf-0023-10.png)

$$\frac{n}{\sum_{i=1}^{n} (1 / X_i)}$$

<!-- Formula Text: _ ∑ i=1 n (1 / X i) . -->

Trung bình điều hòa có thể được xem là một dạng đặc biệt của trung bình có trọng số (*weighted mean*), trong đó trọng số của một quan sát tỷ lệ nghịch với độ lớn của nó. Ví dụ, nếu có một mẫu gồm các quan sát 1, 2, 3, 4, 5, 6, và 1.000, trung bình điều hòa sẽ là $2,8560$. So với trung bình cộng là $145,8571$, chúng ta thấy ảnh hưởng của giá trị ngoại lai (*outlier* — con số 1.000) nhỏ hơn rất nhiều so với trường hợp của trung bình cộng. Vì vậy, trung bình điều hòa khá hữu ích khi làm thước đo xu hướng trung tâm trong trường hợp có sự hiện diện của các giá trị ngoại lai.

Trung bình điều hòa được sử dụng thường xuyên nhất khi dữ liệu bao gồm các tốc độ và tỷ số, chẳng hạn như hệ số P/E (*Price-to-Earnings ratio*). Giả sử ba công ty cùng ngành (*peer companies*) có P/E lần lượt là 45, 15, và 15. Trung bình cộng là 25, nhưng trung bình điều hòa, vốn đặt ít trọng số hơn vào mức P/E bằng 45, là $19,3$.

Trung bình điều hòa là một khái niệm tương đối chuyên biệt về giá trị trung bình, phù hợp để tính trung bình các tỷ số (“số lượng trên mỗi đơn vị”) khi các tỷ số này được áp dụng lặp đi lặp lại cho một lượng cố định để tạo ra một số lượng đơn vị biến thiên. Khái niệm này được giải thích rõ nhất thông qua một ví dụ minh họa. Một ứng dụng nổi tiếng phát sinh trong chiến lược đầu tư được gọi là **trung bình giá vốn (*cost averaging*)**, bao gồm việc đầu tư định kỳ một số tiền cố định. Trong ứng dụng này, các tỷ số mà chúng ta đang tính trung bình là giá mỗi cổ phiếu tại các ngày mua khác nhau, và chúng ta đang áp dụng các mức giá đó cho một số tiền không đổi để thu về một số lượng cổ phiếu biến thiên. Minh họa về việc áp dụng trung bình điều hòa vào chiến lược trung bình giá vốn được cung cấp trong Ví dụ 6.

###### **VÍ DỤ 6 (EXAMPLE 6)** 

###### **Trung bình giá vốn và Trung bình điều hòa (Cost Averaging and the Harmonic Mean)** 

1. Giả sử một nhà đầu tư đầu tư $1.000\text{ EUR}$ mỗi tháng vào một cổ phiếu cụ thể trong $n = 2$ tháng. Giá cổ phiếu lần lượt là $10\text{ EUR}$ và $15\text{ EUR}$ tại hai ngày mua. Mức giá trung bình đã trả cho chứng khoán này là bao nhiêu?

###### **Lời giải (Solution):** 

Giao dịch mua trong tháng thứ nhất $= \text{1.000 EUR} / \text{10 EUR} = 100\text{ cổ phiếu}$.

Giao dịch mua trong tháng thứ hai $= \text{1.000 EUR} / \text{15 EUR} = 66,67\text{ cổ phiếu}$.

Nhà đầu tư đã mua tổng cộng $166,67\text{ cổ phiếu}$ với số tiền $2.000\text{ EUR}$, vì vậy mức giá trung bình đã trả cho mỗi cổ phiếu là $\text{2.000 EUR} / 166,67 = \text{12 EUR}$. Mức giá trung bình đã trả trên thực tế chính là trung bình điều hòa của giá tài sản tại các ngày mua. Sử dụng Phương trình 4 (trong bản gốc ghi Equation 5), mức giá trung bình điều hòa là $2 / [(1/10) + (1/15)] = \text{12 EUR}$. Giá trị $12\text{ EUR}$ này thấp hơn mức giá mua trung bình cộng $(\text{10 EUR} + \text{15 EUR})/2 = \text{12,5 EUR}$.

<!-- PDF Page 24 -->

Bởi vì cùng sử dụng một dữ liệu nhưng liên quan đến các cấp số khác nhau trong phép tính tương ứng, nên trung bình cộng, trung bình nhân và trung bình điều hòa có mối liên hệ toán học với nhau. Chúng ta sẽ không đi sâu vào phần chứng minh mối quan hệ này, nhưng kết quả cơ bản như sau:

$$\text{Trung bình cộng} \times \text{Trung bình điều hòa} = (\text{Trung bình nhân})^2$$

*(Tiếng Anh: $\text{Arithmetic mean} \times \text{Harmonic mean} = (\text{Geometric mean})^2$)*

Trừ khi tất cả các quan sát trong tập dữ liệu đều có cùng một giá trị, trung bình điều hòa luôn nhỏ hơn trung bình nhân, và đến lượt mình, trung bình nhân luôn nhỏ hơn trung bình cộng.

Trung bình điều hòa chỉ áp dụng được cho các số không âm, vì vậy khi làm việc với các tỷ suất sinh lợi được biểu thị dưới dạng phần trăm dương hoặc âm, trước tiên chúng ta chuyển đổi các tỷ suất sinh lợi sang định dạng ghép lãi, giả định có tái đầu tư, dưới dạng $(1 + R)$, giống như đã làm trong phép tính tỷ suất sinh lợi trung bình nhân, sau đó tính $(1 + \text{trung bình điều hòa})$, rồi trừ đi 1 để thu được tỷ suất sinh lợi trung bình điều hòa.

###### **VÍ DỤ 7 (EXAMPLE 7)** 

###### **Tính Trung bình cộng, Trung bình nhân và Trung bình điều hòa cho hệ số P/E (Calculating the Arithmetic, Geometric, and Harmonic Means for P/Es)** 

Mỗi năm vào tháng 12, một nhà phân tích chứng khoán lựa chọn 10 cổ phiếu ưa thích nhất của mình cho năm tiếp theo. Bảng 7 (*Exhibit 7*) trình bày hệ số P/E, tỷ số giữa giá cổ phiếu trên thu nhập dự phóng mỗi cổ phiếu (*projected earnings per share – EPS*), cho 10 lựa chọn cổ phiếu hàng đầu của cô ấy cho năm tới.

**Bảng 7: 10 Cổ phiếu ưa thích nhất của Nhà phân tích cho Năm tới (Exhibit 7: Analyst’s 10 Favorite Stocks for Next Year)** 

|**Cổ phiếu (Stock)**|**P/E**|
|---|---|
|Cổ phiếu 1 (Stock 1)|22,29|
|Cổ phiếu 2 (Stock 2)|15,54|
|Cổ phiếu 3 (Stock 3)|9,38|
|Cổ phiếu 4 (Stock 4)|15,12|
|Cổ phiếu 5 (Stock 5)|10,72|
|Cổ phiếu 6 (Stock 6)|14,57|
|Cổ phiếu 7 (Stock 7)|7,20|
|Cổ phiếu 8 (Stock 8)|7,97|
|Cổ phiếu 9 (Stock 9)|10,34|
|Cổ phiếu 10 (Stock 10)|8,35|

1. Tính P/E trung bình cộng cho 10 cổ phiếu này.

###### **Lời giải (Solution):** 

Trung bình cộng được tính như sau:

$$121,48 / 10 = 12,1480$$

2. Tính P/E trung bình điều hòa cho 10 cổ phiếu này.

###### **Lời giải (Solution):** 

Trung bình điều hòa được tính như sau:

![](assets/Quantitative_method.pdf-0024-19.png)

$$\bar{X}_H = \frac{n}{\sum_{i=1}^{n} (1 / X_i)}$$

$$\bar{X}_H = \frac{10}{\left(\frac{1}{22,29}\right) + \left(\frac{1}{15,54}\right) + \dots + \left(\frac{1}{10,34}\right) + \left(\frac{1}{8,35}\right)}$$

<!-- Picture Text: X  _ H  =   _ n n  ,<br>∑ i =1(1 /  Xi )<br>_ _______________________________10<br>X H  =   _ _ _ _<br>(22.29 1 ) +  ( 15.54 1 ) + … + ( 10.34 1 ) +  ( 8.35 1 ) ,<br> -->

<!-- PDF Page 25 -->

$$\bar{X}_H = 10 / 0,9247 = 10,8142$$

Trong tài chính, trung bình điều hòa có trọng số (*weighted harmonic mean*) được sử dụng khi tính trung bình các tốc độ và các bội số định giá (*multiples*) khác, chẳng hạn như hệ số P/E, bởi vì trung bình điều hòa gán trọng số bằng nhau cho mỗi điểm dữ liệu và làm giảm ảnh hưởng của các giá trị ngoại lai. Các phép tính này có thể được thực hiện bằng Excel:

- Để tính trung bình cộng hay tỷ suất sinh lợi trung bình, có thể sử dụng hàm `=AVERAGE(return1, return2, …)`.

- Để tính tỷ suất sinh lợi trung bình nhân, có thể sử dụng hàm `=GEOMEAN(return1, return2, …)`.

- Để tính tỷ suất sinh lợi trung bình điều hòa, có thể sử dụng hàm `=HARMEAN(return1, return2, …)`.

Ngoài trung bình cộng, trung bình nhân và trung bình điều hòa, hai loại số trung bình khác cũng có thể được sử dụng. Cả trung bình cắt bỏ ngoại lai (*trimmed mean*) và trung bình làm mượt ngoại lai (*winsorized mean*) đều tìm cách giảm thiểu tác động của các giá trị ngoại lai trong một tập dữ liệu. Cụ thể, **trung bình cắt bỏ ngoại lai (*trimmed mean*)** loại bỏ một tỷ lệ phần trăm nhỏ đã xác định của các giá trị lớn nhất và nhỏ nhất khỏi tập dữ liệu chứa các quan sát của chúng ta trước khi tính giá trị trung bình bằng cách lấy trung bình cộng của các quan sát còn lại.

Trung bình làm mượt ngoại lai thay thế các quan sát cực đoan trong tập dữ liệu nhằm hạn chế tác động của các giá trị ngoại lai lên phép tính. **Trung bình làm mượt ngoại lai (*winsorized mean*)** được tính sau khi thay thế các giá trị cực đoan ở cả hai đầu bằng giá trị của các quan sát gần chúng nhất, rồi sau đó tính giá trị trung bình bằng cách lấy trung bình cộng của các quan sát còn lại.

Tuy nhiên, câu hỏi cốt lõi là: Nên sử dụng loại số trung bình nào trong hoàn cảnh nào? Việc lựa chọn sử dụng số trung bình nào phụ thuộc vào nhiều yếu tố, như chúng tôi mô tả trong Bảng 8 (*Exhibit 8*):

- Có các giá trị ngoại lai mà chúng ta muốn đưa vào tính toán hay không?

- Phân phối có đối xứng hay không?

- Có hiệu ứng ghép lãi hay không?

- Có các giá trị ngoại lai cực đoan hay không?

<!-- PDF Page 26 -->

###### **Bảng 8: Quyết định sử dụng thước đo nào (Exhibit 8: Deciding Which Measure to Use)** 

![](assets/Quantitative_method.pdf-0026-04.png)

<!-- Picture Text: Collect Sample<br>Include all<br>Yes<br>values,<br>Arithmetic Mean<br>including<br>outliers?<br>Yes<br>Compounding? Geometric Mean<br>Extreme Yes Harmonic mean,<br>Trimmed mean,<br>outliers?<br>Winsorized mean<br> -->
> **Chú thích hình ảnh (Sơ đồ quyết định):**
> - **Thu thập mẫu (*Collect Sample*)**:
>   - Có tính đến hiệu ứng ghép lãi không (*Compounding*)? $\rightarrow$ Nếu **Có (*Yes*)**: Sử dụng **Trung bình nhân (*Geometric Mean*)**.
>   - Đưa vào tất cả các giá trị, bao gồm cả giá trị ngoại lai (*Include all values, including outliers*)? $\rightarrow$ Nếu **Có (*Yes*)**: Sử dụng **Trung bình cộng (*Arithmetic Mean*)**.
>   - Có các giá trị ngoại lai cực đoan không (*Extreme outliers*)? $\rightarrow$ Nếu **Có (*Yes*)**: Sử dụng **Trung bình điều hòa (*Harmonic mean*)**, **Trung bình cắt bỏ ngoại lai (*Trimmed mean*)**, hoặc **Trung bình làm mượt ngoại lai (*Winsorized mean*)**.

###### **BỘ CÂU HỎI (QUESTION SET)** 

Một quỹ có các mức tỷ suất sinh lợi trong 10 năm qua như sau:

**Bảng 9: Tỷ suất sinh lợi trong 10 năm (Exhibit 9: 10-Year Returns)** 

|**Năm (Year)**|**Tỷ suất sinh lợi (Return)**|
|---|---|
|1|4,5%|
|2|6,0%|
|3|1,5%|
|4|−2,0%|
|5|0,0%|
|6|4,5%|
|7|3,5%|
|8|2,5%|
|9|5,5%|
|10|4,0%|

1. Tỷ suất sinh lợi trung bình cộng trong 10 năm _gần nhất_ với mức nào sau đây:

   - **A.** $2,97\%$.
   - **B.** $3,00\%$.
   - **C.** $3,33\%$.

   - **Lời giải (Solution):** 

B là đáp án đúng. Tỷ suất sinh lợi trung bình cộng được tính như sau:
*(Xem tiếp phần lời giải ở đầu Phần 2/3)*
