# Newton's Method For Finding a Minimum


<!-- PAGE 1737 -->
the method is determined by the largest and the smallest eigenvalues of $A$. Strang discusses this issue in the case of a $2 \times  2$ matrix. Convergence is significantly accelerated. Another method is known as Nesterov acceleration. In this method,
$$u_{k+1} = u_{k} + \beta (u_{k} -u_{k-1}) -\rho \nabla J_{uk+\gamma(uk-uk-1)},$$
where $\beta , \rho , \gamma$  are parameters. For details, see Strang $[177]$ (Chapter VI, Section $4)$. Lax also discusses other methods in which the step $\rho_{k}$  is chosen using roots of Chebyshev polynomials; see Lax $[117]$, Chapter $17$, Sections 2–4. A variant of Newton’s method described in Section 41.2 can be used to find the minimum of a function belonging to a certain class of strictly convex functions. This method is the special case of the case where the norm is induced by a symmetric positive definite matrix $P$, namely $P = \nabla^{2}$ J(x), the Hessian of $J$ at $x$.

## 49.9 Newton’s Method For Finding a Minimum

$$\mathbb{R} \mathbb{R}^{n}$$
If $J$ : $\Omega \to$  is a convex function defined on some open subset $\Omega$ of which is twice differentiable and if its Hessian $\nabla^{2}$ J(x) is symmetric positive definite for all $x \in \Omega$ , then by Proposition 40.12(2), the function $J$ is strictly convex. In this case, for any $x \in \Omega$ , we have the quadratic norm induced by $P = \nabla^{2}$ J(x) as defined in the previous section, given by
$$\|u\|_{\nabla2J(x)} = (u^{\top}\nabla^{2} J(x) u)^{1/2}.$$
The steepest descent direction for this quadratic norm is given by
$$d_{nt} = -(\nabla^{2} J(x))^{-1}\nabla J_{x}.$$
The norm of $d_{nt}$ for the the quadratic norm defined by $\nabla^{2}$ J(x) is given by
$$(d_{nt}^{\top}\nabla^{2} J(x) d_{nt})^{1/2}= \begin{pmatrix} -(\nabla J_{x})^{\top}(\nabla^{2} J(x))^{-1}\nabla^{2} J(x)(-(\nabla^{2} J(x))^{-1}\nabla J_{x} \\ ( & J_{x})^{\top}( & J(x))^{-1} & J_{x}^{1/2} . \end{pmatrix} )^{1/2}$$
$$= \begin{pmatrix} \nabla & \nabla^{2} & \nabla \\ \mathbb{R} \end{pmatrix}$$

> **Definition 49.9.** Given a function $J$ : $\Omega \to$  as above, for any $x \in \Omega$ , the Newton step $d_{nt}$ is defined by
$$d_{nt} = -(\nabla^{2} J(x))^{-1}\nabla J_{x},$$
and the Newton decrement $\lambda (x)$ is defined by
$$.$$
$$\lambda (x) = \begin{pmatrix} (\nabla J_{x})^{\top}(\nabla^{2} J(x))^{-1}\nabla \end{pmatrix} J_{x}^{1/2}$$
Observe that
$$\langle \nabla J_{x}, d_{nt}\rangle = (\nabla J_{x})^{\top}(-(\nabla^{2} J(x))^{-1}\nabla J_{x}) = -\lambda (x)^{2}.$$

