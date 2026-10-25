# Tập 1: Phương pháp Định lượng (*Quantitative Methods*)
## Học phần 8: Kiểm định Giả thuyết (*Hypothesis Testing*)
### Phần 2/3: Các Kiểm định Tỷ suất sinh lợi và Rủi ro trong Tài chính (*Tests of Return and Risk in Finance*) (Trang PDF 230–243)

---

<!-- PDF Page 230 -->

3. Đối với mỗi kiểm định giả thuyết sau đây liên quan đến trung bình tổng thể, $\mu$, hãy nêu kết luận về việc kiểm định các giả thuyết. 

   - **A.** $H_0: \mu = 10$ đối lập với $H_a: \mu \ne 10$, với thống kê $t$ tính toán được là $2.05$ và các giá trị $t$ tới hạn là $\pm 1.984$. 
   - **B.** $H_0: \mu \le 10$ đối lập với $H_a: \mu > 10$, với thống kê $t$ tính toán được là $2.35$ và giá trị $t$ tới hạn là $+1.679$. 
   - **C.** $H_0: \mu = 10$ đối lập với $H_a: \mu \ne 10$, với thống kê $t$ tính toán được là $2.05$, giá trị $p$ (*p-value*) là $4.6352\%$, và mức ý nghĩa là $5\%$. 
   - **D.** $H_0: \mu \le 10$ đối lập với $H_a: \mu > 10$, với mức ý nghĩa $2\%$ và thống kê kiểm định tính toán được có giá trị $p$ là $3\%$. 

#### **Lời giải (*Solution*):** 

Chúng ta đưa ra quyết định bằng cách so sánh thống kê kiểm định tính toán được với các giá trị tới hạn hoặc bằng cách so sánh giá trị $p$ của thống kê kiểm định tính toán được với mức ý nghĩa. 

- **A.** Bác bỏ giả thuyết không vì thống kê kiểm định tính toán được là $2.05$ nằm ngoài giới hạn của các giá trị tới hạn $\pm 1.984$. 
- **B.** Bác bỏ giả thuyết không vì thống kê kiểm định tính toán được là $2.35$ nằm ngoài giới hạn của giá trị tới hạn $+1.679$. 
- **C.** Giá trị $p$ tương ứng với thống kê kiểm định tính toán được là $4.6352\%$ nhỏ hơn mức ý nghĩa ($5\%$), vì vậy chúng ta bác bỏ giả thuyết không. 
- **D.** Chúng ta không bác bỏ giả thuyết không vì giá trị $p$ cho thống kê kiểm định tính toán được là $3\%$ lớn hơn mức ý nghĩa ($2\%$). 

# **<mark>3</mark>** 

## **CÁC KIỂM ĐỊNH TỶ SUẤT SINH LỢI VÀ RỦI RO TRONG TÀI CHÍNH (*TESTS OF RETURN AND RISK IN FINANCE*)** 

*Xây dựng các kiểm định giả thuyết và xác định ý nghĩa thống kê của chúng, các sai lầm Loại I và Loại II liên quan, cũng như lực kiểm định khi biết trước một mức ý nghĩa*

Các kiểm định giả thuyết liên quan đến tỷ suất sinh lợi và rủi ro nằm trong số những kiểm định phổ biến nhất trong tài chính. Phân phối mẫu của giá trị trung bình, khi độ lệch chuẩn của tổng thể chưa biết, có phân phối $t$ (*t-distributed*), và khi độ lệch chuẩn của tổng thể đã biết, nó có phân phối chuẩn, hay phân phối $z$ (*z-distributed*). Vì độ lệch chuẩn của tổng thể hầu như luôn chưa biết trong mọi trường hợp, chúng ta sẽ tập trung vào việc sử dụng thống kê kiểm định có phân phối $t$. 

#### **KIỂM ĐỊNH MỘT GIÁ TRỊ TRUNG BÌNH ĐƠN LẺ: ĐẶC ĐIỂM RỦI RO VÀ TỶ SUẤT SINH LỢI CỦA MỘT QUỸ TƯƠNG HỖ CỔ PHIẾU (*TEST OF A SINGLE MEAN: RISK AND RETURN CHARACTERISTICS OF AN EQUITY MUTUAL FUND*)** 

Giả sử bạn đang phân tích Quỹ Cổ phiếu Sendar (*Sendar Equity Fund*). Trong 24 tháng qua, quỹ đã đạt được tỷ suất sinh lợi hàng tháng trung bình là $1.50\%$, với độ lệch chuẩn mẫu của tỷ suất sinh lợi hàng tháng là $3.60\%$. Với mức độ rủi ro thị trường của quỹ và theo một mô hình định giá, quỹ tương hỗ này được kỳ vọng đạt tỷ suất sinh lợi hàng tháng trung bình là $1.10\%$ trong khoảng thời gian đó. 

Giả sử tỷ suất sinh lợi có phân phối chuẩn, liệu kết quả thực tế có nhất quán với một trung bình tổng thể của tỷ suất sinh lợi hàng tháng là $1.10\%$ hay không? 


<!-- PDF Page 231 -->

Hãy thiết lập và kiểm định giả thuyết rằng kết quả hoạt động của quỹ khác với tỷ suất sinh lợi trung bình $1.1\%$ được suy ra từ mô hình định giá. Sử dụng mức ý nghĩa $5\%$. 

**Minh họa 5: Kiểm định Một Giá trị Trung bình Đơn lẻ (*Exhibit 5: Test of a Single Mean*)** 

|**Bước 1 (*Step 1*)**|Phát biểu các giả thuyết.|$$H_0: \mu = 1.1\% \text{ đối lập với } H_a: \mu \ne 1.1\%$$|
|---|---|---|
|**Bước 2 (*Step 2*)**|Xác định thống kê kiểm định phù hợp.|$$t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}$$<br>với $24 - 1 = 23$ bậc tự do.|
|**Bước 3 (*Step 3*)**|Xác định mức ý nghĩa.|$\alpha = 5\%$ (hai phía – *two tailed*).|
|**Bước 4 (*Step 4*)**|Phát biểu quy tắc quyết định.|Các giá trị $t$ tới hạn $= \pm 2.069$.<br>Bác bỏ giả thuyết không nếu thống kê $t$ tính toán được nhỏ hơn $-2.069$, và bác bỏ giả thuyết không nếu thống kê $t$ tính toán được lớn hơn $+2.069$.<br>**Excel**<br> _Cận dưới (Lower):_ `T.INV(0.025,23)`<br> _Cận trên (Upper):_ `T.INV(0.975,23)`<br>**R** `qt(c(.025,.975),23)`<br>**Python** `from scipy.stats import t`<br> _Cận dưới (Lower):_ `t.ppf(.025,23)`<br> _Cận trên (Upper):_ `t.ppf(.975,23)`|
|**Bước 5 (*Step 5*)**|Tính toán thống kê kiểm định.|$$t = \frac{1.5 - 1.1}{3.6 / \sqrt{24}} = 0.54433$$|
|**Bước 6 (*Step 6*)**|Đưa ra quyết định.|Không bác bỏ giả thuyết không vì thống kê $t$ tính toán được nằm giữa hai giá trị tới hạn. Không có đủ bằng chứng để chỉ ra rằng trung bình tổng thể của tỷ suất sinh lợi hàng tháng khác với $1.10\%$.|

