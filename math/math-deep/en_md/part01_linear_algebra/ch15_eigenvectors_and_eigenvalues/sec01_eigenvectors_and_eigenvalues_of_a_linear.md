# Eigenvectors and Eigenvalues of a Linear Map


<!-- PAGE 569 -->
Chapter $15$ Eigenvectors and Eigenvalues In this chapter all vector spaces are defined over an arbitrary field $K$. For the sake of concreteness, the reader may safely assume that $K =\mathbb{R}$ or $K =\mathbb{C}$.

## 15.1 Eigenvectors and Eigenvalues of a Linear Map

Given a finite-dimensional vector space $E$, let $f$ : $E \to E$ be any linear map. If by luck there is a basis $(e_{1}, \dots  , e_{n})$ of $E$ with respect to which $f$ is represented by a diagonal matrix
$$D = \begin{pmatrix} \lambda_{1} & 0 & \dots & 0 \\ 0 & \lambda_{2} & \ddots & \vdots \\ \vdots & \ddots & \ddots & 0 \\ 0 & \dots & 0 & \lambda_{n} \end{pmatrix} ,$$
then the action of $f$ on $E$ is very simple; in every “direction” $e_{i}$, we have
$$f(e_{i}) = \lambda_{i} e_{i}.$$
We can think of $f$ as a transformation that stretches or shrinks space along the direction $e_{1}, \dots  , e_{n}$ (at least if $E$ is a real vector space). In terms of matrices, the above property translates into the fact that there is an invertible matrix $P$ and a diagonal matrix $D$ such that a matrix $A$ can be factored as
$$A = PDP^{-1} .$$
When this happens, we say that $f$ (or $A)$ is diagonalizable, the $\lambda_{i}$ ’s are called the eigenvalues of $f$, and the $e_{i}’s$ are eigenvectors of $f$. For example, we will see that every symmetric matrix can be diagonalized. Unfortunately, not every matrix can be diagonalized. For example, the matrix
$$A_{1} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$
$$569$$

<!-- PAGE 570 -->
can’t be diagonalized. Sometimes a matrix fails to be diagonalizable because its eigenvalues do not belong to the field of coefficients, such as
$$A_{2} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} ,$$
whose eigenvalues are $\pm i$. This is not a serious problem because $A_{2}$ can be diagonalized over the complex numbers. However, $A_{1}$ is a “fatal” case! Indeed, its eigenvalues are both $1$ and the problem is that $A_{1}$ does not have enough eigenvectors to span $E$. The next best thing is that there is a basis with respect to which $f$ is represented by an upper triangular matrix. In this case we say that $f$ can be triangularized, or that $f$ is triangularizable. As we will see in Section 15.2, if all the eigenvalues of $f$ belong to the field of coefficients $K$, then $f$ can be triangularized. In particular, this is the case if $K =\mathbb{C}$. Now an alternative to triangularization is to consider the representation of $f$ with respect to two bases $(e_{1}, \dots  , e_{n})$ and $(f_{1}, \dots  , f_{n})$, rather than a single basis. In this case, if $K = \mathbb{R}$ or $K = \mathbb{C}$, it turns out that we can even pick these bases to be orthonormal, and we get a diagonal matrix $\Sigma$  with nonnegative entries, such that
$$f(e_{i}) = \sigma_{i} f_{i},1 \le i \le n.$$
The nonzero $\sigma_{i}$ ’s are the singular values of $f$, and the corresponding representation is the singular value decomposition, or SVD. The SVD plays a very important role in applications, and will be considered in detail in Chapter $22$. In this section we focus on the possibility of diagonalizing a linear map, and we introduce the relevant concepts to do so. Given a vector space $E$ over a field $K$, let id denote the identity map on $E$. The notion of eigenvalue of a linear map $f$ : $E \to E$ defined on an infinite-dimensional space $E$ is quite subtle because it cannot be defined in terms of eigenvectors as in the finite-dimensional case. The problem is that the map $\lambda$  id $-f$ (with $\lambda  \in \mathbb{C})$ could be noninvertible (because it is not surjective) and yet injective. In finite dimension this cannot happen, so until further notice we assume that $E$ is of finite dimension $n$.

