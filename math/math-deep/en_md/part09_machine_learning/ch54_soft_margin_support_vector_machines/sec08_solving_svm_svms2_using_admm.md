# Solving SVM (SVMs2') Using ADMM


<!-- PAGE 2018 -->
We have examples where there is a single support vector of type $1$ and $\nu  = 2q_{f}/(p + q)$, so the above method fails. Curiously, perturbing $\nu$  slightly yields a solution with some blue support vector of type $1$ and some red support vector of type $1$, and so we have not yet found an example where the above method succeeds with a single support vector of type $1$. This suggests to conduct some perturbation analysis but it appears to be nontrivial. Among its advantages, the support vector machinery is conducive to finding interesting statistical bounds in terms of the VC dimension, a notion invented by Vapnik and Chernovenkis. We will not go into this here and instead refer the reader to Vapnik $[188]$ (especially, Chapter $4$ and Chapters 9-13).

## 54.8 Solving SVM (SVM ) Using ADMM

$$s2'$$
In order to solve $(SVM_{s2'})$ using ADMM we need to write the matrix corresponding to the constraints in equational form,
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  -\gamma  = K_{m}$$
$$\lambda_{i}  + \alpha_{i}  = K_{s},i = 1, \dots  , p$$
$$\mu_{j}  + \beta_{j}  = K_{s},j = 1, \dots  , q,$$
with $K_{m} = (p + q)K_{s}\nu$ . This is the $(p + q + 2) \times$  (2(p $+ q) + 1)$ matrix $A$ given by
$$A = \begin{pmatrix} 1_{p}^{\top} & -1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} & 0 \\ 1_{p}^{\top} & 1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} & -1 \\ I_{p} & 0_{p,q} & I_{p} & 0_{p,q} & 0_{p} \\ 0_{q,p} & I_{q} & 0_{q,p} & I_{q} & 0_{q} \end{pmatrix} .$$
Observe the remarkable analogy with the matrix arising in $\nu$ -regression in Section 56.3, except that $p = q = m$ and that $-1$ is replaced by $+1$. We leave it as an exercise to prove that $A$ has rank $p + q + 2$. The right-hand side is
$$c = \begin{pmatrix} 0 \\ K_{m} \\ K_{s}1_{p+q} \end{pmatrix} .$$
The symmetric positive semidefinite $(p+q)\times (p+q)$ matrix $P$ defining the quadratic functional is
$$P = X^{\top}X,withX = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} ,$$

<!-- PAGE 2019 -->
and
$$q = 0_{p+q}.$$
Since there are 2(p $+ q) + 1$ Lagrange multipliers $(\lambda , \mu , \alpha , \beta , \gamma$ ), the $(p + q) \times  (p + q)$ matrix $X^{\top}X$ must be augmented with zero’s to make it a (2(p $+ q) + 1) \times$  (2(p $+ q) + 1)$ matrix $P_{a}$ given by
$$P_{a} = \begin{pmatrix} X^{\top}X & 0_{p+q,p+q+1} \\ 0_{p+q+1,p+q} & 0_{p+q+1,p+q+1} \end{pmatrix} ,$$
and similarly $q$ is augmented with zeros as the vector $q_{a} = 0_{2(p+q)+1}$. As we mentioned in Section 54.5, since $\eta  \ge 0$ for an optimal solution, we can drop the constraint $\eta  \ge 0$ from the primal problem. In this case there are $2(p+q)$ Lagrange multipliers $(\lambda , \mu , \alpha , \beta$ ). It is easy to see that the objective function of the dual is unchanged and the set of constraints is
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = K_{m}$$
$$\lambda_{i}  + \alpha_{i}  = K_{s},i = 1, \dots  , p$$
$$\mu_{j}  + \beta_{j}  = K_{s},j = 1, \dots  , q,$$
with $K_{m} = (p + q)K_{s}\nu$ . The constraint matrix corresponding to this system of equations is the $(p + q + 2) \times$  2(p $+ q)$ matrix $A_{2}$ given by
$$A_{2} = \begin{pmatrix} 1_{p}^{\top} & -1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ 1_{p}^{\top} & 1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ I_{p} & 0_{p,q} & I_{p} & 0_{p,q} \\ 0_{q,p} & I_{q} & 0_{q,p} & I_{q} \end{pmatrix} .$$
We leave it as an exercise to prove that $A_{2}$ has rank $p + q + 2$. The right-hand side is
$$c_{2} = \begin{pmatrix} 0 \\ K_{m} \\ K_{s}1_{p+q} \end{pmatrix} .$$
The symmetric positive semidefinite $(p+q)\times (p+q)$ matrix $P$ defining the quadratic functional is
$$P = X^{\top}X,withX = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} ,$$
and
$$q = 0_{p+q}.$$

