# Time-Dependent Biên (boundary) Các bài tập


<!-- PAGE 705 -->
$1$. “Tốt” các tam giác phân phải là tìm thấy. Điều này trong chính nó là vast research topic. Delaunay các tam giác phân là tốt candidates. $2$. “Tốt” các không gian của các hàm phải là tìm thấy; typically từng khúc các đa thức và splines. $3$. “Tốt” các cơ sở bao gồm của các hàm sẽ nhỏ hỗ trợ/giá (support) phải là tìm thấy, sao cho các tích phân có thể được dễ dàng được tính và thưa (sparse) banded các ma trận phát sinh. Ta bây giờ xét biên (boundary) các bài tập ở đâu nghiệm varies với time.

## 19.3 Time-Dependent Biên (boundary) Các bài tập: Wave

$$Equation$$
Xét thuần nhất chuỗi (hoặc rope) của hằng số cross-section, của độ dài $L$, và stretched (trong đứng mặt phẳng) giữa của nó hai kết thúc mà được giả sử là cố định và located dọc theo trục $x$ tại $x = 0$ và tại $x = L$.
$$Figure 19.6: A vibrating string$$
Chuỗi là subjected đến transverse buộc $\tau$ f(x)dx trên mỗi phần tử của độ dài dx (ở đâu $\tau$ là tension của chuỗi). Ta sẽ like đến investigate nhỏ displacements của chuỗi trong đứng mặt phẳng, nghĩa là, cách mà nó vibrates. Do đó, ta seek hàm u(x, $t)$ được định nghĩa cho $t \ge 0$ và $x \in [0, L]$, sao cho u(x, $t)$ biểu diễn đứng deformation của chuỗi tại abscissa $x$ và tại time $t$. Nó có thể được được hiển thị rằng $u$ phải thỏa mãn sau đây PDE
$$\frac{1}{c^{2}} \frac{\partial^{2} u}{\partial t^{2}} (x, t) - \frac{\partial^{2} u}{\partial x^{2}} (x, t) = f(x, t),0 < x < L, t > 0,$$
Với $c = p\overline{\tau /\rho}$, ở đâu $\rho$ là tuyến tính density của chuỗi, đã biết như một chiều wave phương trình. Hơn nữa, ban đầu hình dạng của chuỗi là đã biết tại $t = 0$, cũng như distribution của ban đầu velocities dọc theo chuỗi; nói cách khác, có hai các hàm $u_{i,0}$ và $u_{i,1}$

<!-- PAGE 706 -->
Sao cho
$$u(x, 0) = u_{i,0}(x),0 \le x \le L,$$
$$\frac{\partial u}{\partial t} (x, 0) = u_{i,1}(x),0 \le x \le L.$$
Ví dụ, nếu chuỗi là đơn giản released từ của nó cho trước bắt đầu position, ta có $u_{i,1} = 0$. một cách cuối cùng, bởi vì kết thúc của chuỗi là cố định, ta phải có
$$u(0, t) = u(L, t) = 0,t \ge 0.$$
Hệ quả là, ta nhìn cho hàm $u: \mathbb{R}_{+} \times  [0, L] \to \mathbb{R}$ thỏa mãn sau đây các điều kiện:
$$\frac{1}{c^{2}} \frac{\partial^{2} u}{\partial t^{2}} (x, t) - \frac{\partial^{2} u}{\partial x^{2}} (x, t) = f(x, t),0 < x < L, t > 0,$$
$$u(0, t) = u(L, t) = 0,t \ge 0(boundary condition),$$
$$u(x, 0) = u_{i,0}(x),0 \le x \le L(intitial condition),$$
$$\frac{\partial u}{\partial t} (x, 0) = u_{i,1}(x),0 \le x \le L(intitial condition).$$
Điều này là ví dụ của time-dependent boundary-value bài toán, với hai ban đầu các điều kiện. để đơn giản hóa bài toán, giả sử rằng $f = 0$, mà tương đương với đến neglecting effect của gravity. Trong trường hợp này, của ta PDE trở thành
$$\frac{1}{c^{2}} \frac{\partial^{2} u}{\partial t^{2}} (x, t) - \frac{\partial^{2} u}{\partial x^{2}} (x, t) = 0,0 < x < L, t > 0,$$
Cho chúng ta thử của ta mẹo/kỹ thuật của nhân bởi test hàm $v$ tùy thuộc chỉ trên $x, C^{1}$ trên $[0, L]$, và sao cho v(0) $=$ v(L) $= 0$, và integrate bởi các phần. Ta thu được phương trình
$$\int_{0}^{}  L \frac{\partial^{2} u}{\partial t^{2}} (x, t)v(x)dx -c^{2} \int_{0}^{}  L \frac{\partial^{2} u}{\partial x^{2}} (x, t)v(x)dx = 0.$$
Cho số hạng thứ nhất, ta thu được
$$\int_{0}^{}  L \frac{\partial^{2} u}{\partial t^{2}} (x, t)v(x)dx = \int_{0}^{}  L \frac{\partial^{2}}{\partial t^{2}} [u(x, t)v(x)]dx$$
$$= \frac{d^{2}}{dt^{2}} \int_{0}^{}  Lu(x, t)v(x)dx$$
$$= \frac{d^{2}}{dt^{2}} \langle u, v\rangle ,$$

