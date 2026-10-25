# Tập 6: Chứng khoán Thu nhập Cố định (Fixed Income)
## Learning Module 7 Yield and Yield Spread Measures for Fixed-Rate Bonds (Trang PDF 167–196)

---

# Tập 6: Chứng Khoán Thu Nhập Cố Định (*Fixed Income*)
## Học phần 7: Các Thước Đo Lợi Suất và Chênh Lệch Lợi Suất Cho Trái Phiếu Lãi Suất Cố Định (*Yield and Yield Spread Measures for Fixed-Rate Bonds*)
### Phần 1/2: Giới thiệu (Trang PDF 167–182)

---

<!-- PDF Page 167 -->

#### H Ọ C P H Ầ N

# **<mark>7</mark>**

### **Các Thước Đo Lợi Suất và Chênh Lệch Lợi Suất Cho Trái Phiếu Lãi Suất Cố Định (*Yield and Yield Spread Measures for Fixed-Rate Bonds*)**

###### **<mark>MỤC TIÊU HỌC TẬP (*LEARNING OUTCOMES*)</mark>**

**_Mức độ thành thạo — Ứng viên cần có khả năng:_**
- tính toán lợi suất hàng năm trên một trái phiếu cho các số kỳ ghép lãi (*compounding periods*) khác nhau trong một năm
- so sánh, tính toán và diễn giải các thước đo lợi suất (*yield measures*) và chênh lệch lợi suất (*yield spread measures*) cho trái phiếu lãi suất cố định

##### **GIỚI THIỆU (*INTRODUCTION*)**

**<mark>1</mark>**

Các bài học trước đã minh họa mối quan hệ giữa giá trái phiếu và lợi suất đáo hạn (*yields-to-maturity* – YTMs), cũng như các đặc tính khác, chẳng hạn như lãi suất coupon và thời gian đáo hạn. Hai yếu tố cần cân nhắc quan trọng để diễn giải và xác định lợi suất đáo hạn cùng các thước đo lợi suất khác là tần suất ghép lãi giả định (*assumed frequency of compounding interest*) và sự hiện diện của các quyền chọn đi kèm (*embedded options*) có thể làm ảnh hưởng đến quy mô hoặc thời điểm của dòng tiền. Học phần này khám phá những yếu tố đó và mở rộng việc phân tích lợi suất bằng cách giới thiệu các thước đo chênh lệch lợi suất (*spread measures*), dùng để so sánh lợi suất với các lãi suất chuẩn (*benchmark rates*) nhằm xác định mức độ đền bù mà một nhà đầu tư nhận được khi chấp nhận những rủi ro nhất định.

Hầu hết các ví dụ và bảng minh họa được sử dụng xuyên suốt bài đọc này có thể được tải xuống dưới dạng sổ làm việc Microsoft Excel. Mỗi trang tính trong sổ làm việc được gắn nhãn với số thứ tự ví dụ hoặc bảng minh họa tương ứng trong bài học.

###### **TỔNG QUAN HỌC PHẦN (*LEARNING MODULE OVERVIEW*)**

- Lợi suất đáo hạn (*yields-to-maturity*) cho phép các chuyên viên phân tích sử dụng một thước đo đơn nhất để so sánh các trái phiếu có kỳ hạn và lãi suất coupon khác nhau. Một yếu tố quan trọng trong việc xác định và diễn giải lợi suất là tần suất ghép lãi (*frequency of compounding*), được gọi là số kỳ ghép lãi trong năm (*periodicity*).

- Khi các yếu tố khác không đổi, việc ghép lãi thường xuyên hơn sẽ dẫn đến giá trị tương lai hoặc tỷ suất sinh lợi lớn hơn. Do đó, việc ghép lãi thường xuyên hơn ở một mức lãi suất thấp hơn có thể tương đương với việc ghép lãi ít thường xuyên hơn ở một mức lãi suất cao hơn; việc ghép lãi thường xuyên hơn đã bù đắp cho mức lãi suất thấp hơn đó.

<!-- PDF Page 168 -->

- Giá và lợi suất của các trái phiếu có quyền chọn đi kèm (*embedded options*) đòi hỏi phải có sự điều chỉnh để phản ánh giá trị của quyền chọn. Chênh lệch lợi suất đã điều chỉnh quyền chọn (*option-adjusted yield spread*) và lợi suất thấp nhất có thể (*yield-to-worst*) là các thước đo phản ánh giá trị quyền chọn.

- Các thước đo lợi suất của một trái phiếu, cũng như những thay đổi trong chúng, có thể được phân tách thành một lãi suất chuẩn (*benchmark rate*) và một mức chênh lệch (*spread*) so với lãi suất chuẩn đó. Lãi suất chuẩn phản ánh các điều kiện kinh tế vĩ mô “từ trên xuống” (*“top-down”*) tác động đến tất cả các trái phiếu trên thị trường, trong khi mức chênh lệch nắm bắt các yếu tố đặc thù của tổ chức phát hành “từ dưới lên” (*“bottom-up”*), chẳng hạn như rủi ro tín dụng, thanh khoản và thuế.

- Tương tự như cách đường cong lợi suất (*yield curve*) biểu diễn bằng đồ thị mối quan hệ giữa lợi suất đáo hạn và thời gian đáo hạn đối với các chứng khoán có cùng hồ sơ rủi ro, lãi suất chuẩn và các mức chênh lệch lợi suất cũng có thể được vẽ đồ thị theo thời gian đáo hạn nhằm thể hiện cấu trúc kỳ hạn của chênh lệch tín dụng (*term structure of credit spreads*).

###### **TỰ ĐÁNH GIÁ HỌC PHẦN (*LEARNING MODULE SELF-ASSESSMENT*)**

Các câu hỏi ban đầu này nhằm giúp bạn đánh giá mức độ hiểu biết hiện tại của mình về học phần này.

1. Hoàn thành các câu sau bằng cách điền vào chỗ trống sử dụng các từ sau đây:

   - quy đổi theo năm (*annualized*)
   - ghép lãi (*compounded*)
   - chuẩn hóa (*standardized*)

Cả lợi suất của chứng khoán thị trường vốn và lãi suất thị trường tiền tệ có ngày đáo hạn ngắn hơn một năm đều được _________________. Tuy nhiên, lãi suất thị trường tiền tệ không được ________________.

###### **Lời giải:**

Cả lợi suất của chứng khoán thị trường vốn và lãi suất thị trường tiền tệ có ngày đáo hạn ngắn hơn một năm đều được quy đổi theo năm (*annualized*). Tuy nhiên, lãi suất thị trường tiền tệ không được ghép lãi (*compounded*).

2. Một trái phiếu chính phủ trung ương kỳ hạn 3 năm không kèm quyền mua lại trước hạn được định giá ở mức 106,24 trên mỗi 100 đơn vị mệnh giá. Trái phiếu trả lãi coupon bán niên 2%/năm. Lợi suất đáo hạn hàng năm của trái phiếu này gần nhất với:

   - **A.** –0,077% (trong đề gốc thiếu dấu trừ ở phương án A và B, lời giải tính ra –0,077%).

   - **B.** –0,039%.

   - **C.** 1,883%.

###### **Lời giải:**

A là đáp án đúng. Vì trái phiếu trả lãi coupon bán niên, lợi suất đáo hạn bán niên được tính bằng cách giải tìm $r$ trong phương trình sau đây. Ngoài ra, có thể sử dụng hàm `IRR` hoặc `YIELD` trong Microsoft Excel và Google Sheets.

<!-- PDF Page 169 -->

![](assets/Fixed_Income.pdf-0169-03.png)

<!-- Formula Text: 106.24  = 1 _ (1 + r) 1  + 1 _ (1 + r) 2  + 1 _ (1 + r) 3  + 1 _ (1 + r) 4  + 1 _ (1 + r) 5  +   101 _ (1 + r) 6 . r  =  − 0.00038596. -->
$$106{,}24 = \frac{1}{(1 + r)^1} + \frac{1}{(1 + r)^2} + \frac{1}{(1 + r)^3} + \frac{1}{(1 + r)^4} + \frac{1}{(1 + r)^5} + \frac{101}{(1 + r)^6}$$
$$r = -0{,}00038596$$

Vì lợi suất được biểu thị theo kỳ bán niên, nó cần được quy đổi theo năm bằng cách nhân với 2, dẫn đến kết quả là $-0{,}000772$, hay $-0{,}077\%$.

B không đúng vì đó là lợi suất bán niên, chứ không phải lợi suất năm.

C không đúng vì 1,883% là lợi suất hiện hành (*current yield*) của trái phiếu, chứ không phải lợi suất đáo hạn.

3. Một chuyên viên phân tích thu nhập cố định thu thập được dữ liệu sau đây cho ba trái phiếu doanh nghiệp có cùng ngày đáo hạn. Lãi suất chuẩn trái phiếu chính phủ có liên quan, được tính trên cơ sở tương đương trái phiếu bán niên (*semiannual bond equivalent basis*), là 1,10%. Hãy tính mức chênh lệch G (*G-spread*) cho mỗi trái phiếu.

||**Trái phiếu A (*Bond A*)**|**Trái phiếu B (*Bond B*)**|**Trái phiếu C (*Bond C*)**|
|---|---|---|---|
|Lợi suất đáo hạn (*Yield-to-maturity*)|1,271%|1,213%|1,178%|
|Tần suất coupon và số kỳ ghép lãi giả định (*Coupon frequency and assumed periodicity*)|Hàng năm (*Annual*)|Bán niên (*Semiannual*)|Hàng quý (*Quarterly*)|

###### **Lời giải:**

G-spread của Trái phiếu B là $(0{,}01213 - 0{,}011) = 11{,}3\text{ bps}$.

Trước khi tính G-spread cho Trái phiếu A và C, lợi suất đáo hạn của chúng trước tiên phải được chuyển đổi sang số kỳ ghép lãi trong năm là 2 (*periodicity of two*). Lợi suất tương đương bán niên của Trái phiếu A là 1,267%:

![](assets/Fixed_Income.pdf-0169-12.png)

<!-- Formula Text: (1 + AP R m _ m  ) m =  (1 + AP R n _ n  ) n . (1 +  0.01271 _ 1 ) 1 =  (1 + AP R 2 _ 2  ) 2 . AP R 2  =  0.01267  =  1.267 % . -->
$$\left(1 + \frac{APR_m}{m}\right)^m = \left(1 + \frac{APR_n}{n}\right)^n$$
$$\left(1 + \frac{0{,}01271}{1}\right)^1 = \left(1 + \frac{APR_2}{2}\right)^2$$
$$APR_2 = 0{,}01267 = 1{,}267\%$$

Do đó, G-spread của nó là $(0{,}01267 - 0{,}011) = 16{,}7\text{ bps}$ (trong bản gốc tiếng Anh ghi nhầm là 167 bps do dịch dấu thập phân). Lợi suất tương đương bán niên của Trái phiếu C là 1,1797%:

![](assets/Fixed_Income.pdf-0169-14.png)

<!-- Formula Text: (1 + AP R m _ m  ) m =  (1 + AP R n _ n  ) n . (1 +  0.01178 _ 4 ) 4 =  (1 + AP R 2 _ 2  ) 2 . AP R 2  =  0.011797  =  1.1797 % . -->
$$\left(1 + \frac{APR_m}{m}\right)^m = \left(1 + \frac{APR_n}{n}\right)^n$$
$$\left(1 + \frac{0{,}01178}{4}\right)^4 = \left(1 + \frac{APR_2}{2}\right)^2$$
$$APR_2 = 0{,}011797 = 1{,}1797\%$$

Do đó, G-spread của nó là $(0{,}011797 - 0{,}011) = 8\text{ bps}$ (chính xác là $7{,}97\text{ bps}$).

4. Nếu một trái phiếu có quyền chọn mua lại đi kèm (*embedded call option*) và giá trị của quyền chọn mua lại là dương, thì giá đã điều chỉnh quyền chọn (*option-adjusted price*), so với giá tịnh (*flat price*) của trái phiếu đó, nhiều khả năng nhất là:

**A.** thấp hơn.

**B.** bằng nhau.

**C.** cao hơn.

###### **Lời giải:**

A là đáp án đúng (theo lời giải trong sách gốc; lưu ý ở phần bài học trang 181 sách định nghĩa giá đã điều chỉnh quyền chọn bằng giá tịnh cộng giá trị quyền chọn mua lại, tức cao hơn giá tịnh, nhưng trong câu hỏi tự đánh giá số 4 này đáp án của sách in là A với lập luận như sau). Giá trị của quyền chọn mua lại bằng giá của trái phiếu không kèm quyền chọn trừ đi giá của trái phiếu có quyền mua lại trước hạn. Nếu giá trị của quyền chọn mua lại là

<!-- PDF Page 170 -->

dương, thì giá đã điều chỉnh quyền chọn thấp hơn so với giá tịnh của trái phiếu.

B không đúng vì nếu giá trị của quyền chọn mua lại là dương, giá đã điều chỉnh quyền chọn so với giá tịnh của trái phiếu là thấp hơn, chứ không phải bằng nhau.

C không đúng vì nếu giá trị của quyền chọn mua lại là dương, giá đã điều chỉnh quyền chọn so với giá tịnh của trái phiếu là thấp hơn, chứ không phải cao hơn.

## **<mark>2</mark>**

##### **SỐ KỲ GHÉP LÃI TRONG NĂM VÀ LỢI SUẤT QUY ĐỔI THEO NĂM (*PERIODICITY AND ANNUALIZED YIELDS*)**

tính toán lợi suất hàng năm trên một trái phiếu cho các số kỳ ghép lãi (*compounding periods*) khác nhau trong một năm

Các nhà đầu tư khi phân tích các trái phiếu có hồ sơ dòng tiền và kỳ hạn đa dạng đều tìm kiếm một thước đo lợi suất _chuẩn hóa_ (*standardized*) để so sánh giữa các lựa chọn khác nhau. Các thước đo lợi suất thường được _quy đổi theo năm_ (*annualized*) nhằm cho phép so sánh trực tiếp. Đối với các chứng khoán thị trường vốn đáo hạn sau hơn một năm, các nhà đầu tư muốn có một mức lợi suất đáo hạn _được quy đổi theo năm_ và _có ghép lãi_ (*compounded*). Các quy ước đối với những công cụ đáo hạn trong vòng một năm hoặc ngắn hơn sẽ được trình bày trong một bài học sau.

Một mức lợi suất quy đổi theo năm và có ghép lãi trên một trái phiếu lãi suất cố định phụ thuộc vào số kỳ tính lãi giả định trong năm, được gọi là **số kỳ ghép lãi trong năm (*periodicity*)** của lãi suất năm. Số kỳ ghép lãi trong năm (*periodicity*) thường khớp với tần suất thanh toán coupon. Ví dụ, trái phiếu kỳ hạn 5 năm trả lãi cố định do Bright Wheels Automotive (BRWA) phát hành từ các bài học trước trả lãi coupon bán niên với lợi suất đáo hạn công bố theo năm là 3,2% ứng với số kỳ ghép lãi trong năm là 2—bằng lãi suất mỗi kỳ nửa năm (1,6%) nhân với 2. Một trái phiếu trả lãi coupon hàng quý có lợi suất công bố theo năm ứng với số kỳ ghép lãi trong năm là 4—bằng lãi suất mỗi quý nhân với 4.

Bảng minh họa 1 cho thấy cách một mức lợi suất đáo hạn công bố theo năm là 5% tạo ra các số tiền lãi khác nhau trong một năm khi ghép lãi hàng năm, bán niên, hàng quý và hàng tháng dựa trên một trái phiếu ngang giá lãi suất cố định có giá là 100.

<!-- PDF Page 171 -->

###### **Bảng minh họa 1: Lãi Suất Hiệu Dụng Năm Cho Các Kỳ Ghép Lãi Khác Nhau (*Exhibit 1: Effective Annual Rate for Different Compounding Periods*)**

![](assets/Fixed_Income.pdf-0171-04.png)

> **Chú thích hình ảnh:** Lãi suất hiệu dụng năm ứng với các số kỳ ghép lãi khác nhau từ $t = 0$ đến $t = 1$ (Giá trái phiếu = 100):
> - Hàng năm (*Annual*, 5,00%/kỳ): Tiền lãi trái phiếu vào cuối năm = 5,00.
> - Bán niên (*Semi-annual*, 2,50%/kỳ): Tiền lãi trái phiếu vào cuối năm = 5,0625.
> - Hàng quý (*Quarterly*, 1,25%/kỳ): Tiền lãi trái phiếu vào cuối năm = 5,0945.
> - Hàng tháng (*Monthly*, 0,4167%/kỳ): Tiền lãi trái phiếu vào cuối năm = 5,1162.

