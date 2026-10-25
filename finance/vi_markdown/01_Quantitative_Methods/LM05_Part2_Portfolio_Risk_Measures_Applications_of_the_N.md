# Tập 1: Phương pháp Định lượng (*Quantitative Methods*)
## Học phần 5: Toán học Danh mục đầu tư (*Portfolio Mathematics*)
### Phần 2/2: Các Thước đo Rủi ro Danh mục đầu tư: Ứng dụng của Phân phối Chuẩn (*Portfolio Risk Measures: Applications of the Normal Distribution*) (Trang PDF 173–182)

---

<!-- PDF Page 173 -->

### **CÁC THƯỚC ĐO RỦI RO DANH MỤC ĐẦU TƯ: ỨNG DỤNG CỦA PHÂN PHỐI CHUẨN (*PORTFOLIO RISK MEASURES: APPLICATIONS OF THE NORMAL DISTRIBUTION*)** 

# **<mark>4</mark>** 

định nghĩa rủi ro thiếu hụt (*shortfall risk*), tính toán tỷ số an toàn trên hết (*safety-first ratio*), và xác định danh mục đầu tư tối ưu bằng cách sử dụng tiêu chuẩn an toàn trên hết của Roy (*Roy’s safety-first criterion*) 

Lý thuyết danh mục đầu tư hiện đại (MPT) thường liên quan đến việc đánh giá các cơ hội đầu tư bằng cách sử dụng các thước đo tỷ suất sinh lợi trung bình và phương sai của tỷ suất sinh lợi. Trong lý thuyết kinh tế, **phân tích trung bình–phương sai (*mean–variance analysis*)** hoàn toàn chính xác khi các nhà đầu tư ngại rủi ro (*risk averse*); khi họ lựa chọn các khoản đầu tư nhằm tối đa hóa hữu dụng kỳ vọng (*expected utility*) hay sự thỏa mãn; và khi hoặc (giả định 1) tỷ suất sinh lợi có phân phối chuẩn hoặc (giả định 2) các nhà đầu tư có hàm hữu dụng bậc hai (*quadratic utility functions* – một khái niệm được sử dụng trong kinh tế học để biểu diễn toán học sự đánh đổi giữa rủi ro và tỷ suất sinh lợi). Tuy nhiên, phân tích trung bình–phương sai vẫn có thể hữu ích—nghĩa là nó có thể đúng một cách xấp xỉ—khi giả định 1 hoặc giả định 2 bị vi phạm. Bởi vì những người hành nghề thực tiễn thích làm việc với các đại lượng có thể quan sát được, chẳng hạn như tỷ suất sinh lợi, nên mệnh đề cho rằng tỷ suất sinh lợi ít nhất tuân theo phân phối chuẩn một cách xấp xỉ đã đóng một vai trò then chốt trong phần lớn lý thuyết MPT. 

Để minh họa khái niệm này, giả sử một nhà đầu tư đang tiết kiệm cho việc nghỉ hưu. Mặc dù mục tiêu của bà là kiếm được tỷ suất sinh lợi thực cao nhất có thể, bà tin rằng danh mục đầu tư ít nhất phải đạt được mục tiêu bảo toàn vốn thực (*real capital preservation*) trong dài hạn. Giả sử tỷ lệ lạm phát kỳ vọng dài hạn là 2 phần trăm, mức tỷ suất sinh lợi tối thiểu có thể chấp nhận được (*minimum acceptable return*) sẽ là 2 phần trăm. Bảng minh họa 10 so sánh ba phương án đầu tư thay thế xét về tỷ suất sinh lợi kỳ vọng và độ lệch chuẩn của tỷ suất sinh lợi của chúng. Xác suất rơi xuống dưới mức 2 phần trăm được tính dựa trên giả định tỷ suất sinh lợi có phân phối chuẩn. Trong Bảng minh họa 10, chúng ta thấy rằng Danh mục II, kết hợp tỷ suất sinh lợi kỳ vọng cao nhất và độ biến động (*volatility*) thấp nhất, có xác suất kiếm được dưới 2 phần trăm là thấp nhất (hoặc tương đương, có xác suất kiếm được ít nhất 2 phần trăm là cao nhất). Điều này cũng có thể được nhìn thấy trong Bảng B, cho thấy Danh mục II có diện tích tô đậm nhỏ nhất ở phía bên trái mức 2 phần trăm (xác suất kiếm được thấp hơn mức tỷ suất sinh lợi tối thiểu có thể chấp nhận được). 

