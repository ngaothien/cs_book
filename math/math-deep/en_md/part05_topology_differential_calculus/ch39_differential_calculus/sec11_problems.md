# Problems


<!-- PAGE 1489 -->
$\bullet$  Second-order and higher-order derivatives. $\bullet$  Schwarz’s lemma. $\bullet$  Hessian matrix. $\bullet  C^{\infty}-functions$, smooth functions. $\bullet$  Taylor–Young’s formula. $\bullet$  Generalized mean value theorem. $\bullet$  Taylor–MacLaurin’s formula. $\bullet$  Taylor’s formula with integral remainder. $\bullet$  Fa`a di Bruno’s formula.

## 39.11 Problems

Problem 39.1. Let $f$ : $M_{n}(\mathbb{R}) \to M_{n}(\mathbb{R})$ be the function defined on $n \times  n$ matrices by
$$f(A) = A^{2}.$$
Prove that
$$Df_{A}(H) = AH + HA,$$
for all $A, H \in M_{n}(\mathbb{R})$.
Problem 39.2. Let $f$ : $M_{n}(\mathbb{R}) \to M_{n}(\mathbb{R})$ be the function defined on $n \times  n$ matrices by
$$f(A) = A^{3}.$$
Prove that
$$Df_{A}(H) = A^{2}H + AHA + HA^{2},$$
for all $A, H \in M_{n}(\mathbb{R})$.
Problem 39.3. If $f$ : $M_{n}(\mathbb{R}) \to M_{n}(\mathbb{R})$ and $g: M_{n}(\mathbb{R}) \to M_{n}(\mathbb{R})$ are differentiable matrix functions, prove that
$$d(fg)_{A}(B) = df_{A}(B)g(A) + f(A)dg_{A}(B),$$
for all $A, B \in M_{n}(\mathbb{R})$.

<!-- PAGE 1490 -->
Problem 39.4. Recall that $\mathfrak{so}(3)$ denotes the vector space of real skew-symmetric $n \times  n$ matrices $(B^{\top} = -B)$. Let $C$ : $\mathfrak{so}(n) \to M_{n}(\mathbb{R})$ be the function given by
$$C(B) = (I -B)(I + B)^{-1}.$$
$(1)$ Prove that if $B$ is skew-symmetric, then I - $B$ and I $+ B$ are invertible, and so $C$ is well-defined. Prove that
$(2)$ Prove that
$$dC(B)(A) = -[I + (I -B)(I + B)^{-1}]A(I + B)^{-1}= -2(I + B)^{-1}A(I + B)^{-1}.$$
$(3)$ Prove that dC(B) is injective for every skew-symmetric matrix $B$.
Problem 39.5. Prove that $d^{m}C_{B}(H_{1}, \dots  , H$ )
$$= 2(-1)^{m} \sum_{\pi\in Sm}^{m}  (I + B)^{-1}H_{\pi(1)}(I + B)^{-1}H_{\pi(2)}(I + B)^{-1}\cdots  (I + B)^{-1}H_{\pi(m)}(I + B)^{-1}.$$
Problem 39.6. Consider the function $g$ defined for all $A \in GL(n,\mathbb{R})$, that is, all $n \times  n$ real invertible matrices, given by
$$g(A) = \det(A).$$
$(1)$ Prove that
$$dg_{A}(X) = \det(A)\mathrm{tr}(A^{-1}X),$$
for all $n \times  n$ real matrices $X$.
$(2)$ Consider the function $f$ defined for all $A \in GL^{+}(n,\mathbb{R})$, that is, $n \times  n$ real invertible matrices of positive determinants, given by
$$f(A) = \log g(A) = \log \det(A).$$
Prove that
$$df_{A}(X) = \mathrm{tr}(A^{-1}X)$$
$$D^{2}f(A)(X_{1}, X_{2}) = -\mathrm{tr}(A^{-1}X_{1}A^{-1}X_{2}),$$
for all $n \times  n$ real matrices $X, X_{1}, X_{2}$.
$(3)$ Prove that
$$D^{m}f(A)(X_{1}, \dots  , X_{m}) = (-1)^{m-1} \sum_{\in Sm-}  \mathrm{tr}(A^{-1}X_{1}A^{-1}X_{\sigma(1)+1}A^{-1}X_{\sigma(2)+1} \cdots  A^{-1}X_{\sigma(m-1)+1})$$
$$\sigma 1$$
for any $m \ge 1$, where $X_{1}, \dots  X_{m}$ are any $n \times  n$ real matrices.
