# Affine Subsets, Convex Sets, Hyperplanes, Half-Spaces


<!-- PAGE 1577 -->
We give a brief introduction to these topics. As a reward, we provide several criteria for testing whether a system of inequalities
$$Ax \le b, x \ge 0$$
has a solution or not in terms of versions of the Farkas lemma (see Proposition 50.3 and Proposition 47.4). Then we give a complete proof of the strong duality theorem for linear programming (see Theorem 47.7). We also discuss the complementary slackness conditions and show that they can be exploited to design an algorithm for solving a linear program that uses both the primal problem and its dual. This algorithm known as the primal dual algorithm, although not used much nowadays, has been the source of inspiration for a whole class of approximation algorithms also known as primal dual algorithms. We hope that this chapter and the next three will be a motivation for learning more about linear programming, convex optimization, but also convex geometry. The “bible” in convex optimization is Boyd and Vandenberghe $[29]$, and one of the best sources for convex geometry is Ziegler $[201]$. This is a rather advanced text, so the reader may want to begin with Gallier $[74]$.

## 44.2 Affine Subsets, Convex Sets, Affine Hyperplanes,

$$Half-Spaces$$
$$\mathbb{R}^{n}$$
We view as consisting of column vectors $(n\times 1$ matrices). As usual, row vectors represent
$$\mathbb{R}^{n} \mathbb{R}$$
linear forms, that is linear maps $\phi$ : $\to$ , in the sense that the row vector $y$ (a $1 \times  n$ matrix) represents the linear form $\phi$  if $\phi (x) =$ yx for all $x \in \mathbb{R}^{n}$. We denote the space of linear forms (row vectors) by $(\mathbb{R}^{n})^{*}$.
$$\mathbb{R}^{n}$$
Recall that a linear combination of vectors in is an expression
$$\lambda_{1} x_{1} + \cdots  + \lambda_{m} x_{m}$$
$$\mathbb{R}^{n}  \mathbb{R}$$
where $x_{1}, \dots  , x_{m} \in$ and where $\lambda_{1} , \dots  , \lambda_{m}$  are arbitrary scalars in . Given a sequence of vectors $S = (x_{1}, \dots  , x_{m})$ with $x_{i} \in \mathbb{R}^{n}$, the set of all linear combinations of the vectors in $S$ is the smallest (linear) subspace containing $S$ called the linear span of $S$, and denoted span(S).
$$\mathbb{R}^{n}  \mathbb{R}^{n}$$
A linear subspace of is any nonempty subset of closed under linear combinations.
$$\mathbb{R}^{n}$$

> **Definition 44.1.** An affine combination of vectors in is an expression
$$\lambda_{1} x_{1} + \cdots  + \lambda_{m} x_{m}$$
$$\mathbb{R}^{n}  \mathbb{R}$$
where $x_{1}, \dots  , x_{m} \in$ and where $\lambda_{1} , \dots  , \lambda_{m}$  are scalars in  satisfying the condition
$$\lambda_{1}  + \cdots  + \lambda_{m}  = 1.$$
Given a sequence of vectors $S = (x_{1}, \dots  , x_{m})$ with $x_{i} \in \mathbb{R}^{n}$, the set of all affine combinations of the vectors in $S$ is the smallest affine subspace containing $S$ called the affine hull of $S$ and denoted aff(S).

<!-- PAGE 1578 -->
$$(a)(b)$$
$$Figure 44.1: (a) A convex set; (b) A nonconvex set$$
$$\mathbb{R}^{n}  \mathbb{R}^{n}$$

> **Definition 44.2.** An affine subspace $A$ of is any subset of closed under affine combinations. If $A$ is a nonempty affine subspace $of\mathbb{R}^{n}$, then it can be shown that $V_{A} = {a-b$ | a, $b \in A}$
$$\mathbb{R}^{n}$$
is a linear subspace of and that
$$A = a + V_{A} = {a + v | v \in V_{A}}$$
for any $a \in A$; see Gallier $[73]$ (Section 2.5).

> **Definition 44.3.** Given an affine subspace $A$, the linear space $V_{A} = {a$ - $b$ | a, $b \in A}$ is called the direction of $A$. The dimension of the nonempty affine subspace $A$ is the dimension of its direction $V_{A}$.

