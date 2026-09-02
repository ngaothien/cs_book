# **Chương 12 (Chapter 12)**

# **Đại số Tuyến tính trong Xác suất & Thống kê (Linear Algebra in Probability & Statistics)**

# **12.1 Trung bình, Phương sai và Xác suất (Mean, Variance, and Probability)**

Chúng ta đang bắt đầu với ba từ cơ bản của chương này: *trung bình (mean), phương sai (variance) và xác suất (probability).* Hãy để tôi đưa ra một giải thích sơ lược về ý nghĩa của chúng trước khi tôi viết ra bất kỳ công thức nào:

**Trung bình (mean)** là *giá trị trung bình* hoặc giá trị kỳ vọng
**Phương sai (variance)** $\sigma^2$ đo lường *bình phương khoảng cách* trung bình từ giá trị trung bình $m$
Các **xác suất** của $n$ kết quả khác nhau là các số dương $p_1, \dots, p_n$ có tổng bằng 1.

Chắc chắn giá trị trung bình là rất dễ hiểu. Chúng ta sẽ bắt đầu từ đó. Nhưng ngay lập tức chúng ta có hai tình huống khác nhau mà bạn phải phân định rõ ràng. Một mặt, chúng ta có thể có các kết quả *(các giá trị mẫu - sample values)* từ một thử nghiệm đã hoàn thành. Mặt khác, chúng ta có thể có các kết quả kỳ vọng *(giá trị kỳ vọng - expected values)* từ các thử nghiệm trong tương lai. Hãy để tôi đưa ra các ví dụ:

**Các giá trị mẫu (Sample values)** Năm sinh viên năm nhất ngẫu nhiên có độ tuổi **18, 17, 18, 19, 17**
**Trung bình mẫu (Sample mean)** $m = \frac{1}{5}(18 + 17 + 18 + 19 + 17) = \mathbf{17.8}$

**Xác suất (Probabilities)** Độ tuổi trong một lớp sinh viên năm nhất là **17 (20%), 18 (50%), 19 (30%)**
Một sinh viên năm nhất ngẫu nhiên có **độ tuổi kỳ vọng (expected age) $\mathbb{E}[x]$** = (0.2) **17** + (0.5) **18** + (0.3) **19** = **18.1**

Cả hai con số **17.8** và **18.1** đều là những mức trung bình đúng. Trung bình mẫu (sample mean) bắt đầu với $N$ mẫu $x_1, \dots, x_N$ từ một thử nghiệm đã hoàn thành. Giá trị trung bình của chúng là mức *trung bình* của $N$ mẫu được quan sát:
| Trung bình mẫu | $m = \mu = \frac{1}{N}(x_1 + x_2 + \cdots + x_N)$ | (1) |
|-------------|---------------------------------------------------|-----|

**Giá trị kỳ vọng (expected value) của $x$** bắt đầu với các xác suất $p_1, \dots, p_n$ của các độ tuổi $x_1, \dots, x_n$:
| Giá trị kỳ vọng | $m = \mathbb{E}[x] = p_1x_1 + p_2x_2 + \cdots + p_nx_n$ | (2) |
|----------------|---------------------------------------------------------|-----|

Đây là $p \cdot x$. Chú ý rằng $m = \mathbb{E}[x]$ cho chúng ta biết điều phải kỳ vọng, $m = \mu$ cho chúng ta biết những gì chúng ta đã thu được.

Bằng cách lấy nhiều mẫu ($N$ lớn), các kết quả mẫu sẽ tiến gần đến các xác suất. "Luật Số lớn (Law of Large Numbers)" nói rằng với xác suất bằng 1, trung bình mẫu sẽ hội tụ về giá trị kỳ vọng $\mathbb{E}[x]$ của nó khi kích thước mẫu $N$ tăng lên. Một đồng xu đồng chất có xác suất $p_0 = \frac{1}{2}$ ngửa và $p_1 = \frac{1}{2}$ sấp. Khi đó $\mathbb{E}[x] = (\frac{1}{2})0 + \frac{1}{2}(1)$. Tỷ lệ mặt sấp trong $N$ lần tung đồng xu là trung bình mẫu, được kỳ vọng sẽ tiến đến $\mathbb{E}[x] = \frac{1}{2}$.

Điều này *không* có nghĩa là nếu chúng ta thấy mặt ngửa nhiều hơn mặt sấp thì lần tung tiếp theo có khả năng là mặt sấp. Tỷ lệ cược (odds) vẫn là 50-50. 100 hoặc 1000 lần tung đầu tiên có ảnh hưởng đến trung bình mẫu. *Nhưng* 1000 *lần tung đó sẽ không ảnh hưởng đến* giới hạn của nó — bởi vì bạn đang chia cho $N \rightarrow \infty$.

#### **Phương sai (xoay quanh mức trung bình) (Variance (around the mean))**

**Phương sai (variance)** $\sigma^2$ đo lường khoảng cách kỳ vọng (bình phương) so với giá trị trung bình kỳ vọng $\mathbb{E}[x]$. **Phương sai mẫu (sample variance)** $S^2$ đo lường khoảng cách thực tế (bình phương) từ trung bình mẫu. Căn bậc hai là **độ lệch chuẩn (standard deviation)** $\sigma$ hoặc $S$. Sau một bài thi, tôi gửi email $\mu$ và $S$ cho cả lớp. Tôi không biết giá trị trung bình kỳ vọng và phương sai bởi vì tôi không biết các xác suất từ $p_1$ đến $p_{100}$ cho mỗi điểm số. (Sau 50 năm giảng dạy, tôi vẫn không biết phải kỳ vọng điều gì.)

Độ lệch (deviation) luôn là độ lệch *so với* trung bình — trung bình mẫu hoặc trung bình kỳ vọng. Chúng ta đang tìm kiếm quy mô của sự "phân tán (spread)" xung quanh giá trị trung bình $x = m$. Bắt đầu với $N$ mẫu.
| Phương sai mẫu | $S^2 = \frac{1}{N-1} \left[ (x_1 - m)^2 + \dots + (x_N - m)^2 \right]$ | (3) |
|-----------------|------------------------------------------------------------------------|-----|

Các độ tuổi mẫu $x = 18, 17, 18, 19, 17$ có trung bình $m = 17.8$. Mẫu đó có phương sai $0.7$:
$$S^2 = \frac{1}{4} \left[ (.2)^2 + (-.8)^2 + (.2)^2 + (1.2)^2 + (-.8)^2 \right] = \frac{1}{4} (2.8) = \mathbf{0.7}$$

Các dấu trừ biến mất khi chúng ta tính bình phương. Xin lưu ý! Các nhà thống kê chia cho $N - 1 = 4$ (và không phải $N = 5$) để $S^2$ là một ước lượng không chệch (unbiased estimate) của $\sigma^2$. Một bậc tự do (degree of freedom) đã được tính đến trong trung bình mẫu.

Một đồng nhất thức (identity) quan trọng xuất phát từ việc khai triển từng $(x - m)^2$ thành $x^2 - 2mx + m^2$:
$$\begin{aligned} \text{tổng của } (x_i - m)^2 &= (\text{tổng của } x_i^2) - 2m(\text{tổng của } x_i) + (\text{tổng của } m^2) \\ &= (\text{tổng của } x_i^2) - 2m(Nm) + Nm^2 \\ \text{tổng của } (x_i - m)^2 &= (\text{tổng của } x_i^2) - Nm^2. \end{aligned} \quad (4)$$

Đây là một cách tương đương để tìm $(x_1 - m)^2 + \cdots + (x_N - m)^2$ bằng cách cộng $x_1^2 + \cdots + x_N^2$.

Bây giờ hãy bắt đầu với các xác suất $p_i$ (không bao giờ âm!) thay vì các mẫu. Chúng ta tìm các giá trị kỳ vọng thay vì các giá trị mẫu. Phương sai $\sigma^2$ là con số cực kỳ quan trọng trong thống kê.
| Phương sai | $\sigma^2 = \mathbb{E}[(x - m)^2] = p_1(x_1 - m)^2 + \dots + p_n(x_n - m)^2$ |
|----------|----------------------------------------------------------------------|

Chúng ta đang bình phương khoảng cách tính từ giá trị kỳ vọng $m = \mathbb{E}[x]$. Chúng ta không có mẫu, chỉ có các kỳ vọng. Chúng ta biết xác suất nhưng chúng ta không biết kết quả thực nghiệm.

**Ví dụ 1** Tìm phương sai $\sigma^2$ cho độ tuổi của các sinh viên đại học năm nhất.

**Giải** Xác suất của các độ tuổi $x_i = 17, 18, 19$ là $p_i = 0.2$ và $0.5$ và $0.3$. Giá trị kỳ vọng là $m = \sum p_i x_i = 18.1$. Phương sai sử dụng cùng các xác suất đó:
$$\sigma^2 = (0.2)(17 - 18.1)^2 + (0.5)(18 - 18.1)^2 + (0.3)(19 - 18.1)^2$$
$$= (0.2)(1.21) + (0.5)(0.01) + (0.3)(0.81) = 0.49.$$
**Độ lệch chuẩn** là căn bậc hai $\sigma = 0.7$.

Điều này đo lường sự phân tán của $17, 18, 19$ xung quanh $\mathbb{E}[x]$, được tính trọng số bởi các xác suất $.2, .5, .3$.

# **Các Phân phối Xác suất Liên tục (Continuous Probability Distributions)**

Cho đến nay chúng ta đã cho phép $n$ kết quả có thể xảy ra $x_1, \dots, x_n$. Với độ tuổi $17, 18, 19$, chúng ta chỉ có $n = 3$. Nếu chúng ta đo độ tuổi theo ngày thay vì theo năm, sẽ có hàng ngàn độ tuổi có thể xảy ra (quá nhiều). Tốt hơn là nên cho phép *mọi con số giữa* $17$ *và* $20$ — một chuỗi liên tục (continuum) các độ tuổi có thể xảy ra. Khi đó các xác suất $p_1, p_2, p_3$ cho độ tuổi $x_1, x_2, x_3$ phải chuyển thành một **phân phối xác suất (probability distribution)** $p(x)$ cho cả một phạm vi độ tuổi liên tục $17 \leq x \leq 20$.

Cách tốt nhất để giải thích các phân phối xác suất là đưa ra cho bạn hai ví dụ. Chúng sẽ là **phân phối đều (uniform distribution)** và **phân phối chuẩn (normal distribution)**. Cái đầu tiên (đều) thì dễ. Phân phối chuẩn có tầm quan trọng bao trùm tất cả.

**Phân phối đều** Giả sử độ tuổi được phân phối đều giữa $17.0$ và $20.0$. Tất cả các độ tuổi giữa những con số đó đều "có khả năng xảy ra như nhau". Tất nhiên bất kỳ một độ tuổi chính xác nào cũng hoàn toàn không có cơ hội. Xác suất để bạn đạt được con số chính xác $x = 17.1$ hoặc $x = 17 + \sqrt{2}$ là bằng không. Điều bạn có thể thực sự đưa ra (với giả định phân phối đều của chúng ta) là **cơ hội $F(x)$ để một sinh viên năm nhất ngẫu nhiên có độ tuổi nhỏ hơn $x$**:
Cơ hội để độ tuổi nhỏ hơn $x = 17$ là $F(17) = 0 \quad$ ( $x \leq 17$ sẽ không xảy ra )
| Cơ hội để độ tuổi nhỏ hơn $x = 20$ là $F(20) = 1$             | $x \leq 20$ chắc chắn sẽ xảy ra |
|-----------------------------------------------------------------|-------------------------|
| Cơ hội để độ tuổi nhỏ hơn $x$ là $F(x) = \frac{1}{3}(x - 17)$ | $F$ đi từ 0 đến 1    |

Công thức $F(x) = \frac{1}{3}(x - 17)$ cho $F = 0$ tại $x = 17$; khi đó $x \leq 17$ sẽ không xảy ra. Nó cho $F(x) = 1$ tại $x = 20$; khi đó $x \leq 20$ là chắc chắn. Giữa $17$ và $20$, đồ thị của **phân phối tích lũy (cumulative distribution)** $F(x)$ tăng tuyến tính đối với mô hình đồng đều này.

Hãy để tôi vẽ đồ thị của $F(x)$ và đạo hàm của nó $p(x)$ = "hàm mật độ xác suất (probability density function)".

Hình 12.1: $F(x)$ là phân phối tích lũy và đạo hàm của nó $p(x) = dF/dx$ là **hàm mật độ xác suất (probability density function - pdf).** Đối với phân phối đều này, $p(x)$ là hằng số giữa $17$ và $20$. Tổng diện tích dưới đồ thị của $p(x)$ là tổng xác suất $F = 1$.

Bạn có thể nói rằng $p(x) dx$ là xác suất để một mẫu rơi vào khoảng giữa $x$ và $x + dx$. Điều này "đúng vô cùng bé (infinitesimally true)": $p(x) dx$ là $F(x + dx) - F(x)$. Đây là sự thật đầy đủ:
| $F =$ tích phân của $p$ | Xác suất của $a \leq x \leq b = \int_a^b p(x) dx = F(b) - F(a)$ |
|-----------------------------|-------------------------------------------------------------------|

$F(b)$ là xác suất của $x \leq b$. Tôi trừ đi $F(a)$ để giữ $x \geq a$. Điều đó để lại $a \leq x \leq b$.

# **Trung bình và Phương sai của $p(x)$ (Mean and Variance of $p(x)$)**

Giá trị trung bình $m$ và phương sai $\sigma^2$ của một phân phối xác suất là gì? Trước đây chúng ta cộng $p_i x_i$ để nhận được giá trị trung bình (giá trị kỳ vọng). Với một phân phối liên tục, chúng ta **tích phân** $xp(x)$:
$$\text{Trung bình } m = \mathbb{E}[x] = \int_{x=17}^{20} x p(x) dx = \int_{x=17}^{20} (x) \left(\frac{1}{3}\right) dx = 18.5$$

Đối với phân phối đều này, giá trị trung bình $m$ nằm chính giữa $17$ và $20$. Khi đó xác suất của một giá trị ngẫu nhiên $x$ nằm dưới điểm giữa $m = 18.5$ này là $F(m) = \frac{1}{2}$.

Trong MATLAB, `x = rand(1)` chọn một số ngẫu nhiên có phân phối đều giữa $0$ và $1$. Khi đó trung bình kỳ vọng là $m = \frac{1}{2}$. Khoảng từ $0$ đến $x$ có xác suất $F(x) = x$. Khoảng dưới giá trị trung bình $m$ luôn có xác suất $F(m) = \frac{1}{2}$.

Phương sai là khoảng cách bình phương trung bình tới mức trung bình. Với $N$ kết quả, $\sigma^2$ là tổng của $p_i (x_i - m)^2$. Đối với một biến ngẫu nhiên liên tục $x$, tổng sẽ chuyển thành một **tích phân**.
| Phương sai | $\sigma^2 = \mathbb{E}[(x - m)^2] = \int p(x) (x - m)^2 dx$ | (7) |
|----------|--------------------------------------------------------------|-----|

Khi độ tuổi đồng đều giữa $17 \leq x \leq 20$, tích phân có thể dịch chuyển thành $0 \leq x \leq 3$:
$$\sigma^2 = \int_{17}^{20} \frac{1}{3}(x - 18.5)^2 dx = \int_0^3 \frac{1}{3}(x - 1.5)^2 dx = \frac{1}{9}(x - 1.5)^3 \bigg|_{x=0}^{x=3} = \frac{2}{9}(1.5)^3 = \frac{3}{4}.$$

Đó là một ví dụ điển hình, và đây là bức tranh hoàn chỉnh cho một $p(x)$ phân phối đều, từ $0$ đến $a$.
| Phân phối đều cho $0 \leq x \leq a$ | Mật độ | $p(x) = \frac{1}{a}$ | Tích lũy | $F(x) = \frac{x}{a}$ |
|--------------------------------------------|---------|----------------------|------------|----------------------|

$$\text{Trung bình } m = \frac{a}{2} \text{ ở giữa} \quad \text{Phương sai } \sigma^2 = \int_0^a \frac{1}{a} \left(x - \frac{a}{2}\right)^2 dx = \frac{a^2}{12} \quad (8)$$

Giá trị trung bình là một bội số của $a$, phương sai là một bội số của $a^2$. Với $a = 3$, $\sigma^2 = \frac{9}{12} = \frac{3}{4}$. Đối với một số ngẫu nhiên giữa $0$ và $1$ (trung bình $\frac{1}{2}$) phương sai là $\sigma^2 = \frac{1}{12}$.

# **Phân phối Chuẩn: Đường cong Hình chuông (Normal Distribution: Bell-shaped Curve)**

Phân phối chuẩn còn được gọi là phân phối "Gaussian". Nó là hàm quan trọng nhất trong tất cả các hàm mật độ xác suất $p(x)$. Lý do cho tầm quan trọng to lớn của nó đến từ việc lặp lại một thực nghiệm và lấy trung bình các kết quả. Các thực nghiệm có phân phối riêng của chúng (như mặt ngửa và mặt sấp). *Mức trung bình tiến gần đến một phân phối chuẩn.*

**Định lý Giới hạn Trung tâm (Central Limit Theorem - phi chính thức)** Trung bình của $N$ mẫu của "bất kỳ" phân phối xác suất nào đều tiến gần đến phân phối chuẩn khi $N \rightarrow \infty$.

