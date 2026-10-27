# Noetherian Rings and Hilbert's Basis Theorem


<!-- PAGE 1157 -->
and for $k \neq  i$,
$$e_{k}a = e_{k}e_{i}\alpha_{i}  = 0,$$
$$which shows that a = e_{1}a + \cdots  + e_{n}a = 0, so \mathfrak{a}_{i} \cap \bigoplus_{j}  \neq i \mathfrak{a}_{j} = {0} for i = 1, \dots  , n. Thus we$$
have the direct sum $A =\mathfrak{a}_{1} \oplus \cdots  \oplus \mathfrak{a}_{n}$.
$(4)$ Since the $\mathfrak{a}_{i} = e_{i}A$ are ideal and $A =\mathfrak{a}_{1} \oplus \cdots  \oplus \mathfrak{a}_{n} = e_{1}A \oplus \cdots  \oplus e_{n}A$, we obtain $\mathfrak{b} =\mathfrak{b} \cap A =\mathfrak{b} \cap \mathfrak{a}_{1} \oplus \cdots  \oplus \mathfrak{b} \cap \mathfrak{a}_{n} =\mathfrak{b} \cap e_{1}A \oplus \cdots  \oplus \mathfrak{b} \cap e_{n}A = e_{1}\mathfrak{b} \oplus \cdots  \oplus e_{n}\mathfrak{b}$, where each $\mathfrak{b} \cap e_{i}A = e_{i}\mathfrak{b}$ is an ideal.
$(5)$ Since each $e_{i}$ is a nonzero idempotent and the ring is commutative, each $e_{i}A$ is a nonzero ideal. The proof above showing that we have the direct sum $A =\mathfrak{a}_{1} \oplus \cdots  \oplus \mathfrak{a}_{n}$ only uses the properties of the $e_{i}$ stated in $(1)$, so it also applies in $(5)$. Since we have the direct sum $A =\mathfrak{a}_{1} \oplus \cdots  \oplus \mathfrak{a}_{n}$, we have projections $\pi_{i}$  : $A \to \mathfrak{a}_{i}$, and we check immediately that the map $\theta$  given by $\theta (a) = (\pi_{1} (a), \dots  , \pi_{n}$ (a)) is an isomorphism $\theta$ : $A \to \mathfrak{a}_{1} \times  \cdots  \times \mathfrak{a}_{n}$.
Remark: Even if the rings $A_{i}$ are not commutative, since $e_{i}(a_{1}, \dots  , a_{n}) = (a_{1}, \dots  , a_{n})e_{i}$ for all $(a_{1}, \dots  , a_{n}) \in A_{1} \times  \cdots  \times  A_{n}$ and all $i = 1, \dots  , n$, we also have
$$e_{i}a = ae_{i},1 \le i \le n,$$
for all $a \in A$. We say that the $e_{i}$ are central idempotents. It follows that Proposition 32.18 also holds for nonncommutative rings with identity. It should also be noted that if $n \ge 2$ and $e_{1}, \dots  , e_{n} \in A$ are nonzero and satisfy the properties in $(1)$, then they are distinct and noninvertible. In particular, $e_{i} \neq  1$. Indeed, if $e_{i} = e_{j}$ for some $i \neq  j$, then
$$e_{i} = e_{i}^{2} = e_{i}e_{j} = 0,$$
contradicting the fact that $e_{i} \neq  0$. If $e_{i}$ is invertible, from $e_{i}e_{j} = 0$ for $i \neq  j$, we deduce that $e_{j} = 0$, a contradiction. Since $1$ is invertible, $e_{i} \neq  1$. As a consequence, the nonzero ideals $\mathfrak{a}_{i} = e_{i}A$ are proper ideals. Otherwise, there would be some $a \in A$ such that $e_{i}a = 1$, so $e_{i}$ would be invertible, a contradiction.

## 32.3 Noetherian Rings and Hilbert’s Basis Theorem

