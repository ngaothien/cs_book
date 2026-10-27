# Complete Metric Spaces and Compactness


<!-- PAGE 1407 -->
$$\varepsilon$$
$$> \varepsilon$$
$$a 0$$
$$\varepsilon > \varepsilon$$
$$\overline{\varepsilon}>$$
$$\overline{a}\overline{1}> \varepsilon$$
$$\overline{\varepsilon}$$
$$\overline{a}> \varepsilon$$
$$\overline{>}> \varepsilon$$
$$\overline{\varepsilon}\varepsilon$$
$$am$$
$$a\varepsilon > \varepsilon$$
$$(i.) n$$
$$+1$$
$$E$$
$$\varepsilon /3a$$
$$> 2q$$
$$ap\overline{a}_{\varepsilon/3}\overline{\varepsilon}$$
$$(ii.)$$

![Figure 37.44](../../assets/ch37/fig_37_44.png)

**Figure 37.44:** Let $E$ be the peach region of $\mathbb{R}^{2}$. If $E$ is not covered by a finite collection of orange balls with radius $\epsilon$ , the points of the sequence $(a_{n})$ are separated by a distance of at least $\epsilon$ . This contradicts the fact that a is the accumulation point of a, as evidenced by the enlargement of the plum disk in Figure (ii).

> **Theorem 37.47.** A metric space, $E$, is compact iff every sequence, $(x_{n})$, has an accumulation point.

*Proof.* We already observed that the proof of Proposition 37.43 shows that for any compact space (not necessarily metric), every sequence, $(x_{n})$, has an accumulation point. Conversely, let $E$ be a metric space, and assume that every sequence, $(x_{n})$, has an accumulation point. Given any open cover, $(U_{i})_{i\in I}$ for $E$, we must find a finite open subcover of $E$. By Lemma 37.44, there is some $\delta  > 0$ (a Lebesgue number for $(U_{i})_{i\in I})$ such that, for every open ball, $B_{0}(a, \epsilon$ ), of radius $\epsilon  \le \delta$ , there is some open subset, $U_{j}$, such that $B_{0}(a, \epsilon$ ) $\subseteq U_{j}$. By Lemma 37.46, for every $\delta  > 0$, there is a finite open cover, $B_{0}(a_{0}, \delta$ ) $\cup \cdots  \cup B_{0}(a_{n}, \delta$ ), of $E$ by open balls of radius $\delta$ . But from the previous statement, every open ball, $B_{0}(a_{i}, \delta$ ), is contained in some open set, $U_{ji}$, and thus, ${U_{j1}, \dots  , U_{jn}}$ is an open cover of $E$.

## 37.8 Complete Metric Spaces and Compactness

Another very useful characterization of compact metric spaces is obtained in terms of Cauchy sequences. Such a characterization is quite useful in fractal geometry (and elsewhere). First

<!-- PAGE 1408 -->
recall the definition of a Cauchy sequence and of a complete metric space.

> **Definition 37.38.** Given a metric space, $(E, d)$, a sequence, $(x_{n})_{n\in N}$, in $E$ is a Cauchy sequence if the following condition holds: for every $\epsilon  > 0$, there is some $p \ge 0$, such that, for all $m, n \ge p$, then $d(x_{m}, x_{n}) \le \epsilon$ . If every Cauchy sequence in $(E, d)$ converges we say that $(E, d)$ is a complete metric space. First let us show the following proposition:

> **Proposition 37.48.** Given a metric space, $E$, if a Cauchy sequence, $(x_{n})$, has some accumulation point, a, then a is the limit of the sequence, $(x_{n})$.

*Proof.* Since $(x_{n})$ is a Cauchy sequence, for every $\epsilon  > 0$, there is some $p \ge 0$, such that, for all $m, n \ge p$, then $d(x_{m}, x_{n}) \le \epsilon /2$. Since a is an accumulation point for $(x_{n})$, for infinitely many $n$, we have $d(x_{n}, a) \le \epsilon /2$, and thus, for at least some $n \ge p$, we have $d(x_{n}, a) \le \epsilon /2$. Then, for all $m \ge p$,
$$d(x_{m}, a) \le d(x_{m}, x_{n}) + d(x_{n}, a) \le \epsilon ,$$
which shows that a is the limit of the sequence $(x_{n})$. We can now prove the following theorem.

> **Theorem 37.49.** A metric space, $E$, is compact iff it is precompact and complete.

