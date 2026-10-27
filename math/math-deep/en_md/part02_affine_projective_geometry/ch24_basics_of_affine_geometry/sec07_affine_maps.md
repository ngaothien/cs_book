# Affine Maps


<!-- PAGE 833 -->
$$\begin{pmatrix} a_{1} & b_{1} & c_{1} \\ a_{2} & b_{2} & c_{2} \\ a_{3} & b_{3} & c_{3} \end{pmatrix} \begin{pmatrix} \lambda_{0} \\ \lambda_{1} \\ \lambda_{2} \end{pmatrix} = \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \end{pmatrix} .$$
However, there is a problem when the origin of the coordinate system belongs to the plane (a, $b, c)$, since in this case, the matrix is not invertible! What we should really be doing is to solve the system
$$\longrightarrow \longrightarrow \longrightarrow  \longrightarrow$$
$$\lambda_{0} Oa + \lambda_{1} Ob + \lambda_{2} Oc =Ox,$$
where $O$ is any point not in the plane (a, $b, c)$. An alternative is to use certain well-chosen cross products. It can be shown that barycentric coordinates correspond to various ratios of areas and volumes; see the problems.

## 24.7 Affine Maps

Corresponding to linear maps we have the notion of an affine map. An affine map is defined as a map preserving affine combinations.
$$\longrightarrow  \longrightarrow$$

> **Definition 24.6.** Given two affine spaces $E, E , +$ and E',E', $+'$ , a function $f$ : $E \to$ E'
$$is an affine map iff for every family ((a_{i}, \lambda_{i} ))_{i\in I} of weighted points in E such that \sum_{i}  \in I \lambda_{i}  = 1,$$
we have
$$f \sum_{i\in I}  \lambda_{i} a_{i}!= \sum_{i\in I}  \lambda_{i} f(a_{i}).$$
In other words, $f$ preserves barycenters. Affine maps can be obtained from linear maps as follows. For simplicity of notation, the same symbol $+$ is used for both affine spaces (instead of using both $+$ and $+')$.
$$\longrightarrow$$

> **Proposition 24.7.** Given any point $a \in E$, any point $b \in$ E', and any linear map $h: E \to \longrightarrow$ E', the map $f$ : $E \to$ E' defined such that
$$f(a + v) = b + h(v)$$
is an affine map.
$$Proof. Indeed, for any family (\lambda_{i} )_{i\in I} of scalars with \sum_{i}  \in I \lambda_{i}  = 1 and any family (v_{i})_{i\in I}, since$$
$$\sum_{i\in I}  \lambda_{i} (a + v_{i}) = a + \sum_{i\in I}  \lambda_{i} ----\longrightarrow a(a + v_{i}) = a + \sum_{i\in I}  \lambda_{i} v_{i}$$

<!-- PAGE 834 -->
and
$$\sum_{i\in I}  \lambda_{i} (b + h(v_{i})) = b + \sum_{i\in I}  \lambda_{i} ------\longrightarrow b(b + h(v_{i})) = b + \sum_{i\in I}  \lambda_{i} h(v_{i}),$$
we have
$$f \sum_{i\in I}  \lambda_{i} (a + v_{i})!=fa + \sum_{i\in I}  \lambda_{i} v_{i}!$$
$$=b + h \sum_{i\in I}  \lambda_{i} v_{i}!$$
$$=b + \sum_{i\in I}  \lambda_{i} h(v_{i})$$
$$= \sum_{i\in I}  \lambda_{i} (b + h(v_{i}))$$
$$= \sum_{i\in I}  \lambda_{i} f(a + v_{i}),$$
as claimed.
$$Note that the condition \sum_{i}  I \lambda_{i}  = 1 was implicitly used (in a hidden call to Proposition$$
24.1) in deriving that
$$\sum_{i\in I}^{\in}  \lambda_{i} (a + v_{i}) = a + \sum_{i\in I}  \lambda_{i} v_{i}$$
and
$$\sum_{i\in I}  \lambda_{i} (b + h(v_{i})) = b + \sum_{i\in I}  \lambda_{i} h(v_{i}).$$
As a more concrete example, the map
$$\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} \mapsto \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} + \begin{pmatrix} 3 \\ 1 \end{pmatrix}$$
defines an affine map $in\mathbb{A}^{2}$. It is a “shear” followed by a translation. The effect of this shear on the square (a, $b, c, d)$ is shown in Figure 24.18. The image of the square (a, $b, c, d)$ is the parallelogram (a', b', c', d'). Let us consider one more example. The map
$$\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} \mapsto \begin{pmatrix} 1 & 1 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} + \begin{pmatrix} 3 \\ 0 \end{pmatrix}$$
is an affine map. Since we can write
$$\sqrt$$
$$\begin{pmatrix} 1 & 1 \\ 1 & 3 \end{pmatrix} =\overline{2} \begin{pmatrix} \sqrt & \sqrt \\ \overline{2}/2 & -\sqrt{2}/2 \\ 2/2 & 2/2 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} ,$$

