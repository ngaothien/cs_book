# Tập 7: Công cụ Phái sinh (*Derivatives*)
## Học phần 2: Đặc điểm và Công cụ của Cam kết Kỳ hạn và Quyền đòi hỏi Có điều kiện (*Forward Commitment and Contingent Claim Features and Instruments*)
### Phần 2/2: Quyền chọn (*Options*) (Trang PDF 46–60)

---

<!-- PDF Page 46 -->

3. Đáp án đúng là A. Bên trả lãi suất cố định (còn được gọi là bên nhận lãi suất thả nổi) nhận được một khoản thanh toán ròng nếu lãi suất tham chiếu thị trường vượt quá lãi suất cố định trong một kỳ nhất định.

# **<mark>5</mark>** 

#### **QUYỀN CHỌN (*OPTIONS*)** 

định nghĩa hợp đồng kỳ hạn, hợp đồng tương lai, hợp đồng hoán đổi, quyền chọn (quyền chọn mua và quyền chọn bán), và công cụ phái sinh tín dụng cũng như so sánh các đặc điểm cơ bản của chúng

xác định giá trị khi đáo hạn và lợi nhuận từ một vị thế mua hoặc vị thế bán đối với quyền chọn mua hoặc quyền chọn bán

đối chiếu giữa các cam kết kỳ hạn với các quyền đòi hỏi có điều kiện

Quyền đòi hỏi có điều kiện (*contingent claims*) là một loại hợp đồng phái sinh ETD hoặc OTC trong đó một trong các đối tác có quyền quyết định liệu một giao dịch có được thanh toán hay không dựa trên giá trị của tài sản cơ sở. Hợp đồng quyền chọn (*option contracts*) là quyền đòi hỏi có điều kiện phổ biến nhất. Tương tự như hợp đồng kỳ hạn và hợp đồng tương lai, quyền chọn là các hợp đồng phái sinh giữa người mua và người bán quy định rõ một tài sản cơ sở, quy mô hợp đồng, một mức giá thực hiện thỏa thuận trước, và một ngày đáo hạn. Người mua quyền chọn có quyền nhưng không có nghĩa vụ (*right but not the obligation*) thực hiện giao dịch, và người bán quyền chọn có nghĩa vụ phải thực hiện giao dịch theo sự lựa chọn của người mua quyền chọn. Hệ quả là, giá trị nhận được khi đáo hạn (*payoff*) của người mua quyền chọn luôn bằng không hoặc là một số dương. Giá trị này không bao giờ có thể âm.

Giả sử người mua quyền chọn trả một khoản phí quyền chọn ($c_0$) là $\$5$ tại thời điểm $t = 0$ để có quyền — nhưng không phải nghĩa vụ — mua cổ phiếu $S$ tại thời điểm $T$ ở một mức giá đã thỏa thuận trước ($X$) là $\$30$. Quyết định của người mua quyền chọn khi đáo hạn phụ thuộc vào giá cổ phiếu khi đáo hạn ($S_T$), như được thể hiện trong hai kịch bản sau đây:

##### **Kịch bản 1: Thực hiện giao dịch ($S_T > X$)** 

- Nếu $S_T = \$40$, người mua quyền chọn lựa chọn thực hiện quyền chọn (*exercise the option*) và mua cổ phiếu với giá $X = \$30$.

- Người mua quyền chọn thu được $\$10$ $[(S_T - X) = \$40 - \$30]$ trên giao dịch này.

- Người mua quyền chọn thực hiện được khoản lợi nhuận là $\$5$ $[(S_T - X) - c_0 = (\$40 - \$30) - \$5]$.

##### **Kịch bản 2: Không thực hiện giao dịch ($S_T < X$)** 

- Nếu $S_T = \$25$, người mua quyền chọn lựa chọn không thực hiện quyền chọn để mua cổ phiếu với giá $X = \$30$.

- Người mua quyền chọn chịu một khoản lỗ là $\$5$ ($c_0 = \$5$).

Bảng minh họa 6 cho thấy cơ chế hoạt động của quyền chọn đối với trường hợp người mua quyền chọn trả tiền để có quyền mua một cổ phiếu cơ sở $S$ tại mức giá thực hiện thỏa thuận trước là $X$ trong tương lai ($t = T$).

<!-- PDF Page 47 -->

**Bảng minh họa 6: Cơ chế Hoạt động của Quyền chọn Mua (*Exhibit 6: Call Option Mechanics*)** 

![](assets/Derivatives.pdf-0047-04.png)

<!-- Picture Text: Time<br>t  = 0 t  =  T<br>Underlying  ST  ≤  X<br>Buyer does not purchase underlying<br>Option buyer<br>Right to purchase Option buyer Option seller<br>underlying at  X<br>Upfront<br>premium Underlying  ST  >  X<br>Buyer purchases underlying<br>X<br>Option seller<br>Obligated to sell Option buyer Option seller<br>underlying at  X<br>Underlying ( ST )<br> -->

> **Chú thích hình ảnh:**
> - **Tại thời điểm $t = 0$:** **Người mua quyền chọn (*Option buyer*)** (có quyền mua tài sản cơ sở tại giá $X$) trả **Phí quyền chọn trả trước (*Upfront premium*)** cho **Người bán quyền chọn (*Option seller*)** (có nghĩa vụ bán tài sản cơ sở tại giá $X$).
> - **Tại thời điểm $t = T$:**
>   - Nếu giá tài sản cơ sở $S_T \le X$: Người mua không mua tài sản cơ sở (không có giao dịch giữa Người mua và Người bán).
>   - Nếu giá tài sản cơ sở $S_T > X$: Người mua mua tài sản cơ sở — trả tiền $X$ cho Người bán và nhận về Tài sản cơ sở ($S_T$).

Quyết định giao dịch tài sản cơ sở được gọi là **thực hiện quyền (*exercise*)**, và mức giá thực hiện đã thỏa thuận trước được gọi là **giá thực hiện (*exercise price* hoặc *strike price*)**. Người mua quyền chọn có thể giao dịch tài sản cơ sở trong tương lai hoàn toàn theo quyết định riêng của họ tại mức giá thực hiện — một mức giá giao ngay tương lai thỏa thuận trước có thể cao hơn, bằng, hoặc thấp hơn giá kỳ hạn, như đã trình bày trong một bài học trước. Quyền được thực hiện giao dịch trong tương lai này có một giá trị được trả trước cho người bán quyền chọn dưới hình thức một khoản **phí quyền chọn (*option premium*)**.

Các điều khoản của hợp đồng quyền chọn, chẳng hạn như quyền mua hoặc quyền bán, giá thực hiện, kỳ hạn, và quy mô, có thể được thỏa thuận giữa các đối tác trong một giao dịch phi tập trung (OTC) hoặc được thực hiện trên một sở giao dịch dựa trên các điều khoản được tiêu chuẩn hóa. Bài học này tập trung vào **quyền chọn kiểu châu Âu (*European options*)**, hay các quyền chọn chỉ có thể được thực hiện vào ngày đáo hạn, mặc dù vẫn tồn tại các kiểu quyền chọn khác. Ví dụ, **quyền chọn kiểu Mỹ (*American options*)** có thể được thực hiện vào bất kỳ thời điểm nào kể từ khi khởi tạo hợp đồng cho đến khi đáo hạn. Lưu ý rằng tên gọi “châu Âu” và “Mỹ” không đề cập đến nơi các quyền chọn này được sử dụng, mà đề cập đến sự khác biệt về thời điểm chúng có thể được thực hiện.

