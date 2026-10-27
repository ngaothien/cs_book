# The Effect of a Change of Bases on Matrices


<!-- PAGE 141 -->
Therefore, the coordinates of the polynomial $2x^{3}$ - $x + 1$ over the basis $\mathcal{V}$ are
$$\begin{pmatrix} 1 \\ 2/3 \\ 1/3 \\ 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1/3 & 0 & 0 \\ 1 & 2/3 & 1/3 & 0 \\ 1 & 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \\ 0 \\ 2 \end{pmatrix} ,$$
and so
$$2x^{3}-x + 1 = B_{0}^{3}(x) + \frac{2}{3} B_{1}^{3}(x) + \frac{1}{3} B_{2}^{3}(x) + 2B_{3}^{3}(x).$$

## 4.4 The Effect of a Change of Bases on Matrices

The effect of a change of bases on the representation of a linear map is described in the following proposition.

> **Proposition 4.5.** Let $E$ and $F$ be vector spaces, let $\mathcal{U} = (u_{1}, \dots  , u_{n})$ and $\mathcal{U}' = (u_{1}', \dots  , u_{n}')$ be two bases of $E$, and let $\mathcal{V} = (v_{1}, \dots  , v_{m})$ and $\mathcal{V}' = (v_{1}', \dots  , v_{m}')$ be two bases of $F$. Let $P = P_{U',U}$ be the change of basis matrix from $\mathcal{U}$ to $\mathcal{U}'$, and let $Q = P_{V',V}$ be the change of basis matrix $from\mathcal{V} to\mathcal{V}'$. For any linear map $f$ : $E \to F$, let M(f) $= M_{U,V}(f)$ be the matrix associated to $f$ w.r.t. the bases $\mathcal{U}$ and $\mathcal{V}$, and let M' $(f) = M_{U',V'}(f)$ be the matrix associated to $f$ w.r.t. the bases $\mathcal{U}'$ and $\mathcal{V}'$. We have
$$M' (f) = Q^{-1}M(f)P,$$
or more explicitly
$$M_{U',V'}(f) = P_{V',V}^{-1} M_{U,V}(f)P_{U',U} = P_{V,V'}M_{U,V}(f)P_{U',U}.$$

*Proof.* Since $f$ : $E \to F$ can be written as $f = id_{F} \circ f \circ id_{E}$, since $P = P_{U',U}$ is the matrix of $id_{E}$ w.r.t. the bases $(u_{1}', \dots  , u_{n}')$ and $(u_{1}, \dots  , u_{n})$, and $Q^{-1} = P_{V'}^{-1}  = P_{V,V'}$ is the matrix of $id_{F}$ w.r.t. the bases $(v_{1}, \dots  , v_{m})$ and $(v_{1}', \dots  , v_{m}')$ as illustrated $by^{,V}$ the following diagram
$$f\mathcal{V}/$$
$$\mathcal{U}, E, F$$
$$\overline{M}\mathcal{U},\mathcal{V}\overline{(}\overline{f}\overline{)}$$
$$PidP-1id$$
$$U',\mathcal{U} E 'F$$
$$\mathcal{V},\mathcal{V}$$
$$\mathcal{U}', E_{f}^{MU',V'(f)}\mathcal{V}'/, F,$$
by Proposition 4.2, we have M' $(f) = Q^{-1}M(f)P$. As a corollary, we get the following result.

<!-- PAGE 142 -->

> **Corollary 4.6.** Let $E$ be a vector space, and let $\mathcal{U} = (u_{1}, \dots  , u_{n})$ and $\mathcal{U}' = (u_{1}', \dots  , u_{n}')$ be two bases of $E$. Let $P = P_{U',U}$ be the change of basis matrix from $\mathcal{U}$ to $\mathcal{U}'$. For any linear map $f$ : $E \to E$, let M(f) $= M_{U}(f)$ be the matrix associated to $f$ w.r.t. the basis $\mathcal{U}$, and let M' $(f) = M_{U'}(f)$ be the matrix associated to $f$ w.r.t. the basis $\mathcal{U}'$. We have
$$M' (f) = P^{-1} M(f)P,$$
or more explicitly,
$$M_{U'}(f) = P_{U',U}^{-1} M_{U}(f)P_{U',U} = P_{U,U'}M_{U}(f)P_{U',U},$$
as illustrated by the following diagram
$$f\mathcal{U}/$$
$$\mathcal{U}, E, E$$
$$\overline{M}\mathcal{U},\overline{(}\overline{f}\overline{)}$$
$$PidP-1id$$
$$U',\mathcal{U} E 'E$$
$$\mathcal{U},\mathcal{U}$$
$$MU'(f)\mathcal{U}'/$$
$$\mathcal{U}', E, E.$$
$$\overline{f}$$

> **Example 4.3.** Let $E =\mathbb{R}^{2}, \mathcal{U} = (e_{1}, e_{2})$ where $e_{1} = (1, 0)$ and $e_{2} = (0, 1)$ are the canonical basis vectors, let $\mathcal{V} = (v_{1}, v_{2}) = (e_{1}, e_{1}$ - $e_{2})$, and let
$$A = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} .$$
The change of basis matrix $P = P_{V,U}$ from $\mathcal{U}$ to $\mathcal{V}$ is
$$P = \begin{pmatrix} 1 & 1 \\ 0 & -1 \end{pmatrix} ,$$
and we check that
$$P^{-1}= P.$$
Therefore, in the basis $\mathcal{V}$, the matrix representing the linear map $f$ defined by $A$ is
$$A'= P^{-1}AP = PAP = \begin{pmatrix} 1 & 1 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} = D,$$
a diagonal matrix. In the basis $\mathcal{V}$, it is clear what the action of $f$ is: it is a stretch by a factor of $2$ in the $v_{1}$ direction and it is the identity in the $v_{2}$ direction. Observe that $v_{1}$ and $v_{2}$ are not orthogonal. What happened is that we diagonalized the matrix $A$. The diagonal entries $2$ and $1$ are the eigenvalues of $A$ (and $f)$, and $v_{1}$ and $v_{2}$ are corresponding eigenvectors. We will come back to eigenvalues and eigenvectors later on.

<!-- PAGE 143 -->

> **Example 4.4.** Let $E =\mathbb{R}^{2}, \mathcal{U} = (e_{1}, e_{2})$ where $e_{1} = (1, 0)$ and $e_{2} = (0, 1)$ are the canonical basis vectors, let
$$\mathcal{V} = (v_{1}, v_{2}),withv_{1} = \begin{pmatrix} \cos \phi /2 \\ \sin \phi /2 \end{pmatrix} ,v_{2} = \begin{pmatrix} -\sin \phi /2 \\ \cos \phi /2 \end{pmatrix} ,$$
and let $A$ be the reflection about the line making an angle $\phi /2$ with the x-axis (see Example 2.4) given by
$$A = \begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} .$$
The change of basis matrix $P = P_{V,U}$ from $\mathcal{U}$ to $\mathcal{V}$ is
$$P = \begin{pmatrix} \cos \phi /2 & -\sin \phi /2 \\ \sin \phi /2 & \cos \phi /2 \end{pmatrix}$$
and we check that
$$P^{-1}= P^{\top}.$$
Using the notation of Example 2.4, $A = \rho_{\phi}$  and $P$ is the rotation matrix $P = M_{\phi /2}$. Since we proved that
$$\rho_{\phi}  = M_{\phi /2}\rho_{0} M_{-\phi /2}$$
and the inverse of $M_{\phi /2}$ is $M_{-\phi /2}$, we obtain
$$M_{-\phi /2}\rho_{\phi} M_{\phi /2} = \rho_{0} .$$
Therefore, in the basis $\mathcal{V}$, the matrix representing the linear map $f$ defined by $A$ is A' $= P^{-1}AP = P^{\top}AP = M_{-\phi /2}\rho_{\phi} M_{\phi /2}$
$$= \begin{pmatrix} \cos \phi /2 & \sin \phi /2 \\ -\sin \phi /2 & \cos \phi /2 \end{pmatrix} \begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} \begin{pmatrix} \cos \phi /2 & -\sin \phi /2 \\ \sin \phi /2 & \cos \phi /2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \rho_{0} ,$$
a diagonal matrix. In the basis $\mathcal{V}$, the matrix $\rho_{0}$  is the reflection about the x-axis (see Example 2.4). In the concrete case where $\phi  = \pi /2$,
$$A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$
is the reflection about the line of equation $y = x$ making an angle $\pi /4$ with the x-axix and
$$P = \begin{pmatrix} \sqrt & \sqrt \\ \sqrt{2}/2 & -\sqrt{2}/2 \\ 2/2 & 2/2 \end{pmatrix} .$$
The above examples show that the same linear map can be represented by different matrices. This suggests making the following definition:

<!-- PAGE 144 -->

> **Definition 4.5.** Two $n\times n$ matrices $A$ and $B$ are said to be similar iff there is some invertible matrix $P$ such that
$$B = P^{-1} AP.$$
It is easily checked that similarity is an equivalence relation. From our previous considerations, two $n \times  n$ matrices $A$ and $B$ are similar iff they represent the same linear map with respect to two different bases. The following surprising fact can be shown: Every square matrix $A$ is similar to its transpose $A^{\top}$. The proof requires advanced concepts (the Jordan form or similarity invariants). If $\mathcal{U} = (u_{1}, \dots  , u_{n})$ and $\mathcal{V} = (v_{1}, \dots  , v_{n})$ are two bases of $E$, the change of basis matrix
$$P = P_{V,U} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix}$$
from $(u_{1}, \dots  , u_{n})$ to $(v_{1}, \dots  , v_{n})$ is the matrix whose jth column consists of the coordinates of $v_{j}$ over the basis $(u_{1}, \dots  , u_{n})$, which means that
$$v_{j} = \sum_{i=1}^{n}  a_{ij}u_{i}.$$
$$It is natural to extend the matrix notation and to express the vector \begin{pmatrix} v_{1} \\ \vdots \\ v_{n} \end{pmatrix} in E^{n} as the$$
$$product of a matrix times the vector \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} in E^{n}, namely as$$
$$\begin{pmatrix} v_{1} \\ v_{2} \\ \vdots \\ v_{n} \end{pmatrix} = \begin{pmatrix} a_{11} & a_{21} & \cdots & a_{n1} \\ a_{12} & a_{22} & \cdots & a_{n2} \\ \vdots & \vdots & \ddots & \vdots \\ a_{1n} & a_{2n} & \cdots & a_{nn} \end{pmatrix} \begin{pmatrix} u_{1} \\ u_{2} \\ \vdots \\ u_{n} \end{pmatrix} ,$$
but notice that the matrix involved is not $P$, but its transpose $P^{\top}$ . This observation has the following consequence: if $\mathcal{U} = (u_{1}, \dots  , u_{n})$ and $\mathcal{V} = (v_{1}, \dots  , v_{n})$ are two bases of $E$ and if
$$\begin{pmatrix} v_{1} \\ \vdots \\ v_{n} \end{pmatrix} = A \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} ,$$

