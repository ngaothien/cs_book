# Tập 1: Các Phương pháp Định lượng (*Quantitative Methods*)
## Học phần 10: Hồi quy Tuyến tính Đơn (*Simple Linear Regression*)
### Phần 3/6: Kiểm định Giả thuyết trong Mô hình Hồi quy Tuyến tính Đơn (Trang PDF 290–302)

---

<!-- PDF Page 290 -->

1. Dựa trên Hình 17 và Hình 18, hãy mô tả (các) giả định nào của hồi quy tuyến tính đơn mà mô hình của nhà phân tích có thể đang vi phạm.

###### **Lời giải:**

Mô hình đúng không phải là tuyến tính, như thấy rõ từ quy luật của doanh thu trong Hình 17. Trong những năm đầu (tức là năm 1 và 2) và những năm cuối (tức là năm 14 và 15), mô hình tuyến tính ước lượng thấp hơn thực tế (*underestimates*) doanh thu, trong khi đối với những năm ở giữa (tức là năm 7–11), mô hình tuyến tính lại ước lượng cao hơn thực tế (*overestimates*) doanh thu. Hơn nữa, quy luật cong của phần dư trong Hình 18 cho thấy khả năng có phương sai sai số thay đổi (*heteroskedasticity* – phần dư có phương sai không bằng nhau), thiếu tính độc lập giữa các quan sát (*lack of independence*), và không tuân theo phân phối chuẩn (*non-normality* – một mối quan ngại do cỡ mẫu nhỏ $n = 15$). Tóm lại, nhà phân tích cần lo ngại rằng mô hình của cô ấy vi phạm tất cả các giả định chi phối hồi quy tuyến tính đơn (tính tuyến tính, phương sai sai số không đổi, tính độc lập và tính phân phối chuẩn).

# **<mark>4</mark>**

### **KIỂM ĐỊNH GIẢ THUYẾT TRONG MÔ HÌNH HỒI QUY TUYẾN TÍNH ĐƠN (*HYPOTHESIS TESTS IN THE SIMPLE LINEAR REGRESSION MODEL*)**

- tính toán và diễn giải các thước đo mức độ phù hợp (*measures of fit*) cũng như thiết lập và đánh giá các kiểm định mức độ phù hợp (*tests of fit*) và kiểm định các hệ số hồi quy trong hồi quy tuyến tính đơn

#### **Phân tích Phương sai (*Analysis of Variance*)**

Mô hình hồi quy tuyến tính đơn đôi khi mô tả mối quan hệ giữa hai biến số khá tốt, nhưng đôi khi lại không. Chúng ta phải có khả năng phân biệt giữa hai trường hợp này để sử dụng phân tích hồi quy một cách hiệu quả. Hãy nhớ rằng mục tiêu của chúng ta là giải thích sự biến thiên của biến phụ thuộc. Vậy mục tiêu này đã đạt được tốt đến mức nào, với lựa chọn biến độc lập của chúng ta?

##### **_Phân rã Tổng Bình phương Toàn phần thành các Thành phần của Nó (*Breaking Down the Sum of Squares Total into Its Components*)_**

Chúng ta bắt đầu với tổng bình phương toàn phần (*sum of squares total* – SST) và sau đó chia nó thành hai phần: tổng bình phương sai số (*sum of squares error* – SSE) và **tổng bình phương hồi quy (*sum of squares regression* – SSR)**. Tổng bình phương hồi quy là tổng bình phương các chênh lệch giữa giá trị dự báo của biến phụ thuộc, $\hat{Y}_i$, dựa trên đường hồi quy ước lượng, và giá trị trung bình của biến phụ thuộc, $\bar{Y}$:

![](assets/Quantitative_method.pdf-0290-13.png)

<!-- Formula Text: ∑ i=1 n ( ˆ Y  i − _ Y ) 2. (9) -->
$$\text{SSR} = \sum_{i=1}^{n} (\hat{Y}_i - \bar{Y})^2 \tag{9}$$

Chúng ta đã định nghĩa tổng bình phương toàn phần (SST), là tổng biến thiên trong $Y$, và tổng bình phương sai số (SSE), là phần biến thiên không được giải thích (*unexplained variation*) trong $Y$. Lưu ý rằng tổng bình phương hồi quy (SSR) là phần biến thiên được giải thích (*explained variation*) trong $Y$. Do đó, như được minh họa trong Hình 19, $\text{SST} = \text{SSR} + \text{SSE}$, nghĩa là tổng biến thiên trong $Y$ bằng phần biến thiên được giải thích trong $Y$ cộng với phần biến thiên không được giải thích trong $Y$.

<!-- PDF Page 291 -->

**Hình 19: Phân rã Sự biến thiên của Biến phụ thuộc (*Breakdown of Variation of Dependent Variable*)**

![](assets/Quantitative_method.pdf-0291-03.png)

<!-- Picture Text: Sum of Squares Total (SST)<br>Σ ni =1( Yi  –  Y– ) 2<br>Sum of Squares Regression (SSR) Sum of Squares Error (SSE)<br>n ^<br>^ – n<br>Σ( Yi  –  Y ) 2 Σ i =1( Yi  –  Yi ) 2<br>i =1<br> -->
> **Chú thích hình ảnh:** Tổng bình phương toàn phần ($\text{SST} = \sum_{i=1}^n (Y_i - \bar{Y})^2$) được chia thành hai nhánh: Tổng bình phương hồi quy ($\text{SSR} = \sum_{i=1}^n (\hat{Y}_i - \bar{Y})^2$) và Tổng bình phương sai số ($\text{SSE} = \sum_{i=1}^n (Y_i - \hat{Y}_i)^2$).

Chúng ta trình bày sự phân rã công thức tổng bình phương toàn phần cho ví dụ hồi quy ROA của chúng ta trong Bảng 20. Tổng biến thiên của ROA mà chúng ta muốn giải thích (SST) là 239,50. Con số này bao gồm phần biến thiên không được giải thích (SSE) là 47,88, và phần biến thiên được giải thích (SSR) là 191,63. Các giá trị tổng bình phương này là các dữ liệu đầu vào quan trọng cho các thước đo mức độ phù hợp của đường hồi quy.

**Bảng 20: Phân rã Tổng Bình phương Toàn phần cho Mô hình ROA**

|**Công ty (*Company*)**|**ROA ($Y_i$)**|**CAPEX ($X_i$)**|**ROA dự báo ($\hat{Y}_i$)**|**Biến thiên cần giải thích $(Y_i - \bar{Y})^2$**|**Biến thiên không được giải thích $(Y_i - \hat{Y}_i)^2$**|**Biến thiên được giải thích $(\hat{Y}_i - \bar{Y})^2$**|
|---|---|---|---|---|---|---|
|A|6.0|0.7|5.750|42.25|0.063|45.563|
|B|4.0|0.4|5.375|72.25|1.891|50.766|
|C|15.0|5.0|11.125|6.25|15.016|1.891|
|D|20.0|10.0|17.375|56.25|6.891|23.766|
|E|10.0|8.0|14.875|6.25|23.766|5.641|
|F|20.0|12.5|20.500|56.25|0.250|64.000|
|||||239.50|47.88|191.625|
|Trung bình (*Mean*)|12.50||||||

