# Cơ bản Các tính chất của Các nhân xác định dương


<!-- PAGE 1952 -->

## 53.2 Cơ bản Các tính chất của Các nhân xác định dương

Mệnh đề 53.1 suggests thứ hai cách tiếp cận đến hạt nhân (kernel) các hàm mà thực hiện không giả sử rằng đặc trưng (feature) không gian và đặc trưng (feature) ánh xạ là miễn là/được cung cấp. Ta sẽ xem trong Mục 53.3 rằng hai các cách tiếp cận là tương đương. thứ hai cách tiếp cận là hữu ích trong thực tế bởi vì nó là thường khó để định nghĩa đặc trưng (feature) không gian và đặc trưng (feature) ánh xạ trong đơn giản cách thức.

> **Định nghĩa 53.2.** Cho $X$ là khác rỗng tập hợp. hàm $\kappa$: $X \times X \to \mathbb{C}$ là nhân xác định dương (positive definite kernel) nếu với mọi hữu hạn tập con $S = {x_{1}, \dots  , x_{p}}$ của $X$, nếu $K_{S}$ là ma trận cỡ $p \times  p$
$$K_{S} = (\kappa (x_{j}, x_{i}))_{1\le i,j\le p}$$
Được gọi là Gram ma trận, thì ta có
$$u^{*}K_{S} u = \sum_{i,j=1}^{p}  \kappa (x_{i}, x_{j})u_{i}\overline{u}_{j} \ge 0,for all u \in \mathbb{C}^{p}.$$
Nhận thấy rằng Định nghĩa 53.2 thực hiện không đòi hỏi rằng $u^{*}K_{S} u > 0$ nếu $u \neq  0$, do đó thuật ngữ xác định dương (positive definite) là bit abusive, và nó sẽ là nhiều hơn/thêm thích hợp để sử dụng thuật ngữ nửa xác định dương (positive semidefinite). Tuy nhiên, nó dường như thông lệ để sử dụng số hạng nhân xác định dương (positive definite kernel), hoặc chẵn/ngay cả dương hạt nhân (kernel).

> **Mệnh đề 53.2.** Cho $\kappa$: $X \times  X \to \mathbb{C}$ là nhân xác định dương (positive definite kernel). Thì $\kappa (x, x) \ge 0$ với mọi $x \in X$, và với mọi hữu hạn tập con $S = {x_{1}, \dots  , x_{p}}$ của $X$, ma trận cỡ $p \times  p$ $K_{S}$ cho trước bởi
$$K_{S} = (\kappa (x_{j}, x_{i}))_{1\le i,j\le p}$$
Là Hermite, nghĩa là, $K_{S}^{*} = K_{S}$.

*Chứng minh.* thứ nhất tính chất là hiển nhiên bằng cách chọn $S = {x}$. để chứng minh rằng $K_{S}$ là Hermite, nhận thấy rằng ta có
$$(u + v)^{*}K_{S}(u + v) = u^{*}K_{S}u + u^{*}K_{S}v + v^{*}K_{S}u + v^{*}K_{S}v,$$
Và vì $(u + v)^{*}K_{S}(u + v), u^{*}K_{S}u, v^{*}K_{S}v \ge 0$, ta suy ra rằng
$$2A = u^{*}K_{S}v + v^{*}K_{S}u(1)$$
Phải là thực. Bằng cách thay thế $u$ bởi iu, ta xem rằng
$$2B = -iu^{*}K_{S}v + iv^{*}K_{S}u(2)$$
Phải cũng là thực. Bằng cách nhân Phương trình $(2)$ bởi $i$ và cộng nó đến Phương trình $(1)$ ta thu được
$$u^{*}K_{S}v = A + iB.(3)$$

<!-- PAGE 1953 -->
Bằng cách trừ Phương trình $(3)$ từ Phương trình $(1)$ ta thu được
$$v^{*}K_{S}u = A -iB.$$
Thì
$$u^{*}K_{S}^{*}v =\overline{v}^{*}\overline{K}_{S}\overline{u} =\overline{A}\overline{-}\overline{iB} = A + iB = u^{*}K_{S}v,$$
Với mọi $u, v \in \mathbb{C}^{*}$, mà suy ra $K_{S}^{*} = K_{S}$. Nếu ánh xạ $\kappa$: $X \times  X \to \mathbb{R}$ là nhận giá trị thực (real-valued), thì ta có kết quả sau tiêu chuẩn cho $\kappa$ là nhân xác định dương (positive definite kernel) rằng chỉ liên quan đến thực các vectơ.

