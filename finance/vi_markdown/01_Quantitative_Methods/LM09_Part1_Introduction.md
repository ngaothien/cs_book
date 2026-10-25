# Tập 1: Phương pháp Định lượng (*Quantitative Methods*)
## Học phần 9: Các Kiểm định Tính Độc lập Tham số và Phi tham số (*Parametric and Non-Parametric Tests of Independence*)
### Phần 1/2: Giới thiệu (*Introduction*) (Trang PDF 251–260)

---

<!-- PDF Page 251 -->

#### H Ọ C P H Ầ N 

# **<mark>9</mark>** 

### **Các Kiểm định Tính Độc lập Tham số và Phi tham số (*Parametric and Non-Parametric Tests of Independence*)** 

**tác giả: Pamela Peterson Drake, PhD, CFA.** 

_Pamela Peterson Drake, PhD, CFA, làm việc tại Đại học James Madison (Hoa Kỳ)._ 

###### **<mark>MỤC TIÊU HỌC TẬP (*LEARNING OUTCOMES*)</mark>** 

**_Mức độ Thành thạo – Ứng viên cần có khả năng:_**
- Giải thích các kiểm định tham số và phi tham số đối với giả thuyết rằng hệ số tương quan tổng thể (*population correlation coefficient*) bằng 0, và xác định xem giả thuyết có bị bác bỏ ở một mức ý nghĩa cho trước hay không.
- Giải thích các kiểm định tính độc lập dựa trên dữ liệu bảng tiếp liên (*contingency table data*).

##### **GIỚI THIỆU (*INTRODUCTION*)** 

**<mark>1</mark>** 

Trong nhiều bối cảnh đầu tư, chúng ta muốn đánh giá độ mạnh của mối quan hệ tuyến tính giữa hai biến số—tức là chúng ta muốn đánh giá **tương quan (*correlation*)** giữa chúng. Một kiểm định ý nghĩa của hệ số tương quan cho phép chúng ta đánh giá xem liệu mối quan hệ giữa hai biến ngẫu nhiên có phải là kết quả của sự ngẫu nhiên hay không. Bài 1 trình bày cách tiếp cận tham số và phi tham số để kiểm định tương quan giữa hai biến số. Nếu chúng ta kết luận rằng mối quan hệ không phải do ngẫu nhiên mà có, thì chúng ta có thể sử dụng thông tin này trong việc mô hình hóa hoặc dự báo bằng cách sử dụng các mô hình hồi quy (*regression models*) hoặc học máy (*machine learning*) được trình bày trong các Học phần sau. 

Tuy nhiên, khi đối mặt với dữ liệu phân loại (*categorical data*) hoặc dữ liệu rời rạc (*discrete data*), chúng ta không thể sử dụng các phương pháp được thảo luận trong bài học đầu tiên để kiểm định xem các phân loại của dữ liệu đó có độc lập với nhau hay không. Nếu chúng ta muốn kiểm định xem liệu có mối quan hệ nào giữa dữ liệu phân loại hoặc rời rạc hay không, chúng ta có thể thực hiện kiểm định tính độc lập (*test of independence*) bằng cách sử dụng một thống kê kiểm định phi tham số. Bài học thứ hai trình bày việc sử dụng các bảng tiếp liên (*contingency tables*) trong việc triển khai kiểm định phi tham số này. 

###### **TỔNG QUAN HỌC PHẦN (*LEARNING MODULE OVERVIEW*)** 

- Có ba cách để thiết lập các giả thuyết. Gọi $\theta$ biểu thị các tham số tổng thể: 


<!-- PDF Page 252 -->

   **1.** Giả thuyết đối hai phía (*Two-sided alternative*): $H_0: \theta = \theta_0$ đối lập với $H_a: \theta \ne \theta_0$ 
   **2.** Giả thuyết đối một phía (phía bên phải – *right side*): $H_0: \theta \le \theta_0$ đối lập với $H_a: \theta > \theta_0$ 
   **3.** Giả thuyết đối một phía (phía bên trái – *left side*): $H_0: \theta \ge \theta_0$ đối lập với $H_a: \theta < \theta_0$ 

   trong đó $\theta_0$ là một giá trị theo giả thuyết của tham số tổng thể và $\theta$ là giá trị thực của tham số tổng thể. 

- Kiểm định tham số (*parametric test*) là một kiểm định giả thuyết liên quan đến một tham số tổng thể hoặc một kiểm định giả thuyết dựa trên các giả định phân phối cụ thể. Ngược lại, kiểm định phi tham số (*nonparametric test*) hoặc không liên quan đến một tham số hoặc đưa ra các giả định tối thiểu về tổng thể mà từ đó mẫu được rút ra. 

