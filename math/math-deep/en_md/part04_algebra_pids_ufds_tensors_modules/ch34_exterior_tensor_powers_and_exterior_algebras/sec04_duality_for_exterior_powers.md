# Duality for Exterior Powers


<!-- PAGE 1239 -->
Proposition 34.8 shows that geometrically every nonzero wedge $u_{1} \wedge \cdots  \wedge u_{n}$ corresponds to some oriented version of an $n$-dimensional subspace of $E$.

## 34.3 Some Useful Isomorphisms for Exterior Powers

We can show the following property of the exterior tensor product, using the proof technique of Proposition 33.13.

> **Proposition 34.9.** We have the following isomorphism:
$$nkn-k$$
$$^ \oplus  \sim^{n} M^ \otimes ^$$
$$(EF)=(E)(F).$$
$$k=0$$

## 34.4 Duality for Exterior Powers

In this section all vector spaces are assumed to have finite dimension. We define a nonde-
$$generate pairing \bigwedge  n(E^{*}) \times \bigwedge  n(E) \longrightarrow K as follows: Consider the multilinear map$$
$$(E^{*})^{n}\times  E^{n}\longrightarrow K$$
given by
$$(v_{1}^{*}, \dots  , v_{n}^{*}, u_{1}, \dots  , u_{n}) \mapsto \sum_{\sigma\in Sn}  sgn(\sigma ) v_{\sigma(1)}^{*}(u_{1}) \cdots  v_{\sigma(n)}^{*}(u_{n}) = \det(v_{j}^{*}(u_{i}))$$
$$v_{1}^{*}(u_{1})\cdots v_{1}^{*}(u_{n})$$
$$\vdots \ddots \vdots$$
$$=.$$
$$v_{n}^{*}(u_{1})\cdots v_{n}^{*}(u_{n})$$
It is easily checked that this expression is alternating w.r.t. the $u_{i}’s$ and also w.r.t. the $v_{j}^{*}$. For any fixed $(v_{1}^{*}, \dots  , v_{n}^{*}) \in (E^{*})^{n}$, we get an alternating multilinear map
$$l_{v1*,...,vn*} : (u_{1}, \dots  , u_{n}) \mapsto \det(v_{j}^{*}(u_{i}))$$
$$n$$
$$from E^{n}to K. The map l_{v1*,...,vn*} extends uniquely to a linear map L_{v1*,...,vn*} : \bigwedge  (E) \to K$$
making the following diagram commute:
$$E^{n}\overline{H}^{\iota\wedge}\overline{H}\overline{H}/ \bigwedge  n(E)$$
$$HH$$
$$HH$$
$$HLv*,...,v*$$
$$lHH1n$$
$$v*,...,v*$$$
$$1n$$
$$K.$$
We also have the alternating multilinear map
$$(v_{1}^{*}, \dots  , v_{n}^{*}) \mapsto L_{v1*,...,vn*}$$

