# Tập 1: Các Phương pháp Định lượng (*Quantitative Methods*)
## Học phần 10: Hồi quy Tuyến tính Đơn (*Simple Linear Regression*)
### Phần 4/6: Dự báo trong Mô hình Hồi quy Tuyến tính Đơn (Trang PDF 303–317)

---

<!-- PDF Page 303 -->

![](assets/Quantitative_method.pdf-0303-02.png)

<!-- Picture Text: Exhibit 31: Fit of the Model with and without Data Errors<br>A. Before the Data Errors Are Corrected<br>Portfolio Return<br>80<br>70<br>60<br>50<br>40<br>30<br>20<br>10<br>0<br>–10<br>–20 0 20 40 60 80<br>Index Return<br>B. After the Data Errors Are Corrected<br>Portfolio Return (%)<br>8<br>6<br>4<br>2<br>0<br>–2<br>–4<br>–10 –5 0 5 10<br>Index Return (%)<br> -->
> **Chú thích hình ảnh (Hình 31: Mức độ phù hợp của Mô hình khi có và không có Lỗi dữ liệu):**
> - **A. Trước khi sửa lỗi dữ liệu (*Before the Data Errors Are Corrected*):** Trục tung: Tỷ suất sinh lợi danh mục đầu tư (từ $-10$ đến $80$). Trục hoành: Tỷ suất sinh lợi chỉ số (từ $-20$ đến $80$). Điểm dữ liệu ngoại lai ở góc trên bên phải kéo đường hồi quy đi qua nó, tạo cảm giác khớp gần như tuyệt đối.
> - **B. Sau khi sửa lỗi dữ liệu (*After the Data Errors Are Corrected*):** Trục tung: Tỷ suất sinh lợi danh mục đầu tư (%) (từ $-4$ đến $8$). Trục hoành: Tỷ suất sinh lợi chỉ số (%) (từ $-10$ đến $10$). Các điểm dữ liệu phân tán tự nhiên hơn quanh đường hồi quy.

## **DỰ BÁO TRONG MÔ HÌNH HỒI QUY TUYẾN TÍNH ĐƠN (*PREDICTION IN THE SIMPLE LINEAR REGRESSION MODEL*)**

# **<mark>5</mark>**

- mô tả việc sử dụng phân tích phương sai (*analysis of variance* – ANOVA) trong phân tích hồi quy, diễn giải kết quả ANOVA, và tính toán cũng như diễn giải sai số chuẩn của ước lượng (*standard error of estimate*) trong hồi quy tuyến tính đơn

- tính toán và diễn giải giá trị dự báo cho biến phụ thuộc (*dependent variable*), và khoảng dự báo (*prediction interval*) cho giá trị đó, khi biết mô hình hồi quy tuyến tính ước lượng và một giá trị của biến độc lập (*independent variable*)

### **ANOVA và Sai số chuẩn của Ước lượng trong Hồi quy Tuyến tính Đơn (*ANOVA and Standard Error of Estimate in Simple Linear Regression*)**

Chúng ta thường biểu diễn các tổng bình phương từ một mô hình hồi quy trong bảng **phân tích phương sai (*analysis of variance* – ANOVA)**, như trình bày trong Bảng 32, bao gồm các tổng bình phương (*sums of squares*), bậc tự do (*degrees of freedom*), trung bình bình phương (*mean squares*), và thống kê $F$ (*$F$-statistic*). Lưu ý rằng phương sai của biến phụ thuộc là tỷ số giữa tổng bình phương toàn phần (SST) và $n - 1$.

<!-- PDF Page 304 -->

**Bảng 32: Bảng Phân tích Phương sai (ANOVA) cho Hồi quy Tuyến tính Đơn**

|**Nguồn biến thiên (*Source*)**|**Tổng bình phương (*Sum of Squares*)**|**Bậc tự do (*Degrees of Freedom*)**|**Trung bình bình phương (*Mean Square*)**|**Thống kê $F$ (*$F$-Statistic*)**|
|---|---|---|---|---|
|Hồi quy (*Regression*)|$\text{SSR} = \sum_{i=1}^{n} (\hat{Y}_i - \bar{Y})^2$|$1$|$\text{MSR} = \frac{\sum_{i=1}^{n} (\hat{Y}_i - \bar{Y})^2}{1}$|$F = \frac{\text{MSR}}{\text{MSE}} = \frac{\frac{\sum_{i=1}^{n} (\hat{Y}_i - \bar{Y})^2}{1}}{\frac{\sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2}{n - 2}}$|
|Sai số (*Error*)|$\text{SSE} = \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2$|$n - 2$|$\text{MSE} = \frac{\sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2}{n - 2}$||
|Tổng (*Total*)|$\text{SST} = \sum_{i=1}^{n} (Y_i - \bar{Y})^2$|$n - 1$|||

Từ bảng ANOVA, chúng ta cũng có thể tính **sai số chuẩn của ước lượng (*standard error of the estimate* – $s_e$)**, còn được gọi là sai số chuẩn của hồi quy (*standard error of the regression*) hoặc căn bậc hai trung bình bình phương sai số (*root mean square error* – RMSE). Đại lượng $s_e$ là thước đo khoảng cách giữa các giá trị quan sát được của biến phụ thuộc và các giá trị được dự báo từ hồi quy ước lượng—$s_e$ càng nhỏ thì độ phù hợp của mô hình càng tốt. Cùng với hệ số xác định ($R^2$) và thống kê $F$, $s_e$ là một thước đo mức độ phù hợp của đường hồi quy ước lượng. Không giống như hệ số xác định và thống kê $F$ là các thước đo mức độ phù hợp mang tính tương đối (*relative measures of fit*), sai số chuẩn của ước lượng là một thước đo tuyệt đối (*absolute measure*) về khoảng cách từ biến phụ thuộc quan sát được đến đường hồi quy. Do đó, $s_e$ là một thống kê quan trọng được sử dụng để đánh giá mô hình hồi quy và được dùng để tính các khoảng dự báo (*prediction intervals*) cũng như thực hiện các kiểm định đối với các hệ số. Việc tính toán $s_e$ rất đơn giản một khi chúng ta có bảng ANOVA bởi vì nó là căn bậc hai của MSE:

![](assets/Quantitative_method.pdf-0304-07.png)

