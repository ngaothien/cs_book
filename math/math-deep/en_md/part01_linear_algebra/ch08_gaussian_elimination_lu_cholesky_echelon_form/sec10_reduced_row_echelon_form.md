# Reduced Row Echelon Form


<!-- PAGE 301 -->
its eigenvalues must be positive. We will have to learn about the spectral theorem for symmetric matrices to establish this criterion (see Proposition 22.3). Proposition 8.11 also holds for complex Hermitian positive definite matrices, where in $(d)$, the factorization $LDL^{\top}$ is replaced by $LDL^{*}$. For more on the stability analysis and efficient implementation methods of Gaussian elimination, LU-factoring and Cholesky factoring, see Demmel $[48]$, Trefethen and Bau $[182]$, Ciarlet $[41]$, Golub and Van Loan $[83]$, Meyer $[129]$, Strang $[175, 176]$, and Kincaid and Cheney $[105]$.

## 8.10 Reduced Row Echelon Form (RREF)

Gaussian elimination described in Section 8.2 can also be applied to rectangular matrices. This yields a method for determining whether a system Ax $= b$ is solvable and a description of all the solutions when the system is solvable, for any rectangular $m \times  n$ matrix $A$. It turns out that the discussion is simpler if we rescale all pivots to be $1$, and for this we need a third kind of elementary matrix. For any $\lambda  \neq  0$, let $E_{i,\lambda}$ be the $n\times n$ diagonal matrix
$$E_{i,\lambda} = \begin{pmatrix} 1 \\ \ddots \\ 1 \\ \lambda \\ 1 \\ \ddots \\ 1 \end{pmatrix} ,$$
with $(E_{i,\lambda})_{ii} = \lambda  (1 \le i \le n)$. Note that $E_{i,\lambda}$ is also given by
$$E_{i,\lambda} = I + (\lambda  -1)e_{i i},$$
and that $E_{i,\lambda}$ is invertible with
$$E_{i,\lambda}^{-1} = E_{i,\lambda-1}.$$
Now after $k$ - $1$ elimination steps, if the bottom portion
$$(a_{kk}^{(k)} , a_{k+1k}^{(k)}, \dots  , a_{mk}^{(k)})$$
of the kth column of the current matrix $A_{k}$ is nonzero so that a pivot $\pi_{k}$  can be chosen, after a permutation of rows if necessary, we also divide row $k$ by $\pi_{k}$  to obtain the pivot $1$, and not only do we zero all the entries $i = k + 1, \dots  , m$ in column $k$, but also all the entries $i = 1, \dots  , k$ - $1$, so that the only nonzero entry in column $k$ is a $1$ in row $k$. These row operations are achieved by multiplication on the left by elementary matrices. If $a_{kk}^{(k)} = a_{k+1k}^{(k)} = \cdots  = a_{mk}^{(k)} = 0$, we move on to column $k + 1$.