> **Definition 15.1.** Given any vector space $E$ of finite dimension $n$ and any linear map $f$ : $E \to E$, a scalar $\lambda  \in K$ is called an eigenvalue, or proper value, or characteristic value of $f$ if there is some nonzero vector $u \in E$ such that
$$f(u) = \lambda u.$$
Equivalently, $\lambda$  is an eigenvalue of $f$ if Ker $(\lambda$  id - $f)$ is nontrivial (i.e., Ker $(\lambda$  id - $f) \neq  {0})$ iff $\lambda$  id-f is not invertible (this is where the fact that $E$ is finite-dimensional is used; a linear map from $E$ to itself is injective iff it is invertible). A vector $u \in E$ is called an eigenvector, or proper vector, or characteristic vector of $f$ if $u \neq  0$ and if there is some $\lambda  \in K$ such that
$$f(u) = \lambda u;$$

<!-- PAGE 571 -->
the scalar $\lambda$  is then an eigenvalue, and we say that $u$ is an eigenvector associated with $\lambda$ . Given any eigenvalue $\lambda  \in K$, the nontrivial subspace Ker $(\lambda$  id - $f)$ consists of all the eigenvectors associated with $\lambda$  together with the zero vector; this subspace is denoted by $E_{\lambda}(f)$, or $E(\lambda , f)$, or even by $E_{\lambda}$, and is called the eigenspace associated with $\lambda$ , or proper subspace associated with $\lambda$ . Note that distinct eigenvectors may correspond to the same eigenvalue, but distinct eigenvalues correspond to disjoint sets of eigenvectors.
Remark: As we emphasized in the remark following Definition 9.5, we require an eigenvector to be nonzero. This requirement seems to have more benefits than inconveniences, even though it may considered somewhat inelegant because the set of all eigenvectors associated with an eigenvalue is not a subspace since the zero vector is excluded. The next proposition shows that the eigenvalues of a linear map $f$ : $E \to E$ are the roots of a polynomial associated with $f$.

> **Proposition 15.1.** Let $E$ be any vector space of finite dimension $n$ and let $f$ be any linear map $f$ : $E \to E$. The eigenvalues of $f$ are the roots (in $K)$ of the polynomial
$$\det(\lambda  id -f).$$

*Proof.* A scalar $\lambda  \in K$ is an eigenvalue of $f$ iff there is some vector $u \neq  0$ in $E$ such that
$$f(u) = \lambda u$$
iff
$$(\lambda  id -f)(u) = 0$$
$iff(\lambda$  id - $f)$ is not invertible iff, by Proposition 7.13,
$$\det(\lambda  id -f) = 0.$$
In view of the importance of the polynomial $det(\lambda$  id-f), we have the following definition.

> **Definition 15.2.** Given any vector space $E$ of dimension $n$, for any linear map $f$ : $E \to E$, the polynomial $P_{f}(X) = \chi_{f} (X) =$ det(X id - $f)$ is called the characteristic polynomial of $f$. For any square matrix $A$, the polynomial $P_{A}(X) = \chi_{A} (X) =$ det(XI - $A)$ is called the characteristic polynomial of $A$. Note that we already encountered the characteristic polynomial in Section 7.7; see Definition 7.9.