*Tổng bình phương toàn phần (SST) = 239.50. Tổng bình phương sai số (SSE) = 47.88. Tổng bình phương hồi quy (SSR) = 191.63.*

#### **Các Thước đo Mức độ Phù hợp (*Measures of Goodness of Fit*)**

Chúng ta có thể sử dụng một số thước đo để đánh giá mức độ phù hợp (*goodness of fit*)—tức là mô hình hồi quy khớp với dữ liệu tốt đến mức nào. Những thước đo này bao gồm hệ số xác định (*coefficient of determination*), thống kê $F$ (*$F$-statistic*) cho kiểm định mức độ phù hợp, và sai số chuẩn của hồi quy (*standard error of the regression*).

<!-- PDF Page 292 -->

**Hệ số xác định (*coefficient of determination* – $R^2$)**, còn được gọi là $R$-bình phương (*$R$-squared*), là tỷ lệ phần trăm sự biến thiên của biến phụ thuộc được giải thích bởi biến độc lập:

![](assets/Quantitative_method.pdf-0292-05.png)

<!-- Formula Text: Coefficient of determination = Sum of squares regression ___________________ Sum of squares total Coefficient of determination = ∑ i=1 n (ˆ Y i − _ Y ) 2 ___________ ∑ i=1 n (Y i − _ Y ) 2 . (10) -->
$$\text{Hệ số xác định } (R^2) = \frac{\text{Tổng bình phương hồi quy (SSR)}}{\text{Tổng bình phương toàn phần (SST)}} = \frac{\sum_{i=1}^{n} (\hat{Y}_i - \bar{Y})^2}{\sum_{i=1}^{n} (Y_i - \bar{Y})^2} \tag{10}$$

Theo cách xây dựng, hệ số xác định nằm trong khoảng từ 0% đến 100%. Trong ví dụ ROA của chúng ta, hệ số xác định là $191.625 \div 239.50$, hay $0.8001$, nghĩa là 80,01% sự biến thiên trong ROA được giải thích bởi CAPEX. Trong hồi quy tuyến tính đơn, bình phương của hệ số tương quan cặp bằng với hệ số xác định:

![](assets/Quantitative_method.pdf-0292-07.png)

<!-- Formula Text: r 2  = ∑ i=1 n (ˆ Y i − _ Y ) 2 ____________ ∑ i=1 n (Y i − _ Y ) 2 =  R 2. (11) -->
$$r^2 = \frac{\sum_{i=1}^{n} (\hat{Y}_i - \bar{Y})^2}{\sum_{i=1}^{n} (Y_i - \bar{Y})^2} = R^2 \tag{11}$$

Trong phân tích hồi quy ROA trước đó của chúng ta, $r = 0.8945$, vì vậy bây giờ chúng ta thấy rằng $r^2$ thực sự bằng hệ số xác định ($R^2$), vì $(0.8945)^2 = 0.8001$.

Mặc dù hệ số xác định—phần biến thiên của biến phụ thuộc được giải thích bởi biến độc lập—mang tính mô tả, nhưng nó không phải là một kiểm định thống kê. Để xem liệu mô hình hồi quy của chúng ta có khả năng mang ý nghĩa thống kê hay không, chúng ta sẽ cần xây dựng một thống kê kiểm định có phân phối $F$ (*$F$-distributed test statistic*).

Nhìn chung, chúng ta sử dụng một thống kê kiểm định có phân phối $F$ để so sánh hai phương sai. Trong phân tích hồi quy, chúng ta có thể sử dụng thống kê kiểm định có phân phối $F$ để kiểm định xem liệu các hệ số góc trong một hồi quy có bằng 0 hay không, với các hệ số góc được ký hiệu là $b_i$, đối lập với giả thuyết đối rằng có ít nhất một hệ số góc khác 0:

![](assets/Quantitative_method.pdf-0292-11.png)

<!-- Formula Text: H0: b1 = b2 = b3 =. . . = bk= 0. -->
$$H_0: b_1 = b_2 = b_3 = \dots = b_k = 0$$

![](assets/Quantitative_method.pdf-0292-12.png)

<!-- Formula Text: Ha: At least one bk is not equal to zero. -->
$$H_a: \text{Có ít nhất một } b_k \text{ khác } 0$$

Đối với hồi quy tuyến tính đơn, các giả thuyết này được đơn giản hóa thành:

![](assets/Quantitative_method.pdf-0292-14.png)

<!-- Formula Text: H0: b1 = 0. Ha: b1 ≠ 0. -->
$$H_0: b_1 = 0$$
$$H_a: b_1 \neq 0$$

Thống kê kiểm định có phân phối $F$ được xây dựng bằng cách sử dụng tổng bình phương hồi quy (SSR) và tổng bình phương sai số (SSE), mỗi đại lượng được điều chỉnh theo bậc tự do (*degrees of freedom*); nói cách khác, nó là tỷ số của hai phương sai. Chúng ta chia tổng bình phương hồi quy cho số lượng biến độc lập, được ký hiệu là $k$. Trong trường hợp hồi quy tuyến tính đơn, $k = 1$, vì vậy chúng ta thu được **trung bình bình phương hồi quy (*mean square regression* – MSR)**, có giá trị bằng chính tổng bình phương hồi quy:

![](assets/Quantitative_method.pdf-0292-16.png)

<!-- Formula Text: MSR  = Sum of squares regression ___________________ k = ∑ i=1 n (ˆ Y i − _ Y ) 2 ___________ 1 . (12) -->
$$\text{MSR} = \frac{\text{Tổng bình phương hồi quy (SSR)}}{k} = \frac{\sum_{i=1}^{n} (\hat{Y}_i - \bar{Y})^2}{1} \tag{12}$$

Vì vậy, đối với hồi quy tuyến tính đơn:

![](assets/Quantitative_method.pdf-0292-18.png)

<!-- Formula Text: MSR  =  ∑ i=1 n (ˆ Y i − _ Y ) 2. (13) -->
$$\text{MSR} = \sum_{i=1}^{n} (\hat{Y}_i - \bar{Y})^2 \tag{13}$$

Tiếp theo, chúng ta tính **trung bình bình phương sai số (*mean square error* – MSE)**, bằng tổng bình phương sai số chia cho bậc tự do là $n - k - 1$. Trong hồi quy tuyến tính đơn, $n - k - 1$ trở thành $n - 2$:

![](assets/Quantitative_method.pdf-0292-20.png)

<!-- Formula Text: MSE  = Sum of squares error _______________ n − k − 1 , -->
$$\text{MSE} = \frac{\text{Tổng bình phương sai số (SSE)}}{n - k - 1}$$

<!-- PDF Page 293 -->

![](assets/Quantitative_method.pdf-0293-03.png)

<!-- Formula Text: MSE  = ∑ i=1 n (Y i − ˆ Y i) 2 ___________ n − 2 . -->

![](assets/Quantitative_method.pdf-0293-04.png)

<!-- Formula Text: (14) -->
$$\text{MSE} = \frac{\sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2}{n - 2} \tag{14}$$

Do đó, thống kê kiểm định có phân phối $F$ ($\text{MSR}/\text{MSE}$) là:

![](assets/Quantitative_method.pdf-0293-06.png)

<!-- Formula Text: F  = Sum of squares regression ___________________ k ________________ Sum of squares error _______________ n − k − 1 =   MSR _ MSE , F  = ∑ i=1 n ( ˆ Y  i − _ Y ) 2 ____________ 1 ___________ ∑ i=1 n (Y i −  ˆ Y  i) 2 ____________ n − 2 , (15) -->
$$F = \frac{\frac{\text{Tổng bình phương hồi quy}}{k}}{\frac{\text{Tổng bình phương sai số}}{n - k - 1}} = \frac{\text{MSR}}{\text{MSE}}, \quad F = \frac{\frac{\sum_{i=1}^{n} (\hat{Y}_i - \bar{Y})^2}{1}}{\frac{\sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2}{n - 2}} \tag{15}$$

phân phối theo 1 và $n - 2$ bậc tự do trong hồi quy tuyến tính đơn. Thống kê $F$ trong phân tích hồi quy là kiểm định một phía (*one sided*), với miền bác bỏ (*rejection region*) nằm ở phía bên phải, bởi vì chúng ta quan tâm đến việc liệu phần biến thiên trong $Y$ được giải thích (tử số) có lớn hơn phần biến thiên trong $Y$ không được giải thích (mẫu số) hay không.

#### **Kiểm định Giả thuyết cho Từng Hệ số Hồi quy Riêng lẻ (*Hypothesis Testing of Individual Regression Coefficients*)**

##### **_Kiểm định Giả thuyết đối với Hệ số góc (*Hypothesis Tests of the Slope Coefficient*)_**

Chúng ta có thể sử dụng thống kê $F$ để kiểm định ý nghĩa thống kê của hệ số góc (tức là liệu nó có khác 0 một cách có ý nghĩa thống kê hay không), nhưng chúng ta cũng có thể muốn thực hiện các kiểm định giả thuyết khác cho hệ số góc—ví dụ: kiểm định xem hệ số góc tổng thể có khác một giá trị cụ thể nào đó hay không hoặc liệu hệ số góc có dương hay không. Chúng ta có thể sử dụng thống kê kiểm định có phân phối $t$ (*$t$-distributed test statistic*) để kiểm định các giả thuyết như vậy về một hệ số hồi quy.

Giả sử chúng ta muốn kiểm tra định giá của một cổ phiếu bằng cách sử dụng mô hình thị trường (*market model*); chúng ta đặt giả thuyết rằng cổ phiếu có rủi ro hệ thống (*systematic risk*) ở mức trung bình (tức là rủi ro tương tự như rủi ro của thị trường), được đại diện bởi hệ số gắn với biến tỷ suất sinh lợi thị trường. Hoặc chúng ta có thể muốn kiểm định giả thuyết rằng dự báo của các nhà kinh tế học về tỷ lệ lạm phát là không chệch (*unbiased* – tức là xét trung bình, không ước lượng cao hơn hay thấp hơn tỷ lệ lạm phát thực tế). Trong mỗi trường hợp, bằng chứng có ủng hộ giả thuyết đó không? Những câu hỏi như thế này có thể được giải quyết bằng các kiểm định giả thuyết đối với hệ số góc hồi quy. Để kiểm định một giả thuyết về hệ số góc, chúng ta tính toán thống kê kiểm định bằng cách lấy hệ số góc ước lượng ($\hat{b}_1$) trừ đi hệ số góc tổng thể theo giả thuyết ($B_1$) và sau đó chia hiệu số này cho sai số chuẩn của hệ số góc, $s_{\hat{b}_1}$:

![](assets/Quantitative_method.pdf-0293-12.png)

<!-- Formula Text: t  = ˆ b  1 − B 1 _ s  ˆ b  1  . (16) -->
$$t = \frac{\hat{b}_1 - B_1}{s_{\hat{b}_1}} \tag{16}$$

Thống kê kiểm định này có phân phối $t$ với $n - k - 1$ hoặc $n - 2$ bậc tự do bởi vì có hai tham số (một hệ số chặn và một hệ số góc) đã được ước lượng trong hồi quy.

**Sai số chuẩn của hệ số góc (*standard error of the slope coefficient* – $s_{\hat{b}_1}$)** đối với hồi quy tuyến tính đơn là tỷ số giữa sai số chuẩn của ước lượng của mô hình ($s_e$), sẽ được giới thiệu sau, với căn bậc hai của sự biến thiên của biến độc lập:

![](assets/Quantitative_method.pdf-0293-15.png)

<!-- Formula Text: s  ˆ b  1  = s e ____________ √ _____________ ∑ i=1 n (X i − _ X ) 2 . (17) -->
$$s_{\hat{b}_1} = \frac{s_e}{\sqrt{\sum_{i=1}^{n} (X_i - \bar{X})^2}} \tag{17}$$

Chúng ta so sánh thống kê $t$ tính được với các giá trị tới hạn (*critical values*) để kiểm định giả thuyết. Lưu ý rằng mức độ biến thiên của biến độc lập càng lớn thì sai số chuẩn của hệ số góc càng thấp (Phương trình 17) và do đó thống kê $t$ tính được càng lớn (Phương trình 16). Nếu thống kê $t$ tính được nằm ngoài phạm vi của các giá trị $t$ tới hạn, chúng ta bác bỏ giả thuyết không (*reject the null hypothesis*), nhưng nếu thống kê $t$ tính được nằm trong phạm vi của các giá trị tới hạn, chúng ta không bác bỏ giả thuyết không (*fail to reject the null hypothesis*). Tương tự như kiểm định giá trị trung bình, giả thuyết đối (*alternative hypothesis*) có thể là hai phía (*two sided*) hoặc một phía (*one sided*).

<!-- PDF Page 294 -->

Hãy xem xét ví dụ hồi quy tuyến tính đơn trước đó của chúng ta với ROA là biến phụ thuộc và CAPEX là biến độc lập. Giả sử chúng ta muốn kiểm định xem liệu hệ số góc của CAPEX có khác 0 hay không nhằm xác nhận trực giác của chúng ta về một mối quan hệ có ý nghĩa thống kê giữa ROA và CAPEX. Chúng ta có thể kiểm định giả thuyết liên quan đến hệ số góc bằng quy trình sáu bước, như được trình bày trong Bảng 21. Kết quả của kiểm định này là chúng ta kết luận rằng hệ số góc khác 0; nghĩa là CAPEX là một biến giải thích có ý nghĩa thống kê đối với ROA.

**Bảng 21: Kiểm định Hệ số góc cho Hồi quy của ROA theo CAPEX**

