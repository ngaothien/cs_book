# Tập 9: Quản lý Danh mục Đầu tư (*Volume 9: Portfolio Management*)
## Học phần 2: Rủi ro và Tỷ suất sinh lợi của Danh mục Đầu tư: Phần II (*Learning Module 2: Portfolio Risk and Return: Part II*)
### Phần 1/4: Giới thiệu (*Introduction*) (Trang PDF 71–86)

---

<!-- PDF Page 71 -->

#### H Ọ C P H Ầ N (*L E A R N I N G M O D U L E*)

# **<mark>2</mark>** 

### **Rủi ro và Tỷ suất sinh lợi của Danh mục Đầu tư: Phần II (*Portfolio Risk and Return: Part II*)** 

###### **Bởi Vijay Singal, PhD, CFA.** 

_Vijay Singal, PhD, CFA, công tác tại Đại học Công nghệ Virginia – Virginia Tech (Hoa Kỳ)._ 

|**MỤC TIÊU**|**HỌC TẬP (*LEARNING OUTCOMES*)**|
|---|---|
|**_Mức độ thành thạo_**|**_Ứng viên cần có khả năng:_**|
||mô tả hệ quả của việc kết hợp một tài sản phi rủi ro với một danh mục các tài sản rủi ro (*describe the implications of combining a risk-free asset with a portfolio of risky assets*)|
||giải thích đường phân bổ vốn (*capital allocation line* – CAL) và đường thị trường vốn (*capital market line* – CML)|
||giải thích rủi ro hệ thống (*systematic risk*) và rủi ro phi hệ thống (*nonsystematic risk*), bao gồm lý do tại sao một nhà đầu tư không nên kỳ vọng nhận thêm tỷ suất sinh lợi khi gánh chịu rủi ro phi hệ thống|
||giải thích các mô hình tạo tỷ suất sinh lợi (*return generating models*, bao gồm cả mô hình thị trường – *market model*) và công dụng của chúng|
||tính toán và diễn giải hệ số beta (*calculate and interpret beta*)|
||giải thích mô hình định giá tài sản vốn (*capital asset pricing model* – CAPM), bao gồm các giả định của mô hình, và đường thị trường chứng khoán (*security market line* – SML)|
||tính toán và diễn giải tỷ suất sinh lợi kỳ vọng (*expected return*) của một tài sản bằng cách sử dụng CAPM|
||mô tả và minh họa các ứng dụng của CAPM và SML|
||tính toán và diễn giải tỷ số Sharpe (*Sharpe ratio*), tỷ số Treynor (*Treynor ratio*), $M^2$, và alpha của Jensen (*Jensen’s alpha*)|

![](assets/Portfolio_Management.pdf-0071-07.png)

<!-- Picture Text: 1<br> -->

##### **GIỚI THIỆU (*INTRODUCTION*)** 

Mục tiêu của chúng ta trong bài đọc này là xác định danh mục đầu tư rủi ro tối ưu (*optimal risky portfolio*) cho tất cả các nhà đầu tư bằng cách sử dụng mô hình định giá tài sản vốn (*capital asset pricing model* – CAPM). Nền tảng của bài đọc này là việc tính toán rủi ro và tỷ suất sinh lợi của một danh mục đầu tư cũng như vai trò của hệ số tương quan (*correlation*) trong việc đa dạng hóa rủi ro danh mục (*diversifying portfolio risk*) và đạt đến đường biên hiệu quả (*efficient frontier*). Đường biên hiệu quả và đường phân bổ vốn (*capital allocation line* – CAL) bao gồm các danh mục đầu tư nhìn chung được chấp nhận 


<!-- PDF Page 72 -->

đối với tất cả các nhà đầu tư. Bằng cách kết hợp các đường bàng quan (*indifference curves*) cá nhân của một nhà đầu tư với đường phân bổ vốn do thị trường xác định, chúng ta có thể minh họa rằng danh mục rủi ro tối ưu duy nhất cho một nhà đầu tư là danh mục bao gồm tất cả các tài sản rủi ro (tức là thị trường – *the market*). 

Ngoài ra, chúng ta thảo luận về đường thị trường vốn (*capital market line* – CML), một trường hợp đặc biệt của đường phân bổ vốn được sử dụng cho các danh mục của nhà đầu tư thụ động (*passive investor portfolios*). Chúng ta cũng phân biệt giữa rủi ro hệ thống (*systematic risk*) và rủi ro phi hệ thống (*nonsystematic risk*), đồng thời giải thích tại sao các nhà đầu tư được đền bù khi gánh chịu rủi ro hệ thống nhưng lại không nhận được sự đền bù nào khi gánh chịu rủi ro phi hệ thống. Chúng ta thảo luận chi tiết về CAPM, một mô hình đơn giản để ước tính tỷ suất sinh lợi của tài sản chỉ dựa trên rủi ro hệ thống của tài sản đó. Cuối cùng, chúng ta minh họa cách CAPM cho phép lựa chọn chứng khoán (*security selection*) để xây dựng một danh mục đầu tư tối ưu cho nhà đầu tư bằng cách thay đổi cơ cấu tài sản vượt ra ngoài một danh mục thị trường thụ động. 

Bài đọc được cấu trúc như sau. Trong Phần 2, chúng ta thảo luận về các hệ quả của việc kết hợp một tài sản phi rủi ro với danh mục thị trường và đưa ra cách diễn giải về đường thị trường vốn. Phần 3 phân rã tổng rủi ro (*total risk*) thành rủi ro hệ thống và rủi ro phi hệ thống, đồng thời thảo luận về đặc điểm và sự khác biệt giữa hai loại rủi ro này. Chúng ta cũng giới thiệu các mô hình tạo tỷ suất sinh lợi (*return-generating models*), bao gồm mô hình đơn chỉ số (*single-index model*), và minh họa cách tính hệ số beta. Trong Phần 4, chúng ta giới thiệu mô hình định giá tài sản vốn và đường thị trường chứng khoán (*security market line* – SML). Việc chúng ta tập trung vào CAPM không có nghĩa là CAPM là mô hình định giá tài sản khả thi duy nhất. Mặc dù CAPM là một điểm khởi đầu xuất sắc, các bài đọc nâng cao hơn sẽ mở rộng những thảo luận này và phát triển phân tích sang các mô hình khác có tính đến nhiều nhân tố giải thích (*multiple explanatory factors*). Phần 5 đề cập đến một số phát triển lý thuyết hậu CAPM. Phần 6 trình bày các thước đo đánh giá hiệu quả hoạt động của danh mục đầu tư có tính đến yếu tố rủi ro. Phần 7 trình bày một số ứng dụng của CAPM trong việc xây dựng danh mục đầu tư (*portfolio construction*). Phần tóm tắt và các bài tập thực hành sẽ khép lại bài đọc. 

## **<mark>2</mark>** 

##### **LÝ THUYẾT THỊ TRƯỜNG VỐN: TÀI SẢN PHI RỦI RO VÀ TÀI SẢN RỦI RO (*CAPITAL MARKET THEORY: RISK-FREE AND RISKY ASSETS*)** 

mô tả hệ quả của việc kết hợp một tài sản phi rủi ro với một danh mục các tài sản rủi ro (*describe the implications of combining a risk-free asset with a portfolio of risky assets*)

giải thích đường phân bổ vốn (*capital allocation line* – CAL) và đường thị trường vốn (*capital market line* – CML)

Bạn đã học cách kết hợp một tài sản phi rủi ro với một tài sản rủi ro và với nhiều tài sản rủi ro để tạo ra một đường phân bổ vốn (*capital allocation line* – CAL). Trong phần này, chúng ta sẽ mở rộng thảo luận về nhiều tài sản rủi ro và xem xét một trường hợp đặc biệt của đường phân bổ vốn, được gọi là đường thị trường vốn (*capital market line* – CML). Trong khi thảo luận về đường thị trường vốn, chúng ta sẽ định nghĩa thị trường và vai trò của nó trong quản lý danh mục đầu tư thụ động (*passive portfolio management*). Sử dụng các khái niệm này, chúng ta sẽ minh họa cách các danh mục đầu tư có sử dụng đòn bẩy (*leveraged portfolios*) có thể làm gia tăng cả rủi ro lẫn tỷ suất sinh lợi. 

###### **Danh mục gồm Tài sản Phi rủi ro và Tài sản Rủi ro (*Portfolio of Risk-Free and Risky Assets*)** 

Mặc dù các nhà đầu tư luôn mong muốn một tài sản mang lại tỷ suất sinh lợi cao nhất và có rủi ro thấp nhất, nhưng một tài sản như vậy không tồn tại. Như lý thuyết thị trường vốn về rủi ro – tỷ suất sinh lợi đã minh họa, một người phải chấp nhận rủi ro cao hơn để kiếm được tỷ suất sinh lợi cao hơn. Tuy nhiên, chúng ta có thể cải thiện danh mục đầu tư của một nhà đầu tư bằng cách mở rộng tập hợp cơ hội (*opportunity set*) của các tài sản rủi ro vì điều này cho phép nhà đầu tư lựa chọn một cơ cấu tài sản vượt trội hơn. 


<!-- PDF Page 73 -->

