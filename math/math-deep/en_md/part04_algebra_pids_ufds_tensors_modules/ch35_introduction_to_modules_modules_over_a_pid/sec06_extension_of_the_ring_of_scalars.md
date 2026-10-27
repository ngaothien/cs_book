# Extension of the Ring of Scalars


<!-- PAGE 1313 -->
sum of two nonzero proper submodules of $M$. For a proof, see Bourbaki $[26]$ (Chapter VII, Section $4$, No. $8$, Proposition $8)$. Theorem 35.38 shows that a finitely generated module over a PID is a direct sum of indecomposable modules. In Chapter $36$ we apply the structure theorems for finitely generated (torsion) modules to the K[X]-module $E_{f}$ associated with an endomorphism $f$ on a vector space $E$. First, we need to understand the process of extension of the ring of scalars.

## 35.6 Extension of the Ring of Scalars

The need to extend the ring of scalars arises, in particular when dealing with eigenvalues. First we need to define how to restrict scalar multiplication to a subring. The situation is that we have two rings $A$ and $B$, a B-module $M$, and a ring homomorphism $\rho$ : $A \to B$. The special case that arises often is that $A$ is a subring of $B (B$ could be a field) and $\rho$  is the inclusion map. Then we can make $M$ into an A-module by defining the scalar multiplication $\cdot$ : $A \times  M \to M$ as follows.

> **Definition 35.14.** Given two rings $A$ and $B$ and a ring homomorphism $\rho$ : $A \to B$, any B- module $M$ can made into an A-module denoted by $\rho_{*} (M)$, by defining scalar multiplication by any element of $A$ as follows:
$$a \cdot  x = \rho (a)x,for all a \in A and all x \in M.$$
In particular, viewing $B$ as a B-module, we obtain the A-module $\rho_{*} (B)$. If $M$ and $N$ are two B-modules and if $f$ : $M \to N$ is a $B$-linear map, the map $f$ is a homomorphism $f$ : $\rho_{*} (M) \to \rho_{*} (N)$ of the abelian groups $\rho_{*} (M)$ and $\rho_{*} (N)$. This map is also $A$-linear, because for all $u \in M$ and all $a \in A$, by definition of the scalar multiplication by elements of $A$, we have
$$f(a \cdot  u) = f(\rho (a)u) = \rho (a)f(u) = a \cdot  f(u).$$
The map $f$ : $\rho_{*} (M) \to \rho_{*} (N)$ viewed as an $A$-linear map is denoted by $\rho_{*} (f)$. As homomorphisms of abelian groups, the maps $f$ : $M \to N$ and $\rho_{*} (f): \rho_{*} (M) \to \rho_{*} (N)$ are identical, but $f$ is a $B$-linear map whereas $\rho_{*} (f)$ is an $A$-linear map. Now we can describe the process of scalar extension. Given any A-module $M$, we make $\rho_{*} (B) \otimes_{A}  M$ into a (left) B-module as follows: for every $\beta  \in B$, let $\mu_{\beta}$  : $\rho_{*} (B) \times  M \to \rho_{*} (B) \otimes_{A}  M$ be given by
$$\mu_{\beta} (\beta' , x) = (\beta \beta' ) \otimes x.$$
The map $\mu_{\beta}$  is bilinear so it induces a linear map $\mu_{\beta}$  : $\rho_{*} (B) \otimes_{A}  M \to \rho_{*} (B) \otimes_{A}  M$ such that
$$\mu_{\beta} (\beta' \otimes x) = (\beta \beta' ) \otimes x.$$

