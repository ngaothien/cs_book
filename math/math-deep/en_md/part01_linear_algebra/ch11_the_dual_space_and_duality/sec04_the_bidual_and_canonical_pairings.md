# The Bidual and Canonical Pairings


<!-- PAGE 433 -->
and it is easy to see that they are linearly independent. Therefore, the space $U$ of linear forms in $E^{*}$ spanned by the above linear forms (equations) has dimension $n$ - $1$, and the space $U^{0}$ of matrices satisfying all these equations has dimension $n^{2}$ - $n + 1$. It is not so obvious to find a basis for this space. We will now pin down the relationship between a vector space $E$ and its bidual $E^{**}$.

## 11.4 The Bidual and Canonical Pairings


> **Proposition 11.5.** Let $E$ be a vector space. The following properties hold:
(a) The linear map $eval_{E}$ : $E \to E^{**}$ defined such that
$$eval_{E}(v) = eval_{v}for all v \in E,$$
that is, $eval_{E}(v)(u^{*}) = \langle u^{*}, v\rangle = u^{*}(v)$ for every $u^{*} \in E^{*}$, is injective.
$(b)$ When $E$ is of finite dimension $n$, the linear map $eval_{E}$ : $E \to E^{**}$ is an isomorphism (called the canonical isomorphism).
$$Proof. (a) Let (u_{i})_{i\in I} be a basis of E, and let v = \sum_{i}  \in I v_{i}u_{i}.If eval_{E}(v) = 0, then in$$
particular $eval_{E}(v)(u_{i}^{*}$ ) $= 0$ for all $u_{i}^{*}$ , and since
$$eval_{E}(v)(u_{i}^{*} ) = \langle u_{i}^{*} , v\rangle = v_{i},$$
we have $v_{i} = 0$ for all $i \in$ I, that is, $v = 0$, showing that $eval_{E}$ : $E \to E^{**}$ is injective. If $E$ is of finite dimension $n$, by Theorem 11.4, for every basis $(u_{1}, \dots  , u_{n})$, the family $(u_{1}^{*}, \dots  , u_{n}^{*})$ is a basis of the dual space $E^{*}$, and thus the family $(u_{1}^{**} , \dots  , u_{n}^{**}$ ) is a basis of the bidual $E^{**}$. This shows that dim(E) $= dim(E^{**}) = n$, and since by Part (a), we know that $eval_{E}$ : $E \to E^{**}$ is injective, in fact, $eval_{E}$ : $E \to E^{**}$ is bijective (by Proposition 6.19).  When a vector space $E$ has infinite dimension, $E$ and its bidual $E^{**}$ are never isomorphic. When $E$ is of finite dimension and $(u_{1}, \dots  , u_{n})$ is a basis of $E$, in view of the canonical isomorphism $eval_{E}$ : $E \to E^{**}$, the basis $(u_{1}^{**} , \dots  , u_{n}^{**}$ ) of the bidual is identified with $(u_{1}, \dots  , u_{n})$. Proposition 11.5 can be reformulated very fruitfully in terms of pairings, a remarkably useful concept discovered by Pontrjagin in $1931$ (adapted from $E$. Artin $[6]$, Chapter $1)$. Given two vector spaces $E$ and $F$ over a field $K$, we say that a function $\phi$ : $E \times  F \to K$ is bilinear if for every $v \in V$ , the map $u \mapsto \phi (u, v)$ (from $E$ to $K)$ is linear, and for every $u \in E$, the map $v \mapsto \phi (u, v)$ (from $F$ to $K)$ is linear.

> **Definition 11.4.** Given two vector spaces $E$ and $F$ over $K$, a pairing between $E$ and $F$ is a bilinear map $\phi$ : $E \times  F \to K$. Such a pairing is nondegenerate iff

<!-- PAGE 434 -->
$(1)$ for every $u \in E$, if $\phi (u, v) = 0$ for all $v \in F$, then $u = 0$, and
$(2)$ for every $v \in F$, if $\phi (u, v) = 0$ for all $u \in E$, then $v = 0$. A pairing $\phi$ : $E \times  F \to K$ is often denoted by $\langle$ -, $-\rangle$ : $E \times  F \to K$. For example, the map $\langle$ -, $-\rangle$ : $E^{*} \times  E \to K$ defined earlier is a nondegenerate pairing (use the proof of (a) in Proposition 11.5). If $E = F$ and $K = \mathbb{R}$, any inner product on $E$ is a nondegenerate pairing (because an inner product is positive definite); see Chapter $12$. Other interesting nondegenerate pairings arise in exterior algebra and differential geometry. Given a pairing $\phi$ : $E \times  F \to K$, we can define two maps $l_{\phi}$ : $E \to F^{*}$ and $r_{\phi}$ : $F \to E^{*}$ as follows: For every $u \in E$, we define the linear form $l_{\phi}(u)$ in $F^{*}$ such that
$$l_{\phi}(u)(y) = \phi (u, y)for every y \in F,$$
and for every $v \in F$, we define the linear form $r_{\phi}(v)$ in $E^{*}$ such that
$$r_{\phi}(v)(x) = \phi (x, v)for every x \in E.$$
We have the following useful proposition.

> **Proposition 11.6.** Given two vector spaces $E$ and $F$ over $K$, for every nondegenerate pairing $\phi$ : $E \times  F \to K$ between $E$ and $F$, the maps $l_{\phi}$ : $E \to F^{*}$ and $r_{\phi}$ : $F \to E^{*}$ are linear and injective. Furthermore, if $E$ and $F$ have finite dimension, then this dimension is the same and $l_{\phi}$ : $E \to F^{*}$ and $r_{\phi}$ : $F \to E^{*}$ are bijections.

*Proof.* The maps $l_{\phi}$ : $E \to F^{*}$ and $r_{\phi}$ : $F \to E^{*}$ are linear because a pairing is bilinear. If $l_{\phi}(u) = 0$ (the null form), then
$$l_{\phi}(u)(v) = \phi (u, v) = 0for every v \in F,$$
and since $\phi$  is nondegenerate, $u = 0$. Thus, $l_{\phi}$ : $E \to F^{*}$ is injective. Similarly, $r_{\phi}$ : $F \to E^{*}$ is injective. When $F$ has finite dimension $n$, we have seen that $F$ and $F^{*}$ have the same dimension. Since $l_{\phi}$ : $E \to F^{*}$ is injective, we have $m =$ dim(E) $\le$ dim(F) $= n$. The same argument applies to $E$, and thus $n =$ dim(F) $\le$ dim(E) $= m$. But then, dim(E) $=$ dim(F), and $l_{\phi}$ : $E \to F^{*}$ and $r_{\phi}$ : $F \to E^{*}$ are bijections. When $E$ has finite dimension, the nondegenerate pairing $\langle$ -, $-\rangle$ : $E^{*} \times  E \to K$ yields another proof of the existence of a natural isomorphism between $E$ and $E^{**}$. When $E = F$, the nondegenerate pairing induced by an inner product on $E$ yields a natural isomorphism between $E$ and $E^{*}$ (see Section 12.2). We now show the relationship between hyperplanes and linear forms.
