# The Hilbert Space 2(K) and the Riesz–Fischer Theorem


<!-- PAGE 2158 -->
for every finite subset I of $K$, we get
$$\|u -v\|\le u - \sum_{i\in I}  c_{i}u_{i} + \sum_{i\in I}  c_{i}u_{i} -v$$
$$\le u - \sum_{i\in I}  c_{i}u_{i} + \sum_{i\in I}  \lambda_{i} u_{i} -v$$
$$\le u - \sum_{i\in I}  c_{i}u_{i} + \|v -w\|+w - \sum_{i\in I}  \lambda_{i} u_{i},$$
and thus
$$\|u -v\|\le \|v -w\|+ 2\epsilon .$$
Since this holds for every $\epsilon  > 0$, we have
$$\|u -v\|\le \|v -w\|$$
for all $w \in V$ , i.e. $\|v$ - $u\| =$ d(v, $V$ ), with $u \in V$ , which proves that $u = p_{V} (v)$.

## A.2 The Hilbert Space \ell 2(K) and the Riesz–Fischer

$$Theorem$$
Proposition A.2 suggests looking at the space of sequences $(z_{k})_{k\in K}$ (where $z_{k} \in \mathbb{C})$ such that $(|z_{k}|^{2})_{k\in K}$ is summable. Indeed, such spaces are Hilbert spaces, and it turns out that every Hilbert space is isomorphic to one of those. Such spaces are the infinite-dimensional version
$$\mathbb{C}^{n}$$
of the spaces under the usual Euclidean norm.

> **Definition A.3.** Given any nonempty index set $K$, the space $\ell (K)$ is the set of all sequences
$$\mathbb{C}$$
$$(z_{k})_{k\in K}, where z_{k} \in , such that (|z_{k}|^{2})_{k\in K} is summable, i.e., \sum_{k}^{2}  \in K |z_{k}|^{2}< \infty .$$
Remarks:
$(1)$ When $K$ is a finite set of cardinality $n, \ell^{2} (K)$ is isomorphic to $\mathbb{C}^{n}$.
$$\mathbb{N}\mathbb{N}$$
$(2)$ When $K =$ , the space $\ell^{2}$ ( ) corresponds to the space $\ell^{2}$ of Example $2$ in Section 14.1 . In that example, we claimed that $\ell^{2}$ was a Hermitian space, and in fact, a Hilbert space. We now prove this fact for any index set $K$.

> **Proposition A.3.** Given any nonempty index set $K$, the space $\ell^{2} (K)$ is a Hilbert space under the Hermitian product
$$\langle (x_{k})_{k\in K}, (y_{k})_{k\in K}\rangle = \sum_{k\in K}  x_{k}\overline{y}_{k}.$$
The subspace consisting of sequences $(z_{k})_{k\in K}$ such that $z_{k} = 0$, except perhaps for finitely many $k$, is a dense subspace of $\ell^{2} (K)$.

<!-- PAGE 2159 -->

