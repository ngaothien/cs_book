# LU-Factorization


<!-- PAGE 269 -->

> **Theorem 8.1.** (Gaussian elimination) Let $A$ be an $n \times  n$ matrix (invertible or not). Then there is some invertible matrix $M$ so that $U = MA$ is upper-triangular. The pivots are all nonzero iff $A$ is invertible.

*Proof.* We already proved the theorem when $A$ is invertible, as well as the last assertion. Now $A$ is singular iff some pivot is zero, say at Stage $k$ of the elimination. If so, we must have $a_{i k}^{(k)} = 0$ for $i = k, \dots  , n$; but in this case, $A_{k+1} = A_{k}$ and we may pick $P_{k} = E_{k} =$ I.
Remark: Obviously, the matrix $M$ can be computed as
$$M = E_{n-1}P_{n-1} \cdots  E_{2}P_{2}E_{1}P_{1},$$
but this expression is of no use. Indeed, what we need is $M^{-1}$ ; when no permutations are needed, it turns out that $M^{-1}$ can be obtained immediately from the matrices $E_{k}’s$, in fact, from their inverses, and no multiplications are necessary.
Remark: Instead of looking for an invertible matrix $M$ so that $MA$ is upper-triangular, we can look for an invertible matrix $M$ so that $MA$ is a diagonal matrix. Only a simple change to Gaussian elimination is needed. At every Stage $k$, after the pivot has been found and pivoting been performed, if necessary, in addition to adding suitable multiples of the kth row to the rows below row $k$ in order to zero the entries in column $k$ for $i = k + 1, \dots  , n$, also add suitable multiples of the kth row to the rows above row $k$ in order to zero the entries in column $k$ for $i = 1, \dots  , k$ - $1$. Such steps are also achieved by multiplying on the left by elementary matrices $E_{i,k;\beta i,k}$, except that $i < k$, so that these matrices are not lower-triangular matrices. Nevertheless, at the end of the process, we find that $A_{n} = MA$, is a diagonal matrix. This method is called the Gauss-Jordan factorization. Because it is more expensive than Gaussian elimination, this method is not used much in practice. However, Gauss-Jordan factorization can be used to compute the inverse of a matrix $A$. Indeed, we find the jth column of $A^{-1}$ by solving the system $Ax^{(j)} = e_{j}$ (where $e_{j}$ is the jth canonical basis vector $\mathbb{R}^{n}$ of ). By applying Gauss-Jordan, we are led to a system of the form $D_{j}x^{(j)} = M_{j}e_{j}$, where $D_{j}$ is a diagonal matrix, and we can immediately compute $x^{(j)}$. It remains to discuss the choice of the pivot, and also conditions that guarantee that no permutations are needed during the Gaussian elimination process. We begin by stating a necessary and sufficient condition for an invertible matrix to have an LU-factorization (i.e., Gaussian elimination does not require pivoting).

## 8.4 LU-Factorization


> **Definition 8.1.** We say that an invertible matrix $A$ has an LU-factorization if it can be written as $A = LU$, where $U$ is upper-triangular invertible and $L$ is lower-triangular, with $L_{i i} = 1$ for $i = 1, \dots  , n$.

<!-- PAGE 270 -->
A lower-triangular matrix with diagonal entries equal to $1$ is called a unit lower-triangular matrix. Given an $n\times n$ matrix $A = (a_{i j})$, for any $k$ with $1 \le k \le n$, let A(1 : $k, 1$ : $k)$ denote the submatrix of $A$ whose entries are $a_{i j}$, where $1 \le i, j \le k.^{1}$ For example, if $A$ is the $5 \times  5$ matrix
$$A = \begin{pmatrix} a_{11} & a_{12} & a_{13} & a_{14} & a_{15} \\ a_{21} & a_{22} & a_{23} & a_{24} & a_{25} \\ a_{31} & a_{32} & a_{33} & a_{34} & a_{35} \\ a_{41} & a_{42} & a_{43} & a_{44} & a_{45} \\ a_{51} & a_{52} & a_{53} & a_{54} & a_{55} \end{pmatrix} ,$$
then
$$A(1 : 3, 1 : 3) = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} .$$

> **Proposition 8.2.** Let $A$ be an invertible $n \times n$-matrix. Then $A$ has an LU-factorization $A = LU$ iff every matrix A(1 : $k, 1$ : $k)$ is invertible for $k = 1, \dots  , n$. Furthermore, when $A$ has an LU-factorization, we have
$$\det(A(1 : k, 1 : k)) = \pi_{1} \pi_{2}  \cdots  \pi_{k} ,k = 1, \dots  , n,$$
where $\pi_{k}$  is the pivot obtained after $k -1$ elimination steps. Therefore, the kth pivot is given by
$$a_{11} = \det(A(1 : 1, 1 : 1))if k = 1$$
$$$$
$$\pi_{k}  =$$
$$ \frac{\det(A(1 : k, 1 : k))}{\det(A(1 : k -1, 1 : k -1))} if k = 2, \dots  , n.$$

*Proof.* First assume that $A = LU$ is an LU-factorization of $A$. We can write
$$A = \begin{pmatrix} A(1 : k, 1 : k) & A_{2} \\ A_{3} & A_{4} \end{pmatrix} = \begin{pmatrix} L_{1} & 0 \\ L_{3} & L_{4} \end{pmatrix} \begin{pmatrix} U_{1} & U_{2} \\ 0 & U_{4} \end{pmatrix} = \begin{pmatrix} L_{1}U_{1} & L_{1}U_{2} \\ L_{3}U_{1} & L_{3}U_{2} + L_{4}U_{4} \end{pmatrix} ,$$
where $L_{1}, L_{4}$ are unit lower-triangular and $U_{1}, U_{4}$ are upper-triangular. (Note, A(1 : $k, 1$ : $k), L_{1}$, and $U_{1}$ are $k \times k$ matrices; $A_{2}$ and $U_{2}$ are $k \times$ (n-k) matrices; $A_{3}$ and $L_{3}$ are $(n-k)\times k$ matrices; $A_{4}, L_{4}$, and $U_{4}$ are $(n$ - $k) \times  (n$ - $k)$ matrices.) Thus,
$$A(1 : k, 1 : k) = L_{1}U_{1},$$
and since $U$ is invertible, $U_{1}$ is also invertible (the determinant of $U$ is the product of the diagonal entries in $U$, which is the product of the diagonal entries in $U_{1}$ and $U_{4})$. As $L_{1}$ is invertible (since its diagonal entries are equal to $1)$, we see that A(1 : $k, 1$ : $k)$ is invertible for $k = 1, \dots  , n$. Conversely, assume that A(1 : $k, 1$ : $k)$ is invertible for $k = 1, \dots  , n$. We just need to show that Gaussian elimination does not need pivoting. We prove by induction on $k$ that the kth step does not need pivoting. $\overline{1}\overline{We} \overline{are} \overline{using} \overline{Matlab}\overline{’s} \overline{notation.}$

<!-- PAGE 271 -->
This holds for $k = 1$, since A(1 : $1, 1$ : $1) = (a_{1 1})$, so $a_{1 1} \neq  0$. Assume that no pivoting was necessary for the first $k$ - $1$ steps $(2 \le k \le n$ - $1)$. In this case, we have
$$E_{k-1} \cdots  E_{2}E_{1}A = A_{k},$$
where $L = E_{k-1} \cdots  E_{2}E_{1}$ is a unit lower-triangular matrix and $A_{k}(1$ : $k, 1$ : $k)$ is uppertriangular, so that $LA = A_{k}$ can be written as
$$\begin{pmatrix} L_{1} & 0 \\ L_{3} & L_{4} \end{pmatrix} \begin{pmatrix} A(1 : k, 1 : k) & A_{2} \\ A_{3} & A_{4} \end{pmatrix} = \begin{pmatrix} U_{1} & B_{2} \\ 0 & B_{4} \end{pmatrix} ,$$
where $L_{1}$ is unit lower-triangular and $U_{1}$ is upper-triangular. (Once again A(1 : $k, 1$ : $k), L_{1}$, and $U_{1}$ are $k \times  k$ matrices; $A_{2}$ and $B_{2}$ are $k \times  (n$ - $k)$ matrices; $A_{3}$ and $L_{3}$ are $(n$ - $k) \times  k$ matrices; $A_{4}, L_{4}$, and $B_{4}$ are $(n$ - $k) \times  (n$ - $k)$ matrices.) But then,
$$L_{1}A(1 : k, 1 : k)) = U_{1},$$
where $L_{1}$ is invertible (in fact, $det(L_{1}) = 1)$, and since by hypothesis A(1 : $k, 1$ : $k)$ is invertible, $U_{1}$ is also invertible, which implies that $(U_{1})_{kk} \neq  0$, since $U_{1}$ is upper-triangular. Therefore, no pivoting is needed in Step $k$, establishing the induction step. Since $det(L_{1}) = 1$, we also have $det(U_{1}) = det(L_{1}A(1$ : $k, 1$ : $k)) = det(L_{1})$ det(A(1 : $k, 1$ : $k)) =$ det(A(1 : $k, 1$ : $k))$, and since $U_{1}$ is upper-triangular and has the pivots $\pi_{1} , \dots  , \pi_{k}$  on its diagonal, we get
$$\det(A(1 : k, 1 : k)) = \pi_{1} \pi_{2}  \cdots  \pi_{k} ,k = 1, \dots  , n,$$
as claimed.
Remark: The use of determinants in the first part of the proof of Proposition 8.2 can be avoided if we use the fact that a triangular matrix is invertible iff all its diagonal entries are nonzero.

> **Corollary 8.3.** (LU-Factorization) Let $A$ be an invertible $n \times n$-matrix. If every matrix A(1 : $k, 1$ : $k)$ is invertible for $k = 1, \dots  , n$, then Gaussian elimination requires no pivoting and yields an LU-factorization $A = LU$.

*Proof.* We proved in Proposition 8.2 that in this case Gaussian elimination requires no pivoting. Then since every elementary matrix $E_{i,k;\beta}$ is lower-triangular (since we always arrange that the pivot $\pi_{k}$  occurs above the rows that it operates on), since $E_{i,k;\beta}^{-1} = E_{i,k;-\beta}$ and the $E_{k}s$ are products of $E_{i,k;\beta i,k}s$, from
$$E_{n-1} \cdots  E_{2}E_{1}A = U,$$
where $U$ is an upper-triangular matrix, we get
$$A = LU,$$
where $L = E_{1}^{-1} E_{2}^{-1} \cdots  E_{n}^{-1}$  is a lower-triangular matrix. Furthermore, as the diagonal entries of each $E_{i,k;\beta}$ are $1,^{-1}$ the diagonal entries of each $E_{k}$ are also $1$.

<!-- PAGE 272 -->

> **Example 8.1.** The reader should verify that
$$\begin{pmatrix} 2 & 1 & 1 & 0 \\ 4 & 3 & 3 & 1 \\ 8 & 7 & 9 & 5 \\ 6 & 7 & 9 & 8 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 2 & 1 & 0 & 0 \\ 4 & 3 & 1 & 0 \\ 3 & 4 & 1 & 1 \end{pmatrix} \begin{pmatrix} 2 & 1 & 1 & 0 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 2 & 2 \\ 0 & 0 & 0 & 2 \end{pmatrix}$$
is an LU-factorization. One of the main reasons why the existence of an LU-factorization for a matrix $A$ is interesting is that if we need to solve several linear systems Ax $= b$ corresponding to the same matrix $A$, we can do this cheaply by solving the two triangular systems
$$Lw = b,andUx = w.$$
There is a certain asymmetry in the LU-decomposition $A = LU$ of an invertible matrix $A$. Indeed, the diagonal entries of $L$ are all $1$, but this is generally false for $U$. This asymmetry can be eliminated as follows: if
$$D = \mathrm{diag}(u_{11}, u_{22}, \dots  , u_{nn})$$
is the diagonal matrix consisting of the diagonal entries in $U$ (the pivots), then if we let U' $= D^{-1}U$, we can write
$$A = LDU' ,$$
where $L$ is lower- triangular, U' is upper-triangular, all diagonal entries of both $L$ and U' are $1$, and $D$ is a diagonal matrix of pivots. Such a decomposition leads to the following definition.

> **Definition 8.2.** We say that an invertible $n\times n$ matrix $A$ has an LDU-factorization if it can be written as $A =$ LDU', where $L$ is lower- triangular, U' is upper-triangular, all diagonal entries of both $L$ and U' are $1$, and $D$ is a diagonal matrix. We will see shortly than if $A$ is real symmetric, then U' $= L^{\top}$. As we will see a bit later, real symmetric positive definite matrices satisfy the condition of

> **Proposition 8.2.** Therefore, linear systems involving real symmetric positive definite matrices can be solved by Gaussian elimination without pivoting. Actually, it is possible to do better: this is the Cholesky factorization. If a square invertible matrix $A$ has an LU-factorization, then it is possible to find $L$ and $U$ while performing Gaussian elimination. Recall that at Step $k$, we pick a pivot $\pi_{k}  = a_{ik}^{(k)}$ ̸ $= 0$ in the portion consisting of the entries of index $j \ge k$ of the $k$-th column of the matrix $A_{k}$ obtained so far, we swap rows $i$ and $k$ if necessary (the pivoting step), and then we zero the entries of index $j = k + 1, \dots  , n$ in column $k$. Schematically, we have the following steps:
$$\begin{pmatrix} \times & \times & \times & \times & \times \\ 0 & \times & \times & \times & \times \\ 0 & \times & \times & \times & \times \\ 0 & a_{ik}^{(k)} & \times & \times & \times \\ 0 \end{pmatrix} pivot=\Rightarrow \begin{pmatrix} \times & \times & \times & \times & \times \\ 0 & a_{ik}^{(k)} & \times & \times & \times \\ 0 & \times & \times & \times & \times \\ 0 & \times & \times & \times & \times \\ 0 \end{pmatrix} elim=\Rightarrow \begin{pmatrix} \times & \times & \times & \times & \times \\ 0 & \times & \times & \times & \times \\ 0 & 0 & \times & \times & \times \\ 0 & 0 & \times & \times & \times \\ 0 & 0 & \times & \times & \times \end{pmatrix} .$$
$$\times \times \times \times \times \times \times \times$$

<!-- PAGE 273 -->
More precisely, after permuting row $k$ and row $i$ (the pivoting step), if the entries in column $k$ below row $k$ are $\alpha_{k+1k} , \dots  , \alpha_{nk}$ , then we add $-\alpha_{jk} /\pi_{k}$  times row $k$ to row $j$; this process is illustrated below:
$$\begin{pmatrix} a_{kk}^{(k)} \\ a_{k+1k}^{(k)} \\ \vdots \\ a_{ik}^{(k)} \\ \vdots \\ a_{nk}^{(k)} \end{pmatrix} pivot=\Rightarrow \begin{pmatrix} a_{ik}^{(k)} \\ a_{k+1k}^{(k)} \\ \vdots \\ a_{kk}^{(k)} \\ \vdots \\ a_{nk}^{(k)} \end{pmatrix} = \begin{pmatrix} \pi_{k} \\ \alpha_{k+1k} \\ \vdots \\ \alpha_{ik} \\ \vdots \\ \alpha_{nk} \end{pmatrix} elim=\Rightarrow \begin{pmatrix} \pi_{k} \\ 0 \\ \vdots \\ 0 \\ \vdots \\ 0 \end{pmatrix} .$$
Then if we write $\ell_{jk}  = \alpha_{jk} /\pi_{k}$  for $j = k + 1, \dots  , n$, the kth column of $L$ is
$$\begin{pmatrix} 0 \\ \vdots \\ 0 \\ 1 \\ \ell_{k+1k} \\ \vdots \\ \ell_{nk} \end{pmatrix} .$$
Observe that the signs of the multipliers $-\alpha_{jk} /\pi_{k}$  have been flipped. Thus, we obtain the unit lower triangular matrix
$$L = \begin{pmatrix} 1 & 0 & 0 & \cdots & 0 \\ \ell_{21} & 1 & 0 & \cdots & 0 \\ \ell_{31} & \ell_{32} & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & 0 \\ \ell_{n1} & \ell_{n2} & \ell_{n3} & \cdots & 1 \end{pmatrix} .$$
It is easy to see (and this is proven in Theorem 8.5) that if the result of Gaussian elimination (without pivoting) is $U = E_{n-1} \cdots  E_{1}A$, so that $L = E_{1}^{-1} E_{2}^{-1} \cdots  E_{n-1}^{-1}$, then
$$E_{k} = \begin{pmatrix} 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 1 & 0 & \cdots & 0 \\ 0 & \cdots & -\ell_{k} & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \ddots & \vdots \\ 0 & \ell_{nk} & 0 & 1 \end{pmatrix} andE_{k}^{-1}= \begin{pmatrix} 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 1 & 0 & \cdots & 0 \\ 0 & \cdots & \ell_{k+1k} & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & \ell_{nk} & 0 & 1 \end{pmatrix} ,$$
$$\cdots -\cdots \cdots \cdots$$
so the kth column of $E_{k}^{-1}$ is the kth column of $L$.

<!-- PAGE 274 -->
Unfortunately, even though $L^{-1} = E_{n-1} \cdots  E_{2}E_{1}$, the matrices $E_{k}$ occur in the wrong order and the kth column of $L^{-1}$ is not the kth column of $E_{k}$. Here is an example illustrating the method.

> **Example 8.2.** Given
$$A = A_{1} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & -1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} ,$$
$$--$$
we have the following sequence of steps: The first pivot is $\pi_{1}  = 1$ in row $1$, and we subtract row $1$ from rows $2, 3$, and $4$. We get
$$A_{2} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 2 & 1 & 1 \end{pmatrix} L_{1} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 0 & 0 & 1 \end{pmatrix} .$$
$$---$$
The next pivot is $\pi_{2}  = -2$ in row $2$, and we subtract row $2$ from row $4$ (and add $0$ times row $2$ to row $3)$. We get
$$A_{3} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix} L_{2} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} .$$
$$-$$
The next pivot is $\pi_{3}  = -2$ in row $3$, and since the fourth entry in column $3$ is already a zero, we add $0$ times row $3$ to row $4$. We get
$$A_{4} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix} L_{3} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} .$$
$$-$$
The procedure is finished, and we have
$$L = L_{3} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} U = A_{4} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix} .$$
$$-$$
It is easy to check that indeed
$$LU = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & -1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} = A.$$
$$---$$
We now show how to extend the above method to deal with pivoting efficiently. This is the $PA = LU$ factorization.
