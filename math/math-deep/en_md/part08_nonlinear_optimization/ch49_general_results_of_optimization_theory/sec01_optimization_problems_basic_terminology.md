# Optimization Problems; Basic Terminology


<!-- PAGE 1703 -->
Chapter $49$ General Results of Optimization Theory This chapter is devoted to some general results of optimization theory. A main theme is to find sufficient conditions that ensure that an objective function has a minimum which is achieved. We define the notion of a coercive function. The most general result is Theorem 49.2, which applies to a coercive convex function on a convex subset of a separable Hilbert space. In the special case of a coercive quadratic functional, we obtain the Lions– Stampacchia theorem (Theorem 49.6), and the Lax–Milgram theorem (Theorem 49.7). We define elliptic functionals, which generalize quadratic functions defined by symmetric positive definite matrices. We define gradient descent methods, and discuss their convergence. A gradient descent method looks for a descent direction and a stepsize parameter, which is obtained either using an exact line search or a backtracking line search. A popular technique to find the search direction is steepest descent. In addition to steepest descent for the Euclidean norm, we discuss steepest descent for an arbitrary norm. We also consider a special case of steepest descent, Newton’s method. This method converges faster than the other gradient descent methods, but it is quite expensive since it requires computing and storing Hessians. We also present the method of conjugate gradients and prove its correctness. We briefly discuss the method of gradient projection and the penalty method in the case of constrained optima.

## 49.1 Optimization Problems; Basic Terminology

The main goal of optimization theory is to construct algorithms to find solutions (often approximate) of problems of the form
$$findu$$
$$such that u \in U and J(u) = \inf J(v),$$
$$v\in U$$
where $U$ is a given subset of a (real) vector space $V$ (possibly infinite dimensional) and $J$ : $\Omega \to \mathbb{R}$ is a function defined on some open subset $\Omega$ of $V$ such that $U \subseteq \Omega$ .
$$1703$$

<!-- PAGE 1704 -->
To be very clear, $inf_{v\in U}$ J(v) denotes the greatest lower bound of the set of real numbers ${J(u)$ | $u \in U}$. To make sure that we are on firm grounds, let us review the notions of greatest lower bound and least upper bound of a set of real numbers. Let $X$ be any nonempty subset of $\mathbb{R}$. The set LB(X) of lower bounds of $X$ is defined as
$$LB(X) = {b \in \mathbb{R} | b \le x for all x \in X}.$$
If the set $X$ is not bounded below, which means that for every $r \in \mathbb{R}$ there is some $x \in X$ such that $x < r$, then LB(X) is empty. Otherwise, if LB(X) is nonempty, since it is bounded above by every element of $X$, by a fundamental property of the real numbers, the set LB(X) has a greatest element denoted inf $X$. The real number inf $X$ is thus the greatest lower bound of $X$. In general, inf $X$ does not belong to $X$, but if it does, then it is the least element of $X$. If LB(X) $= \emptyset$ , then $X$ is unbounded below and inf $X$ is undefined. In this case (with an abuse of notation), we write
$$\inf X = -\infty .$$
By convention, when $X = \emptyset$ we set
$$\inf \emptyset = +\infty .$$
For example, if $X = {x \in \mathbb{R}$ | $x \le 0}$, then LB(X) $= \emptyset$ . On the other hand, if $X = {1/n$ | $n \in \mathbb{N} -{0}}$, then LB(X) $= {x \in \mathbb{R}$ | $x \le 0}$ and inf $X = 0$, which is not in $X$. Similarly, the set UB(X) of upper bounds of $X$ is given by
$$UB(X) = {u \in \mathbb{R} | x \le u for all x \in X}.$$
If $X$ is not bounded above, then UB(X) $= \emptyset$ . Otherwise, if UB(X) $\neq  \emptyset$ , then it has least element denoted sup $X$. Thus sup $X$ is the least upper bound of $X$. If sup $X \in X$, then it is the greatest element of $X$. If UB(X) $= \emptyset$ , then
$$\sup X = +\infty .$$
By convention, when $X = \emptyset$ we set
$$\sup \emptyset = -\infty .$$
For example, if $X = {x \in \mathbb{R}$ | $x \ge 0}$, then UB(X) $= \emptyset$ . On the other hand, if $X = {1$ - $1/n$ | $n \in \mathbb{N} -{0}}$, then UB(X) $= {x \in \mathbb{R}$ | $x \ge 1}$ and sup $X = 1$, which is not in $X$. The element $inf_{v\in U}$ J(v) is just $inf{J(v)$ | $v \in U}$. The notation $J^{*}$ is often used to denote $inf_{v\in U}$ J(v). If the function $J$ is not bounded below, which means that for every $r \in \mathbb{R}$, there is some $u \in U$ such that J(u) $< r$, then
$$\inf J(v) = -\infty ,$$
$$v\in U$$