Hãy bắt đầu với "phân phối chuẩn tắc (standard normal distribution)". Nó đối xứng qua $x = 0$, vì vậy giá trị trung bình của nó là $m = 0$. Nó được chọn để có một phương sai chuẩn $\sigma^2 = 1$. Nó được gọi là **$\mathbf{N}(0, 1)$**.
| Phân phối chuẩn tắc | $p(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ | (9) |
|------------------------------|-------------------------------------------|-----|

Đồ thị của $p(x)$ là **đường cong hình chuông (bell-shaped curve)** trong Hình 12.2. Các sự thật tiêu chuẩn là
| Tổng xác suất $= 1$ | $\int_{-\infty}^{\infty} p(x) dx = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-x^2/2} dx = 1$ |
|-----------------------|-----------------------------------------------------------------------------------------------------|

| Trung bình $\mathbb{E}[x] = 0$ | $m = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty x e^{-x^2/2} dx = 0$ |
|-----------------|---------------------------------------------------------------|

| Phương sai $\mathbb{E}[x^2] = 1$ | $\sigma^2 = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} x^2 e^{-x^2/2} dx = 1$ |
|--------------------------|----------------------------------------------------------------------------------------|

Giá trị trung bình bằng không thì dễ thấy vì chúng ta đang lấy tích phân một hàm lẻ. Đổi $x$ thành $-x$ cho thấy rằng "tích phân = - tích phân". Vậy tích phân đó phải là $m = 0$.

Hai tích phân còn lại áp dụng ý tưởng trong Bài 12 để đạt tới số 1. Hình 12.2 cho thấy một đồ thị của $p(x)$ cho phân phối chuẩn $\mathbf{N}(0, \sigma)$ và cả phân phối tích lũy $F(x) =$ tích phân của $p(x)$. Từ tính đối xứng của $p(x)$, bạn thấy *trung bình = không*. Từ $F(x)$, bạn thấy một phép xấp xỉ thực tế rất quan trọng đối với việc thăm dò dư luận:

Xác suất để một mẫu ngẫu nhiên rơi vào khoảng giữa $-\sigma$ và $\sigma$ là $F(\sigma) - F(-\sigma) \approx \frac{2}{3}$.
Điều này là bởi vì $\int_{-\sigma}^{\sigma} p(x) dx$ bằng $\int_{-\infty}^{\sigma} p(x) dx - \int_{-\infty}^{-\sigma} p(x) dx = F(\sigma) - F(-\sigma)$.

Tương tự, xác suất để một giá trị $x$ ngẫu nhiên nằm giữa $-2\sigma$ và $2\sigma$ *("nhỏ hơn hai độ lệch chuẩn so với giá trị trung bình")* là $F(2\sigma) - F(-2\sigma) \approx 0.95$. Nếu bạn có một kết quả thực nghiệm cách xa mức trung bình hơn $2\sigma$, nó khá chắc chắn là không phải ngẫu nhiên: cơ hội = $0.05$. Thử nghiệm thuốc có thể tìm kiếm một xác nhận chặt chẽ hơn, chẳng hạn như xác suất $0.001$. Việc tìm kiếm hạt Higgs đã sử dụng một thử nghiệm cực kỳ nghiêm ngặt về độ lệch $5\sigma$ so với sự tình cờ thuần túy.

Hình 12.2: Phân phối chuẩn tắc $p(x)$ có trung bình $m = 0$ và $\sigma = 1$.

Phân phối chuẩn với bất kỳ giá trị trung bình $m$ và độ lệch chuẩn $\sigma$ nào đều xuất phát từ việc dịch chuyển và kéo giãn phân phối chuẩn tắc $\mathbf{N}(0, 1)$. **Dịch chuyển (Shift)** $x$ **thành** $x - m$. **Kéo giãn (Stretch)** $x - m$ **thành** $(x - m)/\sigma$.
| <div><b>Mật độ Gaussian <math display="block">p(x)</math></b></div> | <div><b>Phân phối chuẩn <math>N(m, \sigma)</math></b></div> |
|----------------------------------------------------------------------|-----------------------------------------------------------------|
| $p(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-(x-m)^2/2\sigma^2}$          | (10)                                                            |

Tích phân của $p(x)$ là $F(x)$ — xác suất để một mẫu ngẫu nhiên sẽ rơi xuống dưới $x$. Vi phân $p(x) dx = F(x + dx) - F(x)$ là xác suất để một mẫu ngẫu nhiên sẽ rơi vào khoảng giữa $x$ và $x + dx$. Không có công thức đơn giản nào để tích phân $e^{-x^2/2}$, vì vậy phân phối tích lũy $F(x)$ này được tính toán và lập bảng rất cẩn thận.

Tích phân của $p(x)$ là $F(x)$ — xác suất để một mẫu ngẫu nhiên sẽ rơi xuống dưới $x$. Vi phân $p(x) dx = F(x + dx) - F(x)$ là xác suất để một mẫu ngẫu nhiên sẽ rơi vào khoảng giữa $x$ và $x + dx$. Không có công thức đơn giản nào để tích phân $e^{-x^2/2}$, vì vậy phân phối tích lũy $F(x)$ này được tính toán và lập bảng rất cẩn thận.

# **$N$ lần Tung Đồng xu và $N \rightarrow \infty$ ($N$ Coin Flips and $N \rightarrow \infty$)**

**Ví dụ 2 Giả sử $x$ là $1$ hoặc $-1$ với xác suất bằng nhau $p_1 = p_{-1} = \frac{1}{2}$.**

Giá trị trung bình là $m = \frac{1}{2}(1) + \frac{1}{2}(-1) = 0$. Phương sai là $\sigma^2 = \frac{1}{2}(1)^2 + \frac{1}{2}(-1)^2 = 1$.

Câu hỏi then chốt là *trung bình* $A_N = (x_1 + \cdots + x_N)/N$. Các $x_i$ độc lập là $\pm 1$ và chúng ta chia tổng của chúng cho $N$. Trung bình kỳ vọng của $A_N$ vẫn bằng 0. Luật Số lớn nói rằng trung bình mẫu này tiến về 0 với xác suất 1. $A_N$ tiến về 0 nhanh như thế nào? **Phương sai $\sigma_N^2$ của nó là gì?**
| Theo tính tuyến tính | $\sigma_N^2 = \frac{\sigma^2}{N^2} + \frac{\sigma^2}{N^2} + \cdots + \frac{\sigma^2}{N^2} = N \frac{\sigma^2}{N^2} = \frac{1}{N}$ | vì $\sigma^2 = 1$. | (11) |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------|------------------------|------|

**Ví dụ 3 Thay đổi các kết quả đầu ra từ $1$ hoặc $-1$ thành $x = 1$ hoặc $x = 0$. Giữ $p_1 = p_0 = \frac{1}{2}$.** Giá trị trung bình mới $m = \frac{1}{2}$ rơi vào khoảng giữa $0$ và $1$. Phương sai chuyển thành $\sigma^2 = \frac{1}{4}$:
$$\mathbf{m} = \frac{1}{2}(1) + \frac{1}{2}(0) = \frac{1}{2} \quad \text{và} \quad \mathbf{\sigma}^2 = \frac{1}{2} \left(1 - \frac{1}{2}\right)^2 + \frac{1}{2} \left(0 - \frac{1}{2}\right)^2 = \frac{1}{4}.$$

Trung bình $A_N$ bây giờ có trung bình $\frac{1}{2}$ và phương sai $\frac{1}{4N} + \cdots + \frac{1}{4N} = \frac{N}{4N^2} = \frac{1}{4N} = \sigma_N^2$. (12)
$\sigma_N^2$ này có kích thước bằng một nửa so với $\sigma_N^2$ trong Ví dụ 2. Điều này phải đúng vì phạm vi mới $0$ đến $1$ có độ dài bằng một nửa so với $-1$ đến $1$. Các Ví dụ 2-3 đang cho thấy một định luật tuyến tính.

**Biến mới $0 - 1$ $x_{\text{new}}$ bằng $\frac{1}{2} x_{\text{old}} + \frac{1}{2}$.** Vì vậy giá trị trung bình $m$ được tăng thêm $\frac{1}{2}$ và phương sai được *nhân* với $(\frac{1}{2})^2$. Một phép dịch chuyển (shift) sẽ làm thay đổi $m$ và việc định tỷ lệ lại (rescaling) làm thay đổi $\sigma$.
$$\mathbf{\text{Tính tuyến tính (Linearity) \quad } x_{\text{new}} = a x_{\text{old}} + b \text{ có } m_{\text{new}} = a m_{\text{old}} + b \text{ và } \sigma_{\text{new}}^2 = a^2 \sigma_{\text{old}}^2.} \quad (13)$$

Dưới đây là kết quả từ ba thử nghiệm số: lấy trung bình ngẫu nhiên $0$ hoặc $1$ qua $N$ lần thử.
**[48 con số 1 từ $N = 100$] \quad [5035 con số 1 từ $N = 10000$] \quad [19967 con số 1 từ $N = 40000$].
Giá trị $X$ chuẩn hóa (standardized)** $X = (x - m)/\sigma = (A_N - \frac{1}{2}) / \frac{1}{2\sqrt{N}}$ tương ứng là **$[-.40]$ \quad $[.70]$ \quad $[-.33]$.**

Định lý Giới hạn Trung tâm nói rằng mức trung bình của nhiều lần tung đồng xu sẽ tiến tới một phân phối chuẩn. Hãy bắt đầu xem điều đó xảy ra như thế nào: **nhị thức tiến đến chuẩn (binomial approaches normal).**

Với mỗi lần tung, xác suất để ngửa là $\frac{1}{2}$. Với $N = 3$ lần tung, xác suất ngửa cả ba lần là $(\frac{1}{2})^3 = \frac{1}{8}$. Xác suất hai lần ngửa và một lần sấp là $\frac{3}{8}$, từ ba chuỗi $HHT$ và $HTH$ và $THH$. Những con số $\frac{1}{8}$ và $\frac{3}{8}$ này là các phần của $(\frac{1}{2} + \frac{1}{2})^3 = \frac{1}{8} + \frac{3}{8} + \frac{3}{8} + \frac{1}{8} = 1$. *Số lần ngửa trung bình trong 3 lần tung là 1.5.*
**Trung bình** $m = (3 \text{ ngửa})\frac{1}{8} + (2 \text{ ngửa})\frac{3}{8} + (1 \text{ ngửa})\frac{3}{8} + 0 = \frac{3}{8} + \frac{6}{8} + \frac{3}{8} = \mathbf{1.5 \text{ ngửa}}$

Với $N$ lần tung, Ví dụ 3 (hoặc theo lẽ thường) cho trung bình là $m = \sum x_i p_i = \frac{1}{2}N$ lần ngửa.

Phương sai $\sigma^2$ dựa trên *khoảng cách bình phương* từ mức trung bình $N/2$ này. Với $N = 3$, phương sai là $\sigma^2 = \frac{3}{4}$ *(bằng $N/4$)*. Để tìm $\sigma^2$, ta cộng $(x_i - m)^2 p_i$ với $m = 1.5$:
$$\sigma^2 = (3 - 1.5)^2 \frac{1}{8} + (2 - 1.5)^2 \frac{3}{8} + (1 - 1.5)^2 \frac{3}{8} + (0 - 1.5)^2 \frac{1}{8} = \frac{9 + 3 + 3 + 9}{32} = \frac{3}{4}.$$

Với bất kỳ $N$ nào, phương sai là $\sigma_N^2 = N/4$. Vậy $\sigma_N = \sqrt{N}/2$.

Hình 12.3 cho thấy cách các xác suất cho $0, 1, 2, 3, 4$ lần ngửa trong $N = 4$ lần tung tiến gần đến phân phối Gaussian hình chuông. Gaussian đó có tâm tại giá trị trung bình $N/2 = 2$. Để đạt đến phân phối Gaussian chuẩn (trung bình $0$ và phương sai $1$), chúng ta tịnh tiến và kéo giãn đồ thị đó. Nếu $x$ là số lần ngửa trong $N$ lần tung — mức trung bình của $N$ kết quả đầu ra là $0-1$ — thì $x$ được tịnh tiến đi một đoạn bằng mức trung bình của nó $m = N/2$ và được kéo giãn bởi $\sigma = \sqrt{N}/2$ để tạo ra giá trị $X$ chuẩn:
| Tịnh tiến và định tỷ lệ (Shifted and scaled) | $X = \frac{x - m}{\sigma} = \frac{x - \frac{1}{2}N}{\sqrt{N}/2}$ | $(N = 4 \text{ có } X = x - 2)$ |
|--------------------|------------------------------------------------------------------|----------------------------------|

**Trừ đi $m$ là "đưa về trung tâm (centering)" hoặc "khử xu hướng (detrending)". Giá trị trung bình của $X$ là không.**
**Chia cho $\sigma$ là "chuẩn hóa (normalizing)" hoặc "tiêu chuẩn hóa (standardizing)". Phương sai của $X$ là 1.**

Hình 12.3: Xác suất $p_i = (1, 4, 6, 4, 1)/16$ đối với số lần ngửa trong $4$ lần tung. Các $p_i$ này tiếp cận một phân phối Gaussian có phương sai $\sigma^2 = N/4$ có tâm tại $m = N/2$. Đối với $X$, Định lý Giới hạn Trung tâm cho sự hội tụ về phân phối chuẩn $\mathbf{N}(0, 1)$.

Thật thú vị khi thấy Định lý Giới hạn Trung tâm cho ra câu trả lời đúng tại điểm tâm $X = 0$. Tại điểm đó, hệ số $e^{-X^2/2}$ bằng $1$. Chúng ta biết rằng phương sai đối với $N$ lần tung đồng xu là $\sigma^2 = N/4$. Tâm của đường cong hình chuông có chiều cao $1/\sqrt{2\pi \sigma^2} = \sqrt{2/N\pi}$.

Chiều cao tại tâm của phân phối tung đồng xu $p_0$ đến $p_N$ (phân phối nhị thức) là bao nhiêu? Với $N = 4$, các xác suất cho $0, 1, 2, 3, 4$ lần ngửa đến từ $(\frac{1}{2} + \frac{1}{2})^4$.
| Xác suất ở tâm (Center probability) $\frac{6}{16}$ | $\left(\frac{1}{2} + \frac{1}{2}\right)^4 = \frac{1}{16} + \frac{4}{16} + \frac{6}{16} + \frac{4}{16} + \frac{1}{16} = 1.$ |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------|

Định lý nhị thức trong Bài 8 cho chúng ta biết xác suất ở tâm $p_{N/2}$ đối với bất kỳ $N$ chẵn nào:
| Xác suất ở tâm $\left(\frac{N}{2} \text{ ngửa}, \frac{N}{2} \text{ sấp}\right)$ là | $\frac{1}{2^N} \frac{N!}{(N/2)!(N/2)!}$ |
|-----------------------------------------------------------------------------------------------|-----------------------------------------|

Với $N = 4$, các giai thừa đó tạo ra $4!/2! 2! = 24/4 = 6$. Với $N$ lớn, công thức Stirling $\sqrt{2\pi N} (N/e)^N$ là một xấp xỉ gần của $N!$. Sử dụng Stirling đối với $N$ và hai lần đối với $N/2$:
| Giới hạn xác suất ở tâm khi tung đồng xu | $p_{N/2} \approx \frac{1}{2^N} \frac{\sqrt{2\pi N} (N/e)^N}{\pi N (N/2e)^N} = \frac{\sqrt{2}}{\sqrt{\pi N}} = \frac{1}{\sqrt{2\pi \sigma^2}}.$ | (14) |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|------|

Ở bước cuối cùng đó, chúng ta đã sử dụng phương sai $\sigma^2 = N/4$ cho bài toán tung đồng xu. Kết quả $1/\sqrt{2\pi \sigma^2}$ khớp với giá trị tâm (ở trên) đối với Gaussian. Định lý Giới hạn Trung tâm là đúng: "Phân phối nhị thức" tiếp cận phân phối chuẩn khi $N \rightarrow \infty$.

#### **Các Phương pháp Ước lượng Monte Carlo (Monte Carlo Estimation Methods)**

Tính toán khoa học phải làm việc với các sai số trong dữ liệu. Tính toán tài chính phải làm việc với những con số không chắc chắn và những dự đoán không rõ ràng. Toàn bộ toán học ứng dụng đã chuyển sang **chấp nhận sự không chắc chắn trong dữ liệu đầu vào và ước tính phương sai ở các kết quả đầu ra.**

Làm thế nào để ước tính phương sai đó? Thông thường các phân phối xác suất $p(x)$ không được biết đến. Những gì chúng ta có thể làm là thử các dữ liệu đầu vào khác nhau $b$ và tính toán các kết quả đầu ra $x$ rồi lấy trung bình. Đây là dạng đơn giản nhất của **phương pháp Monte Carlo** (được đặt theo tên của sòng bạc trên vùng Riviera, nơi tôi đã từng thấy một cuộc cãi vã về việc đặt cược có được thực hiện kịp thời hay không). Phương pháp Monte Carlo tính xấp xỉ một giá trị kỳ vọng $\mathbb{E}[x]$ bằng một trung bình mẫu $(x_1 + \cdots + x_N)/N$.

Hãy hiểu rằng mỗi $x_k$ có thể tốn kém để tính toán. Chúng ta không chỉ tung đồng xu. Mỗi mẫu đến từ một tập dữ liệu $b_k$. *Monte Carlo chọn ngẫu nhiên dữ liệu $b_k$ này, nó tính toán kết quả đầu ra $x_k$, và sau đó nó lấy trung bình các giá trị $x$ đó.* Để có được độ chính xác khá tốt cho $\mathbb{E}[x]$ thường cần đến nhiều mẫu $b$ và chi phí máy tính khổng lồ. Sai số trong việc xấp xỉ $\mathbb{E}[x]$ bằng $(x_1 + \cdots + x_N)/N$ thường có cấp (order) $1/\sqrt{N}$. *Sự cải thiện chậm chạp khi $N$ tăng lên.*

