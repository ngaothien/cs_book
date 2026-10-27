# Gradien liên hợp (conjugate gradient) Các phương pháp; Không ràng buộc Các bài tập


<!-- PAGE 1741 -->
$(1)$ Nếu $\lambda (u_{k}) > \eta$, thì
$$J(u_{k+1}) -J(u_{k}) \le -\gamma .$$
$(2)$ Nếu $\lambda (u_{k}) \le \eta$, thì backtracking đường thẳng search các chọn $t = 1$ và ta có
$$2\lambda (u_{k+1}) \le (2\lambda (u_{k}))^{2}.$$
Hệ quả là, với mọi $\ell \ge k$, ta có
$$1^{2\ell-k+1}$$
$$J(u_{\ell}) -p^{*}\le \lambda (u_{\ell})^{2}\le \begin{pmatrix} \overline{2} \end{pmatrix} .$$
Trong kết thúc/cuối, accuracy $\epsilon  > 0$ là đạt được trong nhiều nhất
$$-$$
$$\frac{208\alpha}{\alpha \beta (1 -2\alpha )^{2}} (J(u_{0}) -p^{*}) + log_{2} log_{2}(1/\epsilon )$$
Các vòng lặp, ở đâu $\alpha$ và $\beta$ là các hằng số liên quan trong đường thẳng search. Điều này cận là hiển nhiên độc lập của được chọn tọa độ hệ. Trái với trực giác, descent hướng $d_{k} = -\nabla J_{uk}$ cho trước bởi opposite của gradien là không luôn luôn tối ưu. Trong mục tiếp theo ta sẽ xem cách mà tốt hơn hướng có thể được được chọn; điều này là phương pháp của liên hợp các gradien.

## 49.10 Gradien liên hợp (conjugate gradient) Các phương pháp cho Không ràng buộc

$$Problems$$
Gradien liên hợp (conjugate gradient) phương pháp do Hestenes và Stiefel $(1952)$ là hạ gradien (gradient descent)
$$\mathbb{R}^{n} \mathbb{R}$$
Phương pháp rằng áp dụng đến elliptic toàn phương phiếm hàm $J$: $\to$ cho trước bởi
$$J(v) = \frac{1}{2} \langle Av, v\rangle -\langle b, v\rangle ,$$
Ở đâu $A$ là $n \times  n$ đối xứng xác định dương (SPD) ma trận. Mặc dù nó được trình bày như phương pháp lặp (iterative method), nó kết thúc trong nhiều nhất $n$ các bước. Như thông thường, gradien liên hợp (conjugate gradient) phương pháp các bắt đầu với một số tùy ý ban đầu vectơ $u_{0}$ và tiến hành qua dãy của vòng lặp các bước sinh (tốt hơn và tốt hơn) các xấp xỉ $u_{k}$ của tối ưu vectơ $u$ cực tiểu hóa $J$. During vòng lặp bước, hai các vectơ cần được xác định:
$(1)$ descent hướng $d_{k}$.
$(2)$ tiếp theo xấp xỉ $u_{k+1}$. để tìm $u_{k+1}$, ta cần để tìm bước nhảy (stepsize) $\rho_{k}  > 0$ và thì
$$u_{k+1} = u_{k} -\rho_{k} d_{k}.$$
Typically, $\rho_{k}$ là tìm thấy bởi performing đường thẳng search dọc theo hướng $d_{k}$, cụ thể là ta tìm $\rho_{k}$ như thực số sao cho hàm $\rho  \mapsto J(u_{k}$ - $\rho d_{k})$ được cực tiểu hóa.

<!-- PAGE 1742 -->
Ta đã thấy trong Mệnh đề 49.13 rằng during execution của gradien phương pháp với tối ưu bước nhảy (stepsize) tham số rằng bất kỳ hai liên tiếp descent các hướng là trực giao. mới twist với gradien liên hợp (conjugate gradient) phương pháp là rằng cho trước $u_{0}, u_{1}, \dots  , u_{k}$, tiếp theo xấp xỉ $u_{k+1}$ là thu được như nghiệm của bài toán mà bao gồm trong cực tiểu hóa $J$ trên afin
$$\mathbb{R}^{n}$$
Không gian con $u_{k} +\mathcal{G}_{k}$, ở đâu $\mathcal{G}_{k}$ là không gian con của được sinh (spanned) bởi các gradien
$$\nabla J_{u0}, \nabla J_{u1}, \dots  , \nabla J_{uk}.$$
Ta có thể giả sử rằng $\nabla J_{u\ell}$ ̸ $= 0$ cho $\ell = 0, \dots  , k$, vì phương pháp kết thúc như soon như $\nabla J_{uk} = 0$. Tiên nghiệm (a priori) không gian con $\mathcal{G}_{k}$ có số chiều $\le k + 1$, nhưng ta sẽ xem rằng thực ra nó có số chiều $k + 1$. Thì ta có
$$$$
$$u_{k} +\mathcal{G}_{k} =u_{k} + \sum_{i=0}^{k}  \alpha_{i} \nabla J_{ui} \alpha_{i}  \in \mathbb{R}, 0 \le i \le k,$$
Và của ta cực tiểu hóa bài toán là để tìm $u_{k+1}$ sao cho
$$u_{k+1} \in u_{k} +\mathcal{G}_{k}andJ(u_{k+1}) =\inf J(v).$$
$$v\in uk+\mathcal{G} k$$
Trong gradien phương pháp với tối ưu bước nhảy (stepsize) tham số descent hướng $d_{k}$ là tỷ lệ đến gradien $\nabla J_{uk}$, nhưng trong gradien liên hợp (conjugate gradient) phương pháp, $d_{k}$ bằng $\nabla J_{uk}$ được đúng bởi một số bội của $d_{k-1}$. gradien liên hợp (conjugate gradient) phương pháp là superior đến gradien phương pháp với tối ưu bước nhảy (stepsize) tham số cho sau đây các lý do được chứng minh đúng sau này:
() các gradien $\nabla J_{ui}$ và $\nabla J_{uj}$ là trực giao với mọi $i, j$ với $0 \le i \neq  j \le k$. Điều này suy ra rằng nếu $\nabla J_{ui}$ ̸ $= 0$ cho $i = 0, \dots  , k$, thì các vectơ $\nabla J_{ui}$ là độc lập tuyến tính (linearly independent), do đó phương pháp các dừng trong nhiều nhất $n$ các bước.
$(b)$ Nếu ta viết $\Delta_{\ell} = u_{\ell+1}$ - $u_{\ell} = -\rho_{\ell} d_{\ell}$, thứ hai đáng chú ý sự kiện về gradien liên hợp (conjugate gradient) phương pháp là rằng các vectơ $\Delta_{\ell}$ thỏa mãn sau đây các điều kiện:
$$\langle A\Delta_{\ell} , \Delta_{i} \rangle = 00 \le i < \ell \le k.$$
Các vectơ $\Delta_{\ell}$ và $\Delta_{i}$ được nói là liên hợp đối với ma trận $A$ (hoặc A-conjugate). Hệ quả là, nếu $\Delta_{\ell}  \neq  0$ cho $\ell = 0, \dots  , k$, thì các vectơ $\Delta_{\ell}$ là độc lập tuyến tính (linearly independent).
$(c)$ Có một đơn giản công thức để tính $d_{k+1}$ từ $d_{k}$, và để tính $\rho_{k}$. Ta bây giờ chứng minh ở trên các sự kiện. Ta bắt đầu với ().

