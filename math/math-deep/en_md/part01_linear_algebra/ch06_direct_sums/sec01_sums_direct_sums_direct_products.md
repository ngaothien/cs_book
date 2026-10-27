# Sums, Direct Sums, Direct Products


<!-- PAGE 179 -->
Chapter $6$ Direct Sums In this chapter all vector spaces are defined over an arbitrary field $K$. For the sake of concreteness, the reader may safely assume that $K =\mathbb{R}$.

## 6.1 Sums, Direct Sums, Direct Products

There are some useful ways of forming new vector spaces from older ones, in particular, direct products and direct sums. Regarding direct sums, there is a subtle point, which is that if we attempt to define the direct sum $E$ `F of two vector spaces using the cartesian product $E \times  F$, we don’t quite get the right notion because elements of $E \times  F$ are ordered pairs, but we want $E$ `F $= F$ `E. Thus, we want to think of the elements of $E$ `F as unordrered pairs of elements. It is possible to do so by considering the direct sum of a family $(E_{i})_{i\in {1,2}}$, and more generally of a family $(E_{i})_{i\in I}$. For simplicity, we begin by considering the case where $I = {1, 2}$.

> **Definition 6.1.** Given a family $(E_{i})_{i\in {1,2}}$ of two vector spaces, we define the (external)
$$E$$
direct sum $E_{1}$ `  (or coproduct) of the family $(E_{i})_{i\in {1,2}}$ as the set
$$2$$
$$E_{1}aE_{2} = {{\langle 1, u\rangle , \langle 2, v\rangle } | u \in E_{1}, v \in E_{2}},$$
with addition
$${\langle 1, u_{1}\rangle , \langle 2, v_{1}\rangle } + {\langle 1, u_{2}\rangle , \langle 2, v_{2}\rangle } = {\langle 1, u_{1} + u_{2}\rangle , \langle 2, v_{1} + v_{2}\rangle },$$
and scalar multiplication
$$\lambda {\langle 1, u\rangle , \langle 2, v\rangle } = {\langle 1, \lambda u\rangle , \langle 2, \lambda v\rangle }.$$
$$E E$$
We define the injections $in_{1}$ : $E_{1} \to E_{1}$ `  and $in_{2}$ : $E_{2} \to E_{1}$ `  as the linear maps
$$22$$
defined such that,
$$in_{1}(u) = {\langle 1, u\rangle , \langle 2, 0\rangle },$$
and
$$in_{2}(v) = {\langle 1, 0\rangle , \langle 2, v\rangle }.$$
$$179$$

<!-- PAGE 180 -->
Note that
$$E_{2}aE_{1} = {{\langle 2, v\rangle , \langle 1, u\rangle } | v \in E_{2}, u \in E_{1}} = E_{1}aE_{2}.$$
$$E$$
Thus, every member ${\langle 1, u\rangle , \langle 2, v\rangle$ } of $E_{1}$ `  can be viewed as an unordered pair consisting
$$2$$
of the two vectors $u$ and $v$, tagged with the index $1$ and $2$, respectively.
$$E$$
$$Remark: In fact, E_{1}`2 is just the product \prod_{i}  \in {1,2} E_{i} of the family (E_{i})_{i\in {1,2}}.$$
 This is not to be confused with the cartesian product $E_{1} \times E_{2}$. The vector space $E_{1} \times E_{2}$ is the set of all ordered pairs $\langle u, v\rangle$ , where $u \in E_{1}$, and $v \in E_{2}$, with addition and multiplication by a scalar defined such that
$$\langle u_{1}, v_{1}\rangle + \langle u_{2}, v_{2}\rangle = \langle u_{1} + u_{2}, v_{1} + v_{2}\rangle ,$$
$$\lambda \langle u, v\rangle = \langle \lambda u, \lambda v\rangle .$$
$$There is a bijection between \prod_{i}  E_{i} and E_{1} \times  E_{2}, but as we just saw, elements of$$
$$\prod_{i}  \in { E_{i} are certain sets. The^{\in {1,2}} product E_{1} \times  \cdots  \times  E_{n} of any number of vector spaces$$
$can^{1,2}}$ also be defined. We will do this shortly. The following property holds.
$$E$$

> **Proposition 6.1.** Given any two vector spaces, $E_{1}$ and $E_{2}$, the set $E_{1}$ `  is a vector space. For every pair of linear maps, $f$ : $E_{1} \to G$ and $g: E_{2} \to G$, there is $a^{2}$ unique linear
$$E$$
map, $f + g: E_{1}$ `  $\to G$, such that $(f + g) \circ in_{1} = f$ and $(f + g) \circ in_{2} = g$, as in the following $diagram:^{2}$
$$E_{1}P$$
$$PP$$
$$PP$$
$$PP$$
$$P^{f}P$$
$$inPP$$
$$1PP$$
$$EPP$$
$$P'$$
$$f+g /$$
$$E_{1}`7G$$
$$2\overline{n}\overline{n}$$
$$\overline{n}\overline{n}$$
$$nn$$
$$nn$$
$$innn_{g}$$
$$2nn$$
$$nn$$
$$nn$$
$$E_{2}$$