**Bảng minh họa 10: Xác suất Kiếm được Tỷ suất sinh lợi Tối thiểu Có thể Chấp nhận được (*Probability of Earning a Minimum Acceptable Return*)** 

#### **Bảng A: Đặc điểm của các Danh mục Thay thế (*Alternative Portfolio Characteristics*)** 

|**Danh mục đầu tư (*Portfolio*)**|**I**|**II**|**III**|
|---|---|---|---|
|Tỷ suất sinh lợi kỳ vọng (*Expected return*)|5%|8%|5%|
|Độ lệch chuẩn của tỷ suất sinh lợi (*Standard deviation of return*)|8%|8%|12%|
|Xác suất kiếm được $< 2\%$ [$P(x < 2)$]|37.7%|24.6%|41.7%|
|Xác suất kiếm được $\ge 2\%$ [$P(x \ge 2)$]|62.3%|75.4%|58.3%|


<!-- PDF Page 174 -->

#### **Bảng B: Khả năng Đạt được Tỷ suất sinh lợi Tối thiểu Có thể Chấp nhận được (*Likelihoods of Attaining Minimal Acceptable Return*)** 

##### **_A. Danh mục I (*Portfolio I*)_** 

![](assets/Quantitative_method.pdf-0174-05.png)

<!-- Picture Text: 0.05<br>Minimum Acceptable Mean = 5%<br>0.04 Return = 2%<br>0.03<br>0.02<br>0.01<br>0<br>–40 –30 –20 –10 0 10 20 30 40<br>Return<br>B. Portfolio II<br>0.05<br>Minimum Acceptable Mean = 8 %<br>0.04 Return = 2%<br>0.03<br>0.02<br>0.01<br>0<br>–40 –30 –20 –10 0 10 20 30 40<br>Return<br>C. Portfolio III<br>0.05<br>0.04<br>Minimum Acceptable Mean = 5%<br>0.03 Return = 2%<br>0.02<br>0.01<br>0<br>–40 –30 –20 –10 0 10 20 30 40<br>Return<br> -->

> **Chú thích hình ảnh:**
> - **A. Portfolio I:** Tỷ suất sinh lợi tối thiểu chấp nhận được (*Minimum Acceptable Return*) = 2%, Trung bình (*Mean*) = 5%.
> - **B. Portfolio II:** Tỷ suất sinh lợi tối thiểu chấp nhận được = 2%, Trung bình = 8%.
> - **C. Portfolio III:** Tỷ suất sinh lợi tối thiểu chấp nhận được = 2%, Trung bình = 5% (đường cong rộng hơn do độ lệch chuẩn 12%).

Phân tích trung bình–phương sai nhìn chung xem xét rủi ro một cách đối xứng theo nghĩa là độ lệch chuẩn nắm bắt sự biến thiên ở cả phía trên và phía dưới giá trị trung bình. Một cách tiếp cận thay thế chỉ đánh giá rủi ro phía dưới (*downside risk*). Chúng ta thảo luận về một cách tiếp cận như vậy, đó là các quy tắc an toàn trên hết (*safety-first rules*), bởi vì chúng cung cấp một minh họa xuất sắc về việc áp dụng lý thuyết phân phối chuẩn vào các bài toán đầu tư thực tế. **Các quy tắc an toàn trên hết (*Safety-first rules*)** tập trung vào **rủi ro thiếu hụt (*shortfall risk*)**, tức rủi ro giá trị danh mục đầu tư (hoặc tỷ suất sinh lợi danh mục đầu tư) sẽ rơi xuống dưới một mức tối thiểu có thể chấp nhận được nào đó trong một khoảng thời gian nhất định. Rủi ro tài sản trong một quỹ hưu trí có mức hưởng xác định (*defined benefit plan*) giảm xuống thấp hơn các nghĩa vụ nợ của quỹ là một ví dụ về rủi ro thiếu hụt. 

