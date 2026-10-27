# Existence of Solutions of an Optimization Problem


<!-- PAGE 1707 -->

## 49.2 Existence of Solutions of an Optimization

$$Problem$$
We begin with the case where $U$ is a closed but possibly unbounded subset of $\mathbb{R}^{n}$. In this case the following type of functions arise.

> **Definition 49.1.** A real-valued function $J$ : $V \to \mathbb{R}$ defined on a normed vector space $V$ is coercive iff for any sequence $(v_{k})_{k\ge1}$ of vectors $v_{k} \in V$ , if $lim_{k\mapsto \infty} \|v_{k}\| = \infty$ , then
$$limJ(v_{k}) = +\infty .$$
$$k\mapsto \infty$$
For example, the function f(x) $= x^{2}+2x$ is coercive, but an affine function f(x) $= ax+b$ is not.
$$\mathbb{R}^{n} \mathbb{R}^{n} \mathbb{R}$$

> **Proposition 49.1.** Let $U$ be a nonempty, closed subset of , and let $J$ : $\to$  be a continuous function which is coercive if $U$ is unbounded. Then there is a least one element $\mathbb{R}^{n} u \in$ such that
$$u \in UandJ(u) = \inf J(v).$$
$$v\in U$$

*Proof.* Since $U \neq  \emptyset$ , pick any $u_{0} \in U$. Since $J$ is coercive, there is some $r > 0$ such that for all $v \in \mathbb{R}^{n}$, if $\|v\| > r$ then $J(u_{0}) <$ J(v). It follows that $J$ is minimized over the set
$$\mathbb{R}^{n}$$
$$U_{0} = U \cap {v \in | \|v\|\le r}.$$
$$\mathbb{R}^{n}$$
Since $U$ is closed and since the closed ball ${v \in$ | $\|v\|\le r}$ is compact, $U_{0}$ is compact, but we know that any continuous function on a compact set has a minimum which is achieved. The key point in the above proof is the fact that $U_{0}$ is compact. In order to generalize Proposition 49.1 to the case of an infinite dimensional vector space, we need some additional assumptions, and it turns out that the convexity of $U$ and of the function $J$ is sufficient. The key is that convex, closed and bounded subsets of a Hilbert space are “weakly compact.”

> **Definition 49.2.** Let $V$ be a Hilbert space. A sequence $(u_{k})_{k\ge1}$ of vectors $u_{k} \in V$ converges weakly if there is some $u \in V$ such that
$$lim\langle v, u_{k}\rangle = \langle v, u\rangle for every v \in V .$$
$$k\mapsto \infty$$
Recall that a Hibert space is separable if it has a countable Hilbert basis (see Definition A.4). Also, in a Euclidean space (of finite dimension) $V$ , the inner product induces an isomorphism between $V$ and its dual $V^{*}$ . In our case, we need the isomorphism $\sharp$ from $V^{*}$ to $V$ defined such that for every linear form $\omega  \in V^{*}$ , the vector $\omega^{\sharp} \in V$ is uniquely defined by the equation
$$\omega (v) = \langle v, \omega^{\sharp} \rangle for all v \in V .$$

<!-- PAGE 1708 -->
$$\mathbb{R}$$
In a Hilbert space, the dual space V' is the set of all continuous linear forms $\omega$ : $V \to$ , and the existence of the isomorphism $\sharp$ between V' and $V$ is given by the Riesz representation theorem; see Proposition 48.9. This theorem allows a generalization of the notion of gradient. Indeed, if $f$ : $V \to \mathbb{R}$ is a function defined on the Hilbert space $V$ and if $f$ is differentiable at some point $u \in V$ , then by definition, the derivative $df_{u}$ : $V \to \mathbb{R}$ is a continuous linear form, so by the Riesz representation theorem (Proposition 48.9) there is a unique vector, denoted $\nabla f_{u} \in V$ , such that
$$df_{u}(v) = \langle v, \nabla f_{u}\rangle for all v \in V .$$

> **Definition 49.3.** The unique vector $\nabla f_{u}$ such that
$$df_{u}(v) = \langle v, \nabla f_{u}\rangle for all v \in V$$
is called the gradient of $f$ at $u$. Similarly, since the second derivative $D^{2}f_{u}$ : $V \to$ V' of $f$ induces a continuous symmetric bilinear form from $V \times V to\mathbb{R}$, by Proposition 48.10, there is a unique continuous self-adjoint linear map $\nabla^{2} f_{u}$ : $V \to V$ such that
$$D^{2}f_{u}(v, w) = \langle \nabla^{2} f_{u}(v), w\rangle for all v, w \in V .$$
The map $\nabla^{2} f_{u}$ is a generalization of the Hessian. The next theorem is a rather general result about the existence of minima of convex functions defined on convex domains. The proof is quite involved and can be omitted upon first reading.

