# Duality in Projective Geometry


<!-- PAGE 946 -->
has no eigenvalue in the field $K$ is quite different from the case where $f$ has some eigenvalue in $K$. In the first case, $h$ has no fixed point. It turns out that this implies that dim(E) is even and there is a simple description of the matrices representing an involution. If $h$ has some fixed point, then $f$ is an involution of $E$, so it has the eigenvalues $+1$ and $-1$, and $E$ is the direct sum of the corresponding eigenspaces $E_{1}$ and $E_{-1}$. Then $h$ can be described in terms of $\mathbb{P}(E_{1})$ and $\mathbb{P}(E_{-1})$. For details, we refer the reader to Vienne $[191]$ (Chapter IV, Propositions $11$ and $12)$.

## 26.12 Duality in Projective Geometry

We now consider duality in projective geometry. Given a vector space $E$ of finite dimension $n+1$, recall that its dual space $E^{*}$ is the vector space of all linear forms $f$ : $E \to K$ and that $E^{*}$ is isomorphic to $E$. We also have a canonical isomorphism between $E$ and its bidual $E^{**}$, which allows us to identify $E$ and $E^{**}$. Let $\mathcal{H}(E)$ denote the set of hyperplanes in P(E). In Section 26.3 we observed that the map
$$p(f) \mapsto P(\mathrm{Ker} f)$$
is a bijection between $P(E^{*})$ and $\mathcal{H}(E)$, in which the equivalence class p(f) $= {\lambda f$ | $\lambda  \neq  0}$ of a nonnull linear form $f \in E^{*}$ is mapped to the hyperplane P(Ker $f)$. Using the above bijection between $P(E^{*})$ and $\mathcal{H}(E)$, a projective subspace P(U) of $P(E^{*})$ (where $U$ is a subspace of $E^{*})$ can be identified with a subset of $\mathcal{H}(E)$, namely the family
$${P(H) | H = \mathrm{Ker} f, f \in U -{0}}$$
consisting of the projective hyperplanes in $\mathcal{H}(E)$ corresponding to nonnull linear forms in $U$. Such subsets of $\mathcal{H}(E)$ are called linear systems (of hyperplanes). The bijection between $P(E^{*})$ and $\mathcal{H}(E)$ allows us to view $\mathcal{H}(E)$ as a projective space, and linear systems as projective subspaces $of\mathcal{H}(E)$. In the projective $space\mathcal{H}(E)$, a point is a hyperplane in P(E)! The duality between subspaces of $E$ and subspaces of $E^{*}$ (reviewed below) and the fact that there is a bijection between $P(E^{*})$ and $\mathcal{H}(E)$ yields a powerful duality between the set of projective subspaces of P(E) and the set of linear systems in $\mathcal{H}(E)$ (or equivalently, the set of projective subspaces of $P(E^{*}))$. The idea of duality in projective geometry goes back to Gergonne and Poncelet, in the early nineteenth century. However, Poncelet had a more restricted type of duality in mind (polarity with respect to a conic or a quadric), whereas Gergonne had the more general idea of the duality between points and lines (or points and planes). This more general duality arises from a specific pairing between $E$ and $E^{*}$ (a nonsingular bilinear form). Here we consider the pairing $\langle$ -, $-\rangle$ : $E^{*} \times  E \to K$, defined such that
$$\langle f, v\rangle = f(v),$$