<!-- PAGE 2020 -->
Since there are 2(p $+ q)$ Lagrange multipliers the $(p + q) \times  (p + q)$ matrix $X^{\top}X$ must be augmented with zero’s to make it a 2(p $+ q) \times$  2(p $+ q)$ matrix $P_{2a}$ given by
$$P_{2a} = \begin{pmatrix} X^{\top}X & 0_{p+q,p+q} \\ 0_{p+q,p+q} & 0_{p+q,p+q} \end{pmatrix} ,$$
and similarly $q$ is augmented with zeros as the vector $q_{2a} = 0_{2(p+q)}$. The Matlab programs implementing the above method are given in Appendix $B$, Section B.2. We ran our program on two sets of $30$ points each generated at random using the following code which calls the function runSVMs2pbv3: rho $= 10$; u16 $= 10.1*randn(2,30)+7$ ; v16 $=$ -10.1*randn(2,30)-7; [~,~,~,~,~,~,w3] $= runSVMs2pbv3(0.37,rho,u16,v16,1/60)$ We picked $K = 1/60$ and various values of $\nu$  starting with $\nu  =$ 0.37, which appears to be the smallest value for which the method converges; see Figure 54.11. In this example, $p_{f} = 10, q_{f} = 11, p_{m} = 12, q_{m} = 12$. The quadratic solver converged after $8121$ steps to reach primal and dual residuals smaller than $10^{-10}$. Reducing $\nu$  below $\nu  =$ 0.37 has the effect that $p_{f}, q_{f}, p_{m}, q_{m}$ decrease but the following situation arises. Shrinking $\eta$  a little bit has the effect that $p_{f} = 9, q_{f} = 10, p_{m} = 10, q_{m} = 11$. Then $max{p_{f}, q_{f}} = min{p_{m}, q_{m}} = 10$, so the only possible value for $\nu$  is $\nu  = 20/60 = 1/3 =$ 0.3333333 $\cdots$  . When we run our program with $\nu  = 1/3$, it returns a value of $\eta$  less than $10^{-13}$ and a value of $w$ whose components are also less than $10^{-13}$. This is probably due to numerical precision. Values of $\nu$  less than $1/3$ cause the same problem. It appears that the geometry of the problem constrains the values of $p_{f}, q_{f}, p_{m}, q_{m}$ in such a way that it has no solution other than $w = 0$ and $\eta  = 0$. Figure 54.12 shows the result of running the program with $\nu  =$ 0.51. We have $p_{f} = 15, q_{f} = 16, p_{m} = 16, q_{m} = 16$. Interestingly, for $\nu  =$ 0.5, we run into the singular situation where there is only one support vector and $\nu  = 2p_{f}/(p + q)$.

<!-- PAGE 2021 -->
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.11: Running (SVM_{s2'}) on two sets of 30 points; \nu  = 0.37.$$
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.13: Running (SVM_{s2'}) on two sets of 30 points; \nu  = 0.71.$$
Next Figure 54.13 shows the result of running the program with $\nu  =$ 0.71. We have $p_{f} = 21, q_{f} = 21, p_{m} = 22, q_{m} = 23$. Interestingly, for $\nu  =$ 0.7, we run into the singular