Ước tính $1/\sqrt{N}$ đó xuất hiện đối với việc tung đồng xu trong phương trình (11). Lấy trung bình $N$ mẫu độc lập $x_k$ có phương sai $\sigma^2$ sẽ làm giảm phương sai xuống $\sigma^2/N$.

"Quasi-Monte Carlo" (Monte Carlo tựa ngẫu nhiên) đôi khi có thể làm giảm phương sai này xuống $\sigma^2/N^2$: một sự khác biệt lớn! Các dữ liệu đầu vào $b_k$ được lựa chọn rất cẩn thận — không chỉ một cách ngẫu nhiên. Cách tiếp cận QMC này được khảo sát trong tạp chí *Acta Numerica* 2013. Ý tưởng mới hơn về "Multilevel Monte Carlo" (Monte Carlo đa cấp độ) được phác thảo bởi Michael Giles trong tạp chí *Acta Numerica* 2015. Đây là cách nó hoạt động.

Giả sử việc mô phỏng một biến khác $y(b)$ gần với $x(b)$ là đơn giản hơn nhiều. Khi đó hãy sử dụng $N$ phép tính toán của $y(b_k)$ và chỉ cần $N^* < N$ phép tính của $x(b_k)$ để ước tính $\mathbb{E}[x]$.
| Monte Carlo 2 cấp độ | $\mathbb{E}[x] \approx \frac{1}{N} \sum_1^N y(b_k) + \frac{1}{N^*} \sum_1^{N^*} [x(b_k) - y(b_k)]$ |
|---------------------|----------------------------------------------------------------------------------------------------------|

Ý tưởng là $x - y$ có một phương sai $\sigma^*$ nhỏ hơn so với $x$ ban đầu. Do đó $N^*$ có thể nhỏ hơn $N$, với cùng một độ chính xác đối với $\mathbb{E}[x]$. Chúng ta thực hiện $N$ mô phỏng rẻ tiền để tìm các giá trị $y$. Những mô phỏng đó mỗi cái tiêu tốn $C$. Chúng ta chỉ thực hiện $N^*$ mô phỏng đắt tiền liên quan đến các giá trị $x$. Những mô phỏng đó mỗi cái tốn $C^*$. Tổng chi phí tính toán là $NC + N^*C^*$.

Giải tích giảm thiểu tổng phương sai đối với một tổng chi phí cố định. Tỷ lệ tối ưu $N^*/N$ là $\sqrt{C/C^*}(\sigma^*/\sigma)$. Monte Carlo 3 cấp độ sẽ mô phỏng $x, y$, và $z$:

Giles tối ưu hóa $N, N^*, N^{**}, \dots$ để giữ cho sai số $\mathbb{E}[x]$ $\leq$ $E_0$ cố định, và cung cấp một mã MATLAB.

# **Ôn tập: Ba Công thức cho Trung bình và Phương sai (Review: Three Formulas for the Mean and the Variance)**

Các công thức cho $m$ và $\sigma^2$ là điểm khởi đầu cho toàn bộ phần xác suất và thống kê. Có ba trường hợp khác nhau cần phải phân định rõ ràng: các giá trị **mẫu (sample)** $x_i$, các giá trị **kỳ vọng** (rời rạc $p_i$), và một phạm vi các giá trị **kỳ vọng** (liên tục $p(x)$). Dưới đây là giá trị trung bình và phương sai:
| Các mẫu (Samples) $x_1$ đến $x_N$ | $m = \frac{x_1 + \cdots + x_N}{N}$ | $S^2 = \frac{(x_1 - m)^2 + \cdots + (x_N - m)^2}{N-1}$ |
|------------------------------------------------------|------------------------|------------------------|
| $n$ kết quả đầu ra có thể xảy ra với các xác suất $p_i$ | $m = \sum p_i x_i$ | $\sigma^2 = \sum p_i (x_i - m)^2$ |
| Phạm vi đầu ra (Range of outputs) với mật độ xác suất $p(x)$ | $m = \int x p(x) dx$ | $\sigma^2 = \int (x - m)^2 p(x) dx$ |

Một câu hỏi tự nhiên: Tại sao lại không có xác suất $p$ trên dòng đầu tiên? Làm thế nào mà những công thức này có thể song song với nhau được? Trả lời: *Chúng ta kỳ vọng một tỷ lệ* $p_i$ *của các mẫu bằng* $x_i$. Nếu điều này là hoàn toàn chính xác, $x = x_i$ được lặp lại $p_iN$ lần. Khi đó dòng 1 và 2 mang lại cùng một giá trị $m$.

Khi chúng ta làm việc với các mẫu, chúng ta không biết các $p_i$. Chúng ta chỉ đưa vào mỗi kết quả $x$ thường xuyên như khi nó xuất hiện. Chúng ta có được mức trung bình "theo kinh nghiệm (empirical)" thay vì mức trung bình kỳ vọng.

### **Tập bài tập 12.1 (Problem Set 12.1)**

**1** Cộng thêm 7 vào mỗi kết quả đầu ra $x$. Điều gì xảy ra với giá trị trung bình và phương sai? Mức trung bình mẫu mới, trung bình kỳ vọng mới và phương sai mới là gì?
**2** Chúng ta biết: $\frac{1}{2}$ trong tất cả các số nguyên chia hết cho 3 và $\frac{1}{7}$ các số nguyên chia hết cho 7. Tỷ lệ số nguyên nào sẽ chia hết cho 3 hoặc 7 hoặc cả hai?
**3** Giả sử bạn lấy mẫu từ các số 1 đến 1000 với xác suất bằng nhau là $1/1000$. Xác suất $p_0$ đến $p_9$ để chữ số cuối cùng trong mẫu của bạn là $0, \dots, 9$ là bao nhiêu? Giá trị trung bình kỳ vọng $m$ của chữ số cuối cùng đó là bao nhiêu? Phương sai $\sigma^2$ của nó là gì?
**4** Lấy mẫu lại từ 1 đến 1000 nhưng xem xét chữ số cuối cùng của mẫu được *bình phương*. Bình phương đó có thể kết thúc bằng $x = 0, 1, 4, 5, 6$, hoặc $9$. Các xác suất $p_0, p_1, p_4, p_5, p_6, p_9$ là bao nhiêu? Mức trung bình (kỳ vọng) $m$ và phương sai $\sigma^2$ của con số $x$ đó là bao nhiêu?
**5** (hơi mẹo một chút) Lấy mẫu lại từ 1 đến 1000 với xác suất bằng nhau và gọi $x$ là chữ số *đầu tiên* ($x = 1$ nếu con số là $15$). Các xác suất $p_1$ đến $p_9$ (có tổng bằng 1) của $x = 1, \dots, 9$ là bao nhiêu? Giá trị trung bình và phương sai của $x$ là gì?
**6** Giả sử bạn có $N = 4$ mẫu 157, 312, 696, 602 trong Bài 5. Các chữ số đầu tiên $x_1$ đến $x_4$ của các bình phương là gì? Trung bình mẫu $\mu$ là bao nhiêu? Phương sai mẫu $S^2$ là bao nhiêu? Hãy nhớ chia cho $N - 1 = 3$ chứ không phải $N = 4$.
**7** Phương trình (4) đã đưa ra một dạng tương đương thứ hai đối với $S^2$ (phương sai sử dụng các mẫu):
$$S^2 = \frac{1}{N-1} \text{ tổng của } (x_i - m)^2 = \frac{1}{N-1} [(\text{tổng của } x_i^2) - Nm^2].$$
Xác minh đồng nhất thức tương ứng đối với phương sai kỳ vọng $\sigma^2$ (sử dụng $m = \sum p_i x_i$):
$$\sigma^2 = \text{tổng của } p_i (x_i - m)^2 = (\text{tổng của } p_i x_i^2) - m^2.$$
**8** Nếu cả 24 mẫu từ một quần thể đều tạo ra cùng một độ tuổi $x = 20$, trung bình mẫu $\mu$ và phương sai mẫu $S^2$ là bao nhiêu? Nếu $x = 20$ hoặc $21$, mỗi độ tuổi 12 lần thì sao?
**9** Thực nghiệm máy tính như trên trang 541: Tìm trung bình $A_{1000000}$ của một triệu mẫu ngẫu nhiên $0-1$! $X = (A_N - \frac{1}{2}) / (1/2\sqrt{N})$ bằng bao nhiêu?
**10** Xác suất $p_i$ để có được $i$ lần ngửa trong $N$ lần tung đồng xu là *số nhị thức (binomial number)* $b_i = \binom{N}{i}$ chia cho $2^N$. Các $b_i$ có tổng là $(1+1)^N = 2^N$ vì vậy các xác suất $p_i$ có tổng bằng 1.
$$p_0 + \dots + p_N = \left(\frac{1}{2} + \frac{1}{2}\right)^N = \frac{1}{2^N} (b_0 + \dots + b_N) \text{ với } b_i = \frac{N!}{i!(N-i)!}$$
$$N=4 \text{ dẫn đến } b_0 = \frac{24}{24}, b_1 = \frac{24}{(1)(6)} = 4, b_2 = \frac{24}{(2)(2)} = 6, p_i = \frac{1}{16}(1, 4, 6, 4, 1).$$
Chú ý $b_i = b_{N-i}$. *Bài toán:* Xác nhận rằng giá trị trung bình $m = 0p_0 + \dots + Np_N$ bằng $\frac{N}{2}$.
**11** Đối với bất kỳ hàm $f(x)$ nào, giá trị kỳ vọng là $\mathbb{E}[f] = \sum p_i f(x_i)$ hoặc $\int p(x) f(x) dx$ (xác suất rời rạc hoặc xác suất liên tục). Giả sử giá trị trung bình là $\mathbb{E}[x] = m$ và phương sai là $\mathbb{E}[(x - m)^2] = \sigma^2$. **$\mathbb{E}[x^2]$ bằng bao nhiêu?**
**12** Chỉ ra rằng phân phối chuẩn tắc $p(x)$ có tổng xác suất $\int p(x) dx = 1$ như yêu cầu. Một thủ thuật nổi tiếng nhân $\int p(x) dx$ với $\int p(y) dy$ và tính tích phân qua mọi $x$ và mọi $y$ ($-\infty$ đến $\infty$). Thủ thuật là thay thế $dx dy$ trong tích phân kép đó bằng $r dr d\theta$ (tọa độ cực với $x^2 + y^2 = r^2$). Giải thích mỗi bước:
$$2\pi \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} e^{-(x^2+y^2)/2} dx dy = \int_0^{2\pi} \int_0^{\infty} e^{-r^2/2} r dr d\theta = 2\pi.$$

# **12.2 Ma trận Hiệp phương sai và Xác suất Đồng thời (Covariance Matrices and Joint Probabilities)**

Đại số tuyến tính xuất hiện khi chúng ta chạy $M$ thử nghiệm khác nhau cùng một lúc. Chúng ta có thể đo độ tuổi, chiều cao và cân nặng ($M = 3$ phép đo của $N$ người). Mỗi thử nghiệm có giá trị trung bình riêng. Vậy nên chúng ta có một vectơ $m = (m_1, m_2, m_3)$ chứa $M$ giá trị trung bình. Đó có thể là các *trung bình mẫu* của độ tuổi, chiều cao và cân nặng. Hoặc $m_1, m_2, m_3$ có thể là các *giá trị kỳ vọng* của độ tuổi, chiều cao, cân nặng dựa trên các xác suất đã biết.

Một ma trận được tham gia vào khi chúng ta xem xét các phương sai. Mỗi thử nghiệm sẽ có một phương sai mẫu $S_i^2$ hoặc một phương sai kỳ vọng $\sigma_i^2 = \mathbb{E}[(x_i - m_i)^2]$ dựa trên khoảng cách bình phương từ giá trị trung bình của nó. Những số $M$ đó $\sigma_1^2, \dots, \sigma_M^2$ sẽ đi vào đường chéo chính của ma trận. Cho đến nay chúng ta chưa tạo ra sự kết nối nào giữa $M$ thử nghiệm song song. Chúng đo lường $M$ biến ngẫu nhiên khác nhau, nhưng các thử nghiệm không nhất thiết phải độc lập!

Nếu chúng ta đo độ tuổi, chiều cao và cân nặng ($a, h, w$) cho trẻ em, kết quả sẽ có sự tương quan mạnh mẽ. Trẻ lớn tuổi hơn thường cao hơn và nặng hơn. Giả sử các giá trị trung bình $m_a, m_h, m_w$ đã được biết. Khi đó $\sigma_a^2, \sigma_h^2, \sigma_w^2$ là các phương sai riêng biệt về tuổi, chiều cao, cân nặng. **Những con số mới là các hiệp phương sai (covariances) giống như $\sigma_{ah}$, nơi độ tuổi nhân với chiều cao.**
| Hiệp phương sai (Covariance) | $\sigma_{ah} = \mathbb{E}[(\text{tuổi} - \text{tuổi trung bình}) (\text{chiều cao} - \text{chiều cao trung bình})].$ | (1) |
|------------|---------------------------------------------------------------------------------------------------|-----|

Định nghĩa này cần được xem xét kỹ. Để tính $\sigma_{ah}$, không đủ để chỉ biết xác suất của mỗi độ tuổi và xác suất của mỗi chiều cao. Chúng ta phải biết **xác suất đồng thời (joint probability) của mỗi cặp (độ tuổi và chiều cao).** Đó là do độ tuổi có sự kết nối với chiều cao.
$p_{ah} =$ xác suất để một đứa trẻ ngẫu nhiên có độ tuổi = $a$ **và** chiều cao = $h$: cả hai cùng một lúc
$p_{ij} =$ **xác suất để thử nghiệm 1 tạo ra $x_i$ và thử nghiệm 2 tạo ra $y_j$**

Giả sử thử nghiệm 1 (độ tuổi) có trung bình $m_1$. Thử nghiệm 2 (chiều cao) có trung bình $m_2$. Hiệp phương sai trong (1) giữa thử nghiệm 1 và 2 xem xét **tất cả các cặp** độ tuổi $x_i$, chiều cao $y_j$:
| Hiệp phương sai | $\sigma_{12} = \sum_{i, j} p_{ij}(x_i - m_1)(y_j - m_2)$ | (2) |
|------------|-----------------------------------------------------------------------------|-----|

Để nắm bắt được ý tưởng về "xác suất đồng thời $p_{ij}$", chúng ta bắt đầu bằng hai ví dụ nhỏ.

**Ví dụ 1** Tung hai đồng xu một cách riêng rẽ. Với 1 cho sấp và 0 cho ngửa, các kết quả có thể là $(1, 1)$ hoặc $(1, 0)$ hoặc $(0, 1)$ hoặc $(0, 0)$. Bốn kết quả đó đều có xác suất $p_{11} = p_{10} = p_{01} = p_{00} = \frac{1}{4}$. **Các thử nghiệm độc lập có Xác suất của $(i, j)$ = (Xác suất của $i$)(Xác suất của $j$).**

**Ví dụ 2** *Dán hai đồng xu lại với nhau*, úp cùng một mặt. Các khả năng duy nhất là $(1, 1)$ và $(0, 0)$. Những khả năng đó có xác suất là $\frac{1}{2}$ và $\frac{1}{2}$. Các xác suất $p_{10}$ và $p_{01}$ bằng 0. $(1, 0)$ và $(0, 1)$ sẽ không xảy ra bởi vì hai đồng xu dính lại với nhau: cả hai cùng sấp hoặc cả hai cùng ngửa.
| Các ma trận xác suất cho Ví dụ 1 và 2 | $P = \begin{bmatrix} p_{11} & p_{12} \\ p_{21} & p_{22} \end{bmatrix} = \begin{bmatrix} 1/4 & 1/4 \\ 1/4 & 1/4 \end{bmatrix}$ | $P = \begin{bmatrix} 1/2 & 0 \\ 0 & 1/2 \end{bmatrix}$ |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|

Hãy để tôi dừng lại ở $P$ lâu hơn, để chỉ ra nó trong ký hiệu ma trận tốt. Ma trận hiển thị xác suất $p_{ij}$ của mỗi cặp $(x_i, y_j)$ — bắt đầu với $(x_1, y_1) = (\text{sấp}, \text{sấp})$ và $(x_1, y_2) = (\text{sấp}, \text{ngửa})$. Hãy chú ý các tổng theo hàng $p_i$ và các tổng theo cột $p_j$ và tổng toàn bộ $= 1$.
| Ma trận xác suất (Probability matrix) | $P = \begin{bmatrix} p_{11} & p_{12} \\ p_{21} & p_{22} \end{bmatrix}$ | $p_{11} + p_{12} = p_1 \quad (\text{đồng xu})$<br>$p_{21} + p_{22} = p_2 \quad (\text{thứ nhất})$ |
|--------------------|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| tổng các cột (đồng xu thứ 2) (column sums) | $P_1$ \quad $P_2$ | 4 phần tử có tổng bằng 1 |

Những con số $p_1, p_2$ và $P_1, P_2$ được gọi là **các giá trị biên (marginals)** của ma trận $P$:
$$p_1 = p_{11} + p_{12} = \text{cơ hội sấp từ } \mathbf{\text{đồng xu 1}} \text{ (đồng xu 2 có thể sấp hoặc ngửa)}$$
$$P_1 = p_{11} + p_{21} = \text{cơ hội sấp từ } \mathbf{\text{đồng xu 2}} \text{ (đồng xu 1 có thể sấp hoặc ngửa)}$$

