# The Primal-Dual Algorithm


<!-- PAGE 1664 -->

## 47.6 The Primal-Dual Algorithm

Let (P2) be a linear program in standard form
$$maximizecx$$
$$subject toAx = b and x \ge 0,$$
where $A$ is an $m \times  n$ matrix of rank $m$, and $(D)$ be its dual given by
$$minimizeyb$$
$$subject toyA \ge c,$$
where $y \in (\mathbb{R}^{m})^{*}$.
$$First we may assume that b \ge 0 by changing every equation \sum_{j}  n=1 a_{ij}x_{j} = b_{i} with b_{i} < 0$$
$$to \sum_{j}  n=1 -a_{ij}x_{j} = -b_{i}. If we happen to have some feasible solution y of the dual program$$
$(D)$, we know from Theorem 47.13 that a feasible solution $x$ of (P2) is an optimal solution iff the equations in $(*_{P})$ hold. If we denote by $J$ the subset of ${1, \dots  , n}$ for which the equalities
$$yA^{j}= c_{j}$$
hold, then by Theorem 47.13 a feasible solution $x$ of (P2) is an optimal solution iff
$$x_{j} = 0for all j \in /J.$$
$$\mathbb{R}^{n}$$
Let |J| $= p$ and $N = {1, \dots  , n}$ - $J$. The above suggests looking for $x \in$ such that
$$\sum_{j\in J}  x_{j}A^{j} = b$$
$$x_{j} \ge 0for all j \in J$$
$$x_{j} = 0for all j \in /J,$$
or equivalently
$$A_{J}x_{J} = b,x_{J} \ge 0,(*_{1})$$
and
$$x_{N} = 0_{n-p}.$$
To search for such an $x$, we just need to look for a feasible $x_{J}$, and for this we can use the Restricted Primal linear program (RP) defined as follows:
$$maximize-(\xi_{1}  + \cdots  + \xi_{m} )$$
$$subject to \begin{pmatrix} A_{J} & I_{m} \end{pmatrix} \begin{pmatrix} x_{J} \\ \xi \end{pmatrix} = b and x, \xi  \ge 0.$$

<!-- PAGE 1665 -->
Since by hypothesis $b \ge 0$ and the objective function is bounded above by $0$, this linear program has an optimal solution $(x_{J}^{*}, \xi^{*}$ ).
$$\mathbb{R}^{n}$$
If $\xi^{*} = 0$, then the vector $u^{*} \in$ given by $u_{J}^{*} = x_{J}^{*}$ and $u_{N}^{*} = 0_{n-p}$ is an optimal solution of $(P)$. Otherwise, $\xi^{*} > 0$ and we have failed to solve $(*_{1})$. However we may try to use $\xi^{*}$ to improve $y$. For this consider the Dual (DRP) of $(RP)$:
$$minimizezb$$
$$subject tozA_{J} \ge 0$$
$$z \ge -1_{m}^{\top}.$$
Observe that the Program (DRP) has the same objective function as the original Dual Program $(D)$. We know by Theorem 47.12 that the optimal solution $(x_{J}^{*}, \xi^{*}$ ) of $(RP)$ yields an optimal solution $z^{*}$ of $(DRP)$ such that
$$z^{*}b = -(\xi_{1}^{*}  + \cdots  + \xi_{m}^{*} ) < 0.$$
In fact, if $K^{*}$ is the basis associated with $(x_{J}^{*}, \xi^{*}$ ) and if we write
$$A =$$
$$b \begin{pmatrix} A_{J} & I_{m} \end{pmatrix}$$
and $c = [0_{p}^{\top}$ - $1^{\top}]$, then by Theorem 47.12 we have $b$
$$z^{*}=c_{K*}A_{K*}^{-1}= -1_{m}^{\top} -(\overline{c}_{K*})_{(p+1,...,p+m)},$$
$$bb$$
where $(\overline{c}_{K*})_{(p+1,...,p+m)}$ denotes the row vector of reduced costs in the final tableau corresponding to the last $m$ columns. If we write
$$y(\theta ) = y + \theta z^{*},$$
then the new value of the objective function of $(D)$ is
$$y(\theta )b = yb + \theta z^{*}b,(*_{2})$$
and since $z^{*}b < 0$, we have a chance of improving the objective function of $(D)$, that is, decreasing its value for $\theta  > 0$ small enough if $y(\theta$ ) is feasible for $(D)$. This will be the case iff $y(\theta )A \ge c$ iff
$$yA + \theta z^{*}A \ge c.(*_{3})$$
Now since $y$ is a feasible solution of $(D)$ we have yA $\ge c$, so if $z^{*}A \ge 0$, then $(*_{3})$ is satisfied and $y(\theta$ ) is a solution of $(D)$ for all $\theta  > 0$, which means that $(D)$ is unbounded. But this implies that $(P)$ is not feasible.

