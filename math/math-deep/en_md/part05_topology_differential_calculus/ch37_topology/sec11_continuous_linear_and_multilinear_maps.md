# Continuous Linear and Multilinear Maps


<!-- PAGE 1421 -->
Finally we need to prove that if $(X, d)$ is compact, then $(\mathcal{K}(X), D)$ is compact. Since we already know that $(\mathcal{K}(X), D)$ is complete if $(X, d)$ is, it is enough to prove that $(\mathcal{K}(X), D)$ is totally bounded if $(X, d)$ is, which is not hard. In view of Theorem 37.55 and Theorem 37.54, it is possible to define some nonempty compact subsets of $X$ in terms of fixed points of contraction maps. This can be done in terms of iterated function systems, yielding a large class of fractals. However, we will omit this topic and instead refer the reader to Edgar $[56]$. In Chapter $38$ we show how certain fractals can be defined by iterated function systems, using Theorem 37.55 and Theorem 37.54. Before considering differentials, we need to look at the continuity of linear maps.

## 37.11 Continuous Linear and Multilinear Maps

If $E$ and $F$ are normed vector spaces, we first characterize when a linear map $f$ : $E \to F$ is continuous.

> **Proposition 37.56.** Given two normed vector spaces $E$ and $F$, for any linear map $f$ : $E \to F$, the following conditions are equivalent:
$(1)$ The function $f$ is continuous at $0$.
$(2)$ There is a constant $k \ge 0$ such that,
$$\|f(u)\|\le k, for every u \in E such that \|u\|\le 1.$$
$(3)$ There is a constant $k \ge 0$ such that,
$$\|f(u)\|\le k\|u\|, for every u \in E.$$
$(4)$ The function $f$ is continuous at every point of $E$.

*Proof.* Assume $(1)$. Then for every $\epsilon  > 0$, there is some $\eta  > 0$ such that, for every $u \in E$, if $\|u\|\le \eta$ , then $\|f(u)\|\le \epsilon$ . Pick $\epsilon  = 1$, so that there is some $\eta  > 0$ such that, if $\|u\|\le \eta$ , then $\|f(u)\|\le 1$. If $\|u\|\le 1$, then $\|\eta u\|\le \eta \|u\|\le \eta$ , and so, $\|f(\eta u)\|\le 1$, that is, $\eta \|f(u)\|\le 1$, which implies $\|f(u)\|\le \eta^{-1}$ . Thus, $(2)$ holds with $k = \eta^{-1}$ . Assume that $(2)$ holds. If $u = 0$, then by linearity, f(0) $= 0$, and thus $\|f(0)\|\le k\|0\|$ holds trivially for all $k \ge 0$. If $u \neq  0$, then $\|u\| > 0$, and since
$$\frac{u}{\|u\|} = 1,$$

<!-- PAGE 1422 -->
we have
$$$$
$$f \frac{u}{\|u\|} \le k,$$
which implies that
$$\|f(u)\|\le k\|u\|.$$
Thus, $(3)$ holds. If $(3)$ holds, then for all $u, v \in E$, we have
$$\|f(v) -f(u)\|= \|f(v -u)\|\le k\|v -u\|.$$
If $k = 0$, then $f$ is the zero function, and continuity is obvious. Otherwise, if $k > 0$, for every $\epsilon  > 0$, if $\|v$ - $u\|\le_{k}^{\epsilon}$ , then $\|f(v$ - $u)\|\le \epsilon$ , which shows continuity at every $u \in E$. Finally, it is obvious that $(4)$ implies $(1)$. Among other things, Proposition 37.56 shows that a linear map is continuous iff the image of the unit (closed) ball is bounded. Since a continuous linear map satisfies the condition $\|f(u)\|\le k\|u\|$ (for some $k \ge 0)$, it is also uniformly continuous. If $E$ and $F$ are normed vector spaces, the set of all continuous linear maps $f$ : $E \to F$ is denoted by $\mathcal{L}(E; F)$. Using Proposition 37.56, we can define a norm $on\mathcal{L}(E; F)$ which makes it into a normed vector space. This definition has already been given in Chapter $9$ (Definition 9.8) but for the reader’s convenience, we repeat it here.

