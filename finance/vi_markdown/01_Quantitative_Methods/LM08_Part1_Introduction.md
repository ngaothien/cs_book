# Tập 1: Phương pháp Định lượng (*Quantitative Methods*)
## Học phần 8: Kiểm định Giả thuyết (*Hypothesis Testing*)
### Phần 1/3: Giới thiệu (*Introduction*) (Trang PDF 223–229)

---

<!-- PDF Page 223 -->

#### H Ọ C P H Ầ N 

# **<mark>8</mark>** 

### **Kiểm định Giả thuyết (*Hypothesis Testing*)** 

**tác giả: Pamela Peterson Drake, PhD, CFA.** 

_Pamela Peterson Drake, PhD, CFA, làm việc tại Đại học James Madison (Hoa Kỳ)._ 

###### **<mark>MỤC TIÊU HỌC TẬP (*LEARNING OUTCOMES*)</mark>** 

|**_Mức độ Thành thạo_**|**_Ứng viên cần có khả năng:_**|
|---|---|
||Giải thích kiểm định giả thuyết (*hypothesis testing*) và các cấu phần của nó, bao gồm ý nghĩa thống kê (*statistical significance*), sai lầm Loại I và Loại II (*Type I and Type II errors*), và lực kiểm định (*power of a test*).|
||Xây dựng các kiểm định giả thuyết và xác định ý nghĩa thống kê của chúng, các sai lầm Loại I và Loại II liên quan, cũng như lực kiểm định khi biết trước một mức ý nghĩa (*significance level*).|
||So sánh và đối chiếu các kiểm định tham số (*parametric tests*) và phi tham số (*nonparametric tests*), đồng thời mô tả các tình huống mà mỗi loại kiểm định là phù hợp hơn.|

![](assets/Quantitative_method.pdf-0223-08.png)

<!-- Picture Text: 1<br> -->

##### **GIỚI THIỆU (*INTRODUCTION*)** 

Kiểm định giả thuyết (*hypothesis testing*) đã được trình bày chi tiết trong phần tài liệu đọc trước (*pre-read*). Học phần này phát triển dựa trên nội dung đó và giả định rằng người học đã có sự hiểu biết thực hành về chủ đề này từ tài liệu đó hoặc từ nguồn khác. 

Bài 1 tóm tắt quy trình kiểm định giả thuyết thông qua các ví dụ về việc sử dụng nó trong tài chính và quản lý đầu tư. Bài 2 làm rõ tác động của các sai lầm trong quy trình kiểm định giả thuyết. Bài 3 giới thiệu các kiểm định phi tham số (*nonparametric tests*) và ứng dụng của chúng trong quản lý đầu tư. 

###### **TỔNG QUAN HỌC PHẦN (*LEARNING MODULE OVERVIEW*)** 

- Các bước trong việc kiểm định một giả thuyết như sau:
   **1.** Phát biểu các giả thuyết (*State the hypotheses*).
   **2.** Xác định thống kê kiểm định phù hợp và phân phối xác suất của nó (*Identify the appropriate test statistic and its probability distribution*). 
   **3.** Xác định mức ý nghĩa (*Specify the significance level*). 
   **4.** Phát biểu quy tắc quyết định (*State the decision rule*).
   **5.** Thu thập dữ liệu và tính toán thống kê kiểm định (*Collect the data and calculate the test statistic*). 


<!-- PDF Page 224 -->

   **6.** Đưa ra quyết định (*Make a decision*). 

- Thống kê kiểm định (*test statistic*) là một đại lượng được tính toán bằng cách sử dụng một mẫu, có giá trị làm cơ sở để quyết định bác bỏ hay không bác bỏ giả thuyết không (*null hypothesis*). Chúng ta so sánh giá trị tính toán được của thống kê kiểm định với một giá trị tới hạn (*critical value*) của cùng thống kê kiểm định đó để xác định xem nên bác bỏ hay không bác bỏ giả thuyết không. 

- Khi đưa ra một quyết định thống kê, có thể mắc phải hai sai lầm: bác bỏ một giả thuyết không đang đúng (sai lầm Loại I – *Type I error*, hay dương tính giả – *false positive*), hoặc không bác bỏ một giả thuyết không đang sai (sai lầm Loại II – *Type II error*, hay âm tính giả – *false negative*). 

