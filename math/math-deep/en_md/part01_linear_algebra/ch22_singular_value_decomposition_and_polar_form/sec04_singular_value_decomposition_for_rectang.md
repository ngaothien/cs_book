# Singular Value Decomposition for Rectangular Matrices


<!-- PAGE 759 -->
If $A$ is a complex $n \times  n$ matrix, the eigenvalues $\lambda_{1} , \dots  , \lambda_{n}$  and the singular values $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{n}$  of $A$ are not unrelated, since
$$\sigma_{1}^{2}  \cdots  \sigma_{n}^{2}  = \det(A^{*}A) = | \det(A)|^{2}$$
and
$$|\lambda_{1} | \cdots  |\lambda_{n} | = | \det(A)|,$$
so we have
$$|\lambda_{1} | \cdots  |\lambda_{n} | = \sigma_{1}  \cdots  \sigma_{n} .$$
More generally, Hermann Weyl proved the following remarkable theorem:

> **Theorem 22.6.** (Weyl’s inequalities, $1949)$ For any complex $n\times n$ matrix, $A$, if $\lambda_{1} , \dots  , \lambda_{n}  \in \mathbb{C}$ are the eigenvalues of $A$ and $\sigma_{1} , \dots  , \sigma_{n}  \in \mathbb{R}_{+}$ are the singular values of $A$, listed so that $|\lambda_{1}$ | $\ge \cdots  \ge |\lambda_{n}$ | and $\sigma_{1}  \ge \cdots  \ge \sigma_{n}  \ge 0$, then
$$|\lambda_{1} | \cdots  |\lambda_{n} | = \sigma_{1}  \cdots  \sigma_{n} and$$
$$|\lambda_{1} | \cdots  |\lambda_{k} | \le \sigma_{1}  \cdots  \sigma_{k} ,fork = 1, \dots  , n -1.$$
A proof of Theorem 22.6 can be found in Horn and Johnson $[99]$, Chapter $3$, Section 3.3, where more inequalities relating the eigenvalues and the singular values of a matrix are given. Theorem 22.5 can be easily extended to rectangular $m \times  n$ matrices, as we show in the next section. For various versions of the SVD for rectangular matrices, see Strang $[176]$ Golub and Van Loan $[83]$, Demmel $[48]$, and Trefethen and Bau $[182]$.

## 22.4 Singular Value Decomposition for

$$Rectangular Matrices$$
Here is the generalization of Theorem 22.5 to rectangular matrices.

> **Theorem 22.7.** (Singular value decomposition) For every real $m \times  n$ matrix $A$, there are two orthogonal matrices $U (n\times n)$ and $V (m\times m)$ and a diagonal $m\times n$ matrix $D$ such that $A = V D U^{\top}$ , where $D$ is of the form
$$D = \begin{pmatrix} \sigma_{1} & \dots \\ \sigma_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & \sigma_{n} \\ \vdots \\ 0 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ \vdots \\ 0 & \dots & 0 \end{pmatrix} or D = \begin{pmatrix} \sigma_{1} & \dots & 0 & \dots & 0 \\ \sigma_{2} & \dots & 0 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 \\ \dots & \sigma_{m} & 0 & \dots & 0 \end{pmatrix} ,$$

<!-- PAGE 760 -->
where $\sigma_{1} , \dots  , \sigma_{r}$  are the singular values of $A$, i.e. the (positive) square roots of the nonzero eigenvalues of $A^{\top}A$ and $A A^{\top}$, and $\sigma_{r+1}  = \dots  = \sigma_{p}  = 0$, where $p =$ min(m, $n)$. The columns of $U$ are eigenvectors of $A^{\top}A$, and the columns of $V$ are eigenvectors of $A A^{\top}$.

