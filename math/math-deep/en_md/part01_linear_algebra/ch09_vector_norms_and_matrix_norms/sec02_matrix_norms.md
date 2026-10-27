# Matrix Norms


<!-- PAGE 349 -->
Remark: Let $P$ be a $n \times  n$ symmetric positive definite matrix. It is immediately verified that the map $x \mapsto \|x\|_{P}$ given by
$$\|x\|_{P} = (x^{\top}Px)^{1/2}$$
$$\mathbb{R}^{n}$$
is a norm on called a quadratic norm. Using some convex analysis (the L¨owner–John
$$\mathbb{R}^{n}$$
ellipsoid), it can be shown that any norm $\|\|$ on can be approximated by a quadratic norm in the sense that there is a quadratic norm $\|\|_{P}$ such that
$$\sqrt$$
$$\|x\|_{P} \le \|x\|\le \overline{n} \|x\|_{P}for all x \in \mathbb{R}^{n};$$
see Boyd and Vandenberghe $[29]$, Section 8.4.1. Next we will consider norms on matrices.

## 9.2 Matrix Norms

For simplicity of exposition, we will consider the vector spaces $M_{n}(\mathbb{R})$ and $M_{n}(\mathbb{C})$ of square $n \times  n$ matrices. Most results also hold for the spaces $M_{m,n}(\mathbb{R})$ and $M_{m,n}(\mathbb{C})$ of rectangular $m \times  n$ matrices. Since $n \times  n$ matrices can be multiplied, the idea behind matrix norms is that they should behave “well” with respect to matrix multiplication.

> **Definition 9.4.** A matrix norm $\|\|$ on the space of square $n \times  n$ matrices in $M_{n}(K)$, with $K =\mathbb{R}$ or $K =\mathbb{C}$, is a norm on the vector space $M_{n}(K)$, with the additional property called submultiplicativity that
$$\|AB\|\le \|A\|\|B\|,$$
for all $A, B \in M_{n}(K)$. A norm on matrices satisfying the above property is often called a submultiplicative matrix norm. Since $I^{2} =$ I, from $\|I\| = \|I^{2}\|\le \|I\|^{2}$, we get $\|I\|\ge 1$, for every matrix norm.
$$Before giving examples of matrix norms, we\mathbb{C} need to review \frac{some}{A} basic definitions about$$
matrices. Given any matrix $A = (a_{ij}) \in M_{m,n}($ ), the conjugate  of $A$ is the matrix such that
$$\overline{A}_{ij} =\overline{a}_{ij},1 \le i \le m, 1 \le j \le n.$$
The transpose of $A$ is the $n \times  m$ matrix $A^{\top}$ such that
$$A_{ij}^{\top} = a_{ji},1 \le i \le m, 1 \le j \le n.$$
The adjoint of $A$ is the $n \times  m$ matrix $A^{*}$ such that
$$A^{*}\overline{= (}\overline{A}^{\top}\overline{) = (}\overline{A})^{\top}.$$
When $A$ is a real matrix, $A^{*} = A^{\top}$. A matrix $A \in M_{n}(\mathbb{C})$ is Hermitian if
$$A^{*}= A.$$

<!-- PAGE 350 -->
If $A$ is a real matrix $(A \in M_{n}(\mathbb{R}))$, we say that $A$ is symmetric if
$$A^{\top}= A.$$
A matrix $A \in M_{n}(\mathbb{C})$ is normal if
$$AA^{*}= A^{*}A,$$
and if $A$ is a real matrix, it is normal if
$$AA^{\top}= A^{\top}A.$$
A matrix $U \in M_{n}(\mathbb{C})$ is unitary if
$$UU^{*} = U^{*} U = I.$$
A real matrix $Q \in M_{n}(\mathbb{R})$ is orthogonal if
$$QQ^{\top}= Q^{\top}Q = I.$$
Given any matrix $A = (a_{ij}) \in M_{n}(\mathbb{C})$, the trace tr(A) of $A$ is the sum of its diagonal elements
$$\mathrm{tr}(A) = a_{11} + \cdots  + a_{nn}.$$
It is easy to show that the trace is a linear map, so that
$$\mathrm{tr}(\lambda A) = \lambda \mathrm{tr}(A)$$
and
$$\mathrm{tr}(A + B) = \mathrm{tr}(A) + \mathrm{tr}(B).$$
Moreover, if $A$ is an $m \times  n$ matrix and $B$ is an $n \times  m$ matrix, it is not hard to show that
$$\mathrm{tr}(AB) = \mathrm{tr}(BA).$$
We also review eigenvalues and eigenvectors. We content ourselves with definition involving matrices. A more general treatment will be given later on (see Chapter $15)$.