<!-- PAGE 947 -->
for all $f \in E^{*}$ and all $v \in E$. Recall that given a subset $V$ of $E$ (respectively a subset $U$ of $E^{*})$, the orthogonal $V^{0}$ of $V$ is the subspace of $E^{*}$ defined such that
$$V^{0}= {f \in E^{*}| \langle f, v\rangle = 0, for every v \in V },$$
and that the orthogonal $U^{0}$ of $U$ is the subspace of $E$ defined such that
$$U^{0}= {v \in E | \langle f, v\rangle = 0, for every f \in U} = \bigcap_{f\in U}  \mathrm{Ker} f.$$
Then, by Theorem 11.4 (since $E$ and $E^{*}$ have the same finite dimension $n + 1), U = U^{00} , V = V^{00}$ , and the maps
$$V \mapsto V^{0} andU \mapsto U^{0}$$
are inverse bijections, where $V$ is a subspace of $E$, and $U$ is a subspace of $E^{*}$. These maps set up a duality between subspaces of $E$ and subspaces of $E^{*}$. Furthermore, we know that $U$ has dimension $k$ iff $U^{0}$ has dimension $n +$ 1-k, and similarly for $V$ and $V^{0}$. Since a linear system $P =$ P(U) of hyperplanes in $\mathcal{H}(E)$ corresponds to a subspace $U$ of $E^{*}$, and since
$$U^{0}  = \bigcap_{f\in U}  \mathrm{Ker} f$$
is the intersection of all the hyperplanes defined by nonnull linear forms in $U$, we can view a linear system $P =$ P(U) $= P(U^{00}$ ) $in\mathcal{H}(E)$ as the family of hyperplanes in P(E) containing $P(U^{0}$ ). In view of the identification of $P(E^{*})$ with the set $\mathcal{H}(E)$ of hyperplanes in P(E), by passing to projective spaces, the above bijection between the set of subspaces of $E$ and the set of subspaces of $E^{*}$ yields a bijection between the set of projective subspaces of P(E) and the set of linear systems in $\mathcal{H}(E)$ (or equivalently, the set of projective subspaces of $P(E^{*}))$ called duality. Recall that a point of $\mathcal{H}(E)$ is a hyperplane in P(E). More specifically, assuming that $E$ has dimension $n + 1$, so that P(E) has dimension $n$, if $Q =$ P(V ) is any projective subspace of P(E) (where $V$ is any subspace of $E)$ and if $P =$ P(U) is any linear system in $\mathcal{H}(E)$ (where $U$ is any subspace of $E^{*})$, we get a subspace $Q^{0}$ of $\mathcal{H}(E)$ defined by
$$Q^{0}= {P(H) | Q \subseteq P(H), P(H) a hyperplane in \mathcal{H}(E)},$$
and a subspace $P^{0}$ of P(E) defined by
$$P^{0}= \bigcap  {P(H) | P(H) \in P, P(H) a hyperplane in \mathcal{H}(E)}.$$
We have $P = P^{00}$ and $Q = Q^{00}$. Since $Q^{0}$ is determined by $P(V^{0})$, if $Q =$ P(V ) has dimension $k$ (i.e., if $V$ has dimension $k + 1)$, then $Q^{0}$ has dimension $n$ - $k$ - $1$ (since $V$ has dimension $k + 1$ and dim(E) $= n + 1$, then $V^{0}$ has dimension $n + 1$ -(k $+ 1) = n -k)$. Thus,
$$\dim(Q) + \dim(Q^{0}) = n -1,$$

