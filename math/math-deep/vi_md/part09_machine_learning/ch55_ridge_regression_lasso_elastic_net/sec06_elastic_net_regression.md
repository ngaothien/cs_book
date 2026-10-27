# Mạng đàn hồi (elastic net) Hồi quy


<!-- PAGE 2097 -->
Khi $n \le 2$ và $K$ và $\tau$ là nhỏ và của cùng thứ tự của magnitude, nói 0.1 hoặc 0.01, không có noticeable difference. Ta ran ra các bài toán quy hoạch trên dữ liệu tập hợp của $200$ các điểm được sinh bởi sau đây Matlab bài toán quy hoạch: X14 $=$ 15*randn(200,1); ww14 $= 1$; y14 $=$ X14*ww14 $+$ 10*randn(200,1) $+ 20$; kết quả được hiển thị trong Hình 55.10, với sau đây colors: Phương pháp $(1)$ trong magenta, Phương pháp $(2)$ trong đỏ, Phương pháp $(3)$ trong xanh lam, và Phương pháp $(4)$ trong cyan. Tất cả bốn các đường thẳng là đồng nhất.
$$70$$
$$60$$
$$50$$
$$40$$
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-60-40-200204060$$
$$Figure 55.10: Comparison of the four methods with K = \tau  = 0.1.$$
Trong thứ tự để xem difference ta cũng ran của ta các bài toán quy hoạch với $K = 1000$ và $\tau  = 10000$; xem Hình 55.11. Như được kỳ vọng, do penalization của $b$, Phương pháp $(3)$ cho ta một cách đáng kể thấp hơn đường thẳng (trong đỏ), và do lớn giá trị của $\tau$, đường thẳng tương ứng với lasso (trong cyan) có nhỏ hơn hệ số góc. Phương pháp $(1)$ (trong magenta) cũng có nhỏ hơn hệ số góc nhưng vẫn thực hiện không deviate rằng nhiều từ bình phương tối thiểu (least squares) (trong xanh lam). Nó là cũng thú vị đến experiment trên dữ liệu các tập hợp ở đâu $n$ là lớn hơn (nói $20, 50)$.

## 55.6 Mạng đàn hồi (elastic net) Hồi quy

Lasso phương pháp là unsatisfactory khi $n$ (số chiều của dữ liệu) là nhiều lớn hơn hơn số $m$ của dữ liệu, bởi vì nó chỉ các chọn $m$ các tọa độ và các tập hợp những cái khác đến các giá trị

<!-- PAGE 2098 -->
$$70$$
$$60$$
$$50$$
$$40$$
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-60-40-200204060$$
$$Figure 55.11: Comparison of the four methods with K = 1000, \tau  = 10000.$$
Close đến không. Nó cũng có các bài tập với các nhóm của một cách cao correlated các biến. cách đến overcome bài toán này là đến cộng “ridge-like” số hạng $(1/2)Kw^{\top}w$ đến hàm mục tiêu (objective function). Điều này cách ta thu được hybrid của lasso và hồi quy Ridge (ridge regression) được gọi là mạng đàn hồi (elastic net) phương pháp và được định nghĩa như sau: Bài toán quy hoạch (mạng đàn hồi (elastic net)):
$$minimize \frac{1}{2} \xi^{\top} \xi  + \frac{1}{2} Kw^{\top}w + \tau 1_{n}^{\top} \epsilon$$
$$subject to$$
$$y -Xw -b1_{m} = \xi$$
$$w \le \epsilon$$
$$-w \le \epsilon ,$$
Ở đâu $K > 0$ và $\tau  \ge 0$ là hai các hằng số controlling influence của $\ell^{2}$ -chỉnh quy hóa (regularization) và $\ell^{1} -regularization.^{1}$ Nhận thấy rằng như trong trường hợp của hồi quy Ridge (ridge regression), cực tiểu hóa là performed trên $\xi , w, \epsilon$ và $b$, nhưng $b$ là không có phạt trong hàm mục tiêu (objective function). Ta có thể biểu diễn hàm mục tiêu (objective function) một cách trực tiếp theo $w, b$ và $\|w\|_{1}$, như
$$J(w, b) = \frac{1}{2} (Xw + b1_{m} -y)^{\top}(Xw + b1_{m} -y) + \frac{1}{2} Kw^{\top}w + \tau  \|w\|_{1} .$$
$\overline{1}\overline{Some} \overline{of} \overline{the} \overline{literature} \overline{denotes} \overline{K} \overline{by} \overline{\lambda}_{2}$ và $\tau$ bởi $\lambda_{1}$, nhưng ta ưu tiên không đến adopt điều này ký hiệu vì ta sử dụng $\lambda , \mu$ etc. đến ký hiệu Các nhân tử Lagrange (Lagrange multipliers).

