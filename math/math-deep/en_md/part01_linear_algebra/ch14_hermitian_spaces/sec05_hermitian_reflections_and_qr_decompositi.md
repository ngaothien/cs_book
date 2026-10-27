# Hermitian Reflections and QR-Decomposition


<!-- PAGE 548 -->
Then it is easy to show that there is a diagonal matrix $D$ with diagonal entries such that $|d_{ii}| = 1$ for $i = 1, \dots  , n$, and $U_{2} = U_{1}D, R_{2} = D^{*}R_{1}$. We have the following version of the Hadamard inequality for complex matrices. The proof is essentially the same as in the Euclidean case but it uses Proposition 14.16 instead of Proposition 12.16.

> **Proposition 14.17.** (Hadamard) For any complex $n \times  n$ matrix $A = (a_{ij})$, we have
$$1/21/2$$
$$| \det(A)| \le \prod_{i=1}^{n}  \begin{pmatrix} |a_{ij}|^{2} \end{pmatrix} \sum_{j=1}^{n}  and| \det(A)| \le \prod_{j=1}^{n}  \begin{pmatrix} |a_{ij}|^{2} \end{pmatrix} \sum_{i=1}^{n}  .$$
Moreover, equality holds iff either $A$ has orthogonal rows in the left inequality or orthogonal columns in the right inequality. We also have the following version of Proposition 12.18 for Hermitian matrices. The proof of Proposition 12.18 goes through because the Cholesky decomposition for a Hermitian positive definite $A$ matrix holds in the form $A = B^{*}B$, where $B$ is upper triangular with positive diagonal entries. The details are left to the reader.

> **Proposition 14.18.** (Hadamard) For any complex $n\times n$ matrix $A = (a_{ij})$, if $A$ is Hermitian positive semidefinite, then we have
$$\det(A) \le \prod_{i=1}^{n}  a_{ii}.$$
Moreover, if $A$ is positive definite, then equality holds iff $A$ is a diagonal matrix.

## 14.5 Hermitian Reflections and QR-Decomposition

If $A$ is an $n \times  n$ complex singular matrix, there is some (not necessarily unique) QRdecomposition $A = QR$ with $Q$ a unitary matrix which is a product of Householder reflections and $R$ an upper triangular matrix, but the proof is more involved. One way to proceed is to generalize the notion of hyperplane reflection. This is not really surprising since in the Hermitian case there are improper isometries whose determinant can be any unit complex number. Hyperplane reflections are generalized as follows.

> **Definition 14.12.** Let $E$ be a Hermitian space of finite dimension. For any hyperplane $H$, for any nonnull vector $w$ orthogonal to $H$, so that $E = H \oplus G$, where $G =\mathbb{C} w$, a Hermitian reflection about $H$ of angle $\theta$  is a linear map of the form $\rho_{H, \theta}$  : $E \to E$, defined such that
$$\rho_{H, \theta} (u) = p_{H}(u) + e^{i\theta}p_{G}(u),$$
$$̸$$
for any unit complex number $e^{i\theta} = 1$ (i.e. $\theta$ ̸ $= k2\pi$ ). For any nonzero vector $w \in E$, we denote by $\rho_{w,\theta}$  the Hermitian reflection given by $\rho_{H,\theta}$ , where $H$ is the hyperplane orthogonal to $w$.

