# Tensor Products of Modules over a Commutative Ring


<!-- PAGE 1288 -->

## 35.3 Tensor Products of Modules over a

$$Commutative Ring$$
It is possible to define tensor products of modules over a ring, just as in Section 33.2, and the results of this section continue to hold. The results of Section 33.4 also continue to hold since they are based on the universal mapping property. However, the results of Section 33.3 on bases generally fail, except for free modules. Similarly, the results of Section 33.5 on duality generally fail. Tensor algebras can be defined for modules, as in Section 33.6. Symmetric tensor and alternating tensors can be defined for modules but again, results involving bases generally fail. Tensor products of modules have some unexpected properties. For example, if $p$ and $q$ are relatively prime integers, then
$$\mathbb{Z}/p\mathbb{Z} \otimes_{Z} \mathbb{Z}/q\mathbb{Z} = (0).$$
This is because, by Bezout’s identity, there are a, $b \in \mathbb{Z}$ such that
$$ap + bq = 1,$$
so, for all $x \in \mathbb{Z}/p\mathbb{Z}$ and all $y \in \mathbb{Z}/q\mathbb{Z}$, we have
$$x \otimes y = ap(x \otimes y) + bq(x \otimes y)$$
$$= a(px \otimes y) + b(x \otimes qy)$$
$$= a(0 \otimes y) + b(x \otimes 0)$$
$$= 0.$$
It is possible to salvage certain properties of tensor products holding for vector spaces by restricting the class of modules under consideration. For example, projective modules have a pretty good behavior w.r.t. tensor products. A free A-module $F$, is a module that has a basis (i.e., there is a family, $(e_{i})_{i\in I}$, of linearly independent vectors in $F$ that span $F)$. Projective modules have many equivalent characterizations. Here is one that is best suited for our needs:

> **Definition 35.7.** An A-module, $P$, is projective if it is a summand of a free module, that is, if there is a free A-module, $F$, and some A-module, $Q$, so that
$$F = P \oplus Q.$$
Given any A-module, $M$, we let $M^{*} = Hom_{A}(M, A)$ be its dual. We have the following proposition:

> **Proposition 35.11.** For any finitely-generated projective A-modules, $P$, and any A-module, $Q$, we have the isomorphisms:
$$\sim$$
$$P^{**}=P$$
$$\sim  \otimes_{A}$$
$$Hom_{A}(P, Q)=P^{*} Q.$$

<!-- PAGE 1289 -->
Proof sketch. We only consider the second isomorphism. Since $P$ is projective, we have some A-modules, $P_{1}, F$, with
$$P \oplus P_{1} = F,$$
where $F$ is some free module. Now, we know that for any A-modules, $U, V, W$, we have
$$Hom_{A}(U \oplus V, W) \sim = Hom_{A}(U, W) \prod  Hom_{A}(V, W) \sim = Hom_{A}(U, W) \oplus Hom_{A}(V, W),$$
so
$$\oplus   \sim  \oplus  \sim$$
$$P^{*}P_{1}^{*}= F^{*},Hom_{A}(P, Q)Hom_{A}(P_{1}, Q)= Hom_{A}(F, Q).$$
By tensoring with $Q$ and using the fact that tensor distributes w.r.t. coproducts, we get
$$\otimes_{A}  \oplus   \otimes_{A}  \sim \oplus  \otimes_{A}  \sim \otimes_{A}$$
$$(P^{*} Q)(P_{1}^{*} Q)= (P^{*}P_{1}^{*} ) Q= F^{*} Q.$$
Now, the proof of Proposition 33.19 goes through because $F$ is free and finitely generated, so
$$\otimes_{A}  \oplus   \otimes_{A}  \sim \otimes_{A}  \longrightarrow  \sim  \oplus$$
$\alpha_{\otimes}$ : $(P^{*}  Q) (P_{1}^{*}  Q) = F^{*}  Q Hom_{A}(F, Q) = Hom_{A}(P, Q) Hom_{A}(P_{1}, Q)$ is an isomorphism and as $\alpha_{\otimes}$ maps $P^{*} \otimes_{A} Q$ to $Hom_{A}(P, Q)$, it yields an isomorphism between these two spaces.
$$\otimes_{A}  \sim$$
The isomorphism $\alpha_{\otimes}$ : $P^{*}  Q = Hom_{A}(P, Q)$ of Proposition 35.11 is still given by
$$\alpha_{\otimes} (u^{*}\otimes f)(x) = u^{*}(x)f,u^{*}\in P^{*} , f \in Q, x \in P.$$
It is convenient to introduce the evaluation map, $Ev_{x}$ : $P^{*} \otimes_{A}  Q \to Q$, defined for every $x \in P$ by
$$Ev_{x}(u^{*}\otimes f) = u^{*}(x)f,u^{*}\in P^{*} , f \in Q.$$
We will need the following generalization of part $(4)$ of Proposition 33.13.

