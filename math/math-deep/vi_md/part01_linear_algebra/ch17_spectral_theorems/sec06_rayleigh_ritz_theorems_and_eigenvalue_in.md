# Rayleigh–Ritz Các định lý và Trị riêng (eigenvalue) Interlacing


<!-- PAGE 645 -->
Nhắc lại từ Mệnh đề 14.15 rằng khi $E$ là Không gian Hermite (Hermitian space) và $(e_{1}, \dots , e_{n})$ là cơ sở trực chuẩn (orthonormal basis) cho $E$, nếu $A$ là ma trận của ánh xạ tuyến tính (linear map) $f$: $E \to E$ w.r.t. cơ sở (basis) $(e_{1}, \dots  , e_{n})$, thì $A^{*}$ là ma trận của liên hợp (adjoint) $f^{*}$ của $f$. Hệ quả là, chuẩn tắc/bình thường ánh xạ tuyến tính (linear map) có ma trận chuẩn tắc (normal matrix), tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map) có Ma trận Hermite (Hermitian matrix), phản tự liên hợp (skew-self-adjoint) ánh xạ tuyến tính (linear map) có ma trận phản Hermite (skew-Hermitian matrix), và unita ánh xạ tuyến tính (linear map) có ma trận unita (unitary matrix). Hơn nữa, nếu $(u_{1}, \dots  , u_{n})$ là một cái khác cơ sở trực chuẩn (orthonormal basis) cho $E$ và $P$ là ma trận chuyển cơ sở (change of basis matrix) có các cột là các thành phần của $u_{i}$ w.r.t. cơ sở (basis) $(e_{1}, \dots  , e_{n})$, thì $P$ là unita, và với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$, nếu $A$ là ma trận của $f$ w.r.t $(e_{1}, \dots  , e_{n})$ và $B$ là ma trận của $f$ w.r.t. $(u_{1}, \dots  , u_{n})$, thì
$$B = P^{*} AP.$$
Định lý 17.13 và Mệnh đề 17.7 có thể được restated theo các ma trận như sau.

> **Định lý 17.22.** Với mọi phức ma trận chuẩn tắc (normal matrix) $A$ có một ma trận unita (unitary matrix) $U$ và ma trận đường chéo (diagonal matrix) $D$ sao cho $A = UDU^{*}$. Hơn nữa, nếu $A$ là Hermite, thì $D$ là thực ma trận; nếu $A$ là skew-Hermitian, thì các phần tử (entries) trong $D$ là thuần túy imaginary hoặc không; và nếu $A$ là unita, thì các phần tử (entries) trong $D$ có tuyệt đối giá trị $1$.

## 17.6 Rayleigh–Ritz Các định lý và Trị riêng (eigenvalue) Interlac-

$$ing$$
Sự kiện rằng được sử dụng frequently trong tối ưu hóa các bài tập là rằng các trị riêng (eigenvalues) của ma trận đối xứng (symmetric matrix) được đặc trưng hóa theo những gì là đã biết như Rayleigh tỉ số, được định nghĩa bởi
$$R(A)(x) = \frac{x^{\top}Ax}{x^{\top}x} ,x \in \mathbb{R}^{n}, x \neq  0.$$
Sau đây mệnh đề là thường được sử dụng để chứng minh tính đúng đắn của khác nhau tối ưu hóa hoặc xấp xỉ các bài tập (ví dụ PCA; xem Mục 23.4). Nó cũng được sử dụng để chứng minh Mệnh đề 17.25, mà được sử dụng đến justify tính đúng đắn của phương pháp cho graph-drawing (xem Chương $21)$.

> **Mệnh đề 17.23.** (Rayleigh–Ritz) Nếu $A$ là đối xứng $n \times  n$ ma trận với các trị riêng (eigenvalues) $\lambda_{1}  \le \lambda_{2}  \le \cdots  \le \lambda_{n}$ và nếu $(u_{1}, \dots  , u_{n})$ là bất kỳ cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors) của $A$, ở đâu $u_{i}$ là unit vectơ riêng (eigenvector) liên kết với $\lambda_{i}$, thì
$$maxx\neq 0 \frac{x^{\top}Ax}{x^{\top}x} = \lambda_{n}$$
(với cực đại đạt được cho $x = u_{n})$, và
$$x\neq 0,x\in {umax,...,u}\perp \frac{x^{\top}Ax}{x^{\top}x} = \lambda_{n-k}$$
$$n-k+1n$$

<!-- PAGE 646 -->
(với cực đại đạt được cho $x = u_{n-k})$, ở đâu $1 \le k \le n$ - $1$. Tương đương, nếu $V_{k}$ là không gian con được sinh (spanned) bởi $(u_{1}, \dots  , u_{k})$, thì
$$\lambda_{k}  =x\neq 0max,x\in V \frac{x^{\top}Ax}{x^{\top}x} ,k = 1, \dots  , n.$$
$$k$$

