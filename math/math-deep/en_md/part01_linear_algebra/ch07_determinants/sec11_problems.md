# Problems


<!-- PAGE 251 -->

## 7.10 Further Readings

Thorough expositions of the material covered in Chapter 3–6 and $7$ can be found in Strang $[176, 175]$, Lax $[117]$, Lang $[113]$, Artin $[7]$, Mac Lane and Birkhoff[122], Hoffman and Kunze $[97]$, Dummit and Foote $[55]$, Bourbaki $[25, 26]$, Van Der Waerden $[185]$, Serre $[162]$, Horn and Johnson $[98]$, and Bertin $[15]$. These notions of linear algebra are nicely put to use in classical geometry, see Berger $[11, 12]$, Tisseron $[181]$ and Dieudonn´e $[49]$.

## 7.11 Problems

Problem 7.1. Prove that every transposition can be written as a product of basic transpositions.
$$\mathbb{R}^{2}$$
Problem 7.2. $(1)$ Given two vectors in of coordinates $(c_{1}-a_{1}, c_{2}-a_{2})$ and $(b_{1}-a_{1}, b_{2}-a_{2})$, prove that they are linearly dependent iff
$$a_{1}b_{1}c_{1}$$
$$a_{2}b_{2}c_{2}= 0.$$
$$111$$
$$\mathbb{R}^{3}$$
$(2)$ Given three vectors in of coordinates $(d_{1}-a_{1}, d_{2}-a_{2}, d_{3}-a_{3}), (c_{1}-a_{1}, c_{2}-a_{2}, c_{3}-a_{3})$, and $(b_{1}$ - $a_{1}, b_{2}$ - $a_{2}, b_{3}$ - $a_{3})$, prove that they are linearly dependent iff
$$a_{1}b_{1}c_{1}d_{1}$$
$$a_{2}b_{2}c_{2}d_{2}$$
$$= 0.$$
$$a_{3}b_{3}c_{3}d_{3}$$
$$1111$$
Problem 7.3. Let $A$ be the $(m + n) \times  (m + n)$ block matrix (over any field $K)$ given by
$$A = \begin{pmatrix} A_{1} & A_{2} \\ 0 & A_{4} \end{pmatrix} ,$$
where $A_{1}$ is an $m \times  m$ matrix, $A_{2}$ is an $m \times  n$ matrix, and $A_{4}$ is an $n \times  n$ matrix. Prove that det(A) $= det(A_{1}) det(A_{4})$. Use the above result to prove that if $A$ is an upper triangular $n\times n$ matrix, then det(A) $= a_{11}a_{22} \cdots  a_{nn}$.
Problem 7.4. Prove that if $n \ge 3$, then
$$\det \begin{pmatrix} 1 + x_{1}y_{1} & 1 + x_{1}y_{2} & \cdots & 1 + x_{1}y_{n} \\ 1 + x_{2}y_{1} & 1 + x_{2}y_{2} & \cdots & 1 + x_{2}y_{n} \\ \vdots & \vdots & \vdots & \vdots \\ 1 + x_{n}y_{1} & 1 + x_{n}y_{2} & \cdots & 1 + x_{n}y_{n} \end{pmatrix} = 0.$$

<!-- PAGE 252 -->
Problem 7.5. Prove that
$$14916$$
$$491625$$
$$= 0.$$
$$9162536$$
$$16253649$$
Problem 7.6. Consider the $n \times  n$ symmetric matrix
$$A = \begin{pmatrix} 1 & 2 & 0 & 0 & \dots & 0 & 0 \\ 2 & 5 & 2 & 0 & \dots & 0 & 0 \\ 0 & 2 & 5 & 2 & \dots & 0 & 0 \\ \vdots & \vdots & \ddots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 2 & 5 & 2 & 0 \\ 0 & 0 & \dots & 0 & 2 & 5 & 2 \\ 0 & 0 & \dots & 0 & 0 & 2 & 5 \end{pmatrix} .$$
$(1)$ Find an upper-triangular matrix $R$ such that $A = R^{\top}R$.
$(2)$ Prove that det(A) $= 1$.
$(3)$ Consider the sequence
$$p_{0}(\lambda ) = 1$$
$$p_{1}(\lambda ) = 1 -\lambda$$
$$p_{k}(\lambda ) = (5 -\lambda )p_{k-1}(\lambda ) -4p_{k-2}(\lambda )2 \le k \le n.$$
Prove that
$$\det(A -\lambda I) = p_{n}(\lambda ).$$
Remark: It can be shown that $p_{n}(\lambda$ ) has $n$ distinct (real) roots and that the roots of $p_{k}(\lambda$ ) separate the roots of $p_{k+1}(\lambda$ ).
Problem 7.7. Let $B$ be the $n \times  n$ matrix $(n \ge 3)$ given by
$$B = \begin{pmatrix} 1 & -1 & -1 & -1 & \cdots & -1 & -1 \\ 1 & -1 & 1 & 1 & \cdots & 1 & 1 \\ 1 & 1 & -1 & 1 & \cdots & 1 & 1 \\ 1 & 1 & 1 & -1 & \cdots & 1 & 1 \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ 1 & 1 & 1 & 1 & \cdots & -1 & 1 \\ 1 & 1 & 1 & 1 & \cdots & 1 & -1 \end{pmatrix} .$$
Prove that
$$\det(B) = (-1)^{n}(n -2)2^{n-1}.$$

