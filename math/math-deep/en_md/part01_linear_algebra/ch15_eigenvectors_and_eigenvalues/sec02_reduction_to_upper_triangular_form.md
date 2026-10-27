# Reduction to Upper Triangular Form


<!-- PAGE 577 -->

## 15.2 Reduction to Upper Triangular Form

Unfortunately, not every linear map on a complex vector space can be diagonalized. The next best thing is to “triangularize,” which means to find a basis over which the matrix has zero entries below the main diagonal. Fortunately, such a basis always exist. We say that a square matrix $A$ is an upper triangular matrix if it has the following shape,
$$\begin{pmatrix} a_{1 1} & a_{1 2} & a_{1 3} & \dots & a_{1n-1} & a_{1n} \\ 0 & a_{2 2} & a_{2 3} & \dots & a_{2n-1} & a_{2n} \\ 0 & 0 & a_{3 3} & \dots & a_{3n-1} & a_{3n} \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \dots & a_{n-1n-1} & a_{n-1n} \\ 0 & 0 & 0 & \dots & 0 & a_{n n} \end{pmatrix} ,$$
i.e., $a_{i j} = 0$ whenever $j < i, 1 \le i, j \le n$.

> **Theorem 15.5.** Given any finite dimensional vector space over a field $K$, for any linear map $f$ : $E \to E$, there is a basis $(u_{1}, \dots  , u_{n})$ with respect to which $f$ is represented by an upper triangular matrix (in $M_{n}(K))$ iff all the eigenvalues of $f$ belong to $K$. Equivalently, for every $n \times  n$ matrix $A \in M_{n}(K)$, there is an invertible matrix $P$ and an upper triangular matrix $T$ (both in $M_{n}(K))$ such that
$$A = PTP^{-1}$$
iff all the eigenvalues of $A$ belong to $K$.

*Proof.* If there is a basis $(u_{1}, \dots  , u_{n})$ with respect to which $f$ is represented by an upper triangular matrix $T$ in $M_{n}(K)$, then since the eigenvalues of $f$ are the diagonal entries of $T$, all the eigenvalues of $f$ belong to $K$. For the converse, we proceed by induction on the dimension $n$ of $E$. For $n = 1$ the result is obvious. If $n > 1$, since by assumption $f$ has all its eigenvalues in $K$, pick some eigenvalue $\lambda_{1}  \in K$ of $f$, and let $u_{1}$ be some corresponding (nonzero) eigenvector. We can find $n$ - $1$ vectors $(v_{2}, \dots  , v_{n})$ such that $(u_{1}, v_{2}, \dots  , v_{n})$ is a basis of $E$, and let $F$ be the subspace of dimension $n$ - $1$ spanned by $(v_{2}, \dots  , v_{n})$. In the basis $(u_{1}, v_{2} \dots  , v_{n})$, the matrix of $f$ is of the form
$$U = \begin{pmatrix} \lambda_{1} & a_{1 2} & \dots & a_{1n} \\ 0 & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & a_{n2} & \dots & a_{n n} \end{pmatrix} ,$$
since its first column contains the coordinates of $\lambda_{1} u_{1}$ over the basis $(u_{1}, v_{2}, \dots  , v_{n})$. If we let $p: E \to F$ be the projection defined such that $p(u_{1}) = 0$ and $p(v_{i}) = v_{i}$ when $2 \le i \le n$, the linear map $g: F \to F$ defined as the restriction of $p \circ f$ to $F$ is represented by the

