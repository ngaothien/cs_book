# Problems


<!-- PAGE 799 -->
$\bullet$  Least squares problems. $\bullet$  Existence of a least squares solution of smallest norm (Theorem 23.1). $\bullet$  The pseudo-inverse $A^{+}$ of a matrix $A. \bullet$  The least squares solution of smallest norm is given by the pseudo-inverse (Theorem 23.2) $\bullet$  Projection properties of the pseudo-inverse. $\bullet$  The pseudo-inverse of a normal matrix. $\bullet$  The Penrose characterization of the pseudo-inverse. $\bullet$  Data compression and SVD. $\bullet$  Best approximation of rank $< r$ of a matrix. $\bullet$  Principal component analysis. $\bullet$  Review of basic statistical concepts: mean, variance, covariance, covariance matrix. $\bullet$  Centered data, centroid. $\bullet$  The principal components (PCA). $\bullet$  The Rayleigh–Ritz theorem (Theorem 23.10). $\bullet$  The main theorem: SVD yields PCA (Theorem 23.11). $\bullet$  Best affine approximation. $\bullet$  SVD yields a best affine approximation (Theorem 23.12). $\bullet$  Face recognition, eigenfaces.

## 23.7 Problems

Problem 23.1. Consider the overdetermined system in the single variable $x$:
$$a_{1}x = b_{1}, \dots  , a_{m}x = b_{m},$$
with $a_{1}^{2} + \cdots  + a_{m}^{2}$ ̸ $= 0$. Prove that the least squares solution of smallest norm is given by
$$x^{+} = \frac{a_{1}b_{1} + + a_{m}b_{m}}{a_{1}^{2}+ \cdots  + a_{m}^{2}} \cdots .$$

<!-- PAGE 800 -->
Problem 23.2. Let $X$ be an $m \times  n$ real matrix. For any strictly positive constant $K > 0$, the matrix $X^{\top}X + KI_{n}$ is invertible. Prove that the limit of the matrix $(X^{\top}X + KI_{n})^{-1}X^{\top}$ when $K$ goes to zero is equal to the pseudo-inverse $X^{+}$ of $X$.
Problem 23.3. Use Matlab to find the pseudo-inverse of the $8 \times  6$ matrix
$$A = \begin{pmatrix} 64 & 2 & 3 & 61 & 60 & 6 \\ 9 & 55 & 54 & 12 & 13 & 51 \\ 17 & 47 & 46 & 20 & 21 & 43 \\ 40 & 26 & 27 & 37 & 36 & 30 \\ 32 & 34 & 35 & 29 & 28 & 38 \\ 41 & 23 & 22 & 44 & 45 & 19 \\ 49 & 15 & 14 & 52 & 53 & 11 \\ 8 & 58 & 59 & 5 & 4 & 62 \end{pmatrix} .$$
Observe that the sums of the columns are all equal to $260$. Let $b$ be the vector of dimension $8$ whose coordinates are all equal to $256$. Find the solution $x^{+}$ of the system Ax $= b$.
Problem 23.4. The purpose of this problem is to show that Proposition 23.9 (the Eckart– Young theorem) also holds for the Frobenius norm. This problem is adapted from Strang $[177]$, Section I.9. Suppose the $m\times n$ matrix $B$ of rank at most $k$ minimizes $\|A$ - $B\|_{F}$. Start with an SVD of $B$,
$$B = V \begin{pmatrix} D & 0 \\ 0 & 0 \end{pmatrix} U^{\top} ,$$
where $D$ is a diagonal $k \times  k$ matrix. We can write
$$A = V \begin{pmatrix} L + E + R & F \\ G & H \end{pmatrix} U^{\top} ,$$
where $L$ is strictly lower triangular in the first $k$ rows, $E$ is diagonal, and $R$ is strictly upper triangular, and let
$$C = V \begin{pmatrix} L + D + R & F \\ 0 & 0 \end{pmatrix} U^{\top} ,$$
which clearly has rank $\le k$.
$(1)$ Prove that
$$\|A -B\|_{F}^{2} = \|A -C\|_{F}^{2} + \|L\|_{F}^{2} + \|R\|_{F}^{2} + \|F\|_{F}^{2} .$$
Since $\|A$ - $B\|_{F}$ is minimal, show that $L = R = F = 0$. Similarly, show that $G = 0$.

<!-- PAGE 801 -->
$(2)$ We have
$$V^{\top} AU = \begin{pmatrix} E & 0 \\ 0 & H \end{pmatrix} ,V^{\top} BU = \begin{pmatrix} D & 0 \\ 0 & 0 \end{pmatrix} ,$$
where $E$ is diagonal, so deduce that $1. D = diag(\sigma_{1} , \dots  , \sigma_{k}$ ). $2$. The singular values of $H$ must be the smallest $n$ - $k$ singular values of $A. 3$. The minimum of $\|A$ - $B\|_{F}$ must be $\|H\|_{F} = (\sigma_{k+1}^{2}  + \cdots  + \sigma_{r}^{2} )^{1/2}$.
Problem 23.5. Prove that the closest rank $1$ approximation (in $\|\|_{2})$ of the matrix
$$A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$$
is
$$A_{1} = \frac{3}{2} \begin{pmatrix} 1 & 1 \\ 3 & 3 \end{pmatrix} .$$
Show that the Eckart–Young theorem fails for the operator norm $\|\|_{\infty}$ by finding a rank $1$ matrix $B$ such that $\|A$ - $B\|_{\infty} < \|A$ - $A_{1}\|_{\infty}$.
Problem 23.6. Find a closest rank $1$ approximation (in $\|\|_{2})$ for the matrices
$$A = \begin{pmatrix} 3 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix} ,A = \begin{pmatrix} 0 & 3 \\ 2 & 0 \end{pmatrix} ,A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} .$$
Problem 23.7. Find a closest rank $1$ approximation (in $\|\|_{2})$ for the matrix
$$A = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} .$$
Problem 23.8. Let $S$ be a real symmetric positive definite matrix and let $S = U\Sigma U^{\top}$ be a diagonalization of $S$. Prove that the closest rank $1$ matrix (in the $L^{2}-norm)$ to $S$ is $u_{1}\sigma_{1} u_{1}^{\top}$ , where $u_{1}$ is the first column of $U$.

<!-- PAGE 802 -->
