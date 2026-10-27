# Uzawa's Method


<!-- PAGE 1847 -->

## 50.13 Uzawa’s Method

Let us go back to our Minimization Problem
$$minimizeJ(v)$$
$$subject to \phi_{i} (v) \le 0,i = 1, \dots  , m,$$
where the functions $J$ and $\phi_{i}$  are defined on some open subset $\Omega$ of a finite-dimensional Euclidean vector space $V$ (more generally, a real Hilbert space $V$ ). As usual, let
$$U = {v \in V | \phi_{i} (v) \le 0, 1 \le i \le m}.$$
If the functional $J$ satisfies the inequalities of Proposition 49.18 and if the functions $\phi_{i}$  are convex, in theory, the projected-gradient method converges to the unique minimizer of $J$ over $U$. Unfortunately, it is usually impossible to compute the projection map $p_{U}$ : $V \to U$. On the other hand, the domain of the Lagrange dual function $G: \mathbb{R}_{+}^{m} \to \mathbb{R}$ given by
$$G(\mu ) = infL(v, \mu )\mu  \in \mathbb{R}_{+}^{m},$$
$$v\in \Omega$$
is $\mathbb{R}_{+}^{m}$, where
$$L(v, \mu ) = J(v) + \sum_{i=1}^{m}  \mu_{i} \phi_{i} (v)$$
$$\mathbb{R}^{m}  \mathbb{R}_{+}^{m}$$
is the Lagrangian of our problem. Now the projection $p_{+}$ from to  is very simple, namely
$$(p_{+}(\lambda ))_{i} = \max{\lambda_{i} , 0},1 \le i \le m.$$
It follows that the projection-gradient method should be applicable to the Dual Problem $(D)$:
$$maximizeG(\mu )$$
$$subject to \mu  \in \mathbb{R}_{+}^{m}.$$
If the hypotheses of Theorem 50.17 hold, then a solution $\lambda$  of the Dual Program $(D)$ yields a solution $u_{\lambda}$ of the primal problem. Uzawa’s method is essentially the gradient method with fixed stepsize applied to the Dual Problem $(D)$. However, it is designed to yield a solution of the primal problem. Uzawa’s method:
$$\mathbb{R}_{+}^{m}$$
Given an arbitrary initial vector $\lambda^{0} \in$ , two sequences $(\lambda^{k} )_{k\ge0}$ and $(u^{k})_{k\ge0}$ are con-
$$\mathbb{R}_{+}^{m}$$
structed, with $\lambda^{k} \in$  and $u^{k} \in V$ . Assuming that $\lambda^{0} , \lambda^{1} , \dots  , \lambda^{k}$ are known, $u^{k}$ and $\lambda^{k+1}$ are determined as follows:

<!-- PAGE 1848 -->
$u^{k}$ is the unique solution of the minimization problem, find $u^{k} \in V$ such that
$$J(u^{k}) + \sum_{i=1}^{m}  \lambda_{i}^{k}  \phi_{i} (u^{k}) = \inf \sum_{i=1}^{m}  ; and$$
$$(UZ)v\in V \begin{pmatrix} J(v) + & \lambda_{i}^{k} \phi_{i} (v) \end{pmatrix}$$
$$\lambda_{i}^{k+1} = \max{\lambda_{i}^{k}  + \rho \phi_{i} (u^{k}), 0},1 \le i \le m,$$
$$$$
where $\rho  > 0$ is a suitably chosen parameter. Recall that in the proof of Theorem 50.17 we showed $(*_{deriv})$, namely
$$G_{\lambda k}'(\xi ) = \langle \nabla G_{\lambda k}, \xi \rangle = \sum_{i=1}^{m}  \xi_{i} \phi_{i} (u^{k}),$$
which means that $(\nabla G_{\lambda k})_{i} = \phi_{i} (u^{k})$. Then the second equation in (UZ) corresponds to the gradient-projection step
$$\lambda^{k+1} = p_{+}(\lambda^{k} + \rho \nabla G_{\lambda k}).$$
Note that because the problem is a maximization problem we use a positive sign instead of a negative sign. Uzawa’s method is indeed a gradient method. Basically, Uzawa’s method replaces a constrained optimization problem by a sequence of unconstrained optimization problems involving the Lagrangian of the (primal) problem. Interestingly, under certain hypotheses, it is possible to prove that the sequence of approximate solutions $(u^{k})_{k\ge0}$ converges to the minimizer $u$ of $J$ over $U$, even if the sequence $(\lambda^{k} )_{k\ge0}$ does not converge. We prove such a result when the constraints $\phi_{i}$  are affine.
$$\mathbb{R}^{n} \mathbb{R}$$