<!-- PAGE 2099 -->
Ta để lại nó như một bài tập để chỉ ra rằng bởi expanding số hạng thứ nhất ta thu được
$$J(w, b) = \frac{1}{2} \begin{pmatrix} w^{\top} & b \end{pmatrix} \begin{pmatrix} X^{\top}X+ KI_{n} & X^{\top}1_{m} \\ 1_{m}^{\top}X & m \end{pmatrix} \begin{pmatrix} w \\ b \end{pmatrix} - \begin{pmatrix} w^{\top} & b \end{pmatrix} \begin{pmatrix} X^{\top}y \\ 1_{m}^{\top}y \end{pmatrix} + \frac{1}{2} y^{\top}y + \tau  \|w\|_{1} .$$
Ta cũng để lại nó như một bài tập để chỉ ra rằng ma trận
$$\begin{pmatrix} X^{\top}X+ KI_{n} & X^{\top}1_{m} \\ 1_{m}^{\top}X & m \end{pmatrix}$$
Là đối xứng xác định dương (SPD), và rằng hệ quả là, $J$ là lồi chặt (strictly convex). Vì nó là không âm, nó có duy nhất cực tiểu, sự kiện rằng là không hiển nhiên tại thứ nhất glance. Hàm Lagrange (Lagrangian) liên kết với của ta thứ nhất formulation của điều này tối ưu hóa bài toán là
$$L(\xi , w, \epsilon , b, \lambda , \alpha_{+} , \alpha_{-} ) = \frac{1}{2} \xi^{\top} \xi  -\xi^{\top} \lambda  + \lambda^{\top} y -b1_{m}^{\top}\lambda$$
$$+ \epsilon^{\top} (\tau 1_{n} -\alpha_{+}  -\alpha_{-} ) + w^{\top}(\alpha_{+}  -\alpha_{-} -X^{\top}\lambda ) + \frac{1}{2} Kw^{\top}w,$$
Do đó bằng cách đặt gradien $\nabla L_{\xi ,w,\epsilon ,b}$ đến không ta thu được các phương trình
$$\xi  = \lambda$$
$$Kw = -(\alpha_{+}  -\alpha_{-} -X^{\top}\lambda )(*_{w})$$
$$\alpha_{+}  + \alpha_{-} -\tau 1_{n} = 0$$
$$1_{m}^{\top}\lambda  = 0.$$
Ta tìm rằng $(*_{w})$ xác định $w$. Bằng cách sử dụng các phương trình này, ta có thể tìm đối ngẫu (dual) hàm nhưng trong thứ tự để giải đối ngẫu (dual) bằng cách sử dụng ADMM, vì $\lambda  \in \mathbb{R}^{m}$, nó là nhiều hơn/thêm thuận tiện đến viết $\lambda  = \lambda_{+}$ - $\lambda_{-}$, với $\lambda_{+} , \lambda_{-} \in \mathbb{R}_{+}^{m}$ (nhắc lại rằng $\alpha_{+} , \alpha_{-} \in \mathbb{R}_{+}^{n})$. Như trong derivation của đối ngẫu (dual) của hồi quy Ridge (ridge regression), ta rescale của ta các biến bởi định nghĩa $\beta_{+} , \beta_{-} , \mu_{+} , \mu_{-}$ sao cho
$$\alpha_{+}  = K\beta_{+} , \alpha_{-} = K\beta_{-} , \lambda_{+}  = K\mu_{+} , \lambda_{-} = K\mu_{-} .$$
Ta cũng cho $\mu  = \mu_{+}$ - $\mu_{-}$ sao cho $\lambda  = K\mu$. Thì $1_{m}^{\top}\lambda  = 0$ là tương đương đến
$$1_{m}^{\top}\mu_{+}  -1_{m}^{\top}\mu_{-} = 0,$$
Và vì $\xi  = \lambda  = K\mu$, ta có
$$\xi  = K(\mu_{+}  -\mu_{-} )$$
$$\beta_{+}  + \beta_{-} = \frac{\tau}{K} 1_{n}.$$
Bằng cách sử dụng $(*_{w})$ ta có thể viết
$$w = -(\beta_{+}  -\beta_{-} -X^{\top}\mu ) = -\beta_{+}  + \beta_{-} + X^{\top}\mu_{+}  -X^{\top}\mu_{-}$$
$$= \begin{pmatrix} -I_{n} & I_{n} & X^{\top} & -X^{\top} \end{pmatrix} \begin{pmatrix} \beta_{+} \\ \beta_{-} \\ \mu_{+} \\ \mu_{-} \end{pmatrix} .$$

