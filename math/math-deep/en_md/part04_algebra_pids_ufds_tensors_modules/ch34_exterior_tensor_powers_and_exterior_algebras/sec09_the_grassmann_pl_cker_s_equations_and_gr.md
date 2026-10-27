# The Grassmann-Plücker's Equations and Grassmannians


<!-- PAGE 1264 -->

## 34.9 The Grassmann-Pl¨ucker’s Equations and

$$⊛$$
$$Grassmannian Manifolds$$
We follow an argument adapted from Bourbaki $[25]$ (Chapter III, §11, Section $13)$. Let $E$ be a vector space of dimensions $n$, let $(e_{1}, \dots  , e_{n})$ be a basis of $E$, and let $(e_{1}^{*}, \dots  , e_{n}^{*})$
$$p$$
$$be its dual basis.Our objective is to determine whether a nonzero vector⌟ z \in \bigwedge  E is$$
decomposable. By Proposition 34.27, the vector $z$ is decomposable $iff(u^{*} z) \wedge z = 0$ for all
$$p-1 p-1$$
$$u^{*}\in \bigwedge  E^{*}. We can let u^{*}range over a basis of \bigwedge  E^{*}, and then the conditions are$$
$$(e_{H}^{*} ⌟z) \wedge z = 0$$
$$⌟p+1 E$$
$$for all H \subseteq {1, \dots  , n}, with |H| = p -1. Since (e_{H}^{*} z) \wedge z \in \bigwedge  , this is equivalent to$$
$$\langle e_{J}^{*}, (e_{H}^{*} ⌟z) \wedge z\rangle = 0$$
for all $H, J \subseteq {1, \dots  , n}$, with |H| $= p$ - $1$ and |J| $= p + 1$. Then, for all I, I' $\subseteq {1, \dots  , n}$ with |I| $=$ |I'| $= p$, Formulae $(2)$ and $(4)$ of Proposition 34.18 show that
$$\langle e_{J}^{*}, (e_{H}^{*} ⌟e_{I}) \wedge e_{I'}\rangle = 0,$$
unless there is some $i \in {1, \dots  , n}$ such that
$$I -H = {i},J -I'= {i}.$$
In this case, $I = H \cup {i}$ and I' $= J -{i}$, and using Formulae $(2)$ and $(4)$ of Proposition 34.18, we have $\langle e_{J}^{*}, (e_{H}^{*}$ ⌟ $e_{H\cup {i}}) \wedge e_{J-{i}}\rangle = \langle e_{J}^{*}, \rho_{{i},H} e_{i} \wedge e_{J-{i}}\rangle = \langle e_{J}^{*}, \rho_{{i},H} \rho_{{i},J-{i}} e_{J}\rangle = \rho_{{i},H} \rho_{{i},J-{i}}$ . If we let
$$\epsilon_{i,J,H}  = \rho_{{i},H} \rho_{{i},J-{i}} ,$$
we have $\epsilon_{i,J,H}  = +1$ if the parity of the number of $j \in J$ such that $j < i$ is the same as the parity of the number of $h \in H$ such that $h < i$, and $\epsilon_{i,J,H}  = -1$ otherwise. Finally we obtain the following criterion in terms of quadratic equations (Pl¨ucker’s equations) for the decomposability of an alternating tensor.
$$p E$$
$$Proposition 34.29. (Grassmann-Pl¨ucker’s Equations) For z = \sum_{I}  \lambda_{I} e_{I} \in \bigwedge  , the con-$$
ditions for $z \neq  0$ to be decomposable are
$$\sum_{i\in J-H}  \epsilon_{i,J,H} \lambda_{H\cup {i}} \lambda_{J-{i}}  = 0,$$
with $\epsilon_{i,J,H}  = \rho_{{i},H} \rho_{{i},J-{i}}$ , for all $H, J \subseteq {1, \dots  , n}$ such that |H| $= p -1$, |J| $= p + 1$, and all $i \in J$ - $H$.

<!-- PAGE 1265 -->
Using the above criterion, it is a good exercise to reprove that if dim(E) $= n$, then every
$$tensor in \bigwedge  n-1(E) is decomposable. We already proved this fact as a corollary of Proposition$$
34.23.
$$p E$$
$$Given any z = \sum_{I}  \lambda_{I} e_{I} \in \bigwedge  where \dim(E) = n, the family of scalars (\lambda_{I} ) (with$$
$I = {i_{1} < \cdots  < i_{p}} \subseteq {1, \dots  , n}$ listed in increasing order) is called the Pl¨ucker coordinates of z.The Grassmann-Pl¨ucker’s equations give necessary and sufficient conditions for any nonzero $z$ to be decomposable. For example, when dim(E) $= n = 4$ and $p = 2$, these equations reduce to the single equation
$$\lambda_{12} \lambda_{34}  -\lambda_{13} \lambda_{24}  + \lambda_{14} \lambda_{23}  = 0.$$
However, it should be noted that the equations given by Proposition 34.29 are not independent in general. We are now in the position to prove that the Grassmannian G(p, $n)$ can be embedded in
$$\mathbb{RP}(_{p}^{n})^{-1}$$
the projective space , For any $n \ge 1$ and any $k$ with $1 \le p \le n$, recall that the Grassmannian G(p, $n)$ is the
$$\mathbb{R}^{n}$$
set of all linear $p$-dimensional subspaces of (also called p-planes). Any $p$-dimensional
$$\mathbb{R}^{n}  \mathbb{R}^{n}$$
subspace $U$ of is spanned by $p$ linearly independent vectors $u_{1}, \dots  , u_{p}$ in ; write $U = span(u_{1}, \dots  , u_{k})$. By Proposition 34.8, $(u_{1}, \dots  , u_{p})$ are linearly independent iff $u_{1}\wedge \cdots \wedge u_{p} \neq 0$. If $(v_{1}, \dots  , v_{p})$ are any other linearly independent vectors spanning $U$, then we have
$$v_{j} = \sum_{i=1}^{p}  a_{ij}u_{i},1 \le j \le p,$$
for some $a_{ij} \in \mathbb{R}$, and by Proposition 34.2
$$v_{1} \wedge \cdots  \wedge v_{p} = \det(A) u_{1} \wedge \cdots  \wedge u_{p},$$
$$\mathbb{RP}(_{p}^{n})^{-1}$$
where $A = (a_{ij})$. As a consequence, we can define a map $i_{G}$ : G(p, $n) \to$ such that for any k-plane $U$, for any basis $(u_{1}, \dots  , u_{p})$ of $U$,
$$i_{G}(U) = [u_{1} \wedge \cdots  \wedge u_{p}],$$
$$\mathbb{RP}(_{p}^{n})^{-1} \mathbb{R}(_{p}^{n})$$
the point of given by the one-dimensional subspace of spanned by $u_{1} \wedge \cdots \wedge u_{p}$.
$$\mathbb{RP}(_{p}^{n})^{-1}$$

> **Proposition 34.30.** The map $i_{G}$ : G(p, $n) \to$ is injective.

*Proof.* Let $U$ and $V$ be any two p-planes and assume that $i_{G}(U) = i_{G}(V$ ). This means that there is a basis $(u_{1}, \dots  , u_{p})$ of $U$ and a basis $(v_{1}, \dots  , v_{p})$ of $V$ such that
$$v_{1} \wedge \cdots  \wedge v_{p} = c u_{1} \wedge \cdots  \wedge u_{p}$$

<!-- PAGE 1266 -->
$$\mathbb{R}   \mathbb{R}^{n}$$
for some nonzero $c \in$ . The above implies that the smallest subspaces $W$ and W' of
$$p p$$
$$such that u_{1} \wedge \cdots  \wedge u_{p} \in \bigwedge  W and v_{1} \wedge \cdots  \wedge v_{p} \in \bigwedge_{1}  W' are identical, so W = W' . By$$
Corollary 34.26, this smallest subspace $W$ has both $(u , \dots  , u_{p})$ and $(v_{1}, \dots  , v_{p})$ as bases, so the $v_{j}$ are linear combinations of the $u_{i}$ (and vice-versa), and $U = V$ .
$$p\mathbb{R}^{n}$$
$$Since any nonzero z \in \bigwedge  can be uniquely written as$$
$$z = \sum_{I}  \lambda_{I} e_{I}$$
$$\mathbb{RP}(_{p}^{n})^{-1}$$
in terms of its Pl¨ucker coordinates $(\lambda_{I}$ ), every point of is defined by the Pl¨ucker
$$\mathbb{RP}(_{p}^{n})^{-1}$$
coordinates $(\lambda_{I}$ ) viewed as homogeneous coordinates. The points of corresponding to one-dimensional spaces associated with decomposable alternating p-tensors are the points whose coordinates satisfy the Grassmann-Pl¨ucker’s equations of Proposition 34.29.
$$\mathbb{RP}(_{p}^{n})^{-1}$$
Therefore, the map $i_{G}$ embeds the Grassmannian G(p, $n)$ as an algebraic variety in defined by equations of degree $2$. We can replace the field $\mathbb{R}$ by $\mathbb{C}$ in the above reasoning and we obtain an embedding of
$$\mathbb{CP}(_{p}^{n})^{-1}$$
the complex Grassmannian $G_{C}(p, n)$ as an algebraic variety in defined by equations of degree $2$. In particular, if $n = 4$ and $p = 2$, the equation
$$\lambda_{12} \lambda_{34}  -\lambda_{13} \lambda_{24}  + \lambda_{14} \lambda_{23}  = 0$$
$$\mathbb{CP}^{5}$$
is the homogeneous equation of a quadric in known as the Klein quadric. The points on this quadric are in one-to-one correspondence with the lines in $\mathbb{CP}^{3}$. There is also a simple algebraic criterion to decide whether the smallest subspaces $U$ and $V$ associated with two nonzero decomposable vectors $u_{1} \wedge \cdots  \wedge u_{p}$ and $v_{1} \wedge \cdots  \wedge v_{q}$ have a nontrivial intersection.

> **Proposition 34.31.** Let $E$ be any $n$-dimensional vector space over a field $K$, and let $U$ and $V$ be the smallest subspaces of $E$ associated with two nonzero decomposable vectors
$$p q$$
$$u = u_{1} \wedge \cdots  \wedge u_{p} \in \bigwedge  U and v = v_{1} \wedge \cdots  \wedge v_{q} \in \bigwedge  V . The following properties hold:$$
$(1)$ We have $U \cap V = (0)$ iff $u \wedge v \neq  0$.
$(2)$ If $U \cap V = (0)$, then $U + V$ is the least subspace associated with $u \wedge v$.

*Proof.* Assume $U \cap V = (0)$. We know by Corollary 34.26 that $(u_{1}, \dots  , u_{p})$ is a basis of $U$ and $(v_{1}, \dots  , v_{q})$ is a basis of $V$ . Since $U \cap V = (0), (u_{1}, \dots  , u_{p}, v_{1}, \dots  , v_{q})$ is a basis of $U +V$ , and by Proposition 34.8, we have
$$u \wedge v = u_{1} \wedge \cdots  \wedge u_{p} \wedge v_{1} \wedge \cdots  \wedge v_{q} \neq  0.$$
This also proves $(2)$.
