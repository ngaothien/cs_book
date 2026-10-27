# Change of Basis Matrix


<!-- PAGE 136 -->
over the basis $(u_{1}, \dots  , u_{n})$. Since $\phi$  is represented by the column vector $\lambda^{\top}$ over the dual basis $(v_{1}^{*}, \dots  , v_{m}^{*})$, we see that $f^{\top}(\phi$ ) is represented by the column vector
$$(\lambda A)^{\top}= A^{\top}\lambda^{\top}$$
over the dual basis $(u_{1}^{*}, \dots  , u_{n}^{*})$. The matrix defining $f^{\top}$ over the dual bases $(v_{1}^{*}, \dots  , v_{m}^{*})$ and $(u_{1}^{*}, \dots  , u_{n}^{*})$ is indeed $A^{\top}$. Conceptually, we will show later (see Section 30.1) that the linear map $f^{\top}$ : $F^{*} \to E^{*}$ is defined by
$$f^{\top} (\phi ) = \phi  \circ f,$$
for all $\phi  \in F^{*}$ (remember that $\phi$ : $F \to K$, so composing $f$ : $E \to F$ and $\phi$ : $F \to K$ yields a linear form $\phi  \circ f$ : $E \to K)$.

## 4.3 Change of Basis Matrix

It is important to observe that the isomorphism $M$ : Hom(E, $F) \to M_{n,p}$ given by Proposition 4.2 depends on the choice of the bases $(u_{1}, \dots  , u_{p})$ and $(v_{1}, \dots  , v_{n})$, and similarly for the isomorphism $M$ : Hom(E, $E) \to M_{n}$, which depends on the choice of the basis $(u_{1}, \dots  , u_{n})$. Thus, it would be useful to know how a change of basis affects the representation of a linear map $f$ : $E \to F$ as a matrix. The following simple proposition is needed.

> **Proposition 4.3.** Let $E$ be a vector space, and let $(u_{1}, \dots  , u_{n})$ be a basis of $E$. For every
$$family (v_{1}, \dots  , v_{n}), let P = (a_{i j}) be the matrix defined such that v_{j} = \sum_{i}  n=1 a_{i j}u_{i}. The matrix$$
$P$ is invertible iff $(v_{1}, \dots  , v_{n})$ is a basis of $E$.

*Proof.* Note that we have $P =$ M(f), the matrix (with respect to the basis $(u_{1}, \dots  , u_{n}))$ associated with the unique linear map $f$ : $E \to E$ such that $f(u_{i}) = v_{i}$. Since $E$ has dimension $n$, by Proposition 3.20, $f$ is injective $iff(v_{1}, \dots  , v_{n})$ is linearly independent iff $(v_{1}, \dots  , v_{n})$ is a basis of $E$ iff $f$ is bijective. Assume that $P =$ M(f) is invertible. We have f(x) $= 0$ iff M(f)M(x) $=$ PM(x) $= 0$, which implies (by multiplying both sides by $P^{-1}$ ) that M(x) $= 0$, and so $x = 0$. By Proposition 3.19, $f$ is injective, and so also bijective, and thus $(v_{1}, \dots  , v_{n})$ is a basis of $E$. Conversely, assume that $(v_{1}, \dots  , v_{n})$ is a basis of $E$, which implies that $f$ is an isomorphism. Furthermore, it is obvious that the identity matrix $I_{n}$ is the matrix associated with the identity id: $E \to E$ w.r.t. any basis. Since $f$ is an isomorphism, $f \circ f^{-1} = f^{-1} \circ f =$ id, and by Proposition 4.2, we get $M(f)M(f^{-1}$ ) $= M(f^{-1}$ )M(f) $= I_{n}$, showing that $P$ is invertible and that $M(f^{-1}$ ) $= P^{-1}$ . An important corollary of Proposition 4.3 yields the following criterion for a square matrix to be invertible. This criterion was already proven in Proposition 3.16 but Proposition 4.3 yields a shorter proof.

<!-- PAGE 137 -->

> **Proposition 4.4.** A square matrix $A \in M_{n}(K)$ is invertible iff its columns $(A^{1}, \dots  , A^{n})$ are linearly independent.

