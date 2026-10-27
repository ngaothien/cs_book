# Các bài tập


<!-- PAGE 1534 -->
$$\mathbb{R}^{n}$$
Ở đâu $\nabla J(x_{k})$ là gradien của $J$ tại $x_{k}$ (ở đây, ta đồng nhất E' với). Đặc biệt, Newton’s ban đầu phương pháp chọn $A_{k} =$ J'', và vòng lặp bước là của tạo thành
$$x_{k+1} = x_{k} -(\nabla^{2} J(x_{k}))^{-1}\nabla J(x_{k}),k \ge 0,$$
Ở đâu $\nabla^{2} J(x_{k})$ là Hessian của $J$ tại $x_{k}$.

> **Ví dụ 41.3.** Cho chúng ta áp dụng Newton’s ban đầu phương pháp đến hàm $J$ cho trước bởi J(x) $= 1$ - - $x^{3}$ 4x. Ta có J'(x) $= x^{2} 4$ và J''(x) $=$ 2x, do đó Newton bước được cho bởi $\overline{3}$
$$-$$
$$x_{k+1} = x_{k} - \frac{x_{k}^{2}4}{2x_{k}} = \frac{1}{2} \begin{pmatrix} 4 \\ x_{k} + \\ x_{k} \end{pmatrix} .$$
Điều này là dãy của Ví dụ 41.1 để tính square nghiệm (root) của $4$. Bắt đầu với bất kỳ $x_{0} > 0$ nó hội tụ rất quickly đến $2$. Như được nhận xét trong Ciarlet $[41]$ (Mục 7.5), suy rộng/tổng quát hóa Newton các phương pháp có rất wide miền giá trị (range) của applicability. Ví dụ, khác nhau các phiên bản của hạ gradien (gradient descent) các phương pháp có thể được được quan điểm như instances của Newton phương pháp. Xem Mục 49.9 cho ví dụ. Newton’s phương pháp cũng đóng quan trọng vai trò trong lồi tối ưu hóa, đặc biệt, interior-point các phương pháp. biến thể của Newton’s phương pháp dealing với đẳng thức các ràng buộc có đã được developed. Ta refer độc giả đến Boyd và Vandenberghe $[29]$, Các chương $10$ và $11$, cho toàn diện trình bày của các phần tử này topics.

## 41.3 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Newton’s phương pháp cho các hàm $f$: $\mathbb{R} \to \mathbb{R}. \bullet$ Suy rộng/tổng quát hóa Newton các phương pháp. $\bullet$ Newton-Kantorovich định lý.

## 41.4 Các bài tập

Bài toán 41.1. Nếu $\alpha  > 0$ và f(x) $= x^{2}$ - $\alpha$, Newton’s phương pháp cho ta dãy
$$x_{k+1} = \frac{1}{2} \begin{pmatrix} \alpha \\ x_{k} + \\ x_{k} \end{pmatrix}$$
$$\sqrt$$
Để tính square nghiệm (root) $\overline{\alpha}$ của $\alpha$.

<!-- PAGE 1535 -->
$(1)$ Chứng minh rằng nếu $x_{0} > 0$, thì $x_{k} > 0$ và
$$\sqrt\sqrt$$
$$x_{k+1} -\overline{\alpha} = \frac{1}{2x_{k}} (x_{k} -\overline{\alpha})^{2}$$
$$x_{k+2} -x_{k+1} = \frac{1}{2x_{k+1}} (\alpha  -x_{k+1}^{2})$$
$$\sqrt$$
Với mọi $k \ge 0$. Suy ra rằng Newton’s phương pháp hội tụ đến $\overline{\alpha}$ với mọi $x_{0} > 0$.
$$\sqrt$$
$(2)$ Chứng minh rằng nếu $x_{0} < 0$, thì Newton’s phương pháp hội tụ đến - $\overline{\alpha}$.
Bài toán 41.2. $(1)$ Nếu $\alpha  > 0$ và f(x) $= x^{2}$ - $\alpha$, chỉ ra rằng các điều kiện của Định lý 41.1 được thỏa mãn bởi bất kỳ $\beta  \in (0, 1)$ và bất kỳ $x_{0}$ sao cho
$$-$$
$$|x_{0}^{2} -\alpha | \le \frac{4\beta (1\beta )}{(\beta  + 2)^{2}} x_{0}^{2},$$
Với
$$r = \frac{\beta}{\beta  + 2} x_{0},M = \frac{\beta  + 2}{4x_{0}} .$$
$(2)$ Chứng minh rằng cực đại của hàm được định nghĩa trên $[0, 1]$ bởi
$$-$$
$$\beta  \mapsto \frac{4\beta (1\beta )}{(\beta  + 2)^{2}}$$
Có cực đại cho $\beta  = 2/5$. Cho giá trị này của $\beta$, kiểm tra rằng $r = (1/6)x_{0}, M = 3/(5x_{0})$, và
$$\frac{6}{7} \alpha  \le x_{0}^{2} \le \frac{6}{5} \alpha .$$
Bài toán 41.3. Xét generalizing Bài toán 41.1 đến ma trận hàm $f$ cho trước bởi f(X) $= X^{2}$ - $C$, ở đâu $X$ và $C$ là hai thực $n \times  n$ các ma trận với $C$ đối xứng xác định dương (SPD). bước thứ nhất là để xác định cho mà $A$ thực hiện nghịch đảo $df_{A}^{-1}$ tồn tại. Cho $g$ là hàm cho trước bởi g(X) $= X^{2}$. Từ Bài toán 39.1 ta biết rằng đạo hàm tại $A$ của hàm $g$ là $dg_{A}(X) = AX + XA$, và hiển nhiên $df_{A} = dg_{A}$. Do đó ta là đã dẫn đến đến hình ra khi tuyến tính ma trận ánh xạ $X \mapsto AX + XA$ là khả nghịch. Điều này có thể được được thực hiện bằng cách sử dụng Kronecker tích. Cho trước một ma trận cỡ $m \times  n$ $A = (a_{ij})$ và một ma trận cỡ $p \times  q$ $B = (b_{ij})$, Kronecker tích (hoặc tích tenxơ (tensor product)) $A \otimes B$ của $A$ và $B$ là mp $\times$ nq ma trận
$$A \otimes B = \begin{pmatrix} a_{11}B & a_{12}B & \cdots & a_{1n}B \\ a_{21}B & a_{22}B & \cdots & a_{2n}B \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1}B & a_{m2}B & \cdots & a_{mn}B \end{pmatrix} .$$

