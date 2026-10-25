# Tập 7: Công cụ Phái sinh (Derivatives)
## Learning Module 8 Pricing and Valuation of Options (Trang PDF 179–204)

---

# Tập 7: Công cụ Phái sinh (*Derivatives*)
## Học phần 8: Định giá và Xác định giá trị của Quyền chọn (*Pricing and Valuation of Options*)
### Phần 1/2: Giới thiệu (Trang PDF 179–193)

---

<!-- PDF Page 179 -->

#### H Ọ C P H Ầ N

# **<mark>8</mark>** 

### **Định giá và Xác định giá trị của Quyền chọn (*Pricing and Valuation of Options*)** 

###### **<mark>MỤC TIÊU HỌC TẬP (*LEARNING OUTCOMES*)</mark>** 

|**_Mức độ thành thạo_**<br>**_Ứng viên cần có khả năng:_**|
|---|
|giải thích giá trị thực hiện (*exercise value*), trạng thái giá trị (*moneyness*), và giá trị thời gian (*time value*) của một quyền chọn|
|đối chiếu việc sử dụng các khái niệm kinh doanh chênh lệch giá (*arbitrage*) và mô phỏng (*replication*) trong việc định giá các cam kết kỳ hạn (*forward commitments*) và các quyền đòi nợ có điều kiện (*contingent claims*)|
|xác định các nhân tố quyết định giá trị của một quyền chọn và mô tả cách thức mỗi nhân tố ảnh hưởng đến giá trị của một quyền chọn|

##### **GIỚI THIỆU (*INTRODUCTION*)** 

Hợp đồng quyền chọn (*option contracts*) là các quyền đòi nợ có điều kiện (*contingent claims*) trong đó một trong các đối tác quyết định liệu giao dịch có được thanh toán hay không và vào thời điểm nào. Không giống như một cam kết kỳ hạn (*forward commitment*) có giá trị bằng không đối với cả hai đối tác tại thời điểm khởi tạo, người mua quyền chọn trả một khoản phí quyền chọn (*premium*) cho người bán để có quyền giao dịch tài sản cơ sở (*underlying*) trong tương lai tại một mức giá đã thỏa thuận trước. Bản chất có điều kiện của quyền chọn ảnh hưởng đến mức giá cũng như giá trị của chúng theo thời gian. 

Trong bài học đầu tiên, chúng ta sẽ khám phá ba đặc điểm độc nhất của các quyền đòi nợ có điều kiện liên quan đến giá trị của quyền chọn so với giá giao ngay của tài sản cơ sở: giá trị thực hiện hay giá trị nội tại (*exercise, or intrinsic, value*); mối quan hệ giữa giá giao ngay của tài sản cơ sở và giá thực hiện của quyền chọn, được gọi là “trạng thái giá trị” (*“moneyness”*); và giá trị thời gian (*time value*). Tiếp theo, chúng ta chuyển sang tìm hiểu cách thức các khái niệm kinh doanh chênh lệch giá (*arbitrage*) và mô phỏng (*replication*) đã được giới thiệu trước đó đối với các cam kết kỳ hạn có sự khác biệt như thế nào khi được áp dụng cho các quyền đòi nợ có điều kiện với hồ sơ kết quả thanh toán bất đối xứng (*asymmetric payoff profile*). Cuối cùng, chúng ta xác định và mô tả các nhân tố quyết định giá trị của một quyền chọn. Các bài học này tập trung vào quyền chọn kiểu châu Âu (*European options*), vốn chỉ có thể được thực hiện vào ngày đáo hạn (*at expiration*). 

## **<mark>1</mark>** 

###### **TỔNG QUAN HỌC PHẦN (*LEARNING MODULE OVERVIEW*)** 

- Giá trị của một quyền chọn bao gồm giá trị thực hiện (*exercise value*) và giá trị thời gian (*time value*) của nó. Giá trị thực hiện là giá trị của quyền chọn nếu nó có thể được thực hiện _ngay lập tức_ (*immediately exercisable*), trong khi giá trị thời gian nắm bắt _khả năng_ (*possibility*) rằng sự trôi qua của thời gian và tính biến thiên của giá tài sản cơ sở sẽ làm tăng khả năng sinh lời của việc thực hiện quyền khi đáo hạn. 


<!-- PDF Page 180 -->

- Trạng thái giá trị của quyền chọn (*option moneyness*) biểu thị mối quan hệ giữa giá tài sản cơ sở (*underlying price*) và giá thực hiện (*exercise price*). Một quyền chọn bán (*put option*) hoặc quyền chọn mua (*call option*) ở trạng thái “ngang giá” (*“at the money”* – ATM) khi giá tài sản cơ sở bằng với giá thực hiện. Một quyền chọn có nhiều khả năng được thực hiện hơn nếu nó ở trạng thái “có lời” (*“in the money”* – ITM)—với giá tài sản cơ sở cao hơn (đối với quyền chọn mua) hoặc thấp hơn (đối với quyền chọn bán) so với giá thực hiện—và ít có khả năng được thực hiện hơn nếu nó ở trạng thái “lỗ” (*“out of the money”* – OTM). 

- Do hồ sơ kết quả thanh toán bất đối xứng, các quyền chọn có đặc trưng là các cận giá không có kinh doanh chênh lệch giá (*no-arbitrage price bounds*). Cận dưới (*lower bound*) là một hàm số của giá trị hiện tại của giá thực hiện và giá tài sản cơ sở, trong khi cận trên (*upper bound*) là giá tài sản cơ sở đối với quyền chọn mua và là giá thực hiện đối với quyền chọn bán. 

- Giống như trong trường hợp của các cam kết kỳ hạn, việc mô phỏng (*replication*) các hợp đồng quyền chọn sử dụng sự kết hợp của các vị thế mua (*long* – đối với quyền chọn mua) hoặc vị thế bán (*short* – đối với quyền chọn bán) trên một tài sản cơ sở cùng với việc đi vay hoặc cho vay tiền mặt. Giao dịch mô phỏng cho một quyền chọn được dựa trên một tỷ lệ của tài sản cơ sở, tỷ lệ này gắn liền mật thiết với trạng thái giá trị (*moneyness*) của quyền chọn. 

- Giá tài sản cơ sở, giá thực hiện, thời gian đến khi đáo hạn (*time to maturity*), lãi suất phi rủi ro (*risk-free rate*), độ biến động giá của tài sản cơ sở (*volatility of the underlying price*), và bất kỳ khoản thu nhập hoặc chi phí nào gắn liền với việc sở hữu tài sản cơ sở là những nhân tố then chốt quyết định giá trị của một quyền chọn. 

- Những thay đổi trong độ biến động giá của tài sản cơ sở và thời gian đến khi đáo hạn thường có tác động cùng chiều lên giá trị của cả quyền chọn bán và quyền chọn mua. Những thay đổi trong giá thực hiện, lãi suất phi rủi ro, và bất kỳ khoản thu nhập hay chi phí nào gắn liền với việc sở hữu tài sản cơ sở có tác động ngược chiều lên quyền chọn mua so với quyền chọn bán. 

###### **TỰ ĐÁNH GIÁ HỌC PHẦN (*LEARNING MODULE SELF-ASSESSMENT*)** 

Những câu hỏi ban đầu này nhằm giúp bạn tự đánh giá mức độ hiểu biết hiện tại của mình về học phần này. 

1. Phát biểu nào sau đây mô tả đúng về cận dưới (*lower bound*) đối với giá trị của một quyền chọn mua (*call option*)? 

   - **A.** Giá của tài sản cơ sở trừ đi giá trị hiện tại của giá thực hiện quyền chọn 

   - **B.** Giá của tài sản cơ sở trừ đi giá thực hiện quyền chọn hoặc bằng không, tùy theo giá trị nào lớn hơn 

   - **C.** Giá của tài sản cơ sở trừ đi giá trị hiện tại của giá thực hiện quyền chọn hoặc bằng không, tùy theo giá trị nào lớn hơn 

###### **Lời giải:** 

C là đáp án đúng. Cận dưới của giá quyền chọn mua là giá của tài sản cơ sở trừ đi giá trị hiện tại của giá thực hiện hoặc bằng không, tùy theo giá trị nào lớn hơn. A không đúng vì câu trả lời bỏ qua thực tế rằng cận dưới bằng không nếu giá của tài sản cơ sở nhỏ hơn giá trị hiện tại của giá thực hiện. B không đúng vì bỏ qua yếu tố giá trị hiện tại (*present value*). 


<!-- PDF Page 181 -->

2. Hãy ghép các phát biểu sau đây về chiến lược mô phỏng (*replication strategies*) với (các) công cụ phái sinh tương ứng của chúng:

| Phát biểu về chiến lược mô phỏng | Công cụ phái sinh tương ứng |
|---|---|
| 1. Tại thời điểm $t = 0$, cho vay ở mức lãi suất phi rủi ro và bán tài sản cơ sở tại giá $S_0$. | A. Không phải chiến lược mô phỏng quyền chọn mua cũng không phải chiến lược mô phỏng quyền chọn bán |
| 2. Chiến lược mô phỏng được thực thi tại thời điểm khởi tạo và được tất toán khi đáo hạn mà không cần điều chỉnh theo thời gian. | B. Chiến lược mô phỏng quyền chọn bán (*put option replication strategy*) |
| 3. Tại thời điểm $t = T$, bán tài sản cơ sở tại giá $S_T$ và hoàn trả khoản vay trị giá $X$. | C. Chiến lược mô phỏng quyền chọn mua (*call option replication strategy*) nếu được thực hiện |

###### **Lời giải:**

   **1.** B là đáp án đúng. Tại thời điểm $t = 0$, chiến lược mô phỏng quyền chọn bán bao gồm việc cho vay ở mức lãi suất phi rủi ro và bán tài sản cơ sở tại giá $S_0$.

   **2.** A là đáp án đúng. Vì cả quyền chọn mua và quyền chọn bán đều có hồ sơ kết quả thanh toán phi tuyến tính (*non-linear payoff profile*), chiến lược mô phỏng của chúng đòi hỏi phải có sự điều chỉnh theo thời gian khi xác suất thực hiện quyền thay đổi.

   **3.** C là đáp án đúng. Chiến lược mô phỏng quyền chọn mua nếu được thực hiện bao gồm việc hoàn trả khoản vay trị giá $X$ và bán tài sản cơ sở tại giá $S_T$ vào thời điểm $t = T$.

3. Một quyền chọn mua kiểu châu Âu (*European call option*) còn 3 tháng nữa là đáo hạn trên một cổ phiếu cơ sở không có dòng tiền bổ sung có giá thực hiện ($X$) là 50 GBP, lãi suất phi rủi ro là 2%, và giá tài sản cơ sở hiện tại ($S_t$) là 57,50 GBP. Nếu giá quyền chọn mua hiện tại là 10 GBP, phương án nào dưới đây thể hiện gần đúng nhất giá trị thực hiện (*exercise value*) và giá trị thời gian (*time value*) của quyền chọn?

   - **A.** Giá trị thực hiện = 7,50 GBP; Giá trị thời gian = 2,50 GBP
   - **B.** Giá trị thực hiện = 7,75 GBP; Giá trị thời gian = 2,25 GBP
   - **C.** Giá trị thực hiện = 0 GBP; Giá trị thời gian = 10 GBP

###### **Lời giải:**

B là đáp án đúng. Giá trị của một quyền chọn bao gồm giá trị thực hiện cộng với giá trị thời gian của nó. Giá trị thực hiện của một quyền chọn mua là $\text{Max}(0, S_t - \text{PV}(X))$ và được tính như sau:

$$\text{Giá trị thực hiện của quyền chọn mua (Call Option Exercise Value)} = \text{Max}\left(0, S_t - X(1 + r)^{-(T - t)}\right)$$

$$= \text{Max}\left(0, 57,50\text{ GBP} - 50\text{ GBP}(1,02)^{-0,25}\right) = 7,75\text{ GBP}$$

Giá trị thực hiện mang số dương vì giá tài sản cơ sở hiện tại vượt quá giá trị hiện tại của giá thực hiện. Giá trị thời gian là phần chênh lệch giữa giá quyền chọn và giá trị thực hiện, đại diện cho khả năng kết quả thanh toán của quyền chọn khi đáo hạn sẽ vượt quá giá trị thực hiện hiện tại nhờ sự biến động giá thuận lợi:

$$\text{Giá trị thời gian của quyền chọn mua (Call Option Time Value)} = c_t - \text{Max}\left(0, S_t - X(1 + r)^{-(T - t)}\right)$$

$$= 2,25\text{ GBP} \ (= 10\text{ GBP} - 7,75\text{ GBP})$$

Giá trị thời gian luôn dương và giảm dần về không khi đáo hạn ($t = T$). A không đúng vì thành phần giá trị hiện tại bị bỏ qua trong phép tính giá trị thực hiện. C không đúng vì nó hàm ý rằng quyền chọn có giá trị thực hiện bằng không.