- Kiểm định phi tham số chủ yếu được sử dụng khi dữ liệu không đáp ứng các giả định về phân phối, khi có các giá trị ngoại lai (*outliers*), khi dữ liệu được cho dưới dạng thứ hạng (*ranks*), hoặc khi giả thuyết chúng ta đang giải quyết không liên quan đến một tham số. 

- Trong các kiểm định liên quan đến tương quan, chúng ta sử dụng thống kê $t$ để kiểm định xem hệ số tương quan tổng thể có khác $0$ hay không. Nếu chúng ta có $n$ quan sát cho hai biến số, thống kê kiểm định này có phân phối $t$ với $n - 2$ bậc tự do. 

- Hệ số tương quan hạng Spearman (*Spearman rank correlation coefficient*) được tính toán trên thứ hạng của hai biến số trong các mẫu tương ứng của chúng. 

- Một thống kê kiểm định có phân phối Khi-bình phương (*chi-square distributed test statistic*) được sử dụng để kiểm định tính độc lập của hai biến phân loại. Kiểm định phi tham số này so sánh các tần số thực tế với các tần số kỳ vọng trên cơ sở tính độc lập. Thống kê kiểm định này có bậc tự do là $(r - 1)(c - 1)$ *(lưu ý: bản gốc tiếng Anh ở trang 252 in nhầm thành $(r - 1)(c - 2)$, công thức đúng chuẩn ở trang 262 là $(r - 1)(c - 1)$)*, trong đó $r$ là số danh mục của biến thứ nhất và $c$ là số danh mục của biến thứ hai. 

## **<mark>2</mark>** 

##### **CÁC KIỂM ĐỊNH LIÊN QUAN ĐẾN TƯƠNG QUAN (*TESTS CONCERNING CORRELATION*)** 

- *Giải thích các kiểm định tham số và phi tham số đối với giả thuyết rằng hệ số tương quan tổng thể bằng 0, và xác định xem giả thuyết có bị bác bỏ ở một mức ý nghĩa cho trước hay không*

Các giả thuyết phổ biến nhất liên quan đến tương quan xuất hiện khi so sánh hệ số tương quan tổng thể với $0$ bởi vì chúng ta thường đặt câu hỏi liệu một mối quan hệ có tồn tại hay không, điều này ngụ ý một giả thuyết không rằng hệ số tương quan bằng $0$ (tức là không có mối quan hệ). Các giả thuyết liên quan đến hệ số tương quan tổng thể có thể là hai phía hoặc một phía, như chúng ta đã thấy trong các kiểm định khác. Gọi $\rho$ đại diện cho hệ số tương quan tổng thể. Các giả thuyết có thể có như sau: 

- Hai phía (*Two sided*): $H_0: \rho = 0$ đối lập với $H_a: \rho \ne 0$ 
- Một phía (phía bên phải – *right side*): $H_0: \rho \le 0$ đối lập với $H_a: \rho > 0$ 
- Một phía (phía bên trái – *left side*): $H_0: \rho \ge 0$ đối lập với $H_a: \rho < 0$ 

Chúng ta sử dụng tương quan mẫu để kiểm định các giả thuyết này về tương quan tổng thể. 


<!-- PDF Page 253 -->

###### **Kiểm định Tham số về Tương quan (*Parametric Test of a Correlation*)** 

Hệ số tương quan từng cặp tham số thường được gọi là **tương quan Pearson (*Pearson correlation*)**, **tương quan hai biến (*bivariate correlation*)**, hoặc đơn giản là tương quan. Trọng tâm của chúng ta là việc kiểm định tương quan chứ không phải phép tính thực tế của thống kê này, nhưng việc nhìn vào công thức tính tương quan mẫu sẽ giúp phân biệt tương quan này với tương quan phi tham số. Xét hai biến số, $X$ và $Y$. Tương quan mẫu, $r_{XY}$, được tính như sau: 

![](assets/Quantitative_method.pdf-0253-04.png)

<!-- Formula Text: r XY  = s XY _ s X s Y , (1) -->
$$r_{XY} = \frac{s_{XY}}{s_X s_Y} \tag{1}$$

trong đó $s_{XY}$ là hiệp phương sai mẫu (*sample covariance*) giữa hai biến $X$ và $Y$, $s_X$ là độ lệch chuẩn của biến $X$, và $s_Y$ là độ lệch chuẩn của biến $Y$. Chúng ta thường lược bỏ chỉ số dưới để biểu thị tương quan đơn giản là $r$. 

Do đó, bạn có thể thấy từ công thức này rằng mỗi quan sát được so sánh với giá trị trung bình của biến tương ứng và, do có hiệp phương sai, mức độ chênh lệch của mỗi quan sát so với giá trị trung bình của biến tương ứng đóng vai trò rất quan trọng. Lưu ý rằng hiệp phương sai quyết định dấu của hệ số tương quan. 