Tồn tại hai loại quyền chọn chính — cụ thể là, (1) quyền mua một tài sản cơ sở được gọi là **quyền chọn mua (*call option*)** và (2) quyền bán tài sản cơ sở, hay **quyền chọn bán (*put option*)**. Người mua quyền chọn sẽ chỉ thực hiện quyền chọn mua hoặc quyền chọn bán nếu nó mang lại một giá trị nhận được (*payoff*) dương. Nếu không được thực hiện, quyền chọn sẽ hết hạn mà không có giá trị (*expires worthless*), và khoản lỗ của người mua quyền chọn bằng đúng khoản phí quyền chọn đã trả.

Một yếu tố cấu thành giá trị của quyền chọn trước khi đáo hạn ($t < T$) là giá trị thực hiện của quyền chọn tại thời điểm $t$, được gọi là **giá trị nội tại (*intrinsic value*)** của quyền chọn.

Chúng ta có thể nói một quyền chọn mua đang ở trạng thái **cao giá / có lời (*in-the-money*)** tại thời điểm $t$ nếu giá giao ngay, $S_t$, vượt quá $X$, với giá trị nội tại bằng $(S_t - X)$. Cả quyền chọn ở trạng thái **kiệt giá / lỗ (*out-of-the-money*)** (khi $S_t < X$) và quyền chọn ở trạng thái **ngang giá (*at-the-money*)** ($S_t = X$) đều có giá trị nội tại bằng không, do đó giá của chúng, $c_t$, chỉ bao gồm toàn bộ giá trị thời gian (*time value*).

Người mua quyền chọn mua sẽ hưởng lợi từ sự gia tăng trong giá của tài sản cơ sở. Bảng minh họa 7 cho thấy giá trị nhận được (*payoff*) và lợi nhuận (*profit*) khi đáo hạn đối với người mua quyền chọn mua.

<!-- PDF Page 48 -->

**Bảng minh họa 7: Cấu trúc Giá trị nhận được của Vị thế Mua Quyền chọn Mua (*Exhibit 7: Long Call Payoff Profile*)** 

![](assets/Derivatives.pdf-0048-04.png)

<!-- Picture Text: Payoff/<br>Profit<br>+<br>Payoff<br>0 ST<br>Profit<br>– c0<br>X X  +  c0<br> -->

> **Chú thích hình ảnh:**
> - **Trục tung:** Giá trị nhận được / Lợi nhuận (*Payoff / Profit*).
> - **Trục hoành:** Giá giao ngay khi đáo hạn $S_T$.
> - Đường **Giá trị nhận được (*Payoff*)** nằm ngang ở mức $0$ khi $S_T \le X$ và dốc lên tuyến tính khi $S_T > X$.
> - Đường **Lợi nhuận (*Profit*)** nằm ngang ở mức $-c_0$ khi $S_T \le X$, bắt đầu đi lên từ $X$, cắt trục hoành (hòa vốn) tại $X + c_0$.

Người mua quyền chọn trả một khoản phí quyền chọn mua, $c_0$, tại thời điểm $t = 0$ cho người bán quyền chọn và có quyền mua tài sản cơ sở, $S_T$, tại mức giá thực hiện $X$ vào thời điểm $t = T$. _Giá trị nhận được khi thực hiện quyền (exercise payoff)_ $(S_T - X)$ là số dương nếu $S_T > X$ và bằng không nếu $S_T \le X$. Giá trị của quyền chọn mua khi đáo hạn, $c_T$, có thể được biểu diễn như sau:

![](assets/Derivatives.pdf-0048-06.png)

<!-- Formula Text: cT = max(0, ST – X). (1) -->
$$c_T = \max(0, S_T - X) \tag{1}$$

_Lợi nhuận (profit)_ của người mua quyền chọn mua bằng _giá trị nhận được khi đáo hạn (payoff)_ trừ đi phí quyền chọn mua, $c_0$ (bỏ qua giá trị thời gian của tiền tệ trong bài học này):

![](assets/Derivatives.pdf-0048-08.png)

<!-- Formula Text: Π = max(0, ST – X) – c0. (2) -->
$$\Pi = \max(0, S_T - X) - c_0 \tag{2}$$

Cấu trúc giá trị nhận được bất đối xứng (*asymmetric payoff profile*) này là một đặc điểm chung của các quyền đòi hỏi có điều kiện, đôi khi được gọi là các **công cụ phái sinh phi tuyến tính (*non-linear derivatives*)**.

###### **VÍ DỤ 5 (*EXAMPLE 5*)** 

##### **Hightest Capital — Giao dịch Mua Quyền chọn Mua (*Call Option Purchase*)** 

Hightest Capital mua một quyền chọn mua trên Chỉ số Ngành Chăm sóc Sức khỏe Chọn lọc S&P 500 (*S&P 500 Health Care Select Sector Index* – SIXV). Hợp đồng quyền chọn giao dịch trên sở giao dịch có kỳ hạn sáu tháng này có quy mô là 100 đơn vị chỉ số và mức giá thực hiện là $\$1.240$ mỗi đơn vị so với mức giá giao ngay ban đầu của SIXV là $\$1.180,95$. Khoản phí quyền chọn trả trước là $\$24,85$ mỗi đơn vị, hay $\$2.485$ ($= \$24,85 \times 100$). Khi quyền chọn gần đến ngày đáo hạn, một chuyên viên phân tích của Hightest được yêu cầu xác định giá trị nhận được và lợi nhuận kỳ vọng của quyền chọn trên mỗi đơn vị khi đáo hạn theo các kịch bản khác nhau của giá giao ngay SIXV vào ngày thực hiện quyền. Cô lập bảng sau đây:

- $c_0 =$ Phí quyền chọn mua $= \$24,85$ mỗi đơn vị.

- $X =$ Giá thực hiện tại thời điểm $T = \$1.240$ mỗi đơn vị.

- $S_T =$ Giá giao ngay trên mỗi đơn vị tại thời điểm $T$.

|**Giá giao ngay SIXV ($S_T$)**|**Giá thực hiện ($X$)**|**Giá trị nhận được (*Payoff*) $\max(0, S_T - X)$**|**Lợi nhuận (*Profit*) $\max(0, S_T - X) - c_0$**|
|---|---|---|---|
|$\$1.280$|$\$1.240$|$\$40$|$\$15,15$|
|$\$1.260$|$\$1.240$|$\$20$|$-\$4,85$|

<!-- PDF Page 49 -->

|**Giá giao ngay SIXV ($S_T$)**|**Giá thực hiện ($X$)**|**Giá trị nhận được (*Payoff*) $\max(0, S_T - X)$**|**Lợi nhuận (*Profit*) $\max(0, S_T - X) - c_0$**|
|---|---|---|---|
|$\$1.240$|$\$1.240$|$\$0$|$-\$24,85$|
|$\$1.220$|$\$1.240$|$\$0$|$-\$24,85$|

Ví dụ 5 đặt ra một câu hỏi khác liên quan đến giá trị của một quyền chọn trước khi đáo hạn ($t < T$). Thời gian cho đến khi quyền chọn đáo hạn càng dài, khả năng xảy ra một biến động có lợi trong giá tài sản cơ sở làm tăng cả xác suất lẫn khả năng sinh lời của việc thực hiện quyền càng cao. **Giá trị thời gian (*time value*)** này của một quyền chọn luôn dương và giảm dần về không khi quyền chọn tiến đến ngày đáo hạn.

