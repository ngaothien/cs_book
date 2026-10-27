# Modules over a Commutative Ring


<!-- PAGE 1273 -->
Chapter $35$ Introduction to Modules; Modules over a PID

## 35.1 Modules over a Commutative Ring

In this chapter we introduce modules over a commutative ring (with unity). After a quick overview of fundamental concepts such as free modules, torsion modules, and some basic results about them, we focus on finitely generated modules over a PID and we prove the structure theorems for this class of modules (invariant factors and elementary divisors). Our main goal is not to give a comprehensive exposition of modules, but instead to apply the structure theorem to the K[X]-module $E_{f}$ defined by a linear map $f$ acting on a finite-dimensional vector space $E$, and to obtain several normal forms for $f$, including the rational canonical form. A module is the generalization of a vector space $E$ over a field $K$ obtained replacing the field $K$ by a commutative ring $A$ (with unity $1)$. Although formally the definition is the same, the fact that some nonzero elements of $A$ are not invertible has some serious consequences. For example, it is possible that $\lambda  \cdot  u = 0$ for some nonzero $\lambda  \in A$ and some nonzero $u \in E$, and a module may no longer have a basis. For the sake of completeness, we give the definition of a module, although it is the same as Definition 3.1 with the field $K$ replaced by a ring $A$. In this chapter, all rings under consideration are assumed to be commutative and to have an identity element $1$.

> **Definition 35.1.** Given a ring $A$, a (left) module over $A$ (or A-module) is a set $M$ (of vectors) together with two operations $+: M \times M \to M$ (called vector $addition),^{1}$ and $\cdot$ : $A\times M \to M$ (called scalar multiplication) satisfying the following conditions for all $\alpha , \beta  \in A$ and all $u, v \in M$;
(M0) $M$ is an abelian group w.r.t. $+$, with identity element $0; \overline{1}\overline{The} \overline{symbol} \overline{+} \overline{is} \overline{overloaded,} \overline{since} \overline{it} \overline{denotes}$ both addition in the ring $A$ and addition of vectors in $M$. It is usually clear from the context which $+$ is intended.
$$1273$$

<!-- PAGE 1274 -->
(M1) $\alpha  \cdot  (u + v) = (\alpha  \cdot  u) + (\alpha  \cdot  v)$;
(M2) $(\alpha  + \beta$ ) $\cdot  u = (\alpha  \cdot  u) + (\beta  \cdot  u)$;
(M3) $(\alpha$  * $\beta$ ) $\cdot  u = \alpha  \cdot  (\beta  \cdot  u)$;
(M4) $1 \cdot  u = u$. Given $\alpha  \in A$ and $v \in M$, the element $\alpha  \cdot  v$ is also denoted by $\alpha v$. The ring $A$ is often called the ring of scalars. Unless specified otherwise or unless we are dealing with several different rings, in the rest of this chapter, we assume that all A-modules are defined with respect to a fixed ring $A$. Thus, we will refer to a A-module simply as a module. From (M0), a module always contains the null vector $0$, and thus is nonempty. From (M1), we get $\alpha  \cdot  0 = 0$, and $\alpha  \cdot  (-v) = -(\alpha  \cdot  v)$. From (M2), we get $0 \cdot  v = 0$, and $(-\alpha$ ) $\cdot  v = -(\alpha  \cdot  v)$. The ring $A$ itself can be viewed as a module over itself, addition of vectors being addition in the ring, and multiplication by a scalar being multiplication in the ring. When the ring $A$ is a field, an A-module is a vector space. When $A =\mathbb{Z}, a \mathbb{Z}-module$ is just an abelian group, with the action given by
$$0 \cdot  u = 0,$$
$$n \cdot  u = u + \cdots  + u,n > 0$$
$$|{z}$$
$$n$$
$$n \cdot  u = -(-n) \cdot  u,n < 0.$$
All definitions from Section 3.4, linear combinations, linear independence and linear dependence, subspaces renamed as submodules, apply unchanged to modules. Proposition 3.6 also holds for the module spanned by a set of vectors. The definition of a basis (Definition 3.6) also applies to modules, but the only result from Section 3.5 that holds for modules is Proposition 3.14. Unfortunately, it is longer true that every module has a basis. For example, for any nonzero integer $n \in \mathbb{Z}$, the $\mathbb{Z}-module \mathbb{Z}/n\mathbb{Z}$ has no basis since $n \cdot \overline{x} = 0$ for all $\overline{x} \in \mathbb{Z}/n\mathbb{Z}$. Similarly, $\mathbb{Q}$, as $a \mathbb{Z}-module$, has no basis. Any two distinct nonzero elements $p_{1}/q_{1}$ and $p_{2}/q_{2}$ are linearly dependent, since
$$(p_{2}q_{1}) \begin{pmatrix} p_{1} \\ q_{1} \end{pmatrix} -(p_{1}q_{2}) \begin{pmatrix} p_{2} \\ q_{2} \end{pmatrix} = 0.$$
Furthermore, the $\mathbb{Z}-module \mathbb{Q}$ is not finitely generated. For if ${p_{1}/q_{1}, \cdots  p_{n}/q_{n}} \subset \mathbb{Q}$ generated $\mathbb{Q}$, then for any $x = r/s \in \mathbb{Q}$, we have
$$c_{1} \frac{p_{1}}{q_{1}} + \cdots  + c_{n} \frac{p_{n}}{q_{n}} = \frac{r}{s} ,$$

