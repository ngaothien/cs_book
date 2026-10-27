# Orthogonality and Duality in Euclidean Spaces


<!-- PAGE 462 -->
is a little tricky. The strategy is to prove the identity for $\lambda  \in \mathbb{Z}$, then to promote it to $\mathbb{Q}$, and then to $\mathbb{R}$ by continuity. Since
$$-\|-$$
$$\langle -u, v\rangle = \frac{1}{4} (\|-u + v\|^{2}u -v\|^{2})$$
$$-\|$$
$$= \frac{1}{4} (\|u -v\|^{2}u + v\|^{2})$$
$$= -\langle u, v\rangle ,$$
the property holds for $\lambda  = -1$. By linearity and by induction, for any $n \in \mathbb{N}$ with $n \ge 1$, writing $n = n$ - $1 + 1$, we get
$$\langle \lambda x, y\rangle = \lambda \langle x, y\rangle for all \lambda  \in \mathbb{N},$$
and since the above also holds for $\lambda  = -1$, it holds for all $\lambda  \in \mathbb{Z}$. For $\lambda  = p/q$ with $p, q \in \mathbb{Z}$ and $q \neq  0$, we have
$$q\langle (p/q)u, v\rangle = \langle pu, v\rangle = p\langle u, v\rangle ,$$
which shows that
$$\langle (p/q)u, v\rangle = (p/q)\langle u, v\rangle ,$$
and thus
$$\langle \lambda x, y\rangle = \lambda \langle x, y\rangle for all \lambda  \in \mathbb{Q}.$$
To finish the proof, we use the fact that a norm is a continuous map $x \mapsto \|x\|$. Then, the continuous function $t \mapsto^{1} \langle$ tu, $v\rangle$ defined on $\mathbb{R} -{0}$ agrees with $\langle u, v\rangle$ on $\mathbb{Q} -{0}$, so it is equal to $\langle u, v\rangle$ on $\mathbb{R} -{0^{t}}$. The case $\lambda  = 0$ is trivial, so we are done. We now define orthogonality.

## 12.2 Orthogonality and Duality in Euclidean Spaces

An inner product on a vector space gives the ability to define the notion of orthogonality. Families of nonnull pairwise orthogonal vectors must be linearly independent. They are called orthogonal families. In a vector space of finite dimension it is always possible to find orthogonal bases. This is very useful theoretically and practically. Indeed, in an orthogonal basis, finding the coordinates of a vector is very cheap: It takes an inner product. Fourier series make crucial use of this fact. When $E$ has finite dimension, we prove that the inner product on $E$ induces a natural isomorphism between $E$ and its dual space $E^{*}$. This allows us to define the adjoint of a linear map in an intrinsic fashion (i.e., independently of bases). It is also possible to orthonormalize any basis (certainly when the dimension is finite). We give two proofs, one using duality, the other more constructive using the Gram–Schmidt orthonormalization procedure.

<!-- PAGE 463 -->

> **Definition 12.2.** Given a Euclidean space $E$, any two vectors $u, v \in E$ are orthogonal, or perpendicular, if $u \cdot  v = 0$. Given a family $(u_{i})_{i\in I}$ of vectors in $E$, we say that $(u_{i})_{i\in I}$ is orthogonal if $u_{i} \cdot  u_{j} = 0$ for all $i, j \in$ I, where i̸ $= j$. We say that the family $(u_{i})_{i\in I}$ is orthonormal if $u_{i} \cdot  u_{j} = 0$ for all $i, j \in$ I, where $i \neq  j$, and $\|u_{i}\| = u_{i} \cdot  u_{i} = 1$, for all $i \in$ I. For any subset $F$ of $E$, the set
$$F^{\perp} = {v \in E | u \cdot  v = 0, for all u \in F},$$
of all vectors orthogonal to all vectors in $F$, is called the orthogonal complement of $F$. Since inner products are positive definite, observe that for any vector $u \in E$, we have
$$u \cdot  v = 0for all v \in Eiffu = 0.$$
It is immediately verified that the orthogonal complement $F^{\perp}$ of $F$ is a subspace of $E$.

> **Example 12.5.** Going back to Example 12.3 and to the inner product
$$\langle f, g\rangle = \int_{-}^{}  \pi f(t)g(t)dt$$
$$\pi$$
on the vector space $\mathcal{C}[-\pi , \pi$ ], it is easily checked that
$$\pi if p = q, p, q \ge 1,$$
$$\langle \sin px, \sin qx\rangle =$$
$$0if p \neq  q, p, q \ge 1,$$
$$\pi if p = q, p, q \ge 1,$$
$$\langle \cos px, \cos qx\rangle =$$
$$0if p \neq  q, p, q \ge 0,$$
and
$$\langle \sin px, \cos qx\rangle = 0,$$
$$for all p \ge 1 and q \ge 0, and of course, \langle 1, 1\rangle =_{\pi}^{\pi} \int_{-}  dx = 2\pi .$$
As a consequence, the family (sin $px)_{p\ge1}\cup$ (cos $qx)_{q\ge0}$ is orthogonal. It is not orthonormal,
$$\sqrt\sqrt$$
but becomes so if we divide every trigonometric function by $\overline{\pi}$, and $1$ by $\overline{2}\overline{\pi}$.

