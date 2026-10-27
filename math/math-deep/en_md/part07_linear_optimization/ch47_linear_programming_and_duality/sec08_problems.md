# Problems


<!-- PAGE 1674 -->
importantly $(x_{1}, x_{2}, x_{3}, x_{4}) = (1/3, 0, 1/3, 2)$ is an optimal solution for our original linear program and provides an optimal value of $-10/3$. The primal-dual algorithm for linear programming doesn’t seem to be the favorite method to solve linear programs nowadays. But it is important because its basic principle, to use a restricted (simpler) primal problem involving an objective function with fixed weights, namely $1$, and the dual problem to provide feedback to the primal by improving the objective function of the dual, has led to a whole class of combinatorial algorithms (often approximation algorithms) based on the primal-dual paradigm. The reader will get a taste of this kind of algorithm by consulting Papadimitriou and Steiglitz $[139]$, where it is explained how classical algorithms such as Dijkstra’s algorithm for the shortest path problem, and Ford and Fulkerson’s algorithm for max flow can be derived from the primal-dual paradigm.

## 47.7 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Strictly separating hyperplane. $\bullet$  Farkas–Minkowski proposition. $\bullet$  Farkas lemma, version I, Farkas lemma, version II. $\bullet$  Distance of a point to a subset. $\bullet$  Dual linear program, primal linear program. $\bullet$  Dual variables, primal variables. $\bullet$  Complementary slackness conditions. $\bullet$  Dual simplex algorithm. $\bullet$  Primal-dual algorithm. $\bullet$  Restricted primal linear program.

## 47.8 Problems

$$\mathbb{R}^{d}$$
Problem 47.1. Let $(v_{1}, \dots  , v_{n})$ be a sequence of $n$ vectors in and let $V$ be the $d \times  n$ matrix whose $j$-th column is $v_{j}$. Prove the equivalence of the following two statements:
(a) There is no nontrivial positive linear dependence among the $v_{j}$, which means that there is no nonzero vector, $y = (y_{1}, \dots  , y_{n}) \in \mathbb{R}^{n}$, with $y_{j} \ge 0$ for $j = 1, \dots  , n$, so that
$$y_{1}v_{1} + \cdots  + y_{n}v_{n} = 0$$
or equivalently, $V y = 0$.