> **Mệnh đề 49.15.** Giả sử rằng $\nabla J_{ui}$ ̸ $= 0$ cho $i = 0, \dots  , k$. Thì cực tiểu hóa bài toán, tìm $u_{k+1}$ sao cho
$$u_{k+1} \in u_{k} +\mathcal{G}_{k}andJ(u_{k+1}) =\inf J(v),$$
$$v\in uk+\mathcal{G} k$$
Có duy nhất nghiệm, và các gradien $\nabla J_{ui}$ và $\nabla J_{uj}$ là trực giao với mọi $i, j$ với $0 \le i \neq  j \le k + 1$.

<!-- PAGE 1743 -->

*Chứng minh.* không gian afin (affine space) $u_{\ell} + \mathcal{G}_{\ell}$ là đóng và lồi, và vì $J$ là toàn phương elliptic phiếm hàm nó là bức (coercive) và lồi chặt (strictly convex), do đó theo Định lý 49.8(2) nó có duy nhất cực tiểu trong $u_{\ell} +\mathcal{G}_{\ell}$. Điều này cực tiểu $u_{\ell+1}$ là cũng cực tiểu của bài toán, tìm $u_{\ell+1}$ sao cho
$$u_{\ell+1} \in u_{\ell}+\mathcal{G}_{\ell}andJ(u_{\ell+1}) = infJ(u_{\ell}+ v),$$
$$v\in G\ell$$
Và vì $\mathcal{G}_{\ell}$ là không gian con, theo Hệ quả 40.10 ta phải có
$$dJ_{u\ell+1}(w) = 0for all w \in G_{\ell},$$
Rằng là
$$\langle \nabla J_{u\ell+1}, w\rangle = 0for all w \in G_{\ell}.$$
Vì $\mathcal{G}_{\ell}$ được sinh (spanned) bởi $(\nabla J_{u0}, \nabla J_{u1}, \dots  , \nabla J_{u\ell})$, ta thu được
$$\langle \nabla J_{u\ell+1}, \nabla J_{uj}\rangle = 0,0 \le j \le \ell ,$$
Và vì điều này nghiệm đúng cho $\ell = 0, \dots  , k$, ta thu được
$$\langle \nabla J_{ui}, \nabla J_{uj}\rangle = 0,0 \le i \neq  j \le k + 1,$$
Mà chỉ ra phần thứ hai của mệnh đề. Như hệ quả của Mệnh đề 49.15, nếu $\nabla J_{ui}$ ̸ $= 0$ cho $i = 0, \dots  , k$, thì các vectơ $\nabla J_{ui}$ là độc lập tuyến tính (linearly independent) $and\mathcal{G}_{k}$ có số chiều $k + 1$. Vì vậy, gradien liên hợp (conjugate gradient) phương pháp kết thúc trong nhiều nhất $n$ các bước. Đây là một ví dụ của bài toán cho mà hạ gradien (gradient descent) với tối ưu bước nhảy (stepsize) tham số thực hiện không hội tụ trong hữu hạn số của các bước.
$$\mathbb{R}^{2} \mathbb{R}$$

