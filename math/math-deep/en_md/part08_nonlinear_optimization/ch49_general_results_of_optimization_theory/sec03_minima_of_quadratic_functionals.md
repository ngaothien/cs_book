# Minima of Quadratic Functionals


<!-- PAGE 1711 -->
and by definition of weak convergence
$$lim\langle \nabla J_{v}, z_{\ell}\rangle = \langle \nabla J_{v}, v\rangle ,$$
$$\ell \mapsto \infty$$
so $lim_{\ell\mapsto \infty}\langle \nabla J_{v}, z_{\ell}$ - $v\rangle = 0$, and by definition of lim inf we get
$$J(v) \le lim infJ(z_{\ell})$$
$$\ell \mapsto \infty$$
for every sequence $(z_{\ell})_{\ell\ge0}$ converging weakly to some element $v \in V$ . Step $4$. The weak limit $u \in U$ of the subsequence $(w_{\ell})_{\ell\ge0}$ extracted from the minimizing sequence $(u_{k})_{k\ge0}$ satisfies the equation
$$J(u) = \inf J(v).$$
$$v\in U$$
By Step $(1)$ and Step $(2)$ the subsequence $(w_{\ell})_{\ell\ge0}$ of the sequence $(u_{k})_{k\ge0}$ converges weakly to some element $u \in U$, so by Step $(3)$ we have
$$J(u) \le lim infJ(w_{\ell}).$$
$$\ell \mapsto \infty$$
On the other hand, by definition of $(w_{\ell})_{\ell\ge0}$ as a subsequence of $(u_{k})_{k\ge0}$, since the sequence $(J(u_{k}))_{k\ge0}$ converges to J(v), we have
$$J(u) \le lim infJ(w_{\ell}) = limJ(u_{k}) = \inf J(v),$$
$$\ell \mapsto \infty k\mapsto \infty v\in U$$
which proves that $u \in U$ achieves the minimum of $J$ on $U$.
Remark: Theorem 49.2 still holds if we only assume that $J$ is convex and continuous. It also holds in a reflexive Banach space, of which Hilbert spaces are a special case; see Brezis $[31]$, Corollary 3.23. Theorem 49.2 is a rather general theorem whose proof is quite involved. For functions $J$ of a certain type, we can obtain existence and uniqueness results that are easier to prove. This is true in particular for quadratic functionals.

## 49.3 Minima of Quadratic Functionals


> **Definition 49.4.** Let $V$ be a real Hilbert space. A function $J$ : $V \to \mathbb{R}$ is called a quadratic functional if it is of the form
$$J(v) = \frac{1}{2} a(v, v) -h(v),$$
where a: $V \times  V \to \mathbb{R}$ is a bilinear form which is symmetric and continuous, and $h: V \to \mathbb{R}$ is a continuous linear form.

<!-- PAGE 1712 -->
Definition 49.4 is a natural extension of the notion of a quadratic functional on $\mathbb{R}^{n}$. Indeed, by Proposition 48.10, there is a unique continuous self-adjoint linear map $A: V \to V$ such that
$$a(u, v) = \langle Au, v\rangle for all u, v \in V ,$$
and by the Riesz representation theorem (Proposition 48.9), there is a unique $b \in V$ such that
$$h(v) = \langle b, v\rangle for all v \in V .$$
Consequently, $J$ can be written as
$$J(v) = \frac{1}{2} \langle Av, v\rangle -\langle b, v\rangle for all v \in V .(1)$$
Since a is bilinear and $h$ is linear, by Propositions 39.3 and 39.5, observe that the derivative of $J$ is given by
$$dJ_{u}(v) = a(u, v) -h(v)for all v \in V ,$$
or equivalently by
$$dJ_{u}(v) = \langle Au, v\rangle -\langle b, v\rangle = \langle Au -b, v\rangle ,for all v \in V .$$
Thus the gradient of $J$ is given by
$$\nabla J_{u} = Au -b,(2)$$
just as in the case of a quadratic function of the form J(v) $= (1/2)v^{\top}Av$ - $b^{\top}v$, where $A$ is a symmetric $n \times  n$ matrix and $b \in \mathbb{R}^{n}$. To find the second derivative $D^{2}J_{u}$ of $J$ at $u$ we compute
$$dJ_{u+v}(w) -dJ_{u}(w) = a(u + v, w) -h(w) -(a(u, w) -h(w)) = a(v, w),$$
so
$$D^{2}J_{u}(v, w) = a(v, w) = \langle Av, w\rangle ,$$
which yields
$$\nabla^{2} J_{u} = A.(3)$$
We will also make use of the following formula.

