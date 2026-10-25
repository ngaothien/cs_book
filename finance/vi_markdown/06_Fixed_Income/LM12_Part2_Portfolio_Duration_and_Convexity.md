# Tập 6: Thu nhập Cố định (Fixed Income)
## Học phần 12: Độ lồi Trái phiếu Dựa trên Lợi suất và Các Đặc tính Danh mục Đầu tư (Yield-Based Bond Convexity and Portfolio Properties)
### Phần 2/2: Thời lượng và Độ lồi của Danh mục Đầu tư (Trang PDF 321–330)

---

<!-- PDF Page 321 -->

$$= 99.937$$

$$PV_- = \text{PRICE(DATE(2025,6,30),DATE(2032,6,30),0.0295,0.0294,100,2,0)} = 100.063$$

$$\text{ApproxModDur} = \frac{100.063 - 99.937}{2 \times (0.0001) \times 100} = 6.283$$

$$\text{ApproxCon} = \frac{100.063 + 99.937 - (2 \times 100)}{(0.0001)^2 \times 100} = 44.965$$

2. Tính $\text{MoneyDur}$ và $\text{MoneyCon}$ cho vị thế trái phiếu bằng cách sử dụng các kết quả từ Câu hỏi 1.

###### **Lời giải:**

$$\text{MoneyDur} \approx 6.283 \times \text{10,000,000 EUR} = \text{62,829,180 EUR}$$

$$\text{MoneyCon} \approx 44.965 \times \text{10,000,000 EUR} = \text{449,647,660 EUR}$$

3. Tính mức thay đổi giá ước tính trong vị thế trái phiếu của nhà đầu tư bằng cách sử dụng $\text{MoneyDur}$ và $\text{MoneyCon}$ đối với mức giảm 50 bp trong lợi suất đáo hạn.

###### **Lời giải:**

$$\Delta PV^{\text{Full}} \approx -(\text{62,829,180 EUR} \times -0.005) + \left[ \frac{1}{2} \times \text{449,647,660 EUR} \times (-0.005)^2 \right] = \text{319,767 EUR}$$

4. Tính chênh lệch giữa mức thay đổi giá ước tính và mức thay đổi giá thực tế khi lợi suất đáo hạn giảm 50 bp.

###### **Lời giải:**

$$PV^{\text{Full}} = \text{PRICE(DATE(2025,6,30),DATE(2032,6,30),0.0295,0.0245,100,2,0)} = 103.198$$

*(Lưu ý: trong bản gốc ghi `0.0345` do lỗi đánh máy của giáo trình khi tính cho mức giảm 50 bp từ `0.0295`, giá kết quả là `103.198`)*

Mức tăng thực tế trong giá trái phiếu là 3.1984%:

$$\Delta PV^{\text{Full}} = 3.1984\% \times \text{10,000,000 EUR} = \text{319,840 EUR}$$

Chênh lệch giữa mức thay đổi giá thực tế và ước tính là 73 EUR ($= 319,840 - 319,767$).

# **THỜI LƯỢNG VÀ ĐỘ LỒI CỦA DANH MỤC ĐẦU TƯ (PORTFOLIO DURATION AND CONVEXITY)** **<mark>4</mark>** 

- tính toán thời lượng và độ lồi của danh mục đầu tư (*portfolio duration and convexity*) và giải thích những hạn chế của các thước đo này 

Cũng giống như thời lượng và độ lồi cung cấp các thước đo về rủi ro lãi suất của một trái phiếu đơn lẻ, các thước đo này cũng có thể được sử dụng để đo lường rủi ro lãi suất của một danh mục đầu tư trái phiếu. Có hai cách để tính thời lượng và độ lồi của một danh mục đầu tư trái phiếu: 

**1.** Sử dụng trung bình có trọng số của thời gian nhận các dòng tiền _gộp_ (*aggregate cash flows*) 


<!-- PDF Page 322 -->

**2.** Sử dụng trung bình có trọng số của thời lượng và độ lồi của từng trái phiếu riêng lẻ cấu thành nên danh mục đầu tư 