- Mức ý nghĩa của một kiểm định (*level of significance*) là xác suất mắc sai lầm Loại I khi tiến hành kiểm định giả thuyết. Cách tiếp cận tiêu chuẩn trong kiểm định giả thuyết bao gồm việc chỉ định trước một mức ý nghĩa (tức là xác suất mắc sai lầm Loại I). Phần bù của mức ý nghĩa là mức độ tin cậy (*confidence level*). 

- Đối với các kiểm định giả thuyết liên quan đến trung bình tổng thể của một tổng thể có phân phối chuẩn với phương sai chưa biết, thống kê kiểm định chính xác về mặt lý thuyết là thống kê $t$ (*t-statistic*). 

- Để kiểm định xem sự khác biệt quan sát được giữa hai giá trị trung bình có ý nghĩa thống kê hay không, trước tiên nhà phân tích phải quyết định xem các mẫu là độc lập (*independent*) hay phụ thuộc/có liên quan (*dependent/related*). Nếu các mẫu độc lập, kiểm định sự khác biệt giữa hai giá trị trung bình (*test concerning differences between means*) được sử dụng. Nếu các mẫu phụ thuộc, kiểm định giá trị trung bình của các chênh lệch (*test of mean differences* hay kiểm định so sánh cặp – *paired comparisons test*) được sử dụng. 

- Để xác định sự khác biệt giữa hai trung bình tổng thể từ các tổng thể có phân phối chuẩn với phương sai chưa biết nhưng bằng nhau, kiểm định phù hợp là kiểm định $t$ (*t-test*) dựa trên việc gộp chung (*pooling*) các quan sát của hai mẫu để ước tính phương sai chung chưa biết. Kiểm định này dựa trên giả định các mẫu độc lập. 

- Trong các kiểm định liên quan đến hai giá trị trung bình dựa trên hai mẫu không độc lập, dữ liệu thường được sắp xếp thành các quan sát ghép cặp (*paired observations*) và một kiểm định trung bình của các chênh lệch (kiểm định so sánh cặp) được tiến hành. Khi các mẫu đến từ các tổng thể có phân phối chuẩn với phương sai chưa biết, thống kê kiểm định phù hợp có phân phối $t$. 

- Trong các kiểm định liên quan đến phương sai của một tổng thể đơn lẻ có phân phối chuẩn, thống kê kiểm định là Khi-bình phương (*chi-square* – $\chi^2$) với $n - 1$ bậc tự do (*degrees of freedom*), trong đó $n$ là kích thước mẫu. 

- Đối với các kiểm định liên quan đến sự khác biệt giữa phương sai của hai tổng thể có phân phối chuẩn dựa trên hai mẫu ngẫu nhiên, độc lập, thống kê kiểm định phù hợp dựa trên kiểm định $F$ (*F-test* – tỷ số của hai phương sai mẫu). Bậc tự do cho kiểm định $F$ này là $n_1 - 1$ và $n_2 - 1$, trong đó $n_1$ tương ứng với số lượng quan sát trong phép tính ở tử số, và $n_2$ là số lượng quan sát trong phép tính ở mẫu số của thống kê $F$. 

- Kiểm định tham số (*parametric test*) là một kiểm định giả thuyết liên quan đến một tham số tổng thể, hoặc một kiểm định giả thuyết dựa trên các giả định phân phối cụ thể. Ngược lại, kiểm định phi tham số (*nonparametric test*) hoặc không liên quan đến một tham số hoặc đưa ra các giả định tối thiểu về tổng thể mà từ đó mẫu được lấy ra. 


<!-- PDF Page 225 -->

- Kiểm định phi tham số chủ yếu được sử dụng khi dữ liệu không đáp ứng các giả định về phân phối, khi có các giá trị ngoại lai (*outliers*), khi dữ liệu được cho dưới dạng thứ hạng (*ranks*), hoặc khi giả thuyết chúng ta đang giải quyết không liên quan đến một tham số. 

##### **CÁC KIỂM ĐỊNH GIẢ THUYẾT TRONG TÀI CHÍNH (*HYPOTHESIS TESTS FOR FINANCE*)** 

## **<mark>2</mark>** 