<!-- PDF Page 182 -->

4. Hãy ghép các mối quan hệ giữa giá tài sản cơ sở và giá thực hiện sau đây với quyền chọn bán (*put option*) tương ứng của chúng: 

| Mối quan hệ giữa $S_T$ và $X$ | Trạng thái của quyền chọn bán |
|---|---|
| 1. $S_T = 100, X = 100$ | A. Quyền chọn bán ngang giá (*At-the-money put option*) |
| 2. $S_T = 110, X = 100$ | B. Quyền chọn bán có lời (*In-the-money put option*) |
| 3. $S_T = 90, X = 100$ | C. Quyền chọn bán lỗ (*Out-of-the-money put option*) |

###### **Lời giải:** 

Quyền chọn bán ở trạng thái có lời (*in the money*) khi $S_T < X$, ngang giá (*at the money*) khi $S_T = X$, và lỗ (*out of the money*) khi $S_T > X$. Do đó: 

**1.** A là đáp án đúng. Vì $S_T = X = 100$, đây là một quyền chọn bán ngang giá (*at-the-money put option*). 

**2.** C là đáp án đúng. Vì $S_T > X$, đây là một quyền chọn bán lỗ (*out-of-the-money put option*). 

**3.** B là đáp án đúng. Vì $S_T < X$, đây là một quyền chọn bán có lời (*in-the-money put option*). 

5. Hãy ghép những thay đổi sau đây của một nhân tố ảnh hưởng đến giá trị quyền chọn (giữ các nhân tố khác không đổi) với sự thay đổi giá trị quyền chọn tương ứng của chúng: 

| Thay đổi của nhân tố | Thay đổi giá trị quyền chọn |
|---|---|
| 1. Giá thực hiện ($X$) cao hơn | A. Làm giảm giá trị của cả quyền chọn mua và quyền chọn bán |
| 2. Giá tài sản cơ sở ($S_T$) cao hơn | B. Làm giảm giá trị của quyền chọn mua |
| 3. Sự sụt giảm trong độ biến động (*volatility*) của giá tài sản cơ sở | C. Làm giảm giá trị của quyền chọn bán |

###### **Lời giải:** 

   **1.** B là đáp án đúng. Giá thực hiện cao hơn làm giảm giá trị của quyền chọn mua; đối với một mức giá tài sản cơ sở nhất định khi đáo hạn ($S_T$), giá trị thanh toán của quyền chọn mua là $\text{Max}(0, S_T - X)$ sẽ giảm xuống khi $X$ cao hơn. 

   **2.** C là đáp án đúng. Giá tài sản cơ sở ($S_T$) cao hơn sẽ làm giảm giá trị của quyền chọn bán. Vì quyền chọn bán là quyền được bán một tài sản cơ sở, giá trị thanh toán của quyền chọn bán là $\text{Max}(0, X - S_T)$ sẽ giảm khi $S_T$ tăng lên. 

   **3.** A là đáp án đúng. Sự sụt giảm trong độ biến động của giá tài sản cơ sở sẽ làm giảm giá trị của cả quyền chọn mua và quyền chọn bán. Độ biến thiên giá thấp hơn của tài sản cơ sở sẽ làm giảm xác suất đạt được giá trị thực hiện dương cao hơn đối với quyền chọn mua hoặc quyền chọn bán mà không làm ảnh hưởng đến trường hợp bất lợi phía dưới nơi quyền chọn hết hạn mà không được thực hiện. 

6. Phát biểu nào sau đây mô tả đúng về cách thức giá trị của một quyền chọn mua thay đổi nếu khoản thu nhập trên tài sản cơ sở giảm xuống ngoài dự kiến, giữ tất cả các yếu tố khác không đổi? 

   - **A.** Giá trị quyền chọn mua tăng lên. 

   - **B.** Giá trị quyền chọn mua giảm xuống. 

   - **C.** Giá trị quyền chọn mua không thay đổi. 

###### **Lời giải:** 

A là đáp án đúng. Thu nhập hoặc các lợi ích phi tiền mặt khác (chẳng hạn như lợi suất thuận tiện – *convenience yield*) thuộc về người sở hữu tài sản cơ sở chứ không thuộc về người sở hữu công cụ phái sinh vốn có giá trị dựa trên tài sản cơ sở đó. Một quyền chọn mua trên một tài sản cơ sở có tạo ra thu nhập sẽ có giá trị thấp hơn so với một quyền chọn mua giống hệt trên cùng 


<!-- PDF Page 183 -->

tài sản cơ sở đó nhưng không có thu nhập. Do đó, sự sụt giảm thu nhập trên tài sản cơ sở sẽ làm tăng giá trị của quyền chọn mua. 

##### **GIÁ TRỊ QUYỀN CHỌN SO VỚI GIÁ GIAO NGAY CỦA TÀI SẢN CƠ SỞ (*OPTION VALUE RELATIVE TO THE UNDERLYING SPOT PRICE*)** 

## **<mark>2</mark>** 

giải thích giá trị thực hiện (*exercise value*), trạng thái giá trị (*moneyness*), và giá trị thời gian (*time value*) của một quyền chọn 

Như đã chỉ ra trong các bài học trước, hồ sơ kết quả thanh toán phi tuyến tính (*non-linear*) hay bất đối xứng (*asymmetric*) của một quyền chọn khiến chúng ta phải tiếp cận các công cụ phái sinh này theo cách khác với một cam kết kỳ hạn. Khi đánh giá các công cụ phái sinh này, vốn có giá trị phụ thuộc quyết định vào việc liệu giá giao ngay có vượt qua ngưỡng giá thực hiện khi đáo hạn hay không, người mua và người bán thường dựa vào ba thước đo—giá trị thực hiện (*exercise value*), trạng thái giá trị (*moneyness*), và giá trị thời gian (*time value*)—để đo lường giá trị của một quyền chọn trong suốt vòng đời của hợp đồng. Hãy nhớ lại từ bài học trước rằng quyền chọn kiểu Mỹ (*American options*) có thể được thực hiện vào bất kỳ thời điểm nào, trong khi quyền chọn kiểu châu Âu (*European options*) chỉ có thể được thực hiện khi đáo hạn. Bài học này chỉ tập trung vào các quyền chọn kiểu châu Âu không có thêm chi phí hay lợi ích nào gắn với việc sở hữu tài sản cơ sở. 

##### **GIÁ TRỊ THỰC HIỆN CỦA QUYỀN CHỌN (*OPTION EXERCISE VALUE*)** 

**<mark>3</mark>** 

giải thích giá trị thực hiện (*exercise value*), trạng thái giá trị (*moneyness*), và giá trị thời gian (*time value*) của một quyền chọn 

Người mua quyền chọn sẽ chỉ thực hiện quyền chọn mua hoặc quyền chọn bán khi đáo hạn nếu nó mang lại một kết quả thanh toán dương (*positive payoff*)—nghĩa là: 

- $(S_T - X) > 0$ đối với quyền chọn mua (*call*) 

- $(X - S_T) > 0$ đối với quyền chọn bán (*put*) 

Nếu không được thực hiện, quyền chọn sẽ hết hạn mà không có giá trị (*expires worthless*) và khoản lỗ của người mua quyền chọn bằng đúng khoản phí quyền chọn đã trả (*premium paid*). 

Tại bất kỳ thời điểm nào _trước_ khi đáo hạn ($t < T$), người mua và người bán thường đo lường giá trị của một quyền chọn bằng cách so sánh giá giao ngay của tài sản cơ sở ($S_t$) với giá thực hiện ($X$) để xác định giá trị thực hiện (*exercise value*) của quyền chọn tại thời điểm $t$. Đây là giá trị của hợp đồng quyền chọn _nếu_ quyền chọn có thể được thực hiện ngay tại thời điểm $t$. Giá trị thực hiện đối với một quyền chọn mua và một quyền chọn bán tại thời điểm $t$ có tính đến giá trị thời gian của tiền tệ là chênh lệch giữa giá giao ngay ($S_t$) và giá trị hiện tại của giá thực hiện ($\text{PV}(X)$), như sau: 

![](assets/Derivatives.pdf-0183-16.png)

<!-- Formula Text: Call Option Exercise Value: Max(0,   S t − X (1 + r) −(T−t)) (1) Put Option Exercise Value: Max(0,  X (1 + r) −(T−t) − S t) (2) -->
$$\text{Giá trị thực hiện của quyền chọn mua (Call Option Exercise Value): } \text{Max}\left(0, S_t - X(1 + r)^{-(T - t)}\right) \tag{1}$$

$$\text{Giá trị thực hiện của quyền chọn bán (Put Option Exercise Value): } \text{Max}\left(0, X(1 + r)^{-(T - t)} - S_t\right) \tag{2}$$

Nếu chúng ta giả định mức giá thực hiện, $X$, bằng với mức giá kỳ hạn, $F_0(T)$, thì giá trị thực hiện của một quyền chọn mua sẽ _giống hệt_ như giá trị của một cam kết mua kỳ hạn (*long forward commitment*) tại thời điểm $t$ ($V_t(T)$). Cam kết kỳ hạn này đã được chứng minh trước đó là bằng $S_t - \text{PV}(F_0(T))$, _với điều kiện là_ $S_t > \text{PV}(X)$. Nghĩa là, đối với một quyền chọn mua có $F_0(T) = X$: 
Nếu $S_t > \text{PV}(X)$: $S_t - \text{PV}(F_0(T)) = \text{Max}(0, S_t - \text{PV}(X))$. 


<!-- PDF Page 184 -->

Lưu ý rằng phép so sánh này _bỏ qua_ khoản phí quyền chọn mua trả trước (*upfront call option premium*) do người mua quyền chọn trả ($c_0$ tại thời điểm $t = 0$). 

###### **VÍ DỤ 1 (*EXAMPLE 1*)** 

###### **Giá trị Thực hiện của Quyền chọn Bán (*Put Option Exercise Value*)** 

Hãy xem xét trường hợp của một quyền chọn bán kỳ hạn 1 năm có giá thực hiện ($X$) là 1.000 EUR và lãi suất phi rủi ro là 1%. Giá trị thực hiện của quyền chọn sau thời gian 6 tháng là bao nhiêu nếu giá giao ngay ($S_t$) bằng 950 EUR? 

Sử dụng Phương trình 2 để giải tìm $\text{Max}(0, \text{PV}(X) - S_t)$: 

$$X(1 + r)^{-(T - t)} - S_t = 45,04\text{ EUR} \ (= 1.000\text{ EUR}(1,01)^{-0,5} - 950\text{ EUR})$$

## **<mark>4</mark>** 

##### **TRẠNG THÁI GIÁ TRỊ CỦA QUYỀN CHỌN (*OPTION MONEYNESS*)** 

giải thích giá trị thực hiện (*exercise value*), trạng thái giá trị (*moneyness*), và giá trị thời gian (*time value*) của một quyền chọn 

Giá trị thực hiện của một quyền chọn tại bất kỳ thời điểm $t$ nào đã được chỉ ra là kết quả thanh toán hiện tại (*current payoff*) của nó. Mối quan hệ giữa giá giao ngay của tài sản cơ sở và giá thực hiện của quyền chọn biểu thị **trạng thái giá trị (*moneyness*)** của quyền chọn. Các ví dụ về quyền chọn ở trạng thái có lời (*in-the-money* – ITM) bao gồm một quyền chọn mua có giá giao ngay của tài sản cơ sở _cao hơn_ giá thực hiện ($X$) và một quyền chọn bán có giá giao ngay của tài sản cơ sở _thấp hơn_ giá thực hiện. Khi giá tài sản cơ sở _bằng_ với giá thực hiện, quyền chọn bán hoặc quyền chọn mua được gọi là ở trạng thái ngang giá (*at the money* – ATM). Khi giá tài sản cơ sở _thấp hơn_ (_cao hơn_) giá thực hiện đối với một quyền chọn _mua_ (_bán_), quyền chọn đó ít có khả năng được thực hiện hơn và được gọi là ở trạng thái lỗ (*out of the money* – OTM). 

Ngoài ra, _mức độ_ (*degree*) mà một quyền chọn đang ở trạng thái có lời (ITM) hay lỗ (OTM) cũng ảnh hưởng đến độ nhạy (*sensitivity*) của giá quyền chọn trước những thay đổi của giá tài sản cơ sở. Ví dụ, cái gọi là **quyền chọn có lời sâu (*deep-in-the-money option*)**, hay một quyền chọn có khả năng rất cao sẽ được thực hiện, thường thể hiện sự tương ứng gần như một-đổi-một (*one-to-one correspondence*) giữa biến động giá quyền chọn và biến động giá tài sản cơ sở. Một **quyền chọn lỗ sâu (*deep-out-of-the-money option*)**, vốn rất _ít có khả năng_ được thực hiện, thể hiện độ nhạy giá quyền chọn thấp hơn rất nhiều đối với một mức thay đổi giá tài sản cơ sở nhất định. Ngược lại, những thay đổi giá tương đối nhỏ của tài sản cơ sở đối với một quyền chọn ngang giá (*at-the-money option*) thường quyết định liệu quyền chọn đó có được thực hiện hay không. Trạng thái giá trị (*moneyness*) thường được sử dụng để so sánh các quyền chọn trên cùng một tài sản cơ sở nhưng có các mức giá thực hiện và/hoặc thời gian đến khi đáo hạn khác nhau. Bảng 1 (*Exhibit 1*) thể hiện trạng thái giá trị của một quyền chọn mua khi đáo hạn và tóm tắt các mối quan hệ này. 


