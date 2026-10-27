# Quadratic Optimization: The Positive Definite Case


<!-- PAGE 1543 -->
Chapter $42$ Quadratic Optimization Problems In this chapter we consider two classes of quadratic optimization problems that appear frequently in engineering and in computer science (especially in computer vision): $1$. Minimizing
$$Q(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b$$
over all $x \in \mathbb{R}^{n}$, or subject to linear or affine constraints. $2$. Minimizing
$$Q(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b$$
over the unit sphere. In both cases, $A$ is a symmetric matrix. We also seek necessary and sufficient conditions for $Q$ to have a global minimum.

## 42.1 Quadratic Optimization: The Positive

$$Definite Case$$
Many problems in physics and engineering can be stated as the minimization of some energy function, with or without constraints. Indeed, it is a fundamental principle of mechanics that nature acts so as to minimize energy. Furthermore, if a physical system is in a stable state of equilibrium, then the energy in that state should be minimal. For example, a small ball placed on top of a sphere is in an unstable equilibrium position. A small motion causes the ball to roll down. On the other hand, a ball placed inside and at the bottom of a sphere is in a stable equilibrium position because the potential energy is minimal. The simplest kind of energy function is a quadratic function. Such functions can be conveniently defined in the form
$$Q(x) = x^{\top}Ax -x^{\top}b,$$
$$1543$$

<!-- PAGE 1544 -->
where $A$ is a symmetric $n \times  n$ matrix and $x, b$, are vectors in $\mathbb{R}^{n}$, viewed as column vectors. Actually, for reasons that will be clear shortly, it is preferable to put a $factor_{2}^{1}$  in front of the quadratic term, so that
$$Q(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b.$$
The question is, under what conditions (on $A)$ does Q(x) have a global minimum, preferably unique? We give a complete answer to the above question in two stages: $1$. In this section we show that if $A$ is symmetric positive definite, then Q(x) has a unique global minimum precisely when
$$Ax = b.$$
$2$. In Section 42.2 we give necessary and sufficient conditions in the general case, in terms of the pseudo-inverse of $A$. We begin with the matrix version of Definition 22.2.

> **Definition 42.1.** A symmetric positive definite matrix is a matrix whose eigenvalues are strictly positive, and a symmetric positive semidefinite matrix is a matrix whose eigenvalues are nonnegative. Equivalent criteria are given in the following proposition.

> **Proposition 42.1.** Given any Euclidean space $E$ of dimension $n$, the following properties hold:
$(1)$ Every self-adjoint linear map $f$ : $E \to E$ is positive definite iff
$$\langle f(x), x\rangle > 0$$
for all $x \in E$ with $x \neq  0$.
$(2)$ Every self-adjoint linear map $f$ : $E \to E$ is positive semidefinite iff
$$\langle f(x), x\rangle \ge 0$$
for all $x \in E$.

*Proof.* $(1)$ First assume that $f$ is positive definite. Recall that every self-adjoint linear map has an orthonormal basis $(e_{1}, \dots  , e_{n})$ of eigenvectors, and let $\lambda_{1} , \dots  , \lambda_{n}$  be the corresponding eigenvalues. With respect to this basis, for every $x = x_{1}e_{1} + \cdots  + x_{n}e_{n} \neq  0$, we have
$$\langle f(x), x\rangle = \bigoplus  f \begin{pmatrix} x_{i}e_{i} \end{pmatrix} \sum_{i=1}^{n}  , \sum_{i=1}^{n}  x_{i}e_{i}E= \bigoplus  \sum_{i=1}^{n}  \lambda_{i} x_{i}e_{i}, \sum_{i=1}^{n}  x_{i}e_{i}E= \sum_{i=1}^{n}  \lambda_{i} x_{i}^{2} ,$$

<!-- PAGE 1545 -->
which is strictly positive, since $\lambda_{i}  > 0$ for $i = 1, \dots  , n$, and $x_{i}^{2} > 0$ for some $i$, since $x \neq  0$. Conversely, assume that
$$\langle f(x), x\rangle > 0$$
for all $x \neq  0$. Then for $x = e_{i}$, we get
$$\langle f(e_{i}), e_{i}\rangle = \langle \lambda_{i} e_{i}, e_{i}\rangle = \lambda_{i} ,$$
and thus $\lambda_{i}  > 0$ for all $i = 1, \dots  , n$.
$(2)$ As in $(1)$, we have
$$\langle f(x), x\rangle = \sum_{i=1}^{n}  \lambda_{i} x_{i}^{2} ,$$
and since $\lambda_{i}  \ge 0$ for $i = 1, \dots  , n$ because $f$ is positive semidefinite, we have $\langle$ f(x), $x\rangle \ge 0$, as claimed. The converse is as in $(1)$ except that we get only $\lambda_{i}  \ge 0$ since $\langle f(e_{i}), e_{i}\rangle \ge 0$. Some special notation is customary (especially in the field of convex optimization) to express that a symmetric matrix is positive definite or positive semidefinite.

> **Definition 42.2.** Given any $n \times  n$ symmetric matrix $A$ we write $A$ ⪰ $0$ if $A$ is positive semidefinite and we write $A$ ≻ $0$ if $A$ is positive definite.
Remark: It should be noted that we can define the relation
$$A ⪰B$$
between any two $n \times  n$ matrices (symmetric or not) iff $A -B$ is symmetric positive semidefinite. It is easy to check that this relation is actually a partial order on matrices, called the positive semidefinite cone ordering; for details, see Boyd and Vandenberghe $[29]$, Section 2.4. If $A$ is symmetric positive definite, it is easily checked that $A^{-1}$ is also symmetric positive definite. Also, if $C$ is a symmetric positive definite $m\times m$ matrix and $A$ is an $m\times n$ matrix of rank $n$ (and so $m \ge n$ and the map $x \mapsto$ Ax is injective), then $A^{\top}CA$ is symmetric positive definite. We can now prove that
$$Q(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b$$
has a global minimum when $A$ is symmetric positive definite.

> **Proposition 42.2.** Given a quadratic function
$$Q(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b,$$
if $A$ is symmetric positive definite, then Q(x) has a unique global minimum for the solution $x_{0} = A^{-1}b$ of the linear system Ax $= b$. The minimum value of Q(x) is
$$Q(A^{-1}b) = - \frac{1}{2} b^{\top}A^{-1}b.$$

<!-- PAGE 1546 -->

*Proof.* Since $A$ is positive definite, it is invertible since its eigenvalues are all strictly positive. Let $x_{0} = A^{-1}b$, and compute Q(y) - $Q(x_{0})$ for any $y \in \mathbb{R}^{n}$. Since $Ax_{0} = b$, we get
$$Q(y) -Q(x_{0}) = \frac{1}{2} y^{\top}Ay -y^{\top}b - \frac{1}{2} x_{0}^{\top} Ax_{0} + x_{0}^{\top} b$$
$$= \frac{1}{2} y^{\top}Ay -y^{\top}Ax_{0} + \frac{1}{2} x_{0}^{\top} Ax_{0}$$
$$= \frac{1}{2} (y -x_{0})^{\top}A(y -x_{0}).$$
Since $A$ is positive definite, the last expression is nonnegative, and thus
$$Q(y) \ge Q(x_{0})$$
for all $y \in \mathbb{R}^{n}$, which proves that $x_{0} = A^{-1}b$ is a global minimum of Q(x). A simple computation yields
$$Q(A^{-1}b) = - \frac{1}{2} b^{\top}A^{-1}b.$$
Remarks:
$(1)$ The quadratic function Q(x) is also given by
$$Q(x) = \frac{1}{2} x^{\top}Ax -b^{\top}x,$$
but the definition using $x^{\top}b$ is more convenient for the proof of Proposition 42.2.
$(2)$ If Q(x) contains a constant term $c \in \mathbb{R}$, so that
$$Q(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b + c,$$
the proof of Proposition 42.2 still shows that Q(x) has a unique global minimum for $x = A^{-1}b$, but the minimal value is
$$Q(A^{-1}b) = - \frac{1}{2} b^{\top}A^{-1}b + c.$$
Thus when the energy function Q(x) of a system is given by a quadratic function
$$Q(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b,$$
where $A$ is symmetric positive definite, finding the global minimum of Q(x) is equivalent to solving the linear system Ax $= b$. Sometimes, it is useful to recast a linear problem Ax $= b$ as a variational problem (finding the minimum of some energy function). However, very often, a minimization problem comes with extra constraints that must be satisfied for all admissible solutions.

<!-- PAGE 1547 -->

> **Example 42.1.** For instance, we may want to minimize the quadratic function
$$Q(x_{1}, x_{2}) = \frac{1}{2}$$
$$\begin{pmatrix} x_{1}^{2}+ x_{2}^{2} \end{pmatrix}$$
subject to the constraint
$$2x_{1} -x_{2} = 5.$$
The solution for which $Q(x_{1}, x_{2})$ is minimum is no longer $(x_{1}, x_{2}) = (0, 0)$, but instead, $(x_{1}, x_{2}) = (2, -1)$, as will be shown later.
$$\mathbb{R}^{3}$$
Geometrically, the graph of the function defined by $z = Q(x_{1}, x_{2})$ in is a paraboloid of revolution $P$ with axis of revolution Oz. The constraint
$$2x_{1} -x_{2} = 5$$
corresponds to the vertical plane $H$ parallel to the z-axis and containing the line of equation $2x_{1}$ - $x_{2} = 5$ in the xy-plane. Thus, as illustrated by Figure 42.1, the constrained minimum of $Q$ is located on the parabola that is the intersection of the paraboloid $P$ with the plane $H$. A nice way to solve constrained minimization problems of the above kind is to use the method of Lagrange multipliers discussed in Section 40.1. But first let us define precisely what kind of minimization problems we intend to solve.

> **Definition 42.3.** The quadratic constrained minimization problem consists in minimizing a quadratic function
$$Q(x) = \frac{1}{2} x^{\top}A^{-1}x -b^{\top}x$$
subject to the linear constraints
$$B^{\top}x = f,$$
where $A^{-1}$ is an $m \times  m$ symmetric positive definite matrix, $B$ is an $m \times  n$ matrix of rank $n$
$$\mathbb{R}^{m} \mathbb{R}^{n}$$
(so that $m \ge n)$, and where $b, x \in$ (viewed as column vectors), and $f \in$ (viewed as a column vector). The reason for using $A^{-1}$ instead of $A$ is that the constrained minimization problem has an interpretation as a set of equilibrium equations in which the matrix that arises naturally is $A$ (see Strang $[175])$. Since $A$ and $A^{-1}$ are both symmetric positive definite, this doesn’t make any difference, but it seems preferable to stick to Strang’s notation. In Example 42.1 we have $m = 2, n = 1$,
$$A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_{2},b = \begin{pmatrix} 0 \\ 0 \end{pmatrix} ,B = \begin{pmatrix} 2 \\ -1 \end{pmatrix} ,f = 5.$$
As explained in Section 40.1, the method of Lagrange multipliers consists in incorporating the $n$ constraints $B^{\top}x = f$ into the quadratic function Q(x), by introducing extra variables

<!-- PAGE 1548 -->
$$Figure 42.1: Two views of the constrained optimization problem Q(x_{1}, x_{2}) =_{2}^{1} \begin{pmatrix} x_{1}^{2}+ x_{2}^{2} \\ vertexof \end{pmatrix}$$
subject to the constraint $2x_{1}$ - $x_{2} = 5$. The minimum $(x_{1}, x_{2}) = (2, -1)$ is the the the parabolic curve formed the intersection of the magenta planar constraint with the bowl shaped surface. $\lambda  = (\lambda_{1} , \dots  , \lambda_{n}$ ) called Lagrange multipliers, one for each constraint. We form the Lagrangian
$$L(x, \lambda ) = Q(x) + \lambda^{\top} (B^{\top}x -f) = \frac{1}{2} x^{\top}A^{-1}x -(b -B\lambda )^{\top}x -\lambda^{\top} f.$$
We know from Theorem 40.2 that a necessary condition for our constrained optimization problem to have a solution is that $\nabla$ L(x, $\lambda$ ) $= 0$. Since
$$\frac{\partial L}{\partial x} (x, \lambda ) = A^{-1}x -(b -B\lambda )$$
$$\frac{\partial L}{\partial \lambda} (x, \lambda ) = B^{\top}x -f,$$
we obtain the system of linear equations
$$A^{-1}x + B\lambda  = b,$$
$$B^{\top}x = f,$$
which can be written in matrix form as
$$\begin{pmatrix} A^{-1} & B \\ B^{\top} & 0 \end{pmatrix} \begin{pmatrix} x \\ \lambda \end{pmatrix} = \begin{pmatrix} b \\ f \end{pmatrix} .$$

<!-- PAGE 1549 -->
We shall prove in Proposition 42.3 below that our constrained minimization problem has a unique solution actually given by the above system. Note that the matrix of this system is symmetric. We solve it as follows. Eliminating $x$ from the first equation
$$A^{-1}x + B\lambda  = b,$$
we get
$$x = A(b -B\lambda ),$$
and substituting into the second equation, we get
$$B^{\top}A(b -B\lambda ) = f,$$
that is,
$$B^{\top}AB\lambda  = B^{\top}Ab -f.$$
However, by a previous remark, since $A$ is symmetric positive definite and the columns of $B$ are linearly independent, $B^{\top}AB$ is symmetric positive definite, and thus invertible. Thus we obtain the solution
$$\lambda  = (B^{\top}AB)^{-1}(B^{\top}Ab -f),x = A(b -B\lambda ).$$
Note that this way of solving the system requires solving for the Lagrange multipliers first. Letting $e = b$ - $B\lambda$ , we also note that the system
$$\begin{pmatrix} A^{-1} & B \\ B^{\top} & 0 \end{pmatrix} \begin{pmatrix} x \\ \lambda \end{pmatrix} = \begin{pmatrix} b \\ f \end{pmatrix}$$
is equivalent to the system
$$e = b -B\lambda ,$$
$$x = Ae,$$
$$B^{\top}x = f.$$
The latter system is called the equilibrium equations by Strang $[175]$. Indeed, Strang shows that the equilibrium equations of many physical systems can be put in the above form. This includes spring-mass systems, electrical networks and trusses, which are structures built from elastic bars. In each case, $x, e, b, A, \lambda , f$, and $K = B^{\top}AB$ have a physical interpretation. The matrix $K = B^{\top}AB$ is usually called the stiffness matrix. Again, the reader is referred to Strang $[175]$. In order to prove that our constrained minimization problem has a unique solution, we proceed to prove that the constrained minimization of Q(x) subject to $B^{\top}x = f$ is equivalent to the unconstrained maximization of another function $-G(\lambda$ ). We get $G(\lambda$ ) by minimizing the Lagrangian L(x, $\lambda$ ) treated as a function of $x$ alone. The function $-G(\lambda$ ) is the dual

<!-- PAGE 1550 -->
function of the Lagrangian L(x, $\lambda$ ). Here we are encountering a special case of the notion of dual function defined in Section 50.7. Since $A^{-1}$ is symmetric positive definite and
$$L(x, \lambda ) = \frac{1}{2} x^{\top}A^{-1}x -(b -B\lambda )^{\top}x -\lambda^{\top} f,$$
by Proposition 42.2 the global minimum (with respect to $x)$ of L(x, $\lambda$ ) is obtained for the solution $x$ of
$$A^{-1}x = b -B\lambda ,$$
that is, when
$$x = A(b -B\lambda ),$$
and the minimum of L(x, $\lambda$ ) is
$$minx L(x, \lambda ) = - \frac{1}{2} (B\lambda  -b)^{\top}A(B\lambda  -b) -\lambda^{\top} f.$$
Letting
$$G(\lambda ) = \frac{1}{2} (B\lambda  -b)^{\top}A(B\lambda  -b) + \lambda^{\top} f,$$
we will show in Proposition 42.3 that the solution of the constrained minimization of Q(x) subject to $B^{\top}x = f$ is equivalent to the unconstrained maximization of $-G(\lambda$ ). This is a special case of the duality discussed in Section 50.7. Of course, since we minimized L(x, $\lambda$ ) with respect to $x$, we have
$$L(x, \lambda ) \ge -G(\lambda )$$
for all $x$ and all $\lambda$ . However, when the constraint $B^{\top}x = f$ holds, L(x, $\lambda$ ) $=$ Q(x), and thus for any admissible $x$, which means that $B^{\top}x = f$, we have
$$\min Q(x) \ge \max-G(\lambda ).$$
$$x\lambda$$
In order to prove that the unique minimum of the constrained problem Q(x) subject to $B^{\top}x = f$ is the unique maximum of $-G(\lambda$ ), we compute Q(x) $+ G(\lambda$ ).

> **Proposition 42.3.** The quadratic constrained minimization problem of Definition 42.3 has a unique solution $(x, \lambda$ ) given by the system
$$\begin{pmatrix} A^{-1} & B \\ B^{\top} & 0 \end{pmatrix} \begin{pmatrix} x \\ \lambda \end{pmatrix} = \begin{pmatrix} b \\ f \end{pmatrix} .$$
Furthermore, the component $\lambda$  of the above solution is the unique value for which $-G(\lambda$ ) is maximum.

<!-- PAGE 1551 -->

*Proof.* As we suggested earlier, let us compute Q(x) $+ G(\lambda$ ), assuming that the constraint $B^{\top}x = f$ holds. Eliminating $f$, since $b^{\top}x = x^{\top}b$ and $\lambda^{\top} B^{\top}x = x^{\top}B\lambda$ , we get
$$Q(x) + G(\lambda ) = \frac{1}{2} x^{\top}A^{-1}x -b^{\top}x + \frac{1}{2} (B\lambda  -b)^{\top}A(B\lambda  -b) + \lambda^{\top} f$$
$$= \frac{1}{2} (A^{-1}x + B\lambda  -b)^{\top}A(A^{-1}x + B\lambda  -b).$$
Since $A$ is positive definite, the last expression is nonnegative. In fact, it is null iff
$$A^{-1}x + B\lambda  -b = 0,$$
that is,
$$A^{-1}x + B\lambda  = b.$$
But then the unique constrained minimum of Q(x) subject to $B^{\top}x = f$ is equal to the unique maximum of $-G(\lambda$ ) exactly when $B^{\top}x = f$ and $A^{-1}x + B\lambda  = b$, which proves the proposition. We can confirm that the maximum of $-G(\lambda$ ), or equivalently the minimum of
$$G(\lambda ) = \frac{1}{2} (B\lambda  -b)^{\top}A(B\lambda  -b) + \lambda^{\top} f,$$
corresponds to value of $\lambda$  obtained by solving the system
$$\begin{pmatrix} A^{-1} & B \\ B^{\top} & 0 \end{pmatrix} \begin{pmatrix} x \\ \lambda \end{pmatrix} = \begin{pmatrix} b \\ f \end{pmatrix} .$$
Indeed, since
$$G(\lambda ) = \frac{1}{2} \lambda^{\top} B^{\top}AB\lambda  -\lambda^{\top} B^{\top}Ab + \lambda^{\top} f + \frac{1}{2} b^{\top}b,$$
and $B^{\top}AB$ is symmetric positive definite, by Proposition 42.2, the global minimum of $G(\lambda$ ) is obtained when
$$B^{\top}AB\lambda  -B^{\top}Ab + f = 0,$$
that is, $\lambda  = (B^{\top}AB)^{-1}(B^{\top}Ab$ - $f)$, as we found earlier.
Remarks:
$(1)$ There is a form of duality going on in this situation. The constrained minimization of Q(x) subject to $B^{\top}x = f$ is called the primal problem, and the unconstrained maximization of $-G(\lambda$ ) is called the dual problem. Duality is the fact stated slightly loosely as
$$\min Q(x) = \max-G(\lambda ).$$
$$x\lambda$$
A general treatment of duality in constrained minimization problems is given in Section 50.7.

<!-- PAGE 1552 -->
Recalling that $e = b$ - $B\lambda$ , since
$$G(\lambda ) = \frac{1}{2} (B\lambda  -b)^{\top}A(B\lambda  -b) + \lambda^{\top} f,$$
we can also write
$$G(\lambda ) = \frac{1}{2} e^{\top}Ae + \lambda^{\top} f.$$
This expression often represents the total potential energy of a system. Again, the optimal solution is the one that minimizes the potential energy (and thus maximizes $-G(\lambda$ )).
$(2)$ It is immediately verified that the equations of Proposition 42.3 are equivalent to the equations stating that the partial derivatives of the Lagrangian L(x, $\lambda$ ) are null:
$$\frac{\partial L}{\partial x_{i}} = 0,i = 1, \dots  , m,$$
$$\frac{\partial L}{\partial \lambda_{j}} = 0,j = 1, \dots  , n.$$
Thus, the constrained minimum of Q(x) subject to $B^{\top}x = f$ is an extremum of the Lagrangian L(x, $\lambda$ ). As we showed in Proposition 42.3, this extremum corresponds to simultaneously minimizing L(x, $\lambda$ ) with respect to $x$ and maximizing L(x, $\lambda$ ) with respect to $\lambda$ . Geometrically, such a point is a saddle point for L(x, $\lambda$ ). Saddle points are discussed in Section 50.7.
$(3)$ The Lagrange multipliers sometimes have a natural physical meaning. For example, in the spring-mass system they correspond to node displacements. In some general sense, Lagrange multipliers are correction terms needed to satisfy equilibrium equations and the price paid for the constraints. For more details, see Strang $[175]$. Going back to the constrained minimization of $Q(x_{1}, x_{2}) =_{2}^{1} (x_{1}^{2} + x_{2}^{2})$ subject to
$$2x_{1} -x_{2} = 5,$$
the Lagrangian is
$$L(x_{1}, x_{2}, \lambda ) = \frac{1}{2} \begin{pmatrix} x_{1}^{2}+ x_{2}^{2} \\ Lagrangian \end{pmatrix} + \lambda (2x_{1} -x_{2} -5),$$
and the equations stating that the  has a saddle point are
$$x_{1} + 2\lambda  = 0,$$
$$x_{2} -\lambda  = 0,$$
$$2x_{1} -x_{2} -5 = 0.$$
We obtain the solution $(x_{1}, x_{2}, \lambda$ ) $= (2, -1, -1)$.