Given a (commutative) ring $A$ (with unit element $1)$, an ideal $\mathfrak{A} \subseteq A$ is said to be finitely generated if there exists a finite set ${a_{1}, \dots  , a_{n}}$ of elements from $\mathfrak{A}$ so that
$$\mathfrak{A} = (a_{1}, \dots  , a_{n}) = {\lambda_{1} a_{1} + \cdots  + \lambda_{n} a_{n} | \lambda_{i}  \in A, 1 \le i \le n}.$$
If $K$ is a field, it turns out that every polynomial ideal $\mathfrak{A}$ in $K[X_{1}, \dots  , X_{m}]$ is finitely generated. This fact due to Hilbert and known as Hilbert’s basis theorem, has very important

<!-- PAGE 1158 -->
consequences. For example, in algebraic geometry, one is interested in the zero locus of a set of polyomial equations, i.e., the set, $V (\mathcal{P})$, of $n$-tuples $(\lambda_{1} , \dots  , \lambda_{n}$ ) $\in K^{n}$ so that
$$P_{i}(\lambda_{1} , \dots  , \lambda_{n} ) = 0$$
for all polynomials $P_{i}(X_{1}, \dots  , X_{n})$ in some given family, $\mathcal{P} = (P_{i})_{i\in I}$. However, it is clear that
$$V (\mathcal{P}) = V (\mathfrak{A}),$$
$where\mathfrak{A}$ is the ideal generated $by\mathcal{P}$. Then, Hilbert’s basis theorem says that $V (\mathfrak{A})$ is actually defined by a finite number of polynomials (any set of generators of $\mathfrak{A})$, even if $\mathcal{P}$ is infinite. The property that every ideal in a ring is finitely generated is equivalent to other natural properties, one of which is the so-called ascending chain condition, abbreviated a.c.c. Before proving Hilbert’s basis theorem, we explore the equivalence of these conditions.

> **Definition 32.7.** Let $A$ be a commutative ring with unit $1$. We say that $A$ satisfies the ascending chain condition, for short, the a.c.c, if for every ascending chain of ideals
$$\mathfrak{A}_{1} \subseteq \mathfrak{A}_{2} \subseteq \cdots  \subseteq \mathfrak{A}_{i} \subseteq \cdots  ,$$
there is some integer $n \ge 1$ so that
$$\mathfrak{A}_{i} =\mathfrak{A}_{n}for alli \ge n + 1.$$
We say that $A$ satisfies the maximum condition if every nonempty collection $C$ of ideals in $A$ has a maximal element, i.e., there is some $ideal\mathfrak{A} \in C$ which is not contained in any other ideal in $C$.

> **Proposition 32.19.** A ring $A$ satisfies the a.c.c if and only if it satisfies the maximum condition.

*Proof.* Suppose that $A$ does not satisfy the a.c.c. Then, there is an infinite strictly ascending sequence of ideals
$$\mathfrak{A}_{1} \subset \mathfrak{A}_{2} \subset \cdots  \subset \mathfrak{A}_{i} \subset \cdots  ,$$
and the collection $C = {\mathfrak{A}_{i}}$ has no maximal element. Conversely, assume that $A$ satisfies the a.c.c. Let $C$ be a nonempty collection of ideals Since $C$ is nonempty, we may pick some ideal $\mathfrak{A}_{1}$ in $C$. If $\mathfrak{A}_{1}$ is not maximal, then there is some ideal $\mathfrak{A}_{2}$ in $C$ so that
$$\mathfrak{A}_{1} \subset \mathfrak{A}_{2}.$$
Using this process, if $C$ has no maximal element, we can define by induction an infinite strictly increasing sequence
$$\mathfrak{A}_{1} \subset \mathfrak{A}_{2} \subset \cdots  \subset \mathfrak{A}_{i} \subset \cdots  .$$
However, the a.c.c. implies that such a sequence cannot exist. Therefore, $C$ has a maximal element.