Phương pháp thứ nhất là phương pháp đúng về mặt lý thuyết, nhưng rất khó sử dụng trong thực tế. Trọng tâm của chúng ta sẽ là phương pháp thứ hai vì nó thường được các nhà quản lý danh mục đầu tư thu nhập cố định sử dụng. Chúng ta cũng sẽ làm nổi bật những hạn chế của nó. 

Giả sử một nhà đầu tư định chế nắm giữ một danh mục đầu tư gồm hai trái phiếu với mệnh giá 50 triệu USD mỗi loại của trái phiếu BRWA kỳ hạn 5 năm và trái phiếu chính phủ Romania kỳ hạn 30 năm, với thông tin chi tiết như trong Bảng 6. Giả sử cả hai trái phiếu đều được định danh bằng đô la Mỹ (USD). 

**Bảng 6: Các Thông số Đầu vào để Xác định Thời lượng và Độ lồi của Danh mục Đầu tư (Exhibit 6: Inputs for Determining Portfolio Duration and Convexity)** 

|**Trái phiếu (Bond)**|**Kỳ hạn (Năm) (Maturity - Years)**|**Coupon (%)**|**Giá (Price)**|**Lợi suất (%) (Yield %)**|**Thời lượng (Duration)**|**Độ lồi (Convexity)**|
|---|---|---|---|---|---|---|
|BRWA|5|3.200|100.000|3.200|4.58676|24.23896|
|Romania|30|4.625|98.022|4.750|15.90637|369.64203|

|**Trái phiếu (Bond)**|**Mệnh giá (Par Value)**|**Giá trị Thị trường (Market Value)**|**Trọng số Danh mục (Portfolio Weight)**|
|---|---|---|---|
|BRWA|50,000,000|50,000,000|0.5050|
|Romania (*Romanian*)|50,000,000|49,011,224|0.4950|

Tổng giá trị thị trường của danh mục đầu tư là $\$99,011,224$, và danh mục đầu tư được phân bổ trọng số gần như ngang nhau xét theo giá trị thị trường giữa hai trái phiếu. Như đã lưu ý trước đó, thời lượng và độ lồi của một danh mục đầu tư được tính bằng trung bình có trọng số của các số liệu thống kê của từng trái phiếu riêng lẻ, với tỷ trọng giá trị thị trường trong tổng danh mục đầu tư làm trọng số. Trung bình có trọng số này xấp xỉ với thời lượng và độ lồi của danh mục đầu tư đúng về mặt lý thuyết và trở nên chính xác hơn khi sự khác biệt về lợi suất đáo hạn giữa các trái phiếu nhỏ hơn và khi đường cong lợi suất phẳng (*flat*). 

Với các trọng số danh mục đầu tư trong ví dụ đơn giản này, thời lượng và độ lồi của danh mục đầu tư được tính như sau: 

$$\text{Thời lượng điều chỉnh trung bình có trọng số} = (4.58676 \times 0.5050) + (15.90637 \times 0.4950) = 10.19004$$

$$\text{Độ lồi trung bình có trọng số} = (24.23896 \times 0.5050) + (369.64203 \times 0.4950) = 195.21581$$

Ưu điểm chính của phương pháp trung bình có trọng số này là nó dễ dàng được sử dụng làm thước đo rủi ro lãi suất. Chẳng hạn, nếu lợi suất đáo hạn của mỗi trái phiếu trong danh mục đầu tư tăng 100 bps, thì mức sụt giảm ước tính trong giá trị danh mục đầu tư là 9.214%. 

$$\%\Delta PV^{\text{Full}} \approx (-10.19004 \times 0.0100) + \left[ \frac{1}{2} \times 195.21581 \times (0.0100)^2 \right] = -9.21396\%$$

Tuy nhiên, phương pháp này cũng đi kèm với một hạn chế: Các thước đo thời lượng và độ lồi của danh mục đầu tư này ngầm giả định rằng lợi suất của tất cả các kỳ hạn đều thay đổi cùng một lượng theo cùng một chiều, tức là một **sự dịch chuyển song song (*parallel shift*)** trong đường cong lợi suất. Trên thực tế, những sự dịch chuyển song song thuần túy rất hiếm khi xảy ra; thay vào đó, chúng ta thường xuyên quan sát thấy đường cong lợi suất dốc lên (*steepening*), phẳng ra (*flattening*), hoặc thậm chí xoắn lại (*twisting*). 