*Chứng minh.* Thứ nhất nhận thấy rằng
$$maxx\neq 0 \frac{x^{\top}Ax}{x^{\top}x} = maxx {x^{\top}Ax | x^{\top}x = 1},$$
Và tương tự,
$$x\neq 0,x\in {umax,...,u}\perp \frac{x^{\top}Ax}{x^{\top}x} = maxxx^{\top}Ax | (x \in {u_{n-k+1}, \dots  , u_{n}}^{\perp}) \wedge (x^{\top}x = 1).$$
$$n-k+1n$$
Vì $A$ là ma trận đối xứng (symmetric matrix), các trị riêng (các trị riêng (eigenvalues)) của nó là thực và nó có thể được được chéo hóa đối với cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors), do đó cho $(u_{1}, \dots  , u_{n})$ là như vậy cơ sở (basis). Nếu ta viết
$$x = \sum_{i=1}^{n}  x_{i}u_{i},$$
Đơn giản phép tính chỉ ra rằng
$$x^{\top}Ax = \sum_{i=1}^{n}  \lambda_{i} x_{i}^{2} .$$
$$If x^{\top}x = 1, then \sum_{i}  n=1 x_{i}^{2} = 1, and since we assumed that \lambda_{1}  \le \lambda_{2}  \le \cdots  \le \lambda_{n} , we get$$
$$x^{\top}Ax = \sum_{i=1}^{n}  \lambda_{i} x_{i}^{2} \le \lambda_{n} \begin{pmatrix} x_{i}^{2} \end{pmatrix} \sum_{i=1}^{n}  = \lambda_{n} .$$
Do đó,
$$\maxx^{\top}Ax | x^{\top}x = 1\le \lambda_{n} ,$$
$$x$$
Và vì điều này cực đại là đạt được cho $e_{n} = (0, 0, \dots  , 1)$, ta kết luận rằng
$$\maxx^{\top}Ax | x^{\top}x = 1= \lambda_{n} .$$
$$x$$
Tiếp theo nhận thấy rằng $x \in {u_{n-k+1}, \dots  , u_{n}}^{\perp}$ và $x^{\top}x = 1$ khi và chỉ khi $x_{n-k+1} = \cdots  = x_{n} = 0$ và
$$\sum_{i}  n=1-k x_{i}^{2} = 1. Consequently, for such an x, we have$$
$$x^{\top}Ax = \sum_{i=1}^{n-k}  \lambda_{i} x_{i}^{2} \le \lambda_{n-k} \begin{pmatrix} x_{i}^{2} \end{pmatrix} \sum_{i=1}^{n-k}  = \lambda_{n-k} .$$

<!-- PAGE 647 -->
Do đó,
$$\maxx^{\top}Ax | (x \in {u_{n-k+1}, \dots  , u_{n}}^{\perp}) \wedge (x^{\top}x = 1)\le \lambda_{n-k} ,$$
$$x$$
Và vì điều này cực đại là đạt được cho $e_{n-k} = (0, \dots  , 0, 1, 0, \dots  , 0)$ với $1$ trong position $n$ - $k$, ta kết luận rằng
$$\maxx^{\top}Ax | (x \in {u_{n-k+1}, \dots  , u_{n}}^{\perp}) \wedge (x^{\top}x = 1)= \lambda_{n-k} ,$$
$$x$$
Như đã khẳng định. Cho của ta các mục đích ta cần phiên bản của Mệnh đề 17.23 áp dụng đến min thay vì của max, có chứng minh là thu được bởi tầm thường modification của chứng minh của Mệnh đề 17.23.

