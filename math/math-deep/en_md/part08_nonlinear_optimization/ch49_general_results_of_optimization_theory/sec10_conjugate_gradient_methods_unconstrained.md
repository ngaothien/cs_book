# Conjugate Gradient Methods; Unconstrained Problems


<!-- PAGE 1741 -->
$(1)$ If $\lambda (u_{k}) > \eta$ , then
$$J(u_{k+1}) -J(u_{k}) \le -\gamma .$$
$(2)$ If $\lambda (u_{k}) \le \eta$ , then the backtracking line search selects $t = 1$ and we have
$$2\lambda (u_{k+1}) \le (2\lambda (u_{k}))^{2}.$$
As a consequence, for all $\ell \ge k$, we have
$$1^{2\ell-k+1}$$
$$J(u_{\ell}) -p^{*}\le \lambda (u_{\ell})^{2}\le \begin{pmatrix} \overline{2} \end{pmatrix} .$$
In the end, accuracy $\epsilon  > 0$ is achieved in at most
$$-$$
$$\frac{208\alpha}{\alpha \beta (1 -2\alpha )^{2}} (J(u_{0}) -p^{*}) + log_{2} log_{2}(1/\epsilon )$$
iterations, where $\alpha$  and $\beta$  are the constants involved in the line search. This bound is obviously independent of the chosen coordinate system. Contrary to intuition, the descent direction $d_{k} = -\nabla J_{uk}$ given by the opposite of the gradient is not always optimal. In the next section we will see how a better direction can be picked; this is the method of conjugate gradients.

## 49.10 Conjugate Gradient Methods for Unconstrained

$$Problems$$
The conjugate gradient method due to Hestenes and Stiefel $(1952)$ is a gradient descent
$$\mathbb{R}^{n} \mathbb{R}$$
method that applies to an elliptic quadratic functional $J$ : $\to$  given by
$$J(v) = \frac{1}{2} \langle Av, v\rangle -\langle b, v\rangle ,$$
where $A$ is an $n \times  n$ symmetric positive definite matrix. Although it is presented as an iterative method, it terminates in at most $n$ steps. As usual, the conjugate gradient method starts with some arbitrary initial vector $u_{0}$ and proceeds through a sequence of iteration steps generating (better and better) approximations $u_{k}$ of the optimal vector $u$ minimizing $J$. During an iteration step, two vectors need to be determined:
$(1)$ The descent direction $d_{k}$.
$(2)$ The next approximation $u_{k+1}$. To find $u_{k+1}$, we need to find the stepsize $\rho_{k}  > 0$ and then
$$u_{k+1} = u_{k} -\rho_{k} d_{k}.$$
Typically, $\rho_{k}$  is found by performing a line search along the direction $d_{k}$, namely we find $\rho_{k}$  as the real number such that the function $\rho  \mapsto J(u_{k}$ - $\rho d_{k})$ is minimized.

<!-- PAGE 1742 -->
We saw in Proposition 49.13 that during execution of the gradient method with optimal stepsize parameter that any two consecutive descent directions are orthogonal. The new twist with the conjugate gradient method is that given $u_{0}, u_{1}, \dots  , u_{k}$, the next approximation $u_{k+1}$ is obtained as the solution of the problem which consists in minimizing $J$ over the affine
$$\mathbb{R}^{n}$$
subspace $u_{k} +\mathcal{G}_{k}$, where $\mathcal{G}_{k}$ is the subspace of spanned by the gradients
$$\nabla J_{u0}, \nabla J_{u1}, \dots  , \nabla J_{uk}.$$
We may assume that $\nabla J_{u\ell}$ ̸ $= 0$ for $\ell = 0, \dots  , k$, since the method terminates as soon as $\nabla J_{uk} = 0$. A priori the subspace $\mathcal{G}_{k}$ has dimension $\le k + 1$, but we will see that in fact it has dimension $k + 1$. Then we have
$$$$
$$u_{k} +\mathcal{G}_{k} =u_{k} + \sum_{i=0}^{k}  \alpha_{i} \nabla J_{ui} \alpha_{i}  \in \mathbb{R}, 0 \le i \le k,$$
and our minimization problem is to find $u_{k+1}$ such that
$$u_{k+1} \in u_{k} +\mathcal{G}_{k}andJ(u_{k+1}) =\inf J(v).$$
$$v\in uk+\mathcal{G} k$$
In the gradient method with optimal stepsize parameter the descent direction $d_{k}$ is proportional to the gradient $\nabla J_{uk}$, but in the conjugate gradient method, $d_{k}$ is equal to $\nabla J_{uk}$ corrected by some multiple of $d_{k-1}$. The conjugate gradient method is superior to the gradient method with optimal stepsize parameter for the following reasons proved correct later:
(a) The gradients $\nabla J_{ui}$ and $\nabla J_{uj}$ are orthogonal for all $i, j$ with $0 \le i \neq  j \le k$. This implies that if $\nabla J_{ui}$ ̸ $= 0$ for $i = 0, \dots  , k$, then the vectors $\nabla J_{ui}$ are linearly independent, so the method stops in at most $n$ steps.
$(b)$ If we write $\Delta_{\ell} = u_{\ell+1}$ - $u_{\ell} = -\rho_{\ell} d_{\ell}$, the second remarkable fact about the conjugate gradient method is that the vectors $\Delta_{\ell}$ satisfy the following conditions:
$$\langle A\Delta_{\ell} , \Delta_{i} \rangle = 00 \le i < \ell \le k.$$
The vectors $\Delta_{\ell}$ and $\Delta_{i}$  are said to be conjugate with respect to the matrix $A$ (or A-conjugate). As a consequence, if $\Delta_{\ell}  \neq  0$ for $\ell = 0, \dots  , k$, then the vectors $\Delta_{\ell}$ are linearly independent.
$(c)$ There is a simple formula to compute $d_{k+1}$ from $d_{k}$, and to compute $\rho_{k}$ . We now prove the above facts. We begin with (a).

