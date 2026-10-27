# Orthogonality, Duality, Adjoint of a Linear Map


<!-- PAGE 538 -->
shows that $\phi$ : $E \times  E \to \mathbb{C}$ is continuous, and thus, that $\|\|$ is continuous. If $\langle E, \phi \rangle$ is only pre-Hilbertian, $\|u\|$ is called a seminorm. In this case, the condition
$$\|u\|= 0impliesu = 0$$
is not necessarily true. However, the Cauchy–Schwarz inequality shows that if $\|u\| = 0$, then $u \cdot  v = 0$ for all $v \in E$.
Remark: As in the case of real vector spaces, a norm on a complex vector space is induced by some positive definite Hermitian product $\langle$ -, $-\rangle$ iff it satisfies the parallelogram law:
$$\|u + v\|^{2}+ \|u -v\|^{2}= 2(\|u\|^{2}+ \|v\|^{2}).$$
This time the Hermitian product is recovered using the polarization identity from Proposition 14.1:
$$4\langle u, v\rangle = \|u + v\|^{2}-\|u -v\|^{2}+ i \|u + iv\|^{2}-i \|u -iv\|^{2}.$$
It is easy to check that $\langle u, u\rangle = \|u\|^{2}$, and
$$\langle v, u\rangle =\overline{\langle}\overline{u, v}\overline{\rangle}$$
$$\langle iu, v\rangle = i\langle u, v\rangle ,$$
so it is enough to check linearity in the variable $u$, and only for real scalars. This is easily done by applying the proof from Section 12.1 to the real and imaginary part of $\langle u, v\rangle$ ; the details are left as an exercise. We will now basically mirror the presentation of Euclidean geometry given in Chapter $12$ rather quickly, leaving out most proofs, except when they need to be seriously amended.

## 14.2 Orthogonality, Duality, Adjoint of a Linear Map

In this section we assume that we are dealing with Hermitian spaces. We denote the Hermitian inner product by $u \cdot  v$ or $\langle u, v\rangle$ . The concepts of orthogonality, orthogonal family of vectors, orthonormal family of vectors, and orthogonal complement of a set of vectors are unchanged from the Euclidean case (Definition 12.2). For example, the set $\mathcal{C}[-\pi , \pi$ ] of continuous functions $f$ : $[-\pi , \pi$ ] $\to \mathbb{C}$ is a Hermitian space under the product
$$\langle f, g\rangle = \int_{-}^{}  \pi f(x)\overline{g}\overline{(}\overline{x}\overline{)} dx,$$
$$\pi$$
and the family $(e^{ikx})_{k\in Z}$ is orthogonal. Propositions 12.4 and 12.5 hold without any changes. It is easy to show that
$$2$$
$$\sum_{i=1}^{n}  u_{i}= \sum_{i=1}^{n}  \|u_{i}\|^{2}+ \sum_{\le i<j\le}  2\mathcal{ℜ}(u_{i} \cdot  u_{j}).$$
$$1n$$

<!-- PAGE 539 -->
Analogously to the case of Euclidean spaces of finite dimension, the Hermitian product induces a canonical bijection (i.e., independent of the choice of bases) between the vector space $E$ and the space $E^{*}$. This is one of the places where conjugation shows up, but in this case, troubles are minor. Given a Hermitian space $E$, for any vector $u \in E$, let $\phi_{u}^{l}$  : $E \to \mathbb{C}$ be the map defined such that
$$\phi_{u}^{l} (v) =\overline{u}\overline{\cdot}\overline{v,} for all v \in E.$$
Similarly, for any vector $v \in E$, let $\phi_{v}^{r}$  : $E \to \mathbb{C}$ be the map defined such that
$$\phi_{v}^{r} (u) = u \cdot  v,for all u \in E.$$
Since the Hermitian product is linear in its first argument $u$, the map $\phi_{v}^{r}$  is a linear form in $E^{*}$, and since it is semilinear in its second argument $v$, the map $\phi_{u}^{l}$  is also a linear form in $E^{*}$. Thus, we have two maps $\flat^{l}$ : $E \to E^{*}$ and $\flat^{r}$ : $E \to E^{*}$, defined such that
$$\flat^{l} (u) = \phi_{u}^{l} ,and\flat^{r} (v) = \phi_{v}^{r} .$$

> **Proposition 14.5.** The equations $\phi_{u}^{l}  = \phi_{u}^{r}$  and $\flat^{l} = \flat^{r}$ hold.

