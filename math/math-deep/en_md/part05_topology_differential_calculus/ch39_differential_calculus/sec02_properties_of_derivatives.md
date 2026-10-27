# Properties of Derivatives


<!-- PAGE 1450 -->
We have f(A $+ H)$ - f(A) - $(A^{\top}H + H^{\top}A) = (A + H)^{\top}(A + H)$ - I - $(A^{\top}A$ - I) - $A^{\top}H$ - $H^{\top}A$
$$= A^{\top}A + A^{\top}H + H^{\top}A + H^{\top}H -A^{\top}A -A^{\top}H -H^{\top}A$$
$$= H^{\top}H.$$
It follows that
$$- -$$
$$\epsilon (H) = \frac{f(A + H)f(A)(A^{\top}H + H^{\top}A)}{\|H\|} = \frac{H^{\top}H}{\|H\|} ,$$
and since our norm is the Frobenius norm,
$$\|\|$$
$$\|\epsilon (H)\|= \frac{H^{\top}H}{\|H\|} \le \frac{H^{\top}H}{\|H\|} =

$H^{\top}$

$= \|H\|,$$$ so
$$lim \epsilon (H) = 0,$$
$$H\mapsto 0$$
and we conclude that
$$Df(A)(H) = A^{\top}H + H^{\top}A.$$

> **Definition 39.4.** If the derivative $Df_{a}$ of a function $f$ : $A \to F$ exists for every $a \in A$, we
$$\longrightarrow  \longrightarrow$$
get a map Df : $A \to$ L(E ; $F$ ), called the derivative of $f$ on $A$, also denoted by df. Here $\longrightarrow  \longrightarrow  \longrightarrow  \longrightarrow \mathcal{L}(E$ ; $F$ ) denotes the vector space of all continuous maps from $E$ to $F$ . Note that according to the old notion of the derivative of a function $f$ : $A \to \mathbb{R}$, the
$$\mathbb{R}$$
derivative f' of $f$ is the map f': $A \to$  given by $a \mapsto$ f'(a). But the “right” notion is that
$$\longrightarrow  \longrightarrow  \longrightarrow$$
the derivative Df of $f$ is a map from $A$ to the space $\mathcal{L}(E$ ; $F$ ) of continuous maps from $E \longrightarrow$ to $F$ . When $E = F =\mathbb{R}$, there is an accidental isomorphism between $\mathcal{L}(\mathbb{R};\mathbb{R})$ and $\mathbb{R}$. We now consider a number of standard results about derivatives.

## 39.2 Properties of Derivatives


> **Proposition 39.3.** Given two normed affine spaces $E$ and $F$, if $f$ : $E \to F$ is a constant
$$\longrightarrow$$
function, then Df(a) $= 0$, for every $a \in E$. (here, $0$ denotes the linear map from $E$ to $\longrightarrow \longrightarrow \longrightarrow F$ whose value is $0 \in F$ for all $u \in E$ ). If $f$ : $E \to F$ is a continuous affine map, then
$$\longrightarrow  \longrightarrow$$
Df(a) $= f$ , for every $a \in E$, where $f$ denotes the linear map associated with $f$. In particular, if $E$ and $F$ are normed vector spaces and $f$ : $E \to F$ is a continuous linear map, then Df(a) $= f$ for all $a \in E$.

*Proof.* If $f$ : $E \to F$ is the constant function such that f(u) $= c$ for all $u \in E$ for some fixed $c \in F$, then
$$f(a + h) -f(a) = c -c = 0 = 0 \|h\|,$$

<!-- PAGE 1451 -->
$$\longrightarrow \longrightarrow$$
so $\epsilon (h) = 0$ for all $h \in E$ , and by definition, Df(a)(h) $= 0$ for all $a \in E$ and $h \in E$ .
$$\longrightarrow$$
If $f$ : $E \to F$ is a continuous affine map, since $f$ is linear, we have
$$\longrightarrow \longrightarrow  \longrightarrow  \longrightarrow \longrightarrow$$
f(a $+ h)$ - f(a) $= f (a + h) + c$ - ( $f (a) + c) = f (a) + f (h) + c$ - ( $f (a) + c)$
$$\longrightarrow  \longrightarrow$$
$$=f (h) =f (h) + 0 \|h\|,$$
$$\longrightarrow  \longrightarrow$$
so $\epsilon (h) = 0$ for all $h \in E$ , and by definition, Df(a) $= f$ for all $a \in E$.
$$\mathbb{R}^{n} \mathbb{R}$$

