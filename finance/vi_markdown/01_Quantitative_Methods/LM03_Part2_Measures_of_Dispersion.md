# Tập 1: Phương pháp Định lượng (*Quantitative Methods*)
## Học phần 3: Các thước đo Thống kê về Tỷ suất sinh lợi Tài sản (*Statistical Measures of Asset Returns*)
### Phần 2/4: Các thước đo Độ phân tán (*Measures of Dispersion*) (Trang PDF 108–117)

---

<!-- PDF Page 108 -->

**Bảng minh họa 10: Biểu đồ Hộp và Râu (*Box and Whisker Plot*)** 

![](assets/Quantitative_method.pdf-0108-04.png)

<!-- Picture Text: 180<br>160<br>154.45<br>140<br>120<br>114.25<br>100 100.49<br>80 79.74<br>60<br>51.51<br>40<br> -->

> **Chú thích hình ảnh:**
> - **Giá trị cao nhất (râu trên):** 154.45
> - **Cận trên của hộp ($Q_3$):** 114.25
> - **Đường giữa hộp (Trung vị):** 100.49
> - **Cận dưới của hộp ($Q_1$):** 79.74
> - **Giá trị thấp nhất (râu dưới):** 51.51

8. Trung vị (*median*) _gần nhất_ với: 

   - **A.** 34.51. 

   - **B.** 100.49. 

   - **C.** 102.98. 

   - **Lời giải:** 

B là đáp án đúng. Trong biểu đồ hộp và râu, phần “hộp” đại diện cho cận dưới của tứ phân vị thứ hai và cận trên của tứ phân vị thứ ba, với trung vị hoặc trung bình cộng được đánh dấu như một thước đo xu hướng trung tâm của toàn bộ phân phối. Trung vị được biểu thị bên trong hộp, có giá trị là 100.49. 

9. Khoảng tứ phân vị (*interquartile range*) _gần nhất_ với: 

   - **A.** 13.76. 

   - **B.** 25.74. 

   - **C.** 34.51. 

   - **Lời giải:** 

C là đáp án đúng. Khoảng tứ phân vị là chiều cao của hộp, tức là chênh lệch giữa 114.25 và 79.74, bằng 34.51 ($114.25 - 79.74 = 34.51$). 

# **<mark>3</mark>** 

## **CÁC THƯỚC ĐO ĐỘ PHÂN TÁN (*MEASURES OF DISPERSION*)** 

tính toán, diễn giải và đánh giá các thước đo độ phân tán để giải quyết một bài toán đầu tư 

Ít ai có thể phủ nhận tầm quan trọng của tỷ suất sinh lợi kỳ vọng hay tỷ suất sinh lợi trung bình trong đầu tư: Tuy nhiên, để hiểu đầy đủ hơn về một khoản đầu tư, chúng ta cũng cần biết tỷ suất sinh lợi phân tán như thế nào xung quanh giá trị trung bình. **Độ phân tán (*Dispersion*)** là mức độ biến thiên xung quanh xu hướng trung tâm. Nếu tỷ suất sinh lợi trung bình đề cập đến phần thưởng (*reward*), thì độ phân tán đề cập đến rủi ro và sự không chắc chắn (*risk and uncertainty*). 


<!-- PDF Page 109 -->

Trong bài học này, chúng ta xem xét các thước đo độ phân tán phổ biến nhất: khoảng biến thiên (*range*), độ lệch tuyệt đối trung bình (*mean absolute deviation*), phương sai (*variance*), và độ lệch chuẩn (*standard deviation*). Đây đều là các thước đo **độ phân tán tuyệt đối (*absolute dispersion*)**. Độ phân tán tuyệt đối là mức độ biến thiên hiện có mà không so sánh với bất kỳ điểm tham chiếu hay chuẩn so sánh (*benchmark*) nào. 

### **Khoảng biến thiên (*The Range*)** 

Chúng ta đã bắt gặp khoảng biến thiên trước đó khi thảo luận về việc xây dựng các phân phối tần số. Đây là thước đo đơn giản nhất trong tất cả các thước đo độ phân tán. 

**Định nghĩa Khoảng biến thiên (*Definition of Range*).** **Khoảng biến thiên (*range*)** là chênh lệch giữa giá trị lớn nhất và giá trị nhỏ nhất trong một tập dữ liệu: 

$$\text{Range} = \text{Giá trị lớn nhất} - \text{Giá trị nhỏ nhất} \tag{2}$$