<!-- PAGE 1275 -->
where $c_{i} \in \mathbb{Z}$ for $i = 1, \dots  , n$. The left hand side of the preceding line is equivalent to
$$\frac{c_{1}p_{1}q_{2} q_{n} + + c_{n}p_{n}q_{1} q_{n-1}}{q_{1}q_{2} \cdots  q_{n}} \cdots  \cdots  \cdots ,$$
where the numerator is an element of the ideal in $\mathbb{Z}$ spanned by $(c_{1}, c_{2}, \cdots  , c_{n})$. Since $\mathbb{Z}$ is a PID, there exists $a \in \mathbb{Z}$ such that (a) is the ideal spanned by $(c_{1}, c_{2}, \cdots  , c_{n})$. Thus
$$c_{1} \frac{p_{1}}{q_{1}} + \cdots  + c_{n} \frac{p_{n}}{q_{n}} = \frac{ma}{q_{1}q_{2} \cdots  q_{n}} = \frac{r}{s} ,$$
where $m \in \mathbb{Z}$. Set
$$\frac{a}{q_{1}q_{2} \cdots  q_{n}} = \frac{a_{1}}{b} ,(a_{1}, b) = 1.$$
Then if $\mathbb{Q}$ was a finitely generated $\mathbb{Z}-module$, we deduce that for all $x \in \mathbb{Q}$
$$ma_{1}$$
$$x = \frac{r}{s} =\overline{b} ,$$
whenever $a_{1}/b$ is a fixed rational number, clearly a contradiction. (In particular let $x = 1/p$ where $p$ is a fixed prime $p > b$. If $ma_{1}/b = 1/p$, then $ma_{1} \in \mathbb{Z}$ with $ma_{1} = b_{1}/p$, an impossiblity since $(b_{1}, p) = 1$ and $p > b_{1}.)$ Definition 3.11 can be generalized to rings and yields free modules.

> **Definition 35.2.** Given a commutative ring $A$ and any (nonempty) set $I$, let $A^{(I)}$ be the subset of the cartesian product $A^{I}$ consisting of all families $(\lambda_{i} )_{i\in I}$ with finite support of scalars in $A.^{2}$ We define addition and multiplication by a scalar as follows:
$$(\lambda_{i} )_{i\in I} + (\mu_{i} )_{i\in I} = (\lambda_{i}  + \mu_{i} )_{i\in I},$$
and
$$\lambda  \cdot  (\mu_{i} )_{i\in I} = (\lambda \mu_{i} )_{i\in I}.$$
It is immediately verified that addition and multiplication by a scalar are well defined. Thus, $A^{(I)}$ is a module. Furthermore, because families with finite support are considered, the family $(e_{i})_{i\in I}$ of vectors $e_{i}$, defined such that $(e_{i})_{j} = 0$ if $j \neq  i$ and $(e_{i})_{i} = 1$, is clearly a basis of the module $A^{(I)}$. When $I = {1, \dots  , n}$, we denote $A^{(I)}$ by $A^{n}$. The function $\iota$ : I $\to A^{(I)}$, such that $\iota (i) = e_{i}$ for every $i \in$ I, is clearly an injection.