> **Definition 37.41.** Given two normed vector spaces $E$ and $F$, for every continuous linear map $f$ : $E \to F$, we define the operator norm $\|f\|$ of $f$ as
$$\|f\|= \inf {k \ge 0 | \|f(x)\|\le k\|x\|, for all x \in E} = \sup {\|f(x)\|| \|x\|\le 1} .$$
From Definition 37.41, for every continuous linear map $f \in$ L(E; $F)$, we have
$$\|f(x)\|\le \|f\|\|x\|,$$
for every $x \in E$. It is easy to verify that $\mathcal{L}(E; F)$ is a normed vector space under the norm of Definition 37.41. Furthermore, if $E, F, G$, are normed vector spaces, and $f$ : $E \to F$ and $g: F \to G$ are continuous linear maps, we have
$$\|g \circ f\|\le \|g\|\|f\|.$$
$$\mathbb{R}^{n}  \mathbb{C}^{n}$$
We can now show that when $E =$ or $E =$ , with any of the norms $\|\|_{1}, \|\|_{2}$, or $\|\|_{\infty}$, then every linear map $f$ : $E \to F$ is continuous.
$$\mathbb{R}^{n} \mathbb{C}^{n}$$

> **Proposition 37.57.** If $E =$ or $E =$ , with any of the norms $\|\|_{1}, \|\|_{2}$, or $\|\|_{\infty}$, and $F$ is any normed vector space, then every linear map $f$ : $E \to F$ is continuous.

<!-- PAGE 1423 -->
$$\mathbb{R}^{n}  \mathbb{C}^{n}$$

*Proof.* Let $(e_{1}, \dots  , e_{n})$ be the standard basis of (a similar proof applies to ). In view of Proposition 9.3, it is enough to prove the proposition for the norm
$$\|x\|_{\infty}= \max{|x_{i}| | 1 \le i \le n}.$$
We have,
$$\|f(v) -f(u)\|= \|f(v -u)\|=f( \sum_{1\le i\le n}  (v_{i} -u_{i})e_{i}) = \sum_{1\le i\le n}  (v_{i} -u_{i})f(e_{i}) ,$$
and so,
$$\|f(v) -f(u)\|\le \begin{pmatrix} \|f(e_{i})\| \end{pmatrix} \sum_{1\le i\le n}  1max\le i\le n |v_{i} -u_{i}| = \begin{pmatrix} \|f(e_{i})\| \end{pmatrix} \sum_{1\le i\le n}  \|v -u\|_{\infty}.$$
By the argument used in Proposition 37.56 to prove that $(3)$ implies $(4), f$ is continuous. Actually, we proved in Theorem 9.6 that if $E$ is a vector space of finite dimension, then any two norms are equivalent, so that they define the same topology. This fact together with Proposition 37.57 prove the following:

> **Theorem 37.58.** If $E$ is a vector space of finite dimension (over $\mathbb{R}$ or $\mathbb{C})$, then all norms are equivalent (define the same topology). Furthermore, for any normed vector space $F$, every linear map $f$ : $E \to F$ is continuous.  If $E$ is a normed vector space of infinite dimension, a linear map $f$ : $E \to F$ may not be continuous. As an example, let $E$ be the infinite vector space of all polynomials over $\mathbb{R}$. Let
$$\|P(X)\|= \max |P(x)|.$$
$$0\le x\le 1$$
We leave as an exercise to show that this is indeed a norm. Let $F = \mathbb{R}$, and let $f$ : $E \to F$ be the map defined such that, f(P(X)) $=$ P(3). It is clear that $f$ is linear. Consider the sequence of polynomials
$$P_{n}(X) = \begin{pmatrix} X^{n} \\ \overline{2} \end{pmatrix} .$$
$$It is clear that \|P_{n}\| \begin{pmatrix} =_{2}^{1n} \end{pmatrix} , and thus, the sequence P_{n} has the null polynomial as a limit.$$
However, we have
$$3^{n}$$
$$f(P_{n}(X)) = P_{n}(3) = \begin{pmatrix} \overline{2} \end{pmatrix} ,$$
and the sequence $f(P_{n}(X))$ diverges to $+\infty$ . Consequently, in view of Proposition 37.15 $(1), f$ is not continuous.