<!-- Picture Text: Time<br>t = 0 t = 1<br>Periodicity Bond interest at year end<br>(Rate per Period) (Price = 100)<br>Annual 5.00<br>(5.00%)<br>Semi-annual 5.0625<br>(2.50%)<br>Quarterly 5.0945<br>(1.25%)<br>Monthly 5.1162<br>(0.4167%)<br> -->

Số tiền lãi trái phiếu ở phía bên phải của Bảng minh họa 1 khi được biểu thị dưới dạng phần trăm được gọi là lãi suất hiệu dụng năm. **Lãi suất hiệu dụng năm (*effective annual rate* – EAR)** có số kỳ ghép lãi trong năm (*periodicity*) là 1 bởi vì chỉ có duy nhất một kỳ ghép lãi trong năm. Ví dụ, đối với một trái phiếu trả lãi coupon hàng quý ở mức 1,25% mỗi kỳ, hay lãi suất coupon năm là $(1{,}25\% \times 4) = 5\%$, mỗi khoản coupon nhận được đều được giả định là sẽ tái đầu tư ở mức lãi suất định kỳ—ở đây là 1,25%—trong phần thời gian còn lại của năm. Chúng ta có thể giải tìm giá trị tương lai của các dòng tiền này bằng cách sử dụng hàm `FV` trong Excel hoặc Google Sheets:

`=FV(rate, nper, pmt, [pv], [type]),`

trong đó:

_rate_ là lãi suất tái đầu tư định kỳ

_nper_ là số kỳ trong một năm

_pmt_ là khoản lãi mỗi kỳ

[_pv_] là giá trị hiện tại

[_type_] cho biết thời điểm thanh toán diễn ra, với 0 chỉ định việc thanh toán vào cuối mỗi kỳ

Đối với trái phiếu trả lãi coupon hàng quý:

`=FV(0.0125,4,1.25,0,0) = 5.0945.`

Do đó, giả định mỗi khoản coupon được tái đầu tư ở mức 1,25% cho đến hết năm, một trái phiếu trả lãi coupon hàng quý với lãi suất công bố theo năm là 5% sẽ tạo ra cùng số tiền lãi như một trái phiếu trả lãi coupon hàng năm với lãi suất công bố là 5,0945%. Hàm `EFFECT` trong Excel hoặc Google Sheets cũng có thể được sử dụng để tính lãi suất hiệu dụng năm cho một số kỳ ghép lãi nhất định mỗi năm.

Số kỳ ghép lãi trong năm phổ biến nhất tại Hoa Kỳ, Vương quốc Anh và một số thị trường thu nhập cố định khác là 2 bởi vì hầu hết các trái phiếu tại những khu vực tài phán này đều thực hiện thanh toán coupon bán niên. Một mức lãi suất hàng năm có số kỳ ghép lãi là 2 được gọi là **lợi suất theo cơ sở trái phiếu bán niên (*semiannual bond basis yield*)**, hay **lợi suất tương đương trái phiếu bán niên (*semiannual bond equivalent yield*)**. Do đó, lợi suất theo cơ sở trái phiếu bán niên bằng lợi suất mỗi kỳ nửa năm nhân với 2. Điều quan trọng cần ghi nhớ là “lợi suất theo cơ sở trái phiếu bán niên” (*“semiannual bond basis yield”*) và “lợi suất mỗi kỳ nửa năm” (*“yield per semiannual period”*) có ý nghĩa khác nhau. Ví dụ, nếu lợi suất trái phiếu là 2% mỗi kỳ nửa năm, thì lợi suất hàng năm của nó là 4% khi được công bố trên cơ sở trái phiếu bán niên.

<!-- PDF Page 172 -->

###### **VÍ DỤ 1 (*EXAMPLE 1*)**

###### **Số Kỳ Ghép Lãi Trong Năm của Trái Phiếu Không Trả Lãi Định Kỳ (*Periodicity of Zero-Coupon Bonds*)**

Số kỳ ghép lãi trong năm của lãi suất chiết khấu thị trường hàng năm đối với một trái phiếu không trả lãi định kỳ (*zero-coupon bond*) là tùy ý (*arbitrary*) bởi vì không có các khoản thanh toán coupon. Xét một trái phiếu không trả lãi định kỳ kỳ hạn 5 năm được định giá ở mức 80 trên mỗi 100 đơn vị mệnh giá. Giả định ghép lãi hàng năm, tức số kỳ ghép lãi là 1, lợi suất đáo hạn là 4,564%.

![](assets/Fixed_Income.pdf-0172-07.png)

<!-- Formula Text: 80  =    100 _ (1 + r) 5 ; r  =  0.045640;4.564% -->
$$80 = \frac{100}{(1 + r)^5}; \quad r = 0{,}045640 = 4{,}564\%$$

Giả định ghép lãi hàng quý, tức số kỳ ghép lãi là 4, lợi suất đáo hạn hàng năm cho cùng trái phiếu không trả lãi định kỳ kỳ hạn 5 năm này là 4,488%.

![](assets/Fixed_Income.pdf-0172-09.png)

<!-- Formula Text: 80  =    100 _ (1 + r) 20 ; r  =  0.011220; × 4  =  0.044880. -->
$$80 = \frac{100}{(1 + r)^{20}}; \quad r = 0{,}011220; \quad 0{,}011220 \times 4 = 0{,}044880 = 4{,}488\%$$

Như được thể hiện trong Bảng minh họa 2, mức lãi suất 2,2565% ghép lãi 2 lần một năm, 1,1220% ghép lãi 4 lần một năm, và 0,3726% ghép lãi 12 lần một năm đều tương đương với mức lãi suất hiệu dụng năm là 4,564%.

###### **Bảng minh họa 2: Số Kỳ Ghép Lãi Trong Năm của Lãi Suất Chiết Khấu Hàng Năm Đối Với Trái Phiếu Không Trả Lãi Định Kỳ (*Exhibit 2: Periodicity of Annual Discount Rate for Zero-Coupon Bond*)**

|**_Cột 1_**|**_Cột 2_**|**_Cột 3:_**<br>**_(Cột 2 × 5)_**|**_Cột 4_**|**_Cột 5:_**<br>**_(Cột 2 × Cột 4)_**|**_Cột 6:_**<br>**_$(1 + \text{Cột 4})^{(\text{Cột 2})} - 1$_**|
|---|---|---|---|---|---|
|**Tần suất (*Periodicity*)**|**Số kỳ / Năm (*Number of Periods/Year*)**|**Tổng số kỳ ghép lãi (*Number of Compounding Periods*)**|**Lợi suất đáo hạn định kỳ (*Periodic YTM*) (%)**|**Lợi suất đáo hạn hàng năm (*Annual YTM*) (%)**|**YTM định kỳ được ghép lãi theo số kỳ/năm (%)**|
|Hàng năm (*Annual*)|1|5|0,045640|0,045640|0,045640|
|Bán niên (*Semi-annual*)|2|10|0,022565|0,045130|0,045640|
|Hàng quý (*Quarterly*)|4|20|0,011220|0,044879|0,045640|
|Hàng tháng (*Monthly*)|12|60|0,003726|0,044712|0,045640|

Tổng tỷ suất sinh lợi ghép lãi là như nhau đối với mỗi cách biểu diễn lãi suất hàng năm. Chúng chỉ khác nhau về số kỳ ghép lãi mỗi năm—tức là về _số kỳ ghép lãi trong năm_ (*periodicity*) của lãi suất hàng năm. Đối với một cặp dòng tiền nhất định, lãi suất công bố theo năm và số kỳ ghép lãi trong năm có mối quan hệ tỉ lệ nghịch.

Một công cụ quan trọng trong phân tích thu nhập cố định là việc chuyển đổi một mức lợi suất quy đổi theo năm từ một số kỳ ghép lãi này sang một số kỳ ghép lãi khác. Đây được gọi là phép chuyển đổi số kỳ ghép lãi (*periodicity conversions* hay *compounding conversions*). Phương trình 1 thể hiện công thức tổng quát để chuyển đổi một mức lãi suất phần trăm năm (*annual percentage rate* – APR) cho $m$ kỳ mỗi năm, ký hiệu là $APR_m$, sang mức lãi suất phần trăm năm cho $n$ kỳ mỗi năm, ký hiệu là $APR_n$:

![](assets/Fixed_Income.pdf-0172-15.png)

<!-- Formula Text: (1 + AP R m _ m  ) m =  (1 + AP R n _ n  ) n . (1) -->
$$\left(1 + \frac{APR_m}{m}\right)^m = \left(1 + \frac{APR_n}{n}\right)^n \tag{1}$$

Ví dụ, giả sử một trái phiếu doanh nghiệp kỳ hạn 3 năm, trả lãi coupon bán niên 5%/năm được định giá ở mức 104 trên mỗi 100 đơn vị mệnh giá. Lợi suất đáo hạn của nó là 3,582%, được yết trên cơ sở trái phiếu bán niên ứng với số kỳ ghép lãi là 2: $0{,}01791 \times 2 = 0{,}03582$.

![](assets/Fixed_Income.pdf-0172-17.png)

<!-- Formula Text: 104  =    2.5 _ (1 + r) 1  +   2.5 _ (1 + r) 2  +   2.5 _ (1 + r) 3  +   2.5 _ (1 + r) 4  +   2.5 _ (1 + r) 5  +   102.5 _ (1 + r) 6 ; r  =  0.01791. -->
$$104 = \frac{2{,}5}{(1 + r)^1} + \frac{2{,}5}{(1 + r)^2} + \frac{2{,}5}{(1 + r)^3} + \frac{2{,}5}{(1 + r)^4} + \frac{2{,}5}{(1 + r)^5} + \frac{102{,}5}{(1 + r)^6}; \quad r = 0{,}01791$$

Để so sánh trái phiếu này với các trái phiếu khác, một chuyên viên phân tích chuyển đổi mức lợi suất đáo hạn quy đổi theo năm này sang ghép lãi hàng quý và hàng tháng. Việc này đòi hỏi sử dụng Phương trình 1 để chuyển đổi từ số kỳ ghép lãi $m = 2$ sang số kỳ ghép lãi $n = 4$ và $n = 12$.

<!-- PDF Page 173 -->

![](assets/Fixed_Income.pdf-0173-03.png)

<!-- Formula Text: (1 +  0.03582 _ 2 ) 2 =  (1 + AP R 4 _ 4  ) 4 ; AP R 4  =  0.03566. (1 +  0.03582 _ 2 ) 2 =  (1 + AP R 12 _ 12  ) 12 ; AP R 12  =  0.03556. -->
$$\left(1 + \frac{0{,}03582}{2}\right)^2 = \left(1 + \frac{APR_4}{4}\right)^4; \quad APR_4 = 0{,}03566$$
$$\left(1 + \frac{0{,}03582}{2}\right)^2 = \left(1 + \frac{APR_{12}}{12}\right)^{12}; \quad APR_{12} = 0{,}03556$$

Mức lợi suất đáo hạn hàng năm 3,582% khi ghép lãi bán niên mang lại cùng tỷ suất sinh lợi như mức lợi suất hàng năm 3,566% và 3,556% khi ghép lãi lần lượt theo quý và theo tháng. Một quy tắc chung cho việc chuyển đổi số kỳ ghép lãi là _ghép lãi thường xuyên hơn ở mức lãi suất năm thấp hơn sẽ tương ứng với ghép lãi ít thường xuyên hơn ở mức lãi suất năm cao hơn_. Quy tắc này có thể được sử dụng để kiểm tra các phép tính chuyển đổi số kỳ ghép lãi.

###### **VÍ DỤ 2 (*EXAMPLE 2*)**

###### **So Sánh Trái Phiếu Tách Lãi Với Trái Phiếu Trả Lãi Định Kỳ (*Comparing Strip Bonds to Coupon Bonds*)**

Các định chế trung gian tài chính có thể sở hữu các trái phiếu trả lãi coupon định kỳ rồi sau đó phát hành các trái phiếu không trả lãi định kỳ (*zero-coupon bonds*) riêng lẻ được cấu thành từ các khoản thanh toán coupon hoặc gốc của những trái phiếu trả lãi coupon đó. Những trái phiếu không trả lãi định kỳ này được gọi là trái phiếu tách lãi (*strip bonds*). Trái phiếu tách lãi hấp dẫn đối với các nhà đầu tư đang tìm cách khớp các dòng tiền đã biết vào một ngày cụ thể trong tương lai.

Một trái phiếu tách lãi (*strip bond* – không trả lãi định kỳ) kỳ hạn 20 năm của chính phủ Canada được định giá ở mức 69,4300 trên mỗi 100 đơn vị mệnh giá. Một chuyên viên phân tích muốn so sánh lợi suất của trái phiếu tách lãi này với lợi suất của một trái phiếu trả lãi coupon kỳ hạn 20 năm mới được phát hành. Cả trái phiếu tách lãi và trái phiếu trả lãi coupon đều không kèm quyền mua lại trước hạn. Trái phiếu trả lãi coupon kỳ hạn 20 năm trả lãi bán niên 2%/năm, và giá hiện tại của nó là 101,99 trên mỗi 100 đơn vị mệnh giá, tương ứng với mức lợi suất tương đương trái phiếu bán niên là 1,880%.

Chuyên viên phân tích sẽ tính lợi suất tương đương trái phiếu bán niên cho trái phiếu tách lãi và so sánh nó với mức lợi suất tương đương trái phiếu bán niên 1,880% của trái phiếu trả lãi coupon kỳ hạn 20 năm.

Có hai phương pháp tiếp cận. Phương pháp thứ nhất bao gồm việc tính lợi suất đáo hạn giả định ghép lãi hàng năm cho trái phiếu tách lãi rồi chuyển đổi nó sang lợi suất tương đương trái phiếu bán niên. Phương pháp thứ hai bao gồm việc tính trực tiếp lợi suất đáo hạn bán niên cho trái phiếu tách lãi rồi quy đổi theo năm bằng cách nhân với 2.

###### **Phương pháp 1 (*Approach 1*)**

Trái phiếu tách lãi kỳ hạn 20 năm không trả bất kỳ khoản coupon nào, vì vậy ở bước đầu tiên, chúng ta giả định ghép lãi hàng năm (số kỳ ghép lãi là 1) để tính lãi suất hiệu dụng năm dựa trên mức giá hiện tại và số năm còn lại cho đến khi đáo hạn.

![](assets/Fixed_Income.pdf-0173-13.png)

<!-- Formula Text: 69.43  =    100 _ (1 + r) 20 ; r  =  0.01840997  =  1.841 % . -->
$$69{,}43 = \frac{100}{(1 + r)^{20}}; \quad r = 0{,}01840997 = 1{,}841\%$$

Bước tiếp theo là chuyển đổi lãi suất hiệu dụng năm sang lợi suất tương đương trái phiếu bán niên. Việc này được thực hiện bằng cách sử dụng Phương trình 1 để chuyển đổi từ số kỳ ghép lãi là 1 sang số kỳ ghép lãi là 2.

![](assets/Fixed_Income.pdf-0173-15.png)

<!-- Formula Text: (1 + AP R m _ m  ) m =  (1 + AP R n _ n  ) n . (1 +  0.01841 _ 1 ) 1 =  (1 + AP R 2 _ 2  ) 2 . AP R 2  =  0.01832604  =  1.833 % . -->
$$\left(1 + \frac{APR_m}{m}\right)^m = \left(1 + \frac{APR_n}{n}\right)^n$$
$$\left(1 + \frac{0{,}01841}{1}\right)^1 = \left(1 + \frac{APR_2}{2}\right)^2$$
$$APR_2 = 0{,}01832604 = 1{,}833\%$$

<!-- PDF Page 174 -->

###### **Phương pháp 2 (*Approach 2*)**

Cách khác, chúng ta có thể giả định rằng việc ghép lãi diễn ra mỗi nửa năm (số kỳ ghép lãi là 2) và mức lãi suất hiệu dụng tính được sẽ là lãi suất bán niên.

![](assets/Fixed_Income.pdf-0174-04.png)

<!-- Formula Text: 69.43  =    100 _ (1 + r) 40 ; r  =  0.009163  =  0.916 % . -->
$$69{,}43 = \frac{100}{(1 + r)^{40}}; \quad r = 0{,}009163 = 0{,}916\%$$

