# Problems


<!-- PAGE 654 -->
$\bullet$  Properties of the eigenvalues and eigenvectors of a normal linear map. $\bullet$  The complexification of a real vector space, of a linear map, and of a Euclidean inner product. $\bullet$  The eigenvalues of a self-adjoint map in a Hermitian space are real. $\bullet$  The eigenvalues of a self-adjoint map in a Euclidean space are real. $\bullet$  Every self-adjoint linear map on a Euclidean space has an orthonormal basis of eigenvectors. $\bullet$  Every normal linear map on a Euclidean space can be block diagonalized (blocks of size at most $2 \times  2)$ with respect to an orthonormal basis of eigenvectors. $\bullet$  Every normal linear map on a Hermitian space can be diagonalized with respect to an orthonormal basis of eigenvectors. $\bullet$  The spectral theorems for self-adjoint, skew-self-adjoint, and orthogonal linear maps (on a Euclidean space). $\bullet$  The spectral theorems for normal, symmetric, skew-symmetric, and orthogonal (real) matrices. $\bullet$  The spectral theorems for normal, Hermitian, skew-Hermitian, and unitary (complex) matrices. $\bullet$  The Rayleigh ratio and the Rayleigh–Ritz theorem. $\bullet$  Interlacing inequalities and the Cauchy interlacing theorem. $\bullet$  The Poincar´e separation theorem. $\bullet$  The Courant–Fischer theorem. $\bullet$  Inequalities involving perturbations of the eigenvalues of a symmetric matrix. $\bullet$  The Weyl inequalities.

## 17.9 Problems

Problem 17.1. Prove that the structure $E_{C}$ introduced in Definition 17.2 is indeed a complex vector space.

<!-- PAGE 655 -->
Problem 17.2. Prove that the formula
$$\langle u_{1} + iv_{1}, u_{2} + iv_{2}\rangle_{C}  = \langle u_{1}, u_{2}\rangle + \langle v_{1}, v_{2}\rangle + i(\langle v_{1}, u_{2}\rangle -\langle u_{1}, v_{2}\rangle )$$
defines a Hermitian form on $E_{C}$ that is positive definite and that $\langle$ -, $-\rangle_{C}$  agrees with $\langle$ -, $-\rangle$ on real vectors.
Problem 17.3. Given any linear map $f$ : $E \to E$, prove the map $f_{C}^{*}$  defined such that
$$f_{C}^{*} (u + iv) = f^{*}(u) + if^{*}(v)$$
for all $u, v \in E$ is the adjoint of $f_{C}$ w.r.t. $\langle$ -, $-\rangle_{C}$ .
Problem 17.4. Let $A$ be a real symmetric $n\times n$ matrix whose eigenvalues are nonnegative. Prove that for every $p > 0$, there is a real symmetric matrix $S$ whose eigenvalues are nonnegative such that $S^{p} = A$.
Problem 17.5. Let $A$ be a real symmetric $n \times  n$ matrix whose eigenvalues are positive.
$(1)$ Prove that there is a real symmetric matrix $S$ such that $A = e^{S}$.
$(2)$ Let $S$ be a real symmetric $n \times  n$ matrix. Prove that $A = e^{S}$ is a real symmetric $n \times  n$ matrix whose eigenvalues are positive.
Problem 17.6. Let $A$ be a complex matrix. Prove that if $A$ can be diagonalized with respect to an orthonormal basis, then $A$ is normal.
$$\mathbb{C}^{n} \mathbb{C}^{n}$$
Problem 17.7. Let $f$ : $\to$ be a linear map.
$(1)$ Prove that if $f$ is diagonalizable and if $\lambda_{1} , \dots  , \lambda_{n}$  are the eigenvalues of $f$, then $\lambda_{1}^{2} , \dots  , \lambda_{n}^{2}$  are the eigenvalues of $f^{2}$, and if $\lambda_{i}^{2}  = \lambda_{j}^{2}$  implies that $\lambda_{i}  = \lambda_{j}$ , then $f$ and $f^{2}$ have the same eigenspaces.
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
$(2)$ Let $f$ and $g$ be two real self-adjoint linear maps $f, g: \to$ . Prove that if $f$ and $g$ have nonnegative eigenvalues $(f$ and $g$ are positve semidefinite) and if $f^{2} = g^{2}$, then $f = g$.
Problem 17.8. $(1)$ Let $\mathfrak{so}(3)$ be the space of $3 \times  3$ skew symmetric matrices
$$$$
$$\mathfrak{so}(3) = \begin{pmatrix} 0 & -c & b \\ c & 0 & -a \\ b & a & 0 \end{pmatrix} a, b, c \in \mathbb{R}.$$
$$-$$
For any matrix
$$A = \begin{pmatrix} 0 & -c & b \\ c & 0 & -a \\ b & a & 0 \end{pmatrix} \in \mathfrak{so}(3),$$
$$-$$
$$\sqrt$$
if we let $\theta  = \overline{a}^{2} \overline{+}\overline{b}^{2} \overline{+}\overline{c}^{2}$, recall from Section 12.7 (the Rodrigues formula) that the exponential map exp: $\mathfrak{so}(3) \to$ SO(3) is given by
$$-$$
$$e^{A}= I_{3} + \frac{\sin \theta}{\theta} A + \frac{(1cos \theta )}{\theta^{2}} A^{2},if \theta  \neq  0,$$