> **Proposition 49.3.** If $J$ is a quadratic functional, then
$$J(u + \rho v) = \frac{\rho^{2}}{2} a(v, v) + \rho (a(u, v) -h(v)) + J(u).$$

<!-- PAGE 1713 -->

*Proof.* Since a is symmetric bilinear and $h$ is linear, we have
$$J(u + \rho v) = \frac{1}{2} a(u + \rho v, u + \rho v) -h(u + \rho v)$$
$$= \frac{\rho^{2}}{2} a(v, v) + \rho a(u, v) + \frac{1}{2} a(u, u) -h(u) -\rho h(v)$$
$$= \frac{\rho^{2}}{2} a(v, v) + \rho (a(u, v) -h(v)) + J(u).$$
Since $dJ_{u}(v) =$ a(u, $v)$ - h(v) $= \langle$ Au - $b, v\rangle$ and $\nabla J_{u} =$ Au - $b$, we can also write
$$J(u + \rho v) = \frac{\rho^{2}}{2} a(v, v) + \rho \langle \nabla J_{u}, v\rangle + J(u),$$
as claimed. We have the following theorem about the existence and uniqueness of minima of quadratic functionals.

> **Theorem 49.4.** Given any real Hilbert space $V$ , let $J$ : $V \to \mathbb{R}$ be a quadratic functional of the form
$$J(v) = \frac{1}{2} a(v, v) -h(v).$$
Assume that there is some real number $\alpha  > 0$ such that
$$a(v, v) \ge \alpha  \|v\|^{2}for all v \in V .(*_{\alpha})$$
If $U$ is any nonempty, closed, convex subset of $V$ , then there is a unique $u \in U$ such that
$$J(u) = \inf J(v).$$
$$v\in U$$
The element $u \in U$ satisfies the condition
$$a(u, v -u) \ge h(v -u)for all v \in U.(*)$$
Conversely (with the same assumptions on $U$ as above), if an element $u \in U$ satisfies (*), then
$$J(u) = \inf J(v).$$
$$v\in U$$
If $U$ is a subspace of $V$ , then the above inequalities are replaced by the equations
$$a(u, v) = h(v)for all v \in U.(**)$$

*Proof.* The key point is that the bilinear form a is actually an inner product in $V$ . This is because it is positive definite, since $(*_{\alpha})$ implies that
$$\sqrt$$
$$\overline{\alpha} \|v\|\le (a(v, v))^{1/2},$$