<!-- PAGE 302 -->
When the kth column contains a pivot, the kth stage of the procedure for converting a matrix to rref consists of the following three steps illustrated below:
$$\begin{pmatrix} 1 & \times & 0 & \times & \times & \times & \times \\ 0 & 0 & 1 & \times & \times & \times & \times \\ 0 & 0 & 0 & \times & \times & \times & \times \\ 0 & 0 & 0 & \times & \times & \times & \times \\ 0 & 0 & 0 & a_{ik}^{(k)} & \times & \times & \times \\ 0 & 0 & 0 \end{pmatrix} pivot=\Rightarrow \begin{pmatrix} 1 & \times & 0 & \times & \times & \times & \times \\ 0 & 0 & 1 & \times & \times & \times & \times \\ 0 & 0 & 0 & a_{ik}^{(k)} & \times & \times & \times \\ 0 & 0 & 0 & \times & \times & \times & \times \\ 0 & 0 & 0 & \times & \times & \times & \times \\ 0 & 0 & 0 \end{pmatrix} rescale=\Rightarrow$$
$$\times \times \times \times \times \times \times \times$$
$$\begin{pmatrix} 1 & \times & 0 & \times & \times & \times & \times \\ 0 & 0 & 1 & \times & \times & \times & \times \\ 0 & 0 & 0 & 1 & \times & \times & \times \\ 0 & 0 & 0 & \times & \times & \times & \times \\ 0 & 0 & 0 & \times & \times & \times & \times \\ 0 & 0 & 0 \end{pmatrix} elim=\Rightarrow \begin{pmatrix} 1 & \times & 0 & 0 & \times & \times & \times \\ 0 & 0 & 1 & 0 & \times & \times & \times \\ 0 & 0 & 0 & 1 & \times & \times & \times \\ 0 & 0 & 0 & 0 & \times & \times & \times \\ 0 & 0 & 0 & 0 & \times & \times & \times \\ 0 & 0 & 0 & 0 & \times & \times & \times \end{pmatrix} .$$
$$\times \times \times \times$$
If the kth column does not contain a pivot, we simply move on to the next column. The result is that after performing such elimination steps, we obtain a matrix that has a special shape known as a reduced row echelon matrix, for short rref. Here is an example illustrating this process: Starting from the matrix
$$A_{1} = \begin{pmatrix} 1 & 0 & 2 & 1 & 5 \\ 1 & 1 & 5 & 2 & 7 \\ 1 & 2 & 8 & 4 & 12 \end{pmatrix} ,$$
we perform the following steps
$$A_{1} \longrightarrow A_{2} = \begin{pmatrix} 1 & 0 & 2 & 1 & 5 \\ 0 & 1 & 3 & 1 & 2 \\ 0 & 2 & 6 & 3 & 7 \end{pmatrix} ,$$
by subtracting row $1$ from row $2$ and row $3$;
$$A_{2} \longrightarrow \begin{pmatrix} 1 & 0 & 2 & 1 & 5 \\ 0 & 2 & 6 & 3 & 7 \\ 0 & 1 & 3 & 1 & 2 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 0 & 2 & 1 & 5 \\ 0 & 1 & 3 & 3/2 & 7/2 \\ 0 & 1 & 3 & 1 & 2 \end{pmatrix} \longrightarrow A_{3} = \begin{pmatrix} 1 & 0 & 2 & 1 & 5 \\ 0 & 1 & 3 & 3/2 & 7/2 \\ 0 & 0 & 0 & 1/2 & 3/2 \end{pmatrix} ,$$
$$--$$
after choosing the pivot $2$ and permuting row $2$ and row $3$, dividing row $2$ by $2$, and subtracting row $2$ from row $3$;
$$A_{3} \longrightarrow \begin{pmatrix} 1 & 0 & 2 & 1 & 5 \\ 0 & 1 & 3 & 3/2 & 7/2 \\ 0 & 0 & 0 & 1 & 3 \end{pmatrix} \longrightarrow A_{4} = \begin{pmatrix} 1 & 0 & 2 & 0 & 2 \\ 0 & 1 & 3 & 0 & -1 \\ 0 & 0 & 0 & 1 & 3 \end{pmatrix} ,$$

<!-- PAGE 303 -->
after dividing row $3$ by $-1/2$, subtracting row $3$ from row $1$, and subtracting $(3/2) \times$  row $3$ from row $2$. It is clear that columns $1, 2$ and $4$ are linearly independent, that column $3$ is a linear combination of columns $1$ and $2$, and that column $5$ is a linear combination of columns $1, 2, 4$. In general, the sequence of steps leading to a reduced echelon matrix is not unique. For example, we could have chosen $1$ instead of $2$ as the second pivot in matrix $A_{2}$. Nevertheless, the reduced row echelon matrix obtained from any given matrix is unique; that is, it does not depend on the the sequence of steps that are followed during the reduction process. This fact is not so easy to prove rigorously, but we will do it later. If we want to solve a linear system of equations of the form Ax $= b$, we apply elementary row operations to both the matrix $A$ and the right-hand side $b$. To do this conveniently, we form the augmented matrix $(A, b)$, which is the $m \times  (n + 1)$ matrix obtained by adding $b$ as an extra column to the matrix $A$. For example if
$$A = \begin{pmatrix} 1 & 0 & 2 & 1 \\ 1 & 1 & 5 & 2 \\ 1 & 2 & 8 & 4 \end{pmatrix} andb = \begin{pmatrix} 5 \\ 7 \\ 12 \end{pmatrix} ,$$
then the augmented matrix is
$$(A, b) = \begin{pmatrix} 1 & 0 & 2 & 1 & 5 \\ 1 & 1 & 5 & 2 & 7 \\ 1 & 2 & 8 & 4 & 12 \end{pmatrix} .$$
Now for any matrix $M$, since
$$M(A, b) = (MA, Mb),$$
performing elementary row operations on $(A, b)$ is equivalent to simultaneously performing operations on both $A$ and $b$. For example, consider the system
$$x_{1}+2x_{3}+x_{4}=5$$
$$x_{1}+x_{2}+5x_{3}+2x_{4}=7$$
$$x_{1}+2x_{2}+8x_{3}+4x_{4}=12.$$
Its augmented matrix is the matrix
$$(A, b) = \begin{pmatrix} 1 & 0 & 2 & 1 & 5 \\ 1 & 1 & 5 & 2 & 7 \\ 1 & 2 & 8 & 4 & 12 \end{pmatrix}$$
considered above, so the reduction steps applied to this matrix yield the system
$$x_{1}+2x_{3}=2$$
$$x_{2}+3x_{3}=-1$$
$$x_{4}=3.$$

