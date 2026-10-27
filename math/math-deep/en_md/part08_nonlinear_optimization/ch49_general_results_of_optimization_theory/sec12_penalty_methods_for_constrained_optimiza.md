# Penalty Methods for Constrained Optimization


<!-- PAGE 1755 -->
In particular, this is the case if
$$\mathbb{R}_{+}^{n}\mathbb{R}^{n}$$
$$U = = {v \in | v \ge 0}$$
and if
$$J(v) = \frac{1}{2} \langle Av, a\rangle -\langle b, v\rangle$$
is an elliptic quadratic functional on $\mathbb{R}^{n}$. Then the vector $u_{k+1} = (u_{1}^{k+1}, \dots  , u_{n}^{k+1})$ is given in terms of $u_{k} = (u_{1}^{k}, \dots  , u_{n}^{k})$ by
$$u_{i}^{k+1}= \max{u_{i}^{k} -\rho_{k} (Au_{k} -b)_{i}, 0},1 \le i \le n.$$

## 49.12 Penalty Methods for Constrained Optimization

In the case where $V = \mathbb{R}^{n}$, another method to deal with constrained optimization is to incorporate the domain $U$ into the objective function $J$ by adding a penalty function.
$$\mathbb{R}^{n} \mathbb{R}^{n} \mathbb{R}$$

> **Definition 49.11.** Given a nonempty closed convex subset $U$ of , a function $\psi$ : $\to$ is called a penalty function for $U$ if $\psi$  is convex and continuous and if the following conditions hold:
$$\psi (v) \ge 0for allv \in \mathbb{R}^{n},and\psi (v) = 0iffv \in U.$$
The following proposition shows that the use of penalty functions reduces a constrained optimization problem to a sequence of unconstrained optimization problems.
$$\mathbb{R}^{n} \mathbb{R}$$

> **Proposition 49.19.** Let $J$ : $\to$  be a continuous, coercive, strictly convex function, $U$
$$\mathbb{R}^{n} \mathbb{R}^{n} \mathbb{R}$$
be a nonempty, convex, closed subset of , $\psi$ : $\to$  be a penalty function for $U$, and let $\mathbb{R}^{n} \mathbb{R} J_{\epsilon}$ : $\to$  be the penalized objective function given by
$$J_{\epsilon}(v) = J(v) + \frac{1}{\epsilon} \psi (v)for all v \in \mathbb{R}^{n}.$$
$$\mathbb{R}^{n}$$
Then for every $\epsilon  > 0$, there exists a unique element $u_{\epsilon} \in$ such that
$$J_{\epsilon}(u_{\epsilon}) = \inf J_{\epsilon}(v).$$
$$v\in \mathbb{R} n$$
Furthermore, if $u \in U$ is the unique minimizer of $J$ over $U$, so that J(u) $= inf_{v\in U}$ J(v), then
$$lim u_{\epsilon} = u.$$
$$\epsilon \mapsto 0$$

*Proof.* Observe that since $J$ is coercive, since $\psi (v) \ge 0$ for all $v \in \mathbb{R}^{n}$, and $J_{\epsilon} = J + (1/\epsilon )\psi$ , we have $J_{\epsilon}(v) \ge$ J(v) for all $v \in \mathbb{R}^{n}$, so $J_{\epsilon}$ is also coercive. Since $J$ is strictly convex and $(1/\epsilon )\psi$  is convex, it is immediately checked that $J_{\epsilon} = J + (1/\epsilon )\psi$  is also strictly convex. Then by Proposition 49.1 (and the fact that $J$ and $J_{\epsilon}$ are strictly convex), $J$ has a unique minimizer $u \in U$, and $J_{\epsilon}$ has a unique minimizer $u_{\epsilon} \in \mathbb{R}^{n}$.

<!-- PAGE 1756 -->
Since $\psi (u) = 0$ iff $u \in U$, and $\psi (v) \ge 0$ for all $v \in \mathbb{R}^{n}$, we have $J_{\epsilon}(u) =$ J(u), and since $u_{\epsilon}$ is the minimizer of $J_{\epsilon}$ we have $J_{\epsilon}(u_{\epsilon}) \le J_{\epsilon}(u)$, so we obtain
$$J(u_{\epsilon}) \le J(u_{\epsilon}) + \frac{1}{\epsilon} \psi (u_{\epsilon}) = J_{\epsilon}(u_{\epsilon}) \le J_{\epsilon}(u) = J(u),$$
that is,
$$J(u_{\epsilon}) \le J(u).(*_{1})$$
Since $J$ is coercive, the family $(u_{\epsilon})_{\epsilon >0}$ is bounded. By compactness (since we are in $\mathbb{R}^{n})$,
$$\mathbb{R}^{n}$$
there exists a subsequence $(u_{\epsilon(i)})_{i\ge0}$ with $lim_{i\mapsto \infty} \epsilon (i) = 0$ and some element u' $\in$ such that
$$limu_{\epsilon(i)} = u'.$$
$$i\mapsto \infty$$
From the inequality $J(u_{\epsilon}) \le$ J(u) proven in $(*_{1})$ and the continuity of $J$, we deduce that
$$J(u') = limJ(u_{\epsilon(i)}) \le J(u).(*_{2})$$
$$i\mapsto \infty$$
By definition of $J_{\epsilon}(u_{\epsilon})$ and $(*_{1})$, we have
$$0 \le \psi (u_{\epsilon(i)}) \le \epsilon (i)(J(u) -J(u_{\epsilon(i)})),$$
and since the sequence $(u_{\epsilon(i)})_{i\ge0}$ converges, the numbers J(u) - $J(u_{\epsilon(i)})$ are bounded independently of $i$. Consequently, since $lim_{i\mapsto \infty} \epsilon (i) = 0$ and since the function $\psi$  is continuous, we have
$$0 = lim\psi (u_{\epsilon(i)}) = \psi (u'),$$
$$i\mapsto \infty$$
which shows that u' $\in U$. Since by $(*_{2})$ we have J(u') $\le$ J(u), and since both $u$, u' $\in U$ and $u$ is the unique minimizer of $J$ over $U$ we must have u' $= u$. Therfore u' is the unique minimizer of $J$ over $U$. But then the whole family $(u_{\epsilon})_{\epsilon >0}$ converges to $u$ since we can use the same argument as above for every subsequence of $(u_{\epsilon})_{\epsilon >0}$.
$$\mathbb{R}^{n} \mathbb{R}$$
Note that a convex function $\psi$ : $\to$  is automatically continuous, so the assumption of continuity is redundant. As an application of Proposition 49.19, if $U$ is given by
$$\mathbb{R}^{n}$$
$$U = {v \in | \phi_{i} (v) \le 0, i = 1, \dots  , m},$$
$$\mathbb{R}^{n} \mathbb{R}$$
where the functions $\phi_{i}$  : $\to$  are convex, we can take $\psi$  to be the function given by
$$\psi (v) = \sum_{i=1}^{m}  \max{\phi_{i} (v), 0}.$$
