# Liên hợp Hàm và Legendre Đối ngẫu (dual) Hàm


<!-- PAGE 1833 -->
Mà là một cách chính xác kết quả của cộng $\alpha  \ge 0$ và $\beta  \ge 0$ như bù/lỏng các biến đến các bất đẳng thức $(*_{3})$ của Ví dụ 50.6, cụ thể là
$$-X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + b \begin{pmatrix} 1_{p} \\ -1_{q} \end{pmatrix} + 1_{p+q} \le 0_{p+q},$$
Để tạo chúng các đẳng thức, ở đâu $\rho$ đóng vai trò của $b$. Khi các ràng buộc là afin, đối ngẫu (dual) hàm $G(\lambda , \nu$) có thể được được biểu diễn theo liên hợp của hàm mục tiêu (objective function) $J$.

## 50.11 Liên hợp Hàm và Legendre Đối ngẫu (dual) Func-

$$tion$$
Khái niệm của liên hợp hàm đi quay lại đến Legendre và đóng quan trọng vai trò trong cổ điển cơ học cho chuyển đổi Hàm Lagrange (Lagrangian) đến Hamiltonian; xem Arnold $[5]$ (Chương $3$, Các mục $14$ và $15)$.

> **Định nghĩa 50.11.** Cho $f$: $A \to \mathbb{R}$ là hàm được định nghĩa trên một số tập con $A$ của $\mathbb{R}^{n}$.
$$\mathbb{R}^{n} \mathbb{R}$$
Liên hợp $f^{*}$ của hàm $f$ là riêng hàm $f^{*}: \to$ được định nghĩa bởi
$$f^{*} (y) = \sup(\langle y, x\rangle -f(x)) = \sup(y^{\top}x -f(x)),y \in \mathbb{R}^{n}.$$
$$x\in Ax\in A$$
Liên hợp của hàm cũng được gọi là Fenchel liên hợp, hoặc Legendre biến đổi khi $f$ là khả vi (differentiable). Như từng điểm cận trên đúng (supremum) của họ của afin các hàm trong $y$, liên hợp hàm $f^{*}$ là lồi, chẵn/ngay cả nếu ban đầu hàm $f$ là không lồi. Theo định nghĩa của $f^{*}$ ta có
$$f(x) + f^{*} (y) \ge \langle x, y\rangle = x^{\top}y,$$
Bất cứ khi nào vế trái được định nghĩa. ở trên là đã biết như Fenchel’s bất đẳng thức (hoặc Young’s bất đẳng thức nếu $f$ là khả vi (differentiable)). Nếu $f$: $A \to \mathbb{R}$ là lồi (do đó $A$ là lồi) và nếu epi(f) là đóng, thì nó có thể được được hiển thị rằng $f^{**} = f$. Đặc biệt, điều này là đúng nếu $A =\mathbb{R}^{n}$. miền xác định của $f^{*}$ có thể được rất nhỏ, chẵn/ngay cả nếu miền xác định của $f$ là big. Ví dụ, nếu $f$: $\mathbb{R} \to \mathbb{R}$ là afin hàm cho trước bởi f(x) $=$ ax $+ b$ (với, $b \in \mathbb{R})$, thì hàm $x \mapsto$ yx - ax - $b$ là không bị chặn ở trên trừ khi $y = a$, do đó
$$($$
$$-bif y = a$$
$$f^{*} (y) =$$
$$+\infty otherwise.$$

<!-- PAGE 1834 -->
Miền xác định của $f^{*}$ có thể cũng là bigger hơn miền xác định của $f$; xem Ví dụ 50.8(3). các liên hợp của nhiều các hàm rằng đến lên trong tối ưu hóa là derived trong Boyd và Vandenberghe; xem $[29]$, Mục 3.3. Ta mention một vài rằng sẽ được sử dụng trong chương này.

> **Ví dụ 50.8.**
$(1)$ Âm lôgarit: f(x) $=$ -log $x$, với dom(f) $= {x \in \mathbb{R}$ | $x > 0}$. hàm $x \mapsto yx+log x$ là không bị chặn ở trên nếu $y \ge 0$, và khi $y < 0$, của nó cực đại là thu được khi và chỉ khi đạo hàm của nó là không, cụ thể là
$$y + \frac{1}{x} = 0.$$
Thế cho $x = -1/y$ trong yx $+$ log $x$, ta thu được $-1 + log(-1/y) = -1$ - log(-y), do đó ta có
$$f^{*} (y) = -\log(-y) -1,$$
Với $dom(f^{*}$) $= {y \in \mathbb{R}$ | $y < 0}$.
$$\mathbb{R}$$
$(2)$ Hàm mũ: f(x) $= e^{x}$, với dom(f) $=$. hàm $x \mapsto$ yx - $e^{x}$ là không bị chặn nếu $y < 0$. Khi $y > 0$, nó các đạt tới cực đại khi và chỉ khi đạo hàm của nó là không, cụ thể là
$$y -e^{x}= 0.$$
Thế cho $x =$ log $y$ trong yx - $e^{x}$, ta thu được $y$ log $y$ - $y$, do đó ta có
$$f^{*} (y) = y \log y -y,$$
Với $dom(f^{*}$) $= {y \in \mathbb{R}$ | $y \ge 0}$, với quy ước rằng $0$ log $0 = 0$.
$(3)$ Âm Entropy: f(x) $= x$ log $x$, với dom(f) $= {x \in \mathbb{R}$ | $x \ge 0}$, với quy ước rằng $0$ log $0 = 0$. hàm $x \mapsto$ yx - $x$ log $x$ là bị chặn ở trên với mọi $y > 0$, và nó đạt của nó cực đại khi đạo hàm của nó là không, cụ thể là
$$y -\log x -1 = 0.$$
Thế cho $x = e^{y-1}$ trong yx - $x$ log $x$, ta thu được $ye^{y-1}$ - $e^{y-1}(y$ - $1) = e^{y-1}$, mà cho ta
$$f^{*} (y) = e^{y-1},$$
Với $dom(f^{*}$) $=\mathbb{R}$.
$(4)$ Lồi chặt (strictly convex) toàn phương hàm: f(x) $=^{1} x^{\top}Ax$, ở đâu $A$ là $n \times  n$ đối xứng xác định dương (SPD) ma trận, với dom(f) $= \mathbb{R}^{n}.^{2}$ hàm $x \mapsto y^{\top}x -_{2}^{1}x^{\top}Ax$ có duy nhất cực đại khi là gradien là không, cụ thể là
$$y = Ax.$$

<!-- PAGE 1835 -->
Thế cho $x = A^{-1}y$ trong $y^{\top}x -_{2}^{1}x^{\top}Ax$, ta thu được
$$y^{\top}A^{-1}y - \frac{1}{2} y^{\top}A^{-1}y = - \frac{1}{2} y^{\top}A^{-1}y,$$
Do đó
$$f^{*} (y) = - \frac{1}{2} y^{\top}A^{-1}y$$
Với $dom(f^{*}$) $=\mathbb{R}^{n}$.
$(5)$ Log-determinant: f(X) $=$ log $det(X^{-1})$, ở đâu $X$ là $n\times n$ đối xứng xác định dương (SPD) ma trận. Thì
$$f(Y ) = \log \det((-Y )^{-1}) -n,$$
Ở đâu $Y$ là $n \times  n$ đối xứng âm xác định ma trận; xem Boyd và Vandenberghe; xem $[29]$, Mục 3.3.1, Ví dụ 3.23.
$(6)$ Chuẩn (norm) trên $\mathbb{R}^{n}$: f(x) $= \|x\|$ với mọi chuẩn (norm) $\|\|$ trên $\mathbb{R}^{n}$, với dom(f) $= \mathbb{R}^{n}$. Nhắc lại từ Mục 14.7 rằng đối ngẫu (dual) chuẩn (norm) $\|\|^{D}$ của chuẩn (norm) $\|\|$ (đối với chính tắc
$$\mathbb{R}^{n}$$
Tích vô hướng (inner product) $x \cdot  y = y^{\top}x$ trên được cho bởi
$$\|y\|^{D}= \sup|y^{\top}x|,$$
$$\|x\|=1$$
Và rằng
$$|y^{\top}x| \le \|x\|\|y\|^{D}.$$
Ta có
$$f^{*} (y) = \sup(y^{\top}x -\|x\|)$$
$$x\in \mathbb{R} n$$
$$=\in \mathbb{R} supn \begin{pmatrix} x \\ y^{\top} & -1 \\ \|x\| \end{pmatrix} \|x\|$$
$$x,x\neq 0$$
$$\le \sup(\|y\|^{D}-1) \|x\|,$$
$$x\in \mathbb{R} n,x\neq 0$$
Do đó nếu $\|y\|^{D} > 1$ điều này số hạng cuối cùng đi đến $+\infty$, nhưng nếu $\|y\|^{D} \le 1$, thì của nó cực đại là $0$. Vì vậy,
$$($$
$$0if \|y\|^{D}\le 1$$
$$f^{*} (y) = \|y\|^{*}=$$
$$+\infty otherwise.$$
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
$(7)$ Chuẩn (norm) squared: f(x) $=_{2}^{1} \|x\|^{2}$ với mọi chuẩn (norm) $\|\|$ trên, với dom(f) $=$. Vì $|y^{\top}x| \le \|x\|\|y\|^{D}$, ta có
$$y^{\top}x -(1/2) \|x\|^{2}\le \|y\|^{D}\|x\|-(1/2) \|x\|^{2}.$$

<!-- PAGE 1836 -->
Vế phải là toàn phương hàm của $\|x\|$ mà đạt được của nó cực đại tại $\|x\| = \|y\|^{D}$, với cực đại giá trị $(1/2)(\|y\|^{D})^{2}$. Vì vậy
$$y^{\top}x -(1/2) \|x\|^{2}\le (1/2) \begin{pmatrix} \|y\|^{D2} \end{pmatrix}$$
Với mọi $x$, mà chỉ ra rằng
$$f^{*} (y) \le (1/2) \begin{pmatrix} \|y\|^{D2} \end{pmatrix} .$$
Theo định nghĩa của đối ngẫu (dual) chuẩn (norm) và bởi vì unit mặt cầu là compắc, với mọi $y \in \mathbb{R}^{n}$,
$$\mathbb{R}^{n}$$
Tồn tại một $x \in$ sao cho $\|x\| = 1$ và $y^{\top}x = \|y\|^{D}$, do đó nhân cả hai các vế/cạnh bởi $\|y\|^{D}$ ta thu được
$$y^{\top}\|y\|^{D}x = \begin{pmatrix} \|y\|^{D2} \\ = & y \end{pmatrix}$$
Và cho $z = \|y\|^{D} x$, vì $\|x\| = 1$ ta có $\|z\|  \| \|^{D} \|x\| = \|y\|^{D}$, do đó ta thu được
$$y^{\top}z -(1/2)(\|z\|)^{2}= \begin{pmatrix} \|y\|^{D2} \end{pmatrix} -(1/2) \begin{pmatrix} \|y\|^{D2} \end{pmatrix} = (1/2) \begin{pmatrix} \|y\|^{D2} \end{pmatrix} ,$$
$$which shows that the upper bound (1/2) \begin{pmatrix} \|y\|^{D2} \\ 1 \end{pmatrix} is achieved. Therefore,$$
$$f^{*} (y) =2 \begin{pmatrix} \|y\|^{D2} \end{pmatrix} ,$$
Và $dom(f^{*}$) $=\mathbb{R}^{n}$.
$$(8) Log-sum-\exp function: f(x) = \log \sum_{i}  , where x = (x_{1}, \dots  , x_{n}) \in \mathbb{R}^{n}.To$$
$$\mathbb{R}^{n} \begin{pmatrix} n & e^{xi} \\ =1 \\ whichthe \end{pmatrix}$$
Xác định các giá trị của $y \in$ cho cực đại của g(x) $= y^{\top}x$ - f(x) trên
$$\mathbb{R}^{n}$$
$x \in$ là đạt được, ta tính gradien của nó và ta tìm
$$\begin{pmatrix} e^{x1} \\ y_{1} - \\ n & e_{i}^{x} \\ \ddots \\ e^{xn} \\ y_{n} - \\ n & e_{i}^{x} \end{pmatrix} \sum_{i}$$
$$\nabla f_{x} =.$$
$$\sum_{i}  =1$$
Vì vậy, $(y_{1}, \dots  , y_{n})$ phải thỏa mãn hệ của các phương trình
$$y_{j} = \frac{e^{xj}}{e_{i}^{x}} \sum_{i}  n  ,j = 1, \dots  , n.(*)$$
$$=1$$
$$The condition \sum_{i}  n=1 y_{i} = 1 is obviously necessary, as well as the conditions y_{i} > 0, for$$
$i = 1, \dots  , n$. Ngược lại, nếu $1^{\top}y = 1$ và $y > 0$, thì $x_{j} =$ log $y_{i}$ cho $i = 1, \dots  , n$ là nghiệm. Vì (*) suy ra rằng
$$x_{i} = \log y_{i} + \log \begin{pmatrix} e^{xi} \end{pmatrix} \sum_{i=1}^{n}  ,(**)$$

<!-- PAGE 1837 -->
Ta thu được
$$y^{\top}x -f(x) = \sum_{i=1}^{n}  y_{i}x_{i} -\log \begin{pmatrix} e^{xi} \end{pmatrix} \sum_{i=1}^{n}$$
$$= \sum_{i=1}^{n}  y_{i} \log y_{i} + \sum_{i=1}^{n}  y_{i} \log \begin{pmatrix} e^{xi} \end{pmatrix} \sum_{i=1}^{n}  -\log \begin{pmatrix} e^{xi} \end{pmatrix} \sum_{i=1}^{n}  by (**)$$
$$= \sum_{i=1}^{n}  y_{i} \log y_{i} + \begin{pmatrix} y_{i} -1 \end{pmatrix} \sum_{i=1}^{n}  \log \begin{pmatrix} e^{xi} \end{pmatrix} \sum_{i=1}^{n}$$
$$= \sum_{i=1}^{n}  y_{i} \log y_{i}since \sum_{i}  n=1 y_{i} = 1.$$
$$Consequently, if f^{*} (y) is defined, then f^{*} (y) = \sum_{i}  n=1 y_{i} \log y_{i}. If we agree that 0 \log 0 =$$
$0$, thì nó là dễ bài tập (hoặc, xem Boyd và Vandenberghe $[29]$, Mục 3.3, Ví dụ 3.25) để chỉ ra rằng
$$f^{*} (y) =( \sum_{i}  n=1 y_{i} \log y_{i}if 1^{\top}y = 1 and y \ge 0$$
$$\infty otherwise.$$
Do đó ta thu được âm entropy bị thu hẹp đến miền xác định $1^{\top}y = 1$ và $y \ge 0$.
$$\mathbb{R}^{n} \mathbb{R}$$
Nếu $f$: $\to$ là lồi và khả vi (differentiable), thì $x^{*}$ các cực đại hóa $x^{\top}y$ -f(x) khi và chỉ khi $x^{*}$ cực tiểu hóa $-x^{\top}y +$ f(x) khi và chỉ khi
$$\nabla f_{x*}= y,$$
Và do đó
$$f^{*} (y) = (x^{*})^{\top}\nabla f_{x*}-f(x^{*}).$$
Hệ quả là, nếu ta có thể giải phương trình
$$\nabla f_{z} = y$$
Cho $z$ cho trước $y$, thì ta thu được $f^{*} (y)$. Nó có thể được được hiển thị rằng nếu $f$ là hai lần khả vi (differentiable), lồi chặt (strictly convex), và surlinear, mà có nghĩa là
$$\|y\|lim\mapsto +\infty \frac{f(y)}{\|y\|} = +\infty ,$$
Thì tồn tại duy nhất một $x_{y}$ sao cho $\nabla f_{xy} = y$, sao cho
$$f^{*} (y) = x_{y}^{\top} \nabla f_{xy} -f(x_{y}),$$
Và $f^{*}$ là khả vi (differentiable) với
$$\nabla f_{y}^{*}  = x_{y}.$$
Ta bây giờ trả về đến của ta tối ưu hóa bài toán.

<!-- PAGE 1838 -->

> **Mệnh đề 50.20.** Xét Bài toán $(P)$,
$$minimizeJ(v)$$
$$subject to Av \le b$$
$$Cv = d,$$
Với afin bất đẳng thức và đẳng thức các ràng buộc (với $A$ một ma trận cỡ $m \times  n$, $C$ một ma trận cỡ $p \times  n$, $b \in \mathbb{R}^{m}, d \in \mathbb{R}^{p})$. đối ngẫu (dual) hàm $G(\lambda , \nu$) được cho bởi
$$($$
$$-b^{\top}\lambda  -d^{\top}\nu  -J^{*}(-A^{\top}\lambda  -C^{\top}\nu )if -A^{\top}\lambda  -C^{\top}\nu  \in dom(J^{*}),$$
$$G(\lambda , \nu ) =$$
$$-\infty otherwise,$$
Với mọi $\lambda  \in \mathbb{R}_{+}^{m}$ và tất cả $\nu  \in \mathbb{R}^{p}$, ở đâu $J^{*}$ là liên hợp của $J$.

*Chứng minh.* Hàm Lagrange (Lagrangian) liên kết với ở trên bài toán quy hoạch là
$$L(v, \lambda , \nu ) = J(v) + (Av -b)^{\top}\lambda  + (Cv -d)^{\top}\nu$$
$$= -b^{\top}\lambda  -d^{\top}\nu  + J(v) + (A^{\top}\lambda  + C^{\top}\nu )^{\top}v,$$
Với $\lambda  \in \mathbb{R}_{+}^{m}$ và $\nu  \in \mathbb{R}^{p}$. Theo Định nghĩa
$$G(\lambda , \nu ) = -b^{\top}\lambda  -d^{\top}\nu  + \inf(J(v) + (A^{\top}\lambda  + C^{\top}\nu )^{\top}v)$$
$$v\in \mathbb{R} n$$
$$= -b^{\top}\lambda  -d^{\top}\nu  -\sup(-(A^{\top}\lambda  + C^{\top}\nu )^{\top}v -J(v))$$
$$v\in \mathbb{R} n$$
$$= -b^{\top}\lambda  -d^{\top}\nu  -J^{*}(-A^{\top}\lambda  -C^{\top}\nu ).$$
Vì vậy, với mọi $\lambda  \in \mathbb{R}_{+}^{m}$ và tất cả $\nu  \in \mathbb{R}^{p}$, ta có
$$($$
$$-b^{\top}\lambda  -d^{\top}\nu  -J^{*}(-A^{\top}\lambda  -C^{\top}\nu )if -A^{\top}\lambda  -C^{\top}\nu  \in dom(J^{*}),$$
$$G(\lambda , \nu ) =$$
$$-\infty otherwise,$$
Như đã khẳng định. Như ứng dụng của Mệnh đề 50.20, xét sau đây ví dụ.

> **Ví dụ 50.9.** Xét sau đây bài toán:
$$minimize\|v\|$$
$$subject to Av = b,$$
Ở đâu $\|\|$ là bất kỳ chuẩn (norm) trên $\mathbb{R}^{n}$. Bằng cách sử dụng kết quả của Ví dụ 50.8(6), ta thu được
$$G(\nu ) = -b^{\top}\nu  -

$-A^{\top}\nu^{*}$

,$$ rằng là,
$$($$
$$-b^{\top}\nu if

$A^{\top}\nu^{D}$

$\le$ 1$$
$$G(\nu ) =$$
$$-\infty otherwise.$$
Trong trường hợp đặc biệt khi $\|\| = \|\|_{2}$, ta cũng có $\|\|^{D} = \|\|_{2}$.

<!-- PAGE 1839 -->
Một cái khác thú vị ứng dụng là đến entropy cực tiểu hóa bài toán.

> **Ví dụ 50.10.** Xét sau đây bài toán đã biết như entropy cực tiểu hóa:
$$minimizef(x) = \sum_{i=1}^{n}  x_{i} \log x_{i}$$
$$subject to Ax \le b$$
$$1^{\top}x = 1,$$
$$\mathbb{R}^{n}$$
Ở đâu dom(f) $= {x \in$ | $x \ge 0}$. Bởi Ví dụ 50.8(3), liên hợp của âm entropy hàm $u$ log $u$ là $e^{v-1}$, do đó ta dễ dàng xem rằng
$$f^{*} (y) = \sum_{i=1}^{n}  e^{yi-1},$$
Mà được định nghĩa trên $\mathbb{R}^{n}$. Mệnh đề 50.20 suy ra rằng đối ngẫu (dual) hàm $G(\lambda , \mu$) của entropy cực tiểu hóa bài toán được cho bởi
$$G(\lambda , \mu ) = -b^{\top}\lambda  -\mu  -e^{-\mu-1} \sum_{i=1}^{n}  e^{-(Ai)\top\lambda},$$
$$\mathbb{R}_{+}^{n}\mathbb{R}$$
Với mọi $\lambda  \in$ và tất cả $\mu  \in$, ở đâu $A^{i}$ là cột thứ $i$ của $A$. Suy ra rằng đối ngẫu (dual) bài toán quy hoạch là:
$$maximize-b^{\top}\lambda  -\mu  -e^{-\mu-1} \sum_{i=1}^{n}  e^{-(Ai)\top\lambda}$$
$$subject to \lambda  \ge 0.$$
Ta có thể đơn giản hóa bài toán này bởi cực đại hóa trên biến $\mu  \in \mathbb{R}$. Cho cố định $\lambda$, hàm mục tiêu (objective function) là maximized khi đạo hàm là không, nghĩa là,
$$-1 + e^{-\mu-1} \sum_{i=1}^{n}  e^{-(Ai)\top\lambda}= 0,$$
Mà cho ta
$$\mu  = \log \begin{pmatrix} e^{-(Ai)\top\lambda} \end{pmatrix} \sum_{i=1}^{n}  -1.$$
Bởi plugging ở trên giá trị quay lại vào hàm mục tiêu (objective function) của đối ngẫu (dual), ta thu được kết quả sau bài toán quy hoạch:
$$maximize-b^{\top}\lambda  -\log \begin{pmatrix} e^{-(Ai)\top\lambda} \end{pmatrix} \sum_{i=1}^{n}$$
$$subject to \lambda  \ge 0.$$

<!-- PAGE 1840 -->
Entropy cực tiểu hóa bài toán là một cái khác bài toán cho mà Định lý 50.18 áp dụng, và do đó có thể được được giải bằng cách sử dụng đối ngẫu (dual) bài toán quy hoạch. Thật vậy, Hàm Lagrange (Lagrangian) của gốc (primal) bài toán quy hoạch được cho bởi
$$L(x, \lambda , \mu ) = \sum_{i-1}^{n}  x_{i} \log x_{i} + \lambda^{\top} (Ax -b) + \mu (1^{\top}x -1).$$
Bằng cách sử dụng đạo hàm thứ hai tiêu chuẩn cho tính lồi, ta xem rằng L(x, $\lambda , \mu$) là lồi chặt (strictly convex) cho $x \in \mathbb{R}_{+}^{n}$ và là bị chặn ở dưới, do đó nó có duy nhất cực tiểu mà là thu được bằng cách đặt gradien $\nabla L_{x}$ đến không. Ta có
$$\nabla L_{x} = \begin{pmatrix} \log x_{1} + 1 + (A^{1})^{\top}\lambda  + \mu \\ \vdots \\ \log x_{n} + 1 + (A^{n})^{\top}\lambda  + \mu . \end{pmatrix}$$
Do đó bằng cách đặt $\nabla L_{x}$ đến $0$ ta thu được
$$x_{i} = e^{-((An)\top\lambda+\mu+1)},i = 1, \dots  , n.(*)$$
Theo Định lý 50.18, vì hàm mục tiêu (objective function) là lồi và các ràng buộc là afin, nếu gốc (primal) có nghiệm thì do đó thực hiện đối ngẫu (dual), và $\lambda$ và $\mu$ constitute nghiệm tối ưu (optimal solution) của đối ngẫu (dual), thì $x = (x_{1}, \dots  , x_{n})$ cho trước bởi các phương trình trong (*) là nghiệm tối ưu (optimal solution) của gốc (primal). Khác các ví dụ là cho trước trong Boyd và Vandenberghe; xem $[29]$, Mục 5.1.6. derivation của đối ngẫu (dual) hàm của Bài toán $(SVM_{h1})$ từ Mục 50.5 liên quan đến đồng dạng loại/kiểu của lập luận.

> **Ví dụ 50.11.** Xét Lề cứng (hard margin) Bài toán $(SVM_{h1})$:
$$maximize\delta$$
$$subject to$$
$$w^{\top}u_{i} -b \ge \delta i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge \delta j = 1, \dots  , q$$
$$\|w\|_{2} \le 1,$$
Mà được chuyển đổi đến sau đây cực tiểu hóa bài toán:
$$minimize-2\delta$$
$$subject to$$
$$w^{\top}u_{i} -b \ge \delta i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge \delta j = 1, \dots  , q$$
$$\|w\|_{2} \le 1.$$

<!-- PAGE 1841 -->
Ta được thay thế $\delta$ bởi $2\delta$ bởi vì điều này sẽ tạo nó dễ hơn để tìm đẹp hình học interpretation. Nhắc lại từ Mục 50.5 rằng Bài toán $(SVM_{h1})$ có nghiệm tối ưu (optimal solution) khi và chỉ khi $\delta  > 0$, trong mà trường hợp $\|w\| = 1$. tương ứng Hàm Lagrange (Lagrangian) với $\lambda  \in \mathbb{R}_{+}^{p}, \mu  \in \mathbb{R}_{+}^{q}, \gamma  \in \mathbb{R}^{+}$, là
$$L(w, b, \delta , \lambda , \mu , \gamma ) = -2\delta  + \sum_{i=1}^{p}  \lambda_{i} (\delta  + b -w^{\top}u_{i}) + \sum_{j=1}^{q}  \mu_{j} (\delta  -b + w^{\top}v_{j}) + \gamma (\|w\|_{2} -1)$$
$$= w^{\top} \begin{pmatrix} - & \lambda_{i} u_{i} + & \mu_{j} v_{j} \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}  + \gamma  \|w\|_{2} + \begin{pmatrix} \lambda_{i}  - & \mu_{j} \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}  b$$
$$+ \begin{pmatrix} -2 + & \lambda_{i}  + & \mu_{j} \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}  \delta  -\gamma .$$
Tiếp theo để tìm đối ngẫu (dual) hàm $G(\lambda , \mu , \gamma$) ta cần để cực tiểu hóa L(w, $b, \delta , \lambda , \mu , \gamma$) đối với $w, b$ và $\delta$, do đó gradien của nó đối với $w, b$ và $\delta$ phải là không. Điều này suy ra rằng
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$-2 + \sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = 0,$$
Mà cho ta
$$\sum_{i=1}^{p}  \lambda_{i}  = \sum_{j=1}^{q}  \mu_{j}  = 1.$$
Nhận thấy rằng ta đã thực hiện không tính đạo hàm riêng (partial derivative) đối với $w$ bởi vì nó thực hiện không cho bất kỳ hữu ích information do presence của số hạng $\|w\|_{2}$ (như opposed đến $\|w\|_{2}^{2})$. Của ta cực tiểu hóa bài toán là rút gọn đến: tìm
$$!$$
$$w,\|infw\|\le 1w^{\top} \begin{pmatrix} \mu_{j} v_{j}- & \lambda_{i} u_{i} \end{pmatrix} \sum_{j=1}^{q}  \sum_{i=1}^{p}  + \gamma  \|w\|_{2} -\gamma$$
$$!$$
$$= -\gamma  -\gamma w,\|infw\|\le 1-w^{\top} \frac{1}{\gamma} \begin{pmatrix} \mu_{j} v_{j}- & \lambda_{i} u_{i} \end{pmatrix} \sum_{j=1}^{q}  \sum_{i=1}^{p}  + \|-w\|_{2}$$
$$-\gamma if_{\gamma}^{1} \sum_{j}  q \mu_{j} v_{j} -p \lambda_{i} u_{i}



$D\le$ 1$$
$$==1 \sum_{i}  =12by Example 50.8(6)$$
$-\infty$ ngược lại 
$$=(-\gamma if \sum  qj=1 \mu_{j} v_{j} - \sum_{i}  p=1 \lambda_{i} u_{i} \le \gamma since \|\|_{2}^{D} = \|\|_{2} and \gamma  > 0$$
$$2$$
$-\infty$ ngược lại.

<!-- PAGE 1842 -->
Ta kiểm chứng được ngay rằng ở trên công thức là vẫn đúng nếu $\gamma  = 0$. Vì vậy
$$G(\lambda , \mu , \gamma ) =(-\gamma if \sum  qj=1 \mu_{j} v_{j} - \sum_{i}  p=1 \lambda_{i} u_{i} \le \gamma$$
$$2$$
$$-\infty otherwise.$$
$$Since \sum_{j}  q=1 \mu_{j} v_{j} - \sum_{i}  p=1 \lambda_{i} u_{i} \le \gamma  iff-\gamma  \le - \sum_{j}  q=1 \mu_{j} v_{j} - \sum_{i}  p=1 \lambda_{i} u_{i}, the dual pro-$$
$$2$$
Gram, cực đại hóa $G(\lambda , \mu , \gamma$), $is^{2}$ tương đương đến
$$maximize- \sum_{j=1}^{q}  \mu_{j} v_{j} - \sum_{i=1}^{p}  \lambda_{i} u_{i}$$
$$2$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  = 1, \lambda  \ge 0$$
$$\sum_{j=1}^{q}  \mu_{j}  = 1, \mu  \ge 0,$$
Tương đương
$$minimize \sum_{j=1}^{q}  \mu_{j} v_{j} - \sum_{i=1}^{p}  \lambda_{i} u_{i}$$
$$2$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  = 1, \lambda  \ge 0$$
$$\sum_{j=1}^{q}  \mu_{j}  = 1, \mu  \ge 0.$$
$$Geometrically, \sum_{i}  p=1 \lambda u_{i} with \sum_{i}  p \lambda_{i}  = 1 and \lambda  \ge 0 is a convex combination of the u_{i}s,$$
$$and \sum_{j}  q=1 \mu_{j} v_{j} with \sum_{j}^{i}  q \mu_{j}  = 1^{=1} and \mu  \ge 0 is a convex combination of the v_{j}s, so the dual$$
Bài toán quy hoạch là đến $minimize^{=1}$ khoảng cách giữa đa diện $conv(u_{1}, \dots  , u_{p})$ (bao lồi (convex hull) của $u_{i}s)$ và đa diện $conv(v_{1}, \dots  , v_{q})$ (bao lồi (convex hull) của $v_{j}s)$. Vì cả hai các đa diện là compắc, ngắn nhất khoảng cách giữa thì là đạt được. Thực ra, tồn tại một đỉnh $u_{i}$ sao cho nếu $P(u_{i})$ là của nó phép chiếu lên $conv(v_{1}, \dots  , v_{q})$ (mà tồn tại bởi Không gian Hilbert (Hilbert space) lý thuyết), thì độ dài của đường thẳng đoạn thẳng $(u_{i}, P(u_{i}))$ là ngắn nhất khoảng cách giữa hai các đa diện (và tương tự tồn tại một đỉnh $v_{j}$ sao cho nếu $P(v_{j})$ là của nó phép chiếu lên $conv(u_{1}, \dots  , u_{p})$ thì độ dài của đường thẳng đoạn thẳng $(v_{j}, P(v_{j}))$ là ngắn nhất khoảng cách giữa hai các đa diện). Nếu hai các tập con là khả ly, trong mà trường hợp Bài toán $(SVM_{h1})$ có nghiệm tối ưu (optimal solution) $\delta  > 0$, bởi vì hàm mục tiêu (objective function) là lồi và lồi ràng buộc $\|w\|_{2} \le 1$ là qualified vì $\delta$ có thể là âm, theo Định lý 50.17(2) khoảng cách đối ngẫu (duality gap) là không, do đó $\delta$ là một nửa của