Ví dụ 1 cho thấy các biến *độc lập*. Mỗi xác suất $p_{ij}$ bằng $p_i$ nhân với $P_j$ ($\frac{1}{2}$ nhân với $\frac{1}{2}$ cho $p_{ij} = \frac{1}{4}$ trong ví dụ đó). Trong trường hợp này **hiệp phương sai $\sigma_{12}$ sẽ bằng 0.** Sấp hay ngửa từ đồng xu đầu tiên không cung cấp thông tin gì về đồng xu thứ hai.
| Hiệp phương sai bằng không $\sigma_{12}$ | $V = \begin{bmatrix} \sigma_1^2 & 0 \\ 0 & \sigma_2^2 \end{bmatrix} = \text{ma trận hiệp phương sai đường chéo.}$ |
|-------------------------------|-----------------------------------------------------------------------------------------------------------|
| cho các thử nghiệm độc lập        |                                                                                                           |

Các thử nghiệm độc lập có $\sigma_{12} = 0$ bởi vì mỗi $p_{ij} = (p_i)(P_j)$ trong phương trình (2):
$$\sigma_{12} = \sum_i \sum_j (p_i)(P_j)(x_i - m_1)(y_j - m_2) = \left[ \sum_i (p_i)(x_i - m_1) \right] \left[ \sum_j (P_j)(y_j - m_2) \right] = [\mathbf{0}][\mathbf{0}].$$

Hai đồng xu được dán lại với nhau cho thấy sự tương quan hoàn hảo. Mặt sấp trên một đồng nghĩa là mặt sấp trên đồng kia. Hiệp phương sai $\sigma_{12}$ chuyển từ $0$ thành $\sigma_1 \sigma_2 = \frac{1}{4}$ — đây là giá trị lớn nhất có thể có của $\sigma_{12}$:
| Các giá trị trung bình = $\frac{1}{2}$ | $\sigma_{12} = \frac{1}{2} \left(1 - \frac{1}{2}\right) \left(1 - \frac{1}{2}\right) + \mathbf{0} + \mathbf{0} + \frac{1}{2} \left(0 - \frac{1}{2}\right) \left(0 - \frac{1}{2}\right) = \frac{1}{4}$ |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Sấp hay ngửa từ đồng xu 1 cung cấp thông tin hoàn chỉnh về sấp hay ngửa từ đồng xu 2:
| Đồng xu được dán với nhau mang lại hiệp phương sai lớn nhất có thể có | $V_{\text{glue}} = \begin{bmatrix} \sigma_1^2 & \sigma_1\sigma_2 \\ \sigma_1\sigma_2 & \sigma_2^2 \end{bmatrix}$ |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Ma trận hiệp phương sai suy biến: định thức = 0   |                                                                                                                  |

**Luôn có** $\sigma_{12}^2 \leq \sigma_1^2 \sigma_2^2$. Do đó $\sigma_{12}$ nằm *giữa* $-\sigma_1\sigma_2$ *và* $\sigma_1\sigma_2$. Ma trận hiệp phương sai $V$ là **xác định dương** (hoặc trong trường hợp suy biến của đồng xu được dán này, $V$ là **bán xác định dương**). Đó là một sự thật quan trọng về các ma trận hiệp phương sai $M$ nhân $M$ cho $M$ thử nghiệm.

Lưu ý rằng **ma trận hiệp phương sai mẫu** $S$ từ $N$ lần thử chắc chắn là bán xác định dương. Mỗi mẫu $X$ mới = (độ tuổi, chiều cao, cân nặng) đóng góp vào **trung bình mẫu** $\bar{X}$ và vào $S$. Mỗi số hạng $(X_i - \bar{X})(X_i - \bar{X})^T$ là bán xác định dương và chúng ta chỉ cần cộng lại để đạt được $S$:
$$\bar{X} = \frac{X_1 + \dots + X_N}{N} \quad S = \frac{(X_1 - \bar{X})(X_1 - \bar{X})^T + \dots + (X_N - \bar{X})(X_N - \bar{X})^T}{N-1} \quad (3)$$

# **Ma trận Hiệp phương sai $V$ là Bán xác định dương (The Covariance Matrix $V$ is Positive Semidefinite)**

Quay trở lại với hiệp phương sai *kỳ vọng* $\sigma_{12}$ giữa hai thử nghiệm 1 và 2 (hai đồng xu):
$$\begin{aligned} \sigma_{12} &= \text{giá trị kỳ vọng của } [(\text{kết quả đầu ra } 1 - \text{trung bình } 1) \text{ nhân với } (\text{kết quả đầu ra } 2 - \text{trung bình } 2)] \\ &= \sum_{\text{tất cả } i, j} p_{ij} (x_i - m_1) (y_j - m_2). \end{aligned} \quad (4)$$

$p_{ij} \geq 0$ là xác suất quan sát thấy kết quả $x_i$ trong thử nghiệm 1 **và** $y_j$ trong thử nghiệm 2. Một số cặp kết quả đầu ra phải xuất hiện. Do đó $n^2$ xác suất $p_{ij}$ có tổng bằng 1.
| Tổng xác suất (tất cả các cặp) là 1 | $\sum_{\text{tất cả } i,j} p_{ij} = 1.$ | (5) |
|------------------------------------|--------------------------------------------|-----|

Đây là một sự thật khác mà chúng ta cần. *Cố định vào một kết quả cụ thể* $x_i$ trong thử nghiệm 1. Cho phép *tất cả các kết quả* $y_j$ trong thử nghiệm 2. Cộng các xác suất của $(x_i, y_1), (x_i, y_2), \dots, (x_i, y_n)$:
| Tổng theo hàng $p_i$ của $P$ | $\sum_{j=1}^n p_{ij} = \text{xác suất } p_i \text{ của } x_i \text{ trong thử nghiệm 1.}$ | (6) |
|----------------------|------------------------------------------------------------------------------------------|-----|

Một $y_j$ nào đó phải xảy ra trong thử nghiệm 2! Cho dù hai đồng xu là hoàn toàn tách biệt hay được dán lại với nhau, chúng ta vẫn nhận được $\frac{1}{2}$ cho xác suất $p_H = P_{HH} + P_{HT}$ rằng đồng xu 1 là sấp:
| (riêng biệt) $P_{HH} + P_{HT} = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}$ | (được dán) $P_{HH} + P_{HT} = \frac{1}{2} + 0 = \frac{1}{2}$. |
|------------------------------------------------------------------------|-------------------------------------------------------------|

Lập luận cơ bản đó cho phép chúng ta viết một công thức ma trận bao gồm hiệp phương sai $\sigma_{12}$ cùng với các phương sai riêng biệt $\sigma_1^2$ và $\sigma_2^2$ cho thử nghiệm 1 và thử nghiệm 2. Chúng ta có được toàn bộ ma trận hiệp phương sai $V$ bằng cách cộng các ma trận $V_{ij}$ cho mỗi cặp $(i, j)$:
| Ma trận hiệp phương sai | $V = \sum_{i,j} p_{ij} \begin{bmatrix} (x_i - m_1)^2 & (x_i - m_1)(y_j - m_2) \\ (x_i - m_1)(y_j - m_2) & (y_j - m_2)^2 \end{bmatrix}$ | (7) |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|-----|

Ngoại trừ trên đường chéo, đây là phương trình (2) cho hiệp phương sai $\sigma_{12}$. Trên đường chéo, chúng ta đang thu được các phương sai thông thường $\sigma_1^2$ và $\sigma_2^2$. Tôi sẽ trình bày chi tiết cách chúng ta có được $V_{11} = \sigma_1^2$ bằng cách sử dụng phương trình (6). Cho phép tất cả $j$ chỉ để lại xác suất $p_i$ của $x_i$ trong thử nghiệm 1:
$$\mathbf{V}_{11} = \sum_{\text{tất cả } i,j} p_{ij}(x_i - m_1)^2 = \sum_i (\text{xác suất của } x_i) (x_i - m_1)^2 = \sigma_1^2. \quad (8)$$

Vui lòng xem lại điều đó hai lần. Đó là chìa khóa để tạo ra toàn bộ ma trận hiệp phương sai bằng một công thức (7). Vẻ đẹp của công thức đó là nó kết hợp các ma trận $2 \times 2$ $V_{ij}$. Và ma trận $V_{ij}$ trong (7) cho mỗi cặp kết quả $i, j$ là **bán xác định dương:**
| $V_{ij}$ | có các phần tử trên đường chéo $p_{ij}(x_i - m_1)^2 \geq 0$ | và $p_{ij}(y_j - m_2)^2 \geq 0$ | và | $\det(V_{ij}) = 0$. |
|----------|---------------------------------------------------|----------------------------------|-----|---------------------|

Ma trận $V_{ij}$ đó có hạng 1. Phương trình (7) nhân $p_{ij}$ *với cột $U$ nhân với hàng $U^T$*:
$$\begin{bmatrix} (x_i - m_1)^2 & (x_i - m_1)(y_j - m_2) \\ (x_i - m_1)(y_j - m_2) & (y_j - m_2)^2 \end{bmatrix} = \begin{bmatrix} x_i - m_1 \\ y_j - m_2 \end{bmatrix} \begin{bmatrix} x_i - m_1 & y_j - m_2 \end{bmatrix} \quad (9)$$

*Mọi ma trận $UU^T$ đều là bán xác định dương.* Do đó toàn bộ ma trận $V$ (kết hợp các ma trận $UU^T$ này với các trọng số $p_{ij} \geq 0$) là **ít nhất cũng là bán xác định — và** có lẽ $V$ là xác định.

**Ma trận hiệp phương sai $V$ là xác định dương trừ khi các thử nghiệm phụ thuộc vào nhau.**

Bây giờ chúng ta chuyển từ hai biến $x$ và $y$ sang $M$ biến giống như tuổi-chiều cao-cân nặng. Kết quả từ mỗi thử nghiệm là một vectơ $X$ có $M$ thành phần. (Mỗi đứa trẻ có một vectơ tuổi-chiều cao-cân nặng với 3 thành phần.) Ma trận hiệp phương sai $V$ bây giờ là $M$ nhân $M$. $V$ được tạo ra từ các vectơ kết quả $X$ và giá trị trung bình $\bar{X} = \mathbb{E}[X]$ của chúng.
| Ma trận hiệp phương sai | $V = \mathbb{E} \left[ (X - \bar{X}) (X - \bar{X})^T \right]$ | (10) |
|-------------------|------------------------------------------------------|------|

Hãy nhớ rằng $X X^T$ và $\bar{X} \bar{X}^T$ = (cột)(hàng) là các ma trận $M$ nhân $M$.

Với $M = 1$ (một biến), bạn thấy rằng $\bar{X}$ là giá trị trung bình $m$ và $V$ là $\sigma^2$ (Phần 12.1). Với $M = 2$ (hai đồng xu), bạn thấy rằng $\bar{X}$ là $(m_1, m_2)$ và $V$ khớp với phương trình (10). Giá trị kỳ vọng $\mathbb{E}$ luôn cộng các kết quả đầu ra nhân với xác suất của chúng. Đối với tuổi-chiều cao-cân nặng, kết quả đầu ra có thể là $X =$ (5 tuổi, 31 inch, 48 pound) và xác suất của nó là $p_{5, 31, 48}$.

Bây giờ đến một ý tưởng mới. *Lấy bất kỳ tổ hợp tuyến tính nào* $c^T X = c_1 X_1 + \cdots + c_M X_M$. Với $c = (6, 2, 5)$, cái này sẽ là $c^T X = 6 \text{ (tuổi)} + 2 \text{ (chiều cao)} + 5 \text{ (cân nặng)}$. Bằng tính tuyến tính, chúng ta biết rằng giá trị kỳ vọng $\mathbb{E}[c^T X]$ của nó là $c^T \mathbb{E}[X] = c^T \bar{X}$:
$$\mathbb{E}[c^T X] = c^T \mathbb{E}[X] = 6 \text{ (tuổi kỳ vọng)} + 2 \text{ (chiều cao kỳ vọng)} + 5 \text{ (cân nặng kỳ vọng)}.$$

Hơn thế nữa, chúng ta cũng biết *phương sai* $\sigma^2$ của con số $c^T X$ đó:
$$\begin{aligned} \text{Phương sai của } c^T X &= \mathbb{E} \left[ (c^T X - c^T \bar{X}) (c^T X - c^T \bar{X})^T \right] \\ &= c^T \mathbb{E} \left[ (X - \bar{X}) (X - \bar{X})^T \right] c = c^T V c \end{aligned} \quad (11)$$

Bây giờ là điểm cốt lõi: *Phương sai của $c^T X$ không bao giờ có thể là số âm.* Vậy nên $c^T V c \geq 0$. *Do đó ma trận hiệp phương sai $V$ là bán xác định dương thông qua phép thử năng lượng* $c^T V c \geq 0$.

Các ma trận hiệp phương sai $V$ mở ra mối liên kết giữa xác suất và đại số tuyến tính: $V$ bằng $Q \Lambda Q^T$ với các trị riêng $\lambda_i \geq 0$ và các vectơ riêng trực chuẩn $q_1$ đến $q_M$.

**Chéo hóa ma trận hiệp phương sai có nghĩa là tìm ra $M$ thử nghiệm *độc lập* dưới dạng các tổ hợp của $M$ thử nghiệm ban đầu.**

**Thú nhận** Tôi không hoàn toàn hài lòng với phép chứng minh đó dựa trên $c^T V c \geq 0$. Ký hiệu giá trị kỳ vọng $\mathbb{E}$ đang che giấu ý tưởng cốt lõi về **xác suất đồng thời.** Cho phép tôi chỉ ra trực tiếp rằng $V$ là bán xác định dương (ít nhất là đối với ví dụ tuổi-chiều cao-cân nặng). Phép chứng minh đơn giản là $V$ **là tổng của xác suất đồng thời** $p_{ahw}$ **của mỗi kết hợp (tuổi, chiều cao, cân nặng) nhân với ma trận bán xác định dương** $UU^T$. Ở đây $U$ là $X - \bar{X}$:
$$V = \sum_{\text{tất cả } a, h, w} p_{ahw} U U^T \quad \text{với} \quad U = \begin{bmatrix} \text{tuổi} \\ \text{chiều cao} \\ \text{cân nặng} \end{bmatrix} - \begin{bmatrix} \text{tuổi trung bình} \\ \text{chiều cao trung bình} \\ \text{cân nặng trung bình} \end{bmatrix}. \quad (12)$$

Điều này hoàn toàn giống với ma trận tung đồng xu $2 \times 2$ $V$ trong phương trình (7). Bây giờ $M = 3$.

Giá trị của ký hiệu kỳ vọng $\mathbb{E}$ là nó cũng cho phép các *pdf* (các hàm mật độ xác suất như $p(x, y, z)$ đối với các biến ngẫu nhiên liên tục $x, y$ và $z$). Nếu chúng ta cho phép tất cả các con số đóng vai trò là tuổi, chiều cao và cân nặng, thay vì tuổi $i = 0, 1, 2, 3 \dots$, thì chúng ta cần $p(x, y, z)$ thay vì $p_{ijk}$. Các tổng trong phần này của tài liệu tất cả sẽ chuyển thành các tích phân. Nhưng chúng ta vẫn có $V = \mathbb{E}[U U^T]$:
**Ma trận hiệp phương sai**
$$V = \iiint p(x, y, z) U U^T dx dy dz \quad \text{với} \quad U = \begin{bmatrix} x - \bar{x} \\ y - \bar{y} \\ z - \bar{z} \end{bmatrix}. \quad (13)$$

Luôn có $\iiint p = 1$. Ví dụ 1-2 đã nhấn mạnh việc $p$ có thể mang lại $V$ đường chéo hoặc $V$ suy biến như thế nào:
**Các biến độc lập** $x, y, z$: $p(x, y, z) = p_1(x) p_2(y) p_3(z)$.
**Các biến phụ thuộc** $x, y, z$: $p(x, y, z) = 0$ ngoại trừ khi $cx + dy + ez = 0$.

### **Giá trị Trung bình và Phương sai của $z = x + y$ (The Mean and Variance of $z = x + y$)**

Bắt đầu với trung bình mẫu. Chúng ta có $N$ mẫu của $x$. Giá trị trung bình (mức trung bình) của chúng là $m_x$. Chúng ta cũng có $N$ mẫu của $y$ và giá trị trung bình của chúng là $m_y$. **Trung bình mẫu của $z = x + y$ rõ ràng là** $m_z = m_x + m_y$:
| Giá trị trung bình của tổng = Tổng các giá trị trung bình | $\frac{1}{N} \sum_1^N (x_i + y_i) = \frac{1}{N} \sum_1^N x_i + \frac{1}{N} \sum_1^N y_i.$ | (14) |
|----------------------------|-------------------------------------------------------------------------------------------|------|

Thật tuyệt khi thấy một thứ gì đó đơn giản như vậy. Giá trị trung bình *kỳ vọng* của $z = x + y$ có vẻ không đơn giản như thế, nhưng nó phải ra kết quả là $\mathbb{E}[z] = \mathbb{E}[x] + \mathbb{E}[y]$. Đây là một cách để nhận ra điều này.

Xác suất đồng thời của cặp $(x_i, y_j)$ là $p_{ij}$. Giá trị của nó phụ thuộc vào việc các thử nghiệm có độc lập hay không, điều mà chúng ta không biết. Nhưng đối với giá trị trung bình của tổng $z = x + y$, sự phụ thuộc hay độc lập của $x$ và $y$ không quan trọng. Các giá trị kỳ vọng vẫn được cộng lại với nhau:
$$\mathbb{E}[x + y] = \sum_i \sum_j p_{ij}(x_i + y_j) = \sum_i \sum_j p_{ij}x_i + \sum_i \sum_j p_{ij}y_j. \quad (15)$$