<!-- Formula Text: Standard error of the estimate (s e)  =  √ _ MSE   =  √ ____________ ∑ i=1 n (Y i −  ˆ Y  i) 2 ____________ n − 2 . (22) -->
$$\text{Sai số chuẩn của ước lượng } (s_e) = \sqrt{\text{MSE}} = \sqrt{\frac{\sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2}{n - 2}} \tag{22}$$

Chúng ta trình bày bảng ANOVA cho ví dụ hồi quy ROA của chúng ta trong Bảng 33 (dựa theo cấu trúc của Bảng 32). Tại mức ý nghĩa 5%, giá trị $F$ tới hạn cho kiểm định xem liệu mô hình có độ phù hợp tốt hay không (tức là liệu hệ số góc có khác 0 hay không) là $7.71$. Chúng ta có thể lấy giá trị tới hạn này theo các cách sau:

- *Excel*: `[F.INV(0.95,1,4)]`

- *R*: `[qf(.95,1,4)]`

- *Python*: `[from scipy.stats import f` *và* `f.ppf(.95,1,4)]`

Với thống kê $F$ tính được là $16.0104$ và giá trị $F$ tới hạn là $7.71$, chúng ta bác bỏ giả thuyết không và kết luận rằng hệ số góc của mô hình hồi quy tuyến tính đơn cho ROA của chúng ta khác 0.

**Bảng 33: Bảng ANOVA cho Mô hình Hồi quy ROA**

|**Nguồn biến thiên (*Source*)**|**Tổng bình phương (*Sum of Squares*)**|**Bậc tự do (*Degrees of Freedom*)**|**Trung bình bình phương (*Mean Square*)**|**Thống kê $F$ (*$F$-Statistic*)**|
|---|---|---|---|---|
|Hồi quy (*Regression*)|191.625|1|191.625|16.0104|
|Sai số (*Error*)|47.875|4|11.96875||
|Tổng (*Total*)|239.50|5|||

<!-- PDF Page 305 -->

Các phép tính để lập bảng ANOVA và cuối cùng là kiểm định mức độ phù hợp của mô hình hồi quy có thể tốn nhiều thời gian, đặc biệt đối với các mẫu có nhiều quan sát. Tuy nhiên, các gói thống kê như SAS, SPSS Statistics và Stata, cũng như các phần mềm như Excel, R và Python, đều tạo ra bảng ANOVA như một phần của kết quả đầu ra cho phân tích hồi quy.

### **Dự báo Sử dụng Hồi quy Tuyến tính Đơn và Khoảng Dự báo (*Prediction Using Simple Linear Regression and Prediction Intervals*)**

Các nhà phân tích tài chính thường muốn sử dụng kết quả hồi quy để đưa ra các dự báo về biến phụ thuộc. Ví dụ, chúng ta có thể hỏi, “Doanh số của Tập đoàn XYZ sẽ tăng trưởng nhanh như thế nào trong năm nay nếu GDP thực tăng trưởng 4%?” Nhưng chúng ta không chỉ đơn thuần quan tâm đến việc đưa ra các dự báo này; chúng ta còn muốn biết mình có thể chắc chắn đến mức nào về kết quả của các dự báo đó. Một giá trị dự báo của biến phụ thuộc, $\hat{Y}_f$, được xác định bằng cách sử dụng hệ số chặn và hệ số góc ước lượng, cũng như biến độc lập kỳ vọng hoặc dự báo, $X_f$:

![](assets/Quantitative_method.pdf-0305-06.png)

<!-- Formula Text: ˆ Y  f  =   ˆ b  0 +  ˆ b  1 X f. (23) -->
$$\hat{Y}_f = \hat{b}_0 + \hat{b}_1 X_f \tag{23}$$

Trong mô hình hồi quy ROA của chúng ta, nếu chúng ta dự báo CAPEX của một công ty là 6%, thì ROA dự báo dựa trên phương trình ước lượng của chúng ta là 12,375%:

$$\hat{Y}_f = 4.875 + (1.25 \times 6) = 12.375$$

Tuy nhiên, chúng ta cần lưu ý rằng đường hồi quy ước lượng không mô tả hoàn hảo mối quan hệ giữa biến phụ thuộc và biến độc lập; nó chỉ là mức trung bình của mối quan hệ giữa hai biến số. Điều này thể hiện rõ bởi vì không phải tất cả các phần dư đều bằng 0.

Do đó, cần có một ước lượng khoảng (*interval estimate*) của dự báo để phản ánh sự không chắc chắn này. Phương sai ước lượng của sai số dự báo (*prediction error*), $s_f^2$, của $Y$ khi biết $X$ là:

![](assets/Quantitative_method.pdf-0305-11.png)

<!-- Formula Text: s f 2  =  s e 2[1 +  1 _ n  + (X f − _ X ) 2 _ (n − 1) s X 2  ]  =  s e 2 [ 1 +  1 _ n  + (X f − _ X ) 2 ___________ ∑ i=1 n (X i − _ X ) 2 ] , and the standard error of the forecast is s f  =  s e √ ___________________ 1 +  1 _ n  + (X f − _ X ) 2 ___________ ∑ i=1 n (X i − _ X ) 2 . (24) -->
$$s_f^2 = s_e^2 \left[ 1 + \frac{1}{n} + \frac{(X_f - \bar{X})^2}{(n - 1) s_X^2} \right] = s_e^2 \left[ 1 + \frac{1}{n} + \frac{(X_f - \bar{X})^2}{\sum_{i=1}^{n} (X_i - \bar{X})^2} \right]$$

và **sai số chuẩn của dự báo (*standard error of the forecast*)** là:

$$s_f = s_e \sqrt{1 + \frac{1}{n} + \frac{(X_f - \bar{X})^2}{\sum_{i=1}^{n} (X_i - \bar{X})^2}} \tag{24}$$

Sai số chuẩn của dự báo phụ thuộc vào các yếu tố sau:

- sai số chuẩn của ước lượng, $s_e$;

- số lượng quan sát, $n$;

- giá trị dự báo của biến độc lập, $X_f$, được sử dụng để dự báo biến phụ thuộc và độ lệch của nó so với giá trị trung bình ước lượng, $\bar{X}$; và

- sự biến thiên của biến độc lập.

Chúng ta có thể thấy những điều sau đây từ phương trình tính sai số chuẩn của dự báo:

**1.** Mô hình hồi quy có độ phù hợp càng tốt thì sai số chuẩn của ước lượng ($s_e$) càng nhỏ và do đó, sai số chuẩn của dự báo ($s_f$) càng nhỏ.

