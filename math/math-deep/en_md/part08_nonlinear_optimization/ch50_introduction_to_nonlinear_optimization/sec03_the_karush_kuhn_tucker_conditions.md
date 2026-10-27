# The Karush–Kuhn–Tucker Conditions


<!-- PAGE 1778 -->
$$(\varphi ‘)\le 0$$
$$1u$$
$$u$$
$$1$$
$$u$$
$$2$$
$$\delta w$$
$$u3v$$
$$uk$$
$$u$$
$$v$$
$$(i.)$$
$$w$$
$$(\varphi ‘)\le 0$$
$$1u$$
$$\delta w$$
$$v$$
$$u$$
$$v(ii.)$$
$$w$$

![Figure 50.10](../../assets/ch50/fig_50_10.png)

**Figure 50.10:** Let $U$ be the pink lounge in $\mathbb{R}^{2}$. Let $u$ satisfy the non-affine constraint $\phi_{1} (u)$. Choose vectors $v$ and $w$ in the half space $(\phi_{1}' )_{u} \le 0$. Figure $(i.)$ approaches $u$ along the line $u + t(\delta w + v)$ and shows that $v + \delta w \in$ C(u) for fixed $\delta$ . Figure (ii.) varies $\delta$  in order that the purple vectors approach $v$ as $\delta  \to \infty$ .

## 50.3 The Karush–Kuhn–Tucker Conditions

If the domain $U$ is defined by inequality constraints satisfying mild differentiability conditions and if the constraints at $u$ are qualified, then there is a necessary condition for the function $J$ to have a local minimum at $u \in U$ involving generalized Lagrange multipliers. The proof uses a version of Farkas lemma. In fact, the necessary condition stated next holds for infinite-dimensional vector spaces because there a version of Farkas lemma holding for real Hilbert spaces, but we will content ourselves with the version holding for finite dimensional normed vector spaces. For the more general version, see Theorem 48.12 (or Ciarlet $[41]$, Chapter $9)$. We will be using the following version of Farkas lemma.

> **Proposition 50.3.** (Farkas Lemma, Version I) Let $A$ be a real $m\times n$ matrix and let $b \in \mathbb{R}^{m}$ be any vector. The linear system Ax $= b$ has no solution $x \ge 0$ iff there is some nonzero

<!-- PAGE 1779 -->
linear form $y \in (\mathbb{R}^{m})^{*}$ such that yA $\ge 0_{n}^{\top}$ and yb $< 0$. We will use the version of Farkas lemma obtained by taking a contrapositive, namely: if yA $\ge 0_{n}^{\top}$ implies yb $\ge 0$ for all linear forms $y \in (\mathbb{R}^{m})^{*}$, then the linear system Ax $= b$ has some solution $x \ge 0$. Actually, it is more convenient to use a version of Farkas lemma applying to a Euclidean vector space (with an inner product denoted $\langle$ -, $-\rangle$ ). This version also applies to an infinite dimensional real Hilbert space; see Theorem 48.12. Recall that in a Euclidean space $V$ the inner product induces an isomorphism between $V$ and V' , the space of continuous linear forms on $V$ . In our case, we need the isomorphism $\sharp$ from V' to $V$ defined such that for every linear form $\omega  \in$ V' , the vector $\omega^{\sharp} \in V$ is uniquely defined by the equation
$$\omega (v) = \langle v, \omega^{\sharp} \rangle for all v \in V .$$
$\mathbb{R}^{n}  \mathbb{R}^{n} \mathbb{R}^{n} \mathbb{R}^{n}$ In , the isomorphism between and ( $)^{*}$ amounts to transposition: if $y \in$ ( $)^{*}$ is
$$\mathbb{R}^{n}$$
a linear form and $v \in$ is a vector, then
$$yv = v^{\top}y^{\top}.$$
The version of the Farkas–Minskowski lemma in term of an inner product is as follows.

> **Proposition 50.4.** (Farkas–Minkowski) Let $V$ be a Euclidean space of finite dimension with inner product $\langle$ -, $-\rangle$ (more generally, a Hilbert space). For any finite family $(a_{1}, \dots  , a_{m})$ of $m$ vectors $a_{i} \in V$ and any vector $b \in V$ , for any $v \in V$ ,
$$if \langle a_{i}, v\rangle \ge 0 for i = 1, \dots  , m implies that \langle b, v\rangle \ge 0,$$
then there exist $\lambda_{1} , \dots  , \lambda_{m}  \in \mathbb{R}$ such that
$$\lambda_{i}  \ge 0 for i = 1, \dots  , m, and b = \sum_{i=1}^{m}  \lambda_{i} a_{i},$$
that is, $b$ belong to the polyhedral cone $cone(a_{1}, \dots  , a_{m})$. Proposition 50.4 is the special case of Theorem 48.12 which holds for real Hilbert spaces. We can now prove the following theorem.

> **Theorem 50.5.** Let $\phi_{i}$  : $\Omega \to \mathbb{R}$ be $m$ constraints defined on some open subset $\Omega$ of a finite-dimensional Euclidean vector space $V$ (more generally, a real Hilbert space $V$ ), let $J$ : $\Omega \to \mathbb{R}$ be some function, and let $U$ be given by
$$U = {x \in \Omega | \phi_{i} (x) \le 0, 1 \le i \le m}.$$
For any $u \in U$, let
$$I(u) = {i \in {1, \dots  , m} | \phi_{i} (u) = 0},$$

<!-- PAGE 1780 -->
and assume that the functions $\phi_{i}$  are differentiable at $u$ for all $i \in$ I(u) and continuous at $u$ for all $i \in /$ I(u). If $J$ is differentiable at $u$, has a local minimum at $u$ with respect to $U$, and if the constraints are qualified at $u$, then there exist some scalars $\lambda_{i} (u) \in \mathbb{R}$ for all $i \in$ I(u), such that
$$J_{u}' + \sum_{i\in I(u)}  \lambda_{i} (u)(\phi_{i}' )_{u} = 0,and\lambda_{i} (u) \ge 0 for all i \in I(u).$$
The above conditions are called the Karush–Kuhn–Tucker optimality conditions. Equivalently, in terms of gradients, the above conditions are expressed as
$$\nabla J_{u} + \sum_{i\in I(u)}  \lambda_{i} (u)\nabla (\phi_{i} )_{u} = 0,and\lambda_{i} (u) \ge 0 for all i \in I(u).$$

