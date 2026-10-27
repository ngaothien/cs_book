# Jacobian Matrices


<!-- PAGE 1457 -->
This notion is a generalization of the notion defined in Definition 39.5. In fact, when $E$ is of dimension $n$, and a frame $(a_{0}, (u_{1}, \dots  , u_{n}))$ has been chosen, we can write $E = (E_{1}, a_{1}) \oplus \cdots  \oplus (E_{n}, a_{n})$, for some obvious $(E_{j}, a_{j})$ (as explained just after Proposition 39.9), and then
$$D_{j}f(c)(\lambda u_{j}) = \lambda \partial_{j} f(c),$$
and the two notions are consistent. The definition of $i_{j}^{c}$ and of $D_{j}f(c)$ also makes sense for a finite product $E_{1} \times  \cdots  \times  E_{n}$ of affine spaces $E_{i}$. We will use freely the notation $\partial_{j}$ f(c) instead of $D_{j}f(c)$. The notion $\partial_{j}$ f(c) introduced in Definition 39.5 is really that of the vector derivative, whereas $D_{j}f(c)$ is the corresponding linear map. Although perhaps confusing, we identify the two notions. The following proposition holds.

> **Proposition 39.11.** Given a normed affine space $E = (E_{1}, a_{1}) \oplus \cdots  \oplus (E_{n}, a_{n})$, and a normed affine space $F$, given any open subset $A$ of $E$, for any function $f$ : $A \to F$, for every $c \in A$, if Df(c) exists, then each $D_{j}f(c)$ exists, and
$$Df(c)(u_{1}, \dots  , u_{n}) = D_{1}f(c)(u_{1}) + \cdots  + D_{n}f(c)(u_{n}),$$
for every $u_{i} \in E_{i}, 1 \le i \le n$. The same result holds for the finite product $E_{1} \times  \cdots  \times  E_{n}$.

*Proof.* Since every $c \in E$ can be written as $c = a + c$ - $a$, where $a = (a_{1}, \dots  , a_{n})$, defining $\longrightarrow \longrightarrow f_{a}$ : $E \to F$ such that, $f_{a}(u) =$ f(a $+ u)$, for every $u \in E$ , clearly, Df(c) $= Df_{a}(c$ - $a)$, and
$$\longrightarrow$$
thus, we can work with the function $f_{a}$ whose domain is the vector space $E$ . The proposition is then a simple application of Theorem 39.6.

## 39.3 Jacobian Matrices

If both $E$ and $F$ are of finite dimension, for any frame $(a_{0}, (u_{1}, \dots  , u_{n}))$ of $E$ and any frame $(b_{0}, (v_{1}, \dots  , v_{m}))$ of $F$, every function $f$ : $E \to F$ is determined by $m$ functions $f_{i}$ : $E \to \mathbb{R}$ (or $f_{i}$ : $E \to \mathbb{C})$, where
$$f(x) = b_{0} + f_{1}(x)v_{1} + \cdots  + f_{m}(x)v_{m},$$
for every $x \in E$. From Proposition 39.1, we have
$$Df(a)(u_{j}) = D_{uj}f(a) = \partial_{j} f(a),$$
and from Proposition 39.10, we have
$$Df(a)(u_{j}) = Df_{1}(a)(u_{j})v_{1} + \cdots  + Df_{i}(a)(u_{j})v_{i} + \cdots  + Df_{m}(a)(u_{j})v_{m},$$
that is,
$$Df(a)(u_{j}) = \partial_{j} f_{1}(a)v_{1} + \cdots  + \partial_{j} f_{i}(a)v_{i} + \cdots  + \partial_{j} f_{m}(a)v_{m}.$$