<!-- PAGE 1536 -->
Nó có thể được được hiển thị (và bạn có thể sử dụng các phần tử này các sự kiện mà không có chứng minh) rằng $\otimes$ là kết hợp và rằng
$$(A \otimes B)(C \otimes D) = AC \otimes BD$$
$$(A \otimes B)^{\top}= A^{\top}\otimes B^{\top},$$
Bất cứ khi nào AC và BD là tốt được định nghĩa. Cho trước bất kỳ ma trận cỡ $n \times  n$ $X$, cho vec(X) là vectơ trong $\mathbb{R}^{n2}$ thu được bởi concatenating các hàng của $X$.
$(1)$ Chứng minh rằng $AX = Y$ khi và chỉ khi
$$(A \otimes I_{n})vec(X) = vec(Y )$$
Và $XA = Y$ khi và chỉ khi
$$(I_{n} \otimes A^{\top})vec(X) = vec(Y ).$$
Suy ra rằng $AX + XA = Y$ khi và chỉ khi
$$((A \otimes I_{n}) + (I_{n} \otimes A^{\top}))vec(X) = vec(Y ).$$
Trong trường hợp ở đâu $n = 2$ và nếu ta viết
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} ,$$
Kiểm tra rằng
$$A \otimes I_{2} + I_{2} \otimes A^{\top}= \begin{pmatrix} 2a & c & b & 0 \\ b & a + d & 0 & b \\ c & 0 & a + d & c \\ 0 & c & b & 2d \end{pmatrix} .$$
Bài toán là để xác định khi ma trận $(A \otimes I_{n}) + (I_{n} \otimes A^{\top})$ là khả nghịch.
Nhận xét: phương trình $AX + XA = Y$ là đặc biệt trường hợp của phương trình $AX + XB = C$ (đôi khi được viết $AX$ - $XB = C)$, được gọi là Sylvester phương trình, ở đâu $A$ là một ma trận cỡ $m \times  m$, $B$ là một ma trận cỡ $n \times  n$, và $X, C$ là $m \times  n$ các ma trận; xem Higham $[94]$ (Phụ lục $B)$.
$(2)$ Trong trường hợp ở đâu $n = 2$, chứng minh rằng
$$\det(A \otimes I_{2} + I_{2} \otimes A^{\top}) = 4(a + d)^{2}(ad -bc).$$
$(3)$ Cho $A$ và $B$ là bất kỳ hai $n\times n$ phức các ma trận. Sử dụng Schur các nhân tử hóa $A = UT_{1}U^{*}$ và $B = V T_{2}V^{*}$ (ở đâu $U$ và $V$ là unita và $T_{1}, T_{2}$ là tam giác trên (upper-triangular)) để chứng minh rằng nếu $\lambda_{1} , \dots  , \lambda_{n}$ là các trị riêng (eigenvalues) của $A$ và $\mu_{1} , \dots  , \mu_{n}$ là các trị riêng (eigenvalues) của $B$, thì các vô hướng $\lambda_{i} \mu_{j}$ là các trị riêng (eigenvalues) của $A \otimes B$, cho $i, j = 1, \dots  , n$. Hint. Kiểm tra rằng $U \otimes V$ là unita và rằng $T_{1} \otimes T_{2}$ là tam giác trên (upper triangular).