> **Proposition 49.15.** Assume that $\nabla J_{ui}$ ̸ $= 0$ for $i = 0, \dots  , k$. Then the minimization problem, find $u_{k+1}$ such that
$$u_{k+1} \in u_{k} +\mathcal{G}_{k}andJ(u_{k+1}) =\inf J(v),$$
$$v\in uk+\mathcal{G} k$$
has a unique solution, and the gradients $\nabla J_{ui}$ and $\nabla J_{uj}$ are orthogonal for all $i, j$ with $0 \le i \neq  j \le k + 1$.

<!-- PAGE 1743 -->

*Proof.* The affine space $u_{\ell} + \mathcal{G}_{\ell}$ is closed and convex, and since $J$ is a quadratic elliptic functional it is coercive and strictly convex, so by Theorem 49.8(2) it has a unique minimum in $u_{\ell} +\mathcal{G}_{\ell}$. This minimum $u_{\ell+1}$ is also the minimum of the problem, find $u_{\ell+1}$ such that
$$u_{\ell+1} \in u_{\ell}+\mathcal{G}_{\ell}andJ(u_{\ell+1}) = infJ(u_{\ell}+ v),$$
$$v\in G\ell$$
and since $\mathcal{G}_{\ell}$ is a subspace, by Corollary 40.10 we must have
$$dJ_{u\ell+1}(w) = 0for all w \in G_{\ell},$$
that is
$$\langle \nabla J_{u\ell+1}, w\rangle = 0for all w \in G_{\ell}.$$
Since $\mathcal{G}_{\ell}$ is spanned by $(\nabla J_{u0}, \nabla J_{u1}, \dots  , \nabla J_{u\ell})$, we obtain
$$\langle \nabla J_{u\ell+1}, \nabla J_{uj}\rangle = 0,0 \le j \le \ell ,$$
and since this holds for $\ell = 0, \dots  , k$, we get
$$\langle \nabla J_{ui}, \nabla J_{uj}\rangle = 0,0 \le i \neq  j \le k + 1,$$
which shows the second part of the proposition. As a corollary of Proposition 49.15, if $\nabla J_{ui}$ ̸ $= 0$ for $i = 0, \dots  , k$, then the vectors $\nabla J_{ui}$ are linearly independent $and\mathcal{G}_{k}$ has dimension $k + 1$. Therefore, the conjugate gradient method terminates in at most $n$ steps. Here is an example of a problem for which the gradient descent with optimal stepsize parameter does not converge in a finite number of steps.
$$\mathbb{R}^{2} \mathbb{R}$$