Trái ngược với người mua quyền chọn mua có tiềm năng sinh lời không giới hạn khi giá tăng và mức lỗ được giới hạn ở khoản phí quyền chọn đã trả, người bán quyền chọn mua nhận được mức lợi nhuận tối đa bằng khoản phí quyền chọn và phải đối mặt với rủi ro thua lỗ không giới hạn khi tài sản cơ sở tăng giá vượt lên trên mức giá thực hiện. Cấu trúc giá trị nhận được của vị thế bán quyền chọn mua (*short call*) trong Bảng minh họa 8 là hình ảnh phản chiếu qua gương của Bảng minh họa 7.

###### **Bảng minh họa 8: Cấu trúc Giá trị nhận được của Vị thế Bán Quyền chọn Mua (*Exhibit 8: Short Call Payoff Profile*)** 

![](assets/Derivatives.pdf-0049-07.png)

<!-- Picture Text: Payoff/<br>Profit<br>Profit<br>c0<br>Payoff<br>0 ST<br>–<br>X X  +  c0<br> -->

> **Chú thích hình ảnh:**
> - **Trục tung:** Giá trị nhận được / Lợi nhuận (*Payoff / Profit*).
> - **Trục hoành:** Giá giao ngay khi đáo hạn $S_T$.
> - Đường **Giá trị nhận được (*Payoff*)** nằm ngang ở mức $0$ khi $S_T \le X$ và dốc xuống âm khi $S_T > X$.
> - Đường **Lợi nhuận (*Profit*)** nằm ngang ở mức $+c_0$ khi $S_T \le X$, đi xuống cắt trục hoành tại $X + c_0$, và lỗ không giới hạn khi $S_T$ tiếp tục tăng.

Cấu trúc giá trị nhận được của người mua và người bán quyền chọn minh họa cho bản chất một chiều (*one-sided nature*) của rủi ro tín dụng đối tác đối với các quyền đòi hỏi có điều kiện. Nghĩa là, người bán quyền chọn không có mức độ tiếp xúc rủi ro tín dụng nào đối với người mua quyền chọn một khi phí quyền chọn đã được thanh toán. Tuy nhiên, người mua quyền chọn phải đối mặt với rủi ro tín dụng đối tác từ phía người bán quyền chọn bằng đúng giá trị nhận được của quyền chọn khi đáo hạn.

Người mua quyền chọn bán (*put option buyers*) hưởng lợi từ mức giá tài sản cơ sở thấp hơn bằng cách bán tài sản cơ sở tại mức giá thực hiện đã thỏa thuận trước. Người mua quyền chọn bán sẽ thực hiện quyền khi giá tài sản cơ sở thấp hơn giá thực hiện ($S_T < X$), như được thể hiện trong Bảng minh họa 9.

<!-- PDF Page 50 -->

**Bảng minh họa 9: Cấu trúc Giá trị nhận được của Vị thế Mua Quyền chọn Bán (*Exhibit 9: Long Put Payoff Profile*)** 

![](assets/Derivatives.pdf-0050-03.png)

<!-- Picture Text: Payoff/<br>Profit<br>Payoff<br>+<br>Profit<br>0 ST<br>– p0<br>X  –  p0 X<br> -->

> **Chú thích hình ảnh:**
> - **Trục tung:** Giá trị nhận được / Lợi nhuận (*Payoff / Profit*).
> - **Trục hoành:** Giá giao ngay khi đáo hạn $S_T$.
> - Đường **Giá trị nhận được (*Payoff*)** dốc xuống từ trái sang phải khi $S_T < X$ và nằm ngang ở mức $0$ khi $S_T \ge X$.
> - Đường **Lợi nhuận (*Profit*)** cắt trục hoành (hòa vốn) tại $X - p_0$ và nằm ngang ở mức lỗ tối đa $-p_0$ khi $S_T \ge X$.

Người mua quyền chọn bán trả một khoản phí quyền chọn là $p_0$ khi khởi tạo cho người bán quyền chọn và sẽ chỉ thực hiện quyền chọn nếu $(X - S_T) > 0$. Giống như trong Phương trình 1 và 2, chúng ta có thể biểu diễn _giá trị nhận được (payoff)_ và _lợi nhuận (profit)_, $\Pi$, của vị thế mua quyền chọn bán như sau:

![](assets/Derivatives.pdf-0050-05.png)

<!-- Formula Text: pT = max(0, X – ST). (3) -->
$$p_T = \max(0, X - S_T) \tag{3}$$

![](assets/Derivatives.pdf-0050-06.png)

<!-- Formula Text: Π = max(0, X – ST) – p0. (4) -->
$$\Pi = \max(0, X - S_T) - p_0 \tag{4}$$

Giá trị nhận được hoặc lợi nhuận từ góc độ của người bán quyền chọn bán là ngược dấu với khoản lãi hoặc lỗ của người mua quyền chọn bán tại một mức giá tài sản cơ sở nhất định khi đáo hạn. Giống như trường hợp của người bán quyền chọn mua, người bán quyền chọn bán có mức lãi tối đa bằng khoản phí quyền chọn. Tuy nhiên, mặc dù người bán quyền chọn mua phải đối mặt với khoản lỗ tiềm tàng không giới hạn khi tài sản cơ sở tăng giá vượt quá giá thực hiện, khoản lỗ của người bán quyền chọn bán thường có giới hạn bởi vì giá tài sản cơ sở không thể giảm xuống dưới mức không ($0$). _Giá trị nhận được (payoff)_ và _lợi nhuận (profit)_ của vị thế bán quyền chọn bán (*short put*) như sau:

$$-p_T = -\max(0, X - S_T) \tag{5}$$

![](assets/Derivatives.pdf-0050-09.png)

<!-- Formula Text: Π = –max(0, X – ST) + p0. (6) -->
$$\Pi = -\max(0, X - S_T) + p_0 \tag{6}$$

###### **BỘ CÂU HỎI (*QUESTION SET*)** 

##### **Quyền chọn (*Options*)** 

1. Hãy tính mức giá giao ngay SIXV khi đáo hạn từ Ví dụ 5 mà tại đó Hightest Capital sẽ đạt điểm hòa vốn (*breakeven point*) và có lợi nhuận bằng không.

###### **Lời giải:** 

Bên mua quyền chọn mua có mức lợi nhuận bằng $\max(0, S_T - X) - c_0$. Trong trường hợp của Hightest ở Ví dụ 5, giá thực hiện SIXV là $\$1.240$ và phí quyền chọn mua ban đầu là $\$24,85$. Do đó, điểm hòa vốn hay điểm có lợi nhuận bằng không sẽ bằng $\$1.240 + \$24,85$, hay $\$1.264,85$.

<!-- PDF Page 51 -->

2. Một người bán quyền chọn bán nhận được khoản phí quyền chọn $\$5$ cho một quyền chọn bán được bán trên một tài sản cơ sở có giá thực hiện là $\$30$. Lợi nhuận tối đa của người bán quyền chọn theo hợp đồng này là bao nhiêu? Mức lỗ tối đa theo hợp đồng là bao nhiêu?

###### **Lời giải:** 

Một người bán quyền chọn bán nhận được khoản phí quyền chọn $\$5$ ($p_0$) cho một quyền chọn bán được bán trên một tài sản cơ sở có giá thực hiện ($X$) là $\$30$. Lợi nhuận của người bán quyền chọn bán là $\Pi = -\max(0, X - S_T) + p_0$. Nếu quyền chọn không được thực hiện, $-\max(0, X - S_T) = 0$ và người bán quyền chọn bán thu được $p_0 = \$5$. Nếu quyền chọn được thực hiện và $S_T = 0$, khi đó $\Pi = -\max(0, 30 - 0) + 5 = -\$25$. Do đó, lợi nhuận tối đa của người bán quyền chọn theo hợp đồng là _$\$5$_ và mức lỗ tối đa theo hợp đồng là _$\$25$_.

