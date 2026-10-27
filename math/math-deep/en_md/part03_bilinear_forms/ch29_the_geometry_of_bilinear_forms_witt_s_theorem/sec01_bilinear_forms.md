# Bilinear Forms


<!-- PAGE 1011 -->
Chapter $29$ The Geometry of Bilinear Forms; Witt’s Theorem; The Cartan–Dieudonn´e Theorem

## 29.1 Bilinear Forms

In this chapter, we study the structure of a $K$-vector space $E$ endowed with a nondegenerate bilinear form $\phi$ : $E \times  E \to K$ (for any field $K)$, which can be viewed as a kind of generalized inner product. Unlike the case of an inner product, there may be nonzero vectors $u \in E$ such that $\phi (u, u) = 0$ so the map $u \mapsto \phi (u, u)$ can no longer be interpreted as a notion of square length (also, $\phi (u, u)$ may not be real and positive!). However, the notion of orthogonality survives: we say that $u, v \in E$ are orthogonal iff $\phi (u, v) = 0$. Under some additional conditions on $\phi$ , it is then possible to split $E$ into orthogonal subspaces having some special properties. It turns out that the special cases where $\phi$  is symmetric (or Hermitian) or skewsymmetric (or skew-Hermitian) can be handled uniformly using a deep theorem due to Witt (the Witt decomposition theorem $(1936))$. We begin with the very general situation of a bilinear form $\phi$ : $E\times F \to K$, where $K$ is an arbitrary field, possibly of characteristric $2$. Actually, even though at first glance this may appear to be an unnecessary abstraction, it turns out that this situation arises in attempting to prove properties of a bilinear map $\phi$ : $E \times E \to K$, because it may be necessary to restrict $\phi$  to different subspaces $U$ and $V$ of $E$. This general approach was pioneered by Chevalley $[37], E$. Artin $[6]$, and Bourbaki $[24]$. The third source was a major source of inspiration, and many proofs are taken from it. Other useful references include Snapper and Troyer $[168]$, Berger $[12]$, Jacobson $[101]$, Grove $[86]$, Taylor $[180]$, and Berndt $[14]$.

> **Definition 29.1.** Given two vector spaces $E$ and $F$ over a field $K$, a map $\phi$ : $E \times  F \to K$ is a bilinear form iff the following conditions hold: For all $u, u_{1}, u_{2} \in E$, all $v, v_{1}, v_{2} \in F$, for
$$1011$$

<!-- PAGE 1012 -->
all $\lambda , \mu  \in K$, we have
$$\phi (u_{1} + u_{2}, v) = \phi (u_{1}, v) + \phi (u_{2}, v)$$
$$\phi (u, v_{1} + v_{2}) = \phi (u, v_{1}) + \phi (u, v_{2})$$
$$\phi (\lambda u, v) = \lambda \phi (u, v)$$
$$\phi (u, \mu v) = \mu \phi (u, v).$$
A bilinear form as in Definition 29.1 is sometimes called a pairing. The first two conditions imply that $\phi (0, v) = \phi (u, 0) = 0$ for all $u \in E$ and all $v \in F$. If $E = F$, observe that
$$\phi (\lambda u + \mu v, \lambda u + \mu v) = \lambda \phi (u, \lambda u + \mu v) + \mu \phi (v, \lambda u + \mu v)$$
$$= \lambda^{2} \phi (u, u) + \lambda \mu \phi (u, v) + \lambda \mu \phi (v, u) + \mu^{2} \phi (v, v).$$
If we let $\lambda  = \mu  = 1$, we get
$$\phi (u + v, u + v) = \phi (u, u) + \phi (u, v) + \phi (v, u) + \phi (v, v).$$
If $\phi$  is symmetric, which means that
$$\phi (u, v) = \phi (v, u)for all u, v \in E,$$
then
$$2\phi (u, v) = \phi (u + v, u + v) -\phi (u, u) -\phi (v, v).(*)$$
The function $\Phi$  defined such that
$$\Phi (u) = \phi (u, u)u \in E,$$
is called the quadratic form associated with $\phi$ . If the field $K$ is not of characteristic $2$, then $\phi$  is completely determined by its quadratic form $\Phi$ . The symmetric bilinear form $\phi$  is called the polar form of $\Phi$ . This suggests the following definition.