*Proof.* Define
$$(f + g)({\langle 1, u\rangle , \langle 2, v\rangle }) = f(u) + g(v),$$
for every $u \in E_{1}$ and $v \in E_{2}$. It is immediately verified that $f + g$ is the unique linear map with the required properties.
$$E$$
We already noted that $E_{1}$ `  is in bijection with $E_{1} \times  E_{2}$. If we define the projections
$$E E2$$
$\pi_{1}$  : $E_{1}$ `  $\to E_{1}$ and $\pi_{2}$  : $E_{1}$ `  $\to E_{2}$, such that
$$22$$
$$\pi_{1} ({\langle 1, u\rangle , \langle 2, v\rangle }) = u,$$
and
$$\pi_{2} ({\langle 1, u\rangle , \langle 2, v\rangle }) = v,$$
we have the following proposition.

<!-- PAGE 181 -->

> **Proposition 6.2.** Given any two vector spaces, $E_{1}$ and $E_{2}$, for every pair of linear maps,
$$E$$
$f$ : $D \to E_{1}$ and $g: D \to E_{2}$, there is a unique linear map, $f \times  g: D \to E_{1}$ ` , such that
$$2$$
$\pi_{1}  \circ (f \times  g) = f$ and $\pi_{2}  \circ (f \times  g) = g$, as in the following diagram:
$$7E_{1}$$
$$nn$$
$$nn$$
$$nn$$
$$nn$$
$$n^{f}n\pi 1$$
$$n_{f\times g}n$$
$$nn E$$
$$nn$$
$$D\overline{P} E_{1}`$$
$$\overline{P}\overline{P} 2$$
$$\overline{P}\overline{P}$$
$$PP$$
$$PP$$
$$PP\pi$$
$$gPP2$$
$$PP$$
$$P($$
$$E_{2}$$

*Proof.* Define
$$(f \times  g)(w) = {\langle 1, f(w)\rangle , \langle 2, g(w)\rangle },$$
for every $w \in D$. It is immediately verified that $f \times  g$ is the unique linear map with the required properties.
Remark: It is a peculiarity of linear algebra that direct sums and products of finite families are isomorphic. However, this is no longer true for products and sums of infinite families. When $U, V$ are subspaces of a vector space $E$, letting $i_{1}$ : $U \to E$ and $i_{2}$ : $V \to E$ be the inclusion maps, if $U$ `V is isomomorphic to $E$ under the map $i_{1} + i_{2}$ given by Proposition 6.1, we say that $E$ is a direct sum of $U$ and $V$ , and we write $E = U$ `V (with a slight abuse of notation, since $E$ and $U$ `V are only isomorphic). It is also convenient to define the sum $U_{1} + \cdots  + U_{p}$ and the internal direct sum $U_{1} \oplus \cdots  \oplus U_{p}$ of any number of subspaces of $E$.

