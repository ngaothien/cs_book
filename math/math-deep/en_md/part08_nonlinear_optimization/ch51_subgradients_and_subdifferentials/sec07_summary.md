# Summary


<!-- PAGE 1900 -->

> **Theorem 51.43.** (Theorem 28.4, Rockafellar) Let $(P)$ be an ordinary convex program with
$$\mathbb{R}_{+}^{m}\mathbb{R}^{p} \mathbb{R}^{n}$$
Lagrangian L(x, $\lambda , \mu$ ). If the Lagrange multipliers $(\lambda^{*} , \mu^{*}$ ) $\in  \times$ and the vector $x^{*} \in$ have the property that
(a) The infimum of the function $h = J + m  \lambda_{i}^{*}  \phi_{i}  + p  \mu_{j}^{*} \psi_{j}$ is finite and equal to the
$$optimal value of over, and \sum_{i}  =1 \sum  j=1$$
$$J U$$
$(b)$ The vector $x^{*}$ is an optimal solution of $(P)$ (so $x^{*} \in U)$, then the saddle value $L(x^{*}, \lambda^{*} , \mu^{*}$ ) is the optimal value $J(x^{*})$ of $(P)$.
$$\mathbb{R}_{+}^{m}\mathbb{R}^{p}$$
More generally, the Lagrange multipliers $(\lambda^{*} , \mu^{*}$ ) $\in  \times$ have Property (a) iff
$$-\infty < \inf L(x, \lambda^{*} , \mu^{*} ) \le supinf L(x, \lambda , \mu ) = \inf supL(x, \lambda , \mu ),$$
$$x\lambda ,\mu xx\lambda ,\mu$$
in which case, the common value of the extremum value is the optimal value of $(P)$. In particular, if $x^{*}$ is an optimal solution for $(P)$, then $sup_{\lambda ,\mu} G(\lambda , \mu$ ) $= L(x^{*}, \lambda^{*} , \mu^{*}$ ) $= J(x^{*})$ (zero duality gap). Observe that Theorem 51.43 gives sufficient Conditions (a) and $(b)$ for the duality gap to be zero. In view of Theorem 51.41, these conditions are equivalent to the fact that $(x^{*}, \lambda^{*} , \mu^{*}$ ) is a saddle point of $L$, or equivalently that the KKT conditions hold. Again, by Theorem 51.40, if the optimal value of $(P)$ is finite and if the constraints are qualified, then Condition (a) of Theorem 51.43 holds for $(\lambda , \mu$ ). Then the following corollary of Theorem 51.43 holds.

> **Theorem 51.44.** (Theorem 28.4.1, Rockafellar) Let $(P)$ be an ordinary convex program satisfying the hypothesis of Theorem 51.40, which means that the optimal value of $(P)$ is
$$\mathbb{R}_{+}^{m}\mathbb{R}^{p}$$
finite, and that the constraints are qualified. The Lagrange multipliers $(\lambda , \mu$ ) $\in  \times$ that have the property that the infimum of the function $h = J + m  \lambda_{i} \phi_{i}  + p  \mu_{j} \psi_{j}$ is finite
$$and equal to the optimal value of over are exactly the vectors \sum_{i}  =1 where the^{j=1} \sum  dual function$$
$$J U G$$
attains is supremum over $\mathbb{R}^{n}$. Theorem 51.44 is a generalized and stronger version of Theorem 50.19(2). Part $(1)$ of Theorem 50.19 requires $J$ and the $\phi_{i}$  to be differentiable, so it does not generalize. More results can shown about ordinary convex programs, and another class of programs called generalized convex programs. However, we do not need such resuts for our purposes, in particular to discuss the ADMM method. The interested reader is referred to Rockafellar $[143]$ (Part VI, Sections $28$ and $29)$.

## 51.7 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Extended real-valued functions.

<!-- PAGE 1901 -->
$\bullet$  Epigraph (epi(f)). $\bullet$  Convex and concave (extended real-valued) functions. $\bullet$  Effective domain (dom(f)). $\bullet$  Proper and improper convex functions. $\bullet$  Sublevel sets. $\bullet$  Lower semi-continuous functions. $\bullet$  Lower semi-continuous hull; closure of a convex function. $\bullet$  Relative interior (relint(C)). $\bullet$  Indicator function. $\bullet$  Lipschitz condition. $\bullet$  Affine form, affine hyperplane. $\bullet$  Half spaces. $\bullet$  Supporting hyperplane. $\bullet$  Normal cone at $a. \bullet$  Subgradient, subgradient inequality, subdifferential. $\bullet$  Minkowski’s supporting hyperplane theorem. $\bullet$  One-sided directional derivative. $\bullet$  Support function. $\bullet$  ReLU function. $\bullet  \epsilon$ -subgradient. $\bullet$  Minimum set of a convex function. $\bullet$  Direction of recession. $\bullet$  Ordinary convex programs. $\bullet$  Set of feasible solutions. $\bullet$  Lagrangian.