Tất cả các tổng đều đi từ $1$ đến $N$. Chúng ta có thể cộng theo bất kỳ thứ tự nào. Đối với số hạng đầu tiên ở vế phải, cộng các $p_{ij}$ dọc theo hàng $i$ của ma trận xác suất $P$ để nhận được $p_i$. Tổng kép đó mang lại $\mathbb{E}[x]$:
$$\sum_i \sum_j p_{ij} x_i = \sum_i (p_{i1} + \cdots + p_{iN}) x_i = \sum_i p_i x_i = \mathbb{E}[x].$$

Đối với số hạng cuối cùng, cộng $p_{ij}$ dọc theo cột $j$ của ma trận để nhận được xác suất $P_j$ của $y_j$. Các cặp $(x_1, y_j)$ và $(x_2, y_j)$ và $\dots$ và $(x_N, y_j)$ đó là tất cả các cách để tạo ra $y_j$:
$$\sum_i \sum_j p_{ij} y_j = \sum_j (p_{1j} + \cdots + p_{Nj}) y_j = \sum_j P_j y_j = \mathbb{E}[y].$$

Bây giờ phương trình (15) nói rằng $\mathbb{E}[x + y] = \mathbb{E}[x] + \mathbb{E}[y]$.

Còn phương sai của $z = x + y$ thì sao? Các xác suất đồng thời $p_{ij}$ và hiệp phương sai $\sigma_{xy}$ sẽ có liên quan. Cho phép tôi tách phương sai của $x + y$ thành ba phần đơn giản:
$$\begin{aligned}\sigma_z^2 &= \sum \sum p_{ij}(x_i + y_j - m_x - m_y)^2 \\ &= \sum \sum p_{ij}(x_i - m_x)^2 + \sum \sum p_{ij}(y_j - m_y)^2 + 2 \sum \sum p_{ij}(x_i - m_x)(y_j - m_y)\end{aligned}$$

Phần đầu tiên là $\sigma_x^2$. Phần thứ hai là $\sigma_y^2$. Phần cuối cùng là **$2\sigma_{xy}$**.
| <b>Phương sai của <math display="block">z = x + y</math></b> | <b><math>z</math></b> | $\sigma_z^2 = \sigma_x^2 + \sigma_y^2 + 2\sigma_{xy}$ | <b>(16)</b> |
|---------------------------------------------------------------|-----------------------|-------------------------------------------------------|-------------|

#### **Ma trận Hiệp phương sai cho $Z = AX$ (The Covariance Matrix for $Z = AX$)**

Đây là một cách tốt để thấy $\sigma_z^2$ khi $z = x + y$. Hãy nghĩ về $(x, y)$ như một vectơ cột $X$. Hãy nghĩ về ma trận $1 \times 2$ $A = \begin{bmatrix} 1 & 1 \end{bmatrix}$ nhân với vectơ $X$ đó. Khi đó $AX$ là tổng $z = x + y$. Phương sai $\sigma_z^2$ trong phương trình (16) được đưa vào ký hiệu ma trận là
$$\sigma_z^2 = \begin{bmatrix} 1 & 1 \end{bmatrix} \begin{bmatrix} \sigma_x^2 & \sigma_{xy} \\ \sigma_{xy} & \sigma_y^2 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \end{bmatrix} \quad \text{đó là} \quad \sigma_z^2 = AVA^T. \quad (17)$$

Bạn có thể thấy rằng $\sigma_z^2 = AV A^T$ trong (17) khớp với $\sigma_x^2 + \sigma_y^2 + 2\sigma_{xy}$ trong (16).

Bây giờ đến điểm chính. Vectơ $X$ có thể có $M$ thành phần đến từ $M$ thử nghiệm (thay vì chỉ 2). Các thử nghiệm đó sẽ có một ma trận hiệp phương sai $M \times M$ là $V_X$. Ma trận $A$ có thể là $K \times M$. Khi đó $AX$ là một vectơ với $K$ tổ hợp của $M$ kết quả đầu ra (thay vì $1$ tổ hợp $x + y$ của $2$ kết quả đầu ra).

Vectơ $Z = AX$ đó có chiều dài $K$ có một ma trận hiệp phương sai $K \times K$ là $V_Z$. Khi đó quy tắc tuyệt vời dành cho các ma trận hiệp phương sai — trong đó phương trình (17) chỉ là một ví dụ $1 \times 2$ — chính là công thức đẹp đẽ này: Ma trận hiệp phương sai của $AX$ là $A$ (ma trận hiệp phương sai của $X$) $A^T$:
| <b>Ma trận hiệp phương sai của <math display="block">Z = AX</math> là <math>V_Z = AV_X A^T</math></b> | (18) |
|----------------------------------------------------------------------------------------------------|------|

Đối với tôi, công thức gọn gàng này cho thấy vẻ đẹp của phép nhân ma trận. Tôi sẽ không chứng minh công thức này, chỉ chiêm ngưỡng nó. Nó liên tục được sử dụng trong các ứng dụng — sẽ xuất hiện trong Phần 12.3.

### **Sự Tương quan $\rho$ (The Correlation $\rho$)**

Sự tương quan $\rho_{xy}$ có liên quan chặt chẽ đến hiệp phương sai $\sigma_{xy}$. Cả hai đều đo lường sự phụ thuộc hay sự độc lập. Bắt đầu bằng cách định tỷ lệ lại hoặc "tiêu chuẩn hóa" các biến ngẫu nhiên $x$ và $y$. **Biến mới $X = x/\sigma_x$ và $Y = y/\sigma_y$ có phương sai $\sigma_X^2 = \sigma_Y^2 = 1$.** Điều này giống như việc chia một vectơ $v$ cho độ dài của nó để tạo ra một vectơ đơn vị $v/\|v\|$ có chiều dài 1.

**Sự tương quan của $x$ và $y$ là hiệp phương sai của $X$ và $Y$.** Nếu hiệp phương sai ban đầu của $x$ và $y$ là $\sigma_{xy}$, thì việc định tỷ lệ lại thành $X$ và $Y$ sẽ chia cho $\sigma_x$ và $\sigma_y$:
| Sự tương quan | $\rho_{xy} = \frac{\sigma_{xy}}{\sigma_x \sigma_y} = \text{hiệp phương sai của } \frac{x}{\sigma_x} \text{ và } \frac{y}{\sigma_y}$ | Luôn luôn $-1 \leq \rho_{xy} \leq 1$ |
|-------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|

Hiệp phương sai bằng không mang lại sự tương quan bằng không. *Các biến ngẫu nhiên độc lập* tạo ra $\rho_{xy} = 0$.

Chúng ta biết rằng luôn luôn có $\sigma_{xy}^2 \leq \sigma_x^2\sigma_y^2$ (ma trận hiệp phương sai $V$ ít nhất là bán xác định dương). Khi đó $\rho_{xy}^2 \leq 1$. Sự tương quan gần $\rho = +1$ có nghĩa là sự phụ thuộc mạnh mẽ theo cùng một hướng: thường bỏ phiếu giống nhau. Tương quan âm có nghĩa là $y$ có xu hướng ở dưới mức trung bình của nó khi $x$ ở trên mức trung bình của nó: Bỏ phiếu theo các hướng trái ngược.

**Ví dụ 3** *Giả sử rằng $y$ chỉ là $-x$.* Việc tung một đồng xu có kết quả $x = 0$ hoặc $1$. Cùng một lần tung đó có kết quả $y = 0$ hoặc $-1$. Giá trị trung bình $m_x$ là $\frac{1}{2}$ đối với một đồng xu đồng chất, và $m_y$ là $-\frac{1}{2}$. Hiệp phương sai là $\sigma_{xy} = -\sigma_x\sigma_y$. Tương quan sẽ chia cho $\sigma_x\sigma_y$ để thu được $\rho_{xy} = -1$. Trong trường hợp này ma trận tương quan $R$ có định thức bằng không (suy biến và chỉ là bán xác định):
| Ma trận tương quan | $R = \begin{bmatrix} 1 & \rho_{xy} \\ \rho_{xy} & 1 \end{bmatrix}$ | $R = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$ | khi $y = -x$ |
|--------------------|--------------------------------------------------------------------|------------------------------------------------------|---------------|

*$R$ luôn luôn có số $1$ trên đường chéo bởi vì chúng ta đã chuẩn hóa về $\sigma_X = \sigma_Y = 1$.* $R$ là ma trận tương quan cho $x$ và $y$, và là ma trận hiệp phương sai cho $X = x/\sigma_x$ và $Y = y/\sigma_y$.

Con số $\rho_{xy}$ đó còn được gọi là hệ số Pearson.

**Ví dụ 4** Giả sử các biến ngẫu nhiên $x, y, z$ là *độc lập. Ma trận $R$ là gì?*

*Trả lời $R$ là ma trận đơn vị.* Tất cả ba sự tương quan $\rho_{xx}, \rho_{yy}, \rho_{zz}$ đều bằng $1$ theo định nghĩa. Tất cả ba sự tương quan chéo $\rho_{xy}, \rho_{xz}, \rho_{yz}$ đều bằng không do tính độc lập.

Ma trận tương quan $R$ xuất phát từ ma trận hiệp phương sai $V$, khi chúng ta định tỷ lệ lại cho mọi hàng và mọi cột. Chia mỗi hàng $i$ và cột $i$ cho độ lệch chuẩn thứ $i$ là $\sigma_i$.
- (a) $R = DVD$ đối với ma trận đường chéo $D = \text{diag}[1/\sigma_1, \dots, 1/\sigma_M]$.
- (b) Nếu hiệp phương sai $V$ là xác định dương, thì tương quan $R = DVD$ cũng là xác định dương.

#### **• CÁC VÍ DỤ ĐÃ GIẢI (WORKED EXAMPLES) •**

**12.2 A** Giả sử $x$ và $y$ là các biến ngẫu nhiên độc lập có giá trị trung bình bằng 0 và phương sai bằng 1. Khi đó ma trận hiệp phương sai $V_X$ cho $X = (x, y)$ là ma trận đơn vị $2 \times 2$. Trung bình $m_Z$ và ma trận hiệp phương sai $V_Z$ cho vectơ 3 thành phần $Z = (x, y, ax + by)$ là gì?

**Giải**

$Z$ được kết nối với $X$ bởi $A$
$$Z = \begin{bmatrix} x \\ y \\ ax + by \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ a & b \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = AX.$$

Vectơ $m_X$ chứa các giá trị trung bình của $M$ thành phần của $X$. Vectơ $m_Z$ chứa các giá trị trung bình của $K$ thành phần của $Z = AX$. Mối liên kết ma trận giữa các giá trị trung bình của $X$ và $Z$ phải là tuyến tính: $m_Z = Am_X$. Giá trị trung bình của $ax + by$ là $am_x + bm_y$.

Ma trận hiệp phương sai cho $Z$ là $V_Z = AV_XA^T$, khi $V_X$ là ma trận đơn vị $2 \times 2$:
$$V_Z = \text{ma trận hiệp phương sai cho } Z = (x, y, ax + by) = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ a & b \end{bmatrix} \begin{bmatrix} 1 & 0 & a \\ 0 & 1 & b \end{bmatrix} = \begin{bmatrix} 1 & 0 & a \\ 0 & 1 & b \\ a & b & a^2 + b^2 \end{bmatrix}.$$

Giải thích: $x$ và $y$ độc lập nên $\sigma_{xy} = 0$. Khi đó hiệp phương sai của $x$ với $ax + by$ là $a$ và hiệp phương sai của $y$ với $ax + by$ là $b$. Những giá trị đó chỉ đến từ hai phần độc lập của $ax + by$. Cuối cùng, phương trình (18) đưa ra phương sai của $ax + by$:
| Sử dụng $V_Z = AV_XA^T$ | $\sigma_{ax+by}^2 = \sigma_{ax}^2 + \sigma_{by}^2 + 2\sigma_{ax,by} = a^2 + b^2 + 0.$ |
|----------------------|---------------------------------------------------------------------------------------|

Ma trận $3 \times 3$ $V_Z$ là *suy biến*. Định thức của nó là $a^2 + b^2 - a^2 - b^2 = 0$. Thành phần thứ ba $z = ax + by$ hoàn toàn phụ thuộc vào $x$ và $y$. Hạng của $V_Z$ chỉ bằng $2$.

**Ví dụ về GPS** Tín hiệu từ vệ tinh GPS bao gồm cả thời gian khởi hành của nó. Đồng hồ của máy thu cung cấp thời gian đến. Máy thu nhân thời gian di chuyển với tốc độ ánh sáng. Khi đó nó biết được khoảng cách từ vệ tinh đó. Khoảng cách từ bốn hoặc nhiều vệ tinh sẽ xác định chính xác vị trí của máy thu (sử dụng bình phương tối thiểu!).

Một vấn đề: Tốc độ ánh sáng thay đổi trong tầng điện ly. Nhưng sự hiệu chỉnh sẽ gần như giống nhau đối với tất cả các máy thu ở gần nhau. Nếu một máy thu ở vị trí đã biết, chúng ta có thể lấy sự khác biệt từ vị trí đó. **GPS vi phân (Differential GPS)** làm giảm phương sai sai số:
| Ma trận hiệu số (Difference matrix)                                    | Ma trận hiệp phương sai (Covariance matrix) | $V_Z = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$ | $\sigma_1^2 - 2\sigma_{12} + \sigma_2^2$ |
|------------------------------------------------------|-------------------|--------------------------------------------------------|------------------------------------------|
| $A = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$ | $AV_X A^T$        |                                                        |                                          |

Các sai số trong tốc độ ánh sáng đã biến mất. Khi đó độ chính xác định vị ở mức centimet là có thể đạt được. (Các ý tưởng then chốt nằm trên trang 320 của cuốn *Algorithms for Global Positioning* bởi Borre và Strang). Thế giới GPS là tất cả về không gian và thời gian cùng với độ chính xác đáng kinh ngạc.

### **Tập bài tập 12.2 (Problem Set 12.2)**

**1** (a) Tính phương sai $\sigma^2$ khi các xác suất tung đồng xu là $p$ và $1 - p$ (sấp = $0$, ngửa = $1$).
(b) Tổng của $N$ lần tung độc lập ($0$ hoặc $1$) là số đếm của số lần ngửa sau $N$ lần thử. Quy tắc (16-17-18) đối với phương sai của một tổng cho ra $\sigma^2 = \_\_\_$.
**2** Hiệp phương sai $\sigma_{35}$ giữa các kết quả $x_1, \dots, x_N$ của Thử nghiệm 3 và các kết quả $y_1, \dots, y_N$ của Thử nghiệm 5 là bao nhiêu? Công thức của bạn sẽ trông giống như $\sigma_{12}$ trong phương trình (2). Sau đó các phần tử $(3, 5)$ và $(5, 3)$ của ma trận hiệp phương sai $V$ là $\sigma_{35} = \sigma_{53}$.
**3** Đối với $M = 3$ thử nghiệm, ma trận hiệp phương sai $V$ sẽ là $3 \times 3$. Sẽ có một xác suất $p_{ijk}$ để ba kết quả đầu ra là $x_i$ và $y_j$ và $z_k$. Hãy viết một công thức giống như phương trình (7) cho ma trận $V$.
**4** Ma trận hiệp phương sai $V$ cho $M = 3$ thử nghiệm độc lập có trung bình $m_1, m_2, m_3$ và phương sai $\sigma_1^2, \sigma_2^2, \sigma_3^2$ là gì?

**Các Bài toán 5-9 nói về xác suất có điều kiện (conditional probability) để $Y = y_j$ khi chúng ta biết $X = x_i$.**
Ký hiệu: **Xác suất** $(Y = y_j | X = x_i) =$ xác suất của kết quả $Y = y_j$ cho biết (given that) $X = x_i$.
*Ví dụ 1 Đồng xu 1 được dán vào đồng xu 2.* Khi đó Xác suất ($Y =$ ngửa khi $X =$ ngửa) là 1.
*Ví dụ 2 Các lần tung đồng xu độc lập*: $X$ không cung cấp thông tin gì về $Y$. Việc biết $X$ là vô ích. Khi đó Xác suất ($Y =$ ngửa | $X =$ ngửa) cũng giống như Xác suất ($Y =$ ngửa).

**5** Giải thích **quy tắc tổng (sum rule)** của xác suất có điều kiện:
Xác suất $(Y = y_j) =$ tổng trên tất cả các kết quả $x_i$ của Xác suất $(Y = y_j | X = x_i)$.
**6** Ma trận $n \times n$ $P$ chứa **các xác suất đồng thời (joint probabilities)** $p_{ij} = \text{Xác suất } (X = x_i \text{ và } Y = y_j)$. Giải thích tại sao Xác suất có điều kiện $(Y = y_j | X = x_i)$ lại bằng $\frac{p_{ij}}{p_{i1} + \cdots + p_{in}} = \frac{p_{ij}}{p_i}$.
**7** Đối với ma trận xác suất đồng thời này với Xác suất $(x_1, y_2) = 0.3$, hãy tìm Xác suất $(y_2 | x_1)$ và Xác suất $(x_1)$.
| $P = \begin{bmatrix} p_{11} & p_{12} \\ p_{21} & p_{22} \end{bmatrix} = \begin{bmatrix} 0.1 & 0.3 \\ 0.2 & 0.4 \end{bmatrix}$ | Các phần tử $p_{ij}$ có tổng bằng 1.<br>Một vài $i, j$ nào đó phải xảy ra. |
|-------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|