*Proof.* First assume that $A$ is invertible. If $\lambda_{1} A^{1} + \cdots  + \lambda_{n} A^{n} = 0$ for some $\lambda_{1} , \dots  , \lambda_{n}  \in K$, then
$$A\lambda  = \lambda_{1} A^{1}+ \cdots  + \lambda_{n} A^{n}= 0,$$
where $\lambda$  is the column vector $\lambda  = (\lambda_{1} , \dots  , \lambda_{n}$ ). Since $A$ has an inverse $A^{-1}$, by multiplying both sides of the equation $A\lambda  = 0$ by $A^{-1}$ we obtain
$$A^{-1}A\lambda  = I_{n}\lambda  = \lambda  = A^{-1}0 = 0,$$
which shows that the columns $(A^{1}, \dots  , A^{n})$ are linearly independent. Conversely, assume that the columns $(A^{1}, \dots  , A^{n})$ are linearly independent. Since the vector space $E = K^{n}$ has dimension $n$, the vectors $(v_{1}, \dots  , v_{n}) = (A^{1}, \dots  , A^{n})$ form a basis of $K^{n}$. By definition, the matrix $A$ is defined by expressing each vector $v_{j} = A^{j}$ as the
$$n$$
$$linear combination A^{j}= \sum_{i}  a_{ij}e_{i}, where (e_{1}, \dots  , e_{n}) is the canonical basis of K^{n}, and$$
since $(v_{1}, \dots  , v_{n})$ is a $basis,^{=1}$ by Proposition 4.3, the matrix $A$ is invertible. Proposition 4.3 suggests the following definition.

> **Definition 4.3.** Given a vector space $E$ of dimension $n$, for any two bases $(u_{1}, \dots  , u_{n})$ and $(v_{1}, \dots  , v_{n})$ of $E$, let $P = (a_{i j})$ be the invertible matrix defined such that
$$v_{j} = \sum_{i=1}^{n}  a_{i j}u_{i},$$
which is also the matrix of the identity id: $E \to E$ with respect to the bases $(v_{1}, \dots  , v_{n})$ and $(u_{1}, \dots  , u_{n})$, in that order. Indeed, we express each $id(v_{j}) = v_{j}$ over the basis $(u_{1}, \dots  , u_{n})$. The coefficients $a_{1j}, a_{2j}, \dots  , a_{nj}$ of $v_{j}$ over the basis $(u_{1}, \dots  , u_{n})$ form the jth column of the matrix $P$ shown below:
$$v_{1}v_{2}\dots v_{n}$$
$$u_{1}$$
$$u_{2}\vdots \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \dots & a_{nn} \end{pmatrix} .$$
$$u_{n}$$
The matrix $P$ is called the change of basis matrix from $(u_{1}, \dots  , u_{n})$ to $(v_{1}, \dots  , v_{n})$. Clearly, the change of basis matrix from $(v_{1}, \dots  , v_{n})$ to $(u_{1}, \dots  , u_{n})$ is $P^{-1}$ . Since $P = (a_{i j})$ is the matrix of the identity id: $E \to E$ with respect to the bases $(v_{1}, \dots  , v_{n})$ and

