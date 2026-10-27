# Problems


<!-- PAGE 1758 -->
$\bullet$  Newton’s method. $\bullet$  Newton step. $\bullet$  Newton decrement. $\bullet$  Damped Newton phase. $\bullet$  Quadratically convergent phase. $\bullet$  Self-concordant functions. $\bullet$  Conjugate gradient method. $\bullet$  Projected gradient methods. $\bullet$  Penalty methods.

## 49.14 Problems

$$\mathbb{R}^{n} \mathbb{R}$$
Problem 49.1. Consider the function $J$ : $\to$  given by
$$J(v) = \frac{1}{2} \langle Av, v\rangle -\langle b, v\rangle + g(v),$$
$$\mathbb{R}^{n} \mathbb{R}^{n} \mathbb{R}$$
where $A$ is a real $n \times  n$ symmetric positive definite matrix, $b \in$ , and $g: \to$  is a continuous (not necessarily differentiable) convex function such that g(v) $\ge 0$ for all $v \in \mathbb{R}^{n}$, and let $U$ be a nonempty, bounded, closed, convex subset of $\mathbb{R}^{n}$.
$(1)$ Prove that there is a unique element $u \in U$ such that
$$J(u) = \inf J(v).$$
$$v\in U$$
Hint. Prove that $J$ is strictly convex on $\mathbb{R}^{n}$.
$(2)$ Check that
$$J(v) -J(u) = \langle Au -b, v -u\rangle + g(v) -g(u) + \frac{1}{2} \langle A(v -u), v -u\rangle .$$
Prove that an element $u \in U$ minimizes $J$ in $U$ iff
$$\langle Au -b, v -u\rangle + g(v) -g(u) \ge 0for all v \in U.$$
$$\mathbb{R}$$
Problem 49.2. Consider $n$ piecewise $C^{1}$ functions $\phi_{i}$  : $[0, 1] \to$  and assume that these functions are linearly independent and that
$$\sum_{i=1}^{n}  \phi_{i} (x) = 1for all x \in [0, 1].$$

<!-- PAGE 1759 -->
$$\mathbb{R}^{n} \mathbb{R}$$
Let $J$ : $\to$  be the function given by
$$J(v) = \sum_{i,j=1}^{n}  a_{ij}v_{i}v_{j} + \sum_{i=1}^{n}  b_{i}v_{i},$$
where $v = (v_{1}, \dots  , v_{n})$ and
$$a_{ij} = \int_{0}^{}  1\phi_{i}' (t)\phi_{j}' (t)dt,b_{i} = \int_{0}^{}  1\phi_{i} (t)dt.$$
$$\mathbb{R}^{n}$$
$(1)$ Let $U_{1}$ be the subset of given by
$$U_{1} = \begin{pmatrix} v\in \mathbb{R}^{n}| & b_{i}v_{i}= 0 \end{pmatrix} \sum_{i=1}^{n}  .$$
Consider the problem of finding a minimum of $J$ over $U_{1}$. Prove that the Lagrange multiplier $\lambda$  for which the Lagrangian has a critical point is $\lambda  = -1$.
$(2)$ Prove that the map defined on $U_{1}$ by
$$1/2$$
$$\|v\|= \begin{pmatrix} 1 & !2 \\ v_{i}\phi_{i}' (x) & dx \end{pmatrix} \int_{0}^{}  \sum_{i=1}^{n}$$
is a norm. Prove that $J$ is elliptic on $U_{1}$ with this norm. Prove that $J$ has a unique minimum on $U_{1}$.
$$\mathbb{R}^{n}$$
$(3)$ Consider the the subset of given by
$$U_{2} = \begin{pmatrix} v\in \mathbb{R}^{n}| & (\phi_{i} (1) + \phi_{i} (0))v_{i}= 0 \end{pmatrix} \sum_{i=1}^{n}  .$$
Consider the problem of finding a minimum of $J$ over $U_{2}$. Prove that the Lagrange multiplier $\lambda$  for which the Lagrangian has a critical point is $\lambda  = -1/2$. Prove that $J$ is elliptic on $U_{2}$ with the same norm as in $(2)$. Prove that $J$ has a unique minimum on $U_{2}$.
$$\mathbb{R}^{n}$$
$(4)$ Consider the the subset of given by
$$U_{3} = \begin{pmatrix} v\in \mathbb{R}^{n}| & (\phi_{i} (1) -\phi_{i} (0))v_{i}= 0 \end{pmatrix} \sum_{i=1}^{n}  .$$
This time show that the necessary condition for having a minimum on $U_{3}$ yields the equation $1 + \lambda (1$ - $1) = 0$. Conclude that $J$ does not have a minimum on $U_{3}$.