<!-- PAGE 572 -->
Given any basis $(e_{1}, \dots  , e_{n})$, if $A =$ M(f) is the matrix of $f$ w.r.t. $(e_{1}, \dots  , e_{n})$, we can compute the characteristic polynomial $\chi_{f} (X) =$ det(X id - $f)$ of $f$ by expanding the following determinant:
$$X -a_{1 1}-a_{1 2}\dots -a_{1n}$$
$$-a_{2 1}X -a_{2 2}\dots -a_{2n}$$
$$\det(XI -A) =\vdots \vdots \ddots \vdots .$$
$$-a_{n1}-a_{n2}\dots X -a_{n n}$$
If we expand this determinant, we find that
$$\chi_{A} (X) = \det(XI -A) = X^{n}-(a_{1 1} + \cdots  + a_{n n})X^{n-1}+ \cdots  + (-1)^{n}\det(A).$$
The sum tr(A) $= a_{1 1} +\cdots +a_{n n}$ of the diagonal elements of $A$ is called the trace of $A$. Since we proved in Section 7.7 that the characteristic polynomial only depends on the linear map $f$, the above shows that tr(A) has the same value for all matrices $A$ representing $f$. Thus, the trace of a linear map is well-defined; we have tr(f) $=$ tr(A) for any matrix $A$ representing $f$.
Remark: The characteristic polynomial of a linear map is sometimes defined as det(f - $X$ id). Since
$$\det(f -X id) = (-1)^{n}\det(X id -f),$$
this makes essentially no difference but the version det(X id - $f)$ has the small advantage that the coefficient of $X^{n}$ is $+1$. If we write $\chi_{A} (X) =$ det(XI - $A) = X^{n}$ - $\tau_{1} (A)X^{n-1} + \cdots  + (-1)^{k}\tau_{k} (A)X^{n-k} + \cdots  + (-1)^{n}\tau_{n} (A)$, then we just proved that
$$\tau_{1} (A) = \mathrm{tr}(A)and\tau_{n} (A) = \det(A).$$
It is also possible to express $\tau_{k} (A)$ in terms of determinants of certain submatrices of $A$. For any nonempty ordered subset, $I \subseteq {1, \dots  , n}$, say $I = {i_{1} < \cdots  < i_{k}}$, let $A_{I,I}$ be the $k \times  k$ submatrix of $A$ whose jth column consists of the elements $a_{ihij}$, where $h = 1, \dots  , k$. Equivalently, $A_{I,I}$ is the matrix obtained from $A$ by first selecting the columns whose indices belong to I, and then the rows whose indices also belong to I. Then it can be shown that
$$\tau_{k} (A) = \sum_{\subseteq {1,...,n}  \det(A_{I,I});$$
$$I}$$
$$I={i1,...,ik}$$
$$i1<\cdot \cdot \cdot <ik$$

