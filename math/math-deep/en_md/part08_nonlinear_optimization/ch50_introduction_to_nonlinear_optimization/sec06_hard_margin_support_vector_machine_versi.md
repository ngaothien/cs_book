# Hard Margin Support Vector Machine; Version II


<!-- PAGE 1799 -->

## 50.6 Hard Margin Support Vector Machine; Version II

Since $\delta  > 0$ (otherwise the data would not be separable into two disjoint sets), we can divide the affine constraints by $\delta$  to obtain
$$w^{'\top}u_{i} -b'\ge 1i = 1, \dots  , p$$
$$-w^{'\top}v_{j} + b'\ge 1j = 1, \dots  , q,$$
except that now, w' is not necessarily a unit vector. To obtain the distances to the hyperplane $H$, we need to divide by $\|w'\|$ and then we have
$$-$$
$$\frac{w^{'\top}u_{i}b'}{\|w'\|} \ge \frac{1}{\|w'\|} i = 1, \dots  , p$$
$$-$$
$$\frac{w^{'\top}v_{j}+ b'}{\|w'\|} \ge \frac{1}{\|w'\|} j = 1, \dots  , q,$$
which means that the shortest distance from the data points to the hyperplane is $1/ \|w'\|$. Therefore, we wish to maximize $1/ \|w'\|$, that is, to minimize $\|w'\|$, so we obtain the following optimization Problem $(SVM_{h2})$: Hard margin SVM $(SVM_{h2})$:
$$minimize \frac{1}{2} \|w\|^{2}$$
$$subject to$$
$$w^{\top}u_{i} -b \ge 1i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge 1j = 1, \dots  , q.$$
The objective function J(w) $= 1/2 \|w\|^{2}$ is convex, so Proposition 50.7 applies and gives us a necessary and sufficient condition for having a minimum in terms of the KKT conditions. First observe that the trivial solution $w = 0$ is impossible, because the blue constraints would be
$$-b \ge 1,$$
that is $b \le -1$, and the red constraints would be
$$b \ge 1,$$
but these are contradictory. Our goal is to find $w$ and $b$, and optionally, $\delta$ . We proceed in four steps first demonstrated on the following example. Suppose that $p = q = n = 2$, so that we have two blue points
$$u_{1}^{\top} = (u_{11}, u_{12})u_{2}^{\top} = (u_{21}, u_{22}),$$

<!-- PAGE 1800 -->
two red points
$$v_{1}^{\top} = (v_{11}, v_{12})v_{2}^{\top} = (v_{21}, v_{22}),$$
and
$$w^{\top}= (w_{1}, w_{2}).$$
Step $1$: Write the constraints in matrix form. Let
$$C = \begin{pmatrix} -u_{11} & -u_{12} & 1 \\ -u_{21} & -u_{22} & 1 \\ v_{11} & v_{12} & -1 \\ v_{21} & v_{22} & 1 \end{pmatrix} d = \begin{pmatrix} -1 \\ -1 \\ -1 \\ 1 \end{pmatrix} .(M)$$
$$--$$
The constraints become
$$C \begin{pmatrix} w \\ b \end{pmatrix} = \begin{pmatrix} -u_{11} & -u_{12} & 1 \\ -u_{21} & -u_{22} & 1 \\ v_{11} & v_{12} & -1 \\ v_{21} & v_{22} & 1 \end{pmatrix} \begin{pmatrix} w_{1} \\ w_{2} \\ b \end{pmatrix} \le \begin{pmatrix} -1 \\ -1 \\ -1 \\ 1 \end{pmatrix} .(C)$$
$$--$$
Step $2$: Write the objective function in matrix form.
$$J(w_{1}, w_{2}, b) = \frac{1}{2} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} w_{1} \\ w_{2} \\ b \end{pmatrix} .(O)$$
$$\begin{pmatrix} w_{1} & w_{2} & b \end{pmatrix}$$
Step $3$: Apply Proposition 50.7 to solve for $w$ in terms of $\lambda$  and $\mu$ . We obtain
$$\begin{pmatrix} w_{1} \\ w_{2} \\ 0 \end{pmatrix} + \begin{pmatrix} -u_{11} & -u_{21} & v_{11} & v_{21} \\ -u_{12} & -u_{22} & v_{12} & v_{22} \\ 1 & 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} \lambda_{1} \\ \lambda_{2} \\ \mu_{1} \\ \mu_{2} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} ,$$
$$--$$
i.e.
$$\nabla J_{(w,b)} + C^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = 0_{3},\lambda^{\top} = (\lambda_{1} , \lambda_{2} ), \mu^{\top} = (\mu_{1} , \mu_{2} ).$$
Then
$$\begin{pmatrix} w_{1} \\ w_{2} \\ 0 \end{pmatrix} = \begin{pmatrix} u_{11} & u_{21} & -v_{11} & -v_{21} \\ u_{12} & u_{22} & -v_{12} & -v_{22} \\ 1 & 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} \lambda_{1} \\ \lambda_{2} \\ \mu_{1} \\ \mu_{2} \end{pmatrix} ,$$
$$--$$
which implies
$$w = \begin{pmatrix} w_{1} \\ w_{2} \end{pmatrix} = \lambda_{1} \begin{pmatrix} u_{11} \\ u_{12} \end{pmatrix} + \lambda_{2} \begin{pmatrix} u_{21} \\ u_{22} \end{pmatrix} -\mu_{1} \begin{pmatrix} v_{11} \\ v_{12} \end{pmatrix} -\mu_{2} \begin{pmatrix} v_{21} \\ v_{22} \end{pmatrix} (*_{1})$$

