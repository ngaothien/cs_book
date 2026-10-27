# Tensor Products


<!-- PAGE 1174 -->
$$\mathbb{R}^{2}\mathbb{R}^{2} \mathbb{R}$$
We demonstrate how to calculate tr(f) where $f$ : $\times \to$  with $f((x_{1}, y_{1}), (x_{2}, y_{2})) = x_{1}x_{2}+2x_{2}y_{1}+3x_{1}y_{2}-y_{1}y_{2}$. Under the standard basis $for\mathbb{R}^{2}$, the bilinear form $f$ is represented as
$$\begin{pmatrix} x_{1} & y_{1} \end{pmatrix} \begin{pmatrix} 1 & 3 \\ 2 & -1 \end{pmatrix} \begin{pmatrix} x_{2} \\ y_{2} \end{pmatrix} .$$
Since in the present case $G = I_{2}$, this matrix representation shows that
$$\top$$
$$f^{\natural} = \begin{pmatrix} 1 & 3 \\ 2 & -1 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix} ,$$
and hence
$$\mathrm{tr}(f) = \mathrm{tr}(f^{\natural} ) = \mathrm{tr} \begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix} = 0.$$
We will also need the following proposition to show that various families are linearly independent.

> **Proposition 33.4.** Let $E$ and $F$ be two nontrivial vector spaces and let $(u_{i})_{i\in I}$ be any family of vectors $u_{i} \in E$. The family $(u_{i})_{i\in I}$ is linearly independent iff for every family $(v_{i})_{i\in I}$ of vectors $v_{i} \in F$, there is some linear map $f$ : $E \to F$ so that $f(u_{i}) = v_{i}$ for all $i \in$ I.

*Proof.* Left as an exercise.

## 33.2 Tensor Products

First we define tensor products, and then we prove their existence and uniqueness up to isomorphism.

> **Definition 33.4.** Let $K$ be a given field, and let $E_{1}, \dots  , E_{n}$ be $n \ge 2$ given vector spaces. For any vector space $F$, a map $f$ : $E_{1} \times  \cdots  \times  E_{n} \to F$ is multilinear iff it is linear in each of its argument; that is,
$$f(u_{1}, \dots  u_{i1}, v + w, u_{i+1}, \dots  , u_{n})=f(u_{1}, \dots  u_{i1}, v, u_{i+1}, \dots  , u_{n})$$
$$+ f(u_{1}, \dots  u_{i1}, w, u_{i+1}, \dots  , u_{n})$$
$$f(u_{1}, \dots  u_{i1}, \lambda v, u_{i+1}, \dots  , u_{n})=\lambda f(u_{1}, \dots  u_{i1}, v, u_{i+1}, \dots  , u_{n}),$$
for all $u_{j} \in E_{j} (j \neq  i)$, all $v, w \in E_{i}$ and all $\lambda  \in K$, for $i = 1 \dots  , n$. The set of multilinear maps as above forms a vector space denoted $L(E_{1}, \dots  , E_{n}; F)$ or $Hom(E_{1}, \dots  , E_{n}; F)$. When $n = 1$, we have the vector space of linear maps L(E, $F)$ (also denoted Hom(E, $F))$. (To be very precise, we write $Hom_{K}(E_{1}, \dots  , E_{n}; F)$ and $Hom_{K}(E, F).)$

<!-- PAGE 1175 -->

> **Definition 33.5.** A tensor product of $n \ge 2$ vector spaces $E_{1}, \dots  , E_{n}$ is a vector space $T$ together with a multilinear map $\phi$ : $E_{1} \times  \cdots  \times  E_{n} \to T$, such that for every vector space $F$ and for every multilinear map $f$ : $E_{1}\times \cdots \times E_{n} \to F$, there is a unique linear map $f_{\otimes}: T \to F$ with
$$f(u_{1}, \dots  , u_{n}) = f_{\otimes}(\phi (u_{1}, \dots  , u_{n})),$$
for all $u_{1} \in E_{1}, \dots  , u_{n} \in E_{n}$, or for short
$$f = f_{\otimes}\circ \phi .$$
Equivalently, there is a unique linear map $f_{\otimes}$ such that the following diagram commutes.
$$\phi  /$$
$$E_{1} \times  \cdots  \times  E_{n}T$$
$$NN$$
$$NN$$
$$NN$$
$$NN$$
$$NN$$
$$fN^{f\otimes}&$$
$$F$$
The above property is called the universal mapping property of the tensor product $(T, \phi$ ). We show that any two tensor products $(T_{1}, \phi_{1}$ ) and $(T_{2}, \phi_{2}$ ) for $E_{1}, \dots  , E_{n}$, are isomorphic.

