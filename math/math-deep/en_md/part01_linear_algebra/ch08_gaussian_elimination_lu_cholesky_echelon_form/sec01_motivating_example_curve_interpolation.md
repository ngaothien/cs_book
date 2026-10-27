# Motivating Example: Curve Interpolation


<!-- PAGE 257 -->
Chapter $8$ Gaussian Elimination, $LU$ -Factorization, Cholesky Factorization, Reduced Row Echelon Form In this chapter we assume that all vector spaces are over the field $\mathbb{R}$. All results that do not rely on the ordering on $\mathbb{R}$ or on taking square roots hold for arbitrary fields.

## 8.1 Motivating Example: Curve Interpolation

Curve interpolation is a problem that arises frequently in computer graphics and in robotics (path planning). There are many ways of tackling this problem and in this section we will describe a solution using cubic splines. Such splines consist of cubic B´ezier curves. They are often used because they are cheap to implement and give more flexibility than quadratic B´ezier curves.
$$\mathbb{R}^{2}  \mathbb{R}^{3}$$
A cubic B´ezier curve C(t) (in or ) is specified by a list of four control points $(b_{0}, b_{1}, b_{2}, b_{3})$ and is given parametrically by the equation
$$C(t) = (1 -t)^{3}b_{0} + 3(1 -t)^{2}t b_{1} + 3(1 -t)t^{2}b_{2} + t^{3}b_{3}.$$
Clearly, C(0) $= b_{0}$, C(1) $= b_{3}$, and for $t \in [0, 1]$, the point C(t) belongs to the convex hull of the control points $b_{0}, b_{1}, b_{2}, b_{3}$. The polynomials
$$(1 -t)^{3},3(1 -t)^{2}t,3(1 -t)t^{2},t^{3}$$
are the Bernstein polynomials of degree $3$. Typically, we are only interested in the curve segment corresponding to the values of $t$ in the interval $[0, 1]$. Still, the placement of the control points drastically affects the shape of the curve segment, which can even have a self-intersection; See Figures 8.1, 8.2, 8.3 illustrating various configurations.
$$257$$

<!-- PAGE 258 -->
$$b$$
$$1$$
$$b$$
$$2$$
$$bb$$
$$03$$
$$Figure 8.1: A “standard” B´ezier curve.$$
$$b$$
$$1$$
$$b$$
$$3$$
$$b$$
$$0$$
$$b$$
$$2$$
$$Figure 8.2: A B´ezier curve with an inflection point.$$

<!-- PAGE 259 -->
$$bb$$
$$21$$
$$bb$$
$$03$$
$$Figure 8.3: A self-intersecting B´ezier curve.$$
Interpolation problems require finding curves passing through some given data points and possibly satisfying some extra constraints. A B´ezier spline curve $F$ is a curve which is made up of curve segments which are B´ezier curves, say $C_{1}, \dots  , C_{m} (m \ge 2)$. We will assume that $F$ defined on $[0, m]$, so that for $i = 1, \dots  , m$,
$$F(t) = C_{i}(t -i + 1),i -1 \le t \le i.$$
Typically, some smoothness is required between any two junction points, that is, between any two points $C_{i}(1)$ and $C_{i+1}(0)$, for $i = 1, \dots  , m$ - $1$. We require that $C_{i}(1) = C_{i+1}(0) (C^{0}-continuity)$, and typically that the derivatives of $C_{i}$ at $1$ and of $C_{i+1}$ at $0$ agree up to second order derivatives. This is called $C^{2}-continuity$, and it ensures that the tangents agree as well as the curvatures. There are a number of interpolation problems, and we consider one of the most common problems which can be stated as follows: Problem: Given $N + 1$ data points $x_{0}, \dots  , x_{N}$, find a $C^{2}$ cubic spline curve $F$ such that F(i) $= x_{i}$ for all $i, 0 \le i \le N (N \ge 2)$. A way to solve this problem is to find $N + 3$ auxiliary points $d_{-1}, \dots  , d_{N+1}$, called de Boor control points, from which $N$ B´ezier curves can be found. Actually,
$$d_{-1} = x_{0}andd_{N+1} = x_{N}$$

<!-- PAGE 260 -->
so we only need to find $N + 1$ points $d_{0}, \dots  , d_{N}$. It turns out that the $C^{2}-continuity$ constraints on the $N$ B´ezier curves yield only $N$ - $1$ equations, so $d_{0}$ and $d_{N}$ can be chosen arbitrarily. In practice, $d_{0}$ and $d_{N}$ are chosen according to various end conditions, such as prescribed velocities at $x_{0}$ and $x_{N}$. For the time being, we will assume that $d_{0}$ and $d_{N}$ are given. Figure 8.4 illustrates an interpolation problem involving $N + 1 = 7 + 1 = 8$ data points. The control points $d_{0}$ and $d_{7}$ were chosen arbitrarily.
$$d_{2}$$
$$d_{1}$$
$$x_{2}$$
$$d_{7}$$
$$x_{1}$$
$$d_{3}$$
$$x_{3}$$
$d_{0} d_{6}$
$$x_{6}$$
$$x_{4}$$
$$x_{5}$$
$$d_{4}$$
$$d_{5}$$
$x_{0} = d_{-1} x_{7} = d_{8}$

![Figure 8.4](../../assets/ch08/fig_8_4.png)

**Figure 8.4:** A $C^{2}$ cubic interpolation spline curve passing through the points $x_{0}, x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{6}, x_{7}$. It can be shown that $d_{1}, \dots  , d_{N-1}$ are given by the linear system
$$\begin{pmatrix} 7 & 1 \\ 1\overline{2} & 4 & 1 & 0 \\ \ddots & \ddots & \ddots \\ 0 & 1 & 4 & 1 \\ 1 & 7 \end{pmatrix} \begin{pmatrix} d_{1} \\ d_{2} \\ \vdots \\ d_{N-2} \\ d_{N-1} \end{pmatrix} = \begin{pmatrix} 6x_{1} -^{3}d_{0} \\ 6x_{2}^{2} \\ \vdots \\ 6x_{N-2} \\ 6x_{N-1} & d_{N} \end{pmatrix} .$$
$$-_{2}^{3}$$
$$\overline{2}$$
We will show later that the above matrix is invertible because it is strictly diagonally dominant.