<!-- PAGE 707 -->
Ở đâu $\langle u, v\rangle$ là tích vô hướng (inner product) trong $L^{2}([0, L])$. sự kiện rằng nó là legitimate đến di chuyển $\partial^{2} /\partial t^{2}$ bên ngoài của tích phân cần là justified một cách chặt chẽ, nhưng ta won’t thực hiện nó ở đây. Cho số hạng thứ hai, ta thu được
$$- \int_{0}^{}  L \frac{\partial^{2} u}{\partial x^{2}} (x, t)v(x)dx = - \frac{\partial u}{\partial x} (x, t)v(x)x=L+ \int_{0}^{}  L \frac{\partial u}{\partial x} (x, t) \frac{dv}{dx} (x)dx,$$
$$x=0$$
Và bởi vì $v \in V$, ta có v(0) $=$ v(L) $= 0$, do đó ta thu được
$$- \int_{0}^{}  L \frac{\partial^{2} u}{\partial x^{2}} (x, t)v(x)dx = \int_{0}^{}  L \frac{\partial u}{\partial x} (x, t) \frac{dv}{dx} (x)dx.$$
Của ta integrated phương trình trở thành
$$\frac{d^{2}}{dt^{2}} \langle u, v\rangle + c^{2} \int_{0}^{}  L \frac{\partial u}{\partial x} (x, t) \frac{dv}{dx} (x)dx = 0,for all v \in Vand all t \ge 0.$$
Nó là tự nhiên đến giới thiệu dạng song tuyến tính (bilinear form): $V \times  V \to \mathbb{R}$ cho trước bởi
$$a(u, v) = \int_{0}^{}  L \frac{\partial u}{\partial x} (x, t) \frac{\partial v}{\partial x} (x, t)dx,$$
Ở đâu, với mọi $t \in \mathbb{R}_{+}$, các hàm u(x, $t)$ và $(v, t)$ thuộc đến $V$. Thực sự, ta có đến thay thế $V$ bởi không gian con của Sobolev không gian $H_{0}^{1}(0, L)$ bao gồm của các hàm sao cho v(0) $=$ v(L) $= 0$. Thì, yếu formulation (variational formulation) của bài toán của chúng ta là điều này: Tìm hàm $u \in V$ sao cho
$$\frac{d^{2}}{dt^{2}} \langle u, v\rangle + a(u, v) = 0,for all v \in Vand all t \ge 0$$
$$u(x, 0) = u_{i,0}(x),0 \le x \le L(intitial condition),$$
$$\frac{\partial u}{\partial t} (x, 0) = u_{i,1}(x),0 \le x \le L(intitial condition).$$
Nó có thể được được hiển thị rằng có một dương hằng số $\alpha  > 0$ sao cho
$$a(u, u) \ge \alpha  \|u\|_{H1}^{2}for all v \in V$$
$$0$$
(Poincar´e’s bất đẳng thức), mà chỉ ra rằng là xác định dương (positive definite) trên $V$. ở trên phương pháp là đã biết như phương pháp của Rayleigh-Ritz. study của ở trên phương trình đòi hỏi một số sophisticated các công cụ của giải tích/phân tích mà vượt xa scope của các phần tử này các lưu ý. Cho chúng ta chỉ nói rằng có một đếm được dãy của các nghiệm với được tách các biến của tạo thành
$$u_{k}^{(1)}= \sin \begin{pmatrix} k\pi x \\ L \end{pmatrix} \cos \begin{pmatrix} k\pi ct \\ L \end{pmatrix} ,u_{k}^{(2)}= \sin \begin{pmatrix} k\pi x \\ L \end{pmatrix} \sin \begin{pmatrix} k\pi ct \\ L \end{pmatrix} ,k \in \mathbb{N}_{+},$$

