# Left and Right Hooks


<!-- PAGE 1251 -->
where $A$ is the matrix expressing the $v_{j}$ in terms of the $e_{i}$, we have
$$\langle v_{1} \wedge \cdots  \wedge v_{n}, v_{1} \wedge \cdots  \wedge v_{n}\rangle_{\wedge} = \det(A)^{2}\langle e_{1} \wedge \cdots  \wedge e_{n}, e_{1} \wedge \cdots  \wedge e_{n}\rangle = \det(A)^{2}.$$
As a consequence, det(A) $= p\overline{det(}\overline{\langle}\overline{v}_{i}\overline{, v}_{j}\overline{\rangle}\overline{),}$ and
$$q$$
$$v_{1} \wedge \cdots  \wedge v_{n} =\det(\langle v_{i}, v_{j}\rangle ) e_{1} \wedge \cdots  \wedge e_{n},$$
from which it follows that
$$*(1) = \frac{1}{pdet(\langle v_{i}, v_{j}\rangle )} v_{1} \wedge \cdots  \wedge v_{n}$$
(see Jost $[104]$, Chapter $2$, Lemma 2.1.3).
$$⊛$$

## 34.7 Left and Right Hooks

In this section all vector spaces are assumed to have finite dimension. Say dim(E) $= n$. Using our nonsingular pairing
$$pp$$
$$\langle -, -\rangle :^E^{*}\times ^E \longrightarrow K(1 \le p \le n)$$
defined on generators by
$$\langle u_{1}^{*} \wedge \cdots  \wedge u_{p}^{*}, v_{1} \wedge \cdots  \wedge u_{p}\rangle = \det(u_{i}^{*} (v_{j})),$$
we define various contraction operations (partial evaluation operators)
$$pp+qq$$
$$⌟:^E \times ^E^{*}\longrightarrow ^E^{*}(left hook)$$
and
$$p+qpq$$
$$⌞:^E^{*}\times ^E \longrightarrow ^E^{*}(right hook),$$
as well as the versions obtained by replacing $E$ by $E^{*}$ and $E^{**}$ by $E$. We begin with the left interior product or left hook, ⌟.
$$p$$
$$Let u \in \bigwedge  E. For any q such that p + q \le n, multiplication on the right by u is a linear$$
map
$$qp+q$$
$$\wedge_{R} (u):^E \longrightarrow ^E$$
given by
$$v \mapsto v \wedge u$$

<!-- PAGE 1252 -->
$$q$$
$$where v \in \bigwedge  E. The transpose of \wedge_{R} (u) yields a linear map$$
$$* *$$
$$(\wedge_{R} (u))^{\top}: \begin{pmatrix} p+q \\ ^E \end{pmatrix} \longrightarrow \begin{pmatrix} q \\ ^E \end{pmatrix} ,$$
$$which, using the isomorphisms \bigwedge  \sim = \bigwedge_{+q}  p+q E_{*}and \bigwedge  \sim = \bigwedge  q E_{*}, can be viewed$$
$$as a map \begin{pmatrix} p+q E^{*} \end{pmatrix} \begin{pmatrix} q E^{*} \end{pmatrix}$$
$$pq$$
$$(\wedge_{R} (u))^{\top}:^E^{*}\longrightarrow ^E^{*}$$
given by
$$z^{*}\mapsto z^{*}\circ \wedge_{R} (u),$$
$$p+q  ⌟$$
$$where ⌟ z^{*}\in \bigwedge  E^{*}. We denote z^{*}\circ \wedge_{R} (u) by uz^{*}. In terms of our pairing, the adjoint$$
$u$ of $\wedge_{R} (u)$ defined by
$$\langle u ⌟z^{*}, v\rangle = \langle z^{*}, \wedge_{R} (u)(v)\rangle ;$$
this in turn leads to the following definition.
$$p p+q  ⌟q$$
$$Definition 34.8. Let u \in \bigwedge  E and z^{*}\in \bigwedge  E^{*}. We define uz^{*}\in \bigwedge  E^{*}to be q-vector$$
uniquely determined by
$$⌟q$$
$$\langle uz^{*}, v\rangle = \langle z^{*}, v \wedge u\rangle ,for all v \in \bigwedge  E.$$
Remark: Note that to be precise the operator
$$pp+qq$$
$$⌟:^E \times ^E^{*}\longrightarrow ^E^{*}$$
depends of $p, q$, so we really defined a family of operators $⌟_{p,q}$. This family of operators $⌟_{p,q}$ induces a map
$$⌟:^E \times ^E^{*}\longrightarrow ^E^{*},$$
with
$$pp+qq$$
$$⌟_{p,q} :^E \times ^E^{*}\longrightarrow ^E^{*}$$
as defined before. The common practice is to omit the subscripts of ⌟ . It is immediately verified that
$$(u \wedge v) ⌟z^{*}= u ⌟(v ⌟z^{*}),$$
$$k p-k p+q$$
$$for all u \in \bigwedge  E, v \in \bigwedge  E, z^{*}\in \bigwedge  E^{*}since$$
$$\langle (u \wedge v) ⌟z^{*}, w\rangle = \langle z^{*}, w \wedge u \wedge v\rangle = \langle v ⌟z^{*}, w \wedge u\rangle = \langle u ⌟(v ⌟z^{*}), w\rangle ,$$

