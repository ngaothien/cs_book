# Các bài tập


<!-- PAGE 1489 -->
$\bullet$ Bậc hai và bậc cao các đạo hàm. $\bullet$ Schwarz’s bổ đề. $\bullet$ Ma trận Hesse (Hessian matrix). $\bullet  C^{\infty}-functions$, trơn (smooth) các hàm. $\bullet$ Taylor–Young’s công thức. $\bullet$ Suy rộng/tổng quát hóa có nghĩa giá trị định lý. $\bullet$ Taylor–MacLaurin’s công thức. $\bullet$ Taylor’s công thức với tích phân phần dư. $\bullet$ Fa` di Bruno’s công thức.

## 39.11 Các bài tập

Bài toán 39.1. Cho $f$: $M_{n}(\mathbb{R}) \to M_{n}(\mathbb{R})$ là hàm được định nghĩa trên $n \times  n$ các ma trận bởi
$$f(A) = A^{2}.$$
Chứng minh rằng
$$Df_{A}(H) = AH + HA,$$
Với mọi $A, H \in M_{n}(\mathbb{R})$.
Bài toán 39.2. Cho $f$: $M_{n}(\mathbb{R}) \to M_{n}(\mathbb{R})$ là hàm được định nghĩa trên $n \times  n$ các ma trận bởi
$$f(A) = A^{3}.$$
Chứng minh rằng
$$Df_{A}(H) = A^{2}H + AHA + HA^{2},$$
Với mọi $A, H \in M_{n}(\mathbb{R})$.
Bài toán 39.3. Nếu $f$: $M_{n}(\mathbb{R}) \to M_{n}(\mathbb{R})$ và $g: M_{n}(\mathbb{R}) \to M_{n}(\mathbb{R})$ là khả vi (differentiable) ma trận các hàm, chứng minh rằng
$$d(fg)_{A}(B) = df_{A}(B)g(A) + f(A)dg_{A}(B),$$
Với mọi $A, B \in M_{n}(\mathbb{R})$.

<!-- PAGE 1490 -->
Bài toán 39.4. Nhắc lại rằng $\mathfrak{so}(3)$ ký hiệu không gian vectơ (vector space) của thực phản đối xứng $n \times  n$ các ma trận $(B^{\top} = -B)$. Cho $C$: $\mathfrak{so}(n) \to M_{n}(\mathbb{R})$ là hàm cho trước bởi
$$C(B) = (I -B)(I + B)^{-1}.$$
$(1)$ Chứng minh rằng nếu $B$ là phản đối xứng, thì I - $B$ và I $+ B$ là khả nghịch, và do đó $C$ là xác định tốt (well-defined). Chứng minh rằng
$(2)$ Chứng minh rằng
$$dC(B)(A) = -[I + (I -B)(I + B)^{-1}]A(I + B)^{-1}= -2(I + B)^{-1}A(I + B)^{-1}.$$
$(3)$ Chứng minh rằng dC(B) là đơn ánh (injective) với mọi ma trận phản đối xứng (skew-symmetric matrix) $B$.
Bài toán 39.5. Chứng minh rằng $d^{m}C_{B}(H_{1}, \dots  , H$)
$$= 2(-1)^{m} \sum_{\pi\in Sm}^{m}  (I + B)^{-1}H_{\pi(1)}(I + B)^{-1}H_{\pi(2)}(I + B)^{-1}\cdots  (I + B)^{-1}H_{\pi(m)}(I + B)^{-1}.$$
Bài toán 39.6. Xét hàm $g$ được định nghĩa với mọi $A \in GL(n,\mathbb{R})$, nghĩa là, tất cả $n \times  n$ thực các ma trận khả nghịch, cho trước bởi
$$g(A) = \det(A).$$
$(1)$ Chứng minh rằng
$$dg_{A}(X) = \det(A)\mathrm{tr}(A^{-1}X),$$
Với mọi $n \times  n$ thực các ma trận $X$.
$(2)$ Xét hàm $f$ được định nghĩa với mọi $A \in GL^{+}(n,\mathbb{R})$, nghĩa là, $n \times  n$ thực các ma trận khả nghịch của dương các định thức, cho trước bởi
$$f(A) = \log g(A) = \log \det(A).$$
Chứng minh rằng
$$df_{A}(X) = \mathrm{tr}(A^{-1}X)$$
$$D^{2}f(A)(X_{1}, X_{2}) = -\mathrm{tr}(A^{-1}X_{1}A^{-1}X_{2}),$$
Với mọi $n \times  n$ thực các ma trận $X, X_{1}, X_{2}$.
$(3)$ Chứng minh rằng
$$D^{m}f(A)(X_{1}, \dots  , X_{m}) = (-1)^{m-1} \sum_{\in Sm-}  \mathrm{tr}(A^{-1}X_{1}A^{-1}X_{\sigma(1)+1}A^{-1}X_{\sigma(2)+1} \cdots  A^{-1}X_{\sigma(m-1)+1})$$
$$\sigma 1$$
Với mọi $m \ge 1$, ở đâu $X_{1}, \dots  X_{m}$ là bất kỳ $n \times  n$ thực các ma trận.