<!-- PAGE 1458 -->
Since the $j$-th column of the $m\times n$-matrix representing Df(a) w.r.t. the bases $(u_{1}, \dots  , u_{n})$ and $(v_{1}, \dots  , v_{m})$ is equal to the components of the vector $Df(a)(u_{j})$ over the basis $(v_{1}, \dots  ,v_{m})$, the linear map Df(a) is determined by the $m \times n$-matrix J(f)(a) $= (\partial_{j} f_{i}(a))$, (or J(f)(a) $=$
$$( \frac{\partial f_{i}}{\partial x_{j}} (a))):$$
$$J(f)(a) = \begin{pmatrix} \partial_{1} f_{1}(a) & \partial_{2} f_{1}(a) & \dots & \partial_{n} f_{1}(a) \\ \partial_{1} f_{2}(a) & \partial_{2} f_{2}(a) & \dots & \partial_{n} f_{2}(a) \\ \vdots & \vdots & \ddots & \vdots \\ \partial_{1} f_{m}(a) & \partial_{2} f_{m}(a) & \dots & \partial_{n} f_{m}(a) \end{pmatrix}$$
or
$$J(f)(a) = \begin{pmatrix} \partial f_{1} & \partial f_{1} & \partial f_{1} \\ (a) & (a) & \dots & (a) \\ \partial x_{1} & \partial x_{2} & \partial x_{n} \\ \partial f_{2} & \partial f_{2} & \partial f_{2} \\ (a) & (a) & \dots & (a) \\ \partial x_{1} & \partial x_{2} & \partial x_{n} \\ \vdots & \vdots & \ddots & \vdots \\ \partial f_{m} & \partial f_{m} & \partial f_{m} \\ (a) & (a) & \dots & (a) \\ \partial x_{1} & \partial x_{2} & \partial x_{n} \end{pmatrix}$$

> **Definition 39.6.** The matrix J(f)(a) is called the Jacobian matrix of Df at a. When $m = n$, the determinant, det(J(f)(a)), of J(f)(a) is called the Jacobian of Df(a). From a previous result, we know that this determinant in fact only depends on Df(a), and not on specific bases. However, partial derivatives give a means for computing it.
$$\mathbb{R}^{n}  \mathbb{R}^{m} \mathbb{R}^{n} \mathbb{R}^{m}$$
When $E =$ and $F =$ , for any function $f$ : $\to$ , it is easy to compute the
$$partial derivatives \frac{\partial f_{i}}{\partial x_{j}} (a). We simply treat the function f_{i} : \mathbb{R}^{n}\to \mathbb{R} as a function of its j-th$$
argument, leaving the others fixed, and compute the derivative as in Definition 39.1, that is, the usual derivative.
$$\mathbb{R}^{2} \mathbb{R}^{2}$$

> **Example 39.5.** For example, consider the function $f$ : $\to$ , defined such that
$$f(r, \theta ) = (r \cos(\theta ), r \sin(\theta )).$$
Then, we have
$$J(f)(r, \theta ) = \begin{pmatrix} \cos(\theta ) & -r \sin(\theta ) \\ \sin(\theta ) & r \cos(\theta ) \end{pmatrix}$$
and the Jacobian (determinant) has value det(J(f)(r, $\theta$ )) $= r$. In the case where $E = \mathbb{R}$ (or $E = \mathbb{C})$, for any function $f$ : $\mathbb{R} \to F$ (or $f$ : $\mathbb{C} \to F)$, the Jacobian matrix of Df(a) is a column vector. In fact, this column vector is just $D_{1}f(a)$. Then, for every $\lambda  \in \mathbb{R}$ (or $\lambda  \in \mathbb{C})$,
$$Df(a)(\lambda ) = \lambda D_{1}f(a).$$
This case is sufficiently important to warrant a definition.

<!-- PAGE 1459 -->

> **Definition 39.7.** Given a function $f$ : $\mathbb{R} \to F$ (or $f$ : $\mathbb{C} \to F)$, where $F$ is a normed affine space, the vector
$$Df(a)(1) = D_{1}f(a)$$
is called the vector derivative or velocity vector (in the real case) at a. We usually identify Df(a) with its Jacobian matrix $D_{1}f(a)$, which is the column vector corresponding to $D_{1}f(a)$. By abuse of notation, we also let Df(a) denote the vector Df(a)(1) $= D_{1}f(a)$. When $E = \mathbb{R}$, the physical interpretation is that $f$ defines a (parametric) curve that is
$$\mathbb{R}^{m}$$
the trajectory of some particle moving in as a function of time, and the vector $D_{1}f(a)$ is the velocity of the moving particle f(t) at $t = a$. It is often useful to consider functions $f$ : [a, $b] \to F$ from a closed interval [a, $b] \subseteq \mathbb{R}$ to a normed affine space $F$, and its derivative Df(a) on [a, $b]$, even though [a, $b]$ is not open. In this case, as in the case of a real-valued function, we define the right derivative $D_{1}f(a_{+})$ at a, and the left derivative $D_{1}f(b_{-})$ at $b$, and we assume their existence.

