# Total Orthogonal Families, Fourier Coefficients


<!-- PAGE 2149 -->
Appendix $A$ Total Orthogonal Families in Hilbert Spaces

## A.1 Total Orthogonal Families (Hilbert Bases),

$$Fourier Coefficients$$
We conclude our quick tour of Hilbert spaces by showing that the notion of orthogonal basis can be generalized to Hilbert spaces. However, the useful notion is not the usual notion of a basis, but a notion which is an abstraction of the concept of Fourier series. Every element of a Hilbert space is the “sum” of its Fourier series.

> **Definition A.1.** Given a Hilbert space $E$, a family $(u_{k})_{k\in K}$ of nonnull vectors is an orthogonal family iff the $u_{k}$ are pairwise orthogonal, i.e., $\langle u_{i}, u_{j}\rangle = 0$ for all $i \neq  j (i, j \in K)$, and an orthonormal family iff $\langle u_{i}, u_{j}\rangle = \delta_{i, j}$ , for all $i, j \in K$. A total orthogonal family (or system) or Hilbert basis is an orthogonal family that is dense in $E$. This means that for every $v \in E$, for every $\epsilon  > 0$, there is some finite subset $I \subseteq K$ and some family $(\lambda_{i} )_{i\in I}$ of complex numbers, such that
$$v - \sum_{i\in I}  \lambda_{i} u_{i} < \epsilon .$$
Given an orthogonal family $(u_{k})_{k\in K}$, for every $v \in E$, for every $k \in K$, the scalar $c_{k} = \langle v, u_{k}\rangle /\|u_{k}\|^{2}$ is called the $k$-th Fourier coefficient of $v$ over $(u_{k})_{k\in K}$.
Remark: The terminology Hilbert basis is misleading because a Hilbert basis $(u_{k})_{k\in K}$ is not necessarily a basis in the algebraic sense. Indeed, in general, $(u_{k})_{k\in K}$ does not span $E$. Intuitively, it takes linear combinations of the $u_{k}’s$ with infinitely many nonnull coefficients to span $E$. Technically, this is achieved in terms of limits. In order to avoid the confusion between bases in the algebraic sense and Hilbert bases, some authors refer to algebraic bases as Hamel bases and to total orthogonal families (or Hilbert bases) as Schauder bases.
$$2149$$

<!-- PAGE 2150 -->
Given an orthogonal family $(u_{k})_{k\in K}$, for any finite subset I of $K$, we often call sums of
$$the form \sum_{i}  \in  \lambda u partial sums of Fourier series, and if these partial sums converge to a$$
$$limit denoted^{I} as \sum_{k}^{ii}  \in K c_{k}u_{k}, we call \sum_{k}  \in K c_{k}u_{k} a Fourier series.$$
However, we have to make sense of such sums! Indeed, when $K$ is unordered or uncountable, the notion of limit or sum has not been defined. This can be done as follows (for more details, see Dixmier $[52])$:

> **Definition A.2.** Given a normed vector space $E$ (say, a Hilbert space), for any nonempty index set $K$, we say that a family $(u_{k})_{k\in K}$ of vectors in $E$ is summable with sum $v \in E$ iff for every $\epsilon  > 0$, there is some finite subset I of $K$, such that,
$$v - \sum_{j\in J}  u_{j} < \epsilon$$
for every finite subset $J$ with $I \subseteq J \subseteq K$. We say that the family $(u_{k})_{k\in K}$ is summable iff there is some $v \in E$ such that $(u_{k})_{k\in K}$ is summable with sum $v$. A family $(u_{k})_{k\in K}$ is a Cauchy family iff for every $\epsilon  > 0$, there is a finite subset I of $K$, such that,
$$\sum_{j\in J}  u_{j}


$< \epsilon$$$ for every finite subset $J$ of $K$ with I $\cap J = \emptyset$ ,
$$If (u_{k})_{k\in K} is summable with sum v, we usually denote v as \sum_{k}  \in K u_{k}. The following$$
technical proposition will be needed:

> **Proposition A.1.** Let $E$ be a complete normed vector space (say, a Hilbert space).
$(1)$ For any nonempty index set $K$, a family $(u_{k})_{k\in K}$ is summable iff it is a Cauchy family.
$(2)$ Given a family $(r_{k})_{k\in K}$ of nonnegative reals $r_{k} \ge 0$, if there is some real number $B > 0$
$$such that \sum_{i}  r_{i} < B for every finite subset I of K, then (r_{k})_{k\in} is summable and$$
$$\sum_{k}  \in K r_{k} = r,^{\in I} where r is least upper bound of the set of finite sums \sum_{i}^{K}  \in I r_{i} (I \subseteq K).$$