<!-- PAGE 835 -->
$$d= (5,2)c= (6,2)$$
$$d = (0,1)c = (1,1)$$
$$a\overline{= (3,1)}\overline{b}= (4,1)$$
$$\overline{a = (0,0)} b = (1,0)$$
$$Figure 24.18: The effect of a shear.$$
this affine map is the composition of a shear, followed by a rotation of angle $\pi /4$, followed by
$$\sqrt$$
a magnification of ratio $\overline{2,}$ followed by a translation. The effect of this map on the square (a, $b, c, d)$ is shown in Figure 24.19. The image of the square (a, $b, c, d)$ is the parallelogram (a', b', c', d').
$$c= (5,4)$$
$$‘= (4,3)$$
$$d$$
$$d = (0,1)c= (1,1)$$
$$b= (4,1)$$
$$\overline{a = (0,0)}\overline{b = (1,0)} a= (3,0)$$
$$Figure 24.19: The effect of an affine map.$$
The following proposition shows the converse of what we just showed. Every affine map is determined by the image of any point and a linear map.
$$\longrightarrow  \longrightarrow$$

> **Proposition 24.8.** Given an affine map $f$ : $E \to$ E', there is a unique linear map $f$ : $E \to \longrightarrow$ E' such that
$$\longrightarrow$$
$$f(a + v) = f(a) +f (v),$$
$$\longrightarrow$$
for every $a \in E$ and every $v \in E$ .

*Proof.* Let $a \in E$ be any point in $E$. We claim that the map defined such that
$$\longrightarrow  --------\longrightarrow$$
$$f (v) =f(a)f(a + v)$$

<!-- PAGE 836 -->
$$\longrightarrow  \longrightarrow  \longrightarrow \longrightarrow$$
for every $v \in E$ is a linear map $f$ : $E \to$ E'. Indeed, we can write
$$a + \lambda v = \lambda (a + v) + (1 -\lambda )a,$$
$$----\longrightarrow$$
$$\longrightarrow$$
since $a + \lambda v = a + \lambda$ a(a $+ v) + (1$ - $\lambda$ )aa, and also
$$a + u + v = (a + u) + (a + v) -a,$$
$$----\longrightarrow  ----\longrightarrow$$
$$\longrightarrow$$
since $a + u + v = a +$ a(a $+ u) +$ a(a $+ v)$ - aa. Since $f$ preserves barycenters, we get
$$f(a + \lambda v) = \lambda f(a + v) + (1 -\lambda )f(a).$$
$$If we recall that x = \sum_{i}  \in I \lambda_{i} a_{i} is the barycenter of a family ((a_{i}, \lambda_{i} ))_{i\in I} of weighted points$$
$$(with \sum_{i}  \in I \lambda_{i}  = 1) iff\longrightarrow \longrightarrow$$
$$bx = \sum_{i\in I}  \lambda_{i} ba_{i}for every b \in E,$$
we get
$$---------\longrightarrow --------\longrightarrow ----\longrightarrow --------\longrightarrow$$
$$f(a)f(a + \lambda v) = \lambda f(a)f(a + v) + (1 -\lambda )f(a)f(a) = \lambda f(a)f(a + v),$$
$$\longrightarrow \longrightarrow$$
showing that $f (\lambda v) = \lambda f (v)$. We also have
$$f(a + u + v) = f(a + u) + f(a + v) -f(a),$$
from which we get
$$-----------\longrightarrow  --------\longrightarrow  --------\longrightarrow$$
$$f(a)f(a + u + v) =f(a)f(a + u) +f(a)f(a + v),$$
$$\longrightarrow  \longrightarrow  \longrightarrow  \longrightarrow$$
showing that $f (u + v) = f (u) + f (v)$. Consequently, $f$ is a linear map. For any other point $b \in E$, since
$$\longrightarrow  ----\longrightarrow  \longrightarrow$$
$$\longrightarrow$$
$$b + v = a +ab + v = a +a(a + v) -aa +ab,$$
$b + v = (a + v)$ - $a + b$, and since $f$ preserves barycenters, we get
$$f(b + v) = f(a + v) -f(a) + f(b),$$
which implies that
$$-------\longrightarrow -------\longrightarrow ----\longrightarrow  ----\longrightarrow$$
$$f(b)f(b + v)=f(b)f(a + v) -f(b)f(a) +f(b)f(b),$$
$$----\longrightarrow  -------\longrightarrow$$
$$=f(a)f(b) +f(b)f(a + v),$$
$$--------\longrightarrow$$
$$=f(a)f(a + v).$$
$-------\longrightarrow  --------\longrightarrow  \longrightarrow$ Thus, f(b)f(b $+ v) =$ f(a)f(a $+ v)$, which shows that the definition of $f$ does not depend
$$\longrightarrow  \longrightarrow$$
on the choice of $a \in E$. The fact that $f$ is unique is obvious: We must have $f (v) = --------\longrightarrow$ f(a)f(a $+ v)$.