<!-- PAGE 573 -->
see Jacobson $[101]$, Section 3.10, just after Formula $(33)$. If all the roots, $\lambda_{1} , \dots  , \lambda_{n}$ , of the polynomial det(XI $-A)$ belong to the field $K$, then we can write
$$\chi_{A} (X) = \det(XI -A) = (X -\lambda_{1} ) \cdots  (X -\lambda_{n} ),$$
where some of the $\lambda_{i}$ ’s may appear more than once. Consequently, $\chi_{A} (X) =$ det(XI - $A) = X^{n}$ - $\sigma_{1} (\lambda )X^{n-1} + \cdots  + (-1)^{k}\sigma_{k} (\lambda )X^{n-k} + \cdots  + (-1)^{n}\sigma_{n} (\lambda$ ), where
$$\sigma_{k} (\lambda ) = \sum_{\subseteq {1,...,n}  \prod_{}i\in I}  \lambda_{i} ,$$
$$I$$
$$|I|=k$$
the kth elementary symmetric polynomial (or function) of the $\lambda_{i}$ ’s, where $\lambda  = (\lambda_{1} , \dots  , \lambda_{n}$ ). The elementary symmetric polynomial $\sigma_{k} (\lambda$ ) is often denoted $E_{k}(\lambda$ ), but this notation may be confusing in the context of linear algebra. For $n = 5$, the elementary symmetric polynomials are listed below:
$$\sigma_{0} (\lambda ) = 1$$
$$\sigma_{1} (\lambda ) = \lambda_{1}  + \lambda_{2}  + \lambda_{3}  + \lambda_{4}  + \lambda_{5}$$
$$\sigma_{2} (\lambda ) = \lambda_{1} \lambda_{2}  + \lambda_{1} \lambda_{3}  + \lambda_{1} \lambda_{4}  + \lambda_{1} \lambda_{5}  + \lambda_{2} \lambda_{3}  + \lambda_{2} \lambda_{4}  + \lambda_{2} \lambda_{5}$$
$$+ \lambda_{3} \lambda_{4}  + \lambda_{3} \lambda_{5}  + \lambda_{4} \lambda_{5}$$
$$\sigma_{3} (\lambda ) = \lambda_{3} \lambda_{4} \lambda_{5}  + \lambda_{2} \lambda_{4} \lambda_{5}  + \lambda_{2} \lambda_{3} \lambda_{5}  + \lambda_{2} \lambda_{3} \lambda_{4}  + \lambda_{1} \lambda_{4} \lambda_{5}$$
$$+ \lambda_{1} \lambda_{3} \lambda_{5}  + \lambda_{1} \lambda_{3} \lambda_{4}  + \lambda_{1} \lambda_{2} \lambda_{5}  + \lambda_{1} \lambda_{2} \lambda_{4}  + \lambda_{1} \lambda_{2} \lambda_{3}$$
$$\sigma_{4} (\lambda ) = \lambda_{1} \lambda_{2} \lambda_{3} \lambda_{4}  + \lambda_{1} \lambda_{2} \lambda_{3} \lambda_{5}  + \lambda_{1} \lambda_{2} \lambda_{4} \lambda_{5}  + \lambda_{1} \lambda_{3} \lambda_{4} \lambda_{5}  + \lambda_{2} \lambda_{3} \lambda_{4} \lambda_{5}$$
$$\sigma_{5} (\lambda ) = \lambda_{1} \lambda_{2} \lambda_{3} \lambda_{4} \lambda_{5} .$$
Since
$$\chi_{A} (X) = X^{n}-\tau_{1} (A)X^{n-1}+ \cdots  + (-1)^{k}\tau_{k} (A)X^{n-k}+ \cdots  + (-1)^{n}\tau_{n} (A)$$
$$= X^{n}-\sigma_{1} (\lambda )X^{n-1}+ \cdots  + (-1)^{k}\sigma_{k} (\lambda )X^{n-k}+ \cdots  + (-1)^{n}\sigma_{n} (\lambda ),$$
we have
$$\sigma_{k} (\lambda ) = \tau_{k} (A),k = 1, \dots  , n,$$
and in particular, the product of the eigenvalues of $f$ is equal to det(A) $=$ det(f), and the sum of the eigenvalues of $f$ is equal to the trace tr(A) $=$ tr(f), of $f$; for the record,
$$\mathrm{tr}(f) = \lambda_{1}  + \cdots  + \lambda_{n}$$
$$\det(f) = \lambda_{1}  \cdots  \lambda_{n} ,$$
where $\lambda_{1} , \dots  , \lambda_{n}$  are the eigenvalues of $f$ (and $A)$, where some of the $\lambda_{i}$ ’s may appear more than once. In particular, $f$ is not invertible iff it admits $0$ has an eigenvalue (since $f$ is singular iff $\lambda_{1}  \cdots  \lambda_{n}  =$ det(f) $= 0)$.

