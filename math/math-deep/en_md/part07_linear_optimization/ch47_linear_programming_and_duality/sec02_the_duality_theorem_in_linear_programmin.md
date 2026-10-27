# The Duality Theorem in Linear Programming


<!-- PAGE 1645 -->

## 47.2 The Duality Theorem in Linear Programming

Let $(P)$ be the linear program
$$maximizecx$$
$$subject toAx \le b and x \ge 0,$$
with $A$ a $m \times  n$ matrix, and assume that $(P)$ has a feasible solution and is bounded above. Since by hypothesis the objective function $x \mapsto$ cx is bounded $on\mathcal{P}(A, b)$, it might be useful to deduce an upper bound for cx from the inequalities Ax $\le b$, for any $x \in$ P(A, $b)$. We can do this as follows: for every inequality
$$a_{i}x \le b_{i}1 \le i \le m,$$
pick a nonnegative scalar $y_{i}$, multiply both sides of the above inequality by $y_{i}$ obtaining
$$y_{i}a_{i}x \le y_{i}b_{i}1 \le i \le m,$$
(the direction of the inequality is preserved since $y_{i} \ge 0)$, and then add up these $m$ equations, which yields
$$(y_{1}a_{1} + \cdots  + y_{m}a_{m})x \le y_{1}b_{1} + \cdots  + y_{m}b_{m}.$$
If we can pick the $y_{i} \ge 0$ such that
$$c \le y_{1}a_{1} + \cdots  + y_{m}a_{m},$$
then since $x_{j} \ge 0$, we have
$$cx \le (y_{1}a_{1} + \cdots  + y_{m}a_{m})x \le y_{1}b_{1} + \cdots  + y_{m}b_{m},$$
namely we found an upper bound of the value cx of the objective function of $(P)$ for any feasible solution $x \in$ P(A, $b)$. If we let $y$ be the linear form $y = (y_{1}, \dots  , y_{m})$, then since
$$A = \begin{pmatrix} a_{1} \\ \vdots \\ a_{m} \end{pmatrix}$$
$y_{1}a_{1} + \cdots  + y_{m}a_{m} =$ yA, and $y_{1}b_{1} + \cdots  + y_{m}b_{m} =$ yb, what we did was to look for some $y \in (\mathbb{R}^{m})^{*}$ such that
$$c \le yA,y \ge 0,$$
so that we have
$$cx \le ybfor all x \in P(A, b).(*)$$
Then it is natural to look for a “best” value of yb, namely a minimum value, which leads to the definition of the dual of the linear program $(P)$, a notion due to John von Neumann.

<!-- PAGE 1646 -->

> **Definition 47.2.** Given any Linear Program $(P)$
$$maximizecx$$
$$subject toAx \le b and x \ge 0,$$
with $A$ an $m \times  n$ matrix, the dual $(D)$ of $(P)$ is the following optimization problem:
$$minimizeyb$$
$$subject toyA \ge c and y \ge 0,$$
where $y \in (\mathbb{R}^{m})^{*}$. The variables $y_{1}, \dots  , y_{m}$ are called the dual variables. The original Linear Program
$(P)$ is called the primal linear program and the original variables $x_{1}, \dots  , x_{n}$ are the primal variables. Here is an explicit example of a linear program and its dual.

