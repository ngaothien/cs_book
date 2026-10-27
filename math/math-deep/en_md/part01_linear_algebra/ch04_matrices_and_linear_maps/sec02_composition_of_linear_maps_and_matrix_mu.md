# Composition of Linear Maps and Matrix Multiplication


<!-- PAGE 130 -->
This is to be expected by the fundamental theorem of calculus since the derivative of an integral returns the function. As we will shortly see, the above matrix product corresponds to this functional composition. The equation $DS = I_{4}$ shows that $S$ is injective and has $D$ as a left inverse. However, SD $\neq  I_{5}$, and instead
$$\begin{pmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1/2 & 0 & 0 \\ 0 & 0 & 1/3 & 0 \\ 0 & 0 & 0 & 1/4 \end{pmatrix} \begin{pmatrix} 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 & 0 \\ 0 & 0 & 0 & 3 & 0 \\ 0 & 0 & 0 & 0 & 4 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix} ,$$
because constant polynomials (polynomials of degree $0)$ belong to the kernel of $D$.

## 4.2 Composition of Linear Maps and Matrix

$$Multiplication$$
Let us now consider how the composition of linear maps is expressed in terms of bases. Let $E, F$, and $G$, be three vectors spaces with respective bases $(u_{1}, \dots  , u_{p})$ for $E, (v_{1}, \dots  , v_{n})$ for $F$, and $(w_{1}, \dots  , w_{m})$ for $G$. Let $g: E \to F$ and $f$ : $F \to G$ be linear maps. As explained earlier, $g: E \to F$ is determined by the images of the basis vectors $u_{j}$, and $f$ : $F \to G$ is determined by the images of the basis vectors $v_{k}$. We would like to understand how $f \circ g: E \to G$ is determined by the images of the basis vectors $u_{j}$.
Remark: Note that we are considering linear maps $g: E \to F$ and $f$ : $F \to G$, instead of $f$ : $E \to F$ and $g: F \to G$, which yields the composition $f \circ g: E \to G$ instead of $g \circ f$ : $E \to G$. Our perhaps unusual choice is motivated by the fact that if $f$ is represented by a matrix M(f) $= (a_{i k})$ and $g$ is represented by a matrix M(g) $= (b_{k j})$, then $f \circ g: E \to G$ is represented by the product $AB$ of the matrices $A$ and $B$. If we had adopted the other choice where $f$ : $E \to F$ and $g: F \to G$, then $g \circ f$ : $E \to G$ would be represented by the product $BA$. Personally, we find it easier to remember the formula for the entry in Row $i$ and Column $j$ of the product of two matrices when this product is written by AB, rather than BA. Obviously, this is a matter of taste! We will have to live with our perhaps unorthodox choice. Thus, let
$$f(v_{k}) = \sum_{i=1}^{m}  a_{i k}w_{i},$$
for every $k, 1 \le k \le n$, and let
$$g(u_{j}) = \sum_{k=1}^{n}  b_{k j}v_{k},$$

<!-- PAGE 131 -->
for every $j, 1 \le j \le p$; in matrix form, we have
$$f(v_{1})f(v_{2})\dots f(v_{n})$$
$$w_{1}$$
$$w_{2}\vdots \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{pmatrix}$$
$$w_{m}$$
and
$$g(u_{1})g(u_{2})\dots g(u_{p})$$
$$v_{1}$$
$$v_{2}\vdots \begin{pmatrix} b_{11} & b_{12} & \dots & b_{1p} \\ b_{21} & b_{22} & \dots & b_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ b_{n1} & b_{n2} & \dots & b_{np} \end{pmatrix} .$$
$$v_{n}$$
By previous considerations, for every
$$x = x_{1}u_{1} + \cdots  + x_{p}u_{p},$$
letting g(x) $= y = y_{1}v_{1} + \cdots  + y_{n}v_{n}$, we have
$$y_{k} = \sum_{j=1}^{p}  b_{k j}x_{j}(2)$$
for all $k, 1 \le k \le n$, and for every
$$y = y_{1}v_{1} + \cdots  + y_{n}v_{n},$$
letting f(y) $= z = z_{1}w_{1} + \cdots  + z_{m}w_{m}$, we have
$$z_{i} = \sum_{k=1}^{n}  a_{i k}y_{k}(3)$$
for all $i, 1 \le i \le m$. Then if $y =$ g(x) and $z =$ f(y), we have $z =$ f(g(x)), and in view of $(2)$ and $(3)$, we have
$$z_{i} = \sum_{k=1}^{n}  a_{i k}( \sum_{j=1}^{p}  b_{k j}x_{j})$$
$$= \sum_{k=1j}^{n}  \sum_{=1}^{p}  a_{i k}b_{k j}x_{j}$$
$$= \sum_{j=1}^{p}  \sum_{k=1}^{n}  a_{i k}b_{k j}x_{j}$$
$$= \sum_{j=1}^{p}  ( \sum_{k=1}^{n}  a_{i k}b_{k j})x_{j}.$$

