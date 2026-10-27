# Generalization of the Lagrangian Framework


<!-- PAGE 1897 -->

## 51.6 Generalization of the Lagrangian Framework

Essentially all the results presented in Section 50.3, Section 50.7, Section 50.8, and Section 50.9 about Lagrangians and Lagrangian duality generalize to programs involving a proper and convex objective function $J$, proper and convex inequality constraints, and affine equality constraints. The extra generality is that it is no longer assumed that these functions are differentiable. This theory is thoroughly discussed in Part VI, Section $28$, of Rockafellar $[143]$, for programs called ordinary convex programs. We do not have the space to even sketch this theory but we will spell out some of the key results.
$$\mathbb{R}^{n} \mathbb{R}$$
We will be dealing with programs consisting of an objective function $J$ : $\to \cup {+\infty$ } which is convex and proper, subject to $m \ge 0$ inequality contraints $\phi_{i} (v) \le 0$, and $p \ge 0$ affine equality constraints $\psi_{j} (v) = 0$. The constraint functions $\phi_{i}$  are also convex and proper, and we assume that
$$relint(dom(J)) \subseteq relint(dom(\phi_{i} )),dom(J) \subseteq dom(\phi_{i} ),i = 1, \dots  , m.$$
Such programs are called ordinary convex programs. Let
$$\mathbb{R}^{n}$$
$$U = dom(J) \cap {v \in | \phi_{i} (v) \le 0, \psi_{j} (v) = 0, 1 \le i \le m, 1 \le j \le p},$$
be the set of feasible solutions. We are seeking elements in $u \in U$ that minimize $J$ over $U$. A generalized version of Theorem 50.18 holds under the above hypotheses on $J$ and the constraints $\phi_{i}$  and $\psi_{j}$ , except that in the KKT conditions, the equation involving gradients must be replaced by the following condition involving subdifferentials:
$$!$$
$$0 \in \partial J + \sum_{i=1}^{m}  \lambda_{i} \phi_{i}  + \sum_{j=1}^{p}  \mu_{j} \psi_{j} (u),$$
with $\lambda_{i}  \ge 0$ for $i = 1, \dots  , m$ and $\mu_{j}  \in \mathbb{R}$ for $j = 1, \dots  , p$ (where $u \in U$ and $J$ attains its minimum at $u)$. The Lagrangian L(v, $\lambda , \nu$ ) of our problem is defined as follows: Let
$$\mathbb{R}^{m+p}$$
$$E_{m} = {x \in | x_{i} \ge 0, 1 \le i \le m}.$$
Then
$$J(v) + \sum_{i}  m=1 \lambda_{i} \phi_{i} (v) + \sum  pj=1 \mu_{j} \psi_{j} (v)if (\lambda , \mu ) \in E_{m}, v \in dom(J)$$
$$$$
L(v, $\lambda , \mu$ ) $= -\infty$ if $(\lambda , \mu$ ) $\in / E_{m}, v \in$ dom(J)
$$+\infty if v \in /dom(J).$$
$$$$
$$\mathbb{R}_{+}^{m}\mathbb{R}^{p} \mathbb{R}^{n} \mathbb{R}$$
For fixed values $(\lambda , \mu$ ) $\in  \times$ , we also define the function $h: \to  \cup {+\infty$ } given by
$$h(x) = J(x) + \sum_{i=1}^{m}  \lambda_{i} \phi_{i} (x) + \sum_{j=1}^{p}  \mu_{j} \psi_{j} (x),$$

<!-- PAGE 1898 -->
whose effective domain is dom(J) (since we are assuming that dom(J) $\subseteq dom(\phi_{i}$ ), $i = 1, \dots  , m)$. Thus h(x) $=$ L(x, $\lambda , \mu$ ), but $h$ is a function only of $x$, so we denote it differently to avoid confusion (also, technically, L(x, $\lambda , \mu$ ) may take the value $-\infty$ , but $h$ does not). Since $J$ and the $\phi_{i}$  are proper convex functions and the $\psi_{j}$  are affine, the function $h$ is a proper convex function. A proof of a generalized version of Theorem 50.18 can be obtained by putting together Theorem 28.1, Theorem 28.2, and Theorem 28.3, in Rockafellar $[143]$. For the sake of completeness, we state these theorems. Here is Theorem 28.1.

> **Theorem 51.39.** (Theorem 28.1, Rockafellar) Let $(P)$ be an ordinary convex program. Let
$$\mathbb{R}_{+}^{m}\mathbb{R}^{p}$$
$(\lambda , \mu$ ) $\in  \times$ be Lagrange multipliers such that the infimum of the function $h = J + m  \lambda_{i} \phi_{i}  + p  \mu_{j} \psi_{j}$ is finite and equal to the optimal value of $J$ over $U$. Let $D$ be the
$$\sum_{i}  minimal=1 set \sum  of^{j=1} over \mathbb{R}^{n} , and let { \in {} |}. Ifis the subset of$$
$$h I =i1, \dots  , m \lambda_{i}  = 0 D_{0}  D$$
consisting of vectors $x$ such that
$$\phi_{i} (x) \le 0for all i \in I$$
$$\phi_{i} (x) = 0for all i \in /I$$
$$\psi_{j} (x) = 0for all j = 1, \dots  , p,$$
then $D_{0}$ is the set of minimizers of $(P)$ over $U$. And now here is Theorem 28.2.