> **Example 39.3.** Consider the function $f$ : $\to M_{1,m}($ ) given by
$$\phi (v) = (Cv -d)^{\top},v \in \mathbb{R}^{n},$$
where $C$ is an $m \times  n$ matrix and $d \in \mathbb{R}^{m}$. Since transposition is linear,
$$\phi (v) = (Cv)^{\top}-d^{\top}$$
is an affine map with linear part given by $v \mapsto (Cv)^{\top}$, so by Proposition 39.3,
$$D\phi_{v} (w) = (Cw)^{\top},v, w \in \mathbb{R}^{n}.$$

> **Proposition 39.4.** Given a normed affine space $E$ and a normed vector space $F$, for any two functions $f, g: E \to F$, for every $a \in E$, if Df(a) and Dg(a) exist, then D(f $+g)(a)$ and $D(\lambda$ f)(a) exist, and
$$D(f + g)(a) = Df(a) + Dg(a),$$
$$D(\lambda f)(a) = \lambda Df(a).$$

*Proof.* Straightforward. Given two normed vector spaces $(E_{1}, \|\|_{1})$ and $(E_{2}, \|\|_{2})$, there are three natural and equivalent norms that can be used to make $E_{1} \times  E_{2}$ into a normed vector space: $1. \|(u_{1}, u_{2})\|_{1} = \|u_{1}\|_{1} + \|u_{2}\|_{2}. 2. \|(u_{1}, u_{2})\|_{2} = (\|u_{1}\|_{1}^{2} + \|u_{2}\|_{2}^{2})^{1/2}. 3. \|(u_{1}, u_{2})\|_{\infty} = max(\|u_{1}\|_{1} , \|u_{2}\|_{2})$. We usually pick the first norm. If $E_{1}, E_{2}$, and $F$ are three normed vector spaces, recall that a bilinear map $f$ : $E_{1} \times  E_{2} \to F$ is continuous iff there is some constant $C \ge 0$ such that
$$\|f(u_{1}, u_{2})\|\le C \|u_{1}\|_{1} \|u_{2}\|_{2}for all u_{1} \in E_{1} and all u_{2} \in E_{2}.$$

> **Proposition 39.5.** Given three normed vector spaces $E_{1}, E_{2}$, and $F$, for any continuous bilinear map $f$ : $E_{1} \times  E_{2} \to F$, for every (a, $b) \in E_{1} \times  E_{2}$, Df(a, $b)$ exists, and for every $u \in E_{1}$ and $v \in E_{2}$,
$$Df(a, b)(u, v) = f(u, b) + f(a, v).$$

<!-- PAGE 1452 -->

*Proof.* Since $f$ is bilinear, a simple computation implies that f((a, $b) + (u, v))$ - f(a, $b)$ - (f(u, $b) +$ f(a, $v)) =$ f(a $+ u, b + v)$ - f(a, $b)$ - f(u, $b)$ - f(a, $v)$
$$= f(a + u, b) + f(a + u, v) -f(a, b) -f(u, b) -f(a, v)$$
$$= f(a, b) + f(u, b) + f(a, v) + f(u, v) -f(a, b) -f(u, b) -f(a, v)$$
$$= f(u, v).$$
We define
$$f((a, b) + (u, v)) -f(a, b) -(f(u, b) + f(a, v))$$
$$\epsilon (u, v) =,$$
$$\|(u, v)\|_{1}$$
and observe that the continuity of $f$ implies $\|f((a, b) + (u, v))$ - f(a, $b)$ - (f(u, $b) +$ f(a, $v))\| = \|f(u, v)\|$
$$\le C \|u\|_{1} \|v\|_{2} \le C (\|u\|_{1} + \|v\|_{2})^{2}.$$
Hence
$$\|\|\|\|_{1} \|\|_{2}$$
$$\|\epsilon (u, v)\|= \frac{f(u, v)}{\|(u, v)\|_{1}} = \frac{f(u, v)}{\|(u, v)\|_{1}} \le \frac{C (u +v)^{2}}{\|u\|_{1} + \|v\|_{2}} = C (\|u\|_{1} + \|v\|_{2}) = C \|(u, v)\|_{1} ,$$
which in turn implies
$$lim \epsilon (u, v) = 0.$$
$$(u,v)\mapsto (0,0)$$
$$\mathbb{R}^{n} \mathbb{R}^{m} \mathbb{R}$$

