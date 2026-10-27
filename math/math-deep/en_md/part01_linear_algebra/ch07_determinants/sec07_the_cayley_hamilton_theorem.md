# The Cayley–Hamilton Theorem


<!-- PAGE 242 -->
matrix, by Corollary 4.6, the matrix of $f$ with respect to the basis $(v_{1}, \dots  , v_{n})$ is $P^{-1}$ M(f)P. By Proposition 7.9, we have $det(P^{-1}$ M(f)P) $= det(P^{-1}$ ) det(M(f)) det(P) $= det(P^{-1}$ ) det(P) det(M(f)) $=$ det(M(f)). Thus, det(f) is indeed independent of the basis of $E$.

> **Definition 7.8.** Given a vector space $E$ of finite dimension, for any linear map $f$ : $E \to E$, we define the determinant det(f) of $f$ as the determinant det(M(f)) of the matrix of $f$ in any basis (since, from the discussion just before this definition, this determinant does not depend on the basis). Then we have the following proposition.

> **Proposition 7.13.** Given any vector space $E$ of finite dimension $n$, a linear map $f$ : $E \to E$ is invertible iff det(f) $\neq  0$.

*Proof.* The linear map $f$ : $E \to E$ is invertible iff its matrix M(f) in any basis is invertible (by Proposition 4.2), iff det(M(f)) $\neq  0$, by Proposition 7.10. Given a vector space of finite dimension $n$, it is easily seen that the set of bijective linear maps $f$ : $E \to E$ such that det(f) $= 1$ is a group under composition. This group is a subgroup of the general linear group GL(E). It is called the special linear group (of $E)$, and it is denoted by SL(E), or when $E = K^{n}$, by SL(n, $K)$, or even by SL(n).

## 7.7 The Cayley–Hamilton Theorem

We next discuss an interesting and important application of Proposition 7.10, the Cayley– Hamilton theorem. The results of this section apply to matrices over any commutative ring $K$. First we need the concept of the characteristic polynomial of a matrix.

> **Definition 7.9.** If $K$ is any commutative ring, for every $n \times  n$ matrix $A \in M_{n}(K)$, the characteristic polynomial $P_{A}(X)$ of $A$ is the determinant
$$P_{A}(X) = \det(XI -A).$$
The characteristic polynomial $P_{A}(X)$ is a polynomial in K[X], the ring of polynomials in the indeterminate $X$ with coefficients in the ring $K$. For example, when $n = 2$, if
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} ,$$
then
$$X -a-b$$
$$-$$
$$P_{A}(X) = = X^{2}(a + d)X + ad -bc.$$
$$-cX -d$$

<!-- PAGE 243 -->
We can substitute the matrix $A$ for the variable $X$ in the polynomial $P_{A}(X)$, obtaining a matrix $P_{A}$. If we write
$$P_{A}(X) = X^{n}+ c_{1}X^{n-1}+ \cdots  + c_{n},$$
then
$$P_{A} = A^{n}+ c_{1}A^{n-1}+ \cdots  + c_{n}I.$$
We have the following remarkable theorem.

> **Theorem 7.14.** (Cayley–Hamilton) If $K$ is any commutative ring, for every $n \times  n$ matrix $A \in M_{n}(K)$, if we let
$$P_{A}(X) = X^{n}+ c_{1}X^{n-1}+ \cdots  + c_{n}$$
be the characteristic polynomial of $A$, then
$$P_{A} = A^{n}+ c_{1}A^{n-1}+ \cdots  + c_{n}I = 0.$$

