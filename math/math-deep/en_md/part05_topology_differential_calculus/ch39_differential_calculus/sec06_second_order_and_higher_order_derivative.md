# Second-Order and Higher-Order Derivatives


<!-- PAGE 1474 -->
The proof is actually rather simple. We have $T_{a}(\Gamma$ ) $= a + T_{a}(\Gamma$ ), and since $T_{a}(\Gamma$ ) is a
$$\longrightarrow \times  \longrightarrow$$
subspace of $E F$ , the set $T_{a}(\Gamma$ ) is an affine variety. Thus, the affine tangent space at a point (a, f(a)) is a familar object, a line, a plane, etc.
$$\mathbb{R}^{2} \mathbb{R}$$
As an illustration, when $E =$ and $F =$ , the affine tangent plane at the point (a, $b, c)$ to the surface of equation $z =$ f(x, $y)$, is defined by the equation
$$z = c + \frac{\partial f}{\partial x} (a, b)(x -a) + \frac{\partial f}{\partial y} (a, b)(y -b).$$
If $E = \mathbb{R}$ and $F = \mathbb{R}^{2}$, the tangent line at (a, $b, c)$, to the curve of equations $y =$ g(x), $z =$ h(x), is defined by the equations
$$y = b + Dg(a)(x -a),$$
$$z = c + Dh(a)(x -a).$$
Thus, derivatives and partial derivatives have the desired intended geometric interpretation as tangent spaces. Of course, in order to deal with this topic properly, we really would have to go deeper into the study of (differential) manifolds. We now briefly consider second-order and higher-order derivatives.

## 39.6 Second-Order and Higher-Order Derivatives

Given two normed affine spaces $E$ and $F$, and some open subset $A$ of $E$, if Df(a) is defined
$$\longrightarrow  \longrightarrow \longrightarrow  \longrightarrow$$
for every $a \in A$, then we have a mapping Df : $A \to$ L(E ; $F$ ). Since $\mathcal{L}(E$ ; $F$ ) is a normed vector space, if Df exists on an open subset $U$ of $A$ containing a, we can consider taking the derivative of Df at some $a \in A$.

> **Definition 39.14.** Given a function $f$ : $A \to F$ defined on some open subset $A$ of $E$ such that Df(a) is defined for every $a \in A$, If D(Df)(a) exists for every $a \in A$, we
$$\longrightarrow \longrightarrow  \longrightarrow$$
get a mapping $D^{2}f$ : $A \to$ L(E $;\mathcal{L}(E$ ; $F$ )) called the second derivative of $f$ on $A$, where $D^{2}f(a) =$ D(Df)(a), for every $a \in A$. As in the case of the first derivative $Df_{a}$ where $Df_{a}(u) = D_{u}f(a)$, where $D_{u}f(a)$ is the directional derivative of $f$ at a in the direction $u$, it would be useful to express $D^{2}f(a)(u)(v)$ in terms of two directional derivatives. This can indeed be done. If $D^{2}f(a)$ exists, then for
$$\longrightarrow$$
every $u \in E$ ,
$$\longrightarrow  \longrightarrow$$
$$D^{2}f(a)(u) = D(Df)(a)(u) = D_{u}(Df)(a) \in L(E ;F ).$$
We have the following result.

> **Proposition 39.19.** If $D^{2}f(a)$ exists, then $D_{u}(D_{v}f)(a)$ exists and
$$\longrightarrow$$
$$D^{2}f(a)(u)(v) = D_{u}(D_{v}f)(a),for all u, v \in E .$$

<!-- PAGE 1475 -->
$$\longrightarrow  \longrightarrow  \times  \longrightarrow  \longrightarrow$$