<!-- PAGE 145 -->
that is,
$$v_{i} = \sum_{j=1}^{n}  a_{ij}u_{j},$$
for any vector $w \in E$, we have
$$w = \sum_{i=1}^{n}  x_{i}u_{i} = \sum_{k=1}^{n}  y_{k}v_{k} = \sum_{k=1}^{n}  y_{k} \begin{pmatrix} a_{kj}u_{j} \end{pmatrix} \sum_{j=1}^{n}  = \sum_{j=1}^{n}  \begin{pmatrix} a_{kj}y_{k} \end{pmatrix} \sum_{k=1}^{n}  u_{j},$$
so
$$x_{i} = \sum_{k=1}^{n}  a_{kj}y_{k},$$
which means (note the inevitable transposition) that
$$\begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix} = A^{\top} \begin{pmatrix} y_{1} \\ \vdots \\ y_{n} \end{pmatrix} ,$$
and so
$$\begin{pmatrix} y_{1} \\ \vdots \\ y_{n} \end{pmatrix} = (A^{\top})^{-1} \begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix} .$$
It is easy to see that $(A^{\top})^{-1} = (A^{-1})^{\top}$. Also, if $\mathcal{U} = (u_{1}, \dots  , u_{n}), \mathcal{V} = (v_{1}, \dots  , v_{n})$, and $\mathcal{W} = (w_{1}, \dots  , w_{n})$ are three bases of $E$, and if the change of basis matrix from $\mathcal{U}$ to $\mathcal{V}$ is $P = P_{V,U}$ and the change of basis matrix from $\mathcal{V}$ to $\mathcal{W}$ is $Q = P_{W,V}$, then
$$\begin{pmatrix} v_{1} \\ \vdots \\ v_{n} \end{pmatrix} = P^{\top} \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} , \begin{pmatrix} w_{1} \\ \vdots \\ w_{n} \end{pmatrix} = Q^{\top} \begin{pmatrix} v_{1} \\ \vdots \\ v_{n} \end{pmatrix} ,$$
so
$$\begin{pmatrix} w_{1} \\ \vdots \\ w_{n} \end{pmatrix} = Q^{\top}P^{\top} \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} = (PQ)^{\top} \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} ,$$
which means that the change of basis matrix $P_{W,U}$ from $\mathcal{U}$ to $\mathcal{W}$ is PQ. This proves that
$$P_{W,U} = P_{V,U}P_{W,V}.$$
Remark: In order to avoid the transposition involved in writing
$$\begin{pmatrix} v_{1} \\ \vdots \\ v_{n} \end{pmatrix} = P^{\top} \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} ,$$

