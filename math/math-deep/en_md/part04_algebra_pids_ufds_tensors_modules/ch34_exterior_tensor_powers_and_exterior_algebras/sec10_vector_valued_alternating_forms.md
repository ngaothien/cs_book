# Vector-Valued Alternating Forms


<!-- PAGE 1267 -->
Conversely, assume that dim(U $\cap V$ ) $\ge 1$. Pick a basis $(w_{1}, \dots  , w_{r})$ of $W = U \cap V$ , and extend this basis to a basis $(w_{1}, \dots  , w_{r}, w_{r+1}, \dots  , w_{p})$ of $U$ and to a basis $(w_{1}, \dots  , w_{r}, w_{p+1}, \dots , w_{p+q-r})$ of $V$ . By Corollary 34.26, $(u_{1}, \dots  , u_{p})$ is also basis of $U$, so
$$u_{1} \wedge \cdots  \wedge u_{p} = a w_{1} \wedge \cdots  \wedge w_{r} \wedge w_{r+1} \wedge \cdots  \wedge w_{p}$$
for some $a \in K$, and $(v_{1}, \dots  , v_{q})$ is also basis of $V$ , so
$$v_{1} \wedge \cdots  \wedge v_{q} = b w_{1} \cdots  \wedge w_{r} \wedge w_{p+1} \wedge \cdots  \wedge w_{p+q-r}$$
for some $b \in K$, and thus
$$u \wedge v = u_{1} \wedge \cdots  \wedge u_{p} \wedge v_{1} \wedge \cdots  \wedge v_{q} = 0$$
since it contains some repeated $w_{i}$, with $1 \le i \le r$. As an application of Proposition 34.31, consider two projective lines $D_{1}$ and $D_{2}$ in $\mathbb{RP}^{3}$, which means that $D_{1}$ and $D_{2}$ correspond to two 2-planes in $\mathbb{R}^{4}$, and thus by Proposition
$$\mathbb{RP}(_{2}^{4})^{-1} \mathbb{RP}^{5}$$
34.30, to two points in $=$ . These two points correspond to the 2-vectors
$$z = a_{1,2}e_{1} \wedge e_{2} + a_{1,3}e_{1} \wedge e_{3} + a_{1,4}e_{1} \wedge e_{4} + a_{2,3}e_{2} \wedge e_{3} + a_{2,4}e_{2} \wedge e_{4} + a_{3,4}e_{3} \wedge e_{4}$$
and z' $= a_{1,2}'e_{1} \wedge e_{2} + a_{1,3}'e_{1} \wedge e_{3} + a_{1,4}'e_{1} \wedge e_{4} + a_{2,3}'e_{2} \wedge e_{3} + a_{2,4}'e_{2} \wedge e_{4} + a_{3,4}'e_{3} \wedge e_{4}$ whose Pl¨ucker coordinates, (where $a_{i,j} = \lambda_{ij}$ ), satisfy the equation
$$\lambda_{12} \lambda_{34}  -\lambda_{13} \lambda_{24}  + \lambda_{14} \lambda_{23}  = 0$$
of the Klein quadric, and $D_{1}$ and $D_{2}$ intersect iff $z \wedge$ z' $= 0$ iff
$$a_{1,2}a_{3,4}' -a_{1,3}a_{3,4}' + a_{1,4}a_{2,3}' + a_{2,3}a_{1,4}' -a_{2,4}a_{1,3}' + a_{3,4}a_{1,2}' = 0.$$
Observe that for $D_{1}$ fixed, this is a linear condition. This fact is very helpful for solving problems involving intersections of lines. A famous problem is to find how many lines $in\mathbb{RP}^{3}$ meet four given lines in general position. The answer is at most $2$.

## 34.10 Vector-Valued Alternating Forms

The purpose of this section is to present the technical background needed to understand vector-valued differential forms, in particular in the case of Lie groups where differential forms taking their values in a Lie algebra arise naturally. In this section the vector space $E$ is assumed to have finite dimension. We know that
$$n \sim$$
$$there is a canonical isomorphism \bigwedge  (E^{*})= Alt^{n}(E; K) between alternating n-forms and$$

<!-- PAGE 1268 -->
alternating multilinear maps. As in the case of general tensors, the isomorphisms provided by Propositions 34.5, 33.19, and 34.10, namely
$$\sim$$
$$Alt^{n}(E; F)=Hom \begin{pmatrix} n \\ ^(E), F \\ * \end{pmatrix}$$
$$\sim \otimes$$
$$Hom \begin{pmatrix} n \\ ^(E), F \\ n \end{pmatrix} = \begin{pmatrix} n \\ ^(E) \end{pmatrix} F$$
$$*n$$
$$\sim ^$$
$$\begin{pmatrix} ^(E) \end{pmatrix} =(E^{*})$$
yield a canonical isomorphism
$$\sim \otimes$$
$$Alt^{n}(E; F)= \begin{pmatrix} n \\ ^(E^{*}) \end{pmatrix} F$$
which we record as a corollary.

