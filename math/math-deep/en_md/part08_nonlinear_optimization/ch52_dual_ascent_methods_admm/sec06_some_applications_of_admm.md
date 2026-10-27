# Some Applications of ADMM


<!-- PAGE 1927 -->
The above suggests that a reasonable termination criterion is that

$r^{k}$

and

$s^{k}$

should be small, namely that
$$r^{k}

$\le \epsilon^{pri}$ and

$s^{k}$

$\le \epsilon^{dual}$ ,$$ for some chosen feasibility tolerances $\epsilon^{pri}$ and $\epsilon^{dual}$ . Further discussion for choosing these parameters can be found in Boyd et al. $[28]$ (Section 3.3.1). Various extensions and variations of ADMM are discussed in Boyd et al. $[28]$ (Section 3.4). In order to accelerate convergence of the method, one may choose a different $\rho$  at each step (say $\rho^{k}$ ), although proving the convergence of such a method may be difficult. If we assume that $\rho^{k}$ becomes constant after a number of iterations, then the proof that we gave still applies. A simple scheme is this:
$$\tau^{incr}  \rho^{k} if

$r^{k}$

$> \mu$

$s^{k}$$$
$$$$
$$ > \mu$$
$$\rho^{k+1} =\rho^{k} /\tau^{decr}  if

$s^{k}$



$r^{k}$$$
$$\rho^{k} otherwise,$$
$$$$
where $\tau^{incr} > 1, \tau^{decr} > 1$, and $\mu  > 1$ are some chosen parameters. Again, we refer the interested reader to Boyd et al. $[28]$ (Section 3.4).

## 52.6 Some Applications of ADMM

Structure in $f, g, A$, and $B$ can often be exploited to yield more efficient methods for performing the x-update and the z-update. We focus on the x-update, but the discussion applies just as well to the z-update. Since $z$ and $\lambda$  are held constant during minimization over $x$, it is more convenient to use the scaled form of ADMM. Recall that
$$x^{k+1}= arg minx \begin{pmatrix} f(x) + (\rho /2) & Ax + Bz^{k} -c + u_{2}^{k2} \end{pmatrix}$$
(here we use $u$ instead of $\mu$ ), so we can express the x-update step as
$$x^{+}= arg minx \begin{pmatrix} f(x) + (\rho /2) \|Ax -v\|_{2}^{2} \end{pmatrix} ,$$
with $v = -Bz^{k} + c$ - $u^{k}$.

> **Example 52.7.** A first simplification arises when $A =$ I, in which case the x-update is
$$x^{+}= arg minx \begin{pmatrix} f(x) + (\rho /2) \|x -v\|_{2}^{2} \end{pmatrix} = prox_{f,\rho}(v).$$
The map $v \mapsto prox_{f,\rho}(v)$ is known as the proximity operator of $f$ with penalty $\rho$ . The above minimization is generally referred to as proximal minimization.

<!-- PAGE 1928 -->

> **Example 52.8.** When the function $f$ is simple enough, the proximity operator can be computed analytically. This is the case in particular when $f = I_{C}$, the indicator function of a nonempty closed convex set $C$. In this case, it is easy to see that
$$x^{+}= arg minx \begin{pmatrix} I_{C}(x) + (\rho /2) \|x -v\|_{2}^{2} \end{pmatrix} = \Pi_{C} (v),$$
the orthogonal projection of $v$ onto $C$. In the special case where $C =\mathbb{R}_{+}^{n}$ (the first orthant), then
$$x^{+}= (v)_{+},$$
the vector obtained by setting the negative components of $v$ to zero.