<!-- PAGE 1314 -->
If we define the scalar multiplication $\cdot$ : $B \times  (\rho_{*} (B) \otimes_{A}  M) \to \rho_{*} (B) \otimes_{A}  M$ by
$$\beta  \cdot  z = \mu_{\beta} (z),for all \beta  \in B and all z \in \rho_{*} (B) \otimes_{A}  M,$$
then it is easy to check that the axioms M1, M2, M3, M4 hold. Let us check M2 and M3. We have
$$\mu_{\beta1+\beta2} (\beta' \otimes x) = (\beta_{1}  + \beta_{2} )\beta' \otimes x$$
$$= (\beta_{1} \beta' + \beta_{2} \beta' ) \otimes x$$
$$= \beta_{1} \beta' \otimes x + \beta_{2} \beta' \otimes x$$
$$= \mu_{\beta1} (\beta' \otimes x) + \mu_{\beta2} (\beta' \otimes x)$$
and
$$\mu_{\beta1\beta2} (\beta' \otimes x) = \beta_{1} \beta_{2} \beta' \otimes x$$
$$= \mu_{\beta1} (\beta_{2} \beta' \otimes x)$$
$$= \mu_{\beta1} (\mu_{\beta2} (\beta' \otimes x)).$$

> **Definition 35.15.** Given two rings $A$ and $B$ and a ring homomorphism $\rho$ : $A \to B$, for any A-module $M$, with the scalar multiplication by elements of $B$ given by
$$\beta  \cdot  (\beta' \otimes x) = (\beta \beta' ) \otimes x,\beta , \beta' \in B, x \in M,$$
the tensor product $\rho_{*} (B) \otimes_{A}  M$ is a B-module denoted by $\rho^{*} (M)$, or $M_{(B)}$ when $\rho$  is the inclusion of $A$ into $B$. The B-module $\rho^{*} (M)$ is sometimes called the module induced from $M$ by extension to $B$ of the ring of scalars through $\rho$ . Here is a specific example of Definition 35.15. Let $A =\mathbb{R}, B =\mathbb{C}$ and $\rho$  be the inclusion map of $\mathbb{R}$ into $\mathbb{C}$, i.e. $\rho$ : $\mathbb{R} \to \mathbb{C}$ with $\rho (a) = a$ for $a \in \mathbb{R}$. Let $M$ be an $\mathbb{R}-module$. The field $\mathbb{C}$ is $a \mathbb{C}-module$, and when we restrict scalar multiplication by scalars $\lambda  \in \mathbb{R}$, we obtain the $\mathbb{R}-module \rho_{*} (\mathbb{C})$ (which, as an abelian group, is just $\mathbb{C})$. Form $\rho_{*} (\mathbb{C}) \otimes_{R}  M$. This is
$$an \mathbb{R}-module where typical elements have the form \sum_{i}  n=1 a_{i}(z_{i} \otimes m_{i}), a_{i} \in \mathbb{R}, z_{i} \in \mathbb{C}, and$$
$m_{i} \in M$. Since
$$a_{i}(z_{i} \otimes m_{i}) = a_{i}z_{i} \otimes m_{i}$$
and since $a_{i}z_{i} \in \mathbb{C}$ and any element of $\mathbb{C}$ is obtained this way (let $a_{i} = 1)$, the elements of $\rho_{*} (\mathbb{C}) \otimes_{R}  M$ can be written as
$$\sum_{i=1}^{n}  z_{i} \otimes m_{i},z_{i} \in \mathbb{C}, m_{i} \in M.$$
We want to make $\rho_{*} (\mathbb{C}) \otimes_{R}  M$ into $a \mathbb{C}-module$, denoted $\rho^{*} (M)$, and thus must describe
$$how a complex number \beta  acts on \sum_{i}  n z_{i} \otimes m_{i}. By linearity, it is enough to determine how$$
$\beta  = u +$ iv acts on a generator $z \otimes m^{=1}$, where $z = x +$ iy and $m \in M$. The action is given by
$$\beta  \cdot  (z \otimes m) = \beta z \otimes m = (u + iv)(x + iy) \otimes m = (ux -vy + i(uy + vx)) \otimes m,$$

<!-- PAGE 1315 -->
since complex multiplication only makes sense over $\mathbb{C}$. We claim that $\rho^{*} (M)$ is isomorphic to the $\mathbb{C}-module M \times  M$ with addition defined by
$$(u_{1}, v_{1}) + (u_{2}, v_{2}) = (u_{1} + u_{2}, v_{1} + v_{2})$$
and scalar multiplication by $\lambda  + i\mu  \in \mathbb{C}$ as
$$(\lambda  + i\mu ) \cdot  (u, v) = (\lambda u -\mu v, \lambda v + \mu u).$$
Define the map $\alpha_{0}$  : $\rho_{*} (\mathbb{C}) \times  M \to M \times  M$ by
$$\alpha_{0} (\lambda  + i\mu , u) = (\lambda u, \mu u).$$
It is easy to check that $\alpha_{0}  is\mathbb{R}-linear$, so we obtain $an\mathbb{R}-linear$ map $\alpha$ : $\rho_{*} (\mathbb{C})\otimes_{R} M \to M \times M$ such that
$$\alpha ((\lambda  + i\mu ) \otimes u) = (\lambda u, \mu u).$$
We also define the map $\beta$  : $M \times  M \to \rho_{*} (\mathbb{C}) \otimes_{R}  M$ by
$$\beta (u, v) = 1 \otimes u + i \otimes v.$$
Again, it is clear that this map is $\mathbb{R}-linear$. We can now check that $\alpha$  and $\beta$  are mutual inverses. We have
$$\alpha (\beta (u, v)) = \alpha (1 \otimes u + i \otimes v) = \alpha (1 \otimes u) + \alpha (i \otimes v) = (u, 0) + (0, v) = (u, v),$$
and on generators, $\beta (\alpha ((\lambda  + i\mu$ ) $\otimes u)) = \beta (\lambda u, \mu u) = 1 \otimes \lambda u + i \otimes \mu u = \lambda  \otimes u + i\mu  \otimes u = (\lambda  + i\mu$ ) $\otimes u$. Therefore, $\rho_{*} (\mathbb{C}) \otimes_{R}  M$ and $M \times  M$ are isomorphic $as\mathbb{R}-module$. However, the isomorphism $\alpha$  is also an isomorphism of $\mathbb{C}-modules$. This is because in $\rho_{*} (\mathbb{C}) \otimes_{R}  M$, on generators we have
$$(\lambda  + i\mu ) \cdot  ((x + iy) \otimes u) = (\lambda  + i\mu )(x + iy) \otimes u = (\lambda x -\mu y + i(\lambda y + \mu x)) \otimes u,$$
so
$$\alpha ((\lambda  + i\mu ) \cdot  ((x + iy) \otimes u) = \alpha ((\lambda x -\mu y + i(\lambda y + \mu x)) \otimes u)$$
$$= ((\lambda x -\mu y)u, (\lambda y + \mu x)u),$$
and by definition of the scalar multiplication by elements of $\mathbb{C}$ on $M \times  M$
$$(\lambda  + i\mu ) \cdot  \alpha ((x + iy) \otimes u) = (\lambda  + i\mu ) \cdot  (xu, yu) = ((\lambda x -\mu y)u, (\lambda y + \mu x)u).$$
Therefore, $\alpha$  is an isomorphism between the $\mathbb{C}-modules \rho^{*} (M) = \rho_{*} (\mathbb{C}) \otimes_{R}  M$ and $M \times  M$. The above process of ring extension can also be applied to linear maps. We have the following proposition whose proof is given in Bourbaki $[25]$ (Chapter II, Section $5$, Proposition $1)$.

<!-- PAGE 1316 -->

> **Proposition 35.39.** Given a ring homomomorphism $\rho$ : $A \to B$ and given any A-module $M$, the map $\phi$ : $M \to \rho_{*} (\rho^{*} (M))$ given by $\phi (x) = 1 \otimes_{A}  x$ is $A$-linear and $\phi (M)$ spans the B-module $\rho^{*} (M)$. For every B-module $N$, and for every $A$-linear map $f$ : $M \to \rho_{*} (N)$, there is a unique $B$-linear map
$$\overline{f}\overline{:} \rho^{*} (M) \to N$$
such that
$$\rho_{*} (\overline{f}) \circ \phi  = f$$
as in the following commutative diagram
$$M\rho_{*} (\rho^{*} (M))$$
$$\overline{J}^{\phi}\overline{J}$$
$$\overline{J} J$$
$$JJ$$
$$JJ\rho (\overline{f})$$
$$fJJ*$$
$$$$$
$$\rho_{*} (N)$$
or equivalently,
$$\overline{f}(1 \otimes_{A}  x) = f(x),for all x \in M.$$
As a consequence of Proposition 35.39, we obtain the following result.

> **Proposition 35.40.** Given a ring homomomorphism $\rho$ : $A \to B$, for any two A-modules $M$
$$and N, for every A \frac{-linear}{f} map f : M \to N, there is a unique B-linear map \rho^{*} (f): \rho^{*} (M) \to$$
$\rho^{*} (N)$ (also denoted ) given by
$$\rho^{*} (f) = id_{B} \otimes f,$$
such that the following diagam commutes:
$$M^{\phi M}\rho_{*} (\rho^{*} (M))$$
$$f\rho (\rho *(f))$$
$$*$$
$$N_{\phi N}  /\rho_{*} (\rho^{*} (N))$$

*Proof.* Apply Proposition 35.40 to the $A$-linear map $\phi_{N}  \circ f$. If $S$ spans the module $M$, it is clear that $\phi (S)$ spans $\rho^{*} (M)$. In particular, if $M$ is finitely generated, so if $\rho^{*} (M)$. Bases of $M$ also extend to bases of $\rho^{*} (M)$.

> **Proposition 35.41.** Given a ring homomomorphism $\rho$ : $A \to B$, for any A-module $M$, if $(u_{1}, \dots  , u_{n})$ is a basis of $M$, then $(\phi (u_{1}), \dots  , \phi (u_{n}))$ is a basis of $\rho^{*} (M)$, where $\phi$  is the $A$-linear map $\phi$ : $M \to \rho_{*} (\rho^{*} (M))$ given by $\phi (x) = 1 \otimes_{A}  x$. Furthermore, if $\rho$  is injective, then so is $\phi$ .

*Proof.* The first assertion follows immediately from Proposition 35.13, since it asserts that every element $z$ of $\rho^{*} (M) = \rho_{*} (B) \otimes_{A}  M$ can be written in a unique way as
$$z = b_{1} \otimes u_{1} + \cdots  + b_{n} \otimes u_{n} = b_{1}(1 \otimes u_{1}) + \cdots  + b_{n}(1 \otimes u_{n}),$$

<!-- PAGE 1317 -->
and $\phi (u_{i}) = 1 \otimes u_{i}$. Next, if $\rho$  is injective, by definition of the scalar multiplication in the A-module $\rho_{*} (\rho^{*} (M))$, we have $\phi (a_{1}u_{1} + \cdots  + a_{n}u_{n}) = 0$ iff
$$\rho (a_{1})\phi (u_{1}) + \cdots  + \rho (a_{n})\phi (u_{n}) = 0,$$
and since $(\phi (u_{1}), \dots  , \phi (u_{n}))$ is a basis of $\rho^{*} (M)$, we must have $\rho (a_{i}) = 0$ for $i = 1, \dots  , n$, which (by injectivity of $\rho$ ) implies that $a_{i} = 0$ for $i = 1, \dots  , n$. Therefore, $\phi$  is injective. In particular, if $A$ is a subring of $B$, then $\rho$  is the inclusion map and Proposition 35.41 shows that a basis of $M$ becomes a basis of $M_{(B)}$ and that $M$ is embedded into $M_{(B)}$. It is also easy to see that if $M$ and $N$ are two free A-modules and $f$ : $M \to N$ is a linear map rep-
$$resented by the matrix \frac{X}{f} with respect to some bases (u_{1}, \dots  , u_{n}) of M and (v_{1}, \dots  , v_{m}) of N,$$
then the $B$-linear map  is also represented by the matrix $X$ over the bases $(\phi (u_{1}), \dots  , \phi (u_{n}))$ and $(\phi (v_{1}), \dots  , \phi (v_{m}))$. Proposition 35.41 yields another proof of the fact that any two bases of a free A-module have the same cardinality. Indeed, if $\mathfrak{m}$ is a maximal ideal in the ring $A$, then we have the quotient ring homomorphism $\pi$ : $A \to A/\mathfrak{m}$, and we get the $A/\mathfrak{m}-module \pi^{*} (M)$. If $M$ is free, any basis $(u_{1}, \dots  , u_{n})$ of $M$ becomes the basis $(\phi (u_{1}), \dots  , \phi (u_{n}))$ of $\pi^{*} (M)$; but $A/\mathfrak{m}$ is a field, so the dimension $n$ is uniquely determined. This argument also applies to an infinite basis $(u_{i})_{i\in I}$. Observe that by Proposition 35.14, we have an isomorphism
$$\pi^{*} (M) = (A/\mathfrak{m}) \otimes_{A}  M \approx M/\mathfrak{m} M,$$
so $M/\mathfrak{m} M$ is a vector space over the field $A/\mathfrak{m}$, which is the argument used in Theorem 35.1.

> **Proposition 35.42.** Given a ring homomomorphism $\rho$ : $A \to B$, for any two A-modules $M$ and $N$, there is a unique isomorphism
$$\rho^{*} (M) \otimes_{B}  \rho^{*} (N) \approx \rho^{*} (M \otimes_{A}  N),$$
such that $(1 \otimes u) \otimes (1 \otimes v) \mapsto 1 \otimes (u \otimes v)$, for all $u \in M$ and all $v \in N$. The proof uses identities from Proposition 33.13. It is not hard but it requires a little gymnastic; a good exercise for the reader.

<!-- PAGE 1318 -->
