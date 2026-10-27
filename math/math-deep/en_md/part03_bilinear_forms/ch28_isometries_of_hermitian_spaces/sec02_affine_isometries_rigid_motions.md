# Affine Isometries (Rigid Motions)


<!-- PAGE 1006 -->
Remark: For numerical stability, it is preferable to use $w_{k+1} = r_{k+1,k+1} e_{k+1} + e^{-i\theta k+1}u_{k+1}''$ instead of $w_{k+1} = r_{k+1,k+1} e_{k+1}$ - $e^{-i\theta k+1}u_{k+1}''$. The effect of that choice is that the diagonal entries in $R$ will be of the form $-e^{i\theta j}r_{j, j} = e^{i(\theta j+\pi)}r_{j, j}$. Of course, we can make these entries nonegative by applying
$$h_{n+1} = \rho_{en, \pi-\theta n}  \circ \cdots  \circ \rho_{e1,\pi-\theta1}$$
after $h_{n}$. As in the Euclidean case, Proposition 28.7 immediately implies the QR-decomposition for arbitrary complex $n\times n$-matrices, where $Q$ is now unitary (see Kincaid and Cheney $[105]$, Golub and Van Loan $[83]$, Trefethen and Bau $[182]$, or Ciarlet $[41])$.

> **Proposition 28.8.** For every complex $n \times n$-matrix $A$, there is a sequence $H_{1}, \dots  , H_{n-1}$ of matrices, where each $H_{i}$ is either a Householder matrix or the identity, and an upper triangular matrix $R$, such that
$$R = H_{n-1} \cdots  H_{2}H_{1}A.$$
As a corollary, there is a pair of matrices $Q, R$, where $Q$ is unitary and $R$ is upper triangular, such that $A = QR$ (a QR-decomposition of $A)$. Furthermore, $R$ can be chosen so that its diagonal entries are nonnegative. This can be achieved by a diagonal matrix $D$ with entries such that $|d_{ii}| = 1$ for $i = 1, \dots  , n$, and we have $A = QR$ with
$$e e$$
$$Q = H_{1} \cdots  H_{n-1}D,R = D^{*}R,$$
$$ee$$
where $R$ is upper triangular and has nonnegative diagonal entries $e$

*Proof.* It is essentially identical to the proof of Proposition 13.4, and we leave the details as an exercise. For the last statement, observe that $h_{n} \circ \cdots  \circ h_{1}$ is also an isometry. As in the Euclidean case, the QR-decomposition has applications to least squares problems. It is also possible to convert any complex matrix to bidiagonal form.

## 28.2 Affine Isometries (Rigid Motions)

In this section, we study very briefly the affine isometries of a Hermitian space. Most results holding for Euclidean affine spaces generalize without any problems to Hermitian spaces. The characterization of the set of fixed points of an affine map is unchanged. Similarly, every affine isometry $f$ (of a Hermitian space) can be written uniquely as
$$f = t \circ g,witht \circ g = g \circ t,$$
where $g$ is an isometry having a fixed point, and $t$ is a translation by a vector $\tau$  such that $\longrightarrow f (\tau$ ) $= \tau$ , and with some additional nice properties (see Proposition 28.13). A generalization

<!-- PAGE 1007 -->
of the Cartan–Dieudonn´e theorem can easily be shown: every affine isometry in $Is(n,\mathbb{C})$ can be written as the composition of at most 2n - $1$ isometries if it has a fixed point, or else as the composition of at most $2n+1$ isometries, where all these isometries are affine hyperplane reflections except for possibly one affine Hermitian reflection. We also prove that every rigid motion in $SE(n,\mathbb{C})$ is the composition of at most 2n - $2$ flips (for $n \ge 3)$.

> **Definition 28.2.** Given any two nontrivial Hermitian affine spaces $E$ and $F$ of the same finite dimension $n$, a function $f$ : $E \to F$ is an affine isometry (or rigid map) iff it is an affine map and
$$----\longrightarrow \longrightarrow$$
$$f(a)f(b) =ab ,$$
for all a, $b \in E$. When $E = F$, an affine isometry $f$ : $E \to E$ is also called a rigid motion. Thus, an affine isometry is an affine map that preserves the distance. This is a rather strong requirement, but unlike the Euclidean case, not strong enough to force $f$ to be an affine map. The following simple Proposition is left as an exercise.