<!-- PAGE 2100 -->
Thì ta có
$$\begin{pmatrix} -I_{n} & I_{n} & X^{\top} & -X^{\top\top} \end{pmatrix} \begin{pmatrix} -I_{n} & I_{n} & X^{\top} & -X^{\top} \end{pmatrix} = \begin{pmatrix} -I_{n} \\ I_{n} \\ X \\ X \end{pmatrix} \begin{pmatrix} -I_{n} & I_{n} & X^{\top} & -X^{\top} \end{pmatrix}$$
$$-$$
$$= \begin{pmatrix} I_{n} & -I_{n} & -X^{\top} & X^{\top} \\ -I_{n} & I_{n} & X^{\top} & -X^{\top} \\ -X & X & XX^{\top} & -XX^{\top} \\ X & X & XX^{\top} & XX^{\top} \end{pmatrix} .$$
$$--$$
Nếu ta định nghĩa đối xứng nửa xác định dương (positive semidefinite) 2(n $+ m) \times$ 2(n $+ m)$ ma trận $Q$ như
$$Q = \begin{pmatrix} I_{n} & -I_{n} & -X^{\top} & X^{\top} \\ -I_{n} & I_{n} & X^{\top} & -X^{\top} \\ -X & X & XX^{\top} & -XX^{\top} \\ X & X & XX^{\top} & XX^{\top} \end{pmatrix} ,$$
$$--$$
Thì
$$\frac{1}{2} w^{\top}w = \frac{1}{2} Q \begin{pmatrix} \beta_{+} \\ \beta_{-} \\ \mu_{+} \\ \mu_{-} \end{pmatrix} .$$
$$\begin{pmatrix} \beta_{+}^{\top} & \beta_{-}^{\top} & \mu_{+}^{\top} & \mu_{-}^{\top} \end{pmatrix}$$
Hệ quả là, bằng cách sử dụng $(*_{w})$ và sự kiện rằng $\xi  = K\mu$, ta tìm rằng đối ngẫu (dual) hàm được cho bởi
$$G(\mu , \beta_{+} , \beta_{-} ) = \frac{1}{2} \xi^{\top} \xi  -\xi^{\top} \lambda  + \lambda^{\top} y + w^{\top}(\alpha_{+}  -\alpha_{-} -X^{\top}\lambda ) + \frac{1}{2} Kw^{\top}w$$
$$= \frac{1}{2} \xi^{\top} \xi  -K\xi^{\top} \mu  + K\mu^{\top} y + Kw^{\top}(\beta_{+}  -\beta_{-} -X^{\top}\mu ) + \frac{1}{2} Kw^{\top}w$$
$$= \frac{1}{2} K^{2}\mu^{\top} \mu  -K^{2}\mu^{\top} \mu  + Ky^{\top}\mu  -Kw^{\top}w + \frac{1}{2} Kw^{\top}w$$
$$= - \frac{1}{2} K^{2}\mu^{\top} \mu  - \frac{1}{2} Kw^{\top}w + Ky^{\top}\mu .$$
Nhưng
$$\mu  = \begin{pmatrix} I_{m} & -I_{m} \end{pmatrix} \begin{pmatrix} \mu_{+} \\ \mu_{-} \end{pmatrix} ,$$
Do đó
$$\frac{1}{2} \mu^{\top} \mu  = \frac{1}{2} \begin{pmatrix} I_{m} & -I_{m} \\ -I_{m} & I_{m} \end{pmatrix} \begin{pmatrix} \mu_{+} \\ \mu_{-} \end{pmatrix} ,$$
$$\begin{pmatrix} \mu_{+}^{\top} & \mu_{-}^{\top} \end{pmatrix}$$

