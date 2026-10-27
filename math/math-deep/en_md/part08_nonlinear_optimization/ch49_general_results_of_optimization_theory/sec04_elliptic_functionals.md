# Elliptic Functionals


<!-- PAGE 1718 -->

## 49.4 Elliptic Functionals

We begin by defining the notion of an elliptic functional which generalizes the notion of a quadratic function defined by a symmetric positive definite matrix. Elliptic functionals are well adapted to the types of iterative methods described in this section and lend themselves well to an analysis of the convergence of these methods.

> **Definition 49.7.** Given a Hilbert space $V$ , a functional $J$ : $V \to \mathbb{R}$ is said to be elliptic if it is continuously differentiable on $V$ , and if there is some constant $\alpha  > 0$ such that
$$\langle \nabla J_{v} -\nabla J_{u}, v -u\rangle \ge \alpha  \|v -u\|^{2}for all u, v \in V .$$
The following proposition gathers properties of elliptic functionals that will be used later to analyze the convergence of various gradient descent methods.

> **Theorem 49.8.** Let $V$ be a Hilbert space.
$(1)$ An elliptic functional $J$ : $V \to \mathbb{R}$ is strictly convex and coercive. Furthermore, it satisfies the identity
$$J(v) -J(u) \ge \langle \nabla J_{u}, v -u\rangle + \frac{\alpha}{2} \|v -u\|^{2}for all u, v \in V .$$
$(2)$ If $U$ is a nonempty, convex, closed subset of the Hilbert space $V$ and if $J$ is an elliptic functional, then Problem $(P)$,
$$findu$$
$$such that u \in U and J(u) = \inf J(v)$$
$$v\in U$$
has a unique solution.
$(3)$ Suppose the set $U$ is convex and that the functional $J$ is elliptic. Then an element $u \in U$ is a solution of Problem $(P)$ if and only if it satisfies the condition
$$\langle \nabla J_{u}, v -u\rangle \ge 0for every v \in U$$
in the general case, or
$$\nabla J_{u} = 0 if U = V .$$
$(4) A$ functional $J$ which is twice differentiable in $V$ is elliptic if and only if
$$\langle \nabla^{2} J_{u}(w), w\rangle \ge \alpha  \|w\|^{2}for all u, w \in V .$$

<!-- PAGE 1719 -->

*Proof.* $(1)$ Since $J$ is a $C^{1}-function$, by Taylor’s formula with integral remainder in the case $m = 0$ (Theorem 39.26), we get
$$J(v) -J(u) = \int_{0}^{}  1dJ_{u+t(v-u)}(v -u)dt$$
$$= \int_{0}^{}  1\langle \nabla J_{u+t(v-u)}, v -u\rangle dt$$
$$= \langle \nabla J_{u}, v -u\rangle + \int_{0}^{}  1\langle \nabla J_{u+t(v-u)} -\nabla J_{u}, v -u\rangle dt$$
$$= \langle \nabla J_{u}, v -u\rangle + \int_{0}^{}  1 \frac{J_{u+t(v-u)}J_{u}, t(vu)}{t} \langle \nabla  -\nabla  -\rangle dt$$
$$1$$
$$\ge \langle \nabla J_{u}, v -u\rangle + \int_{0}^{}  \alpha t \|v -u\|^{2} dtsince J is elliptic$$
$$.$$
$$= \langle \nabla J_{u}, v -u\rangle + \frac{\alpha}{2} \|v -u\|^{2}$$
Using the inequality
$$J(v) -J(u) \ge \langle \nabla J_{u}, v -u\rangle + \frac{\alpha}{2} \|v -u\|^{2}for all u, v \in V ,$$
by Proposition 40.11(2), since
$$J(v) > J(u) + \langle \nabla J_{u}, v -u\rangle for all u, v \in V , v \neq  u,$$
the function $J$ is strictly convex. It is coercive because (using Cauchy–Schwarz)
$$J(v) \ge J(0) + \langle \nabla J_{0}, v\rangle + \frac{\alpha}{2} v\|^{2}$$
$$,$$
$$\ge J(0) -\|\nabla J_{0}\|\|v\|+ \frac{\|\alpha}{2} \|v\|^{2}$$
and the term $(-\|\nabla J_{0}\| +_{2}^{\alpha}  \|v\|) \|v\|$ goes to $+\infty$ when $\|v\|$ tends to $+\infty$ .
$(2)$ Since by $(1)$ the functional $J$ is coercive, by Theorem 49.2, Problem $(P)$ has a solution. Since $J$ is strictly convex, by Theorem 40.13(2), it has a unique minimum.
$(3)$ These are just the conditions of Theorem 40.13(3, $4)$.
$(4)$ If $J$ is twice differentiable, we showed in Section 39.6 that we have
$$-$$
$$D^{2}J_{u}(w, w) = D_{w}(DJ)(u) = \theta lim\mapsto 0 \frac{DJ_{u+\theta w}(w)DJ_{u}(w)}{\theta} ,$$
and since
$$D^{2}J_{u}(w, w) = \langle \nabla^{2} J_{u}(w), w\rangle$$
$$DJ_{u+\theta w}(w) = \langle \nabla J_{u+\theta w}, w\rangle$$
$$DJ_{u}(w) = \langle \nabla J_{u}, w\rangle ,$$