> **Example 49.2.** Let $J$ : $\to$  be the function given by
$$J(v_{1}, v_{2}) = \frac{1}{2} (\alpha_{1} v_{1}^{2} + \alpha_{2} v_{2}^{2}),$$
where $0 < \alpha_{1}  < \alpha_{2}$ . The minimum of $J$ is attained at $(0, 0)$. Unless the initial vector $u_{0} = (u_{1}^{0}, u_{2}^{0})$ has the property that either $u_{1}^{0} = 0$ or $u_{2}^{0} = 0$, we claim that the gradient descent with optimal stepsize parameter does not converge in a finite number of steps. Observe that
$$\nabla J_{(v1,v2)} = \begin{pmatrix} \alpha_{1} v_{1} \\ \alpha_{2} v_{2} \end{pmatrix} .$$
As a consequence, given $u_{k}$, the line search for finding $\rho_{k}$  and $u_{k+1}$ yields $u_{k+1} = (0, 0)$ iff there is some $\rho  \in \mathbb{R}$ such that
$$u_{1}^{k} = \rho \alpha_{1} u_{1}^{k}andu_{2}^{k} = \rho \alpha_{2} u_{2}^{k}.$$
Since $\alpha_{1}  \neq  \alpha_{2}$ , this is only possible if either $u_{1}^{k} = 0$ or $u_{2}^{k} = 0$. The formulae given just before Proposition 49.14 yield
$$u_{1}^{k+1}= \frac{\alpha_{2}^{2} (\alpha_{2} \alpha_{1} )u_{1}^{k}(u_{2}^{k})^{2}}{\alpha_{1}^{3} (u_{1}^{k})^{2} \alpha_{2}^{3} (u_{2}^{k})^{2}} - ,u_{2}^{k+1}= \frac{\alpha_{1}^{2} (\alpha_{1} \alpha_{2} )u_{2}^{k}(u_{1}^{k})^{2}}{\alpha_{1}^{3} (u_{1}^{k})^{2} \alpha_{2}^{3} (u_{2}^{k})^{2}} - ,$$
$$+ +$$
which implies that if $u_{1}^{k}$ ̸ $= 0$ and $u_{2}^{k}$ ̸ $= 0$, then $u_{1}^{k+1} = 0$ and $u_{2}^{k+1} = 0$, so the method runs forever from any initial vector $u_{0} = (u_{1}^{0}, u_{2}^{0})$ such that $u_{1}^{0}$ ̸ $= 0$ and, $u_{2}^{0}$ ̸ $= 0$.

<!-- PAGE 1744 -->
We now prove $(b)$.

> **Proposition 49.16.** Assume that $\nabla J_{ui}$ ̸ $= 0$ for $i = 0, \dots  , k$, and let $\Delta_{\ell} = u_{\ell+1}$ - $u_{\ell}$, for $\ell = 0, \dots  , k$. Then $\Delta_{\ell}  \neq  0$ for $\ell = 0, \dots  , k$, and
$$\langle A\Delta_{\ell} , \Delta_{i} \rangle = 0,0 \le i < \ell \le k.$$
The vectors $\Delta_{0} , \dots  , \Delta_{k}$  are linearly independent.

*Proof.* Since $J$ is a quadratic functional we have
$$\nabla J_{v+w} = A(v + w) -b = Av -b + Aw = \nabla J_{v} + Aw.$$
It follows that
$$\nabla J_{u\ell+1} = \nabla J_{u\ell+\Delta\ell}= \nabla J_{u\ell}+ A\Delta_{\ell} ,0 \le \ell \le k.(*_{1})$$
By Proposition 49.15, since
$$\langle \nabla J_{ui}, \nabla J_{uj}\rangle = 0,0 \le i \neq  j \le k,$$
we get
$$0 = \langle \nabla J_{u\ell+1}, \nabla J_{u\ell}\rangle = \|\nabla J_{u\ell}\|^{2}+ \langle A\Delta_{\ell} , \nabla J_{u\ell}\rangle ,\ell = 0, \dots  , k,$$
and since by hypothesis $\nabla J_{ui}$ ̸ $= 0$ for $i = 0, \dots  , k$, we deduce that
$$\Delta_{\ell}  \neq  0,\ell = 0, \dots  , k.$$
If $k \ge 1$, for $i = 0, \dots  , \ell$ - $1$ and $\ell \le k$ we also have
$$0 = \langle \nabla J_{u\ell+1}, \nabla J_{ui}\rangle = \langle \nabla J_{u\ell}, \nabla J_{ui}\rangle + \langle A\Delta_{\ell} , \nabla J_{ui}\rangle$$
$$= \langle A\Delta_{\ell} , \nabla J_{ui}\rangle .$$
Since $\Delta_{j}  = u_{j+1}$ - $u_{j} \in G_{j}$ and $\mathcal{G}_{j}$ is spanned by $(\nabla J_{u0}, \nabla J_{u1}, \dots  , \nabla J_{uj})$, we obtain
$$\langle A\Delta_{\ell} , \Delta_{j} \rangle = 0,0 \le j < \ell \le k.$$
For the last statement of the proposition, let $w_{0}, w_{1}, \dots  , w_{k}$ be any $k + 1$ nonzero vectors such that
$$\langle Aw_{i}, w_{j}\rangle = 0,0 \le i < j \le k.$$
We claim that $w_{0}, w_{1}, \dots  , w_{k}$ are linearly independent.
$$If we have a linear dependence \sum_{i}  k=0 \lambda_{i} w_{i} = 0, then we have$$
$$0 =A \begin{pmatrix} \lambda_{i} w_{i} \end{pmatrix} \sum_{i=0}^{k}  , w_{j}= \sum_{i=0}^{k}  \lambda_{i} \langle Aw_{i}, w_{j}\rangle = \lambda_{j} \langle Aw_{j}, w_{j}\rangle ,$$
where we form these inner products for $j = 0, \dots  , k$, in that order. Since $A$ is symmetric positive definite (because $J$ is a quadratic elliptic functional) and $w_{j}$ ̸ $= 0$, we have $\langle Aw_{j}, w_{j}\rangle > 0$, and so $\lambda_{j}  = 0$ for $j = 0, \dots  , k$. Therefore the vectors $w_{0}, w_{1}, \dots  , w_{k}$ are linearly independent.

