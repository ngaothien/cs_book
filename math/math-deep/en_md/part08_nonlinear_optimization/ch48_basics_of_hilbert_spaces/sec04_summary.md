# Summary


<!-- PAGE 1700 -->
or equivalently
$$\|b -c\|= \inf \|b -v\|> 0$$
$$v\in C$$
$$\langle v -c, c -b\rangle \ge 0for all v \in C.$$
As a consequence, since $b\notin C$ and $c \in C$, we have $c$ - $b \neq  0$, so
$$\langle v, c -b\rangle \ge \langle c, c -b\rangle > \langle b, c -b\rangle$$
because $\langle c, c$ - $b\rangle -\langle b, c$ - $b\rangle = \langle c$ - $b, c$ - $b\rangle > 0$, and if we pick $u = c$ - $b$ and any $\alpha$  such that
$$\langle c, c -b\rangle > \alpha  > \langle b, c -b\rangle ,$$
the claim is satisfied. We now prove the Farkas–Minkowski lemma. Assume that $b \in / C$. Since $C$ is nonempty, convex, and closed, by the claim there is some $u \in V$ and some $\alpha  \in \mathbb{R}$ such that
$$\langle v, u\rangle > \alpha for every v \in C$$
$$\langle b, u\rangle < \alpha .$$
But $C$ is a polyhedral cone containing $0$, so we must have $\alpha  < 0$. Then for every $v \in C$, since $C$ a polyhedral cone if $v \in C$ then $\lambda v \in C$ for all $\lambda  > 0$, so by the above
$$\langle v, u\rangle > \frac{\alpha}{\lambda} for every \lambda  > 0,$$
which implies that
$$\langle v, u\rangle \ge 0.$$
Since $a_{i} \in C$ for $i = 1, \dots  , m$, we proved that
$$\langle a_{i}, u\rangle \ge 0i = 1, \dots  , mand\langle b, u\rangle < \alpha  < 0,$$
which proves Farkas lemma.
Remark: Observe that the claim established during the proof of Theorem 48.12 shows that the affine hyperplane $H_{u,\alpha}$ of equation $\langle v, u\rangle = \alpha$  for all $v \in V$ separates strictly $C$ and ${b}$.

## 48.4 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Hilbert space. $\bullet$  Projection lemma.