<!-- PAGE 837 -->
$$\longrightarrow  \longrightarrow \longrightarrow$$
The unique linear map $f$ : $E \to$ E' given by Proposition 24.8 is called the linear map associated with the affine map $f$. Note that the condition
$$\longrightarrow$$
$$f(a + v) = f(a) +f (v),$$
$$\longrightarrow$$
for every $a \in E$ and every $v \in E$ , can be stated equivalently as
$$\longrightarrow ----\longrightarrow  \longrightarrow$$
$$\longrightarrow \longrightarrow$$
$$f(x) = f(a) +f (ax),orf(a)f(x) =f (ax),$$
for all a, $x \in E$. Proposition 24.8 shows that for any affine map $f$ : $E \to$ E', there are points
$$\longrightarrow  \longrightarrow \longrightarrow$$
$a \in E, b \in$ E', and a unique linear map $f$ : $E \to$ E', such that
$$\longrightarrow$$
$$f(a + v) = b +f (v),$$
$$\longrightarrow  \longrightarrow$$
for all $v \in E$ (just let $b =$ f(a), for any $a \in E)$. Affine maps for which $f$ is the identity
$$\longrightarrow$$
map are called translations. Indeed, if $f =$ id,
$$\longrightarrow  --\longrightarrow$$
$$\longrightarrow  \longrightarrow  \longrightarrow  \longrightarrow$$
$$f(x)=f(a) +f (ax) = f(a) +ax = x +xa +af(a) +ax$$
$$--\longrightarrow  --\longrightarrow$$
$$\longrightarrow \longrightarrow$$
$$=x +xa +af(a) -xa = x +af(a),$$
and so
$$--\longrightarrow  --\longrightarrow$$
$$xf(x) =af(a),$$
$$--\longrightarrow$$
which shows that $f$ is the translation induced by the vector af(a) (which does not depend on a). Since an affine map preserves barycenters, and since an affine subspace $V$ is closed under barycentric combinations, the image f(V ) of $V$ is an affine subspace in E'. So, for example, the image of a line is a point or a line, and the image of a plane is either a point, a line, or a plane. It is easily verified that the composition of two affine maps is an affine map. Also, given affine maps $f$ : $E \to$ E' and $g$: E' $\to$ E'', we have
$$\longrightarrow$$
$$g(f(a + v)) = g \begin{pmatrix} \longrightarrow \\ f(a) +f(v) \end{pmatrix} = g(f(a)) +g \begin{pmatrix} \longrightarrow \\ f(v) \end{pmatrix} ,$$
$$-\longrightarrow  \longrightarrow \longrightarrow$$
which shows that $g \circ f = g \circ f$ . It is easy to show that an affine map $f$ : $E \to$ E' is injective $\longrightarrow  \longrightarrow \longrightarrow \longrightarrow  \longrightarrow \longrightarrow$ iff $f$ : $E \to$ E' is injective, and that $f$ : $E \to$ E' is surjective iff $f$ : $E \to$ E' is surjective.
$$\longrightarrow  \longrightarrow \longrightarrow$$
An affine map $f$ : $E \to$ E' is constant iff $f$ : $E \to$ E' is the null (constant) linear map equal
$$\longrightarrow$$
to $0$ for all $v \in E$ . If $E$ is an affine space of dimension $m$ and $(a_{0}, a_{1}, \dots  , a_{m})$ is an affine frame for $E$, then for any other affine space $F$ and for any sequence $(b_{0}, b_{1}, \dots  , b_{m})$ of $m + 1$ points in $F$, there