<!-- PAGE 1714 -->
and on the other hand the continuity of a implies that
$$a(v, v) \le \|a\|\|v\|^{2},$$
so we get
$$\sqrt$$
$$p$$
$$\overline{\alpha} \|v\|\le (a(v, v))^{1/2}\le \overline{\|}\overline{a}\overline{\|\|} v\|.$$
The above also shows that the norm $v \mapsto$ (a(v, $v))^{1/2}$ induced by the inner product a is equivalent to the norm induced by the inner product $\langle$ -, $-\rangle$ on $V$ . Thus $h$ is still continuous with respect to the norm $v \mapsto$ (a(v, $v))^{1/2}$. Then by the Riesz representation theorem (Proposition 48.9), there is some unique $c \in V$ such that
$$h(v) = a(c, v)for all v \in V .$$
Consequently, we can express J(v) as
$$J(v) = \frac{1}{2} a(v, v) -a(c, v) = \frac{1}{2} a(v -c, v -c) - \frac{1}{2} a(c, c).$$
But then minimizing J(v) over $U$ is equivalent to minimizing (a(v $-c, v -c))^{1/2}$ over $v \in U$, and by the projection lemma (Proposition 48.5(1)) this is equivalent to finding the projection $p_{U}(c)$ of $c$ on the closed convex set $U$ with respect to the inner product a. Therefore, there is a unique $u = p_{U}(c) \in U$ such that
$$J(u) = \inf J(v).$$
$$v\in U$$
Also by Proposition 48.5(2), this unique element $u \in U$ is characterized by the condition
$$a(u -c, v -u) \ge 0for all v \in U.$$
Since
$$a(u -c, v -u) = a(u, v -u) -a(c, v -u) = a(u, v -u) -h(v -u),$$
the above inequality is equivalent to
$$a(u, v -u) \ge h(v -u)for all v \in U.(*)$$
If $U$ is a subspace of $V$ , then by Proposition 48.5(3) we have the condition
$$a(u -c, v) = 0for all v \in U,$$
which is equivalent to
$$a(u, v) = a(c, v) = h(v)for all v \in U,(**)$$
a claimed.

<!-- PAGE 1715 -->
Note that the symmetry of the bilinear form a played a crucial role. Also, the inequalities
$$a(u, v -u) \ge h(v -u)for all v \in U$$
are sometimes called variational inequalities.

> **Definition 49.5.** A bilinear form a: $V \times  V \to \mathbb{R}$ such that there is some real $\alpha  > 0$ such that
$$a(v, v) \ge \alpha  \|v\|^{2}for all v \in V$$
is said to be coercive. Theorem 49.4 is the special case of Stampacchia’s theorem and the Lax–Milgram theorem when $U = V$ , and where a is a symmetric bilinear form. To prove Stampacchia’s theorem in general, we need to recall the contraction mapping theorem.

> **Definition 49.6.** Let $(E, d)$ be a metric space. A map $f$ : $E \to E$ is a contraction (or a contraction mapping) if there is some real number $k$ such that $0 \le k < 1$ and
$$d(f(u), f(v)) \le kd(u, v)for all u, v \in E.$$
The number $k$ is often called a Lipschitz constant. The following theorem is proven in Section 37.10; see Theorem 37.54. A proof can be also found in Apostol $[4]$, Dixmier $[52]$, or Schwartz $[156]$, among many sources. For the reader’s convenience we restate this theorem.

> **Theorem 49.5.** (Contraction Mapping Theorem) Let $(E, d)$ be a complete metric space. Every contraction $f$ : $E \to E$ has a unique fixed point (that is, an element $u \in E$ such that f(u) $= u)$. The contraction mapping theorem is also known as the Banach fixed point theorem.

> **Theorem 49.6.** (Lions–Stampacchia) Given a Hilbert space $V$ , let a: $V \times  V \to \mathbb{R}$ be a continuous bilinear form (not necessarily symmetric), let $h \in$ V' be a continuous linear form, and let $J$ be given by
$$J(v) = \frac{1}{2} a(v, v) -h(v),v \in V.$$
If a is coercive, then for every nonempty, closed, convex subset $U$ of $V$ , there is a unique $u \in U$ such that
$$a(u, v -u) \ge h(v -u)for all v \in U.(*)$$
If a is symmetric, then $u \in U$ is the unique element of $U$ such that
$$J(u) = \inf J(v).$$
$$v\in U$$

<!-- PAGE 1716 -->

