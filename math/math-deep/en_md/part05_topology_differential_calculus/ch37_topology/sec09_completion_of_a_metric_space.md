# Completion of a Metric Space


<!-- PAGE 1410 -->

*Proof.* Assume $x \in \overline{A}$. By Proposition 37.13, there is some sequence $(a_{n})$ of points $a_{n} \in A$ which converges to $x$. Consequently $(a_{n})$ is a Cauchy sequence in $E$, and thus a Cauchy sequence in $A$ (since $a_{n} \in A$ for all $n)$. Since $A$ is complete, the sequence $(a_{n})$ has a limit $a \in A$, but since $E$ is a metric space it is Hausdorff, so $a = x$, which shows that $x \in A$; that is, $A$ is closed.

> **Proposition 37.51.** Let $(E, d)$ be a metric space, and let $A$ be a subset of $E$. If $E$ is complete and if $A$ is closed in $E$, then $A$ is complete.

*Proof.* Let $(a_{n})$ be a Cauchy sequence in $A$. The sequence $(a_{n})$ is also a Cauchy sequence in $E$, and since $E$ is complete, it has a limit $x \in E$. But $a_{n} \in A$ for all $n$, so by Proposition 37.13 we must have $x \in \overline{A}$. Since $A$ is closed, actually $x \in A$, which proves that $A$ is complete. An arbitrary metric space $(E, d)$ is not necessarily complete, but there is a construction of a metric space (E,d) such that $E$ is complete, and there is a continuous (injective) distance-
$$b b b$$
preserving map $\phi$ : $E \to E$ such that $\phi (E)$ is dense in $E$. This is a generalization of the
$$b b$$
construction of the set $\mathbb{R}$ of real numbers from the set $\mathbb{Q}$ of rational numbers in terms of Cauchy sequences. This construction can be immediately adapted to a normed vector space $(E, \|\|)$ to embed $(E, \|\|)$ into a complete normed vector space $(E, \|\|_{E})$ (a Banach space).
$$b$$
$$b$$
This construction is used heavily in integration theory, where $E$ is a set of functions.

## 37.9 Completion of a Metric Space

In order to prove a kind of uniqueness result for the completion (E,d) of a metric space
$$b b$$
$(E, d)$, we need the following result about extending a uniformly continuous function. Recall that $E_{0}$ is dense in $E$ iff $\overline{E}_{0} = E$. Since $E$ is a metric space, by Proposition 37.13, this means that for every $x \in E$, there is some sequence $(x_{n})$ converging to $x$, with $x_{n} \in E_{0}$.

> **Theorem 37.52.** Let $E$ and $F$ be two metric spaces, let $E_{0}$ be a dense subspace of $E$, and let $f_{0}$ : $E_{0} \to F$ be a continuous function. If $f_{0}$ is uniformly continuous and if $F$ is complete, then there is a unique uniformly continuous function $f$ : $E \to F$ extending $f_{0}$.

*Proof.* We follow Schwartz’s proof; see Schwartz $[155]$ (Chapter XI, Section $3$, Theorem $1)$. Step $1$. We begin by constructing a function $f$ : $E \to F$ extending $f_{0}$. Since $E_{0}$ is dense in $E$, for every $x \in E$, there is some sequence $(x_{n})$ converging to $x$, with $x_{n} \in E_{0}$. Then the sequence $(x_{n})$ is a Cauchy sequence in $E$. We claim that $(f_{0}(x_{n}))$ is a Cauchy sequence in $F$. Proof of the claim. For every $\epsilon  > 0$, since $f_{0}$ is uniformly continuous, there is some $\eta  > 0$ such that for all $(y, z) \in E_{0}$, if d(y, $z) \le \eta$ , then $d(f_{0}(y), f_{0}(z)) \le \epsilon$ . Since $(x_{n})$ is a Cauchy sequence with $x_{n} \in E_{0}$, there is some integer $p > 0$ such that if $m, n \ge p$, then $d(x_{m}, x_{n}) \le \eta$ , thus $d(f_{0}(x_{m}), f_{0}(x_{n})) \le \epsilon$ , which proves that $(f_{0}(x_{n}))$ is a Cauchy sequence in $F$.

