# Finding a Homography Between Two Projective Frames


<!-- PAGE 904 -->
$$RP2$$
$$D‘D$$
$$a$$
$$Ob$$
$$a’$$
$$cx*$$
$$\overline{b’}$$
$$x*$$
$$D’D$$
$$b$$
$$a$$
$$O$$
$$a’ = f(a)b’ = f(b)$$
$$c$$

![Figure 26.12](../../assets/ch26/fig_26_12.png)

**Figure 26.12:** An illustration of the perspectivity construction of Proposition 26.6. h(d) $= d$. Thus by Proposition 26.6, the projectivity $h: \langle$ a, $a'\rangle \to \langle c, c'\rangle$ is a perspectivity. Since
$$h(a)=g(f(a)) = g(b) = c,$$
$$h(a')=g(f(a')) = g(b') = c',$$
the intersection $q$ of $\langle$ a, $c\rangle$ and $\langle$ a', $c'\rangle$ is the center of the perspectivity $h$. Also note that the point $m = \langle$ a, $a'\rangle \cap \langle p, r\rangle$ and its image h(m) are both on the line $\langle p, r\rangle$ , since $r$ is the center of $f$ and $p$ is the center of $g$. Since $h$ is a perspectivity of center $q$, the line $\langle m, h(m)\rangle = \langle p, r\rangle$ passes through $q$, which proves the proposition. Desargues’s theorem is illustrated in Figure 26.13. It can also be shown that every projectivity between two distinct lines is the composition of two perspectivities (not in a unique way). An elegant proof of Pappus’s theorem can also be given using perspectivities.

## 26.6 Finding a Homography Between Two Projective

$$Frames$$
In this section we present a method for finding the matrix (up to a scalar) of the unique homography (bijective projective transformation) mapping one projective frame to an other projective frame. This problem arises notably in computer vision in the context of image morphing. We begin with the simple case of two nondegenerate quadrilatrerals $([p_{1}], [p_{2}], [p_{3}], [p_{4}])$ and $[(q_{1}], [q_{2}], [q_{3}], [q_{4}])$ in $\mathbb{RP}^{2}$, that is, two projective frames, which means that $(p_{1}, p_{2}, p_{3})$

<!-- PAGE 905 -->
$$q$$
$$a'$$
$$ap$$
$$d \frac{bb'}{c}$$
$$c'$$
$$r$$
$$Figure 26.13: Desargues’s theorem (projective version in the plane).$$
and $(q_{1}, q_{2}, q_{3})$ are linearly independent, and that if we write
$$p_{4} = \alpha_{1} p_{1} + \alpha_{2} p_{2} + \alpha_{3} p_{3}$$
and
$$q_{4} = \lambda_{1} q_{1} + \lambda_{2} q_{2} + \lambda_{3} q_{3},$$
for some unique scalars $\alpha_{1} , \alpha_{2} , \alpha_{3}$  and $\lambda_{1} , \lambda_{2} , \lambda_{3}$ , then $\alpha_{i}  \neq  0$ and $\lambda_{i}  \neq  0$ for $i = 1, 2, 3$. The problem is to find the $3 \times  3$ matrix (up to a scalar) representing the unique homography $h$ mapping $[p_{i}]$ to $[q_{i}]$ for $i = 1, 2, 3, 4$. We will use the canonical basis $\mathcal{E} = (e_{1}, e_{2}, e_{3})$ of $\mathbb{R}^{3}$, with $e_{1} = (1, 0, 0), e_{2} = (0, 1, 0), e_{3} = (0, 0, 1)$, and the bases $\mathcal{P} = (p_{1}, p_{2}, p_{3})$ and $\mathcal{Q} = (q_{1}, q_{2}, q_{3})$ of $\mathbb{R}^{3}$. As a first step, it is convenient to express $(q_{1}, q_{2}, q_{3}, q_{4})$ over the $basis\mathcal{P} = (p_{1}, p_{2}, p_{3})$, with $q_{1} = (x_{1}, y_{1}, z_{1}), q_{2} = (x_{2}, y_{2}, z_{2}), q_{3} = (x_{3}, y_{3}, z_{3}), q_{4} = (x_{4}, y_{4}, z_{4})$. Over the canonical basis $\mathcal{E}$, the points $(p_{1}, p_{2}, p_{3}, p_{4})$ are given by the coordinates $p_{1} = (p_{1}^{x}, p_{1}^{y}, p_{1}^{z}), p_{2} = (p_{2}^{x}, p_{2}^{y}, p_{2}^{z}), p_{3} = (p_{3}^{x}, p_{3}^{y}, p_{3}^{z}), p_{4} = (p_{4}^{x}, p_{4}^{y}, p_{4}^{z})$, and similarly, the points $(q_{1}, q_{2}, q_{3}, q_{4})$ are given by the coordinates $q_{1} = (q_{1}^{x}, q_{1}^{y}, q_{1}^{z}), q_{2} = (q_{2}^{x}, q_{2}^{y}, q_{2}^{z}), q_{3} = (q_{3}^{x}, q_{3}^{y}, q_{3}^{z}), q_{4} = (q_{4}^{x}, q_{4}^{y}, q_{4}^{z})$.

<!-- PAGE 906 -->

> **Proposition 26.8.** With respect to the basis $\mathcal{P} = (p_{1}, p_{2}, p_{3})$, the matrix $A_{P}$ of the unique
$$\mathbb{RP}^{2}$$
homography $h$ of mapping the projective frame $([p_{1}], [p_{2}], [p_{3}], [p_{4}])$ to the projective frame $[(q_{1}], [q_{2}], [q_{3}], [q_{4}])$ is given by
$$A_{P} = \begin{pmatrix} x_{1} & x_{2} & x_{3} \\ y_{1} & y_{2} & y_{3} \\ z_{1} & z_{2} & z_{3} \end{pmatrix} \begin{pmatrix} \lambda \overline{1} & 0 & 0 \\ \overline{\alpha}\overline{1} \\ 0 & \lambda \overline{2} & 0 \\ \overline{\alpha}\overline{2} \\ 0 & 0 & \lambda \overline{3} \end{pmatrix} .$$
$$\overline{\alpha}\overline{3}$$

*Proof.* Let $u_{1} = \alpha_{1} p_{1}, u_{2} = \alpha_{2} p_{2}, u_{3} = \alpha_{3} p_{3}$, and let $v_{1} = \lambda_{1} q_{1}, v_{2} = \lambda_{2} q_{2}, v_{3} = \lambda_{3} q_{3}$, so that
$$p_{4} = u_{1} + u_{2} + u_{3}$$
and
$$q_{4} = v_{1} + v_{2} + v_{3}.$$
Because $p_{1}, p_{2}, p_{3}$ are linearly independent and since $\alpha_{i}$  ̸ $= 0$ for $i = 1, 2, 3$, the vectors
$$\mathbb{R}^{3} \mathbb{R}^{3}$$
$(u_{1}, u_{2}, u_{2})$ are also linearly independent, so there is a unique linear map $f$ : $\to$ , such that
$$f(u_{i}) = v_{i}i = 1, \dots  , 3,$$
and by linearity
$$f(p_{4}) = f(u_{1} + u_{2} + u_{3}) = f(u_{1}) + f(u_{2}) + f(u_{3}) = v_{1} + v_{2} + v_{3} = q_{4}.$$
With respect to the basis $\mathcal{P} = (p_{1}, p_{2}, p_{3})$, we have
$$f(p_{i}) = \frac{1}{\alpha_{i}} v_{i} = \frac{\lambda_{i}}{\alpha_{i}} q_{i},i = 1, \dots  , 3,$$
so with respect to the basis $\mathcal{P}$, the matrix of $f$ is
$$A_{P} = \begin{pmatrix} \lambda \overline{1} x_{1\alpha}^{\lambda2}x_{2\alpha}^{\lambda3}x_{3} \\ \overline{\alpha}\overline{1} & \overline{2} & \overline{3} \\ \lambda \overline{1} y_{1} & \lambda \overline{2} y_{2} & \lambda \overline{3} y_{3} \\ \overline{\alpha}\overline{1} & \overline{\alpha}\overline{2} & \overline{\alpha}\overline{3} \\ \lambda \overline{1} z_{1} & \lambda \overline{2} z_{2} & \lambda \overline{3} z_{3} \end{pmatrix} = \begin{pmatrix} x_{1} & x_{2} & x_{3} \\ y_{1} & y_{2} & y_{3} \\ z_{1} & z_{2} & z_{3} \end{pmatrix} \begin{pmatrix} \lambda \overline{1} & 0 & 0 \\ \overline{\alpha}\overline{1} \\ 0 & \lambda \overline{2} & 0 \\ \overline{\alpha}\overline{2} \\ 0 & 0 & \lambda \overline{3} \end{pmatrix} ,$$
$$\overline{\alpha}\overline{1}\overline{\alpha}\overline{2}\overline{\alpha}\overline{3}\overline{\alpha}\overline{3}$$
as claimed. If we assume that we pick the coordinates of $(p_{1}, p_{2}, p_{3}, p_{4})$ and $(q_{1}, q_{2}, q_{3}, q_{4})$ with respect to the canonical basis $\mathcal{E}$, then the coordinates $\alpha_{1} , \alpha_{2} , \alpha_{3}$  and $\lambda_{1} , \lambda_{2} , \lambda_{3}$  are solutions of the systems
$$\begin{pmatrix} p_{1}^{x} & p_{2}^{x} & p_{3}^{x} \\ p_{1}^{y} & p_{2}^{y} & p_{3}^{y} \\ p_{1}^{z} & p_{2}^{z} & p_{3}^{z} \end{pmatrix} \begin{pmatrix} \alpha_{1} \\ \alpha_{2} \\ \alpha_{3} \end{pmatrix} = \begin{pmatrix} p_{4}^{x} \\ p_{4}^{y} \\ p_{4}^{z} \end{pmatrix}$$

<!-- PAGE 907 -->
and
$$\begin{pmatrix} q_{1}^{x} & q_{2}^{x} & q_{3}^{x} \\ q_{1}^{y} & q_{2}^{y} & q_{3}^{y} \\ q_{1}^{z} & q_{2}^{z} & q_{3}^{z} \end{pmatrix} \begin{pmatrix} \lambda_{1} \\ \lambda_{2} \\ \lambda_{3} \end{pmatrix} = \begin{pmatrix} q_{4}^{x} \\ q_{4}^{y} \\ q_{4}^{z} \end{pmatrix} ,$$
and the matrix $A_{E}$ of our linear map $f$ with respect to the canonical basis is determined as follows.

> **Proposition 26.9.** With respect to the canonical basis $\mathcal{E} = (e_{1}, e_{2}, e_{3})$, the matrix $A_{E}$ of
$$\mathbb{RP}^{2}$$
the unique homography $h$ of mapping the projective frame $([p_{1}], [p_{2}], [p_{3}], [p_{4}])$ to the projective frame $[(q_{1}], [q_{2}], [q_{3}], [q_{4}])$ is given by
$$p_{3}^{x-1}$$
$$A_{E} = \begin{pmatrix} q_{1}^{x} & q_{2}^{x} & q_{3}^{x} \\ q_{1}^{y} & q_{2}^{y} & q_{3}^{y} \\ q_{1}^{z} & q_{2}^{z} & q_{3}^{z} \end{pmatrix} \begin{pmatrix} \lambda \overline{1} & 0 & 0 \\ \overline{\alpha}\overline{1} \\ 0 & \lambda \overline{2} & 0 \\ \overline{\alpha}\overline{2} \\ 0 & 0 & \lambda \overline{3} \end{pmatrix} \begin{pmatrix} p_{1}^{x} & p_{2}^{x} \\ p_{1}^{y} & p_{2}^{y} & p_{3}^{y} \\ p_{1}^{z} & p_{2}^{z} & p_{3}^{z} \end{pmatrix} .$$
$$\overline{\alpha}\overline{3}$$
$$\mathbb{R}^{3} \mathbb{R}^{3}$$

*Proof.* Since $f$ : $\to$ is the unique linear map given by
$$f(u_{i}) = v_{i},i = 1, \dots  , 3,$$
$$\mathbb{R}^{3} \mathbb{R}^{3}$$
the map $f$ : $\to$ is equal to the composition
$$f = f_{Q} \circ g,$$
$$\mathbb{R}^{3} \mathbb{R}^{3}$$
where $g: \to$ is the unique linear map given by
$$g(u_{i}) = e_{i},i = 1, \dots  , 3,$$
$$\mathbb{R}^{3} \mathbb{R}^{3}$$
and $f_{Q}$ : $\to$ is the unique linear map given by
$$f_{Q}(e_{i}) = v_{i},i = 1, \dots  , 3.$$
$$\mathbb{R}^{3} \mathbb{R}^{3}  \mathbb{R}^{3} \mathbb{R}^{3}$$
However, $g: \to$ is the inverse of the unique linear map $f_{P}$ : $\to$ given by
$$f_{P}(e_{i}) = u_{i},i = 1, \dots  , 3,$$
so
$$f = f_{Q} \circ f_{P}^{-1}  .$$
The matrix $B_{P}$ representing $f_{P}$ over the canonical basis $\mathcal{E}$ is
$$B_{P} = \begin{pmatrix} \alpha_{1} p_{1}^{x} & \alpha_{2} p_{2}^{x} & \alpha_{3} p_{3}^{x} \\ \alpha_{1} p_{1}^{y} & \alpha_{2} p_{2}^{y} & \alpha_{3} p_{3}^{y} \\ \alpha_{1} p_{1}^{z} & \alpha_{2} p_{2}^{z} & \alpha_{3} p_{3}^{z} \end{pmatrix} = \begin{pmatrix} p_{1}^{x} & p_{2}^{x} & p_{3}^{x} \\ p_{1}^{y} & p_{2}^{y} & p_{3}^{y} \\ p_{1}^{z} & p_{2}^{z} & p_{3}^{z} \end{pmatrix} \begin{pmatrix} \alpha_{1} & 0 & 0 \\ 0 & \alpha_{2} & 0 \\ 0 & 0 & \alpha_{3} \end{pmatrix} ,$$

<!-- PAGE 908 -->
and similarly the matrix $B_{Q}$ representing $f_{Q}$ over $\mathcal{E}$ is
$$B_{Q} = \begin{pmatrix} \lambda_{1} q_{1}^{x} & \lambda_{2} q_{2}^{x} & \lambda_{3} q_{3}^{x} \\ \lambda_{1} q_{1}^{y} & \lambda_{2} q_{2}^{y} & \lambda_{3} q_{3}^{y} \\ \lambda_{1} q_{1}^{z} & \lambda_{2} q_{2}^{z} & \lambda_{3} q_{3}^{z} \end{pmatrix} = \begin{pmatrix} q_{1}^{x} & q_{2}^{x} & q_{3}^{x} \\ q_{1}^{y} & q_{2}^{y} & q_{3}^{y} \\ q_{1}^{z} & q_{2}^{z} & q_{3}^{z} \end{pmatrix} \begin{pmatrix} \lambda_{1} & 0 & 0 \\ 0 & \lambda_{2} & 0 \\ 0 & 0 & \lambda_{3} \end{pmatrix} ,$$
and we have
$$A_{E} = B_{Q}B_{P}^{-1} .$$
Therefore, we have
$$p_{3}^{x-1}$$
$$A_{E} = \begin{pmatrix} q_{1}^{x} & q_{2}^{x} & q_{3}^{x} \\ q_{1}^{y} & q_{2}^{y} & q_{3}^{y} \\ q_{1}^{z} & q_{2}^{z} & q_{3}^{z} \end{pmatrix} \begin{pmatrix} \lambda \overline{1} & 0 & 0 \\ \overline{\alpha}\overline{1} \\ 0 & \lambda \overline{2} & 0 \\ \overline{\alpha}\overline{2} \\ 0 & 0 & \lambda \overline{3} \end{pmatrix} \begin{pmatrix} p_{1}^{x} & p_{2}^{x} \\ p_{1}^{y} & p_{2}^{y} & p_{3}^{y} \\ p_{1}^{z} & p_{2}^{z} & p_{3}^{z} \end{pmatrix} ,$$
$$\overline{\alpha}\overline{3}$$
as claimed The above method generalizes immediately to any dimension (and any field $K)$. If $([p_{1}], \dots  , [p_{n+1}], [p_{n+2}])$ and $[(q_{1}], \dots  , [q_{n+1}], [q_{n+2}])$ are any two projective frames in a projective space $\mathbb{P}(E)$ where $E$ is a $K$-vector space of dimension $n + 1$, then $(p_{1}, \dots  , p_{n+1})$ is a basis of $E$ denoted by $\mathcal{P}$ and $(q_{1}, \dots  , q_{n+1})$ is a basis of $E$ denoted $\mathcal{Q}$, and we can write
$$p_{n+2} = \alpha_{1} p_{1} + \cdots  + \alpha_{n+1} p_{n+1}$$
$$q_{n+2} = \lambda_{1} q_{1} + \cdots  + \lambda_{n+1} q_{n+1}$$
for some unique $\alpha_{i} , \lambda_{i}  \in K$ such that $\alpha_{i}  \neq  0$ and $\lambda_{i}  \neq  0$ for $i = 1, \dots  , n + 1$. If we assume that $E = K^{n+1}$, then the canonical basis is $\mathcal{E} = (e_{1}, \dots  , e_{n+1})$. If we express the coordinates of the $q_{j}$ over the basis $\mathcal{P}$ by
$$q_{j} = (x_{j}^{1}, \dots  , x_{j}^{n} , x_{j}^{n+1}),j = 1, \dots  , n + 2,$$
then we have the following proposition.

> **Proposition 26.10.** With respect to the basis $\mathcal{P} = (p_{1}, \dots  , p_{n+1})$, the matrix $A_{P}$ of the unique homography $h$ of $\mathbb{P}(E)$ where $E$ is a $K$-vector space of dimension $n + 1$, mapping the projective frame $([p_{1}], \dots  , [p_{n+1}], [p_{n+2}])$ to the projective frame $[(q_{1}], \dots  , [q_{n+1}], [q_{n+2}])$ is given by
$$A_{P} = \begin{pmatrix} x_{1}^{1} & \dots & x_{n}^{1} & x_{n+1}^{1} \\ \vdots & \ddots & \vdots & \vdots \\ x_{1}^{n} & \dots & x_{n}^{n} & x_{+1}^{n} \\ x_{1}^{n+1} & \dots & x_{n}^{n+1} & x_{n+1}^{nn+1} \end{pmatrix} \begin{pmatrix} \lambda \overline{1} & \dots & 0 & 0 \\ \overline{\alpha}\vdots & \ddots & \vdots & \vdots \\ 0 & \dots_{\alpha}^{\lambda n} & 0 \\ 0 & \dots & 0^{n} & \lambda n+1 \end{pmatrix} .$$
$$\overline{\alpha}\overline{n}\overline{+1}$$

<!-- PAGE 909 -->
If we express the coordinates of the vectors $p_{i}$ and $q_{i}$ over the canonical basis as
$$p_{i} = (p_{i}^{1} , \dots  , p_{i}^{n} , p_{i}^{n+1}),q_{i} = (q_{i}^{1} , \dots  , q_{i}^{n} , q_{i}^{n+1}),i = 1, \dots  , n + 2,$$
then we have the following result.

> **Proposition 26.11.** With respect to the canonical $basis\mathcal{E} = (e_{1}, \dots  , e_{n+1})$, the matrix $A_{E}$ of the unique homography $h$ of $\mathbb{P}(E)$ where $E$ is a $K$-vector space of dimension $n + 1$, mapping the projective frame $([p_{1}], \dots  , [p_{n+1}], [p_{n+2}])$ to the projective frame $[(q_{1}], \dots  , [q_{n+1}], [q_{n+2}])$ is given by
$$A_{E} = \begin{pmatrix} q_{1}^{1} & \dots & q_{n}^{1} & q_{n+1}^{1} \\ \vdots & \ddots & \vdots & \vdots \\ q_{1}^{n} & \dots & q_{n}^{n} & q_{n+1}^{n} \\ q_{1}^{n+1} & \dots & q_{n}^{n+1} & q_{n+1}^{n+1} \end{pmatrix} \begin{pmatrix} \lambda \overline{1} & \dots & 0 & 0 \\ \overline{\alpha}\vdots & \ddots & \vdots & \vdots \\ 0 & \dots_{\alpha}^{\lambda n} & 0 \\ 0 & \dots & 0^{n} & \lambda n+1 \end{pmatrix} \begin{pmatrix} p_{1}^{1} & \dots & p_{n}^{1} & p_{n+1}^{1-1} \\ \vdots & \ddots & \vdots & \vdots \\ p_{1}^{n} & \dots & p_{n}^{n} & p_{n+1}^{n} \\ p_{1}^{n+1} & \dots & p_{n}^{n+1} & p_{n+1}^{n+1} \end{pmatrix} ,$$
$$\overline{\alpha}\overline{n}\overline{+1}$$
where $(\alpha_{1} , \dots  , \alpha_{n+1}$ ) and $(\lambda_{1} , \dots  , \lambda_{n+1}$ ) are the solutions of the systems
$$\begin{pmatrix} p_{1}^{1} & \dots & p_{n}^{1} & p_{n+1}^{1} \\ \vdots & \ddots & \vdots & \vdots \\ p_{1}^{n} & \dots & p_{n}^{n} & p_{n+1}^{n} \\ p_{1}^{n+1} & \dots & p_{n}^{n+1} & p_{n+1}^{n+1} \end{pmatrix} \begin{pmatrix} \alpha_{1} \\ \vdots \\ \alpha_{n} \\ \alpha_{n+1} \end{pmatrix} = \begin{pmatrix} p_{n+2}^{1} \\ \vdots \\ p_{n+2}^{n} \\ p_{n+2}^{n+1} \end{pmatrix}$$
and
$$\begin{pmatrix} q_{1}^{1} & \dots & q_{n}^{1} & q_{n+1}^{1} \\ \vdots & \ddots & \vdots & \vdots \\ q_{1}^{n} & \dots & q_{n}^{n} & q_{n+1}^{n} \\ q_{1}^{n+1} & \dots & q_{n}^{n+1} & q_{n+1}^{n+1} \end{pmatrix} \begin{pmatrix} \lambda_{1} \\ \vdots \\ \lambda_{n} \\ \lambda_{n+1} \end{pmatrix} = \begin{pmatrix} q_{n+2}^{1} \\ \vdots \\ q_{n+2}^{n} \\ q_{n+2}^{n+1} \end{pmatrix} .$$
We now consider the special case where the points $([p_{1}], [p_{2}], [p_{3}], [p_{4}])$ belong to the affine
$$\mathbb{RP}^{2}$$
patch of corresponding to the plane $H$ of equation $z = 1$. In this case, we may identify $[p_{i}]$ with $p_{i}$, which has coordinates $(p^{i}, p_{i}^{y} , 1)$ with respect to the canonical basis (the $p_{i}s$ are not points at infinity; points at infinity are of of form $(x, y, 0))$. Then, the barycentric coordinates $\alpha_{1} , \alpha_{2} , \alpha_{3}$  of $p_{4}$ are solutions of the systems
$$\begin{pmatrix} p_{1}^{x} & p_{2}^{x} & p_{3}^{x} \\ p_{1}^{y} & p_{2}^{y} & p_{3}^{y} \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} \alpha_{1} \\ \alpha_{2} \\ \alpha_{3} \end{pmatrix} = \begin{pmatrix} p_{4}^{x} \\ p_{4}^{y} \\ 1 \end{pmatrix} .$$
By Proposition 26.9, we obtain the following result.

> **Proposition 26.12.** With respect to the canonical basis $\mathcal{E} = (e_{1}, e_{2}, e_{3})$, the matrix $A_{E}$ of
$$\mathbb{RP}^{2}$$
the unique homography $h$ of mapping $(p_{1}, p_{2}, p_{4}, p_{4})$, points of the affine plane $z = 1$, to $[(q_{1}], [q_{2}], [q_{3}], [q_{4}])$ is given by
$$p_{3}^{x-1}$$
$$A_{E} = \begin{pmatrix} q_{1}^{x} & q_{2}^{x} & q_{3}^{x} \\ q_{1}^{y} & q_{2}^{y} & q_{3}^{y} \\ q_{1}^{z} & q_{2}^{z} & q_{3}^{z} \end{pmatrix} \begin{pmatrix} \lambda \overline{1} & 0 & 0 \\ \overline{\alpha}\overline{1} \\ 0 & \lambda \overline{2} & 0 \\ \overline{\alpha}\overline{2} \\ 0 & 0 & \lambda \overline{3} \end{pmatrix} \begin{pmatrix} p_{1}^{x} & p_{2}^{x} \\ p_{1}^{y} & p_{2}^{y} & p_{3}^{y} \\ 1 & 1 & 1 \end{pmatrix} .$$
$$\overline{\alpha}\overline{3}$$

<!-- PAGE 910 -->
Observe that the above homography may map some of the affine points $p_{1}, p_{2}, p_{3}, p_{4}$ (which are not “points at infinity”) to arbitrary points in $\mathbb{RP}^{2}$, which may be points at infinity (in which case $q_{i}^{z} = 0)$. The generalization to any dimension $n \ge 2$ is immediate. We define the basis $\mathcal{E}^{a} = (e_{1}^{a}, e_{2}^{a}, e_{3}^{a})$, with $e_{1}^{a} = (1, 0, 1), e_{2}^{a} = (0, 1, 1), e_{3}^{a} = (0, 0, 1)$, and call it the affine canonical basis (of $\mathbb{R}^{2})$. We also define $e_{4}^{a}$ as $e_{4}^{a} = (1, 1, 1)$. In the special case where $(p_{1}, p_{2}, p_{3}, p_{4})$ is the canonical square $(e_{1}^{a}, e_{2}^{a}, e_{3}^{a}, e_{4}^{a})$, since
$$e_{4}^{a} = e_{1}^{a} + e_{2}^{a} -e_{3}^{a},$$
we have $\alpha_{1}  = 1, \alpha_{2}  = 1$, and $\alpha_{3}  = -1$, so
$$\mathcal{B}_{P} =\mathcal{B}_{Ea} = P \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$
$$-$$
where $P$ is the change of basis matrix from the canonical basis $\mathcal{E} = (e_{1}, e_{2}, e_{3})$ to the affine basis $\mathcal{E}^{a} = (e_{1}^{a}, e_{2}^{a}, e_{3}^{a})$. We have
$$P = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{pmatrix} ,$$
and its inverse is
$$P^{-1}  = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{pmatrix} .$$
$$--$$
In this case,
$$\mathcal{B}_{Ea} = \begin{pmatrix} \alpha_{1} p_{1}^{x} & \alpha_{2} p_{2}^{x} & \alpha_{3} p_{3}^{x} \\ \alpha_{1} p_{1}^{y} & \alpha_{2} p_{2}^{y} & \alpha_{3} p_{3}^{y} \\ \alpha_{1} & \alpha_{2} & \alpha_{3} \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{pmatrix} ,$$
$$--$$
and since
$$-1$$
$$\mathcal{B}_{Ea}^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{pmatrix} =\mathcal{B}_{Ea},$$
$$--$$
we obtain
$$A_{E} = \begin{pmatrix} q_{1}^{x} & q_{2}^{x} & q_{3}^{x} \\ q_{1}^{y} & q_{2}^{y} & q_{3}^{y} \\ q_{1}^{z} & q_{2}^{z} & q_{3}^{z} \end{pmatrix} \begin{pmatrix} \lambda_{1} & 0 & 0 \\ 0 & \lambda_{2} & 0 \\ 0 & 0 & \lambda_{3} \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{pmatrix} ,$$
$$--$$
that is,
$$A_{E} = \begin{pmatrix} q_{1}^{x} & q_{2}^{x} & q_{3}^{x} \\ q_{1}^{y} & q_{2}^{y} & q_{3}^{y} \\ q_{1}^{z} & q_{2}^{z} & q_{3}^{z} \end{pmatrix} \begin{pmatrix} \lambda_{1} & 0 & 0 \\ 0 & \lambda_{2} & 0 \\ 0 & 0 & \lambda_{3} \end{pmatrix} .$$

<!-- PAGE 911 -->
The generalization to any dimension $n \ge 2$ is immediate. Finally, we consider the special case where the points $([p_{1}], [p_{2}], [p_{3}], [p_{4}])$ and the points
$$\mathbb{RP}^{2}$$
$[(q_{1}], [q_{2}], [q_{3}], [q_{4}])$ belong to the affine patch of corresponding to the plane $H$ of equation $z = 1$. In this case, we may also identify $[q_{i}]$ with $q_{i}$, which has coordinates $(q_{i}^{x} , q_{i}^{y} , 1)$ with respect to the canonical basis. Then, the barycentric coordinates $\lambda_{1} , \lambda_{2} , \lambda_{3}$  of $q_{4}$ are solutions of the systems
$$\begin{pmatrix} q_{1}^{x} & q_{2}^{x} & q_{3}^{x} \\ q_{1}^{y} & q_{2}^{y} & q_{3}^{y} \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} \lambda_{1} \\ \lambda_{2} \\ \lambda_{3} \end{pmatrix} = \begin{pmatrix} q_{4}^{x} \\ q_{4}^{y} \\ 1 \end{pmatrix} .$$
By Proposition 26.12 we obtain the following result.