Giả sử một nhà đầu tư coi bất kỳ mức tỷ suất sinh lợi nào thấp hơn mức $R_L$ là không thể chấp nhận được. **Tiêu chuẩn an toàn trên hết của Roy (*Roy’s safety-first criterion*)** (Roy 1952) phát biểu rằng danh mục đầu tư tối ưu sẽ tối thiểu hóa xác suất để tỷ suất sinh lợi của danh mục, $R_P$, rơi xuống dưới mức ngưỡng (*threshold level*), $R_L$. Nghĩa là, mục tiêu của nhà đầu tư là chọn một danh mục tối thiểu hóa $P(R_P < R_L)$. Khi tỷ suất sinh lợi của danh mục có phân phối chuẩn, chúng ta có thể tính $P(R_P < R_L)$ bằng cách sử dụng số lần độ lệch chuẩn mà mức $R_L$ nằm thấp hơn tỷ suất sinh lợi kỳ vọng của danh mục, $E(R_P)$. 


<!-- PDF Page 175 -->

Danh mục nào có $E(R_P) - R_L$ lớn nhất tương ứng với độ lệch chuẩn sẽ tối thiểu hóa $P(R_P < R_L)$. Do đó, nếu tỷ suất sinh lợi có phân phối chuẩn, danh mục tối ưu theo tiêu chuẩn an toàn trên hết sẽ _tối đa hóa_ **tỷ số an toàn trên hết (*safety-first ratio* – SFRatio)**, như sau: 

$$\text{SFRatio} = \frac{E(R_P) - R_L}{\sigma_P} \tag{9}$$

Đại lượng $E(R_P) - R_L$ là khoảng cách từ tỷ suất sinh lợi trung bình đến mức thiếu hụt (*shortfall level*). Chia khoảng cách này cho $\sigma_P$ sẽ cho biết khoảng cách tính theo đơn vị độ lệch chuẩn. Khi lựa chọn giữa các danh mục đầu tư bằng tiêu chuẩn của Roy (giả định phân phối chuẩn), hãy làm theo hai bước sau: 

**1.** Tính $\text{SFRatio}$ của từng danh mục đầu tư. 

**2.** Chọn danh mục đầu tư có $\text{SFRatio}$ cao nhất. 

Đối với một danh mục có tỷ số an toàn trên hết cho trước, xác suất để tỷ suất sinh lợi của nó nhỏ hơn $R_L$ là $\text{Normal}(-\text{SFRatio})$, và danh mục tối ưu theo tiêu chuẩn an toàn trên hết có xác suất đó thấp nhất. Ví dụ, giả sử mức tỷ suất sinh lợi ngưỡng của một nhà đầu tư, $R_L$, là 2 phần trăm. Ông được giới thiệu hai danh mục đầu tư. Danh mục 1 có tỷ suất sinh lợi kỳ vọng là 12 phần trăm, với độ lệch chuẩn là 15 phần trăm. Danh mục 2 có tỷ suất sinh lợi kỳ vọng là 14 phần trăm, với độ lệch chuẩn là 16 phần trăm. Các tỷ số $\text{SFRatio}$, sử dụng Phương trình 9, lần lượt là $0.667 = (12 - 2)/15$ và $0.75 = (14 - 2)/16$ đối với Danh mục 1 và 2. Đối với Danh mục 2 vượt trội hơn, xác suất để tỷ suất sinh lợi của danh mục nhỏ hơn 2 phần trăm là $N(-0.75) = 1 - N(0.75) = 1 - 0.7734 = 0.227$, hay khoảng 23 phần trăm, giả sử rằng tỷ suất sinh lợi của danh mục có phân phối chuẩn. 

Bạn có thể đã nhận thấy sự tương đồng giữa $\text{SFRatio}$ và tỷ số Sharpe (*Sharpe ratio*). Nếu chúng ta thay lãi suất phi rủi ro, $R_F$, cho mức tới hạn $R_L$, thì $\text{SFRatio}$ sẽ trở thành tỷ số Sharpe. Cách tiếp cận an toàn trên hết mang lại một góc nhìn mới về tỷ số Sharpe: Khi chúng ta đánh giá các danh mục đầu tư bằng tỷ số Sharpe, danh mục có tỷ số Sharpe cao nhất chính là danh mục tối thiểu hóa xác suất tỷ suất sinh lợi của danh mục sẽ thấp hơn lãi suất phi rủi ro (với giả định phân phối chuẩn). 