<!-- PAGE 1666 -->
Let us take a closer look at the inequalities $z^{*}A \ge 0$. For $j \in J$, since $z^{*}$ is an optimal solution of $(DRP)$, we know that $z^{*}A_{J} \ge 0$, so if $z^{*}A^{j} \ge 0$ for all $j \in N$, then (P2) is not feasible. Otherwise, there is some $j \in N = {1, \dots  , n}$ - $J$ such that
$$z^{*}A^{j}< 0,$$
and then since by the definition of $N$ we have $yA^{j} > c_{j}$ for all $j \in N$, if we pick $\theta$  such that
$$-$$
$$0 < \theta  \le \frac{yA^{j}c_{j}}{-z^{*}A^{j}} j \in N, z^{*}A^{j}< 0,$$
then we decrease the objective function $y(\theta )b =$ yb $+ \theta z^{*}b$ of $(D)$ (since $z^{*}b < 0)$. Therefore we pick the best $\theta$ , namely
$$-



$$
$$\theta^{+} = \min \frac{yA^{j}c_{j}}{-z^{*}A^{j}} j \in /J, z^{*}A^{j}< 0> 0.(*_{4})$$
Next we update $y$ to $y^{+} = y(\theta^{+}$ ) $= y + \theta^{+} z^{*}$, we create the new restricted primal with the new subset
$$J^{+}= {j \in {1, \dots  , n} | y^{+}A^{j}= c_{j}},$$
and repeat the process. Here are the steps of the primal-dual algorithm. Step $1$. Find some feasible solution $y$ of the Dual Program $(D)$. We will show later
$$that this is always possible.$$
Step $2$. Compute
$$J^{+}= {j \in {1, \dots  , n} | yA^{j}= c_{j}}.$$
Step $3$. Set $J = J^{+}$ and solve the Problem (RP) using the simplex algorithm, starting
$$from the optimal solution determined during the previous round, obtaining the$$
$$optimal solution (x_{J}^{*}, \xi^{*} ) with the basis K^{*}.$$
Step $4$.
$$If \xi^{*} = 0, then stop with an optimal solution u^{*}for (P) such that u_{J}^{*} = x_{J}^{*} and the$$
$$other components of u^{*}are zero.$$
$$Else let$$
$$z^{*}= -1_{m}^{\top} -(\overline{c}_{K*})_{(p+1,...,p+m)},$$
$$be the optimal solution of (DRP) corresponding to (x_{J}^{*}, \xi^{*} ) and the basis K^{*}.$$
$$If z^{*}A^{j}\ge 0 for all j \in /J, then stop; the Program (P) has no feasible solution.$$

<!-- PAGE 1667 -->
$$Else compute$$
$$-



$$
$$\theta^{+} = \min- \frac{yA^{j}c_{j}}{z^{*}A^{j}} j \in /J, z^{*}A^{j}< 0,y^{+}= y + \theta^{+} z^{*},$$
$$and$$
$$J^{+}= {j \in {1, \dots  , n} | y^{+}A^{j}= c_{j}}.$$
$$Go back to Step 3.$$
The following proposition shows that at each iteration we can start the Program (RP) with the optimal solution obtained at the previous iteration.

> **Proposition 47.14.** Every $j \in J$ such that $A^{j}$ is in the basis of the optimal solution $\xi^{*}$ belongs to the next index set $J^{+}$.

*Proof.* Such an index $j \in J$ correspond to a variable $\xi_{j}$  such that $\xi_{j}  > 0$, so by complementary slackness, the constraint $z^{*}A^{j} \ge 0$ of the Dual Program (DRP) must be an equality, that is, $z^{*}A^{j} = 0$. But then we have
$$y^{+}A^{j}= yA^{j}+ \theta^{+} z^{*}A^{j}= c_{j},$$
which shows that $j \in J^{+}$. If $(u^{*}, \xi^{*}$ ) with the basis $K^{*}$ is the optimal solution of the Program (RP), Proposition 47.14 together with the last property of Theorem 47.12 allows us to restart the (RP) in Step $3$ with $(u^{*}, \xi^{*} )_{K*}$ as initial solution (with basis $K^{*})$. For every $j \in J$ - $J^{+}$, column $j$ is deleted, and for every $j \in J^{+}$ - $J$, the new column $A^{j}$ is computed by multiplying $A_{K*}^{-1}$ and
$$b$$
$A^{j}$, but $A_{K*}^{-1}$ is the matrix $\Gamma^{*}$ [1:m; $p +$ 1:p $+ m]$ consisting of the last $m$ columns of $\Gamma^{*}$ in the
$$b$$
final tableau, and the new reduced $\overline{c}_{j}$ is given by $c_{j}$ - $z^{*}A^{j}$. Reusing the optimal solution of the previous (RP) may improve efficiency significantly. Another crucial observation is that for any index $j_{0} \in N$ such that $\theta^{+} = (yA^{j0}$ - $c_{j0})/(-z^{*}A^{j0})$, we have
$$y^{+}A_{j0} = yA_{j0} + \theta^{+} z^{*}A^{j0}= c_{j0},$$
and so $j_{0} \in J^{+}$. This fact that be used to ensure that the primal-dual algorithm terminates in a finite number of steps (using a pivot rule that prevents cycling); see Papadimitriou and Steiglitz $[139]$ (Theorem 5.4). It remains to discuss how to pick some initial feasible solution $y$ of the Dual Program $(D)$. If $c_{j} \le 0$ for $j = 1, \dots  , n$, then we can pick $y = 0$. If we are dealing with a minimization problem, the weight $c_{j}$ are often nonnegative, so from the point of view of maximization we will have $-c_{j} \le 0$ for all $j$, and we will be able to use $y = 0$ as a starting point. Going back to our primal problem in maximization form and its dual in minimization form, we still need to deal with the situation where $c_{j} > 0$ for some $j$, in which case there

<!-- PAGE 1668 -->
may not be any obvious $y$ feasible for $(D)$. Preferably we would like to find such a $y$ very cheaply. There is a trick to deal with this situation. We pick some very large positive number $M$ and add to the set of equations Ax $= b$ the new equation
$$x_{1} + \cdots  + x_{n} + x_{n+1} = M,$$
with the new variable $x_{n+1}$ constrained to be nonnegative. If the Program $(P)$ has a feasible solution, such an $M$ exists. In fact it can shown that for any basic feasible solution $u = (u_{1}, \dots  , u_{n})$, each $|u_{i}|$ is bounded by some expression depending only on $A$ and $b$; see Papadimitriou and Steiglitz $[139]$ (Lemma 2.1). The proof is not difficult and relies on the fact that the inverse of a matrix can be expressed in terms of certain determinants (the adjugates). Unfortunately, this bound contains $m$! as a factor, which makes it quite impractical. Having added the new equation above, we obtain the new set of equations
$$\begin{pmatrix} A \\ 0_{n} \\ 1_{n}^{\top} & 1 \end{pmatrix} \begin{pmatrix} x \\ x_{n+1} \end{pmatrix} = \begin{pmatrix} b \\ M \end{pmatrix} ,$$
with $x \ge 0, x_{n+1} \ge 0$, and the new objective function given by
$$\begin{pmatrix} c & 0 \end{pmatrix} \begin{pmatrix} x \\ x_{n+1} \end{pmatrix} = cx.$$
The dual of the above linear program is
$$minimizeyb + y_{m+1}M$$
$$subject toyA^{j}+ y_{m+1} \ge c_{j}j = 1, \dots  , n$$
$$y_{m+1} \ge 0.$$
If $c_{j} > 0$ for some $j$, observe that the linear form $y$ given by
$$e$$
$$($$
$$0if 1 \le i \le m$$
$$y_{i} =$$
$$emax_{1\le j\le n}{c_{j}} > 0$$
is a feasible solution of the new dual program. In practice, we can choose $M$ to be a number close to the largest integer representable on the computer being used. Here is an example of the primal-dual algorithm given in the Math $588$ class notes of $T$. Molla $[132]$.

> **Example 47.3.** Consider the following linear program in standard form:
$$Maximize-x_{1} -3x_{2} -3x_{3} -x_{4}$$
$$subject to \begin{pmatrix} 3 & 4 & -3 & 1 \\ 3 & -2 & 6 & -1 \\ 6 & 4 & 0 & 1 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \\ x_{4} \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ 4 \end{pmatrix} and x_{1}, x_{2}, x_{3}, x_{4} \ge 0.$$

<!-- PAGE 1669 -->
The associated Dual Program $(D)$ is
$$Minimize2y_{1} + y_{2} + 4y_{3}$$
$$subject to \begin{pmatrix} y_{1} & y_{2} & y_{3} \end{pmatrix} \begin{pmatrix} 3 & 4 & -3 & 1 \\ 3 & -2 & 6 & -1 \\ 6 & 4 & 0 & 1 \end{pmatrix} \ge \begin{pmatrix} -1 & -3 & -3 & -1 \end{pmatrix} .$$
We initialize the primal-dual algorithm with the dual feasible point $y = (-1/3 0 0)$. Observe that only the first inequality of $(D)$ is actually an equality, and hence $J = {1}$. We form the Restricted Primal Program (RP1)
$$Maximize-(\xi_{1}  + \xi_{2}  + \xi_{3} )$$
$$subject to \begin{pmatrix} 3 & 1 & 0 & 0 \\ 3 & 0 & 1 & 0 \\ 6 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x_{1} \\ \xi_{1} \\ \xi_{2} \\ \xi_{3} \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ 4 \end{pmatrix} and x_{1}, \xi_{1} , \xi_{2} , \xi_{3}  \ge 0.$$
We now solve (RP1) via the simplex algorithm. The initial tableau with $K = (2, 3, 4)$ and $J = {1}$ is
$$\frac{\overline{x}_{1}\overline{\xi}_{1}\overline{\xi}_{2}\overline{\xi}_{3}}{712000}$$
$$\xi_{1}  = 23100.$$
$$\xi_{2}  = 13010$$
$$\frac{\xi_{3} = 46001}{(x_{1}, \xi_{1} , \xi_{2} , \xi_{3} )=(0, 2, 1, 4),}$$
For (RP1), cˆ $= (0, -1, -1, -1)$,    and the nonzero reduced cost is given by
$$0 -(-1 -1 -1) \begin{pmatrix} 3 \\ 3 \\ 6 \end{pmatrix} = 12.$$
Since there is only one nonzero reduced cost, we must set $j^{+} = 1$. Since $min{\xi_{1} /3, \xi_{2} /3, \xi_{3} /6} = 1/3$, we see that $k^{-} = 3$ and $K = (2, 1, 4)$. Hence we pivot through the red circled $3$ (namely we divide row $2$ by $3$, and then subtract $3\times$  (row $2)$ from row $1, 6\times$  (row $2)$ from row $3$, and        obtain the tableau
$$\frac{12\times (row2)fromrow0),to}{x_{1}\xi_{1} \xi_{2} \xi_{3}}$$
$$\frac{30040}{\xi_{1} = 101-10} -$$
$$.$$
$$x_{1} = 1/3101/30$$
$$\frac{\xi_{3} = 20021}{RP} -$$
At this stage the simplex algorithm for ( $1)$ terminates since there are no positive reduced costs. Since the upper left corner of the final tableau is not zero, we proceed with Step $4$ of the primal dual algorithm and compute
$$z^{*}= (-1 -1 -1) -(0 -4 0) = (-1 3 -1),$$

<!-- PAGE 1670 -->
$$yA^{2} -c_{2} = (-1/3 0 0) \begin{pmatrix} 4 \\ -2 \\ 4 \end{pmatrix} + 3 = \frac{5}{3} ,z^{*}A^{2} = -(-1 3 -1) \begin{pmatrix} 4 \\ -2 \\ 4 \end{pmatrix} = 14,$$
$$yA^{4} -c_{4} = (-1/3 0 0) \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} + 1 = \frac{2}{3} ,z^{*}A^{4} = -(-1 3 -1) \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} = 5,$$
so
$$ $$
$$\theta^{+} = \min \frac{5}{42} , \frac{2}{15} = \frac{5}{42} ,$$
and we conclude that the new feasible solution for $(D)$ is
$$y^{+}= (-1/3 0 0) + \frac{5}{42} (-1 3 -1) = (-19/42 5/14 -5/42).$$
When we substitute $y^{+}$ into $(D)$, we discover that the first two constraints are equalities, and that the new $J$ is $J = {1, 2}$. The new Reduced Primal (RP2) is
$$Maximize-(\xi_{1}  + \xi_{2}  + \xi_{3} )$$
$$subject to \begin{pmatrix} 3 & 4 & 1 & 0 & 0 \\ 3 & -2 & 0 & 1 & 0 \\ 6 & 4 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ \xi_{1} \\ \xi_{2} \\ \xi_{3} \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ 4 \end{pmatrix} and x_{1}, x_{2}, \xi_{1} , \xi_{2} , \xi_{3}  \ge 0.$$
Once again, we solve (RP2) via the simplex algorithm, where cˆ $= (0, 0, -1, -1, -1), (x_{1}, x_{2}, \xi_{1} , \xi_{2} , \xi_{3}$ ) $= (1/3, 0, 1, 0, 2)$ and $K = (3, 1, 5)$. The initial tableau is obtained from the final tableau of the previous (RP1) by adding a column corresponding the the variable $x_{2}$, namely
$$A_{K}^{-1}b A^{2} = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1/3 & 0 \\ 0 & 2 & 1 \end{pmatrix} \begin{pmatrix} 4 \\ -2 \\ 4 \end{pmatrix} = \begin{pmatrix} 6 \\ -2/3 \\ 8 \end{pmatrix} ,$$
$$-$$
with
$$\overline{c}_{2} = c_{2} -z^{*}A^{2} = 0 - \begin{pmatrix} -1 & 3 & -1 \end{pmatrix} \begin{pmatrix} 4 \\ -2 \\ 4 \end{pmatrix} = 14,$$
and we get
$$\frac{\overline{x}_{1}\overline{x}_{2}\overline{\xi}_{1}\overline{\xi}_{2}\overline{\xi}_{3}}{30140-40}$$
$$\xi_{1}  = 1061-10.$$
$$x_{1} = 1/31-2/301/30$$
$$\xi_{3}  = 2080-21$$

