# The Unitary Group, Unitary Matrices


<!-- PAGE 545 -->
Remarks:
$(i)$ In the Euclidean case, we proved that the assumption
$$\|f(v) -f(u)\|= \|v -u\|for all u, v \in E and f(0) = 0(2')$$
implies $(3)$. For this we used the polarization identity
$$2u \cdot  v = \|u\|^{2}+ \|v\|^{2}-\|u -v\|^{2}.$$
In the Hermitian case the polarization identity involves the complex number $i$. In fact, the implication (2') implies $(3)$ is false in the Hermitian case! Conjugation $z \mapsto \overline{z}$ satisfies (2') since
$$|\overline{z}_{2} -\overline{z}_{1}| = |\overline{z}_{2}\overline{-}\overline{z}_{1}| = |z_{2} -z_{1}|,$$
and yet, it is not linear!
(ii) If we modify $(2)$ by changing the second condition by now requiring that there be some $\tau  \in E$ such that
$$f(\tau  + iu) = f(\tau ) + i(f(\tau  + u) -f(\tau ))$$
for all $u \in E$, then the function $g: E \to E$ defined such that
$$g(u) = f(\tau  + u) -f(\tau )$$
satisfies the old conditions of $(2)$, and the implications $(2) \to (3)$ and $(3) \to (1)$ prove that $g$ is linear, and thus that $f$ is affine. In view of the first remark, some condition involving $i$ is needed on $f$, in addition to the fact that $f$ is distance-preserving.

## 14.4 The Unitary Group, Unitary Matrices

In this section, as a mirror image of our treatment of the isometries of a Euclidean space, we explore some of the fundamental properties of the unitary group and of unitary matrices. As an immediate corollary of the Gram–Schmidt orthonormalization procedure, we obtain the QR-decomposition for invertible matrices. In the Hermitian framework, the matrix of the adjoint of a linear map is not given by the transpose of the original matrix, but by the conjugate of the original matrix. For the reader’s convenience we recall the following definitions from Section 9.2.

> **Definition 14.8.** Given a complex $m \times  n$ matrix $A$, the transpose $A^{\top}$ of $A$ is the $n \times  m$
$$matrix A^{\top}= \begin{pmatrix} a_{i j}^{\top} \end{pmatrix} defined such that$$
$$a_{i j}^{\top} = a_{j i},$$
and the conjugate $\overline{A}$ of $A$ is the $m \times  n$ matrix $\overline{A} = (b_{i j})$ defined such that
$$b_{i j} =\overline{a}_{i j}$$
for all $i, j, 1 \le i \le m, 1 \le j \le n$. The adjoint $A^{*}$ of $A$ is the matrix defined such that
$$A^{*}\overline{= (}\overline{A}^{\top}\overline{) =} \begin{pmatrix}\end{pmatrix} \overline{A}^{\top}.$$

<!-- PAGE 546 -->

> **Proposition 14.15.** Let $E$ be any Hermitian space of finite dimension $n$, and let $f$ : $E \to E$ be any linear map. The following properties hold:
$(1)$ The linear map $f$ : $E \to E$ is an isometry iff
$$f \circ f^{*} = f^{*} \circ f = id.$$
$(2)$ For every orthonormal basis $(e_{1}, \dots  , e_{n})$ of $E$, if the matrix of $f$ is $A$, then the matrix of $f^{*}$ is the adjoint $A^{*}$ of $A$, and $f$ is an isometry iff $A$ satisfies the identities
$$A A^{*}= A^{*}A = I_{n},$$
where $I_{n}$ denotes the identity matrix of order $n$, iff the columns of $A$ form an orthonormal basis of $\mathbb{C}^{n}$, iff the rows of $A$ form an orthonormal basis of $\mathbb{C}^{n}$.

*Proof.* $(1)$ The proof is identical to that of Proposition 12.14 $(1)$.
$(2)$ If $(e_{1}, \dots  , e_{n})$ is an orthonormal basis for $E$, let $A = (a_{i j})$ be the matrix of $f$, and let $B = (b_{i j})$ be the matrix of $f^{*}$ . Since $f^{*}$ is characterized by
$$f^{*} (u) \cdot  v = u \cdot  f(v)$$
for all $u, v \in E$, using the fact that if $w = w_{1}e_{1} + \cdots  + w_{n}e_{n}$, we have $w_{k} = w \cdot  e_{k}$, for all $k, 1 \le k \le n$; letting $u = e_{i}$ and $v = e_{j}$, we get
$$b_{j i} = f^{*} (e_{i}) \cdot  e_{j} = e_{i} \cdot  f(e_{j}) =\overline{f}\overline{(}\overline{e}_{j}\overline{)}\overline{\cdot}\overline{e}_{i} =\overline{a}_{i j},$$
for all $i, j, 1 \le i, j \le n$. Thus, $B = A^{*}$. Now if $X$ and $Y$ are arbitrary matrices over the basis $(e_{1}, \dots  , e_{n})$, denoting as usual the jth column of $X$ by $X^{j}$, and similarly for $Y$ , a simple calculation shows that
$$Y^{*}X = (X^{j}\cdot  Y^{i})_{1\le i,j\le n}.$$
Then it is immediately verified that if $X = Y = A$, then $A^{*}A = A A^{*} = I_{n}$ iff the column vectors $(A^{1}, \dots  , A^{n})$ form an orthonormal basis. Thus, from $(1)$, we see that $(2)$ is clear. Proposition 12.14 shows that the inverse of an isometry $f$ is its adjoint $f^{*}$ . Proposition 12.14 also motivates the following definition.

> **Definition 14.9.** A complex $n \times  n$ matrix is a unitary matrix if
$$A A^{*}= A^{*}A = I_{n}.$$
Remarks:

<!-- PAGE 547 -->
$(1)$ The conditions $A A^{*} = I_{n}, A^{*}A = I_{n}$, and $A^{-1} = A^{*}$ are equivalent. Given any two orthonormal bases $(u_{1}, \dots  , u_{n})$ and $(v_{1}, \dots  , v_{n})$, if $P$ is the change of basis matrix from $(u_{1}, \dots  , u_{n})$ to $(v_{1}, \dots  , v_{n})$, it is easy to show that the matrix $P$ is unitary. The proof of Proposition 14.14 $(3)$ also shows that if $f$ is an isometry, then the image of an orthonormal basis $(u_{1}, \dots  , u_{n})$ is an orthonormal basis.
$(2)$ Using the explicit formula for the determinant, we see immediately that
$$\det(\overline{A}\overline{) = \det(}\overline{A}\overline{)}.$$
If $f$ is a unitary transformation and $A$ is its matrix with respect to any orthonormal basis, from $AA^{*} =$ I, we get
$$\det(AA^{*}) = \det(A) \det(A^{*}) = \det(A\overline{)\det(}\overline{A}^{\top}\overline{) = \det(} A\overline{)\det(}\overline{A}\overline{) =} | \det(A)|^{2},$$
and so | det(A)| $= 1$. It is clear that the isometries of a Hermitian space of dimension $n$ form a group, and that the isometries of determinant $+1$ form a subgroup. This leads to the following definition.

> **Definition 14.10.** A very important example of unitary matrices is provided by Fourier matrices (up to a
$$\sqrt$$
factor of $\overline{n})$, matrices that arise in the various versions of the discrete Fourier transform. For more on this topic, see the problems, and Strang $[175, 178]$. The group SU(2) turns out to be the group of unit quaternions, invented by Hamilton. This group plays an important role in the representation of rotations in SO(3) used in computer graphics and robotics; see Chapter $16$. Now that we have the definition of a unitary matrix, we can explain how the Gram– Schmidt orthonormalization procedure immediately yields the QR-decomposition for matrices.

> **Definition 14.11.** Given any complex $n\times n$ matrix $A$, a QR-decomposition of $A$ is any pair of $n \times  n$ matrices $(U, R)$, where $U$ is a unitary matrix and $R$ is an upper triangular matrix such that $A = UR$.

> **Proposition 14.16.** Given any $n \times  n$ complex matrix $A$, if $A$ is invertible, then there is a unitary matrix $U$ and an upper triangular matrix $R$ with positive diagonal entries such that $A = UR$. The proof is absolutely the same as in the real case!
Remark: If $A$ is invertible and if $A = U_{1}R_{1} = U_{2}R_{2}$ are two QR-decompositions for $A$, then
$$R_{1}R_{2}^{-1}= U_{1}^{*} U_{2}.$$
