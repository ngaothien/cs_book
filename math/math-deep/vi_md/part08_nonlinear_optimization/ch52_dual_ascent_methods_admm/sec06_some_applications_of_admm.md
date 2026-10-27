# Một số Các ứng dụng của ADMM


<!-- PAGE 1927 -->
Ở trên suggests rằng reasonable termination tiêu chuẩn là rằng

$r^{k}$

Và

$s^{k}$

Nên là nhỏ, cụ thể là rằng
$$r^{k}

$\le \epsilon^{pri}$ và

$s^{k}$

$\le \epsilon^{dual}$,$$ for some chosen feasibility tolerances $\epsilon^{pri}$ and $\epsilon^{đối ngẫu (dual)}$ . Further discussion for choosing these parameters can be found in Boyd et al. $[28]$ (Section 3.3.1). Various extensions and variations of ADMM are discussed in Boyd et al. $[28]$ (Section 3.4). In order to accelerate convergence of the method, one may choose a different $\rho$  at each step (say $\rho^{k}$ ), although proving the convergence of such a method may be difficult. If we assume that $\rho^{k}$ trở thành hằng số sau số của các vòng lặp, thì chứng minh rằng ta gave vẫn áp dụng. đơn giản scheme là điều này:
$$\tau^{incr}  \rho^{k} if

$r^{k}$

$> \mu$

$s^{k}$$$
$$$$
$$ > \mu$$
$$\rho^{k+1} =\rho^{k} /\tau^{decr}  if

$s^{k}$



$r^{k}$$$
$$\rho^{k} otherwise,$$
$$$$
Ở đâu $\tau^{incr} > 1, \tau^{decr} > 1$, và $\mu  > 1$ là một số được chọn các tham số. Một lần nữa, ta refer interested độc giả đến Boyd et al. $[28]$ (Mục 3.4).

## 52.6 Một số Các ứng dụng của ADMM

Cấu trúc trong $f, g, A$, và $B$ có thể thường là exploited đến cho nhiều hơn/thêm efficient các phương pháp cho performing x-update và z-update. Ta focus trên x-update, nhưng thảo luận áp dụng chỉ cũng vậy đến z-update. Vì $z$ và $\lambda$ là held hằng số during cực tiểu hóa trên $x$, nó là nhiều hơn/thêm thuận tiện để sử dụng scaled tạo thành của ADMM. Nhắc lại rằng
$$x^{k+1}= arg minx \begin{pmatrix} f(x) + (\rho /2) & Ax + Bz^{k} -c + u_{2}^{k2} \end{pmatrix}$$
(ở đây ta sử dụng $u$ thay vì của $\mu$), do đó ta có thể biểu diễn x-update bước như
$$x^{+}= arg minx \begin{pmatrix} f(x) + (\rho /2) \|Ax -v\|_{2}^{2} \end{pmatrix} ,$$
Với $v = -Bz^{k} + c$ - $u^{k}$.

> **Ví dụ 52.7.** thứ nhất simplification phát sinh khi $A =$ I, trong mà trường hợp x-update là
$$x^{+}= arg minx \begin{pmatrix} f(x) + (\rho /2) \|x -v\|_{2}^{2} \end{pmatrix} = prox_{f,\rho}(v).$$
Ánh xạ $v \mapsto prox_{f,\rho}(v)$ là đã biết như proximity toán tử của $f$ với hình phạt (penalty) $\rho$. ở trên cực tiểu hóa là một cách tổng quát referred đến như proximal cực tiểu hóa.

<!-- PAGE 1928 -->

> **Ví dụ 52.8.** Khi hàm $f$ là đơn giản đủ, proximity toán tử có thể được được tính analytically. Điều này là trường hợp đặc biệt khi $f = I_{C}$, indicator hàm của khác rỗng đóng tập lồi (convex set) $C$. Trong trường hợp này, nó là dễ để xem rằng
$$x^{+}= arg minx \begin{pmatrix} I_{C}(x) + (\rho /2) \|x -v\|_{2}^{2} \end{pmatrix} = \Pi_{C} (v),$$
Phép chiếu trực giao (orthogonal projection) của $v$ lên $C$. Trong trường hợp đặc biệt khi $C =\mathbb{R}_{+}^{n}$ (thứ nhất orthant), thì
$$x^{+}= (v)_{+},$$
Vectơ thu được bằng cách đặt âm các thành phần của $v$ đến không.