<!-- PAGE 1745 -->
Remarks:
$(1)$ Since $A$ is symmetric positive definite, the bilinear map $(u, v) \mapsto \langle$ Au, $v\rangle$ is an inner product $\langle$ -, $-\rangle_{A}$  on $\mathbb{R}^{n}$. Consequently, two vectors $u, v$ are conjugate with respect to the matrix $A$ (or A-conjugate), which means that $\langle$ Au, $v\rangle = 0$, iff $u$ and $v$ are orthogonal with respect to the inner product $\langle$ -, $-\rangle_{A}$ .
$(2)$ By picking the descent direction to be $-\nabla J_{uk}$, the gradient descent method with optimal stepsize parameter treats the level sets ${u$ | J(u) $= J(u_{k})}$ as if they were spheres. The conjugate gradient method is more subtle, and takes the “geometry” of the level set ${u$ | J(u) $= J(u_{k})}$ into account, through the notion of conjugate directions.
$(3)$ The notion of conjugate direction has its origins in the theory of projective conics and quadrics where $A$ is a $2 \times  2$ or a $3 \times  3$ matrix and where $u$ and $v$ are conjugate iff $u^{\top}Av = 0$.
$(4)$ The terminology conjugate gradient is somewhat misleading. It is not the gradients who are conjugate directions, but the descent directions. By definition of the vectors $\Delta_{\ell} = u_{\ell+1}$ - $u_{\ell}$, we can write
$$\Delta_{\ell} = \sum_{i=0}^{\ell}  \delta_{i}^{\ell}  \nabla J_{ui},0 \le \ell \le k.(*_{2})$$
In matrix form, we can write
$$\begin{pmatrix} \Delta_{0} & \Delta_{1} & \cdots & \Delta_{k} \end{pmatrix} = \begin{pmatrix} \nabla J_{u0} & \nabla J_{u1} & \cdots & \nabla J_{uk} \end{pmatrix} \begin{pmatrix} \delta_{0}^{0} & \delta^{1} & \cdots & \delta^{k-1} & \delta^{k} \\ 0 & \delta_{1}^{01} & \cdots & \delta^{0k-1} & \delta^{0k} \\ 0 & 0 & \cdots & \delta_{2}^{1k-1} & \delta_{2}^{1k} \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \delta_{k}^{k} \end{pmatrix} ,$$
$$\cdots$$
which implies that $\delta_{\ell}^{\ell}$  ̸ $= 0$ for $\ell = 0, \dots  , k$. In view of the above fact, since $\Delta_{\ell}$ and $d_{\ell}$ are collinear, it is convenient to write the descent direction $d_{\ell}$ as
$$d_{\ell}= \sum_{i=0}^{\ell-1}  \lambda_{i}^{\ell}  \nabla J_{ui} + \nabla J_{u\ell},0 \le \ell \le k.(*_{3})$$
Our next goal is to compute $u_{k+1}$, assuming that the coefficients $\lambda_{i}^{k}$  are known for $i = 0, \dots  , k$, and then to find simple formulae for the $\lambda_{i}^{k}$  . The problem reduces to finding $\rho_{k}$  such that
$$J(u_{k} -\rho_{k} d_{k}) = \inf J(u_{k} -\rho d_{k}),$$
$$\rho \in \mathbb{R}$$

<!-- PAGE 1746 -->
and then $u_{k+1} = u_{k}$ - $\rho_{k} d_{k}$. In fact, by $(*_{2})$, since
$$\Delta_{k}  = \sum_{i=0}^{k}  \delta_{i}^{k}  \nabla J_{ui} = \delta_{k}^{k} \begin{pmatrix} \delta_{i}^{k} \\ \nabla J_{ui}+ \nabla J_{uk} \\ \delta_{k}^{k} \end{pmatrix} \sum_{i=0}^{k-1}  ,$$
we must have
$$\Delta_{k}  = \delta_{k}^{k} d_{k}and\rho_{k}  = -\delta_{k}^{k} .(*_{4})$$
Remarkably, the coefficients $\lambda_{i}^{k}$  and the descent directions $d_{k}$ can be computed easily using the following formulae.

