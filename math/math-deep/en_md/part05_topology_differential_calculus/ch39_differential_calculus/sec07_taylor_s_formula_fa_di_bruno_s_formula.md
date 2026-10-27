# Taylor's formula, Faà di Bruno's formula


<!-- PAGE 1481 -->
where $\alpha_{1}  + \alpha_{2}  + \cdots  + \alpha_{n}  = m$. If we denote $(\alpha_{1} , \dots  , \alpha_{n}$ ) simply by $\alpha$ , then we denote
$$\cdots$$
$$\alpha 1\alpha 2\alpha n$$
$$\begin{pmatrix} \partial \\ \partial x_{1} \end{pmatrix} \begin{pmatrix} \partial \\ \partial x_{2} \end{pmatrix} \begin{pmatrix} \partial \\ \partial x_{n} \end{pmatrix} f$$
by
$$\alpha$$
$$\partial^{\alpha} f,or \begin{pmatrix} \partial \\ \partial x \end{pmatrix} f.$$
If $\alpha  = (\alpha_{1} , \dots  , \alpha_{n}$ ), we let $|\alpha$ | $= \alpha_{1}  + \alpha_{2}  + \cdots  + \alpha_{n} , \alpha$ ! $= \alpha_{1}$ ! $\cdots  \alpha_{n}$ !, and if $h = (h_{1}, \dots  , h_{n})$, we denote $h_{1}^{\alpha1} \cdots  h_{n}^{\alpha n}$ by $h^{\alpha}$. In the next section, we survey various versions of Taylor’s formula.

## 39.7 Taylor’s formula, Fa`a di Bruno’s formula

We discuss, without proofs, several versions of Taylor’s formula. The hypotheses required in each version become increasingly stronger. The first version can be viewed as a generalization
$$\longrightarrow \longrightarrow \longrightarrow$$
of the notion of derivative. Given an $m$-linear map $f$ : $E^{m} \to F$ , for any vector $h \in E$ , we abbreviate
$$f(h, \dots  , h)$$
$$| {z }$$
$$m$$
by $f(h^{m})$. The version of Taylor’s formula given next is sometimes referred to as the formula of Taylor–Young.

> **Theorem 39.23.** (Taylor–Young) Given two normed affine spaces $E$ and $F$, for any open subset $A \subseteq E$, for any function $f$ : $A \to F$, for any $a \in A$, if $D^{k}f$ exists in $A$ for all $k, 1 \le k \le m$ - $1$, and if $D^{m}f(a)$ exists, then we have:
$$f(a + h) = f(a) + \frac{1}{1!} D^{1}f(a)(h) + \cdots  + \frac{1}{m!} D^{m}f(a)(h^{m}) + \|h\|^{m}\epsilon (h),$$
for any $h$ such that $a + h \in A$, and where $lim_{h\to0, h\neq 0} \epsilon (h) = 0$. The above version of Taylor’s formula has applications to the study of relative maxima (or minima) of real-valued functions. It is also used to study the local properties of curves and surfaces. The next version of Taylor’s formula can be viewed as a generalization of Proposition 39.12. It is sometimes called the Taylor formula with Lagrange remainder or generalized mean value theorem.

<!-- PAGE 1482 -->

