# Projective Subspaces


<!-- PAGE 881 -->
obtained by taking the quotient of the (upper) half-sphere $S_{+}^{n}$, by the equivalence relation identifying antipodal points $a_{+}$ and $a_{-}$ on the boundary of the half-sphere.
$$\mathbb{CP}^{1} \mathbb{C}^{2}$$
Another interesting fact is that the complex projective line $= P($ ) is homeomor-
$$\mathbb{RP}^{3}$$
phic to the (real) 2-sphere $S^{2}$, and that the real projective space is homeomorphic to the group of rotations SO(3) of $\mathbb{R}^{3}$.
$(2)$ If $H$ is a hyperplane in $E$, recall from Proposition 11.7 that there is some nonnull linear form $f \in E^{*}$ such that $H =$ Ker $f$. Also, given any nonnull linear form $f \in E^{*}$, its kernel $H =$ Ker $f = f^{-1} (0)$ is a hyperplane, and if Ker $f =$ Ker $g = H$, then $g = \lambda f$ for some $\lambda  \neq  0$. These facts can be concisely stated by saying that the map
$$[f]_{\sim}\mapsto \mathrm{Ker} f$$
mapping the equivalence class $[f]_{\sim} = {\lambda f$ | $\lambda  \neq  0}$ of a nonnull linear form $f \in E^{*}$ to the hyperplane $H =$ Ker $f$ in $E$ is a bijection between the projective space $P(E^{*})$ and the set of hyperplanes in $E$. When $E$ is of finite dimension, this bijection yields a useful duality, which will be investigated in Section 26.12. We now define projective subspaces.

## 26.3 Projective Subspaces

Projective subspaces of a projective space P(E) are induced by subspaces of the vector space $E$.

> **Definition 26.2.** Given a nontrivial vector space $E$, a projective subspace (or linear projective variety) of P(E) is any subset $W$ of P(E) such that there is some subspace V̸ $= {0}$ of $E$ with $W =$ p(V $-{0})$. The dimension dim(W) of $W$ is defined as follows: If $V$ is of infinite dimension, then dim(W) $=$ dim(V ), and if dim(V ) $= p \ge 1$, then dim(W) $= p$ - $1$. We say that a family $(a_{i})_{i\in I}$ of points of P(E) is projectively independent if there is a linearly independent family $(u_{i})_{i\in I}$ in $E$ such that $a_{i} = p(u_{i})$ for every $i \in$ I.
Remark: If we allow the empty subset to be a projective subspace, then if assign the empty subset to the trivial subspace ${0}$, we obtain a bijection between the subspaces of $E$ and the projective subspaces of P(E). If P(V ) is the projective space induced by the vector space $V$ , we also denote p(V $-{0})$ by P(V ), or even by p(V ), even though p(0) is undefined. A projective subspace of dimension $0$ is a called a (projective) point. A projective subspace of dimension $1$ is called a (projective) line, and a projective subspace of dimension $2$ is called a (projective) plane. If $H$ is a hyperplane in $E$, then P(H) is called a projective hyperplane. It is easily verified that any arbitrary intersection of projective subspaces is a projective subspace.

<!-- PAGE 882 -->
A single point is projectively independent. Two points a, $b$ are projectively independent if a̸ $= b$. Two distinct points define a (unique) projective line. Three points a, $b, c$ are projectively independent if they are distinct, and neither belongs to the projective line defined by the other two. Three projectively independent points define a (unique) projective plane. A closer look at projective subspaces will show some of the advantages of projective geometry: In considering intersection properties, there are no exceptions due to parallelism, as in affine spaces. Let $E$ be a nontrivial vector space. Given any nontrivial subset $S$ of $E$, the subset $S$ defines a subset $U =$ p(S $-{0})$ of the projective space P(E), and if $\langle S\rangle$ denotes the subspace of $E$ spanned by $S$, it is immediately verified that $P(\langle S\rangle$ ) is the intersection of all projective subspaces containing $U$, and this projective subspace is denoted by $\langle U\rangle$ . Then $n \ge 2$ point $a_{1}, \dots  , a_{n} \in$ P(E) are projectively independent iff for all $i = 1, \dots  , n$ the point $a_{i}$ does not belong to the projective subspace $\langle a_{1}, \dots  , a_{i-1}, a_{i+1}, \dots  , a_{n}\rangle$ spanned by ${a_{1}, \dots  , a_{i-1}, a_{i+1}, \dots  , a_{n}}$. Given any subspaces $M$ and $N$ of $E$, recall from Proposition 24.15 that we have the Grassmann relation
$$\dim(M) + \dim(N) = \dim(M + N) + \dim (M \cap N).$$
Then the following proposition is easily shown.