Kiểm định giả thuyết bằng cách sử dụng khoảng tin cậy $95\%$. Khoảng tin cậy $95\%$ là $\bar{X} \pm \text{Giá trị tới hạn} \times \left(\frac{s}{\sqrt{n}}\right)$, do đó:
$$\left\{1.5 - 2.069 \left(\frac{3.6}{\sqrt{24}}\right), \; 1.5 + 2.069 \left(\frac{3.6}{\sqrt{24}}\right)\right\}$$
$$\{1.5 - 1.5204, \; 1.5 + 1.5204\}$$
$$\{-0.0204, \; 3.0204\}$$
Giá trị theo giả thuyết là $1.1\%$ nằm trong giới hạn của khoảng tin cậy $95\%$, vì vậy chúng ta không bác bỏ giả thuyết không. 

#### **KIỂM ĐỊNH MỘT PHƯƠNG SAI ĐƠN LẺ: ĐẶC ĐIỂM RỦI RO CỦA MỘT QUỸ TƯƠNG HỖ CỔ PHIẾU (*TEST OF A SINGLE VARIANCE: RISK CHARACTERISTICS OF AN EQUITY MUTUAL FUND*)** 

Giả sử chúng ta muốn sử dụng phương sai mẫu quan sát được của quỹ để kiểm định xem liệu phương sai thực sự của quỹ có thấp hơn một mức ngưỡng kích hoạt (*trigger level*) nào đó, chẳng hạn độ lệch chuẩn $4\%$, hay không. Việc thực hiện kiểm định phương sai tổng thể đòi hỏi phải chỉ định giá trị theo giả thuyết của phương sai. Chúng ta có thể thiết lập các giả thuyết liên quan đến việc liệu phương sai có bằng một giá trị cụ thể hay lớn hơn hoặc nhỏ hơn một giá trị theo giả thuyết: 

Giả thuyết đối một phía (đuôi bên trái – *left tail*): $H_0: \sigma^2 \ge \sigma_0^2$ đối lập với $H_a: \sigma^2 < \sigma_0^2$. 


<!-- PDF Page 232 -->

Lưu ý rằng độ lệch chuẩn của quỹ nhỏ hơn mức ngưỡng kích hoạt $\sigma_0 = 4\%$ (tức phương sai $\sigma_0^2 = 16(\%^2)$ hoặc $0.0016$) nếu giả thuyết không bị bác bỏ để ủng hộ giả thuyết đối. Trong các kiểm định liên quan đến phương sai của một tổng thể đơn lẻ có phân phối chuẩn, chúng ta sử dụng thống kê kiểm định Khi-bình phương (*chi-square test statistic*), được ký hiệu là $\chi^2$. 

Bạn tiếp tục phân tích Quỹ Cổ phiếu Sendar, một quỹ tăng trưởng vốn hóa trung bình (*midcap growth fund*) mới chỉ tồn tại được 24 tháng. Trong giai đoạn này, Quỹ Cổ phiếu Sendar đạt tỷ suất sinh lợi hàng tháng trung bình là $1.50\%$ và độ lệch chuẩn của tỷ suất sinh lợi hàng tháng là $3.60\%$. Sử dụng mức ý nghĩa $5\%$, hãy kiểm định xem liệu độ lệch chuẩn của tỷ suất sinh lợi có nhỏ hơn $4\%$ hay không. Hãy nhớ lại rằng độ lệch chuẩn là căn bậc hai của phương sai, do đó độ lệch chuẩn $4\%$ hay $0.04$ tương đương với phương sai là $16(\%^2)$ hay $0.0016$ (và $s = 3.60\%$ tương đương $s^2 = 3.6^2 = 12.96$). 

#### **Minh họa 6: Kiểm định Một Phương sai Đơn lẻ (*Exhibit 6: Test of Single Variance*)** 

|**Bước 1 (*Step 1*)**|Phát biểu các giả thuyết.|$$H_0: \sigma^2 \ge 16 \text{ đối lập với } H_a: \sigma^2 < 16$$|
|---|---|---|
|**Bước 2 (*Step 2*)**|Xác định thống kê kiểm định phù hợp.|$$\chi^2 = \frac{(n - 1)s^2}{\sigma_0^2}$$|
|**Bước 3 (*Step 3*)**|Xác định mức ý nghĩa.|$5\%$|
|**Bước 4 (*Step 4*)**|Phát biểu quy tắc quyết định.|Với $24 - 1 = 23$ bậc tự do, giá trị tới hạn là $13.09051$.<br>*(Lưu ý nguyên bản sách CFA và đính chính chuẩn xác: Kiểm định đuôi trái $H_a: \sigma^2 < 16$ có miền bác bỏ ở phía trái, tức bác bỏ $H_0$ nếu thống kê $\chi^2$ tính được nhỏ hơn $13.09051$; bản gốc in nhầm chữ "greater than").*<br>**Excel** `CHISQ.INV(0.05,23)`<br>**R** `qchisq(.05,23)`<br>**Python**<br>`from scipy.stats import chi2`<br>`chi2.ppf(.05,23)`|
|**Bước 5 (*Step 5*)**|Tính toán thống kê kiểm định.|$$\chi^2 = \frac{(24 - 1)12.96}{16} = 18.63000$$|
|**Bước 6 (*Step 6*)**|Đưa ra quyết định.|*(Theo văn bản gốc trong sách)*: Bác bỏ giả thuyết không bởi vì thống kê $\chi^2$ tính toán được lớn hơn giá trị tới hạn. Có đủ bằng chứng để chỉ ra rằng phương sai nhỏ hơn $16\%$ (hoặc tương đương là độ lệch chuẩn nhỏ hơn $4\%$). *(Lưu ý học thuật: Với $\chi^2 = 18.63 > 13.09051$, thực tế thống kê kiểm định không rơi vào miền bác bỏ đuôi trái nên đúng về mặt toán học là không thể bác bỏ $H_0$).*|

#### **KIỂM ĐỊNH LIÊN QUAN ĐẾN SỰ KHÁC BIỆT GIỮA HAI GIÁ TRỊ TRUNG BÌNH VỚI CÁC MẪU ĐỘC LẬP (*TEST CONCERNING DIFFERENCES BETWEEN MEANS WITH INDEPENDENT SAMPLES*)** 

Chúng ta thường muốn biết liệu một giá trị trung bình—ví dụ, tỷ suất sinh lợi trung bình—có khác nhau giữa hai nhóm hay không. Sự khác biệt quan sát được là do ngẫu nhiên hay do các giá trị cơ sở khác nhau của giá trị trung bình? Chúng ta kiểm định điều này bằng cách rút một mẫu từ mỗi nhóm. Khi có cơ sở hợp lý để tin rằng các mẫu đến từ các tổng thể có phân phối xấp xỉ chuẩn và các mẫu cũng độc lập với nhau, chúng ta sử dụng kiểm định sự khác biệt giữa hai giá trị trung bình (*test of the difference in the means*). Chúng ta có thể giả định rằng các phương sai tổng thể bằng nhau hoặc không bằng nhau. Tuy nhiên, trọng tâm của chúng ta khi thảo luận về kiểm định sự khác biệt giữa hai giá trị trung bình là sử dụng giả định rằng các phương sai tổng thể bằng nhau. Trong phép tính thống kê kiểm định, chúng ta kết hợp các quan sát từ cả hai mẫu để thu được một ước lượng gộp (*pooled estimate*) của phương sai tổng thể chung. 

Gọi $\mu_1$ và $\mu_2$ lần lượt đại diện cho trung bình tổng thể của tổng thể thứ nhất và tổng thể thứ hai. Thường thì chúng ta muốn kiểm định xem các trung bình tổng thể có bằng nhau hay không hoặc liệu có một giá trị lớn hơn giá trị kia hay không. Do đó, chúng ta thiết lập các giả thuyết sau: 