> **Corollary 34.32.** For any finite-dimensional vecgtor space $E$ and any vector space $F$, we have a canonical isomorphism
$$\sim \otimes$$
$$Alt^{n}(E; F)= \begin{pmatrix} n \\ ^(E^{*}) \end{pmatrix} F.$$
Note that $F$ may have infinite dimension. This isomorphism allows us to view the tensors
$$in \bigwedge  n(E^{*})\otimes F as vector-valued alternating forms, a point of view that is useful in differential$$
$$geometry. If (f_{1}, \dots  , f_{r}) is a basis of F, every tensor \omega  \in \bigwedge  n(E^{*}) \otimes F can be written as$$
some linear combination
$$\omega  = \sum_{i=1}^{r}  \alpha_{i}  \otimes f_{i},$$
$$with \alpha_{i}  \in \bigwedge  n(E^{*}).We also let$$
$$n!$$
$$^(E; F) =M^(E^{*})\otimes F = \begin{pmatrix} ^(E) \end{pmatrix} \otimes F.$$
$$n=0$$
Given three vector spaces, $F, G, H$, if we have some bilinear map $\Phi$ : $F \times  G \to H$, then we can define a multiplication operation
$$\wedge_{\Phi}  :^(E; F) \times ^(E; G) \to ^(E; H)$$
as follows: For every pair $(m, n)$, we define the multiplication
$$! !$$
$$\wedge_{\Phi}  : \begin{pmatrix} m \\ ^(E^{*}) \end{pmatrix} \otimes F\times \begin{pmatrix} n \\ ^(E^{*}) \end{pmatrix} \otimes G\longrightarrow \begin{pmatrix} m+n \\ ^(E^{*}) \end{pmatrix} \otimes H$$