<!-- PAGE 1253 -->
$$q$$
$$whenever w \in \bigwedge  E. This means that$$
$$⌟:^E \times ^E^{*}\longrightarrow ^E^{*}$$
$$is a left  action of the (noncommutative)  ring \bigwedge  E with multiplication \wedge on \bigwedge  E^{*}, which$$
$$makes \bigwedge  E^{*}into a left \bigwedge  E-module.$$
By interchanging $E$ and $E^{*}$ and using the isomorphism
$$*$$
$$\sim^{k} ^$$
$$\begin{pmatrix} k \\ ^F \end{pmatrix} =F^{*},$$
we can also define some maps
$$pp+qq$$
$$⌟:^E^{*}\times ^E \longrightarrow ^E,$$
and make the following definition.
$$p p+q ⌟q$$
$$Definition 34.9. Let u^{*}\in \bigwedge  E^{*}, and z \in \bigwedge  E. We define u^{*}z \in \bigwedge  as the q-vector$$
uniquely defined by
$$⌟q$$
$$\langle v^{*}\wedge u^{*}, z\rangle = \langle v^{*}, u^{*}z\rangle ,for all v^{*}\in \bigwedge  E^{*}.$$
As for the previous version, we have a family of operators $⌟_{p,q}$ which define an operator
$$⌟:^E^{*}\times ^E \longrightarrow ^E.$$
We easily verify that
$$(u^{*}\wedge v^{*}) ⌟z = u^{*}⌟(v^{*}⌟z),$$
$$p-k p+q  ⌟$$
$$whenever u^{*} \in \bigwedge  E^{*} , v^{*}\in \bigwedge  E^{*}, and  z \in \bigwedge  E;  so this version ofis a left action of$$
$$the ring \bigwedge  E^{*}on \bigwedge^{k}  E which makes \bigwedge  E into a left \bigwedge  E^{*}-module.$$
In order to proceed any further we need some combinatorial properties of the basis of $p E$
$$\bigwedge  constructed from a basis (e_{1}, \dots  , e_{n}) of E. Recall that for any (nonempty) subset$$
$I \subseteq {1, \dots  , n}$, we let
$$e_{I} = e_{i1} \wedge \cdots  \wedge e_{ip},$$
where $I = {i_{1}, \dots  , i_{p}}$ with $i_{1} < \cdots  < i_{p}$. We also let $e_{\emptyset} = 1$. Given any two nonempty subsets $H, L \subseteq {1, \dots  , n}$ both listed in increasing order, say $H = {h_{1} < \dots  < h_{p}}$ and $L = {\ell_{1}  < \dots  < \ell_{q}$ }, if $H$ and $L$ are disjoint, let $H \cup L$ be union of $H$ and $L$ considered as the ordered sequence
$$(h_{1}, \dots  , h_{p}, \ell_{1} , \dots  , \ell_{q} ).$$
Then let
$$0if H \cap L \neq  \emptyset ,$$
$$\rho_{H,L}  =$$
$$(-1)^{\nu}if H \cap L = \emptyset ,$$