*Proof.* First we need to prove that $\ell^{2} (K)$ is a vector space. Assume that $(x_{k})_{k\in K}$ and $(y_{k})_{k\in K}$ are in $\ell^{2} (K)$. This means that $(|x_{k}|^{2})_{k\in K}$ and $(|y_{k}|^{2})_{k\in K}$ are summable, which, in view of Proposition A.1(2), is equivalent to the existence of some positive bounds $A$ and $B$ such
$$that \sum_{ik}  |x_{i}|^{2}< A and \sum_{i}  |y_{i}|^{2}< B, for every finite subset I of K.To prove that$$
$(|x_{k} + y^{\in I}|^{2})_{k\in K}$ is $summable,^{\in I}$ it is sufficient to prove that there is some $C > 0$ such that
$$\sum_{i}  \in I |x_{i} + y_{i}|^{2}< C for every finite subset I of K. However, the parallelogram inequality$$
implies that
$$\sum_{i\in I}  |x_{i} + y_{i}|^{2}\le \sum_{i\in I}  2(|x_{i}|^{2}+ |y_{i}|^{2}) \le 2(A + B),$$
for every finite subset I of $K$, and we conclude by Proposition A.1(2). Similarly, for every $\lambda  \in \mathbb{C}$,
$$\sum_{i\in I}  |\lambda x_{i}|^{2}\le \sum_{i\in I}  |\lambda |^{2}|x_{i}|^{2}\le |\lambda |^{2}A,$$
and $(\lambda_{k} x_{k})_{k\in K}$ is summable. Therefore, $\ell^{2} (K)$ is a vector space. By the Cauchy-Schwarz inequality,
$$\sum_{i\in I}  |x_{i}\overline{y}_{i}| \le \sum_{i\in I}  |x_{i}||y_{i}| \le \begin{pmatrix} |x_{i} \end{pmatrix} \sum_{i\in I}  |^{21/2} \begin{pmatrix} |xy_{i} \end{pmatrix} \sum_{i\in I}  |^{21/2}\le \sum_{i\in I}  (|x_{i}|^{2}+ |y_{i}|^{2})/2 \le (A + B)/2,$$
for every finite subset I of $K$. For the third inequality we used the fact that
$$4CD \le (C + D)^{2},$$
$$(with C = \sum_{i}  \in I |x_{i}|^{2}and D = \sum  i\in I |y_{i}|^{2}) which is equivalent to$$
$$(C -D)^{2}\ge 0.$$
By Proposition A.1(2), $(|x_{k}\overline{y}_{k}|)_{k\in K}$ is summable. The customary language is that $(x_{k}\overline{y}_{k})_{k\in K}$ is absolutely summable. However, it is a standard fact that this implies that $(x_{k}\overline{y}_{k})_{k\in K}$ is summable (For every $\epsilon  > 0$, there is some finite subset I of $K$ such that
$$\sum_{j\in J}  |x_{j}\overline{y}_{j}| < \epsilon$$
for every finite subset $J$ of $K$ such that I $\cap J = \emptyset$ , and thus
$$| \sum_{j\in J}  x_{j}\overline{y}_{j}| \le \sum_{i\in J}  |x_{j}\overline{y}_{j}| < \epsilon ,$$
proving that $(x_{k}\overline{y}_{k})_{k\in K}$ is a Cauchy family, and thus summable). We still have to prove that $\ell^{2} (K)$ is complete. Consider a sequence $((\lambda_{k}^{n} )_{k\in K})_{n\ge1}$ of sequences $(\lambda_{k}^{n} )_{k\in K} \in \ell^{2} (K)$, and assume that it is a Cauchy sequence. This means that for every $\epsilon  > 0$, there is some $N \ge 1$ such that
$$\sum_{k\in K}  |\lambda_{k}^{m}  -\lambda_{k}^{n} |^{2}< \epsilon^{2}$$

