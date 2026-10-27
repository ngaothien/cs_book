# Solving Hard Margin (SVMh2) Using ADMM


<!-- PAGE 1932 -->
We see immediately that the constraints
$$x + y -z = 0$$
$$x -y -z = 0$$
imply that $z = x$ and $y = 0$. Then it is easy using calculus to find that the unique minimum is given by $(x, y, z) = (1, 0, 1)$. Running qsolve1 on $P_{1}, q_{1}, A_{1}, b_{1}$ with $\rho  = 10$, tolr $=$ tols $= 10^{-12}$ and iternum $= 10000$, we find that after $83$ iterations the primal and the dual residuals are less than $10^{-12}$, and we get
$$(x, y, z) = (1.000000000000149, 0.000000000000000, 1.000000000000148).$$

> **Example 52.12.** Consider the quadratic program for which
$$P_{2} = \begin{pmatrix} 4 & 1 & 0 & 0 \\ 1 & 4 & 1 & 0 \\ 0 & 1 & 4 & 1 \\ 0 & 0 & 1 & 4 \end{pmatrix} q_{2} = - \begin{pmatrix} 4 \\ 4 \\ 4 \\ 4 \end{pmatrix}$$
$$A_{2} = \begin{pmatrix} 1 & 1 & -1 & 0 \\ 1 & -1 & -1 & 0 \end{pmatrix} b_{2} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} .$$
Again, we see immediately that the constraints imply that $z = x$ and $y = 0$. Then it is easy using calculus to find that the unique minimum is given by $(x, y, z) = (28/31, 0, 28/31, 24/31)$. Running qsolve1 on $P_{2}, q_{2}, A_{2}, b_{2}$ with $\rho  = 10$, tolr $=$ tols $= 10^{-12}$ and iternum $= 10000$, we find that after $95$ iterations the primal and the dual residuals are less than $10^{-12}$, and we get $(x, y, z, t) =$ (0.903225806451495, 0.000000000000000, 0.903225806451495,
$$0.774193548387264),$$
which agrees with the answer found earlier up to $11$ decimals. As an illustration of the wide range of applications of ADMM we show in the next section how to solve the hard margin SVM $(SVM_{h2})$ discussed in Section 50.6.

## 52.7 Solving Hard Margin (SVM ) Using ADMM

$$h2$$
Recall that we would like to solve the following optimization problem (see Section 50.6): Hard margin SVM $(SVM_{h2})$:
$$minimize \frac{1}{2} \|w\|^{2}$$
$$subject to$$
$$w^{\top}u_{i} -b \ge 1i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge 1j = 1, \dots  , q.$$

<!-- PAGE 1933 -->
The margin is $\delta  = 1/ \|w\|$. The separating hyperplane $H_{w,b}$ is the hyperplane of equation $w^{\top}x$ - $b = 0$, and the margin hyperplanes are the hyperplanes $H_{w,b+1}$ (the blue hyperplane) of equation $w^{\top}x$ - $b$ - $1 = 0$ and $H_{w,b-1}$ (the red hyperplane) of equation $w^{\top}x$ - $b + 1 = 0$. The dual program derived in Section 50.10 is the following program: Dual of the Hard margin SVM $(SVM_{h2})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\lambda  \ge 0, \mu  \ge 0,$$
where $X$ is the $n \times  (p + q)$ matrix given by
$$X = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} .$$
Then $w$ is determined as follows:
$$w = -X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = \sum_{i=1}^{p}  \lambda_{i} u_{i} - \sum_{j=1}^{q}  \mu_{j} v_{j}.$$
To solve the dual using ADMM we need to determine the matrices $P, q A$ and $c$ as in Section 52.6(2). We renamed $b$ as $c$ to avoid a clash since $b$ is already used. We have
$$P = X^{\top}X,q = -1_{p+q},$$
and since the only constraint is
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0,$$
the matrix $A$ is the $1 \times  (p + q)$ row vector
$$A = \begin{pmatrix} 1_{p}^{\top} & -1_{q}^{\top} \end{pmatrix} ,$$
and the right-hand side $c$ is the scalar
$$c = 0.$$
Obviously the matrix $A$ has rank $1$. We obtain $b$ using any $i_{0}$ such that $\lambda_{i0}  > 0$ and any $j_{0}$ such that $\mu_{j0}  > 0$. Since the corresponding constraints are active, we have
$$w^{\top}u_{i0} -b = 1,-w^{\top}v_{j0} + b = 1,$$
