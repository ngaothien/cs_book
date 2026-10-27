# Subordinate Norms


<!-- PAGE 354 -->
and
$$\|A\|_{F}^{2} = \mathrm{tr}(A^{*}A) = \mathrm{tr}(A^{*}U^{*}UA) = \|UA\|_{F}^{2} .$$
The identity
$$\|A\|_{F} = \|UAV \|_{F}$$
follows from the previous two.
$(3)$ It is shown in Section 15.1 that the trace of a matrix is equal to the sum of its eigenvalues. Furthermore, $A^{*}A$ is symmetric positive semidefinite (which means that its eigenvalues are nonnegative), so $\rho (A^{*}A)$ is the largest eigenvalue of $A^{*}A$ and
$$\rho (A^{*}A) \le \mathrm{tr}(A^{*}A) \le n\rho (A^{*}A),$$
which yields $(3)$ by taking square roots.
Remark: The Frobenius norm is also known as the Hilbert-Schmidt norm or the Schur norm. So many famous names associated with such a simple thing!

## 9.3 Subordinate Norms

We now give another method for obtaining matrix norms using subordinate norms. First we need a proposition that shows that in a finite-dimensional space, the linear map induced by a matrix is bounded, and thus continuous.
$$\mathbb{C}^{n}  \mathbb{R}^{n}\mathbb{C}$$

> **Proposition 9.9.** For every norm $\|\|$ on (or ), for every matrix $A \in M_{n}($ ) (or $A \in M_{n}(\mathbb{R}))$, there is a real constant $C_{A} \ge 0$, such that
$$\|Au\|\le C_{A} \|u\|,$$
$$\mathbb{C}^{n} \mathbb{R}^{n}$$
for every vector $u \in$ (or $u \in$ if $A$ is real).
$$\mathbb{C}^{n}  \mathbb{R}^{n}$$

*Proof.* For every basis $(e_{1}, \dots  , e_{n})$ of (or ), for every vector $u = u_{1}e_{1} + \cdots  + u_{n}e_{n}$, we have
$$\|Au\|= \|u_{1}A(e_{1}) + \cdots  + u_{n}A(e_{n})\|$$
$$\le |u_{1}| \|A(e_{1})\|+ \cdots  + |u_{n}| \|A(e_{n})\|$$
$$\le C_{1}(|u_{1}| + \cdots  + |u_{n}|) = C_{1} \|u\|_{1} ,$$
where $C_{1} = max_{1\le i\le n} \|A(e_{i})\|$. By Theorem 9.6, the norms $\|\|$ and $\|\|_{1}$ are equivalent, so there is some constant $C_{2} > 0$ so that $\|u\|_{1} \le C_{2} \|u\|$ for all $u$, which implies that
$$\|Au\|\le C_{A} \|u\|,$$
where $C_{A} = C_{1}C_{2}$.

<!-- PAGE 355 -->
Proposition 9.9 says that every linear map on a finite-dimensional space is bounded. This implies that every linear map on a finite-dimensional space is continuous. Actually, it is not hard to show that a linear map on a normed vector space $E$ is bounded iff it is continuous, regardless of the dimension of $E$. Proposition 9.9 implies that for every matrix $A \in M_{n}(\mathbb{C})$ (or $A \in M_{n}(\mathbb{R}))$,
$$\|\|$$
$$\sup\in \mathbb{C} n \frac{Ax}{\|x\|} \le C_{A}.$$
$$x$$
$$x\neq 0$$
Since $\|\lambda u\| = |\lambda$ | $\|u\|$, for every nonzero vector $x$, we have
$$\|\| \|\|\| \|\|\|$$
$$\frac{Ax}{\|x\|} = \frac{xA(x/x)}{\|x\|} = \|A(x/ \|x\|)\|,$$
which implies that
$$\|\|$$
$$\sup\in \mathbb{C} n \frac{Ax}{\|x\|} = \sup\in \mathbb{C} n\|Ax\|.$$
$$xx$$
$$x\neq 0\|x\|=1$$
Similarly
$$\|\|$$
$$\sup\in \mathbb{R} n \frac{Ax}{\|x\|} = \sup\in \mathbb{R} n\|Ax\|.$$
$$xx$$
$$x\neq 0\|x\|=1$$
The above considerations justify the following definition.