<!-- PAGE 708 -->
Được gọi là modes (hoặc chuẩn tắc/bình thường modes). Đầy đủ các nghiệm của bài toán là chuỗi thu được bởi combining chuẩn tắc/bình thường modes, và chúng là của tạo thành
$$u(x, t) = \sum_{k=1}^{\infty}  \sin \begin{pmatrix} k\pi x \\ L \end{pmatrix} \begin{pmatrix} k\pi ct \\ A_{k} \cos \\ L \end{pmatrix} \begin{pmatrix} k\pi ct \\ + B_{k} \sin \\ L \end{pmatrix} \begin{pmatrix}\end{pmatrix} ,$$
Ở đâu các hệ số $A_{k}, B_{k}$ được xác định từ Fourier chuỗi của $u_{i,0}$ và $u_{i,1}$. Ta bây giờ xét rời rạc các xấp xỉ của bài toán của chúng ta. Như trước, xét hữu hạn dimensional không gian con $V_{a}$ của $V$ và giả sử rằng ta có các xấp xỉ $u_{a,0}$ và $u_{a,1}$ của $u_{i,0}$ và $u_{i,1}$. Nếu ta chọn cơ sở (basis) $(w_{1}, \dots  , w_{n})$ của $V_{a}$, thì ta có thể viết của ta unknown hàm u(x, $t)$ như
$$u(x, t) = u_{1}(t)w_{1} + \cdots  + u_{n}(t)w_{n},$$
Ở đâu $u_{1}, \dots  , u_{n}$ là các hàm của $t$. Thì, nếu ta viết $u = (u_{1}, \dots  , u_{n})$, rời rạc phiên bản của bài toán của chúng ta là
$$A \frac{d^{2}u}{dt^{2}} + Ku = 0,$$
$$u(x, 0) = u_{a,0}(x),0 \le x \le L,$$
$$\frac{\partial u}{\partial t} (x, 0) = u_{a,1}(x),0 \le x \le L,$$
Ở đâu $A = (\langle w_{i}, w_{j}\rangle$) và $K = (a(w_{i}, w_{j}))$ là hai các ma trận đối xứng, được gọi là mass ma trận và stiffness ma trận, respectively. Thực ra, bởi vì và tích vô hướng (inner product) $\langle$ -, $-\rangle$ là xác định dương (positive definite), các ma trận này là cũng xác định dương (positive definite). Ta có được tạo một số progress vì ta bây giờ có hệ của ODE’s, và ta có thể giải nó bởi analogy với vô hướng (scalar) trường hợp. Do đó, ta nhìn cho các nghiệm của tạo thành $U$ cos $\omega t$ (hoặc $U$ sin $\omega t)$, ở đâu $U$ là $n$ chiều vectơ. Ta tìm rằng ta nên có
$$(K -\omega^{2} A)U \cos \omega t = 0,$$
Mà suy ra rằng $\omega$ phải là nghiệm của phương trình
$$KU = \omega^{2} AU.$$
Do đó, ta có để tìm một số $\lambda$ sao cho
$$KU = \lambda AU,$$
Bài toán đã biết như suy rộng/tổng quát hóa trị riêng (eigenvalue) bài toán, vì thông thường trị riêng (eigenvalue) bài toán cho $K$ là
$$KU = \lambda U.$$