**8** Giải thích **quy tắc tích (product rule)** của xác suất có điều kiện: $p_{ij} = \text{Xác suất } (X = x_i \text{ và } Y = y_j)$ bằng Xác suất $(Y = y_j | X = x_i)$ nhân với Xác suất $(X = x_i)$.
**9** Rút ra **Định lý Bayes (Bayes Theorem)** này cho $p_{ij}$ từ quy tắc tích trong Bài 8:
| Xác suất ( $Y = y_j$ <b>và</b> $X = x_i$ ) | $\frac{\text{Xác suất}(X = x_i | Y = y_j) \text{Xác suất}(Y = y_j)}{\text{Xác suất}(X = x_i)}$ |
|-----------------------------------------|------------------------------------------------------------------------------------|

Những người theo "thuyết Bayes (Bayesians)" sử dụng thông tin từ trước (prior information). Những người theo "thuyết Tần suất (Frequentists)" chỉ sử dụng thông tin lấy mẫu (sampling information).

# **12.3 Gaussian Đa biến và Bình phương Tối thiểu Có trọng số (Multivariate Gaussian and Weighted Least Squares)**

Mật độ xác suất chuẩn $p(x)$ (Gaussian) chỉ phụ thuộc vào hai con số:
| Giá trị trung bình $m$ và phương sai $\sigma^2$ | $p(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-(x-m)^2/2\sigma^2}$ | (1) |
|----------------------------------|-------------------------------------------------------------|-----|

Đồ thị của $p(x)$ là một đường cong hình chuông có tâm tại $x = m$. Biến liên tục $x$ có thể nằm ở bất kỳ đâu trong khoảng từ $-\infty$ đến $\infty$. Với xác suất gần bằng $\frac{2}{3}$, giá trị $x$ ngẫu nhiên đó sẽ nằm giữa $m - \sigma$ và $m + \sigma$ (cách giá trị trung bình $m$ nhỏ hơn một độ lệch chuẩn $\sigma$).
$$\int_{-\infty}^{\infty} p(x) dx = 1 \quad \text{và} \quad \int_{m-\sigma}^{m+\sigma} p(x) dx = \frac{1}{\sqrt{2\pi}} \int_{-1}^1 e^{-X^2/2} dX \approx \frac{2}{3}. \quad (2)$$

Tích phân đó có sự đổi biến từ $x$ thành $X = (x - m)/\sigma$. Điều này làm đơn giản hóa số mũ thành $-X^2/2$ và đơn giản hóa các giới hạn của tích phân thành $-1$ và $1$. Thậm chí hệ số $1/\sigma$ từ $p$ cũng biến mất bên ngoài tích phân vì $dX$ bằng $dx/\sigma$. Mọi Gaussian đều biến thành một **Gaussian chuẩn (standard Gaussian)** $p(X)$ với trung bình $m = 0$ và phương sai $\sigma^2 = 1$. Hãy gọi nó là $p(x)$:
| Phân phối chuẩn tắc $N(0, 1)$ | có | $p(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ | (3) |
|--------------------------------------------|-----|-------------------------------------------|-----|

Lấy tích phân $p(x)$ từ $-\infty$ đến $x$ mang lại phân phối tích lũy $F(x)$: xác suất để một mẫu ngẫu nhiên nằm dưới $x$. Xác suất đó sẽ là $F = \frac{1}{2}$ tại $x = 0$ (giá trị trung bình).

#### **Gaussians Hai chiều (Two-dimensional Gaussians)**

Bây giờ chúng ta có $M = 2$ biến ngẫu nhiên Gaussian $x$ và $y$. Chúng có giá trị trung bình là $m_1$ và $m_2$. Chúng có phương sai là $\sigma_1^2$ và $\sigma_2^2$. Nếu chúng *độc lập*, thì mật độ xác suất của chúng $p(x, y)$ chỉ là $p_1(x)$ **nhân với** $p_2(y)$. Nhân các xác suất khi các biến là độc lập:
| $x$ và $y$ độc lập | $p(x, y) = \frac{1}{2\pi\sigma_1\sigma_2} e^{-(x-m_1)^2/2\sigma_1^2} e^{-(y-m_2)^2/2\sigma_2^2}$ |
|-------------------------|--------------------------------------------------------------------------------------------------|

Hiệp phương sai của $x$ và $y$ sẽ là $\sigma_{12} = 0$. Ma trận hiệp phương sai $V$ sẽ là ma trận *đường chéo*. Các phương sai $\sigma_1^2$ và $\sigma_2^2$ luôn nằm trên đường chéo chính của $V$. Số mũ trong $p(x, y)$ chỉ là tổng của số mũ $x$ và số mũ $y$. Thật tốt khi nhận thấy rằng hai số mũ đó có thể được kết hợp thành $-\frac{1}{2}(x - m)^T V^{-1}(x - m)$ với $V^{-1}$ ở giữa:
$$-\frac{(x-m_1)^2}{2\sigma_1^2} - \frac{(y-m_2)^2}{2\sigma_2^2} = -\frac{1}{2} \begin{bmatrix} x-m_1 & y-m_2 \end{bmatrix} \begin{bmatrix} \sigma_1^2 & 0 \\ 0 & \sigma_2^2 \end{bmatrix}^{-1} \begin{bmatrix} x-m_1 \\ y-m_2 \end{bmatrix} \quad (5)$$

# **$x$ và $y$ Không Độc lập (Non-independent $x$ and $y$)**

Chúng ta đã sẵn sàng để từ bỏ tính độc lập. Số mũ (5) chứa $V^{-1}$ vẫn đúng khi $V$ không còn là ma trận đường chéo nữa. **Bây giờ Gaussian phụ thuộc vào một vectơ $m$ và một ma trận $V$.**

Khi $M = 2$, biến thứ nhất $x$ có thể cung cấp thông tin một phần về biến thứ hai $y$ (và ngược lại). Có lẽ một phần của $y$ được quyết định bởi $x$ và một phần là hoàn toàn độc lập. Chính ma trận hiệp phương sai $M \times M$ $V$ đã tính đến sự phụ thuộc lẫn nhau giữa $M$ biến $x = x_1, \dots, x_M$. Ma trận nghịch đảo $V^{-1}$ của nó đi vào $p(x)$:
| Phân phối xác suất Gaussian đa biến (Multivariate Gaussian probability distribution) | $p(x) = \frac{1}{(\sqrt{2\pi})^M \sqrt{\det V}} e^{-(x-m)^T V^{-1}(x-m)/2} \quad (6)$ |
|------------------------------------------------|---------------------------------------------------------------------------------------|

Các vectơ $x = (x_1, \dots, x_M)$ và $m = (m_1, \dots, m_M)$ chứa các biến ngẫu nhiên và giá trị trung bình của chúng. $M$ căn bậc hai của $2\pi$ và định thức của $V$ được bao gồm để làm cho tổng xác suất bằng 1. Hãy để tôi kiểm tra điều đó bằng đại số tuyến tính. Tôi sử dụng các trị riêng $\Lambda$ và các vectơ riêng trực chuẩn $Q$ của ma trận đối xứng $V = Q \Lambda Q^T$. Do đó **$V^{-1}$** $= Q \Lambda^{-1} Q^T$:
$$X = x - m \quad (x - m)^T V^{-1}(x - m) = X^T Q \Lambda^{-1} Q^T X = Y^T \Lambda^{-1} Y$$

*Chú ý!* Các tổ hợp $Y = Q^T X = Q^T (x - m)$ là độc lập về mặt thống kê. *Ma trận hiệp phương sai $\Lambda$ của chúng là ma trận đường chéo.*

Bước chéo hóa $V$ bằng ma trận vectơ riêng $Q$ của nó cũng giống như việc "khử tương quan (uncorrelating)" các biến ngẫu nhiên. Các hiệp phương sai bằng không đối với các biến mới $Y_1, \dots, Y_M$. Đây là điểm mà đại số tuyến tính giúp giải tích tính toán các tích phân đa chiều.

Tích phân của $p(x)$ không bị thay đổi khi chúng ta đưa biến $x$ về trung tâm bằng cách trừ đi $m$ để thu được $X$, và quay biến đó để thu được $Y = Q^T X$. Ma trận $\mathbf{\Lambda}$ là ma trận đường chéo! Do đó tích phân mà chúng ta muốn sẽ tách thành $M$ tích phân một chiều riêng biệt mà chúng ta đã biết:
$$\begin{aligned} \int \dots \int e^{-Y^T \Lambda^{-1} Y / 2} dY &= \left( \int_{-\infty}^{\infty} e^{-y_1^2/2\lambda_1} dy_1 \right) \dots \left( \int_{-\infty}^{\infty} e^{-y_M^2/2\lambda_M} dy_M \right) \\ &= \left( \sqrt{2\pi\lambda_1} \right) \dots \left( \sqrt{2\pi\lambda_M} \right) = \left( \sqrt{2\pi} \right)^M \sqrt{\det V}. \end{aligned} \quad (7)$$

Định thức của $V$ (cũng là định thức của $\Lambda$) là tích số $(\lambda_1) \dots (\lambda_M)$ của các trị riêng. Khi đó (7) mang lại con số chính xác để đem chia sao cho $p(x_1, \dots, x_M)$ trong phương trình (6) có tích phân $= 1$ như mong muốn.

Giá trị trung bình và phương sai của $p(x)$ cũng là các tích phân $M$ chiều. Cùng một ý tưởng về việc chéo hóa $V$ bằng các vectơ riêng của nó và việc đưa vào $Y = Q^T X$ sẽ tìm ra được các tích phân đó:
| Vectơ các giá trị trung bình $m$ | $\int \dots \int x p(x) dx = (m_1, m_2, \dots) = m$ | (8) |
|---------------------|-----------------------------------------------------|-----|
| Ma trận hiệp phương sai $V$ | $\int \dots \int (x - m) p(x)(x - m)^T dx = V$. | (9) |

Kết luận: Công thức (6) cho mật độ xác suất $p(x)$ có tất cả các tính chất mà chúng ta mong muốn.

# **Bình phương Tối thiểu Có trọng số (Weighted Least Squares)**

Trong Chương 4, bình phương tối thiểu bắt đầu từ một hệ không thể giải được $Ax = b$. Chúng ta đã chọn $x$ để cực tiểu hóa sai số $\|b - Ax\|^2$. Điều đó dẫn chúng ta đến phương trình bình phương tối thiểu $A^TA\hat{x} = A^Tb$. Giá trị $A\hat{x}$ tốt nhất là hình chiếu của $b$ lên không gian cột của $A$. Nhưng bình phương khoảng cách $E = \|b - Ax\|^2$ này có phải là thước đo sai số đúng đắn cần cực tiểu hóa không?

Nếu các sai số đo lường trong $b$ là các biến ngẫu nhiên độc lập, với giá trị trung bình $m = 0$ và phương sai $\sigma^2 = 1$ và một phân phối chuẩn, Gauss sẽ nói **có:** *Sử dụng bình phương tối thiểu.* Nếu các sai số không độc lập hoặc các phương sai của chúng không bằng nhau. Gauss sẽ nói **không**: *Sử dụng bình phương tối thiểu có trọng số.* Phần này sẽ cho thấy rằng thước đo sai số tốt là $E = (b - Ax)^T V^{-1}(b - Ax)$. Phương trình cho $x$ tốt nhất sử dụng ma trận hiệp phương sai $V$:
| Bình phương tối thiểu có trọng số | $A^T V^{-1} A \hat{x} = A^T V^{-1} b$ | (10) |
|------------------------|---------------------------------------|------|

Các ví dụ quan trọng nhất có $m$ sai số *độc lập* trong $b$. Các sai số đó có phương sai $\sigma_1^2, \dots, \sigma_m^2$. Nhờ tính độc lập, $V$ là một ma trận đường chéo. Các trọng số tốt $1/\sigma_1^2, \dots, 1/\sigma_m^2$ đến từ $V^{-1}$. *Chúng ta đang gắn trọng số cho các sai số trong $b$ để có **phương sai** = **1**:*
| Bình phương tối thiểu có trọng số  | Thu nhỏ tối đa | $E = \sum_{i=1}^m \frac{(b - Ax)_i^2}{\sigma_i^2}$ | (11) |
|------------------------------------|----------|-------------------------------------------------------------|------|
| Các sai số độc lập trong $b$ |          |                                                             |      |

Bằng cách tính trọng số cho các sai số, chúng ta đang "làm trắng (whitening)" nhiễu. **Nhiễu trắng (White noise)** là một mô tả nhanh gọn về các sai số độc lập dựa trên phân phối Gaussian chuẩn $\mathbf{N}(0, 1)$ có giá trị trung bình bằng 0 và $\sigma^2 = 1$.

Hãy để tôi viết ra các bước dẫn đến các phương trình (10) và (11) đối với $\hat{x}$ tốt nhất:
Bắt đầu với $Ax = b$ ($m$ phương trình, $n$ ẩn số, $m > n$, vô nghiệm)
Mỗi vế phải $b_i$ có trung bình bằng không và phương sai $\sigma_i^2$. Các $b_i$ là độc lập.
Chia phương trình thứ $i$ cho $\sigma_i$ để có phương sai = 1 cho mọi $b_i/\sigma_i$
Phép chia đó biến $Ax = b$ thành $V^{-1/2}Ax = V^{-1/2}b$ với $V^{-1/2} = \text{diag}(1/\sigma_1, \dots, 1/\sigma_m)$
Bình phương tối thiểu thông thường trên các phương trình có trọng số đó sẽ có $A \rightarrow V^{-1/2}A$ và $b \rightarrow V^{-1/2}b$
| $(V^{-1/2}A)^T(V^{-1/2}A)\hat{x} = (V^{-1/2}A)^TV^{-1/2}b$ | là | $A^TV^{-1}A\hat{x} = A^TV^{-1}b$ | (12) |
|------------------------------------------------------------|----|----------------------------------|------|

Vì $1/\sigma^2$ nằm trong $V^{-1}$, các phương trình đáng tin cậy hơn ($\sigma$ *nhỏ hơn*) nhận được trọng số nặng hơn. Đây là điểm mấu chốt của phương pháp bình phương tối thiểu có trọng số.

Những cách gắn trọng số trên đường chéo đó (các phương trình không liên kết) là phổ biến nhất và đơn giản nhất. Chúng áp dụng cho các *sai số độc lập trong $b_i$*. Khi các sai số đo lường này không độc lập, $V$ không còn là ma trận đường chéo nữa — nhưng (12) vẫn là phương trình có trọng số đúng đắn.

Trong thực tế, việc tìm kiếm tất cả các hiệp phương sai có thể là một công việc nghiêm túc. $V$ đường chéo thì đơn giản hơn.

#### **Phương sai trong Ước lượng $\hat{x}$ (The Variance in the Estimated $\hat{x}$)**

Một điểm nữa: Thường thì câu hỏi quan trọng không phải là $x$ tốt nhất đối với một tập hợp các phép đo $b$ cụ thể. Đây chỉ là một mẫu! Mục tiêu thực sự là biết được độ tin cậy của toàn bộ thử nghiệm. Điều đó được đo lường (như độ tin cậy luôn được đo lường) bằng **phương sai trong ước lượng** $\hat{x}$. Đầu tiên, giá trị trung bình bằng 0 trong $b$ mang lại giá trị trung bình bằng 0 trong $\hat{x}$. Sau đó công thức kết nối phương sai $V$ ở các đầu vào $b$ với phương sai $W$ ở các đầu ra $\hat{x}$ hóa ra lại rất đẹp:
| Ma trận phương sai - hiệp phương sai $W$ cho $\hat{x}$ | $\mathbb{E}[(\hat{x} - x)(\hat{x} - x)^T] = (A^T V^{-1} A)^{-1}$ | (13) |
|----------------------------------------------|---------------------------------------------------------|------|

Phương sai nhỏ nhất có thể có đó đến từ cách tính trọng số tốt nhất có thể, đó là $V^{-1}$.

Công thức cốt lõi này là một ứng dụng hoàn hảo của Phần 12.2. Nếu $b$ **có ma trận hiệp phương sai** $V$, **thì** $x = Lb$ **có ma trận hiệp phương sai** $L V L^T$. Phương trình (12) ở trên cho chúng ta biết rằng $L$ là $(A^T V^{-1} A)^{-1} A^T V^{-1}$. Bây giờ hãy thế cái này vào $L V L^T$ và quan sát phương trình (13) xuất hiện:
$$L V L^T = (A^T V^{-1} A)^{-1} A^T V^{-1} \quad V \quad V^{-1} A (A^T V^{-1} A)^{-1} = (A^T V^{-1} A)^{-1}.$$

Đây là hiệp phương sai $W$ của đầu ra, ước lượng tốt nhất $\hat{x}$ của chúng ta. Đã đến lúc đưa ra các ví dụ.

**Ví dụ 1** Giả sử một bác sĩ đo nhịp tim $x$ của bạn ba lần ($m = 3, n = 1$):
| $x = b_1$ | là | $Ax = b$ | với | $A = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$ | và | $V = \begin{bmatrix} \sigma_1^2 & 0 & 0 \\ 0 & \sigma_2^2 & 0 \\ 0 & 0 & \sigma_3^2 \end{bmatrix}$ |
|-----------|----|----------|------|-------------------------------------------------|-----|----------------------------------------------------------------------------------------------------|
| $x = b_2$ |    |          |      |                                                 |     |                                                                                                    |
| $x = b_3$ |    |          |      |                                                 |     |                                                                                                    |

Các phương sai có thể là $\sigma_1^2 = 1/9$ và $\sigma_2^2 = 1/4$ và $\sigma_3^2 = 1$. Bạn ngày càng lo lắng khi các phép đo được thực hiện: $b_3$ kém tin cậy hơn $b_2$ và $b_1$. Tất cả ba phép đo đều chứa một số thông tin, vì vậy tất cả chúng đều đi vào ước lượng tốt nhất (có trọng số) $\hat{x}$:
$$V^{-1/2} A \hat{x} = V^{-1/2} b \quad \text{là} \quad \begin{aligned} 3x &= 3b_1 \\ 2x &= 2b_2 \\ 1x &= 1b_3 \end{aligned} \quad \text{dẫn đến} \quad A^T V^{-1} A \hat{x} = A^T V^{-1} b$$

$$\begin{bmatrix} 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} 9 & & \\ & 4 & \\ & & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} \hat{x} = \begin{bmatrix} 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} 9 & & \\ & 4 & \\ & & 1 \end{bmatrix} \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}$$