> **Proposition 49.17.** Assume that $\nabla J_{ui}$ ̸ $= 0$ for $i = 0, \dots  , k$. If we write
$$d_{\ell}= \sum_{i=0}^{\ell-1}  \lambda_{i}^{\ell}  \nabla J_{ui} + \nabla J_{u\ell},0 \le \ell \le k,$$
then we have
$$ \|\nabla \|^{2}$$
$$\lambda_{i}^{k}  = \frac{J_{uk}}{\|\nabla J_{ui}\|^{2}} ,0 \le i \le k -1,$$
$$$$
$$$$
$$$$
$$(\dagger )d_{0} = \nabla J_{u0}$$
$$ \|\nabla \|^{2}$$
$$$$
$$d_{\ell}= \nabla J_{u\ell}+ \frac{J_{u\ell}}{\nabla J_{u\ell-1}^{2}} d_{\ell-1},1 \le \ell \le k.$$
$$$$

*Proof.* Since by $(*_{4})$ we have $\Delta_{k}  = \delta_{k}^{k} d_{k}, \delta_{k}^{k}$  ̸ $= 0$, (by Proposition 49.16) we have
$$\langle Ad_{\ell}, \Delta_{i} \rangle = 0,0 \le i < \ell \le k.$$
By $(*_{1})$ we have $\nabla J_{u\ell+1} = \nabla J_{u\ell} + A\Delta_{\ell}$ , and since $A$ is a symmetric matrix, we have
$$0 = \langle Ad_{k}, \Delta_{\ell} \rangle = \langle d_{k}, A\Delta_{\ell} \rangle = \langle d_{k}, \nabla J_{u\ell+1} -\nabla J_{u\ell}\rangle ,$$
for $\ell = 0, \dots  , k$ - $1$. Since
$$d_{k} = \sum_{i=0}^{k-1}  \lambda_{i}^{k}  \nabla J_{ui} + \nabla J_{uk},$$
we have
$$\sum_{i=0}^{k-1}  \lambda_{i}^{k}  \nabla J_{ui} + \nabla J_{uk}, \nabla J_{u\ell+1} -\nabla J_{u\ell}= 0,0 \le \ell \le k -1.$$
Since by Proposition 49.15 the gradients $\nabla J_{ui}$ are pairwise orthogonal, the above equations yield
$$+$$
$$-\lambda_{k-1}^{k}

$\nabla J_{uk-1}^{2}$

$\|\nabla J_{uk}\|^{2}=$ 0$$
$$+$$
$$-\lambda_{\ell}^{k} \|\nabla J_{u\ell}\|^{2} \lambda_{\ell+1}^{k}

$\nabla J_{u\ell+1}^{2}$

$=$ 0,0 $\le \ell \le k$ -2,k $\ge$ 2,$$

<!-- PAGE 1747 -->
and an easy induction yields
$$\|\nabla \|^{2}$$
$$\lambda_{i}^{k}  = \frac{J_{uk}}{\|\nabla J_{ui}\|^{2}} ,0 \le i \le k -1.$$
Consequently, using $(*_{3})$ we have
$$\|\nabla \|^{2}$$
$$d_{k} = \sum_{i=0}^{k-1}  \frac{J_{uk}}{\|\nabla J_{ui}\|^{2}} \nabla J_{ui} + \nabla J_{uk}$$
$$\nabla

!$$
$$\|\nabla \|^{2}$$
$$= \nabla J_{uk} + \frac{J_{uk}}{\nabla J_{uk-1}^{2}} \sum_{i=0}^{k-2}  \frac{J_{uk-1}^{2}}{\|\nabla J_{ui}\|^{2}} \nabla J_{ui} + \nabla J_{uk-1}$$
$$\|\nabla \|^{2}$$
$$= \nabla J_{uk} + \frac{J_{uk}}{\nabla J_{uk-1}^{2}} d_{k-1},$$
which concludes the proof. It remains to compute $\rho_{k}$ , which is the solution of the line search
$$J(u_{k} -\rho_{k} d_{k}) = \inf J(u_{k} -\rho d_{k}).$$
$$\rho \in \mathbb{R}$$
Since $J$ is a quadratic functional, a basic computation left to the reader shows that the function to be minimized is
$$\rho  \mapsto \frac{\rho^{2}}{2} \langle Ad_{k}, d_{k}\rangle -\rho \langle \nabla J_{uk}, d_{k}\rangle + J(u_{k}),$$
whose mininum is obtained when its derivative is zero, that is,
$$\langle \nabla \rangle$$
$$\rho_{k}  = \frac{J_{uk}, d_{k}}{\langle Ad_{k}, d_{k}\rangle} .(*_{5})$$
In summary, the conjugate gradient method finds the minimum $u$ of the elliptic quadratic functional
$$J(v) = \frac{1}{2} \langle Av, v\rangle -\langle b, v\rangle$$
by computing the sequence of vectors $u_{1}, d_{1}, \dots  , u_{k-1}, d_{k-1}, u_{k}$, starting from any vector $u_{0}$, with
$$d_{0} = \nabla J_{u0}.$$
If $\nabla J_{u0} = 0$, then the algorithm terminates with $u = u_{0}$. Otherwise, for $k \ge 0$, assuming that $\nabla J_{ui}$ ̸ $= 0$ for $i = 1, \dots  , k$, compute
$$ \langle \nabla \rangle$$
$$\rho_{k}  = \frac{J_{uk}, d_{k}}{\langle Ad_{k}, d_{k}\rangle}$$
$$$$
$$$$
$$u_{k+1} = u_{k} -\rho_{k} d_{k}$$
$$(*_{6})$$
$$