3. Xác định những bên tham gia hợp đồng quyền chọn tương ứng với các phát biểu sau đây:

|**Bên tham gia**|**Đặc điểm mô tả**|
|---|---|
|A. Bên bán quyền chọn bán (*Put option seller*)|1. Không có rủi ro tín dụng đối tác đối với người mua quyền chọn một khi phí quyền chọn trả trước đã được thanh toán|
|B. Bên bán quyền chọn mua (*Call option seller*)|2. Thu được khoản lợi nhuận bằng với phí quyền chọn nếu giá tài sản cơ sở khi đáo hạn thấp hơn giá thực hiện|
|C. Cả bên bán quyền chọn bán và bên bán quyền chọn mua|3. Thu được khoản lợi nhuận bằng với phí quyền chọn nếu giá tài sản cơ sở khi đáo hạn vượt quá giá thực hiện|

###### **Lời giải:** 

1. Đáp án đúng là C. Người bán quyền chọn không có rủi ro tín dụng đối tác đối với người mua quyền chọn một khi phí quyền chọn trả trước đã được thanh toán.

2. Đáp án đúng là B. Người bán quyền chọn mua thu được khoản lợi nhuận bằng với phí quyền chọn nếu giá tài sản cơ sở khi đáo hạn thấp hơn giá thực hiện.

3. Đáp án đúng là A. Người bán quyền chọn bán thu được khoản lợi nhuận bằng với phí quyền chọn nếu giá tài sản cơ sở khi đáo hạn lớn hơn giá thực hiện.

#### **CÔNG CỤ PHÁI SINH TÍN DỤNG (*CREDIT DERIVATIVES*)** 

![](assets/Derivatives.pdf-0051-13.png)

<!-- Picture Text: 6<br> -->

định nghĩa hợp đồng kỳ hạn, hợp đồng tương lai, hợp đồng hoán đổi, quyền chọn (quyền chọn mua và quyền chọn bán), và công cụ phái sinh tín dụng cũng như so sánh các đặc điểm cơ bản của chúng

Các hợp đồng phái sinh tín dụng (*credit derivative contracts*) dựa trên một biến số cơ sở tín dụng, hay rủi ro vỡ nợ (*default risk*) của một tổ chức phát hành nợ đơn lẻ hoặc một nhóm các tổ chức phát hành nợ trong một chỉ số. Hợp đồng phái sinh tín dụng phổ biến nhất là hợp đồng hoán đổi rủi ro tín dụng (*credit default swap* – CDS). Các hợp đồng CDS cho phép nhà đầu tư quản lý rủi ro tổn thất từ việc tổ chức phát hành vỡ nợ một cách tách biệt khỏi trái phiếu giao ngay (*cash bond*). Hợp đồng CDS được giao dịch dựa trên một mức chênh lệch tín dụng (**chênh lệch tín dụng CDS – *CDS credit spread***) tương tự như chênh lệch tín dụng của một trái phiếu giao ngay. Mức chênh lệch tín dụng phụ thuộc vào xác suất vỡ nợ (*probability of default* – POD) và mức tổn thất khi vỡ nợ (*loss given default* – LGD), như đã trình bày trong một bài học trước. Một mức chênh lệch tín dụng _cao hơn_ (hay khả năng kiệt quệ tài chính của tổ chức phát hành cao hơn) tương ứng với một mức giá trái phiếu giao ngay _thấp hơn_, và ngược lại.

<!-- PDF Page 52 -->

Mặc dù có tên gọi là hoán đổi (*swap*), các hợp đồng CDS thực chất là các quyền đòi hỏi có điều kiện (*contingent claims*) nhưng mang một số đặc điểm của các cam kết chắc chắn (*firm commitments*). Không giống như các quyền chọn mua và quyền chọn bán đã thảo luận trước đó, cả thời điểm thực hiện quyền lẫn khoản thanh toán khi thực hiện quyền theo một hợp đồng CDS đều thay đổi tùy thuộc vào (các) tổ chức phát hành cơ sở. Giống như trường hợp của một hợp đồng hoán đổi lãi suất tiêu chuẩn, một hợp đồng CDS được định giá tại mức chênh lệch ngang giá (*par spread*) có giá trị hiện tại ròng bằng không, và giá trị danh nghĩa (*notional amount*) không được trao đổi mà thay vào đó đóng vai trò làm cơ sở để tính toán mức phí chênh lệch (*spread*) và số tiền thanh toán.

Trong một hợp đồng CDS, bên mua bảo vệ tín dụng (*credit protection buyer*) trả phí cho bên bán bảo vệ tín dụng (*credit protection seller*) để bên bán gánh chịu rủi ro tổn thất từ việc vỡ nợ của một tổ chức phát hành thứ ba cơ sở. Nếu một **sự kiện tín dụng (*credit event*)** của tổ chức phát hành xảy ra — thường được định nghĩa là phá sản (*bankruptcy*), không thanh toán được một nghĩa vụ nợ (*failure to pay an obligation*), hoặc tái cơ cấu nợ bắt buộc (*involuntary debt restructuring*) — bên bán bảo vệ tín dụng sẽ chi trả cho bên mua bảo vệ tín dụng để thanh toán hợp đồng. Khoản thanh toán có điều kiện (*contingent payment*) này bằng đúng mức tổn thất khi vỡ nợ (LGD) của tổ chức phát hành tính trên giá trị danh nghĩa của hợp đồng CDS. Bảng minh họa 10 cho thấy các dòng tiền định kỳ theo một hợp đồng CDS.

**Bảng minh họa 10: Các Khoản Thanh toán Định kỳ theo Hợp đồng Hoán đổi Rủi ro Tín dụng (*Exhibit 10: Periodic Payments under a Credit Default Swap*)** 

![](assets/Derivatives.pdf-0052-06.png)

<!-- Picture Text: Fixed CDS Spread<br>Protection Buyer Protection Seller<br>(Short Risk)  (Long Risk)<br>Contingent Payment<br>Upon Credit Event<br> -->

> **Chú thích hình ảnh:**
> - **Bên mua bảo vệ / Vị thế bán rủi ro (*Protection Buyer / Short Risk*)** trả **Mức phí chênh lệch CDS cố định (*Fixed CDS Spread*)** định kỳ cho **Bên bán bảo vệ / Vị thế mua rủi ro (*Protection Seller / Long Risk*)**.
> - Ngược lại, **Bên bán bảo vệ** thực hiện **Khoản thanh toán có điều kiện khi xảy ra Sự kiện Tín dụng (*Contingent Payment Upon Credit Event*)** cho **Bên mua bảo vệ**.

Tài sản cơ sở có thể là một tổ chức phát hành doanh nghiệp hoặc chính phủ, một chỉ số gồm các tổ chức phát hành, hoặc một thực thể có mục đích đặc biệt (*special purpose entity* – SPE) nắm giữ một danh mục các khoản vay, khoản thế chấp, hoặc trái phiếu.

Người mua có thể sử dụng hợp đồng CDS làm công cụ phòng vệ (*hedge*) cho mức độ tiếp xúc rủi ro tín dụng hiện có đối với tổ chức phát hành cơ sở. Sự bảo vệ tín dụng mà một hợp đồng CDS mang lại tương tự như một hợp đồng bảo hiểm đối với một người mua đang có sẵn vị thế tiếp xúc thu nhập cố định đối với tổ chức phát hành thứ ba đó. Người mua có thể chịu một khoản lỗ về giá trị trên vị thế thu nhập cố định của mình do sự kiện tín dụng gây ra nhưng sẽ nhận được một khoản thanh toán từ hợp đồng CDS giúp bù đắp khoản lỗ đó.