> **Example 39.4.** Consider the function $f$ : $\times \to$  given by
$$f(v, \lambda ) = \lambda^{\top} Cv = v^{\top}C^{\top}\lambda ,v \in \mathbb{R}^{n}, \lambda  \in \mathbb{R}^{m},$$
where $C$ is an $m \times  n$ matrix. Since the function $f$ is bilinear, by Proposition 39.5, its derivative is given by
$$df_{(v,\lambda)}(w, \mu ) = f(w, \lambda ) + f(v, \mu ) = \lambda^{\top} Cw + \mu^{\top} Cv = (C^{\top}\lambda )^{\top}w + (Cv)^{\top}\mu ,$$
with $w \in \mathbb{R}^{n}, \mu  \in \mathbb{R}^{m}$. We now state the very useful chain rule.

> **Theorem 39.6.** Given three normed affine spaces $E, F$, and $G$, let $A$ be an open set in $E$, and let $B$ an open set in $F$. For any functions $f$ : $A \to F$ and $g: B \to G$, such that f(A) $\subseteq B$, for any $a \in A$, if Df(a) exists and Dg(f(a)) exists, then D(g $\circ$ f)(a) exists, and
$$D(g \circ f)(a) = Dg(f(a)) \circ Df(a).$$

<!-- PAGE 1453 -->

*Proof.* Since $f$ is differentiable at a and $g$ is differentiable at $b =$ f(a) for every $\eta$  such that $0 < \eta  < 1$ there is some $\rho  > 0$ such that for all $s, t$, if $\|s\|\le \rho$  and $\|t\|\le \rho$  then
$$f(a + s) = f(a) + Df_{a}(s) + \epsilon_{1} (s)$$
$$g(b + t) = g(b) + Dg_{b}(t) + \epsilon_{2} (t),$$
with $\|\epsilon_{1} (s)\|\le \eta  \|s\|$ and $\|\epsilon_{2} (t)\|\le \eta  \|t\|$. Since $Df_{a}$ and $Dg_{b}$ are continuous, we have
$$\|Df_{a}(s)\|\le \|Df_{a}\|\|s\|and\|Dg_{b}(t)\|\le \|Dg_{b}\|\|t\|,$$
which, since $\|\epsilon_{1} (s)\|\le \eta  \|s\|$ and $\eta  < 1$, implies that $\|Df_{a}(s) + \epsilon_{1} (s)\|\le \|Df_{a}\|\|s\| + \|\epsilon_{1} (s)\|\le \|Df_{a}\|\|s\| + \eta  \|s\|\le (\|Df_{a}\| + 1) \|s\|$. Consequently, if $\|s\| < \rho /(\|Df_{a}\| + 1)$, we have
$$\|\epsilon_{2} (Df_{a}(s) + \epsilon_{1} (s))\|\le \eta (\|Df_{a}\|+ 1) \|s\|(*_{1})$$
and
$$\|Dg_{b}(\epsilon_{1} (s))\|\le \|Dg_{b}\|\|\epsilon_{1} (s)\|\le \eta  \|Dg_{b}\|\|s\|.(*_{2})$$
Then since $b =$ f(a), using the above we have
$$(g \circ f)(a + s) = g(f(a + s)) = g(b + Df_{a}(s) + \epsilon_{1} (s))$$
$$= g(b) + Dg_{b}(Df_{a}(s) + \epsilon_{1} (s)) + \epsilon_{2} (Df_{a}(s) + \epsilon_{1} (s))$$
$$= g(b) + (Dg_{b} \circ Df_{a})(s) + Dg_{b}(\epsilon_{1} (s)) + \epsilon_{2} (Df_{a}(s) + \epsilon_{1} (s)).$$
Now by $(*_{1})$ and $(*_{2})$ we have
$$\|Dg_{b}(\epsilon_{1} (s)) + \epsilon_{2} (Df_{a}(s) + \epsilon_{1} (s))\|\le \|Dg_{b}(\epsilon_{1} (s))\|+ \|\epsilon_{2} (Df_{a}(s) + \epsilon_{1} (s))\|$$
$$\le \eta  \|Dg_{b}\|\|s\|+ \eta (\|Df_{a}\|+ 1) \|s\|$$
$$= \eta (\|Df_{a}\|+ \|Dg_{b}\|+ 1) \|s\|,$$
so if we write $\epsilon_{3} (s) = Dg_{b}(\epsilon_{1} (s)) + \epsilon_{2} (Df_{a}(s) + \epsilon_{1} (s))$ we proved that
$$(g \circ f)(a + s) = g(b) + (Dg_{b} \circ Df_{a})(s) + \epsilon_{3} (s)$$
with $\epsilon_{3} (s) \le \eta (\|Df_{a}\|+ \|Dg_{b}\|+ 1) \|s\|$, which proves that $Dg_{b} \circ Df_{a}$ is the derivative of $g \circ f$ at a. Since $Df_{a}$ and $Dg_{b}$ are continuous, so is $Dg_{b} \circ Df_{a}$, which proves our proposition. In the special case where $E = F = G =\mathbb{R}$ and $A$ and $B$ are open subsets of $\mathbb{R}$ such that f(A) $\subseteq B$, the chain rule gives us back the standard version of the chain rule for functions $f$ : $A \to \mathbb{R}$ and $g: B \to \mathbb{R}$, namely for any $a \in A$,
$$(g \circ f)'(a) = g'(f(a)) \cdot  f' (a),$$