> **Proposition 33.5.** Given any two tensor products $(T_{1}, \phi_{1}$ ) and $(T_{2}, \phi_{2}$ ) for $E_{1}, \dots  , E_{n}$, there is an isomorphism $h: T_{1} \to T_{2}$ such that
$$\phi_{2}  = h \circ \phi_{1} .$$

*Proof.* Focusing on $(T_{1}, \phi_{1}$ ), we have a multilinear map $\phi_{2}$  : $E_{1} \times  \cdots  \times  E_{n} \to T_{2}$, and thus there is a unique linear map $(\phi_{2} )_{\otimes}: T_{1} \to T_{2}$ with
$$\phi_{2}  = (\phi_{2} )_{\otimes}\circ \phi_{1}$$
as illustrated by the following commutative diagram.
$$/$$
$$E_{1} \times  \cdots  \times  E_{n}^{\phi1}T_{1}$$
$$MM$$
$$MM$$
$$MM$$
$$MM(\phi )$$
$$MM2\otimes$$
$$\phi 2MM$$
$$&$$
$$T_{2}$$
Similarly, focusing now on on $(T_{2}, \phi_{2}$ ), we have a multilinear map $\phi_{1}$  : $E_{1} \times  \cdots  \times  E_{n} \to T_{1}$, and thus there is a unique linear map $(\phi_{1} )_{\otimes}: T_{2} \to T_{1}$ with
$$\phi_{1}  = (\phi_{1} )_{\otimes}\circ \phi_{2}$$

<!-- PAGE 1176 -->
as illustrated by the following commutative diagram.
$$/$$
$$E_{1} \times  \cdots  \times  E_{n}^{\phi2}T_{2}$$
$$MM$$
$$MM$$
$$MM$$
$$MM(\phi )$$
$$MM1\otimes$$
$$\phi 1MM$$
$$&$$
$$T_{1}$$
Putting these diagrams together, we obtain the commutative diagrams
$$T_{1}$$
$$q8$$
$$qq$$
$$\phi qq$$
$$q^{1}q$$
$$qq(\phi 2)\otimes$$
$$qq$$
$$/$$
$$E_{1} \times  \cdots  \times  E_{n}^{\phi2}T_{2}$$
$$MM$$
$$MM$$
$$MM$$
$$MM(\phi )$$
$$MM1\otimes$$
$$\phi 1MM$$
$$&$$
$$T_{1}$$
and
$$8T_{2}$$
$$pp$$
$$pp$$
$$pp$$
$$pp(\phi )$$
$$pp^{\phi2}1\otimes$$
$$pp$$
$$E_{1} \times  \cdots  \times  E_{n}^{\phi1} /T_{1}$$
$$NN$$
$$NN$$
$$NN$$
$$NN(\phi )$$
$$\phi NN2\otimes$$
$$2N&$$
$$T_{2},$$
which means that
$$\phi_{1}  = (\phi_{1} )_{\otimes}\circ (\phi_{2} )_{\otimes}\circ \phi_{1} and\phi_{2}  = (\phi_{2} )_{\otimes}\circ (\phi_{1} )_{\otimes}\circ \phi_{2} .$$
On the other hand, focusing on $(T_{1}, \phi_{1}$ ), we have a multilinear map $\phi_{1}$  : $E_{1} \times  \cdots  \times  E_{n} \to T_{1}$, but the unique linear map $h: T_{1} \to T_{1}$ with
$$\phi_{1}  = h \circ \phi_{1}$$
is $h =$ id, as illustrated by the following commutative diagram
$$E_{1} \times  \cdots  \times  E_{n}^{\phi1} /T_{1}$$
$$NN$$
$$NN$$
$$NN$$
$$NNid$$
$$\phi NN$$
$$1N&$$
$$T_{1},$$
and since $(\phi_{1} )_{\otimes} \circ (\phi_{2} )_{\otimes}$ is linear as a composition of linear maps, we must have
$$(\phi_{1} )_{\otimes}\circ (\phi_{2} )_{\otimes}= id.$$