*Proof.* Recall from Proposition 37.61, that the map app from $\mathcal{L}(E$ ; $F$ ) $E$ to $F$ , defined
$$\longrightarrow  \longrightarrow \longrightarrow$$
such that for every $L \in$ L(E ; $F$ ), for every $v \in E$ ,
$$app(L, v) = L(v),$$
$$\longrightarrow$$
is a continuous bilinear map. Thus, in particular, given a fixed $v \in E$ , the linear map
$$\longrightarrow  \longrightarrow \longrightarrow$$
$app_{v}$ : $\mathcal{L}(E$ ; $F$ ) $\to F$ , defined such that $app_{v}(L) =$ L(v), is a continuous map. Also recall from Proposition 39.7, that if $h: A \to G$ is a function such that Dh(a) exits, and $k: G \to H$ is a continuous linear map, then, D(k $\circ$ h)(a) exists, and
$$k(Dh(a)(u)) = D(k \circ h)(a)(u),$$
that is,
$$k(D_{u}h(a)) = D_{u}(k \circ h)(a),$$
Applying these two facts to $h =$ Df, and to $k = app_{v}$, we have
$$D_{u}(Df)(a)(v) = D_{u}(app_{v} \circ Df)(a).$$
But $(app_{v} \circ$ Df)(x) $=$ Df(x)(v) $= D_{v}f(x)$, for every $x \in A$, that is, $app_{v} \circ$ Df $= D_{v}f$ on $A$. So, we have
$$D_{u}(Df)(a)(v) = D_{u}(D_{v}f)(a),$$
and since $D^{2}f(a)(u) = D_{u}(Df)(a)$, we get
$$D^{2}f(a)(u)(v) = D_{u}(D_{v}f)(a).$$
Thus, when $D^{2}f(a)$ exists, $D_{u}(D_{v}f)(a)$ exists, and
$$D^{2}f(a)(u)(v) = D_{u}(D_{v}f)(a),$$
$$\longrightarrow$$
for all $u, v \in E$ .

> **Definition 39.15.** We denote $D_{u}(D_{v}f)(a)$ by $D_{u,v}^{2}f(a)$ (or $D_{u}D_{v}f(a))$.
$$\longrightarrow  \longrightarrow  \longrightarrow \longrightarrow \longrightarrow  \longrightarrow$$
Recall from Proposition 37.60, that the map from $\mathcal{L}_{2}(E , E$ ; $F$ ) to $\mathcal{L}(E ;\mathcal{L}(E$ ; $F$ )) de-
$$\longrightarrow  \longrightarrow  \longrightarrow$$
fined such that $g \mapsto \phi$  iff for every $g \in L_{2}(E , E$ ; $F$ ),
$$\phi (u)(v) = g(u, v),$$
$$\longrightarrow \longrightarrow  \longrightarrow$$
is an isomorphism of vector spaces. Thus, we will consider $D^{2}f(a) \in$ L(E $;\mathcal{L}(E$ ; $F$ ))
$$\longrightarrow  \longrightarrow  \longrightarrow$$
as a continuous bilinear map in $\mathcal{L}_{2}(E , E$ ; $F$ ), and we will write $D^{2}f(a)(u, v)$, instead of $D^{2}f(a)(u)(v)$. Then, the above discussion can be summarized by saying that when $D^{2}f(a)$ is defined, we have
$$D^{2}f(a)(u, v) = D_{u}D_{v}f(a).$$

<!-- PAGE 1476 -->

> **Definition 39.16.** When $E$ has finite dimension and $(a_{0}, (e_{1}, \dots  , e_{n}))$ is a frame for $E$, we
$$denote D_{ej}D_{ei}f(a) by \frac{\partial^{2} f}{\partial x_{i}\partial x_{j}} (a), when i \neq  j, and we denote D_{ei}D_{ei}f(a) by \frac{\partial^{2} f}{\partial x_{i}^{2}} (a).$$
The following important lemma attributed to Schwarz can be shown, using Proposition
$$\longrightarrow \times  \longrightarrow \longrightarrow$$
39.12. Given a bilinear map $f$ : $E E \to F$ , recall that $f$ is symmetric, if
$$f(u, v) = f(v, u),$$
$$\longrightarrow$$
for all $u, v \in E$ .