> **Example 52.9.** A second case where simplifications arise is the case where $f$ is a convex quadratic functional of the form
$$f(x) = \frac{1}{2} x^{\top}Px + q^{\top}x + r,$$
$$\mathbb{R}^{n} \mathbb{R}$$
where $P$ is an $n \times  n$ symmetric positive semidefinite matrix, $q \in$ and $r \in$ . In this case the gradient of the map
$$x \mapsto f(x) + (\rho /2) \|Ax -v\|_{2}^{2} = \frac{1}{2} x^{\top}Px + q^{\top}x + r + \frac{\rho}{2} x^{\top}(A^{\top}A)x -\rho x^{\top}A^{\top}v + \frac{\rho}{2} v^{\top}v$$
is given by
$$(P + \rho A^{\top}A)x + q -\rho A^{\top}v,$$
and since $A$ has rank $n$, the matrix $A^{\top}A$ is symmetric positive definite, so we get
$$x^{+}= (P + \rho A^{\top}A))^{-1}(\rho A^{\top}v -q).$$
Methods from numerical linear algebra can be used so compute $x^{+}$ fairly efficiently; see Boyd et al. $[28]$ (Section $4)$.

> **Example 52.10.** A third case where simplifications arise is the variation of the previous case where $f$ is a convex quadratic functional of the form
$$f(x) = \frac{1}{2} x^{\top}Px + q^{\top}x + r,$$
except that $f$ is constrained by equality constraints Cx $= b$, as in Section 50.4, which means
$$\mathbb{R}^{n}$$
that dom(f) $= {x \in$ | Cx $= b}$, and $A =$ I. The x-minimization step consists in minimizing the function
$$J(x) = \frac{1}{2} x^{\top}Px + q^{\top}x + r + \frac{\rho}{2} x^{\top}x -\rho x^{\top}v + \frac{\rho}{2} v^{\top}v$$
subject to the constraint
$$Cx = b,$$

<!-- PAGE 1929 -->
so by the results of Section 50.4, $x^{+}$ is a component of the solution of the KKT-system
$$\begin{pmatrix} P+ \rho I & C^{\top} \\ C & 0 \end{pmatrix} \begin{pmatrix} x^{+} \\ y \end{pmatrix} = \begin{pmatrix} -q + \rho v \\ b \end{pmatrix} .$$
The matrix $P + \rho$ I is symmetric positive definite, so the KKT-matrix is invertible. We can now describe how ADMM is used to solve two common problems of convex optimization.
$(1)$ Minimization of a proper closed convex function $f$ over a closed convex set $C$ in $\mathbb{R}^{n}$. This is the following problem
$$minimizef(x)$$
$$subject to x \in C,$$
which can be rewritten in ADMM form as
$$minimizef(x) + I_{C}(z)$$
$$subject to x -z = 0.$$
Using the scaled dual variable $u = \lambda /\rho$ , the augmented Lagrangian is
$$.$$
$$L_{\rho}(x, z, u) = f(x) + I_{C}(z) + \frac{\rho}{2} \|x -z + u\|_{2}^{2} - \frac{\rho}{2} \|u\|^{2}$$
In view of Example 52.8, the scaled form of ADMM for this problem is
$$x^{k+1}= arg minx \begin{pmatrix} f(x) + (\rho /2) & x -z^{k} + u_{2}^{k2} \end{pmatrix}$$
$$z^{k+1}= \Pi_{C} (x^{k+1}+ u^{k})$$
$$u^{k+1}= u^{k}+ x^{k+1}-z^{k+1}.$$
The x-update involves evaluating a proximal operator. Note that the function $f$ need not be differentiable. Of course, these minimizations depend on having efficient computational procedures for the proximal operator and the projection operator.
$(2)$ Quadratic Programming, Version $1$. Here the problem is
$$minimize \frac{1}{2} x^{\top}Px + q^{\top}x + r$$
$$subject to Ax = b, x \ge 0,$$
where $P$ is an $n \times  n$ symmetric positive semidefinite matrix, $q \in \mathbb{R}^{n}, r \in \mathbb{R}$, and $A$ is an $m \times  n$ matrix of rank $m$.