<!-- PAGE 948 -->
and similarly, dim(P) $+ dim(P^{0}$ ) $= n$ - $1$. A linear system $P =$ P(U) of hyperplanes in $\mathcal{H}(E)$ is called a pencil of hyperplanes if it corresponds to a projective line in $P(E^{*})$, which means that $U$ is a subspace of dimension $2$ of $E^{*}$. From dim(P) $+ dim(P^{0}$ ) $= n$ - $1$, a pencil of hyperplanes $P$ is the family of hyperplanes in $\mathcal{H}(E)$ containing some projective subspace P(V ) of dimension $n$ - $2$ (where P(V ) is a projective subspace of P(E), and P(E) has dimension $n)$. When $n = 2$, a pencil of hyperplanes in $\mathcal{H}(E)$, also called a pencil of lines, is the family of lines passing through a given point. When $n = 3$, a pencil of hyperplanes in $\mathcal{H}(E)$, also called a pencil of planes, is the family of planes passing through a given line. When $n = 2$, the above duality takes a rather simple form. In this case (of a projective plane P(E)), the duality is a bijection between points in P(E) and lines in $P(E^{*})$, represented by pencils of lines in $\mathcal{H}(E)$, with the following properties: $\bullet  A$ point a in P(E) maps to the line $D_{a}$ in $P(E^{*})$ represented by the pencil of lines in $\mathcal{H}(E)$ containing a, also denoted by $a^{*}$. See Figure 26.36. $\bullet  A$ line $D$ in P(E) maps to the point $p_{D}$ in $P(E^{*})$ represented by the line $D$ in $\mathcal{H}(E)$. See Figure 26.37. $\bullet$  Two points a, $b$ in P(E) map to lines $D_{a}, D_{b}$ in $P(E^{*})$ represented by pencils of lines through a and $b$, and the intersection of $D_{a}$ and $D_{b}$ is the point $p_{\langle a,b\rangle}$ in $P(E^{*})$ corresponding to the line $\langle$ a, $b\rangle$ belonging to both pencils. The point $p_{\langle a,b\rangle}$ is the image of the line $\langle$ a, $b\rangle$ via duality. See Figure 26.38 $\bullet  A$ line $D$ in P(E) containing two points a, $b$ maps to the intersection $p_{D}$ of the lines $D_{a}$ and $D_{b}$ in $P(E^{*})$ which are the images of a and $b$ under duality. This is because a, $b$ map to lines $D_{a}, D_{b}$ in $P(E^{*})$ represented by pencils of lines through a and $b$, and the intersection of $D_{a}$ and $D_{b}$ is the point $p_{D}$ in $P(E^{*})$ corresponding to the line $D = \langle$ a, $b\rangle$ belonging to both pencils. The point $p_{D}$ is the image of the line $D = \langle$ a, $b\rangle$ under duality. Once again, see Figure 26.38. $\bullet$  If $a \in D$, where a is a point and $D$ is a line in P(E), then $p_{D} \in D_{a}$ in $P(E^{*})$. This is because under duality, a is mapped to the line $D_{a}$ in $P(E^{*})$ represented by the pencil of lines containing a, and $D$ is mapped to the point $p_{D} \in P(E^{*})$ represented by the line $D$ through a in this pencil, so $p_{D} \in D_{a}$. The reader will discover that the dual of Desargues’s theorem is its converse. This is a nice way of getting the converse for free! We will not spoil the reader’s fun and let him discover the dual of Pappus’s theorem. In general, when $n \ge 2$, the above duality is a bijection between points in P(E) and hyperplanes in $P(E^{*})$, which are represented by linear systems of dimension $n$ - $1$ in $\mathcal{H}(E)$, with the following properties:

<!-- PAGE 949 -->
$$P(E)$$
$$a$$
$$x$$
$$x$$
$$P(E*)$$
$$Da$$
$$b*a*$$
$$x*$$
$$x*$$
$$H (E)$$
$$DDb*$$
$$a*$$
$$a$$
$$z = 1$$

![Figure 26.36](../../assets/ch26/fig_26_36.png)

**Figure 26.36:** The duality between a point in P(E) and a line in $P(E^{*})$. The line in $P(E^{*})$ is also represented by the pencil of lines through a in $\mathcal{H}(E). \bullet  A$ point a in P(E) maps to the hyperplane $H_{a}$ in $P(E^{*})$ (the linear system of hyperplanes in $\mathcal{H}(E)$ containing a, also denoted by $a^{*}). \bullet  A$ hyperplane $H$ in P(E) maps to the point $p_{H}$ in $P(E^{*})$ (represented by the hyperplane $H$ in $\mathcal{H}(E))$. To conclude our quick tour of projective geometry, we establish a connection between the cross-ratio of hyperplanes in a pencil of hyperplanes with the cross-ratio of the intersection points of any line not contained in any hyperplane in this pencil with four hyperplanes in this pencil.