<!-- PDF Page 233 -->

$$H_0: \mu_1 - \mu_2 = 0 \text{ đối lập với } H_a: \mu_1 - \mu_2 \ne 0$$

#### **VÍ DỤ 1 (*EXAMPLE 1*)** 

### **So sánh Tỷ suất sinh lợi trên Chỉ số ACE High Yield trong Hai Giai đoạn (*Comparison of Returns on the ACE High Yield Index for Two Periods*)** 

Giả sử chúng ta muốn kiểm định xem tỷ suất sinh lợi của Chỉ số Tổng Tỷ suất sinh lợi Lợi suất Cao ACE (*ACE High Yield Total Return Index*), được trình bày trong Minh họa 7, có khác nhau trong hai giai đoạn thời gian khác nhau là Giai đoạn 1 và Giai đoạn 2 hay không. 

**Minh họa 7: Thống kê Mô tả cho Chỉ số Tổng Tỷ suất sinh lợi Lợi suất Cao ACE trong Giai đoạn 1 và 2 (*Exhibit 7: Descriptive Statistics for ACE High Yield Total Return Index for Periods 1 and 2*)** 

||**Giai đoạn 1 (*Period 1*)**|**Giai đoạn 2 (*Period 2*)**|
|---|---|---|
|**Giá trị trung bình (*Mean*)**|0.01775%|0.01134%|
|**Độ lệch chuẩn (*Standard deviation*)**|0.31580%|0.38760%|
|**Kích thước mẫu (*Sample size*)**|445 ngày|859 ngày|

Lưu ý rằng các giai đoạn này có độ dài khác nhau và các mẫu độc lập với nhau; tức là không có sự ghép cặp các ngày giữa hai giai đoạn. 

1. Có sự khác biệt nào giữa tỷ suất sinh lợi hàng ngày trung bình trong Giai đoạn 1 và Giai đoạn 2 hay không, sử dụng mức ý nghĩa $5\%$? 

#### **Lời giải (*Solution*):** 

- **Bước 1:** Phát biểu các giả thuyết.
  $$H_0: \mu_{\text{Period 1}} = \mu_{\text{Period 2}} \text{ đối lập với } H_a: \mu_{\text{Period 1}} \ne \mu_{\text{Period 2}}$$
- **Bước 2:** Xác định thống kê kiểm định phù hợp.
  $$t = \frac{(\bar{X}_{\text{Period 1}} - \bar{X}_{\text{Period 2}}) - (\mu_{\text{Period 1}} - \mu_{\text{Period 2}})}{\sqrt{\frac{s_p^2}{n_{\text{Period 1}}} + \frac{s_p^2}{n_{\text{Period 2}}}}}$$
  trong đó:
  $$s_p^2 = \frac{(n_{\text{Period 1}} - 1)s_{\text{Period 1}}^2 + (n_{\text{Period 2}} - 1)s_{\text{Period 2}}^2}{n_{\text{Period 1}} + n_{\text{Period 2}} - 2}$$
  với $445 + 859 - 2 = 1,302$ bậc tự do.
- **Bước 3:** Xác định mức ý nghĩa. $\alpha = 5\%$.
- **Bước 4:** Phát biểu quy tắc quyết định.
  Các giá trị $t$ tới hạn $= \pm 1.962$.
  Bác bỏ giả thuyết không nếu thống kê $t$ tính toán được nhỏ hơn $-1.962$, và bác bỏ giả thuyết không nếu thống kê $t$ tính toán được lớn hơn $+1.962$.
  - **Excel:** _Cận dưới (Lower):_ `T.INV(0.025,1302)` | _Cận trên (Upper):_ `T.INV(0.975,1302)`
  - **R:** `qt(c(.025,.975),1302)`
  - **Python:** `from scipy.stats import t` | _Cận dưới (Lower):_ `t.ppf(.025,1302)` | _Cận trên (Upper):_ `t.ppf(.975,1302)`


<!-- PDF Page 234 -->

![](assets/Quantitative_method.pdf-0234-04.png)

<!-- Formula Text: Step 5 Calculate the test statistic. s p 2  =   (445 − 1 ) 0.09973 + (859 − 1 ) 0.15023 ____________________________ 445 + 859 − 2 =  0.1330 t  =   (0.01775 − 0.01134 ) − 0 __________________ √ _____________ 0.1330 _ 445   +  0.1330 _ 859 =   0.0064 _ 0.0213   =  0.3009. Step 6 Make a decision. Fail to reject the null because the calculated t-statistic falls within the bounds of the two critical values. We conclude that there is insufficient evidence to indicate that the returns are different for the two time periods. -->

- **Bước 5:** Tính toán thống kê kiểm định.
  $$s_p^2 = \frac{(445 - 1)0.09973 + (859 - 1)0.15023}{445 + 859 - 2} = 0.1330$$
  $$t = \frac{(0.01775 - 0.01134) - 0}{\sqrt{\frac{0.1330}{445} + \frac{0.1330}{859}}} = \frac{0.0064}{0.0213} = 0.3009$$
- **Bước 6:** Đưa ra quyết định.
  Không bác bỏ giả thuyết không bởi vì thống kê $t$ tính toán được nằm trong giới hạn của hai giá trị tới hạn. Chúng ta kết luận rằng không có đủ bằng chứng để chỉ ra rằng tỷ suất sinh lợi là khác nhau giữa hai giai đoạn thời gian.

### **Kiểm định Liên quan đến Sự khác biệt giữa Hai Giá trị Trung bình với các Mẫu Phụ thuộc (*Test Concerning Differences between Means with Dependent Samples*)** 

Khi chúng ta so sánh hai mẫu độc lập, chúng ta sử dụng một thống kê kiểm định có phân phối $t$ sử dụng hiệu số giữa hai trung bình mẫu và một phương sai gộp (*pooled variance*). Một giả định cho tính hợp lệ của các kiểm định đó là các mẫu phải độc lập—tức là không liên quan với nhau. Khi chúng ta muốn tiến hành kiểm định trên hai giá trị trung bình dựa trên các mẫu mà chúng ta tin là phụ thuộc lẫn nhau, chúng ta sử dụng **kiểm định giá trị trung bình của các chênh lệch (*test of the mean of the differences* – hay kiểm định so sánh cặp, *paired comparisons test*)**. 

Kiểm định các chênh lệch ghép cặp này khác với kiểm định sự khác biệt giữa hai giá trị trung bình trong các mẫu độc lập như thế nào? Kiểm định so sánh cặp có lực kiểm định mạnh hơn (*more powerful*) so với kiểm định sự khác biệt giữa hai giá trị trung bình bởi vì bằng cách sử dụng yếu tố chung (chẳng hạn như cùng các giai đoạn thời gian hoặc cùng các công ty), chúng ta loại bỏ được sự biến thiên giữa các mẫu có thể gây ra bởi những yếu tố khác ngoài yếu tố mà chúng ta đang kiểm định. 

#### **VÍ DỤ 2 (*EXAMPLE 2*)** 

### **So sánh Tỷ suất sinh lợi của Hai Chỉ số (*A Comparison of the Returns of Two Indexes*)** 

Giả sử chúng ta muốn so sánh tỷ suất sinh lợi của Chỉ số ACE High Yield với tỷ suất sinh lợi của Chỉ số ACE BBB. Chúng ta thu thập dữ liệu trong cùng 1,304 ngày cho cả hai chỉ số và tính giá trị trung bình cũng như độ lệch chuẩn của chúng như được trình bày trong Minh họa 8. 