> **Proposition 26.13.** With respect to the canonical basis $\mathcal{E} = (e_{1}, e_{2}, e_{3})$, the matrix $A_{E}$ of
$$\mathbb{RP}^{2}$$
the unique homography $h$ of mapping $(p_{1}, p_{2}, p_{4}, p_{4})$ to $(q_{1}, q_{2}, q_{3}, q_{4})$, all points of the affine plane $z = 1$, is given by
$$p_{3}^{x-1}$$
$$A_{E} = \begin{pmatrix} q_{1}^{x} & q_{2}^{x} & q_{3}^{x} \\ q_{1}^{y} & q_{2}^{y} & q_{3}^{y} \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} \lambda \overline{1} & 0 & 0 \\ \overline{\alpha}\overline{1} \\ 0 & \lambda \overline{2} & 0 \\ \overline{\alpha}\overline{2} \\ 0 & 0 & \lambda \overline{3} \end{pmatrix} \begin{pmatrix} p_{1}^{x} & p_{2}^{x} \\ p_{1}^{y} & p_{2}^{y} & p_{3}^{y} \\ 1 & 1 & 1 \end{pmatrix} .$$
$$\overline{\alpha}\overline{3}$$
If
$$A_{E} = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} ,$$
the transformed point of a point $(x, y, 1)$ in the affine plane $z = 1$,
$$\begin{pmatrix} x' \\ y' \\ z' \end{pmatrix} = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix} = \begin{pmatrix} a_{11}x + a_{12}y + a_{13} \\ a_{21}x + a_{22}y + a_{23} \\ a_{31}x + a_{32}y + a_{33} \end{pmatrix} ,$$
is not a point at infinity iff $a_{31}x + a_{32}y + a_{33} \neq  0$, in which case it corresponds to the point in the affine plane $z = 1$ of coordinates
$$\begin{pmatrix} x' \\ z' \\ y' \\ z' \\ 1 \end{pmatrix} = \begin{pmatrix} a_{11}x + a_{12}y + a_{13} \\ a_{31}x + a_{32}y + a_{33} \\ a_{21}x + a_{22}y + a_{23} \\ a_{31}x + a_{32}y + a_{33} \\ 1 \end{pmatrix} .$$
The generalization to any dimension $n \ge 2$ is immediate. Let us go back to the situation where the the points $(p_{1}, p_{2}, p_{3}, p_{4})$ and $(q_{1}, q_{2}, q_{3}, q_{4})$ are in the affine patch $z = 1$, and where the matrix of our linear map is expressed with

