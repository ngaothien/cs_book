# Solving -Regression Using ADMM


<!-- PAGE 2128 -->
The proof is very similar to the proof of the corresponding formula in Section 56.5. By Theorem 56.5, there is some suppor vector $x_{i}$, say
$$w^{\top}x_{i0} + b -y_{i0} = \epsilon or-w^{\top}x_{j0} -b + y_{j0} = \epsilon .$$
Then we find an equation expressing $\epsilon$  in terms of $\lambda , \mu$  and $w$, provided that $\nu$ ̸ $= 2p_{f}/m$ and $\nu$ ̸ $= 2q_{f}/m$. The proof is analogous to the proof of Proposition 54.4 and is left as an exercise.

## 56.3 Solving \nu -Regression Using ADMM

The quadratic functional $F(\lambda , \mu$ ) occurring in the dual program given by
$$F(\lambda , \mu ) = \frac{1}{2} \sum_{i,j=1}^{m}  (\lambda_{i}  -\mu_{i} )(\lambda_{j}  -\mu_{j} )x_{i}^{\top} x_{j} + \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} )y_{i}$$
$$is not of the form_{2}^{1} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \\ letKbe \end{pmatrix} P \begin{pmatrix} \lambda \\ \mu \end{pmatrix} +q^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} , but it can be converted in such a form using$$
a trick. First, if we    the $m \times  m$ symmetric matrix $K = XX^{\top} = (x_{i}^{\top} x_{j})$, then we have
$$F(\lambda , \mu ) = \frac{1}{2} (\lambda^{\top} -\mu^{\top} )K(\lambda  -\mu ) + y^{\top}\lambda  -y^{\top}\mu .$$
Consequently, if we define the 2m $\times$  2m symmetric matrix $P$ by
$$P = \begin{pmatrix} XX^{\top} & -XX^{\top} \\ -XX^{\top} & XX^{\top} \end{pmatrix} = \begin{pmatrix} K & -K \\ -K & K \end{pmatrix}$$
and the 2m $\times  1$ matrix $q$ by
$$q = \begin{pmatrix} y \\ -y \end{pmatrix} ,$$
it is easy to check that
$$F(\lambda , \mu ) = \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} P \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + q^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = \frac{1}{2} \lambda^{\top} K\lambda  + \frac{1}{2} \mu^{\top} K\mu  -\lambda^{\top} K\mu  + y^{\top}\lambda  -y^{\top}\mu . (*_{q})$$
Since
$$\frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} P \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = \frac{1}{2} (\lambda^{\top} -\mu^{\top} )K(\lambda  -\mu )$$
and the matrix $K = XX^{\top}$ is symmetric positive semidefinite, the matrix $P$ is also symmetric

<!-- PAGE 2129 -->
positive semidefinite. Thus we are in a position to apply ADMM since the constraints are
$$\sum_{i=1}^{m}  \lambda_{i}  - \sum_{i=1}^{m}  \mu_{i}  = 0$$
$$\sum_{i=1}^{m}  \lambda_{i}  + \sum_{i=1}^{m}  \mu_{i}  + \gamma  = C\nu$$
$$\lambda  + \alpha  = \frac{C}{m} ,\mu  + \beta  = \frac{C}{m} ,$$
namely affine. We need to check that the (2m $+ 2) \times$  (4m $+ 1)$ matrix $A$ corresponding to this system has rank 2m $+ 2$. Let us clarify this point. The matrix $A$ corresponding to the above equations is
$$A = \begin{pmatrix} 1_{m}^{\top} & -1_{m}^{\top} & 0_{m}^{\top} & 0_{m}^{\top} & 0 \\ 1_{m}^{\top} & 1_{m}^{\top} & 0_{m}^{\top} & 0_{m}^{\top} & 1 \\ I_{m} & 0_{m,m} & I_{m} & 0_{m,m} & 0_{m} \\ 0_{m,m} & I_{m} & 0_{m,m} & I_{m} & 0_{m} \end{pmatrix} .$$
For example, for $m = 3$ we have the $8 \times  13$ matrix
$$\begin{pmatrix} 1 & 1 & 1 & -1 & -1 & -1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 1 & 1 & 1 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \end{pmatrix} .$$
We leave it as an exercise to show that $A$ has rank 2m $+ 2$. Recall that
$$q = \begin{pmatrix} y \\ -y \end{pmatrix}$$
and we also define the vector $c$ (of dimension 2m $+ 2)$ as
$$c = \begin{pmatrix} 0 \\ C\nu \\ C1_{2m} \end{pmatrix} .$$
$$\overline{m}$$
The constraints are given by the system of affine equations Ax $= c$, where
$$x = \begin{pmatrix} \lambda^{\top} & \mu^{\top} & \alpha^{\top} & \beta^{\top} \end{pmatrix} \gamma^{\top} .$$

