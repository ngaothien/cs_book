# Hessenberg Matrices


<!-- PAGE 669 -->
obtained by settting the entries of the part of $A_{k+1}$ below the diagonal to $0$. Then we can find the corresponding eigenvectors by solving the linear system
$$Tv = t_{ii}v,$$
and since $T$ is upper triangular, this can be done by bottom-up elimination. We leave it as an exercise to show that the following vectors $v^{i} = (v_{1}^{i}, \dots  , v_{n}^{i})$ are eigenvectors:
$$v^{1}= e_{1},$$
and if $i = 2, \dots  , n$, then
$$ \le  \le$$
$$0if i + 1jn$$
$$$$
$$$$
$$1if j = i$$
$$$$
$$v_{j}^{i} =$$
$$\cdots$$
$$- \frac{t_{jj+1}v_{j+1}^{i}+ + t_{ji}v_{i}^{i}}{t_{jj}-t_{ii}} if i -1 \ge j \ge 1.$$
Then the vectors $(P_{k}v^{1}, \dots  , P_{k}v^{n})$ are a basis of (approximate) eigenvectors for $A$. In the special case where $T$ is a diagonal matrix, then $v^{i} = e_{i}$ for $i = 1, \dots  , n$ and the columns of $P_{k}$ are an orthonormal basis of (approximate) eigenvectors for $A$. If $A$ is a real matrix whose eigenvalues are not all real, then there is some complex pair of eigenvalues $\lambda  + i\mu$  (with $\mu  \neq  0)$, and the QR-algorithm cannot converge to a matrix whose strictly lower-triangular part is zero. There is a way to deal with this situation using upper Hessenberg matrices which will be discussed in the next section. Since the convergence of the QR method depends crucially only on the fact that the part of $A_{k}$ below the diagonal goes to zero, it would be highly desirable if we could replace $A$ by a similar matrix $U^{*}$ AU easily computable from $A$ having lots of zero strictly below the diagonal. We can’t expect $U^{*}$ AU to be a diagonal matrix (since this would mean that $A$ was easily diagonalized), but it turns out that there is a way to construct a matrix $H = U^{*}$ AU which is almost triangular, except that it may have an extra nonzero diagonal below the main diagonal. Such matrices called Hessenberg matrices are discussed in the next section.

## 18.2 Hessenberg Matrices


> **Definition 18.1.** An $n \times  n$ matrix (real or complex) $H$ is an (upper) Hessenberg matrix if it is almost triangular, except that it may have an extra nonzero diagonal below the main diagonal. Technically, $h_{jk} = 0$ for all $(j, k)$ such that $j$ - $k \ge 2$. The $5 \times  5$ matrix below is an example of a Hessenberg matrix.
$$H = \begin{pmatrix} * & * & * & * & * \\ h_{21} & * & * & * & * \\ 0 & h_{32} & * & * & * \\ 0 & 0 & h_{43} & * & * \\ 0 & 0 & 0 & h_{54} \end{pmatrix} .$$
$$*$$

<!-- PAGE 670 -->
The following result can be shown.