**Minh họa 8: Giá trị Trung bình và Độ lệch chuẩn của Chỉ số ACE High Yield và Chỉ số ACE BBB (*Exhibit 8: Mean and Standard Deviations for the ACE High Yield Index and the ACE BBB Index*)** 

||**Chỉ số ACE High Yield (%)**|**Chỉ số ACE BBB (%)**|**Chênh lệch (*Difference*) (%)**|
|---|---|---|---|
|Tỷ suất sinh lợi trung bình (*Mean return*)|0.0157|0.0135|−0.0021|
|Độ lệch chuẩn (*Standard deviation*)|0.3157|0.3645|0.3622|

1. Sử dụng mức ý nghĩa $5\%$, liệu giá trị trung bình của các chênh lệch có khác $0$ hay không? 

#### **Lời giải (*Solution*):** 

- **Bước 1:** Phát biểu các giả thuyết. $H_0: \mu_{d0} = 0$ đối lập với $H_a: \mu_{d0} \ne 0$.
- **Bước 2:** Xác định thống kê kiểm định phù hợp.
  $$t = \frac{\bar{d} - \mu_{d0}}{s_{\bar{d}}}$$
- **Bước 3:** Xác định mức ý nghĩa. $5\%$.


<!-- PDF Page 235 -->

|**Bước 4 (*Step 4*)**|Phát biểu quy tắc quyết định.|Với $1,304 - 1 = 1,303$ bậc tự do, các giá trị tới hạn là $\pm 1.962$.<br>Chúng ta bác bỏ giả thuyết không nếu thống kê $t$ tính toán được nhỏ hơn $-1.962$ hoặc lớn hơn $+1.962$.<br>**Excel**<br>_Cận dưới (Lower):_ `T.INV(0.025,1303)`<br>_Cận trên (Upper):_ `T.INV(0.975,1303)`<br>**R** `qt(c(.025,.975),1303)`<br>**Python** `from scipy.stats import t`<br>_Cận dưới (Lower):_ `t.ppf(.025,1303)`<br>_Cận trên (Upper):_ `t.ppf(.975,1303)`|
|---|---|---|
|**Bước 5 (*Step 5*)**|Tính toán thống kê kiểm định.|$$\bar{d} = -0.0021\%$$<br>$$s_{\bar{d}} = \frac{s_d}{\sqrt{n}} = \frac{0.3622}{\sqrt{1,304}} = 0.01003\%$$<br>$$t = \frac{-0.00210 - 0}{0.01003} = -0.20937$$|
|**Bước 6 (*Step 6*)**|Đưa ra quyết định.|Không bác bỏ giả thuyết không bởi vì thống kê $t$ tính toán được nằm trong giới hạn của hai giá trị tới hạn. Không có đủ bằng chứng để chỉ ra rằng giá trị trung bình của các chênh lệch tỷ suất sinh lợi là khác $0$.|

### **Kiểm định Liên quan đến Sự Bằng nhau của Hai Phương sai (*Test Concerning the Equality of Two Variances*)** 

Có nhiều trường hợp chúng ta muốn so sánh độ biến động (*volatility*) của hai mẫu, khi đó chúng ta có thể kiểm định sự bằng nhau của hai phương sai. Các ví dụ bao gồm so sánh các rổ chứng khoán với các chỉ số hoặc chỉ số chuẩn (*benchmarks*), cũng như so sánh độ biến động trong các giai đoạn khác nhau. 

#### **VÍ DỤ 3 (*EXAMPLE 3*)** 

### **Độ biến động và Quy định Quản lý (*Volatility and Regulation*)** 

Bạn đang khảo sát xem liệu phương sai tổng thể của tỷ suất sinh lợi trên một chỉ số thị trường chứng khoán có thay đổi sau một sự thay đổi trong quy định quản lý thị trường hay không. 418 tuần đầu tiên diễn ra trước khi thay đổi quy định, và 418 tuần thứ hai diễn ra sau khi thay đổi quy định. Bạn thu thập dữ liệu trong Minh họa 9 cho 418 tuần tỷ suất sinh lợi cả trước và sau khi thay đổi quy định. Bạn đã chỉ định mức ý nghĩa là $5\%$. 

#### **Minh họa 9: Tỷ suất sinh lợi và Phương sai Chỉ số Trước và Sau khi Thay đổi Quy định Thị trường (*Exhibit 9: Index Returns and Variances before and after the Market Regulation Change*)** 

||**$N$**|**Tỷ suất sinh lợi Hàng tuần Trung bình (*Mean Weekly Return*) (%)**|**Phương sai của Tỷ suất sinh lợi (*Variance of Returns*)**|
|---|---|---|---|
|Trước khi thay đổi quy định (*Before regulation change*)|418|0.250|4.644|
|Sau khi thay đổi quy định (*After regulation change*)|418|0.110|3.919|

1. Phương sai của tỷ suất sinh lợi trước khi thay đổi quy định có khác với sau khi thay đổi quy định hay không? 

**Lời giải (*Solution*):** 


<!-- PDF Page 236 -->

|**Bước 1 (*Step 1*)**|Phát biểu các giả thuyết.|$$H_0: \sigma_{\text{Before}}^2 = \sigma_{\text{After}}^2 \text{ đối lập với } H_a: \sigma_{\text{Before}}^2 \ne \sigma_{\text{After}}^2$$|
|---|---|---|
|**Bước 2 (*Step 2*)**|Xác định thống kê kiểm định phù hợp.|$$F = \frac{s_{\text{Before}}^2}{s_{\text{After}}^2}$$|
|**Bước 3 (*Step 3*)**|Xác định mức ý nghĩa.|$5\%$|
|**Bước 4 (*Step 4*)**|Phát biểu quy tắc quyết định.|Với $418 - 1 = 417$ và $418 - 1 = 417$ bậc tự do, các giá trị tới hạn là $0.82512$ và $1.21194$.<br>Bác bỏ giả thuyết không nếu thống kê $F$ tính toán được nhỏ hơn $0.82512$ hoặc lớn hơn $1.21194$.<br>**Excel**<br> _Phía trái (Left side):_ `F.INV(0.025,417,417)`<br> _Phía phải (Right side):_ `F.INV(0.975,417,417)`<br>**R** `qf(c(.025,.975),417,417)`<br>**Python** `from scipy.stats import f`<br> _Phía trái (Left side):_ `f.ppf(.025,417,417)`<br> _Phía phải (Right side):_ `f.ppf(.975,417,417)`|
|**Bước 5 (*Step 5*)**|Tính toán thống kê kiểm định.|$$F = \frac{4.644}{3.919} = 1.18500$$|
|**Bước 6 (*Step 6*)**|Đưa ra quyết định.|Không bác bỏ giả thuyết không vì thống kê $F$ tính toán được nằm trong giới hạn của hai giá trị tới hạn. Không có đủ bằng chứng để chỉ ra rằng phương sai hàng tuần của tỷ suất sinh lợi là khác nhau trong giai đoạn trước và sau khi thay đổi quy định.|

2. Phương sai của tỷ suất sinh lợi trước khi thay đổi quy định có lớn hơn so với sau khi thay đổi quy định hay không?

**Lời giải (*Solution*):**