<!-- PAGE 1801 -->
with respect to
$$\mu_{1}  + \mu_{2}  -\lambda_{1}  -\lambda_{2}  = 0.(*_{2})$$
$$Step 4: Rewrite the constraints at (C) using (*_{1}). In particular C \begin{pmatrix} w \\ b \end{pmatrix} \le d becomes$$
$$\begin{pmatrix} -u_{11} & -u_{12} & 1 \\ -u_{21} & -u_{22} & 1 \\ v_{11} & v_{12} & -1 \\ v_{21} & v_{22} & 1 \end{pmatrix} \begin{pmatrix} u_{11} & u_{21} & -v_{11} & -v_{21} & 0 \\ u_{12} & u_{22} & -v_{21} & -v_{22} & 0 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} \lambda_{1} \\ \lambda_{2} \\ \mu_{1} \\ \mu_{2} \\ b \end{pmatrix} \le \begin{pmatrix} -1 \\ -1 \\ -1 \\ 1 \end{pmatrix} .$$
$$--$$
Rewriting the previous equation in “block” format gives us
$$- \begin{pmatrix} -u_{11} & -u_{12} \\ -u_{21} & -u_{22} \\ v_{11} & v_{12} \\ v_{21} & v_{22} \end{pmatrix} \begin{pmatrix} -u_{11} & -u_{21} & v_{11} & v_{21} \\ -u_{12} & -u_{22} & v_{21} & v_{22} \end{pmatrix} \begin{pmatrix} \lambda_{1} \\ \lambda_{2} \\ \mu_{1} \\ \mu_{2} \end{pmatrix} + b \begin{pmatrix} 1 \\ 1 \\ -1 \\ 1 \end{pmatrix} + \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} \le \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} ,$$
$$-$$
which with the definition
$$X = \begin{pmatrix} -u_{11} & -u_{21} & v_{11} & v_{21} \\ -u_{12} & -u_{22} & v_{21} & v_{22} \end{pmatrix}$$
yields
$$-X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + b \begin{pmatrix} 1_{2} \\ -1_{2} \end{pmatrix} + 1_{4} \le 0_{4}.(*_{3})$$
Let us now consider the general case. Step $1$: Write the constraints in matrix form. First we rewrite the constraints as
$$-u_{i}^{\top} w + b \le -1i = 1, \dots  , p$$
$$v_{j}^{\top} w -b \le -1j = 1, \dots  , q,$$
$$\mathbb{R}^{p+q}$$
and we get the $(p + q) \times  (n + 1)$ matrix $C$ and the vector $d \in$ given by
$$C = \begin{pmatrix} -u_{1}^{\top} & 1 \\ \vdots & \vdots \\ -u_{p}^{\top} & 1 \\ v_{1}^{\top} & -1 \\ \vdots & \vdots \\ v_{q}^{\top} & 1 \end{pmatrix} ,d = \begin{pmatrix} -1 \\ \vdots \\ -1 \end{pmatrix} ,$$
$$-$$
so the set of inequality constraints is
$$C \begin{pmatrix} w \\ b \end{pmatrix} \le d.$$