<!-- PDF Page 323 -->

##### **VÍ DỤ 2 (EXAMPLE 2)** 

#### **Thời lượng và Độ lồi của Danh mục Đầu tư (Portfolio Duration and Convexity)** 

Một nhà đầu tư định chế cân nhắc việc bổ sung một vị thế mới có mệnh giá 50 triệu USD bằng trái phiếu Kho bạc Hoa Kỳ (*US Treasury bond*) kỳ hạn 10 năm vào danh mục đầu tư hiện tại gồm trái phiếu BRWA và trái phiếu chính phủ Romania. Dữ liệu liên quan được thể hiện trong Bảng 7. 

**Bảng 7: Các Thông số Đầu vào để Xác định Thời lượng và Độ lồi của Danh mục Đầu tư (Exhibit 7: Inputs for Determining Portfolio Duration and Convexity)** 

|**Trái phiếu (Bond)**|**Kỳ hạn (Năm) (Maturity - Years)**|**Coupon (%)**|**Giá (Price)**|**Lợi suất (%) (Yield %)**|**Thời lượng (Duration)**|**Độ lồi (Convexity)**|
|---|---|---|---|---|---|---|
|BRWA|5|3.200|100.000|3.200|4.58676|24.23896|
|Romania (*Romanian*)|30|4.625|98.022|4.750|15.90637|369.64203|
|Kho bạc Hoa Kỳ (*US Treasury*)|10|1.500|98.168|1.700|9.23693|93.87376|

|**Trái phiếu (Bond)**|**Mệnh giá (USD) (Par Value)**|**Giá trị Thị trường (USD) (Market Value)**|**Trọng số Danh mục (Portfolio Weight)**|
|---|---|---|---|
|BRWA|50,000,000|50,000,000|0.33762|
|Romania|50,000,000|49,011,224|0.33094|
|Kho bạc Hoa Kỳ (*US Treasury*)|50,000,000|49,083,948|0.33144|

1. Tính thời lượng và độ lồi trung bình có trọng số cho danh mục đầu tư đề xuất. 

##### **Lời giải:** 

Với dữ liệu trong Bảng 7, thời lượng điều chỉnh và độ lồi trung bình có trọng số được tính như sau: 

$$\text{Thời lượng điều chỉnh trung bình có trọng số} = (4.58676 \times 0.33762) + (15.90637 \times 0.33094) + (9.23693 \times 0.33144)$$

$$= 9.87415$$

$$\text{Độ lồi trung bình có trọng số} = (24.23896 \times 0.33762) + (369.64203 \times 0.33094) + (93.87376 \times 0.33144)$$

$$= 161.62749$$

2. So sánh và diễn giải thời lượng và độ lồi của danh mục đầu tư đề xuất so với danh mục đầu tư hiện tại. 

##### **Lời giải:** 

Việc bổ sung vị thế trái phiếu Kho bạc Hoa Kỳ sẽ làm _giảm_ cả thời lượng của danh mục đầu tư (từ 10.19004 xuống 9.87415) và độ lồi (từ 195.21581 xuống 161.62749). Việc giảm thời lượng sẽ làm giảm rủi ro giá của danh mục đầu tư trước sự dịch chuyển song song đi lên của đường cong lợi suất, nhưng do độ lồi thấp hơn, mức giảm rủi ro này sẽ bị thu hẹp đối với những dịch chuyển lớn. 


<!-- PDF Page 324 -->

3. Khuyến nghị xem có nên bổ sung vị thế trái phiếu Kho bạc Hoa Kỳ hay không nếu nhà đầu tư kỳ vọng lợi suất dịch chuyển song song đi xuống 100 bp. 

##### **Lời giải:** 

