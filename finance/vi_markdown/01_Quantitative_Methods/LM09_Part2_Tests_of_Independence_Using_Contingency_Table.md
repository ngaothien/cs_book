# Tập 1: Phương pháp Định lượng (*Quantitative Methods*)
## Học phần 9: Các Kiểm định Tính Độc lập Tham số và Phi tham số (*Parametric and Non-Parametric Tests of Independence*)
### Phần 2/2: Các Kiểm định Tính Độc lập Sử dụng Dữ liệu Bảng Tiếp liên (*Tests of Independence Using Contingency Table Data*) (Trang PDF 261–270)

---

<!-- PDF Page 261 -->

*(Tiếp theo Lời giải Câu 2 của Bộ Câu hỏi cuối Phần 1:)*

|**Quỹ Tương hỗ (*Mutual Fund*)**|**Alpha**|**Tỷ lệ Chi phí (*Expense Ratio*)**|**Thứ hạng theo Alpha (*Rank by Alpha*)**|**Thứ hạng theo Tỷ lệ Chi phí (*Rank by Expense Ratio*)**|**Chênh lệch Thứ hạng (*Difference in Rank*)**|**Bình phương Chênh lệch (*Difference Squared*)**|
|---|---|---|---|---|---|---|
|1|−0.52|1.34|6|6|0|0|
|2|−0.13|0.40|1|9|−8|64|
|3|−0.50|1.90|5|1|4|16|
|4|−1.01|1.50|9|2.5|6.5|42.25|
|5|−0.26|1.35|3|5|−2|4|
|6|−0.89|0.50|8|8|0|0|
|7|−0.42|1.00|4|7|−3|9|
|8|−0.23|1.50|2|2.5|−0.5|0.25|
|9|−0.60|1.45|7|4|3|9|
||||||**Tổng (*Sum*)**|144.5|

$$r_S = 1 - \frac{6(144.5)}{9(80)} = -0.20417$$

3. Xác định xem có bác bỏ giả thuyết không ở mức ý nghĩa $0.05$ hay không nếu các giá trị tới hạn là $\pm 2.306$. 

###### **Lời giải (*Solution*):**

Thống kê kiểm định tính toán được, sử dụng thống kê kiểm định có phân phối $t$:

$$t = \frac{r\sqrt{n - 2}}{\sqrt{1 - r^2}} \quad \text{là} \quad t = \frac{-0.20417\sqrt{7}}{\sqrt{1 - 0.041681}} = \frac{-0.540183}{0.978937} = -0.55181$$

Dựa trên việc giá trị này nằm trong phạm vi $\pm 2.306$, chúng ta không bác bỏ giả thuyết không rằng hệ số tương quan hạng Spearman bằng $0$. 

### **CÁC KIỂM ĐỊNH TÍNH ĐỘC LẬP SỬ DỤNG DỮ LIỆU BẢNG TIẾP LIÊN (*TESTS OF INDEPENDENCE USING CONTINGENCY TABLE DATA*)** 

# **<mark>3</mark>** 

*Giải thích các kiểm định tính độc lập dựa trên dữ liệu bảng tiếp liên*

Khi đối mặt với dữ liệu phân loại (*categorical data*) hoặc dữ liệu rời rạc (*discrete data*), chúng ta không thể sử dụng các phương pháp đã thảo luận cho đến thời điểm này để kiểm định xem các phân loại của dữ liệu đó có độc lập với nhau hay không. Giả sử chúng ta quan sát **bảng tần số (*frequency table*)** sau đây của 1,594 quỹ hoán đổi danh mục (*exchange-traded funds* – ETFs) dựa trên hai phân loại: quy mô (tức giá trị vốn hóa thị trường) và loại hình đầu tư (giá trị, tăng trưởng hoặc hỗn hợp – *value, growth, or blend*), như được hiển thị trong Minh họa 7. Phân loại loại hình đầu tư là rời rạc, vì vậy chúng ta không thể sử dụng hệ số tương quan để đánh giá mối quan hệ giữa quy mô và loại hình đầu tư. 