*Proof.* $(1)$ If $(u_{k})_{k\in K}$ is summable, for every finite subset I of $K$, let
$$u_{I} = \sum_{i\in I}  u_{i}andu = \sum_{k\in K}  u_{k}$$
For every $\epsilon  > 0$, there is some finite subset I of $K$ such that
$$\|u -u_{L}\|< \epsilon /2$$
for all finite subsets $L$ such that $I \subseteq L \subseteq K$. For every finite subset $J$ of $K$ such that I $\cap J = \emptyset$ , since $I \subseteq$ I $\cup J \subseteq K$ and I $\cup J$ is finite, we have
$$\|u -u_{I\cup J}\|< \epsilon /2and\|u -u_{I}\|< \epsilon /2,$$

<!-- PAGE 2151 -->
and since
$$\|u_{I\cup J} -u_{I}\|\le \|u_{I\cup J} -u\|+ \|u -u_{I}\|$$
and $u_{I\cup J}$ - $u_{I} = u_{J}$ since I $\cap J = \emptyset$ , we get
$$\|u_{J}\|= \|u_{I\cup J} -u_{I}\|< \epsilon ,$$
which is the condition for $(u_{k})_{k\in K}$ to be a Cauchy family. Conversely, assume that $(u_{k})_{k\in K}$ is a Cauchy family. We define inductively a decreasing sequence $(X_{n})$ of subsets of $E$, each of diameter at most $1/n$, as follows: For $n = 1$, since $(u_{k})_{k\in K}$ is a Cauchy family, there is some finite subset $J_{1}$ of $K$ such that
$$\|u_{J}\|< 1/2$$
for every finite subset $J$ of $K$ with $J_{1} \cap J = \emptyset$ . We pick some finite subset $J_{1}$ with the above property, and we let $I_{1} = J_{1}$ and
$$X_{1} = {u_{I} | I_{1} \subseteq I \subseteq K, I finite}.$$
For $n \ge 1$, there is some finite subset $J_{n+1}$ of $K$ such that
$$\|u_{J}\|< 1/(2n + 2)$$
for every finite subset $J$ of $K$ with $J_{n+1} \cap J = \emptyset$ . We pick some finite subset $J_{n+1}$ with the above property, and we let $I_{n+1} = I_{n} \cup J_{n+1}$ and
$$X_{n+1} = {u_{I} | I_{n+1} \subseteq I \subseteq K, I finite}.$$
Since $I_{n} \subseteq I_{n+1}$, it is obvious that $X_{n+1} \subseteq X_{n}$ for all $n \ge 1$. We need to prove that each $X_{n}$ has diameter at most $1/n$. Since $J_{n}$ was chosen such that
$$\|u_{J}\|< 1/(2n)$$
for every finite subset $J$ of $K$ with $J_{n} \cap J = \emptyset$ , and since $J_{n} \subseteq I_{n}$, it is also true that
$$\|u_{J}\|< 1/(2n)$$
for every finite subset $J$ of $K$ with $I_{n} \cap J = \emptyset$ (since $I_{n} \cap J = \emptyset$ and $J_{n} \subseteq I_{n}$ implies that $J_{n} \cap J = \emptyset$ ). Then for every two finite subsets $J, L$ such that $I_{n} \subseteq J, L \subseteq K$, we have
$$\|u_{J-In}\|< 1/(2n)and\|u_{L-In}\|< 1/(2n),$$
and since
$$\|u_{J} -u_{L}\|\le \|u_{J} -u_{In}\|+ \|u_{In} -u_{L}\|= \|u_{J-In}\|+ \|u_{L-In}\|,$$
we get
$$\|u_{J} -u_{L}\|< 1/n,$$