|**Bước 1 (*Step 1*)**|Phát biểu các giả thuyết.|$$H_0: \sigma_{\text{Before}}^2 \le \sigma_{\text{After}}^2 \text{ đối lập với } H_a: \sigma_{\text{Before}}^2 > \sigma_{\text{After}}^2$$|
|---|---|---|
|**Bước 2 (*Step 2*)**|Xác định thống kê kiểm định phù hợp.|$$F = \frac{s_{\text{Before}}^2}{s_{\text{After}}^2}$$|
|**Bước 3 (*Step 3*)**|Xác định mức ý nghĩa.|$5\%$|
|**Bước 4 (*Step 4*)**|Phát biểu quy tắc quyết định.|Với $418 - 1 = 417$ và $418 - 1 = 417$ bậc tự do, giá trị tới hạn là $1.17502$.<br>Chúng ta bác bỏ giả thuyết không nếu thống kê $F$ tính toán được lớn hơn $1.17502$.<br>**Excel** `F.INV(0.95,417,417)`<br>**R** `qf(.95,417,417)`<br>**Python**<br>`from scipy.stats import f`<br>`f.ppf(.95,417,417)`|
|**Bước 5 (*Step 5*)**|Tính toán thống kê kiểm định.|$$F = \frac{4.644}{3.919} = 1.18500$$|
|**Bước 6 (*Step 6*)**|Đưa ra quyết định.|Bác bỏ giả thuyết không vì thống kê $F$ tính toán được lớn hơn $1.17502$. Có đủ bằng chứng để chỉ ra rằng phương sai hàng tuần của tỷ suất sinh lợi trước khi thay đổi quy định lớn hơn phương sai sau khi thay đổi quy định.|


<!-- PDF Page 237 -->

#### **BỘ CÂU HỎI (*QUESTION SET*)** 

Các nhà phân tích đầu tư thường sử dụng các dự báo thu nhập trên mỗi cổ phiếu (*earnings per share* – EPS). Một kiểm định về chất lượng dự báo là kiểm định trung bình bằng không (*zero-mean test*), phát biểu rằng các dự báo tối ưu phải có sai số dự báo trung bình bằng 0. Sai số dự báo (*forecasting error*) là chênh lệch giữa giá trị dự đoán của một biến số và giá trị thực tế của biến số đó. 

Bạn đã thu thập dữ liệu (được hiển thị trong Minh họa 10) của hai nhà phân tích phụ trách hai ngành khác nhau: Nhà phân tích A phụ trách ngành viễn thông; Nhà phân tích B phụ trách ngành phụ tùng và nhà cung cấp ô tô. 

**Minh họa 10: Kiểm định Tỷ suất sinh lợi và Rủi ro – Hiệu quả Dự báo Thu nhập trên mỗi Cổ phiếu Hàng quý (*Exhibit 10: Test of Return and Risk – Performance in Forecasting Quarterly Earnings per Share*)** 

||**Số lượng Dự báo (*Number of Forecasts*)**|**Sai số Dự báo Trung bình (Dự đoán − Thực tế) (*Mean Forecast Error: Predicted − Actual*)**|**Độ lệch chuẩn của Sai số Dự báo (*Standard Deviation of Forecast Errors*)**|
|---|---|---|---|
|Nhà phân tích A (*Analyst A*)|10|0.05|0.10|
|Nhà phân tích B (*Analyst B*)|15|0.02|0.09|

Các giá trị $t$ tới hạn (*Critical t-values*): 

|**Bậc Tự do (*Degrees of Freedom*)**|**Diện tích Miền Bác bỏ Phía Bên phải (*Area in the Right-Side Rejection Area*): $p = 0.05$**|**Diện tích Miền Bác bỏ Phía Bên phải (*Area in the Right-Side Rejection Area*): $p = 0.025$**|
|---|---|---|
|8|1.860|2.306|
|9|1.833|2.262|
|10|1.812|2.228|
|11|1.796|2.201|
|12|1.782|2.179|
|13|1.771|2.160|
|14|1.761|2.145|
|15|1.753|2.131|
|16|1.746|2.120|
|17|1.740|2.110|
|18|1.734|2.101|
|19|1.729|2.093|
|20|1.725|2.086|
|21|1.721|2.080|
|22|1.717|2.074|
|23|1.714|2.069|
|24|1.711|2.064|
|25|1.708|2.060|
|26|1.706|2.056|
|27|1.703|2.052|


<!-- PDF Page 238 -->

1. Với $\mu$ là sai số dự báo trung bình của tổng thể, hãy thiết lập giả thuyết không và giả thuyết đối cho kiểm định trung bình bằng không về chất lượng dự báo. 

   - **A.** Đối với Nhà phân tích A, hãy xác định xem có bác bỏ giả thuyết không ở mức ý nghĩa $0.05$ hay không. 
   - **B.** Đối với Nhà phân tích B, hãy xác định xem có bác bỏ giả thuyết không ở mức ý nghĩa $0.05$ hay không. 

**Lời giải (*Solution*):** 

$$H_0: \mu = 0 \text{ đối lập với } H_a: \mu \ne 0$$

- **A.** Kiểm định $t$ dựa trên $t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}$ với $n - 1 = 10 - 1 = 9$ bậc tự do. Ở mức ý nghĩa $0.05$, chúng ta bác bỏ giả thuyết không nếu thống kê $t$ tính toán được nằm ngoài giới hạn $\pm 2.262$ (tra từ bảng với 9 bậc tự do và $0.025$ ở phía bên phải của phân phối). Đối với Nhà phân tích A, chúng ta có thống kê kiểm định tính toán được là: 

$$t = \frac{0.05 - 0}{0.10 / \sqrt{10}} = 1.58114$$

Do đó, chúng ta không bác bỏ giả thuyết không ở mức ý nghĩa $0.05$. 

- **B.** Đối với Nhà phân tích B, kiểm định $t$ dựa trên $t$ với $15 - 1 = 14$ bậc tự do. Ở mức ý nghĩa $0.05$, chúng ta bác bỏ giả thuyết không nếu thống kê $t$ tính toán được nằm ngoài giới hạn $\pm 2.145$ (tra từ bảng với 14 bậc tự do). Thống kê kiểm định tính toán được là: 

$$t = \frac{0.02 - 0}{0.09 / \sqrt{15}} = 0.86066$$

Bởi vì $0.86066$ nằm trong phạm vi $\pm 2.145$, chúng ta không bác bỏ giả thuyết không ở mức ý nghĩa $0.05$. 

2. Khi xem xét dữ liệu hiệu quả dự báo EPS của Nhà phân tích A và B, bạn muốn khảo sát xem liệu sai số dự báo trung bình lớn hơn của Nhà phân tích A so với Nhà phân tích B là do ngẫu nhiên hay do giá trị trung bình cơ sở cao hơn của Nhà phân tích A. Giả sử rằng sai số dự báo của cả hai nhà phân tích đều có phân phối chuẩn và các mẫu độc lập với nhau. 

   - **A.** Thiết lập giả thuyết không và giả thuyết đối nhất quán với việc xác định xem giá trị trung bình tổng thể của sai số dự báo của Nhà phân tích A ($\mu_1$ hay $\mu_A$) có lớn hơn của Nhà phân tích B ($\mu_2$ hay $\mu_B$) hay không. 
   - **B.** Xác định thống kê kiểm định để tiến hành kiểm định giả thuyết không đã thiết lập ở Phần A. 
   - **C.** Xác định (các) điểm bác bỏ cho các giả thuyết được kiểm định ở Phần A tại mức ý nghĩa $0.05$. 
   - **D.** Xác định xem có bác bỏ giả thuyết không ở mức ý nghĩa $0.05$ hay không. 

**Lời giải (*Solution*):** 

- **A.** Phát biểu điều kiện nghi ngờ làm giả thuyết đối, ta có: 