<!-- PAGE 1720 -->
and since $J$ is elliptic, for all $u, w \in V$ we can write
$$\langle \nabla  -\nabla \rangle$$
$$\langle \nabla^{2} J_{u}(w), w\rangle = \theta lim\mapsto 0 \frac{J_{u+\theta w}J_{u}, w}{\theta}$$
$$\langle \nabla  -\nabla \rangle$$
$$= \theta lim\mapsto 0 \frac{J_{u+\theta w}J_{u}, \theta w}{\theta^{2}}$$
$$\ge \theta  \|w\|^{2}.$$
Conversely, assume that the condition
$$\langle \nabla^{2} J_{u}(w), w\rangle \ge \alpha  \|w\|^{2}for all u, w \in V$$
holds. If we define the function $g: V \to \mathbb{R}$ by
$$g(w) = \langle \nabla J_{w}, v -u\rangle = dJ_{w}(v -u) = D_{v-u}J(w),$$
where $u$ and $v$ are fixed vectors in $V$ , then we have $dg_{u+\theta(v-u)}(v-u) = D_{v-u}g(u+\theta$ (v-u)) $= D_{v-u}D_{v-u}J(u+\theta$ (v-u)) $= D^{2}J_{u+\theta(v-u)}(v-u$, v-u) and we can apply the Taylor–MacLaurin formula (Theorem 39.25 with $m = 0)$ to $g$, and we get
$$\langle \nabla J_{v} -\nabla J_{u}, v -u\rangle = g(v) -g(u)$$
$$= dg_{u+\theta(v-u)}(v -u)(0 < \theta  < 1)$$
$$= D^{2}J_{u+\theta(v-u)}(v -u, v -u)$$
$$= \langle \nabla^{2} J_{u+\theta(v-u)}(v -u), v -u\rangle$$
$$\ge \alpha  \|v -u\|^{2},$$
which shows that $J$ is elliptic.
$$\mathbb{R}^{n} \mathbb{R}$$

> **Corollary 49.9.** If $J$ : $\to$  is a quadratic function given by
$$J(v) = \frac{1}{2} \langle Av, v\rangle -\langle b, v\rangle$$
(where $A$ is a symmetric $n \times  n$ matrix and $\langle$ -, $-\rangle$ is the standard Eucidean inner product), then $J$ is elliptic iff $A$ is positive definite. This a consequence of Theorem 49.8 because
$$\langle \nabla^{2} J_{u}(w), w\rangle = \langle Aw, w\rangle \ge \lambda_{1}  \|w\|^{2}$$
where $\lambda_{1}$  is the smallest eigenvalue of $A$; see Proposition 17.24 (Rayleigh–Ritz). Note that by Proposition 17.24 (Rayleigh–Ritz), we also have the folllowing corollary.
