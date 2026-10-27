# Equality Constrained Minimization


<!-- PAGE 1789 -->
which implies that
$$\begin{pmatrix} s_{1}x_{1} & \cdots & s_{n}x_{n} \\ conditions \end{pmatrix} = \mu 1_{n}^{\top} ,$$
and we obtain the following necessary  for $f_{\mu}$ to have a maximum:
$$Ax = b$$
$$A^{\top}y -s = c$$
$$\begin{pmatrix} s_{1}x_{1} & \cdots & s_{n}x_{n} \end{pmatrix} = \mu 1_{n}^{\top}$$
$$s, x > 0.$$
It is not hard to show that if the primal linear program with objective function $c^{\top}x$ and equational constraints Ax $= b$ and the dual program with objective function $b^{\top}y$ and inequality constraints $A^{\top}y \ge c$ have interior feasible points $x$ and $y$, which means that $x > 0$ and $s > 0$ (where $s = A^{\top}y$ - $c)$, then the above system of equations has a unique solution such that $x$ is the unique maximizer of $f_{\mu}$ on $U$; see Matousek and Gardner $[127]$ (Section 7.2, Lemma 7.2.1). A particularly important application of Proposition 50.9 is the situation where $\Omega =\mathbb{R}^{n}$.

## 50.4 Equality Constrained Minimization

In this section we consider the following Program $(P)$:
$$minimizeJ(v)$$
$$subject to Av = b, v \in \mathbb{R}^{n},$$
where $J$ is a convex differentiable function and $A$ is an $m \times  n$ matrix of rank $m < n$ (the number of equality constraints is less than the number of variables, and these constraints are independent), and $b \in \mathbb{R}^{m}$.
$$\mathbb{R}^{n}\mathbb{R}^{n}$$
According to Proposition 50.9 (with $\Omega =$ ), Program $(P)$ has a minimum at $x \in$ if
$$\mathbb{R}^{m}$$
and only if there exist some Lagrange multipliers $\lambda  \in$ such that the following equations hold:
$$Ax = b(pfeasibilty)$$
$$\nabla J_{x} + A^{\top}\lambda  = 0.(dfeasibility)$$
The set of linear equations Ax $= b$ is called the primal feasibility equations and the set of (generally nonlinear) equations $\nabla J_{x} + A^{\top}\lambda  = 0$ is called the set of dual feasibility equations. In general, it is impossible to solve these equations analytically, so we have to use numerical approximation procedures, most of which are variants of Newton’s method. In special cases, for example if $J$ is a quadratic functional, the dual feasibility equations are also linear, a case that we consider in more detail.

<!-- PAGE 1790 -->
Suppose $J$ is a convex quadratic functional of the form
$$J(x) = \frac{1}{2} x^{\top}Px + q^{\top}x + r,$$
$$\mathbb{R}^{n} \mathbb{R}$$
where $P$ is a $n \times  n$ symmetric positive semidefinite matrix, $q \in$ and $r \in$ . In this case
$$\nabla J_{x} = Px + q,$$
so the feasibility equations become
$$Ax = b$$
$$Px + q + A^{\top}\lambda  = 0,$$
which in matrix form become
$$\begin{pmatrix} P & A^{\top} \\ A & 0 \end{pmatrix} \begin{pmatrix} x \\ \lambda \end{pmatrix} = \begin{pmatrix} -q \\ b \end{pmatrix} .(KKT-eq)$$
The matrix of the linear system is usually called the KKT-matrix. Observe that the KKT matrix was already encountered in Proposition 42.3 with a different notation; there we had $P = A^{-1}, A = B^{\top}, q = b$, and $b = f$. If the KKT matrix is invertible, then its unique solution $(x^{*}, \lambda^{*}$ ) yields a unique minimum $x^{*}$ of Problem $(P)$. If the KKT matrix is singular but the System (KKT-eq) is solvable, then any solution $(x^{*}, \lambda^{*}$ ) yields a minimum $x^{*}$ of Problem $(P)$.

> **Proposition 50.10.** If the System (KKT-eq) is not solvable, then Program $(P)$ is unbounded below.