<!-- PAGE 304 -->
This reduced system has the same set of solutions as the original, and obviously $x_{3}$ can be chosen arbitrarily. Therefore, our system has infinitely many solutions given by
$$x_{1} = 2 -2x_{3},x_{2} = -1 -3x_{3},x_{4} = 3,$$
where $x_{3}$ is arbitrary. The following proposition shows that the set of solutions of a system Ax $= b$ is preserved by any sequence of row operations.

> **Proposition 8.12.** Given any $m \times  n$ matrix $A$ and any vector $b \in \mathbb{R}^{m}$, for any sequence of elementary row operations $E_{1}, \dots  , E_{k}$, if $P = E_{k} \cdots  E_{1}$ and (A', b') $=$ P(A, $b)$, then the solutions of Ax $= b$ are the same as the solutions of A'x $=$ b'.

*Proof.* Since each elementary row operation $E_{i}$ is invertible, so is $P$, and since (A', b') $=$ P(A, $b)$, then A' $= PA$ and b' $=$ Pb. If $x$ is a solution of the original system Ax $= b$, then multiplying both sides by $P$ we get PAx $=$ Pb; that is, A'x $=$ b', so $x$ is a solution of the new system. Conversely, assume that $x$ is a solution of the new system, that is A'x $=$ b'. Then because A' $= PA$, b' $=$ Pb, and $P$ is invertible, we get
$$Ax = P^{-1}A'x = P^{-1}b'= b,$$
so $x$ is a solution of the original system Ax $= b$. Another important fact is this:

> **Proposition 8.13.** Given an $m\times n$ matrix $A$, for any sequence of row operations $E_{1}, \dots  , E_{k}$, if $P = E_{k} \cdots  E_{1}$ and $B = PA$, then the subspaces spanned by the rows of $A$ and the rows of $B$ are identical. Therefore, $A$ and $B$ have the same row rank. Furthermore, the matrices $A$ and $B$ also have the same (column) rank.

*Proof.* Since $B = PA$, from a previous observation, the rows of $B$ are linear combinations of the rows of $A$, so the span of the rows of $B$ is a subspace of the span of the rows of $A$. Since $P$ is invertible, $A = P^{-1} B$, so by the same reasoning the span of the rows of $A$ is a subspace of the span of the rows of $B$. Therefore, the subspaces spanned by the rows of $A$ and the rows of $B$ are identical, which implies that $A$ and $B$ have the same row rank. Proposition 8.12 implies that the systems Ax $= 0$ and Bx $= 0$ have the same solutions. Since Ax is a linear combinations of the columns of $A$ and Bx is a linear combinations of the columns of $B$, the maximum number of linearly independent columns in $A$ is equal to the maximum number of linearly independent columns in $B$; that is, $A$ and $B$ have the same rank.
Remark: The subspaces spanned by the columns of $A$ and $B$ can be different! However, their dimension must be the same. We will show in Section 8.14 that the row rank is equal to the column rank. This will also be proven in Proposition 11.15 Let us now define precisely what is a reduced row echelon matrix.

<!-- PAGE 305 -->