> **Example 47.1.** Consider the linear program illustrated by Figure 47.3
$$maximize2x_{1} + 3x_{2}$$
$$subject to$$
$$4x_{1} + 8x_{2} \le 12$$
$$2x_{1} + x_{2} \le 3$$
$$3x_{1} + 2x_{2} \le 4$$
$$x_{1} \ge 0, x_{2} \ge 0.$$
Its dual linear program is illustrated in Figure 47.4
$$minimize12y_{1} + 3y_{2} + 4y_{3}$$
$$subject to$$
$$4y_{1} + 2y_{2} + 3y_{3} \ge 2$$
$$8y_{1} + y_{2} + 2y_{3} \ge 3$$
$$y_{1} \ge 0, y_{2} \ge 0, y_{3} \ge 0.$$
It can be checked that $(x_{1}, x_{2}) = (1/2, 5/4)$ is an optimal solution of the primal linear program, with the maximum value of the objective function $2x_{1} + 3x_{2}$ equal to $19/4$, and that $(y_{1}, y_{2}, y_{3}) = (5/16, 0, 1/4)$ is an optimal solution of the dual linear program, with the minimum value of the objective function $12y_{1} + 3y_{2} + 4y_{3}$ also equal to $19/4$. Observe that in the Primal Linear Program $(P)$, we are looking for a vector $x \in \mathbb{R}^{n}$ maximizing the form cx, and that the constraints are determined by the action of the rows of the matrix $A$ on $x$. On the other hand, in the Dual Linear Program $(D)$, we are looking
$$\mathbb{R}^{*}$$
for a linear form $y \in$ ( $)^{m}$ minimizing the form yb, and the constraints are determined by

<!-- PAGE 1647 -->
$$3$$
$$2x + y = 3$$
$$2$$
$$3x$$
$$+ 2$$
$$y =$$
$$y 4$$
$$14x + 8y$$
$$= 12$$
$$0$$
$$\overline{0}\overline{0.5}\overline{1}\overline{1.5}\overline{2}$$
$$x$$

![Figure 47.3](../../assets/ch47/fig_47_3.png)