> **Definition 35.3.** An A-module $M$ is free iff it has a basis. The module $A^{(I)}$ is a free module. All definitions from Section 3.7 apply to modules, linear maps, kernel, image, except the definition of rank, which has to be defined differently. Propositions 3.19, 3.20, 3.21, and $\overline{2} \overline{Where} \overline{A}^{I} \overline{denotes} \overline{the} \overline{set} \overline{of} \overline{all} \overline{functions}$ from I to $A$.

<!-- PAGE 1276 -->
3.22 hold for modules. However, the other propositions do not generalize to modules. The definition of an isomorphism generalizes to modules. As a consequence, a module is free iff it is isomorphic to a module of the form $A^{(I)}$. Section 3.8 generalizes to modules. Given a submodule $N$ of a module $M$, we can define the quotient module $M/N$. If $\mathfrak{a}$ is an ideal in $A$ and if $M$ is an A-module, we define $\mathfrak{a} M$ as the set of finite sums of the form
$$a_{1}m_{1} + \cdots  + a_{k}m_{k},a_{i} \in \mathfrak{a}, m_{i} \in M.$$
It is immediately verified that $\mathfrak{a} M$ is a submodule of $M$. Interestingly, the part of Theorem 3.12 that asserts that any two bases of a vector space have the same cardinality holds for modules. One way to prove this fact is to “pass” to a vector space by a quotient process.

> **Theorem 35.1.** For any free module $M$, any two bases of $M$ have the same cardinality. Proof sketch. We give the argument for finite bases, but it also holds for infinite bases. The trick is to pick any maximal ideal $\mathfrak{m}$ in $A$ (whose existence is guaranteed by Theorem C.3). Then, $A/\mathfrak{m}$ is a field, and $M/\mathfrak{m} M$ can be made into a vector space over $A/\mathfrak{m}$; we leave the details as an exercise. If $(u_{1}, \dots  , u_{n})$ is a basis of $M$, then it is easy to see that the image of this basis is a basis of the vector space $M/\mathfrak{m} M$. By Theorem 3.12, the number $n$ of elements in any basis of $M/\mathfrak{m} M$ is an invariant, so any two bases of $M$ must have the same number of elements.

> **Definition 35.4.** The common number of elements in any basis of a free module is called the dimension (or rank) of the free module. One should realize that the notion of linear independence in a module is a little tricky. According to the definition, the one-element sequence $(u)$ consisting of a single nonzero vector is linearly independent if for all $\lambda  \in A$, if $\lambda u = 0$ then $\lambda  = 0$. However, there are free modules that contain nonzero vectors that are not linearly independent! For example, the ring $A = \mathbb{Z}/6\mathbb{Z}$ viewed as a module over itself has the basis $(1)$, but the zero-divisors, such as $2$ or $4$, are not linearly independent. Using language introduced in Definition 35.5, a free module may have torsion elements. There are also nonfree modules such that every nonzero vector is linearly independent, such as $\mathbb{Q}$ over $\mathbb{Z}$. All definitions from Section 4.1 about matrices apply to free modules, and so do all the propositions. Similarly, all definitions from Section 6.1 about direct sums and direct products apply to modules. All propositions that do not involve extending bases still hold. The important Proposition 6.15 survives in the following form.

<!-- PAGE 1277 -->

> **Proposition 35.2.** Let $f$ : $E \to F$ be a surjective linear map between two A-modules with $F$ a free module. Given any basis $(v_{1}, \dots  , v_{r})$ of $F$, for any $r$ vectors $u_{1}, \dots  , u_{r} \in E$ such that $f(u_{i}) = v_{i}$ for $i = 1, \dots  , r$, the vectors $(u_{1}, \dots  , u_{r})$ are linearly independent and the module $E$ is the direct sum
$$E = \mathrm{Ker} (f) \oplus U,$$
where $U$ is the free submodule of $E$ spanned by the basis $(u_{1}, \dots  , u_{r})$.