<!-- PAGE 2152 -->
$$which \frac{proves}{X_{n+1}} that \frac{\delta (}{X_{n},} X_{n}) \le 1/n. Now if we consider the sequence of closed sets (\overline{X}_{n}), we$$
$$still have  \subseteq  and by Proposition 48.4, \infty \delta ( \frac{\overline{X}_{n})}{X_{n}} = \delta (X_{n}) \le 1/n, which means that$$
$$lim_{n\to \infty}\delta (X_{n}) = 0, and by Proposition 48.4, \bigcap_{n}  =1  consists of a single element u. We$$
claim that $u$ is the sum of the family $(u_{k})_{k\in K}$. For every $\epsilon  > 0$, there is some $n \ge 1$ such that $n > 2/\epsilon$ , and since $u \in \overline{X}_{m}$ for all $m \ge 1$, there is some finite subset $J_{0}$ of $K$ such that $I_{n} \subseteq J_{0}$ and
$$\|u -u_{J0}\|< \epsilon /2,$$
where $I_{n}$ is the finite subset of $K$ involved in the definition of $X_{n}$. However, since $\delta (X_{n}) \le 1/n$, for every finite subset $J$ of $K$ such that $I_{n} \subseteq J$, we have
$$\|u_{J} -u_{J0}\|\le 1/n < \epsilon /2,$$
and since
$$\|u -u_{J}\|\le \|u -u_{J0}\|+ \|u_{J0} -u_{J}\|,$$
we get
$$\|u -u_{J}\|< \epsilon$$
for every finite subset $J$ of $K$ with $I_{n} \subseteq J$, which proves that $u$ is the sum of the family $(u_{k})_{k\in K}$.
$$(2) Since every finite sum \sum_{i}  \in I r_{i} is bounded by the uniform bound B, the set of these$$
finite sums has a least upper bound $r \le B$. For every $\epsilon  > 0$, since $r$ is the least upper bound
$$of the finite sums \sum_{i}  \in I r_{i} (where I finite, I \subseteq K), there is some finite I \subseteq K such that$$
$$r - \sum_{i\in I}  r_{i} < \epsilon ,$$
and since $r_{k} \ge 0$ for all $k \in K$, we have
$$\sum_{i\in I}  r_{i} \le \sum_{j\in J}  r_{j}$$
whenever $I \subseteq J$, which shows that
$$r - \sum_{j\in J}  r_{j} \le r - \sum_{i\in I}  r_{i} < \epsilon$$
for every finite subset $J$ such that $I \subseteq J \subseteq K$, proving that $(r_{k})_{k\in K}$ is summable with sum
$$\sum_{k}  \in K r_{k} = r.$$

<!-- PAGE 2153 -->
Remark: The notion of summability implies that the sum of a family $(u_{k})_{k\in K}$ is independent of any order on $K$. In this sense it is a kind of “commutative summability.” More precisely, it is easy to show that for every bijection $\phi$ : $K \to K$ (intuitively, a reordering of $K)$, the family $(u_{k})_{k\in K}$ is summable iff the family $(u_{l})_{l\in\phi(K)}$ is summable, and if so, they have the same sum. The following proposition gives some of the main properties of Fourier coefficients. Among other things, at most countably many of the Fourier coefficient may be nonnull, and the partial sums of a Fourier series converge. Given an orthogonal family $(u_{k})_{k\in K}$, we let $U_{k} = \mathbb{C} u_{k}$, and $p_{Uk}$ : $E \to U_{k}$ is the projection of $E$ onto $U_{k}$.

> **Proposition A.2.** Let $E$ be a Hilbert space, $(u_{k})_{k\in K}$ an orthogonal family in $E$, and $V$ the closure of the subspace generated by $(u_{k})_{k\in K}$. The following properties hold:
$(1)$ For every $v \in E$, for every finite subset $I \subseteq K$, we have
$$\sum_{i\in I}  |c_{i}|^{2}\le \|v\|^{2},$$
where the $c_{k}$ are the Fourier coefficients of $v$.
$(2)$ For every vector $v \in E$, if $(c_{k})_{k\in K}$ are the Fourier coefficients of $v$, the following conditions are equivalent:
(2a) $v \in V$
$$(2b) The family (c_{k}u_{k})_{k\in K} is summable and v = \sum_{2k}  c_{k}u_{k}.$$
$$(2c) The family (|c_{k}|^{2})_{k\in K} is summable and \|v\|= \sum_{k}^{\in K}  \in K |c_{k}|^{2};$$
$(3)$ The family $(|c_{k}|^{2})_{k\in K}$ is summable, and we have the Bessel inequality:
$$\sum_{k\in K}  |c_{k}|^{2}\le \|v\|^{2}.$$
As a consequence, at most countably many of the $c_{k}$ may be nonzero. The family
$$(c_{k}u_{k})_{k\in K} forms a Cauchy family, and thus, the Fourier series \sum_{k}  \in K c_{k}u_{k} converges$$
$$in E to some vector u = \sum_{k}  \in K c_{k}u_{k}. Furthermore, u = p_{V} (v).$$
See Figure A.1.

*Proof.* $(1)$ Let
$$u_{I} = \sum_{i\in I}  c_{i}u_{i}$$

