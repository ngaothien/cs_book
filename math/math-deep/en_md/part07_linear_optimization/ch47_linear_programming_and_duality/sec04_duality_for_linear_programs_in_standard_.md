# Duality for Linear Programs in Standard Form


<!-- PAGE 1654 -->
for all feasible solutions $x$ of $(P)$, so $x$ is an optimal solution of $(P)$. Similarly,
$$yb = cx \le yb$$
for all feasible solutions $y$ of $(D)$, so $y$ is an optimal solution of $(D)$. Let us now assume that $x$ is an optimal solution of $(P)$ and that $y$ is an optimal solution of $(D)$. Then as in the proof of Proposition 47.6,
$$\sum_{j=1}^{n}  c_{j}x_{j} \le \sum_{i=1j}^{m}  \sum_{=1}^{n}  y_{i}a_{ij}x_{j} \le \sum_{i=1}^{m}  y_{i}b_{i}.$$
By strong duality, since $x$ and $y$ are optimal solutions the above inequalities are actually equalities, so in particular we have
$$\sum_{j=1}^{n}  \begin{pmatrix} c_{j}- & y_{i}a_{ij} \end{pmatrix} \sum_{i=1}^{m}  x_{j} = 0.$$
$$Since x and y are feasible, x_{i} \ge 0 and y_{j} \ge 0, so if \sum_{i}  m=1 y_{i}a_{ij} > c_{j}, we must have x_{j} = 0.$$
Similarly, we have
$$\sum_{i=1}^{m}  y_{i} \begin{pmatrix} a_{ij}x_{j}-b_{i} \end{pmatrix} \sum_{j=1}^{m}  = 0,$$
$$so if \sum_{j}  m=1 a_{ij}x_{j} < b_{i}, then y_{i} = 0.$$
The equations in $(*_{D})$ and $(*_{P})$ are often called complementary slackness conditions. These conditions can be exploited to solve for an optimal solution of the primal problem with the help of the dual problem, and conversely. Indeed, if we guess a solution to one problem, then we may solve for a solution of the dual using the complementary slackness conditions, and then check that our guess was correct. This is the essence of the primal-dual method. To present this method, first we need to take a closer look at the dual of a linear program already in standard form.

## 47.4 Duality for Linear Programs in Standard Form

Let $(P)$ be a linear program in standard form, where Ax $= b$ for some $m \times  n$ matrix of rank $m$ and some objective function $x \mapsto$ cx (of course, $x \ge 0)$. To obtain the dual of $(P)$ we convert the equations Ax $= b$ to the following system of inequalities involving a (2m) $\times  n$ matrix:
$$\begin{pmatrix} A \\ -A \end{pmatrix} x \le \begin{pmatrix} b \\ -b \end{pmatrix} .$$