*Proof.* Let $E$ be compact. For every $\epsilon  > 0$, the family of all open balls of radius $\epsilon$  is an open cover for $E$ and since $E$ is compact, there is a finite subcover, $B_{0}(a_{0}, \epsilon$ ) $\cup \cdots  \cup B_{0}(a_{n}, \epsilon$ ), of $E$ by open balls of radius $\epsilon$ . Thus $E$ is precompact. Since $E$ is compact, by Theorem 37.47, every sequence, $(x_{n})$, has some accumulation point. Thus every Cauchy sequence, $(x_{n})$, has some accumulation point, a, and, by Proposition 37.48, a is the limit of $(x_{n})$. Thus, $E$ is complete. Now assume that $E$ is precompact and complete. We prove that every sequence, $(x_{n})$, has an accumulation point. By the other direction of Theorem 37.47, this shows that $E$ is compact. Given any sequence, $(x_{n})$, we construct a Cauchy subsequence, $(y_{n})$, of $(x_{n})$ as follows: Since $E$ is precompact, letting $\epsilon  = 1$, there exists a finite cover, $\mathcal{U}_{1}$, of $E$ by open balls of radius $1$. Thus some open ball, $B_{o}^{0}$, in the cover, $\mathcal{U}_{1}$, contains infinitely many elements from the sequence $(x_{n})$. Let $y_{0}$ be any element of $(x_{n})$ in $B_{o}^{0}$. By induction, assume that a sequence of open balls, $(B_{o}^{i})_{1\le i\le m}$, has been defined, such that every ball, $B_{o}^{i}$, has $radius_{i}^{1}$, contains infinitely many elements from the sequence $(x_{n})$ and contains some $y_{i}$ from $(x_{n}^{2})$ such that
$$d(y_{i}, y_{i+1}) \le \frac{1}{2^{i}} ,$$
for all $i, 0 \le i \le m$ - $1$. See Figure 37.45. Then letting $\epsilon  =_{2m+1}^{1}$, because $E$ is precompact, there is some finite $cover,\mathcal{U}_{m+1}$, of $E$ by open balls of radius $\epsilon$  and thus, of the open ball $B_{o}^{m}$ .

<!-- PAGE 1409 -->
Thus, some open ball, $B_{o}^{m+1}$, in the cover, $\mathcal{U}_{m+1}$, contains infinitely many elements from the sequence, $(x_{n})$, and we let $y_{m+1}$ be any element of $(x_{n})$ in $B_{o}^{m+1}$. Thus, we have defined by induction a sequence, $(y_{n})$, which is a subsequence of, $(x_{n})$, and such that
$$d(y_{i}, y_{i+1}) \le \frac{1}{2^{i}} ,$$
for all $i$. However, for all $m, n \ge 1$, we have
$$d(y_{m}, y_{n}) \le d(y_{m}, y_{m+1}) + \cdots  + d(y_{n-1}, y_{n}) \le \sum_{i=m}^{n}  \frac{1}{2^{i}} \le \frac{1}{2^{m-1}} ,$$
and thus, $(y_{n})$ is a Cauchy sequence Since $E$ is complete, the sequence, $(y_{n})$, has a limit, and since it is a subsequence of $(x_{n})$, the sequence, $(x_{n})$, has some accumulation point.
$$\overline{1}\overline{1}$$
$$\overline{1}$$
$$\overline{1} 1$$
$$y00$$
$$Bo$$
$$\overline{1}$$
$$\overline{1}\overline{1}$$
$$(x    )n$$
$$(i.)$$
$$\overline{1/2}\overline{1/2}$$
$$\overline{1/2}\overline{1}\overline{1/4}$$
$$y1\overline{1/2}$$
$$\overline{y} 0\overline{1/4} yy22$$
$$y1\overline{1/4}$$
$$\overline{1/2}\overline{1/2} y0$$
$$(ii.)(iii.)$$

![Figure 37.45](../../assets/ch37/fig_37_45.png)

**Figure 37.45:** The first three stages of the construction of the Cauchy sequence $(y_{n})$, where $E$ is the pink square region $of\mathbb{R}^{2}$. The original sequence $(x_{n})$ is illustrated with plum colored dots. Figure $(i.)$ covers $E$ with ball of radius $1$ and shows the selection of $B_{o}^{0}$ and $y_{0}$. Figure (ii.) covers $B_{o}^{0}$ with balls of radius $1/2$ and selects the yellow ball as $B_{o}^{1}$ with point $y_{1}$. Figure (iii.) covers $B_{o}^{1}$ with balls of radius $1/4$ and selects the pale peach ball as $B_{o}^{2}$ with point $y_{2}$. Another useful property of a complete metric space is that a subset is closed iff it is complete. This is shown in the following two propositions.

> **Proposition 37.50.** Let $(E, d)$ be a metric space, and let $A$ be a subset of $E$. If $A$ is complete (which means that every Cauchy sequence of elements in $A$ converges to some point of $A)$, then $A$ is closed in $E$.