Một người mua bảo vệ tín dụng không nắm giữ vị thế thu nhập cố định tương ứng nhưng vẫn mua một hợp đồng CDS là đang tìm cách thu lợi từ mức chênh lệch tín dụng cao hơn (vốn tương ứng với giá trái phiếu giao ngay thấp hơn) của một tổ chức phát hành cơ sở, và do đó đang ở vị thế bán khống rủi ro tín dụng (*short credit risk*).

Bên bán bảo vệ tín dụng nhận được một khoản thanh toán phí chênh lệch cố định định kỳ để đổi lấy việc gánh chịu rủi ro có điều kiện là phải chi trả cho bên mua bảo vệ tín dụng nhằm bù đắp tổn thất khi xảy ra một sự kiện tín dụng. Cấu trúc hợp đồng này tương tự như bảo hiểm, với khoản phí bảo hiểm định kỳ trong suốt vòng đời của hợp đồng được thỏa thuận trước và thời điểm cũng như quy mô của khoản tổn thất khi xảy ra sự kiện tín dụng là chưa biết trước. Do đó, vị thế của người bán bảo vệ tương tự như một vị thế mua rủi ro (*long risk position*) đối với trái phiếu cơ sở của tổ chức phát hành.

Ví dụ, Bảng minh họa 11 cho thấy hợp đồng CDS đối với một tổ chức phát hành cơ sở trải qua sự dịch chuyển chất lượng tín dụng (*credit migration*) tại $t = 1$, tiếp nối bởi một sự kiện tín dụng (*credit event*) tại $t = 2$.

<!-- PDF Page 53 -->

**Bảng minh họa 11: Hợp đồng CDS với Sự dịch chuyển Tín dụng và Sự kiện Tín dụng (*Exhibit 11: CDS Contract with Credit Migration and Credit Event*)** 

![](assets/Derivatives.pdf-0053-04.png)

<!-- Picture Text: Credit Credit<br>Migration Event<br>Time<br>t  = 0 t  = 1 t  = 2<br>Protection Protection Protection<br>Buyer Buyer Buyer<br>CDS Spread0 CDS Spread0 Payment<br>100 bps p.a. 100 bps p.a. ≈ LGD (%) × Notional<br>Protection Protection Protection<br>Seller Seller Seller<br>Credit migration Credit event<br>CDS Spread1 = 250 bps Issuer default/Failure to pay<br>MTM Gain to buyer CDS Contract terminates<br>MTM Loss to seller<br>CDS MTM Change ≈ Payment from seller to buyer<br>Δ CDS Spread × Notional × ≈ LGD (%) × Notional<br>EffDurCDS<br> -->

> **Chú thích hình ảnh:**
> - **Tại $t = 0$:** Bên mua bảo vệ (*Protection Buyer*) trả phí $\text{CDS Spread}_0 = 100\text{ bps/năm}$ cho Bên bán bảo vệ (*Protection Seller*).
> - **Tại $t = 1$ (Sự dịch chuyển tín dụng – *Credit Migration*):** Chênh lệch tín dụng tăng lên $\text{CDS Spread}_1 = 250\text{ bps}$. Bên mua bảo vệ vẫn chỉ trả $100\text{ bps/năm}$ nên có Lãi định giá theo thị trường (*MTM Gain to buyer*), còn Bên bán bảo vệ chịu Lỗ định giá theo thị trường (*MTM Loss to seller*). Mức thay đổi MTM của CDS: $\text{CDS MTM Change} \approx \Delta\text{CDS Spread} \times \text{Notional} \times \text{EffDur}_{\text{CDS}}$.
> - **Tại $t = 2$ (Sự kiện tín dụng – *Credit Event*):** Tổ chức phát hành vỡ nợ / Không có khả năng thanh toán (*Issuer default/Failure to pay*). Hợp đồng CDS chấm dứt (*CDS Contract terminates*). Khoản thanh toán từ bên bán cho bên mua $\approx \text{LGD (\%)} \times \text{Notional}$.

Bên mua bảo vệ đồng ý trả một mức phí chênh lệch cố định là 100 bps/năm tại thời điểm $t = 0$ cho suốt thời hạn hợp đồng. Khi mức chênh lệch CDS của tổ chức phát hành nới rộng ra thành 250 bps/năm tại thời điểm $t = 1$, người mua có lãi trên hợp đồng CDS nhờ mức phí chênh lệch cố định thấp đang trả, trong khi người bán bị lỗ do mức phí chênh lệch cố định nhận được thấp hơn so với mức chênh lệch CDS thị trường hiện hành đang cao hơn. Giống như bất kỳ công cụ thu nhập cố định nào, thời lượng hiệu dụng (*effective duration* – $\text{EffDur}_{\text{CDS}}$) của thời hạn hợp đồng còn lại có thể được sử dụng để ước tính xấp xỉ mức thay đổi giá trị MTM. Một sự kiện tín dụng của tổ chức phát hành tại thời điểm $t = 2$ khiến hợp đồng chấm dứt, và người bán phải thực hiện một khoản thanh toán cho người mua bằng tỷ lệ phần trăm tổn thất khi vỡ nợ ($\text{LGD}$) nhân với giá trị danh nghĩa của hợp đồng CDS.

###### **BỘ CÂU HỎI (*QUESTION SET*)** 

##### **Công cụ Phái sinh Tín dụng (*Credit Derivatives*)** 

1. Xác định câu trả lời đúng để điền vào chỗ trống: Khoản thanh toán có điều kiện theo một hợp đồng hoán đổi rủi ro tín dụng bằng với ____________ tính trên giá trị danh nghĩa CDS được quy định trong hợp đồng.

###### **Lời giải:** 

Khoản thanh toán có điều kiện theo một hợp đồng hoán đổi rủi ro tín dụng bằng với _mức tổn thất khi vỡ nợ (loss given default – LGD)_ tính trên giá trị danh nghĩa CDS được quy định trong hợp đồng.

2. Mô tả tại sao vị thế của người bán bảo vệ tín dụng lại tương tự như vị thế của một khoản đầu tư trái phiếu giao ngay cơ sở.

###### **Lời giải:** 

Người bán bảo vệ tín dụng nhận được một khoản thanh toán phí chênh lệch CDS định kỳ để đổi lấy rủi ro có điều kiện phải thanh toán cho người mua khi xảy ra một sự kiện tín dụng của tổ chức phát hành. Nhà đầu tư trái phiếu giao ngay nhận được một khoản lãi coupon định kỳ có kết hợp

<!-- PDF Page 54 -->

mức chênh lệch tín dụng của tổ chức phát hành để đổi lấy một khoản tổn thất tiềm tàng nếu tổ chức phát hành vỡ nợ. Theo cả hợp đồng CDS và trái phiếu giao ngay, khoản thanh toán hoặc tổn thất tiềm tàng này đều bằng mức tổn thất khi vỡ nợ (LGD). Do đó, vị thế của người bán bảo vệ tín dụng tương tự như một vị thế mua rủi ro (*long risk position*) đối với trái phiếu cơ sở của tổ chức phát hành.

3. Xác định những bên tham gia hợp đồng CDS tương ứng với các phát biểu sau đây:

|**Bên tham gia**|**Đặc điểm mô tả**|
|---|---|
|A. Bên mua bảo vệ tín dụng (*Credit protection buyer*)|1. Tìm cách thu lợi từ mức chênh lệch tín dụng cao hơn của tổ chức phát hành|
|B. Bên bán bảo vệ tín dụng (*Credit protection seller*)|2. Tham gia vào một hợp đồng phái sinh giúp chuyển giao rủi ro tổn thất từ một sự kiện tín dụng của một tổ chức phát hành thứ ba cơ sở|
|C. Cả bên mua bảo vệ tín dụng và bên bán bảo vệ tín dụng|3. Đạt được một khoản lãi MTM trên hợp đồng CDS nếu mức chênh lệch CDS của tổ chức phát hành cơ sở giảm xuống|

###### **Lời giải:** 

1. Đáp án đúng là A. Bên mua bảo vệ tín dụng tìm cách thu lợi từ mức chênh lệch tín dụng cao hơn của tổ chức phát hành.

2. Đáp án đúng là C. Cả bên mua bảo vệ tín dụng và bên bán bảo vệ tín dụng đều tham gia vào một hợp đồng phái sinh giúp chuyển giao rủi ro tổn thất từ một sự kiện tín dụng của một tổ chức phát hành thứ ba cơ sở.

3. Đáp án đúng là B. Bên bán bảo vệ tín dụng đạt được một khoản lãi MTM trên hợp đồng CDS nếu mức chênh lệch CDS của tổ chức phát hành cơ sở giảm xuống. Sự sụt giảm trong mức chênh lệch CDS của tổ chức phát hành so với mức phí chênh lệch cố định ban đầu trên hợp đồng CDS có nghĩa là bên bán bảo vệ đang nhận được một mức phí chênh lệch cao hơn thị trường (*above-market spread*). Mức phí chênh lệch CDS cao hơn thị trường này bù đắp nhiều hơn mức cần thiết cho người bán trước mức rủi ro tín dụng mới thấp hơn và dẫn đến một khoản lãi MTM.

# **<mark>7</mark>** 

#### **CAM KẾT KỲ HẠN SO VỚI QUYỀN ĐÒI HỎI CÓ ĐIỀU KIỆN (*FORWARD COMMITMENTS VS. CONTINGENT CLAIMS*)** 

đối chiếu giữa các cam kết kỳ hạn với các quyền đòi hỏi có điều kiện

Một cam kết chắc chắn (*firm commitment*) yêu cầu cả hai đối tác phải thực hiện nghĩa vụ theo hợp đồng phái sinh, trong khi người mua quyền chọn có thể quyết định có thực hiện hợp đồng khi đáo hạn hay không tùy thuộc vào giá tài sản cơ sở so với giá thực hiện. Những người tham gia thị trường thường tạo ra các mức độ tiếp xúc rủi ro tương tự nhau đối với một tài sản cơ sở bằng cách sử dụng các loại công cụ phái sinh khác nhau này. Ví dụ, cả vị thế mua hợp đồng kỳ hạn (*long forward position*) và vị thế mua quyền chọn mua (*long call option position*) đều sẽ hưởng lợi từ sự gia tăng trong giá của tài sản cơ sở. Bảng minh họa 12 đối chiếu giá trị nhận được (*payoff*) và lợi nhuận (*profit*) của hai hợp đồng phái sinh này, trong đó giá thực hiện, $X$, bằng với giá kỳ hạn, $F_0(T)$.

<!-- PDF Page 55 -->

###### **Bảng minh họa 12: Cấu trúc Giá trị nhận được của Vị thế Mua Kỳ hạn và Vị thế Mua Quyền chọn Mua (*Exhibit 12: Long Forward and Long Call Option Payoff Profiles*)** 

![](assets/Derivatives.pdf-0055-03.png)

<!-- Picture Text: Payoff/<br>Forward<br>profit<br>profit<br>+<br>Option<br>payoff<br>0 ST<br>Option<br>– profit X  =  F0 ( T )<br> -->

> **Chú thích hình ảnh:**
> - Khi $X = F_0(T)$:
>   - Đường **Lợi nhuận kỳ hạn (*Forward profit*)** là đường thẳng tuyến tính đi qua điểm $X = F_0(T)$ trên trục hoành.
>   - Đường **Giá trị nhận được của quyền chọn (*Option payoff*)** bằng $0$ khi $S_T \le X$ và trùng với đường lợi nhuận kỳ hạn khi $S_T > X$.
>   - Đường **Lợi nhuận của quyền chọn (*Option profit*)** nằm ngang ở mức $-c_0$ khi $S_T \le X$ và song song (thấp hơn một đoạn $c_0$) so với đường lợi nhuận kỳ hạn khi $S_T > X$.

Như đã trình bày trước đó, cả giá trị nhận được của vị thế mua kỳ hạn lẫn quyền chọn mua đều tăng lên khi $S_T$ tăng. Trong trường hợp của hợp đồng kỳ hạn, mối quan hệ tuyến tính này bằng $[S_T - F_0(T)]$, với giá trị nhận được bằng đúng lợi nhuận vì không có khoản tiền mặt nào được trao đổi khi khởi tạo. Đối với người mua một quyền chọn mua có giá thực hiện là $F_0(T)$, Phương trình 2 chuyển thành:

$$\Pi = \max[0, S_T - F_0(T)] - c_0$$

Cho giá trị nhận được/lợi nhuận của hợp đồng kỳ hạn $[S_T - F_0(T)]$ bằng với lợi nhuận của quyền chọn mua, $\Pi$, chúng ta có được cấu trúc lợi nhuận tương đối giữa hợp đồng kỳ hạn và quyền chọn như sau:

- $S_T - F_0(T) > -c_0 \implies$ Lợi nhuận hợp đồng kỳ hạn vượt quá lợi nhuận quyền chọn (*Forward profit exceeds option profit*)

- $S_T - F_0(T) = -c_0 \implies$ Lợi nhuận hợp đồng kỳ hạn bằng lợi nhuận quyền chọn mua (*Forward profit equals call option profit*)

- $S_T - F_0(T) < -c_0 \implies$ Lợi nhuận quyền chọn vượt quá lợi nhuận hợp đồng kỳ hạn (*Option profit exceeds forward profit*)

Sự so sánh song song trong Bảng minh họa 12 giữa đồ thị lợi nhuận của hợp đồng kỳ hạn và quyền chọn mua cho thấy sự tương đồng của vị thế mua quyền chọn mua với một vị thế mua (*long position*) tài sản cơ sở nhưng có sự bảo vệ khi giá giảm (*downside protection*) để đổi lấy việc phải trả một khoản phí quyền chọn.

Một quyền đòi hỏi có điều kiện khác cũng hưởng lợi từ sự gia tăng trong giá của tài sản cơ sở là quyền chọn bán đã bán (*sold put option* / *short put*). Trong khi giá trị nhận được của vị thế mua quyền chọn mua và vị thế mua kỳ hạn đều tăng lên khi giá tài sản cơ sở vượt lên trên giá thực hiện, lợi nhuận của người bán quyền chọn bán lại bị giới hạn ở khoản phí quyền chọn trả trước. Bảng minh họa 13 đối chiếu giá trị nhận được và lợi nhuận của vị thế bán quyền chọn bán với vị thế mua kỳ hạn nếu giá thực hiện, $X$, bằng $F_0(T)$.

<!-- PDF Page 56 -->

###### **Bảng minh họa 13: Cấu trúc Giá trị nhận được của Vị thế Mua Kỳ hạn và Vị thế Bán Quyền chọn Bán (*Exhibit 13: Long Forward and Short Put Option Payoff Profile*)** 

