# Tập 1: Các Phương pháp Định lượng (*Quantitative Methods*)
## Học phần 10: Hồi quy Tuyến tính Đơn (*Simple Linear Regression*)
### Phần 2/6: Các Giả định của Mô hình Hồi quy Tuyến tính Đơn (Trang PDF 283–289)

---

<!-- PDF Page 283 -->

3. Mô hình hồi quy tuyến tính ước lượng này được biểu diễn như thế nào?

###### **Lời giải:**

Mô hình hồi quy được biểu diễn bởi $\hat{Y}_i = 16.5 - 1.3 X_i + \varepsilon_i$.

![](assets/Quantitative_method.pdf-0283-03.png)

<!-- Picture Text: 4. What is the pairwise correlation between NPM and RDR?<br>Solution:<br>The pairwise correlation is −0.8421:<br>r  =  ___________ − 39 ⧸_7  =  ____________ ( 3.1960− 5.5714 )( 2.0702 ) = − 0.8421.<br>√ _ 71.5⧸7 √30⧸7<br> -->

4. Hệ số tương quan cặp (*pairwise correlation*) giữa NPM và RDR là bao nhiêu?

###### **Lời giải:**

Hệ số tương quan cặp là $-0.8421$:

$$r = \frac{-39 / 7}{\sqrt{71.5 / 7} \sqrt{30 / 7}} = \frac{-5.5714}{(3.1960)(2.0702)} = -0.8421$$

## **CÁC GIẢ ĐỊNH CỦA MÔ HÌNH HỒI QUY TUYẾN TÍNH ĐƠN (*ASSUMPTIONS OF THE SIMPLE LINEAR REGRESSION MODEL*)**

# **<mark>3</mark>**

- giải thích các giả định cơ sở của mô hình hồi quy tuyến tính đơn, và mô tả cách phần dư (*residuals*) cùng đồ thị phần dư (*residual plots*) cho biết liệu các giả định này có thể đã bị vi phạm hay không

Chúng ta đã thảo luận về cách diễn giải các hệ số trong mô hình hồi quy tuyến tính đơn. Bây giờ chúng ta chuyển sang các giả định thống kê làm cơ sở cho mô hình này. Giả sử rằng chúng ta có $n$ quan sát của cả biến phụ thuộc, $Y$, và biến độc lập, $X$, và chúng ta muốn ước lượng hồi quy tuyến tính đơn của $Y$ theo $X$. Chúng ta cần đưa ra bốn giả định cốt lõi sau đây để có thể rút ra các kết luận hợp lệ từ một mô hình hồi quy tuyến tính đơn:

**1.** **Tính tuyến tính (*Linearity*)**: Mối quan hệ giữa biến phụ thuộc, $Y$, và biến độc lập, $X$, là tuyến tính.

**2.** **Phương sai sai số không đổi (*Homoskedasticity*)**: Phương sai của phần dư hồi quy là như nhau đối với tất cả các quan sát.

**3.** **Tính độc lập (*Independence*)**: Các quan sát, tức các cặp $Y$ và $X$, độc lập với nhau. Điều này ngụ ý rằng phần dư hồi quy không tương quan với nhau qua các quan sát.

**4.** **Tính phân phối chuẩn (*Normality*)**: Phần dư hồi quy có phân phối chuẩn.

Bây giờ chúng ta sẽ xem xét kỹ hơn từng giả định này và giới thiệu “thông lệ tốt nhất” (*best practice*) trong việc kiểm tra đồ thị phần dư (*residual plots*) của kết quả hồi quy nhằm nhận diện các vi phạm tiềm ẩn đối với những giả định cốt lõi này.

### **Giả định 1: Tính tuyến tính (*Linearity*)**

Chúng ta đang khớp một mô hình tuyến tính, vì vậy chúng ta phải giả định rằng mối quan hệ thực sự ngầm định giữa biến phụ thuộc và biến độc lập là tuyến tính. Nếu mối quan hệ giữa biến độc lập và biến phụ thuộc là phi tuyến tính theo các tham số (*nonlinear in the parameters*), việc ước lượng mối quan hệ đó bằng mô hình hồi quy tuyến tính đơn sẽ tạo ra kết quả không hợp lệ: Mô hình sẽ bị chệch (*biased*), bởi vì nó sẽ ước lượng thấp hơn thực tế (*underestimate*) và ước lượng cao hơn thực tế (*overestimate*) biến phụ thuộc tại những điểm nhất định. Ví dụ, $Y_i = b_0 e^{b_1 X_i} + \varepsilon_i$ là phi tuyến tính theo $b_1$, vì vậy chúng ta không nên áp dụng mô hình hồi quy tuyến tính cho nó. Hình 10 cho thấy một ví dụ về mô hình hàm mũ này,

