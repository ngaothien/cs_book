# The Cross-Ratio


<!-- PAGE 927 -->
24.13), the lines $\langle$ a, $c\rangle$ and $\langle$ a', $c'\rangle$ are parallel, which means that their intersection $q$ belongs to the line at infinity $\Delta = \langle p, r\rangle$ , and thus that $p, q, r$ are collinear.
$$q$$
$$a'$$
$$ap$$
$$d \frac{bb'}{c}$$
$$c'$$
$$r$$
$$Figure 26.21: Desargues’s theorem (projective version).$$
The converse of Desargues’s theorem also holds. Using the projective completion of an affine space, it is easy to state an improved affine version of Desargues’s theorem. The reader will have to figure out how to deal with the case where some of the points $p, q, r$ go to infinity. It can also be shown that Pappus’s theorem implies Desargues’s theorem. Many results of projective or affine geometry can be obtained using the method of “sending points to infinity.” We now discuss briefly the notion of cross-ratio, since it is a major concept of projective geometry.

## 26.10 The Cross-Ratio

Recall that affine maps preserve the ratio of three collinear points. In general, projective maps do not preserve the ratio of three collinear points. However, bijective projective maps preserve the “ratio of ratios” of any four collinear points (three of which are distinct). Such ratios are called cross-ratios (in French, “birapport”). There are several ways of introducing

<!-- PAGE 928 -->
cross-ratios, but since we already have Proposition 26.5 at our disposal, we can circumvent some of the tedious calculations needed if other approaches are chosen. Given a field $K$, say $K =\mathbb{R}$, recall that the projective line $\mathbb{P}_{K}^{1}$ consists of all equivalence classes $[x, y]$ of pairs $(x, y) \in K^{2}$ such that $(x, y) \neq  (0, 0)$, under the equivalence relation $\sim$ defined such that
$$(x_{1}, y_{1}) \sim (x_{2}, y_{2})iff x_{2} = \lambda x_{1}andy_{2} = \lambda y_{1},$$
for some $\lambda  \in K-{0}$. Letting $\infty = [1, 0]$, the projective $line\mathbb{P}_{K}^{1}$ is in bijection with $K\cup {\infty$ }. Furthermore, letting $0 = [0, 1]$ and $1 = [1, 1]$, the triple $(\infty , 0, 1)$ forms a projective frame for $\mathbb{P}_{K}^{1}$. Using this projective frame and Proposition 26.5, we define the cross-ratio of four collinear points as follows.

> **Definition 26.8.** Given a projective line $\Delta =$ P(D) over a field $K$, for any sequence (a, $b, c, d)$ of four points in $\Delta$ , where a, $b, c$ are distinct (i.e., (a, $b, c)$ is a projective frame), the cross-ratio [a, $b, c, d]$ is defined as the element h(d) $\in \mathbb{P}_{K}^{1}$, where $h: \Delta \to \mathbb{P}_{K}^{1}$ is the unique projectivity such that h(a) $= \infty$ , h(b) $= 0$, and h(c) $= 1$ (which exists by Proposition 26.5, since (a, $b, c)$ is a projective frame for $\Delta$ and $(\infty , 0, 1)$ is a projective frame for $\mathbb{P}_{K}^{1})$. For any projective space P(E) (of dimension $\ge 2)$ over a field $K$ and any sequence (a, $b, c, d)$ of four collinear points in P(E), where a, $b, c$ are distinct, the cross-ratio [a, $b, c, d]$ is defined using the projective line $\Delta$ that the points a, $b, c, d$ define. For any affine space $E$ and any sequence (a, $b, c, d)$ of four collinear points in $E$, where a, $b, c$ are distinct, the cross-ratio [a, $b, c, d]$ is defined by considering $E$ as embedded in $E$.
$$e$$
It should be noted that the definition of the cross-ratio [a, $b, c, d]$ depends on the order of the points. Thus, there could be $24 = 4$! different possible values depending on the permutation of ${a, b, c, d}$. In fact, there are at most $6$ distinct values. Also, note that [a, $b, c, d] = \infty$ iff $d = a$, [a, $b, c, d] = 0$ iff $d = b$, and [a, $b, c, d] = 1$ iff $d = c$. Thus, [a, $b, c, d] \in K -{0, 1}$ iff $d \in {/$ a, $b, c}$. The following proposition is almost obvious, but very important. It shows that projectivities between projective lines are characterized by the preservation of the cross-ratio of any four points (three of which are distinct).

> **Proposition 26.20.** Given any two projective lines $\Delta$ and $\Delta'$ , for any sequence (a, $b, c, d)$ of points in $\Delta$ and any sequence (a', b', c', d') of points in $\Delta'$ , if a, $b, c$ are distinct and a', b', c' are distinct, there is a unique projectivity $f$ : $\Delta \to \Delta'$ such that f(a) $=$ a', f(b) $=$ b', f(c) $=$ c', and f(d) $=$ d' iff [a, $b, c, d] =$ [a', b', c', d'].

*Proof.* First, assume that $f$ : $\Delta \to \Delta'$ is a projectivity such that f(a) $=$ a', f(b) $=$ b', f(c) $=$ c', and f(d) $=$ d'. Let $h: \Delta \to \mathbb{P}_{K}^{1}$ be the unique projectivity such that h(a) $= \infty$ ,
$$\mathbb{P}_{K}^{1}$$
h(b) $= 0$, and h(c) $= 1$, and let h': $\Delta' \to$  be the unique projectivity such that h'(a') $= \infty$ , h'(b') $= 0$, and h'(c') $= 1$. By definition, [a, $b, c, d] =$ h(d) and [a', b', c', d'] $=$ h'(d'). However, $h'\circ f$ : $\Delta \to \mathbb{P}_{K}^{1}$ is a projectivity such that $(h'\circ$ f)(a) $= \infty , (h'\circ$ f)(b) $= 0$, and $(h'\circ$ f)(c) $= 1$,