<!-- PAGE 1930 -->
The above program is converted in ADMM form as follows:
$$minimizef(x) + g(z)$$
$$subject to x -z = 0,$$
with
$$f(x) = \frac{1}{2} x^{\top}Px + q^{\top}x + r,dom(f) = {x \in \mathbb{R}^{n}| Ax = b},$$
and
$$g = I_{Rn+},$$
the indicator function of the positive $orthant\mathbb{R}_{+}^{n}$. In view of Example 52.8 and Example 52.10, the scaled form of ADMM consists of the following steps:
$$x^{k+1}= arg minx \begin{pmatrix} f(x) + (\rho /2) & x -z^{k} + u_{2}^{k2} \end{pmatrix}$$
$$z^{k+1}= (x^{k+1}+ u^{k})_{+}$$
$$u^{k+1}= u^{k}+ x^{k+1}-z^{k+1}.$$
The x-update involves solving the KKT equations
$$\begin{pmatrix} P+ \rho I & A^{\top} \\ A & 0 \end{pmatrix} \begin{pmatrix} x^{k+1} \\ y \end{pmatrix} = \begin{pmatrix} -q + \rho (z^{k} -u^{k}) \\ b \end{pmatrix} .$$
This is an important example because it provides one of the best methods for solving quadratic problems, in particular, the SVM problems discussed in Chapter $54$.
$(3)$ Quadratic Programming, Version $2$. This problem is similar to the previous one, except
$$\mathbb{R}^{n}$$
that the variable $x \in$ is not restricted to be nonnegative. The problem is
$$minimize \frac{1}{2} x^{\top}Px + q^{\top}x + r$$
$$subject to Ax = b,$$
where $P$ is an $n \times  n$ symmetric positive semidefinite matrix, $q \in \mathbb{R}^{n}, r \in \mathbb{R}$, and $A$ is an $m \times  n$ matrix of rank $m$. The above program is converted in ADMM form as follows:
$$minimizef(x) + g(z)$$
$$subject to x -z = 0,$$
with
$$f(x) = \frac{1}{2} x^{\top}Px + q^{\top}x + r,dom(f) = {x \in \mathbb{R}^{n}| Ax = b},$$

<!-- PAGE 1931 -->
and
$$g = 1,$$
the constant function which is the indicator function of the convex set $C = \mathbb{R}^{n}$. In view of Example 52.8 and $(1)$, since $\Pi_{Rn} (x^{k+1} + u^{k}) = x^{k+1} + u^{k}$, the scaled form of ADMM consists of the following steps:
$$x^{k+1}= arg minx \begin{pmatrix} f(x) + (\rho /2) & x -z^{k} + u_{2}^{k2} \end{pmatrix}$$
$$z^{k+1}= x^{k+1}+ u^{k}$$
$$u^{k+1}= u^{k}+ x^{k+1}-z^{k+1}= 0,$$
for all $k \ge 0$, so
$$u^{k}= 0$$
$$z^{k+1}= x^{k+1}$$
for all $k \ge 1$. Consequently we have
$$x^{k+1}= arg minx \begin{pmatrix} f(x) + (\rho /2) & x -z^{k} + u_{2}^{k2} \end{pmatrix}$$
$$z^{k+1}= x^{k+1}+ u^{k}$$
$$u^{1}= 0,$$
for $k = 0, 1$, and for $k \ge 2$ we have $u^{k} = 0$ and $z^{k} = x^{k}$, with
$$x^{k+1}= arg minx \begin{pmatrix} f(x) + (\rho /2) & x -x_{2}^{k2} \end{pmatrix} .$$
As before, the x-update involves solving the KKT equations
$$\begin{pmatrix} P+ \rho I & A^{\top} \\ A & 0 \end{pmatrix} \begin{pmatrix} x^{k+1} \\ y \end{pmatrix} = \begin{pmatrix} -q + \rho (z^{k} -u^{k}) \\ b \end{pmatrix} ,$$
with $u^{k} = 0$ if $k \ge 1$ and $z^{k} = x^{k}$ if $k \ge 2$. We programmed the above method in Matlab as the function qsolve1, see Appendix $B$, Section B.1. Here are two examples.

> **Example 52.11.** Consider the quadratic program for which
$$P_{1} = \begin{pmatrix} 4 & 1 & 0 \\ 1 & 4 & 1 \\ 0 & 1 & 4 \end{pmatrix} q_{1} = - \begin{pmatrix} 4 \\ 4 \\ 4 \end{pmatrix}$$
$$A_{1} = \begin{pmatrix} 1 & 1 & -1 \\ 1 & -1 & -1 \end{pmatrix} b_{1} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} .$$