*Proof.* Pick any $w \in E$, write f(w) over the basis $(v_{1}, \dots  , v_{r})$ as f(w) $= a_{1}v_{1} + \cdots  + a_{r}v_{r}$, and let $u = a_{1}u_{1} + \cdots  + a_{r}u_{r}$. Observe that
$$f(w -u) = f(w) -f(u)$$
$$= a_{1}v_{1} + \cdots  + a_{r}v_{r} -(a_{1}f(u_{1}) + \cdots  + a_{r}f(u_{r}))$$
$$= a_{1}v_{1} + \cdots  + a_{r}v_{r} -(a_{1}v_{1} + \cdots  + a_{r}v_{r})$$
$$= 0.$$
Therefore, $h = w$ - $u \in$ Ker $(f)$, and since $w = h + u$ with $h \in$ Ker $(f)$ and $u \in U$, we have $E =$ Ker $(f) + U$. If $u = a_{1}u_{1} + \cdots  + a_{r}u_{r} \in U$ also belongs to Ker $(f)$, then
$$0 = f(u) = f(a_{1}u_{1} + \cdots  + a_{r}u_{r}) = a_{1}v_{1} + \cdots  + a_{r}v_{r},$$
and since $(v_{1}, \dots  , v_{r})$ is a basis, $a_{i} = 0$ for $i = 1, \dots  , r$, which shows that Ker $(f) \cap U = (0)$. Therefore, we have a direct sum
$$E = \mathrm{Ker} (f) \oplus U.$$
Finally, if
$$a_{1}u_{1} + \cdots  + a_{r}u_{r} = 0,$$
the above reasoning shows that $a_{i} = 0$ for $i = 1, \dots  , r$, so $(u_{1}, \dots  , u_{r})$ are linearly independent. Therefore, the module $U$ is a free module. One should be aware that if we have a direct sum of modules
$$U = U_{1} \oplus \cdots  \oplus U_{m},$$
every vector $u \in U$ can be written is a unique way as
$$u = u_{1} + \cdots  + u_{m},$$
with $u_{i} \in U_{i}$ but, unlike the case of vector spaces, this does not imply that any $m$ nonzero vectors $(u_{1}, \dots  , u_{m})$ are linearly independent. For example, we have the direct sum
$$\mathbb{Z}/2\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$$

<!-- PAGE 1278 -->
where $\mathbb{Z}/2\mathbb{Z}$ is viewed as $a \mathbb{Z}-modules$, but $(1, 0)$ and $(0, 1)$ are not linearly independent, since
$$2(1, 0) + 2(0, 1) = (0, 0).$$
A useful fact is that every module is a quotient of some free module. Indeed, if $M$ is an A-module, pick any spanning set $I$ for $M$ (such a set exists, for example, $I = M)$, and consider the unique homomorphism $\phi$ : $A^{(I)} \to M$ extending the identity function from I to itself. Then we have an isomorphism $A^{(I)}/Ker (\phi$ ) $\approx M$. In particular, if $M$ is finitely generated, we can pick I to be a finite set of generators, in which case we get an isomorphism $A^{n}/Ker (\phi$ ) $\approx M$, for some natural number $n$. A finitely generated module is sometimes called a module of finite type. The case $n = 1$ is of particular interest. A module $M$ is said to be cyclic if it is generated by a single element. In this case $M =$ Ax, for some $x \in M$. We have the linear map $m_{x}$ : $A \to M$ given by $a \mapsto$ ax for every $a \in A$, and it is obviously surjective since $M =$ Ax. Since the kernel $\mathfrak{a} =$ Ker $(m_{x})$ of $m_{x}$ is an ideal in $A$, we get an isomorphism $A/\mathfrak{a} \approx$ Ax. Conversely, for any ideal $\mathfrak{a}$ of $A$, if $M = A/\mathfrak{a}$, we see that $M$ is generated by the image $x$ of $1$ in $M$, so $M$ is a cyclic module. The ideal $\mathfrak{a} =$ Ker $(m_{x})$ is the set of all $a \in A$ such that ax $= 0$. This is called the annihilator of $x$, and it is the special case of the following more general situation.

