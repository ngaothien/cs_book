# Duality for Tensor Products


<!-- PAGE 1191 -->
Remark: The isomorphism $(3)$ can be generalized to finite and even arbitrary direct sums
$$\bigoplus_{i}  \in I E_{i} of vector spaces (where I is an arbitrary nonempty index set). We have an isomor-$$
phism
$$\otimes  \sim M \otimes$$
$$\begin{pmatrix} M \\ E_{i} \\ i\in I \end{pmatrix} G=(E_{i}G).$$
$$i\in I$$
This isomorphism (with isomorphism $(1))$ can be used to give another proof of Proposition 33.12 (see Bertin $[15]$, Chapter $4$, Section $1)$ or Lang $[113]$, Chapter XVI, Section $2)$.

> **Proposition 33.14.** Given any three vector spaces $E, F, G$, we have the canonical isomorphism
$$\sim$$
$$Hom(E, F; G)= Hom(E, Hom(F, G)).$$

*Proof.* Any bilinear map $f$ : $E \times  F \to G$ gives the linear map $\phi (f) \in$ Hom(E, Hom(F, $G))$, where $\phi$ (f)(u) is the linear map in Hom(F, $G)$ given by
$$\phi (f)(u)(v) = f(u, v).$$
Conversely, given a linear map $g \in$ Hom(E, Hom(F, $G))$, we get the bilinear map $\psi (g)$ given by
$$\psi (g)(u, v) = g(u)(v),$$
and it is clear that $\phi$  and $\psi$  and mutual inverses. Since by Proposition 33.7 there is a canonical isomorphism
$$\otimes  \sim$$
$$Hom(EF, G)= Hom(E, F; G),$$
together with the isomorphism
$$\sim$$
$$Hom(E, F; G)= Hom(E, Hom(F, G))$$
given by Proposition 33.14, we obtain the important corollary:

> **Proposition 33.15.** For any three vector spaces $E, F, G$, we have the canonical isomorphism
$$\otimes  \sim$$
$$Hom(EF, G)= Hom(E, Hom(F, G)).$$

## 33.5 Duality for Tensor Products

In this section all vector spaces are assumed to have finite dimension, unless specified otherwise. Let us now see how tensor products behave under duality. For this, we define a pairing between $E_{1}^{*} \otimes \cdots \otimes E_{n}^{*}$ and $E_{1}\otimes \cdots \otimes E_{n}$ as follows: For any fixed $(v_{1}^{*}, \dots  , v_{n}^{*}) \in E_{1}^{*} \times \cdots \times E_{n}^{*}$, we have the multilinear map
$$l_{v1*,...,vn*} : (u_{1}, \dots  , u_{n}) \mapsto v_{1}^{*}(u_{1}) \cdots  v_{n}^{*}(u_{n})$$