> **Ví dụ 49.2.** Cho $J$: $\to$ là hàm cho trước bởi
$$J(v_{1}, v_{2}) = \frac{1}{2} (\alpha_{1} v_{1}^{2} + \alpha_{2} v_{2}^{2}),$$
Ở đâu $0 < \alpha_{1}  < \alpha_{2}$. cực tiểu của $J$ là đạt được tại $(0, 0)$. Trừ khi ban đầu vectơ $u_{0} = (u_{1}^{0}, u_{2}^{0})$ có tính chất rằng hoặc $u_{1}^{0} = 0$ hoặc $u_{2}^{0} = 0$, ta khẳng định rằng hạ gradien (gradient descent) với tối ưu bước nhảy (stepsize) tham số thực hiện không hội tụ trong hữu hạn số của các bước. Nhận thấy rằng
$$\nabla J_{(v1,v2)} = \begin{pmatrix} \alpha_{1} v_{1} \\ \alpha_{2} v_{2} \end{pmatrix} .$$
Hệ quả là, cho trước $u_{k}$, đường thẳng search cho việc tìm $\rho_{k}$ và $u_{k+1}$ cho ta $u_{k+1} = (0, 0)$ khi và chỉ khi tồn tại một $\rho  \in \mathbb{R}$ sao cho
$$u_{1}^{k} = \rho \alpha_{1} u_{1}^{k}andu_{2}^{k} = \rho \alpha_{2} u_{2}^{k}.$$
Vì $\alpha_{1}  \neq  \alpha_{2}$, điều này là chỉ khả dĩ/có thể nếu hoặc $u_{1}^{k} = 0$ hoặc $u_{2}^{k} = 0$. các công thức cho trước chỉ trước Mệnh đề 49.14 cho
$$u_{1}^{k+1}= \frac{\alpha_{2}^{2} (\alpha_{2} \alpha_{1} )u_{1}^{k}(u_{2}^{k})^{2}}{\alpha_{1}^{3} (u_{1}^{k})^{2} \alpha_{2}^{3} (u_{2}^{k})^{2}} - ,u_{2}^{k+1}= \frac{\alpha_{1}^{2} (\alpha_{1} \alpha_{2} )u_{2}^{k}(u_{1}^{k})^{2}}{\alpha_{1}^{3} (u_{1}^{k})^{2} \alpha_{2}^{3} (u_{2}^{k})^{2}} - ,$$
$$+ +$$
Mà suy ra rằng nếu $u_{1}^{k}$ ̸ $= 0$ và $u_{2}^{k}$ ̸ $= 0$, thì $u_{1}^{k+1} = 0$ và $u_{2}^{k+1} = 0$, do đó phương pháp chạy forever từ bất kỳ ban đầu vectơ $u_{0} = (u_{1}^{0}, u_{2}^{0})$ sao cho $u_{1}^{0}$ ̸ $= 0$ và, $u_{2}^{0}$ ̸ $= 0$.

<!-- PAGE 1744 -->
Ta bây giờ chứng minh $(b)$.

> **Mệnh đề 49.16.** Giả sử rằng $\nabla J_{ui}$ ̸ $= 0$ cho $i = 0, \dots  , k$, và cho $\Delta_{\ell} = u_{\ell+1}$ - $u_{\ell}$, cho $\ell = 0, \dots  , k$. Thì $\Delta_{\ell}  \neq  0$ cho $\ell = 0, \dots  , k$, và
$$\langle A\Delta_{\ell} , \Delta_{i} \rangle = 0,0 \le i < \ell \le k.$$
Các vectơ $\Delta_{0} , \dots  , \Delta_{k}$ là độc lập tuyến tính (linearly independent).

*Chứng minh.* Vì $J$ là toàn phương phiếm hàm ta có
$$\nabla J_{v+w} = A(v + w) -b = Av -b + Aw = \nabla J_{v} + Aw.$$
Suy ra rằng
$$\nabla J_{u\ell+1} = \nabla J_{u\ell+\Delta\ell}= \nabla J_{u\ell}+ A\Delta_{\ell} ,0 \le \ell \le k.(*_{1})$$
Theo Mệnh đề 49.15, vì
$$\langle \nabla J_{ui}, \nabla J_{uj}\rangle = 0,0 \le i \neq  j \le k,$$
Ta thu được
$$0 = \langle \nabla J_{u\ell+1}, \nabla J_{u\ell}\rangle = \|\nabla J_{u\ell}\|^{2}+ \langle A\Delta_{\ell} , \nabla J_{u\ell}\rangle ,\ell = 0, \dots  , k,$$
Và vì bởi giả thiết $\nabla J_{ui}$ ̸ $= 0$ cho $i = 0, \dots  , k$, ta suy ra rằng
$$\Delta_{\ell}  \neq  0,\ell = 0, \dots  , k.$$
Nếu $k \ge 1$, cho $i = 0, \dots  , \ell$ - $1$ và $\ell \le k$ ta cũng có
$$0 = \langle \nabla J_{u\ell+1}, \nabla J_{ui}\rangle = \langle \nabla J_{u\ell}, \nabla J_{ui}\rangle + \langle A\Delta_{\ell} , \nabla J_{ui}\rangle$$
$$= \langle A\Delta_{\ell} , \nabla J_{ui}\rangle .$$
Vì $\Delta_{j}  = u_{j+1}$ - $u_{j} \in G_{j}$ và $\mathcal{G}_{j}$ được sinh (spanned) bởi $(\nabla J_{u0}, \nabla J_{u1}, \dots  , \nabla J_{uj})$, ta thu được
$$\langle A\Delta_{\ell} , \Delta_{j} \rangle = 0,0 \le j < \ell \le k.$$
Cho cuối cùng phát biểu của mệnh đề, cho $w_{0}, w_{1}, \dots  , w_{k}$ là bất kỳ $k + 1$ khác không các vectơ sao cho
$$\langle Aw_{i}, w_{j}\rangle = 0,0 \le i < j \le k.$$
Ta khẳng định rằng $w_{0}, w_{1}, \dots  , w_{k}$ là độc lập tuyến tính (linearly independent).
$$If we have a linear dependence \sum_{i}  k=0 \lambda_{i} w_{i} = 0, then we have$$
$$0 =A \begin{pmatrix} \lambda_{i} w_{i} \end{pmatrix} \sum_{i=0}^{k}  , w_{j}= \sum_{i=0}^{k}  \lambda_{i} \langle Aw_{i}, w_{j}\rangle = \lambda_{j} \langle Aw_{j}, w_{j}\rangle ,$$
Ở đâu ta tạo thành các phần tử này trong các tích cho $j = 0, \dots  , k$, trong rằng thứ tự. Vì $A$ là đối xứng xác định dương (SPD) (bởi vì $J$ là toàn phương elliptic phiếm hàm) và $w_{j}$ ̸ $= 0$, ta có $\langle Aw_{j}, w_{j}\rangle > 0$, và do đó $\lambda_{j}  = 0$ cho $j = 0, \dots  , k$. Vì vậy các vectơ $w_{0}, w_{1}, \dots  , w_{k}$ là độc lập tuyến tính (linearly independent).