##### **VÍ DỤ 3** 

#### **Danh mục đầu tư Tối ưu theo Tiêu chuẩn An toàn trên hết cho một Khách hàng (*The Safety-First Optimal Portfolio for a Client*)** 

Bạn đang nghiên cứu các phương án phân bổ tài sản cho một khách hàng tại Canada có danh mục đầu tư trị giá CAD 800,000. Mặc dù mục tiêu đầu tư của bà là tăng trưởng dài hạn, nhưng vào cuối một năm, bà có thể muốn thanh lý CAD 30,000 từ danh mục để tài trợ cho các chi phí giáo dục. Nếu nhu cầu đó phát sinh, bà muốn có thể rút ra CAD 30,000 mà không xâm phạm vào số vốn ban đầu là CAD 800,000. Bảng minh họa 11 cho thấy ba phương án phân bổ thay thế. 

##### **Bảng minh họa 11: Giá trị Trung bình và Độ lệch chuẩn của Ba Phương án Phân bổ (tính bằng Phần trăm) (*Mean and Standard Deviation for Three Allocations (in Percent)*)** 

|**Phương án phân bổ (*Allocation*)**|**A**|**B**|**C**|
|---|---|---|---|
|Tỷ suất sinh lợi hàng năm kỳ vọng (*Expected annual return*)|25|11|14|
|Độ lệch chuẩn của tỷ suất sinh lợi (*Standard deviation of return*)|27|8|20|

Hãy trả lời các câu hỏi sau (giả định phân phối chuẩn cho Câu hỏi 2 và 3): 


<!-- PDF Page 176 -->

1. Với mong muốn của khách hàng là không xâm phạm vào vốn gốc CAD 800,000, mức thiếu hụt, $R_L$, là bao nhiêu? Sử dụng mức thiếu hụt này để trả lời câu hỏi 2. 

##### **Lời giải:** 

Bởi vì $\text{CAD } 30,000 / \text{CAD } 800,000$ bằng 3.75 phần trăm, nên với bất kỳ mức tỷ suất sinh lợi nào thấp hơn 3.75 phần trăm, khách hàng sẽ phải xâm phạm vào vốn gốc nếu bà rút ra CAD 30,000. Do đó, $R_L = 3.75\%$. 

2. Theo tiêu chuẩn an toàn trên hết, phương án nào trong ba phương án phân bổ là tốt nhất? 

(Gợi ý: để quyết định phương án phân bổ nào trong ba phương án là tối ưu theo tiêu chuẩn an toàn trên hết, hãy chọn phương án có tỷ số $[E(R_P) - R_L]/\sigma_P$ cao nhất.) 

   - **A.** $0.787037 = (25 - 3.75)/27$ 

   - **B.** $0.90625 = (11 - 3.75)/8$ 

   - **C.** $0.5125 = (14 - 3.75)/20$ 

##### **Lời giải:** 

B là đáp án đúng. Phương án phân bổ B, với tỷ số lớn nhất (0.90625), là phương án tốt nhất theo tiêu chuẩn an toàn trên hết. 

3. Xác suất để tỷ suất sinh lợi của danh mục tối ưu theo tiêu chuẩn an toàn trên hết nhỏ hơn mức thiếu hụt là bao nhiêu? 

##### **Lời giải:** 

Để trả lời câu hỏi này, lưu ý rằng $P(R_B < 3.75) = \text{Normal}(-0.90625)$. Chúng ta có thể làm tròn 0.90625 thành 0.91 để sử dụng với bảng hàm phân phối tích lũy (CDF) chuẩn tắc. Trước tiên, chúng ta tính $\text{Normal}(-0.91) = 1 - \text{Normal}(0.91) = 1 - 0.8186 = 0.1814$, hay khoảng 18.1 phần trăm. Sử dụng hàm bảng tính cho CDF chuẩn tắc với giá trị $-0.90625$ mà không làm tròn, chúng ta thu được 0.182402, hay khoảng 18.2 phần trăm. Danh mục tối ưu theo tiêu chuẩn an toàn trên hết có khoảng 18 phần trăm khả năng không đạt được ngưỡng tỷ suất sinh lợi 3.75 phần trăm. Điều này có thể được nhìn thấy trong đồ thị sau đây, trong đó Phương án phân bổ B có diện tích nằm dưới đường cong phân phối ở phía bên trái mức 3.75 phần trăm là nhỏ nhất. 