$$H_0: \mu_A - \mu_B \le 0 \text{ đối lập với } H_a: \mu_A - \mu_B > 0$$

trong đó: 
- $\mu_A =$ giá trị trung bình tổng thể của sai số dự báo của Nhà phân tích A
- $\mu_B =$ giá trị trung bình tổng thể của sai số dự báo của Nhà phân tích B


<!-- PDF Page 239 -->

- **B.** Chúng ta có hai tổng thể có phân phối chuẩn với phương sai chưa biết. Dựa trên các mẫu, có cơ sở hợp lý để giả định rằng các phương sai tổng thể bằng nhau. Các mẫu được giả định là độc lập; giả định này hợp lý vì các nhà phân tích phụ trách các ngành khác nhau. Thống kê kiểm định phù hợp là $t$ sử dụng ước lượng gộp của phương sai chung: 

![](assets/Quantitative_method.pdf-0239-03.png)

<!-- Formula Text: t  = ( _ X  1 − _ X  2 ) − (μ 1 − μ 2) ________________ √ _ s p 2 _ n 1  + s p 2 _ n 2 , where s p 2  = (n 1 − 1 ) s 1 2 + (n 2 − 1 ) s 2 2 _________________ n 1 + n 2 − 2 . The number of degrees of freedom is nA + nB − 2 = 10 +15 − 2 = 23. C.	 For df = 23, according to the table, the rejection point for a one-sided (right side) test at the 0.05 significance level is 1.714.i -->
$$t = \frac{(\bar{X}_1 - \bar{X}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{s_p^2}{n_1} + \frac{s_p^2}{n_2}}}, \quad \text{trong đó } s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$$
Số bậc tự do là $n_A + n_B - 2 = 10 + 15 - 2 = 23$.

- **C.** Với $df = 23$, theo bảng tra, điểm bác bỏ cho kiểm định một phía (phía bên phải) ở mức ý nghĩa $0.05$ là $1.714$.

![](assets/Quantitative_method.pdf-0239-04.png)

<!-- Formula Text: i D.	 We first calculate the pooled estimate of variance: s p 2  =   (10 − 1 ) 0.01 + (15 − 1 ) 0.0081 ______________________ 10 + 15 − 2 =  0.0088435. -->
- **D.** Trước tiên chúng ta tính ước lượng phương sai gộp:
$$s_p^2 = \frac{(10 - 1)0.01 + (15 - 1)0.0081}{10 + 15 - 2} = 0.0088435$$

Sau đó chúng ta tính thống kê kiểm định có phân phối $t$: 

![](assets/Quantitative_method.pdf-0239-06.png)

<!-- Formula Text: t  = (0.05 − 0.02 ) − 0 _________________ √ __________________ 0.0088435 _ 10 +  0.0088435 _ 15 = 0.03 _ 0.0383916   =  0.78142. -->
$$t = \frac{(0.05 - 0.02) - 0}{\sqrt{\frac{0.0088435}{10} + \frac{0.0088435}{15}}} = \frac{0.03}{0.0383916} = 0.78142$$

Bởi vì $0.78142 < 1.714$, chúng ta không bác bỏ giả thuyết không. Không có đủ bằng chứng để chỉ ra rằng giá trị trung bình của Nhà phân tích A vượt quá giá trị trung bình của Nhà phân tích B. 

Một nhà tư vấn đầu tư thu thập hai mẫu ngẫu nhiên độc lập về dữ liệu hiệu quả hoạt động 5 năm của các quỹ phòng hộ tỷ suất sinh lợi tuyệt đối (*absolute return hedge funds*) tại Hoa Kỳ và Châu Âu. Nhận thấy lợi thế tỷ suất sinh lợi $50\text{ bps}$ nghiêng về các nhà quản lý Hoa Kỳ, nhà tư vấn quyết định kiểm định xem liệu hai giá trị trung bình có khác nhau hay không ở mức ý nghĩa $0.05$. Hai tổng thể được giả định là có phân phối chuẩn với phương sai chưa biết nhưng bằng nhau. Kết quả của kiểm định giả thuyết được trình bày trong Minh họa 11. 

#### **Minh họa 11: Kết quả Kiểm định Giả thuyết (*Exhibit 11: Hypothesis Test Results*)** 

|**Nhóm / Chỉ tiêu**|**Kích thước Mẫu (*Sample Size*)**|**Tỷ suất sinh lợi Trung bình (*Mean Return*) (%)**|**Độ lệch chuẩn (*Standard Deviation*)**|
|---|---|---|---|
|Các nhà quản lý Hoa Kỳ (*US managers*)|50|4.7|5.4|
|Các nhà quản lý Châu Âu (*European managers*)|50|4.2|4.8|
|Giả thuyết không và giả thuyết đối (*Null and alternative hypotheses*)|$H_0: \mu_{\text{US}} - \mu_{\text{E}} = 0$;|$H_a: \mu_{\text{US}} - \mu_{\text{E}} \ne 0$||
|Thống kê kiểm định tính toán được (*Calculated test statistic*)|$0.4893$|||
|Các điểm bác bỏ giá trị tới hạn (*Critical value rejection points*)|$\pm 1.984$|||

_Lưu ý:_ Tỷ suất sinh lợi trung bình của các quỹ Hoa Kỳ là $\mu_{\text{US}}$, và $\mu_{\text{E}}$ là tỷ suất sinh lợi trung bình của các quỹ Châu Âu. 

3. Nhà tư vấn nên kết luận rằng: 

- **A.** giả thuyết không không bị bác bỏ (*null hypothesis is not rejected*). 
- **B.** giả thuyết đối được xác nhận có ý nghĩa thống kê. 


<!-- PDF Page 240 -->

- **C.** sự khác biệt trong tỷ suất sinh lợi trung bình là khác $0$ có ý nghĩa thống kê. 

###### **Lời giải (*Solution*):** 

A đúng. Giá trị thống kê $t$ tính toán được là $0.4893$ nằm trong giới hạn của các giá trị $t$ tới hạn là $\pm 1.984$. Do đó, không thể bác bỏ $H_0$; kết quả không có ý nghĩa thống kê ở mức $0.05$. 

4. Trong giai đoạn 10 năm, độ lệch chuẩn của tỷ suất sinh lợi hàng năm trên một danh mục đầu tư mà bạn đang phân tích là $15\%$ một năm. Bạn muốn xem liệu hồ sơ này có phải là bằng chứng đủ để ủng hộ kết luận rằng phương sai tỷ suất sinh lợi cơ sở của danh mục đầu tư nhỏ hơn $400$, tức phương sai tỷ suất sinh lợi của chỉ số chuẩn (*benchmark*) của danh mục đầu tư hay không. 

   - **A.** Thiết lập giả thuyết không và giả thuyết đối nhất quán với mục tiêu của bạn. 
   - **B.** Xác định thống kê kiểm định để tiến hành kiểm định các giả thuyết ở Phần A, và tính bậc tự do. 
   - **C.** Xác định xem giả thuyết không bị bác bỏ hay không bị bác bỏ ở mức ý nghĩa $0.05$ bằng cách sử dụng giá trị tới hạn là $3.325$. 

###### **Lời giải (*Solution*):** 

   - **A.** Chúng ta có một giả thuyết đối dạng “nhỏ hơn”, trong đó $\sigma^2$ là phương sai tỷ suất sinh lợi của danh mục đầu tư. Các giả thuyết là $H_0: \sigma^2 \ge 400$ đối lập với $H_a: \sigma^2 < 400$, trong đó $400$ là giá trị phương sai theo giả thuyết. Điều này có nghĩa là miền bác bỏ nằm ở phía bên trái của phân phối. 
   - **B.** Thống kê kiểm định có phân phối Khi-bình phương (*chi-square distributed*) với $10 - 1 = 9$ bậc tự do. 
   - **C.** Thống kê kiểm định được tính như sau: 