<!-- PAGE 1424 -->
We now consider the continuity of multilinear maps. We treat explicitly bilinear maps, the general case being a straightforward extension.

> **Proposition 37.59.** Given normed vector spaces $E, F$ and $G$, for any bilinear map $f$ : $E \times F \to G$, the following conditions are equivalent:
$(1)$ The function $f$ is continuous at $\langle 0, 0\rangle$ . $2)$ There is a constant $k \ge 0$ such that,
$$\|f(u, v)\|\le k, for all u \in E, v \in F such that \|u\|, \|v\|\le 1.$$
$3)$ There is a constant $k \ge 0$ such that,
$$\|f(u, v)\|\le k\|u\|\|v\|, for all u \in E, v \in F.$$
$4)$ The function $f$ is continuous at every point of $E \times  F$.

*Proof.* It is similar to that of Proposition 37.56, with a small subtlety in proving that $(3)$ implies $(4)$, namely that two different $\eta$ ’s that are not independent are needed. In contrast to continuous linear maps, which must be uniformly continuous, nonzero continuous bilinear maps are not uniformly continuous. Let $f$ : $E \times  F \to G$ be a continuous bilinear map such that f(a, $b) \neq  0$ for some $a \in E$ and some $b \in F$. Consider the sequences $(u_{n})$ and $(v_{n})$ (with $n \ge 1)$ given by
$$u_{n} = (x_{n}, y_{n}) = (na, nb)$$
$$v_{n} = (x_{n}', y_{n}') = \begin{pmatrix}  & 1 \\ n + \\ n \end{pmatrix} \begin{pmatrix}  & 1 \\ a, & n + \\ n \end{pmatrix} \begin{pmatrix} b \end{pmatrix} .$$
Obviously
$$\|v_{n} -u_{n}\|\le \frac{1}{n} (\|a\|+ \|b\|),$$
so $lim_{n\mapsto \infty} \|v_{n}$ - $u_{n}\| = 0$. On the other hand
$$f(x_{n}', y_{n}') -f(x_{n}, y_{n}) = \begin{pmatrix} 1 \\ 2 + \\ n^{2} \end{pmatrix} f(a, b),$$
and thus $lim_{n\mapsto \infty} \|f(x_{n}', y_{n}')$ - $f(x_{n}, y_{n})\| = 2 \|f(a, b)\|̸ = 0$, which shows that $f$ is not uniformly continuous, because if this was the case, this limit would be zero. If $E, F$, and $G$, are normed vector spaces, we denote the set of all continuous bilinear maps $f$ : $E \times  F \to G$ by $\mathcal{L}_{2}(E, F; G)$. Using Proposition 37.59, we can define a norm on $\mathcal{L}_{2}(E, F; G)$ which makes it into a normed vector space.

<!-- PAGE 1425 -->