Nếu hai biến số có phân phối chuẩn, chúng ta có thể kiểm định để xác định xem giả thuyết không ($H_0: \rho = 0$) có nên bị bác bỏ hay không bằng cách sử dụng tương quan mẫu, $r$. Công thức cho kiểm định $t$ như sau: 

![](assets/Quantitative_method.pdf-0253-08.png)

<!-- Formula Text: t  =   r √ _ n − 2 _ √ _ 1 − r 2  . (2) -->
$$t = \frac{r\sqrt{n - 2}}{\sqrt{1 - r^2}} \tag{2}$$

Thống kê kiểm định này có phân phối $t$ với $n - 2$ bậc tự do. Một nhận xét thực tế liên quan đến Phương trình 2 là độ lớn của $r$ cần thiết để bác bỏ giả thuyết không sẽ giảm xuống khi kích thước mẫu $n$ tăng lên, vì hai lý do. Thứ nhất, khi $n$ tăng lên, số bậc tự do tăng lên và giá trị tuyệt đối của giá trị tới hạn của thống kê $t$ giảm xuống. Thứ hai, giá trị tuyệt đối của tử số tăng lên khi $n$ lớn hơn, dẫn đến độ lớn của thống kê $t$ tính toán được lớn hơn. Ví dụ, với kích thước mẫu $n = 12$, $r = 0.35$ mang lại thống kê $t$ là $1.182$, không khác $0$ ở mức ý nghĩa $0.05$ ($t_{\alpha/2} = \pm 2.228$). Với kích thước mẫu $n = 32$, cùng mức tương quan mẫu đó, $r = 0.35$, mang lại thống kê $t$ là $2.046$, vừa đủ có ý nghĩa thống kê ở mức $0.05$ ($t_{\alpha/2} = \pm 2.042$). 

Một cách khác để diễn đạt điểm này là khi lấy mẫu từ cùng một tổng thể, một giả thuyết không đang sai có nhiều khả năng bị bác bỏ hơn (tức là lực kiểm định tăng lên) khi chúng ta tăng kích thước mẫu, với các yếu tố khác không đổi, bởi vì số lượng quan sát cao hơn làm tăng tử số của thống kê kiểm định. Chúng tôi thể hiện điều này trong Minh họa 1 cho ba hệ số tương quan mẫu khác nhau, với các thống kê $t$ tính toán được tương ứng và ý nghĩa thống kê ở mức $5\%$ cho một giả thuyết đối hai phía. Khi kích thước mẫu tăng lên, ý nghĩa thống kê có nhiều khả năng đạt được hơn, nhưng tốc độ đạt được ý nghĩa thống kê này phụ thuộc vào hệ số tương quan mẫu; tương quan mẫu càng cao thì càng nhanh đạt được ý nghĩa thống kê khi tăng kích thước mẫu. Khi kích thước mẫu tăng lên do các tập dữ liệu ngày càng lớn được xem xét, giả thuyết không hầu như luôn bị bác bỏ và cần phải áp dụng các công cụ phân tích dữ liệu khác. 


<!-- PDF Page 254 -->

**Minh họa 1: Các Thống kê Kiểm định Tính toán được cho các Kích thước Mẫu và Tương quan Mẫu Khác nhau với Mức Ý nghĩa 5% (*Exhibit 1: Calculated Test Statistics for Different Sample Sizes and Sample Correlations with a 5 Percent Level of Significance*)** 

![](assets/Quantitative_method.pdf-0254-04.png)

<!-- Picture Text: Calculated  t -Statistic<br>8<br>7<br>6<br>5<br>4<br>3<br>2<br>1<br>0<br>3 12 21 30 39 48 57 66 75 84 93<br>Sample Size<br>t -Statistic for Correlation = 0.2 Significant Correlation = 0.2<br>t -Statistic for Correlation = 0.4 Significant Correlation = 0.4<br>t -Statistic for Correlation = 0.6 Significant Correlation = 0.6<br> -->
> **Chú thích hình ảnh:** Đồ thị biểu diễn Thống kê $t$ tính toán được (*Calculated t-Statistic*) trên trục tung theo Kích thước mẫu (*Sample Size*) trên trục hoành cho các mức hệ số tương quan $r = 0.2, 0.4, 0.6$, đánh dấu vùng bắt đầu có ý nghĩa thống kê (*Significant Correlation*).

###### **VÍ DỤ 1 (*EXAMPLE 1*)** 