Với kỳ vọng lợi suất dịch chuyển song song đi xuống 100 bp, nhà đầu tư không nên bổ sung vị thế trái phiếu Kho bạc Hoa Kỳ. Việc bổ sung vị thế này làm giảm cả thời lượng và độ lồi của danh mục đầu tư, điều này cũng sẽ làm giảm mức tăng kỳ vọng trong giá trị của danh mục đầu tư. Với quan điểm về đường cong lợi suất của nhà đầu tư, họ nên tìm cách tăng cả thời lượng và độ lồi của danh mục đầu tư. 

##### **BỘ CÂU HỎI (QUESTION SET)** 

Các câu hỏi 1–4 liên quan đến thông tin sau đây. 

Một nhà đầu tư mua 10 triệu EUR mệnh giá của mỗi loại gồm một trái phiếu không trả lãi định kỳ kỳ hạn 5 năm và một trái phiếu trả lãi coupon bán niên cố định kỳ hạn 10 năm. Chi tiết về các trái phiếu được thể hiện dưới đây. 

##### **Danh mục Đầu tư Hai Trái phiếu (Two-Bond Portfolio)** 

|**Trái phiếu (Bond)**|**Kỳ hạn (Năm) (Maturity - Years)**|**Coupon (%)**|**Giá (Price)**|**YTM (%)**|**Thời lượng (Duration)**|**Độ lồi (Convexity)**|
|---|---|---|---|---|---|---|
|Không trả lãi định kỳ (*Zero*)|5|0.00|83.18777|3.750|4.81928|27.87052|
|Bán niên (*Semi-annual*)|10|5.50|105.91556|4.750|7.71210|72.54897|

1. Tính thời lượng điều chỉnh trung bình có trọng số cho danh mục đầu tư. 

##### **Lời giải:** 

Giá trị thị trường của các trái phiếu như sau: 

- Trái phiếu không trả lãi định kỳ (*Zero-coupon*): $€10,000,000 \times 83.18777/100 = €8,318,777$. 

- Trái phiếu bán niên (*Semi-annual*): $€10,000,000 \times 105.91556/100 = €10,591,556$. 

Do đó, trọng số là 43.991% đối với trái phiếu không trả lãi định kỳ và 56.009% đối với trái phiếu bán niên. Kết quả là, thời lượng điều chỉnh trung bình có trọng số là 

$$(4.81928 \times 0.43991) + (7.71210 \times 0.56009) = 6.43953$$

2. Tính độ lồi trung bình có trọng số cho danh mục đầu tư. 

**Lời giải:** 

Sử dụng các trọng số đã tính trước đó, 

$$\text{Độ lồi trung bình có trọng số} = (27.87052 \times 0.43991) + (72.54897 \times 0.56009)$$

$$= 52.89463$$

3. Tính phần trăm thay đổi giá ước tính của danh mục đầu tư khi lợi suất đáo hạn của mỗi trái phiếu tăng 100 bp. 

   - **Lời giải:** 

$$\%\Delta PV^{\text{Full}} \approx (-6.43953 \times 0.0100) + \left[ \frac{1}{2} \times 52.89463 \times (0.0100)^2 \right] = -6.1751\%$$


<!-- PDF Page 325 -->

4. Dựa trên lạm phát gia tăng và chính sách tiền tệ thắt chặt, nhà đầu tư kỳ vọng lãi suất sẽ tăng. Với quan điểm đó, nhà đầu tư nên cân nhắc thay thế trái phiếu kỳ hạn 10 năm bằng trái phiếu nào? 

   - **A.** Một trái phiếu kỳ hạn 20 năm
   - **B.** Một trái phiếu lãi suất thả nổi kỳ hạn 15 năm 
   - **C.** Một trái phiếu kỳ hạn 10 năm có lãi suất coupon thấp hơn 

   - **Lời giải:** 

B là đáp án đúng. Khi lãi suất được kỳ vọng sẽ tăng, nhà đầu tư nên chọn một trái phiếu có rủi ro lãi suất thấp hơn. Cả trái phiếu kỳ hạn 20 năm và trái phiếu kỳ hạn 10 năm có lãi suất coupon thấp hơn đều sẽ có thời lượng cao hơn so với trái phiếu kỳ hạn 10 năm hiện tại, khi các yếu tố khác không đổi, và dự kiến sẽ chịu mức sụt giảm phần trăm giá lớn hơn nếu lãi suất tăng. Tuy nhiên, trái phiếu lãi suất thả nổi lại có rủi ro lãi suất thấp vì các khoản thanh toán coupon sẽ điều chỉnh theo sự thay đổi của lãi suất. 