**2.** Cỡ mẫu ($n$) trong ước lượng hồi quy càng lớn thì sai số chuẩn của dự báo càng nhỏ.

**3.** Biến độc lập dự báo ($X_f$) càng gần với giá trị trung bình của biến độc lập ($\bar{X}$) được sử dụng trong ước lượng hồi quy thì sai số chuẩn của dự báo càng nhỏ.

<!-- PDF Page 306 -->

Một khi chúng ta có ước lượng này về sai số chuẩn của dự báo, việc xác định một khoảng dự báo (*prediction interval*) xung quanh giá trị dự báo của biến phụ thuộc ($\hat{Y}_f$) rất giống với việc ước lượng một khoảng tin cậy (*confidence interval*) xung quanh một tham số ước lượng. Khoảng dự báo là:

$$\hat{Y}_f \pm t_{\text{critical for }\alpha/2} s_f$$

Chúng ta phác thảo các bước để xây dựng khoảng dự báo trong Hình 34.

#### **Hình 34: Tạo Khoảng Dự báo xung quanh Biến phụ thuộc Dự báo**

![](assets/Quantitative_method.pdf-0306-08.png)

<!-- Picture Text: Predict the value of  Y ,  Y^f , given the forecasted value of  X ,  Xf<br>Choose a significance level, α, for the prediction interval<br>Determine the critical value for the prediction interval based on the degrees of<br>freedom and the significance level<br>Compute the standard error of the forecast<br>Compute the (1 – α) percent prediction interval for the prediction as:  Y^f  ± t critical for α/2  sf<br> -->
> **Chú thích hình ảnh (Quy trình 5 bước):**
> 1. Dự báo giá trị của $Y$, tức $\hat{Y}_f$, khi biết giá trị dự báo của $X$, tức $X_f$.
> 2. Chọn một mức ý nghĩa, $\alpha$, cho khoảng dự báo.
> 3. Xác định giá trị tới hạn cho khoảng dự báo dựa trên bậc tự do và mức ý nghĩa.
> 4. Tính sai số chuẩn của dự báo ($s_f$).
> 5. Tính khoảng dự báo $(1 - \alpha)\%$ cho giá trị dự báo theo công thức: $\hat{Y}_f \pm t_{\text{critical for }\alpha/2} s_f$.

Đối với mô hình hồi quy ROA của chúng ta, biết rằng giá trị dự báo của CAPEX là $6.0$, giá trị dự báo của $Y$ là $12.375$:

$$\hat{Y}_f = 4.875 + 1.25 X_f = 4.875 + (1.25 \times 6.0) = 12.375$$

Giả sử mức ý nghĩa 5% ($\alpha$), kiểm định hai phía, với $n - 2$ bậc tự do (tức $\text{df} = 4$), các giá trị tới hạn cho khoảng dự báo là $\pm 2.776$. Sai số chuẩn của dự báo là:

![](assets/Quantitative_method.pdf-0306-12.png)

<!-- Formula Text: s f  =  3.459588 √ ______________ 1 +  1 _ 6  +  (6 − 6.1) 2 _ 122.640    =  3.459588 √ _ 1.166748   =  3.736912. -->
$$s_f = 3.459588 \sqrt{1 + \frac{1}{6} + \frac{(6 - 6.1)^2}{122.640}} = 3.459588 \sqrt{1.166748} = 3.736912$$

Khi đó, khoảng dự báo 95% trở thành:

![](assets/Quantitative_method.pdf-0306-14.png)

<!-- Formula Text: 12.375 ± 2.776 (3.736912) -->
$$12.375 \pm 2.776 (3.736912)$$

$$12.375 \pm 10.3737$$

![](assets/Quantitative_method.pdf-0306-16.png)

<!-- Formula Text: {2.0013  <   ˆ Y  f  <  22.7487} -->
$$\{2.0013 < \hat{Y}_f < 22.7487\}$$

Đối với ví dụ hồi quy ROA của chúng ta, chúng ta có thể thấy sai số chuẩn của dự báo ($s_f$) thay đổi như thế nào khi giá trị dự báo của biến độc lập rời xa dần giá trị trung bình của biến độc lập $(X_f - \bar{X})$ trong Hình 35. Giá trị trung bình của CAPEX là 6,1%, và dải băng biểu thị một sai số chuẩn của dự báo, nằm phía trên và phía dưới mức dự báo, đạt mức tối thiểu tại điểm đó và mở rộng dần khi biến độc lập rời xa $\bar{X}$.

<!-- PDF Page 307 -->

#### **Hình 35: Dự báo ROA và Sai số chuẩn của Dự báo**

![](assets/Quantitative_method.pdf-0307-03.png)

<!-- Picture Text: Forecasted ROA (%)<br>45<br>40<br>35<br>30<br>25<br>20<br>15<br>10<br>5<br>0<br>–5<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20<br>Forecasted CAPEX (%)<br>Forecasted  Y<br>Upper Bound of 95% Prediction Interval<br>Lower Bound of 95% Prediction Interval<br>One Standard Error of the Forecast above the Forecast<br>One Standard Error of the Forecast below the Forecast<br> -->
> **Chú thích hình ảnh:** Trục tung: ROA dự báo (%). Trục hoành: CAPEX dự báo (%). Hiển thị đường Dự báo $Y$ (*Forecasted $Y$*), Cận trên và Cận dưới của Khoảng dự báo 95% (*Upper/Lower Bound of 95% Prediction Interval*), cùng với các đường cộng/trừ 1 Sai số chuẩn của dự báo (*One Standard Error of the Forecast above/below the Forecast*). Các đường giới hạn loe rộng ra khi $X_f$ rời xa mức trung bình $6.1\%$.

#### **BỘ CÂU HỎI (*QUESTION SET*)**

Giả sử bạn chạy một hồi quy dữ liệu chéo cho 100 công ty, trong đó biến phụ thuộc là tỷ suất sinh lợi cổ phiếu hàng năm và biến độc lập là tỷ lệ phần trăm sở hữu của tổ chức có độ trễ (*lagged percentage of institutional ownership* – INST). Kết quả của ước lượng hồi quy tuyến tính đơn này được trình bày trong Bảng 36. Hãy đánh giá mô hình bằng cách trả lời các câu hỏi 1–4.