<!-- PAGE 1192 -->
from $E_{1} \times  \cdots  \times  E_{n}$ to $K$. The map $l_{v1*,...,vn*}$ extends uniquely to a linear map $L_{v1*,...,vn*}$ : $E_{1} \otimes \cdots  \otimes E_{n} \longrightarrow K$ making the following diagram commute.
$$E_{1} \times  \cdots  \times  E_{n}^{\iota\otimes} /E_{1} \otimes \cdots  \otimes E_{n}$$
$$SSS$$
$$SSS$$
$$SSSL$$
$$SSv*,...,v*$$
$$SSS1n$$
$$l**SS)$$
$$v1,...,vn$$
$$K$$
We also have the multilinear map
$$(v_{1}^{*}, \dots  , v_{n}^{*}) \mapsto L_{v1*,...,vn*}$$
from $E_{1}^{*} \times  \cdots  \times  E_{n}^{*}$ to $Hom(E_{1} \otimes \cdots  \otimes E_{n}, K)$, which extends to a unique linear map $L$ from $E_{1}^{*} \otimes \cdots  \otimes E_{n}^{*}$ to $Hom(E_{1} \otimes \cdots  \otimes E_{n}, K)$ making the following diagram commute.
$$\iota \otimes  /$$
$$E_{1}^{*} \times  \cdots  \times  E_{n}^{*}E_{1}^{*} \otimes \cdots  \otimes E_{n}^{*}$$
$$UU\overline{U}$$
$$UUU$$
$$UUU$$
$$UUUL$$
$$UUU$$
$$L**U*$$
$$v1,...,vn$$
$$Hom(E_{1} \otimes \cdots  \otimes E_{n}; K)$$
However, in view of the isomorphism
$$\otimes  \sim$$
$$Hom(UV, W)= Hom(U, Hom(V, W))$$
given by Proposition 33.15, with $U = E_{1}^{*} \otimes \cdots  \otimes E_{n}^{*}, V = E_{1} \otimes \cdots  \otimes E_{n}$ and $W = K$, we can view $L$ as a linear map
$$L: (E_{1}^{*} \otimes \cdots  \otimes E_{n}^{*}) \otimes (E_{1} \otimes \cdots  \otimes E_{n}) \to K,$$
which corresponds to a bilinear map
$$\langle -, -\rangle : (E_{1}^{*} \otimes \cdots  \otimes E_{n}^{*}) \times  (E_{1} \otimes \cdots  \otimes E_{n}) \longrightarrow K,(\dagger \dagger )$$
via  $\otimes \sim$ the isomorphism $(U V )^{*} =$ Hom(U, $V$ ; $K)$ given by Proposition 33.8. This pairing is given explicitly on generators by
$$\langle v_{1}^{*} \otimes \cdots  \otimes v_{n}^{*}, u_{1} \dots  , u_{n}\rangle = v_{1}^{*}(u_{1}) \cdots  v_{n}^{*}(u_{n}).$$
This pairing is nondegenerate, as proved below.

*Proof.* If $(e_{1}^{1}, \dots  , e_{m1}^{1}), \dots  , (e_{1}^{n}, \dots  , e_{mn}^{n})$ are bases for $E_{1}, \dots  , E_{n}$, then for every basis element $(e_{i}^{1} )^{*} \otimes \cdots  \otimes (e_{in}^{n})^{*}$ of $E_{1}^{*} \otimes \cdots  \otimes E_{n}^{*}$, and any basis element $e_{j1}^{1} \otimes \cdots  \otimes e_{jn}^{n}$ of $E_{1} \otimes \cdots  \otimes E_{n}, we^{1}$ have
$$\langle (e_{i1}^{1})^{*}\otimes \cdots  \otimes (e_{in}^{n})^{*}, e_{j1}^{1} \otimes \cdots  \otimes e_{jn}^{n}\rangle = \delta_{i1j1}  \cdots  \delta_{injn} ,$$
where $\delta_{i j}$  is Kronecker delta, defined such that $\delta_{i j}  = 1$ if $i = j$, and $0$ otherwise. Given any $\alpha  \in E_{1}^{*} \otimes \cdots  \otimes E_{n}^{*}$, assume that $\langle \alpha , \beta \rangle = 0$ for all $\beta  \in E_{1} \otimes \cdots  \otimes E_{n}$. The vector $\alpha$  is a finite

