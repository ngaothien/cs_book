# Summary


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