<!-- PDF Page 262 -->

**Minh họa 7: Phân loại Quy mô và Loại hình Đầu tư của 1,594 Quỹ ETF (*Exhibit 7: Size and Investment Type Classifications of 1,594 ETFs*)** 

|**Loại hình Đầu tư (*Investment Type*)**|**Quy mô theo Vốn hóa Thị trường: Nhỏ (*Small*)**|**Quy mô theo Vốn hóa Thị trường: Vừa (*Medium*)**|**Quy mô theo Vốn hóa Thị trường: Lớn (*Large*)**|**Tổng (*Total*)**|
|---|---|---|---|---|
|Giá trị (*Value*)|50|110|343|503|
|Tăng trưởng (*Growth*)|42|122|202|366|
|Hỗn hợp (*Blend*)|56|149|520|725|
|Tổng (*Total*)|148|381|1,065|1,594|

Minh họa 7 được gọi là **bảng tiếp liên (*contingency table*)** hoặc **bảng hai chiều (*two-way table*)** (bởi vì có hai phân loại, hoặc hai lớp—quy mô và loại hình đầu tư). 

Nếu chúng ta muốn kiểm định xem liệu có tồn tại mối quan hệ giữa quy mô và loại hình đầu tư hay không, chúng ta có thể thực hiện một kiểm định tính độc lập bằng cách sử dụng một thống kê kiểm định phi tham số có phân phối Khi-bình phương (*chi-square distributed*): 

![](assets/Quantitative_method.pdf-0262-06.png)

<!-- Formula Text: χ 2  =  ∑ i=1 m (O ij − E ij) 2 _ E ij , (4) -->
$$\chi^2 = \sum_{i=1}^{m} \frac{(O_{ij} - E_{ij})^2}{E_{ij}} \tag{4}$$

trong đó: 

- $m =$ số lượng ô (*cells*) trong bảng, bằng số nhóm trong phân loại thứ nhất nhân với số nhóm trong phân loại thứ hai; 
- $O_{ij} =$ số lượng quan sát trong mỗi ô ở hàng $i$ và cột $j$ (tức là tần số quan sát được – *observed frequency*); và 
- $E_{ij} =$ số lượng quan sát kỳ vọng trong mỗi ô ở hàng $i$ và cột $j$, giả định tính độc lập (tức là tần số kỳ vọng – *expected frequency*). 

Thống kê kiểm định này có $(r - 1)(c - 1)$ bậc tự do, trong đó $r$ là số hàng và $c$ là số cột. 

Trong Minh họa 7, lớp quy mô có ba nhóm (nhỏ, vừa và lớn) và lớp loại hình đầu tư có ba nhóm (giá trị, tăng trưởng và hỗn hợp), vì vậy $m$ bằng $9$ ($= 3 \times 3$). Số lượng quỹ ETF trong mỗi ô ($O_{ij}$), tức tần số quan sát được, đã được cho trước, vì vậy để tính thống kê kiểm định Khi-bình phương, chúng ta cần ước tính $E_{ij}$, tần số kỳ vọng, tức là số lượng quỹ ETF mà chúng ta kỳ vọng sẽ có trong mỗi ô nếu quy mô và loại hình đầu tư hoàn toàn độc lập với nhau. Số lượng quỹ ETF kỳ vọng ($E_{ij}$) được tính bằng công thức sau: 

![](assets/Quantitative_method.pdf-0262-13.png)

<!-- Formula Text: E ij  = (Total row i ) × (Total column j) ______________________ Overall total . (5) -->
$$E_{ij} = \frac{(\text{Tổng hàng } i) \times (\text{Tổng cột } j)}{\text{Tổng chung toàn bảng}} \tag{5}$$

Hãy xem xét một sự kết hợp giữa quy mô và loại hình đầu tư, nhóm giá trị vốn hóa nhỏ (*small-cap value*): 

![](assets/Quantitative_method.pdf-0262-15.png)