<!-- PAGE 578 -->
$(n$ - $1) \times  (n$ - $1)$ matrix $V = (a_{i j})_{2\le i,j\le n}$ over the basis $(v_{2}, \dots  , v_{n})$. We need to prove that all the eigenvalues of $g$ belong to $K$. However, since the entries in the first column of $U$ are all zero for $i = 2, \dots  , n$, we get
$$\chi_{U} (X) = \det(XI -U) = (X -\lambda_{1} ) \det(XI -V ) = (X -\lambda_{1} )\chi_{V}  (X),$$
where $\chi_{U} (X)$ is the characteristic polynomial of $U$ and $\chi_{V}  (X)$ is the characteristic polynomial of $V$ . It follows that $\chi_{V}  (X)$ divides $\chi_{U} (X)$, and since all the roots of $\chi_{U} (X)$ are in $K$, all the roots of $\chi_{V}  (X)$ are also in $K$. Consequently, we can apply the induction hypothesis, and there is a basis $(u_{2}, \dots  , u_{n})$ of $F$ such that $g$ is represented by an upper triangular matrix $(b_{i j})_{1\le i,j\le n-1}$. However,
$$E = Ku_{1} \oplus F,$$
and thus $(u_{1}, \dots  , u_{n})$ is a basis for $E$. Since $p$ is the projection from $E = Ku_{1} \oplus F$ onto $F$ and $g: F \to F$ is the restriction of $p \circ f$ to $F$, we have
$$f(u_{1}) = \lambda_{1} u_{1}$$
and
$$f(u_{i+1}) = a_{1i}u_{1} + \sum_{j=1}^{i}  b_{i j}u_{j+1}$$
for some $a_{1i} \in K$, when $1 \le i \le$ n-1. But then the matrix of $f$ with respect to $(u_{1}, \dots  , u_{n})$ is upper triangular. For the matrix version, we assume that $A$ is the matrix of $f$ with respect to some basis, Then we just proved that there is a change of basis matrix $P$ such that $A = PTP^{-1}$ where $T$ is upper triangular. If $A = PTP^{-1}$ where $T$ is upper triangular, note that the diagonal entries of $T$ are the eigenvalues $\lambda_{1} , \dots  , \lambda_{n}$  of $A$. Indeed, $A$ and $T$ have the same characteristic polynomial. Also, if $A$ is a real matrix whose eigenvalues are all real, then $P$ can be chosen to real, and if $A$ is a rational matrix whose eigenvalues are all rational, then $P$ can be chosen rational. Since any polynomial over $\mathbb{C}$ has all its roots in $\mathbb{C}$, Theorem 15.5 implies that every complex $n \times  n$ matrix can be triangularized. If $E$ is a Hermitian space (see Chapter $14)$, the proof of Theorem 15.5 can be easily adapted to prove that there is an orthonormal basis $(u_{1}, \dots  , u_{n})$ with respect to which the matrix of $f$ is upper triangular. This is usually known as Schur’s lemma.

> **Theorem 15.6.** (Schur decomposition) Given any linear map $f$ : $E \to E$ over a complex Hermitian space $E$, there is an orthonormal basis $(u_{1}, \dots  , u_{n})$ with respect to which $f$ is represented by an upper triangular matrix. Equivalently, for every $n \times  n$ matrix $A \in M_{n}(\mathbb{C})$, there is a unitary matrix $U$ and an upper triangular matrix $T$ such that
$$A = UTU^{*} .$$

<!-- PAGE 579 -->
If $A$ is real and if all its eigenvalues are real, then there is an orthogonal matrix $Q$ and a real upper triangular matrix $T$ such that
$$A = QTQ^{\top}.$$

*Proof.* During the induction, we choose $F$ to be the orthogonal complement of $\mathbb{C} u_{1}$ and we pick orthonormal bases (use Propositions 14.13 and 14.12). If $E$ is a real Euclidean space and if the eigenvalues of $f$ are all real, the proof also goes through with real matrices (use Propositions 12.11 and 12.10). If $\lambda$  is an eigenvalue of the matrix $A$ and if $u$ is an eigenvector associated with $\lambda$ , from
$$Au = \lambda u,$$
we obtain
$$A^{2}u = A(Au) = A(\lambda u) = \lambda Au = \lambda^{2} u,$$
which shows that $\lambda^{2}$ is an eigenvalue of $A^{2}$ for the eigenvector $u$. An obvious induction shows that $\lambda^{k}$ is an eigenvalue of $A^{k}$ for the eigenvector $u$, for all $k \ge 1$. Now, if all eigenvalues $\lambda_{1} , \dots  , \lambda_{n}$  of $A$ are in $K$, it follows that $\lambda_{1}^{k} , \dots  , \lambda_{n}^{k}$  are eigenvalues of $A^{k}$. However, it is not obvious that $A^{k}$ does not have other eigenvalues. In fact, this can’t happen, and this can be proven using Theorem 15.5.

> **Proposition 15.7.** Given any $n \times  n$ matrix $A \in M_{n}(K)$ with coefficients in a field $K$, if all eigenvalues $\lambda_{1} , \dots  , \lambda_{n}$  of $A$ are in $K$, then for every polynomial q(X) $\in$ K[X], the eigenvalues of q(A) are exactly $(q(\lambda_{1}$ ), $\dots  , q(\lambda_{n}$ )).

