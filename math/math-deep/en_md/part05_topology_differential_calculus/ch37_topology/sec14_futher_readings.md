# Futher Readings


<!-- PAGE 1431 -->

## 37.13 Normed Affine Spaces

$$\longrightarrow$$
For geometric applications, we will need to consider affine spaces $(E, E$ ) where the associated
$$\longrightarrow$$
space of translations $E$ is a vector space equipped with a norm.
$$\longrightarrow  \longrightarrow$$

> **Definition 37.44.** Given an affine space $(E, E$ ), where the space of translations $E$ is a
$$\longrightarrow  \longrightarrow$$
vector space over $\mathbb{R}$ or $\mathbb{C}$, we say that $(E, E$ ) is a normed affine space if $E$ is a normed vector space with norm $\|\|$. Given a normed affine space, there is a natural metric on $E$ itself, defined such that
$$\longrightarrow$$
$$d(a, b) = \|ab\|.$$
Observe that this metric is invariant under translation, that is,
$$d(a + u, b + u) = d(a, b).$$
Also, for every fixed $a \in E$ and $\lambda  > 0$, if we consider the map $h: E \to E$, defined such that,
$$\longrightarrow$$
$$h(x) = a + \lambda ax,$$
then d(h(x), h(y)) $= \lambda$ d(x, $y)$.
$$\longrightarrow  \longrightarrow$$
Note that the map (a, $b) \mapsto$ ab from $E \times E$ to $E$ is continuous, and similarly for the map
$$\times  \longrightarrow  \longrightarrow$$
$a \mapsto a + u$ from $E E$ to $E$. In fact, the map $u \mapsto a + u$ is a homeomorphism from $E$ to $E_{a}$.
$$\mathbb{R}^{n}$$
Of course, is a normed affine space under the Euclidean metric, and it is also complete. If an affine space $E$ is a finite direct sum $(E_{1}, a_{1}) \oplus \cdots  \oplus (E_{m}, a_{m})$, and each $E_{i}$ is also a normed affine space with norm $\|\|_{i}$, we make $(E_{1}, a_{1}) \oplus \cdots  \oplus (E_{m}, a_{m})$ into a normed affine space, by giving it the norm
$$\|(x_{1}, \dots  , x_{n})\|= \max(\|x_{1}\|_{1}, \dots  , \|x_{n}\|_{n}).$$
Similarly, the finite product $E_{1} \times  \cdots  \times  E_{m}$ is made into a normed affine space, under the same norm. We are now ready to define the derivative (or differential) of a map between two normed affine spaces. This will lead to tangent spaces to curves and surfaces (in normed affine spaces).

## 37.14 Futher Readings

A thorough treatment of general topology can be found in Munkres $[135, 134]$, Dixmier $[52]$, Lang $[115, 116]$, Schwartz $[156, 155]$, Bredon $[30]$, and the classic, Seifert and Threlfall $[161]$.

<!-- PAGE 1432 -->