<!-- PAGE 574 -->
Remark: Depending on the field $K$, the characteristic polynomial $\chi_{A} (X) =$ det(XI - $A)$ may or may not have roots in $K$. This motivates considering algebraically closed fields, which are fields $K$ such that every polynomial with coefficients in $K$ has all its root in $K$. For example, over $K =\mathbb{R}$, not every polynomial has real roots. If we consider the matrix
$$A = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} ,$$
then the characteristic polynomial det(XI - $A)$ has no real roots unless $\theta  = k\pi$ . However, over the field $\mathbb{C}$ of complex numbers, every polynomial has roots. For example, the matrix above has the roots cos $\theta  \pm  i$ sin $\theta  = e^{\pm i\theta}$.
Remark: It is possible to show that every linear map $f$ over a complex vector space $E$ must have some (complex) eigenvalue without having recourse to determinants (and the characteristic polynomial). Let $n =$ dim(E), pick any nonzero vector $u \in E$, and consider the sequence
$$u, f(u), f^{2} (u), \dots  , f^{n} (u).$$
Since the above sequence has $n + 1$ vectors and $E$ has dimension $n$, these vectors must be linearly dependent, so there are some complex numbers $c_{0}, \dots  , c_{m}$, not all zero, such that
$$c_{0}f^{m} (u) + c_{1}f^{m-1} (u) + \cdots  + c_{m}u = 0,$$
where $m \le n$ is the largest integer such that the coefficient of $f^{m} (u)$ is nonzero $(m$ must exits since we have a nontrivial linear dependency). Now because the $field\mathbb{C}$ is algebraically closed, the polynomial
$$c_{0}X^{m}+ c_{1}X^{m-1}+ \cdots  + c_{m}$$
can be written as a product of linear factors as
$$c_{0}X^{m}+ c_{1}X^{m-1}+ \cdots  + c_{m} = c_{0}(X -\lambda_{1} ) \cdots  (X -\lambda_{m} )$$
for some complex numbers $\lambda_{1} , \dots  , \lambda_{m}  \in \mathbb{C}$, not necessarily distinct. But then since $c_{0} \neq  0$,
$$c_{0}f^{m} (u) + c_{1}f^{m-1} (u) + \cdots  + c_{m}u = 0$$
is equivalent to
$$(f -\lambda_{1}  id) \circ \cdots  \circ (f -\lambda_{m}  id)(u) = 0.$$
If all the linear maps $f$ - $\lambda_{i}$  id were injective, then $(f$ - $\lambda_{1}$  id) $\circ \cdots  \circ (f$ - $\lambda_{m}$  id) would be injective, contradicting the fact that $u \neq  0$. Therefore, some linear map $f$ - $\lambda_{i}$  id must have a nontrivial kernel, which means that there is some $v \neq  0$ so that
$$f(v) = \lambda_{i} v;$$
that is, $\lambda_{i}$  is some eigenvalue of $f$ and $v$ is some eigenvector of $f$. As nice as the above argument is, it does not provide a method for finding the eigenvalues of $f$, and even if we prefer avoiding determinants as much as possible, we are forced to deal with the characteristic polynomial det(X id - $f)$.

<!-- PAGE 575 -->

> **Definition 15.3.** Let $A$ be an $n \times  n$ matrix over a field $K$. Assume that all the roots of the characteristic polynomial $\chi_{A} (X) =$ det(XI - $A)$ of $A$ belong to $K$, which means that we can write
$$\det(XI -A) = (X -\lambda_{1} )^{k1}\cdots  (X -\lambda_{m} )^{km},$$
where $\lambda_{1} , \dots  , \lambda_{m}  \in K$ are the distinct roots of det(XI - $A)$ and $k_{1} + \cdots  + k_{m} = n$. The integer $k_{i}$ is called the algebraic multiplicity of the eigenvalue $\lambda_{i}$ , and the dimension of the eigenspace $E_{\lambda i} = Ker(\lambda_{i}$ I - $A)$ is called the geometric multiplicity of $\lambda_{i}$ . We denote the algebraic multiplicity of $\lambda_{i}$  by $alg(\lambda_{i}$ ), and its geometric multiplicity by $geo(\lambda_{i}$ ). By definition, the sum of the algebraic multiplicities is equal to $n$, but the sum of the geometric multiplicities can be strictly smaller.

> **Proposition 15.2.** Let $A$ be an $n\times n$ matrix over a field $K$ and assume that all the roots of the characteristic polynomial $\chi_{A} (X) =$ det(XI $-A)$ of $A$ belong to $K$. For every eigenvalue $\lambda_{i}$  of $A$ in $K$, the geometric multiplicity of $\lambda_{i}$  is always less than or equal to its algebraic multiplicity, that is,
$$geo(\lambda_{i} ) \le alg(\lambda_{i} ).$$

