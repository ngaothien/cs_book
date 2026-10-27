# Gradient Projection for Constrained Optimization


<!-- PAGE 1752 -->
The method of conjugate gradients can be generalized to functionals that are not necessarily quadratic. The stepsize parameter $\rho_{k}$  is still determined by a line search which consists in finding $\rho_{k}$  such that
$$J(u_{k} -\rho_{k} d_{k}) = \inf J(u_{k} -\rho d_{k}).$$
$$\rho \in \mathbb{R}$$
This is more difficult than in the quadratic case and in general there is no guarantee that $\rho_{k}$ is unique, so some criterion to pick $\rho_{k}$  is needed. Then
$$u_{k+1} = u_{k} -\rho_{k} d_{k},$$
and the next descent direction can be chosen in two ways:
$(1)$ (Polak–Ribi`ere)
$$\langle \nabla  \nabla  -\nabla \rangle$$
$$d_{k} = \nabla J_{uk} + \frac{J_{uk},J_{uk}J_{uk-1}}{\nabla J_{uk-1}^{2}} d_{k-1},$$
$(2)$ (Fletcher–Reeves)
$$\|\nabla \|^{2}$$
$$d_{k} = \nabla J_{uk} + \frac{J_{uk}}{\nabla J_{uk-1}^{2}} d_{k-1}.$$
Consecutive gradients are no longer orthogonal so these methods may run forever. There are various sufficient criteria for convergence. In practice, the Polak–Ribi`ere method converges faster. There is no longer any guarantee that these methods converge to a global minimum.

## 49.11 Gradient Projection Methods for Constrained

$$Optimization$$
We now consider the problem of finding the minimum of a convex functional $J$ : $V \to \mathbb{R}$ over a nonempty, convex, closed subset $U$ of a Hilbert space $V$ . By Theorem 40.13(3), the functional $J$ has a minimum at $u \in U$ iff
$$dJ_{u}(v -u) \ge 0for all v \in U,$$
which can be expressed as
$$\langle \nabla J_{u}, v -u\rangle \ge 0for all v \in U.$$
On the other hand, by the projection lemma (Proposition 48.5), the condition for a vector $u \in U$ to be the projection of an element $w \in V$ onto $U$ is
$$\langle u -w, v -u\rangle \ge 0for all v \in U.$$

<!-- PAGE 1753 -->
These conditions are obviously analogous, and we can make this analogy more precise as follows. If $p_{U}$ : $V \to U$ is the projection map onto $U$, we have the following chain of equivalences: $u \in U$ and J(u) $=$ inf J(v) iff
$$v\in U$$
$u \in U$ and $\langle \nabla J_{u}, v$ - $u\rangle \ge 0$ for every $v \in U$, iff $u \in U$ and $\langle u$ - $(u$ - $\rho \nabla J_{u}), v$ - $u\rangle \ge 0$ for every $v \in U$ and every $\rho  > 0$, iff $u = p_{U}(u$ - $\rho \nabla J_{u})$ for every $\rho  > 0$. In other words, for every $\rho  > 0, u \in V$ is a fixed-point of the function $g: V \to U$ given by
$$g(v) = p_{U}(v -\rho \nabla J_{v}).$$
The above suggests finding $u$ by the method of successive approximations for finding the fixed-point of a contracting mapping, namely given any initial $u_{0} \in V$ , to define the sequence $(u_{k})_{k\ge0}$ such that
$$u_{k+1} = p_{U}(u_{k} -\rho_{k} \nabla J_{uk}),$$
where the parameter $\rho_{k}  > 0$ is chosen at each step. This method is called the projectedgradient method with variable stepsize parameter. Observe that if $U = V$ , then this is just the gradient method with variable stepsize. We have the following result about the convergence of this method.

> **Proposition 49.18.** Let $J$ : $V \to \mathbb{R}$ be a continuously differentiable functional defined on a Hilbert space $V$ , and let $U$ be nonempty, convex, closed subset of $V$ . Suppose there exists two constants $\alpha  > 0$ and $M > 0$ such that
$$\langle \nabla J_{v} -\nabla J_{u}, v -u\rangle \ge \alpha  \|v -u\|^{2}for all u, v \in V ,$$
and
$$\|\nabla J_{v} -\nabla J_{u}\|\le M \|v -u\|for all u, v \in V .$$
If there exists two real nunbers a, $b \in \mathbb{R}$ such that
$$0 < a \le \rho_{k}  \le b \le \frac{2\alpha}{M^{2}} for all k \ge 0,$$
then the projected-gradient method with variable stepsize parameter converges. Furthermore, there is some constant $\beta  > 0$ (depending on $\alpha , M$, a, $b)$ such that
$$\beta  < 1and\|u_{k} -u\|\le \beta^{k} \|u_{0} -u\|,$$
where $u \in M$ is the unique minimum of $J$.

<!-- PAGE 1754 -->

*Proof.* For every $\rho_{k}  \ge 0$, define the function $g_{k}$ : $V \to U$ by
$$g_{k}(v) = p_{U}(v -\rho_{k} \nabla J_{v}).$$
By Proposition 48.6, the projection map $p_{U}$ has Lipschitz constant $1$, so using the inequalities assumed to hold in the proposition, we have $\|g_{k}(v_{1})$ - $g_{k}(v_{2})\|^{2} = \|p_{U}(v_{1}$ - $\rho_{k} \nabla J_{v1})$ - $p_{U}(v_{2}$ - $\rho_{k} \nabla J_{v2})\|^{2}$
$$\le \|(v_{1} -v_{2}) -\rho_{k} (\nabla J_{v1} -\nabla J_{v2})\|^{2}$$
$$= \|v_{1} -v_{2}\|^{2}-2\rho_{k} \langle \nabla J_{v1} -\nabla J_{v2}, v_{1} -v_{2}\rangle + \rho_{k}^{2}  \|\nabla J_{v1} -\nabla J_{v2}\|^{2}$$
$$\le \begin{pmatrix} 1 -2\alpha \rho_{k}  + M^{2}\rho_{k}^{2} \end{pmatrix} \|v_{1} -v_{2}\|^{2}.$$
As in the proof of Proposition 49.14, we know that if a and $b$ satisfy the conditions $0 < a \le \rho_{k}  \le b \le_{M2}^{2\alpha}$ , then there is some $\beta$  such that
$$\begin{pmatrix} 1 -2\alpha \rho_{k}  + M^{2} \end{pmatrix} \rho_{k}^{21/2} \le \beta  < 1for all k \ge 0.$$
Since the minimizing point $u \in U$ is a fixed point of $g_{k}$ for all $k$, by letting $v_{1} = u_{k}$ and $v_{2} = u$, we get
$$\|u_{k+1} -u\|= \|g_{k}(u_{k}) -g_{k}(u)\|\le \beta  \|u_{k} -u\|,$$
which proves the convergence of the sequence $(u_{k})_{k\ge0}$. In the case of an elliptic quadratic functional
$$J(v) = \frac{1}{2} \langle Av, a\rangle -\langle b, v\rangle$$
defined on $\mathbb{R}^{n}$, the reasoning just after the proof of Proposition 49.14 can be immediately adapted to show that convergence takes place as long as a, $b$ and $\rho_{k}$  are chosen such that
$$0 < a \le \rho_{k}  \le b \le \frac{2}{\lambda_{n}} .$$
In theory, Proposition 49.18 gives a guarantee of the convergence of the projected-gradient method. Unfortunately, because computing the projection $p_{U}(v)$ effectively is generally impossible, the range of practical applications of Proposition 49.18 is rather limited. One
$$exception is the case where U is a product \prod_{i}  m[a_{i}, b_{i}] of closed intervals (where a_{i} = -\infty$$
or $b_{i} = +\infty$ is possible). In this case, it is $not^{=1}$ hard to show that
$$a_{i}if w_{i} < a_{i}$$
$$$$
$$$$
$$p_{U}(w)_{i} =w_{i}if a_{i} \le w_{i} \le b_{i}$$
$$b_{i}if b_{i} < w_{i}.$$
$$$$