<!-- PAGE 1254 -->
where
$$\nu  = |{(h, l) | (h, l) \in H \times  L, h > l}|.$$
Observe that when $H \cap L = \emptyset$ , |H| $= p$ and |L| $= q$, the number $\nu$  is the number of inversions of the sequence
$$(h_{1}, \cdots  , h_{p}, \ell_{1} , \cdots  , \ell_{q} ),$$
where an inversion is a pair $(h_{i}, \ell_{j}$ ) such that $h_{i} > \ell_{j}$ .  Unless $p + q = n$, the function whose graph is given by
$$\begin{pmatrix} 1 \\ \cdots & p & p + 1 & \cdots & p + q \\ h_{1} & \cdots & h_{p} & \ell_{1} & \cdots & \ell_{q} \end{pmatrix}$$
is not a permutation of ${1, \dots  , n}$. We can view $\nu$  as a slight generalization of the notion of the number of inversions of a permutation.

> **Proposition 34.18.** For any basis $(e_{1}, \dots  , e_{n})$ of $E$ the following properties hold:
$(1)$ If $H \cap L = \emptyset$ , |H| $= p$, and |L| $= q$, then
$$\rho_{H,L} \rho_{L,H}  = (-1)^{\nu}(-1)^{pq-\nu}= (-1)^{pq}.$$
$(2)$ For $H, L \subseteq {1, \dots  , m}$ listed in increasing order, we have
$$e_{H} \wedge e_{L} = \rho_{H,L} e_{H\cup L}.$$
Similarly,
$$e_{H}^{*} \wedge e_{L}^{*} = \rho_{H,L} e_{H\cup L}^{*}.$$
$(3)$ For the left hook
$$pp+qq$$
$$⌟:^E \times ^E^{*}\longrightarrow ^E^{*},$$
we have
$$e_{H} ⌟e_{L}^{*} = 0if H̸ \subseteq L$$
$$e_{H} ⌟e_{L}^{*} = \rho_{L-H,H} e_{L-H}^{*}if H \subseteq L.$$
$(4)$ For the left hook
$$pp+qq$$
$$⌟:^E^{*}\times ^E \longrightarrow ^E,$$
we have
$$e_{H}^{*} ⌟e_{L} = 0if H̸ \subseteq L$$
$$e_{H}^{*} ⌟e_{L} = \rho_{L-H,H} e_{L-H}if H \subseteq L.$$

<!-- PAGE 1255 -->