<!-- PDF Page 185 -->

**Bảng 1: Trạng thái Giá trị của Quyền chọn Mua khi Đáo hạn (*Exhibit 1: Call Option Moneyness at Maturity*)** 

![](assets/Derivatives.pdf-0185-04.png)

<!-- Picture Text: Payoff/<br>Profit<br>St  >  X<br>In the<br>money Payoff at  T<br>St =  X<br>St  <  X<br>At the<br>+ Out of the money<br>money<br>0 ST<br>X<br>–<br> -->
> **Chú thích hình ảnh:**
> - **Payoff/Profit:** Kết quả thanh toán / Lợi nhuận; **Payoff at $T$:** Kết quả thanh toán tại thời điểm đáo hạn $T$.
> - **Out of the money ($S_t < X$):** Trạng thái lỗ (OTM).
> - **At the money ($S_t = X$):** Trạng thái ngang giá (ATM).
> - **In the money ($S_t > X$):** Trạng thái có lời (ITM).

|**Trạng thái giá trị (*Moneyness*)**|**Quyền chọn mua (*Call option* – $c_t$)**|**Quyền chọn bán (*Put option* – $p_t$)**|
|---|---|---|
|Có lời (*In the money* – ITM)|$S_t > X$|$S_t < X$|
|Ngang giá (*At the money* – ATM)|$S_t = X$|$S_t = X$|
|Lỗ (*Out of the money* – OTM)|$S_t < X$|$S_t > X$|

###### **VÍ DỤ 2 (*EXAMPLE 2*)** 

###### **Trạng thái Giá trị của Quyền chọn Bán (*Put Option Moneyness*)** 

Hãy nhớ lại trong Ví dụ 1 rằng tại thời điểm $t$, một quyền chọn bán còn 6 tháng nữa là đáo hạn có giá thực hiện ($X$) là 1.000 EUR và giá giao ngay của tài sản cơ sở ($S_t$) là 950 EUR. Hãy mô tả trạng thái giá trị (*moneyness*) của quyền chọn bán tại thời điểm $t$. 

Vì giá giao ngay của tài sản cơ sở thấp hơn giá thực hiện, nên quyền chọn bán này đang ở trạng thái có lời (*in the money*) một khoản là 50 EUR. 

##### **GIÁ TRỊ THỜI GIAN CỦA QUYỀN CHỌN (*OPTION TIME VALUE*)** 

![](assets/Derivatives.pdf-0185-11.png)

<!-- Picture Text: 5<br> -->

giải thích giá trị thực hiện (*exercise value*), trạng thái giá trị (*moneyness*), và giá trị thời gian (*time value*) của một quyền chọn 

Trong khi giá trị thực hiện của một quyền chọn phản ánh kết quả thanh toán _hiện tại_ (*current payoff*) của nó, một thành phần bổ sung trong giá trị của quyền chọn được bắt nguồn từ _thời gian_ còn lại cho đến khi đáo hạn. Mặc dù các quyền chọn kiểu châu Âu chỉ có thể được thực hiện khi đáo hạn, chúng có thể được mua hoặc bán trước khi đáo hạn tại một mức giá ($c_t$ hoặc $p_t$, tương ứng cho quyền chọn mua hoặc quyền chọn bán) phản ánh kết quả thanh toán _dự kiến trong tương lai_ (*future expected payoff*) của quyền chọn. Thời gian còn lại cho đến khi đáo hạn càng dài thì thường đồng nghĩa với độ phân tán tiềm năng (*potential dispersion*) của giá tài sản cơ sở trong tương lai càng cao ứng với một mức độ biến động nhất định. 


<!-- PDF Page 186 -->

Tương tự như vậy, sự gia tăng độ biến động (*volatility*) tại một mức giá tài sản cơ sở cụ thể ứng với một khoảng thời gian đáo hạn nhất định sẽ làm tăng giá trị quyền chọn vì cùng một lý do đó. Chúng ta sẽ khám phá sâu hơn các nhân tố này trong một bài học sau. 

Giá trị thời gian (*time value*) của một quyền chọn bằng phần chênh lệch giữa giá quyền chọn hiện tại và kết quả thanh toán hiện tại (hay giá trị thực hiện) của quyền chọn đó: 

![](assets/Derivatives.pdf-0186-05.png)

<!-- Formula Text: Call Option Time Value: Max(0,   S t − X (1 + r) −(T−t)) (3) or: c t  =  Max(0,   S t − X (1 + r) −(T−t)) + Time Value Put Option Time Value: p t − Max(0,  X (1 + r) −(T−t) − S t) (4) or: p t  =  Max(0,  X (1 + r) −(T−t) − S t) + Time Value -->
$$\text{Giá trị thời gian của quyền chọn mua (Call Option Time Value): } c_t - \text{Max}\left(0, S_t - X(1 + r)^{-(T - t)}\right) \tag{3}$$

$$\text{hoặc: } c_t = \text{Max}\left(0, S_t - X(1 + r)^{-(T - t)}\right) + \text{Giá trị thời gian (Time Value)}$$

$$\text{Giá trị thời gian của quyền chọn bán (Put Option Time Value): } p_t - \text{Max}\left(0, X(1 + r)^{-(T - t)} - S_t\right) \tag{4}$$

$$\text{hoặc: } p_t = \text{Max}\left(0, X(1 + r)^{-(T - t)} - S_t\right) + \text{Giá trị thời gian (Time Value)}$$

Nghĩa là, giá quyền chọn hiện tại bằng tổng của giá trị thực hiện và giá trị thời gian của nó. Như Bảng 2 (*Exhibit 2*) cho thấy, giá trị thời gian của một quyền chọn luôn dương nhưng giảm dần về không khi đáo hạn, một quá trình được gọi là **sự hao mòn giá trị thời gian (*time value decay*)**. 

###### **Bảng 2: Giá trị Thực hiện và Giá trị Thời gian của một Quyền chọn Mua (*Exhibit 2: Exercise Value and Time Value of a Call Option*)** 

![](assets/Derivatives.pdf-0186-08.png)

<!-- Picture Text: St<br>X  =  F 0( T )<br>Exercise<br>value<br>X (1+ r ) –( T – t )<br>S 0<br>0 Time t T<br>Time value<br>0 Time t T<br>Ct  = Exercise value t + Time value t<br> -->
> **Chú thích hình ảnh:**
> - **Biểu đồ trên:** Biểu diễn đường giá tài sản cơ sở $S_t$, đường giá trị hiện tại của giá thực hiện $X(1+r)^{-(T-t)}$ tiến dần tới $X = F_0(T)$ tại ngày đáo hạn $T$, và khoảng cách chênh lệch là **Exercise value** (Giá trị thực hiện).
> - **Biểu đồ dưới:** Biểu diễn **Time value** (Giá trị thời gian) giảm dần về $0$ tại thời điểm đáo hạn $T$ ($c_t = \text{Exercise value}_t + \text{Time value}_t$).

###### **VÍ DỤ 3 (*EXAMPLE 3*)** 

###### **Giá trị Thời gian của Quyền chọn Bán (*Put Option Time Value*)** 

Ví dụ 1 đã chỉ ra rằng một quyền chọn bán kỳ hạn 1 năm có giá thực hiện ($X$) là 1.000 EUR có giá trị thực hiện là 45,04 EUR khi còn 6 tháng nữa là đáo hạn vào lúc giá giao ngay ($S_t$) ở mức 950 EUR. Nếu chúng ta quan sát thấy mức giá quyền chọn bán hiện tại ($p_t$) là 50 EUR, thì giá trị thời gian của quyền chọn bán này là bao nhiêu? 

Sử dụng Phương trình 4 để giải tìm $p_t - \text{Max}(0, \text{PV}(X) - S_t)$: 

<!-- PDF Page 187 -->

$$p_t - \text{Max}\left(0, X(1 + r)^{-(T - t)} - S_t\right) = 4,96\text{ EUR} \ (= 50\text{ EUR} - 45,04\text{ EUR})$$

###### **BỘ CÂU HỎI (*QUESTION SET*)**
###### **Giá trị Quyền chọn so với Giá Giao ngay của Tài sản Cơ sở (*Option Value relative to Underlying Spot Price*)**

1. Mô tả những điểm tương đồng và khác biệt giữa giá trị thực hiện của một vị thế mua quyền chọn bán (*long put option position*) có giá thực hiện ($X$) bằng với giá kỳ hạn, $F_0(T)$, và kết quả thanh toán của một vị thế bán kỳ hạn (*short forward position*) khi đáo hạn có cùng các thông số tài sản cơ sở.

###### **Lời giải:**

Giá trị thực hiện của một quyền chọn bán có giá thực hiện $X = F_0(T)$ khi đáo hạn ($\text{Max}(0, X - S_T)$) là _giống hệt_ như kết quả thanh toán của một cam kết bán kỳ hạn khi đáo hạn ($F_0(T) - S_T$) _miễn là_ giá thực hiện lớn hơn giá tài sản cơ sở. Nghĩa là, với $F_0(T) = X$:
Nếu $X > S_T$: $F_0(T) - S_T = \text{Max}(0, X - S_T)$.
Các hồ sơ kết quả thanh toán này sẽ _khác nhau_ nếu $S_T > X$, bởi vì kết quả thanh toán của vị thế bán kỳ hạn khi đáo hạn sẽ đòi hỏi một khoản thanh toán từ người bán cho người mua, trong khi người sở hữu quyền chọn bán sẽ để quyền chọn hết hạn mà không thực hiện. Lưu ý rằng phép so sánh kết quả thanh toán này bỏ qua khoản phí quyền chọn trả trước do người mua quyền chọn bán trả ($p_0$) tại thời điểm $t = 0$.

2. Một quyền chọn bán kiểu châu Âu (*European put option*) còn 3 tháng nữa là đáo hạn trên một cổ phiếu cơ sở không có dòng tiền bổ sung có giá thực hiện ($X$) là 50 GBP, lãi suất phi rủi ro là 2%, và giá tài sản cơ sở hiện tại ($S_t$) là 55 GBP. Nếu giá quyền chọn bán hiện tại là 5 GBP, hãy tính giá trị thực hiện và giá trị thời gian, đồng thời diễn giải kết quả.

###### **Lời giải:**

Giá trị của một quyền chọn bao gồm giá trị thực hiện cộng với giá trị thời gian của nó. Giá trị thực hiện của một quyền chọn bán là $\text{Max}(0, \text{PV}(X) - S_t)$ và có thể được tính như sau:

$$\text{Giá trị thực hiện của quyền chọn bán (Put Option Exercise Value)} = \text{Max}\left(0, X(1 + r)^{-(T - t)} - S_t\right)$$

$$= \text{Max}\left(0, 50\text{ GBP}(1,02)^{-0,25} - 55\text{ GBP}\right) = 0$$

Giá trị thực hiện bằng không, vì giá tài sản cơ sở hiện tại vượt quá giá trị hiện tại của giá thực hiện. Giá trị thời gian là phần chênh lệch giữa giá quyền chọn và giá trị thực hiện, đại diện cho khả năng xác suất và mức sinh lời của việc thực hiện quyền khi đáo hạn có thể tăng lên nhờ một sự biến động giá thuận lợi:

$$\text{Giá trị thời gian của quyền chọn bán (Put Option Time Value)} = p_t - \text{Max}\left(0, X(1 + r)^{-(T - t)} - S_t\right)$$


<!-- PDF Page 188 -->

$$= 5\text{ GBP} \ (= 5\text{ GBP} - 0\text{ GBP})$$

Giá trị thời gian luôn dương và giảm dần về không khi đáo hạn ($t = T$). Vì quyền chọn bán đang ở trạng thái lỗ (*out of the money*), giá trị của nó _chỉ_ bao gồm giá trị thời gian. 

3. Hãy ghép các mối quan hệ giữa giá tài sản cơ sở và giá thực hiện sau đây với quyền chọn mua (*call option*) tương ứng của chúng: 

| Mối quan hệ giữa $S_T$ và $X$ | Trạng thái của quyền chọn mua |
|---|---|
| 1. $S_T = 60, X = 50$ | A. Quyền chọn mua ngang giá (*At-the-money call option*) |
| 2. $S_T = 50, X = 50$ | B. Quyền chọn mua có lời (*In-the-money call option*) |
| 3. $S_T = 40, X = 50$ | C. Quyền chọn mua lỗ (*Out-of-the-money call option*) |