> **Example 39.6.** $1$. When $A = (0, 1)$ and $F =\mathbb{R}^{3}$, a function
$$\mathbb{R}^{3}  \mathbb{R}^{3}$$
$f$ : $(0, 1) \to$ defines a (parametric) curve in . If $f = (f_{1}, f_{2}, f_{3})$, its Jacobian matrix at $a \in \mathbb{R}$ is
$$J(f)(a) = \begin{pmatrix} \partial f_{1} \\ (a) \\ \partial t \\ \partial f_{2} \\ (a) \\ \partial t \\ \partial f_{3} \\ (a) \end{pmatrix} .$$
$$\partial t$$
See Figure 39.4.
$$Figure 39.4: The red space curve f(t) = (\cos(t), \sin(t), t).$$

<!-- PAGE 1460 -->
$$The velocity vectors J(f)(a) = \begin{pmatrix} -\sin(t) \\ \cos(t) \\ 1 \end{pmatrix} are represented by the blue arrows.$$
$$\mathbb{R}^{2}  \mathbb{R}^{3} \mathbb{R}^{2} \mathbb{R}^{3}$$
$2$. When $E =$ and $F =$ , a function $\phi$ : $\to$ defines a parametric surface.
$$\mathbb{R}^{2}$$
Letting $\phi  = (f, g, h)$, its Jacobian matrix at $a \in$ is
$$J(\phi )(a) = \begin{pmatrix} \partial f & \partial f \\ (a) & (a) \\ \partial u & \partial v \\ \partial g & \partial g \\ (a) & (a) \\ \partial u & \partial v \\ \partial h & \partial h \\ (a) & (a) \end{pmatrix} .$$
$$\partial u\partial v$$
$$See Figure 39.5. The Jacobian matrix is J(f)(a) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 2u & 2v \end{pmatrix} . The first column is$$
$$Figure 39.5: The parametric surface x = u, y = v, z = u^{2}+ v^{2}.$$
the vector tangent to the pink u-direction curve, while the second column is the vector tangent to the blue v-direction curve.
$$\mathbb{R}^{3} \mathbb{R} \mathbb{R}^{3} \mathbb{R}\mathbb{R}^{3}$$
$3$. When $E =$ and $F =$ , for a function $f$ : $\to$ , the Jacobian matrix at $a \in$ is
$$J(f)(a) = \begin{pmatrix} \partial f & \partial f & \partial f \\ (a) & (a) & (a) \\ \partial x & \partial y & \partial z \end{pmatrix} .$$
$$\mathbb{R}^{n} \mathbb{R}\mathbb{R}^{n}$$

> **Definition 39.8.** More generally, when $f$ : $\to$ , the Jacobian matrix at $a \in$ is the row vector
$$J(f)(a) = \begin{pmatrix} \partial f \\ \partial f \\ (a)\cdots & (a) \\ \partial x_{1} & \partial x_{n} \end{pmatrix} .$$

<!-- PAGE 1461 -->
Its transpose is a column vector called the gradient of $f$ at a, denoted by gradf(a) or $\nabla$ f(a). Then, given any $v \in \mathbb{R}^{n}$, note that
$$Df(a)(v) = \frac{\partial f}{\partial x_{1}} (a) v_{1} + \cdots  + \frac{\partial f}{\partial x_{n}} (a) v_{n} = gradf(a) \cdot  v,$$
the scalar product of gradf(a) and $v$.
$$\mathbb{R}^{n} \mathbb{R}^{m} \mathbb{R}$$

