# Tập 1: Các Phương pháp Định lượng (*Quantitative Methods*)
## Học phần 10: Hồi quy Tuyến tính Đơn (*Simple Linear Regression*)
### Phần 5/6: Bài tập Thực hành (Trang PDF 318–329)

---

<!-- PDF Page 318 -->

# **BÀI TẬP THỰC HÀNH (*PRACTICE PROBLEMS*)**

## **Thông tin sau đây liên quan đến các câu hỏi 1–3**

Một nhà phân tích đã ước lượng một mô hình hồi quy tỷ suất sinh lợi trên vốn chủ sở hữu (ROE) của một công ty theo cơ hội tăng trưởng (GO) của công ty đó, được định nghĩa là tốc độ tăng trưởng kép hàng năm (*compounded annual growth rate* – CAGR) trong ba năm của doanh số bán hàng, trong giai đoạn 20 năm, và đưa ra hồi quy tuyến tính đơn ước lượng sau đây:

$$\text{ROE}_i = 4 + 1.8 \text{GO}_i + \varepsilon_i$$

Cả hai biến số đều được tính bằng phần trăm, vì vậy một quan sát GO bằng 5% được đưa vào mô hình là 5.

**1.** Giá trị dự báo của ROE của công ty nếu GO của công ty là 10% *gần nhất* với:

   - **A.** 1,8%.

   - **B.** 15,8%.

   - **C.** 22,0%.

**2.** Mức thay đổi trong ROE khi GO thay đổi từ 5% lên 6% *gần nhất* với:

   - **A.** 1,8%.

   - **B.** 4,0%.

   - **C.** 5,8%.

**3.** Phần dư (*residual*) trong trường hợp $\text{GO}$ bằng 8% và $\text{ROE}$ quan sát được bằng 21% *gần nhất* với:

   - **A.** −1,8%.

   - **B.** 2,6%.

   - **C.** 12,0%.

**4.** Phương sai sai số không đổi (*Homoskedasticity*) được mô tả đúng nhất là tình huống trong đó phương sai của phần dư của một hồi quy:

   - **A.** bằng 0.

   - **B.** có phân phối chuẩn.

   - **C.** không đổi qua các quan sát.

<!-- PDF Page 319 -->

## **Thông tin sau đây liên quan đến các câu hỏi 5–8**

Một nhà phân tích đang kiểm tra tốc độ tăng trưởng cung tiền hàng năm của một quốc gia trong 30 năm qua. Quốc gia này đã trải qua một sự thay đổi chính sách của ngân hàng trung ương cách đây 15 năm, làm thay đổi cách tiếp cận quản lý cung tiền. Nhà phân tích đã ước lượng một mô hình sử dụng tốc độ tăng trưởng hàng năm của cung tiền được hồi quy theo biến số ($\text{SHIFT}$) nhận giá trị bằng 0 trước khi thay đổi chính sách và bằng 1 sau khi thay đổi chính sách. Cô ấy đã ước lượng các giá trị trong Bảng 1:

**Bảng 1: Các Ước lượng với Biến SHIFT**

||**Các hệ số (*Coefficients*)**|**Sai số chuẩn (*Standard Error*)**|**Thống kê $t$ (*$t$-Stat.*)**|
|---|---|---|---|
|Hệ số chặn (*Intercept*)|5.767264|0.445229|12.95348|
|SHIFT|−5.13912|0.629649|−8.16188|

*Giá trị $t$ tới hạn, mức ý nghĩa 0,05:*
*Một phía, bên trái: $-1.701$ | Một phía, bên phải: $+1.701$ | Hai phía: $\pm 2.048$*

**5.** Biến số $\text{SHIFT}$ được mô tả đúng nhất là:

   - **A.** một biến chỉ báo (*indicator variable*).

   - **B.** một biến phụ thuộc (*dependent variable*).

   - **C.** một biến liên tục (*continuous variable*).

**6.** Ý nghĩa giải thích của hệ số chặn (*intercept*) là giá trị trung bình của tốc độ tăng trưởng cung tiền hàng năm:

   - **A.** trước khi thay đổi chính sách.

   - **B.** trong toàn bộ giai đoạn.

   - **C.** sau khi thay đổi chính sách.

