# Problems


<!-- PAGE 449 -->
$\bullet$  The matrix of the transpose map $f^{\top}$ is equal to the transpose of the matrix of the map $f$ (Proposition 11.14). $\bullet$  For any $m \times  n$ matrix $A$,
$$rk(A) = rk(A^{\top}).$$
$\bullet$  Characterization of the rank of a matrix in terms of a maximal invertible submatrix (Proposition 11.16). $\bullet$  The four fundamental subspaces:
$$\mathrm{Im} f, \mathrm{Im} f^{\top} , \mathrm{Ker} f, \mathrm{Ker} f^{\top} .$$
$\bullet$  The column space, the nullspace, the row space, and the left nullspace (of a matrix). $\bullet$  Criterion for the solvability of an equation of the form Ax $= b$ in terms of the left nullspace.

## 11.10 Problems

Problem 11.1. Prove the following properties of transposition:
$$(f + g)^{\top}= f^{\top} + g^{\top}$$
$$(g \circ f)^{\top}= f^{\top} \circ g^{\top}$$
$$id_{E}^{\top} = id_{E*}.$$
Problem 11.2. Let $(u_{1}, \dots  , u_{n-1})$ be $n$ - $1$ linearly independent vectors $u_{i} \in \mathbb{C}^{n}$. Prove that the hyperlane $H$ spanned by $(u_{1}, \dots  , u_{n-1})$ is the nullspace of the linear form
$$x \mapsto \det(u_{1}, \dots  , u_{n-1}, x),x \in \mathbb{C}^{n}.$$
Prove that if $A$ is the $n \times  n$ matrix whose columns are $(u_{1}, \dots  , u_{n-1}, x)$, and if $c_{i} = (-1)^{i+n} det(A_{in})$ is the cofactor of $a_{in} = x_{i}$ for $i = 1, \dots  , n$, then $H$ is defined by the equation
$$c_{1}x_{1} + \cdots  + c_{n}x_{n} = 0.$$
$$\mathbb{R}^{n} \mathbb{R}^{n} \mathbb{R}$$
Problem 11.3. $(1)$ Let $\phi$ : $\times \to$  be the map defined by
$$\phi ((x_{1}, \dots  , x_{n}), (y_{1}, \dots  , y_{n})) = x_{1}y_{1} + \cdots  + x_{n}y_{n}.$$
Prove that $\phi$  is a bilinear nondegenerate pairing. Deduce that $(\mathbb{R}^{n})^{*}$ is isomorphic to $\mathbb{R}^{n}$. Prove that $\phi (x, x) = 0$ iff $x = 0$.

<!-- PAGE 450 -->
$$\mathbb{R}^{4} \mathbb{R}^{4} \mathbb{R}$$
$(2)$ Let $\phi_{L}$  : $\times \to$  be the map defined by
$$\phi_{L} ((x_{1}, x_{2}, x_{3}, x_{4}), (y_{1}, y_{2}, y_{3}, , y_{4})) = x_{1}y_{1} -x_{2}y_{2} -x_{3}y_{3} -x_{4}y_{4}.$$
Prove that $\phi$  is a bilinear nondegenerate pairing.
$$\mathbb{R}^{4}$$
Show that there exist nonzero vectors $x \in$ such that $\phi_{L} (x, x) = 0$.
$$\mathbb{R}^{4}$$
Remark: The vector space equipped with the above bilinear form called the Lorentz form is called Minkowski space.
Problem 11.4. Given any two subspaces $V_{1}, V_{2}$ of a finite-dimensional vector space $E$, prove that
$$(V_{1} + V_{2})^{0}= V_{1}^{0} \cap V_{2}^{0}$$
$$(V_{1} \cap V_{2})^{0}= V_{1}^{0} + V_{2}^{0} .$$
Beware that in the second equation, $V_{1}$ and $V_{2}$ are subspaces of $E$, not $E^{*}$.
$$and ($$
Hint. To prove the second equation, prove the inclusions $V_{1}^{0} +V_{2}^{0} \subseteq (V_{1}\cap V_{2})^{0} V_{1}\cap V_{2})^{0} \subseteq V_{1}^{0}  + V_{2}^{0}$  . Proving the second inclusion is a little tricky. First, prove that we can pick a subspace $W_{1}$ of $V_{1}$ and a subspace $W_{2}$ of $V_{2}$ such that $1. V_{1}$ is the direct sum $V_{1} = (V_{1} \cap V_{2}) \oplus W_{1}. 2. V_{2}$ is the direct sum $V_{2} = (V_{1} \cap V_{2}) \oplus W_{2}. 3. V_{1} + V_{2}$ is the direct sum $V_{1} + V_{2} = (V_{1} \cap V_{2}) \oplus W_{1} \oplus W_{2}$.
Problem 11.5. $(1)$ Let $A$ be any $n \times  n$ matrix such that the sum of the entries of every row of $A$ is the same (say $c_{1})$, and the sum of entries of every column of $A$ is the same (say $c_{2})$. Prove that $c_{1} = c_{2}$.
$(2)$ Prove that for any $n \ge 2$, the 2n - $2$ equations asserting that the sum of the entries of every row of $A$ is the same, and the sum of entries of every column of $A$ is the same are lineary independent. For example, when $n = 4$, we have the following $6$ equations
$$a_{11} + a_{12} + a_{13} + a_{14} -a_{21} -a_{22} -a_{23} -a_{24} = 0$$
$$a_{21} + a_{22} + a_{23} + a_{24} -a_{31} -a_{32} -a_{33} -a_{34} = 0$$
$$a_{31} + a_{32} + a_{33} + a_{34} -a_{41} -a_{42} -a_{43} -a_{44} = 0$$
$$a_{11} + a_{21} + a_{31} + a_{41} -a_{12} -a_{22} -a_{32} -a_{42} = 0$$
$$a_{12} + a_{22} + a_{32} + a_{42} -a_{13} -a_{23} -a_{33} -a_{43} = 0$$
$$a_{13} + a_{23} + a_{33} + a_{43} -a_{14} -a_{24} -a_{34} -a_{44} = 0.$$
Hint. Group the equations as above; that is, first list the $n$ - $1$ equations relating the rows, and then list the $n$ - $1$ equations relating the columns. Prove that the first $n$ - $1$ equations

