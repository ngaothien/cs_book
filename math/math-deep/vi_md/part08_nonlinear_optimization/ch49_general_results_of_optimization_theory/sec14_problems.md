# Các bài tập


<!-- PAGE 1758 -->
$\bullet$ Newton’s phương pháp. $\bullet$ Newton bước. $\bullet$ Newton decrement. $\bullet$ Damped Newton phase. $\bullet$ Quadratically convergent phase. $\bullet$ Tự tương hợp (self-concordant) các hàm. $\bullet$ Gradien liên hợp (conjugate gradient) phương pháp. $\bullet$ Projected gradien các phương pháp. $\bullet$ Hình phạt (penalty) các phương pháp.

## 49.14 Các bài tập

$$\mathbb{R}^{n} \mathbb{R}$$
Bài toán 49.1. Xét hàm $J$: $\to$ cho trước bởi
$$J(v) = \frac{1}{2} \langle Av, v\rangle -\langle b, v\rangle + g(v),$$
$$\mathbb{R}^{n} \mathbb{R}^{n} \mathbb{R}$$
Ở đâu $A$ là thực $n \times  n$ đối xứng xác định dương (SPD) ma trận, $b \in$, và $g: \to$ là liên tục (không nhất thiết khả vi (differentiable)) hàm lồi (convex function) sao cho g(v) $\ge 0$ với mọi $v \in \mathbb{R}^{n}$, và cho $U$ là khác rỗng, bị chặn, đóng, lồi tập con của $\mathbb{R}^{n}$.
$(1)$ Chứng minh rằng tồn tại duy nhất một phần tử $u \in U$ sao cho
$$J(u) = \inf J(v).$$
$$v\in U$$
Hint. Chứng minh rằng $J$ là lồi chặt (strictly convex) trên $\mathbb{R}^{n}$.
$(2)$ Kiểm tra rằng
$$J(v) -J(u) = \langle Au -b, v -u\rangle + g(v) -g(u) + \frac{1}{2} \langle A(v -u), v -u\rangle .$$
Chứng minh rằng phần tử $u \in U$ cực tiểu hóa $J$ trong $U$ khi và chỉ khi
$$\langle Au -b, v -u\rangle + g(v) -g(u) \ge 0for all v \in U.$$
$$\mathbb{R}$$
Bài toán 49.2. Xét $n$ từng khúc $C^{1}$ các hàm $\phi_{i}$: $[0, 1] \to$ và giả sử rằng các hàm này là độc lập tuyến tính (linearly independent) và rằng
$$\sum_{i=1}^{n}  \phi_{i} (x) = 1for all x \in [0, 1].$$

<!-- PAGE 1759 -->
$$\mathbb{R}^{n} \mathbb{R}$$
Cho $J$: $\to$ là hàm cho trước bởi
$$J(v) = \sum_{i,j=1}^{n}  a_{ij}v_{i}v_{j} + \sum_{i=1}^{n}  b_{i}v_{i},$$
Ở đâu $v = (v_{1}, \dots  , v_{n})$ và
$$a_{ij} = \int_{0}^{}  1\phi_{i}' (t)\phi_{j}' (t)dt,b_{i} = \int_{0}^{}  1\phi_{i} (t)dt.$$
$$\mathbb{R}^{n}$$
$(1)$ Cho $U_{1}$ là tập con của cho trước bởi
$$U_{1} = \begin{pmatrix} v\in \mathbb{R}^{n}| & b_{i}v_{i}= 0 \end{pmatrix} \sum_{i=1}^{n}  .$$
Xét bài toán của việc tìm cực tiểu của $J$ trên $U_{1}$. Chứng minh rằng Nhân tử Lagrange (Lagrange multiplier) $\lambda$ cho mà Hàm Lagrange (Lagrangian) có tới hạn/quan trọng điểm là $\lambda  = -1$.
$(2)$ Chứng minh rằng ánh xạ được định nghĩa trên $U_{1}$ bởi
$$1/2$$
$$\|v\|= \begin{pmatrix} 1 & !2 \\ v_{i}\phi_{i}' (x) & dx \end{pmatrix} \int_{0}^{}  \sum_{i=1}^{n}$$
Là chuẩn (norm). Chứng minh rằng $J$ là elliptic trên $U_{1}$ với chuẩn (chuẩn (norm)) này. Chứng minh rằng $J$ có duy nhất cực tiểu trên $U_{1}$.
$$\mathbb{R}^{n}$$
$(3)$ Xét tập con của cho trước bởi
$$U_{2} = \begin{pmatrix} v\in \mathbb{R}^{n}| & (\phi_{i} (1) + \phi_{i} (0))v_{i}= 0 \end{pmatrix} \sum_{i=1}^{n}  .$$
Xét bài toán của việc tìm cực tiểu của $J$ trên $U_{2}$. Chứng minh rằng Nhân tử Lagrange (Lagrange multiplier) $\lambda$ cho mà Hàm Lagrange (Lagrangian) có tới hạn/quan trọng điểm là $\lambda  = -1/2$. Chứng minh rằng $J$ là elliptic trên $U_{2}$ với cùng chuẩn (norm) như trong $(2)$. Chứng minh rằng $J$ có duy nhất cực tiểu trên $U_{2}$.
$$\mathbb{R}^{n}$$
$(4)$ Xét tập con của cho trước bởi
$$U_{3} = \begin{pmatrix} v\in \mathbb{R}^{n}| & (\phi_{i} (1) -\phi_{i} (0))v_{i}= 0 \end{pmatrix} \sum_{i=1}^{n}  .$$
Điều này time chỉ ra rằng cần điều kiện cho có cực tiểu trên $U_{3}$ cho ta phương trình $1 + \lambda (1$ - $1) = 0$. Kết luận rằng $J$ thực hiện không có cực tiểu trên $U_{3}$.