<!-- Formula Text: E ij  =   503 × 148 _ 1, 594    =  46.703. -->
$$E_{ij} = \frac{503 \times 148}{1,594} = 46.703$$

Chúng ta lặp lại phép tính này cho từng sự kết hợp giữa quy mô và loại hình đầu tư (tức là $m = 9$ cặp) để thu được các tần số kỳ vọng, được trình bày trong Bảng A của Minh họa 8. Tiếp theo, chúng ta tính: 

![](assets/Quantitative_method.pdf-0262-17.png)

<!-- Formula Text: (O ij − E ij) 2 _ E ij , -->
$$\frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

tức bình phương chênh lệch giữa tần số quan sát được và tần số kỳ vọng được chuẩn hóa theo tần số kỳ vọng, cho mỗi ô như được hiển thị trong Bảng B của Minh họa 8. Cuối cùng, bằng cách cộng tổng các giá trị của: 

![](assets/Quantitative_method.pdf-0262-19.png)

<!-- Formula Text: (O ij − E ij) 2 _ E ij -->
$$\frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$


<!-- PDF Page 263 -->

cho mỗi ô trong số $m$ ô, chúng ta tính được thống kê Khi-bình phương là $32.08025$. 

##### **Minh họa 8: Các Đầu vào cho Phép tính Thống kê Kiểm định Khi-bình phương cho 1,594 Quỹ ETF Giả định Tính Độc lập giữa Quy mô và Loại hình Đầu tư (*Exhibit 8: Inputs to Chi-Square Test Statistic Calculation for 1,594 ETFs Assuming Independence of Size and Investment Type*)** 

###### **A. Tần số Kỳ vọng của các Quỹ ETF theo Quy mô và Loại hình Đầu tư (*Expected Frequency of ETFs by Size and Investment Type*)** 

|**Loại hình Đầu tư (*Investment Type*)**|**Quy mô theo Vốn hóa: Nhỏ (*Small*)**|**Quy mô theo Vốn hóa: Vừa (*Medium*)**|**Quy mô theo Vốn hóa: Lớn (*Large*)**|
|---|---|---|---|
|Giá trị (*Value*)|46.703|120.228|336.070|
|Tăng trưởng (*Growth*)|33.982|87.482|244.536|
|Hỗn hợp (*Blend*)|67.315|173.290|484.395|
|Tổng (*Total*)|148.000|381.000|1,065.000|

###### **B. Độ lệch Bình phương Chuẩn hóa cho Mỗi Sự kết hợp giữa Quy mô và Loại hình Đầu tư (*Scaled Squared Deviation for Each Combination of Size and Investment Type*)** 

|**Loại hình Đầu tư (*Investment Type*)**|**Quy mô theo Vốn hóa: Nhỏ (*Small*)**|**Quy mô theo Vốn hóa: Vừa (*Medium*)**|**Quy mô theo Vốn hóa: Lớn (*Large*)**|
|---|---|---|---|
|Giá trị (*Value*)|0.233|0.870|0.143|
|Tăng trưởng (*Growth*)|1.892|13.620|7.399|
|Hỗn hợp (*Blend*)|1.902|3.405|2.617|

Trong ví dụ về quỹ ETF của chúng ta, chúng ta kiểm định giả thuyết không về tính độc lập giữa hai lớp (tức là không có mối quan hệ giữa quy mô và loại hình đầu tư) đối lập với giả thuyết đối về sự phụ thuộc (tức là có mối quan hệ giữa quy mô và loại hình đầu tư) bằng cách sử dụng mức ý nghĩa $5\%$, như được hiển thị trong Minh họa 9. Nếu các giá trị quan sát được bằng với các giá trị kỳ vọng, thống kê kiểm định tính toán được sẽ bằng $0$. Tuy nhiên, nếu các giá trị quan sát được và kỳ vọng khác nhau, những chênh lệch này được bình phương lên, vì vậy thống kê Khi-bình phương tính toán được sẽ mang giá trị dương. Do đó, đối với kiểm định tính độc lập sử dụng bảng tiếp liên, chỉ có duy nhất một miền bác bỏ nằm ở phía bên phải (*right side*). 