Tương tự, danh mục đầu tư của một nhà đầu tư sẽ được cải thiện nếu một tài sản phi rủi ro được thêm vào cơ cấu. Nói cách khác, sự kết hợp giữa tài sản phi rủi ro và một tài sản rủi ro có thể mang lại sự đánh đổi rủi ro – tỷ suất sinh lợi (*risk–return trade-off*) tốt hơn so với việc chỉ đầu tư vào một loại tài sản duy nhất bởi vì tài sản phi rủi ro có độ tương quan bằng không (*zero correlation*) với tài sản rủi ro. Sự kết hợp này được gọi là **đường phân bổ vốn (*capital allocation line* – CAL)** (và được minh họa trong Bảng minh họa 2). Việc chồng các đường bàng quan (*indifference curves*) của nhà đầu tư lên đường phân bổ vốn sẽ dẫn đến danh mục đầu tư tối ưu của nhà đầu tư (*optimal investor portfolio*). 

Các nhà đầu tư với mức độ ngại rủi ro (*risk aversion*) khác nhau sẽ chọn các danh mục đầu tư khác nhau. Những nhà đầu tư rất ngại rủi ro (*highly risk-averse investors*) chọn đầu tư phần lớn tài sản của họ vào tài sản phi rủi ro và kiếm được tỷ suất sinh lợi thấp vì họ không sẵn lòng chấp nhận mức rủi ro cao hơn. Ngược lại, những nhà đầu tư ít ngại rủi ro hơn (*less risk-averse investors*) sẽ đầu tư nhiều tài sản của họ hơn vào tài sản rủi ro, vốn được kỳ vọng sẽ mang lại tỷ suất sinh lợi cao hơn. Hiển nhiên, tỷ suất sinh lợi cao hơn không thể đi kèm mà không có rủi ro cao hơn, nhưng nhà đầu tư ít ngại rủi ro sẵn sàng chấp nhận phần rủi ro tăng thêm đó. 

###### **_Kết hợp một Tài sản Phi rủi ro với một Danh mục các Tài sản Rủi ro (Combining a Risk-Free Asset with a Portfolio of Risky Assets)_** 

Chúng ta có thể mở rộng phân tích từ một tài sản rủi ro sang một danh mục gồm nhiều tài sản rủi ro. Để thuận tiện, giả sử rằng danh mục đầu tư chứa tất cả các tài sản rủi ro hiện có ($N$), mặc dù một nhà đầu tư có thể không muốn đưa tất cả các tài sản này vào danh mục vì sở thích cụ thể của mình. Nếu một tài sản không được đưa vào danh mục đầu tư, tỷ trọng (*weight*) của nó sẽ bằng không. Các đặc điểm rủi ro – tỷ suất sinh lợi của một danh mục gồm $N$ tài sản rủi ro được cho bởi các phương trình sau: 

![](assets/Portfolio_Management.pdf-0073-07.png)

$$E(R_p) = \sum_{i=1}^{N} w_i E(R_i)$$

$$\sigma_p^2 = \left( \sum_{i=1, j=1}^{N} w_i w_j \text{Cov}(i, j) \right), \quad \text{và} \quad \sum_{i=1}^{N} w_i = 1$$

<!-- Formula Text: E (R p)   =  ∑ i=1 N w i E (R i) σ p 2  =   (  ∑ i=1,j=1 N w i w j Cov (i, j) ) ,  and ∑ i=1 N w i  =  1 -->

Tỷ suất sinh lợi kỳ vọng của danh mục đầu tư, $E(R_p)$, là trung bình có trọng số của tỷ suất sinh lợi kỳ vọng của từng tài sản riêng lẻ, trong đó $w_i$ là tỷ trọng phân bổ vào tài sản $i$ và $E(R_i)$ là tỷ suất sinh lợi kỳ vọng của tài sản $i$. Tuy nhiên, rủi ro của danh mục đầu tư ($\sigma_p$) phụ thuộc vào tỷ trọng của từng tài sản riêng lẻ, rủi ro của từng tài sản riêng lẻ, và mối tương quan qua lại giữa chúng. **Hiệp phương sai (*covariance*)** giữa tài sản $i$ và $j$, $\text{Cov}(i, j)$, là một thước đo thống kê về mối quan hệ qua lại giữa từng cặp tài sản trong danh mục và có thể được biểu diễn như sau, trong đó $\rho_{ij}$ là **hệ số tương quan (*correlation*)** giữa tài sản $i$ và $j$, còn $\sigma_i$ là rủi ro của tài sản $i$: 

$$\text{Cov}(i, j) = \rho_{ij}\sigma_i\sigma_j$$

Lưu ý từ phương trình dưới đây rằng hệ số tương quan của một tài sản với chính nó bằng 1; do đó: 

$$\text{Cov}(i, i) = \rho_{ii}\sigma_i\sigma_i = \sigma_i^2$$

Bằng cách thay thế các biểu thức hiệp phương sai ở trên, chúng ta có thể viết lại phương trình phương sai của danh mục đầu tư (*portfolio variance*) như sau: 

![](assets/Portfolio_Management.pdf-0073-13.png)

$$\sigma_p^2 = \left( \sum_{i=1}^{N} w_i^2 \sigma_i^2 + \sum_{i, j=1, i \neq j}^{N} w_i w_j \rho_{ij} \sigma_i \sigma_j \right)$$

<!-- Formula Text: σ p 2  =   (∑ i=1 N w i 2 σ i 2 +   ∑ i,j=1,i≠j N w i w j ρ ij σ i σ j) -->

Nhận định cho rằng các danh mục đầu tư có rủi ro thấp hơn các tài sản mà chúng nắm giữ có vẻ trái với trực giác. Tuy nhiên, những danh mục như vậy hoàn toàn có thể được xây dựng miễn là các tài sản trong danh mục không tương quan hoàn toàn (*not perfectly correlated*) với nhau. Để minh họa tác động của tỷ trọng tài sản lên các đặc điểm của danh mục đầu tư, hãy xem xét một danh mục đơn giản gồm hai tài sản với tỷ trọng bằng không ở tất cả các tài sản khác. Giả sử Tài sản 1 có tỷ suất sinh lợi là 10% và độ lệch chuẩn (rủi ro) là 20%. Tài sản 2 có tỷ suất sinh lợi là 5% và độ lệch chuẩn (rủi ro) là 10%. Hơn nữa, hệ số tương quan giữa hai tài sản này bằng không. Bảng minh họa 1 cho thấy rủi ro và tỷ suất sinh lợi của Danh mục X với tỷ trọng 25% ở Tài sản 1 và 75% ở Tài sản 2, Danh mục Y với tỷ trọng 50% ở mỗi tài sản trong hai tài sản, và Danh mục Z với tỷ trọng 75% ở Tài sản 1 và 25% ở Tài sản 2. 


<!-- PDF Page 74 -->

**Bảng minh họa 1: Rủi ro và Tỷ suất sinh lợi của Danh mục Đầu tư (*Exhibit 1: Portfolio Risk and Return*)** 

|**Danh mục (*Portfolio*)**|**Tỷ trọng ở Tài sản 1 (*Weight in Asset 1*) (%)**|**Tỷ trọng ở Tài sản 2 (*Weight in Asset 2*) (%)**|**Tỷ suất sinh lợi Danh mục (*Portfolio Return*) (%)**|**Độ lệch chuẩn Danh mục (*Portfolio Standard Deviation*) (%)**|
|---|---|---|---|---|
|X|25.0|75.0|6.25|9.01|
|Y|50.0|50.0|7.50|11.18|
|Z|75.0|25.0|8.75|15.21|
|Tỷ suất sinh lợi (*Return*)|10.0|5.0|||
|Độ lệch chuẩn (*Standard deviation*)|20.0|10.0|||
|Hệ số tương quan giữa Tài sản 1 và 2 (*Correlation between Assets 1 and 2*)||0.0|||

Từ ví dụ này, chúng ta quan sát thấy rằng ba danh mục đầu tư khá khác biệt nhau về mặt rủi ro và tỷ suất sinh lợi. Danh mục X có tỷ suất sinh lợi 6.25% và độ lệch chuẩn chỉ 9.01%, trong khi độ lệch chuẩn của Danh mục Z cao hơn tới hơn hai phần ba (15.21%), mặc dù tỷ suất sinh lợi chỉ cao hơn một chút so với mức một phần ba (8.75%). Các danh mục này có thể trở nên khác biệt hơn nữa khi các tài sản khác được thêm vào cơ cấu. 

Hãy xem xét ba danh mục tài sản rủi ro A, B và C như trong Bảng minh họa 2, có thể đã được ba cố vấn đầu tư khác nhau giới thiệu cho một nhà đầu tư đại diện. Mỗi danh mục được kết hợp với tài sản phi rủi ro để tạo ra ba đường phân bổ vốn: CAL(A), CAL(B) và CAL(C). Bảng minh họa cho thấy Danh mục C vượt trội hơn hai danh mục còn lại vì nó có tỷ suất sinh lợi kỳ vọng lớn hơn tại bất kỳ mức rủi ro cho trước nào. Kết quả là, nhà đầu tư sẽ chọn danh mục nằm trên đường phân bổ vốn của Danh mục C. Sự kết hợp giữa tài sản phi rủi ro và Danh mục rủi ro C được lựa chọn cho một nhà đầu tư phụ thuộc vào mức độ ngại rủi ro của nhà đầu tư đó. 

**Bảng minh họa 2: Tài sản Phi rủi ro và Danh mục các Tài sản Rủi ro (*Exhibit 2: Risk-Free Asset and Portfolio of Risky Assets*)** 

![](assets/Portfolio_Management.pdf-0074-08.png)

<!-- Picture Text: Indifference CAL(C)<br>Curve<br>C CAL(B)<br>CAL(A)<br>B<br>A<br>Rf<br>Expected Portfolio Return ()  ER p<br> -->

