# Iterated Function Systems and Fractals


<!-- PAGE 1433 -->
Chapter $38 A$ Detour On Fractals

## 38.1 Iterated Function Systems and Fractals

A pleasant application of the Hausdorffdistance and of the fixed point theorem for contracting mappings is a method for defining a class of “self-similar” fractals. For this, we can use iterated function systems.

> **Definition 38.1.** Given a metric space, $(X, d)$, an iterated function system, for short, an ifs, is a finite sequence of functions, $(f_{1}, \dots  , f_{n})$, where each $f_{i}$ : $X \to X$ is a contracting mapping. A nonempty compact subset, $K$, of $X$ is an invariant set (or attractor) for the ifs, $(f_{1}, \dots  , f_{n})$, if
$$K = f_{1}(K) \cup \cdots  \cup f_{n}(K).$$
The major result about ifs’s is the following:

> **Theorem 38.1.** If $(X, d)$ is a nonempty complete metric space, then every iterated function system, $(f_{1}, \dots  , f_{n})$, has a unique invariant set, $A$, which is a nonempty compact subset of $X$. Furthermore, for every nonempty compact subset, $A_{0}$, of $X$, this invariant set, $A$, if the limit of the sequence, $(A_{m})$, where $A_{m+1} = f_{1}(A_{m}) \cup \cdots  \cup f_{n}(A_{m})$.

*Proof.* Since $X$ is complete, by Theorem 37.55, the space $(\mathcal{K}(X), D)$ is a complete metric space. The theorem will follow from Theorem 37.54 if we can show that the map, $F$ : $\mathcal{K}(X) \to$ K(X), defined such that
$$F(K) = f_{1}(K) \cup \cdots  \cup f_{n}(K),$$
for every nonempty compact set, $K$, is a contracting mapping. Let $A, B$ be any two nonempty compact subsets of $X$ and consider any $\eta  \ge$ D(A, $B)$. Since each $f_{i}$ : $X \to X$ is a contracting mapping, there is some $\lambda_{i}$ , with $0 \le \lambda_{i}  < 1$, such that
$$d(f_{i}(a), f_{i}(b)) \le \lambda_{i} d(a, b),$$
$$1433$$

<!-- PAGE 1434 -->
for all a, $b \in X$. Let $\lambda  = max{\lambda_{1} , \dots  , \lambda_{n}$ }. We claim that
$$D(F(A), F(B)) \le \lambda D(A, B).$$
For any $x \in$ F(A) $= f_{1}(A)\cup \cdots \cup f_{n}(A)$, there is some $a_{i} \in A_{i}$ such that $x = f_{i}(a_{i})$ and since $\eta  \ge$ D(A, $B)$, there is some $b_{i} \in B$ such that
$$d(a_{i}, b_{i}) \le \eta ,$$
and thus,
$$d(x, f_{i}(b_{i})) = d(f_{i}(a_{i}), f_{i}(b_{i})) \le \lambda_{i} d(a_{i}, b_{i}) \le \lambda \eta .$$
This show that
$$F(A) \subseteq V_{\lambda \eta}(F(B)).$$
Similarly, we can prove that
$$F(B) \subseteq V_{\lambda \eta}(F(A)),$$
and since this holds for all $\eta  \ge$ D(A, $B)$, we proved that
$$D(F(A), F(B)) \le \lambda D(A, B)$$
where $\lambda  = max{\lambda_{1} , \dots  , \lambda_{n}$ }. Since $0 \le \lambda_{i}  < 1$, we have $0 \le \lambda  < 1$ and $F$ is indeed a contracting mapping. Theorem 38.1 justifies the existence of many familiar “self-similar” fractals. One of the best known fractals is the Sierpinski gasket.

> **Example 38.1.** Consider an equilateral triangle with vertices a, $b, c$, and let $f_{1}, f_{2}, f_{3}$ be the dilatations of centers a, $b, c$ and ratio $1/2$. The Sierpinski gasket is the invariant set of the ifs $(f_{1}, f_{2}, f_{3})$. The dilations $f_{1}, f_{2}, f_{3}$ can be defined explicitly as follows, assuming that
$$\sqrt$$
$a = (-1/2, 0), b = (1/2, 0)$, and $c = (0, \overline{3}/2)$. The contractions $f_{1}, f_{2}, f_{3}$ are specified by
$$x'= \frac{1}{2} x - \frac{1}{4} ,$$
$$y'= \frac{1}{2} y,$$
$$x'= \frac{1}{2} x + \frac{1}{4} ,$$
$$y'= \frac{1}{2} y,$$
and
$$x'= \frac{1}{2} x,$$
$$y'= \frac{1}{2} y + \frac{\sqrt{3}}{4} .$$