<!-- PAGE 1537 -->
$(4)$ Chứng minh rằng các trị riêng (eigenvalues) của $(A \otimes I_{n}) + (I_{n} \otimes B)$ là các vô hướng $\lambda_{i}  + \mu_{j}$, cho $i, j = 1, \dots  , n$. Suy ra rằng các trị riêng (eigenvalues) của $(A \otimes I_{n}) + (I_{n} \otimes A^{\top})$ là $\lambda_{i}  + \lambda_{j}$, cho $i, j = 1, \dots  , n$. Do đó $(A\otimes I_{n})+(I_{n} \otimes A^{\top})$ là khả nghịch khi và chỉ khi $\lambda_{i}  +\lambda_{j}  \neq  0$, cho $i, j = 1, \dots  , n$. Đặc biệt, chứng minh rằng nếu $A$ là đối xứng xác định dương (SPD), thì do đó là $(A \otimes I_{n}) + (I_{n} \otimes A^{\top})$. Hint. Sử dụng $(3)$.
$(5)$ Chứng minh rằng nếu $A$ và $B$ là đối xứng và $(A \otimes I_{n}) + (I_{n} \otimes A^{\top})$ là khả nghịch, thì duy nhất nghiệm $X$ của phương trình $AX + XA = B$ là đối xứng.
$(6)$ Bắt đầu với đối xứng xác định dương (SPD) ma trận $X_{0}$, tổng quát bước của Newton’s phương pháp là
$$X_{k+1} = X_{k} -(f_{Xk}' )^{-1}(X_{k}^{2} -C) = X_{k} -(g_{Xk}')^{-1}(X_{k}^{2} -C),$$
Và vì $g_{Xk}'$ là tuyến tính, điều này là tương đương đến
$$X_{k+1} = X_{k} -(g_{Xk}')^{-1}(X_{k}^{2}) + (g_{Xk}')^{-1}(C).$$
Nhưng vì $X_{k}$ là SPD, $(g_{Xk}')^{-1}(X_{k}^{2})$ là duy nhất nghiệm của
$$X_{k}Y + Y X_{k} = X_{k}^{2}$$
Có nghiệm là hiển nhiên $Y = (1/2)X_{k}$. Vì vậy Newton bước là
$$X_{k+1} = X_{k} -(g_{Xk}')^{-1}(X_{k}^{2}) + (g_{Xk}')^{-1}(C) = X_{k} - \frac{1}{2} X_{k} + (g_{Xk}')^{-1}(C) = \frac{1}{2} X_{k} + (g_{Xk}')^{-1}(C),$$
Do đó ta có
$$X_{k+1} = \frac{1}{2} X_{k} + (g_{Xk}')^{-1}(C) = (g_{Xk}')^{-1}(X_{k}^{2} + C).$$
Chứng minh rằng nếu $X_{k}$ và $C$ là đối xứng xác định dương (SPD), thì $(g_{Xk}')^{-1}(C)$ là đối xứng xác định dương (SPD), và nếu $C$ là đối xứng nửa xác định dương (positive semidefinite), thì $(g_{Xk}')^{-1}(C)$ là đối xứng nửa xác định dương (positive semidefinite). Hint. Bởi $(5)$ duy nhất nghiệm $Z$ của phương trình $X_{k}Z +ZX_{k} = C$ (ở đâu $C$ là đối xứng) là đối xứng do đó nó có thể được được chéo hóa như $Z = QDQ^{\top}$ với $Q$ trực giao và $D$ thực ma trận đường chéo (diagonal matrix). Chứng minh rằng
$$Q^{\top}X_{k}QD + DQ^{\top}X_{k}Q = Q^{\top}CQ,$$
Và giải hệ bằng cách sử dụng đường chéo các phần tử. Suy ra rằng nếu $X_{k}$ và $C$ là SPD, thì $X_{k+1}$ là SPD. Vì $C = P\Sigma P^{\top}$ là SPD, nó có SPD square nghiệm (root) (thực ra duy nhất) $C^{1/2} = P\Sigma^{1/2} P^{\top}$. Chứng minh rằng
$$X_{k+1} -C^{1/2}= (g_{Xk}')^{-1}(X_{k} -C^{1/2})^{2}.$$
Chứng minh rằng
$$(g_{Xk}')_{2}^{-1}

$\ge \frac{1}{2 \|X_{k}\|_{2}}$.$$

<!-- PAGE 1538 -->
Mở bài toán: Thực hiện Định lý 41.1 áp dụng với một số phù hợp $r, M, \beta$?
$(7)$ Chứng minh rằng nếu $C$ và $X_{0}$ giao hoán, miễn là/được cung cấp rằng phương trình $X_{k}Z + ZX_{k} = C$ có duy nhất nghiệm với mọi $k$, thì $X_{k}$ và $C$ giao hoán với mọi $k$ và $Z$ được cho bởi
$$Z = \frac{1}{2} X_{k}^{-1} C = \frac{1}{2} CX_{k}^{-1} .$$
Suy ra rằng
$$X_{k+1} = \frac{1}{2} (X_{k} + X_{k}^{-1} C) = \frac{1}{2} (X_{k} + CX_{k}^{-1} ).$$
Điều này là tương tự ma trận của công thức cho trước trong Bài toán 41.1(1). Chứng minh rằng nếu $C$ và $X_{0}$ có dương các trị riêng (eigenvalues) và $C$ và $X_{0}$ giao hoán, thì $X_{k+1}$ có dương các trị riêng (eigenvalues) với mọi $k \ge 0$ và do đó dãy $(X_{k})$ được định nghĩa. Hint. Bởi vì $X_{k}$ và $C$ giao hoán, $X_{k}^{-1}$ và $C$ giao hoán, và hiển nhiên $X_{k}$ và $X_{k}^{-1}$ giao hoán. Theo Mệnh đề 31.9, $X_{k}, X_{k}^{-1}$, và $C$ là triangulable trong chung/phổ biến cơ sở (basis), do đó tồn tại một ma trận trực giao (orthogonal matrix) $P$ và một số tam giác trên (upper-triangular) các ma trận $T_{1}, T_{2}$ sao cho
$$X_{k} = PT_{1}P^{\top} ,X_{k}^{-1}= PT_{1}^{-1}  P^{\top},C = PT_{2}P^{\top} .$$
Suy ra rằng
$$X_{k+1} = \frac{1}{2} P(T_{1} + T_{1}^{-1} T_{2})P^{\top}.$$
Cũng nhắc lại rằng đường chéo các phần tử (entries) của tam giác trên (upper-triangular) ma trận là các trị riêng (eigenvalues) của rằng ma trận. Ta giả thuyết rằng nếu $C$ có dương các trị riêng (eigenvalues), thì Newton dãy hội tụ bắt đầu với bất kỳ $X_{0}$ của tạo thành $X_{0} = \mu I_{n}$, với $\mu  > 0$.
$(8)$ Cài đặt ở trên phương pháp trong Matlab (có một command kron(, $B)$ đến tạo thành Kronecker tích của $A$ và $B)$. Test của bạn bài toán quy hoạch trên chéo hóa được (diagonalizable) và nondiagonalizable các ma trận, bao gồm cả
$$W = \begin{pmatrix} 10 & 7 & 8 & 7 \\ 7 & 5 & 6 & 5 \\ 8 & 6 & 10 & 9 \\ 7 & 5 & 9 & 10 \end{pmatrix} ,A_{1} = \begin{pmatrix} 5 & 4 & 1 & 1 \\ 4 & 5 & 1 & 1 \\ 1 & 1 & 4 & 2 \\ 1 & 1 & 2 & 4 \end{pmatrix} ,$$
Và
$$A_{2} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ -1 & 0.01 & 0 & 0 \\ -1 & -1 & 100 & 100 \\ 1 & 1 & 100 & 100 \end{pmatrix} ,A_{3} = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 \end{pmatrix} ,A_{4} = \begin{pmatrix} 1 & -1 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 1 & 1 \end{pmatrix} .$$
$$---$$
Những gì xảy ra với
$$C = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} ,X_{0} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} .$$

<!-- PAGE 1539 -->
Bài toán của xác định khi square các nghiệm của các ma trận tồn tại và các quy trình cho việc tìm chúng là một cách kỹ lưỡng investigated trong Higham $[94]$ (Chương $6)$.
Bài toán 41.4. $(1)$ Chỉ ra rằng Newton’s phương pháp ứng dụng đến hàm
$$f(x) = \alpha  - \frac{1}{x}$$
Với $\alpha  \neq  0$ và $x \in \mathbb{R} -{0}$ cho ta dãy $(x_{k})$ với
$$x_{k+1} = x_{k}(2 -\alpha x_{k}),k \ge 0.$$
$(2)$ Nếu ta cho $r_{k} = 1$ - $\alpha x_{k}$, chứng minh rằng $r_{k+1} = r_{k}^{2}$ với mọi $k \ge 0$. Suy ra rằng Newton’s phương pháp hội tụ đến $1/\alpha$ nếu $0 < \alpha x_{0} < 2$.
Bài toán 41.5. $(1)$ Chỉ ra rằng Newton’s phương pháp ứng dụng đến ma trận hàm
$$f(X) = A -X^{-1},$$
Với $A$ và $X$ khả nghịch $n \times  n$ các ma trận và được bắt đầu với bất kỳ ma trận cỡ $n \times  n$ $X_{0}$ cho ta dãy $(X_{k})$ với
$$X_{k+1} = X_{k}(2I -AX_{k}),k \ge 0.$$
$(2)$ Nếu ta cho $R_{k} =$ I - $AX_{k}$, chứng minh rằng
$$R_{k+1} = I -(I -R_{k})(I + R_{k}) = R_{k}^{2}$$
Với mọi $k \ge 0$. Suy ra rằng Newton’s phương pháp hội tụ đến $A^{-1}$ khi và chỉ khi bán kính phổ (spectral radius) của I - $AX_{0}$ là chặt nhỏ hơn hơn $1$, nghĩa là, $\rho$ (I - $AX_{0}) < 1$.
$(3)$ Giả sử rằng $A$ là đối xứng xác định dương (SPD) và cho $X_{0} = \mu$ I. Chứng minh rằng điều kiện $\rho$ (I - $AX_{0}) < 1$ là tương đương đến
$$0 < \mu  < \frac{2}{\rho (A)} .$$
$(4)$ Viết Matlab bài toán quy hoạch cài đặt Newton’s phương pháp specified trong $(1)$. Test của bạn bài toán quy hoạch với ma trận cỡ $n \times  n$
$$A_{n} = \begin{pmatrix} 2 & -1 & 0 & \cdots & 0 \\ -1 & 2 & -1 & \dots & 0 \\ \vdots & \ddots & \ddots & \ddots & \vdots \\ 0 & \cdots & -1 & 2 & -1 \\ 0 & \cdots & 0 & -1 & 2 \end{pmatrix} ,$$
Và với $X_{0} = \mu I_{n}$, cho khác nhau các giá trị của $n$, bao gồm cả $n = 8, 10, 20$, và khác nhau các giá trị của $\mu$ sao cho $0 < \mu  \le 1/2$. Tìm một số $\mu  > 1/2$ causing divergence.

<!-- PAGE 1540 -->
$$\mathbb{R}$$
Bài toán 41.6. phương pháp cho việc tính toán thứ $n$ nghiệm (root) $x^{1/n}$ của dương thực số $x \in$, với $n \in \mathbb{N}$ dương số nguyên $n \ge 2$, tiến hành như sau: định nghĩa dãy $(x_{k})$, ở đâu $x_{0}$ là bất kỳ được chọn dương thực, và
$$x_{k+1} = \frac{1}{n} \begin{pmatrix} x \\ (n -1)x_{k} + \\ x_{k}^{n-1} \end{pmatrix} ,k \ge 0.$$
$(1)$ Cài đặt ở trên phương pháp trong Matlab và test nó cho khác nhau input các giá trị của $x, x_{0}$, và của $n \ge 2$, bởi chạy successively của bạn bài toán quy hoạch cho $m = 2, 3, \dots  , 100$ các vòng lặp. Có của bạn bài toán quy hoạch plot các điểm $(i, x_{i})$ đến watch cách mà quickly dãy hội tụ. Experiment với khác nhau các lựa chọn của $x_{0}$. Một của các phần tử này các lựa chọn nên là $x_{0} = x$. Compare của bạn các câu trả lời với kết quả của áp dụng của Matlab hàm $x \mapsto x^{1/n}$. Trong một số trường hợp, khi $x_{0}$ là nhỏ, số của các vòng lặp có là ít nhất $1000$. Exhibit điều này behavior.
Bài toán 41.7. Refer đến Bài toán 41.6 cho định nghĩa của dãy $(x_{k})$.
$(1)$ Định nghĩa tương đối sai số $\epsilon_{k}$ như
$$\epsilon_{k}  = \frac{x_{k}}{x^{1/n}} -1,k \ge 0.$$
Chứng minh rằng
$$\epsilon_{k+1}  = \frac{x^{(1-1/n)}}{nx_{k}^{n-1}} \begin{pmatrix} (n -1)x_{k}^{n} & nx_{k}^{n-1} \\ - & + 1 \\ x & x^{(1-1/n)} \end{pmatrix} ,$$
Và thì rằng
$$\epsilon_{k+1}  = \frac{1}{n(\epsilon_{k}  + 1)^{n-1}} \begin{pmatrix} \epsilon_{k} (\epsilon_{k}  + 1)^{n-2}((n -1)\epsilon_{k}  + (n -2)) + 1 -(\epsilon_{k}  + 1)^{n-2} \end{pmatrix} ,$$
Với mọi $k \ge 0$.
$(2)$ Vì
$$\epsilon_{k}  + 1 = \frac{x_{k}}{x^{1/n}} ,$$
Và vì ta được giả sử $x_{0}, x > 0$, ta có $\epsilon_{0}  + 1 > 0$. Ta sẽ like để chứng minh rằng
$$\epsilon_{k}  \ge 0,for allk \ge 1.$$
Cho điều này xét variations của hàm $f$ cho trước bởi
$$f(u) = (n -1)u^{n}-nx^{1/n}u^{n-1}+ x,$$
Cho $u \in \mathbb{R}$. Sử dụng ở trên để chứng minh rằng f(u) $\ge 0$ với mọi $u \ge 0$. Kết luận rằng
$$\epsilon_{k}  \ge 0,for allk \ge 1.$$

<!-- PAGE 1541 -->
$(3)$ Chứng minh rằng nếu $n = 2$, thì
$$0 \le \epsilon_{k+1}  = \frac{\epsilon_{k}^{2}}{2(\epsilon_{k}  + 1)} ,for allk \ge 0,$$
Khác nếu $n \ge 3$, thì
$$-$$
$$0 \le \epsilon_{k+1}  \le \frac{(n1)}{n} \epsilon_{k} ,for allk \ge 1.$$
Chứng minh rằng dãy $(x_{k})$ hội tụ đến $x^{1/n}$ với mọi ban đầu giá trị $x_{0} > 0$.
$(4)$ Khi $n = 2$, ta đã thấy trong Bài toán 41.7(3) rằng
$$0 \le \epsilon_{k+1}  = \frac{\epsilon_{k}^{2}}{2(\epsilon_{k}  + 1)} ,for allk \ge 0.$$
Cho $n = 3$, chứng minh rằng
$$\epsilon_{k+1}  = \frac{2\epsilon_{k}^{2} (3/2 + \epsilon_{k} )}{3(\epsilon_{k}  + 1)^{2}} ,for allk \ge 0,$$
Và cho $n = 4$, chứng minh rằng
$$\epsilon_{k+1}  = \frac{3\epsilon_{k}^{2}}{4(\epsilon_{k}  + 1)^{3}} \begin{pmatrix} 2 + (8/3)\epsilon_{k}  + \epsilon_{k}^{2} \end{pmatrix} ,for allk \ge 0.$$
Cho $\mu_{3}$ và $\mu_{4}$ là các hàm cho trước bởi
$$\mu_{3} (a) = \frac{3}{2} + a$$
$$\mu_{4} (a) = 2 + \frac{8}{3} a + a^{2},$$
Sao cho nếu $n = 3$, thì
$$\epsilon_{k+1}  = \frac{2\epsilon_{k}^{2} \mu_{3} (\epsilon_{k} )}{3(\epsilon_{k}  + 1)^{2}} ,for allk \ge 0,$$
Và nếu $n = 4$, thì
$$\epsilon_{k+1}  = \frac{3\epsilon_{k}^{2} \mu_{4} (\epsilon_{k} )}{4(\epsilon_{k}  + 1)^{3}} ,for allk \ge 0.$$
Chứng minh rằng
$$a\mu_{3} (a) \le (a + 1)^{2}-1,for alla \ge 0,$$
Và
$$a\mu_{4} (a) \le (a + 1)^{3}-1,for alla \ge 0.$$
Cho $\eta_{3,k}  = \mu_{3} (\epsilon_{1} )\epsilon_{k}$ khi $n = 3$, và $\eta_{4,k}  = \mu_{4} (\epsilon_{1} )\epsilon_{k}$ khi $n = 4$. Chứng minh rằng
$$\eta_{3,k+1}  \le \frac{2}{3} \eta_{3,k}^{2} ,for allk \ge 1,$$

<!-- PAGE 1542 -->
Và
$$\eta_{4,k+1}  \le \frac{3}{4} \eta_{4,k}^{2} ,for allk \ge 1.$$
Suy ra từ ở trên rằng tốc độ của sự hội tụ của $\eta_{i,k}$ là rất fast, cho $i = 3, 4$ (và $k \ge 1)$.
Nhận xét: Nếu ta cho $\mu_{2} (a) = a$ với mọi và $\eta_{2,k}  = \epsilon_{k}$, ta thì được chứng minh rằng
$$\eta_{2,k+1}  \le \frac{1}{2} \eta_{2,k}^{2} ,for allk \ge 1.$$
Bài toán 41.8. Điều này là continuation của Bài toán 41.7.
$(1)$ Chứng minh rằng với mọi $n \ge 2$, ta có
$$\epsilon_{k+1}  = \begin{pmatrix} n -1 \\ n \end{pmatrix} \frac{\epsilon_{k}^{2} \mu_{n} (\epsilon_{k} )}{(\epsilon_{k}  + 1)^{n-1}} ,for allk \ge 0,$$
Ở đâu $\mu_{n}$ được cho bởi
$$\mu_{n} (a) = \frac{1}{2} n + \sum_{j=1}^{n-4}  \frac{1}{n -1} \begin{pmatrix} n -2 \\ (n -1) \\ j \end{pmatrix} \begin{pmatrix} n -2 \\ + (n -2) \\ j + 1 \end{pmatrix} \begin{pmatrix} n -2 \\ - \\ j + 2 \end{pmatrix} \begin{pmatrix}\end{pmatrix} a^{j}$$
$$+ \frac{n(n2)}{n -1} - a^{n-3} + a^{n-2}.$$
Hơn nữa, chứng minh rằng $\mu_{n}$ có thể được biểu diễn dưới dạng
$$\mu_{n} (a) = \frac{1}{2} n + \frac{n(n2)}{3} -a + \sum_{j=2}^{n-4}  \frac{(j + 1)n}{(j + 2)(n -1)} \begin{pmatrix} n -1 \\ j + 1 \end{pmatrix} a^{j} + \frac{n(n2)}{n -1} - a^{n-3} + a^{n-2}.$$
$(2)$ Chứng minh rằng với mọi $j$, với $1 \le j \le n$ - $1$, hệ số của $a^{j}$ trong $a\mu_{n}$ () là ít hơn hoặc bằng hệ số của $a^{j}$ trong $(a + 1)^{n-1}$ - $1$, và do đó
$$a\mu_{n} (a) \le (a + 1)^{n-1}-1,for alla \ge 0,$$
Với chặt bất đẳng thức nếu $n \ge 3$. Thực ra, chứng minh rằng nếu $n \ge 3$, thì với mọi $j$, với $3 \le j \le$ n-2, hệ số của $a^{j}$ trong $a\mu_{n}$ () là chặt ít hơn hệ số của $a^{j}$ trong $(a+1)^{n-1}-1$, và nếu $n \ge 4$, điều này cũng nghiệm đúng cho $j = 2$. Cho $\eta_{n,k}  = \mu_{n} (\epsilon_{1} )\epsilon_{k}  (n \ge 2)$. Chứng minh rằng
$$\eta_{n,k+1}  \le \begin{pmatrix} n -1 \\ n \end{pmatrix} \eta_{n,k}^{2} ,for allk \ge 1.$$