$\nabla$$$
$$$$
$$d_{k+1} = \nabla J_{uk+1} + \frac{J_{uk+1}^{2}}{\|\nabla J_{uk}\|^{2}} d_{k}.$$
$$$$

<!-- PAGE 1748 -->
If $\nabla J_{uk+1} = 0$, then the algorihm terminates with $u = u_{k+1}$. As we showed before, the algorithm terminates in at most $n$ iterations.

> **Example 49.3.** Let us take the example of Section 49.6 and apply the conjugate gradient procedure. Recall that
$$J(x, y) = \frac{1}{2} \begin{pmatrix} x & y \end{pmatrix} \begin{pmatrix} 3 & 2 \\ 2 & 6 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} - \begin{pmatrix} 2 & -8 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}$$
$$+ 2 -$$
$$= \frac{3}{2} x^{2}xy + 3y^{2}2x + 8y.$$
Note that $\nabla J_{v} =$ (3x $+$ 2y - $2$, 2x $+$ 6y $+ 8)$, Initialize the procedure by setting
$$u_{0} = (-2, -2),d_{0} = \nabla J_{u0} = (-12, -8)$$
Step $1$ involves calculating
$$\langle \nabla \rangle$$
$$\rho_{0}  = \frac{J_{u0}, d_{0}}{\langle Ad_{0}, d_{0}\rangle} = \frac{13}{75}$$
$$u_{1} = u_{0} -\rho_{0} d_{0} = (-2, -2) - \frac{13}{75} (-12, -8) = \begin{pmatrix} 2 & 46 \\ , - \\ 25 & 75 \end{pmatrix}$$
$$||\nabla ||^{2}$$
$$d_{1} = \nabla J_{u1} + \frac{J_{u1}}{||\nabla J_{u0}||^{2}} d_{0} = \begin{pmatrix} 2912 18928 \\ - & , \\ 625 & \overline{5625} \end{pmatrix} .$$
Observe that $\rho_{0}$  and $u_{1}$ are precisely the same as in the case the case of gradient descent with optimal step size parameter. The difference lies in the calculation of $d_{1}$. As we will see, this change will make a huge difference in the convergence to the unique minimum $u = (2, -2)$. We continue with the conjugate gradient procedure and calculate Step $2$ as
$$\langle \nabla \rangle$$
$$\rho_{1}  = \frac{J_{u1}, d_{1}}{\langle Ad_{1}, d_{1}\rangle} = \frac{75}{82}$$
$$u_{2} = u_{1} -\rho_{1} d_{1} = \begin{pmatrix} 2 & 46 \\ , - \\ 25 & 75 \end{pmatrix} - \frac{75}{82} \begin{pmatrix} 2912 18928 \\ - & , \\ 625 & \overline{5625} \end{pmatrix} = (2, -2)$$
$$||\nabla ||^{2}$$
$$d_{2} = \nabla J_{u2} + \frac{J_{u2}}{||\nabla J_{u1}||^{2}} d_{1} = (0, 0).$$
Since $\nabla J_{u2} = 0$, the procedure terminates in two steps, as opposed to the $31$ steps needed for gradient descent with optimal step size parameter. Hestenes and Stiefel realized that Equations $(*_{6})$ can be modified to make the computations more efficient, by having only one evaluation of the matrix $A$ on a vector, namely $d_{k}$. The idea is to compute $\nabla_{uk}$  inductively.