> **Mệnh đề 53.3.** Nếu $\kappa$: $X \times  X \to \mathbb{R}$, thì $\kappa$ là nhân xác định dương (positive definite kernel) khi và chỉ khi với mọi hữu hạn tập con $S = {x_{1}, \dots  , x_{p}}$ của $X$, $p \times  p$ thực ma trận $K_{S}$ cho trước bởi
$$K_{S} = (\kappa (x_{k}, x_{j}))_{1\le j,k\le p}$$
Là đối xứng, nghĩa là, $K_{S}^{\top} = K_{S}$, và
$$u^{\top}K_{S} u = \sum_{j,k=1}^{p}  \kappa (x_{j}, x_{k})u_{j}u_{k} \ge 0,for all u \in \mathbb{R}^{p}.$$

*Chứng minh.* Nếu $\kappa$ là nhận giá trị thực (real-valued) nhân xác định dương (positive definite kernel), thì mệnh đề là tầm thường hệ quả của Mệnh đề 53.2. Cho điều ngược lại giả sử rằng $\kappa$ là đối xứng và rằng nó thỏa mãn điều kiện thứ hai của mệnh đề. Ta cần để chỉ ra rằng $\kappa$ là nhân xác định dương (positive definite kernel) đối với phức các vectơ. Nếu ta viết $u_{k} = a_{k} + ib_{k}$, thì
$$u^{*}K_{S} u = \sum_{j,k=1}^{p}  \kappa (x_{j}, x_{k})(a_{j} + ib_{j})(a_{k} -ib_{k})$$
$$= \sum_{j,k=1}^{p}  (a_{j}a_{k} + b_{j}b_{k})\kappa (x_{j}, x_{k}) + i \sum_{j,k=1}^{p}  (b_{j}a_{k} -a_{j}b_{k})\kappa (x_{j}, x_{k})$$
$$= \sum_{j,k=1}^{p}  (a_{j}a_{k} + b_{j}b_{k})\kappa (x_{j}, x_{k}) + i \sum_{\le j<k\le}  b_{j}a_{k}(\kappa (x_{j}, x_{k}) -\kappa (x_{k}, x_{j})).$$
$$1p$$
Do đó $u^{*}K_{S}u$ là thực khi và chỉ khi $K_{S}$ là đối xứng. Hệ quả là ta tạo sau đây định nghĩa.

> **Định nghĩa 53.3.** Cho $X$ là khác rỗng tập hợp. hàm $\kappa$: $X \times  X \to \mathbb{R}$ là (thực) nhân xác định dương (positive definite kernel) nếu $\kappa (x, y) = \kappa (y, x)$ với mọi $x, y \in X$, và với mọi hữu hạn tập con $S = {x_{1}, \dots  , x_{p}}$ của $X$, nếu $K_{S}$ là $p \times  p$ thực ma trận đối xứng (symmetric matrix)
$$K_{S} = (\kappa (x_{i}, x_{j}))_{1\le i,j\le p},$$

<!-- PAGE 1954 -->
Thì ta có
$$u^{\top}K_{S} u = \sum_{i,j=1}^{p}  \kappa (x_{i}, x_{j})u_{i}u_{j} \ge 0,for all u \in \mathbb{R}^{p}.$$
Trong số khác things, tiếp theo mệnh đề chỉ ra rằng nhân xác định dương (positive definite kernel) thỏa mãn Cauchy–Schwarz bất đẳng thức.

> **Mệnh đề 53.4.** Hermite $2 \times  2$ ma trận
$$A = \begin{pmatrix} a & \overline{b} \\ b & d \end{pmatrix}$$
Là nửa xác định dương (positive semidefinite) khi và chỉ khi $a \ge 0, d \ge 0$, và ad $-|b|^{2} \ge 0$. Cho $\kappa$: $X \times  X \to \mathbb{C}$ là nhân xác định dương (positive definite kernel). Với mọi $x, y \in X$, ta có
$$|\kappa (x, y)|^{2}\le \kappa (x, x)\kappa (y, y).$$