<!-- PAGE 838 -->
is a unique affine map $f$ : $E \to F$ such that $f(a_{i}) = b_{i}$, for $0 \le i \le m$. Indeed, $f$ must be such that
$$f(\lambda_{0} a_{0} + \cdots  + \lambda_{m} a_{m}) = \lambda_{0} b_{0} + \cdots  + \lambda_{m} b_{m},$$
where $\lambda_{0} +\cdots +\lambda_{m}  = 1$, and this defines a unique affine map on all of $E$, since $(a_{0}, a_{1}, \dots  , a_{m})$ is an affine frame for $E$. Using affine frames, affine maps can be represented in terms of matrices. We explain how an affine map $f$ : $E \to E$ is represented with respect to a frame $(a_{0}, \dots  , a_{n})$ in $E$, the more general case where an affine map $f$ : $E \to F$ is represented with respect to two affine frames $(a_{0}, \dots  , a_{n})$ in $E$ and $(b_{0}, \dots  , b_{m})$ in $F$ being analogous. Since
$$\longrightarrow$$
$$f(a_{0} + x) = f(a_{0}) +f (x)$$
$$\longrightarrow$$
for all $x \in E$ , we have
$$-------\longrightarrow  ---\longrightarrow  \longrightarrow$$
$$a_{0}f(a_{0} + x) =a_{0}f(a_{0}) +f (x).$$
$$---\longrightarrow  -------\longrightarrow$$
Since $x, a_{0}f(a_{0})$, and $a_{0}f(a_{0} + x)$, can be expressed as
$$-\longrightarrow -\longrightarrow$$
$$x=x_{1}a_{0}a_{1} + \cdots  + x_{n}a_{0}a_{n},$$
$$---\longrightarrow$$
$$-\longrightarrow -\longrightarrow$$
$$a_{0}f(a_{0})=b_{1}a_{0}a_{1} + \cdots  + b_{n}a_{0}a_{n},$$
$$-------\longrightarrow$$
$$-\longrightarrow -\longrightarrow$$
$$a_{0}f(a_{0} + x)=y_{1}a_{0}a_{1} + \cdots  + y_{n}a_{0}a_{n},$$
$$\longrightarrow -\longrightarrow  -\longrightarrow$$
if $A = (a_{i j})$ is the $n\times n$ matrix of the linear map $f$ over the basis $(a_{0}a_{1}, \dots  ,a_{0}a_{n})$, letting $x, y$, and $b$ denote the column vectors of components $(x_{1}, \dots  , x_{n}), (y_{1}, \dots  , y_{n})$, and $(b_{1}, \dots  , b_{n})$,
$$-------\longrightarrow  ---\longrightarrow  \longrightarrow$$
$$a_{0}f(a_{0} + x) =a_{0}f(a_{0}) +f (x)$$
is equivalent to
$$y = Ax + b.$$
Note that $b \neq  0$ unless $f(a_{0}) = a_{0}$. Thus, $f$ is generally not a linear transformation, unless it has a fixed point, i.e., there is a point $a_{0}$ such that $f(a_{0}) = a_{0}$. The vector $b$ is the “translation part” of the affine map. Affine maps do not always have a fixed point. Obviously, nonnull translations have no fixed point. A less trivial example is given by the affine map
$$\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} \mapsto \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} + \begin{pmatrix} 1 \\ 0 \end{pmatrix} .$$
This map is a reflection about the x-axis followed by a translation along the x-axis. The affine map
$$\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} \mapsto \begin{pmatrix} \sqrt \\ \sqrt1 & - & \overline{3} \\ 3/4 & 1/4 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} + \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$

