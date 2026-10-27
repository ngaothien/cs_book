# Duality for Symmetric Powers


<!-- PAGE 1221 -->
is linearly independent. Using the commutativity of $\odot$ , we can also show that these vectors generate $S^{m}(E)$, and thus, they form a basis for $S^{m}(E)$. If I is infinite dimensional, then for any $m$ vectors $v_{1}, \dots  , v_{m} \in F$ there is a finite subset
$$J of I such that v_{k} = \sum_{j}  \in J u_{j,k}e_{j} for k = 1, \dots  , m, and if we write n = |J|, then the formula$$
for $f(v_{1}, \dots  , v_{m})$ is obtained by replacing the set ${1, \dots  , n}$ by $J$. The details are left as an exercise. As a consequence, when I is finite, say of size $p =$ dim(E), the dimension of $S^{m}(E)$ is the number of finite multisets $(j_{1}, \dots  , j_{p})$, such that $j_{1} + \cdots  + j_{p} = m, j_{k} \ge 0$. We leave as
$$an exercise to show that this number \begin{pmatrix} is_{m}^{p+m-1} \end{pmatrix} . Thus, if \dim(E) = p, then the dimension$$
$$of S^{m}(E \begin{pmatrix} ) is_{m}^{p+m-1} \\ dimension \end{pmatrix} . Compare with the dimension of E^{\otimes m}, which is p^{m}. In particular, when$$
$p = 2$, the  of $S^{m}(E)$ is $m + 1$. This can also be seen directly.
$$Remark: The number_{m}^{p+m-1} \begin{pmatrix}\end{pmatrix} is also the number of homogeneous monomials$$
$$X_{1}^{j1} \cdots  X_{p}^{jp}$$
of total degree $m$ in $p$ variables (we have $j_{1} +\cdots +j_{p} = m)$. This is not a coincidence! Given a vector space $E$ and a basis $(e_{i})_{i\in I}$ for $E$, Proposition 33.38 shows that every symmetric tensor $z \in S^{m}(E)$ can be written in a unique way as
$$z = \sum_{M\in N(I)}  \lambda_{M}  e_{i1}^{\odot M(i1)}\odot \cdots  \odot e_{ik}^{\odot M(ik)},$$
$${ \sum_{i1,...,ii}  \in Ik }M=dom((i)=mM)$$
for some unique family of scalars $\lambda_{M}  \in K$, all zero except for a finite number. This looks like a homogeneous polynomial of total degree $m$, where the monomials of total degree $m$ are the symmetric tensors
$$e_{i1}^{\odot M(i1)}\odot \cdots  \odot e_{ik}^{\odot M(ik)}$$
in the “indeterminates” $e_{i}$, where $i \in$ I (recall that $M(i_{1}) + \cdots  + M(i_{k}) = m)$ and implies that polynomials can be defined in terms of symmetric tensors.

## 33.12 Duality for Symmetric Powers

In this section all vector spaces are assumed to have finite dimension over a field of characteristic zero. We define a nondegenerate pairing $S^{n}(E^{*})\times S^{n}(E) \longrightarrow K$ as follows: Consider the multilinear map
$$(E^{*})^{n}\times  E^{n}\longrightarrow K$$
given by
$$(v_{1}^{*}, \dots  , v_{n}^{*}, u_{1}, \dots  , u_{n}) \mapsto \sum_{\sigma\in Sn}  v_{\sigma(1)}^{*}(u_{1}) \cdots  v_{\sigma(n)}^{*}(u_{n}).$$