<!-- PAGE 1454 -->
the product of the real numbers g'(f(a)) and f' (a). This is because for any $a \in A$ and $b \in B, Df_{a}$ is the linear map given by $Df_{a}(u) =$ f' (a)u and $Dg_{b}$ is the linear map given by $Dg_{b}(v) =$ g'(b)v, with $u, v \in \mathbb{R}$, so the chain rule with $b =$ f(a) and $v =$ f' (a)u says that
$$D(g \circ f)_{a}(u) = Dg_{f(a)}(Df_{a}(u)) = g'(f(a))(f' (a)u) = (g'(f(a))f' (a))u,$$
so indeed
$$(g \circ f)'(a) = g'(f(a))f' (a).$$
Theorem 39.6 has many interesting consequences. We mention two corollaries.

> **Proposition 39.7.** Given three normed affine spaces $E, F$, and $G$, for any open subset $A$ in $E$, for any $a \in A$, let $f$ : $A \to F$ such that Df(a) exists, and let $g: F \to G$ be a continuous affine map. Then, D(g $\circ$ f)(a) exists, and
$$\longrightarrow$$
$$D(g \circ f)(a) =g \circ Df(a),$$
$\longrightarrow$ where $g$ is the linear map associated with the affine map $g$.

> **Proposition 39.8.** Given two normed affine spaces $E$ and $F$, let $A$ be some open subset in $E$, let $B$ be some open subset in $F$, let $f$ : $A \to B$ be a bijection from $A$ to $B$, and assume that Df exists on $A$ and that $Df^{-1}$ exists on $B$. Then, for every $a \in A$,
$$Df^{-1} (f(a)) = (Df(a))^{-1}.$$
$$\longrightarrow  \longrightarrow$$
Proposition 39.8 has the remarkable consequence that the two vector spaces $E$ and $F$ have the same dimension. In other words, a local property, the existence of a bijection $f$ between an open set $A$ of $E$ and an open set $B$ of $F$, such that $f$ is differentiable on $A$ and
$$\longrightarrow  \longrightarrow$$
$f^{-1}$ is differentiable on $B$, implies a global property, that the two vector spaces $E$ and $F$ have the same dimension. Let us mention two more rules about derivatives that are used all the time. Let $\iota$ : $GL(n,\mathbb{C}) \to M_{n}(\mathbb{C})$ be the function (inversion) defined on invertible $n\times n$ matrices by
$$\iota (A) = A^{-1}.$$
Observe that $GL(n,\mathbb{C})$ is indeed an open subset of the normed vector space $M_{n}(\mathbb{C})$ of complex $n \times  n$ matrices, since its complement is the closed set of matrices $A \in M_{n}(\mathbb{C})$ satisfying det(A) $= 0$. Then we have
$$d\iota_{A} (H) = -A^{-1}HA^{-1},$$
for all $A \in GL(n,\mathbb{C})$ and for all $H \in M_{n}(\mathbb{C})$.

