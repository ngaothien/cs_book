# Dual of the Hard Margin Support Vector Machine


<!-- PAGE 1828 -->
$(2)$ Assume Problem (P' ) has some solution $u \in U$, and that $\Omega$ is convex (open), the functions $\phi_{i}  (1 \le i \le m)$ and $J$ are convex, differentiable at $u$, and that the constraints are qualified. Then Problem (D') has a solution $(\lambda , \eta$ ) $\in \mathbb{R}_{+}^{m} \times \mathbb{R}^{p}$, and J(u) $= G(\lambda , \eta$ ); that is, the duality gap is zero. In the next section we derive the dual function and the dual program of the optimization problem of Section 50.6 (Hard margin SVM), which involves both inequality and equality constraints. We also derive the KKT conditions associated with the dual program.

## 50.10 Dual of the Hard Margin Support Vector Ma-

$$chine$$
Recall the Hard margin SVM problem $(SVM_{h2})$:
$$,\mathbb{R}^{n}$$
$$minimize \frac{1}{2} \|w\|^{2}w \in$$
$$subject to$$
$$w^{\top}u_{i} -b \ge 1i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge 1j = 1, \dots  , q.$$
We proceed in six steps. Step $1$: Write the constraints in matrix form. The inequality constraints are written as
$$C \begin{pmatrix} w \\ b \end{pmatrix} \le d,$$
$$\mathbb{R}^{p+q}$$
where $C$ is a $(p + q) \times  (n + 1)$ matrix $C$ and $d \in$ is the vector given by
$$C = \begin{pmatrix} -u_{1}^{\top} & 1 \\ \vdots & \vdots \\ -u_{p}^{\top} & 1 \\ v_{1}^{\top} & -1 \\ \vdots & \vdots \\ v_{q}^{\top} & 1 \end{pmatrix} ,d = \begin{pmatrix} -1 \\ \vdots \\ -1 \end{pmatrix} = -1_{p+q}.$$
$$-$$
If we let $X$ be the $n \times  (p + q)$ matrix given by
$$X = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} ,$$

<!-- PAGE 1829 -->
then
$$C = \begin{pmatrix} 1_{p} \\ X^{\top}-1_{q} \end{pmatrix}$$
and so
$$C^{\top}= \begin{pmatrix} X \\ 1_{p}^{\top} & -1_{q}^{\top} \end{pmatrix} .$$
Step $2$: Write the objective function in matrix form. The objective function is given by
$$J(w, b) = \frac{1}{2} \begin{pmatrix} I_{n} & 0_{n} \\ 0_{n}^{\top} & 0 \end{pmatrix} \begin{pmatrix} w \\ b \end{pmatrix} .$$
$$\begin{pmatrix} w^{\top} & b \end{pmatrix}$$
Note that the corresponding matrix is symmetric positive semidefinite, but it is not invertible. Thus the function $J$ is convex but not strictly convex. Step $3$: Write the Lagrangian in matrix form. As in Example 50.7, we obtain the Lagrangian
$$L(w, b, \lambda , \mu ) = \frac{1}{2} \begin{pmatrix} w^{\top} & b \end{pmatrix} \begin{pmatrix} I_{n} & 0_{n} \\ 0_{n}^{\top} & 0 \end{pmatrix} \begin{pmatrix} w \\ b \end{pmatrix} - \begin{pmatrix} w^{\top} & b \end{pmatrix} \begin{pmatrix} \lambda \\ 0_{n+1} -C^{\top} & \mu \end{pmatrix} \begin{pmatrix}\end{pmatrix} + \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q},$$
that is,
$$L(w, b, \lambda , \mu ) = \frac{1}{2} \begin{pmatrix} I_{n} & 0_{n} \\ 0_{n}^{\top} & 0 \end{pmatrix} \begin{pmatrix} w \\ b \end{pmatrix} + \begin{pmatrix} \lambda \\ X & \mu \\ 1_{p}^{\top}\lambda \end{pmatrix} \begin{pmatrix} 1_{q}^{\top}\mu \end{pmatrix} +1_{p+q}.$$
$$\begin{pmatrix} w^{\top} & b \end{pmatrix} \begin{pmatrix} w^{\top} & b \end{pmatrix} - \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix}$$
Step $4$: Find the dual function $G(\lambda , \mu$ ). In order to find the dual function $G(\lambda , \mu$ ), we need to minimize L(w, $b, \lambda , \mu$ ) with respect
$$\mathbb{R}^{n+1}$$
to $w$ and $b$ and for this, since the objective function $J$ is convex and since is convex and open, we can apply Theorem 40.13, which gives a necessary and sufficient condition for a minimum. The gradient of L(w, $b, \lambda , \mu$ ) with respect to $w$ and $b$ is
$$\nabla L_{w,b} = \begin{pmatrix} I_{n} & 0_{n} \\ 0_{n}^{\top} & 0 \end{pmatrix} \begin{pmatrix} w \\ b \end{pmatrix} + \begin{pmatrix} \lambda \\ X & \mu \\ 1_{p}^{\top}\lambda \end{pmatrix} \begin{pmatrix} 1_{q}^{\top}\mu \end{pmatrix}$$
$$-$$
$$= \begin{pmatrix} w \\ 0 \end{pmatrix} + \begin{pmatrix} \lambda \\ X & \mu \\ 1_{p}^{\top}\lambda \end{pmatrix} \begin{pmatrix} 1_{q}^{\top}\mu \end{pmatrix} .$$
$$-$$
The necessary and sufficient condition for a minimum is
$$\nabla L_{w,b} = 0,$$