*Proof.* These are proved in Bourbaki $[25]$ (Chapter III, §11, Section $11)$, but the proofs of
$(3)$ and $(4)$ are very concise. We elaborate on the proofs of $(2)$ and $(4)$, the proof of $(3)$ being similar. In $(2)$ if $H\cap L \neq  \emptyset$ , then $e_{H}\wedge e_{L}$ contains some vector twice and so $e_{H}\wedge e_{L} = 0$. Otherwise, $e_{H} \wedge e_{L}$ consists of
$$e_{h1} \wedge \cdots  \wedge e_{hp} \wedge e_{\ell1} \wedge \cdots  \wedge e_{\ell q},$$
and to order the sequence of indices in increasing order we need to transpose any two indices $(h_{i}, \ell_{j}$ ) corresponding to an inversion, which yields $\rho_{H,L} e_{H\cup L}$. Let us now consider $(4)$. We have |L| $= p + q$ and |H| $= p$, and the $q$-vector $e_{H}^{*}$ ⌟ $e_{L}$ is characterized by
$$\langle v^{*}, e_{H}^{*} ⌟e_{L}\rangle = \langle v^{*}\wedge e_{H}^{*}, e_{L}\rangle$$
$$q$$
$$for all v^{*}\in \bigwedge  E^{*}. There are two cases.$$
$$q$$
$$Case 1: H̸ \subseteq L. If so, no matter what v^{*}\in \bigwedge  E^{*}is, since H contains some index h$$
not in $L$, the hth row $(e_{h}^{*}(e_{\ell1}), \dots  , e_{h}^{*}(e_{\ell p+q}))$ of the determinant $\langle v^{*} \wedge e_{H}^{*}, e_{L}\rangle$ must be zero,
$$q E_{*}$$
$$so \langle ⌟v^{*}\wedge e_{H}^{*}, e_{L}\rangle = 0 for all v^{*}\in \bigwedge  , and since the pairing is nongenerate, we must have$$
$e_{H}^{*} e_{L} = 0$. Case $2: H \subseteq L$. In this case, for $v^{*} = e_{L-H}^{*}$, by $(2)$ we have
$$\langle e_{L-H}^{*}, e_{H}^{*} ⌟e_{L}\rangle = \langle e_{L-H}^{*} \wedge e_{H}^{*}, e_{L}\rangle = \langle \rho_{L-H,H} e_{L}^{*}, e_{L}\rangle = \rho_{L-H,H} ,$$
which yields
$$\langle e_{L-H}^{*}, e_{H}^{*} ⌟e_{L}\rangle = \rho_{L-H,H} .$$
$$The q-vector e_{H}^{*} ⌟e_{L} can be written as a linear combination e_{H}^{*} ⌟e_{L} = \sum  J \lambda_{J} e_{J} with |J| = q$$
so
$$\langle e_{L-H}^{*}, e_{H}^{*} ⌟e_{L}\rangle = \sum_{J}  \lambda_{J} \langle e_{L-H}^{*}, e_{J}\rangle .$$
By definition of the pairing, $\langle e_{L-H}^{*}, e_{J}\rangle = 0$ unless $J = L$ - $H$, which means that
$$\langle e_{L-H}^{*}, e_{H}^{*} ⌟e_{L}\rangle = \lambda_{L-H} \langle e_{L-H}^{*}, e_{L-H}\rangle = \lambda_{L-H} ,$$
so $\lambda_{L-H}  = \rho_{L-H,H}$ , as claimed. Using Proposition 34.18, we have the

> **Proposition 34.19.** For the left hook
$$q+1q$$
$$⌟: E \times ^E^{*}\longrightarrow ^E^{*},$$
$$q+1-s s$$
$$for every u \in E, x^{*}\in \bigwedge  E^{*}, and y^{*}\in \bigwedge  E^{*}, we have$$
$$u ⌟(x^{*}\wedge y^{*}) = (-1)^{s}(u ⌟x^{*}) \wedge y^{*}+ x^{*}\wedge (u ⌟y^{*}).$$

<!-- PAGE 1256 -->