<!-- PAGE 2160 -->
for all $m, n \ge N$. For every fixed $k \in K$, this implies that
$$|\lambda_{k}^{m}  -\lambda_{k}^{n} | < \epsilon$$
for all $m, n \ge N$, which shows that $(\lambda_{k}^{n} )_{n\ge1}$ is a Cauchy sequence in $\mathbb{C}$. Since $\mathbb{C}$ is complete, the sequence $(\lambda_{k}^{n} )_{n\ge1}$ has a limit $\lambda_{k}  \in \mathbb{C}$. We claim that $(\lambda_{k} )_{k\in K} \in \ell^{2} (K)$ and that this is the limit of $((\lambda_{k}^{n} )_{k\in K})_{n\ge1}$. Given any $\epsilon  > 0$, the fact that $((\lambda_{k}^{n} )_{k\in K})_{n\ge1}$ is a Cauchy sequence implies that there is some $N \ge 1$ such that for every finite subset I of $K$, we have
$$\sum_{i\in I}  |\lambda_{i}^{m}  -\lambda_{i}^{n}  |^{2}< \epsilon /4$$
for all $m, n \ge N$. Let $p =$ |I|. Then
$$|\lambda_{i}^{m}  -\lambda_{i}^{n}  | < \frac{\sqrt{\epsilon}}{2\overline{p}} \sqrt$$
for every $i \in$ I. Since $\lambda_{i}$  is the limit of $(\lambda_{i}^{n}  )_{n\ge1}$, we can find some $n$ large enough so that
$$|\lambda_{i}^{n}  -\lambda_{i} | < \frac{\sqrt{\epsilon}}{2\overline{p}} \sqrt$$
for every $i \in$ I. Since
$$|\lambda_{i}^{m}  -\lambda_{i} | \le |\lambda_{i}^{m}  -\lambda_{i}^{n}  | + |\lambda_{i}^{n}  -\lambda_{i} |,$$
we get
$$\sqrt$$
$$\overline{\epsilon}$$
$$|\lambda_{i}^{m}  -\lambda_{i} | <\sqrt p,$$
and thus,
$$\sum_{i\in I}  |\lambda_{i}^{m}  -\lambda_{i} |^{2}< \epsilon ,$$
for all $m \ge N$. Since the above holds for every finite subset I of $K$, by Proposition A.1(2), we get
$$\sum_{k\in K}  |\lambda_{k}^{m}  -\lambda_{k} |^{2}< \epsilon ,$$
for all $m \ge N$. This proves that $(\lambda_{k}^{m}$  - $\lambda_{k} )_{k\in K} \in \ell^{2} (K)$ for all $m \ge N$, and since $\ell^{2} (K)$ is a vector space and $(\lambda_{k}^{m}  )_{k\in K} \in \ell^{2} (K)$ for all $m \ge 1$, we get $(\lambda_{k} )_{k\in K} \in \ell^{2} (K)$. However,
$$\sum_{k\in K}  |\lambda_{k}^{m}  -\lambda_{k} |^{2}< \epsilon$$
for all $m \ge N$, means that the sequence $(\lambda_{k}^{m}  )_{k\in K}$ converges to $(\lambda_{k} )_{k\in K} \in \ell^{2} (K)$. The fact that the subspace consisting of sequences $(z_{k})_{k\in K}$ such that $z_{k} = 0$ except perhaps for finitely many $k$ is a dense subspace of $\ell^{2} (K)$ is left as an easy exercise.

<!-- PAGE 2161 -->
Remark: The subspace consisting of all sequences $(z_{k})_{k\in K}$ such that $z_{k} = 0$, except perhaps for finitely many $k$, provides an example of a subspace which is not closed in $\ell^{2} (K)$. Indeed, this space is strictly contained in $\ell^{2} (K)$, since there are countable sequences of nonnull elements in $\ell^{2} (K)$ (why?). We just need two more propositions before being able to prove that every Hilbert space is isomorphic to some $\ell^{2} (K)$.

> **Proposition A.4.** Let $E$ be a Hilbert space, and $(u_{k})_{k\in K}$ an orthogonal family in $E$. The following properties hold:
$(1)$ For every family $(\lambda_{k} )_{k\in K} \in \ell^{2} (K)$, the family $(\lambda_{k} u_{k})_{k\in K}$ is summable. Furthermore,
$$v = \sum_{k}  \lambda_{k} u_{k} is the only vector such that c_{k} = \lambda_{k}  for all k \in K, where the c_{k} are the$$
$Fourier^{\in K}$ coefficients of $v$.
$$(2) For any two families (\lambda_{k} )_{k\in K} \in \ell^{2} (K) and (\mu_{k} )_{k\in K} \in \ell^{2} (K), if v = \sum_{k}  \in K \lambda_{k} u_{k} and$$
$$w = \sum_{k}  \in K \mu_{k} u_{k}, we have the following equation, also called Parseval identity:$$
$$\langle v, w\rangle = \sum_{k\in K}  \lambda_{k} \overline{\mu}_{k}.$$