<!-- PAGE 1830 -->
which yields
$$w = -X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} (*_{1})$$
and
$$1_{p}^{\top} \lambda  -1_{q}^{\top} \mu  = 0.(*_{2})$$
The second equation can be written as
$$\sum_{i=1}^{p}  \lambda_{i}  = \sum_{j=1}^{q}  \mu_{j} .(*_{3})$$
Plugging back $w$ from $(*_{1})$ into the Lagrangian and using $(*_{2})$ we get
$$G(\lambda , \mu ) = - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q};(*_{4})$$
$$of course, \begin{pmatrix} \lambda^{\top} & \mu^{\top} \\ onthe \end{pmatrix} 1_{p+q} = \sum_{i}  p=1 \lambda_{i}  + \sum  q \mu_{j} . Actually, to be perfectly rigorous G(\lambda , \mu ) is$$
$$only defined   intersection  of the^{j=1} hyperplane of equation \sum_{i}  p \lambda_{i}  = \sum_{jq+}  q \mu_{j}  with the$$
convex octant in $\mathbb{R}^{p+q}$ given by $\lambda  \ge 0, \mu  \ge 0$, so for all $\lambda  \in \mathbb{R}_{+}^{p} and^{=1}$ all $\mu  \in \mathbb{R}^{=1}$, we have
$$!$$
$$\lambda$$
$$G(\lambda , \mu ) =-_{2}^{1} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X\mu + \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q}if \sum_{i}  p=1 \lambda_{i}  = \sum  qj=1 \mu_{j}$$
$$-\infty otherwise.$$
$$$$
Note that the condition
$$\sum_{i=1}^{p}  \lambda_{i}  = \sum_{j=1}^{q}  \mu_{j}$$
is Condition $(*_{2})$ of Example 50.6, which is not surprising. Step $5$: Write the dual program in matrix form. Maximizing the dual function $G(\lambda , \mu$ ) over its domain of definition is equivalent to maximizing
$$Gb(\lambda , \mu ) = - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q}$$
subject to the constraint
$$\sum_{i=1}^{p}  \lambda_{i}  = \sum_{j=1}^{q}  \mu_{j} ,$$