<!-- PAGE 2154 -->
$$v, uk$$
$$form c  =$$
$$v=\Sigma_{ckuk} k\overline{2}$$
$$u$$
$$k       Kek$$
$$\overline{V = span(u  )}\overline{k}$$
$$(i.)$$
$$E$$
$$v$$
$$v, uk$$
$$form c  =$$
$$u = \Sigma_{ckuk}  k\overline{2}$$
$$u$$
$$k       Kek$$
$$\overline{V = span(u  )}\overline{k}$$
$$(ii.)$$
$$E$$
**Figure A.1:** A schematic illustration of Proposition A.2. Figure $(i.)$ illustrates Condition (2b), while Figure (ii.) illustrates Condition $(3)$. Note $E$ is the purple oval and $V$ is the magenta oval. In both cases, take a vector of $E$, form the Fourier coefficients $c_{k}$, then form
$$the Fourier series \sum_{k}  c_{k}u_{k}. Condition (2b) ensures v equals its Fourier series since v \in V .$$
However, if $v \in / V ,^{\in K}$ the Fourier series does not equal $v$. Eventually, we will discover that $V = E$, which implies that that Fourier series converges to its vector $v$. for any finite subset I of $K$. We claim that $v -u_{I}$ is orthogonal to $u_{i}$ for every $i \in$ I. Indeed,
$$*+$$
$$\langle v -u_{I}, u_{i}\rangle =v - \sum_{j\in I}  c_{j}u_{j}, u_{i}$$
$$= \langle v, u_{i}\rangle - \sum_{j\in I}  c_{j} \langle u_{j}, u_{i}\rangle$$
$$= \langle v, u_{i}\rangle -c_{i}\|u_{i}\|^{2}$$
$$= \langle v, u_{i}\rangle -\langle v, u_{i}\rangle = 0,$$

<!-- PAGE 2155 -->
since $\langle u_{j}, u_{i}\rangle = 0$ for all $i \neq  j$ and $c_{i} = \langle v, u_{i}\rangle /\|u_{i}\|^{2}$. As a consequence, we have
$$\|v\|^{2}=v - \sum_{i\in I}  c_{i}u_{i} + \sum_{i\in I}  c_{i}u_{i}^{2}$$
$$=v - \sum_{i\in I}  c_{i}u_{i}^{2}+ \sum_{i\in I}  c_{i}u_{i}^{2}$$
$$=v - \sum_{i\in I}  c_{i}u_{i}^{2}+ \sum_{i\in I}  |c_{i}|^{2},$$
since the $u_{i}$ are pairwise orthogonal, that is,
$$\|v\|^{2}=v - \sum_{i\in I}  c_{i}u_{i}^{2}+ \sum_{i\in I}  |c_{i}|^{2}.$$
Thus,
$$\sum_{i\in I}  |c_{i}|^{2}\le \|v\|^{2},$$
as claimed.
$(2)$ We prove the chain of implications $(a) \Rightarrow (b) \Rightarrow (c) \Rightarrow$ (a).
$(a) \Rightarrow (b)$: If $v \in V$ , since $V$ is the closure of the subspace spanned by $(u_{k})_{k\in K}$, for every $\epsilon  > 0$, there is some finite subset I of $K$ and some family $(\lambda_{i} )_{i\in I}$ of complex numbers, such that
$$v - \sum_{i\in I}  \lambda_{i} u_{i} < \epsilon .$$
Now for every finite subset $J$ of $K$ such that $I \subseteq J$, we have
$$v - \sum_{i\in I}  \lambda_{i} u_{i}^{2}=v - \sum_{j\in J}  c_{j}u_{j} + \sum_{j\in J}  c_{j}u_{j} - \sum_{i\in I}  \lambda_{i} u_{i}^{2}$$
$$=v - \sum_{j\in J}  c_{j}u_{j}^{2}+ \sum_{j\in J}  c_{j}u_{j} - \sum_{i\in I}  \lambda_{i} u_{i}^{2},$$
$$since I \subseteq J and the u_{j} (with j \in J) are orthogonal to v - \sum_{j}  \in J c_{j}u_{j} by the argument in (1),$$
which shows that
$$v - \sum_{j\in J}  c_{j}u_{j} \le v - \sum_{i\in I}  \lambda_{i} u_{i} < \epsilon ,$$
and thus, that the family $(c_{k}u_{k})_{k\in K}$ is summable with sum $v$, so that
$$v = \sum_{k\in K}  c_{k}u_{k}.$$