*Proof.* By Theorem 15.5, there is an upper triangular matrix $T$ and an invertible matrix $P$ (both in $M_{n}(K))$ such that
$$A = PTP^{-1} .$$
Since $A$ and $T$ are similar, they have the same eigenvalues (with the same multiplicities), so the diagonal entries of $T$ are the eigenvalues of $A$. Since
$$A^{k}= PT^{k}P^{-1},k \ge 1,$$
for any polynomial q(X) $= c_{0}X^{m} + \cdots  + c_{m-1}X + c_{m}$, we have
$$q(A) = c_{0}A^{m}+ \cdots  + c_{m-1}A + c_{m}I$$
$$= c_{0}PT^{m}P^{-1}+ \cdots  + c_{m-1}PTP^{-1}+ c_{m}PIP^{-1}$$
$$= P(c_{0}T^{m}+ \cdots  + c_{m-1}T + c_{m}I)P^{-1}$$
$$= Pq(T)P^{-1} .$$
Furthermore, it is easy to check that q(T) is upper triangular and that its diagonal entries are $q(\lambda_{1}$ ), $\dots  , q(\lambda_{n}$ ), where $\lambda_{1} , \dots  , \lambda_{n}$  are the diagonal entries of $T$, namely the eigenvalues of $A$. It follows that $q(\lambda_{1}$ ), $\dots  , q(\lambda_{n}$ ) are the eigenvalues of q(A).

<!-- PAGE 580 -->
$$Remark: There is another way to prove Proposition 15.7 that does \frac{not}{K} use Theorem 15.5,$$
but instead uses the fact that given any field $K$, there is field extension  of $K (K \subseteq \overline{K})$ such that every polynomial q(X) $= c_{0}X^{m} + \cdots  + c_{m-1}X + c_{m}$ (of degree $m \ge 1)$ with coefficients $c_{i} \in K$ factors as
$$q(X) = c_{0}(X -\alpha_{1} ) \cdots  (X -\alpha_{n} ),\alpha_{i}  \in \overline{K, i} = 1, \dots  , n.$$
The field $\overline{K}$ is called an algebraically closed field (and an algebraic closure of $K)$.
$$Assume that all \frac{eigenvalues}{K} \lambda_{1} , \dots  , \lambda_{n}  of A belong to K. Let q(X) be any polynomial$$
$$(in K[X]) and let \mu  \in  be any eigenvalue of q(A) \frac{(this}{K} means that \mu  is a zero of the$$
characteristic polynomial $\chi_{q(A)} (X) \in$ K[X] of q(A). Since  is algebraically closed, $\chi_{q(A)} (X)$ has all its roots in $\overline{K})$. We claim that $\mu  = q(\lambda_{i}$ ) for some eigenvalue $\lambda_{i}$  of $A$.

*Proof.* (After Lax $[117]$, Chapter $6). Since\overline{K}$ is algebraically closed, the polynomial $\mu$ -q(X) factors as
$$\mu  -q(X) = c_{0}(X -\alpha_{1} ) (X -\alpha_{n} ),$$
$$for some \alpha_{i}  \in \overline{K}. Now \mu I -q(A) is a matrix in M_{n}( \frac{\cdots}{K} ), and since \mu  is an eigenvalue of q(A),$$
it must be singular. We have
$$\mu I -q(A) = c_{0}(A -\alpha_{1} I) \cdots  (A -\alpha_{n} I),$$
and since the left-hand side is singular, so is the right-hand side, which implies that some factor $A -\alpha_{i}$ I is singular. This means that $\alpha_{i}$  is an eigenvalue of $A$, say $\alpha_{i}  = \lambda_{i}$ . As $\alpha_{i}  = \lambda_{i}$ is a zero of $\mu$  - q(X), we get
$$\mu  = q(\lambda_{i} ),$$
which proves that $\mu$  is indeed of the form $q(\lambda_{i}$ ) for some eigenvalue $\lambda_{i}$  of $A$. Using Theorem 15.6, we can derive two very important results.

> **Proposition 15.8.** If $A$ is a Hermitian matrix (i.e. $A^{*} = A)$, then its eigenvalues are real and $A$ can be diagonalized with respect to an orthonormal basis of eigenvectors. In matrix terms, there is a unitary matrix $U$ and a real diagonal matrix $D$ such that $A = UDU^{*}$ . If $A$ is a real symmetric matrix (i.e. $A^{\top} = A)$, then its eigenvalues are real and $A$ can be diagonalized with respect to an orthonormal basis of eigenvectors. In matrix terms, there is an orthogonal matrix $Q$ and a real diagonal matrix $D$ such that $A = QDQ^{\top}$.

*Proof.* By Theorem 15.6, we can write $A = UTU^{*}$ where $T = (t_{ij})$ is upper triangular and $U$ is a unitary matrix. If $A^{*} = A$, we get
$$UTU^{*} = UT^{*} U^{*} ,$$
and this implies that $T = T^{*}$ . Since $T$ is an upper triangular matrix, $T^{*}$ is a lower triangular matrix, which implies that $T$ is a diagonal matrix. Furthermore, since $T = T^{*}$ , we have