> **Proposition 28.9.** Given any two nontrivial Hermitian affine spaces $E$ and $F$ of the same finite dimension $n$, an affine map $f$ : $E \to F$ is an affine isometry iff its associated linear $\longrightarrow  \longrightarrow \longrightarrow$ map $f$ : $E \to F$ is an isometry. An affine isometry is a bijection.
$$\longrightarrow$$
As in the Euclidean case, given an affine isometry $f$ : $E \to E$, if $f$ is a rotation, we call
$$\longrightarrow$$
$f$ a proper (or direct) affine isometry, and if $f$ is a an improper linear isometry, we call $f$ a an improper (or skew) affine isometry. It is easily shown that the set of affine isometries
$$\longrightarrow$$
$f$ : $E \to E$ forms a group, and those for which $f$ is a rotation is a subgroup. The group of affine isometries, or rigid motions, is a subgroup of the affine group $GA(E,\mathbb{C})$ denoted as $Is(E,\mathbb{C})$ (or $Is(n,\mathbb{C})$ when $E = \mathbb{C}^{n})$. The subgroup of $Is(E,\mathbb{C})$ consisting of the direct rigid motions is also a subgroup of $SA(E,\mathbb{C})$, and it is denoted as $SE(E,\mathbb{C})$ (or $SE(n,\mathbb{C})$,
$$\longrightarrow$$
when $E = \mathbb{C}^{n})$. The translations are the affine isometries $f$ for which $f =$ id, the identity
$$\longrightarrow$$
map on $E$ . The following Proposition is the counterpart of Proposition 14.14 for isometries between Hermitian vector spaces.

> **Proposition 28.10.** Given any two nontrivial Hermitian affine spaces $E$ and $F$ of the same finite dimension $n$, for every function $f$ : $E \to F$, the following properties are equivalent:
$$----\longrightarrow \longrightarrow$$
$(1) f$ is an affine map and f(a)f(b)  $=$ ab , for all a, $b \in E$.
$$----\longrightarrow \longrightarrow$$
$(2)$ f(a)f(b)  $=$ ab , and there is some $\Omega \in E$ such that
$$---------\longrightarrow$$
$$\longrightarrow  \longrightarrow$$
$$f(\Omega + iab) = f(\Omega ) + i(f(\Omega )f(\Omega +ab)),$$
for all a, $b \in E$.

<!-- PAGE 1008 -->

*Proof.* Obviously, $(1)$ implies $(2)$. The proof that that $(2)$ implies $(1)$ is similar to the proof of Proposition 27.7, but uses Proposition 14.14 instead of Proposition 12.12. The details are left as an exercise. Inspection of the proof shows immediately that Proposition 27.8 holds for Hermitian spaces. For the sake of completeness, we restate the Proposition in the complex case.

> **Proposition 28.11.** Let $E$ be any complex affine space of finite dimension For every affine map $f$ : $E \to E$, let Fix(f) $= {a \in E$ | f(a) $= a}$ be the set of fixed points of $f$. The following properties hold:
$(1)$ If $f$ has some fixed point a, so that Fix(f) $\neq  \emptyset$ , then Fix(f) is an affine subspace of $E$ such that
$$\longrightarrow \longrightarrow$$
$$Fix(f) = a + E(1,f ) = a + \mathrm{Ker} (f -id),$$
$$\longrightarrow  \longrightarrow$$
where E(1, $f$ ) is the eigenspace of the linear map $f$ for the eigenvalue $1$.
$$\longrightarrow \longrightarrow$$
$(2)$ The affine map $f$ has a unique fixed point iff E(1, $f$ ) $=$ Ker ( $f$ - id) $= {0}$. Affine orthogonal symmetries are defined just as in the Euclidean case, and Proposition 27.9 also applies to complex affine spaces.