*Proof.* We use the fact shown in Section 30.7, that a linear system Bx $= c$ has no solution iff there is some $y$ that $B^{\top}y = 0$ and $y^{\top}c \neq  0$. By changing $y$ to $-y$ if necessary, we may assume that $y^{\top}c > 0$. We apply this fact to the linear system (KKT-eq), so $B$ is the KKT-matrix,
$$\mathbb{R}^{n} \mathbb{R}^{m}$$
which is symmetric, and we obtain the condition that there exist $v \in$ and $\lambda  \in$ such that
$$Pv + A^{\top}\lambda  = 0,Av = 0,-q^{\top}v + b^{\top}\lambda  > 0.$$
Since the $m \times  n$ matrix $A$ has rank $m$ and $b \in \mathbb{R}^{m}$, the system Ax $= b$, is solvable, so for any feasible $x_{0}$ (which means that $Ax_{0} = b)$, since Av $= 0$, the vector $x = x_{0} +$ tv is also a feasible solution for all $t \in \mathbb{R}$. Using the fact that Pv $= -A^{\top}\lambda , v^{\top}P = -\lambda^{\top} A$, Av $= 0, x_{0}^{\top} A^{\top} = b^{\top}$, and $P$ is symmetric, we have
$$J(x_{0} + tv) = J(x_{0}) + (v^{\top}Px_{0} + q^{\top}v)t + (1/2)(v^{\top}Pv)t^{2}$$
$$= J(x_{0}) + (x_{0}^{\top} Pv + q^{\top}v)t -(1/2)(\lambda^{\top} Av)t^{2}$$
$$= J(x_{0}) + (-x_{0}^{\top} A^{\top}\lambda  + q^{\top}v)t$$
$$= J(x_{0}) -(b^{\top}\lambda  -q^{\top}v)t,$$
and since $-q^{\top}v + b^{\top}\lambda  > 0$, the above expression goes to $-\infty$ when $t$ goes to $+\infty$ .

<!-- PAGE 1791 -->
It is obviously important to have criteria to decide whether the KKT-matrix is invertible. There are indeed such criteria, as pointed in Boyd and Vandenberghe $[29]$ (Chapter $10$, Exercise 10.1).

> **Proposition 50.11.** The invertibility of the KKT-matrix
$$\begin{pmatrix} P & A^{\top} \\ A & 0 \end{pmatrix}$$
is equivalent to the following conditions:
$(1)$ For all $x \in \mathbb{R}^{n}$, if Ax $= 0$ with $x \neq  0$, then $x^{\top}Px > 0$; that is, $P$ is positive definite on the kernel of $A$.
$(2)$ The kernels of $A$ and $P$ only have $0$ in common ((Ker $A) \cap$ (Ker $P) = {0})$.
$(3)$ There is some $n\times$ (n-m) matrix $F$ such that Im(F) $=$ Ker $(A)$ and $F^{\top}$ PF is symmetric positive definite.
$(4)$ There is some symmetric positive semidefinite matrix $Q$ such that $P + A^{\top}QA$ is symmetric positive definite. In fact, $Q =$ I works. Proof sketch. Recall from Proposition 6.19 that a square matrix $B$ is invertible iff its kernel is reduced to ${0}$; equivalently, for all $x$, if Bx $= 0$, then $x = 0$. Assume that Condition $(1)$ holds. We have
$$\begin{pmatrix} P & A^{\top} \\ A & 0 \end{pmatrix} \begin{pmatrix} v \\ w \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
iff
$$Pv + A^{\top}w = 0,Av = 0.(*)$$
We deduce that
$$v^{\top}Pv + v^{\top}A^{\top}w = 0,$$
and since
$$v^{\top}A^{\top}w = (Av)^{\top}w = 0w = 0,$$
we obtain $v^{\top}Pv = 0$. Since Condition $(1)$ holds, because $v \in$ Ker $A$, we deduce that $v = 0$. Then $A^{\top}w = 0$, but since the $m \times  n$ matrix $A$ has rank $m$, the $n \times  m$ matrix $A^{\top}$ also has rank $m$, so its columns are linearly independent, and so $w = 0$. Therefore the KKT-matrix is invertible. Conversely, assume that the KKT-matrix is invertible, yet the assumptions of Condition
$(1)$ fail. This means there is some $v \neq  0$ such that Av $= 0$ and $v^{\top}Pv = 0$. We claim that Pv $= 0$. This is because if $P$ is a symmetric positive semidefinite matrix, then for any $v$, we have $v^{\top}Pv = 0$ iff Pv $= 0$.