**Figure 47.3:** The $\mathcal{H}-polytope$ for the linear program of Example 47.1. Note $x_{1} \to x$ and $x_{2} \to y$. the action of $y$ on the columns of $A$. This is the sense in which $(D)$ is the dual $(P)$. In most presentations, the fact that $(P)$ and $(D)$ perform a search for a solution in spaces that are dual to each other is obscured by excessive use of transposition. To convert the Dual Program $(D)$ to a standard maximization problem we change the objective function yb to $-b^{\top}y^{\top}$ and the inequality yA $\ge c$ to $-A^{\top}y^{\top} \le -c^{\top}$. The Dual Linear Program $(D)$ is now stated as (D')
$$maximize-b^{\top}y^{\top}$$
$$subject to-A^{\top}y^{\top}\le -c^{\top}and y^{\top}\ge 0,$$
where $y \in (\mathbb{R}^{m})^{*}$. Observe that the dual in maximization form (D'') of the Dual Program (D') gives back the Primal Program $(P)$. The above discussion established the following inequality known as weak duality.

> **Proposition 47.6.** (Weak Duality) Given any Linear Program $(P)$
$$maximizecx$$
$$subject toAx \le b and x \ge 0,$$
$$\mathbb{R}^{n}$$
with $A$ an $m \times  n$ matrix, for any feasible solution $x \in$ of the Primal Problem $(P)$ and every feasible solution $y \in (\mathbb{R}^{m})^{*}$ of the Dual Problem $(D)$, we have
$$cx \le yb.$$

> **Definition 47.3.** We say that the Dual Linear Program $(D)$ is bounded below if ${yb$ | $y^{\top} \in P(-A^{\top}, -c^{\top})}$ is bounded below.

<!-- PAGE 1648 -->
$$8x + y + 2z = 3$$
$$y$$
$$x$$
$$4x + 2y + 3z = 2$$

![Figure 47.4](../../assets/ch47/fig_47_4.png)

**Figure 47.4:** The $\mathcal{H}-polyhedron$ for the dual linear program of Example 47.1 is the spacial region “above” the pink plane and in “front” of the blue plane. Note $y_{1} \to x, y_{2} \to y$, and $y_{3} \to z$. What happens if $x^{*}$ is an optimal solution of $(P)$ and if $y^{*}$ is an optimal solution of $(D)$? We have $cx^{*} \le y^{*}b$, but is there a “duality gap,” that is, is it possible that $cx^{*} < y^{*}b$? The answer is no, this is the strong duality theorem. Actually, the strong duality theorem asserts more than this.

> **Theorem 47.7.** (Strong Duality for Linear Programming) Let $(P)$ be any linear program
$$maximizecx$$
$$subject toAx \le b and x \ge 0,$$
with $A$ an $m \times  n$ matrix. The Primal Problem $(P)$ has a feasible solution and is bounded above iff the Dual Problem $(D)$ has a feasible solution and is bounded below. Furthermore, if
$(P)$ has a feasible solution and is bounded above, then for every optimal solution $x^{*}$ of $(P)$ and every optimal solution $y^{*}$ of $(D)$, we have
$$cx^{*}= y^{*}b.$$

*Proof.* If $(P)$ has a feasible solution and is bounded above, then we know from Proposition 45.1 that $(P)$ has some optimal solution. Let $x^{*}$ be any optimal solution of $(P)$. First we will show that $(D)$ has a feasible solution $v$. Let $\mu  = cx^{*}$ be the maximum of the objective function $x \mapsto$ cx. Then for any $\epsilon  > 0$, the system of inequalities
$$Ax \le b,x \ge 0,cx \ge \mu  + \epsilon$$
has no solution, since otherwise $\mu$  would not be the maximum value of the objective function cx. We would like to apply Farkas II, so first we transform the above system of inequalities

<!-- PAGE 1649 -->
into the system
$$\begin{pmatrix} A \\ -c \end{pmatrix} x \le \begin{pmatrix} b \\ -(\mu  + \epsilon ) \end{pmatrix} .$$
By Proposition 47.4 (Farkas II), there is some linear form $(\lambda , z) \in (\mathbb{R}^{m+1})^{*}$ such that $\lambda  \ge 0, z \ge 0$,
$$\begin{pmatrix} \lambda & z \end{pmatrix} \begin{pmatrix} A \\ -c \end{pmatrix} \ge 0_{m}^{\top},$$
and
$$\begin{pmatrix} \lambda & z \end{pmatrix} \begin{pmatrix} b \\ -(\mu  + \epsilon ) \end{pmatrix} < 0,$$
which means that
$$\lambda A -zc \ge 0_{m}^{\top},\lambda b -z(\mu  + \epsilon ) < 0,$$
that is,
$$\lambda A \ge zc$$
$$\lambda b < z(\mu  + \epsilon )$$
$$\lambda  \ge 0, z \ge 0.$$
On the other hand, since $x^{*} \ge 0$ is an optimal solution of the system Ax $\le b$, by Farkas II again (by taking the negation of the equivalence), since $\lambda A \ge 0$ (for the same $\lambda$  as before), we must have
$$\lambda b \ge 0.(*_{1})$$
We claim that $z > 0$. Otherwise, since $z \ge 0$, we must have $z = 0$, but then
$$\lambda b < z(\mu  + \epsilon )$$
implies
$$\lambda b < 0,(*_{2})$$
and since $\lambda b \ge 0$ by $(*_{1})$, we have a contradiction. Consequently, we can divide by $z > 0$ without changing the direction of inequalities, and we obtain
$$\lambda$$
$$z A \ge c$$
$$\lambda$$
$$z b < \mu  + \epsilon$$
$$\frac{\lambda}{z} \ge 0,$$
which shows that $v = \lambda /z$ is a feasible solution of the Dual Problem $(D)$. However, weak duality (Proposition 47.6) implies that $cx^{*} = \mu  \le$ yb for any feasible solution $y \ge 0$ of the Dual Program $(D)$, so $(D)$ is bounded below and by Proposition 45.1 applied to the version of $(D)$ written as a maximization problem, we conclude that $(D)$ has some optimal solution.

<!-- PAGE 1650 -->
For any optimal solution $y^{*}$ of $(D)$, since $v$ is a feasible solution of $(D)$ such that vb $< \mu  + \epsilon$ , we must have
$$\mu  \le y^{*}b < \mu  + \epsilon ,$$
and since our reasoning is valid for any $\epsilon  > 0$, we conclude that $cx^{*} = \mu  = y^{*}b$. If we assume that the dual program $(D)$ has a feasible solution and is bounded below, since the dual of $(D)$ is $(P)$, we conclude that $(P)$ is also feasible and bounded above. The strong duality theorem can also be proven by the simplex method, because when it terminates with an optimal solution of $(P)$, the final tableau also produces an optimal solution $y$ of $(D)$ that can be read offthe reduced costs of columns $n + 1, \dots  , n + m$ by flipping their signs. We follow the proof in Ciarlet $[41]$ (Chapter $10)$.

> **Theorem 47.8.** Consider the Linear Program $(P)$,
$$maximizecx$$
$$subject toAx \le b and x \ge 0,$$
its equivalent version (P2) in standard form,
$$maximizecx$$
$$b b$$
$$subject toAx = b andx \ge 0,$$
$$bb b$$
where $A$ is an $m \times  (n + m)$ matrix, $c$ is a linear form in $(\mathbb{R}^{n+m})^{*}$, and $x \in \mathbb{R}^{n+m}$, given by $b  b  b$
$$Ab = \begin{pmatrix} A & I_{m} \end{pmatrix} ,bc = \begin{pmatrix} c & 0_{m}^{\top} \end{pmatrix} ,x = \begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix} ,\overline{x} = \begin{pmatrix} x_{n+1} \\ \vdots \\ x_{n+m} \end{pmatrix} ,xb = \begin{pmatrix} x \\ \overline{x} \end{pmatrix} ,$$
and the Dual $(D)$ of $(P)$ given by
$$minimizeyb$$
$$subject toyA \ge c and y \ge 0,$$
where $y \in (\mathbb{R}^{m})^{*}$. If the simplex algorithm applied to the Linear Program (P2) terminates with an optimal solution $(u^{*}, K^{*})$, where $u^{*}$ is a basic feasible solution and $K^{*}$ is a basis for
$$b b$$
$u^{*}$, then $y^{*} = c_{K*}A_{K*}^{-1}$ is an optimal solution for $(D)$ such that $cu^{*} = y^{*}b$. Furthermore, $y^{*} b  b b  b b$ is given in terms of the reduced costs by $y^{*} = -((\overline{c}_{K*})_{n+1} \dots  (\overline{c}_{K*})_{n+m})$.

*Proof.* We know that $K^{*}$ is a subset of ${1, \dots  , n + m}$ consisting of $m$ indices such that the corresponding columns of $A$ are linearly independent. Let $N^{*} = {1, \dots  , n + m}$ - $K^{*}$. The
$$b$$
simplex method terminates with an optimal solution in Case $(A)$, namely when
$$bc_{j} - \sum_{k\in k}  \gamma_{k}^{j} bc_{k} \le 0for all j \in N^{*} ,$$

<!-- PAGE 1651 -->
$$where A^{j}b= \sum_{k}  \in K*\gamma_{k}^{j}  A^{k}b, or using the notations of Section 46.3,$$
$$c_{j} -c_{K*}A_{K*}^{-1}A^{j}\le 0for all j \in N^{*} .$$
$$bbbb$$
The above inequalities can be written as
$$c_{N*}-c_{K*}A_{K*}^{-1}A_{N*}\le 0_{n}^{\top} ,$$
$$bbbb$$
or equivalently as
$$c_{K*}A_{K*}^{-1}A_{N*}\ge c_{N*}.(*_{1})$$
$$bbbb$$
The value of the objective function for the optimal solution $u^{*}$ is $cu^{*} = c_{K*}u_{K*}^{*}$, and since
$$b b b bb$$
$u_{K*}^{*}$ satisfies the equation $A_{K*}u_{K*}^{*} = b$, the value of the objective function is $b  b b$
$$c_{K*}u_{K*}^{*}=c_{K*}A_{K*}^{-1}b.(*_{2})$$
$$bb bb$$
Then if we let $y^{*} = c_{K*}A_{K*}^{-1}$, obviously we have $y^{*}b = c_{K*}u_{K*}$, so if we can prove that $y^{*}$ is a
$$bb bb$$
feasible solution of the Dual Linear program $(D)$, by weak duality, $y^{*}$ is an optimal solution of $(D)$. We have
$$y^{*}A_{K*}=c_{K*}A_{K*}^{-1}A_{K*}=c_{K*},(*_{3})$$
$$b bbb b$$
and by $(*_{1})$ we get
$$y^{*}A_{N*}=c_{K*}A_{K*}^{-1}A_{N*}\ge c_{N*}.(*_{4})$$
$$b bbbb$$
Let $P$ be the $(n + m) \times  (n + m)$ permutation matrix defined so that
$$A P =P =.$$
$$b \begin{pmatrix} A & I_{m} \end{pmatrix} \begin{pmatrix} A_{K*}b & A_{N*}b \end{pmatrix}$$
Then we also have
$$bc P = \begin{pmatrix} c & 0_{m}^{\top} \\ obtain \end{pmatrix} P = \begin{pmatrix} c_{K*} & c_{N*} \\ b & b \end{pmatrix} .$$
Using Equations $(*_{3})$ and $(*_{4})$ we
$$y^{*} \begin{pmatrix} A_{K*}b & A_{N*}b \end{pmatrix} \ge \begin{pmatrix} c_{K*} & c_{N*} \\ b & b \end{pmatrix} ,$$
that is,
$$y^{*} \begin{pmatrix} A & I_{m} \end{pmatrix} P \ge \begin{pmatrix} c & 0_{m}^{\top} \end{pmatrix} P,$$
which is equivalent to
$$y^{*} \begin{pmatrix} A & I_{m} \end{pmatrix} \ge \begin{pmatrix} c & 0_{m}^{\top} \end{pmatrix} ,$$
that is
$$y^{*}A \ge c,y \ge 0,$$
and these are exactly the conditions that say that $y^{*}$ is a feasible solution of the Dual Program $(D)$.

<!-- PAGE 1652 -->
The reduced costs are given by $(c_{K*})_{i} = c_{i}$ - $c_{K*}A_{K*}^{-1}A^{i}$, for $i = 1, \dots  , n + m$. But for
$$b bbbb$$
$i = n + j$ with $j = 1, \dots  , m$ each column $A^{n+j}$ is the jth vector of the identity matrix $I_{m}$
$$b$$
and by definition $c_{n+j} = 0$, so
$$b$$
$$(c_{K*})_{n+j} = -(c_{K*}A_{K*}^{-1})_{j} = -y_{j}^{*}j = 1, \dots  , m,$$
$$bbb$$
as claimed. The fact that the above proof is fairly short is deceptive because this proof relies on the fact that there are versions of the simplex algorithm using pivot rules that prevent cycling, but the proof that such pivot rules work correctly is quite lengthy. Other proofs are given in Matousek and Gardner $[127]$ (Chapter $6$, Sections 6.3), Chvatal $[40]$ (Chapter $5)$, and Papadimitriou and Steiglitz $[139]$ (Section 2.7). Observe that since the last $m$ rows of the final tableau are actually obtained by multipling $[u A]$ by $A_{K*}^{-1}$, the $m\times m$ matrix consisting of the last $m$ columns and last $m$ rows of the final $b  b$ tableau is $A_{K*}^{-1}$ (basically, the simplex algorithm has performed the steps of a Gauss–Jordan
$$b$$
reduction). This fact allows saving some steps in the primal dual method. By combining weak duality and strong duality, we obtain the following theorem which shows that exactly four cases arise.

> **Theorem 47.9.** (Duality Theorem of Linear Programming) Let $(P)$ be any linear program
$$maximizecx$$
$$subject toAx \le b and x \ge 0,$$
and let $(D)$ be its dual program
$$minimizeyb$$
$$subject toyA \ge c and y \ge 0,$$
with $A$ an $m \times  n$ matrix. Then exactly one of the following possibilities occur:
$(1)$ Neither $(P)$ nor $(D)$ has a feasible solution.
$(2) (P)$ is unbounded and $(D)$ has no feasible solution.
$(3) (P)$ has no feasible solution and $(D)$ is unbounded.
$(4)$ Both $(P)$ and $(D)$ have a feasible solution. Then both have an optimal solution, and for every optimal solution $x^{*}$ of $(P)$ and every optimal solution $y^{*}$ of $(D)$, we have
$$cx^{*}= y^{*}b.$$
An interesting corollary of Theorem 47.9 is that there is a test to determine whether a Linear Program $(P)$ has an optimal solution.