> **Proposition 39.20.** (Schwarz’s lemma) Given two normed affine spaces $E$ and $F$, given any open subset $A$ of $E$, given any $f$ : $A \to F$, for every $a \in A$, if $D^{2}f(a)$ exists, then
$$\longrightarrow  \longrightarrow  \longrightarrow$$
$D^{2}f(a) \in L_{2}(E , E$ ; $F$ ) is a continuous symmetric bilinear map. As a corollary, if $E$ is of finite dimension $n$, and $(a_{0}, (e_{1}, \dots  , e_{n}))$ is a frame for $E$, we have
$$\frac{\partial^{2} f}{\partial x_{i}\partial x_{j}} (a) = \frac{\partial^{2} f}{\partial x_{j}\partial x_{i}} (a).$$
Remark: There is a variation of the above result which does not assume the existence of $D^{2}f(a)$, but instead assumes that $D_{u}D_{v}f$ and $D_{v}D_{u}f$ exist on an open subset containing a and are continuous at a, and concludes that $D_{u}D_{v}f(a) = D_{v}D_{u}f(a)$. This is just a different result which does not imply Proposition 39.20, and is not a consequence of Proposition 39.20.
$$When E =\mathbb{R}^{2}, the only existence of \frac{\partial^{2} f}{\partial x\partial y} (a) and \frac{\partial^{2} f}{\partial y\partial x} (a) is not sufficient to insure the$$
existence of $D^{2}f(a)$. When $E$ if of finite dimension $n$ and $(a_{0}, (e_{1}, \dots  , e_{n}))$ is a frame for $E$, if $D^{2}f(a)$ exists,
$$\longrightarrow$$
for every $u = u_{1}e_{1} + \cdots  + u_{n}e_{n}$ and $v = v_{1}e_{1} + \cdots  + v_{n}e_{n}$ in $E$ , since $D^{2}f(a)$ is a symmetric bilinear form, we have
$$D^{2}f(a)(u, v) = \sum_{=1,j=1}^{n}  u_{i}v_{j} \frac{\partial^{2} f}{\partial x_{i}\partial x_{j}} (a),$$
$$i$$
which can be written in matrix form as:
$$D^{2}f(a)(u, v) = U^{\top} \begin{pmatrix} \partial^{2} f & \partial^{2} f & \partial^{2} f \\ (a) & (a) & \dots & (a) \\ \partial x_{1}^{2} & \partial x_{1}\partial x_{2} & \partial x_{1}\partial x_{n} \\ \partial^{2} f & \partial^{2} f & \partial^{2} f \\ (a) & (a) & \dots & (a) \\ \partial x_{1}\partial x_{2} & \partial x_{2}^{2} & \partial x_{2}\partial x_{n} \\ \vdots & \vdots & \ddots & \vdots \\ \partial^{2} f & \partial^{2} f & \partial^{2} f \\ (a) & (a) & \dots & (a) \\ \partial x_{1}\partial x_{n} & \partial x_{2}\partial x_{n} & \partial x_{n}^{2} \end{pmatrix} V$$
where $U$ is the column matrix representing $u$, and $V$ is the column matrix representing $v$, over the frame $(a_{0}, (e_{1}, \dots  , e_{n}))$.

<!-- PAGE 1477 -->

> **Definition 39.17.** The above symmetric matrix is called the Hessian of $f$ at a.

> **Example 39.14.** Consider the function $f$ defined on real invertible $2\times 2$ matrices such that ad - bc $> 0$ given by
$$f(a, b, c, d) = \log(ad -bc).$$
We immediately verify that the Jacobian matrix of $f$ is given by
$$df_{a,b,c,d} = \frac{1}{ad -bc} \begin{pmatrix} d & -c & -b & a \end{pmatrix} .$$
It is easily checked that if
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} ,X = \begin{pmatrix} x_{1} & x_{2} \\ x_{3} & x_{4} \end{pmatrix} ,$$
then
$$df_{A}(X) = \mathrm{tr}(A^{-1}X) = \frac{1}{ad -bc} \mathrm{tr} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} \begin{pmatrix} x_{1} & x_{2} \\ x_{3} & x_{4} \end{pmatrix} \begin{pmatrix}\end{pmatrix} .$$
Computing second-order derivatives, we find that the Hessian matrix of $f$ is given by
$$Hf(A) = \frac{1}{(ad -bc)^{2}} \begin{pmatrix} -d^{2} & cd & bd & -bc \\ cd & -c^{2} & -ad & ac \\ bd & -ad & -b^{2} & ab \\ bc & ac & ab & a^{2} \end{pmatrix} .$$
$$--$$
Using the formula for the derivative of the inversion map and the chain rule we can show that
$$D^{2}f(A)(X_{1}, X_{2}) = -\mathrm{tr}(A^{-1}X_{1}A^{-1}X_{2}),$$
and so
$$Hf(A)(X_{1}, X_{2}) = -\mathrm{tr}(A^{-1}X_{1}A^{-1}X_{2}),$$
a formula which is far from obvious. The function $f$ can be generalized to matrices $A \in GL^{+}(n,\mathbb{R})$, that is, $n\times n$ real invertible matrices of positive determinants, as
$$f(A) = \log \det(A).$$
It can be shown that the formulae
$$df_{A}(X) = \mathrm{tr}(A^{-1}X)$$
$$D^{2}f(A)(X_{1}, X_{2}) = -\mathrm{tr}(A^{-1}X_{1}A^{-1}X_{2})$$
also hold.