> **Proposition 35.12.** Given any two families of A-modules $(M_{i})_{i\in I}$ and $(N_{j})_{j\in J}$ (where I and $J$ are finite index sets), we have an isomorphism
$$\begin{pmatrix} MM_{i} \\ i\in I \end{pmatrix} \otimes \begin{pmatrix} MM_{j} \\ j\in I \end{pmatrix} \approx M(M_{i} \otimes N_{j}).$$
$$(i,j)\in I\times J$$
Proposition 35.12 also holds for infinite index sets.

> **Proposition 35.13.** Let $M$ and $N$ be two A-module with $N$ a free module, and pick any basis $(v_{1}, \dots  , v_{n})$ for $N$. Then, every element of $M \otimes N$ can expressed in a unique way as a sum of the form
$$u_{1} \otimes v_{1} + \cdots  + u_{n} \otimes v_{n},u_{i} \in M,$$
so that $M \otimes N$ is isomorphic to $M^{n}$ (as an A-module).

<!-- PAGE 1290 -->

*Proof.* Since $N$ is free with basis $(v_{1}, \dots  , v_{n})$, we have an isomorphism
$$N \approx Av_{1} \oplus \cdots  \oplus Av_{n}.$$
By Proposition 35.12, we obtain an isomorphism
$$M \otimes N \approx M \otimes (Av_{1} \oplus \cdots  \oplus Av_{n}) \approx (M \otimes Av_{1}) \oplus \cdots  \oplus (M \otimes Av_{n}).$$
Because $(v_{1}, \dots  , v_{n})$ is a basis of $N$, each $v_{j}$ is torsion-free so the map $a \mapsto av_{j}$ is an isomorphism of $A$ onto $Av_{j}$, and because $M \otimes A \approx M$, we have the isomorphism
$$M \otimes N \approx (M \otimes A) \oplus \cdots  \oplus (M \otimes A) \approx M \oplus \cdots  \oplus M = M^{n} ,$$
as claimed. Proposition 35.13 also holds for an infinite basis $(v_{j})_{j\in J}$ of $N$. Obviously, a version of Proposition 35.13 also holds if $M$ is free and $N$ is arbitrary. The next proposition will be also be needed.

> **Proposition 35.14.** Given any A-module $M$ and any ideal $\mathfrak{a}$ in $A$, there is an isomorphism
$$(A/\mathfrak{a}) \otimes_{A}  M \approx M/\mathfrak{a} M$$
given by the map $(\overline{a} \otimes u) \mapsto$ au (mod $\mathfrak{a} M)$, for all $\overline{a} \in A/\mathfrak{a}$ and all $u \in M$. Sketch of proof. Consider the map $\phi$ : $(A/\mathfrak{a}) \times  M \to M/\mathfrak{a} M$ given by
$$\phi (\overline{a, u}) = au(\mathrm{mod} \mathfrak{a} M)$$
for all $\overline{a} \in A/\mathfrak{a}$ and all $u \in M$. It is immediately checked that $\phi$  is well-defined because au (mod $\mathfrak{a} M)$ does not depend on the representative $a \in A$ chosen in the equivalence class $\overline{a}$, and $\phi$  is bilinear. Therefore, $\phi$  induces a linear map $\phi$ : $(A/\mathfrak{a}) \otimes M \to M/\mathfrak{a} M$, such that $\phi (\overline{a} \otimes u) =$ au (mod $\mathfrak{a} M)$. We also define the map $\psi$ : $M \to (A/\mathfrak{a}) \otimes M$ by
$$\psi (u\overline{) = 1} \otimes u.$$
Since $\mathfrak{a} M$ is generated by vectors of the form au with $a \in \mathfrak{a}$ and $u \in M$, and since
$$\psi (au\overline{) = 1} \otimes au =\overline{a} \otimes u = 0 \otimes u = 0,$$
we see that $\mathfrak{a} M \subseteq$ Ker $(\psi$ ), so $\psi$  induces a linear map $\psi$ : $M/\mathfrak{a} M \to (A/\mathfrak{a}) \otimes M$. We have
$$\psi (\phi (\overline{a} \otimes u)) = \psi (au)$$
$$\overline{= 1} \otimes au$$
$$=\overline{a} \otimes u$$