> **Definition 37.42.** Given normed vector spaces $E, F$, and $G$, for every continuous bilinear map $f$ : $E \times  F \to G$, we define the norm $\|f\|$ of $f$ as
$$\|f\|= \inf {k \ge 0 | \|f(x, y)\|\le k\|x\|\|y\|, for all x \in E, y \in F}$$
$$= \sup {\|f(x, y)\|| \|x\|, \|y\|\le 1} .$$
From Definition 37.41, for every continuous bilinear map $f \in L_{2}(E, F; G)$, we have
$$\|f(x, y)\|\le \|f\|\|x\|\|y\|,$$
for all $x, y \in E$. It is easy to verify that $\mathcal{L}_{2}(E, F; G)$ is a normed vector space under the norm of Definition 37.42. Given a bilinear map $f$ : $E \times  F \to G$, for every $u \in E$, we obtain a linear map denoted fu: $F \to G$, defined such that, fu(v) $=$ f(u, $v)$. Furthermore, since
$$\|f(x, y)\|\le \|f\|\|x\|\|y\|,$$
it is clear that fu is continuous. We can then consider the map $\phi$ : $E \to$ L(F; $G)$, defined such that, $\phi (u) =$ fu, for any $u \in E$, or equivalently, such that,
$$\phi (u)(v) = f(u, v).$$
Actually, it is easy to show that $\phi$  is linear and continuous, and that $\|\phi \| = \|f\|$. Thus, $f \mapsto \phi$ defines a map $from\mathcal{L}_{2}(E, F; G) to\mathcal{L}(E;\mathcal{L}(F; G))$. We can also go back $from\mathcal{L}(E;\mathcal{L}(F; G))$ to $\mathcal{L}_{2}(E, F; G)$. We summarize all this in the following proposition.

> **Proposition 37.60.** Let $E, F, G$ be three normed vector spaces. The map $f \mapsto \phi$ , from $\mathcal{L}_{2}(E, F; G)$ to $\mathcal{L}(E;\mathcal{L}(F; G))$, defined such that, for every $f \in L_{2}(E, F; G)$,
$$\phi (u)(v) = f(u, v),$$
is an isomorphism of vector spaces, and furthermore, $\|\phi \| = \|f\|$. As a corollary of Proposition 37.60, we get the following proposition which will be useful when we define second-order derivatives.

> **Proposition 37.61.** Let $E, F$ be normed vector spaces. The map app from $\mathcal{L}(E; F) \times  E$ to $F$, defined such that, for every $f \in$ L(E; $F)$, for every $u \in E$,
$$app(f, u) = f(u),$$
is a continuous bilinear map.

<!-- PAGE 1426 -->
Remark: If $E$ and $F$ are nontrivial, it can be shown that $\|app\| = 1$. It can also be shown that composition
$$\circ : \mathcal{L}(E; F) \times  L(F; G) \to L(E; G),$$
is bilinear and continuous. The above propositions and definition generalize to arbitrary n-multilinear maps, with $n \ge 2$. Proposition 37.59 extends in the obvious way to any n-multilinear map $f$ : $E_{1} \times \cdots \times E_{n} \to F$, but condition $(3)$ becomes: There is a constant $k \ge 0$ such that,
$$\|f(u_{1}, \dots  , u_{n})\|\le k\|u_{1}\|\cdots  \|u_{n}\|, for all u_{1} \in E_{1}, \dots  , u_{n} \in E_{n}.$$
Definition 37.42 also extends easily to
$$\|f\|= \inf {k \ge 0 | \|f(x_{1}, \dots  , x_{n})\|\le k\|x_{1}\|\cdots  \|x_{n}\|, for all x_{i} \in E_{i}, 1 \le i \le n}$$
$$= \sup {\|f(x_{1}, \dots  , x_{n})\|| \|x_{n}\|, \dots  , \|x_{n}\|\le 1} .$$
Proposition 37.60 is also easily extended, and we get an isomorphism between continuous n-multilinear maps in $\mathcal{L}_{n}(E_{1}, \dots  , E_{n}; F)$, and continuous linear maps in
$$\mathcal{L}(E_{1};\mathcal{L}(E_{2}; \dots  ;\mathcal{L}(E_{n}; F)))$$
An obvious extension of Proposition 37.61 also holds.