> **Proposition 12.4.** Given a Euclidean space $E$, for any family $(u_{i})_{i\in I}$ of nonnull vectors in $E$, if $(u_{i})_{i\in I}$ is orthogonal, then it is linearly independent.

*Proof.* Assume there is a linear dependence
$$\sum_{j\in J}  \lambda_{j} u_{j} = 0$$

<!-- PAGE 464 -->
for some $\lambda_{j}  \in \mathbb{R}$ and some finite subset $J$ of I. By taking the inner product with $u_{i}$ for any $i \in J$, and using the the bilinearity of the inner product and the fact that $u_{i} \cdot  u_{j} = 0$ whenever $i \neq  j$, we get
$$0 = u_{i} \cdot  0 = u_{i} \cdot \sum_{j\in J}  \lambda_{j} u_{j}!$$
$$= \sum_{j\in J}  \lambda_{j} (u_{i} \cdot  u_{j}) = \lambda_{i} (u_{i} \cdot  u_{i}),$$
so
$$\lambda_{i} (u_{i} \cdot  u_{i}) = 0,for all i \in J,$$
and since $u_{i} \neq  0$ and an inner product is positive definite, $u_{i} \cdot  u_{i} \neq  0$, so we obtain
$$\lambda_{i}  = 0,for all i \in J,$$
which shows that the family $(u_{i})_{i\in I}$ is linearly independent. We leave the following simple result as an exercise.

> **Proposition 12.5.** Given a Euclidean space $E$, any two vectors $u, v \in E$ are orthogonal iff
$$\|u + v\|^{2}= \|u\|^{2}+ \|v\|^{2}.$$
See Figure 12.2 for a geometrical interpretation.
$$v$$
$$v$$
$$u +$$
$$u$$

![Figure 12.2](../../assets/ch12/fig_12_2.png)

**Figure 12.2:** The sum of the lengths of the two sides of a right triangle is equal to the length of the hypotenuse; i.e. the Pythagorean theorem. One of the most useful features of orthonormal bases is that they afford a very simple method for computing the coordinates of a vector over any basis vector. Indeed, assume that $(e_{1}, \dots  , e_{m})$ is an orthonormal basis. For any vector
$$x = x_{1}e_{1} + \cdots  + x_{m}e_{m},$$

<!-- PAGE 465 -->
if we compute the inner product $x \cdot  e_{i}$, we get
$$x \cdot  e_{i} = x_{1}e_{1} \cdot  e_{i} + \cdots  + x_{i}e_{i} \cdot  e_{i} + \cdots  + x_{m}e_{m} \cdot  e_{i} = x_{i},$$
since
$$1if i = j,$$
$$e_{i} \cdot  e_{j} =$$
$$0if i \neq  j$$
is the property characterizing an orthonormal family. Thus,
$$x_{i} = x \cdot  e_{i},$$
which means that $x_{i}e_{i} = (x \cdot  e_{i})e_{i}$ is the orthogonal projection of $x$ onto the subspace generated by the basis vector $e_{i}$. See Figure 12.3. If the basis is orthogonal but not necessarily
$$x$$
$$\Theta$$
$$\overline{x e}$$
$$\overline{e}$$
$$ii i$$

![Figure 12.3](../../assets/ch12/fig_12_3.png)

**Figure 12.3:** The orthogonal projection of the red vector $x$ onto the black basis vector $e_{i}$ is the maroon vector $x_{i}e_{i}$. Observe that $x \cdot  e_{i} = \|x\|cos \theta$ . orthonormal, then
$$\cdot   \cdot$$
$$x_{i} = \frac{x e_{i}}{e_{i} \cdot  e_{i}} = \frac{x e_{i}}{\|e_{i}\|^{2}} .$$
All this is true even for an infinite orthonormal (or orthogonal) basis $(e_{i})_{i\in I}$.  However, remember that every vector $x$ is expressed as a linear combination
$$x = \sum_{i\in I}  x_{i}e_{i}$$
where the family of scalars $(x_{i})_{i\in I}$ has finite support, which means that $x_{i} = 0$ for all $i \in$ I - $J$, where $J$ is a finite set. Thus, even though the family (sin $px)_{p\ge1} \cup$ (cos $qx)_{q\ge0}$ is orthogonal (it is not orthonormal, but becomes so if we divide every trigonometric function by $\sqrt \sqrt \overline{\pi}$, and $1$ by $\overline{2}\overline{\pi}$; we won’t because it looks messy!), the fact that a function $f \in C^{0}[-\pi , \pi$ ] can be written as a Fourier series as
$$f(x) = a_{0} + \sum_{k=1}^{\infty}  (a_{k} \cos kx + b_{k} \sin kx)$$