Để quy đổi theo năm, chúng ta nhân kết quả này với 2 và thu được cùng kết quả như phương pháp thứ nhất: 1,833%.

###### **VÍ DỤ 3 (*EXAMPLE 3*)**

###### **Chuyển Đổi Số Kỳ Ghép Lãi Với Lợi Suất Âm (*Periodicity Conversion with Negative Yields*)**

Giả sử chính phủ Đức phát hành một trái phiếu không trả lãi định kỳ kỳ hạn 5 năm ở mức giá 103,72. Hãy tính lãi suất năm của trái phiếu tại thời điểm phát hành giả định ghép lãi hàng năm, bán niên và hàng tháng.

###### **Lời giải:**

Trước tiên, chúng ta có thể tính lợi suất đáo hạn của trái phiếu Đức dưới dạng lãi suất hiệu dụng năm giả định số kỳ ghép lãi là 1.

![](assets/Fixed_Income.pdf-0174-11.png)

<!-- Formula Text: 103.72  =    100 _ (1 + r) 5 ; r  =  − 0.00727834  =  − 0.7278 % . -->
$$103{,}72 = \frac{100}{(1 + r)^5}; \quad r = -0{,}00727834 = -0{,}7278\%$$

Việc chuyển đổi mức lợi suất đó sang ghép lãi bán niên và hàng tháng đòi hỏi phải sử dụng Phương trình 1 để chuyển đổi từ số kỳ ghép lãi là 1 sang số kỳ ghép lãi lần lượt là 2 và 12.

Chuyển đổi từ lợi suất năm ($m = 1$) sang bán niên ($n = 2$):

![](assets/Fixed_Income.pdf-0174-14.png)

<!-- Formula Text: (1 + AP R m _ m  ) m =  (1 + AP R n _ n  ) n . (1 +  − 0.007278 _ 1 ) 1 =  (1 + AP R 2 _ 2  ) 2 . AP R 2  =  − 0.007291  =  − 0.7291 % . -->
$$\left(1 + \frac{APR_m}{m}\right)^m = \left(1 + \frac{APR_n}{n}\right)^n$$
$$\left(1 + \frac{-0{,}007278}{1}\right)^1 = \left(1 + \frac{APR_2}{2}\right)^2$$
$$APR_2 = -0{,}007291 = -0{,}7291\%$$

Chuyển đổi từ lợi suất năm ($m = 1$) sang hàng tháng ($n = 12$):

![](assets/Fixed_Income.pdf-0174-16.png)

<!-- Formula Text: (1 + AP R m _ m  ) m =  (1 + AP R n _ n  ) n . (1 +  − 0.007278 _ 1 ) 1 =  (1 + AP R 12 _ 12  ) 12 . AP R 2  =  − 0.007303  =  − 0.7303 % . -->
$$\left(1 + \frac{APR_m}{m}\right)^m = \left(1 + \frac{APR_n}{n}\right)^n$$
$$\left(1 + \frac{-0{,}007278}{1}\right)^1 = \left(1 + \frac{APR_{12}}{12}\right)^{12}$$
$$APR_{12} = -0{,}007303 = -0{,}7303\%$$

_Lưu ý:_ Các đại lượng trong phép tính không được làm tròn trong quá trình tính toán, mặc dù chúng được hiển thị với ba chữ số thập phân cho mục đích trình bày. Kết quả cuối cùng được làm tròn đến ba chữ số thập phân.

###### **BỘ CÂU HỎI (*QUESTION SET*)**

1. Một trái phiếu có lợi suất đáo hạn là $-0{,}50\%$ khi sử dụng ghép lãi hàng năm. Nếu lợi suất này được chuyển đổi sang ghép lãi hàng tháng, nó sẽ _nhiều khả năng nhất_ là:

   - **A.** lớn hơn $-0{,}50\%$.

   - **B.** bằng $-0{,}50\%$.

<!-- PDF Page 175 -->

   - **C.** nhỏ hơn $-0{,}50\%$.

**Lời giải:**

C là đáp án đúng. Một quy tắc chung đối với việc chuyển đổi số kỳ ghép lãi là việc ghép lãi thường xuyên hơn trong năm tương ứng với mức lợi suất đáo hạn thấp hơn (hoặc âm nhiều hơn).

2. Chuyển đổi mức lợi suất 1,736% ghép lãi hàng tháng sang lãi suất hiệu dụng năm.

**Lời giải:**

![](assets/Fixed_Income.pdf-0175-05.png)

<!-- Formula Text: The effective annual rate assumes only one compounding period in a year (periodicity of 1). Converting from monthly to annual compounding re- quires converting from a periodicity of 12 to 1: (1 + AP R m _ m  ) m =  (1 + AP R n _ n  ) n . (1 +  0.01736 _ 12  ) 12 =  (1 + AP R 1 _ 1  ) 1 . AP R 1  =  0.0175  =  1.75 % . -->
Lãi suất hiệu dụng năm giả định chỉ có duy nhất một kỳ ghép lãi trong một năm (số kỳ ghép lãi là 1). Việc chuyển đổi từ ghép lãi hàng tháng sang hàng năm đòi hỏi phải chuyển đổi từ số kỳ ghép lãi là 12 sang 1:

$$\left(1 + \frac{APR_m}{m}\right)^m = \left(1 + \frac{APR_n}{n}\right)^n$$
$$\left(1 + \frac{0{,}01736}{12}\right)^{12} = \left(1 + \frac{APR_1}{1}\right)^1$$
$$APR_1 = 0{,}0175 = 1{,}75\%$$

3. Khi tính lợi suất đáo hạn cho một trái phiếu tách lãi (*strip bond* – không trả lãi định kỳ), số kỳ ghép lãi trong năm bắt buộc phải là 1.

Giải thích câu trả lời của bạn.

**A.** Đúng (*True*)
**B.** Sai (*False*)

###### **Lời giải**

Sai. Số kỳ ghép lãi trong năm của lãi suất chiết khấu thị trường hàng năm đối với một trái phiếu không trả lãi định kỳ là tùy ý bởi vì không có các khoản thanh toán coupon. Ví dụ, một mức lợi suất được tính bằng cách sử dụng số kỳ ghép lãi hàng quý (4) có thể dễ dàng được chuyển đổi sang mức lợi suất có số kỳ ghép lãi hàng năm (1).

##### **CÁC THƯỚC ĐO LỢI SUẤT KHÁC, CÁC QUY ƯỚC VÀ VIỆC HẠCH TOÁN CÁC QUYỀN CHỌN ĐI KÈM (*OTHER YIELD MEASURES, CONVENTIONS, AND ACCOUNTING FOR EMBEDDED OPTIONS*)**

## **<mark>3</mark>**

so sánh, tính toán và diễn giải các thước đo lợi suất (*yield measures*) và chênh lệch lợi suất (*yield spread measures*) cho trái phiếu lãi suất cố định

###### **Các Thước Đo Lợi Suất Khác và Các Quy Ước (*Other Yield Measures and Conventions*)**

Lợi suất hiện hành (*current yield*), một thước đo đơn giản bằng tiền lãi coupon hàng năm của trái phiếu chia cho giá tịnh (*flat price*), đã được giới thiệu trong một bài học trước. Ví dụ, nếu trái phiếu BRWA kỳ hạn 5 năm trả lãi coupon cố định bán niên 3,2%/năm được giới thiệu trước đó đang giao dịch ở mức giá 98,7 trên mỗi 100 đô la mệnh giá tại thời điểm $t$, thì lợi suất hiện hành của nó sẽ là:

$$CY_t = \frac{\text{Annual coupon}_t}{\text{Bond price}_t} = \frac{3{,}2\%}{0{,}987} = 3{,}242\% \tag{2}$$

<!-- PDF Page 176 -->

Lợi suất hiện hành là một thước đo tỷ suất sinh lợi thô sơ bởi vì nó chỉ tập trung vào thu nhập lãi đơn thuần, bỏ qua tần suất thanh toán coupon, tiền lãi sinh ra từ lãi (*interest on interest* – giá trị thời gian của tiền tệ) và lãi tích lũy (*accrued interest*). Bên cạnh việc thu thập và tái đầu tư các khoản thanh toán coupon, nhà đầu tư còn có một khoản lãi vốn (*gain*) nếu trái phiếu được mua ở mức chiết khấu và được hoàn trả ngang mệnh giá. Nhà đầu tư sẽ chịu một khoản lỗ vốn (*loss*) nếu trái phiếu được mua ở mức phần bù và được hoàn trả ngang mệnh giá.

Trên thực tế, thời điểm thực tế của các dòng tiền là yếu tố quan trọng để báo giá và tính toán lợi suất đáo hạn của trái phiếu. Hãy xét lại trái phiếu Eurobond kỳ hạn 30 năm trả lãi coupon hàng năm 4,625% của Romania đáo hạn vào ngày 3 tháng 4 năm 2049 từ phần trước. Giả sử đối với ngày thanh toán giao dịch là ngày 3 tháng 4 năm 2026, trái phiếu được định giá ở mức 97,3684 trên mỗi 100 đơn vị mệnh giá để đạt mức lợi suất 4,75% được yết trên cơ sở hàng năm, đếm ngày thực tế/thực tế (*actual/actual*). Khoản thanh toán coupon của nó được lên lịch vào ngày 3 tháng 4 hàng năm. Phép tính lợi suất này ngầm giả định rằng các khoản thanh toán được thực hiện vào chính xác những ngày đó. Phép tính này bỏ qua thực tế là có một số ngày trong số đó không phải là ngày làm việc (*business days*). Ví dụ, cả ngày 3 tháng 4 năm 2027 và ngày 3 tháng 4 năm 2032 đều là ngày Thứ Bảy, vì vậy các nhà đầu tư sẽ nhận được các khoản thanh toán coupon vào các ngày Thứ Hai kế tiếp, lần lượt là ngày 5 tháng 4 năm 2027 và năm 2032.

Các thước đo lợi suất giả định rằng các khoản thanh toán được thực hiện vào đúng các ngày theo lịch trình và không tính đến các ngày cuối tuần cũng như ngày nghỉ lễ được yết theo cái gọi là **quy ước thông lệ thị trường (*street convention*)**. Giả định này làm đơn giản hóa các phép tính giá và lợi suất trái phiếu và thường được sử dụng trên thực tế. **Lợi suất thực (*true yield*)** sử dụng các ngày thanh toán thực tế (ví dụ: ngày 5 tháng 4 năm 2027 và năm 2032 trong ví dụ trái phiếu Romania), có tính đến các ngày cuối tuần và ngày nghỉ lễ, cũng có thể được tính toán. Lợi suất thực không bao giờ cao hơn lợi suất theo quy ước thông lệ thị trường (*street convention yield*) bởi vì ngày cuối tuần và ngày nghỉ lễ làm trì hoãn thời gian nhận thanh toán. Sự chênh lệch này thường rất nhỏ, không quá một hoặc hai điểm cơ bản (*basis points*). Do đó, lợi suất thực không thường được sử dụng trên thực tế.

Hãy nhớ lại rằng lợi suất trái phiếu doanh nghiệp thường sử dụng quy ước đếm ngày 30/360. Đôi khi, các mức lợi suất này được quy đổi lại bằng cách sử dụng quy ước đếm ngày thực tế/thực tế (*actual/actual*), được gọi là **lợi suất tương đương trái phiếu chính phủ (*government equivalent yield*)**. Lợi suất tương đương trái phiếu chính phủ trên một trái phiếu doanh nghiệp có thể được sử dụng để thu được mức chênh lệch (*spread*) so với lợi suất trái phiếu chính phủ.

###### **VÍ DỤ 4 (*EXAMPLE 4*)**

###### **Lợi Suất Tương Đương Trái Phiếu Chính Phủ Cho Trái Phiếu BRWA Kỳ Hạn 5 Năm (*Government Equivalent Yield for BRWA Five-Year Bond*)**

Trong một ví dụ trước, BRWA đã phát hành một trái phiếu kỳ hạn 5 năm trả lãi coupon cố định bán niên 3,2%/năm ngang mệnh giá (*at par*). Theo tiêu chuẩn đối với trái phiếu doanh nghiệp, lợi suất trái phiếu BRWA được tính trên cơ sở đếm ngày 30/360. Trái phiếu Kho bạc Hoa Kỳ kỳ hạn 5 năm tương đương có lợi suất là 2,3%, nhưng vì là trái phiếu chính phủ nên lợi suất của nó được tính bằng cơ sở đếm ngày thực tế/thực tế (*actual/actual*). Mặc dù mức chênh lệch lợi suất có vẻ như là 90 bps ($= 3{,}2\% - 2{,}3\%$), nhưng cơ sở đếm ngày của chúng lại khác nhau.

Hãy tính lợi suất tương đương trái phiếu chính phủ cho trái phiếu BRWA và chỉ ra mức chênh lệch lợi suất giữa trái phiếu BRWA và trái phiếu chính phủ dựa trên cùng một cơ sở đếm ngày.

**Lời giải:**

![](assets/Fixed_Income.pdf-0176-12.png)

<!-- Formula Text: A simple approximation for restating a corporate bond yield from the 30/360 day count basis to the actual/actual day count basis is to multiply the BRWA bond yield by 365/360. Yiel d ACT/ACT  =   365 _ 360  × Yiel d 30/360. Yiel d ACT/ACT  =   365 _ 360  × 0.032. Yiel d ACT/ACT  =  3.244 % . -->
Một phép xấp xỉ đơn giản để quy đổi lợi suất trái phiếu doanh nghiệp từ cơ sở đếm ngày 30/360 sang cơ sở đếm ngày thực tế/thực tế là nhân lợi suất trái phiếu BRWA với $365/360$:

$$\text{Yield}_{ACT/ACT} = \frac{365}{360} \times \text{Yield}_{30/360}$$
$$\text{Yield}_{ACT/ACT} = \frac{365}{360} \times 0{,}032$$
$$\text{Yield}_{ACT/ACT} = 3{,}244\%$$

<!-- PDF Page 177 -->

Lợi suất tương đương trái phiếu chính phủ của trái phiếu BRWA là 3,2444%; do đó, mức chênh lệch lợi suất đáo hạn giữa hai trái phiếu là 94,4 bps ($= 3{,}2444\% - 2{,}3\%$).

Đôi khi **lợi suất đơn (*simple yield*)** trên một trái phiếu được yết giá. Đó là tổng của các khoản thanh toán coupon hàng năm cộng với phần phân bổ tuyến tính (*straight-line amortized share*) của khoản lãi hoặc lỗ vốn, chia cho giá tịnh (*flat price*). Lợi suất đơn được sử dụng chủ yếu để báo giá trái phiếu chính phủ Nhật Bản, được gọi là JGBs.

**Bảng minh họa 3: Tóm Tắt Các Quy Ước Lợi Suất (*Exhibit 3: Summary of Yield Conventions*)**

|**Quy ước (*Convention*)**|**Ý nghĩa (*Meaning*)**|
|---|---|
|**Thực tế/Thực tế (*Actual/Actual* – Act/Act)**|Số ngày thực tế từ lần thanh toán coupon trước đến ngày thanh toán giao dịch / tổng số ngày trong kỳ trả lãi coupon, giả định số ngày thực tế trong một năm. Thường được sử dụng với trái phiếu chính phủ.|
|**30/360**|Số ngày từ lần thanh toán coupon trước đến ngày thanh toán giao dịch, giả định có 30 ngày trong một tháng / tổng số ngày trong kỳ trả lãi coupon, giả định có 360 ngày trong một năm. Thường được sử dụng với trái phiếu doanh nghiệp.|
|**Quy ước thông lệ thị trường (*Street Convention*)**|Thước đo lợi suất không tính đến ngày cuối tuần và ngày nghỉ lễ ngân hàng, do đó giả định các dòng tiền được thanh toán vào đúng các ngày theo lịch trình của chúng.|
|**Lợi suất thực (*True Yield*)**|Thước đo lợi suất có tính đến ngày cuối tuần và ngày nghỉ lễ ngân hàng, do đó giả định các dòng tiền được thanh toán sau các ngày theo lịch trình khi trùng ngày nghỉ. Lợi suất thực không bao giờ cao hơn lợi suất theo quy ước thông lệ thị trường do sự chậm trễ về thời gian thanh toán.|
|**Lợi suất tương đương trái phiếu chính phủ (*Government Equivalent Yield*)**|Thước đo lợi suất quy đổi lại lợi suất đáo hạn dựa trên quy ước đếm ngày 30/360 sang mức lợi suất dựa trên quy ước đếm ngày thực tế/thực tế. Nó được sử dụng để quy đổi lại YTM trên một trái phiếu doanh nghiệp nhằm thu được mức chênh lệch (*spread*) so với YTM của trái phiếu chính phủ.|
|**Lợi suất đơn (*Simple Yield*)**|Thước đo lợi suất bằng tổng các khoản thanh toán coupon cộng với phần phân bổ tuyến tính của khoản lãi hoặc lỗ vốn, chia cho giá tịnh. Nó được sử dụng chủ yếu để báo giá trái phiếu chính phủ Nhật Bản (JGBs).|