Một cách khác để báo cáo khoảng biến thiên là chỉ rõ cả giá trị lớn nhất và giá trị nhỏ nhất. Định nghĩa thay thế này cung cấp nhiều thông tin hơn khi khoảng biến thiên được báo cáo là “từ Giá trị Lớn nhất đến Giá trị Nhỏ nhất”. 

Một ưu điểm của khoảng biến thiên là dễ tính toán. Nhược điểm là khoảng biến thiên chỉ sử dụng hai mẩu thông tin từ phân phối. Nó không thể cho chúng ta biết dữ liệu được phân phối như thế nào (tức là hình dạng của phân phối). Bởi vì khoảng biến thiên là chênh lệch giữa giá trị lớn nhất và giá trị nhỏ nhất trong tập dữ liệu, nên nó cũng nhạy cảm với các quan sát cực lớn hoặc cực nhỏ (“các giá trị ngoại lai” – *“outliers”*) vốn có thể không đại diện cho phân phối đó. 

### **Độ lệch Tuyệt đối Trung bình (*Mean Absolute Deviations*)** 

Các thước đo độ phân tán có thể được tính bằng cách sử dụng tất cả các quan sát trong phân phối thay vì chỉ giá trị cao nhất và thấp nhất. Chúng ta có thể tính các thước đo độ phân tán bằng trung bình cộng của các độ lệch xung quanh giá trị trung bình, nhưng vấn đề là tổng các độ lệch xung quanh giá trị trung bình luôn bằng 0. Do đó, chúng ta cần tìm một cách để giải quyết vấn đề các độ lệch âm triệt tiêu các độ lệch dương. 

Một giải pháp là xem xét các độ lệch tuyệt đối xung quanh giá trị trung bình như trong **độ lệch tuyệt đối trung bình (*mean absolute deviation* – MAD)**. 

**Công thức MAD (*MAD Formula*).** MAD của một mẫu là: 

![](assets/Quantitative_method.pdf-0109-14.png)

<!-- Formula Text: MAD  = ∑ i=1 n |X i − _ X | _ n , (3) -->

$$\text{MAD} = \frac{\sum_{i=1}^{n} |X_i - \bar{X}|}{n} \tag{3}$$

trong đó $\bar{X}$ là trung bình mẫu, $n$ là số lượng quan sát trong mẫu, và ký hiệu $| \ |$ biểu thị giá trị tuyệt đối của biểu thức nằm bên trong hai vạch thẳng này. 

MAD sử dụng tất cả các quan sát trong mẫu và do đó ưu việt hơn khoảng biến thiên khi làm thước đo độ phân tán. Một nhược điểm kỹ thuật của MAD là nó khó thao tác về mặt toán học so với thước đo tiếp theo mà chúng ta sẽ giới thiệu, đó là phương sai mẫu (*sample variance*). 

### **Phương sai Mẫu và Độ lệch chuẩn Mẫu (*Sample Variance and Sample Standard Deviation*)** 

Cách tiếp cận thứ hai cho vấn đề các độ lệch dương và âm triệt tiêu lẫn nhau là bình phương chúng lên. Phương sai và độ lệch chuẩn, vốn dựa trên các độ lệch bình phương, là hai thước đo độ phân tán được sử dụng rộng rãi nhất. **Phương sai (*Variance*)** được định nghĩa là trung bình của các bình phương độ lệch xung quanh giá trị trung bình. **Độ lệch chuẩn (*Standard deviation*)** là căn bậc hai dương của phương sai. 


<!-- PDF Page 110 -->

#### **_Phương sai Mẫu (*Sample Variance*)_** 

Trong đầu tư, chúng ta thường không biết giá trị trung bình của một tổng thể (*population*) đang quan tâm, vì vậy chúng ta ước lượng nó bằng cách sử dụng giá trị trung bình từ một mẫu được rút ra từ tổng thể đó. Thước đo độ phân tán tương ứng là phương sai mẫu hoặc độ lệch chuẩn mẫu. 

**Công thức Phương sai Mẫu (*Sample Variance Formula*).** **Phương sai mẫu (*sample variance*)**, $s^2$, là: 

![](assets/Quantitative_method.pdf-0110-06.png)

<!-- Formula Text: s 2  = ∑ i=1 n (X i − _ X ) 2 ___________ n − 1 , (4) -->

$$s^2 = \frac{\sum_{i=1}^{n} (X_i - \bar{X})^2}{n - 1} \tag{4}$$

trong đó $\bar{X}$ là trung bình mẫu và $n$ là số lượng quan sát trong mẫu. 