*Proof.* As discussed just after Definition 49.4, by Proposition 48.10, there is a unique continuous linear map $A: V \to V$ such that
$$a(u, v) = \langle Au, v\rangle for all u, v \in V ,$$
with $\|A\| = \|a\| = C$, and by the Riesz representation theorem (Proposition 48.9), there is a unique $b \in V$ such that
$$h(v) = \langle b, v\rangle for all v \in V .$$
Consequently, $J$ can be written as
$$J(v) = \frac{1}{2} \langle Av, v\rangle -\langle b, v\rangle for all v \in V .( *_{1})$$
Since $\|A\| = \|a\| = C$, we have $\|Av\|\le \|A\|\|v\| = C \|v\|$ for all $v \in V$ . Using $(*_{1})$, the inequality (*) is equivalent to finding $u$ such that
$$\langle Au, v -u\rangle \ge \langle b, v -u\rangle for all v \in U.( *_{2})$$
Let $\rho  > 0$ be a constant to be determined later. Then $(*_{2})$ is equivalent to
$$\langle \rho b -\rho Au + u -u, v -u\rangle \le 0for all v \in U.( *_{3})$$
By the projection lemma (Proposition 48.5 $(1)$ and $(2)), (*_{3})$ is equivalent to finding $u \in U$ such that
$$u = p_{U}(\rho b -\rho Au + u).( *_{4})$$
We are led to finding a fixed point of the function $F$ : $U \to U$ given by
$$F(v) = p_{U}(\rho b -\rho Av + v).$$
By Proposition 48.6, the projection map $p_{U}$ does not increase distance, so
$$\|F(v_{1}) -F(v_{2})\|\le \|v_{1} -v_{2} -\rho (Av_{1} -Av_{2})\|.$$
Since a is coercive we have
$$a(v, v) \ge \alpha  \|v\|^{2},$$
since a(v, $v) = \langle$ Av, $v\rangle$ we have
$$\langle Av, v\rangle \ge \alpha  \|v\|^{2}for all v \in V ,( *_{5})$$
and since
$$\|Av\|\le C \|v\|for all v \in V ,( *_{6})$$
we get
$$\|F(v_{1}) -F(v_{2})\|^{2}\le \|v_{1} -v_{2}\|^{2}-2\rho \langle Av_{1} -Av_{2}, v_{1} -v_{2}\rangle + \rho^{2} \|Av_{1} -Av_{2}\|^{2}$$
$$\le \begin{pmatrix} 1 -2\rho \alpha  + \rho^{2} C^{2} \end{pmatrix} \|v_{1} -v_{2}\|^{2}.$$

<!-- PAGE 1717 -->
If we pick $\rho  > 0$ such that $\rho  < 2\alpha /C^{2}$, then
$$k^{2}= 1 -2\rho \alpha  + \rho^{2} C^{2}< 1,$$
and then
$$\|F(v_{1}) -F(v_{2})\|\le k \|v_{1} -v_{2}\|,( *_{7})$$
with $0 \le k < 1$, which shows that $F$ is a contraction. By Theorem 49.5, the map $F$ has a unique fixed point $u \in U$, which concludes the proof of the first statement. If a is also symmetric, then the second statement is just the first part of Theorem 49.4.
Remark: Many physical problems can be expressed in terms of an unknown function $u$ that satisfies some inequality
$$a(u, v -u) \ge h(v -u)for all v \in U,$$
for some set $U$ of “admissible” functions which is closed and convex. The bilinear form a and the linear form $h$ are often given in terms of integrals. The above inequality is called a variational inequality. In the special case where $U = V$ we obtain the Lax–Milgram theorem.

> **Theorem 49.7.** (Lax–Milgram’s Theorem) Given a Hilbert space $V$ , let a: $V \times  V \to \mathbb{R}$ be a continuous bilinear form (not necessarily symmetric), let $h \in$ V' be a continuous linear form, and let $J$ be given by
$$J(v) = \frac{1}{2} a(v, v) -h(v),v \in V.$$
If a is coercive, which means that there is some $\alpha  > 0$ such that
$$a(v, v) \ge \alpha  \|v\|^{2}for all v \in V ,$$
then there is a unique $u \in V$ such that
$$a(u, v) = h(v)for all v \in V .$$
If a is symmetric, then $u \in V$ is the unique element of $V$ such that
$$J(u) = \inf J(v).$$
$$v\in V$$
The Lax–Milgram theorem plays an important role in solving linear elliptic partial differential equations; see Brezis $[31]$. We now consider various methods, known as gradient descents, to find minima of certain types of functionals.
