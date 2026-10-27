# ADMM: Alternating Direction Method of Multipliers


<!-- PAGE 1914 -->
As an exercise, the reader should verify that dual ascent (with $\alpha^{k} = \rho$ ) yields the equations
$$x^{k+1}= \frac{\lambda^{k}}{2\beta}$$
$$y^{k+1}= - \frac{\lambda^{k}}{\beta}$$
$$\lambda^{k+1} = \begin{pmatrix} 2\rho \\ 1 + \\ \beta \end{pmatrix} \lambda^{k} ,$$
and so the method diverges, except for $\lambda^{0} = 0$, which is the optimal solution. The method of multipliers converges under conditions that are far more general than the dual ascent. However, the addition of the penalty term has the negative effect that even if $J$ is separable, then the Lagrangian $L_{\rho}$ is not separable. Thus the basic method of multipliers cannot be used for decomposition and is not parallelizable. The next method deals with the problem of separability.

## 52.3 ADMM: Alternating Direction Method of

$$Multipliers$$
The alternating direction method of multipliers, for short ADMM, combines the decomposability of dual ascent with the superior convergence properties of the method of multipliers. It can be viewed as an approximation of the method of multipliers, but it is generally superior. The idea is to split the function $J$ into two independent parts, as J(x, $z) =$ f(x) $+$ g(z), and to consider the Minimization Problem $(P_{admm})$,
$$minimizef(x) + g(z)$$
$$subject to Ax + Bz = c,$$
for some $p \times  n$ matrix $A$, some $p \times  m$ matrix $B$, and with $x \in \mathbb{R}^{n}, z \in \mathbb{R}^{m}$, and $c \in \mathbb{R}^{p}$. We also assume that $f$ and $g$ are convex. Further conditions will be added later. As in the method of multipliers, we form the augmented Lagrangian
$$L_{\rho}(x, z, \lambda ) = f(x) + g(z) + \lambda^{\top} (Ax + Bz -c) + (\rho /2) \|Ax + Bz -c\|_{2}^{2} ,$$
$$\mathbb{R}^{p}$$
with $\lambda  \in$ and for some $\rho  > 0$. Given some initial values $(z^{0}, \lambda^{0}$ ), the ADMM method consists of the following iterative steps:
$$x^{k+1}= arg minL_{\rho}(x, z^{k}, \lambda^{k} )$$
$$x$$
$$z^{k+1}= arg minL_{\rho}(x^{k+1}, z, \lambda^{k} )$$
$$z$$
$$\lambda^{k+1} = \lambda^{k} + \rho (Ax^{k+1}+ Bz^{k+1}-c).$$

<!-- PAGE 1915 -->
Instead of performing a minimization step jointly over $x$ and $z$, as the method of multipliers would in the step
$$(x^{k+1}, z^{k+1}) = arg minL_{\rho}(x, z, \lambda^{k} ),$$
$$x,z$$
ADMM first performs an x-minimization step, and then a z-minimization step. Thus $x$ and $z$ are updated in an alternating or sequential fashion, which accounts for the term alternating direction. The algorithm state in ADMM is $(z^{k}, \lambda^{k}$ ), in the sense that $(z^{k+1}, \lambda^{k+1}$ ) is a function of $(z^{k}, \lambda^{k}$ ). The variable $x^{k+1}$ is an auxiliary variable which is used to compute $z^{k+1}$ from $(z^{k}, \lambda^{k}$ ). The roles of $x$ and $z$ are not quite symmetric, since the update of $x$ is done before the update of $\lambda$ . By switching $x$ and $z, f$ and $g$ and $A$ and $B$, we obtain a variant of ADMM in which the order of the x-update step and the z-update step are reversed.