> **Theorem 50.21.** Suppose $J$ : $\to$  is an elliptic functional, which means that $J$ is continuously differentiable on $\mathbb{R}^{n}$, and there is some constant $\alpha  > 0$ such that
$$\langle \nabla J_{v} -\nabla J_{u}, v -u\rangle \ge \alpha  \|v -u\|^{2}for all u, v \in \mathbb{R}^{n},$$
and that $U$ is a nonempty closed convex subset given by
$$\mathbb{R}^{n}$$
$$U = {v \in | Cv \le d},$$
where $C$ is a real $m \times  n$ matrix and $d \in \mathbb{R}^{m}$. If the scalar $\rho$  satisfies the condition
$$0 < \rho  < \frac{2\alpha}{\|C\|_{2}^{2}} ,$$
where $\|C\|_{2}$ is the spectral norm of $C$, then the sequence $(u^{k})_{k\ge0}$ computed by Uzawa’s method converges to the unique minimizer $u \in U$ of $J$. Furthermore, if $C$ has rank $m$, then the sequence $(\lambda^{k} )_{k\ge0}$ converges to the unique maximizer of the Dual Problem $(D)$.

<!-- PAGE 1849 -->

*Proof.* Step $1$. We establish algebraic conditions relating the unique minimizer $u \in U$ of $J$ over $U$ and some $\lambda  \in \mathbb{R}_{+}^{m}$ such that $(u, \lambda$ ) is a saddle point. Since $J$ is elliptic and $U$ is nonempty closed and convex, by Theorem 49.8, the functional $J$ is strictly convex, so it has a unique minimizer $u \in U$. Since $J$ is convex and the constraints are affine, by Theorem 50.17(2) the Dual Problem $(D)$ has at least one solution. By Theorem 50.15(2), there is some $\lambda  \in \mathbb{R}_{+}^{m}$ such that $(u, \lambda$ ) is a saddle point of the Lagrangian $L$. If we define the affine function $\phi$  by
$$\phi (v) = (\phi_{1} (v), \dots  , \phi_{m} (v)) = Cv -d,$$
then the Lagrangian L(v, $\mu$ ) can be written as
$$L(v, \mu ) = J(v) + \sum_{i=1}^{m}  \mu_{i} \phi_{i} (v) = J(v) + \langle C^{\top}\mu , v\rangle -\langle \mu , d\rangle .$$
Since
$$L(u, \lambda ) = \inf L(v, \lambda ),$$
$$v\in \mathbb{R} n$$
by Theorem 40.13(4) we must have
$$\nabla J_{u} + C^{\top}\lambda  = 0,(*_{1})$$
and since
$$G(\lambda ) = L(u, \lambda ) = supL(u, \mu ),$$
$$\mu \in \mathbb{R} m$$
$$+$$
by Theorem 40.13(3) (and since maximing a function $g$ is equivalent to minimizing $-g)$, we must have
$$G_{\lambda}'(\mu  -\lambda ) \le 0for all \mu  \in \mathbb{R}_{+}^{m},$$
and since as noted earlier $\nabla G_{\lambda} = \phi (u)$, we get
$$\langle \phi (u), \mu  -\lambda \rangle \le 0for all \mu  \in \mathbb{R}_{+}^{m}.(*_{2})$$
As in the proof of Proposition 49.18, $(*_{2})$ can be expressed as follows for every $\rho  > 0$:
$$\langle \lambda  -(\lambda  + \rho \phi (u)), \mu  -\lambda \rangle \ge 0for all \mu  \in \mathbb{R}_{+}^{m},(**_{2})$$
which shows that $\lambda$  can be viewed as the projection onto $\mathbb{R}_{+}^{m}$ of the vector $\lambda  + \rho \phi (u)$. In summary we obtain the equations
$$(\nabla$$
$$J_{u} + C^{\top}\lambda  = 0$$
$$(\dagger_{1} )$$
$$\lambda  = p_{+}(\lambda  + \rho \phi (u)).$$

<!-- PAGE 1850 -->
Step $2$. We establish algebraic conditions relating the unique solution $u_{k}$ of the minimization problem arising during an iteration of Uzawa’s method in (UZ) and $\lambda^{k}$ . Observe that the Lagrangian L(v, $\mu$ ) is strictly convex as a function of $v$ (as the sum of a strictly convex function and an affine function). As in the proof of Theorem 49.8(1) and using Cauchy–Schwarz, we have
$$+$$
$$J(v) + \langle C^{\top}\mu , v\rangle \ge J(0) + \langle \nabla J_{0}, v\rangle + \frac{\alpha}{2} \|v\|^{2} \langle C^{\top}\mu , v$$
$$,$$
$$\ge J(0) -\|\nabla J_{0}\|\|v\|-

$C^{\top}\mu$

$\|v\|+ \frac{\alpha \rangle}{2} \|v\|^{2}$$$ and the term $(-\|\nabla J_{0}\|-$

$C^{\top}\mu$

$\|v\| +_{2}^{\alpha}  \|v\|) \|v\|$ goes to $+\infty$ when $\|v\|$ tends to $+\infty$ , so L(v, $\mu$ ) is coercive as a function of $v$. Therefore, the minimization problem find $u^{k}$ such that
$$J(u^{k}) + \sum_{i=1}^{m}  \lambda_{i}^{k}  \phi_{i} (u^{k}) = vinf\in \mathbb{R} n \begin{pmatrix} J(v) + & \lambda_{i}^{k} \phi_{i} (v) \end{pmatrix} \sum_{i=1}^{m}$$
$$\mathbb{R}^{n}$$
has a unique solution $u^{k} \in$ . It follows from Theorem 40.13(4) that the vector $u^{k}$ must satisfy the equation
$$\nabla J_{uk} + C^{\top}\lambda^{k} = 0,(*_{3})$$
and since by definition of Uzawa’s method
$$\lambda^{k+1} = p_{+}(\lambda^{k} + \rho \phi (u^{k})),(*_{4})$$
we obtain the equations
$$($$
$$\nabla J_{uk} + C^{\top}\lambda^{k} = 0$$
$$(\dagger_{2} )$$
$$\lambda^{k+1} = p_{+}(\lambda^{k} + \rho \phi (u^{k})).$$
Step $3$. By subtracting the first of the two equations of $(\dagger_{1}$ ) and $(\dagger_{2}$ ) we obtain
$$\nabla J_{uk} -\nabla J_{u} + C^{\top}(\lambda^{k} -\lambda ) = 0,$$
and by subtracting the second of the two equations of $(\dagger_{1}$ ) and $(\dagger_{2}$ ) and using Proposition 48.6, we obtain
$$-

$\le$

- -

.$$
$$\lambda^{k+1} \lambda \lambda^{k} \lambda  + \rho C(u^{k}u)$$
In summary, we proved
$$($$
$$\nabla J_{uk} -\nabla J_{u} + C^{\top}(\lambda^{k} -\lambda ) = 0$$
$$(\dagger )$$
$$-

$\le$

- -

.$$
$$\lambda^{k+1} \lambda \lambda^{k} \lambda  + \rho C(u^{k}u)$$
Step $4$. Convergence of the sequence $(u^{k})_{k\ge0}$ to $u$.

<!-- PAGE 1851 -->
Squaring both sides of the inequality in $(\dagger$ ) we obtain
$$-  - + 2 - - .$$
$$\lambda^{k+1} \lambda^{2}

$\le$

$\lambda^{k} \lambda^{2}$

$\rho \langle C^{\top}(\lambda^{k} \lambda$ ), $u_{k} -u\rangle + \rho^{2}$

$C(u^{k}u)^{2}$$$ Using the equation in $(\dagger$ ) and the inequality
$$- ,$$
$$\langle \nabla J_{uk} -\nabla J_{u}, u^{k}-u\rangle \ge \alpha

$u^{k}u^{2}$$$ we get
$$-  - - - -$$
$$\lambda^{k+1} \lambda^{2}

$\le$

$\lambda^{k} \lambda^{2}$

$2\rho \langle \nabla J_{uk} -\nabla J_{u}, u^{k}u\rangle + \rho^{2}$

$C(u^{k}u)^{2}$$$
$$- - - .$$
$$\le

$\lambda^{k} \lambda^{2}$

$\rho (2\alpha  -\rho  \|C\|_{2}^{2})$

$u^{k}u^{2}$$$ Consequently, if
$$0 \le \rho  \le \frac{2\alpha}{\|C\|_{2}^{2}} ,$$
we have
$$-

$\le$

-

,$$
$$\lambda^{k+1} \lambda \lambda^{k} \lambda for all k \ge 0.(*_{5})$$
$$-$$
By $(*_{5})$, the sequence ( $\lambda^{k} \lambda )_{k\ge0}$ is nonincreasing and bounded below by $0$, so it converges, which implies that
$$

-

-

-$$
$$lim\lambda^{k+1} \lambda \lambda^{k} \lambda = 0,$$
$$k\mapsto \infty$$
and since
$$-  - - - ,$$
$$\lambda^{k+1} \lambda^{2}

$\le$

$\lambda^{k} \lambda^{2}$

$\rho (2\alpha  -\rho  \|C\|_{2}^{2})$

$u^{k}u^{2}$$$ we also have
$$-  - - - .$$
$$\rho (2\alpha  -\rho  \|C\|_{2}^{2})

$u^{k}u^{2}$

$\le$

$\lambda^{k} \lambda^{2}$



$\lambda^{k+1} \lambda^{2}$$$ So if
$$0 < \rho  < \frac{2\alpha}{\|C\|_{2}^{2}} ,$$
then $\rho (2\alpha$  - $\rho  \|C\|_{2}^{2}) > 0$, and we conclude that
$$-

$=$ 0$$
$$limu^{k}u,$$
$$k\mapsto \infty$$
that is, the sequence $(u^{k})_{k\ge0}$ converges to $u$. Step $5$. Convergence of the sequence $(\lambda^{k} )_{k\ge0}$ to $\lambda$  if $C$ has rank $m$.
$$-$$
Since the sequence ( $\lambda^{k} \lambda )_{k\ge0}$ is nonincreasing, the sequence $(\lambda^{k} )_{k\ge0}$ is bounded, and
$$\mathbb{R}_{+}^{m}$$
thus it has a convergent subsequence $(\lambda^{i(k)} )_{i\ge0}$ whose limit is some $\lambda' \in$ . Since J' is continuous, by $(\dagger_{2}$ ) we have
$$\nabla J_{u} + C^{\top}\lambda' = lim(\nabla J_{ui(k)} + C^{\top}\lambda^{i(k)} ) = 0.(*_{6})$$
$$i\mapsto \infty$$
If $C$ has rank $m$, then Im(C) $= \mathbb{R}^{m}$, which is equivalent to Ker $(C^{\top}) = (0)$, so $C^{\top}$ is injective and since by $(\dagger_{1}$ ) we also have $\nabla J_{u} +C^{\top}\lambda  = 0$, we conclude that $\lambda' = \lambda$ . The above reasoning applies to any subsequence of $(\lambda^{k} )_{k\ge0}$, so $(\lambda^{k} )_{k\ge0}$ converges to $\lambda$ .
