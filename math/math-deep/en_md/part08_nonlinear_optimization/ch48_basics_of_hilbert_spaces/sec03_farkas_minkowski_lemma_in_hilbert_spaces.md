# Farkas–Minkowski Lemma in Hilbert Spaces


<!-- PAGE 1699 -->

## 48.3 Farkas–Minkowski Lemma in Hilbert Spaces

In this section $(V, \langle$ -, $-\rangle$ ) is assumed to be a real Hilbert space. The projection lemma can be used to show an interesting version of the Farkas–Minkowski lemma in a Hilbert space. Given a finite sequence of vectors $(a_{1}, \dots  , a_{m})$ with $a_{i} \in V$ , let $C$ be the polyhedral cone
$$$$
$$C = cone(a_{1}, \dots  , a_{m}) = \sum_{i=1}^{m}  \lambda_{i} a_{i} | \lambda_{i}  \ge 0, i = 1, \dots  , m.$$
For any vector $b \in V$ , the Farkas–Minkowski lemma gives a criterion for checking whether $b \in C$. In Proposition 44.2 we proved that every polyhedral cone $cone(a_{1}, \dots  , a_{m})$ with $a_{i} \in \mathbb{R}^{n}$ is closed. Close examination of the proof shows that it goes through if $a_{i} \in V$ where $V$ is any vector space possibly of infinite dimension, because the important fact is that the number $m$ of these vectors is finite, not their dimension.

> **Theorem 48.12.** (Farkas–Minkowski Lemma in Hilbert Spaces) Let $(V, \langle$ -, $-\rangle$ ) be a real Hilbert space. For any finite sequence of vectors $(a_{1}, \dots  , a_{m})$ with $a_{i} \in V$ , if $C$ is the polyhedral cone $C = cone(a_{1}, \dots  , a_{m})$, for any vector $b \in V$ , we have $b \in / C$ iff there is a vector $u \in V$ such that
$$\langle a_{i}, u\rangle \ge 0i = 1, \dots  , m,and\langle b, u\rangle < 0.$$
Equivalently, $b \in C$ iff for all $u \in V$ ,
$$if \langle a_{i}, u\rangle \ge 0i = 1, \dots  , m,then\langle b, u\rangle \ge 0.$$

*Proof.* We follow Ciarlet $[41]$ (Chapter $9$, Theorem 9.1.1). We already established in Proposition 44.2 that the polyhedral cone $C = cone(a_{1}, \dots  , a_{m})$ is closed. Next we claim the following: Claim: If $C$ is a nonempty, closed, convex subset of a Hilbert space $V$ , and $b \in V$ is any vector such that $b \in / C$, then there exist some $u \in V$ and infinitely many scalars $\alpha  \in \mathbb{R}$ such that
$$\langle v, u\rangle > \alpha for every v \in C$$
$$\langle b, u\rangle < \alpha .$$
We use the projection lemma (Proposition 48.5) which says that since $b \in / C$ there is some unique $c = p_{C}(b) \in C$ such that
$$\|b -c\|= \inf \|b -v\|> 0$$
$$v\in C$$
$$\langle b -c, v -c\rangle \le 0for all v \in C,$$