> **Definition 35.5.** If $M$ is any A-module, for any subset $S$ of $M$, the set of all $a \in A$ such that ax $= 0$ for all $x \in S$ is called the annihilator of $S$, and it is denoted by Ann(S). If $S = {x}$, we write Ann(x) instead of $Ann({x})$. A nonzero element $x \in M$ is called a torsion element iff Ann(x) $\neq  (0)$. The set consisting of all torsion elements in $M$ and $0$ is denoted by $M_{tor}$. It is immediately verified that Ann(S) is an ideal of $A$, and by definition,
$$M_{tor} = {x \in M | (\exists a \in A, a \neq  0)(ax = 0)}.$$
If a ring has zero divisors, then the set of all torsion elements in an A-module $M$ may not be a submodule of $M$. For example, if $M = A =\mathbb{Z}/6\mathbb{Z}$, then $M_{tor} = {2, 3, 4}$, but $3 + 4 = 1$ is not a torsion element. Also, a free module may not be torsion-free because there may be torsion elements, as the example of $\mathbb{Z}/6\mathbb{Z}$ as a free module over itself shows. However, if $A$ is an integral domain, then a free module is torsion-free and $M_{tor}$ is a submodule of $M$. (Recall that an integral domain is commutative).

> **Proposition 35.3.** If $A$ is an integral domain, then for any A-module $M$, the set $M_{tor}$ of torsion elements in $M$ is a submodule of $M$.

*Proof.* If $x, y \in M$ are torsion elements $(x, y \neq  0)$, then there exist some nonzero elements a, $b \in A$ such that ax $= 0$ and by $= 0$. Since $A$ is an integral domain, ab $\neq  0$, and then for all $\lambda , \mu  \in A$, we have
$$ab(\lambda x + \mu y) = b\lambda ax + a\mu by = 0.$$

<!-- PAGE 1279 -->
Therefore, $M_{tor}$ is a submodule of $M$. The module $M_{tor}$ is called the torsion submodule of $M$. If $M_{tor} = (0)$, then we say that $M$ is torsion-free, and if $M = M_{tor}$, then we say that $M$ is a torsion module. If $M$ is not finitely generated, then it is possible that $M_{tor}$ ̸ $= 0$, yet the annihilator of $M_{tor}$ is reduced to $0$. For example, let take the $\mathbb{Z}-module$
$$\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/5\mathbb{Z} \times  \cdots  \times \mathbb{Z}/p\mathbb{Z} \times  \cdots  ,$$
where $p$ ranges over the set of primes. Call this module $M$ and the set of primes $P$. Observe that $M$ is generated by ${\alpha_{p} }_{p\in P}$, where $\alpha_{p}$  is the tuple whose only nonzero entry is $\overline{1}_{p}$, the generator of $\mathbb{Z}/p\mathbb{Z}$, i.e.,
$$\alpha_{p}  \overline{= (0},\overline{0},\overline{0}, \cdots  ,\overline{1}_{p},\overline{0}, \cdots  ),\mathbb{Z}/p\mathbb{Z} = {n \cdot \overline{1}_{p}}_{n=0}^{p-1}.$$
In other words, $M$ is not finitely generated. Furthermore, since $p\cdot \overline{1}_{p} \overline{= 0$, we $have} {\alpha_{p} }_{p\in P} \subset M_{tor}$. However, because $p$ ranges over all primes, the only possible nonzero annihilator of ${\alpha_{p} }_{p\in P}$ would be the product of all the primes. Hence $Ann({\alpha_{p} }_{p\in P}) = (0)$. Because of the subset containment, we conclude that $Ann(M_{tor}) = (0)$. However, if $M$ is finitely generated, it is not possible that $M_{tor} \neq  0$, yet the annihilator of $M_{tor}$ is reduced to $0$, since if $x_{1}, \dots  , x_{n}$ generate $M$ and if $a_{1}, \dots  , a_{n}$ annihilate $x_{1}, \dots  , x_{n}$, then $a_{1} \cdots  a_{n}$ annihilates every element of $M$.

> **Proposition 35.4.** If $A$ is an integral domain, then for any A-module $M$, the quotient module $M/M_{tor}$ is torsion free.

