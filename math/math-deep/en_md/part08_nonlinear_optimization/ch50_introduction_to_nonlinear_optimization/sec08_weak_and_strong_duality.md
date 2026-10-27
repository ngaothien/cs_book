# Weak and Strong Duality


<!-- PAGE 1816 -->
Of course, $sup_{\mu\in Rm} G(\mu$ ) and $sup_{(\mu ,\nu)\in Rm\times Rn} G(\mu , \nu$ ) are generally different, but note that
$$b$$
$$+++$$
$$\mathbb{R}_{+}^{n}$$
$G(\mu$ ) $= G(\mu , \nu$ ) iff there is some $\nu  \in$  such that $A^{\top}\mu -\nu +c = 0$ iff $A^{\top}\mu +c \ge 0$. Therefore, $b$ finding $sup_{(\mu ,\nu)\in Rm\times Rn} G(\mu , \nu$ ) is equivalent to the constrained Problem $(D_{1})$
$$++$$
$$maximize-b^{\top}\mu$$
$$subject to A^{\top}\mu  \ge -c, \mu  \ge 0.$$
The above problem is the dual of the Linear Program $(P)$. In summary, the dual function $G$ of a primary Problem $(P)$ often contains hidden inequality constraints that define its domain, and sometimes it is possible to make these domain constraints $\psi_{1} (\mu$ ) $\le 0, \dots  , \psi_{p} (\mu$ ) $\le 0$ explicit, to define a new function $G$ that depends only
$$b$$
on $q < m$ of the variables $\mu_{i}$  and is defined for all values $\mu_{i}  \ge 0$ of these variables, and to replace the Maximization Problem $(D)$, find $sup_{\mu\in Rm} G(\mu$ ), by the constrained Problem
$$+$$
$(D_{1})$
$$maximizeG(\mu )$$
$$b$$
$$subject to \psi_{i} (\mu ) \le 0,i = 1, \dots  , p.$$
Problem $(D_{1})$ is different from the Dual Program $(D)$, but it is equivalent to $(D)$ as a maximization problem.

## 50.8 Weak and Strong Duality