*Proof.* Indeed, for all $u, v \in E$, we have
$$\flat^{l} (u)(v) = \phi_{u}^{l} (v)$$
$$=\overline{u}\overline{\cdot}\overline{v}$$
$$= v \cdot  u$$
$$= \phi_{u}^{r} (v)$$
$$= \flat^{r} (u)(v).$$
Therefore, we use the notation $\phi_{u}$  for both $\phi_{u}^{l}$  and $\phi_{u}^{r}$ , and $\flat$ for both $\flat^{l}$ and $\flat^{r}$ .

> **Theorem 14.6.** Let $E$ be a Hermitian space $E$. The map $\flat$ : $E \to E^{*}$ defined such that
$$\flat (u) = \phi_{u}^{l}  = \phi_{u}^{r} for all u \in E$$
is semilinear and injective. When $E$ is also of finite dimension, the map $\flat$ : $\overline{E} \to E^{*}$ is a canonical isomorphism.

*Proof.* That $\flat$ : $E \to E^{*}$ is a semilinear map follows immediately from the fact that $\flat = \flat^{r}$ , and that the Hermitian product is semilinear in its second argument. If $\phi_{u}  = \phi_{v}$ , then $\phi_{u} (w) = \phi_{v} (w)$ for all $w \in E$, which by definition of $\phi_{u}$  and $\phi_{v}$  means that
$$w \cdot  u = w \cdot  v$$
for all $w \in E$, which by semilinearity on the right is equivalent to
$$w \cdot  (v -u) = 0for all w \in E,$$
which implies that $u = v$, since the Hermitian product is positive definite. Thus, $\flat$ : $E \to E^{*}$
$$is injective. Finally, when E is of finite dimension n, \frac{E^{*}}{E} is also of dimension n, and then$$
$\flat$ : $E \to E^{*}$ is bijective. Since $\flat$ is semilinar, the map $\flat$ :  $\to E^{*}$ is an isomorphism.

<!-- PAGE 540 -->
The inverse of the isomorphism $\flat$ : $\overline{E} \to E^{*}$ is denoted by $\sharp$ : $E^{*} \to \overline{E}$. As a corollary of the isomorphism $\flat$ : $\overline{E} \to E^{*}$ we have the following result.

> **Proposition 14.7.** If $E$ is a Hermitian space of finite dimension, then every linear form $f \in E^{*}$ corresponds to a unique $v \in E$, such that
$$f(u) = u \cdot  v,for every u \in E.$$
In particular, if $f$ is not the zero form, the kernel of $f$, which is a hyperplane $H$, is precisely the set of vectors that are orthogonal to $v$.
Remarks: $1$. The “musical map” $\flat$ : $\overline{E} \to E^{*}$ is not surjective when $E$ has infinite dimension. This result can be salvaged by restricting our attention to continuous linear maps and by assuming that the vector space $E$ is a Hilbert space. $2$. Dirac’s “bra-ket” notation. Dirac invented a notation widely used in quantum mechanics for denoting the linear form $\phi_{u}  = \flat (u)$ associated to the vector $u \in E$ via the duality induced by a Hermitian inner product. Dirac’s proposal is to denote the vectors $u$ in $E$ by $|u\rangle$ , and call them kets; the notation $|u\rangle$ is pronounced “ket u.” Given two kets (vectors) $|u\rangle$ and $|v\rangle$ , their inner product is denoted by
$$\langle u|v\rangle$$
(instead of $|u\rangle \cdot |v\rangle$ ). The notation $\langle u|v\rangle$ for the inner product of $|u\rangle$ and $|v\rangle$ anticipates duality. Indeed, we define the dual (usually called adjoint) bra $u$ of ket $u$, denoted by $\langle$ u|, as the linear form whose value on any ket $v$ is given by the inner product, so
$$\langle u|(|v\rangle ) = \langle u|v\rangle .$$
Thus, bra $u = \langle$ u| is Dirac’s notation for our $\flat (u)$. Since the map $\flat$ is semi-linear, we have
$$\langle \lambda u| =\overline{\lambda}\langle u|.$$
Using the bra-ket notation, given an orthonormal basis $(|u_{1}\rangle , \dots  , |u_{n}\rangle$ ), ket $v$ (a vector) is written as
$$|v\rangle = \sum_{i=1}^{n}  \langle v|u_{i}\rangle |u_{i}\rangle ,$$
and the corresponding linear form bra $v$ is written as
$$\langle v| = \sum_{i=1}^{n}  \overline{\langle}\overline{v}\overline{|}\overline{u}_{i}\overline{\rangle \langle} u_{i}| = \sum_{i=1}^{n}  \langle u_{i}|v\rangle \langle u_{i}|$$
over the dual basis $(\langle u_{1}|, \dots  , \langle u_{n}|)$. As cute as it looks, we do not recommend using the Dirac notation.