![](assets/Derivatives.pdf-0056-04.png)

<!-- Picture Text: Payoff/<br>Profit<br>Forward<br>profit<br>+<br>Option<br>profit<br>0 ST<br>Option<br>payoff<br>– X  =  F0 ( T )<br> -->

> **Chú thích hình ảnh:**
> - Khi $X = F_0(T)$:
>   - Đường **Lợi nhuận kỳ hạn (*Forward profit*)** tăng tuyến tính theo $S_T$ và cắt trục hoành tại $X = F_0(T)$.
>   - Đường **Giá trị nhận được của quyền chọn (*Option payoff*)** trùng với đường lợi nhuận kỳ hạn ở miền âm khi $S_T \le X$ và nằm ngang ở mức $0$ khi $S_T > X$.
>   - Đường **Lợi nhuận của quyền chọn (*Option profit*)** song song và cao hơn đường lợi nhuận kỳ hạn một đoạn $+p_0$ khi $S_T \le X$, và nằm ngang ở mức lợi nhuận tối đa $+p_0$ khi $S_T > X$.

Chúng ta có thể so sánh giá trị nhận được/lợi nhuận của vị thế mua kỳ hạn là $[S_T - F_0(T)]$ với một phiên bản điều chỉnh của Phương trình 6:

$$\Pi = -\max[0, F_0(T) - S_T] + p_0$$

Cho lợi nhuận của hợp đồng kỳ hạn $[S_T - F_0(T)]$ bằng với lợi nhuận của quyền chọn bán, $\Pi$, chúng ta có được cấu trúc lợi nhuận tương đối giữa hợp đồng kỳ hạn và quyền chọn như sau:

- $S_T - F_0(T) > p_0 \implies$ Lợi nhuận hợp đồng kỳ hạn vượt quá lợi nhuận quyền chọn (*Forward profit exceeds option profit*)

- $S_T - F_0(T) = p_0 \implies$ Lợi nhuận hợp đồng kỳ hạn bằng lợi nhuận quyền chọn (*Forward profit equals option profit*)

- $S_T - F_0(T) < p_0 \implies$ Lợi nhuận quyền chọn vượt quá lợi nhuận hợp đồng kỳ hạn (*Option profit exceeds forward profit*)

Sự so sánh song song trong Bảng minh họa 13 giữa đồ thị lợi nhuận của hợp đồng kỳ hạn và quyền chọn bán đã bán cho thấy sự tương đồng của vị thế bán quyền chọn bán với một vị thế mua tài sản cơ sở, trong đó phần lợi nhuận từ sự tăng giá bị từ bỏ để đổi lấy việc nhận được một khoản phí quyền chọn. Tính đối xứng rõ nét giữa các vị thế mua quyền chọn mua (*long call*) và bán quyền chọn bán (*short put*) với vị thế mua kỳ hạn (*long forward*) sẽ được xem xét chi tiết hơn trong một bài học sau.

###### **BỘ CÂU HỎI (*QUESTION SET*)** 

##### **Cam kết Chắc chắn và Quyền đòi hỏi Có điều kiện (*Firm Commitments and Contingent Claims*)** 

1. Xác định các câu trả lời đúng để điền vào chỗ trống: Một vị thế _____ hợp đồng kỳ hạn, một vị thế _____ quyền chọn mua, và một vị thế _____ quyền chọn bán sẽ hưởng lợi từ sự sụt giảm trong giá của tài sản cơ sở.

###### **Lời giải:** 

Một vị thế _bán (short)_ hợp đồng kỳ hạn, một vị thế _bán (short)_ quyền chọn mua, và một vị thế _mua (long)_ quyền chọn bán sẽ hưởng lợi từ sự sụt giảm trong giá của tài sản cơ sở.

<!-- PDF Page 57 -->

2. Xác định các vị thế phái sinh tương ứng với các cấu trúc lợi nhuận khi đáo hạn sau đây với giả định rằng giá thực hiện ($X$) bằng $F_0(T)$:

![](assets/Derivatives.pdf-0057-04.png)

<!-- Picture Text: A. Short forward position 1.<br>Profit<br>Profit<br>+<br>0 ST<br>–<br>F0 ( T )<br>B. Long put position 2.<br>Profit<br>Profit<br>+<br>0 ST<br>– F0 ( T )<br>C. Short call position 3.<br>Profit<br>+ Profit<br>0 ST<br>– F0 ( T )<br> -->

> **Chú thích hình ảnh:**
> - **A. Vị thế bán kỳ hạn (*Short forward position*)** | **Đồ thị 1:** Lợi nhuận dương khi $S_T$ thấp, giảm tuyến tính qua trục hoành trước $F_0(T)$, và nằm ngang ở mức lỗ cố định $-p_0$ khi $S_T \ge F_0(T)$.
> - **B. Vị thế mua quyền chọn bán (*Long put position*)** | **Đồ thị 2:** Đường thẳng tuyến tính dốc xuống từ miền dương qua điểm $F_0(T)$ trên trục hoành xuống miền âm.
> - **C. Vị thế bán quyền chọn mua (*Short call position*)** | **Đồ thị 3:** Lợi nhuận nằm ngang ở mức dương $+c_0$ khi $S_T \le F_0(T)$ và dốc xuống tuyến tính vào miền âm khi $S_T > F_0(T)$.

###### **Lời giải:** 

   1. Đáp án đúng là B (Vị thế mua quyền chọn bán – *Long put position*).

   2. Đáp án đúng là A (Vị thế bán kỳ hạn – *Short forward position*).

   3. Đáp án đúng là C (Vị thế bán quyền chọn mua – *Short call position*).

3. Mô tả điểm mà tại đó một vị thế bán kỳ hạn (*short forward*) và một vị thế mua quyền chọn bán (*long put*) có giá thực hiện ($X$) bằng với giá kỳ hạn, $F_0(T)$, có cùng mức lợi nhuận.

###### **Lời giải:** 

Vị thế bán kỳ hạn và vị thế mua quyền chọn bán sẽ có cùng mức lợi nhuận khi $F_0(T) - S_T = -p_0$ (tức là $S_T - F_0(T) = p_0$). Vị thế bán kỳ hạn hưởng lợi từ sự sụt giảm của giá tài sản cơ sở với giá trị nhận được/lợi nhuận là $[F_0(T) - S_T]$, và vị thế mua quyền chọn bán có lợi nhuận là $\Pi = \max[0, F_0(T) - S_T] - p_0$, theo Phương trình 4, với giá thực hiện bằng giá kỳ hạn, $X = F_0(T)$.

<!-- PDF Page 58 -->

## **BÀI TẬP THỰC HÀNH (*PRACTICE PROBLEMS*)** 

### **Thông tin sau đây liên quan đến các câu hỏi từ 1 đến 4** 

Biomian Limited là một công ty công nghệ sinh học có trụ sở tại Mumbai với cổ phiếu phổ thông cùng các hợp đồng tương lai và quyền chọn được niêm yết trên Sở Giao dịch Chứng khoán Quốc gia (*National Stock Exchange* – NSE). Văn phòng Quản lý Gia sản Viswan (*Viswan Family Office* – VFO) hiện đang sở hữu 10.000 cổ phiếu phổ thông của Biomian. VFO muốn giảm vị thế mua đối với Biomian và đa dạng hóa mức độ tiếp xúc rủi ro trên thị trường cổ phiếu của mình nhưng sẽ trì hoãn việc bán cổ phiếu thu tiền mặt trong sáu tháng vì các lý do về thuế.

