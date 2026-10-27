# Intersection of Affine Spaces


<!-- PAGE 849 -->
Also recall that every linear form $f^{*}$ is such that $f^{*} (x) = \lambda_{1} x_{1} + \cdots  + \lambda_{n} x_{n}$, for every $x = x_{1}u_{1} + \cdots  + x_{n}u_{n}$ and some $\lambda_{1} , \dots  , \lambda_{n}  \in \mathbb{R}$. Since an affine form $f$ : $E \to \mathbb{R}$ satisfies the
$$\longrightarrow$$
property $f(a_{0} +x) = f(a_{0})+ f (x)$, denoting $f(a_{0} +x)$ by $f(x_{1}, \dots  , x_{n})$, we see that we have
$$f(x_{1}, \dots  , x_{n}) = \lambda_{1} x_{1} + \cdots  + \lambda_{n} x_{n} + \mu ,$$
where $\mu  = f(a_{0}) \in \mathbb{R}$ and $\lambda_{1} , \dots  , \lambda_{n}  \in \mathbb{R}$. Thus, a hyperplane is the set of points whose coordinates $(x_{1}, \dots  , x_{n})$ satisfy the (affine) equation
$$\lambda_{1} x_{1} + \cdots  + \lambda_{n} x_{n} + \mu  = 0.$$

## 24.11 Intersection of Affine Spaces

In this section we take a closer look at the intersection of affine subspaces. This subsection can be omitted at first reading. First, we need a result of linear algebra. Given a vector space $E$ and any two subspaces $M$ and $N$, there are several interesting linear maps. We have the canonical injections $i: M \to M +N$ and $j$ : $N \to M +N$, the canonical injections $in_{1}$ : $M \to M \oplus N$ and $in_{2}$ : $N \to M \oplus N$, and thus, injections $f$ : $M \cap N \to M \oplus N$ and $g: M \cap N \to M \oplus N$, where $f$ is the composition of the inclusion map from $M \cap N$ to $M$ with $in_{1}$, and $g$ is the composition of the inclusion map from $M \cap N$ to $N$ with $in_{2}$. Then, we have the maps $f + g: M \cap N \to M \oplus N$, and $i$ - $j$ : $M \oplus N \to M + N$.

> **Proposition 24.15.** Given a vector space $E$ and any two subspaces $M$ and $N$, with the definitions above,
$$0 \longrightarrow M \cap N^{f+g}\longrightarrow M \oplus N^{i-j}\longrightarrow M + N \longrightarrow 0$$
is a short exact sequence, which means that $f + g$ is injective, $i$ - $j$ is surjective, and that Im $(f + g) =$ Ker $(i$ - $j)$. As a consequence, we have the Grassmann relation
$$\dim(M) + \dim(N) = \dim(M + N) + \dim (M \cap N).$$

*Proof.* It is obvious that $i$ - $j$ is surjective and that $f + g$ is injective. Assume that $(i$ - j)(u $+ v) = 0$, where $u \in M$, and $v \in N$. Then, i(u) $=$ j(v), and thus, by definition of $i$ and $j$, there is some $w \in M \cap N$, such that i(u) $=$ j(v) $= w \in M \cap N$. By definition of $f$ and $g, u =$ f(w) and $v =$ g(w), and thus Im $(f + g) =$ Ker $(i$ - $j)$, as desired. The second part of the proposition follows from standard results of linear algebra (see Artin $[7]$, Strang $[176]$, or Lang $[113])$. We now prove a simple proposition about the intersection of affine subspaces.

> **Proposition 24.16.** Given any affine space $E$, for any two nonempty affine subspaces $M$ and $N$, the following facts hold:

<!-- PAGE 850 -->
$$\longrightarrow \longrightarrow  \longrightarrow$$
$(1) M \cap N \neq  \emptyset$ iff ab $\in M + N$ for some $a \in M$ and some $b \in N$.
$$\longrightarrow \longrightarrow  \longrightarrow$$
$(2) M \cap N$ consists of a single point iff ab $\in M + N$ for some $a \in M$ and some $b \in N$,
$$\longrightarrow \longrightarrow$$
and $M \cap N = {0}$.
$$\longrightarrow  \longrightarrow  \longrightarrow \longrightarrow$$
$(3)$ If $S$ is the least affine subspace containing $M$ and $N$, then $S = M + N +$ Kab (the
$$\longrightarrow$$
vector space $E$ is defined over the field $K)$.