#### **Bảng 36: Bảng ANOVA cho Tỷ suất sinh lợi Cổ phiếu Hàng năm được Hồi quy theo Tỷ lệ Sở hữu của Tổ chức**

|**Nguồn biến thiên (*Source*)**|**Tổng bình phương (*Sum of Squares*)**|**Bậc tự do (*Degrees of Freedom*)**|**Trung bình bình phương (*Mean Square*)**|
|---|---|---|---|
|Hồi quy (*Regression*)|576.1485|1|576.1485|
|Sai số (*Error*)|1,873.5615|98|19.1180|
|Tổng (*Total*)|2,449.7100|||

1. Hệ số xác định (*coefficient of determination*) của mô hình hồi quy này là bao nhiêu?

#### **Lời giải:**

Hệ số xác định bằng tổng bình phương hồi quy chia cho tổng bình phương toàn phần: $576.1485 \div 2,449.71 = 0.2352$, hay 23,52%.

<!-- PDF Page 308 -->

2. Sai số chuẩn của ước lượng (*standard error of the estimate*) của mô hình hồi quy này là bao nhiêu?

#### **Lời giải:**

Sai số chuẩn của ước lượng là căn bậc hai của trung bình bình phương sai số (MSE): $\sqrt{19.1180} = 4.3724$.

3. Tại mức ý nghĩa 5%, chúng ta có bác bỏ giả thuyết không cho rằng hệ số góc bằng 0 hay không nếu giá trị $F$ tới hạn là $3.938$?

#### **Lời giải:**

Sử dụng quy trình sáu bước để kiểm định giả thuyết, chúng ta có:

|**Bước 1**|Phát biểu các giả thuyết.|$H_0: b_1 = 0$ đối lập với $H_a: b_1 \neq 0$|
|---|---|---|
|**Bước 2**|Xác định thống kê kiểm định phù hợp.|$F = \frac{\text{MSR}}{\text{MSE}}$ với 1 và 98 bậc tự do.|
|**Bước 3**|Xác định mức ý nghĩa.|$\alpha = 5\%$ (một phía, bên phải).|
|**Bước 4**|Phát biểu quy tắc quyết định.|Giá trị $F$ tới hạn $= 3.938$.<br>Bác bỏ giả thuyết không nếu thống kê $F$ tính được lớn hơn $3.938$.|
|**Bước 5**|Tính toán thống kê kiểm định.|$F = \frac{576.1485}{19.1180} = 30.1364$|
|**Bước 6**|Đưa ra quyết định.|Bác bỏ giả thuyết không bởi vì thống kê $F$ tính được lớn hơn giá trị $F$ tới hạn. Có đủ bằng chứng cho thấy hệ số góc khác $0.0$.|

4. Dựa trên câu trả lời của bạn cho các câu hỏi trước, hãy đánh giá mô hình hồi quy tuyến tính đơn này.

#### **Lời giải:**

Hệ số xác định chỉ ra rằng sự biến thiên của biến độc lập giải thích được 23,52% sự biến thiên của biến phụ thuộc. Ngoài ra, kiểm định thống kê $F$ xác nhận rằng hệ số góc của mô hình khác 0 tại mức ý nghĩa 5%. Tóm lại, mô hình dường như khớp với dữ liệu khá tốt.

### **Thông tin sau đây áp dụng cho các câu hỏi 5–10**

Giả sử chúng ta muốn dự báo biên lợi nhuận ròng (NPM) của một công ty dựa trên chi tiêu nghiên cứu và phát triển được chuẩn hóa theo doanh thu (RDR) của công ty đó, sử dụng mô hình đã ước lượng ở phần trước và các chi tiết được cung cấp trong Bảng 8. Mô hình hồi quy đã được ước lượng bằng dữ liệu của tám công ty như sau:

$$\hat{Y}_f = 16.5 - 1.3 X_f$$

với sai số chuẩn của ước lượng ($s_e$) là $1.8618987$ và phương sai của RDR, $\frac{\sum_{i=1}^{n} (X_i - \bar{X})^2}{n - 1}$, là $4.285714$ như đã cho.

5. Giá trị dự báo của NPM là bao nhiêu nếu giá trị dự báo của RDR là 5?

#### **Lời giải:**

Giá trị dự báo của NPM là 10: $16.5 - (1.3 \times 5) = 10$.

<!-- PDF Page 309 -->

6. Sai số chuẩn của dự báo ($s_f$) là bao nhiêu nếu giá trị dự báo của RDR là 5?

#### **Lời giải:**

Để suy ra sai số chuẩn của dự báo ($s_f$), trước tiên chúng ta phải tính sự biến thiên của RDR. Sau đó, chúng ta có tất cả các mảnh ghép để tính $s_f$:

$$\sum_{i=1}^{n} (X_i - \bar{X})^2 = 4.285714 \times 7 = 30$$

$$s_f = 1.8618987 \sqrt{1 + \frac{1}{8} + \frac{(5 - 7.5)^2}{30}} = 2.1499$$

7. Khoảng dự báo 95% cho giá trị dự báo của NPM sử dụng các giá trị $t$ tới hạn ($\text{df} = 6$) bằng $\pm 2.447$ là bao nhiêu?

#### **Lời giải:**

Khoảng dự báo 95% cho giá trị dự báo của NPM là $\{10 \pm 2.447(2.1499)\}$, hay $\{4.7392 < \hat{Y}_f < 15.2608\}$.

8. Giá trị dự báo của NPM là bao nhiêu nếu giá trị dự báo của RDR là 15?

#### **Lời giải:**

Giá trị dự báo của NPM là $-3$: $16.5 - (1.3 \times 15) = -3$.

9. Tham chiếu Bảng 9, sai số chuẩn của dự báo là bao nhiêu nếu giá trị dự báo của RDR là 15?

#### **Lời giải:**

Để suy ra sai số chuẩn của dự báo, trước tiên chúng ta phải tính sự biến thiên của RDR. Sau đó, chúng ta có thể tính $s_f$:

$$\sum_{i=1}^{n} (X_i - \bar{X})^2 = 4.285714 \times 7 = 30$$

$$s_f = 1.8618987 \sqrt{1 + \frac{1}{8} + \frac{(15 - 7.5)^2}{30}} = 3.2249$$

10. Khoảng dự báo 95% cho giá trị dự báo của NPM sử dụng các giá trị $t$ tới hạn ($\text{df} = 6$) bằng $\pm 2.447$ là bao nhiêu?

#### **Lời giải:**

Khoảng dự báo 95% cho giá trị dự báo của NPM là $\{-3 \pm 2.447(3.2249)\}$, hay $\{-10.8913 < \hat{Y}_f < 4.8913\}$.

### **Thông tin sau đây áp dụng cho các câu hỏi 11–15**

Bạn đang kiểm tra kết quả của một ước lượng hồi quy nhằm cố gắng giải thích tốc độ tăng trưởng doanh số theo đơn vị sản phẩm (*unit sales growth*) của một doanh nghiệp mà bạn đang nghiên cứu. Kết quả đầu ra phân tích phương sai (ANOVA) cho hồi quy được cho trong Bảng 37. Hồi quy được dựa trên năm quan sát ($n = 5$).

<!-- PDF Page 310 -->

#### **Bảng 37: Kết quả Đầu ra ANOVA (*ANOVA Output*)**

![](assets/Quantitative_method.pdf-0310-05.png)

<!-- Picture Text: Sum of  Mean<br>Source df Squares Square F p -Value<br>Regression 1 88.0 88.0 36.667 0.00904<br>Residual 3 7.2 2.4<br>Total 4 95.2<br> -->

|**Nguồn (*Source*)**|**Bậc tự do (*df*)**|**Tổng bình phương (*Sum of Squares*)**|**Trung bình bình phương (*Mean Square*)**|**$F$**|**Trị số $p$ (*$p$-Value*)**|
|---|---|---|---|---|---|
|Hồi quy (*Regression*)|1|88.0|88.0|36.667|0.00904|
|Phần dư (*Residual*)|3|7.2|2.4|||
|Tổng (*Total*)|4|95.2||||

11. Tính phương sai mẫu (*sample variance*) của biến phụ thuộc bằng cách sử dụng thông tin trong bảng.

#### **Lời giải:**

Phương sai mẫu của biến phụ thuộc là tổng bình phương toàn phần chia cho bậc tự do của nó ($n - 1 = 5 - 1 = 4$, như đã cho). Do đó, phương sai mẫu của biến phụ thuộc là $95.2 \div 4 = 23.8$.

12. Tính hệ số xác định (*coefficient of determination*) cho mô hình ước lượng này.

#### **Lời giải:**

Hệ số xác định $= 88.0 \div 95.2 = 0.92437$.

13. Thống kê $F$ kiểm định giả thuyết nào?

#### **Lời giải:**

Thống kê $F$ kiểm định xem liệu tất cả các hệ số góc trong một hồi quy tuyến tính có bằng 0 hay không.

14. Kiểm định $F$ có ý nghĩa thống kê tại mức ý nghĩa $0.05$ hay không?

#### **Lời giải:**

Giá trị tính được của thống kê $F$ là $36.667$, như trình bày trong Bảng 37. Trị số $p$ tương ứng ($0.00904$) nhỏ hơn $0.05$, vì vậy bạn bác bỏ giả thuyết không cho rằng hệ số góc bằng 0.

15. Tính sai số chuẩn của ước lượng (*standard error of the estimate*).

#### **Lời giải:**

Sai số chuẩn của ước lượng là căn bậc hai của trung bình bình phương sai số: $s_e = \sqrt{2.4} = 1.54919$.

# **<mark>6</mark>**

## **CÁC DẠNG HÀM CHO HỒI QUY TUYẾN TÍNH ĐƠN (*FUNCTIONAL FORMS FOR SIMPLE LINEAR REGRESSION*)**

- mô tả các dạng hàm (*functional forms*) khác nhau của hồi quy tuyến tính đơn

Không phải mọi tập hợp biến độc lập và biến phụ thuộc đều có mối quan hệ tuyến tính. Trên thực tế, chúng ta thường thấy các mối quan hệ phi tuyến tính trong dữ liệu kinh tế và tài chính. Hãy xem xét doanh thu của một công ty theo thời gian được minh họa trong Hình 38, với doanh thu là biến phụ thuộc

<!-- PDF Page 311 -->

($Y$) và thời gian là biến độc lập ($X$). Doanh thu tăng trưởng ở mức 15% mỗi năm trong một vài năm, nhưng sau đó tốc độ tăng trưởng cuối cùng giảm xuống chỉ còn 5% mỗi năm. Việc ước lượng mối quan hệ này dưới dạng một mô hình tuyến tính đơn sẽ ước lượng thấp hơn thực tế (*understate*) biến phụ thuộc (doanh thu) đối với một số khoảng của biến độc lập (thời gian), và sẽ ước lượng cao hơn thực tế (*overstate*) đối với các khoảng khác của biến độc lập.

**Hình 38: Doanh thu Công ty theo Thời gian**

![](assets/Quantitative_method.pdf-0311-04.png)

<!-- Picture Text: Revenues ( Y )<br>2,500<br>2,000<br>1,500<br>1,000<br>Y  = –287.61 + 76.578  X<br>500<br>R 2  = 0.9478<br>F –statistic = 508.9017<br>0<br>–500<br>1 4 7 10 13 16 19 22 25 28<br>Time ( X )<br>Observed  Y Linear Prediction of  Y<br> -->
> **Chú thích hình ảnh:** Trục tung: Doanh thu ($Y$). Trục hoành: Thời gian ($X$, từ 1 đến 30). Phương trình tuyến tính: $Y = -287.61 + 76.578X$, $R^2 = 0.9478$, $F\text{-statistic} = 508.9017$. Hiển thị Giá trị $Y$ quan sát (*Observed $Y$*) và Dự báo tuyến tính của $Y$ (*Linear Prediction of $Y$*).

Chúng ta vẫn có thể sử dụng mô hình hồi quy tuyến tính đơn, nhưng chúng ta cần điều chỉnh biến phụ thuộc hoặc biến độc lập để làm cho mô hình hoạt động tốt. Đây là trường hợp của nhiều dữ liệu tài chính hoặc kinh tế khác nhau mà bạn có thể sử dụng làm biến phụ thuộc và biến độc lập trong phân tích hồi quy của mình.

Một số dạng hàm (*functional forms*) khác nhau có thể được sử dụng để biến đổi dữ liệu nhằm cho phép sử dụng chúng trong hồi quy tuyến tính. Những phép biến đổi này bao gồm việc sử dụng logarit (tức là logarit tự nhiên – *natural logarithm*) của biến phụ thuộc, logarit của biến độc lập, nghịch đảo của biến độc lập, bình phương của biến độc lập, hoặc lấy sai phân (*differencing*) của biến độc lập. Chúng ta minh họa và thảo luận ba dạng hàm thường được sử dụng, mỗi dạng đều liên quan đến phép biến đổi logarit:

**1.** **Mô hình log-tuyến tính (*log-lin model*)**, trong đó biến phụ thuộc ở dạng logarit nhưng biến độc lập ở dạng tuyến tính;

**2.** **Mô hình tuyến tính-log (*lin-log model*)**, trong đó biến phụ thuộc ở dạng tuyến tính nhưng biến độc lập ở dạng logarit; và

**3.** **Mô hình log-log (*log-log model*)**, trong đó cả biến phụ thuộc và biến độc lập đều ở dạng logarit.

### **_Mô hình Log-Tuyến tính (*The Log-Lin Model*)_**

Trong mô hình log-tuyến tính (*log-lin model*), biến phụ thuộc ở dạng logarit và biến độc lập thì không, như sau:

$$\ln Y_i = b_0 + b_1 X_i \tag{25}$$

<!-- PDF Page 312 -->

Hệ số góc trong mô hình này là mức thay đổi tương đối (*relative change*) trong biến phụ thuộc ứng với một mức thay đổi tuyệt đối (*absolute change*) trong biến độc lập. Chúng ta có thể biến đổi biến $Y$ (doanh thu) trong Hình 38 thành logarit tự nhiên ($\ln$) của nó và sau đó khớp đường hồi quy, như trình bày trong Hình 39. Từ biểu đồ này, chúng ta thấy rằng mô hình log-lin là một mô hình khớp tốt hơn so với mô hình hồi quy tuyến tính đơn.

**Hình 39: Mô hình Log-Lin được Áp dụng cho Doanh thu Công ty theo Thời gian**

![](assets/Quantitative_method.pdf-0312-05.png)

<!-- Picture Text: Ln Revenues (Ln  Y )<br>9<br>8<br>7<br>6<br>5<br>4 Ln Y  = 4.7932 + 0.1087  X<br>R 2  = 0.9808<br>3 F –statistic = 1429.5473<br>2<br>1<br>0<br>1 4 7 10 13 16 19 22 25 28<br>Time ( X )<br>Ln  Y Log-Lin Prediction of  Y<br> -->
> **Chú thích hình ảnh:** Trục tung: $\ln$ Doanh thu ($\ln Y$). Trục hoành: Thời gian ($X$). Phương trình: $\ln Y = 4.7932 + 0.1087X$, $R^2 = 0.9808$, $F\text{-statistic} = 1429.5473$.

Điều quan trọng cần lưu ý là khi làm việc với mô hình log-lin, bạn phải cẩn thận khi đưa ra dự báo. Ví dụ, giả sử mô hình hồi quy ước lượng là $\ln Y = -7 + 2X$. Nếu $X$ là 2,5%, thì giá trị dự báo của $\ln Y$ là $-2$. Trong trường hợp này, giá trị dự báo của $Y$ là đối logarit (*antilog*) của $-2$, hay $e^{-2} = 0.135335$. Một lưu ý thận trọng khác là bạn không thể so sánh trực tiếp một mô hình log-lin với một mô hình lin-lin (tức là hồi quy của $Y$ theo $X$ mà không có bất kỳ phép biến đổi nào) bởi vì các biến phụ thuộc không ở cùng một dạng—chúng ta sẽ phải biến đổi $R^2$ và thống kê $F$ để có thể so sánh. Tuy nhiên, việc xem xét các phần dư lại rất hữu ích.

### **_Mô hình Tuyến tính-Log (*The Lin-Log Model*)_**

Mô hình tuyến tính-log (*lin-log model*) tương tự như mô hình log-lin, nhưng chỉ có biến độc lập ở dạng logarit:

$$Y_i = b_0 + b_1 \ln X_i$$

![](assets/Quantitative_method.pdf-0312-10.png)

<!-- Formula Text: (26) -->
$$Y_i = b_0 + b_1 \ln X_i \tag{26}$$

Hệ số góc trong mô hình hồi quy này cung cấp mức thay đổi tuyệt đối (*absolute change*) trong biến phụ thuộc ứng với một mức thay đổi tương đối (*relative change*) trong biến độc lập.

Giả sử một nhà phân tích đang kiểm tra mối quan hệ dữ liệu chéo giữa biên lợi nhuận hoạt động (*operating profit margin*), biến phụ thuộc ($Y$), và doanh số theo đơn vị sản phẩm (*unit sales*), biến độc lập ($X$), và thu thập dữ liệu trên một mẫu gồm 30 công ty. Biểu đồ phân tán và đường hồi quy cho các quan sát này được trình bày trong Hình 40. Mặc dù hệ số góc khác 0 tại mức ý nghĩa 5% (thống kê $t$ tính được của hệ số góc là $5.8616$, so với giá trị $t$ tới hạn là $\pm 2.048$), với $R^2$ là 55,10%, vấn đề đặt ra là liệu chúng ta có thể đạt được mức độ phù hợp tốt hơn bằng cách sử dụng một dạng hàm khác hay không.

<!-- PDF Page 313 -->

#### **Hình 40: Mối quan hệ giữa Biên lợi nhuận Hoạt động và Doanh số theo Đơn vị sản phẩm**

![](assets/Quantitative_method.pdf-0313-04.png)

<!-- Picture Text: Operating Profit Margin ( Y )<br>20<br>18<br>16<br>14<br>12<br>10<br>8 Y  = 10.3665 + 0.000045 X<br>6 R 2  = 0.5510<br>4 S e  = 2.2528<br>F –statistic = 33.8259<br>2<br>0<br>0 50,000 100,000 150,000<br>Unit Sales ( X )<br>Operating Profit Margin Regression Line<br> -->
> **Chú thích hình ảnh:** Trục tung: Biên lợi nhuận hoạt động ($Y$). Trục hoành: Doanh số theo đơn vị ($X$). Phương trình: $Y = 10.3665 + 0.000045X$, $R^2 = 0.5510$, $s_e = 2.2528$, $F\text{-statistic} = 33.8259$.