<!-- PAGE 2101 -->
Do đó ta thu được
$$G(\beta_{+} , \beta_{-} , \mu_{+} , \mu_{-} ) = - \frac{1}{2} K \begin{pmatrix} \beta_{+}^{\top} & \beta_{-}^{\top} & \mu_{+}^{\top} & \mu_{-}^{\top} \end{pmatrix} P \begin{pmatrix} \beta_{+} \\ \beta_{-} \\ \mu_{+} \\ \mu_{-} \end{pmatrix} -Kq^{\top} \begin{pmatrix} \beta_{+} \\ \beta_{-} \\ \mu_{+} \\ \mu_{-} \end{pmatrix}$$
Với
$$P = Q + K \begin{pmatrix} 0_{n,n} & 0_{n,n} & 0_{n,m} & 0_{n,m} \\ 0_{n,n} & 0_{n,n} & 0_{n,m} & 0_{n,m} \\ 0_{m,n} & 0_{m,n} & I_{m} & -I_{m} \\ 0_{m,n} & 0_{m,n} & I_{m} & I_{m} \end{pmatrix}$$
$$-$$
$$= \begin{pmatrix} I_{n} & -I_{n} & -X^{\top} & X^{\top} \\ -I_{n} & I_{n} & X^{\top} & -X^{\top} \\ -X & X & XX^{\top}+ KI_{m} & -XX^{\top}-KI_{m} \\ X & X & XX^{\top} & KI_{m} & XX^{\top}+ KI_{m} \end{pmatrix} ,$$
$$---$$
Và
$$q = \begin{pmatrix} 0_{n} \\ 0_{n} \\ -y \\ y \end{pmatrix} .$$
Các ràng buộc là các phương trình
$$\beta_{+}  + \beta_{-} = \frac{\tau}{K} 1_{n}$$
$$1_{m}^{\top}\mu_{+}  -1_{m}^{\top}\mu_{-} = 0,$$
Mà tương ứng với $(n + 1) \times$ 2(n $+ m)$ ma trận
$$A = \begin{pmatrix} I_{n} & I_{n} & 0_{n,m} & 0_{n,m} \\ 0_{n}^{\top} & 0_{n}^{\top} & 1_{m}^{\top} & -1_{m}^{\top} \end{pmatrix}$$
Và vế phải
$$c = \begin{pmatrix} \tau 1_{n} \\ \overline{K} 0 \end{pmatrix} .$$
Vì $K > 0$, đối ngẫu (dual) của mạng đàn hồi (elastic net) là tương đương đến