> **Definition 29.2.** A function $\Phi$ : $E \to K$ is a quadratic form on $E$ if the following conditions hold:
$(1)$ We have $\Phi (\lambda u) = \lambda^{2} \Phi (u)$, for all $u \in E$ and all $\lambda  \in E$.
$(2)$ The map $\phi'$ given by $\phi' (u, v) = \Phi (u+v)-\Phi (u)-\Phi (v)$ is bilinear. Obviously, the map $\phi'$ is symmetric. Since $\Phi (x + x) = \Phi$ (2x) $= 4\Phi (x)$, we have
$$\phi' (u, u) = 2\Phi (u)u \in E.$$

<!-- PAGE 1013 -->
If the field $K$ is not of characteristic $2$, then $\phi  =^{1}\phi'$ is the unique symmetric bilinear form such that that $\phi (u, u) = \Phi (u)$ for all $u \in E. The^{2}$ bilinear form $\phi  =_{2}^{1}\phi'$ is called the polar form of $\Phi$ . In this case, there is a bijection between the set of bilinear forms on $E$ and the set of quadratic forms on $E$. If $K$ is a field of characteristic $2$, then $\phi'$ is alternating, which means that
$$\phi' (u, u) = 0for all u \in E.$$
Thus if $K$ is a field of characteristic $2$, then $\Phi$  cannot be recovered from the symmetric bilinear form $\phi'$ . If $(e_{1}, \dots  , e_{n})$ is a basis of $E$, it is easy to show that
$$\Phi \begin{pmatrix} \lambda_{i} e_{i} \end{pmatrix} \sum_{i=1}^{n}  = \sum_{i=1}^{n}  \lambda_{i}^{2}  \Phi (e_{i}) + \sum_{i\neq j}  \lambda_{i} \lambda_{j} \phi' (e_{i}, e_{j}).$$
This shows that the quadratic form $\Phi$  is completely determined by the scalars $\Phi (e_{i})$ and $\phi' (e_{i}, e_{j})$ (i̸ $= j)$. Furthermore, given any bilinear form $\psi$ : $E \times  E \to K$ (not necessarily symmetric) we can define a quadratic form $\Phi$  by setting $\Phi (x) = \psi (x, x)$, and we immediately check that the symmetric bilinear form $\phi'$ associated with $\Phi$  is given by $\phi' (u, v) = \psi (u, v) + \psi (v, u)$. Using the above facts, it is not hard to prove that given any quadratic form $\Phi$ , there is some (nonsymmetric) bilinear form $\psi$  such that $\Phi (u) = \psi (u, u)$ for all $u \in E$ (see Bourbaki $[24]$, Section §3.4, Proposition $2)$. Thus, quadratic forms are more general than symmetric bilinear forms (except in characteristic $\neq  2)$.

> **Definition 29.3.** Given any bilinear form $\phi$ : $E \times  E \to K$ where $K$ is a field of any characteristic, we say that $\phi$  is alternating if
$$\phi (u, u) = 0for all u \in E,$$
and skew-symmetric if
$$\phi (v, u) = -\phi (u, v)for all u, v \in E.$$
If $K$ is a field of any characteristic, the identity
$$\phi (u + v, u + v) = \phi (u, u) + \phi (u, v) + \phi (v, u) + \phi (v, v)$$
shows that if $\phi$  is alternating, then
$$\phi (v, u) = -\phi (u, v)for all u, v \in E,$$
that is, $\phi$  is skew-symmetric. Conversely, if the field $K$ is not of characteristic $2$, then a skew-symmetric bilinear map is alternating, since $\phi (u, u) = -\phi (u, u)$ implies $\phi (u, u) = 0$. An important consequence of bilinearity is that a pairing yields a linear map from $E$ into $F^{*}$ and a linear map from $F$ into $E^{*}$ (where $E^{*} = Hom_{K}(E, K)$, the dual of $E$, is the set of linear maps from $E$ to $K$, called linear forms).

<!-- PAGE 1014 -->