<!-- PAGE 709 -->
May mắn thay, bởi vì $A$ là SPD, ta có thể rút gọn điều này suy rộng/tổng quát hóa trị riêng (eigenvalue) bài toán đến tiêu chuẩn trị riêng (eigenvalue) bài toán. tốt cách đến thực hiện do đó là để sử dụng Phân rã Cholesky (Cholesky decomposition) của $A$ như
$$A = LL^{\top},$$
Ở đâu $L$ là tam giác dưới (lower triangular) ma trận (xem Định lý 8.10). Bởi vì $A$ là SPD, nó là khả nghịch, do đó $L$ là cũng khả nghịch, và
$$KU = \lambda AU = \lambda LL^{\top}U$$
Cho ta
$$L^{-1}KU = \lambda L^{\top}U,$$
Mà có thể cũng được viết như
$$L^{-1}K(L^{\top})^{-1}L^{\top}U = \lambda L^{\top}U.$$
Thì, nếu ta tạo thay đổi của biến
$$Y = L^{\top}U,$$
Bằng cách sử dụng sự kiện $(L^{\top})^{-1} = (L^{-1})^{\top}$, ở trên phương trình là tương đương đến
$$L^{-1}K(L^{-1})^{\top}Y = \lambda Y,$$
Tiêu chuẩn trị riêng (eigenvalue) bài toán cho ma trận $K = L^{-1}K(L^{-1})^{\top}$. Hơn nữa, ta biết
$$b$$
Từ Mục 8.8 rằng vì $K$ là SPD và $L^{-1}$ là khả nghịch, ma trận $K = L^{-1}K(L^{-1})^{\top}$ là
$$b$$
Cũng SPD. Hệ quả là, $K$ có dương thực các trị riêng (eigenvalues) $(\omega_{1}^{2} , \dots  , \omega_{n}^{2}$) (không nhất thiết phân biệt) và
$$b$$
Nó có thể được được chéo hóa đối với cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors), nói $Y^{1}, \dots  , Y^{n}$. Thì, vì $Y = L^{\top}U$, các vectơ
$$U^{i}= (L^{\top})^{-1}Y^{i},i = 1, \dots  , n,$$
Là độc lập tuyến tính (linearly independent) và là các nghiệm của suy rộng/tổng quát hóa trị riêng (eigenvalue) problem; nghĩa là,
$$KU^{i}= \omega_{i}^{2}  AU^{i},i = 1, \dots  , n.$$
Nhiều hơn/thêm là đúng. Bởi vì các vectơ $Y^{1}, \dots  , Y^{n}$ là trực chuẩn, và bởi vì $Y^{i} = L^{\top}U^{i}$, từ
$$(Y^{i})^{\top}Y^{j}= \delta_{ij} ,$$
Ta thu được
$$(U^{i})^{\top}LL^{\top}U^{j}= \delta_{ij} ,1 \le i, j \le n,$$
Và vì $A = LL^{\top}$, điều này cho ta
$$(U^{i})^{\top}AU^{j}= \delta_{ij} ,1 \le i, j \le n.$$