<!-- PAGE 132 -->
Thus, defining $c_{i j}$ such that
$$c_{i j} = \sum_{k=1}^{n}  a_{i k}b_{k j},$$
for $1 \le i \le m$, and $1 \le j \le p$, we have
$$z_{i} = \sum_{j=1}^{p}  c_{i j}x_{j}(4)$$
Identity $(4)$ shows that the composition of linear maps corresponds to the product of matrices. Then given a linear map $f$ : $E \to F$ represented by the matrix M(f) $= (a_{i j})$ w.r.t. the bases $(u_{1}, \dots  , u_{n})$ and $(v_{1}, \dots  , v_{m})$, by Equation $(1)$, namely
$$y_{i} = \sum_{j=1}^{n}  a_{i j}x_{j}1 \le i \le m,$$
and the definition of matrix multiplication, the equation $y =$ f(x) corresponds to the matrix equation M(y) $=$ M(f)M(x), that is,
$$\begin{pmatrix} y_{1} \\ \vdots \\ y_{m} \end{pmatrix} = \begin{pmatrix} a_{1 1} & \dots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} & \dots & a_{m n} \end{pmatrix} \begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix} .$$
Recall that
$$\begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{m n} \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ \vdots \\ x_{n} \end{pmatrix} = x_{1} \begin{pmatrix} a_{1 1} \\ a_{2 1} \\ \vdots \\ a_{m1} \end{pmatrix} + x_{2} \begin{pmatrix} a_{1 2} \\ a_{2 2} \\ \vdots \\ a_{m2} \end{pmatrix} + \cdots  + x_{n} \begin{pmatrix} a_{1n} \\ a_{2n} \\ \vdots \\ a_{m n} \end{pmatrix} .$$
Sometimes, it is necessary to incorporate the bases $(u_{1}, \dots  , u_{n})$ and $(v_{1}, \dots  , v_{m})$ in the notation for the matrix M(f) expressing $f$ with respect to these bases. This turns out to be a messy enterprise! We propose the following course of action:

> **Definition 4.2.** Write $\mathcal{U} = (u_{1}, \dots  , u_{n})$ and $\mathcal{V} = (v_{1}, \dots  , v_{m})$ for the bases of $E$ and $F$, and denote by $M_{U,V}(f)$ the matrix of $f$ with respect to the bases $\mathcal{U}$ and $\mathcal{V}$. Furthermore, write $x_{U}$ for the coordinates M(x) $= (x_{1}, \dots  , x_{n})$ of $x \in E$ w.r.t. the basis $\mathcal{U}$ and write $y_{V}$ for the coordinates M(y) $= (y_{1}, \dots  , y_{m})$ of $y \in F$ w.r.t. the basis $\mathcal{V}$ . Then
$$y = f(x)$$