<!-- PAGE 1831 -->
so we formulate the dual program as,
$$maximize- \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  = \sum_{j=1}^{q}  \mu_{j}$$
$$\lambda  \ge 0, \mu  \ge 0,$$
or equivalently,
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  = \sum_{j=1}^{q}  \mu_{j}$$
$$\lambda  \ge 0, \mu  \ge 0.$$
The constraints of the dual program are a lot simpler than the constraints
$$\begin{pmatrix} 1_{p} \\ X^{\top}-1_{q} \end{pmatrix} \begin{pmatrix} w \\ b \end{pmatrix} \le -1_{p+q}$$
of the primal program because these constraints have been “absorbed” by the objective function $G(\lambda , \nu$ ) of the dual program which involves the matrix $X^{\top}X$. The matrix $X^{\top}X$ is
$$b$$
symmetric positive semidefinite, but not invertible in general. Step $6$: Solve the dual program. This step involves using numerical procedures typically based on gradient descent to find $\lambda$  and $\mu$ , for example, ADMM from Section 52.6. Once $\lambda$  and $\mu$  are determined, $w$ is determined by $(*_{1})$ and $b$ is determined as in Section 50.6 using the fact that there is at least some $i_{0}$ such that $\lambda_{i0}  > 0$ and some $j_{0}$ such that $\mu_{j0}  > 0$.
Remarks:
$(1)$ Since the constraints are affine and the objective function is convex, by Theorem 50.19(2) the duality gap is zero, so for any minimum $w$ of J(w, $b) = (1/2)w^{\top}w$ and any maximum $(\lambda , \mu$ ) of $G$, we have
$$J(w, b) = \frac{1}{2} w^{\top}w = G(\lambda , \mu ).$$

<!-- PAGE 1832 -->
But by $(*_{1})$
$$w = -X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = \sum_{i=1}^{p}  \lambda_{i} u_{i} - \sum_{j=1}^{q}  \mu_{j} v_{j},$$
so
$$\begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = w^{\top}w,$$
and we get
$$\frac{1}{2} w^{\top}w = - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q} = - \frac{1}{2} w^{\top}w + \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q},$$
so
$$w^{\top}w = \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q} = \sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j} ,$$
which yields
$$!$$
$$G(\lambda , \mu ) = \frac{1}{2} \sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j} .$$
The above formulae are stated in Vapnik $[188]$ (Chapter $10$, Section $1)$.
$(2)$ It is instructive to compute the Lagrangian of the dual program and to derive the KKT conditions for this Lagrangian. The conditions $\lambda  \ge 0$ being equivalent to $-\lambda  \le 0$, and the conditions $\mu  \ge 0$ being equivalent to $-\mu  \le 0$, we introduce Lagrange multipliers $\alpha  \in \mathbb{R}_{+}^{p}$ and $\beta  \in \mathbb{R}_{+}^{q}$ as well as a multiplier $\rho  \in \mathbb{R}$ for the equational constraint, and we form the Lagrangian
$$L(\lambda , \mu , \alpha , \beta , \rho ) = \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q}$$
$$- \sum_{i=1}^{p}  \alpha_{i} \lambda_{i}  - \sum_{j=1}^{q}  \beta_{j} \mu_{j}  + \rho \begin{pmatrix} \mu_{j} - & \lambda_{i} \end{pmatrix} \sum_{j=1}^{q}  \sum_{i=1}^{p}  .$$
It follows that the KKT conditions are
$$X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -1_{p+q} - \begin{pmatrix} \alpha \\ \beta \end{pmatrix} + \rho \begin{pmatrix} -1_{p} \\ 1_{q} \end{pmatrix} = 0_{p+q},(*_{4})$$
and $\alpha_{i} \lambda_{i}  = 0$ for $i = 1, \dots  , p$ and $\beta_{j} \mu_{j}  = 0$ for $j = 1, \dots  , q$. But $(*_{4})$ is equivalent to
$$-X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + \rho \begin{pmatrix} 1_{p} \\ -1_{q} \end{pmatrix} + 1_{p+q} + \begin{pmatrix} \alpha \\ \beta \end{pmatrix} = 0_{p+q},$$