<!-- PAGE 2102 -->
Bài toán quy hoạch (Đối ngẫu (dual) Mạng đàn hồi (elastic net)):
$$minimize \frac{1}{2} \begin{pmatrix} \beta_{+}^{\top} & \beta_{-}^{\top} & \mu_{+}^{\top} & \mu_{-}^{\top} \end{pmatrix} P \begin{pmatrix} \beta_{+} \\ \beta_{-} \\ \mu_{+} \\ \mu_{-} \end{pmatrix} + q^{\top} \begin{pmatrix} \beta_{+} \\ \beta_{-} \\ \mu_{+} \\ \mu_{-} \end{pmatrix}$$
$$subject to$$
$$A \begin{pmatrix} \beta_{+} \\ \beta_{-} \\ \mu_{+} \\ \mu_{-} \end{pmatrix} = c,$$
$\beta_{+} , \beta_{-} \in \mathbb{R}_{+}^{n}, \mu_{+} , \mu_{-} \in \mathbb{R}_{+}^{m}$. Một lần $\xi  = K\mu  = K(\mu_{+}$ - $\mu_{-}$) và $w$ được xác định bởi $(*_{w})$, ta thu được $b$ bằng cách sử dụng phương trình
$$b1_{m} = y -Xw -\xi ,$$
Mà như trong Mục 55.5 cho ta
$$b =\overline{y} - \sum_{j=1}^{n}  \overline{X}^{j}w_{j},$$
Ở đâu $\overline{y}$ là có nghĩa của $y$ và $\overline{X}^{j}$ là có nghĩa của cột thứ $j$ của $X$. Ta để lại nó như dễ bài tập để chỉ ra rằng $A$ có hạng (rank) $n + 1$. Thì ta có thể giải ở trên bài toán quy hoạch bằng cách sử dụng ADMM, và ta có được thực hiện do đó. Điều này rất đồng dạng đến những gì được thực hiện trong Mục 56.3, và do đó chi tiết là để lại như một bài tập. Nhận thấy rằng khi $\tau  = 0$, mạng đàn hồi (elastic net) phương pháp rút gọn đến hồi quy Ridge (ridge regression). Như $K$ tiến tới đến $0$ mạng đàn hồi (elastic net) phương pháp tiến tới đến lasso, nhưng $K = 0$ là không allowable giá trị vì $\tau /0$ là undefined. Anyway, nếu ta thu được rid của ràng buộc
$$\beta_{+}  + \beta_{-} = \frac{\tau}{K} 1_{n}$$
Tương ứng tối ưu hóa bài toán quy hoạch không thực hiện xác định $w$. Experimenting với của ta bài toán quy hoạch ta tìm thấy rằng sự hội tụ trở thành rất slow cho $K < 10^{-3}$. Những gì ta có thể thực hiện nếu $K$ là nhỏ, nói $K < 10^{-3}$, là đến chạy lasso. đẹp cách đến “blend” hồi quy Ridge (ridge regression) và lasso là đến gọi mạng đàn hồi (elastic net) phương pháp với $K =$ C(1 - $\theta$) và $\tau  = C\theta$, ở đâu $0 \le \theta  < 1$ và $C > 0$. Chạy mạng đàn hồi (elastic net) phương pháp trên dữ liệu tập hợp (X14, y14) của Mục 55.5 với $K = \tau  =$ 0.5 chỉ ra một cách tuyệt đối không có difference, nhưng độc giả nên conduct nhiều hơn/thêm experiments để xem cách mà mạng đàn hồi (elastic net) behaves như $K$ và $\tau$ là varied (tốt nhất cách đến thực hiện điều này là để sử dụng $\theta$ như được giải thích ở trên). Đây là một ví dụ liên quan đến dữ liệu tập hợp (X20, y20) ở đâu X20 là một ma trận cỡ $50\times 30$ được sinh như sau:

<!-- PAGE 2103 -->
X20 $=$ randn(50,30); ww20 $= [0; 2; 0; -3; 0; -4; 1; 0; 2; 0; 2; 3; 0; -5; 6; 0; 1; 2; 0; 10; 0; 0; 3; 4; 5; 0; 0; -6; -8; 0]$; y20 $=$ X20*ww20 $+$ randn(50,1)*0.1 $+ 5$; Chạy của ta bài toán quy hoạch với $K =$ 0.01 và $\tau  =$ 0.99, và thì với $K =$ 0.99 và $\tau  =$ 0.01, ta thu được sau đây trọng số các vectơ (trong trái cột là trọng số vectơ tương ứng với $K =$ 0.01 và $\tau  =$ 0.99): 0.0254 0.2007 1.9193 2.0055 0.0766 0.0262 -3.0014 -2.8008 0.0512 0.0089 -3.8815 -3.7670 0.9591 0.8552 -0.0086 -0.3243 1.9576 1.9080 -0.0077 -0.1041 1.9881 2.0566 2.9223 2.8346 -0.0046 -0.0832 -4.9989 -4.8332 5.8640 5.4598 -0.0207 -0.2141 0.8285 0.8585 1.9310 1.8559 0.0046 0.0413 9.9232 9.4836 -0.0216 0.0303 0.0453 -0.0193 2.9384 3.0004 4.0525 3.9753 4.8723 4.6530 0.0767 0.1192 0.0132 -0.0203 -5.9750 -5.7537 -7.9764 -7.7594 -0.0054 0.0528 một cách tổng quát, các số trong trái cột, mà là nhiều hơn/thêm “lasso-like,” có clearer các không điểm và khác không các giá trị closer đến những phần tử đó của trọng số vectơ ww20 rằng đã được sử dụng đến create dữ liệu tập hợp. giá trị của $b$ tương ứng với thứ nhất gọi là $b =$ 5.1372, và giá trị của $b$ tương ứng với thứ hai gọi là $b =$ 5.208.