> **Mệnh đề 17.24.** (Rayleigh–Ritz) Nếu $A$ là đối xứng $n \times  n$ ma trận với các trị riêng (eigenvalues) $\lambda_{1}  \le \lambda_{2}  \le \cdots  \le \lambda_{n}$ và nếu $(u_{1}, \dots  , u_{n})$ là bất kỳ cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors) của $A$, ở đâu $u_{i}$ là unit vectơ riêng (eigenvector) liên kết với $\lambda_{i}$, thì
$$minx\neq 0 \frac{x^{\top}Ax}{x^{\top}x} = \lambda_{1}$$
(với cực tiểu đạt được cho $x = u_{1})$, và
$$x\neq 0,x\in {minu,...,u}\perp \frac{x^{\top}Ax}{x^{\top}x} = \lambda_{i}$$
$$1i-1$$
(với cực tiểu đạt được cho $x = u_{i})$, ở đâu $2 \le i \le n$. Tương đương, nếu $W_{k} = V_{k-1}^{\perp}$ ký hiệu không gian con được sinh (spanned) bởi $(u_{k}, \dots  , u_{n})$ (với $V_{0} = (0))$, thì
$$\lambda_{k}  =x\neq 0min,x\in W \frac{x^{\top}Ax}{x^{\top}x} =x\neq 0min,x\in V\perp \frac{x^{\top}Ax}{x^{\top}x} ,k = 1, \dots  , n.$$
$$kk -1$$
Các mệnh đề 17.23 và 17.24 cùng nhau là đã biết như Rayleigh–Ritz định lý. Nhận thấy rằng Mệnh đề 17.24 ngay lập tức suy ra rằng nếu $A$ là ma trận đối xứng (symmetric matrix), thì $A$ là xác định dương (positive definite) khi và chỉ khi tất cả các trị riêng (các trị riêng (eigenvalues)) của nó là dương. Ta cũng chứng minh sự kiện này trong Mục 22.1; xem Mệnh đề 22.3. Như ứng dụng của Các mệnh đề 17.23 và 17.24, ta chứng minh mệnh đề mà cho phép chúng ta đến compare các trị riêng (eigenvalues) của hai các ma trận đối xứng $A$ và $B = R^{\top}AR$, ở đâu $R$ là rectangular ma trận thỏa mãn phương trình $R^{\top}R =$ I. Thứ nhất ta cần định nghĩa.

> **Định nghĩa 17.5.** Cho trước $n \times  n$ ma trận đối xứng (symmetric matrix) $A$ và $m \times  m$ đối xứng $B$, với $m \le n$, nếu $\lambda_{1}  \le \lambda_{2}  \le \cdots  \le \lambda_{n}$ là các trị riêng (eigenvalues) của $A$ và $\mu_{1}  \le \mu_{2}  \le \cdots  \le \mu_{m}$ là các trị riêng (eigenvalues) của $B$, thì ta nói rằng các trị riêng (eigenvalues) của $B$ interlace các trị riêng (eigenvalues) của $A$ nếu
$$\lambda_{i}  \le \mu_{i}  \le \lambda_{n-m+i} ,i = 1, \dots  , m.$$

<!-- PAGE 648 -->
Ví dụ, nếu $n = 5$ và $m = 3$, ta có
$$\lambda_{1}  \le \mu_{1}  \le \lambda_{3}$$
$$\lambda_{2}  \le \mu_{2}  \le \lambda_{4}$$
$$\lambda_{3}  \le \mu_{3}  \le \lambda_{5} .$$

> **Mệnh đề 17.25.** Cho $A$ là $n \times  n$ ma trận đối xứng (symmetric matrix), $R$ là một ma trận cỡ $n \times  m$ sao cho $R^{\top}R =$ I (với $m \le n)$, và cho $B = R^{\top}AR$ (một ma trận cỡ $m \times  m$). Các tính chất sau đây đúng:
() các trị riêng (eigenvalues) của $B$ interlace các trị riêng (eigenvalues) của $A$.
$(b)$ Nếu $\lambda_{1}  \le \lambda_{2}  \le \cdots  \le \lambda_{n}$ là các trị riêng (eigenvalues) của $A$ và $\mu_{1}  \le \mu_{2}  \le \cdots  \le \mu_{m}$ là các trị riêng (eigenvalues) của $B$, và nếu $\lambda_{i}  = \mu_{i}$, thì có một vectơ riêng (eigenvector) $v$ của $B$ với trị riêng (eigenvalue) $\mu_{i}$ sao cho Rv là vectơ riêng (eigenvector) của $A$ với trị riêng (eigenvalue) $\lambda_{i}$.

*Chứng minh.* () Cho $(u_{1}, \dots  , u_{n})$ là cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors) cho $A$, và cho $(v_{1}, \dots  , v_{m})$ là cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors) cho $B$. Cho $U_{j}$ là không gian con được sinh (spanned) bởi $(u_{1}, \dots  , u_{j})$ và cho $V_{j}$ là không gian con được sinh (spanned) bởi $(v_{1}, \dots  , v_{j})$. Với mọi $i$, không gian con $V_{i}$ có số chiều $i$ và không gian con $R^{\top}U_{i-1}$ có số chiều nhiều nhất $i$ - $1$. Vì vậy, tồn tại một khác không vectơ $v \in V_{i} \cap (R^{\top}U_{i-1})^{\perp}$, và vì
$$v^{\top}R^{\top}u_{j} = (Rv)^{\top}u_{j} = 0,j = 1, \dots  , i -1,$$
Ta có Rv $\in (U_{i-1})^{\perp}$. Theo Mệnh đề 17.24 và bằng cách sử dụng sự kiện rằng $R^{\top}R =$ I, ta có
$$\lambda_{i}  \le \frac{(Rv)^{\top}ARv}{(Rv)^{\top}Rv} = \frac{v^{\top}Bv}{v^{\top}v} .$$
Mặt khác, theo Mệnh đề 17.23,
$$\mu_{i}  =x\neq 0,x\in {maxv,...,v}\perp \frac{x^{\top}Bx}{x^{\top}x} =x\neq 0,xmax\in {v,...,v} \frac{x^{\top}Bx}{x^{\top}x} ,$$
$$i+1n1i$$
Do đó
$$\frac{w^{\top}Bw}{w^{\top}w} \le \mu_{i} for all w \in V_{i},$$
Và vì $v \in V_{i}$, ta có
$$\lambda_{i}  \le \frac{v^{\top}Bv}{v^{\top}v} \le \mu_{i} ,i = 1, \dots  , m.$$
Ta có thể áp dụng cùng lập luận đến các ma trận đối xứng $-A$ và $-B$, để kết luận rằng
$$-\lambda_{n-m+i}  \le -\mu_{i} ,$$