Cách tính phương sai giải quyết được vấn đề các độ lệch âm so với giá trị trung bình triệt tiêu các độ lệch dương bằng cách bình phương các độ lệch đó. 

Đối với phương sai mẫu, bằng cách chia cho kích thước mẫu trừ đi 1 (tức $n - 1$) thay vì $n$, chúng ta cải thiện được các đặc tính thống kê của phương sai mẫu. Đại lượng $n - 1$ còn được gọi là số bậc tự do (*degrees of freedom*) trong việc ước lượng phương sai tổng thể. Để ước lượng phương sai tổng thể bằng $s^2$, trước tiên chúng ta phải tính trung bình mẫu, vốn bản thân nó đã là một tham số ước lượng. Do đó, một khi chúng ta đã tính được trung bình mẫu, chỉ còn lại $n - 1$ mẩu thông tin độc lập từ mẫu; nghĩa là, nếu bạn biết trung bình mẫu và $n - 1$ quan sát, bạn có thể tính được quan sát mẫu còn thiếu. 

#### **_Độ lệch chuẩn Mẫu (*Sample Standard Deviation*)_** 

Phương sai được đo bằng đơn vị bình phương gắn với giá trị trung bình, và chúng ta cần một cách để quay trở lại các đơn vị ban đầu đó. Độ lệch chuẩn, căn bậc hai của phương sai, giải quyết được vấn đề này và dễ diễn giải hơn so với phương sai. 

Một đặc tính hữu ích của độ lệch chuẩn mẫu là, không giống như phương sai mẫu, nó được biểu thị bằng cùng đơn vị với chính dữ liệu đó. Nếu tập dữ liệu là tỷ lệ phần trăm tỷ suất sinh lợi hàng ngày của một chỉ số, thì cả giá trị trung bình và độ lệch chuẩn của tập dữ liệu đều tính theo phần trăm, trong khi phương sai tính theo phần trăm bình phương của tỷ suất sinh lợi hàng ngày. 

**Công thức Độ lệch chuẩn Mẫu (*Sample Standard Deviation Formula*).** **Độ lệch chuẩn mẫu (*sample standard deviation*)**, $s$, là: 

![](assets/Quantitative_method.pdf-0110-14.png)

<!-- Formula Text: s  =  √ ____________ ∑ i=1 n (X i − _ X ) 2 ___________ n − 1 , (5) -->

$$s = \sqrt{\frac{\sum_{i=1}^{n} (X_i - \bar{X})^2}{n - 1}} \tag{5}$$

trong đó $\bar{X}$ là trung bình mẫu và $n$ là số lượng quan sát trong mẫu. 

Bởi vì độ lệch chuẩn là thước đo độ phân tán xung quanh trung bình cộng, chúng ta thường trình bày trung bình cộng và độ lệch chuẩn cùng nhau khi tóm tắt dữ liệu. Khi chúng ta xử lý dữ liệu đại diện cho một chuỗi thời gian của các thay đổi phần trăm, việc trình bày thêm trung bình nhân (*geometric mean* – tức đại diện cho tốc độ tăng trưởng kép) cũng rất hữu ích. 

### **Độ lệch Dưới và Hệ số Biến thiên (*Downside Deviation and Coefficient of Variation*)** 

Phương sai hoặc độ lệch chuẩn của tỷ suất sinh lợi của một tài sản thường được diễn giải là thước đo rủi ro của tài sản đó. Phương sai và độ lệch chuẩn của tỷ suất sinh lợi tính đến cả các mức tỷ suất sinh lợi nằm trên và nằm dưới giá trị trung bình, tương ứng là rủi ro phía trên (*upside risk*) và rủi ro phía dưới (*downside risk*). Tuy nhiên, 


<!-- PDF Page 111 -->

các nhà đầu tư thường chỉ quan tâm đến **rủi ro phía dưới (*downside risk*)**—ví dụ, các mức tỷ suất sinh lợi thấp hơn giá trị trung bình hoặc thấp hơn một mức tỷ suất sinh lợi mục tiêu tối thiểu xác định nào đó. Do đó, các chuyên viên phân tích đã phát triển các thước đo rủi ro phía dưới. 

#### **_Độ lệch Dưới (*Downside Deviation*)_** 

