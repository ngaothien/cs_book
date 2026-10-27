# Problems


<!-- PAGE 1854 -->

## 50.15 Problems

Problem 50.1. Prove $(3)$ and $(4)$ of Proposition 50.11.
Problem 50.2. Assume that in Theorem 50.17, $V = \mathbb{R}^{n}, J$ is elliptic and the constraints $\phi_{i}$  are of the form
$$\sum_{j=1}^{n}  c_{ij}v_{j} \le d_{i},$$
that is, affine. Prove that the Problem $(P_{\mu})$ has a unique solution which is continuous in $\mu$ .
Problem 50.3. $(1)$ Prove that the set of saddle points of a function $L: \Omega \times  M \to \mathbb{R}$ is of the form $V_{0} \times  M_{0}$, for some $V_{0} \subseteq \Omega$ and some $M_{0} \subseteq M$.
$(2)$ Assume that $\Omega$ and $M$ are convex subsets of some normed vector spaces, assume that for any fixed $v \in \Omega$ the map
$$\mu  \mapsto L(v, \mu )is concave,$$
and for any fixed $\mu  \in M$ the map
$$v \mapsto L(v, \mu )is convex.$$
Prove that $V_{0} \times  M_{0}$ is convex.
$(3)$ Prove that if for every fixed $\mu  \in M$ the map
$$v \mapsto L(v, \mu )is strictly convex,$$
then $V_{0}$ has a most one element.
Problem 50.4. Prove that the conjugate of the function $f$ given by f(X) $=$ log $det(X^{-1})$, where $X$ is an $n \times  n$ symmetric positive definite matrix, is
$$f^{*} (Y ) = \log \det((-Y )^{-1}) -n,$$
where $Y$ is an $n \times  n$ symmetric negative definite matrix.
Problem 50.5. (From Boyd and Vandenberghe $[29]$, Problem 5.12) Given an $m \times  n$ matrix $A$ and any vector $b \in \mathbb{R}^{n}$, consider the problem
$$minimize- \sum_{i=1}^{m}  \log(b_{i} -a_{i}x)$$
$$subject to Ax < b,$$
where $a_{i}$ is the ith row of $A$. This is called the analytic centering problem. It can be shown
$$\mathbb{R}^{n}$$
that the problem has a unique solution iff the open polyhedron ${x \in$ | Ax $< b}$ is nonempty and bounded.

<!-- PAGE 1855 -->
$(1)$ Prove that necessary and sufficient conditions for the problem to have an optimal solution are
$$Ax < b, \sum_{i=1}^{m}  \frac{a_{i}^{\top}}{b_{i} -a_{x}x} = 0.$$
$(2)$ Derive a dual program for the above program. Hint. First introduce new variables $y_{i}$ and equations $y_{i} = b_{i}$ - $a_{i}x$.
Problem 50.6. (From Boyd and Vandenberghe $[29]$, Problem 5.13) $A$ Boolean linear program is the following optimization problem:
$$minimizec^{\top}x$$
$$subject to Ax \le b$$
$$x_{i} \in {0, 1}, i = 1, \dots  , n,$$
$$\mathbb{R}^{n} \mathbb{R}^{m}\mathbb{R}^{n}$$
where $A$ is an $m \times  n$ matrix, $c \in$ and $b \in$ . The fact that the solutions $x \in$ are constrained to have coordinates $x_{i}$ taking the values $0$ or $1$ makes it a hard problem. The above problem can be stated as a program with quadratic constraints:
$$minimizec^{\top}x$$
$$subject to Ax \le b$$
$$x_{i}(1 -x_{i}) = 0, i = 1, \dots  , n.$$
$(1)$ Derive the Lagrangian dual of the above program.
$(2) A$ way to approximate a solution of the Boolean linear program is to consider its linear relaxation where the constraints $x_{i} \in {0, 1}$ are replaced by the linear constraints $0 \le x_{i} \le 1$:
$$minimizec^{\top}x$$
$$subject to Ax \le b$$
$$0 \le x_{i} \le 1, i = 1, \dots  , n.$$
Find the dual linear program of the above linear program. Show that the maxima of the dual programs in $(1)$ and $(2)$ are the same.

<!-- PAGE 1856 -->