*Proof.* We can view the matrix $B = XI$ - $A$ as a matrix with coefficients in the polynomial ring K[X], and then we can form the matrix $B$ which is the transpose of the matrix of
$$e$$
cofactors of elements of $B$. Each entry in $B$ is an $(n$ - $1) \times  (n$ - $1)$ determinant, and thus a
$$e$$
polynomial of degree a most $n$ - $1$, so we can write $B$ as
$$e$$
$$B = X^{n-1}B_{0} + X^{n-2}B_{1} + \cdots  + B_{n-1},$$
$$e$$
for some $n \times  n$ matrices $B_{0}, \dots  , B_{n-1}$ with coefficients in $K$. For example, when $n = 2$, we have
$$B = \begin{pmatrix} X-a & -b \\ -c & X-d \end{pmatrix} ,Be = \begin{pmatrix} X-d & b \\ c & X-a \end{pmatrix} = X \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + \begin{pmatrix} -d & b \\ c & -a \end{pmatrix} .$$
By Proposition 7.10, we have
$$BB = \det(B)I = P_{A}(X)I.$$
$$e$$
On the other hand, we have
$$BB = (XI -A)(X^{n-1}B_{0} + X^{n-2}B_{1} + \cdots  + X^{n-j-1}B_{j} + \cdots  + B_{n-1}),$$
$$e$$
and by multiplying out the right-hand side, we get
$$BB = X^{n}D_{0} + X^{n-1}D_{1} + \cdots  + X^{n-j}D_{j} + \cdots  + D_{n},$$
$$e$$
with
$$D_{0} = B_{0}$$
$$D_{1} = B_{1} -AB_{0}$$
$$\vdots$$
$$D_{j} = B_{j} -AB_{j-1}$$
$$\vdots$$
$$D_{n-1} = B_{n-1} -AB_{n-2}$$
$$D_{n} = -AB_{n-1}.$$

<!-- PAGE 244 -->
Since
$$P_{A}(X)I = (X^{n}+ c_{1}X^{n-1}+ \cdots  + c_{n})I,$$
the equality
$$X^{n}D_{0} + X^{n-1}D_{1} + \cdots  + D_{n} = (X^{n}+ c_{1}X^{n-1}+ \cdots  + c_{n})I$$
is an equality between two matrices, so it requires that all corresponding entries are equal, and since these are polynomials, the coefficients of these polynomials must be identical, which is equivalent to the set of equations
$$I = B_{0}$$
$$c_{1}I = B_{1} -AB_{0}$$
$$\vdots$$
$$c_{j}I = B_{j} -AB_{j-1}$$
$$\vdots$$
$$c_{n-1}I = B_{n-1} -AB_{n-2}$$
$$c_{n}I = -AB_{n-1},$$
for all $j$, with $1 \le j \le n$ - $1$. If, as in the table below,
$$A^{n}= A^{n}B_{0}$$
$$c_{1}A^{n-1}= A^{n-1}(B_{1} -AB_{0})$$
$$\vdots$$
$$c_{j}A^{n-j}= A^{n-j}(B_{j} -AB_{j-1})$$
$$\vdots$$
$$c_{n-1}A = A(B_{n-1} -AB_{n-2})$$
$$c_{n}I = -AB_{n-1},$$
we multiply the first equation by $A^{n}$, the last by I, and generally the $(j +$ 1)th by $A^{n-j}$, when we add up all these new equations, we see that the right-hand side adds up to $0$, and we get our desired equation
$$A^{n}+ c_{1}A^{n-1}+ \cdots  + c_{n}I = 0,$$
as claimed. As a concrete example, when $n = 2$, the matrix
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$
satisfies the equation
$$A^{2}-(a + d)A + (ad -bc)I = 0.$$