Trong thực tế, chúng ta có thể quan tâm đến các giá trị tỷ suất sinh lợi (hoặc một biến số khác) thấp hơn một mức nào đó không phải là giá trị trung bình. Ví dụ, nếu mục tiêu tỷ suất sinh lợi của chúng ta là 6.0 phần trăm mỗi năm (mức tỷ suất sinh lợi tối thiểu có thể chấp nhận được của chúng ta), thì chúng ta có thể đặc biệt quan tâm đến các mức tỷ suất sinh lợi dưới 6.0 phần trăm một năm. Độ lệch dưới mục tiêu (*target downside deviation*), còn được gọi là **bán độ lệch mục tiêu (*target semideviation*)**, là thước đo độ phân tán của các quan sát (ở đây là tỷ suất sinh lợi) nằm dưới một mức mục tiêu—ví dụ 6.0 phần trăm. Để tính bán độ lệch mục tiêu mẫu, trước tiên chúng ta xác định mức mục tiêu. Sau khi xác định các quan sát nằm dưới mức mục tiêu, chúng ta tìm tổng các bình phương độ lệch âm đó so với mục tiêu, chia tổng đó cho tổng số quan sát trong mẫu trừ đi 1 ($n - 1$), và cuối cùng lấy căn bậc hai. 

**Công thức Bán độ lệch Mục tiêu Mẫu (*Sample Target Semideviation Formula*).** Bán độ lệch mục tiêu, $s_{\text{Target}}$, là: 

![](assets/Quantitative_method.pdf-0111-07.png)

<!-- Formula Text: S Target    =  √ _________________ ∑ for allX i≤B n (X i − B) 2 _ n − 1   , (6) -->

$$s_{\text{Target}} = \sqrt{\frac{\sum_{\text{với mọi } X_i \le B}^{n} (X_i - B)^2}{n - 1}} \tag{6}$$

trong đó $B$ là mức mục tiêu (*target*) và $n$ là tổng số quan sát trong mẫu. Chúng ta minh họa điều này trong Ví dụ 3. 

#### **VÍ DỤ 3** 

### **Tính Độ lệch Dưới Mục tiêu (*Calculating Target Downside Deviation*)** 

Hãy xem xét tỷ suất sinh lợi hàng tháng của một danh mục đầu tư như được thể hiện trong Bảng minh họa 11: 

**Bảng minh họa 11: Tỷ suất sinh lợi Hàng tháng của Danh mục đầu tư (*Monthly Portfolio Returns*)** 

|**Tháng (*Month*)**|**Tỷ suất sinh lợi (*Return*) (%)**|
|---|---|
|Tháng Một|5|
|Tháng Hai|3|
|Tháng Ba|−1|
|Tháng Tư|−4|
|Tháng Năm|4|
|Tháng Sáu|2|
|Tháng Bảy|0|
|Tháng Tám|4|
|Tháng Chín|3|
|Tháng Mười|0|
|Tháng Mười Một|6|
|Tháng Mười Hai|5|

1. Tính độ lệch dưới mục tiêu khi tỷ suất sinh lợi mục tiêu là 3 phần trăm. 

#### **Lời giải:** 


<!-- PDF Page 112 -->

|**Tháng (*Month*)**|**Quan sát (*Observation*)**|**Độ lệch so với mục tiêu 3% (*Deviation from the 3% Target*)**|**Độ lệch dưới mục tiêu (*Deviations below the Target*)**|**Bình phương độ lệch dưới mục tiêu (*Squared Deviations below the Target*)**|
|---|---|---|---|---|
|Tháng Một|5|2|—|—|
|Tháng Hai|3|0|—|—|
|Tháng Ba|−1|−4|−4|16|
|Tháng Tư|−4|−7|−7|49|
|Tháng Năm|4|1|—|—|
|Tháng Sáu|2|−1|−1|1|
|Tháng Bảy|0|−3|−3|9|
|Tháng Tám|4|1|—|—|
|Tháng Chín|3|0|—|—|
|Tháng Mười|0|−3|−3|9|
|Tháng Mười Một|6|3|—|—|
|Tháng Mười Hai|5|2|—|—|
|**Tổng (*Sum*)**||||**84**|

$$\textbf{Bán độ lệch mục tiêu (Target semideviation)} = \sqrt{\frac{84}{12 - 1}} = 2.7634\%$$

2. Nếu tỷ suất sinh lợi mục tiêu là 4 phần trăm, câu trả lời của bạn có khác với câu trả lời cho câu hỏi 1 không? Không sử dụng phép tính, hãy giải thích nó sẽ khác như thế nào? 

#### **Lời giải:** 