*Proof.* Let $\overline{x}$ be an element of $M/M_{tor}$ and assume that $\overline{ax} = 0$ for some $a \neq  0$ in $A$. This means that ax $\in M_{tor}$, so there is some $b \neq  0$ in $A$ such that bax $= 0$. Since a, $b \neq  0$ and $A$ is an integral domain, ba $\neq  0$, so $x \in M_{tor}$, which means that $\overline{x} = 0$. If $A$ is an integral domain and if $F$ is a free A-module with basis $(u_{1}, \dots  , u_{n})$, then $F$ can be embedded in a $K$-vector space $F_{K}$ isomorphic to $K^{n}$, where $K =$ Frac(A) is the fraction field of $A$. Similarly, any submodule $M$ of $F$ is embedded into a subspace $M_{K}$ of $F_{K}$. Note that any linearly independent vectors $(u_{1}, \dots  , u_{m})$ in the A-module $M$ remain linearly independent in the vector space $M_{K}$, because any linear dependence over $K$ is of the form
$$\frac{a_{1}}{b_{1}} u_{1} + \cdots  + \frac{a_{m}}{b_{m}} u_{m} = 0$$
for some $a_{i}, b_{i} \in A$, with $b_{1} \cdots  b_{m}$ ̸ $= 0$, so if we multiply by $b_{1} \cdots  b_{m}$ ̸ $= 0$, we get a linear dependence in the A-module $M$. Then we see that the maximum number of linearly independent vectors in the A-module $M$ is at most $n$. The maximum number of linearly independent vectors in a finitely generated submodule of a free module (over an integral domain) is called the rank of the module $M$. If $(u_{1}, \dots  , u_{m})$ are linearly independent where

<!-- PAGE 1280 -->
$m$ is the rank of $m$, then for every nonzero $v \in M$, there are some a, $a_{1}, \dots  , a_{m} \in A$, not all zero, such that
$$av = a_{1}u_{1} + \cdots  + a_{m}u_{m}.$$
We must have a̸ $= 0$, since otherwise, linear independence of the $u_{i}$ would imply that $a_{1} = \cdots  = a_{m} = 0$, contradicting the fact that a, $a_{1}, \dots  , a_{m} \in A$ are not all zero. Unfortunately, in general, a torsion-free module is not free. For $example,\mathbb{Q}$ as $a\mathbb{Z}-module$ is torsion-free but not free. If we restrict ourselves to finitely generated modules over PID’s, then such modules split as the direct sum of their torsion module with a free module, and a torsion module has a nice decomposition in terms of cyclic modules. The following proposition shows that over a PID, submodules of a free module are free. There are various ways of proving this result. We give a proof due to Lang $[113]$ (see Chapter III, Section $7)$.

> **Proposition 35.5.** If $A$ is a PID and if $F$ is a free A-module of dimension $n$, then every submodule $M$ of $F$ is a free module of dimension at most $n$.

*Proof.* Let $(u_{1}, \dots  , u_{n})$ be a basis of $F$, and let $M_{r} = M \cap (Au_{1} \oplus \cdots \oplus Au_{r})$, the intersection of $M$ with the free module generated by $(u_{1}, \dots  , u_{r})$, for $r = 1, \dots  , n$. We prove by induction on $r$ that each $M_{r}$ is free and of dimension at most $r$. Since $M = M_{r}$ for some $r$, this will prove our result. Consider $M_{1} = M \cap Au_{1}$. If $M_{1} = (0)$, we are done. Otherwise let
$$\mathfrak{a} = {a \in A | au_{1} \in M}.$$
It is immediately verified $that\mathfrak{a}$ is an ideal, and since $A$ is a $PID,\mathfrak{a} = a_{1}A$, for some $a_{1} \in A$. Since we are assuming that $M_{1}$ ̸ $= (0)$, we have $a_{1}$ ̸ $= 0$, and $a_{1}u_{1} \in M$. If $x \in M_{1}$, then $x = au_{1}$ for some $a \in A$, so $a \in a_{1}A$, and thus $a = ba_{1}$ for some $b \in A$. It follows that $M_{1} = Aa_{1}u_{1}$, which is free. Assume inductively that $M_{r}$ is free of dimension at most $r < n$, and let
$$\mathfrak{a} = {a \in A | (\exists b_{1} \in A) \cdots  (\exists b_{r} \in A)(b_{1}u_{1} + \cdots  + b_{r}u_{r} + au_{r+1} \in M)}.$$
It is immediately verified that $\mathfrak{a}$ is an ideal, and since $A$ is a PID, $\mathfrak{a} = a_{r+1}A$, for some $a_{r+1} \in A$. If $a_{r+1} = 0$, then $M_{r+1} = M_{r}$, and we are done. If $a_{r+1} \neq  0$, then there is some $v_{1} \in Au_{1} \oplus \cdots  \oplus Au_{r}$ such that
$$w = v_{1} + a_{r+1}u_{r+1} \in M.$$
For any $x \in M_{r+1}$, there is some $v \in Au_{1}\oplus \cdots \oplus Au_{r}$ and some $a \in A$ such that $x = v+au_{r+1}$. Then, $a \in a_{r+1}A$, so there is some $b \in A$ such that $a = ba_{r+1}$. As a consequence
$$x -bw = v -bv_{1} \in M_{r},$$