> **Definition 37.43.** A normed vector space $(E, \|\|) over\mathbb{R} (or\mathbb{C})$ which is a complete metric space for the distance d(u, $v) = \|v$ - $u\|$, is called a Banach space. The following theorem is a key result of the theory of Banach spaces worth proving.

> **Theorem 37.62.** If $E$ and $F$ are normed vector spaces, and if $F$ is a Banach space, then $\mathcal{L}(E; F)$ is a Banach space (with the operator norm).

*Proof.* Let $(f)_{n\ge1}$ be a Cauchy sequence of continuous linear maps $f_{n}$ : $E \to F$. We proceed in several steps. Step $1$. Define the pointwise limit $f$ : $E \to F$ of the sequence $(f_{n})_{n\ge1}$. Since $(f)_{n\ge1}$ is a Cauchy sequence, for every $\epsilon  > 0$, there is some $N > 0$ such that $\|f_{m}$ - $f_{n}\| < \epsilon$  for all $m, n \ge N$. Since $\|\|$ is the operator norm, we deduce that for any $u \in E$, we have $\|f_{m}(u)$ - $f_{n}(u)\| = \|(f_{m}$ - $f_{n})(u)\|\le \|f_{m}$ - $f_{n}\|\|u\|\le \epsilon  \|u\|$ for all $m, n \ge N$, that is,
$$\|f_{m}(u) -f_{n}(u)\|\le \epsilon  \|u\|for all m, n \ge N.(*_{1})$$

<!-- PAGE 1427 -->
If $u = 0$, then $f_{m}(0) = f_{n}(0) = 0$ for all $m, n$, so the sequence $(f_{n}(0))$ is a Cauchy sequence in $F$ converging to $0$. If $u \neq  0$, by replacing $\epsilon$  by $\epsilon / \|u\|$, we see that the sequence $(f_{n}(u))$ is a Cauchy sequence in $F$. Since $F$ is complete, the sequence $(f_{n}(u))$ has a limit which we denote by f(u). This defines our candidate limit function $f$ by
$$f(u) = limf_{n}(u).$$
$$n\mapsto \infty$$
It remains to prove that $1. f$ is linear. $2. f$ is continous. $3. f$ is the limit of $(f_{n})$ for the operator norm. Step $2$. The function $f$ is linear. Recall that in a normed vector space, addition and multiplication by a fixed scalar are continuous (since $\|u + v\|\le \|u\| + \|v\|$ and $\|\lambda u\|\le |\lambda$ | $\|u\|)$. Thus by definition of $f$ and since the $f_{n}$ are linear we have
$$f(u + v) = limf_{n}(u + v)by definition of f$$
$$n\mapsto \infty$$
$$= lim(f_{n}(u) + f_{n}(v))by linearity of f_{n}$$
$$n\mapsto \infty$$
$$= limf_{n}(u) + limf_{n}(v)since + is continuous$$
$$n\mapsto \infty n\mapsto \infty$$
$$= f(u) + f(v)by definition of f.$$
Similarly,
$$f(\lambda u) = limf_{n}(\lambda u)by definition of f$$
$$n\mapsto \infty$$
$$= lim\lambda f_{n}(u)by linearity of f_{n}$$
$$n\mapsto \infty$$
$$= \lambda  limf_{n}(u)by continuity of scalar multiplication$$
$$n\mapsto \infty$$
$$= \lambda f(u)by definition of f.$$
Therefore, $f$ is linear. Step $3$. The function $f$ is continuous. Since $(f_{n})_{n\ge1}$ is a Cauchy sequence, for every $\epsilon  > 0$, there is some $N > 0$ such that $\|f_{m}$ - $f_{n}\| < \epsilon$  for all $m, n \ge N$. Since $f_{m} = f_{n} + f_{m}$ - $f_{n}$, we get $\|f_{m}\|\le \|f_{n}\| + \|f_{m}$ - $f_{n}\|$, which implies that
$$\|f_{m}\|\le \|f_{n}\|+ \epsilon for all m, n \ge N.(*_{2})$$