<!-- PAGE 466 -->
does not mean that (sin $px)_{p\ge1} \cup$ (cos $qx)_{q\ge0}$ is a basis of this vector space of functions, because in general, the families $(a_{k})$ and $(b_{k})$ do not have finite support! In order for this infinite linear combination to make sense, it is necessary to prove that the partial sums
$$a_{0} + \sum_{k=1}^{n}  (a_{k} \cos kx + b_{k} \sin kx)$$
of the series converge to a limit when $n$ goes to infinity. This requires a topology on the space. A very important property of Euclidean spaces of finite dimension is that the inner product induces a canonical bijection (i.e., independent of the choice of bases) between the vector space $E$ and its dual $E^{*}$. The reason is that an inner product $\cdot$ : $E \times  E \to \mathbb{R}$ defines a nondegenerate pairing, as defined in Definition 11.4. Indeed, if $u \cdot  v = 0$ for all $v \in E$ then $u = 0$, and similarly if $u \cdot  v = 0$ for all $u \in E$ then $v = 0$ (since an inner product is positive definite and symmetric). By Proposition 11.6, there is a canonical isomorphism between $E$ and $E^{*}$. We feel that the reader will appreciate if we exhibit this mapping explicitly and reprove that it is an isomorphism. The mapping from $E$ to $E^{*}$ is defined as follows.

> **Definition 12.3.** For any vector $u \in E$, let $\phi_{u}$  : $E \to \mathbb{R}$ be the map defined such that
$$\phi_{u} (v) = u \cdot  v,for all v \in E.$$
Since the inner product is bilinear, the map $\phi_{u}$  is a linear form in $E^{*}$. Thus, we have a map $\flat$ : $E \to E^{*}$, defined such that
$$\flat (u) = \phi_{u} .$$

> **Theorem 12.6.** Given a Euclidean space $E$, the map $\flat$ : $E \to E^{*}$ defined such that
$$\flat (u) = \phi_{u}$$
is linear and injective. When $E$ is also of finite dimension, the map $\flat$ : $E \to E^{*}$ is a canonical isomorphism.

*Proof.* That $\flat$ : $E \to E^{*}$ is a linear map follows immediately from the fact that the inner product is bilinear. If $\phi_{u}  = \phi_{v}$ , then $\phi_{u} (w) = \phi_{v} (w)$ for all $w \in E$, which by definition of $\phi_{u}$ means that $u \cdot  w = v \cdot  w$ for all $w \in E$, which by bilinearity is equivalent to
$$(v -u) \cdot  w = 0$$
for all $w \in E$, which implies that $u = v$, since the inner product is positive definite. Thus, $\flat$ : $E \to E^{*}$ is injective. Finally, when $E$ is of finite dimension $n$, we know that $E^{*}$ is also of dimension $n$, and then $\flat$ : $E \to E^{*}$ is bijective.

<!-- PAGE 467 -->
The inverse of the isomorphism $\flat$ : $E \to E^{*}$ is denoted by $\sharp$ : $E^{*} \to E$. As a consequence of Theorem 12.6 we have the following corollary.

> **Corollary 12.7.** If $E$ is a Euclidean space of finite dimension, every linear form $f \in E^{*}$ corresponds to a unique $u \in E$ such that
$$f(v) = u \cdot  v,for every v \in E.$$
In particular, if $f$ is not the zero form, the kernel of $f$, which is a hyperplane $H$, is precisely the set of vectors that are orthogonal to $u$.
Remarks:
$(1)$ The “musical map” $\flat$ : $E \to E^{*}$ is not surjective when $E$ has infinite dimension. The result can be salvaged by restricting our attention to continuous linear maps, and by assuming that the vector space $E$ is a Hilbert space (i.e., $E$ is a complete normed vector space w.r.t. the Euclidean norm). This is the famous “little” Riesz theorem (or Riesz representation theorem).
$(2)$ Theorem 12.6 still holds if the inner product on $E$ is replaced by a nondegenerate symmetric bilinear form $\phi$ . We say that a symmetric bilinear form $\phi$ : $E \times  E \to \mathbb{R}$ is nondegenerate if for every $u \in E$,
$$if\phi (u, v) = 0for all v \in E,thenu = 0.$$
$$\mathbb{R}^{4}$$
For example, the symmetric bilinear form on (the Lorentz form) defined such that
$$\phi ((x_{1}, x_{2}, x_{3}, x_{4}), (y_{1}, y_{2}, y_{3}, y_{4})) = x_{1}y_{1} + x_{2}y_{2} + x_{3}y_{3} -x_{4}y_{4}$$
$$\mathbb{R}^{4}$$
is nondegenerate. However, there are nonnull vectors $u \in$ such that $\phi (u, u) = 0$, which is impossible in a Euclidean space. Such vectors are called isotropic.
$$\mathbb{R}^{n}$$