*Proof.* We can prove the above identity assuming that $x^{*}$ and $y^{*}$ are of the form $e_{I}^{*}$ and $e_{J}^{*}$ using Proposition 34.18 and leave the details as an exercise for the reader.
$$⌟ q$$
$$Thus,: E \times^{q+1} \bigwedge  E^{*}\longrightarrow \bigwedge  E^{*}is almost an anti-derivation, except that the sign (-1)^{s}$$
is applied to the wrong factor. We have a similar identity for the other version of the left hook
$$q+1q$$
$$⌟: E^{*}\times ^E \longrightarrow ^E,$$
namely
$$u⌟(x \wedge y) = (-1)^{s}(u^{*}⌟x) \wedge y + x \wedge (u^{*}⌟y)$$
$$q+1-s s$$
$$for every u^{*}\in E^{*}, x \in \bigwedge^{*}  E, and y \in \bigwedge  E.$$
An application of this formula when $q = 3$ and $s = 2$ yields an interesting equation. In
$$2$$
$$this case, u^{*}\in E^{*}and x, y \in \bigwedge  E, so we get$$
$$u^{*}⌟(x \wedge y) = (u^{*}⌟x) \wedge y + x \wedge (u^{*}⌟y).$$
$$2 ⌟$$
$$In particular,⌟ for x =⌟ y, since x \in \bigwedge  E and u^{*}x \in E, Proposition 34.12 implies that$$
$(u^{*} x) \wedge x = x \wedge (u^{*} x)$, and we obtain
$$u^{*}⌟(x \wedge x) = 2((u^{*}⌟x) \wedge x).(\dagger )$$
As a consequence, $(u^{*}$ ⌟ $x) \wedge x = 0$ iff $u^{*}$ ⌟ $(x \wedge x) = 0$. We will use this identity together
$$2$$
$$with Proposition 34.25 to prove that a 2-vector x \in \bigwedge  E is decomposable iff x \wedge x = 0.$$
It is also possible to define a right interior product or right hook ⌞, using multiplication on the left rather than multiplication on the right. Then we use the maps
$$p+qpq$$
$$⌞:^E^{*}\times ^E \longrightarrow ^E^{*}$$
to make the following definition.
$$p p+q ⌞q$$
$$Definition 34.10. Let u \in \bigwedge  E and z^{*}\in \bigwedge  E^{*}. We define z^{*}u \in \bigwedge  E^{*}to be the$$
$q$-vector uniquely defined as
$$⌞q$$
$$\langle z^{*}u, v\rangle = \langle z^{*}, u \wedge v\rangle ,for all v \in \bigwedge  E.$$
This time we can prove that
$$z^{*}⌞(u \wedge v) = (z^{*}⌞u) ⌞v,$$
so the family of operators $⌞_{p,q}$ defines a right action
$$⌞:^E^{*}\times ^E \longrightarrow ^E^{*}$$

<!-- PAGE 1257 -->
$$of the ring \bigwedge  E on \bigwedge  E^{*}which makes \bigwedge  E^{*}into a right \bigwedge  E-module.$$
Similarly, we have maps
$$p+qpq$$
$$⌞:^E \times ^E^{*}\longrightarrow ^E$$
which in turn leads to the following dual formation of the right hook.
$$p p+q ⌞q$$
$$Definition 34.11. Let u^{*}\in \bigwedge  E^{*}and z \in \bigwedge  E. We define zu^{*}\in \bigwedge  to be the q-vector$$
uniquely defined by
$$⌞q$$
$$\langle u^{*}\wedge v^{*}, z\rangle = \langle v^{*}, zu^{*}\rangle ,for all v^{*}\in \bigwedge  E^{*}.$$
We can prove that
$$z ⌞(u^{*}\wedge v^{*}) = (z ⌞u^{*}) ⌞v^{*},$$
so the family of operators $⌞_{p,q}$ defines a right action
$$⌞:^E \times ^E^{*}\longrightarrow ^E$$
$$of the ring \bigwedge  E^{*}on \bigwedge  E which makes \bigwedge_{+q}  E into a right \bigwedge  E^{*}-module.$$
$$⌟p p q$$
$$Since the left hook: \bigwedge  E \times \bigwedge  E^{*}\longrightarrow \bigwedge_{p}  E^{*}is defined by$$
$$⌟ q p+q$$
$$\langle uz^{*}, v\rangle = \langle z^{*}, v \wedge u\rangle ,for all u \in \bigwedge  E, v \in \bigwedge  E and z^{*}\in \bigwedge  E^{*},$$
the right hook
$$p+qpq$$
$$⌞:^E^{*}\times ^E \longrightarrow ^E^{*}$$
by
$$⌞p q p+q$$
$$\langle z^{*}u, v\rangle = \langle z^{*}, u \wedge v\rangle ,for all u \in \bigwedge  E, v \in \bigwedge  E, and z^{*}\in \bigwedge  E^{*},$$
and $v \wedge u = (-1)^{pq}u \wedge v$, we conclude that
$$⌞  ⌟$$
$$z^{*}u = (-1)^{pq}uz^{*}.$$
Similarly, since
$$⌟p q p+q$$
$$\langle v^{*}\wedge u^{*}, z\rangle = \langle v^{*}, u^{*}z\rangle ,for all u^{*}\in \bigwedge_{p}  E^{*}, v^{*}\in \bigwedge_{q}  E^{*}and z \in \bigwedge  E$$
$$⌞  p+q$$
$$\langle u^{*}\wedge v^{*}, z\rangle = \langle v^{*}, zu^{*}\rangle ,for all u^{*}\in \bigwedge  E^{*}, v^{*}\in \bigwedge  E^{*}, and z \in \bigwedge  E,$$
and $v^{*} \wedge u^{*} = (-1)^{pq}u^{*} \wedge v^{*}$, we have
$$⌞ ⌟$$
$$zu^{*}= (-1)^{pq}u^{*}z.$$
We summarize the above facts in the following proposition.

