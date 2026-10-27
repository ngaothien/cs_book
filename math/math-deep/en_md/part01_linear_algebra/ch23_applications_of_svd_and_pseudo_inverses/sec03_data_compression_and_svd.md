# Data Compression and SVD


<!-- PAGE 781 -->

> **Example 23.3.** Consider the following real diagonal form of the normal matrix
$$A = \begin{pmatrix} -2.7500 & 2.1651 & -0.8660 & 0.5000 \\ 2.1651 & -0.2500 & -1.5000 & 0.8660 \\ 0.8660 & 1.5000 & 0.7500 & -0.4330 \\ 0.5000 & 0.8660 & 0.4330 & 0.2500 \end{pmatrix} = U\Lambda U^{\top},$$
$$---$$
with
$$U = \begin{pmatrix} \cos(\pi /3) & 0 & \sin(\pi /3) & 0 \\ \sin(\pi /3) & 0 & -\cos(\pi /3) & 0 \\ 0 & \cos(\pi /6) & 0 & \sin(\pi /6) \\ 0 & \cos(\pi /6) & 0 & \sin(\pi /6) \end{pmatrix} ,\Lambda  = \begin{pmatrix} 1 & -2 & 0 & 0 \\ 2 & 1 & 0 & 0 \\ 0 & 0 & -4 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} .$$
$$-$$
We obtain
$$\Lambda^{+}  = \begin{pmatrix} 1/5 & 2/5 & 0 & 0 \\ -2/5 & 1/5 & 0 & 0 \\ 0 & 0 & -1/4 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} ,$$
and the pseudo-inverse of $A$ is
$$A^{+} = U\Lambda^{+} U^{\top} = \begin{pmatrix} -0.1375 & 0.1949 & 0.1732 & -0.1000 \\ 0.1949 & 0.0875 & 0.3000 & -0.1732 \\ -0.1732 & -0.3000 & 0.1500 & -0.0866 \\ 0.1000 & 0.1732 & 0.0866 & 0.0500 \end{pmatrix} ,$$
$$-$$
which agrees with pinv(A). The following properties, due to Penrose, characterize the pseudo-inverse of a matrix. We have already proved that the pseudo-inverse satisfies these equations. For a proof of the converse, see Kincaid and Cheney $[105]$.

> **Proposition 23.8.** Given any $m \times  n$ matrix $A$ (real or complex), the pseudo-inverse $A^{+}$ of $A$ is the unique $n \times  m$ matrix satisfying the following properties:
$$AA^{+}A = A,$$
$$A^{+}AA^{+}= A^{+},$$
$$(AA^{+})^{\top}= AA^{+},$$
$$(A^{+}A)^{\top}= A^{+}A.$$

## 23.3 Data Compression and SVD

Among the many applications of SVD, a very useful one is data compression, notably for images. In order to make precise the notion of closeness of matrices, we use the notion of

<!-- PAGE 782 -->
matrix norm. This concept is defined in Chapter $9$, and the reader may want to review it before reading any further. Given an $m \times  n$ matrix of rank $r$, we would like to find a best approximation of $A$ by a matrix $B$ of rank $k \le r$ (actually, $k < r)$ such that $\|A$ - $B\|_{2}$ (or $\|A$ - $B\|_{F})$ is minimized. The following proposition is known as the Eckart–Young theorem.

> **Proposition 23.9.** Let $A$ be an $m \times  n$ matrix of rank $r$ and let $V DU^{\top} = A$ be an SVD for $A$. Write $u_{i}$ for the columns of $U, v_{i}$ for the columns of $V$ , and $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{p}$  for the singular values of $A (p =$ min(m, $n))$. Then a matrix of rank $k < r$ closest to $A$ (in the $\|\|_{2}$ norm) is given by
$$A_{k} = \sum_{i=1}^{k}  \sigma_{i} v_{i}u_{i}^{\top} = V \mathrm{diag}(\sigma_{1} , \dots  , \sigma_{k} , 0, \dots  , 0)U^{\top}$$
and $\|A$ - $A_{k}\|_{2} = \sigma_{k+1}$ .

*Proof.* By construction, $A_{k}$ has rank $k$, and we have
$$\|A -A_{k}\|_{2} = \sum_{i=k+1}^{p}  \sigma_{i} v_{i}u_{i}^{\top} =

$V \mathrm{diag}(0, \dots  , 0, \sigma_{k+1} , \dots  , \sigma_{p} )U_{2}^{\top}$

$= \sigma_{k+1}$ .$$
$$2$$
It remains to show that $\|A$ - $B\|_{2} \ge \sigma_{k+1}$  for all rank $k$ matrices $B$. Let $B$ be any rank $k$ matrix, so its kernel has dimension $n -k$. The subspace $U_{k+1}$ spanned by $(u_{1}, \dots  , u_{k+1})$ has dimension $k + 1$, and because the sum of the dimensions of the kernel of $B$ and of $U_{k+1}$ is $(n$ - $k) + k + 1 = n + 1$, these two subspaces must intersect in a subspace of dimension at least $1$. Pick any unit vector $h$ in Ker(B) $\cap U_{k+1}$. Then since Bh $= 0$, and since $U$ and $V$ are isometries, we have $\|A$ - $B\|_{2}^{2} \ge \|(A$ - $B)h\|_{2}^{2} = \|Ah\|_{2}^{2} =$

$V DU^{\top}h_{2}^{2}$

$=$

$DU^{\top}h_{2}^{2}$

$\ge \sigma_{k+1}^{2}$

$U^{\top}h_{2}^{2}$

$= \sigma_{k+1}^{2}$ , which proves our claim. Note that $A_{k}$ can be stored using $(m +$ n)k entries, as opposed to mn entries. When $k \ll m$, this is a substantial gain.

> **Example 23.4.** Consider the badly conditioned symmetric matrix
$$A = \begin{pmatrix} 10 & 7 & 8 & 7 \\ 7 & 5 & 6 & 5 \\ 8 & 6 & 10 & 9 \\ 7 & 5 & 9 & 10 \end{pmatrix}$$
from Section 9.5. Since $A$ is SPD, we have the SVD
$$A = UDU^{\top} ,$$
