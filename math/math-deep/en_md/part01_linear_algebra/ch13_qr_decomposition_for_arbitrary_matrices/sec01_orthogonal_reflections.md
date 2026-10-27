# Orthogonal Reflections


<!-- PAGE 507 -->
Chapter $13$ QR-Decomposition for Arbitrary Matrices

## 13.1 Orthogonal Reflections

Hyperplane reflections are represented by matrices called Householder matrices. These matrices play an important role in numerical methods, for instance for solving systems of linear equations, solving least squares problems, for computing eigenvalues, and for transforming a symmetric matrix into a tridiagonal matrix. We prove a simple geometric lemma that immediately yields the QR-decomposition of arbitrary matrices in terms of Householder matrices. Orthogonal symmetries are a very important example of isometries. First let us review the definition of projections, introduced in Section 6.1, just after Proposition 6.7. Given a vector space $E$, let $F$ and $G$ be subspaces of $E$ that form a direct sum $E = F \oplus G$. Since every $u \in E$ can be written uniquely as $u = v + w$, where $v \in F$ and $w \in G$, we can define the two projections $p_{F}$ : $E \to F$ and $p_{G}$ : $E \to G$ such that $p_{F}(u) = v$ and $p_{G}(u) = w$. In Section 6.1 we used the notation $\pi_{1}$  and $\pi_{2}$ , but in this section it is more convenient to use $p_{F}$ and $p_{G}$. It is immediately verified that $p_{G}$ and $p_{F}$ are linear maps, and that
$$p_{F}^{2} = p_{F}, p_{G}^{2} = p_{G}, p_{F} \circ p_{G} = p_{G} \circ p_{F} = 0,andp_{F} + p_{G} = id.$$
.

> **Definition 13.1.** Given a vector space $E$, for any two subspaces $F$ and $G$ that form a direct sum $E = F \oplus G$, the symmetry (or reflection) with respect to $F$ and parallel to $G$ is the linear map $s: E \to E$ defined such that
$$s(u) = 2p_{F}(u) -u,$$
for every $u \in E$.
$$507$$

<!-- PAGE 508 -->
Because $p_{F} + p_{G} =$ id, note that we also have
$$s(u) = p_{F}(u) -p_{G}(u)$$
and
$$s(u) = u -2p_{G}(u),$$
$s^{2} =$ id, $s$ is the identity on $F$, and $s =$ -id on $G$. We now assume that $E$ is a Euclidean space of finite dimension.

> **Definition 13.2.** Let $E$ be a Euclidean space of finite dimension $n$. For any two subspaces $F$ and $G$, if $F$ and $G$ form a direct sum $E = F \oplus G$ and $F$ and $G$ are orthogonal, i.e., $F = G^{\perp}$, the orthogonal symmetry (or reflection) with respect to $F$ and parallel to $G$ is the linear map $s: E \to E$ defined such that
$$s(u) = 2p_{F}(u) -u = p_{F}(u) -p_{G}(u),$$
for every $u \in E$. When $F$ is a hyperplane, we call $s$ a hyperplane symmetry with respect to $F$ (or reflection about $F)$, and when $G$ is a plane (and thus dim(F) $= n$ - $2)$, we call $s$ a flip about $F$. A reflection about a hyperplane $F$ is shown in Figure 13.1.
$$G$$
$$u$$
$$p(u)$$
$$G$$
$$p (u)$$
$$F$$
$$-p (u)$$
$$G$$
$$s(u)$$
$$F$$

![Figure 13.1](../../assets/ch13/fig_13_1.png)

**Figure 13.1:** A reflection about the peach hyperplane $F$. Note that $u$ is purple, $p_{F}(u)$ is blue and $p_{G}(u)$ is red. For any two vectors $u, v \in E$, it is easily verified using the bilinearity of the inner product that
$$\|u + v\|^{2}-\|u -v\|^{2}= 4(u \cdot  v).(*)$$
In particular, if $u \cdot  v = 0$, then $\|u + v\| = \|u$ - $v\|$. Then since
$$u = p_{F}(u) + p_{G}(u)$$

<!-- PAGE 509 -->
and
$$s(u) = p_{F}(u) -p_{G}(u),$$
and since $F$ and $G$ are orthogonal, it follows that
$$p_{F}(u) \cdot  p_{G}(v) = 0,$$
and thus by (*)
$$\|s(u)\|= \|p_{F}(u) -p_{G}(u)\|= \|p_{F}(u) + p_{G}(u)\|= \|u\|,$$
so that $s$ is an isometry. Using Proposition 12.10, it is possible to find an orthonormal basis $(e_{1}, \dots  , e_{n})$ of $E$ consisting of an orthonormal basis of $F$ and an orthonormal basis of $G$. Assume that $F$ has dimension $p$, so that $G$ has dimension $n$ - $p$. With respect to the orthonormal basis $(e_{1}, \dots  , e_{n})$, the symmetry $s$ has a matrix of the form
$$\begin{pmatrix} I_{p} & 0 \\ 0 & -I_{n-p} \end{pmatrix} .$$
Thus, det(s) $= (-1)^{n-p}$, and $s$ is a rotation iff $n$ - $p$ is even. In particular, when $F$ is a hyperplane $H$, we have $p = n$ - $1$ and $n$ - $p = 1$, so that $s$ is an improper orthogonal transformation. When $F = {0}$, we have $s =$ -id, which is called the symmetry with respect to the origin. The symmetry with respect to the origin is a rotation iff $n$ is even, and an improper orthogonal transformation iff $n$ is odd. When $n$ is odd, since $s \circ s =$ id and det(s) $= (-1)^{n} = -1$, we observe that every improper orthogonal transformation $f$ is the composition $f = (f \circ s) \circ s$ of the rotation $f \circ s$ with $s$, the symmetry with respect to the origin. When $G$ is a plane, $p = n$ - $2$, and det(s) $= (-1)^{2} = 1$, so that a flip about $F$ is a rotation. In particular, when $n = 3, F$ is a line, and a flip about the line $F$ is indeed a rotation of measure $\pi$  as illustrated by Figure 13.2.
Remark: Given any two orthogonal subspaces $F, G$ forming a direct sum $E = F \oplus G$, let $f$ be the symmetry with respect to $F$ and parallel to $G$, and let $g$ be the symmetry with respect to $G$ and parallel to $F$. We leave as an exercise to show that
$$f \circ g = g \circ f = -id.$$
When $F = H$ is a hyperplane, we can give an explicit formula for s(u) in terms of any nonnull vector $w$ orthogonal to $H$. Indeed, from
$$u = p_{H}(u) + p_{G}(u),$$
since $p_{G}(u) \in G$ and $G$ is spanned by $w$, which is orthogonal to $H$, we have
$$p_{G}(u) = \lambda w$$