*Proof.* To see this, if $n_{i}$ is the dimension of the eigenspace $E_{\lambda i}$ associated with the eigenvalue $\lambda_{i}$ , we can form a basis of $K^{n}$ obtained by picking a basis of $E_{\lambda i}$ and completing this linearly independent family to a basis of $K^{n}$. With respect to this new basis, our matrix is of the form
$$A'= \begin{pmatrix} \lambda_{i} I_{ni} & B \\ 0 & D \end{pmatrix} ,$$
and a simple determinant calculation shows that
$$- - -  -$$
$$\det(XIA) = \det(XIA') = (X\lambda_{i} )^{ni}\det(XI_{n-ni}D).$$
Therefore, $(X -\lambda_{i} )^{ni}$ divides the characteristic polynomial of A', and thus, the characteristic polynomial of $A$. It follows that $n_{i}$ is less than or equal to the algebraic multiplicity of $\lambda_{i}$ . The following proposition shows an interesting property of eigenspaces.

> **Proposition 15.3.** Let $E$ be any vector space of finite dimension $n$ and let $f$ be any linear map. If $u_{1}, \dots  , u_{m}$ are eigenvectors associated with pairwise distinct eigenvalues $\lambda_{1} , \dots  , \lambda_{m}$ of $f$ (in $K)$, then the family $(u_{1}, \dots  , u_{m})$ is linearly independent.

*Proof.* Assume that $(u_{1}, \dots  , u_{m})$ is linearly dependent. Then there exists $\mu_{1} , \dots  , \mu_{k}  \in K$ such that
$$\mu_{1} u_{i1} + \cdots  + \mu_{k} u_{ik} = 0,$$
where $1 \le k \le m, \mu_{i}$  ̸ $= 0$ for all $i, 1 \le i \le k, {i_{1}, \dots  , i_{k}} \subseteq {1, \dots  , m}$, and no proper subfamily of $(u_{i1}, \dots  , u_{ik})$ is linearly dependent (in other words, we consider a dependency relation with $k$ minimal). Applying $f$ to this dependency relation, we get
$$\mu_{1} \lambda_{i1} u_{i1} + \cdots  + \mu_{k} \lambda_{ik} u_{ik} = 0,$$

<!-- PAGE 576 -->
and if we multiply the original dependency relation by $\lambda_{i1}$  and subtract it from the above, we get
$$\mu_{2} (\lambda_{i2}  -\lambda_{i1} )u_{i2} + \cdots  + \mu_{k} (\lambda_{ik}  -\lambda_{i1} )u_{ik} = 0,$$
which is a nontrivial linear dependency among a proper subfamily of $(u_{i1}, \dots  , u_{ik})$ since the $\lambda_{j}$  are all distinct and the $\mu_{i}$  are nonzero, a contradiction. As a corollary of Proposition 15.3 we have the following result.

> **Corollary 15.4.** If $\lambda_{1} , \dots  , \lambda_{m}$  are all the pairwise distinct eigenvalues of $f$ (in $K)$, where $m \le n)$, we have a direct sum
$$E_{\lambda1} \oplus \cdots  \oplus E_{\lambda m}$$
of the eigenspaces $E_{\lambda i}$. Unfortunately, it is not always the case that
$$E = E_{\lambda1} \oplus \cdots  \oplus E_{\lambda m}.$$
When it does is captured by the following definition.

> **Definition 15.4.** If all the distinct eigenvalues $\lambda_{1} , \dots  , \lambda_{m}$  of $f$ belong to $K$ and
$$E = E_{\lambda1} \oplus \cdots  \oplus E_{\lambda m},$$
we say that $f$ is diagonalizable (and similarly for any matrix associated with $f)$. Indeed, picking a basis in each $E_{\lambda i}$, we obtain a matrix which is a diagonal matrix consisting of the eigenvalues, each $\lambda_{i}$  occurring a number of times equal to the dimension of $E_{\lambda i}$. This happens if the algebraic multiplicity and the geometric multiplicity of every eigenvalue are equal. In particular, when the characteristic polynomial has $n$ distinct roots in $K$, then the geometric multiplicity and the geometric multiplicity of every eigenvalue are equal to $1$, so $f$ is diagonalizable. It can also be shown that symmetric matrices have real eigenvalues and can be diagonalized. For a negative example, we leave it as exercise to show that the matrix
$$M = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$
cannot be diagonalized, even though $1$ is an eigenvalue. The problem is that the eigenspace of $1$ only has dimension $1$. The matrix
$$A = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$$
cannot be diagonalized either, because it has no real eigenvalues, unless $\theta  = k\pi$ . However, over the field of complex numbers, it can be diagonalized.