###### **VÍ DỤ 5 (*EXAMPLE 5*)**

###### **So Sánh Lợi Suất Cho Các Số Kỳ Ghép Lãi Khác Nhau (*Comparing Yields for Different Periodicities*)**

Một chuyên viên phân tích quan sát thấy các số liệu thống kê được báo cáo sau đây cho hai trái phiếu.

||**Trái phiếu Antelas AG (*Antelas AG Bond*)**|**Trái phiếu BRWA (*BRWA Bond*)**|
|---|---|---|
|Lãi suất coupon hàng năm (*Annual Coupon Rate*)|3,20%|2,50%|
|Tần suất thanh toán coupon (*Coupon Payment Frequency*)|Hàng quý (*Quarterly*)|Bán niên (*Semiannually*)|
|Số năm đáo hạn (*Years to Maturity*)|5 năm|5 năm|
|Giá (trên 100 đơn vị mệnh giá) (*Price*)|94|98,70|
|Lợi suất hiện hành (*Current Yield*)|3,40%|2,53%|
|Lợi suất đáo hạn (*Yield-to-Maturity*)|4,548%|2,780%|

**1.** Xác nhận phép tính lợi suất hiện hành và lợi suất đáo hạn cho hai trái phiếu.

<!-- PDF Page 178 -->

**2.** Chuyên viên phân tích tin rằng trái phiếu BRWA có ít rủi ro hơn so với trái phiếu Antelas AG. Người mua trái phiếu Antelas AG nhận được bao nhiêu mức đền bù bổ sung, tính bằng điểm cơ bản (*basis points*) của lợi suất đáo hạn, cho việc gánh chịu rủi ro này so với trái phiếu BRWA?

**Lời giải câu 1:**

Hãy nhớ lại rằng lợi suất hiện hành là khoản coupon hàng năm được biểu thị dưới dạng phần trăm so với giá tịnh của trái phiếu.

$$\text{Current yield} = \frac{\text{Annual coupon}}{\text{Flat price}}$$

Lợi suất hiện hành đối với trái phiếu Antelas AG:

$$CY = \frac{3{,}20}{94} = 0{,}0340 = 3{,}40\%$$

Lợi suất hiện hành đối với trái phiếu BRWA:

$$CY = \frac{2{,}50}{98{,}70} = 0{,}0253 = 2{,}53\%$$

Hãy nhớ lại rằng lợi suất đáo hạn là một tỷ suất hoàn vốn nội bộ, tức mức lãi suất chiết khấu $r$ làm cân bằng giá của một trái phiếu với giá trị hiện tại của các dòng tiền tương lai.

$$PV = \frac{PMT_1}{(1 + r)^1} + \frac{PMT_2}{(1 + r)^2} + \dots + \frac{PMT_N + FV_N}{(1 + r)^N}$$

Lợi suất đáo hạn cũng có thể được tính bằng các hàm `YIELD` và `IRR` trong Microsoft Excel hoặc Google Sheets.

|**Trái phiếu Antelas AG (*Antelas AG Bond*)**||**Trái phiếu BRWA (*BRWA Bond*)**||
|---|---|---|---|
|Ngày thanh toán (*Settlement date*)|1/1/2000|Ngày thanh toán (*Settlement date*)|1/1/2000|
|Ngày đáo hạn (*Maturity date*)|1/1/2005|Ngày đáo hạn (*Maturity date*)|1/1/2005|
|Lãi suất coupon (*Coupon*)|0,032|Lãi suất coupon (*Coupon*)|0,025|
|Giá (*Price*)|94|Giá (*Price*)|98,7|
|Giá trị hoàn trả (*Redemption*)|100|Giá trị hoàn trả (*Redemption*)|100|
|Tần suất coupon (*Coupon frequency*)|4|Tần suất coupon (*Coupon frequency*)|2|
|**LỢI SUẤT (*YIELD*)**|**4,548%**|**LỢI SUẤT (*YIELD*)**|**2,780%**|

###### **Lời giải câu 2:**

Lợi suất đáo hạn trên hai trái phiếu có các giả định khác nhau về số kỳ ghép lãi trong năm (*periodicity*). Do đó, sự chênh lệch về lợi suất _không phải_ là 177 bps ($0{,}04548 - 0{,}02780$). Điều cốt yếu là phải so sánh các mức lợi suất trên cùng một số kỳ ghép lãi để đưa ra nhận định về giá trị tương đối (*relative value*).

![](assets/Fixed_Income.pdf-0178-12.png)

<!-- Formula Text: The Antelas AG bond yield-to-maturity of 4.548% for a periodicity of 4 converts to 4.574% for a periodicity of 2: (1 + AP R m _ m  ) m =  (1 + AP R n _ n  ) n . (1 +  0.04548 _ 4 ) 4 =  (1 + AP R 2 _ 2  ) 2 . AP R 2  =  0.04574  =  4.574 % . -->
Lợi suất đáo hạn 4,548% của trái phiếu Antelas AG ứng với số kỳ ghép lãi là 4 chuyển đổi thành 4,574% ứng với số kỳ ghép lãi là 2:

$$\left(1 + \frac{APR_m}{m}\right)^m = \left(1 + \frac{APR_n}{n}\right)^n$$
$$\left(1 + \frac{0{,}04548}{4}\right)^4 = \left(1 + \frac{APR_2}{2}\right)^2$$
$$APR_2 = 0{,}04574 = 4{,}574\%$$

Khi lợi suất đáo hạn của trái phiếu Antelas AG và trái phiếu BRWA được công bố trên cùng một số kỳ ghép lãi chung, phần lợi suất bổ sung mà người mua trái phiếu Antelas AG nhận được để đền bù cho rủi ro cao hơn của nó, so với trái phiếu BRWA, là $(0{,}04574 - 0{,}02780) = 179\text{ bps}$.

<!-- PDF Page 179 -->

###### **Trái Phiếu Có Quyền Chọn Đi Kèm (*Bonds with Embedded Options*)**

Nếu một trái phiếu lãi suất cố định có chứa một quyền chọn đi kèm (*embedded option*), các thước đo lợi suất khác sẽ được sử dụng. Hãy nhớ lại từ bài học trước rằng các điều khoản dự phòng (*contingency provisions*) này của trái phiếu không thể bị tách rời và giao dịch độc lập với trái phiếu. Ví dụ, một trái phiếu có quyền mua lại trước hạn (*callable bond*) trao cho tổ chức phát hành quyền mua lại trái phiếu từ nhà đầu tư. Việc này diễn ra tại các mức giá cụ thể vào những ngày được xác định trước sau một giai đoạn bảo vệ khỏi việc mua lại (*call protection period*) mà trong thời gian đó tổ chức phát hành không được phép thực hiện quyền chọn mua lại.

Ví dụ, một bài học trước về trái phiếu có quyền mua lại trước hạn đã giới thiệu trái phiếu trung hạn có quyền mua lại kỳ hạn 7 năm của Vivivyu Inc. (VIVU) (xem Bảng minh họa 4).

**Bảng minh họa 4: Bản Điều Khoản Trái Phiếu Có Quyền Mua Lại Trước Hạn Kỳ Hạn 7 Năm Lãi Suất 6,5% của VIVU (*Exhibit 4: 6.5% VIVU Seven-Year Callable Notes Term Sheet*)**

|**Trái Phiếu Có Quyền Mua Lại Trước Hạn Kỳ Hạn 7 Năm Lãi Suất 6,5% của Vivivyu Inc. (VIVU) (“Trái Phiếu”) (*6.5% Vivivyu Inc. (VIVU) Seven-Year Callable Notes (The “Notes”)*)**||
|---|---|
||**Tóm Tắt Bản Cáo Bạch (*Prospectus Summary*)**|
|Tổ chức phát hành (*Issuer*):|Vivivyu Incorporated|
|Ngày thanh toán (*Settlement Date*):|[T + 3 Ngày làm việc]|
|Ngày đáo hạn (*Maturity Date*):|[Bảy năm kể từ Ngày thanh toán]|
|Mệnh giá gốc (*Principal Amount*):|400 triệu USD|
|Lãi suất (*Interest*):|Lãi suất coupon cố định 6,5%|
|Thanh toán lãi (*Interest Payment*):|Bắt đầu sáu tháng kể từ [Ngày thanh toán], được trả bán niên với lần thanh toán cuối cùng vào [Ngày đáo hạn]|
|Thứ tự ưu tiên trả nợ (*Seniority*):|Trái phiếu là các nghĩa vụ nợ có tài sản đảm bảo và không phải nợ thứ cấp (*secured and unsubordinated*) của VIVU và có thứ tự ưu tiên ngang hàng (*rank pari passu*) với tất cả các khoản nợ có tài sản đảm bảo và không phải nợ thứ cấp khác|
|Điều khoản mua lại trước hạn (*Call Provision*):|Tổ chức phát hành có thể mua lại một phần hoặc toàn bộ Trái phiếu vào bất kỳ Ngày làm việc nào trước [Ngày đáo hạn] bắt đầu từ ba năm sau [Ngày thanh toán] dựa trên Lịch biểu Giá mua lại (*Call Price Schedule*) tính theo tỷ lệ phần trăm của Mệnh giá gốc cộng với lãi tích lũy|
|Lịch biểu Giá mua lại (*Call Price Schedule*):|103,25% [Từ năm thứ 3 đến năm thứ 4 sau Ngày thanh toán]<br>102,50% [Từ năm thứ 4 đến năm thứ 5 sau Ngày thanh toán]<br>101,75% [Từ năm thứ 5 đến năm thứ 6 sau Ngày thanh toán]|
||101,00% [Từ năm thứ 6 đến năm thứ 7 sau Ngày thanh toán]|

Trái phiếu VIVU không được phép mua lại trong ba năm đầu tiên, nhưng vào năm tiếp theo nó có thể bị mua lại ở mức giá 103,25 đô la trên mỗi 100 đô la mệnh giá. VIVU có quyền mua lại trái phiếu trong bốn năm cuối cùng dựa trên một lịch biểu giá cố định. Các nhà đầu tư đối mặt với rủi ro bị mua lại trước hạn (*call risk*) bắt đầu từ Năm thứ 3 thường ước tính mức lợi suất thấp nhất có thể kiếm được bằng cách tính toán chuỗi các mức lợi suất tương ứng với các ngày mua lại của trái phiếu.

Các thước đo lợi suất đáo hạn truyền thống giả định rằng tất cả các dòng tiền đều diễn ra đúng như cam kết và do đó phải được sửa đổi đối với các trái phiếu có quyền mua lại trước hạn. Các chuyên viên phân tích phải sử dụng các thước đo tỷ suất sinh lợi thay thế có tính đến đặc tính mua lại trước hạn của trái phiếu, chẳng hạn như lợi suất tính đến ngày mua lại đầu tiên (*yield to the first call date*), ngày mua lại thứ hai (*second call date*), v.v. **Lợi suất tính đến ngày mua lại (*yield-to-call* – YTC)** được tính bằng cách sửa đổi công thức tổng quát dùng để tính lợi suất đáo hạn.

![](assets/Fixed_Income.pdf-0179-09.png)

<!-- Formula Text: PV  =    PMT _ (1 + r) 1  +   PMT _ (1 + r) 2  + ... + PMT + Call price _____________ (1 + r) N , (3) -->
$$PV = \frac{PMT}{(1 + r)^1} + \frac{PMT}{(1 + r)^2} + \dots + \frac{PMT + \text{Call price}}{(1 + r)^N} \tag{3}$$

<!-- PDF Page 180 -->

trong đó:

$PV =$ giá của trái phiếu

$PMT =$ khoản thanh toán coupon mỗi kỳ

$\text{Call price} =$ mức giá mà tại đó trái phiếu có thể bị mua lại vào một ngày nhất định

- $r =$ lợi suất mỗi kỳ hay lãi suất chiết khấu thị trường
- $N =$ số kỳ cách đều nhau cho đến ngày mà trái phiếu có thể bị mua lại tại mức giá mua lại ($\text{Call price}$)

###### **VÍ DỤ 6 (*EXAMPLE 6*)**

###### **Lợi Suất Tính Đến Ngày Mua Lại Đối Với Trái Phiếu VIVU (*Yields-to-Call for the VIVU Bond*)**

Giả định lịch biểu giá mua lại đối với trái phiếu VIVU (đang giao dịch ở mức giá 106,50), phép tính lợi suất tính đến ngày mua lại lần thứ nhất, thứ hai, thứ ba, thứ tư, lợi suất thấp nhất có thể (*yield-to-worst*) và lợi suất đáo hạn như sau:

Lợi suất tính đến ngày mua lại lần thứ nhất (*Yield-to-first call*):

$$106{,}50 = \frac{3{,}25}{(1 + r)^1} + \frac{3{,}25}{(1 + r)^2} + \frac{3{,}25}{(1 + r)^3} + \frac{3{,}25}{(1 + r)^4} + \frac{3{,}25}{(1 + r)^5} + \frac{103{,}25 + 3{,}25}{(1 + r)^6}$$
$$r = 0{,}025748 \times 2 = 0{,}0515$$

Cách khác, có thể sử dụng hàm `YIELD` trong Microsoft Excel hoặc Google Sheets.

Lợi suất tính đến ngày mua lại lần thứ hai (*Yield-to-second call*):

$$106{,}50 = \frac{3{,}25}{(1 + r)^1} + \frac{3{,}25}{(1 + r)^2} + \frac{3{,}25}{(1 + r)^3} + \frac{3{,}25}{(1 + r)^4} + \frac{3{,}25}{(1 + r)^5} + \frac{3{,}25}{(1 + r)^6} + \frac{3{,}25}{(1 + r)^7} + \frac{102{,}50 + 3{,}25}{(1 + r)^8}$$
$$r = 0{,}026237 \times 2 = 0{,}0525$$

Lợi suất tính đến ngày mua lại lần thứ ba (*Yield-to-third call*):

$$106{,}50 = \frac{3{,}25}{(1 + r)^1} + \frac{3{,}25}{(1 + r)^2} + \frac{3{,}25}{(1 + r)^3} + \frac{3{,}25}{(1 + r)^4} + \frac{3{,}25}{(1 + r)^5} + \frac{3{,}25}{(1 + r)^6} + \frac{3{,}25}{(1 + r)^7} + \frac{3{,}25}{(1 + r)^8} + \frac{3{,}25}{(1 + r)^9} + \frac{101{,}75 + 3{,}25}{(1 + r)^{10}}$$
$$r = 0{,}02653 \times 2 = 0{,}0531$$

Lợi suất tính đến ngày mua lại lần thứ tư (*Yield-to-fourth call*):

$$106{,}50 = \frac{3{,}25}{(1 + r)^1} + \frac{3{,}25}{(1 + r)^2} + \frac{3{,}25}{(1 + r)^3} + \frac{3{,}25}{(1 + r)^4} + \frac{3{,}25}{(1 + r)^5} + \frac{3{,}25}{(1 + r)^6} + \frac{3{,}25}{(1 + r)^7} + \frac{3{,}25}{(1 + r)^8} + \frac{3{,}25}{(1 + r)^9} + \frac{3{,}25}{(1 + r)^{10}} + \frac{3{,}25}{(1 + r)^{11}} + \frac{101{,}00 + 3{,}25}{(1 + r)^{12}}$$
$$r = 0{,}026811 \times 2 = 0{,}0536$$

Và cuối cùng, lợi suất đáo hạn giả định trái phiếu không bị mua lại trước hạn:

$$106{,}50 = \frac{3{,}25}{(1 + r)^1} + \frac{3{,}25}{(1 + r)^2} + \frac{3{,}25}{(1 + r)^3} + \frac{3{,}25}{(1 + r)^4} + \frac{3{,}25}{(1 + r)^5} + \frac{3{,}25}{(1 + r)^6} + \frac{3{,}25}{(1 + r)^7} + \frac{3{,}25}{(1 + r)^8} + \frac{3{,}25}{(1 + r)^9} + \frac{3{,}25}{(1 + r)^{10}} + \frac{3{,}25}{(1 + r)^{11}} + \frac{3{,}25}{(1 + r)^{12}} + \frac{3{,}25}{(1 + r)^{13}} + \frac{100{,}00 + 3{,}25}{(1 + r)^{14}}$$