> **Theorem 18.2.** Every $n \times  n$ complex or real matrix $A$ is similar to an upper Hessenberg matrix $H$, that is, $A = UHU^{*}$ for some unitary matrix $U$. Furthermore, $U$ can be constructed as a product of Householder matrices (the definition is the same as in Section 13.1, except that $W$ is a complex vector, and that the inner product is the Hermitian inner product on $\mathbb{C}^{n})$. If $A$ is a real matrix, then $U$ is an orthogonal matrix (and $H$ is a real matrix). Theorem 18.2 and algorithms for converting a matrix to Hessenberg form are discussed in Trefethen and Bau $[182]$ (Lecture $26)$, Demmel $[48]$ (Section 4.4.6, in the real case), Serre $[162]$ (Theorem 13.1), and Meyer $[129]$ (Example 5.7.4, in the real case). The proof of correctness is not difficult and will be the object of a homework problem. The following functions written in Matlab implement a function to compute a Hessenberg form of a matrix. The function house constructs the normalized vector $u$ defining the Householder reflection that zeros all but the first entries in a vector $x$. function [uu, $u] =$ house(x) tol $= 2*10^(-15)$; % tolerance uu $= x; p =$ size(x,1); % computes $l^1-norm$ of x(2:p,1) n1 $=$ sum(abs(x(2:p,1))); if n1 $<=$ tol $u =$ zeros(p,1); uu $= u$; else $l =$ sqrt(x’*x); % $l^2$ norm of $x$ uu(1) $=$ x(1) $+$ signe(x(1))*l; $u = uu/sqrt(uu’*uu)$; end end The function signe(z) returms $-1$ if $z < 0$, else $+1$. The function buildhouse builds a Householder reflection from a vector uu. function $P =$ buildhouse(v,i) % This function builds a Householder reflection % [I $0$ ] % $[0$ PP] % from a Householder reflection % $PP =$ I - 2uu*uu’ % where uu $=$ v(i:n)

<!-- PAGE 671 -->
% If uu $= 0$ then $P$ - I % $n =$ size(v,1); if v(i:n) $==$ zeros(n - $i +$ 1,1) $P =$ eye(n); else $PP =$ eye(n - $i + 1)$ - 2*v(i:n)*v(i:n)’; $P =$ [eye(i-1) zeros(i-1, $n$ - $i + 1)$; zeros(n - $i + 1, i$ - $1)$ PP]; end end The function Hessenberg1 computes an upper Hessenberg matrix $H$ and an orthogonal matrix $Q$ such that $A = Q^{\top}HQ$. function $[H, Q] =$ Hessenberg1(A) % % This function constructs an upper Hessenberg % matrix $H$ and an orthogonal matrix $Q$ such that % $A =$ Q’ $H Q n =$ size(A,1); $H = A; Q =$ eye(n); for $i =$ 1:n-2 % $H(i+1:n,i)$ [~,u] $= house(H(i+1:n,i))$; % $u P =$ buildhouse(u,1); $Q(i+1:n,i:n) = P*Q(i+1:n,i:n); H(i+1:n,i:n) = H(i+1:n,i:n)$ - $2*u*(u’)*H(i+1:n,i:n); H(1:n,i+1:n) = H(1:n,i+1:n)$ - $2*H(1:n,i+1:n)*u*(u’)$; end end

> **Example 18.2.** If
$$A = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 2 & 3 & 4 & 5 \\ 3 & 4 & 5 & 6 \\ 4 & 5 & 6 & 7 \end{pmatrix} ,$$

<!-- PAGE 672 -->
running Hessenberg1 we find
$$1.0000-5.385200$$
$$-5.385215.2069-1.6893-0.0000$$
$$H =$$
$$-0.0000-1.6893-0.2069-0.0000$$
$$$$
$$0-0.00000.00000.0000$$
$$1.0000000$$
$$0-0.3714-0.5571-0.7428$$
$$Q =.$$
$$00.83390.1516-0.5307$$
$$$$
$$00.4082-0.81650.4082$$
An important property of (upper) Hessenberg matrices is that if some subdiagonal entry $H_{p+1p} = 0$, then $H$ is of the form
$$H = \begin{pmatrix} H_{11} & H_{12} \\ 0 & H_{22} \end{pmatrix} ,$$
where both $H_{11}$ and $H_{22}$ are upper Hessenberg matrices (with $H_{11}$ a $p \times  p$ matrix and $H_{22}$ a $(n$ - $p) \times  (n$ - $p)$ matrix), and the eigenvalues of $H$ are the eigenvalues of $H_{11}$ and $H_{22}$. For example, in the matrix
$$H = \begin{pmatrix} * & * & * & * & * \\ h_{21} & * & * & * & * \\ 0 & h_{32} & * & * & * \\ 0 & 0 & h_{43} & * & * \\ 0 & 0 & 0 & h_{54} \end{pmatrix} ,$$
$$*$$
if $h_{43} = 0$, then we have the block matrix
$$H = \begin{pmatrix} * & * & * & * & * \\ h_{21} & * & * & * & * \\ 0 & h_{32} & * & * & * \\ 0 & 0 & 0 & * & * \\ 0 & 0 & 0 & h_{54} \end{pmatrix} .$$
$$*$$
Then the list of eigenvalues of $H$ is the concatenation of the list of eigenvalues of $H_{11}$ and the list of the eigenvalues of $H_{22}$. This is easily seen by induction on the dimension of the block $H_{11}$. More generally, every upper Hessenberg matrix can be written in such a way that it has diagonal blocks that are Hessenberg blocks whose subdiagonal is not zero.

