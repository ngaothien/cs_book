# Problems


<!-- PAGE 1601 -->
Every constraint $a_{i}x \ge b_{i}$ is replaced by the constraint $-a_{i}x \le -b_{i}$. Every equality constraint $a_{i}x = b_{i}$ is replaced by the two constraints $a_{i}x \le b_{i}$ and $-a_{i}x \le -b_{i}$. If there are $n$ variables $x_{i}$, we create $n$ new variables $y_{i}$ and $n$ new variables $z_{i}$ and replace every variable $x_{i}$ by $y_{i} -z_{i}$. We also add the 2n constraints $y_{i} \ge 0$ and $z_{i} \ge 0$. If the constraints are given by the inequalities Ax $\le b$, we now have constraints given by
$$\begin{pmatrix} A & -A \end{pmatrix} \begin{pmatrix} y \\ z \end{pmatrix} \le b,y \ge 0, z \ge 0.$$
We replace the objective function cx by cy - cz.
Remark: We also showed that we can replace the inequality constraints Ax $\le b$ by equality constraints Ax $= b$, by adding slack variables constrained to be nonnegative.

## 45.3 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Linear program. $\bullet$  Objective function, constraints. $\bullet$  Feasible solution. $\bullet$  Bounded and unbounded linear programs. $\bullet$  Optimal solution, optimum. $\bullet$  Slack variables, linear program in standard form. $\bullet$  Basic feasible solution. $\bullet$  Basis of a variable. $\bullet$  Basic, nonbasic index, basic, nonbasic variable. $\bullet$  Vertex, face, edge, facet.

## 45.4 Problems

Problem 45.1. Convert the following program to standard form:
$$maximizex_{1} + x_{2}$$
$$subject to$$
$$x_{2} -x_{1} \le 1$$
$$x_{1} + 6x_{2} \le 15$$
$$-4x_{1} + x_{2} \ge 10.$$

<!-- PAGE 1602 -->
Problem 45.2. Convert the following program to standard form:
$$maximize3x_{1} -2x_{2}$$
$$subject to$$
$$2x_{1} -x_{2} \le 4$$
$$x_{1} + 3x_{2} \ge 5$$
$$x_{2} \ge 0.$$
Problem 45.3. The notion of basic feasible solution for linear programs where the constraints are of the form Ax $\le b, x \ge 0$ is defined as follows. A basic feasible solution of a (general) linear program with $n$ variables is a feasible solution for which some $n$ linearly independent constraints hold with equality. Prove that the definition of a basic feasible solution for linear programs in standard form is a special case of the above definition.
Problem 45.4. Consider the linear program
$$maximizex_{1} + x_{2}$$
$$subject to$$
$$x_{1} + x_{2} \le 1.$$
Show that none of the optimal solutions are basic.
$$\mathbb{R}^{n+1}$$
Problem 45.5. The standard n-simplex is the subset $\Delta^{n}$ of given by
$$\mathbb{R}^{n+1}$$
$$\Delta^{n} = {(x_{1}, \dots  , x_{n+1}) \in | x_{1} + \cdots  + x_{n+1} = 1, x_{i} \ge 0, 1 \le i \le n + 1}.$$
$(1)$ Prove that $\Delta^{n}$ is convex and that it is the convex hull of the $n+1$ vectors $e_{1}, \dots  e_{n+1}$, where $e_{i}$ is the ith canonical unit basis vector, $i = 1, \dots  , n + 1$.
$(2)$ Prove that $\Delta^{n}$ is the intersection of $n + 1$ half spaces and determine the hyperplanes defining these half-spaces.
Remark: The volume under the standard simplex $\Delta^{n}$ is $1/(n + 1)$!.
$$\mathbb{R}^{n}$$
Problem 45.6. The $n$-dimensional cross-polytope is the subset $XP_{n}$ of given by
$$\mathbb{R}^{n}$$
$$XP_{n} = {(x_{1}, \dots  , x_{n}) \in | |x_{1}| + \cdots  + |x_{n}| \le 1}.$$
$(1)$ Prove that $XP_{n}$ is convex and that it is the convex hull of the 2n vectors $\pm e_{i}$, where $e_{i}$ is the ith canonical unit basis vector, $i = 1, \dots  , n$.
$(2)$ Prove that $XP_{n}$ is the intersection of $2^{n}$ half spaces and determine the hyperplanes defining these half-spaces.
Remark: The volume of $XP_{n}$ is $2^{n}/n$!.

<!-- PAGE 1603 -->
$$\mathbb{R}^{n}$$
Problem 45.7. The $n$-dimensional hypercube is the subset $C_{n}$ of given by
$$\mathbb{R}^{n}$$
$$C_{n} = {(x_{1}, \dots  , x_{n}) \in | |x_{i}| \le 1, 1 \le i \le n}.$$
$(1)$ Prove that $C_{n}$ is convex and that it is the convex hull of the $2^{n}$ vectors $(\pm 1, \dots  , \pm 1), i = 1, \dots  , n$.
$(2)$ Prove that $C_{n}$ is the intersection of 2n half spaces and determine the hyperplanes defining these half-spaces.
Remark: The volume of $C_{n}$ is $2^{n}$.

<!-- PAGE 1604 -->