<!-- PAGE 133 -->
is expressed in matrix form by
$$y_{V} = M_{U,V}(f) x_{U}.$$
When $\mathcal{U} =\mathcal{V}$, we abbreviate $M_{U,V}(f)$ as $M_{U}(f)$. The above notation seems reasonable, but it has the slight disadvantage that in the expression $M_{U,V}(f)x_{U}$, the input argument $x_{U}$ which is fed to the matrix $M_{U,V}(f)$ does not appear next to the subscript $\mathcal{U}$ in $M_{U,V}(f)$. We could have used the notation $M_{V,U}(f)$, and some people do that. But then, we find a bit confusing $that\mathcal{V}$ comes $before\mathcal{U}$ when $f$ maps from the space $E$ with the basis $\mathcal{U}$ to the space $F$ with the basis $\mathcal{V}$. So, we prefer to use the notation $M_{U,V}(f)$. Be aware that other authors such as Meyer $[129]$ use the notation $[f]_{U,V}$, and others such as Dummit and Foote $[55]$ use the notation $M_{U}^{V}  (f)$, instead of $M_{U,V}(f)$. This gets worse! You may find the notation $M_{V}^{U}  (f)$ (as in Lang $[113]), or_{U}[f]_{V}$, or other strange notations. Definition 4.2 shows that the function which associates to a linear map $f$ : $E \to F$ the matrix M(f) w.r.t. the bases $(u_{1}, \dots  , u_{n})$ and $(v_{1}, \dots  , v_{m})$ has the property that matrix multiplication corresponds to composition of linear maps. This allows us to transfer properties of linear maps to matrices. Here is an illustration of this technique:

> **Proposition 4.1.** $(1)$ Given any matrices $A \in M_{m,n}(K), B \in M_{n,p}(K)$, and $C \in M_{p,q}(K)$, we have
$$(AB)C = A(BC);$$
that is, matrix multiplication is associative.
$(2)$ Given any matrices $A, B \in M_{m,n}(K)$, and $C, D \in M_{n,p}(K)$, for all $\lambda  \in K$, we have
$$(A + B)C = AC + BC$$
$$A(C + D) = AC + AD$$
$$(\lambda A)C = \lambda (AC)$$
$$A(\lambda C) = \lambda (AC),$$
so that matrix multiplication $\cdot$ : $M_{m,n}(K) \times  M_{n,p}(K) \to M_{m,p}(K)$ is bilinear.

*Proof.* $(1)$ Every $m \times  n$ matrix $A = (a_{i j})$ defines the function $f_{A}$ : $K^{n} \to K^{m}$ given by
$$f_{A}(x) = Ax,$$
for all $x \in K^{n}$. It is immediately verified that $f_{A}$ is linear and that the matrix $M(f_{A})$ representing $f_{A}$ over the canonical bases in $K^{n}$ and $K^{m}$ is equal to $A$. Then Formula $(4)$ proves that
$$M(f_{A} \circ f_{B}) = M(f_{A})M(f_{B}) = AB,$$
so we get
$$M((f_{A} \circ f_{B}) \circ f_{C}) = M(f_{A} \circ f_{B})M(f_{C}) = (AB)C$$

<!-- PAGE 134 -->
and
$$M(f_{A} \circ (f_{B} \circ f_{C})) = M(f_{A})M(f_{B} \circ f_{C}) = A(BC),$$
and since composition of functions is associative, we have $(f_{A} \circ f_{B}) \circ f_{C} = f_{A} \circ (f_{B} \circ f_{C})$, which implies that
$$(AB)C = A(BC).$$
$(2)$ It is immediately verified that if $f_{1}, f_{2} \in Hom_{K}(E, F), A, B \in M_{m,n}(K), (u_{1}, \dots  , u_{n})$ is any basis of $E$, and $(v_{1}, \dots  , v_{m})$ is any basis of $F$, then
$$M(f_{1} + f_{2}) = M(f_{1}) + M(f_{2})$$
$$f_{A+B} = f_{A} + f_{B}.$$
Then we have
$$(A + B)C = M(f_{A+B})M(f_{C})$$
$$= M(f_{A+B} \circ f_{C})$$
$$= M((f_{A} + f_{B}) \circ f_{C}))$$
$$= M((f_{A} \circ f_{C}) + (f_{B} \circ f_{C}))$$
$$= M(f_{A} \circ f_{C}) + M(f_{B} \circ f_{C})$$
$$= M(f_{A})M(f_{C}) + M(f_{B})M(f_{C})$$
$$= AC + BC.$$
The equation A(C $+ D) = AC + AD$ is proven in a similar fashion, and the last two equations are easily verified. We could also have verified all the identities by making matrix computations. Note that Proposition 4.1 implies that the vector space $M_{n}(K)$ of square matrices is a
(noncommutative) ring with unit $I_{n}$. (It even shows that $M_{n}(K)$ is an associative algebra.) The following proposition states the main properties of the mapping $f \mapsto$ M(f) between Hom(E, $F)$ and $M_{m,n}$. In short, it is an isomorphism of vector spaces.