<!-- PAGE 541 -->
The existence of the isomorphism $\flat$ : $\overline{E} \to E^{*}$ is crucial to the existence of adjoint maps. Indeed, Theorem 14.6 allows us to define the adjoint of a linear map on a Hermitian space. Let $E$ be a Hermitian space of finite dimension $n$, and let $f$ : $E \to E$ be a linear map. For every $u \in E$, the map
$$v \mapsto \overline{u}\overline{\cdot}\overline{f}\overline{(}\overline{v}\overline{)}$$
is clearly a linear form in $E^{*}$, and by Theorem 14.6, there is a unique vector in $E$ denoted by $f^{*} (u)$, such that
$$\overline{f}^{*} \overline{(}\overline{u}\overline{)}\overline{\cdot}\overline{v} =\overline{u}\overline{\cdot}\overline{f}\overline{(}\overline{v}\overline{)},$$
that is,
$$f^{*} (u) \cdot  v = u \cdot  f(v),for every v \in E.$$
The following proposition shows that the map $f^{*}$ is linear.

> **Proposition 14.8.** Given a Hermitian space $E$ of finite dimension, for every linear map $f$ : $E \to E$ there is a unique linear map $f^{*}$ : $E \to E$ such that
$$f^{*} (u) \cdot  v = u \cdot  f(v),for all u, v \in E.$$

*Proof.* Careful inspection of the proof of Proposition 12.8 reveals that it applies unchanged. The only potential problem is in proving that $f^{*} (\lambda u) = \lambda f^{*} (u)$, but everything takes place in the first argument of the Hermitian product, and there, we have linearity.

> **Definition 14.6.** Given a Hermitian space $E$ of finite dimension, for every linear map $f$ : $E \to E$, the unique linear map $f^{*}$ : $E \to E$ such that
$$f^{*} (u) \cdot  v = u \cdot  f(v),for all u, v \in E$$
given by Proposition 14.8 is called the adjoint of $f$ (w.r.t. to the Hermitian product). The fact that
$$v \cdot  u =\overline{u}\overline{\cdot}\overline{v}$$
implies that the adjoint $f^{*}$ of $f$ is also characterized by
$$f(u) \cdot  v = u \cdot  f^{*} (v),$$
for all $u, v \in E$. Given two Hermitian spaces $E$ and $F$, where the Hermitian product on $E$ is denoted by $\langle$ -, $-\rangle_{1}$  and the Hermitian product on $F$ is denoted by $\langle$ -, $-\rangle_{2}$ , given any linear map $f$ : $E \to F$, it is immediately verified that the proof of Proposition 14.8 can be adapted to show that there is a unique linear map $f^{*}$ : $F \to E$ such that
$$\langle f(u), v\rangle_{2}  = \langle u, f^{*} (v)\rangle_{1}$$
for all $u \in E$ and all $v \in F$. The linear map $f^{*}$ is also called the adjoint of $f$. As in the Euclidean case, the following properties immediately follow from the definition of the adjoint map.

<!-- PAGE 542 -->

> **Proposition 14.9.**
$(1)$ For any linear map $f$ : $E \to F$, we have
$$f^{**} = f.$$
$(2)$ For any two linear maps $f, g: E \to F$ and any scalar $\lambda  \in \mathbb{R}$:
$$(f + g)^{*}= f^{*} + g^{*}$$
$$(\lambda f)^{*}=\overline{\lambda f}^{*} .$$
$(3)$ If $E, F, G$ are Hermitian spaces with respective inner products $\langle$ -, $-\rangle_{1} , \langle$ -, $-\rangle_{2}$ , and $\langle$ -, $-\rangle_{3}$ , and if $f$ : $E \to F$ and $g: F \to G$ are two linear maps, then
$$(g \circ f)^{*}= f^{*} \circ g^{*}.$$
As in the Euclidean case, a linear map $f$ : $E \to E$ (where $E$ is a finite-dimensional Hermitian space) is self-adjoint if $f = f^{*}$ . The map $f$ is positive semidefinite iff
$$\langle f(x), x\rangle \ge 0all x \in E;$$
positive definite iff
$$\langle f(x), x\rangle > 0all x \in E, x \neq  0.$$
An interesting corollary of Proposition 14.3 is that a positive semidefinite linear map must be self-adjoint. In fact, we can prove a slightly more general result.