<!-- PAGE 1193 -->
$$linear combination \alpha  = \sum_{nin}  \lambda_{i1,...,in} (e_{i1}^{1})^{*}\otimes \cdots  \otimes (e_{in}^{n})^{*}, for some unique \lambda_{i1,...,in}  \in K. If we$$
choose $\beta  = e_{i1}^{1} \otimes \cdots  \otimes e$ , then we get
$$0 = \langle \alpha , e_{i1}^{1} \otimes \cdots  \otimes e_{in}^{n}\rangle = \bigoplus  \sum  \lambda_{i1,...,in} (e_{i1}^{1})^{*}\otimes \cdots  \otimes (e_{in}^{n})^{*}, e_{i1}^{1} \otimes \cdots  \otimes e_{in}^{n}E$$
$$= \sum  \lambda_{i1,...,in} \langle (e_{i1}^{1})^{*}\otimes \cdots  \otimes (e_{in}^{n})^{*}, e_{i1}^{1} \otimes \cdots  \otimes e_{in}^{n}\rangle$$
$$= \lambda_{i1,...,in} .$$
Therefore, $\alpha  = 0$, Conversely, given any $\beta  \in E_{1}\otimes \cdots \otimes E_{n}$, assume that $\langle \alpha , \beta \rangle = 0$, for all $\alpha  \in E_{1}^{*} \otimes \cdots \otimes E_{n}^{*}$.
$$The vector \beta  is a finite linear combination \beta  = \sum_{*}  \lambda_{i1,...,in} e_{i1}^{1} \otimes \cdots  \otimes e_{in}^{n}, for some unique$$
$\lambda_{i1,...,in}  \in K$. If we choose $\alpha  = (e_{i1}^{1})^{*} \otimes \cdots  \otimes (e_{in}^{n})$ , then we get
$$0 = \langle (e_{i1}^{1})^{*}\otimes \cdots  \otimes (e_{in}^{n})^{*}, \beta \rangle = \bigoplus  (e_{1}^{1})^{*}\otimes \cdots  \otimes (e_{in}^{n})^{*}, \sum  \lambda_{i1,...,in} e_{i1}^{1} \otimes \cdots  \otimes e_{in}^{n}E$$
$$= \sum^{i}  \lambda_{i1,...,in} \langle (e_{i1}^{1})^{*}\otimes \cdots  \otimes (e_{in}^{n})^{*}, e_{i1}^{1} \otimes \cdots  \otimes e_{in}^{n}\rangle$$
$$= \lambda_{i1,...,in} .$$
Therefore, $\beta  = 0$. By Proposition $33.1,^{1}$ we have a canonical isomorphism
$$\otimes \cdots  \otimes \sim  \otimes \cdots  \otimes$$
$$(E_{1}E_{n})^{*}= E_{1}^{*}E_{n}^{*}.$$
Here is our main proposition about duality of tensor products.

> **Proposition 33.16.** We have canonical isomorphisms
$$\otimes \cdots  \otimes \sim  \otimes \cdots  \otimes$$
$$(E_{1}E_{n})^{*}= E_{1}^{*}E_{n}^{*},$$
and
$$\otimes \cdots  \otimes  \sim$$
$$\mu : E_{1}^{*}E_{n}^{*}= Hom(E_{1}, \dots  , E_{n}; K).$$

*Proof.* $\otimes \cdots \otimes \sim \otimes \cdots \otimes$ The second isomorphism follows from the isomorphism $(E_{1} E_{n})^{*} = E_{1}^{*} E_{n}^{*}$
$$\sim  \otimes \cdots \otimes$$
together with the isomorphism $Hom(E_{1}, \dots  , E_{n}; K) = (E_{1} E_{n})^{*}$ given by Proposition 33.8.
$$\otimes \cdots  \otimes  \sim$$
The isomorphism $\mu$ : $E_{1}^{*} E_{n}^{*} = Hom(E_{1}, \dots  , E_{n}; K)$ can be described explicitly as the linear extension to $E_{1}^{*} \otimes \cdots  \otimes E_{n}^{*}$ of the map given by
$$\mu (v_{1}^{*} \otimes \cdots  \otimes v_{n}^{*})(u_{1} \dots  , u_{n}) = v_{1}^{*}(u_{1}) \cdots  v_{n}^{*}(u_{n}).$$
$\overline{1}\overline{This} \overline{is} \overline{where} \overline{the} \overline{assumption} \overline{that} \overline{our}$ spaces are finite dimensional is used.