<!-- PAGE 656 -->
with $exp(0_{3}) = I_{3}$.
$(2)$ Prove that $e^{A}$ is an orthogonal matrix of determinant $+1$, i.e., a rotation matrix.
$(3)$ Prove that the exponential map exp: $\mathfrak{so}(3) \to$ SO(3) is surjective. For this proceed as follows: Pick any rotation matrix $R \in$ SO(3);
$(1)$ The case $R =$ I is trivial.
$(2)$ If $R \neq$  I and tr(R) $\neq  -1$, then
$$



$$
$$\exp^{-1}(R) = \frac{\theta}{2 \sin \theta} (R -R^{T}) 1 + 2 \cos \theta  = \mathrm{tr}(R).$$
(Recall that tr(R) $= r_{1 1} + r_{2 2} + r_{3 3}$, the trace of the matrix $R)$. Show that there is a unique skew-symmetric $B$ with corresponding $\theta$  satisfying $0 < \theta  < \pi$  such that $e^{B} = R$.
$(3)$ If R̸ $=$ I and tr(R) $= -1$, then prove that the eigenvalues of $R$ are $1, -1, -1$, that $R = R^{\top}$, and that $R^{2} =$ I. Prove that the matrix
$$S = \frac{1}{2} (R -I)$$
is a symmetric matrix whose eigenvalues are $-1, -1, 0$. Thus $S$ can be diagonalized with respect to an orthogonal matrix $Q$ as
$$S = Q \begin{pmatrix} -1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{pmatrix} Q^{\top}.$$
Prove that there exists a skew symmetric matrix
$$U = \begin{pmatrix} 0 & -d & c \\ d & 0 & -b \\ c & b & 0 \end{pmatrix}$$
$$-$$
so that
$$U^{2} = S = \frac{1}{2} (R -I).$$
Observe that
$$U^{2}  = \begin{pmatrix} -(c^{2}+ d^{2}) & bc & bd \\ bc & -(b^{2}+ d^{2}) & cd \\ bd & cd & (b^{2}+ c^{2}) \end{pmatrix} ,$$
$$-$$

<!-- PAGE 657 -->
and use this to conclude that if $U^{2} = S$, then $b^{2} + c^{2} + d^{2} = 1$. Then show that
$$$$
$$\exp^{-1}(R) =(2k + 1)\pi \begin{pmatrix} 0 & -d & c \\ d & 0 & -b \\ c & b & 0 \end{pmatrix} , k \in \mathbb{Z},$$
$$-$$
where $(b, c, d)$ is any unit vector such that for the corresponding skew symmetric matrix $U$, we have $U^{2} = S$.
$(4)$ To find a skew symmetric matrix $U$ so that $U^{2} = S =_{2}^{1}(R$ - I) as in $(3)$, we can solve the system
$$\begin{pmatrix} b^{2}-1 & bc & bd \\ bc & c^{2}-1 & cd \\ bd & cd & d^{2} & 1 \end{pmatrix} = S.$$
$$-$$
We immediately get $b^{2}, c^{2}, d^{2}$, and then, since one of $b, c, d$ is nonzero, say $b$, if we choose the positive square root of $b^{2}$, we can determine $c$ and $d$ from bc and bd. Implement a computer program in Matlab to solve the above system.
Problem 17.9. It was shown in Proposition 15.15 that the exponential map is a map exp: $\mathfrak{so}(n) \to$ SO(n), $where\mathfrak{so}(n)$ is the vector space of real $n\times n$ skew-symmetric matrices. Use the spectral theorem to prove that the map exp: $\mathfrak{so}(n) \to$ SO(n) is surjective.
Problem 17.10. Let $\mathfrak{u}(n)$ be the space of (complex) $n \times  n$ skew-Hermitian matrices $(B^{*} = -B)$ and let $\mathfrak{su}(n)$ be its subspace consisting of skew-Hermitian matrice with zero trace (tr(B) $= 0)$.
$(1)$ Prove that if $B \in \mathfrak{u}(n)$, then $e^{B} \in$ U(n), and if if $B \in \mathfrak{su}(n)$, then $e^{B} \in$ SU(n). Thus we have well-defined maps exp: $\mathfrak{u}(n) \to$ U(n) and exp: $\mathfrak{su}(n) \to$ SU(n).
$(2)$ Prove that the map exp: $\mathfrak{u}(n) \to$ U(n) is surjective.
$(3)$ Prove that the map exp: $\mathfrak{su}(n) \to$ SU(n) is surjective.
Problem 17.11. Recall that a matrix $B \in M_{n}(\mathbb{R})$ is skew-symmetric if $B^{\top} = -B$. Check that the $set\mathfrak{so}(n)$ of skew-symmetric matrices is a vector space of dimension $n(n-1)/2$, and thus is isomorphic to $\mathbb{R}^{n(n-1)/2}$.
$(1)$ Given a rotation matrix
$$R = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} ,$$
where $0 < \theta  < \pi$ , prove that there is a skew symmetric matrix $B$ such that
$$R = (I -B)(I + B)^{-1}.$$