<!-- PAGE 1435 -->
$$Figure 38.1: The Sierpinski gasket$$
We wrote a Mathematica program that iterates any finite number of affine maps on any input figure consisting of combinations of points, line segments, and polygons (with their interior points). Starting with the edges of the triangle a, $b, c$, after $6$ iterations, we get the picture shown in Figure 38.1. It is amusing that the same fractal is obtained no matter what the initial nonempty compact figure is. It is interesting to see what happens if we start with a solid triangle (with its interior points). The result after $6$ iterations is shown in Figure 38.2. The convergence towards the Sierpinski gasket is very fast. Incidently, there are many other ways of defining the Sierpinski gasket. A nice variation on the theme of the Sierpinski gasket is the Sierpinski dragon.

> **Example 38.2.** The Sierpinski dragon is specified by the following three contractions:
$$x'=- \frac{1}{4} x - \frac{\sqrt{3}}{4} y + \frac{3}{4} ,$$
$$y'= \frac{\sqrt3}{4} x - \frac{1}{4} y + \frac{\sqrt3}{4} ,$$
$$x'=- \frac{1}{4\sqrt} x + \frac{\sqrt{3}}{4} y - \frac{3}{4\sqrt} ,$$
$$y'=- \frac{\overline{3}}{4} x - \frac{1}{4} y + \frac{\overline{3}}{4} ,$$
$$x'= \frac{1}{2} x,$$
$$y'= \frac{1}{2} y + \frac{\sqrt{3}}{2} .$$

<!-- PAGE 1436 -->
$$Figure 38.2: The Sierpinski gasket, version 2$$
The result of $7$ iterations starting from the line segment $(-1, 0), (1, 0))$, is shown in Figure 38.3. This curve converges to the boundary of the Sierpinski gasket. A different kind of fractal is the Heighway dragon.

> **Example 38.3.** The Heighway dragon is specified by the following two contractions:
$$x'= \frac{1}{2} x - \frac{1}{2} y,$$
$$y'= \frac{1}{2} x + \frac{1}{2} y,$$
$$x'=- \frac{1}{2} x - \frac{1}{2} y,$$
$$y'= \frac{1}{2} x - \frac{1}{2} y + 1.$$
It can be shown that for any number of iterations, the polygon does not cross itself. This means that no edge is traversed twice and that if a point is traversed twice, then this point is the endpoint of some edge. The result of $13$ iterations, starting with the line segment $((0, 0), (0, 1))$, is shown in Figure 38.4. The Heighway dragon turns out to fill a closed and bounded set. It can also be shown that the plane can be tiled with copies of the Heighway dragon. Another well known example is the Koch curve.

<!-- PAGE 1437 -->
$$Figure 38.3: The Sierpinski dragon$$
$$Figure 38.4: The Heighway dragon$$

<!-- PAGE 1438 -->
$$Figure 38.5: The Koch curve$$

> **Example 38.4.** The Koch curve is specified by the following four contractions:
$$x'= \frac{1}{3} x - \frac{2}{3} ,$$
$$y'= \frac{1}{3} y,$$
$$x'= \frac{1}{\sqrt6} x - \frac{\sqrt{3}}{6} y - \frac{1}{\sqrt6} ,$$
$$y'= \frac{\overline{3}}{6} x + \frac{1}{6} y + \frac{\overline{3}}{6} ,$$
$$x'= \frac{1}{6} x + \frac{\sqrt{3}}{6} y + \frac{1}{6} ,$$
$$y'=- \frac{\sqrt{3}}{6} x + \frac{1}{6} y + \frac{\sqrt{3}}{6} ,$$
$$x'= \frac{1}{3} x + \frac{2}{3} ,$$
$$y'= \frac{1}{3} y.$$
The Koch curve is an example of a continuous curve which is nowhere differentiable (because it “wiggles” too much). It is a curve of infinite length. The result of $6$ iterations, starting with the line segment $((-1, 0), (1, 0))$, is shown in Figure 38.5. The curve obtained by putting three Kock curves together on the sides of an equilateral triangle is known as the snowflake curve (for obvious reasons, see below!).

<!-- PAGE 1439 -->
$$Figure 38.6: The snowflake curve$$

> **Example 38.5.** The snowflake curve obtained after $5$ iterations is shown in Figure 38.6. The snowflake curve is an example of a closed curve of infinite length bounding a finite area. We conclude with another famous example, a variant of the Hilbert curve.

> **Example 38.6.** This version of the Hilbert curve is defined by the following four contractions:
$$x'= \frac{1}{2} x - \frac{1}{2} ,$$
$$y'= \frac{1}{2} y + 1,$$
$$x'= \frac{1}{2} x + \frac{1}{2} ,$$
$$y'= \frac{1}{2} y + 1,$$
$$x'=- \frac{1}{2} y + 1,$$
$$y'= \frac{1}{2} x + \frac{1}{2} ,$$
$$x'= \frac{1}{2} y -1,$$
$$y'=- \frac{1}{2} x + \frac{1}{2} .$$

<!-- PAGE 1440 -->
$$Figure 38.7: A Hilbert curve$$
This continuous curve is a space-filling curve, in the sense that its image is the entire unit square. The result of $6$ iterations, starting with the two lines segments $((-1, 0), (0, 1))$ and $((0, 1), (1, 0))$, is shown in Figure 38.7. For more on iterated function systems and fractals, we recommend Edgar $[56]$.