> **Theorem 49.2.** Let $U$ be a nonempty, convex, closed subset of a separable Hilbert space $V$ , and let $J$ : $V \to \mathbb{R}$ be a convex, differentiable function which is coercive if $U$ is unbounded. Then there is a least one element $u \in V$ such that
$$u \in UandJ(u) = \inf J(v).$$
$$v\in U$$

*Proof.* As in the proof of Proposition 49.1, since the function $J$ is coercive, we may assume that $U$ is bounded and convex (however, if $V$ infinite dimensional, then $U$ is not compact in general). The proof proceeds in four steps. Step $1$. Consider a minimizing sequence $(u_{k})_{k\ge0}$, namely a sequence of elements $u_{k} \in V$ such that
$$u_{k} \in Ufor all k \ge 0,limJ(u_{k}) = \inf J(v).$$
$$k\mapsto \infty v\in U$$
At this stage, it is possible that $inf_{v\in U}$ J(v) $= -\infty$ , but we will see that this is actually impossible. However, since $U$ is bounded, the sequence $(u_{k})_{k\ge0}$ is bounded. Our goal is to prove that there is some subsequence of $(w_{\ell})_{\ell\ge0}$ of $(u_{k})_{k\ge0}$ that converges weakly. Since the sequence $(u_{k})_{k\ge0}$ is bounded there is some constant $C > 0$ such that $\|u_{k}\|\le C$ for all $k \ge 0$. Then by the Cauchy–Schwarz inequality, for every $v \in V$ we have
$$|\langle v, u_{k}\rangle | \le \|v\|\|u_{k}\|\le C \|v\|,$$

<!-- PAGE 1709 -->
which shows that the sequence $(\langle v, u_{k}\rangle )_{k\ge0}$ is bounded. Since $V$ is a separable Hilbert space, there is a countable family $(v_{k})_{k\ge0}$ of vectors $v_{k} \in V$ which is dense in $V$ . Since the sequence $(\langle v_{1}, u_{k}\rangle )_{k\ge0}$ is bounded (in $\mathbb{R})$, we can find a convergent subsequence $(\langle v_{1}, u_{i1(j)}\rangle )_{j\ge0}$. Similarly, since the sequence $(\langle v_{2}, u_{i1(j)}\rangle )_{j\ge0}$ is bounded, we can find a convergent subsequence $(\langle v_{2}, u_{i2(j)}\rangle )_{j\ge0}$, and in general, since the sequence $(\langle v_{k}, u_{ik-1(j)}\rangle )_{j\ge0}$ is bounded, we can find a convergent subsequence $(\langle v_{k}, u_{ik(j)}\rangle )_{j\ge0}$. We obtain the following infinite array:
$$\begin{pmatrix} \langle v_{1}, u_{i1(1)}\rangle & \langle v_{2}, u_{i2(1)}\rangle & \cdots & \langle v_{k}, u_{ik(1)}\rangle & \cdots \\ \langle v_{1}, u_{i1(2)}\rangle & \langle v_{2}, u_{i2(2)}\rangle & \cdots & \langle v_{k}, u_{ik(2)}\rangle & \cdots \\ \vdots & \vdots & \vdots & \vdots & \vdots \\ \langle v_{1}, u_{i1(k)}\rangle & \langle v_{2}, u_{i2(k)}\rangle & \cdots & \langle v_{k}, u_{ik(k)}\rangle & \cdots \\ \vdots & \vdots & \vdots & \vdots & \vdots \end{pmatrix}$$
Consider the “diagonal” sequence $(w_{\ell})_{\ell\ge0}$ defined by
$$w_{\ell}= u_{i\ell(\ell)},\ell \ge 0.$$
We are going to prove that for every $v \in V$ , the sequence $(\langle v, w_{\ell}\rangle )_{\ell\ge0}$ has a limit. By construction, for every $k \ge 0$, the sequence $(\langle v_{k}, w_{\ell}\rangle )_{\ell\ge0}$ has a limit, which is the limit of the sequence $(\langle v_{k}, u_{ik(j)}\rangle )_{j\ge0}$, since the sequence $(i_{\ell}(\ell ))_{\ell\ge0}$ is a subsequence of every sequence $(i_{\ell}(j))_{j\ge0}$ for every $\ell \ge 0$. Pick any $v \in V$ and any $\epsilon  > 0$. Since $(v_{k})_{k\ge0}$ is dense in $V$ , there is some $v_{k}$ such that
$$\|v -v_{k}\|\le \epsilon /(4C).$$
Then we have
$$|\langle v, w_{\ell}\rangle -\langle v, w_{m}\rangle | = |\langle v, w_{\ell}-w_{m}\rangle |$$
$$= |\langle v_{k} + v -v_{k}, w_{\ell}-w_{m}\rangle |$$
$$= |\langle v_{k}, w_{\ell}-w_{m}\rangle + \langle v -v_{k}, w_{\ell}-w_{m}\rangle |$$
$$\le |\langle v_{k}, w_{\ell}\rangle -\langle v_{k}, w_{m}\rangle | + |\langle v -v_{k}, w_{\ell}-w_{m}\rangle |.$$
By Cauchy–Schwarz and since $\|w_{\ell}$ - $w_{m}\|\le \|w_{\ell}\| + \|w_{m}\|\le C + C =$ 2C,
$$|\langle v -v_{k}, w_{\ell}-w_{m}\rangle | \le \|v -v_{k}\|\|w_{\ell}-w_{m}\|\le (\epsilon /(4C))2C = \epsilon /2,$$
so
$$|\langle v, w_{\ell}\rangle -\langle v, w_{m}\rangle | \le |\langle v_{k}, w_{\ell}-w_{m}\rangle | + \epsilon /2.$$
With the element $v_{k}$ held fixed, by a previous argument the sequence $(\langle v_{k}, w_{\ell}\rangle )_{\ell\ge0}$ converges, so it is a Cauchy sequence. Consequently there is some $\ell_{0}$  (depending on $\epsilon$  and $v_{k})$ such that
$$|\langle v_{k}, w_{\ell}\rangle -\langle v_{k}, w_{m}\rangle | \le \epsilon /2for all \ell , m \ge \ell_{0} ,$$