*Proof.* $(1)$ The fact that $(\lambda_{k} )_{k\in K} \in \ell^{2} (K)$ means that $(|\lambda_{k} |^{2})_{k\in K}$ is summable. The proof given in Proposition A.2 $(3)$ applies to the family $(|\lambda |^{2})_{k\in K}$ (instead of $(|c_{k}|^{2})_{k\in K})$, and yields
$$the fact that (\lambda_{k} u_{k})_{k\in K} is summable. Letting v = \sum_{k}^{k}  \in K \lambda_{k} u_{k}, recall that c_{k} = \langle v, u_{k}\rangle /\|u_{k}\|^{2}.$$
Pick some $k \in K$. Since $\langle$ -, $-\rangle$ is continuous, for every $\epsilon  > 0$, there is some $\eta  > 0$ such that
$$| \langle v, u_{k}\rangle -\langle w, u_{k}\rangle | < \epsilon \|u_{k}\|^{2}$$
whenever
$$\|v -w\|< \eta .$$
However, since for every $\eta  > 0$, there is some finite subset I of $K$ such that
$$v - \sum_{j\in J}  \lambda_{j} u_{j} < \eta$$
for every finite subset $J$ of $K$ such that $I \subseteq J$, we can pick $J =$ I $\cup {k}$ and letting
$$w = \sum_{j}  \in J \lambda_{j} u_{j} we get$$
$$\langle v, u_{k}\rangle -* \sum_{j\in J}  \lambda_{j} u_{j}, u_{k}+




$< \epsilon \|u_{k}\|^{2}.$$$ However,
$$\langle v, u_{k}\rangle = c_{k}\|u_{k}\|^{2}and* \sum_{j\in J}  \lambda_{j} u_{j}, u_{k}+= \lambda_{k} \|u_{k}\|^{2},$$
and thus, the above proves that $|c_{k}$ - $\lambda_{k}$ | $< \epsilon$  for every $\epsilon  > 0$, and thus, that $c_{k} = \lambda_{k}$ .

<!-- PAGE 2162 -->
$(2)$ Since $\langle$ -, $-\rangle$ is continuous, for every $\epsilon  > 0$, there are some $\eta_{1}  > 0$ and $\eta_{2}  > 0$, such that
$$| \langle x, y\rangle | < \epsilon$$
$$whenever \|x\|< \eta_{1}  and \|y\|< \eta_{2} . Since v = \sum_{k}  \in K \lambda_{k} u_{k} and w = \sum  k\in K \mu_{k} u_{k}, there is some$$
finite subset $I_{1}$ of $K$ such that
$$v - \sum_{j\in J}  \lambda_{j} u_{j} < \eta_{1}$$
for every finite subset $J$ of $K$ such that $I_{1} \subseteq J$, and there is some finite subset $I_{2}$ of $K$ such that
$$w - \sum_{j\in J}  \mu_{j} u_{j} < \eta_{2}$$
for every finite subset $J$ of $K$ such that $I_{2} \subseteq J$. Letting $I = I_{1} \cup I_{2}$, we get
$$*+$$
$$v - \sum_{i\in I}  \lambda_{i} u_{i}, w - \sum_{i\in I}  \mu_{i} u_{i} < \epsilon .$$
Furthermore,
$$*+$$
$$\langle v, w\rangle =v - \sum_{i\in I}  \lambda_{i} u_{i} + \sum_{i\in I}  \lambda_{i} u_{i}, w - \sum_{i\in I}  \mu_{i} u_{i} + \sum_{i\in I}  \mu_{i} u_{i}$$
$$*+$$
$$=v - \sum_{i\in I}  \lambda_{i} u_{i}, w - \sum_{i\in I}  \mu_{i} u_{i}+ \sum_{i\in I}  \lambda_{i} \overline{\mu}_{i},$$
$$since the u_{i} are orthogonal to v - \sum_{i}  \lambda_{i} u_{i} and w - \sum_{i}  \mu_{i} u_{i} for all i \in I. This proves that$$
for every $\epsilon  > 0$, there is some $finite^{\in I}$ subset I of $K such^{\in I}$ that
$$\langle v, w\rangle - \sum_{i\in I}  \lambda_{i} \overline{\mu}_{i} < \epsilon .$$
We already know from Proposition A.3 that $(\lambda_{k} \overline{\mu}_{k})_{k\in K}$ is summable, and since $\epsilon  > 0$ is arbitrary we get
$$\langle v, w\rangle = \sum_{k\in K}  \lambda_{k} \overline{\mu}_{k}.$$
The next proposition states properties characterizing Hilbert bases (total orthogonal families).