<!-- PAGE 1194 -->
Since our spaces are all finite-dimensional, each space $E_{i}$ is canonically isomorphic to $E_{i}^{**}$ , where the isomorphism $u \mapsto eval_{u}$ is defined by Equation (eval) in Section 33.1, namely
$$eval_{u}(\omega ) = \omega (u),\omega  \in E_{i}^{*} , u \in E_{i}.$$
By replacing each $E_{i}$ by its dual $E_{i}^{*}$ , we obtain an isomorphism
$$\otimes \cdots  \otimes  \sim$$
$$\mu^{*} : E_{1}^{**}E_{n}^{**}= Hom(E_{1}^{*}, \dots  , E_{n}^{*}; K),$$
$$\sim$$
and using the isomorphisms $E_{i} = E_{i}^{**}$ we also obtain an isomorphism
$$\otimes \cdots  \otimes  \sim$$
$$E_{1}E_{n}= Hom(E_{1}^{*}, \dots  , E_{n}^{*}; K).$$
The above isomorphism can be defined explicitly. Indeed, using the same symbol $\mu^{*}$ with a slight abuse of notation, we define the map
$$\mu^{*} : E_{1} \otimes \cdots  \otimes E_{n} \to Hom(E_{1}^{*}, \dots  , E_{n}^{*}; K)$$
given by
$$\mu^{*} (u_{1} \otimes \cdots  \otimes u_{n})(v_{1}^{*}, \dots  , v_{n}^{*}) = \mu^{*} (eval_{u1} \otimes \cdots  \otimes eval_{un})(v_{1}^{*}, \dots  , v_{n}^{*})$$
$$= eval_{u1}(v_{1}^{*}) \cdots  eval_{un}(v_{n}^{*})$$
$$= v_{1}^{*}(u_{1}) \cdots  v_{n}^{*}(u_{n}),$$
for all $u_{i} \in E_{i}$ and all $v_{i}^{*} \in E_{i}^{*} , 1 \le i \le n$. Consequently, we have an explicit definition of the isomorphism
$$\mu^{*} : E_{1} \otimes \cdots  \otimes E_{n} \to Hom(E_{1}^{*}, \dots  , E_{n}^{*}; K)$$
given by
$$\mu^{*} (u_{1} \otimes \cdots  \otimes u_{n})(v_{1}^{*}, \dots  , v_{n}^{*}) = v_{1}^{*}(u_{1}) \cdots  v_{n}^{*}(u_{n}),$$
for all $u_{i} \in E_{i}$ and all $v_{i}^{*} \in E_{i}^{*} , 1 \le i \le n$. Observe the “duality” with the definition of the isomorphism $\mu$ : $E_{1}^{*}\otimes \cdots \otimes E_{n}^{*} \to Hom(E_{1}, \dots  , E_{n}; K)$ given by
$$\mu (v_{1}^{*} \otimes \cdots  \otimes v_{n}^{*})(u_{1}, \dots  , u_{n}) = v_{1}^{*}(u_{1}) \cdots  v_{n}^{*}(u_{n}).$$
We record the above results in the following proposition.

> **Proposition 33.17.** We have the canonical isomorphism
$$\mu^{*} : E_{1} \otimes \cdots  \otimes E_{n} \to Hom(E_{1}^{*}, \dots  , E_{n}^{*}; K)$$
given by
$$\mu^{*} (u_{1} \otimes \cdots  \otimes u_{n})(v_{1}^{*}, \dots  , v_{n}^{*}) = v_{1}^{*}(u_{1}) \cdots  v_{n}^{*}(u_{n}),$$
and the canonical isomorphism $\mu$ : $E_{1}^{*} \otimes \cdots  \otimes E_{n}^{*} \to Hom(E_{1}, \dots  , E_{n}; K)$ given by
$$\mu (v_{1}^{*} \otimes \cdots  \otimes v_{n}^{*})(u_{1}, \dots  , u_{n}) = v_{1}^{*}(u_{1}) \cdots  v_{n}^{*}(u_{n}),$$
for all $u_{i} \in E_{i}$ and all $v_{i}^{*} \in E_{i}^{*} , 1 \le i \le n$.

<!-- PAGE 1195 -->
The above isomorphisms are used by some authors to define tensor products of finite-dimensional vector spaces, for example, Dieudonn´e $[51]$, O’Neill $[137]$ and Sakai $[147]$. They have the advantage of circumventing the quotient construction of the tensor product. The above isomorphisms are easily generalized to “mixed” tensor products
$$E_{1} \otimes \cdots  \otimes E_{r} \otimes F_{1}^{*}  \otimes \cdots  \otimes F_{s}^{*}$$
and
$$E_{1}^{*} \otimes \cdots  \otimes E_{r}^{*} \otimes F_{1} \otimes \cdots  \otimes F_{s}$$
of finite-dimensional vector spaces $E_{1}, \dots  , E_{r}$ and $F_{1}, \dots  , F_{s}$, with $r, s \ge 0$. The proof of the following proposition is left as an exercise.