<!-- PAGE 1710 -->
so we get
$$|\langle v, w_{\ell}\rangle -\langle v, w_{m}\rangle | \le \epsilon /2 + \epsilon /2 = \epsilon for all \ell , m \ge \ell_{0} .$$
This proves that the sequence $(\langle v, w_{\ell}\rangle )_{\ell\ge0}$ is a Cauchy sequence, and thus it converges. Define the function $g: V \to \mathbb{R}$ by
$$g(v) = lim\langle v, w_{\ell}\rangle ,for all v \in V .$$
$$\ell \mapsto \infty$$
Since
$$|\langle v, w_{\ell}\rangle | \le \|v\|\|w_{\ell}\|\le C \|v\|for all \ell \ge 0,$$
we have
$$|g(v)| \le C \|v\|,$$
so $g$ is a continuous linear map. By the Riesz representation theorem (Proposition 48.9), there is a unique $u \in V$ such that
$$g(v) = \langle v, u\rangle for all v \in V ,$$
which shows that
$$lim\langle v, w_{\ell}\rangle = \langle v, u\rangle for all v \in V ,$$
$$\ell \mapsto \infty$$
namely the subsequence $(w_{\ell})_{\ell\ge0}$ of the sequence $(u_{k})_{k\ge0}$ converges weakly to $u \in V$ . Step $2$. We prove that the “weak limit” $u$ of the sequence $(w_{\ell})_{\ell\ge0}$ belongs to $U$. Consider the projection $p_{U}(u)$ of $u \in V$ onto the closed convex set $U$. Since $w_{\ell} \in U$, by Proposition 48.5(2) and the fact that $U$ is convex and closed, we have
$$\langle p_{U}(u) -u, w_{\ell}-p_{U}(u)\rangle \ge 0for all \ell \ge 0.$$
The weak convergence of the sequence $(w_{\ell})_{\ell\ge0}$ to $u$ implies that
$$0 \le lim\langle p_{U}(u) -u, w_{\ell}-p_{U}(u)\rangle = \langle p_{U}(u) -u, u -p_{U}(u)\rangle$$
$$\ell \mapsto \infty$$
$$= -\|p_{U}(u) -u\|\le 0,$$
so $\|p_{U}(u)$ - $u\| = 0$, which means that $p_{U}(u) = u$, and so $u \in U$. Step $3$. We prove that
$$J(v) \le lim infJ(z_{\ell})$$
$$\ell \mapsto \infty$$
for every sequence $(z_{\ell})_{\ell\ge0}$ converging weakly to some element $v \in V$ . Since $J$ is assumed to be differentiable and convex, by Proposition 40.11(1) we have
$$J(v) + \langle \nabla J_{v}, z_{\ell}-v\rangle \le J(z_{\ell})for all \ell \ge 0,$$