###### **Xem xét Mối quan hệ giữa Tỷ suất sinh lợi trên Khoản đầu tư Một và Khoản đầu tư Hai (*Examining the Relationship between Returns on Investment One and Investment Two*)** 

Một nhà phân tích đang xem xét tỷ suất sinh lợi hàng năm của Khoản đầu tư Một và Khoản đầu tư Hai trong 33 năm, như được hiển thị trong Minh họa 2. 

**Minh họa 2: Tỷ suất sinh lợi của Khoản đầu tư Một và Hai trong 33 Năm (*Exhibit 2: Returns for Investments One and Two over 33 Years*)** 

![](assets/Quantitative_method.pdf-0254-09.png)

<!-- Picture Text: Annual Return (%)<br>12<br>10<br>8<br>6<br>4<br>2<br>0<br>–2<br>1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33<br>Year<br>Investment One Investment Two<br> -->
> **Chú thích hình ảnh:** Đồ thị chuỗi thời gian của Tỷ suất sinh lợi hàng năm (*Annual Return* (%)) từ Năm 1 đến Năm 33 của Khoản đầu tư Một (*Investment One*) và Khoản đầu tư Hai (*Investment Two*).

Mặc dù đồ thị chuỗi thời gian này cung cấp một số thông tin hữu ích, nhà phân tích quan tâm nhất đến việc định lượng mối liên hệ giữa tỷ suất sinh lợi của hai chuỗi này, vì vậy cô tính hệ số tương quan giữa hai chuỗi này và thu được kết quả bằng $0.43051$. 

1. Có mối tương quan dương có ý nghĩa thống kê giữa hai chuỗi tỷ suất sinh lợi này hay không nếu cô sử dụng mức ý nghĩa $1\%$?

**Lời giải (*Solution*):** 


<!-- PDF Page 255 -->

|**Bước 1 (*Step 1*)**|Phát biểu các giả thuyết.|$$H_0: \rho \le 0 \text{ đối lập với } H_a: \rho > 0$$|
|---|---|---|
|**Bước 2 (*Step 2*)**|Xác định thống kê kiểm định phù hợp.|$$t = \frac{r\sqrt{n - 2}}{\sqrt{1 - r^2}}$$|
|**Bước 3 (*Step 3*)**|Xác định mức ý nghĩa.|$1\%$|
|**Bước 4 (*Step 4*)**|Phát biểu quy tắc quyết định.|Với $33 - 2 = 31$ bậc tự do và kiểm định một phía với mức ý nghĩa $1\%$, giá trị tới hạn là $2.45282$.<br>Chúng ta bác bỏ giả thuyết không nếu thống kê $t$ tính toán được lớn hơn $2.45282$.|
|**Bước 5 (*Step 5*)**|Tính toán thống kê kiểm định.|$$t = \frac{0.43051\sqrt{33 - 2}}{\sqrt{1 - 0.18534}} = 2.65568$$|
|**Bước 6 (*Step 6*)**|Đưa ra quyết định.|Bác bỏ giả thuyết không bởi vì thống kê $t$ tính toán được lớn hơn $2.45282$. Có đủ bằng chứng để bác bỏ $H_0$ nhằm ủng hộ $H_a$, tức là tương quan giữa tỷ suất sinh lợi hàng năm của hai khoản đầu tư này là dương.|

###### **VÍ DỤ 2 (*EXAMPLE 2*)** 

###### **Tương quan với Tỷ suất sinh lợi S&P 500 (*Correlation with the S&P 500 Returns*)** 

1. Minh họa 3 cho thấy tương quan mẫu giữa tỷ suất sinh lợi hàng tháng của bốn quỹ tương hỗ khác nhau và chỉ số S&P 500. Các hệ số tương quan dựa trên 36 quan sát hàng tháng. Các quỹ như sau: 

###### **Minh họa 3: Tương quan Mẫu giữa Tỷ suất sinh lợi Hàng tháng và S&P 500 (*Exhibit 3: Sample Correlations between Monthly Returns and the S&P 500*)** 

- **Quỹ 1 (*Fund 1*):** Quỹ vốn hóa lớn (*Large-cap fund*)
- **Quỹ 2 (*Fund 2*):** Quỹ vốn hóa trung bình (*Mid-cap fund*)
- **Quỹ 3 (*Fund 3*):** Quỹ giá trị vốn hóa lớn (*Large-cap value fund*)
- **Quỹ 4 (*Fund 4*):** Quỹ thị trường mới nổi (*Emerging market fund*)
- **S&P 500:** Chỉ số cổ phiếu nội địa Hoa Kỳ (*US domestic stock index*)


<!-- PDF Page 256 -->

