# (r,s)-Tensors


<!-- PAGE 1203 -->
which is our multiplication operation in $E \otimes F$. This multiplication is determined by
$$(a \otimes b) \cdot  (c \otimes d) = (ac) \otimes (bd).$$
In summary, we have the following proposition.

> **Proposition 33.23.** Given two K-algebra $E$ and $F$, the operation on $E \otimes F$ defined on generators by
$$(a \otimes b) \cdot  (c \otimes d) = (ac) \otimes (bd)$$
makes $E \otimes F$ into a K-algebra. 33.7 $(r$, s)-Tensors In differential geometry and in physics it is necessary to consider slightly more general tensors.

> **Definition 33.14.** Given a vector space $V$ , for any pair of nonnegative integers $(r, s)$, the tensor space $T^{r,s} (V$ ) of type $(r, s)$ is the tensor product
$$T^{r,s}(V ) = V^{\otimes r}\otimes (V^{*})^{\otimes s}= V \otimes \cdots  \otimes V\otimes V^{*}\otimes \cdots  \otimes V^{*},$$
$$|{z}|{z}$$
$$rs$$
with $T^{0,0} (V$ ) $= K$. We also define the tensor algebra $T^{\bullet,\bullet} (V$ ) as the direct sum (coproduct)
$$T^{\bullet,\bullet} (V ) =MT^{r,s} (V ).$$
$$r,s\ge 0$$
Tensors in $T^{r,s} (V$ ) are called homogeneous of degree $(r, s)$. Note that tensors in $T^{r,0} (V$ ) are just our “old tensors” in $V^{\otimes r}$ . We make $T^{\bullet,\bullet} (V$ ) into an algebra by defining tensor product operations as follows.

> **Definition 33.15.** The multiplication operations
$$\otimes : T^{r1,s1} (V ) \times  T^{r2,s2} (V ) \longrightarrow T^{r1+r2,s1+s2} (V )$$
are defined such that if $u = u_{1} \otimes \cdots  \otimes u_{r1} \otimes u_{1}^{*} \otimes \cdots  \otimes u_{s1}^{*}$ and $v = v_{1} \otimes \cdots  \otimes v_{r2} \otimes v_{1}^{*} \otimes \cdots  \otimes v_{s2}^{*}$, then
$$u \otimes v = u_{1} \otimes \cdots  \otimes u_{r1} \otimes v_{1} \otimes \cdots  \otimes v_{r2} \otimes u_{1}^{*} \otimes \cdots  \otimes u_{s1}^{*} \otimes v_{1}^{*} \otimes \cdots  \otimes v_{s2}^{*}.$$
Denote by $Hom(V^{r}, (V^{*})^{s}; W)$ the vector space of all multilinear maps from $V^{r} \times  (V^{*})^{s}$ to $W$. Then we have the universal mapping property which asserts that there is a canonical isomorphism
$$\sim$$
$$Hom(T^{r,s}(V ), W)= Hom(V^{r}, (V^{*})^{s}; W).$$

<!-- PAGE 1204 -->
In particular,
$$\sim$$
$$(T^{r,s}(V ))^{*}= Hom(V^{r}, (V^{*})^{s}; K).$$
For finite dimensional vector spaces, the duality of Section 33.5 is also easily extended to the tensor spaces $T^{r,s} (V$ ). We define the pairing
$$T^{r,s} (V^{*} ) \times  T^{r,s} (V ) \longrightarrow K$$
as follows: if
$$v^{*}= v_{1}^{*} \otimes \cdots  \otimes v_{r}^{*} \otimes u_{r+1} \otimes \cdots  \otimes u_{r+s} \in T^{r,s}(V^{*} )$$
and
$$u = u_{1} \otimes \cdots  \otimes u_{r} \otimes v_{r+1}^{*} \otimes \cdots  \otimes v_{r+s}^{*} \in T^{r,s}(V ),$$
then
$$(v^{*}, u) = v_{1}^{*}(u_{1}) \cdots  v_{r+s}^{*}(u_{r+s}).$$
This is a nondegenerate pairing, and thus we get a canonical isomorphism
$$\sim$$
$$(T^{r,s}(V ))^{*}= T^{r,s}(V^{*}).$$
Consequently, we get a canonical isomorphism
$$\sim$$
$$T^{r,s}(V^{*})= Hom(V^{r}, (V^{*})^{s}; K).$$
We summarize these results in the following proposition.

> **Proposition 33.24.** Let $V$ be a vector space and let
$$T^{r,s}(V ) = V^{\otimes r}\otimes (V^{*})^{\otimes s}= V \otimes \cdots  \otimes V\otimes V^{*}\otimes \cdots  \otimes V^{*}.$$
$$|{z}|{z}$$
$$rs$$
We have the canonical isomorphisms
$$\sim$$
$$(T^{r,s}(V ))^{*}= T^{r,s}(V^{*}),$$
and
$$\sim$$
$$T^{r,s}(V^{*})= Hom(V^{r}, (V^{*})^{s}; K).$$
Proposition 33.18 specializes to the case where $E_{i} = F_{j} = V$ for $i = 1, \dots  , r$ and $j = 1, \dots  , s$, and this yields a characterization of $(r$, s)-tensors in terms of multilinear maps.

> **Proposition 33.25.** Let $V$ be a finite-dimensional vector space. We have the canonical isomorphism
$$\mu^{r,s} : T^{r,s}(V ) \to Hom((V^{*})^{r}, V^{s}; K)$$
given by
$$\mu^{r,s} (u_{1} \otimes \cdots  \otimes u_{r} \otimes v_{1}^{*} \otimes \cdots  \otimes v_{s}^{*})(x_{1}^{*}, \dots  , x_{r}^{*}, y_{1}, \dots  , y_{s}) = \prod_{i=1j}^{r}  \prod_{=1}^{s}  x_{i}^{*} (u_{i})v_{j}^{*}(y_{j}),$$
for all $u_{i} \in V, x_{i}^{*} \in V^{*} (1 \le i \le r)$, and all $y_{j} \in V, v_{j}^{*} \in V^{*} (1 \le j \le s)$. At first glance, this view of tensors as multilinear maps may appear somewhat contorted, but it is more convenient to define and manipulate tensor fields. For this reason, such a definition of tensors as multilinear maps is often used in the literature