<!-- PAGE 1411 -->
Since $F$ is complete and $(f_{0}(x_{n}))$ is a Cauchy sequence in $F$, the sequence $(f_{0}(x_{n}))$ converges to some element of $F$; denote this element by f(x). Step $2$. Let us now show that f(x) does not depend on the sequence $(x_{n})$ converging to $x$. Suppose that $(x_{n}')$ and $(x_{n}'')$ are two sequences of elements in $E_{0}$ converging to $x$. Then the mixed sequence
$$x_{0}', x_{0}'', x_{1}', x_{1}'', \dots  , x_{n}', x_{n}'', \dots  ,$$
also converges to $x$. It follows that the sequence
$$f_{0}(x_{0}'), f_{0}(x_{0}''), f_{0}(x_{1}'), f_{0}(x_{1}''), \dots  , f_{0}(x_{n}'), f_{0}(x_{n}''), \dots  ,$$
is a Cauchy sequence in $F$, and since $F$ is complete, it converges to some element of $F$, which implies that the sequences $(f_{0}(x_{n}'))$ and $(f_{0}(x_{n}''))$ converge to the same limit. As a summary, we have defined a function $f$ : $E \to F$ by
$$f(x) = limf_{0}(x_{n}).$$
$$n\mapsto \infty$$
for any sequence $(x_{n})$ converging to $x$, with $x_{n} \in E_{0}$. Step $3$. The function $f$ extends $f_{0}$. Since every element $x \in E_{0}$ is the limit of the constant sequence $(x_{n})$ with $x_{n} = x$ for all $n \ge 0$, by definition f(x) is the limit of the sequence $(f_{0}(x_{n}))$, which is the constant sequence with value $f_{0}(x)$, so f(x) $= f_{0}(x)$; that is, $f$ extends $f_{0}$. Step $4$. We now prove that $f$ is uniformly continuous. Since $f_{0}$ is uniformly continuous, for every $\epsilon  > 0$, there is some $\eta  > 0$ such that if a, $b \in E_{0}$ and d(a, $b) \le \eta$ , then $d(f_{0}(a), f_{0}(b)) \le \epsilon$ . Consider any two points $x, y \in E$ such that d(x, $y) \le \eta /2$. We claim that d(f(x), f(y)) $\le \epsilon$ , which shows that $f$ is uniformly continuous. Let $(x_{n})$ be a sequence of points in $E_{0}$ converging to $x$, and let $(y_{n})$ be a sequence of points in $E_{0}$ converging to $y$. By the triangle inequality,
$$d(x_{n}, y_{n}) \le d(x_{n}, x) + d(x, y) + d(y, y_{n}) = d(x, y) + d(x_{n}, x) + d(y_{n}, y),$$
and since $(x_{n})$ converges to $x$ and $(y_{n})$ converges to $y$, there is some integer $p > 0$ such that for all $n \ge p$, we have $d(x_{n}, x) \le \eta /4$ and $d(y_{n}, y) \le \eta /4$, and thus
$$d(x_{n}, y_{n}) \le d(x, y) + \frac{\eta}{2} .$$
Since we assumed that d(x, $y) \le \eta /2$, we get $d(x_{n}, y_{n}) \le \eta$  for all $n \ge p$, and by uniform continuity of $f_{0}$, we get
$$d(f_{0}(x_{n}), f_{0}(y_{n})) \le \epsilon$$
for all $n \ge p$. Since the distance function on $F$ is also continuous, and since $(f_{0}(x_{n}))$ converges to f(x) and $(f_{0}(y_{n}))$ converges to f(y), we deduce that the sequence $(d(f_{0}(x_{n}), f_{0}(y_{n})))$ converges to d(f(x), f(y)). This implies that d(f(x), f(y)) $\le \epsilon$ , as desired.

<!-- PAGE 1412 -->
Step $5$. It remains to prove that $f$ is unique. Since $E_{0}$ is dense in $E$, for every $x \in E$, there is some sequence $(x_{n})$ converging to $x$, with $x_{n} \in E_{0}$. Since $f$ extends $f_{0}$ and since $f$ is continuous, we get
$$f(x) = limf_{0}(x_{n}),$$
$$n\mapsto \infty$$
which only depends on $f_{0}$ and $x$, and shows that $f$ is unique.
Remark: It can be shown that the theorem no longer holds if we either omit the hypothesis that $F$ is complete or omit that $f_{0}$ is uniformly continuous. For example, if $E_{0} \neq  E$ and if we let $F = E_{0}$ and $f_{0}$ be the identity function, it is easy to see that $f_{0}$ cannot be extended to a continuous function from $E$ to $E_{0}$ (for any $x \in E$ - $E_{0}$, any continous extension $f$ of $f_{0}$ would satisfy f(x) $= x$, which is absurd since $x \in / E_{0})$. If $f_{0}$ is continuous but not uniformly continuous, a counter-example can be given by using $E =\mathbb{R} =\mathbb{R} \cup {\infty$ } made into a metric space, $E_{0} =\mathbb{R}, F =\mathbb{R}$, and $f_{0}$ the identity function; for details, see Schwartz $[155]$ (Chapter XI, Section $3$, page $134)$.

> **Definition 37.39.** If $(E, d_{E})$ and $(F, d_{F})$ are two metric spaces, then a function $f$ : $E \to F$ is distance-preserving, or an isometry, if
$$d_{F}(f(x), f(y)) = d_{E}(x, y),for all for all x, y \in E.$$
Observe that an isometry must be injective, because if f(x) $=$ f(y), then $d_{F}(f(x)$, f(y)) $= 0$, and since $d_{F}(f(x)$, f(y)) $= d_{E}(x, y)$, we get $d_{E}(x, y) = 0$, but $d_{E}(x, y) = 0$ implies that $x = y$. Also, an isometry is uniformly continuous (since we can pick $\eta  = \epsilon$  to satisfy the condition of uniform continuity). However, an isometry is not necessarily surjective. We now give a construction of the completion of a metric space. This construction is just a generalization of the classical construction of $\mathbb{R}$ from $\mathbb{Q}$ using Cauchy sequences.

> **Theorem 37.53.** Let $(E, d)$ be any metric space. There is a complete metric space (E,d)
$$b b$$
called a completion of $(E, d)$, and a distance-preserving (uniformly continuous) map $\phi$ : $E \to E$ such that $\phi (E)$ is dense in $E$, and the following extension property holds: for every $b  b$ complete metric space $F$ and for every uniformly continuous function $f$ : $E \to F$, there is a unique uniformly continuous function $f$ : $E \to F$ such that
$$b b$$
$$f =f \circ \phi ,$$
$$b$$
as illustrated in the following diagram.
$$EE$$
$$\overline{@}^{\phi}\overline{@} b$$
$$\overline{@}@$$
$$@@$$
$$@@^{fb}$$
$$f$$
$$F.$$
As a consequence, for any two completions $(E_{1},d_{1})$ and $(E_{2},d_{2})$ of $(E, d)$, there is a unique
$$b b b b$$
bijective isometry betwen $(E_{1},d_{1})$ and $(E_{2},d_{2})$.
$$b b b b$$

<!-- PAGE 1413 -->

*Proof.* Consider the set $\mathcal{E}$ of all Cauchy sequences $(x_{n})$ in $E$, and define the relation $\sim$ on $\mathcal{E}$ as follows:
$$(x_{n}) \sim (y_{n})iff limd(x_{n}, y_{n}) = 0.$$
$$n\mapsto \infty$$
It is easy to check that $\sim$ is an equivalence relation on $\mathcal{E}$, and let $E =\mathcal{E}/ \sim$ be the quotient
$$b$$
set, that is, the set of equivalence classes modulo $\sim$ . Our goal is to show that we can endow $E$ with a distance that makes it into a complete metric space satisfying the conditions of the $b$ theorem. We proceed in several steps. Step $1$. First, let us construct the function $\phi$ : $E \to E$. For every $a \in E$, we have the
$$b$$
constant sequence $(a_{n})$ such that $a_{n} = a$ for all $n \ge 0$, which is obviously a Cauchy sequence. Let $\phi (a) \in E$ be the equivalence class $[(a_{n})]$ of the constant sequence $(a_{n})$ with $a_{n} = a$ for all
$$b$$
$n$. By definition of $\sim$ , the equivalence class $\phi$ (a) is also the equivalence class of all sequences converging to a. The map $a \mapsto \phi$ (a) is injective because a metric space is Hausdorff, so if $a \neq  b$, then a sequence converging to a does not converge to $b$. After having defined a distance on $E$, we will check that $\phi$  is an isometry.
$$b$$
Step $2$. Let us now define a distance on $E$. Let $\alpha  = [(a_{n})]$ and $\beta  = [(b_{n})]$ be two
$$b$$
equivalence classes of Cauchy sequences in $E$. The triangle inequality implies that $d(a_{m}, b_{m}) \le d(a_{m}, a_{n}) + d(a_{n}, b_{n}) + d(b_{n}, b_{m}) = d(a_{n}, b_{n}) + d(a_{m}, a_{n}) + d(b_{m}, b_{n})$ and $d(a_{n}, b_{n}) \le d(a_{n}, a_{m}) + d(a_{m}, b_{m}) + d(b_{m}, b_{n}) = d(a_{m}, b_{m}) + d(a_{m}, a_{n}) + d(b_{m}, b_{n})$, which implies that
$$|d(a_{m}, b_{m}) -d(a_{n}, b_{n})| \le d(a_{m}, a_{n}) + d(b_{m}, b_{n}).$$
Since $(a_{n})$ and $(b_{n})$ are Cauchy sequences, it follows that $(d(a_{n}, b_{n}))$ is a Cauchy sequence of nonnegative reals. $Since\mathbb{R}$ is complete, the sequence $(d(a_{n}, b_{n}))$ has a limit, which we denote by $d(\alpha , \beta$ ); that is, we set $b$
$$d(\alpha , \beta ) = limd(a_{n}, b_{n}),\alpha  = [(a_{n})], \beta  = [(b_{n})].$$
$$b$$
$$n\mapsto \infty$$
Step $3$. Let us check that $d(\alpha , \beta$ ) does not depend on the Cauchy sequences $(a_{n})$ and
$$b$$
$(b_{n})$ chosen in the equivalence classes $\alpha$  and $\beta$ . If $(a_{n}) \sim (a_{n}')$ and $(b_{n}) \sim (b_{n}')$, then $lim_{n\mapsto \infty} d(a_{n}, a_{n}') = 0$ and $lim_{n\mapsto \infty} d(b_{n}, b_{n}') = 0$, and since
$$d(a_{n}', b_{n}') \le d(a_{n}', a_{n}) + d(a_{n}, b_{n}) + d(b_{n}, b_{n}') = d(a_{n}, b_{n}) + d(a_{n}, a_{n}') + d(b_{n}, b_{n}')$$
and
$$d(a_{n}, b_{n}) \le d(a_{n}, a_{n}') + d(a_{n}', b_{n}') + d(b_{n}', b_{n}) = d(a_{n}', b_{n}') + d(a_{n}, a_{n}') + d(b_{n}, b_{n}')$$

<!-- PAGE 1414 -->
we have
$$|d(a_{n}, b_{n}) -d(a_{n}', b_{n}')| \le d(a_{n}, a_{n}') + d(b_{n}, b_{n}'),$$
so we have $lim_{n\mapsto \infty} d(a_{n}', b_{n}') = lim_{n\mapsto \infty} d(a_{n}, b_{n}) = d(\alpha , \beta$ ). Therefore, $d(\alpha , \beta$ ) is indeed well
$$b b$$
defined. Step $4$. Let us check that $\phi$  is indeed an isometry. Given any two elements $\phi$ (a) and $\phi (b)$ in $E$, since they are the equivalence classes of
$$b$$
the constant sequences $(a_{n})$ and $(b_{n})$ such that $a_{n} = a$ and $b_{n} = b$ for all $n$, the constant sequence $(d(a_{n}, b_{n}))$ with $d(a_{n}, b_{n}) =$ d(a, $b)$ for all $n$ converges to d(a, $b)$, so by definition $d(\phi (a), \phi (b)) = lim_{n\mapsto \infty} d(a_{n}, b_{n}) =$ d(a, $b)$, which shows that $\phi$  is an isometry. $b$ Step $5$. Let us verify that $d$ is a metric on $E$. By definition it is obvious that $d(\alpha , \beta$ ) $=$
$$b b b$$
$d(\beta , \alpha$ ). If $\alpha$  and $\beta$  are two distinct equivalence classes, then for any Cauchy sequence $(a_{n}) b$ in the equivalence class $\alpha$  and for any Cauchy sequence $(b_{n})$ in the equivalence class $\beta$ , the sequences $(a_{n})$ and $(b_{n})$ are inequivalent, which means that $lim_{n\mapsto \infty} d(a_{n}, b_{n}) \neq  0$, that is, $d(\alpha , \beta$ ) $\neq  0$. Obviously, $d(\alpha , \alpha$ ) $= 0. b  b$ For any equivalence classes $\alpha  = [(a_{n})], \beta  = [(b_{n})]$, and $\gamma  = [(c_{n})]$, we have the triangle inequality
$$d(a_{n}, c_{n}) \le d(a_{n}, b_{n}) + d(b_{n}, c_{n}),$$
so by continuity of the distance function, by passing to the limit, we obtain
$$d(\alpha , \gamma ) \le d(\alpha , \beta ) +d(\beta , \gamma ),$$
$$bb b$$
which is the triangle inequality for $d$. Therefore, $d$ is a distance on $E$.
$$b b b$$
Step $6$. Let us prove that $\phi (E)$ is dense in $E$. For any $\alpha  = [(a_{n})]$, let $(x_{n})$ be the constant
$$b$$
sequence such that $x_{k} = a_{n}$ for all $k \ge 0$, so that $\phi (a_{n}) = [(x_{n})]$. Then we have
$$d(\alpha , \phi (a_{n})) = limd(a_{m}, a_{n}) \le supd(a_{p}, a_{q}).$$
$$b$$
$$m\mapsto \infty p,q\ge n$$
Since $(a_{n})$ is a Cauchy sequence, $sup_{p,q\ge n} d(a_{p}, a_{q})$ tends to $0$ as $n$ goes to infinity, so
$$limd(\alpha , \phi (a_{n})) = 0,$$
$$n\mapsto \infty$$
which means that the sequence $(\phi (a_{n}))$ converge to $\alpha$ , and $\phi (E)$ is indeed dense in $E$.
$$b$$
Step $7$. Finally, let us prove that the metric space $E$ is complete.
$$b$$
Let $(\alpha_{n}$ ) be a Cauchy sequence in $E$. Since $\phi (E)$ is dense in $E$, for every $n > 0$, there
$$b b$$
some $a_{n} \in E$ such that
$$db(\alpha_{n} , \phi (a_{n})) \le \frac{1}{n} .$$
Since
$$db(\phi (a_{m}), \phi (a_{n})) \le db(\phi (a_{m}), \alpha_{m} ) + db(\alpha_{m} , \alpha_{n} ) + db(\alpha_{n} , \phi (a_{n})) \le db(\alpha_{m} , \alpha_{n} ) + \frac{1}{m} + \frac{1}{n} ,$$

<!-- PAGE 1415 -->
and since $(\alpha_{m}$ ) is a Cauchy sequence, so is $(\phi (a_{n}))$, and as $\phi$  is an isometry, the sequence $(a_{n})$ is a Cauchy sequence in $E$. Let $\alpha  \in E$ be the equivalence class of $(a_{n})$. Since
$$b$$
$$d(\alpha , \phi (a_{n})) = limd(a_{m}, a_{n})$$
$$b$$
$$m\mapsto \infty$$
and $(a_{n})$ is a Cauchy sequence, we deduce that the sequence $(\phi (a_{n}))$ converges to $\alpha$ , and since $d(\alpha_{n} , \phi (a_{n})) \le 1/n$ for all $n > 0$, the sequence $(\alpha_{n}$ ) also converges to $\alpha$ . Step $8$. Let us prove the extension property. Let $F$ be any complete metric space and let $f$ : $E \to F$ be any uniformly continuous function. The function $\phi$ : $E \to E$ is an isometry
$$b$$
and a bijection between $E$ and its image $\phi (E)$, so its inverse $\phi^{-1}$ : $\phi (E) \to E$ is also an isometry, and thus is uniformly continuous. If we let $g = f \circ \phi^{-1}$ , then $g: \phi (E) \to F$ is a uniformly continuous function, and $\phi (E)$ is dense in $E$, so by Theorem 37.52 there is a
$$b$$
unique uniformly continuous function $f$ : $E \to F$ extending $g = f \circ \phi^{-1}$ ; see the diagram
$$b b$$
below:
$$E\overline{R}\overline{R}^{\phi-1}\phi (E)\subseteq E$$
$$\overline{R}\overline{R} Db$$
$$\overline{R} RD$$
$$RRDD$$
$$RRD^{g}$$
$$RRDD$$
$$RRD$$
$$fRRD _{b}^{f}$$
$$RR"$$
$$($$
$$F$$
This means that
$$f|\phi (E) = f \circ \phi^{-1} ,$$
$$b$$
which implies that
$$(f|\phi (E)) \circ \phi  = f,$$
$$b$$
that is, $f = f \circ \phi$ , as illustrated in the diagram below:
$$b$$
$$EE$$
$$\overline{@}^{\phi}\overline{@} b$$
$$\overline{@}@$$
$$@@$$
$$@@^{fb}$$
$$f$$
$$F$$
If $h: E \to F$ is any other uniformly continuous function such that $f = h \circ \phi$ , then
$$b$$
$g = f \circ \phi^{-1} = h|\phi (E)$, so $h$ is a uniformly continuous function extending $g$, and by Theorem 37.52, we have have $h = f$, so $f$ is indeed unique.
$$b b$$
Step $9$. Uniqueness of the completion (E,d) up to a bijective isometry.
$$b b$$
Let $(E_{1},d_{1})$ and $(E_{2},d_{2})$ be any two completions of $(E, d)$. Then we have two uniformly
$$b b b b$$
continuous isometries $\phi_{1}$  : $E \to E_{1}$ and $\phi_{2}$  : $E \to E_{2}$ , so by the unique extension property,
$$bb$$
there exist unique uniformly continuous maps $\phi_{2}$  : $E_{1} \to E_{2}$ and $\phi_{1}$  : $E_{2} \to E_{1}$ such that the
$$c bb c bb$$
following diagrams commute:
$$EE_{1}EE_{2}$$
$$\overline{>}^{\phi1}\overline{>} b\overline{@}^{\phi2}\overline{@} b$$
$$\overline{>}>\overline{@}@$$
$$>>@@$$
$$\phi >\phi 2\phi @\phi 1$$
$$2>c1@c$$
$$E_{2}E_{1}.$$
$$bb$$

<!-- PAGE 1416 -->
Consequently we have the following commutative diagrams:
$$E_{2}E_{1}$$
$$?b?b$$
$$ ~$$
$$  ~~$$
$$\phi 2 \phi 1~$$
$$ \phi 1~\phi 2$$
$$ _{\phi} c~c$$
$$ ~_{\phi}$$
$$~$$
$$EE_{1}EE_{2}$$
$$\overline{>}\overline{>}^{1}b\overline{@}\overline{@}^{2}b$$
$$\overline{>}>\overline{@}@$$
$$>>@@$$
$$\phi >\phi 2\phi @\phi 1$$
$$2>c1@c$$
$$E_{2}E_{1}.$$
$$bb$$
However, $id_{Eb1}$ and $id_{Eb2}$ are uniformly continuous functions making the following diagrams commute
$$EE_{1}EE_{2}$$
$$\overline{>}^{\phi1}\overline{>} b\overline{?}^{\phi2}\overline{?} b$$
$$\overline{>}>\overline{?}?$$
$$>>id??id$$
$$\phi >> bE1\phi ?? bE2$$
$$12$$
$$E_{1}E_{2},$$
$$bb$$
so by the uniqueness of extensions we must have
$$\phi_{1}  \circ \phi_{2}  = id_{Eb1}and\phi_{2}  \circ \phi_{1}  = id_{Eb2}.$$
$$cccc$$
This proves that $\phi_{1}$  and $\phi_{2}$  are mutual inverses. Now, since $\phi_{2}  = \phi_{2}  \circ \phi_{1}$ , we have
$$c c c$$
$$\phi_{2} |\phi_{1} (E) = \phi_{2}  \circ \phi_{1}^{-1}  ,$$
$$c$$
and since $\phi_{1}^{-1}$ and $\phi_{2}$  are isometries, so is $\phi_{2} |\phi_{1} (E)$. But we saw earlier that $\phi_{2}$  is the
$$c c$$
uniform continuous extension of $\phi_{2} |\phi_{1} (E)$ and $\phi_{1} (E)$ is dense in $E_{1}$, so for any two elements
$$c b$$
$\alpha , \beta  \in E_{1}$, if $(a_{n})$ and $(b_{n})$ are sequences in $\phi_{1} (E)$ converging to $\alpha$  and $\beta$ , we have
$$b$$
$$d_{2}((\phi_{2} |\phi_{1} (E))(a_{n}), ((\phi_{2} |\phi_{1} (E))(b_{n})) =d_{1}(a_{n}, b_{n}),$$
$$bcc b$$
and by passing to the limit we get
$$d_{2}(\phi_{2} (\alpha ),\phi_{2} (\beta )) =d_{1}(\alpha , \beta ),$$
$$bc c b$$
which shows that $\phi_{2}$  is an isometry (similarly, $\phi_{1}$  is an isometry).
$$c c$$
Remarks: $1$. Except for Step $8$ and Step $9$, the proof of Theorem 37.53 is the proof given in Schwartz $[155]$ (Chapter XI, Section $4$, Theorem $1)$, and Kormogorov and Fomin $[108]$ (Chapter $2$, Section $7$, Theorem $4). 2$. The construction of $E$ relies on the completeness of $\mathbb{R}$, and so it cannot be used to
$$b$$
$construct\mathbb{R} from\mathbb{Q}$. However, this construction can be modified to yield a construction of $\mathbb{R}$ from $\mathbb{Q}$. We show in Section 37.12 that Theorem 37.53 yields a construction of the completion of a normed vector space.