> **Proposition 14.10.** Given any finite-dimensional Hermitian space $E$ with Hermitian product $\langle$ -, $-\rangle$ , for any linear map $f$ : $E \to E$, if $\langle$ f(x), $x\rangle \in \mathbb{R}$ for all $x \in E$, then $f$ is self-adjoint. In particular, any positive semidefinite linear map $f$ : $E \to E$ is self-adjoint.

*Proof.* Since $\langle$ f(x), $x\rangle \in \mathbb{R}$ for all $x \in E$, we have
$$\langle f(x), x\rangle =\overline{\langle}\overline{f}\overline{(}\overline{x}\overline{)}\overline{, x}\overline{\rangle}$$
$$= \langle x, f(x)\rangle$$
$$= \langle f^{*} (x), x\rangle ,$$
so we have
$$\langle (f -f^{*} )(x), x\rangle = 0all x \in E,$$
and Proposition 14.3 implies that $f$ - $f^{*} = 0$. Beware that Proposition 14.10 is false if $E$ is a real Euclidean space. As in the Euclidean case, Theorem 14.6 can be used to show that any Hermitian space of finite dimension has an orthonormal basis. The proof is unchanged.

<!-- PAGE 543 -->

> **Proposition 14.11.** Given any nontrivial Hermitian space $E$ of finite dimension $n \ge 1$, there is an orthonormal basis $(u_{1}, \dots  , u_{n})$ for $E$. The Gram–Schmidt orthonormalization procedure also applies to Hermitian spaces of finite dimension, without any changes from the Euclidean case!

> **Proposition 14.12.** Given a nontrivial Hermitian space $E$ of finite dimension $n \ge 1$, from any basis $(e_{1}, \dots  , e_{n})$ for $E$ we can construct an orthonormal basis $(u_{1}, \dots  , u_{n})$ for $E$ with the property that for every $k, 1 \le k \le n$, the families $(e_{1}, \dots  , e_{k})$ and $(u_{1}, \dots  , u_{k})$ generate the same subspace.
Remark: The remarks made after Proposition 12.10 also apply here, except that in the QR-decomposition, $Q$ is a unitary matrix. As a consequence of Proposition 12.9 (or Proposition 14.12), given any Hermitian space of finite dimension $n$, if $(e_{1}, \dots  , e_{n})$ is an orthonormal basis for $E$, then for any two vectors $u = u_{1}e_{1} + \cdots  + u_{n}e_{n}$ and $v = v_{1}e_{1} + \cdots  + v_{n}e_{n}$, the Hermitian product $u \cdot  v$ is expressed as
$$u \cdot  v = (u_{1}e_{1} + \cdots  + u_{n}e_{n}) \cdot  (v_{1}e_{1} + \cdots  + v_{n}e_{n}) = \sum_{i=1}^{n}  u_{i}\overline{v}_{i},$$
and the norm $\|u\|$ as
$$1/2$$
$$\|u\|= \|u_{1}e_{1} + \cdots  + u_{n}e_{n}\|= \begin{pmatrix} |u_{i}|^{2} \end{pmatrix} \sum_{i=1}^{n}  .$$
The fact that a Hermitian space always has an orthonormal basis implies that any Gram matrix $G$ can be written as
$$G = Q^{*}Q,$$
for some invertible matrix $Q$. Indeed, we know that in a change of basis matrix, a Gram matrix $G$ becomes G' $= P^{*}GP$. If the basis corresponding to G' is orthonormal, then G' $=$ I, so $G = (P^{-1} )^{*}P^{-1}$ . Proposition 12.11 also holds unchanged.

> **Proposition 14.13.** Given any nontrivial Hermitian space $E$ of finite dimension $n \ge 1$, for any subspace $F$ of dimension $k$, the orthogonal complement $F^{\perp}$ of $F$ has dimension $n$ - $k$, and $E = F \oplus F^{\perp}$ . Furthermore, we have $F^{\perp \perp} = F$.