<!-- PAGE 2156 -->
$$(b) \Rightarrow (c): If v = \sum_{k}  \in K c_{k}u_{k}, then for every \epsilon  > 0, there some finite subset I of K, such$$
that
$$\sqrt$$
$$v - \sum_{j\in J}  c_{j}u_{j} <\overline{\epsilon ,}$$
for every finite subset $J$ of $K$ such that $I \subseteq J$, and since we proved in $(1)$ that
$$\|v\|^{2}=v - \sum_{j\in J}  c_{j}u_{j}^{2}+ \sum_{j\in J}  |c_{j}|^{2},$$
we get
$$\|v\|^{2}- \sum_{j\in J}  |c_{j}|^{2}< \epsilon ,$$
which proves that $(|c_{k}|^{2})_{k\in K}$ is summable with sum $\|v\|^{2}$.
$(c) \Rightarrow$ (a): Finally, if $(|c_{k}|^{2})_{k\in K}$ is summable with sum $\|v\|^{2}$, for every $\epsilon  > 0$, there is some finite subset I of $K$ such that
$$\|v\|^{2}- \sum_{j\in J}  |c_{j}|^{2}< \epsilon^{2}$$
for every finite subset $J$ of $K$ such that $I \subseteq J$, and again, using the fact that
$$\|v\|^{2}=v - \sum_{j\in J}  c_{j}u_{j}^{2}+ \sum_{j\in J}  |c_{j}|^{2},$$
we get
$$v - \sum_{j\in J}  c_{j}u_{j} < \epsilon ,$$
$$which proves that (c_{k}u_{k})_{k\in K} is summable with sum \sum_{k}  \in K c_{k}u_{k} = v, and v \in V .$$
$$(3) Since \sum_{k\in Ki}  \in I |c_{i}|^{2}\le \|v\|^{2}for every finite subset I of K, by Proposition A.1(2), the$$
family $(|c_{k}|^{2})$  is summable. The Bessel inequality
$$\sum_{k\in K}  |c_{k}|^{2}\le \|v\|^{2}$$
$$is an obvious consequence of the inequality \sum_{i}  |c_{i}|^{2}\le \|v\|^{2}(for every finite I \subseteq K). Now$$
for every natural number $n \ge 1$, if $K_{n}$ is $the^{\in I}$ subset of $K$ consisting of all $c_{k}$ such that $|c_{k}| \ge 1/n$, the number of elements in $K_{n}$ is at most
$$\sum_{k\in Kn}  |nc_{k}|^{2}\le n^{2} \sum_{k\in K}  |c_{k}|^{2}\le n^{2}\|v\|^{2},$$
which is finite, and thus, at most a countable number of the $c_{k}$ may be nonzero.

<!-- PAGE 2157 -->
Since $(|c_{k}|^{2})_{k\in K}$ is summable with sum $c$, by Proposition A.1(1) we know that for every $\epsilon  > 0$, there is some finite subset I of $K$ such that
$$\sum_{j\in J}  |c_{j}|^{2}< \epsilon^{2}$$
for every finite subset $J$ of $K$ such that I $\cap J = \emptyset$ . Since
$$\sum_{j\in J}  c_{j}u_{j}^{2}= \sum_{j\in J}  |c_{j}|^{2},$$
we get
$$\sum_{j\in J}  c_{j}u_{j}


$< \epsilon$ .$$ This proves that $(c_{k}u_{k})_{k\in K}$ is a Cauchy family, which, by Proposition A.1(1), implies that
$$(c_{k}u_{k})_{k\in K} is summable since E is complete. Thus, the Fourier series \sum_{k}  \in K c_{k}u_{k} is summable,$$
with its sum denoted $u \in V$ .
$$Since \sum_{k}  \in K c_{k}u_{k} is summable with sum u, for every \epsilon  > 0, there is some finite subset I_{1}$$
of $K$ such that
$$u - \sum_{j\in J}  c_{j}u_{j} < \epsilon$$
for every finite subset $J$ of $K$ such that $I_{1} \subseteq J$. By the triangle inequality, for every finite subset I of $K$,
$$u -v \le u - \sum_{i\in I}  c_{i}u_{i} + \sum_{i\in I}  c_{i}u_{i} -v.$$
$$By (2), every w \in V is the sum of its Fourier series \sum_{k}  \in K \lambda_{k} u_{k}, and for every \epsilon  > 0, there$$
is some finite subset $I_{2}$ of $K$ such that
$$w - \sum_{j\in J}  \lambda_{j} u_{j} < \epsilon$$
for every finite subset $J$ of $K$ such that $I_{2} \subseteq J$. By the triangle inequality, for every finite subset I of $K$,
$$v - \sum_{i\in I}  \lambda_{i} u_{i} \le \|v -w\|+w - \sum_{i\in I}  \lambda_{i} u_{i}.$$
Letting $I = I_{1} \cup I_{2}$, since we showed in $(2)$ that
$$v - \sum_{i\in I}  c_{i}u_{i} \le v - \sum_{i\in I}  \lambda_{i} u_{i}$$