||**Quỹ 1 (*Fund 1*)**|**Quỹ 2 (*Fund 2*)**|**Quỹ 3 (*Fund 3*)**|**Quỹ 4 (*Fund 4*)**|**S&P 500**|
|---|---|---|---|---|---|
|Quỹ 1 (*Fund 1*)|1|||||
|Quỹ 2 (*Fund 2*)|0.9231|1||||
|Quỹ 3 (*Fund 3*)|0.4771|0.4156|1|||
|Quỹ 4 (*Fund 4*)|0.7111|0.7238|0.3102|1||
|S&P 500|0.8277|0.8223|0.5791|0.7515|1|

Hãy kiểm định giả thuyết không rằng mỗi hệ số tương quan này, xét riêng lẻ, bằng $0$ đối lập với giả thuyết đối rằng nó khác $0$. Sử dụng mức ý nghĩa $5\%$ và các giá trị $t$ tới hạn là $\pm 2.032$. 

###### **Lời giải (*Solution*):** 

Các giả thuyết là $H_0: \rho = 0$ và $H_a: \rho \ne 0$. Các thống kê kiểm định tính toán được dựa trên công thức: 

![](assets/Quantitative_method.pdf-0256-06.png)

<!-- Formula Text: t  =   r √ _ n − 2 _ √ _ 1 − r 2  . -->
$$t = \frac{r\sqrt{n - 2}}{\sqrt{1 - r^2}}$$

![](assets/Quantitative_method.pdf-0256-07.png)

<!-- Formula Text: For example, the calculated t-statistic for the correlation of Fund 3 and Fund 4 is as follows t  =   r √ _ n − 2 _ √ _ 1 − r 2    =   0.3102 √ _ 36 − 2 ___________ √ _ 1 − 0.3102 2    =  1.903. -->
Ví dụ, thống kê $t$ tính toán được cho tương quan của Quỹ 3 và Quỹ 4 như sau:
$$t = \frac{r\sqrt{n - 2}}{\sqrt{1 - r^2}} = \frac{0.3102\sqrt{36 - 2}}{\sqrt{1 - 0.3102^2}} = 1.903$$

Lặp lại phép tính này cho toàn bộ ma trận tương quan mang lại kết quả sau: 

###### **Thống kê $t$ Tính toán được cho các Hệ số Tương quan (*Calculated t-Statistics for Correlations*)** 

||**Quỹ 1 (*Fund 1*)**|**Quỹ 2 (*Fund 2*)**|**Quỹ 3 (*Fund 3*)**|**Quỹ 4 (*Fund 4*)**|**S&P 500**|
|---|---|---|---|---|---|
|Quỹ 1 (*Fund 1*)||||||
|Quỹ 2 (*Fund 2*)|13.997|||||
|Quỹ 3 (*Fund 3*)|3.165|2.664||||
|Quỹ 4 (*Fund 4*)|5.897|6.116|1.903|||
|S&P 500|8.600|8.426|4.142|6.642||

Với các giá trị tới hạn là $\pm 2.032$, ngoại trừ tương quan giữa tỷ suất sinh lợi của Quỹ 3 và Quỹ 4, chúng ta bác bỏ giả thuyết không cho tất cả các hệ số tương quan này. Nói cách khác, có đủ bằng chứng để chỉ ra rằng các hệ số tương quan đều khác $0$, ngoại trừ tương quan tỷ suất sinh lợi giữa Quỹ 3 và Quỹ 4. 

Chúng ta có thể sử dụng phần mềm để xác định các giá trị tới hạn: 

###### **Excel** 

![](assets/Quantitative_method.pdf-0256-14.png)

<!-- Formula Text: [T.INV(0.025,34) and T.INV(0.975,34)] -->
`[T.INV(0.025,34) and T.INV(0.975,34)]`

**R** 

![](assets/Quantitative_method.pdf-0256-16.png)

<!-- Formula Text: [qt(c(.025,.975),34)] -->
`[qt(c(.025,.975),34)]`

###### **Python** 

`[from scipy.stats import t and t.ppf(.025,34) and t.ppf(.975,34)]` 

Chúng ta cũng có thể sử dụng phần mềm để xác định giá trị $p$ (*p-value*) cho thống kê kiểm định tính toán được nhằm so sánh với mức ý nghĩa. Ví dụ, đối với $t = 2.664$, giá trị $p$ là $0.01172$: 


<!-- PDF Page 257 -->

- **Excel:** `[(1-T.DIST(2.664,34,TRUE))*2]`
- **R:** `[(1-pt(2.664,34))*2]` 
- **Python:** `[from scipy.stats import t (1-t.cdf(2.664,34))*2]` 

###### **Kiểm định Phi tham số về Tương quan: Hệ số Tương quan Hạng Spearman (*Non-Parametric Test of Correlation: The Spearman Rank Correlation Coefficient*)** 