<!-- PAGE 1177 -->
Similarly, we have the commutative diagram
$$E_{1} \times  \cdots  \times  E_{n}^{\phi2} /T_{2}$$
$$NN$$
$$NN$$
$$NN$$
$$NNid$$
$$\phi NN$$
$$2N&$$
$$T_{2},$$
and we must have
$$(\phi_{2} )_{\otimes}\circ (\phi_{1} )_{\otimes}= id.$$
This shows that $(\phi_{1} )_{\otimes}$ and $(\phi_{2} )_{\otimes}$ are inverse linear maps, and thus, $(\phi_{2} )_{\otimes}: T_{1} \to T_{2}$ is an isomorphism between $T_{1}$ and $T_{2}$. Now that we have shown that tensor products are unique up to isomorphism, we give a construction that produces them. Tensor products are obtained from free vector spaces by a quotient process, so let us begin by describing the construction of the free vector space generated by a set. For simplicity assume that our set $I$ is finite, say
$$I = {♥, ♦, ♠, ♣}.$$
The construction works for any field $K$ (and in fact for any commutative ring $A$, in which case we obtain the free A-module generated by I). Assume that $K = \mathbb{R}$. The free vector space generated by I is the set of all formal linear combinations of the form
$$a♥+ b♦+ c♠+ d♣,$$
with a, $b, c, d \in \mathbb{R}$. It is assumed that the order of the terms does not matter. For example,
$$2♥-5♦+ 3♠= -5♦+ 2♥+ 3♠.$$
Addition and multiplication by a scalar are are defined as follows: $(a_{1}♥ + b_{1}♦ + c_{1}♠ + d_{1}♣) + (a_{2}♥ + b_{2}♦ + c_{2}♠ + d_{2}♣)$
$$= (a_{1} + a_{2})♥+ (b_{1} + b_{2})♦+ (c_{1} + c_{2})♠+ (d_{1} + d_{2})♣,$$
and
$$\alpha  \cdot  (a♥+ b♦+ c♠+ d♣) = \alpha a♥+ \alpha b♦+ \alpha c♠+ \alpha d♣,$$
for all a, $b, c, d, \alpha  \in \mathbb{R}$. With these operations, it is immediately verified that we obtain a
$$\mathbb{R}^{(I)} \mathbb{R}^{(I)}$$
vector space denoted . The set $I$ can be viewed as embedded in by the injection $\iota$ given by
$$\iota (♥) = 1♥,\iota (♦) = 1♦,\iota (♠) = 1♠,\iota (♣) = 1♣.$$
$\mathbb{R}^{(I)}$ Thus, can be viewed as the vector space with the special basis $I = {♥$, ♦, ♠, $♣}$. In our $\mathbb{R}^{(I)}  \mathbb{R}^{4}$ case, is isomorophic to .