<!-- PDF Page 284 -->

với một đường hồi quy được chỉ ra. Bạn có thể thấy rằng đường thẳng này không khớp tốt với mối quan hệ này: Đối với các giá trị thấp hơn và cao hơn của $X$, mô hình tuyến tính ước lượng thấp hơn giá trị của $Y$, trong khi đối với các giá trị ở giữa, mô hình tuyến tính lại ước lượng cao hơn giá trị của $Y$.

**Hình 10: Minh họa Mối quan hệ Phi tuyến tính được Ước lượng như một Mối quan hệ Tuyến tính**

![](assets/Quantitative_method.pdf-0284-05.png)

<!-- Picture Text: Y<br> -->

![](assets/Quantitative_method.pdf-0284-06.png)

![](assets/Quantitative_method.pdf-0284-07.png)

<!-- Picture Text: X<br> -->
> **Chú thích hình ảnh:** Trục tung $Y$, trục hoành $X$. Các điểm dữ liệu đi theo đường cong hàm mũ nhưng được khớp bằng một đường thẳng hồi quy tuyến tính.

Một hàm ý khác của giả định này là biến độc lập, $X$, không được mang tính ngẫu nhiên; nghĩa là nó mang tính phi ngẫu nhiên (*non-stochastic*). Nếu biến độc lập là ngẫu nhiên, sẽ không có mối quan hệ tuyến tính nào giữa biến phụ thuộc và biến độc lập. Mặc dù ban đầu chúng ta có thể giả định rằng biến độc lập trong mô hình hồi quy không phải là ngẫu nhiên, nhưng giả định đó không phải lúc nào cũng đúng.

Khi chúng ta nhìn vào phần dư của một mô hình, điều chúng ta muốn thấy là phần dư mang tính ngẫu nhiên. Phần dư không được thể hiện bất kỳ quy luật (*pattern*) nào khi được vẽ theo biến độc lập. Như chúng ta trình bày trong Hình 11, phần dư từ hồi quy tuyến tính ở Hình 10 dường như không ngẫu nhiên mà thay vào đó, chúng thể hiện một mối quan hệ với biến độc lập, $X$, giảm xuống trong một khoảng giá trị của $X$ và tăng lên trong một khoảng khác.

#### **Hình 11: Minh họa Phần dư trong một Mối quan hệ Phi tuyến tính được Ước lượng như một Mối quan hệ Tuyến tính**

![](assets/Quantitative_method.pdf-0284-11.png)

<!-- Picture Text: Y<br> -->

![](assets/Quantitative_method.pdf-0284-12.png)

![](assets/Quantitative_method.pdf-0284-13.png)

<!-- Picture Text: X<br> -->
> **Chú thích hình ảnh:** Đồ thị phần dư theo biến độc lập $X$ tạo thành hình chữ U (ban đầu dương, sau đó âm ở đoạn giữa, rồi lại tăng lên dương ở cuối), cho thấy vi phạm giả định tính tuyến tính.

<!-- PDF Page 285 -->

### **Giả định 2: Phương sai sai số không đổi (*Homoskedasticity*)**

Giả định 2, rằng phương sai của phần dư là như nhau đối với tất cả các quan sát, được gọi là giả định **phương sai sai số không đổi (*homoskedasticity*)**. Về mặt ký hiệu, giả định này liên quan đến bình phương phần dư:

![](assets/Quantitative_method.pdf-0285-04.png)

<!-- Formula Text: E(ε i 2)  =  σ ε 2, i = 1, . . . , n. (8) -->
$$E(\varepsilon_i^2) = \sigma_\varepsilon^2, \quad i = 1, \dots, n \tag{8}$$

Nếu phần dư không có phương sai không đổi, tức là nếu phương sai của phần dư khác nhau qua các quan sát, thì chúng ta gọi hiện tượng này là **phương sai sai số thay đổi (*heteroskedasticity*)**.

