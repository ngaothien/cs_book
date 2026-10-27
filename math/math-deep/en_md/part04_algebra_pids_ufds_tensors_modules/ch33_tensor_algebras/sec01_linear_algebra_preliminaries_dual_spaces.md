# Linear Algebra Preliminaries: Dual Spaces and Pairings


<!-- PAGE 1168 -->

## 33.1 Linear Algebra Preliminaries: Dual Spaces and

$$Pairings$$
We assume that we are dealing with vector spaces over a field $K$. As usual the dual space $E^{*}$ of a vector space $E$ is defined by $E^{*} =$ Hom(E, $K)$. The dual space $E^{*}$ is the vector space consisting of all linear maps $\omega$ : $E \to K$ with values in the field $K$. A problem that comes up often is to decide when a space $E$ is isomorphic to the dual $F^{*}$ of some other space $F$ (possibly equal to $E)$. The notion of pairing due to Pontrjagin provides a very clean criterion.

> **Definition 33.1.** Given two vector spaces $E$ and $F$ over a field $K$, a map $\langle$ -, $-\rangle$ : $E\times F \to K$ is a nondegenerate pairing iff it is bilinear and iff $\langle u, v\rangle = 0$ for all $v \in F$ implies $u = 0$, and $\langle u, v\rangle = 0$ for all $u \in E$ implies $v = 0$. A nondegenerate pairing induces two linear maps $\phi$ : $E \to F^{*}$ and $\psi$ : $F \to E^{*}$ defined such that for all for all $u \in E$ and all $v \in F, \phi (u)$ is the linear form in $F^{*}$ and $\psi (v)$ is the linear form in $E^{*}$ given by
$$\phi (u)(y) = \langle u, y\rangle for all y \in F$$
$$\psi (v)(x) = \langle x, v\rangle for all x \in E.$$
Schematically, $\phi (u) = \langle u, -\rangle$ and $\psi (v) = \langle$ -, $v\rangle$ .

> **Proposition 33.1.** For every nondegenerate pairing $\langle$ -, $-\rangle$ : $E \times F \to K$, the induced maps $\phi$ : $E \to F^{*}$ and $\psi$ : $F \to E^{*}$ are linear and injective. Furthermore, if $E$ and $F$ are finite dimensional, then $\phi$ : $E \to F^{*}$ and $\psi$ : $F \to E^{*}$ are bijective.

*Proof.* The maps $\phi$ : $E \to F^{*}$ and $\psi$ : $F \to E^{*}$ are linear because $u, v \mapsto \langle u, v\rangle$ is bilinear. Assume that $\phi (u) = 0$. This means that $\phi$ (u)(y) $= \langle u, y\rangle = 0$ for all $y \in F$, and as our pairing is nondegenerate, we must have $u = 0$. Similarly, $\psi$  is injective. If $E$ and $F$ are finite dimensional, then dim(E) $= dim(E^{*})$ and dim(F) $= dim(F^{*}$ ). However, the injectivity of $\phi$ and $\psi$  implies that that dim(E) $\le dim(F^{*}$ ) and dim(F) $\le dim(E^{*})$. Consequently dim(E) $\le$ dim(F) and dim(F) $\le$ dim(E), so dim(E) $=$ dim(F). Therefore, dim(E) $= dim(F^{*}$ ) and $\phi$ is bijective (and similarly dim(F) $= dim(E^{*})$ and $\psi$  is bijective). Proposition 33.1 shows that when $E$ and $F$ are finite dimensional, a nondegenerate pairing induces canonical isomorphisms $\phi$ : $E \to F^{*}$ and $\psi$ : $F \to E^{*}$; that is, isomorphisms that do not depend on the choice of bases. An important special case is the case where $E = F$ and we have an inner product (a symmetric, positive definite bilinear form) on $E$.
Remark: When we use the term “canonical isomorphism,” we mean that such an isomorphism is defined independently of any choice of bases. For example, if $E$ is a finite dimensional vector space and $(e_{1}, \dots  , e_{n})$ is any basis of $E$, we have the dual basis $(e_{1}^{*}, \dots  , e_{n}^{*})$ of $E^{*}$ (where, $e_{i}^{*} (e_{j}) = \delta_{i j}$ ), and thus the map $e_{i} \mapsto e_{i}^{*}$ is an isomorphism between $E$ and $E^{*}$. This isomorphism is not canonical.

