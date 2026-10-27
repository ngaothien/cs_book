# Generalizations of Newton's Method


<!-- PAGE 1525 -->
The case of a real function suggests the following method for finding the zeros of a function $f$ : $\Omega \to Y$ , with $\Omega \subseteq X$: given a starting point $x_{0} \in \Omega$ , the sequence $(x_{k})$ is defined by
$$x_{k+1} = x_{k} -(f' (x_{k}))^{-1}(f(x_{k}))(*)$$
for all $k \ge 0$. For the above to make sense, it must be ensured that
$(1)$ All the points $x_{k}$ remain within $\Omega$ .
$(2)$ The function $f$ is differentiable within $\Omega$ .
$(3)$ The derivative f' $(x)$ is a bijection from $X$ to $Y$ for all $x \in \Omega$ . These are rather demanding conditions but there are sufficient conditions that guarantee that they are met. Another practical issue is that it may be very costly to compute (f' $(x_{k}))^{-1}$ at every iteration step. In the next section we investigate generalizations of Newton’s method which address the issues that we just discussed.

## 41.2 Generalizations of Newton’s Method

$$\mathbb{R}^{n} \mathbb{R}\mathbb{R}^{n}$$
Suppose that $f$ : $\Omega \to$ is given by $n$ functions $f_{i}$ : $\Omega \to$ , where $\Omega \subseteq$ . In this case, finding a zero a of $f$ is equivalent to solving the system
$$f_{1}(a_{1} \dots  , a_{n}) = 0$$
$$f_{2}(a_{1} \dots  , a_{n}) = 0$$
$$\vdots$$
$$f_{n}(a_{1} \dots  , a_{n}) = 0.$$
In the standard Newton method, the iteration step is given by (*), namely
$$x_{k+1} = x_{k} -(f' (x_{k}))^{-1}(f(x_{k})),$$
and if we define $\Delta x_{k}$ as $\Delta x_{k} = x_{k+1}$ - $x_{k}$, we see that $\Delta x_{k} =$ -(f' $(x_{k}))^{-1}(f(x_{k}))$, so $\Delta x_{k}$ is obtained by solving the equation
$$f' (x_{k})\Delta x_{k} = -f(x_{k}),$$
and then we set $x_{k+1} = x_{k} + \Delta x_{k}$. The generalization is as follows. Variant $1$. A single iteration of Newton’s method consists in solving the linear system
$$(J(f)(x_{k}))\Delta x_{k} = -f(x_{k}),$$

<!-- PAGE 1526 -->
and then setting
$$x_{k+1} = x_{k} + \Delta x_{k},$$
$$where J(f)(x_{k}) =_{\partial x}^{\partial fi} \begin{pmatrix} (x_{k}) \\ \overline{j} \\ verycostly \end{pmatrix} is the Jacobian matrix of f at x_{k}.$$
In general it is   to compute $J(f)(x_{k})$ at each iteration and then to solve the corresponding linear system. If the method converges, the consecutive vectors $x_{k}$ should differ only a little, as also the corresponding matrices $J(f)(x_{k})$. Thus, we are led to several variants of Newton’s method. Variant $2$. This variant consists in keeping the same matrix for $p$ consecutive steps (where $p$ is some fixed integer $\ge 2)$:
$$x_{k+1} = x_{k} -(f' (x_{0}))^{-1}(f(x_{k})),0 \le k \le p -1$$
$$x_{k+1} = x_{k} -(f' (x_{p}))^{-1}(f(x_{k})),p \le k \le 2p -1$$
$$\vdots$$
$$x_{k+1} = x_{k} -(f' (x_{rp}))^{-1}(f(x_{k})),rp \le k \le (r + 1)p -1$$
$$\vdots$$
Variant $3$. Set $p = \infty$ , that is, use the same matrix f' $(x_{0})$ for all iterations, which leads to iterations of the form
$$x_{k+1} = x_{k} -(f' (x_{0}))^{-1}(f(x_{k})),k \ge 0,$$
Variant $4$. Replace f' $(x_{0})$ by a particular matrix $A_{0}$ which is easy to invert:
$$x_{k+1} = x_{k} -A_{0}^{-1} f(x_{k}),k \ge 0.$$
In the last two cases, if possible, we use an LU factorization of f' $(x_{0})$ or $A_{0}$ to speed up the method. In some cases, it may even possible to set $A_{0} =$ I. The above considerations lead us to the definition of a generalized Newton method, as in Ciarlet $[41]$ (Chapter $7)$. Recall that a linear map $f \in$ L(E; $F)$ is called an isomorphism iff $f$ is continuous, bijective, and $f^{-1}$ is also continuous.

> **Definition 41.1.** If $X$ and $Y$ are two normed vector spaces and if $f$ : $\Omega \to Y$ is a function from some open subset $\Omega$ of $X$, a generalized Newton method for finding zeros of $f$ consists of
$(1) A$ sequence of families $(A_{k}(x))$ of linear isomorphisms from $X$ to $Y$ , for all $x \in \Omega$ and all integers $k \ge 0$;
$(2)$ Some starting point $x_{0} \in \Omega$ ;

<!-- PAGE 1527 -->
$(3) A$ sequence $(x_{k})$ of points of $\Omega$ defined by
$$x_{k+1} = x_{k} -(A_{k}(x_{\ell}))^{-1}(f(x_{k})),k \ge 0,(**)$$
where for every integer $k \ge 0$, the integer $\ell$ satisfies the condition
$$0 \le \ell \le k.$$
With $\Delta x_{k} = x_{k+1}$ - $x_{k}$, Equation (**) is equivalent to solving the equation
$$A_{k}(x_{\ell})(\Delta x_{k}) = -f(x_{k})$$
and setting $x_{k+1} = x_{k} + \Delta x_{k}$. The function $A_{k}(x)$ usually depends on f' . Definition 41.1 gives us enough flexibility to capture all the situations that we have previously discussed:
$$FunctionIndex$$
Variant $1: A_{k}(x) =$ f' $(x), \ell = k$ Variant $2: A_{k}(x) =$ f' $(x), \ell = min{rp, k}$, if rp $\le k \le (r +$ 1)p - $1, r \ge 0$ Variant $3: A_{k}(x) =$ f' $(x), \ell = 0$ Variant $4: A_{k}(x) = A_{0}$, where $A_{0}$ is a linear isomorphism from $X$ to $Y$ . The first case corresponds to Newton’s original method and the others to the variants that we just discussed. We could also have $A_{k}(x) = A_{k}$, a fixed linear isomorphism independent of $x \in \Omega$ .

> **Example 41.2.** Consider the matrix function $f$ given by
$$f(X) = A -X^{-1},$$
with $A$ and $X$ invertible $n \times  n$ matrices. If we apply Variant $1$ of Newton’s method starting with any $n \times  n$ matrix $X_{0}$, since the derivative of the function $g$ given by g(X) $= X^{-1}$ is $dg_{X}(Y$ ) $= -X^{-1}Y X^{-1}$, we have
$$f_{X}' (Y ) = X^{-1}Y X^{-1},$$
so
$$(f_{X}' )^{-1}(Y ) = XY X$$
and the Newton step is
$$X_{k+1} = X_{k} -(f_{Xk}' )^{-1}(f(X_{k})) = X_{k} -X_{k}(A -X_{k}^{-1} )X_{k},$$
which yields the sequence $(X_{k})$ with
$$X_{k+1} = X_{k}(2I -AX_{k}),k \ge 0.$$
In Problem 41.5, it is shown that Newton’s method converges to $A^{-1}$ iff the spectral radius of I - $X_{0}A$ is strictly smaller than $1$, that is, $\rho$ (I - $X_{0}A) < 1$.

<!-- PAGE 1528 -->
The following theorem inspired by the Newton–Kantorovich theorem gives sufficient conditions that guarantee that the sequence $(x_{k})$ constructed by a generalized Newton method converges to a zero of $f$ close to $x_{0}$. Although quite technical, these conditions are not very surprising.

> **Theorem 41.1.** Let $X$ be a Banach space, let $f$ : $\Omega \to Y$ be differentiable on the open subset $\Omega \subseteq X$, and assume that there are constants $r, M, \beta  > 0$ such that if we let
$$B = {x \in X | \|x -x_{0}\|\le r} \subseteq \Omega ,$$
then $(1)$
$$supsup

$A_{k}^{-1} (x)_{L(Y;X)} \le$ M,$$
$$k\ge 0x\in B$$
$(2) \beta  < 1$ and
$$supsup\|f' (x) -A_{k}(x')\|_{L(X;Y)} \le \frac{\beta}{M}$$
$$k\ge 0x,x'\in B$$
$(3)$
$$\|f(x_{0})\|\le \frac{r}{M} (1 -\beta ).$$
Then the sequence $(x_{k})$ defined by
$$x_{k+1} = x_{k} -A_{k}^{-1} (x_{\ell})(f(x_{k})),0 \le \ell \le k$$
is entirely contained within $B$ and converges to a zero a of $f$, which is the only zero of $f$ in $B$. Furthermore, the convergence is geometric, which means that
$$\| -\|$$
$$\|x_{k} -a\|\le \frac{x_{1}x_{0}}{1 -\beta} \beta^{k} .$$

*Proof.* We follow Ciarlet $[41]$ (Theorem 7.5.1, Section 7.5). The proof has three steps. Step $1$. We establish the following inequalities for all $k \ge 1$.
$$\|x_{k} -x_{k-1}\|\le M \|f(x_{k-1})\|(a)$$
$$\|x_{k} -x_{0}\|\le r(x_{k} \in B)(b)$$
$$\|f(x_{k})\|\le \frac{\beta}{M} \|x_{k} -x_{k-1}\|.(c)$$
We proceed by induction on $k$, starting with the base case $k = 1$. Since
$$x_{1} = x_{0} -A_{0}^{-1} (x_{0})(f(x_{0})),$$

<!-- PAGE 1529 -->
we have $x_{1}$ - $x_{0} = -A_{0}^{-1} (x_{0})(f(x_{0}))$, so by $(1)$ and $(3)$ and since $0 < \beta  < 1$, we have
$$\|x_{1} -x_{0}\|\le M \|f(x_{0})\|\le r(1 -\beta ) \le r,$$
establishing (a) and $(b)$ for $k = 1$. We also have $f(x_{0}) = -A_{0}(x_{0})(x_{1}$ - $x_{0})$, so $-f(x_{0})$ - $A_{0}(x_{0})(x_{1}$ - $x_{0}) = 0$ and thus
$$f(x_{1}) = f(x_{1}) -f(x_{0}) -A_{0}(x_{0})(x_{1} -x_{0}).$$
By the mean value theorem (Proposition 39.12) applied to the function $x \mapsto f(x)-A_{0}(x_{0})(x)$, by $(2)$, we get
$$\|f(x_{1})\|\le \sup\|f' (x) -A_{0}(x_{0})\|\|x_{1} -x_{0}\|\le \frac{\beta}{M} \|x_{1} -x_{0}\|,$$
$$x\in B$$
which is $(c)$ for $k = 1$. We now establish the induction step. Since by definition
$$x_{k} -x_{k-1} = -A_{k-1}^{-1}(x_{\ell})(f(x_{k-1})),0 \le \ell \le k -1,$$
by $(1)$ and the fact that by the induction hypothesis for $(b), x_{\ell} \in B$, we get
$$\|x_{k} -x_{k-1}\|\le M \|f(x_{k-1})\|,$$
which proves (a) for $k$. As a consequence, since by the induction hypothesis for $(c)$,
$$\|f(x_{k-1})\|\le \frac{\beta}{M} \|x_{k-1} -x_{k-2}\|,$$
we get
$$\|x_{k} -x_{k-1}\|\le M \|f(x_{k-1})\|\le \beta  \|x_{k-1} -x_{k-2}\|,(*_{1})$$
and by repeating this step,
$$\|x_{k} -x_{k-1}\|\le \beta^{k-1} \|x_{1} -x_{0}\|.(*_{2})$$
Using $(*_{2})$ and $(3)$, we obtain
$$!$$
$$\|x_{k} -x_{0}\|\le \sum_{j=1}^{k}  \|x_{j} -x_{j-1}\|\le \sum_{j=1}^{k}  \beta^{j-1} \|x_{1} -x_{0}\|$$
$$\| -\|$$
$$\le \frac{x_{1}x_{0}}{1 -\beta} \le \frac{M}{1 -\beta} \|f(x_{0})\|\le r,$$
which proves that $x_{k} \in B$, which is $(b)$ for $k$. Since
$$x_{k} -x_{k-1} = -A_{k-1}^{-1}(x_{\ell})(f(x_{k-1}))$$

<!-- PAGE 1530 -->
we also have $f(x_{k-1}) = -A_{k-1}(x_{\ell})(x_{k}$ - $x_{k-1})$, so we have
$$f(x_{k}) = f(x_{k}) -f(x_{k-1}) -A_{k-1}(x_{\ell})(x_{k} -x_{k-1}),$$
and as in the base case, applying the mean value theorem (Proposition 39.12) to the function $x \mapsto$ f(x) - $A_{k-1}(x_{\ell})(x)$, by $(2)$, we obtain
$$\|f(x_{k})\|\le \sup\|f' (x) -A_{k-1}(x_{\ell})\|\|x_{k} -x_{k-1}\|\le \frac{\beta}{M} \|x_{k} -x_{k-1}\|,$$
$$x\in B$$
proving $(c)$ for $k$. Step $2$. Prove that $f$ has a zero in $B$. To do this we prove that $(x_{k})$ is a Cauchy sequence. This is because, using $(*_{2})$, we have
$$!$$
$$\|x_{k+j} -x_{k}\|\le \sum_{i=0}^{j-1}  \|x_{k+i+1} -x_{k+i}\|\le \beta^{k} \sum_{i=0}^{j-1}  \beta^{i} \|x_{1} -x_{0}\|$$
$$\le \frac{\beta^{k}}{1 -\beta} \|x_{1} -x_{0}\|,$$
for all $k \ge 0$ and all $j \ge 0$, proving that $(x_{k})$ is a Cauchy sequence. Since $B$ is a closed ball in a complete normed vector space, $B$ is complete and the Cauchy sequence $(x_{k})$ converges to a limit $a \in B$. Since $f$ is continuous on $\Omega$ (because it is differentiable), by $(c)$ we obtain
$$\beta$$
$$\|f(a)\|= lim\|f(x_{k})\|\le  lim\|x_{k} -x_{k-1}\|= 0,$$
$$k\mapsto \infty \overline{M}_{k\mapsto \infty}$$
which yields f(a) $= 0$. Since
$$\|x_{k+j} -x_{k}\|\le \frac{\beta^{k}}{1 -\beta} \|x_{1} -x_{0}\|,$$
if we let $j$ tend to infinity, we obtain the inequality
$$\|x_{k} -a\|= \|a -x_{k}\|\le \frac{\beta^{k}}{1 -\beta} \|x_{1} -x_{0}\|,$$
which is the last statement of the theorem. Step $3$. Prove that $f$ has a unique zero in $B$. Suppose f(a) $=$ f(b) $= 0$ with a, $b \in B$. Since $A_{0}^{-1} (x_{0})(A_{0}(x_{0})(b$ - $a)) = b$ - $a$, we have
$$b -a = -A_{0}^{-1} (x_{0})(f(b) -f(a) -A_{0}(x_{0})(b -a)),$$
which by $(1)$ and $(2)$ and the mean value theorem implies that
$$\|b -a\|\le

$A_{0}^{-1} (x_{0})$

$\sup\|f' (x) -A_{0}(x_{0})\|\|b -a\|\le \beta  \|b -a\|.$$$
$$x\in B$$
Since $0 < \beta  < 1$, the inequality $\|b$ - $a\|\le \beta  \|b$ - $a\|$ is only possible if $a = b$.

<!-- PAGE 1531 -->
It should be observed that the conditions of Theorem 41.1 are typically quite stringent. It can be shown that Theorem 41.1 applies to the function $f$ of Example 41.1 given by f(x) $= x^{2}$ - $\alpha$  with $\alpha  > 0$, for any $x_{0} > 0$ such that
$$\frac{6}{7} \alpha  \le x_{0}^{2} \le \frac{6}{5} \alpha ,$$
$$\sqrt$$
with $\beta  = 2/5, r = (1/6)x_{0}, M = 3/(5x_{0})$. Such values of $x_{0}$ are quite close to $\overline{\alpha}$. If we assume that we already know that some element $a \in \Omega$ is a zero of $f$, the next theorem gives sufficient conditions for a special version of a generalized Newton method to converge. For this special method the linear isomorphisms $A_{k}(x)$ are independent of $x \in \Omega$ .

> **Theorem 41.2.** Let $X$ be a Banach space and let $f$ : $\Omega \to Y$ be differentiable on the open subset $\Omega \subseteq X$. If $a \in \Omega$ is a point such that f(a) $= 0$, if f' (a) is a linear isomorphism, and if there is some $\lambda$  with $0 < \lambda  < 1/2$ such that
$$\sup\|A_{k} -f' (a)\|_{L(X;Y)} \le \frac{\lambda}{\|(f'(a))^{-1}\|_{L(Y;X)}} ,$$
$$k\ge 0$$
then there is a closed ball $B$ of center a such that for every $x_{0} \in B$, the sequence $(x_{k})$ defined by
$$x_{k+1} = x_{k} -A_{k}^{-1} (f(x_{k})),k \ge 0,$$
is entirely contained within $B$ and converges to a, which is the only zero of $f$ in $B$. Furthermore, the convergence is geometric, which means that
$$\|x_{k} -a\|\le \beta^{k} \|x_{0} -a\|,$$
for some $\beta  < 1$. A proof of Theorem 41.2 can be found in Ciarlet $[41]$ (Section 7.5). For the sake of completeness, we state a version of the Newton–Kantorovich theorem which corresponds to the case where $A_{k}(x) =$ f' $(x)$. In this instance, a stronger result can be obtained especially regarding upper bounds, and we state a version due to Gragg and Tapia which appears in Problem 7.5-4 of Ciarlet $[41]$.

> **Theorem 41.3.** (Newton–Kantorovich) Let $X$ be a Banach space, and let $f$ : $\Omega \to Y$ be differentiable on the open subset $\Omega \subseteq X$. Assume that there exist three positive constants $\lambda , \mu , \nu$  and a point $x_{0} \in \Omega$ such that
$$0 < \lambda \mu \nu  \le \frac{1}{2} ,$$

<!-- PAGE 1532 -->
and if we let
$$-\sqrt$$
$$\overline{-}$$
$$\rho^{-} = \frac{1\overline{1}\overline{2}\overline{\lambda \mu \nu}}{\sqrt\mu \nu}$$
$$\overline{-}$$
$$\rho^{+} = \frac{1 +\overline{1}\overline{2}\overline{\lambda \mu \nu}}{\mu \nu}$$
$$B = {x \in X | \|x -x_{0}\|< \rho^{-} }$$
$$\Omega^{+} = {x \in \Omega | \|x -x_{0}\|< \rho^{+} },$$
then $\overline{B} \subseteq \Omega$ , f' $(x_{0})$ is an isomorphism of $\mathcal{L}(X; Y$ ), and
$$(f'(x_{0}))^{-1}

$\le \mu$ ,$$
$$(f'(x_{0}))^{-1}f(x_{0})

$\le \lambda$ ,$$
$$\sup \|f'(x) -f'(y)\|\le \nu  \|x -y\|.$$
$$x,y\in \Omega +$$
Then f' $(x)$ is isomorphism of $\mathcal{L}(X; Y$ ) for all $x \in B$, and the sequence defined by
$$x_{k+1} = x_{k} -(f' (x_{k}))^{-1}(f(x_{k})),k \ge 0$$
is entirely contained within the ball $B$ and converges to a zero a of $f$ which is the only zero of $f$ in $\Omega^{+}$ . Finally, if we write $\theta  = \rho^{-} /\rho^{+}$ , then we have the following bounds:
$$\overline{-}$$
$$\|x_{k} -a\|\le \frac{2\sqrt{1}\overline{2}\overline{\lambda \mu \nu}}{\lambda \mu \nu} \frac{\theta^{2k}}{1 -\theta^{2k}} \|x_{1} -x_{0}\|if \lambda \mu \nu  < \frac{1}{2}$$
$$\| -\|$$
$$\|x_{k} -a\|\le \frac{x_{1}x_{0}}{2^{k-1}} if \lambda \mu \nu  = \frac{1}{2} ,$$
and
$$\| -\|$$
$$\frac{2x_{k+1}x_{k}}{1 +p(1 + 4\theta^{2k} (1 + \theta^{2k} )^{-2})} \le \|x_{k} -a\|\le \theta^{2k-1} \|x_{k} -x_{k-1}\|.$$
We can now specialize Theorems 41.1 and 41.2 to the search of zeros of the derivative $\mathbb{R}$ J': $\Omega \to$ E', of a function $J$ : $\Omega \to$ , with $\Omega \subseteq E$. The second derivative J'' of $J$ is
$$\mathbb{R}$$
a continuous bilinear form J'': $E \times  E \to$ , but is is convenient to view it as a linear map in $\mathcal{L}(E$, E'); the continuous linear form J''(u) is given by J''(u)(v) $=$ J''(u, $v)$. In our next theorem, which follows immediately from Theorem 41.1, we assume that the $A_{k}(x)$ are isomorphisms in $\mathcal{L}(E$, E').

> **Theorem 41.4.** Let $E$ be a Banach space, let $J$ : $\Omega \to \mathbb{R}$ be twice differentiable on the open subset $\Omega \subseteq E$, and assume that there are constants $r, M, \beta  > 0$ such that if we let
$$B = {x \in E | \|x -x_{0}\|\le r} \subseteq \Omega ,$$
then

<!-- PAGE 1533 -->
$(1)$
$$supsup

$A_{k}^{-1} (x)_{L(E';E)} \le$ M,$$
$$k\ge 0x\in B$$
$(2) \beta  < 1$ and
$$\sup\ge \sup'\in \|J''(x) -A_{k}(x')\|_{L(E;E')} \le \frac{\beta}{M}$$
$$k0x,xB$$
$(3)$
$$\|J'(x_{0})\|\le \frac{r}{M} (1 -\beta ).$$
Then the sequence $(x_{k})$ defined by
$$x_{k+1} = x_{k} -A_{k}^{-1} (x_{\ell})(J'(x_{k})),0 \le \ell \le k$$
is entirely contained within $B$ and converges to a zero a of J', which is the only zero of J' in $B$. Furthermore, the convergence is geometric, which means that
$$\| -\|$$
$$\|x_{k} -a\|\le \frac{x_{1}x_{0}}{1 -\beta} \beta^{k} .$$
In the next theorem, which follows immediately from Theorem 41.2, we assume that the $A_{k}(x)$ are isomorphisms in $\mathcal{L}(E$, E') that are independent of $x \in \Omega$ .

> **Theorem 41.5.** Let $E$ be a Banach space and let $J$ : $\Omega \to \mathbb{R}$ be twice differentiable on the open subset $\Omega \subseteq E$. If $a \in \Omega$ is a point such that J'(a) $= 0$, if J''(a) is a linear isomorphism, and if there is some $\lambda$  with $0 < \lambda  < 1/2$ such that
$$\sup\ge \|A_{k} -J''(a)\|_{L(E;E')} \le \frac{\lambda}{\|(J''(a))^{-1}\|_{L(E';E)}} ,$$
$$k0$$
then there is a closed ball $B$ of center a such that for every $x_{0} \in B$, the sequence $(x_{k})$ defined by
$$x_{k+1} = x_{k} -A_{k}^{-1} (J'(x_{k})),k \ge 0,$$
is entirely contained within $B$ and converges to a, which is the only zero of J' in $B$. Furthermore, the convergence is geometric, which means that
$$\|x_{k} -a\|\le \beta^{k} \|x_{0} -a\|,$$
for some $\beta  < 1$. When $E = \mathbb{R}^{n}$, the Newton method given by Theorem 41.4 yields an iteration step of the form
$$x_{k+1} = x_{k} -A_{k}^{-1} (x_{\ell})\nabla J(x_{k}),0 \le \ell \le k,$$
