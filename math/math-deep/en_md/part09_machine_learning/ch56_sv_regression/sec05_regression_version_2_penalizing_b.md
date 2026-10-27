# -Regression Version 2; Penalizing b


<!-- PAGE 2137 -->
Dual Program $\epsilon$ -SV Regression:
$$minimize \frac{1}{2} \sum_{i,j=1}^{m}  (\lambda_{i}  -\mu_{i} )(\lambda_{j}  -\mu_{j} )x_{i}^{\top} x_{j} + \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} )y_{i} + \epsilon \sum_{i=1}^{m}  (\lambda_{i}  + \mu_{i} )$$
$$subject to$$
$$\sum_{i=1}^{m}  \lambda_{i}  - \sum_{i=1}^{m}  \mu_{i}  = 0$$
$$0 \le \lambda_{i}  \le \frac{C}{m} ,0 \le \mu_{i}  \le \frac{C}{m} ,i = 1, \dots  , m,$$
minimizing over $\alpha$  and $\mu$ . The constraint
$$\sum_{i=1}^{m}  \lambda_{i}  + \sum_{i=1}^{m}  \mu_{i}  \le C\nu$$
$$is gone but the extra term \epsilon \sum_{i}  m=1(\lambda_{i}  + \mu_{i} ) has been added to the dual function, to prevent$$
$\lambda_{i}$  and $\mu_{i}$  from blowing up. There is an obvious kernelized version of $\epsilon$ -SV regression. It is easy to show that $\nu$ -SV regression subsumes $\epsilon$ -SV regression, in the sense that if $\nu$ -SV regression succeeds and yields $w, b, \epsilon  > 0$, then $\epsilon$ -SV regression with the same $C$ and the same value of $\epsilon$  also succeeds and returns the same pair $(w, b)$. For more details on these methods, see Sch¨olkopf, Smola, Williamson, and Bartlett $[153]$.
$$Remark: The linear penalty function \sum_{i}  m=1(\xi_{i} +\xi_{i}' ) can be replaced by the quadratic penalty$$
$$function \sum_{i}  m(\xi_{i}^{2}  + \xi_{i}^{'2}  ); see Shawe–Taylor and Christianini [165] (Chapter 7). In this case,$$
it is easy $to^{=1}$ see that for an optimal solution we must have $\xi_{i}  \ge 0$ and $\xi_{i}'  \ge 0$, so we may omit the constraints $\xi_{i}  \ge 0$ and $\xi_{i}'  \ge 0$. We must also have $\gamma  = 0$ so we omit the variable $\gamma$ as well. It can be shown that $\xi  = (m/2C)\lambda$  and $\xi' = (m/2C)\mu$ . This problem is very similar to the Soft Margin SVM $(SVM_{s4})$ discussed in Section 54.13. 56.5 $\nu$ -Regression Version $2$; Penalizing $b$ Yet another variant of $\nu$ -SV regression is to add the $term^{1}b^{2}$ to the objective function. We will see that solving the dual not only determines $w but^{2}$ also $b$ and $\epsilon$  (provided a mild condition on $\nu$ ). We wish to solve the following program:

<!-- PAGE 2138 -->
Program $\nu$ -SV Regression Version $2$
$$minimize \frac{1}{2} w^{\top}w + \frac{1}{2} b^{2} + C \begin{pmatrix} 1 \\ \nu \epsilon  + & (\xi_{i}  + \xi_{i}' ) \\ m \end{pmatrix} \sum_{i=1}^{m}$$
$$subject to$$
$$w^{\top}x_{i} + b -y_{i} \le \epsilon  + \xi_{i} ,\xi_{i}  \ge 0i = 1, \dots  , m$$
$$-w^{\top}x_{i} -b + y_{i} \le \epsilon  + \xi_{i}' ,\xi_{i}'  \ge 0i = 1, \dots  , m,$$
minimizing over the variables $w, b, \epsilon , \xi$ , and $\xi'$ . The constraint $\epsilon  \ge 0$ is omitted since the problem has no solution if $\epsilon  < 0$. We leave it as an exercise to show that the new Lagrangian is
$$!$$
$$L(w, b, \lambda , \mu , \xi , \xi' , \epsilon , \alpha , \beta ) = \frac{1}{2} w^{\top}w + w^{\top} \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} )x_{i}$$
$$!$$
$$+ \epsilon C\nu  - \sum_{i=1}^{m}  (\lambda_{i}  + \mu_{i} )+ \sum_{i=1}^{m}  \xi_{i} \begin{pmatrix} C \\ -\lambda_{i}  -\alpha_{i} \\ m \end{pmatrix}$$
$$!$$
$$+$$
$$+ \sum_{i=1}^{m}  \xi_{i}' \begin{pmatrix} C \\ -\mu_{i}  -\beta_{i} \\ m \end{pmatrix} + \frac{1}{2} b^{2} b \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} )- \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} )y_{i}.$$
If we set the Laplacian $\nabla L_{w,\epsilon ,b,\xi ,\xi'}$ to zero we obtain the equations
$$w = \sum_{i=1}^{m}  (\mu_{i}  -\lambda_{i} )x_{i} = X^{\top}(\mu  -\lambda )(*_{w})$$
$$C\nu  - \sum_{i=1}^{m}  (\lambda_{i}  + \mu_{i} ) = 0$$
$$b + \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} ) = 0$$
$$\frac{C}{m} -\lambda  -\alpha  = 0, \frac{C}{m} -\mu  -\beta  = 0.$$
We obtain the new equation
$$b = - \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} ) = -(1_{m}^{\top}\lambda  -1_{m}^{\top}\mu )(*_{b})$$
determining $b$, which replaces the equation
$$\sum_{i=1}^{m}  \lambda_{i}  - \sum_{i=1}^{m}  \mu_{i}  = 0.$$

<!-- PAGE 2139 -->
Plugging back $w$ from $(*_{w})$ and $b$ from $(*_{b})$ into the Lagrangian we get
$$-$$
$$G(\lambda , \mu , \alpha , \beta ) = - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} P \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -q^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + \frac{1}{2} b^{2}b^{2}$$
$$= - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} P \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -q^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \frac{1}{2} b^{2}$$
$$= - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ P+ & -1_{m}1_{m}^{\top} & 1_{m}1_{m}^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -q^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} ,$$
with
$$P = \begin{pmatrix} XX^{\top} & -XX^{\top} \\ -XX^{\top} & XX^{\top} \end{pmatrix} = \begin{pmatrix} K & -K \\ -K & K \end{pmatrix}$$
and
$$q = \begin{pmatrix} y \\ -y \end{pmatrix} .$$
The new dual program is Dual Program $\nu$ -SV Regression Version $2$
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ P+ & -1_{m}1_{m}^{\top} & 1_{m}1_{m}^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + q^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{m}  \lambda_{i}  + \sum_{i=1}^{m}  \mu_{i}  = C\nu$$
$$0 \le \lambda_{i}  \le \frac{C}{m} ,0 \le \mu_{i}  \le \frac{C}{m} ,i = 1, \dots  , m.$$
Definition 56.1 and Definition 56.2 are unchanged. We have the following version of Proposition 56.2 showing that $p_{f}, q_{f}, p_{m}$ an $q_{m}$ have direct influence on the choice of $\nu$ .

