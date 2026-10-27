# Transvections and Dilatations


<!-- PAGE 319 -->
$1$. As a row operation, P(i, $k)$ permutes row $i$ and row $k. 2$. As a column operation, P(i, $k)$ permutes column $i$ and column $k. 3$. The inverse of P(i, $k)$ is P(i, $k)$ itself. $4$. As a row operation, $E_{i,j;\beta}$ adds $\beta$  times row $j$ to row $i. 5$. As a column operation, $E_{i,j;\beta}$ adds $\beta$  times column $i$ to column $j$ (note the switch in the indices). $6$. The inverse of $E_{i,j;\beta}$ is $E_{i,j;-\beta}. 7$. As a row operation, $E_{i,\lambda}$ multiplies row $i$ by $\lambda$ . $8$. As a column operation, $E_{i,\lambda}$ multiplies column $i$ by $\lambda$ . $9$. The inverse of $E_{i,\lambda}$ is $E_{i,\lambda-1}$. We can define the notion of a reduced column echelon matrix and show that every matrix can be reduced to a unique reduced column echelon form. Now given any $m \times  n$ matrix $A$, if we first convert $A$ to its reduced row echelon form $R$, it is easy to see that we can apply elementary column operations that will reduce $R$ to a matrix of the form
$$\begin{pmatrix} I_{r} & 0_{r,n-r} \\ 0_{m-r,r} & 0_{m-r,n-r} \end{pmatrix} ,$$
where $r$ is the number of pivots (obtained during the row reduction). Therefore, for every $m\times n$ matrix $A$, there exist two sequences of elementary matrices $E_{1}, \dots  , E_{p}$ and $F_{1}, \dots  , F_{q}$, such that
$$E_{p} \cdots  E_{1}AF_{1} \cdots  F_{q} = \begin{pmatrix} I_{r} & 0_{r,n-r} \\ 0_{m-r,r} & 0_{m-r,n-r} \end{pmatrix} .$$
The matrix on the right-hand side is called the rank normal form of $A$. Clearly, $r$ is the rank of $A$. As a corollary we obtain the following important result whose proof is immediate.

> **Proposition 8.21.** A matrix $A$ and its transpose $A^{\top}$ have the same rank.
$$⊛$$

## 8.15 Transvections and Dilatations

In this section we characterize the linear isomorphisms of a vector space $E$ that leave every vector in some hyperplane fixed. These maps turn out to be the linear maps that are represented in some suitable basis by elementary matrices of the form $E_{i,j;\beta}$ (transvections) or $E_{i,\lambda}$ (dilatations). Furthermore, the transvections generate the group SL(E), and the dilatations generate the group GL(E).

<!-- PAGE 320 -->
Let $H$ be any hyperplane in $E$, and pick some (nonzero) vector $v \in E$ such that $v \in / H$, so that
$$E = H \oplus Kv.$$
Assume that $f$ : $E \to E$ is a linear isomorphism such that f(u) $= u$ for all $u \in H$, and that $f$ is not the identity. We have
$$f(v) = h + \alpha v,for some h \in H and some \alpha  \in K,$$
with $\alpha  \neq  0$, because otherwise we would have f(v) $= h =$ f(h) since $h \in H$, contradicting the injectivity of $f (v \neq  h$ since $v \in / H)$. For any $x \in E$, if we write
$$x = y + tv,for some y \in H and some t \in K,$$
then
$$f(x) = f(y) + f(tv) = y + tf(v) = y + th + t\alpha v,$$
and since $\alpha x = \alpha y + t\alpha v$, we get
$$f(x) -\alpha x = (1 -\alpha )y + th$$
$$f(x) -x = t(h + (\alpha  -1)v).$$
Observe that if $E$ is finite-dimensional, by picking a basis of $E$ consisting of $v$ and basis vectors of $H$, then the matrix of $f$ is a lower triangular matrix whose diagonal entries are all $1$ except the first entry which is equal to $\alpha$ . Therefore, det(f) $= \alpha$ . Case $1. \alpha  \neq  1$. We have f(x) $= \alpha x$ iff(1 - $\alpha )y +$ th $= 0$ iff
$$y = \frac{t}{\alpha  -1} h.$$
Then if we let $w = h + (\alpha$  - 1)v, for $y = (t/(\alpha$  - 1))h, we have
$$x = y + tv = \frac{t}{\alpha  -1} h + tv = \frac{t}{\alpha  -1} (h + (\alpha  -1)v) = \frac{t}{\alpha  -1} w,$$
which shows that f(x) $= \alpha x$ iff $x \in$ Kw. Note that $w \in / H$, since $\alpha$ ̸ $= 1$ and $v \in / H$. Therefore,
$$E = H \oplus Kw,$$
and $f$ is the identity on $H$ and a magnification by $\alpha$  on the line $D =$ Kw.