> **Definition 6.2.** Given $p \ge 2$ vector spaces $E_{1}, \dots  , E_{p}$, the product $F = E_{1} \times  \cdots  \times  E_{p}$ can be made into a vector space by defining addition and scalar multiplication as follows:
$$(u_{1}, \dots  , u_{p}) + (v_{1}, \dots  , v_{p}) = (u_{1} + v_{1}, \dots  , u_{p} + v_{p})$$
$$\lambda (u_{1}, \dots  , u_{p}) = (\lambda u_{1}, \dots  , \lambda u_{p}),$$
for all $u_{i}, v_{i} \in E_{i}$ and all $\lambda  \in \mathbb{R}$. The zero vector of $E_{1} \times  \cdots  \times  E_{p}$ is the $p$-tuple
$$( 0, \dots  , 0),$$
$$| {z }$$
$$p$$
where the ith zero is the zero vector of $E_{i}$. With the above addition and multiplication, the vector space $F = E_{1} \times  \cdots  \times  E_{p}$ is called the direct product of the vector spaces $E_{1}, \dots  , E_{p}$. As a special case, when $E_{1} = \cdots  = E_{p} =\mathbb{R}$, we find again the vector space $F =\mathbb{R}^{p}$. The projection maps $pr_{i}$ : $E_{1} \times  \cdots  \times  E_{p} \to E_{i}$ given by
$$pr_{i}(u_{1}, \dots  , u_{p}) = u_{i}$$

<!-- PAGE 182 -->
are clearly linear. Similarly, the maps $in_{i}$ : $E_{i} \to E_{1} \times  \cdots  \times  E_{p}$ given by
$$in_{i}(u_{i}) = (0, \dots  , 0, u_{i}, 0, \dots  , 0)$$
are injective and linear. If $dim(E_{i}) = n_{i}$ and if $(e_{1}^{i}, \dots  , e_{ni}^{i})$ is a basis of $E_{i}$ for $i = 1, \dots  , p$, then it is easy to see that the $n_{1} + \cdots  + n_{p}$ vectors
$$(e_{1}^{1}, 0, \dots  , 0),\dots  ,(e_{n1}^{1}, 0, \dots  , 0),$$
$$\vdots \vdots \vdots$$
$$(0, \dots  , 0, e_{1}^{i}, 0, \dots  , 0),\dots  ,(0, \dots  , 0, e_{ni}^{i}, 0, \dots  , 0),$$
$$\vdots \vdots \vdots$$
$$(0, \dots  , 0, e_{1}^{p}),\dots  ,(0, \dots  , 0, e_{np}^{p})$$
form a basis of $E_{1} \times  \cdots  \times  E_{p}$, and so
$$\dim(E_{1} \times  \cdots  \times  E_{p}) = \dim(E_{1}) + \cdots  + \dim(E_{p}).$$
Let us now consider a vector space $E$ and $p$ subspaces $U_{1}, \dots  , U_{p}$ of $E$. We have a map
$$a: U_{1} \times  \cdots  \times  U_{p} \to E$$
given by
$$a(u_{1}, \dots  , u_{p}) = u_{1} + \cdots  + u_{p},$$
with $u_{i} \in U_{i}$ for $i = 1, \dots  , p$. It is clear that this map is linear, and so its image is a subspace of $E$ denoted by
$$U_{1} + \cdots  + U_{p}$$
and called the sum of the subspaces $U_{1}, \dots  , U_{p}$. By definition,
$$U_{1} + \cdots  + U_{p} = {u_{1} + \cdots  + u_{p} | u_{i} \in U_{i}, 1 \le i \le p},$$
and it is immediately verified that $U_{1} + \cdots  + U_{p}$ is the smallest subspace of $E$ containing $U_{1}, \dots  , U_{p}$. This also implies that $U_{1} + \cdots  + U_{p}$ does not depend on the order of the factors $U_{i}$; in particular,
$$U_{1} + U_{2} = U_{2} + U_{1}.$$