<!-- PAGE 1802 -->
Step $2$: The objective function in matrix form is given by
$$J(w, b) = \frac{1}{2} \begin{pmatrix} w^{\top} & b \end{pmatrix} \begin{pmatrix} I_{n} & 0_{n} \\ 0_{n}^{\top} & 0 \end{pmatrix} \begin{pmatrix} w \\ b \end{pmatrix} .$$
Note that the corresponding matrix is symmetric positive semidefinite, but it is not invertible. Thus, the function $J$ is convex but not strictly convex. This will cause some minor trouble in finding the dual function of the problem.
$$\mathbb{R}^{p} \mathbb{R}^{q}$$
Step $3$: If we introduce the generalized Lagrange multipliers $\lambda  \in$ and $\mu  \in$ , according to Proposition 50.7, the first KKT condition is
$$\nabla J_{(w,b)} + C^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = 0_{n+1},$$
with $\lambda  \ge 0, \mu  \ge 0$. By the result of Example 39.8,
$$\nabla J_{(w,b)} = \begin{pmatrix} I_{n} & 0_{n} \\ 0_{n}^{\top} & 0 \end{pmatrix} \begin{pmatrix} w \\ b \end{pmatrix} = \begin{pmatrix} w \\ 0 \end{pmatrix} ,$$
so we get
$$\begin{pmatrix} w \\ 0 \end{pmatrix} = -C^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} ,$$
that is,
$$\begin{pmatrix} w \\ 0 \end{pmatrix} = \begin{pmatrix} u \\ \cdots & u_{p} & -v_{1} & \cdots & -v_{q} \\ -^{1}1 & \cdots & -1 & 1 & \cdots & 1 \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} .$$
Consequently,
$$w = \sum_{i=1}^{p}  \lambda_{i} u_{i} - \sum_{j=1}^{q}  \mu_{j} v_{j},(*_{1})$$
and
$$\sum_{j=1}^{q}  \mu_{j}  - \sum_{i=1}^{p}  \lambda_{i}  = 0.(*_{2})$$
Step $4$: Rewrite the constraint using $(*_{1})$. Plugging the above expression for $w$ into the
$$constraints C \begin{pmatrix} w \\ b \end{pmatrix} \le d we get$$
$$\begin{pmatrix} -u_{1}^{\top} & 1 \\ \vdots & \vdots \\ -u_{p}^{\top} & 1 \\ v_{1}^{\top} & -1 \\ \vdots & \vdots \\ v_{q}^{\top} & 1 \end{pmatrix} \begin{pmatrix} u_{1} & \cdots & u_{p} & -v_{1} & \cdots & -v_{q} & 0_{n} \\ 0 & \cdots & 0 & 0 & \cdots & 0 & 1 \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \\ b \end{pmatrix} \le \begin{pmatrix} -1 \\ \vdots \\ -1 \end{pmatrix} ,$$
$$-$$

<!-- PAGE 1803 -->
so if let $X$ be the $n \times  (p + q)$ matrix given by
$$X = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} ,$$
we obtain
$$w = -X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} ,(*_{1}')$$
and the above inequalities are written in matrix form as
$$\begin{pmatrix} 1_{p} \\ X^{\top}-1_{q} \end{pmatrix} \begin{pmatrix} -X & 0_{n} \\ 0_{p+q}^{\top} & 1 \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \\ b \end{pmatrix} \le -1_{p+q};$$
that is,
$$-X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + b \begin{pmatrix} 1_{p} \\ -1_{q} \end{pmatrix} + 1_{p+q} \le 0_{p+q}.(*_{3})$$
Equivalently, the ith inequality is
$$- \sum_{j=1}^{p}  u_{i}^{\top} u_{j}\lambda_{j}  + \sum_{k=1}^{q}  u_{i}^{\top} v_{k}\mu_{k}  + b + 1 \le 0i = 1, \dots  , p,$$
and the $(p +$ j)th inequality is
$$\sum_{i=1}^{p}  v_{j}^{\top} u_{i}\lambda_{i}  - \sum_{k=1}^{q}  v_{j}^{\top} v_{k}\mu_{k}  -b + 1 \le 0j = 1, \dots  , q.$$
We also have $\lambda  \ge 0, \mu  \ge 0$. Furthermore, if the ith inequality is inactive, then $\lambda_{i}  = 0$, and if the $(p +$ j)th inequality is inactive, then $\mu_{j}  = 0$. Since the constraints are affine and since $J$ is convex, if we can find $\lambda  \ge 0, \mu  \ge 0$, and $b$ such that the inequalities in $(*_{3})$ are satisfied, and $\lambda_{i}  = 0$ and $\mu_{j}  = 0$ when the corresponding constraint is inactive, then by Proposition 50.7 we have an optimum solution.
Remark: The second KKT condition can be written as
$$\begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} \lambda \\ -X^{\top}X & \mu \end{pmatrix} \begin{pmatrix} 1_{p} \\ + b & -1_{q} \end{pmatrix} \begin{pmatrix} + 1_{p+q} \end{pmatrix} = 0;$$
that is,
$$- \begin{pmatrix} \lambda^{\top} & \mu^{\top} \\ p \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \\ q \end{pmatrix} + b \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p} \\ -1_{q} \\ term \end{pmatrix} + \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q} = 0.$$
$$Since (*_{2}) says that \sum_{i}  =1 \lambda_{i}  = \sum  j=1 \mu_{j} , the second  is zero, and by (*_{1}') we get$$
$$w^{\top}w = \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = \sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j} .$$