<!-- PDF Page 326 -->

## **BÀI TẬP THỰC HÀNH (PRACTICE PROBLEMS)** 

**1.** Một trái phiếu trả lãi coupon cố định bán niên 5.5% được phát hành ngang mệnh giá vào ngày 1 tháng 5 năm 2025 và đáo hạn vào ngày 1 tháng 5 năm 2029. Đối với mức tăng và giảm 50 bps trong lợi suất đáo hạn, $PV_+$ và $PV_-$ lần lượt là 99.82283 và 100.177546. Độ lồi xấp xỉ _gần nhất_ với: 

   - **A.** 3.548. 

   - **B.** 15.045. 

   - **C.** 101.793. 

**2.** Một trái phiếu trả lãi coupon cố định bán niên là 4.70%. Nó giao dịch ngang mệnh giá vào ngày trả coupon là ngày 16 tháng 12 năm 2025 và đáo hạn vào ngày 16 tháng 12 năm 2033. Số liệu thống kê độ lồi năm hóa của trái phiếu _gần nhất_ với: 

   - **A.** 51.670. 

   - **B.** 53.231. 

   - **C.** 206.681. 

**3.** Đối với những thay đổi trong lợi suất đáo hạn, phần điều chỉnh độ lồi là _cần thiết nhất_ để tính đến: 

   - **A.** tác động bậc nhất lên giá trái phiếu. 

   - **B.** rủi ro giá trái phiếu do những thay đổi nhỏ trong lợi suất đáo hạn. 

   - **C.** mối quan hệ phi tuyến tính giữa giá trái phiếu và lợi suất đáo hạn. 

### **Thông tin sau đây liên quan đến các câu hỏi 4–9** 

Một danh mục đầu tư trái phiếu bao gồm ba trái phiếu lãi suất cố định, không kèm quyền chọn sau đây: 

|**Trái phiếu (Bond)**|**Giá trị Thị trường (£) (Market Value)**|**Thời lượng Điều chỉnh Hàng năm (Annual Modified Duration)**|**Độ lồi Hàng năm (Annual Convexity)**|
|---|---|---|---|
|X|5,000,000|3.6239|16.2513|
|Y|5,000,000|9.0036|91.0278|
|Z|10,000,000|12.7512|179.8591|

**4.** Nếu lợi suất đáo hạn của Trái phiếu X tăng 50 bps, phần trăm thay đổi giá kỳ vọng của Trái phiếu X _gần nhất_ với: 

   - **A.** 1.792%. 

   - **B.** 1.812%. 

   - **C.** 1.832%. 

**5.** Với mức thay đổi 75 bps trong lợi suất đáo hạn của Trái phiếu Y và Z, phần điều chỉnh độ lồi của Trái phiếu Z sẽ lớn hơn phần điều chỉnh độ lồi của Trái phiếu 


<!-- PDF Page 327 -->

Y: 

   - **A.** nếu mức thay đổi YTM là số dương. 

   - **B.** nếu mức thay đổi YTM là số âm. 

   - **C.** bất kể chiều hướng thay đổi của YTM. 

**6.** Đối với mức tăng 100 bps trong lợi suất đáo hạn và sử dụng thời lượng tiền tệ cùng độ lồi tiền tệ, mức thay đổi ước tính trong giá toàn phần của Trái phiếu Y _gần nhất_ với: 

   - **A.** 472,937 GBP. 

   - **B.** 450,180 GBP. 

   - **C.** 427,423 GBP. 

**7.** Đối với mức tăng 100 bps trong lợi suất đáo hạn và sử dụng thời lượng và độ lồi trung bình có trọng số, phần trăm thay đổi giá kỳ vọng của danh mục đầu tư trái phiếu _gần nhất_ với: 

   - **A.** 7.981%. 

   - **B.** 8.949%. 

   - **C.** 9.533%. 