<!-- PAGE 1169 -->
On the other hand, there are two important cases where we have canonical isomorphisms for a vector space $E$ of finite dimension.
$(1)$ The pairing $\langle$ -, $-\rangle$ : $E^{*} \times  E \to K$ given by
$$\langle \omega , u\rangle = \omega (u),\omega  \in E^{*}, u \in E,$$
namely evaluation at $u$. This pairing induces the isomorphism $\psi$ : $E \to E^{**}$ given by
$$\psi (u)(\omega ) = \langle \omega , u\rangle = \omega (u),\omega  \in E^{*}, u \in E.$$

> **Definition 33.2.** The bilinear map eval: $E^{*}\times E \to K$, also denoted $\delta_{1}^{1}$  : $E^{*}\times E \to K$, given by
$$eval(\omega , u) = \delta_{1}^{1} (\omega , u) = \omega (u),\omega  \in E^{*}, u \in E,$$
is the evaluation map or Kronecker delta, and for every $u \in E$, the linear form $eval_{u} \in E^{**}$ is given by
$$eval_{u}(\omega ) = eval(\omega , u) = \omega (u),\omega  \in E^{*}.(eval)$$
Thus, we see that that the isomorphism $\psi$ : $E \to E^{**}$ is given by
$$\psi (u) = eval_{u},u \in E.$$
$(2)$ If $\langle$ -, $-\rangle$ is an inner product on a real vector space $E$, then Proposition 33.1 shows that the nondegenerate pairing $\langle$ -, $-\rangle$ on $E\times E$ induces a canonical isomorphism between $E$ and $E^{*}$. This isomorphism is often denoted $\flat$ : $E \to E^{*}$, and we usually write $u^{\flat}$ for $\flat (u)$, with $u \in E$. Schematically, $u^{\flat} = \langle u, -\rangle$ . The inverse of $\flat$ is denoted $\sharp$ : $E^{*} \to E$, and given any linear form $\omega  \in E^{*}$, we usually write $\omega^{\sharp}$ for $\sharp (\omega$ ). Schematically, $\omega  = \langle \omega^{\sharp} , -\rangle$ . Given any basis, $(e_{1}, \dots  , e_{n})$ of $E$ (not necessarily orthonormal), let $(g_{ij})$ be the $n \times$  n- matrix given by $g_{ij} = \langle e_{i}, e_{j}\rangle$ (the Gram matrix of the inner product). Recall that the dual basis $(e_{1}^{*}, \dots  , e_{n}^{*})$ of $E^{*}$ consists of the coordinate forms $e_{i}^{*} \in E^{*}$, which are characterized by the following properties:
$$e_{i}^{*} (e_{j}) = \delta_{ij} ,1 \le i, j \le n.$$
The inverse of the Gram matrix $(g_{ij})$ is often denoted by $(g^{ij})$ (by raising the indices). The tradition of raising and lowering indices is pervasive in the literature on tensors. It is indeed useful to have some notational convention to distinguish between vectors and linear forms (also called one-forms or covectors). The usual convention is that coordinates
$$of vectors are written using superscripts, as in u = \sum_{i}  n=1 u^{i}e_{i}, and coordinates of one-forms$$
$$are written using subscripts, as in \omega  = \sum_{i}  n=1 \omega_{i} e_{i}^{*} . Actually, since vectors are indexed with$$
subscripts, one-forms are indexed with superscripts, so $e_{i}^{*}$ should be written as $e^{i}$. The motivation is that summation signs can then be omitted, according to the Einstein summation convention. According to this convention, whenever a summation variable (such

<!-- PAGE 1170 -->
as $i)$ appears both as a subscript and a superscript in an expression, it is assumed that it is
$$involved in a summation. For example the sum \sum_{i}  n=1 u^{i}e_{i} is abbreviated as$$
$$u^{i}e_{i},$$
$$n$$
$$and the sum \sum_{i}  =1 \omega_{i} e^{i}is abbreviated as$$
$$\omega_{i} e^{i}.$$
In this text we will typically only use the Einstein summation convention for tensors. The maps $\flat$ and $\sharp$ can be described explicitly in terms of the Gram matrix of the inner product and its inverse.