![](assets/Quantitative_method.pdf-0240-13.png)

<!-- Formula Text: χ 2  =   (n − 1) s 2 _ σ 0 2 =   9 × 15 2 _ 400    =   2, 025 _ 400    =  5.0625 ,  or  5.06. -->
$$\chi^2 = \frac{(n - 1)s^2}{\sigma_0^2} = \frac{9 \times 15^2}{400} = \frac{2,025}{400} = 5.0625, \text{ hay } 5.06$$

*(Lưu ý nguyên bản sách CFA và đính chính chuẩn xác)*: Văn bản gốc ghi "Bởi vì $5.06$ lớn hơn $3.325$, chúng ta bác bỏ giả thuyết không; thống kê kiểm định tính toán được rơi về phía bên phải của giá trị tới hạn, nơi giá trị tới hạn ngăn cách vùng phía bên trái với vùng chúng ta bác bỏ giả thuyết không." *(Đính chính toán học: Vì $H_a: \sigma^2 < 400$ là kiểm định đuôi trái với giá trị tới hạn đuôi trái $\chi^2_{0.05, 9} = 3.325$, miền bác bỏ là $\chi^2 < 3.325$. Vì $5.06 > 3.325$ và $p\text{-value} = 17.0953\% > 5\%$, kết luận chuẩn xác về mặt toán học là **không bác bỏ** $H_0$).* Chúng ta có thể xác định giá trị tới hạn cho kiểm định này bằng phần mềm: 

- **Excel:** `[CHISQ.INV(0.05,9)]` 
- **R:** `[qchisq(.05,9)]` 
- **Python:** `[from scipy.stats import chi2 and chi2.ppf(.05,9)]`

Chúng ta có thể xác định giá trị $p$ (*p-value*) cho thống kê kiểm định tính toán được là $17.0953\%$ bằng phần mềm: 

- **Excel:** `[CHISQ.DIST(5.06,9,TRUE)]` 
- **R:** `[pchisq(5.06,9,lower.tail=TRUE)]` 
- **Python:** `[from scipy.stats import chi2 and chi2.cdf(5.06,9)]` 


<!-- PDF Page 241 -->

5. Bạn đang khảo sát xem liệu phương sai tổng thể của tỷ suất sinh lợi trên một chỉ số có thay đổi sau một sự kiện gián đoạn thị trường (*market disruption*) hay không. Bạn thu thập dữ liệu sau đây cho 120 tháng tỷ suất sinh lợi trước khi gián đoạn và 120 tháng tỷ suất sinh lợi sau khi gián đoạn. Bạn đã chỉ định mức ý nghĩa là $0.05$. 

#### **Minh họa 12: Dữ liệu cho 120 Tháng Tỷ suất sinh lợi (*Exhibit 12: Data for 120 Months of Returns*)** 

|**Giai đoạn Thời gian (*Time Period*)**|**$N$**|**Tỷ suất sinh lợi Hàng tháng Trung bình (*Mean Monthly Return*) (%)**|**Phương sai của Tỷ suất sinh lợi (*Variance of Returns*)**|
|---|---|---|---|
|Trước gián đoạn (*Before disruption*)|120|1.416|22.367|
|Sau gián đoạn (*After disruption*)|120|1.436|15.795|

- **A.** Thiết lập giả thuyết không và giả thuyết đối nhất quán với mục tiêu nghiên cứu. 
- **B.** Xác định thống kê kiểm định để tiến hành kiểm định các giả thuyết ở Phần A, và tính bậc tự do. 
- **C.** Xác định xem có bác bỏ giả thuyết không ở mức ý nghĩa $0.05$ hay không nếu các giá trị tới hạn là $0.6969$ và $1.4349$. 

###### **Lời giải (*Solution*):**

- **A.** Chúng ta có một giả thuyết đối dạng “khác” (*not equal to*): 
  $$H_0: \sigma_{\text{Before}}^2 = \sigma_{\text{After}}^2 \text{ đối lập với } H_a: \sigma_{\text{Before}}^2 \ne \sigma_{\text{After}}^2$$
- **B.** Để kiểm định giả thuyết không về sự bằng nhau của hai phương sai, chúng ta sử dụng kiểm định $F$ (*F-test*): 
  $$F = \frac{s_1^2}{s_2^2}$$
  $$F = \frac{22.367}{15.795} = 1.416$$
  với $120 - 1 = 119$ bậc tự do ở tử số và $120 - 1 = 119$ bậc tự do ở mẫu số. 
- **C.** Bởi vì đây là kiểm định hai phía (*two-tailed test*), chúng ta sử dụng các giá trị tới hạn cho mức $0.05 / 2 = 0.025$. Thống kê kiểm định tính toán được nằm trong giới hạn của các giá trị tới hạn (tức là nằm giữa $0.6969$ và $1.4349$), vì vậy chúng ta không bác bỏ giả thuyết không; không có đủ bằng chứng để chỉ ra rằng phương sai là khác nhau trước và sau khi gián đoạn. Lưu ý rằng chúng ta cũng có thể lập thống kê $F$ dưới dạng $15.795 / 22.367 = 0.706$ và rút ra cùng một kết luận. 

Chúng ta cũng có thể sử dụng phần mềm để tính các giá trị tới hạn: 

- **Excel:** `[F.INV(0.025,119,119) and F.INV(0.975,119,119)]`
- **R:** `[qf(c(.025,.975),119,119)]`
- **Python:** `from scipy.stats import f and f.ppf[(.025,119,119) and f.ppf(.975,119,119)]` 


<!-- PDF Page 242 -->

Ngoài ra, chúng ta có thể sử dụng phần mềm để tính giá trị $p$ của thống kê kiểm định tính toán được, có kết quả là $5.896\%$, và sau đó so sánh nó với mức ý nghĩa: 

- **Excel:** `[(1-F.DIST(22.367/15.796,119,119,TRUE))*2 or F.DIST(15.796/22.367,119,119,TRUE)*2]`
- **R:** `[(1-pf(22.367/15.796,119,119))*2 or pf(15.796/22.367,119,119)*2]` 
- **Python:** `from scipy.stats import f and f.cdf[(15.796/22.367,119,119)*2 or (1-f.cdf(22.367/15.796,119,119))*2]` 

# **<mark>4</mark> KIỂM ĐỊNH THAM SỐ SO VỚI KIỂM ĐỊNH PHI THAM SỐ (*PARAMETRIC VERSUS NONPARAMETRIC TESTS*)** 

*So sánh và đối chiếu các kiểm định tham số và phi tham số, đồng thời mô tả các tình huống mà mỗi loại kiểm định là phù hợp hơn*

Các thủ tục kiểm định giả thuyết mà chúng ta đã thảo luận cho đến thời điểm này có hai đặc điểm chung. Thứ nhất, chúng liên quan đến các tham số (*parameters*), và thứ hai, tính hợp lệ của chúng phụ thuộc vào một tập hợp các giả định xác định. Ví dụ, giá trị trung bình và phương sai là hai tham số, hay hai đại lượng xác định, của một phân phối chuẩn. Các kiểm định này cũng đưa ra các giả định cụ thể—đặc biệt là các giả định về phân phối của tổng thể tạo ra mẫu. Bất kỳ kiểm định hoặc thủ tục nào có một trong hai đặc điểm này đều là **kiểm định tham số (*parametric test*)** hoặc thủ tục tham số. 