> **Proposition A.5.** Let $E$ be a Hilbert space, and let $(u_{k})_{k\in K}$ be an orthogonal family in $E$. The following properties are equivalent:

<!-- PAGE 2163 -->
$(1)$ The family $(u_{k})_{k\in K}$ is a total orthogonal family.
$(2)$ For every vector $v \in E$, if $(c_{k})$  are the Fourier coefficients of $v$, then the family
$$(c_{k}u_{k})_{k\in K} is summable and v = \sum_{k}^{k\in K}  \in K c_{k}u_{k}.$$
$(3)$ For every vector $v \in E$, we have the Parseval identity:
$$\|v\|^{2}= \sum_{k\in K}  |c_{k}|^{2}.$$
$(4)$ For every vector $u \in E$, if $\langle u, u_{k}\rangle = 0$ for all $k \in K$, then $u = 0$. See Figure A.2.
$$v, u$$
$$k$$
$$form c  =$$
$$v=\Sigma_{ckuk} k\overline{2}$$
$$u$$
$$k       Kek$$
$$\overline{E}_{=k}^{V = span(u  )}$$
**Figure A.2:** A schematic illustration of Proposition A.5. Since $(u_{k})_{k\in K}$ is a Hilbert basis, $V = E$. Then given a vector of $E$, if we form the Fourier coefficients $c_{k}$, then form the
$$Fourier series \sum_{k}  \in K c_{k}u_{k}, we are ensured that v is equal to its Fourier series.$$

*Proof.* The equivalence of $(1), (2)$, and $(3)$ is an immediate consequence of Proposition A.2 and Proposition A.4.
$(4)$ If $(u_{k})_{k\in K}$ is a total orthogonal family and $\langle u, u_{k}\rangle = 0$ for all $k \in K$, since $u =$
$$\sum_{k}  \in K c_{k}u_{k} where c_{k} = \langle u, u_{k}\rangle /\|u_{k}\|^{2}, we have c_{k} = 0 for all k \in K, and u = 0.$$
Conversely, assume that the closure $V$ of $(u_{k})_{k\in K}$ is different from $E$. Then by Proposition 48.7, we have $E = V \oplus V^{\perp}$ , where $V^{\perp}$ is the orthogonal complement of $V$ , and $V^{\perp}$ is nontrivial since V̸ $= E$. As a consequence, there is some nonnull vector $u \in V^{\perp}$ . But then $u$ is orthogonal to every vector in $V$ , and in particular,
$$\langle u, u_{k}\rangle = 0$$
for all $k \in K$, which, by assumption, implies that $u = 0$, contradicting the fact that $u \neq 0$.

<!-- PAGE 2164 -->
Remarks:
$(1)$ If $E$ is a Hilbert space and $(u_{k})_{k\in K}$ is a total orthogonal family in $E$, there is a simpler argument to prove that $u = 0$ if $\langle u, u_{k}\rangle = 0$ for all $k \in K$ based on the continuity of $\langle$ -, $-\rangle$ . The argument is to prove that the assumption implies that $\langle v, u\rangle = 0$ for all $v \in E$. Since $\langle$ -, $-\rangle$ is positive definite, this implies that $u = 0$. By continuity of $\langle$ -, $-\rangle$ , for every $\epsilon  > 0$, there is some $\eta  > 0$ such that for every finite subset I of $K$, for every family $(\lambda_{i} )_{i\in I}$, for every $v \in E$,
$$\langle v, u\rangle -* \sum_{i\in I}  \lambda_{i} u_{i}, u+




