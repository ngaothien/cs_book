# Trực giao Các nhóm và Cartan–Dieudonné Định lý


<!-- PAGE 1052 -->
$U^{\perp}$. Bằng cách sử dụng nhận xét trước định lý và Mệnh đề 29.37, ta có thể tìm phép trượt (transvection) $\tau$ ánh xạ $W_{i+1}''$ lên $W_{i}'$ và để lại mọi vectơ trong $U$ cố định. Thì, $\tau  \circ g_{i}$ các ánh xạ $(u_{1}, v_{1}, \dots  , u_{i+1}, v_{i+1})$ đến $(u_{1}', v_{1}^{'+1}, \dots  , u_{i+1}', v_{i+1}')$, thiết lập quy nạp bước. Cho thứ hai phát biểu, vì ta đã được chứng minh rằng mọi phép trượt (transvection) có định thức (determinant) bằng $+1$, điều này cũng nghiệm đúng với mọi hợp thành của các phép trượt trong $G$, và vì $G =$ Sp(2m, $K)$, ta được thực hiện. Nó có thể cũng được hiển thị rằng tâm của Sp(2m, $K)$ là rút gọn đến nhóm con ${id, -id}$. xạ ảnh nhóm symplectic (symplectic group) PSp(2m, $K)$ là nhóm thương (quotient group) PSp(2m, $K)/{id, -id}$. Tất cả symplectic xạ ảnh các nhóm là đơn giản, ngoại trừ $PSp(2,\mathbb{F}_{2}), PSp(2,\mathbb{F}_{3})$, và $PSp(4,\mathbb{F}_{2})$, xem Grove $[86]$. các thứ tự của symplectic các nhóm trên hữu hạn các trường có thể được được xác định. Cho chi tiết, xem Artin $[6]$, Jacobson $[101]$ và Grove $[86]$. thú vị tính chất của symplectic các không gian là rằng định thức (determinant) của ma trận phản đối xứng (skew-symmetric matrix) $B$ là square của một số đa thức Pf(B) được gọi là Pfaffian; xem Jacobson $[101]$ và Artin $[6]$. Ta để lại considerations của Pfaffian đến các bài tập. Ta bây giờ lấy nhìn tại trực giao các nhóm.

## 29.9 Trực giao Các nhóm và Cartan–Dieudonn´e

$$Theorem$$
Trong mục này ta là dealing với không suy biến đối xứng song tuyến tính từ $\phi$ trên không gian vectơ hữu hạn chiều $E$ có số chiều $n$ trên trường của characateristic không bằng $2$. Nhắc lại rằng trực giao nhóm $O(\phi$) là nhóm của các phép đẳng cự của $\phi$; rằng là, nhóm của các ánh xạ tuyến tính (linear maps) $f$: $E \to E$ sao cho
$$\phi (f(u), f(v)) = \phi (u, v)for all u, v \in E.$$
Các phần tử của $O(\phi$) cũng được gọi là trực giao các phép biến đổi. Nếu $M$ là ma trận của $\phi$ trong bất kỳ cơ sở (basis), thì ma trận $A$ biểu diễn trực giao phép biến đổi khi và chỉ khi
$$A^{\top}MA = M.$$
Vì $\phi$ là không suy biến, $M$ là khả nghịch, do đó ta xem rằng det() $= \pm 1$. nhóm con
$$SO(\phi ) = {f \in O(\phi ) | \det(f) = 1}$$
Được gọi là đặc biệt trực giao nhóm (của $\phi$), và của nó members được gọi là các phép quay (hoặc thực sự/đúng đắn trực giao các phép biến đổi). Các phép đẳng cự $f \in O(\phi$) sao cho det(f) $= -1$ được gọi là suy rộng/không thực sự trực giao các phép biến đổi, hoặc đôi khi reversions.

<!-- PAGE 1053 -->
Nếu $H$ là bất kỳ không suy biến siêu phẳng (hyperplane) trong $E$, thì $D = H^{\perp}$ là không suy biến đường thẳng và ta có
$$E = H^{\perp}\oplus H^{\perp}.$$
Với mọi khác không vectơ $u \in D = H^{\perp}$ Xét ánh xạ $\tau_{u}$ cho trước bởi
$$\tau_{u} (v) = v -2 \frac{\phi (v, u)}{\phi (u, u)} ufor all v \in E.$$
Nếu ta thay thế $u$ bởi $\lambda u$ với $\lambda  \neq  0$, ta có
$$\tau_{\lambda u} (v) = v -2 \frac{\phi (v, \lambda u)}{\phi (\lambda u, \lambda u)} \lambda u = v -2 \frac{\lambda \phi (v, u)}{\lambda^{2} \phi (u, u)} \lambda u = v -2 \frac{\phi (v, u)}{\phi (u, u)} u,$$
Mà chỉ ra rằng $\tau_{u}$ phụ thuộc chỉ trên đường thẳng $D$, và do đó chỉ siêu phẳng (hyperplane) $H$. Vì vậy, ký hiệu bởi $\tau_{H}$ ánh xạ tuyến tính (linear map) $\tau_{u}$ được xác định như ở trên bởi bất kỳ khác không vectơ $u \in H^{\perp}$. Lưu ý rằng nếu $v \in H$, thì
$$\tau_{H} (v) = v,$$
Và nếu $v \in D$, thì
$$\tau_{H} (v) = -v.$$
Đơn giản phép tính chỉ ra rằng
$$\phi (\tau_{H} (u), \tau_{H} (v)) = \phi (u, v)for all u, v \in E,$$
Do đó $\tau_{H}  \in O(\phi$), và bởi chọn cơ sở (basis) bao gồm của $u$ và các vectơ trong $H$, rằng $det(\tau_{H}$) $= -1$. Nó là cũng rõ ràng rằng $\tau_{H}^{2}   =$ id.

> **Định nghĩa 29.21.** Nếu $H$ là bất kỳ không suy biến siêu phẳng (hyperplane) trong $E$, với mọi khác không vectơ $u \in H^{\perp}$, ánh xạ tuyến tính (linear map) $\tau_{H}$ cho trước bởi
$$\tau_{H} (v) = v -2 \frac{\phi (v, u)}{\phi (u, u)} ufor all v \in E$$
Là involutive phép đẳng cự (isometry) của $E$ được gọi là phép đối xứng (reflection) qua (hoặc về) siêu phẳng (hyperplane) $H$.
Các nhận xét: $1$. Nó có thể được được hiển thị rằng nếu $f \in O(\phi$) để lại mọi vectơ trong một số siêu phẳng (hyperplane) $H$ cố định, thì hoặc $f =$ id hoặc $f = \tau_{H}$; xem Taylor $[180]$ (Chương $11)$. Do đó, không có tương tự đến symplectic các phép trượt trong trực giao nhóm. $2$. Nếu $K = \mathbb{R}$ và $\phi$ là thông thường Euclidean tích vô hướng (inner product), các ma trận tương ứng với siêu phẳng (hyperplane) các phép đối xứng được gọi là Householder các ma trận. Của ta mục tiêu là để chứng minh rằng $O(\phi$) được sinh bởi siêu phẳng (hyperplane) các phép đối xứng. sau đây mệnh đề là cần thiết.

<!-- PAGE 1054 -->

> **Mệnh đề 29.39.** Cho $\phi$ là không suy biến dạng song tuyến tính đối xứng trên không gian vectơ (vector space) $E$. Với mọi hai khác không các vectơ $u, v \in E$, nếu $\phi (u, u) = \phi (v, v)$ và $v$ - $u$ là nonisotropic, thì siêu phẳng (hyperplane) phép đối xứng (reflection) $\tau_{H}  = \tau_{v-u}$ các ánh xạ $u$ đến $v$, với $H =$ (K(v - $u))^{\perp}$.

*Chứng minh.* Vì $v$ - $u$ là không đẳng hướng, $\phi (v$ - $u, v$ - $u) \neq  0$, và ta có
$$-$$
$$\tau_{v-u} (u) = u -2 \frac{\phi (u, vu)}{\phi (v -u, v -u)} (v -u)$$
$$-$$
$$= u -2 \frac{\phi (u, v)\phi (u, u)}{\phi (v, v) -2\phi (u, v) + \phi (u, u)} (v -u)$$
$$-$$
$$= u - \frac{2(\phi (u, v)\phi (u, u))}{2(\phi (u, u) -2\phi (u, v))} (v -u)$$
$$= v,$$
Mà chứng minh mệnh đề. Ta có thể bây giờ thu được cheap phiên bản của Cartan–Dieudonn´e định lý.

> **Định lý 29.40.** (Cartan–Dieudonn´e, yếu tạo thành) Cho $\phi$ là không suy biến dạng song tuyến tính đối xứng trên vectơ $K$ không gian $E$ có số chiều $n$ (char(K) $\neq  2)$. Thì, mọi phép đẳng cự (isometry) $f \in O(\phi$) với $f \neq$ id là hợp thành của nhiều nhất 2n - $1$ siêu phẳng (hyperplane) các phép đối xứng.

*Chứng minh.* Ta tiến hành bằng quy nạp theo $n$. Cho $n = 0$, điều này là tầm thường (vì $O(\phi$) $= {id})$. Tiếp theo, giả sử rằng $n \ge 1$. Vì $\phi$ là không suy biến, ta biết rằng tồn tại một nonisotropic vectơ $u \in E$. Có ba các trường hợp. Trường hợp $1$. f(u) $= u$. Vì $\phi$ là nondegenrate và $u$ là nonisotropic, siêu phẳng (hyperplane) $H = (Ku)^{\perp}$ là không suy biến, $E = H^{\perp}\oplus$ Ku, và vì f(u) $= u$, ta phải có f(H) $= H$. thu hẹp f' của của $f$ đến $H$ là phép đẳng cự (isometry) của $H$. Theo giả thiết quy nạp, ta có thể viết
$$f'= \tau_{k}'  \circ \cdots  \circ \tau_{1}' ,$$
Ở đâu $\tau_{i}$ là một số siêu phẳng (hyperplane) phép đối xứng (reflection) về siêu phẳng (hyperplane) $L_{i}$ trong $H$, với $k \le$ 2n - $3$. Ta có thể mở rộng mỗi $\tau_{i}'$ đến phép đối xứng (reflection) $\tau_{i}$ về siêu phẳng (hyperplane) $L_{i}^{\perp}\oplus$ Ku sao cho $\tau_{i} (u) = u$, và rõ ràng,
$$f = \tau_{k}  \circ \cdots  \circ \tau_{1} .$$
Trường hợp $2$. f(u) $= -u$. Nếu $\tau$ là siêu phẳng (hyperplane) phép đối xứng (reflection) về siêu phẳng (hyperplane) $H = (Ku)^{\perp}$, thì $g = \tau  \circ f$ là phép đẳng cự (isometry) của $E$ sao cho g(u) $= u$, và ta là quay lại đến Trường hợp $(1)$. Vì $\tau^{2} = 1$ Ta thu được
$$f = \tau  \circ \tau_{k}  \circ \cdots  \circ \tau_{1}$$

<!-- PAGE 1055 -->
Ở đâu $\tau$ và $\tau_{i}$ là siêu phẳng (hyperplane) các phép đối xứng, với $k \ge$ 2n - $3$, và ta thu được tổng của 2n - $2$ siêu phẳng (hyperplane) các phép đối xứng. Trường hợp $3$. f(u) $\neq  u$ và f(u) $\neq  -u$. Lưu ý rằng f(u) - $u$ và f(u) $+ u$ là trực giao, vì
$$\phi (f(u) -u, f(u) + u) = \phi (f(u), f(u)) + \phi (f(u), u) -\phi (u, f(u)) -\phi (u, u)$$
$$= \phi (u, u) -\phi (u, u) = 0.$$
Ta cũng có
$$\phi (u, u) = \phi ((f(u) + u -(f(u) -u))/2, (f(u) + u -(f(u) -u))/2)$$
$$= \frac{1}{4} \phi (f(u) + u, f(u) + u) + \frac{1}{4} \phi (f(u) -u, f(u) -u),$$
Do đó f(u) $+ u$ và f(u) - $u$ không thể là cả hai đẳng hướng, vì $u$ là không đẳng hướng. Nếu f(u) - $u$ là không đẳng hướng, thì phép đối xứng (reflection) $\tau_{f(u)-u}$ là sao cho
$$\tau_{f(u)-u} (u) = f(u),$$
Và vì $\tau_{f(u)-u}^{2}   =$ id, nếu $g = \tau_{f(u)-u}  \circ f$, thì g(u) $= u$, và ta là quay lại đến trường hợp $(1)$. Ta thu được
$$f = \tau_{f(u)-u}  \circ \tau_{k}  \circ \cdots  \circ \tau_{1}$$
Ở đâu $\tau_{f(u)-u}$ và $\tau_{i}$ là siêu phẳng (hyperplane) các phép đối xứng, với $k \ge$ 2n - $3$, và ta thu được tổng của 2n - $2$ siêu phẳng (hyperplane) các phép đối xứng. Nếu f(u) $+ u$ là không đẳng hướng, thì phép đối xứng (reflection) $\tau_{f(u)+u}$ là sao cho
$$\tau_{f(u)+u} (u) = -f(u),$$
Và vì $\tau_{f(u)+u}^{2}   =$ id, nếu $g = \tau_{f(u)+u}  \circ f$, thì g(u) $= -u$, và ta là quay lại đến trường hợp $(2)$. Ta thu được
$$f = \tau_{f(u)-u}  \circ \tau  \circ \tau_{k}  \circ \cdots  \circ \tau_{1}$$
Ở đâu $\tau , \tau_{f(u)-u}$ và $\tau_{i}$ là siêu phẳng (hyperplane) các phép đối xứng, với $k \ge$ 2n - $3$, và ta thu được tổng của 2n - $1$ siêu phẳng (hyperplane) các phép đối xứng. Điều này chứng minh quy nạp bước. cận 2n - $1$ là không tối ưu. mạnh phiên bản của Cartan–Dieudonn´e định lý nói rằng rằng nhiều nhất $n$ các phép đối xứng là cần thiết, nhưng chứng minh là khó hơn. Ở đây là neat chứng minh do $E$. Artin (xem $[6]$, Chương III, Mục $4)$. Trường hợp $1$ vẫn còn unchanged. Trường hợp $2$ là slightly khác nhau: f(u) - $u \neq  0$ là không đẳng hướng. Vì $\phi$ (f(u) $+ u$, f(u) - $u) = 0$, như trong thứ nhất subcase của Trường hợp $(3), g = \tau_{f(u)-u}  \circ f$ là sao cho g(u) $= u$ và ta là quay lại đến Trường hợp $1$. Điều này chỉ chi phí một nhiều hơn/thêm phép đối xứng (reflection). mới (xấu) trường hợp là:

<!-- PAGE 1056 -->
Trường hợp 3’. f(u) - $u$ là khác không và đẳng hướng với mọi nonisotropic $u \in E$. Trong trường hợp này, những gì saves chúng ta là rằng $E$ phải là Artinian không gian có số chiều $n =$ 2m và rằng $f$ phải là phép quay $(f \in SO(\phi$)). Nếu ta acccept sự kiện này được chứng minh trong Mệnh đề 29.43 thì chọn bất kỳ siêu phẳng (hyperplane) phép đối xứng (reflection) $\tau$. Thì, vì $f$ là phép quay, $g = \tau  \circ f$ là không phép quay bởi vì det(g) $= det(\tau$) det(f) $= (-1)(+1) = -1$, do đó g(u) - $u$ là hoặc $0$ hoặc không đẳng hướng với một số nonisotropic $u \in E$ (ngược lại, $g$ sẽ là phép quay), ta là quay lại đến hoặc Trường hợp $1$ hoặc Trường hợp $2$, và bằng cách sử dụng giả thiết quy nạp (induction hypothesis), ta thu được
$$\tau  \circ f = \tau_{k}  \circ \dots  , \tau_{1} ,$$
Ở đâu mỗi $\tau_{i}$ là siêu phẳng (hyperplane) phép đối xứng (reflection), và $k \le$ 2m. Vì $\tau  \circ f$ là không phép quay, thực sự $k \le$ 2m $-1$, và thì $f = \tau  \circ \tau_{k}  \circ \dots  , \tau_{1}$, hợp thành của nhiều nhất $k + 1 \le$ 2m siêu phẳng (hyperplane) các phép đối xứng. Vì vậy, ngoại trừ cho sự kiện rằng trong Trường hợp 3’, $E$ phải là Artinian không gian có số chiều $n =$ 2m và rằng $f$ phải là phép quay, mà có không đã được được chứng minh vẫn chưa, ta được chứng minh sau đây định lý.

> **Định lý 29.41.** (Cartan–Dieudonn´e, mạnh tạo thành) Cho $\phi$ là không suy biến dạng song tuyến tính đối xứng trên vectơ $K$ không gian $E$ có số chiều $n$ (char(K) $\neq  2)$. Thì, mọi phép đẳng cự (isometry) $f \in O(\phi$) với $f \neq$ id là hợp thành của nhiều nhất $n$ siêu phẳng (hyperplane) các phép đối xứng. Đến fill trong khoảng cách, ta cần hai các mệnh đề.

> **Mệnh đề 29.42.** Cho $(E, \phi$) là Artinian không gian có số chiều 2m, và cho $U$ là một cách tổng đẳng hướng không gian con có số chiều $m$. Với mọi phép đẳng cự (isometry) $f \in O(\phi$), nếu f(U) $= U$, thì det(f) $= 1 (f$ là phép quay).

*Chứng minh.* Ta biết rằng ta có thể tìm cơ sở (basis) $(u_{1}, \dots  , u_{m}, v_{1}, \dots  , v_{m})$ của $E$ như vậy $(u_{1}, \dots  , u_{m})$ là cơ sở (basis) của $U$ và $\phi$ được biểu diễn bởi ma trận
$$\begin{pmatrix} 0 & I_{m} \\ I_{m} & 0 \end{pmatrix} .$$
Vì f(U) $= U$, ma trận biểu diễn $f$ là của tạo thành
$$A = \begin{pmatrix} B & C \\ 0 & D \end{pmatrix} .$$
Điều kiện $A^{\top}A_{m,m}A = A_{m,m}$ translates như
$$\begin{pmatrix} B^{\top} & 0 \\ C^{\top} & D^{\top} \end{pmatrix} \begin{pmatrix} 0 & I_{m} \\ I_{m} & 0 \end{pmatrix} \begin{pmatrix} B & C \\ 0 & D \end{pmatrix} = \begin{pmatrix} 0 & I_{m} \\ I_{m} & 0 \end{pmatrix}$$
Rằng là,
$$\begin{pmatrix} B^{\top} & 0 \\ C^{\top} & D^{\top} \end{pmatrix} \begin{pmatrix} 0 \\ D \\ B & C \end{pmatrix} = \begin{pmatrix} 0 & B^{\top}D \\ D^{\top}B & C^{\top}D + D^{\top}C \end{pmatrix} = \begin{pmatrix} 0 & I_{m} \\ I_{m} & 0 \end{pmatrix} ,$$

<!-- PAGE 1057 -->
Mà suy ra rằng $B^{\top}D =$ I, và do đó
$$\det(A) = \det(B) \det(D) = \det(B^{\top}) \det(D) = \det(B^{\top}D) = \det(I) = 1,$$
Như đã khẳng định

> **Mệnh đề 29.43.** Cho $\phi$ là không suy biến dạng song tuyến tính đối xứng trên không gian $E$ có số chiều $n$, và cho $f$ là bất kỳ phép đẳng cự (isometry) $f \in O(\phi$) sao cho f(u)-u là khác không và đẳng hướng với mọi nonisotropic vectơ $u \in E$. Thì, $E$ là Artinian không gian có số chiều $n =$ 2m, và $f$ là phép quay $(f \in SO(\phi$)).

*Chứng minh.* Ta suy ra $E$. Artin’s chứng minh (xem $[6]$, Chương III, Mục $4)$. Thứ nhất, xét trường hợp $n = 2$. Vì ta là giả sử rằng $E$ có một số khác không vectơ đẳng hướng (isotropic vector), theo Mệnh đề 29.26, $E$ là Artinian mặt phẳng và có một cơ sở (basis) trong mà $\phi$ được biểu diễn bởi ma trận
$$\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} ,$$
Ta có $\phi ((x_{1}, x_{2}), (x_{1}, x_{2})) = 2x_{1}x_{2}$, và các ma trận biểu diễn các phép đẳng cự là của tạo thành
$$\begin{pmatrix} \lambda & 0 \\ 0 & \lambda^{-1} \end{pmatrix} or \begin{pmatrix} 0 & \lambda \\ \lambda^{-1} & 0 \end{pmatrix} ,\lambda  \in K -{0}.$$
Trong trường hợp thứ hai,
$$\begin{pmatrix} 0 & \lambda \\ \lambda^{-1} & 0 \end{pmatrix} \begin{pmatrix} \lambda \\ 1 \end{pmatrix} = \begin{pmatrix} \lambda \\ 1 \end{pmatrix} ,$$
Nhưng $u = (\lambda , 1)$ là nonisotropic vectơ sao cho f(u) $-u = 0$. Vì vậy, ta phải là trong trường hợp thứ nhất, và det(f) $= +1$. Bây giờ ta giả sử rằng $n \ge 3$. Ta là đi để chứng minh rằng f(y) - $y$ là đẳng hướng với mọi khác không đẳng hướng các vectơ $y$. Cho $y$ là bất kỳ khác không vectơ đẳng hướng (isotropic vector). Vì $n \ge 3$, trực giao không gian $(Ky)^{\perp}$ có số chiều ít nhất $2$, và ta biết rằng rad(Ky) $= rad((Ky)^{\perp})$, không gian có số chiều nhiều nhất $1$, mà suy ra rằng $(Ky)^{\perp}$ chứa một số nonisotropic vectơ, nói $x$. Ta có $\phi (x, y) = 0$, do đó $\phi (x + \epsilon y, x + \epsilon y) = \phi (x$, x)̸ $= 0$, cho $\epsilon  = \pm 1$. Thì, bởi giả thiết, các vectơ f(x) - $x$, f(x $+ y)$ - $(x + y) =$ f(x) - $x +$ (f(y) - $y)$, và f(x $-y)$ -(x $-y) =$ f(x) $-x$ -(f(y) $-y)$ là đẳng hướng. cuối cùng hai các vectơ có thể được viết dưới dạng f(x) - $x) + \epsilon$ (f(y) - $y)$ với $\epsilon  = \pm 1$, do đó ta có $0 = \phi$ (f(x) - $x) + \epsilon$ (f(y) - $y)$, f(x) - $x) + \epsilon$ (f(y) - $y))$
$$= 2\epsilon \phi (f(x) -x, f(y) -y)) + \epsilon^{2} \phi (f(y) -y, f(y) -y).$$
Nếu ta viết hai các phương trình tương ứng với $\epsilon  = \pm 1$, và thì cộng chúng lên, ta thu được
$$\phi (f(y) -y, f(y) -y) = 0.$$

