# The Rodrigues Formula


<!-- PAGE 484 -->
Remark: It is easy to show that the conditions $A A^{\top} = I_{n}, A^{\top}A = I_{n}$, and $A^{-1} = A^{\top}$, are equivalent. Given any two orthonormal bases $(u_{1}, \dots  , u_{n})$ and $(v_{1}, \dots  , v_{n})$, if $P$ is the change of basis matrix from $(u_{1}, \dots  , u_{n})$ to $(v_{1}, \dots  , v_{n})$, since the columns of $P$ are the coordinates
$$of the vectors v_{j} with respect to the basis (u_{1}, \dots  , u_{n}), if v_{j1} = \sum_{i1}  n=1 p_{i1j1}u_{i1} and v_{j2} =$$
$$\sum_{i2}  n=1 p_{i2j2}u_{i2}, since (u_{1}, \dots  , u_{n}) is orthonormal,$$
$$v_{j1} \cdot  v_{j2} = \sum_{i1=1i}^{n}  \sum_{2=1}^{n}  p_{i1j1}p_{i2j2}(u_{i1} \cdot  u_{i2}) = \sum_{i=1}^{n}  p_{ij1}p_{ij2},$$
and since $(v_{1}, \dots  , v_{n})$ is orthonormal, $v_{j1} \cdot  v_{j2} = \delta_{j1j2}$ , so the columns of $P$ are orthonormal, and by Proposition 12.14 $(2)$, the matrix $P$ is orthogonal. The proof of Proposition 12.12 $(3)$ also shows that if $f$ is an isometry, then the image of an orthonormal basis $(u_{1}, \dots  , u_{n})$ is an orthonormal basis. Students often ask why orthogonal matrices are not called orthonormal matrices, since their columns (and rows) are orthonormal bases! I have no good answer, but isometries do preserve orthogonality, and orthogonal matrices correspond to isometries. Recall that the determinant det(f) of a linear map $f$ : $E \to E$ is independent of the choice of a basis in $E$. Also, for every matrix $A \in M_{n}(\mathbb{R})$, we have det(A) $= det(A^{\top})$, and for any two $n \times  n$ matrices $A$ and $B$, we have det(AB) $=$ det(A) det(B). Then if $f$ is an isometry, and $A$ is its matrix with respect to any orthonormal basis, $A A^{\top} = A^{\top}A = I_{n}$ implies that $det(A)^{2} = 1$, that is, either det(A) $= 1$, or det(A) $= -1$. It is also clear that the isometries of a Euclidean space of dimension $n$ form a group, and that the isometries of determinant $+1$ form a subgroup. This leads to the following definition.

> **Definition 12.7.** Given a Euclidean space $E$ of dimension $n$, the set of isometries $f$ : $E \to E$ forms a subgroup of GL(E) denoted by O(E), or O(n) when $E =\mathbb{R}^{n}$, called the orthogonal group (of $E)$. For every isometry $f$, we have det(f) $= \pm 1$, where det(f) denotes the determinant of $f$. The isometries such that det(f) $= 1$ are called rotations, or proper isometries, or proper orthogonal transformations, and they form a subgroup of the special linear group SL(E) (and of O(E)), denoted by SO(E), or SO(n) when $E = \mathbb{R}^{n}$, called the special orthogonal group (of $E)$. The isometries such that det(f) $= -1$ are called improper isometries, or improper orthogonal transformations, or flip transformations.

## 12.7 The Rodrigues Formula

When $n = 3$ and $A$ is a skew symmetric matrix, it is possible to work out an explicit formula for $e^{A}$. For any $3 \times  3$ real skew symmetric matrix
$$A = \begin{pmatrix} 0 & -c & b \\ c & 0 & -a \\ b & a & 0 \end{pmatrix} ,$$
$$-$$

<!-- PAGE 485 -->
$$\sqrt$$
if we let $\theta  = \overline{a}^{2} \overline{+}\overline{b}^{2} \overline{+}\overline{c}^{2}$ and
$$B = \begin{pmatrix} a^{2} & ab & ac \\ ab & b^{2} & bc \\ ac & bc & c^{2} \end{pmatrix} ,$$
then we have the following result known as Rodrigues’ formula $(1840)$. The (real) vector space of $n \times  n$ skew symmetric matrices is denoted by $\mathfrak{so}(n)$.