###### **Lời giải:** 

Quyền chọn mua ở trạng thái có lời (*in the money*) khi $S_T > X$, ngang giá (*at the money*) khi $S_T = X$, và lỗ (*out of the money*) khi $S_T < X$. Do đó: 

   **1.** B là đáp án đúng. Vì $S_T > X$, đây là một quyền chọn mua có lời (*in-the-money call option*). 

   **2.** A là đáp án đúng. Vì $S_T = X = 50$, đây là một quyền chọn mua ngang giá (*at-the-money call option*). 

   **3.** C là đáp án đúng. Vì $S_T < X$, đây là một quyền chọn mua lỗ (*out-of-the-money call option*). 

4. Mô tả cách thức trạng thái giá trị (*moneyness*) của một quyền chọn ảnh hưởng đến mức thay đổi giá trị của quyền chọn đó ứng với một mức thay đổi nhất định trong giá của tài sản cơ sở. 

###### **Lời giải:** 

Sự gia tăng trong trạng thái giá trị (*moneyness*) của một quyền chọn sẽ làm tăng độ nhạy của giá trị quyền chọn đó trước những thay đổi trong giá tài sản cơ sở. Ví dụ, một quyền chọn có khả năng rất cao sẽ được thực hiện sẽ có mức thay đổi giá trị quyền chọn gần như theo tỷ lệ một-đổi-một ứng với một mức thay đổi nhất định trong giá tài sản cơ sở, trong khi một quyền chọn ít có khả năng được thực hiện sẽ có mức thay đổi giá trị tương đối nhỏ ứng với một mức thay đổi nhất định trong giá tài sản cơ sở. 

## **<mark>6</mark>** 

##### **KINH DOANH CHÊNH LỆCH GIÁ (*ARBITRAGE*)** 

đối chiếu việc sử dụng các khái niệm kinh doanh chênh lệch giá (*arbitrage*) và mô phỏng (*replication*) trong việc định giá các cam kết kỳ hạn (*forward commitments*) và các quyền đòi nợ có điều kiện (*contingent claims*) 

Một bài học trước đã chỉ ra rằng các cơ hội kinh doanh chênh lệch giá phi rủi ro (*riskless arbitrage opportunities*) sẽ phát sinh nếu “quy luật một giá” (*“law of one price”*) không được duy trì—nghĩa là một tài sản giống hệt nhau được giao dịch tại các mức giá khác nhau ở các nơi khác nhau vào cùng một thời điểm. Trong trường hợp của một công cụ phái sinh, chúng ta thiết lập các điều kiện không kinh doanh chênh lệch giá (*no-arbitrage conditions*) dựa trên hồ sơ kết quả thanh toán khi đáo hạn. Như đã chỉ ra trước đó, các cam kết kỳ hạn với hồ sơ kết quả thanh toán _đối xứng_ (*symmetric payoff profile*) được thanh toán dựa trên chênh lệch giữa giá kỳ hạn, $F_0(T)$, tại thời điểm khởi tạo hợp đồng ($t = 0$) và giá tài sản cơ sở, $S_T$, khi hợp đồng đáo hạn ($t = T$), hay $(S_T - F_0(T))$ đối với vị thế mua kỳ hạn. Đối với một tài sản cơ sở không có dòng tiền bổ sung, chúng ta đã chứng minh rằng các tài sản có mức giá tương lai đã biết phải có giá giao ngay bằng với giá tương lai được chiết khấu theo lãi suất phi rủi ro, $r$: $S_0 = S_T(1 + r)^{-T}$. Cho mục đích của bài học này, chúng ta bỏ qua mọi chi phí hoặc lợi ích của việc sở hữu tài sản cơ sở ngoài chi phí cơ hội (hay lãi suất phi rủi ro, $r$). 


<!-- PDF Page 189 -->

Các quyền đòi nợ có điều kiện (*contingent claims*) có đặc trưng là hồ sơ kết quả thanh toán _bất đối xứng_ (*asymmetric payoff profiles*), như đã giới thiệu trước đó. Trong trường hợp của các quyền chọn kiểu châu Âu đại diện cho quyền được mua một tài sản cơ sở (hay quyền chọn mua, $c$) hoặc quyền được bán một tài sản cơ sở (hay quyền chọn bán, $p$) tại một mức giá thực hiện nhất định ($X$) khi đáo hạn, hồ sơ kết quả thanh toán khi đáo hạn đối với người mua quyền chọn đã được chỉ ra là: 

![](assets/Derivatives.pdf-0189-04.png)

<!-- Formula Text: cT = Max (0, ST − X) (5) -->
$$c_T = \text{Max}(0, S_T - X) \tag{5}$$

![](assets/Derivatives.pdf-0189-05.png)

<!-- Formula Text: pT = Max (0, X − ST) (6) -->
$$p_T = \text{Max}(0, X - S_T) \tag{6}$$

**Bảng 3: Thực hiện Quyền chọn Kiểu châu Âu khi Đáo hạn (*Exhibit 3: European Option Exercise at Expiration*)** 

![](assets/Derivatives.pdf-0189-07.png)

<!-- Picture Text: cT > 0<br>ST  >  X<br>PT = 0<br>X ST<br>X  >  ST PT > 0<br>cT = 0<br>S 0<br>0 time T<br> -->
> **Chú thích hình ảnh:**
> - Khi $S_T > X$: Quyền chọn mua được thực hiện ($c_T > 0$), quyền chọn bán không được thực hiện ($p_T = 0$).
> - Khi $X > S_T$: Quyền chọn bán được thực hiện ($p_T > 0$), quyền chọn mua không được thực hiện ($c_T = 0$).

Hãy nhớ lại rằng, không giống như các cam kết kỳ hạn có mức giá ban đầu bằng không, người mua quyền chọn phải trả cho người bán một khoản phí quyền chọn ($c_0$ đối với quyền chọn mua và $p_0$ đối với quyền chọn bán tại thời điểm $t = 0$), vì vậy _lợi nhuận_ (*profit*) của người mua quyền chọn khi đáo hạn đã được giới thiệu trước đó như sau (bỏ qua giá trị thời gian của tiền tệ): 

![](assets/Derivatives.pdf-0189-09.png)

<!-- Formula Text: Π = Max (0, ST − X) − c0 (7) -->
$$\Pi = \text{Max}(0, S_T - X) - c_0 \tag{7}$$

![](assets/Derivatives.pdf-0189-10.png)

<!-- Formula Text: Π = Max (0, X − ST) − p0 (8) -->
$$\Pi = \text{Max}(0, X - S_T) - p_0 \tag{8}$$

Phương trình 7 và 8 cho thấy điểm khác biệt then chốt giữa các cam kết kỳ hạn và các quyền đòi nợ có điều kiện xét theo mục đích kinh doanh chênh lệch giá. Người mua kỳ hạn tham gia vào hợp đồng mà không phải trả tiền mặt trả trước và có khoản lãi hoặc lỗ không giới hạn (được chặn dưới bởi số không đối với một tài sản cơ sở như cổ phiếu vốn không thể có giá âm) khi đáo hạn lúc giá tài sản cơ sở tăng hoặc giảm. Ngược lại, người mua quyền chọn sẽ chỉ thực hiện quyền chọn khi đáo hạn nếu nó ở trạng thái có lời (*in the money*). Bản chất _có điều kiện_ (*conditional nature*) này của hồ sơ kết quả thanh toán quyền chọn dẫn chúng ta đến việc thiết lập các cận giá trên và cận giá dưới không có kinh doanh chênh lệch giá (*upper and lower no-arbitrage price bounds*) tại bất kỳ thời điểm $t$ nào. 

Người mua quyền chọn mua sẽ chỉ thực hiện quyền nếu giá giao ngay ($S_T$) vượt quá giá thực hiện ($X$) khi đáo hạn. Do đó, cận _dưới_ (*lower bound*) của giá quyền chọn mua là giá của tài sản cơ sở trừ đi giá trị hiện tại của giá thực hiện hoặc bằng không, tùy theo giá trị nào lớn hơn. Nói cách khác, một quyền chọn giao dịch dưới mức giá trị thực hiện của nó sẽ vi phạm điều kiện không kinh doanh chênh lệch giá. Người mua quyền chọn mua sẽ không trả nhiều tiền hơn cho quyền được mua một tài sản cơ sở so với chính mức giá của tài sản cơ sở đó, vốn là cận _trên_ (*upper bound*): 

![](assets/Derivatives.pdf-0189-13.png)

<!-- Formula Text: Max(0,   S t − X (1 + r) −(T−t))  <  c t  ≤  S t (9) c t,Lower bound  =  Max(0,   S t − X (1 + r) −(T−t)) (10) c t,Upper bound=S t (11) -->
$$\text{Max}\left(0, S_t - X(1 + r)^{-(T - t)}\right) < c_t \le S_t \tag{9}$$

$$c_{t,\text{Lower bound}} = \text{Max}\left(0, S_t - X(1 + r)^{-(T - t)}\right) \tag{10}$$

$$c_{t,\text{Upper bound}} = S_t \tag{11}$$


<!-- PDF Page 190 -->

Người mua quyền chọn bán sẽ chỉ thực hiện quyền nếu giá giao ngay, $S_T$, thấp hơn $X$ khi đáo hạn. Do đó, giá thực hiện, $X$, đại diện cho cận _trên_ (*upper bound*) đối với giá trị quyền chọn bán. Cận _dưới_ (*lower bound*) là giá trị hiện tại của giá thực hiện trừ đi giá giao ngay hoặc bằng không, tùy theo giá trị nào lớn hơn: 

![](assets/Derivatives.pdf-0190-04.png)

<!-- Formula Text: Max(0,  X (1 + r) −(T−t) − S t)  <  p t  ≤  X (12) -->
$$\text{Max}\left(0, X(1 + r)^{-(T - t)} - S_t\right) < p_t \le X \tag{12}$$

![](assets/Derivatives.pdf-0190-05.png)

<!-- Formula Text: p t,Lower bound  =  Max(0,  X (1 + r) −(T−t) − S t) (13) -->
$$p_{t,\text{Lower bound}} = \text{Max}\left(0, X(1 + r)^{-(T - t)} - S_t\right) \tag{13}$$

![](assets/Derivatives.pdf-0190-06.png)

<!-- Formula Text: p t,Upper bound  =  X (14) -->
$$p_{t,\text{Upper bound}} = X \tag{14}$$

###### **VÍ DỤ 4 (*EXAMPLE 4*)** 

###### **Cận Trên và Cận Dưới của Quyền chọn Mua (*Call Option Upper and Lower Bounds*)** 

Hãy xem xét một quyền chọn mua kỳ hạn 1 năm có giá thực hiện, $X$, là 1.000 EUR. Tài sản cơ sở, $S_0$, giao dịch ở mức 990 EUR tại thời điểm $t = 0$ và lãi suất phi rủi ro, $r$, là 1%. Cận trên và cận dưới không kinh doanh chênh lệch giá sau thời gian 6 tháng là bao nhiêu nếu giá tài sản cơ sở, $S_t$, bằng 1.050 EUR? 

Vì người mua quyền chọn sẽ chỉ thực hiện quyền nếu $S_T > X$ tại thời điểm $t = T$, nên cận _dưới_ bằng $S_t - \text{PV}(X)$ hoặc bằng không, tùy theo giá trị nào lớn hơn: 

$$c_{t,\text{Lower bound}} = \text{Max}\left(0, S_t - X(1 + r)^{-(T - t)}\right)$$

$$c_{t,\text{Lower bound}} = \text{Max}\left(0, 1.050\text{ EUR} - 1.000\text{ EUR}(1,01)^{-0,5}\right)$$

$$c_{t,\text{Lower bound}} = \text{Max}(0, 54,96\text{ EUR}) = 54,96\text{ EUR}$$

Người mua quyền chọn mua sẽ không trả nhiều hơn $S_t$ cho quyền được mua tài sản cơ sở: 

$$c_{t,\text{Upper bound}} = S_t = 1.050\text{ EUR}$$

## **<mark>7</mark>** 

##### **MÔ PHỎNG (*REPLICATION*)** 

đối chiếu việc sử dụng các khái niệm kinh doanh chênh lệch giá (*arbitrage*) và mô phỏng (*replication*) trong việc định giá các cam kết kỳ hạn (*forward commitments*) và các quyền đòi nợ có điều kiện (*contingent claims*) 

Trong một bài học trước, chúng ta đã sử dụng phương pháp mô phỏng (*replication*) để tạo ra các dòng tiền của cam kết kỳ hạn, bằng cách tận dụng sự kết hợp giữa các vị thế mua hoặc bán trên một tài sản cơ sở cùng với việc đi vay hoặc cho vay tiền mặt. Khả năng sử dụng các chiến lược mô phỏng của những người tham gia thị trường đảm bảo rằng quy luật một giá được duy trì và không tồn tại cơ hội thu lợi nhuận kinh doanh chênh lệch giá phi rủi ro. 