**Minh họa 9: Kiểm định Tính Độc lập của Quy mô và Loại hình Đầu tư cho 1,594 Quỹ ETF (*Exhibit 9: Test of Independence of Size and Investment Type for 1,594 ETFs*)** 

|**Bước 1 (*Step 1*)**|Phát biểu các giả thuyết.|$H_0$: Quy mô ETF và loại hình đầu tư không có liên hệ với nhau, vì vậy các phân loại này độc lập với nhau; $H_a$: Quy mô ETF và loại hình đầu tư có liên hệ với nhau, vì vậy các phân loại này không độc lập với nhau.|
|---|---|---|
|**Bước 2 (*Step 2*)**|Xác định thống kê kiểm định phù hợp.|$$\chi^2 = \sum_{i=1}^{m} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$|
|**Bước 3 (*Step 3*)**|Xác định mức ý nghĩa.|$5\%$|


<!-- PDF Page 264 -->

|**Bước 4 (*Step 4*)**|Phát biểu quy tắc quyết định.|Với $(3 - 1) \times (3 - 1) = 4$ bậc tự do và kiểm định một phía với mức ý nghĩa $5\%$, giá trị tới hạn là $9.4877$.<br>Chúng ta bác bỏ giả thuyết không nếu thống kê $\chi^2$ tính toán được lớn hơn $9.4877$.<br>**Excel:** `CHISQ.INV(0.95,4)`<br>**R:** `qchisq(.95,4)`<br>**Python:** `from scipy.stats import chi2` / `chi2.ppf(.95,4)`|
|---|---|---|
|**Bước 5 (*Step 5*)**|Tính toán thống kê kiểm định.|$$\chi^2 = 32.08025$$|
|**Bước 6 (*Step 6*)**|Đưa ra quyết định.|Bác bỏ giả thuyết không về tính độc lập bởi vì thống kê kiểm định $\chi^2$ tính toán được lớn hơn $9.4877$. Có đủ bằng chứng để kết luận rằng quy mô ETF và loại hình đầu tư có liên hệ với nhau (tức là không độc lập).|

Chúng ta có thể trực quan hóa bảng tiếp liên trong một đồ họa được gọi là biểu đồ khảm (*mosaic*). Trong biểu đồ khảm, một lưới các ô phản ánh sự so sánh giữa tần số quan sát được và tần số kỳ vọng. Hãy xem xét Minh họa 10, biểu diễn bảng tiếp liên của quỹ ETF. 

**Minh họa 10: Biểu đồ Khảm của Bảng Tiếp liên ETF (*Exhibit 10: Mosaic of the ETF Contingency Table*)** 

![](assets/Quantitative_method.pdf-0264-07.png)

<!-- Picture Text: Small Medium Large<br>Size<br>4><br>2 to 4<br>Value<br>0 to 2<br>–2 to 0<br>Growth<br>Investment Type<br>–4- to –2<br>–4<<br>Blend<br>Standardized Residuals:<br> -->
> **Chú thích hình ảnh:** Biểu đồ khảm (*Mosaic plot*) chia theo Quy mô (*Size*: *Small, Medium, Large*) và Loại hình đầu tư (*Investment Type*: *Value, Growth, Blend*) cùng thang màu của Phần dư chuẩn hóa (*Standardized Residuals* từ $<-4$ đến $>4$).

Chiều rộng của các hình chữ nhật trong Minh họa 10 phản ánh tỷ trọng của các quỹ ETF có quy mô nhỏ, vừa và lớn, trong khi chiều cao phản ánh tỷ trọng thuộc nhóm giá trị, tăng trưởng và hỗn hợp. Độ tô bóng đậm hơn cho biết số lượng quan sát nhiều hơn mức kỳ vọng dưới giả thuyết không về tính độc lập, trong khi độ tô bóng nhạt hơn cho biết số lượng quan sát ít hơn mức kỳ vọng, với mức “nhiều hơn” và “ít hơn” được xác định bằng cách tham chiếu đến các ô phần dư chuẩn hóa (*standardized residuals*). Phần dư chuẩn hóa, còn được gọi là phần dư Pearson (*Pearson residual*), được tính như sau: 