Cách khác, có thể sử dụng hàm `YIELD` trong Microsoft Excel hoặc Google Sheets.

<!-- PDF Page 181 -->

###### $r = 0{,}026868 \times 2 = 0{,}0537$.

Tóm lại, các thước đo lợi suất đối với trái phiếu VIVU như sau:

|Lợi suất tính đến ngày mua lại lần thứ nhất (*Yield-to-first call*)|5,149%|
|---|---|
|Lợi suất tính đến ngày mua lại lần thứ hai (*Yield-to-second call*)|5,247%|
|Lợi suất tính đến ngày mua lại lần thứ ba (*Yield-to-third call*)|5,313%|
|Lợi suất tính đến ngày mua lại lần thứ tư (*Yield-to-fourth call*)|5,362%|
|Lợi suất đáo hạn (*Yield-to-maturity*)|5,374%|

Mức thấp nhất trong chuỗi các lợi suất tính đến ngày mua lại và lợi suất đáo hạn được gọi là **lợi suất thấp nhất có thể (*yield-to-worst* – YTW)**. Đối với trái phiếu VIVU, đó là lợi suất tính đến ngày mua lại lần thứ nhất ở mức 5,15%. Mục đích của thước đo này là cung cấp cho nhà đầu tư thước đo thận trọng nhất (*most conservative measure*) về tỷ suất sinh lợi.

Lợi suất thấp nhất có thể (*yield-to-worst*) là một thước đo lợi suất thường được trích dẫn đối với các trái phiếu lãi suất cố định có quyền mua lại trước hạn do các nhà tạo lập thị trường trái phiếu và các nhà đầu tư sử dụng. Tuy nhiên, một phương pháp tiếp cận chính xác hơn là sử dụng mô hình định giá quyền chọn (*option pricing model*) cùng một giả định về độ biến động lãi suất tương lai để định giá quyền chọn mua lại đi kèm (*embedded call option*). Giá trị của quyền chọn mua lại đi kèm được cộng vào giá tịnh của trái phiếu để thu được **giá đã điều chỉnh quyền chọn (*option-adjusted price*)**. Nhà đầu tư gánh chịu rủi ro bị mua lại trước hạn (tổ chức phát hành trái phiếu nắm giữ quyền chọn mua lại), vì vậy quyền chọn mua lại đi kèm làm giảm giá trị của trái phiếu dưới góc độ của nhà đầu tư. Nhà đầu tư trả mức giá thấp hơn cho trái phiếu có quyền mua lại so với trường hợp nó không kèm quyền chọn (*option-free*). Nếu trái phiếu không kèm quyền mua lại, giá của nó sẽ cao hơn. Giá đã điều chỉnh quyền chọn được sử dụng để tính **lợi suất đã điều chỉnh quyền chọn (*option-adjusted yield*)**. Lợi suất đã điều chỉnh quyền chọn là lãi suất chiết khấu thị trường yêu cầu mà theo đó mức giá đã được điều chỉnh cho giá trị của quyền chọn đi kèm. Giá trị của quyền chọn mua lại bằng giá của trái phiếu không kèm quyền chọn trừ đi giá của trái phiếu có quyền mua lại trước hạn.

###### **BỘ CÂU HỎI (*QUESTION SET*)**

1. Xác định thước đo lợi suất nào sau đây tương ứng với các đặc điểm được liệt kê dưới đây.

|**Thước đo lợi suất (*Yield Measure*)**|**Đặc điểm (*Characteristic*)**|
|---|---|
|A. Lợi suất đơn (*Simple Yield*)|1. Thước đo lợi suất giả định một kỳ ghép lãi mỗi năm|
|B. Lãi suất hiệu dụng năm (*Effective Annual Rate*)|2. Thước đo lợi suất quy đổi lại mức lợi suất dựa trên quy ước đếm ngày 30/360 sang mức lợi suất dựa trên quy ước đếm ngày thực tế/thực tế|
|C. Lợi suất theo quy ước thông lệ thị trường (*Street Convention Yield*)|3. Thước đo lợi suất bằng tổng các khoản thanh toán coupon cộng với phần phân bổ tuyến tính của khoản lãi hoặc lỗ vốn, chia cho giá tịnh|
|D. Lợi suất tương đương trái phiếu chính phủ (*Government Equivalent Yield*)|4. Giả định các dòng tiền được thanh toán vào đúng các ngày theo lịch trình của chúng, không tính đến ngày cuối tuần và ngày nghỉ lễ ngân hàng|

**Lời giải:**

<!-- PDF Page 182 -->

|**Thước đo lợi suất (*Yield Measure*)**|**Đặc điểm (*Characteristic*)**|
|---|---|
|B. Lãi suất hiệu dụng năm (*Effective Annual Rate*)|1. Thước đo lợi suất giả định một kỳ ghép lãi trong năm|
|D. Lợi suất tương đương trái phiếu chính phủ (*Government Equivalent Yield*)|2. Thước đo lợi suất quy đổi lại lợi suất đáo hạn dựa trên quy ước đếm ngày 30/360 sang mức lợi suất dựa trên quy ước đếm ngày thực tế/thực tế|
|A. Lợi suất đơn (*Simple Yield*)|3. Thước đo lợi suất bằng tổng các khoản thanh toán coupon cộng với phần phân bổ tuyến tính của khoản lãi hoặc lỗ vốn, chia cho giá tịnh|
|C. Lợi suất theo quy ước thông lệ thị trường (*Street Convention Yield*)|4. Giả định các dòng tiền được thanh toán vào đúng các ngày theo lịch trình của chúng, không tính đến ngày cuối tuần và ngày nghỉ lễ ngân hàng|

2. Một chuyên viên phân tích đã tính toán các mức lợi suất sau đây cho một trái phiếu có quyền mua lại kỳ hạn 4 năm. Hãy xác định lợi suất thấp nhất có thể (*yield-to-worst*).

|**Thước đo lợi suất (*Yield Measure*)**|**Giá trị (*Value*)**|
|---|---|
|Lợi suất tính đến ngày mua lại lần thứ nhất (*Yield-to-first call*)|0,000%|
|Lợi suất tính đến ngày mua lại lần thứ hai (*Yield-to-second call*)|0,157%|
|Lợi suất tính đến ngày mua lại lần thứ ba (*Yield-to-third call*)|0,939%|
|Lợi suất đáo hạn (*Yield-to-maturity*)|–0,385%|

###### **Lời giải:**

$-0{,}385\%$ (hay $-0{,}3852\%$). Lợi suất thấp nhất có thể (*yield-to-worst*) là mức thấp nhất trong chuỗi các lợi suất tính đến ngày mua lại và lợi suất đáo hạn. Mục đích của *yield-to-worst* là cung cấp cho nhà đầu tư giả định thận trọng nhất về tỷ suất sinh lợi.

Sử dụng thông tin sau đây do một chuyên viên phân tích thu nhập cố định tổng hợp cho hai trái phiếu, vào ngày cả hai được phát hành, để trả lời Câu hỏi 3 và 4.

||**Trái phiếu Doanh nghiệp (*Corporate Bond*)**|**Trái phiếu Chính phủ (*Sovereign Bond*)**|
|---|---|---|
|Lãi suất coupon hàng năm (*Annual coupon rate*)|4,00%|1,00%|
|Tần suất coupon (*Coupon frequency*)|Bán niên (*Semiannual*)|Hàng quý (*Quarterly*)|
|Số năm đáo hạn (*Years to maturity*)|3 năm|3 năm|
|Giá (trên 100 đơn vị mệnh giá) (*Price*)|91|102|
|Cơ sở đếm ngày (*Day-count basis*)|30/360|Thực tế/thực tế (*Actual/actual*)|
|Lịch biểu giá mua lại (*Call price schedule*):|101,25 (1–2 năm sau ngày thanh toán)|-|

3. Lợi suất hiện hành (*current yield*) của trái phiếu chính phủ xấp xỉ:

   - **A.** _thấp hơn_ 140 bps so với lợi suất hiện hành của trái phiếu doanh nghiệp.

   - **B.** _thấp hơn_ 340 bps so với lợi suất hiện hành của trái phiếu doanh nghiệp.

   - **C.** _cao hơn_ 140 bps so với lợi suất hiện hành của trái phiếu doanh nghiệp.

   - **Lời giải:**

B là đáp án đúng. Lợi suất hiện hành là khoản coupon hàng năm được biểu thị dưới dạng phần trăm so với giá của trái phiếu. Lợi suất hiện hành của trái phiếu doanh nghiệp là 440 bps ($4/91 = 4{,}3956\%$), trong khi lợi suất hiện hành của trái phiếu chính phủ là 98 bps ($1/102 = 0{,}9804\%$), thấp hơn 342 bps.


---

# Tập 6: Chứng Khoán Thu Nhập Cố Định (*Fixed Income*)
## Học phần 7: Các Thước Đo Lợi Suất và Chênh Lệch Lợi Suất Cho Trái Phiếu Lãi Suất Cố Định (*Yield and Yield Spread Measures for Fixed-Rate Bonds*)
### Phần 2/2: Các Thước Đo Chênh Lệch Lợi Suất Cho Trái Phiếu Lãi Suất Cố Định và Định Giá Ma Trận (Trang PDF 183–196)

---

<!-- PDF Page 183 -->

4. Lợi suất tính đến ngày mua lại lần thứ nhất (*yield-to-first call*) của trái phiếu doanh nghiệp gần nhất với:

**A.** 2,15%.

**B.** 7,80%.

**C.** 15,00%.

**Lời giải:**

C là đáp án đúng. Lợi suất tính đến ngày mua lại lần thứ nhất là tỷ suất hoàn vốn nội bộ $r$ của một trái phiếu có quyền mua lại trước hạn giả định nó được mua lại vào ngày mua lại theo lịch trình sớm nhất tại mức giá mua lại của nó.

![](assets/Fixed_Income.pdf-0183-04.png)

<!-- Formula Text: PV  =    PMT _ (1 + r) 1  +   PMT _ (1 + r) 2  + ... + PMT + Callprice ____________ (1 + r) N . 91  = 2 _ (1 + r) 1  +  101.5 + 2 _ (1 + r) 2 . -->
$$PV = \frac{PMT}{(1 + r)^1} + \frac{PMT}{(1 + r)^2} + \dots + \frac{PMT + \text{Call price}}{(1 + r)^N}$$
$$91 = \frac{2}{(1 + r)^1} + \frac{101{,}25 + 2}{(1 + r)^2} \quad (\text{trong ảnh gốc ghi } 101{,}5 + 2)$$

![](assets/Fixed_Income.pdf-0183-05.png)

<!-- Formula Text: r  =  0.0762 × 2  =  0.1525. -->
$$r = 0{,}0762 \times 2 = 0{,}1525$$

Lợi suất tính đến ngày mua lại lần thứ nhất của trái phiếu là 15,25%.

### **CÁC THƯỚC ĐO CHÊNH LỆCH LỢI SUẤT CHO TRÁI PHIẾU LÃI SUẤT CỐ ĐỊNH VÀ ĐỊNH GIÁ MA TRẬN (*YIELD SPREAD MEASURES FOR FIXED-RATE BONDS AND MATRIX PRICING*)**

# **<mark>4</mark>**

so sánh, tính toán và diễn giải các thước đo lợi suất (*yield measures*) và chênh lệch lợi suất (*yield spread measures*) cho trái phiếu lãi suất cố định

#### **Chênh Lệch Lợi Suất So Với Lãi Suất Chuẩn (*Yield Spreads over Benchmark Rates*)**

Trong phân tích chứng khoán thu nhập cố định, điều quan trọng là phải hiểu _tại sao_ giá trái phiếu và lợi suất đáo hạn lại thay đổi. Để làm được điều này, sẽ rất hữu ích khi phân tách lợi suất đáo hạn thành một lãi suất cơ sở hay **lãi suất chuẩn (*benchmark*)** và một **mức chênh lệch (*spread*)** đặc thù của tổ chức phát hành. Ví dụ, một bài học trước đã giới thiệu trái phiếu chuẩn của chính phủ (*government benchmark bonds*) là những chứng khoán có tính thanh khoản cao nhất với rủi ro vỡ nợ thấp nhất cho một thời gian đáo hạn cụ thể trên mỗi thị trường. **Chênh lệch lợi suất (*yield spread*)** là hiệu số giữa lợi suất đáo hạn của trái phiếu và lợi suất chuẩn (*benchmark yield*).

Hai thành phần này giúp các nhà đầu tư phân biệt giữa các yếu tố kinh tế vĩ mô (từ trên xuống – *top-down*) và kinh tế vi mô (từ dưới lên – *bottom-up*) tác động đến giá trái phiếu và do đó tác động đến lợi suất đáo hạn của nó. Lãi suất chuẩn nắm bắt các yếu tố từ trên xuống, trong khi mức chênh lệch nắm bắt các yếu tố từ dưới lên, như được thể hiện trong Bảng minh họa 5.

<!-- PDF Page 184 -->

**Bảng minh họa 5: Các Thành Phần của Lợi Suất Đáo Hạn (*Exhibit 5: Yield-to-Maturity Components*)**

![](assets/Fixed_Income.pdf-0184-04.png)

> **Chú thích hình ảnh:** Cấu trúc các thành phần của Lợi suất đáo hạn (YTM):
> - **Mức chênh lệch (*Spread*) — Phần bù rủi ro (*Risk Premium*):** Thuế (*Taxation*), Thanh khoản (*Liquidity*), Rủi ro tín dụng (*Credit Risk*).
> - **Lãi suất chuẩn (*Benchmark*) — Tỷ suất sinh lợi “phi rủi ro” (*“Risk-Free” Rate of Return*):** Tỷ lệ lạm phát kỳ vọng (*Expected Inflation Rate*), Lãi suất thực kỳ vọng (*Expected Real Rate*).

<!-- Picture Text: Taxation<br>Spread Risk Premium Liquidity<br>Credit Risk<br>Expected Inflation<br>Rate<br>Benchmark “Risk-Free” Rate of<br>Return<br>Expected Real<br>Rate<br> -->

Lãi suất chuẩn được sử dụng nhiều nhất là trái phiếu chính phủ được phát hành gần đây nhất, được gọi là chứng khoán **mới phát hành (*on-the-run*)**. Trái phiếu chính phủ *on-the-run* là chứng khoán được giao dịch sôi động nhất và có lãi suất coupon gần nhất với lãi suất chiết khấu thị trường hiện hành cho kỳ hạn đó. Điều này ngụ ý rằng nó được định giá gần với mệnh giá (*par value*). Các trái phiếu chính phủ đã lưu hành lâu hơn được gọi là **chứng khoán phát hành đợt cũ (*off-the-run*)**. Các trái phiếu *on-the-run* thường giao dịch ở mức lợi suất đáo hạn thấp hơn một chút so với các trái phiếu *off-the-run* có cùng thời gian đáo hạn hoặc có thời gian đáo hạn tương tự do sự khác biệt về nhu cầu đối với chứng khoán và đôi khi là sự khác biệt về chi phí tài trợ chứng khoán chính phủ trên thị trường repo.

Mức chênh lệch lợi suất so với một chuẩn tham chiếu cụ thể được gọi là **chênh lệch chuẩn (*benchmark spread*)** và đại diện cho phần bù rủi ro đối với rủi ro tín dụng, rủi ro thanh khoản và có thể cả tác động thuế của việc nắm giữ một trái phiếu cụ thể. Bảng minh họa 6 thể hiện mối quan hệ giữa lợi suất đáo hạn của một tổ chức phát hành cụ thể và đường cong lợi suất chính phủ chuẩn (*benchmark government yield curve*).

<!-- PDF Page 185 -->

**Bảng minh họa 6: Đường Cong Lợi Suất của Tổ Chức Phát Hành và của Chính Phủ (*Exhibit 6: Issuer and Government Yield Curves*)**

![](assets/Fixed_Income.pdf-0185-03.png)

> **Chú thích hình ảnh:** Đồ thị Đường cong lợi suất với trục tung là Lợi suất (*Yield %*) và trục hoành là Kỳ hạn (*Term*: 2, 3, 5, 7, 10, 20):
> - Đường bên dưới: Trái phiếu Kho bạc mới phát hành (*On-the-Run Treasuries*).
> - Đường bên trên: Bao gồm thêm phần Chênh lệch lợi suất so với trái phiếu Kho bạc (*Yield Spread Over Treasuries*).

