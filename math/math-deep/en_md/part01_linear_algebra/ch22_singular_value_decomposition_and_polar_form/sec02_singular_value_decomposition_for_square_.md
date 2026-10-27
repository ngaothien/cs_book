# Singular Value Decomposition for Square Matrices


<!-- PAGE 753 -->
Since
$$\dim(\mathrm{Im} f) = n -\dim(\mathrm{Ker} f)$$
and
$$\dim(\mathrm{Im} f^{*} ) = n -\dim((\mathrm{Im} f^{*} )^{\perp}),$$
from
$$\mathrm{Ker} f = (\mathrm{Im} f^{*} )^{\perp}$$
we also have
$$\dim(\mathrm{Ker} f) = \dim((\mathrm{Im} f^{*} )^{\perp}),$$
from which we obtain
$$\dim(\mathrm{Im} f) = \dim(\mathrm{Im} f^{*} ).$$
Since
$$\dim(\mathrm{Ker} (f^{*} \circ f)) + \dim(\mathrm{Im} (f^{*} \circ f)) = \dim(E),$$
Ker $(f^{*} \circ f) =$ Ker $f$ and Ker $f =$ (Im $f^{*} )^{\perp}$, we get
$$\dim((\mathrm{Im} f^{*} )^{\perp}) + \dim(\mathrm{Im} (f^{*} \circ f)) = \dim(E).$$
Since
$$\dim((\mathrm{Im} f^{*} )^{\perp}) + \dim(\mathrm{Im} f^{*} ) = \dim(E),$$
we deduce that
$$\dim(\mathrm{Im} f^{*} ) = \dim(\mathrm{Im} (f^{*} \circ f)).$$
A similar proof shows that
$$\dim(\mathrm{Im} f) = \dim(\mathrm{Im} (f \circ f^{*} )).$$
Consequently, $f, f^{*} , f^{*} \circ f$, and $f \circ f^{*}$ have the same rank.

## 22.2 Singular Value Decomposition for

$$Square Matrices$$
We will now prove that every square matrix has an SVD. Stronger results can be obtained if we first consider the polar form and then derive the SVD from it (there are uniqueness properties of the polar decomposition). For our purposes, uniqueness results are not as important so we content ourselves with existence results, whose proofs are simpler. Readers interested in a more general treatment are referred to Gallier $[73]$. The early history of the singular value decomposition is described in a fascinating paper by Stewart $[171]$. The SVD is due to Beltrami and Camille Jordan independently $(1873, 1874)$. Gauss is the grandfather of all this, for his work on least squares $(1809, 1823)$ (but Legendre also published a paper on least squares!). Then come Sylvester, Schmidt, and

<!-- PAGE 754 -->
Hermann Weyl. Sylvester’s work was apparently “opaque.” He gave a computational method to find an SVD. Schmidt’s work really has to do with integral equations and symmetric and asymmetric kernels $(1907)$. Weyl’s work has to do with perturbation theory $(1912)$. Autonne came up with the polar decomposition $(1902, 1915)$. Eckart and Young extended SVD to rectangular matrices $(1936, 1939)$.

> **Theorem 22.5.** (Singular value decomposition) For every real $n\times n$ matrix $A$ there are two orthogonal matrices $U$ and $V$ and a diagonal matrix $D$ such that $A = V DU^{\top}$ , where $D$ is of the form
$$D = \begin{pmatrix} \sigma_{1} & \dots \\ \sigma_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & \sigma_{n} \end{pmatrix} ,$$
where $\sigma_{1} , \dots  , \sigma_{r}$  are the singular values of $A$, i.e., the (positive) square roots of the nonzero eigenvalues of $A^{\top}A$ and $A A^{\top}$, and $\sigma_{r+1}  = \cdots  = \sigma_{n}  = 0$. The columns of $U$ are eigenvectors of $A^{\top}A$, and the columns of $V$ are eigenvectors of $A A^{\top}$.