> **Chú thích hình ảnh:** Trục tung: Tỷ suất sinh lợi kỳ vọng của danh mục $E(R_p)$ (*Expected Portfolio Return*); Trục hoành: Độ lệch chuẩn của danh mục $\sigma_p$ (*Portfolio Standard Deviation*). Các đường trên đồ thị gồm: Đường bàng quan (*Indifference Curve*), các đường phân bổ vốn $\text{CAL(C)}$, $\text{CAL(B)}$, $\text{CAL(A)}$ đi qua lãi suất phi rủi ro $R_f$ và các danh mục tương ứng $C$, $B$, $A$.

Độ lệch chuẩn của Danh mục (*Portfolio Standard Deviation*) ($\sigma_p$) 


<!-- PDF Page 75 -->

###### **_Liệu có Tồn tại một Danh mục Rủi ro Tối ưu Duy nhất? (Does a Unique Optimal Risky Portfolio Exist?)_** 

Chúng ta giả định rằng tất cả các nhà đầu tư đều có cùng kỳ vọng kinh tế và do đó có cùng kỳ vọng về giá cả, dòng tiền và các đặc điểm đầu tư khác. Giả định này được gọi là **tính đồng nhất của kỳ vọng (*homogeneity of expectations*)**. Với những đặc điểm đầu tư này, mọi người đều thực hiện cùng một quá trình tính toán và sẽ đi đến cùng một danh mục rủi ro tối ưu. Do đó, nếu giả định kỳ vọng đồng nhất, chỉ có duy nhất một danh mục tối ưu tồn tại. Tuy nhiên, nếu các nhà đầu tư có những kỳ vọng khác nhau, họ có thể đi đến các danh mục rủi ro tối ưu khác nhau. Để minh họa, chúng ta bắt đầu với biểu thức tính giá của một tài sản: 

![](assets/Portfolio_Management.pdf-0075-04.png)

$$P = \sum_{t=0}^{T} \frac{CF_t}{(1 + r_t)^t}$$

<!-- Formula Text: P  =  ∑ t=0 T CF t _ (1 + r t) t -->

trong đó $CF_t$ là dòng tiền tại thời điểm cuối kỳ $t$ và $r_t$ là lãi suất chiết khấu (*discount rate*) hay tỷ suất sinh lợi yêu cầu (*required rate of return*) đối với tài sản đó trong kỳ $t$. Kỳ $t$ đề cập đến tất cả các kỳ bắt đầu từ hiện tại cho đến khi tài sản ngừng tồn tại vào cuối thời điểm $T$. Bởi vì thời điểm hiện tại là cuối kỳ 0, cũng chính là đầu kỳ 1, nên có $(T + 1)$ dòng tiền và $(T + 1)$ tỷ suất sinh lợi yêu cầu. Các điều kiện này dựa trên giả định rằng một dòng tiền, chẳng hạn như khoản đầu tư ban đầu, có thể xảy ra ngay bây giờ ($t = 0$). Tuy nhiên, thông thường $CF_0$ bằng không. 

Chúng ta sử dụng công thức tính giá tài sản để ước tính giá trị nội tại (*intrinsic value*) của một tài sản. Giả sử rằng tài sản chúng ta đang định giá là một cổ phiếu của Siemens AG được giao dịch trên sàn Xetra. Trong trường hợp cổ phiếu công ty, không có ngày đáo hạn, vì vậy $T$ có thể cực kỳ lớn, nghĩa là chúng ta sẽ cần ước tính một số lượng lớn các dòng tiền và tỷ suất sinh lợi. May mắn thay, mẫu số làm giảm tầm quan trọng của các dòng tiền ở xa trong tương lai, vì vậy có thể chỉ cần ước tính, chẳng hạn, 20 dòng tiền hàng năm và 20 tỷ suất sinh lợi là đủ. Siemens sẽ kiếm được bao nhiêu vào năm tới và năm sau nữa? Thị trường sản phẩm mà Siemens hoạt động sẽ trông như thế nào sau 5 năm nữa? Các nhà phân tích và nhà đầu tư khác nhau sẽ có những ước tính của riêng họ và chúng có thể rất khác nhau. Ngoài ra, khi chúng ta đi sâu hơn vào tương lai, những vấn đề nghiêm trọng hơn trong việc ước tính doanh thu, chi phí và tốc độ tăng trưởng tương lai sẽ phát sinh. Do đó, việc giả định rằng các ước tính dòng tiền cho Siemens sẽ khác nhau giữa các nhà đầu tư này là hoàn toàn hợp lý. Ngoài tử số (dòng tiền), chúng ta còn cần phải ước tính mẫu số, tức các tỷ suất sinh lợi yêu cầu. Chúng ta biết rằng các công ty rủi ro hơn sẽ đòi hỏi tỷ suất sinh lợi cao hơn vì rủi ro và tỷ suất sinh lợi có tương quan dương. Cổ phiếu Siemens rủi ro hơn một tài sản phi rủi ro, nhưng rủi ro hơn bao nhiêu? Và mức đền bù cho phần rủi ro tăng thêm đó nên là bao nhiêu? Một lần nữa, hiển nhiên là các nhà phân tích khác nhau sẽ nhìn nhận mức độ rủi ro của Siemens theo cách khác nhau và do đó, đi đến các tỷ suất sinh lợi yêu cầu khác nhau. 

Cổ phiếu Siemens đóng cửa ở mức €111.84 trên sàn Xetra vào ngày 31 tháng 8 năm 2018. Mức giá giao dịch đại diện cho giá trị mà một nhà đầu tư cận biên (*marginal investor*) gắn cho một cổ phiếu của Siemens, giả sử tương ứng với kỳ vọng của Nhà phân tích A. Tuy nhiên, Nhà phân tích B có thể nghĩ rằng mức giá nên là €95, và Nhà phân tích C có thể nghĩ rằng mức giá nên là €125. Với mức giá €111.84, tỷ suất sinh lợi kỳ vọng của Siemens là khá khác nhau đối với ba nhà phân tích. Nhà phân tích B, người tin rằng giá nên là €95, kết luận rằng Siemens đang được định giá quá cao (*overvalued*) và có thể gán tỷ trọng bằng 0 cho Siemens trong danh mục khuyến nghị mặc dù vốn hóa thị trường (*market capitalization*) của Siemens vượt quá €100 tỷ tại ngày báo giá. Ngược lại, Nhà phân tích C, với mức định giá €125, cho rằng Siemens đang bị định giá thấp (*undervalued*) và có thể phân bổ tỷ trọng lớn (*overweight*) đáng kể cho Siemens trong danh mục đầu tư. 

Cuộc thảo luận của chúng ta minh họa rằng các nhà phân tích có thể đi đến những mức định giá khác nhau, đòi hỏi việc phân bổ các tỷ trọng tài sản khác nhau trong một danh mục đầu tư. Với sự tồn tại của nhiều loại tài sản (*asset classes*) và vô số tài sản trong mỗi loại tài sản, người ta có thể hình dung rằng mỗi nhà đầu tư sẽ có danh mục rủi ro tối ưu của riêng mình tùy thuộc vào các giả định cơ sở trong tính toán định giá của họ. Do đó, những người tham gia thị trường sẽ có các danh mục rủi ro tối ưu của riêng họ và có thể khác biệt nhau. 


<!-- PDF Page 76 -->

Nếu các nhà đầu tư có các định giá tài sản khác nhau, thì việc xây dựng một danh mục rủi ro tối ưu duy nhất là không thể. Nếu chúng ta đưa ra một giả định đơn giản hóa về tính đồng nhất trong kỳ vọng của nhà đầu tư (*homogeneity in investor expectations*), chúng ta sẽ có một danh mục rủi ro tối ưu duy nhất như đã đề cập trước đó. Ngay cả khi các nhà đầu tư có những kỳ vọng khác nhau, giá thị trường vẫn là một đại diện (*proxy*) cho những gì mà nhà đầu tư cận biên, có đầy đủ thông tin kỳ vọng, và danh mục thị trường (*market portfolio*) sẽ trở thành trường hợp cơ sở, chuẩn tham chiếu (*benchmark*), hay danh mục tham chiếu mà các danh mục khác có thể được đem ra so sánh và đánh giá. Đối với Siemens, giá thị trường là €111.84 mỗi cổ phiếu và vốn hóa thị trường vào khoảng €108 tỷ. Khi xây dựng danh mục thị trường, tỷ trọng của Siemens trong danh mục thị trường sẽ bằng giá trị thị trường của nó chia cho tổng giá trị của tất cả các tài sản khác được đưa vào danh mục thị trường. 

## **<mark>3</mark>** 

##### **LÝ THUYẾT THỊ TRƯỜNG VỐN: ĐƯỜNG THỊ TRƯỜNG VỐN (*CAPITAL MARKET THEORY: THE CAPITAL MARKET LINE*)** 

giải thích đường phân bổ vốn (*capital allocation line* – CAL) và đường thị trường vốn (*capital market line* – CML)

Trong phần trước, chúng ta đã thảo luận về cách tài sản phi rủi ro có thể được kết hợp với một danh mục rủi ro để tạo ra đường phân bổ vốn (CAL). Trong phần này, chúng ta thảo luận về một đường CAL cụ thể sử dụng danh mục thị trường làm danh mục rủi ro tối ưu và được gọi là đường thị trường vốn (*capital market line* – CML). Chúng ta cũng thảo luận về ý nghĩa của danh mục thị trường và các ứng dụng của đường thị trường vốn (CML). 

###### **Danh mục Đầu tư Thụ động và Chủ động (*Passive and Active Portfolios*)** 

Trong tiểu mục trên, chúng ta đã giả định ba mức định giá khả dĩ cho mỗi cổ phiếu của Siemens: €95, €111.84 và €125. Mức định giá nào là đúng? 