<!-- Picture Text: Yield (%)<br>4.0<br>Yield Spread<br>3.5 Over Treasuries<br>3.0<br>2.5<br>2.0<br>On-the-Run<br>Treasuries<br>1.5<br>1.0<br>0<br>2 3 5 7 10 20<br>Term<br> -->

Các mức chênh lệch lợi suất (*spreads*) cho phép chuyên viên phân tích đánh giá tốt hơn giá trị tương đối (*relative value*) của một trái phiếu trên cơ sở lịch sử và so sánh bằng cách kiểm soát (loại trừ) các yếu tố kinh tế vĩ mô, chẳng hạn như sự tăng hoặc giảm trên diện rộng của lãi suất chuẩn. Một chuyên viên phân tích có thể so sánh mức chênh lệch hiện tại với mức trung bình lịch sử cũng như các mức đỉnh và đáy trong quá khứ của nó, đồng thời so sánh với các trái phiếu khác để giúp xác định liệu một trái phiếu đang bị định giá thấp hay định giá cao trên cơ sở tương đối.

Mức chênh lệch lợi suất tính bằng điểm cơ bản (*basis points*) so với lợi suất trái phiếu chính phủ thực tế hoặc nội suy được gọi là **chênh lệch G (*G-spread*)** và đại diện cho tỷ suất sinh lợi để gánh chịu các rủi ro so với trái phiếu chính phủ trung ương. Nếu không có trái phiếu chuẩn của chính phủ trung ương nào khớp với kỳ hạn của trái phiếu đang xét, một quy trình xấp xỉ để tìm G-spread phải được sử dụng, như được minh họa trong Bảng minh họa 7 và được trình bày trong ví dụ sau đây.

##### **Bảng minh họa 7: Tìm Chênh Lệch G Khi Không Có Trái Phiếu Chuẩn Tương Đương (*Exhibit 7: Finding G-Spreads When a Comparable Benchmark Bond Does Not Exist*)**

![](assets/Fixed_Income.pdf-0185-07.png)

> **Chú thích hình ảnh:** Quy trình 3 bước tính G-spread khi không có trái phiếu chuẩn cùng kỳ hạn:
> - **Bước 1 (*Step 1*):** Tính YTM hiện tại của trái phiếu.
> - **Bước 2 (*Step 2*):** Nội suy tuyến tính lãi suất (YTM) hiện tại của các trái phiếu chính phủ chuẩn có kỳ hạn gần nhất (ngắn hơn / dài hơn) với kỳ hạn của trái phiếu đã cho, để tìm mức lãi suất chính phủ xấp xỉ khớp với kỳ hạn của trái phiếu đã cho.
> - **Bước 3 (*Step 3*):** G-spread là hiệu số giữa YTM hiện tại của trái phiếu và lãi suất chuẩn chính phủ nội suy (xấp xỉ).

<!-- Picture Text: Step 1<br>Step 2<br>Step 3<br>Calculate the bond’s<br>current YTM. Linearly interpolate current<br>rates (YTMs) for the  G-spread is difference<br>sovereign benchmark bonds  between the bond’s<br>with maturities closest to  current YTM and the<br>(below/above) the given interpolated (appproximate)<br>bond’s maturity, to find sovereign<br>an approximate sovereign  benchmark rate.<br>rate matching the given<br>bond’s maturity.<br> -->

<!-- PDF Page 186 -->

##### **VÍ DỤ 7 (*EXAMPLE 7*)**

#### **Tính Chênh Lệch G Khi Không Có Trái Phiếu Chuẩn Tương Đương (*Calculating G-Spread without a Comparable Benchmark Bond*)**

Giả sử Liên bang Nga đã phát hành một trái phiếu chính phủ kỳ hạn 30 năm định danh bằng đồng đô la Mỹ dựa trên các điều khoản sau đây:

|**Trái Phiếu Liên Bang Nga Lãi Suất 5,25% (*5.25% Russian Federation Bonds*)**<br>**Tóm Tắt Ngắn Gọn Các Điều Khoản (*Brief Summary of Terms*)**||
|---|---|
|Tổ chức phát hành (*Issuer*):|Liên bang Nga (*Russian Federation*)|
|Ngày thanh toán (*Settlement Date*):|[T + 5 Ngày làm việc]|
|Ngày đáo hạn (*Maturity Date*):|[30 năm kể từ Ngày thanh toán]|
|Mệnh giá gốc (*Principal Amount*):|750 triệu USD|
|Lãi suất (*Interest*):|Lãi suất cố định bán niên 5,25%, cơ sở đếm ngày 30/360|
|Giá phát hành (*Issuance Price*):|99,625|
|Chênh lệch phát hành (*Issuance Spread*):|200 bp so với trái phiếu Kho bạc Hoa Kỳ kỳ hạn 30 năm hiện hành|
|Phát hành và Giao dịch (*Issuance and Trading*):|Phát hành riêng lẻ tại Hoa Kỳ theo Quy tắc 144A (*US Private Placement under Rule 144A*)<br>DTC / Euroclear / Clearstream|
|Thứ tự ưu tiên trả nợ (*Seniority*):|Trái phiếu cấp cao không có tài sản đảm bảo (*Senior Unsecured*)|
|Sở giao dịch (*Exchanges*):|Luxembourg|

Sáu năm sau ngày phát hành ban đầu, vào ngày 15 tháng 3 năm 2026, trái phiếu này đang giao dịch ở mức giá 123,5 trên mỗi 100 đơn vị mệnh giá, và một chuyên viên phân tích quan sát thấy lợi suất trái phiếu Kho bạc Hoa Kỳ kỳ hạn 20 năm và 30 năm hiện lần lượt ở mức 2,00% và 2,25%. Hãy tính mức G-spread hiện tại của trái phiếu Liên bang Nga.

- Bước 1: Tính lợi suất đáo hạn hiện tại của trái phiếu Liên bang Nga. Chúng ta có thể giải tìm $r$ bằng công thức tổng quát cho giá và lợi suất trái phiếu:

$$PV = \frac{PMT_1}{(1 + r)^1} + \frac{PMT_2}{(1 + r)^2} + \dots + \frac{PMT_N + FV_N}{(1 + r)^N}$$

- Hoặc chúng ta có thể sử dụng hàm `YIELD` trong Excel hay Google Sheets giả định ngày thanh toán giao dịch là 15 tháng 3 năm 2026:

`=YIELD(DATE(2026,3,15),DATE(2050,3,15),5.25%,123.5,100,2,0)`

`= 3.756%.`

- Bước 2: Nội suy tuyến tính lợi suất trái phiếu Kho bạc Hoa Kỳ kỳ hạn 20 năm ($r_{20y}$) và 30 năm ($r_{30y}$) hiện hành để giải tìm mức chuẩn trái phiếu Kho bạc Hoa Kỳ kỳ hạn 24 năm xấp xỉ ($r_{24y}$):

   **1.** Giải tìm tỷ trọng của trái phiếu kỳ hạn 20 năm và 30 năm trong phép tính nội suy:

Tỷ trọng trái phiếu kỳ hạn 20 năm $= w_{20} = 60\%$ $[= (30 - 24)/(30 - 20)]$.
Tỷ trọng trái phiếu kỳ hạn 30 năm $= w_{30} = 40\%$, hay $(1 - w_{20})$.

- Lưu ý rằng $(w_{20} \times 20) + (w_{30} \times 30) = 24$.

- **2.** Lãi suất chính phủ kỳ hạn 24 năm là mức bình quân gia quyền của lãi suất trái phiếu kỳ hạn 20 năm và lãi suất trái phiếu Kho bạc Hoa Kỳ kỳ hạn 30 năm sử dụng các tỷ trọng ở trên.

$$r_{24y} = w_{20} \times r_{20y} + w_{30} \times r_{30y}$$

<!-- PDF Page 187 -->

$$= (60\% \times 2{,}00\%) + (40\% \times 2{,}25\%) = 2{,}10\%$$

Bước 3: G-spread là hiệu số giữa lợi suất đáo hạn hiện tại của trái phiếu Liên bang Nga và lãi suất chính phủ Hoa Kỳ kỳ hạn 24 năm: $1{,}656\% = 3{,}756\% - 2{,}10\%$, vì vậy G-spread là 166 bps.

Mức chênh lệch lợi suất của một trái phiếu so với lãi suất hoán đổi tiêu chuẩn (*standard swap rate*) bằng cùng đồng tiền và có cùng kỳ hạn được gọi là **chênh lệch I (*I-spread*)** hay chênh lệch nội suy (*interpolated spread*). Loại chênh lệch này là một phép so sánh với một lãi suất tham chiếu ngắn hạn dựa trên thị trường và là thông lệ phổ biến để định giá cũng như báo giá các trái phiếu doanh nghiệp định danh bằng đồng euro, sử dụng hợp đồng hoán đổi lãi suất đồng euro (*euro interest rate swap*) làm chuẩn tham chiếu. Ví dụ, trái phiếu đồng euro không trả lãi định kỳ kỳ hạn 5 năm do chính phủ Trung Quốc phát hành ở mức lợi suất đáo hạn âm từ bài học trước đã được định giá ở mức “lãi suất hoán đổi trung bình cộng 30 bps” (*“mid-swaps plus 30 bps”*), trong đó “lãi suất hoán đổi trung bình” (*“mid-swaps”*) là mức trung bình cộng của lãi suất hoán đổi chào mua (*bid*) và chào bán (*offered*).

Các tổ chức phát hành sẽ sử dụng I-spread để xác định chi phí tương đối của trái phiếu lãi suất cố định so với các phương án lãi suất thả nổi thay thế, chẳng hạn như khoản vay ngân hàng hoặc thương phiếu (*commercial paper*), trong khi các nhà đầu tư sử dụng nó như một thước đo rủi ro tín dụng của trái phiếu. Trong khi một hợp đồng hoán đổi lãi suất tiêu chuẩn bao gồm việc trao đổi các dòng tiền cố định lấy dòng tiền thả nổi dựa trên một chỉ số lãi suất thả nổi, thì một hợp đồng hoán đổi tài sản (*asset swap*) chuyển đổi khoản coupon cố định định kỳ của một trái phiếu cụ thể thành lãi suất tham chiếu thị trường (*market reference rate* – MRR) cộng hoặc trừ một mức chênh lệch. Nếu trái phiếu được định giá gần với mệnh giá, phép chuyển đổi này xấp xỉ với cái giá của rủi ro tín dụng của trái phiếu cao hơn chỉ số MRR.

##### **VÍ DỤ 8 (*EXAMPLE 8*)**

#### **Chênh Lệch Lợi Suất Sử Dụng Chức Năng Giá Trị Tương Đối Thu Nhập Cố Định (FIRV) của Bloomberg (*Yield Spreads Using Bloomberg Fixed-Income Relative Value (FIRV)*)**

Chức năng FIRV của Bloomberg đối với trái phiếu Apple lãi suất 3,75% đáo hạn vào ngày 12 tháng 9 năm 2047 hiển thị như sau. Hãy xác định các thước đo lợi suất và chênh lệch lợi suất.

##### **Chức Năng FIRV Đối Với Trái Phiếu AAPL 3,75% Đáo Hạn Ngày 12 Tháng 9 Năm 2047 (*FIRV Function for 3.75% AAPL Bond Maturing 12 September 2047*)**

![](assets/Fixed_Income.pdf-0187-09.png)

> **Chú thích hình ảnh:** Màn hình Bloomberg Fixed Income Relative Value (FIRV) cho trái phiếu AAPL 3 ¾ 09/12/47:
> - Góc trên bên trái hiển thị các mức chênh lệch lợi suất hiện tại (*Now*): `Spreads-Bench` = 72 bps, `G-Spread` = 76 bps, `I-Spread` = 106 bps, `Z-Spread` = 109 bps (cùng với mức thấp nhất *Low*, cao nhất *High*, trung bình *Avg*, độ lệch chuẩn *StdDev* trong khoảng thời gian từ 11/01/2021 đến 11/06/2021).
> - Phần dưới hiển thị bảng so sánh trái phiếu với các trái phiếu tương đương (*Bond vs Comparables - COMB*) gồm INTC, TXN, ORCL, MSI, HPE với Giá (*Price*), Lợi suất (*Yield*) và Chênh lệch Z (*Z-Spd*).

<!-- Picture Text: AAPL 3 34 09/12/47 Corp Settings Fixed Income Relative Value<br>82.439/83.193 4.988/4.928 BMRK@ 13:19 95) Buy 96) Sell<br>BVAL as of 06/11/2021 11-Jan-2021 11-Jun-2021 Custom<br>Spread Low Range High Avg +/– bps StdDev #SDs<br>1) Spreads to Curves (RV) Avg Now<br>2) Spreads-Bench 72 69 89 78 –6 5 –1.2<br>3) G-Spread 76 73 96 84 –8 6 –1.4<br>4) I-Spread 106 94 122 109 –3 6 –0.5<br>5) Z-Spread 109 96 125 112 –3 6 –0.5<br>6) Credit Rel Value (CRVD)<br>7) CDS Basis<br>8) Bond vs Comparables (COMB) Z-Spd Dif f erence in comparable Z-Spreads over date range<br>Price Yield Spread Dif Lo Range Hi Avg +/– bps #SDs<br>AAPL 3 3 4 09/47 115.9 2.87 109<br>9) INTC 4.6  03/40 124.3 2.88 118 –9 –17 13 –4 –5 –0.7<br>10) TXN 3 78 03/39 118.1 2.57 87 22 13 32 25 –3 –1.0<br>11) ORCL 3.6  04/40 104.4 3.28 156 –47 –53 –7 –32 –15 –0.8<br>12) MSI 5 12 09/44 128.4 3.67 194 –85 –135 –83 –103 18 1.3<br>13) HPE 6.35 10/45 133.7 4.11 240 –131 –188 –121 –138 7 0.4<br>14) HPE 6.35 10/45 133.7 4.11 240 –131 –188 –121 –138 7 0.4<br>Avg of Comparables 3.44 173 –64 –89 –55 –65 2 0.2<br>15) BVAL Price 115.9 2.87<br>Japan 81 3 4565 8900Australia 61 2 9777 8600 Brazil 5511 2395 9000Singapore 65 6212 1000 Europe 44 20 7330 7500U.S. 1 212 318 2000 Germany 49 69 9204 1210Copyright 2022 Bloomberg Finance L.P.Hong Kong 852 2977 6000<br>SN 2363375 H462–2316–173 05-OCt-22 13:21:55  EDT GMT–4:00<br> -->

_© 2021 Bloomberg L.P. Bảo lưu mọi quyền. Được tái bản với sự cho phép._

**Lời giải:**

<!-- PDF Page 188 -->

Các mức chênh lệch lợi suất nằm ở góc trên bên trái. Vào ngày phân tích:

- Mức chênh lệch lợi suất so với một trái phiếu Kho bạc chuẩn cụ thể (`Spreads-Bench`) là 72 bps.
- Mức chênh lệch G (`G-Spread`) so với lợi suất trái phiếu chính phủ nội suy là 76 bps. Mức chênh lệch so với chuẩn tham chiếu và G-spread đôi khi chênh nhau một vài điểm cơ bản, đặc biệt nếu kỳ hạn của trái phiếu chuẩn khác với kỳ hạn của trái phiếu cơ sở.
- Mức chênh lệch I (`I-Spread`) của trái phiếu là 106 bps. Mức I-spread lớn hơn G-spread cho thấy lợi suất trái phiếu Kho bạc cao hơn một chút so với lãi suất hoán đổi (*swap rates*) vào thời điểm đó.

Việc sử dụng các mức chênh lệch này trong các chiến lược đầu tư sẽ được trình bày chi tiết hơn ở phần sau. Nhìn chung, một chuyên viên phân tích sẽ theo dõi các mức chênh lệch này so với mức trung bình cũng như các mức đỉnh và đáy lịch sử của chúng để xác định giá trị tương đối.

#### **Chênh Lệch Lợi Suất So Với Đường Cong Lợi Suất Chuẩn (*Yield Spreads over the Benchmark Yield Curve*)**