![](assets/Quantitative_method.pdf-0176-17.png)

<!-- Picture Text: 0.10<br>Target Return = 3.75%<br>0.08<br>B<br>0.06<br>0.04 C<br>0.02 A<br>0<br>–80.3 –56.3 –32.3 –8.3 15.8 39.8 63.8 87.8<br>Percent<br> -->

> **Chú thích hình ảnh:**
> - **Target Return = 3.75%:** Tỷ suất sinh lợi mục tiêu = 3.75%
> - Ba đường cong phân phối chuẩn của phương án **A, B, C** với trục hoành là **Percent** (Phần trăm).

Có một số điểm đáng lưu ý. Thứ nhất, nếu các dữ liệu đầu vào hơi khác một chút, chúng ta có thể nhận được một thứ hạng khác. Ví dụ, nếu tỷ suất sinh lợi trung bình của B là 10 phần trăm thay vì 11 phần trăm, thì Phương án phân bổ A sẽ vượt trội hơn B. Thứ hai, nếu việc đáp ứng ngưỡng tỷ suất sinh lợi 3.75 phần trăm là một điều bắt buộc thay vì chỉ là một mong muốn, thì mức CAD 830,000 sau một năm có thể được mô hình hóa như một khoản nợ phải trả (*liability*). Các chiến lược thu nhập cố định, chẳng hạn như khớp dòng tiền (*cash flow matching*), có thể được sử dụng để bù đắp hoặc miễn nhiễm rủi ro (*immunize*) cho khoản chuẩn nợ (*quasi-liability*) trị giá CAD 830,000 này. 


<!-- PDF Page 177 -->

Trong nhiều bối cảnh đầu tư ngoài tiêu chuẩn an toàn trên hết của Roy, chúng ta sử dụng phân phối chuẩn để ước tính xác suất. Một lĩnh vực khác mà phân phối chuẩn đóng vai trò quan trọng là quản trị rủi ro tài chính (*financial risk management*). Các định chế tài chính, chẳng hạn như ngân hàng đầu tư, nhà kinh doanh chứng khoán và ngân hàng thương mại, có các hệ thống chính thức để đo lường và kiểm soát rủi ro tài chính ở nhiều cấp độ khác nhau, từ các vị thế giao dịch đến rủi ro tổng thể của toàn công ty. Hai trụ cột chính trong quản trị rủi ro tài chính là giá trị có rủi ro (*value at risk* – VaR) và kiểm định sức chịu đựng/phân tích kịch bản (*stress testing/scenario analysis*). **Kiểm định sức chịu đựng (*Stress testing*)** và **phân tích kịch bản (*scenario analysis*)** đề cập đến một tập hợp các kỹ thuật nhằm ước tính các khoản lỗ trong những sự kết hợp biến cố hoặc kịch bản cực kỳ bất lợi. **Giá trị có rủi ro (*Value at risk* – VaR)** là thước đo bằng tiền về giá trị tổn thất tối thiểu dự kiến trong một khoảng thời gian xác định (ví dụ: một ngày, một quý, hoặc một năm) tại một mức xác suất cho trước (thường là 0.05 hoặc 0.01). Giả sử chúng ta chỉ định khung thời gian một ngày và mức xác suất là 0.05, khi đó sẽ được gọi là VaR một ngày ở mức độ tin cậy 95 phần trăm (*95 percent one-day VaR*). Nếu mức VaR này bằng EUR 5 triệu đối với một danh mục đầu tư, thì sẽ có xác suất 0.05 là danh mục đầu tư đó sẽ lỗ từ EUR 5 triệu trở lên trong một ngày duy nhất (giả sử các giả định của chúng ta là chính xác). Một trong những cách tiếp cận cơ bản để ước tính VaR, phương pháp phương sai–hiệp phương sai hay phương pháp giải tích (*variance–covariance or analytical method*), giả định rằng tỷ suất sinh lợi tuân theo phân phối chuẩn. 