Giả sử bạn đang kiểm tra một chuỗi thời gian của lãi suất ngắn hạn với vai trò là biến phụ thuộc và tỷ lệ lạm phát với vai trò là biến độc lập trong vòng 16 năm. Chúng ta có thể tin rằng lãi suất ngắn hạn ($Y$) và tỷ lệ lạm phát ($X$) phải có liên hệ với nhau (tức là lãi suất cao hơn khi tỷ lệ lạm phát cao hơn). Nếu chuỗi thời gian này kéo dài nhiều năm, với các hành động khác nhau của ngân hàng trung ương buộc lãi suất ngắn hạn phải ở mức thấp (một cách nhân tạo) trong tám năm cuối của chuỗi, thì rất có khả năng phần dư trong mô hình ước lượng này sẽ có vẻ như đến từ hai mô hình khác nhau. Chúng ta sẽ gọi tám năm đầu tiên là Chế độ 1 (*Regime 1* – lãi suất bình thường) và tám năm thứ hai là Chế độ 2 (*Regime 2* – lãi suất thấp). Nếu mô hình có mức độ phù hợp khác nhau trong hai chế độ, phần dư và phương sai của chúng sẽ khác nhau.

Bạn có thể thấy tình huống này trong Hình 12, thể hiện biểu đồ phân tán với một đường hồi quy ước lượng. Hệ số góc của đường hồi quy trong cả 16 năm là 1,1979.

**Hình 12: Biểu đồ phân tán của Lãi suất ($Y$) và Tỷ lệ Lạm phát ($X$)**

![](assets/Quantitative_method.pdf-0285-09.png)

<!-- Picture Text: Short-Term Interest Rate ( Y ,%)<br>5.0<br>4.5<br>4.0<br>3.5<br>3.0<br>2.5<br>2.0<br>1.5 Y  = 0.9954 + 1.1979 X<br>1.0<br>0.5<br>0<br>0 0.5 1.0 1.5 2.0 2.5 3.0<br>Rate of Inflation ( X ,%)<br>Short-Term Interest Rate ( Y ,%) Regression Line: All Years<br> -->
> **Chú thích hình ảnh:** Trục tung: Lãi suất ngắn hạn ($Y$, %). Trục hoành: Tỷ lệ lạm phát ($X$, %). Đường hồi quy cho tất cả các năm: $Y = 0.9954 + 1.1979X$.

Chúng ta vẽ đồ thị phần dư của mô hình này trong Hình 13 theo các năm. Trong đồ thị này, chúng ta chỉ ra khoảng cách hai độ lệch chuẩn tính từ mức 0 (giá trị trung bình của phần dư) cho phần dư của tám năm đầu tiên và sau đó làm tương tự cho tám năm thứ hai. Như bạn có thể thấy, phần dư có vẻ khác biệt giữa hai chế độ: sự biến thiên của phần dư trong tám năm đầu tiên nhỏ hơn nhiều so với sự biến thiên trong tám năm thứ hai.

<!-- PDF Page 286 -->

#### **Hình 13: Đồ thị Phần dư cho Mô hình Lãi suất ($Y$) theo Tỷ lệ Lạm phát ($X$)**

![](assets/Quantitative_method.pdf-0286-04.png)

<!-- Picture Text: Residual (%)<br>1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>–0.2<br>–0.4<br>–0.6<br>–0.8<br>–1.0<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16<br>Year<br>Residuals Regime 1 Residuals Regime 2<br>2 Standard Deviations below the Zero<br>2 Standard Deviations above the Zero<br> -->
> **Chú thích hình ảnh:** Trục tung: Phần dư (%). Trục hoành: Năm (từ 1 đến 16). Hiển thị Phần dư Chế độ 1 (Năm 1–8) có dải $\pm 2$ độ lệch chuẩn hẹp, và Phần dư Chế độ 2 (Năm 9–16) có dải $\pm 2$ độ lệch chuẩn rộng hơn nhiều.

Tại sao điều này lại xảy ra? Mô hình có vẻ hợp lý, nhưng khi chúng ta kiểm tra phần dư (Hình 13), một bước quan trọng trong việc đánh giá độ phù hợp của mô hình, chúng ta thấy rằng mô hình khớp tốt hơn ở một số năm so với những năm khác. Sự khác biệt về phương sai của phần dư giữa hai chế độ thể hiện rõ qua dải băng rộng hơn nhiều xung quanh phần dư của Chế độ 2 (giai đoạn lãi suất thấp). Điều này cho thấy sự vi phạm rõ ràng đối với giả định phương sai sai số không đổi (*homoskedasticity*).