> **Definition 29.4.** Given a bilinear map $\phi$ : $E \times  F \to K$, for every $u \in E$, let $l_{\phi}(u)$ be the linear form in $F^{*}$ given by
$$l_{\phi}(u)(y) = \phi (u, y)for all y \in F,$$
and for every $v \in F$, let $r_{\phi}(v)$ be the linear form in $E^{*}$ given by
$$r_{\phi}(v)(x) = \phi (x, v)for all x \in E.$$
Because $\phi$  is bilinear, the maps $l_{\phi}$ : $E \to F^{*}$ and $r_{\phi}$ : $F \to E^{*}$ are linear.

> **Definition 29.5.** A bilinear map $\phi$ : $E\times F \to K$ is said to be nondegenerate iff the following conditions hold:
$(1)$ For every $u \in E$, if $\phi (u, v) = 0$ for all $v \in F$, then $u = 0$, and
$(2)$ For every $v \in F$, if $\phi (u, v) = 0$ for all $u \in E$, then $v = 0$. The following proposition shows the importance of $l_{\phi}$ and $r_{\phi}$.

> **Proposition 29.1.** Given a bilinear map $\phi$ : $E \times  F \to K$, the following properties hold:
(a) The map $l_{\phi}$ is injective iff Property $(1)$ of Definition 29.5 holds.
$(b)$ The map $r_{\phi}$ is injective iff Property $(2)$ of Definition 29.5 holds.
$(c)$ The bilinear form $\phi$  is nondegenerate and iff $l_{\phi}$ and $r_{\phi}$ are injective.
$(d)$ If the bilinear form $\phi$  is nondegenerate and if $E$ and $F$ have finite dimensions, then dim(E) $=$ dim(F), and $l_{\phi}$ : $E \to F^{*}$ and $r_{\phi}$ : $F \to E^{*}$ are linear isomorphisms.

*Proof.* (a) Assume that $(1)$ of Definition 29.5 holds. If $l_{\phi}(u) = 0$, then $l_{\phi}(u)$ is the linear form whose value is $0$ for all $y$; that is,
$$l_{\phi}(u)(y) = \phi (u, y) = 0for all y \in F,$$
and by $(1)$ of Definition 29.5, we must have $u = 0$. Therefore, $l_{\phi}$ is injective. Conversely, if $l_{\phi}$ is injective, and if
$$l_{\phi}(u)(y) = \phi (u, y) = 0for all y \in F,$$
then $l_{\phi}(u)$ is the zero form, and by injectivity of $l_{\phi}$, we get $u = 0$; that is, $(1)$ of Definition 29.5 holds.
$(b)$ The proof is obtained by swapping the arguments of $\phi$ .
$(c)$ This follows from (a) and $(b)$.
$(d)$ If $E$ and $F$ are finite dimensional, then dim(E) $= dim(E^{*})$ and dim(F) $= dim(F^{*}$ ). Since $\phi$  is nondegenerate, $l_{\phi}$ : $E \to F^{*}$ and $r_{\phi}$ : $F \to E^{*}$ are injective, so dim(E) $\le dim(F^{*}$ ) $=$ dim(F) and dim(F) $\le dim(E^{*}) =$ dim(E), which implies that
$$\dim(E) = \dim(F),$$
and thus, $l_{\phi}$ : $E \to F^{*}$ and $r_{\phi}$ : $F \to E^{*}$ are bijective.

<!-- PAGE 1015 -->
As a corollary of Proposition 29.1, we have the following characterization of a nondegenerate bilinear map. The proof is left as an exercise.

> **Proposition 29.2.** Given a bilinear map $\phi$ : $E \times  F \to K$, if $E$ and $F$ have the same finite dimension, then the following properties are equivalent:
$(1)$ The map $l_{\phi}$ is injective.
$(2)$ The map $l_{\phi}$ is surjective.
$(3)$ The map $r_{\phi}$ is injective.
$(4)$ The map $r_{\phi}$ is surjective.
$(5)$ The bilinear form $\phi$  is nondegenerate. Observe that in terms of the canonical pairing between $E^{*}$ and $E$ given by
$$\langle f, u\rangle = f(u),f \in E^{*}, u \in E,$$
(and the canonical pairing between $F^{*}$ and $F)$, we have
$$\phi (u, v) = \langle l_{\phi}(u), v\rangle = \langle r_{\phi}(v), u\rangle u \in E, v \in F.$$