**7.** Ý nghĩa giải thích của hệ số góc (*slope*) là:

   - **A.** mức thay đổi trong tốc độ tăng trưởng cung tiền hàng năm qua mỗi năm.

   - **B.** tốc độ tăng trưởng cung tiền trung bình hàng năm sau khi thay đổi chính sách.

   - **C.** sự chênh lệch trong tốc độ tăng trưởng cung tiền trung bình hàng năm từ trước sang sau khi thay đổi chính sách.

**8.** Kiểm định xem liệu có sự thay đổi trong tăng trưởng cung tiền sau khi thay đổi chính sách hay không, sử dụng mức ý nghĩa $0.05$, chúng ta kết luận rằng:

   - **A.** có đủ bằng chứng cho thấy tăng trưởng cung tiền đã thay đổi.

   - **B.** không có đủ bằng chứng cho thấy tăng trưởng cung tiền khác 0.

   - **C.** không có đủ bằng chứng để chỉ ra rằng tăng trưởng cung tiền đã thay đổi.

<!-- PDF Page 320 -->

## **Thông tin sau đây liên quan đến các câu hỏi 9–12**

Kenneth McCoin, CFA, là một người phỏng vấn đầy thử thách. Năm ngoái, ông đã đưa cho mỗi ứng viên xin việc một tờ giấy có thông tin trong Bảng 1, và sau đó ông hỏi một số câu hỏi về phân tích hồi quy. Một số câu hỏi của McCoin, cùng với một mẫu các câu trả lời mà ông nhận được cho từng câu hỏi, được đưa ra dưới đây. McCoin nói với các ứng viên rằng biến độc lập là tỷ lệ lợi nhuận ròng trên doanh thu (*ratio of net income to sales*) của các nhà hàng có vốn hóa thị trường trên 100 triệu đô la và biến phụ thuộc là tỷ lệ dòng tiền từ hoạt động kinh doanh trên doanh thu (*ratio of cash flow from operations to sales*) của các nhà hàng đó. Lựa chọn nào được cung cấp dưới đây là câu trả lời đúng nhất cho từng câu hỏi của McCoin?

**Bảng 1: Phân tích Hồi quy (*Regression Analysis*)**

|**Thống kê Hồi quy (*Regression Statistics*)**||
|---|---|
|$R^2$|0.7436|
|Sai số chuẩn (*Standard error*)|0.0213|
|Số quan sát (*Observations*)|24|

![](assets/Quantitative_method.pdf-0320-07.png)

|**Nguồn (*Source*)**|**Bậc tự do (*df*)**|**Tổng bình phương (*Sum of Squares*)**|**Trung bình bình phương (*Mean Square*)**|**$F$**|**Trị số $p$ (*$p$-Value*)**|
|---|---|---|---|---|---|
|Hồi quy (*Regression*)|1|0.029|0.029000|63.81|0|
|Phần dư (*Residual*)|22|0.010|0.000455|||
|Tổng (*Total*)|23|0.040||||

||**Các hệ số (*Coefficients*)**|**Sai số chuẩn (*Standard Error*)**|**Thống kê $t$ (*$t$-Statistic*)**|**Trị số $p$ (*$p$-Value*)**|
|---|---|---|---|---|
|Hệ số chặn (*Intercept*)|0.077|0.007|11.328|0|
|Lợi nhuận ròng trên doanh thu (%)|0.826|0.103|7.988|0|

**9.** Hệ số xác định (*coefficient of determination*) *gần nhất* với:

   - **A.** 0,7436.

   - **B.** 0,8261.

   - **C.** 0,8623.

**10.** Hệ số tương quan giữa $X$ và $Y$ *gần nhất* với:

   - **A.** −0,7436.

   - **B.** 0,7436.

   - **C.** 0,8623.

**11.** Nếu tỷ lệ lợi nhuận ròng trên doanh thu của một nhà hàng là 5%, tỷ lệ dòng tiền từ hoạt động kinh doanh (CFO) trên doanh thu dự báo *gần nhất* với:

   - **A.** −4,054.

<!-- PDF Page 321 -->

   - **B.** 0,524.

   - **C.** 4,207.

