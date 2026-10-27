# Conjugate Function and Legendre Dual Function


<!-- PAGE 1833 -->
which is precisely the result of adding $\alpha  \ge 0$ and $\beta  \ge 0$ as slack variables to the inequalities $(*_{3})$ of Example 50.6, namely
$$-X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + b \begin{pmatrix} 1_{p} \\ -1_{q} \end{pmatrix} + 1_{p+q} \le 0_{p+q},$$
to make them equalities, where $\rho$  plays the role of $b$. When the constraints are affine, the dual function $G(\lambda , \nu$ ) can be expressed in terms of the conjugate of the objective function $J$.

## 50.11 Conjugate Function and Legendre Dual Func-

$$tion$$
The notion of conjugate function goes back to Legendre and plays an important role in classical mechanics for converting a Lagrangian to a Hamiltonian; see Arnold $[5]$ (Chapter $3$, Sections $14$ and $15)$.

> **Definition 50.11.** Let $f$ : $A \to \mathbb{R}$ be a function defined on some subset $A$ of $\mathbb{R}^{n}$. The
$$\mathbb{R}^{n} \mathbb{R}$$
conjugate $f^{*}$ of the function $f$ is the partial function $f^{*}: \to$  defined by
$$f^{*} (y) = \sup(\langle y, x\rangle -f(x)) = \sup(y^{\top}x -f(x)),y \in \mathbb{R}^{n}.$$
$$x\in Ax\in A$$
The conjugate of a function is also called the Fenchel conjugate, or Legendre transform when $f$ is differentiable. As the pointwise supremum of a family of affine functions in $y$, the conjugate function $f^{*}$ is convex, even if the original function $f$ is not convex. By definition of $f^{*}$ we have
$$f(x) + f^{*} (y) \ge \langle x, y\rangle = x^{\top}y,$$
whenever the left-hand side is defined. The above is known as Fenchel’s inequality (or Young’s inequality if $f$ is differentiable). If $f$ : $A \to \mathbb{R}$ is convex (so $A$ is convex) and if epi(f) is closed, then it can be shown that $f^{**} = f$. In particular, this is true if $A =\mathbb{R}^{n}$. The domain of $f^{*}$ can be very small, even if the domain of $f$ is big. For example, if $f$ : $\mathbb{R} \to \mathbb{R}$ is the affine function given by f(x) $=$ ax $+ b$ (with a, $b \in \mathbb{R})$, then the function $x \mapsto$ yx - ax - $b$ is unbounded above unless $y = a$, so
$$($$
$$-bif y = a$$
$$f^{*} (y) =$$
$$+\infty otherwise.$$

<!-- PAGE 1834 -->
The domain of $f^{*}$ can also be bigger than the domain of $f$; see Example 50.8(3). The conjugates of many functions that come up in optimization are derived in Boyd and Vandenberghe; see $[29]$, Section 3.3. We mention a few that will be used in this chapter.

> **Example 50.8.**
$(1)$ Negative logarithm: f(x) $=$ -log $x$, with dom(f) $= {x \in \mathbb{R}$ | $x > 0}$. The function $x \mapsto yx+log x$ is unbounded above if $y \ge 0$, and when $y < 0$, its maximum is obtained iff its derivative is zero, namely
$$y + \frac{1}{x} = 0.$$
Substituting for $x = -1/y$ in yx $+$ log $x$, we obtain $-1 + log(-1/y) = -1$ - log(-y), so we have
$$f^{*} (y) = -\log(-y) -1,$$
with $dom(f^{*}$ ) $= {y \in \mathbb{R}$ | $y < 0}$.
$$\mathbb{R}$$
$(2)$ Exponential: f(x) $= e^{x}$, with dom(f) $=$ . The function $x \mapsto$ yx - $e^{x}$ is unbounded if $y < 0$. When $y > 0$, it reaches a maximum iff its derivative is zero, namely
$$y -e^{x}= 0.$$
Substituting for $x =$ log $y$ in yx - $e^{x}$, we obtain $y$ log $y$ - $y$, so we have
$$f^{*} (y) = y \log y -y,$$
with $dom(f^{*}$ ) $= {y \in \mathbb{R}$ | $y \ge 0}$, with the convention that $0$ log $0 = 0$.
$(3)$ Negative Entropy: f(x) $= x$ log $x$, with dom(f) $= {x \in \mathbb{R}$ | $x \ge 0}$, with the convention that $0$ log $0 = 0$. The function $x \mapsto$ yx - $x$ log $x$ is bounded above for all $y > 0$, and it attains its maximum when its derivative is zero, namely
$$y -\log x -1 = 0.$$
Substituting for $x = e^{y-1}$ in yx - $x$ log $x$, we obtain $ye^{y-1}$ - $e^{y-1}(y$ - $1) = e^{y-1}$, which yields
$$f^{*} (y) = e^{y-1},$$
with $dom(f^{*}$ ) $=\mathbb{R}$.
$(4)$ Strictly convex quadratic function: f(x) $=^{1} x^{\top}Ax$, where $A$ is an $n \times  n$ symmetric positive definite matrix, with dom(f) $= \mathbb{R}^{n}.^{2}$ The function $x \mapsto y^{\top}x -_{2}^{1}x^{\top}Ax$ has a unique maximum when is gradient is zero, namely
$$y = Ax.$$

<!-- PAGE 1835 -->
Substituting for $x = A^{-1}y$ in $y^{\top}x -_{2}^{1}x^{\top}Ax$, we obtain
$$y^{\top}A^{-1}y - \frac{1}{2} y^{\top}A^{-1}y = - \frac{1}{2} y^{\top}A^{-1}y,$$
so
$$f^{*} (y) = - \frac{1}{2} y^{\top}A^{-1}y$$
with $dom(f^{*}$ ) $=\mathbb{R}^{n}$.
$(5)$ Log-determinant: f(X) $=$ log $det(X^{-1})$, where $X$ is an $n\times n$ symmetric positive definite matrix. Then
$$f(Y ) = \log \det((-Y )^{-1}) -n,$$
where $Y$ is an $n \times  n$ symmetric negative definite matrix; see Boyd and Vandenberghe; see $[29]$, Section 3.3.1, Example 3.23.
$(6)$ Norm on $\mathbb{R}^{n}$: f(x) $= \|x\|$ for any norm $\|\|$ on $\mathbb{R}^{n}$, with dom(f) $= \mathbb{R}^{n}$. Recall from Section 14.7 that the dual norm $\|\|^{D}$ of the norm $\|\|$ (with respect to the canonical
$$\mathbb{R}^{n}$$
inner product $x \cdot  y = y^{\top}x$ on is given by
$$\|y\|^{D}= \sup|y^{\top}x|,$$
$$\|x\|=1$$
and that
$$|y^{\top}x| \le \|x\|\|y\|^{D}.$$
We have
$$f^{*} (y) = \sup(y^{\top}x -\|x\|)$$
$$x\in \mathbb{R} n$$
$$=\in \mathbb{R} supn \begin{pmatrix} x \\ y^{\top} & -1 \\ \|x\| \end{pmatrix} \|x\|$$
$$x,x\neq 0$$
$$\le \sup(\|y\|^{D}-1) \|x\|,$$
$$x\in \mathbb{R} n,x\neq 0$$
so if $\|y\|^{D} > 1$ this last term goes to $+\infty$ , but if $\|y\|^{D} \le 1$, then its maximum is $0$. Therefore,
$$($$
$$0if \|y\|^{D}\le 1$$
$$f^{*} (y) = \|y\|^{*}=$$
$$+\infty otherwise.$$
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
$(7)$ Norm squared: f(x) $=_{2}^{1} \|x\|^{2}$ for any norm $\|\|$ on , with dom(f) $=$ . Since $|y^{\top}x| \le \|x\|\|y\|^{D}$, we have
$$y^{\top}x -(1/2) \|x\|^{2}\le \|y\|^{D}\|x\|-(1/2) \|x\|^{2}.$$

<!-- PAGE 1836 -->
The right-hand side is a quadratic function of $\|x\|$ which achieves its maximum at $\|x\| = \|y\|^{D}$, with maximum value $(1/2)(\|y\|^{D})^{2}$. Therefore
$$y^{\top}x -(1/2) \|x\|^{2}\le (1/2) \begin{pmatrix} \|y\|^{D2} \end{pmatrix}$$
for all $x$, which shows that
$$f^{*} (y) \le (1/2) \begin{pmatrix} \|y\|^{D2} \end{pmatrix} .$$
By definition of the dual norm and because the unit sphere is compact, for any $y \in \mathbb{R}^{n}$,
$$\mathbb{R}^{n}$$
there is some $x \in$ such that $\|x\| = 1$ and $y^{\top}x = \|y\|^{D}$, so multiplying both sides by $\|y\|^{D}$ we obtain
$$y^{\top}\|y\|^{D}x = \begin{pmatrix} \|y\|^{D2} \\ = & y \end{pmatrix}$$
and for $z = \|y\|^{D} x$, since $\|x\| = 1$ we have $\|z\|  \| \|^{D} \|x\| = \|y\|^{D}$, so we get
$$y^{\top}z -(1/2)(\|z\|)^{2}= \begin{pmatrix} \|y\|^{D2} \end{pmatrix} -(1/2) \begin{pmatrix} \|y\|^{D2} \end{pmatrix} = (1/2) \begin{pmatrix} \|y\|^{D2} \end{pmatrix} ,$$
$$which shows that the upper bound (1/2) \begin{pmatrix} \|y\|^{D2} \\ 1 \end{pmatrix} is achieved. Therefore,$$
$$f^{*} (y) =2 \begin{pmatrix} \|y\|^{D2} \end{pmatrix} ,$$
and $dom(f^{*}$ ) $=\mathbb{R}^{n}$.
$$(8) Log-sum-\exp function: f(x) = \log \sum_{i}  , where x = (x_{1}, \dots  , x_{n}) \in \mathbb{R}^{n}.To$$
$$\mathbb{R}^{n} \begin{pmatrix} n & e^{xi} \\ =1 \\ whichthe \end{pmatrix}$$
determine the values of $y \in$ for   maximum of g(x) $= y^{\top}x$ - f(x) over
$$\mathbb{R}^{n}$$
$x \in$ is attained, we compute its gradient and we find
$$\begin{pmatrix} e^{x1} \\ y_{1} - \\ n & e_{i}^{x} \\ \ddots \\ e^{xn} \\ y_{n} - \\ n & e_{i}^{x} \end{pmatrix} \sum_{i}$$
$$\nabla f_{x} =.$$
$$\sum_{i}  =1$$
Therefore, $(y_{1}, \dots  , y_{n})$ must satisfy the system of equations
$$y_{j} = \frac{e^{xj}}{e_{i}^{x}} \sum_{i}  n  ,j = 1, \dots  , n.(*)$$
$$=1$$
$$The condition \sum_{i}  n=1 y_{i} = 1 is obviously necessary, as well as the conditions y_{i} > 0, for$$
$i = 1, \dots  , n$. Conversely, if $1^{\top}y = 1$ and $y > 0$, then $x_{j} =$ log $y_{i}$ for $i = 1, \dots  , n$ is a solution. Since (*) implies that
$$x_{i} = \log y_{i} + \log \begin{pmatrix} e^{xi} \end{pmatrix} \sum_{i=1}^{n}  ,(**)$$

<!-- PAGE 1837 -->
we get
$$y^{\top}x -f(x) = \sum_{i=1}^{n}  y_{i}x_{i} -\log \begin{pmatrix} e^{xi} \end{pmatrix} \sum_{i=1}^{n}$$
$$= \sum_{i=1}^{n}  y_{i} \log y_{i} + \sum_{i=1}^{n}  y_{i} \log \begin{pmatrix} e^{xi} \end{pmatrix} \sum_{i=1}^{n}  -\log \begin{pmatrix} e^{xi} \end{pmatrix} \sum_{i=1}^{n}  by (**)$$
$$= \sum_{i=1}^{n}  y_{i} \log y_{i} + \begin{pmatrix} y_{i} -1 \end{pmatrix} \sum_{i=1}^{n}  \log \begin{pmatrix} e^{xi} \end{pmatrix} \sum_{i=1}^{n}$$
$$= \sum_{i=1}^{n}  y_{i} \log y_{i}since \sum_{i}  n=1 y_{i} = 1.$$
$$Consequently, if f^{*} (y) is defined, then f^{*} (y) = \sum_{i}  n=1 y_{i} \log y_{i}. If we agree that 0 \log 0 =$$
$0$, then it is an easy exercise (or, see Boyd and Vandenberghe $[29]$, Section 3.3, Example 3.25) to show that
$$f^{*} (y) =( \sum_{i}  n=1 y_{i} \log y_{i}if 1^{\top}y = 1 and y \ge 0$$
$$\infty otherwise.$$
Thus we obtain the negative entropy restricted to the domain $1^{\top}y = 1$ and $y \ge 0$.
$$\mathbb{R}^{n} \mathbb{R}$$
If $f$ : $\to$  is convex and differentiable, then $x^{*}$ maximizes $x^{\top}y$ -f(x) iff $x^{*}$ minimizes $-x^{\top}y +$ f(x) iff
$$\nabla f_{x*}= y,$$
and so
$$f^{*} (y) = (x^{*})^{\top}\nabla f_{x*}-f(x^{*}).$$
Consequently, if we can solve the equation
$$\nabla f_{z} = y$$
for $z$ given $y$, then we obtain $f^{*} (y)$. It can be shown that if $f$ is twice differentiable, strictly convex, and surlinear, which means that
$$\|y\|lim\mapsto +\infty \frac{f(y)}{\|y\|} = +\infty ,$$
then there is a unique $x_{y}$ such that $\nabla f_{xy} = y$, so that
$$f^{*} (y) = x_{y}^{\top} \nabla f_{xy} -f(x_{y}),$$
and $f^{*}$ is differentiable with
$$\nabla f_{y}^{*}  = x_{y}.$$
We now return to our optimization problem.

<!-- PAGE 1838 -->

> **Proposition 50.20.** Consider Problem $(P)$,
$$minimizeJ(v)$$
$$subject to Av \le b$$
$$Cv = d,$$
with affine inequality and equality constraints (with $A$ an $m \times  n$ matrix, $C$ an $p \times  n$ matrix, $b \in \mathbb{R}^{m}, d \in \mathbb{R}^{p})$. The dual function $G(\lambda , \nu$ ) is given by
$$($$
$$-b^{\top}\lambda  -d^{\top}\nu  -J^{*}(-A^{\top}\lambda  -C^{\top}\nu )if -A^{\top}\lambda  -C^{\top}\nu  \in dom(J^{*}),$$
$$G(\lambda , \nu ) =$$
$$-\infty otherwise,$$
for all $\lambda  \in \mathbb{R}_{+}^{m}$ and all $\nu  \in \mathbb{R}^{p}$, where $J^{*}$ is the conjugate of $J$.

*Proof.* The Lagrangian associated with the above program is
$$L(v, \lambda , \nu ) = J(v) + (Av -b)^{\top}\lambda  + (Cv -d)^{\top}\nu$$
$$= -b^{\top}\lambda  -d^{\top}\nu  + J(v) + (A^{\top}\lambda  + C^{\top}\nu )^{\top}v,$$
with $\lambda  \in \mathbb{R}_{+}^{m}$ and $\nu  \in \mathbb{R}^{p}$. By definition
$$G(\lambda , \nu ) = -b^{\top}\lambda  -d^{\top}\nu  + \inf(J(v) + (A^{\top}\lambda  + C^{\top}\nu )^{\top}v)$$
$$v\in \mathbb{R} n$$
$$= -b^{\top}\lambda  -d^{\top}\nu  -\sup(-(A^{\top}\lambda  + C^{\top}\nu )^{\top}v -J(v))$$
$$v\in \mathbb{R} n$$
$$= -b^{\top}\lambda  -d^{\top}\nu  -J^{*}(-A^{\top}\lambda  -C^{\top}\nu ).$$
Therefore, for all $\lambda  \in \mathbb{R}_{+}^{m}$ and all $\nu  \in \mathbb{R}^{p}$, we have
$$($$
$$-b^{\top}\lambda  -d^{\top}\nu  -J^{*}(-A^{\top}\lambda  -C^{\top}\nu )if -A^{\top}\lambda  -C^{\top}\nu  \in dom(J^{*}),$$
$$G(\lambda , \nu ) =$$
$$-\infty otherwise,$$
as claimed. As application of Proposition 50.20, consider the following example.

> **Example 50.9.** Consider the following problem:
$$minimize\|v\|$$
$$subject to Av = b,$$
where $\|\|$ is any norm on $\mathbb{R}^{n}$. Using the result of Example 50.8(6), we obtain
$$G(\nu ) = -b^{\top}\nu  -

$-A^{\top}\nu^{*}$

,$$ that is,
$$($$
$$-b^{\top}\nu if

$A^{\top}\nu^{D}$

$\le$ 1$$
$$G(\nu ) =$$
$$-\infty otherwise.$$
In the special case where $\|\| = \|\|_{2}$, we also have $\|\|^{D} = \|\|_{2}$.

<!-- PAGE 1839 -->
Another interesting application is to the entropy minimization problem.

> **Example 50.10.** Consider the following problem known as entropy minimization:
$$minimizef(x) = \sum_{i=1}^{n}  x_{i} \log x_{i}$$
$$subject to Ax \le b$$
$$1^{\top}x = 1,$$
$$\mathbb{R}^{n}$$
where dom(f) $= {x \in$ | $x \ge 0}$. By Example 50.8(3), the conjugate of the negative entropy function $u$ log $u$ is $e^{v-1}$, so we easily see that
$$f^{*} (y) = \sum_{i=1}^{n}  e^{yi-1},$$
which is defined on $\mathbb{R}^{n}$. Proposition 50.20 implies that the dual function $G(\lambda , \mu$ ) of the entropy minimization problem is given by
$$G(\lambda , \mu ) = -b^{\top}\lambda  -\mu  -e^{-\mu-1} \sum_{i=1}^{n}  e^{-(Ai)\top\lambda},$$
$$\mathbb{R}_{+}^{n}\mathbb{R}$$
for all $\lambda  \in$  and all $\mu  \in$ , where $A^{i}$ is the ith column of $A$. It follows that the dual program is:
$$maximize-b^{\top}\lambda  -\mu  -e^{-\mu-1} \sum_{i=1}^{n}  e^{-(Ai)\top\lambda}$$
$$subject to \lambda  \ge 0.$$
We can simplify this problem by maximizing over the variable $\mu  \in \mathbb{R}$. For fixed $\lambda$ , the objective function is maximized when the derivative is zero, that is,
$$-1 + e^{-\mu-1} \sum_{i=1}^{n}  e^{-(Ai)\top\lambda}= 0,$$
which yields
$$\mu  = \log \begin{pmatrix} e^{-(Ai)\top\lambda} \end{pmatrix} \sum_{i=1}^{n}  -1.$$
By plugging the above value back into the objective function of the dual, we obtain the following program:
$$maximize-b^{\top}\lambda  -\log \begin{pmatrix} e^{-(Ai)\top\lambda} \end{pmatrix} \sum_{i=1}^{n}$$
$$subject to \lambda  \ge 0.$$

<!-- PAGE 1840 -->
The entropy minimization problem is another problem for which Theorem 50.18 applies, and thus can be solved using the dual program. Indeed, the Lagrangian of the primal program is given by
$$L(x, \lambda , \mu ) = \sum_{i-1}^{n}  x_{i} \log x_{i} + \lambda^{\top} (Ax -b) + \mu (1^{\top}x -1).$$
Using the second derivative criterion for convexity, we see that L(x, $\lambda , \mu$ ) is strictly convex for $x \in \mathbb{R}_{+}^{n}$ and is bounded below, so it has a unique minimum which is obtain by setting the gradient $\nabla L_{x}$ to zero. We have
$$\nabla L_{x} = \begin{pmatrix} \log x_{1} + 1 + (A^{1})^{\top}\lambda  + \mu \\ \vdots \\ \log x_{n} + 1 + (A^{n})^{\top}\lambda  + \mu . \end{pmatrix}$$
so by setting $\nabla L_{x}$ to $0$ we obtain
$$x_{i} = e^{-((An)\top\lambda+\mu+1)},i = 1, \dots  , n.(*)$$
By Theorem 50.18, since the objective function is convex and the constraints are affine, if the primal has a solution then so does the dual, and $\lambda$  and $\mu$  constitute an optimal solution of the dual, then $x = (x_{1}, \dots  , x_{n})$ given by the equations in (*) is an optimal solution of the primal. Other examples are given in Boyd and Vandenberghe; see $[29]$, Section 5.1.6. The derivation of the dual function of Problem $(SVM_{h1})$ from Section 50.5 involves a similar type of reasoning.

> **Example 50.11.** Consider the Hard Margin Problem $(SVM_{h1})$:
$$maximize\delta$$
$$subject to$$
$$w^{\top}u_{i} -b \ge \delta i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge \delta j = 1, \dots  , q$$
$$\|w\|_{2} \le 1,$$
which is converted to the following minimization problem:
$$minimize-2\delta$$
$$subject to$$
$$w^{\top}u_{i} -b \ge \delta i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge \delta j = 1, \dots  , q$$
$$\|w\|_{2} \le 1.$$

<!-- PAGE 1841 -->
We replaced $\delta$  by $2\delta$  because this will make it easier to find a nice geometric interpretation. Recall from Section 50.5 that Problem $(SVM_{h1})$ has a an optimal solution iff $\delta  > 0$, in which case $\|w\| = 1$. The corresponding Lagrangian with $\lambda  \in \mathbb{R}_{+}^{p}, \mu  \in \mathbb{R}_{+}^{q}, \gamma  \in \mathbb{R}^{+}$, is
$$L(w, b, \delta , \lambda , \mu , \gamma ) = -2\delta  + \sum_{i=1}^{p}  \lambda_{i} (\delta  + b -w^{\top}u_{i}) + \sum_{j=1}^{q}  \mu_{j} (\delta  -b + w^{\top}v_{j}) + \gamma (\|w\|_{2} -1)$$
$$= w^{\top} \begin{pmatrix} - & \lambda_{i} u_{i} + & \mu_{j} v_{j} \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}  + \gamma  \|w\|_{2} + \begin{pmatrix} \lambda_{i}  - & \mu_{j} \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}  b$$
$$+ \begin{pmatrix} -2 + & \lambda_{i}  + & \mu_{j} \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}  \delta  -\gamma .$$
Next to find the dual function $G(\lambda , \mu , \gamma$ ) we need to minimize L(w, $b, \delta , \lambda , \mu , \gamma$ ) with respect to $w, b$ and $\delta$ , so its gradient with respect to $w, b$ and $\delta$  must be zero. This implies that
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$-2 + \sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = 0,$$
which yields
$$\sum_{i=1}^{p}  \lambda_{i}  = \sum_{j=1}^{q}  \mu_{j}  = 1.$$
Observe that we did not compute the partial derivative with respect to $w$ because it does not yield any useful information due to the presence of the term $\|w\|_{2}$ (as opposed to $\|w\|_{2}^{2})$. Our minimization problem is reduced to: find
$$!$$
$$w,\|infw\|\le 1w^{\top} \begin{pmatrix} \mu_{j} v_{j}- & \lambda_{i} u_{i} \end{pmatrix} \sum_{j=1}^{q}  \sum_{i=1}^{p}  + \gamma  \|w\|_{2} -\gamma$$
$$!$$
$$= -\gamma  -\gamma w,\|infw\|\le 1-w^{\top} \frac{1}{\gamma} \begin{pmatrix} \mu_{j} v_{j}- & \lambda_{i} u_{i} \end{pmatrix} \sum_{j=1}^{q}  \sum_{i=1}^{p}  + \|-w\|_{2}$$
$$-\gamma if_{\gamma}^{1} \sum_{j}  q \mu_{j} v_{j} -p \lambda_{i} u_{i}



$D\le$ 1$$
$$==1 \sum_{i}  =12by Example 50.8(6)$$
$-\infty$ otherwise 
$$=(-\gamma if \sum  qj=1 \mu_{j} v_{j} - \sum_{i}  p=1 \lambda_{i} u_{i} \le \gamma since \|\|_{2}^{D} = \|\|_{2} and \gamma  > 0$$
$$2$$
$-\infty$ otherwise.

<!-- PAGE 1842 -->
It is immediately verified that the above formula is still correct if $\gamma  = 0$. Therefore
$$G(\lambda , \mu , \gamma ) =(-\gamma if \sum  qj=1 \mu_{j} v_{j} - \sum_{i}  p=1 \lambda_{i} u_{i} \le \gamma$$
$$2$$
$$-\infty otherwise.$$
$$Since \sum_{j}  q=1 \mu_{j} v_{j} - \sum_{i}  p=1 \lambda_{i} u_{i} \le \gamma  iff-\gamma  \le - \sum_{j}  q=1 \mu_{j} v_{j} - \sum_{i}  p=1 \lambda_{i} u_{i}, the dual pro-$$
$$2$$
gram, maximizing $G(\lambda , \mu , \gamma$ ), $is^{2}$ equivalent to
$$maximize- \sum_{j=1}^{q}  \mu_{j} v_{j} - \sum_{i=1}^{p}  \lambda_{i} u_{i}$$
$$2$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  = 1, \lambda  \ge 0$$
$$\sum_{j=1}^{q}  \mu_{j}  = 1, \mu  \ge 0,$$
equivalently
$$minimize \sum_{j=1}^{q}  \mu_{j} v_{j} - \sum_{i=1}^{p}  \lambda_{i} u_{i}$$
$$2$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  = 1, \lambda  \ge 0$$
$$\sum_{j=1}^{q}  \mu_{j}  = 1, \mu  \ge 0.$$
$$Geometrically, \sum_{i}  p=1 \lambda u_{i} with \sum_{i}  p \lambda_{i}  = 1 and \lambda  \ge 0 is a convex combination of the u_{i}s,$$
$$and \sum_{j}  q=1 \mu_{j} v_{j} with \sum_{j}^{i}  q \mu_{j}  = 1^{=1} and \mu  \ge 0 is a convex combination of the v_{j}s, so the dual$$
program is to $minimize^{=1}$ the distance between the polyhedron $conv(u_{1}, \dots  , u_{p})$ (the convex hull of the $u_{i}s)$ and the polyhedron $conv(v_{1}, \dots  , v_{q})$ (the convex hull of the $v_{j}s)$. Since both polyhedra are compact, the shortest distance between then is achieved. In fact, there is some vertex $u_{i}$ such that if $P(u_{i})$ is its projection onto $conv(v_{1}, \dots  , v_{q})$ (which exists by Hilbert space theory), then the length of the line segment $(u_{i}, P(u_{i}))$ is the shortest distance between the two polyhedra (and similarly there is some vertex $v_{j}$ such that if $P(v_{j})$ is its projection onto $conv(u_{1}, \dots  , u_{p})$ then the length of the line segment $(v_{j}, P(v_{j}))$ is the shortest distance between the two polyhedra). If the two subsets are separable, in which case Problem $(SVM_{h1})$ has an optimal solution $\delta  > 0$, because the objective function is convex and the convex constraint $\|w\|_{2} \le 1$ is qualified since $\delta$  may be negative, by Theorem 50.17(2) the duality gap is zero, so $\delta$  is half of the