<!-- PAGE 146 -->
as a more convenient notation we may write
$$\begin{pmatrix} v_{1} & \cdots & v_{n} \end{pmatrix} = \begin{pmatrix} u_{1} & \cdots & u_{n} \end{pmatrix} P.$$
Here we are defining the product
$$\begin{pmatrix} u_{1} & \cdots & u_{n} \end{pmatrix} \begin{pmatrix} p_{1j} \\ \vdots \\ p_{nj} \end{pmatrix} (*)$$
$$of a row of vectors \begin{pmatrix} u_{1} & \cdots & u_{n} \end{pmatrix} by the jth column of P as the linear combination$$
$$\sum_{i=1}^{n}  p_{ij}u_{i}.$$
Such a definition is needed since scalar multiplication of a vector by a scalar is only defined if the scalar is on the left of the vector, but in the matrix expression (*) above, the vectors are on the left of the scalars! Even though matrices are indispensable since they are the major tool in applications of linear algebra, one should not lose track of the fact that linear maps are more fundamental because they are intrinsic
$$objects that do not depend on the choice of bases.$$
Consequently, we advise the reader to try to think in terms of
$$linear maps rather than reduce everything to matrices.$$
In our experience, this is particularly effective when it comes to proving results about linear maps and matrices, where proofs involving linear maps are often more “conceptual.” These proofs are usually more general because they do not depend on the fact that the dimension is finite. Also, instead of thinking of a matrix decomposition as a purely algebraic operation, it is often illuminating to view it as a geometric decomposition. This is the case of the SVD, which in geometric terms says that every linear map can be factored as a rotation, followed by a rescaling along orthogonal axes and then another rotation. After all,
$$a matrix is a representation of a linear map,$$
and most decompositions of a matrix reflect the fact that with a suitable choice of a basis (or bases), the linear map is a represented by a matrix having a special shape. The problem is then to find such bases. Still, for the beginner, matrices have a certain irresistible appeal, and we confess that it takes a certain amount of practice to reach the point where it becomes more natural to