Nếu thị trường là một **thị trường hiệu quả về mặt thông tin (*informationally efficient market*)**, thì mức giá trên thị trường, €111.84, là một ước tính không chệch (*unbiased estimate*) của tất cả các dòng tiền chiết khấu trong tương lai (hãy nhớ lại công thức tính giá của một tài sản). Nói cách khác, mức giá đã tổng hợp và phản ánh tất cả các thông tin được công bố rộng rãi, và các nhà đầu tư không thể kỳ vọng kiếm được mức tỷ suất sinh lợi lớn hơn tỷ suất sinh lợi yêu cầu đối với tài sản đó. Tuy nhiên, nếu mức giá đã phản ánh tất cả thông tin công khai sẵn có và không có cách nào để chiến thắng thị trường (*outperform the market*), thì chẳng có mấy ý nghĩa khi bỏ thời gian và tiền bạc vào việc đánh giá Siemens để tìm ra mức giá của riêng bạn bằng cách sử dụng các ước tính dòng tiền và tỷ suất sinh lợi của chính bạn. 

Trong trường hợp đó, một cách tiếp cận đơn giản và thuận tiện để đầu tư là dựa vào mức giá do thị trường thiết lập. Các danh mục đầu tư dựa trên giả định về giá thị trường không chệch được gọi là danh mục đầu tư thụ động (*passive portfolios*). Các danh mục thụ động phổ biến nhất là sao chép và bám sát (*replicate and track*) các chỉ số thị trường (*market indexes*), vốn được xây dựng một cách thụ động dựa trên giá thị trường và vốn hóa thị trường. Ví dụ về các chỉ số thị trường là Chỉ số S&P 500, Nikkei 300 và CAC 40. Các danh mục đầu tư thụ động dựa trên các chỉ số thị trường được gọi là quỹ chỉ số (*index funds*) và nhìn chung có chi phí thấp vì không cần bỏ ra nỗ lực đáng kể nào trong việc định giá các chứng khoán nằm trong chỉ số. 

Trái ngược với sự phụ thuộc của các nhà đầu tư thụ động vào giá thị trường và các quỹ chỉ số, các nhà đầu tư chủ động (*active investors*) có thể không dựa vào định giá của thị trường. Họ tự tin hơn vào khả năng của bản thân trong việc ước tính dòng tiền, tốc độ tăng trưởng và lãi suất chiết khấu. Dựa trên những ước tính này, họ định giá tài sản và xác định xem liệu một tài sản có được định giá hợp lý (*fairly valued*) hay không. Trong một danh mục đầu tư được quản lý chủ động (*actively managed portfolio*), các tài sản đang bị định giá thấp (*undervalued*), hoặc có cơ hội mang lại tỷ suất sinh lợi cao hơn mức bình thường, sẽ có tỷ trọng dương (tức là phân bổ tỷ trọng cao hơn – *overweight* so với tỷ trọng thị trường trong chỉ số chuẩn), trong khi các tài sản khác sẽ có tỷ trọng bằng không, 


<!-- PDF Page 77 -->

hoặc thậm chí là tỷ trọng âm nếu việc bán khống (*short selling*) được cho phép (tức là một số tài sản sẽ được phân bổ tỷ trọng thấp hơn – *underweighted* so với tỷ trọng thị trường trong chỉ số chuẩn). (**Bán khống (*Short selling*)** là một giao dịch trong đó các chứng khoán đi vay được bán ra với ý định mua lại chúng ở mức giá thấp hơn vào một ngày sau đó và hoàn trả lại cho bên cho vay.) Phong cách đầu tư này được gọi là quản lý đầu tư chủ động (*active investment management*), và các danh mục đầu tư được gọi là danh mục đầu tư chủ động (*active portfolios*). Hầu hết các quỹ tương hỗ mở (*open-end mutual funds*) và quỹ phòng hộ (*hedge funds*) đều thực hành quản lý đầu tư chủ động, và hầu hết các nhà phân tích đều tin rằng đầu tư chủ động mang lại giá trị gia tăng. Việc các nhà phân tích này đúng hay sai vẫn là chủ đề của những cuộc tranh luận chưa có hồi kết. 

###### **“Thị trường” là gì? (*What Is the “Market”?*)** 

Trong phần thảo luận trước, chúng ta đã đề cập đến “thị trường” (*the “market”*) nhiều lần mà chưa thực sự định nghĩa nó. Danh mục rủi ro tối ưu và đường thị trường vốn phụ thuộc vào định nghĩa về thị trường. Vậy thị trường là gì? 

Về mặt lý thuyết, thị trường bao gồm tất cả các tài sản rủi ro hoặc bất cứ thứ gì có giá trị, bao gồm cổ phiếu, trái phiếu, bất động sản và thậm chí cả vốn nhân lực (*human capital*). Tuy nhiên, không phải tất cả các tài sản đều có thể giao dịch được (*tradable*), và không phải tất cả các tài sản có thể giao dịch đều có thể đầu tư được (*investable*). Ví dụ, đền Taj Mahal ở Ấn Độ là một tài sản nhưng không phải là một tài sản có thể giao dịch. Tương tự, vốn nhân lực là một tài sản không thể giao dịch. Hơn nữa, các tài sản có thể giao dịch được nhưng lại không thể đầu tư được do các hạn chế áp đặt lên một số đối tượng nhà đầu tư nhất định. Ví dụ, tất cả các cổ phiếu niêm yết trên Sở Giao dịch Chứng khoán Thượng Hải đều có thể giao dịch. Tuy nhiên, trong khi cổ phiếu Hạng A (*Class A shares*) được niêm yết bằng đồng Nhân dân tệ (RMB) và mở cửa cho các nhà đầu tư trong nước cùng các nhà đầu tư nước ngoài đủ điều kiện, thì cổ phiếu Hạng B (*Class B shares*) được niêm yết bằng đồng USD và mở cửa cho các nhà đầu tư nước ngoài cùng các nhà đầu tư trong nước nắm giữ tài khoản giao dịch ngoại tệ. 

Nếu chúng ta xem xét tất cả cổ phiếu, trái phiếu, tài sản bất động sản, hàng hóa, v.v., có lẽ có đến hàng trăm nghìn tài sản có thể giao dịch và có thể đầu tư. “Thị trường” nên bao gồm càng nhiều tài sản càng tốt; chúng ta nhấn mạnh từ “có thể” (*possible*) bởi vì việc đưa tất cả các tài sản vào một danh mục rủi ro duy nhất là điều không thực tế. Mặc dù những tiến bộ trong công nghệ và sự kết nối liên thông giữa các thị trường đã giúp việc tiếp cận các thị trường cổ phiếu lớn trở nên dễ dàng hơn nhiều, chúng ta vẫn chưa thể dễ dàng đầu tư vào các loại tài sản khác như trái phiếu và bất động sản ngoại trừ ở những quốc gia phát triển nhất. 

Trong phần còn lại của bài đọc này, chúng ta sẽ định nghĩa “thị trường” theo nghĩa khá hẹp vì làm như vậy mang tính thực tiễn và thuận tiện. Thông thường, một chỉ số thị trường chứng khoán trong nước hoặc khu vực được sử dụng làm đại diện (*proxy*) cho thị trường do hoạt động giao dịch sôi động của cổ phiếu và vì thị trường trong nước hoặc khu vực là dễ quan sát nhất đối với các nhà đầu tư bản địa. Cho mục đích của chúng ta, chúng ta sẽ sử dụng Chỉ số S&P 500 làm đại diện cho thị trường. S&P 500 thường được các nhà phân tích sử dụng làm chuẩn tham chiếu (*benchmark*) cho hiệu quả hoạt động của thị trường trên toàn Hoa Kỳ. Nó bao gồm 500 cổ phiếu lớn nhất có trụ sở tại Hoa Kỳ, và các cổ phiếu này được tính tỷ trọng theo vốn hóa thị trường của chúng (giá nhân với số lượng cổ phiếu đang lưu hành). 

Tính đến giữa năm 2018, các cổ phiếu trong S&P 500 chiếm khoảng 80% tổng vốn hóa thị trường cổ phiếu tại Hoa Kỳ, và bởi vì thị trường chứng khoán Hoa Kỳ chiếm khoảng 40% thị trường thế giới, nên S&P 500 đại diện cho khoảng 32% lượng cổ phiếu được giao dịch công khai trên toàn cầu. Định nghĩa về thị trường của chúng ta không bao gồm các thị trường chứng khoán ngoài Hoa Kỳ, thị trường trái phiếu, bất động sản và nhiều loại tài sản khác; do đó, tỷ suất sinh lợi “thị trường” và phần bù rủi ro “thị trường” (*“market” risk premium*) lần lượt đề cập đến tỷ suất sinh lợi cổ phiếu Hoa Kỳ và phần bù rủi ro cổ phiếu Hoa Kỳ. Tuy nhiên, việc sử dụng đại diện này là đủ cho cuộc thảo luận của chúng ta, và tương đối dễ dàng để mở rộng sang bao gồm các tài sản có thể giao dịch khác. 

###### **Đường Thị trường Vốn (*The Capital Market Line* – CML)** 

Một đường phân bổ vốn (CAL) bao gồm tất cả các sự kết hợp khả dĩ giữa tài sản phi rủi ro và danh mục rủi ro tối ưu của một nhà đầu tư. **Đường thị trường vốn (*capital market line* – CML)** là một trường hợp đặc biệt của đường phân bổ vốn, trong đó danh mục rủi ro chính là danh mục thị trường (*market portfolio*). Tài sản phi rủi ro 


<!-- PDF Page 78 -->

