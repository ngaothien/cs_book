# The Contraction Mapping Theorem


<!-- PAGE 1417 -->

## 37.10 The Contraction Mapping Theorem

If $(E, d)$ is a nonempty complete metric space, every map, $f$ : $E \to E$, for which there is some $k$ such that $0 \le k < 1$ and
$$d(f(x), f(y)) \le kd(x, y)$$
for all $x, y \in E$, has the very important property that it has a unique fixed point, that is, there is a unique, $a \in E$, such that f(a) $= a$. A map as above is called a contraction mapping. Furthermore, the fixed point of a contraction mapping can be computed as the limit of a fast converging sequence. The fixed point property of contraction mappings is used to show some important theorems of analysis, such as the implicit function theorem and the existence of solutions to certain differential equations. It can also be used to show the existence of fractal sets defined in terms of iterated function systems. Since the proof is quite simple, we prove the fixed point property of contraction mappings. First, observe that a contraction mapping is
(uniformly) continuous.

> **Proposition 37.54.** If $(E, d)$ is a nonempty complete metric space, every contraction mapping, $f$ : $E \to E$, has a unique fixed point. Furthermore, for every $x_{0} \in E$, defining the sequence, $(x_{n})$, such that $x_{n+1} = f(x_{n})$, the sequence, $(x_{n})$, converges to the unique fixed point of $f$.

*Proof.* First we prove that $f$ has at most one fixed point. Indeed, if f(a) $= a$ and f(b) $= b$, since
$$d(a, b) = d(f(a), f(b)) \le kd(a, b)$$
and $0 \le k < 1$, we must have d(a, $b) = 0$, that is, $a = b$. Next, we prove that $(x_{n})$ is a Cauchy sequence. Observe that
$$d(x_{2}, x_{1})\le kd(x_{1}, x_{0}),$$
$$d(x_{3}, x_{2})\le kd(x_{2}, x_{1}) \le k^{2}d(x_{1}, x_{0}),$$
$$\vdots \vdots$$
$$d(x_{n+1}, x_{n})\le kd(x_{n}, x_{n-1}) \le \cdots  \le k^{n}d(x_{1}, x_{0}).$$
Thus, we have
$$d(x_{n+p}, x_{n})\le d(x_{n+p}, x_{n+p-1}) + d(x_{n+p-1}, x_{n+p-2}) + \cdots  + d(x_{n+1}, x_{n})$$
$$\le (k^{p-1}+ k^{p-2}+ \cdots  + k + 1)k^{n}d(x_{1}, x_{0})$$
$$\le \frac{k^{n}}{1 -k} d(x_{1}, x_{0}).$$

<!-- PAGE 1418 -->
We conclude that $d(x_{n+p}, x_{n})$ converges to $0$ when $n$ goes to infinity, which shows that $(x_{n})$ is a Cauchy sequence. Since $E$ is complete, the sequence $(x_{n})$ has a limit, a. Since $f$ is continuous, the sequence $(f(x_{n}))$ converges to f(a). But $x_{n+1} = f(x_{n})$ converges to a and so f(a) $= a$, the unique fixed point of $f$. Note that no matter how the starting point $x_{0}$ of the sequence $(x_{n})$ is chosen, $(x_{n})$ converges to the unique fixed point of $f$. Also, the convergence is fast, since
$$d(x_{n}, a) \le \frac{k^{n}}{1 -k} d(x_{1}, x_{0}).$$
The Hausdorffdistance between compact subsets of a metric space provides a very nice illustration of some of the theorems on complete and compact metric spaces just presented.

> **Definition 37.40.** Given a metric space, $(X, d)$, for any subset, $A \subseteq X$, for any, $\epsilon  \ge 0$, define the $\epsilon$ -hull of $A$ as the set
$$V_{\epsilon}(A) = {x \in X, \exists a \in A | d(a, x) \le \epsilon }.$$
See Figure 37.46. Given any two nonempty bounded subsets, $A, B$ of $X$, define D(A, $B)$, the Hausdorffdistance between $A$ and $B$, by
$$D(A, B) = \inf{\epsilon  \ge 0 | A \subseteq V_{\epsilon}(B) and B \subseteq V_{\epsilon}(A)}.$$
$$A$$
$$V (A)$$
$$є$$
$$Figure 37.46: The \epsilon -hull of a polygonal region A of \mathbb{R}^{2}$$
Note that since we are considering nonempty bounded subsets, D(A, $B)$ is well defined (i.e., not infinite). However, $D$ is not necessarily a distance function. It is a distance function if we restrict our attention to nonempty compact subsets of $X$ (actually, it is also a metric on closed and bounded subsets). We let $\mathcal{K}(X)$ denote the set of all nonempty compact subsets of $X$. The remarkable fact is that $D$ is a distance on $\mathcal{K}(X)$ and that if $X$ is complete or compact, then so is $\mathcal{K}(X)$. The following theorem is taken from Edgar $[56]$.

<!-- PAGE 1419 -->

