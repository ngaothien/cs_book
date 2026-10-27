# Making Good Use of Hyperplanes at Infinity


<!-- PAGE 925 -->
subspaces of $E$ have the same intersection with the hyperplane at infinity $P$ . There is
$$also a bijection between affine maps from e E to F and projective maps fromE \begin{pmatrix} \longrightarrow \\ E \\ to \end{pmatrix} F mapping$$
$$e e$$
$$the hyperplane at infinity P \begin{pmatrix} \longrightarrow \\ E \end{pmatrix} into the hyperplane at infinity P \begin{pmatrix} \longrightarrow \\ F \end{pmatrix} . In the projective$$
plane, two distinct lines intersect in a single point (possibly at infinity, when the lines are parallel). In the projective space, two distinct planes intersect in a single line (possibly at infinity, when the planes are parallel). In the projective space, a plane and a line not contained in that plane intersect in a single point (possibly at infinity, when the plane and the line are parallel).

## 26.9 Making Good Use of Hyperplanes at Infinity

Given a vector space $E$ and a hyperplane $H$ in $E$, we have already observed that the projective spaces $E_{H}$ and P(E) are isomorphic. Thus, P(H) can be viewed as the hyperplane at
$$f$$
infinity in P(E), and the considerations applying to the projective completion of an affine space apply to the affine patch $E_{H}$ on P(E). This fact yields a powerful and elegant method for proving theorems in projective geometry. The general schema is to choose some projective hyperplane P(H) in P(E), view it as the “hyperplane at infinity,” then prove an affine version of the desired result in the affine patch $E_{H}$ (the complement of P(H) in P(E), which has an affine structure), and then transfer this result back to the projective space P(E). This technique is often called “sending objects to infinity.” We refer the reader to geometry textbooks for a comprehensive development of these ideas (for example, Berger $[11, 12]$, Samuel $[148]$, Sidler $[167]$, Tisseron $[181]$, or Pedoe $[141])$, but we cannot resist presenting the projective versions of the theorems of Pappus and Desargues. Indeed, the method of sending points to infinity provides some strikingly elegant proofs. We begin with Pappus’s theorem, illustrated in Figure 26.20.

> **Proposition 26.18.** (Pappus) Given any projective plane P(E) and any two distinct lines $D$ and D', for any distinct points a, $b, c$, a', b', c', with a, $b, c$ on $D$ and a', b', c' on D', if a, $b, c$, a', b', c' are distinct from the intersection of $D$ and D', then the intersection points $p = \langle b, c'\rangle \cap \langle$ b', $c\rangle , q = \langle$ a, $c'\rangle \cap \langle$ a', $c\rangle$ , and $r = \langle$ a, $b'\rangle \cap \langle$ a', $b\rangle$ are collinear.

*Proof.* First, since any two lines in a projective plane intersect in a single point, the points $p, q, r$ are well defined. Choose $\Delta = \langle p, r\rangle$ as the line at infinity, and consider the affine plane $X =$ P(E) - $\Delta$ . Since $\langle$ a, $b'\rangle$ and $\langle$ a', $b\rangle$ intersect at a point at infinity $r$ on $\Delta , \langle$ a, $b'\rangle$ and $\langle$ a', $b\rangle$ are parallel, and similarly $\langle b, c'\rangle$ and $\langle$ b', $c\rangle$ are parallel. Thus, by the affine version of Pappus’s theorem (Proposition 24.12), the lines $\langle$ a, $c'\rangle$ and $\langle$ a', $c\rangle$ are parallel, which means that their intersection $q$ is on the line at infinity $\Delta = \langle p, r\rangle$ , which means that $p, q, r$ are collinear. By working in the projective completion of an affine plane, we can obtain an improved version of Pappus’s theorem for affine planes. The reader will have to figure out how to deal with the special cases where some of $p, q, r$ go to infinity.

<!-- PAGE 926 -->
$$c$$
$$b$$
$$a$$
$$q$$
$$r$$
$$p$$
$$a'$$
$$b'$$
$$c'$$
$$Figure 26.20: Pappus’s theorem (projective version).$$
Now, we prove a projective version of Desargues’s theorem slightly more general than that given in Proposition 26.7. It is interesting that the proof is radically different, depending on the dimension of the projective space P(E). This is not surprising. In axiomatic presentations of projective plane geometry, Desargues’s theorem is independent of the other axioms. Desargues’s theorem is illustrated in Figure 26.21.

> **Proposition 26.19.** (Desargues) Let P(E) be a projective space. Given two triangles (a, $b, c)$ and (a', b', c'), where the points a, $b, c$, a', b', c' are pairwise distinct and the lines $A = \langle b, c\rangle , B = \langle$ a, $c\rangle , C = \langle$ a, $b\rangle$ , A' $= \langle$ b', $c'\rangle$ , B' $= \langle$ a', $c'\rangle$ , C' $= \langle$ a', $b'\rangle$ are pairwise distinct, if the lines $\langle$ a, $a'\rangle , \langle b, b'\rangle$ , and $\langle c, c'\rangle$ intersect in a common point $d$ distinct from a, $b, c$, a', b', c', then the intersection points $p = \langle b, c\rangle \cap \langle$ b', $c'\rangle , q = \langle$ a, $c\rangle \cap \langle$ a', $c'\rangle$ , and $r = \langle$ a, $b\rangle \cap \langle$ a', $b'\rangle$ belong to a common line distinct from $A, B, C$, A', B', C'.

*Proof.* First, it is immediately shown that the line $\langle p, q\rangle$ is distinct from the lines $A, B, C$, A', B', C'. Let us assume that P(E) has dimension $n \ge 3$. If the seven points $d$, a, $b, c$, a', b', c' generate a projective subspace of dimension $3$, then by Proposition 26.1, the intersection of the two planes $\langle$ a, $b, c\rangle$ and $\langle$ a', b', $c'\rangle$ is a line, and thus $p, q, r$ are collinear. If P(E) has dimension $n = 2$ or the seven points $d$, a, $b, c$, a', b', c' generate a projective subspace of dimension $2$, we use the following argument. In the projective plane $X$ generated by the seven points $d$, a, $b, c$, a', b', c', choose the projective line $\Delta = \langle p, r\rangle$ as the line at infinity. Then in the affine plane $Y = X -\Delta$ , the lines $\langle b, c\rangle$ and $\langle$ b', $c'\rangle$ are parallel, and the lines $\langle$ a, $b\rangle$ and $\langle$ a', $b'\rangle$ are parallel, and the lines $\langle$ a, $a'\rangle , \langle b, b'\rangle$ , and $\langle c, c'\rangle$ are either parallel or concurrent. Then by the converse of the affine version of Desargues’s theorem (Proposition