$$\hat{x} = \frac{9b_1 + 4b_2 + b_3}{14} \quad \text{là trung bình có trọng số của } b_1, b_2, b_3$$

Trọng số lớn nhất nằm ở $b_1$ vì phương sai $\sigma_1^2$ của nó là nhỏ nhất. Phương sai của $\hat{x}$ có công thức tuyệt đẹp $W = (A^T V^{-1} A)^{-1} = 1/14$:
| Phương sai của $\hat{x}$ | $\left( \begin{bmatrix} 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} 9 & & \\ & 4 & \\ & & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} \right)^{-1} = \frac{1}{14}$ nhỏ hơn $\frac{1}{9}$ |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Định lý BLUE của Gauss (được chứng minh trên trang web) nói rằng $\hat{x} = Lb$ của chúng ta là ước lượng tuyến tính không chệch tốt nhất (best linear unbiased estimate - BLUE) cho nghiệm của $Ax = b$. Bất kỳ lựa chọn không chệch nào khác $x^* = L^* b$ đều có phương sai lớn hơn $\hat{x}$. Tất cả các lựa chọn không chệch đều có $L^* A = I$ sao cho một $Ax = b$ chính xác sẽ tạo ra câu trả lời đúng $x = L^* b = L^* A x$.

*Lưu ý.* Tôi phải thêm vào rằng có những lý do để không cực tiểu hóa bình phương sai số ngay từ đầu. Một lý do: Giá trị $x$ này thường có nhiều thành phần nhỏ. Bình phương của các số nhỏ là rất nhỏ, và chúng xuất hiện khi chúng ta cực tiểu hóa. Sẽ dễ hiểu hơn với các vectơ *thưa (sparse)* — chỉ có một vài phần tử khác không. Các nhà thống kê thường thích cực tiểu hóa **các sai số không bình phương: tổng của** $|(b - Ax)_i|$. *Thước đo sai số này là* $\ell_1$ *thay vì* $\ell_2$. Do các giá trị tuyệt đối, phương trình cho $x$ trở nên phi tuyến tính (thực chất nó là tuyến tính từng khúc).

Các thuật toán mới và nhanh đang tính toán một $x$ thưa một cách nhanh chóng và tương lai có thể thuộc về $\ell_1$.

#### **Bộ lọc Kalman (The Kalman Filter)**

"Bộ lọc Kalman" là thuật toán tuyệt vời trong bình phương tối thiểu động (dynamic least squares). Từ *động (dynamic)* đó có nghĩa là các phép đo mới $b_k$ liên tục xuất hiện. Vì vậy, ước lượng tốt nhất $\hat{x}_k$ liên tục thay đổi (dựa trên tất cả các giá trị từ $b_0, \dots, b_k$). Hơn thế nữa, ma trận $A$ cũng đang thay đổi. Do đó $\hat{x}_2$ sẽ là ước lượng bình phương tối thiểu tốt nhất của chúng ta đối với nghiệm mới nhất $x_2$ cho **toàn bộ lịch sử của các phương trình quan sát và các phương trình cập nhật (phương trình trạng thái - state equations) cho đến thời điểm 2:**
| $A_0x_0 = b_0$ | $x_1 = F_0x_0$ | $A_1x_1 = b_1$ | $x_2 = F_1x_1$ | $A_2x_2 = b_2$ | (14) |
|----------------|----------------|----------------|----------------|----------------|------|

Ý tưởng Kalman là đưa vào từng phương trình một. Sẽ có những sai số trong mỗi phương trình. Với mỗi phương trình mới, chúng ta cập nhật ước lượng tốt nhất $\hat{x}_k$ cho giá trị $x_k$ hiện tại. Nhưng lịch sử không bị lãng quên! Ước lượng $\hat{x}_k$ mới này sử dụng tất cả các quan sát trong quá khứ $b_0$ đến $b_{k-1}$ và tất cả các phương trình trạng thái $x_{\text{new}} = F_{\text{old}} x_{\text{old}}$. Một bài toán bình phương tối thiểu lớn và đang phát triển.

Thêm một điểm quan trọng nữa. Mỗi phương trình bình phương tối thiểu được **gắn trọng số** bằng cách sử dụng ma trận hiệp phương sai $V_k$ cho sai số trong $b_k$. Thậm chí còn có một ma trận hiệp phương sai $C_k$ cho các sai số trong các phương trình cập nhật $x_{k+1} = F_k x_k$. Giá trị $\hat{x}_2$ tốt nhất khi đó phụ thuộc vào $b_0, b_1, b_2$ và $V_0, V_1, V_2$ cùng với $C_1, C_2$. Cách tốt để viết $\hat{x}_k$ là dưới dạng một bản cập nhật cho $\hat{x}_{k-1}$ trước đó.

Cho phép tôi tập trung vào một bài toán đơn giản hóa, không có các ma trận $F_k$ và các hiệp phương sai $C_k$. Chúng ta đang ước lượng cùng một giá trị $x$ thực tại mỗi bước. Làm thế nào để chúng ta có được $\hat{x}_1$ từ $\hat{x}_0$?

**CŨ** 
$$A_0 x_0 = b_0$$
 dẫn đến phương trình có trọng số $A_0^T V_0^{-1} A_0 \hat{x}_0 = A_0^T V_0^{-1} b_0$. (15)

**MỚI** 
$$\begin{bmatrix} A_0 \\ A_1 \end{bmatrix} \hat{x}_1 = \begin{bmatrix} b_0 \\ b_1 \end{bmatrix}$$
 dẫn đến phương trình có trọng số sau đây cho $\hat{x}_1$:
| $\begin{bmatrix} A_0^T & A_1^T \end{bmatrix} \begin{bmatrix} V_0^{-1} & 0 \\ 0 & V_1^{-1} \end{bmatrix} \begin{bmatrix} A_0 \\ A_1 \end{bmatrix} \hat{x}_1 = \begin{bmatrix} A_0^T & A_1^T \end{bmatrix} \begin{bmatrix} V_0^{-1} & 0 \\ 0 & V_1^{-1} \end{bmatrix} \begin{bmatrix} b_0 \\ b_1 \end{bmatrix}. \quad (16)$ |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Đúng vậy, chúng ta có thể chỉ cần giải quyết bài toán mới đó và quên đi bài toán cũ. Nhưng nghiệm cũ $\hat{x}_0$ cần công việc mà chúng ta hy vọng sẽ tái sử dụng trong $\hat{x}_1$. Điều chúng ta tìm kiếm là **một sự cập nhật (update) đối với $\hat{x}_0$**:
| Cập nhật Kalman mang lại $\hat{x}_1$ từ $\hat{x}_0$ | $\hat{x}_1 = \hat{x}_0 + K(b_1 - A_1 \hat{x}_0)$ | (17) |
|--------------------------------------------------|-----------------------------------------------------------|------|

Sự sửa lỗi cập nhật là sự sai lệch $b_1 - A_1\hat{x}_0$ giữa trạng thái cũ $\hat{x}_0$ và các phép đo mới $b_1$ — nhân với *ma trận khuếch đại Kalman (Kalman gain matrix)* $K_1$. Công thức cho $K_1$ đến từ việc so sánh các nghiệm $\hat{x}_1$ và $\hat{x}_0$ với (15) và (16). Và khi chúng ta cập nhật $\hat{x}_0$ thành $\hat{x}_1$ dựa trên dữ liệu mới **$b_1$, chúng ta cũng cập nhật ma trận hiệp phương sai $W_0$ thành $W_1$.** Hãy nhớ $W_0 = (A_0^T V_0^{-1} A_0)^{-1}$ từ phương trình (13). Cập nhật ma trận nghịch đảo của nó thành $W_1^{-1}$:
| Hiệp phương sai $W_1$ của các sai số trong $\hat{x}_1$ | $W_1^{-1} = W_0^{-1} + A_1^T V_1^{-1} A_1$ | (18) |
|-------------------------------------------|-----------------------------------------------|------|

| Ma trận khuếch đại Kalman $K_1$ | $K_1 = W_1 A_1^T V_1^{-1}$ | (19) |
|--------------------------|-------------------------------|------|

Đây là trung tâm của bộ lọc Kalman. Hãy chú ý đến tầm quan trọng của các $W_k$. Các ma trận đó đo lường độ tin cậy của toàn bộ quá trình, trong đó vectơ $\hat{x}_k$ ước lượng trạng thái hiện tại dựa trên các phép đo cụ thể từ $b_0$ đến $b_k$.

Cả những chương sách và những cuốn sách hoàn chỉnh đã được viết để giải thích bộ lọc Kalman động (dynamic Kalman filter), khi các trạng thái $x_k$ cũng đang thay đổi (dựa trên các ma trận $F_k$). Có một sự *dự đoán (prediction)* của $x_k$ sử dụng $F$, theo sau là một sự *sửa lỗi (correction)* sử dụng dữ liệu mới $b$. Có lẽ tốt nhất là dừng lại ở đây.

Trang này nói về **bình phương tối thiểu đệ quy (recursive least squares):** thêm dữ liệu mới $b_k$ và cập nhật cả $\hat{x}$ và $W$: ước lượng hiện tại tốt nhất dựa trên tất cả dữ liệu, và ma trận hiệp phương sai của nó.

### **Tập bài tập 12.3 (Problem Set 12.3)**

**1** Hai phép đo của cùng một biến $x$ đưa ra hai phương trình $x = b_1$ và $x = b_2$. Giả sử các giá trị trung bình bằng 0 và các phương sai là $\sigma_1^2$ và $\sigma_2^2$, với các sai số độc lập: $V$ là ma trận đường chéo với các phần tử $\sigma_1^2$ và $\sigma_2^2$. Viết hai phương trình dưới dạng $Ax = b$ ($A$ là ma trận $2 \times 1$). Giống như trong Ví dụ 1 của tài liệu, hãy tìm ước lượng tốt nhất $\hat{x}$ này dựa trên $b_1$ và $b_2$:
$$\hat{x} = \frac{b_1/\sigma_1^2 + b_2/\sigma_2^2}{1/\sigma_1^2 + 1/\sigma_2^2} \quad \mathbb{E} \left[ (\hat{x}-x)(\hat{x}-x)^T \right] = \left( \frac{1}{\sigma_1^2} + \frac{1}{\sigma_2^2} \right)^{-1}.$$
**2** (a) Trong Bài 1, giả sử phép đo thứ hai $b_2$ trở nên cực kỳ chính xác và phương sai $\sigma_2^2 \rightarrow 0$ của nó. Ước lượng $\hat{x}$ tốt nhất là gì khi $\sigma_2$ tiến đến 0?
(b) Trường hợp ngược lại có $\sigma_2^2 \rightarrow \infty$ và không có thông tin trong $b_2$. Bây giờ đâu là ước lượng tốt nhất $\hat{x}$ dựa trên $b_1$ và $b_2$?
**3** Nếu $x$ và $y$ độc lập với các xác suất $p_1(x)$ và $p_2(y)$, thì $p(x, y) = p_1(x)p_2(y)$. Bằng cách tách các tích phân kép thành tích của các tích phân đơn (từ $-\infty$ đến $\infty$), hãy chỉ ra rằng
$$\iint p(x, y) dx dy = 1 \quad \text{và} \quad \iint (x + y) p(x, y) dx dy = m_1 + m_2.$$
**4** Tiếp tục Bài 3 đối với $x, y$ độc lập để chỉ ra rằng $p(x, y) = p_1(x)p_2(y)$ có
$$\iint (x - m_1)^2 p(x, y) dx dy = \sigma_1^2 \quad \iint (x - m_1)(y - m_2) p(x, y) dx dy = 0.$$
Vì vậy ma trận hiệp phương sai $2 \times 2$ $V$ là ma trận đường chéo và các phần tử của nó là \_\_\_\_\_\_.
**5** Chỉ ra rằng ma trận nghịch đảo của một ma trận hiệp phương sai $2 \times 2$ $V$ là
$$V^{-1} = \begin{bmatrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{bmatrix}^{-1} = \frac{1}{1 - \rho^2} \begin{bmatrix} 1/\sigma_1^2 & -\rho/\sigma_1\sigma_2 \\ -\rho/\sigma_1\sigma_2 & 1/\sigma_2^2 \end{bmatrix} \quad \text{với tương quan (correlation)} \quad \rho = \frac{\sigma_{12}}{\sigma_1\sigma_2}.$$
Điều này tạo ra số mũ $-(x - m)^T V^{-1}(x - m)/2$ trong một Gaussian 2 biến.
**6** Giả sử $\hat{x}_k$ là giá trị trung bình của $b_1, \dots, b_k$. Một phép đo mới $b_{k+1}$ đến và chúng ta muốn giá trị trung bình mới $\hat{x}_{k+1}$. Phương trình cập nhật Kalman (17) là
$$\text{Trung bình mới} \quad \hat{x}_{k+1} = \hat{x}_k + \frac{1}{k+1} (b_{k+1} - \hat{x}_k).$$
Xác minh rằng $\hat{x}_{k+1}$ là giá trị trung bình chính xác của $b_1, \dots, b_{k+1}$.
**7** Cũng kiểm tra phương trình cập nhật (18) cho phương sai $W_{k+1} = \sigma^2/(k+1)$ của giá trị trung bình $\hat{x}$ này, giả sử rằng $W_k = \sigma^2/k$ và $b_{k+1}$ có phương sai $V = \sigma^2$.
**8** (**Mô hình tĩnh (Steady model)**) Các bài toán 6-7 là bình phương tối thiểu *tĩnh (static)*. Tất cả các giá trị trung bình mẫu $\hat{x}_k$ đều là ước lượng của cùng một $x$. Để biến bộ lọc Kalman thành *động (dynamic)*, cũng bao gồm một *phương trình trạng thái (state equation)* $x_{k+1} = Fx_k$ với phương sai sai số của riêng nó là $s^2$. Bài toán bình phương tối thiểu động cho phép $x$ "trôi dạt (drift)" khi $k$ tăng lên:
$$\begin{bmatrix} 1 & \\ -F & 1 \end{bmatrix} \begin{bmatrix} x_0 \\ x_1 \end{bmatrix} = \begin{bmatrix} b_0 \\ 0 \\ b_1 \end{bmatrix} \quad \text{với các phương sai} \quad \begin{bmatrix} \sigma^2 \\ s^2 \\ \sigma^2 \end{bmatrix}.$$
Với $F = 1$, hãy chia cả hai vế của ba phương trình đó cho $\sigma, s$, và $\sigma$. Tìm $\hat{x}_0$ và $\hat{x}_1$ bằng bình phương tối thiểu, điều này sẽ mang lại nhiều trọng số hơn cho $b_1$ gần đây. Bộ lọc Kalman được phát triển trong cuốn *Algorithms for Global Positioning* (Borre và Strang, Wellesley-Cambridge Press).

# **Sự Thay đổi trong $A^{-1}$ từ một Sự Thay đổi trong $A$ (Change in $A^{-1}$ from a Change in $A$)**

Trang cuối cùng này kết nối phần đầu của cuốn sách (các ma trận nghịch đảo và các ma trận hạng 1) với phần cuối của cuốn sách (bình phương tối thiểu động và các bộ lọc). Bắt đầu với công thức cơ bản này:
| Ma trận nghịch đảo của $M = I - uv^T$ là $M^{-1} = I + \frac{uv^T}{1 - v^Tu}$ |
|------------------------------------------------------------------------|

Phép chứng minh nhanh nhất là $M M^{-1} = I - uv^T + \frac{uv^T - (uv^T)(uv^T)}{1 - v^Tu} = I - uv^T + \frac{u(1 - v^Tu)v^T}{1 - v^Tu} = I$.
$M$ không thể nghịch đảo nếu $v^Tu = 1$ (khi đó $Mu = 0$). Ở đây $v^T = u^T = \begin{bmatrix} 1 & 1 & 1 \end{bmatrix}$:
**Ví dụ** Ma trận nghịch đảo của
$$M = I - \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} \begin{bmatrix} 1 & 1 & 1 \end{bmatrix} = I - \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$$
 là $M^{-1} = I + \frac{1}{1 - 3} \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$.

Nhưng chúng ta không phải lúc nào cũng bắt đầu từ ma trận đơn vị. Nhiều ứng dụng cần phải nghịch đảo $M = A - uv^T$. Sau khi chúng ta giải $Ax = b$, chúng ta kỳ vọng một sự thay đổi hạng 1 (rank one change) để giải ra được $My = b$. Phép chia cho $1 - v^Tu$ ở trên sẽ trở thành phép chia cho $c = 1 - v^T A^{-1} u = 1 - v^T z$.

**Bước 1** Giải $Az = u$ và tính $c = 1 - v^T z$.
**Bước 2** Nếu $c \neq 0$ thì $y = M^{-1} b$ là $y = x + \frac{v^T x}{c} z$.

Giả sử $A$ rất dễ làm việc cùng. $A$ có thể đã được phân tích thành $LU$ nhờ phép khử. Khi đó công thức Sherman-Woodbury-Morrison này là cách nhanh chóng để giải $My = b$. Dưới đây là ba bài toán để kết thúc cuốn sách!