> **Proposition 33.18.** We have the canonical isomorphism
$$rs$$
$$\mu^{*} :OE_{i} \otimes OF_{j}^{*}  \to Hom \begin{pmatrix} E_{1}^{*}\times & F_{j}; K \end{pmatrix} \prod_{i=1}^{r}  \prod_{j=1}^{s}$$
$$i=1j=1$$
given by
$$\mu^{*} (u_{1} \otimes \cdots  \otimes u_{r} \otimes v_{1}^{*} \otimes \cdots  \otimes v_{s}^{*})(x_{1}^{*}, \dots  , x_{r}^{*}, y_{1}, \dots  , y_{s}) = \prod_{i=1j}^{r}  \prod_{=1}^{s}  x_{i}^{*} (u_{i})v_{j}^{*}(y_{j}),$$
and the canonical isomorphism
$$rs$$
$$\mu :OE_{i}^{*} \otimes OF_{j} \to Hom \begin{pmatrix} E_{1} \times & F_{j}^{*}; K \end{pmatrix} \prod_{i=1}^{r}  \prod_{j=1}^{s}$$
$$i=1j=1$$
given by
$$\mu (x_{1}^{*} \otimes \cdots  \otimes x_{r}^{*} \otimes y_{1} \otimes \cdots  \otimes y_{s})(u_{1}, \dots  , u_{r}, v_{1}^{*}, \dots  , v_{s}^{*}) = \prod_{i=1j}^{r}  \prod_{=1}^{s}  x_{i}^{*} (u_{i})v_{j}^{*}(y_{j}),$$
for all $u_{i} \in E_{i}, x_{i}^{*} \in E_{i}^{*} (1 \le i \le r), v_{j}^{*} \in F_{j}^{*} , y_{j} \in F_{j} (1 \le j \le s)$.
Remark: The canonical isomorphisms of Proposition 33.16 holds under more general conditions. Namely, that $K$ is a commutative ring with identity and that the $E_{i}$ are finitelygenerated projective K-modules (see Definition 35.7). See Bourbaki, $[25]$ (Chapter III, §11, Section $5$, Proposition $7)$. In the special case where $i = j = 1$, we have a canonical isomorphism between $E^{*} \otimes F$ and Hom(E $\times  F^{*}$ ; $K)$. There is also a canonical isomorphism $\beta$  between Hom(E $\times  F^{*}$ ; $K)$ and Hom(E, $F^{**}$ ), namely for any $f \in$ Hom(E $\times  F^{*}$ ; $K)$, for any $u \in E, \beta (f)$ is the linear map from $E$ to $F^{**}$ given by
$$[\beta (f)(u)](v^{*}) = f(u, v^{*}),v^{*}\in F^{*} .$$

<!-- PAGE 1196 -->
$$\sim$$
Since there is a canonical isomorphism $F = F^{**}$, we also obtain canonical isomorphisms
$$\otimes  \sim  \times   \sim   \sim$$
$$E^{*}F= Hom(E F^{*}; K)= Hom(E, F^{**})= Hom(E, F).$$
$$\otimes  \sim$$
The method for deriving the isomorphism $E^{*} F =$ Hom(E, $F)$ uses the canonical
$$\sim$$
isomorphism $F = F^{**}$, which is slightly indirect and actually unnecessary, as we now explain. Let $E$ and $F$ be two vector spaces and let $\alpha$ : $E^{*} \times  F \to$ Hom(E, $F)$ be the map defined such that
$$\alpha (u^{*}, f)(x) = u^{*}(x)f,$$
for all $u^{*} \in E^{*}, f \in F$, and $x \in E$. This map is clearly bilinear, and thus it induces a linear map $\alpha_{\otimes}$ : $E^{*} \otimes F \to$ Hom(E, $F)$ making the following diagram commute
$$\iota \otimes  /$$
$$E^{*}\times  FE^{*}\otimes F$$
$$O\overline{O}$$
$$\overline{O} O$$
$$OO$$
$$OO\alpha$$
$$\alpha OO\otimes$$
$$O'$$
$$Hom(E, F),$$
such that
$$\alpha_{\otimes} (u^{*}\otimes f)(x) = u^{*}(x)f.$$