> **Definition 8.8.** Given a vector space $E$, for any hyperplane $H$ in $E$, any nonzero vector $u \in E$ such that $u \notin H$, and any scalar $\alpha  \neq  0, 1$, a linear map $f$ such that f(x) $= x$ for all $x \in H$ and f(x) $= \alpha x$ for every $x \in D =$ Ku is called a dilatation of hyperplane $H$, direction $D$, and scale factor $\alpha$ .

<!-- PAGE 321 -->
If $\pi_{H}$  and $\pi_{D}$  are the projections of $E$ onto $H$ and $D$, then we have
$$f(x) = \pi_{H} (x) + \alpha \pi_{D} (x).$$
The inverse of $f$ is given by
$$f^{-1} (x) = \pi_{H} (x) + \alpha^{-1} \pi_{D} (x).$$
When $\alpha  = -1$, we have $f^{2} =$ id, and $f$ is a symmetry about the hyperplane $H$ in the direction $D$. This situation includes orthogonal reflections about $H$. Case $2. \alpha  = 1$. In this case,
$$f(x) -x = th,$$
that is, f(x) - $x \in$ Kh for all $x \in E$. Assume that the hyperplane $H$ is given as the kernel of some linear form $\phi$ , and let $a = \phi (v)$. We have $a \neq  0$, since $v \in / H$. For any $x \in E$, we have
$$\phi (x -a^{-1}\phi (x)v) = \phi (x) -a^{-1}\phi (x)\phi (v) = \phi (x) -\phi (x) = 0,$$
which shows that $x$ - $a^{-1}\phi$ (x)v $\in H$ for all $x \in E$. Since every vector in $H$ is fixed by $f$, we get
$$x -a^{-1}\phi (x)v = f(x -a^{-1}\phi (x)v)$$
$$= f(x) -a^{-1}\phi (x)f(v),$$
so
$$f(x) = x + \phi (x)(f(a^{-1}v) -a^{-1}v).$$
Since f(z) - $z \in$ Kh for all $z \in E$, we conclude that $u = f(a^{-1}v)$ - $a^{-1}v = \beta h$ for some $\beta  \in K$, so $\phi (u) = 0$, and we have
$$f(x) = x + \phi (x)u,\phi (u) = 0.(*)$$
A linear map defined as above is denoted by $\tau_{\phi ,u}$ . Conversely for any linear map $f = \tau_{\phi ,u}$  given by Equation (*), where $\phi$  is a nonzero linear form and $u$ is some vector $u \in E$ such that $\phi (u) = 0$, if $u = 0$ , then $f$ is the identity, so assume that $u \neq  0$. If so, we have f(x) $= x$ iff $\phi (x) = 0$, that is, iff $x \in H$. We also claim that the inverse of $f$ is obtained by changing $u$ to $-u$. Actually, we check the slightly more general fact that
$$\tau_{\phi ,u}  \circ \tau_{\phi ,w}  = \tau_{\phi ,u+w} .$$
Indeed, using the fact that $\phi (w) = 0$, we have
$$\tau_{\phi ,u} (\tau_{\phi ,w} (x)) = \tau_{\phi ,w} (x) + \phi (\tau_{\phi ,w} (x))u$$
$$= \tau_{\phi ,w} (x) + (\phi (x) + \phi (x)\phi (w))u$$
$$= \tau_{\phi ,w} (x) + \phi (x)u$$
$$= x + \phi (x)w + \phi (x)u$$
$$= x + \phi (x)(u + w).$$

<!-- PAGE 322 -->
For $v = -u$, we have $\tau_{\phi ,u+v}  = \phi_{\phi ,0}  =$ id, so $\tau_{\phi ,u}^{-1}   = \tau_{\phi ,-u}$ , as claimed. Therefore, we proved that every linear isomorphism of $E$ that leaves every vector in some hyperplane $H$ fixed and has the property that f(x) - $x \in H$ for all $x \in E$ is given by a map $\tau_{\phi ,u}$  as defined by Equation (*), where $\phi$  is some nonzero linear form defining $H$ and $u$ is some vector in $H$. We have $\tau_{\phi ,u}  =$ id iff $u = 0$.