$< \epsilon$$$ whenever
$$v - \sum_{i\in I}  \lambda_{i} u_{i} < \eta .$$
Since $(u_{k})_{k\in K}$ is dense in $E$, for every $v \in E$, there is some finite subset I of $K$ and some family $(\lambda_{i} )_{i\in I}$ such that
$$v - \sum_{i\in I}  \lambda_{i} u_{i} < \eta ,$$
$$and since by assumption, \sum_{i}  \in I \lambda_{i} u_{i}, u= 0, we get$$
$$|\langle v, u\rangle | < \epsilon .$$
Since this holds for every $\epsilon  > 0$, we must have $\langle v, u\rangle = 0$
$(2)$ If $V$ is any nonempty subset of $E$, the kind of argument used in the previous remark can be used to prove that $V^{\perp}$ is closed (even if $V$ is not), and that $V^{\perp \perp}$ is the closure of $V$ . We will now prove that every Hilbert space has some Hilbert basis. This requires using a fundamental theorem from set theory known as Zorn’s lemma, which we quickly review. Given any set $X$ with a partial ordering $\le$ , recall that a nonempty subset $C$ of $X$ is a chain if it is totally ordered (i.e., for all $x, y \in C$, either $x \le y$ or $y \le x)$. A nonempty subset $Y$ of $X$ is bounded iff there is some $b \in X$ such that $y \le b$ for all $y \in Y$ . Some $m \in X$ is maximal iff for every $x \in X, m \le x$ implies that $x = m$. We can now state Zorn’s lemma. For more details, see Rudin $[145]$, Lang $[113]$, or Artin $[7]$.

> **Proposition A.6.** (Zorn’s lemma) Given any nonempty partially ordered set $X$, if every
(nonempty) chain in $X$ is bounded, then $X$ has some maximal element.

<!-- PAGE 2165 -->
We can now prove the existence of Hilbert bases. We define a partial order on families $(u_{k})_{k\in K}$ as follows: for any two families $(u_{k})_{k\in K1}$ and $(v_{k})_{k\in K2}$, we say that
$$(u_{k})_{k\in K1} \le (v_{k})_{k\in K2}$$
iff $K_{1} \subseteq K_{2}$ and $u_{k} = v_{k}$ for all $k \in K_{1}$. This is clearly a partial order.

> **Proposition A.7.** Let $E$ be a Hilbert space. Given any orthogonal family $(u_{k})_{k\in K}$ in $E$, there is a total orthogonal family $(u_{l})_{l\in L}$ containing $(u_{k})_{k\in K}$.

*Proof.* Consider the set $\mathcal{S}$ of all orthogonal families greater than or equal to the family $B = (u_{k})_{k\in K}$. We claim that every chain in $\mathcal{S}$ is bounded. Indeed, if $C = (C_{l})_{l\in L}$ is a chain in $\mathcal{S}$, where $C_{l} = (u_{k,l})_{k\in Kl}$, the union family
$$(u_{k})_{k}, where u_{k} = u_{k,l} whenever k \in K_{l},$$
$$\bigcup_{\in l\in}  L Kl$$
is clearly an upper bound for $C$, and it is immediately verified that it is an orthogonal family. By Zorn’s Lemma A.6, there is a maximal family $(u_{l})_{l\in L}$ containing $(u_{k})_{k\in K}$. If $(u_{l})_{l\in L}$ is not dense in $E$, then its closure $V$ is strictly contained in $E$, and by Proposition 48.7, the orthogonal complement $V^{\perp}$ of $V$ is nontrivial since V̸ $= E$. As a consequence, there is some nonnull vector $u \in V^{\perp}$ . But then $u$ is orthogonal to every vector in $(u_{l})_{l\in L}$, and we can form an orthogonal family strictly greater than $(u_{l})_{l\in L}$ by adding $u$ to this family, contradicting the maximality of $(u_{l})_{l\in L}$. Therefore, $(u_{l})_{l\in L}$ is dense in $E$, and thus it is a Hilbert basis.
Remark: It is possible to prove that all Hilbert bases for a Hilbert space $E$ have index sets $K$ of the same cardinality. For a proof, see Bourbaki $[27]$.