<!-- PAGE 1240 -->
$$n$$
$$from (E^{*})^{n}to Hom(^{n} \bigwedge  (E), K), which extends to a linear map L from \bigwedge  (E^{*}) to$$
$$Hom(^{n} \bigwedge  (E), K) making the following diagram commute:$$
$$\iota \wedge */n$$
$$(E^{*})^{n}\overline{P}\overline{P}\overline{P} P \bigwedge  (E^{*})$$
$$PP$$
$$PP$$
$$PPL$$
$$PP$$
$$'$$
$$Hom(^{n} \bigwedge  (E), K).$$
However, in view of the isomorphism
$$\otimes  \sim$$
$$Hom(UV, W)= Hom(U, Hom(V, W)),$$
$$with U = \bigwedge  n(E^{*}), V = \bigwedge  n(E) and W = K, we can view L as a linear map$$
$$nn$$
$$L:^(E^{*}) \otimes ^(E) \longrightarrow K,$$
which by Proposition 33.8 corresponds to a bilinear map
$$nn$$
$$\langle -, -\rangle :^(E^{*}) \times ^(E) \longrightarrow K.(*)$$
This pairing is given explicitly in terms of generators by
$$\langle v_{1}^{*} \wedge \cdots  \wedge v_{n}^{*}, u_{1}, \dots  , u_{n}\rangle = \det(v_{j}^{*}(u_{i})).$$
Now this pairing in nondegenerate. This can be shown using bases. Given any basis
$$(e_{1}, \dots  , e_{m}) of E, for every basis element e_{i1}^{*}\wedge \cdots \wedge e_{in}^{*} of \bigwedge_{1}  n(E^{*}) (with 1 \le i_{1} < \cdots  < i_{n} \le m),$$
we have
$$($$
$$1if (j, \dots  , j_{n}) = (i_{1}, \dots  , i_{n})$$
$$\langle e_{i1}^{*} \wedge \cdots  \wedge e_{in}^{*}, e_{j1}, \dots  , e_{jn}\rangle =$$
$$0otherwise.$$
We leave the details as an exercise to the reader. As a consequence we get the following canonical isomorphisms.

> **Proposition 34.10.** There is a canonical isomorphism
$$n$$
$$^\sim^{n} ^$$
$$((E))^{*}=(E^{*}).$$
There is also a canonical isomorphism
$$n$$
$$^ \sim$$
$$\mu :(E^{*})= Alt^{n}(E; K)$$
which allows us to interpret alternating tensors over $E^{*}$ as alternating multilinear maps.

<!-- PAGE 1241 -->

*Proof.* $\sim n$
$$The second isomorphism follows from the canonical isomorphism (^{n}\sim \bigwedge  (E))^{*}= \bigwedge  (E^{*})$$
$$and the canonical isomorphism (^{n} \bigwedge  (E))^{*}= Alt^{n}(E; K) given by Proposition 34.5.$$
Remarks:
$$n \sim$$
$$1. The isomorphism \mu : \bigwedge  (E^{*})= Alt^{n}(E; K) discussed above can be described explicitly$$
as the linear extension of the map given by
$$\mu (v_{1}^{*} \wedge \cdots  \wedge v_{n}^{*})(u_{1}, \dots  , u_{n}) = \det(v_{j}^{*}(u_{i})).$$
$2$. The canonical isomorphism of Proposition 34.10 holds under more general conditions. Namely, that $K$ is a commutative ring with identity and that $E$ is a finitely-generated projective K-module (see Definition 35.7). See Bourbaki, $[25]$ (Chapter III, §11, Section $5$, Proposition $7). 3$. Variants of our isomorphism $\mu$  are found in the literature. For example, there is a version $\mu'$ , where
$$\mu' = \frac{1}{n!} \mu ,$$
with the $factor_{n!}^{1}$ added in front of the determinant. Each version has its its own merits and inconveniences. Morita $[133]$ uses $\mu'$ because it is more convenient than $\mu$ when dealing with characteristic classes. On the other hand, $\mu'$ may not be defined for a field with positive characteristic, and when using $\mu'$ , some extra factor is needed in defining the wedge operation of alternating multilinear forms (see Section 34.5) and for exterior differentiation. The version $\mu$  is the one adopted by Warner $[192]$, Knapp $[107]$, Fulton and Harris $[69]$, and Cartan $[34, 35]$. If $f$ : $E \to F$ is any linear map, by transposition we get a linear map $f^{\top}$ : $F^{*} \to E^{*}$ given by
$$f^{\top} (v^{*}) = v^{*}\circ f,v^{*}\in F^{*} .$$
Consequently, we have
$$f^{\top} (v^{*})(u) = v^{*}(f(u)),for all u \in E and all v^{*}\in F^{*} .$$
For any $p \ge 1$, the map
$$(u_{1}, \dots  , u_{p}) \mapsto f(u_{1}) \wedge \cdots  \wedge f(u_{p})$$
$$p p p$$
$$fromp F E^{p}to \bigwedge  F is multilinear alternating, so it induces a unique linear map \bigwedge  f : \bigwedge  E \to$$
$$\bigwedge  making the following diagram commute$$
$$p$$
$$E^{p}\overline{E}^{\iota\wedge}\overline{E}\overline{E}/ \bigwedge  E$$
$$EE$$
$$EEp f$$
$$EE" F, \bigwedge_{p}$$
$$\bigwedge$$

<!-- PAGE 1242 -->
and defined on generators by
$$p$$
$$\begin{pmatrix} ^f \end{pmatrix} (u_{1} \wedge \cdots  \wedge u_{p}) = f(u_{1}) \wedge \cdots  \wedge f(u).$$
$$p p p p$$
$$Combining \bigwedge  and duality, we get a linear map \bigwedge  f^{\top} : \bigwedge  F^{*} \to \bigwedge^{p}  E^{*}defined on generators$$
by
$$p$$
$$\begin{pmatrix} ^f^{\top} \\ f :E \end{pmatrix} (v_{1}^{*} \wedge \cdots  \wedge v_{p}^{*}) = f^{\top}(v_{1}^{*}) \wedge \cdots  \wedge f^{\top}(v_{p}^{*}).$$

> **Proposition 34.11.** If   $\to F$ is any linear map between two finite-dimensional vector spaces $E$ and $F$, then
$$pp$$
$$\mu \begin{pmatrix} ^f^{\top} \\ Itis \end{pmatrix} \begin{pmatrix} (\omega ) \\ enough \end{pmatrix} (u_{1}, \dots  , u_{p}) = \mu (\omega )(f(u_{1}), \dots  , f(u_{p})),\omega  \in ^F^{*} , u_{1}, \dots  , u_{p} \in E.$$

*Proof.* to prove the formula on generators. By definition of $\mu$ , we have
$$p$$
$$\mu \begin{pmatrix} ^f^{\top} \end{pmatrix} \begin{pmatrix} (v_{1}^{*}\wedge \cdots  \wedge v_{p}^{*}) \end{pmatrix} (u_{1}, \dots  , u_{p})=\mu (f^{\top} (v_{1}^{*}) \wedge \cdots  \wedge f^{\top}(v_{p}^{*}))(u_{1}, \dots  , u_{p})$$
$$=\det(f^{\top} (v_{j}^{*})(u_{i}))$$
$$=\det(v_{j}^{*}(f(u_{i})))$$
$$=\mu (v_{1}^{*} \wedge \cdots  \wedge v_{p}^{*})(f(u_{1}), \dots  , f(u_{p})),$$
as claimed.
$$p$$
$$Remark: The map \bigwedge  f^{\top} is often denoted f^{*} , although this is an ambiguous notation since$$
$$p is E_{*} dropped. Proposition 34.11 gives us the behavior of \bigwedge  pf^{\top} under the identification of$$
$$\bigwedge  pand Alt^{p}(E; K) via the isomorphism \mu .$$
$$n$$
$$As in the case of symmetric powers,  the mapn from E^{n}to \bigwedge  (E) given by (u_{1}, \dots  , u_{n}) \mapsto$$
$$u_{1} \wedge \cdots  \wedge u_{n} yields a surjectionn \pi : E^{\otimes n} \to \bigwedge  (E). Now this map has some section, so there$$
$$is some injection \eta : \bigwedge  (E) \to E^{\otimes n}with \pi  \circ \eta  = id. As we saw in Proposition 34.10 there is$$
a canonical isomorphism
$$n$$
$$^\sim^{n} ^$$
$$((E))^{*}=(E^{*})$$
for any field $K$, even of positive characteristic. However, if our field $K$ has characteristic $0$, then there is a special section having a natural definition involving an antisymmetrization process. Recall, from Section 33.12 that we have a left action of the symmetric $group\mathfrak{S}_{n}$ on $E^{\otimes n}$. The tensors $z \in E^{\otimes n}$ such that
$$\sigma  \cdot  z = sgn(\sigma ) z,for all\sigma  \in \mathfrak{S}_{n}$$
are called antisymmetrized tensors. We define the map $\eta$ : $E^{n} \to E^{\otimes n}$ by
$$\eta (u_{1}, \dots  , u_{n}) = \frac{1}{n!} \sum_{\sigma\in Sn}  sgn(\sigma ) u_{\sigma(1)} \otimes \cdots  \otimes u_{\sigma(n)}.^{1}$$
$\overline{1}\overline{It} \overline{is} \overline{the} \overline{division} \overline{by} \overline{n}\overline{!} \overline{that} \overline{requires} \overline{the}$ field to have characteristic zero.