<!-- PAGE 710 -->
Điều này suggests định nghĩa các hàm $U^{i} \in V_{a}$ bởi
$$U^{i}  = \sum_{k=1}^{n}  U_{k}^{i}w_{k}.$$
Thì, nó immediate để kiểm tra rằng
$$a(U^{i}, U^{j}) = (U^{i})^{\top}AU^{j}= \delta_{ij} ,$$
Mà có nghĩa là các hàm $(U^{1} , \dots  , U^{n}$) tạo thành cơ sở trực chuẩn (orthonormal basis) của $V_{a}$ cho tích vô hướng (inner product). các hàm $U^{i} \in V_{a}$ được gọi là modes (hoặc modal các vectơ). Như cuối cùng bước, cho chúng ta nhìn một lần nữa cho nghiệm của của ta rời rạc yếu formulation của bài toán, điều này time biểu diễn unknown nghiệm u(x, $t)$ trên modal cơ sở (basis) $(U^{1} , \dots  , U^{n}$), nói
$$u = \sum_{j=1}^{n}  u_{j}e(t)U^{j} ,$$
Ở đâu mỗi $u_{j}$ là hàm của $t$. Bởi vì
$$e$$
$$! !$$
$$u = \sum_{j=1}^{n}  u_{j}(t)U^{j}  = \sum_{j=1}^{n}  u_{j}(t) \sum_{k=1}^{n}  U_{k}^{j}w_{k}= \sum_{k=1}^{n}  \sum_{j=1}^{n}  u_{j}(t)U_{k}^{j}w_{k},$$
$$eee$$
$$if we write u = (u_{1}, \dots  , u_{n}) with u_{k} = \sum_{j}  n=1u_{j}e(t)U_{k}^{j} for k = 1, \dots  , n, we see that$$
$$u = \sum_{j=1}^{n}  u_{j}eU^{j},$$
Do đó bằng cách sử dụng sự kiện rằng
$$KU^{j}= \omega_{j}^{2} AU^{j},j = 1, \dots  , n,$$
Phương trình
$$A \frac{d^{2}u}{dt^{2}} + Ku = 0$$
Cho ta
$$\sum_{j=1}^{n}  [(u_{j})'' + \omega_{j}^{2} u_{j}]AU^{j} = 0.$$
$$e e$$
Vì $A$ là khả nghịch và vì $(U^{1}, \dots  , U^{n})$ là độc lập tuyến tính (linearly independent), các vectơ $(AU^{1}, \dots  , AU^{n})$ là độc lập tuyến tính (linearly independent), và hệ quả là ta thu được hệ của $n$ ODEs’
$$(u_{j})''+ \omega_{j}^{2} u_{j} = 0,1 \le j \le n.$$
$$e e$$
Mỗi của phương trình này có well-known nghiệm của tạo thành
$$u_{j} = A_{j} \cos \omega_{j} t + B_{j} \sin \omega_{j} t.$$
$$e$$