> **Example 12.6.** Consider with its usual Euclidean inner product. Given any differentiable function $f$ : $U \to \mathbb{R}$, where $U$ is some open subset of $\mathbb{R}^{n}$, by definition, for any $x \in U$, the total derivative $df_{x}$ of $f$ at $x$ is the linear form defined so that for all $u = (u_{1}, \dots  , u_{n}) \in \mathbb{R}^{n}$,
$$df_{x}(u) = \begin{pmatrix} \partial f \\ \partial f \\ (x) & \cdots & (x) \\ \partial x_{1} & \partial x_{n} \end{pmatrix} \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} = \sum_{i=1}^{n}  \frac{\partial f}{\partial x_{i}} (x) u_{i}.$$
$$\mathbb{R}^{n}$$
The unique vector $v \in$ such that
$$v \cdot  u = df_{x}(u)for all u \in \mathbb{R}^{n}$$

<!-- PAGE 468 -->
is the transpose of the Jacobian matrix of $f$ at $x$, the $1 \times  n$ matrix
$$\begin{pmatrix} \partial f \\ \partial f \\ (x) & \cdots & (x) \\ \partial x_{1} & \partial x_{n} \end{pmatrix} .$$
This is the gradient $grad(f)_{x}$ of $f$ at $x$, given by
$$grad(f)_{x} = \begin{pmatrix} \partial f \\ (x) \\ \partial x_{1} \\ \vdots \\ \partial f \\ (x) \\ \partial x_{n} \end{pmatrix} .$$

> **Example 12.7.** Given any two vectors $u, v \in \mathbb{R}^{3}$, let c(u, $v)$ be the linear form given by
$$c(u, v)(w) = \det(u, v, w)for all w \in \mathbb{R}^{3}.$$
Since
$$u_{1}v_{1}w_{1}$$
$$u_{2}v_{2}



$u_{1}v_{1}$



$u_{1}v_{1}$$$
$$\det(u, v, w) =u_{2}v_{2}w_{2}= w_{1} -w_{2} + w_{3}$$
$$u_{3}v_{3}u_{3}v_{3}u_{2}v_{2}$$
$$u_{3}v_{3}w_{3}$$
$$= w_{1}(u_{2}v_{3} -u_{3}v_{2}) + w_{2}(u_{3}v_{1} -u_{1}v_{3}) + w_{3}(u_{1}v_{2} -u_{2}v_{1}),$$
$$\mathbb{R}^{3}$$
we see that the unique vector $z \in$ such that
$$z \cdot  w = c(u, v)(w) = \det(u, v, w)for all w \in \mathbb{R}^{3}$$
is the vector
$$z = \begin{pmatrix} u_{2}v_{3} -u_{3}v_{2} \\ u_{3}v_{1} -u_{1}v_{3} \\ u_{1}v_{2} & u_{2}v_{1} \end{pmatrix} .$$
$$-$$
This is just the cross-product $u \times  v$ of $u$ and $v$. Since det(u, $v, u) =$ det(u, $v, v) = 0$, we see that $u\times v$ is orthogonal to both $u$ and $v$. The above allows us to generalize the cross-product to $\mathbb{R}^{n}$. Given any $n$ - $1$ vectors $u_{1}, \dots  , u_{n-1} \in \mathbb{R}^{n}$, the cross-product $u_{1} \times  \cdots  \times  u_{n-1}$ is the
$$\mathbb{R}^{n}$$
unique vector in such that
$$(u_{1} \times  \cdots  \times  u_{n-1}) \cdot  w = \det(u_{1}, \dots  , u_{n-1}, w)for all w \in \mathbb{R}^{n}.$$

> **Example 12.8.** Consider the vector space $M_{n}(\mathbb{R})$ of real $n \times  n$ matrices with the inner product
$$\langle A, B\rangle = \mathrm{tr}(A^{\top}B).$$
Let $s: M_{n}(\mathbb{R}) \to \mathbb{R}$ be the function given by
$$s(A) = \sum_{i,j=1}^{n}  a_{ij},$$
