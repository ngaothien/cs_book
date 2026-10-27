# Eigenvalues of the Matrix Exponential


<!-- PAGE 587 -->
Proposition 15.11 implies that for any diagonalizable matrix $A$, if we define $\Gamma (A)$ by
$$\Gamma (A) = \inf{cond(P) | P^{-1} AP = D},$$
then for every eigenvalue $\lambda$  of $A + \Delta A$, we have
$$\mathbb{C}^{n}$$
$$\lambda  \in \bigcup_{k=1}^{n}  {z \in | |z -\lambda_{k} | \le \Gamma (A) \|\Delta A\|}.$$

> **Definition 15.6.** The number $\Gamma (A) = inf{cond(P)$ | $P^{-1} AP = D}$ is called the conditioning of $A$ relative to the eigenvalue problem. If $A$ is a normal matrix, since by Theorem 17.22, $A$ can be diagonalized with respect to a unitary matrix $U$, and since for the spectral norm $\|U\|_{2} = 1$, we see that $\Gamma (A) = 1$. Therefore, normal matrices are very well conditionned w.r.t. the eigenvalue problem. In fact, for every eigenvalue $\lambda$  of $A + \Delta A$ (with $A$ normal), we have
$$\mathbb{C}^{n}$$
$$\lambda  \in \bigcup_{k=1}^{n}  {z \in | |z -\lambda_{k} | \le \|\Delta A\|_{2}}.$$
If $A$ and $A+\Delta A$ are both symmetric (or Hermitian), there are sharper results; see Proposition 17.28. Note that the matrix $A(\epsilon$ ) from the beginning of the section is not normal.

## 15.5 Eigenvalues of the Matrix Exponential

The Schur decomposition yields a characterization of the eigenvalues of the matrix exponential $e^{A}$ in terms of the eigenvalues of the matrix $A$. First we have the following proposition.

> **Proposition 15.12.** Let $A$ and $U$ be (real or complex) matrices and assume that $U$ is invertible. Then
$$e^{UAU-1}= Ue^{A}U^{-1} .$$

*Proof.* A trivial induction shows that
$$UA^{p}U^{-1}= (UAU^{-1})^{p},$$
and thus
$$e^{UAU-1} = \sum_{p\ge0}  \frac{(UAU^{-1})^{p}}{p!} = \sum_{p\ge0}  \frac{UA^{p}U^{-1}}{p!}$$
$$= U \sum_{p\ge0}  \frac{A^{p}}{p!} !U^{-1}  = Ue^{A}U^{-1} ,$$
as claimed.

<!-- PAGE 588 -->

> **Proposition 15.13.** Given any complex $n \times  n$ matrix $A$, if $\lambda_{1} , \dots  , \lambda_{n}$  are the eigenvalues of , then  are the eigenvalues of . Furthermore, if  is an eigenvector of $A  e^{\lambda1}, \dots  , e^{\lambda n}  e^{A}  u  A$ for $\lambda_{i}$ , then $u$ is an eigenvector of $e^{A}$ for $e^{\lambda i}$.

*Proof.* By Theorem 15.5, there is an invertible matrix $P$ and an upper triangular matrix $T$ such that
$$A = PTP^{-1} .$$
By Proposition 15.12,
$$e^{PTP-1}= Pe^{T}P^{-1} .$$
$$Tp$$
$$Note that e^{T}= \sum_{p}  \ge   is upper triangular since T^{p}is upper triangular for all p \ge 0. If$$
$\lambda_{1} , \lambda_{2} , \dots  , \lambda_{n}$  are $the^{0p!}$ diagonal entries of $T$, the properties of matrix multiplication, when combined with an induction on $p$, imply that the diagonal entries of $T^{p}$ are $\lambda_{1}^{p} , \lambda_{2}^{p} , \dots  , \lambda_{n}^{p}$ .
$$\lambda p$$
$$This in turn implies that the diagonal entries of e^{T}are \sum_{p}  \ge \overline{i} = e^{\lambda i}for 1 \le i \le n. Since$$
$A$ and $T$ are similar matrices, we know that they have $the^{0p!}$ same eigenvalues, namely the diagonal entries $\lambda_{1} , \dots  , \lambda_{n}$  of $T$. Since $e^{A} = e^{PTP-1} = Pe^{T}P^{-1}$ , and $e^{T}$ is upper triangular, we use the same argument to conclude that both $e^{A}$ and $e^{T}$ have the same eigenvalues, which are the diagonal entries of $e^{T}$, where the diagonal entries of $e^{T}$ are of the form $e^{\lambda1}, \dots  , e^{\lambda n}$. Now, if $u$ is an eigenvector of $A$ for the eigenvalue $\lambda$ , a simple induction shows that $u$ is an eigenvector of $A^{n}$ for the eigenvalue $\lambda^{n}$ , from which is follows that
$$   $$
$$e^{A}u =I + \frac{A}{1!} + \frac{A^{2}}{2!} + \frac{A^{3}}{3!} + \dots u = u + Au + \frac{A^{2}}{2!} u + \frac{A^{3}}{3!} u + \dots$$
$$  $$
$$= u + \lambda u + \frac{\lambda^{2}}{2!} u + \frac{\lambda^{3}}{3!} u + \cdots  =1 + \lambda  + \frac{\lambda^{2}}{2!} + \frac{\lambda^{3}}{3!} + \dots u = e^{\lambda}u,$$
which shows that $u$ is an eigenvector of $e^{A}$ for $e^{\lambda}$. As a consequence, we obtain the following result.

> **Proposition 15.14.** For every complex (or real) square matrix $A$, we have
$$\det(e^{A}) = e^{\mathrm{tr}(A)},$$
where tr(A) is the trace of $A$, i.e., the sum $a_{1 1} + \cdots  + a_{n n}$ of its diagonal entries.

*Proof.* The trace of a matrix $A$ is equal to the sum of the eigenvalues of $A$. The determinant of a matrix is equal to the product of its eigenvalues, and if $\lambda_{1} , \dots  , \lambda_{n}$  are the eigenvalues of $A$, then by Proposition 15.13, $e^{\lambda1}, \dots  , e^{\lambda n}$ are the eigenvalues of $e^{A}$, and thus
$$\det \begin{pmatrix} e^{A} \end{pmatrix} = e^{\lambda1}\cdots  e^{\lambda n}= e^{\lambda1+\cdot \cdot \cdot+\lambda n}= e^{\mathrm{tr}(A)},$$
as desired.
