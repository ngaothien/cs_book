# Complexification of a Real Projective Space


<!-- PAGE 952 -->
$$c$$
$$d_{1}$$
$$d_{2}$$
$$d_{3}$$
$$d_{4}$$
$$\Delta$$
$$d_{1}'d_{2}'d_{3}'d_{4}'\Delta'$$
$$D_{1}D_{2}D_{3}D_{4}$$
$$Figure 26.39: A pencil of lines and its cross-ratio with intersecting lines.$$
$G = \psi^{-1} (0)$. Let $a =$ P(F) $\cap \Delta$ and $b =$ P(G) $\cap \Delta$ . There are some vectors $u, v \in D$ such that $a =$ p(u) and $b =$ p(v), and since $\phi$  and $\psi$  are linearly independent, we have $a \neq  b$, and we can choose $\phi$  and $\psi$  such that $\phi (v) = -1$ and $\psi (u) = 1$. Also, $(u, v)$ is a basis of $D$. Then a point $p(\alpha u + \beta v)$ on $\Delta$ belongs to the hyperplane $H = p(\gamma \phi  + \delta \psi$ ) of the pencil $P$ iff
$$(\gamma \phi  + \delta \psi )(\alpha u + \beta v) = 0,$$
which, since $\phi (u) = 0, \psi (v) = 0, \phi (v) = -1$, and $\psi (u) = 1$, yields $\gamma \beta  = \delta \alpha$ , which is equivalent to $[\alpha , \beta$ ] $= [\gamma , \delta$ ] in $P(K^{2})$. But then the map $h: P \to \Delta$ is a projectivity. Letting $d_{i} = \Delta \cap H_{i}$, since by Proposition 26.20 a projectivity of lines preserves the cross-ratio, we get $[d_{1}, d_{2}, d_{3}, d_{4}] = [H_{1}, H_{2}, H_{3}, H_{4}]$.

## 26.14 Complexification of a Real Projective Space

Notions such as orthogonality, angles, and distance between points are not projective concepts. In order to define such notions, one needs an inner product on the underlying vector space. We say that such notions belong to Euclidean geometry. At first glance, the fact that some important Euclidean concepts are not covered by projective geometry seems a major drawback of projective geometry. Fortunately, geometers of the nineteenth century (including Laguerre, Monge, Poncelet, Chasles, von Staudt, Cayley, and Klein) found an astute way of recovering certain Euclidean notions such as angles and orthogonality (also circles) by embedding real projective spaces into complex projective spaces. In the next two sections we will give a brief account of this method. More details can be found in Berger $[11, 12]$, Pedoe $[141]$, Samuel $[148]$, Coxeter $[43, 44]$, Sidler $[167]$, Tisseron $[181]$, Lehmann and Bkouche $[119]$, and, of course, Volume II of Veblen and Young $[190]$.

<!-- PAGE 953 -->
The first step is to embed a real vector space $E$ into a complex vector space $E_{C}$. A quick but somewhat bewildering way to do so is to define the complexification of $E$ as the tensor product $\mathbb{C} \otimes E$. A more tangible way is to define the following structure.

> **Definition 26.13.** Given a real vector space $E$, let $E_{C}$ be the structure $E \times  E$ under the addition operation
$$(u_{1}, u_{2}) + (v_{1}, v_{2}) = (u_{1} + v_{1}, u_{2} + v_{2}),$$
and let multiplication by a complex scalar $z = x +$ iy be defined such that
$$(x + iy) \cdot  (u, v) = (xu -yv, yu + xv).$$
It is easily shown that the structure $E_{C}$ is a complex vector space. It is also immediate that
$$(0, v) = i(v, 0),$$
and thus, identifying $E$ with the subspace of $E_{C}$ consisting of all vectors of the form $(u, 0)$, we can write
$$(u, v) = u + iv.$$
Given a vector $w = u +$ iv, its conjugate $\overline{w}$ is the vector $\overline{w} = u$ - iv. Then conjugation is a map from $E_{C}$ to itself that is an involution. If $(e_{1}, \dots  , e_{n})$ is any basis of $E$, then $((e_{1}, 0), \dots  , (e_{n}, 0))$ is a basis of $E_{C}$. We call such a basis a real basis. Given a linear map $f$ : $E \to E$, the map $f$ can be extended to a linear map $f_{C}$ : $E_{C} \to E_{C}$ defined such that
$$f_{C}(u + iv) = f(u) + if(v).$$
$$We define the complexification of P(E) as P(E_{C} ). If \begin{pmatrix} \longrightarrow \\ E,E \\ (E_{C}b \end{pmatrix} is a real affine space, we$$
define the complexified projective completion of as $P$ ) and denote it by $E_{C}$. Then
$$E is naturally embedded inE_{C}, and it is called \begin{pmatrix} \longrightarrow \\ E,E \\ theset \end{pmatrix} of real  points ofE_{C}. e$$
$e  e  e$ If $E$ has dimension $n+1$ and $(e_{1}, \dots  , e_{n+1})$ is a basis of $E$, given any homogeneous polynomial $P(x_{1}, \dots  , x_{n+1})$ over $\mathbb{C}$ of total degree $m$, because $P$ is homogeneous, it is immediately verified that
$$P(x_{1}, \dots  , x_{n+1}) = 0$$
iff
$$P(\lambda x_{1}, \dots  , \lambda x_{n+1}) = 0,$$
for any $\lambda  \neq  0$. Thus, we can define the hypersurface $V (P)$ of equation $P(x_{1}, \dots  , x_{n+1}) = 0$ as the subset of $E_{C}$ consisting of all points of homogeneous coordinates $(x_{1}, \dots  , x_{n+1})$ such that
$$e$$
$P(x_{1}, \dots  , x_{n+1}) = 0$. We say that the hypersurface $V (P)$ of equation $P(x_{1}, \dots  , x_{n+1}) = 0$ is real whenever $P(x_{1}, \dots  , x_{n+1}) = 0$ implies that $P(\overline{x}_{1}\overline{, \dots  , x}_{n+1}) = 0$.