![](assets/Quantitative_method.pdf-0264-09.png)

<!-- Formula Text: Standardized residual  = O ij − E ij _ √ _ E ij   . -->
$$\text{Phần dư chuẩn hóa (Standardized residual)} = \frac{O_{ij} - E_{ij}}{\sqrt{E_{ij}}}$$


<!-- PDF Page 265 -->

Cách diễn giải cho ví dụ ETF này là có nhiều quỹ ETF tăng trưởng quy mô vừa hơn (phần dư chuẩn hóa là $3.69$) và ít quỹ ETF tăng trưởng quy mô lớn hơn (phần dư chuẩn hóa là $-2.72$) so với mức được kỳ vọng nếu quy mô và loại hình đầu tư độc lập với nhau. 

##### **VÍ DỤ 4 (*EXAMPLE 4*)** 

#### **Sử dụng Bảng Tiếp liên để Kiểm định Tính Độc lập (*Using Contingency Tables to Test for Independence*)** 

Hãy xem xét bảng tiếp liên trong Minh họa 11, phân loại 500 công ty được chọn ngẫu nhiên trên cơ sở hai chiều kích xếp hạng môi trường, xã hội và quản trị (ESG): xếp hạng môi trường (*environmental rating*) và xếp hạng quản trị (*governance rating*). 

**Minh họa 11: Phân loại 500 Công ty Được Chọn Ngẫu nhiên Dựa trên Xếp hạng Môi trường và Quản trị (*Exhibit 11: Classification of 500 Randomly Selected Companies Based on Environmental and Governance Ratings*)** 

|**Xếp hạng Môi trường (*Environmental Rating*)**|**Xếp hạng Quản trị: Tiến bộ (*Progressive*)**|**Xếp hạng Quản trị: Trung bình (*Average*)**|**Xếp hạng Quản trị: Kém (*Poor*)**|**Tổng (*Total*)**|
|---|---|---|---|---|
|Tiến bộ (*Progressive*)|35|40|5|80|
|Trung bình (*Average*)|80|130|50|260|
|Kém (*Poor*)|40|60|60|160|
|Tổng (*Total*)|155|230|115|500|

1. Các tần số kỳ vọng cho hai chiều kích xếp hạng ESG này là bao nhiêu nếu các danh mục này độc lập với nhau? 

##### **Lời giải (*Solution*):** 

Các tần số kỳ vọng dựa trên tính độc lập của xếp hạng quản trị và xếp hạng môi trường được hiển thị trong Bảng A của Minh họa 12. Ví dụ, sử dụng Phương trình 5, tần số kỳ vọng cho sự kết hợp giữa xếp hạng quản trị tiến bộ và xếp hạng môi trường tiến bộ là: 

![](assets/Quantitative_method.pdf-0265-12.png)

<!-- Formula Text: E ij  =   155 × 80 _ 500    =  24.80. -->
$$E_{ij} = \frac{155 \times 80}{500} = 24.80$$

Các độ lệch bình phương chuẩn hóa (*scaled squared deviations*) cho mỗi sự kết hợp giữa xếp hạng môi trường và quản trị được hiển thị trong Bảng B của Minh họa 12. Ví dụ, sử dụng Phương trình 4, độ lệch bình phương chuẩn hóa cho sự kết hợp giữa xếp hạng quản trị tiến bộ và xếp hạng môi trường tiến bộ như sau: 

![](assets/Quantitative_method.pdf-0265-14.png)

<!-- Formula Text: =  (35 − 24.8) 2 _ 24.8 =  4.195. -->
$$\frac{(35 - 24.8)^2}{24.8} = 4.195$$


<!-- PDF Page 266 -->