> **Proposition 33.2.** For any real vector space $E$, given a basis $(e_{1}, \dots  , e_{n})$ for $E$ and its dual basis $(e_{1}^{*}, \dots  , e_{n}^{*})$ for $E^{*}$, for any inner product $\langle$ -, $-\rangle$ on $E$, if $(g$ ) is its Gram matrix, with
$$g_{ij} = \langle e_{i}, e_{j}\rangle , and (g^{ij}) is its inverse, then for every vector u = \sum_{j}^{ij}  n=1 u^{j}e_{j} \in E and every$$
$$one-form \omega  = \sum_{i}  n=1 \omega_{i} e_{i}^{*} \in E^{*}, we have$$
$$u^{\flat}= \sum_{i=1}^{n}  (u^{\flat})_{i}e_{i}^{*} ,with(u^{\flat})_{i} = \sum_{j=1}^{n}  g_{ij}u^{j},$$
and
$$\omega^{\sharp} = \sum_{i=1}^{n}  (\omega^{\sharp} )^{i}e_{i},with(\omega^{\sharp} )^{i}= \sum_{j=1}^{n}  g^{ij}\omega_{j} .$$
$$Proof. For every u = \sum_{j}  n=1 u^{j}e_{j}, since u^{\flat}(v) = \langle u, v\rangle for all v \in E and the Gram matrix is$$
symmetric, we have
$$u^{\flat}(e_{i}) = \langle u, e_{i}\rangle = \sum_{j=1}^{n}  u^{j}e_{j}, e_{i}= \sum_{j=1}^{n}  u^{j}\langle e_{j}, e_{i}\rangle = \sum_{j=1}^{n}  g_{ij}u^{j},$$
so we get
$$u^{\flat}= \sum_{i=1}^{n}  (u^{\flat})_{i}e_{i}^{*} ,with(u^{\flat})_{i} = \sum_{j=1}^{n}  g_{ij}u^{j}.$$
$$If we write \omega  \in E^{*}as \omega  = \sum_{i}  n=1 \omega_{i} e_{i}^{*} and \omega^{\sharp} \in E as \omega^{\sharp} = \sum_{\sharp}  nj=1(\omega^{\sharp} )^{j}e_{j}, since$$
$$\omega_{i}  = \omega (e_{i}) = \langle \omega^{\sharp} , e_{i}\rangle = \sum_{j=1}^{n}  (\omega^{\sharp} )^{j}g_{ij} = \sum_{j=1}^{n}  g_{ij}(\omega )^{j},1 \le i \le n,$$
we get
$$(\omega^{\sharp} )^{i} = \sum_{j=1}^{n}  g^{ij}\omega_{j} ,$$
where $(g^{ij})$ is the inverse of the matrix $(g_{ij})$.

