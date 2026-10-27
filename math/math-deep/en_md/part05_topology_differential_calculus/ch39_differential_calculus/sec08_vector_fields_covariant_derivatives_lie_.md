# Vector Fields, Covariant Derivatives, Lie Brackets


<!-- PAGE 1486 -->
When $m = 1$, the above simplifies to the familiar formula
$$(g \circ f)'(a) = g'(b)f' (a),$$
and for $m = 2$, we have
$$(g \circ f)^{(2)}(a) = g^{(2)}(b)(f^{(1)}(a))^{2}+ g^{(1)}(b)f^{(2)}(a).$$

## 39.8 Vector Fields, Covariant Derivatives, Lie Brack-

$$ets$$
In this section, we briefly consider vector fields and covariant derivatives of vector fields. Such derivatives play an important role in continuous mechanics. Given a normed affine
$$\longrightarrow  \longrightarrow \longrightarrow$$
space $(E, E$ ), a vector field over $(E, E$ ) is a function $X$ : $E \to E$ . Intuitively, a vector field assigns a vector to every point in $E$. Such vectors could be forces, velocities, accelerations, etc. Given two vector fields $X, Y$ defined on some open subset $\Omega$ of $E$, for every point $a \in \Omega$ , we would like to define the derivative of $X$ with respect to $Y$ at a. This is a type of directional derivative that gives the variation of $X$ as we move along $Y$ , and we denote it by $D_{Y}$ X(a). The derivative $D_{Y}$ X(a) is defined as follows.
$$\longrightarrow$$

> **Definition 39.22.** Let $(E, E$ ) be a normed affine space. Given any open subset $\Omega$ of $E$, given any two vector fields $X$ and $Y$ defined over $\Omega$ , for any $a \in \Omega$ , the covariant derivative (or Lie derivative) of $X$ w.r.t. the vector field $Y$ at a, denoted by $D_{Y}$ X(a), is the limit (if it exists)
$$-$$
$$t\to lim0, t\in U \frac{X(a + tY (a))X(a)}{t} ,$$
where $U = {t \in \mathbb{R}$ | $a +$ tY $(a) \in \Omega , t \neq  0}$. If $Y$ is a constant vector field, it is immediately verified that the map
$$X \mapsto D_{Y} X(a)$$
is a linear map called the derivative of the vector field $X$, and denoted by DX(a). If $f$ : $E \to \mathbb{R}$ is a function, we define $D_{Y}$ f(a) as the limit (if it exists)
$$-$$
$$t\to lim0, t\in U \frac{f(a + tY (a))f(a)}{t} ,$$
where $U = {t \in \mathbb{R}$ | $a +$ tY $(a) \in \Omega , t \neq  0}$. It is the directional derivative of $f$ w.r.t. the vector field $Y$ at a, and it is also often denoted by $Y$ (f)(a), or $Y (f)_{a}$. From now on, we assume that all the vector fields and all the functions under consideration are smooth $(C^{\infty})$. The set $C^{\infty}(\Omega$ ) of smooth $C^{\infty}-functions f$ : $\Omega \to \mathbb{R}$ is a ring. Given a

<!-- PAGE 1487 -->
smooth vector field $X$ and a smooth function $f$ (both over $\Omega$ ), the vector field fX is defined such that (fX)(a) $=$ f(a)X(a), and it is immediately verified that it is smooth. Thus, the set $\mathcal{X}(\Omega$ ) of smooth vector fields over $\Omega$ is a $C^{\infty}(\Omega$ )-module. The following proposition is left as an exercise. It shows that $D_{Y}$ X(a) is $a \mathbb{R}-bilinear$ map on $\mathcal{X}(\Omega$ ), is $C^{\infty}(\Omega$ )-linear in $Y$ , and satisfies the Leibniz derivation rules with respect to $X$.

> **Proposition 39.28.** The covariant derivative $D_{Y}$ X(a) satisfies the following properties:
$$D_{(Y1+Y2)}X(a) = D_{Y1}X(a) + D_{Y2}X(a),$$
$$D_{fY} X(a) = f(a)D_{Y} X(a),$$
$$D_{Y} (X_{1} + X_{2})(a) = D_{Y} X_{1}(a) + D_{Y} X_{2}(a),$$
$$D_{Y} fX(a) = D_{Y} f(a)X(a) + f(a)D_{Y} X(a),$$
where $X, Y, X_{1}, X_{2}, Y_{1}, Y_{2}$ are smooth vector fields over $\Omega$ , and $f$ : $E \to \mathbb{R}$ is a smooth function. In differential geometry, the above properties are taken as the axioms of affine connections, in order to define covariant derivatives of vector fields over manifolds. In many cases, the vector field $Y$ is the tangent field of some smooth curve $\gamma$  : ] - $\eta , \eta [\to E$. If so, the following proposition holds.

> **Proposition 39.29.** Given a smooth curve $\gamma$  : ] - $\eta , \eta [\to E$, letting $Y$ be the vector field defined on $\gamma$ (] - $\eta , \eta$ [) such that
$$Y (\gamma (u)) = \frac{d\gamma}{dt} (u),$$
for any vector field $X$ defined on $\gamma$ (] - $\eta , \eta$ [), we have
$$$$
$$D_{Y} X(a) = \frac{d}{dt} X(\gamma (t))(0),$$
where $a = \gamma (0)$. The derivative $D_{Y}$ X(a) is thus the derivative of the vector field $X$ along the curve $\gamma$ , and it is called the covariant derivative of $X$ along $\gamma$ .
$$\longrightarrow$$
Given an affine frame $(O, (u_{1}, \dots  , u_{n}))$ for $(E, E$ ), it is easily seen that the covariant derivative $D_{Y}$ X(a) is expressed as follows:
$$D_{Y} X(a) = \sum_{i=1j}^{n}  \sum_{=1}^{n}  \begin{pmatrix} \partial X_{i} \\ Y_{j} \\ \partial x_{j} \end{pmatrix} (a)e_{i}.$$
Generally, $D_{Y}$ X(a) $\neq  D_{X}Y$ (a). The quantity
$$[X, Y ] = D_{X}Y -D_{Y} X$$