<!-- PAGE 1269 -->
by
$$\omega  \wedge_{\Phi}  \eta  = (\alpha  \otimes f) \wedge_{\Phi}  (\beta  \otimes g) = (\alpha  \wedge \beta ) \otimes \Phi (f, g).$$
As in Section 34.5 (following $H$. Cartan $[35])$, we can also define a multiplication
$$\wedge_{\Phi}  : Alt^{m}(E; F) \times  Alt^{n}(E; G) \longrightarrow Alt^{m+n}(E; H)$$
directly on alternating multilinear maps as follows: For $f \in Alt^{m}(E; F)$ and $g \in Alt^{n}(E; G)$,
$$(f \wedge_{\Phi}  g)(u_{1}, \dots  , u_{m+n}) = \sum_{shuffle(}  sgn(\sigma ) \Phi \begin{pmatrix} f(u_{\sigma(1)}, \dots  , u_{\sigma(m)}), g(u_{\sigma(m+1)}, \dots  , u_{\sigma(m+n)}) \end{pmatrix} ,$$
$$\sigma \in m,n)$$
where shuffle(m, $n)$ consists of all $(m$, n)-“shuffles;” that is, permutations $\sigma$  of ${1, \dots  m + n}$ such that $\sigma (1) < \cdots  < \sigma (m)$ and $\sigma (m + 1) < \cdots  < \sigma (m + n)$. A special case of interest is the case where $F = G = H$ is a Lie algebra and $\Phi$ (a, $b) = [a, b]$
$$is the Lie bracket of F. In this case, using a basis (f_{1}, \dots  , f_{r}) of F, if we write \omega  = \sum_{i}  \alpha_{i} \otimes f_{i}$$
$$and \eta  = \sum_{j}  \beta_{j}  \otimes f_{j}, we have$$
$$\omega  \wedge_{\Phi}  \eta  = [\omega , \eta ] = \sum_{i,j}  \alpha_{i}  \wedge \beta_{j}  \otimes [f_{i}, f_{j}].$$
It is customary to denote $\omega \wedge_{\Phi} \eta$  by $[\omega , \eta$ ] (unfortunately, the bracket notation is overloaded). Consequently,
$$[\eta , \omega ] = (-1)^{mn+1}[\omega , \eta ].$$
In general not much can be said about $\wedge_{\Phi}$ , unless $\Phi$  has some additional properties. In particular, $\wedge_{\Phi}$  is generally not associative. We now use vector-valued alternating forms to generalize both the $\mu$  map of Proposition 34.14 and generalize Proposition 33.19 by defining the map
$$n!$$
$$\mu_{F}  :^(E^{*})\otimes F \longrightarrow Alt^{n}(E; F)$$
on generators by
$$\mu_{F} ((v_{1}^{*} \wedge \cdots  \wedge v_{n}^{*}) \otimes f)(u_{1}, \dots  , u_{n}) = (\det(v_{j}^{*}(u_{i}))f,$$
with $v_{1}^{*}, \dots  , v_{n}^{*} \in E^{*}, u_{1}, \dots  , u_{n} \in E$, and $f \in F$.

> **Proposition 34.33.** The map
$$n!$$
$$\mu_{F}  :^(E^{*})\otimes F \longrightarrow Alt^{n}(E; F)$$
defined as above is a canonical isomorphism for every $n \ge 0$. Furthermore, given any three
$$vector spaces, F, G, H, and any bilinear map \Phi : F \times  G \to H, for all \omega  \in (^{n} \bigwedge  (E^{*})) \otimes F and$$
$$all \eta  \in (^{n} \bigwedge  (E^{*})) \otimes G,$$
$$\mu_{H} (\omega  \wedge_{\Phi}  \eta ) = \mu_{F} (\omega ) \wedge_{\Phi}  \mu_{G} (\eta ).$$

<!-- PAGE 1270 -->
$$Proof. Since we already know that ( \bigwedge  (E^{*}))\otimes F and Alt^{n}(E; F) are isomorphic, it is enough$$
$$to show that \mu_{F}  maps some basis of (^{n} \bigwedge_{\in J}^{n}  (E^{*})) \otimes F to linearly independent elements. Pick$$
some bases $(e_{1}, \dots  , e_{p})$ in $E$ and $(f_{j})_{j}$  in $F$. Then we know that the vectors $e_{I}^{*} \otimes f_{j}$, where
$$I \subseteq {1, \dots  , p} and |I| = n, form a basis of (^{n} \bigwedge  (E^{*})) \otimes F. If we have a linear dependence$$
$$\sum_{I,j}  \lambda_{I,j} \mu_{F} (e_{I}^{*} \otimes f_{j}) = 0,$$
applying the above combination to each $(e_{i1}, \dots  , e_{in}) (I = {i_{1}, \dots  , i_{n}}, i_{1} < \cdots  < i_{n})$, we get the linear combination
$$\sum_{j}  \lambda_{I,j} f_{j} = 0,$$
and by linear independence of the $f_{j}’s$, we get $\lambda_{I,j}  = 0$ for all I and all $j$. Therefore, the $\mu_{F} (e_{I}^{*} \otimes f_{j})$ are linearly independent, and we are done. The second part of the proposition is checked using a simple computation. The following proposition will be useful in dealing with vector-valued differential forms.
$$Proposition 34.34. If (e_{1}, \dots  , e_{p}) is any basis of E, then every element \omega  \in (^{n} \bigwedge  (E^{*})) \otimes F$$
can be written in a unique way as
$$\omega  = \sum_{I}  e_{I}^{*} \otimes f_{I},f_{I} \in F,$$
where the $e_{I}^{*}$ are defined as in Section 34.2.
$$Proof. Since, by Proposition 34.7, the e_{I}^{*} form a basis of \bigwedge  n(E^{*}), elements of the form e_{I}^{*} \otimes f$$
$$span (^{n} \bigwedge  (E^{*})) \otimes F.Now if we apply \mu_{F} (\omega ) to (e_{i1}, \dots  , e_{in}), where I = {i_{1}, \dots  , i_{n}} \subseteq$$
${1, \dots  , p}$, we get
$$\mu_{F} (\omega )(e_{i1}, \dots  , e_{in}) = \mu_{F} (e_{I}^{*} \otimes f_{I})(e_{i1}, \dots  , e_{in}) = f_{I}.$$
Therefore, the $f_{I}$ are uniquely determined by $f$. Proposition 34.34 can also be formulated in terms of alternating multilinear maps, a fact that will be useful to deal with differential forms.

> **Corollary 34.35.** Define the product $\cdot$ : $Alt^{n}(E;\mathbb{R}) \times  F \to Alt^{n}(E; F)$ as follows: For all $\omega  \in Alt^{n}(E;\mathbb{R})$ and all $f \in F$,
$$(\omega  \cdot  f)(u_{1}, \dots  , u) = \omega (u_{1}, \dots  , u_{n})f,$$
$$for all u_{1}, \dots  , u_{n} \in E. Then for every \omega  \in (^{n} \bigwedge^{n}  (E^{*})) \otimes F of the form$$
$$\omega  = u_{1}^{*} \wedge \cdots  \wedge u_{n}^{*} \otimes f,$$
we have
$$\mu_{F} (u_{1}^{*} \wedge \cdots  \wedge u_{n}^{*} \otimes f) = \mu_{F} (u_{1}^{*} \wedge \cdots  \wedge u_{n}^{*}) \cdot  f.$$