> **Proposition 56.7.**
$(1)$ Let $p_{f}$ be the number of points $x_{i}$ such that $\lambda_{i}  = C/m$, and let $q_{f}$ be the number of points $x_{i}$ such that $\mu_{i}  = C/m$. We have $p_{f} + q_{f} \le m\nu$ .
$(2)$ Let $p_{m}$ be the number of points $x_{i}$ such that $\lambda_{i}  > 0$, and let $q_{m}$ be the number of points $x_{i}$ such that $\mu_{i}  > 0$. We have $p_{m} + q_{m} \ge m\nu$ .
$(3)$ If $p_{f} \ge 1$ or $q_{f} \ge 1$, then $\nu  \ge 1/m$.

*Proof.* $(1)$ Let $K_{\lambda}$ and $K_{\mu}$ be the sets of indices corresponding to points failing the margin,
$$K_{\lambda} = {i \in {1, \dots  , m} | \lambda_{i}  = C/m}$$
$$K_{\mu} = {i \in {1, \dots  , m} | \mu_{i}  = C/m}.$$

<!-- PAGE 2140 -->
By definition $p_{f} = |K_{\lambda}|, q_{f} = |K_{\mu}|$. Since the equation
$$\sum_{i=1}^{m}  \lambda_{i}  + \sum_{j=1}^{m}  \mu_{j}  = C\nu$$
holds, by definition of $K_{\lambda}$ and $K_{\mu}$ we have
$$(p_{f} + q_{f}) \frac{C}{m} = \sum_{i\in K\lambda}  \lambda_{i}  + \sum_{j\in K\mu}  \mu_{j}  \le \sum_{i=1}^{m}  \lambda_{i}  + \sum_{j=1}^{m}  \mu_{j}  = C\nu ,$$
which implies that
$$p_{f} + q_{f} \le m\nu .$$
$(2)$ Let $I_{\lambda >0}$ and $I_{\mu >0}$ be the sets of indices
$$I_{\lambda >0} = {i \in {1, \dots  , m} | \lambda_{i}  > 0}$$
$$I_{\mu >0} = {i \in {1, \dots  , m} | \mu_{i}  > 0}.$$
By definition $p_{m} = |I_{\lambda >0}|, q_{m} = |I_{\mu >0}|$. We have
$$\sum_{i=1}^{m}  \lambda_{i}  + \sum_{j=1}^{m}  \mu_{j}  = \sum_{i\in I\lambda >0}  \lambda_{i}  + \sum_{j\in I\mu >0}  \mu_{j}  = C\nu .$$
Since $\lambda_{i}  \le C/m$ and $\mu_{j}  \le C/m$, we obtain
$$C\nu  \le (p_{m} + q_{m}) \frac{C}{m} ,$$
that is, $p_{m} + q_{m} \ge m\nu$ .
$(3)$ follows immediately from $(1)$. Proposition 56.7 yields the following bounds on $\nu$ :
$$\frac{p_{f}+ q_{f}}{m} \le \nu  \le \frac{p_{m} + q_{m}}{m} .$$
Again, the smaller $\nu$  is, the wider the $\epsilon$ -slab is, and the larger $\nu$  is, the narrower the $\epsilon$ -slab is.
Remark: It can be shown that for any optimal solution with w̸ $= 0$ and $\epsilon  > 0$, if the inequalities $(p_{f} + q_{f})/m < \nu  < 1$ hold, then some point $x_{i}$ is a support vector. The proof is essentially Case 1b in the proof of Proposition 56.4. We leave the details as an exercise.