> **Theorem 39.24.** (Generalized mean value theorem) Let $E$ and $F$ be two normed affine spaces, let $A$ be an open subset of $E$, and let $f$ : $A \to F$ be a function on $A$. Given any
$$\longrightarrow$$
$a \in A$ and any $h \neq  0$ in $E$ , if the closed segment [a, $a + h]$ is contained in $A, D^{k}f$ exists in $A$ for all $k, 1 \le k \le m, D^{m+1}f(x)$ exists at every point $x$ of the open segment ]a, $a + h[$, and
$$\max

$D^{m+1}f(x)$

$\le$ M,$$
$$x\in (a,a+h)$$
for some $M \ge 0$, then
$$\|\|^{m+1}$$
$$f(a + h) -f(a) - \begin{pmatrix} 1 & 1 \\ D^{1}f(a)(h) + \cdots  + & D^{m}f(a)(h^{m}) \\ 1! & m! \end{pmatrix} \le M \frac{h}{(m + 1)!} .$$
$$--\longrightarrow \longrightarrow$$
As a corollary, if $L: E^{m+1} \to F$ is a continuous $(m +$ 1)-linear map, then $\| \|^{m+1}$
$$f(a + h) -f(a) - \begin{pmatrix} 1 & 1 & L(h^{m+1}) \\ D^{1}f(a)(h) + \cdots  + & D^{m}f(a)(h^{m}) + \\ 1! & m! & (m + 1)! \end{pmatrix} \le M \frac{h}{(m + 1)!} ,$$
where $M = max_{x\in(a,a+h)} \|D^{m+1}f(x)$ - $L\|$. The above theorem is sometimes stated under the slightly stronger assumption that $f$ is a $C^{m}-function$ on $A$. If $f$ : $A \to \mathbb{R}$ is a real-valued function, Theorem 39.24 can be refined a little bit. This version is often called the formula of Taylor–MacLaurin.

> **Theorem 39.25.** (Taylor–MacLaurin) Let $E$ be a normed affine space, let $A$ be an open subset of $E$, and let $f$ : $A \to \mathbb{R}$ be a real-valued function on $A$. Given any $a \in A$ and any
$$\longrightarrow$$
$h \neq  0$ in $E$ , if the closed segment [a, $a + h]$ is contained in $A$, if $D^{k}f$ exists in $A$ for all $k, 1 \le k \le m$, and $D^{m+1}f(x)$ exists at every point $x$ of the open segment ]a, $a + h[$, then there is some $\theta  \in \mathbb{R}$, with $0 < \theta  < 1$, such that
$$f(a + h) = f(a) + \frac{1}{1!} D^{1}f(a)(h) + \cdots  + \frac{1}{m!} D^{m}f(a)(h^{m}) + \frac{1}{(m + 1)!} D^{m+1}f(a + \theta h)(h^{m+1}).$$

> **Example 39.17.** Going back to the function $f$ of Example 39.14 given by f(A) $=$ log det(A), we know from Example 39.16 that
$$D^{m}f(A)(X_{1}, \dots  , X_{m}) = (-1)^{m-1} \sum_{\in Sm-}  \mathrm{tr}(A^{-1}X_{1}A^{-1}X_{\sigma(1)+1} \cdots  A^{-1}X_{\sigma(m-1)+1})(*)$$
$$\sigma 1$$
for all $m \ge 1$, with $A \in GL^{+}(n,\mathbb{R})$. If we make the stronger assumption that $A$ is symmetric positive definite, then for any other symmetric positive definite matrix $B$, since the symmetric positive definite matrices form a convex set, the matrices $A + \theta (B -A) = (1 -\theta )A + \theta B$ are also symmetric positive definite for $\theta  \in [0, 1]$. Theorem 39.25 applies with $H = B$ - $A$ (a symmetric matrix), and using (*), we obtain
$$ -$$
$$+$$
$$\log \det(A + H) = \log \det(A) + trA^{-1}H - \frac{1}{2} (A^{-1}H)^{2} \cdots  + \frac{(1)^{m-1}}{m} (A^{-1}H)^{m}$$
$$-$$
$$+ \frac{(1)^{m}}{m} + 1 ((A + \theta H)^{-1}H)^{m+1},$$

<!-- PAGE 1483 -->
for some $\theta$  such that $0 < \theta  < 1$. In particular, if $A =$ I, for any symmetric matrix $H$ such that I $+ H$ is symmetric positive definite, we obtain
$$ -$$
$$+$$
$$\log \det(I + H) = trH - \frac{1}{2} H^{2} \cdots  + \frac{(1)^{m-1}}{m} H^{m}$$
$$+ \frac{(1)^{m}}{m} - + 1 ((I + \theta H)^{-1}H)^{m+1},$$
for some $\theta$  such that $0 < \theta  < 1$. In the special case when $n = 1$, we have $I = 1, H$ is a real such that $1 + H > 0$ and the trace function is the identity, so we recognize the partial sum of the series for $x \mapsto$ log(1 $+ x)$,
$$+ -$$
$$\log(1 + H) = H - \frac{1}{2} H^{2} \cdots  + \frac{(1)^{m-1}}{m} H^{m}$$
$$-$$
$$+ \frac{(1)^{m}}{m} + 1 (1 + \theta H)^{-(m+1)}H^{m+1}.$$
We also mention for “mathematical culture,” a version with integral remainder, in the case of a real-valued function. This is usually called Taylor’s formula with integral remainder.

> **Theorem 39.26.** (Taylor’s formula with integral remainder) Let $E$ be a normed affine space, let $A$ be an open subset of $E$, and let $f$ : $A \to \mathbb{R}$ be a real-valued function on $A$. Given any
$$\longrightarrow$$
$a \in A$ and any $h \neq  0$ in $E$ , if the closed segment [a, $a + h]$ is contained in $A$, and if $f$ is a $C^{m+1}-function$ on $A$, then we have
$$f(a + h) = f(a) + \frac{1}{1!} D^{1}f(a)(h) + \cdots  + \frac{1}{m!} D^{m}f(a)(h^{m})$$
$$+ \int_{0}^{}  1 \frac{(1t)^{m}}{m!} -hD^{m+1}f(a + th)(h^{m+1})idt.$$
The advantage of the above formula is that it gives an explicit remainder. We now examine briefly the situation where $E$ is of finite dimension $n$, and $(a_{0}, (e_{1}, \dots  , e_{n}))$ is a frame for $E$. In this case, we get a more explicit expression for the expression
$$\sum_{i=0}^{k=m}  \frac{1}{k!} D^{k}f(a)(h^{k})$$
involved in all versions of Taylor’s formula, where by convention, $D^{0}f(a)(h^{0}) =$ f(a). If $h = h_{1}e_{1} + \cdots  + h_{n}e_{n}$, then we have
$$\cdots$$
$$\sum_{k=0}^{k=m}  \frac{1}{k!} D^{k}f(a)(h^{k}) = \sum_{\cdot \cdot \cdot+kn}  \frac{h_{1}^{k1} h_{n}^{kn}}{k_{1}! \cdots  k_{n}!} \cdots k1knf(a),$$
$$k+\le m \begin{pmatrix} \partial \\ \partial x_{1} \end{pmatrix} \begin{pmatrix} \partial \\ \partial x_{n} \end{pmatrix}$$
$$1$$

<!-- PAGE 1484 -->
which, using the abbreviated notation introduced at the end of Section 39.6, can also be written as
$$\sum_{k=0}^{k=m}  \frac{1}{k!} D^{k}f(a)(h^{k}) = \sum_{|\alpha|\le m}  \frac{h^{\alpha}}{\alpha !} \partial^{\alpha} f(a).$$
The advantange of the above notation is that it is the same as the notation used when $n = 1$, i.e., when $E = \mathbb{R}$ (or $E = \mathbb{C})$. Indeed, in this case, the Taylor–MacLaurin formula reads as:
$$f(a + h) = f(a) + \frac{h}{1!} D^{1}f(a) + \cdots  + \frac{h^{m}}{m} ! D^{m}f(a) + \frac{h^{m+1}}{(m + 1)!} D^{m+1}f(a + \theta h),$$
for some $\theta  \in \mathbb{R}$, with $0 < \theta  < 1$, where $D^{k}f(a)$ is the value of the $k$-th derivative of $f$ at a (and thus, as we have already said several times, this is the kth-order vector derivative, which is just a scalar, since $F =\mathbb{R})$. In the above formula, the assumptions are that $f$ : [a, $a + h] \to \mathbb{R}$ is a $C^{m}-function$ on [a, $a + h]$, and that $D^{m+1}f(x)$ exists for every $x \in$ (a, $a + h)$. Taylor’s formula is useful to study the local properties of curves and surfaces. In the case of a curve, we consider a function $f$ : $[r, s] \to F$ from a closed interval $[r, s]$ of $\mathbb{R}$ to some affine space $F$, the derivatives $D^{k}f(a)(h^{k})$ correspond to vectors $h^{k}D^{k}f(a)$, where $D^{k}f(a)$ is the kth vector derivative of $f$ at a (which is really $D^{k}f(a)(1, \dots  , 1))$, and for any $a \in (r, s)$, Theorem 39.23 yields the following formula:
$$f(a + h) = f(a) + \frac{h}{1!} D^{1}f(a) + \cdots  + \frac{h^{m}}{m} ! D^{m}f(a) + h^{m}\epsilon (h),$$
for any $h$ such that $a + h \in (r, s)$, and where $lim_{h\to0, h\neq 0} \epsilon (h) = 0$.
$$\mathbb{R}^{n} \mathbb{R}$$
In the case of functions $f$ : $\to$ , it is convenient to have formulae for the Taylor– Young formula and the Taylor–MacLaurin formula in terms of the gradient and the Hessian.
$$\mathbb{R}^{n}$$
Recall that the gradient $\nabla$ f(a) of $f$ at $a \in$ is the column vector
$$\nabla f(a) = \begin{pmatrix} \partial f \\ (a) \\ \partial x_{1} \\ \partial f \\ (a) \\ \partial x_{2} \\ \vdots \\ \partial f \\ (a) \\ \partial x_{n} \end{pmatrix} ,$$
and that
$$f' (a)(u) = Df(a)(u) = \nabla f(a) \cdot  u,$$
$$\mathbb{R}^{n}$$
for any $u \in$ (where $\cdot$  means inner product). The above equation shows that the direction of the gradient $\nabla$ f(a) is the direction of maximal increase of the function $f$ at a and that

<!-- PAGE 1485 -->
$\|\nabla f(a)\|$ is the rate of change of $f$ in its direction of maximal increase. This is the reason why methods of “gradient descent” pick the direction opposite to the gradient (we are trying to minimize $f)$.
$$\mathbb{R}^{n}$$
The Hessian matrix $\nabla^{2}$ f(a) of $f$ at $a \in$ is the $n \times  n$ symmetric matrix
$$\nabla^{2} f(a) = \begin{pmatrix} \partial^{2} f & \partial^{2} f & \partial^{2} f \\ (a) & (a) & \dots & (a) \\ \partial x_{1}^{2} & \partial x_{1}\partial x_{2} & \partial x_{1}\partial x_{n} \\ \partial^{2} f & \partial^{2} f & \partial^{2} f \\ (a) & (a) & \dots & (a) \\ \partial x_{1}\partial x_{2} & \partial x_{2}^{2} & \partial x_{2}\partial x_{n} \\ \vdots & \vdots & \ddots & \vdots \\ \partial^{2} f & \partial^{2} f & \partial^{2} f \\ (a) & (a) & \dots & (a) \\ \partial x_{1}\partial x_{n} & \partial x_{2}\partial x_{n} & \partial x_{n}^{2} \end{pmatrix} ,$$
and we have
$$D^{2}f(a)(u, v) = u^{\top}\nabla^{2} f(a) v = u \cdot  \nabla^{2} f(a)v = \nabla^{2} f(a)u \cdot  v,$$
for all $u, v \in \mathbb{R}^{n}$. Then, we have the following three formulations of the formula of Taylor– Young of order $2$:
$$\epsilon$$
$$f(a + h) = f(a) + Df(a)(h) + \frac{1}{2} D^{2}f(a)(h, h) + \|h\|^{2}(h)$$
$$f(a + h) = f(a) + \nabla f(a) \cdot  h + \frac{1}{2} (h \cdot  \nabla^{2} f(a)h) + (h \cdot  h)\epsilon (h)$$
$$f(a + h) = f(a) + (\nabla f(a))^{\top}h + \frac{1}{2} (h^{\top}\nabla^{2} f(a) h) + (h^{\top}h)\epsilon (h).$$
with $lim_{h\mapsto0} \epsilon (h) = 0$. One should keep in mind that only the first formula is intrinsic (i.e., does not depend on the choice of a basis), whereas the other two depend on the basis and the inner product chosen on $\mathbb{R}^{n}$. As an exercise, the reader should write similar formulae for the Taylor–MacLaurin formula of order $2$. Another application of Taylor’s formula is the derivation of a formula which gives the m- th derivative of the composition of two functions, usually known as “Fa`a di Bruno’s formula.” This formula is useful when dealing with geometric continuity of splines curves and surfaces.

> **Proposition 39.27.** Given any normed affine space $E$, for any function $f$ : $\mathbb{R} \to \mathbb{R}$ and any function $g: \mathbb{R} \to E$, for any $a \in \mathbb{R}$, letting $b =$ f(a), $f^{(i)} (a) = D^{i}f(a)$, and $g^{(i)}(b) = D^{i}g(b)$, for any $m \ge 1$, if $f^{(i)}$ (a) and $g^{(i)}(b)$ exist for all $i, 1 \le i \le m$, then $(g\circ f)^{(m)}(a) = D^{m}(g\circ$ f)(a) exists and is given by the following formula:
$$)^{i1})^{im}$$
$$(g \circ f)^{(m)}(a) = \sum_{0\le j\le m}  \sum_{2+\cdot \cdot \cdot+i}  \frac{m!}{i_{1}! \cdots  i_{m}!} g^{(j)}(b) \begin{pmatrix} f^{(1)}(a \\ 1! \end{pmatrix} \cdots \begin{pmatrix} f^{(m)}(a \\ m! \end{pmatrix} .$$
$$i1+im=j$$
$$i1+2i2+\cdot \cdot \cdot +mim=m$$
$$i1,i2,\cdot \cdot \cdot  ,im\ge 0$$
