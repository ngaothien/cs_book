# Sesquilinear Forms


<!-- PAGE 1019 -->

## 29.2 Sesquilinear Forms

$$In \frac{order}{\lambda ,} to accomodate Hermitian forms, we assume that some involutive automorphism,$$
$\lambda  \mapsto$  of the field $K$ is given. This automorphism of $K$ satisfies the following properties:
$$\overline{(}\overline{\lambda}\overline{+}\overline{\mu}\overline{) =}\overline{\lambda} +\overline{\mu}$$
$$\overline{(}\overline{\lambda \mu}\overline{) =}\overline{\lambda  \mu}$$
$$\overline{\lambda} = \lambda .$$
Since any field automorphism maps the multiplicative unit $1$ to itself, we have $\overline{1 = 1.}$ If the automorphism $\lambda  \mapsto \overline{\lambda}$ is the identity, then we are in the standard situation of a bilinear form. When $K =\mathbb{C}$ (the complex numbers), then we usually pick the automorphism of $\mathbb{C}$ to be conjugation; namely, the map
$$a + ib \mapsto a -ib.$$

> **Definition 29.8.** Given two vector spaces $E$ and $F$ over a field $K$ with an involutive automorphism $\lambda  \mapsto \overline{\lambda}$, a map $\phi$ : $E \times  F \to K$ is a (right) sesquilinear form iff the following conditions hold: For all $u, u_{1}, u_{2} \in E$, all $v, v_{1}, v_{2} \in F$, for all $\lambda , \mu  \in K$, we have
$$\phi (u_{1} + u_{2}, v) = \phi (u_{1}, v) + \phi (u_{2}, v)$$
$$\phi (u, v_{1} + v_{2}) = \phi (u, v_{1}) + \phi (u, v_{2})$$
$$\phi (\lambda u, v) = \lambda \phi (u, v)$$
$$\phi (u, \mu v) =\overline{\mu \phi}(u, v).$$
Again, $\phi (0, v) = \phi (u, 0) = 0$. If $E = F$, then we have
$$\phi (\lambda u + \mu v, \lambda u + \mu v) = \lambda \phi (u, \lambda u + \mu v) + \mu \phi (v, \lambda u + \mu v)$$
$$=\overline{\lambda \lambda \phi}(u, u) +\overline{\lambda \mu \phi}(u, v) +\overline{\lambda \mu \phi}(v, u) +\overline{\mu \mu \phi}(v, v).$$
If we let $\lambda  = \mu  = 1$ and then $\lambda  = 1, \mu  = -1$, we get
$$\phi (u + v, u + v) = \phi (u, u) + \phi (u, v) + \phi (v, u) + \phi (v, v)$$
$$\phi (u -v, u -v) = \phi (u, u) -\phi (u, v) -\phi (v, u) + \phi (v, v),$$
so by subtraction, we get
$$2(\phi (u, v) + \phi (v, u)) = \phi (u + v, u + v) -\phi (u -v, u -v)for u, v \in E.$$
If we replace $v$ by $\lambda v$ (with $\lambda  \neq  0)$, we get
$$2(\overline{\lambda \phi}(u, v) + \lambda \phi (v, u)) = \phi (u + \lambda v, u + \lambda v) -\phi (u -\lambda v, u -\lambda v),$$

<!-- PAGE 1020 -->
and by combining the above two equations, we get
$$2(\lambda  -\overline{\lambda})\phi (u, v) = \lambda \phi (u + v, u + v) -\lambda \phi (u -v, u -v)$$
$$-\phi (u + \lambda v, u + \lambda v) + \phi (u -\lambda v, u -\lambda v).(*)$$
If the automorphism $\lambda  \mapsto \overline{\lambda}$ is not the identity, then there is some $\lambda  \in K$ such that $\lambda -\overline{\lambda} \neq  0$, and if $K$ is not of characteristic $2$, then we see that the sesquilinear form $\phi$  is completely determined by its restriction to the diagonal (that is, the set of values ${\phi (u, u)$ | $u \in E})$. In the special case where $K =\mathbb{C}$, we can pick $\lambda  = i$, and we get $4\phi (u, v) = \phi (u + v, u + v)$ - $\phi (u$ - $v, u$ - $v) + i\phi (u + \lambda v, u + \lambda v)$ - $i\phi (u$ - $\lambda v, u$ - $\lambda v)$.
Remark: If the automorphism $\lambda  \mapsto \overline{\lambda}$ is the identity, then in general $\phi$  is not determined by its value on the diagonal, unless $\phi$  is symmetric. In the sesquilinear setting, it turns out that the following two cases are of interest: $1$. We have
$$\phi (v, u) =\overline{\phi}\overline{(}\overline{u, v}\overline{)},for all u, v \in E,$$
in which case we say that $\phi$  is Hermitian. In the special case where $K = \mathbb{C}$ and the involutive automorphism is conjugation, we see that $\phi (u, u) \in \mathbb{R}$, for $u \in E. 2$. We have
$$\phi (v, u) = -\overline{\phi}\overline{(}\overline{u, v}\overline{)},for all u, v \in E,$$
in which case we say that $\phi$  is skew-Hermitian. We observed that in characteristic different from $2$, a sesquilinear form is determined by its restriction to the diagonal. For Hermitian and skew-Hermitian forms, we have the following kind of converse.