<!-- PAGE 1749 -->
Since by $(*_{1})$ and $(*_{4})$ we have $\nabla J_{u\ell+1} = \nabla J_{u\ell} + A\Delta_{\ell} = \nabla J_{u\ell}$ - $\rho_{\ell} Ad_{\ell}$, the gradient $\nabla J_{u\ell+1}$ can be computed iteratively:
$$\nabla J_{0} = Au_{0} -b$$
$$\nabla J_{u\ell+1} = \nabla J_{u\ell}-\rho_{\ell} Ad_{\ell}.$$
Since by Proposition 49.17 we have
$$\|\nabla \|^{2}$$
$$d_{k} = \nabla J_{uk} + \frac{J_{uk}}{\nabla J_{uk-1}^{2}} d_{k-1}$$
and since $d_{k-1}$ is a linear combination of the gradients $\nabla J_{ui}$ for $i = 0, \dots  , k$ - $1$, which are all orthogonal to $\nabla J_{uk}$, we have
$$\langle \nabla \rangle  \|\nabla \|^{2}$$
$$\rho_{k}  = \frac{J_{uk}, d_{k}}{\langle Ad_{k}, d_{k}\rangle} = \frac{J_{uk}}{\langle Ad_{k}, d_{k}\rangle} .$$
It is customary to introduce the term $r_{k}$ defined as
$$r_{k} = \nabla J_{uk} = Au_{k} -b(*_{7})$$
and to call it the residual. Then the conjugate gradient method consists of the following steps. We intitialize the method starting from any vector $u_{0}$ and set
$$d_{0} = r_{0} = Au_{0} -b.$$
The main iteration step is $(k \ge 0)$:
$$\|\|^{2}$$
$$\rho_{k}  = \frac{r_{k}}{\langle Ad_{k}, d_{k}\rangle}$$
$$$$
$$$$
$$$$
$$u_{k+1} = u_{k} -\rho_{k} d_{k}$$
$$$$
$$$$
$$$$
$$$$
$$(*_{8})r_{k+1} = r_{k}\rho_{k} Ad_{k}$$
$$ \|\|^{2}$$
$$$$
$$\beta_{k+1}  = \frac{r_{k+1} -}{\|r_{k}\|^{2}}$$
$$$$
$$$$
$$$$
$$$$
$$d_{k+1} = r_{k+1} + \beta_{k+1}  d_{k}.$$
$$$$
 Beware that some authors define the residual $r_{k}$ as $r_{k} = b-Au_{k}$ and the descent direction $d_{k}$ as $-d_{k}$. In this case, the second equation becomes
$$u_{k+1} = u_{k} + \rho_{k} d_{k}.$$
Since $d_{0} = r_{0}$, the equations
$$r_{k+1} = r_{k} -\rho_{k} Ad_{k}$$
$$d_{k+1} = r_{k+1} + \beta_{k+1} d_{k}$$

<!-- PAGE 1750 -->
imply by induction that the subspace $\mathcal{G}_{k}$ is spanned by $(r_{0}, r_{1}, \dots  , r_{k})$ and $(d_{0}, d_{1}, \dots  , d_{k})$ is the subspace spanned by
$$(r_{0}, Ar_{0}, A^{2}r_{0}, \dots  , A^{k}r_{0}).$$
Such a subspace is called a Krylov subspace. If we define the error $e_{k}$ as $e_{k} = u_{k}$ - $u$, then $e_{0} = u_{0}$ - $u$ and $Ae_{0} = Au_{0}$ - Au $= Au_{0}$ - $b = d_{0} = r_{0}$, and then because
$$u_{k+1} = u_{k} -\rho_{k} d_{k}$$
we see that
$$e_{k+1} = e_{k} -\rho_{k} d_{k}.$$
Since $d_{k}$ belongs to the subspace spanned by $(r_{0}, Ar_{0}, A^{2}r_{0}, \dots  , A^{k}r_{0})$ and $r_{0} = Ae_{0}$, we see that $d_{k}$ belongs to the subspace spanned by $(Ae_{0}, A^{2}e_{0}, A^{3}e_{0}, \dots  , A^{k+1}e_{0})$, and then by induction we see that $e_{k+1}$ belongs to the subspace spanned by $(e_{0}, Ae_{0}, A^{2}e_{0}, A^{3}e_{0}, \dots  , A^{k+1}e_{0})$. This means that there is a polynomial $P_{k}$ of degree $\le k$ such that $P_{k}(0) = 1$ and
$$e_{k} = P_{k}(A)e_{0}.$$
This is an important fact because it allows for an analysis of the convergence of the conjugate gradient method; see Trefethen and Bau $[182]$ (Lecture $38)$. For this, since $A$ is
$$\mathbb{R}^{n}$$
symmetric positive definite, we know that $\langle u, v\rangle_{A}  = \langle$ Av, $u\rangle$ is an inner product on whose associated norm is denoted by $\|v\|_{A}$. Then observe that if e(v) $= v$ - $u$, then
$$\|e(v)\|_{A}^{2} = \langle Av -Au, v -u\rangle$$
$$= \langle Av, v\rangle -2\langle Au, v\rangle + \langle Au, u\rangle$$
$$= \langle Av, v\rangle -2\langle b, v\rangle + \langle b, u\rangle$$
$$= 2J(v) + \langle b, u\rangle .$$
It follows that $v = u_{k}$ minimizes $\|e(v)\|_{A}$ on $u_{k-1}+\mathcal{G}_{k-1}$ since $u_{k}$ minimizes $J$ on $u_{k-1}+\mathcal{G}_{k-1}$. Since $e_{k} = P_{k}(A)e_{0}$ for some polynomial $P_{k}$ of degree $\le k$ such that $P_{k}(0) = 1$, if we let $\mathcal{P}_{k}$ be the set of polynomials P(t) of degree $\le k$ such that P(0) $= 1$, then we have
$$\|e_{k}\|_{A} = \inf \|P(A)e_{0}\|_{A} .$$
$$P\in Pk$$
Since $A$ is a symmetric positive definite matrix it has real positive eigenvalues $\lambda_{1} , \dots  , \lambda_{n}$  and
$$there is an orthonormal basis of eigenvectors h_{1}, \dots  , h_{n} so that if we write e_{0} = \sum_{j}  n=1 a_{j}h_{j}.$$
then we have
$$\|e_{0}\|_{A}^{2} = \langle Ae_{0}, e_{0}\rangle = \sum_{i=1}^{n}  a_{i}\lambda_{i} h_{i}, \sum_{j=1}^{n}  a_{j}h_{j}= \sum_{j=1}^{n}  a_{j}^{2}\lambda_{j}$$
and
$$\|P(A)e_{0}\|_{A}^{2} = \langle AP(A)e_{0}, P(A)e_{0}\rangle = \sum_{i=1}^{n}  a_{i}\lambda_{i} P(\lambda_{i} )h_{i}, \sum_{j=1}^{n}  a_{j}P(\lambda_{j} )h_{j}= \sum_{j=1}^{n}  a_{j}^{2}\lambda_{j} (P(\lambda_{j} ))^{2}.$$