*Proof.* $(1)$ Pick any $a \in M$ and any $b \in N$, which is possible, since $M$ and $N$ are nonempty. $\longrightarrow \longrightarrow  \longrightarrow \longrightarrow$ Since $M = {ax$ | $x \in M}$ and $N = {by$ | $y \in N}$, if $M \cap N \neq  \emptyset$ , for any $c \in M \cap N$ we have $\longrightarrow  \longrightarrow \longrightarrow  \longrightarrow \longrightarrow  \longrightarrow \longrightarrow  \longrightarrow \longrightarrow  \longrightarrow$ ab $=$ ac - bc, with ac $\in M$ and bc $\in N$ , and thus, ab $\in M + N$ . Conversely, assume that $\longrightarrow \longrightarrow  \longrightarrow  \longrightarrow  \longrightarrow  \longrightarrow$ ab $\in M + N$ for some $a \in M$ and some $b \in N$. Then ab $=$ ax $+$ by, for some $x \in M$ and some $y \in N$. But we also have
$$\longrightarrow  \longrightarrow  \longrightarrow  \longrightarrow$$
$$ab =ax +xy +yb,$$
$$\longrightarrow  \longrightarrow \longrightarrow  \longrightarrow \longrightarrow$$
and thus we get $0 =$ xy $+$ yb - by, that is, xy $=$ 2by. Thus, $b$ is the middle of the segment
$$\longrightarrow \longrightarrow$$
$[x, y]$, and since yx $=$ 2yb, $x =$ 2b - $y$ is the barycenter of the weighted points $(b, 2)$ and $(y, -1)$. Thus $x$ also belongs to $N$, since $N$ being an affine subspace, it is closed under barycenters. Thus, $x \in M \cap N$, and $M \cap N \neq  \emptyset$ .
$(2)$ Note that in general, if $M \cap N \neq  \emptyset$ , then
$$---\longrightarrow  \longrightarrow \longrightarrow$$
$$M \cap N =M \cap N ,$$
because
$$---\longrightarrow \longrightarrow \longrightarrow \longrightarrow  \longrightarrow \longrightarrow$$
$$M \cap N = {ab | a, b \in M \cap N} = {ab | a, b \in M} \cap {ab | a, b \in N} =M \cap N .$$
$$---\longrightarrow$$
Since $M \cap N = c + M \cap N$ for any $c \in M \cap N$, we have
$$\longrightarrow \longrightarrow$$
$$M \cap N = c +M \cap Nfor any c \in M \cap N.$$
$$\longrightarrow \longrightarrow$$
From this it follows that if $M \cap N \neq  \emptyset$ , then $M \cap N$ consists of a single point iff $M \cap N = {0}$. This fact together with what we proved in $(1)$ proves $(2)$.
$(3)$ This is left as an easy exercise.
Remarks:
$$\longrightarrow \longrightarrow  \longrightarrow$$
$(1)$ The proof of Proposition 24.16 shows that if $M \cap$ N̸ $= \emptyset$ , then ab $\in M + N$ for all $a \in M$ and all $b \in N$.

<!-- PAGE 851 -->
$(2)$ Proposition 24.16 implies that for any two nonempty affine subspaces $M$ and $N$, if $\longrightarrow  \longrightarrow \longrightarrow  \longrightarrow  \longrightarrow \longrightarrow E = M \oplus N$ , then $M \cap N$ consists of a single point. Indeed, if $E = M \oplus N$ , then $\longrightarrow \longrightarrow  \longrightarrow \longrightarrow$ ab $\in E$ for all $a \in M$ and all $b \in N$, and since $M \cap N = {0}$, the result follows from part $(2)$ of the proposition. We can now state the following proposition.

> **Proposition 24.17.** Given an affine space $E$ and any two nonempty affine subspaces $M$ and $N$, if $S$ is the least affine subspace containing $M$ and $N$, then the following properties hold:
$(1)$ If $M \cap N = \emptyset$ , then
$$\longrightarrow  \longrightarrow$$
$$\dim(M) + \dim(N) < \dim(E) + \dim(M +N )$$
and
$$\longrightarrow \longrightarrow$$
$$\dim(S) = \dim(M) + \dim(N) + 1 -\dim(M \cap N ).$$
$(2)$ If $M \cap N \neq  \emptyset$ , then
$$\dim(S) = \dim(M) + \dim(N) -\dim(M \cap N).$$

*Proof.* The proof is not difficult, using Proposition 24.16 and Proposition 24.15, but we leave it as an exercise.

<!-- PAGE 852 -->