<!-- PAGE 2141 -->
The new dual program is solved using ADMM. The $(2m+1)\times$ 4m matrix $A_{3}$ corresponding to the equational constraints
$$\sum_{i=1}^{m}  \lambda_{i}  + \sum_{i=1}^{m}  \mu_{i}  = C\nu$$
$$\lambda  + \alpha  = \frac{C}{m} ,\mu  + \beta  = \frac{C}{m} ,$$
is given by
$$A_{3} = \begin{pmatrix} 1_{m}^{\top} & 1_{m}^{\top} & 0_{m}^{\top} & 0_{m}^{\top} \\ I_{m} & 0_{m,m} & I_{m} & 0_{m,m} \\ 0_{m,m} & I_{m} & 0_{m,m} & I_{m} \end{pmatrix} .$$
We leave it as an exercise to show that $A_{3}$ has rank 2m $+ 1$. We define the vector $c_{3}$ (of dimension 2m $+ 1)$ as
$$c_{3} = \begin{pmatrix} C\nu \\ C1_{2m} \\ \overline{m} \end{pmatrix} .$$
Since there are 4m Lagrange multipliers $(\lambda , \mu , \alpha , \beta$ ), we need to pad the 2m $\times$  2m matrix
$$P_{3} = P + \begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ -1_{m}1_{m}^{\top} & 1_{m}1_{m}^{\top} \end{pmatrix} with zeros to make it into a 4m \times  4m matrix$$
$$P_{3a} = \begin{pmatrix} P_{3} & 0_{2m,2m} \\ 0_{2m,2m} & 0_{2m,2m} \end{pmatrix} .$$
Similarly, we pad $q$ with zeros to make it a vector $q_{3a}$ of dimension 4m,
$$q_{3a} = \begin{pmatrix} q \\ 0_{2m} \end{pmatrix} .$$
It remains to compute $\epsilon$ . Ther are two methods to do this. The first method assumes the Standard Margin Hypothesis, which is that there is some $i_{0}$ such that $0 < \lambda_{i0}  < C/m$ or there is some $j_{0}$ such that $0 < \mu_{j0}  < C/m$; in other words, there is some support vector of type $1$. By the complementary slackness conditions, $\xi_{i0}  = 0$ or $\xi_{j0}'  = 0$, so we have either $w^{\top}x_{i0} + b$ - $y_{i0} = \epsilon$  or $-w^{\top}x_{j0}$ - $b + y_{j0} = \epsilon$ , which determines $\epsilon$ . Due to numerical instability, when writing a computer program it is preferable to compute the lists of indices $I_{\lambda}$ and $I_{\mu}$ given by
$$I_{\lambda} = {i \in {1, \dots  , m} | 0 < \lambda_{i}  < C/m}$$
$$I_{\mu} = {j \in {1, \dots  , m} | 0 < \mu_{j}  < C/m}.$$