Khi chúng ta tin rằng tổng thể đang xem xét lệch đáng kể so với phân phối chuẩn, chúng ta có thể sử dụng một kiểm định dựa trên **hệ số tương quan hạng Spearman (*Spearman rank correlation coefficient*)**, $r_S$. Hệ số tương quan hạng Spearman về cơ bản tương đương với hệ số tương quan Pearson như đã định nghĩa trước đó, nhưng nó được tính toán trên _thứ hạng_ (*ranks*) của hai biến số (ví dụ: $X$ và $Y$) trong các mẫu tương ứng của chúng. Phép tính $r_S$ đòi hỏi các bước sau: 

**1.** Xếp hạng các quan sát của $X$ từ lớn nhất đến nhỏ nhất. Gán số 1 cho quan sát có giá trị lớn nhất, số 2 cho quan sát có giá trị lớn thứ hai, và cứ tiếp tục như vậy. Trong trường hợp có các giá trị bằng nhau (*ties*), hãy gán cho mỗi quan sát đồng hạng giá trị trung bình của các thứ hạng mà chúng cùng chiếm giữ. Ví dụ, nếu giá trị lớn thứ ba và thứ tư bằng nhau, chúng ta gán cho cả hai quan sát thứ hạng là $3.5$ (trung bình cộng của 3 và 4). Thực hiện thủ tục tương tự cho các quan sát của $Y$. 

**2.** Tính chênh lệch, $d_i$, giữa các thứ hạng cho mỗi cặp quan sát của $X$ và $Y$, và sau đó tính $d_i^2$ (bình phương chênh lệch thứ hạng). 

![](assets/Quantitative_method.pdf-0257-10.png)

<!-- Formula Text: 3.	 With n as the sample size, the Spearman rank correlation is given as follows: r s  =  1 − 6∑ i=1 n d i 2 _ n(n 2 − 1) . (3) -->
**3.** Với $n$ là kích thước mẫu, tương quan hạng Spearman được cho như sau:
$$r_S = 1 - \frac{6 \sum_{i=1}^{n} d_i^2}{n(n^2 - 1)} \tag{3}$$

Giả sử một nhà phân tích đang xem xét mối quan hệ giữa tỷ suất sinh lợi của hai quỹ đầu tư, A và B, có rủi ro tương tự nhau trong 35 năm. Cô lo ngại rằng các giả định cho tương quan tham số có thể không được đáp ứng, vì vậy cô quyết định kiểm định tương quan hạng Spearman. Các giả thuyết của cô là $H_0: r_S = 0$ và $H_a: r_S \ne 0$. Cô thu thập tỷ suất sinh lợi, xếp hạng tỷ suất sinh lợi cho mỗi quỹ, và tính chênh lệch thứ hạng cùng bình phương các chênh lệch. Một phần của bảng được cung cấp trong Minh họa 4. 

**Minh họa 4: Chênh lệch và Bình phương Chênh lệch Thứ hạng của Quỹ A và Quỹ B trong 35 Năm (*Exhibit 4: Differences and Squared Differences in Ranks for Fund A and Fund B over 35 Years*)** 

|**Năm (*Year*)**|**Quỹ A (*Fund A*)**|**Quỹ B (*Fund B*)**|**Thứ hạng của A (*Rank of A*)**|**Thứ hạng của B (*Rank of B*)**|**$d$**|**$d^2$**|
|---|---|---|---|---|---|---|
|1|2.453|1.382|27|31|−4|16|
|2|3.017|3.110|24|24|0|0|
|3|4.495|6.587|19|7|12|144|
|4|3.627|3.300|23|23|0|0|

$$\vdots$$


<!-- PDF Page 258 -->

|**Năm (*Year*)**|**Quỹ A (*Fund A*)**|**Quỹ B (*Fund B*)**|**Thứ hạng của A (*Rank of A*)**|**Thứ hạng của B (*Rank of B*)**|**$d$**|**$d^2$**|
|---|---|---|---|---|---|---|
|30|2.269|0.025|28|35|−7|49|
|31|6.354|4.428|10|19|−9|81|
|32|6.793|4.165|8|20|−12|144|
|33|7.300|7.623|5|5|0|0|
|34|6.266|4.527|11|18|−7|49|
|35|1.257|4.704|34|16|18|324|
||||||Tổng (*Sum*) =|2,202|

Tương quan hạng Spearman được tính như sau: 

![](assets/Quantitative_method.pdf-0258-05.png)

<!-- Formula Text: r s  =  1 − 6∑ i=1 n d i 2 _ n(n 2 − 1)   =  1 − 6(2, 202) _ 35(1, 225 − 1)   =  0.6916. -->
$$r_S = 1 - \frac{6 \sum_{i=1}^{n} d_i^2}{n(n^2 - 1)} = 1 - \frac{6(2,202)}{35(1,225 - 1)} = 0.6916$$