<!-- PAGE 2130 -->
Since there are 4m $+ 1$ Lagrange multipliers $(\lambda , \mu , \alpha , \beta , \gamma$ ), we need to pad the 2m $\times$  2m matrix $P$ with zeros to make it into a (4m $+ 1) \times$  (4m $+ 1)$ matrix
$$P_{a} = \begin{pmatrix} P & 0_{2m,2m+1} \\ 0_{2m+1,2m} & 0_{2m+1,2m+1} \end{pmatrix} .$$
Similarly, we pad $q$ with zeros to make it a vector $q_{a}$ of dimension 4m $+ 1$,
$$q_{a} = \begin{pmatrix} q \\ 0_{2m+1} \end{pmatrix} .$$
In order to solve our dual program, we apply ADMM to the quadractic functional
$$\frac{1}{2} x^{\top}P_{a}x + q_{a}^{\top} x,$$
subject to the constraints
$$Ax = c,x \ge 0,$$
with $P_{a}, q_{a}, A, b$ and $x$, as above. Since for an optimal solution with $\epsilon  > 0$ we must have $\gamma  = 0$ (from the KKT conditions), we can solve the dual problem with the following set of constraints only involving the Lagrange multipliers $(\lambda , \mu , \alpha , \beta$ ),
$$\sum_{i=1}^{m}  \lambda_{i}  - \sum_{i=1}^{m}  \mu_{i}  = 0$$
$$\sum_{i=1}^{m}  \lambda_{i}  + \sum_{i=1}^{m}  \mu_{i}  = C\nu$$
$$\lambda  + \alpha  = \frac{C}{m} ,\mu  + \beta  = \frac{C}{m} ,$$
which corresponds to the (2m $+ 2) \times$  4m $A_{2}$ given by
$$A_{2} = \begin{pmatrix} 1_{m}^{\top} & -1_{m}^{\top} & 0_{m}^{\top} & 0_{m}^{\top} \\ 1_{m}^{\top} & 1_{m}^{\top} & 0_{m}^{\top} & 0_{m}^{\top} \\ I_{m} & 0_{m,m} & I_{m} & 0_{m,m} \\ 0_{m,m} & I_{m} & 0_{m,m} & I_{m} \end{pmatrix} .$$
We leave it as an exercise to show that $A_{2}$ has rank 2m $+ 2$. We define the vector $c_{2}$ (of dimension 2m $+ 2)$ as
$$c_{2} = c = \begin{pmatrix} 0 \\ C\nu \\ C1_{2m} \end{pmatrix} .$$
$$\overline{m}$$

<!-- PAGE 2131 -->
Since there are 4m Lagrange multipliers $(\lambda , \mu , \alpha , \beta$ ), we need to pad the 2m $\times$  2m matrix $P$ with zeros to make it into a 4m $\times$  4m matrix
$$P_{2a} = \begin{pmatrix} P & 0_{2m,2m} \\ 0_{2m,2m} & 0_{2m,2m} \end{pmatrix} .$$
Similarly, we pad $q$ with zeros to make it a vector $q_{2a}$ of dimension 4m,
$$q_{2a} = \begin{pmatrix} q \\ 0_{2m} \end{pmatrix} .$$
We implemented the above methods in Matlab; see Appendix $B$, Section B.4. Choosing $C = m$ is typically a good choice because then the values of $\lambda_{i}$  and $\mu_{j}$  are not too small $(C/m = 1)$. If $C$ is chosen too small, we found that numerical instability increases drastically and very poor results are obtained. Increasing $C$ tends to encourage sparsity. We ran our Matlab implementation of the above method on the set of $50$ points generated at random by the program shown below with $C = 50$ and various values of $\nu$  starting with $\nu  =$ 0.03: X13 $=$ 15*randn(50,1); ww13 $= 1$; y13 $=$ X13*ww13 $+$ 10*randn(50,1) $+ 20$; [~,~,~,~,~,~,~,~,w1] $=$ runuregb(rho,0.03,X13,y13,50) Figure 56.11 shows the result of running the program with $\nu  =$ 0.03. We have $p_{f} = 0, q_{f} = 0, p_{m} = 2$ and $q_{m} = 1$. There are $47$ points strictly inside the slab. The slab is large enough to contain all the data points, so none of them is considered an error. The next value of $\nu$  is $\nu  =$ 0.21, see Figure 56.12. We have $p_{f} = 4, q_{f} = 5, p_{m} = 6$ and $q_{m} = 6$. There are $38$ points strictly inside the slab.

<!-- PAGE 2132 -->
$$80$$
$$60$$
$$40$$
$$20$$
$$0$$
$$-20$$
$$-40$$
$$-40-30-20-100102030405060$$
$$Figure 56.11: Running \nu -SV regression on a set of 50 points; \nu  = 0.03.$$
$$80$$
$$60$$
$$40$$
$$20$$
$$0$$
$$-20$$
$$-40$$
$$-40-30-20-100102030405060$$
$$Figure 56.12: Running \nu -SV regression on a set of 50 points; \nu  = 0.21.$$
The next value of $\nu$  is $\nu  =$ 0.5, see Figure 56.13. We have $p_{f} = 12, q_{f} = 12, p_{m} = 13$ and

<!-- PAGE 2133 -->
$q_{m} = 14$. There are $23$ points strictly inside the slab.
$$80$$
$$60$$
$$40$$
$$20$$
$$0$$
$$-20$$
$$-40$$
$$\overline{-40}\overline{-30}\overline{-20}\overline{-10}\overline{0}\overline{10}\overline{20}\overline{30}\overline{40}\overline{50}\overline{60}$$
$$Figure 56.13: Running \nu -SV regression on a set of 50 points; \nu  = 0.5.$$
$$80$$
$$60$$
$$40$$
$$20$$
$$0$$
$$-20$$
$$-40$$
$$\overline{-40}\overline{-30}\overline{-20}\overline{-10}\overline{0}\overline{10}\overline{20}\overline{30}\overline{40}\overline{50}\overline{60}$$
$$Figure 56.14: Running \nu -SV regression on a set of 50 points; \nu  = 0.7.$$
The next value of $\nu$  is $\nu  =$ 0.7, see Figure 56.14. We have $p_{f} = 17, q_{f} = 17, p_{m} = 18$ and