là một chứng khoán nợ không có rủi ro vỡ nợ (*default risk*), không có rủi ro lạm phát (*inflation risk*), không có rủi ro thanh khoản (*liquidity risk*), không có rủi ro lãi suất (*interest rate risk*), và không có bất kỳ loại rủi ro nào khác. Tín phiếu Kho bạc Hoa Kỳ (*US Treasury bills*) thường được sử dụng làm đại diện cho tỷ suất sinh lợi phi rủi ro, $R_f$. 

Chỉ số S&P 500 là một đại diện của danh mục thị trường, vốn là danh mục rủi ro tối ưu. Do đó, tỷ suất sinh lợi kỳ vọng của danh mục rủi ro là tỷ suất sinh lợi kỳ vọng của thị trường, được biểu diễn là $E(R_m)$. Đường thị trường vốn được thể hiện trong Bảng minh họa 3, trong đó độ lệch chuẩn ($\sigma_p$), hay tổng rủi ro, nằm trên trục hoành ($x$) và tỷ suất sinh lợi kỳ vọng của danh mục, $E(R_p)$, nằm trên trục tung ($y$). Về mặt đồ thị, danh mục thị trường là điểm nằm trên đường biên hiệu quả Markowitz (*Markowitz efficient frontier*) nơi một đường thẳng kẻ từ tài sản phi rủi ro tiếp xúc (*tangent*) với đường biên hiệu quả Markowitz. Tất cả các điểm nằm phía bên trong đường biên hiệu quả Markowitz đều là các danh mục không hiệu quả (*inefficient portfolios*) ở chỗ chúng cung cấp cùng một mức tỷ suất sinh lợi nhưng với mức rủi ro cao hơn, hoặc mức tỷ suất sinh lợi thấp hơn với cùng một mức rủi ro. Khi được vẽ cùng nhau, tiếp điểm mà tại đó đường CML tiếp xúc với đường biên hiệu quả Markowitz chính là sự kết hợp tối ưu của các tài sản rủi ro, dựa trên giá thị trường và vốn hóa thị trường. Danh mục rủi ro tối ưu chính là danh mục thị trường. 

**Bảng minh họa 3: Đường Thị trường Vốn (*Exhibit 3: Capital Market Line*)** 

![](assets/Portfolio_Management.pdf-0078-07.png)

<!-- Picture Text: CML<br>Points above the<br>CML are not<br>achievable<br>Efficient<br>E ( Rm ) frontier<br>M<br>Individual<br>Securities<br>Rf<br>Standard Deviation of Portfolio σ p<br>Expected Portfolio Return ()  ER p<br> -->

> **Chú thích hình ảnh:** Trục tung: Tỷ suất sinh lợi kỳ vọng của danh mục $E(R_p)$; Trục hoành: Độ lệch chuẩn của danh mục $\sigma_p$. Đường thị trường vốn ($\text{CML}$) xuất phát từ $R_f$ và tiếp xúc với Đường biên hiệu quả (*Efficient frontier*) tại danh mục thị trường $M$ có tỷ suất sinh lợi kỳ vọng $E(R_m)$. Các điểm nằm phía trên đường CML là không thể đạt được (*Points above the CML are not achievable*), và phía dưới đường biên hiệu quả là các Chứng khoán riêng lẻ (*Individual Securities*).

Điểm cắt trục tung ($y$) của đường CML là tỷ suất sinh lợi phi rủi ro ($R_f$) bởi vì đó là mức tỷ suất sinh lợi gắn liền với rủi ro bằng không. Đường CML đi qua điểm được đại diện bởi tỷ suất sinh lợi thị trường, $E(R_m)$. Theo lý thuyết thị trường vốn, bất kỳ điểm nào nằm phía trên đường CML đều không thể đạt được (*not achievable*) và bất kỳ điểm nào nằm phía dưới đường CML đều bị lấn át (*dominated*) và kém ưu việt hơn (*inferior*) so với bất kỳ điểm nào nằm trên đường CML. 

Lưu ý rằng chúng ta xác định CML và CAL là các đường thẳng mặc dù chúng là sự kết hợp của hai tài sản. Không giống như sự kết hợp của hai tài sản rủi ro (thường không phải là một đường thẳng), sự kết hợp giữa tài sản phi rủi ro và một danh mục rủi ro là một đường thẳng, như được minh họa dưới đây thông qua việc tính toán rủi ro và tỷ suất sinh lợi của sự kết hợp này. 

Các đặc điểm rủi ro và tỷ suất sinh lợi của danh mục đầu tư được đại diện bởi đường CML có thể được tính toán bằng cách sử dụng các biểu thức tỷ suất sinh lợi và rủi ro cho danh mục gồm hai tài sản: 

$$E(R_p) = w_1 R_f + (1 - w_1) E(R_m),$$


<!-- PDF Page 79 -->

và 

![](assets/Portfolio_Management.pdf-0079-03.png)

$$\sigma_p = \sqrt{w_1^2 \sigma_f^2 + (1 - w_1)^2 \sigma_m^2 + 2 w_1 (1 - w_1) \text{Cov}(R_f, R_m)}$$

<!-- Formula Text: σ p  =  √ ___________________________________________ w 1 2 σ f 2 + (1 − w 1) 2 σ m 2  + 2 w 1 (1 − w 1) Cov (R f, R m) -->

Tỷ trọng đầu tư vào tài sản phi rủi ro được ký hiệu là $w_1$, và phần còn lại được đầu tư vào danh mục thị trường, $(1 - w_1)$. Rủi ro của tài sản phi rủi ro được ký hiệu là $\sigma_f$, rủi ro của thị trường là $\sigma_m$, rủi ro của danh mục đầu tư là $\sigma_p$, và hiệp phương sai giữa tài sản phi rủi ro và danh mục thị trường được biểu diễn bởi $\text{Cov}(R_f, R_m)$. Theo định nghĩa, độ lệch chuẩn của tài sản phi rủi ro bằng không. Bởi vì rủi ro của nó bằng không, tài sản phi rủi ro không đồng biến thiên (*co-vary*) hay biến động cùng với bất kỳ tài sản nào khác. Do đó, hiệp phương sai của nó với tất cả các tài sản khác, bao gồm cả danh mục thị trường, đều bằng không, làm cho số hạng thứ nhất và thứ ba dưới dấu căn bậc hai bằng không. Kết quả là, tỷ suất sinh lợi của danh mục và độ lệch chuẩn của danh mục có thể được rút gọn và viết lại như sau: 

$$E(R_p) = w_1 R_f + (1 - w_1) E(R_m),$$

và 

![](assets/Portfolio_Management.pdf-0079-07.png)

$$\sigma_p = (1 - w_1)\sigma_m$$

<!-- Formula Text: σp = (1 – w1)σm -->

Bằng phương pháp thế, chúng ta có thể biểu diễn $E(R_p)$ theo $\sigma_p$. Thay thế cho $w_1$, chúng ta nhận được: 

![](assets/Portfolio_Management.pdf-0079-09.png)

$$E(R_p) = R_f + \left( \frac{E(R_m) - R_f}{\sigma_m} \right) \times \sigma_p$$

<!-- Formula Text: E (R p)   =  R f +  ( E (R m)  − R f _ σ m )  × σ p -->

Lưu ý rằng biểu thức này có dạng phương trình đường thẳng, $y = a + bx$. Điểm cắt trục tung ($y$-intercept) là lãi suất phi rủi ro, và độ dốc (*slope*) của đường thẳng — được gọi là cái giá thị trường của rủi ro (*market price of risk*) — là $[E(R_m) - R_f]/\sigma_m$. Đường CML có độ dốc dương bởi vì tỷ suất sinh lợi rủi ro của thị trường lớn hơn tỷ suất sinh lợi phi rủi ro. Khi quy mô tổng vốn đầu tư dành cho thị trường tăng lên — tức là khi chúng ta di chuyển lên phía trên dọc theo đường thẳng — cả độ lệch chuẩn (rủi ro) và tỷ suất sinh lợi kỳ vọng đều tăng lên. 

###### **VÍ DỤ 1 (*EXAMPLE 1*)** 

###### **Rủi ro và Tỷ suất sinh lợi trên đường CML (*Risk and Return on the CML*)** 

Ông Miles là một nhà đầu tư lần đầu tham gia thị trường và muốn xây dựng một danh mục đầu tư chỉ sử dụng Tín phiếu Kho bạc Hoa Kỳ (*US T-bills*) và một quỹ chỉ số bám sát Chỉ số S&P 500. Tín phiếu Kho bạc có tỷ suất sinh lợi là 5%. Chỉ số S&P 500 có độ lệch chuẩn là 20% và tỷ suất sinh lợi kỳ vọng là 15%. 

1. Hãy vẽ đường CML và đánh dấu các điểm mà tại đó tỷ trọng đầu tư vào thị trường lần lượt là 0%, 25%, 75% và 100%. 

###### **Lời giải (*Solution*):** 

Chúng ta tính phương trình cho đường CML là $E(R_p) = 5\% + 0.50 \times \sigma_p$ bằng cách thay các thông tin đã cho vào phương trình CML tổng quát. Điểm cắt trục tung của đường thẳng là 5%, và độ dốc của nó là 0.50. Chúng ta có thể vẽ đường CML bằng cách lấy tùy ý hai điểm bất kỳ trên đường thẳng thỏa mãn phương trình trên. 

Ngoài ra, đường CML có thể được vẽ bằng cách nối điểm tỷ suất sinh lợi phi rủi ro 5% trên trục tung ($y$) với danh mục thị trường tại tọa độ (20%, 15%). Đường CML được thể hiện trong Bảng minh họa 4. 


<!-- PDF Page 80 -->