> **Theorem 51.40.** (Theorem 28.2, Rockafellar) Let $(P)$ be an ordinary convex program, and let $I \subseteq {1, \dots  , m}$ be the subset of indices of inequality constraints that are not affine. Assume that the optimal value of $(P)$ is finite, and that $(P)$ has at least one feasible solution $x \in$ relint(dom(J)) such that
$$\phi_{i} (x) < 0for all i \in I.$$
$$\mathbb{R}_{+}^{m}\mathbb{R}^{p}$$
Then there exist some Lagrange multipliers $(\lambda , \mu$ ) $\in  \times$ (not necessarily unique) such that
(a) The infimum of the function $h = J + m  \lambda_{i} \phi_{i}  + p  \mu_{j} \psi_{j}$ is finite and equal to the
$$optimal value of over. \sum_{i}  =1 \sum  j=1$$
$$J U$$
The hypotheses of Theorem 51.40 are qualification conditions on the constraints, essentially Slater’s conditions from Definition 50.6.

> **Definition 51.21.** Let $(P)$ be an ordinary convex program, and let $I \subseteq {1, \dots  , m}$ be the subset of indices of inequality constraints that are not affine. The constraints are qualified is there is a feasible solution $x \in$ relint(dom(J)) such that
$$\phi_{i} (x) < 0for all i \in I.$$
Finally, here is Theorem 28.3 from Rockafellar $[143]$.

<!-- PAGE 1899 -->

> **Theorem 51.41.** (Theorem 28.3, Rockafellar) Let $(P)$ be an ordinary convex program. If $\mathbb{R}^{n} \mathbb{R}_{+}^{m} \mathbb{R}^{p} x \in$ and $(\lambda , \mu$ ) $\in  \times$ , then $(\lambda , \mu$ ) and $x$ have the property that
(a) The infimum of the function $h = J + m  \lambda_{i} \phi_{i}  + p  \mu_{j} \psi_{j}$ is finite and equal to the
$$optimal value of over, and \sum_{i}  =1 \sum  j=1$$
$$J U$$
$(b)$ The vector $x$ is an optimal solution of $(P)$ (so $x \in U)$, iff $(x, \lambda , \mu$ ) is a saddle point of the Lagrangian L(x, $\lambda , \mu$ ) of $(P)$. Moreover, this condition holds iff the following KKT conditions hold:
$(1) \lambda  \in \mathbb{R}_{+}^{m}, \phi_{i} (x) \le 0$, and $\lambda_{i} \phi_{i} (x) = 0$ for $i = 1, \dots  , m$.
$(2) \psi_{j} (x) = 0$ for $j = 1, \dots  , p$.
$$(3) 0 \in \partial J(x) + \sum_{i}  m=1 \lambda_{i} \partial \phi_{i} (x) + \sum  pj=1 \mu_{j} \partial \psi_{j} (x).$$
Observe that by Theorem 51.40, if the optimal value of $(P)$ is finite and if the constraints are qualified, then Condition (a) of Theorem 51.41 holds for $(\lambda , \mu$ ). As a consequence we obtain the following corollary of Theorem 51.41 attributed to Kuhn and Tucker, which is one of the main results of the theory. It is a generalized version of Theorem 50.18.

> **Theorem 51.42.** (Theorem 28.3.1, Rockafellar) Let $(P)$ be an ordinary convex program satisfying the hypothesis of Theorem 51.40, which means that the optimal value of $(P)$ is
$$\mathbb{R}^{n}$$
finite, and that the constraints are qualified. In order that a vector $x \in$ be an optimal solution to $(P)$, it is necessary and sufficient that there exist Lagrange multipliers $(\lambda , \mu$ ) $\in \mathbb{R}_{+}^{m} \mathbb{R}^{p} \times$ such that $(x, \lambda , \mu$ ) is a saddle point of L(x, $\lambda , \mu$ ). Equivalently, $x$ is an optimal solution of $(P)$ if and only if there exist Lagrange multipliers $(\lambda , \mu$ ) $\in \mathbb{R}_{+}^{m} \times  \mathbb{R}^{p}$, which, together with $x$, satisfy the KKT conditions from Theorem 51.41. Theorem 51.42 has to do with the existence of an optimal solution for $(P)$, but it does not say anything about the optimal value of $(P)$. To establish such a result, we need the notion of dual function. The dual function $G$ is defined by
$$G(\lambda , \mu ) = \inf L(v, \lambda , \mu ).$$
$$v\in \mathbb{R} n$$
It is a concave function (so $-G$ is convex) which may take the values $\pm \infty$ . Note that maximizing $G$, which is equivalent to minimizing $-G$, runs into troubles if $G(\lambda , \mu$ ) $= +\infty$ for some $\lambda , \mu$ , but that $G(\lambda , \mu$ ) $= -\infty$ does not cause a problem. At first glance, this seems counterintuitive, but remember that $G$ is concave, not convex. It is $-G$ that is convex, and $-\infty$ and $+\infty$ get flipped. Then a generalized and stronger version of Theorem 50.19(2) also holds. A proof can be obtained by putting together Corollary 28.3.1, Theorem 28.4, and Corollary 28.4.1, in Rockafellar $[143]$. For the sake of completeness, we state the following results from Rockafellar $[143]$.