<!-- PAGE 912 -->
respect to the basis $\mathcal{P} = (p_{1}, p_{2}, p_{3})$ and the coordinates of $(q_{1}, q_{2}, q_{3}, q_{4})$ are also expressed with respect to the basis $\mathcal{P} = (p_{1}, p_{2}, p_{3})$. In practical situations, for example in computer vision, it is important to find necessary and sufficient conditions for the unique projective transformation mapping $(p_{1}, p_{2}, p_{3}, p_{4})$ to $(q_{1}, q_{2}, q_{3}, q_{4})$ to be defined on the convex hull of the points $p_{1}, p_{2}, p_{3}, p_{4}$.

> **Proposition 26.14.** The unique projective transformation mapping $(p_{1}, p_{2}, p_{3}, p_{4})$ to $(q_{1}, q_{2}, q_{3}, q_{4})$ (all points in the affine plane $H$ of equation $z = 1)$ is defined on the convex hull of the points $p_{1}, p_{2}, p_{3}, p_{4}$ iff the scalars in each of the pairs $(\alpha_{1} , \lambda_{1}$ ), $(\alpha_{2} , \lambda_{2}$ ) and $(\alpha_{3} , \lambda_{3}$ ), have the same sign.

*Proof.* With respect to the basis $\mathcal{P}$, the equation of the plane $H$ is
$$x + y + z = 1,$$
so the image of $p = (x, y, 1$ - $x$ - $y)$ under our linear map is
$$\begin{pmatrix} \lambda \overline{1} x_{1\alpha}^{\lambda2}x_{2\alpha}^{\lambda3}x_{3} \\ \overline{\alpha}\overline{1} & \overline{2} & \overline{3} \\ \lambda \overline{1} y_{1} & \lambda \overline{2} y_{2} & \lambda \overline{3} y_{3} \\ \overline{\alpha}\overline{1} & \overline{\alpha}\overline{2} & \overline{\alpha}\overline{3} \\ \lambda \overline{1} & \lambda \overline{2} & \lambda \overline{3} \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 -x -y \end{pmatrix} .$$
$$\overline{\alpha}\overline{1}\overline{\alpha}\overline{2}\overline{\alpha}\overline{3}$$
The above point is a point at infinity iff
$$\begin{pmatrix} \lambda_{1} -\lambda_{3} \\ \alpha_{1} & \alpha_{3} \end{pmatrix} x + \begin{pmatrix} \lambda_{2} -\lambda_{3} \\ \alpha_{2} & \alpha_{3} \end{pmatrix} y + \frac{\lambda_{3}}{\alpha_{3}} = 0.(*)$$
The unique projective transformation mapping $(p_{1}, p_{2}, p_{3}, p_{4})$ to $(q_{1}, q_{2}, q_{3}, q_{4})$ is defined on the convex hull of the points $p_{1}, p_{2}, p_{3}, p_{4}$ iff all four points $p_{1}, p_{2}, p_{3}, p_{4}$ are strictly contained in one of the two open half spaces determined by the line of equation (*), which means that the affine form in (*) must have the same sign on these four points. When we evaluate the affine form in (*) on the four points $p_{1}, p_{2}, p_{3}, p_{4}$ using coordinates $(x, y, 1$ - $x$ - $y)$, w.r.t. the basis $\mathcal{P} = (p_{1}, p_{2}, p_{3}), 1$. for $p_{1} = (1, 0, 0)$ we get $\lambda_{1} /\alpha_{1} , 2$. for $p_{2} = (0, 1, 0)$ we get $\lambda_{2} /\alpha_{2} , 3$. for $p_{3} = (0, 0, 1)$ we get $\lambda_{3} /\alpha_{3} , 4$. and for $p_{4} = (\alpha_{1} , \alpha_{2} , \alpha_{3}$ ) we get
$$\begin{pmatrix} \lambda_{1} -\lambda_{3} \\ \alpha_{1} & \alpha_{3} \end{pmatrix} \alpha_{1}  + \begin{pmatrix} \lambda_{2} -\lambda_{3} \\ \alpha_{2} & \alpha_{3} \end{pmatrix} \alpha_{2}  + \frac{\lambda_{3}}{\alpha_{3}} = \lambda_{1}  + \lambda_{2}  + \frac{\lambda_{3}}{\alpha_{3}} (1 -\alpha_{1}  -\alpha_{2} )$$
$$= \lambda_{1}  + \lambda_{2}  + \lambda_{3}  = 1.$$