> **Definition 9.8.** If $\|\|$ is any norm on $\mathbb{C}^{n}$, we define the function $\|\|_{op}$ on $M_{n}(\mathbb{C})$ by
$$\|\|$$
$$\|A\|_{op} = \sup\in \mathbb{C} n \frac{Ax}{\|x\|} = \sup\in \mathbb{C} n\|Ax\|.$$
$$xx$$
$$x\neq 0\|x\|=1$$
The function $A \mapsto \|A\|_{op}$ is called the subordinate matrix norm or operator norm induced by the norm $\|\|$. Another notation for the operator norm of a matrix $A$ (in particular, used by Horn and Johnson $[98])$, is |||A|||. It is easy to check that the function $A \mapsto \|A\|_{op}$ is indeed a norm, and by definition, it satisfies the property
$$\|Ax\|\le \|A\|_{op} \|x\|,for all x \in \mathbb{C}^{n}.$$
A norm $\|\|_{op}$ on $M_{n}(\mathbb{C})$ satisfying the above property is said to be subordinate to the vector norm $\|\|$ on $\mathbb{C}^{n}$. As a consequence of the above inequality, we have
$$\|ABx\|\le \|A\|_{op} \|Bx\|\le \|A\|_{op} \|B\|_{op} \|x\|,$$

<!-- PAGE 356 -->
for all $x \in \mathbb{C}^{n}$, which implies that
$$\|AB\|_{op} \le \|A\|_{op} \|B\|_{op}for all A, B \in M_{n}(\mathbb{C}),$$
showing that $A \mapsto \|A\|_{op}$ is a matrix norm (it is submultiplicative). Observe that the operator norm is also defined by
$$\|A\|_{op} = \inf{\lambda  \in \mathbb{R} | \|Ax\|\le \lambda  \|x\|, for all x \in \mathbb{C}^{n}}.$$
Since the function $x \mapsto \|Ax\|$ is continuous (because | $\|Ay\|-\|Ax\|| \le \|Ay$ - $Ax\|\le$
$$\mathbb{C}^{n}$$
$C_{A} \|x$ - $y\|)$ and the unit sphere $S^{n-1} = {x \in$ | $\|x\| = 1}$ is compact, there is some $\mathbb{C}^{n} x \in$ such that $\|x\| = 1$ and
$$\|Ax\|= \|A\|_{op} .$$
$$\mathbb{C}^{n}$$
Equivalently, there is some $x \in$ such that $x \neq  0$ and
$$\|Ax\|= \|A\|_{op} \|x\|.$$
Consequently we can replace sup by max in the definition of $\|A\|_{op}$ (and inf by min), namely
$$\|A\|_{op} = \max\|Ax\|.$$
$$x\in \mathbb{C} n$$
$$\|x\|=1$$
The definition of an operator norm also implies that
$$\|I\|_{op} = 1.$$
The above shows that the Frobenius norm is not a subordinate matrix norm for $n \ge 2$ (why?). If $\|\|$ is a vector norm $on\mathbb{C}^{n}$, the operator norm $\|\|_{op}$ that it induces applies to matrices in $M_{n}(\mathbb{C})$. If we are careful to denote vectors and matrices so that no confusion arises, for example, by using lower case letters for vectors and upper case letters for matrices, it should be clear that $\|A\|_{op}$ is the operator norm of the matrix $A$ and that $\|x\|$ is the vector norm of $x$. Consequently, following common practice to alleviate notation, we will drop the subscript “op” and simply write $\|A\|$ instead of $\|A\|_{op}$. The notion of subordinate norm can be slightly generalized.

> **Definition 9.9.** If $K =\mathbb{R}$ or $K =\mathbb{C}$, for any norm $\|\|$ on $M_{m,n}(K)$, and for any two norms $\|\|_{a}$ on $K^{n}$ and $\|\|_{b}$ on $K^{m}$, we say that the norm $\|\|$ is subordinate to the norms $\|\|_{a}$ and $\|\|_{b}$ if
$$\|Ax\|_{b} \le \|A\|\|x\|_{a}for all A \in M_{m,n}(K) and all x \in K^{n}.$$

<!-- PAGE 357 -->
Remark: For any norm $\|\|$ on $\mathbb{C}^{n}$, we can define the function $\|\|_{R}$ on $M_{n}(\mathbb{R})$ by
$$\|\|$$
$$\|A\|_{R} = \sup\in \mathbb{R} n \frac{Ax}{\|x\|} = \sup\in \mathbb{R} n\|Ax\|.$$
$$xx$$
$$x\neq 0\|x\|=1$$
The function $A \mapsto \|A\|_{R}$ is a matrix norm on $M_{n}(\mathbb{R})$, and
$$\|A\|_{R} \le \|A\|,$$
for all real matrices $A \in M_{n}(\mathbb{R})$. However, it is possible to construct vector norms $\|\| on\mathbb{C}^{n}$ and real matrices $A$ such that
$$\|A\|_{R} < \|A\|.$$
In order to avoid this kind of difficulties, we define subordinate matrix norms over $M_{n}(\mathbb{C})$. Luckily, it turns out that $\|A\|_{R} = \|A\|$ for the vector norms, $\|\|_{1} , \|\|_{2}$, and $\|\|_{\infty}$. We now prove Proposition 9.7 for real matrix norms.