<!-- PAGE 1159 -->
Having shown that the a.c.c. condition is equivalent to the maximal condition, we now prove that the a.c.c. condition is equivalent to the fact that every ideal is finitely generated.

> **Proposition 32.20.** A ring $A$ satisfies the a.c.c if and only if every ideal is finitely generated.

*Proof.* Assume that every ideal is finitely generated. Consider an ascending sequence of ideals
$$\mathfrak{A}_{1} \subseteq \mathfrak{A}_{2} \subseteq \cdots  \subseteq \mathfrak{A}_{i} \subseteq \cdots  .$$
$$Observe that \mathfrak{A} = \bigcup_{i}  \mathfrak{A}_{i} is also an ideal.By hypothesis, \mathfrak{A} has a finite generating set$$
${a_{1}, \dots  , a_{n}}$. By definition of $\mathfrak{A}$, each $a_{i}$ belongs to some $\mathfrak{A}_{ji}$, and since the $\mathfrak{A}_{i}$ form an ascending chain, there is some $m$ so that $a_{i} \in \mathfrak{A}_{m}$ for $i = 1, \dots  , n$. But then,
$$\mathfrak{A}_{i} =\mathfrak{A}_{m}$$
for all $i \ge m + 1$, and the a.c.c. holds. Conversely, assume that the a.c.c. holds. $Let\mathfrak{A}$ be any ideal in $A$ and consider the family $C$ of subideals of $\mathfrak{A}$ that are finitely generated. The family $C$ is nonempty, since $(0)$ is a subideal of $\mathfrak{A}$. By Proposition 32.19, the family $C$ has some maximal element, say $\mathfrak{B}$. For any $a \in \mathfrak{A}$, the ideal $\mathfrak{B} + (a)$ (where $\mathfrak{B} + (a) = {b + \lambda$ a | $b \in \mathfrak{B}, \lambda  \in A})$ is also finitely generated (since $\mathfrak{B}$ is finitely generated), and by maximality, we have
$$\mathfrak{B} =\mathfrak{B} + (a).$$
So, we get $a \in \mathfrak{B}$ for all $a \in \mathfrak{A}$, and thus, $\mathfrak{A} =\mathfrak{B}$, and $\mathfrak{A}$ is finitely generated.

> **Definition 32.8.** A commutative ring $A$ (with unit $1)$ is called noetherian if it satisfies the a.c.c. condition. A noetherian domain is a noetherian ring that is also a domain. By Proposition 32.19 and Proposition 32.20, a noetherian ring can also be defined as a ring that either satisfies the maximal property or such that every ideal is finitely generated. The proof of Hilbert’s basis theorem will make use the following lemma:

> **Lemma 32.21.** Let $A$ be a (commutative) ring. For every ideal $\mathfrak{A}$ in A[X], for every $i \ge 0$, let $L_{i}(\mathfrak{A})$ denote the set of elements of $A$ consisting of $0$ and of the coefficients of $X^{i}$ in all the polynomials f(X) $\in \mathfrak{A}$ which are of degree $i$. Then, the $L_{i}(\mathfrak{A})’s$ form an ascending chain of ideals in $A$. Furthermore, if $\mathfrak{B}$ is any ideal of A[X] so that $\mathfrak{A} \subseteq \mathfrak{B}$ and if $L_{i}(\mathfrak{A}) = L_{i}(\mathfrak{B})$ for all $i \ge 0$, then $\mathfrak{A} =\mathfrak{B}$.