> **Proposition 29.8.** If $\phi$  is a nonzero Hermitian or skew-Hermitian form and if $\phi (u, u) = 0$ for all $u \in E$, then $K$ is of characteristic $2$ and the automorphism $\lambda  \mapsto \overline{\lambda}$ is the identity.

*Proof.* We give the proof in the Hermitian case, the skew-Hermitian case being left as an exercise. Assume that $\phi$  is alternating. From the identity
$$\phi (u + v, u + v) = \phi (u, u) + \phi (u, v) +\overline{\phi}\overline{(}\overline{u, v}\overline{) +} \phi (v, v),$$
we get
$$\phi (u, v) = -\overline{\phi}\overline{(}\overline{u, v}\overline{)} for all u, v \in E.$$
Since $\phi$  is not the zero form, there exist some nonzero vectors $u, v \in E$ such that $\phi (u, v) = 1$. For any $\lambda  \in K$, we have
$$\lambda \phi (u, v) = \phi (\lambda u, v) = -\overline{\phi}\overline{(}\overline{\lambda u, v}\overline{) =} -\overline{\lambda  \phi}\overline{(}\overline{u, v}\overline{)},$$

<!-- PAGE 1021 -->
and since $\phi (u, v) = 1$, we get
$$\lambda  = -\overline{\lambda} for all \lambda  \in K.$$
For $\lambda  = 1$, we get $1 = -1$, which means that $K$ has characterictic $2$. But then
$$\lambda  = -\overline{\lambda} =\overline{\lambda} for all \lambda  \in K,$$
so the automorphism $\lambda  \mapsto \overline{\lambda}$ is the identity. The definition of the linear maps $l_{\phi}$ and $r_{\phi}$ requires a small twist due to the automorphism $\lambda  \mapsto \overline{\lambda}$.
$$\frac{Definition}{\lambda ,} 29.9. Given a vector space \frac{E}{E} over a field K with an involutive automorphism$$
$\lambda  \mapsto$  we define the $K$-vector space  as $E$ with its abelian group structure, but with scalar multiplication given by
$$(\lambda , u) \mapsto \overline{\lambda u.}$$
Given two $K$-vector spaces $E$ and $F$, a semilinear map $f$ : $E \to F$ is a function, such that for all $u, v \in E$, for all $\lambda  \in K$, we have
$$f(u + v) = f(u) + f(v)$$
$$f(\lambda u) =\overline{\lambda f}(u).$$
$$Because \overline{\lambda} = \lambda , observe that a \frac{function}{E} f : E \to F is semilinear iff it is a linear map$$
$$f : \overline{E} \to F \frac{.}{E.} The K-vector spaces E and are isomorphic, since any basis (e_{i})_{i\in I} of E is also$$
a basis of The maps $l_{\phi}$ and $r_{\phi}$ are defined as follows: For every $u \in E$, let $l_{\phi}(u)$ be the linear form in $F^{*}$ defined so that
$$l_{\phi}(u)(y) =\overline{\phi}\overline{(}\overline{u, y}\overline{)} for all y \in F,$$
and for every $v \in F$, let $r_{\phi}(v)$ be the linear form in $E^{*}$ defined so that
$$r_{\phi}(v)(x) = \phi (x, v)for all x \in E.$$
The reader should check that because we used $\overline{\phi}\overline{(}\overline{u, y}\overline{)}$ in the definition of $l_{\phi}(u)(y)$, the
$$function \frac{l_{\phi}}{E} (u) is indeed a linear form in F^{*} . It \frac{is}{F} also easy to check that l_{\phi} is a linear$$
map $l_{\phi}$ :  $\to F^{*}$ , and that $r_{\phi}$ is a linear map $r_{\phi}$ :  $\to E^{*}$ (equivalently, $l_{\phi}$ : $E \to F^{*}$ and $r_{\phi}$ : $F \to E^{*}$ are semilinear). The notion of a nondegenerate sesquilinear form is identical to the notion for bilinear forms. For the convenience of the reader, we repeat the definition.