**12.** Mối quan hệ giữa tỷ lệ dòng tiền từ hoạt động kinh doanh trên doanh thu và tỷ lệ lợi nhuận ròng trên doanh thu có ý nghĩa thống kê tại mức 0,05 hay không?

   - **A.** Không, bởi vì $R^2$ lớn hơn 0,05.

   - **B.** Không, bởi vì trị số $p$ của hệ số chặn và hệ số góc nhỏ hơn 0,05.

   - **C.** Có, bởi vì các trị số $p$ cho $F$ và $t$ của hệ số góc nhỏ hơn 0,05.

## **Thông tin sau đây liên quan đến các câu hỏi 13–17**

Howard Golub, CFA, đang chuẩn bị viết một báo cáo nghiên cứu về cổ phiếu phổ thông của Stellar Energy Corp. Là một trong những công ty lớn nhất thế giới, Stellar hoạt động trong lĩnh vực lọc dầu và tiếp thị dầu mỏ. Như một phần trong phân tích của mình, Golub muốn đánh giá độ nhạy cảm của tỷ suất sinh lợi cổ phiếu đối với các yếu tố kinh tế khác nhau. Ví dụ, một khách hàng gần đây đã hỏi Golub liệu giá cổ phiếu của Stellar Energy Corp. có xu hướng tăng sau các đợt tăng giá năng lượng bán lẻ hay không. Golub tin rằng mối liên hệ giữa hai biến số là âm (ngược chiều), nhưng ông không biết độ mạnh của mối liên hệ này.

Golub chỉ đạo trợ lý của mình, Jill Batten, nghiên cứu mối quan hệ giữa (1) tỷ suất sinh lợi cổ phiếu phổ thông hàng tháng của Stellar và mức thay đổi phần trăm của tháng trước trong Chỉ số Giá Tiêu dùng Năng lượng Hoa Kỳ (CPIENG) và (2) tỷ suất sinh lợi cổ phiếu phổ thông hàng tháng của Stellar và mức thay đổi phần trăm của tháng trước trong Chỉ số Giá Sản xuất Vật liệu Năng lượng Thô Hoa Kỳ (PPICEM). Golub muốn Batten chạy cả phân tích tương quan và phân tích hồi quy tuyến tính. Để đáp lại, Batten tổng hợp các thống kê tóm tắt được trình bày trong Bảng 1 cho 248 tháng. Tất cả dữ liệu đều ở dạng thập phân, trong đó $0.01$ biểu thị mức tỷ suất sinh lợi 1%. Batten cũng chạy phân tích hồi quy sử dụng tỷ suất sinh lợi hàng tháng của Stellar làm biến phụ thuộc và mức thay đổi hàng tháng trong CPIENG làm biến độc lập. Bảng 2 hiển thị kết quả của mô hình hồi quy này.

### **Bảng 1: Thống kê Mô tả (*Descriptive Statistics*)**

||**Tỷ suất sinh lợi hàng tháng cổ phiếu phổ thông Stellar**|**Thay đổi hàng tháng có độ trễ: CPIENG**|**Thay đổi hàng tháng có độ trễ: PPICEM**|
|---|---|---|---|
|Trung bình (*Mean*)|0.0123|0.0023|0.0042|
|Độ lệch chuẩn (*Standard deviation*)|0.0717|0.0160|0.0534|
|Hiệp phương sai (*Covariance*), Stellar vs. CPIENG|−0.00017|||
|Hiệp phương sai (*Covariance*), Stellar vs. PPICEM|−0.00048|||
|Hiệp phương sai (*Covariance*), CPIENG vs. PPICEM|0.00044|||
|Hệ số tương quan (*Correlation*), Stellar vs. CPIENG|−0.1452|||

<!-- PDF Page 322 -->

### **Bảng 2: Phân tích Hồi quy với CPIENG**

|**Thống kê Hồi quy (*Regression Statistics*)**|||
|---|---|---|
|$R^2$|0.0211||
|Sai số chuẩn của ước lượng (*Standard error of the estimate*)|0.0710||
|Số quan sát (*Observations*)|248||
||**Các hệ số (*Coefficients*)**|**Sai số chuẩn (*Standard Error*)**|**Thống kê $t$ (*$t$-Statistic*)**|
|Hệ số chặn (*Intercept*)|0.0138|0.0046|3.0275|
|CPIENG (%)|−0.6486|0.2818|−2.3014|