###### **Bảng minh họa 4: Rủi ro và Tỷ suất sinh lợi trên đường CML (*Exhibit 4: Risk and Return on the CML*)** 

![](assets/Portfolio_Management.pdf-0080-05.png)

<!-- Picture Text: CML<br>100% in market<br>75%<br>Rm  = 15% M<br>25%<br>0% in market<br>Slope = .5<br>Rf  = 5%<br>σ m  = 20<br>Standard Deviation of Portfolio σ p<br>Expected Portfolio Return () ER p<br> -->

> **Chú thích hình ảnh:** Trục tung: Tỷ suất sinh lợi kỳ vọng của danh mục $E(R_p)$; Trục hoành: Độ lệch chuẩn của danh mục $\sigma_p$. Đường $\text{CML}$ có độ dốc (*Slope*) $= 0.5$, đi từ điểm $0\%$ vào thị trường ($R_f = 5\%$), qua các điểm $25\%$, $75\%$, đến điểm $M$ ($100\%$ vào thị trường, với $R_m = 15\%$ và $\sigma_m = 20$).

2. Ông Miles cũng quan tâm đến việc xác định chính xác mức rủi ro và tỷ suất sinh lợi tại mỗi điểm. 

###### **Lời giải (*Solution*):** 

Tỷ suất sinh lợi khi đầu tư 0% vào thị trường 

$= 5\%$, đây chính là tỷ suất sinh lợi phi rủi ro. 

Độ lệch chuẩn khi đầu tư 0% vào thị trường 

$= 0\%$ bởi vì Tín phiếu Kho bạc không có rủi ro. 

Tỷ suất sinh lợi khi đầu tư 25% vào thị trường $= (0.75 \times 5\%) + (0.25 \times 15\%) = 7.5\%$. 

Độ lệch chuẩn khi đầu tư 25% vào thị trường $= 0.25 \times 20\% = 5\%$. 

Tỷ suất sinh lợi khi đầu tư 75% vào thị trường $= (0.25 \times 5\%) + (0.75 \times 15\%) = 12.50\%$. 

Độ lệch chuẩn khi đầu tư 75% vào thị trường $= 0.75 \times 20\% = 15\%$. 

Tỷ suất sinh lợi khi đầu tư 100% vào thị trường 

$= 15\%$, đây chính là tỷ suất sinh lợi của S&P 500. 

Độ lệch chuẩn khi đầu tư 100% vào thị trường $= 20\%$, đây chính là rủi ro của S&P 500. 


<!-- PDF Page 81 -->

##### **LÝ THUYẾT THỊ TRƯỜNG VỐN: ĐƯỜNG CML – CÁC DANH MỤC ĐẦU TƯ SỬ DỤNG ĐÒN BẨY (*CAPITAL MARKET THEORY: CML - LEVERAGED PORTFOLIOS*)** 

## **<mark>4</mark>** 

giải thích đường phân bổ vốn (*capital allocation line* – CAL) và đường thị trường vốn (*capital market line* – CML)

Trong ví dụ trước, ông Miles đã đánh giá khoản đầu tư trong khoảng từ 0% đến 100% vào thị trường và phần còn lại vào Tín phiếu Kho bạc. Đoạn thẳng nối $R_f$ và $M$ (danh mục thị trường) trong Bảng minh họa 4 minh họa các danh mục đầu tư này với các mức đầu tư tương ứng. Tại $R_f$, nhà đầu tư đang đầu tư toàn bộ tài sản của mình vào các chứng khoán phi rủi ro, tương đương với việc cho vay (*lending*) 100% ở mức lãi suất phi rủi ro. Tại Điểm $M$, nhà đầu tư nắm giữ danh mục thị trường và không cho vay bất kỳ khoản tiền nào ở mức lãi suất phi rủi ro. Sự kết hợp giữa tài sản phi rủi ro và danh mục thị trường, có thể đạt được tại các điểm nằm giữa hai giới hạn này, được gọi là các danh mục “cho vay” (*“lending” portfolios*). Thực chất, nhà đầu tư đang cho vay một phần tài sản của mình ở mức lãi suất phi rủi ro. 

Nếu ông Miles sẵn sàng chấp nhận rủi ro cao hơn, ông có thể dịch chuyển sang phía bên phải của danh mục thị trường (Điểm $M$ trong Bảng minh họa 4) bằng cách vay tiền (*borrowing money*) và mua thêm Danh mục M. Giả sử rằng ông có thể vay tiền ở cùng mức lãi suất phi rủi ro, $R_f$, bằng với mức lãi suất mà ông có thể đầu tư. Khi đó, ông có thể bổ sung số tiền đi vay vào khối tài sản sẵn có của mình và xây dựng một danh mục đi vay (*borrowing portfolio*). Nếu đường thẳng nối $R_f$ và $M$ được kéo dài về phía bên phải của Điểm $M$, phần kéo dài này của đường thẳng đại diện cho các danh mục đi vay. Khi một người di chuyển càng xa về phía bên phải của Điểm $M$, một lượng tiền đi vay ngày càng lớn đang được đầu tư vào thị trường. Điều này có nghĩa là có một khoản đầu tư *âm* (*negative investment*) vào tài sản phi rủi ro, được gọi là một *vị thế sử dụng đòn bẩy* (*leveraged position*) trong danh mục rủi ro. Điểm cụ thể được lựa chọn trên đường CML sẽ phụ thuộc vào hàm hữu dụng (*utility function*) của cá nhân đó, mà đến lượt nó lại được quyết định bởi sở thích về rủi ro và tỷ suất sinh lợi của người đó. 

###### **VÍ DỤ 2 (*EXAMPLE 2*)** 

###### **Rủi ro và Tỷ suất sinh lợi của Danh mục Sử dụng Đòn bẩy với Lãi suất Cho vay và Đi vay Bằng nhau (*Risk and Return of a Leveraged Portfolio with Equal Lending and Borrowing Rates*)** 

1. Ông Miles quyết định dành ra một phần nhỏ tài sản của mình để đầu tư vào một danh mục có rủi ro lớn hơn các khoản đầu tư trước đây vì ông dự đoán rằng thị trường chung sẽ tạo ra tỷ suất sinh lợi hấp dẫn trong tương lai. Ông giả định rằng mình có thể vay tiền ở mức lãi suất 5% và đạt được cùng mức tỷ suất sinh lợi trên S&P 500 như trước: tỷ suất sinh lợi kỳ vọng là 15% với độ lệch chuẩn là 20%. 

Hãy tính rủi ro và tỷ suất sinh lợi kỳ vọng của ông nếu ông vay thêm một khoản bằng 25%, 50% và 100% số tiền đầu tư ban đầu của mình. 

###### **Lời giải (*Solution*):** 

Độ lệch chuẩn và tỷ suất sinh lợi của danh mục sử dụng đòn bẩy có thể được tính toán theo cách tương tự như trước bằng các phương trình sau: 

$$E(R_p) = w_1 R_f + (1 - w_1) E(R_m)$$

và 


<!-- PDF Page 82 -->

$$\sigma_p = (1 - w_1)\sigma_m$$

Tỷ trọng đầu tư vào Tín phiếu Kho bạc trở thành số âm thay vì số dương bởi vì ông Miles đang đi vay tiền. Nếu vay thêm 25% khoản đầu tư ban đầu, $w_1 = -0.25$, và $(1 - w_1) = 1.25$, v.v. 

Tỷ suất sinh lợi với $w_1 = -0.25$: $(-0.25 \times 5\%) + (1.25 \times 15\%) = 17.5\%$. 

Độ lệch chuẩn với $w_1 = -0.25$: $1.25 \times 20\% = 25\%$. 

Tỷ suất sinh lợi với $w_1 = -0.50$: $(-0.50 \times 5\%) + (1.50 \times 15\%) = 20.0\%$. 

Độ lệch chuẩn với $w_1 = -0.50$: $1.50 \times 20\% = 30\%$. 

Tỷ suất sinh lợi với $w_1 = -1.00$: $(-1.00 \times 5\%) + (2.00 \times 15\%) = 25.0\%$. 

Độ lệch chuẩn với $w_1 = -1.00$: $2.00 \times 20\% = 40\%$. 

Lưu ý rằng khoản đầu tư âm (đi vay) vào tài sản phi rủi ro mang lại tỷ suất sinh lợi kỳ vọng cao hơn cho danh mục đầu tư, nhưng mức tỷ suất sinh lợi cao hơn đó cũng gắn liền với rủi ro cao hơn. 

###### **Các Danh mục Sử dụng Đòn bẩy với Lãi suất Cho vay và Đi vay Khác nhau (*Leveraged Portfolios with Different Lending and Borrowing Rates*)** 

Mặc dù chúng ta đã giả định rằng ông Miles có thể đi vay ở cùng mức lãi suất như chính phủ Hoa Kỳ, nhưng trên thực tế nhiều khả năng ông sẽ phải trả mức lãi suất cao hơn chính phủ bởi vì khả năng trả nợ của ông không chắc chắn như của chính phủ. Bây giờ hãy xem xét trường hợp mặc dù ông Miles có thể đầu tư (cho vay) ở mức lãi suất $R_f$, nhưng ông chỉ có thể đi vay ở mức $R_b$, một mức lãi suất cao hơn lãi suất phi rủi ro. 

Với lãi suất cho vay và đi vay khác nhau, đường CML sẽ không còn là một đường thẳng duy nhất nữa. Đường này sẽ có độ dốc là $[E(R_m) - R_f]/\sigma_m$ giữa Điểm $R_f$ và Điểm $M$, nơi lãi suất cho vay là $R_f$, nhưng sẽ có độ dốc nhỏ hơn là $[E(R_m) - R_b]/\sigma_m$ tại các điểm nằm bên phải Điểm $M$, nơi lãi suất đi vay là $R_b$. Bảng minh họa 5 minh họa đường CML với lãi suất cho vay và đi vay khác nhau. 