*Chứng minh.* Với mọi $x, y \in \mathbb{C}$, ta có
$$\begin{pmatrix} \overline{x} & \overline{y} \end{pmatrix} \begin{pmatrix} a & \overline{b} \\ b & d \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} \overline{x} & \overline{y} \end{pmatrix} \begin{pmatrix} ax +\overline{by} \\ bx + dy \end{pmatrix}$$
$$= a|x|^{2}+\overline{bxy} +\overline{bxy} + d|y|^{2}.$$
$$If A is positive semidefinite, then we already know \frac{that}{\overline{bxy},} a \ge 0 and d \ge 0. If a = 0, then$$
Ta phải có $b = 0$, vì ngược lại ta có thể tạo $\overline{bxy} +$ mà là hai lần thực phần của $\overline{bxy}$, như âm như ta muốn. Trong trường hợp này, ad $-|b|^{2} = 0$. Nếu $> 0$, thì
$$\overline{b}^{2} ||^{2}$$
$$a|x|^{2}+\overline{bxy} +\overline{bxy} + d|y|^{2}= ax +\overline{a} y+ \frac{y}{a} (ad -|b|^{2}).$$
Nếu $ad-|b|^{2} < 0$, ta có thể chọn $y \neq  0$ và $x = -(\overline{by})/a$, sao cho ở trên biểu thức là âm. Vì vậy, ad $-|b|^{2} \ge 0$. điều ngược lại là tầm thường. Nếu $x = y$, bất đẳng thức $|\kappa (x, y)|^{2} \le \kappa (x, x)\kappa (y, y)$ là tầm thường. Nếu x̸ $= y$, bất đẳng thức suy ra bằng cách áp dụng tiêu chuẩn cho đang là nửa xác định dương (positive semidefinite) đến ma trận
$$\begin{pmatrix} \kappa (x, x) & \overline{\kappa}\overline{(}\overline{x, y}\overline{)} \\ \kappa (x, y) & \kappa (y, y) \end{pmatrix} ,$$
Như đã khẳng định. sau đây tính chất do I. Schur $(1911)$ chỉ ra rằng từng điểm tích của hai các nhân xác định dương là cũng nhân xác định dương (positive definite kernel).

<!-- PAGE 1955 -->

> **Mệnh đề 53.5.** (I. Schur) Nếu $\kappa_{1}$: $X \times  X \to \mathbb{C}$ và $\kappa_{2}$: $X \times  X \to \mathbb{C}$ là hai các nhân xác định dương, thì hàm $\kappa$: $X \times  X \to \mathbb{C}$ cho trước bởi $\kappa (x, y) = \kappa_{1} (x, y)\kappa_{2} (x, y)$ với mọi $x, y \in X$ là cũng nhân xác định dương (positive definite kernel).

*Chứng minh.* Nó suffices để chứng minh rằng nếu $A = (a_{jk})$ và $B = (b_{jk})$ là hai Hermite nửa xác định dương (positive semidefinite) $p \times  p$ các ma trận, thì do đó là của chúng từng điểm tích $C = A \circ B = (a_{jk}b_{jk})$ (cũng đã biết như Hadamard hoặc Schur tích). Nhắc lại rằng Hermite nửa xác định dương (positive semidefinite) ma trận $A$ có thể được được chéo hóa như $A = U\Lambda U^{*}$, ở đâu $\Lambda$ là ma trận đường chéo (diagonal matrix) với không âm các phần tử (entries) và $U$ là ma trận unita (unitary matrix). Cho $\Lambda^{1/2}$ là ma trận đường chéo (diagonal matrix) bao gồm của dương square các nghiệm của đường chéo các phần tử (entries) trong $\Lambda$. Thì ta có
$$A = U\Lambda U^{*} = U\Lambda^{1/2} \Lambda^{1/2} U^{*} = U\Lambda^{1/2} (U\Lambda^{1/2} )^{*}.$$
Do đó nếu ta tập hợp $R = U\Lambda^{1/2}$, ta có
$$A = RR^{*},$$
Mà có nghĩa là
$$a_{jk} = \sum_{h=1}^{p}  r_{jh}\overline{r}_{kh}.$$
Thì với mọi $u \in \mathbb{C}^{p}$, ta có
$$u^{*}(A \circ B)u = \sum_{j,k=1}^{p}  a_{jk}b_{jk}u_{j}\overline{u}_{k}$$
$$= \sum_{j,k=1}^{p}  \sum_{h=1}^{p}  r_{jh}\overline{r}_{kh}b_{jk}u_{j}\overline{u}_{k}$$
$$= \sum_{h=1}^{p}  \sum_{j,k=1}^{p}  b_{jk}u_{j}r_{jh}\overline{u}_{k}\overline{r}_{kh}.$$
Vì $B$ là nửa xác định dương (positive semidefinite), với mỗi cố định $h$, ta có
$$\sum_{j,k=1}^{p}  b_{jk}u_{j}r_{jh}\overline{u}_{k}\overline{r}_{kh} = \sum_{j,k=1}^{p}  b_{jk}z_{j}\overline{z}_{k} \ge 0,$$
Như ta xem bởi đặt $z = (u_{1}r_{1h}, \dots  , u_{p}r_{ph})$, Ngược lại, thông thường tích $AB$ của hai đối xứng nửa xác định dương (positive semidefinite) các ma trận $A$ và $B$ có thể không là đối xứng nửa xác định dương (positive semidefinite); xem Mục 8.9 cho ví dụ. Ở đây là khác các cách của thu được mới các nhân xác định dương từ old các một.