> **Definition 29.10.** A sesquilinear map $\phi$ : $E \times  F \to K$ is said to be nondegenerate iff the following conditions hold:

<!-- PAGE 1022 -->
$(1)$ For every $u \in E$, if $\phi (u, v) = 0$ for all $v \in F$, then $u = 0$, and
$(2)$ For every $v \in F$, if $\phi (u, v) = 0$ for all $u \in E$, then $v = 0$. Proposition 29.1 translates into the following proposition. The proof is left as an exercise.

> **Proposition 29.9.** Given a sesquilinear map $\phi$ : $E \times  F \to K$, the following properties hold:
(a) The map $l_{\phi}$ is injective iff Property $(1)$ of Definition 29.10 holds.
$(b)$ The map $r_{\phi}$ is injective iff Property $(2)$ of Definition 29.10 holds.
$(c)$ The sesquilinear form $\phi$  is nondegenerate and iff $l_{\phi}$ and $r_{\phi}$ are injective.
$$(d) If the sesquillinear form \phi  is nondegenerate and \frac{if}{F} E and F have finite dimensions,$$
then dim(E) $=$ dim(F), and $l_{\phi}$ : $\overline{E} \to F^{*}$ and $r_{\phi}$ :  $\to E^{*}$ are linear isomorphisms. Propositions 29.2 and 29.3 also generalize to sesquilinear forms. We also have the following version of Theorem 29.4, whose proof is left as an exercise.

> **Theorem 29.10.** Given any sesquilinear form $\phi$ : $E \times  E \to K$ with dim(E) $= n$, if $\phi$  is Hermitian and $K$ does not have characteristic $2$, then there is a basis $(e_{1}, \dots  , e_{n})$ of $E$ such that $\phi (e_{i}, e_{j}) = 0$, for all $i \neq  j$. As in Section 29.1, if $E$ and $F$ are finite-dimensional vector spaces and if $(e_{1}, \dots  , e_{m})$ is a basis of $E$ and $(f_{1}, \dots  , f_{n})$ is a basis of $F$ then the sesquilinearity of $\phi$  yields
$$\phi \begin{pmatrix} x_{i}e_{i}, & y_{j}f_{j} \end{pmatrix} \sum_{i=1}^{m}  \sum_{j=1}^{n}  = \sum_{i=1j}^{m}  \sum_{=1}^{n}  x_{i}\phi (e_{i}, f_{j})\overline{y}_{j}.$$
This shows that $\phi$  is completely determined by the $n \times  m$ matrix $M = (m_{ij})$ with $m_{ij} = \phi (e_{j}, f_{i})$, and in matrix form, we have
$$\phi (x, y) = x^{\top}M^{\top} \overline{y} = y^{*}Mx,$$
where $x$ and $\overline{y}$ are the column vectors associated with $(x_{1}, \dots  , x_{m}) \in K^{m}$ and $(\overline{y}_{1}\overline{, \dots  , y}_{n}) \in K^{n}$, and $y^{*} = \overline{y}^{\top}$. As earlier, we are committing the slight abuse of notation of letting $x$
$$denote both the vector x = \sum_{i}  n=1 x_{i}e_{i} and the column vector associated with (x_{1}, \dots  , x_{n})$$
(and similarly for $y)$.

> **Definition 29.11.** If $(e_{1}, \dots  , e_{m})$ is a basis of $E$ and $(f_{1}, \dots  , f_{n})$ is a basis of $F$, for any sesquilinear form $\phi$ : $E \times  F \to K$, the $n \times  m$ matrix $M = (m_{ij})$ given by $m_{ij} = \phi (e_{j}, f_{i})$ for $i = 1, \dots  , n$ and $j = 1, \dots  , m$ is called the matrix of $\phi$  with respect to the bases $(e_{1}, \dots  , e_{m})$ and $(f_{1}, \dots  , f_{n})$.
