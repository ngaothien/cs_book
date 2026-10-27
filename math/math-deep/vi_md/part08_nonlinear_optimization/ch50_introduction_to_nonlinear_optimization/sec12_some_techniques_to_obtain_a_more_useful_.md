# Một số Các kỹ thuật để thu được Nhiều hơn/thêm Hữu ích Đối ngẫu (dual) Bài toán quy hoạch


<!-- PAGE 1843 -->
Cực tiểu khoảng cách giữa hai lồi các đa diện $conv(u_{1}, \dots  , u_{p})$ và $conv(v_{1}, \dots  , v_{q})$; xem Hình 50.19.
$$u3$$
$$u2$$
$$u4$$
$$u1$$
$$up$$
$$ui$$
$$v1$$
$$v$$
$$2$$
$$vp$$
$$v3$$
$$\mathbb{R}^{2}$$

![Figure 50.19](../../assets/ch50/fig_50_19.png)

**Hình 50.19:** Trong bao lồi (convex hull) của $u_{i}s$, cụ thể là xanh lam hexagon, được tách từ bao lồi (convex hull) của $v_{j}s$, i.e. đỏ square, bởi tím siêu phẳng (hyperplane) (đường thẳng) mà là vuông góc đường phân giác đến xanh lam đường thẳng đoạn thẳng giữa $u_{i}$ và $v_{1}$, ở đâu điều này xanh lam đường thẳng đoạn thẳng là ngắn nhất khoảng cách giữa hai lồi các đa giác. Nó nên được lưu ý rằng ràng buộc $\|w\|\le 1$ cho ta formulation của bài toán đối ngẫu (dual problem) mà có advantage của có đẹp hình học interpretation: việc tìm tối tiểu khoảng cách giữa lồi các đa diện $conv(u_{1}, \dots  , u_{p})$ và $conv(v_{1}, \dots  , v_{q})$. Không may là điều này formulation là không hữu ích cho thực sự việc giải bài toán. Tuy nhiên, nếu tương đương ràng buộc $\|w\|^{2} (= w^{\top}w) \le 1$ được sử dụng, thì bài toán đối ngẫu (dual problem) là nhiều nhiều hơn/thêm hữu ích như việc giải công cụ. Trong Chương $54$ ta xét trường hợp ở đâu các tập hợp của các điểm ${u_{1}, \dots  , u_{p}}$ và ${v_{1}, \dots  , v_{q}}$ là không một cách tuyến tính khả ly.

## 50.12 Một số Các kỹ thuật để thu được Nhiều hơn/thêm Hữu ích Đối ngẫu (dual)

$$Program$$
Trong một số các trường hợp, nó là advantageous đến reformulate gốc (primal) tối ưu hóa bài toán để thu được nhiều hơn/thêm hữu ích bài toán đối ngẫu (dual problem). Ba khác nhau reformulations là proposed trong Boyd và Vandenberghe; xem $[29]$, Mục 5.7:
$(1)$ Giới thiệu mới các biến và liên kết đẳng thức các ràng buộc.
$(2)$ Thay thế hàm mục tiêu (objective function) với tăng hàm của ban đầu hàm.

<!-- PAGE 1844 -->
$(3)$ Tạo ra tường minh các ràng buộc ẩn, nghĩa là, incorporating chúng vào miền xác định của hàm mục tiêu (objective function). Ta chỉ cho illustrations của $(1)$ và $(2)$ và refer độc giả đến Boyd và Vandenberghe $[29]$ (Mục 5.7) cho nhiều hơn/thêm các ví dụ của các phần tử này các kỹ thuật. Xét không ràng buộc bài toán quy hoạch:
$$minimizef(Ax + b),$$
Ở đâu $A$ là một ma trận cỡ $m \times  n$ và $b \in \mathbb{R}^{m}$. Trong khi các điều kiện cho không khoảng cách đối ngẫu (duality gap) được thỏa mãn, Hàm Lagrange (Lagrangian) là
$$L(x) = f(Ax + b),$$
Do đó đối ngẫu (dual) hàm $G$ là hằng số hàm có giá trị là
$$G = \inf f(Ax + b),$$
$$x\in \mathbb{R} n$$
Mà là không hữu ích tại tất cả. Cho chúng ta reformulate bài toán như
$$minimizef(y)$$
$$subject to$$
$$Ax + b = y,$$
$$\mathbb{R}^{m}$$
Ở đâu ta đã giới thiệu mới biến $y \in$ và đẳng thức ràng buộc Ax $+ b = y$. hai các bài tập là hiển nhiên tương đương. Hàm Lagrange (Lagrangian) của reformulated bài toán là
$$L(x, y, \mu ) = f(y) + \mu^{\top} (Ax + b -y)$$
Ở đâu $\mu  \in \mathbb{R}^{m}$. để tìm đối ngẫu (dual) hàm $G(\mu$) ta cực tiểu hóa L(x, $y, \mu$) trên $x$ và $y$. Cực tiểu hóa trên $x$ ta xem rằng $G(\mu$) $= -\infty$ trừ khi $A^{\top}\mu  = 0$, trong mà trường hợp ta là trái với
$$G(\mu ) = b^{\top}\mu  + \inf (f(y) -\mu^{\top} y) = b^{\top}\mu  -\inf (\mu^{\top} y -f(y)) = b^{\top}\mu  -f^{*}(\mu ),$$
$$yy$$
Ở đâu $f^{*}$ là liên hợp của $f$. Suy ra rằng đối ngẫu (dual) bài toán quy hoạch có thể được biểu diễn dưới dạng
$$maximizeb^{\top}\mu  -f^{*} (\mu )$$
$$subject to$$
$$A^{\top}\mu  = 0.$$
Điều này formulation của đối ngẫu (dual) là nhiều nhiều hơn/thêm hữu ích hơn đối ngẫu (dual) của ban đầu bài toán quy hoạch.