<!-- PAGE 1222 -->
Note that the expression on the right-hand side is “almost” the determinant $det(v_{j}^{*}(u_{i}))$, except that the sign $sgn(\sigma$ ) is missing (where $sgn(\sigma$ ) is the signature of the permutation $\sigma$ ; that is, the parity of the number of transpositions into which $\sigma$  can be factored). Such an expression is called a permanent. It can be verified that this expression is symmetric w.r.t. the $u_{i}’s$ and also w.r.t. the $v_{j}^{*}$. For any fixed $(v_{1}^{*}, \dots  , v_{n}^{*}) \in (E^{*})^{n}$, we get a symmetric multilinear map
$$l_{v1*,...,vn*} : (u_{1}, \dots  , u_{n}) \mapsto \sum_{\sigma\in Sn}  v_{\sigma(1)}^{*}(u_{1}) \cdots  v_{\sigma(n)}^{*}(u_{n})$$
from $E^{n}$ to $K$. The map $l_{v1*,...,vn*}$ extends uniquely to a linear map $L_{v1*,...,vn*}$ : $S^{n}(E) \to K$ making the following diagram commute:
$$E^{n} /S^{n}(E)$$
$$\overline{G}^{\iota\odot}\overline{G}$$
$$\overline{G} G$$
$$GG$$
$$GGLv*,...,v*$$
$$l**G1n$$
$$v,...,vn#$$
$$1$$
$$K.$$
We also have the symmetric multilinear map
$$(v_{1}^{*}, \dots  , v_{n}^{*}) \mapsto L_{v1*,...,vn*}$$
from $(E^{*})^{n}$ to $Hom(S^{n}(E), K)$, which extends to a linear map $L$ from $S^{n}(E^{*})$ to $Hom(S^{n}(E), K)$ making the following diagram commute:
$$\iota \odot *$$
$$(E^{*})^{n}/S^{n}(E^{*})$$
$$\overline{P}\overline{P}$$
$$\overline{P} P$$
$$PP$$
$$PP$$
$$PPL$$
$$PP$$
$$'$$
$$Hom(S^{n}(E), K).$$
However, in view of the isomorphism
$$\otimes  \sim$$
$$Hom(UV, W)= Hom(U, Hom(V, W)),$$
with $U = S^{n}(E^{*}), V = S^{n}(E)$ and $W = K$, we can view $L$ as a linear map
$$L: S^{n}(E^{*}) \otimes S^{n}(E) \longrightarrow K,$$
which by Proposition 33.8 corresponds to a bilinear map
$$\langle -, -\rangle : S^{n}(E^{*}) \times  S^{n}(E) \longrightarrow K.(*)$$
This pairing is given explicitly on generators by
$$\langle v_{1}^{*} \odot \cdots  \odot v_{n}^{*}, u_{1} \odot \cdots  \odot u_{n}\rangle = \sum_{\sigma\in Sn}  v_{\sigma(1)}^{*}(u_{1}) \cdots  v_{\sigma(n)}^{*}(u_{n}).$$

<!-- PAGE 1223 -->
Now this pairing in nondegenerate. This can be shown using $bases.^{2}$ If $(e_{1}, \dots  , e_{m})$ is a
$$\odot \cdots \odot  \cdots$$
basis of $E$, then for every basis element $(e_{i1}^{*})^{\odot n1} (e_{ik}^{*})^{\odot nk}$ of $S^{n}(E^{*})$, with $n_{1}+ +n_{k} = n$, we have
$$\langle (e_{i1}^{*})^{\odot n1}\odot \cdots  \odot (e_{ik}^{*})^{\odot nk}, e_{i1}^{\odot n1}\odot \cdots  \odot e_{ik}^{\odot nk}\rangle = n_{1}! \cdots  n_{k}!,$$
and
$$\langle (e_{i1}^{*})^{\odot n1}\odot \cdots  \odot (e_{ik}^{*})^{\odot nk}, e_{j1} \odot \cdots  \odot e_{jn}\rangle = 0$$
if $(j_{1} \dots  , j_{n}) \neq  (i_{1}, \dots  , i_{1}, \dots  , i_{k}, \dots  , i_{k})$.
$$|{z}|{z}$$
$$n1nk$$
If the field $K$ has characteristic zero, then $n_{1}! \cdots  n_{k}!̸ = 0$. We leave the details as an exercise to the reader. Therefore we get a canonical isomorphism
$$\sim$$
$$(S^{n}(E))^{*}= S^{n}(E^{*}).$$
The following proposition summarizes the duality properties of symmetric powers.

> **Proposition 33.39.** Assume the field $K$ has characteristic zero. We have the canonical isomorphisms
$$\sim$$
$$(S^{n}(E))^{*}= S^{n}(E^{*})$$
and
$$\sim$$
$$S^{n}(E^{*})= Sym^{n}(E; K) = Hom_{symlin}(E^{n}, K),$$
which allows us to interpret symmetric tensors over $E^{*}$ as symmetric multilinear maps.

*Proof.* The isomorphism
$$\sim$$
$$\mu : S^{n}(E^{*})= Sym^{n}(E; K)$$
$$\sim \sim$$
follows from the isomorphisms $(S^{n}(E))^{*} = S^{n}(E^{*})$ and $(S^{n}(E))^{*} = Sym^{n}(E; K)$ given by

