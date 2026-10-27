# Courant–Fischer Định lý; Perturbation Các kết quả


<!-- PAGE 650 -->

## 17.7 Courant–Fischer Định lý; Perturbation Re-

$$sults$$
Một cái khác hữu ích công cụ để chứng minh trị riêng (eigenvalue) các đẳng thức là Courant–Fischer đặc trưng của các trị riêng (eigenvalues) của ma trận đối xứng (symmetric matrix), cũng đã biết như Min-max (và Max-min) định lý.

> **Định lý 17.27.** (Courant–Fischer) Cho $A$ là đối xứng $n \times  n$ ma trận với các trị riêng (eigenvalues)
$$\mathbb{R}^{n}$$
$\lambda_{1}  \le \lambda_{2}  \le \cdots  \le \lambda_{n}$. Nếu $\mathcal{V}_{k}$ ký hiệu tập hợp của các không gian con của có số chiều $k$, thì
$$\lambda_{k}  =W\in Vmaxx\in minW,x\neq 0 \frac{x^{\top}Ax}{x^{\top}x}$$
$$n-k+1$$
$$\lambda_{k}  = Wmin\in Vx\in maxW,x\neq 0 \frac{x^{\top}Ax}{x^{\top}x} .$$
$$k$$

*Chứng minh.* Cho chúng ta xét thứ hai đẳng thức, chứng minh của thứ nhất đẳng thức đang là đồng dạng. Cho $(u_{1}, \dots  , u_{n})$ là bất kỳ cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors) của $A$, ở đâu $u_{i}$ là unit vectơ riêng (eigenvector) liên kết với $\lambda_{i}$. Nhận thấy rằng không gian $V_{k}$ được sinh (spanned) bởi $(u_{1}, \dots  , u_{k})$ có số chiều $k$, và theo Mệnh đề 17.23, ta có
$$\lambda_{k}  =x\neq 0max,x\in V \frac{x^{\top}Ax}{x^{\top}x} \ge Winf\in Vx\in maxW,x\neq 0 \frac{x^{\top}Ax}{x^{\top}x} .$$
$$kk$$
Vì vậy, ta cần để chứng minh reverse inequality; nghĩa là, ta có để chỉ ra rằng
$$\lambda_{k}  \le x\neq 0max,x\in W \frac{x^{\top}Ax}{x^{\top}x} ,for allW \in V_{k}.$$
Bây giờ với mọi $W \in V_{k}$, nếu ta có thể chứng minh rằng $W \cap V_{k-1}^{\perp}  = (0)$, thì với mọi khác không $v \in W \cap V_{k-1}^{\perp}$,
$$̸$$
Theo Mệnh đề 17.24, ta có
$$\lambda_{k}  =x\neq 0min,x\in V\perp \frac{x^{\top}Ax}{x^{\top}x} \le \frac{v^{\top}Av}{v^{\top}v} \le x\in maxW,x\neq 0 \frac{x^{\top}Ax}{x^{\top}x} .$$
$$k -1$$
Nó vẫn còn để chứng minh rằng dim(W $\cap V_{k}^{\perp}$) $\ge 1$. Tuy nhiên, $dim(V_{k-1}) = k$ - $1$, do đó $dim(V_{k-1}^{\perp}$) $= n$ - $k + 1$, và bởi giả thiết $dim(W^{-1}) = k$. Bởi Grassmann quan hệ,
$$\dim(W) + \dim(V_{k-1}^{\perp} ) = \dim(W \cap V_{k-1}^{\perp} ) + \dim(W + V_{k-1}^{\perp} ),$$
Và vì dim(W $+ V_{k-1}^{\perp}$) $\le dim(\mathbb{R}^{n}) = n$, ta thu được
$$k + n -k + 1 \le \dim(W \cap V_{k-1}^{\perp} ) + n;$$
Rằng là, $1 \le$ dim(W $\cap V_{k-1}^{\perp}$), như đã khẳng định. Do đó ta được chứng minh rằng
$$\lambda_{k}  = Winf\in Vx\in maxW,x\neq 0 \frac{x^{\top}Ax}{x^{\top}x} ,$$
$$k$$
Nhưng vì inf là đạt được cho không gian con $V_{k}$, phương trình cũng nghiệm đúng với inf được thay thế bởi min.

<!-- PAGE 651 -->
Courant–Fischer định lý cho ta sau đây hữu ích kết quả về perturbing các trị riêng (eigenvalues) của ma trận đối xứng (symmetric matrix) do Hermann Weyl.

> **Mệnh đề 17.28.** Cho trước hai $n\times n$ các ma trận đối xứng $A$ và $B = A+\Delta A$, nếu $\alpha_{1}  \le \alpha_{2}  \le \cdots  \le \alpha_{n}$ là các trị riêng (eigenvalues) của $A$ và $\beta_{1}  \le \beta_{2}  \le \cdots  \le \beta_{n}$ là các trị riêng (eigenvalues) của $B$, thì
$$|\alpha_{k}  -\beta_{k} | \le \rho (\Delta A) \le \|\Delta A\|_{2} ,k = 1, \dots  , n.$$