<!-- PAGE 1258 -->

> **Proposition 34.20.** The following identities hold:
$$⌞  ⌟p p+q$$
$$z^{*}u = (-1)^{pq}uz^{*}for all u \in \bigwedge  E and all z^{*}\in \bigwedge  E^{*}$$
$$⌞ ⌟p p+q$$
$$zu^{*}= (-1)^{pq}u^{*}zfor all u^{*}\in \bigwedge  E^{*}and all z \in \bigwedge  E.$$
Therefore the left and right hooks are not independent, and in fact each one determines the other. As a consequence, we can restrict our attention to only one of the hooks, for example the left hook, but there are a few situations where it is nice to use both, for example in Proposition 34.23. A version of Proposition 34.18 holds for right hooks, but beware that the indices in $\rho_{L-H,H}$  are permuted. This permutation has to do with the fact that the left hook and the right hook are related via a sign factor.

> **Proposition 34.21.** For any basis $(e_{1}, \dots  , e_{n})$ of $E$ the following properties hold:
$(1)$ For the right hook
$$p+qpq$$
$$⌞:^E \times ^E^{*}\longrightarrow ^E$$
we have
$$e_{L} ⌞e_{H}^{*} = 0if H̸ \subseteq L$$
$$e_{L} ⌞e_{H}^{*} = \rho_{H,L-H} e_{L-H}if H \subseteq L.$$
$(2)$ For the right hook
$$p+qpq$$
$$⌞:^E^{*}\times ^E \longrightarrow ^E^{*}$$
we have
$$e_{L}^{*} ⌞e_{H} = 0if H̸ \subseteq L$$
$$e_{L}^{*} ⌞e_{H} = \rho_{H,L-H} e_{L-H}^{*}if H \subseteq L.$$
$$⌟p p+q q$$
$$Remark:⌟p  Our definition  qof  left hooks as left actions: \bigwedge  ⌞E \times \bigwedge_{p+q}  E\longrightarrow \bigwedge  Eqand$$
$$: \bigwedge  ⌞Ep\times^{p+q} \bigwedge_{+q}  E \longrightarrow \bigwedge  E and right hooks as right actionsq : \bigwedge  E^{*}\times^{p} \bigwedge^{*}  E \longrightarrow \bigwedge^{*}  E^{*}$$
$$and: \bigwedge^{*}  E\times^{p} \bigwedge  E^{*}\longrightarrow \bigwedge  E is identical to the definition found in Fulton and Harris [69]$$
(Appendix $B)$. However, the reader should be aware that this is not a universally accepted notation. In fact, the left hook $u^{*}$ ⌟ $z$ defined in Bourbaki $[25]$ is our right hook $z$ ⌞ $u^{*}$, up to the sign $(-1)^{p(p-1)/2}$. This has to do with the fact that Bourbaki uses a different pairing which also involves an extra sign, namely
$$\langle v^{*}, u^{*}⌟z\rangle = (-1)^{p(p-1)/2}\langle u^{*}\wedge v^{*}, z\rangle .$$

