# Some Useful Isomorphisms for Tensor Products


<!-- PAGE 1187 -->

*Proof.* For each $k, 1 \le k \le n$, every $v^{k} \in E_{k}$ can be written uniquely as
$$v^{k} = \sum_{j\in Ik}  v_{j}^{k} u_{j}^{k},$$
for some family of scalars $(v_{j}^{k} )_{j\in Ik}$. Let $F$ be any nontrivial vector space. We show that for every family
$$(w_{i1,...,in})_{(i1,...,in)\in I1\times...\times In},$$
of vectors in $F$, there is some linear map $h: E_{1} \otimes \cdots  \otimes E_{n} \to F$ such that
$$h(u_{i1}^{1} \otimes \cdots  \otimes u_{in}^{n}) = w_{i1,...,in}.$$
Then by Proposition 33.4, it follows that
$$(u_{i1}^{1} \otimes \cdots  \otimes u_{in}^{n})_{(i1,...,in)\in I1\times...\times In}$$
is linearly independent. However, since $(u_{i}^{k} )_{i\in Ik}$ is a basis for $E_{k}$, the $u_{i1}^{1} \otimes \cdots  \otimes u_{in}^{n}$ also generate $E_{1} \otimes \cdots  \otimes E_{n}$, and thus, they form a basis of $E_{1} \otimes \cdots  \otimes E_{n}$. We define the function $f$ : $E_{1} \times  \cdots  \times  E_{n} \to F$ as follows: For any $n$ nonempty finite subsets $J_{1}, \dots  , J_{n}$ such that $J_{k} \subseteq I_{k}$ for $k = 1, \dots  , n$,
$$f( \sum_{j1\in J1}  v_{j1}^{1}u_{j1}^{1}, \dots  , \sum_{jn\in Jn}  v_{jn}^{n}u_{jn}^{n}) = \sum_{J1,...,jn}  v_{j1}^{1} \cdots  v_{jn}^{n} w_{j1,...,jn}.$$
$$j1\in \in Jn$$
It is immediately verified that $f$ is multilinear. By the universal mapping property of the tensor product, the linear map $f_{\otimes}: E_{1} \otimes \cdots  \otimes E_{n} \to F$ such that $f = f_{\otimes} \circ \phi$ , is the desired map $h$. In particular, when each $I_{k}$ is finite and of size $m_{k} = dim(E_{k})$, we see that the dimension of the tensor product $E_{1} \otimes \cdots  \otimes E_{n}$ is $m_{1} \cdots  m_{n}$. As a corollary of Proposition 33.12, if $(u_{i}^{k} )_{i\in Ik}$ is a basis for $E_{k}, 1 \le k \le n$, then every tensor $z \in E_{1} \otimes \cdots  \otimes E_{n}$ can be written in a unique way as
$$z = \sum_{n)\in I1}  \lambda_{i1,...,in}  u_{i1}^{1} \otimes \cdots  \otimes u_{in}^{n},$$
$$(i1,...,i\times ...\times In$$
for some unique family of scalars $\lambda_{i1,...,in}  \in K$, all zero except for a finite number.

## 33.4 Some Useful Isomorphisms for Tensor Products


> **Proposition 33.13.** Given three vector spaces $E, F, G$, there exists unique canonical isomorphisms
$(1)  \otimes  \sim  \otimes E F = F E$

<!-- PAGE 1188 -->
$(2)  \otimes  \otimes  \sim  \otimes  \otimes  \sim  \otimes  \otimes (E F) G = E (F G) = E F G$
$(3)  \oplus  \otimes  \sim  \otimes  \oplus  \otimes (E F) G = (E G) (F G)$
$(4)  \otimes  \sim K E = E$ such that respectively
$$(a) u \otimes v \mapsto v \otimes u$$
$$(b) (u \otimes v) \otimes w \mapsto u \otimes (v \otimes w) \mapsto u \otimes v \otimes w$$
$$(c) (u, v) \otimes w \mapsto (u \otimes w, v \otimes w)$$
$$(d) \lambda  \otimes u \mapsto \lambda u.$$

*Proof.* Except for $(3)$, these isomorphisms are proved using the universal mapping property of tensor products.
$(1)$ The map from $E \times  F$ to $F \otimes E$ given by $(u, v) \mapsto v \otimes u$ is clearly bilinear, thus it induces a unique linear $\alpha$ : $E \otimes F \to F \otimes E$ making the following diagram commute
$$\iota \otimes  /$$
$$E \times  FE \otimes F$$
$$L\overline{L}$$
$$\overline{L} L$$
$$LL$$
$$LL\alpha$$
$$LL$$
$$%$$
$$F \otimes E,$$
such that
$$\alpha (u \otimes v) = v \otimes u,for all u \in E and all v \in F.$$
Similarly, the map from $F \times  E$ to $E \otimes F$ given by $(v, u) \mapsto u \otimes v$ is clearly bilinear, thus it induces a unique linear $\beta$  : $F \otimes E \to E \otimes F$ making the following diagram commute
$$F \times  E^{\iota\otimes} /F \otimes E$$
$$LL$$
$$\overline{L} L$$
$$LL$$
$$LL\beta$$
$$LL$$
$$%$$
$$E \otimes F,$$
such that
$$\beta (v \otimes u) = u \otimes v,for all u \in E and all v \in F.$$
It is immediately verified that
$$(\beta  \circ \alpha )(u \otimes v) = u \otimes vand(\alpha  \circ \beta )(v \otimes u) = v \otimes u$$
for all $u \in E$ and all $v \in F$. Since the tensors of the form $u \otimes v$ span $E \otimes F$ and similarly the tensors of the form $v \otimes u$ span $F \otimes E$, the map $\beta  \circ \alpha$  is actually the identity on $E \otimes F$, and similarly $\alpha  \circ \beta$  is the identity on $F \otimes E$, so $\alpha$  and $\beta$  are isomorphisms.

<!-- PAGE 1189 -->
$(2)$ Fix some $w \in G$. The map
$$(u, v) \mapsto u \otimes v \otimes w$$
from $E \times F$ to $E \otimes F \otimes G$ is bilinear, and thus there is a linear map $f_{w}$ : $E \otimes F \to E \otimes F \otimes G$ making the following diagram commute
$$\iota \otimes  /$$
$$E \times  FE \otimes F$$
$$O\overline{O}$$
$$\overline{O} O$$
$$OO$$
$$OOf$$
$$OOw$$
$$O'$$
$$E \otimes F \otimes G,$$
with $f_{w}(u \otimes v) = u \otimes v \otimes w$. Next consider the map
$$(z, w) \mapsto f_{w}(z),$$
from $(E \otimes F) \times  G$ into $E \otimes F \otimes G$. It is easily seen to be bilinear, and thus it induces a linear map $f$ : $(E \otimes F) \otimes G \to E \otimes F \otimes G$ making the following diagram commute
$$(E \otimes F) \times  G^{\iota\otimes} /(E \otimes F) \otimes G$$
$$RR$$
$$RR$$
$$RR$$
$$RR$$
$$RRf$$
$$RR$$
$$R($$
$$E \otimes F \otimes G,$$
with f((u $\otimes v) \otimes w) = u \otimes v \otimes w$. Also consider the map
$$(u, v, w) \mapsto (u \otimes v) \otimes w$$
from $E \times F \times G$ to $(E \otimes F)\otimes G$. It is trilinear, and thus there is a linear map $g: E \otimes F \otimes G \to (E \otimes F) \otimes G$ making the following diagram commute
$$\iota \otimes  /$$
$$E \times  F \times  GE \otimes F \otimes G$$
$$QQ$$
$$QQ$$
$$QQ$$
$$QQ$$
$$QQg$$
$$QQ$$
$$Q($$
$$(E \otimes F) \otimes G,$$
with g(u $\otimes v \otimes w) = (u \otimes v) \otimes w$. Clearly, $f \circ g$ and $g \circ f$ are identity maps, and thus $f$ and $g$ are isomorphisms. The other case is similar.
$(3)$ Given a fixed vector space $G$, for any two vector spaces $M$ and $N$ and every linear map $f$ : $M \to N$, let $\tau_{G} (f) = f \otimes id_{G}$ be the unique linear map making the following diagram commute.
$$M \times  G^{\iota M\otimes} /M \otimes G$$
$$f\times idGf\otimes idG$$
$$N \times  G_{\iota N\otimes} /N \otimes G$$

<!-- PAGE 1190 -->
The identity (*) proved in Proposition 33.10 shows that if $g: N \to P$ is another linear map, then $\tau_{G} (g) \circ \tau_{G} (f) = (g \otimes id_{G}) \circ (f \otimes id_{G}) = (g \circ f) \otimes (id_{G} \circ id_{G}) = (g \circ f) \otimes id_{G} = \tau_{G} (g \circ f)$. Clearly, $\tau_{G} (0) = 0$, and a direct computation on generators also shows that
$$\tau_{G} (id_{M}) = (id_{M} \otimes id_{G}) = id_{M\otimes G},$$
and that if f': $M \to N$ is another linear map, then
$$\tau_{G} (f + f' ) = \tau_{G} (f) + \tau_{G} (f' ).$$
In fancy terms, $\tau_{G}$  is a functor. Now, if $E \oplus F$ is a direct sum, it is a standard fact of linear algebra that if $\pi_{E}$  : $E \oplus F \to E$ and $\pi_{F}$  : $E \oplus F \to F$ are the projection maps, then $\pi_{E}  \circ \pi_{E}  = \pi_{E} \pi_{F}  \circ \pi_{F}  = \pi_{F} \pi_{E}  \circ \pi_{F}  = 0 \pi_{F}  \circ \pi_{E}  = 0 \pi_{E}  + \pi_{F}  = id_{E\oplus F}$. If we apply $\tau_{G}$  to these identites, we get $\tau_{G} (\pi_{E}$ ) $\circ \tau_{G} (\pi_{E}$ ) $= \tau_{G} (\pi_{E}$ ) $\tau_{G} (\pi_{F}$ ) $\circ \tau_{G} (\pi_{F}$ ) $= \tau_{G} (\pi_{F}$ ) $\tau_{G} (\pi_{E}$ ) $\circ \tau_{G} (\pi_{F}$ ) $= 0 \tau_{G} (\pi_{F}$ ) $\circ \tau_{G} (\pi_{E}$ ) $= 0 \tau_{G} (\pi_{E}$ ) $+ \tau_{G} (\pi_{F}$ ) $= id_{(E\oplus F)\otimes G}$. Observe that $\tau_{G} (\pi_{E}$ ) $= \pi_{E}  \otimes id_{G}$ is a map from $(E \oplus F) \otimes G$ onto $E \otimes G$ and that $\tau_{G} (\pi_{F}$ ) $= \pi_{F}  \otimes id_{G}$ is a map from $(E \oplus F) \otimes G$ onto $F \otimes G$, and by linear algebra, the above equations mean that we have a direct sum
$$\otimes  \oplus  \otimes  \sim  \oplus  \otimes$$
$$(EG)(FG)= (EF)G.$$
$(4)$ We have the linear map $\epsilon$ : $E \to K \otimes E$ given by
$$\epsilon (u) = 1 \otimes u,for all u \in E.$$
The map $(\lambda , u) \mapsto \lambda u$ from $K \times  E$ to $E$ is bilinear, so it induces a unique linear map $\eta$ : $K \otimes E \to E$ making the following diagram commute
$$K \times  E^{\iota\otimes} /K \otimes E$$
$$LL$$
$$\overline{L} L$$
$$LL$$
$$LL\eta$$
$$LL$$
$$L%$$
$$E,$$
such that $\eta (\lambda  \otimes u) = \lambda u$, for all $\lambda  \in K$ and all $u \in E$. We have
$$(\eta  \circ \epsilon )(u) = \eta (1 \otimes u) = 1u = u,$$
and
$$(\epsilon  \circ \eta )(\lambda  \otimes u) = \epsilon (\lambda u) = 1 \otimes (\lambda u) = \lambda (1 \otimes u) = \lambda  \otimes u,$$
which shows that both $\epsilon  \circ \eta$  and $\eta  \circ \epsilon$  are the identity, so $\epsilon$  and $\eta$  are isomorphisms.