> **Definition 18.2.** An upper Hessenberg $n \times  n$ matrix $H$ is unreduced if $h_{i+1i} \neq  0$ for $i = 1, \dots  , n$ - $1$. A Hessenberg matrix which is not unreduced is said to be reduced.

<!-- PAGE 673 -->
The following is an example of an $8 \times  8$ matrix consisting of three diagonal unreduced Hessenberg blocks:
$$H = \begin{pmatrix} ⋆ & ⋆ & ⋆ & * & * & * & * & * \\ h_{21} & ⋆ & ⋆ & * & * & * & * & * \\ 0 & h_{32} & ⋆ & * & * & * & * & * \\ 0 & 0 & 0 & ⋆ & ⋆ & ⋆ & * & * \\ 0 & 0 & 0 & h_{54} & ⋆ & ⋆ & * & * \\ 0 & 0 & 0 & 0 & h_{65} & ⋆ & * & * \\ 0 & 0 & 0 & 0 & 0 & 0 & ⋆ & ⋆ \\ 0 & 0 & 0 & 0 & 0 & 0 & h_{87} & ⋆ \end{pmatrix} .$$
An interesting and important property of unreduced Hessenberg matrices is the following.

> **Proposition 18.3.** Let $H$ be an $n \times  n$ complex or real unreduced Hessenberg matrix. Then every eigenvalue of $H$ is geometrically simple, that is, $dim(E_{\lambda}) = 1$ for every eigenvalue $\lambda$ , where $E_{\lambda}$ is the eigenspace associated with $\lambda$ . Furthermore, if $H$ is diagonalizable, then every eigenvalue is simple, that is, $H$ has $n$ distinct eigenvalues.

*Proof.* We follow Serre’s proof $[162]$ (Proposition 3.26). Let $\lambda$  be any eigenvalue of $H$, let $M = \lambda I_{n}$ - $H$, and let $N$ be the $(n$ - $1) \times  (n$ - $1)$ matrix obtained from $M$ by deleting its first row and its last column. Since $H$ is upper Hessenberg, $N$ is a diagonal matrix with entries $-h_{i+1i} \neq  0, i = 1, \dots  , n$ - $1$. Thus $N$ is invertible and has rank $n$ - $1$. But a matrix has rank greater than or equal to the rank of any of its submatrices, so rank(M) $= n$ - $1$, since $M$ is singular. By the rank-nullity theorem, rank(Ker $N) = 1$, that is, $dim(E_{\lambda}) = 1$, as claimed. If $H$ is diagonalizable, then the sum of the dimensions of the eigenspaces is equal to $n$, which implies that the eigenvalues of $H$ are distinct. As we said earlier, a case where Theorem 18.1 applies is the case where $A$ is a symmetric (or Hermitian) positive definite matrix. This follows from two facts. The first fact is that if $A$ is Hermitian (or symmetric in the real case), then it is easy to show that the Hessenberg matrix similar to $A$ is a Hermitian (or symmetric in real case) tridiagonal matrix. The conversion method is also more efficient. Here is an example of a symmetric tridiagonal matrix consisting of three unreduced blocks:
$$H = \begin{pmatrix} \alpha_{1} & \beta_{1} & 0 & 0 & 0 & 0 & 0 & 0 \\ \beta_{1} & \alpha_{2} & \beta_{2} & 0 & 0 & 0 & 0 & 0 \\ 0 & \beta_{2} & \alpha_{3} & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & \alpha_{4} & \beta_{4} & 0 & 0 & 0 \\ 0 & 0 & 0 & \beta_{4} & \alpha_{5} & \beta_{5} & 0 & 0 \\ 0 & 0 & 0 & 0 & \beta_{5} & \alpha_{6} & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & \alpha_{7} & \beta_{7} \\ 0 & 0 & 0 & 0 & 0 & 0 & \beta_{7} & \alpha_{8} \end{pmatrix} .$$