> **Ví dụ 52.9.** trường hợp thứ hai ở đâu simplifications phát sinh là trường hợp ở đâu $f$ là lồi toàn phương phiếm hàm của tạo thành
$$f(x) = \frac{1}{2} x^{\top}Px + q^{\top}x + r,$$
$$\mathbb{R}^{n} \mathbb{R}$$
Ở đâu $P$ là $n \times  n$ đối xứng nửa xác định dương (positive semidefinite) ma trận, $q \in$ và $r \in$. Trong trường hợp này gradien của ánh xạ
$$x \mapsto f(x) + (\rho /2) \|Ax -v\|_{2}^{2} = \frac{1}{2} x^{\top}Px + q^{\top}x + r + \frac{\rho}{2} x^{\top}(A^{\top}A)x -\rho x^{\top}A^{\top}v + \frac{\rho}{2} v^{\top}v$$
Được cho bởi
$$(P + \rho A^{\top}A)x + q -\rho A^{\top}v,$$
Và vì $A$ có hạng (rank) $n$, ma trận $A^{\top}A$ là đối xứng xác định dương (SPD), do đó ta thu được
$$x^{+}= (P + \rho A^{\top}A))^{-1}(\rho A^{\top}v -q).$$
Các phương pháp từ số tuyến tính đại số có thể được được sử dụng do đó tính $x^{+}$ fairly efficiently; xem Boyd et al. $[28]$ (Mục $4)$.

> **Ví dụ 52.10.** trường hợp thứ ba ở đâu simplifications phát sinh là variation của trước đó trường hợp ở đâu $f$ là lồi toàn phương phiếm hàm của tạo thành
$$f(x) = \frac{1}{2} x^{\top}Px + q^{\top}x + r,$$
Ngoại trừ rằng $f$ là có ràng buộc bởi đẳng thức các ràng buộc Cx $= b$, như trong Mục 50.4, mà có nghĩa là
$$\mathbb{R}^{n}$$
Rằng dom(f) $= {x \in$ | Cx $= b}$, và $A =$ I. x-minimization bước bao gồm trong cực tiểu hóa hàm
$$J(x) = \frac{1}{2} x^{\top}Px + q^{\top}x + r + \frac{\rho}{2} x^{\top}x -\rho x^{\top}v + \frac{\rho}{2} v^{\top}v$$
Subject đến ràng buộc
$$Cx = b,$$

<!-- PAGE 1929 -->
Do đó bởi các kết quả của Mục 50.4, $x^{+}$ là thành phần của nghiệm của KKT-system
$$\begin{pmatrix} P+ \rho I & C^{\top} \\ C & 0 \end{pmatrix} \begin{pmatrix} x^{+} \\ y \end{pmatrix} = \begin{pmatrix} -q + \rho v \\ b \end{pmatrix} .$$
Ma trận $P + \rho$ I là đối xứng xác định dương (SPD), do đó KKT-matrix là khả nghịch. Ta có thể bây giờ mô tả cách mà ADMM được sử dụng để giải hai chung/phổ biến các bài tập của lồi tối ưu hóa.
$(1)$ Cực tiểu hóa của thực sự/đúng đắn đóng hàm lồi (convex function) $f$ trên đóng tập lồi (convex set) $C$ trong $\mathbb{R}^{n}$. Điều này là sau đây bài toán
$$minimizef(x)$$
$$subject to x \in C,$$
Mà có thể được được viết lại trong ADMM tạo thành như
$$minimizef(x) + I_{C}(z)$$
$$subject to x -z = 0.$$
Bằng cách sử dụng scaled đối ngẫu (dual) biến $u = \lambda /\rho$, augmented Hàm Lagrange (Lagrangian) là
$$.$$
$$L_{\rho}(x, z, u) = f(x) + I_{C}(z) + \frac{\rho}{2} \|x -z + u\|_{2}^{2} - \frac{\rho}{2} \|u\|^{2}$$
Xét theo Ví dụ 52.8, scaled tạo thành của ADMM cho bài toán này là
$$x^{k+1}= arg minx \begin{pmatrix} f(x) + (\rho /2) & x -z^{k} + u_{2}^{k2} \end{pmatrix}$$
$$z^{k+1}= \Pi_{C} (x^{k+1}+ u^{k})$$
$$u^{k+1}= u^{k}+ x^{k+1}-z^{k+1}.$$
X-update liên quan đến evaluating proximal toán tử. Lưu ý rằng hàm $f$ cần không là khả vi (differentiable). Của course, các phần tử này các cực tiểu hóa phụ thuộc vào có efficient tính toán các quy trình cho proximal toán tử và phép chiếu toán tử.
$(2)$ Toàn phương Quy hoạch, Phiên bản $1$. Ở đây bài toán là
$$minimize \frac{1}{2} x^{\top}Px + q^{\top}x + r$$
$$subject to Ax = b, x \ge 0,$$
Ở đâu $P$ là $n \times  n$ đối xứng nửa xác định dương (positive semidefinite) ma trận, $q \in \mathbb{R}^{n}, r \in \mathbb{R}$, và $A$ là một ma trận cỡ $m \times  n$ của hạng (rank) $m$.

