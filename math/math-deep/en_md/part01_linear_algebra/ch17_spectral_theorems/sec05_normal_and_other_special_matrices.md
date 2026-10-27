# Normal and Other Special Matrices


<!-- PAGE 642 -->

## 17.5 Normal and Other Special Matrices

First we consider real matrices. Recall the following definitions.

> **Definition 17.3.** Given a real $m \times  n$ matrix $A$, the transpose $A^{\top}$ of $A$ is the $n \times  m$ matrix $A^{\top} = (a_{i j}^{\top})$ defined such that
$$a_{i j}^{\top} = a_{j i}$$
for all $i, j, 1 \le i \le m, 1 \le j \le n$. A real $n \times  n$ matrix $A$ is $\bullet$  normal if
$$A A^{\top}= A^{\top}A,$$
$\bullet$  symmetric if
$$A^{\top}= A,$$
$\bullet$  skew-symmetric if
$$A^{\top}= -A,$$
$\bullet$  orthogonal if
$$A A^{\top}= A^{\top}A = I_{n}.$$
Recall from Proposition 12.14 that when $E$ is a Euclidean space and $(e_{1}, \dots , e_{n})$ is an orthonormal basis for $E$, if $A$ is the matrix of a linear map $f$ : $E \to E$ w.r.t. the basis $(e_{1}, \dots  , e_{n})$, then $A^{\top}$ is the matrix of the adjoint $f^{*}$ of $f$. Consequently, a normal linear map has a normal matrix, a self-adjoint linear map has a symmetric matrix, a skew-self-adjoint linear map has a skew-symmetric matrix, and an orthogonal linear map has an orthogonal matrix. Furthermore, if $(u_{1}, \dots  , u_{n})$ is another orthonormal basis for $E$ and $P$ is the change of basis matrix whose columns are the components of the $u_{i}$ w.r.t. the basis $(e_{1}, \dots  , e_{n})$, then $P$ is orthogonal, and for any linear map $f$ : $E \to E$, if $A$ is the matrix of $f$ w.r.t $(e_{1}, \dots  , e_{n})$ and $B$ is the matrix of $f$ w.r.t. $(u_{1}, \dots  , u_{n})$, then
$$B = P^{\top} AP.$$
As a consequence, Theorems 17.12 and 17.14–17.16 can be restated as follows.

<!-- PAGE 643 -->

> **Theorem 17.18.** For every normal matrix $A$ there is an orthogonal matrix $P$ and a block diagonal matrix $D$ such that $A = PD P^{\top}$ , where $D$ is of the form
$$D = \begin{pmatrix} D_{1} & \dots \\ D_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & D_{p} \end{pmatrix}$$
such that each block $D_{j}$ is either a one-dimensional matrix (i.e., a real scalar) or a twodimensional matrix of the form
$$D_{j} = \begin{pmatrix} \lambda_{j} & -\mu_{j} \\ \mu_{j} & \lambda_{j} \end{pmatrix} ,$$
where $\lambda_{j} , \mu_{j}  \in \mathbb{R}$, with $\mu_{j}  > 0$.

> **Theorem 17.19.** For every symmetric matrix $A$ there is an orthogonal matrix $P$ and a diagonal matrix $D$ such that $A = PD P^{\top}$ , where $D$ is of the form
$$D = \begin{pmatrix} \lambda_{1} & \dots \\ \lambda_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & \lambda_{n} \end{pmatrix} ,$$
where $\lambda_{i}  \in \mathbb{R}$.

> **Theorem 17.20.** For every skew-symmetric matrix $A$ there is an orthogonal matrix $P$ and a block diagonal matrix $D$ such that $A = PD P^{\top}$ , where $D$ is of the form
$$D = \begin{pmatrix} D_{1} & \dots \\ D_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & D_{p} \end{pmatrix}$$
such that each block $D_{j}$ is either $0$ or a two-dimensional matrix of the form
$$D_{j} = \begin{pmatrix} 0 \\ -\mu_{j} \\ \mu_{j} & 0 \end{pmatrix} ,$$
where $\mu_{j}  \in \mathbb{R}$, with $\mu_{j}  > 0$. In particular, the eigenvalues of $A$ are pure imaginary of the form $\pm i\mu_{j}$ , or $0$.

> **Theorem 17.21.** For every orthogonal matrix $A$ there is an orthogonal matrix $P$ and a block diagonal matrix $D$ such that $A = PD P^{\top}$ , where $D$ is of the form
$$D = \begin{pmatrix} D_{1} & \dots \\ D_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & D_{p} \end{pmatrix}$$

<!-- PAGE 644 -->
such that each block $D_{j}$ is either $1, -1$, or a two-dimensional matrix of the form
$$D_{j} = \begin{pmatrix} \cos \theta_{j} & -\sin \theta_{j} \\ \sin \theta_{j} & \cos \theta_{j} \end{pmatrix}$$
where $0 < \theta_{j}  < \pi$ . In particular, the eigenvalues of $A$ are of the form cos $\theta_{j}  \pm  i$ sin $\theta_{j} , 1$, or $-1$. Theorem 17.21 can be used to show that the exponential map exp: $\mathfrak{so}(n) \to$ SO(n) is surjective; see Gallier $[73]$. We now consider complex matrices.

> **Definition 17.4.** Given a complex $m \times  n$ matrix $A$, the transpose $A^{\top}$ of $A$ is the $n \times  m$
$$matrix A^{\top}= \begin{pmatrix} a_{i j}^{\top} \end{pmatrix} defined such that$$
$$a_{i j}^{\top} = a_{j i}$$
for all $i, j, 1 \le i \le m, 1 \le j \le n$. The conjugate $\overline{A}$ of $A$ is the $m \times  n$ matrix $\overline{A} = (b_{i j})$ defined such that
$$b_{i j} =\overline{a}_{i j}$$
for all $i, j, 1 \le i \le m, 1 \le j \le n$. Given an $m \times  n$ complex matrix $A$, the adjoint $A^{*}$ of $A$ is the matrix defined such that
$$A^{*}\overline{= (}\overline{A}^{\top}\overline{) = (}\overline{A})^{\top}.$$
A complex $n \times  n$ matrix $A$ is $\bullet$  normal if
$$AA^{*}= A^{*}A,$$
$\bullet$  Hermitian if
$$A^{*}= A,$$
$\bullet$  skew-Hermitian if
$$A^{*}= -A,$$
$\bullet$  unitary if
$$AA^{*}= A^{*}A = I_{n}.$$