Kiểm định giả thuyết cho tương quan hạng Spearman phụ thuộc vào việc mẫu là nhỏ hay lớn ($n > 30$). Đối với các mẫu nhỏ, nhà nghiên cứu cần một bảng giá trị tới hạn chuyên biệt, nhưng đối với các mẫu lớn, chúng ta có thể tiến hành kiểm định $t$ bằng cách sử dụng thống kê kiểm định trong Phương trình 2, có phân phối $t$ với $n - 2$ bậc tự do. 

Trong ví dụ này, đối với kiểm định hai phía với mức ý nghĩa $5\%$, các giá trị tới hạn cho $n - 2 = 35 - 2 = 33$ bậc tự do là $\pm 2.0345$. Với thông tin mẫu trong Minh họa 4, thống kê kiểm định tính toán được như sau: 

![](assets/Quantitative_method.pdf-0258-08.png)

<!-- Formula Text: t  =    0.6916 √ _ 33 ___________ √ ____________ 1 − (0.6916 2)    =  5.5005 -->
$$t = \frac{0.6916\sqrt{33}}{\sqrt{1 - (0.6916^2)}} = 5.5005$$

Theo đó, chúng ta bác bỏ giả thuyết không ($H_0: r_S = 0$), kết luận rằng có đủ bằng chứng để chỉ ra rằng tương quan giữa tỷ suất sinh lợi của Quỹ A và Quỹ B là khác $0$. 

###### **VÍ DỤ 3 (*EXAMPLE 3*)** 

###### **Kiểm định Tương quan Tỷ giá Hối đoái (*Testing the Exchange Rate Correlation*)** 

Một nhà phân tích thu thập dữ liệu tỷ giá hối đoái của năm đồng tiền so với đồng đô la Mỹ. Khi kiểm tra phân phối của các tỷ giá hối đoái này, cô quan sát thấy có sự lệch khỏi phân phối chuẩn, đặc biệt là độ lệch âm (*negative skewness*) đối với bốn chuỗi và độ lệch dương (*positive skewness*) đối với chuỗi thứ năm. Do đó, cô quyết định xem xét mối quan hệ giữa các đồng tiền này bằng cách sử dụng tương quan hạng Spearman. Cô tính toán các hệ số tương quan này giữa các đồng tiền trong 180 ngày, được hiển thị trong biểu đồ tương quan (*correlogram*) ở Minh họa 5. Trong biểu đồ tương quan này, tam giác dưới báo cáo các hệ số tương quan từng cặp và tam giác trên cung cấp hình ảnh trực quan về độ lớn của các hệ số tương quan, với các hình tròn lớn hơn biểu thị giá trị tuyệt đối lớn hơn của các hệ số tương quan và các hình tròn đậm hơn biểu thị các hệ số tương quan âm. 


<!-- PDF Page 259 -->

###### **Minh họa 5: Tương quan Hạng Spearman giữa các Tỷ giá Hối đoái so với Đô la Mỹ (*Exhibit 5: Spearman Rank Correlations between Exchanges Rates Relative to the US Dollar*)** 

![](assets/Quantitative_method.pdf-0259-03.png)

<!-- Picture Text: 1.0<br>AUD 0.8<br>0.6<br>0.9124 CAD 0.4<br>0.2<br>0.6079 0.5654 EUR 0<br>–0.2<br>0.6816 0.7047 0.4889 GBP –0.4<br>–0.6<br>–0.1973 –0.2654 0.3691 –0.2046 JPY –0.8<br>–1.0<br> -->
> **Chú thích hình ảnh:** Biểu đồ ma trận tương quan (*correlogram*) giữa 5 đồng tiền (AUD, CAD, EUR, GBP, JPY) so với USD, hiển thị giá trị số ở nửa dưới và biểu tượng hình tròn theo thang màu từ -1.0 đến 1.0 ở nửa trên.

1. Đối với bất kỳ tương quan hạng Spearman từng cặp nào trong số này, chúng ta có thể bác bỏ giả thuyết không về việc không có tương quan ($H_0: r_S = 0$ và $H_a: r_S \ne 0$) ở mức ý nghĩa $5\%$ hay không? 

###### **Lời giải (*Solution*):** 

Các giá trị $t$ tới hạn cho $2.5\%$ ở mỗi đuôi của phân phối là $\pm 1.97338$. 