> **Proposition 29.3.** Given a bilinear map $\phi$ : $E \times  F \to K$, if $\phi$  is nondegenerate and $E$ and $F$ are finite-dimensional, then dim(E) $=$ dim(F) $= n$, and for every basis $(e_{1}, \dots  , e_{n})$ of $E$, there is a basis $(f_{1}, \dots  , f_{n})$ of $F$ such that $\phi (e_{i}, f_{j}) = \delta_{ij}$ , for all $i, j = 1, \dots  , n$.

*Proof.* Since $\phi$  is nondegenerate, by Proposition 29.1 we have dim(E) $=$ dim(F) $= n$, and by Proposition 29.2, the linear map $r_{\phi}$ is bijective. Then, if $(e_{1}^{*}, \dots  , e_{n}^{*})$ is the dual basis (in $E^{*})$ of the basis $(e_{1}, \dots  , e_{n})$, the vectors $(f_{1}, \dots  , f_{n})$ given by $f_{i} = r_{\phi}^{-1} (e_{i}^{*}$ ) form a basis of $F$, and we have
$$\phi (e_{i}, f_{j}) = \langle r_{\phi}(f_{j}), e_{i}\rangle = \langle e_{i}^{*} , e_{j}\rangle = \delta_{ij} ,$$
as claimed. If $E = F$ and $\phi$  is symmetric, then we have the following interesting result.

> **Theorem 29.4.** Given any bilinear form $\phi$ : $E\times E \to K$ with dim(E) $= n$, if $\phi$  is symmetric (possibly degenerate) and $K$ does not have characteristic $2$, then there is a basis $(e_{1}, \dots  , e_{n})$ of $E$ such that $\phi (e_{i}, e_{j}) = 0$, for all $i \neq  j$.

*Proof.* We proceed by induction on $n \ge 0$, following a proof due to Chevalley. The base case $n = 0$ is trivial. For the induction step, assume that $n \ge 1$ and that the induction hypothesis holds for all vector spaces of dimension n-1. If $\phi (u, v) = 0$ for all $u, v \in E$, then the statement holds trivially. Otherwise, since $K$ does not have characteristic $2$, equation
$$2\phi (u, v) = \phi (u + v, u + v) -\phi (u, u) -\phi (v, v)(*)$$

<!-- PAGE 1016 -->
show that there is some nonzero vector $e_{1} \in E$ such that $\phi (e_{1}, e_{1}) \neq  0$ since otherwise $\phi$ would vanish for all $u, v \in E$. We claim that the set
$$H = {v \in E | \phi (e_{1}, v) = 0}$$
has dimension $n$ - $1$, and that $e_{1} \in / H$. This is because
$$H = \mathrm{Ker} (l_{\phi}(e_{1})),$$
where $l_{\phi}(e_{1})$ is the linear form in $E^{*}$ determined by $e_{1}$. Since $\phi (e_{1}, e_{1}) \neq  0$, we have $e_{1} \in / H$, the linear form $l_{\phi}(e_{1})$ is not the zero form, and thus its kernel is a hyperplane $H$ (a subspace of dimension $n$ - $1)$. Since dim(H) $= n$ - $1$ and $e_{1} \in / H$, we have the direct sum
$$E = H \oplus Ke_{1}.$$
By the induction hypothesis applied to $H$, we get a basis $(e_{2}, \dots  , e_{n})$ of vectors in $H$ such that $\phi (e_{i}, e_{j}) = 0$, for all $i \neq  j$ with $2 \le i, j \le n$. Since $\phi (e_{1}, v) = 0$ for all $v \in H$ and since $\phi$  is symmetric, we also have $\phi (v, e_{1}) = 0$ for all $v \in H$, so we obtain a basis $(e_{1}, \dots  , e_{n})$ of $E$ such that $\phi (e_{i}, e_{j}) = 0$, for all $i \neq  j$. If $E$ and $F$ are finite-dimensional vector spaces and if $(e_{1}, \dots  , e_{m})$ is a basis of $E$ and $(f_{1}, \dots  , f_{n})$ is a basis of $F$ then the bilinearity of $\phi$  yields
$$\phi \begin{pmatrix} x_{i}e_{i}, & y_{j}f_{j} \end{pmatrix} \sum_{i=1}^{m}  \sum_{j=1}^{n}  = \sum_{i=1j}^{m}  \sum_{=1}^{n}  x_{i}\phi (e_{i}, f_{j})y_{j}.$$
This shows that $\phi$  is completely determined by the $n \times  m$ matrix $M = (m_{ij})$ with $m_{ij} = \phi (e_{j}, f_{i})$, and in matrix form, we have
$$\phi (x, y) = x^{\top}M^{\top} y = y^{\top}Mx,$$
where $x$ and $y$ are the column vectors associated with $(x_{1}, \dots  , x_{m}) \in K^{m}$ and $(y_{1}, \dots  , y_{n}) \in K^{n}$. As in Section 12.1, we are committing the slight abuse of notation of letting $x$ denote
$$both the vector x = \sum_{i}  n=1 x_{i}e_{i} and the column vector associated with (x_{1}, \dots  , x_{n}) (and$$
similarly for $y)$.