> **Proposition 9.10.** For any matrix norm $\|\|$ on $M_{n}(\mathbb{R})$ and for any square $n \times  n$ matrix $A \in M_{n}(\mathbb{R})$, we have
$$\rho (A) \le \|A\|.$$

*Proof.* We follow the proof in Denis Serre’s book $[162]$. If $A$ is a real matrix, the problem is that the eigenvectors associated with the eigenvalue of maximum modulus may be complex. We use a trick based on the fact that for every matrix $A$ (real or complex),
$$\rho (A^{k}) = (\rho (A))^{k},$$
which is left as an exercise (use Proposition 15.7 which shows that if $(\lambda_{1} , \dots  , \lambda_{n}$ ) are the (not necessarily distinct) eigenvalues of $A$, then $(\lambda_{1}^{k} , \dots  , \lambda_{n}^{k}$ ) are the eigenvalues of $A^{k}$, for $k \ge 1)$.
$$\mathbb{C}^{n}$$
Pick any complex matrix norm $\|\|_{c}$ on (for example, the Frobenius norm, or any subordinate matrix norm induced by a norm $on\mathbb{C}^{n})$. The restriction of $\|\|_{c}$ to real matrices is a real norm that we also denote by $\|\|_{c}$. Now by Theorem 9.6, since $M_{n}(\mathbb{R})$ has finite dimension $n^{2}$, there is some constant $C > 0$ so that
$$\|B\|_{c} \le C \|B\|,for allB \in M_{n}(\mathbb{R}).$$
Furthermore, for every $k \ge 1$ and for every real $n\times n$ matrix $A$, by Proposition 9.7, $\rho (A^{k}) \le A_{c}^{k}$

, and because $\|\|$ is a matrix norm,

$A^{k}$

$\le \|A\|^{k}$, so we have
$$\le  ,$$
$$(\rho (A))^{k}= \rho (A^{k}) \le

$A_{c}^{k}$

$\le C$

$A^{k}$

$C \|A\|^{k}$$$ for all $k \ge 1$. It follows that
$$\rho (A) \le C^{1/k}\|A\|,for allk \ge 1.$$

<!-- PAGE 358 -->
However because $C > 0$, we have $lim_{k\mapsto \infty} C^{1/k} = 1$ (we have $lim_{k\mapsto \infty k}^{1}$ log(C) $= 0)$. Therefore, we conclude that
$$\rho (A) \le \|A\|,$$
as desired. We now determine explicitly what are the subordinate matrix norms associated with the vector norms $\|\|_{1} , \|\|_{2}$, and $\|\|_{\infty}$.

> **Proposition 9.11.** For every square matrix $A = (a_{ij}) \in M_{n}(\mathbb{C})$, we have
$$\|A\|_{1} = \sup\in \mathbb{C} n\|Ax\|_{1} = maxj \sum_{i=1}^{n}  |a_{ij}|$$
$$x$$
$$\|x\|=1$$
$$1$$
$$\|A\|_{\infty}=\sup\in \mathbb{C} n\|Ax\|_{\infty}= maxi \sum_{j=1}^{n}  |a_{ij}|$$
$$x$$
$$\|x\|=1$$
$$\infty$$
$$\|A\|_{2} = \sup\|Ax\|_{2} =p\overline{\rho}\overline{(}\overline{A}^{*}\overline{A}\overline{) =} p\overline{\rho}\overline{(}\overline{AA}^{*}\overline{)}.$$
$$x\in \mathbb{C} n$$
$$\|x\|=1$$
$$2$$
Note that $\|A\|_{1}$ is the maximum of the $\ell^{1}$ -norms of the columns of $A$ and $\|A\|_{\infty}$ is the maximum of the $\ell^{1}$ -norms of the rows of $A$. Furthermore, $\|A^{*}\|_{2} = \|A\|_{2}$, the norm $\|\|_{2}$ is unitarily invariant, which means that
$$\|A\|_{2} = \|UAV \|_{2}$$
for all unitary matrices $U, V$ , and if $A$ is a normal matrix, then $\|A\|_{2} = \rho (A)$.

