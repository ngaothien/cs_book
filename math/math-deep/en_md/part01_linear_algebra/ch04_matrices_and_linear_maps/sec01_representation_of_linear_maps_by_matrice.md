# Representation of Linear Maps by Matrices


<!-- PAGE 125 -->
Chapter $4$ Matrices and Linear Maps In this chapter, all vector spaces are defined over an arbitrary field $K$. For the sake of concreteness, the reader may safely assume that $K =\mathbb{R}$.

## 4.1 Representation of Linear Maps by Matrices

Proposition 3.20 shows that given two vector spaces $E$ and $F$ and a basis $(u_{j})_{j\in J}$ of $E$, every linear map $f$ : $E \to F$ is uniquely determined by the family $(f(u_{j}))_{j\in J}$ of the images under $f$ of the vectors in the basis $(u_{j})_{j\in J}$. If we also have a basis $(v_{i})_{i\in I}$ of $F$, then every vector $f(u_{j})$ can be written in a unique way as
$$f(u_{j}) = \sum_{i\in I}  a_{i j}v_{i},$$
where $j \in J$, for a family of scalars $(a_{i j})_{i\in I}$. Thus, with respect to the two bases $(u_{j})_{j\in J}$ of $E$ and $(v_{i})_{i\in I}$ of $F$, the linear map $f$ is completely determined by a “I $\times J$-matrix” M(f) $= (a_{i j})_{(i,j)\in I\times J}$.
Remark: Note that we intentionally assigned the index set $J$ to the basis $(u_{j})_{j\in J}$ of $E$, and the index set $I$ to the basis $(v_{i})_{i\in I}$ of $F$, so that the rows of the matrix M(f) associated with $f$ : $E \to F$ are indexed by I, and the columns of the matrix M(f) are indexed by $J$. Obviously, this causes a mildly unpleasant reversal. If we had considered the bases $(u_{i})_{i\in I}$ of $E$ and $(v_{j})_{j\in J}$ of $F$, we would obtain a $J \times I$-matrix M(f) $= (a_{j i})_{(j,i)\in J\times I}$. No matter what we do, there will be a reversal! We decided to stick to the bases $(u_{j})_{j\in J}$ of $E$ and $(v_{i})_{i\in I}$ of $F$, so that we get an I $\times J$-matrix M(f), knowing that we may occasionally suffer from this decision! When I and $J$ are finite, and say, when |I| $= m$ and |J| $= n$, the linear map $f$ is determined by the matrix M(f) whose entries in the $j$-th column are the components of the
$$125$$

<!-- PAGE 126 -->
vector $f(u_{j})$ over the basis $(v_{1}, \dots  , v_{m})$, that is, the matrix
$$M(f) = \begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{m n} \end{pmatrix}$$
whose entry on Row $i$ and Column $j$ is $a_{i j} (1 \le i \le m, 1 \le j \le n)$. We will now show that when $E$ and $F$ have finite dimension, linear maps can be very conveniently represented by matrices, and that composition of linear maps corresponds to matrix multiplication. We will follow rather closely an elegant presentation method due to Emil Artin. Let $E$ and $F$ be two vector spaces, and assume that $E$ has a finite basis $(u_{1}, \dots  , u_{n})$ and that $F$ has a finite basis $(v_{1}, \dots  , v_{m})$. Recall that we have shown that every vector $x \in E$ can be written in a unique way as
$$x = x_{1}u_{1} + \cdots  + x_{n}u_{n},$$
and similarly every vector $y \in F$ can be written in a unique way as
$$y = y_{1}v_{1} + \cdots  + y_{m}v_{m}.$$
Let $f$ : $E \to F$ be a linear map between $E$ and $F$. Then for every $x = x_{1}u_{1} + \cdots  + x_{n}u_{n}$ in $E$, by linearity, we have
$$f(x) = x_{1}f(u_{1}) + \cdots  + x_{n}f(u_{n}).$$
Let
$$f(u_{j}) = a_{1j}v_{1} + \cdots  + a_{m j}v_{m},$$
or more concisely,
$$f(u_{j}) = \sum_{i=1}^{m}  a_{i j}v_{i},$$
for every $j, 1 \le j \le n$. This can be expressed by writing the coefficients $a_{1j}, a_{2j}, \dots  , a_{mj}$ of $f(u_{j})$ over the basis $(v_{1}, \dots  , v_{m})$, as the jth column of a matrix, as shown below:
$$f(u_{1})f(u_{2})\dots f(u_{n})$$
$$v_{1}$$
$$v_{2}\vdots \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{pmatrix} .$$
$$v_{m}$$
Then substituting the right-hand side of each $f(u_{j})$ into the expression for f(x), we get
$$f(x) = x_{1}( \sum_{i=1}^{m}  a_{i1}v_{i}) + \cdots  + x_{n}( \sum_{i=1}^{m}  a_{i n}v_{i}),$$