<!-- PAGE 1171 -->
In the special case where $(e_{1}, \dots  , e_{n})$ is an orthonormal basis, the Gram matrix is the identity matrix, thus $(u^{\flat})_{i} = u^{i}$ and $(\omega^{\sharp} )^{i} = \omega_{i}$ , so the map $\flat$ has the effect of lowering (flattening!) indices, and the map $\sharp$ has the effect of raising (sharpening!) indices. Here is an explicit example of Proposition 33.2. Let $(e_{1}, e_{2})$ be a basis of $E$ such that
$$\langle e_{1}, e_{1}\rangle = 1,\langle e_{1}, e_{2}\rangle = 2,\langle e_{2}, e_{2}\rangle = 5.$$
Then
$$g = \begin{pmatrix} 1 & 2 \\ 2 & 5 \end{pmatrix} ,g^{-1}= \begin{pmatrix} 5 & -2 \\ -2 & 1 \end{pmatrix} .$$
Set $u = u^{1}e_{1} + u^{2}e_{2}$ and observe that
$$u^{\flat}(e_{1}) = \langle u^{1}e_{1} + u^{2}e_{2}, e_{1}\rangle = \langle e_{1}, e_{1}\rangle u^{1}+ \langle e_{2}, e_{1}\rangle u^{2}= g_{11}u^{1}+ g_{12}u^{2}= u^{1}+ 2u^{2}$$
$$u^{\flat}(e_{2}) = \langle u^{1}e_{1} + u^{2}e_{2}, e_{2}\rangle = \langle e_{1}, e_{2}\rangle u^{1}+ \langle e_{2}, e_{2}\rangle u^{2}= g_{21}u^{1}+ g_{22}u^{2}= 2u^{1}+ 5u^{2},$$
which in turn implies that
$$+ 2 + 5$$
$$u^{\flat}= u^{\flat}(e_{1})e_{1}^{*} + u^{\flat}(e_{2})e_{2}^{*} = (u^{1}u^{2})e_{1}^{*} + (2u^{1}u^{2})e_{2}^{*}.$$
Given $\omega  = \omega_{1} e_{1}^{*} + \omega_{2} e_{2}^{*}$, we calculate $\omega^{\sharp} = (\omega^{\sharp} )^{1}e_{1} + (\omega^{\sharp} )^{2}e_{2}$ from the following two linear equalities:
$$\omega_{1}  = \omega (e_{1}) = \langle \omega^{\sharp} , e_{1}\rangle = \langle (\omega^{\sharp} )^{1}e_{1} + (\omega^{\sharp} )^{2}e_{2}, e_{1}\rangle$$
$$= \langle e_{1}, e_{1}\rangle (\omega^{\sharp} )^{1}+ \langle e_{2}, e_{1}\rangle (\omega^{\sharp} )^{2}= (\omega^{\sharp} )^{1}+ 2(\omega^{\sharp} )^{2}= g_{11}(\omega^{\sharp} )^{1}+ g_{12}(\omega^{\sharp} )^{2}$$
$$\omega_{2}  = \omega (e_{2}) = \langle \omega^{\sharp} , e_{2}\rangle = \langle (\omega^{\sharp} )^{1}e_{1} + (\omega^{\sharp} )^{2}e_{2}, e_{2}\rangle$$
$$= \langle e_{1}, e_{2}\rangle (\omega^{\sharp} )^{1}+ \langle e_{2}, e_{2}\rangle (\omega^{\sharp} )^{2}= 2(\omega^{\sharp} )^{1}+ 5(\omega^{\sharp} )^{2}= g_{21}(\omega^{\sharp} )^{1}+ g_{22}(\omega^{\sharp} )^{2}.$$
These equalities are concisely written as
$$\begin{pmatrix} \omega_{1} \\ \omega_{2} \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 2 & 5 \end{pmatrix} \begin{pmatrix} (\omega^{\sharp} )^{1} \\ (\omega^{\sharp} )^{2} \end{pmatrix} = g \begin{pmatrix} (\omega^{\sharp} )^{1} \\ (\omega^{\sharp} )^{2} \end{pmatrix} .$$
Then
$$\begin{pmatrix} (\omega^{\sharp} )^{1} \\ (\omega^{\sharp} )^{2} \end{pmatrix} = g^{-1} \begin{pmatrix} \omega_{1} \\ \omega_{2} \end{pmatrix} = \begin{pmatrix} 5 & -2 \\ -2 & 1 \end{pmatrix} \begin{pmatrix} \omega_{1} \\ \omega_{2} \end{pmatrix} ,$$
which in turn implies
$$(\omega^{\sharp} )^{1}= 5\omega_{1}  -2\omega_{2} ,(\omega^{\sharp} )^{2}= -2\omega_{1}  + \omega_{2} ,$$
i.e.
$$\omega^{\sharp} = (5\omega_{1}  -2\omega_{2} )e_{1} + (-2\omega_{1}  + \omega_{2} )e_{2}.$$

<!-- PAGE 1172 -->
The inner product $\langle$ -, $-\rangle$ on $E$ induces an inner product on $E^{*}$ denoted $\langle$ -, $-\rangle_{E*}$ , and given by
$$\langle \omega_{1} , \omega_{2} \rangle_{E*} = \langle \omega_{1}^{\sharp} , \omega_{2}^{\sharp} \rangle ,for all \omega_{1} , \omega_{2}  \in E^{*}.$$
Then we have
$$\langle u^{\flat}, v^{\flat}\rangle_{E*} = \langle (u^{\flat})^{\sharp}, (v^{\flat})^{\sharp}\rangle = \langle u, v\rangle for allu, v \in E.$$
If $(e_{1}, \dots  , e_{n})$ is a basis of $E$ and $g_{ij} = \langle e_{i}, e_{j}\rangle$ , as
$$(e_{i}^{*} )^{\sharp}= \sum_{k=1}^{n}  g^{ik}e_{k},$$
an easy computation shows that
$$\langle e_{i}^{*} , e_{j}^{*}\rangle_{E*} = \langle (e_{i}^{*} )^{\sharp}, (e_{j}^{*})^{\sharp}\rangle = g^{ji}= g^{ij};$$
that is, in the basis $(e_{1}^{*}, \dots  , e_{n}^{*})$, the inner product on $E^{*}$ is represented by the matrix $(g^{ij})$, the inverse of the matrix $(g_{ij})$. The inner product on a finite dimensional real vector space also yields a canonical isomorphism between the space Hom(E, $E;\mathbb{R})$ of bilinear forms on $E$, and the space Hom(E, $E)$ of linear maps from $E$ to itself. Using this isomorphism, we can define the trace of a bilinear form in an intrinsic manner. This technique is used in differential geometry, for example, to define the divergence of a differential one-form.