*Giá trị $t$ tới hạn: Một phía, bên trái: $-1.651$ | Một phía, bên phải: $+1.651$ | Hai phía: $\pm 1.967$*

**13.** Câu nào sau đây mô tả đúng nhất hồi quy của Batten?

   - **A.** Hồi quy chuỗi thời gian (*Time-series regression*)

   - **B.** Hồi quy dữ liệu chéo (*Cross-sectional regression*)

   - **C.** Hồi quy chuỗi thời gian và dữ liệu chéo (*Time-series and cross-sectional regression*)

**14.** Dựa trên hồi quy, nếu CPIENG *giảm* 1,0%, tỷ suất sinh lợi kỳ vọng trên cổ phiếu phổ thông của Stellar trong kỳ tiếp theo *gần nhất* với:

   - **A.** 0,0073 (0,73%).

   - **B.** 0,0138 (1,38%).

   - **C.** 0,0203 (2,03%).

**15.** Dựa trên mô hình hồi quy của Batten, hệ số xác định chỉ ra rằng:

   - **A.** tỷ suất sinh lợi của Stellar giải thích 2,11% sự biến thiên trong CPIENG.

   - **B.** tỷ suất sinh lợi của Stellar giải thích 14,52% sự biến thiên trong CPIENG.

   - **C.** những thay đổi trong CPIENG giải thích 2,11% sự biến thiên trong tỷ suất sinh lợi của Stellar.

**16.** Đối với mô hình hồi quy của Batten, $0.0710$ là độ lệch chuẩn của:

   - **A.** biến phụ thuộc.

   - **B.** phần dư từ hồi quy.

   - **C.** biến phụ thuộc dự báo từ hồi quy.

**17.** Đối với phân tích được thực hiện bởi Batten, câu nào sau đây là một kết luận *không chính xác* từ kết quả đầu ra của hồi quy?

   - **A.** Hệ số chặn ước lượng từ hồi quy của Batten khác 0 một cách có ý nghĩa thống kê tại mức ý nghĩa 0,05.

<!-- PDF Page 323 -->

   - **B.** Trong tháng sau khi CPIENG giảm, cổ phiếu phổ thông của Stellar được kỳ vọng sẽ mang lại tỷ suất sinh lợi dương.

   - **C.** Khi xem xét kết hợp, hệ số góc và hệ số chặn từ hồi quy của Batten không khác 0 một cách có ý nghĩa thống kê tại mức ý nghĩa 0,05.

## **Thông tin sau đây liên quan đến các câu hỏi 18–26**

Anh Liu là một nhà phân tích đang nghiên cứu xem liệu gánh nặng nợ của một công ty có ảnh hưởng đến quyết định bán khống (*short*) cổ phiếu công ty đó của các nhà đầu tư hay không. Cô tính toán tỷ lệ bán khống (*short interest ratio* – tỷ lệ giữa khối lượng cổ phiếu bán khống chưa đóng vị thế trên khối lượng giao dịch cổ phiếu trung bình hàng ngày, tính bằng số ngày) cho 50 công ty tính đến cuối năm và so sánh tỷ lệ này với tỷ lệ nợ của các công ty (*debt ratio* – tỷ lệ tổng nợ phải trả trên tổng tài sản, biểu diễn dưới dạng thập phân). Liu cung cấp một số thống kê trong Bảng 1. Cô cũng ước lượng một hồi quy đơn để điều tra tác động của tỷ lệ nợ lên tỷ lệ bán khống của công ty. Kết quả của hồi quy đơn này, bao gồm phân tích phương sai (ANOVA), được trình bày trong Bảng 2.

Ngoài việc ước lượng phương trình hồi quy, Liu vẽ đồ thị 50 quan sát bằng biểu đồ phân tán, với tỷ lệ bán khống trên trục tung và tỷ lệ nợ trên trục hoành.

**Bảng 1: Thống kê Tóm tắt (*Summary Statistics*)**