*Proof.* That $L_{i}(\mathfrak{A})$ is an ideal and that $L_{i}(\mathfrak{A}) \subseteq L_{i+1}(\mathfrak{A})$ follows from the fact that if f(X) $\in \mathfrak{A}$ and g(X) $\in \mathfrak{A}$, then f(X) $+$ g(X), $\lambda$ f(X), and Xf(X) all belong to $\mathfrak{A}$. Now, let g(X) be any polynomial in $\mathfrak{B}$, and assume that g(X) has degree $n$. Since $L_{n}(\mathfrak{A}) = L_{n}(\mathfrak{B})$, there is some polynomial $f_{n}(X)$ in $\mathfrak{A}$, of degree $n$, so that g(X) - $f_{n}(X)$ is of degree at most $n$ - $1$. Now, since $\mathfrak{A} \subseteq \mathfrak{B}$, the polynomial g(X) - $f_{n}(X)$ belongs to $\mathfrak{B}$. Using this process, we can

<!-- PAGE 1160 -->
define by induction a sequence of polynomials $f_{n+i}(X) \in \mathfrak{A}$, so that each $f_{n+i}(X)$ is either zero or has degree $n$ - $i$, and
$$g(X) -(f_{n}(X) + f_{n+1}(X) + \cdots  + f_{n+i}(X))$$
is of degree at most $n$ - $i$ - $1$. Note that this last polynomial must be zero when $i = n$, and thus, g(X) $\in \mathfrak{A}$. We now prove Hilbert’s basis theorem. The proof is substantially Hilbert’s original proof. A slightly shorter proof can be given but it is not as transparent as Hilbert’s proof (see the remark just after the proof of Theorem 32.22, and Zariski and Samuel $[200]$, Chapter IV, Section $1$, Theorem $1)$.

> **Theorem 32.22.** (Hilbert’s basis theorem) If $A$ is a noetherian ring, then A[X] is also a noetherian ring.

*Proof.* Let $\mathfrak{A}$ be any ideal in A[X], and denote by $\mathcal{L}$ the set of elements of $A$ consisting of $0$ and of all the coefficients of the highest degree terms of all the polynomials in $\mathfrak{A}$. Observe that
$$\mathcal{L} = \bigcup_{i}  L_{i}(\mathfrak{A}).$$
Thus, $\mathcal{L}$ is an ideal in $A$ (this can also be proved directly). Since $A$ is noetherian, $\mathcal{L}$ is finitely generated, and let ${a_{1}, \dots  , a_{n}}$ be a set of generators of $\mathcal{L}$. Let $f_{1}(X), \dots  , f_{n}(X)$ be polynomials in $\mathfrak{A}$ having respectively $a_{1}, \dots  , a_{n}$ as highest degree term coefficients. These polynomials generate an $ideal\mathfrak{B}$. Let $q$ be the maximum of the degrees of the $f_{i}(X)’s$. Now, pick any polynomial g(X) $\in \mathfrak{A}$ of degree $d \ge q$, and let $aX^{d}$ be its term of highest degree. Since $a \in L$, we have
$$a = \lambda_{1} a_{1} + \cdots  + \lambda_{n} a_{n},$$
for some $\lambda_{i}  \in A$. Consider the polynomial
$$g_{1}(X) = \sum_{i=1}^{n}  \lambda_{i} f_{i}(X)X^{d-di},$$
where $d_{i}$ is the degree of $f_{i}(X)$. Now, g(X) - $g_{1}(X)$ is a polynomial in $\mathfrak{A}$ of degree at most $d$ - $1$. By repeating this procedure, we get a sequence of polynomials $g_{i}(X)$ in $\mathfrak{B}$, having strictly decreasing degrees, and such that the polynomial
$$g(X) -(g_{1}(X) + \cdots  + g_{i}(X))$$
is of degree at most $d$ - $i$. This polynomial must be of degree at most $q$ - $1$ as soon as $i = d$ - $q + 1$. Thus, we proved that every polynomial in $\mathfrak{A}$ of degree $d \ge q$ belongs to $\mathfrak{B}$. It remains to take care of the polynomials in $\mathfrak{A}$ of degree at most $q$ - $1$. Since $A$ is noetherian, each ideal $L_{i}(\mathfrak{A})$ is finitely generated, and let ${a_{i1}, \dots  , a_{ini}}$ be a set of generators