<!-- PAGE 2142 -->
Then it is easy to see that we can compute $\epsilon$  using the following averaging formulae: if $I_{\lambda} \neq  \emptyset$ , then
$$\epsilon  = w^{\top} \begin{pmatrix} x_{i} \\ i \end{pmatrix} \sum_{\in I\lambda}  /|I_{\lambda}| + b - \begin{pmatrix} y_{i} \\ i \end{pmatrix} \sum_{\in I\lambda}  /|I_{\lambda}|,$$
and if $I_{\mu} \neq  \emptyset$ , then
$$\epsilon  = -w^{\top} \begin{pmatrix} x_{j} \end{pmatrix} \sum_{j\in I\mu}  /|I_{\mu}| -b + \begin{pmatrix} y_{i} \\ i \end{pmatrix} \sum_{\in I\mu}  /|I_{\mu}|.$$
The second method uses duality. Under a mild condition, expressing that the duality gap is zero, we can determine $\epsilon$  in terms of $\lambda , \mu$  and $b$. This is because points $x_{i}$ that fail the margin, which means that $\lambda_{i}  = C/m$ or $\mu_{i}  = C/m$, are the only points for which $\xi_{i}  > 0$ or $\xi_{i}'  > 0$. But in this case we have an active constraint
$$w^{\top}x_{i} + b -y_{i} = \epsilon  + \xi_{i} (*_{\xi})$$
or
$$-w^{\top}x_{i} -b + y_{i} = \epsilon  + \xi_{i}' ,(*_{\xi'})$$
so $\xi_{i}$  and $\xi_{i}'$  can be expressed in terms of $w$ and $b$. Since the duality gap is zero for an optimal solution, the optimal value of the primal is equal to the optimal value of the dual. Using the fact that
$$w = X^{\top}(\mu  -\lambda )$$
$$b = -(1_{m}^{\top}\lambda  -1_{m}^{\top}\mu ) = \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} -1_{m} \\ 1_{m} \end{pmatrix}$$
we obtain an expression for the optimal value of the primal. First we have
$$\frac{1}{2} w^{\top}w + \frac{1}{2} b^{2}= \frac{1}{2} (\lambda^{\top} -\mu^{\top} )XX^{\top}(\lambda  -\mu ) + \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ -1_{m}1_{m}^{\top} & 1_{m}1_{m}^{\top} \\ \lambda  \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$= \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \mu \end{pmatrix} ,$$
$$\begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ P+ & -1_{m}1_{m}^{\top} & 1_{m}1_{m}^{\top} \end{pmatrix}$$
with
$$P = \begin{pmatrix} XX^{\top} & -XX^{\top} \\ -XX^{\top} & XX^{\top} \end{pmatrix} .$$
Let $K_{\lambda}$ and $K_{\mu}$ be the sets of indices corresponding to points failing the margin,
$$K_{\lambda} = {i \in {1, \dots  , m} | \lambda_{i}  = C/m}$$
$$K_{\mu} = {i \in {1, \dots  , m} | \mu_{i}  = C/m}.$$