|**Thống kê (*Statistic*)**|**Tỷ lệ nợ (*Debt Ratio*, $X_i$)**|**Tỷ lệ bán khống (*Short Interest Ratio*, $Y_i$)**|
|---|---|---|
|Tổng (*Sum*)|$19.8550$|$192.3000$|
|Tổng bình phương các độ lệch so với giá trị trung bình|$\sum_{i=1}^{n} (X_i - \bar{X})^2 = 2.2225$|$\sum_{i=1}^{n} (Y_i - \bar{Y})^2 = 412.2042$|
|Tổng tích chéo của các độ lệch so với giá trị trung bình|$\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y}) = -9.2430$||

**Bảng 2: Hồi quy của Tỷ lệ Bán khống theo Tỷ lệ Nợ**

|**ANOVA**|**Bậc tự do (*df*)**|**Tổng bình phương (*Sum of Squares*)**|**Trung bình bình phương (*Mean Square*)**|
|---|---|---|---|
|Hồi quy (*Regression*)|1|38.4404|38.4404|
|Phần dư (*Residual*)|48|373.7638|7.7867|
|Tổng (*Total*)|49|412.2042||
|**Thống kê Hồi quy (*Regression Statistics*)**||||
|$R^2$|0.0933|||
|Sai số chuẩn của ước lượng (*Standard error of estimate*)|2.7905|||

<!-- PDF Page 324 -->

|**ANOVA**|**Bậc tự do (*df*)**|**Tổng bình phương (*Sum of Squares*)**|**Trung bình bình phương (*Mean Square*)**|
|---|---|---|---|
|Số quan sát (*Observations*)|50|||
||**Các hệ số (*Coefficients*)**|**Sai số chuẩn (*Standard Error*)**|**Thống kê $t$ (*$t$-Statistic*)**|
|Hệ số chặn (*Intercept*)|5.4975|0.8416|6.5322|
|Tỷ lệ nợ (*Debt ratio*, %)|−4.1589|1.8718|−2.2219|

*Giá trị $t$ tới hạn cho mức ý nghĩa 0,05: Một phía, bên trái: $-1.677$ | Một phía, bên phải: $+1.677$ | Hai phía: $\pm 2.011$*

Liu đang xem xét ba cách diễn giải các kết quả này cho báo cáo của cô về mối quan hệ giữa tỷ lệ nợ và tỷ lệ bán khống:

- Cách diễn giải 1: Tỷ lệ nợ cao hơn của các công ty gây ra (*cause*) tỷ lệ bán khống thấp hơn.

- Cách diễn giải 2: Tỷ lệ bán khống cao hơn của các công ty gây ra (*cause*) tỷ lệ nợ cao hơn.

- Cách diễn giải 3: Các công ty có tỷ lệ nợ cao hơn có xu hướng (*tend to*) có tỷ lệ bán khống thấp hơn.

Cô đặc biệt quan tâm đến việc sử dụng kết quả ước lượng của mình để dự báo tỷ lệ bán khống cho Tập đoàn MQD, công ty có tỷ lệ nợ là $0.40$.

**18.** Dựa trên Bảng 1 và Bảng 2, nếu Liu vẽ đồ thị 50 quan sát, biểu đồ phân tán tóm tắt mối quan hệ này sẽ được mô tả *đúng nhất* là:

   - **A.** nằm ngang (*horizontal*).

   - **B.** dốc lên (*upward sloping*).

   - **C.** dốc xuống (*downward sloping*).

**19.** Dựa trên Bảng 1, hiệp phương sai mẫu (*sample covariance*) *gần nhất* với:

   - **A.** −9,2430.

   - **B.** −0,1886.

   - **C.** 8,4123.

**20.** Dựa trên Bảng 1 và Bảng 2, hệ số tương quan giữa tỷ lệ nợ và tỷ lệ bán khống *gần nhất* với:

   - **A.** −0,3054.

   - **B.** 0,0933.

   - **C.** 0,3054.

**21.** Cách diễn giải nào mô tả *đúng nhất* những phát hiện của Liu?

   - **A.** Cách diễn giải 1

<!-- PDF Page 325 -->

   - **B.** Cách diễn giải 2

   - **C.** Cách diễn giải 3

**22.** Biến phụ thuộc trong phân tích hồi quy của Liu là:

   - **A.** hệ số chặn.

   - **B.** tỷ lệ nợ.

   - **C.** tỷ lệ bán khống.

**23.** Dựa trên Bảng 2, số bậc tự do cho kiểm định $t$ của hệ số góc trong hồi quy này là:

   - **A.** 48.

   - **B.** 49.

   - **C.** 50.