##### **BỘ CÂU HỎI (*QUESTION SET*)** 

Một khách hàng có danh mục đầu tư gồm các cổ phiếu phổ thông và các công cụ thu nhập cố định với giá trị hiện tại là GBP 1,350,000. Bà dự định thanh lý GBP 50,000 từ danh mục đầu tư vào cuối năm để mua cổ phần hợp danh trong một doanh nghiệp. Hơn nữa, khách hàng muốn có thể rút ra GBP 50,000 mà không làm giảm số vốn ban đầu là GBP 1,350,000. Bảng sau đây cho thấy bốn phương án phân bổ tài sản thay thế. 

##### **Giá trị Trung bình và Độ lệch chuẩn của Bốn Phương án Phân bổ (tính bằng Phần trăm) (*Mean and Standard Deviation for Four Allocations (in Percent)*)** 

||**A**|**B**|**C**|**D**|
|---|---|---|---|---|
|Tỷ suất sinh lợi hàng năm kỳ vọng (*Expected annual return*)|16|12|10|9|
|Độ lệch chuẩn của tỷ suất sinh lợi (*Standard deviation of return*)|24|17|12|11|

1. Hãy trả lời các câu hỏi sau (giả định phân phối chuẩn cho Phần B và C): 

   - **A.** Với mong muốn của khách hàng là không xâm phạm vào vốn gốc GBP 1,350,000, mức thiếu hụt, $R_L$, là bao nhiêu? Sử dụng mức thiếu hụt này để trả lời Câu B. 

   - **B.** Theo tiêu chuẩn an toàn trên hết, phương án phân bổ nào là tốt nhất? 

   - **C.** Xác suất để tỷ suất sinh lợi của danh mục tối ưu theo tiêu chuẩn an toàn trên hết nhỏ hơn mức thiếu hụt, $R_L$, là bao nhiêu? 

   - **Lời giải:** 

   - **A.** Bởi vì $\text{GBP } 50,000 / \text{GBP } 1,350,000$ bằng 3.7 phần trăm, nên với bất kỳ mức tỷ suất sinh lợi nào thấp hơn 3.7 phần trăm, khách hàng sẽ phải xâm phạm vào vốn gốc nếu bà rút ra GBP 50,000. Do đó, $R_L = 3.7\%$. 

   - **B.** Để quyết định phương án phân bổ nào là tối ưu theo tiêu chuẩn an toàn trên hết, hãy chọn phương án có tỷ số $[E(R_P) - R_L]/\sigma_P$ cao nhất: 

      - Phương án A: $0.5125 = (16 - 3.7)/24$. 

      - Phương án B: $0.488235 = (12 - 3.7)/17$. 


<!-- PDF Page 178 -->

      - Phương án C: $0.525 = (10 - 3.7)/12$. 

      - Phương án D: $0.481818 = (9 - 3.7)/11$. 

      - Phương án C, với tỷ số lớn nhất (0.525), là phương án thay thế tốt nhất theo tiêu chuẩn an toàn trên hết. 

   - **C.** Để trả lời câu hỏi này, lưu ý rằng $P(R_C < 3.7) = N((0.037 - 0.10)/0.12) = \text{Normal}(-0.525)$. Bằng cách sử dụng hàm `NORM.S.DIST()` của Excel, chúng ta thu được `NORM.S.DIST((0.037 - 0.10)/0.12)` $= 29.98\%$, hay khoảng 30 phần trăm. Danh mục tối ưu theo tiêu chuẩn an toàn trên hết có khoảng 30 phần trăm khả năng không đạt được ngưỡng tỷ suất sinh lợi 3.7 phần trăm. 

2. Một khách hàng nắm giữ danh mục đầu tư trị giá GBP 2,000,000 muốn rút ra GBP 90,000 sau một năm mà không xâm phạm vào vốn gốc. Theo tiêu chuẩn an toàn trên hết của Roy, phương án phân bổ danh mục đầu tư nào sau đây là tối ưu? 