<!-- PAGE 127 -->
which, by regrouping terms to obtain a linear combination of the $v_{i}$, yields
$$f(x) = ( \sum_{j=1}^{n}  a_{1j}x_{j})v_{1} + \cdots  + ( \sum_{j=1}^{n}  a_{m j}x_{j})v_{m}.$$
Thus, letting f(x) $= y = y_{1}v_{1} + \cdots  + y_{m}v_{m}$, we have
$$y_{i} = \sum_{j=1}^{n}  a_{i j}x_{j}(1)$$
for all $i, 1 \le i \le m$. To make things more concrete, let us treat the case where $n = 3$ and $m = 2$. In this case,
$$f(u_{1}) = a_{11}v_{1} + a_{21}v_{2}$$
$$f(u_{2}) = a_{12}v_{1} + a_{22}v_{2}$$
$$f(u_{3}) = a_{13}v_{1} + a_{23}v_{2},$$
which in matrix form is expressed by
$$f(u_{1})f(u_{2})f(u_{3})$$
$$v_{1}$$
$$v_{2} \begin{pmatrix} a \\ 11 & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{pmatrix} ,$$
and for any $x = x_{1}u_{1} + x_{2}u_{2} + x_{3}u_{3}$, we have
$$f(x) = f(x_{1}u_{1} + x_{2}u_{2} + x_{3}u_{3})$$
$$= x_{1}f(u_{1}) + x_{2}f(u_{2}) + x_{3}f(u_{3})$$
$$= x_{1}(a_{11}v_{1} + a_{21}v_{2}) + x_{2}(a_{12}v_{1} + a_{22}v_{2}) + x_{3}(a_{13}v_{1} + a_{23}v_{2})$$
$$= (a_{11}x_{1} + a_{12}x_{2} + a_{13}x_{3})v_{1} + (a_{21}x_{1} + a_{22}x_{2} + a_{23}x_{3})v_{2}.$$
Consequently, since
$$y = y_{1}v_{1} + y_{2}v_{2},$$
we have
$$y_{1} = a_{11}x_{1} + a_{12}x_{2} + a_{13}x_{3}$$
$$y_{2} = a_{21}x_{1} + a_{22}x_{2} + a_{23}x_{3}.$$
This agrees with the matrix equation
$$\begin{pmatrix} y_{1} \\ y_{2} \end{pmatrix} = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \end{pmatrix} .$$
We now formalize the representation of linear maps by matrices.

<!-- PAGE 128 -->