**24.** Liu nên rút ra kết luận nào sau đây từ các kết quả được trình bày trong Bảng 2?

   - **A.** Tỷ lệ bán khống trung bình là 5,4975.

   - **B.** Hệ số góc ước lượng khác 0 tại mức ý nghĩa 0,05.

   - **C.** Tỷ lệ nợ giải thích 30,54% sự biến thiên trong tỷ lệ bán khống.

**25.** Dựa trên Bảng 2, tỷ lệ bán khống kỳ vọng cho Tập đoàn MQD *gần nhất* với:

   - **A.** 3,8339.

   - **B.** 5,4975.

   - **C.** 6,2462.

**26.** Dựa trên kết quả hồi quy của Liu trong Bảng 2, thống kê $F$ để kiểm định xem hệ số góc có bằng 0 hay không *gần nhất* với:

   - **A.** −2,2219.

   - **B.** 3,5036.

   - **C.** 4,9367.

## **Thông tin sau đây liên quan đến các câu hỏi 27–29**

Doug Abitbol là người quản lý danh mục đầu tư cho Polyi Investments, một quỹ phòng hộ giao dịch tại Hoa Kỳ. Abitbol quản lý quỹ phòng hộ với sự giúp đỡ của Robert Olabudo, một người quản lý danh mục đầu tư cấp dưới. Abitbol xem xét các dự báo lạm phát của các nhà kinh tế học và muốn kiểm tra

<!-- PDF Page 326 -->

mối quan hệ giữa dự báo đồng thuận về Chỉ số Giá Tiêu dùng Hoa Kỳ (US CPI) và US CPI thực tế bằng cách sử dụng phân tích hồi quy. Olabudo ước lượng các hệ số hồi quy để kiểm định xem liệu dự báo đồng thuận có phải là không chệch (*unbiased*) hay không. Nếu các dự báo đồng thuận là không chệch, hệ số chặn phải bằng $0.0$ và hệ số góc sẽ bằng $1.0$. Kết quả hồi quy được trình bày trong Bảng 1. Ngoài ra, Olabudo tính khoảng dự báo 95% của CPI thực tế bằng cách sử dụng dự báo đồng thuận US CPI là $2.8$.

**Bảng 1: Kết quả Đầu ra Hồi quy: Ước lượng US CPI**

|**Thống kê Hồi quy (*Regression Statistics*)**||||
|---|---|---|---|
|$R^2$|0.9859|||
|Sai số chuẩn của ước lượng (*Standard error of estimate*)|0.0009|||
|Số quan sát (*Observations*)|60|||
||**Các hệ số (*Coefficients*)**|**Sai số chuẩn (*Standard Error*)**|**Thống kê $t$ (*$t$-Statistic*)**|
|Hệ số chặn (*Intercept*)|0.0001|0.0002|0.5000|
|Dự báo đồng thuận US CPI|0.9830|0.0155|63.4194|

*Ghi chú:*

**1.** Giá trị tuyệt đối của giá trị tới hạn cho thống kê $t$ là $2.002$ tại mức ý nghĩa 5%.

**2.** Độ lệch chuẩn của dự báo đồng thuận US CPI là $s_X = 0.7539$.

**3.** Giá trị trung bình của dự báo đồng thuận US CPI là $\bar{X} = 1.3350$.

Cuối cùng, Abitbol và Olabudo thảo luận về dự báo và khoảng dự báo:

   - Nhận xét 1: Đối với một mức độ tin cậy cho trước, khoảng dự báo là như nhau bất kể dự báo đồng thuận US CPI là bao nhiêu.

   - Nhận xét 2: Sai số chuẩn của ước lượng lớn hơn sẽ dẫn đến khoảng tin cậy (dự báo) rộng hơn.

**27.** Dựa trên Bảng 1, Olabudo nên:

   - **A.** kết luận rằng các dự báo lạm phát là không chệch.

   - **B.** bác bỏ giả thuyết không cho rằng hệ số góc bằng 1.

   - **C.** bác bỏ giả thuyết không cho rằng hệ số chặn bằng 0.