<!-- PAGE 245 -->
Most readers will probably find the proof of Theorem 7.14 rather clever but very mysterious and unmotivated. The conceptual difficulty is that we really need to understand how polynomials in one variable “act” on vectors in terms of the matrix $A$. This can be done and yields a more “natural” proof. Actually, the reasoning is simpler and more general if we free ourselves from matrices and instead consider a finite-dimensional vector space $E$ and some given linear map $f$ : $E \to E$. Given any polynomial p(X) $= a_{0}X^{n} + a_{1}X^{n-1} + \cdots  + a_{n}$ with coefficients in the field $K$, we define the linear map p(f): $E \to E$ by
$$p(f) = a_{0}f^{n}+ a_{1}f^{n-1}+ \cdots  + a_{n}id,$$
where $f^{k} = f \circ \cdots  \circ f$, the k-fold composition of $f$ with itself. Note that
$$p(f)(u) = a_{0}f^{n} (u) + a_{1}f^{n-1} (u) + \cdots  + a_{n}u,$$
for every vector $u \in E$. Then we define a new kind of scalar multiplication $\cdot$ : $K[X]\times E \to E$ by polynomials as follows: for every polynomial p(X) $\in$ K[X], for every $u \in E$,
$$p(X) \cdot  u = p(f)(u).$$
It is easy to verify that this is a “good action,” which means that
$$p \cdot  (u + v) = p \cdot  u + p \cdot  v$$
$$(p + q) \cdot  u = p \cdot  u + q \cdot  u$$
$$(pq) \cdot  u = p \cdot  (q \cdot  u)$$
$$1 \cdot  u = u,$$
for all $p, q \in$ K[X] and all $u, v \in E$. With this new scalar multiplication, $E$ is a K[X]-module. If $p = \lambda$  is just a scalar in $K$ (a polynomial of degree $0)$, then
$$\lambda  \cdot  u = (\lambda id)(u) = \lambda u,$$
which means that $K$ acts on $E$ by scalar multiplication as before. If p(X) $= X$ (the monomial $X)$, then
$$X \cdot  u = f(u).$$
Now if we pick a basis $(e_{1}, \dots  , e_{n})$ of $E$, if a polynomial p(X) $\in$ K[X] has the property that
$$p(X) \cdot  e_{i} = 0,i = 1, \dots  , n,$$
then this means that $p(f)(e_{i}) = 0$ for $i = 1, \dots  , n$, which means that the linear map p(f) vanishes on $E$. We can also check, as we did in Section 7.2, that if $A$ and $B$ are two $n \times  n$ matrices and if $(u_{1}, \dots  , u_{n})$ are any $n$ vectors, then
$$A \cdot \begin{pmatrix} u_{1} \\ B \cdot \vdots \\ u_{n} \end{pmatrix} \begin{pmatrix}\end{pmatrix} = (AB) \cdot \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} .$$

<!-- PAGE 246 -->
This suggests the plan of attack for our second proof of the Cayley–Hamilton theorem. For simplicity, we prove the theorem for vector spaces over a field. The proof goes through for a free module over a commutative ring.

> **Theorem 7.15.** (Cayley–Hamilton) For every finite-dimensional vector space over a field $K$, for every linear map $f$ : $E \to E$, for every basis $(e_{1}, \dots  , e_{n})$, if $A$ is the matrix over $f$ over the basis $(e_{1}, \dots  , e_{n})$ and if
$$P_{A}(X) = X^{n}+ c_{1}X^{n-1}+ \cdots  + c_{n}$$
is the characteristic polynomial of $A$, then
$$P_{A}(f) = f^{n}+ c_{1}f^{n-1}+ \cdots  + c_{n}id = 0.$$

*Proof.* Since the columns of $A$ consist of the vector $f(e_{j})$ expressed over the basis $(e_{1}, \dots  , e_{n})$, we have
$$f(e_{j}) = \sum_{i=1}^{n}  a_{i j}e_{i},1 \le j \le n.$$
Using our action of K[X] on $E$, the above equations can be expressed as
$$X \cdot  e_{j} = \sum_{i=1}^{n}  a_{i j} \cdot  e_{i},1 \le j \le n,$$
which yields
$$\sum_{i=1}^{j-1}  -a_{i j} \cdot  e_{i} + (X -a_{j j}) \cdot  e_{j} + \sum_{i=j+1}^{n}  -a_{i j} \cdot  e_{i} = 0,1 \le j \le n.$$
Observe that the transpose of the characteristic polynomial shows up, so the above system can be written as
$$\begin{pmatrix} X-a_{1 1} & -a_{2 1} & \cdots & -a_{n1} \\ -a_{1 2} & X-a_{2 2} & \cdots & -a_{n2} \\ \vdots & \vdots & \vdots & \vdots \\ -a_{1n} & -a_{2n} & \cdots & X-a_{n n} \end{pmatrix} \cdot \begin{pmatrix} e_{1} \\ e_{2} \\ \vdots \\ e_{n} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix} .$$
If we let $B = XI$ - $A^{\top}$, then as in the previous proof, if $B$ is the transpose of the matrix of
$$e$$
cofactors of $B$, we have
$$BB = \det(B)I = \det(XI -A^{\top})I = \det(XI -A)I = P_{A}I.$$
$$e$$
But since
$$B \cdot \begin{pmatrix} e_{1} \\ e_{2} \\ \vdots \\ e_{n} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix} ,$$