<!-- PAGE 1745 -->
Các nhận xét:
$(1)$ Vì $A$ là đối xứng xác định dương (SPD), ánh xạ song tuyến tính (bilinear map) $(u, v) \mapsto \langle$ Au, $v\rangle$ là tích vô hướng (inner product) $\langle$ -, $-\rangle_{A}$ trên $\mathbb{R}^{n}$. Hệ quả là, hai các vectơ $u, v$ là liên hợp đối với ma trận $A$ (hoặc A-conjugate), mà có nghĩa là $\langle$ Au, $v\rangle = 0$, khi và chỉ khi $u$ và $v$ là trực giao đối với tích vô hướng (inner product) $\langle$ -, $-\rangle_{A}$.
$(2)$ Bởi chọn descent hướng là $-\nabla J_{uk}$, hạ gradien (gradient descent) phương pháp với tối ưu bước nhảy (stepsize) tham số treats mức các tập hợp ${u$ | J(u) $= J(u_{k})}$ như nếu chúng đã là các mặt cầu. gradien liên hợp (conjugate gradient) phương pháp là nhiều hơn/thêm tinh tế, và lấy “hình học” của mức tập hợp ${u$ | J(u) $= J(u_{k})}$ vào account, qua khái niệm của liên hợp các hướng.
$(3)$ khái niệm của liên hợp hướng có của nó các gốc trong lý thuyết của xạ ảnh các đường bậc hai (conics) và các mặt bậc hai ở đâu $A$ là $2 \times  2$ hoặc một ma trận cỡ $3 \times  3$ và ở đâu $u$ và $v$ là liên hợp khi và chỉ khi $u^{\top}Av = 0$.
$(4)$ thuật ngữ gradien liên hợp (conjugate gradient) là somewhat misleading. Nó là không các gradien ai là liên hợp các hướng, nhưng descent các hướng. Theo định nghĩa của các vectơ $\Delta_{\ell} = u_{\ell+1}$ - $u_{\ell}$, ta có thể viết
$$\Delta_{\ell} = \sum_{i=0}^{\ell}  \delta_{i}^{\ell}  \nabla J_{ui},0 \le \ell \le k.(*_{2})$$
Trong ma trận tạo thành, ta có thể viết
$$\begin{pmatrix} \Delta_{0} & \Delta_{1} & \cdots & \Delta_{k} \end{pmatrix} = \begin{pmatrix} \nabla J_{u0} & \nabla J_{u1} & \cdots & \nabla J_{uk} \end{pmatrix} \begin{pmatrix} \delta_{0}^{0} & \delta^{1} & \cdots & \delta^{k-1} & \delta^{k} \\ 0 & \delta_{1}^{01} & \cdots & \delta^{0k-1} & \delta^{0k} \\ 0 & 0 & \cdots & \delta_{2}^{1k-1} & \delta_{2}^{1k} \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \delta_{k}^{k} \end{pmatrix} ,$$
$$\cdots$$
Mà suy ra rằng $\delta_{\ell}^{\ell}$ ̸ $= 0$ cho $\ell = 0, \dots  , k$. Xét theo ở trên sự kiện, vì $\Delta_{\ell}$ và $d_{\ell}$ là thẳng hàng, nó là thuận tiện đến viết descent hướng $d_{\ell}$ như
$$d_{\ell}= \sum_{i=0}^{\ell-1}  \lambda_{i}^{\ell}  \nabla J_{ui} + \nabla J_{u\ell},0 \le \ell \le k.(*_{3})$$
Của ta tiếp theo mục tiêu là để tính $u_{k+1}$, giả sử rằng các hệ số $\lambda_{i}^{k}$ là đã biết cho $i = 0, \dots  , k$, và thì để tìm đơn giản các công thức cho $\lambda_{i}^{k}$. bài toán rút gọn đến việc tìm $\rho_{k}$ sao cho
$$J(u_{k} -\rho_{k} d_{k}) = \inf J(u_{k} -\rho d_{k}),$$
$$\rho \in \mathbb{R}$$

<!-- PAGE 1746 -->
Và thì $u_{k+1} = u_{k}$ - $\rho_{k} d_{k}$. Thực ra, bởi $(*_{2})$, vì
$$\Delta_{k}  = \sum_{i=0}^{k}  \delta_{i}^{k}  \nabla J_{ui} = \delta_{k}^{k} \begin{pmatrix} \delta_{i}^{k} \\ \nabla J_{ui}+ \nabla J_{uk} \\ \delta_{k}^{k} \end{pmatrix} \sum_{i=0}^{k-1}  ,$$
Ta phải có
$$\Delta_{k}  = \delta_{k}^{k} d_{k}and\rho_{k}  = -\delta_{k}^{k} .(*_{4})$$
Đáng chú ý, các hệ số $\lambda_{i}^{k}$ và descent các hướng $d_{k}$ có thể được được tính dễ dàng bằng cách sử dụng sau đây các công thức.