**28.** Dựa trên Bảng 1, Olabudo nên tính khoảng dự báo cho US CPI thực tế *gần nhất* với:

   - **A.** 2,7506 đến 2,7544.

   - **B.** 2,7521 đến 2,7529.

   - **C.** 2,7981 đến 2,8019.

**29.** Nhận xét nào của Olabudo về việc dự báo là đúng?

   - **A.** Chỉ Nhận xét 1

<!-- PDF Page 327 -->

   - **B.** Chỉ Nhận xét 2

   - **C.** Cả Nhận xét 1 và Nhận xét 2

## **Thông tin sau đây liên quan đến các câu hỏi 30–34**

Elena Vasileva gần đây đã gia nhập EnergyInvest với tư cách là chuyên viên phân tích danh mục đầu tư cấp dưới. Người giám sát của Vasileva yêu cầu cô đánh giá một cơ hội đầu tư tiềm năng vào Amtex, một tập đoàn dầu khí đa quốc gia có trụ sở tại Hoa Kỳ. Người giám sát của Vasileva gợi ý sử dụng phân tích hồi quy để kiểm tra mối quan hệ giữa cổ phiếu Amtex và tỷ suất sinh lợi trên dầu thô.

Vasileva ghi chú các giả định sau đây của phân tích hồi quy:

- Giả định 1: Hạng tử sai số không tương quan qua các quan sát.

- Giả định 2: Phương sai của hạng tử sai số là như nhau đối với tất cả các quan sát.

- Giả định 3: Biến phụ thuộc có phân phối chuẩn.

Vasileva chạy một hồi quy của tỷ suất sinh lợi cổ phiếu Amtex theo tỷ suất sinh lợi dầu thô bằng cách sử dụng dữ liệu hàng tháng mà cô thu thập được. Dữ liệu chọn lọc được sử dụng trong hồi quy được trình bày trong Bảng 1, và kết quả đầu ra hồi quy chọn lọc được trình bày trong Bảng 2. Cô sử dụng mức ý nghĩa 1% trong tất cả các kiểm định của mình.

**Bảng 1: Dữ liệu Chọn lọc cho Tỷ suất sinh lợi Dầu thô và Tỷ suất sinh lợi Cổ phiếu Amtex**

||**Tỷ suất sinh lợi Dầu ($X_i$)**|**Tỷ suất sinh lợi Amtex ($Y_i$)**|**Tích chéo $(X_i - \bar{X})(Y_i - \bar{Y})$**|**Tỷ suất sinh lợi Amtex dự báo ($\hat{Y}_i$)**|**Phần dư hồi quy $(Y_i - \hat{Y}_i)$**|**Bình phương phần dư $(Y_i - \hat{Y}_i)^2$**|
|---|---|---|---|---|---|---|
|Tháng 1|−0.032000|0.033145|−0.000388|0.002011|−0.031134|0.000969|
|$\vdots$|$\vdots$|$\vdots$|$\vdots$|$\vdots$|$\vdots$|$\vdots$|
|Tháng 36|0.028636|0.062334|0.002663|0.016282|−0.046053|0.002121|
|Tổng (*Sum*)|||0.085598|||0.071475|
|Trung bình (*Average*)|−0.018056|0.005293|||||

**Bảng 2: Kết quả Đầu ra Hồi quy Chọn lọc, Biến phụ thuộc: Tỷ suất sinh lợi Cổ phiếu Amtex**

||**Hệ số (*Coefficient*)**|**Sai số chuẩn (*Standard Error*)**|
|---|---|---|
|Hệ số chặn (*Intercept*)|0.0095|0.0078|
|Tỷ suất sinh lợi dầu (*Oil return*)|0.2354|0.0760|

Giá trị $t$ tới hạn cho mức ý nghĩa 1%:

Một phía, bên trái: $-2.441$

<!-- PDF Page 328 -->

Một phía, bên phải: $+2.441$ | Hai phía: $\pm 2.728$

Vasileva kỳ vọng tỷ suất sinh lợi dầu thô vào tháng tới, Tháng 37, sẽ là $-0.01$. Cô tính toán sai số chuẩn của dự báo là $0.0469$.

**30.** Giả định nào của Vasileva liên quan đến phân tích hồi quy là *không chính xác*?

   - **A.** Giả định 1

   - **B.** Giả định 2

   - **C.** Giả định 3