> **Definition A.4.** A Hilbert space $E$ is separable if its Hilbert bases are countable. At last, we can prove that every Hilbert space is isomorphic to some Hilbert space $\ell^{2} (K)$ for some suitable $K$.

> **Theorem A.8.** (Riesz–Fischer) For every Hilbert space $E$, there is some nonempty set $K$ such that $E$ is isomorphic to the Hilbert space $\ell^{2} (K)$. More specifically, for any Hilbert basis $(u_{k})_{k\in K}$ of $E$, the maps $f$ : $\ell^{2} (K) \to E$ and $g: E \to \ell^{2} (K)$ defined such that
$$f ((\lambda_{k} )_{k\in K}) = \sum_{k\in K}  \lambda_{k} u_{k}andg(u) = \begin{pmatrix} \langle u, u_{k}\rangle /\|u_{k} \end{pmatrix} \|_{k\in K}^{2} = (c_{k})_{k\in K},$$
are bijective linear isometries such that $g \circ f =$ id and $f \circ g =$ id.

*Proof.* By Proposition A.4 $(1)$, the map $f$ is well defined, and it is clearly linear. By Proposition A.2 $(3)$, the map $g$ is well defined, and it is also clearly linear. By Proposition A.2 (2b), we have
$$f(g(u)) = u = \sum_{k\in K}  c_{k}u_{k},$$

<!-- PAGE 2166 -->
and by Proposition A.4 $(1)$, we have
$$g(f ((\lambda_{k} )_{k\in K})) = (\lambda_{k} )_{k\in K},$$
and thus $g \circ f =$ id and $f \circ g =$ id. By Proposition A.4 $(2)$, the linear map $g$ is an isometry. Therefore, $f$ is a linear bijection and an isometry between $\ell^{2} (K)$ and $E$, with inverse $g$.
Remark: The surjectivity of the map $g: E \to \ell^{2} (K)$ is known as the Riesz–Fischer theorem. Having done all this hard work, we sketch how these results apply to Fourier series. Again we refer the readers to Rudin $[145]$ or Lang $[115, 116]$ for a comprehensive exposition. Let $\mathcal{C}(T)$ denote the set of all periodic continuous functions $f$ : $[-\pi , \pi$ ] $\to \mathbb{C}$ with period $2\pi$ . There is a Hilbert space $L^{2}(T)$ containing $\mathcal{C}(T)$ and such that $\mathcal{C}(T)$ is dense in $L^{2}(T)$, whose inner product is given by
$$\langle f, g\rangle = \int_{-}^{}  \pi f(x)\overline{g}\overline{(}\overline{x}\overline{)} dx.$$
$$\pi$$
The Hilbert space $L^{2}(T)$ is the space of Lebesgue square-integrable periodic functions (of period $2\pi$ ). It turns out that the family $(e^{ikx})_{k\in Z}$ is a total orthogonal family in $L^{2}(T)$, because it is already dense in $\mathcal{C}(T)$ (for instance, see Rudin $[145])$. Then the Riesz–Fischer theorem says that for every family $(c_{k})_{k\in Z}$ of complex numbers such that
$$\sum_{k\in Z}  |c_{k}|^{2}< \infty ,$$
there is a unique function $f \in L^{2}(T)$ such that $f$ is equal to its Fourier series
$$f(x) = \sum_{k\in Z}  c_{k}e^{ikx},$$
where the Fourier coefficients $c_{k}$ of $f$ are given by the formula
$$c_{k} = \frac{1}{2\pi} \int_{-}^{}  \pi f(t)e^{-ikt}dt.$$
$$\pi$$
The Parseval theorem says that
$$\sum_{k=-\infty}^{+\infty}  c_{k}\overline{d}_{k} = \frac{1}{2\pi} \int_{-}^{}  \pi f(t)\overline{g}\overline{(}\overline{t}\overline{)} dt$$
$$\pi$$
for all $f, g \in L^{2}(T)$, where $c_{k}$ and $d_{k}$ are the Fourier coefficients of $f$ and $g$.
