# Statement of Zorn's Lemma


<!-- PAGE 2193 -->
Appendix $C$ Zorn’s Lemma; Some Applications

## C.1 Statement of Zorn’s Lemma

Zorn’s lemma is a particularly useful form of the axiom of choice, especially for algebraic applications. Readers who want to learn more about Zorn’s lemma and its applications to algebra should consult either Lang $[113]$, Appendix $2$, §2 (pp. 878-884) and Chapter III, §5 (pp. 139-140), or Artin $[7]$, Appendix §1 (pp. 588-589). For the logical ramifications of Zorn’s lemma and its equivalence with the axiom of choice, one should consult Schwartz $[156]$, (Vol. $1)$, Chapter I, §6, or a text on set theory such as Enderton $[57]$, Suppes $[179]$, or Kuratowski and Mostowski $[111]$. Given a set, $S$, a partial order, $\le$ , on $S$ is a binary relation on $S$ (i.e., $\le \subseteq S \times  S)$ which is
$(1)$ reflexive, i.e., $x \le x$, for all $x \in S$,
$(2)$ transitive, i.e, if $x \le y$ and $y \le z$, then $x \le z$, for all $x, y, z \in S$, and
$(3)$ antisymmetric, i.e, if $x \le y$ and $y \le x$, then $x = y$, for all $x, y \in S$. A pair $(S, \le$ ), where $\le$ is a partial order on $S$, is called a partially ordered set or poset. Given a poset, $(S, \le$ ), a subset, $C$, of $S$ is totally ordered or a chain if for every pair of elements $x, y \in C$, either $x \le y$ or $y \le x$. The empty set is trivially a chain. A subset, $P$, (empty or not) of $S$ is bounded if there is some $b \in S$ so that $x \le b$ for all $x \in P$. Observe that the empty subset of $S$ is bounded if and only if $S$ is nonempty. A maximal element of $P$ is an element, $m \in P$, so that $m \le x$ implies that $m = x$, for all $x \in P$. Zorn’s lemma can be stated as follows:

> **Lemma C.1.** Given a partially ordered set, $(S, \le$ ), if every chain is bounded, then $S$ has a maximal element.

*Proof.* See any of Schwartz $[156]$, Enderton $[57]$, Suppes $[179]$, or Kuratowski and Mostowski $[111]$.
$$2193$$