<!-- PAGE 138 -->
$(u_{1}, \dots  , u_{n})$, given any vector $x \in E$, if $x = x_{1}u_{1} + \cdots  + x_{n}u_{n}$ over the basis $(u_{1}, \dots  , u_{n})$ and $x = x_{1}'v_{1} + \cdots  + x_{n}'v_{n}$ over the basis $(v_{1}, \dots  , v_{n})$, from Proposition 4.2, we have
$$\begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix} = \begin{pmatrix} a_{1 1} & \dots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{n1} & \dots & a_{n n} \end{pmatrix} \begin{pmatrix} x_{1}' \\ \vdots \\ x_{n}' \end{pmatrix} ,$$
showing that the old coordinates $(x_{i})$ of $x$ (over $(u_{1}, \dots  , u_{n}))$ are expressed in terms of the new coordinates $(x_{i}')$ of $x$ (over $(v_{1}, \dots  , v_{n}))$. This fact may seem wrong, but it is correct as we can reassure ourselves by doing the following computation. Suppose that $n = 2$, so that
$$v_{1} = a_{11}u_{1} + a_{21}u_{2}$$
$$v_{2} = a_{12}u_{1} + a_{22}u_{2},$$
and our matrix is
$$A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} .$$
The same vector $x$ is written as
$$x = x_{1}u_{1} + x_{2}u_{2} = x_{1}'v_{1} + x_{2}'v_{2},$$
so by substituting the expressions for $v_{1}$ and $v_{2}$ as linear combinations of $u_{1}$ and $u_{2}$, we obtain
$$x_{1}u_{1} + x_{2}u_{2} = x_{1}'v_{1} + x_{2}'v_{2}$$
$$= x_{1}'(a_{11}u_{1} + a_{21}u_{2}) + x_{2}'(a_{12}u_{1} + a_{22}u_{2})$$
$$= (a_{11}x_{1}' + a_{12}x_{2}')u_{1} + (a_{21}x_{1}' + a_{22}x_{2}')u_{2},$$
and since $u_{1}$ and $u_{2}$ are linearly independent, we must have
$$x_{1} = a_{11}x_{1}' + a_{12}x_{2}'$$
$$x_{2} = a_{21}x_{1}' + a_{22}x_{2}',$$
namely
$$\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} \begin{pmatrix} x_{1}' \\ x_{2}' \end{pmatrix} ,$$
as claimed. If the vectors $u_{1}, \dots  , u_{n}$ and the vectors $v_{1}, \dots  , v_{n}$ are vectors in $K^{n}$, then we can form the $n \times  n$ matrix $U = (u_{1} \cdots  u_{n})$ whose columns are $u_{1}, \dots  , u_{n}$ and the $n \times  n$ matrix $V = (v_{1} \cdots  v_{n})$ whose columns are $v_{1}, \dots  , v_{n}$. Then we can express the change of basis $P$ from $(u_{1}, \dots  , u_{n})$ to $(v_{1}, \dots  , v_{n})$ in terms of $U$ and $V$ . Indeeed, the equation
$$v_{j} = \sum_{i=1}^{n}  a_{ij}u_{i}$$

<!-- PAGE 139 -->
can be expressed in matrix form as
$$v_{j} = UA^{j},$$
where
$$A^{j} = \begin{pmatrix} a_{1j} \\ \vdots \\ a_{ij} \\ \vdots \\ a_{n1} \end{pmatrix}$$
is the jth column of $P$, so we get
$$V = UP,$$
which yields
$$P = U^{-1} V.$$
Now we face the painful task of assigning a “good” notation incorporating the bases $\mathcal{U} = (u_{1}, \dots  , u_{n})$ and $\mathcal{V} = (v_{1}, \dots  , v_{n})$ into the notation for the change of basis matrix from $\mathcal{U}$ to $\mathcal{V}$. Because the change of basis matrix from $\mathcal{U}$ to $\mathcal{V}$ is the matrix of the identity map $id_{E}$ with respect to the bases $\mathcal{V}$ and $\mathcal{U}$ in that order, we could denote it by $M_{V,U}(id)$ (Meyer $[129]$ uses the notation $[I]_{V,U})$. We prefer to use an abbreviation for $M_{V,U}(id)$.

