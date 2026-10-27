# The Basic QR Algorithm


<!-- PAGE 663 -->
than $m)$ the idea is to generate the $n \times  n$ Hessenberg submatrix $H_{n}$ of the full Hessenberg matrix $H$ (such that $A = UHU^{*}$ ) consisting of its first $n$ rows and $n$ columns; the matrix $U_{n}$ consisting of the first $n$ columns of $U$ is also produced. The Rayleigh–Ritz method consists in computing the eigenvalues of $H_{n}$ using the QR- method with shifts. These eigenvalues, called Ritz values, are approximations of the eigenvalues of $A$. Typically, extreme eigenvalues are found first. Arnoldi iteration can also be viewed as a way of computing an orthonormal basis of a Krylov subspace, namely the $subspace\mathcal{K}_{n}(A, b)$ spanned by $(b$, Ab, $\dots  , A^{n}b)$. We can also use Arnoldi iteration to find an approximate solution of a linear equation Ax $= b$ by minimizing $\|b$ - $Ax_{n}\|_{2}$ for all $x_{n}$ is the Krylov $space\mathcal{K}_{n}(A, b)$. This method named GMRES is discussed in Section 18.5. The special case where $H$ is a symmetric (or Hermitian) tridiagonal matrix is discussed in Section 18.6. In this case, Arnoldi’s algorithm becomes Lanczos’ algorithm. It is much more efficient than Arnoldi iteration. We close this chapter by discussing two classical methods for computing a single eigenvector and a single eigenvalue: power iteration and inverse (power) iteration; see Section 18.7.

## 18.1 The Basic QR Algorithm

Let $A$ be an $n \times  n$ matrix which is assumed to be diagonalizable and invertible. The basic QR algorithm makes use of two very simple steps. Starting with $A_{1} = A$, we construct sequences of matrices $(A_{k}), (Q_{k}) (R_{k})$ and $(P_{k})$ as follows:
$$FactorA_{1} = Q_{1}R_{1}$$
$$SetA_{2} = R_{1}Q_{1}$$
$$FactorA_{2} = Q_{2}R_{2}$$
$$SetA_{3} = R_{2}Q_{2}$$
$$\vdots$$
$$FactorA_{k} = Q_{k}R_{k}$$
$$SetA_{k+1} = R_{k}Q_{k}$$
$$\vdots$$
Thus, $A_{k+1}$ is obtained from a QR-factorization $A_{k} = Q_{k}R_{k}$ of $A_{k}$ by swapping $Q_{k}$ and $R_{k}$. Define $P_{k}$ by
$$P_{k} = Q_{1}Q_{2} \cdots  Q_{k}.$$
Since $A_{k} = Q_{k}R_{k}$, we have $R_{k} = Q_{k}^{*}A_{k}$, and since $A_{k+1} = R_{k}Q_{k}$, we obtain
$$A_{k+1} = Q_{k}^{*}A_{k}Q_{k}.(*_{1})$$