<!-- PAGE 1930 -->
Ở trên bài toán quy hoạch được chuyển đổi trong ADMM tạo thành như sau:
$$minimizef(x) + g(z)$$
$$subject to x -z = 0,$$
Với
$$f(x) = \frac{1}{2} x^{\top}Px + q^{\top}x + r,dom(f) = {x \in \mathbb{R}^{n}| Ax = b},$$
Và
$$g = I_{Rn+},$$
Indicator hàm của dương $orthant\mathbb{R}_{+}^{n}$. Xét theo Ví dụ 52.8 và Ví dụ 52.10, scaled tạo thành của ADMM bao gồm của sau đây các bước:
$$x^{k+1}= arg minx \begin{pmatrix} f(x) + (\rho /2) & x -z^{k} + u_{2}^{k2} \end{pmatrix}$$
$$z^{k+1}= (x^{k+1}+ u^{k})_{+}$$
$$u^{k+1}= u^{k}+ x^{k+1}-z^{k+1}.$$
X-update liên quan đến việc giải KKT các phương trình
$$\begin{pmatrix} P+ \rho I & A^{\top} \\ A & 0 \end{pmatrix} \begin{pmatrix} x^{k+1} \\ y \end{pmatrix} = \begin{pmatrix} -q + \rho (z^{k} -u^{k}) \\ b \end{pmatrix} .$$
Điều này là quan trọng ví dụ bởi vì nó cung cấp một của tốt nhất các phương pháp cho việc giải toàn phương các bài tập, đặc biệt, SVM các bài tập được thảo luận trong Chương $54$.
$(3)$ Toàn phương Quy hoạch, Phiên bản $2$. bài toán này là đồng dạng đến trước đó một, ngoại trừ
$$\mathbb{R}^{n}$$
Rằng biến $x \in$ là không bị thu hẹp là không âm. bài toán là
$$minimize \frac{1}{2} x^{\top}Px + q^{\top}x + r$$
$$subject to Ax = b,$$
Ở đâu $P$ là $n \times  n$ đối xứng nửa xác định dương (positive semidefinite) ma trận, $q \in \mathbb{R}^{n}, r \in \mathbb{R}$, và $A$ là một ma trận cỡ $m \times  n$ của hạng (rank) $m$. ở trên bài toán quy hoạch được chuyển đổi trong ADMM tạo thành như sau:
$$minimizef(x) + g(z)$$
$$subject to x -z = 0,$$
Với
$$f(x) = \frac{1}{2} x^{\top}Px + q^{\top}x + r,dom(f) = {x \in \mathbb{R}^{n}| Ax = b},$$

<!-- PAGE 1931 -->
Và
$$g = 1,$$
Hằng số hàm mà là indicator hàm của tập lồi (convex set) $C = \mathbb{R}^{n}$. Xét theo Ví dụ 52.8 và $(1)$, vì $\Pi_{Rn} (x^{k+1} + u^{k}) = x^{k+1} + u^{k}$, scaled tạo thành của ADMM bao gồm của sau đây các bước:
$$x^{k+1}= arg minx \begin{pmatrix} f(x) + (\rho /2) & x -z^{k} + u_{2}^{k2} \end{pmatrix}$$
$$z^{k+1}= x^{k+1}+ u^{k}$$
$$u^{k+1}= u^{k}+ x^{k+1}-z^{k+1}= 0,$$
Với mọi $k \ge 0$, do đó
$$u^{k}= 0$$
$$z^{k+1}= x^{k+1}$$
Với mọi $k \ge 1$. Hệ quả là ta có
$$x^{k+1}= arg minx \begin{pmatrix} f(x) + (\rho /2) & x -z^{k} + u_{2}^{k2} \end{pmatrix}$$
$$z^{k+1}= x^{k+1}+ u^{k}$$
$$u^{1}= 0,$$
Cho $k = 0, 1$, và cho $k \ge 2$ ta có $u^{k} = 0$ và $z^{k} = x^{k}$, với
$$x^{k+1}= arg minx \begin{pmatrix} f(x) + (\rho /2) & x -x_{2}^{k2} \end{pmatrix} .$$
Như trước, x-update liên quan đến việc giải KKT các phương trình
$$\begin{pmatrix} P+ \rho I & A^{\top} \\ A & 0 \end{pmatrix} \begin{pmatrix} x^{k+1} \\ y \end{pmatrix} = \begin{pmatrix} -q + \rho (z^{k} -u^{k}) \\ b \end{pmatrix} ,$$
Với $u^{k} = 0$ nếu $k \ge 1$ và $z^{k} = x^{k}$ nếu $k \ge 2$. Ta programmed ở trên phương pháp trong Matlab như hàm qsolve1, xem Phụ lục $B$, Mục B.1. Ở đây là hai các ví dụ.

> **Ví dụ 52.11.** Xét toàn phương bài toán quy hoạch cho mà
$$P_{1} = \begin{pmatrix} 4 & 1 & 0 \\ 1 & 4 & 1 \\ 0 & 1 & 4 \end{pmatrix} q_{1} = - \begin{pmatrix} 4 \\ 4 \\ 4 \end{pmatrix}$$
$$A_{1} = \begin{pmatrix} 1 & 1 & -1 \\ 1 & -1 & -1 \end{pmatrix} b_{1} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} .$$