|**Bước 1**|Phát biểu các giả thuyết.|$H_0: b_1 = 0$ đối lập với $H_a: b_1 \neq 0$|
|---|---|---|
|**Bước 2**|Xác định thống kê kiểm định phù hợp.|$t = \frac{\hat{b}_1 - B_1}{s_{\hat{b}_1}}$ với $6 - 2 = 4$ bậc tự do.|
|**Bước 3**|Xác định mức ý nghĩa (*level of significance*).|$\alpha = 5\%$.|
|**Bước 4**|Phát biểu quy tắc quyết định (*decision rule*).|Giá trị $t$ tới hạn (*Critical $t$-values*) $= \pm 2.776$.<br>Chúng ta có thể xác định giá trị này từ:<br>**Excel:**<br>*Giới hạn dưới (Lower):* `T.INV(0.025,4)`<br>*Giới hạn trên (Upper):* `T.INV(0.975,4)`<br>**R:** `qt(c(.025,.975),4)`<br>**Python:** `from scipy.stats import t`<br>*Giới hạn dưới (Lower):* `t.ppf(.025,4)`<br>*Giới hạn trên (Upper):* `t.ppf(.975,4)`<br>Chúng ta bác bỏ giả thuyết không nếu thống kê $t$ tính được nhỏ hơn $-2.776$ hoặc lớn hơn $+2.776$.|
|**Bước 5**|Tính toán thống kê kiểm định.|Hệ số góc là $1.25$ (Bảng 6).<br>Trung bình bình phương sai số (MSE) là $11.96875$ (Bảng 33).<br>Sự biến thiên của CAPEX là $122.640$ (Bảng 6).<br>$s_e = \sqrt{11.96875} = 3.459588$.<br>$s_{\hat{b}_1} = \frac{3.459588}{\sqrt{122.640}} = 0.312398$.<br>$t = \frac{1.25 - 0}{0.312398} = 4.00131$.|
|**Bước 6**|Đưa ra quyết định.|Bác bỏ giả thuyết không về hệ số góc bằng 0. Có đủ bằng chứng cho thấy hệ số góc khác 0.|

Một đặc điểm của hồi quy tuyến tính đơn là thống kê $t$ được sử dụng để kiểm định xem hệ số góc có bằng 0 hay không và thống kê $t$ để kiểm định xem hệ số tương quan cặp có bằng 0 hay không (tức là $H_0: \rho = 0$ đối lập với $H_a: \rho \neq 0$) có cùng một giá trị. Giống như kiểm định hệ số góc, cả giả thuyết đối hai phía và một phía đều có thể áp dụng cho kiểm định hệ số tương quan—ví dụ: $H_0: \rho \le 0$ đối lập với $H_a: \rho > 0$. Thống kê kiểm định để kiểm tra xem hệ số tương quan có bằng 0 hay không như sau:

![](assets/Quantitative_method.pdf-0294-07.png)

<!-- Formula Text: t  =   r √ _ n − 2 _ √ _ 1 − r 2  . (18) -->
$$t = \frac{r\sqrt{n - 2}}{\sqrt{1 - r^2}} \tag{18}$$

Trong ví dụ ROA được hồi quy theo CAPEX của chúng ta, hệ số tương quan ($r$) là $0.8945$. Để kiểm định xem hệ số tương quan này có khác 0 hay không, chúng ta thực hiện kiểm định giả thuyết được trình bày trong Bảng 22. Như bạn có thể thấy, chúng ta rút ra một kết luận tương tự như kết luận cho kiểm định hệ số góc của chúng ta, nhưng được diễn đạt theo mối tương quan giữa ROA và CAPEX: Có mối tương quan có ý nghĩa thống kê giữa ROA và CAPEX.

<!-- PDF Page 295 -->

**Bảng 22: Kiểm định Hệ số tương quan giữa ROA và CAPEX**

|**Bước 1**|Phát biểu các giả thuyết.|$H_0: \rho = 0$ đối lập với $H_a: \rho \neq 0$|
|---|---|---|
|**Bước 2**|Xác định thống kê kiểm định phù hợp.|$t = \frac{r\sqrt{n - 2}}{\sqrt{1 - r^2}}$ với $6 - 2 = 4$ bậc tự do.|
|**Bước 3**|Xác định mức ý nghĩa.|$\alpha = 5\%$.|
|**Bước 4**|Phát biểu quy tắc quyết định.|Giá trị $t$ tới hạn $= \pm 2.776$.<br>Bác bỏ giả thuyết không nếu thống kê $t$ tính được nhỏ hơn $-2.776$ hoặc lớn hơn $+2.776$.|
|**Bước 5**|Tính toán thống kê kiểm định.|$t = \frac{0.8945\sqrt{4}}{\sqrt{1 - 0.8001}} = 4.00163$.|
|**Bước 6**|Đưa ra quyết định.|Bác bỏ giả thuyết không về việc không có tương quan. Có đủ bằng chứng cho thấy hệ số tương quan giữa ROA và CAPEX khác 0.|

Một đặc điểm thú vị khác của hồi quy tuyến tính đơn là thống kê kiểm định được sử dụng để kiểm định mức độ phù hợp của mô hình (tức là thống kê kiểm định có phân phối $F$) có liên hệ với thống kê $t$ tính được dùng để kiểm định xem hệ số góc có bằng 0 hay không: $t^2 = F$; do đó, $4.00131^2 = 16.0104$.

Điều gì sẽ xảy ra nếu thay vào đó chúng ta muốn kiểm định xem liệu có mối quan hệ một-đối-một (*one-to-one relationship*) giữa ROA và CAPEX hay không, ngụ ý hệ số góc bằng $1.0$? Các giả thuyết sẽ trở thành $H_0: b_1 = 1$ và $H_a: b_1 \neq 1$. Thống kê $t$ tính được như sau:

![](assets/Quantitative_method.pdf-0295-07.png)

<!-- Formula Text: t  =   1.25 − 1 _ 0.312398   =  0.80026. -->
$$t = \frac{1.25 - 1}{0.312398} = 0.80026$$

Thống kê kiểm định tính được này nằm trong phạm vi của các giá trị tới hạn, $\pm 2.776$, vì vậy chúng ta không bác bỏ giả thuyết không: Không có đủ bằng chứng để chỉ ra rằng hệ số góc khác $1.0$.

Điều gì sẽ xảy ra nếu thay vào đó chúng ta muốn kiểm định xem liệu có hệ số góc dương hay tương quan dương như trực giác của chúng ta gợi ý hay không? Trong trường hợp này, tất cả các bước đều giống như trong Bảng 21 và Bảng 22 ngoại trừ các giá trị tới hạn bởi vì đây là các kiểm định một phía. Đối với kiểm định hệ số góc dương hoặc tương quan dương, giá trị tới hạn tại mức ý nghĩa 5% là $+2.132$. Chúng ta trình bày kiểm định giả thuyết cho hệ số góc dương và tương quan dương trong Bảng 23. Kết luận của chúng ta là có đủ bằng chứng để ủng hộ cả hệ số góc dương và tương quan dương.

**Bảng 23: Kiểm định Một phía cho Hệ số góc và Hệ số tương quan**

|||**Kiểm định Hệ số góc (*Test of the Slope*)**|**Kiểm định Hệ số tương quan (*Test of the Correlation*)**|
|---|---|---|---|
|**Bước 1**|Phát biểu các giả thuyết.|$H_0: b_1 \le 0$ đối lập với $H_a: b_1 > 0$|$H_0: \rho \le 0$ đối lập với $H_a: \rho > 0$|
|**Bước 2**|Xác định thống kê kiểm định phù hợp.|$t = \frac{\hat{b}_1 - B_1}{s_{\hat{b}_1}}$ với $6 - 2 = 4$ bậc tự do.|$t = \frac{r\sqrt{n - 2}}{\sqrt{1 - r^2}}$ với $6 - 2 = 4$ bậc tự do.|
|**Bước 3**|Xác định mức ý nghĩa.|$\alpha = 5\%$.|$\alpha = 5\%$.|
|**Bước 4**|Phát biểu quy tắc quyết định.|Giá trị $t$ tới hạn $= 2.132$.<br>Bác bỏ giả thuyết không nếu thống kê $t$ tính được lớn hơn $2.132$.|Giá trị $t$ tới hạn $= 2.132$.<br>Bác bỏ giả thuyết không nếu thống kê $t$ tính được lớn hơn $2.132$.|

<!-- PDF Page 296 -->

|||**Kiểm định Hệ số góc (*Test of the Slope*)**|**Kiểm định Hệ số tương quan (*Test of the Correlation*)**|
|---|---|---|---|
|**Bước 5**|Tính toán thống kê kiểm định.|$t = \frac{1.25 - 0}{0.312398} = 4.00131$|$t = \frac{0.8945\sqrt{4}}{\sqrt{1 - 0.8001}} = 4.00131$|
|**Bước 6**|Đưa ra quyết định.|Bác bỏ giả thuyết không. Có đủ bằng chứng cho thấy hệ số góc lớn hơn 0.|Bác bỏ giả thuyết không. Có đủ bằng chứng cho thấy hệ số tương quan lớn hơn 0.|

##### **_Kiểm định Giả thuyết đối với Hệ số chặn (*Hypothesis Tests of the Intercept*)_**

Chúng ta có thể muốn kiểm định xem liệu hệ số chặn tổng thể có bằng một giá trị cụ thể nào đó hay không. Để nhắc lại cách diễn giải hệ số chặn, hãy xem xét hồi quy tuyến tính đơn với tốc độ tăng trưởng doanh thu của một công ty là biến phụ thuộc ($Y$), và tốc độ tăng trưởng GDP của quốc gia sở tại là biến độc lập ($X$). Hệ số chặn là tốc độ tăng trưởng doanh thu của công ty nếu tốc độ tăng trưởng GDP là 0%.

![](assets/Quantitative_method.pdf-0296-07.png)

<!-- Formula Text: g g p The equation for the standard error of the intercept, s  ˆ b  0, is as follows: s  ˆ b  0  =  S e √ _______________ 1 _ n  + _ X  2 ___________ ∑ i=1 n (X i − _ X ) 2 . (19) -->
Phương trình tính sai số chuẩn của hệ số chặn, $s_{\hat{b}_0}$, như sau:

$$s_{\hat{b}_0} = s_e \sqrt{\frac{1}{n} + \frac{\bar{X}^2}{\sum_{i=1}^{n} (X_i - \bar{X})^2}} \tag{19}$$

Chúng ta có thể kiểm định xem liệu hệ số chặn có khác với giá trị theo giả thuyết, $B_0$, hay không bằng cách so sánh hệ số chặn ước lượng ($\hat{b}_0$) với hệ số chặn theo giả thuyết và sau đó chia hiệu số này cho sai số chuẩn của hệ số chặn:

![](assets/Quantitative_method.pdf-0296-09.png)

<!-- Formula Text: t intercept  = ˆ b  0 − B 0 _ s  ˆ b  0    = ˆ b  0 − B 0 _______________ S √ _______________ 1 _ n  + _ X  2 ___________ ∑ i-1 n (X i − _ X ) 2 . (20) -->
$$t_{\text{intercept}} = \frac{\hat{b}_0 - B_0}{s_{\hat{b}_0}} = \frac{\hat{b}_0 - B_0}{s_e \sqrt{\frac{1}{n} + \frac{\bar{X}^2}{\sum_{i=1}^{n} (X_i - \bar{X})^2}}} \tag{20}$$

Trong ví dụ hồi quy ROA, hệ số chặn là 4,875%. Giả sử chúng ta muốn kiểm định xem liệu hệ số chặn có lớn hơn 3% hay không. Kiểm định giả thuyết một phía được trình bày trong Bảng 24. Như bạn có thể thấy, chúng ta không bác bỏ giả thuyết không (Lưu ý: văn bản gốc tiếng Anh ở đoạn dẫn ghi nhầm "reject", nhưng trong Bảng 24 Bước 6 ghi chính xác là "Do not reject" vì $t = 0.7905 < 2.132$). Nói cách khác, không có đủ bằng chứng cho thấy nếu không có chi tiêu vốn ($\text{CAPEX} = 0$), ROA sẽ lớn hơn 3%.

**Bảng 24: Kiểm định Giả thuyết cho Hệ số chặn đối với Hồi quy của ROA theo CAPEX**

|**Bước 1**|Phát biểu các giả thuyết.|$H_0: b_0 \le 3\%$ đối lập với $H_a: b_0 > 3\%$|
|---|---|---|
|**Bước 2**|Xác định thống kê kiểm định phù hợp.|$t_{\text{intercept}} = \frac{\hat{b}_0 - B_0}{s_{\hat{b}_0}}$ với $6 - 2 = 4$ bậc tự do.|
|**Bước 3**|Xác định mức ý nghĩa.|$\alpha = 5\%$.|
|**Bước 4**|Phát biểu quy tắc quyết định.|Giá trị $t$ tới hạn $= 2.132$.<br>Bác bỏ giả thuyết không nếu thống kê $t$ tính được lớn hơn $2.132$.|
|**Bước 5**|Tính toán thống kê kiểm định.|$t_{\text{intercept}} = \frac{4.875 - 3.0}{3.4596 \times \sqrt{\frac{1}{6} + \frac{6.1^2}{122.64}}} = \frac{1.875}{3.4596 \times 0.68562} = 0.7905$|
|**Bước 6**|Đưa ra quyết định.|Không bác bỏ giả thuyết không. Không có đủ bằng chứng để chỉ ra rằng hệ số chặn lớn hơn 3%.|

<!-- PDF Page 297 -->

##### **_Kiểm định Giả thuyết của Hệ số góc khi Biến độc lập là một Biến chỉ báo (*Hypothesis Tests of Slope When the Independent Variable Is an Indicator Variable*)_**

Giả sử chúng ta muốn kiểm tra xem liệu các đợt công bố thu nhập hàng quý của một công ty có ảnh hưởng đến tỷ suất sinh lợi cổ phiếu hàng tháng của công ty đó hay không. Trong trường hợp này, chúng ta có thể sử dụng một **biến chỉ báo (*indicator variable*)**, hay biến giả (*dummy variable*), chỉ nhận các giá trị 0 hoặc 1 làm biến độc lập. Hãy xem xét trường hợp tỷ suất sinh lợi cổ phiếu hàng tháng của một công ty trong giai đoạn 30 tháng. Một mô hình hồi quy tuyến tính đơn để nghiên cứu câu hỏi này sẽ là tỷ suất sinh lợi hàng tháng, $\text{RET}$, được hồi quy theo biến chỉ báo, $\text{EARN}$, nhận giá trị bằng 0 nếu không có công bố thu nhập vào tháng đó và bằng 1 nếu có công bố thu nhập:

$$\text{RET}_i = b_0 + b_1 \text{EARN}_i + \varepsilon_i \tag{21}$$

Thiết lập hồi quy này cho phép chúng ta kiểm định xem liệu có sự khác biệt về tỷ suất sinh lợi giữa các tháng có công bố thu nhập so với các tháng không có công bố thu nhập hay không. Các quan sát và kết quả hồi quy được thể hiện bằng đồ thị trong Hình 25.

**Hình 25: Công bố Thu nhập, Biến giả và Tỷ suất sinh lợi Cổ phiếu**

![](assets/Quantitative_method.pdf-0297-07.png)

<!-- Picture Text: Monthly Return (%)<br>2.5<br>2.0<br>1.5<br>1.0<br>0.5<br>0<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30<br>Month<br>Returns for Announcement Months Returns for Months without Announcements<br>Mean Return for Announcement Months<br>Mean Return for Non-Announcement Months<br> -->
> **Chú thích hình ảnh:** Trục tung: Tỷ suất sinh lợi hàng tháng (%). Trục hoành: Tháng (từ 1 đến 30). Hiển thị Tỷ suất sinh lợi của các tháng có công bố (*Returns for Announcement Months*) với đường trung bình ở mức cao (~1,77%), và Tỷ suất sinh lợi của các tháng không có công bố (*Returns for Months without Announcements*) với đường trung bình ở mức thấp (~0,56%).

Rõ ràng có một số tháng mà tỷ suất sinh lợi khác biệt so với những tháng khác, và những tháng này tương ứng với các tháng có công bố thu nhập. Chúng ta ước lượng mô hình hồi quy tuyến tính đơn và thực hiện kiểm định giả thuyết theo cùng một cách giống như khi biến độc lập là một biến liên tục (*continuous variable*). Trong hồi quy tuyến tính đơn, ý nghĩa của hệ số chặn là giá trị dự báo của biến phụ thuộc nếu biến chỉ báo bằng 0. Hơn nữa, hệ số góc khi biến chỉ báo bằng 1 chính là chênh lệch giữa hai giá trị trung bình nếu chúng ta phân nhóm các quan sát theo biến chỉ báo. Kết quả của hồi quy được cho trong Phần A của Bảng 26.

**Bảng 26: Hồi quy và Kiểm định Sự khác biệt sử dụng Biến chỉ báo**

#### **A. Kết quả Ước lượng Hồi quy (*Regression Estimation Results*)**

||**Các hệ số ước lượng (*Estimated Coefficients*)**|**Sai số chuẩn của các hệ số (*Standard Error of Coefficients*)**|**Thống kê kiểm định tính được (*Calculated Test Statistic*)**|
|---|---|---|---|
|Hệ số chặn (*Intercept*)|0.5629|0.0560|10.0596|
|EARN|1.2098|0.1158|10.4435|

*Kết quả ước lượng hồi quy: Bậc tự do = 28.*

<!-- PDF Page 298 -->

*Giá trị $t$ tới hạn = $\pm 2.0484$ (mức ý nghĩa 5%).*

#### **B. Kiểm định Sự khác biệt giữa Hai Giá trị Trung bình (*Test of Differences in Means*)**

||**RET cho các tháng có công bố thu nhập**|**RET cho các tháng không có công bố thu nhập**|**Chênh lệch giữa hai trung bình (*Difference in Means*)**|
|---|---|---|---|
|Trung bình (*Mean*)|1.7727|0.5629|1.2098|
|Phương sai (*Variance*)|0.1052|0.0630||
|Số quan sát (*Observations*)|7|23||
|Phương sai gộp (*Pooled variance*)|||0.07202|
|Thống kê kiểm định tính được (*Calculated test statistic*)|||10.4435|

*Kiểm định sự khác biệt giữa hai giá trị trung bình: Bậc tự do = 28. Giá trị $t$ tới hạn = $\pm 2.0484$ (mức ý nghĩa 5%).*

Chúng ta có thể thấy những điều sau đây từ Phần A của Bảng 26:

- Hệ số chặn ($0.5629$) là giá trị trung bình của tỷ suất sinh lợi cho các tháng không có công bố thu nhập.

- Hệ số góc ($1.2098$) là mức chênh lệch giữa trung bình tỷ suất sinh lợi của các tháng có công bố thu nhập và các tháng không có công bố thu nhập.

- Chúng ta bác bỏ giả thuyết không cho rằng hệ số góc của $\text{EARN}$ bằng 0. Chúng ta cũng bác bỏ giả thuyết không cho rằng hệ số chặn bằng 0. Lý do là trong cả hai trường hợp, thống kê kiểm định tính được đều vượt quá giá trị $t$ tới hạn.

Chúng ta cũng có thể kiểm định xem liệu tỷ suất sinh lợi trung bình hàng tháng có như nhau đối với cả các tháng không có công bố thu nhập và các tháng có công bố thu nhập hay không bằng cách kiểm định giả thuyết sau:

$$H_0: \mu_{\text{RET}_{\text{earnings}}} = \mu_{\text{RET}_{\text{Non-earnings}}} \quad \text{và} \quad H_a: \mu_{\text{RET}_{\text{earnings}}} \neq \mu_{\text{RET}_{\text{Non-earnings}}}$$

Kết quả của kiểm định giả thuyết này được rút ra từ Phần B của Bảng 26. Như bạn có thể thấy, chúng ta bác bỏ giả thuyết không cho rằng không có sự khác biệt về giá trị trung bình của $\text{RET}$ giữa các tháng có công bố thu nhập và các tháng không có công bố thu nhập tại mức ý nghĩa 5%, bởi vì thống kê kiểm định tính được ($10.4435$) vượt quá giá trị tới hạn ($2.0484$).

##### **_Kiểm định Giả thuyết: Mức ý nghĩa và Trị số p (*Level of Significance and p-Values*)_**

Việc lựa chọn mức ý nghĩa (*significance level*) trong kiểm định giả thuyết luôn là vấn đề mang tính phán đoán. Các nhà phân tích thường chọn mức ý nghĩa $0.05$, biểu thị 5% khả năng bác bỏ giả thuyết không khi trên thực tế nó đúng (sai lầm Loại I – *Type I error*, hay dương tính giả – *false positive*). Tất nhiên, việc giảm mức ý nghĩa từ $0.05$ xuống $0.01$ làm giảm xác suất mắc sai lầm Loại I, nhưng nó cũng làm tăng xác suất mắc sai lầm Loại II (*Type II error*)—không bác bỏ giả thuyết không khi trên thực tế nó sai (tức là âm tính giả – *false negative*).

Trị số $p$ (*$p$-value*) là mức ý nghĩa nhỏ nhất mà tại đó giả thuyết không có thể bị bác bỏ. Trị số $p$ càng nhỏ thì cơ hội mắc sai lầm Loại I (tức là bác bỏ một giả thuyết không đúng) càng nhỏ, do đó khả năng mô hình hồi quy hợp lệ càng lớn. Ví dụ, nếu trị số $p$ là $0.005$, chúng ta bác bỏ giả thuyết không cho rằng tham số thực sự bằng 0 tại mức ý nghĩa 0,5% (độ tin cậy 99,5%).

<!-- PDF Page 299 -->