<!-- PAGE 664 -->
An obvious induction shows that
$$A_{k+1} = Q_{k}^{*} \cdots  Q_{1}^{*}A_{1}Q_{1} \cdots  Q_{k} = P_{k}^{*} AP_{k},$$
that is
$$A_{k+1} = P_{k}^{*}  AP_{k}.(*_{2})$$
Therefore, $A_{k+1}$ and $A$ are similar, so they have the same eigenvalues. The basic QR iteration method consists in computing the sequence of matrices $A_{k}$, and in the ideal situation, to expect that $A_{k}$ “converges” to an upper triangular matrix, more precisely that the part of $A_{k}$ below the main diagonal goes to zero, and the diagonal entries converge to the eigenvalues of $A$. This ideal situation is only achieved in rather special cases. For one thing, if $A$ is unitary (or orthogonal in the real case), since in the QR decomposition we have $R =$ I, we get $A_{2} = IQ = Q = A_{1}$, so the method does not make any progress. Also, if $A$ is a real matrix, since the $A_{k}$ are also real, if $A$ has complex eigenvalues, then the part of $A_{k}$ below the main diagonal can’t go to zero. Generally, the method runs into troubles whenever $A$ has distinct eigenvalues with the same modulus. The convergence of the sequence $(A_{k})$ is only known under some fairly restrictive hypotheses. Even under such hypotheses, this is not really genuine convergence. Indeed, it can be shown that the part of $A_{k}$ below the main diagonal goes to zero, and the diagonal entries converge to the eigenvalues of $A$, but the part of $A_{k}$ above the diagonal may not converge. However, for the purpose of finding the eigenvalues of $A$, this does not matter. The following convergence result is proven in Ciarlet $[41]$ (Chapter $6$, Theorem 6.3.10 and Serre $[162]$ (Chapter $13$, Theorem 13.2). It is rarely applicable in practice, except for symmetric (or Hermitian) positive definite matrices, as we will see shortly.

> **Theorem 18.1.** Suppose the (complex) $n\times n$ matrix $A$ is invertible, diagonalizable, and that its eigenvalues $\lambda_{1} , \dots  , \lambda_{n}$  have different moduli, so that
$$|\lambda_{1} | > |\lambda_{2} | > \cdots  > |\lambda_{n} | > 0.$$
If $A = P\Lambda P^{-1}$, where $\Lambda  = diag(\lambda_{1} , \dots  , \lambda_{n}$ ), and if $P^{-1}$ has an LU-factorization, then the strictly lower-triangular part of $A_{k}$ converges to zero, and the diagonal of $A_{k}$ converges to $\Lambda$ .

*Proof.* We reproduce the proof in Ciarlet $[41]$ (Chapter $6$, Theorem 6.3.10). The strategy is to study the asymptotic behavior of the matrices $P_{k} = Q_{1}Q_{2} \cdots  Q_{k}$. For this, it turns out that we need to consider the powers $A^{k}$. Step $1$. Let $\mathcal{R}_{k} = R_{k} \cdots  R_{2}R_{1}$. We claim that
$$A^{k}= (Q_{1}Q_{2} \cdots  Q_{k})(R_{k} \cdots  R_{2}R_{1}) = P_{k}\mathcal{R}_{k}.(*_{3})$$

<!-- PAGE 665 -->
We proceed by induction. The base case $k = 1$ is trivial. For the induction step, from $(*_{2})$, we have
$$P_{k}A_{k+1} = AP_{k}.$$
Since $A_{k+1} = R_{k}Q_{k} = Q_{k+1}R_{k+1}$, we have
$$P_{k+1}\mathcal{R}_{k+1} = P_{k}Q_{k+1}R_{k+1}\mathcal{R}_{k} = P_{k}A_{k+1}\mathcal{R}_{k} = AP_{k}\mathcal{R}_{k} = AA^{k}= A^{k+1}$$
establishing the induction step. Step $2$. We will express the matrix $P_{k}$ as $P_{k} = QQ_{k}D_{k}$, in terms of a diagonal matrix
$$e$$
$D_{k}$ with unit entries, with $Q$ and $Q_{k}$ unitary.
$$e$$
Let $P = QR$, a QR-factorization of $P$ (with $R$ an upper triangular matrix with positive diagonal entries), and $P^{-1} = LU$, an LU-factorization of $P^{-1}$. Since $A = P\Lambda P^{-1}$, we have
$$A^{k}= P\Lambda^{k} P^{-1}= QR\Lambda^{k} LU = QR(\Lambda^{k} L\Lambda^{-k} )\Lambda^{k} U.(*_{4})$$
Here, $\Lambda^{-k}$ is the diagonal matrix with entries $\lambda_{i}^{-k}$  . The reason for introducing the matrix $\Lambda^{k} L\Lambda^{-k}$ is that its asymptotic behavior is easy to determine. Indeed, we have
$$0if i < j$$
$$$$
$$$$
$$1if i = j$$
$$$$
$$(\Lambda^{k} L\Lambda^{-k} )_{ij} =$$
$$L_{ij}if i > j.$$
$$ \begin{pmatrix} \lambda_{i}^{k} \\ \lambda_{j} \end{pmatrix}$$
The hypothesis that $|\lambda_{1}$ | $> |\lambda_{2}$ | $> \cdots  > |\lambda_{n}$ | $> 0$ implies that
$$lim\Lambda^{k} L\Lambda^{-k} = I.(\dagger )$$
$$k\mapsto \infty$$
Note that it is to obtain this limit that we made the hypothesis on the moduli of the eigenvalues. We can write
$$\Lambda^{k} L\Lambda^{-k} = I + F_{k},withlimF_{k} = 0,$$
$$k\mapsto \infty$$
and consequently, since $R(\Lambda^{k} L\Lambda^{-k}$ ) $=$ R(I $+ F_{k}) = R + RF_{k}R^{-1}R =$ (I $+ RF_{k}R^{-1})R$, we have
$$R(\Lambda^{k} L\Lambda^{-k} ) = (I + RF_{k}R^{-1})R.(*_{5})$$
By Proposition 9.12(1), since $lim_{k\mapsto \infty} F_{k} = 0$, and thus $lim_{k\mapsto \infty} RF_{k}R^{-1} = 0$, the matrices I $+ RF_{k}R^{-1}$ are invertible for $k$ large enough. Consequently for $k$ large enough, we have a QR-factorization
$$I + RF_{k}R^{-1}=Q_{k}R_{k},(*_{6})$$
$$ee$$
$$e$$
with $(R_{k})_{ii} > 0$ for $i = 1, \dots  , n$. Since the matrices $Q_{k}$ are unitary, we have $Q_{k}  = 1, e  e$
$$2$$
so the sequence $(Q_{k})$ is bounded. It follows that it has a convergent subsequence $(Q_{\ell})$ that
$$e e$$
converges to some matrix $Q$, which is also unitary. Since
$$e$$
$$R_{\ell}= (Q_{\ell})^{*}(I + RF_{\ell}R^{-1}),$$
$$e e$$

<!-- PAGE 666 -->
we deduce that the subsequence $(R_{\ell})$ also converges to some matrix $R$, which is also upper
$$e e$$
triangular with positive diagonal entries. By passing to the limit (using the subsequences), we get $R = (Q)^{*}$, that is, $e  e$
$$I =QR.$$
$$e e$$
By the uniqueness of a QR-decomposition (when the diagonal entries of $R$ are positive), we get
$$Q =R = I.$$
$$e e$$
Since the above reasoning applies to any subsequences of $(Q_{k})$ and $(R_{k})$, by the uniqueness
$$e e$$
of limits, we conclude that the “full” sequences $(Q_{k})$ and $(R_{k})$ converge:
$$e e$$
$$limQ_{k} = I,limR_{k} = I.$$
$$ee$$
$$k\mapsto \infty k\mapsto \infty$$
Since by $(*_{4})$,
$$A^{k}= QR(\Lambda^{k} L\Lambda^{-k} )\Lambda^{k} U,$$
by $(*_{5})$,
$$R(\Lambda^{k} L\Lambda^{-k} ) = (I + RF_{k}R^{-1})R,$$
and by $(*_{6})$
$$I + RF_{k}R^{-1}=Q_{k}R_{k},$$
$$ee$$
we proved that
$$A^{k}= (QQ_{k})(R_{k}R\Lambda^{k} U).(*_{7})$$
$$e e$$
Observe that $QQ_{k}$ is a unitary matrix, and $R_{k}R\Lambda^{k} U$ is an upper triangular matrix, as a
$$e e$$
product of upper triangular matrices. However, some entries in $\Lambda$  may be negative, so we can’t claim that $R_{k}R\Lambda^{k} U$ has positive diagonal entries. Nevertheless, we have another
$$e$$
QR-decomposition of $A^{k}$,
$$A^{k}= (QQ_{k})(R_{k}R\Lambda^{k} U) = P_{k}\mathcal{R}_{k}.$$
$$e e$$
It is easy to prove that there is diagonal matrix $D_{k}$ with $|(D_{k})_{ii}| = 1$ for $i = 1, \dots  , n$, such that
$$P_{k} = QQ_{k}D_{k}.(*_{8})$$
$$e$$
The existence of $D_{k}$ is consequence of the following fact: If an invertible matrix $B$ has two QR factorizations $B = Q_{1}R_{1} = Q_{2}R_{2}$, then there is a diagonal matrix $D$ with unit entries such that $Q_{2} = DQ_{1}$. The expression for $P_{k}$ in $(*_{8})$ is that which we were seeking. Step $3$. Asymptotic behavior of the matrices $A_{k+1} = P_{k}^{*}  AP_{k}$. Since $A = P\Lambda P^{-1} = QR\Lambda R^{-1}Q^{-1}$ and by $(*_{8}), P_{k} = QQ_{k}D_{k}$, we get
$$e$$
$$A_{k+1} = D_{k}^{*}(Q_{k})^{*}Q^{*}QR\Lambda R^{-1}Q^{-1}QQ_{k}D_{k} = D_{k}^{*}(Q_{k})^{*}R\Lambda R^{-1}Q_{k}D_{k}.(*_{9})$$
$$e e e e$$

<!-- PAGE 667 -->
Since $lim_{k\mapsto \infty} Q_{k} =$ I, we deduce that
$$e$$
$$lim(Q_{k} e)^{*}R\Lambda R^{-1} eQ_{k} = R\Lambda R^{-1} = \begin{pmatrix} \lambda_{1} & * & \cdots & * \\ 0 & \lambda_{2} & \cdots & * \\ \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_{n} \end{pmatrix} ,$$
$$k\mapsto \infty$$
an upper triangular matrix with the eigenvalues of $A$ on the diagonal. Since $R$ is upper triangular, the order of the eigenvalues is preserved. If we let
$$\mathcal{D}_{k} = (Q_{k})^{*}R\Lambda R^{-1}Q_{k},(*_{10})$$
$$e e$$
then by $(*_{9})$ we have $A_{k+1} = D_{k}^{*}\mathcal{D}_{k}D_{k}$, and since the matrices $D_{k}$ are diagonal matrices, we have
$$(A_{k+1})_{jj} = (D_{k}^{*}\mathcal{D}_{k}D_{k})_{ij} \overline{= (}\overline{D}_{k}\overline{)}_{ii}(D_{k})_{jj}(\mathcal{D}_{k})_{ij},$$
which implies that
$$(A_{k+1})_{ii} = (\mathcal{D}_{k})_{ii},i = 1, \dots  , n,(*_{11})$$
since $|(D_{k})_{ii}| = 1$ for $i = 1, \dots  , n$. Since $lim_{k\mapsto \infty} \mathcal{D}_{k} = R\Lambda R^{-1}$, we conclude that the strictly lower-triangular part of $A_{k+1}$ converges to zero, and the diagonal of $A_{k+1}$ converges to $\Lambda$ . Observe that if the matrix $A$ is real, then the hypothesis that the eigenvalues have distinct moduli implies that the eigenvalues are all real and simple. The following Matlab program implements the basic QR-method using the function qrv4 from Section 12.8. function $T =$ qreigen(A,m) $T = A$; for $k =$ 1:m $[Q R] =$ qrv4(T); $T =$ R*Q; end end

> **Example 18.1.** If we run the function qreigen with $100$ iterations on the $8 \times  8$ symmetric matrix
$$A = \begin{pmatrix} 4 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ 1 & 4 & 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 4 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 4 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 4 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 4 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 & 4 & 1 \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 4 \end{pmatrix} ,$$

<!-- PAGE 668 -->
we find the matrix
$$T = \begin{pmatrix} 5.8794 & 0.0015 & 0.0000 & -0.0000 & 0.0000 & -0.0000 & 0.0000 & -0.0000 \\ 0.0015 & 5.5321 & 0.0001 & 0.0000 & -0.0000 & 0.0000 & 0.0000 & 0.0000 \\ 0 & 0.0001 & 5.0000 & 0.0000 & -0.0000 & 0.0000 & 0.0000 & 0.0000 \\ 0 & 0 & 0.0000 & 4.3473 & 0.0000 & 0.0000 & 0.0000 & 0.0000 \\ 0 & 0 & 0 & 0.0000 & 3.6527 & 0.0000 & 0.0000 & -0.0000 \\ 0 & 0 & 0 & 0 & 0.0000 & 3.0000 & 0.0000 & -0.0000 \\ 0 & 0 & 0 & 0 & 0 & 0.0000 & 2.4679 & 0.0000 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0.0000 & 2.1206 \end{pmatrix} .$$
The diagonal entries match the eigenvalues found by running the Matlab function eig(A). If several eigenvalues have the same modulus, then the proof breaks down, we can no longer claim $(\dagger$ ), namely that
$$lim\Lambda^{k} L\Lambda^{-k} = I.$$
$$k\mapsto \infty$$
If we assume that $P^{-1}$ has a suitable “block LU-factorization,” it can be shown that the matrices $A_{k+1}$ converge to a block upper-triangular matrix, where each block corresponds to eigenvalues having the same modulus. For example, if $A$ is a $9 \times  9$ matrix with eigenvalues $\lambda_{i}$  such that $|\lambda_{1}$ | $= |\lambda_{2}$ | $= |\lambda_{3}$ | $> |\lambda_{4}$ | $> |\lambda_{5}$ | $= |\lambda_{6}$ | $= |\lambda_{7}$ | $= |\lambda_{8}$ | $= |\lambda_{9}$ |, then $A_{k}$ converges to a block diagonal matrix (with three blocks, a $3 \times  3$ block, a $1 \times  1$ block, and a $5 \times  5$ block) of the form
$$\begin{pmatrix} ⋆ & ⋆ & ⋆ & * & * & * & * & * & * \\ ⋆ & ⋆ & ⋆ & * & * & * & * & * & * \\ ⋆ & ⋆ & ⋆ & * & * & * & * & * & * \\ 0 & 0 & 0 & ⋆ & * & * & * & * & * \\ 0 & 0 & 0 & 0 & ⋆ & ⋆ & ⋆ & ⋆ & ⋆ \\ 0 & 0 & 0 & 0 & ⋆ & ⋆ & ⋆ & ⋆ & ⋆ \\ 0 & 0 & 0 & 0 & ⋆ & ⋆ & ⋆ & ⋆ & ⋆ \\ 0 & 0 & 0 & 0 & ⋆ & ⋆ & ⋆ & ⋆ & ⋆ \\ 0 & 0 & 0 & 0 & ⋆ & ⋆ & ⋆ & ⋆ & ⋆ \end{pmatrix} .$$
See Ciarlet $[41]$ (Chapter $6$ Section 6.3) for more details. Under the conditions of Theorem 18.1, in particular, if $A$ is a symmetric (or Hermitian) positive definite matrix, the eigenvectors of $A$ can be approximated. However, when $A$ is not a symmetric matrix, since the upper triangular part of $A_{k}$ does not necessarily converge, one has to be cautious that a rigorous justification is lacking. Suppose we apply the QR algorithm to a matrix $A$ satisfying the hypotheses of Theorem

> **Theorem 18.1.** For $k$ large enough, $A_{k+1} = P_{k}^{*}  AP_{k}$ is nearly upper triangular and the diagonal entries of $A_{k+1}$ are all distinct, so we can consider that they are the eigenvalues of $A_{k+1}$, and thus of $A$. To avoid too many subscripts, write $T$ for the upper triangular matrix
