# Handling Equality Constraints Explicitly


<!-- PAGE 1825 -->

## 50.9 Handling Equality Constraints Explicitly

Sometimes it is desirable to handle equality constraints explicitly (for instance, this is what Boyd and Vandenberghe do, see $[29])$. The only difference is that the Lagrange multipliers associated with equality constraints are not required to be nonnegative, as we now show. Consider the Optimization Problem (P' )
$$minimizeJ(v)$$
$$subject to \phi_{i} (v) \le 0,i = 1, \dots  , m$$
$$\psi_{j} (v) = 0,j = 1, \dots  , p.$$
We treat each equality constraint $\psi_{j} (u) = 0$ as the conjunction of the inequalities $\psi_{j} (u) \le 0$ and $-\psi_{j} (u) \le 0$, and we associate Lagrange multipliers $\lambda  \in \mathbb{R}_{+}^{m}$, and $\nu^{+} , \nu^{-} \in \mathbb{R}_{+}^{p}$. Assuming that the constraints are qualified, by Theorem 50.5, the KKT conditions are
$$J_{u}' + \sum_{i=1}^{m}  \lambda_{i} (\phi_{i}' )_{u} + \sum_{j=1}^{p}  \nu_{j}^{+}  (\psi_{j}' )_{u} - \sum_{j=1}^{p}  \nu_{j}^{-}  (\psi_{j}' )_{u} = 0,$$
and
$$\sum_{i=1}^{m}  \lambda_{i} \phi_{i} (u) + \sum_{j=1}^{p}  \nu_{j}^{+}  \psi_{j} (u) - \sum_{j=1}^{p}  \nu_{j}^{-}  \psi_{j} (u) = 0,$$
with $\lambda  \ge 0, \nu^{+} \ge 0, \nu^{-} \ge 0$. Since $\psi_{j} (u) = 0$ for $j = 1, \dots  , p$, these equations can be rewritten as
$$J_{u}' + \sum_{i=1}^{m}  \lambda_{i} (\phi_{i}' )_{u} + \sum_{j=1}^{p}  (\nu_{j}^{+}  -\nu_{j}^{-}  )(\psi_{j}' )_{u} = 0,$$
and
$$\sum_{i=1}^{m}  \lambda_{i} \phi_{i} (u) = 0$$
with $\lambda  \ge 0, \nu^{+} \ge 0, \nu^{-} \ge 0$, and if we introduce $\nu_{j}  = \nu_{j}^{+}$  - $\nu_{j}^{-}$  we obtain the following KKT conditions for programs with explicit equality constraints:
$$J_{u}' + \sum_{i=1}^{m}  \lambda_{i} (\phi_{i}' )_{u} + \sum_{j=1}^{p}  \nu_{j} (\psi_{j}' )_{u} = 0,$$
and
$$\sum_{i=1}^{m}  \lambda_{i} \phi_{i} (u) = 0$$
$$\mathbb{R}^{p}$$
with $\lambda  \ge 0$ and $\nu  \in$ arbitrary.

<!-- PAGE 1826 -->
Let us now assume that the functions $\phi_{i}$  and $\psi_{j}$  are convex. As we explained just after Definition 50.6, nonaffine equality constraints are never qualified. Thus, in order to generalize Theorem 50.6 to explicit equality constraints, we assume that the equality constraints $\psi_{j}$  are affine.

> **Theorem 50.18.** Let $\phi_{i}$  : $\Omega \to \mathbb{R}$ be $m$ convex inequality constraints and $\psi_{j}$  : $\Omega \to \mathbb{R}$ be $p$ affine equality constraints defined on some open convex subset $\Omega$ of a finite-dimensional Euclidean vector space $V$ (more generally, a real Hilbert space $V$ ), let $J$ : $\Omega \to \mathbb{R}$ be some function, let $U$ be given by
$$U = {x \in \Omega | \phi_{i} (x) \le 0, \psi_{j} (x) = 0, 1 \le i \le m, 1 \le j \le p},$$
and let $u \in U$ be any point such that the functions $\phi_{i}$  and $J$ are differentiable at $u$.
$(1)$ If $J$ has a local minimum at $u$ with respect to $U$, and if the constraints are qualified, then there exist some vectors $\lambda  \in \mathbb{R}_{+}^{m}$ and $\nu  \in \mathbb{R}^{p}$, such that the KKT condition hold:
$$J_{u}' + \sum_{i=1}^{m}  \lambda_{i} (u)(\phi_{i}' )_{u} + \sum_{j=1}^{p}  \nu_{j} (\psi_{j}' )_{u} = 0,$$
and
$$\sum_{i=1}^{m}  \lambda_{i} (u)\phi_{i} (u) = 0,\lambda_{i}  \ge 0,i = 1, \dots  , m.$$
Equivalently, in terms of gradients, the above conditions are expressed as
$$\nabla J_{u} + \sum_{i=1}^{m}  \lambda_{i} \nabla (\phi_{i} )_{u} + \sum_{j=1}^{p}  \nu_{j} \nabla (\psi_{j} )_{u} = 0$$
and
$$\sum_{i=1}^{m}  \lambda_{i} (u)\phi_{i} (u) = 0,\lambda_{i}  \ge 0,i = 1, \dots  , m.$$
$(2)$ Conversely, if the restriction of $J$ to $U$ is convex and if there exist vectors $\lambda  \in \mathbb{R}_{+}^{m}$ and
$$\mathbb{R}^{p}$$
$\nu  \in$ such that the KKT conditions hold, then the function $J$ has a (global) minimum at $u$ with respect to $U$. The Lagrangian L(v, $\lambda , \nu$ ) of Problem (P' ) is defined as
$$L(v, \mu , \nu ) = J(v) + \sum_{i=1}^{m}  \mu_{i} \phi_{i} (v) + \sum_{j=1}^{p}  \nu_{i} \psi_{j} (v),$$
where $v \in \Omega , \mu  \in \mathbb{R}_{+}^{m}$, and $\nu  \in \mathbb{R}^{p}$.

<!-- PAGE 1827 -->
$$\mathbb{R}_{+}^{m}\mathbb{R}^{p} \mathbb{R}$$
The function $G:  \times \to$  given by
$$G(\mu , \nu ) = infL(v, \mu , \nu )\mu  \in \mathbb{R}_{+}^{m}, \nu  \in \mathbb{R}^{p}$$
$$v\in \Omega$$
is called the Lagrange dual function (or dual function), and the Dual Problem (D') is
$$maximizeG(\mu , \nu )$$
$$subject to \mu  \in \mathbb{R}_{+}^{m}, \nu  \in \mathbb{R}^{p}.$$
Observe that the Lagrange multipliers $\nu$  are not restricted to be nonnegative. Theorem 50.15 and Theorem 50.17 are immediately generalized to Problem (P' ). We only state the new version of 50.17, leaving the new version of Theorem 50.15 as an exercise.

> **Theorem 50.19.** Consider the minimization problem (P' ):
$$minimizeJ(v)$$
$$subject to \phi_{i} (v) \le 0,i = 1, \dots  , m$$
$$\psi_{j} (v) = 0,j = 1, \dots  , p.$$
where the functions $J, \phi_{i}$  are defined on some open subset $\Omega$ of a finite-dimensional Euclidean vector space $V$ (more generally, a real Hilbert space $V$ ), and the functions $\psi_{j}$  are affine.
$(1)$ Suppose the functions $\phi_{i}$  : $\Omega \to \mathbb{R}$ are continuous, and that for every $\mu  \in \mathbb{R}_{+}^{m}$ and every $\nu  \in \mathbb{R}^{p}$, the Problem $(P_{\mu ,\nu})$:
$$minimizeL(v, \mu , \nu )$$
$$subject to v \in \Omega ,$$
has a unique solution $u_{\mu ,\nu}$, so that
$$L(u_{\mu ,\nu}, \mu , \nu ) = infL(v, \mu , \nu ) = G(\mu , \nu ),$$
$$v\in \Omega$$
and the function $(\mu , \nu$ ) $\mapsto u_{\mu ,\nu}$ is continuous (on $\mathbb{R}_{+}^{m} \times \mathbb{R}^{p})$. Then the function $G$ is differentiable for all $\mu  \in \mathbb{R}_{+}^{m}$ and all $\nu  \in \mathbb{R}^{p}$, and
$$\mathbb{R}^{m} \mathbb{R}^{p}$$
$$G_{\mu ,\nu}'(\xi , \zeta ) = \sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu ,\nu}) + \sum_{j=1}^{p}  \zeta_{j} \psi_{j} (u_{\mu ,\nu})for all \xi  \in and all \zeta  \in .$$
If $(\lambda , \eta$ ) is any solution of Problem $(D)$:
$$maximizeG(\mu , \nu )$$
$$subject to \mu  \in \mathbb{R}_{+}^{m}, \nu  \in \mathbb{R}^{p},$$
then the solution $u_{\lambda ,\eta}$ of the corresponding Problem $(P_{\lambda ,\eta})$ is a solution of Problem (P' ).