> **Definition 8.9.** Given any hyperplane $H$ in $E$, for any nonzero nonlinear form $\phi  \in E^{*}$ defining $H$ (which means that $H =$ Ker $(\phi$ )) and any nonzero vector $u \in H$, the linear map $f = \tau_{\phi ,u}$  given by
$$\tau_{\phi ,u} (x) = x + \phi (x)u,\phi (u) = 0,$$
for all $x \in E$ is called a transvection of hyperplane $H$ and direction $u$. The map $f = \tau_{\phi ,u}$ leaves every vector in $H$ fixed, and f(x) - $x \in$ Ku for all $x \in E$. The above arguments show the following result.

> **Proposition 8.22.** Let $f$ : $E \to E$ be a bijective linear map and assume that f̸ $=$ id and that f(x) $= x$ for all $x \in H$, where $H$ is some hyperplane in $E$. If there is some nonzero vector $u \in E$ such that $u \in / H$ and f(u) - $u \in H$, then $f$ is a transvection of hyperplane $H$; otherwise, $f$ is a dilatation of hyperplane $H$.

*Proof.* Using the notation as above, for some $v \in / H$, we have f(v) $= h + \alpha v$ with $\alpha  \neq  0$, and write $u = y +$ tv with $y \in H$ and $t \neq  0$ since $u \in / H$. If f(u) - $u \in H$, from
$$f(u) -u = t(h + (\alpha  -1)v),$$
we get $(\alpha$  - 1)v $\in H$, and since $v \in / H$, we must have $\alpha  = 1$, and we proved that $f$ is a transvection. Otherwise, $\alpha  \neq  0, 1$, and we proved that $f$ is a dilatation. If $E$ is finite-dimensional, then $\alpha  =$ det(f), so we also have the following result.

> **Proposition 8.23.** Let $f$ : $E \to E$ be a bijective linear map of a finite-dimensional vector space $E$ and assume that $f \neq$  id and that f(x) $= x$ for all $x \in H$, where $H$ is some hyperplane in $E$. If det(f) $= 1$, then $f$ is a transvection of hyperplane $H$; otherwise, $f$ is a dilatation of hyperplane $H$. Suppose that $f$ is a dilatation of hyperplane $H$ and direction $u$, and say det(f) $= \alpha  \neq  0, 1$. Pick a basis $(u, e_{2}, \dots  , e_{n})$ of $E$ where $(e_{2}, \dots  , e_{n})$ is a basis of $H$. Then the matrix of $f$ is of the form
$$\begin{pmatrix} \alpha & 0 & \cdots & 0 \\ 0 & 1 & 0 \\ \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix} ,$$

<!-- PAGE 323 -->
which is an elementary matrix of the form $E_{1,\alpha}$. Conversely, it is clear that every elementary matrix of the form $E_{i,\alpha}$ with $\alpha  \neq  0, 1$ is a dilatation. Now, assume that $f$ is a transvection of hyperplane $H$ and direction $u \in H$. Pick some $v \in / H$, and pick some basis $(u, e_{3}, \dots  , e_{n})$ of $H$, so that $(v, u, e_{3}, \dots  , e_{n})$ is a basis of $E$. Since f(v) - $v \in$ Ku, the matrix of $f$ is of the form
$$\begin{pmatrix} 1 & 0 & \cdots & 0 \\ \alpha & 1 & 0 \\ \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix} ,$$
which is an elementary matrix of the form $E_{2,1;\alpha}$. Conversely, it is clear that every elementary matrix of the form $E_{i,j;\alpha} (\alpha  \neq  0)$ is a transvection. The following proposition is an interesting exercise that requires good mastery of the elementary row operations $E_{i,j;\beta}$; see Problems 8.10 and 8.11.

> **Proposition 8.24.** Given any invertible $n \times  n$ matrix $A$, there is a matrix $S$ such that
$$SA = \begin{pmatrix} I_{n-1} & 0 \\ 0 & \alpha \end{pmatrix} = E_{n,\alpha},$$
with $\alpha  =$ det(A), and where $S$ is a product of elementary matrices of the form $E_{i,j;\beta}$; that is, $S$ is a composition of transvections. Surprisingly, every transvection is the composition of two dilatations!

> **Proposition 8.25.** If the field $K$ is not of characteristic $2$, then every transvection $f$ of hyperplane $H$ can be written as $f = d_{2} \circ d_{1}$, where $d_{1}, d_{2}$ are dilatations of hyperplane $H$, where the direction of $d_{1}$ can be chosen arbitrarily.