<!-- PAGE 839 -->
can also be written as
$$\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} \mapsto \begin{pmatrix} 2 & 0 \\ 0 & 1/2 \end{pmatrix} \begin{pmatrix} \sqrt \\ \sqrt1/2 & - & \overline{3}/2 \\ 3/2 & 1/2 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} + \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$
which shows that it is the composition of a rotation of angle $\pi /3$, followed by a stretch (by a factor of $2$ along the x-axis, and by a factor $of^{1}$  along the y-axis), followed by a translation. It is easy to show that this affine map has $a^{2}$ unique fixed point. On the other hand, the affine map
$$\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} \mapsto \begin{pmatrix} 8 \\ /5 & -6/5 \\ 3/10 & 2/5 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} + \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$
has no fixed point, even though
$$\begin{pmatrix} 8 \\ /5 & -6/5 \\ 3/10 & 2/5 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 1/2 \end{pmatrix} \begin{pmatrix} 4/5 & -3/5 \\ 3/5 & 4/5 \end{pmatrix} ,$$
and the second matrix is a rotation of angle $\theta$  such that cos $\theta  =_{5}^{4}$  and sin $\theta  =_{5}^{3}$ .
$$\longrightarrow$$
To simplify notation, given any two points $x, y$, let us denote the vector xy by $y$ - $x$ and the linear map asociated with an affine map $f$ by $h$. The reason for using the origins a and $b$ is that it gives us more flexibility. In particular, we can choose $b =$ f(a), and then $f$ behaves like a linear map with respect to the origins a and $b =$ f(a). When $E = F$, if there is some $a \in E$ such that f(a) $= a$ (a is a fixed point of $f)$, then we can pick $b = a$. Then because f(a) $= a$, we get
$$v = f(u) = f(a + u -a) = f(a) + h(u -a) = a + h(u -a),$$
that is
$$v -a = h(u -a).$$
With respect to the new origin a, if we define $x$ and $y$ by
$$x = u -a$$
$$y = v -a,$$
then we get
$$y = h(x).$$
Therefore, $f$ really behaves like a linear map, but with respect to the new origin a (not the standard origin $0)$. This is the case of a rotation around an axis that does not pass through the origin. We now describe the trick which allows us to incorporate the translation part $d$ into the matrix $A$. This trick is very useful in kinematics and dynamics, where $A$ is a rotation matrix. Such affine maps are called rigid motions.

<!-- PAGE 840 -->
We define the $(m + 1) \times  (n + 1)$ matrix A' obtained by first adding $d$ as the $(n +$ 1)th column and then $(0, \dots  , 0, 1)$ as the $(m +$ 1)th row:
$$| {z }$$
$$n$$
$$A'= \begin{pmatrix} A & d \\ 0_{n} & 1 \end{pmatrix} .$$
It is clear that
$$\begin{pmatrix} y \\ 1 \end{pmatrix} = \begin{pmatrix} A & d \\ 0_{n} & 1 \end{pmatrix} \begin{pmatrix} x \\ 1 \end{pmatrix}$$
iff
$$y = Ax + d.$$
$$\mathbb{R}^{n}$$
This amounts to considering a point $x \in$ as a point $(x, 1)$ in the (affine) hyperplane $H_{n+1} \mathbb{R}^{n+1}$ in of equation $x_{n+1} = 1$. Then an affine map is the restriction to the hyperplane $H_{n+1}$
$$\mathbb{R}^{n+1}  \mathbb{R}^{m+1}$$
of the linear map $f$ from to corresponding to the matrix A' which maps $H_{n+1}$
$$b$$
into $H_{m+1} (f(H_{n+1}) \subseteq H_{m+1})$. Figure 24.20 illustrates this process for $n = 2$.
$$b$$
$$x_{3}$$
$$(x_{1},x_{2}, 1)$$
$$H_{3} : x_{3} = 1$$
$$x_{2}$$
$$x = ( x_{1},x_{2})$$
$$x_{1}$$
$$\mathbb{R}^{n}  \mathbb{R}^{n+1}$$
$$Figure 24.20: Viewingas a hyperplane in(n = 2)$$
For example, the map
$$\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} \mapsto \begin{pmatrix} 1 & 1 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} + \begin{pmatrix} 3 \\ 0 \end{pmatrix}$$
$$\mathbb{R}^{3}$$
defines an affine map $f$ which is represented in by
$$\begin{pmatrix} x_{1} \\ x_{2} \\ 1 \end{pmatrix} \mapsto \begin{pmatrix} 1 & 1 & 3 \\ 1 & 3 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ 1 \end{pmatrix} .$$
