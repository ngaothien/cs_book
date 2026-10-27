# Annihilating Polynomials and the Minimal Polynomial


<!-- PAGE 1105 -->
where $\nu_{i}  = 1$ or $\nu_{i}  = 0$; see Theorem 31.16. As a corollary we obtain the Jordan form; which involves matrices of the form
$$J_{r}(\lambda ) = \begin{pmatrix} \lambda & 1 & 0 & \cdots & 0 \\ 0 & \lambda & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \ddots & \vdots \\ 0 & 0 & 0 & \ddots & 1 \\ 0 & 0 & 0 & \lambda \end{pmatrix} ,$$
$$\cdots$$
called Jordan blocks; see Theorem 31.17.

## 31.1 Annihilating Polynomials and the Minimal Poly-

$$nomial$$
Given a linear map $f$ : $E \to E$, it is easy to check that the set Ann(f) of polynomials that annihilate $f$ is an ideal. Furthermore, when $E$ is finite-dimensional, the Cayley–Hamilton Theorem implies that Ann(f) is not the zero ideal. Therefore, by Proposition 30.10, there is a unique monic polynomial $m_{f}$ that generates Ann(f). Results from Chapter $30$, especially about gcd’s of polynomials, will come handy.

> **Definition 31.1.** If $f$ : $E \to E$ is a linear map on a finite-dimensional vector space $E$, the unique monic polynomial $m_{f}(X)$ that generates the ideal Ann(f) of polynomials which annihilate $f$ (the annihilator of $f)$ is called the minimal polynomial of $f$. The minimal polynomial $m_{f}$ of $f$ is the monic polynomial of smallest degree that annihilates $f$. Thus, the minimal polynomial divides the characteristic polynomial $\chi_{f}$ , and $deg(m_{f}) \ge 1$. For simplicity of notation, we often write $m$ instead of $m_{f}$. If $A$ is any $n \times  n$ matrix, the set Ann(A) of polynomials that annihilate $A$ is the set of polynomials
$$p(X) = a_{0}X^{d}+ a_{1}X^{d-1}+ \cdots  + a_{d-1}X + a_{d}$$
such that
$$a_{0}A^{d}+ a_{1}A^{d-1}+ \cdots  + a_{d-1}A + a_{d}I = 0.$$
It is clear that Ann(A) is a nonzero ideal and its unique monic generator is called the minimal polynomial of $A$. We check immediately that if $Q$ is an invertible matrix, then $A$ and $Q^{-1}AQ$ have the same minimal polynomial. Also, if $A$ is the matrix of $f$ with respect to some basis, then $f$ and $A$ have the same minimal polynomial. The zeros (in $K)$ of the minimal polynomial of $f$ and the eigenvalues of $f$ (in $K)$ are intimately related.

> **Proposition 31.1.** Let $f$ : $E \to E$ be a linear map on some finite-dimensional vector space $E$. Then $\lambda  \in K$ is a zero of the minimal polynomial $m_{f}(X)$ of $f$ iff $\lambda$  is an eigenvalue of $f$

<!-- PAGE 1106 -->
iff $\lambda$  is a zero of $\chi_{f} (X)$. Therefore, the minimal and the characteristic polynomials have the same zeros (in $K)$, except for multiplicities.

*Proof.* First assume that $m(\lambda$ ) $= 0$ (with $\lambda  \in K$, and writing $m$ instead of $m_{f})$. If so, using polynomial division, $m$ can be factored as
$$m = (X -\lambda )q,$$
with deg(q) $<$ deg(m). Since $m$ is the minimal polynomial, q(f)̸ $= 0$, so there is some nonzero vector $v \in E$ such that $u =$ q(f)(v)̸ $= 0$. But then, because $m$ is the minimal polynomial,
$$0 = m(f)(v)$$
$$= (f -\lambda id)(q(f)(v))$$
$$= (f -\lambda id)(u),$$
which shows that $\lambda$  is an eigenvalue of $f$. Conversely, assume that $\lambda  \in K$ is an eigenvalue of $f$. This means that for some $u \neq  0$, we have f(u) $= \lambda u$. Now it is easy to show that
$$m(f)(u) = m(\lambda )u,$$
and since $m$ is the minimal polynomial of $f$, we have m(f)(u) $= 0$, so $m(\lambda )u = 0$, and since $u \neq  0$, we must have $m(\lambda$ ) $= 0$.

> **Proposition 31.2.** Let $f$ : $E \to E$ be a linear map on some finite-dimensional vector space $E$. If $f$ diagonalizable, then its minimal polynomial is a product of distinct factors of degree $1$.

*Proof.* If we assume that $f$ is diagonalizable, then its eigenvalues are all in $K$, and if $\lambda_{1} , \dots  , \lambda_{k}$ are the distinct eigenvalues of $f$, and then by Proposition 31.1, the minimal polynomial $m$ of $f$ must be a product of powers of the polynomials $(X$ - $\lambda_{i}$ ). Actually, we claim that
$$m = (X -\lambda_{1} ) \cdots  (X -\lambda_{k} ).$$
For this we just have to show that $m$ annihilates $f$. However, for any eigenvector $u$ of $f$, one of the linear maps $f$ - $\lambda_{i}$ id sends $u$ to $0$, so
$$m(f)(u) = (f -\lambda_{1} id) \circ \cdots  \circ (f -\lambda_{k} id)(u) = 0.$$
Since $E$ is spanned by the eigenvectors of $f$, we conclude that
$$m(f) = 0.$$
It turns out that the converse of Proposition 31.2 is true, but this will take a little work to establish it.