<!-- PAGE 913 -->
The fourth case shows that the sign of the affine form in (*) is positive, and thus $\lambda_{1} /\alpha_{1} , \lambda_{2} /\alpha_{2} , \lambda_{3} /\alpha_{3}  > 0$, which implies that the scalars in each of the pairs $(\alpha_{1} , \lambda_{1}$ ), $(\alpha_{2} , \lambda_{2}$ ) and $(\alpha_{3} , \lambda_{3}$ ), must have the same sign. The generalization to any dimension $n \ge 2$ is immediate: the scalars in each pair $(\alpha_{i} , \lambda_{i}$ ) must have the same sign for $i = 1, \dots  , n + 2$. In dimension $2$, since $\alpha_{3}  = 1$ - $\alpha_{1}$  - $\alpha_{2}$  and $\lambda_{3}  = 1$ - $\lambda_{1}$  - $\lambda_{2}$ , there are four cases to consider:
$(1) \alpha_{1} , \lambda_{1} , \alpha_{2} , \lambda_{2}  < 0$. In this case, $\alpha_{3} , \lambda_{3}  > 1$ so $\alpha_{3} , \lambda_{3}$  also have the same sign.
$(2) \alpha_{1} , \lambda_{1}  < 0$ and $\alpha_{2} , \lambda_{2}  > 0$. In this case, since $\alpha_{3}  = 1$ - $\alpha_{1}$  - $\alpha_{2}$  and $\lambda_{3}  = 1$ - $\lambda_{1}$  - $\lambda_{2}$ , we must have either both $\alpha_{1}  + \alpha_{2}  < 1$ and $\lambda_{1}  + \lambda_{2}  < 1$, or both $\alpha_{1}  + \alpha_{2}  > 1$ and $\lambda_{1}  + \lambda_{2}  > 1$, in order for $\alpha_{3}$  and $\lambda_{3}$  to have the same sign.
$(3) \alpha_{1} , \lambda_{1}  > 0$ and $\alpha_{2} , \lambda_{2}  < 0$. As in the previous case, since $\alpha_{3}  = 1$ - $\alpha_{1}$  - $\alpha_{2}$  and $\lambda_{3}  = 1$ - $\lambda_{1}$  - $\lambda_{2}$ , we must have either both $\alpha_{1}  + \alpha_{2}  < 1$ and $\lambda_{1}  + \lambda_{2}  < 1$, or both $\alpha_{1}  + \alpha_{2}  > 1$ and $\lambda_{1}  + \lambda_{2}  > 1$, in order for $\alpha_{3}$  and $\lambda_{3}$  to have the same sign.
$(4) \alpha_{1} , \lambda_{1} , \alpha_{2} , \lambda_{2}  > 0$. As in the previous case, since $\alpha_{3}  = 1-\alpha_{1}  -\alpha_{2}$  and $\lambda_{3}  = 1-\lambda_{1}  -\lambda_{2}$ , we must have either both $\alpha_{1}  + \alpha_{2}  < 1$ and $\lambda_{1}  + \lambda_{2}  < 1$, or both $\alpha_{1}  + \alpha_{2}  > 1$ and $\lambda_{1}  + \lambda_{2}  > 1$, in order for $\alpha_{3}$  and $\lambda_{3}$  to have the same sign. Since $\alpha_{3}  = 1$ - $\alpha_{1}$  - $\alpha_{2}$  and $\lambda_{3}  = 1$ - $\lambda_{1}$  - $\lambda_{2}$ , we can write
$$p_{4} = \alpha_{1} p_{1} + \alpha_{2} p_{2} + \alpha_{3} p_{3} = p_{3} + \alpha_{1} (p_{1} -p_{3}) + \alpha_{2} (p_{2} -p_{3})$$
$$q_{4} = \lambda_{1} q_{1} + \lambda_{2} q_{2} + \lambda_{3} q_{3} = q_{3} + \lambda_{1} (q_{1} -q_{3}) + \lambda_{2} (q_{2} -q_{3}).$$
In the affine frame $(p_{3}, (p_{1}$ - $p_{3}, p_{2}$ - $p_{3}))$, points have coordinates $(\alpha_{1} , \alpha_{2}$ ), and in the affine frame $(q_{3}, (q_{1}$ - $q_{3}, q_{2}$ - $q_{3}))$, points have coordinates $(\lambda_{1} , \lambda_{2}$ ). In the first affine frame, the line $\langle p_{1}, p_{2}\rangle$ is given by the equation $\alpha_{1}  + \alpha_{2}  = 1$, and in the second affine frame, the line $\langle q_{1}, q_{2}\rangle$ is given by the equation $\lambda_{1}  +\lambda_{2}  = 1$. The open half plane containing $p_{3}$ and bounded by the line $\langle p_{1}, p_{2}\rangle$ corresponds to the points of coordinates $(\alpha_{1} , \alpha_{2}$ ) satisfying $\alpha_{1}  + \alpha_{2}  < 1$, and the other open half plane not containing $p_{3}$ corresponds to the points of coordinates $(\alpha_{1} , \alpha_{2}$ ) satisfying $\alpha_{1}  + \alpha_{2}  > 1$. Similarly, the open half plane containing $q_{3}$ and bounded by the line $\langle q_{1}, q_{2}\rangle$ corresponds to the points of coordinates $(\lambda_{1} , \lambda_{2}$ ) satisfying $\lambda_{1}  + \lambda_{2}  < 1$, and the other open half plane not containing $q_{3}$ corresponds to the points of coordinates $(\lambda_{1} , \lambda_{2}$ ) satisfying $\lambda_{1}  + \lambda_{2}  > 1$. Then, the above conditions have the following interpretation in terms of regions in the affine plane $z = 1$:
$(1)$ When $\alpha_{1}  < 0$ and $\alpha_{2}  < 0$, the point $p_{4}$ lies in quadrant III (with respect to the affine frames $(p_{3}, (p_{1}$ - $p_{3}, p_{2}$ - $p_{3})))$. Under the mapping $f$, the point $q_{4}$ is also mapped to quadrant III (with respect to the affine frame $(q_{3}, (q_{1} -q_{3}, q_{2} -q_{3})))$; see Figure 26.14.