> **Definition 9.5.** Given any square matrix $A \in M_{n}(\mathbb{C})$, a complex number $\lambda  \in \mathbb{C}$ is an eigenvalue of $A$ if there is some nonzero vector $u \in \mathbb{C}^{n}$, such that
$$Au = \lambda u.$$
$$\mathbb{C}^{n}$$
If $\lambda$  is an eigenvalue of $A$, then the nonzero vectors $u \in$ such that Au $= \lambda u$ are called eigenvectors of $A$ associated with $\lambda$ ; together with the zero vector, these eigenvectors form a
$$\mathbb{C}^{n}$$
subspace of denoted by $E_{\lambda}(A)$, and called the eigenspace associated with $\lambda$ .

<!-- PAGE 351 -->
Remark: Note that Definition 9.5 requires an eigenvector to be nonzero. A somewhat unfortunate consequence of this requirement is that the set of eigenvectors is not a subspace, since the zero vector is missing! On the positive side, whenever eigenvectors are involved, there is no need to say that they are nonzero. In contrast, even if we allow $0$ to be an eigenvector, in order for a scalar $\lambda$  to be an eigenvalue, there must be a nonzero vector $u$ such that Au $= \lambda u$. Without this restriction, since A0 $= \lambda 0 = 0$ for all $\lambda$ , every scalar would be an eigenvector, which would make the definition of an eigenvalue trivial and useless. The fact that eigenvectors are nonzero is implicitly used in all the arguments involving them, so it seems preferable (but perhaps not as elegant) to stipulate that eigenvectors should be nonzero. If $A$ is a square real matrix $A \in M_{n}(\mathbb{R})$, then we restrict Definition 9.5 to real eigenvalues $\lambda  \in \mathbb{R}$ and real eigenvectors. However, it should be noted that although every complex matrix always has at least some complex eigenvalue, a real matrix may not have any real eigenvalues. For example, the matrix
$$A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$$
has the complex eigenvalues $i$ and $-i$, but no real eigenvalues. Thus, typically even for real matrices, we consider complex eigenvalues. Observe that $\lambda  \in \mathbb{C}$ is an eigenvalue of $A \bullet$  iff Au $= \lambda u$ for some nonzero vector $u \in \mathbb{C}^{n} \bullet  iff(\lambda$ I - A)u $= 0 \bullet$  iff the matrix $\lambda$ I - $A$ defines a linear map which has a nonzero kernel, that is, $\bullet$  iff $\lambda$ I - $A$ not invertible. However, from Proposition 7.10, $\lambda$ I - $A$ is not invertible iff
$$\det(\lambda I -A) = 0.$$
Now $det(\lambda$ I - $A)$ is a polynomial of degree $n$ in the indeterminate $\lambda$ , in fact, of the form
$$\lambda^{n} -\mathrm{tr}(A)\lambda^{n-1} + \cdots  + (-1)^{n}\det(A).$$
Thus we see that the eigenvalues of $A$ are the zeros (also called roots) of the above polynomial. Since every complex polynomial of degree $n$ has exactly $n$ roots, counted with their multiplicity, we have the following definition:

> **Definition 9.6.** Given any square $n \times  n$ matrix $A \in M_{n}(\mathbb{C})$, the polynomial
$$\det(\lambda I -A) = \lambda^{n} -\mathrm{tr}(A)\lambda^{n-1} + \cdots  + (-1)^{n}\det(A)$$

<!-- PAGE 352 -->
is called the characteristic polynomial of $A$. The $n$ (not necessarily distinct) roots $\lambda_{1} , \dots  , \lambda_{n}$ of the characteristic polynomial are all the eigenvalues of $A$ and constitute the spectrum of $A$. We let
$$\rho (A) = \max |\lambda_{i} |$$
$$1\le i\le n$$
be the largest modulus of the eigenvalues of $A$, called the spectral radius of $A$. Since the eigenvalues $\lambda_{1} , \dots  , \lambda_{n}$  of $A$ are the zeros of the polynomial
$$\det(\lambda I -A) = \lambda^{n} -\mathrm{tr}(A)\lambda^{n-1} + \cdots  + (-1)^{n}\det(A),$$
we deduce (see Section 15.1 for details) that
$$\mathrm{tr}(A) = \lambda_{1}  + \cdots  + \lambda_{n}$$
$$\det(A) = \lambda_{1}  \cdots  \lambda_{n} .$$

> **Proposition 9.7.** For any matrix norm $\|\|$ on $M_{n}(\mathbb{C})$ and for any square $n \times  n$ matrix $A \in M_{n}(\mathbb{C})$, we have
$$\rho (A) \le \|A\|.$$