<!-- PAGE 1455 -->
To prove the preceding line observe that for $H$ with sufficiently small norm, we have $\iota (A + H)$ - $\iota (A) + A^{-1}HA^{-1} = (A + H)^{-1}$ - $A^{-1} + A^{-1}HA^{-1}$
$$= (A + H)^{-1}[I -(A + H)A^{-1}+ (A + H)A^{-1}HA^{-1}]$$
$$= (A + H)^{-1}[I -I -HA^{-1}+ HA^{-1}+ HA^{-1}HA^{-1}]$$
$$= (A + H)^{-1}HA^{-1}HA^{-1}.$$
Consequently, we get
$$-$$
$$\epsilon (H) = \frac{\iota (A + H)\iota (A) + A^{-1}HA^{-1}}{\|H\|} = \frac{(A + H)^{-1}HA^{-1}HA^{-1}}{\|H\|} ,$$
and since
$$(A + H)^{-1}HA^{-1}HA^{-1}

$\le \|H\|^{2}$

$A^{-12}$



$(A + H)^{-1}$

,$$ it is clear that $lim_{H\mapsto0} \epsilon (H) = 0$, which proves that
$$d\iota_{A} (H) = -A^{-1}HA^{-1}.$$
In particular, if $A =$ I, then $d\iota_{I} (H) = -H$. Next, if $f$ : $M_{n}(\mathbb{C}) \to M_{n}(\mathbb{C})$ and $g: M_{n}(\mathbb{C}) \to M_{n}(\mathbb{C})$ are differentiable matrix functions, then
$$d(fg)_{A}(B) = df_{A}(B)g(A) + f(A)dg_{A}(B),$$
for all $A, B \in M_{n}(\mathbb{C})$. This is known as the product rule. When $E$ is of finite dimension $n$, for any frame $(a_{0}, (u_{1}, \dots  , u_{n}))$ of $E$, where $(u_{1}, \dots  , u_{n})$
$$\longrightarrow$$
is a basis of $E$ , we can define the directional derivatives with respect to the vectors in the basis $(u_{1}, \dots  , u_{n})$ (actually, we can also do it for an infinite frame). This way, we obtain the definition of partial derivatives, as follows.

> **Definition 39.5.** For any two normed affine spaces $E$ and $F$, if $E$ is of finite dimension $n$, for every frame $(a_{0}, (u_{1}, \dots  , u_{n}))$ for $E$, for every $a \in E$, for every function $f$ : $E \to F$, the directional derivatives $D_{uj}f(a)$ (if they exist) are called the partial derivatives of $f$ with respect to the frame $(a_{0}, (u_{1}, \dots  , u_{n}))$. The partial derivative $D_{uj}f(a)$ is also denoted by
$$\partial_{j} f(a), or \frac{\partial f}{\partial x_{j}} (a).$$
$$The notation \frac{\partial f}{\partial x_{j}} (a) for a partial derivative, although customary and going back to$$
Leibniz, is a “logical obscenity.” Indeed, the variable $x_{j}$ really has nothing to do with the formal definition. This is just another of these situations where tradition is just too hard to overthrow! We now consider the situation where the normed affine space $F$ is a finite direct sum $F = (F_{1}, b_{1}) \oplus \cdots  \oplus (F_{m}, b_{m})$.

<!-- PAGE 1456 -->