*Giải thích kiểm định giả thuyết và các cấu phần của nó, bao gồm ý nghĩa thống kê, sai lầm Loại I và Loại II, và lực kiểm định*

Chúng ta sử dụng **kiểm định giả thuyết (*hypothesis testing*)** để đưa ra quyết định bằng cách sử dụng dữ liệu. Kiểm định giả thuyết là một phần của suy luận thống kê (*statistical inference*), quá trình đưa ra các phán đoán về một nhóm lớn hơn (tổng thể) dựa trên một nhóm quan sát nhỏ hơn (mẫu). 

Trong kiểm định giả thuyết, chúng ta kiểm định để xác định xem một thống kê mẫu có khả năng đến từ một tổng thể có giá trị tham số tổng thể như giả thuyết hay không. 

Các khái niệm và công cụ của kiểm định giả thuyết cung cấp một phương tiện khách quan để đánh giá xem bằng chứng hiện có có ủng hộ giả thuyết hay không. Sau khi áp dụng một kiểm định thống kê, chúng ta sẽ có ý niệm rõ ràng hơn về xác suất một giả thuyết là đúng hay sai, mặc dù kết luận của chúng ta luôn chưa đạt tới sự chắc chắn tuyệt đối. 

Trọng tâm chính của bài học này là khuôn khổ của kiểm định giả thuyết và các kiểm định liên quan đến giá trị trung bình và phương sai, hai thước đo thường xuyên được sử dụng trong đầu tư. 

###### **Quy trình Kiểm định Giả thuyết (*The Process of Hypothesis Testing*)** 

Kiểm định giả thuyết là một phần của nhánh thống kê được gọi là suy luận thống kê. Trong suy luận thống kê, có ước lượng (*estimation*) và kiểm định giả thuyết (*hypothesis testing*). Ước lượng bao gồm ước lượng điểm (*point estimates*) và ước lượng khoảng (*interval estimates*). Hãy xem xét một trung bình mẫu, vốn là một ước lượng điểm, mà chúng ta có thể sử dụng để lập một khoảng tin cậy. Trong kiểm định giả thuyết, trọng tâm là xem xét cách một thống kê mẫu cung cấp thông tin cho chúng ta về một tham số tổng thể. Một **giả thuyết (*hypothesis*)** là một phát biểu về một hoặc nhiều tổng thể mà chúng ta kiểm định bằng cách sử dụng các thống kê mẫu. 

Quy trình kiểm định giả thuyết bắt đầu bằng việc hình thành một lý thuyết để sắp xếp và giải thích các quan sát. Chúng ta đánh giá tính đúng đắn của lý thuyết bằng khả năng đưa ra các dự đoán chính xác của nó—ví dụ, dự đoán kết quả của các quan sát mới. Nếu các dự đoán là chính xác, chúng ta tiếp tục duy trì lý thuyết đó như một lời giải thích có khả năng đúng cho các quan sát của mình. Rủi ro đóng một vai trò trong kết quả của các quan sát trong tài chính, vì vậy chúng ta chỉ có thể cố gắng đưa ra các phán đoán không chệch, dựa trên xác suất về việc liệu dữ liệu mới có ủng hộ các dự đoán hay không. Kiểm định giả thuyết thống kê lấp đầy vai trò quan trọng đó là kiểm định các giả thuyết khi có sự không chắc chắn. Khi một nhà phân tích chuyển hóa đúng câu hỏi thành một giả thuyết có thể kiểm định được và tiến hành kiểm định giả thuyết, việc sử dụng các phương pháp khoa học đã được thiết lập vững chắc sẽ củng cố cho các kết luận và quyết định được đưa ra trên cơ sở kiểm định này. 

Chúng tôi sắp xếp phần giới thiệu về kiểm định giả thuyết này xoay quanh sáu bước được trình bày trong Minh họa 1, minh họa cách tiếp cận tiêu chuẩn đối với kiểm định giả thuyết. 


<!-- PDF Page 226 -->

###### **Minh họa 1: Quy trình Kiểm định Giả thuyết (*Exhibit 1: The Process of Hypothesis Testing*)** 

![](assets/Quantitative_method.pdf-0226-05.png)