<!-- PAGE 1738 -->
If $\nabla J_{x} \neq  0$, we have $\lambda (x) \neq  0$, so $\langle \nabla J_{x}, d_{nt}\rangle < 0$, and $d_{nt}$ is indeed a descent direction. The number $\langle \nabla J_{x}, d_{nt}\rangle$ is the constant that shows up during a backtracking line search. A nice feature of the Newton step and of the Newton decrement is that they are affine invariant. This means that if $T$ is an invertible matrix and if we define $g$ by g(y) $=$ J(Ty), if the Newton step associated with $J$ is denoted by $d_{J,nt}$ and similarly the Newton step associated with $g$ is denoted by $d_{g,nt}$, then it is shown in Boyd and Vandenberghe $[29]$ (Section 9.5.1) that
$$d_{g,nt} = T^{-1} d_{J,nt},$$
and so
$$x + d_{J,nt} = T(y + d_{g,nt}).$$
A similar properties applies to the Newton decrement. Newton’s method consists of the following steps: Given a starting point $u_{0} \in$ dom(J) and a tolerance $\epsilon  > 0$ do: repeat
$(1)$ Compute the Newton step and decrement $d_{nt,k} = -(\nabla^{2} J(u_{k}))^{-1}\nabla J_{uk}$ and $\lambda (u_{k})^{2} = (\nabla J_{uk})^{\top}(\nabla^{2} J(u_{k}))^{-1}\nabla J_{uk}$.
$(2)$ Stopping criterion. quit if $\lambda (u_{k})^{2}/2 \le \epsilon$ .
$(3)$ Line Search. Perform an exact or backtracking line search to find $\rho_{k}$ .
$(4)$ Update. $u_{k+1} = u_{k} + \rho_{k} d_{nt,k}$. Observe that this is essentially the descent procedure of Section 49.8 using the Newton step as search direction, except that the stopping criterion is checked just after computing the search direction, rather than after the update (a very minor difference). The convergence of Newton’s method is thoroughly analyzed in Boyd and Vandenberghe $[29]$ (Section 9.5.3). This analysis is made under the following assumptions:
$(1)$ The function $J$ : $\Omega \to \mathbb{R}$ is a convex function defined on some open subset $\Omega$ of $\mathbb{R}^{n}$ which is twice differentiable and its Hessian $\nabla^{2}$ J(x) is symmetric positive definite for all $x \in \Omega$ . This implies that there are two constants $m > 0$ and $M > 0$ such that mI $⪯\nabla^{2}$ J(x) ⪯ MI for all $x \in \Omega$ , which means that the eigenvalues of $\nabla^{2}$ J(x) belong to $[m, M]$.
$(2)$ The Hessian is Lipschitzian, which means that there is some $L \ge 0$ such that
$$\nabla^{2} J(x) -\nabla^{2} J(y)_{2} \le L \|x, y\|_{2}for all x, y \in \Omega .$$
It turns out that the iterations of Newton’s method fall into two phases, depending whether $\|\nabla J_{uk}\|_{2} \ge \eta$  or $\|\nabla J_{uk}\|_{2} < \eta$ , where $\eta$  is a number which depends on $m, L$, and the constant $\alpha$  used in the backtracking line search, and $\eta  \le m^{2}/L$.

<!-- PAGE 1739 -->
$(1)$ The first phase, called the damped Newton phase, occurs while $\|\nabla J_{uk}\|_{2} \ge \eta$ . During this phase, the procedure can choose a step size $\rho_{k}  = t < 1$, and there is some constant $\gamma  > 0$ such that
$$J(u_{k+1}) -J(u_{k}) \le -\gamma .$$
$(2)$ The second phase, called the quadratically convergent phase or pure Newton phase, occurs while $\|\nabla J_{uk}\|_{2} < \eta$ . During this phase, the step size $\rho_{k}  = t = 1$ is always chosen, and we have
$$2$$
$$\frac{L}{2m^{2}} \nabla J_{uk+12} \le \begin{pmatrix} L \\ \|\nabla J_{uk}\|_{2} \\ 2m^{2} \end{pmatrix} .(*_{1})$$
If we denote the minimal value of $f$ by $p^{*}$, then the number of damped Newton steps is at most
$$\frac{J(u_{0})p^{*}}{\gamma} -.$$
Equation $(*_{1})$ and the fact that $\eta  \le m^{2}/L$ shows that if $\|\nabla J_{uk}\|_{2} < \eta$ , then