<!-- PAGE 1671 -->
Note that $j^{+} = 2$ since the only positive reduced cost occurs in column $2$. Also observe that since $min{\xi_{1} /6, \xi_{3} /8} = \xi_{1} /6 = 1/6$, we set $k^{-} = 3, K = (2, 1, 5)$ and pivot along the red $6$ to obtain the tableau
$$\frac{\overline{x}_{1}\overline{x}_{2}\overline{\xi}_{1}\overline{\xi}_{2}\overline{\xi}_{3}}{2/300-7/3-5/30}$$
$$x_{2} = 1/6011/6-1/60.$$
$$x_{1} = 4/9101/92/90$$
$$\frac{\xi_{3} = 2/3004/32/31}{Since the reduced costs are either zero or negative the simplex algorithm terminates, and} --$$
we compute
$$z^{*}= (-1 -1 -1) -(-7/3 -5/3 0) = (4/3 2/3 -1),$$
$$y^{+}A^{4} -c_{4} = (-19/42 5/14 -5/42) \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} + 1 = 1/14,$$
$$z^{*}A^{4} = -(4/3 2/3 -1) \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} = 1/3,$$
so
$$\theta^{+} = \frac{3}{14} ,$$
$$y^{+}= (-19/42 5/14 -5/42) + \frac{5}{14} (4/3 2/3 -1) = (-1/6 1/2 -1/3).$$
When we plug $y^{+}$ into $(D)$, we discover that the first, second, and fourth constraints are equalities, which implies $J = {1, 2, 4}$. Hence the new Restricted Primal (RP3) is Maximize - $(\xi_{1}  + \xi_{2}  + \xi_{3}$ )
$$subject to \begin{pmatrix} 3 & 4 & 1 & 1 & 0 & 0 \\ 3 & -2 & -1 & 0 & 1 & 0 \\ 6 & 4 & 1 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{4} \\ \xi_{1} \\ \xi_{2} \\ \xi_{3} \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ 4 \end{pmatrix} and x_{1}, x_{2}, x_{4}, \xi_{1} , \xi_{2} , \xi_{3}  \ge 0.$$
The initial tableau for (RP3), with ˆc $= (0, 0, 0, -1, -1, -1), (x_{1}, x_{2}, x_{4}, \xi_{1} , \xi_{2} , \xi_{3}$ ) $= (4/9, 1/6, 0, 0, 0, 2/3)$ and $K = (2, 1, 6)$, is obtained from the final tableau of the previous (RP2) by adding a column corresponding the the variable $x_{4}$, namely
$$A_{K}^{-1}b A^{4} = \begin{pmatrix} 1/6 & -1/6 & 0 \\ 1/9 & 2/9 & 0 \\ 4/3 & 2/3 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1/3 \\ -1/9 \\ 1/3 \end{pmatrix} ,$$
$$--$$