<!-- PAGE 711 -->
Vì vậy, nghiệm của của ta xấp xỉ bài toán được cho bởi
$$u = \sum_{j=1}^{n}  (A_{j} \cos \omega_{j} t + B_{j} \sin \omega_{j} t)U^{j} ,$$
Và các hằng số $A_{j}, B_{j}$ là thu được từ intial các điều kiện
$$u(x, 0) = u_{a,0}(x),0 \le x \le L,$$
$$\frac{\partial u}{\partial t} (x, 0) = u_{a,1}(x),0 \le x \le L,$$
Bởi biểu diễn $u_{a,0}$ và $u_{a,1}$ trên modal cơ sở (basis) $(U^{1} , \dots  , U^{n}$). Hơn nữa, modal các hàm $(U^{1} , \dots  , U^{n}$) tạo thành cơ sở trực chuẩn (orthonormal basis) của $V_{a}$ cho tích vô hướng (inner product). Nếu ta sử dụng không gian vectơ (vector space) $V_{N}^{0}$ của từng khúc afin các hàm, ta tìm rằng các ma trận $A$ và $K$ là familar! Thật vậy,
$$A = \frac{1}{h} \begin{pmatrix} 2 & -1 & 0 & 0 & 0 \\ -1 & 2 & -1 & 0 & 0 \\ \vdots & \ddots & \ddots & \ddots & \vdots \\ 0 & 0 & -1 & 2 & -1 \\ 0 & 0 & 0 & -1 & 2 \end{pmatrix}$$
Và
$$K = \frac{h}{6} \begin{pmatrix} 4 & 1 & 0 & 0 & 0 \\ 1 & 4 & 1 & 0 & 0 \\ \vdots & \ddots & \ddots & \ddots & \vdots \\ 0 & 0 & 1 & 4 & 1 \\ 0 & 0 & 0 & 1 & 4 \end{pmatrix} .$$
Để kết luận điều này mục, cho chúng ta thảo luận ngắn gọn wave phương trình cho elastic membrane, như được mô tả trong Mục 19.2. Điều này time, ta nhìn cho hàm $u: \mathbb{R}_{+} \times  \Omega \to \mathbb{R}$ thỏa mãn sau đây các điều kiện:
$$\frac{1}{c^{2}} \frac{\partial^{2} u}{\partial t^{2}} (x, t) -\Delta u(x, t) = f(x, t),x \in \Omega , t > 0,$$
$$u(x, t) = 0,x \in \Gamma ,t \ge 0(boundary condition),$$
$$u(x, 0) = u_{i,0}(x),x \in \Omega (intitial condition),$$
$$\frac{\partial u}{\partial t} (x, 0) = u_{i,1}(x),x \in \Omega (intitial condition).$$
Giả sử rằng $f = 0$, ta nhìn cho các nghiệm trong không gian con $V$ của Sobolev không gian $H_{0}^{1}\overline{(\Omega$)} bao gồm của các hàm $v$ sao cho $v = 0$ trên $\Gamma$. Nhân bởi test hàm $v \in V$ và bằng cách sử dụng Xanh lục’s thứ nhất đồng nhất thức, ta thu được yếu formulation của bài toán của chúng ta:

<!-- PAGE 712 -->
Tìm hàm $u \in V$ sao cho
$$\frac{d^{2}}{dt^{2}} \langle u, v\rangle + a(u, v) = 0,for all v \in Vand all t \ge 0$$
$$u(x, 0) = u_{i,0}(x),x \in \Omega (intitial condition),$$
$$\frac{\partial u}{\partial t} (x, 0) = u_{i,1}(x),x \in \Omega (intitial condition),$$
Ở đâu: $V \times  V \to \mathbb{R}$ là dạng song tuyến tính (bilinear form) cho trước bởi
$$a(u, v) = \int_{\Omega}  \begin{pmatrix} \partial u \\ \partial v & \partial u\partial v \\ + \\ \partial x_{1}\partial x_{1} & \partial x_{2}\partial x_{2} \end{pmatrix} dx,$$
$$and \int_{\Omega}$$
$$\langle u, v\rangle =uvdx.$$
Như thông thường, ta tìm các xấp xỉ của bài toán của chúng ta bằng cách sử dụng hữu hạn dimensional các không gian con $V_{a}$ của $V$. Chọn một số cơ sở (basis) $(w_{1}, \dots  , w_{n})$ của $V_{a}$, và triangulating $\Omega$, như trước, ta thu được phương trình
$$A \frac{d^{2}u}{dt^{2}} + Ku = 0,$$
$$u(x, 0) = u_{a,0}(x),x \in \Gamma ,$$
$$\frac{\partial u}{\partial t} (x, 0) = u_{a,1}(x),x \in \Gamma ,$$
Ở đâu $A = (\langle w_{i}, w_{j}\rangle$) và $K = (a(w_{i}, w_{j}))$ là hai đối xứng xác định dương (SPD) các ma trận. Trong nguyên lý, bài toán được giải, nhưng, nó có thể là khó để tìm tốt các không gian $V_{a}$, tốt các tam giác phân của $\Omega$, và tốt các cơ sở của $V_{a}$, là able để tính các ma trận $A$ và $K$, và để đảm bảo rằng chúng là thưa (sparse).