> **Proposition 33.3.** If $\langle$ -, $-\rangle$ is an inner product on a finite dimensional real vector space $E$, then for every bilinear form $f$ : $E \times  E \to \mathbb{R}$, there is a unique linear map $f^{\natural}$ : $E \to E$ such that
$$f(u, v) = \langle f^{\natural} (u), v\rangle ,for all u, v \in E.$$
The map $f \mapsto f^{\natural}$ is a linear isomorphism between Hom(E, $E; K)$ and Hom(E, $E)$. Furthermore, for any basis $(e_{1}, \dots  , e_{n})$ of $E$, if $A = (f(e_{i}, e_{j}))$ is the matrix representing $f, G = (g_{ij} = \langle e_{i}, e_{j}\rangle$ ) the symmetric Gram matrix representing the inner product $\langle$ -, $-\rangle$ , and $B = (b_{ij})$ the matrix representing $f^{\natural}$ , then
$$B = G^{-1}A^{\top}.$$

*Proof.* For every $g \in$ Hom(E, $E)$, the map given by
$$f(u, v) = \langle g(u), v\rangle ,u, v \in E,$$
is clearly bilinear. It is also clear that the above defines a linear map from Hom(E, $E)$ to Hom(E, $E; K)$. This map is injective, because if f(u, $v) = 0$ for all $u, v \in E$, as $\langle$ -, $-\rangle$ is an inner product, we get g(u) $= 0$ for all $u \in E$. Furthermore, both spaces Hom(E, $E)$ and Hom(E, $E; K)$ have the same dimension, so our linear map is an isomorphism.

<!-- PAGE 1173 -->
Since the jth column of $B$ determines $f^{\natural} (e_{j})$ by
$$f^{\natural} (e_{j}) = \sum_{k=1}^{n}  b_{kj}e_{k},$$
using the fact that the Gram matrix $G$ is symmetric, we have
$$*+$$
$$a_{ji} = f(e_{j}, e_{i}) =f^{\natural} (e_{j}), e_{i}= \sum_{k=1}^{n}  b_{kj}e_{k}, e_{i}$$
$$= \sum_{k=1}^{n}  b_{kj}\langle e_{k}, e_{i}\rangle = \sum_{k=1}^{n}  b_{kj}g_{ki} = \sum_{k=1}^{n}  g_{ik}b_{kj}.$$
The equations
$$a_{ji} = \sum_{k=1}^{n}  g_{ik}b_{kj}$$
are equivalent to $GB = A^{\top}$, and so
$$B = G^{-1}A^{\top},$$
as claimed. If $(e_{1}, \dots  , e_{n})$ is an orthonormal basis of $E$, then we check immediately that the trace of a linear map $g$ (which is independent of the choice of a basis) is given by
$$\mathrm{tr}(g) = \sum_{i=1}^{n}  \langle g(e_{i}), e_{i}\rangle ,$$
where $n =$ dim(E).

> **Definition 33.3.** We define the trace of the bilinear form $f$ by
$$\mathrm{tr}(f) = \mathrm{tr}(f^{\natural} ).$$
From Proposition 33.3, tr(f) is given by
$$\mathrm{tr}(f) = \sum_{i=1}^{n}  f(e_{i}, e_{i}),$$
for any orthonormal basis $(e_{1}, \dots  , e_{n})$ of $E$. We can also check directly that the above expression is independent of the choice of an orthonormal basis.
