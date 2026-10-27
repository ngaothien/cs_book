# The Hodge *-Operator


<!-- PAGE 1247 -->
$$Proposition 34.14. When E is finite dimensional, the maps \mu : \bigwedge  n(E^{*}) \longrightarrow Alt^{n}(E; K)$$
induced by the linear extensions of the maps given by
$$\mu (v_{1}^{*} \wedge \cdots  \wedge v_{n}^{*})(u_{1}, \dots  , u_{n}) = \det(v_{j}^{*}(u_{i}))$$
$$yield a canonical isomorphism of algebras \mu : \bigwedge  (E^{*}) \longrightarrow Alt(E), where the multiplication in$$
Alt(E) is defined by the maps $\wedge$ : $Alt^{m}(E; K) \times  Alt^{n}(E; K) \longrightarrow Alt^{m+n}(E; K)$, with
$$(f \wedge g)(u_{1}, \dots  , u_{m+n}) = \sum_{shuffle(}  sgn(\sigma ) f(u_{\sigma(1)}, \dots  , u_{\sigma(m)})g(u_{\sigma(m+1)}, \dots  , u_{\sigma(m+n)}),$$
$$\sigma \in m,n)$$
where shuffle(m, $n)$ consists of all $(m$, n)-“shuffles,” that is, permutations $\sigma$  of ${1, \dots  m+n}$ such that $\sigma (1) < \cdots  < \sigma (m)$ and $\sigma (m + 1) < \cdots  < \sigma (m + n)$.
$$Remark: The algebra \bigwedge  (E) is a graded algebra. Given two graded algebras E and F, we$$
can make a new tensor product $E \otimes F$, where $E \otimes F$ is equal to $E \otimes F$ as a vector space,
$$b b$$
but with a skew-commutative multiplication given by
$$(a \otimes b) \wedge (c \otimes d) = (-1)^{deg(b)deg(c)}(ac) \otimes (bd),$$
where $a \in E^{m}, b \in F^{p} , c \in E^{n}, d \in F^{q}$ . Then, it can be shown that
$$^ \oplus  \sim ^\otimes ^$$
$$(EF)=(E)(F).$$
$$b$$

## 34.6 The Hodge *-Operator

In order to define a generalization of the Laplacian that applies to differential forms on a Riemannian manifold, we need to define isomorphisms
$$kn-k$$
$$^V \longrightarrow ^V,$$
for any Euclidean vector space $V$ of dimension $n$ and any $k$, with $0 \le k \le n$. If $\langle$ -, $-\rangle$
$$k$$
$$denotes the inner product on V , we define an inner product on \bigwedge  V , denoted \langle -, -\rangle_{\wedge} , by$$
setting
$$\langle u_{1} \wedge \cdots  \wedge u_{k}, v_{1} \wedge \cdots  \wedge v_{k}\rangle_{\wedge} = \det(\langle u_{i}, v_{j}\rangle ),$$
for all $u_{i}, v_{i} \in V$ , and extending $\langle$ -, $-\rangle_{\wedge}$ by bilinearity.
$$k$$
$$It is easy to show that if (e_{1}, \dots  , e_{n}) is an orthonormal basis of V , then the basis of \bigwedge  V$$
consisting of the $e_{I}$ (where $I = {i_{1}, \dots  , i_{k}}$, with $1 \le i_{1} < \cdots  < i_{k} \le n)$ is an orthonormal
$$k$$
$$basis of \bigwedge  V . Since the inner product on V induces an inner product on V_{*} V^{*} (recall that$$
$$\langle \omega_{1} , \omega_{2} \rangle = \langle \omega_{1}^{\sharp} , \omega_{2}^{\sharp} \rangle , for all \omega_{1} , \omega_{2}  \in V^{*} ), we also get an inner product on \bigwedge  k .$$

<!-- PAGE 1248 -->

> **Definition 34.6.** An orientation of a vector space $V$ of dimension $n$ is given by the choice of some basis $(e_{1}, \dots  , e_{n})$. We say that a basis $(u_{1}, \dots  , u_{n})$ of $V$ is positively oriented iff $det(u_{1}, \dots  , u_{n}) > 0$ (where $det(u_{1}, \dots  , u_{n})$ denotes the determinant of the matrix whose jth column consists of the coordinates of $u_{j}$ over the basis $(e_{1}, \dots  , e_{n}))$, otherwise it is negatively oriented. An oriented vector space is a vector space $V$ together with an orientation of $V$ . If $V$ is oriented by the basis $(e_{1}, \dots  , e_{n})$, then $V^{*}$ is oriented by the dual basis $(e_{1}^{*}, \dots  , e_{n}^{*})$. If $\sigma$  is any permutation of ${1, \dots  , n}$, then the basis $(e_{\sigma(1)}, \dots  , e_{\sigma(n)})$ has positive orientation iff the signature $sgn(\sigma$ ) of the permutation $\sigma$  is even. If $V$ is an oriented vector space of dimension $n$, then we can define a linear isomorphism
$$kn-k$$
$$*:^V \to ^V,$$
called the Hodge *-operator. The existence of this operator is guaranteed by the following proposition.

