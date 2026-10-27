# The Orthogonal Group, Orthogonal Matrices


<!-- PAGE 482 -->
(ii) The implication that $(3)$ implies $(1)$ holds if we also assume that $f$ is surjective, even if $E$ has infinite dimension. In $(2)$, when $f$ does not satisfy the condition f(0) $= 0$, the proof shows that $f$ is an affine map. Indeed, taking any vector $\tau$  as an origin, the map $g$ is linear, and
$$f(\tau  + u) = f(\tau ) + g(u)for all u \in E.$$
By Proposition 24.7, this shows that $f$ is affine with associated linear map $g$. This fact is worth recording as the following proposition.

> **Proposition 12.13.** Given any two nontrivial Euclidean spaces $E$ and $F$ of the same finite dimension $n$, for every function $f$ : $E \to F$, if
$$\|f(v) -f(u)\|= \|v -u\|for all u, v \in E,$$
then $f$ is an affine map, and its associated linear map $g$ is an isometry. In view of Proposition 12.12, we usually abbreviate “linear isometry” as “isometry,” unless we wish to emphasize that we are dealing with a map between vector spaces. We are now going to take a closer look at the isometries $f$ : $E \to E$ of a Euclidean space of finite dimension.

## 12.6 The Orthogonal Group, Orthogonal Matrices

In this section we explore some of the basic properties of the orthogonal group and of orthogonal matrices.

> **Proposition 12.14.** Let $E$ be any Euclidean space of finite dimension $n$, and let $f$ : $E \to E$ be any linear map. The following properties hold:
$(1)$ The linear map $f$ : $E \to E$ is an isometry iff
$$f \circ f^{*} = f^{*} \circ f = id.$$
$(2)$ For every orthonormal basis $(e_{1}, \dots  , e_{n})$ of $E$, if the matrix of $f$ is $A$, then the matrix of $f^{*}$ is the transpose $A^{\top}$ of $A$, and $f$ is an isometry iff $A$ satisfies the identities
$$A A^{\top}= A^{\top}A = I_{n},$$
where $I_{n}$ denotes the identity matrix of order $n$, iff the columns of $A$ form an orthonormal basis of $\mathbb{R}^{n}$, iff the rows of $A$ form an orthonormal basis of $\mathbb{R}^{n}$.

<!-- PAGE 483 -->

*Proof.* $(1)$ The linear map $f$ : $E \to E$ is an isometry iff
$$f(u) \cdot  f(v) = u \cdot  v,$$
for all $u, v \in E$, iff
$$f^{*} (f(u)) \cdot  v = f(u) \cdot  f(v) = u \cdot  v$$
for all $u, v \in E$, which implies
$$(f^{*} (f(u)) -u) \cdot  v = 0$$
for all $u, v \in E$. Since the inner product is positive definite, we must have
$$f^{*} (f(u)) -u = 0$$
for all $u \in E$, that is,
$$f^{*} \circ f = id.$$
But an endomorphism $f$ of a finite-dimensional vector space that has a left inverse is an isomorphism, so $f \circ f^{*} =$ id. The converse is established by doing the above steps backward.
$(2)$ If $(e_{1}, \dots  , e_{n})$ is an orthonormal basis for $E$, let $A = (a_{i j})$ be the matrix of $f$, and let $B = (b_{i j})$ be the matrix of $f^{*}$ . Since $f^{*}$ is characterized by
$$f^{*} (u) \cdot  v = u \cdot  f(v)$$
for all $u, v \in E$, using the fact that if $w = w_{1}e_{1} + \cdots  + w_{n}e_{n}$ we have $w_{k} = w \cdot  e_{k}$ for all $k, 1 \le k \le n$, letting $u = e_{i}$ and $v = e_{j}$, we get
$$b_{j i} = f^{*} (e_{i}) \cdot  e_{j} = e_{i} \cdot  f(e_{j}) = a_{i j},$$
for all $i, j, 1 \le i, j \le n$. Thus, $B = A^{\top}$. Now if $X$ and $Y$ are arbitrary matrices over the basis $(e_{1}, \dots  , e_{n})$, denoting as usual the jth column of $X$ by $X^{j}$, and similarly for $Y$ , a simple calculation shows that
$$X^{\top}Y = (X^{i}\cdot  Y^{j})_{1\le i,j\le n}.$$
Then it is immediately verified that if $X = Y = A$, then
$$A^{\top}A = A A^{\top}= I_{n}$$
iff the column vectors $(A^{1}, \dots  , A^{n})$ form an orthonormal basis. Thus, from $(1)$, we see that
$(2)$ is clear (also because the rows of $A$ are the columns of $A^{\top})$. Proposition 12.14 shows that the inverse of an isometry $f$ is its adjoint $f^{*}$ . Recall that the set of all real $n \times  n$ matrices is denoted by $M_{n}(\mathbb{R})$. Proposition 12.14 also motivates the following definition.

> **Definition 12.6.** A real $n \times  n$ matrix is an orthogonal matrix if
$$A A^{\top}= A^{\top}A = I_{n}.$$