*Proof.* Since $A^{\top}A$ is a symmetric matrix, in fact, a positive semidefinite matrix, there exists an orthogonal matrix $U$ such that
$$A^{\top}A = UD^{2}U^{\top} ,$$
with $D = diag(\sigma_{1} , \dots  , \sigma_{r} , 0, \dots  , 0)$, where $\sigma_{1}^{2} , \dots  , \sigma_{r}^{2}$  are the nonzero eigenvalues of $A^{\top}A$, and where $r$ is the rank of $A$; that is, $\sigma_{1} , \dots  , \sigma_{r}$  are the singular values of $A$. It follows that
$$U^{\top} A^{\top}AU = (AU)^{\top}AU = D^{2},$$
and if we let $f_{j}$ be the jth column of $AU$ for $j = 1, \dots  , n$, then we have
$$\langle f_{i}, f_{j}\rangle = \sigma_{i}^{2}  \delta_{ij} ,1 \le i, j \le r$$
and
$$f_{j} = 0,r + 1 \le j \le n.$$
If we define $(v_{1}, \dots  , v_{r})$ by
$$v_{j} = \sigma_{j}^{-1}  f_{j},1 \le j \le r,$$
then we have
$$\langle v_{i}, v_{j}\rangle = \delta_{ij} ,1 \le i, j \le r,$$
so complete $(v_{1}, \dots  , v_{r})$ into an orthonormal basis $(v_{1}, \dots  , v_{r}, v_{r+1}, \dots  , v_{n})$ (for example, using Gram–Schmidt). Now since $f_{j} = \sigma_{j} v_{j}$ for $j = 1 \dots  , r$, we have
$$\langle v_{i}, f_{j}\rangle = \sigma_{j} \langle v_{i}, v_{j}\rangle = \sigma_{j} \delta_{i,j} ,1 \le i \le n, 1 \le j \le r$$

<!-- PAGE 755 -->
and since $f_{j} = 0$ for $j = r + 1, \dots  , n$,
$$\langle v_{i}, f_{j}\rangle = 01 \le i \le n, r + 1 \le j \le n.$$
If $V$ is the matrix whose columns are $v_{1}, \dots  , v_{n}$, then $V$ is orthogonal and the above equations prove that
$$V^{\top} AU = D,$$
which yields $A = V DU^{\top}$ , as required. The equation $A = V DU^{\top}$ implies that
$$A^{\top}A = UD^{2}U^{\top} ,AA^{\top}= V D^{2}V^{\top} ,$$
which shows that $A^{\top}A$ and $AA^{\top}$ have the same eigenvalues, that the columns of $U$ are eigenvectors of $A^{\top}A$, and that the columns of $V$ are eigenvectors of $AA^{\top}$.

> **Example 22.4.** Here is a simple example of how to use the proof of Theorem 22.5 to obtain
$$an SVD decomposition.Let A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} .Then A^{\top}= \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} , A^{\top}A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} , and$$
$$AA^{\top}= \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix} . A simple calculation shows that the eigenvalues of A^{\top}A are 2 and 0, and$$
$$for the eigenvalue 2, a unit eigenvector is \begin{pmatrix} \sqrt \\ 1/\sqrt{2} \\ 1/ & 2 \end{pmatrix} , while a unit eigenvector for the eigenvalue$$
$$\sqrt$$
$$0 is \begin{pmatrix} \sqrt \\ 1/\sqrt{2} \\ -1/\sqrt2 \\ 1/ & 2 \end{pmatrix} . Observe that the singular values are \sigma_{1}  =\overline{2} and \sigma_{2}  = 0. Furthermore,$$
$$U = \begin{pmatrix} \sqrt \\ \sqrt & 1/\sqrt{2} \\ 1/ & 2 & -1/ & 2 \end{pmatrix} = U^{\top} . To determine V , the proof of Theorem 22.5 tells us to first$$
calculate
$$AU = \begin{pmatrix} \sqrt \\ \overline{2} & 0 \\ 0 & 0 \end{pmatrix} ,$$
and then set
$$\sqrt$$
$$v_{1} = (1/\overline{2)} \begin{pmatrix} \sqrt \\ \overline{2} \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} .$$
Once $v_{1}$ is determined, since $\sigma_{2}  = 0$, we have the freedom to choose $v_{2}$ such that $(v_{1}, v_{2})$
$$forms an orthonormal basis for\mathbb{R}^{2}. Naturally, we chose v_{2} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} and set V = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} . The$$
columns of $V$ are unit eigenvectors of $AA^{\top}$, but finding $V$ by computing unit eigenvectors of $AA^{\top}$ does not guarantee that these vectors are consistent with $U$ so that $A = V \Sigma U^{\top}$ . Thus one has to use AU instead. We leave it to the reader to check that
$$A = V \begin{pmatrix} \sqrt \\ \overline{2} & 0 \\ 0 & 0 \end{pmatrix} U^{\top} .$$
Theorem 22.5 suggests the following definition.