> **Definition 4.1.** Let $E$ and $F$ be two vector spaces, and let $(u_{1}, \dots  , u_{n})$ be a basis for $E$, and $(v_{1}, \dots  , v_{m})$ be a basis for $F$. Each vector $x \in E$ expressed in the basis $(u_{1}, \dots  , u_{n})$ as $x = x_{1}u_{1} + \cdots  + x_{n}u_{n}$ is represented by the column matrix
$$M(x) = \begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix}$$
and similarly for each vector $y \in F$ expressed in the basis $(v_{1}, \dots  , v_{m})$. Every linear map $f$ : $E \to F$ is represented by the matrix M(f) $= (a_{i j})$, where $a_{i j}$ is the $i$-th component of the vector $f(u_{j})$ over the basis $(v_{1}, \dots  , v_{m})$, i.e., where
$$f(u_{j}) = \sum_{i=1}^{m}  a_{i j}v_{i},for every j, 1 \le j \le n.$$
The coefficients $a_{1j}, a_{2j}, \dots  , a_{mj}$ of $f(u_{j})$ over the basis $(v_{1}, \dots  , v_{m})$ form the jth column of the matrix M(f) shown below:
$$f(u_{1})f(u_{2})\dots f(u_{n})$$
$$v_{1}$$
$$v_{2}\vdots \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{pmatrix} .$$
$$v_{m}$$
The matrix M(f) associated with the linear map $f$ : $E \to F$ is called the matrix of $f$ with respect to the bases $(u_{1}, \dots  , u_{n})$ and $(v_{1}, \dots  , v_{m})$. When $E = F$ and the basis $(v_{1}, \dots  , v_{m})$ is identical to the basis $(u_{1}, \dots  , u_{n})$ of $E$, the matrix M(f) associated with $f$ : $E \to E$ (as above) is called the matrix of $f$ with respect to the basis $(u_{1}, \dots  , u_{n})$.
Remark: As in the remark after Definition 3.12, there is no reason to assume that the vectors in the bases $(u_{1}, \dots  , u_{n})$ and $(v_{1}, \dots  , v_{m})$ are ordered in any particular way. However, it is often convenient to assume the natural ordering. When this is so, authors sometimes refer to the matrix M(f) as the matrix of $f$ with respect to the ordered bases $(u_{1}, \dots  , u_{n})$ and $(v_{1}, \dots  , v_{m})$. Let us illustrate the representation of a linear map by a matrix in a concrete situation. Let $E$ be the vector $space\mathbb{R}[x]_{4}$ of polynomials of degree at most $4$, let $F$ be the vector space $\mathbb{R}[x]_{3}$ of polynomials of degree at most $3$, and let the linear map be the derivative map $d$: that is,
$$d(P + Q) = dP + dQ$$
$$d(\lambda P) = \lambda dP,$$

<!-- PAGE 129 -->
with $\lambda  \in \mathbb{R}$. We choose $(1, x, x^{2}, x^{3}, x^{4})$ as a basis of $E$ and $(1, x, x^{2}, x^{3})$ as a basis of $F$. Then the $4 \times  5$ matrix $D$ associated with $d$ is obtained by expressing the derivative $dx^{i}$ of each basis vector $x^{i}$ for $i = 0, 1, 2, 3, 4$ over the basis $(1, x, x^{2}, x^{3})$. We find
$$D = \begin{pmatrix} 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 & 0 \\ 0 & 0 & 0 & 3 & 0 \\ 0 & 0 & 0 & 0 & 4 \end{pmatrix} .$$
If $P$ denotes the polynomial
$$P = 3x^{4}-5x^{3}+ x^{2}-7x + 5,$$
we have
$$dP = 12x^{3}-15x^{2}+ 2x -7.$$
The polynomial $P$ is represented by the vector $(5, -7, 1, -5, 3)$, the polynomial dP is represented by the vector $(-7, 2$, -15, $12)$, and we have
$$\begin{pmatrix} 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 & 0 \\ 0 & 0 & 0 & 3 & 0 \\ 0 & 0 & 0 & 0 & 4 \end{pmatrix} \begin{pmatrix} 5 \\ -7 \\ 1 \\ -5 \\ 3 \end{pmatrix} = \begin{pmatrix} -7 \\ 2 \\ -15 \\ 12 \end{pmatrix} ,$$
as expected! The kernel (nullspace) of $d$ consists of the polynomials of degree $0$, that is, the constant polynomials. Therefore dim(Ker $d) = 1$, and from
$$\dim(E) = \dim(\mathrm{Ker} d) + \dim(\mathrm{Im} d)$$
(see Theorem 6.16), we get dim(Im $d) = 4$ (since dim(E) $= 5)$. For fun, let us figure out the linear map from the vector space $\mathbb{R}[x]_{3}$ to the vector space $\mathbb{R}[x]_{4}$ given by integration (finding the primitive, or anti-derivative) of $x^{i}$, for $i = 0, 1, 2, 3)$.
$$The 5 \times  4 matrix S representing \int  with respect to the same bases as before is$$
$$S = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1/2 & 0 & 0 \\ 0 & 0 & 1/3 & 0 \\ 0 & 0 & 0 & 1/4 \end{pmatrix} .$$
We verify that $DS = I_{4}$,
$$\begin{pmatrix} 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 & 0 \\ 0 & 0 & 0 & 3 & 0 \\ 0 & 0 & 0 & 0 & 4 \end{pmatrix} \begin{pmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1/2 & 0 & 0 \\ 0 & 0 & 1/3 & 0 \\ 0 & 0 & 0 & 1/4 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