Nếu thay vào đó chúng ta sử dụng logarit tự nhiên của doanh số theo đơn vị sản phẩm làm biến độc lập trong mô hình của mình, chúng ta sẽ nhận được một bức tranh rất khác, như trình bày trong Hình 41. Hệ số $R^2$ cho mô hình biên lợi nhuận hoạt động được hồi quy theo logarit tự nhiên của doanh số theo đơn vị sản phẩm nhảy vọt lên 97,17%. Bởi vì biến phụ thuộc là như nhau trong cả mô hình gốc và mô hình đã biến đổi, chúng ta có thể so sánh sai số chuẩn của ước lượng: $2.2528$ với biến độc lập gốc và mức thấp hơn nhiều là $0.5659$ (văn bản ghi $0.5629$, hình ghi $0.5659$) với biến độc lập đã biến đổi. Rõ ràng biến giải thích được biến đổi logarit đã mang lại một mô hình có độ phù hợp tốt hơn.

**Hình 41: Mối quan hệ giữa Biên lợi nhuận Hoạt động và Logarit Tự nhiên của Doanh số theo Đơn vị sản phẩm**

![](assets/Quantitative_method.pdf-0313-07.png)

<!-- Picture Text: Operating Profit Margin ( Y )<br>20<br>18<br>16<br>14<br>12<br>10<br>8 Y  = 2.6286 + 1.1797 Ln X<br>6 R 2  = 0.9717<br>4 S e  = 0.5659<br>F –statistic = 960.1538<br>2<br>0<br>0 2 4 6 8 10 12 14<br>Ln of Unit Sales (Ln  X )<br>Operating Profit Margin Lin-Log Regression Line<br> -->
> **Chú thích hình ảnh:** Trục tung: Biên lợi nhuận hoạt động ($Y$). Trục hoành: $\ln$ của Doanh số theo đơn vị ($\ln X$). Phương trình: $Y = 2.6286 + 1.1797 \ln X$, $R^2 = 0.9717$, $s_e = 0.5659$, $F\text{-statistic} = 960.1538$.

<!-- PDF Page 314 -->

### **_Mô hình Log-Log (*The Log-Log Model*)_**

Mô hình log-log (*log-log model*), trong đó cả biến phụ thuộc và biến độc lập đều tuyến tính dưới dạng logarit của chúng, còn được gọi là mô hình log kép (*double-log model*):

$$\ln Y_i = b_0 + b_1 \ln X_i \tag{27}$$

Mô hình này rất hữu ích trong việc tính toán độ co giãn (*elasticities*) bởi vì hệ số góc là mức thay đổi tương đối (*relative change*) trong biến phụ thuộc ứng với một mức thay đổi tương đối trong biến độc lập. Hãy xem xét một mô hình dữ liệu chéo của doanh thu công ty (biến $Y$) được hồi quy theo chi tiêu quảng cáo tính theo tỷ lệ phần trăm của chi phí bán hàng, chi phí chung và quản lý (SG&A), ký hiệu là $\text{ADVERT}$ (biến $X$). Như trình bày trong Hình 42, mô hình hồi quy tuyến tính đơn tạo ra một đường hồi quy khá thoải, với hệ số xác định chỉ đạt 20,89%.

**Hình 42: Khớp Mối quan hệ Tuyến tính giữa Doanh thu và Chi tiêu Quảng cáo**

![](assets/Quantitative_method.pdf-0314-07.png)

<!-- Picture Text: Revenues ( Y )<br>5,000<br>4,500<br>Y  = 70.7139 + 475.3665  X<br>4,000 R 2  = 0.2089<br>F –statistic = 7.3924<br>3,500<br>3,000<br>2,500<br>2,000<br>1,500<br>1,000<br>500<br>0<br>0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0<br>Advertising as a Percentage of SG&A  (%,  X )<br>Revenues Regression Line<br> -->
> **Chú thích hình ảnh:** Trục tung: Doanh thu ($Y$). Trục hoành: Quảng cáo tính theo tỷ lệ % của SG&A (%, $X$). Phương trình: $Y = 70.7139 + 475.3665X$, $R^2 = 0.2089$, $F\text{-statistic} = 7.3924$.

Nếu thay vào đó chúng ta sử dụng logarit tự nhiên của cả doanh thu và $\text{ADVERT}$, chúng ta sẽ có một bức tranh rất khác về mối quan hệ này. Như trình bày trong Hình 43, đường hồi quy ước lượng có hệ số góc dương có ý nghĩa thống kê; hệ số $R^2$ của mô hình log-log tăng hơn bốn lần, từ 20,89% lên 84,91%; và thống kê $F$ nhảy vọt từ $7.39$ lên $157.52$. Do đó, việc sử dụng phép biến đổi log-log cải thiện đáng kể mức độ phù hợp của mô hình hồi quy đối với dữ liệu của chúng ta.

<!-- PDF Page 315 -->

#### **Hình 43: Khớp Mô hình Log-Log của Doanh thu và Chi tiêu Quảng cáo**

![](assets/Quantitative_method.pdf-0315-03.png)

<!-- Picture Text: Ln Revenues (Ln  Y )<br>10<br>8<br>6<br>4<br>2<br>0<br>Ln Y  = 5.3109 + 1.3686 Ln X<br>–2 R 2  = 0.8491<br>F –statistic = 157.5208<br>–4<br>–6<br>–8 –6 –4 –2 0 2<br>Ln Advertising as a Percentage of SG&A  (Ln  X )<br>Natural Log of Revenues Log-Log Regression Line<br> -->
> **Chú thích hình ảnh:** Trục tung: $\ln$ Doanh thu ($\ln Y$). Trục hoành: $\ln$ Quảng cáo tính theo tỷ lệ % của SG&A ($\ln X$). Phương trình: $\ln Y = 5.3109 + 1.3686 \ln X$, $R^2 = 0.8491$, $F\text{-statistic} = 157.5208$.

### **_Lựa chọn Dạng hàm Đúng (*Selecting the Correct Functional Form*)_**

Chìa khóa để khớp dạng hàm phù hợp của một hồi quy tuyến tính đơn là xem xét các thước đo mức độ phù hợp (*goodness-of-fit measures*)—hệ số xác định ($R^2$), thống kê $F$, và sai số chuẩn của ước lượng ($s_e$)—cũng như kiểm tra xem liệu có các quy luật (*patterns*) trong phần dư hay không. Ngoài các thống kê về độ phù hợp, hầu hết các gói thống kê đều cung cấp đồ thị phần dư như một phần của kết quả đầu ra hồi quy, cho phép bạn kiểm tra trực quan các phần dư. Để nhắc lại một điểm quan trọng, điều bạn muốn thấy trong các đồ thị này là các phần dư mang tính ngẫu nhiên.