##### **Minh họa 12: Các Đầu vào cho Phép tính Thống kê Kiểm định Khi-bình phương Giả định Tính Độc lập của Xếp hạng Môi trường và Quản trị (*Exhibit 12: Inputs to Chi-Square Test Statistic Calculation Assuming Independence of Environmental and Governance Ratings*)** 

**A. Tần số Kỳ vọng của Xếp hạng Môi trường và Quản trị Giả định Tính Độc lập (*Expected Frequencies of Environmental and Governance Ratings Assuming Independence*)** 

|**Xếp hạng Môi trường (*Environmental Rating*)**|**Xếp hạng Quản trị: Tiến bộ (*Progressive*)**|**Xếp hạng Quản trị: Trung bình (*Average*)**|**Xếp hạng Quản trị: Kém (*Poor*)**|
|---|---|---|---|
|Tiến bộ (*Progressive*)|24.8|36.8|18.4|
|Trung bình (*Average*)|80.6|119.6|59.8|
|Kém (*Poor*)|49.6|73.6|36.8|

**B. Độ lệch Bình phương Chuẩn hóa cho Mỗi Sự kết hợp giữa Xếp hạng Môi trường và Quản trị (*Scaled Squared Deviation for Each Combination of Environmental and Governance Ratings*)** 

|**Xếp hạng Môi trường (*Environmental Rating*)**|**Xếp hạng Quản trị: Tiến bộ (*Progressive*)**|**Xếp hạng Quản trị: Trung bình (*Average*)**|**Xếp hạng Quản trị: Kém (*Poor*)**|
|---|---|---|---|
|Tiến bộ (*Progressive*)|4.195|0.278|9.759|
|Trung bình (*Average*)|0.004|0.904|1.606|
|Kém (*Poor*)|1.858|2.513|14.626|

2. Sử dụng mức ý nghĩa $5\%$, hãy xác định xem hai chiều kích xếp hạng ESG này có độc lập với nhau hay không. 

##### **Lời giải (*Solution*):** 

|**Bước 1 (*Step 1*)**|Phát biểu các giả thuyết.|$H_0$: Xếp hạng quản trị và môi trường không có liên hệ với nhau, vì vậy các xếp hạng này độc lập với nhau;<br>$H_a$: Xếp hạng quản trị và môi trường có liên hệ với nhau, vì vậy các xếp hạng này không độc lập với nhau.|
|---|---|---|
|**Bước 2 (*Step 2*)**|Xác định thống kê kiểm định phù hợp.|$$\chi^2 = \sum_{i=1}^{m} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$|
|**Bước 3 (*Step 3*)**|Xác định mức ý nghĩa.|$5\%$|
|**Bước 4 (*Step 4*)**|Phát biểu quy tắc quyết định.|Với $(3 - 1) \times (3 - 1) = 4$ bậc tự do và kiểm định một phía với mức ý nghĩa $5\%$, giá trị tới hạn là $9.487729$.<br>Chúng ta bác bỏ giả thuyết không nếu thống kê $\chi^2$ tính toán được lớn hơn $9.487729$.<br>**Excel:** `CHISQ.INV(0.95,4)`<br>**R:** `qchisq(.95,4)`<br>**Python:** `from scipy.stats import chi2` / `chi2.ppf(.95,4)`|


<!-- PDF Page 267 -->

|**Bước 5 (*Step 5*)**|Tính toán thống kê kiểm định.|$\chi^2 = 35.74415$<br>Để tính thống kê kiểm định, trước tiên chúng ta tính bình phương chênh lệch giữa tần số quan sát được và tần số kỳ vọng được chuẩn hóa theo tần số kỳ vọng cho mỗi ô, như được hiển thị trong Bảng B của Minh họa 12. Sau đó, cộng tổng các giá trị trong mỗi ô của $m$ ô (xem Phương trình 4), chúng ta tính được thống kê Khi-bình phương là $35.74415$.|
|---|---|---|
|**Bước 6 (*Step 6*)**|Đưa ra quyết định.|Bác bỏ giả thuyết không bởi vì thống kê kiểm định $\chi^2$ tính toán được lớn hơn $9.487729$. Có đủ bằng chứng để chỉ ra rằng xếp hạng môi trường và quản trị có liên hệ với nhau, vì vậy chúng không độc lập với nhau.|