<!-- Picture Text: Step 1: State the hypotheses<br>Step 2: Identify the appropriate test statistic<br>Step 3: Specify the level of significance<br>Step 4: State the decision rule<br>Step 5: Collect data and calculate the test statistic<br>Step 6: Make a decision<br> -->
> **Chú thích hình ảnh:**
> - **Bước 1:** Phát biểu các giả thuyết (*State the hypotheses*)
> - **Bước 2:** Xác định thống kê kiểm định phù hợp (*Identify the appropriate test statistic*)
> - **Bước 3:** Xác định mức ý nghĩa (*Specify the level of significance*)
> - **Bước 4:** Phát biểu quy tắc quyết định (*State the decision rule*)
> - **Bước 5:** Thu thập dữ liệu và tính toán thống kê kiểm định (*Collect data and calculate the test statistic*)
> - **Bước 6:** Đưa ra quyết định (*Make a decision*)

###### **_Phát biểu các Giả thuyết (Stating the Hypotheses)_** 

Đối với mỗi kiểm định giả thuyết, chúng ta luôn phát biểu hai giả thuyết: **giả thuyết không (*null hypothesis*)**, được ký hiệu là $H_0$, và **giả thuyết đối (*alternative hypothesis*)**, được ký hiệu là $H_a$. Giả thuyết không là một phát biểu liên quan đến một hoặc nhiều tham số tổng thể được coi là đúng trừ khi mẫu mà chúng ta sử dụng để tiến hành kiểm định giả thuyết đưa ra bằng chứng thuyết phục rằng giả thuyết không là sai. Trên thực tế, giả thuyết không là thứ mà chúng ta muốn bác bỏ. Nếu có đủ bằng chứng chỉ ra rằng giả thuyết không là không đúng, chúng ta bác bỏ nó để ủng hộ giả thuyết đối. 

Điều quan trọng là giả thuyết không và giả thuyết đối được phát biểu theo các tham số tổng thể (*population parameters*), và chúng ta sử dụng các thống kê mẫu (*sample statistics*) để kiểm định các giả thuyết này. 

Thứ hai, giả thuyết không và giả thuyết đối phải xung khắc lẫn nhau (*mutually exclusive*) và bao quát toàn bộ (*collectively exhaustive*); nói cách khác, tất cả các giá trị có thể có đều nằm trong giả thuyết không hoặc giả thuyết đối. 

###### **_Xác định Thống kê Kiểm định và Phân phối Phù hợp (Identify the Appropriate Test Statistic and Distribution)_** 

Thống kê kiểm định (*test statistic*) là một giá trị được tính toán trên cơ sở một mẫu mà khi được sử dụng kết hợp với một quy tắc quyết định sẽ là cơ sở để quyết định có bác bỏ giả thuyết không hay không. 

Trọng tâm của quyết định thống kê của chúng ta là giá trị của thống kê kiểm định. Thống kê kiểm định mà chúng ta sử dụng phụ thuộc vào những gì chúng ta đang kiểm định. 

Sau khi xác định được thống kê kiểm định phù hợp, chúng ta phải quan tâm đến phân phối của thống kê kiểm định đó. Chúng tôi trình bày các ví dụ về thống kê kiểm định và phân phối tương ứng của chúng trong Minh họa 2. 


<!-- PDF Page 227 -->

**Minh họa 2: Các Thống kê Kiểm định và Phân phối của Chúng (*Exhibit 2: Test Statistics and Their Distribution*)** 