<!-- PAGE 1672 -->
with
$$\overline{c}_{4} = c_{4} -z^{*}A^{4} = 0 - \begin{pmatrix} 4/3 & 2/3 & -1 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} = 1/3,$$
and we get
$$x_{1}x_{2}x_{4}\xi_{1} \xi_{2} \xi_{3}$$
$$2/3001/3-7/3-5/30$$
$$x_{2} = 1/6011/31/6-1/60.$$
$$x_{1} = 4/910-1/91/92/90$$
$$\xi_{3}  = 2/3001/3-4/3-2/31$$
Since the only positive reduced cost occurs in column $3$, we set $j^{+} = 3$. Furthermore since $min{x_{2}/(1/3), \xi_{3} /(1/3)} = x_{2}/(1/3) = 1/2$, we let $k^{-} = 2, K = (3, 1, 6)$, and pivot around the red circled $1/3$ to obtain
$$x_{1}x_{2}x_{4}\xi_{1} \xi_{2} \xi_{3}$$
$$1/20-10-5/2-3/20$$
$$x_{4} = 1/20311/2-1/20.$$
$$x_{1} = 1/211/301/61/60$$
$$\xi_{3}  = 1/20-10-3/2-1/21$$
At this stage there are no positive reduced costs, and we must compute
$$z^{*}= (-1 -1 -1) -(-5/2 -3/2 0) = (3/2 1/2 -1),$$
$$y^{+}A^{3} -c_{3} = (-1/6 1/2 -1/3) \begin{pmatrix} -3 \\ 6 \\ 0 \end{pmatrix} + 3 = 13/2,$$
$$z^{*}A^{3} = -(3/2 1/2 -1) \begin{pmatrix} -3 \\ 6 \\ 0 \end{pmatrix} = 3/2,$$
so
$$\theta^{+}  = \frac{13}{3} ,$$
$$y^{+}= (-1/6 1/2 -1/3) + \frac{13}{3} (3/2 1/2 -1) = (19/3 8/3 -14/3).$$