Nếu tỷ suất sinh lợi mục tiêu cao hơn, thì các độ lệch hiện có sẽ lớn hơn và sẽ có thêm một số giá trị nằm trong cột độ lệch và bình phương độ lệch dưới mục tiêu; do đó, bán độ lệch mục tiêu sẽ lớn hơn. 

Độ lệch dưới mục tiêu liên hệ như thế nào với độ lệch chuẩn mẫu? Chúng ta minh họa sự khác biệt giữa độ lệch dưới mục tiêu và độ lệch chuẩn trong Ví dụ 4, sử dụng dữ liệu trong Ví dụ 3. 

#### **VÍ DỤ 4** 

### **So sánh Độ lệch Dưới Mục tiêu với Độ lệch chuẩn (*Comparing the Target Downside Deviation with the Standard Deviation*)** 

1. Cho dữ liệu trong Ví dụ 3, hãy tính độ lệch chuẩn mẫu. 

#### **Lời giải:** 

|**Tháng (*Month*)**|**Quan sát (*Observation*)**|**Độ lệch so với giá trị trung bình (*Deviation from the Mean*)**|**Bình phương độ lệch (*Squared Deviation*)**|
|---|---|---|---|
|Tháng Một|5|2.75|7.5625|
|Tháng Hai|3|0.75|0.5625|
|Tháng Ba|−1|−3.25|10.5625|
|Tháng Tư|−4|−6.25|39.0625|
|Tháng Năm|4|1.75|3.0625|
|Tháng Sáu|2|−0.25|0.0625|


<!-- PDF Page 113 -->

|**Tháng (*Month*)**|**Quan sát (*Observation*)**|**Độ lệch so với giá trị trung bình (*Deviation from the Mean*)**|**Bình phương độ lệch (*Squared Deviation*)**|
|---|---|---|---|
|Tháng Bảy|0|−2.25|5.0625|
|Tháng Tám|4|1.75|3.0625|
|Tháng Chín|3|0.75|0.5625|
|Tháng Mười|0|−2.25|5.0625|
|Tháng Mười Một|6|3.75|14.0625|
|Tháng Mười Hai|5|2.75|7.5625|
|**Tổng (*Sum*)**|27||**96.2500**|

Độ lệch chuẩn mẫu là $\sqrt{\frac{96.2500}{11}} = 2.958\%$. 

2. Cho dữ liệu trong Ví dụ 3, hãy tính độ lệch dưới mục tiêu nếu mức mục tiêu là 2 phần trăm. 

#### **Lời giải:** 

|**Tháng (*Month*)**|**Quan sát (*Observation*)**|**Độ lệch so với mục tiêu 2% (*Deviation from the 2% Target*)**|**Độ lệch dưới mục tiêu (*Deviations below the Target*)**|**Bình phương độ lệch dưới mục tiêu (*Squared Deviations below the Target*)**|
|---|---|---|---|---|
|Tháng Một|5|3|—|—|
|Tháng Hai|3|1|—|—|
|Tháng Ba|−1|−3|−3|9|
|Tháng Tư|−4|−6|−6|36|
|Tháng Năm|4|2|—|—|
|Tháng Sáu|2|0|—|—|
|Tháng Bảy|0|−2|−2|4|
|Tháng Tám|4|2|—|—|
|Tháng Chín|3|1|—|—|
|Tháng Mười|0|−2|−2|4|
|Tháng Mười Một|6|4|—|—|
|Tháng Mười Hai|5|3|—|—|
|**Tổng (*Sum*)**||||**53**|

Bán độ lệch mục tiêu với mức mục tiêu 2 phần trăm $= \sqrt{\frac{53}{11}} = 2.195\%$. 

3. So sánh độ lệch chuẩn, độ lệch dưới mục tiêu nếu mức mục tiêu là 2 phần trăm, và độ lệch dưới mục tiêu nếu mức mục tiêu là 3 phần trăm. 

#### **Lời giải:** 

Độ lệch chuẩn dựa trên độ lệch so với giá trị trung bình, tức là $27\% / 12 = 2.25\%$. Độ lệch chuẩn bao gồm tất cả các độ lệch so với giá trị trung bình, chứ không chỉ những độ lệch nằm dưới nó. Điều này dẫn đến độ lệch chuẩn mẫu là 2.958 phần trăm. 

Khi chỉ xét bốn quan sát nằm dưới mức mục tiêu 2 phần trăm, bán độ lệch mục tiêu là 2.195 phần trăm. Giá trị này nhỏ hơn độ lệch chuẩn mẫu vì bán độ lệch mục tiêu chỉ nắm bắt rủi ro phía dưới (tức là các độ lệch dưới mục tiêu). Khi xét bán độ lệch mục tiêu với mức mục tiêu 3 phần trăm, 