Trong hầu hết các gói phần mềm, trị số $p$ được cung cấp cho các hệ số hồi quy là dành cho kiểm định giả thuyết không rằng tham số thực sự bằng 0 đối lập với giả thuyết đối rằng tham số khác 0.

Trong ví dụ hồi quy ROA của chúng ta, thống kê $t$ tính được cho kiểm định xem liệu hệ số góc có bằng 0 hay không là $4.00131$. Trị số $p$ tương ứng với thống kê kiểm định này là $0.016$, có nghĩa là, giả sử giả thuyết không là đúng, có 1,6% khả năng quan sát được một thống kê kiểm định khắc nghiệt như giá trị đã quan sát, hoặc khắc nghiệt hơn. So sánh trị số $p$ này với mức ý nghĩa 5% (và các giá trị tới hạn $\pm 2.776$) giúp chúng ta dễ dàng bác bỏ giả thuyết không $H_0: b_1 = 0$.

Làm thế nào chúng ta xác định được các trị số $p$? Bởi vì đây là diện tích trong phân phối nằm bên ngoài thống kê kiểm định tính được, chúng ta cần nhờ đến các công cụ phần mềm. Đối với trị số $p$ tương ứng với $t = 4.00131$ từ ví dụ hồi quy ROA, chúng ta có thể sử dụng các hàm sau:

- **Excel:** `(1-T.DIST(4.00131,4,TRUE))*2`

- **R:** `(1-pt(4.00131,4))*2`

- **Python:** `from scipy.stats import t` *và* `(1 - t.cdf(4.00131,4))*2`

##### **BỘ CÂU HỎI (*QUESTION SET*)**

Thông tin sau đây áp dụng cho các câu hỏi 1–3:

Julie Moon là một nhà phân tích năng lượng đang kiểm tra mức tiêu thụ điện, dầu và khí tự nhiên ở các khu vực khác nhau qua các mùa khác nhau. Cô đã chạy một hồi quy đơn giải thích sự biến thiên trong mức tiêu thụ năng lượng như một hàm số của nhiệt độ. Tổng biến thiên (*total variation*) của biến phụ thuộc là $140.58$, và phần biến thiên được giải thích (*explained variation*) là $60.16$. Cô có 60 quan sát hàng tháng.

1. Tính hệ số xác định (*coefficient of determination*).

##### **Lời giải:**

Hệ số xác định là $0.4279$:

![](assets/Quantitative_method.pdf-0299-15.png)

<!-- Picture Text: ______________Explained variation _<br>=   60.16<br>Total variation 140.58  = 0.4279.<br> -->
$$R^2 = \frac{\text{Biến thiên được giải thích}}{\text{Tổng biến thiên}} = \frac{60.16}{140.58} = 0.4279$$

2. Tính thống kê $F$ (*$F$-statistic*) để kiểm định mức độ phù hợp của mô hình.

![](assets/Quantitative_method.pdf-0299-17.png)

<!-- Picture Text: Solution:<br>_________________ 60.16 ⧸1 _<br>F  =   =   60.16<br>1.3866  = 43.3882.<br>(140.58 − 60.16) ⧸(60 − 2)<br> -->

##### **Lời giải:**

$$F = \frac{60.16 / 1}{(140.58 - 60.16) / (60 - 2)} = \frac{60.16}{1.3866} = 43.3882$$

3. Tính độ lệch chuẩn mẫu (*sample standard deviation*) của mức tiêu thụ năng lượng hàng tháng.

##### **Lời giải:**

Phương sai mẫu của biến phụ thuộc sử dụng tổng biến thiên của biến phụ thuộc và chia cho số lượng quan sát trừ đi một:

![](assets/Quantitative_method.pdf-0299-21.png)

<!-- Formula Text: ∑ i=1 n (Y i − _ Y ) 2 _ n − 1    =   Total variation ___________ n − 1 =   140.58 _ 60 − 1   =  2.3827. -->
$$\frac{\sum_{i=1}^{n} (Y_i - \bar{Y})^2}{n - 1} = \frac{\text{Tổng biến thiên}}{n - 1} = \frac{140.58}{60 - 1} = 2.3827$$

Độ lệch chuẩn mẫu của biến phụ thuộc là căn bậc hai của phương sai, hay $\sqrt{2.3827} = 1.544$.

Thông tin sau đây áp dụng cho các câu hỏi 4–6:

<!-- PDF Page 300 -->

Một nhà phân tích quan tâm đến việc diễn giải kết quả và thực hiện các kiểm định giả thuyết cho ước lượng mô hình thị trường (*market model*) hồi quy tỷ suất sinh lợi hàng ngày của cổ phiếu ABC theo tỷ suất sinh lợi hàng ngày của Chỉ số Cổ phiếu Âu–Á–Phi (EAA) giả định, đại diện (*proxy*) cho thị trường chứng khoán của anh ấy. Anh ấy đã tạo ra các kết quả hồi quy được trình bày trong Bảng 27.

##### **Bảng 27: Kiểm định Giả thuyết Kết quả Hồi quy Tuyến tính Đơn – Kết quả Chọn lọc của Ước lượng Mô hình Thị trường cho Cổ phiếu ABC**

|Thống kê / Hệ số|Giá trị|
|---|---|
|Sai số chuẩn của ước lượng ($s_e$)|1.26|
|Độ lệch chuẩn của tỷ suất sinh lợi cổ phiếu ABC|0.80|
|Độ lệch chuẩn của tỷ suất sinh lợi Chỉ số Cổ phiếu EAA|0.70|
|Số lượng quan sát|1,200|
||*Các hệ số (Coefficients)*|
|Hệ số chặn (*Intercept*)|0.010|
|Hệ số góc của tỷ suất sinh lợi Chỉ số Cổ phiếu EAA|0.982|

4. Nếu các giá trị $t$ tới hạn là $\pm 1.96$ (tại mức ý nghĩa 5%), hệ số góc có khác 0 hay không?

##### **Lời giải:**

Đầu tiên, chúng ta tính sự biến thiên của biến độc lập bằng cách sử dụng độ lệch chuẩn của biến độc lập:

![](assets/Quantitative_method.pdf-0300-08.png)

<!-- Formula Text: ∑ i=1 n (X i − _ X ) 2  = ∑ i=1 n (X i − _ X ) 2 ___________ n − 1 × (n − 1). So, ∑ i=1 n (X i − _ X ) 2  =  0.70 2 × 1, 199  =  587.51. -->
$$\sum_{i=1}^{n} (X_i - \bar{X})^2 = \frac{\sum_{i=1}^{n} (X_i - \bar{X})^2}{n - 1} \times (n - 1)$$

Vì vậy,

$$\sum_{i=1}^{n} (X_i - \bar{X})^2 = 0.70^2 \times 1,199 = 587.51$$

Tiếp theo, sai số chuẩn của hệ số góc ước lượng là:

![](assets/Quantitative_method.pdf-0300-11.png)

<!-- Formula Text: s  ˆ b  1  = s e ____________ √ _____________ ∑ i=1 n (X i − _ X ) 2 =    1.26 _ √ _ 587.51    =  0.051983, and the test statistic is t  = ˆ b  1 − B 1 _ s  ˆ b  1    =   0.982 − 0 _ 0.051983   =  18.8907. -->
$$s_{\hat{b}_1} = \frac{s_e}{\sqrt{\sum_{i=1}^{n} (X_i - \bar{X})^2}} = \frac{1.26}{\sqrt{587.51}} = 0.051983$$