> **Proposition 26.1.** Given a projective space P(E), for any two projective subspaces $U, V$ of P(E), we have
$$\dim(U) + \dim(V ) = \dim(\langle U \cup V \rangle ) + \dim (U \cap V ).$$
Furthermore, if $dim(U)+dim(V$ ) $\ge$ dim(P(E)), then $U \cap V$ is nonempty and if dim(P(E)) $= n$, then:
$(i)$ The intersection of any $n$ hyperplanes is nonempty.
(ii) For every hyperplane $H$ and every point $a \in / H$, every line $D$ containing a intersects $H$ in a unique point.
(iii) In a projective plane, every two distinct lines intersect in a unique point. As a corollary, in 3D projective space (dim(P(E)) $= 3)$, for every plane $H$, every line not contained in $H$ intersects $H$ in a unique point. It is often useful to deal with projective hyperplanes in terms of nonnull linear forms and equations. Recall that the map
$$[f]_{\sim}\mapsto \mathrm{Ker} f$$

<!-- PAGE 883 -->
is a bijection between $P(E^{*})$ and the set of hyperplanes in $E$, mapping the equivalence class $[f]_{\sim} = {\lambda f$ | $\lambda  \neq  0}$ of a nonnull linear form $f \in E^{*}$ to the hyperplane $H =$ Ker $f$. Furthermore, if $u \sim v$, which means that $u = \lambda v$ for some $\lambda  \neq  0$, we have
$$f(u) = 0ifff(v) = 0,$$
since f(v) $= \lambda$ f(u) and $\lambda  \neq  0$. Thus, there is a bijection
$${\lambda f | \lambda  \neq  0} \mapsto P(\mathrm{Ker} f)$$
mapping points in $P(E^{*})$ to hyperplanes in P(E). Any nonnull linear form $f$ associated with some hyperplane P(H) in the above bijection (i.e., $H =$ Ker $f)$ is called an equation of the projective hyperplane P(H). We also say that $f = 0$ is the equation of the hyperplane P(H). Before ending this section, we give an example of a projective space where lines have a nontrivial geometric interpretation, namely as “pencils of lines.” If $E = \mathbb{R}^{3}$, recall that the
$$\mathbb{R}^{3} \mathbb{R}$$
dual space $E^{*}$ is the set of all linear maps $f$ : $\to$ . As we have just explained, there is a bijection
$$p(f) \mapsto P(\mathrm{Ker} f)$$
between $P(E^{*})$ and the set of lines in P(E), mapping every point $a^{*} =$ p(f) to the line $D_{a*} =$ P(Ker $f)$. Is there a way to give a geometric interpretation in P(E) of a line $\Delta$ in $P(E^{*})$? Well, a line $\Delta$ in $P(E^{*})$ is defined by two distinct points $a^{*} =$ p(f) and $b^{*} =$ p(g), where $f, g \in E^{*}$ are two linearly independent linear forms. But $f$ and $g$ define two distinct planes $H_{1} =$ Ker $f$ and $H_{2} =$ Ker $g$ through the origin (in $E = \mathbb{R}^{3})$, and $H_{1}$ and $H_{2}$ define two distinct lines $D_{1} = p(H_{1})$ and $D_{2} = p(H_{2})$ in P(E). The line $\Delta$ in $P(E^{*})$ is of the form $\Delta =$ p(V ), where
$$V = {\lambda f + \mu g | \lambda , \mu  \in \mathbb{R}}$$
is the plane in $E^{*}$ spanned by $f, g$. Every nonnull linear form $\lambda f + \mu g \in V$ defines a plane $H =$ Ker $(\lambda f + \mu g)$ in $E$, and since $H_{1}$ and $H_{2}$ (in $E)$ are distinct, they intersect in a line $L$ that is also contained in every plane $H$ as above. Thus, the set of planes in $E$ associated with nonnull linear forms in $V$ is just the set of all planes containing the line $L$. Passing to P(E) using the projection $p$, the line $L$ in $E$ corresponds to the point $c =$ p(L) in P(E), which is just the intersection of the lines $D_{1}$ and $D_{2}$. Thus, every point of the line $\Delta$ in $P(E^{*})$ corresponds to a line in P(E) passing through $c$ (the intersection of the lines $D_{1}$ and $D_{2})$, and this correspondence is bijective. In summary, a line $\Delta$ in $P(E^{*})$ corresponds to the set of all lines in P(E) through some given point. Such sets of lines are called pencils of lines and are illustrated in Figure 26.6. The above discussion can be generalized to higher dimensions and is discussed quite extensively in Section 26.12. In brief, letting $E =\mathbb{R}^{n+1}$, there is a bijection mapping points in $P(E^{*})$ to hyperplanes in P(E). A line in $P(E^{*})$ corresponds to a pencil of hyperplanes in