**1.** Hợp đồng phái sinh nào sau đây sẵn có cho giám đốc đầu tư (*CIO*) của VFO là phù hợp nhất để giảm mức độ tiếp xúc rủi ro trước sự sụt giảm giá cổ phiếu của Biomian trong sáu tháng tới?

   - **A.** Một vị thế bán quyền chọn bán (*short put position*) trên cổ phiếu Biomian đáo hạn sau sáu tháng

   - **B.** Một vị thế mua quyền chọn mua (*long call position*) trên cổ phiếu Biomian đáo hạn sau sáu tháng

   - **C.** Một vị thế bán hợp đồng tương lai (*short futures position*) trên cổ phiếu Biomian thanh toán sau sáu tháng

**2.** Chiến lược gia thị trường của VFO tin rằng giá cổ phiếu của Biomian sẽ tăng trong sáu tháng tới nhưng muốn bảo vệ trước khả năng sụt giảm giá cổ phiếu của Biomian trong giai đoạn này. Vị thế nào sau đây là phù hợp nhất để VFO quản lý mức độ tiếp xúc rủi ro hiện có đối với Biomian dựa trên quan điểm này?

   - **A.** Một vị thế mua quyền chọn bán (*long put position*) trên cổ phiếu Biomian đáo hạn sau sáu tháng

   - **B.** Một vị thế bán quyền chọn mua (*short call position*) trên cổ phiếu Biomian đáo hạn sau sáu tháng

   - **C.** Một vị thế mua hợp đồng tương lai (*long futures position*) trên cổ phiếu Biomian thanh toán sau sáu tháng

**3.** Giả sử rằng cổ phiếu Biomian tăng giá trong sáu tháng tới. Phát biểu nào sau đây về các chiến lược phái sinh của VFO theo kịch bản này là chính xác nhất?

   - **A.** Một giao dịch bán kỳ hạn cổ phiếu Biomian sau sáu tháng sẽ mang lại lợi nhuận cao hơn so với việc mua quyền bán cổ phiếu Biomian sau sáu tháng.

   - **B.** Việc mua quyền bán cổ phiếu Biomian sau sáu tháng sẽ mang lại lợi nhuận cao hơn so với một giao dịch bán kỳ hạn cổ phiếu Biomian sau sáu tháng.

   - **C.** Chúng ta không có đủ thông tin để xác định liệu một giao dịch bán kỳ hạn hay việc mua quyền bán cổ phiếu Biomian sẽ mang lại lợi nhuận cao hơn sau sáu tháng.

**4.** Chiến lược gia thị trường của VFO đang cân nhắc một chiến lược quyền chọn mua kỳ hạn sáu tháng trên chỉ số chứng khoán chuẩn NIFTY 50 của Ấn Độ nhằm làm tăng mức độ tiếp xúc với thị trường cổ phiếu rộng lớn. Giá của chỉ số NIFTY 50 hôm nay là 15.200 INR, và chiến lược gia quan sát thấy rằng một quyền chọn mua có giá thực hiện ($X$) là 16.000 INR đang được giao dịch với mức phí quyền chọn là 1.500 INR. Đâu là giá trị nhận được (*payoff*) và lợi nhuận (*profit*) của chiến lược này ngay trước khi đáo hạn nếu chỉ số NIFTY 50 đang giao dịch ở mức 16.500 INR?

   - **A.** Giá trị nhận được là 500 INR; lợi nhuận là $-1.000\text{ INR}$.

   - **B.** Giá trị nhận được là 1.300 INR; lợi nhuận là 800 INR.

<!-- PDF Page 59 -->

   - **C.** Giá trị nhận được là 1.300 INR; lợi nhuận là 500 INR.

<!-- PDF Page 60 -->

## **LỜI GIẢI (*SOLUTIONS*)** 

1. C là đáp án đúng. VFO có thể cân nhắc một vị thế bán hợp đồng tương lai (hoặc một giao dịch bán kỳ hạn) đối với cổ phiếu Biomian sau sáu tháng để đạt được mục tiêu của mình. Cam kết chắc chắn này cho phép VFO bù đắp vị thế mua cơ sở của mình bằng một vị thế bán sau sáu tháng tại một mức giá đã thỏa thuận trước. Hợp đồng tương lai là một công cụ phái sinh giao dịch trên sở giao dịch với các điều khoản được tiêu chuẩn hóa do sở giao dịch quy định và yêu cầu phải có ký quỹ ban đầu cùng việc thanh toán hàng ngày. Các đáp án A và B là những quyền đòi hỏi có điều kiện mà cả hai đều có khả năng làm tăng, chứ không phải làm giảm, mức độ tiếp xúc rủi ro của VFO đối với cổ phiếu Biomian sau sáu tháng.

2. A là đáp án đúng. VFO nên mua một quyền chọn bán kỳ hạn sáu tháng trên cổ phiếu Biomian để quản lý mức độ tiếp xúc rủi ro của mình dựa trên quan điểm của chiến lược gia thị trường. Quyền đòi hỏi có điều kiện này cấp cho VFO quyền nhưng không phải nghĩa vụ được bán cổ phiếu Biomian tại một mức giá thực hiện thỏa thuận trước để đổi lấy một khoản phí quyền chọn. Người mua quyền chọn bán thực hiện quyền chọn khi đáo hạn khi giá tài sản cơ sở thấp hơn giá thực hiện. Điều này cho phép VFO tiếp tục hưởng lợi từ sự gia tăng trong giá cổ phiếu của Biomian trong sáu tháng tới với mức rủi ro khi giá giảm được giới hạn. Cả B lẫn C đều không cung cấp cho VFO sự bảo vệ khi giá giảm nếu cổ phiếu Biomian sụt giảm sau sáu tháng.

3. C là đáp án đúng. Theo một giao dịch bán kỳ hạn cổ phiếu Biomian, lợi nhuận là $[F_0(T) - S_T]$. Nếu cổ phiếu tăng giá mạnh trong sáu tháng tới — nghĩa là $S_T > F_0(T)$ — thì khoản lỗ của VFO trên công cụ phái sinh là phần chênh lệch giữa giá kỳ hạn của Biomian, $F_0(T)$, và giá giao ngay, $S_T$. Theo vị thế mua quyền chọn bán trên cổ phiếu Biomian, lợi nhuận của VFO là $\max(0, X - S_T) - p_0$. Nếu cổ phiếu Biomian tăng giá mạnh trong sáu tháng tới (tức là $S_T > X$), thì quyền chọn sẽ hết hạn mà không có giá trị và khoản lỗ của VFO được giới hạn ở mức phí quyền chọn bán đã trả, $p_0$. Chỉ khi biết mức độ tăng cụ thể (ví dụ, nếu $[F_0(T) - S_T] < -p_0$, tức là $S_T - F_0(T) > p_0$), chúng ta mới biết được khoản lỗ của VFO theo cam kết chắc chắn có lớn hơn so với theo quyền đòi hỏi có điều kiện hay không.

4. A là đáp án đúng. Lợi nhuận bằng $\Pi = \max(0, S_T - X) - c_0$, và giá trị nhận được khi đáo hạn bằng $\max(0, S_T - X)$. Giá thực hiện là 16.000 INR, và giá giao ngay ngay trước khi đáo hạn là 16.500 INR, do đó $\Pi = -1.000\text{ INR}$ $[= (16.500 - 16.000) - 1.500]$, và giá trị nhận được bằng $500\text{ INR}$ $[= (16.500 - 16.000)]$.