<!-- PAGE 510 -->
$$F$$
$$s(u)p  (u)u$$
$$F$$
$$G$$
$$\mathbb{R}^{3}$$
$$Figure 13.2: A flip inis a rotation of \pi  about the F axis.$$
for some $\lambda  \in \mathbb{R}$, and we get
$$u \cdot  w = \lambda \|w\|^{2},$$
and thus
$$\cdot$$
$$p_{G}(u) = \frac{(u w)}{\|w\|^{2}} w.$$
Since
$$s(u) = u -2p_{G}(u),$$
we get
$$2  \cdot$$
$$s(u) = u - \frac{(u w)}{\|w\|^{2}} w.$$
Since the above formula is important, we record it in the following proposition.

> **Proposition 13.1.** Let $E$ be a finite-dimensional Euclidean space and let $H$ be a hyperplane in $E$. For any nonzero vector $w$ orthogonal to $H$, the hyperplane reflection $s$ about $H$ is given by
$$2  \cdot$$
$$s(u) = u - \frac{(u w)}{\|w\|^{2}} w,u \in E.$$
Such reflections are represented by matrices called Householder matrices, which play an important role in numerical matrix analysis (see Kincaid and Cheney $[105]$ or Ciarlet $[41])$.

> **Definition 13.3.** A Householder matrix is a matrix of the form
$$WW^{\top}$$
$$H = I_{n} -2 \frac{WW^{\top}}{\|W\|^{2}} = I_{n} -2\overline{W}^{\top} W ,$$
$$\mathbb{R}^{n}$$
where $W \in$ is a nonzero vector.

<!-- PAGE 511 -->
Householder matrices are symmetric and orthogonal. It is easily checked that over an orthonormal basis $(e_{1}, \dots  , e_{n})$, a hyperplane reflection about a hyperplane $H$ orthogonal to a nonzero vector $w$ is represented by the matrix
$$H = I_{n} -2 \frac{WW^{\top}}{\|W\|^{2}} ,$$
where $W$ is the column vector of the coordinates of $w$ over the basis $(e_{1}, \dots  , e_{n})$. Since
$$\cdot$$
$$p_{G}(u) = \frac{(u w)}{\|w\|^{2}} w,$$
the matrix representing $p_{G}$ is
$$\frac{WW^{\top}}{W^{\top}} W  ,$$
and since $p_{H} + p_{G} =$ id, the matrix representing $p_{H}$ is
$$I_{n} - \frac{WW^{\top}}{W^{\top}} W .$$
These formulae can be used to derive a formula for a rotation of $\mathbb{R}^{3}$, given the direction $w$ of its axis of rotation and given the angle $\theta$  of rotation. The following fact is the key to the proof that every isometry can be decomposed as a product of reflections.

> **Proposition 13.2.** Let $E$ be any nontrivial Euclidean space. For any two vectors $u, v \in E$, if $\|u\| = \|v\|$, then there is a hyperplane $H$ such that the reflection $s$ about $H$ maps $u$ to $v$, and if $u \neq  v$, then this reflection is unique. See Figure 13.3.

*Proof.* If $u = v$, then any hyperplane containing $u$ does the job. Otherwise, we must have $H = {v$ - $u}^{\perp}$, and by the above formula,
$$-$$
$$2  \cdot  - \|\|^{2} \cdot$$
$$s(u) = u - \frac{(u (vu))}{\|(v -u)\|^{2}} (v -u) = u + \frac{2u2u v}{\|(v -u)\|^{2}} (v -u),$$
and since
$$\|(v -u)\|^{2}= \|u\|^{2}+ \|v\|^{2}-2u \cdot  v$$
and $\|u\| = \|v\|$, we have
$$\|(v -u)\|^{2}= 2\|u\|^{2}-2u \cdot  v,$$
and thus, s(u) $= v$.  If $E$ is a complex vector space and the inner product is Hermitian, Proposition 13.2
$$is false. The problem is that the vector v -u does not work unless the inner product$$
$u\cdot v$ is real! The proposition can be salvaged enough to yield the QR-decomposition in terms of Householder transformations; see Section 14.5. We now show that hyperplane reflections can be used to obtain another proof of the QR-decomposition.