<!-- PAGE 674 -->
Thus the problem of finding the eigenvalues of a symmetric (or Hermitian) matrix reduces to the problem of finding the eigenvalues of a symmetric (resp. Hermitian) tridiagonal matrix, and this can be done much more efficiently. The second fact is that if $H$ is an upper Hessenberg matrix and if it is diagonalizable, then there is an invertible matrix $P$ such that $H = P\Lambda P^{-1}$ with $\Lambda$  a diagonal matrix consisting of the eigenvalues of $H$, such that $P^{-1}$ has an LU-decomposition; see Serre $[162]$ (Theorem 13.3). As a consequence, since any symmetric (or Hermitian) tridiagonal matrix is a block diagonal matrix of unreduced symmetric (resp. Hermitian) tridiagonal matrices, by Proposition 18.3, we see that the QR algorithm applied to a tridiagonal matrix which is symmetric (or Hermitian) positive definite converges to a diagonal matrix consisting of its eigenvalues. Let us record this important fact.

> **Theorem 18.4.** Let $H$ be a symmetric (or Hermitian) positive definite tridiagonal matrix. If $H$ is unreduced, then the QR algorithm converges to a diagonal matrix consisting of the eigenvalues of $H$. Since every symmetric (or Hermitian) positive definite matrix is similar to a tridiagonal symmetric (resp. Hermitian) positive definite matrix, we deduce that we have a method for finding the eigenvalues of a symmetric (resp. Hermitian) positive definite matrix (more accurately, to find approximations as good as we want for these eigenvalues). If $A$ is a symmetric (or Hermitian) matrix, since its eigenvalues are real, for some $\mu  > 0$ large enough (pick $\mu  > \rho (A)), A + \mu$ I is symmetric (resp. Hermitan) positive definite, so we can apply the QR algorithm to an upper Hessenberg matrix similar to $A + \mu$ I to find its eigenvalues, and then the eigenvalues of $A$ are obtained by subtracting $\mu$ . The problem of finding the eigenvalues of a symmetric matrix is discussed extensively in Parlett $[140]$, one of the best references on this topic. The upper Hessenberg form also yields a way to handle singular matrices. First, checking the proof of Proposition 14.21 that an $n \times  n$ complex matrix $A$ (possibly singular) can be factored as $A = QR$ where $Q$ is a unitary matrix which is a product of Householder reflections and $R$ is upper triangular, it is easy to see that if $A$ is upper Hessenberg, then $Q$ is also upper Hessenberg. If $H$ is an unreduced upper Hessenberg matrix, since $Q$ is upper Hessenberg and $R$ is upper triangular, we have $h_{i+1i} = q_{i+1i}r_{ii}$ for $i = 1 \dots  , n -1$, and since $H$ is unreduced, $r_{ii} \neq  0$ for $i = 1, \dots  , n -1$. Consequently $H$ is singular iff $r_{nn} = 0$. Then the matrix $RQ$ is a matrix whose last row consists of zero’s thus we can deflate the problem by considering the $(n$ - $1) \times  (n$ - $1)$ unreduced Hessenberg matrix obtained by deleting the last row and the last column. After finitely many steps (not larger that the multiplicity of the eigenvalue $0)$, there remains an invertible unreduced Hessenberg matrix. As an alternative, see Serre $[162]$ (Chapter $13$, Section 13.3.2). As is, the QR algorithm, although very simple, is quite inefficient for several reasons. In the next section, we indicate how to make the method more efficient. This involves a lot of work and we only discuss the main ideas at a high level.