> **Proposition 34.15.** Let $V$ be any oriented Euclidean vector space whose orientation is given
$$k$$
$$by some chosen orthonormal basis (en, \dots  , e_{n}-k ). For any alternating tensor \alpha  \in \bigwedge  V , there$$
$$is a unique alternating tensor *\alpha  \in \bigwedge^{1}  V such that$$
$$\alpha  \wedge \beta  = \langle *\alpha , \beta \rangle_{\wedge} e_{1} \wedge \cdots  \wedge e_{n}$$
$$n-k$$
$$for all \beta  \in \bigwedge  V . The alternating tensor *\alpha  is independent of the choice of the positive$$
orthonormal basis $(e_{1}, \dots  , e_{n})$.
$$n n$$
$$Proof. Since \bigwedge  V has dimension 1,k  the alternating tensor e_{1} \wedge \cdots  \wedge n-k e_{n} is an basis  of \bigwedge  V .$$
$$It follows that for any fixed \alpha  \in \bigwedge  V , the linear map \lambda_{\alpha}  from \bigwedge  V to \bigwedge  V given by$$
$$\lambda_{\alpha} (\beta ) = \alpha  \wedge \beta$$
is of the form
$$\lambda_{\alpha} (\beta ) = f_{\alpha}(\beta ) e_{1} \wedge \cdots  \wedge e_{n}$$
$$for some linear form  f_{\alpha} \in \begin{pmatrix} n-k V^{*} \\ aunique \end{pmatrix} \bigwedge  . But then, by the duality induced by the inner product$$
$$\langle -, -\rangle on \bigwedge  n-kV , there is   vector *\alpha  \in \bigwedge  n-kV such that$$
$$n-k$$
$$f_{\lambda}(\beta ) = \langle *\alpha , \beta \rangle_{\wedge} for all \beta  \in \bigwedge  V ,$$
which implies that
$$\alpha  \wedge \beta  = \lambda_{\alpha} (\beta ) = f_{\alpha}(\beta ) e_{1} \wedge \cdots  \wedge e_{n} = \langle *\alpha , \beta \rangle_{\wedge} e_{1} \wedge \cdots  \wedge e_{n},$$
as claimed. If $(e_{1}', \dots  , e_{n}')$ is any other positively oriented orthonormal basis, by Proposition 34.2, $e_{1}' \wedge \cdots  \wedge e_{n}' =$ det(P) $e_{1} \wedge \cdots  \wedge e_{n} = e_{1} \wedge \cdots  \wedge e_{n}$, since det(P) $= 1$ where $P$ is the change of basis from $(e_{1}, \dots  , e_{n})$ to $(e_{1}', \dots  , e_{n}')$ and both bases are positively oriented.

<!-- PAGE 1249 -->
$$k n-k$$
$$Definition 34.7. The operator *from \bigwedge  V to \bigwedge  V defined by Proposition 34.15 is$$
called the Hodge *-operator. Obseve that the Hodge *-operator is linear.
$$The Hodge *-operator is defined in terms of the orthonormal basis elements of \bigwedge  V as$$
follows: For any increasing sequence $(i_{1}, \dots  , i_{k})$ of elements $i_{p} \in {1, \dots  , n}$, if $(j_{1}, \dots  , j_{n-k})$ is the increasing sequence of elements $j_{q} \in {1, \dots  , n}$ such that
$${i_{1}, \dots  , i_{k}} \cup {j_{1}, \dots  , j_{n-k}} = {1, \dots  , n},$$
then
$$*(e_{i1} \wedge \cdots  \wedge e_{ik}) = sign(i_{1}, \dots  i_{k}, j_{1}, \dots  , j_{n-k}) e_{j1} \wedge \cdots  \wedge e_{jn-k}.$$
In particular, for $k = 0$ and $k = n$, we have
$$*(1)=e_{1} \wedge \cdots  \wedge e_{n}$$
$$*(e_{1} \wedge \cdots  \wedge e_{n})=1.$$
For example, if $n = 3$, we have
$$*e_{1} = e_{2} \wedge e_{3}$$
$$*e_{2} = -e_{1} \wedge e_{3}$$
$$*e_{3} = e_{1} \wedge e_{2}$$
$$*(e_{1} \wedge e_{2}) = e_{3}$$
$$*(e_{1} \wedge e_{3}) = -e_{2}$$
$$*(e_{2} \wedge e_{3}) = e_{1}.$$
$$The Hodge *-operators *: \bigwedge  Vk  \to \bigwedge  n-Vk  induce a linear map *: \bigwedge  (V ) \to \bigwedge  (V ). We$$
$$also have Hodge *-operators *: \bigwedge^{k}  V^{*} \to \bigwedge^{n-k}  V^{*} .$$
$$The following proposition shows that the linear map *: \bigwedge  (V ) \to \bigwedge  (V ) is an isomorphism.$$