<!-- PDF Page 83 -->

###### **Bảng minh họa 5: Đường CML với Lãi suất Cho vay và Đi vay Khác nhau (*Exhibit 5: CML with Different Lending and Borrowing Rates*)** 

![](assets/Portfolio_Management.pdf-0083-03.png)

<!-- Picture Text: Market<br>portfolio, M<br>Lending<br>E ( Rm )  – Rb<br>σ m<br>Borrowing<br>E ( Rm )  – Rf<br>Rf Slope = σ m<br>Standard Deviation of Portfolio σ p<br>Expected Portfolio Return () ER p<br> -->

> **Chú thích hình ảnh:** Trục tung: Tỷ suất sinh lợi kỳ vọng của danh mục $E(R_p)$; Trục hoành: Độ lệch chuẩn của danh mục $\sigma_p$. Đồ thị đường CML bị gấp khúc tại Danh mục thị trường $M$ (*Market portfolio, M*): đoạn Cho vay (*Lending*) bên trái $M$ xuất phát từ $R_f$ có độ dốc $\text{Slope} = \frac{E(R_m) - R_f}{\sigma_m}$, và đoạn Đi vay (*Borrowing*) bên phải $M$ có độ dốc thoải hơn là $\frac{E(R_m) - R_b}{\sigma_m}$.

Các phương trình cho hai đoạn thẳng được cho dưới đây. 

![](assets/Portfolio_Management.pdf-0083-05.png)

$$w_1 \ge 0: \quad E(R_p) = R_f + \left( \frac{E(R_m) - R_f}{\sigma_m} \right) \times \sigma_p$$

và 

$$w_1 < 0: \quad E(R_p) = R_b + \left( \frac{E(R_m) - R_b}{\sigma_m} \right) \times \sigma_p$$

<!-- Formula Text: w 1  ≥  0: E (R p)   =  R f +  ( E (R m)  − R f _ σ m )  × σ p d w 1  <  0: E (R p)   =  R b +  ( E (R m)  − R b _ σ m )  × σ p -->

Phương trình đầu tiên dành cho đoạn thẳng nơi khoản đầu tư vào tài sản phi rủi ro bằng không hoặc dương — tức là tại Điểm $M$ hoặc phía bên trái của Điểm $M$ trong Bảng minh họa 5. Phương trình thứ hai dành cho đoạn thẳng nơi hoạt động đi vay, hay đầu tư âm vào tài sản phi rủi ro, diễn ra. Lưu ý rằng sự khác biệt duy nhất giữa hai phương trình nằm ở mức lãi suất được sử dụng cho việc đi vay và cho vay. 

Tất cả các danh mục đầu tư thụ động sẽ nằm trên đường CML gấp khúc (*kinked CML*) này, mặc dù khoản đầu tư vào tài sản phi rủi ro có thể là dương (cho vay), bằng không (không cho vay cũng không đi vay), hoặc âm (đi vay). Đòn bẩy cho phép những nhà đầu tư ít ngại rủi ro hơn gia tăng mức rủi ro mà họ gánh chịu bằng cách vay tiền và đầu tư hơn 100% vào danh mục thụ động. 

###### **VÍ DỤ 3 (*EXAMPLE 3*)** 

###### **Danh mục Sử dụng Đòn bẩy với Lãi suất Cho vay và Đi vay Khác nhau (*Leveraged Portfolio with Different Lending and Borrowing Rates*)** 

1. Ông Miles liên hệ với nhà môi giới của mình để vay tiền thế chấp bằng các chứng khoán nắm giữ trong danh mục đầu tư. Mặc dù khoản vay của ông Miles sẽ được đảm bảo bằng các chứng khoán trong danh mục, lãi suất mà nhà môi giới áp dụng khi cho khách hàng vay là 7%. Giả sử lãi suất phi rủi ro là 5% và tỷ suất sinh lợi thị trường là 15% với độ lệch chuẩn là 20%, hãy ước tính tỷ suất sinh lợi kỳ vọng và rủi ro của ông Miles nếu ông đầu tư 25% và 75% vào thị trường, và nếu ông quyết định 


<!-- PDF Page 84 -->

vay thêm 25% và 75% số tiền đầu tư ban đầu của mình rồi đầu tư số tiền đó vào thị trường. 

###### **Lời giải (*Solution*):** 

Độ lệch chuẩn và tỷ suất sinh lợi của danh mục không sử dụng đòn bẩy (*unleveraged portfolio*) được tính bằng các phương trình tương tự như trước: 

$$E(R_p) = w_1 R_f + (1 - w_1) E(R_m), \quad \text{và}$$

$$\sigma_p = (1 - w_1)\sigma_m$$

Kết quả không thay đổi. Độ dốc của đường thẳng đối với danh mục không sử dụng đòn bẩy là 0.50, giống hệt như trước: 

Tỷ suất sinh lợi khi đầu tư 25% vào thị trường $= (0.75 \times 5\%) + (0.25 \times 15\%) = 7.5\%$. 

Độ lệch chuẩn khi đầu tư 25% vào thị trường $= 0.25 \times 20\% = 5\%$. 

Tỷ suất sinh lợi khi đầu tư 75% vào thị trường $= (0.25 \times 5\%) + (0.75 \times 15\%) = 12.5\%$. 

Độ lệch chuẩn khi đầu tư 75% vào thị trường $= 0.75 \times 20\% = 15\%$. 

Đối với danh mục sử dụng đòn bẩy (*leveraged portfolio*), mọi thứ vẫn giữ nguyên ngoại trừ việc $R_f$ được thay thế bằng $R_b$. 

$$E(R_p) = w_1 R_b + (1 - w_1) E(R_m),$$

và 

$$\sigma_p = (1 - w_1)\sigma_m.$$

Tỷ suất sinh lợi với $w_1 = -0.25$: $(-0.25 \times 7\%) + (1.25 \times 15\%) = 17.0\%$. 

Độ lệch chuẩn với $w_1 = -0.25$: $1.25 \times 20\% = 25\%$. 

Tỷ suất sinh lợi với $w_1 = -0.75$: $(-0.75 \times 7\%) + (1.75 \times 15\%) = 21.0\%$. 

Độ lệch chuẩn với $w_1 = -0.75$: $1.75 \times 20\% = 35\%$. 

Rủi ro và tỷ suất sinh lợi của danh mục sử dụng đòn bẩy cao hơn so với danh mục không sử dụng đòn bẩy. Khi ông Miles vay thêm nhiều tiền hơn để đầu tư vào thị trường, tỷ suất sinh lợi kỳ vọng tăng lên nhưng độ lệch chuẩn của danh mục cũng tăng theo. Độ dốc của đường thẳng đối với danh mục sử dụng đòn bẩy là 0.40, so với 0.50 của danh mục không sử dụng đòn bẩy, có nghĩa là cứ mỗi 1% rủi ro tăng thêm, nhà đầu tư nhận được mức tăng 0.40% trong tỷ suất sinh lợi kỳ vọng ở phần danh mục có đòn bẩy, so với mức tăng 0.50% trong tỷ suất sinh lợi kỳ vọng ở phần danh mục không có đòn bẩy. Chỉ những nhà đầu tư ít ngại rủi ro hơn mới lựa chọn các danh mục sử dụng đòn bẩy. 


<!-- PDF Page 85 -->

##### **RỦI RO HỆ THỐNG VÀ RỦI RO PHI HỆ THỐNG (*SYSTEMATIC AND NONSYSTEMATIC RISK*)** 

## **<mark>5</mark>** 

giải thích rủi ro hệ thống (*systematic risk*) và rủi ro phi hệ thống (*nonsystematic risk*), bao gồm lý do tại sao một nhà đầu tư không nên kỳ vọng nhận thêm tỷ suất sinh lợi khi gánh chịu rủi ro phi hệ thống

Khi xây dựng một danh mục đầu tư, điều quan trọng là phải hiểu khái niệm tương quan (*correlation*) và cách mà mức tương quan nhỏ hơn 1 (không hoàn hảo) có thể giúp đa dạng hóa rủi ro của một danh mục đầu tư. Hệ quả là, rủi ro của một tài sản khi được nắm giữ đơn lẻ có thể lớn hơn rủi ro của chính tài sản đó khi nó là một phần của danh mục đầu tư. Bởi vì rủi ro của một tài sản thay đổi từ môi trường này sang môi trường khác, nhà đầu tư nên xem xét loại rủi ro nào và rủi ro đó nên được định giá (*priced*) ra sao? Phần này giải quyết câu hỏi về định giá rủi ro bằng cách phân rã tổng rủi ro của một chứng khoán hoặc một danh mục đầu tư thành rủi ro hệ thống (*systematic risk*) và rủi ro phi hệ thống (*nonsystematic risk*). Ý nghĩa của các loại rủi ro này, cách tính toán chúng, và sự liên quan của chúng đến việc định giá tài sản cũng sẽ được thảo luận. 

###### **Rủi ro Hệ thống và Rủi ro Phi hệ thống (*Systematic Risk and Nonsystematic Risk*)** 

