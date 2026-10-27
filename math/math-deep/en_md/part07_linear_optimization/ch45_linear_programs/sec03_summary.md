# Summary


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