Nếu chúng ta ước lượng một đường hồi quy cho từng chế độ, chúng ta có thể thấy rằng mô hình cho hai chế độ là khá khác nhau, như được trình bày trong Hình 14. Trong trường hợp Chế độ 1 (lãi suất bình thường), hệ số góc là 1,0247, trong khi ở Chế độ 2 (lãi suất thấp), hệ số góc là $-0,2805$. Tóm lại, sự phân cụm của phần dư thành hai nhóm có phương sai rất khác nhau chỉ ra rõ ràng sự tồn tại của các chế độ riêng biệt đối với mối quan hệ giữa lãi suất ngắn hạn và tỷ lệ lạm phát.

<!-- PDF Page 287 -->

#### **Hình 14: Các Đường hồi quy Ước lượng cho Hai Chế độ (*Two Regimes*)**

![](assets/Quantitative_method.pdf-0287-03.png)

<!-- Picture Text: Short-Term Interest Rate ( Y ,%)<br>5.0<br>4.5<br>4.0<br>3.5<br>3.0<br>Regime 1:<br>2.5 Y  = 1.4372 + 1.0247 X<br>2.0<br>1.5<br>1.0<br>Regime 2:<br>0.5 Y  = 1.6440 – 0.2805 X<br>0<br>0 0.5 1.0 1.5 2.0 2.5 3.0<br>Rate of Inflation ( X ,%)<br>Regime 1 Regime 1 Regression Line<br>Regime 2 Regime 2 Regression Line<br> -->
> **Chú thích hình ảnh:** Trục tung: Lãi suất ngắn hạn ($Y$, %). Trục hoành: Tỷ lệ lạm phát ($X$, %). Đường hồi quy Chế độ 1: $Y = 1.4372 + 1.0247X$. Đường hồi quy Chế độ 2: $Y = 1.6440 - 0.2805X$.

### **Giả định 3: Tính độc lập (*Independence*)**

Chúng ta giả định rằng các quan sát (các cặp $Y$ và $X$) không tương quan với nhau, nghĩa là chúng độc lập với nhau. Nếu có sự tương quan giữa các quan sát (tức là tự tương quan – *autocorrelation*), chúng không độc lập và các phần dư sẽ tương quan với nhau. Giả định rằng các phần dư không tương quan qua các quan sát cũng rất cần thiết để ước lượng chính xác phương sai của các **tham số ước lượng (*estimated parameters*)** của $b_0$ và $b_1$ (tức là $\hat{b}_0$ và $\hat{b}_1$) mà chúng ta sử dụng trong các kiểm định giả thuyết cho hệ số chặn và hệ số góc tương ứng. Điều quan trọng là phải kiểm tra xem liệu phần dư có thể hiện một quy luật (*pattern*) nào đó hay không, điều gợi ý sự vi phạm giả định này. Do đó, chúng ta cần kiểm tra trực quan và kiểm tra thống kê đối với phần dư của một mô hình hồi quy.

Hãy xem xét doanh thu hàng quý của một công ty được hồi quy qua 40 quý, như trình bày trong Hình 15, kèm theo đường hồi quy. Rõ ràng là các mức doanh thu này thể hiện một quy luật mang tính thời vụ (*seasonal pattern*), một dấu hiệu chỉ báo của hiện tượng tự tương quan (*autocorrelation*).

<!-- PDF Page 288 -->

**Hình 15: Hồi quy Doanh thu Hàng quý theo Thời gian (40 Quý)**

![](assets/Quantitative_method.pdf-0288-05.png)

<!-- Picture Text: Revenues (millions, €)( Y )<br>140,000<br>135,000<br>130,000<br>125,000<br>120,000<br>115,000<br>110,000<br>105,000 Y  = 108,502.3 + 609.6427<br>100,000<br>95,000<br>90,000<br>1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39<br>Quarter ( X )<br>Observed Quarterly Revenues: 1st-3rd Quarters<br>Observed Quarterly Revenues: 4th Quarter<br> -->
> **Chú thích hình ảnh:** Trục tung: Doanh thu (triệu €) ($Y$). Trục hoành: Quý ($X$, từ 1 đến 40). Đường hồi quy: $Y = 108,502.3 + 609.6427X$. Doanh thu quan sát của Quý 4 luôn vọt lên cao hơn hẳn so với Quý 1–3.

Trong Hình 16, chúng ta vẽ đồ thị phần dư từ mô hình này và thấy rằng có một quy luật lặp lại. Các phần dư này có tương quan với nhau, cụ thể là nhảy vọt lên vào Quý 4 và sau đó giảm trở lại vào quý tiếp theo. Tóm lại, các quy luật trong cả Hình 15 và Hình 16 đều cho thấy sự vi phạm giả định về tính độc lập.