và thống kê kiểm định là:

$$t = \frac{\hat{b}_1 - B_1}{s_{\hat{b}_1}} = \frac{0.982 - 0}{0.051983} = 18.8907$$

Thống kê kiểm định tính được nằm ngoài phạm vi $\pm 1.96$, vì vậy chúng ta bác bỏ giả thuyết không cho rằng hệ số góc bằng 0.

5. Nếu các giá trị $t$ tới hạn là $\pm 1.96$ (tại mức ý nghĩa 5%), hệ số góc có khác $1.0$ hay không?

##### **Lời giải:**

Thống kê kiểm định tính được cho kiểm định xem liệu hệ số góc có bằng $1.0$ hay không là:

<!-- PDF Page 301 -->

$$t = \frac{0.982 - 1}{0.051983} = -0.3463$$

Thống kê kiểm định tính được nằm trong phạm vi $\pm 1.96$, vì vậy chúng ta không bác bỏ giả thuyết không cho rằng hệ số góc bằng $1.0$, đây là bằng chứng cho thấy hệ số góc tổng thể thực sự có thể bằng $1.0$.

6. Một nhà kinh tế học đã thu thập tỷ suất sinh lợi hàng tháng cho danh mục đầu tư của KDL và một chỉ số cổ phiếu đa dạng hóa. Dữ liệu thu thập được trình bày trong Bảng 28:

##### **Bảng 28: Tỷ suất sinh lợi Hàng tháng của KDL**

|**Tháng (*Month*)**|**Tỷ suất sinh lợi Danh mục đầu tư (%)**|**Tỷ suất sinh lợi Chỉ số (%)**|
|---|---|---|
|1|1.11|−0.59|
|2|72.10|64.90|
|3|5.12|4.81|
|4|1.01|1.68|
|5|−1.72|−4.97|
|6|4.06|−2.06|

Nhà kinh tế học đã tính hệ số tương quan giữa hai tỷ suất sinh lợi và thấy nó bằng $0.996$. Kết quả hồi quy với tỷ suất sinh lợi danh mục đầu tư là biến phụ thuộc và tỷ suất sinh lợi chỉ số là biến độc lập được cho trong Bảng 29:

##### **Bảng 29: Kết quả Hồi quy (*Regression Results*)**

|**Thống kê Hồi quy (*Regression Statistics*)**||
|---|---|
|$R^2$|0.9921|
|Sai số chuẩn (*Standard error*)|2.8619|
|Số quan sát (*Observations*)|6|

![](assets/Quantitative_method.pdf-0301-10.png)

|**Nguồn (*Source*)**|**Bậc tự do (*df*)**|**Tổng bình phương (*Sum of Squares*)**|**Trung bình bình phương (*Mean Square*)**|**$F$**|**Trị số $p$ (*$p$-Value*)**|
|---|---|---|---|---|---|
|Hồi quy (*Regression*)|1|4,101.6205|4,101.6205|500.7921|0.0000|
|Phần dư (*Residual*)|4|32.7611|8.1903|||
|Tổng (*Total*)|5|4,134.3815||||

||**Các hệ số (*Coefficients*)**|**Sai số chuẩn (*Standard Error*)**|**Thống kê $t$ (*$t$-Statistic*)**|**Trị số $p$ (*$p$-Value*)**|
|---|---|---|---|---|
|Hệ số chặn (*Intercept*)|2.2521|1.2739|1.7679|0.1518|
|Tỷ suất sinh lợi chỉ số (*Index return*, %)|1.0690|0.0478|22.3784|0.0000|

Khi xem xét lại kết quả, Andrea Fusilier nghi ngờ rằng chúng không đáng tin cậy. Cô phát hiện ra rằng tỷ suất sinh lợi của Tháng 2 lẽ ra phải là 7,21%

<!-- PDF Page 302 -->

và 6,49%, thay vì các giá trị lớn được hiển thị trong bảng đầu tiên. Việc sửa lại các giá trị này đã mang lại hệ số tương quan điều chỉnh là $0.824$ và kết quả hồi quy điều chỉnh trong Bảng 30:

**Bảng 30: Kết quả Hồi quy Đã điều chỉnh (*Revised Regression Results*)**

![](assets/Quantitative_method.pdf-0302-06.png)

<!-- Picture Text: Regression Statistics<br>R 2 0.6784<br>Standard error 2.0624<br>Observations 6<br>Sum of  Mean<br>Source df Squares Square F p -Value<br>Regression 1 35.8950 35.8950 8.4391 0.044<br>Residual 4 17.0137 4.2534<br>Total 5 52.91<br> -->

|**Thống kê Hồi quy (*Regression Statistics*)**||
|---|---|
|$R^2$|0.6784|
|Sai số chuẩn (*Standard error*)|2.0624|
|Số quan sát (*Observations*)|6|

|**Nguồn (*Source*)**|**Bậc tự do (*df*)**|**Tổng bình phương (*Sum of Squares*)**|**Trung bình bình phương (*Mean Square*)**|**$F$**|**Trị số $p$ (*$p$-Value*)**|
|---|---|---|---|---|---|
|Hồi quy (*Regression*)|1|35.8950|35.8950|8.4391|0.044|
|Phần dư (*Residual*)|4|17.0137|4.2534|||
|Tổng (*Total*)|5|52.91||||

||**Các hệ số (*Coefficients*)**|**Sai số chuẩn (*Standard Error*)**|**Thống kê $t$ (*$t$-Statistic*)**|**Trị số $p$ (*$p$-Value*)**|
|---|---|---|---|---|
|Hệ số chặn (*Intercept*)|2.2421|0.8635|2.5966|0.060|
|Hệ số góc (*Slope*)|0.6217|0.2143|2.9050|0.044|

Hãy giải thích dữ liệu sai đã ảnh hưởng đến kết quả như thế nào.

##### **Lời giải:**

Điểm dữ liệu Tháng 2 là một giá trị ngoại lai (*outlier*), nằm cách rất xa so với các giá trị dữ liệu khác. Bởi vì giá trị ngoại lai này là do lỗi nhập dữ liệu, việc sửa chữa giá trị ngoại lai giúp cải thiện tính hợp lệ và độ tin cậy của hồi quy. Trong trường hợp này, $R^2$ sau điều chỉnh thấp hơn (từ $0.9921$ xuống $0.6784$). Các giá trị ngoại lai đã tạo ra ảo giác về mức độ phù hợp tốt hơn từ mức $R^2$ cao hơn; các giá trị ngoại lai cũng đã làm thay đổi ước lượng của hệ số góc. Sai số chuẩn của ước lượng thấp hơn khi lỗi dữ liệu được sửa chữa (từ $2.8619$ xuống $2.0624$), do trung bình bình phương sai số (MSE) thấp hơn. Tại mức ý nghĩa $0.05$, cả hai mô hình đều phù hợp tốt. Sự khác biệt về mức độ phù hợp được minh họa trong Hình 31.