> **Definition 29.6.** If $(e_{1}, \dots  , e_{m})$ is a basis of $E$ and $(f_{1}, \dots  , f_{n})$ is a basis of $F$, for any bilinear form $\phi$ : $E \times  F \to K$, the $n \times  m$ matrix $M = (m_{ij})$ given by $m_{ij} = \phi (e_{j}, f_{i})$ for $i = 1, \dots  , n$ and $j = 1, \dots  , m$ is called the matrix of $\phi$  with respect to the bases $(e_{1}, \dots  , e_{m})$ and $(f_{1}, \dots  , f_{n})$. The following fact is easily proved.

> **Proposition 29.5.** If $m =$ dim(E) $=$ dim(F) $= n$, then $\phi$  is nondegenerate iff the matrix $M$ is invertible iff det(M) $\neq  0$.

<!-- PAGE 1017 -->
As we will see later, most bilinear forms that we will encounter are equivalent to one whose matrix is of the following form: $1. I_{n}, -I_{n}. 2$. If $p + q = n$, with $p, q \ge 1$,
$$I_{p,q} = \begin{pmatrix} I_{p} & 0 \\ 0 & -I_{q} \end{pmatrix}$$
$3$. If $n =$ 2m,
$$J_{m.m} = \begin{pmatrix} 0 & I_{m} \\ -I_{m} & 0 \end{pmatrix}$$
$4$. If $n =$ 2m,
$$A_{m,m} = I_{m.m}J_{m.m} = \begin{pmatrix} 0 & I_{m} \\ I_{m} & 0 \end{pmatrix} .$$
If we make changes of bases given by matrices $P$ and $Q$, so that $x =$ Px' and $y =$ Qy', then the new matrix expressing $\phi$  is $P^{\top}$ MQ. In particular, if $E = F$ and the same basis is used, then the new matrix is $P^{\top}$ MP. This shows that if $\phi$  is nondegenerate, then the determinant of $\phi$  is determined up to a square element. Observe that if $\phi$  is a symmetric bilinear form $(E = F)$ and if $K$ does not have characteristic $2$, then by Theorem 29.4, there is a basis of $E$ with respect to which the matrix $M$ representing $\phi$  is a diagonal matrix. If $K =\mathbb{R}$ or $K =\mathbb{C}$, this allows us to classify completely the symmetric bilinear forms. Recall that $\Phi (u) = \phi (u, u)$ for all $u \in E$.

> **Proposition 29.6.** Given any bilinear form $\phi$ : $E \times  E \to K$ with dim(E) $= n$, if $\phi$  is symmetric and $K$ does not have characteristic $2$, then there is a basis $(e_{1}, \dots  , e_{n})$ of $E$ such that
$$\Phi \begin{pmatrix} x_{i}e_{i} \end{pmatrix} \sum_{i=1}^{n}  = \sum_{i=1}^{r}  \lambda_{i} x_{i}^{2} ,$$
for some $\lambda_{i}  \in K -{0}$ and with $r \le n$. Furthermore, if $K = \mathbb{C}$, then there is a basis $(e_{1}, \dots  , e_{n})$ of $E$ such that
$$\Phi \begin{pmatrix} x_{i}e_{i} \end{pmatrix} \sum_{i=1}^{n}  = \sum_{i=1}^{r}  x_{i}^{2} ,$$
and if $K =\mathbb{R}$, then there is a basis $(e_{1}, \dots  , e_{n})$ of $E$ such that
$$\Phi \begin{pmatrix} x_{i}e_{i} \end{pmatrix} \sum_{i=1}^{n}  = \sum_{i=1}^{p}  x_{i}^{2} - \sum_{i=p+1}^{p+q}  x_{i}^{2} ,$$
with $0 \le p, q$ and $p + q \le n$.