> **Example 52.4.** Let us reconsider the problem of Example 52.2 to solve it using ADMM. We formulate the problem as
$$minimize2x + z^{2}$$
$$subject to 2x -z = 0,$$
with f(x) $=$ 2x and g(z) $= z^{2}$. The augmented Lagrangian is given by
$$L_{\rho}(x, z, \lambda ) = 2x + z^{2}+ 2\lambda x -\lambda z + 2\rho x^{2}-2\rho xz + \frac{\rho}{2} z^{2}.$$
The ADMM steps are as follows. The x-update is
$$x^{k+1}= arg minx \begin{pmatrix} 2\rho x^{2}-2\rho xz^{k}+ 2\lambda^{k} x + 2x \end{pmatrix} ,$$
and since this is a quadratic function in $x$, its minimum is achieved when the derivative of the above function (with respect to $x)$ is zero, namely
$$- -$$
$$x^{k+1}= \frac{1}{2} z^{k} \frac{1}{2\rho} \lambda^{k} \frac{1}{2\rho} .(1)$$
The z-update is
$$z^{k+1}= arg minz \begin{pmatrix} \rho & - \\ z^{2}+ & z^{2} & 2\rho x^{k+1}z -\lambda^{k} z \\ 2 \end{pmatrix} ,$$
and as for the x-step, the minimum is achieved when the derivative of the above function (with respect to $z)$ is zero, namely
$$z^{k+1}= \frac{2\rho x^{k+1}}{\rho  + 2} + \frac{\lambda^{k}}{\rho  + 2} .(2)$$
The $\lambda$ -update is
$$\lambda^{k+1} = \lambda^{k} + \rho (2x^{k+1}-z^{k+1}).(3)$$

<!-- PAGE 1916 -->
Substituting the right hand side of $(1)$ for $x^{k+1}$ in $(2)$ yields
$$z^{k+1}= \frac{\rho z^{k}}{\rho  + 2} - \frac{1}{\rho  + 2} .(4)$$
Using $(2)$, we obtain
$$2x^{k+1}-z^{k+1}= \frac{4x^{k+1}}{\rho  + 2} - \frac{\lambda^{k}}{\rho  + 2} ,(5)$$
and then using $(3)$ we get
$$\lambda^{k+1} = \frac{2\lambda^{k}}{\rho  + 2} + \frac{4\rho x^{k+1}}{\rho  + 2} .(6)$$
Substituting the right hand side of $(1)$ for $x^{k+1}$ in $(6)$, we obtain
$$\lambda^{k+1} = \frac{2\rho z^{k}}{\rho  + 2} - \frac{2}{\rho  + 2} .(7)$$
Equation $(7)$ shows that $z^{k}$ determines $\lambda^{k+1}$ , and Equation $(1)$ for $k+2$, along with Equation $(4)$, shows that $z^{k}$ also determines $x^{k+2}$. In particular, we find that
$$- -$$
$$x^{k+2}= \frac{1}{2} z^{k+1} \frac{1}{2\rho} \lambda^{k+1} \frac{1}{2\rho}$$
$$-$$
$$= \frac{(\rho 2)z^{k}}{2(\rho  + 2)} - \frac{1}{\rho  + 2} .$$
Thus is suffices to find the limit of the sequence $(z^{k})$. Since we already know from Example 52.2 that this limit is $-1/2$, using $(4)$, we write
$$z^{k+1}= - \frac{1}{2} + \frac{\rho z^{k}}{\rho  + 2} - \frac{1}{\rho  + 2} + \frac{1}{2} = - \frac{1}{2} + \frac{\rho}{\rho  + 2} \begin{pmatrix} 1 \\ + z^{k} \\ 2 \end{pmatrix} .$$
By induction, we deduce that
$$k+1$$
$$z^{k+1}= - \frac{1}{2} + \begin{pmatrix} \rho \\ \rho  + 2 \end{pmatrix} \begin{pmatrix} 1 \\ + z^{0} \\ 2 \end{pmatrix} ,$$
and since $\rho  > 0$, we have $\rho /(\rho  + 2) < 1$, so the limit of the sequence $(z^{k+1})$ is indeed $-1/2$, and consequently the limit of $(\lambda^{k+1}$ ) is $-1$ and the limit of $x^{k+2}$ is $-1/4$. For ADMM to be practical, the x-minimization step and the z-minimization step have to be doable efficiently. It is often convenient to write the ADMM updates in terms of the scaled dual variable $\mu  = (1/\rho )\lambda$ . If we define the residual as
$$r = Ax + bz -c,$$