> **Example 39.7.** Consider the function $f$ : $\times \to$  from Example 39.4 given by
$$f(v, \lambda ) = \lambda^{\top} Cv = v^{\top}C^{\top}\lambda ,v \in \mathbb{R}^{n}, \lambda  \in \mathbb{R}^{m},$$
where $C$ is an $m \times  n$ matrix. We showed that its derivative is given by
$$df_{(v,\lambda)}(w, \mu ) = (C^{\top}\lambda )^{\top}w + (Cv)^{\top}\mu  = (C^{\top}\lambda Cv)^{\top} \begin{pmatrix} v \\ \lambda \end{pmatrix} ,$$
so the gradient of $f$ at $(v, \lambda$ ) is
$$\nabla f_{(v,\lambda)} = \begin{pmatrix} C^{\top}\lambda \\ Cv \end{pmatrix} .$$
$$\mathbb{R}^{n} \mathbb{R}$$

> **Example 39.8.** Consider the quadratic function $f$ : $\to$  given by
$$f(x) = x^{\top}Ax,x \in \mathbb{R}^{n},$$
where $A$ is a real $n \times  n$ symmetric matrix. We claim that
$$df_{u}(h) = 2u^{\top}Ahfor all u, h \in \mathbb{R}^{n}.$$
Since $A$ is symmetric, we have
$$f(u + h) = (u^{\top}+ h^{\top})A(u + h)$$
$$= u^{\top}Au + u^{\top}Ah + h^{\top}Au + h^{\top}Ah$$
$$= u^{\top}Au + 2u^{\top}Ah + h^{\top}Ah,$$
so we have
$$f(u + h) -f(u) -2u^{\top}Ah = h^{\top}Ah.$$
If we write
$$\epsilon (h) = \frac{h^{\top}Ah}{\|h\|}$$
for $h \in / 0$ where $\|\|$ is the 2-norm, by Cauchy–Schwarz we have
$$\|$$
$$\|\|\|\|\|\|^{2}\|$$
$$|\epsilon (h)| \le \frac{hAh}{\|h\|} \le \frac{hA}{\|h\|} = \|h\|\|A\|,$$

<!-- PAGE 1462 -->
which shows that $lim_{h\mapsto0} \epsilon (h) = 0$. Therefore,
$$df_{u}(h) = 2u^{\top}Ahfor all u, h \in \mathbb{R}^{n},$$
as claimed. This formula shows that the gradient $\nabla f_{u}$ of $f$ at $u$ is given by
$$\nabla f_{u} = 2Au.$$
As a first corollary we obtain the gradient of a function of the form
$$f(x) = \frac{1}{2} x^{\top}Ax -b^{\top}x,$$
where $A$ is a symmetric $n \times  n$ matrix and $b$ is some vector $b \in \mathbb{R}^{n}$. Since the derivative of a linear function is itself, we obtain
$$df_{u}(h) = u^{\top}Ah -b^{\top}h,$$
and the gradient of $f$ is given by
$$\nabla f_{u} = Au -b.$$
As a second corollary we obtain the gradient of the function
$$f(x) = \|Ax -b\|_{2}^{2} = (Ax -b)^{\top}(Ax -b) = (x^{\top}A^{\top}-b^{\top})(Ax -b)$$
which is the function to minimize in a least squares problem, where $A$ is an $m \times  n$ matrix. We have
$$f(x) = x^{\top}A^{\top}Ax -x^{\top}A^{\top}b -b^{\top}Ax + b^{\top}b = x^{\top}A^{\top}Ax -2b^{\top}Ax + b^{\top}b,$$
and since the derivative of a constant function is $0$ and the derivative of a linear function is itself, we get
$$df_{u}(h) = 2u^{\top}A^{\top}Ah -2b^{\top}Ah.$$
Consequently, the gradient of $f$ is given by
$$\nabla f_{u} = 2A^{\top}Au -2A^{\top}b.$$

