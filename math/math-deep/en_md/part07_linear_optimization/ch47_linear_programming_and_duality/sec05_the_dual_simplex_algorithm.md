# The Dual Simplex Algorithm


<!-- PAGE 1657 -->
and to the version of $(D)$ given by
$$minimizey'b -y''b$$
$$subject to \begin{pmatrix} y' & y'' \end{pmatrix} \begin{pmatrix} A \\ -A \\ Ax \end{pmatrix} \ge c and y', y''\ge 0,$$
$$\mathbb{R}^{m}$$
where y', y'' $\in$ ( $)^{*}$, since the inequalities  $\le b$ and -Ax $\le -b$ together imply that Ax $= b$, we have equality for all these inequality constraints, and so the Conditions $(*_{D})$ place no constraints at all on y' and y'', while the Conditions $(*_{P})$ assert that
$$x_{j} = 0for all j for which \sum_{i}  m=1(y_{i}' -y_{i}'' )a_{ij} > c_{j}.$$
If we write $y =$ y' - y'', the above conditions are equivalent to
$$x_{j} = 0for all j for which \sum_{i}  m=1 y_{i}a_{ij} > c_{j}.$$
Thus we have the following version of Theorem 47.11.

> **Theorem 47.13.** (Equilibrium Theorem, Version $2)$ For any Linear Program (P2) in standard form (with Ax $= b$ where $A$ is an $m \times  n$ matrix, $x \ge 0$, and objective function $x \mapsto$ cx) and its Dual Linear Program $(D)$, for any feasible solution $x$ of $(P)$ and any feasible solution $y$ of $(D), x$ and $y$ are optimal solutions iff
$$x_{j} = 0for all j for which \sum_{i}  m=1 y_{i}a_{ij} > c_{j}.(*_{P})$$
Therefore, the slackness conditions applied to a Linear Program (P2) in standard form and to its Dual $(D)$ only impose slackness conditions on the variables $x_{j}$ of the primal problem. The above fact plays a crucial role in the primal-dual method.

## 47.5 The Dual Simplex Algorithm

Given a Linear Program (P2) in standard form
$$maximizecx$$
$$subject toAx = b and x \ge 0,$$
where $A$ is an $m\times n$ matrix of rank $m$, if no obvious feasible solution is available but if $c \le 0$, rather than using the method for finding a feasible solution described in Section 46.2 we may use a method known as the dual simplex algorithm. This method uses basic solutions $(u, K)$ where Au $= b$ and $u_{j} = 0$ for all $u_{j} \in / K$, but does not require $u \ge 0$, so $u$ may not be feasible. However, $y = c_{K}A_{K}^{-1}$ is required to be feasible for the dual program
$$minimizeyb$$
$$subject toyA \ge c,$$

<!-- PAGE 1658 -->
where $y \in (\mathbb{R}^{*})^{m}$. Since $c \le 0$, observe that $y = 0_{m}^{\top}$ is a feasible solution of the dual. If a basic solution $u$ of (P2) is found such that $u \ge 0$, then cu $=$ yb for $y = c_{K}A_{K}^{-1}$ , and we have found an optimal solution $u$ for (P2) and $y$ for $(D)$. The dual simplex method makes progress by attempting to make negative components of $u$ zero and by decreasing the objective function of the dual program. The dual simplex method starts with a basic solution $(u, K)$ of Ax $= b$ which is not feasible but for which $y = c_{K}A_{K}^{-1}$ is dual feasible. In many cases the original linear program is specified by a set of inequalities Ax $\le b$ with some $b_{i} < 0$, so by adding slack variables it is easy to find such basic solution $u$, and if in addition $c \le 0$, then because the cost associated with slack variables is $0$, we see that $y = 0$ is a feasible solution of the dual. Given a basic solution $(u, K)$ of Ax $= b$ (feasible or not), $y = c_{K}A_{K}^{-1}$ is dual feasible iff $c_{K}A_{K}^{-1} A \ge c$, and since $c_{K}A_{K}^{-1} A_{K} = c_{K}$, the inequality $c_{K}A_{K}^{-1} A \ge c$ is equivalent to $c_{K}A_{K}^{-1} A_{N} \ge c_{N}$, that is,
$$c_{N} -c_{K}A_{K}^{-1} A_{N} \le 0,(*_{1})$$
where $N = {1, \dots  , n}$ - $K$. Equation $(*_{1})$ is equivalent to
$$c_{j} -c_{K}\gamma_{K}^{j}  \le 0for all j \in N,(*_{2})$$
where $\gamma_{K}^{j}  = A_{K}^{-1} A^{j}$. Recall that the notation $\overline{c}_{j}$ is used to denote $c_{j}$ - $c_{K}\gamma_{K}^{j}$ , which is called the reduced cost of the variable $x_{j}$. As in the simplex algorithm we need to decide which column $A^{k}$ leaves the basis $K$ and which column $A^{j}$ enters the new basis $K^{+}$, in such a way that $y^{+} = c_{K+}A_{K}^{-1}$  is a feasible solution of $(D)$, that is, $c_{N+}$ - $c_{K+}A_{K}^{-1} A_{N+} \le 0$, where $N^{+} = {1, \dots  , n} -^{+}K^{+}$. We use Proposition 46.2 to decide wich $column^{+} k^{-}$ should leave the basis. Suppose $(u, K)$ is a solution of Ax $= b$ for which $y = c_{K}A_{K}^{-1}$ is dual feasible. Case $(A)$. If $u \ge 0$, then $u$ is an optimal solution of (P2). Case $(B)$. There is some $k \in K$ such that $u_{k} < 0$. In this case pick some $k^{-} \in K$ such that $u_{k-} < 0$ (according to some pivot rule). Case (B1). Suppose that $\gamma_{k-}^{j} \ge 0$ for all $j \in / K$ (in fact, for all $j$, since $\gamma_{k-}^{j} \in {0, 1}$ for all $j \in K)$. If so, we we claim that (P2) is not feasible. Indeed, let $v$ be some basic feasible solution. We have $v \ge 0$ and Av $= b$, that is,
$$\sum_{j=1}^{n}  v_{j}A^{j} = b,$$
so by multiplying both sides by $A_{K}^{-1}$ and using the fact that by definition $\gamma_{K}^{j}  = A_{K}^{-1} A^{j}$, we obtain
$$\sum_{j=1}^{n}  v_{j}\gamma_{K}^{j}  = A_{K}^{-1} b = u_{K}.$$

<!-- PAGE 1659 -->
But recall that by hypothesis $u_{k-} < 0$, yet $v_{j} \ge 0$ and $\gamma_{k-}^{j} \ge 0$ for all $j$, so the component of index $k^{-}$ is zero or positive on the left, and negative on the right, a contradiction. Therefore,
(P2) is indeed not feasible. Case (B2). We have $\gamma_{k-}^{j} < 0$ for some $j$. We pick the column $A^{j}$ entering the basis among those for which $\gamma_{k-}^{j} < 0$. Since we assumed that $c_{j}$ - $c_{K}\gamma_{K}^{j}  \le 0$ for all $j \in N$ by $(*_{2})$, consider
$$ -







$$
$$\mu^{+} = \max- \frac{c_{j}c_{K}\gamma_{K}^{j}}{\gamma_{k-}^{j}} \gamma_{k-}^{j} < 0, j \in N= \max- \frac{\overline{c}_{j}}{\gamma_{k-}^{j}} \gamma_{k-}^{j} < 0, j \in N\le 0,$$
and the set
$$



$$
$$N(\mu^{+} ) =j \in N - \frac{\overline{c}_{j}}{\gamma_{k-}^{j}} = \mu^{+} .$$
We pick some index $j^{+} \in N(\mu^{+}$ ) as the index of the column entering the basis (using some pivot rule). Recall that by hypothesis $c_{i}$ - $c_{K}\gamma_{K}^{i}  \le 0$ for all $j \in / K$ and $c_{i}$ - $c_{K}\gamma_{K}^{i}  = 0$ for all $i \in K$. Since $\gamma_{k-}^{j+} < 0$, for any index $i$ such that $\gamma_{k-}^{i} \ge 0$, we have $-\gamma_{k-}^{i} /\gamma_{k-}^{j+} \ge 0$, and since by Proposition 46.2
$$c_{i} -c_{K+}\gamma_{K+}^{i}  = c_{i} -c_{K}\gamma_{K}^{i}  - \frac{\gamma_{k-}^{i}}{\gamma_{k-}^{j+}} (c_{j+} -c_{K}\gamma_{K}^{j+}  ),$$
we have $c_{i}$ - $c_{K+}\gamma_{K+}^{i}  \le 0$. For any index $i$ such that $\gamma_{k-}^{i} < 0$, by the choice of $j^{+} \in K^{*}$,
$$- -$$
$$- \frac{c_{i}c_{K}\gamma_{K}^{i}}{\gamma_{k-}^{i}} \le - \frac{c_{j+}c_{K}\gamma_{K}^{j+}}{\gamma_{k-}^{j+}} ,$$
so
$$c_{i} -c_{K}\gamma_{K}^{i}  - \frac{\gamma_{k-}^{i}}{\gamma_{k-}^{j+}} (c_{j+} -c_{K}\gamma_{K}^{j+}  ) \le 0,$$
and again, $c_{i}-c_{K+}\gamma_{K+}^{i}  \le 0$. Therefore, if we let $K^{+} = (K-{k^{-}})\cup {j^{+}}$, then $y^{+} = c_{K+}A_{K+}^{-1}$ is dual feasible. As in the simplex algorithm, $\theta^{+}$ is given by
$$\theta^{+} = u_{k-}/\gamma_{k-}^{j+} \ge 0,$$
and $u^{+}$ is also computed as in the simplex algorithm by
$$u_{i} -\theta^{j+} \gamma_{i}^{j+} if i \in K$$
$$$$
$$$$
$$u_{i}^{+} =\theta^{j+} if i = j^{+}.$$
$$0if i \in /K \cup {j^{+}}$$
$$$$

<!-- PAGE 1660 -->
The change in the objective function of the primal and dual program (which is the same, since $u_{K} = A_{K}^{-1} b$ and $y = c_{K}A_{K}^{-1}$ is chosen such that cu $= c_{K}u_{K} =$ yb) is the same as in the simplex algorithm, namely
$$\theta^{+} \begin{pmatrix} c^{j+}-c_{K}\gamma_{K}^{j+} \end{pmatrix} .$$
We have $\theta^{+} > 0$ and $c^{j+}$ - $c_{K}\gamma_{K}^{j+}  \le 0$, so if $c^{j+}$ - $c_{K}\gamma_{K}^{j+}  < 0$, then the objective function of the dual program decreases strictly. Case (B3). $\mu^{+} = 0$. The possibity that $\mu^{+} = 0$, that is, $c^{j+} -c_{K}\gamma_{K}^{j+}  = 0$, may arise. In this case, the objective function doesn’t change. This is a case of degeneracy similar to the degeneracy that arises in the simplex algorithm. We still pick $j^{+} \in N(\mu^{+}$ ), but we need a pivot rule that prevents cycling. Such rules exist; see Bertsimas and Tsitsiklis $[21]$ (Section 4.5) and Papadimitriou and Steiglitz $[139]$ (Section 3.6). The reader surely noticed that the dual simplex algorithm is very similar to the simplex algorithm, except that the simplex algorithm preserves the property that $(u, K)$ is (primal) feasible, whereas the dual simplex algorithm preserves the property that $y = c_{K}A_{K}^{-1}$ is dual feasible. One might then wonder whether the dual simplex algorithm is equivalent to the simplex algorithm applied to the dual problem. This is indeed the case, there is a one-to-one correspondence between the dual simplex algorithm and the simplex algorithm applied to the dual problem in maximization form. This correspondence is described in Papadimitriou and Steiglitz $[139]$ (Section 3.7). The comparison between the simplex algorithm and the dual simplex algorithm is best illustrated if we use a description of these methods in terms of (full) tableaux. Recall that a (full) tableau     organized as follows:
$$\frac{isan(m + 1) \times  (n + 1)matrix}{-c_{K}u_{K}\overline{c}_{1}\cdots \overline{c}_{j}\cdots \overline{c}_{n}}$$
$$u_{k1}\gamma_{1}^{1} \cdots \gamma_{1}^{j} \cdots \gamma_{1}^{n}$$
$$\vdots \vdots \vdots \vdots$$
$$u_{km}\gamma_{m}^{1} \cdots \gamma_{m}^{j} \cdots \gamma_{m}^{n}$$
The top row contains the current value of the objective function and the reduced costs, the first column except for its top entry contain the components of the current basic solution $u_{K}$, and the remaining columns except for their top entry contain the vectors $\gamma_{K}^{j}$ . Observe that the $\gamma_{K}^{j}$  corresponding to indices $j$ in $K$ constitute a permutation of the identity matrix $I_{m}$. A tableau together with the new basis $K^{+} = (K -{k^{-}}) \cup {j^{+}}$ contains all the data needed to compute the new $u_{K+}$, the new $\gamma_{K+}^{j}$ , and the new reduced $costs\overline{c}_{i} -(\gamma_{k-}^{i} /\gamma_{k-}^{j+} )\overline{c}_{j+}$. When executing the simplex algorithm, we have $u_{k} \ge 0$ for all $k \in K$ (and $u_{j} = 0$ for all $j \in / K)$, and the incoming column $j^{+}$ is determined by picking one of the column indices such that $\overline{c}_{j} > 0$. Then the index $k^{-}$ of the leaving column is determined by looking at the minimum of the ratios $u_{k}/\gamma_{k}^{j+}$ for which $\gamma_{k}^{j+} > 0$ (along column $j^{+})$.

<!-- PAGE 1661 -->
On the other hand, when executing the dual simplex algorithm, we have $\overline{c}_{j} \le 0$ for all $j \in / K$ (and $\overline{c}_{k} = 0$ for all $k \in K)$, and the outgoing column $k^{-}$ is determined by picking one of the row indices such that $u_{k} < 0$. The index $j^{+}$ of the incoming column is determined by looking at the maximum of the ratios $-\overline{c}_{j}/\gamma_{k-}^{j}$ for which $\gamma_{k-}^{j} < 0$ (along row $k^{-})$. More details about the comparison between the simplex algorithm and the dual simplex algorithm can be found in Bertsimas and Tsitsiklis $[21]$ and Papadimitriou and Steiglitz $[139]$. Here is an example of the the dual simplex method.

> **Example 47.2.** Consider the following linear program in standard form: Maximize - $4x_{1}$ - $2x_{2}$ - $x_{3}$
$$subject to \begin{pmatrix} -1 & -1 & 2 & 1 & 0 & 0 \\ -4 & -2 & 1 & 0 & 1 & 0 \\ 1 & 1 & 4 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \\ x_{4} \\ x_{5} \\ x_{6} \end{pmatrix} = \begin{pmatrix} -3 \\ -4 \\ 2 \end{pmatrix} and x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{6} \ge 0.$$
$$-$$
$$We initialize the dual simplex procedure with (u, K) where u = \begin{pmatrix} 0 \\ 0 \\ 0 \\ -3 \\ -4 \\ 2 \end{pmatrix} and K = (4, 5, 6).$$
The initial tableau, before explicitly calculating the reduced cost, is
$$\frac{\overline{0}\overline{c}_{1}\overline{c}_{2}\overline{c}_{3}\overline{c}_{4}\overline{c}_{5}\overline{c}_{6}}{u_{4}= -3-1-12100}$$
$$.$$
$$u_{5} = -4-4-21010$$
$$u_{6} = 211-4001$$
Since $u$ has negative coordinates, Case $(B)$ applies, and we will set $k^{-} = 4$. We must now determine whether Case (B1) or Case (B2) applies. This determination is accomplished by scanning the first three columns in the tableau and observing each column has a negative entry. Thus Case (B2) is applicable, and we need to determine the reduced costs. Observe that $c = (-4, -2, -1, 0, 0, 0)$, which in turn implies $c_{(4,5,6)} = (0, 0, 0)$. Equation $(*_{2})$ implies

<!-- PAGE 1662 -->
that the nonzero reduced costs are
$$\overline{c}_{1} = c_{1} -c_{(4,5,6)}= -4$$
$$\overline{c}_{2} = c_{2} -c_{(4,5,6)} \begin{pmatrix} -1 \\ -4 \\ 1 \\ -1 \\ -2 \\ 1 \\ -2 \\ 1 \\ 4 \end{pmatrix} = -2$$
$$\overline{c}_{3} = c_{3} -c_{(4,5,6)}= -1,$$
and our tableau becomes
$$\frac{\overline{0}\overline{4}\overline{2}\overline{1}\overline{0}\overline{0}\overline{0}}{u_{4}= -3-1-12100} \overline{-}\overline{-}\overline{-}$$
$$.$$
$$u_{5} =4421010$$
$$\frac{u_{6}= 2 --1-14001}{rowisthefirstrowofthetableau.To} -$$
Since $k^{-} = 4$, our pivot          determine candidates for $j^{+}$, we scan this row, locate negative entries and compute
$$



- -$$
$$\mu^{+} = \max- \frac{\overline{c}_{j}}{\gamma_{4}^{j}} \gamma_{4}^{j}  < 0, j \in {1, 2, 3}= \max \frac{2}{1} , \frac{4}{1} = -2.$$
Since $\mu^{+}$ occurs when $j = 2$, we set $j^{+} = 2$. Our new basis is $K^{+} = (2, 5, 6)$. We must normalize the first row of the tableau, namely multiply by $-1$, then add twice this normalized row to the second row, and subtract the normalized row from the third row to obtain the updated tableau.
$$\frac{\overline{0}\overline{4}\overline{2}\overline{1}\overline{0}\overline{0}\overline{0}}{u_{2}= 311-2-100} \overline{-}\overline{-}\overline{-}$$
$$u_{5} = 2203210$$
$$\frac{u_{6}=1-00-2-101}{reducedcostsandthevalueofthe} --$$
It remains to update the        objective function by adding twice the normalized row to the top row.
$$\frac{\overline{6}\overline{2}\overline{0}\overline{5}\overline{2}\overline{0}\overline{0}}{u_{2}= 311-2-100} \overline{-}\overline{-}\overline{-}$$
$$u_{5} = 2-20-3-210$$
$$u_{6} = -100-2101$$
We now repeat the procedure of Case (B2) and set $k^{-} = 6$ (since this is the only negative entry of $u^{+})$. Our pivot row is now the third row of the updated tableau, and the new $\mu^{+}$

<!-- PAGE 1663 -->
becomes
$$



-$$
$$\mu^{+} = \max- \frac{\overline{c}_{j}}{\gamma_{6}^{j}} \gamma_{6}^{j}  < 0, j \in {1, 3, 4}= \max \frac{5}{2} = - \frac{5}{2} ,$$
which implies that $j^{+} = 3$. Hence the new basis is $K^{+} = (2, 5, 3)$, and we update the tableau by taking $-_{2}^{1}$ of Row $3$, adding twice the normalized Row $3$ to Row $1$, and adding three times the normalized Row $3$ to Row $2$.
$$6-20-5-200$$
$$u_{2} = 4110-20-1$$
$$u_{5} = 7/2-200-7/21-3/2$$
$$u_{3} = 1/2001-1/20-1/2$$
It remains to update the objective function and the reduced costs by adding five times the normalized row to the top row.
$$17/2-200-9/20-5/2$$
$$u_{2} = 4110-20-1$$
$$u_{5} = 7/2-200-^{7}1-3/2$$
$$u_{3} = 1/2001-1^{2}/20-1/2$$
Since $u^{+}$ has no negative entries, the dual simplex method terminates and objective function $-4x_{1}$ - $2x_{2}$ - $x_{3}$ is maximized with $-_{2}^{17}$ at $(0, 4,_{2}^{1}$ ). See Figure 47.5.
$$z =$$
$$1/$$
$$2$$
$$(0, 4, 1/2)$$

![Figure 47.5](../../assets/ch47/fig_47_5.png)

**Figure 47.5:** The objective function $-4x_{1}-2x_{2}-x_{3}$ is maximized at the intersection between the blue plane $-x_{1}$ - $x_{2} + 2x_{3} = -3$ and the pink plane $x_{1} + x_{2}$ - $4x_{3} = 2$.