> **Mệnh đề 49.17.** Giả sử rằng $\nabla J_{ui}$ ̸ $= 0$ cho $i = 0, \dots  , k$. Nếu ta viết
$$d_{\ell}= \sum_{i=0}^{\ell-1}  \lambda_{i}^{\ell}  \nabla J_{ui} + \nabla J_{u\ell},0 \le \ell \le k,$$
Thì ta có
$$ \|\nabla \|^{2}$$
$$\lambda_{i}^{k}  = \frac{J_{uk}}{\|\nabla J_{ui}\|^{2}} ,0 \le i \le k -1,$$
$$$$
$$$$
$$$$
$$(\dagger )d_{0} = \nabla J_{u0}$$
$$ \|\nabla \|^{2}$$
$$$$
$$d_{\ell}= \nabla J_{u\ell}+ \frac{J_{u\ell}}{\nabla J_{u\ell-1}^{2}} d_{\ell-1},1 \le \ell \le k.$$
$$$$

*Chứng minh.* Vì bởi $(*_{4})$ ta có $\Delta_{k}  = \delta_{k}^{k} d_{k}, \delta_{k}^{k}$ ̸ $= 0$, (theo Mệnh đề 49.16) ta có
$$\langle Ad_{\ell}, \Delta_{i} \rangle = 0,0 \le i < \ell \le k.$$
Bởi $(*_{1})$ ta có $\nabla J_{u\ell+1} = \nabla J_{u\ell} + A\Delta_{\ell}$, và vì $A$ là ma trận đối xứng (symmetric matrix), ta có
$$0 = \langle Ad_{k}, \Delta_{\ell} \rangle = \langle d_{k}, A\Delta_{\ell} \rangle = \langle d_{k}, \nabla J_{u\ell+1} -\nabla J_{u\ell}\rangle ,$$
Cho $\ell = 0, \dots  , k$ - $1$. Vì
$$d_{k} = \sum_{i=0}^{k-1}  \lambda_{i}^{k}  \nabla J_{ui} + \nabla J_{uk},$$
Ta có
$$\sum_{i=0}^{k-1}  \lambda_{i}^{k}  \nabla J_{ui} + \nabla J_{uk}, \nabla J_{u\ell+1} -\nabla J_{u\ell}= 0,0 \le \ell \le k -1.$$
Vì theo Mệnh đề 49.15 các gradien $\nabla J_{ui}$ là đôi một trực giao, ở trên các phương trình cho
$$+$$
$$-\lambda_{k-1}^{k}

$\nabla J_{uk-1}^{2}$

$\|\nabla J_{uk}\|^{2}=$ 0$$
$$+$$
$$-\lambda_{\ell}^{k} \|\nabla J_{u\ell}\|^{2} \lambda_{\ell+1}^{k}

$\nabla J_{u\ell+1}^{2}$

$=$ 0,0 $\le \ell \le k$ -2,k $\ge$ 2,$$

<!-- PAGE 1747 -->
Và dễ quy nạp cho ta
$$\|\nabla \|^{2}$$
$$\lambda_{i}^{k}  = \frac{J_{uk}}{\|\nabla J_{ui}\|^{2}} ,0 \le i \le k -1.$$
Hệ quả là, bằng cách sử dụng $(*_{3})$ ta có
$$\|\nabla \|^{2}$$
$$d_{k} = \sum_{i=0}^{k-1}  \frac{J_{uk}}{\|\nabla J_{ui}\|^{2}} \nabla J_{ui} + \nabla J_{uk}$$
$$\nabla

!$$
$$\|\nabla \|^{2}$$
$$= \nabla J_{uk} + \frac{J_{uk}}{\nabla J_{uk-1}^{2}} \sum_{i=0}^{k-2}  \frac{J_{uk-1}^{2}}{\|\nabla J_{ui}\|^{2}} \nabla J_{ui} + \nabla J_{uk-1}$$
$$\|\nabla \|^{2}$$
$$= \nabla J_{uk} + \frac{J_{uk}}{\nabla J_{uk-1}^{2}} d_{k-1},$$
Mà kết luận chứng minh. Nó vẫn còn để tính $\rho_{k}$, mà là nghiệm của đường thẳng search
$$J(u_{k} -\rho_{k} d_{k}) = \inf J(u_{k} -\rho d_{k}).$$
$$\rho \in \mathbb{R}$$
Vì $J$ là toàn phương phiếm hàm, cơ bản phép tính trái đến độc giả chỉ ra rằng hàm được cực tiểu hóa là
$$\rho  \mapsto \frac{\rho^{2}}{2} \langle Ad_{k}, d_{k}\rangle -\rho \langle \nabla J_{uk}, d_{k}\rangle + J(u_{k}),$$
Có mininum là thu được khi đạo hàm của nó là không, nghĩa là,
$$\langle \nabla \rangle$$
$$\rho_{k}  = \frac{J_{uk}, d_{k}}{\langle Ad_{k}, d_{k}\rangle} .(*_{5})$$
Trong tóm tắt, gradien liên hợp (conjugate gradient) phương pháp tìm cực tiểu $u$ của elliptic toàn phương phiếm hàm
$$J(v) = \frac{1}{2} \langle Av, v\rangle -\langle b, v\rangle$$
Bởi việc tính toán dãy của các vectơ $u_{1}, d_{1}, \dots  , u_{k-1}, d_{k-1}, u_{k}$, bắt đầu từ bất kỳ vectơ $u_{0}$, với
$$d_{0} = \nabla J_{u0}.$$
Nếu $\nabla J_{u0} = 0$, thì thuật toán kết thúc với $u = u_{0}$. Ngược lại, cho $k \ge 0$, giả sử rằng $\nabla J_{ui}$ ̸ $= 0$ cho $i = 1, \dots  , k$, tính
$$ \langle \nabla \rangle$$
$$\rho_{k}  = \frac{J_{uk}, d_{k}}{\langle Ad_{k}, d_{k}\rangle}$$
$$$$
$$$$
$$u_{k+1} = u_{k} -\rho_{k} d_{k}$$
$$(*_{6})$$
$$