> **Mệnh đề 53.6.** Cho $\kappa_{1}$: $X \times X \to \mathbb{C}$ và $\kappa_{2}$: $X \times X \to \mathbb{C}$ là hai các nhân xác định dương,
$$\mathbb{C}\mathbb{R}^{N}  \mathbb{R}^{N} \mathbb{R}^{N} \mathbb{C}$$
$f$: $X \to$ là hàm, $\psi$: $X \to$ là hàm, $\kappa_{3}$: $\times \to$ là nhân xác định dương (positive definite kernel), và $a \in \mathbb{R}$ là bất kỳ dương thực số. Thì sau đây các hàm là các nhân xác định dương:

<!-- PAGE 1956 -->
$(1) \kappa (x, y) = \kappa_{1} (x, y) + \kappa_{2} (x, y)$.
$(2) \kappa (x, y) = a\kappa_{1} (x, y)$.
$(3) \kappa (x, y) = f(x)\overline{f}\overline{(}\overline{y}\overline{)}$.
$(4) \kappa (x, y) = \kappa_{3} (\psi (x), \psi (y))$.
$(5)$ Nếu $B$ là đối xứng nửa xác định dương (positive semidefinite) $n \times  n$ ma trận, thì ánh xạ
$$\mathbb{R}^{n} \mathbb{R}^{n} \mathbb{R}$$
$\kappa$: $\times \to$ cho trước bởi
$$\kappa (x, y) = x^{\top}By$$
Là nhân xác định dương (positive definite kernel).

*Chứng minh.* $(1)$ Với mọi hữu hạn tập con $S = {x_{1}, \dots  , x_{p}}$ của $X$, nếu $K_{1}$ là ma trận cỡ $p \times  p$
$$K_{1} = (\kappa_{1} (x_{k}, x_{j}))_{1\le j,k\le p}$$
Và nếu nếu $K_{2}$ là ma trận cỡ $p \times  p$
$$K_{2} = (\kappa_{2} (x_{k}, x_{j}))_{1\le j,k\le p},$$
Thì với mọi $u \in \mathbb{C}^{p}$, ta có
$$u^{*}(K_{1} + K_{2})u = u^{*}K_{1}u + u^{*}K_{2}u \ge 0,$$
Vì $u^{*}K_{1}u \ge 0$ và $u^{*}K_{2}u \ge 0$ bởi vì $\kappa_{2}$ và $\kappa_{2}$ là các nhân xác định dương, mà có nghĩa là $K_{1}$ và $K_{2}$ là nửa xác định dương (positive semidefinite).
$(2)$ Ta có
$$u^{*}(aK_{1})u = au^{*}K_{1}u \ge 0,$$
Vì $> 0$ và $u^{*}K_{1}u \ge 0$.
$(3)$ Với mọi hữu hạn tập con $S = {x_{1}, \dots  , x_{p}}$ của $X$, nếu $K$ là ma trận cỡ $p \times  p$
$$K = (\kappa (x_{k}, x_{j}))_{1\le j,k\le p} = (\overline{f}\overline{(}\overline{x}_{k}\overline{)} f(x_{j}))_{1\le j,k\le p}$$
Thì ta có
$$2$$
$$u^{*}Ku = u^{\top}K^{\top}\overline{u} = \sum_{j,k=1}^{p}  \kappa (x_{j}, x_{k})u_{j}\overline{u}_{k} = \sum_{j,k=1}^{p}  u_{j}f(x_{j})\overline{u}_{k}\overline{f}\overline{(}\overline{x}_{k}\overline{) =} \sum_{j=1}^{p}  u_{j}f(x_{j})\ge 0.$$
$(4)$ Với mọi hữu hạn tập con $S = {x_{1}, \dots  , x_{p}}$ của $X$, ma trận cỡ $p \times  p$ $K$ cho trước bởi
$$K = (\kappa (x_{k}, x_{j}))_{1\le j,k\le p} = (\kappa_{3} (\psi (x_{k}), \psi (x_{j})))_{1\le j,k\le p}$$
Là đối xứng nửa xác định dương (positive semidefinite) vì $\kappa_{3}$ là nhân xác định dương (positive definite kernel).