> **Proposition 39.9.** Given normed affine spaces $E$ and $F = (F_{1}, b_{1}) \oplus \cdots  \oplus (F_{m}, b_{m})$, given any open subset $A$ of $E$, for any $a \in A$, for any function $f$ : $A \to F$, letting $f = (f_{1}, \dots  , f_{m})$, Df(a) exists iff every $Df_{i}(a)$ exists, and
$$Df(a) = in_{1} \circ Df_{1}(a) + \cdots  + in_{m} \circ Df_{m}(a).$$

*Proof.* Observe that f(a $+ h)$ - f(a) $=$ (f(a $+ h)$ - $b)$ - (f(a) - $b)$, where $b = (b_{1}, \dots  , b_{m})$,
$$\longrightarrow$$
and thus, as far as dealing with derivatives, Df(a) is equal to $Df_{b}(a)$, where $f_{b}$ : $E \to F$ is defined such that $f_{b}(x) =$ f(x)-b, for every $x \in E$. Thus, we can work with the vector space $\longrightarrow F$ instead of the affine space $F$. The proposition is then a simple application of Theorem 39.6. In the special case where $F$ is a normed affine space of finite dimension $m$, for any frame
$$\longrightarrow$$
$(b_{0}, (v_{1}, \dots  , v_{m}))$ of $F$, where $(v_{1}, \dots  , v_{m})$ is a basis of $F$ , every point $x \in F$ can be expressed uniquely as
$$x = b_{0} + x_{1}v_{1} + \cdots  + x_{m}v_{m},$$
where $(x_{1}, \dots  , x_{m}) \in K^{m}$, the coordinates of $x$ in the frame $(b_{0}, (v_{1}, \dots  , v_{m}))$ (where $K =\mathbb{R}$ or $K = \mathbb{C})$. Thus, letting $F_{i}$ be the standard normed affine space $K$ with its natural structure, we note that $F$ is isomorphic to the direct sum $F = (K, 0) \oplus \cdots  \oplus (K, 0)$. Then, every function $f$ : $E \to F$ is represented by $m$ functions $(f_{1}, \dots  , f_{m})$, where $f_{i}$ : $E \to K$ (where $K =\mathbb{R}$ or $K =\mathbb{C})$, and
$$f(x) = b_{0} + f_{1}(x)v_{1} + \cdots  + f_{m}(x)v_{m},$$
for every $x \in E$. The following proposition is an immediate corollary of Proposition 39.9.

> **Proposition 39.10.** For any two normed affine spaces $E$ and $F$, if $F$ is of finite dimension
$$\longrightarrow$$
$m$, for any frame $(b_{0}, (v_{1}, \dots  , v_{m}))$ of $F$, where $(v_{1}, \dots  , v_{m})$ is a basis of $F$ , for every $a \in E$, a function $f$ : $E \to F$ is differentiable at a iff each $f_{i}$ is differentiable at a, and
$$Df(a)(u) = Df_{1}(a)(u)v_{1} + \cdots  + Df_{m}(a)(u)v_{m},$$
$$\longrightarrow$$
for every $u \in E$ . We now consider the situation where $E$ is a finite direct sum. Given a normed affine space $E = (E_{1}, a_{1}) \oplus \cdots  \oplus (E_{n}, a_{n})$ and a normed affine space $F$, given any open subset $A$ of $E$, for any $c = (c_{1}, \dots  , c_{n}) \in A$, we define the continuous functions $i_{j}^{c}$ : $E_{j} \to E$, such that
$$i_{j}^{c}(x) = (c_{1}, \dots  , c_{j-1}, x, c_{j+1}, \dots  , c_{n}).$$
For any function $f$ : $A \to F$, we have functions $f \circ i_{j}^{c}$ : $E_{j} \to F$, defined on $(i_{j}^{c})^{-1}(A)$, which contains $c_{j}$. If D(f $\circ i_{j}^{c})(c_{j})$ exists, we call it the partial derivative of $f$ w.r.t. its jth argument,
$$\longrightarrow  \longrightarrow$$
at $c$. We also denote this derivative by $D_{j}f(c)$. Note that $D_{j}f(c) \in L(E_{j}; F$ ).