*Proof.* By Proposition 50.1(2), we have
$$J_{u}'(w) \ge 0for all w \in C(u),(*_{1})$$
and by Proposition 50.2(2), we have C(u) $= C^{*}(u)$, where
$$C^{*}(u) = {v \in V | (\phi_{i}' )_{u}(v) \le 0, i \in I(u)},(*_{2})$$
so $(*_{1})$ can be expressed as: for all $w \in V$ ,
$$if w \in C^{*}(u) then J_{u}'(w) \ge 0,$$
or
$$if -(\phi_{i}' )_{u}(w) \ge 0 for all i \in I(u), then J_{u}'(w) \ge 0.(*_{3})$$
Under the isomorphism $\sharp$ , the vector $(J_{u}')^{\sharp}$ is the gradient $\nabla J_{u}$, so that
$$J_{u}'(w) = \langle w, \nabla J_{u}\rangle ,(*_{4})$$
and the vector $((\phi_{i}' )_{u})^{\sharp}$ is the gradient $\nabla (\phi_{i} )_{u}$, so that
$$(\phi_{i}' )_{u}(w) = \langle w, \nabla (\phi_{i} )_{u}\rangle .(*_{5})$$
Using Equations $(*_{4})$ and $(*_{5})$, Equation $(*_{3})$ can be written as: for all $w \in V$ ,
$$if \langle w, -\nabla (\phi_{i} )_{u}\rangle \ge 0 for all i \in I(u), then \langle w, \nabla J_{u}\rangle \ge 0.(*_{6})$$
By the Farkas–Minkowski proposition (Proposition 50.4), there exist some sacalars $\lambda_{i} (u)$ for all $i \in$ I(u), such that $\lambda_{i} (u) \ge 0$ and
$$\nabla J_{u} = \sum_{i\in I(u)}  \lambda_{i} (u)(-\nabla (\phi_{i} )_{u}),$$
that is
$$\nabla J_{u} + \sum_{i\in I(u)}  \lambda_{i} (u)\nabla (\phi_{i} )_{u} = 0,$$

<!-- PAGE 1781 -->
and using the inverse of the isomorphism $\sharp$ (which is linear), we get
$$J_{u}' + \sum_{i\in I(u)}  \lambda_{i} (u)(\phi_{i}' )_{u} = 0,$$
as claimed. Since the constraints are inequalities of the form $\phi_{i} (x) \le 0$, there is a way of expressing the Karush–Kuhn–Tucker optimality conditions, often abbreviated as KKT conditions, in a way that does not refer explicitly to the index set I(u):
$$J_{u}' + \sum_{i=1}^{m}  \lambda_{i} (u)(\phi_{i}' )_{u} = 0,(KKT_{1})$$
and
$$\sum_{i=1}^{m}  \lambda_{i} (u)\phi_{i} (u) = 0,\lambda_{i} (u) \ge 0,i = 1, \dots  , m.(KKT_{2})$$
Indeed, if we have the strict inequality $\phi_{i} (u) < 0$ (the constraint $\phi_{i}$  is inactive at $u)$, since all the terms $\lambda_{i} (u)\phi_{i} (u)$ are nonpositive, we must have $\lambda_{i} (u) = 0$; that is, we only need to consider the $\lambda_{i} (u)$ for all $i \in$ I(u). Yet another way to express the conditions in $(KKT_{2})$ is
$$\lambda_{i} (u)\phi_{i} (u) = 0,\lambda_{i} (u) \ge 0,i = 1, \dots  , m.(KKT_{2}')$$
In other words, for any $i \in {1, \dots  , m}$, if $\phi_{i} (u) < 0$, then $\lambda_{i} (u) = 0$; that is, $\bullet$  if the constraint $\phi_{i}$  is inactive at $u$, then $\lambda_{i} (u) = 0$. By contrapositive, if $\lambda_{i} (u) \neq  0$, then $\phi_{i} (u) = 0$; that is, $\bullet$  if $\lambda_{i} (u) \neq  0$, then the constraint $\phi_{i}$  is active at $u$. The conditions in $(KKT_{2}')$ are referred to as complementary slackness conditions. The scalars $\lambda_{i} (u)$ are often called generalized Lagrange multipliers. If $V = \mathbb{R}^{n}$, the necessary conditions of Theorem 50.5 are expressed as the following system of equations and
$$\mathbb{R}^{n} \mathbb{R}_{+}^{m}$$
inequalities in the unknowns $(u_{1}, \dots  , u_{n}) \in$ and $(\lambda_{1} , \dots  , \lambda_{m}$ ) $\in$ :
$$\frac{\partial J}{\partial x_{1}} (u) + \lambda_{1} \frac{\partial \phi_{1}}{\partial x_{1}} (u) + \cdots  + \lambda_{m} \frac{\partial \phi_{m}}{\partial x_{1}} (u) = 0$$
$$\vdots \vdots$$
$$\frac{\partial J}{\partial x_{n}} (u) + \lambda_{1} \frac{\partial \phi_{1}}{\partial x_{n}} (u) + \cdots  + \lambda_{m} \frac{\partial \phi_{m}}{\partial x_{n}} (u) = 0$$
$$\lambda_{1} \phi_{1} (u) + \cdots  + \lambda_{m} \phi_{m} (u) = 0$$
$$\phi_{1} (u) \le 0$$
$$\vdots \vdots$$
$$\phi_{m} (u) \le 0$$
$$\lambda_{1} , \dots  , \lambda_{m}  \ge 0.$$

<!-- PAGE 1782 -->

> **Example 50.3.** Let $J, \phi_{1}$  and $\phi_{2}$  be the functions defined on $\mathbb{R}$ by
$$J(x) = x$$
$$\phi_{1} (x) = -x$$
$$\phi_{2} (x) = x -1.$$
In this case
$$U = {x \in \mathbb{R} | -x \le 0, x -1 \le 0} = [0, 1].$$
Since the constraints are affine, they are automatically qualified for any $u \in [0, 1]$. The system of equations and inequalities shown above becomes
$$1 -\lambda_{1}  + \lambda_{2}  = 0$$
$$-\lambda_{1} x + \lambda_{2} (x -1) = 0$$
$$-x \le 0$$
$$x -1 \le 0$$
$$\lambda_{1} , \lambda_{2}  \ge 0.$$
The first equality implies that $\lambda_{1}  = 1 + \lambda_{2}$ . The second equality then becomes
$$-(1 + \lambda_{2} )x + \lambda_{2} (x -1) = 0,$$
which implies that $\lambda_{2}  = -x$. Since $0 \le x \le 1$, or equivalently $-1 \le -x \le 0$, and $\lambda_{2}  \ge 0$, we conclude that $\lambda_{2}  = 0$ and $\lambda_{1}  = 1$ is the solution associated with $x = 0$, the minimum of J(x) $= x$ over $[0, 1]$. Observe that the case $x = 1$ corresponds to the maximum and not a minimum of J(x) $= x$ over $[0, 1]$.
Remark: Unless the linear forms $(\phi_{i}' )_{u}$ for $i \in$ I(u) are linearly independent, the $\lambda_{i} (u)$ are generally not unique. Also, if I(u) $= \emptyset$ , then the KKT conditions reduce to $J_{u}' = 0$. This is not surprising because in this case $u$ belongs to the relative interior of $U$. If the constraints are all affine equality constraints, then the KKT conditions are a bit simpler. We will consider this case shortly. The conditions for the qualification of nonaffine constraints are hard (if not impossible) to use in practice, because they depend on $u \in U$ and on the derivatives $(\phi_{i}' )_{u}$. Thus it is desirable to find simpler conditions. Fortunately, this is possible if the nonaffine functions $\phi_{i}$  are convex.

> **Definition 50.6.** Let $U \subseteq \Omega \subseteq V$ be given by
$$U = {x \in \Omega | \phi_{i} (x) \le 0, 1 \le i \le m},$$
where $\Omega$ is an open subset of the Euclidean vector space $V$ . If the functions $\phi_{i}$  : $\Omega \to \mathbb{R}$ are convex, we say that the constraints are qualified if the following conditions hold:

<!-- PAGE 1783 -->
(a) Either the constraints $\phi_{i}$  are affine for all $i = 1, \dots  , m$ and $U \neq  \emptyset$ , or
$(b)$ There is some vector $v \in \Omega$ such that the following conditions hold for $i = 1, \dots  , m$:
$$(i) \phi_{i} (v) \le 0.$$
$$(ii) If \phi_{i}  is not affine, then \phi_{i} (v) < 0.$$
The above qualification conditions are known as Slater’s conditions. Condition (b)(i) also implies that $U$ has nonempty relative interior. If $\Omega$ is convex, then $U$ is also convex. This is because for all $u, v \in \Omega$ , if $u \in U$ and $v \in U$, that is $\phi_{i} (u) \le 0$ and $\phi_{i} (v) \le 0$ for $i = 1, \dots  , m$, since the functions $\phi_{i}$  are convex, for all $\theta  \in [0, 1]$ we have $\phi_{i} ((1$ - $\theta )u + \theta v) \le (1$ - $\theta )\phi_{i} (u) + \theta \phi_{i} (v)$ since $\phi_{i}$  is convex
$$\le 0since 1 -\theta  \ge 0, \theta  \ge 0, \phi_{i} (u) \le 0, \phi_{i} (v) \le 0,$$
and any intersection of convex sets is convex.  It is important to observe that a nonaffine equality constraint $\phi_{i} (u) = 0$ is never qualified. Indeed, $\phi_{i} (u) = 0$ is equivalent to $\phi_{i} (u) \le 0$ and $-\phi_{i} (u) \le 0$, so if these constraints are qualified and if $\phi_{i}$  is not affine then there is some nonzero vector $v \in \Omega$ such that both $\phi_{i} (v) < 0$ and $-\phi_{i} (v) < 0$, which is impossible. For this reason, equality constraints are often assumed to be affine. The following theorem yields a more flexible version of Theorem 50.5 for constraints given by convex functions. If in addition, the function $J$ is also convex, then the KKT conditions are also a sufficient condition for a local minimum.

> **Theorem 50.6.** Let $\phi_{i}$  : $\Omega \to \mathbb{R}$ be $m$ convex constraints defined on some open convex subset $\Omega$ of a finite-dimensional Euclidean vector space $V$ (more generally, a real Hilbert space $V$ ), let $J$ : $\Omega \to \mathbb{R}$ be some function, let $U$ be given by
$$U = {x \in \Omega | \phi_{i} (x) \le 0, 1 \le i \le m},$$
and let $u \in U$ be any point such that the functions $\phi_{i}$  and $J$ are differentiable at $u$.
$(1)$ If $J$ has a local minimum at $u$ with respect to $U$, and if the constraints are qualified, then there exist some scalars $\lambda_{i} (u) \in \mathbb{R}$, such that the KKT condition hold:
$$J_{u}' + \sum_{i=1}^{m}  \lambda_{i} (u)(\phi_{i}' )_{u} = 0$$
and
$$\lambda_{i} (u)\phi_{i} (u) = 0,\lambda_{i} (u) \ge 0,i = 1, \dots  , m.$$

<!-- PAGE 1784 -->
Equivalently, in terms of gradients, the above conditions are expressed as
$$\nabla J_{u} + \sum_{i=1}^{m}  \lambda_{i} (u)\nabla (\phi_{i} )_{u} = 0,$$
and
$$\lambda_{i} (u)\phi_{i} (u) = 0,\lambda_{i} (u) \ge 0,i = 1, \dots  , m.$$
Furthermore, the $m$ conditions
$$\lambda_{i} (u)\phi_{i} (u) = 0,\lambda_{i} (u) \ge 0,i = 1, \dots  , m,$$
are equivalent to the conditions
$$\sum_{i=1}^{m}  \lambda_{i} (u)\phi_{i} (u) = 0and\lambda_{i} (u) \ge 0,i = 1, \dots  , m.$$
$(2)$ Conversely, if the restriction of $J$ to $U$ is convex and if there exist scalars $(\lambda_{1} , \dots  , \lambda_{m}$ ) $\in \mathbb{R}_{+}^{m}$ such that the KKT conditions hold, then the function $J$ has a (global) minimum at $u$ with respect to $U$.

*Proof.* $(1)$ It suffices to prove that if the convex constraints are qualified according to Definition 50.6, then they are qualified according to Definition 50.5, since in this case we can apply Theorem 50.5. If $v \in \Omega$ is a vector such that Condition $(b)$ of Definition 50.6 holds and if $v \neq  u$, for any $i \in$ I(u), since $\phi_{i} (u) = 0$ and since $\phi_{i}$  is convex, by Proposition 40.11(1),
$$\phi_{i} (v) \ge \phi_{i} (u) + (\phi_{i}' )_{u}(v -u) = (\phi_{i}' )_{u}(v -u),$$
so if we let $w = v$ - $u$ then
$$(\phi_{i}' )_{u}(w) \le \phi_{i} (v),$$
which shows that the nonaffine constraints $\phi_{i}$  for $i \in$ I(u) are qualified according to Definition 50.5, by Condition $(b)$ of Definition 50.6. If $v = u$, then the constraints $\phi_{i}$  for which $\phi_{i} (u) = 0$ must be affine (otherwise, Condition (b)(ii) of Definition 50.6 would be false), and in this case we can pick $w = 0$.
$(2)$ Let $v$ be any arbitrary point in the convex subset $U$. Since $\phi_{i} (v) \le 0$ and $\lambda_{i}  \ge 0$ for
$$i = 1, \dots  , m, we have \sum_{i}  m=1 \lambda_{i} \phi_{i} (v) \le 0, and using the fact that$$
$$\sum_{i=1}^{m}  \lambda_{i} (u)\phi_{i} (u) = 0,\lambda_{i} (u) \ge 0,i = 1, \dots  , m,$$

<!-- PAGE 1785 -->
we have $\lambda_{i}  = 0$ if $i \in /$ I(u) and $\phi_{i} (u) = 0$ if $i \in$ I(u), so we have
$$J(u) \le J(u) - \sum_{i=1}^{m}  \lambda_{i} \phi_{i} (v)$$
$$\le J(u) - \sum_{i\in I(u)}  \lambda_{i} (\phi_{i} (v) -\phi_{i} (u))\lambda_{i}  = 0 if i \in /I(u), \phi_{i} (u) = 0 if i \in I(u)$$
$$\le J(u) - \sum_{i\in I(u)}  \lambda_{i} (\phi_{i}' )_{u}(v -u)(by Proposition 40.11)(1)$$
$$\le J(u) + J_{u}'(v -u)(by the KKT conditions)$$
$$\le J(v)(by Proposition 40.11)(1),$$
and this shows that $u$ is indeed a (global) minimum of $J$ over $U$. It is important to note that when both the constraints, the domain of definition $\Omega$ , and the objective function $J$ are convex, if the KKT conditions hold for some $u \in U$ and some $\lambda  \in \mathbb{R}_{+}^{m}$, then Theorem 50.6 implies that $J$ has a (global) minimum at $u$ with respect to $U$, independently of any assumption on the qualification of the constraints. The above theorem suggests introducing the function $L: \Omega \times \mathbb{R}_{+}^{m} \to \mathbb{R}$ given by
$$L(v, \lambda ) = J(v) + \sum_{i=1}^{m}  \lambda_{i} \phi_{i} (v),$$
with $\lambda  = (\lambda_{1} , \dots  , \lambda_{m}$ ). The function $L$ is called the Lagrangian of the Minimization Problem $(P)$:
$$minimizeJ(v)$$
$$subject to \phi_{i} (v) \le 0,i = 1, \dots  , m.$$
The KKT conditions of Theorem 50.6 imply that for any $u \in U$, if the vector $\lambda  = (\lambda_{1} , \dots  , \lambda_{m}$ ) is known and if $u$ is a minimum of $J$ on $U$, then
$$\frac{\partial L}{\partial u} (u) = 0$$
$$J(u) = L(u, \lambda ).$$
The Lagrangian technique “absorbs” the constraints into the new objective function $L$ and reduces the problem of finding a constrained minimum of the function $J$, to the problem of finding an unconstrained minimum of the function L(v, $\lambda$ ). This is the main point of Lagrangian duality which will be treated in the next section. A case that arises often in practice is the case where the constraints $\phi_{i}$  are affine. If so, the $m$ constraints $a_{i}x \le b_{i}$ can be expressed in matrix form as Ax $\le b$, where $A$ is an $m \times  n$ matrix whose ith row is the row vector $a_{i}$. The KKT conditions of Theorem 50.6 yield the following corollary.

<!-- PAGE 1786 -->

> **Proposition 50.7.** If $U$ is given by
$$U = {x \in \Omega | Ax \le b},$$
$$\mathbb{R}^{n}$$
where $\Omega$ is an open convex subset of and $A$ is an $m \times  n$ matrix, and if $J$ is differentiable at $u$ and $J$ has a local minimum at $u$, then there exists some vector $\lambda  \in \mathbb{R}^{m}$, such that
$$\nabla J_{u} + A^{\top}\lambda  = 0$$
$$\lambda_{i}  \ge 0 andif a_{i}u < b_{i}, then \lambda_{i}  = 0, i = 1, \dots  , m.$$
If the function $J$ is convex, then the above conditions are also sufficient for $J$ to have a minimum at $u \in U$. Another case of interest is the generalization of the minimization problem involving the affine constraints of a linear program in standard form, that is, equality constraints Ax $= b$ with $x \ge 0$, where $A$ is an $m \times  n$ matrix. In our formalism, this corresponds to the 2m $+ n$ constraints
$$a_{i}x -b_{i} \le 0,i = 1, \dots  , m$$
$$-a_{i}x + b_{i} \le 0,i = 1, \dots  , m$$
$$-x_{j} \le 0,i = 1, \dots  , n.$$
In matrix form, they can be expressed as
$$\begin{pmatrix} A \\ -A \\ I_{n} \end{pmatrix} \begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix} \le \begin{pmatrix} b \\ -b \\ 0_{n} \end{pmatrix} .$$
$$-$$
If we introduce the generalized Lagrange multipliers $\lambda_{i}^{+}$  and $\lambda_{i}^{-}$  for $i = 1, \dots  , m$ and $\mu_{j}$ for $j = 1, \dots  , n$, then the KKT conditions are
$$\nabla J_{u} + \begin{pmatrix} A^{\top} & -A^{\top} & -I_{n} \end{pmatrix} \begin{pmatrix} \lambda^{+} \\ \lambda^{-} \\ \mu \end{pmatrix} = 0_{n},$$
that is,
$$\nabla J_{u} + A^{\top}\lambda^{+} -A^{\top}\lambda^{-} -\mu  = 0,$$
and $\lambda^{+} , \lambda^{-} , \mu  \ge 0$, and if $a_{i}u < b_{i}$, then $\lambda_{i}^{+}  = 0$, if $-a_{i}u < -b_{i}$, then $\lambda_{i}^{-}  = 0$, and if $-u_{j} < 0$, then $\mu_{j}  = 0$. But the constraints $a_{i}u = b_{i}$ hold for $i = 1, \dots  , m$, so this places no restriction on the $\lambda_{i}^{+}$  and $\lambda_{i}^{-}$  , and if we write $\lambda_{i}  = \lambda_{i}^{+}$  - $\lambda_{i}^{-}$  , then we have
$$\nabla J_{u} + A^{\top}\lambda  = \mu ,$$
with $\mu_{j}  \ge 0$, and if $u_{j} > 0$ then $\mu_{j}  = 0$, for $j = 1, \dots  , n$. Thus we proved the following proposition (which is slight generalization of Proposition 8.7.2 in Matousek and Gardner $[127])$.

<!-- PAGE 1787 -->

> **Proposition 50.8.** If $U$ is given by
$$U = {x \in \Omega | Ax = b, x \ge 0},$$
$$\mathbb{R}^{n}$$
where $\Omega$ is an open convex subset of and $A$ is an $m \times  n$ matrix, and if $J$ is differentiable
$$\mathbb{R}^{m} \mathbb{R}^{n}$$
at $u$ and $J$ has a local minimum at $u$, then there exist two vectors $\lambda  \in$ and $\mu  \in$ , such that
$$\nabla J_{u} + A^{\top}\lambda  = \mu ,$$
with $\mu_{j}  \ge 0$, and if $u_{j} > 0$ then $\mu_{j}  = 0$, for $j = 1, \dots  , n$. Equivalently, there exists a vector $\mathbb{R}^{m} \lambda  \in$ such that
$$($$
$$= 0if u_{j} > 0$$
$$(\nabla J_{u})_{j} + (A^{j})^{\top}\lambda$$
$$\ge 0if u_{j} = 0,$$
where $A^{j}$ is the jth column of $A$. If the function $J$ is convex, then the above conditions are also sufficient for $J$ to have a minimum at $u \in U$. Yet another special case that arises frequently in practice is the minimization problem involving the affine equality constraints Ax $= b$, where $A$ is an $m \times  n$ matrix, with no restriction on $x$. Reviewing the proof of Proposition 50.8, we obtain the following proposition.

> **Proposition 50.9.** If $U$ is given by
$$U = {x \in \Omega | Ax = b},$$
$$\mathbb{R}^{n}$$
where $\Omega$ is an open convex subset of and $A$ is an $m \times  n$ matrix, and if $J$ is differentiable
$$\mathbb{R}^{m}$$
at $u$ and $J$ has a local minimum at $u$, then there exists some vector $\lambda  \in$ such that
$$\nabla J_{u} + A^{\top}\lambda  = 0.$$
$$\mathbb{R}^{m}$$
Equivalently, there exists a vector $\lambda  \in$ such that
$$(\nabla J_{u})_{j} + (A^{j})^{\top}\lambda  = 0,$$
where $A^{j}$ is the jth column of $A$. If the function $J$ is convex, then the above conditions are also sufficient for $J$ to have a minimum at $u \in U$. Observe that in Proposition 50.9, the $\lambda_{i}$  are just standard Lagrange multipliers, with no restriction of positivity. Thus, Proposition 50.9 is a slight generalization of Theorem 40.2 that requires $A$ to have rank $m$, but in the case of equational affine constraints, this assumption is unnecessary. Here is an application of Proposition 50.9 to the interior point method in linear programming.

<!-- PAGE 1788 -->

> **Example 50.4.** In linear programming, the interior point method using a central path uses
$$\mathbb{R}^{n}$$
a logarithmic barrier function to keep the solutions $x \in$ of the equation Ax $= b$ away from boundaries by forcing $x > 0$, which means that $x_{i} > 0$ for all $i$; see Matousek and Gardner $[127]$ (Section 7.2). Write
$$\mathbb{R}_{++}^{n}\mathbb{R}^{n}$$
$$= {x \in | x_{i} > 0, i = 1, \dots  , n}.$$
Observe that $\mathbb{R}_{++}^{n}$ is open and convex. For any $\mu  > 0$, we define the function $f_{\mu}$ defined on $\mathbb{R}_{++}^{n}$ by
$$f_{\mu}(x) = c^{\top}x + \mu \sum_{i=1}^{n}  \ln x_{i},$$
where $c \in \mathbb{R}^{n}$. We would like to find necessary conditions for $f_{\mu}$ to have a maximum on
$$U = {x \in \mathbb{R}_{++}^{n} | Ax = b},$$
or equivalently to solve the following problem:
$$maximizef_{\mu}(x)$$
$$subject to$$
$$Ax = b$$
$$x > 0.$$
Since maximizing $f_{\mu}$ is equivalent to minimizing $-f_{\mu}$, by Proposition 50.9, if $x$ is an
$$\mathbb{R}^{m}$$
optimal of the above problem then there is some $y \in$ such that
$$-\nabla f_{\mu}(x) + A^{\top}y = 0.$$
Since
$$\nabla f_{\mu}(x) = \begin{pmatrix} c_{1} +_{x}^{\mu} \\ \ddots \\ c_{n} +_{xn}^{\mu} \end{pmatrix} ,$$
we obtain the equation
$$c + \mu \begin{pmatrix} 1 \\ \overline{x}\vdots \\ 1 \end{pmatrix} = A^{\top}y.$$
$$\overline{x}\overline{n}$$
To obtain a more convenient formulation, we define $s \in \mathbb{R}_{++}^{n}$ such that
$$s = \mu \begin{pmatrix} 1 \\ \overline{x}\vdots \\ 1 \end{pmatrix}$$
$$\overline{x}\overline{n}$$