> **Definition 4.4.** The change of basis matrix from $\mathcal{U}$ to $\mathcal{V}$ is denoted
$$P_{V,U}.$$
Note that
$$P_{U,V} = P_{V,U}^{-1} .$$
Then, if we write $x_{U} = (x_{1}, \dots  , x_{n})$ for the old coordinates of $x$ with respect to the basis $\mathcal{U}$ and $x_{V} = (x_{1}', \dots  , x_{n}')$ for the new coordinates of $x$ with respect to the basis $\mathcal{V}$, we have
$$x_{U} = P_{V,U} x_{V},x_{V} = P_{V,U}^{-1}  x_{U}.$$
The above may look backward, but remember that the matrix $M_{U,V}(f)$ takes input expressed over the basis $\mathcal{U}$ to output expressed over the basis $\mathcal{V}$. Consequently, $P_{V,U}$ takes input expressed over the basis $\mathcal{V}$ to output expressed over the basis $\mathcal{U}$, and $x_{U} = P_{V,U} x_{V}$ matches this point of view!  Beware that some authors (such as Artin $[7])$ define the change of basis matrix from $\mathcal{U}$ to $\mathcal{V}$ as $P_{U,V} = P_{V,U}^{-1}$ . Under this point of view, the old basis $\mathcal{U}$ is expressed in terms of the new basis $\mathcal{V}$. We find this a bit unnatural. Also, in practice, it seems that the new basis is often expressed in terms of the old basis, rather than the other way around.

<!-- PAGE 140 -->
Since the matrix $P = P_{V,U}$ expresses the new basis $(v_{1}, \dots  , v_{n})$ in terms of the old basis $(u_{1}, \dots , u_{n})$, we observe that the coordinates $(x_{i})$ of a vector $x$ vary in the opposite direction of the change of basis. For this reason, vectors are sometimes said to be contravariant. However, this expression does not make sense! Indeed, a vector in an intrinsic quantity that does not depend on a specific basis. What makes sense is that the coordinates of a vector vary in a contravariant fashion. Let us consider some concrete examples of change of bases.

> **Example 4.1.** Let $E = F =\mathbb{R}^{2}$, with $u_{1} = (1, 0), u_{2} = (0, 1), v_{1} = (1, 1)$ and $v_{2} = (-1, 1)$. The change of basis matrix $P$ from the basis $\mathcal{U} = (u_{1}, u_{2})$ to the basis $\mathcal{V} = (v_{1}, v_{2})$ is
$$P = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$$
and its inverse is
$$P^{-1}= \begin{pmatrix} 1/2 & 1/2 \\ -1/2 & 1/2 \end{pmatrix} .$$
The old coordinates $(x_{1}, x_{2})$ with respect to $(u_{1}, u_{2})$ are expressed in terms of the new coordinates $(x_{1}', x_{2}')$ with respect to $(v_{1}, v_{2})$ by
$$\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} x_{1}' \\ x_{2}' \end{pmatrix} ,$$
and the new coordinates $(x_{1}', x_{2}')$ with respect to $(v_{1}, v_{2})$ are expressed in terms of the old coordinates $(x_{1}, x_{2})$ with respect to $(u_{1}, u_{2})$ by
$$\begin{pmatrix} x_{1}' \\ x_{2}' \end{pmatrix} = \begin{pmatrix} 1/2 & 1/2 \\ -1/2 & 1/2 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} .$$

> **Example 4.2.** Let $E = F =\mathbb{R}[x]_{3}$ be the set of polynomials of degree at most $3$, and consider the $bases\mathcal{U} = (1, x, x^{2}, x^{3}) and\mathcal{V} = (B_{0}^{3}(x), B_{1}^{3}(x), B_{2}^{3}(x), B_{3}^{3}(x))$, where $B_{0}^{3}(x), B_{1}^{3}(x), B_{2}^{3}(x), B_{3}^{3}(x)$ are the Bernstein polynomials of degree $3$, given by $B_{0}^{3}(x) = (1$ - $x)^{3} B_{1}^{3}(x) =$ 3(1 - $x)^{2}x B_{2}^{3}(x) =$ 3(1 - $x)x^{2} B_{3}^{3}(x) = x^{3}$. By expanding the Bernstein polynomials, we find that the change of basis matrix $P_{V,U}$ is given by
$$P_{V,U} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ -3 & 3 & 0 & 0 \\ 3 & -6 & 3 & 0 \\ 1 & 3 & 3 & 1 \end{pmatrix} .$$
$$--$$
We also find that the inverse of $P_{V,U}$ is
$$P_{V,U}^{-1}  = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1/3 & 0 & 0 \\ 1 & 2/3 & 1/3 & 0 \\ 1 & 1 & 1 & 1 \end{pmatrix} .$$
