# Solving SVM (SVMs4) Using ADMM


<!-- PAGE 2045 -->
Dual of the Soft margin kernel SVM $(SVM_{s4})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1 \\ K + & I_{p+q} \\ 2K_{s} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  \ge \nu$$
$$\lambda_{i}  \ge 0,i = 1, \dots  , p$$
$$\mu_{j}  \ge 0,j = 1, \dots  , q,$$
where $K$ is the kernel matrix of Section 54.1. Then $w, b$, and f(x) are obtained exactly as in Section 54.5.

## 54.14 Solving SVM (SVM ) Using ADMM

$$s4$$
In order to solve $(SVM_{s4})$ using ADMM we need to write the matrix corresponding to the constraints in equational form,
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  -\gamma  = K_{m},$$
with $K_{m} = (p + q)K_{s}\nu$ . This is the $2 \times  (p + q + 1)$ matrix $A$ given by
$$1_{p}^{\top}-1_{q}^{\top}0!$$
$$A =.$$
$$1_{p}^{\top}1_{q}^{\top}-1$$
We leave it as an exercise to prove that $A$ has rank $2$. The right-hand side is
$$c = \begin{pmatrix} 0 \\ K_{m} \end{pmatrix} .$$
The symmetric positive semidefinite $(p+q)\times (p+q)$ matrix $P$ defining the quadratic functional is
$$P = X^{\top}X + \frac{1}{2K_{s}} I_{p+q},withX = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} ,$$
and
$$q = 0_{p+q}.$$

<!-- PAGE 2046 -->
Since there are $p + q + 1$ Lagrange multipliers $(\lambda , \mu , \gamma$ ), the $(p + q) \times  (p + q)$ matrix $P$ must be augmented with zero’s to make it a $(p + q + 1) \times  (p + q + 1)$ matrix $P_{a}$ given by
$$P_{a} = \begin{pmatrix} X^{\top}X & 0_{p+q} \\ 0_{p+q}^{\top} & 0 \end{pmatrix} ,$$
and similarly $q$ is augmented with zeros as the vector $q_{a} = 0_{p+q+1}$. As in Section 54.8, since $\eta  \ge 0$ for an optimal solution, we can drop the constraint $\eta  \ge 0$ from the primal problem. In this case, there are $p + q$ Lagrange multipliers $(\lambda , \mu$ ). It is easy to see that the objective function of the dual is unchanged and the set of constraints is
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = K_{m},$$
with $K_{m} = (p + q)K_{s}\nu$ . The matrix corresponding to the above equations is the $2 \times  (p + q)$ matrix $A_{2}$ given by
$$1_{p}^{\top}-1_{q}^{\top}!$$
$$A_{2} =.$$
$$1_{p}^{\top}1_{q}^{\top}$$
We leave it as an exercise to prove that $A_{2}$ has rank $2$. The right-hand side is
$$c_{2} = \begin{pmatrix} 0 \\ K_{m} \end{pmatrix} .$$
The symmetric positive semidefinite $(p+q)\times (p+q)$ matrix $P$ defining the quadratic functional is
$$P = X^{\top}X + \frac{1}{2K_{s}} I_{p+q},withX = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} ,$$
and
$$q = 0_{p+q}.$$
Since there are $p + q$ Lagrange multipliers $(\lambda , \mu$ ), the $(p + q) \times  (p + q)$ matrix $P$ need not be augmented with zero’s, so $P_{2a} = P$ and similarly $q_{2a} = 0_{p+q}$. We ran our Matlab implementation of the above version of $(SVM_{s4})$ on the data set of Section 54.12. Since the value of $\nu$  is irrelevant, we picked $\nu  = 1$. First we ran our program with $K = 190$; see Figure 54.22. We have $p_{m} = 23$ and $q_{m} = 18$. The program does not converge for $K \ge 200$.