**8.** Chuẩn tham chiếu (*benchmark*) của danh mục đầu tư trái phiếu là một chỉ số thu nhập cố định có thời lượng là 9.5325 và độ lồi là 103.0677. Dựa trên thời lượng và độ lồi trung bình có trọng số của danh mục đầu tư, danh mục đầu tư sẽ có thành quả vượt trội hơn chuẩn tham chiếu của nó trong kịch bản nào sau đây? 

   - **A.** Chỉ khi lãi suất đang tăng 

   - **B.** Chỉ khi lãi suất đang giảm 

   - **C.** Cả khi lãi suất đang tăng và đang giảm 

**9.** Phương pháp sử dụng các thước đo thời lượng và độ lồi trung bình có trọng số của danh mục đầu tư để đánh giá rủi ro giá của một danh mục đầu tư trái phiếu được mô tả _đúng nhất_ là: 

   - **A.** đúng về mặt lý thuyết. 

   - **B.** thường được sử dụng bởi các nhà quản lý danh mục đầu tư. 

   - **C.** tính đến được những sự dịch chuyển không song song (*non-parallel shifts*) trong đường cong lợi suất. 


<!-- PDF Page 328 -->

## **LỜI GIẢI (SOLUTIONS)** 

![](assets/Fixed_Income.pdf-0328-04.png)

<!-- Formula Text: 1.	 B is correct. ApproxCon  =   100.177546 + 99.82283 − (2 × 100) _________________________ (0.005) 2 × 100 =  15.04. -->

1. B là đáp án đúng.

$$\text{ApproxCon} = \frac{100.177546 + 99.82283 - (2 \times 100)}{(0.005)^2 \times 100} = 15.04$$

2. A là đáp án đúng. 

##### **Trái phiếu Bán niên 4.70%, Kỳ hạn 8 Năm (Eight-Year, 4.70% Semiannual Bond)** 

|Đặc điểm|Giá trị|
|---|---|
|**Lãi suất Coupon Cố định (%) (Fixed Coupon %)**|4.70|
|**Số kỳ mỗi năm (Periods p.a.)**|2|
|**Giá (trên 100 Mệnh giá) (Price per 100 Par Value)**|100|
|**Lợi suất Đáo hạn (%) (Yield-to-Maturity %)**|4.70|

|**Cột 1**|**Cột 2**|**Cột 3**|**Cột 4**|**Cột 5**|**Cột 6 = Cột 2 × Cột 5**|**Cột 7 = Cột 2 × (Cột 2 + 1) × Cột 5 × (1 + YTM/2)⁻²**|
|---|---|---|---|---|---|---|
|**Kỳ (Period)**|**Thời gian nhận (Time to Receipt)**|**Dòng tiền (Cash Flow)**|**Giá trị hiện tại (Present Value)**|**Trọng số (Weight)**|**Thời gian nhận × Trọng số (Time to Receipt × Weight)**|**Độ lồi của Dòng tiền (Convexity of Cash Flows)**|
|1|1.0|2.35|2.296043|0.02296|0.02296|0.04384|
|2|2.0|2.35|2.243325|0.02243|0.04487|0.12849|
|3|3.0|2.35|2.191817|0.02192|0.06575|0.25108|
|4|4.0|2.35|2.141492|0.02141|0.08566|0.40886|
|5|5.0|2.35|2.092323|0.02092|0.10462|0.59920|
|6|6.0|2.35|2.044282|0.02044|0.12266|0.81962|
|7|7.0|2.35|1.997344|0.01997|0.13981|1.06774|
|8|8.0|2.35|1.951484|0.01951|0.15612|1.34129|
|9|9.0|2.35|1.906677|0.01907|0.17160|1.63811|
|10|10.0|2.35|1.862899|0.01863|0.18629|1.95617|
|11|11.0|2.35|1.820126|0.01820|0.20021|2.29351|
|12|12.0|2.35|1.778336|0.01778|0.21340|2.64827|
|13|13.0|2.35|1.737504|0.01738|0.22588|3.01871|
|14|14.0|2.35|1.697610|0.01698|0.23767|3.40315|
|15|15.0|2.35|1.658632|0.01659|0.24879|3.80002|
|16|16.0|102.35|70.580104|0.70580|11.29282|183.26330|
||||**100.0000**|**1.00000**|**13.51910**|**206.68136**|
|**Độ lồi Năm hóa (Annualized Convexity)**||||||**51.67034**|