Hãy nhớ lại từ bài học trước rằng một quyền chọn mua _tương tự như_ một vị thế mua kỳ hạn (*long forward position*) ở chỗ nó tăng giá trị khi giá tài sản cơ sở tăng lên nhưng _khác biệt_ ở chỗ quyền chọn mua chỉ thanh toán nếu có khoản lãi khi thực hiện quyền. Sự đối xứng bề ngoài này đối với các kết quả dương được thể hiện trong Bảng 4 (*Exhibit 4*), nơi giá thực hiện, $X$, bằng với giá kỳ hạn, $F_0(T)$. 


<!-- PDF Page 191 -->

###### **Bảng 4: Quyền chọn Mua so với Vị thế Mua Kỳ hạn (*Exhibit 4: Call Option versus Long Forward Position*)** 

![](assets/Derivatives.pdf-0191-04.png)

<!-- Picture Text: Payoff/ Forward<br>Profit profit<br>+ Option<br>payoff<br>0 ST<br>Option<br>– profit X  =  F 0( T )<br>ST > X :<br>VT  = ( ST  –  F 0( T )) > 0<br>cT  = ( ST  –  X ) > 0<br>X  =  F 0( T )<br>ST < X :<br>VT  = ( ST  –  F 0( T )) < 0<br>cT  = 0<br>S0<br>0 Time T<br> -->
> **Chú thích hình ảnh:**
> - **Khi $S_T > X = F_0(T)$:** Cả vị thế mua kỳ hạn và quyền chọn mua đều có kết quả thanh toán dương: $V_T = (S_T - F_0(T)) > 0$ và $c_T = (S_T - X) > 0$.
> - **Khi $S_T < X = F_0(T)$:** Vị thế mua kỳ hạn bị lỗ $V_T = (S_T - F_0(T)) < 0$, trong khi kết quả thanh toán của quyền chọn mua bằng không ($c_T = 0$).

Để mô phỏng quyền chọn mua tại thời điểm khởi tạo hợp đồng ($t = 0$), chúng ta cũng phải đi vay ở mức lãi suất phi rủi ro, $r$, và sử dụng số tiền thu được để mua tài sản cơ sở tại mức giá $S_0$. Khi quyền chọn đáo hạn ($t = T$), không giống như trong trường hợp của cam kết kỳ hạn, có hai kết quả mô phỏng có thể xảy ra: 

- **Thực hiện quyền (*Exercise*)** ($S_T > X$): Bán tài sản cơ sở lấy $S_T$ và sử dụng số tiền thu được để hoàn trả khoản vay $X$. 

- **Không thực hiện quyền (*No exercise*)** ($S_T < X$): Không cần thực hiện thanh toán. 

Nếu việc thực hiện quyền là chắc chắn, chúng ta sẽ vay $X(1 + r)^{-T}$ tại thời điểm khởi tạo, giống như trong trường hợp của hợp đồng kỳ hạn. Tuy nhiên, vì việc này là không chắc chắn, thay vào đó chúng ta chỉ vay một _tỷ lệ_ (*proportion*) của $X(1 + r)^{-T}$ dựa trên _xác suất_ (*likelihood*) thực hiện quyền tại thời điểm $T$, vốn gắn liền mật thiết với trạng thái giá trị (*moneyness*) của quyền chọn. Hồ sơ kết quả thanh toán phi tuyến tính của một quyền chọn đòi hỏi giao dịch mô phỏng phải được điều chỉnh khi xác suất này thay đổi, trong khi các giao dịch mô phỏng cho một cam kết kỳ hạn vẫn giữ nguyên không đổi. Việc mô phỏng quyền chọn sẽ được đề cập chi tiết hơn trong các bài học sau. 

Bây giờ chúng ta chuyển sự chú ý sang việc mô phỏng quyền chọn bán (*put option replication*). Trước đó chúng ta đã chỉ ra rằng một vị thế _bán_ quyền chọn bán (*short put position*) có giá thực hiện bằng với giá kỳ hạn ($X = F_0(T)$) phản chiếu các kết quả của một vị thế _mua_ kỳ hạn (*long forward position*) khi giá tài sản cơ sở lúc đáo hạn _thấp hơn_ giá kỳ hạn ($S_T < X = F_0(T)$). Quyền chọn bán đã bán sẽ _giảm_ giá trị (tức tăng khoản lỗ cho người bán quyền chọn bán, hoặc quyền chọn bán tăng giá trị đối với người mua quyền chọn bán) khi giá tài sản cơ sở giảm xuống, nhưng nó chỉ được thanh toán nếu có khoản lãi khi thực hiện quyền. Mối quan hệ này được thể hiện trong Bảng 5 (*Exhibit 5*), nơi giá thực hiện ($X$) bằng với giá kỳ hạn, $F_0(T)$. 


<!-- PDF Page 192 -->

**Bảng 5: Quyền chọn Bán so với Vị thế Bán Kỳ hạn (*Exhibit 5: Put Option versus Short Forward Position*)** 

![](assets/Derivatives.pdf-0192-04.png)

<!-- Picture Text: Payoff/ Forward<br>Profit profit<br>+ Option<br>profit<br>0 ST<br>Option<br>– payoff<br>X  =  F 0( T )<br>ST > X :<br>VT  = ( ST  –  F 0( T )) > 0<br>– pT  = 0<br>X  =  F 0( T )<br>ST < X :<br>VT  = ( ST  –  F 0( T )) < 0<br>– pT  = ( X  –  ST ) < 0<br>S 0<br>0 Time T<br> -->
> **Chú thích hình ảnh:**
> - **Khi $S_T > X = F_0(T)$:** Vị thế mua kỳ hạn có $V_T = (S_T - F_0(T)) > 0$, vị thế bán quyền chọn bán có $-p_T = 0$.
> - **Khi $S_T < X = F_0(T)$:** Vị thế mua kỳ hạn có $V_T = (S_T - F_0(T)) < 0$, vị thế bán quyền chọn bán có $-p_T = -(X - S_T) < 0$ (và người mua quyền chọn bán nhận $p_T = X - S_T > 0$).

Để mô phỏng quyền chọn bán (vị thế mua quyền chọn bán) tại thời điểm khởi tạo hợp đồng ($t = 0$), chúng ta phải bán khống (*sell short*) tài sản cơ sở tại mức giá $S_0$ và đem số tiền thu được cho vay ở mức lãi suất phi rủi ro, $r$. Khi quyền chọn đáo hạn ($t = T$), không giống như trong trường hợp của cam kết kỳ hạn, có hai kết quả mô phỏng có thể xảy ra: 

- **Thực hiện quyền (*Exercise*)** ($S_T < X$): Mua lại tài sản cơ sở với giá $S_T$ từ số tiền thu được của khoản cho vay phi rủi ro. 

- **Không thực hiện quyền (*No exercise*)** ($S_T > X$): Không cần thực hiện thanh toán. 

Nếu việc thực hiện quyền là chắc chắn, chúng ta sẽ cho vay $X(1 + r)^{-T}$ tại thời điểm khởi tạo, giống như trong trường hợp của hợp đồng kỳ hạn. Tuy nhiên, giống như trong trường hợp của quyền chọn mua, hồ sơ kết quả thanh toán bất đối xứng đòi hỏi phải có sự điều chỉnh theo thời gian dựa trên _xác suất_ (*likelihood*) thực hiện quyền. 

Trong bài học tiếp theo, chúng ta sẽ chuyển sự chú ý sang các nhân tố thúc đẩy xác suất thực hiện quyền chọn trước khi đáo hạn. 

###### **BỘ CÂU HỎI (*QUESTION SET*)** 

###### **Kinh doanh Chênh lệch giá và Mô phỏng (*Arbitrage and Replication*)** 

1. Xác định các câu trả lời đúng để hoàn thành câu sau đây: Cận dưới của giá quyền chọn mua là giá của tài sản cơ sở ______ giá trị hiện tại của giá ________ của nó hoặc bằng không, tùy theo giá trị nào lớn hơn. 

###### **Lời giải:** 

Cận dưới của giá quyền chọn mua là giá của tài sản cơ sở _trừ đi (minus)_ giá trị hiện tại của giá _thực hiện (exercise)_ của nó hoặc bằng không, tùy theo giá trị nào lớn hơn. 

2. Một quyền chọn mua kiểu châu Âu kỳ hạn 6 tháng trên một cổ phiếu cơ sở không có dòng tiền bổ sung có giá thực hiện ($X$) <u>là 50 GBP, giá tài sản cơ sở ban đầu</u> 


<!-- PDF Page 193 -->

($S_0$) là 49,75 GBP, và lãi suất phi rủi ro là 2%. Hãy tính cận dưới của giá quyền chọn mua sau thời gian 3 tháng nếu $S_t = 65\text{ GBP}$. 

###### **Lời giải:** 

Vì người mua quyền chọn mua sẽ chỉ thực hiện quyền nếu $S_T > X$ khi đáo hạn, nên cận dưới bằng $S_t - \text{PV}(X)$ hoặc bằng không sau thời gian 3 tháng, tùy theo giá trị nào lớn hơn: 

$$c_{t,\text{Lower bound}} = \text{Max}\left(0, S_t - X(1 + r)^{-(T - t)}\right)$$

Với $S_t = 65\text{ GBP}$, $X = 50\text{ GBP}$, $r = 2\%$, và $(T - t) = 0,25$, chúng ta có thể giải tìm cận dưới của quyền chọn mua như sau: 

$$c_{t,\text{Lower bound}} = \text{Max}\left(0, 65\text{ GBP} - 50\text{ GBP}(1,02)^{-0,25}\right) = 15,25\text{ GBP}$$

3. Hãy ghép các phát biểu sau đây về chiến lược mô phỏng với (các) công cụ phái sinh tương ứng của chúng: 

| Phát biểu về chiến lược mô phỏng | Công cụ phái sinh tương ứng |
|---|---|
| 1. Tại thời điểm $t = 0$, đi vay ở mức lãi suất phi rủi ro và mua tài sản cơ sở tại giá $S_0$. | A. Chiến lược mô phỏng cả quyền chọn mua và quyền chọn bán |
| 2. Chiến lược đòi hỏi phải có sự điều chỉnh theo thời gian khi xác suất thực hiện quyền thay đổi. | B. Chiến lược mô phỏng quyền chọn mua (*call option replication strategy*) |
| 3. Tại thời điểm $t = T$, nhận tiền hoàn trả khoản cho vay và mua tài sản cơ sở tại giá $S_T$. | C. Chiến lược mô phỏng quyền chọn bán (*put option replication strategy*) nếu được thực hiện |

###### **Lời giải:** 

   **1.** B là đáp án đúng. Tại thời điểm $t = 0$, chiến lược mô phỏng quyền chọn mua bao gồm việc đi vay ở mức lãi suất phi rủi ro và mua tài sản cơ sở. 

   **2.** A là đáp án đúng. Vì cả quyền chọn mua và quyền chọn bán đều có hồ sơ kết quả thanh toán phi tuyến tính, chiến lược mô phỏng đòi hỏi phải có sự điều chỉnh theo thời gian khi xác suất thực hiện quyền thay đổi. 

   **3.** C là đáp án đúng. Chiến lược mô phỏng quyền chọn bán nếu được thực hiện bao gồm việc nhận tiền hoàn trả khoản cho vay và mua tài sản cơ sở tại giá $S_T$ vào thời điểm $t = T$. 

4. Giải thích điểm khác biệt then chốt giữa những thay đổi trong việc mô phỏng một quyền đòi nợ có điều kiện (*contingent claim*) so với một cam kết kỳ hạn (*forward commitment*) trong suốt vòng đời của hợp đồng. 

###### **Lời giải:** 

Một quyền chọn có hồ sơ kết quả thanh toán _bất đối xứng_ (*asymmetric*), bởi vì người mua quyền chọn sẽ chỉ thực hiện quyền nếu giá trị thực hiện của quyền chọn mang số dương. Vì xác suất thực hiện quyền chọn thay đổi theo thời gian, các giao dịch mô phỏng một hợp đồng quyền chọn phải được điều chỉnh theo thời gian. Một cam kết kỳ hạn có hồ sơ kết quả thanh toán _đối xứng_ (*symmetric*) chắc chắn sẽ được thanh toán vào một ngày trong tương lai, và do đó các giao dịch mô phỏng không đòi hỏi phải điều chỉnh trong suốt vòng đời của hợp đồng. 


---

# Tập 7: Công cụ Phái sinh (*Derivatives*)
## Học phần 8: Định giá và Xác định giá trị của Quyền chọn (*Pricing and Valuation of Options*)
### Phần 2/2: Các Nhân tố Ảnh hưởng đến Giá trị Quyền chọn (Trang PDF 194–204)