<!-- PAGE 253 -->
Problem 7.8. Given a field $K$ (say $K = \mathbb{R}$ or $K = \mathbb{C})$, given any two polynomials p(X), q(X) $\in$ K[X], we says that q(X) divides p(X) (and that p(X) is a multiple of q(X)) iff there is some polynomial s(X) $\in$ K[X] such that
$$p(X) = q(X)s(X).$$
In this case we say that q(X) is a factor of p(X), and if q(X) has degree at least one, we say that q(X) is a nontrivial factor of p(X). Let f(X) and g(X) be two polynomials in K[X] with
$$f(X) = a_{0}X^{m}+ a_{1}X^{m-1}+ \cdots  + a_{m}$$
of degree $m \ge 1$ and
$$g(X) = b_{0}X^{n}+ b_{1}X^{n-1}+ \cdots  + b_{n}$$
of degree $n \ge 1$ (with $a_{0}, b_{0} \neq  0)$. You will need the following result which you need not prove: Two polynomials f(X) and g(X) with deg(f) $= m \ge 1$ and deg(g) $= n \ge 1$ have some common nontrivial factor iff there exist two nonzero polynomials p(X) and q(X) such that
$$fp = gq,$$
with deg(p) $\le n$ - $1$ and deg(q) $\le m$ - $1$.
$(1)$ Let $\mathcal{P}_{m}$ denote the vector space of all polynomials in K[X] of degree at most $m$ - $1$, and let $T$ : $\mathcal{P}_{n} \times  P_{m} \to P_{m+n}$ be the map given by
$$T(p, q) = fp + gq,p \in P_{n}, q \in P_{m},$$
where $f$ and $g$ are some fixed polynomials of degree $m \ge 1$ and $n \ge 1$. Prove that the map $T$ is linear.
$(2)$ Prove that $T$ is not injective iff $f$ and $g$ have a common nontrivial factor.
$(3)$ Prove that $f$ and $g$ have a nontrivial common factor iff R(f, $g) = 0$, where R(f, $g)$ is the determinant given by
$$a_{0}a_{1}\cdots \cdots a_{m}0\cdots \cdots \cdots \cdots 0$$
$$0a_{0}a_{1}\cdots \cdots a_{m}0\cdots \cdots \cdots 0$$
$$\cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots$$
$$\cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots$$
$$\cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots$$
$$R(f, g) =\cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots .$$
$$0\cdots \cdots \cdots \cdots 0a_{0}a_{1}\cdots \cdots a_{m}$$
$$b_{0}b_{1}\cdots \cdots \cdots \cdots \cdots b_{n}0\cdots 0$$
$$0b_{0}b_{1}\cdots \cdots \cdots \cdots \cdots b_{n}0\cdots$$
$$\cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots$$
$$0\cdots 0b_{0}b_{1}\cdots \cdots \cdots \cdots \cdots b_{n}$$

<!-- PAGE 254 -->
The above determinant is called the resultant of $f$ and $g$. Note that the matrix of the resultant is an $(n + m) \times  (n + m)$ matrix, with the first row (involving the $a_{i}s)$ occurring $n$ times, each time shifted over to the right by one column, and the $(n +$ 1)th row (involving the $b_{j}s)$ occurring $m$ times, each time shifted over to the right by one column. Hint. Express the matrix of $T$ over some suitable basis.
$(4)$ Compute the resultant in the following three cases:
(a) $m = n = 1$, and write f(X) $=$ aX $+ b$ and g(X) $=$ cX $+ d$.
$(b) m = 1$ and $n \ge 2$ arbitrary.
$(c)$ f(X) $= aX^{2} +$ bX $+ c$ and g(X) $=$ 2aX $+ b$.
$(5)$ Compute the resultant of f(X) $= X^{3} +$ pX $+ q$ and g(X) $= 3X^{2} + p$, and
$$f(X) = a_{0}X^{2}+ a_{1}X + a_{2}$$
$$g(X) = b_{0}X^{2}+ b_{1}X + b_{2}.$$
In the second case, you should get
$$4R(f, g) = (2a_{0}b_{2} -a_{1}b_{1} + 2a_{2}b_{0})^{2}-(4a_{0}a_{2} -a_{1}^{2})(4b_{0}b_{2} -b_{1}^{2}).$$
Problem 7.9. Let $A, B, C, D$ be $n \times  n$ real or complex matrices.
$(1)$ Prove that if $A$ is invertible and if $AC = CA$, then
$$\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det(AD -CB).$$
$(2)$ Prove that if $H$ is an $n \times  n$ Hadamard matrix $(n \ge 2)$, then | det(H)| $= n^{n/2}$.
$(3)$ Prove that if $H$ is an $n \times  n$ Hadamard matrix $(n \ge 2)$, then
$$\det \begin{pmatrix} H & H \\ H & -H \end{pmatrix} = (2n)^{n}.$$
Problem 7.10. Compute the product of the following determinants
$$a-b-c-dx-y-z-t$$
$$ba-dcyx-tz$$
$$cda-bztx-y$$
$$d-cbat-zyx$$
to prove the following identity (due to Euler): $(a^{2} + b^{2} + c^{2} + d^{2})(x^{2} + y^{2} + z^{2} + t^{2}) =$ (ax $+$ by $+$ cz $+ dt)^{2} +$ (ay - bx $+$ ct - $dz)^{2}$
$$+ (az -bt -cx + dy)^{2}+ (at + bz -cy -dx)^{2}.$$