*Proof.* As in the proof of Theorem 22.5, since $A^{\top}A$ is symmetric positive semidefinite, there exists an $n \times  n$ orthogonal matrix $U$ such that
$$A^{\top}A = U\Sigma^{2} U^{\top} ,$$
with $\Sigma  = diag(\sigma_{1} , \dots  , \sigma_{r} , 0, \dots  , 0)$, where $\sigma_{1}^{2} , \dots  , \sigma_{r}^{2}$  are the nonzero eigenvalues of $A^{\top}A$, and where $r$ is the rank of $A$. Observe that $r \le min{m, n}$, and AU is an $m \times  n$ matrix. It follows that
$$U^{\top} A^{\top}AU = (AU)^{\top}AU = \Sigma^{2} ,$$
$$\mathbb{R}^{m}$$
and if we let $f_{j} \in$ be the jth column of $AU$ for $j = 1, \dots  , n$, then we have
$$\langle f_{i}, f_{j}\rangle = \sigma_{i}^{2}  \delta_{ij} ,1 \le i, j \le r$$
and
$$f_{j} = 0,r + 1 \le j \le n.$$
If we define $(v_{1}, \dots  , v_{r})$ by
$$v_{j} = \sigma_{j}^{-1}  f_{j},1 \le j \le r,$$
then we have
$$\langle v_{i}, v_{j}\rangle = \delta_{ij} ,1 \le i, j \le r,$$
so complete $(v_{1}, \dots  , v_{r})$ into an orthonormal basis $(v_{1}, \dots  , v_{r}, v_{r+1}, \dots  , v_{m})$ (for example, using Gram–Schmidt). Now since $f_{j} = \sigma_{j} v_{j}$ for $j = 1 \dots  , r$, we have
$$\langle v_{i}, f_{j}\rangle = \sigma_{j} \langle v_{i}, v_{j}\rangle = \sigma_{j} \delta_{i,j} ,1 \le i \le m, 1 \le j \le r$$
and since $f_{j} = 0$ for $j = r + 1, \dots  , n$, we have
$$\langle v_{i}, f_{j}\rangle = 01 \le i \le m, r + 1 \le j \le n.$$
If $V$ is the matrix whose columns are $v_{1}, \dots  , v_{m}$, then $V$ is an $m \times  m$ orthogonal matrix and if $m \ge n$, we let
$$D = \begin{pmatrix} \Sigma \\ 0_{m-n} \end{pmatrix} = \begin{pmatrix} \sigma_{1} & \dots \\ \sigma_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & \sigma_{n} \\ 0 & \vdots & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & \vdots & \dots & 0 \end{pmatrix} ,$$

<!-- PAGE 761 -->
else if $n \ge m$, then we let
$$D = \begin{pmatrix} \sigma_{1} & \dots & 0 & \dots & 0 \\ \sigma_{2} & \dots & 0 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots & 0 & \vdots & 0 \\ \dots & \sigma_{m} & 0 & \dots & 0 \end{pmatrix} .$$
In either case, the above equations prove that
$$V^{\top} AU = D,$$
which yields $A = V DU^{\top}$ , as required. The equation $A = V DU^{\top}$ implies that
$$A^{\top}A = UD^{\top}DU^{\top} = Udiag(\sigma_{1}^{2} , \dots  , \sigma_{r}^{2} , 0, \dots  , 0)U^{\top}$$
$$| {z }$$
$$n-r$$
and
$$AA^{\top}= V DD^{\top}V^{\top} = V \mathrm{diag}(\sigma_{1}^{2} , \dots  , \sigma_{r}^{2} , 0, \dots  , 0)V^{\top} ,$$
$$| {z }$$
$$m-r$$
which shows that $A^{\top}A$ and $AA^{\top}$ have the same nonzero eigenvalues, that the columns of $U$ are eigenvectors of $A^{\top}A$, and that the columns of $V$ are eigenvectors of $AA^{\top}$. A triple $(U, D, V$ ) such that $A = V D U^{\top}$ is called a singular value decomposition (SVD) of $A$. If $D = diag(\sigma_{1} , \dots  , \sigma_{p}$ ) (with $p =$ min(m, $n))$, it is customary to assume that $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{p}$ .
$$Example 22.7. Let A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \\ 0 & 0 \end{pmatrix} . Then A^{\top}= \begin{pmatrix} 1 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix} A^{\top}A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} , and AA^{\top}=$$
$$\begin{pmatrix} 2 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} .The reader should verify that A^{\top}A = U\Sigma^{2} U^{\top} where \Sigma^{2}  = \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix} and$$
$$U = U^{\top} = \begin{pmatrix} \sqrt & \sqrt \\ 1/\sqrt{2} & 1/\sqrt{2} \\ 1/ & 2 & -1/ & 2 \end{pmatrix} . Since AU = \begin{pmatrix} \sqrt \\ \overline{2} & 0 \\ 0 & 0 \\ 0 & 0 \end{pmatrix} , set v_{1} =_{2}^{\sqrt1} \begin{pmatrix} \sqrt \\ \overline{2} \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} ,$$
$$and complete an orthonormal basis for \mathbb{R}^{3} by assigning v_{2} = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} , and v_{3} = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} . Thus$$
$$V = I_{3}, and the reader should verify that A = V DU^{\top} , where D = \begin{pmatrix} \sqrt \\ \overline{2} & 0 \\ 0 & 0 \\ 0 & 0 \end{pmatrix} .$$