<!-- PAGE 451 -->
are linearly independent, and that the last $n$ - $1$ equations are also linearly independent. Then, find a relationship between the two groups of equations that will allow you to prove that they span subspace $V^{r}$ and $V^{c}$ such that $V^{r} \cap V^{c} = (0)$.
$(3)$ Now consider magic squares. Such matrices satisfy the two conditions about the sum of the entries in each row and in each column to be the same number, and also the additional two constraints that the main descending and the main ascending diagonals add up to this common number. Traditionally, it is also required that the entries in a magic square are positive integers, but we will consider generalized magic square with arbitrary real entries. For example, in the case $n = 4$, we have the following system of $8$ equations:
$$a_{11} + a_{12} + a_{13} + a_{14} -a_{21} -a_{22} -a_{23} -a_{24} = 0$$
$$a_{21} + a_{22} + a_{23} + a_{24} -a_{31} -a_{32} -a_{33} -a_{34} = 0$$
$$a_{31} + a_{32} + a_{33} + a_{34} -a_{41} -a_{42} -a_{43} -a_{44} = 0$$
$$a_{11} + a_{21} + a_{31} + a_{41} -a_{12} -a_{22} -a_{32} -a_{42} = 0$$
$$a_{12} + a_{22} + a_{32} + a_{42} -a_{13} -a_{23} -a_{33} -a_{43} = 0$$
$$a_{13} + a_{23} + a_{33} + a_{43} -a_{14} -a_{24} -a_{34} -a_{44} = 0$$
$$a_{22} + a_{33} + a_{44} -a_{12} -a_{13} -a_{14} = 0$$
$$a_{41} + a_{32} + a_{23} -a_{11} -a_{12} -a_{13} = 0.$$
In general, the equation involving the descending diagonal is
$$a_{22} + a_{33} + \cdots  + a_{nn} -a_{12} -a_{13} -\cdots  -a_{1n} = 0(r)$$
and the equation involving the ascending diagonal is
$$a_{n1} + a_{n-12} + \cdots  + a_{2n-1} -a_{11} -a_{12} -\cdots  -a_{1n-1} = 0.(c)$$
Prove that if $n \ge 3$, then the 2n equations asserting that a matrix is a generalized magic square are linearly independent. Hint. Equations are really linear forms, so find some matrix annihilated by all equations except equation $r$, and some matrix annihilated by all equations except equation $c$.
Problem 11.6. Let $U_{1}, \dots  , U_{p}$ be some subspaces of a vector space $E$, and assume that they form a direct sum $U = U_{1} \oplus \cdots  \oplus U_{p}$. Let $j_{i}$ : $U_{i} \to U_{1} \oplus \cdots  \oplus U_{p}$ be the canonical injections, and let $\pi_{i}$  : $U_{1}^{*}  \times  \cdots  \times  U_{p}^{*} \to U_{i}^{*}$ be the canonical projections. Prove that there is an isomorphism $f$ from $(U_{1} \oplus \cdots  \oplus U_{p})^{*}$ to $U_{1}^{*}  \times  \cdots  \times  U_{p}^{*}$ such that
$$\pi_{i}  \circ f = j_{i}^{\top} ,1 \le i \le p.$$
Problem 11.7. Let $U$ and $V$ be two subspaces of a vector space $E$ such that $E = U \oplus V$ . Prove that
$$E^{*}= U^{0}\oplus V^{0}.$$

<!-- PAGE 452 -->