<!-- PAGE 1760 -->
Problem 49.3. Let $A$ be a real $n \times  n$ symmetric positive definite matrix and let $b \in \mathbb{R}^{n}$.
$(1)$ Prove that if we apply the steepest descent method (for the Euclidean norm) to
$$J(v) = \frac{1}{2} \langle Av, v\rangle -\langle b, v\rangle ,$$
and if we define the norm $\|v\|_{A}$ by
$$\|v\|_{A} = \langle Av, v\rangle^{1/2} ,$$
we get the inequality
$$!$$
$$\| -\|_{2}^{4}$$
$$\|u_{k+1} -u\|_{A}^{2} \le \|u_{k} -u\|_{A}^{2}1 - \frac{A(u_{k}u)}{\|u_{k} -u\|_{A}^{2}\|A(u_{k} -u)\|_{A}^{2}} .$$
$(2)$ Using a diagonalization of $A$, where the eigenvalues of $A$ are denoted $0 < \lambda_{1}  \le \lambda_{2}  \le \cdots  \le \lambda_{n}$ , prove that
$$-$$
$$\|u_{k+1} -u\|_{A} \le \frac{cond_{2}(A)1}{cond_{2}(A) + 1} \|u_{k} -u\|_{A} ,$$
where $cond_{2}(A) = \lambda_{n} /\lambda_{1}$ , and thus
$$1^{k}$$
$$\|u_{k} -u\|_{A} \le \begin{pmatrix} cond_{2}(A) - \\ cond_{2}(A) + 1 \end{pmatrix} \|u_{0} -u\|_{A} .$$
$(3)$ Prove that when $cond_{2}(A) = 1$, then $A =$ I and the method converges in one step.
$$\mathbb{R}^{n} \mathbb{R}$$
Problem 49.4. Prove that the method of Polak–Ribi`ere converges if $J$ : $\to$  is elliptic and a $C^{2}$ function.
Problem 49.5. Prove that the backtracking line search method described in Section 49.5 has the property that for $t$ small enough the condition $J(u_{k}+td_{k}) \le J(u_{k})+\alpha t\langle \nabla J_{uk}, d_{k}\rangle$ will hold and the search will stop. Prove that the exit inequality $J(u_{k} + td_{k}) \le J(u_{k}) + \alpha t\langle \nabla J_{uk}, d_{k}\rangle$ holds for all $t \in (0, t_{0}]$, for some $t_{0} > 0$, so the backtracking line search stops with a step length $\rho_{k}$  that satisfies $\rho_{k}  = 1$ or $\rho_{k}  \in (\beta t_{0}, t_{0}]$.
Problem 49.6. Let $d_{nsd,k}$ and $d_{sd,k}$ be the normalized and unnormalized descent directions of the steepest descent method for an arbitrary norm (see Section 49.8). Prove that
$$\langle \nabla J_{uk}, d_{nsd,k}\rangle = -\|\nabla J_{uk}\|^{D}$$
$$\langle \nabla J_{uk}, d_{sd,k}\rangle = -(\|\nabla J_{uk}\|^{D})^{2}$$
$$d_{sd,k} = arg minv \begin{pmatrix} 1 \\ \langle \nabla J_{uk}, v\rangle + & \|v\|^{2} \\ 2 \end{pmatrix} .$$

<!-- PAGE 1761 -->
Problem 49.7. If $P$ is a symmetric positive definite matrix, prove that $\|z\|_{P} = (z^{\top}Pz)^{1/2} = P^{1/2}z_{2}$ is a norm. Prove that the normalized steepest descent direction is
$$d_{nsd,k} = -(\nabla J_{uk}^{\top}P^{-1}\nabla J_{uk})^{-1/2}P^{-1}\nabla J_{uk},$$
the dual norm is $\|z\|^{D} =$

$P^{-1/2}z_{2}$, and the steepest descent direction with respect to $\|\|_{P}$ is given by
$$d_{sd,k} = -P^{-1} \nabla J_{uk}.$$
Problem 49.8. If $\|\|$ is the $\ell^{1}$ -norm, then show that $d_{nsd,k}$ is determined as follows: let $i$ be any index for which $\|\nabla J_{uk}\|_{\infty} = |(\nabla J_{uk})_{i}|$. Then
$$d_{nsd,k} = -sign \begin{pmatrix} \partial J \\ (u_{k}) \\ \partial x_{i} \end{pmatrix} e_{i},$$
where $e_{i}$ is the ith canonical basis vector, and
$$d_{sd,k} = - \frac{\partial J}{\partial x_{i}} (u_{k})e_{i}.$$
Problem 49.9. (From Boyd and Vandenberghe $[29]$, Problem 9.12). If $\nabla^{2}$ f(x) is singular (or very ill-conditioned), the Newton step $d_{nt} = -(\nabla^{2} J(x))^{-1}\nabla J_{x}$ is not well defined. Instead we can define a search direction $d_{tr}$ as the solution of the problem
$$minimize(1/2)\langle Hv, v\rangle + \langle g, v\rangle$$
$$subject to\|v\|_{2} \le \gamma ,$$
where $H = \nabla^{2} f_{x}, g = \nabla f_{x}$, and $\gamma$  is some positive constant. The idea is to use a trust region, which is the closed ball ${v$ | $\|v\|_{2} \le \gamma$ }. The point $x+d_{tr}$ minimizes the second-order approximation of $f$ at $x$, subject to the constraint that
$$\|x + d_{\mathrm{tr}} -x\|_{2} \le \gamma .$$
The parameter $\gamma$ , called the trust parameter, reflects our confidence in the second-order approximation. Prove that $d_{tr}$ minimizes
$$\frac{1}{2} \langle Hv, v\rangle + \langle g, v\rangle + \beta b \|v\|_{2}^{2} ,$$
for some $\beta$ .
$$b$$
Problem 49.10. (From Boyd and Vandenberghe $[29]$, Problem 9.9). Prove that the Newton decrement $\lambda (x)$ is given by
$$\langle \nabla \rangle$$
$$\lambda (x) = \sup- \frac{J_{x}, v}{(\langle \nabla^{2} J_{x}v, v\rangle )^{1/2}} .$$
$$v\neq 0$$

<!-- PAGE 1762 -->
Problem 49.11. Show that the function $f$ given by f(x) $= log(e^{x} + e^{-x})$ has a unique minimum for $x^{*} = 0$. Run Newton’s method with fixed step size $t = 1$, starting with $x_{0} = 1$, and then $x_{0} =$ 1.1. What do you observe?
Problem 49.12. Write a Matlab program implementing the conjugate gradient method. Test your program with the $n \times  n$ matrix
$$A_{n} = \begin{pmatrix} 2 & -1 & 0 & \cdots & 0 \\ -1 & 2 & -1 & \dots & 0 \\ \vdots & \ddots & \ddots & \ddots & \vdots \\ 0 & \cdots & -1 & 2 & -1 \\ 0 & \cdots & 0 & -1 & 2 \end{pmatrix}$$
and various right-hand sides, for various values of $n$. Verify that the running time is $O(n^{3/2})$.