<!-- PAGE 255 -->
Problem 7.11. Let $A$ be an $n \times  n$ matrix with integer entries. Prove that $A^{-1}$ exists and has integer entries if and only if det(A) $= \pm 1$.
Problem 7.12. Let $A$ be an $n \times  n$ real or complex matrix.
$(1)$ Prove that if $A^{\top} = -A (A$ is skew-symmetric) and if $n$ is odd, then det(A) $= 0$.
$(2)$ Prove that
$$0abc$$
$$-a0de$$
$$= (af -be + dc)^{2}.$$
$$-b-d0f$$
$$-c-e-f0$$
Problem 7.13. A Cauchy matrix is a matrix of the form
$$\begin{pmatrix} 1 & 1 & \cdots & 1 \\ \lambda_{1}  -\sigma_{1} & \lambda_{1}  -\sigma_{2} & \lambda_{1}  -\sigma_{n} \\ 1 & 1 & \cdots & 1 \\ \lambda_{2}  -\sigma_{1} & \lambda_{2}  -\sigma_{2} & \lambda_{2}  -\sigma_{n} \\ \vdots & \vdots & \vdots & \vdots \\ 1 & 1 & \cdots & 1 \end{pmatrix}$$
$$\lambda_{n}  -\sigma_{1} \lambda_{n}  -\sigma_{2} \lambda_{n}  -\sigma_{n}$$
where $\lambda_{i}  \neq  \sigma_{j}$ , for all $i, j$, with $1 \le i, j \le n$. Prove that the determinant $C_{n}$ of a Cauchy matrix as above is given by
$$C_{n} = \frac{(\lambda_{i} \lambda_{j} )(\sigma_{j} \sigma_{i} )}{(\lambda_{i}  -\sigma_{j} )} \prod_{i}  n \prod_{ni=1j}  i- - -.$$
$$\prod^{=2}  \prod_{j}^{=11}  n=1$$
Problem 7.14. Let $(\alpha_{1} , \dots  , \alpha_{m+1}$ ) be a sequence of pairwise distinct scalars in $\mathbb{R}$ and let $(\beta_{1} , \dots  , \beta_{m+1}$ ) be any sequence of scalars in $\mathbb{R}$, not necessarily distinct.
$(1)$ Prove that there is a unique polynomial $P$ of degree at most $m$ such that
$$P(\alpha_{i} ) = \beta_{i} ,1 \le i \le m + 1.$$
Hint. Remember Vandermonde!
$(2)$ Let $L_{i}(X)$ be the polynomial of degree $m$ given by
$$(X -\alpha_{1} ) \cdots  (X -\alpha_{i-1} )(X -\alpha_{i+1} ) \cdots  (X -\alpha_{m+1} )$$
$$L_{i}(X) =,1 \le i \le m + 1.$$
$$(\alpha_{i}  -\alpha_{1} ) \cdots  (\alpha_{i}  -\alpha_{i-1} )(\alpha_{i}  -\alpha_{i+1} ) \cdots  (\alpha_{i}  -\alpha_{m+1} )$$
The polynomials $L_{i}(X)$ are known as Lagrange polynomial interpolants. Prove that
$$L_{i}(\alpha_{j} ) = \delta_{i j} 1 \le i, j \le m + 1.$$

<!-- PAGE 256 -->
Prove that
$$P(X) = \beta_{1} L_{1}(X) + \cdots  + \beta_{m+1} L_{m+1}(X)$$
is the unique polynomial of degree at most $m$ such that
$$P(\alpha_{i} ) = \beta_{i} ,1 \le i \le m + 1.$$
$(3)$ Prove that $L_{1}(X), \dots  , L_{m+1}(X)$ are linearly independent, and that they form a basis of all polynomials of degree at most $m$. How is $1$ (the constant polynomial $1)$ expressed over the basis $(L_{1}(X), \dots  , L_{m+1}(X))$? Give the expression of every polynomial P(X) of degree at most $m$ over the basis $(L_{1}(X), \dots  , L_{m+1}(X))$.
$(4)$ Prove that the dual basis $(L_{1}^{*}, \dots  , L_{m+1}^{*})$ of the basis $(L_{1}(X), \dots  , L_{m+1}(X))$ consists of the linear forms $L_{i}^{*}$ given by
$$L_{i}^{*} (P) = P(\alpha_{i} ),$$
for every polynomial $P$ of degree at most $m$; this is simply evaluation at $\alpha_{i}$ .