<!-- PAGE 1478 -->

> **Example 39.15.** If we restrict the function of Example 39.14 to symmetric positive definite matrices we obtain the function $g$ defined by
$$g(a, b, c) = \log(ac -b^{2}).$$
We immediately verify that the Jacobian matrix of $g$ is given by
$$dg_{a,b,c} = \frac{1}{ac -b^{2}} \begin{pmatrix} c & -2b & a \end{pmatrix} .$$
Computing second-order derivatives, we find that the Hessian matrix of $g$ is given by
$$Hg(a, b, c) = \frac{1}{(ac -b^{2})^{2}} \begin{pmatrix} -c^{2} & 2bc & -b^{2} \\ 2bc & -2(b^{2}+ ac) & 2ab \\ b^{2} & 2ab & a^{2} \end{pmatrix} .$$
$$--$$
Although this is not obvious, it can be shown that if ac - $b^{2} > 0$ and a, $c > 0$, then the matrix -Hg(a, $b, c)$ is symmetric positive definite. If $F$ itself is of finite dimension, and $(b_{0}, (v_{1}, \dots  , v_{m}))$ is a frame for $F$, then $f = (f_{1}, \dots  , f_{m})$, and each component $D^{2}f(a)_{i}(u, v)$ of $D^{2}f(a)(u, v) (1 \le i \le m)$, can be written as
$$D^{2}f(a)_{i}(u, v) = U^{\top} \begin{pmatrix} \partial^{2} f_{i} & \partial^{2} f_{i} & \partial^{2} f_{i} \\ (a) & (a) & \dots & (a) \\ \partial x_{1}^{2} & \partial x_{1}\partial x_{2} & \partial x_{1}\partial x_{n} \\ \partial^{2} f_{i} & \partial^{2} f_{i} & \partial^{2} f_{i} \\ (a) & (a) & \dots & (a) \\ \partial x_{1}\partial x_{2} & \partial x_{2}^{2} & \partial x_{2}\partial x_{n} \\ \vdots & \vdots & \ddots & \vdots \\ \partial^{2} f_{i} & \partial^{2} f_{i} & \partial^{2} f_{i} \\ (a) & (a) & \dots & (a) \\ \partial x_{1}\partial x_{n} & \partial x_{2}\partial x_{n} & \partial x_{n}^{2} \end{pmatrix} V$$
Thus, we could describe the vector $D^{2}f(a)(u, v)$ in terms of an $mn\times$ mn-matrix consisting of $m$ diagonal blocks, which are the above Hessians, and the row matrix $(U^{\top} , \dots  , U^{\top}$ ) $(m$ times) and the column matrix consisting of $m$ copies of $V$ . We now indicate briefly how higher-order derivatives are defined. Let $m \ge 2$. Given a function $f$ : $A \to F$ as before, for any $a \in A$, if the derivatives $D^{i}f$ exist on $A$ for all $i, 1 \le i \le m$ - $1$, by induction, $D^{m-1}f$ can be considered to be a continuous function
$$--\longrightarrow  \longrightarrow$$
$D^{m-1}f$ : $A \to L_{m-1}(E^{m-1}; F$ ).

> **Definition 39.18.** Define $D^{m}f(a)$, the $m$-th derivative of $f$ at a, as
$$D^{m}f(a) = D(D^{m-1}f)(a).$$
$$\longrightarrow  \longrightarrow$$
Then $D^{m}f(a)$ can be identified with a continuous m-multilinear map in $\mathcal{L}_{m}(E^{m}; F$ ). We can then show (as we did before), that if $D^{m}f(a)$ is defined, then
$$D^{m}f(a)(u_{1}, \dots  , u_{m}) = D_{u1} \dots  D_{um}f(a).$$