<!-- PAGE 1178 -->
The exact same construction works for any field $K$, and we obtain a vector space denoted by $K^{(I)}$ and an injection $\iota$ : I $\to K^{(I)}$. The main reason why the free vector space $K^{(I)}$ over a set $I$ is interesting is that it satisfies a universal mapping property. This means that for every vector space $F$ (over the
$$field K), \frac{any}{h} function  h: I \to F, where F is considered just a set, has a unique linear$$
extension : $K^{(I)} \to F$. By extension, we mean that $\overline{h}(i) =$ h(i) for all $i \in$ I, or more rigorously that $h =\overline{h} \circ \iota$ . For example, if $I = {♥$, ♦, ♠, $♣}, K =\mathbb{R}$, and $F =\mathbb{R}^{3}$, the function $h$ given by
$$h(♥) = (1, 1, 1),h) = (1, 1, 0),h(♠) = (1, 0, 0),h(♣) = (0, 0 -1)$$
$$has a unique linear extension \frac{(♦}{h} : \mathbb{R}^{(I)} \mathbb{R}^{3} to the free vector space \mathbb{R}^{(I)}, given by$$
$$\overline{h}(a♥+ b♦+ c♠+ d♣) = \frac{\to}{ah} (♥) +\overline{bh}(♦) +\overline{ch}(♠) +\overline{dh}(♣)$$
$$= ah(♥) + bh(♦) + ch(♠) + dh(♣)$$
$$= a(1, 1, 1) + b(1, 1, 0) + c(1, 0, 0) + d(0, 0, -1)$$
$$= (a + b + c, a + b, a -d).$$
To generalize the construction of a free vector space to infinite sets I, we observe that the formal linear combination a♥ $+$ b♦ $+$ c♠ $+$ d♣ can be viewed as the function $f$ : I $\to \mathbb{R}$ given by
$$f(♥) = a,f(♦) = b,f(♠) = c,f(♣) = d,$$
where a, $b, c, d \in \mathbb{R}$. More generally, we can replace $\mathbb{R}$ by any field $K$. If I is finite, then the set of all such functions is a vector space under pointwise addition and pointwise scalar multiplication. If I is infinite, since addition and scalar multiplication only makes sense for finite vectors, we require that our functions $f$ : I $\to K$ take the value $0$ except for possibly finitely many arguments. We can think of such functions as an infinite sequences $(f_{i})_{i\in I}$ of elements $f_{i}$ of $K$ indexed by I, with only finitely many nonzero $f_{i}$. The formalization of this construction goes as follows. Given any set $I$ viewed as an index set, let $K^{(I)}$ be the set of all functions $f$ : I $\to K$ such that f(i) $\neq  0$ only for finitely many $i \in$ I. As usual, denote such a function by $(f_{i})_{i\in I}$; it is a family of finite support. We make $K^{(I)}$ into a vector space by defining addition and scalar multiplication by
$$(f_{i}) + (g_{i})=(f_{i} + g_{i})$$
$$\lambda (f_{i})=(\lambda f_{i}).$$
The family $(e_{i})_{i\in I}$ is defined such that $(e_{i})_{j} = 0$ if j̸ $= i$ and $(e_{i})_{i} = 1$. It is a basis of the vector space $K^{(I)}$, so that every $w \in K^{(I)}$ can be uniquely written as a finite linear combination of the $e_{i}$. There is also an injection $\iota$ : I $\to K^{(I)}$ such that $\iota (i) = e_{i}$ for every $i \in$ I. Furthermore, it is easy to show that for any vector space $F$, and for any function

<!-- PAGE 1179 -->
$h$: I $\to F$, there is a unique linear map $\overline{h}: K^{(I)} \to F$ such that $h =\overline{h} \circ \iota$ , as in the following diagram.
$$I /K^{(I)}$$
$$\overline{C}\overline{C}^{\iota}$$
$$\overline{C} C$$
$$CC$$
$$CC$$
$$hC^{h}!$$
$$F$$

> **Definition 33.6.** The vector space $(K^{(I)}, \iota$ ) constructed as above from a set $I$ is called the free vector space generated by I (or over I). The commutativity of the above diagram is called the universal mapping property of the free vector space $(K^{(I)}, \iota$ ) over I. Using the proof technique of Proposition 33.5, it is not hard to prove that any two vector spaces satisfying the above universal mapping property are isomorphic. We can now return to the construction of tensor products. For simplicity consider two vector spaces $E_{1}$ and $E_{2}$. Whatever $E_{1} \otimes E_{2}$ and $\phi$ : $E_{1} \times  E_{2} \to E_{1} \otimes E_{2}$ are, since $\phi$  is supposed to be bilinear, we must have
$$\phi (u_{1} + u_{2}, v_{1}) = \phi (u_{1}, v_{1}) + \phi (u_{2}, v_{1})$$
$$\phi (u_{1}, v_{1} + v_{2}) = \phi (u_{1}, v_{1}) + \phi (u_{1}, v_{2})$$
$$\phi (\lambda u_{1}, v_{1}) = \lambda \phi (u_{1}, v_{1})$$
$$\phi (u_{1}, \mu v_{1}) = \mu \phi (u_{1}, v_{1})$$
for all $u_{1}, u_{2} \in E_{1}$, all $v_{1}, v_{2} \in E_{2}$, and all $\lambda , \mu  \in K$. Since $E_{1} \otimes E_{2}$ must satisfy the universal mapping property of Definition 33.5, we may want to define $E_{1} \otimes E_{2}$ as the free vector space $K^{(E1\times E2)}$ generated by $I = E_{1} \times E_{2}$ and let $\phi$  be the injection of $E_{1} \times E_{2}$ into $K^{(E1\times E2)}$. The problem is that in $K^{(E1\times E2)}$, vectors such that
$$(u_{1} + u_{2}, v_{1})and(u_{1}, v_{1}) + (u_{2}, v_{2})$$
are different, when they should really be the same, since $\phi$  is bilinear. Since $K^{(E1\times E2)}$ is free, there are no relations among the generators and this vector space is too big for our purpose. The remedy is simple: take the quotient of the free vector space $K^{(E1\times E2)}$ by the subspace $N$ generated by the vectors of the form
$$(u_{1} + u_{2}, v_{1}) -(u_{1}, v_{1}) -(u_{2}, v_{1})$$
$$(u_{1}, v_{1} + v_{2}) -(u_{1}, v_{1}) -(u_{1}, v_{2})$$
$$(\lambda u_{1}, v_{1}) -\lambda (u_{1}, v_{1})$$
$$(u_{1}, \mu v_{1}) -\mu (u_{1}, v_{1}).$$
Then, if we let $E_{1} \otimes E_{2}$ be the quotient space $K^{(E1\times E2)}/N$ and let $\phi$  be the quotient map, this forces $\phi$  to be bilinear. Checking that $(K^{(E1\times E2)}/N, \phi$ ) satisfies the universal mapping property is straightforward. Here is the detailed construction.

<!-- PAGE 1180 -->

> **Theorem 33.6.** Given $n \ge 2$ vector spaces $E_{1}, \dots  , E_{n}$, a tensor product $(E_{1} \otimes \cdots  \otimes E_{n}, \phi$ ) for $E_{1}, \dots  , E_{n}$ can be constructed. Furthermore, denoting $\phi (u_{1}, \dots  , u_{n})$ as $u_{1} \otimes \cdots  \otimes u_{n}$, the tensor product $E_{1} \otimes \cdots  \otimes E_{n}$ is generated by the vectors $u_{1} \otimes \cdots  \otimes u_{n}$, where $u_{1} \in E_{1}, \dots  , u_{n} \in E_{n}$, and for every multilinear map $f$ : $E_{1} \times  \cdots  \times  E_{n} \to F$, the unique linear map $f_{\otimes}: E_{1} \otimes \cdots  \otimes E_{n} \to F$ such that $f = f_{\otimes} \circ \phi$  is defined by
$$f_{\otimes}(u_{1} \otimes \cdots  \otimes u_{n}) = f(u_{1}, \dots  , u_{n})$$
on the generators $u_{1} \otimes \cdots  \otimes u_{n}$ of $E_{1} \otimes \cdots  \otimes E_{n}$.

*Proof.* First we apply the construction of a free vector space to the cartesian product $I = E_{1}\times \cdots \times E_{n}$, obtaining the free vector space $M = K^{(I)}$ on $I = E_{1}\times \cdots \times E_{n}$. Since every basis generator $e_{i} \in M$ is uniquely associated with some $n$-tuple $i = (u_{1}, \dots  , u_{n}) \in E_{1} \times  \cdots  \times  E_{n}$, we denote $e_{i}$ by $(u_{1}, \dots  , u_{n})$. Next let $N$ be the subspace of $M$ generated by the vectors of the following type:
$$(u_{1}, \dots  , u_{i} + v_{i}, \dots  , u_{n}) -(u_{1}, \dots  , u_{i}, \dots  , u_{n}) -(u_{1}, \dots  , v_{i}, \dots  , u_{n}),$$
$$(u_{1}, \dots  , \lambda u_{i}, \dots  , u_{n}) -\lambda (u_{1}, \dots  , u_{i}, \dots  , u_{n}).$$
We let $E_{1} \otimes \cdots  \otimes E_{n}$ be the quotient $M/N$ of the free vector space $M$ by $N, \pi$ : $M \to M/N$ be the quotient map, and set
$$\phi  = \pi  \circ \iota .$$
By construction, $\phi$  is multilinear, and since $\pi$  is surjective and the $\iota (i) = e_{i}$ generate $M$, the fact that each $i$ is of the form $i = (u_{1}, \dots  , u_{n}) \in E_{1} \times  \cdots  \times  E_{n}$ implies that $\phi (u_{1}, \dots  , u_{n})$ generate $M/N$. Thus, if we denote $\phi (u_{1}, \dots  , u_{n})$ as $u_{1} \otimes \cdots  \otimes u_{n}$, the space $E_{1} \otimes \cdots  \otimes E_{n}$ is generated by the vectors $u_{1} \otimes \cdots  \otimes u_{n}$, with $u_{i} \in E_{i}$. It remains to show that $(E_{1} \otimes \cdots  \otimes E_{n}, \phi$ ) satisfies the universal mapping property. To this end, we begin by proving there is a map $h$ such that $f = h \circ \phi$ . Since $M = K^{(E1\times \cdot \cdot \cdot \times En)}$ is free on $I = E_{1} \times  \cdots  \times  E_{n}$, there is a unique linear map $\overline{f}\overline{:} K^{(E1\times \cdot \cdot \cdot \times En)} \to F$, such that
$$f =\overline{f} \circ \iota ,$$
as in the diagram below.
$$\iota  /$$
$$E_{1} \times  \cdots  \times  E_{n}K^{(E1\times \cdot \cdot \cdot \times En)}= M$$
$$SSS$$
$$SSS$$
$$SSS$$
$$SSS\overline{f}$$
$$SSS$$
$$fSSS$$
$$)$$
$$F$$
Because $f$ is multilinear, note that we must have $\overline{f}(w) = 0$ for every $w \in N$; for example, on the generator
$$(u_{1}, \dots  , u_{i} + v_{i}, \dots  , u_{n}) -(u_{1}, \dots  , u_{i}, \dots  , u_{n}) -(u_{1}, \dots  , v_{i}, \dots  , u_{n})$$