> **Proposition 4.2.** Given three vector spaces $E, F, G$, with respective bases $(u_{1}, \dots  , u_{p}), (v_{1}, \dots  , v_{n})$, and $(w_{1}, \dots  , w_{m})$, the mapping $M$ : Hom(E, $F) \to M_{n,p}$ that associates the matrix M(g) to a linear map $g: E \to F$ satisfies the following properties for all $x \in E$, all $g, h: E \to F$, and all $f$ : $F \to G$:
$$M(g(x)) = M(g)M(x)$$
$$M(g + h) = M(g) + M(h)$$
$$M(\lambda g) = \lambda M(g)$$
$$M(f \circ g) = M(f)M(g),$$

<!-- PAGE 135 -->
where M(x) is the column vector associated with the vector $x$ and M(g(x)) is the column vector associated with g(x), as explained in Definition 4.1. Thus, $M$ : Hom(E, $F) \to M_{n,p}$ is an isomorphism of vector spaces, and when $p = n$ and the basis $(v_{1}, \dots  , v_{n})$ is identical to the basis $(u_{1}, \dots  , u_{p}), M$ : Hom(E, $E) \to M_{n}$ is an isomorphism of rings.

*Proof.* That M(g(x)) $=$ M(g)M(x) was shown by Definition 4.2 or equivalently by Formula $(1)$. The identities M(g $+ h) =$ M(g) $+$ M(h) and $M(\lambda g) = \lambda$ M(g) are straightforward, and M(f $\circ g) =$ M(f)M(g) follows from Identity $(4)$ and the definition of matrix multiplication. The mapping $M$ : Hom(E, $F) \to M_{n,p}$ is clearly injective, and since every matrix defines a linear map (see Proposition 4.1), it is also surjective, and thus bijective. In view of the above identities, it is an isomorphism (and similarly for $M$ : Hom(E, $E) \to M_{n}$, where Proposition 4.1 is used to show that $M_{n}$ is a ring). In view of Proposition 4.2, it seems preferable to represent vectors from a vector space of finite dimension as column vectors rather than row vectors. Thus, from now on, we will
$$\mathbb{R}^{n}$$
denote vectors of (or more generally, of $K^{n})$ as column vectors. We explained in Section 3.9 that if the space $E$ is finite-dimensional and has a finite basis $(u_{1}, \dots  , u_{n})$, then a linear form $f^{*}$ : $E \to K$ is represented by the row vector of coefficients
$$\begin{pmatrix} f^{*}(u_{1}) & \cdots & f^{*}(u_{n}) \end{pmatrix} ,(1)$$
over the bases $(u_{1}, \dots  , u_{n})$ and $1$ (in $K)$, and that over the dual basis $(u_{1}^{*}, \dots  , u_{n}^{*})$ of $E^{*}$, the linear form $f^{*}$ is represented by the same coefficients, but as the column vector
$$\begin{pmatrix} f^{*}(u_{1}) \\ \vdots \\ f^{*}(u_{n}) \end{pmatrix} ,(2)$$
which is the transpose of the row vector in $(1)$. This is a special case of a more general phenomenon. A linear map $f$ : $E \to F$ induces a map $f^{\top}$ : $F^{*} \to E^{*}$ called the transpose of $f$ (note that $f^{\top}$ maps $F^{*}$ to $E^{*}$, not $E^{*}$ to $F^{*}$ ), and if $(u_{1} \dots  , u_{n})$ is a basis of $E, (v_{1} \dots  , v_{m})$ is a basis of $F$, and if $f$ is represented by the $m \times  n$ matrix $A$ over these bases, then over the dual bases $(v_{1}^{*}, \dots  , v_{m}^{*})$ and $(u_{1}^{*}, \dots  , u_{n}^{*})$, the linear map $f^{\top}$ is represented by $A^{\top}$, the transpose of the matrix $A$. This is because over the basis $(v_{1}, \dots  , v_{m})$, a linear form $\phi  \in F^{*}$ is represented by the row vector
$$\lambda  = \begin{pmatrix} \phi (v_{1}) & \cdots & \phi (v_{m}) \\ representedbythe \end{pmatrix} ,$$
and we define $f^{\top} (\phi$ ) as the linear form    row vector
$$\lambda A$$