<!-- PAGE 756 -->

> **Definition 22.3.** A triple $(U, D, V$ ) such that $A = V D U^{\top}$ , where $U$ and $V$ are orthogonal and $D$ is a diagonal matrix whose entries are nonnegative (it is positive semidefinite) is called a singular value decomposition (SVD) of $A$. If $D = diag(\sigma_{1} , \dots  , \sigma_{n}$ ), it is customary to assume that $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{n}$ . The Matlab command for computing an SVD $A = V DU^{\top}$ of a matrix $A$ is $[V, D, U] =$ svd(A). The proof of Theorem 22.5 shows that there are two orthonormal bases $(u_{1}, \dots  , u_{n})$ and $(v_{1}, \dots  , v_{n})$, where $(u_{1}, \dots  , u_{n})$ are eigenvectors of $A^{\top}A$ and $(v_{1}, \dots  , v_{n})$ are eigenvectors of $AA^{\top}$. Furthermore, $(u_{1}, \dots  , u_{r})$ is an orthonormal basis of Im $A^{\top}, (u_{r+1}, \dots  , u_{n})$ is an orthonormal basis of Ker $A, (v_{1}, \dots  , v_{r})$ is an orthonormal basis of Im $A$, and $(v_{r+1}, \dots  , v_{n})$ is an orthonormal basis of Ker $A^{\top}$. Using a remark made in Chapter $4$, if we denote the columns of $U$ by $u_{1}, \dots  , u_{n}$ and the columns of $V$ by $v_{1}, \dots  , v_{n}$, then we can write
$$A = V D U^{\top} = \sigma_{1} v_{1}u_{1}^{\top} + \cdots  + \sigma_{r} v_{r}u_{r}^{\top} ,$$
with $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{r}$ . As a consequence, if $r$ is a lot smaller than $n$ (we write $r \ll n)$, we see that $A$ can be reconstructed from $U$ and $V$ using a much smaller number of elements. This idea will be used to provide “low-rank” approximations of a matrix. The idea is to keep only the $k$ top singular values for some suitable $k \ll r$ for which $\sigma_{k+1} , \dots  , \sigma_{r}$  are very small.
Remarks:
$(1)$ In Strang $[176]$ the matrices $U, V, D$ are denoted by $U = Q_{2}, V = Q_{1}$, and $D = \Sigma$ , and an SVD is written as $A = Q_{1}\Sigma Q_{2}^{\top}$ . This has the advantage that $Q_{1}$ comes before $Q_{2}$ in $A = Q_{1}\Sigma Q_{2}^{\top}$ . This has the disadvantage that $A$ maps the columns of $Q_{2}$ (eigenvectors of $A^{\top}A)$ to multiples of the columns of $Q_{1}$ (eigenvectors of $A A^{\top})$.
$(2)$ Algorithms for actually computing the SVD of a matrix are presented in Golub and Van Loan $[83]$, Demmel $[48]$, and Trefethen and Bau $[182]$, where the SVD and its applications are also discussed quite extensively.
$(3)$ If $A$ is a symmetric matrix, then in general, there is no SVD $V \Sigma U^{\top}$ of $A$ with $V = U$. However, if $A$ is positive semidefinite, then the eigenvalues of $A$ are nonnegative, and so the nonzero eigenvalues of $A$ are equal to the singular values of $A$ and SVDs of $A$ are of the form
$$A = V \Sigma V^{\top} .$$
$(4)$ The SVD also applies to complex matrices. In this case, for every complex $n\times n$ matrix $A$, there are two unitary matrices $U$ and $V$ and a diagonal matrix $D$ such that
$$A = V D U^{*} ,$$
where $D$ is a diagonal matrix consisting of real entries $\sigma_{1} , \dots  , \sigma_{n}$ , where $\sigma_{1}  \ge \cdots  \ge \sigma_{r}$ are the singular values of $A$, i.e., the positive square roots of the nonzero eigenvalues of $A^{*}A$ and $A A^{*}$, and $\sigma_{r+1}  = \dots  = \sigma_{n}  = 0$.