<!-- PAGE 1792 -->
If Pv $= 0$, then obviously $v^{\top}Pv = 0$, so assume the converse, namely $v^{\top}Pv = 0$. Since $P$ is a symmetric positive semidefinite matrix, it can be diagonalized as
$$P = R^{\top}\Sigma R,$$
where $R$ is an orthogonal matrix and $\Sigma$  is a diagonal matrix
$$\Sigma  = \mathrm{diag}(\lambda_{1} , \dots  , \lambda_{s} , 0, \dots  , 0),$$
where $s$ is the rank of $P$ and $\lambda_{1}  \ge \cdots  \ge \lambda_{s}  > 0$. Then $v^{\top}Pv = 0$ is equivalent to
$$v^{\top}R^{\top}\Sigma Rv = 0,$$
equivalently
$$(Rv)^{\top}\Sigma Rv = 0.$$
If we write Rv $= y$, then we have
$$0 = (Rv)^{\top}\Sigma Rv = y^{\top}\Sigma y = \sum_{i=1}^{s}  \lambda_{i} y_{i}^{2} ,$$
and since $\lambda_{i}  > 0$ for $i = 1, \dots  , s$, this implies that $y_{i} = 0$ for $i = 1, \dots  , s$. Consequently, $\Sigma y = \Sigma$ Rv $= 0$, and so Pv $= R^{\top}\Sigma$ Rv $= 0$, as claimed. Since $v \neq  0$, the vector $(v, 0)$ is a nontrivial solution of Equations (*), a contradiction of the invertibility assumption of the KKT-matrix. Observe that we proved that Av $= 0$ and Pv $= 0$ iff Av $= 0$ and $v^{\top}Pv = 0$, so we easily obtain the fact that Condition $(2)$ is equivalent to the invertibility of the KKT-matrix. Parts
$(3)$ and $(4)$ are left as an exercise. In particular, if $P$ is positive definite, then Proposition 50.11(4) applies, as we already know from Proposition 42.3. In this case, we can solve for $x$ by elimination. We get
$$x = -P^{-1} (A^{\top}\lambda  + q),where\lambda  = -(AP^{-1} A^{\top})^{-1}(b + AP^{-1} q).$$
In practice, we do not invert $P$ and $AP^{-1} A^{\top}$. Instead, we solve the linear systems
$$Pz = q$$
$$PE = A^{\top}$$
$$(AE)\lambda  = -(b + Az)$$
$$Px = -(A^{\top}\lambda  + q).$$
Observe that $(AP^{-1}A^{\top})^{-1}$ is the Schur complement of $P$ in the KKT matrix. Since the KKT-matrix is symmetric, if it is invertible, we can convert it to $LDL^{\top}$ form using Proposition 8.6. This method is only practical when the problem is small or when $A$ and $P$ are sparse.

<!-- PAGE 1793 -->
If the KKT-matrix is invertible but $P$ is not, then we can use a trick involving Proposition 50.11. We find a symmetric positive semidefinite matrix $Q$ such that $P +A^{\top}QA$ is symmetric positive definite, and since a solution $(v, w)$ of the KKT-system should have Av $= b$, we also have $A^{\top}QAv = A^{\top}Qb$, so the KKT-system is equivalent to
$$\begin{pmatrix} P+ A^{\top}QA & A^{\top} \\ A & 0 \end{pmatrix} \begin{pmatrix} v \\ w \end{pmatrix} = \begin{pmatrix} -q + A^{\top}Qb \\ b \end{pmatrix} ,$$
and since $P +A^{\top}QA$ is symmetric positive definite, we can solve this system by elimination. Another way to solve Problem $(P)$ is to use variants of Newton’s method as described in Section 49.9 dealing with equality constraints. Such methods are discussed extensively in Boyd and Vandenberghe $[29]$ (Chapter $10$, Sections 10.2-10.4). There are two variants of this method:
$(1)$ The first method, called feasible start Newton method, assumes that the starting point $u_{0}$ is feasible, which means that $Au_{0} = b$. The Newton step $d_{nt}$ is a feasible direction, which means that $Ad_{nt} = 0$.
$(2)$ The second method, called infeasible start Newton method, does not assume that the starting point $u_{0}$ is feasible, which means that $Au_{0} = b$ may not hold. This method is a little more complicated than the other method. We only briefly discuss the feasible start Newton method, leaving it to the reader to consult Boyd and Vandenberghe $[29]$ (Chapter $10$, Section 10.3) for a discussion of the infeasible start Newton method. The Newton step $d_{nt}$ is the solution of the linear system
$$\begin{pmatrix} \nabla^{2} J(x) & A^{\top} \\ A & 0 \end{pmatrix} \begin{pmatrix} d_{nt} \\ w \end{pmatrix} = \begin{pmatrix} -\nabla J_{x} \\ 0 \end{pmatrix} .$$
The Newton decrement $\lambda (x)$ is defined as in Section 49.9 as
$$.$$
$$\lambda (x) = (d_{nt}^{\top}\nabla^{2} J(x) d_{nt})^{1/2}= \begin{pmatrix} (\nabla J_{x})^{\top}(\nabla^{2} J(x))^{-1}\nabla \end{pmatrix} J_{x}^{1/2}$$
Newton’s method with equality constraints (with feasible start) consists of the following steps: Given a starting point $u_{0} \in$ dom(J) with $Au_{0} = b$, and a tolerance $\epsilon  > 0$ do: repeat
$(1)$ Compute the Newton step and decrement $d_{nt,k} = -(\nabla^{2} J(u_{k}))^{-1}\nabla J_{uk}$ and $\lambda (u_{k})^{2} = (\nabla J_{uk})^{\top}(\nabla^{2} J(u_{k}))^{-1}\nabla J_{uk}$.
$(2)$ Stopping criterion. quit if $\lambda (u_{k})^{2}/2 \le \epsilon$ .
$(3)$ Line Search. Perform an exact or backtracking line search to find $\rho_{k}$ .