##### **BỘ CÂU HỎI (*QUESTION SET*)** 

Một nhóm phân tích theo dõi 250 công ty và phân loại chúng theo hai chiều kích. Thứ nhất, họ sử dụng lịch sử chi trả cổ tức và dự báo thu nhập để phân loại các công ty vào một trong ba nhóm, với nhóm 1 biểu thị các ngôi sao cổ tức (*dividend stars*) và nhóm 3 biểu thị các công ty tụt hậu về cổ tức (*dividend laggards*). Thứ hai, họ phân loại các công ty trên cơ sở đòn bẩy tài chính (*financial leverage*), sử dụng các tỷ số nợ, đặc điểm khoản nợ và quản trị doanh nghiệp để phân loại các công ty thành ba nhóm, với nhóm 1 biểu thị các công ty ít rủi ro nhất dựa trên đòn bẩy tài chính và nhóm 3 biểu thị các công ty rủi ro nhất. Phân loại của 250 công ty như sau: 

|**Nhóm Đòn bẩy Tài chính (*Financial Leverage Group*)**|**Nhóm Cổ tức (*Dividend Group*): 1**|**Nhóm Cổ tức (*Dividend Group*): 2**|**Nhóm Cổ tức (*Dividend Group*): 3**|
|---|---|---|---|
|1|40|40|40|
|2|30|10|20|
|3|10|50|10|

Sử dụng bảng phân loại của 250 công ty này, hãy trả lời các câu hỏi sau: 

1. Giả thuyết không và giả thuyết đối để kiểm định xem các nhóm cổ tức và nhóm đòn bẩy tài chính có độc lập với nhau hay không là gì? 

###### **Lời giải (*Solution*):** 

Các giả thuyết như sau: 

- $H_0$: Xếp hạng cổ tức và đòn bẩy tài chính không có liên hệ với nhau, vì vậy các cách phân nhóm này độc lập với nhau. 
- $H_a$: Xếp hạng cổ tức và đòn bẩy tài chính có liên hệ với nhau, vì vậy các cách phân nhóm này không độc lập với nhau. 

2. Thống kê kiểm định phù hợp để sử dụng trong loại kiểm định này là gì?

###### **Lời giải (*Solution*):** 

Thống kê kiểm định phù hợp là: 


<!-- PDF Page 268 -->

![](assets/Quantitative_method.pdf-0268-03.png)

<!-- Formula Text: χ 2  =  ∑ i=1 m (O ij − E ij) 2 _ E ij , -->
$$\chi^2 = \sum_{i=1}^{m} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

trong đó $O_{ij}$ đại diện cho tần số quan sát được đối với nhóm $i$ và $j$, còn $E_{ij}$ đại diện cho tần số kỳ vọng đối với nhóm $i$ và $j$ nếu các cách phân nhóm là độc lập với nhau. 

Các tần số kỳ vọng dựa trên tính độc lập như sau: 

|**Nhóm Đòn bẩy Tài chính (*Financial Leverage Group*)**|**Nhóm Cổ tức: 1**|**Nhóm Cổ tức: 2**|**Nhóm Cổ tức: 3**|**Tổng (*Sum*)**|
|---|---|---|---|---|
|1|38.4|48|33.6|120|
|2|19.2|24|16.8|60|
|3|22.4|28|19.6|70|
|Tổng (*Sum*)|80|100|70|250|

Các độ lệch bình phương chuẩn hóa cho mỗi sự kết hợp giữa nhóm đòn bẩy tài chính và nhóm cổ tức là: 

|**Nhóm Đòn bẩy Tài chính (*Financial Leverage Group*)**|**Nhóm Cổ tức: 1**|**Nhóm Cổ tức: 2**|**Nhóm Cổ tức: 3**|
|---|---|---|---|
|1|0.06667|1.33333|1.21905|
|2|6.07500|8.16667|0.60952|
|3|6.86429|17.28571|4.70204|