<!-- PAGE 2143 -->
Because $\lambda_{i} \mu_{i}  = 0$, the sets $K_{\lambda}$ and $K_{\mu}$ are disjoint. Observe that from Definition 56.2 we have $p_{f} = |K_{\lambda}|$ and $q_{f} = |K_{\mu}|$. Then by $(*_{\xi})$ and $(*_{\xi'})$, we have
$$\sum_{i=1}^{m}  (\xi_{i}  + \xi_{i}' ) = \sum_{i\in K\lambda}  \xi_{i}  + \sum_{j\in K\mu}  \xi_{j}'$$
$$= \sum_{i\in K\lambda}  (w^{\top}x_{i} + b -y_{i} -\epsilon ) + \sum_{j\in K\mu}  (-w^{\top}x_{j} -b + y_{j} -\epsilon )$$
$$= w^{\top} \begin{pmatrix} x_{i} - & x_{j} \end{pmatrix} \sum_{i\in K\lambda}  \sum_{j\in K\mu}  - \sum_{i\in K\lambda}  y_{i} + \sum_{j\in K\mu}  y_{j} + (p_{f} -q_{f})b -(p_{f} + q_{f})\epsilon .$$
The optimal value of the dual is given by
$$- \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ P+ & -1_{m}1_{m}^{\top} & 1_{m}1_{m}^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -q^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} ,$$
with
$$q = \begin{pmatrix} y \\ -y \end{pmatrix} .$$
Expressing that the duality gap is zero we have
$$\frac{1}{2} w^{\top}w + \frac{1}{2} b^{2} + C\nu \epsilon  + \frac{C}{m} \sum_{i=1}^{m}  (\xi_{i}  + \xi_{i}' )$$
$$= - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ P+ & -1_{m}1_{m}^{\top} & 1_{m}1_{m}^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -q^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} ,$$
that is,
$$\frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ P+ & -1_{m}1_{m}^{\top} & 1_{m}1_{m}^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + C\nu \epsilon$$
$$+ \frac{C}{m} \begin{pmatrix}  \\ w^{\top} & x_{i} - & x_{j} \end{pmatrix} \sum_{i\in K\lambda}  \sum_{j\in K\mu}  \sum_{i\in K\lambda}  \sum_{j\in K\mu}$$
$$\begin{pmatrix} - & y_{i} + & y_{j}+ (p_{f}-q_{f})b -(p_{f}+ q_{f})\epsilon \\ 1 &  &  \end{pmatrix}$$
$$= -2 \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ P+ & -1_{m}1_{m}^{\top} & 1_{m}1_{m}^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -q^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} .$$
Solving for $\epsilon$  we get
$$C \begin{pmatrix} p_{f}+ q_{f} \\ \nu  - \\ m \end{pmatrix} \epsilon  = - \begin{pmatrix} \lambda^{\top} & \mu^{\top} \\  \end{pmatrix} \begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ P+ & -11_{m}^{\top} & 11^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \begin{pmatrix} y^{\top} & -y^{\top} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$- \frac{C}{m} \begin{pmatrix}  \\ w^{\top} & x_{i} - & x_{j} \end{pmatrix} \begin{pmatrix} - & y_{i} + & y_{j}+ (p_{f}-q_{f})b \end{pmatrix} \sum_{i\in K\lambda}  \sum_{j\in K\mu}^{m}  \sum_{i\in K\lambda}^{mm}  \sum_{j\in K\mu}  ,$$