<!-- PAGE 1760 -->
Bài toán 49.3. Cho $A$ là thực $n \times  n$ đối xứng xác định dương (SPD) ma trận và cho $b \in \mathbb{R}^{n}$.
$(1)$ Chứng minh rằng nếu ta áp dụng hạ nhanh nhất (steepest descent) phương pháp (cho Euclidean chuẩn (norm)) đến
$$J(v) = \frac{1}{2} \langle Av, v\rangle -\langle b, v\rangle ,$$
Và nếu ta định nghĩa chuẩn (norm) $\|v\|_{A}$ bởi
$$\|v\|_{A} = \langle Av, v\rangle^{1/2} ,$$
Ta thu được bất đẳng thức
$$!$$
$$\| -\|_{2}^{4}$$
$$\|u_{k+1} -u\|_{A}^{2} \le \|u_{k} -u\|_{A}^{2}1 - \frac{A(u_{k}u)}{\|u_{k} -u\|_{A}^{2}\|A(u_{k} -u)\|_{A}^{2}} .$$
$(2)$ Bằng cách sử dụng sự chéo hóa của $A$, ở đâu các trị riêng (eigenvalues) của $A$ được ký hiệu $0 < \lambda_{1}  \le \lambda_{2}  \le \cdots  \le \lambda_{n}$, chứng minh rằng
$$-$$
$$\|u_{k+1} -u\|_{A} \le \frac{cond_{2}(A)1}{cond_{2}(A) + 1} \|u_{k} -u\|_{A} ,$$
Ở đâu $cond_{2}(A) = \lambda_{n} /\lambda_{1}$, và do đó
$$1^{k}$$
$$\|u_{k} -u\|_{A} \le \begin{pmatrix} cond_{2}(A) - \\ cond_{2}(A) + 1 \end{pmatrix} \|u_{0} -u\|_{A} .$$
$(3)$ Chứng minh rằng khi $cond_{2}(A) = 1$, thì $A =$ I và phương pháp hội tụ trong một bước.
$$\mathbb{R}^{n} \mathbb{R}$$
Bài toán 49.4. Chứng minh rằng phương pháp của Polak–Ribi`ere hội tụ nếu $J$: $\to$ là elliptic và $C^{2}$ hàm.
Bài toán 49.5. Chứng minh rằng backtracking đường thẳng search phương pháp được mô tả trong Mục 49.5 có tính chất rằng cho $t$ nhỏ đủ điều kiện $J(u_{k}+td_{k}) \le J(u_{k})+\alpha t\langle \nabla J_{uk}, d_{k}\rangle$ sẽ đúng và search sẽ dừng. Chứng minh rằng exit bất đẳng thức $J(u_{k} + td_{k}) \le J(u_{k}) + \alpha t\langle \nabla J_{uk}, d_{k}\rangle$ nghiệm đúng với mọi $t \in (0, t_{0}]$, với một số $t_{0} > 0$, do đó backtracking đường thẳng search các dừng với bước độ dài $\rho_{k}$ rằng thỏa mãn $\rho_{k}  = 1$ hoặc $\rho_{k}  \in (\beta t_{0}, t_{0}]$.
Bài toán 49.6. Cho $d_{nsd,k}$ và $d_{sd,k}$ được chuẩn hóa và chưa chuẩn hóa descent các hướng của hạ nhanh nhất (steepest descent) phương pháp cho tùy ý chuẩn (norm) (xem Mục 49.8). Chứng minh rằng
$$\langle \nabla J_{uk}, d_{nsd,k}\rangle = -\|\nabla J_{uk}\|^{D}$$
$$\langle \nabla J_{uk}, d_{sd,k}\rangle = -(\|\nabla J_{uk}\|^{D})^{2}$$
$$d_{sd,k} = arg minv \begin{pmatrix} 1 \\ \langle \nabla J_{uk}, v\rangle + & \|v\|^{2} \\ 2 \end{pmatrix} .$$

<!-- PAGE 1761 -->
Bài toán 49.7. Nếu $P$ là đối xứng xác định dương (SPD) ma trận, chứng minh rằng $\|z\|_{P} = (z^{\top}Pz)^{1/2} = P^{1/2}z_{2}$ là chuẩn (norm). Chứng minh rằng được chuẩn hóa hạ nhanh nhất (steepest descent) hướng là
$$d_{nsd,k} = -(\nabla J_{uk}^{\top}P^{-1}\nabla J_{uk})^{-1/2}P^{-1}\nabla J_{uk},$$
Đối ngẫu (dual) chuẩn (norm) là $\|z\|^{D} =$

$P^{-1/2}z_{2}$, và hạ nhanh nhất (steepest descent) hướng đối với $\|\|_{P}$ được cho bởi
$$d_{sd,k} = -P^{-1} \nabla J_{uk}.$$
Bài toán 49.8. Nếu $\|\|$ là $\ell^{1}$ -chuẩn (norm), thì chỉ ra rằng $d_{nsd,k}$ được xác định như sau: cho $i$ là bất kỳ chỉ số cho mà $\|\nabla J_{uk}\|_{\infty} = |(\nabla J_{uk})_{i}|$. Thì
$$d_{nsd,k} = -sign \begin{pmatrix} \partial J \\ (u_{k}) \\ \partial x_{i} \end{pmatrix} e_{i},$$
Ở đâu $e_{i}$ là vectơ cơ sở chính tắc thứ $i$, và
$$d_{sd,k} = - \frac{\partial J}{\partial x_{i}} (u_{k})e_{i}.$$
Bài toán 49.9. (Từ Boyd và Vandenberghe $[29]$, Bài toán 9.12). Nếu $\nabla^{2}$ f(x) là suy biến (hoặc rất ill-conditioned), Newton bước $d_{nt} = -(\nabla^{2} J(x))^{-1}\nabla J_{x}$ là không tốt được định nghĩa. Thay vì ta có thể định nghĩa search hướng $d_{tr}$ như nghiệm của bài toán
$$minimize(1/2)\langle Hv, v\rangle + \langle g, v\rangle$$
$$subject to\|v\|_{2} \le \gamma ,$$
Ở đâu $H = \nabla^{2} f_{x}, g = \nabla f_{x}$, và $\gamma$ là một số dương hằng số. ý tưởng là để sử dụng trust miền, mà là hình cầu đóng (closed ball) ${v$ | $\|v\|_{2} \le \gamma$ }. điểm $x+d_{tr}$ cực tiểu hóa bậc hai xấp xỉ của $f$ tại $x$, subject đến ràng buộc rằng
$$\|x + d_{\mathrm{tr}} -x\|_{2} \le \gamma .$$
Tham số $\gamma$, được gọi là trust tham số, reflects của ta confidence trong bậc hai xấp xỉ. Chứng minh rằng $d_{tr}$ cực tiểu hóa
$$\frac{1}{2} \langle Hv, v\rangle + \langle g, v\rangle + \beta b \|v\|_{2}^{2} ,$$
Với một số $\beta$.
$$b$$
Bài toán 49.10. (Từ Boyd và Vandenberghe $[29]$, Bài toán 9.9). Chứng minh rằng Newton decrement $\lambda (x)$ được cho bởi
$$\langle \nabla \rangle$$
$$\lambda (x) = \sup- \frac{J_{x}, v}{(\langle \nabla^{2} J_{x}v, v\rangle )^{1/2}} .$$
$$v\neq 0$$

<!-- PAGE 1762 -->
Bài toán 49.11. Chỉ ra rằng hàm $f$ cho trước bởi f(x) $= log(e^{x} + e^{-x})$ có duy nhất cực tiểu cho $x^{*} = 0$. Chạy Newton’s phương pháp với cố định bước kích thước $t = 1$, bắt đầu với $x_{0} = 1$, và thì $x_{0} =$ 1.1. Những gì thực hiện bạn quan sát?
Bài toán 49.12. Viết Matlab bài toán quy hoạch cài đặt gradien liên hợp (conjugate gradient) phương pháp. Test của bạn bài toán quy hoạch với ma trận cỡ $n \times  n$
$$A_{n} = \begin{pmatrix} 2 & -1 & 0 & \cdots & 0 \\ -1 & 2 & -1 & \dots & 0 \\ \vdots & \ddots & \ddots & \ddots & \vdots \\ 0 & \cdots & -1 & 2 & -1 \\ 0 & \cdots & 0 & -1 & 2 \end{pmatrix}$$
Và khác nhau right-hand các vế/cạnh, cho khác nhau các giá trị của $n$. Kiểm chứng rằng chạy time là $O(n^{3/2})$.