> **Example 39.9.** In Example 40.3 from Section 40.1, we need to find the gradient of the function
$$L(v, \lambda ) = \frac{1}{2} v^{\top}Av -v^{\top}b + v^{\top}C^{\top}\lambda  -d^{\top}\lambda ,$$
where $A$ is an $n \times  n$ symmetric matrix and $C$ is an $m \times  n$ matrix of rank $m$. From Example 39.7 and Example 39.8, we have
$$\nabla L_{((v,\lambda)} = \begin{pmatrix} Av -b \\ 0 \end{pmatrix} + \begin{pmatrix} C^{\top}\lambda \\ Cv \end{pmatrix} + \begin{pmatrix} 0 \\ -d \end{pmatrix} = \begin{pmatrix} Av -b + C^{\top}\lambda \\ Cv -d \end{pmatrix} .$$

<!-- PAGE 1463 -->
When $E, F$, and $G$ have finite dimensions, and $(a_{0}, (u_{1}, \dots  , u_{p}))$ is an affine frame for $E, (b_{0}, (v_{1}, \dots  , v_{n}))$ is an affine frame for $F$, and $(c_{0}, (w_{1}, \dots  , w_{m}))$ is an affine frame for $G$, if $A$ is an open subset of $E, B$ is an open subset of $F$, for any functions $f$ : $A \to F$ and $g: B \to G$, such that f(A) $\subseteq B$, for any $a \in A$, letting $b =$ f(a), and $h = g \circ f$, if Df(a) exists and Dg(b) exists, by Theorem 39.6, the Jacobian matrix J(h)(a) $=$ J(g $\circ$ f)(a) w.r.t. the bases $(u_{1}, \dots  , u_{p})$ and $(w_{1}, \dots  , w_{m})$ is the product of the Jacobian matrices J(g)(b) w.r.t. the bases $(v_{1}, \dots  , v_{n})$ and $(w_{1}, \dots  , w_{m})$, and J(f)(a) w.r.t. the bases $(u_{1}, \dots  , u_{p})$ and $(v_{1}, \dots  , v_{n})$:
$$J(h)(a) = \begin{pmatrix} \partial_{1} g_{1}(b) & \partial_{2} g_{1}(b) & \dots & \partial_{n} g_{1}(b) \\ \partial_{1} g_{2}(b) & \partial_{2} g_{2}(b) & \dots & \partial_{n} g_{2}(b) \\ \vdots & \vdots & \ddots & \vdots \\ \partial_{1} g_{m}(b) & \partial_{2} g_{m}(b) & \dots & \partial_{n} g_{m}(b) \end{pmatrix} \begin{pmatrix} \partial_{1} f_{1}(a) & \partial_{2} f_{1}(a) & \dots & \partial_{p} f_{1}(a) \\ \partial_{1} f_{2}(a) & \partial_{2} f_{2}(a) & \dots & \partial_{p} f_{2}(a) \\ \vdots & \vdots & \ddots & \vdots \\ \partial_{1} f_{n}(a) & \partial_{2} f_{n}(a) & \dots & \partial_{p} f_{n}(a) \end{pmatrix}$$
or
$$J(h)(a) = \begin{pmatrix} \partial g_{1} & \partial g_{1} & \partial g_{1} \\ (b) & (b) & \dots & (b) \\ \partial y_{1} & \partial y_{2} & \partial y_{n} \\ \partial g_{2} & \partial g_{2} & \partial g_{2} \\ (b) & (b) & \dots & (b) \\ \partial y_{1} & \partial y_{2} & \partial y_{n} \\ \vdots & \vdots & \ddots & \vdots \\ \partial g_{m} & \partial g_{m} & \partial g_{m} \\ (b) & (b) & \dots & (b) \\ \partial y_{1} & \partial y_{2} & \partial y_{n} \end{pmatrix} \begin{pmatrix} \partial f_{1} & \partial f_{1} & \partial f_{1} \\ (a) & (a) & \dots & (a) \\ \partial x_{1} & \partial x_{2} & \partial x_{p} \\ \partial f_{2} & \partial f_{2} & \partial f_{2} \\ (a) & (a) & \dots & (a) \\ \partial x_{1} & \partial x_{2} & \partial x_{p} \\ \vdots & \vdots & \ddots & \vdots \\ \partial f_{n} & \partial f_{n} & \partial f_{n} \\ (a) & (a) & \dots & (a) \\ \partial x_{1} & \partial x_{2} & \partial x_{p} \end{pmatrix} .$$
Thus, we have the familiar formula
$$\frac{\partial h_{i}}{\partial x_{j}} (a) = \sum_{k=1}^{k=n}  \frac{\partial g_{i}}{\partial y_{k}} (b) \frac{\partial f_{k}}{\partial x_{j}} (a).$$
Given two normed affine spaces $E$ and $F$ of finite dimension, given an open subset $A$ of $E$, if a function $f$ : $A \to F$ is differentiable at $a \in A$, then its Jacobian matrix is well defined.  One should be warned that the converse is false. There are functions such that all the partial derivatives exist at some $a \in A$, but yet, the function is not differentiable at a,
$$\mathbb{R}^{2} \mathbb{R}$$
and not even continuous at a. For example, consider the function $f$ : $\to$ , defined such that f(0, $0) = 0$, and
$$f(x, y) = \frac{x^{2}y}{x^{4}+ y^{2}} if (x, y) \neq  (0, 0).$$
$$For any u \neq  0, letting u = \begin{pmatrix} h \\ k \end{pmatrix} , we have$$
$$\frac{f(0 + tu)f(0)}{t} -= \frac{h^{2}k}{t^{2}h^{4}+ k^{2}} ,$$

<!-- PAGE 1464 -->
so that
$$h2$$
$$if k \neq  0$$
$$D_{u}f(0, 0) =$$
$$0^{k}if k = 0.$$
Thus, $D_{u}f(0, 0)$ exists for all $u \neq  0$. On the other hand, if Df(0, $0)$ existed, it would be
$$\mathbb{R}^{2} \mathbb{R}$$
a linear map Df(0, $0): \to$  represented by a row matrix $(\alpha  \beta$ ), and we would have $D_{u}f(0, 0) =$ Df(0, 0)(u) $= \alpha h + \beta k$, but the explicit formula for $D_{u}f(0, 0)$ is not linear. As a matter of fact, the function $f$ is not continuous at $(0, 0)$. For example, on the parabola $y = x^{2}$, f(x, $y) =_{2}^{1}$ , and when we approach the origin on this parabola, the limit $is_{2}^{1}$ , when in fact, f(0, $0) = 0$. However, there are sufficient conditions on the partial derivatives for Df(a) to exist, namely, continuity of the partial derivatives.
$$\longrightarrow  \longrightarrow$$
If $f$ is differentiable on $A$, then $f$ defines a function Df : $A \to$ L(E ; $F$ ). It turns out that the continuity of the partial derivatives on $A$ is a necessary and sufficient condition for Df to exist and to be continuous on $A$. If $f$ : [a, $b] \to \mathbb{R}$ is a function which is continuous on [a, $b]$ and differentiable on (a, $b)$, then there is some $c$ with a $< c < b$ such that
$$f(b) -f(a) = (b -a)f' (c).$$
This result is known as the mean value theorem and is a generalization of Rolle’s theorem, which corresponds to the case where f(a) $=$ f(b). Unfortunately, the mean value theorem fails for vector-valued functions. For example,
$$\mathbb{R}^{2}$$
the function $f$ : $[0, 2\pi$ ] $\to$ given by
$$f(t) = (\cos t, \sin t)$$
is such that $f(2\pi$ ) -f(0) $= (0, 0)$, yet its derivative f' $(t) =$ (-sin $t$, cos $t)$ does not vanish in $(0, 2\pi$ ). A suitable generalization of the mean value theorem to vector-valued functions is possible if we consider an inequality (an upper bound) instead of an equality. This generalized version of the mean value theorem plays an important role in the proof of several major results of differential calculus. If $E$ is an affine space (over $\mathbb{R}$ or $\mathbb{C})$, given any two points a, $b \in E$, the closed segment [a, $b]$ is the set of all points $a + \lambda (b$ - $a)$, where $0 \le \lambda  \le 1, \lambda  \in \mathbb{R}$, and the open segment (a, $b)$ is the set of all points $a + \lambda (b$ - $a)$, where $0 < \lambda  < 1, \lambda  \in \mathbb{R}$.

> **Proposition 39.12.** Let $E$ and $F$ be two normed affine spaces, let $A$ be an open subset of $E$, and let $f$ : $A \to F$ be a continuous function on $A$. Given any $a \in A$ and any $h \neq  0$ in $\longrightarrow E$ , if the closed segment [a, $a + h]$ is contained in $A$, if $f$ : $A \to F$ is differentiable at every point of the open segment (a, $a + h)$, and
$$\sup\|Df(x)\|\le M,$$
$$x\in (a,a+h)$$