|**Nội dung Cần Kiểm định (*What We Want to Test*)**|**Thống kê Kiểm định (*Test Statistic*)**|**Phân phối Xác suất của Thống kê (*Probability Distribution of the Statistic*)**|**Bậc Tự do (*Degrees of Freedom*)**|
|---|---|---|---|
|Kiểm định một giá trị trung bình đơn lẻ (*Test of a single mean*)|$$t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}$$|Phân phối $t$ (*t-distributed*)|$n - 1$|
|Kiểm định sự khác biệt giữa hai giá trị trung bình (*Test of the difference in means*)|$$t = \frac{(\bar{X}_{d1} - \bar{X}_{d2}) - (\mu_{d1} - \mu_{d2})}{\sqrt{\frac{s_p^2}{n_{d1}} + \frac{s_p^2}{n_{d2}}}}$$|Phân phối $t$ (*t-distributed*)|$n_1 + n_2 - 2$|
|Kiểm định giá trị trung bình của các chênh lệch (*Test of the mean of differences*)|$$t = \frac{\bar{d} - \mu_{d0}}{s_{\bar{d}}}$$|Phân phối $t$ (*t-distributed*)|$n - 1$|
|Kiểm định một phương sai đơn lẻ (*Test of a single variance*)|$$\chi^2 = \frac{(n - 1)s^2}{\sigma_0^2}$$|Phân phối Khi-bình phương (*Chi-square distributed*)|$n - 1$|
|Kiểm định sự khác biệt giữa hai phương sai (*Test of the difference in variances*)|$$F = \frac{s_{\text{Before}}^2}{s_{\text{After}}^2}$$|Phân phối $F$ (*F-distributed*)|$n_1 - 1, n_2 - 1$|
|Kiểm định hệ số tương quan (*Test of a correlation*)|$$t = \frac{r\sqrt{n - 2}}{\sqrt{1 - r^2}}$$|Phân phối $t$ (*t-distributed*)|$n - 2$|
|Kiểm định tính độc lập – dữ liệu phân loại (*Test of independence – categorical data*)|$$\chi^2 = \sum_{i=1}^{m} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$|Phân phối Khi-bình phương (*Chi-square distributed*)|$(r - 1)(c - 1)$|

_Lưu ý:_ $\mu_0, \mu_{d0}$ và $\sigma_0^2$ lần lượt ký hiệu các giá trị theo giả thuyết của trung bình, trung bình chênh lệch và phương sai. $\bar{X}, \bar{d}, s^2, s$ và $r$ lần lượt ký hiệu cho trung bình mẫu, trung bình của các chênh lệch, phương sai mẫu, độ lệch chuẩn mẫu và hệ số tương quan mẫu, với các chỉ số dưới cho biết mẫu tương ứng nếu phù hợp. Kích thước mẫu được biểu thị là $n$, và chỉ số dưới cho biết mẫu nếu phù hợp. $O_{ij}$ và $E_{ij}$ lần lượt là tần số quan sát được (*observed frequencies*) và tần số kỳ vọng (*expected frequencies*), với $r$ biểu thị số hàng và $c$ biểu thị số cột trong bảng tiếp liên (*contingency table*). 

###### **_Xác định Mức Ý nghĩa (Specify the Level of Significance)_** 

Mức ý nghĩa (*level of significance*) phản ánh lượng bằng chứng mẫu mà chúng ta yêu cầu để bác bỏ giả thuyết không. Tiêu chuẩn bằng chứng yêu cầu có thể thay đổi tùy theo bản chất của các giả thuyết và mức độ nghiêm trọng của hậu quả khi mắc sai lầm. 

Có bốn kết quả có thể xảy ra khi chúng ta kiểm định một giả thuyết không, như được hiển thị trong Minh họa 3. **Sai lầm Loại I (*Type I error*)** là dương tính giả (*false positive* – bác bỏ khi giả thuyết không đang đúng), trong khi **sai lầm Loại II (*Type II error*)** là âm tính giả (*false negative* – không bác bỏ khi giả thuyết không đang sai). 

**Minh họa 3: Các Quyết định Đúng và Sai trong Kiểm định Giả thuyết (*Exhibit 3: Correct and Incorrect Decisions in Hypothesis Testing*)** 

|**Quyết định (*Decision*)**|**$H_0$ Đúng (*$H_0$ True*)**|**$H_0$ Sai (*$H_0$ False*)**|
|---|---|---|
|**Không bác bỏ $H_0$ (*Fail to reject $H_0$*)**|**Quyết định đúng (*Correct decision*):**<br>Không bác bỏ một giả thuyết không đang đúng.|**Sai lầm Loại II (*Type II error*):**<br>Không bác bỏ một giả thuyết không đang sai.<br>Âm tính giả (*False negative*)|
|**Bác bỏ $H_0$ (*Reject $H_0$*)**|**Sai lầm Loại I (*Type I error*):**<br>Bác bỏ một giả thuyết không đang đúng.<br>Dương tính giả (*False positive*)|**Quyết định đúng (*Correct decision*):**<br>Bác bỏ một giả thuyết không đang sai.|


<!-- PDF Page 228 -->