<!-- PDF Page 114 -->

hiện có năm quan sát nằm dưới mức 3 phần trăm, vì vậy bán độ lệch mục tiêu cao hơn, ở mức 2.763 phần trăm. 


#### **_Hệ số Biến thiên (*Coefficient of Variation*)_** 

Trước đó chúng ta đã lưu ý rằng độ lệch chuẩn dễ diễn giải hơn phương sai vì độ lệch chuẩn sử dụng cùng đơn vị đo lường với các quan sát. Tuy nhiên, đôi khi chúng ta có thể thấy khó diễn giải ý nghĩa của độ lệch chuẩn xét về mức độ biến thiên tương đối của các tập dữ liệu khác nhau, hoặc bởi vì các tập dữ liệu có giá trị trung bình khác biệt rõ rệt hoặc bởi vì các tập dữ liệu có đơn vị đo lường khác nhau. Trong phần này, chúng ta giải thích một thước đo độ phân tán tương đối, đó là hệ số biến thiên, vốn có thể hữu ích trong những tình huống như vậy. **Độ phân tán tương đối (*Relative dispersion*)** là mức độ phân tán so với một giá trị tham chiếu hoặc chuẩn so sánh (*benchmark*). 

Hệ số biến thiên rất hữu ích trong các tình huống như vừa mô tả (tức là các tập dữ liệu có giá trị trung bình khác biệt rõ rệt hoặc đơn vị đo lường khác nhau). 

**Công thức Hệ số Biến thiên (*Coefficient of Variation Formula*).** **Hệ số biến thiên (*coefficient of variation* – CV)** là tỷ số giữa độ lệch chuẩn của một tập hợp các quan sát với giá trị trung bình của chúng: 

![](assets/Quantitative_method.pdf-0114-09.png)

<!-- Formula Text: CV  =   s _ _ X  , -->

![](assets/Quantitative_method.pdf-0114-10.png)

<!-- Formula Text: (7) -->

$$\text{CV} = \frac{s}{\bar{X}} \tag{7}$$

trong đó $s$ là độ lệch chuẩn mẫu và $\bar{X}$ là trung bình mẫu. 

Ví dụ, khi các quan sát là tỷ suất sinh lợi, CV đo lường lượng rủi ro (độ lệch chuẩn) trên mỗi đơn vị phần thưởng (tỷ suất sinh lợi trung bình). Một vấn đề có thể phát sinh, đặc biệt khi xử lý tỷ suất sinh lợi, là nếu $\bar{X}$ âm thì con số thống kê này trở nên vô nghĩa. 

CV có thể được biểu thị dưới dạng bội số (ví dụ: hai lần) hoặc dưới dạng phần trăm (ví dụ: 200 phần trăm). Bằng cách biểu thị độ lớn của sự biến thiên giữa các quan sát tương ứng với quy mô trung bình của chúng, CV cho phép so sánh trực tiếp độ phân tán giữa các tập dữ liệu khác nhau. Phản ánh việc điều chỉnh theo quy mô, CV là một thước đo không phụ thuộc vào quy mô (*scale-free measure*, tức là nó không có đơn vị đo lường). 

Chúng ta minh họa tính hữu ích của CV trong việc so sánh các tập dữ liệu có độ lệch chuẩn khác biệt rõ rệt bằng cách sử dụng hai mẫu công ty giả định trong Ví dụ 5. 

#### **VÍ DỤ 5** 

### **Hệ số Biến thiên của Tỷ suất sinh lợi trên Tài sản (*Coefficient of Variation of Returns on Assets*)** 

Giả sử một chuyên viên phân tích thu thập tỷ suất sinh lợi trên tài sản (ROA), tính theo phần trăm, của 10 công ty cho mỗi ngành trong hai ngành: 

**Bảng minh họa 12: Tỷ suất sinh lợi trên Tài sản của Hai Ngành (*Returns on Assets for Two Industries*)** 

|**Công ty (*Company*)**|**Ngành A (*Industry A*)**|**Ngành B (*Industry B*)**|
|---|---|---|
|1|−5|−10|
|2|−3|−9|
|3|−1|−7|
|4|2|−3|
|5|4|1|
|6|6|3|
|7|7|5|
|8|9|18|


<!-- PDF Page 115 -->