<!-- PAGE 1673 -->
We plug $y^{+}$ into $(D)$ and discover that the first, third, and fourth constraints are equalities. Thus, $J = {1, 3, 4}$ and the Restricted Primal (RP4) is Maximize - $(\xi_{1}  + \xi_{2}  + \xi_{3}$ )
$$subject to \begin{pmatrix} 3 & -3 & 1 & 1 & 0 & 0 \\ 3 & 6 & -1 & 0 & 1 & 0 \\ 6 & 0 & 1 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{3} \\ x_{4} \\ \xi_{1} \\ \xi_{2} \\ \xi_{3} \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ 4 \end{pmatrix} and x_{1}, x_{3}, x_{4}, \xi_{1} , \xi_{2} , \xi_{3}  \ge 0.$$
The initial tableau for (RP4), with cˆ $= (0, 0, 0, -1, -1, -1), (x_{1}, x_{3}, x_{4}, \xi_{1} , \xi_{2} , \xi_{3}$ ) $= (1/2, 0, 1/2, 0, 0, 1/2)$ and $K = (3, 1, 6)$ is obtained from the final tableau of the previous (RP3) by replacing the column corresponding to the variable $x_{2}$ by a column corresponding to the variable $x_{3}$, namely
$$A_{K}^{-1}b A^{3} = \begin{pmatrix} 1/2 & -1/2 & 0 \\ 1/6 & 1/6 & 0 \\ 3/2 & 1/2 & 1 \end{pmatrix} \begin{pmatrix} -3 \\ 6 \\ 0 \end{pmatrix} = \begin{pmatrix} -9/2 \\ 1/2 \\ 3/2 \end{pmatrix} ,$$
$$--$$
with
$$\overline{c}_{3} = c_{3} -z^{*}A^{3} = 0 - \begin{pmatrix} 3/2 & 1/2 & -1 \end{pmatrix} \begin{pmatrix} -3 \\ 6 \\ 0 \end{pmatrix} = 3/2,$$
and we get
$$x_{1}x_{3}x_{4}\xi_{1} \xi_{2} \xi_{3}$$
$$1/203/20-5/2-3/20$$
$$x_{4} = 1/20-9/211/2-1/20$$
$$.$$
$$x_{1} = 1/211/201/61/60$$
$$\xi_{3}  = 1/203/20-3/2-1/21$$
By analyzing the top row of reduced cost, we see that $j^{+} = 2$. Furthermore, since $min{x_{1}/(1/2), \xi_{3} /(3/2)} = \xi_{3} /(3/2) = 1/3$, we let $k^{-} = 6, K = (3, 1, 2)$, and pivot along the red circled $3/2$ to obtain
$$x_{1}x_{3}x_{4}\xi_{1} \xi_{2} \xi_{3}$$
$$0000-1-1-1$$
$$x_{4} = 2001-4-23.$$
$$x_{1} = 1/31002/31/3-1/3$$
$$x_{3} = 1/3010-1-1/32/3$$
Since the upper left corner of the final tableau is zero and the reduced costs are all $\le 0$, we are finally finished. Then $y = (19/3 8/3 -14/3)$ is an optimal solution of $(D)$, but more