<!-- PAGE 1845 -->

> **Ví dụ 50.12.** Như concrete ví dụ, xét sau đây không ràng buộc bài toán quy hoạch:
$$minimizef(x) = \log \begin{pmatrix} e^{(Ai)\top x+bi} \end{pmatrix} \sum_{i=1}^{n}$$
$$\mathbb{R}^{n}$$
Ở đâu $A^{i}$ là vectơ cột (column vector) trong. Ta reformulate bài toán bởi giới thiệu mới các biến và đẳng thức các ràng buộc như sau:
$$minimizef(y) = \log \begin{pmatrix} e^{yi} \end{pmatrix} \sum_{i=1}^{n}$$
$$subject to$$
$$Ax + b = y,$$
Ở đâu $A$ là ma trận cỡ $n \times  n$ có các cột là các vectơ $A^{i}$ và $b = (b , \dots  , b_{n})$. Vì
$$by Example 50.8(8), the conjugate of the \log-sum-\exp function f(y) = \log \sum_{i}^{1}  is$$
$$\begin{pmatrix} n & e^{yi} \\ =1 \end{pmatrix}$$
$$f^{*} (\mu ) =( \sum_{i}  n=1 \mu_{i}  \log \mu_{i} if 1^{\top}\mu  = 1 and \mu  \ge 0$$
$$\infty otherwise,$$
Đối ngẫu (dual) của reformulated bài toán có thể được biểu diễn dưới dạng
$$maximizeb^{\top}\mu  -\log \begin{pmatrix} \mu_{i}  \log \mu_{i} \end{pmatrix} \sum_{i=1}^{n}$$
$$subject to$$
$$1^{\top}\mu  = 1$$
$$A^{\top}\mu  = 0$$
$$\mu  \ge 0,$$
Entropy cực đại hóa bài toán.

> **Ví dụ 50.13.** Tương tự không ràng buộc chuẩn (norm) cực tiểu hóa bài toán
$$minimize\|Ax -b\|,$$
Ở đâu $\|\|$ là bất kỳ chuẩn (norm) trên $\mathbb{R}^{m}$, có đối ngẫu (dual) hàm mà là hằng số, và là không hữu ích. bài toán này có thể được reformulated như
$$minimize\|y\|$$
$$subject to$$
$$Ax -b = y.$$

<!-- PAGE 1846 -->
Bởi Ví dụ 50.8(6), liên hợp của chuẩn (norm) được cho bởi
$$($$
$$0if \|y\|^{D}\le 1$$
$$\|y\|^{*}=$$
$$+\infty otherwise,$$
Do đó đối ngẫu (dual) của reformulated bài toán quy hoạch là:
$$maximizeb^{\top}\mu$$
$$subject to$$
$$\|\mu \|^{D}\le 1$$
$$A^{\top}\mu  = 0.$$
Ở đây là bây giờ ví dụ của $(2)$, thay thế hàm mục tiêu (objective function) với tăng hàm của ban đầu hàm.

> **Ví dụ 50.14.** chuẩn (norm) cực tiểu hóa của Ví dụ 50.13 có thể được reformulated như
$$minimize \frac{1}{2} \|y\|^{2}$$
$$subject to$$
$$Ax -b = y.$$
Điều này bài toán quy hoạch là hiển nhiên tương đương đến ban đầu một. Bởi Ví dụ 50.8(7), liên hợp của square chuẩn (norm) được cho bởi
$$\frac{1}{2} \begin{pmatrix} \|y\|^{D2} \end{pmatrix} ,$$
Do đó đối ngẫu (dual) của reformulated bài toán quy hoạch là
$$maximize- \frac{1}{2} \begin{pmatrix} \|\mu \|^{D2} \end{pmatrix} + b^{\top}\mu$$
$$subject to$$
$$A^{\top}\mu  = 0.$$
Lưu ý rằng đối ngẫu (đối ngẫu (dual)) này là khác nhau từ đối ngẫu (dual) thu được trong Ví dụ 50.13. hàm mục tiêu (objective function) của đối ngẫu (dual) bài toán quy hoạch trong Ví dụ 50.13 là tuyến tính, nhưng ta có phi tuyến ràng buộc $\|\mu \|^{D} \le 1$. Mặt khác, hàm mục tiêu (objective function) của đối ngẫu (dual) bài toán quy hoạch của Ví dụ 50.14 là toàn phương, trong khi đó của nó các ràng buộc là afin. Ta có khác các ví dụ của điều này trade-offwith Các bài toán quy hoạch $(SVM_{h2})$ (toàn phương hàm mục tiêu (objective function), afin các ràng buộc), và $(SVM_{h1})$ (tuyến tính hàm mục tiêu (objective function), một phi tuyến ràng buộc). Đôi khi, nó là cũng helpful đến thay thế ràng buộc bởi tăng hàm của điều này ràng buộc; ví dụ, để sử dụng ràng buộc $\|w\|_{2}^{2} (= w^{\top}w) \le 1$ thay vì của $\|w\|_{2} \le 1$. Trong Chương $55$ ta revisit bài toán của việc giải quá xác định hoặc underdetermined hệ phương trình tuyến tính Ax $= b$ được xét trong Mục 23.1, từ khác nhau điểm của quan điểm.