$\nabla J_{uk+12} < \eta$ . It follows by induction that for all $\ell \ge k$, we have
$$2$$
$$\frac{L}{2m^{2}} \nabla J_{u\ell+12} \le \begin{pmatrix} L \\ \|\nabla J_{u\ell}\|_{2} \\ 2m^{2} \end{pmatrix} ,(*_{2})$$
and thus (since $\eta  \le m^{2}/L$ and $\|\nabla J_{uk}\|_{2} < \eta$ , we have $(L/m^{2}) \|\nabla J_{uk}\|_{2} < (L/m^{2})\eta  \le 1)$, so
$$2\ell -k$$
$$1^{2\ell-k}$$
$$\frac{L}{2m^{2}} \|\nabla J_{u\ell}\|_{2} \le \begin{pmatrix} L \\ \|\nabla J_{uk}\|_{2} \\ 2m^{2} \end{pmatrix} \le \begin{pmatrix} \overline{2} \end{pmatrix} ,\ell \ge k.(*_{3})$$
It is shown in Boyd and Vandenberghe $[29]$ (Section 9.1.2) that the hypothesis mI $⪯\nabla^{2}$ J(x) implies that
$$J(x) -p^{*}\le \frac{1}{2m} \|\nabla J_{x}\|_{2}^{2}x \in \Omega .$$
As a consequence, by $(*_{3})$, we have
$$1^{2\ell-k+1}$$
$$J(u_{\ell}) -p^{*}\le \frac{1}{2m} \|\nabla J_{u\ell}\|_{2}^{2} \le \frac{2m^{3}}{L^{2}} \begin{pmatrix} \overline{2} \end{pmatrix} .(*_{4})$$
Equation $(*_{4})$ shows that the convergence during the quadratically convergence phase is very fast. If we let
$$\epsilon_{0}  = \frac{2m^{3}}{L^{2}} ,$$
then Equation $(*_{4})$ implies that we must have $J(u_{\ell})$ - $p^{*} \le \epsilon$  after no more than
$$log_{2} log_{2}(\epsilon_{0} /\epsilon )$$

<!-- PAGE 1740 -->
iterations. The term $log_{2} log_{2}(\epsilon_{0} /\epsilon$ ) grows extremely slowly as $\epsilon$  goes to zero, and for practical purposes it can be considered constant, say five or six (six iterations gives an accuracy of about $\epsilon  \approx 5 \cdot  10^{-20}\epsilon_{0}$ ). In summary, the number of Newton iterations required to find a minimum of $J$ is approximately bounded by
$$\frac{J(u_{0})p^{*}}{\gamma} -+ 6.$$
Examples of the application of Newton’s method and further discussion of its efficiency are given in Boyd and Vandenberghe $[29]$ (Section 9.5.4). Basically, Newton’s method has a faster convergence rate than gradient or steepest descent. Its main disadvantage is the cost for forming and storing the Hessian, and of computing the Newton step, which requires solving a linear system. There are two major shortcomings of the convergence analysis of Newton’s method as sketched above. The first is a pracical one. The complexity estimates involve the constants $m, M$, and $L$, which are almost never known in practice. As a result, the bound on the number of steps required is almost never known specifically. The second shortcoming is that although Newton’s method itself is affine invariant, the analysis of convergence is very much dependent on the choice of coordinate system. If the coordinate system is changed, the constants $m, M, L$ also change. This can be viewed as an aesthetic problem, but it would be nice if an analysis of convergence independent of an affine change of coordinates could be given. Nesterov and Nemirovski discovered a condition on functions that allows an affineinvariant convergence analysis. This property, called self-concordance, is unfortunately not very intuitive.

> **Definition 49.10.** A (partial) convex function $f$ defined on $\mathbb{R}$ is self-concordant if
$$|f''' (x)| \le 2(f'' (x))^{3/2}for all x \in \mathbb{R}.$$
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
A (partial) convex function $f$ defined on is self-concordant if for every nonzero $v \in$ and all $x \in \mathbb{R}^{n}$, the function $t \mapsto$ J(x $+$ tv) is self-concordant. Affine and convex quadratic functions are obviously self-concordant, since f''' $= 0$. There are many more interesting self-concordant functions, for example, the function $X \mapsto$ -log det(X), where $X$ is a symmetric positive definite matrix. Self-concordance is discussed extensively in Boyd and Vandenberghe $[29]$ (Section 9.6). The main point of self-concordance is that a coordinate system-invariant proof of convergence can be given for a certain class of strictly convex self-concordant functions. This proof is given in Boyd and Vandenberghe $[29]$ (Section 9.6.4). Given a starting value $u_{0}$, we assume
$$\mathbb{R}^{n}$$
that the sublevel set ${x \in$ | J(x) $\le J(u_{0})}$ is closed and that $J$ is bounded below. Then there are two parameters $\eta$  and $\gamma$  as before, but depending only on the parameters $\alpha , \beta$ involved in the line search, such that:
