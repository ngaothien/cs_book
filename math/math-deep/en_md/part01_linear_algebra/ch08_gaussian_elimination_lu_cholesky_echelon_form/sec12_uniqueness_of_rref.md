# Uniqueness of RREF


<!-- PAGE 310 -->

## 8.12 Uniqueness of RREF Form

For the sake of completeness, we prove that the reduced row echelon form of a matrix is unique. The neat proof given below is borrowed and adapted from $W$. Kahan.

> **Proposition 8.19.** Let $A$ be any $m \times  n$ matrix. If $U$ and $V$ are two reduced row echelon matrices obtained from $A$ by applying two sequences of elementary row operations $E_{1}, \dots  , E_{p}$ and $F_{1}, \dots  , F_{q}$, so that
$$U = E_{p} \cdots  E_{1}AandV = F_{q} \cdots  F_{1}A,$$
then $U = V$ . In other words, the reduced row echelon form of any matrix is unique.

*Proof.* Let
$$C = E_{p} \cdots  E_{1}F_{1}^{-1} \cdots  F_{q}^{-1}$$
so that
$$U = CVandV = C^{-1}U.$$
Recall from Proposition 8.13 that $U$ and $V$ have the same row rank $r$, and since $U$ and $V$ are in rref, this is the number of nonzero rows in both $U$ and $V$ . We prove by induction on $n$ that $U = V$ (and that the first $r$ columns of $C$ are the first $r$ columns in $I_{m})$. If $r = 0$ then $A = U = V = 0$ and the result is trivial. We now assume that $r \ge 1$. Let $\ell_{j}^{n}$  denote the jth column of the identity matrix $I_{n}$, and let $u_{j} = U\ell_{j}^{n}  , v_{j} = V \ell_{j}^{n}  , c_{j} = C\ell_{j}^{m}$  , and $a_{j} = A\ell_{j}^{n}$  , be the jth column of $U, V , C$, and $A$ respectively. First I claim that $u_{j} = 0$ iff $v_{j} = 0$ iff $a_{j} = 0$. Indeed, if $v_{j} = 0$, then (because $U = CV$ ) $u_{j} = Cv_{j} = 0$, and if $u_{j} = 0$, then $v_{j} = C^{-1}u_{j} = 0$. Since $U = E_{p} \cdots  E_{1}A$, we also get $a_{j} = 0$ iff $u_{j} = 0$. Therefore, we may simplify our task by striking out columns of zeros from $U, V$ , and $A$, since they will have corresponding indices. We still use $n$ to denote the number of columns of $A$. Observe that because $U$ and $V$ are reduced row echelon matrices with no zero columns, we must have $u_{1} = v_{1} = \ell_{1}^{m}$  . Claim. If $U$ and $V$ are reduced row echelon matrices without zero columns such that $U = CV$ , for all $k \ge 1$, if $k \le m$, then $\ell_{k}^{m}$  occurs in $U$ iff $\ell_{k}^{m}$  occurs in $V$ , and if $\ell_{k}^{m}$  does occur in $U$, then $1. \ell_{k}^{m}$  occurs for the same column index $j_{k}$ in both $U$ and $V$ ; $2$. the first $j_{k}$ columns of $U$ and $V$ match; $3$. the subsequent columns in $U$ and $V$ (of column index $> j_{k})$ whose coordinates of index $k + 1$ through $m$ are all equal to $0$ also match. Let $n_{k}$ be the rightmost index of such a column, with $n_{k} = j_{k}$ if there is none.

<!-- PAGE 311 -->
$4$. the first $k$ columns of $C$ match the first $k$ columns of $I_{m}$. We prove this claim by induction on $k$. For the base case $k = 1$, we already know that $u_{1} = v_{1} = \ell_{1}^{m}$  . We also have
$$c_{1} = C\ell_{1}^{m}  = Cv_{1} = u_{1} = \ell_{1}^{m}  .$$
If $v_{j} = \lambda \ell_{1}^{m}$  for some $\lambda  \in \mathbb{R}$, then
$$u_{j} = U\ell_{j}^{n}  = CV \ell_{j}^{n}  = Cv_{j} = \lambda C\ell_{1}^{m}  = \lambda c_{1} = \lambda \ell_{1}^{m}  = v_{j}.$$
A similar argument using $C^{-1}$ shows that if $u_{j} = \lambda \ell_{1}^{m}$  , then $v_{j} = u_{j}$. Therefore, all the columns of $U$ and $V$ proportional to $\ell_{1}^{m}$  match, which establishes the base case. Observe that if $\ell_{2}^{m}$  appears in $U$, then it must appear in both $U$ and $V$ for the same index, and if not then $n_{1} = n$ and $U = V$ . Next us now prove the induction step. If $n_{k} = n$, then $U = V$ and we are done. If $k = r$, then $C$ is a block matrix of the form
$$C = \begin{pmatrix} I_{r} & B \\ 0_{m-r,r} & C \end{pmatrix}$$
and since the last $m$ - $r$ rows of both $U$ and $V$ are zero rows, $C$ acts as the identity on the first $r$ rows, and so $U = V$ . Otherwise $k < r, n_{k} < n$, and $\ell_{k+1}^{m}$  appears in both $U$ and $V$ , in which case, by $(2)$ and $(3)$ of the induction hypothesis, it appears in both $U$ and $V$ for the same index, say $j_{k+1}$. Thus, $u_{jk+1} = v_{jk+1} = \ell_{k+1}^{m}$ . It follows that
$$c_{k+1} = C\ell_{k+1}^{m}  = Cv_{jk+1} = u_{jk+1} = \ell_{k+1}^{m} ,$$
so the first $k + 1$ columns of $C$ match the first $k + 1$ columns of $I_{m}$. Consider any subsequent column $v_{j}$ (with $j > j_{k+1})$ whose elements beyond the $(k +1)th$ all vanish. Then $v_{j}$ is a linear combination of columns of $V$ to the left of $v_{j}$, so
$$u_{j} = Cv_{j} = v_{j}.$$
because the first $k + 1$ columns of $C$ match the first $k + 1$ column of $I_{m}$. Similarly, any subsequent column $u_{j}$ (with $j > j_{k+1})$ whose elements beyond the $(k+1)th$ all vanish is equal to $v_{j}$. Therefore, all the subsequent columns in $U$ and $V$ (of index $> j_{k+1})$ whose elements beyond the $(k +$ 1)th all vanish also match, which completes the induction hypothesis.
Remark: Observe that $C = E_{p} \cdots  E_{1}F_{1}^{-1} \cdots  F_{q}^{-1}$ is not necessarily the identity matrix $I_{m}$. However, $C = I_{m}$ if $r = m (A$ has row rank $m)$. The reduction to row echelon form also provides a method to describe the set of solutions of a linear system of the form Ax $= b$.