<!-- PAGE 1804 -->
Thus, we obtain a simple expression for $\|w\|^{2}$ in terms of $\lambda$  and $\mu$ . The vectors $u_{i}$ and $v_{j}$ for which the $i$-th inequality is active and the $(p +$ j)th inequality is active are called support vectors. For every vector $u_{i}$ or $v_{j}$ that is not a support vector, the corresponding inequality is inactive, so $\lambda_{i}  = 0$ and $\mu_{j}  = 0$. Thus we see that only the support vectors contribute to a solution. If we can guess which vectors $u_{i}$ and $v_{j}$ are support vectors, namely, those for which $\lambda_{i}  \neq  0$ and $\mu_{j}  \neq  0$, then for each support vector $u_{i}$ we have an equation
$$- \sum_{j=1}^{p}  u_{i}^{\top} u_{j}\lambda_{j}  + \sum_{k=1}^{q}  u_{i}^{\top} v_{k}\mu_{k}  + b + 1 = 0,$$
and for each support vector $v_{j}$ we have an equation
$$\sum_{i=1}^{p}  v_{j}^{\top} u_{i}\lambda_{i}  - \sum_{k=1}^{q}  v_{j}^{\top} v_{k}\mu_{k}  -b + 1 = 0,$$
with $\lambda_{i}  = 0$ and $\mu_{j}  = 0$ for all non-support vectors, so together with the Equation $(*_{2})$ we have a linear system with an equal number of equations and variables, which is solvable if our separation problem has a solution. Thus, in principle we can find $\lambda , \mu$ , and $b$ by solving a linear system.
Remark: We can first solve for $\lambda$  and $\mu$  (by eliminating $b)$, and by $(*_{1})$ and since $w \neq  0$, there is a least some nonzero $\lambda_{i0}$  and thus some nonzero $\mu_{j0}$ , so the corresponding inequalities are equations
$$- \sum_{j=1}^{p}  u_{i0}^{\top}u_{j}\lambda_{j}  + \sum_{k=1}^{q}  u_{i0}^{\top}v_{k}\mu_{k}  + b + 1 = 0$$
$$\sum_{i=1}^{p}  v_{j0}^{\top}u_{i}\lambda_{i}  - \sum_{k=1}^{q}  v_{j0}^{\top}v_{k}\mu_{k}  -b + 1 = 0,$$
so $b$ is given in terms of $\lambda$  and $\mu$  by
$$!$$
$$b = \frac{1}{2} (u_{i0}^{\top} + v_{j0}^{\top}) \sum_{i=1}^{p}  \lambda_{i} u_{i} - \sum_{j=1}^{p}  \mu_{j} v_{j}.$$
Using the dual of the Lagrangian, we can solve for $\lambda$  and $\mu$ , but typically $b$ is not determined, so we use the above method to find $b$. The above nondeterministic procedure in which we guess which vectors are support vectors is not practical. We will see later that a practical method for solving for $\lambda$  and $\mu$  consists in maximizing the dual of the Lagrangian.