<!-- PAGE 1957 -->
$(5)$ Như trong chứng minh của Mệnh đề 53.5 (được điều chỉnh đến thực trường hợp) có một ma trận $R$ sao cho
$$B = RR^{\top},$$
Do đó
$$\kappa (x, y) = x^{\top}By = x^{\top}RR^{\top}y = (R^{\top}x)^{\top}R^{\top}y = \langle R^{\top}x, R^{\top}y\rangle ,$$
$$\mathbb{R}^{n}$$
Do đó $\kappa$ là hạt nhân (kernel) hàm cho trước bởi đặc trưng (feature) ánh xạ $\phi (x) = R^{\top}x$ từ đến chính nó, và theo Mệnh đề 53.1, nó là đối xứng xác định dương (SPD) hạt nhân (kernel).

> **Mệnh đề 53.7.** Cho $\kappa_{1}$: $X \times  X \to \mathbb{C}$ là nhân xác định dương (positive definite kernel), và cho p(z) là đa thức với không âm các hệ số. Thì sau đây các hàm $\kappa$ được định nghĩa ở dưới là cũng các nhân xác định dương.
$(1) \kappa (x, y) = p(\kappa_{1} (x, y))$.
$(2) \kappa (x, y) = e^{\kappa1(x,y)}$.
$(3)$ Nếu $X$ là thực Không gian Hilbert (Hilbert space) với tích vô hướng (inner product) $\langle$ -, $-\rangle_{X}$ và tương ứng chuẩn (norm) $\|\|_{X}$,
$$\kappa (x, y) =\overline{e}_{2\sigma}^{-\|x-y2\|2X}$$
Với mọi $\sigma  > 0$.

*Chứng minh.* $(1)$ Nếu p(z) $= a_{m}z^{m} + \cdots  + a_{1}z + a_{0}$, thì
$$p(\kappa_{1} (x, y)) = a_{m}\kappa_{1} (x, y)^{m}+ \cdots  + a_{1}\kappa_{1} (x, y) + a_{0}.$$
Vì $a_{k} \ge 0$ cho $k = 0, \dots  , m$, theo Mệnh đề 53.5 và Mệnh đề 53.6(2), mỗi hàm $a_{k}\kappa_{i} (x, y)^{k}$ với $1 \le k \le m$ là nhân xác định dương (positive definite kernel), theo Mệnh đề 53.6(3) với
$$\sqrt$$
F(x) $= \overline{a}_{0}$, hằng số hàm $a_{0}$ là nhân xác định dương (positive definite kernel), và theo Mệnh đề 53.6(1), $p(\kappa_{1} (x, y))$ là nhân xác định dương (positive definite kernel).
$(2)$ Ta có
$$e^{\kappa1(x,y)} = \sum_{k=0}^{\infty}  \frac{\kappa_{1} (x, y)^{k}}{k!} .$$
Bởi $(1)$, riêng các tổng
$$\sum_{k=0}^{m}  \frac{\kappa_{1} (x, y)^{k}}{k!}$$
Là các nhân xác định dương, và vì $e^{\kappa1(x,y)}$ là (uniform) từng điểm giới hạn của các nhân xác định dương, nó là cũng nhân xác định dương (positive definite kernel).
$(3)$ Theo Mệnh đề 53.6(2), vì ánh xạ $(x, y) \mapsto \langle x, y\rangle_{X}$ là hiển nhiên nhân xác định dương (positive definite kernel) (đặc trưng (feature) ánh xạ là đồng nhất thức) và vì $\sigma  \neq  0$, hàm $(x, y) \mapsto \langle x, y\rangle_{X} /\sigma^{2}$ là nhân xác định dương (positive definite kernel) (theo Mệnh đề 53.6(2)), do đó bởi $(2)$,
$$\kappa_{1} (x, y) =\overline{e}_{\sigma}^{\langle x,y2\rangle X}$$
