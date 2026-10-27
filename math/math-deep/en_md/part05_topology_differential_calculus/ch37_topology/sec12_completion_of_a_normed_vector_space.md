# Completion of a Normed Vector Space


<!-- PAGE 1428 -->
Using $(*_{2})$, we also have
$$\|f_{m}(u)\|\le \|f_{m}\|\|u\|\le (\|f_{n}\|+ \epsilon ) \|u\|for all m, n \ge N,$$
that is,
$$\|f_{m}(u)\|\le (\|f_{n}\|+ \epsilon ) \|u\|for all m, n \ge N.(*_{3})$$
Hold $n \ge N$ fixed and let $m$ tend to $+\infty$ in $(*_{3})$. Since the norm is continuous, we get
$$\|f(u)\|\le (\|f_{n}\|+ \epsilon ) \|u\|,$$
which shows that $f$ is continuous. Step $4$. The function $f$ is the limit of $(f_{n})$ for the operator norm. Recall $(*_{1})$:
$$\|f_{m}(u) -f_{n}(u)\|\le \epsilon  \|u\|for all m, n \ge N.(*_{1})$$
Hold $n \ge N$ fixed but this time let $m$ tend to $+\infty$ in $(*_{1})$. By continuity of the norm we get
$$\|f(u) -f_{n}(u)\|= \|(f -f_{n})(u)\|\le \epsilon  \|u\|.$$
By definition of the operator norm,
$$\|f -f_{n}\|= \sup{\|(f -f_{n})(u)\|| \|u\|= 1} \le \epsilon for all n \ge N,$$
which proves that $f_{n}$ converges to $f$ for the operator norm. As a special case of Theorem 37.62, if we let $F = \mathbb{R}$ (or $F = \mathbb{C}$ in the case of complex
$$\mathbb{R} \mathbb{C} \mathbb{R} \mathbb{C}$$
vector spaces) we see that E' $= \mathcal{L}(E$; ) (or E' $= \mathcal{L}(E$; )) is complete (since  and  are complete). The space E' of continuous linear forms on $E$ is called the dual of $E$. It is a subspace of the algebraic dual $E^{*}$ of $E$ which consists of all linear forms on $E$, not necessarily continuous. It can also be shown that if $E, F$ and $G$ are normed vector spaces, and if $G$ is a Banach space, then $\mathcal{L}_{2}(E, F; G)$ is a Banach space. The proof is essentially identical.

## 37.12 Completion of a Normed Vector Space

An easy corollary of Theorem 37.53 and Theorem 37.52 is that every normed vector space can be embedded in a complete normed vector space, that is, a Banach space.

> **Theorem 37.63.** If $(E, \|\|)$ is a normed vector space, then its completion (E,d) as a metric
$$b b$$
space (where $E$ is given the metric d(x, $y) = \|x$ - $y\|)$ can be given a unique vector space structure extending the vector space structure on $E$, and a norm $\|\|_{E}$, so that $(E, \|\|_{E})$ is a
$$b$$
$$bb$$
Banach space, and the metric $d$ is associated with the norm $\|\|_{E}$. Furthermore, the isometry
$$b$$
$$b$$
$\phi$ : $E \to E$ is a linear isometry.
$$b$$

<!-- PAGE 1429 -->

*Proof.* The addition operation $+: E \times  E \to E$ is uniformly continuous because
$$\|(u'+ v') -(u''+ v'')\|\le \|u'-u''\|+ \|v'-v''\|.$$
It is not hard to show that $E \times E$ is a complete metric space and that $E \times  E$ is dense
$$b b$$
in $E \times E$. Then, by Theorem 37.52, the uniformly continuous function $+$ has a unique $b  b$ continuous extension $+: E \times E \to E$.
$$b bb$$
The map $\cdot$ : $\mathbb{R} \times  E \to E$ is not uniformly continuous, but for any fixed $\lambda  \in \mathbb{R}$, the map $L_{\lambda}$ : $E \to E$ given by $L_{\lambda}(u) = \lambda  \cdot  u$ is uniformly continuous, so by Theorem 37.52 the function $L_{\lambda}$ has a unique continuous extension $L_{\lambda}$ : $E \to E$, which we use to define the scalar
$$bb$$
multiplication $\cdot$ : $\mathbb{R} \times E \to E$. It is easily checked that with the above addition and scalar
$$bb$$
multiplication, $E$ is a vector space.
$$b$$
Since the norm $\|\|$ on $E$ is uniformly continuous, it has a unique continuous extension $\|\|_{E}$ : $E \to \mathbb{R}_{+}$. The identities $\|u + v\|\le \|u\| + \|v\|$ and $\|\lambda u\|\le |\lambda$ | $\|u\|$ extend to $E$ by $b  b b$ continuity. The equation
$$d(u, v) = \|u -v\|$$
also extends to $E$ by continuity and yields
$$b$$
$$d(\alpha , \beta ) = \|\alpha  -\beta \|_{E},$$
$$b$$
$$b$$
which shows that $\|\|_{E}$ is indeed a norm, and that the metric $d$ is associated to it. Finally, it
$$b$$
is easy to verify $that^{b}$ the map $\phi$  is linear. The uniqueness of the structure of normed vector space follows from the uniqueness of continuous extensions in Theorem 37.52. Theorem 37.63 and Theorem 37.52 will be used to show that every Hermitian space can be embedded in a Hilbert space. The following version of Theorem 37.52 for normed vector spaces is needed in the theory of integration.