<!-- PAGE 1805 -->
If $w$ is an optimal solution, then $\delta  = 1/ \|w\|$ is the shortest distance from the support vectors to the separating hyperplane $H_{w,b}$ of equation $w^{\top}x$ - $b = 0$. If we consider the two hyperplanes $H_{w,b+1}$ and $H_{w,b-1}$ of equations
$$w^{\top}x -b -1 = 0andw^{\top}x -b + 1 = 0,$$
then $H_{w,b+1}$ and $H_{w,b-1}$ are two hyperplanes parallel to the hyperplane $H_{w,b}$ and the distance between them is $2\delta$ . Furthermore, $H_{w,b+1}$ contains the support vectors $u_{i}, H_{w,b-1}$ contains the support vectors $v_{j}$, and there are no data points $u_{i}$ or $v_{j}$ in the open region between these two hyperplanes containing the separating hyperplane $H_{w,b}$ (called a “slab” by Boyd and Vandenberghe; see $[29]$, Section 8.6). This situation is illustrated in Figure 50.14.
$$u$$
$$4u$$
$$3$$
$$= 0$$
$$- 1$$
$$- b u$$
$$w T x1$$
$$b = 0u$$
$$x -2$$
$$w  T$$
$$= 0u$$
$$x - b + 1i$$
$$wT$$
$$vv$$
$$21$$
$$vv$$
$$4j$$
$$v$$
$$3$$
$$v$$
$$5$$

![Figure 50.14](../../assets/ch50/fig_50_14.png)

**Figure 50.14:** In $\mathbb{R}^{3}$, the solution to Hard Margin $SVM_{h2}$ is the purple plane sandwiched between the red plane $w^{\top}x$ - $b + 1 = 0$ and the blue plane $w^{\top}x$ - $b$ - $1 = 0$, each of which contains the appropriate support vectors $u_{i}$ and $v_{j}$. Even if $p = 1$ and $q = 2$, a solution is not obvious. In the plane, there are four possibilities:
$(1)$ If $u_{1}$ is on the segment $(v_{1}, v_{2})$, there is no solution.
$(2)$ If the projection $h$ of $u_{1}$ onto the line determined by $v_{1}$ and $v_{2}$ is between $v_{1}$ and $v_{2}$, that is $h = (1$ - $\alpha )v_{1} + \alpha_{2} v_{2}$ with $0 \le \alpha  \le 1$, then it is the line parallel to $v_{2}$ - $v_{1}$ and equidistant to $u$ and both $v_{1}$ and $v_{2}$, as illustrated in Figure 50.15.
$(3)$ If the projection $h$ of $u_{1}$ onto the line determined by $v_{1}$ and $v_{2}$ is to the right of $v_{2}$, that is $h = (1$ - $\alpha )v_{1} + \alpha_{2} v_{2}$ with $\alpha  > 1$, then it is the bisector of the line segment $(u_{1}, v_{2})$.
$(4)$ If the projection $h$ of $u_{1}$ onto the line determined by $v_{1}$ and $v_{2}$ is to the left of $v_{1}$, that is $h = (1$ - $\alpha )v_{1} + \alpha_{2} v_{2}$ with $\alpha  < 0$, then it is the bisector of the line segment $(u_{1}, v_{1})$.

<!-- PAGE 1806 -->
$$u$$
$$v$$
$$1$$
$$v$$
$$2$$

![Figure 50.15](../../assets/ch50/fig_50_15.png)

**Figure 50.15:** The purple line, which is the bisector of the altitude of the isosceles triangle, separates the two red points from the blue point in a manner which satisfies Hard Margin $SVM_{h2}$. If $p = q = 1$, we can find a solution explicitly. Then $(*_{2})$ yields
$$\lambda  = \mu ,$$
and if we guess that the constraints are active, the corresponding equality constraints are
$$-u^{\top}u\lambda  + u^{\top}v\mu  + b + 1 = 0$$
$$u^{\top}v\lambda  -v^{\top}v\mu  -b + 1 = 0,$$
so we get
$$(-u^{\top}u + u^{\top}v)\lambda  + b + 1 = 0$$
$$(u^{\top}v -v^{\top}v)\lambda  -b + 1 = 0,$$
Adding up the two equations we find
$$(2u^{\top}v -u^{\top}u -v^{\top}v)\lambda  + 2 = 0,$$
that is
$$\lambda  = \frac{2}{(u -v)^{\top}(u -v)} .$$
By subtracting the first equation from the second, we find
$$(u^{\top}u -v^{\top}v)\lambda  -2b = 0,$$
which yields
$$- -$$
$$b = \lambda \frac{(u^{\top}uv^{\top}v)}{2} = \frac{u^{\top}uv^{\top}v}{(u -v)^{\top}(u -v)} .$$