> **Definition 44.4.** Convex combinations are affine combinations $\lambda_{1} x_{1} +\cdots +\lambda_{m} x_{m}$ satisfying the extra condition that $\lambda_{i}  \ge 0$ for $i = 1, \dots  , m$. A convex set is defined as follows.
$$\mathbb{R}^{n}$$

> **Definition 44.5.** A subset $V$ of is convex if for any two points a, $b \in V$ , we have $c \in V$ for every point $c = (1$ - $\lambda )a + \lambda b$, with $0 \le \lambda  \le 1 (\lambda  \in \mathbb{R})$. Given any two points a, $b$, the notation [a, $b]$ is often used to denote the line segment between a and $b$, that is,
$$\mathbb{R}^{n}$$
$$[a, b] = {c \in | c = (1 -\lambda )a + \lambda b, 0 \le \lambda  \le 1},$$
and thus a set $V$ is convex if [a, $b] \subseteq V$ for any two points a, $b \in V (a = b$ is allowed). The dimension of a convex set $V$ is the dimension of its affine hull aff(A). The empty set is trivially convex, every one-point set ${a}$ is convex, and the entire affine $\mathbb{R}^{n}$ space is convex. It is obvious that the intersection of any family (finite or infinite) of convex sets is convex.

<!-- PAGE 1579 -->

> **Definition 44.6.** Given any (nonempty) subset $S of\mathbb{R}^{n}$, the smallest convex set containing $S$ is denoted by conv(S) and called the convex hull of $S$ (it is the intersection of all convex sets containing $S)$. It is essential not only to have a good understanding of conv(S), but to also have good methods for computing it. We have the following simple but crucial result.

> **Proposition 44.1.** For any family $S = (a_{i})_{i\in I}$ of points in $\mathbb{R}^{n}$, the set $V$ of convex combi-
$$nations \sum_{i}  \in I \lambda_{i} a_{i} (where \sum_{i}  \in I \lambda_{i}  = 1 and \lambda_{i}  \ge 0) is the convex hull conv(S) of S = (a_{i})_{i\in I}.$$
It is natural to wonder whether Proposition 44.1 can be sharpened in two directions:
$(1)$ Is it possible to have a fixed bound on the number of points involved in the convex combinations? $(2)$ Is it necessary to consider convex combinations of all points, or is it possible to consider only a subset with special properties? The answer is yes in both cases. In Case $1$, Carath´eodory’s theorem asserts that it is enough to consider convex combinations of $n + 1$ points. For example, in the plane $\mathbb{R}^{2}$, the convex hull of a set $S$ of points is the union of all triangles (interior points included) with vertices in $S$. In Case $2$, the theorem of Krein and Milman asserts that a convex set that is also compact is the convex hull of its extremal points (given a convex set $S$, a point $a \in S$ is extremal if $S -{a}$ is also convex). We will not prove these theorems here, but we invite the reader to consult Gallier $[74]$ or Berger $[12]$. Convex sets also arise as half-spaces cut out by affine hyperplanes.
$$\mathbb{R}^{n} \mathbb{R}\mathbb{R}^{n}$$

> **Definition 44.7.** An affine form $\phi$ : $\to$  is defined by some linear form $c \in$ ( $)^{*}$ and some scalar $\beta  \in \mathbb{R}$ so that
$$\phi (x) = cx + \beta for all x \in \mathbb{R}^{n}.$$
If $c \neq  0$, the affine form $\phi$  specified by $(c, \beta$ ) defines the affine hyperplane (for short hyperplane) $H(\phi$ ) given by
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
$$H(\phi ) = {x \in | \phi (x) = 0} = {x \in | cx + \beta  = 0},$$
and the two (closed) half-spaces
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
$$H_{+}(\phi ) = {x \in | \phi (x) \ge 0} = {x \in | cx + \beta  \ge 0},$$
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
$$H_{-}(\phi ) = {x \in | \phi (x) \le 0} = {x \in | cx + \beta  \le 0}.$$
When $\beta  = 0$, we call $H$ a linear hyperplane. Both $H_{+}(\phi$ ) and $H_{-}(\phi$ ) are convex and $H = H_{+}(\phi$ ) $\cap H_{-}(\phi$ ).
$$\mathbb{R}^{2} \mathbb{R}$$
For example, $\phi$ : $\to$  with $\phi (x, y) =$ 2x $+ y + 3$ is an affine form defining the line
$$\mathbb{R}^{3} \mathbb{R}$$
given by the equation $y =$ -2x - $3$. Another example of an affine form is $\phi$ : $\to$