<!-- PAGE 929 -->
and by the uniqueness of $h$, we get $h =$ h' $\circ f$. But then, [a, $b, c, d] =$ h(d) $=$ h'(f(d)) $=$ h'(d') $=$ [a', b', c', d']. Conversely, assume that [a, $b, c, d] =$ [a', b', c', d']. Since (a, $b, c)$ and (a', b', c') are projective frames, by Proposition 26.5, there is a unique projectivity $g: \Delta \to \Delta'$ such that
$$\mathbb{P}_{K}^{1}$$
g(a) $=$ a', g(b) $=$ b', and g(c) $=$ c'. Now, h' $\circ g: \Delta \to$  is a projectivity such that (h' $\circ$ g)(a) $= \infty$ , (h' $\circ$ g)(b) $= 0$, and (h' $\circ$ g)(c) $= 1$, and thus, $h =$ h' $\circ g$. However, h'(d') $=$ [a', b', c', d'] $= [a, b, c, d] =$ h(d) $=$ h'(g(d)), and since h' is injective, we get d' $=$ g(d). As a corollary of Proposition 26.20, given any three distinct points a, $b, c$ on a projective line $\Delta$ , for every $\lambda  \in \mathbb{P}_{K}^{1}$ there is a unique point $d \in \Delta$ such that [a, $b, c, d] = \lambda$ . In order to compute explicitly the cross-ratio, we show the following easy proposition.

> **Proposition 26.21.** Given any projective line $\Delta =$ P(D), for any three distinct points a, $b, c$ in $\Delta$ , if $a =$ p(u), $b =$ p(v), and $c =$ p(u $+ v)$, where $(u, v)$ is a basis of $D$, and for any $[\lambda , \mu ]_{\sim} \in \mathbb{P}_{K}^{1}$ and any point $d \in \Delta$ , we have
$$d = p(\lambda u + \mu v)iff[a, b, c, d] = [\lambda , \mu ]_{\sim}.$$

*Proof.* If $(e_{1}, e_{2})$ is the basis of $K^{2}$ such that $e_{1} = (1, 0)$ and $e_{2} = (0, 1)$, it is obvious that $p(e_{1}) = \infty , p(e_{2}) = 0$, and $p(e_{1} + e_{2}) = 1$. Let $f$ : $D \to K^{2}$ be the bijective linear map such that f(u) $= e_{1}$ and f(v) $= e_{2}$. Then f(u $+ v) = e_{1} + e_{2}$, and thus $f$ induces the unique projectivity P(f): P(D) $\to \mathbb{P}_{K}^{1}$ such that P(f)(a) $= \infty$ , P(f)(b) $= 0$, and P(f)(c) $= 1$. Then
$$P(f)(p(\lambda u + \mu v)) = [f(\lambda u + \mu v)]_{\sim}= [\lambda e_{1} + \mu e_{2}]_{\sim}= [\lambda , \mu ]_{\sim},$$
that is,
$$d = p(\lambda u + \mu v)iff[a, b, c, d] = [\lambda , \mu ]_{\sim},$$
as claimed. We can now compute the cross-ratio explicitly for any given basis $(u, v)$ of $D$. Assume that a, $b, c, d$ have homogeneous coordinates $[\lambda_{1} , \mu_{1}$ ], $[\lambda_{2} , \mu_{2}$ ], $[\lambda_{3} , \mu_{3}$ ], and $[\lambda_{4} , \mu_{4}$ ] over the projective frame induced by $(u, v)$. Letting $w_{i} = \lambda_{i} u + \mu_{i} v$, we have $a = p(w_{1}), b = p(w_{2}), c = p(w_{3})$, and $d = p(w_{4})$. Since a and $b$ are distinct, $w_{1}$ and $w_{2}$ are linearly independent, and we can write $w_{3} = \alpha w_{1} + \beta w_{2}$ and $w_{4} = \gamma w_{1} + \delta w_{2}$, which can also be written as
$$\gamma$$
$$w_{4} =\alpha  \alpha  w_{1} + \frac{\delta}{\beta} \beta  w_{2},$$
$$and by Proposition 26.21, [a, b, c, d] = \begin{bmatrix} \gamma /\alpha , \delta /\beta \\ \alpha , \beta , \gamma , \delta \end{bmatrix} . However, since w_{1} and w_{2} are linearly$$
independent, it is possible to solve for  in terms of the homogeneous coordinates,

<!-- PAGE 930 -->
obtaining expressions involving determinants:
$$\alpha = \frac{\det(w_{3}, w_{2})}{\det(w_{1}, w_{2})} ,\beta  = \frac{\det(w_{1}, w_{3})}{\det(w_{1}, w_{2})} ,$$
$$\gamma = \frac{\det(w_{4}, w_{2})}{\det(w_{1}, w_{2})} ,\delta  = \frac{\det(w_{1}, w_{4})}{\det(w_{1}, w_{2})} ,$$
and thus, assuming that $d \neq$  a, we get
$$\lambda_{3} \lambda_{1} \lambda_{4} \lambda_{1}$$
$$,$$
$$[a, b, c, d] = \frac{\mu_{3} \mu_{1}}{\lambda_{3} \lambda_{2}} \frac{\mu_{4} \mu_{1}}{\lambda_{4} \lambda_{2}} .$$
$$\mu_{3} \mu_{2} \mu_{4} \mu_{2}$$
When $d = a$, we have [a, $b, c, d] = \infty$ . In particular, if $\Delta$ is the projective completion of an affine line $D$, then $\mu_{i}  = 1$, and we get
$$-
-$$
$$[a, b, c, d] = \frac{\lambda_{3} \lambda_{1}}{\lambda_{3}  -\lambda_{2}} \frac{\lambda_{4} \lambda_{1}}{\lambda_{4}  -\lambda_{2}} = \frac{\longrightarrow ca}{cb} \longrightarrow \frac{\longrightarrow da}{db} \longrightarrow .$$
When $d = \infty$ , we get
$$[a, b, c, \infty ] = \frac{\longrightarrow ca}{cb} \longrightarrow ,$$
which is just the usual ratio (although we defined it earlier as -ratio(a, $c, b))$. We briefly mention some of the properties of the cross-ratio. For example, the crossratio [a, $b, c, d]$ is invariant if any two elements and the complementary two elements are transposed, and letting $0^{-1} = \infty$ and $\infty^{-1} = 0$, we have
$$[a, b, c, d] = [b, a, c, d]^{-1}= [a, b, d, c]^{-1}$$
and
$$[a, b, c, d] = 1 -[a, c, b, d].$$
Since the permutations of ${a, b, c, d}$ are generated by the above transpositions, the crossratio takes at most six values. Letting $\lambda  = [a, b, c, d]$, if $\lambda  \in {\infty , 0, 1}$, then any permutation of ${a, b, c, d}$ yields a cross-ratio in ${\infty , 0, 1}$, and if $\lambda  \in {\infty / , 0, 1}$, then there are at most the six values
$$\lambda , \frac{1}{\lambda} ,1 -\lambda ,1 - \frac{1}{\lambda} , \frac{1}{1 -\lambda} , \frac{\lambda}{\lambda  -1} .$$
It can be shown that the function
$$-$$
$$\lambda  \mapsto 256 \frac{(\lambda^{2} \lambda  + 1)^{3}}{\lambda^{2} (1 -\lambda )^{2}}$$
takes a constant value on the six values listed above. We also define when four points form a harmonic division. For this, we need to assume that $K$ is not of characteristic $2$.

<!-- PAGE 931 -->

> **Definition 26.9.** Given a projective line $\Delta$ , we say that a sequence of four collinear points (a, $b, c, d)$ in $\Delta$ (where a, $b, c$ are distinct) forms a harmonic division if [a, $b, c, d] = -1$. When [a, $b, c, d] = -1$, we also say that $c$ and $d$ are harmonic conjugates of a and $b$. If a, $b, c$ are distinct collinear points in some affine space, from
$$[a, b, c, \infty ] = \frac{\longrightarrow ca}{cb} \longrightarrow ,$$
we note that $c$ is the midpoint of (a, $b)$ iff[a, $b, c, \infty$ ] $= -1$, that is, if (a, $b, c, \infty$ ) forms a harmonic division. Figure 26.22 shows a harmonic division (a, $b, c, d)$ on the real line, where the coordinates of (a, $b, c, d)$ are $(-2, 2, 1, 4)$.
$$acbd$$
$$Figure 26.22: Four points forming a harmonic division.$$
If $\Delta =\mathbb{P}_{K}^{1}$ and a, $b, c, d$ are all distinct from $\infty$ , then we see immediately from the formula
$$-
-$$
$$[a, b, c, d] = \frac{ca}{c -b} \frac{da}{d -b}$$
that [a, $b, c, d] = -1$ iff
$$2(ab + cd) = (a + b)(c + d).$$
We also check immediately that [a, $b, c, \infty$ ] $= -1$ iff
$$a + b = 2c.$$
There is a nice geometric interpretation of harmonic divisions in terms of quadrangles (or complete quadrilaterals). Consider the quadrangle (projective frame) (a, $b, c, d)$ in a projective plane, and let a' be the intersection of $\langle d, a\rangle$ and $\langle b, c\rangle$ , b' be the intersection of $\langle d, b\rangle$ and $\langle$ a, $c\rangle$ , and c' be the intersection of $\langle d, c\rangle$ and $\langle$ a, $b\rangle$ . If we let $g$ be the intersection of $\langle$ a, $b\rangle$ and $\langle$ a', $b'\rangle$ , then it is an interesting exercise to show that (a, $b, g$, c') is a harmonic division. One way to prove this is to pick (a, $c, b, d)$ as a projective frame and to compute the coordinates of a', b', c', and $g$. Then because $\langle$ a, $c\rangle$ is the line at infinity, [a, $b, g$, c'] $= [\infty , b, g$, c'], which is computed using the above formula. Another way is to send some well chosen points to infinity; see Berger $[11]$ (Chapter $6$, Section 6.4). In fact, it can be shown that the following quadruples of lines induce harmonic divisions: $(\langle c, a\rangle , \langle$ b', $a'\rangle , \langle d, b\rangle , \langle$ b', $c'\rangle$ ) on $\langle$ a, $b\rangle , (\langle b, a\rangle , \langle$ c', $a'\rangle , \langle d, c\rangle , \langle$ c', $b'\rangle$ ) on $\langle$ a, $c\rangle$ , and $(\langle b, c\rangle , \langle$ a', $c'\rangle , \langle$ a, $d\rangle , \langle$ a', $b'\rangle$ ) on $\langle c, d\rangle$ ; see Figure 26.23. For more on harmonic divisions, the interested reader should consult any text on projective geometry (for example, Berger $[11, 12]$, Samuel $[148]$, Sidler $[167]$, Tisseron $[181]$, or Pedoe $[141])$.