Another important property of the dual function $G$ is that it provides a lower bound on the value of the objective function $J$. Indeed, we have
$$G(\mu ) \le L(u, \mu ) \le J(u)for all u \in U and all \mu  \in \mathbb{R}_{+}^{m},(\dagger )$$
since $\mu  \ge 0$ and $\phi_{i} (u) \le 0$ for $i = 1, \dots  , m$, so
$$G(\mu ) = vinf\in \Omega L(v, \mu ) \le L(u, \mu ) = J(u) + \sum_{i=1}^{m}  \mu_{i} \phi_{i} (u) \le J(u).$$
If the Primal Problem $(P)$ has a minimum denoted $p^{*}$ and the Dual Problem $(D)$ has a maximum denoted $d^{*}$, then the above inequality implies that
$$d^{*}\le p^{*}(\dagger_{w} )$$
known as weak duality. Equivalently, for every optimal solution $\lambda^{*}$ of the dual problem and every optimal solution $u^{*}$ of the primal problem, we have
$$G(\lambda^{*} ) \le J(u^{*}).(\dagger_{w'} )$$
In particular, if $p^{*} = -\infty$ , which means that the primal problem is unbounded below, then the dual problem is unfeasible. Conversely, if $d^{*} = +\infty$ , which means that the dual problem is unbounded above, then the primal problem is unfeasible.

<!-- PAGE 1817 -->

> **Definition 50.10.** The difference $p^{*}-d^{*} \ge 0$ is called the optimal duality gap. If the duality gap is zero, that is, $p^{*} = d^{*}$, then we say that strong duality holds. Even when the duality gap is strictly positive, the inequality $(\dagger_{w}$ ) can be helpful to find a lower bound on the optimal value of a primal problem that is difficult to solve, since the dual problem is always convex. If the primal problem and the dual problem are feasible and if the optimal values $p^{*}$ and $d^{*}$ are finite and $p^{*} = d^{*}$ (no duality gap), then the complementary slackness conditions hold for the inequality constraints.

> **Proposition 50.16.** (Complementary Slackness) Given the Minimization Problem $(P)$
$$minimizeJ(v)$$
$$subject to \phi_{i} (v) \le 0,i = 1, \dots  , m,$$
and its Dual Problem $(D)$
$$maximizeG(\mu )$$
$$subject to \mu  \in \mathbb{R}_{+}^{m},$$
if both $(P)$ and $(D)$ are feasible, $u \in U$ is an optimal solution of $(P), \lambda  \in \mathbb{R}_{+}^{m}$ is an optimal solution of $(D)$, and J(u) $= G(\lambda$ ), then
$$\sum_{i=1}^{m}  \lambda_{i} \phi_{i} (u) = 0.$$
In other words, if the constraint $\phi_{i}$  is inactive at $u$, then $\lambda_{i}  = 0$.

*Proof.* Since J(u) $= G(\lambda$ ) we have J(u) $= G(\lambda$ )
$$= infJ(v) + \sum_{i=1}^{m}  \lambda_{i} \phi_{i} (v)!by definition of G$$
$$v\in \Omega$$
$$\le J(u) + \sum_{i=1}^{m}  \lambda_{i} \phi_{i} (u)the greatest lower bound is a lower bound$$
$$\le J(u)since \lambda_{i}  \ge 0, \phi_{i} (u) \le 0.$$
$$which implies that \sum_{i}  m=1 \lambda_{i} \phi_{i} (u) = 0.$$
Going back to Example 50.5, we see that weak duality says that for any feasible solution
$$\mathbb{R}^{n}$$
$u$ of the Primal Problem $(P)$, that is, some $u \in$ such that
$$Au \le b, u \ge 0,$$

<!-- PAGE 1818 -->
$$\mathbb{R}^{m}$$
and for any feasible solution $\mu  \in$ of the Dual Problem $(D_{1})$, that is,
$$A^{\top}\mu  \ge -c, \mu  \ge 0,$$
we have
$$-b^{\top}\mu  \le c^{\top}u.$$
Actually, if $u$ and $\lambda$  are optimal, then we know from Theorem 47.7 that strong duality holds, namely $-b^{\top}\mu  = c^{\top}u$, but the proof of this fact is nontrivial. The following theorem establishes a link between the solutions of the Primal Problem
$(P)$ and those of the Dual Problem $(D)$. It also gives sufficient conditions for the duality gap to be zero.

> **Theorem 50.17.** Consider the Minimization Problem $(P)$:
$$minimizeJ(v)$$
$$subject to \phi_{i} (v) \le 0,i = 1, \dots  , m,$$
where the functions $J$ and $\phi_{i}$  are defined on some open subset $\Omega$ of a finite-dimensional Euclidean vector space $V$ (more generally, a real Hilbert space $V$ ).
$(1)$ Suppose the functions $\phi_{i}$  : $\Omega \to \mathbb{R}$ are continuous, and that for every $\mu  \in \mathbb{R}_{+}^{m}$, the Problem $(P_{\mu})$:
$$minimizeL(v, \mu )$$
$$subject to v \in \Omega ,$$
has a unique solution $u_{\mu}$, so that
$$L(u_{\mu}, \mu ) = infL(v, \mu ) = G(\mu ),$$
$$v\in \Omega$$
and the function $\mu  \mapsto u_{\mu}$ is continuous (on $\mathbb{R}_{+}^{m})$. Then the function $G$ is differentiable for all $\mu  \in \mathbb{R}_{+}^{m}$, and
$$G_{\mu}'(\xi ) = \sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu})for all \xi  \in \mathbb{R}^{m}.$$
If $\lambda$  is any solution of Problem $(D)$:
$$maximizeG(\mu )$$
$$subject to \mu  \in \mathbb{R}_{+}^{m},$$
then the solution $u_{\lambda}$ of the corresponding problem $(P_{\lambda})$ is a solution of Problem $(P)$.

<!-- PAGE 1819 -->
$(2)$ Assume Problem $(P)$ has some solution $u \in U$, and that $\Omega$ is convex (open), the functions $\phi_{i}  (1 \le i \le m)$ and $J$ are convex and differentiable at $u$, and that the constraints are qualified. Then Problem $(D)$ has a solution $\lambda  \in \mathbb{R}_{+}^{m}$, and J(u) $= G(\lambda$ ); that is, the duality gap is zero.

*Proof.* $(1)$ Our goal is to prove that for any solution $\lambda$  of Problem $(D)$, the pair $(u_{\lambda}, \lambda$ ) is a saddle point of $L$. By Theorem 50.15(1), the point $u_{\lambda} \in U$ is a solution of Problem $(P)$. Since $\lambda  \in \mathbb{R}_{+}^{m}$ is a solution of Problem $(D)$, by definition of $G(\lambda$ ) and since $u_{\lambda}$ satisfies Problem $(P_{\lambda})$, we have
$$G(\lambda ) = infL(v, \lambda ) = L(u_{\lambda}, \lambda ),$$
$$v\in \Omega$$
which is one of the two equations characterizing a saddle point. In order to prove the second equation characterizing a saddle point,
$$supL(u_{\mu}, \mu ) = L(u_{\lambda}, \lambda ),$$
$$\mu \in \mathbb{R} m$$
$$+$$
we will begin by proving that the function $G$ is differentiable for all $\mu  \in \mathbb{R}_{+}^{m}$, in order to be able to apply Theorem 40.9 to conclude that since $G$ has a maximum at $\lambda$ , that is, $-G$ has minimum at $\lambda$ , then $-G_{\lambda}'(\mu$  - $\lambda$ ) $\ge 0$ for all $\mu  \in \mathbb{R}_{+}^{m}$. In fact, we prove that
$$G_{\mu}'(\xi ) = \sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu})for all \xi  \in \mathbb{R}^{m}.(*_{deriv})$$
Consider any two points $\mu$  and $\mu  + \xi$  in $\mathbb{R}_{+}^{m}$. By definition of $u_{\mu}$ we have
$$L(u_{\mu}, \mu ) \le L(u_{\mu+\xi}, \mu ),$$
which means that
$$J(u_{\mu}) + \sum_{i=1}^{m}  \mu_{i} \phi_{i} (u_{\mu}) \le J(u_{\mu+\xi}) + \sum_{i=1}^{m}  \mu_{i} \phi_{i} (u_{\mu+\xi}),(*_{1})$$
$$and since G(\mu ) = L(u_{\mu}, \mu ) = J(u_{\mu}) + \sum_{i}  m \mu_{i} \phi_{i} (u_{\mu}) and G(\mu  + \xi ) = L(u_{\mu+\xi}, \mu  + \xi ) =$$
$$J(u_{\mu+\xi}) + \sum_{i}  m=1(\mu_{i}  + \xi_{i} )\phi_{i} (u_{\mu+\xi}), we have^{=1}$$
$$G(\mu  + \xi ) -G(\mu ) = J(u_{\mu+\xi}) -J(u_{\mu}) + \sum_{i=1}^{m}  (\mu_{i}  + \xi_{i} )\phi_{i} (u_{\mu+\xi}) - \sum_{i=1}^{m}  \mu_{i} \phi_{i} (u_{\mu}).(*_{2})$$
Since $(*_{1})$ can be written as
$$0 \le J(u_{\mu+\xi}) -J(u_{\mu}) + \sum_{i=1}^{m}  \mu_{i} \phi_{i} (u_{\mu+\xi}) - \sum_{i=1}^{m}  \mu_{i} \phi_{i} (u_{\mu}),$$

<!-- PAGE 1820 -->
$$by adding \sum_{i}  m=1 \xi_{i} \phi_{i} (u_{\mu+\xi}) to both sides of the above inequality and using (*_{2}) we get$$
$$\sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu+\xi}) \le G(\mu  + \xi ) -G(\mu ).(*_{3})$$
By definition of $u_{\mu+\xi}$ we have
$$L(u_{\mu+\xi}, \mu  + \xi ) \le L(u_{\mu}, \mu  + \xi ),$$
which means that
$$J(u_{\mu+\xi}) + \sum_{i=1}^{m}  (\mu_{i}  + \xi_{i} )\phi_{i} (u_{\mu+\xi}) \le J(u_{\mu}) + \sum_{i=1}^{m}  (\mu_{i}  + \xi_{i} )\phi_{i} (u_{\mu}).(*_{4})$$
This can be written as
$$J(u_{\mu+\xi}) -J(u_{\mu}) + \sum_{i=1}^{m}  (\mu_{i}  + \xi_{i} )\phi_{i} (u_{\mu+\xi}) - \sum_{i=1}^{m}  (\mu_{i}  + \xi_{i} )\phi_{i} (u_{\mu}) \le 0,$$
$$and by adding \sum_{i}  m=1 \xi_{i} \phi_{i} (u_{\mu}) to both sides of the above inequality and using (*_{2}) we get$$
$$G(\mu  + \xi ) -G(\mu ) \le \sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu}).(*_{5})$$
By putting $(*_{3})$ and $(*_{5})$ together we obtain
$$\sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu+\xi}) \le G(\mu  + \xi ) -G(\mu ) \le \sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu}).(*_{6})$$
Consequently there is some $\theta  \in [0, 1]$ such that
$$G(\mu  + \xi ) -G(\mu ) = (1 -\theta ) \begin{pmatrix} \xi_{i} \phi_{i} (u_{\mu}) \end{pmatrix} \sum_{i=1}^{m}  + \theta \begin{pmatrix} \xi_{i} \phi_{i} (u_{\mu+\xi}) \end{pmatrix} \sum_{i=1}^{m}$$
$$= \sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu}) + \theta \begin{pmatrix} \xi_{i} (\phi_{i} (u_{\mu+\xi}) -\phi_{i} (u_{\mu})) \end{pmatrix} \sum_{i=1}^{m}  .$$
Since by hypothesis the functions $\mu  \mapsto u_{\mu}$ (from $\mathbb{R}_{+}^{m}$ to $\Omega$ ) and $\phi_{i}$  : $\Omega \to \mathbb{R}$ are continuous, for any $\mu  \in \mathbb{R}_{+}^{m}$ we can write
$$G(\mu  + \xi ) -G(\mu ) = \sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu}) + \|\xi \|\epsilon (\xi ),with lim_{\xi\mapsto0} \epsilon (\xi ) = 0,(*_{7})$$