|**Công ty (*Company*)**|**Ngành A (*Industry A*)**|**Ngành B (*Industry B*)**|
|---|---|---|
|9|10|20|
|10|11|22|

Dữ liệu này có thể được biểu diễn bằng đồ thị như trong Bảng minh họa 13: 

#### **Bảng minh họa 13: Tỷ suất sinh lợi trên Tài sản được Biểu diễn bằng Đồ thị (*Returns on Assets Depicted Graphically*)** 

![](assets/Quantitative_method.pdf-0115-06.png)

<!-- Picture Text: Industry A<br>–5 –3 –1 2 4 6 7 9 10 11<br>Industry B<br>–10–9 –7 –3 1 3 5 18 20 22<br> -->

> **Chú thích hình ảnh:**
> - **Industry A (Ngành A):** Các quan sát phân bố từ –5 đến 11 (–5, –3, –1, 2, 4, 6, 7, 9, 10, 11).
> - **Industry B (Ngành B):** Các quan sát phân bố rộng hơn từ –10 đến 22 (–10, –9, –7, –3, 1, 3, 5, 18, 20, 22).

1. Tính ROA trung bình cho mỗi ngành. 

#### **Lời giải:** 

ROA trung bình cộng của cả hai ngành là tổng của 10 quan sát, trong cả hai trường hợp đều bằng 40, chia cho 10 quan sát, hay $40 / 10 = 4\%$. 

2. Tính độ lệch chuẩn của ROA cho mỗi ngành. 

#### **Lời giải:** 

Sử dụng Phương trình 5, độ lệch chuẩn đối với Ngành A là 5.60 và đối với Ngành B là 12.12. 

3. Tính hệ số biến thiên (CV) của ROA cho mỗi ngành. 

#### **Lời giải:** 

Sử dụng Phương trình 7, CV của Ngành A $= 5.60 / 4 = 1.40$ và CV của Ngành B $= 12.12 / 4 = 3.03$. 

Mặc dù hai ngành có cùng mức ROA trung bình cộng, nhưng độ phân tán lại rất khác nhau—với tỷ suất sinh lợi trên tài sản của Ngành B phân tán rộng hơn nhiều so với Ngành A. Hệ số CV của hai ngành này phản ánh điều đó, với Ngành B có CV lớn hơn. Cách diễn giải ở đây là rủi ro trên mỗi đơn vị tỷ suất sinh lợi trung bình của Ngành B lớn hơn gấp đôi ($2.16 = 3.03 / 1.40$) so với Ngành A. 

#### **BỘ CÂU HỎI (*QUESTION SET*)** 

Hãy xem xét tổng tỷ suất sinh lợi hàng năm của Chỉ số Thế giới MSCI (MSCI World Index) trong giai đoạn 10 năm, như được thể hiện trong Bảng minh họa 14: 


<!-- PDF Page 116 -->

#### **Bảng minh họa 14: Tổng Tỷ suất sinh lợi của Chỉ số Thế giới MSCI (*MSCI World Index Total Returns*)** 

|Năm 1|15.25%|Năm 6|30.79%|
|---|---|---|---|
|Năm 2|10.02%|Năm 7|12.34%|
|Năm 3|20.65%|Năm 8|−5.02%|
|Năm 4|9.57%|Năm 9|16.54%|
|Năm 5|−40.33%|Năm 10|27.37%|

1. Đối với giai đoạn từ Năm 6 đến Năm 10, độ lệch tuyệt đối trung bình (MAD) của tổng tỷ suất sinh lợi Chỉ số Thế giới MSCI _gần nhất_ với: 

   - **A.** 10.20 phần trăm. 

   - **B.** 12.74 phần trăm. 

   - **C.** 16.40 phần trăm. 

   - **Lời giải:** 

A là đáp án đúng. MAD được tính như sau: 

Bước 1 Cộng các mức tỷ suất sinh lợi hàng năm và chia cho $n$ để tìm trung bình cộng ($\bar{X}$) là 16.40 phần trăm. 

![](assets/Quantitative_method.pdf-0116-12.png)

<!-- Formula Text: Step 2	 Calculate the absolute value of the difference between each year’s return and the mean from Step 1. Sum the results and divide by n to find the MAD: MAD  = ∑ i=1 n |X i − _ X | _ n , -->

Bước 2 Tính giá trị tuyệt đối của chênh lệch giữa tỷ suất sinh lợi mỗi năm và giá trị trung bình từ Bước 1. Cộng các kết quả lại và chia cho $n$ để tìm MAD:

$$\text{MAD} = \frac{\sum_{i=1}^{n} |X_i - \bar{X}|}{n}$$

$$\text{MAD} = \frac{50.98\%}{5} = 10.20\%$$

Các phép tính này được trình bày trong bảng sau: 

||**Bước 1 (*Step 1*)**|**Bước 2 (*Step 2*)**|
|---|---|---|
|**Năm (*Year*)**|**Tỷ suất sinh lợi (*Return*)**|**$|X_i - \bar{X}|$**|
|Năm 6|30.79%|14.39%|
|Năm 7|12.34%|4.06%|
|Năm 8|−5.02%|21.42%|
|Năm 9|16.54%|0.14%|
|Năm 10|27.37%|10.97%|
|Tổng (*Sum*):|82.02%|50.98%|
|$n$:|5|5|
|$\bar{X}$:|16.40%|10.20%|

Tỷ suất sinh lợi hàng năm và các thống kê tóm tắt cho ba quỹ đầu tư được liệt kê như sau: 

||**Tỷ suất sinh lợi hàng năm (*Annual Returns*) (%)**|||
|---|---|---|---|
|**Năm (*Year*)**|**Quỹ ABC**|**Quỹ XYZ**|**Quỹ PQR**|
|Năm 1|−20.0|−33.0|−14.0|
|Năm 2|23.0|−12.0|−18.0|
|Năm 3|−14.0|−12.0|6.0|


<!-- PDF Page 117 -->

||**Tỷ suất sinh lợi hàng năm (*Annual Returns*) (%)**|||
|---|---|---|---|
|**Năm (*Year*)**|**Quỹ ABC**|**Quỹ XYZ**|**Quỹ PQR**|
|Năm 4|5.0|−8.0|−2.0|
|Năm 5|−14.0|11.0|3.0|
|Giá trị trung bình (*Mean*)|−4.0|−10.8|−5.0|
|Độ lệch chuẩn (*Standard deviation*)|17.8|15.6|10.5|

2. Quỹ có độ lệch tuyệt đối trung bình (MAD) cao nhất là Quỹ: 

   - **A.** ABC. 

   - **B.** XYZ. 

   - **C.** PQR. 

   - **Lời giải:** 

A là đáp án đúng. MAD của tỷ suất sinh lợi Quỹ ABC là cao nhất trong số ba quỹ. Sử dụng Phương trình 3, MAD cho mỗi quỹ được tính như sau: 

MAD của Quỹ ABC = 

![](assets/Quantitative_method.pdf-0117-11.png)

<!-- Formula Text: |  − 20 − (− 4) |+| 23 − (− 4) |+|  − 14 − (− 4) |+| 5 − (− 4) |+|  − 14 − (− 4) | ________________________________________________ 5 =  14.4%. -->

$$\text{MAD}_{\text{ABC}} = \frac{|-20 - (-4)| + |23 - (-4)| + |-14 - (-4)| + |5 - (-4)| + |-14 - (-4)|}{5} = 14.4\%$$

MAD của Quỹ XYZ = 

$$\text{MAD}_{\text{XYZ}} = \frac{|-33 - (-10.8)| + |-12 - (-10.8)| + |-12 - (-10.8)| + |-8 - (-10.8)| + |11 - (-10.8)|}{5} = 9.8\%$$

MAD của Quỹ PQR = 

$$\text{MAD}_{\text{PQR}} = \frac{|-14 - (-5)| + |-18 - (-5)| + |6 - (-5)| + |-2 - (-5)| + |3 - (-5)|}{5} = 8.8\%$$

3. Hãy xem xét các số liệu thống kê trong Bảng minh họa 15 cho Danh mục A và Danh mục B trong 12 tháng qua: 

#### **Bảng minh họa 15: Các Thống kê của Danh mục A và Danh mục B (*Portfolio A and Portfolio B Statistics*)** 

||**Danh mục A (*Portfolio A*)**|**Danh mục B (*Portfolio B*)**|
|---|---|---|
|Tỷ suất sinh lợi trung bình (*Average Return*)|3%|3%|
|Tỷ suất sinh lợi trung bình nhân (*Geometric Return*)|2.85%|?|
|Độ lệch chuẩn (*Standard Deviation*)|4%|6%|

4. Tỷ suất sinh lợi trung bình nhân (*geometric mean return*) của Danh mục B _có khả năng cao nhất_ sẽ: 

   - **A.** nhỏ hơn 2.85 phần trăm. 

   - **B.** bằng 2.85 phần trăm. 