<!-- PAGE 1181 -->
we have
$$\overline{f}((u_{1}, \dots  , u_{i} + v_{i}, \dots  , u_{n}) -(u_{1}, \dots  , u_{i}, \dots  , u_{n}) -(u_{1}, \dots  , v_{i}, \dots  , u_{n}))$$
$$= f(u_{1}, \dots  , u_{i} + v_{i}, \dots  , u_{n}) -f(u_{1}, \dots  , u_{i}, \dots  , u_{n}) -f(u_{1}, \dots  , v_{i}, \dots  , u_{n})$$
$$= f(u_{1}, \dots  , u_{i}, \dots  , u_{n}) + f(u_{1}, \dots  , v_{i}, \dots  , u_{n}) -f(u_{1}, \dots  , u_{i}, \dots  , u_{n})$$
$$-f(u_{1}, \dots  , v_{i}, \dots  , u_{n})$$
$$= 0.$$
$$But then, \overline{f}\overline{:} M \to F \frac{factors}{f} through M/N, which means that there is a unique linear map$$
$h: M/N \to F$ such that  $= h \circ \pi$  making the following diagram commute
$$M /M/N$$
$$\overline{E}^{\pi}\overline{E}$$
$$\overline{E} E$$
$$EE$$
$$EE$$
$$\overline{f} E^{h}"$$
$$F,$$
$$by defining h([z]) = \overline{f}(z) for \frac{every}{f} z \in M, where [z] denotes the equivalence class in M/N$$
of $z \in M$. Indeed, the fact that  vanishes on $N$ insures that $h$ is well defined on $M/N$, and it is clearly linear by definition. Since $f =\overline{f} \circ \iota$ , from the equation $\overline{f} = h \circ \pi$ , by composing on the right with $\iota$ , we obtain
$$f =\overline{f} \circ \iota  = h \circ \pi  \circ \iota  = h \circ \phi ,$$
as in the following commutative diagram.
$$K$$
$$m^{\times \cdot \cdot \cdot \times En)}6RR$$
$$mm^{(E1}RR$$
$$mmRR$$
$$mmR^{\pi}R$$
$$m^{\iota}mRR$$
$$mRR$$
$$mmRR$$
$$mm($$
$$E_{1} \times  \cdots  \times  E_{n}\overline{f} K^{(E1\times \cdot \cdot \cdot \times En)}/N$$
$$RRllllllllllllll$$
$$RR$$
$$RR$$
$$RR$$
$$RR$$
$$RR$$
$$fRRh$$
$$R(ul$$
$$F$$
We now prove the uniqueness of $h$. For any linear map $f_{\otimes}: E_{1} \otimes \cdots  \otimes E_{n} \to F$ such that $f = f_{\otimes} \circ \phi$ , since the vectors $u_{1} \otimes \cdots  \otimes u_{n}$ generate $E_{1} \otimes \cdots  \otimes E_{n}$ and since $\phi (u_{1}, \dots  , u_{n}) = u_{1} \otimes \cdots  \otimes u_{n}$, the map $f_{\otimes}$ is uniquely defined by
$$f_{\otimes}(u_{1} \otimes \cdots  \otimes u_{n}) = f(u_{1}, \dots  , u_{n}).$$
Since $f = h \circ \phi$ , the map $h$ is unique, and we let $f_{\otimes} = h$. The map $\phi$  from $E_{1} \times  \cdots  \times  E_{n}$ to $E_{1} \otimes \cdots  \otimes E_{n}$ is often denoted by $\iota_{\otimes}$ , so that
$$\iota_{\otimes} (u_{1}, \dots  , u_{n}) = u_{1} \otimes \cdots  \otimes u_{n}.$$

<!-- PAGE 1182 -->
What is important about Theorem 33.6 is not so much the construction itself but the fact that it produces a tensor product with the universal mapping property with respect to multilinear maps. Indeed, Theorem 33.6 yields a canonical isomorphism
$$\otimes \cdots  \otimes  \sim$$
$$L(E_{1}E_{n}, F)= L(E_{1}, \dots  , E_{n}; F)$$
between the vector space of linear maps $L(E_{1} \otimes \cdots  \otimes E_{n}, F)$, and the vector space of multilinear maps $\mathcal{L}(E_{1}, \dots  , E_{n}; F)$, via the linear map $-\circ \phi$  defined by
$$h \mapsto h \circ \phi ,$$
where $h \in L(E_{1} \otimes \cdots  \otimes E_{n}, F)$. Indeed, $h \circ \phi$  is clearly multilinear, and since by Theorem 33.6, for every multilinear map $f \in L(E_{1}, \dots  , E_{n}; F)$, there is a unique linear map $f_{\otimes} \in L(E_{1} \otimes \cdots  \otimes E_{n}, F)$ such that $f = f_{\otimes} \circ \phi$ , the map $-\circ \phi$  is bijective. As a matter of fact, its inverse is the map
$$f \mapsto f_{\otimes}.$$
We record this fact as the following proposition.

> **Proposition 33.7.** Given a tensor product $(E_{1} \otimes \cdots  \otimes E_{n}, \phi$ ), the linear map $h \mapsto h \circ \phi$  is a canonical isomorphism
$$\otimes \cdots  \otimes  \sim$$
$$L(E_{1}E_{n}, F)= L(E_{1}, \dots  , E_{n}; F)$$
between the vector space of linear maps $L(E_{1}\otimes \cdots \otimes E_{n}, F)$, and the vector space of multilinear maps $\mathcal{L}(E_{1}, \dots  , E_{n}; F)$. Using the “Hom” notation, the above canonical isomorphism is written
$$\otimes \cdots  \otimes  \sim$$
$$Hom(E_{1}E_{n}, F)= Hom(E_{1}, \dots  , E_{n}; F).$$
Remarks:
$(1)$ To be very precise, since the tensor product depends on the field $K$, we should subscript the symbol $\otimes$ with $K$ and write
$$E_{1} \otimes_{K}  \cdots  \otimes_{K}  E_{n}.$$
However, we often omit the subscript $K$ unless confusion may arise.
$(2)$ For $F = K$, the base field, Proposition 33.7 yields a canonical isomorphism between the vector space $L(E_{1} \otimes \cdots  \otimes E_{n}, K)$, and the vector space of multilinear forms $\mathcal{L}(E_{1}, \dots  , E_{n}; K)$. However, $L(E_{1} \otimes \cdots \otimes E_{n}, K)$ is the dual space $(E_{1} \otimes \cdots \otimes E_{n})^{*}$, and thus the vector space of multilinear forms $\mathcal{L}(E_{1}, \dots  , E_{n}; K)$ is canonically isomorphic to $(E_{1} \otimes \cdots  \otimes E_{n})^{*}$. Since this isomorphism is used often, we record it as the following proposition.

<!-- PAGE 1183 -->

> **Proposition 33.8.** Given a tensor product $E_{1} \otimes \cdots \otimes E_{n}$,, there is a canonical isomorphism
$$\sim  \otimes \cdots  \otimes$$
$$L(E_{1}, \dots  , E_{n}; K)= (E_{1}E_{n})^{*}$$
between the vector space of multilinear maps $\mathcal{L}(E_{1}, \dots  , E_{n}; K)$ and the dual $(E_{1} \otimes \cdots  \otimes E_{n})^{*}$ of the tensor product $E_{1} \otimes \cdots  \otimes E_{n}$. The fact that the map $\phi$ : $E_{1} \times  \cdots  \times  E_{n} \to E_{1} \otimes \cdots  \otimes E_{n}$ is multilinear, can also be expressed as follows: $u_{1} \otimes \cdots  \otimes (v_{i} + w_{i}) \otimes \cdots  \otimes u_{n} = (u_{1} \otimes \cdots  \otimes v_{i} \otimes \cdots  \otimes u_{n}) + (u_{1} \otimes \cdots  \otimes w_{i} \otimes \cdots  \otimes u_{n}), u_{1} \otimes \cdots  \otimes (\lambda u_{i}) \otimes \cdots  \otimes u_{n} = \lambda (u_{1} \otimes \cdots  \otimes u_{i} \otimes \cdots  \otimes u_{n})$. Of course, this is just what we wanted!

> **Definition 33.7.** Tensors in $E_{1} \otimes \cdots  \otimes E_{n}$ are called n-tensors, and tensors of the form $u_{1} \otimes \cdots  \otimes u_{n}$, where $u_{i} \in E_{i}$ are called simple (or decomposable) n-tensors. Those n-tensors that are not simple are often called compound n-tensors. Not only do tensor products act on spaces, but they also act on linear maps (they are functors).

> **Proposition 33.9.** Given two linear maps $f$ : $E \to$ E' and $g: F \to$ F', there is a unique linear map
$$f \otimes g: E \otimes F \to E'\otimes F'$$
such that
$$(f \otimes g)(u \otimes v) = f(u) \otimes g(v),$$
for all $u \in E$ and all $v \in F$.

*Proof.* We can define $h: E \times  F \to$ E' $\otimes$ F' by
$$h(u, v) = f(u) \otimes g(v).$$
It is immediately verified that $h$ is bilinear, and thus it induces a unique linear map
$$f \otimes g: E \otimes F \to E'\otimes F'$$
making the following diagram commutes
$$\iota \otimes  /$$
$$E \times  FE \otimes F$$
$$L\overline{L}$$
$$\overline{L} L$$
$$LL$$
$$LLf\otimes g$$
$$hLL$$
$$&$$
$$E'\otimes F',$$
such that $(f \otimes$ g)(u $\otimes v) =$ f(u) $\otimes$ g(v), for all $u \in E$ and all $v \in F$.

<!-- PAGE 1184 -->

> **Definition 33.8.** The linear map $f \otimes g: E \otimes F \to$ E' $\otimes$ F' given by Proposition 33.9 is called the tensor product of $f$ : $E \to$ E' and $g: F \to$ F'. Another way to define $f \otimes g$ proceeds as follows. Given two linear maps $f$ : $E \to$ E' and $g: F \to$ F', the map $f \times  g$ is the linear map from $E \times  F$ to E' $\times$  F' given by
$$(f \times  g)(u, v) = (f(u), g(v)),for all u \in E and all v \in F.$$
Then the map $h$ in the proof of Proposition 33.9 is given by $h = \iota_{\otimes}' \circ (f \times  g)$, and $f \otimes g$ is the unique linear map making the following diagram commute.
$$\iota \otimes  /$$
$$E \times  FE \otimes F$$
$$f\times gf\otimes g$$
$$/$$
$$E'\times  F_{\iota'}'E'\otimes F'$$
$$\otimes$$
Remark: The notation $f \otimes g$ is potentially ambiguous, because Hom(E, $F)$ and Hom(E', F' ) are vector spaces, so we can form the tensor product Hom(E, $F)\otimes$ Hom(E', F' ) which contains elements also denoted $f \otimes g$. To avoid confusion, the first kind of tensor product of linear maps defined in Proposition 33.9 (which yields a linear map in Hom(E $\otimes F$, E' $\otimes$ F')) can be denoted by T(f, $g)$. If we denote the tensor product $E \otimes F$ by T(E, $F)$, this notation makes it clearer that $T$ is a bifunctor. If $E$, E' and $F$, F' are finite dimensional, by picking bases it is not hard to show that the map induced by $f \otimes g \mapsto$ T(f, $g)$ is an isomorphism
$$\sim$$
$$Hom(E, F) \otimes Hom(E', F')= Hom(E \otimes F, E'\otimes F').$$

> **Proposition 33.10.** Suppose we have linear maps $f$ : $E \to$ E', $g: F \to$ F', f': E' $\to$ E'' and g': F' $\to$ F''. Then the following identity holds:
$$(f'\circ f) \otimes (g'\circ g) = (f'\otimes g') \circ (f \otimes g).(*)$$

*Proof.* We have the commutative diagram
$$\iota \otimes  /$$
$$E \times  FE \otimes F$$
$$f\times gf\otimes g$$
$$\iota '$$
$$E'\times  F' \otimes  E'/\otimes F'$$
$$f'\times g'f'\otimes g'$$
$$/$$
$$E''\times  F''E''\otimes F'',$$
$$\overline{\iota}\overline{''}$$
$$\otimes$$
and thus the commutative diagram.
$$\iota \otimes  /$$
$$E \times  FE \otimes F$$
$$(f'\times g')\circ (f\times g)(f'\otimes g')\circ (f\otimes g)$$
$$/$$
$$E''\times  F_{\iota''}''E''\otimes F''$$
$$\otimes$$

<!-- PAGE 1185 -->
We also have the commutative diagram.
$$\iota \otimes  /$$
$$E \times  FE \otimes F$$
$$(f'\circ f)\times (g'\circ g)(f'\circ f)\otimes (g'\circ g)$$
$$/$$
$$E''\times  F''E''\otimes F''.$$
$$\overline{\iota}\overline{''}$$
$$\otimes$$
Since we immediately verify that
$$(f'\circ f) \times  (g'\circ g) = (f'\times  g') \circ (f \times  g),$$
by uniqueness of the map between $E \otimes F$ and E'' $\otimes$ F'' in the above diagram, we conclude that
$$(f'\circ f) \otimes (g'\circ g) = (f'\otimes g') \circ (f \otimes g),$$
as claimed. The above formula (*) yields the following useful fact.

> **Proposition 33.11.** If $f$ : $E \to$ E' and $g: F \to$ F' are isomorphisms, then $f \otimes g: E \otimes F \to$ E' $\otimes$ F' is also an isomorphism.

*Proof.* If $f^{-1}$: E' $\to E$ is the inverse of $f$ : $E \to$ E' and $g^{-1}$: F' $\to F$ is the inverse of $g: F \to$ F' , then $f^{-1} \otimes g^{-1}$: E' $\otimes$ F' $\to E \otimes F$ is the inverse of $f \otimes g: E \otimes F \to$ E' $\otimes$ F', which is shown as follows:
$$(f \otimes g) \circ (f^{-1}\otimes g^{-1}) = (f \circ f^{-1}) \otimes (g \circ g^{-1})$$
$$= id_{E'} \otimes id_{F'}$$
$$= id_{E'\otimes F'},$$
and
$$(f^{-1}\otimes g^{-1}) \circ (f \otimes g) = (f^{-1}\circ f) \otimes (g^{-1}\circ g)$$
$$= id_{E} \otimes id_{F}$$
$$= id_{E\otimes F}.$$
Therefore, $f \otimes g: E \otimes F \to$ E' $\otimes$ F' is an isomorphism. The generalization to the tensor product $f_{1} \otimes \cdots  \otimes f_{n}$ of $n \ge 3$ linear maps $f_{i}$ : $E_{i} \to F_{i}$ is immediate, and left to the reader.