<!-- PAGE 1259 -->
One of the side-effects of this choice is that Bourbaki’s version of Formula $(4)$ of Proposition 34.18 (Bourbaki $[25]$, Chapter III, page $168)$ is
$$e_{H}^{*} ⌟e_{L} = 0if H̸ \subseteq L$$
$$e_{H}^{*} ⌟e_{L} = (-1)^{p(p-1)/2}\rho_{H,L-H} e_{L-H}if H \subseteq L,$$
where |H| $= p$ and |L| $= p + q$. This correspond to Formula $(1)$ of Proposition 34.21 up to the sign factor $(-1)^{p(p-1)/2}$, which we find horribly confusing. Curiously, an older edition of Bourbaki $(1958)$ uses the same pairing as Fulton and Harris $[69]$. The reason (and the advantage) for this change of sign convention is not clear to us. We also have the following version of Proposition 34.19 for the right hook.

> **Proposition 34.22.** For the right hook
$$q+1q$$
$$⌞:^E^{*}\times  E \longrightarrow ^E^{*},$$
$$r q+1-r$$
$$for every u \in E, x^{*}\in \bigwedge  E^{*}, and y^{*}\in \bigwedge  E^{*}, we have$$
$$(x^{*}\wedge y^{*}) ⌞u = (x^{*}⌞u) \wedge y^{*}+ (-1)^{r}x^{*}\wedge (y^{*}⌞u).$$

*Proof.* A proof involving determinants can be found in Warner $[192]$, Chapter $2$.
$$⌞q+1 q$$
$$Thus,: \bigwedge  ⌞Eq+1\times   E \longrightarrow \bigwedge_{*}  Eisq  an anti-derivation. A similar formula holds for the$$
$$the right hook: \bigwedge^{*}  E \times  E\longrightarrow \bigwedge^{*}  E, namely$$
$$(x \wedge y) ⌞u^{*}= (x ⌞u^{*}) \wedge y + (-1)^{r}x \wedge (y ⌞u^{*}),$$
$$r q+1-r$$
$$for every u^{*}\in E, \in \bigwedge  E, and y \in \bigwedge  E. This formula is used by Shafarevitch⌟ [164] to$$
define a hook, but beware that Shafarevitch use the left hook notation $u^{*} x$ rather than the right hook notation. Shafarevitch uses the terminology convolution, which seems very unfortunate. For $u \in E$, the right hook $z^{*}$ ⌞ $u$ is also denoted $i(u)z^{*}$, and called insertion operator or interior product. This operator plays an important role in differential geometry.
$$Definition 34.12. Let u \in E and z^{*}\in \bigwedge  n+1(E^{*}). If we view z^{*}as an alternating multilinear$$
map in $Alt^{n+1}(E; K)$, then we define $i(u)z^{*} \in Alt^{n}(E; K)$ as given by
$$(i(u)z^{*})(v_{1}, \dots  , v_{n}) = z^{*}(u, v_{1}, \dots  , v_{n}).$$
$$⌟ ⌞p$$
$$n-Usingp E_{*} the left hookp E_{*}andn- thep E right hookwe can define two linear maps \gamma  : \bigwedge  E \to$$
$$\bigwedge  and \delta : \bigwedge  \to \bigwedge  as follows:$$

<!-- PAGE 1260 -->

