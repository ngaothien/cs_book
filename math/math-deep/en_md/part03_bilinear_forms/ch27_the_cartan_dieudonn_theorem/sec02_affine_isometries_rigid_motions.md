# Affine Isometries (Rigid Motions)


<!-- PAGE 983 -->
The proof of Lemma 27.4 yields two flips $f_{2k-1}$ and $f_{2k}$ such that
$$f_{2k}(e_{n-2}) = -e_{n-2}ands_{2k} \circ s_{2k-1} = f_{2k} \circ f_{2k-1},$$
since the $(n$ - 2)th diagonal entry in both matrices is $-1$, which means that $e_{n-2} \in F_{2k}^{\perp}$ , where $F_{2k}$ is the subspace of dimension $n$ - $2$ determining $f_{2k}$. Since $u = \|u\|e_{n-2}$, we also have $u \in F_{2k}^{\perp}$ .
Remarks:
$(1)$ It is easy to prove that if $f$ is a rotation in SO(3) and if $D$ is its axis and $\theta$  is its angle of rotation, then $f$ is the composition of two flips about lines $D_{1}$ and $D_{2}$ orthogonal to $D$ and making an angle $\theta /2$.
$(2)$ It is natural to ask what is the minimal number of flips needed to obtain a rotation $f$ (when $n \ge 3)$. As for arbitrary isometries, we will prove later that every rotation is the composition of $k$ flips, where
$$k = n -\dim(\mathrm{Ker} (f -id)),$$
and that this number is minimal (where $n =$ dim(E)). We now turn to affine isometries.

## 27.2 Affine Isometries (Rigid Motions)

In the remaining sections we study affine isometries. First, we characterize the set of fixed points of an affine map. Using this characterization, we prove that every affine isometry $f$ can be written uniquely as
$$f = t \circ g,witht \circ g = g \circ t,$$
where $g$ is an isometry having a fixed point, and $t$ is a translation by a vector $\tau$  such that $\longrightarrow f (\tau$ ) $= \tau$ , and with some additional nice properties (see Theorem 27.10). This is a gener-
$$\mathbb{R}^{3}$$
alization of a classical result of Chasles about (proper) rigid motions in (screw motions). We prove a generalization of the Cartan–Dieudonn´e theorem for the affine isometries: Every isometry in Is(n) can be written as the composition of at most $n$ affine reflections if it has a fixed point, or else as the composition of at most $n + 2$ affine reflections. We also prove that every rigid motion in SE(n) is the composition of at most $n$ affine flips (for $n \ge 3)$. This is somewhat surprising, in view of the previous theorem.

> **Definition 27.1.** Given any two nontrivial Euclidean affine spaces $E$ and $F$ of the same finite dimension $n$, a function $f$ : $E \to F$ is an affine isometry (or rigid map) if it is an affine map and
$$----\longrightarrow \longrightarrow$$
$$\|f(a)f(b)\|= \|ab\|,$$
for all a, $b \in E$. When $E = F$, an affine isometry $f$ : $E \to E$ is also called a rigid motion.

<!-- PAGE 984 -->
Thus, an affine isometry is an affine map that preserves the distance. This is a rather strong requirement. In fact, we will show that for any function $f$ : $E \to F$, the assumption that
$$----\longrightarrow \longrightarrow$$
$$\|f(a)f(b)\|= \|ab\|,$$
for all a, $b \in E$, forces $f$ to be an affine map.
Remark: Sometimes, an affine isometry is defined as a bijective affine isometry. When $E$ and $F$ are of finite dimension, the definitions are equivalent. The following simple lemma is left as an exercise.

> **Proposition 27.6.** Given any two nontrivial Euclidean affine spaces $E$ and $F$ of the same finite dimension $n$, an affine map $f$ : $E \to F$ is an affine isometry iff its associated linear $\longrightarrow  \longrightarrow \longrightarrow$ map $f$ : $E \to F$ is an isometry. An affine isometry is a bijection.
$$\longrightarrow$$
Let us now consider affine isometries $f$ : $E \to E$. If $f$ is a rotation, we call $f$ a proper (or
$$\longrightarrow$$
direct) affine isometry, and if $f$ is an improper linear isometry, we call $f$ an improper (or skew) affine isometry. It is easily shown that the set of affine isometries $f$ : $E \to E$ forms a
$$\longrightarrow$$
group, and those for which $f$ is a rotation is a subgroup. The group of affine isometries, or rigid motions, is a subgroup of the affine group GA(E), denoted by Is(E) (or Is(n) when $E = \mathbb{E}^{n})$. In Snapper and Troyer $[168]$ the group of rigid motions is denoted by Mo(E). Since we denote the group of affine bijections as GA(E), perhaps we should denote the group of affine isometries by IA(E) (or EA(E)!). The subgroup of Is(E) consisting of the direct rigid motions is also a subgroup of SA(E), and it is denoted by SE(E) (or SE(n),
$$\longrightarrow$$
when $E = \mathbb{E}^{n})$. The translations are the affine isometries $f$ for which $f =$ id, the identity
$$\longrightarrow$$
map on $E$ . The following lemma is the counterpart of Lemma 12.12 for isometries between Euclidean vector spaces.

> **Proposition 27.7.** Given any two nontrivial Euclidean affine spaces $E$ and $F$ of the same finite dimension $n$, for every function $f$ : $E \to F$, the following properties are equivalent:
$$----\longrightarrow \longrightarrow$$
$(1) f$ is an affine map and $\|f(a)f(b)\| = \|ab\|$, for all a, $b \in E$.
$$----\longrightarrow \longrightarrow$$
$(2) \|f(a)f(b)\| = \|ab\|$, for all a, $b \in E$.

*Proof.* Obviously, $(1)$ implies $(2)$. In order to prove that $(2)$ implies $(1)$, we proceed as
$$\longrightarrow \longrightarrow$$
follows. First, we pick some arbitrary point $\Omega \in E$. We define the map $g: E \to F$ such that
$$--------\longrightarrow$$
$$g(u) =f(\Omega )f(\Omega + u)$$
for all $u \in E$. Since
$$--------\longrightarrow$$
$$f(\Omega ) + g(u) = f(\Omega ) +f(\Omega )f(\Omega + u) = f(\Omega + u)$$