> **Theorem 37.64.** Let $E$ and $F$ be two normed vector spaces, let $E_{0}$ be a dense subspace of $E$, and let $f_{0}$ : $E_{0} \to F$ be a continuous function. If $f_{0}$ is uniformly continuous and if $F$ is complete, then there is a unique uniformly continuous function $f$ : $E \to F$ extending $f_{0}$. Furthermore, if $f_{0}$ is a continuous linear map, then $f$ is also a linear continuous map, and $\|f\| = \|f_{0}\|$.

*Proof.* We only need to prove the second statement. Given any two vectors $x, y \in E$, since $E_{0}$ is dense on $E$ we can pick sequences $(x_{n})$ and $(y_{n})$ of vectors $x_{n}, y_{n} \in E_{0}$ such that $x = lim_{n\mapsto \infty} x_{n}$ and $y = lim_{n\mapsto \infty} y_{n}$. Since addition and scalar multiplication are continuous, we get
$$x + y = lim(x_{n} + y_{n})$$
$$n\mapsto \infty$$
$$\lambda x = lim(\lambda x_{n})$$
$$n\mapsto \infty$$

<!-- PAGE 1430 -->
for any $\lambda  \in \mathbb{R}$ (or $\lambda  \in \mathbb{C})$. Since f(x) is defined by
$$f(x) = limf_{0}(x_{n})$$
$$n\mapsto \infty$$
independently of the sequence $(x_{n})$ converging to $x$, and similarly for f(y) and f(x $+ y)$, since $f_{0}$ is linear, we have
$$f(x + y) = limf_{0}(x_{n} + y_{n})$$
$$n\mapsto \infty$$
$$= lim(f_{0}(x_{n}) + f_{0}(y_{n}))$$
$$n\mapsto \infty$$
$$= limf_{0}(x_{n}) + limf_{0}(y_{n})$$
$$n\mapsto \infty n\mapsto \infty$$
$$= f(x) + f(y).$$
Similarly,
$$f(\lambda x) = limf_{0}(\lambda x_{n})$$
$$n\mapsto \infty$$
$$= lim\lambda f_{0}(x_{n})$$
$$n\mapsto \infty$$
$$= \lambda  limf_{0}(x_{n})$$
$$n\mapsto \infty$$
$$= \lambda f(x).$$
Therefore, $f$ is linear. Since the norm is continuous, we have
$$\|f(x)\|= limf_{0}(x_{n}) = lim\|f_{0}(x_{n})\|,$$
$$n\mapsto \infty n\mapsto \infty$$
and since $f_{0}$ is continuous
$$\|f_{0}(x_{n})\|\le \|f_{0}\|\|x_{n}\|for all n \ge 1,$$
so we get
$$lim\|f_{0}(x_{n})\|\le lim\|f_{0}\|\|x_{n}\|for all n \ge 1,$$
$$n\mapsto \infty n\mapsto \infty$$
that is,
$$\|f(x)\|\le \|f_{0}\|\|x\|.$$
Since
$$\|f\|=\sup\|f(x)\|,$$
$$\|x\|=1, x\in E$$
we deduce that $\|f\|\le \|f_{0}\|$. But since $E_{0} \subseteq E$ and $f$ agrees with $f_{0}$ on $E_{0}$, we also have
$$\|f_{0}\|=\sup\|f_{0}(x)\|=\sup\|f(x)\|\le \sup\|f(x)\|= \|f\|,$$
$$\|x\|=1, x\in E0\|x\|=1, x\in E0\|x\|=1, x\in E$$
and thus $\|f\| = \|f_{0}\|$. Finally, we consider normed affine spaces.