Để làm ví dụ, hãy xem xét mối quan hệ giữa tỷ suất sinh lợi hàng tháng của cổ phiếu DEF và tỷ suất sinh lợi hàng tháng của Chỉ số Cổ phiếu EAA, như được mô tả trong Phần A của Hình 44, kèm theo đường hồi quy. Sử dụng phương trình của đường hồi quy này, chúng ta tính toán phần dư và vẽ đồ thị của chúng theo Chỉ số Cổ phiếu EAA, như trình bày trong Phần B của Hình 44. Các phần dư có vẻ ngẫu nhiên, không mang mối liên hệ nào với biến độc lập. Phân phối của phần dư, được trình bày trong Phần C của Hình 44, cho thấy các phần dư xấp xỉ phân phối chuẩn. Sử dụng phần mềm thống kê, chúng ta có thể nghiên cứu sâu hơn bằng cách kiểm tra phân phối của phần dư, bao gồm việc sử dụng biểu đồ xác suất chuẩn (*normal probability plot*) hoặc các thống kê để kiểm định tính phân phối chuẩn của phần dư.

<!-- PDF Page 316 -->

#### **Hình 44: Tỷ suất sinh lợi Hàng tháng của Cổ phiếu DEF được Hồi quy theo Tỷ suất sinh lợi của Chỉ số EAA**

#### **_A. Biểu đồ phân tán của Tỷ suất sinh lợi Cổ phiếu DEF và Tỷ suất sinh lợi Chỉ số EAA_**
Tỷ suất sinh lợi Cổ phiếu DEF (%)

![](assets/Quantitative_method.pdf-0316-06.png)

<!-- Picture Text: 3.0<br>2.0 Y  = 0.0062 + 1.1905 X<br>1.0<br>0<br>–1.0<br>–2.0<br>–3.0<br>–4.0<br>–3.0 –2.0 –1.0 0 1.0 2.0<br>Return on the EAA Index (%)<br> -->
> **Chú thích hình ảnh (Phần A):** Trục tung: Tỷ suất sinh lợi cổ phiếu DEF (%). Trục hoành: Tỷ suất sinh lợi Chỉ số EAA (%). Phương trình đường hồi quy: $Y = 0.0062 + 1.1905X$.

#### **_B. Biểu đồ phân tán của Phần dư và Tỷ suất sinh lợi Chỉ số EAA_**

##### Phần dư Tỷ suất sinh lợi Cổ phiếu DEF (%)

![](assets/Quantitative_method.pdf-0316-09.png)

<!-- Picture Text: 0.3<br>0.2<br>0.1<br>0<br>–0.1<br>–0.2<br>–0.3<br>–0.4<br>–3.0 –2.0 –1.0 0 1.0 2.0 3.0<br>Return on the EAA Index (%)<br>C. Histogram of Residuals<br>Number of Observations<br>35<br>30<br>25<br>20<br>15<br>10<br>5<br>0<br>–0.28  –0.22 –0.16 –0.10 –0.04 0.02 0.08 0.14 0.20<br>to to to to to to to to to<br>–0.22 –0.16 –0.10 –0.04 0.02 0.08 0.14 0.20 0.26<br>Residual Range (%)<br> -->
> **Chú thích hình ảnh (Phần B & C):**
> - **B. Biểu đồ phân tán của phần dư:** Các điểm phần dư phân bố ngẫu nhiên quanh đường 0 trên toàn bộ dải giá trị của Tỷ suất sinh lợi Chỉ số EAA (%).
> - **C. Biểu đồ tần suất của phần dư (*Histogram of Residuals*):** Trục tung: Số lượng quan sát (*Number of Observations*). Trục hoành: Khoảng phần dư (*Residual Range*, %). Hình dáng quả chuông đối xứng cho thấy phần dư có phân phối xấp xỉ chuẩn.

#### **BỘ CÂU HỎI (*QUESTION SET*)**

Một nhà phân tích đang nghiên cứu mối quan hệ giữa tốc độ tăng trưởng chi tiêu tiêu dùng hàng năm ($\text{CONS}$) ở một quốc gia và tốc độ tăng trưởng GDP hàng năm của quốc gia đó ($\text{GGDP}$). Nhà phân tích ước lượng hai mô hình trong Bảng 45.

<!-- PDF Page 317 -->

#### **Bảng 45: Các Ước lượng Mô hình (*Model Estimates*)**

||**Mô hình 1 (*Model 1*)**|**Mô hình 2 (*Model 2*)**|
|---|---|---|
||$\text{GGDP}_i = b_0 + b_1 \text{CONS}_i + \varepsilon_i$|$\text{GGDP}_i = b_0 + b_1 \ln(\text{CONS}_i) + \varepsilon_i$|
|Hệ số chặn (*Intercept*)|1.040|1.006|
|Hệ số góc (*Slope*)|0.669|1.994|
|$R^2$|0.788|0.867|
|Sai số chuẩn của ước lượng (*Standard error of the estimate*)|0.404|0.320|
|Thống kê $F$ (*$F$-statistic*)|141.558|247.040|

1. Xác định dạng hàm (*functional form*) được sử dụng trong các mô hình này.

#### **Lời giải:**

Mô hình 1 là mô hình hồi quy tuyến tính đơn không có biến đổi biến số, trong khi Mô hình 2 là mô hình tuyến tính-log (*lin-log model*) với logarit tự nhiên của biến $\text{CONS}$ làm biến độc lập.

2. Giải thích mô hình nào có mức độ phù hợp (*goodness of fit*) tốt hơn với dữ liệu mẫu.

#### **Lời giải:**

Mô hình lin-log, tức Mô hình 2, khớp với dữ liệu tốt hơn. Bởi vì biến phụ thuộc là như nhau đối với cả hai mô hình, chúng ta có thể so sánh mức độ phù hợp của hai mô hình bằng cách sử dụng các thước đo tương đối ($R^2$ hoặc thống kê $F$) hoặc thước đo mức độ phù hợp tuyệt đối là sai số chuẩn của ước lượng ($s_e$). Sai số chuẩn của ước lượng thấp hơn đối với Mô hình 2 ($0.320 < 0.404$), trong khi $R^2$ và thống kê $F$ lại cao hơn đối với Mô hình 2 so với Mô hình 1.
