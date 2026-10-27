# Complementary Slackness Conditions


<!-- PAGE 1653 -->

> **Corollary 47.10.** The Primal Program $(P)$ has an optimal solution iff the following set of constraints is satisfiable:
$$Ax \le b$$
$$yA \ge c$$
$$cx \ge yb$$
$$x \ge 0, y \ge 0_{m}^{\top}.$$
In fact, for any feasible solution $(x^{*}, y^{*})$ of the above system, $x^{*}$ is an optimal solution of
$(P)$ and $y^{*}$ is an optimal solution of $(D)$

## 47.3 Complementary Slackness Conditions

Another useful corollary of the strong duality theorem is the following result known as the equilibrium theorem.

> **Theorem 47.11.** (Equilibrium Theorem) For any Linear Program $(P)$ and its Dual Linear Program $(D)$ (with set of inequalities Ax $\le b$ where $A$ is an $m \times  n$ matrix, and objective function $x \mapsto$ cx), for any feasible solution $x$ of $(P)$ and any feasible solution $y$ of $(D), x$ and $y$ are optimal solutions iff
$$y_{i} = 0for all i for which \sum_{j}  n=1 a_{ij}x_{j} < b_{i}(*_{D})$$
and
$$x_{j} = 0for all j for which \sum_{i}  m=1 y_{i}a_{ij} > c_{j}.(*_{P})$$

*Proof.* First assume that $(*_{D})$ and $(*_{P})$ hold. The equations in $(*_{D})$ say that $y_{i} = 0$ unless
$$\sum_{j}  n=1 a_{ij}x_{j} = b_{i}, hence$$
$$yb = \sum_{i=1}^{m}  y_{i}b_{i} = \sum_{i=1}^{m}  y \sum_{ij=1}^{n}  a_{ij}x_{j} = \sum_{i=1j}^{m}  \sum_{=1}^{n}  y_{i}a_{ij}x_{j}.$$
$$Similarly, the equations in (*_{P}) say that x_{j} = 0 unless \sum_{i}  m=1 y_{i}a_{ij} = c_{j}, hence$$
$$cx = \sum_{j=1}^{n}  c_{j}x_{j} = \sum_{j=1}^{n}  \sum_{i=1}^{m}  y_{i}a_{ij}x_{j}.$$
Consequently, we obtain
$$cx = yb.$$
By weak duality (Proposition 47.6), we have
$$cx \le yb = cx$$