Có năm tỷ giá hối đoái, vì vậy có $_5C_2 = \frac{5!}{2!(5 - 2)!}$, hay 10 cặp tương quan duy nhất. Do đó, chúng ta cần tính 10 thống kê $t$. Ví dụ, tương quan giữa EUR/USD và AUD/USD là $0.6079$. Thống kê $t$ tính toán được là: 

![](assets/Quantitative_method.pdf-0259-08.png)

<!-- Formula Text: 0.6079 √ _ 180 − 2 ____________ √ _ 1 − 0.6079 2     =   8.11040 _ 0.79401   =  10.2144. -->
$$t = \frac{0.6079\sqrt{180 - 2}}{\sqrt{1 - 0.6079^2}} = \frac{8.11040}{0.79401} = 10.2144$$

Lặp lại phép tính thống kê $t$ này cho mỗi cặp tỷ giá hối đoái mang lại các thống kê kiểm định được trình bày trong Minh họa 6. 

**Minh họa 6: Các Thống kê Kiểm định Tính toán được cho Kiểm định Tương quan Hạng Spearman (*Exhibit 6: Calculated Test Statistics for Test of Spearman Rank Correlations*)** 

||**AUD/USD**|**CAD/USD**|**EUR/USD**|**GBP/USD**|
|---|---|---|---|---|
|CAD/USD|29.7409||||
|EUR/USD|10.2144|9.1455|||
|GBP/USD|12.4277|13.2513|7.4773||
|JPY/USD|−2.6851|−3.6726|5.2985|−2.7887|

Nhà phân tích nên bác bỏ tất cả 10 giả thuyết không, bởi vì các thống kê $t$ tính toán được cho tất cả các cặp tỷ giá hối đoái đều nằm ngoài giới hạn của hai giá trị tới hạn. Cô nên kết luận rằng tất cả các tương quan cặp tỷ giá hối đoái đều khác $0$ ở mức ý nghĩa $5\%$. 


<!-- PDF Page 260 -->

###### **BỘ CÂU HỎI (*QUESTION SET*)** 

Bạn đang quan tâm đến việc liệu tỷ suất sinh lợi vượt trội đã điều chỉnh rủi ro (alpha) có tương quan với tỷ lệ chi phí (*expense ratios*) của quỹ tương hỗ đối với các quỹ tăng trưởng vốn hóa lớn tại Hoa Kỳ hay không. Bảng sau đây trình bày dữ liệu mẫu. 

|**Quỹ Tương hỗ (*Mutual Fund*)**|**Alpha**|**Tỷ lệ Chi phí (*Expense Ratio*)**|
|---|---|---|
|1|−0.52|1.34|
|2|−0.13|0.40|
|3|−0.50|1.90|
|4|−1.01|1.50|
|5|−0.26|1.35|
|6|−0.89|0.50|
|7|−0.42|1.00|
|8|−0.23|1.50|
|9|−0.60|1.45|

1. Thiết lập giả thuyết không và giả thuyết đối nhất quán với mô tả bằng lời về mục tiêu nghiên cứu. 

###### **Lời giải (*Solution*):** 

Chúng ta có một giả thuyết đối dạng “khác” (*not equal to*): 

$$H_0: \rho = 0 \text{ đối lập với } H_a: \rho \ne 0$$

2. Xác định và giải thích lý do lựa chọn thống kê kiểm định để tiến hành kiểm định các giả thuyết ở Câu 1. 

###### **Lời giải (*Solution*):** 

Tỷ lệ chi phí của quỹ tương hỗ bị chặn trên và chặn dưới; trên thực tế, có ít nhất một cận dưới đối với alpha (vì bất kỳ tỷ suất sinh lợi nào cũng không thể nhỏ hơn $-100\%$), và tỷ lệ chi phí không thể âm. Các biến số này có thể không có phân phối chuẩn, và các giả định của một kiểm định tham số không có khả năng được thỏa mãn. Do đó, một kiểm định phi tham số có vẻ là phù hợp. 

Chúng ta sẽ sử dụng hệ số tương quan hạng Spearman phi tham số để tiến hành kiểm định: 

![](assets/Quantitative_method.pdf-0260-14.png)

<!-- Formula Text: r s  =  1 − 6∑ i=1 n d i 2 _ n(n 2 − 1) -->
$$r_S = 1 - \frac{6 \sum_{i=1}^{n} d_i^2}{n(n^2 - 1)}$$

với thống kê kiểm định có phân phối $t$ là: 

![](assets/Quantitative_method.pdf-0260-16.png)

<!-- Formula Text: t  =   r √ _ n − 2 _ √ _ 1 − r 2  . -->
$$t = \frac{r\sqrt{n - 2}}{\sqrt{1 - r^2}}$$

Phép tính hệ số tương quan hạng Spearman được cho trong bảng tiếp theo *(xem đầu Phần 2)*. 