<!-- PAGE 658 -->
$(2)$ Prove that the eigenvalues of a skew-symmetric matrix are either $0$ or pure imaginary (that is, of the form $i\mu$  for $\mu  \in \mathbb{R}.)$. Let $C$ : $\mathfrak{so}(n) \to M_{n}(\mathbb{R})$ be the function (called the Cayley transform of $B)$ given by
$$C(B) = (I -B)(I + B)^{-1}.$$
Prove that if $B$ is skew-symmetric, then I - $B$ and I $+ B$ are invertible, and so $C$ is welldefined. Prove that
$$(I + B)(I -B) = (I -B)(I + B),$$
and that
$$(I + B)(I -B)^{-1}= (I -B)^{-1}(I + B).$$
Prove that
$$(C(B))^{\top}C(B) = I$$
and that
$$\det C(B) = +1,$$
so that C(B) is a rotation matrix. Furthermore, show that C(B) does not admit $-1$ as an eigenvalue.
$(3)$ Let SO(n) be the group of $n \times  n$ rotation matrices. Prove that the map
$$C : \mathfrak{so}(n) \to SO(n)$$
is bijective onto the subset of rotation matrices that do not admit $-1$ as an eigenvalue. Show that the inverse of this map is given by
$$B = (I + R)^{-1}(I -R) = (I -R)(I + R)^{-1},$$
where $R \in$ SO(n) does not admit $-1$ as an eigenvalue.
Problem 17.12. Please refer back to Problem 4.6. Let $\lambda_{1} , \dots  , \lambda_{n}$  be the eigenvalues of $A$ (not necessarily distinct). Using Schur’s theorem, $A$ is similar to an upper triangular matrix $B$, that is, $A = PBP^{-1}$ with $B$ upper triangular, and we may assume that the diagonal entries of $B$ in descending order are $\lambda_{1} , \dots  , \lambda_{n}$ .
$(1)$ If the $E_{ij}$ are listed according to total order given by
$$i = h and j > k$$
$$(i, j) < (h, k)iff$$
$$or i < h.$$
prove that $R_{B}$ is an upper triangular matrix whose diagonal entries are
$$(\lambda_{n} , \dots  , \lambda_{1} , \dots  , \lambda_{n} , \dots  , \lambda_{1} ),$$
$$|{z}$$
$$n2$$

<!-- PAGE 659 -->
and that $L_{B}$ is an upper triangular matrix whose diagonal entries are
$$(\lambda_{1} , \dots  , \lambda_{1} \dots  , \lambda_{n} , \dots  , \lambda_{n} ).$$
$$|{z}|{z}$$
$$nn$$
Hint. Figure out what are $R_{B}(E_{ij}) = E_{ij}B$ and $L_{B}(E_{ij}) = BE_{ij}$.
$(2)$ Use the fact that
$$L_{A} = L_{P} \circ L_{B} \circ L_{P}^{-1} ,R_{A} = R_{P}^{-1} \circ R_{B} \circ R_{P},$$
to express $ad_{A} = L_{A}$ - $R_{A}$ in terms of $L_{B}$ - $R_{B}$, and conclude that the eigenvalues of $ad_{A}$ are $\lambda_{i}$  - $\lambda_{j}$ , for $i = 1, \dots  , n$, and for $j = n, \dots  , 1$.

<!-- PAGE 660 -->