> **Proposition 28.12.** Given any affine complex space $E$, if $f$ : $E \to E$ and $g: E \to E$ are affine orthogonal symmetries about parallel affine subspaces $F_{1}$ and $F_{2}$, then $g \circ f$ is a
$$\longrightarrow  \longrightarrow$$
translation defined by the vector 2ab, where ab is any vector perpendicular to the common
$$\longrightarrow


$\longrightarrow$$$ direction $F$ of $F_{1}$ and $F_{2}$ such that ab  is the distance between $F_{1}$ and $F_{2}$, with $a \in F_{1}$ and $b \in F_{2}$. Conversely, every translation by a vector $\tau$  is obtained as the composition of two affine orthogonal symmetries about parallel affine subspaces $F_{1}$ and $F_{2}$ whose common
$$\longrightarrow$$
direction is orthogonal to $\tau  =$ ab, for some $a \in F_{1}$ and some $b \in F_{2}$ such that the distance
$$\longrightarrow$$
betwen $F_{1}$ and $F_{2}$ is ab  $/2$. It is easy to check that the proof of Proposition 27.10 also holds in the Hermitian case.

> **Proposition 28.13.** Let $E$ be a Hermitian affine space of finite dimension $n$. For every affine isometry $f$ : $E \to E$, there is a unique affine isometry $g: E \to E$ and a unique
$$\longrightarrow \longrightarrow$$
translation $t = t_{\tau}$, with $f (\tau$ ) $= \tau$  (i.e., $\tau  \in$ Ker ( $f$ - id)), such that the set Fix(g) $= {a \in E$, | g(a) $= a}$ of fixed points of $g$ is a nonempty affine subspace of $E$ of direction
$$\longrightarrow \longrightarrow  \longrightarrow$$
$$G = \mathrm{Ker} (f -id) = E(1,f ),$$
and such that
$$f = t \circ gandt \circ g = g \circ t.$$
Furthermore, we have the following additional properties:

<!-- PAGE 1009 -->
(a) $f = g$ and $\tau  = 0$ iff $f$ has some fixed point, i.e., iff Fix(f) $\neq  \emptyset$ .
$$\longrightarrow$$
$(b)$ If $f$ has no fixed points, i.e., Fix(f) $= \emptyset$ , then dim(Ker ( $f$ - id)) $\ge 1$. The remarks made in the Euclidean case also apply to the Hermitian case. In particular, the fact that $E$ has finite dimension is only used to prove $(b)$. A version of the Cartan–Dieudonn´e also holds for affine isometries, but it may not be possible to get rid of Hermitian reflections entirely.

> **Theorem 28.14.** Let $E$ be an affine Hermitian space of dimension $n \ge 1$. Every affine isometry in $Is(n,\mathbb{C})$ can be written as the composition of at most 2n - $1$ affine isometries if it has a fixed point, or else as the composition of at most 2n $+ 1$ affine isometries, where all these isometries are affine hyperplane reflections except for possibly one affine Hermitian reflection. When $n \ge 2$, the identity is the composition of any reflection with itself.

*Proof.* The proof is very similar to the proof of Theorem 27.11, except that it uses Theorem 28.5 instead of Theorem 27.1. The details are left as an exercise. When $n \ge 3$, as in the Euclidean case, we can characterize the affine isometries in $SE(n,\mathbb{C})$ in terms of flips, and we can even bound the number of flips by 2n - $2$.

> **Theorem 28.15.** Let $E$ be a Hermitian affine space of dimension $n \ge 3$. Every rigid motion $f \in SE(E,\mathbb{C})$ is the composition of an even number of affine flips $f = f_{2k} \circ \cdots  \circ f_{1}$, where $k \le n$ - $1$.

*Proof.* It is very similar to the proof of theorem 27.12, but it uses Proposition 28.6 instead of Proposition 27.5. The details are left as an exercise. A more detailed study of the rigid motions of Hermitian spaces of dimension $2$ and $3$ would seem worthwhile, but we are not aware of any reference on this subject.

<!-- PAGE 1010 -->