<!-- PAGE 1821 -->
for any $\|\|$ norm on $\mathbb{R}^{m}$. Equation $(*_{7})$ show that $G$ is differentiable for any $\mu  \in \mathbb{R}_{+}^{m}$, and that
$$G_{\mu}'(\xi ) = \sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu})for all \xi  \in \mathbb{R}^{m}.(*_{8})$$
Actually there is a small problem, namely that the notion of derivative was defined for a function defined on an open set, but $\mathbb{R}_{+}^{m}$ is not open. The difficulty only arises to ensure that the derivative is unique, but in our case we have a unique expression for the derivative so there is no problem as far as defining the derivative. There is still a potential problem, which is that we would like to apply Theorem 40.9 to conclude that since $G$ has a maximum at $\lambda$ , that is, $-G$ has a minimum at $\lambda$ , then
$$-G_{\lambda}'(\mu  -\lambda ) \ge 0for all \mu  \in \mathbb{R}_{+}^{m},(*_{9})$$
but the hypotheses of Theorem 40.9 require the domain of the function to be open. Fortunately, close examination of the proof of Theorem 40.9 shows that the proof still holds with $U =\mathbb{R}_{+}^{m}$. Therefore, $(*_{8})$ holds, Theorem 40.9 is valid, which in turn implies
$$G_{\lambda}'(\mu  -\lambda ) \le 0for all \mu  \in \mathbb{R}_{+}^{m},(*_{10})$$
which, using the expression for $G_{\lambda}'$ given in $(*_{8})$ gives
$$\sum_{i=1}^{m}  \mu_{i} \phi_{i} (u_{\lambda}) \le \sum_{i=1}^{m}  \lambda_{i} \phi_{i} (u_{\lambda}),for all \mu  \in \mathbb{R}_{+}^{m}.(*_{11})$$
As a consequence of $(*_{11})$, we obtain
$$L(u_{\lambda}, \mu ) = J(u_{\lambda}) + \sum_{i=1}^{m}  \mu_{i} \phi_{i} (u_{\lambda})$$
$$\le J(u_{\lambda}) + \sum_{i=1}^{m}  \lambda_{i} \phi_{i} (u_{\lambda}) = L(u_{\lambda}, \lambda ),$$
for all $\mu  \in \mathbb{R}_{+}^{m}$, that is,
$$L(u_{\lambda}, \mu ) \le L(u_{\lambda}, \lambda ),for all \mu  \in \mathbb{R}_{+}^{m},(*_{12})$$
which implies the second inequality
$$supL(u_{\mu}, \mu ) = L(u_{\lambda}, \lambda )$$
$$\mu \in \mathbb{R} m$$
$$+$$
stating that $(u_{\lambda}, \lambda$ ) is a saddle point. Therefore, $(u_{\lambda}, \lambda$ ) is a saddle point of $L$, as claimed.
$(2)$ The hypotheses are exactly those required by Theorem 50.15(2), thus there is some $\lambda  \in \mathbb{R}_{+}^{m}$ such that $(u, \lambda$ ) is a saddle point of the Lagrangian $L$, and by Theorem 50.15(1) we have J(u) $=$ L(u, $\lambda$ ). By Proposition 50.14, we have
$$J(u) = L(u, \lambda ) = infL(v, \lambda ) = supinfL(v, \mu ),$$
$$v\in \Omega \mu \in \mathbb{R} mv\in \Omega$$
$$+$$