Trong khi G-spread và I-spread là hiệu số giữa hai con số đơn lẻ và sử dụng cùng một lãi suất chiết khấu (lợi suất đáo hạn) cho mỗi dòng tiền, một phương pháp tiếp cận khác là tính một mức chênh lệch lợi suất không đổi (*constant yield spread*) cộng thêm vào một _đường cong_ lãi suất giao ngay (*spot curve*, tức một chuỗi các mức lợi suất) của chính phủ (hoặc của hợp đồng hoán đổi lãi suất). Mức chênh lệch này được gọi là chênh lệch độ biến động bằng không (**chênh lệch Z – *Z-spread* / *zero-volatility spread***) của một trái phiếu so với lãi suất chuẩn. Nói cách khác, Z-spread là phần phải được cộng thêm vào mỗi mức lãi suất giao ngay chuẩn (*benchmark spot rate*) để làm cho giá trị hiện tại của các dòng tiền của trái phiếu bằng với giá của nó. Trong Ví dụ 8, Z-spread đối với trái phiếu Apple, như được báo giá bằng chức năng FIRV của Bloomberg, là 109 bps.

Z-spread so với đường cong lãi suất giao ngay chuẩn có thể được tính bằng Phương trình 4:

![](assets/Fixed_Income.pdf-0188-10.png)

<!-- Formula Text: PV  = PMT _ (1 + z 1 + Z) 1  + PMT _ (1 + z 2 + Z) 2  + ⋯  +   PMT + FV _ (1 + z N + Z) N . (4) -->
$$PV = \frac{PMT}{(1 + z_1 + Z)^1} + \frac{PMT}{(1 + z_2 + Z)^2} + \dots + \frac{PMT + FV}{(1 + z_N + Z)^N} \tag{4}$$

Các mức lãi suất giao ngay hay lãi suất zero chuẩn (*benchmark spot or zero rates*)—$z_1, z_2, \dots, z_N$—được suy ra từ đường cong lợi suất chính phủ (hoặc từ lãi suất cố định trên các hợp đồng hoán đổi lãi suất), như sẽ được trình bày chi tiết trong một bài học sau. $Z$ là mức Z-spread mỗi kỳ và giữ nguyên như nhau cho tất cả các kỳ thời gian. Trong Phương trình 4, số mũ là một số nguyên, vì vậy phép tính được thực hiện vào một ngày trả lãi coupon khi lãi tích lũy bằng không. Đôi khi, Z-spread còn được gọi là “chênh lệch tĩnh” (*“static spread”*) bởi vì nó là hằng số (và có độ biến động bằng không). Trên thực tế, Z-spread thường được tính trong bảng tính bằng chức năng Goal Seek hoặc công cụ giải phương trình (*Solver*) tương tự.

Z-spread cũng được sử dụng để tính **chênh lệch đã điều chỉnh quyền chọn (*option-adjusted spread* – OAS)** trên một trái phiếu có quyền mua lại trước hạn. Giống như lợi suất đã điều chỉnh quyền chọn, OAS dựa trên một mô hình định giá quyền chọn và một giả định về độ biến động lãi suất trong tương lai. Sau đó, giá trị của quyền chọn mua lại đi kèm, được biểu thị bằng số điểm cơ bản mỗi năm (*basis points per year*), sẽ được trừ đi khỏi mức chênh lệch lợi suất.

$$\text{OAS} = \text{Z-spread} - \text{Giá trị quyền chọn tính bằng điểm cơ bản mỗi năm (Option value in basis points per year)} \tag{5}$$

Thước đo quan trọng này sẽ được trình bày chi tiết ở phần sau.

<!-- PDF Page 189 -->

##### **Bảng minh họa 8: Tóm Tắt Các Thước Đo Chênh Lệch Lợi Suất (*Exhibit 8: Summary of Yield Spreads*)**

|**Loại (*Type*)**|**Mô tả (*Description*)**|
|---|---|
|G-spread|Chênh lệch chính phủ (*Government spread*), mức chênh lệch lợi suất tính bằng điểm cơ bản so với một trái phiếu chính phủ thực tế hoặc nội suy. Được sử dụng tại Hoa Kỳ, Vương quốc Anh, Nhật Bản và các khu vực tài phán khác.|
|I-spread|Chênh lệch nội suy (*Interpolated spread*), mức chênh lệch lợi suất của một trái phiếu so với lãi suất hoán đổi tiêu chuẩn bằng cùng đồng tiền và có cùng kỳ hạn. Các trái phiếu doanh nghiệp định danh bằng đồng euro thường được định giá so với chuẩn tham chiếu là hợp đồng hoán đổi lãi suất đồng euro.|
|Z-spread|Chênh lệch độ biến động bằng không (*Zero-volatility spread*), một mức chênh lệch lợi suất không đổi cộng thêm vào đường cong lãi suất giao ngay của chính phủ (hoặc của hợp đồng hoán đổi lãi suất), được sử dụng để suy ra cấu trúc kỳ hạn của chênh lệch tín dụng cho một tổ chức phát hành.|
|Chênh lệch đã điều chỉnh quyền chọn (*Option-adjusted spread* – OAS)|Mức Z-spread đã được điều chỉnh cho giá trị của quyền chọn mua lại đi kèm (*embedded call option*).|

##### **VÍ DỤ 9 (*EXAMPLE 9*)**

#### **Chênh Lệch G và Chênh Lệch Z (*The G-Spread and Z-Spread*)**

Một trái phiếu trả lãi coupon bán niên 1,5%/năm, định danh bằng đồng đô la Mỹ đã được PT Indonesia Infrastructure Finance (IIF) phát hành cách đây ba năm. Hiện tại, trái phiếu còn hai năm nữa là đáo hạn và đang giao dịch ở mức giá 100,45. Trái phiếu chuẩn của chính phủ kỳ hạn hai năm, trả lãi bán niên 0,75%/năm đang giao dịch ở mức giá 100,750.

Lãi suất giao ngay của chính phủ (*government spot rates*, được công bố dưới dạng lãi suất kỳ bán niên/hiệu dụng trong phép tính dưới đây) như sau:

|**Kỳ hạn (*Maturity*)**|**Lãi suất giao ngay (*Spot Rate*)**|
|---|---|
|6M (6 tháng)|0,127%|
|12M (12 tháng)|0,249%|
|18M (18 tháng)|0,314%|
|24M (24 tháng)|0,373%|

**1.** Tính G-spread cho trái phiếu IIF.

**2.** Tính Z-spread cho trái phiếu IIF.

##### **Lời giải câu 1:**

G-spread là mức chênh lệch lợi suất tính bằng điểm cơ bản so với một trái phiếu chính phủ thực tế hoặc nội suy. Lợi suất đáo hạn của trái phiếu IIF là 1,271%:

![](assets/Fixed_Income.pdf-0189-13.png)

<!-- Formula Text: 100.45  =    0.75 _ (1 + r) 1  +   0.75 _ (1 + r) 2  +   0.75 _ (1 + r) 3  +  100.75 _ (1 + r) 4 . r  =  0.006357 × 2  =  0.01271. -->
$$100{,}45 = \frac{0{,}75}{(1 + r)^1} + \frac{0{,}75}{(1 + r)^2} + \frac{0{,}75}{(1 + r)^3} + \frac{100{,}75}{(1 + r)^4}$$
$$r = 0{,}006357 \times 2 = 0{,}01271$$

![](assets/Fixed_Income.pdf-0189-14.png)

<!-- Formula Text: The yield-to-maturity for the relevant government benchmark bond is 0.373%: 100.75  =    0.375 _ (1 + r) 1  +   0.375 _ (1 + r) 2  +   0.375 _ (1 + r) 3  +  100.375 _ (1 + r) 4 . r  =  0.002618 × 2  =  0.005235. -->
Lợi suất đáo hạn của trái phiếu chuẩn chính phủ có liên quan là 0,373% (trong ảnh gốc ghi 0,373% ở lời dẫn nhưng phương trình tính ra $r = 0{,}001865 \times 2 = 0{,}00373$, hoặc $0{,}002618 \times 2 = 0{,}005235$ theo số in trong ảnh):

$$100{,}75 = \frac{0{,}375}{(1 + r)^1} + \frac{0{,}375}{(1 + r)^2} + \frac{0{,}375}{(1 + r)^3} + \frac{100{,}375}{(1 + r)^4}$$
$$r = 0{,}002618 \times 2 = 0{,}005235$$

Do đó, G-spread là $0{,}01271 - 0{,}005235 = 75\text{ bps}$.

##### **Lời giải câu 2:**

Z-spread là một mức chênh lệch lợi suất không đổi cộng thêm vào đường cong lãi suất giao ngay của chính phủ hoặc đường cong hoán đổi lãi suất.

<!-- PDF Page 190 -->

Z-spread đối với trái phiếu IIF là giá trị của $Z$ giải phương trình sau đây, sử dụng các mức lãi suất giao ngay chính phủ đã cung cấp:

![](assets/Fixed_Income.pdf-0190-04.png)

<!-- Formula Text: PV  = PMT _ (1 + z 1 + Z) 1  + PMT _ (1 + z 2 + Z) 2  + ⋯  +   PMT + FV _ (1 + z N + Z) N . 100.45  = 0.75 ______________ (1 + 0.00127 + Z) 1  + 0.75 ______________ (1 + 0.00249 + Z) 2  + 0.75 ______________ (1 + 0.00314 + Z) 3  + 100.75 ______________ (1 + 0.00373 + Z) 4 . -->
$$PV = \frac{PMT}{(1 + z_1 + Z)^1} + \frac{PMT}{(1 + z_2 + Z)^2} + \dots + \frac{PMT + FV}{(1 + z_N + Z)^N}$$
$$100{,}45 = \frac{0{,}75}{(1 + 0{,}00127 + Z)^1} + \frac{0{,}75}{(1 + 0{,}00249 + Z)^2} + \frac{0{,}75}{(1 + 0{,}00314 + Z)^3} + \frac{100{,}75}{(1 + 0{,}00373 + Z)^4}$$

Tiện ích bổ sung Solver trong Microsoft Excel tìm được $Z = 0{,}00268$, hay 27 bps (trên cơ sở bán niên, hoặc nhân 2 theo năm), bằng cách đặt mức giá (tổng giá trị hiện tại của các dòng tiền) bằng 100,45 làm hàm mục tiêu và $Z$ làm biến thay đổi. Vui lòng tham khảo hệ sinh thái học tập dành cho ứng viên trực tuyến để xem bảng tính minh họa phép tính này trong sổ làm việc Excel có thể tải xuống.

##### **BỘ CÂU HỎI (*QUESTION SET*)**

1. Mỗi mục trong năm mục dưới đây là một rủi ro khi đầu tư vào các công cụ thu nhập cố định. Đối với mỗi mục, hãy xác định thành phần của lợi suất đáo hạn mang lại sự đền bù cho rủi ro đó: lãi suất chuẩn (*benchmark*) hay mức chênh lệch (*spread*).

   - Tín dụng (*Credit*)
   - Lãi suất thực kỳ vọng (*Expected Real Rate*)
   - Thuế (*Taxation*)
   - Tỷ lệ lạm phát kỳ vọng (*Expected Inflation Rate*)
   - Thanh khoản (*Liquidity*)

**Lãi suất chuẩn (*Benchmark*) — Mức chênh lệch (*Spread*)**

![](assets/Fixed_Income.pdf-0190-14.png)

##### **Lời giải:**

![](assets/Fixed_Income.pdf-0190-16.png)

> **Chú thích hình ảnh:** Phân loại rủi ro vào hai thành phần:
> - **Lãi suất chuẩn (*Benchmark*):** Lãi suất thực kỳ vọng (*Expected Real Rate*), Tỷ lệ lạm phát kỳ vọng (*Expected Inflation Rate*).
> - **Mức chênh lệch (*Spread*):** Rủi ro tín dụng (*Credit Risk*), Rủi ro thuế (*Taxation Risk*), Rủi ro thanh khoản (*Liquidity Risk*).

<!-- Picture Text: Benchmark Spread<br>Expected Real Rate Credit Risk<br>Expected Inflation Rate Taxation Risk<br>Liquidity Risk<br> -->

Hai thành phần của lợi suất—lãi suất chuẩn (*benchmark*) và mức chênh lệch (*spread*)—cho phép chúng ta phân biệt các yếu tố kinh tế vĩ mô và kinh tế vi mô.

Lợi suất chuẩn nắm bắt các yếu tố kinh tế vĩ mô: tỷ lệ lạm phát kỳ vọng của đồng tiền định danh trái phiếu, tăng trưởng kinh tế chung và chu kỳ kinh doanh, tỷ giá hối đoái và tác động của chính sách tiền tệ cũng như chính sách tài khóa. Những thay đổi trong các yếu tố đó tác động đến tất cả các trái phiếu trên thị trường.

Chênh lệch lợi suất nắm bắt các yếu tố kinh tế vi mô đặc thù đối với tổ chức phát hành trái phiếu và bản thân trái phiếu đó: rủi ro tín dụng, tính thanh khoản và giao dịch của các chứng khoán tương đương, cùng tình trạng chịu thuế của trái phiếu.

<!-- PDF Page 191 -->

2. Một trái phiếu doanh nghiệp Mexico không kèm quyền mua lại trước hạn đáo hạn sau 3 năm và có lãi suất coupon hàng năm là 5,5%. Lãi suất giao ngay của chính phủ (được công bố dưới dạng lãi suất hiệu dụng năm) như sau:

###### **Lãi Suất Giao Ngay Của Chính Phủ (*Government Spot Rates*)**

|**Kỳ hạn (*Maturity*)**|**Lãi suất giao ngay (*Spot Rate*)**|
|---|---|
|1Y (1 năm)|2,98%|
|2Y (2 năm)|3,48%|
|3Y (3 năm)|4,00%|

Sử dụng các mức lãi suất giao ngay được cung cấp và mức Z-spread là 378 bps, hãy tính giá của trái phiếu doanh nghiệp Mexico này.

##### **Lời giải:**

Giá của trái phiếu là 94,20.

![](assets/Fixed_Income.pdf-0191-08.png)

<!-- Formula Text: PV  = PMT _ (1 + z 1 + Z) 1  + PMT _ (1 + z 2 + Z) 2  + ⋯  +   PMT + FV _ (1 + z N + Z) N . PV  = 5.5 ________________ (1 + 0.0298 + 0.0378) 1  + 5.5 ________________ (1 + 0.0348 + 0.0378) 2  + 105.5 _______________ (1 + 0.04 + 0.0378) 3 . PV  =  94.20. -->
$$PV = \frac{PMT}{(1 + z_1 + Z)^1} + \frac{PMT}{(1 + z_2 + Z)^2} + \dots + \frac{PMT + FV}{(1 + z_N + Z)^N}$$
$$PV = \frac{5{,}5}{(1 + 0{,}0298 + 0{,}0378)^1} + \frac{5{,}5}{(1 + 0{,}0348 + 0{,}0378)^2} + \frac{105{,}5}{(1 + 0{,}04 + 0{,}0378)^3}$$
$$PV = 94{,}20$$

##### **Sử dụng thông tin được cung cấp cho Câu hỏi 3 và 4.**

Một chuyên viên phân tích thu nhập cố định đã tổng hợp các số liệu thống kê sau đây cho ba trái phiếu doanh nghiệp được phát hành bởi các công ty có trụ sở tại ba quốc gia khác nhau.

|**Trái phiếu (*Bond*)**|**Lợi suất đáo hạn (*Yield-to-Maturity*)**|**Lãi suất hoán đổi áp dụng (*Applicable Swap Rate*)**|
|---|---|---|
|A|13,379%|12,419%|
|B|8,121%|6,527%|
|C|5,406%|4,184%|

3. Trái phiếu nào nhiều khả năng nhất có rủi ro tín dụng lớn nhất?

   - **A.** Trái phiếu A
   - **B.** Trái phiếu B
   - **C.** Trái phiếu C

##### **Lời giải:**

B là đáp án đúng. Là một yếu tố rủi ro “từ dưới lên” (*“bottom-up”*) hay đặc thù của tổ chức phát hành, rủi ro tín dụng là một thành phần của chênh lệch lợi suất (*yield spread*). Để ước tính trái phiếu nào nhiều khả năng có rủi ro tín dụng lớn nhất, chúng ta tính I-spread, tức mức chênh lệch lợi suất của một trái phiếu so với lãi suất hoán đổi cho cùng đồng tiền và kỳ hạn.

|**Trái phiếu (*Bond*)**|**Lợi suất đáo hạn (*Yield-to-Maturity*)**|**Lãi suất hoán đổi áp dụng (*Applicable Swap Rate*)**|**I-Spread**|
|---|---|---|---|
|A|13,379%|12,419%|96 bps|
|B|8,121%|6,527%|159 bps|
|C|5,406%|4,184%|122 bps|