3. C là đáp án đúng. Phần điều chỉnh độ lồi là một thước đo rủi ro bổ sung cho thời lượng. Nó tính đến tác động bậc hai (phi tuyến tính) của những thay đổi lợi suất lên giá. Nó hữu ích nhất đối với những thay đổi lợi suất lớn, bởi vì thời lượng đã cung cấp một phép xấp xỉ tốt cho những thay đổi lợi suất nhỏ. 

4. A là đáp án đúng. Mức thay đổi giá kỳ vọng được tính như sau: 

$$\%\Delta PV^{\text{Full}} \approx (-3.6239 \times 0.005) + \left[ \frac{1}{2} \times 16.2513 \times (0.005)^2 \right]$$


<!-- PDF Page 329 -->

$$= -1.79164\% \approx -1.792\%$$

5. C là đáp án đúng. Vì phần điều chỉnh độ lồi sử dụng bình phương của mức thay đổi lợi suất, nên nó luôn mang giá trị dương bất kể chiều hướng thay đổi của lợi suất đáo hạn. Do đó, phần điều chỉnh độ lồi của Trái phiếu Z sẽ luôn lớn hơn phần điều chỉnh độ lồi của Trái phiếu Y, khi có cùng một mức thay đổi trong lợi suất đáo hạn. 

6. C là đáp án đúng. 

$$\text{MoneyDur} \approx 9.0036 \times 5,000,000 = 45,018,000$$

$$\text{MoneyCon} \approx 91.0278 \times 5,000,000 = 455,139,000$$

$$\Delta PV^{\text{Full}} \approx -(45,018,000 \times 0.01) + \left[ \frac{1}{2} \times 455,139,000 \times (0.01)^2 \right] = -\text{427,423 GBP}$$

7. B là đáp án đúng. Trọng số danh mục đầu tư cho các Trái phiếu X, Y và Z lần lượt là 0.25, 0.25 và 0.50. Các thước đo thời lượng và độ lồi trung bình có trọng số được tính như sau: 

$$\text{Thời lượng trung bình có trọng số} = (0.25 \times 3.6239) + (0.25 \times 9.0036) + (0.50 \times 12.7512) = 9.5325$$

$$\text{Độ lồi trung bình có trọng số} = (0.25 \times 16.2513) + (0.25 \times 91.0278) + (0.50 \times 179.8591)$$

$$= 116.7493$$

$$\%\Delta PV^{\text{Full}} \approx (-9.5325 \times 0.01) + \left[ \frac{1}{2} \times 116.7493 \times (0.01)^2 \right] = -8.9487\% \approx -8.949\%$$

8. C là đáp án đúng. Danh mục đầu tư có thời lượng trung bình có trọng số là 9.5325, giống hệt với thời lượng của chuẩn tham chiếu. Tuy nhiên, danh mục đầu tư có độ lồi cao hơn (116.7493) so với chuẩn tham chiếu (103.0677). Khi các yếu tố khác không đổi, danh mục đầu tư sẽ có thành quả vượt trội hơn danh mục chuẩn tham chiếu có độ lồi thấp hơn trong cả môi trường lãi suất tăng và giảm. 

9. B là đáp án đúng. Phương pháp thời lượng và độ lồi trung bình có trọng số của danh mục đầu tư rất dễ tính toán và áp dụng trong thực tế và thường được các nhà quản lý danh mục đầu tư sử dụng để đánh giá rủi ro giá của danh mục đầu tư trái phiếu. Tuy nhiên, phương pháp này ngầm giả định sự dịch chuyển song song trong đường cong lợi suất. Việc sử dụng trung bình có trọng số của thời gian nhận các dòng tiền gộp là phương pháp đúng về mặt lý thuyết để tính thời lượng và độ lồi của danh mục đầu tư, nhưng rất khó sử dụng trong thực tế. 


<!-- PDF Page 330 -->