<!-- PAGE 1655 -->
$$\mathbb{R}^{m}$$
Then if we denote the 2m dual variables by (y', y''), with y', y'' $\in$ ( $)^{*}$, the dual of the above program is
$$minimizey'b -y''b$$
$$subject to \begin{pmatrix} y' & y'' \end{pmatrix} \begin{pmatrix} A \\ -A \end{pmatrix} \ge c and y', y''\ge 0,$$
$$\mathbb{R}^{m}$$
where y', y'' $\in$ ( $)^{*}$, which is equivalent to
$$minimize(y'-y'')b$$
$$subject to(y'-y'')A \ge c and y', y''\ge 0,$$
$$\mathbb{R}^{m}$$
where y', y'' $\in$ ( $)^{*}$. If we write $y =$ y' - y'', we find that the above linear program is equivalent to the following Linear Program $(D)$:
$$minimizeyb$$
$$subject toyA \ge c,$$
where $y \in (\mathbb{R}^{m})^{*}$. Observe that $y$ is not required to be nonnegative; it is arbitrary. Next we would like to know what is the version of Theorem 47.8 for a linear program already in standard form. This is very simple.

> **Theorem 47.12.** Consider the Linear Program (P2) in standard form
$$maximizecx$$
$$subject toAx = b and x \ge 0,$$
and its Dual $(D)$ given by
$$minimizeyb$$
$$subject toyA \ge c,$$
where $y \in (\mathbb{R}^{m})^{*}$. If the simplex algorithm applied to the Linear Program (P2) terminates with an optimal solution $(u^{*}, K^{*})$, where $u^{*}$ is a basic feasible solution and $K^{*}$ is a basis for $u^{*}$, then $y^{*} = c_{K*}A_{K*}^{-1}$ is an optimal solution for $(D)$ such that $cu^{*} = y^{*}b$. Furthermore, if we assume that the simplex algorithm is started with a basic feasible solution $(u_{0}, K_{0})$ where $K_{0} = (n-m+1, \dots  , n)$ (the indices of the last $m$ columns of $A)$ and $A_{(n-m+1,...,n)} = I_{m}$ (the last $m$ columns of $A$ constitute the identity matrix $I_{m})$, then the optimal solution $y^{*} = c_{K*}A_{K*}^{-1}$ for $(D)$ is given in terms of the reduced costs by
$$y^{*}= c_{(n-m+1,...,n)} -(\overline{c}_{K*})_{(n-m+1,...,n)},$$
and the $m\times m$ matrix consisting of last $m$ columns and the last $m$ rows of the final tableau is $A_{K*}^{-1}$.

<!-- PAGE 1656 -->

*Proof.* The proof of Theorem 47.8 applies with $A$ instead of $A$, and we can show that
$$b$$
$$c_{K*}A_{K*}^{-1}A_{N*}\ge c_{N*},$$
and that $y^{*} = c_{K*}A_{K*}^{-1}$ satisfies, $cu^{*} = y^{*}b$, and
$$y^{*}A_{K*}= c_{K*}A_{K*}^{-1}A_{K*}= c_{K*},$$
$$y^{*}A_{N*}= c_{K*}A_{K*}^{-1}A_{N*}\ge c_{N*}.$$
Let $P$ be the $n \times  n$ permutation matrix defined so that
$$AP = \begin{pmatrix} A_{K*} & A_{N*} \end{pmatrix} .$$
Then we also have
$$cP = \begin{pmatrix} c_{K*} & c_{N*} \\ we \end{pmatrix} ,$$
and using the above equations and inequalities  obtain
$$y^{*} \begin{pmatrix} A_{K*} & A_{N*} \\ equivalentto \end{pmatrix} \ge \begin{pmatrix} c_{K*} & c_{N*} \end{pmatrix} ,$$
that is, $y^{*}AP \ge$ cP, which is
$$y^{*}A \ge c,$$
which shows that $y^{*}$ is a feasible solution of $(D)$ (remember, $y^{*}$ is arbitrary so there is no need for the constraint $y^{*} \ge 0)$. The reduced costs are given by
$$(\overline{c}_{K*})_{i} = c_{i} -c_{K*}A_{K*}^{-1}A^{i},$$
and since for $j = n -m + 1, \dots  , n$ the column $A^{j}$ is the $(j + m$ -n)th column of the identity matrix $I_{m}$, we have
$$(\overline{c}_{K*})_{j} = c_{j} -(c_{K*}A_{K*}^{-1})_{j+m-n}j = n -m + 1, \dots  , n,$$
that is,
$$y^{*}= c_{(n-m+1,...,n)} -(\overline{c}_{K*})_{(n-m+1,...,n)},$$
as claimed. Since the last $m$ rows of the final tableau is obtained by multiplying $[u_{0} A]$ by $A_{K}^{-1}$, and the last $m$ columns of $A$ constitute $I_{m}$, the last $m$ rows and the last $m$ columns of $the^{*}$ final tableau constitute $A_{K*}^{-1}$. Let us now take a look at the complementary slackness conditions of Theorem 47.11. If we go back to the version of $(P)$ given by
$$maximizecx$$
$$subject to \begin{pmatrix} A \\ -A \end{pmatrix} x \le \begin{pmatrix} b \\ -b \end{pmatrix} and x \ge 0,$$