> **Definition 6.3.** For any vector space $E$ and any $p \ge 2$ subspaces $U_{1}, \dots  , U_{p}$ of $E$, if the map a defined above is injective, then the sum $U_{1} + \cdots  + U_{p}$ is called a direct sum and it is denoted by
$$U_{1} \oplus \cdots  \oplus U_{p}.$$
The space $E$ is the direct sum of the subspaces $U_{i}$ if
$$E = U_{1} \oplus \cdots  \oplus U_{p}.$$

<!-- PAGE 183 -->
As in the case of a sum, $U_{1} \oplus U_{2} = U_{2} \oplus U_{1}$. If the map a is injective, then by Proposition 3.19 we have Ker $a =$ {( $0, \dots  , 0)}$ where
$$| {z }$$
each $0$ is the zero vector of $E$, which means that if $u_{i} \in U_{i}$ for $i = 1, \dots  , p and^{p}$ if
$$u_{1} + \cdots  + u_{p} = 0,$$
then $(u_{1}, \dots  , u_{p}) = (0, \dots  , 0)$, that is, $u_{1} = 0, \dots  , u_{p} = 0$.

> **Proposition 6.3.** If the map a: $U_{1} \times \cdots \times U_{p} \to E$ is injective, then every $u \in U_{1} +\cdots +U_{p}$ has a unique expression as a sum
$$u = u_{1} + \cdots  + u_{p},$$
with $u_{i} \in U_{i}$, for $i = 1, \dots  , p$.

*Proof.* If
$$u = v_{1} + \cdots  + v_{p} = w_{1} + \cdots  + w_{p},$$
with $v_{i}, w_{i} \in U_{i}$, for $i = 1, \dots  , p$, then we have
$$w_{1} -v_{1} + \cdots  + w_{p} -v_{p} = 0,$$
and since $v_{i}, w_{i} \in U_{i}$ and each $U_{i}$ is a subspace, $w_{i} -v_{i} \in U_{i}$. The injectivity of a implies that $w_{i}-v_{i} = 0$, that is, $w_{i} = v_{i}$ for $i = 1, \dots  , p$, which shows the uniqueness of the decomposition of $u$.

> **Proposition 6.4.** If the map a: $U_{1} \times  \cdots  \times  U_{p} \to E$ is injective, then any $p$ nonzero vectors $u_{1}, \dots  , u_{p}$ with $u_{i} \in U_{i}$ are linearly independent.

*Proof.* To see this, assume that
$$\lambda_{1} u_{1} + \cdots  + \lambda_{p} u_{p} = 0$$
for some $\lambda_{i}  \in \mathbb{R}$. Since $u_{i} \in U_{i}$ and $U_{i}$ is a subspace, $\lambda_{i} u_{i} \in U_{i}$, and the injectivity of a implies that $\lambda_{i} u_{i} = 0$, for $i = 1, \dots  , p$. Since $u_{i} \neq  0$, we must have $\lambda_{i}  = 0$ for $i = 1, \dots  , p$; that is, $u_{1}, \dots  , u_{p}$ with $u_{i} \in U_{i}$ and $u_{i} \neq  0$ are linearly independent. Observe that if a is injective, then we must have $U_{i} \cap U_{j} = (0)$ whenever $i \neq  j$. However,
$$\mathbb{R}^{2}$$
this condition is generally not sufficient if $p \ge 3$. For example, if $E =$ and $U_{1}$ the line spanned by $e_{1} = (1, 0), U_{2}$ is the line spanned by $d = (1, 1)$, and $U_{3}$ is the line spanned by $e_{2} = (0, 1)$, then $U_{1}\cap U_{2} = U_{1}\cap U_{3} = U_{2}\cap U_{3} = {(0, 0)}$, but $U_{1}+U_{2} = U_{1}+U_{3} = U_{2}+U_{3} =\mathbb{R}^{2}$, so $U_{1} + U_{2} + U_{3}$ is not a direct sum. For example, $d$ is expressed in two different ways as
$$d = (1, 1) = (1, 0) + (0, 1) = e_{1} + e_{2}.$$