Tuy nhiên, trong một số trường hợp, chúng ta quan tâm đến các đại lượng khác ngoài các tham số của phân phối. Trong các trường hợp khác, chúng ta có thể tin rằng các giả định của kiểm định tham số không được thỏa mãn. Trong những trường hợp chúng ta đang xem xét các đại lượng khác ngoài tham số tổng thể hoặc nơi các giả định về tham số không được thỏa mãn, một kiểm định hoặc thủ tục phi tham số có thể rất hữu ích. 

**Kiểm định phi tham số (*nonparametric test*)** là một kiểm định không liên quan đến một tham số hoặc một kiểm định đưa ra các giả định tối thiểu về tổng thể mà từ đó mẫu được rút ra. Minh họa 13 trình bày các ví dụ về các phương pháp thay thế phi tham số cho các kiểm định tham số có phân phối $t$ liên quan đến giá trị trung bình. 

**Minh họa 13: Các Phương pháp Thay thế Phi tham số cho các Kiểm định Tham số Liên quan đến Giá trị Trung bình (*Exhibit 13: Nonparametric Alternatives to Parametric Tests Concerning Means*)** 

||**Tham số (*Parametric*)**|**Phi tham số (*Nonparametric*)**|
|---|---|---|
|Các kiểm định liên quan đến một giá trị trung bình đơn lẻ (*Tests concerning a single mean*)|Kiểm định phân phối $t$ (*t-distributed test*)<br>Kiểm định phân phối $z$ (*z-distributed test*)|Kiểm định thứ hạng có dấu Wilcoxon (*Wilcoxon signed-rank test*)|


<!-- PDF Page 243 -->

||**Tham số (*Parametric*)**|**Phi tham số (*Nonparametric*)**|
|---|---|---|
|Các kiểm định liên quan đến sự khác biệt giữa hai giá trị trung bình (*Tests concerning differences between means*)|Kiểm định phân phối $t$ (*t-distributed test*)|Kiểm định $U$ Mann–Whitney (*Mann–Whitney U test*)<br>(Kiểm định tổng thứ hạng Wilcoxon – *Wilcoxon rank sum test*)|
|Các kiểm định liên quan đến trung bình của các chênh lệch – kiểm định so sánh cặp (*Tests concerning mean differences – paired comparisons tests*)|Kiểm định phân phối $t$ (*t-distributed test*)|Kiểm định thứ hạng có dấu Wilcoxon (*Wilcoxon signed-rank test*)<br>Kiểm định dấu (*Sign test*)|

### **Ứng dụng của các Kiểm định Phi tham số (*Uses of Nonparametric Tests*)** 

Các thủ tục phi tham số chủ yếu được sử dụng trong bốn tình huống: (1) khi dữ liệu không đáp ứng các giả định về phân phối, (2) khi có các giá trị ngoại lai (*outliers*), (3) khi dữ liệu được cho dưới dạng thứ hạng (*ranks*) hoặc sử dụng thang đo thứ bậc (*ordinal scale*), hoặc (4) khi các giả thuyết có liên quan không đề cập đến một tham số. 

Tình huống thứ nhất xảy ra khi dữ liệu sẵn có để phân tích cho thấy rằng các giả định về phân phối của kiểm định tham số không được thỏa mãn. Ví dụ, chúng ta có thể muốn kiểm định một giả thuyết liên quan đến giá trị trung bình của một tổng thể nhưng tin rằng cả kiểm định phân phối $t$ lẫn phân phối $z$ đều không phù hợp bởi vì mẫu nhỏ và có thể đến từ một tổng thể có phân phối lệch chuẩn rõ rệt (*markedly non-normally distributed*). Trong trường hợp đó, chúng ta có thể sử dụng một kiểm định phi tham số. Kiểm định phi tham số sẽ thường xuyên bao gồm việc chuyển đổi các quan sát (hoặc một hàm của các quan sát) thành các thứ hạng (*ranks*) theo độ lớn, và đôi khi nó sẽ chỉ làm việc với các mối quan hệ “lớn hơn” hoặc “nhỏ hơn” (sử dụng các dấu $+$ và $-$ để biểu thị các mối quan hệ đó). Về mặt đặc trưng, người ta phải tham khảo các bảng thống kê chuyên biệt để xác định các điểm bác bỏ của thống kê kiểm định, ít nhất là đối với các mẫu nhỏ. Khi đó, các kiểm định như vậy thường diễn giải giả thuyết không thành một giả thuyết về thứ hạng hoặc dấu. 

Thứ hai, trong khi phân phối cơ sở của tổng thể có thể là chuẩn, có thể có các giá trị cực đoan hoặc giá trị ngoại lai (*outliers*) gây ảnh hưởng đến các thống kê tham số nhưng không ảnh hưởng đến các thống kê phi tham số. Ví dụ, chúng ta có thể muốn sử dụng một kiểm định phi tham số về trung vị (*median*), trong trường hợp có các giá trị ngoại lai, thay vì kiểm định về giá trị trung bình (*mean*). 

Thứ ba, chúng ta có thể có một mẫu trong đó các quan sát được xếp hạng (*ranked*). Trong những trường hợp đó, chúng ta cũng sử dụng các kiểm định phi tham số bởi vì các kiểm định tham số thường đòi hỏi một thang đo mạnh hơn thang đo thứ hạng. Ví dụ, nếu dữ liệu của chúng ta là bảng xếp hạng các nhà quản lý đầu tư, chúng ta sẽ sử dụng các thủ tục phi tham số để kiểm định các giả thuyết liên quan đến các bảng xếp hạng đó. 

Tình huống thứ tư mà chúng ta sử dụng các thủ tục phi tham số xảy ra khi câu hỏi của chúng ta không liên quan đến một tham số. Ví dụ, nếu câu hỏi liên quan đến việc liệu một mẫu có ngẫu nhiên hay không, chúng ta sử dụng kiểm định phi tham số phù hợp (kiểm định mạch – “*runs test*”). Kiểm định mạch phi tham số được sử dụng để kiểm định xem liệu các thay đổi giá cổ phiếu có thể được dùng để dự báo các thay đổi giá cổ phiếu trong tương lai hay không—nói cách khác, một kiểm định về lý thuyết bước đi ngẫu nhiên (*random walk theory*). Một loại câu hỏi khác mà các phương pháp phi tham số có thể giải quyết là liệu một mẫu có đến từ một tổng thể tuân theo một phân phối xác suất cụ thể nào đó hay không. 

### **Suy luận Phi tham số: Tóm tắt (*Nonparametric Inference: Summary*)** 

Các thủ tục thống kê phi tham số mở rộng phạm vi của suy luận bởi vì chúng đưa ra rất ít giả định, có thể được sử dụng trên dữ liệu xếp hạng, và có thể giải quyết các câu hỏi không liên quan đến tham số. Khá thường xuyên, các kiểm định phi tham số được báo cáo song song với các kiểm định tham số; khi đó người dùng có thể đánh giá mức độ nhạy cảm của kết luận thống kê đối với các giả định cơ sở của kiểm định tham số. Tuy nhiên, nếu các giả định của kiểm định tham số được đáp ứng, kiểm định tham số (khi có sẵn) nhìn chung được ưu tiên hơn so với kiểm định phi tham số bởi vì kiểm định tham số có thể có lực kiểm định lớn hơn (*more power*)—tức là khả năng lớn hơn trong việc bác bỏ một giả thuyết không đang sai. 