<!-- PAGE 914 -->
$$IIIz= 1$$
$$IIIIV$$
$$f$$
$$III$$
$$z= 1$$
$$ppIIIIV$$
$$2p$$
$$31$$
$$q2q1$$
$$q3$$
$$f$$
$$p2$$
$$- p3q$$
$$p 22$$
$$p1  -   p$$
$$p33q3$$
$$-$$
$$p4p1q  2$$
$$q  - q$$
$$qq13$$
$$43q$$
$$1$$
$$Figure 26.14: Case (1)$$
$(2)$ When $\alpha_{1} , \lambda_{1}  < 0$ and $\alpha_{2} , \lambda_{2}  > 0$, the points $p_{4}$ and $q_{4}$ belongs to quadrant II (with respect to the affine frames $(p_{3}, (p_{1}$ - $p_{3}, p_{2}$ - $p_{3}))$ and $(q_{3}, (q_{1}$ - $q_{3}, q_{2}$ - $q_{3})))$. Two possibilities occur. Either $p_{4}$ belong to the open half space containing $p_{3}$ and bounded by the line $\langle p_{1}, p_{2}\rangle$ and $q_{4}$ belong to the open half space containing $q_{3}$ and bounded by the line $\langle q_{1}, q_{2}\rangle$ , or $p_{4}$ belong to the open half space not containing $p_{3}$ and bounded by the line $\langle p_{1}, p_{2}\rangle$ and $q_{4}$ belong to the open half space not containing $q_{3}$ and bounded by the line $\langle q_{1}, q_{2}\rangle$ . The first possibility is illustrated by the top of Figure 26.15, while the second is illustrated by the bottom of Figure 26.15.
$(3)$ When $\alpha_{1} , \lambda_{1}  > 0$ and $\alpha_{2} , \lambda_{2}  < 0$, the points $p_{4}$ and $q_{4}$ belongs to quadrant IV (with respect to the affine frames $(p_{3}, (p_{1}$ - $p_{3}, p_{2}$ - $p_{3}))$ and $(q_{3}, (q_{1}$ - $q_{3}, q_{2}$ - $q_{3})))$. Two possibilities occur exactlty as in Case $(2)$ depending on the position of $p_{4}$ with respect to the line $\langle p_{1}, p_{2}\rangle$ and on the position of $q_{4}$ with respect to the line $\langle q_{1}, q_{2}\rangle$ . The first possibility is illustrated by the top of Figure 26.16, while the second is illustrated by the bottom of Figure 26.16.
$(4)$ When $\alpha_{1} , \lambda_{1} , \alpha_{2} , \lambda  > 0$ and $\alpha_{2} , \lambda_{2}  < 0$, the points $p_{4}$ and $q_{4}$ belongs to quadrant I