*Chứng minh.* Cho $\mathcal{V}_{k}$ được định nghĩa như trong Courant–Fischer định lý và cho $V_{k}$ là không gian con được sinh (spanned) bởi $k$ các vectơ riêng (eigenvectors) liên kết với $\alpha_{1} , \dots  , \alpha_{k}$. Bởi Courant–Fischer định lý ứng dụng đến $B$, ta có
$$\beta_{k}  = Wmin\in Vx\in maxW,x\neq 0 \frac{x^{\top}Bx}{x^{\top}x}$$
$$k$$
$$\le maxx\in V \frac{x^{\top}Bx}{x^{\top}x}$$
$$k$$
$$= maxx\in V \begin{pmatrix} x^{\top}Ax & x^{\top}\Delta Ax \\ + \\ x^{\top}x & x^{\top}x \\ x^{\top}Ax & x^{\top}\Delta \end{pmatrix}$$
$$k$$
$$\le maxx\in Vx^{\top}x + maxx\in V \frac{A x}{x^{\top}x} .$$
$$kk$$
Theo Mệnh đề 17.23, ta có
$$\alpha_{k}  = maxx\in V \frac{x^{\top}Ax}{x^{\top}x} ,$$
$$k$$
Do đó ta thu được
$$\beta_{k}  \le maxx\in V \frac{x^{\top}Ax}{x^{\top}x} + maxx\in V \frac{x^{\top}\Delta A x}{x^{\top}x}$$
$$kk$$
$$= \alpha_{k}  + maxx\in V \frac{x^{\top}\Delta A x}{x^{\top}x}$$
$$k$$
$$\le \alpha_{k}  + maxx\in \mathbb{R} n \frac{x^{\top}\Delta A x}{x^{\top}x} .$$
Bây giờ theo Mệnh đề 17.23 và Mệnh đề 9.10, ta có
$$maxx\in \mathbb{R} n \frac{x^{\top}\Delta A x}{x^{\top}x} = maxi\lambda_{i} (\Delta A) \le \rho (\Delta A) \le \|\Delta A\|_{2} ,$$
Ở đâu $\lambda_{i} (\Delta A)$ ký hiệu thứ $i$ trị riêng (eigenvalue) của $\Delta A$, mà suy ra rằng
$$\beta_{k}  \le \alpha_{k}  + \rho (\Delta A) \le \alpha_{k}  + \|\Delta A\|_{2} .$$
Bởi exchanging các vai trò của $A$ và $B$, ta cũng có
$$\alpha_{k}  \le \beta_{k}  + \rho (\Delta A) \le \beta_{k}  + \|\Delta A\|_{2} ,$$
Và do đó,
$$|\alpha_{k}  -\beta_{k} | \le \rho (\Delta A) \le \|\Delta A\|_{2} ,k = 1, \dots  , n,$$
Như đã khẳng định.

<!-- PAGE 652 -->
Mệnh đề 17.28 cũng nghiệm đúng cho Các ma trận Hermite. pretty kết quả của Wielandt và Hoffman khẳng định rằng
$$\sum_{k=1}^{n}  (\alpha_{k}  -\beta_{k} )^{2}\le \|\Delta A\|_{F}^{2} ,$$
Ở đâu $\|\|_{F}$ là Chuẩn Frobenius (Frobenius norm). Tuy nhiên, chứng minh là một cách đáng kể khó hơn hơn ở trên chứng minh; xem Lax $[117]$. Courant–Fischer định lý có thể cũng được sử dụng để chứng minh một số nổi tiếng các bất đẳng thức do Hermann Weyl. Các phần tử này có thể cũng được quan điểm như perturbation các kết quả. Cho trước hai đối xứng (hoặc Hermite) các ma trận $A$ và $B$, cho $\lambda_{i} (A), \lambda_{i} (B)$, và $\lambda_{i} (A + B)$ ký hiệu thứ $i$ trị riêng (eigenvalue) của $A, B$, và $A + B$, respectively, arranged trong nondecreasing thứ tự.

> **Mệnh đề 17.29.** (Weyl) Cho trước hai đối xứng (hoặc Hermite) $n \times  n$ các ma trận $A$ và $B$, sau đây các bất đẳng thức đúng: Với mọi $i, j, k$ với $1 \le i, j, k \le n: 1$. Nếu $i + j = k + 1$, thì
$$\lambda_{i} (A) + \lambda_{j} (B) \le \lambda_{k} (A + B).$$
$2$. Nếu $i + j = k + n$, thì
$$\lambda_{k} (A + B) \le \lambda_{i} (A) + \lambda_{j} (B).$$

*Chứng minh.* Nhận thấy rằng thứ nhất tập hợp của các bất đẳng thức là thu được từ thứ hai tập hợp bằng cách thay thế $A$ bởi $-A$ và $B$ bởi $-B$, do đó nó là đủ để chứng minh thứ hai tập hợp của các bất đẳng thức. Bởi Courant–Fischer định lý, có một không gian con $H$ có số chiều $n$ - $k + 1$ sao cho
$$\lambda_{k} (A + B) =x\in minH,x\neq 0 \frac{x^{\top}(A + B)x}{x^{\top}x} .$$
Tương tự, tồn tại một không gian con $F$ có số chiều $i$ và không gian con $G$ có số chiều $j$ sao cho
$$\lambda_{i} (A) = x\in maxF,x\neq 0 \frac{x^{\top}Ax}{x^{\top}x} ,\lambda_{j} (B) =x\in maxG,x\neq 0 \frac{x^{\top}Bx}{x^{\top}x} .$$
Ta khẳng định rằng $F \cap G \cap H \neq  (0)$. để chứng minh điều này, ta sử dụng Grassmann quan hệ hai lần. Thứ nhất, dim(F $\cap G \cap H) =$ dim(F) $+$ dim(G $\cap H)$ -dim(F $+ (G \cap H)) \ge$ dim(F) $+$ dim(G $\cap H) -n$, và thứ hai,
$$\dim(G \cap H) = \dim(G) + \dim(H) -\dim(G + H) \ge \dim(G) + \dim(H) -n,$$
Do đó
$$\dim(F \cap G \cap H) \ge \dim(F) + \dim(G) + \dim(H) -2n.$$