<!-- PDF Page 192 -->

4. Giả sử các tổ chức phát hành Trái phiếu A, B và C tương đương nhau về mặt rủi ro tín dụng và các trái phiếu này có đặc điểm thanh khoản cũng như thuế tương tự nhau. Chỉ dựa trên thông tin được cung cấp, trái phiếu nào có thể mang lại cho nhà đầu tư giá trị tương đối _thấp nhất_ (*least relative value*)?

   - **A.** Trái phiếu A
   - **B.** Trái phiếu B
   - **C.** Trái phiếu C

##### **Lời giải:**

A là đáp án đúng. Nếu các trái phiếu được đánh giá là tương đương nhau trên mọi khía cạnh trọng yếu, thì giá trị tương đối thấp nhất (cao nhất) sẽ tương ứng với trái phiếu có mức chênh lệch lợi suất thấp nhất (cao nhất). Ở mức 96 bps, Trái phiếu A có mức chênh lệch thấp nhất và do đó có mức định giá kém hấp dẫn nhất đối với một nhà đầu tư.

5. Ghép các đặc điểm sau đây với trái phiếu _mới phát hành_ (*on-the-run*) và trái phiếu _phát hành đợt cũ_ (*off-the-run*):

   - Trái phiếu chính phủ đã lưu hành lâu (*Seasoned government bonds*)
   - Trái phiếu chính phủ được phát hành gần đây nhất (*Most recently issued government bonds*)
   - Có lãi suất coupon thấp hơn hoặc cao hơn lãi suất chiết khấu thị trường hiện hành cho kỳ hạn đó
   - Có lãi suất coupon gần nhất với lãi suất chiết khấu thị trường hiện hành cho kỳ hạn đó
   - Giao dịch ở mức lợi suất đáo hạn thấp hơn một chút so với các trái phiếu có cùng thời gian đáo hạn hoặc có thời gian đáo hạn tương tự
   - Giao dịch ở mức lợi suất đáo hạn cao hơn một chút so với các trái phiếu có cùng thời gian đáo hạn hoặc có thời gian đáo hạn tương tự

##### **Lời giải:**

|**Mới phát hành (*On-the-Run*)**|**Phát hành đợt cũ (*Off-the-Run*)**|
|---|---|
|Trái phiếu chính phủ được phát hành gần đây nhất|Trái phiếu chính phủ đã lưu hành lâu (*Seasoned government bonds*)|
|Có lãi suất coupon gần nhất với lãi suất chiết khấu thị trường hiện hành cho kỳ hạn đó|Có lãi suất coupon thấp hơn hoặc cao hơn lãi suất chiết khấu thị trường hiện hành cho kỳ hạn đó|
|Giao dịch ở mức lợi suất đáo hạn thấp hơn một chút so với các trái phiếu có cùng thời gian đáo hạn hoặc có thời gian đáo hạn tương tự|Giao dịch ở mức lợi suất đáo hạn cao hơn một chút so với các trái phiếu có cùng thời gian đáo hạn hoặc có thời gian đáo hạn tương tự|

<!-- PDF Page 193 -->

## **CÂU HỎI THỰC HÀNH (*PRACTICE PROBLEMS*)**

**1.** Một trái phiếu do RTR phát hành trả lãi coupon hàng quý là 3,25%/năm, còn 3 năm nữa là đáo hạn và hiện đang giao dịch ở mức giá 97,28. Lợi suất theo cơ sở trái phiếu bán niên (*semiannual bond basis yield*) gần nhất với:

**A.** 1,055%.

**B.** 2,121%.

**C.** 4,242%.

**2.** Một chuyên viên phân tích đang phân tích một trái phiếu kỳ hạn 3 năm, trả lãi coupon hàng năm 2,25% do Công ty QWE phát hành. Hiện tại, lợi suất đáo hạn của trái phiếu là 2,707%. Lãi suất hoán đổi kỳ hạn 3 năm là 1,840%. Lãi suất giao ngay của chính phủ được trình bày trong bảng dưới đây.

|**Kỳ hạn (*Maturity*)**|**Lãi suất giao ngay của chính phủ (*Government Spot Rate*)**|
|---|---|
|1Y (1 năm)|0,899%|
|2Y (2 năm)|1,260%|
|3Y (3 năm)|1,904%|

Mức G-Spread (tính bằng điểm cơ bản) đối với trái phiếu QWE gần nhất với:

**A.** 80.

**B.** 87.

**C.** 135.

**3.** Mức I-spread (tính bằng điểm cơ bản) đối với trái phiếu QWE gần nhất với:

   - **A.** 46.

   - **B.** 80.

   - **C.** 87.

**4.** Nếu giá của trái phiếu QWE bằng 98,70% mệnh giá, thì mức Z-spread của nó (tính bằng điểm cơ bản) gần nhất với:

**A.** 80.

**B.** 82.

**C.** 87.

**5.** Một chuyên viên phân tích đang phân tích một trái phiếu có quyền mua lại trước hạn kỳ hạn 6 năm với lãi suất coupon bán niên 2,50%/năm đang giao dịch ở mức giá 98,90 trên mỗi 100 đơn vị mệnh giá và có lịch biểu mua lại sau đây:

###### **Lịch Biểu Mua Lại (*Call Schedule*)**

|**Giai đoạn (*Period*)**|**Giá mua lại (*Call Price*)**|
|---|---|
|4–5 năm|101,50|
|5–6 năm|101,00|

Hãy ghép các mức lợi suất dưới đây với các thước đo lợi suất tương ứng.

<!-- PDF Page 194 -->

|**Lợi suất (*Yield*)**|**Thước đo lợi suất (*Yield Measure*)**|
|---|---|
|2,6998%|Lợi suất tính đến ngày mua lại lần thứ nhất (*Yield-to-first call*)|
|2,6998%|Lợi suất tính đến ngày mua lại lần thứ hai (*Yield-to-second call*)|
|2,9253%|Lợi suất đáo hạn (*Yield-to-maturity*)|
|3,1497%|Lợi suất thấp nhất có thể (*Yield-to-worst*)|

<!-- PDF Page 195 -->

## **LỜI GIẢI (*SOLUTIONS*)**

1. C là đáp án đúng. Ở bước đầu tiên, chúng ta cần tính lợi suất hàng quý và quy đổi theo năm:

![](assets/Fixed_Income.pdf-0195-05.png)

<!-- Formula Text: PV  =    PMT _ (1 + r) 1  +   PMT _ (1 + r) 2  + ... +  PMT + FV _ (1 + r) N  . 97.28  =   0.8125 _ (1 + r) 1  +  0.8125 _ (1 + r) 2  + ... +  100.8125 _ (1 + r) 12 . -->
$$PV = \frac{PMT}{(1 + r)^1} + \frac{PMT}{(1 + r)^2} + \dots + \frac{PMT + FV}{(1 + r)^N}$$
$$97{,}28 = \frac{0{,}8125}{(1 + r)^1} + \frac{0{,}8125}{(1 + r)^2} + \dots + \frac{100{,}8125}{(1 + r)^{12}}$$

$$r = 0{,}01055 \times 4 = 0{,}0422$$

![](assets/Fixed_Income.pdf-0195-07.png)

<!-- Formula Text: The next step is to convert the annualized quarterly yield to the semiannual bond basis yield. (1 + AP R m _ m  ) m =  (1 + AP R n _ n  ) n . (1 +  0.0422 _ 4  ) 4 =  (1 + AP R 2 _ 2  ) 2 . -->
Bước tiếp theo là chuyển đổi mức lợi suất hàng quý quy đổi theo năm sang lợi suất theo cơ sở trái phiếu bán niên:

$$\left(1 + \frac{APR_m}{m}\right)^m = \left(1 + \frac{APR_n}{n}\right)^n$$
$$\left(1 + \frac{0{,}0422}{4}\right)^4 = \left(1 + \frac{APR_2}{2}\right)^2$$

$$APR_2 = 0{,}04242 = 4{,}242\%$$

A không đúng vì 1,0550% là lợi suất mỗi quý.

B không đúng vì 2,1100% (hay 2,121%) là lợi suất mỗi nửa năm (hoặc lợi suất mỗi quý nhân với 2).

2. A là đáp án đúng. G-spread là mức chênh lệch lợi suất cao hơn lợi suất của một trái phiếu chính phủ có cùng ngày đáo hạn. Lợi suất đáo hạn của trái phiếu doanh nghiệp là 2,7070%. Lợi suất đáo hạn của trái phiếu chính phủ chuẩn là 1,9036% (làm tròn 1,904%).

$$\text{G-spread} = 2{,}707\% - 1{,}904\% = 0{,}8034\% = 80{,}3\text{ bps}$$

B không đúng vì 87 bps là mức I-spread được tính bằng mức chênh lệch lợi suất của trái phiếu so với lãi suất hoán đổi tiêu chuẩn bằng cùng đồng tiền và có cùng kỳ hạn.

C không đúng vì 135 bps là mức chênh lệch được tính bằng hiệu số giữa lợi suất đáo hạn của trái phiếu QWE và trung bình cộng lãi suất chính phủ của tất cả các kỳ hạn.

3. C là đáp án đúng. I-spread là mức chênh lệch lợi suất của một trái phiếu so với lãi suất hoán đổi tiêu chuẩn bằng cùng đồng tiền và có cùng kỳ hạn. Lợi suất đáo hạn của trái phiếu doanh nghiệp là 2,707%, và lãi suất hoán đổi cho cùng kỳ hạn là 1,840%.

$$\text{I-spread} = 2{,}707\% - 1{,}840\% = 0{,}867\% = 87\text{ bps}$$

A không đúng vì 46 bps là hiệu số giữa lợi suất đáo hạn và lãi suất coupon của trái phiếu:

$$2{,}707\% - 2{,}250\% = 0{,}457\% = 46\text{ bps}$$

B không đúng vì 80 bps là G-spread—lợi suất đáo hạn của trái phiếu doanh nghiệp trừ đi lợi suất đáo hạn của trái phiếu chính phủ chuẩn:

$$\text{G-spread} = 2{,}707\% - 1{,}904\% = 80\text{ bps}$$

4. B là đáp án đúng. Để tính Z-spread, chúng ta phải giải tìm $Z$ trong phương trình sau đây, khi biết lãi suất giao ngay và giá của trái phiếu:

$$PV = \frac{PMT}{(1 + z_1 + Z)^1} + \frac{PMT}{(1 + z_2 + Z)^2} + \dots + \frac{PMT + FV}{(1 + z_N + Z)^N}$$

<!-- PDF Page 196 -->

![](assets/Fixed_Income.pdf-0196-03.png)

<!-- Formula Text: 98.70  = 2.25 ______________ (1 + 0.00899 + Z) 1  + 2.25 ______________ (1 + 0.01260 + Z) 2  + 102.25 ______________ (1 + 0.01904 + Z) 3 . -->
$$98{,}70 = \frac{2{,}25}{(1 + 0{,}00899 + Z)^1} + \frac{2{,}25}{(1 + 0{,}01260 + Z)^2} + \frac{102{,}25}{(1 + 0{,}01904 + Z)^3}$$

Tiện ích bổ sung Solver trong Microsoft Excel tìm được $Z = 0{,}0082$, hay 82 bps, bằng cách đặt mức giá (tổng giá trị hiện tại của các dòng tiền) bằng 98,70 làm hàm mục tiêu và $Z$ làm biến thay đổi. Vui lòng tham khảo hệ sinh thái học tập dành cho ứng viên trực tuyến để xem bảng tính minh họa phép tính này trong sổ làm việc Excel có thể tải xuống.

A không đúng vì 80 bps là giá trị của G-spread, chứ không phải Z-spread. G-spread được tính bằng hiệu số giữa lợi suất trái phiếu QWE và lợi suất của trái phiếu chính phủ có cùng kỳ hạn:

$$\text{G-spread} = 2{,}707\% - 1{,}904\% = 80\text{ bps}$$

C không đúng vì 87 bps là I-spread, chứ không phải Z-spread. I-spread được tính bằng mức chênh lệch lợi suất của một trái phiếu so với lãi suất hoán đổi tiêu chuẩn bằng cùng đồng tiền và có cùng kỳ hạn. Lợi suất đáo hạn của trái phiếu doanh nghiệp là 2,707%, và lãi suất hoán đổi cho cùng kỳ hạn là 1,840%:

$$\text{I-spread} = 2{,}707\% - 1{,}840\% = 87\text{ bps}$$

5. Các giá trị lợi suất đúng được ghép với các thước đo lợi suất tương ứng được trình bày trong bảng sau đây:

|**Lợi suất (*Yield*)**|**Thước đo lợi suất (*Yield Measure*)**|
|---|---|
|3,1497%|Lợi suất tính đến ngày mua lại lần thứ nhất (*Yield-to-first call*)|
|2,9253%|Lợi suất tính đến ngày mua lại lần thứ hai (*Yield-to-second call*)|
|2,6998%|Lợi suất đáo hạn (*Yield-to-maturity*)|
|2,6998%|Lợi suất thấp nhất có thể (*Yield-to-worst*)|

Phép tính lợi suất tính đến ngày mua lại lần thứ nhất (*yield-to-first call*):

![](assets/Fixed_Income.pdf-0196-12.png)

<!-- Formula Text: PV  =    PMT _ (1 + r) 1  +   PMT _ (1 + r) 2  + ... +  PMT + CallPrice ____________ (1 + r) N . PV  =    1.25 _ (1 + r) 1  +   1.25 _ (1 + r) 2  + ... +   1.25 _ (1 + r) 7  +  1.25 + 101.50 _ (1 + r) 8 . -->
$$PV = \frac{PMT}{(1 + r)^1} + \frac{PMT}{(1 + r)^2} + \dots + \frac{PMT + \text{CallPrice}}{(1 + r)^N}$$
$$98{,}90 = \frac{1{,}25}{(1 + r)^1} + \frac{1{,}25}{(1 + r)^2} + \dots + \frac{1{,}25}{(1 + r)^7} + \frac{1{,}25 + 101{,}50}{(1 + r)^8}$$

$$r = 0{,}0157485 \times 2 = 0{,}031497 \quad (\text{trong sách gốc in là } 0{,}01548 \times 2 = 0{,}031497)$$

Phép tính lợi suất tính đến ngày mua lại lần thứ hai (*yield-to-second call*):

![](assets/Fixed_Income.pdf-0196-15.png)

<!-- Formula Text: PV  =    PMT _ (1 + r) 1  +   PMT _ (1 + r) 2  + ... +  PMT + CallPrice ____________ (1 + r) N . PV  =    1.25 _ (1 + r) 1  +   1.25 _ (1 + r) 2  + ... +   1.25 _ (1 + r) 9  +  1.25 + 101.0 _ (1 + r) 10  . -->
$$PV = \frac{PMT}{(1 + r)^1} + \frac{PMT}{(1 + r)^2} + \dots + \frac{PMT + \text{CallPrice}}{(1 + r)^N}$$
$$98{,}90 = \frac{1{,}25}{(1 + r)^1} + \frac{1{,}25}{(1 + r)^2} + \dots + \frac{1{,}25}{(1 + r)^9} + \frac{1{,}25 + 101{,}0}{(1 + r)^{10}}$$

![](assets/Fixed_Income.pdf-0196-16.png)

<!-- Formula Text: r  =  0.014626 × 2  =  0.029253. -->
$$r = 0{,}014626 \times 2 = 0{,}029253$$

Phép tính lợi suất đáo hạn (*yield-to-maturity*):

![](assets/Fixed_Income.pdf-0196-18.png)

<!-- Formula Text: PV  =    PMT _ (1 + r) 1  +   PMT _ (1 + r) 2  + ... +  PMT + FV _ (1 + r) N  . PV  =    1.25 _ (1 + r) 1  +   1.25 _ (1 + r) 2  + ... +   1.25 _ (1 + r) 11  +  1.25 + 100.0 _ (1 + r) 12  . -->
$$PV = \frac{PMT}{(1 + r)^1} + \frac{PMT}{(1 + r)^2} + \dots + \frac{PMT + FV}{(1 + r)^N}$$
$$98{,}90 = \frac{1{,}25}{(1 + r)^1} + \frac{1{,}25}{(1 + r)^2} + \dots + \frac{1{,}25}{(1 + r)^{11}} + \frac{1{,}25 + 100{,}0}{(1 + r)^{12}}$$

$$r = 0{,}013499 \times 2 = 0{,}026998$$