*Proof.* For every vector $u$, we have
$$\|Au\|_{1} = \sum_{i}  \sum_{j}  a_{ij}u_{j} \le \sum_{j}  |u_{j}| \sum_{i}  |a_{ij}| \le \begin{pmatrix} \max & |a_{ij}| \\ j \end{pmatrix} \sum_{i}  \|u\|_{1} ,$$
which implies that
$$\|A\|_{1} \le maxj \sum_{i=1}^{n}  |a_{ij}|.$$
It remains to show that equality can be achieved. For this let $j_{0}$ be some index such that
$$maxj \sum_{i}  |a_{ij}| = \sum_{i}  |a_{ij0}|,$$
and let $u_{i} = 0$ for all $i \neq  j_{0}$ and $u_{j0} = 1$. In a similar way, we have
$$\|Au\|_{\infty}= maxi \sum_{j}  a_{ij}u_{j} \le \begin{pmatrix} \max & |a_{ij}| \\ i \end{pmatrix} \sum_{j}  \|u\|_{\infty},$$

<!-- PAGE 359 -->
which implies that
$$\|A\|_{\infty}\le maxi \sum_{j=1}^{n}  |a_{ij}|.$$
To achieve equality, let $i_{0}$ be some index such that
$$maxi \sum_{j}  |a_{ij}| = \sum_{j}  |a_{i0j}|.$$
The reader should check that the vector given by
$$(\overline{a} ij$$
$$\overline{0} if a_{i0j} \neq  0$$
$$u_{j} =\overline{|}\overline{a}\overline{i}\overline{j}\overline{|}$$
$$1^{0}if a_{i0j} = 0$$
works. We have
$$\|A\|_{2}^{2} = \sup\|Ax\|_{2}^{2} = supx^{*}A^{*}Ax.$$
$$x\in \mathbb{C} nx\in \mathbb{C} n$$
$$x*x=1x*x=1$$
Since the matrix $A^{*}A$ is symmetric, it has real eigenvalues and it can be diagonalized with respect to a unitary matrix. These facts can be used to prove that the function $x \mapsto x^{*}A^{*}Ax$ has a maximum on the sphere $x^{*}x = 1$ equal to the largest eigenvalue of $A^{*}A$, namely, $\rho (A^{*}A)$. We postpone the proof until we discuss optimizing quadratic functions. Therefore,
$$\|A\|_{2} =p\overline{\rho}\overline{(}\overline{A}^{*}\overline{A}\overline{)}.$$
Let use now prove that $\rho (A^{*}A) = \rho (AA^{*})$. First assume that $\rho (A^{*}A) > 0$. In this case, there is some eigenvector $u (\neq  0)$ such that
$$A^{*}Au = \rho (A^{*}A)u,$$
and since $\rho (A^{*}A) > 0$, we must have Au $\neq  0$. Since Au $\neq  0$,
$$AA^{*}(Au) = A(A^{*}Au) = \rho (A^{*}A)Au$$
which means that $\rho (A^{*}A)$ is an eigenvalue of $AA^{*}$, and thus
$$\rho (A^{*}A) \le \rho (AA^{*}).$$
Because $(A^{*})^{*} = A$, by replacing $A$ by $A^{*}$, we get
$$\rho (AA^{*}) \le \rho (A^{*}A),$$
and so $\rho (A^{*}A) = \rho (AA^{*})$.

<!-- PAGE 360 -->
If $\rho (A^{*}A) = 0$, then we must have $\rho (AA^{*}) = 0$, since otherwise by the previous reasoning we would have $\rho (A^{*}A) = \rho (AA^{*}) > 0$. Hence, in all case
$$\|A\|_{2}^{2} = \rho (A^{*}A) = \rho (AA^{*}) = \|A^{*}\|_{2}^{2} .$$
For any unitary matrices $U$ and $V$ , it is an easy exercise to prove that $V^{*} A^{*}AV$ and $A^{*}A$ have the same eigenvalues, so
$$\|A\|_{2}^{2} = \rho (A^{*}A) = \rho (V^{*} A^{*}AV ) = \|AV \|_{2}^{2} ,$$
and also
$$\|A\|_{2}^{2} = \rho (A^{*}A) = \rho (A^{*}U^{*}UA) = \|UA\|_{2}^{2} .$$
Finally, if $A$ is a normal matrix $(AA^{*} = A^{*}A)$, it can be shown that there is some unitary matrix $U$ so that
$$A = UDU^{*} ,$$
where $D = diag(\lambda_{1} , \dots  , \lambda_{n}$ ) is a diagonal matrix consisting of the eigenvalues of $A$, and thus
$$A^{*}A = (UDU^{*} )^{*}UDU^{*} = UD^{*}U^{*} UDU^{*} = UD^{*}DU^{*} .$$
However, $D^{*}D = diag(|\lambda_{1} |^{2}, \dots  , |\lambda_{n} |^{2})$, which proves that the eigenvalues of $A^{*}A = AA^{*}$ are $(|\lambda_{1} |^{2}, \dots  , |\lambda_{n} |^{2})$, and thus,
$$\rho (A^{*}A) = \rho (D^{*}D) = \max|\lambda_{i} |^{2}= (\rho (A))^{2},$$
$$i$$
so that $\|A\|_{2} = \rho (A)$.

> **Definition 9.10.** For $A = (a_{ij}) \in M_{n}(\mathbb{C})$, the norm $\|A\|_{2}$ is often called the spectral norm. Observe that Property $(3)$ of Proposition 9.8 says that
$$\sqrt$$
$$\|A\|_{2} \le \|A\|_{F} \le \overline{n} \|A\|_{2} ,$$
which shows that the Frobenius norm is an upper bound on the spectral norm. The Frobenius norm is much easier to compute than the spectral norm. The reader will check that the above proof still holds if the matrix $A$ is real (change unitary to orthogonal), confirming the fact that $\|A\|_{R} = \|A\|$ for the vector norms $\|\|_{1} , \|\|_{2}$, and $\|\|_{\infty}$. It is also easy to verify that the proof goes through for rectangular $m\times n$ matrices, with the same formulae. Similarly, the Frobenius norm given by
$$1/2$$
$$\|A\|_{F} = \begin{pmatrix} |a_{ij}|^{2} \end{pmatrix} \sum_{i=1j}^{m}  \sum_{=1}^{n}  =p\overline{\mathrm{tr}(}\overline{A}^{*}\overline{A}\overline{) =} p\overline{\mathrm{tr}(}\overline{AA}^{*}\overline{)}$$
is also a norm on rectangular matrices. For these norms, whenever AB makes sense, we have
$$\|AB\|\le \|A\|\|B\|.$$

<!-- PAGE 361 -->
$$Remark: It can be shown that for any two real numbers p, q \ge 1 such that \frac{1}{p} + \frac{1}{q} = 1, we$$
have $\|A^{*}\|_{q} = \|A\|_{p} = sup{\mathfrak{R}(y^{*}Ax)$ | $\|x\|_{p} = 1, \|y\|_{q} = 1} = sup{|\langle$ Ax, $y\rangle$ | | $\|x\|_{p} = 1, \|y\|_{q} = 1}$, where $\|A^{*}\|_{q}$ and $\|A\|_{p}$ are the operator norms.
Remark: Let $(E, \|\|)$ and $(F, \|\|)$ be two normed vector spaces (for simplicity of notation, we use the same symbol $\|\|$ for the norms on $E$ and $F$; this should not cause any confusion). Recall that a function $f$ : $E \to F$ is continuous if for every $a \in E$, for every $\epsilon  > 0$, there is some $\eta  > 0$ such that for all $x \in E$,
$$if\|x -a\|\le \eta then\|f(x) -f(a)\|\le \epsilon .$$
It is not hard to show that a linear map $f$ : $E \to F$ is continuous iff there is some constant $C \ge 0$ such that
$$\|f(x)\|\le C \|x\|for all x \in E.$$
If so, we say that $f$ is bounded (or a linear bounded operator). We let $\mathcal{L}(E; F)$ denote the set of all continuous (equivalently, bounded) linear maps from $E$ to $F$. Then we can define the operator norm (or subordinate norm) $\|\|$ on $\mathcal{L}(E; F)$ as follows: for every $f \in$ L(E; $F)$,
$$\|\|$$
$$\|f\|= \sup\in \frac{f(x)}{\|x\|} = \sup\in \|f(x)\|,$$
$$xExE$$
$$x\neq 0\|x\|=1$$
or equivalently by
$$\|f\|= \inf{\lambda  \in \mathbb{R} | \|f(x)\|\le \lambda  \|x\|, for all x \in E}.$$
Here because $E$ may be infinite-dimensional, sup can’t be replaced by max and inf can’t be replaced by min. It is not hard to show that the map $f \mapsto \|f\|$ is a norm on $\mathcal{L}(E; F)$ satisfying the property
$$\|f(x)\|\le \|f\|\|x\|$$
for all $x \in E$, and that if $f \in$ L(E; $F)$ and $g \in$ L(F; $G)$, then
$$\|g \circ f\|\le \|g\|\|f\|.$$
Operator norms play an important role in functional analysis, especially when the spaces $E$ and $F$ are complete.