<!-- PAGE 1479 -->

> **Definition 39.19.** When $E$ if of finite dimension $n$ and $(a_{0}, (e_{1}, \dots  , e_{n}))$ is a frame for $E$, if $D^{m}f(a)$ exists, for every $j_{1}, \dots  , j_{m} \in {1, \dots  , n}$, we denote $D_{ejm} \dots  D_{ej1}f(a)$ by
$$\frac{\partial^{m} f}{\partial x_{j1} \dots  \partial x_{jm}} (a).$$

> **Example 39.16.** Going back to the function $f$ of Example 39.14 given by f(A) $=$ log det(A), using the formula for the derivative of the inversion map, the chain rule and the product rule, we can show that
$$D^{m}f(A)(X_{1}, \dots  , X_{m}) = (-1)^{m-1} \sum_{\in Sm-}  \mathrm{tr}(A^{-1}X_{1}A^{-1}X_{\sigma(1)+1}A^{-1}X_{\sigma(2)+1} \cdots  A^{-1}X_{\sigma(m-1)+1})$$
$$\sigma 1$$
for any $m \ge 1$, where $A \in GL^{+}(n,\mathbb{R})$ and $X_{1}, \dots  X_{m}$ are any $n \times  n$ real matrices.
$$\longrightarrow  \longrightarrow$$
Given a m-multilinear map $f \in L_{m}(E^{m}; F$ ), recall that $f$ is symmetric if
$$f(u_{\pi(1)}, \dots  , u_{\pi(m)}) = f(u_{1}, \dots  , u_{m}),$$
$$\longrightarrow$$
for all $u_{1}, \dots  , u_{m} \in E$ , and all permutations $\pi$  on ${1, \dots  , m}$. Then, the following generalization of Schwarz’s lemma holds.

> **Proposition 39.21.** Given two normed affine spaces $E$ and $F$, given any open subset $A$ of $E$, given any $f$ : $A \to F$, for every $a \in A$, for every $m \ge 1$, if $D^{m}f(a)$ exists, then
$$\longrightarrow  \longrightarrow$$
$D^{m}f(a) \in L_{m}(E^{m}; F$ ) is a continuous symmetric m-multilinear map. As a corollary, if $E$ is of finite dimension $n$, and $(a_{0}, (e_{1}, \dots  , e_{n}))$ is a frame for $E$, we have
$$\frac{\partial^{m} f}{\partial x_{j1} \dots  \partial x_{jm}} (a) = \frac{\partial^{m} f}{\partial x_{\pi(j1)} \dots  \partial x_{\pi(jm)}} (a),$$
for every $j_{1}, \dots  , j_{m} \in {1, \dots  , n}$, and for every permutation $\pi$  on ${1, \dots  , m}$. Because the trace function is invariant under permutation of its arguments (tr(XY ) $=$ tr(Y $X))$, we see that the $m$-th derivatives in Example 39.16 are indeed symmetric multilinear maps. If $E$ is of finite dimension $n$, and $(a_{0}, (e_{1}, \dots  , e_{n}))$ is a frame for $E, D^{m}f(a)$ is a symmetric m-multilinear map, and we have
$$D^{m}f(a)(u_{1}, \dots  , u_{m}) = \sum_{j}  u_{1,j1} \cdots  u_{m,jm} \frac{\partial^{m} f}{\partial x_{j1} \dots  \partial x_{jm}} (a),$$
where $j$ ranges over all functions $j$ : ${1, \dots  , m} \to {1, \dots  , n}$, for any $m$ vectors
$$u_{j} = u_{j,1}e_{1} + \cdots  + u_{j,n}e_{n}.$$
The concept of $C^{1}-function$ is generalized to the concept of $C^{m}-function$, and Theorem 39.13 can also be generalized.

<!-- PAGE 1480 -->