**31.** Dựa trên Bảng 1, sai số chuẩn của ước lượng (*standard error of the estimate*) *gần nhất* với:

   - **A.** 0,04456.

   - **B.** 0,04585.

   - **C.** 0,05018.

**32.** Dựa trên Bảng 2, Vasileva nên bác bỏ giả thuyết không cho rằng:

   - **A.** hệ số góc nhỏ hơn hoặc bằng 0,15.

   - **B.** hệ số chặn nhỏ hơn hoặc bằng 0.

   - **C.** tỷ suất sinh lợi dầu thô không giải thích được tỷ suất sinh lợi cổ phiếu Amtex.

**33.** Dựa trên Bảng 2 và dự báo của Vasileva về tỷ suất sinh lợi dầu thô cho Tháng 37, ước lượng tỷ suất sinh lợi cổ phiếu Amtex cho Tháng 37 *gần nhất* với:

   - **A.** −0,0024.

   - **B.** 0,0071.

   - **C.** 0,0119.

**34.** Sử dụng thông tin từ Bảng 2, khoảng dự báo 99% cho tỷ suất sinh lợi cổ phiếu Amtex vào Tháng 37 được mô tả *đúng nhất* là:

   - **A.** $\hat{Y}_f \pm 0.0053$.

   - **B.** $\hat{Y}_f \pm 0.0469$.

   - **C.** $\hat{Y}_f \pm 0.1279$.

## **Thông tin sau đây liên quan đến các câu hỏi 35–38**

Espey Jones đang kiểm tra mối quan hệ giữa biên lợi nhuận ròng (NPM) của các công ty, tính bằng phần trăm, và vòng quay tài sản cố định (*fixed asset turnover* – FATO) của chúng. Anh ấy đã thu thập một mẫu gồm 35 công ty cho năm tài chính gần nhất và khớp một số dạng hàm khác nhau, cuối cùng chọn mô hình sau đây:

<!-- PDF Page 329 -->

$$\ln(\text{NPM}_i) = b_0 + b_1 \text{FATO}_i$$

Kết quả của ước lượng này được cung cấp trong Bảng 1.

**Bảng 1: Kết quả Hồi quy NPM theo FATO**

|**Nguồn (*Source*)**|**Bậc tự do (*df*)**|**Tổng bình phương (*Sum of Squares*)**|**Trung bình bình phương (*Mean Square*)**|**$F$**|**Trị số $p$ (*$p$-Value*)**|
|---|---|---|---|---|---|
|Hồi quy (*Regression*)|1|102.9152|102.9152|1,486.7079|0.0000|
|Phần dư (*Residual*)|32|2.2152|0.0692|||
|Tổng (*Total*)|33|105.1303||||

||**Các hệ số (*Coefficients*)**|**Sai số chuẩn (*Standard Error*)**|**Thống kê $t$ (*$t$-Statistic*)**|**Trị số $p$ (*$p$-Value*)**|
|---|---|---|---|---|
|Hệ số chặn (*Intercept*)|0.5987|0.0561|10.6749|0.0000|
|FATO|0.2951|0.0077|38.5579|0.0000|

**35.** Hệ số xác định (*coefficient of determination*) *gần nhất* với:

   - **A.** 0,0211.

   - **B.** 0,9789.

   - **C.** 0,9894.

**36.** Sai số chuẩn của ước lượng (*standard error of the estimate*) *gần nhất* với:

   - **A.** 0,2631.

   - **B.** 1,7849.

   - **C.** 38,5579.

**37.** Tại mức ý nghĩa $0.01$, Jones nên kết luận rằng:

   - **A.** biên lợi nhuận ròng trung bình là 0,5987%.

   - **B.** sự biến thiên của vòng quay tài sản cố định giải thích sự biến thiên của logarit tự nhiên của biên lợi nhuận ròng.

   - **C.** sự thay đổi trong vòng quay tài sản cố định từ 3 lên 4 lần có khả năng dẫn đến sự thay đổi trong biên lợi nhuận ròng là 0,5987%.

**38.** Biên lợi nhuận ròng dự báo cho một công ty có vòng quay tài sản cố định là 2 lần *gần nhất* với:

   - **A.** 1,1889%.

   - **B.** 1,8043%.

   - **C.** 3,2835%.