Khi đưa ra một quyết định trong một kiểm định giả thuyết, chúng ta đối mặt với rủi ro mắc sai lầm Loại I hoặc Loại II. Như được hiển thị trong Minh họa 3, các sai lầm này loại trừ lẫn nhau (*mutually exclusive*): Nếu chúng ta bác bỏ nhầm giả thuyết không đang đúng, chúng ta chỉ có thể mắc sai lầm Loại I; nếu chúng ta không bác bỏ nhầm giả thuyết không đang sai, chúng ta chỉ có thể mắc sai lầm Loại II. 

Xác suất mắc sai lầm Loại I được ký hiệu bằng chữ cái Hy Lạp viết thường alpha, $\alpha$. Xác suất này còn được gọi là **mức ý nghĩa (*level of significance*)** của kiểm định, và phần bù của nó, $(1 - \alpha)$, là **mức độ tin cậy (*confidence level*)**. Ví dụ, mức ý nghĩa $5\%$ cho một kiểm định có nghĩa là có $5\%$ xác suất bác bỏ một giả thuyết không đang đúng và tương ứng với mức độ tin cậy $95\%$. 

Việc kiểm soát xác suất của hai loại sai lầm này bao hàm sự đánh đổi (*trade-off*). Với các yếu tố khác không đổi, nếu chúng ta giảm xác suất mắc sai lầm Loại I bằng cách chỉ định một mức ý nghĩa nhỏ hơn (chẳng hạn $1\%$ thay vì $5\%$), chúng ta sẽ làm tăng xác suất mắc sai lầm Loại II bởi vì chúng ta sẽ ít bác bỏ giả thuyết không hơn, kể cả khi nó sai. Cả sai lầm Loại I và Loại II đều là rủi ro đưa ra kết luận sai. Việc chấp nhận loại sai lầm nào nhiều hơn phụ thuộc vào hậu quả của các sai lầm đó, chẳng hạn như chi phí. Sự đánh đổi này cân nhắc tác động của những sai lầm mà chúng ta sẵn sàng chấp nhận và nếu có thì với cái giá nào. Cách duy nhất để giảm xác suất của cả hai loại sai lầm cùng một lúc là tăng kích thước mẫu, $n$. 

Trong khi mức ý nghĩa của một kiểm định là xác suất bác bỏ *sai* giả thuyết không đang đúng, thì **lực kiểm định (*power of a test*)** là xác suất bác bỏ _đúng_ giả thuyết không—tức là xác suất bác bỏ giả thuyết không khi nó thực sự sai. Lực kiểm định trên thực tế là phần bù của sai lầm Loại II. Xác suất mắc sai lầm Loại II thường được ký hiệu bằng chữ cái Hy Lạp viết thường beta, $\beta$. Chúng ta có thể phân loại các xác suất khác nhau trong Minh họa 4 để phản ánh các ký hiệu thường được sử dụng. 

**Minh họa 4: Các Xác suất Liên quan đến Quyết định Kiểm định Giả thuyết (*Exhibit 4: Probabilities Associated with Hypothesis Testing Decisions*)** 

|**Quyết định (*Decision*)**|**$H_0$ Đúng (*$H_0$ True*)**|**$H_0$ Sai (*$H_0$ False*)**|
|---|---|---|
|Không bác bỏ $H_0$ (*Fail to reject $H_0$*)|$1 - \alpha$|$\beta$|
|Bác bỏ $H_0$ (*Reject $H_0$*)|$\alpha$|$1 - \beta$|

###### **_Phát biểu Quy tắc Quyết định (State the Decision Rule)_** 

Bước thứ tư trong kiểm định giả thuyết là phát biểu quy tắc quyết định: Khi nào chúng ta bác bỏ giả thuyết không, và khi nào chúng ta không bác bỏ? Hành động chúng ta thực hiện dựa trên việc so sánh thống kê kiểm định mẫu tính toán được với một hoặc nhiều giá trị được chỉ định, được gọi là **các giá trị tới hạn (*critical values*)**. 