||**Phương án A (*Allocation A*)**|**Phương án B (*Allocation B*)**|**Phương án C (*Allocation C*)**|
|---|---|---|---|
|Tỷ suất sinh lợi hàng năm kỳ vọng (*Expected annual return*)|6.5%|7.5%|8.5%|
|Độ lệch chuẩn của tỷ suất sinh lợi (*Standard deviation of returns*)|8.35%|10.21%|14.34%|

   - **A.** Phương án A 

   - **B.** Phương án B 

   - **C.** Phương án C 

   - **Lời giải:** 

B là đáp án đúng. Phương án B có tỷ số an toàn trên hết cao nhất. Mức tỷ suất sinh lợi ngưỡng, $R_L$, đối với danh mục đầu tư là $\text{GBP } 90,000 / \text{GBP } 2,000,000 = 4.5\%$; do đó, bất kỳ mức tỷ suất sinh lợi nào nhỏ hơn $R_L = 4.5\%$ sẽ xâm phạm vào vốn gốc của danh mục đầu tư. Để tính toán phương án phân bổ tối ưu theo tiêu chuẩn an toàn trên hết, hãy chọn phương án có tỷ số cao nhất: 

![](assets/Quantitative_method.pdf-0178-13.png)

<!-- Formula Text: [E(R P − R L)] _ σ P . Allocation A  =   6.5 − 4.5 _ 8.35    =  0.240. Allocation B  =   7.5 − 4.5 _ 10.21    =  0.294. Allocation C  =   8.5 − 4.5 _ 14.34    =  0.279. -->

$$\frac{E(R_P) - R_L}{\sigma_P}$$

$$\text{Phương án A} = \frac{6.5 - 4.5}{8.35} = 0.240$$

$$\text{Phương án B} = \frac{7.5 - 4.5}{10.21} = 0.294$$

$$\text{Phương án C} = \frac{8.5 - 4.5}{14.34} = 0.279$$


<!-- PDF Page 179 -->

## **TÀI LIỆU THAM KHẢO (*REFERENCES*)** 

Roy, A. D. 1952. “Safety First and the Holding of Assets.” _Econometrica_ 20 (3): 431–49. 10.2307/1907413 


<!-- PDF Page 180 -->

## **BÀI TẬP THỰC HÀNH (*PRACTICE PROBLEMS*)** 

**1.** Một chuyên viên phân tích lập hàm xác suất đồng thời (*joint probability function*) sau đây cho một chỉ số nước ngoài (FI) và một chỉ số trong nước (DI). 

||**$R_{\text{DI}} = 30\%$**|**$R_{\text{DI}} = 25\%$**|**$R_{\text{DI}} = 15\%$**|
|---|---|---|---|
|$R_{\text{FI}} = 25\%$|0.25|||
|$R_{\text{FI}} = 15\%$||0.50||
|$R_{\text{FI}} = 10\%$|||0.25|

Hiệp phương sai của tỷ suất sinh lợi trên chỉ số nước ngoài và tỷ suất sinh lợi trên chỉ số trong nước _gần nhất_ với: 

   - **A.** 26.39. 

   - **B.** 26.56. 

   - **C.** 28.12. 


<!-- PDF Page 181 -->

## **LỜI GIẢI (*SOLUTIONS*)** 

1. B là đáp án đúng. Hiệp phương sai là 26.56, được tính như sau. Trước tiên, tỷ suất sinh lợi kỳ vọng là $E(R_{\text{FI}}) = (0.25 \times 25) + (0.50 \times 15) + (0.25 \times 10) = 6.25 + 7.50 + 2.50 = 16.25$ và $E(R_{\text{DI}}) = (0.25 \times 30) + (0.50 \times 25) + (0.25 \times 15) = 7.50 + 12.50 + 3.75 = 23.75$. Hiệp phương sai là: 

$$\text{Cov}(R_{\text{FI}}, R_{\text{DI}}) = \sum_{i} \sum_{j} P(R_{\text{FI},i}, R_{\text{DI},j})(R_{\text{FI},i} - ER_{\text{FI}})(R_{\text{DI},j} - ER_{\text{DI}})$$

$$= 0.25[(25 - 16.25)(30 - 23.75)] + 0.50[(15 - 16.25)(25 - 23.75)] + 0.25[(10 - 16.25)(15 - 23.75)]$$

$$= 13.67 + (-0.78) + 13.67 = 26.56$$


<!-- PDF Page 182 -->