<!-- PAGE 1281 -->
and so $x = x$ - bw $+$ bw with $x$ - bw $\in M_{r}$, which shows that
$$M_{r+1} = M_{r} + Aw.$$
On the other hand, if $u \in M_{r} \cap$ Aw, then since $w = v_{1} + a_{r+1}u_{r+1}$ we have
$$u = bv_{1} + ba_{r+1}u_{r+1},$$
for some $b \in A$, with $u, v_{1} \in Au_{1} \oplus \cdots  \oplus Au_{r}$, and if $b \neq  0$, this yields the nontrivial linear combination
$$bv_{1} -u + ba_{r+1}u_{r+1} = 0,$$
contradicting the fact that $(u_{1}, \dots  , u_{r+1})$ are linearly independent. Therefore,
$$M_{r+1} = M_{r} \oplus Aw,$$
which shows that $M_{r+1}$ is free of dimension at most $r + 1$. The following two examples show why the hypothesis of Proposition 35.5 requires $A$ to be PID. First consider $6\mathbb{Z} = {\overline{0},\overline{1},\overline{2},\overline{3},\overline{4},\overline{5}}$ as a free $6\mathbb{Z}-module$ with generator $\overline{1.}$ The $6\mathbb{Z}-$ submodule ${\overline{0},\overline{2},\overline{4}}$ is not free, even though it is generated by $\overline{2}$ since $\overline{3} \cdot \overline{2 = 0.}$ Proposition 35.5 fails since $6\mathbb{Z}$ is not even an integral domain. Next $consider\mathbb{Z}[X]$ as a $free\mathbb{Z}[X]-module$ with generator $1$. We claim the ideal
$$(2, X) = {2p(X) + Xq(X) | p(X), q(X) \in \mathbb{Z}[X]},$$
is not a free $\mathbb{Z}[X]-module$. Indeed any two nonzero elements of $(2, X)$, say s(X) and t(X), are linearly dependent since t(X)s(X) - s(X)t(X) $= 0$. Once again Proposition 35.5 fails since $\mathbb{Z}[X]$ is not a PID. See Example 32.1. Proposition 35.5 implies that if $M$ is a finitely generated module over a PID, then any submodule $N$ of $M$ is also finitely generated. Indeed, if $(u_{1}, \dots  , u_{n})$ generate $M$, then we have a surjection $\phi$ : $A^{n} \to M$ from the free module $A^{n}$ onto $M$. The inverse image $\phi^{-1} (N)$ of $N$ is a submodule of the free module $A^{n}$, therefore by Proposition 35.5, $\phi^{-1} (N)$ is free and finitely generated. This implies that $N$ is finitely generated (and that it has a number of generators $\le n)$. We can also prove that a finitely generated torsion-free module over a PID is actually free. We will give another proof of this fact later, but the following proof is instructive.

> **Proposition 35.6.** If $A$ is a PID and if $M$ is a finitely generated module which is torsionfree, then $M$ is free.

*Proof.* Let $(y_{1}, \dots  , y_{n})$ be some generators for $M$, and let $(u_{1}, \dots  , u_{m})$ be a maximal subsequence of $(y_{1}, \dots  , y_{n})$ which is linearly independent. If $m = n$, we are done. Otherwise, due to the maximality of $m$, for $i = 1, \dots  , n$, there is some $a_{i}$ ̸ $= 0$ such that such that