<!-- PAGE 1751 -->
These equations imply that
$$\|e_{k}\|_{A} \le \begin{pmatrix} \inf & \max|P(\lambda_{i} )| \\ P\in Pk1\le i\le n \end{pmatrix} \|e_{0}\|_{A} .$$
It can be shown that the conjugate gradient method requires of the order of $n^{3}$ additions, $n^{3}$ multiplications, 2n divisions. In theory, this is worse than the number of elementary operations required by the Cholesky method. Even though the conjugate gradient method does not seem to be the best method for full matrices, it usually outperforms other methods for sparse matrices. The reason is that the matrix $A$ only appears in the computation of the vector $Ad_{k}$. If the matrix $A$ is banded (for example, tridiagonal), computing $Ad_{k}$ is very cheap and there is no need to store the entire matrix $A$, in which case the conjugate gradient method is fast. Also, although in theory, up to $n$ iterations may be required, in practice, convergence may occur after a much smaller number of iterations. Using the inequality
$$\|e_{k}\|_{A} \le \begin{pmatrix} \inf & \max|P(\lambda_{i} )| \\ P\in Pk1\le i\le n \end{pmatrix} \|e_{0}\|_{A} ,$$
by choosing $P$ to be a shifted Chebyshev polynomial, it can be shown that
$$1^{k}$$
$$\|e_{k}\|_{A} \le 2 \begin{pmatrix} \sqrt \\ \sqrt{\kappa} - \\ \overline{\kappa} + 1 \end{pmatrix} \|e_{0}\|_{A} ,$$
where $\kappa  = cond_{2}(A)$; see Trefethen and Bau $[182]$ (Lecture $38$, Theorem 38.5). Thus the rate of convergence of the conjugate gradient method is governed by the ratio
$$\frac{p\overline{cond}_{2}\overline{(}\overline{A}\overline{)} 1}{p\overline{cond}_{2}\overline{(}\overline{A}\overline{) + 1}} -,$$
where $cond_{2}(A) = \lambda_{n} /\lambda_{1}$  is the condition number of the matrix $A$. Since $A$ is positive definite, $\lambda_{1}$  is its smallest eigenvalue and $\lambda_{n}$  is its largest eigenvalue. The above fact leads to the process of preconditioning, a method which consists in replacing the matrix of a linear system Ax $= b$ by an “equivalent” one for example $M^{-1} A$ (since $M$ is invertible, the system Ax $= b$ is equivalent to the system $M^{-1}$ Ax $= M^{-1} b)$, where $M$ is chosen so that $M^{-1} A$ is still symmetric positive definite and has a smaller condition number than $A$; see Trefethen and Bau $[182]$ (Lecture $40)$ and Demmel $[48]$ (Section 6.6.5).