---

<!-- PDF Page 194 -->

# **<mark>8</mark>** 

#### **CÁC NHÂN TỐ ẢNH HƯỞNG ĐẾN GIÁ TRỊ QUYỀN CHỌN (*FACTORS AFFECTING OPTION VALUE*)** 

xác định các nhân tố quyết định giá trị của một quyền chọn và mô tả cách thức mỗi nhân tố ảnh hưởng đến giá trị của một quyền chọn 

Bây giờ chúng ta chuyển sự chú ý sang việc xác định và mô tả các nhân tố ảnh hưởng đến giá trị của một quyền chọn. Một số nhân tố trong số này là điểm chung của cả các cam kết kỳ hạn (*forward commitments*) và các quyền chọn (*options*), và một số nhân tố là nét đặc thù riêng của các quyền đòi nợ có điều kiện (*contingent claims*). Các nhân tố quyết định giá trị của một quyền chọn bao gồm giá trị của tài sản cơ sở (*value of the underlying*), giá thực hiện (*exercise price*), thời gian đến khi đáo hạn (*time to maturity*), lãi suất phi rủi ro (*risk-free rate*), độ biến động giá của tài sản cơ sở (*volatility of the underlying price*), và bất kỳ khoản thu nhập hoặc chi phí nào gắn liền với việc sở hữu tài sản cơ sở. 

##### **Giá trị của Tài sản Cơ sở (*Value of the Underlying*)** 

Những thay đổi trong giá trị của tài sản cơ sở sẽ có tác động cùng chiều lên _quyền_ giao dịch tài sản cơ sở theo hợp đồng quyền chọn giống như tác động lên _nghĩa vụ_ giao dịch theo một cam kết kỳ hạn. Ví dụ, một quyền chọn mua (*call option*) và một vị thế mua kỳ hạn (*long forward position*) sẽ cùng _tăng giá trị_ (*appreciate*) nếu giá giao ngay của tài sản cơ sở _tăng lên_, trong khi một quyền chọn bán (*put option*) và một vị thế bán kỳ hạn (*short forward position*) sẽ cùng _tăng giá trị_ nếu giá giao ngay của tài sản cơ sở _giảm xuống_, như được minh họa trong Bảng 6 (*Exhibit 6*). 

**Bảng 6: Giá trị Quyền chọn Mua và Quyền chọn Bán so với Giá trị Tài sản Cơ sở (*Exhibit 6: Call and Put Option Value versus Underlying Value*)** 

![](assets/Derivatives.pdf-0194-10.png)

<!-- Picture Text: Option value ( t  < T )<br>Payoff/<br>Profit Call option Payoff at  T<br>+<br>0 ST<br>–<br>X<br>Payoff/ Put option<br>Profit<br>+ Option value ( t < T )<br>0 ST Payoff at  T<br>–<br>X<br> -->
> **Chú thích hình ảnh:**
> - **Đồ thị trên (Call option – Quyền chọn mua):** Đường cong **Option value ($t < T$)** (Giá trị quyền chọn trước khi đáo hạn) nằm phía trên đường gấp khúc **Payoff at $T$** (Kết quả thanh toán khi đáo hạn) và dốc lên khi $S_T$ tăng.
> - **Đồ thị dưới (Put option – Quyền chọn bán):** Đường cong **Option value ($t < T$)** và đường gấp khúc **Payoff at $T$** dốc xuống khi $S_T$ tăng (tức tăng giá trị khi $S_T$ giảm).


<!-- PDF Page 195 -->

Một điểm khác biệt quan trọng giữa các cam kết kỳ hạn và các quyền đòi nợ có điều kiện là _độ lớn_ (*magnitude*) của mức thay đổi giá công cụ phái sinh ứng với một mức thay đổi nhất định trong giá trị tài sản cơ sở. Đối với một cam kết kỳ hạn, giá trị của công cụ phái sinh là một hàm _tuyến tính_ (*linear*, một-đổi-một) theo giá tài sản cơ sở, trong khi đối với một quyền chọn, đó là một mối quan hệ _phi tuyến tính_ (*non-linear*) phụ thuộc vào xác suất người mua quyền chọn sẽ thực hiện quyền trong tương lai. Khả năng người mua quyền chọn sẽ thực hiện quyền càng cao (ví dụ: khi quyền chọn đang ở trạng thái có lời – *in the money*), thì giá trị của quyền chọn càng nhạy cảm với giá tài sản cơ sở. Khả năng này phụ thuộc vào mối quan hệ giữa giá trị của tài sản cơ sở và giá thực hiện, một đặc điểm độc nhất của các hợp đồng quyền chọn mà chúng ta sẽ tìm hiểu tiếp theo. 

##### **Giá Thực hiện (*Exercise Price*)** 

Giá thực hiện (*exercise price*) là ngưỡng quyết định liệu người mua quyền chọn có lựa chọn thực hiện giao dịch khi hợp đồng đáo hạn hay không. Đối với một quyền chọn mua đại diện cho quyền được mua tài sản cơ sở, giá thực hiện đại diện cho một cận _dưới_ (*lower bound*) đối với giá trị thực hiện của quyền chọn khi đáo hạn, dẫn đến giá trị quyền chọn _cao hơn_ khi giá thực hiện _thấp hơn_. Vì các quyền chọn mua được thanh toán dựa trên $\text{Max}(0, S_T - X)$ khi đáo hạn, một mức $X$ thấp hơn sẽ làm tăng cả xác suất thực hiện quyền lẫn giá trị thanh toán nếu được thực hiện. 

Ngược lại, giá thực hiện của một quyền chọn bán là một cận _trên_ (*upper bound*) đối với giá trị thực hiện của nó khi đáo hạn. Do đó, một mức giá thực hiện _cao hơn_ mà tại đó người mua quyền chọn bán có quyền bán tài sản cơ sở sẽ _làm tăng_ giá trị của quyền chọn bán. Bảng 7 (*Exhibit 7*) thể hiện những tác động khác nhau này của sự thay đổi giá thực hiện đối với cả quyền chọn mua và quyền chọn bán. 

**Bảng 7: Giá trị Quyền chọn Mua và Quyền chọn Bán so với Giá Thực hiện (*Exhibit 7: Call and Put Option Value versus Exercise Price*)** 

![](assets/Derivatives.pdf-0195-08.png)

<!-- Picture Text: Payoff at  T<br>Call option<br>Payoff/<br>Profit<br>+<br>0 ST<br>–<br>X – X<br>Put option<br>Payoff/<br>Profit<br>Payoff at  T<br>+<br>0 ST<br>–<br>X X +<br> -->
> **Chú thích hình ảnh:**
> - **Đồ thị trên (Call option):** Khi giá thực hiện giảm từ $X$ xuống $X^-$, đường kết quả thanh toán và giá trị quyền chọn mua dịch chuyển sang trái (tăng giá trị).
> - **Đồ thị dưới (Put option):** Khi giá thực hiện tăng từ $X$ lên $X^+$, đường kết quả thanh toán và giá trị quyền chọn bán dịch chuyển sang phải (tăng giá trị).


<!-- PDF Page 196 -->

##### **Thời gian đến khi Đáo hạn (*Time to Expiration*)** 

Hãy nhớ lại từ bài học trước rằng giá trị thời gian (*time value*), hay phần chênh lệch giữa giá của một quyền chọn và giá trị thực hiện của nó, đại diện cho khả năng những thay đổi thuận lợi trong giá tài sản cơ sở sẽ làm tăng mức sinh lời của việc thực hiện quyền. Không giống như một vị thế mua kỳ hạn (*long forward position*) nơi người mua có khả năng ngang nhau trong việc trải qua sự tăng giá hoặc giảm giá của tài sản cơ sở trong một khoảng thời gian dài hơn, hồ sơ kết quả thanh toán một phía (hay bất đối xứng – *one-sided or asymmetric payoff profile*) của quyền chọn cho phép người mua bỏ qua bất kỳ kết quả nào mà tại đó quyền chọn hết hạn mà không được thực hiện. 

Đối với một quyền chọn mua, thời gian đến khi đáo hạn dài hơn sẽ làm tăng giá trị của quyền chọn trong _tất cả_ các trường hợp. Tiềm năng tăng giá của một tài sản cơ sở về cơ bản là không giới hạn và tăng lên qua các khoảng thời gian dài hơn, trong khi rủi ro giảm giá phía dưới được giới hạn ở mức tổn thất khoản phí quyền chọn. 

Một quyền chọn bán đại diện cho quyền được bán tài sản cơ sở cũng thường được hưởng lợi từ sự trôi qua của thời gian (khi thời gian đáo hạn dài hơn). Trong trường hợp của quyền chọn bán, thời gian đến khi đáo hạn dài hơn mang lại tiềm năng _giảm giá_ (*price depreciation*) lớn hơn xuống dưới mức giá thực hiện, trong khi khoản lỗ được giới hạn ở mức phí quyền chọn nếu giá tài sản cơ sở tăng lên. Tuy nhiên, vì người mua quyền chọn bán phải chờ đợi việc _bán_ tài sản cơ sở để nhận được $(X - S_T)$ khi thực hiện quyền, thời gian đến khi đáo hạn dài hơn sẽ _làm giảm_ giá trị hiện tại của khoản thanh toán nhận được. Mặc dù ít phổ biến hơn, trong một số trường hợp, thời gian đến khi đáo hạn dài hơn sẽ _làm giảm_ giá trị của một quyền chọn bán, đặc biệt là đối với các quyền chọn bán có lời sâu (*deep-in-the-money puts*) có thời gian đến khi đáo hạn dài hơn và mức lãi suất phi rủi ro cao hơn. 

##### **Lãi suất Phi Rủi ro (*Risk-Free Interest Rate*)** 

Một bài học trước đã chỉ ra rằng lãi suất phi rủi ro là chi phí cơ hội của việc nắm giữ một tài sản, điều này cũng được mở rộng sang việc định giá không kinh doanh chênh lệch giá đối với các công cụ phái sinh. Ví dụ, giá trị thực hiện của một quyền chọn đã được chứng minh là bằng phần chênh lệch giữa giá giao ngay và _giá trị hiện tại_ (*present value*) của giá thực hiện: 

$$\text{Giá trị thực hiện của quyền chọn mua (Call Option Exercise Value): } \text{Max}(0, (S_t - \text{PV}(X)))$$

$$\text{Giá trị thực hiện của quyền chọn bán (Put Option Exercise Value): } \text{Max}(0, (\text{PV}(X) - S_t))$$

Do đó, một mức lãi suất phi rủi ro _cao hơn_ sẽ _làm giảm_ giá trị hiện tại của giá thực hiện _với điều kiện_ quyền chọn đang ở trạng thái có lời (*in the money*). Một mức lãi suất phi rủi ro cao hơn sẽ _làm tăng_ giá trị thực hiện của một quyền chọn mua và _làm giảm_ giá trị thực hiện của một quyền chọn bán. Lưu ý rằng lãi suất phi rủi ro không ảnh hưởng trực tiếp đến giá trị thời gian của một quyền chọn. 

##### **Độ biến động của Tài sản Cơ sở (*Volatility of the Underlying*)** 

Độ biến động (*volatility*) là một thước đo về mức độ phân tán dự kiến (*expected dispersion*) của các biến động giá trong tương lai của một tài sản cơ sở. Độ biến động giá của tài sản cơ sở càng cao sẽ làm tăng khả năng đạt được một giá trị thực hiện dương cao hơn mà không làm ảnh hưởng đến trường hợp bất lợi phía dưới khi quyền chọn hết hạn mà không được thực hiện, như được minh họa trong Bảng 8 (*Exhibit 8*). Lưu ý rằng tác động này sẽ giống nhau đối với cả quyền chọn mua và quyền chọn bán. 

Ví dụ, khi độ biến động _tăng lên_, phạm vi rộng hơn của các mức giá tài sản cơ sở có thể xảy ra sẽ _làm tăng_ giá trị thời gian của quyền chọn cũng như khả năng quyền chọn sẽ kết thúc ở trạng thái có lời (*in the money*). Độ biến động _thấp hơn_ sẽ _làm giảm_ giá trị thời gian của cả quyền chọn bán và quyền chọn mua. 


<!-- PDF Page 197 -->

###### **Bảng 8: Độ biến động và Giá trị Quyền chọn (*Exhibit 8: Volatility and Option Value*)** 

![](assets/Derivatives.pdf-0197-04.png)

<!-- Picture Text: ST<br>ST<br>X<br>S 0<br>0 Time T<br> -->
> **Chú thích hình ảnh:**
> - Khi độ biến động (*volatility*) tăng lên, biên độ phân tán của giá tài sản cơ sở $S_T$ quanh giá thực hiện $X$ tại thời điểm đáo hạn $T$ mở rộng ra, làm tăng tiềm năng sinh lời khi quyền chọn ở trạng thái ITM trong khi mức lỗ tối đa khi OTM vẫn được giới hạn.