> **Definition 34.13.** For any basis $(e_{1}, \dots  , e$ ) of $E$, if we let $M = {1, \dots  , n}, e = e_{1}\wedge \cdots \wedge e_{n}$,
$$p En-p E_{*}p E_{*}n-p E$$
$$and e^{*}= e_{1}^{*} \wedge \cdots  \wedge e_{n}^{*}, define \gamma  : \bigwedge  \to \bigwedge^{n}  and \delta : \bigwedge  \to \bigwedge  as$$
$$\gamma (u) = u ⌟e^{*}and\delta (v^{*}) = e ⌞v^{*},$$
$$p p$$
$$for all u \in \bigwedge  E and all v^{*}\in \bigwedge  E^{*}.$$
$$p n-p p n-p$$
$$Proposition 34.23. The  linear maps \gamma  : \bigwedge  E \to \bigwedge  E^{*}and \delta : \bigwedge  E^{*}\to \bigwedge  E are$$
isomorphims, and $\gamma^{-1} = \delta$ . The isomorphisms $\gamma$  and $\delta$  map decomposable vectors to de-
$$p$$
$$composable vectors. Furthermore, if z \in \bigwedge_{p}  E is decomposable, say z = u_{1} \wedge \cdots  \wedge u_{p} for$$
some $u_{i} \in E$, then $\gamma (z) = v_{1}^{*} \wedge \cdots  \wedge v_{n-}^{*}$  for some $v_{j}^{*} \in E^{*}$, and $v_{j}^{*}(u_{i}) = 0$ for all $i, j$. A
$$p$$
$$similar p  propertyn -holdsp  for v^{*} \in \bigwedge_{p}  E^{*}and \delta n(-v^{*}p ). If (e_{1}', \dots  , e_{n}') is any other basis of E and$$
$$\gamma'  : \bigwedge  E \to \bigwedge_{'}  E^{*}and \delta' : \bigwedge  E^{*}\to \bigwedge  E are the corresponding isomorphisms, then$$
$\gamma' = \lambda \gamma$  and $\delta = \lambda^{-1} \delta$  for some nonzero $\lambda  \in K$.

*Proof.* Using Propositions 34.18 and 34.21, for any subset $J \subseteq {1, \dots  , n} = M$ such that |J| $= p$, we have
$$\gamma (e_{J}) = e_{J} ⌟e^{*}= \rho_{M-J,J} e_{M-J}^{*}and\delta (e_{M-J}^{*}) = e ⌞e_{M-J}^{*} = \rho_{M-J,J} e_{J}.$$
Thus,
$$\delta  \circ \gamma (e_{J}) = \rho_{M-J,J} \rho_{M-J,J} e_{J} = e_{J},$$
since $\rho_{M-J,J}  = \pm 1$. A similar result holds for $\gamma  \circ \delta$ . This implies that
$$\delta  \circ \gamma  = idand\gamma  \circ \delta  = id.$$
Thus, $\gamma$  and $\delta$  are inverse isomorphisms.
$$p$$
$$If z \in \bigwedge  E is decomposable, then z = u_{1} \wedge \cdots  \wedge u_{p} where u_{1}, \dots  , u_{p} are linearly inde-$$
pendent since $z \neq  0$, and we can pick a basis of $E$ of the form $(u_{1}, \dots  , u_{n})$. Then the above formulae show that
$$\gamma (z) = \pm u_{p+1}^{*} \wedge \cdots  \wedge u_{n}^{*}.$$
Since $(u_{1}^{*}, \dots  , u_{n}^{*})$ is the dual basis of $(u_{1}, \dots  , u_{n})$, we have $u_{i}^{*} (u_{j}) = \delta_{ij}$ , If $(e_{1}', \dots  , e_{n}')$ is any
$$n$$
$$other basis of E, because \bigwedge  E has dimension 1, we have$$
$$e_{1}' \wedge \cdots  \wedge e_{n}' = \lambda e_{1} \wedge \cdots  \wedge e_{n}$$
for some nonzero $\lambda  \in K$, and the rest is trivial.
$$n-1$$
$$1 E_{*}Applying Proposition 34.23 to the casen where-1 E p = n -1, the isomorphism \gamma  : \bigwedge_{1}  E_{*}E \to$$
$$\bigwedge  maps indecomposable vectors in \bigwedge  to indecomposablen-1  vectors in \bigwedge  = E^{*}.$$
$$But every vector in E^{*}is decomposable, so every vector in \bigwedge  E is decomposable.$$
$$n-1$$
$$Corollary 34.24. If E is a finite-dimensional vector space, then every vector in \bigwedge  E is$$
decomposable.