*Proof.* Pick some dilatation $d_{1}$ of hyperplane $H$ and scale factor $\alpha  \neq  0, 1$. Then, $d_{2} = f \circ d_{1}^{-1}$ leaves every vector in $H$ fixed, and $det(d_{2}) = \alpha^{-1} \neq  1$. By Proposition 8.23, the linear map $d_{2}$ is a dilatation of hyperplane $H$, and we have $f = d_{2} \circ d_{1}$, as claimed. Observe that in Proposition 8.25, we can pick $\alpha  = -1$; that is, every transvection of hyperplane $H$ is the compositions of two symmetries about the hyperplane $H$, one of which can be picked arbitrarily.
Remark: Proposition 8.25 holds as long as $K \neq  {0, 1}$. The following important result is now obtained.

> **Theorem 8.26.** Let $E$ be any finite-dimensional vector space over a field $K$ of characteristic not equal to $2$. Then the group SL(E) is generated by the transvections, and the group GL(E) is generated by the dilatations.

<!-- PAGE 324 -->

*Proof.* Consider any $f \in$ SL(E), and let $A$ be its matrix in any basis. By Proposition 8.24, there is a matrix $S$ such that
$$SA = \begin{pmatrix} I_{n-1} & 0 \\ 0 & \alpha \end{pmatrix} = E_{n,\alpha},$$
with $\alpha  =$ det(A), and where $S$ is a product of elementary matrices of the form $E_{i,j;\beta}$. Since det(A) $= 1$, we have $\alpha  = 1$, and the result is proven. Otherwise, if $f$ is invertible but $f \in /$ SL(E), the above equation shows $E_{n,\alpha}$ is a dilatation, $S$ is a product of transvections, and by Proposition 8.25, every transvection is the composition of two dilatations. Thus, the second result is also proven. We conclude this section by proving that any two transvections are conjugate in GL(E). Let $\tau_{\phi ,u}  (u \neq  0)$ be a transvection and let $g \in$ GL(E) be any invertible linear map. We have
$$(g \circ \tau_{\phi ,u}  \circ g^{-1})(x) = g(g^{-1}(x) + \phi (g^{-1}(x))u)$$
$$= x + \phi (g^{-1}(x))g(u).$$
Let us find the hyperplane determined by the linear form $x \mapsto \phi (g^{-1}(x))$. This is the set of vectors $x \in E$ such that $\phi (g^{-1}(x)) = 0$, which holds iff $g^{-1}(x) \in H$ iff $x \in$ g(H). Therefore, Ker $(\phi \circ g^{-1}) =$ g(H) $=$ H', and we have g(u) $\in$ g(H) $=$ H', so $g\circ \tau_{\phi ,u} \circ g^{-1}$ is the transvection of hyperplane H' $=$ g(H) and direction u' $=$ g(u) (with u' $\in$ H').
$$̸$$
Conversely, let $\tau_{\psi ,u'}$  be some transvection (u' $= 0)$. Pick some vectors $v$, v' such that $\phi (v) = \psi$ (v') $= 1$, so that
$$E = H \oplus Kv = H'\oplus Kv'.$$
There is a linear map $g \in$ GL(E) such that g(u) $=$ u', g(v) $=$ v', and g(H) $=$ H'. To define $g$, pick a basis $(v, u, e_{2}, \dots  , e_{n-1})$ where $(u, e_{2}, \dots  , e_{n-1})$ is a basis of $H$ and pick a basis (v', u', $e_{2}', \dots  , e_{n-1}')$ where (u', $e_{2}', \dots  , e_{n-1}')$ is a basis of H'; then $g$ is defined so that g(v) $=$ v', g(u) $=$ u', and $g(e_{i}) = g(e_{i}')$, for $i = 2, \dots  , n$ - $1$. If $n = 2$, then $e_{i}$ and $e_{i}'$ are missing. Then, we have
$$(g \circ \tau_{\phi ,u}  \circ g^{-1})(x) = x + \phi (g^{-1}(x))u'.$$
Now $\phi  \circ g^{-1}$ also determines the hyperplane H' $=$ g(H), so we have $\phi  \circ g^{-1} = \lambda \psi$  for some nonzero $\lambda$  in $K$. Since v' $=$ g(v), we get
$$\phi (v) = \phi  \circ g^{-1}(v') = \lambda \psi (v'),$$
and since $\phi (v) = \psi$ (v') $= 1$, we must have $\lambda  = 1$. It follows that
$$(g \circ \tau_{\phi ,u}  \circ g^{-1})(x) = x + \psi (x)u'= \tau_{\psi ,u'} (x).$$
In summary, we proved almost all parts the following result.