> **Proposition 33.19.** If $E$ and $F$ are vector spaces (not necessarily finite dimensional), then the following properties hold:
$(1)$ The linear map $\alpha_{\otimes}$ : $E^{*} \otimes F \to$ Hom(E, $F)$ is injective.
$(2)$ If $E$ is finite dimensional, then $\alpha_{\otimes}$ : $E^{*}\otimes F \to$ Hom(E, $F)$ is a canonical isomorphism.
$(3)$ If $F$ is finite dimensional, then $\alpha_{\otimes}$ : $E^{*}\otimes F \to$ Hom(E, $F)$ is a canonical isomorphism.

*Proof.* $(1)$ Let $(e_{i}^{*} )_{i\in I}$ be a basis of $E^{*}$ and let $(f_{j})_{j\in J}$ be a basis of $F$. Then we know that $(e_{i}^{*} \otimes f_{j})_{i\in I,j\in J}$ is a basis of $E^{*} \otimes F$. To prove that $\alpha_{\otimes}$ is injective, let us show that its kernel is reduced to $(0)$. For any vector
$$\omega  = \sum_{\in I',j\in J}  \lambda_{ij}  e_{i}^{*} \otimes f_{j}$$
$$i'$$
in $E^{*} \otimes F$, with I' and J' some finite sets, assume that $\alpha_{\otimes} (\omega$ ) $= 0$. This means that for every $x \in E$, we have $\alpha_{\otimes} (\omega )(x) = 0$; that is,
$$\sum_{\in I',j\in J}  \alpha_{\otimes} (\lambda_{ij}  e_{i}^{*} \otimes f_{j})(x) = \sum_{j\in J'}  \begin{pmatrix} \lambda_{ij} e_{i}^{*}(x) \end{pmatrix} \sum_{i\in I'}  f_{j} = 0.$$
$$i'$$

<!-- PAGE 1197 -->
Since $(f_{j})_{j\in J}$ is a basis of $F$, for every $j \in$ J', we must have
$$\sum_{i\in I'}  \lambda_{ij} e_{i}^{*} (x) = 0,for all x \in E.$$
But then $(e_{i}^{*} )_{i\in I'}$ would be linearly dependent, contradicting the fact that $(e_{i}^{*} )_{i\in I}$ is a basis of $E^{*}$, so we must have
$$\lambda_{ij}  = 0,for all i \in I'and all j \in J',$$
which shows that $\omega  = 0$. Therefore, $\alpha_{\otimes}$ is injective.
$(2)$ Let $(e_{j})_{1\le j\le n}$ be a finite basis of $E$, and as usual, let $e_{j}^{*} \in E^{*}$ be the linear form defined by
$$e_{j}^{*}(e_{k}) = \delta_{j,k} ,$$
where $\delta_{j,k}  = 1$ iff $j = k$ and $0$ otherwise. We know that $(e_{j}^{*})_{1\le j\le n}$ is a basis of $E^{*}$ (this is where we use the finite dimension of $E)$. For any linear map $f \in$ Hom(E, $F)$, for every $x = x_{1}e_{1} + \cdots  + x_{n}e_{n} \in E$, we have f(x) $= f(x_{1}e_{1} + \cdots  + x_{n}e_{n}) = x_{1}f(e_{1}) + \cdots  + x_{n}f(e_{n}) = e_{1}^{*}(x)f(e_{1}) + \cdots  + e_{n}^{*}(x)f(e_{n})$. Consequently, every linear map $f \in$ Hom(E, $F)$ can be expressed as
$$f(x) = e_{1}^{*}(x)f_{1} + \cdots  + e_{n}^{*}(x)f_{n},$$
for some $f_{i} \in F$. Furthermore, if we apply $f$ to $e_{i}$, we get $f(e_{i}) = f_{i}$, so the $f_{i}$ are unique. Observe that
$$(\alpha_{\otimes} (e_{1}^{*} \otimes f_{1} + \cdots  + e_{n}^{*} \otimes f_{n}))(x) = \sum_{i=1}^{n}  (\alpha_{\otimes} (e_{i}^{*} \otimes f_{i}))(x) = \sum_{i=1}^{n}  e_{i}^{*} (x)f_{i}.$$
Thus, $\alpha_{\otimes}$ is surjective, so $\alpha_{\otimes}$ is a bijection.
$(3)$ Let $(f_{1}, \dots  , f_{m})$ be a finite basis of $F$, and let $(f_{1}^{*} , \dots  , f_{m}^{*})$ be its dual basis. Given any linear map $h: E \to F$, for all $u \in E$, since $f_{i}^{*}  (f_{j}) = \delta_{ij}$ , we have
$$h(u) = \sum_{i=1}^{m}  f_{i}^{*}  (h(u))f_{i}.$$
If
$$h(u) = \sum_{j=1}^{m}  v_{j}^{*}(u)f_{j}for all u \in E(*)$$
for some linear forms $(v_{1}^{*}, \dots  , v_{m}^{*}) \in (E^{*})^{m}$, then
$$f_{i}^{*}  (h(u)) = \sum_{j=1}^{m}  v_{j}^{*}(u)f_{i}^{*} (f_{j}) = v_{i}^{*} (u)for all u \in E,$$

<!-- PAGE 1198 -->
which shows that $v_{i}^{*} = f_{i}^{*} \circ h$ for $i = 1, \dots  , m$. This means that $h$ has a unique expression in terms of linear forms as in (*). Define the map $\alpha$  from $(E^{*})^{m}$ to Hom(E, $F)$ by
$$\alpha (v_{1}^{*}, \dots  , v_{m}^{*})(u) = \sum_{j=1}^{m}  v_{j}^{*}(u)f_{j}for all u \in E.$$
This map is linear. For any $h \in$ Hom(E, $F)$, we showed earlier that the expression of $h$ in (*) is unique, thus $\alpha$  is an isomorphism. Similarly, $E^{*} \otimes F$ is isomorphic to $(E^{*})^{m}$. Any tensor $\omega  \in E^{*} \otimes F$ can be written as a linear combination
$$\sum_{k=1}^{p}  u_{k}^{*} \otimes y_{k}$$
for some $u_{k}^{*} \in E^{*}$ and some $y_{k} \in F$, and since $(f_{1}, \dots  , f_{m})$ is a basis of $F$, each $y_{k}$ can be written as a linear combination of $(f_{1}, \dots  , f_{m})$, so $\omega$  can be expressed as
$$\omega  = \sum_{i=1}^{m}  v_{i}^{*} \otimes f_{i},(\dagger )$$
for some linear forms $v_{i}^{*} \in E^{*}$ which are linear combinations of the $u_{k}^{*}$. If we pick a basis $(w_{i}^{*} )_{i\in I}$ for $E^{*}$, then we know that the family $(w_{i}^{*} \otimes f_{j})_{i\in I,1\le j\le m}$ is a basis of $E^{*} \otimes F$, and this implies that the $v_{i}^{*}$ in $(\dagger$ ) are unique. Define the linear map $\beta$  from $(E^{*})^{m}$ to $E^{*} \otimes F$ by
$$\beta (v_{1}^{*}, \dots  , v_{m}^{*}) = \sum_{i=1}^{m}  v_{i}^{*} \otimes f_{i}.$$
Since every tensor $\omega  \in E^{*} \otimes F$ can be written in a unique way as in $(\dagger$ ), this map is an isomorphism. Note that in Proposition 33.19, we have an isomorphism if either $E$ or $F$ has finite dimension. The following proposition allows us to view a multilinear map as a tensor product.

> **Proposition 33.20.** If the spaces $E_{1}, \dots  E_{n}$ are finite dimensional vector spaces and $F$ is any vector space, then we have the canonical isomorphism
$$\sim  \otimes \cdots  \otimes  \otimes$$
$$Hom(E_{1}, \dots  , E_{n}; F)= E_{1}^{*}E_{n}^{*}F.$$

*Proof.* In view of the canonical isomorphism
$$\sim  \otimes \cdots  \otimes$$
$$Hom(E_{1}, \dots  , E_{n}; F)= Hom(E_{1}E_{n}, F)$$
$$\otimes \cdots  \otimes \sim  \otimes \cdots  \otimes$$
given by Proposition 33.7 and the canonical isomorphism $(E_{1} E_{n})^{*} = E_{1}^{*} E_{n}^{*}$ given by Proposition 33.16, if the $E_{i}’s$ are finite dimensional, then Proposition 33.19 yields the canonical isomorphism
$$\sim  \otimes \cdots  \otimes  \otimes$$
$$Hom(E_{1}, \dots  , E_{n}; F)= E_{1}^{*}E_{n}^{*}F,$$
as claimed.