<!-- PAGE 184 -->
See Figure 6.1.
$$U3U$$
$$2$$
$$e(1,1)$$
$$2$$
$$\overline{e1} U1$$
$$Figure 6.1: The linear subspaces U_{1}, U_{2}, and U_{3} illustrated as lines in \mathbb{R}^{2}.$$
As in the case of a sum, $U_{1} \oplus U_{2} = U_{2} \oplus U_{1}$. Observe that when the map a is injective, then it is a linear isomorphism between $U_{1} \times  \cdots  \times  U_{p}$ and $U_{1} \oplus \cdots  \oplus U_{p}$. The difference is that $U_{1} \times  \cdots  \times  U_{p}$ is defined even if the spaces $U_{i}$ are not assumed to be subspaces of some common space. If $E$ is a direct sum $E = U_{1} \oplus \cdots \oplus U_{p}$, since any $p$ nonzero vectors $u_{1}, \dots  , u_{p}$ with $u_{i} \in U_{i}$ are linearly independent, if we pick a basis $(u_{k})_{k\in Ij}$ in $U_{j}$ for $j = 1, \dots  , p$, then $(u_{i})_{i\in I}$ with $I = I_{1} \cup \cdots  \cup I_{p}$ is a basis of $E$. Intuitively, $E$ is split into $p$ independent subspaces. Conversely, given a basis $(u_{i})_{i\in I}$ of $E$, if we partition the index set $I$ as $I = I_{1} \cup \cdots  \cup I_{p}$, then each subfamily $(u_{k})_{k\in Ij}$ spans some subspace $U_{j}$ of $E$, and it is immediately verified that we have a direct sum
$$E = U_{1} \oplus \cdots  \oplus U_{p}.$$

> **Definition 6.4.** Let $f$ : $E \to E$ be a linear map. For any subspace $U$ of $E$, if f(U) $\subseteq U$ we say that $U$ is invariant under $f$. Assume that $E$ is finite-dimensional, a direct sum $E = U_{1} \oplus \cdots  \oplus U_{p}$, and that each $U_{j}$ is invariant under $f$. If we pick a basis $(u_{i})_{i\in I}$ as above with $I = I_{1} \cup \cdots  \cup I_{p}$ and with each $(u_{k})_{k\in Ij}$ a basis of $U_{j}$, since each $U_{j}$ is invariant under $f$, the image $f(u_{k})$ of every basis vector $u_{k}$ with $k \in I_{j}$ belongs to $U_{j}$, so the matrix $A$ representing $f$ over the basis $(u_{i})_{i\in I}$ is a block diagonal matrix of the form
$$A = \begin{pmatrix} A_{1} \\ A_{2} \\ \ddots \\ A_{p} \end{pmatrix} ,$$

<!-- PAGE 185 -->
with each block $A_{j}$ a $d_{j} \times  d_{j}-matrix$ with $d_{j} = dim(U_{j})$ and all other entries equal to $0$. If $d_{j} = 1$ for $j = 1, \dots  , p$, the matrix $A$ is a diagonal matrix. There are natural injections from each $U_{i}$ to $E$ denoted by $in_{i}$ : $U_{i} \to E$. Now, if $p = 2$, it is easy to determine the kernel of the map a: $U_{1} \times  U_{2} \to E$. We have
$$a(u_{1}, u_{2}) = u_{1} + u_{2} = 0iffu_{1} = -u_{2}, u_{1} \in U_{1}, u_{2} \in U_{2},$$
which implies that
$$\mathrm{Ker} a = {(u, -u) | u \in U_{1} \cap U_{2}}.$$
Now, $U_{1} \cap U_{2}$ is a subspace of $E$ and the linear map $u \mapsto (u, -u)$ is clearly an isomorphism between $U_{1} \cap U_{2}$ and Ker a, so Ker a is isomorphic to $U_{1} \cap U_{2}$. As a consequence, we get the following result:

> **Proposition 6.5.** Given any vector space $E$ and any two subspaces $U_{1}$ and $U_{2}$, the sum $U_{1} + U_{2}$ is a direct sum iff $U_{1} \cap U_{2} = (0)$. An interesting illustration of the notion of direct sum is the decomposition of a square matrix into its symmetric part and its skew-symmetric part. Recall that an $n \times  n$ matrix $A \in M_{n}$ is symmetric if $A^{\top} = A$, skew -symmetric if $A^{\top} = -A$. It is clear that $s$
$$S(n) = {A \in M_{n} | A^{\top}= A}andSkew(n) = {A \in M_{n} | A^{\top}= -A}$$
are subspaces of $M_{n}$, and that S(n) $\cap$ Skew(n) $= (0)$. Observe that for any matrix $A \in M_{n}$, the matrix H(A) $= (A + A^{\top})/2$ is symmetric and the matrix S(A) $= (A$ - $A^{\top})/2$ is skewsymmetric. Since
$$A = H(A) + S(A) = \frac{A + A^{\top}}{2} + \frac{AA^{\top}}{2} -,$$
we see that $M_{n} = S(n)+Skew(n)$, and since $S(n)\cap$ Skew(n) $= (0)$, we have the direct sum
$$M_{n} = S(n) \oplus Skew(n).$$
Remark: The vector space Skew(n) of skew-symmetric matrices is also denoted by $\mathfrak{so}(n)$. It is the Lie algebra of the group SO(n). Proposition 6.5 can be generalized to any $p \ge 2$ subspaces at the expense of notation. The proof of the following proposition is left as an exercise.

> **Proposition 6.6.** Given any vector space $E$ and any $p \ge 2$ subspaces $U_{1}, \dots  , U_{p}$, the following properties are equivalent:
$(1)$ The sum $U_{1} + \cdots  + U_{p}$ is a direct sum.

<!-- PAGE 186 -->
$(2)$ We have
$$U_{i} \cap \begin{pmatrix} U_{j} \\ i \end{pmatrix} \sum_{j=1,j\neq}^{p}  = (0),i = 1, \dots  , p.$$
$(3)$ We have
$$U_{i} \cap \begin{pmatrix} U_{j} \end{pmatrix} \sum_{j=1}^{i-1}  = (0),i = 2, \dots  , p.$$
Because of the isomorphism
$$U_{1} \times  \cdots  \times  U_{p} \approx U_{1} \oplus \cdots  \oplus U_{p},$$
we have