**Hình 16: Đồ thị Phần dư cho Mô hình Doanh thu Hàng quý theo Thời gian**

![](assets/Quantitative_method.pdf-0288-08.png)

<!-- Picture Text: Residuals (millions, €)<br>15,000<br>10,000<br>5,000<br>0<br>–5,000<br>–10,000<br>1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39<br>Quarter<br>Residuals: 1st-3rd Quarters Residuals: 4th Quarter<br> -->
> **Chú thích hình ảnh:** Trục tung: Phần dư (triệu €). Trục hoành: Quý (từ 1 đến 40). Phần dư của Quý 1–3 luôn âm hoặc thấp, trong khi phần dư của Quý 4 luôn dương cao (khoảng $+10,000$).

### **Giả định 4: Tính phân phối chuẩn (*Normality*)**

Giả định về tính phân phối chuẩn đòi hỏi phần dư phải có phân phối chuẩn. Điều này không có nghĩa là biến phụ thuộc và biến độc lập phải có phân phối chuẩn; nó chỉ có nghĩa là phần dư từ mô hình có phân phối chuẩn. Tuy nhiên, khi ước lượng bất kỳ mô hình nào, thông lệ tốt là cần hiểu rõ phân phối của

<!-- PDF Page 289 -->

biến phụ thuộc và biến độc lập để dò tìm các giá trị ngoại lai (*outliers*). Một giá trị ngoại lai ở một hoặc cả hai biến số có thể ảnh hưởng đáng kể đến đường thẳng ước lượng đến mức mô hình ước lượng sẽ không còn khớp tốt đối với hầu hết các quan sát khác.

Với phần dư có phân phối chuẩn, chúng ta có thể kiểm định một giả thuyết cụ thể về mô hình hồi quy tuyến tính. Đối với các cỡ mẫu lớn, chúng ta có thể bỏ qua giả định về tính phân phối chuẩn bằng cách dựa vào định lý giới hạn trung tâm (*central limit theorem*); lý thuyết tiệm cận (*asymptotic theory* – xử lý các mẫu lớn) chỉ ra rằng trong nhiều trường hợp, các thống kê kiểm định (*test statistics*) được tạo ra bởi các chương trình hồi quy tiêu chuẩn vẫn hợp lệ ngay cả khi phần dư của mô hình không có phân phối chuẩn.

#### **BỘ CÂU HỎI (*QUESTION SET*)**

Một nhà phân tích đang nghiên cứu doanh thu của một công ty và ước lượng một mô hình chuỗi thời gian tuyến tính đơn bằng cách hồi quy doanh thu theo thời gian, trong đó thời gian—$1, 2, \dots, 15$—được đo bằng năm. Cô vẽ đồ thị doanh thu quan sát được của công ty và đường hồi quy ước lượng, như trình bày trong Hình 17. Cô cũng vẽ đồ thị phần dư từ mô hình hồi quy này, như trình bày trong Hình 18.

#### **Hình 17: Doanh thu theo Thời gian sử dụng Hồi quy Tuyến tính Đơn**

![](assets/Quantitative_method.pdf-0289-08.png)

<!-- Picture Text: Revenues (millions, €)( Y )<br>900<br>800<br>700<br>600<br>500<br>400<br>300<br>200<br>100<br>0<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15<br>Year ( X )<br>Observed Revenues Linear Prediction of Revenues<br> -->
> **Chú thích hình ảnh:** Trục tung: Doanh thu (triệu €) ($Y$). Trục hoành: Năm ($X$, từ 1 đến 15). Hiển thị Doanh thu quan sát (*Observed Revenues* - tăng theo đường cong) và Dự báo tuyến tính của doanh thu (*Linear Prediction of Revenues* - đường thẳng).

#### **Hình 18: Đồ thị Phần dư của Doanh thu theo Thời gian**

![](assets/Quantitative_method.pdf-0289-10.png)

<!-- Picture Text: Revenues (millions, €)( Y )<br>150<br>100<br>50<br>0<br>–50<br>–100<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15<br>Year ( X )<br> -->
> **Chú thích hình ảnh:** Trục tung: Phần dư doanh thu (triệu €). Trục hoành: Năm ($X$, từ 1 đến 15). Các điểm phần dư tạo thành đường cong hình chữ U rõ rệt.