<!-- PAGE 1018 -->

*Proof.* The first statement is a direct consequence of Theorem 29.4. If $K = \mathbb{C}$, then every $\lambda_{i}$  has a square root $\mu_{i}$ , and if replace $e_{i}$ by $e_{i}/\mu_{i}$ , we obtained the desired form. If $K =\mathbb{R}$, then there are two cases: $1$. If $\lambda_{i}  > 0$, let $\mu_{i}$  be a positive square root of $\lambda_{i}$  and replace $e_{i}$ by $e_{i}/\mu_{i}$ . $2$. If $\lambda_{i}  < 0$, et $\mu_{i}$  be a positive square root of $-\lambda_{i}$  and replace $e_{i}$ by $e_{i}/\mu_{i}$ . In the nondegenerate case, the matrices corresponding to the complex and the real case are, $I_{n}, -I_{n}$, and $I_{p,q}$. Observe that the second statement of Proposition 29.6 holds in any field in which every element has a square root. In the case $K = \mathbb{R}$, we can show that(p, $q)$ only depends on $\phi$ .

> **Definition 29.7.** Let $\phi$ : $E \times E \to \mathbb{R}$ be any symmetric real bilinear form. For any subspace $U$ of $E$, we say that $\phi$  is positive definite on $U$ iff $\phi (u, u) > 0$ for all nonzero $u \in U$, and we say that $\phi$  is negative definite on $U$ iff $\phi (u, u) < 0$ for all nonzero $u \in U$. Then, let
$$r = \max{\dim(U) | U \subseteq E, \phi  is positive definite on U}$$
and let
$$s = \max{\dim(U) | U \subseteq E, \phi  is negative definite on U}$$

> **Proposition 29.7.** (Sylvester’s inertia law) Given any symmetric bilinear form $\phi$ : $E\times E \to \mathbb{R}$ with dim(E) $= n$, for any basis $(e_{1}, \dots  , e_{n})$ of $E$ such that
$$\Phi \begin{pmatrix} x_{i}e_{i} \end{pmatrix} \sum_{i=1}^{n}  = \sum_{i=1}^{p}  x_{i}^{2} - \sum_{i=p+1}^{p+q}  x_{i}^{2} ,$$
with $0 \le p, q$ and $p + q \le n$, the integers $p, q$ depend only on $\phi$ ; in fact, $p = r$ and $q = s$, with $r$ and $s$ as defined above.

*Proof.* If we let $U$ be the subspace spanned by $(e_{1}, \dots  , e_{p})$, then $\phi$  is positive definite on $U$, so $r \ge p$. Similarly, if we let $V$ be the subspace spanned by $(e_{p+1}, \dots  , e_{p+q})$, then $\phi$  is negative definite on $V$ , so $s \ge q$. Next, if $W_{1}$ is any subspace of maximum dimension such that $\phi$  is positive definite on $W_{1}$, and if we let V' be the subspace spanned by $(e_{p+1}, \dots  , e_{n})$, then $\phi (u, u) \le 0$ on V', so $W_{1} \cap$ V' $= (0)$, which implies that $dim(W_{1}) +$ dim(V') $\le n$, and thus, $r + n$ - $p \le n$; that is, $r \le p$. Similarly, if $W_{2}$ is any subspace of maximum dimension such that $\phi$  is negative definite on $W_{2}$, and if we let U' be the subspace spanned by $(e_{1}, \dots  , e_{p}, e_{p+q+1}, \dots  , e_{n})$, then $\phi (u, u) \ge 0$ on U', so $W_{2} \cap$ U' $= (0)$, which implies that $s + n$ - $q \le n$; that is, $s \le q$. Therefore, $p = r$ and $q = s$, as claimed These last two results can be generalized to ordered fields. For example, see Snapper and Troyer $[168]$, Artin $[6]$, and Bourbaki $[24]$.