##### **Thu nhập hoặc Chi phí Liên quan đến Việc Sở hữu Tài sản Cơ sở (*Income or Cost Related to Owning Underlying Asset*)** 

Trong một bài học trước, những lợi ích và chi phí của việc sở hữu một tài sản cơ sở theo thời gian đã được chứng minh là có ảnh hưởng đến mối quan hệ giữa giá giao ngay và giá kỳ hạn. Ví dụ, thu nhập hoặc các lợi ích phi tiền mặt khác (chẳng hạn như lợi suất thuận tiện – *convenience yield*) thuộc về người sở hữu tài sản cơ sở nhưng không thuộc về người sở hữu công cụ phái sinh. Tác động này đúng với cả các cam kết kỳ hạn và các quyền đòi nợ có điều kiện. Thu nhập hoặc các lợi ích khác của quyền sở hữu sẽ _làm giảm_ giá trị của một quyền chọn mua và _làm tăng_ giá trị của một quyền chọn bán. Chi phí lưu giữ (*carry costs*, chẳng hạn như chi phí lưu kho và bảo hiểm đối với hàng hóa) có tác động ngược lại, _làm tăng_ giá trị của một quyền chọn mua và _làm giảm_ giá trị của một quyền chọn bán. Bảng tóm tắt các nhân tố ảnh hưởng đến giá trị của một quyền chọn được cung cấp trong Bảng 9 (*Exhibit 9*), với dấu trên giá trị quyền chọn đề cập đến tác động (cùng chiều dương hay ngược chiều âm) của sự _gia tăng_ trong nhân tố đó. 

**Bảng 9: Các Nhân tố Ảnh hưởng đến Giá trị của một Quyền chọn (*Exhibit 9: Factors That Affect the Value of an Option*)** 

|**Nhân tố (*Factor*) (khi tăng lên)**|**Giá trị Quyền chọn Mua (*Call Value*)**|**Giá trị Quyền chọn Bán (*Put Value*)**|
|---|---|---|
|Giá trị của tài sản cơ sở (*Value of the underlying*)|**+**|**−**|
|Giá thực hiện (*Exercise price*)|**−**|**+**|
|Thời gian đến khi đáo hạn (*Time to expiration*)|**+**|**+/−**|
|Lãi suất phi rủi ro (*Risk-free interest rate*)|**+**|**−**|
|Độ biến động của tài sản cơ sở (*Volatility of the underlying*)|**+**|**+**|
|Thu nhập/chi phí liên quan đến việc sở hữu tài sản cơ sở (*Income/cost related to owning the underlying*)|**−/+**|**+/−**|


<!-- PDF Page 198 -->

###### **BỘ CÂU HỎI (*QUESTION SET*)** 

##### **Các Nhân tố Ảnh hưởng đến Giá trị Quyền chọn (*Factors That Affect Option Value*)** 

1. Xác định các câu trả lời đúng để hoàn thành câu sau đây: Đối với một quyền chọn mua đại diện cho quyền được mua tài sản cơ sở, giá thực hiện đại diện cho một cận ______ đối với giá trị thực hiện của quyền chọn khi đáo hạn, dẫn đến giá trị quyền chọn ______ ứng với một mức giá thực hiện thấp hơn. 

###### **Lời giải:** 

Đối với một quyền chọn mua đại diện cho quyền được mua tài sản cơ sở, giá thực hiện đại diện cho một cận _dưới (lower)_ đối với giá trị thực hiện của quyền chọn khi đáo hạn, dẫn đến giá trị quyền chọn _cao hơn (higher)_ ứng với một mức giá thực hiện thấp hơn. 

2. Hãy ghép những thay đổi sau đây trong các nhân tố ảnh hưởng đến giá trị quyền chọn (giữ các nhân tố khác không đổi) với sự thay đổi giá trị quyền chọn tương ứng của chúng: 

| Thay đổi trong nhân tố | Thay đổi giá trị quyền chọn |
|---|---|
| 1. Giá thực hiện ($X$) thấp hơn | A. Làm tăng giá trị của cả quyền chọn mua và quyền chọn bán |
| 2. Giá tài sản cơ sở ($S_T$) thấp hơn | B. Làm tăng giá trị của quyền chọn mua |
| 3. Sự gia tăng trong độ biến động của giá tài sản cơ sở | C. Làm tăng giá trị của quyền chọn bán |

###### **Lời giải:** 

   **1.** B là đáp án đúng. Giá thực hiện thấp hơn làm tăng giá trị của quyền chọn mua, bởi vì ứng với một mức giá tài sản cơ sở nhất định khi đáo hạn là $S_T$, giá trị thanh toán của quyền chọn mua là $\text{Max}(0, S_T - X)$ sẽ tăng lên khi $X$ thấp hơn. 

   **2.** C là đáp án đúng. Giá tài sản cơ sở ($S_T$) thấp hơn sẽ làm tăng giá trị của quyền chọn bán. Vì quyền chọn bán là quyền được bán một tài sản cơ sở tại mức giá thực hiện ($X$), giá trị thanh toán của quyền chọn bán là $\text{Max}(0, X - S_T)$ sẽ tăng lên khi $S_T$ giảm xuống. 

   **3.** A là đáp án đúng. Sự gia tăng trong độ biến động của giá tài sản cơ sở sẽ làm tăng giá trị của cả quyền chọn mua và quyền chọn bán. Biến thiên giá lớn hơn của tài sản cơ sở sẽ làm tăng xác suất đạt được một giá trị thực hiện dương cao hơn đối với quyền chọn mua hoặc quyền chọn bán mà không làm ảnh hưởng đến trường hợp bất lợi phía dưới nơi quyền chọn hết hạn mà không được thực hiện. 

3. Xác định các câu trả lời đúng để hoàn thành các câu sau đây: Một điểm khác biệt quan trọng giữa các cam kết kỳ hạn và các quyền đòi nợ có điều kiện là __________ của mức thay đổi giá công cụ phái sinh ứng với một mức thay đổi nhất định trong giá trị tài sản cơ sở. Đối với một cam kết kỳ hạn, giá trị công cụ phái sinh là một hàm ______ theo giá tài sản cơ sở, trong khi đối với một quyền chọn thì đó là một mối quan hệ _______. 

###### **Lời giải:** 

Một điểm khác biệt quan trọng giữa các cam kết kỳ hạn và các quyền đòi nợ có điều kiện là _độ lớn (magnitude)_ của mức thay đổi giá công cụ phái sinh ứng với một mức thay đổi nhất định trong giá trị tài sản cơ sở. Đối với một cam kết kỳ hạn, giá trị công cụ phái sinh là một hàm _tuyến tính (linear)_ theo giá tài sản cơ sở, trong khi đối với một quyền chọn thì đó là một mối quan hệ _phi tuyến tính (non-linear)_. 


<!-- PDF Page 199 -->

4. Giải thích tác động của sự _sụt giảm_ trong lãi suất phi rủi ro lên giá trị của quyền chọn bán và quyền chọn mua, đồng thời giải thích lý do cho câu trả lời của bạn. 

###### **Lời giải:** 

- Sự _sụt giảm_ trong lãi suất phi rủi ro _làm tăng_ giá trị hiện tại của _giá_ thực hiện quyền chọn ($\text{PV}(X)$). Giá trị thực hiện của một _quyền chọn mua đang có lời (in-the-money call)_ sẽ giảm xuống, bởi vì $(S_t - \text{PV}(X))$ thấp hơn khi $\text{PV}(X)$ cao hơn, trong khi giá trị thực hiện của một _quyền chọn bán đang có lời (in-the-money put)_ sẽ tăng lên, bởi vì $(\text{PV}(X) - S_t)$ tăng lên khi $\text{PV}(X)$ cao hơn. Lưu ý rằng giá trị thời gian của một quyền chọn không bị ảnh hưởng trực tiếp bởi lãi suất phi rủi ro. 


<!-- PDF Page 200 -->

## **BÀI TẬP THỰC HÀNH (*PRACTICE PROBLEMS*)** 

### **Thông tin sau đây liên quan đến các câu hỏi từ 1 đến 9** 

Văn phòng Quản lý Gia sản Viswan (Viswan Family Office – VFO) sở hữu cổ phiếu không trả cổ tức của Biomian Limited hiện đang có giá ($S_0$) là 295 INR mỗi cổ phiếu. Giám đốc Đầu tư (CIO) của VFO đang cân nhắc một lời đề nghị bán cổ phiếu tại mức giá kỳ hạn ($F_0(T)$) là 300,84 INR mỗi cổ phiếu sau thời gian 6 tháng dựa trên mức lãi suất phi rủi ro là 4%. Bạn được yêu cầu tư vấn về việc mua một quyền chọn bán (*purchase of a put option*) hoặc bán một quyền chọn mua (*sale of a call option*) có giá thực hiện ($X$) bằng với giá kỳ hạn ($F_0(T)$) như những phương án thay thế cho việc bán cổ phiếu kỳ hạn. 

**1.** Phát biểu nào sau đây mô tả đúng về phí quyền chọn bán và phí quyền chọn mua dựa trên mối quan hệ giữa mức giá hiện tại 295 INR của Biomian và mức giá thực hiện bằng với giá kỳ hạn 300,84 INR? 

   - **A.** Phí quyền chọn mua chỉ bao gồm giá trị thời gian, và phí quyền chọn bán chỉ bao gồm giá trị thực hiện. 

   - **B.** Phí quyền chọn mua chỉ bao gồm giá trị thực hiện, và phí quyền chọn bán chỉ bao gồm giá trị thời gian. 

   - **C.** Phí quyền chọn mua chỉ bao gồm giá trị thời gian, và phí quyền chọn bán cũng chỉ bao gồm giá trị thời gian. 

**2.** Phát biểu nào sau đây mô tả đúng một điểm khác biệt quan trọng giữa hai chiến lược mua quyền chọn bán và bán quyền chọn mua xét về mặt sự hao mòn giá trị thời gian (*time value decay*) của quyền chọn? 

   - **A.** Sự hao mòn giá trị thời gian là một lợi ích đối với cả hai chiến lược quyền chọn. 

   - **B.** Sự hao mòn giá trị thời gian là một chi phí đối với cả hai chiến lược quyền chọn. 

   - **C.** Sự hao mòn giá trị thời gian là một lợi ích đối với việc bán quyền chọn mua và là một chi phí đối với việc mua quyền chọn bán. 

**3.** VFO đang cân nhắc việc mua quyền chọn bán để phòng ngừa rủi ro (*hedge*) trước sự sụt giảm giá cổ phiếu của Biomian. Phát biểu nào sau đây mô tả đúng nhất sự đánh đổi (*trade-off*) giữa quyền chọn bán và hợp đồng kỳ hạn dựa trên nguyên tắc định giá không kinh doanh chênh lệch giá? 

   - **A.** Khoản lãi từ việc bán kỳ hạn sẽ _bằng_ với lợi nhuận của quyền chọn bán đã mua khi đáo hạn _với điều kiện_ quyền chọn bán kết thúc ở trạng thái có lời (*in the money*) khi đáo hạn. 

   - **B.** Khoản lỗ từ việc bán kỳ hạn sẽ _vượt quá_ khoản lỗ của quyền chọn bán đã mua khi đáo hạn nếu giá cổ phiếu của Biomian vượt quá giá kỳ hạn một mức lớn hơn khoản phí quyền chọn bán ban đầu đã trả. 

   - **C.** Chúng ta không có đủ thông tin để trả lời câu hỏi này, bởi vì chúng ta không biết giá trị thời gian của quyền chọn khi đáo hạn. 

**4.** Khi đánh giá chiến lược mua quyền chọn bán (với $X = F_0(T)$), CIO đã yêu cầu bạn cân nhắc việc bán lại quyền chọn bán đó sau thời gian 3 tháng nếu giá của nó tăng lên trong khoảng thời gian đó. Phương án nào sau đây mô tả đúng nhất mức giá quyền chọn bán không kinh doanh chênh lệch giá tại 


<!-- PDF Page 201 -->

###### thời điểm đó? 

   - **A.** Vì VFO sẽ chỉ thực hiện quyền nếu giá giao ngay thấp hơn giá thực hiện, cận dưới của giá quyền chọn bán là giá trị lớn hơn giữa số không và giá trị hiện tại của giá giao ngay trừ đi giá thực hiện. 

   - **B.** Vì VFO sẽ chỉ thực hiện quyền nếu giá giao ngay thấp hơn giá thực hiện, cận trên của giá quyền chọn bán bằng giá trị hiện tại của giá thực hiện trừ đi giá giao ngay. 

   - **C.** Giá quyền chọn bán không thể lớn hơn giá kỳ hạn và không thể nhỏ hơn giá trị lớn hơn giữa số không và giá trị hiện tại của giá thực hiện trừ đi giá giao ngay. 