<!-- PAGE 762 -->
Even though the matrix $D$ is an $m \times  n$ rectangular matrix, since its only nonzero entries are on the descending diagonal, we still say that $D$ is a diagonal matrix. The Matlab command for computing an SVD $A = V DU^{\top}$ of a matrix $A$ is $[V, D, U] =$ svd(A). Beware that Matlab uses the convention that the SVD of a matrix $A$ is written as $A = UDV^{\top}$ , and so the call for this version of the SVD is $[U, D, V] =$ svd(A). If we view $A$ as the representation of a linear map $f$ : $E \to F$, where dim(E) $= n$ and dim(F) $= m$, the proof of Theorem 22.7 shows that there are two orthonormal bases $(u_{1}, \dots , u_{n})$ and $(v_{1}, \dots  , v_{m})$ for $E$ and $F$, respectively, where $(u_{1}, \dots  , u_{n})$ are eigenvectors of $f^{*} \circ f$ and $(v_{1}, \dots  , v_{m})$ are eigenvectors of $f \circ f^{*}$ . Furthermore, $(u_{1}, \dots  , u_{r})$ is an orthonormal basis of Im $f^{*} , (u_{r+1}, \dots  , u_{n})$ is an orthonormal basis of Ker $f, (v_{1}, \dots  , v_{r})$ is an orthonormal basis of Im $f$, and $(v_{r+1}, \dots  , v_{m})$ is an orthonormal basis of Ker $f^{*}$ . The SVD of matrices can be used to define the pseudo-inverse of a rectangular matrix; we will do so in Chapter $23$. The reader may also consult Strang $[176]$, Demmel $[48]$, Trefethen and Bau $[182]$, and Golub and Van Loan $[83]$. One of the spectral theorems states that a symmetric matrix can be diagonalized by an orthogonal matrix. There are several numerical methods to compute the eigenvalues of a symmetric matrix $A$. One method consists in tridiagonalizing $A$, which means that there exists some orthogonal matrix $P$ and some symmetric tridiagonal matrix $T$ such that $A = PTP^{\top}$ . In fact, this can be done using Householder transformations; see Theorem 18.2. It is then possible to compute the eigenvalues of $T$ using a bisection method based on Sturm sequences. One can also use Jacobi’s method. For details, see Golub and Van Loan $[83]$, Chapter $8$, Demmel $[48]$, Trefethen and Bau $[182]$, Lecture $26$, Ciarlet $[41]$, and Chapter $18$. Computing the SVD of a matrix $A$ is more involved. Most methods begin by finding orthogonal matrices $U$ and $V$ and a bidiagonal matrix $B$ such that $A = V BU^{\top}$ ; see Problem 13.8 and Problem 22.3. This can also be done using Householder transformations. Observe that $B^{\top}B$ is symmetric tridiagonal. Thus, in principle, the previous method to diagonalize a symmetric tridiagonal matrix can be applied. However, it is unwise to compute $B^{\top}B$ explicitly, and more subtle methods are used for this last step; the matrix of Problem 22.1 can be used, and see Problem 22.3. Again, see Golub and Van Loan $[83]$, Chapter $8$, Demmel $[48]$, and Trefethen and Bau $[182]$, Lecture $31$. The polar form has applications in continuum mechanics. Indeed, in any deformation it is important to separate stretching from rotation. This is exactly what QS achieves. The orthogonal part $Q$ corresponds to rotation (perhaps with an additional reflection), and the symmetric matrix $S$ to stretching (or compression). The real eigenvalues $\sigma_{1} , \dots  , \sigma_{r}$  of $S$ are the stretch factors (or compression factors) (see Marsden and Hughes $[124])$. The fact that $S$ can be diagonalized by an orthogonal matrix corresponds to a natural choice of axes, the principal axes. The SVD has applications to data compression, for instance in image processing. The idea is to retain only singular values whose magnitudes are significant enough. The SVD