<!-- PAGE 649 -->
Rằng là,
$$\mu_{i}  \le \lambda_{n-m+i} ,i = 1, \dots  , m.$$
Vì vậy,
$$\lambda_{i}  \le \mu_{i}  \le \lambda_{n-m+i} ,i = 1, \dots  , m,$$
Như mong muốn.
$(b)$ Nếu $\lambda_{i}  = \mu_{i}$, thì
$$\lambda_{i}  = \frac{(Rv)^{\top}ARv}{(Rv)^{\top}Rv} = \frac{v^{\top}Bv}{v^{\top}v} = \mu_{i} ,$$
Do đó $v$ phải là vectơ riêng (eigenvector) cho $B$ và Rv phải là vectơ riêng (eigenvector) cho $A$, cả hai cho trị riêng (eigenvalue) $\lambda_{i}  = \mu_{i}$. Mệnh đề 17.25 ngay lập tức suy ra Poincar´e separation định lý. Nó có thể được được sử dụng trong các tình huống, chẳng hạn như trong quantum cơ học, ở đâu một có information về trong các tích $u_{i}^{\top} Au_{j}$.

> **Mệnh đề 17.26.** (Poincar´e separation định lý) Cho $A$ là $n\times n$ đối xứng (hoặc Hermite) ma trận, cho $m$ là một số số nguyên với $1 \le m \le n$, và cho $(u_{1}, \dots  , u_{m})$ là $m$ trực chuẩn các vectơ. Cho $B = (u_{i}^{\top} Au_{j})$ (một ma trận cỡ $m \times  m$), cho $\lambda_{1} (A) \le \dots  \le \lambda_{n} (A)$ là các trị riêng (eigenvalues) của $A$ và $\lambda_{1} (B) \le \dots  \le \lambda_{m} (B)$ là các trị riêng (eigenvalues) của $B$; thì ta có
$$\lambda_{k} (A) \le \lambda_{k} (B) \le \lambda_{k+n-m} (A),k = 1, \dots  , m.$$
Nhận thấy rằng Mệnh đề 17.25 suy ra rằng
$$\lambda_{1}  + \cdots  + \lambda_{m}  \le \mathrm{tr}(R^{\top}AR) \le \lambda_{n-m+1}  + \cdots  + \lambda_{n} .$$
Nếu $P_{1}$ là $n \times  (n$ - $1)$ ma trận thu được từ ma trận đơn vị (identity matrix) bởi dropping của nó cột cuối cùng, ta có $P_{1}^{\top}  P_{1} =$ I, và ma trận $B = P_{1}^{\top} AP_{1}$ là ma trận thu được từ $A$ bởi xóa của nó hàng cuối cùng và của nó cột cuối cùng. Trong trường hợp này interlacing kết quả là
$$\lambda_{1}  \le \mu_{1}  \le \lambda_{2}  \le \mu_{2}  \le \cdots  \le \mu_{n-2}  \le \lambda_{n-1}  \le \mu_{n-1}  \le \lambda_{n} ,$$
Genuine interlacing. Ta thu được đồng dạng các kết quả với ma trận $P_{n-m}$ thu được bởi dropping cuối cùng $n -m$ các cột của ma trận đơn vị (identity matrix) và đặt $B = P_{n-m}^{\top} AP_{n-m} (B$ là ma trận cỡ $m \times  m$ thu được từ $A$ bởi xóa của nó cuối cùng $n$ - $m$ các hàng và các cột). Trong trường hợp này ta có kết quả sau interlacing các bất đẳng thức đã biết như Cauchy interlacing định lý:
$$\lambda_{k}  \le \mu_{k}  \le \lambda_{k+n-m} ,k = 1, \dots  , m.(*)$$