(Các) giá trị tới hạn mà chúng ta chọn dựa trên mức ý nghĩa và phân phối xác suất gắn với thống kê kiểm định. Nếu chúng ta thấy rằng giá trị tính toán được của thống kê kiểm định khắc nghiệt hơn (*more extreme* – nằm ngoài vùng chấp nhận) so với (các) giá trị tới hạn, thì chúng ta bác bỏ giả thuyết không; chúng ta nói rằng kết quả có **ý nghĩa thống kê (*statistically significant*)**. Ngược lại, chúng ta không bác bỏ giả thuyết không; không có đủ bằng chứng để bác bỏ giả thuyết không. Hãy nhớ lại rằng mức ý nghĩa nhỏ nhất mà tại đó giả thuyết không có thể bị bác bỏ chính là **giá trị p (*p-value*)**, phần diện tích trong phân phối xác suất nằm bên ngoài thống kê kiểm định tính toán được. 


<!-- PDF Page 229 -->

###### **BỘ CÂU HỎI (*QUESTION SET*)** 

1. Willco là một nhà sản xuất trong một ngành có tính chu kỳ đã trưởng thành. Trong chu kỳ ngành gần đây nhất, thu nhập ròng của công ty đạt trung bình 30 triệu USD mỗi năm với độ lệch chuẩn là 10 triệu USD ($n = 6$ quan sát). Ban giám đốc tuyên bố rằng kết quả hoạt động của Willco trong chu kỳ gần đây nhất là nhờ các phương pháp tiếp cận mới và khả năng sinh lời của Willco sẽ vượt mức trung bình 24 triệu USD mỗi năm từng quan sát được trong các chu kỳ trước. 

   - **A.** Với $\mu$ là giá trị tổng thể của thu nhập ròng hàng năm trung bình, hãy thiết lập giả thuyết không và giả thuyết đối nhất quán với việc kiểm định tuyên bố của ban giám đốc Willco. 
   - **B.** Giả sử thu nhập ròng của Willco ít nhất có phân phối xấp xỉ chuẩn, hãy xác định thống kê kiểm định phù hợp và tính bậc tự do. 
   - **C.** Dựa trên giá trị tới hạn là $2.015$, hãy xác định xem có bác bỏ giả thuyết không hay không. 

###### **Lời giải (*Solution*):** 

   - **A.** Chúng ta thường thiết lập điều kiện “mong muốn” hoặc “nghi ngờ” làm giả thuyết đối. Ở đây, điều kiện đó là giá trị tổng thể của thu nhập ròng hàng năm trung bình của Willco vượt quá 24 triệu USD. Do đó, ta có $H_0: \mu \le 24$ đối lập với $H_a: \mu > 24$. 
   - **B.** Biết rằng thu nhập ròng có phân phối chuẩn với phương sai chưa biết, thống kê kiểm định phù hợp là thống kê $t$ với bậc tự do là $n - 1 = 6 - 1 = 5$. 
   - **C.** Chúng ta bác bỏ giả thuyết không nếu thống kê $t$ tính toán được lớn hơn $2.015$. Thống kê $t$ tính toán được là: 

   $$t = \frac{30 - 24}{10 / \sqrt{6}} = 1.4697$$

   - **D.** Bởi vì thống kê kiểm định tính toán được không vượt quá $2.015$, chúng ta không bác bỏ giả thuyết không (*fail to reject the null hypothesis*). Không có đủ bằng chứng để chỉ ra rằng thu nhập ròng trung bình lớn hơn 24 triệu USD. 

2. Với các yếu tố khác không đổi, việc chỉ định một mức ý nghĩa nhỏ hơn trong một kiểm định giả thuyết có khả năng làm tăng xác suất của: 

||**Sai lầm Loại I (*Type I error*)?**|**Sai lầm Loại II (*Type II error*)?**|
|---|---|---|
|A.|Không (*No*)|Không (*No*)|
|B.|Không (*No*)|Có (*Yes*)|
|C.|Có (*Yes*)|Không (*No*)|

###### **Lời giải (*Solution*):** 

B đúng. Việc chỉ định một mức ý nghĩa nhỏ hơn làm giảm xác suất mắc sai lầm Loại I (bác bỏ một giả thuyết không đang đúng) nhưng làm tăng xác suất mắc sai lầm Loại II (không bác bỏ một giả thuyết không đang sai). Khi mức ý nghĩa giảm xuống, giả thuyết không ít bị bác bỏ hơn. 