<!-- PAGE 549 -->
Since $u = p_{H}(u) + p_{G}(u)$, the Hermitian reflection $\rho_{w, \theta}$  is also expressed as
$$\rho_{w, \theta} (u) = u + (e^{i\theta}-1)p_{G}(u),$$
or as
$$1)  \cdot$$
$$\rho_{w, \theta} (u) = u + (e^{i\theta}- \frac{(u w)}{\|w\|^{2}} w.$$
Note that the case of a standard hyperplane reflection is obtained when $e^{i\theta} = -1$, i.e., $\theta  = \pi$ . In this case,
$$2  \cdot$$
$$\rho_{w, \pi} (u) = u - \frac{(u w)}{\|w\|^{2}} w,$$
and the matrix of such a reflection is a Householder matrix, as in Section 13.1, except that $w$ may be a complex vector. We leave as an easy exercise to check that $\rho_{w, \theta}$  is indeed an isometry, and that the inverse of $\rho_{w, \theta}$  is $\rho_{w,-\theta}$ . If we pick an orthonormal basis $(e_{1}, \dots  , e_{n})$ such that $(e_{1}, \dots  , e_{n-1})$ is an orthonormal basis of $H$, the matrix of $\rho_{w, \theta}$  is
$$\begin{pmatrix} I_{n-1} & 0 \\ 0 & e^{i\theta} \end{pmatrix}$$
We now come to the main surprise. Given any two distinct vectors $u$ and $v$ such that $\|u\| = \|v\|$, there isn’t always a hyperplane reflection mapping $u$ to $v$, but this can be done using two Hermitian reflections!

> **Proposition 14.19.** Let $E$ be any nontrivial Hermitian space.
$(1)$ For any two vectors $u, v \in E$ such that $u \neq  v$ and $\|u\| = \|v\|$, if $u \cdot  v = e^{i\theta}|u \cdot$  v|, then the (usual) reflection $s$ about the hyperplane orthogonal to the vector $v$ - $e^{-i\theta}u$ is such that s(u) $= e^{i\theta}v$.
$(2)$ For any nonnull vector $v \in E$, for any unit complex number $e^{i\theta} \neq  1$, there is a Hermitian reflection $\rho_{v,\theta}$  such that
$$\rho_{v,\theta} (v) = e^{i\theta}v.$$
As a consequence, for $u$ and $v$ as in $(1)$, we have $\rho_{v,-\theta}  \circ$ s(u) $= v$.

*Proof.* $(1)$ Consider the (usual) reflection about the hyperplane orthogonal to $w = v -e^{-i\theta}u$. We have
$$2  \cdot  -$$
$$s(u) = u - \frac{(u (ve^{-i\theta}u))}{\|v -e^{-i\theta}u\|^{2}} (v -e^{-i\theta}u).$$
We need to compute
$$-2u \cdot  (v -e^{-i\theta}u)and(v -e^{-i\theta}u) \cdot  (v -e^{-i\theta}u).$$

<!-- PAGE 550 -->
Since $u \cdot  v = e^{i\theta}|u \cdot$  v|, we have
$$e^{-i\theta}u \cdot  v = |u \cdot  v|ande^{i\theta}v \cdot  u = |u \cdot  v|.$$
Using the above and the fact that $\|u\| = \|v\|$, we get
$$-2u \cdot  (v -e^{-i\theta}u) = 2e^{i\theta}\|u\|^{2}-2u \cdot  v,$$
$$= 2e^{i\theta}(\|u\|^{2}-|u \cdot  v|),$$
and
$$(v -e^{-i\theta}u) \cdot  (v -e^{-i\theta}u) = \|v\|^{2}+ \|u\|^{2}-e^{-i\theta}u \cdot  v -e^{i\theta}v \cdot  u,$$
$$= 2(\|u\|^{2}-|u \cdot  v|),$$
and thus,
$$2  \cdot  -$$
$$- \frac{(u (ve^{-i\theta}u))}{\|(v -e^{-i\theta}u)\|^{2}} (v -e^{-i\theta}u) = e^{i\theta}(v -e^{-i\theta}u).$$
But then,
$$s(u) = u + e^{i\theta}(v -e^{-i\theta}u) = u + e^{i\theta}v -u = e^{i\theta}v,$$
and s(u) $= e^{i\theta}v$, as claimed.
$(2)$ This part is easier. Consider the Hermitian reflection
$$1)  \cdot$$
$$\rho_{v,\theta} (u) = u + (e^{i\theta}- \frac{(u v)}{\|v\|^{2}} v.$$
We have
$$1)  \cdot$$
$$\rho_{v,\theta} (v) = v + (e^{i\theta}- \frac{(v v)}{\|v\|^{2}} v,$$
$$= v + (e^{i\theta}-1)v,$$
$$= e^{i\theta}v.$$
Thus, $\rho_{v,\theta} (v) = e^{i\theta}v$. Since $\rho_{v,\theta}$  is linear, changing the argument $v$ to $e^{i\theta}v$, we get
$$\rho_{v,-\theta} (e^{i\theta}v) = v,$$
and thus, $\rho_{v,-\theta}  \circ$ s(u) $= v$.
Remarks:
$(1)$ If we use the vector $v + e^{-i\theta}u$ instead of $v$ - $e^{-i\theta}u$, we get s(u) $= -e^{i\theta}v$.

<!-- PAGE 551 -->
$(2)$ Certain authors, such as Kincaid and Cheney $[105]$ and Ciarlet $[41]$, use the vector $u + e^{i\theta}v$ instead of the vector $v + e^{-i\theta}u$. The effect of this choice is that they also get s(u) $= -e^{i\theta}v$.
$(3)$ If $v = \|u\|e_{1}$, where $e_{1}$ is a basis vector, $u \cdot  e_{1} = a_{1}$, where $a_{1}$ is just the coefficient of $u$ over the basis vector $e_{1}$. Then, since $u \cdot  e_{1} = e^{i\theta}|a_{1}|$, the choice of the plus sign in the vector $\|u\|e_{1} + e^{-i\theta}u$ has the effect that the coefficient of this vector over $e_{1}$ is $\|u\| + |a_{1}|$, and no cancellations takes place, which is preferable for numerical stability (we need to divide by the square norm of this vector). We now show that the QR-decomposition in terms of (complex) Householder matrices holds for complex matrices. We need the version of Proposition 14.19 and a trick at the end of the argument, but the proof is basically unchanged.

> **Proposition 14.20.** Let $E$ be a nontrivial Hermitian space of dimension $n$. Given any orthonormal basis $(e_{1}, \dots  , e_{n})$, for any $n$-tuple of vectors $(v_{1}, \dots  , v_{n})$, there is a sequence of $n$ - $1$ isometries $h_{1}, \dots  , h_{n-1}$, such that $h_{i}$ is a (standard) hyperplane reflection or the identity, and if $(r_{1}, \dots  , r_{n})$ are the vectors given by
$$r_{j} = h_{n-1} \circ \cdots  \circ h_{2} \circ h_{1}(v_{j}),1 \le j \le n,$$
then every $r_{j}$ is a linear combination of the vectors $(e_{1}, \dots  , e_{j}), (1 \le j \le n)$. Equivalently, the matrix $R$ whose columns are the components of the $r_{j}$ over the basis $(e_{1}, \dots  , e_{n})$ is an upper triangular matrix. Furthermore, if we allow one more isometry $h_{n}$ of the form
$$h_{n} = \rho_{en, \phi n}  \circ \cdots  \circ \rho_{e1,\phi1}$$
after $h_{1}, \dots  , h_{n-1}$, we can ensure that the diagonal entries of $R$ are nonnegative.

*Proof.* The proof is very similar to the proof of Proposition 13.3, but it needs to be modified a little bit since Proposition 14.19 is weaker than Proposition 13.2. We explain how to modify the induction step, leaving the base case and the rest of the proof as an exercise. As in the proof of Proposition 13.3, the vectors $(e_{1}, \dots  , e_{k})$ form a basis for the subspace denoted as $U_{k}'$ , the vectors $(e_{k+1}, \dots  , e_{n})$ form a basis for the subspace denoted as $U_{k}''$ , the subspaces $U_{k}'$  and $U_{k}''$ are orthogonal, and $E = U_{k}' \oplus U_{k}''$ . Let
$$u_{k+1} = h_{k} \circ \cdots  \circ h_{2} \circ h_{1}(v_{k+1}).$$
We can write
$$u_{k+1} = u_{k+1}' + u_{k+1}'',$$
where $u_{k+1}' \in U_{k}'$ and $u_{k+1}'' \in U_{k}''$ . Let
$$r_{k+1,k+1} =

$u_{k+1}''$

$,ande^{i\theta k+1}|u_{k+1}'' \cdot  e_{k+1}| = u_{k+1}'' \cdot  e_{k+1}.$$$

<!-- PAGE 552 -->
If $u_{k+1}'' = e^{i\theta k+1}r_{k+1,k+1} e_{k+1}$, we let $h_{k+1} =$ id. Otherwise, by Proposition 14.19(1) (with $u = u_{k+1}''$ and $v = r_{k+1,k+1} e_{k+1})$, there is a unique hyperplane reflection $h_{k+1}$ such that
$$h_{k+1}(u_{k+1}'') = e^{i\theta k+1}r_{k+1,k+1} e_{k+1},$$
where $h_{k+1}$ is the reflection about the hyperplane $H_{k+1}$ orthogonal to the vector
$$w_{k+1} = r_{k+1,k+1} e_{k+1} -e^{-i\theta k+1}u_{k+1}''.$$
At the end of the induction, we have a triangular matrix $R$, but the diagonal entries $e^{i\theta j}r_{j, j}$ of $R$ may be complex. Letting
$$h_{n} = \rho_{en,-\theta n}  \circ \cdots  \circ \rho_{e1,-\theta1} ,$$
we observe that the diagonal entries of the matrix of vectors
$$r_{j}' = h_{n} \circ h_{n-1} \circ \cdots  \circ h_{2} \circ h_{1}(v_{j})$$
is triangular with nonnegative entries.
Remark: For numerical stability, it is preferable to use $w_{k+1} = r_{k+1,k+1} e_{k+1} + e^{-i\theta k+1}u_{k+1}''$ instead of $w_{k+1} = r_{k+1,k+1} e_{k+1}$ - $e^{-i\theta k+1}u_{k+1}''$. The effect of that choice is that the diagonal entries in $R$ will be of the form $-e^{i\theta j}r_{j, j} = e^{i(\theta j+\pi)}r_{j, j}$. Of course, we can make these entries nonegative by applying
$$h_{n} = \rho_{en, \pi-\theta n}  \circ \cdots  \circ \rho_{e1,\pi-\theta1}$$
after $h_{n-1}$. As in the Euclidean case, Proposition 14.20 immediately implies the QR-decomposition for arbitrary complex $n\times n$-matrices, where $Q$ is now unitary (see Kincaid and Cheney $[105]$ and Ciarlet $[41])$.

> **Proposition 14.21.** For every complex $n \times n$-matrix $A$, there is a sequence $H_{1}, \dots  , H_{n-1}$ of matrices, where each $H_{i}$ is either a Householder matrix or the identity, and an upper triangular matrix $R$, such that
$$R = H_{n-1} \cdots  H_{2}H_{1}A.$$
As a corollary, there is a pair of matrices $Q, R$, where $Q$ is unitary and $R$ is upper triangular, such that $A = QR$ (a QR-decomposition of $A)$. Furthermore, $R$ can be chosen so that its diagonal entries are nonnegative. This can be achieved by a diagonal matrix $D$ with entries such that $|d_{ii}| = 1$ for $i = 1, \dots  , n$, and we have $A = QR$ with
$$e e$$
$$Q = H_{1} \cdots  H_{n-1}D,R = D^{*}R,$$
$$ee$$
where $R$ is upper triangular and has nonnegative diagonal entries. $e$

*Proof.* It is essentially identical to the proof of Proposition 13.4, and we leave the details as an exercise. For the last statement, observe that $h_{n} \circ \cdots  \circ h_{1}$ is also an isometry.