Rủi ro hệ thống (*systematic risk*), còn được gọi là rủi ro không thể đa dạng hóa (*non-diversifiable risk*) hay rủi ro thị trường (*market risk*), là loại rủi ro tác động đến toàn bộ thị trường hoặc nền kinh tế. Ngược lại, rủi ro phi hệ thống (*nonsystematic risk*) là rủi ro gắn liền với một công ty hoặc một ngành đơn lẻ và còn được gọi là rủi ro đặc thù của công ty (*company-specific risk*), rủi ro đặc thù của ngành (*industry-specific risk*), rủi ro có thể đa dạng hóa (*diversifiable risk*), hay rủi ro riêng biệt (*idiosyncratic risk*). 

**Rủi ro hệ thống (*Systematic risk*)** là rủi ro không thể tránh khỏi và vốn có trong tổng thể thị trường. Nó không thể đa dạng hóa được vì nó bao gồm các nhân tố rủi ro mang tính bản chất bên trong thị trường và ảnh hưởng đến toàn bộ thị trường nói chung. Ví dụ về các nhân tố cấu thành rủi ro hệ thống bao gồm lãi suất, lạm phát, chu kỳ kinh tế, bất ổn chính trị và thiên tai trên diện rộng. Những sự kiện này ảnh hưởng đến toàn bộ thị trường và không có cách nào để tránh khỏi tác động của chúng. Rủi ro hệ thống có thể được khuếch đại thông qua việc lựa chọn chứng khoán hoặc sử dụng đòn bẩy, hoặc được giảm bớt bằng cách đưa vào các chứng khoán có độ tương quan thấp với danh mục đầu tư, giả định rằng chúng chưa có mặt trong danh mục đó. 

**Rủi ro phi hệ thống (*Nonsystematic risk*)** là rủi ro mang tính cục bộ hoặc giới hạn ở một tài sản hay một ngành cụ thể mà không nhất thiết ảnh hưởng đến các tài sản nằm ngoài loại tài sản đó. Ví dụ về rủi ro phi hệ thống có thể bao gồm sự thất bại của một cuộc thử nghiệm thuốc hoặc một vụ tai nạn máy bay. Tất cả những sự kiện này sẽ ảnh hưởng trực tiếp đến các công ty tương ứng và có thể cả ngành của chúng, nhưng không có tác động gì đến các tài sản hoàn toàn tách biệt với những ngành này. Nhà đầu tư có thể tránh được rủi ro phi hệ thống thông qua đa dạng hóa (*diversification*) bằng cách hình thành một danh mục gồm các tài sản không có độ tương quan cao với nhau. 

Chúng ta sẽ xây dựng các biểu thức cho từng loại rủi ro ở phần sau của bài đọc này. Bạn sẽ thấy rằng tổng của phương sai hệ thống (*systematic variance*) và phương sai phi hệ thống (*nonsystematic variance*) bằng tổng phương sai (*total variance*) của chứng khoán hoặc danh mục đầu tư: 

$$\text{Tổng phương sai (Total variance)} = \text{Phương sai hệ thống (Systematic variance)} + \text{Phương sai phi hệ thống (Nonsystematic variance)}$$

Mặc dù mối quan hệ đẳng thức này là giữa các phương sai (*variances*), bạn sẽ thường xuyên bắt gặp các tài liệu đề cập đến tổng rủi ro như là tổng của rủi ro hệ thống và rủi ro phi hệ thống. Trong những trường hợp đó, các phát biểu này đang đề cập đến phương sai chứ không phải độ lệch chuẩn (*standard deviation*). 

###### **_Định giá Rủi ro (Pricing of Risk)_** 

Việc định giá (*pricing*) hay xác định giá trị (*valuing*) một tài sản tương đương với việc ước tính tỷ suất sinh lợi kỳ vọng của nó. Nếu một tài sản có giá trị cuối kỳ (*terminal value*) đã biết trước, chẳng hạn như mệnh giá của một trái phiếu, thì mức giá hiện tại thấp hơn hàm ý tỷ suất sinh lợi tương lai cao hơn, và mức giá hiện tại cao hơn hàm ý tỷ suất sinh lợi 


<!-- PDF Page 86 -->

tương lai thấp hơn. Mối quan hệ giữa giá và tỷ suất sinh lợi cũng có thể được quan sát thấy trong biểu thức định giá đã trình bày ở Phần 2.1.2. Do đó, đôi khi chúng ta sẽ sử dụng thuật ngữ giá và tỷ suất sinh lợi thay thế cho nhau khi thảo luận về cái giá của rủi ro (*price of risk*). 

Hãy xem xét một tài sản có cả rủi ro hệ thống và rủi ro phi hệ thống. Giả sử rằng cả hai loại rủi ro này đều được định giá — tức là bạn nhận được tỷ suất sinh lợi đền bù cho cả rủi ro hệ thống lẫn rủi ro phi hệ thống. Bạn sẽ làm gì? Nhận thức được rằng rủi ro phi hệ thống có thể được triệt tiêu thông qua đa dạng hóa, bạn sẽ mua những tài sản có lượng rủi ro phi hệ thống lớn. Sau khi đã mua những tài sản có rủi ro phi hệ thống đó, bạn sẽ đa dạng hóa, hay làm giảm rủi ro đó, bằng cách đưa thêm vào các tài sản khác không có độ tương quan cao. Trong quá trình đó, bạn sẽ giảm thiểu rủi ro phi hệ thống và cuối cùng loại bỏ hoàn toàn nó ra khỏi danh mục đầu tư của mình. Bây giờ bạn sẽ có một danh mục đầu tư đã được đa dạng hóa chỉ còn chứa rủi ro hệ thống, thế nhưng bạn vẫn được đền bù cho phần rủi ro phi hệ thống mà bạn không còn nắm giữ nữa. Giống như tất cả mọi người khác, bạn sẽ có động cơ để gánh nhận ngày càng nhiều rủi ro có thể đa dạng hóa bởi vì bạn được đền bù cho nó mặc dù bạn hoàn toàn có thể loại bỏ nó. Nhu cầu đối với rủi ro có thể đa dạng hóa sẽ tiếp tục tăng lên cho đến khi giá của nó trở nên vô hạn và tỷ suất sinh lợi kỳ vọng của nó giảm xuống bằng không. Điều này có nghĩa là giả định ban đầu của chúng ta về một mức tỷ suất sinh lợi khác không cho rủi ro có thể đa dạng hóa là không chính xác, và giả định đúng phải là tỷ suất sinh lợi bằng không cho rủi ro có thể đa dạng hóa. Do đó, theo lý thuyết, trong một thị trường hiệu quả, không có phần thưởng tăng thêm nào (*no incremental reward*) kiếm được từ việc gánh chịu rủi ro có thể đa dạng hóa. 

Chúng ta đã lập luận rằng các nhà đầu tư không nên được đền bù cho việc gánh chịu rủi ro phi hệ thống. Do đó, những nhà đầu tư đang nắm giữ rủi ro phi hệ thống phải đa dạng hóa để triệt tiêu nó bằng cách đầu tư vào nhiều ngành, nhiều quốc gia và nhiều loại tài sản khác nhau. Bởi vì tỷ suất sinh lợi trong tương lai là chưa biết trước và không thể chỉ chọn toàn những khoản đầu tư chiến thắng, việc đa dạng hóa giúp bù đắp tỷ suất sinh lợi kém ở một loại tài sản này bằng việc thu về tỷ suất sinh lợi tốt ở một loại tài sản khác, qua đó làm giảm rủi ro tổng thể của danh mục đầu tư. Ngược lại, các nhà đầu tư phải được đền bù cho việc chấp nhận rủi ro hệ thống bởi vì loại rủi ro đó không thể được triệt tiêu bằng đa dạng hóa. Nếu các nhà đầu tư không nhận được một mức tỷ suất sinh lợi tương xứng với lượng rủi ro hệ thống mà họ đang gánh chịu, họ sẽ từ chối chấp nhận rủi ro hệ thống. 

Tóm lại, theo lý thuyết, rủi ro hệ thống hay rủi ro không thể đa dạng hóa được định giá (*is priced*) và các nhà đầu tư được đền bù khi nắm giữ tài sản hoặc danh mục đầu tư chỉ dựa trên rủi ro hệ thống của khoản đầu tư đó. Các nhà đầu tư không nhận được bất kỳ tỷ suất sinh lợi nào cho việc chấp nhận rủi ro phi hệ thống hay rủi ro có thể đa dạng hóa. Do đó, vì lợi ích của chính mình, các nhà đầu tư ngại rủi ro chỉ nên nắm giữ các danh mục đầu tư đã được đa dạng hóa tốt (*well-diversified portfolios*). 

###### **VÍ DỤ 4 (*EXAMPLE 4*)** 

###### **Rủi ro Hệ thống và Rủi ro Phi hệ thống (*Systematic and Nonsystematic Risk*)** 

**1.** Hãy mô tả các thành phần rủi ro hệ thống và rủi ro phi hệ thống của các tài sản sau đây: 

   - **A.** Một tài sản phi rủi ro, chẳng hạn như tín phiếu Kho bạc kỳ hạn 3 tháng 

   - **B.** Danh mục thị trường, chẳng hạn như S&P 500. 

**2.** Hãy xem xét hai tài sản A và B. Tài sản A có tổng rủi ro gấp đôi Tài sản B. Đối với Tài sản A, rủi ro hệ thống chiếm hai phần ba tổng rủi ro. Đối với Tài sản B, toàn bộ tổng rủi ro đều là rủi ro hệ thống. Tài sản nào sẽ có tỷ suất sinh lợi kỳ vọng cao hơn? 

###### **Lời giải cho câu 1A (*Solution to 1A*):** 

Theo định nghĩa, một tài sản phi rủi ro không có rủi ro. Do đó, một tài sản phi rủi ro có rủi ro hệ thống bằng không và rủi ro phi hệ thống bằng không. 