$\nabla$$$
$$$$
$$d_{k+1} = \nabla J_{uk+1} + \frac{J_{uk+1}^{2}}{\|\nabla J_{uk}\|^{2}} d_{k}.$$
$$$$

<!-- PAGE 1748 -->
Nếu $\nabla J_{uk+1} = 0$, thì algorihm kết thúc với $u = u_{k+1}$. Như ta đã chỉ ra trước, thuật toán kết thúc trong nhiều nhất $n$ các vòng lặp.

> **Ví dụ 49.3.** Cho chúng ta lấy ví dụ của Mục 49.6 và áp dụng gradien liên hợp (conjugate gradient) quy trình. Nhắc lại rằng
$$J(x, y) = \frac{1}{2} \begin{pmatrix} x & y \end{pmatrix} \begin{pmatrix} 3 & 2 \\ 2 & 6 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} - \begin{pmatrix} 2 & -8 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}$$
$$+ 2 -$$
$$= \frac{3}{2} x^{2}xy + 3y^{2}2x + 8y.$$
Lưu ý rằng $\nabla J_{v} =$ (3x $+$ 2y - $2$, 2x $+$ 6y $+ 8)$, Initialize quy trình bằng cách đặt
$$u_{0} = (-2, -2),d_{0} = \nabla J_{u0} = (-12, -8)$$
Bước $1$ liên quan đến tính toán
$$\langle \nabla \rangle$$
$$\rho_{0}  = \frac{J_{u0}, d_{0}}{\langle Ad_{0}, d_{0}\rangle} = \frac{13}{75}$$
$$u_{1} = u_{0} -\rho_{0} d_{0} = (-2, -2) - \frac{13}{75} (-12, -8) = \begin{pmatrix} 2 & 46 \\ , - \\ 25 & 75 \end{pmatrix}$$
$$||\nabla ||^{2}$$
$$d_{1} = \nabla J_{u1} + \frac{J_{u1}}{||\nabla J_{u0}||^{2}} d_{0} = \begin{pmatrix} 2912 18928 \\ - & , \\ 625 & \overline{5625} \end{pmatrix} .$$
Nhận thấy rằng $\rho_{0}$ và $u_{1}$ là một cách chính xác cùng như trong trường hợp trường hợp của hạ gradien (gradient descent) với tối ưu bước kích thước tham số. difference lies trong phép tính của $d_{1}$. Như ta sẽ xem, điều này thay đổi sẽ tạo huge difference trong sự hội tụ đến duy nhất cực tiểu $u = (2, -2)$. Ta tiếp tục với gradien liên hợp (conjugate gradient) quy trình và tính toán Bước $2$ như
$$\langle \nabla \rangle$$
$$\rho_{1}  = \frac{J_{u1}, d_{1}}{\langle Ad_{1}, d_{1}\rangle} = \frac{75}{82}$$
$$u_{2} = u_{1} -\rho_{1} d_{1} = \begin{pmatrix} 2 & 46 \\ , - \\ 25 & 75 \end{pmatrix} - \frac{75}{82} \begin{pmatrix} 2912 18928 \\ - & , \\ 625 & \overline{5625} \end{pmatrix} = (2, -2)$$
$$||\nabla ||^{2}$$
$$d_{2} = \nabla J_{u2} + \frac{J_{u2}}{||\nabla J_{u1}||^{2}} d_{1} = (0, 0).$$
Vì $\nabla J_{u2} = 0$, quy trình kết thúc trong hai các bước, như opposed đến $31$ các bước cần thiết cho hạ gradien (gradient descent) với tối ưu bước kích thước tham số. Hestenes và Stiefel realized rằng Các phương trình $(*_{6})$ có thể được được sửa đổi để tạo các phép tính nhiều hơn/thêm efficient, bởi có chỉ một việc tính giá trị của ma trận $A$ trên vectơ, cụ thể là $d_{k}$. ý tưởng là để tính $\nabla_{uk}$ một cách quy nạp.