3. Nếu giá trị tới hạn cho mức ý nghĩa $0.05$ là $9.4877$, kết luận của bạn là gì? 

##### **Lời giải (*Solution*):** 

Tổng của các độ lệch bình phương chuẩn hóa này là thống kê Khi-bình phương tính toán được bằng $46.3223$. Bởi vì giá trị tính toán được này vượt quá giá trị tới hạn là $9.4877$, chúng ta bác bỏ giả thuyết không rằng các cách phân nhóm này độc lập với nhau. 


<!-- PDF Page 269 -->

## **BÀI TẬP THỰC HÀNH (*PRACTICE PROBLEMS*)** 

**1.** Jill Batten đang phân tích xem tỷ suất sinh lợi trên cổ phiếu của Stellar Energy Corp. có liên hệ như thế nào với thay đổi phần trăm của tháng trước đó trong Chỉ số Giá Tiêu dùng Hoa Kỳ ngành Năng lượng (CPIENG). Dựa trên 248 quan sát, cô đã tính được tương quan mẫu giữa hai biến Stellar và CPIENG là $-0.1452$. Cô cũng muốn xác định xem liệu tương quan mẫu có khác $0$ một cách có ý nghĩa thống kê hay không. Giá trị tới hạn cho thống kê kiểm định ở mức ý nghĩa $0.05$ là xấp xỉ $1.96$. Batten nên kết luận rằng mối quan hệ thống kê giữa Stellar và CPIENG là: 

   - **A.** có ý nghĩa thống kê, bởi vì thống kê kiểm định tính toán được nằm ngoài giới hạn của các giá trị tới hạn cho thống kê kiểm định. 
   - **B.** có ý nghĩa thống kê, bởi vì thống kê kiểm định tính toán được có giá trị tuyệt đối thấp hơn giá trị tới hạn cho thống kê kiểm định. 
   - **C.** không có ý nghĩa thống kê, bởi vì thống kê kiểm định tính toán được nằm ngoài giới hạn của các giá trị tới hạn cho thống kê kiểm định. 

**2.** Phát biểu nào sau đây là đúng liên quan đến kiểm định Khi-bình phương về tính độc lập (*chi-square test of independence*)? 

   - **A.** Kiểm định có miền bác bỏ một phía (*one-sided rejection region*). 
   - **B.** Giả thuyết không là hai nhóm phụ thuộc lẫn nhau. 
   - **C.** Nếu có hai danh mục, mỗi danh mục có ba mức độ hoặc nhóm, thì có sáu bậc tự do. 


<!-- PDF Page 270 -->

## **LỜI GIẢI (*SOLUTIONS*)** 

1. **A đúng.** Thống kê kiểm định tính toán được là: 

![](assets/Quantitative_method.pdf-0270-04.png)

<!-- Formula Text: t  =   r √ _ n − 2 _ √ _ 1 − r 2 =  − 0.1452 √ _ 248 − 2 _____________ √ _____________ 1 − (− 0.1452) 2    =  − 2.30177. -->
$$t = \frac{r\sqrt{n - 2}}{\sqrt{1 - r^2}} = \frac{-0.1452\sqrt{248 - 2}}{\sqrt{1 - (-0.1452)^2}} = -2.30177$$

Bởi vì giá trị của $t = -2.30177$ nằm ngoài giới hạn của $\pm 1.96$, chúng ta bác bỏ giả thuyết không về việc không có tương quan và kết luận rằng có đủ bằng chứng để chỉ ra rằng tương quan là khác $0$. 

2. **A đúng.** Thống kê kiểm định bao gồm bình phương các chênh lệch giữa giá trị quan sát được và giá trị kỳ vọng, vì vậy kiểm định chỉ bao gồm một phía là phía bên phải (*right side*). B sai bởi vì giả thuyết không là các nhóm độc lập với nhau, và C sai bởi vì với ba mức độ nhóm cho hai biến phân loại, có $(3 - 1)(3 - 1) = 4$ bậc tự do. 