> **Proposition 33.35.**
Remarks:
$$\sim$$
$1$. The isomorphism $\mu$ : $S^{n}(E^{*}) = Sym^{n}(E; K)$ discussed above can be described explicitly as the linear extension of the map given by
$$\mu (v_{1}^{*} \odot \cdots  \odot v_{n}^{*})(u_{1} \odot \cdots  \odot u_{n}) = \sum_{\sigma\in Sn}  v_{\sigma(1)}^{*}(u_{1}) \cdots  v_{\sigma(n)}^{*}(u_{n}).$$
$$\odot \cdots  \odot$$
If $(e_{1}, \dots  , e_{m})$ is a basis of $E$, then for every basis element $(e_{i1}^{*})^{\odot n1} (e_{ik}^{*})^{\odot nk}$ of $S^{n}(E^{*})$, with $n_{1} + \cdots  + n_{k} = n$, we have
$$\mu ((e_{i1}^{*})^{\odot n1}\odot \cdots  \odot (e_{ik}^{*})^{\odot nk})(e_{i1}, \dots  , e_{i1}\dots  , e_{ik}, \dots  , e_{ik}) = n_{1}! \cdots  n_{k}!,$$
$$|{z}|{z}$$
$$n1nk$$
$\overline{2}\overline{This} \overline{is} \overline{where} \overline{the} \overline{assumption} \overline{that} \overline{we}$ are in finite dimension and that the field has characteristic zero are used.

<!-- PAGE 1224 -->
If the field $K$ has positive characteristic, then it is possible that $n_{1}! \cdots  n_{k}! = 0$, and this is why we required $K$ to be of characteristic $0$ in order for Proposition 33.39 to hold. $2$. The canonical isomorphism of Proposition 33.39 holds under more general conditions. Namely, that $K$ is a commutative algebra with identity over $\mathbb{Q}$, and that the $E$ is a finitely-generated projective K-module (see Definition 35.7). See Bourbaki, $[25]$ (Chapter III, §11, Section $5$, Proposition $8)$. The map from $E^{n}$ to $S^{n}(E)$ given by $(u_{1}, \dots  , u_{n}) \mapsto u_{1} \odot \cdots  \odot u_{n}$ yields a surjection $\pi$ : $E^{\otimes n} \to S^{n}(E)$. Because we are dealing with vector spaces, this map has some section; that is, there is some injection $\beta$  : $S^{n}(E) \to E^{\otimes n}$ with $\pi  \circ \beta  =$ id. Since our field $K$ has characteristic $0$, there is a special injection having a natural definition involving a symmetrization process defined as follows: For every permutation $\sigma$ , we have the map $r_{\sigma}$ : $E^{n} \to E^{\otimes n}$ given by
$$r_{\sigma}(u_{1}, \dots  , u_{n}) = u_{\sigma(1)} \otimes \cdots  \otimes u_{\sigma(n)}.$$
As $r_{\sigma}$ is clearly multilinear, $r_{\sigma}$ extends to a linear map $(r_{\sigma})_{\otimes}: E^{\otimes n} \to E^{\otimes n}$ making the following diagram commute
$$E^{n} /E^{\otimes n}$$
$$\overline{F}^{\iota\otimes}\overline{F}$$
$$\overline{F} F$$
$$FF$$
$$FF(r\sigma )\otimes$$
$$r\sigma F$$
$$"$$
$$E^{\otimes n},$$
and we get a map $\mathfrak{S}_{n} \times  E^{\otimes n} \longrightarrow E^{\otimes n}$, namely
$$\sigma  \cdot  z = (r_{\sigma})_{\otimes}(z).$$
It is immediately checked that this is a left action of the symmetric group $\mathfrak{S}_{n}$ on $E^{\otimes n}$, and the tensors $z \in E^{\otimes n}$ such that
$$\sigma  \cdot  z = z,for all\sigma  \in \mathfrak{S}_{n}$$
are called symmetrized tensors. We define the map $\eta$ : $E^{n} \to E^{\otimes n}$ by
$$\eta (u_{1}, \dots  , u_{n}) = \frac{1}{n!} \sum_{\sigma\in Sn}  \sigma  \cdot  (u_{1} \otimes \cdots  \otimes u_{n}) = \frac{1}{n!} \sum_{\sigma\in Sn}  u_{\sigma(1)} \otimes \cdots  \otimes u_{\sigma(n)}.$$
As the right hand side is clearly symmetric, we get a linear map $\eta_{\odot}$ : $S^{n}(E) \to E^{\otimes n}$ making the following diagram commute.
$$E^{n} /S^{n}(E)$$
$$\overline{G}^{\iota\odot}\overline{G}$$
$$\overline{G} G$$
$$GG$$
$$GG\eta \odot$$
$$\eta G$$
$$#$$
$$E^{\otimes n}$$