<!-- PAGE 1749 -->
Vì bởi $(*_{1})$ và $(*_{4})$ ta có $\nabla J_{u\ell+1} = \nabla J_{u\ell} + A\Delta_{\ell} = \nabla J_{u\ell}$ - $\rho_{\ell} Ad_{\ell}$, gradien $\nabla J_{u\ell+1}$ có thể được được tính một cách lặp:
$$\nabla J_{0} = Au_{0} -b$$
$$\nabla J_{u\ell+1} = \nabla J_{u\ell}-\rho_{\ell} Ad_{\ell}.$$
Vì theo Mệnh đề 49.17 ta có
$$\|\nabla \|^{2}$$
$$d_{k} = \nabla J_{uk} + \frac{J_{uk}}{\nabla J_{uk-1}^{2}} d_{k-1}$$
Và vì $d_{k-1}$ là tổ hợp tuyến tính (linear combination) của các gradien $\nabla J_{ui}$ cho $i = 0, \dots  , k$ - $1$, mà là tất cả trực giao đến $\nabla J_{uk}$, ta có
$$\langle \nabla \rangle  \|\nabla \|^{2}$$
$$\rho_{k}  = \frac{J_{uk}, d_{k}}{\langle Ad_{k}, d_{k}\rangle} = \frac{J_{uk}}{\langle Ad_{k}, d_{k}\rangle} .$$
Nó là thông lệ đến giới thiệu số hạng $r_{k}$ được định nghĩa như
$$r_{k} = \nabla J_{uk} = Au_{k} -b(*_{7})$$
Và đến gọi nó phần dư (residual). Thì gradien liên hợp (conjugate gradient) phương pháp bao gồm của sau đây các bước. Ta intitialize phương pháp bắt đầu từ bất kỳ vectơ $u_{0}$ và tập hợp
$$d_{0} = r_{0} = Au_{0} -b.$$
Chính vòng lặp bước là $(k \ge 0)$:
$$\|\|^{2}$$
$$\rho_{k}  = \frac{r_{k}}{\langle Ad_{k}, d_{k}\rangle}$$
$$$$
$$$$
$$$$
$$u_{k+1} = u_{k} -\rho_{k} d_{k}$$
$$$$
$$$$
$$$$
$$$$
$$(*_{8})r_{k+1} = r_{k}\rho_{k} Ad_{k}$$
$$ \|\|^{2}$$
$$$$
$$\beta_{k+1}  = \frac{r_{k+1} -}{\|r_{k}\|^{2}}$$
$$$$
$$$$
$$$$
$$$$
$$d_{k+1} = r_{k+1} + \beta_{k+1}  d_{k}.$$
$$$$
 Beware rằng một số các tác giả định nghĩa phần dư (residual) $r_{k}$ như $r_{k} = b-Au_{k}$ và descent hướng $d_{k}$ như $-d_{k}$. Trong trường hợp này, phương trình thứ hai trở thành
$$u_{k+1} = u_{k} + \rho_{k} d_{k}.$$
Vì $d_{0} = r_{0}$, các phương trình
$$r_{k+1} = r_{k} -\rho_{k} Ad_{k}$$
$$d_{k+1} = r_{k+1} + \beta_{k+1} d_{k}$$

<!-- PAGE 1750 -->
Suy ra bởi quy nạp rằng không gian con $\mathcal{G}_{k}$ được sinh (spanned) bởi $(r_{0}, r_{1}, \dots  , r_{k})$ và $(d_{0}, d_{1}, \dots  , d_{k})$ là không gian con được sinh (spanned) bởi
$$(r_{0}, Ar_{0}, A^{2}r_{0}, \dots  , A^{k}r_{0}).$$
Như vậy không gian con được gọi là một Krylov không gian con. Nếu ta định nghĩa sai số $e_{k}$ như $e_{k} = u_{k}$ - $u$, thì $e_{0} = u_{0}$ - $u$ và $Ae_{0} = Au_{0}$ - Au $= Au_{0}$ - $b = d_{0} = r_{0}$, và thì bởi vì
$$u_{k+1} = u_{k} -\rho_{k} d_{k}$$
Ta xem rằng
$$e_{k+1} = e_{k} -\rho_{k} d_{k}.$$
Vì $d_{k}$ thuộc đến không gian con được sinh (spanned) bởi $(r_{0}, Ar_{0}, A^{2}r_{0}, \dots  , A^{k}r_{0})$ và $r_{0} = Ae_{0}$, ta xem rằng $d_{k}$ thuộc đến không gian con được sinh (spanned) bởi $(Ae_{0}, A^{2}e_{0}, A^{3}e_{0}, \dots  , A^{k+1}e_{0})$, và thì bởi quy nạp ta xem rằng $e_{k+1}$ thuộc đến không gian con được sinh (spanned) bởi $(e_{0}, Ae_{0}, A^{2}e_{0}, A^{3}e_{0}, \dots  , A^{k+1}e_{0})$. Điều này có nghĩa là có một đa thức $P_{k}$ của bậc $\le k$ sao cho $P_{k}(0) = 1$ và
$$e_{k} = P_{k}(A)e_{0}.$$
Điều này là quan trọng sự kiện bởi vì nó cho phép cho giải tích/phân tích của sự hội tụ của gradien liên hợp (conjugate gradient) phương pháp; xem Trefethen và Bau $[182]$ (Lecture $38)$. Cho điều này, vì $A$ là
$$\mathbb{R}^{n}$$
Đối xứng xác định dương (SPD), ta biết rằng $\langle u, v\rangle_{A}  = \langle$ Av, $u\rangle$ là tích vô hướng (inner product) trên có liên kết chuẩn (norm) được ký hiệu bởi $\|v\|_{A}$. Thì nhận thấy rằng nếu e(v) $= v$ - $u$, thì
$$\|e(v)\|_{A}^{2} = \langle Av -Au, v -u\rangle$$
$$= \langle Av, v\rangle -2\langle Au, v\rangle + \langle Au, u\rangle$$
$$= \langle Av, v\rangle -2\langle b, v\rangle + \langle b, u\rangle$$
$$= 2J(v) + \langle b, u\rangle .$$
Suy ra rằng $v = u_{k}$ cực tiểu hóa $\|e(v)\|_{A}$ trên $u_{k-1}+\mathcal{G}_{k-1}$ vì $u_{k}$ cực tiểu hóa $J$ trên $u_{k-1}+\mathcal{G}_{k-1}$. Vì $e_{k} = P_{k}(A)e_{0}$ với một số đa thức $P_{k}$ của bậc $\le k$ sao cho $P_{k}(0) = 1$, nếu ta cho $\mathcal{P}_{k}$ là tập hợp của các đa thức P(t) của bậc $\le k$ sao cho P(0) $= 1$, thì ta có
$$\|e_{k}\|_{A} = \inf \|P(A)e_{0}\|_{A} .$$
$$P\in Pk$$
Vì $A$ là đối xứng xác định dương (SPD) ma trận nó có thực dương các trị riêng (eigenvalues) $\lambda_{1} , \dots  , \lambda_{n}$ và
$$there is an orthonormal basis of eigenvectors h_{1}, \dots  , h_{n} so that if we write e_{0} = \sum_{j}  n=1 a_{j}h_{j}.$$
Thì ta có
$$\|e_{0}\|_{A}^{2} = \langle Ae_{0}, e_{0}\rangle = \sum_{i=1}^{n}  a_{i}\lambda_{i} h_{i}, \sum_{j=1}^{n}  a_{j}h_{j}= \sum_{j=1}^{n}  a_{j}^{2}\lambda_{j}$$
Và
$$\|P(A)e_{0}\|_{A}^{2} = \langle AP(A)e_{0}, P(A)e_{0}\rangle = \sum_{i=1}^{n}  a_{i}\lambda_{i} P(\lambda_{i} )h_{i}, \sum_{j=1}^{n}  a_{j}P(\lambda_{j} )h_{j}= \sum_{j=1}^{n}  a_{j}^{2}\lambda_{j} (P(\lambda_{j} ))^{2}.$$