> **Proposition 12.15.** The exponential map exp: $\mathfrak{so}(3) \to$ SO(3) is given by
$$-$$
$$e^{A}= \cos \theta  I_{3} + \frac{\sin \theta}{\theta} A + \frac{(1cos \theta )}{\theta^{2}} B,$$
or, equivalently, by
$$-$$
$$e^{A}= I_{3} + \frac{\sin \theta}{\theta} A + \frac{(1cos \theta )}{\theta^{2}} A^{2}$$
if $\theta  \neq  0$, with $e^{03} = I_{3}$. Proof sketch. First observe that
$$A^{2}= -\theta^{2} I_{3} + B,$$
since
$$$$
$$0-cb$$
$$A^{2} =c0-a \begin{pmatrix} 0 & -c & b \\ c & 0 & -a \\ b & a & 0 \end{pmatrix} = \begin{pmatrix} -c^{2}-b^{2} & ba & ca \\ ab & -c^{2}-a^{2} & cb \\ ac & cb & b^{2} & a^{2} \end{pmatrix}$$
$$-ba0---$$
$$  $$
$$-a^{2}-b^{2}-c^{2}00$$
$$=0-a^{2} -b^{2} -c^{2}0+ \begin{pmatrix} a^{2} & ba & ca \\ ab & b^{2} & cb \\ ac & cb & c^{2} \end{pmatrix}$$
$$00-a^{2}-b^{2}-c^{2}$$
$$= -\theta^{2} I_{3} + B,$$
and that
$$AB = BA = 0.$$
From the above, deduce that
$$A^{3}= -\theta^{2} A,$$
and for any $k \ge 0$,
$$A^{4k+1}= \theta^{4k} A,$$
$$A^{4k+2}= \theta^{4k} A^{2},$$
$$A^{4k+3}= -\theta^{4k+2} A,$$
$$A^{4k+4}= -\theta^{4k+2} A^{2}.$$

<!-- PAGE 486 -->
Then prove the desired result by writing the power series for $e^{A}$ and regrouping terms so that the power series for cos $\theta$  and sin $\theta$  show up. In particular
$$e^{A} = I_{3} + \sum_{p\ge1}  \frac{A^{p}}{p!} = I_{3} + \sum_{p\ge0}  \frac{A^{2p+1}}{(2p + 1)!} + \sum_{p\ge1}  \frac{A^{2p}}{(2p)!}$$
$$= I_{3} + \sum_{p\ge0}  \frac{(1)^{p}\theta^{2p}}{(2p + 1)!} -A + \sum_{p\ge1}  \frac{(1)^{p-1}\theta^{2(p-1)}}{(2p)!} -A^{2}$$
$$--$$
$$= I_{3} + \frac{A}{\theta} \sum_{p\ge0}  \frac{(1)^{p}\theta^{2p+1}}{(2p + 1)!} - \frac{A^{2}}{\theta^{2}} \sum_{p\ge1}  \frac{(1)^{p}\theta^{2p}}{(2p)!}$$
$$-$$
$$= I_{3} + \frac{\sin \theta}{\theta} A - \frac{A^{2}}{\theta^{2}} \sum_{p\ge0}  \frac{(1)^{p}\theta^{2p}}{(2p)!} + \frac{A^{2}}{\theta^{2}}$$
$$-$$
$$= I_{3} + \frac{\sin \theta}{\theta} A + \frac{(1cos \theta )}{\theta^{2}} A^{2},$$
as claimed. The above formulae are the well-known formulae expressing a rotation of axis specified by the vector (a, $b, c)$ and angle $\theta$ . The Rodrigues formula can used to show that the exponential map exp: $\mathfrak{so}(3) \to$ SO(3) is surjective. Given any rotation matrix $R \in$ SO(3), we have the following cases:
$(1)$ The case $R =$ I is trivial.
$(2)$ If $R \neq$  I and tr(R) $\neq  -1$, then
$$



$$
$$\exp^{-1}(R) = \frac{\theta}{2 \sin \theta} (R -R^{T}) 1 + 2 \cos \theta  = \mathrm{tr}(R).$$
(Recall that tr(R) $= r_{1 1} + r_{2 2} + r_{3 3}$, the trace of the matrix $R)$. Then there is a unique skew-symmetric $B$ with corresponding $\theta$  satisfying $0 < \theta  < \pi$ such that $e^{B} = R$.
$(3)$ If $R \neq$  I and tr(R) $= -1$, then $R$ is a rotation by the angle $\pi$  and things are more complicated, but a matrix $B$ can be found. We leave this part as a good exercise: see
Problem 17.8. The computation of a logarithm of a rotation in SO(3) as sketched above has applications in kinematics, robotics, and motion interpolation. As an immediate corollary of the Gram–Schmidt orthonormalization procedure, we obtain the QR-decomposition for invertible matrices.