<!-- PAGE 1058 -->
Điều này chứng tỏ rằng f(y)-y là đẳng hướng với mọi khác không vectơ đẳng hướng (isotropic vector) $y$. Vì bởi giả thiết f(u) $-u$ là đẳng hướng với mọi nonisotropic vectơ $u$, ta được chứng minh rằng f(u) $-u$ là đẳng hướng với mọi $u \in E$. Nếu ta cho $W =$ Im(f - id), thì mọi vectơ trong $W$ là đẳng hướng, và do đó $W$ là một cách tổng đẳng hướng (nhắc lại rằng ta được giả sử rằng char(K) $\neq  2$, do đó $\phi$ được xác định bởi $\Phi$). Với mọi $u \in E$ và bất kỳ $v \in W^{\perp}$, vì $W$ là một cách tổng đẳng hướng, ta có
$$\phi (f(u) -u, f(v) -v) = 0,$$
Và vì f(u) - $u \in W$ và $v \in W^{\perp}$, ta có $\phi$ (f(u) - $u, v) = 0$, và do đó
$$0 = \phi (f(u) -u, f(v) -v)$$
$$= \phi (f(u), f(v)) -\phi (u, f(v)) -\phi (f(u) -u, v)$$
$$= \phi (u, v) -\phi (u, f(v))$$
$$= \phi (u, v -f(v)),$$
Với mọi $u \in E$. Vì $\phi$ là không suy biến, điều này có nghĩa là f(v) $= v$, với mọi $v \in W^{\perp}$. Tuy nhiên, bởi giả thiết, không có nonisotropic vectơ là trái cố định, mà suy ra rằng $W^{\perp}$ là cũng một cách tổng đẳng hướng. Trong tóm tắt, ta được chứng minh rằng $W \subseteq W^{\perp}$ và $W^{\perp} \subseteq W^{\perp \perp} = W$, nghĩa là,
$$W = W^{\perp} .$$
Vì, dim(W) $+ dim(W^{\perp}$) $= n$, ta kết luận rằng $W$ là một cách tổng đẳng hướng không gian con của $E$ sao cho
$$\dim(W) = n/2.$$
Theo Mệnh đề 29.29, không gian $E$ là Artinian không gian có số chiều $n =$ 2m. Vì $W = W^{\perp}$ và f(W) $= W$, theo Mệnh đề 29.42, phép đẳng cự (isometry) $f$ là phép quay.
Các nhận xét: $1$. Một cái khác cách đến hoàn tất chứng minh của Mệnh đề 29.43 là để chứng minh rằng nếu $f$ là phép đẳng cự (isometry), thì
$$\mathrm{Ker} (f -id) = (\mathrm{Im}(f -id))^{\perp}.$$
Sau có được chứng minh rằng $W =$ Im(f - id) là một cách tổng đẳng hướng, ta thu được
$$\mathrm{Ker} (f -id) = \mathrm{Im}(f -id),$$
Mà suy ra rằng $(f$ - $id)^{2} = 0$. Từ điều này, ta suy ra rằng det(f) $= 1$. Cho chi tiết, xem Jacobson $[101]$ (Chương $6$, Mục $6). 2$. Nếu $f = \tau_{Hk}  \circ \cdots  \circ \tau_{H1}$, ở đâu $H_{i}$ là các siêu phẳng, thì nó có thể được được hiển thị rằng
$$\dim(H_{1} \cap H_{2} \cap \cdots  \cap H_{s}) \ge n -s.$$
Bây giờ, vì mỗi $H_{i}$ là trái cố định bởi $\tau_{Hi}$, ta xem rằng mọi vectơ trong $H_{1} \cap \cdots  \cap H_{s}$ là trái cố định bởi $f$. Đặc biệt, nếu $s < n$, thì $f$ có một số khác không cố định điểm. Hệ quả là, phép đẳng cự (isometry) mà không có cố định các điểm đòi hỏi $n$ siêu phẳng (hyperplane) các phép đối xứng.