> **Definition 39.20.** Given two normed affine spaces $E$ and $F$, and an open subset $A$ of $E$, for any $m \ge 1$, we say that a function $f$ : $A \to F$ is of class $C^{m}$ on $A$ or a $C^{m}-function$ on $A$ if $D^{k}f$ exists and is continuous on $A$ for every $k, 1 \le k \le m$. We say that $f$ : $A \to F$ is of class $C^{\infty}$ on $A$ or a $C^{\infty}-function$ on $A$ if $D^{k}f$ exists and is continuous on $A$ for every $k \ge 1$. A $C^{\infty}-function$ (on $A)$ is also called a smooth function (on $A)$. A $C^{m}-diffeomorphism f$ : $A \to B$ between $A$ and $B$ (where $A$ is an open subset of $E$ and $B$ is an open subset of $B)$ is a bijection between $A$ and $B =$ f(A), such that both $f$ : $A \to B$ and its inverse $f^{-1}: B \to A$ are $C^{m}-functions$. Equivalently, $f$ is a $C^{m}-function$ on $A$ if $f$ is a $C^{1}-function$ on $A$ and Df is a $C^{m-1}-$ function on $A$. We have the following theorem giving a necessary and sufficient condition for $f$ to a $C^{m}-function$ on $A$. A generalization to the case where $E = (E_{1}, a_{1}) \oplus \cdots  \oplus (E_{n}, a_{n})$ also holds.

> **Theorem 39.22.** Given two normed affine spaces $E$ and $F$, where $E$ is of finite dimension $n$, and where $(a_{0}, (u_{1}, \dots  , u_{n}))$ is a frame of $E$, given any open subset $A$ of $E$, given any function $f$ : $A \to F$, for any $m \ge 1$, the derivative $D^{m}f$ is a $C^{m}-function$ on $A$ iff every
$$partial derivative D_{ujk} \dots  D_{uj1}f (or \frac{\partial^{k} f}{\partial x_{j1} \dots  \partial x_{jk}} (a)) is defined and continuous on A, for all$$
$k, 1 \le k \le m$, and all $j_{1}, \dots  , j_{k} \in {1, \dots  , n}$. As a corollary, if $F$ is of finite dimension $p$, and $(b_{0}, (v_{1}, \dots  , v_{p}))$ is a frame of $F$, the derivative $D^{m}f$ is defined and continuous on $A$ iff
$$every partial derivative D_{ujk} \dots  D_{uj1}f_{i} (or \frac{\partial^{k} f_{i}}{\partial x_{j1} \dots  \partial x_{jk}} (a)) is defined and continuous on A,$$
for all $k, 1 \le k \le m$, for all $i, 1 \le i \le p$, and all $j_{1}, \dots  , j_{k} \in {1, \dots  , n}$.

> **Definition 39.21.** When $E = \mathbb{R}$ (or $E = \mathbb{C})$, for any $a \in E, D^{m}f(a)(1, \dots  , 1)$ is a vector $\longrightarrow$ in $F$ , called the mth-order vector derivative. As in the case $m = 1$, we will usually identify the multilinear map $D^{m}f(a)$ with the vector $D^{m}f(a)(1, \dots  , 1)$. Some notational conventions can also be introduced to simplify the notation of higherorder derivatives, and we discuss such conventions very briefly. Recall that when $E$ is of finite dimension $n$, and $(a_{0}, (e_{1}, \dots  , e_{n}))$ is a frame for $E, D^{m}f(a)$ is a symmetric m-multilinear map, and we have
$$D^{m}f(a)(u_{1}, \dots  , u_{m}) = \sum_{j}  u_{1,j1} \cdots  u_{m,jm} \frac{\partial^{m} f}{\partial x_{j1} \dots  \partial x_{jm}} (a),$$
where $j$ ranges over all functions $j$ : ${1, \dots  , m} \to {1, \dots  , n}$, for any $m$ vectors
$$u_{j} = u_{j,1}e_{1} + \cdots  + u_{j,n}e_{n}.$$
We can then group the various occurrences of $\partial x_{jk}$ corresponding to the same variable $x_{jk}$, and this leads to the notation
$$\cdots$$
$$\alpha 1\alpha 2\alpha n$$
$$\begin{pmatrix} \partial \\ \partial x_{1} \end{pmatrix} \begin{pmatrix} \partial \\ \partial x_{2} \end{pmatrix} \begin{pmatrix} \partial \\ \partial x_{n} \end{pmatrix} f(a),$$