<!-- PAGE 1822 -->
which can be rewritten as
$$J(u) = G(\lambda ) = supG(\mu ).$$
$$\mu \in \mathbb{R} m$$
$$+$$
In other words, Problem $(D)$ has a solution, and J(u) $= G(\lambda$ ).
Remark: Note that Theorem 50.17(2) could have already be obtained as a consequence of Theorem 50.15(2), but the dual function $G$ was not yet defined. If $(u, \lambda$ ) is a saddle point of the Lagrangian $L$ (defined on $\Omega \times \mathbb{R}_{+}^{m})$, then by Proposition 50.14, the vector $\lambda$  is a solution of Problem $(D)$. Conversely, under the hypotheses of Part $(1)$ of Theorem 50.17, if $\lambda$  is a solution of Problem $(D)$, then $(u_{\lambda}, \lambda$ ) is a saddle point of $L$. Consequently, under the above hypotheses, the set of solutions of the Dual Problem $(D)$ coincide with the set of second arguments $\lambda$  of the saddle points $(u, \lambda$ ) of $L$. In some sense, this result is the “dual” of the result stated in Theorem 50.15, namely that the set of solutions of Problem $(P)$ coincides with set of first arguments $u$ of the saddle points $(u, \lambda$ ) of $L$. Informally, in Theorem 50.17(1), the hypotheses say that if $G(\mu$ ) can be “computed nicely,” in the sense that there is a unique minimizer $u_{\mu}$ of L(v, $\mu$ ) (with $v \in \Omega$ ) such that $G(\mu$ ) $= L(u_{\mu}, \mu$ ), and if a maximizer $\lambda$  of $G(\mu$ ) (with $\mu  \in \mathbb{R}_{+}^{m})$ can be determined, then $u_{\lambda}$ yields the minimum value of $J$, that is, $p^{*} = J(u_{\lambda})$. If the constraints are qualified and if the functions $J$ and $\phi_{i}$  are convex and differentiable, then since the KKT conditions hold, the duality gap is zero; that is,
$$G(\lambda ) = L(u_{\lambda}, \lambda ) = J(u_{\lambda}).$$

