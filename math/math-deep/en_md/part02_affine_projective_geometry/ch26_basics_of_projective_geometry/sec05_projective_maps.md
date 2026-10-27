# Projective Maps


<!-- PAGE 898 -->

## 26.5 Projective Maps

Given two nontrivial vector spaces $E$ and $F$ and a linear map $f$ : $E \to F$, observe that for every $u, v \in (E$ - Ker $f)$, if $v = \lambda u$ for some $\lambda  \in K -{0}$, then f(v) $= \lambda$ f(u), and thus $f$ restricted to $(E$ -Ker $f)$ induces a function P(f): (P(E) -P(Ker $f)) \to$ P(F) defined such that
$$P(f)([u]_{\sim}) = [f(u)]_{\sim},$$
as in the following commutative diagram:
$$f$$
$$E -\mathrm{Ker} fF -{0}$$
$$pp$$
$$P(E) -P(\mathrm{Ker} f)_{P(f)} /P(F)$$
When $f$ is injective, i.e., when Ker $f = {0}$, then P(f): P(E) $\to$ P(F) is indeed a welldefined function. The above discussion motivates the following definition.

> **Definition 26.5.** Given two nontrivial vector spaces $E$ and $F$, any linear map $f$ : $E \to F$ induces a partial map P(f): P(E) $\to$ P(F) called a projective map, such that if Ker $f = {u \in E$ | f(u) $= 0}$ is the kernel of $f$, then P(f): (P(E)-P(Ker $f)) \to$ P(F) is a total map defined such that
$$P(f)([u]_{\sim}) = [f(u)]_{\sim},$$
as in the following commutative diagram:
$$f$$
$$E -\mathrm{Ker} fF -{0}$$
$$pp$$
$$P(E) -P(\mathrm{Ker} f)_{P(f)} /P(F)$$
If $f$ is injective, i.e., when Ker $f = {0}$, then P(f): P(E) $\to$ P(F) is a total function called a projective transformation, and when $f$ is bijective, we call P(f) a projectivity, or projective isomorphism, or homography. The set of projectivities P(f): P(E) $\to$ P(E) is a group called the projective (linear) group, and is denoted by PGL(E).  One should realize that if a linear map $f$ : $E \to F$ is not injective, then the projective
$$map P(f): P(E) \to P(F) is only a partial map, i.e., it is undefined on P(\mathrm{Ker} f). In$$
particular, if $f$ : $E \to F$ is the null map (i.e., Ker $f = E)$, the domain of P(f) is empty and P(f) is the partial function undefined everywhere. We might want to require in Definition 26.5 that $f$ not be the null map to avoid this degenerate case. Projective maps are often defined only when they are induced by bijective linear maps.

<!-- PAGE 899 -->
We take a closer look at the projectivities of the projective $line\mathbb{P}_{K}^{1}$, since they play a role in the “change of parameters” for projective curves. A projectivity $f$ : $\mathbb{P}_{K}^{1} \to \mathbb{P}_{K}^{1}$ is induced by some bijective linear map $g: K^{2} \to K^{2}$ given by some invertible matrix
$$M(g) = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$
with ad -bc $\neq  0$. Since the projective line $\mathbb{P}_{K}^{1}$ is isomorphic to $K \cup {\infty$ }, it is easily verified that $f$ is defined as follows:
$$$$
$$z \frac{az + b}{cz + d} if z \neq  - \frac{d}{c} ,$$
$$$$
$$$$
$$$$
$$c \neq  0- \frac{\mapsto d}{c} \mapsto \infty ,$$
$$$$
$$\infty \mapsto \frac{a}{c} ;c = 0z \mapsto \frac{az + b}{d} ,$$
$$$$
$$$$
$$\infty \mapsto \infty .$$
$$$$
From Section 26.4, we know that the points not at infinity are repesented by vectors of the form $(z, 1)$ where $z \in K$ and that $\infty$ is represented by $(1, 0)$. First, assume $c \neq  0$. Since
$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} z \\ 1 \end{pmatrix} = \begin{pmatrix} az + b \\ cz + d \end{pmatrix} ,$$
if cz $+ d \neq  0$, that is, $z \neq  -d/c$, then
$$(az + b, cz + d) \sim \begin{pmatrix} az + b \\ , 1 \\ cz + d \end{pmatrix} ,$$
so $z$ is is mapped to (az $+ d)/cz + d)$. If cz $+ d = 0$, then
$$(az + d, 0) \sim (1, 0) = \infty ,$$
so $-d/c$ is mapped to $\infty$ . We also have
$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} a \\ c \end{pmatrix} ,$$
and since $c \neq  0$ we have
$$(a, c) \sim (a/c, 1),$$
so $\infty$ is mapped to $a/c$. The case where $c = 0$ is handled similarly. If $K = \mathbb{R}$ or $K = \mathbb{C}$, note that $a/c$ is the limit of (az $+ b)/(cz + d)$, as $z$ approaches infinity, and the limit of (az $+ b)/(cz + d)$ as $z$ approaches $-d/c$ is $\infty$ (when $c \neq  0)$. Projections between hyperplanes form an important example of projectivities.