> **Proposition 34.16.** If $V$ is any oriented vector space of dimension $n$, for every $k$ with $0 \le k \le n$, we have
$(i)$ ** $= (-id)^{k(n-k)}$.
$$k$$
$$(ii) \langle x, y\rangle_{\wedge} = *(x \wedge *y) = *(y \wedge *x), for all x, y \in \bigwedge  V .$$

*Proof.* $(1)$ Let $(e_{i})_{i}^{n}$  is an orthonormal basis of $V$ . It is enough to check the identity on basis elements. $We^{=1}$ have
$$*(e_{i1} \wedge \cdots  \wedge e_{ik}) = sign(i_{1}, \dots  i_{k}, j_{1}, \dots  , j_{n-k}) e_{j1} \wedge \cdots  \wedge e_{jn-k}$$

<!-- PAGE 1250 -->
and $**(e_{i1} \wedge \cdots  \wedge e_{ik}) = sign(i_{1}, \dots  i_{k}, j_{1}, \dots  , j_{n-k}) *(e_{j1} \wedge \cdots  \wedge e_{jn-k})$
$$= sign(i_{1}, \dots  i_{k}, j_{1}, \dots  , j_{n-k}) sign(j_{1}, \dots  , j_{n-k}, i_{1}, \dots  i_{k}) e_{i1} \wedge \cdots  \wedge e_{ik}.$$
It is easy to see that
$$sign(i_{1}, \dots  i_{k}, j_{1}, \dots  , j_{n-k}) sign(j_{1}, \dots  , j_{n-k}, i_{1}, \dots  i_{k}) = (-1)^{k(n-k)},$$
which yields
$$**(e_{i1} \wedge \cdots  \wedge e_{ik}) = (-1)^{k(n-k)}e_{i1} \wedge \cdots  \wedge e_{ik},$$
as claimed.
(ii) These identities are easily checked on basis elements; see Jost $[104]$, Chapter $2$, Lemma 2.1.1. In particular let
$$k$$
$$x = e_{i1} \wedge \cdots  \wedge e_{ik},y = e_{ij} \wedge \cdots  \wedge e_{ij},x, y \in ^V,$$
where $(e_{i})_{i=1}^{n}$ is an orthonormal basis of $V$ . If $x \neq  y, \langle x, y\rangle_{\wedge} = 0$ since there is some $e_{ip}$ of $x$ not equal to any $e_{jq}$ of $y$ by the orthonormality of the basis, this means the $p^{th}$ row of $(\langle e_{il}, e_{js}\rangle$ ) consists entirely of zeroes. Also $x \neq  y$ implies that $y \wedge$ *x $= 0$ since
$$*x = sign(i_{1}, \dots  i_{k}, l_{1}, \dots  , l_{n-k})e_{l1} \wedge \cdots  \wedge e_{\ln-k},$$
where $e_{ls}$ is the same as some $e_{p}$ in $y$. A similar argument shows that if $x \neq  y, x \wedge$ *y $= 0$. So now assume $x = y$. Then
$$*(e_{i1} \wedge \cdots  \wedge e_{ik} \wedge *(e_{i1} \wedge \cdots  \wedge e_{ik})) = *(e_{1} \wedge e_{2} \cdots  \wedge e_{n})$$
$$= 1 = \langle x, x\rangle_{\wedge} .$$
It is possible to express *(1) in terms of any basis (not necessarily orthonormal) of $V$ .

> **Proposition 34.17.** If $V$ is any finite-dimensional oriented vector space, for any basis $(v_{!}, \dots  , v_{n})$ of $V$ , we have
$$*(1) = \frac{1}{pdet(\langle v_{i}, v_{j}\rangle )} v_{1} \wedge \cdots  \wedge v_{n}.$$

*Proof.* If $(e_{1}, \dots  , e_{n})$ is an orthonormal basis of $V$ and $(v_{1}, \dots  , v_{n})$ is any other basis of $V$ , then
$$\langle v_{1} \wedge \cdots  \wedge v_{n}, v_{1} \wedge \cdots  \wedge v_{n}\rangle_{\wedge} = \det(\langle v_{i}, v_{j}\rangle ),$$
and since
$$v_{1} \wedge \cdots  \wedge v_{n} = \det(A) e_{1} \wedge \cdots  \wedge e_{n}$$