<!-- PAGE 915 -->
$$f$$
$$p4p$$
$$2\alpha$$
$$1   +$$
$$- p3 \alpha  2q$$
$$p 2=q2$$
$$p  -   p 14\lambda$$
$$p313q31  +-$$
$$-$$
$$q  22\lambda$$
$$pq  - q=$$
$$1q13 1$$
$$3q$$
$$1$$
$$p4$$
$$p$$
$$2\alpha f$$
$$1   +$$
$$- p3 \alpha  2$$
$$p 2=$$
$$p  -   p 1$$
$$p313q$$
$$4$$
$$p$$
$$1$$
$$q$$
$$2$$
$$q3\lambda$$
$$-  1+-$$
$$q  2 \lambda$$
$$q  -2$$
$$1 q=$$
$$q3 1$$
$$3q$$
$$1$$
$$Figure 26.15: Case (2)$$
(with respect to the affine frames $(p_{3}, (p_{1}$ - $p_{3}, p_{2}$ - $p_{3}))$ and $(q_{3}, (q_{1}$ - $q_{3}, q_{2}$ - $q_{3})))$. Two possibilities occur exactlty as in Cases $(2)$ and $(3)$ depending on the position of $p_{4}$ with respect to the line $\langle p_{1}, p_{2}\rangle$ and on the position of $q_{4}$ with respect to the line $\langle q_{1}, q_{2}\rangle$ . The first possibility is illustrated by the top of Figure 26.17, while the second is illustrated by the bottom of Figure 26.17. Thus, if both $(p_{1}, p_{2}, p_{3}, p_{4})$ and $(q_{1}, q_{2}, q_{3}, q_{4})$ satisfy the conditions listed above, there is no point at infinity inside of the convex hull of the quadrangle $(p_{1}, p_{2}, p_{3}, p_{4})$. It remains to prove that the image of the convex hull of $(p_{1}, p_{2}, p_{3}, p_{4})$ is the convex hull of $(q_{1}, q_{2}, q_{3}, q_{4})$.