<!-- PAGE 900 -->

> **Definition 26.6.** Given a projective space P(E), for any two distinct hyperplanes P(H) and P(H'), for any point $c \in$ P(E) neither in P(H) nor in P(H'), the projection (or perspectivity) of center $c$ between P(H) and P(H') is the map $f$ : P(H) $\to$ P(H') defined such that for every $a \in$ P(H), the point f(a) is the intersection of the line $\langle c, a\rangle$ through $c$ and a with P(H'). Let us verify that $f$ is well–defined and a bijective projective transformation. Since the hyperplanes P(H) and P(H') are distinct, the hyperplanes $H$ and H' in $E$ are distinct, and since $c$ is neither in P(H) nor in P(H'), letting $c =$ p(u) for some nonnull vector $u \in E$, then $u \in / H$ and $u \in /$ H', and thus $E = H \oplus$ Ku $=$ H' $\oplus$ Ku. If $\pi$ : $E \to$ H' is the linear map (projection onto H' parallel to $u)$ defined such that
$$\pi (w + \lambda u) = w,$$
for all $w \in$ H' and all $\lambda  \in K$, since $E = H \oplus$ Ku $=$ H' $\oplus$ Ku, the restriction $g: H \to$ H' of $\pi$ : $E \to$ H' to $H$ is a linear bijection between $H$ and H', and clearly $f =$ P(g), which shows that $f$ is a projectivity.
Remark: Going back to the linear map $\pi$ : $E \to$ H' (projection onto H' parallel to $u)$, note that $P(\pi$ ): P(E) $\to$ P(H') is also a projective map, but it is not injective, and thus only a partial map. More generally, given a direct sum $E = V \oplus W$, the projection $\pi$ : $E \to V$ onto $V$ parallel to $W$ induces a projective map $P(\pi$ ): P(E) $\to$ P(V ), and given another direct sum $E = U \oplus W$, the restriction of $\pi$  to $U$ induces a perspectivity $f$ between P(U) and P(V ). Geometrically, $f$ is defined as follows: Given any point $a \in$ P(U), if $\langle$ P(W), $a\rangle$ is the smallest projective subspace containing P(W) and a, the point f(a) is the intersection of $\langle$ P(W), $a\rangle$ with P(V ). Figure 26.11 illustrates a projection $f$ of center $c$ between two projective lines $\Delta$ and $\Delta'$ (in the real projective plane). If we consider three distinct points $d_{1}, d_{2}, d_{3}$ on $\Delta$ and their images $d_{1}', d_{2}', d_{3}'$ on $\Delta'$ under the projection $f$, then ratios are not preserved, that is,
$$\frac{-\longrightarrow d_{3}d_{1}}{d_{3}d_{2}} -\longrightarrow = \frac{-\longrightarrow d_{3}'d_{1}'}{d_{3}'d_{2}'} -\longrightarrow .$$
However, if we consider four distinct points $d_{1}, d_{2}, d_{3}, d_{4}$ on $\Delta$ and their images $d_{1}', d_{2}', d_{3}', d_{4}'$ on $\Delta'$ under the projection $f$, we will show later that we have the following preservation of the so-called “cross-ratio”
$$\frac{-\longrightarrow d_{3}d_{1}}{d_{3}d_{2}} , \frac{-\longrightarrow d_{4}d_{1}}{d_{4}d_{2}} = \frac{-\longrightarrow d_{3}'d_{1}'}{d_{3}'d_{2}'} , \frac{-\longrightarrow d_{4}'d_{1}'}{d_{4}'d_{2}'} .$$
$$-\longrightarrow -\longrightarrow -\longrightarrow -\longrightarrow$$
Cross-ratios and projections play an important role in geometry (for some very elegant illustrations of this fact, see Sidler $[167])$.

<!-- PAGE 901 -->
$$c$$
$$d_{1}$$
$$d_{2}$$
$$d_{3}$$
$$d_{4}$$
$$\Delta$$
$$d_{1}'d_{2}'d_{3}'d_{4}'\Delta'$$
$$D_{1}D_{2}D_{3}D_{4}$$
$$Figure 26.11: A projection of center c between two lines \Delta and \Delta' .$$
We now turn to the issue of determining when two linear maps $f, g$ determine the same projective map, i.e., when P(f) $=$ P(g). The following proposition gives us a complete answer.

> **Proposition 26.4.** Given two nontrivial vector spaces $E$ and $F$, for any two linear maps $f$ : $E \to F$ and $g: E \to F$, we have P(f) $=$ P(g) iff there is some scalar $\lambda  \in K -{0}$ such that $g = \lambda f$.

*Proof.* If $g = \lambda f$, it is clear that P(f) $=$ P(g). Conversely, in order to have P(f) $=$ P(g), we must have Ker $f =$ Ker $g$. If Ker $f =$ Ker $g = E$, then $f$ and $g$ are both the null map, and this case is trivial. If $E$ -Ker $f \neq  \emptyset$ , by taking a basis of Im $f$ and some inverse image of this basis, we obtain a basis $B$ of a subspace $G$ of $E$ such that $E =$ Ker $f \oplus G$. If dim(G) $= 1$, the restriction of any linear map $f$ : $E \to F$ to $G$ is determined by some nonzero vector $u \in E$ and some scalar $\lambda  \in K$, and the proposition is obvious. Thus, assume that dim(G) $\ge 2$. For any two distinct basis vectors $u, v \in B$, since P(f) $=$ P(g), there must be some nonzero scalars $\lambda (u), \lambda (v)$, and $\lambda (u + v)$ such that
$$g(u) = \lambda (u)f(u),g(v) = \lambda (v)f(v),g(u + v) = \lambda (u + v)f(u + v).$$
Since $f$ and $g$ are linear, we get
$$g(u) + g(v) = \lambda (u)f(u) + \lambda (v)f(v) = \lambda (u + v)(f(u) + f(v)),$$
that is,
$$(\lambda (u + v) -\lambda (u))f(u) + (\lambda (u + v) -\lambda (v))f(v) = 0.$$
Since $f$ is injective on $G$ and $u, v \in B \subseteq G$ are linearly independent, f(u) and f(v) are also linearly independent, and thus we have
$$\lambda (u + v) = \lambda (u) = \lambda (v).$$

<!-- PAGE 902 -->
Now we have shown that $\lambda (u) = \lambda (v)$, for any two distinct basis vectors in $B$, which proves that $\lambda (u)$ is independent of $u \in G$, and proves that $g = \lambda f$. Proposition 26.4 shows that the projective linear group PGL(E) is isomorphic to the quotient group of the linear group GL(E) modulo the subgroup $K^{*}id_{E}$ (where $K^{*} = K$ - ${0})$. Using projective frames, we prove the following useful result.

> **Proposition 26.5.** Given two nontrivial vector spaces $E$ and $F$ of the same dimension $n + 1$, for any two projective frames $(a_{i})_{1\le i\le n+2}$ for P(E) and $(b_{i})_{1\le i\le n+2}$ for P(F), there is a unique projectivity $h$: P(E) $\to$ P(F) such that $h(a_{i}) = b_{i}$ for $1 \le i \le n + 2$.

*Proof.* Let $(u_{1}, \dots  , u_{n+1})$ be a basis of $E$ associated with the projective frame $(a_{i})_{1\le i\le n+2}$, and let $(v_{1}, \dots  , v_{n+1})$ be a basis of $F$ associated with the projective frame $(b_{i})_{1\le i\le n+2}$. Since $(u_{1}, \dots  , u_{n+1})$ is a basis, there is a unique linear bijection $g: E \to F$ such that $g(u_{i}) = v_{i}$, for $1 \le i \le n + 1$. Clearly, $h =$ P(g) is a projectivity such that $h(a_{i}) = b_{i}$, for $1 \le i \le n + 2$. Let h': P(E) $\to$ P(F) be any projectivity such that $h'(a_{i}) = b_{i}$, for $1 \le i \le n + 2$. By definition, there is a linear isomorphism $f$ : $E \to F$ such that h' $=$ P(f). Since $h'(a_{i}) = b_{i}$, for $1 \le i \le n + 2$, we must have $f(u_{i}) = \lambda_{i} v_{i}$, for some $\lambda_{i}  \in K -{0}$, where $1 \le i \le n + 1$, and
$$f(u_{1} + \cdots  + u_{n+1}) = \lambda (v_{1} + \cdots  + v_{n+1}),$$
for some $\lambda  \in K -{0}$. By linearity of $f$, we have
$$\lambda_{1} v_{1} + \cdots  + \lambda_{n+1} v_{n+1} = \lambda v_{1} + \cdots  + \lambda v_{n+1},$$
and since $(v_{1}, \dots  , v_{n+1})$ is a basis of $F$, we must have
$$\lambda_{1}  = \cdots  = \lambda_{n+1}  = \lambda .$$
This shows that $f = \lambda g$, and thus that
$$h'= P(f) = P(g) = h,$$
and $h$ is uniquely determined.  The above proposition and Proposition 26.4 are false if $K$ is a skew field. Also,
$$Proposition 26.5 fails if (b_{i})_{1\le i\le n+2} is not a projective frame, or if a_{n+2} is dropped.$$
As a corollary of Proposition 26.5, given a projective space P(E), two distinct projective lines $D$ and D' in P(E), three distinct points a, $b, c$ on $D$, and any three distinct points a', b', c' on D', there is a unique projectivity from $D$ to D', mapping a to a', $b$ to b', and $c$ to c'. This is because, as we mentioned earlier, any three distinct points on a line form a projective frame.
Remark: As in the affine case, there is “fundamental theorem of projective geometry.” For simplicity, we state this theorem assuming that vector spaces are over the field $K =\mathbb{R}$. Given

<!-- PAGE 903 -->
any two projective spaces P(E) and P(F) of the same dimension $n \ge 2$, for any bijective function $f$ : P(E) $\to$ P(F), if $f$ maps any three distinct collinear points a, $b, c$ to collinear points f(a), f(b), f(c), then $f$ is a projectivity. For more general fields, $f =$ P(g) for some “semilinear” bijection $g: E \to F$. A map such as $f$ (preserving collinearity of any three distinct points) is often called a collineation. For $K = \mathbb{R}$, collineations and projectivities coincide. For more details, see Samuel $[148]$. Before closing this section, we illustrate the power of Proposition 26.5 by proving two interesting results. We begin by characterizing perspectivities between lines.
$$\mathbb{RP}^{2}$$

> **Proposition 26.6.** Given any two distinct lines $D$ and D' in the real projective plane , a projectivity $f$ : $D \to$ D' is a perspectivity iff f(O) $= O$, where $O$ is the intersection of $D$ and D'.

*Proof.* If $f$ : $D \to$ D' is a perspectivity, then by the very definition of $f$, we have f(O) $= O$. Conversely, let $f$ : $D \to$ D' be a projectivity such that f(O) $= O$. Let a, $b$ be any two distinct points on $D$ also distinct from $O$, and let a' $=$ f(a) and b' $=$ f(b) on D'. Since $f$ is a bijection and since a, $b, O$ are pairwise distinct, a' $\neq$  b'. Let $c$ be the intersection of the lines $\langle$ a, $a'\rangle$ and $\langle b, b'\rangle$ , which by the assumptions on a, $b, O$, cannot be on $D$ or D'. Then we can define the perspectivity $g: D \to$ D' of center $c$, and by the definition of $c$, we have
$$g(a) = a',g(b) = b',g(O) = O.$$
See Figure 26.12. However, $f$ agrees with $g$ on $O$, a, $b$, and since $(O$, a, $b)$ is a projective frame for $D$, by Proposition 26.5, we must have $f = g$. Using Proposition 26.6, we can give an elegant proof of a version of Desargues’s theorem (in the plane).

> **Proposition 26.7.** (Desargues) Given two triangles (a, $b, c)$ and (a', b', c') $in\mathbb{RP}^{2}$, where the points a, $b, c$, a', b', c' are pairwise distinct and the lines $A = \langle b, c\rangle , B = \langle$ a, $c\rangle , C = \langle$ a, $b\rangle$ , A' $= \langle$ b', $c'\rangle$ , B' $= \langle$ a', $c'\rangle$ , C' $= \langle$ a', $b'\rangle$ are pairwise distinct, if the lines $\langle$ a, $a'\rangle , \langle b, b'\rangle$ , and $\langle c, c'\rangle$ intersect in a common point $d$ distinct from a, $b, c$, a', b', c', then the intersection points $p = \langle b, c\rangle \cap \langle$ b', $c'\rangle , q = \langle$ a, $c\rangle \cap \langle$ a', $c'\rangle$ , and $r = \langle$ a, $b\rangle \cap \langle$ a', $b'\rangle$ belong to a common line distinct from $A, B, C$, A', B', C'.

*Proof.* In view of the assumptions on a, $b, c$, a', b', c', and $d$, the point $r$ is on neither $\langle$ a, $a'\rangle$ nor $\langle b, b'\rangle$ , the point $p$ is on neither $\langle b, b'\rangle$ nor $\langle c, c'\rangle$ , and the point $q$ is on neither $\langle$ a, $a'\rangle$ nor $\langle c, c'\rangle$ . It is also immediately shown that the line $\langle p, q\rangle$ is distinct from the lines $A, B, C$, A', B', C'. Let $f$ : $\langle$ a, $a'\rangle \to \langle b, b'\rangle$ be the perspectivity of center $r$ and $g: \langle b, b'\rangle \to \langle c, c'\rangle$ be the perspectivity of center $p$. Let $h = g \circ f$. Since both f(d) $= d$ and g(d) $= d$, we also have