**5.** VFO đang cân nhắc chiến lược bán quyền chọn mua (*sold call strategy*) để tạo ra thu nhập từ việc bán quyền chọn mua. Trong phân tích kịch bản của bạn về phương án bán quyền chọn mua, VFO đã yêu cầu bạn định giá quyền chọn mua sau thời gian 3 tháng nếu giá giao ngay của Biomian là 325 INR mỗi cổ phiếu. Với mức giá quyền chọn mua ước tính là 46,41 INR vào thời điểm đó, phương án nào sau đây phản ánh đúng mối quan hệ giữa giá trị thực hiện và giá trị thời gian của quyền chọn mua? 

   - **A.** Giá trị thực hiện của quyền chọn mua là 24,16 INR, và giá trị thời gian của nó là 22,25 INR. 

   - **B.** Giá trị thực hiện của quyền chọn mua là 27,10 INR, và giá trị thời gian của nó là 19,31 INR. 

   - **C.** Giá trị thực hiện của quyền chọn mua là 20,99 INR, và giá trị thời gian của nó là 25,42 INR. 

**6.** Phát biểu nào sau đây mô tả đúng cách thức VFO có thể mô phỏng (*replicate*) việc bán một quyền chọn mua đối với cổ phiếu Biomian nếu việc thực hiện quyền là chắc chắn? 

   - **A.** Vay $X(1 + r)^{-T}$ ở mức lãi suất phi rủi ro và sử dụng số tiền thu được để mua cổ phiếu Biomian tại mức giá giao ngay hiện tại, $S_0$. Khi đáo hạn, bán cổ phiếu Biomian và sử dụng số tiền thu được để trả hết khoản vay. 

   - **B.** Bán khống (*sell short*) cổ phiếu Biomian tại mức giá giao ngay hiện tại, $S_0$, và sử dụng số tiền thu được để cho vay $X(1 + r)^{-T}$ ở mức lãi suất phi rủi ro. Khi đáo hạn, nhận $X$ từ việc hoàn trả khoản cho vay phi rủi ro và mua lại cổ phiếu Biomian. 

   - **C.** Bán khống cổ phiếu Biomian tại mức giá giao ngay hiện tại, $S_0$, và vay $X(1 + r)^{-T}$ ở mức lãi suất phi rủi ro. Khi đáo hạn, trả hết khoản vay phi rủi ro trị giá $X$ và mua lại cổ phiếu Biomian. 

**7.** Khi so sánh chiến lược bán quyền chọn mua và mua quyền chọn bán tại mức giá kỳ hạn, CIO của VFO lo ngại về việc sự gia tăng độ biến động (*volatility*) của cổ phiếu cơ sở Biomian sẽ ảnh hưởng như thế nào đến phí quyền chọn. Phát biểu nào sau đây về sự thay đổi độ biến động và tác động của nó lên chiến lược là chính xác nhất? 

   - **A.** Sự gia tăng độ biến động của cổ phiếu cơ sở có tác động _giống nhau_ lên giá trị quyền chọn mua và quyền chọn bán, vì vậy sự thay đổi này sẽ không ảnh hưởng đến quyết định lựa chọn chiến lược của VFO. 

   - **B.** Vì những thay đổi trong độ biến động của cổ phiếu cơ sở có tác động _ngược chiều_ lên quyền chọn bán so với quyền chọn mua, sự thay đổi này sẽ làm tăng sức hấp dẫn của chiến lược quyền chọn bán so với chiến lược quyền chọn mua. 


<!-- PDF Page 202 -->

   - **C.** Sự gia tăng độ biến động của cổ phiếu cơ sở sẽ làm tăng cả _chi phí_ của chiến lược mua quyền chọn bán lẫn khoản phí quyền chọn nhận được từ chiến lược bán quyền chọn mua, vì vậy sự thay đổi này sẽ làm tăng sức hấp dẫn của chiến lược quyền chọn mua so với chiến lược quyền chọn bán. 

**8.** Khi so sánh chiến lược mua quyền chọn bán và bán quyền chọn mua đối với Biomian, phát biểu nào sau đây là đúng nhất về cách thức giá trị quyền chọn mua và quyền chọn bán bị ảnh hưởng bởi những thay đổi trong các nhân tố ngoài độ biến động? 

   - **A.** Những thay đổi trong thời gian đến khi đáo hạn và lãi suất phi rủi ro có tác động cùng chiều tương tự nhau lên chiến lược quyền chọn bán và quyền chọn mua, trong khi những thay đổi trong giá thực hiện có xu hướng có tác động ngược chiều. 

   - **B.** Những thay đổi trong thời gian đến khi đáo hạn có xu hướng có tác động cùng chiều tương tự nhau lên chiến lược quyền chọn bán và quyền chọn mua, trong khi những thay đổi trong giá thực hiện và lãi suất phi rủi ro có xu hướng có tác động ngược chiều. 

   - **C.** Những thay đổi trong lãi suất phi rủi ro có tác động cùng chiều tương tự nhau lên chiến lược quyền chọn bán và quyền chọn mua, trong khi những thay đổi trong giá thực hiện và thời gian đến khi đáo hạn có xu hướng có tác động ngược chiều. 

**9.** VFO đang lo ngại về khả năng lãi suất tăng lên trong tương lai. Phát biểu nào sau đây mô tả đúng nhất về cách thức lãi suất tăng lên sau khi đã tham gia vào hai chiến lược quyền chọn sẽ ảnh hưởng đến việc định giá quyền chọn? 

   - **A.** Lãi suất phi rủi ro tăng lên sẽ làm cho chiến lược bán quyền chọn mua có lợi hơn cho VFO bởi vì quyền chọn mua tăng giá trị khi lãi suất phi rủi ro cao hơn. 

   - **B.** Lãi suất phi rủi ro tăng lên sẽ làm cho chiến lược mua quyền chọn bán có lợi hơn cho VFO bởi vì công ty đã khóa chặt (*locks in*) mức phí quyền chọn bán ở mức lãi suất thấp hơn. 

   - **C.** Lãi suất phi rủi ro tăng lên là một yếu tố bất lợi (*negative*) đối với cả hai chiến lược quyền chọn. 


<!-- PDF Page 203 -->

## **LỜI GIẢI (*SOLUTIONS*)** 

1. C là đáp án đúng. Giá trị thực hiện của cả quyền chọn mua và quyền chọn bán đều bằng không bởi vì giá trị hiện tại của giá thực hiện là 295 INR ($\text{PV}(X) = 300,84 \times (1,04)^{-0,5} = 295\text{ INR}$), tương đương với mức giá cổ phiếu hiện tại là 295 INR. Do đó, cả hai khoản phí quyền chọn đều chỉ phản ánh giá trị thời gian. A không đúng vì phát biểu này không tính đến việc chiết khấu giá thực hiện một cách hợp lý. B không đúng vì phí quyền chọn mua không phản ánh giá trị thực hiện. 

2. C là đáp án đúng. Thành phần giá trị thời gian trong phí quyền chọn giảm dần về không khi thời gian trôi dần về ngày đáo hạn. Một quyền chọn đã mua sẽ giảm giá trị, khi các yếu tố khác không đổi, do sự sụt giảm của giá trị thời gian. Một vị thế bán quyền chọn sẽ có lợi (giảm nghĩa vụ nợ), khi các yếu tố khác không đổi, nhờ sự sụt giảm của giá trị thời gian. A không đúng vì sự hao mòn giá trị thời gian là một chi phí đối với chiến lược mua quyền chọn bán, và B không đúng vì sự hao mòn giá trị thời gian là một lợi ích đối với chiến lược bán quyền chọn. 

3. Đáp án đúng là B. Khoản lỗ từ việc bán kỳ hạn sẽ lớn hơn khoản lỗ của quyền chọn bán đã mua khi đáo hạn nếu giá cổ phiếu của Biomian vượt quá giá kỳ hạn một mức lớn hơn khoản phí quyền chọn bán ban đầu. Mức lỗ phía dưới (*downside return*) của VFO được giới hạn ở khoản phí quyền chọn bán đã trả, trong khi giao dịch bán kỳ hạn có mức lỗ không giới hạn khi cổ phiếu Biomian tăng giá. A không đúng vì nó không tính đến khoản phí quyền chọn bán đã trả, trong khi C không đúng vì giá trị thời gian của một quyền chọn bằng không khi đáo hạn. 

4. Đáp án đúng là C. Giá thực hiện của quyền chọn bán, $X$ (bằng với $F_0(T)$ trong trường hợp này), đại diện cho cận _trên_ đối với giá trị quyền chọn bán, trong khi cận _dưới_ là giá trị lớn hơn giữa giá trị hiện tại của giá thực hiện trừ đi giá giao ngay và số không: 

   $$\text{Max}\left(0, X(1 + r)^{-(T - t)} - S_t\right) < p_t \le X$$

A không đúng vì cận _dưới_ của giá quyền chọn bán là giá trị lớn hơn giữa số không và giá trị hiện tại của giá thực hiện trừ đi giá giao ngay, chứ không phải giá trị hiện tại của giá giao ngay trừ đi giá thực hiện. B không đúng vì cận _dưới_, chứ không phải cận trên, của giá quyền chọn bán bằng giá trị hiện tại của giá thực hiện trừ đi giá giao ngay. 

5. Đáp án đúng là B. Giá quyền chọn bằng tổng của giá trị thực hiện và giá trị thời gian. Giá trị thực hiện của một quyền chọn mua bằng giá trị lớn hơn giữa số không và giá giao ngay trừ đi giá trị hiện tại của giá thực hiện: 

   $$\text{Max}\left(0, S_t - X(1 + r)^{-(T - t)}\right)$$

   $$= \text{Max}\left(0, 325\text{ INR} - 300,84\text{ INR}(1,04)^{-0,25}\right) = 27,10\text{ INR}$$

Giá trị thời gian bằng giá quyền chọn mua trừ đi giá trị thực hiện, hay $19,31\text{ INR} \ (= 46,41\text{ INR} - 27,10\text{ INR})$. A không đúng vì lấy giá giao ngay trừ đi giá thực hiện làm giá trị thực hiện, trong khi C tính giá trị thực hiện bằng giá trị hiện tại của giá giao ngay trừ đi giá thực hiện. 

6. B là đáp án đúng. Để mô phỏng việc bán một quyền chọn mua, hãy kết hợp việc bán khống tài sản cơ sở với việc cho vay phi rủi ro. Đây là chiến lược hoàn toàn ngược lại với việc mô phỏng mua một quyền chọn mua, trong đó tài sản cơ sở được mua bằng số tiền thu được từ việc đi vay phi rủi ro. A không đúng vì phát biểu này mô tả việc mô phỏng mua một quyền chọn mua. C không đúng vì việc bán khống và đi vay ban đầu tạo ra hai dòng tiền 


<!-- PDF Page 204 -->

vào (*cash inflows*) tại thời điểm $t = 0$ tiếp nối bởi hai dòng tiền ra (*cash outflows*) tại thời điểm $t = T$. 

7. Đáp án đúng là C. Sự gia tăng độ biến động của giá cổ phiếu cơ sở sẽ làm tăng cả khoản phí quyền chọn trả trước nhận được từ quyền chọn mua đã bán lẫn khoản phí quyền chọn phải trả cho quyền chọn bán đã mua. Do đó, vì chiến lược mua quyền chọn bán liên quan đến khoản thanh toán trả trước cao hơn do VFO phải chi trả và chiến lược bán quyền chọn mua liên quan đến khoản phí quyền chọn nhận được cao hơn, sự gia tăng độ biến động sẽ làm tăng sức hấp dẫn của chiến lược bán quyền chọn mua so với chiến lược mua quyền chọn bán. 

8. Đáp án đúng là B. Những thay đổi trong thời gian đến khi đáo hạn có xu hướng có tác động cùng chiều tương tự nhau lên chiến lược quyền chọn bán và quyền chọn mua (ngoại lệ duy nhất là các quyền chọn bán có lời sâu trong một số trường hợp), trong khi những thay đổi trong giá thực hiện và lãi suất phi rủi ro có xu hướng có tác động ngược chiều. 

9. C là đáp án đúng. Bởi vì cả hai chiến lược quyền chọn (mua một quyền chọn bán hoặc bán một quyền chọn mua) đều là các chiến lược bán khống cơ sở (*short strategies*), VFO đang trì hoãn các dòng tiền thu vào nên lãi suất phi rủi ro cao hơn là yếu tố bất lợi (khi lãi suất phi rủi ro tăng, giá quyền chọn bán giảm làm bất lợi cho người mua quyền chọn bán, đồng thời giá quyền chọn mua tăng làm bất lợi cho người bán quyền chọn mua). A không đúng vì phát biểu này mô tả tác động giá trị từ việc mua một quyền chọn mua chứ không phải từ việc bán quyền chọn mua. B không đúng vì giá trị của quyền chọn bán sẽ sụt giảm sau khi lãi suất phi rủi ro tăng lên. 