**9** Thực hiện các Bước 1-2 để tìm $y$ khi $A = I$ và $u^T = v^T = \begin{bmatrix} 1 & 2 & 3 \end{bmatrix}$ và $b^T = \begin{bmatrix} 2 & 1 & 4 \end{bmatrix}$.
**10** Bước 2 trong "công thức cập nhật (update formula)" này tuyên bố rằng $M y = (A - uv^T) \left(x + \frac{v^Tx}{c}z\right) = b$. Hãy đơn giản hóa điều này thành $\frac{uv^Tx}{c} [c - 1 + v^T z] = 0$. Điều này đúng vì $c = 1 - v^T z$.
**11** Khi $A$ có một hàng mới $v^T$, $A^TA$ trong phương trình bình phương tối thiểu sẽ thay đổi thành $M$:
$M = \begin{bmatrix} A \\ v^T \end{bmatrix}^T \begin{bmatrix} A \\ v^T \end{bmatrix} = A^TA + vv^T = \text{sự thay đổi hạng 1 (rank one change) trong } A^TA$.
Tại sao phép nhân đó lại đúng? Giá trị $x_{\text{new}}$ được cập nhật đến từ các Bước 1 và 2. Để tham khảo, đây là bốn công thức cho $M^{-1}$. Hai công thức đầu tiên đã được đưa ra ở trên, khi sự thay đổi là $uv^T$. Các công thức 3 và 4 đi xa hơn hạng 1 để cho phép các ma trận $U, V, W$.

$M = I - uv^T$ và $M^{-1} = I + uv^T/(1 - v^Tu)$ (sự thay đổi hạng 1 - rank 1 change)
$M = A - uv^T$ và $M^{-1} = A^{-1} + A^{-1}uv^T A^{-1}/(1 - v^T A^{-1} u)$
$M = I - UV$ và $M^{-1} = I_n + U(I_m - VU)^{-1}V$
$M = A - UW^{-1}V$ và $M^{-1} = A^{-1} + A^{-1}U(W - VA^{-1}U)^{-1} VA^{-1}$

Công thức 4 là "bổ đề nghịch đảo ma trận (matrix inversion lemma)" trong kỹ thuật. Chưa từng được thấy cho đến tận bây giờ! Bộ lọc Kalman cho việc giải các hệ thống khối ba đường chéo (block tridiagonal systems) sử dụng công thức 4 tại mỗi bước.

# PHÂN TÍCH MA TRẬN (MATRIX FACTORIZATIONS)

1. $A = LU = \begin{pmatrix} L \text{ tam giác dưới} & U \text{ tam giác trên} \\ \text{các số 1 trên đường chéo} & \text{các phần tử chốt trên đường chéo} \end{pmatrix}$
**Yêu cầu:** Không có các phép hoán vị hàng (row exchanges) do phép khử Gauss rút gọn ma trận vuông $A$ thành $U$.

2. $A = LDU = \begin{pmatrix} L \text{ tam giác dưới} & \text{ma trận chốt} \\ \text{các số 1 trên đường chéo} & D \text{ là ma trận đường chéo} \end{pmatrix} \begin{pmatrix} U \text{ tam giác trên} \\ \text{các số 1 trên đường chéo} \end{pmatrix}$
**Yêu cầu:** Không có các phép hoán vị hàng. Các phần tử chốt trong $D$ được chia ra để lại các số 1 trên đường chéo của $U$. Nếu $A$ đối xứng thì $U$ là $L^T$ và $A = LDL^T$.

3. $PA = LU$ (ma trận hoán vị (permutation matrix) $P$ để tránh các số không (zeros) ở các vị trí chốt).
**Yêu cầu:** $A$ có thể nghịch đảo. Khi đó $P, L, U$ có thể nghịch đảo. $P$ thực hiện trước tất cả các phép hoán vị hàng trên $A$, để cho phép một $LU$ thông thường. Cách khác: $A = L_1 P_1 U_1$.

4. $EA = R$ (ma trận nghịch đảo $E$ kích thước $m \times m$) (bất kỳ ma trận $A$ kích thước $m \times n$) $= \text{rref}(A)$.
**Yêu cầu:** Không có! *Ma trận dạng bậc thang rút gọn (reduced row echelon form) $R$ có $r$ hàng chốt và cột chốt, chứa ma trận đơn vị. $m - r$ hàng cuối cùng của $E$ là một cơ sở cho không gian null bên trái (left nullspace) của $A$; chúng nhân với $A$ để mang lại $m - r$ hàng chứa các số 0 trong $R$. $r$ cột đầu tiên của $E^{-1}$ là một cơ sở cho không gian cột (column space) của $A$.*

5. $S = C^T C =$ (tam giác dưới) (tam giác trên) với $\sqrt{D}$ trên cả hai đường chéo
**Yêu cầu:** $S$ là ma trận đối xứng và xác định dương (symmetric and positive definite) (tất cả $n$ phần tử chốt trong $D$ đều dương). Phân tích Cholesky (Cholesky factorization) $C = \text{chol}(S)$ này có $C^T = L\sqrt{D}$, do đó $S = C^TC = LDL^T$.

6. $A = QR =$ (các cột trực giao trong $Q$) (tam giác trên $R$).
**Yêu cầu:** $A$ có các cột độc lập tuyến tính. Chúng được trực giao hóa (orthogonalized) trong $Q$ bằng quá trình Gram-Schmidt hoặc quá trình Householder. Nếu $A$ là ma trận vuông thì $Q^{-1} = Q^T$.

7. $A = X \Lambda X^{-1} =$ (các vectơ riêng trong $X$) (các trị riêng trong $\Lambda$) (các vectơ riêng bên trái trong $X^{-1}$).
**Yêu cầu:** $A$ phải có $n$ vectơ riêng độc lập tuyến tính.

8. $S = Q \Lambda Q^T =$ (ma trận trực giao $Q$) (ma trận trị riêng thực $\Lambda$) ($Q^T$ là $Q^{-1}$).
**Yêu cầu:** $S$ là ma trận *thực và đối xứng*: $S^T = S$. Đây là Định lý Phổ (Spectral Theorem).

9. $A = B J B^{-1} =$ (các vectơ riêng tổng quát (generalized eigenvectors) trong $B$) (các khối Jordan (Jordan blocks) trong $J$) ($B^{-1}$).
**Yêu cầu:** $A$ là bất kỳ ma trận vuông nào. Dạng Jordan (Jordan form) $J$ này có một khối cho mỗi vectơ riêng độc lập của $A$. Mỗi khối chỉ có một trị riêng.

10. $A = U \Sigma V^T =$ (trực giao) (ma trận giá trị kỳ dị (singular value matrix) $m \times n$) (trực giao).
$U$ kích thước $m \times m$
$\Sigma$ có $\sigma_1, \dots, \sigma_r$ trên đường chéo
$V$ kích thước $n \times n$
**Yêu cầu:** Không có. Phân tích Giá trị Kỳ dị (Singular Value Decomposition - SVD) này có các vectơ riêng của $AA^T$ nằm trong $U$ và các vectơ riêng của $A^TA$ nằm trong $V$; $\sigma_i = \sqrt{\lambda_i(A^TA)} = \sqrt{\lambda_i(AA^T)}$.
Những giá trị kỳ dị (singular values) đó là $\sigma_1 \geq \sigma_2 \geq \dots \geq \sigma_r > 0$. Bằng phép nhân cột-hàng
$$A = U \Sigma V^T = \sigma_1 u_1 v_1^T + \dots + \sigma_r u_r v_r^T.$$
Nếu $S$ là ma trận đối xứng xác định dương thì $U = V = Q$ và $\Sigma = \Lambda$ và $S = Q \Lambda Q^T$.

11. $A^+ = V \Sigma^+ U^T =$ (trực giao) (ma trận nghịch đảo giả (pseudoinverse) $n \times m$ của $\Sigma$) (trực giao).
$V$ kích thước $n \times n$
$\Sigma^+$ có $1/\sigma_1, \dots, 1/\sigma_r$ trên đường chéo
$U^T$ kích thước $m \times m$
**Yêu cầu:** Không có. Ma trận *nghịch đảo giả (pseudoinverse)* $A^+$ có $A^+A =$ hình chiếu lên không gian hàng của $A$ và $AA^+ =$ hình chiếu lên không gian cột. $A^+ = A^{-1}$ nếu $A$ có thể nghịch đảo. Nghiệm bình phương tối thiểu ngắn nhất cho $Ax = b$ là $x^+ = A^+b$. Nó giải quyết được $A^TAx^+ = A^Tb$.

12. $A = QS =$ (ma trận trực giao $Q$) (ma trận đối xứng xác định dương $S$).
**Yêu cầu:** $A$ có thể nghịch đảo. *Phân tích định dạng cực (polar decomposition)* này có $S^2 = A^TA$. Nhân tử $S$ là bán xác định dương nếu $A$ suy biến. Phân tích định dạng cực đảo $A = K Q$ có $K^2 = AA^T$. Cả hai đều có $Q = U V^T$ từ SVD.

13. $A = U \Lambda U^{-1} = $ (ma trận unita $U$) (ma trận trị riêng $\Lambda$) ($U^{-1}$ là $U^H$).
**Yêu cầu:** $A$ là ma trận *chuẩn (normal)*: $A^HA = AA^H$. Các vectơ riêng trực chuẩn (và có thể là số phức) của nó là các cột của $U$. Các $\lambda$ phức trừ khi $S = S^H$: Trường hợp ma trận Hermitian.

14. $A = Q T Q^{-1} = $ (ma trận unita $Q$) (ma trận tam giác $T$ với $\lambda$ trên đường chéo) ($Q^{-1} = Q^H$).
**Yêu cầu:** *Tam giác hóa Schur (Schur triangularization)* của bất kỳ ma trận vuông $A$ nào. Có một ma trận $Q$ với các cột trực giao làm cho $Q^{-1}AQ$ trở thành ma trận tam giác: Phần 6.4.

15. $F_n = \begin{bmatrix} I & D \\ I & -D \end{bmatrix} \begin{bmatrix} F_{n/2} & \\ & F_{n/2} \end{bmatrix} [\text{hoán vị chẵn-lẻ (even-odd permutation)}]$
= một bước của FFT đệ quy.
**Yêu cầu:** $F_n =$ ma trận Fourier với các phần tử $w^{jk}$ trong đó $w^n = 1$: $F_n \bar{F}_n = nI$. $D$ có $1, w, \dots, w^{n/2 - 1}$ trên đường chéo của nó. Đối với $n = 2^\ell$, *Biến đổi Fourier Nhanh (Fast Fourier Transform - FFT)* sẽ tính $F_n x$ với chỉ $\frac{1}{2} n \ell = \frac{1}{2} n \log_2 n$ phép nhân từ $\ell$ giai đoạn của các ma trận $D$.

# **Chỉ mục Ký hiệu và Mã Máy tính (Index of Symbols and Computer Codes)**

| $A = LDU$, 99 | $(AB)^{-1} = B^{-1}A^{-1}$, 84 | chebfun, 428 |
|---|---|---|
| $A = LU$, 99, 114, 378 | $(AB)C = A(BC)$, 70 | Fortran, 39 |
| $A = QR$, 239, 240, 378 | $\begin{bmatrix} A & b \end{bmatrix}$ và $\begin{bmatrix} A & I \end{bmatrix}$, 149 | Julia, 16, 38, 39 |
| $A = QS$ và $KQ$, 394 | $\det(A - \lambda I) = 0$, 292, 293 | LAPACK, 100, 378, 509, 515, 529 |
| $A = U\Sigma V^T$, 372, 378 | $C(A)$ và $C(A^T)$, 128 | Maple, 38 |
| $A = uv^T$, 140 | $N(A)$ và $N(A^T)$, 135 | Mathematica, 38 |
| $A = BCB^{-1}$, 308 | $\mathbb{C}^n$, 430, 444 | MATLAB, 16, 38, 43, 88, 115, 240, 303 |
| $A = BJB^{-1}$, 422, 423 | $\mathbb{R}^n$, 123, 430 | MINRES, 528 |
| $A = QR$, 239, 513, 530, 532 | $S \cup T$, 134 | Python, 16, 38, 39 |
| $A = QTQ^{-1}$, 343 | $S + T$, 134, 179 | R, 38, 39 |
| $A = X\Lambda X^{-1}$, 304, 310 | $S \cap T$, 133, 179 | |
| $A^k = X\Lambda^k X^{-1}$, 307, 310 | $V^\perp$, 197, 204 | **Tên Mã lệnh (Code Names)** |
| $A^+ = V\Sigma^+ U^T$, 395 | $\mathbf{Z}$, 123, 125, 137, 173 | **amd**, 513 |
| $A^T A$, 112, 203, 212, 372 | $\ell^1$ và $\ell^\infty$, 523 | **chol**, 353 |
| $A^T A \widehat{x} = A^T b$, 219 | $i, j, k$, 13, 169, 280 | **eig**, 293 |
| $A^T C A$, 362, 459, 467 | $u \times v$, 279 | **eigshow**, 303, 380 |
| $P = A(A^T A)^{-1} A^T$, 211 | $x^+ = A^+ b$, 397 | **lu**, 103 |
| $PA = LU$, 114 | $N(0, 1)$, 555 | **norm**, 17, 392, 518 |
| $Q^T Q = I$, 234 | $mod\ p$, 502, 503 | **pascal**, 95 |
| $R = \mathbf{rref}(A)$, 137 | $NaN$, 225 | **plot2d**, 406, 410 |
| $S = A^T A$, 352, 372 | Ma trận $-1, 2, -1$, 259, 368, 523 | **qr**, 241, 246 |
| $S = LDL^T$, 342 | Định thức $3 \times 3$, 271 | **rand**, 370 |
| $S = Q\Lambda Q^T$, 338, 341, 353 | | **rref**, 88, 137 |
| $e^{At}$, 326, 328, 334 | | **svd**, 378 |
| $e^{At} = X e^{At} X^{-1}$, 327 | | **toeplitz**, 108 |
| $(A - \lambda I)x = 0$, 292 | | |
| $(Ax)^T y = x^T (A^T y)$, 111 | | |
| $(AB)^T = B^T A^T$, 110 | | |

### Các Trang web và Địa chỉ Email về Đại số Tuyến tính

[math.mit.edu/linearalgebra](http://math.mit.edu/linearalgebra) Dành cho độc giả và giáo viên làm việc với cuốn sách này
[ocw.mit.edu](http://ocw.mit.edu) Trang web OpenCourseWare của MIT bao gồm các video bài giảng cho 18.06 và 18.085-6
[web.mit.edu/18.06](http://web.mit.edu/18.06) Đề thi và bài tập về nhà hiện tại và quá khứ cùng với các tài liệu bổ sung
[wellesleycambridge.com](http://wellesleycambridge.com) Thông tin đặt hàng cho các cuốn sách của Gilbert Strang
[linearalgebrabook@gmail.com](mailto:linearalgebrabook@gmail.com) Liên hệ email trực tiếp về cuốn sách này


# **Sáu Định lý Lớn của Đại số Tuyến tính (Six Great Theorems of Linear Algebra)**

**Định lý Số chiều (Dimension Theorem)** Mọi cơ sở của một không gian vectơ đều có cùng số lượng vectơ.

**Định lý Đếm (Counting Theorem)** Số chiều của không gian cột + số chiều của không gian null = số lượng cột.

**Định lý Hạng (Rank Theorem)** Số chiều của không gian cột = số chiều của không gian hàng. Đây chính là hạng (rank).

**Định lý Cơ bản (Fundamental Theorem)** Không gian hàng và không gian null của $A$ là các phần bù trực giao trong $\mathbb{R}^n$.

**Định lý Giá trị Kỳ dị (SVD Theorem)** Tồn tại các cơ sở trực chuẩn (các $v$ và các $u$ cho các không gian hàng và cột) sao cho $A v_i = \sigma_i u_i$.

**Định lý Phổ (Spectral Theorem)** Nếu $A^T = A$ thì tồn tại các $q$ trực chuẩn sao cho $A q_i = \lambda_i q_i$ và $A = Q \Lambda Q^T$.

# **ĐẠI SỐ TUYẾN TÍNH TÓM LƯỢC (LINEAR ALGEBRA IN A NUTSHELL)**

**((** *Ma trận A có kích thước $n \times n$* **))**

### **Không suy biến (Nonsingular)**
$A$ có thể nghịch đảo
Các cột độc lập tuyến tính
Các hàng độc lập tuyến tính
Định thức khác không
$Ax = 0$ có một nghiệm duy nhất $x = 0$
$Ax = b$ có một nghiệm duy nhất $x = A^{-1}b$
$A$ có $n$ phần tử chốt (khác không)
$A$ có hạng đầy đủ $r = n$
Ma trận dạng bậc thang rút gọn là $R = I$
Không gian cột là toàn bộ $\mathbb{R}^n$
Không gian hàng là toàn bộ $\mathbb{R}^n$
Tất cả các trị riêng đều khác không
$A^TA$ là ma trận đối xứng xác định dương
$A$ có $n$ giá trị kỳ dị (dương)

### **Suy biến (Singular)**
$A$ không thể nghịch đảo
Các cột phụ thuộc tuyến tính
Các hàng phụ thuộc tuyến tính
Định thức bằng không
$Ax = 0$ có vô số nghiệm
$Ax = b$ không có nghiệm hoặc có vô số nghiệm
$A$ có $r < n$ phần tử chốt
$A$ có hạng $r < n$
$R$ có ít nhất một hàng gồm toàn số 0
Không gian cột có số chiều $r < n$
Không gian hàng có số chiều $r < n$
Không là một trị riêng của $A$
$A^TA$ chỉ là ma trận bán xác định
$A$ có $r < n$ giá trị kỳ dị