> **Example 50.6.** Going back to Example 50.5 where we considered the linear program $(P)$
$$minimizec^{\top}v$$
$$subject to Av \le b, v \ge 0,$$
with $A$ an $m \times  n$ matrix, the Lagrangian L(v, $\mu , \nu$ ) is given by
$$L(v, \mu , \nu ) = -b^{\top}\mu  + (c + A^{\top}\mu  -\nu )^{\top}v,$$
and we found that the dual function $G(\mu , \nu$ ) $= inf_{v\in Rn}$ L(v, $\mu , \nu$ ) is given for all $\mu  \ge 0$ and $\nu  \ge 0$ by
$$($$
$$-b^{\top}\mu if A^{\top}\mu  -\nu  + c = 0,$$
$$G(\mu , \nu ) =$$
$$-\infty otherwise.$$
$$\mathbb{R}^{n}$$
The hypotheses of Theorem 50.17(1) certainly fail since there are infinitely $u_{\mu ,\nu} \in$ such that $G(\mu , \nu$ ) $= inf_{v\in Rn}$ L(v, $\mu , \nu$ ) $= L(u_{\mu ,\nu}, \mu , \nu$ ). Therefore, the dual function $G$ is no help in finding a solution of the Primal Problem $(P)$. As we saw earlier, if we consider the modified dual Problem $(D_{1})$ then strong duality holds, but this does not follow from Theorem 50.17, and a different proof is required.

<!-- PAGE 1823 -->
Thus, we have the somewhat counter-intuitive situation that the general theory of Lagrange duality does not apply, at least directly, to linear programming, a fact that is not sufficiently emphasized in many expositions. A separate treatment of duality is required. Unlike the case of linear programming, which needs a separate treatment, Theorem 50.17 applies to the optimization problem involving a convex quadratic objective function and a set of affine inequality constraints. So in some sense, convex quadratic programming is simpler than linear programming!

> **Example 50.7.** Consider the quadratic objective function
$$J(v) = \frac{1}{2} v^{\top}Av -v^{\top}b,$$
where $A$ is an $n \times  n$ matrix which is symmetric positive definite, $b \in \mathbb{R}^{n}$, and the constraints are affine inequality constraints of the form
$$Cv \le d,$$
where $C$ is an $m \times  n$ matrix and $d \in \mathbb{R}^{m}$. For the time being, we do not assume that $C$ has rank $m$. Since $A$ is symmetric positive definite, $J$ is strictly convex, as implied by Proposition 40.11 (see Example 40.6). The Lagrangian of this quadratic optimization problem is given by
$$L(v, \mu ) = \frac{1}{2} v^{\top}Av -v^{\top}b + (Cv -d)^{\top}\mu$$
$$= \frac{1}{2} v^{\top}Av -v^{\top}(b -C^{\top}\mu ) -\mu^{\top} d.$$
Since $A$ is symmetric positive definite, by Proposition 42.2, the function $v \mapsto$ L(v, $\mu$ ) has a unique minimum obtained for the solution $u_{\mu}$ of the linear system
$$Av = b -C^{\top}\mu ;$$
that is,
$$u_{\mu} = A^{-1}(b -C^{\top}\mu ).$$
This shows that the Problem $(P_{\mu})$ has a unique solution which depends continuously on $\mu$ . Then for any solution $\lambda$  of the dual problem, $u_{\lambda} = A^{-1}(b$ - $C^{\top}\lambda$ ) is an optimal solution of the primal problem.

<!-- PAGE 1824 -->
We compute $G(\mu$ ) as follows:
$$G(\mu ) = L(u_{\mu}, \mu ) = \frac{1}{2} u_{\mu}^{\top} Au_{\mu} -u_{\mu}^{\top} (b -C^{\top}\mu ) -\mu^{\top} d$$
$$= \frac{1}{2} u_{\mu}^{\top} (b -C^{\top}\mu ) -u_{\mu}^{\top} (b -C^{\top}\mu ) -\mu^{\top} d$$
$$= - \frac{1}{2} u_{\mu}^{\top} (b -C^{\top}\mu ) -\mu^{\top} d$$
$$= - \frac{1}{2} (b -C^{\top}\mu )^{\top}A^{-1}(b -C^{\top}\mu ) -\mu^{\top} d$$
$$= - \frac{1}{2} \mu^{\top} CA^{-1}C^{\top}\mu  + \mu^{\top} (CA^{-1}b -d) - \frac{1}{2} b^{\top}A^{-1}b.$$
Since $A$ is symmetric positive definite, the matrix $CA^{-1}C^{\top}$ is symmetric positive semidefinite. Since $A^{-1}$ is also symmetric positive definite, $\mu^{\top} CA^{-1}C^{\top}\mu  = 0 iff(C^{\top}\mu )^{\top}A^{-1}(C^{\top}\mu$ ) $= 0$ iff $C^{\top}\mu  = 0$ implies $\mu  = 0$, that is, Ker $C^{\top} = (0)$, which is equivalent to Im(C) $= \mathbb{R}^{m}$, namely if $C$ has rank $m$ (in which case, $m \le n)$. Thus $CA^{-1}C^{\top}$ is symmetric positive definite iff $C$ has rank $m$. We showed just after Theorem 49.8 that the functional $v \mapsto (1/2)v^{\top}Av$ is elliptic iff $A$ is symmetric positive definite, and Theorem 49.8 shows that an elliptic functional is coercive, which is the hypothesis used in Theorem 49.4. Therefore, by Theorem 49.4, if the inequalities Cx $\le d$ have a solution, the primal problem has a unique solution. In this case, as a consequence, by Theorem 50.17(2), the function $-G(\mu$ ) always has a minimum, which is unique if $C$ has rank $m$. The fact that $-G(\mu$ ) has a minimum is not obvious when $C$ has rank $< m$, since in this case $CA^{-1}C^{\top}$ is not invertible. We also verify easily that the gradient of $G$ is given by
$$\nabla G_{\mu} = Cu_{\mu} -d = -CA^{-1}C^{\top}\mu  + CA^{-1}b -d.$$
Observe that since $CA^{-1}C^{\top}$ is symmetric positive semidefinite, $-G(\mu$ ) is convex. Therefore, if $C$ has rank $m$, a solution of Problem $(P)$ is obtained by finding the unique solution $\lambda$  of the equation
$$-CA^{-1}C^{\top}\mu  + CA^{-1}b -d = 0,$$
and then the minimum $u_{\lambda}$ of Problem $(P)$ is given by
$$u_{\lambda} = A^{-1}(b -C^{\top}\lambda ).$$
If $C$ has rank $< m$, then we can find $\lambda  \ge 0$ by finding a feasible solution of the linear program whose set of constraints is given by
$$-CA^{-1}C^{\top}\mu  + CA^{-1}b -d = 0,$$
using the standard method of adding nonnegative slack variables $\xi_{1} , \dots  , \xi_{m}$  and maximizing $-(\xi_{1}  + \cdots  + \xi_{m}$ ).