<!-- PAGE 1705 -->
and we say that our minimization problem has no solution, or that it is unbounded (below). For example, if $V = \Omega = \mathbb{R}, U = {x \in \mathbb{R}$ | $x \le 0}$, and J(x) $= x$, then the function J(x) is not bounded below and $inf_{v\in U}$ J(v) $= -\infty$ . The issue is that $J^{*}$ may not belong to ${J(u)$ | $u \in U}$, that is, it may not be achieved by some element $u \in U$, and solving the above problem consists in finding some $u \in U$ that achieves the value $J^{*}$ in the sense that J(u) $= J^{*}$. If no such $u \in U$ exists, again we say that our minimization problem has no solution. The minimization problem
$$findu$$
$$such that u \in U and J(u) = \inf J(v)$$
$$v\in U$$
is often presented in the following more informal way:
$$minimizeJ(v)$$
$$( Problem M)$$
$$subject to v \in U.$$
A vector $u \in U$ such that J(u) $= inf_{v\in U}$ J(v) is often called a minimizer of $J$ over $U$. Some authors denote the set of minimizers of $J$ over $U$ by arg $min_{v\in U}$ J(v) and write
$$u \in arg minJ(v)$$
$$v\in U$$
to express that $u$ is such a minimizer. When such a minimizer is unique, by abuse of notation, this unique minimizer $u$ is denoted by
$$u = arg minJ(v).$$
$$v\in U$$
We prefer not to use this notation, although it seems to have invaded the literature. If we need to maximize rather than minimize a function, then we try to find some $u \in U$ such that
$$J(u) = supJ(v).$$
$$v\in U$$
Here $sup_{v\in U}$ J(v) is the least upper bound of the set ${J(u)$ | $u \in U}$. Some authors denote the set of maximizers of $J$ over $U$ by arg $max_{v\in U}$ J(v).
Remark: Some authors define an extended real-valued function as a function $f$ : $\Omega \to \mathbb{R}$ which is allowed to take the value $-\infty$ or even $+\infty$ for some of its arguments. Although this may be convenient to deal with situations where we need to consider $inf_{v\in U}$ J(v) or $sup_{v\in U}$ J(v), such “functions” are really partial functions and we prefer not to use the notion of extended real-valued function.

<!-- PAGE 1706 -->
In most cases, $U$ is defined as the set of solutions of a finite sets of constraints, either equality constraints $\phi_{i} (v) = 0$, or inequality constraints $\phi_{i} (v) \le 0$, where the $\phi_{i}$  : $\Omega \to \mathbb{R}$ are some given functions. The function $J$ is often called the functional of the optimization problem. This is a slightly odd terminology, but it is justified if $V$ is a function space. The following questions arise naturally:
$(1)$ Results concerning the existence and uniqueness of a solution for Problem $(M)$. In the next section we state sufficient conditions either on the domain $U$ or on the function $J$ that ensure the existence of a solution.
$(2)$ The characterization of the possible solutions of Problem $M$. These are conditions for any element $u \in U$ to be a solution of the problem. Such conditions usually involve the derivative $dJ_{u}$ of $J$, and possibly the derivatives of the functions $\phi_{i}$  defining $U$. Some of these conditions become sufficient when the functions $\phi_{i}$  are convex,
$(3)$ The effective construction of algorithms, typically iterative algorithms that construct a sequence $(u_{k})_{k\ge1}$ of elements of $U$ whose limit is a solution $u \in U$ of our problem. It is then necessary to understand when and how quickly such sequences converge. Gradient descent methods fall under this category. As a general rule, unconstrained problems (for which $U = \Omega = V$ ) are (much) easier to deal with than constrained problems (where $U \neq  V$ ). The material of this chapter is heavily inspired by Ciarlet $[41]$. In this chapter it is assumed that $V$ is a real vector space with an inner product $\langle$ -, $-\rangle$ . If $V$ is infinite dimensional, then we assume that it is a real Hilbert space (it is complete). As usual, we write $\|u\| = \langle u, u\rangle^{1/2}$ for the norm associated with the inner product $\langle$ -, $-\rangle$ . The reader may want to review Section 48.1, especially the projection lemma and the Riesz representation theorem. As a matter of terminology, if $U$ is defined by inequality and equality constraints as
$$U = {v \in \Omega | \phi_{i} (v) \le 0, i = 1, \dots  , m, \psi_{j} (v) = 0, j = 1, \dots  , p},$$
if $J$ and all the functions $\phi_{i}$  and $\psi_{j}$  are affine, the problem is said to be linear (or a linear program), and otherwise nonlinear. If $J$ is of the form
$$J(v) = \langle Av, v\rangle -\langle b, v\rangle$$
where $A$ is a nonzero symmetric positive semidefinite matrix and the constraints are affine, the problem is called a quadratic programming problem. If the inner product $\langle$ -, $-\rangle$ is the standard Euclidean inner product, $J$ is also expressed as
$$J(v) = v^{\top}Av -b^{\top}v.$$