> **Proposition 26.15.** If both $(p_{1}, p_{2}, p_{3}, p_{4})$ and $(q_{1}, q_{2}, q_{3}, q_{4})$ satisfy the conditions of Proposition 26.14, then the image of the convex hull of $(p_{1}, p_{2}, p_{3}, p_{4})$ under the unique projective map mapping $(p_{1}, p_{2}, p_{3}, p_{4})$ to $(q_{1}, q_{2}, q_{3}, q_{4})$ is the convex hull of $(q_{1}, q_{2}, q_{3}, q_{4})$

*Proof.* It suffices to show that the restriction of our projective transformation maps a line segment to the convex hull of the images of the endpoints of this segment. Thus, the problem reduces to proving that if a projective transformation given by an invertible matrix
$$\begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

<!-- PAGE 916 -->
$$pf$$
$$2\alpha$$
$$1  + -$$
$$- p3 \alpha  2q$$
$$p 2= 12$$
$$p  -   p\lambda$$
$$p313q31  +$$
$$-  -$$
$$q  2 \lambda$$
$$pq  -2$$
$$11 q=$$
$$q3 1$$
$$3q$$
$$p41$$
$$q$$
$$4$$
$$p$$
$$2\alpha f$$
$$1  + -$$
$$- p3  \alpha$$
$$p 2 2$$
$$p  - =$$
$$1  p1$$
$$p33$$
$$p$$
$$1p4$$
$$q$$
$$2$$
$$q3\lambda$$
$$-  1+-$$
$$q  2 \lambda$$
$$q  -2$$
$$1 q=$$
$$q3 1$$
$$3q$$
$$1$$
$$q$$
$$4$$
$$Figure 26.16: Case (3)$$
$$\mathbb{R}^{2}$$
does not have points at infinity on the line segment in corresponding to the points of coordinates $(x, 1)$ with $0 \le x \le 1$, then the image of the line segment $[(0, 1), (1, 1)]$ is the line segment $[(b/d, 1), ((a + b)/(c + d), 1)]$ (or $[((a + b)/(c + d), 1), (b/d, 1)])$. We have
$$- -$$
$$\frac{ax + b}{cx + d} - \frac{b}{d} = \frac{adx + bdbcxbd}{d(cx + d)}$$
$$-$$
$$= \frac{(adbc)x}{d(cx + d)}$$
and
$$- - - -$$
$$\frac{ax + b}{cx + d} - \frac{a + b}{c + d} = \frac{acx + bc + adx + bdacxadbcxbd}{(c + d)(cx + d)}$$
$$- -$$
$$= \frac{(adbc)(x1)}{(c + d)(cx + d)}$$
In order for our map to be defined for $0 \le x \le 1$, cx $+ d$ must have a constant sign for $0 \le x \le 1$, which means that $d$ and $c + d$ have the same sign. Then,
$$\frac{(adbc)x}{d(cx + d)} -$$