> **Theorem 37.55.** If $(X, d)$ is a metric space, then the Hausdorffdistance, $D$, on the set, $\mathcal{K}(X)$, of nonempty compact subsets of $X$ is a distance. If $(X, d)$ is complete, then $(\mathcal{K}(X), D)$ is complete and if $(X, d)$ is compact, then $(\mathcal{K}(X), D)$ is compact.

*Proof.* Since (nonempty) compact sets are bounded, D(A, $B)$ is well defined. Clearly $D$ is symmetric. Assume that D(A, $B) = 0$. Then for every $\epsilon  > 0, A \subseteq V_{\epsilon}(B)$, which means
$$that for every a \in A, there is some b \in B such \frac{that}{B} d(a, b) \le \epsilon , and thus, that A \subseteq \overline{B}.$$
Since Proposition 37.26 implies that $B$ is closed,  $= B$, and we have $A \subseteq B$. Similarly, $B \subseteq A$, and thus, $A = B$. Clearly, if $A = B$, we have D(A, $B) = 0$. It remains to prove the triangle inequality. Assume that D(A, $B) \le \epsilon_{1}$  and that D(B, $C) \le \epsilon_{2}$ . We must show that D(A, $C) \le \epsilon_{1}  + \epsilon_{2}$ . This will be accomplished if we can show that $C \subseteq V_{\epsilon1+\epsilon2}(A)$ and $A \subseteq V_{\epsilon1+\epsilon2}(C)$. By assumption and definition of $D, B \subseteq V_{\epsilon1}(A)$ and $C \subseteq V_{\epsilon2}(B)$. Then
$$V_{\epsilon2}(B) \subseteq V_{\epsilon2}(V_{\epsilon1}(A)),$$
and since a basic application of the triangle inequality implies that
$$V_{\epsilon2}(V_{\epsilon1}(A)) \subseteq V_{\epsilon1+\epsilon2}(A),$$
we get
$$C \subseteq V_{\epsilon2}(B) \subseteq V_{\epsilon1+\epsilon2}(A).$$
See Figure 37.47.
$$Vє (V (A))$$
$$2є$$
$$1$$
$$V (A)$$
$$є$$
$$1$$
$$AB$$
$$CV   (B)є$$
$$2$$
$$Vє є(A)$$
$$1 +2$$

![Figure 37.47](../../assets/ch37/fig_37_47.png)

**Figure 37.47:** Let $A$ be the small pink square and $B$ be the small purple triangle $in\mathbb{R}^{2}$. The periwinkle oval $C$ is contained in $V_{\epsilon1+\epsilon2}(A)$. Similarly, the conditions $(A, B) \le \epsilon_{1}$  and D(B, $C) \le \epsilon_{2}$  imply that
$$A \subseteq V_{\epsilon1}(B),B \subseteq V_{\epsilon2}(C).$$

<!-- PAGE 1420 -->
Hence
$$A \subseteq V_{\epsilon1}(B) \subseteq V_{\epsilon1}(V_{\epsilon2}(C)) \subseteq V_{\epsilon1+\epsilon2}(C),$$
and thus the triangle inequality follows. Next we need to prove that if $(X, d)$ is complete, then $(\mathcal{K}(X), D)$ is also complete. First we show that if $(A_{n})$ is a sequence of nonempty compact sets converging to a nonempty compact set $A$ in the Hausdorffmetric, then
$$A = {x \in X | there is a sequence, (x_{n}), with x_{n} \in A_{n} converging to x}.$$
Indeed, if $(x_{n})$ is a sequence with $x_{n} \in A_{n}$ converging to $x$ and $(A_{n})$ converges to $A$ then,
$$for every \epsilon  > 0, there is some x_{n} such that d(x_{n}, x) \le \epsilon /2 and \frac{there}{A.} is some a_{n} \in A such$$
that $d(a_{n}, x_{n}) \le \epsilon /2$ and thus, $d(a_{n}, x) \le \epsilon$ , which shows that $x \in$  Since $A$ is compact, it is closed, and $x \in A$. See Figure 37.48.
$$x$$
$$xn$$
$$x2$$
$$Ax1$$
$$A1$$
$$2$$
$$An$$
$$(i.)$$
$$A$$
$$< є$$
$$x$$
$$an$$
$$є/2$$
$$є/2$$
$$(ii.)$$
$$xn$$

![Figure 37.48](../../assets/ch37/fig_37_48.png)

**Figure 37.48:** Let $(A_{n})$ be the sequence of parallelograms converging to $A$, the large pale yellow parallelogram. Figure (ii.) expands the dashed region and shows why $d(a_{n}, x) < \epsilon$ . Conversely, since $(A_{n})$ converges to $A$, for every $x \in A$, for every $n \ge 1$, there is some $x_{n} \in A_{n}$ such that $d(x_{n}, x) \le 1/n$ and the sequence $(x_{n})$ converges to $x$. Now let $(A_{n})$ be a Cauchy sequence in $\mathcal{K}(X)$. It can be proven that $(A_{n})$ converges to the set
$$A = {x \in X | there is a sequence, (x_{n}), with x_{n} \in A_{n} converging to x},$$
and that $A$ is nonempty and compact. To prove that $A$ is compact, one proves that it is totally bounded and complete. Details are given in Edgar $[56]$.
