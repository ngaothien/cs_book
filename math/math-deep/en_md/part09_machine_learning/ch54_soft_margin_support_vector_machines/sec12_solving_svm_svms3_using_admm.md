# Solving SVM (SVMs3) Using ADMM


<!-- PAGE 2033 -->

> **Theorem 54.7.** For every optimal solution $(w, b, \eta , \epsilon , \xi$ ) of Problem $(SVM_{s3})$ with w̸ $= 0$ and $\eta  > 0$, if
$$(p_{sf} + q_{sf})/(p + q) < \nu  < 1,$$
then some $u_{i0}$ or some $v_{j0}$ is a support vector. The proof proceeds by contradiction using Proposition 54.6 (for a very similar proof, see the proof of Theorem 54.3).

## 54.12 Solving SVM (SVM ) Using ADMM

$$s3$$
In order to solve $(SVM_{s3})$ using ADMM we need to write the matrix corresponding to the constraints in equational form,
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = K_{m}$$
$$\lambda_{i}  + \alpha_{i}  = K_{s},i = 1, \dots  , p$$
$$\mu_{j}  + \beta_{j}  = K_{s},j = 1, \dots  , q$$
with $K_{m} = (p + q)K_{s}\nu$ . This is the $(p + q + 1) \times$  2(p $+ q)$ matrix $A$ given by
$$A = \begin{pmatrix} 1_{p}^{\top} & 1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ I_{p} & 0_{p,q} & I_{p} & 0_{p,q} \\ 0_{q,p} & I_{q} & 0_{q,p} & I_{q} \end{pmatrix} .$$
We leave it as an exercise to prove that $A$ has rank $p + q + 1$. The right-hand side is
$$c = \begin{pmatrix} K_{m} \\ K_{s}1_{p+q} \end{pmatrix} .$$
The symmetric positive semidefinite $(p+q)\times (p+q)$ matrix $P$ defining the quadratic functional is
$$P = X^{\top}X + \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} ,withX = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} ,$$
and
$$q = 0_{p+q}.$$
Since there are 2(p $+q)$ Lagrange multipliers $(\lambda , \mu , \alpha , \beta$ ), the $(p +q)\times (p +q)$ matrix $P$ must be augmented with zero’s to make it a 2(p $+ q) \times$  2(p $+ q)$ matrix $P_{a}$ given by
$$P_{a} = \begin{pmatrix} P & 0_{p+q,p+q} \\ 0_{p+q,p+q} & 0_{p+q,p+q} \end{pmatrix} ,$$

<!-- PAGE 2034 -->
and similarly $q$ is augmented with zeros as the vector
$$q_{a} = 0_{2(p+q)}.$$
The Matlab programs implementing the above method are given in Appendix $B$, Section B.3. We ran our program on the same input data points used in Section 54.8, namely u16 $= 10.1*randn(2,30)+7$ ; v16 $=$ -10.1*randn(2,30)-7; [~,~,~,~,~,~,w3] $= runSVMs3b(0.365,rho,u16,v16,1/60)$ We picked $K = 1/60$ and various values of $\nu$  starting with $\nu  =$ 0.365, which appears to be the smallest value for which the method converges; see Figure 54.16.
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.16: Running (SVM_{s3}) on two sets of 30 points; \nu  = 0.365.$$
We have $p_{f} = 10, q_{f} = 10, p_{m} = 12$ and $q_{m} = 11$, as opposed to $p_{f} = 10, q_{f} = 11, p_{m} = 12, q_{m} = 12$, which was obtained by running $(SVM_{s2'})$; see Figure 54.11. A slightly narrower margin is achieved. Next we ran our program with $\nu  =$ 0.5, see Figure 54.17. We have $p_{f} = 13, q_{f} = 16, p_{m} = 14$ and $q_{m} = 17$. We also ran our program with $\nu  =$ 0.71, see Figure 54.18. We have $p_{f} = 21, q_{f} = 21, p_{m} = 22$ and $q_{m} = 22$. The value $\nu  =$ 0.7 is a singular value for which there are no support vectors and $\nu  = (p_{f} + q_{f})/(p + q)$.

<!-- PAGE 2035 -->
Finally we ran our program with $\nu  =$ 0.98, see Figure 54.19. We have $p_{f} = 28, q_{f} = 30, p_{m} = 29$ and $q_{m} = 30$. Because the term $(1/2)b^{2}$ is added to the objective function to be minimized, it turns out that $(SVM_{s3})$ yields values of $b$ and $\eta$  that are smaller than the values returned by $(SVM_{s2'})$. This is the reason why a smaller margin width could be obtained for $\nu  =$ 0.365. On the other hand, $(SVM_{s3})$ is unable to achieve as big a margin as $(SVM_{s2'})$ for values of $\nu  \ge$ 0.97, because the separating line produced by $(SVM_{s3})$ is lower than the the separating line produced by $(SVM_{s2'})$.
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.17: Running (SVM_{s3}) on two sets of 30 points; \nu  = 0.5.$$

<!-- PAGE 2036 -->
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.18: Running (SVM_{s3}) on two sets of 30 points; \nu  = 0.71.$$
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.19: Running (SVM_{s3}) on two sets of 30 points; \nu  = 0.98.$$