<!-- PAGE 1751 -->
Các phương trình này suy ra rằng
$$\|e_{k}\|_{A} \le \begin{pmatrix} \inf & \max|P(\lambda_{i} )| \\ P\in Pk1\le i\le n \end{pmatrix} \|e_{0}\|_{A} .$$
Nó có thể được được hiển thị rằng gradien liên hợp (conjugate gradient) phương pháp đòi hỏi của thứ tự của $n^{3}$ các phép cộng, $n^{3}$ các phép nhân, 2n các phép chia. Trong lý thuyết, điều này là tệ hơn hơn số của sơ cấp các phép toán cần thiết bởi Cholesky phương pháp. Chẵn/ngay cả dù gradien liên hợp (conjugate gradient) phương pháp thực hiện không dường như là tốt nhất phương pháp cho đầy đủ các ma trận, nó thường outperforms khác các phương pháp cho thưa (sparse) các ma trận. lý do là rằng ma trận $A$ chỉ xuất hiện trong phép tính của vectơ $Ad_{k}$. Nếu ma trận $A$ là banded (ví dụ, ba đường chéo), việc tính toán $Ad_{k}$ là rất cheap và không có cần đến store toàn bộ ma trận $A$, trong mà trường hợp gradien liên hợp (conjugate gradient) phương pháp là fast. Cũng, mặc dù trong lý thuyết, sai khác $n$ các vòng lặp có thể là cần thiết, trong thực tế, sự hội tụ có thể xảy ra sau nhiều nhỏ hơn số của các vòng lặp. Bằng cách sử dụng bất đẳng thức
$$\|e_{k}\|_{A} \le \begin{pmatrix} \inf & \max|P(\lambda_{i} )| \\ P\in Pk1\le i\le n \end{pmatrix} \|e_{0}\|_{A} ,$$
Bằng cách chọn $P$ là shifted Chebyshev đa thức, nó có thể được được hiển thị rằng
$$1^{k}$$
$$\|e_{k}\|_{A} \le 2 \begin{pmatrix} \sqrt \\ \sqrt{\kappa} - \\ \overline{\kappa} + 1 \end{pmatrix} \|e_{0}\|_{A} ,$$
Ở đâu $\kappa  = cond_{2}(A)$; xem Trefethen và Bau $[182]$ (Lecture $38$, Định lý 38.5). Do đó tốc độ của sự hội tụ của gradien liên hợp (conjugate gradient) phương pháp là governed bởi tỉ số
$$\frac{p\overline{cond}_{2}\overline{(}\overline{A}\overline{)} 1}{p\overline{cond}_{2}\overline{(}\overline{A}\overline{) + 1}} -,$$
Ở đâu $cond_{2}(A) = \lambda_{n} /\lambda_{1}$ là số điều kiện (condition number) của ma trận $A$. Vì $A$ là xác định dương (positive definite), $\lambda_{1}$ là của nó nhỏ nhất trị riêng (eigenvalue) và $\lambda_{n}$ là của nó lớn nhất trị riêng (eigenvalue). ở trên sự kiện dẫn đến đến process của preconditioning, phương pháp mà bao gồm trong thay thế ma trận của hệ phương trình tuyến tính Ax $= b$ bởi “tương đương” một ví dụ $M^{-1} A$ (vì $M$ là khả nghịch, hệ Ax $= b$ là tương đương đến hệ $M^{-1}$ Ax $= M^{-1} b)$, ở đâu $M$ được chọn sao cho $M^{-1} A$ là vẫn đối xứng xác định dương (SPD) và có nhỏ hơn số điều kiện (condition number) hơn $A$; xem Trefethen và Bau $[182]$ (Lecture $40)$ và Demmel $[48]$ (Mục 6.6.5).