<!-- PAGE 1675 -->
$(b)$ There is some vector, $c \in \mathbb{R}^{d}$, so that $c^{\top}V > 0$, which means that $c^{\top}v_{j} > 0$, for $j = 1, \dots  , n$.
Problem 47.2. Check that the dual in maximization form (D'') of the Dual Program (D') (which is the dual of $(P)$ in maximization form),
$$maximize-b^{\top}y^{\top}$$
$$subject to-A^{\top}y^{\top}\le -c^{\top}and y^{\top}\ge 0,$$
where $y \in (\mathbb{R}^{m})^{*}$, gives back the Primal Program $(P)$.
Problem 47.3. In a General Linear Program $(P)$ with $n$ primal variables $x_{1}, \dots  , x_{n}$ and
$$objective function \sum_{j}  n=1 c_{j}x_{j} (to be maximized), the m constraints are of the form$$
$$\sum_{j=1}^{n}  a_{ij}x_{j} \le b_{i},$$
$$\sum_{j=1}^{n}  a_{ij}x_{j} \ge b_{i},$$
$$\sum_{j=1}^{n}  a_{ij}x_{j} = b_{i},$$
for $i = 1, \dots  , m$, and the variables $x_{j}$ satisfy an inequality of the form
$$x_{j} \ge 0,$$
$$x_{j} \le 0,$$
$$x_{j} \in \mathbb{R},$$
for $j = 1, \dots  , n$. If $y_{1}, \dots  , y_{m}$ are the dual variables, show that the dual program of the linear program in standard form equivalent to $(P)$ is equivalent to the linear program whose
$$objective function is \sum_{i}  m=1 y_{i}b_{i} (to be minimized) and whose constraints are determined as$$
follows:
$$$$
$$ \sum_{i=1m}^{m}  a_{ij}y_{i} \ge c_{j}$$
$$$$
$$x_{j} \ge 0$$
$$$$
$$$$
$$$$
$$ifx_{j} \le \mathbb{R} 0,then \sum_{i=1m}  a_{ij}y_{i} \le c_{j},$$
$$x_{j} \in $$
$$$$
$$$$
$$$$
$$ \sum_{i=1}  a_{ij}y_{i} = c_{j}$$
$$$$

<!-- PAGE 1676 -->
and
$$$$
$$ \sum_{j=1}^{n}  a_{ij}x_{j} \le b_{i}$$
$$$$
$$$$
$$y_{i} \ge 0$$
$$$$
$$$$
$$$$
$$if \sum_{j=1}^{n}  a_{ij}x_{j} \ge b_{i},theny_{i} \le 0.$$
$$y_{i} \in \mathbb{R}$$
$$$$
$$$$
$$$$
$$$$
$$$$
$$ \sum_{j=1}^{n}  a_{ij}x_{j} = b_{i}$$
$$$$
Problem 47.4. Apply the procedure of Problem 47.3 to show that the dual of the (general) linear program
$$maximize3x_{1} + 2x_{2} + 5x_{3}$$
$$subject to$$
$$5x_{1} + 3x_{2} + x_{3} = -8$$
$$4x_{1} + 2x_{2} + 8x_{3} \le 23$$
$$6x_{1} + 7x_{2} + 3x_{3} \ge 1$$
$$x_{1} \le 4, x_{3} \ge 0$$
is the (general) linear program:
$$minimize-8y_{1} + 23y_{2} -y_{3} + 4y_{4}$$
$$subject to$$
$$5y_{1} + 4y_{2} -6y_{3} + y_{4} = 3$$
$$3y_{1} + 2y_{2} -7y_{3} = 2$$
$$y_{1} + 8y_{2} -3y_{3} \ge 5$$
$$y_{2}, y_{3}, y_{4} \ge 0.$$
Problem 47.5. $(1)$ Prove that the dual of the (general) linear program
$$maximizecx$$
$$subject toAx = b and x \in \mathbb{R}^{n}$$
is
$$minimizeyb$$
$$subject toyA = c and y \in \mathbb{R}^{m}.$$
$(2)$ Prove that the dual of the (general) linear program
$$maximizecx$$
$$subject toAx \ge b and x \ge 0$$

<!-- PAGE 1677 -->
is
$$minimizeyb$$
$$subject toyA \ge c and y \le 0.$$
Problem 47.6. Use the complementary slackness conditions to confirm that
$$x_{1} = 2, x_{2} = 4, x_{3} = 0, x_{4} = 0, x_{5} = 7, x_{6} = 0$$
is an optimal solution of the following linear program (from Chavatal $[40]$, Chapter $5)$:
$$maximize18x_{1} -7x_{2} + 12x_{3} + 5x_{4} + 8x_{6}$$
$$subject to$$
$$2x_{1} -6x_{2} + 2x_{3} + 7x_{4} + 3x_{5} + 8x_{6} \le 1$$
$$-3x_{1} -x_{2} + 4x_{3} -3x_{4} + x_{5} + 2x_{6} \le -2$$
$$8x_{1} -3x_{2} + 5x_{3} -2x_{4} + 2x_{6} \le 4$$
$$4x_{1} + 8x_{3} + 7x_{4} -x_{5} + 3x_{6} \le 1$$
$$5x_{1} + 2x_{2} -3x_{3} + 6x_{4} -2x_{5} -x_{6} \le 5$$
$$x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{6} \ge 0.$$
Problem 47.7. Check carefully that the dual simplex method is equivalent to the simplex method applied to the dual program in maximization form.

<!-- PAGE 1678 -->