> **Proposition 6.7.** If $E$ is any vector space, for any (finite-dimensional) subspaces $U_{1}, \dots , U_{p}$ of $E$, we have
$$\dim(U_{1} \oplus \cdots  \oplus U_{p}) = \dim(U_{1}) + \cdots  + \dim(U_{p}).$$
If $E$ is a direct sum
$$E = U_{1} \oplus \cdots  \oplus U_{p},$$
since every $u \in E$ can be written in a unique way as
$$u = u_{1} + \cdots  + u_{p}$$
with $u_{i} \in U_{i}$ for $i = 1 \dots  , p$, we can define the maps $\pi_{i}$  : $E \to U_{i}$, called projections, by
$$\pi_{i} (u) = \pi_{i} (u_{1} + \cdots  + u_{p}) = u_{i}.$$
It is easy to check that these maps are linear and satisfy the following properties:
$$($$
$$\pi_{i} if i = j$$
$$\pi_{j}  \circ \pi_{i}  =$$
$$0if i \neq  j,$$
$$\pi_{1}  + \cdots  + \pi_{p}  = id_{E}.$$
For example, in the case of the direct sum
$$M_{n} = S(n) \oplus Skew(n),$$
the projection onto S(n) is given by
$$\pi_{1} (A) = H(A) = \frac{A + A^{\top}}{2} ,$$

<!-- PAGE 187 -->
and the projection onto Skew(n) is given by
$$\pi_{2} (A) = S(A) = \frac{AA^{\top}}{2} -.$$
Clearly, $H(A)+S(A) = A$, H(H(A)) $=$ H(A), S(S(A)) $=$ S(A), and H(S(A)) $=$ S(H(A)) $= 0$. A function $f$ such that $f \circ f = f$ is said to be idempotent. Thus, the projections $\pi_{i}$  are idempotent. Conversely, the following proposition can be shown:

> **Proposition 6.8.** Let $E$ be a vector space. For any $p \ge 2$ linear maps $f_{i}$ : $E \to E$, if
$$($$
$$f_{i}if i = j$$
$$f_{j} \circ f_{i} =$$
$$0if i \neq  j,$$
$$f_{1} + \cdots  + f_{p} = id_{E},$$
then if we let $U_{i} = f_{i}(E)$, we have a direct sum
$$E = U_{1} \oplus \cdots  \oplus U_{p}.$$
We also have the following proposition characterizing idempotent linear maps whose proof is also left as an exercise.

> **Proposition 6.9.** For every vector space $E$, if $f$ : $E \to E$ is an idempotent linear map, i.e., $f \circ f = f$, then we have a direct sum
$$E = \mathrm{Ker} f \oplus \mathrm{Im} f,$$
so that $f$ is the projection onto its image Im $f$. We now give the definition of a direct sum for any arbitrary nonempty index set $I$. First, let us recall the notion of the product of a family $(E )_{\in I}$. Given a family of sets $(E_{i})_{i\in I}$, its
$$product \prod_{i}  E_{i}, is the set of all functions f : I \to \bigcup_{i}^{ii}  E_{i}, such that, f(i) \in E_{i}, for every$$
$i \in$ I. It $is^{\in I}$ one of the many versions of the axiom $of^{\in I}$ choice, that, if $E_{i} \neq  \emptyset$ for every $i \in$ I,
$$then \prod_{i}  E_{i} \neq  \emptyset . A member f \in \prod_{ii}  E_{i}, is often denoted as (f_{i})_{i\in I}. For every i \in I, we$$
$$have the^{\in I} projection \pi_{i}  : \prod_{i}  \in I E_{i} \to E^{\in I}, defined such that, \pi_{i} ((f_{i})_{i\in I}) = f_{i}. We now define$$
direct sums.

> **Definition 6.5.** Let I be any nonempty set, and let $(E_{i})_{i\in I}$ be a family of vector spaces. The (external) direct sum `  $E$  (or coproduct) of the family $(E_{i})_{i\in I}$ is defined as follows:
$$i\in$$
$$`i\in I E_{i} consists of all f \in \prod_{i}^{Ii}  E_{i}, which have finite support, and addition and multi-$$
plication by a scalar are $defined^{\in I}$ as follows:
$$(f_{i})_{i\in I} + (g_{i})_{i\in I} = (f_{i} + g_{i})_{i\in I},$$
$$\lambda (f_{i})_{i\in I} = (\lambda f_{i})_{i\in I}.$$
We also have injection maps $in_{i}$ : $E_{i} \to$ `  $E_{i}$, defined such that, $in_{i}(x) = (f_{i})_{i\in I}$, where
$$i\in I$$
$f_{i} = x$, and $f_{j} = 0$, for all $j \in$ (I $-{i})$.

<!-- PAGE 188 -->
The following proposition is an obvious generalization of Proposition 6.1.

> **Proposition 6.10.** Let I be any nonempty set, let $(E_{i})_{i\in I}$ be a family of vector spaces, and let $G$ be any vector space. The direct sum `  $E_{i}$ is a vector space, and for every family $(h_{i})_{i\in I}$ of linear maps $h_{i}$ : $E_{i} \to G$, there is $a^{i\in I}$ unique linear map
$$\begin{pmatrix} h_{i} \end{pmatrix} \sum_{i\in I}  :aE_{i} \to G,$$
$$i\in I$$
$$such that, ( \sum_{i}  \in I h_{i}) \circ in_{i} = h_{i}, for every i \in I.$$
Remarks:
$(1)$ One might wonder why the direct sum `  $E_{i}$ consists of familes of finite support
$$i\in$$
instead of arbitrary families; in other $words,^{I}$ why didn’t we define the direct sum of
$$the family (E_{i})_{i\in I} as \prod_{i}  E_{i}? The product space \prod_{i}  E_{i} with addition and scalar$$
multiplication defined $as^{\in I}$ above is also a vector $space^{\in I}$ but the problem is that any
$$linear map bh: \prod_{i}  \in I E_{i} \to G such that bh \circ in = h_{i} for all \in I must be given by$$
$$bh((u_{i})_{\in I}) = \sum_{i\in I}^{i}  h_{i}(u_{i}),$$
and if I is infinite, the sum on the right-hand side is infinite, and thus undefined! If I
$$is finite then \prod_{i}  \in I E_{i} and `i\in I E_{i} are isomorphic.$$
$(2)$ When $E_{i} = E$, for all $i \in$ I, we denote `  $E_{i}$ by $E^{(I)}$. In particular, when $E_{i} = K$, for all $i \in$ I, we find the vector space $K^{(I)i\in I}of$ Definition 3.11. We also have the following basic proposition about injective or surjective linear maps.

> **Proposition 6.11.** Let $E$ and $F$ be vector spaces, and let $f$ : $E \to F$ be a linear map. If $f$ : $E \to F$ is injective, then there is a surjective linear map $r: F \to E$ called a retraction, such that $r \circ f = id_{E}$. See Figure 6.2. If $f$ : $E \to F$ is surjective, then there is an injective linear map $s: F \to E$ called a section, such that $f \circ s = id_{F}$. See Figure 6.3.

*Proof.* Let $(u_{i})_{i\in I}$ be a basis of $E$. Since $f$ : $E \to F$ is an injective linear map, by Proposition 3.20, $(f(u_{i}))_{i\in I}$ is linearly independent in $F$. By Theorem 3.8, there is a basis $(v_{j})_{j\in J}$ of $F$, where $I \subseteq J$, and where $v_{i} = f(u_{i})$, for all $i \in$ I. By Proposition 3.20, a linear map $r: F \to E$ can be defined such that $r(v_{i}) = u_{i}$, for all $i \in$ I, and $r(v_{j}) = w$ for all $j \in (J$ - I), where $w$ is any given vector in $E$, say $w = 0$. Since $r(f(u_{i})) = u_{i}$ for all $i \in$ I, by Proposition 3.20, we have $r \circ f = id_{E}$. Now, assume that $f$ : $E \to F$ is surjective. Let $(v_{j})_{j\in J}$ be a basis of $F$. Since $f$ : $E \to F$ is surjective, for every $v_{j} \in F$, there is some $u_{j} \in E$ such that $f(u_{j}) = v_{j}$. Since $(v_{j})_{j\in J}$ is a basis of $F$, by Proposition 3.20, there is a unique linear map $s: F \to E$ such that $s(v_{j}) = u_{j}$. Also, since $f(s(v_{j})) = v_{j}$, by Proposition 3.20 (again), we must have $f \circ s = id_{F}$. The converse of Proposition 6.11 is obvious.
