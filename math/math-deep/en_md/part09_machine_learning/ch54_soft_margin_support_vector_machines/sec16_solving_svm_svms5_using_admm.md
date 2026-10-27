# Solving SVM (SVMs5) Using ADMM


<!-- PAGE 2051 -->
defining the convex set
$$$$
$$U = \begin{pmatrix} \lambda \\ \mu \end{pmatrix} \in \mathbb{R}_{+}^{p+q}| 1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu  = (p + q)K_{s}\nu .$$
The proof is essentially the proof of 54.8 using the above SPD matrix and convex set. The “kernelized” version of Problem $(SVM_{s5})$ is the following: Soft margin kernel SVM $(SVM_{s5})$:
$$-$$
$$minimize \frac{1}{2} \langle w, w\rangle + \frac{1}{2} b^{2}\nu \eta  + K_{s}(\epsilon^{\top} \epsilon  + \xi^{\top} \xi )$$
$$subject to$$
$$\langle w, \phi (u_{i})\rangle -b \ge \eta  -\epsilon_{i} ,i = 1, \dots  , p$$
$$-\langle w, \phi (v_{j})\rangle + b \ge \eta  -\xi_{j} ,j = 1, \dots  , q,$$
with $K_{s} = 1/(p + q)$. Tracing through the derivation of the dual program, we obtain Dual of the Soft margin kernel SVM $(SVM_{s5})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ K + & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix} 1 \\ + & I_{p+q} \\ 2K_{s} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu$$
$$\lambda_{i}  \ge 0,i = 1, \dots  , p$$
$$\mu_{j}  \ge 0,j = 1, \dots  , q,$$
where $K$ is the kernel matrix of Section 54.1. Then $w, b$, and f(x) are obtained exactly as in Section 54.13.

## 54.16 Solving SVM (SVM ) Using ADMM

$$s5$$
In order to solve $(SVM_{5})$ using ADMM we need to write the matrix corresponding to the constraints in equational form,
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = K_{m},$$
with $K_{m} = (p + q)K_{s}\nu$ . This is the $1 \times  (p + q)$ matrix $A$ given by
$$A = \begin{pmatrix} 1_{p}^{\top} & 1_{q}^{\top} \end{pmatrix} .$$

<!-- PAGE 2052 -->
Obviously, $A$ has rank $1$. The right-hand side is
$$c = K_{m}.$$
The symmetric positive definite $(p + q) \times  (p + q)$ matrix $P$ defining the quadratic functional is
$$P = X^{\top}X + \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} + \frac{1}{2K_{s}} I_{p+q},withX = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} ,$$
and
$$q = 0_{p+q}.$$
Since there are $p + q$ Lagrange multipliers $(\lambda , \mu$ ), the $(p + q) \times  (p + q)$ matrix $P$ does not have to be augmented with zero’s. We ran our Matlab implementation of the above version of $(SVM_{s5})$ on the data set of Section 54.14. Since the value of $\nu$  is irrelevant, we picked $\nu  = 1$. First we ran our program with $K = 190$; see Figure 54.24. We have $p_{m} = 23$ and $q_{m} = 18$. The program does not converge for $K \ge 200$.
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.24: Running (SVM_{s5}) on two sets of 30 points; K = 190.$$