> **Definition 8.6.** An $m \times  n$ matrix $A$ is a reduced row echelon matrix iff the following conditions hold:
(a) The first nonzero entry in every row is $1$. This entry is called a pivot.
$(b)$ The first nonzero entry of row $i + 1$ is to the right of the first nonzero entry of row $i$.
$(c)$ The entries above a pivot are zero. If a matrix satisfies the above conditions, we also say that it is in reduced row echelon form, for short rref . Note that Condition $(b)$ implies that the entries below a pivot are also zero. For example, the matrix
$$A = \begin{pmatrix} 1 & 6 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$
is a reduced row echelon matrix. In general, a matrix in rref has the following shape:
$$\begin{pmatrix} 1 & 0 & 0 & \times & \times & 0 & 0 & \times \\ 0 & 1 & 0 & \times & \times & 0 & 0 & \times \\ 0 & 0 & 1 & \times & \times & 0 & 0 & \times \\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & \times \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & \times \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \end{pmatrix}$$
if the last row consists of zeros, or
$$\begin{pmatrix} 1 & 0 & 0 & \times & \times & 0 & 0 & \times & 0 & \times \\ 0 & 1 & 0 & \times & \times & 0 & 0 & \times & 0 & \times \\ 0 & 0 & 1 & \times & \times & 0 & 0 & \times & 0 & \times \\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & \times & 0 & \times \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & \times & \times & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \end{pmatrix}$$
$$\times$$
if the last row contains a pivot. The following proposition shows that every matrix can be converted to a reduced row echelon form using row operations.

> **Proposition 8.14.** Given any $m \times  n$ matrix $A$, there is a sequence of row operations $E_{1}, \dots  , E_{k}$ such that if $P = E_{k} \cdots  E_{1}$, then $U = PA$ is a reduced row echelon matrix.

<!-- PAGE 306 -->

*Proof.* We proceed by induction on $m$. If $m = 1$, then either all entries on this row are zero, so $A = 0$, or if $a_{j}$ is the first nonzero entry in $A$, let $P = (a_{j}^{-1}$ ) (a $1 \times  1$ matrix); clearly, PA is a reduced row echelon matrix. Let us now assume that $m \ge 2$. If $A = 0$, we are done, so let us assume that $A \neq  0$. Since $A \neq  0$, there is a leftmost column $j$ which is nonzero, so pick any pivot $\pi  = a_{ij}$ in the jth column, permute row $i$ and row $1$ if necessary, multiply the new first row by $\pi^{-1}$ , and clear out the other entries in column $j$ by subtracting suitable multiples of row $1$. At the end of this process, we have a matrix $A_{1}$ that has the following shape:
$$A_{1} = \begin{pmatrix} 0 & \cdots & 0 & 1 & * & \cdots & * \\ 0 & \cdots & 0 & 0 & * & \cdots & * \\ \vdots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 0 & 0 & * & \cdots & * \end{pmatrix} ,$$
where * stands for an arbitrary scalar, or more concisely
$$A_{1} = \begin{pmatrix} 0 & 1 & B \\ 0 & 0 & D \end{pmatrix} ,$$
where $D$ is a $(m$ - $1) \times  (n$ - $j)$ matrix (and $B$ is a $1 \times  n$ - $j$ matrix). If $j = n$, we are done. Otherwise, by the induction hypothesis applied to $D$, there is a sequence of row operations that converts $D$ to a reduced row echelon matrix R', and these row operations do not affect the first row of $A_{1}$, which means that $A_{1}$ is reduced to a matrix of the form
$$R = \begin{pmatrix} 0 & 1 & B \\ 0 & 0 & R' \end{pmatrix} .$$
Because R' is a reduced row echelon matrix, the matrix $R$ satisfies Conditions (a) and $(b)$ of the reduced row echelon form. Finally, the entries above all pivots in R' can be cleared out by subtracting suitable multiples of the rows of R' containing a pivot. The resulting matrix also satisfies Condition $(c)$, and the induction step is complete.
Remark: There is a Matlab function named rref that converts any matrix to its reduced row echelon form. If $A$ is any matrix and if $R$ is a reduced row echelon form of $A$, the second part of Proposition 8.13 can be sharpened a little, since the structure of a reduced row echelon matrix makes it clear that its rank is equal to the number of pivots.

> **Proposition 8.15.** The rank of a matrix $A$ is equal to the number of pivots in its rref $R$.