*Proof.* Let $\lambda$  be some eigenvalue of $A$ for which $|\lambda$ | is maximum, that is, such that $|\lambda$ | $= \rho (A)$. If $u (\neq  0)$ is any eigenvector associated with $\lambda$  and if $U$ is the $n \times  n$ matrix whose columns are all $u$, then Au $= \lambda u$ implies
$$AU = \lambda U,$$
and since
$$|\lambda | \|U\|= \|\lambda U\|= \|AU\|\le \|A\|\|U\|$$
and $U \neq  0$, we have $\|U\|̸ = 0$, and get
$$\rho (A) = |\lambda | \le \|A\|,$$
as claimed. Proposition 9.7 also holds for any real matrix norm $\|\|$ on $M_{n}(\mathbb{R})$ but the proof is more subtle and requires the notion of induced norm. We prove it after giving Definition 9.8. It turns out that if $A$ is a real $n \times  n$ symmetric matrix, then the eigenvalues of $A$ are all real and there is some orthogonal matrix $Q$ such that
$$A = Qdiag(\lambda_{1} , \dots  , \lambda_{n} )Q^{\top},$$
where $diag(\lambda_{1} , \dots  , \lambda_{n}$ ) denotes the matrix whose only nonzero entries (if any) are its diagonal entries, which are the (real) eigenvalues of $A$. Similarly, if $A$ is a complex $n \times  n$ Hermitian matrix, then the eigenvalues of $A$ are all real and there is some unitary matrix $U$ such that
$$A = Udiag(\lambda_{1} , \dots  , \lambda_{n} )U^{*} ,$$

<!-- PAGE 353 -->
where $diag(\lambda_{1} , \dots  , \lambda_{n}$ ) denotes the matrix whose only nonzero entries (if any) are its diagonal entries, which are the (real) eigenvalues of $A$. See Chapter $17$ for the proof of these results. We now return to matrix norms. We begin with the so-called Frobenius norm, which is just the norm $\|\|_{2}$ on $\mathbb{C}^{n2}$, where the $n \times  n$ matrix $A$ is viewed as the vector obtained by concatenating together the rows (or the columns) of $A$. The reader should check that for any $n \times  n$ complex matrix $A = (a_{ij})$,
$$1/2$$
$$\begin{pmatrix} |a_{ij}|^{2} \end{pmatrix} \sum_{i,j=1}^{n}  =p\overline{\mathrm{tr}(}\overline{A}^{*}\overline{A}\overline{) =} p\overline{\mathrm{tr}(}\overline{AA}^{*}\overline{)}.$$

> **Definition 9.7.** The Frobenius norm $\|\|_{F}$ is defined so that for every square $n \times  n$ matrix $A \in M_{n}(\mathbb{C})$,
$$1/2$$
$$\|A\|_{F} = \begin{pmatrix} |a_{ij}|^{2} \end{pmatrix} \sum_{i,j=1}^{n}  =p\overline{\mathrm{tr}(}\overline{AA}^{*}\overline{) =} p\overline{\mathrm{tr}(}\overline{A}^{*}\overline{A}\overline{)}.$$
The following proposition show that the Frobenius norm is a matrix norm satisfying other nice properties.

> **Proposition 9.8.** The Frobenius norm $\|\|_{F}$ on $M_{n}(\mathbb{C})$ satisfies the following properties:
$(1)$ It is a matrix norm; that is, $\|AB\|_{F} \le \|A\|_{F} \|B\|_{F}$, for all $A, B \in M_{n}(\mathbb{C})$.
$(2)$ It is unitarily invariant, which means that for all unitary matrices $U, V$ , we have
$$\|A\|_{F} = \|UA\|_{F} = \|AV \|_{F} = \|UAV \|_{F} .$$
$$\sqrt$$
$(3) p\overline{\rho}\overline{(}\overline{A}^{*}\overline{A}\overline{)} \le \|A\|_{F} \le \overline{n} p\overline{\rho}\overline{(}\overline{A}^{*}\overline{A}\overline{)}$, for all $A \in M_{n}(\mathbb{C})$.

*Proof.* $(1)$ The only property that requires a proof is the fact $\|AB\|_{F} \le \|A\|_{F} \|B\|_{F}$. This follows from the Cauchy–Schwarz inequality:
$$2$$
$$\|AB\|_{F}^{2} = \sum_{i,j=1}^{n}  \sum_{k=1}^{n}  a_{ik}b_{kj}$$
$$\le \sum_{i,j=1}^{n}  \begin{pmatrix} |a_{ih}|^{2} \end{pmatrix} \sum_{h=1}^{n}  \begin{pmatrix} |b_{kj}|^{2} \end{pmatrix} \sum_{k=1}^{n}$$
$$= \begin{pmatrix} |a_{ih}|^{2} \end{pmatrix} \sum_{i,h=1}^{n}  \begin{pmatrix} |b_{kj}|^{2} \end{pmatrix} \sum_{k,j=1}^{n}  = \|A\|_{F}^{2} \|B\|_{F}^{2} .$$
$(2)$ We have
$$\|A\|_{F}^{2} = \mathrm{tr}(AA^{*}) = \mathrm{tr}(AV V^{*} A^{*}) = \mathrm{tr}(AV (AV )^{*}) = \|AV \|_{F}^{2} ,$$
